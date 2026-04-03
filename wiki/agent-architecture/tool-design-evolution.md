# 工具设计演进

Agent 的工具质量 > 工具数量。调试 Agent 应优先检查工具定义，多数"选错工具"源于描述不准确。

## 三代工具设计

| 代际 | 思路 | 问题 |
|------|------|------|
| **1. API 封装** | 把现有 API 直接暴露给 Agent | 粒度过细，Agent 需要多步组合才能完成一个意图 |
| **2. ACI（Agent-Computer Interface）** | 面向 Agent 的目标而非底层 API | 正确方向，但工具数量容易爆炸（5 个 MCP server ≈ 55K tokens） |
| **3. Advanced Tool Use** | 动态发现 + 代码编排 + 示例驱动 | 当前最佳实践，但仍在探索中 |

### ACI 设计原则

- 参数明确 + 结构化错误返回 + 修正建议
- 定义与实现绑定（如 Zod schema），避免定义漂移
- 工具描述写"何时该用我"比"我能做什么"更准确（与 Skill 描述符同理）

### Advanced Tool Use 关键技术

- **动态发现**：`search_tools` 按需检索工具，准确率 49%→74%
- **代码编排**：让 Agent 写代码调用工具而非逐一调用，token 消耗 150K→2K
- **示例驱动**：提供工具使用示例，准确率 72%→90%

## MCP vs CLI

MCP 和 CLI 不是互斥替代，而是分别服务不同场景：

| 维度 | CLI | MCP |
|------|-----|-----|
| **定位** | 开发内环（inner loop） | 集成外环（outer loop） |
| **第一用户** | 人类开发者 + 脚本 | AI Agent |
| **优势** | 速度、可组合性、可调试 | 可发现性、跨客户端互操作、权限治理 |
| **输入输出** | 字符串参数 + 文本输出 | Schema 明确 + 结构化错误 |
| **安全风险** | 命令注入（开放 shell） | 工具元数据攻击（投毒/影子污染） |

### 场景选择

- **个人/小团队**：CLI 优先，少量 MCP 桥接
- **中型团队**：MCP 标准化工具，CLI 做专家入口
- **企业级**：MCP + OAuth/审计/治理，禁止开放式 shell
- **上下文敏感**：工具路由 + 渐进加载（一次性加载大量 schema 压上下文）

### 文件系统做上下文接口

工具结果写文件，Agent 按需 grep 读取。Cursor A/B 测试显示 MCP 工具 token 消耗减少 46.9%。压缩时把历史写文件保留可追溯性——这就是 Dynamic Context Discovery。

## 与 Deferred Tools 的关系

Claude Code 的 deferred tools 是 Advanced Tool Use "动态发现"在产品层面的实现：低频工具不预加载 schema，Agent 按需通过 ToolSearch 获取。减少 ~40% 工具定义开销。

→ [control-flow-patterns.md](control-flow-patterns.md) — 工具在 Agent Loop 中的角色
→ [../claude-code/tool-governance.md](../claude-code/tool-governance.md) — Claude Code 的 6 阶段工具执行 pipeline
→ [../harness-engineering/agent-environment-design.md](../harness-engineering/agent-environment-design.md) — "约束编码化"在工具层的体现

> 来源：resources/20260319-agent-architecture-engineering-practice.md
> 来源：resources/work-with-ai/20260329-mcp-vs-cli-research-justineo.md
> 来源：resources/work-with-ai/20260329-working-with-ai-justineo.md
