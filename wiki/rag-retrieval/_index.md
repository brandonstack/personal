# RAG & Retrieval

检索增强生成的完整技术栈：从 embedding 到检索到生成。覆盖标准 pipeline、前沿优化（Contextual Retrieval）、评估方法。

## 文件

- [rag-pipeline.md](rag-pipeline.md) — RAG 标准 pipeline：分块 → 嵌入 → 检索 → 重排 → 生成
- [embeddings.md](embeddings.md) — Embedding 模型选择、向量索引（FAISS/HNSW）、多模态 embedding
- [contextual-retrieval.md](contextual-retrieval.md) — Anthropic 的 chunk 上下文增强技术，67% 检索失败率降低
- [chunking-strategies.md](chunking-strategies.md) — 分块策略对比、chunk size 实验数据
- [hybrid-search.md](hybrid-search.md) — Dense + Sparse 混合检索、RRF 融合
- [rag-evaluation.md](rag-evaluation.md) — RAG 评估方法、LLM-as-Judge、Anyscale 实践

## 核心概念

- **RAG**：给 LLM 接上外部知识库，先检索再生成
- **Contextual Retrieval**：为 chunk 添加上下文前缀后再 embedding，显著提升检索质量
- **Hybrid Search**：语义 + 关键词检索互补，几乎总是优于单一检索
- **Reranking**：cross-encoder 重排序，检索质量的最后一道提升

## 跨主题连接

- → [ml-fundamentals/](../ml-fundamentals/) — Transformer encoder 产生 embedding
- → [ai-eval-safety/](../ai-eval-safety/) — RAG 评估方法与 LLM 评估方法共通
- → [ai-infra/](../ai-infra/) — 向量检索的基础设施需求
- → [harness-engineering/](../harness-engineering/) — RAG 是 harness 的常见组件
- → [glossary/RAG](../glossary/rag.md) — RAG 术语定义
