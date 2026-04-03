# Agent Architecture

Agent 系统设计的核心模块：控制流、工具设计、多 Agent 编排、评测、风险管理、人机交互。

## 文件

- [control-flow-patterns.md](control-flow-patterns.md) — 五种控制模式、Agent Loop 核心机制、上下文分层、任务象限
- [tool-design-evolution.md](tool-design-evolution.md) — 三代工具设计演进（API→ACI→Advanced）、MCP vs CLI、动态发现
- [multi-agent-patterns.md](multi-agent-patterns.md) — 指挥者 vs 统筹者、通信协议、隔离、安全边界
- [evaluation-systems.md](evaluation-systems.md) — Task/Trial/Grader 三层结构、Pass@k vs Pass^k、评分器类型、可观测性
- [agentic-coding-risks.md](agentic-coding-risks.md) — 错误复合、复杂性贩子、低召回率、AI 创造力边界、应对策略
- [agent-interaction-design.md](agent-interaction-design.md) — Linear AIG 五原则、L0-L5 自动驾驶等级、人机信任渐进

## 核心概念

- **Workflow vs Agent**：执行路径代码写死 = Workflow，LLM 动态决定 = Agent
- **ACI（Agent-Computer Interface）**：面向 Agent 目标的工具设计，不是底层 API 封装
- **MCP vs CLI**：CLI = 内环（速度、可组合），MCP = 外环（互操作、治理）
- **Pass@k vs Pass^k**：前者验证能力边界（开发），后者保证上线质量（回归）
- **错误复合**：Agent 不学习 + 无瓶颈 → 微小错误以不可持续的速率积累
- **AIG**：Agent Interaction Guidelines，人机协作的基础契约
- **L3 瓶颈**：Agent 执行 + 人 review 阶段，瓶颈从写代码变成 code review

## 跨主题连接

- → [harness-engineering/](../harness-engineering/) — Agent 系统需要 Harness 来保证可靠性；Harness 比模型更关键
- → [claude-code/](../claude-code/) — Claude Code 是 Agent 架构概念的完整产品实现
- → [knowledge-management/](../knowledge-management/) — Agent 的知识层设计（LLM Knowledge Bases）
- → [ai-engineering/](../ai-engineering/) — Agent 风险与应对影响 AI 工程师的定位和技能要求
