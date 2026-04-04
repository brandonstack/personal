# LLM Evaluation Methods

评估 LLM 系统质量的方法论。从自动化 metrics 到人工评估，从单元测试到 A/B 测试，分层构建评估体系。

## 三层评估体系

Hamel Husain 提出的分层模型：

### Level 1: Unit Tests（断言测试）
- 最快、最便宜、最先建
- 测试格式正确性、关键词包含、长度限制、安全过滤
- 例：`assert "sorry" not in response` / `assert len(response) < 500`
- 适合做 CI/CD 回归测试

### Level 2: Human / Model Eval（质量评估）
- **LLM-as-Judge**：→ [LLM-as-Judge](llm-as-judge.md)
- **人工评估**：小规模抽样，校验 LLM 评估结果
- 典型频率：每次重大变更

### Level 3: A/B Testing（在线评估）
- 真实用户流量对比
- 衡量业务指标（留存率、任务完成率、用户满意度）
- 最接近真实质量，但最慢、成本最高
- **Chatbot Arena** 是最大规模的在线 LLM 评估平台 → 众包 pairwise 对比 + Elo rating

## 自动化 Metrics

| Metric | 类型 | 适用场景 |
|--------|------|---------|
| BLEU | N-gram 精确率 | 翻译（已过时） |
| ROUGE | N-gram 召回率 | 摘要 |
| BERTScore | 语义相似度 | 通用文本质量 |
| MoverScore | 最优传输距离 | 通用文本质量 |

这些 metrics 与人类判断相关性有限，适合做回归检测（"是否变差了"），不适合做质量判断（"够不够好"）。

## Elo Rating（Chatbot Arena）

LMSYS 的众包评估方法：
1. 匿名展示两个模型的回答
2. 用户选择更好的那个（或平局）
3. 按 Elo 算法更新评分
- 截至 2024 年已收集 1M+ 投票
- 优势：反映真实用户偏好，不受 benchmark gaming 影响
- 局限：无法评估特定能力维度

## 实践要点

- 评估是迭代的——先 Level 1，有能力后加 Level 2，有流量后加 Level 3
- 评估数据集要**代表真实用例**，不是学术 benchmark
- 投入在评估上的时间回报最高——比盲目调参有效得多

> 来源：resources/hamel-husain/20260404-untitled.md
> 来源：resources/lmsys/20260404-chatbot-arena-benchmarking-llms-in-the-wild-with-e.md
> 来源：resources/eugene-yan/20260404-untitled.md

→ [LLM-as-Judge](llm-as-judge.md)
→ [Eval Driven Development](eval-driven-development.md)
→ [RAG Evaluation](../rag-retrieval/rag-evaluation.md)
