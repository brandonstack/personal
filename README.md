# Personal

个人事务管理，PARA 方法论组织。

## 结构

- **projects/** — 有明确目标的项目（完成后归档到 archive/）
- **areas/** — 长期持续的生活领域（finance, health, travel, learning, home）
- **inbox/** — 信息摄入：feed 文章、待消化内容（按来源分目录）
- **archive/** — 已完成项目归档
- **scripts/** — 自动化脚本（feed 摄入等）

## Feed 摄入

```bash
# 同步订阅源到 feed CLI
python3 scripts/ingest/sync-feeds.py --fetch

# 摄入最近 24h 文章到 inbox/
python3 scripts/ingest/feed-to-inbox.py --hours 24
```

## 工作流

1. Feed 脚本定期摄入 → `inbox/`
2. 有价值的内容手动整理到 `areas/` 或 `projects/`
3. 项目完成后归档到 `archive/`
