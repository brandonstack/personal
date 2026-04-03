# Agent Architecture

多 agent 系统设计、编排模式、tool 设计、记忆与状态管理。

## 文件

（尚未从 inbox 编译，待 /compile 后填充）

## 核心概念

- **Multi-agent 编排**：coordinator、specialist、evaluator 的角色分配
- **Tool 设计**：MCP（外循环）vs CLI（内循环）的取舍
- **Agent 记忆**：短期 context vs 长期 knowledge base
- **Agent Interaction Guidelines (AIG)**：agent 行为约束的工程化

## 跨主题连接

- → [harness-engineering/](../harness-engineering/) — agent 系统需要 harness 来保证可靠性
- → [claude-code/](../claude-code/) — Claude Code 的 skill/hook 系统是 agent tool use 的具体实现
- → [knowledge-management/](../knowledge-management/) — agent 的知识层设计
