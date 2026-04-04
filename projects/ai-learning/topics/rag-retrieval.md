---
topic: "RAG & Retrieval Systems"
status: "curating"
hours_budget: 15
target_wiki_dir: "rag-retrieval"
---

# RAG & Retrieval Systems

从 prompt engineering 到生产级 RAG pipeline。理解 embedding、向量检索、chunking 策略、hybrid search，能设计和评估一个 RAG 系统。

## 学习目标

- [ ] 理解 RAG 基本架构：indexing → retrieval → generation
- [ ] 能解释 embedding 模型如何工作、如何选型
- [ ] 理解 chunking 策略对检索质量的影响
- [ ] 了解 vector DB 选型（Pinecone, Weaviate, Chroma, pgvector）
- [ ] 理解 hybrid search（dense + sparse）和 reranking
- [ ] 能识别 RAG 常见故障模式并知道如何诊断

## Tier 1 — 必读

| # | 标题 | URL | Source | 说明 | Status |
|---|------|-----|--------|------|--------|
| 1 | Retrieval Augmented Generation (RAG) | https://docs.anthropic.com/en/docs/build-with-claude/retrieval-augmented-generation | Anthropic | 官方 RAG 指南，权威起点 | ✅ |
| 2 | Building RAG-based LLM Applications | https://www.anyscale.com/blog/a-comprehensive-guide-for-building-rag-based-llm-applications-part-1 | Anyscale | 端到端 RAG 构建指南 | ✅ |
| 3 | Pinecone: What is RAG? | https://www.pinecone.io/learn/retrieval-augmented-generation/ | Pinecone | 清晰的 RAG 概念讲解 + 架构图 | ✅ |
| 4 | Chunking Strategies for RAG | https://www.pinecone.io/learn/chunking-strategies/ | Pinecone | Chunking 策略对比和最佳实践 | ✅ |
| 5 | A Guide to Embeddings | https://simonwillison.net/2023/Oct/23/embeddings/ | Simon Willison | 工程师视角的 embedding 入门 | ✅ |
| 6 | Contextual Retrieval | https://www.anthropic.com/news/contextual-retrieval | Anthropic | Anthropic 的 contextual retrieval 方法 | ✅ |
| 7 | Patterns for Building LLM-based Systems | https://eugeneyan.com/writing/llm-patterns/ | Eugene Yan | LLM 系统模式总览，RAG 在全局中的位置 | ✅ |

## Tier 2 — 推荐

| # | 标题 | URL | Source | 说明 | Status |
|---|------|-----|--------|------|--------|
| 1 | LangChain RAG Tutorial | https://python.langchain.com/docs/tutorials/rag/ | LangChain | 实操向 RAG 教程 | ⬜ |
| 2 | MTEB Embedding Leaderboard | https://huggingface.co/spaces/mteb/leaderboard | Hugging Face | Embedding 模型选型参考 | ⬜ |
| 3 | Advanced RAG Techniques | https://blog.llamaindex.ai/a-cheat-sheet-and-some-recipes-for-building-advanced-rag-803a9d94c41b | LlamaIndex | 高级 RAG 技巧 cheat sheet | ⬜ |
| 4 | Vector Database Comparison | https://superlinked.com/vector-db-comparison | Superlinked | 向量数据库功能对比表 | ⬜ |
| 5 | Hybrid Search Explained | https://www.pinecone.io/learn/hybrid-search-intro/ | Pinecone | Dense + Sparse 混合检索 | ⬜ |

## Fetch Commands

```bash
python3 .ingest/batch-fetch.py projects/ai-learning/topics/rag-retrieval.md --tier 1
```

## Wiki Output

（compile 后填入）
