# Context Engineering 实践

Claude Code 如何管理 200K token 的 context window——预算分配、缓存优化、成本控制策略。Context 是 Agent 最稀缺的资源，管理好它是 harness 设计的核心能力。

## 200K Token 预算分配

| 类型 | 占比 | 内容 |
|------|------|------|
| 固定开销 | ~15-20K | System prompt + 工具定义 + 行为约束 |
| 半固定 | ~5-10K | CLAUDE.md 链 + git 状态 + 环境信息 |
| 动态可用 | ~160-180K | 对话历史 + tool results + 文件内容 |

关键认知：**可用 context 远小于标称 context**。每多注册一个 MCP 工具，工具定义就多吃几百 token。

## MCP 是最大的隐形 Context 杀手

每个 MCP 工具的 schema 定义需要几百 token。一个 MCP server 暴露 20 个工具 → 数千 token 固定开销。

解法一：**Deferred Tools（延迟加载工具）**
- 低频工具不预加载 schema，只在 tools 列表放名字
- 模型需要时先调 `ToolSearch` 拉取完整 schema，然后才能调用
- 实测减少 ~40% tools array 开销

解法二：**只注册真正需要的 MCP 工具**
- 审查每个 MCP server 暴露的工具列表
- 用 `allowedTools` 过滤不需要的工具

## Prompt Caching 机制

System prompt 分为静态和动态两段：

- **静态段**：角色定义、工具 schema、通用规则 → 写入 cache
- **动态段**：当前日期、OS 信息、CLAUDE.md 内容 → 每次重算
- `SYSTEM_PROMPT_DYNAMIC_BOUNDARY` 标记分界点

Cache-aware fork：当检测到 cache miss，fork 两个请求——一个用旧缓存前缀继续，一个用新缓存点。取先返回的结果。这优化了缓存过期时的延迟。

## Conversation Compaction

context 接近 token limit 时触发压缩：
- 保留 system prompt 和最近几轮对话
- 中间部分由 LLM 摘要
- `/compact` 命令可手动触发

## 成本控制策略

**模型策略**：
- `/model opusplan`：规划用 Opus（贵但准），执行用 Sonnet（便宜快）
- 简单任务直接用 Sonnet
- 模型选择是最直接的成本杠杆

**Context 策略**：
- 频繁 `/compact` 释放 context 空间
- 复杂任务拆分到多个 session（每个 session 干净的 context）
- 用 `/branch` 隔离不同任务，避免 context 污染

**工具策略**：
- 减少不必要的 MCP 工具注册
- 利用 deferred tools 降低固定开销
- 批量文件操作用一次 tool call 完成

**实际花费参考**（社区数据）：
- 30 天高强度使用：70 个 plan 文件，263 个 commits
- 日常编码：每天 $5-15（Sonnet 为主）
- 重度架构任务：单次 $20-50（Opus）

→ [architecture-overview.md](architecture-overview.md) — 架构中的 Context 层
→ [../harness-engineering/agent-environment-design.md](../harness-engineering/agent-environment-design.md) — "Context 是稀缺资源"的环境设计原则

> 来源：resources/20260312-claude-code-architecture-governance.md, resources/clippings/Claude Code 高效使用指南...md, resources/clippings/ClaudeCode 你想知道的所有秘密...md
