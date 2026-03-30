# Personal — Dev Guide for Claude Code

## What This Is

个人 mono repo，PARA 方法论组织生活事务 + 自动化信息摄入。

## Structure

```
personal/
├── inbox/             # 未处理的输入（自动摄入 + 手动 fetch），status: raw → digested
├── resources/         # 已处理的参考资料（从 inbox promote 后移过来，被 areas 引用）
│   └── <topic>/       # 按话题自由分类（如 ai-engineering/, mental-health/）
├── areas/             # 长期持续的生活领域（career, finance, health, travel, learning, home）
├── projects/          # 有明确目标的项目（完成后归档到 archive/）
├── archive/           # 已完成项目归档
└── scripts/
    └── ingest/        # Feed 摄入脚本
        ├── sources.yaml       # 订阅源配置
        ├── sync-feeds.py      # 同步 sources → feed CLI DB
        └── feed-to-inbox.py   # 拉取 entries → inbox/<source>/
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

1. Feed 脚本定期摄入 → `inbox/`（status: raw）
2. `/digest <inbox-file>` — 在 inbox 文件末尾追加消化内容（骨架、苏格拉底问题、连接、行动），status → digested
3. 回答苏格拉底问题，在文件末尾写个人思考
4. `/promote <inbox-file>` — 精华写入 `areas/`，文件移到 `resources/<topic>/`，status → promoted

## Key Rules

- `inbox/` 是待处理的输入队列，量大，机器写的
- `resources/` 是已处理的参考资料，按话题分类，被 areas/ 引用
- `areas/` 和 `projects/` 是人确认过的内容
- 不要自动移动或删除 inbox 里的文件（只有 `/promote` 执行移动）
- Markdown 文件中英混用，保持自然

## Areas Content Rules

- 每个文件聚焦一个话题，文件名是话题的 slug（英文、小写、连字符）
- 文件超过 80 行或涵盖两个以上独立话题时，应该拆分
- README.md 只做索引，不放实际内容。格式：`- [文件名](文件名.md) — 一行说明`
- area 下新增内容时，先看 README 索引有没有合适的文件可以追加，没有再新建
- 文件名不用泛标题（❌ mental-health.md），用具体话题（✅ anxiety-reframing.md）
