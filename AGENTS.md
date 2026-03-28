# AGENTS.md

本 repo 使用 Claude Code 作为 AI 交互层。

## Agent 行为准则

### 信息摄入
- Feed 脚本（`scripts/ingest/`）是自动化工具，Agent 不主动运行
- Agent 可以帮助 review inbox 内容、总结文章、提取要点

### 知识整理
- Agent 可以建议将 inbox 内容归类到哪个 area
- **不要自动移动文件** — 始终由用户确认后操作
- 整理后的内容写入 `areas/<area>/` 或 `projects/<project>/`

### 写作风格
- 中英混用，技术术语保留英文
- 不要加 emoji（除非用户要求）
- 简洁直接，不要客套废话

### 文件操作
- 只编辑用户指定的文件，不要主动创建文档
- 不要修改 `scripts/` 里的代码，除非用户要求
- 不要删除 inbox 里的文件