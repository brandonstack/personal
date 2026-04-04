# Embeddings

将文本（或图像、音频）映射为稠密向量的技术。向量空间中语义相近的内容距离更近。是 RAG、语义搜索、聚类、推荐系统的基础。

## 核心概念

- **维度**：通常 384-4096 维
- **相似度度量**：余弦相似度最常用（-1 到 1，1 = 完全相同方向）
- **关键特性**：语义相似的文本 → 向量距离近；语义不同 → 距离远

## 模型分类

### 词级别 Embedding
- **Word2Vec**（2013）：词向量算术 `king - man + woman ≈ queen`
- **GloVe**：基于共现矩阵的全局统计

### 句/段落级别 Embedding（当前主流）

| 模型 | 维度 | 特点 |
|------|------|------|
| **E5-large** | 1024 | 微软，query 需加 "query:" 前缀 |
| **GTE-large** | 1024 | 阿里，通用性强 |
| **BGE-large-en** | 1024 | BAAI，中英双语 |
| **Instructor** | 768 | 可自定义 instruction |
| **text-embedding-ada-002** | 1536 | OpenAI，API 调用 |
| **text-embedding-3-large** | 3072 | OpenAI 最新，支持维度缩减 |

实验对比（Anyscale RAG production 数据）：
- `gte-large` 在学术数据集上显著优于 `ada-002`
- 开源模型在垂直领域往往超过通用 API 模型

### 多模态 Embedding
- **CLIP**（OpenAI）：图像和文本在同一向量空间
  - 可以用文本搜索图片（"a photo of a cat" → 找到猫的图片）
  - 可以用图片搜索文本

## 向量索引

高维向量的近似最近邻（ANN）搜索：

| 技术 | 原理 | 代表库 |
|------|------|--------|
| **HNSW** | 分层导航小世界图 | FAISS, Pinecone |
| **IVF** | 倒排文件索引 | FAISS |
| **ScaNN** | Google 的量化 + 重排 | ScaNN |

## 在 RAG 中的使用

```python
# 一行式 RAG（Simon Willison 的简化描述）
collection.query(query_texts=["your question"], n_results=5)
```

实际流程：
1. 离线：文档 → 分块 → embedding → 存入向量数据库
2. 在线：query → embedding → ANN 搜索 → top-K 文档 → 送入 LLM

## 实践要点

- 同一系统中 query 和 document 必须用同一个 embedding 模型
- Embedding 模型的选择对 RAG 质量影响极大——务必做 A/B 测试
- 较新的模型（E5, GTE）通常优于旧模型（ada-002），且免费
- 维度越高不一定越好，要在质量和延迟间权衡

> 来源：resources/simon-willison/20260404-embeddings-what-they-are-and-why-they-matter.md
> 来源：resources/anyscale/20260404-building-rag-based-llm-applications-for-production.md

→ [RAG Pipeline](rag-pipeline.md)
→ [Hybrid Search](hybrid-search.md)
