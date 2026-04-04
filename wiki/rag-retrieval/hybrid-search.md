# Hybrid Search

结合语义搜索（dense retrieval）和关键词搜索（sparse retrieval）的检索方法。两者互补：语义搜索擅长同义词和概念匹配，关键词搜索擅长精确术语和罕见词。

## 两种检索的对比

| 维度 | 语义搜索（Dense） | 关键词搜索（Sparse / BM25） |
|------|-------------------|---------------------------|
| 匹配方式 | 向量余弦相似度 | 词频 × 逆文档频率 |
| 优势 | 同义词、意译、概念级匹配 | 精确术语、缩写、专有名词 |
| 劣势 | 对罕见词/新词效果差 | 不理解同义词和语义 |
| 计算 | 需要 embedding + ANN 索引 | 倒排索引，成熟高效 |

## 融合方法

### Reciprocal Rank Fusion (RRF)
最常用的简单融合：
```
RRF_score(d) = Σ 1/(k + rank_i(d))
```
- k 通常 = 60
- 对每个检索系统的排名取倒数再求和
- 不需要归一化分数，只用排名

### 加权分数融合
```
score = α × dense_score + (1-α) × sparse_score
```
- α 需要调参（通常 0.5-0.7）
- 需要归一化两种分数

## 在 Contextual Retrieval 中的效果

Anthropic 实验数据：

| 方法 | 检索失败率降低 |
|------|---------------|
| Contextual Embedding only | 35% |
| **Contextual Embedding + BM25** | **49%** |
| Contextual Embedding + BM25 + Reranking | 67% |

BM25 的加入带来额外 14% 的改善——在语义检索的盲区（精确术语、缩写等）上补位。

## 支持 Hybrid Search 的平台

- **Pinecone**：原生支持 dense + sparse 向量
- **Weaviate**：BM25 + vector 融合
- **Elasticsearch**：k-NN + BM25
- **手动实现**：分别调用两个检索器 + RRF 融合

## 实践要点

- 几乎总是应该用 hybrid search，纯语义搜索在生产环境不够鲁棒
- BM25 是极其成熟的技术，几乎零额外成本
- RRF 是最稳健的融合方式（不需要调权重）
- 先确认 BM25 baseline，再加 dense retrieval——很多时候 BM25 已经很好

> 来源：resources/anthropic/20260404-untitled.md
> 来源：resources/pinecone/20260404-untitled.md

→ [RAG Pipeline](rag-pipeline.md)
→ [Contextual Retrieval](contextual-retrieval.md)
→ [Embeddings](embeddings.md)
