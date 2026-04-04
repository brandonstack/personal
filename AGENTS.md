# AGENTS.md

本 repo 使用 Claude Code 作为 AI 交互层。

## Agent 行为准则

### 信息摄入
- Feed 脚本（`scripts/ingest/`）是自动化工具，Agent 不主动运行
- Agent 可以帮助 review inbox 内容、总结文章、提取要点

### Wiki 维护
- Agent 是 `wiki/` 的全权维护者 — 创建、修改、重组 wiki 文件无需用户逐条确认
- 但 Agent 生成的 report 必须提交给用户审阅
- wiki 内容必须标注来源（resources 文件或对话日期）
- 更新 wiki 时同步更新 `_index.md`
- wiki 文件是概念文档，不是文章摘要
- 更新 wiki 或 compile 时，检查文章中引用的术语是否已在 `wiki/glossary/` 有条目，缺失则补充

### Areas 写入
- `areas/` 仍然是用户确认过的内容
- 对话中用户明确表达的个人决策/想法，可以写入 areas/（无需额外确认）
- LLM 主动建议写入 areas/ 时，需要用户确认

### 文件操作
- `wiki/` 下的文件：Agent 可自由创建、修改、删除、重组
- `areas/` 下的文件：需要用户确认后操作
- `inbox/` 下的文件：compile 时标记 `status: compiled` 后移到 `resources/`（保持目录结构）
- `resources/` 下的文件：只读，不修改不删除
- `reports/` 下的文件：Agent 创建新 report，不修改已有 report
- 不要修改 `scripts/` 里的代码，除非用户要求

### 写作风格
- 中英混用，技术术语保留英文
- 不要加 emoji（除非用户要求）
- 简洁直接，不要客套废话
