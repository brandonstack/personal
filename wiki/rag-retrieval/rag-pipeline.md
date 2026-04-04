# RAG Pipeline

Retrieval-Augmented Generation：给 LLM 接上外部知识库，先检索相关文档再生成回答。解决 LLM 知识截止日期、幻觉、领域特定知识不足的问题。

## 标准 Pipeline

```
用户问题 → Query Processing → Retrieval → Reranking → Context Assembly → LLM Generation → 回答
```

### 1. 文档预处理
- **分块（Chunking）**：→ [Chunking Strategies](chunking-strategies.md)
- **Embedding**：→ [Embeddings](embeddings.md)
- **索引**：存入向量数据库（FAISS, Pinecone, Chroma, Weaviate）

### 2. 检索
- **语义搜索**：query embedding 与文档 embedding 的余弦相似度
- **关键词搜索**：BM25（稀疏检索）
- **混合搜索**：→ [Hybrid Search](hybrid-search.md)
- 典型 top-K：20-150 候选

### 3. Reranking
- 用 cross-encoder 对 (query, document) 对重新打分
- 比 bi-encoder 更准但更慢（不能预计算）
- 典型流程：top-150 → reranker → top-20
- 配合 Contextual Retrieval 可减少 67% 检索失败率

### 4. Context Assembly
- 将 top-K 文档拼入 prompt
- 控制总长度（避免超出上下文窗口 / 稀释注意力）
- 可以按相关性排序、去重、添加元数据

### 5. Generation
- 带 context 的 prompt 送入 LLM
- 可以要求 LLM 标注来源（citation）

## 进阶架构

| 方法 | 原理 |
|------|------|
| **HyDE** | 先让 LLM 生成假设性答案，用假设答案做 embedding 检索 |
| **Contextual Retrieval** | 为每个 chunk 添加上下文前缀再 embedding → [详见](contextual-retrieval.md) |
| **Agentic RAG** | Agent 自主决定何时检索、检索什么、是否需要多轮检索 |
| **Self-RAG** | 模型自我评估是否需要检索、检索结果是否相关 |
| **RETRO** | 在 transformer 层内嵌入检索模块，训练时就用检索 |

## 评估

→ [RAG Evaluation](rag-evaluation.md)

## 实践要点

- 先做好检索质量，再优化生成——"garbage in, garbage out"
- Embedding 模型选择对结果影响巨大（gte-large > ada-002 在多数学术任务上）
- 100-500 字符的 chunk size 通常最优，太小丢失上下文，太大引入噪音
- 生产环境必须有 evaluation pipeline

> 来源：resources/anyscale/20260404-building-rag-based-llm-applications-for-production.md
> 来源：resources/pinecone/20260404-untitled.md
> 来源：resources/anthropic/20260404-untitled.md
> 来源：resources/eugene-yan/20260404-untitled.md

→ [Embeddings](embeddings.md)
→ [Contextual Retrieval](contextual-retrieval.md)
→ [glossary/RAG](../glossary/rag.md)
