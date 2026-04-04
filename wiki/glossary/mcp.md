# MCP (Model Context Protocol)

Anthropic 推出的开放协议，让 LLM 应用能以标准化方式连接外部数据源和工具。

## 解决什么问题

没有 MCP 之前，每个 AI 工具要对接一个外部服务就得写一套定制集成代码。N 个 AI 工具 × M 个服务 = N×M 套胶水代码。MCP 把这变成 N+M：工具端实现 MCP client，服务端实现 MCP server，中间走统一协议。

## 三个核心原语

- **Tools** — Agent 可调用的操作（如"搜索数据库"、"发邮件"）
- **Resources** — Agent 可读取的数据（如文件内容、数据库记录）
- **Prompts** — 预定义的交互模板

## 类比

USB-C 接口。以前每个设备一种线，现在一根线通吃。MCP 就是 AI 工具和外部服务之间的 USB-C。

## 在本 wiki 的语境

wiki 中提到 MCP 主要在两个场景：
1. **Claude Code 工具扩展** — 通过 MCP server 给 Agent 接入新能力（→ [tool-design-evolution](../agent-architecture/tool-design-evolution.md)）
2. **Token 开销问题** — 5 个 MCP server 的工具描述可能吃掉 ~55K tokens，所以需要 Deferred Tools 等优化（→ [tool-governance](../claude-code/tool-governance.md)）

→ 深度阅读：[architecture-overview](../claude-code/architecture-overview.md)、[tool-design-evolution](../agent-architecture/tool-design-evolution.md)
