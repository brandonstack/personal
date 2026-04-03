# Harness Engineering

设计包裹 LLM 的运行时系统——管理 context、tool、state、feedback loop。

## 文件

（尚未从 inbox 编译，待 /compile 后填充）

## 核心概念

- **Harness**：LLM 的运行时外壳，从 prompt template 到 context engine 到完整运行时的演进
- **Context Engineering**：主动管理 context window 的内容、结构和时机
- **Evaluator-Generator 模式**：生成器产出，评估器打分，循环迭代
- **长时运行 Harness**：跨会话持久化状态、记忆治理

## 跨主题连接

- → [claude-code/](../claude-code/) — Claude Code 是 harness 的一个具体实现
- → [agent-architecture/](../agent-architecture/) — multi-agent 系统是 harness 的高阶形态
- → [ai-engineering/](../ai-engineering/) — harness 设计是 AI Systems Engineer 的核心技能
