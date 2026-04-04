---
topic: "Agent SDK & Harness Engineering"
status: "curating"
hours_budget: 20
target_wiki_dir: "harness-engineering"
---

# Agent SDK & Harness Engineering

主线加深。wiki 已有 22 个相关文件，重点是补充 SDK 实操、frontier agent 分析、multi-agent 模式的最新实践。

## 学习目标

- [ ] Claude Agent SDK 文档通读，能用 SDK 搭建 multi-agent 系统
- [ ] 理解 SWE-Bench / SWE-Agent 的 harness 设计
- [ ] 掌握 tool use 的高级模式（parallel tool calls, streaming, error recovery）
- [ ] 了解 frontier agent 系统（Devin, Cursor, Windsurf）的架构决策
- [ ] 能设计 evaluator agent 的评分标准和反馈循环
- [ ] 理解 agent memory 和 context management 的最新方案

## Tier 1 — 必读

| # | 标题 | URL | Source | 说明 | Status |
|---|------|-----|--------|------|--------|
| 1 | Claude Agent SDK Documentation | https://docs.anthropic.com/en/docs/agents-and-tools/claude-agent-sdk | Anthropic | 官方 SDK 文档，首要材料 | ⬜ |
| 2 | Building Effective Agents | https://www.anthropic.com/research/building-effective-agents | Anthropic | Agent 架构设计指南，经典 | ⬜ |
| 3 | Tool Use Documentation | https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview | Anthropic | Tool use 完整文档 | ⬜ |
| 4 | Multi-Agent Orchestration | https://docs.anthropic.com/en/docs/build-with-claude/agentic-tool-use | Anthropic | Multi-agent patterns 官方指南 | ⬜ |
| 5 | SWE-Agent: Agent-Computer Interfaces | https://swe-agent.com/paper/ | Princeton NLP | ACI 设计论文，harness 关键参考 | ⬜ |
| 6 | OpenAI Harness Engineering | https://cookbook.openai.com/examples/coding_agent | OpenAI | Coding agent harness 实践 | ⬜ |
| 7 | Claude Code: Best Practices | https://docs.anthropic.com/en/docs/claude-code/overview | Anthropic | Claude Code 官方指南和最佳实践 | ⬜ |
| 8 | Extended Thinking with Claude | https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking | Anthropic | Extended thinking 模式，影响 agent 决策 | ⬜ |

## Tier 2 — 推荐

| # | 标题 | URL | Source | 说明 | Status |
|---|------|-----|--------|------|--------|
| 1 | Anthropic Cookbook — Agent Patterns | https://github.com/anthropics/anthropic-cookbook/tree/main/misc/prompt_caching | Anthropic | 官方 cookbook 示例代码 | ⬜ |
| 2 | SWE-Bench Leaderboard | https://www.swebench.com/ | SWE-Bench | Agent 评估基准，了解评测方法 | ⬜ |
| 3 | The Agent Protocol | https://agentprotocol.ai/ | Agent Protocol | Agent 通信标准化尝试 | ⬜ |
| 4 | Prompt Caching | https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching | Anthropic | 长上下文 agent 的成本优化 | ⬜ |
| 5 | Model Context Protocol | https://modelcontextprotocol.io/introduction | MCP | MCP 规范，agent tool 生态 | ⬜ |

## Fetch Commands

```bash
python3 .ingest/batch-fetch.py projects/ai-learning/topics/agent-harness.md --tier 1
```

## Wiki Output

（compile 后填入）
