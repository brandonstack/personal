# LLM Production Patterns

Eugene Yan 总结的 LLM 应用生产化 7 大模式。覆盖从评估到上线后运维的全生命周期。

## 七大模式

### 1. Evals（评估）
→ [Eval Driven Development](eval-driven-development.md)
- 一切的起点。没有 eval 就无法量化改进

### 2. RAG（检索增强生成）
→ [RAG Pipeline](../rag-retrieval/rag-pipeline.md)
- 给模型接上最新的、领域特定的知识

### 3. Fine-tuning（微调）
→ [Fine-tuning Methods](../ml-fundamentals/fine-tuning-methods.md)
- 当 prompting + RAG 不够时的下一步

### 4. Caching（缓存）
减少延迟和成本的关键手段：
- **精确缓存**：完全相同的 query 命中缓存
- **语义缓存**：语义相似的 query 命中缓存（用 embedding 相似度判断）
- **预计算缓存**：高频 query 预先生成答案
- 常见能减少 30-50% 的 API 调用

### 5. Guardrails（护栏）
防止 LLM 输出不当内容或格式错误：

| 类型 | 说明 | 示例 |
|------|------|------|
| 结构化 | 强制输出格式 | JSON schema validation |
| 语法 | 检查语言质量 | 语法检查、拼写检查 |
| 语义 | 检查内容质量 | 事实核查、相关性检查 |
| 安全 | 过滤有害内容 | 毒性检测、PII 检测 |

- 输入侧 guardrail（过滤恶意 prompt）+ 输出侧 guardrail（过滤有害回答）

### 6. Defensive UX（防御性用户体验）
设计 UI 来管理 LLM 的不确定性：
- 明确告知用户"AI 可能出错"
- 提供 "thumbs up/down" 反馈机制
- 展示置信度或来源
- 限制高风险操作的自动化程度
- 提供人类接管的出口

### 7. Collect Feedback（反馈收集飞轮）
- 隐式反馈：用户是否采纳建议、是否编辑输出
- 显式反馈：点赞/踩、评分、评论
- 反馈用于：改进 eval dataset、fine-tuning、发现新 failure mode
- 形成**数据飞轮**：更多用户 → 更多反馈 → 更好模型 → 更多用户

## 模式间的关系

```
Evals ←→ RAG / Fine-tuning（eval 指导选择和优化）
Guardrails ← Evals（eval 发现的问题变成 guardrail 规则）
Feedback → Evals（用户反馈扩充 eval dataset）
Caching ← 观察到的高频 query patterns
```

## 实践要点

- 这 7 个模式不需要同时实现——按优先级逐步加入
- 推荐顺序：Evals → RAG/Guardrails → Caching → Feedback → Fine-tuning
- Defensive UX 从第一天就应该有

> 来源：resources/eugene-yan/20260404-untitled.md

→ [Eval Driven Development](eval-driven-development.md)
→ [RAG Pipeline](../rag-retrieval/rag-pipeline.md)
