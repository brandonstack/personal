# 统一内容摄入 & 处理管线设计

## Context

当前 PKM 系统有四个 skill（`/fetch-url`, `/digest`, `/ingest`, `/promote`）和 Python 脚本处理 RSS 摄入，但存在几个问题：

1. **播客没有处理流程** — `sources.yaml` 里有 5 个播客源标了 `transcribe: true`，但没有转录脚本，resources/pending/podcast/ 里的文件只有 show notes，没有 transcript
2. **Web clip 不规范** — `resources/pending/clippings/` 里文件命名混乱（中文标题、无日期前缀），frontmatter 不统一
3. **没有自动评分/分类** — 所有内容进 resources/pending 后 status 永远是 raw，无法快速 triage
4. **翻译时机不对** — `/fetch-url` 每次都翻译，但大部分 RSS 文章不会被读，浪费资源
5. **没有触发机制** — 一切都是手动的，没有 cron，没有自动化

用户希望设计一个统一的管线，覆盖播客、web clip、RSS 文章，加上自动评分/分类，并用小龙虾（Claude Code `--print` 模式）作为触发端。

---

## 设计方案

### 一、统一文件组织

**保持 `resources/pending/<source>/` 结构不变**，用 frontmatter `type` 字段区分内容类型，不用目录区分。

```
resources/pending/
├── <source>/                          # 按来源（不变）
│   ├── YYYYMMDD-<slug>.md             # 主文件（原文或 show notes）
│   ├── YYYYMMDD-<slug>-zh.md          # 中文翻译（可选）
│   └── YYYYMMDD-<slug>.transcript.md  # 完整转录（仅播客）
├── clippings/                         # Web clip（统一命名后）
└── _archive/                          # 低分自动归档
```

**命名规范**：所有文件统一 `YYYYMMDD-<slug>.md`，播客转录加 `.transcript.md` 后缀。

**为什么转录单独一个文件？** 转录 5000-30000 字，内联在主文件里 Obsidian 打开很慢，Git diff 巨大。主文件 frontmatter 里 `transcript:` 字段指向转录文件。

### 二、统一 Frontmatter Schema

在现有字段基础上扩展：

```yaml
---
# === 身份 ===
type: "article" | "podcast" | "clip" | "rss"    # NEW
source: "Simon Willison"
url: "https://..."
date: "2026-04-02"

# === 生命周期 ===
status: "raw" | "scored" | "digested" | "promoted"  # 新增 "scored" 阶段
score: 0.82                    # NEW: 相关性评分 0-1
score_reason: "与 agent 架构直接相关"  # NEW: 评分理由
summary: "一句话摘要..."        # NEW: AI 生成的摘要

# === 分类 ===
tags: [AI, agents]             # 已有，自动补充
topics: [agent-architecture]   # NEW: 更细粒度的话题
lang: "en"                     # NEW: 主语言
has_translation: false         # NEW: 是否有 -zh.md

# === 播客专用（可选）===
audio: "https://..."
duration: "01:23:45"
transcript: "YYYYMMDD-slug.transcript.md"  # 指向转录文件
---
```

### 三、处理管线

```
内容到达 (raw) → /score (scored) → 人工 triage → /digest (digested) → /promote (promoted)
                    ↑                                    ↑
                  自动化                              半自动
```

#### Stage 0: 到达（按类型不同）

| 类型 | 触发 | 产出 |
|------|------|------|
| RSS 文章 | cron → `feed-to-inbox.py` | `resources/pending/<source>/YYYYMMDD-slug.md` |
| 手动文章 | 用户 `/fetch-url`（不再自动翻译） | `resources/pending/<source>/YYYYMMDD-slug.md` |
| 播客 | cron → `feed-to-inbox.py` 检测 podcast 类型 | stub `.md` + 异步 Whisper API 转录 |
| Web clip | Obsidian Web Clipper 插件 | `resources/pending/clippings/<title>.md`（Clipper 格式） |

#### Stage 1: `/score`（NEW，自动化）

