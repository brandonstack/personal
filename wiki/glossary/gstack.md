# gstack

Y Combinator CEO Garry Tan 开源的 Claude Code skills 集合，用角色化 slash commands 模拟一支完整的工程团队。

## 解决什么问题

单独用 Claude Code 时，你是在和"一个全能但没有明确职责的 Agent"对话。gstack 把不同职责拆成独立的 slash commands，每个命令背后是一个专门角色，有自己的 system prompt 和评审标准。

## 主要角色

| 命令 | 角色 | 职责 |
|------|------|------|
| `/plan-ceo-review` | CEO | 产品方向和用户价值把关 |
| `/plan-eng-review` | 工程经理 | 架构和技术方案把关 |
| `/qa` | QA | 浏览器实测 + 自动验证 |

## 与 Compound Engineering 的互补

gstack 覆盖**决策层和审查层**（做之前审，做之后查），CE 覆盖**知识层**（做完之后记）。两者合起来构成完整的 Harness 架构。

→ 深度阅读：[compound-engineering](../harness-engineering/compound-engineering.md)（含 gstack + CE 全栈覆盖表）
