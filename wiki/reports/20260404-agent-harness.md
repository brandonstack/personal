---
date: "2026-04-04"
sources:
  - resources/anthropic/20260404-tool-use-with-claude---claude-api-docs.md
  - resources/anthropic/20260404-building-with-extended-thinking---claude-api-docs.md
  - resources/princeton-nlp/20260404-untitled.md
wiki_updated: []
---

# Agent SDK & Harness Engineering — Knowledge Sprint 消化报告

## 这批材料在说什么

这批 3 篇 Agent SDK 方向的新增材料**内容质量极低**：
- Tool Use 文档页：只抓到了 docs 站点导航结构，没有实际文档内容
- Extended Thinking 文档页：只有 "Loading..." 字样，本质是空页面
- Princeton NLP (SWE-Agent)：404 页面

有效提取的知识为零。这三个 URL 需要重新 fetch 或替换为其他高质量资源。

## 关键洞察

1. **Jina Reader 对文档站点的抓取效果不稳定**：Anthropic docs 站点可能有 JavaScript 渲染依赖，Jina Reader 抓取到的是未渲染的导航 HTML 而非实际文档内容。这是 fetch pipeline 的已知局限。

2. **wiki 已有的 harness-engineering 和 agent-architecture 内容仍然是最丰富的**：22 个 wiki 文件覆盖了 harness 设计、agent loop、ACI、tools、multi-agent 等概念。本批 sprint 未能增添新知识。

## 与已有知识的关系

无新知识，无更新。

## 对你的具体建议

1. **重新获取这 3 个 URL 的内容**：
   - Anthropic Tool Use：直接在浏览器中阅读 https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview 并手动保存关键内容
   - Extended Thinking：同上，https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking
   - SWE-Agent paper：尝试从 arxiv 获取论文 https://arxiv.org/abs/2405.15793

2. **补充 Tier 1 资源**：
   - Claude Agent SDK GitHub repo README + examples
   - Anthropic "Building Effective Agents" 博文（已有 pending 文件但需要确认内容质量）
   - SWE-Bench 论文（评估 agent coding 能力的标准 benchmark）

3. **这个 topic 的 sprint 建议标记为 "需要重做"**，不要急于标记完成。

## Wiki 更新摘要

无更新。

## 值得讨论的问题

1. **Jina Reader 对 JS 渲染站点的抓取问题如何系统性解决？** 是否值得投入时间改进 fetch-url.py（如加入 Playwright/Puppeteer fallback），还是接受某些站点需要手动处理？

2. **Agent SDK & Harness 已有 22 个 wiki 文件，是不是这个 topic 的 sprint 应该聚焦在"深化"而非"广度"？** 比如：在现有 wiki 基础上做 gap analysis，找出缺什么概念，然后针对性补充。
