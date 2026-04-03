# Agent 交互设计

当 Agent 从开发工具走进产品和协作流程，人机交互契约需要重新定义。Linear 的 Agent Interaction Guidelines (AIG) 提出了五条基础原则。

## AIG 五原则

| 原则 | 要求 | 为什么重要 |
|------|------|-----------|
| **Agent 必须表明身份** | 清晰标识，不能被误认为人 | 人需要知道交互对象是谁，才能校准信任和期望 |
| **原生栖息于平台** | 使用平台已有的 UI 和操作模式 | 减少认知负担，Agent 不应创造全新的交互范式 |
| **状态透明** | 清晰展示思考中/等待输入/执行中/完成 | 沉默导致不确定性；用户需要一眼判断进度 |
| **尊重退出请求** | 被要求停止时立即停止 | Agent 不应自作主张继续，人的控制权高于一切 |
| **Agent 不能被问责** | 最终责任归属人类 | 明确的委托模型——Agent 执行任务，人承担后果 |

关键设计含义：
- 被调用时立即给反馈（"Thinking..."），消除等待不确定性
- 推理过程完全可检查（tool calls、prompts、decision logic）
- 人-Agent 委派关系在 UI 中可视化（谁委托、谁负责）

## 自动驾驶等级模型

Justineo 提出的 AI 编程自动驾驶等级：

| 等级 | 描述 | 代表工具 | 交互模式 |
|------|------|----------|----------|
| L0 | 完全人工 | — | 人写所有代码 |
| L1 | 行内自动补全 | TabNine / Copilot | 逐行确认 |
| L2 | 代码片段生成 | Copilot / Cursor | 段落级确认 |
| L3 | Agent 执行，人 review | Claude Code / Codex | 结果级审查 |
| L4 | Agent + AI review | — | 异常时人介入 |
| L5 | AI 工程团队 | — | 人定义目标 |

**关键洞察**：L3 开始，瓶颈从"写代码"变成"code review"。信任需要慢慢建立才能往 L4 发展——这不是技术问题，是人机信任的渐进过程。

## "默认不信任快"

> 用了 AI 以后，反而开始信任"慢"。"快"给人不踏实的感觉——AI 是不是跳过了什么？"慢"说明它在认真思考、在做 research、在 plan。

这和人的直觉一致：三秒给你答案的人，你信吗？

## 与 Harness 的关系

AIG 的五原则可以映射到 Harness 设计：
- "状态透明" → Harness 的可观测性层（Trace、事件流）
- "Agent 不能被问责" → Evaluator-Generator 分离（人是 evaluator，Agent 是 generator）
- "尊重退出" → Tool governance 的权限系统（人随时可以收回控制权）

→ [control-flow-patterns.md](control-flow-patterns.md) — Agent Loop 中人的干预点
→ [agentic-coding-risks.md](agentic-coding-risks.md) — 为什么交互设计很重要（Agent 的风险需要人来兜底）
→ [../claude-code/workflow-patterns.md](../claude-code/workflow-patterns.md) — Plan-first 是 L3 级别人机协作的最佳实践

> 来源：resources/clippings/Agent Interaction Guidelines (AIG) – Linear Developers.md
> 来源：resources/work-with-ai/20260329-working-with-ai-justineo.md
