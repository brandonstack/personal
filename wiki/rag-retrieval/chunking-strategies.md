# Chunking Strategies

RAG 中将文档切分为可检索片段的方法。Chunk size 和 chunking 策略直接影响检索质量和生成效果。

## 常用方法

### 固定大小分块
- 按字符数 / token 数切分
- 可设置 overlap（如 100 字符重叠）防止语义断裂
- 简单高效，适合非结构化文本

### 语义分块（Semantic Chunking）
- 用 embedding 相似度检测语义边界
- 相邻句子相似度骤降处切分
- 效果更好但计算成本更高

### 结构化分块
- 按文档结构切分（标题、段落、章节）
- 适合有明确结构的文档（技术文档、论文、法律合同）
- 保持逻辑完整性

### 递归分块
- LangChain 默认：先按段落分，段落太长按句子分，句子太长按字符分
- 尽量保持大块，只在必要时细分

## Chunk Size 的影响

Anyscale 在 RAG production 中的实验（100-900 字符）：

| Chunk Size | 特点 |
|-----------|------|
| 100-200 chars | 精确匹配，但丢失上下文；检索需要更多 chunks |
| 300-500 chars | 通常最优区间——足够的上下文，合理的精确度 |
| 500-900 chars | 上下文丰富，但引入不相关信息；embedding 质量可能下降 |

**没有普适最优值**——必须根据具体数据集和任务做评估。

## 与 Contextual Retrieval 的配合

→ [Contextual Retrieval](contextual-retrieval.md) 通过给 chunk 添加上下文前缀，部分缓解了小 chunk 丢失上下文的问题。这意味着可以用更小的 chunk（更精确）而不必担心上下文丢失。

## 实践要点

- 先用固定大小 + overlap 跑基线
- 尝试 2-3 种 chunk size，用 evaluation pipeline 量化比较
- 结构化文档优先用结构化分块
- Overlap 通常设为 chunk size 的 10-20%
- 考虑在 chunk 中保留元数据（来源文件名、章节标题）

> 来源：resources/anyscale/20260404-building-rag-based-llm-applications-for-production.md
> 来源：resources/anthropic/20260404-untitled.md

→ [RAG Pipeline](rag-pipeline.md)
→ [Contextual Retrieval](contextual-retrieval.md)
