# Deferred Tools

Claude Code 的工具加载优化机制：低频工具只注册名字，不预加载完整 schema。

## 解决什么问题

Agent 的每个可用工具都需要在 prompt 中放一段描述（名字、参数、用途），这消耗 context tokens。工具一多（内置 21 个 + MCP 扩展），光工具描述就可能吃掉几万 tokens。Deferred Tools 把低频工具的 schema 延迟加载——模型能看到工具名，但要用时需要先调 `ToolSearch` 获取完整描述，然后才能调用。

## 效果

工具 array 的 token 开销降低约 40%。

## 类比

手机 App 的"轻应用"——图标在桌面上，但点开才下载完整内容。Deferred Tools 就是 Agent 工具箱的轻应用模式。

→ 深度阅读：[tool-governance](../claude-code/tool-governance.md)
