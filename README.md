# Personal

个人事务管理，PARA 方法论组织。

## 结构

- **projects/** — 有明确目标的项目（完成后归档到 archive/）
- **areas/** — 长期持续的生活领域（career, finance, health, travel, learning, home, habits）
- **resources/** — 参考资料库（pending/ = 待消化，其余 = 已处理原文）
- **wiki/** — LLM 维护的知识库 + 消化报告
- **archive/** — 已完成项目归档

## Feed 摄入

```bash
# 同步订阅源到 feed CLI
python3 .ingest/sync-feeds.py --fetch

# 摄入最近 24h 文章到 resources/pending/
python3 .ingest/feed-to-inbox.py --hours 24
```

## 工作流

1. Feed 脚本定期摄入 → `resources/pending/`
2. `/compile` 消化 → 更新 `wiki/` + 生成 `wiki/reports/` + 移到 `resources/`
3. 有价值的内容手动整理到 `areas/` 或 `projects/`
4. 项目完成后归档到 `archive/`
