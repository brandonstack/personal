---
source: "FradSer (Twitter)"
url: "https://x.com/FradSer/status/2036619884122267745"
date: "2026-03-25"
tags: [vibe-coding, claude-code, workflow, AI-coding]
---

# Vibe Coding 又快又好的秘诀

作者在公司内多次分享的 vibe coding 方法论，前端质量高且速度快。

## 第一阶段：全自动模式

基于 superpowers 的魔改版本（[dotclaude/superpowers](https://github.com/FradSer/dotclaude/tree/main/superpowers)），流程：分析需求 → 写计划 → 执行。

关键改进：
- 每个阶段强制启动 loop 校验，防止 AI 幻觉漏掉细节
- 用 BDD 部分替代 TDD

## 第二阶段：半自动模式

发现问题 → `/plan` → 执行，反复迭代。

**技巧：**

- **频繁 git commit**，类似游戏存档（作者做了 [git-agent.dev](https://git-agent.dev)）
- **问题超过两次未修复**时：
  1. 让 AI 从 git 历史查看改动并反思原因
  2. 换模型，甚至换工具
- **多窗口并行执行**，用 prompt 手动区分范围。不用 git worktree——多任务并行时 merge 压力大易出错，这类需求应在第一阶段用 superpowers 解决

## Prompt 技巧

- 最少限制，充分利用工具自动获取上下文（同 Claude Code 理念）
- 但人为补充上下文也很关键：随时打断说"你之前改了 xxx"或"应该有 xxx，你先看看再执行"
- 把 AI 当老师：多问"你做了什么"、"我应该怎么做"
- 善用 `/btw`，必要时打断并修改任务
