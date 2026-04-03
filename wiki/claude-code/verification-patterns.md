# 验证模式

Claude Code 的验证层不是"确认看起来 OK"，而是对抗性设计——"尝试打破它"。这与 Anthropic 的 evaluator-generator 分离理念一脉相承。

## Verification Agent 的对抗性设计

Claude Code 内置的 Verification Agent 遵循一个核心哲学：

> **"Try to break it"** — 不是验证成功，而是尝试发现失败。

这与 QA 工程中的"破坏性测试"思想一致。具体表现：
- 不只运行 happy path，主动探测边界情况
- 对工具执行结果持怀疑态度
- 发现问题后不是简单报告，而是生成具体的修复建议

## 验证闭环

```
Generator 产出代码 → Verification Agent 尝试破坏
  → 发现问题 → 生成修复指令 → Generator 修复 → 再次验证
  → 未发现问题 → 通过
```

这个闭环在 Claude Code 内部自动运行，不需要人工介入。与 Anthropic harness 博客的 evaluator-generator 循环本质相同，只是规模更小（单文件/单功能级别 vs 完整应用级别）。

## 验证工具链

Claude Code 利用已有工具做验证：
- **Linter/Formatter**：语法和风格检查（通过 Bash 工具调用）
- **Type checker**：类型正确性（tsc, mypy 等）
- **Test runner**：单元测试和集成测试
- **Playwright/Puppeteer**：UI 功能验证（Anthropic 评估用）

关键洞察：**验证工具的错误消息本身就是 context**。Claude Code 的 linter 错误消息中注入修复指令——Agent 读到错误就知道怎么修，不需要人介入。这与 OpenAI 的"错误消息中注入修复指令到 Agent 上下文"技巧一致。

## 验证的层级

| 层级 | 验证方式 | 自动化程度 |
|------|----------|-----------|
| 语法 | Linter, formatter | 全自动 |
| 类型 | Type checker | 全自动 |
| 逻辑 | Unit tests | 半自动（需有测试） |
| 功能 | Integration tests, Playwright | 半自动 |
| 设计 | Evaluator Agent + 评分标准 | 需人工调优 rubric |

越往下越需要人的参与——但参与的形式是"设计评估标准"，不是"手动验证每个产出"。

## 与 Evaluator-Generator 模式的关系

Claude Code 的验证层是 evaluator-generator 模式在工具级别的实现：

| 维度 | Anthropic Harness 博客 | Claude Code 内部 |
|------|----------------------|------------------|
| 评估粒度 | 完整应用（sprint 级） | 单个 tool call 结果 |
| 评估方式 | Playwright 端到端测试 | Linter + tests + 对抗性检查 |
| 反馈机制 | 评分标准 + 迭代循环 | 错误消息 + 自动修复 |
| 人工参与 | 调优评分标准 | 配置 linter 规则 + 写测试 |

核心一致性：**人定义"什么是好"，机器执行"检查是不是好"**。

→ [architecture-overview.md](architecture-overview.md) — 验证层在整体架构中的位置
→ [../harness-engineering/evaluator-generator.md](../harness-engineering/evaluator-generator.md) — Evaluator-Generator 分离的完整理论
→ [../harness-engineering/agent-environment-design.md](../harness-engineering/agent-environment-design.md) — 错误消息注入修复指令

> 来源：resources/clippings/ClaudeCode 你想知道的所有秘密...md, resources/20260312-claude-code-architecture-governance.md, resources/20260315-build-claude-code-from-scratch.md
