# Personal — Dev Guide for Claude Code

## What This Is

个人 mono repo，PARA 方法论组织生活事务 + LLM 维护的知识库 + 自动化信息摄入。

## Structure

```
personal/
├── inbox/             # 未处理的输入队列（自动摄入 + 手动 fetch），compiled 后移到 resources/
├── wiki/              # LLM 全权维护的知识库（概念原子化，按主题分目录）
│   ├── _index.md      # 全局索引（LLM 维护）
│   └── <topic>/       # 按主题分目录（如 harness-engineering/, claude-code/）
│       └── _index.md  # 子目录索引（LLM 维护）
├── reports/           # LLM 生成的消化报告（供用户审阅和对话）
├── resources/         # 已处理的参考资料（inbox compiled 后移入，原文存档，被 wiki 和 areas 引用）
├── areas/             # 长期持续的个人生活领域（career, finance, health, travel, learning, home）
├── projects/          # 有明确目标的项目（完成后归档到 archive/）
├── archive/           # 已完成项目归档
└── scripts/
    └── ingest/        # Feed 摄入脚本
        ├── sources.yaml       # 订阅源配置
        ├── sync-feeds.py      # 同步 sources → feed CLI DB
        ├── feed-to-inbox.py   # 拉取 entries → inbox/<source>/
        └── fetch-url.py       # 单篇 URL 抓取（Jina Reader）
```

## Feed Ingestion

```bash
# 同步订阅源到 feed CLI
python3 scripts/ingest/sync-feeds.py --fetch

# 摄入最近 24h 文章到 inbox/
python3 scripts/ingest/feed-to-inbox.py --hours 24

# Dry run（不写文件）
python3 scripts/ingest/feed-to-inbox.py --dry-run --hours 48
```

依赖：`pyyaml`，`feed` CLI（Go）

## URL Fetch + Translate

```bash
# Claude Code skill（推荐）：抓取 + 自动翻译
/fetch-url <url> --source SOURCE --tags tag1,tag2

# 仅抓取原文（不翻译）
python3 scripts/ingest/fetch-url.py <url> --source SOURCE --tags tag1,tag2 [--date YYYY-MM-DD] [--no-translate] [--dry-run]
```

产出两个文件：`inbox/<source>/YYYYMMDD-<slug>.md`（原文）+ `-zh.md`（中文翻译+summary+comments）。
使用 fetch-skill 自动路由抓取：普通网页（Jina Reader + fallback）、Twitter/X（FxTwitter）、微信公众号（wechat-exporter）。
fetch-skill 未安装时自动降级为 Jina Reader。

## Inbox Note Format

文件路径：`inbox/<source-slug>/YYYYMMDD-<title-slug>.md`

```yaml
---
source: "Simon Willison"
url: "https://..."
date: "2026-03-28"
tags: [AI, engineering]
status: "raw"
---
```

去重：按 `url` 字段扫描同 source 目录下已有文件。

## Workflow

1. Feed 脚本 / fetch-url 摄入 → `inbox/`
2. `/compile` — LLM 批量消化 inbox 文件 → 更新 `wiki/` + 生成 `reports/` + 移到 `resources/`
3. 用户审阅 report → 对话讨论 → 有价值的内容回流到 `wiki/` 或 `areas/`
4. 每次对话都可能增强 wiki（复合效应）

## Wiki

`wiki/` 是 LLM 全权维护的知识库。人不直接编辑 wiki 文件，所有更新通过 `/compile` 或对话回流完成。

### Wiki Rules

- wiki 文件由 LLM 创建和维护，人通过审阅 report + 对话来影响内容
- 每个子目录一个 `_index.md`，由 LLM 自动维护（文件列表 + 摘要 + 核心概念 + 跨主题连接）
- **概念原子化**：一个文件 = 一个概念，50-150 行，自包含。判断标准：问"什么是 X"只需读一个文件
- **概念去重**：一个概念只在一个地方定义（single source of truth），其他地方通过 `→ [wiki/xxx]` 链接引用
- wiki 文件必须标注来源：`> 来源：resources/xxx/yyy.md` 或 `> 来源：对话 YYYY-MM-DD`
- 文件超过 150 行时拆分为更细的概念
- 新主题超过 3 个相关文件时，建新子目录
- wiki 内容是**概念文档**（像 wiki 词条），不是文章摘要
- **Glossary 补全**：wiki 文章中引用的术语/概念，如果 `glossary/` 里没有对应条目，需要补充。compile 时和更新 wiki 时都应检查

### Wiki 与 Areas 的区别

- `wiki/`：通用知识、框架、模式、工具用法 — LLM 全权维护
- `areas/`：个人生活决策、计划、目标、反思 — 人确认后才写入

## Key Rules

- `inbox/` 是待处理的输入队列，compiled 后出队移到 `resources/`
- `resources/` 是已处理的原文参考（从 inbox 毕业），被 wiki 和 areas 引用
- `wiki/` 是 LLM 维护的知识库，概念原子化，跨来源综合
- `reports/` 是消化报告，供用户审阅和对话
- `areas/` 和 `projects/` 是人确认过的个人内容
- Markdown 文件中英混用，保持自然

## Honesty Rules

- **wiki 内容必须标注来源。** 每个知识点追溯到具体的 resources 文件或对话日期
- **区分 LLM 分析和用户观点：** wiki 里的内容是 LLM 从材料中提取的，不代表用户认同。只有用户在对话中明确表达的观点才能标注为用户确认
- **report 中的建议是建议，不是事实。** report 的「对你的具体建议」部分是 LLM 的推断，需要用户审阅
- **宁可留空，不可虚构。** 如果材料不够得出某个结论，就说不够，不要编
- **写周记/日记时，只基于有明确证据的事实：** git commits、status 变更、areas/ 和 projects/ 中的实际改动。推测的内容必须标注为推测

## Areas Content Rules

- 每个文件聚焦一个话题，文件名是话题的 slug（英文、小写、连字符）
- 文件超过 80 行或涵盖两个以上独立话题时，应该拆分
- README.md 只做索引，不放实际内容。格式：`- [文件名](文件名.md) — 一行说明`
- area 下新增内容时，先看 README 索引有没有合适的文件可以追加，没有再新建
- 文件名不用泛标题（❌ mental-health.md），用具体话题（✅ anxiety-reframing.md）
