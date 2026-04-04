# Evaluator-Generator

一种迭代循环模式：Generator 生成输出，Evaluator 评估质量，不合格就打回重做，直到通过。

## 解决什么问题

LLM 单次输出的质量不稳定（1-5% 错误率）。Evaluator-Generator 用"检查 → 修复"的循环来逼近正确结果，类似 TDD（测试驱动开发）的思路——先定义"什么是对的"，再迭代直到满足标准。

## 在 Agent 中的两种形态

1. **连续运行** — Generator 边写代码边跑测试，发现失败立即修复（如 Claude Code 的 verification agent）
2. **结束时评审** — 代码写完后，独立的 Evaluator agent 做全面 review，发现问题再回 Generator 修

## 关键洞察

评估器本身也需要校准。Anthropic 的做法：找人类判断和 Evaluator 判断不一致的例子 → 更新评估标准 → 重复。经过多轮才能达到合理水平。

## 类比

代码 review 流程：开发写代码（Generator），reviewer 提意见（Evaluator），开发改完再提交，直到 approved。

→ 深度阅读：[evaluator-generator 深度分析](../harness-engineering/evaluator-generator.md)、[evaluation-systems](../agent-architecture/evaluation-systems.md)
