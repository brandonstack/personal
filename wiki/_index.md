# Wiki — LLM 维护的知识库

本目录由 LLM 全权维护。人通过审阅 report + 对话来影响内容，不直接编辑。

## 主题目录

| 目录 | 说明 | 文件数 | 最后更新 |
|------|------|--------|----------|
| [harness-engineering/](harness-engineering/) | Harness 设计模式：包裹 LLM 的运行时系统 | 4 | 2026-04-03 |
| [claude-code/](claude-code/) | Claude Code 架构、context 管理、工具治理、skill 设计、工作流 | 8 | 2026-04-03 |
| [agent-architecture/](agent-architecture/) | 控制流、工具设计、多 Agent 编排、评测、风险、人机交互 | 6 | 2026-04-03 |
| [knowledge-management/](knowledge-management/) | LLM 知识库、复合循环、Wiki 模式、案例研究 | 2 | 2026-04-03 |
| [ai-engineering/](ai-engineering/) | AI 工程通用框架、定位模型、能力迁移 | 1 | 2026-04-03 |
| [dev-tools/](dev-tools/) | 开发工具与工作流：Git Worktree 等 | 1 | 2026-04-03 |

## 跨主题核心概念

- **Harness**：包裹 LLM 的运行时系统，管理 context、tool、state → [harness-engineering/](harness-engineering/)
- **三代范式**：Prompt → Context → Harness，每代包含前代但核心问题不同 → [harness-engineering/](harness-engineering/)
- **Evaluator-Generator 分离**：harness 核心模式，也是 AI 工程能力迁移的关键 → [harness-engineering/](harness-engineering/) + [ai-engineering/](ai-engineering/)
- **Compound Engineering**：跨 session 知识积累，备忘录 vs 知识库 → [harness-engineering/](harness-engineering/) + [knowledge-management/](knowledge-management/)
- **Agent 环境设计**：工程师从写代码变为设计 Agent 工作环境 → [harness-engineering/](harness-engineering/)
- **Claude Code 作为 Harness 实现**：Claude Code 的 6 层架构是 harness 三支柱的具体案例 → [claude-code/](claude-code/) + [harness-engineering/](harness-engineering/)
- **Context 经济学**：200K token 预算分配、MCP 隐形成本、deferred tools 优化 → [claude-code/](claude-code/)
- **对抗性验证**："try to break it" 哲学，evaluator-generator 在工具级别的实现 → [claude-code/](claude-code/) + [harness-engineering/](harness-engineering/)
- **Plan-First 工作流**：规划 2h → 执行 10min → 审查 1h → [claude-code/](claude-code/)
- **Skill 作为可分发 prompt**：Anthropic 内部 9 大类别，社区插件生态 → [claude-code/](claude-code/)
- **ACI 工具设计**：三代演进（API→ACI→Advanced），MCP vs CLI 双通道 → [agent-architecture/](agent-architecture/)
- **Pass@k vs Pass^k**：开发阶段验证能力边界 vs 上线质量保证 → [agent-architecture/](agent-architecture/)
- **Agentic Coding 风险**：错误复合、复杂性贩子、低召回率、AI 创造力边界 → [agent-architecture/](agent-architecture/)
- **Agent Interaction Guidelines**：Linear AIG 五原则、L0-L5 自动驾驶等级 → [agent-architecture/](agent-architecture/)
- **LLM Knowledge Bases**：Karpathy 模式，raw→compile→wiki→Q&A→回流，复合循环 → [knowledge-management/](knowledge-management/)
- **渐进式加载与上下文感知注入**：Claudesidian 的 L0→L1→L2 + Skill Discovery，与 Claude Code deferred tools 同源 → [knowledge-management/](knowledge-management/) + [agent-architecture/](agent-architecture/)
- **Git Worktree**：一仓多工作区并行开发，Claude Code 多会话并行的基础设施 → [dev-tools/](dev-tools/) + [claude-code/](claude-code/)
