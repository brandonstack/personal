# 工具治理 Pipeline

Claude Code 的工具系统不是简单的"注册 → 调用"，而是一个多阶段治理 pipeline。理解这个 pipeline 对于写 hooks、设计 MCP 工具、和排查权限问题都很重要。

## 工具注册体系

三类工具来源：

| 类型 | 数量 | 特点 |
|------|------|------|
| 内置工具 | 21 个 | Read, Write, Edit, Bash, Glob, Grep, Agent, TodoWrite 等 |
| MCP 工具 | 动态 | 通过 MCP server 注册，schema 占 context |
| Deferred 工具 | ~10+ | 低频工具，只注册名字不加载 schema |

**Deferred Tools 机制**：低频工具（如 NotebookEdit、WebSearch）不预加载完整 schema。模型看到工具名但无法直接调用——需要先调 `ToolSearch` 获取 schema，然后才能使用。这把 tools array 开销降低约 40%。

## 6 阶段执行 Pipeline

每个 tool call 经过：

```
Input Validation → Speculative Classification → PreToolUse Hooks
       → Permission Check → Execute → PostToolUse Hooks
```

### 1. Input Validation
验证参数格式、路径安全性。拦截明显的非法输入。

### 2. Speculative Classification（预判分类）
在等待用户确认前，先预判这个 tool call 可能需要什么权限级别。目的是减少不必要的等待——如果预判为安全操作，可能直接放行。

### 3. PreToolUse Hooks
`.claude/hooks/` 中的 `PreToolUse` hook 在工具执行前触发。可以：
- 拦截并修改工具参数
- 完全阻止执行
- 注入额外 context

用例：自动在 Bash 命令前加 `set -e`，或拦截对特定目录的写操作。

### 4. Permission Check
三种权限模式：
- **Trust mode**（`--dangerously-skip-permissions`）：全部放行
- **Auto-accept edits**：文件编辑自动放行，bash 命令仍需确认
- **Default**：所有有副作用的操作需确认

两阶段分类器：
1. 静态规则匹配（allowlist/denylist pattern）
2. 模型推理（对复杂命令判断安全性）

### 5. Execute
实际执行工具操作。内置工具直接调用，MCP 工具通过 MCP protocol 分发。

### 6. PostToolUse Hooks
执行后触发。可以：
- 记录操作日志
- 触发后续动作（如 lint、format）
- 收集 metrics

**Failure Hooks**：工具执行失败时触发的专门 hook，用于错误恢复或上报。

## Settings.json 工具配置

```json
{
  "permissions": {
    "allow": ["Read", "Glob", "Grep", "Bash(npm test:*)"],
    "deny": ["Bash(rm -rf:*)"]
  }
}
```

Pattern 语法：`ToolName(command_prefix:*)` 支持通配符匹配。

## 与 Harness 的关系

工具治理 pipeline 本质是 harness 的"约束层"——与 OpenAI 的"架构约束通过 linter + CI 机械执行"思路一致。区别在于 Claude Code 把约束嵌入了 agent 内部（hooks + permission），而不是外部 CI。

→ [architecture-overview.md](architecture-overview.md) — 工具层在整体架构中的位置
→ [skills-design.md](skills-design.md) — Skills 作为控制层的组件
→ [../harness-engineering/agent-environment-design.md](../harness-engineering/agent-environment-design.md) — 架构约束是加速器

> 来源：resources/20260312-claude-code-architecture-governance.md, resources/20260315-build-claude-code-from-scratch.md, resources/clippings/ClaudeCode 你想知道的所有秘密...md
