# Harness Engineering

设计包裹 LLM 的运行时系统——管理 context、tool、state、feedback loop。

## 文件

- [harness-generations.md](harness-generations.md) — Prompt → Context → Harness 三代演进，三根支柱，Build to Delete 原则
- [evaluator-generator.md](evaluator-generator.md) — Generator-Evaluator 分离模式：为什么需要、架构演进（V1→V2）、评分标准设计、sprint 合约
- [agent-environment-design.md](agent-environment-design.md) — OpenAI Codex 实践：环境设计、地图式知识组织、架构约束机械执行、熵对抗
- [compound-engineering.md](compound-engineering.md) — 跨 session 知识积累：备忘录 vs 知识库、CE 的 compound 机制、记忆系统学术研究

## 核心概念

- **Harness**：Agent 的操作系统——评估闭环 + 架构约束 + 记忆治理
- **三代范式**：Prompt Engineering → Context Engineering → Harness Engineering，每代包含前代
- **Evaluator-Generator 分离**：Agent 自评不可靠，生成和评估必须独立
- **Build to Delete**：Harness 组件编码模型局限性假设，模型升级后需重新评估
- **Agent 环境设计**：工程师角色从写代码变为设计让 Agent 高效工作的环境
- **渐进式披露**：知识组织用地图（目录表）而非手册（大 AGENTS.md）
- **Compound Engineering**：每次工作产出不只是代码，还有可复用的知识——线性交接 vs 指数积累
- **记忆治理**：3 行 prompt + 记忆 ≈ 200 行专家 prompt，差异在学习轨迹

## 跨主题连接

- → [claude-code/](../claude-code/) — Claude Code 是 harness 的一个具体实现
- → [agent-architecture/](../agent-architecture/) — multi-agent 系统是 harness 的高阶形态
- → [ai-engineering/](../ai-engineering/) — harness 设计是 AI Systems Engineer 的核心技能
- → [knowledge-management/](../knowledge-management/) — Compound Engineering 的知识积累模式与 PKM 方法论相通
