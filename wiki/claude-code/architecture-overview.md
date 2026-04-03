# Claude Code 架构概览

Claude Code 是一个基于 TypeScript 的 AI 编程 agent，零框架手搓，核心是一个状态机驱动的 agent loop。理解它的架构对设计 harness 和写好 skill 都至关重要。

## 六层架构

| 层级 | 职责 | 关键组件 |
|------|------|----------|
| Context 层 | 管理 200K token 的 context window | System prompt 动态组装、CLAUDE.md 加载、conversation compaction |
| Control 层 | 控制执行流程 | Skills（.claude/commands/）、Hooks（pre/post tool use） |
| Tool 层 | 与外部世界交互 | 21 个内置工具 + MCP 扩展 + LSP 集成 |
| Subagent 层 | 并行/隔离执行 | 6 种内置 agent（Task、SearchAndReplace、NotebookEdit 等），支持 worktree 隔离 |
| Verification 层 | 质量把关 | Verification Agent（对抗性设计）、linter 集成 |
| CLAUDE.md 合约层 | 行为约束的 "宪法" | 分层加载：root → project → subdirectory |

## Agent Loop 状态机

核心是一个 while 循环（默认最多 25 turns）：

1. 接收用户输入（或上一轮 tool result）
2. 调用 API 获取 assistant message
3. 解析 tool_use blocks
4. 对每个 tool call 执行 6 阶段 pipeline：
   - render（UI 展示）→ speculative classification（预判权限）
   - PreToolUse hooks → permission check → execute → PostToolUse hooks
5. 收集所有 tool results，回到步骤 2
6. 无 tool call 时结束循环（或达到 max turns）

Cache-aware 优化：检测到 cache miss 时 fork API 请求——一个带缓存前缀继续对话，一个使用新缓存点。

## 14 步 Agent Pipeline

完整的从触发到清理的生命周期：

1. 触发（用户输入 / API 调用）
2. 环境初始化（工作目录、git 状态）
3. System prompt 动态组装
4. CLAUDE.md 链加载（root → project → cwd）
5. 工具注册（内置 + MCP + deferred）
6. Context 预算分配
7. Cache checkpoint 设置
8. API 调用（cache-aware fork path）
9. Response 解析 + streaming
10. Tool call 分发（parallel safe tools batch）
11. Permission 检查 + hooks pipeline
12. Tool 执行 + result 收集
13. Conversation compaction（如接近 token limit）
14. 状态清理 + metrics 上报

## System Prompt 组装

System prompt 不是静态文本，而是 `getSystemPrompt()` 动态拼装：

- **静态段**（缓存）：角色定义、工具说明、通用规则
- **动态段**（不缓存）：当前日期、OS 信息、git 状态、CLAUDE.md 内容
- 用 `SYSTEM_PROMPT_DYNAMIC_BOUNDARY` 标记分界——静态段走 prompt cache，动态段每次重算

行为约束通过 `getSimpleDoingTasksSection()` 注入，包含文件操作规范、安全规则、输出格式等。

→ [context-engineering.md](context-engineering.md) — Context 经济学详解
→ [tool-governance.md](tool-governance.md) — 工具治理 pipeline 详解
→ [verification-patterns.md](verification-patterns.md) — 验证层设计
→ [../harness-engineering/harness-generations.md](../harness-engineering/harness-generations.md) — Claude Code 是 Harness 的一个具体实现

> 来源：resources/20260312-claude-code-architecture-governance.md, resources/20260315-build-claude-code-from-scratch.md, resources/clippings/ClaudeCode 你想知道的所有秘密...md
