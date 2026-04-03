# Knowledge Management

知识库架构、LLM 辅助知识管理、复合循环、Wiki 模式。

## 文件

- [llm-knowledge-bases.md](llm-knowledge-bases.md) — Karpathy 模式：raw→compile→wiki→Q&A→回流、复合循环、为什么不需要 RAG

## 核心概念

- **LLM Knowledge Base**：用 LLM 编译和维护个人知识库（raw→compile→wiki→Q&A→回流）
- **复合循环**：每次查询/对话都增强知识库，知识 compound——不是线性积累而是复合增长
- **Wiki 模式**：LLM 维护的 .md 文件集合，自动索引，概念原子化，人很少直接编辑
- **Index 优于 RAG**：在中等规模（~400K words）下，好的文件组织 + index > 向量搜索

## 跨主题连接

- → [agent-architecture/](../agent-architecture/) — Agent 的知识层就是 knowledge management 问题
- → [harness-engineering/](../harness-engineering/) — Harness 的 memory/state 管理本质是知识治理
- → [harness-engineering/compound-engineering.md](../harness-engineering/compound-engineering.md) — Compound Engineering 是复合循环在代码 session 中的实现
- → [claude-code/plugins-ecosystem.md](../claude-code/plugins-ecosystem.md) — CE 插件的知识提取架构
