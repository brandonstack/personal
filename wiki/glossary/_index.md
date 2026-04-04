# Glossary

快速查阅 wiki 中频繁出现的概念。每个条目用几句话说清"是什么"和"解决什么问题"，深度分析链接到对应的长文。

## 索引

**Agent 核心**
- [Agent Loop](agent-loop.md) — Agent 的基本运行循环
- [ACI](aci.md) — Agent-Computer Interface
- [AIG](aig.md) — Agent Interaction Guidelines
- [RAG](rag.md) — Retrieval-Augmented Generation

**ML/DL 基础**
- [Transformer](transformer.md) — 基于 attention 的序列建模架构
- [KV Cache](kv-cache.md) — 自回归推理的 Key/Value 缓存优化
- [Embeddings](embeddings.md) — 文本到稠密向量的映射

**协议与工具**
- [MCP](mcp.md) — Model Context Protocol
- [Deferred Tools](deferred-tools.md) — 延迟加载工具机制
- [LSP](lsp.md) — Language Server Protocol

**推理优化**
- [Continuous Batching](continuous-batching.md) — 动态批处理，iteration-level scheduling
- [PagedAttention](paged-attention.md) — KV Cache 的非连续内存管理

**工作流与框架**
- [gstack](gstack.md) — Garry Tan 的 Claude Code 角色化工作流
- [Compound Engineering](compound-engineering.md) — 跨 session 知识积累
- [Plan-First](plan-first.md) — 先规划再执行的工作模式
- [Evaluator-Generator](evaluator-generator.md) — 评估驱动的迭代循环

**演进线索**
- [Prompt → Context → Harness](prompt-context-harness.md) — 三代范式演进
