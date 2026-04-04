# ACI (Agent-Computer Interface)

面向 Agent 设计的工具接口，区别于面向人类的 UI 和面向程序的 API。

## 解决什么问题

传统 API 是给程序员用的：参数多、组合灵活、需要人来决定调用顺序。但 Agent 不是程序员——它通过自然语言理解工具描述，然后自主决定调用什么。ACI 的核心思路是：**工具描述和接口应该为 Agent 的理解方式优化**，而不是照搬 REST API。

## 设计原则

- 工具粒度要对齐 Agent 的"一步操作"（不要太细碎也不要太粗）
- 工具名和参数名要自解释（Agent 靠名字理解用途）
- 减少工具数量（每个工具描述都消耗 context tokens）

## 陷阱

工具数量容易爆炸。5 个 MCP server 可能带来几十个工具，光描述就吃 ~55K tokens。所以需要配合 Deferred Tools 等机制控制开销。

## 类比

UI 是给人看的（按钮、菜单），API 是给代码调的（函数签名），ACI 是给 Agent 用的（自然语言描述 + 结构化参数）。三层各有优化目标。

→ 深度阅读：[tool-design-evolution](../agent-architecture/tool-design-evolution.md)
