# Harness 三代演进：Prompt → Context → Harness

AI 工程的核心问题经历了三次范式转移，每一代包含前一代，但核心问题完全不同。

## 三代范式

| 阶段 | 时间 | 核心问题 | 优化对象 |
|------|------|---------|---------|
| **Prompt Engineering** | 2023-2024 | 怎么跟模型说话 | 人与模型的接口（措辞、few-shot、CoT） |
| **Context Engineering** | 2025 | 单靠提示词不够 | 模型的输入空间（RAG、长上下文、tool use、memory） |
| **Harness Engineering** | 2026 | Agent 自主运行数小时/天 | Agent 的整个运行时环境 |

## 每代的关键区别

**Prompt → Context**：从优化"怎么说"到优化"知道什么"。模型能力提升后，单靠措辞已不够，需要给模型准备参考资料、历史记录、工具描述。

**Context → Harness**：从优化"单次输入"到优化"持续运行环境"。Agent 需要在数小时内自主工作，光有好的 context 不够——需要评估闭环、架构约束、记忆治理的完整运行时。

## Harness 三根支柱

完整 Harness = 评估机制 + 架构约束 + 记忆治理。少任何一层，Agent 系统都会在某个维度失控。

1. **评估闭环**：Agent 不能自评 → 独立 evaluator → 评估驱动开发（TDD 的 Agent 版）
2. **架构约束**：用 linter + CI 机械执行不变量，而非依赖文档自觉遵守 → 约束越多反而越可靠
3. **记忆治理**：跨 session 知识积累，让 Agent 越跑越好而不是每次从零开始

## Harness = Agent 的操作系统

Phil Schmid 的类比：模型是 CPU，context window 是内存，Agent 是应用程序，Harness 是操作系统。没有操作系统，CPU 再强也只是一块芯片。

Martin Fowler 的预测：Harness 未来会变成"服务模板"——起一个新 Agent 就像今天起一个新项目一样，从模板开始。

## 关键数据

- 同样模型 + 不同 Harness：LangChain 实验中 Terminal Bench 2.0 通过率从 52.8% → 66.5%
- Vercel 删掉 80% Agent 工具，结果步骤更少、速度更快、效果更好
- Manus 6 个月重构 5 次 Harness，同模型每次变更好

## Build to Delete 原则

今天写的"聪明逻辑"，明天模型升级可能就不需要了。Harness 的每个组件都编码了对模型局限性的假设——模型变强后有些假设失效。架构必须模块化，随时准备撕掉重来。

> "竞争优势不再是 prompt，而是你的 Harness 捕获的轨迹。每次 Agent 的成功和失败，都是训练下一代的数据。" — Phil Schmid

→ [evaluator-generator.md](evaluator-generator.md) — 评估闭环的具体实现
→ [agent-environment-design.md](agent-environment-design.md) — 架构约束的具体实践
→ [compound-engineering.md](compound-engineering.md) — 记忆治理的具体方案

> 来源：resources/20260328-prompt-context-harness-paradigm-shift.md, resources/clippings/别再卷模型了...Harness.md
