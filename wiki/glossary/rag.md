# RAG (Retrieval-Augmented Generation)

先检索相关资料，再让 LLM 基于检索结果生成回答的技术模式。

## 解决什么问题

LLM 的知识有截止日期，也不知道你的私有数据。RAG 的做法是：用户提问 → 从知识库中检索相关文档片段 → 把这些片段塞进 prompt → LLM 基于这些真实资料回答。这样 LLM 就能回答它训练数据中没有的内容，同时减少幻觉。

## 基本流程

```
用户提问 → 向量检索（从知识库找相关内容）
              ↓
         拼接 prompt（问题 + 检索到的文档片段）
              ↓
         LLM 生成回答
```

## 局限

- 检索质量决定回答质量（garbage in, garbage out）
- 文档切分粒度影响检索精度
- 对于需要跨多个文档综合推理的问题效果有限

## 在本 wiki 的语境

wiki 中提到 RAG 主要是与 Agent 的知识管理对比：RAG 是"被动检索"，Agent + 知识库（如 Compound Engineering）是"主动积累"。两者互补但解决不同问题。

→ 深度阅读：[rag-retrieval/rag-pipeline](../rag-retrieval/rag-pipeline.md) — 完整 RAG 技术栈
→ 深度阅读：[llm-knowledge-bases](../knowledge-management/llm-knowledge-bases.md) — RAG vs 知识积累
