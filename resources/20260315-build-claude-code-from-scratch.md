---
source: "IceBearMiner (Twitter)"
url: "https://x.com/IceBearMiner/status/2037888800341610684"
date: "2026-03-15"
tags: [claude-code, architecture, agents, AI-engineering]
status: "compiled"
---

# 从零构建 Claude Code：AI CLI 架构拆解

作者两天内以 Claude Code 为参照，从零重建了功能等价的 agentic CLI——纯 TypeScript，零框架，唯一依赖 fast-glob。产出：46 文件，1 万行 TS。

## 整体架构

核心循环：用户输入 → 组装请求 → SSE API 调用 → 解析事件流 → 按 stop_reason 分支：
- **end_turn** → 输出文本，结束本轮
- **tool_use** → 执行工具 → tool_result 追加到 messages → 下一轮迭代

六层目录，依赖单向：
- **core/** — Agent Loop、SSE 客户端、context 管理、compact
- **tools/** — 内置工具实现 + MCP 客户端
- **ui/** — 终端渲染、流式输出、颜色主题
- **plugins/** — 运行时注入工具和 hook
- **skills/** — slash command 高级功能
- **commands/** — / 前缀命令解析分发

技术选型：Node.js 22 原生能力（fetch、ReadableStream、TextDecoder、child_process），不需要额外 HTTP 库。

## System Prompt 分段与 Prompt Caching

单字符串 system prompt 的问题：缓存无法有效命中，动态内容污染缓存。

解法：system 参数设为 block 数组，按可变性分类：

**静态段**（打 cache_control，缓存命中）：身份声明 → 工具使用规范 → 编码风格 → 安全规则

**动态段**（不缓存，每轮重算）：工作目录/环境 → Git 状态 → CLAUDE.md → MCP 指令

Anthropic 的 prompt caching 按 block 数组前缀匹配，静态内容排前面 → 缓存命中率最高。这就是官方订阅省钱的原因。

## Agent Loop：状态机

有上限的 while 循环（max 25 轮），每轮：
1. 检查是否需要 compact
2. 构建 prompt → 发起流式请求 → 处理事件流
3. stop_reason 判断：tool_use 则执行工具，end_turn/max_tokens 则结束

**工具执行管线**（6 阶段）：renderToolCall → permissionCheck → preHook → checkpoint（破坏性操作前快照）→ executeTool → postHook

**自动 compact**：估算 token 数（字符数 ÷ 4），超过上下文限制 85% 时触发压缩——独立 API 调用生成摘要替换 messages。

**三层 Prompt Caching**：
1. system prompt 静态段
2. tools 数组最后一个 definition 打 cache_control
3. 最后一条 tool_result message 作为缓存断点

效果：每轮只有少量 tokens 按正常输入计费，大部分走缓存价格（~10%）。

## 21 个内置工具

关键实现：
- **Read** — fs.readFile + 行号前缀，支持 offset/limit 分页
- **Edit** — 精确字符串替换，old_string 必须文件中唯一出现，否则报错（迫使模型精确定位）
- **Bash** — child_process.exec，120s 超时，输出超 500 行截断（前 200 + 后 100）
- **Grep** — 自实现 regex，三种输出模式 + 上下文行 + 跨行匹配

**Deferred Tools** 优化：低频工具（NotebookRead、TodoWrite 等）不放入每次请求的 tools 数组，模型需要时通过 ToolSearch 查询获取 schema。tools 数组固定开销降低 ~40%。

## 权限系统

三种模式：
- **default** — safe 工具自动执行，dangerous/write 需确认
- **auto** — 绕过交互提示（CI 用），但 deny rules 仍生效
- **plan** — 只读沙箱，dangerous/write 静默拒绝

工具分类：safe（Read/Glob/Grep）、dangerous（Bash/Agent）、write（Write/Edit）、bypass（PlanMode）

**两阶段分类器**（auto 模式安全增强）：
1. 模式匹配：已知安全/危险命令规则表，覆盖 90%+，零延迟
2. 未覆盖情况：发给 Haiku 判断 allow/deny/ask_user（~300-500ms）

## MCP 与 LSP 集成

**MCP**：JSON-RPC 2.0 over stdio。启动序列：initialize → tools/list。工具名加 `mcp__server_name__` 前缀做命名空间隔离。

**LSP**：不是扩展工具，而是给模型提供实时代码诊断。Write/Edit 后自动通知语言服务器，诊断结果注入下一轮 system prompt → 模型修改代码后立即看到编译器反馈。

## 插件系统与 Skills

插件 = 目录 + plugin.json，声明六类扩展点：skills、agents、hooks、commands、mcpServers、lspServers。

Skills 是参数化 prompt 模板，8 个内置：commit/pr/review（Git 操作）、init、simplify、loop/schedule、update-config。

查找优先级：内置 → 插件 → 项目 `.clio/skills/`。项目级可覆盖插件级但不能覆盖内置（安全）。

## 多 Agent 协作

子 Agent 通过 executeSubAgent() 运行（主 loop 简化版，排除团队管理工具防嵌套，max 15 轮）。isolation: "worktree" 可创建 Git worktree 独立分支操作。

后台 Agent：`run_in_background: true`，Promise 存入 Map，完成时以 tool_result 通知主 Agent。

协作流程：TeamCreate → SendMessage 分发 → 等待完成 → 汇总 → TeamDelete。最小化协调协议：无消息队列，无共享状态，只有显式消息传递。

## Auto Memory

用文件系统模拟持久记忆，四种类型：user（偏好）、feedback（行为纠正）、project（项目约定）、reference（外部资源指针）。

MEMORY.md 索引文件每次对话开始注入 system prompt。写入复用现有工具（Write/Edit/Read），零新增代码路径。

## 核心结论

> 构建 agent 工具的核心难点在于 Harness Engineering。调用 API 是十行代码的事，把工具调用结果正确反馈给模型、在流式输出中插入用户交互、处理长任务错误恢复——这些才是真正的工程挑战。
