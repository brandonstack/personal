# Embeddings

将文本（或图像、音频）映射为稠密向量的技术。语义相近的内容在向量空间中距离更近。RAG、语义搜索、聚类的基础。

## 解决什么问题

计算机不能直接理解文本的"意义"。Embeddings 把文本变成数字向量，让"相似度"可以用数学计算（余弦相似度）。

## 关键模型

主流 sentence embedding：E5, GTE, BGE（开源）；text-embedding-3（OpenAI API）。多模态：CLIP（图文统一空间）。

→ 深度阅读：[rag-retrieval/embeddings](../rag-retrieval/embeddings.md)