读取文件内容（播客读 transcript），对照 `areas/` 目录和最近 promoted 的内容，产出：
- `score`: 0-1 评分
- `summary`: 1-2 句摘要
- `topics`: 话题分类
- `tags`: 补充标签
- `status: scored`

**评分维度**：
- 与 areas/ 的相关性（40%）
- 可行动性（30%）
- 新颖性 vs resources/ 已有内容（20%）
- 来源权威度（10%）

#### Stage 2: `/digest`（已有，增强）

增强点：
- 播客类型：额外生成 `## 关键引述`（带时间戳）
- 如果 `has_translation: false` 且 `score > 0.7`，先调 `/translate` 再 digest

#### Stage 3: `/promote`（已有，不变）

### 四、新增/修改 Skill

#### 新增 `/score`
- **文件**: `.claude/commands/score.md`
- **allowed-tools**: `Read, Edit, Glob, Grep`
- **输入**: 文件路径或 glob pattern
- **行为**: 读文件 + areas/ 上下文 → 评分 → 更新 frontmatter
- **评分标准**: 内嵌在 skill prompt 里（见上方维度）

#### ~~`/clip` — 不需要~~
Web clip 由 Obsidian Web Clipper 插件完成，直接存入 `resources/pending/clippings/`。
Clipper 产出的 frontmatter 格式不同（`title`, `source`, `author`, `published`, `created`, `description`, `tags: [clippings]`），`/score` 需要兼容。

#### 新增 `/translate`
- **文件**: `.claude/commands/translate.md`
- **allowed-tools**: `Bash(claude:*), Read, Edit`
- **输入**: 文件路径
- **行为**: 从 `/fetch-url` 中提取翻译逻辑为独立 skill
- **修改 `/fetch-url`**: 默认行为改为调 `/translate`，保持向后兼容

#### 新增 `/triage`
- **文件**: `.claude/commands/triage.md`
- **allowed-tools**: `Read, Write, Glob, Grep`
- **输入**: 无
- **行为**: 扫描所有 `status: scored` 的文件，按 score 排序，生成 `resources/pending/TRIAGE.md`

#### 新增 `/sweep`
- **文件**: `.claude/commands/sweep.md`
- **allowed-tools**: `Read, Edit, Glob, Grep, Bash(mv:*), Bash(mkdir:*)`
- **输入**: 无（或 `--dry-run`）
- **行为**:
  - `score < 0.3` 且 >14 天 → 移入 `resources/pending/_archive/`
  - `scored` 状态超 3 天且 `score > 0.7` → 在 TRIAGE.md 标注提醒
  - 汇报统计数据

#### 修改 `/digest`
- 识别 `type: podcast` → 读取 `.transcript.md` → 额外生成关键引述+时间戳

#### 新增 `.ingest/transcribe.py`
- **输入**: 播客 stub 文件路径（读取 `audio` 字段）
- **行为**: 下载音频 → Whisper API (OpenAI/Azure) 转录 → 写 `.transcript.md` → 更新 stub frontmatter
- **方案**: Whisper API（在职期间用 Azure 额度，离职后用 OpenAI API key）
- **备注**: 用户订阅的播客大多是中文的，Whisper 对中文支持良好

### 五、触发模型

```
┌─────────────┬──────────────┬───────────────────────────────┐
│ 触发方式     │ 频率         │ 执行内容                       │
├─────────────┼──────────────┼───────────────────────────────┤
│ Cron (RSS)  │ 每 4 小时    │ feed-to-inbox.py              │
│             │              │ → /score 新 raw 文件           │
│             │              │ → /triage 更新阅读队列          │
├─────────────┼──────────────┼───────────────────────────────┤
│ Cron (播客) │ 每 6 小时    │ transcribe.py                 │
│             │              │ （检查 transcript: null 的 stub）│
├─────────────┼──────────────┼───────────────────────────────┤
│ Cron (清理) │ 每天早 6 点  │ /sweep → /triage              │
├─────────────┼──────────────┼───────────────────────────────┤
│ 手动        │ 用户触发     │ /fetch-url, /clip, /digest    │
│             │              │ /promote, /translate, /score   │
└─────────────┴──────────────┴───────────────────────────────┘
```

