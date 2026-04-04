# Knowledge Sprint — Topic Index

> 大规模主题摄入，按 topic 策划 URL → 批量 fetch → compile → wiki

## 进度总览

| Topic | 预算 | Tier 1 | Tier 2 | Status |
|-------|------|--------|--------|--------|
| [ML/DL Fundamentals](ml-fundamentals.md) | 25h | 8 URLs | 6 URLs | curating |
| [RAG & Retrieval](rag-retrieval.md) | 15h | 7 URLs | 5 URLs | curating |
| [AI Eval & Safety](ai-eval-safety.md) | 15h | 7 URLs | 5 URLs | curating |
| [Agent SDK & Harness](agent-harness.md) | 20h | 8 URLs | 5 URLs | curating |
| [AI Infra & Deployment](ai-infra.md) | 15h | 7 URLs | 5 URLs | curating |

## 工作流

1. **策划** — topic 文件中填入 Tier 1/2/3 URL 列表
2. **批量 fetch** — `python3 .ingest/batch-fetch.py topics/<topic>.md [--tier 1]`
3. **Compile** — `/compile` 消化 → wiki + reports
4. **审阅** — 读 report，对话讨论，知识回流
5. **标记完成** — 更新 topic status

## Status 含义

- `not-started` — 还没开始
- `curating` — 正在策划 URL 列表
- `fetching` — 正在批量抓取
- `compiling` — 正在 compile 到 wiki
- `done` — 完成，wiki 已更新
