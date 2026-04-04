# LSP (Language Server Protocol)

微软推出的开放协议，让代码编辑器与语言分析服务之间标准化通信。

## 解决什么问题

以前每个编辑器（VS Code、Vim、Emacs）要支持一种语言（Python、TypeScript、Rust）就得写一套插件。N 个编辑器 × M 种语言 = N×M 套实现。LSP 把这变成 N+M：编辑器实现 LSP client，语言工具实现 LSP server，中间走统一协议。

## 提供的能力

自动补全、跳转定义、查找引用、重命名、错误诊断等——所有你在 IDE 里用到的"智能"功能。

## 在本 wiki 的语境

Agent（如 Claude Code）可以通过 LSP 获取代码的语义信息，而不只是把代码当纯文本处理。这让 Agent 能做到"跳转到定义"、"找所有引用"等精确操作，而不是靠 grep 瞎猜。

## 与 MCP 的关系

两者思路相同（用协议解耦 N×M 问题），但领域不同：LSP 解决编辑器与语言服务的对接，MCP 解决 AI 工具与外部数据源的对接。

→ 深度阅读：[architecture-overview](../claude-code/architecture-overview.md)