**小龙虾 (Claude Code `--print`) 作为触发端**：

```bash
# crontab 条目
# RSS 摄入 + 评分 + triage（每4小时）
0 */4 * * * cd /path/to/personal && python3 .ingest/feed-to-inbox.py --hours 4 && claude --print "对 resources/pending 里所有 status: raw 的文件运行 /score，然后运行 /triage"

# 播客转录（每6小时）
0 */6 * * * cd /path/to/personal && python3 .ingest/transcribe.py

# 每日清理（早6点）
0 6 * * * cd /path/to/personal && claude --print "/sweep 然后 /triage"
```

### 六、实施顺序

#### Phase 1: 基础 skill（本周）
1. 创建 `/score` skill → `.claude/commands/score.md`
2. 从 `/fetch-url` 中提取 `/translate` skill → `.claude/commands/translate.md`
3. 更新 `/fetch-url` 默认改为不翻译，用户想翻译时手动 `/translate`
4. 更新 CLAUDE.md 文档

**注意**: `/clip` 不需要做——Web Clipper 插件已经处理了。`/score` 需要兼容两种 frontmatter 格式：
- fetch-url 产出的：`source`, `url`, `date`, `tags`
- Web Clipper 产出的：`title`, `source`, `author`, `published`, `created`, `description`, `tags: [clippings]`

#### Phase 2: 播客管线（下周）
5. 创建 `.ingest/transcribe.py`（Whisper API）
6. 修改 `feed-to-inbox.py` 支持播客 stub 创建
7. 增强 `/digest` 支持播客类型

#### Phase 3: 自动化（5 月）
8. 创建 `/triage` skill + `resources/pending/TRIAGE.md`
9. 创建 `/sweep` skill
10. 配置 cron jobs
11. 在 Dashboard.md 加 triage 视图（Dataview 查询 scored 文件）

#### Phase 4: 迭代（6 月）
12. 根据 2 个月数据调优评分标准和阈值
13. 迁移现有 clippings 文件命名（批量 rename 脚本）
14. 可选：Obsidian Dataview dashboard 增强

### 七、关键文件清单

| 操作 | 文件路径 |
|------|----------|
| 新建 | `.claude/commands/score.md` |
| 新建 | `.claude/commands/translate.md` |
| 新建 | `.claude/commands/triage.md` |
| 新建 | `.claude/commands/sweep.md` |
| 新建 | `.ingest/transcribe.py` |
| 修改 | `.claude/commands/digest.md` — 增加播客支持 |
| 修改 | `.claude/commands/fetch-url.md` — 默认不翻译，翻译改为调 /translate |
| 修改 | `.ingest/feed-to-inbox.py` — 支持播客 stub |
| 修改 | `CLAUDE.md` — 更新 workflow 文档 |
| 修改 | `projects/pkm-polish/README.md` — 更新项目进度 |
| 修改 | `Dashboard.md` — 加 triage 视图（可选） |

### 八、验证方式

1. **`/score` 测试 (fetch-url 格式)**: 对现有 pending 文件运行 `/score resources/pending/anthropic/20260328-harness-design-long-running-apps.md`，验证 score/summary/topics 写入 frontmatter
2. **`/score` 测试 (Web Clipper 格式)**: 对 clippings 文件运行 `/score "resources/pending/clippings/Agent Interaction Guidelines (AIG) – Linear Developers.md"`，验证兼容 Clipper frontmatter
3. **`/translate` 测试**: 对一个未翻译的文件运行 `/translate resources/pending/clippings/...`，验证 `-zh.md` 生成
4. **`/fetch-url` 回归测试**: 运行 `/fetch-url <url>`，验证不再自动翻译
5. **播客转录测试**: 手动对一个 podcast stub 运行 `transcribe.py`，验证 `.transcript.md` 生成
6. **`/digest` 播客测试**: 对有 transcript 的播客运行 `/digest`，验证生成关键引述+时间戳
7. **端到端**: cron 模拟 — 手动运行 `feed-to-inbox.py` → `/score` 批量 → `/triage` → 检查 `TRIAGE.md`
