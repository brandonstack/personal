# AIG (Agent Interaction Guidelines)

Linear 团队提出的 Agent 人机交互设计原则，定义 Agent 在产品中应该如何与用户互动。

## 解决什么问题

Agent 不再只是开发工具里的 coding assistant，它正进入产品（项目管理、客服、协作）。但 Agent 在产品中该怎么表现？什么时候该自主行动，什么时候该问人？AIG 给出了五条基础原则。

## 五原则概要

1. **可预测** — 用户能预期 Agent 会做什么
2. **可控制** — 用户能随时介入、修正、叫停
3. **透明** — Agent 的推理过程和行动对用户可见
4. **谨慎** — 高风险操作需要确认，低风险可自主
5. **可审计** — 所有行动有记录，可追溯

## 与 Harness 的关系

AIG 的原则可以直接映射到 Harness 设计：可控制 → 权限治理，可审计 → 日志系统，谨慎 → Tool Governance 的分级策略。

→ 深度阅读：[agent-interaction-design](../agent-architecture/agent-interaction-design.md)
