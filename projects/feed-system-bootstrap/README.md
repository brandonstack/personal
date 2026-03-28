# Feed 系统启动

> 启动日期: 2026-03-28
> 目标: 把已配置好的 feed 摄入系统跑起来，建立定期 review 习惯

## 背景

`scripts/ingest/` 里已经有完整的 feed 同步和摄入脚本，`sources.yaml` 配置了 9 个订阅源（5 播客 + 2 博客 + 2 新闻聚合），但还没有真正运行过，inbox/ 是空的。

## 步骤

- [ ] 首次运行 `python3 scripts/ingest/sync-feeds.py --fetch`
- [ ] Dry run 测试 `python3 scripts/ingest/feed-to-inbox.py --dry-run --hours 48`
- [ ] 正式运行，检查 inbox/ 的产出质量
- [ ] 调优 filter（keywords、min-points）
- [ ] 建立 review 节奏（每周？每天？）
- [ ] 确认哪些 source 产出好、哪些需要调整或替换

## 完成标准

- feed 系统稳定运行 2 周
- inbox/ 有持续内容产出
- 至少 review 过一批文章，有内容被提炼到 areas/ 或 projects/
- 完成后归档，feed 系统成为日常基建

---

*Created: 2026-03-28*
