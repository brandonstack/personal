# Claude Code

Claude Code 工具的架构分析、context 管理、工具治理、skill 设计、验证模式、工作流最佳实践。

## 文件

- [architecture-overview.md](architecture-overview.md) — 6 层架构、14 步 agent pipeline、system prompt 动态组装
- [context-engineering.md](context-engineering.md) — 200K token 预算分配、prompt caching、MCP context 成本、成本控制策略
- [tool-governance.md](tool-governance.md) — 6 阶段工具执行 pipeline、权限系统、deferred tools、hooks
- [skills-design.md](skills-design.md) — 9 大 skill 类别、写作最佳实践、渐进式披露、分发策略
- [verification-patterns.md](verification-patterns.md) — Verification Agent 对抗性设计、验证闭环、与 evaluator-generator 的关系
- [workflow-patterns.md](workflow-patterns.md) — Plan-first、vibe coding 两阶段、多会话并行、移动端/远程、实用技巧
- [workflow-commands.md](workflow-commands.md) — 隐藏/进阶命令：会话控制（rewind/branch/btw）、工作流编排（loop/rc）、模型切换
- [plugins-ecosystem.md](plugins-ecosystem.md) — Superpowers（5-skill 工作流）、Compound Engineering（知识复利）、插件架构

## 核心概念

- **6 层架构**：Context → Control（Skills/Hooks）→ Tool → Subagent → Verification → CLAUDE.md 合约
- **Context 经济学**：200K token 中只有 ~160-180K 可用于动态内容；MCP 是最大隐形成本
- **Deferred Tools**：低频工具延迟加载 schema，减少 ~40% 工具定义开销
- **对抗性验证**："try to break it" 而非 "confirm it looks OK"
- **Plan-First**：规划 2h → 执行 10min → 审查 1h，人的时间在规划和审查
- **Skill 作为可分发 prompt**：写好一次，团队/社区复用
- **知识复利**：每个 session 不只产出代码，还产出可复用知识（CE /compound）

## 跨主题连接

- → [harness-engineering/](../harness-engineering/) — Claude Code 本身是一个完整的 harness 实现
- → [harness-engineering/evaluator-generator.md](../harness-engineering/evaluator-generator.md) — 验证层是 evaluator-generator 的工具级实现
- → [harness-engineering/agent-environment-design.md](../harness-engineering/agent-environment-design.md) — 架构约束、渐进式披露、错误消息注入修复指令
- → [harness-engineering/compound-engineering.md](../harness-engineering/compound-engineering.md) — CE 插件是 Compound Engineering 的具体实践
- → [ai-engineering/](../ai-engineering/) — Claude Code 熟练度是 AI 工程师的核心技能
