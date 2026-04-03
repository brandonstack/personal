---
source: "https://x.com/wquguru/status/2038483068428685538"
url: "https://x.com/wquguru/status/2038483068428685538"
date: "2026-03-30"
tags: [claude-code, productivity, tools]
status: "compiled"
---

# Boris 的菜刀：Claude Code 隐藏用法

Claude Code 之父 Boris 推特分享的高频实用功能，作者以"做菜刀的人讲菜刀用法"为喻串联。

## 核心功能清单

**手机写代码**
- iPhone Claude app → Code 标签，随时随地改代码，不用开电脑

**会话传送**
- `--teleport`：把云端会话迁移到本地继续
- `/remote-control`：从手机/网页控制本地运行的会话（Boris 一直开着）

**自动化循环**
- `/loop 5m /babysit`：每 5 分钟自动处理代码审查、rebase 等，可持续最长一周
- `/schedule`：定时任务

**并行处理**
- `git worktrees` + `claude -w`：同时开几十个 Claude 实例，互不干扰
- `/batch`：先采访用户需求，自动决定开多少 worktree 并行分配任务，适合大规模代码迁移

**快速问答**
- `/btw`：让 AI 继续干活的同时插问快速问题，并行处理

**性能优化**
- `--bare`：跳过 CLAUDE.md/设置/MCP 扫描，启动速度提升 10×；适合非交互式脚本

**多仓库协作**
- `--add-dir <path>`：给当前会话授权读写另一个仓库目录

**自定义 Agent**
- `.claude/agents/` 目录下定义 agent，指定系统提示词和工具
- `claude --agent=<名字>` 启动，适合专用场景（写测试、重构、写文档）

**语音输入**
- `/voice`：按住空格键说话，Boris 大部分时候语音写代码

## 作者观察

- 这些技巧站在重度用户视角，$200/月套餐早高峰两个提示词就用完是真实痛点
- 知道技巧和用得上是两码事，但了解创造者怎么用工具本身有价值
