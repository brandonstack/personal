# Claude Code

Claude Code 工具的用法、架构分析、skill 系统、最佳实践。

## 文件

- [workflow-commands.md](workflow-commands.md) — 隐藏/进阶命令：会话控制（rewind/branch/btw）、工作流编排（loop/rc）、模型切换

## 核心概念

- **会话版本控制**：/rewind 提供代码+对话的四模式回退
- **对话分叉**：/branch 创建平行会话，任务隔离
- **工作流运行时**：/loop + /branch 让 Claude Code 从对话工具变成可编排系统
- **Skill 系统**：.claude/commands/ 下的自定义命令

## 跨主题连接

- → [harness-engineering/](../harness-engineering/) — Claude Code 本身是一个 harness 实现，CLAUDE.md + commands + memory 构成运行时
- → [agent-architecture/](../agent-architecture/) — skill 系统体现 agent tool use 设计模式
