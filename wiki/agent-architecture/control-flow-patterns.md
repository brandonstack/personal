# Agent 控制流模式

Agent 的核心是一个循环（感知 → 决策 → 行动 → 反馈），约 20 行代码。关键区分：执行路径由代码写死 = Workflow，由 LLM 动态决定 = Agent。

## 五种控制模式

| 模式 | 适用场景 | 示例 |
|------|----------|------|
| **提示链** | 线性流程，步骤确定 | 生成 → 翻译、大纲 → 正文 |
| **路由** | 输入分类，定向处理 | 简单 → 轻量模型，复杂 → 强模型 |
| **并行** | 可拆分的独立子任务 | 分段法（拆子任务并发）/ 投票法（同任务多次取共识） |
| **编排器-工作者** | 复杂任务，子任务不可预知 | 中央 LLM 动态分解委派，综合结果 |
| **评估器-优化器** | 质量标准难精确定义 | 生成 → 评估 → 循环修复 |

设计原则：循环本身应极度稳定，新能力通过三种方式接入——扩展工具集、调整系统提示、状态外化到文件/DB。**不应让循环变成状态机。**

## Agent Loop 核心机制

loop 默认 ~25 turns，每 turn：接收输入 → 调用 API → 解析 tool_use → 执行工具 → 收集结果 → 回到 API。无 tool call 时结束。

**跨 session 自主运行**：
- Initializer Agent 生成 feature-list.json + 进度文件
- Coding Agent 循环执行，每次从文件恢复现场
- 进度放文件不放上下文，功能清单用 JSON 不用 Markdown
- 同时只有一个 in_progress 任务，每完成一步先更新状态再继续

## 上下文分层管理

| 层级 | 内容 | 特点 |
|------|------|------|
| 常驻层 | 身份、约定、禁止项 | 短、硬、可执行 |
| 按需加载 | Skills 描述符常驻，内容触发时注入 | 渐进式披露 |
| 运行时注入 | 时间、渠道 ID、用户偏好 | 每次请求不同 |
| 记忆层 | MEMORY.md 跨会话 | 需要时读取 |
| 系统层 | Hooks/代码规则 | 不进上下文 |

核心原则：**确定性逻辑不进上下文，交给 Hooks/代码/工具。**

压缩优先级：架构决策 > 已修改文件 > 验证状态 > TODO > 工具输出。标识符（UUID/hash/URL）必须原样保留。

## 任务象限

目标清晰度 × 验证自动化程度。右上角（明确 + 自动验证）最适合 Agent。**Harness 的目标是把任务推向右上角。**

→ [multi-agent-patterns.md](multi-agent-patterns.md) — 多 Agent 组织模式
→ [evaluation-systems.md](evaluation-systems.md) — 评测系统设计
→ [../claude-code/architecture-overview.md](../claude-code/architecture-overview.md) — Claude Code 的 agent loop 具体实现
→ [../harness-engineering/harness-generations.md](../harness-engineering/harness-generations.md) — Harness 比模型更关键

> 来源：resources/20260319-agent-architecture-engineering-practice.md
