# LLM-as-Judge

用 LLM（通常是 GPT-4）来评估另一个 LLM 的输出质量。在人工评估太贵、自动 metrics 太粗糙时，作为中间方案。

## 工作原理

给评估 LLM 一个结构化 prompt：
```
请评估以下回答的质量。

问题：{question}
参考答案：{reference}（可选）
模型回答：{response}

请从以下维度打分（1-5）：
- Relevance（相关性）
- Faithfulness（忠实度）
- Completeness（完整性）

并给出理由。
```

## G-Eval 框架

Liu et al. (2023) 提出的 LLM-as-Judge 方法论：
1. 让 LLM 先生成评估步骤（Chain-of-Thought）
2. 再按步骤打分
3. 使用 token probabilities 做加权平均（而非直接取生成的数字）
- 与人类判断的 Spearman 相关系数达到 0.514（显著优于传统 metrics）

## 优势与局限

### 优势
- 比人工评估便宜 10-100 倍
- 一致性高（同样输入得到相似分数）
- 可以 24/7 自动化运行
- 可以评估开放式输出（人工 metrics 做不到的）

### 局限
- **Position bias**：偏好放在前面的答案
- **Self-enhancement bias**：偏好与自身风格相似的输出
- **Length bias**：偏好更长的回答
- **对微妙错误不敏感**：逻辑错误、细微幻觉可能被忽略

## 实践要点

- 用 GPT-4 作为 judge 是当前 golden standard（用更弱的模型评估更强的模型不可靠）
- **必须做 calibration**：用人工标注的子集校验 LLM judge 的一致性
- 多次评估取平均可以降低随机性
- 评估 prompt 的措辞对结果影响很大——需要迭代优化

## Anyscale 生产案例

在 RAG production 中使用 LLM-as-Judge：
- 评估 (query, retrieved_context, generated_answer) 三元组
- 从 relevance, faithfulness, completeness 三个维度打分
- 用于对比不同 RAG 配置（chunk size, embedding model, top-K）

> 来源：resources/hamel-husain/20260404-untitled.md
> 来源：resources/anyscale/20260404-building-rag-based-llm-applications-for-production.md
> 来源：resources/eugene-yan/20260404-untitled.md

→ [LLM Evaluation Methods](llm-evaluation-methods.md)
→ [Eval Driven Development](eval-driven-development.md)
