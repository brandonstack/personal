# RAG Evaluation

评估 RAG 系统质量的方法论。需要分别评估检索质量和生成质量，以及端到端效果。

## 评估维度

### 检索质量
- **Recall@K**：top-K 结果中包含相关文档的比例
- **Precision@K**：top-K 中实际相关的文档占比
- **MRR（Mean Reciprocal Rank）**：第一个相关结果的排名倒数的均值
- **nDCG**：考虑位置加权的排名质量

### 生成质量
- **Faithfulness**：回答是否忠实于检索到的上下文（不幻觉）
- **Relevance**：回答是否回答了用户问题
- **Completeness**：回答是否覆盖了所有要点

### 端到端
- **Answer correctness**：最终答案是否正确
- **Citation accuracy**：引用来源是否正确

## 评估方法

### LLM-as-Judge
Anyscale 生产实践中使用 GPT-4 作为评估者：
- 给定 (query, context, answer, reference_answer)
- 让 GPT-4 从多个维度打分（1-5）
- 成本远低于人工评估，一致性更高
- 需要注意评估 prompt 的设计和 calibration

### 人工评估
- 小规模抽样，做 LLM-as-Judge 的校验
- 关注 LLM 评估者容易遗漏的问题（逻辑错误、细微幻觉）

### 自动化 metrics
- BLEU/ROUGE：词级别重叠，粗糙但快速
- BERTScore：语义级别相似度
- 适合做回归测试，不适合做质量判断

## Anyscale 的 RAG 评估实践

1. 准备 evaluation dataset：(query, reference_answer, reference_sources)
2. 对每个配置变体（chunk size, embedding model, top-K）运行 pipeline
3. 用 LLM-as-Judge 评分
4. 比较不同配置的平均分

关键发现：
- Chunk size 100-300 chars 在他们的学术数据集上最优
- `gte-large` embedding 显著优于 `ada-002`
- Top-K=5 是较好的平衡点

## 实践要点

- 先建 evaluation dataset（哪怕 50 条），再调优
- 不要只看一个 metric——faithfulness 和 relevance 可能矛盾
- LLM-as-Judge 要做 calibration（和人工评估对比一致性）
- → [Eval Driven Development](../ai-eval-safety/eval-driven-development.md) 的理念同样适用于 RAG

> 来源：resources/anyscale/20260404-building-rag-based-llm-applications-for-production.md
> 来源：resources/eugene-yan/20260404-untitled.md

→ [RAG Pipeline](rag-pipeline.md)
→ [LLM Evaluation Methods](../ai-eval-safety/llm-evaluation-methods.md)
→ [Eval Driven Development](../ai-eval-safety/eval-driven-development.md)
