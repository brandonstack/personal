---
source: "Twitter @Khazix0918"
url: "https://x.com/Khazix0918/status/2037015170091016257"
date: "2026-03-29"
tags: [claude-code, agent-workflow, vibe-coding, tools]
---

# Superpowers：给 Agent 加结构化工作流的插件

GitHub: https://github.com/obra/superpowers — 11 万 Star，Anthropic 官方认证，安装量 23 万（排名第二）。适配 Claude Code、Codex、OpenCode、Cursor。

## 核心理念

Agent 天然倾向拿到任务就写代码，跳过设计、测试、review。Superpowers 在 Agent 链路里插入结构化工作流，由 14 个 Skills 组成。

本质流程：**规划 → 拆解 → 执行 → 审查 → 复盘**。不限于开发，营销方案、PPT、数据分析等通用。

## 工作流详解（以 ADHD 阅读器开发为例）

### 对比：原生 Claude Code Plan 模式

- 进入 `/plan`，描述需求，AI 并行提几个问题（使用场景、技术栈、功能偏好）
- 回答后直接开发，几分钟出结果
- **问题**：问题浮于表面，覆盖不了深层需求。示例中做出的"仿生阅读"是英文方案，中文没有词边界直接乱套；也没考虑公众号/知乎等国内平台适配

### Superpowers 流程

**Skill 1 — Brainstorming（头脑风暴）**
- 苏格拉底式提问：一次只问一个问题，根据回答决定下一个问什么，逐步深入
- 会主动调研（如 ADHD 阅读辅助的学术研究），给出功能优先级建议（例：仿生阅读对中文 ADHD 用户无显著改善）
- 逼你想清楚所有细节：目标浏览器、中文分词库、UI 风格等
- 最终产出一份详细设计文档

**Skill 2 — Using Git Worktrees**
- 从主分支拉新分支做隔离开发，避免直接改炸主分支

**Skill 3 — Writing Plans**
- 把设计文档拆成 2~5 分钟可完成的开发任务清单
- 设计目标："让没有品味、没有判断力、厌恶测试的热情初级工程师也能照着做"
- 拆细后每完成一个小任务就能验证，问题及时发现

**Skill 4 — Subagent-Driven Development**
- 开多个子 Agent 并行执行任务
- 每个任务过两道审查：
  - 第一轮：需求审查 — 是否按需求做，有无过度设计
  - 第二轮：代码质量审查 — 规范性、可维护性
- 不通过就打回修改，循环直到通过

**Skill 5 — Requesting Code Review**
- 最终审查：全局视角检查模块集成、遗漏、一致性
- 跑全量测试，确认通过后合并回主分支，清理工作区

## 关键启发

> **规划 2 小时，执行 10 分钟，审查 1 小时。**

- 大多数用户心里只有模糊想法，需要被"拷打"才能想清楚需求边界
- 能力一般的模型用 Superpowers 加持反而更大
- 不是 AI 不行，是需求没说清楚

## 安装

```
帮我下载并安装这个插件：https://github.com/obra/superpowers
```

安装后需重启生效（非热加载）。
