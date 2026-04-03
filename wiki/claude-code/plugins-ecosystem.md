# 插件生态

Claude Code 的第三方插件生态——以 Superpowers 和 Compound Engineering 为代表的社区工具如何扩展 Claude Code 的能力边界。

## Superpowers Plugin

GitHub 120K+ stars，最受欢迎的 Claude Code 插件。核心理念：**将 Agent 编码从对话式升级为结构化工作流**。

### 5-Skill 工作流

```
brainstorm → worktrees → plans → subagent-driven-dev → code-review
```

1. **Brainstorm**：多角色讨论（产品经理、架构师、工程师），输出结构化决策文档
2. **Worktrees**：为每个功能创建独立 git worktree，物理隔离避免冲突
3. **Plans**：生成详细执行计划，人审阅后才进入开发
4. **Subagent-Driven Development**：按 plan 拆分子任务，spawn 多个 subagent 并行执行
5. **Code Review**：自动化代码审查 + 合并

### 规划 2 小时，执行 10 分钟，审查 1 小时

Superpowers 的时间分配模型翻转了传统开发：人的时间主要花在规划和审查，执行由 Agent 完成。这与 harness 的"人设计环境，Agent 执行"理念一致。

## Compound Engineering Plugin

核心理念：**知识复利**——每次开发 session 不只产出代码，还产出可复用的知识。

### 核心 Skills

| Skill | 功能 | 特点 |
|-------|------|------|
| `/ce:plan` | 规划 + 知识检索 | spawn research agents，搜索 `docs/solutions/` 历史知识 |
| `/ce:work` | 按计划执行 | 增量执行，每步验证 |
| `/ce:review` | 多角色代码审查 | 6-15 个 reviewer agents，覆盖不同维度 |
| `/ce:compound` | 知识提取与存档 | 3 个并行 agent 提取、去重、写入知识库 |

### `/ce:compound` 的知识提取

做完一个功能/修完一个 bug 后，三个 Agent 并行：
- **Context Analyzer**：回溯 session，提取问题类型和症状
- **Solution Extractor**：提取解法——什么没用、什么管用、root cause
- **Related Docs Finder**：搜索已有知识去重

输出结构化文档：Problem → What Didn't Work → Solution → Prevention

### 为什么不全自动 Compound

不是每个 session 都值得——改 typo 不产生新知识。全自动 compound 会产生噪音，降低搜索质量。可能的解法：**compound janitor**，每天自动扫 session 判断哪些值得 compound。

## 插件架构

插件本质是 `.claude/commands/` 下的 skill 集合，通过 npm 分发：

```json
// settings.json
{
  "plugins": ["@anthropic/superpowers", "@anthropic/compound-engineering"]
}
```

插件可以：
- 注册新 skills
- 添加 hooks（pre/post tool use）
- 提供 MCP servers
- 注入 CLAUDE.md 内容

模型通过 `description` 字段感知插件能力——这让模型能在适当时机建议使用特定 skill。

→ [workflow-patterns.md](workflow-patterns.md) — 插件在工作流中的应用
→ [skills-design.md](skills-design.md) — Skill 设计原则（插件就是打包的 skills）
→ [../harness-engineering/compound-engineering.md](../harness-engineering/compound-engineering.md) — CE 的知识积累理论基础

> 来源：resources/20260329-superpowers-plugin-structured-workflow.md, resources/20260323-claude-code-hacks.md, resources/clippings/Claude Code 高效使用指南...md
