# Contextual Retrieval

Anthropic 提出的 RAG 优化技术：在 embedding 之前，为每个 chunk 生成一段简短的上下文描述（50-100 tokens），补充 chunk 在原文档中的语境信息。

## 核心问题

标准 RAG 分块后，每个 chunk 失去了全局上下文：
- "公司 Q3 收入增长 2%" — 哪个公司？哪年？
- "该方法在测试集上达到 95% 准确率" — 什么方法？什么数据集？

检索时 query 和 chunk 之间的语义匹配度因此下降。

## 解决方案

在 embedding/索引之前，用 LLM 为每个 chunk 生成上下文前缀：

```
原始 chunk: "Q3 收入增长 2%，主要由广告业务驱动"

上下文前缀: "这段内容来自 Acme Corp 2024 年度报告的财务摘要部分。
Acme 是一家全球科技公司，主营业务包括广告、云计算和硬件。"

最终 chunk: [上下文前缀] + [原始 chunk]
```

然后对拼接后的文本做 embedding 和索引。

## 效果数据

Anthropic 的实验结果：

| 方法 | 检索失败率降低 |
|------|---------------|
| Contextual Embedding only | 35% |
| Contextual Embedding + BM25 (hybrid) | 49% |
| Contextual Embedding + BM25 + Reranking | **67%** |

最佳组合：Contextual Retrieval + Hybrid Search + Reranking → top-20 检索失败率降低 67%。

## 成本分析

为每个 chunk 调用 LLM 生成上下文——看似昂贵，实际可控：

- 利用 **prompt caching**：同一文档的所有 chunk 共享相同的文档上下文 prompt
- Prompt caching 后写入成本仅 $1.02/million tokens
- 一次性索引成本，后续检索不再增加

## 实践要点

- 上下文长度控制在 50-100 tokens，太长会稀释 chunk 本身的信号
- 结合 BM25 hybrid search 效果提升显著（关键词匹配补充语义检索盲区）
- Reranking 是最后一道提升（cross-encoder），必须加
- 适合中大型知识库（数千+ 文档），小型知识库可能不值得

> 来源：resources/anthropic/20260404-untitled.md

→ [RAG Pipeline](rag-pipeline.md)
→ [Hybrid Search](hybrid-search.md)
→ [Chunking Strategies](chunking-strategies.md)
