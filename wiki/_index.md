# Wiki — LLM 维护的知识库

本目录由 LLM 全权维护。人通过审阅 report + 对话来影响内容，不直接编辑。

## 主题目录

| 目录 | 说明 | 文件数 | 最后更新 |
|------|------|--------|----------|
| [harness-engineering/](harness-engineering/) | Harness 设计模式：包裹 LLM 的运行时系统 | 0 | — |
| [claude-code/](claude-code/) | Claude Code 工具用法、架构、skill 系统 | 1 | 2026-04-03 |
| [agent-architecture/](agent-architecture/) | 多 agent 系统、编排模式、tool 设计 | 0 | — |
| [knowledge-management/](knowledge-management/) | 知识库架构、信息治理、PKM 方法论 | 0 | — |
| [ai-engineering/](ai-engineering/) | AI 工程通用框架、定位模型、能力迁移 | 1 | 2026-04-03 |

## 跨主题核心概念

- **Harness**：包裹 LLM 的运行时系统，管理 context、tool、state → [harness-engineering/](harness-engineering/)
- **Context Engineering**：主动管理 context window 的内容和结构 → [harness-engineering/](harness-engineering/)
- **Evaluator-Generator 分离**：harness 核心模式，也是 AI 工程能力迁移的关键 → [harness-engineering/](harness-engineering/) + [ai-engineering/](ai-engineering/)
- **Claude Code 作为 Harness 实现**：Claude Code 本身是 harness 的一个具体案例 → [claude-code/](claude-code/) + [harness-engineering/](harness-engineering/)
