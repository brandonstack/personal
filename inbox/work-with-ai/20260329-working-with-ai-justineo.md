---
source: "Justineo"
url: "https://github.com/Justineo/working-with-ai"
date: "2026-03-29"
tags: [AI, engineering, workflow, agent, prompt]
---

# Working with AI — Justineo 部门分享 Slides 干货提炼

> 作者：Justineo（前端工程师，Codex 重度用户），部门周会分享。Slides 本身用 Claude Code + Vite+ 制作。
> 定位：不是 best practice，是 real practice。AI 进化速度太快，所有经验都只是暂时的。

---

## 1. 从 Tab 到 Agent：AI 编程的演进

- **Tab 时代**：行内自动补全（TabNine → Copilot），人是驾驶员，AI 是副驾
- **Tab Tab**：多插入点同时补全（Cursor）
- **Agent 时代**：你说目的地，AI 开车（Claude Code / Codex / OpenCode）

隐喻：从"逐行确认"到"审查结果"，review 粒度在变粗，信任在增加。

## 2. AI 编程的自动驾驶等级

| 等级 | 描述 | 工具 |
|------|------|------|
| L0 | 完全人工 | 古法编程 |
| L1 | 行内自动补全 | TabNine / Copilot |
| L2 | 代码片段生成 / IDE chat | Copilot / Cursor |
| **L3** | **Coding agent，人 review** | **Claude Code / Codex / Cursor** |
| L4 | Agent + AI review 完成项目 | — |
| L5 | AI 工程团队，完全自主 | — |

**关键洞察**：L3 开始瓶颈变成 code review，信任还需要慢慢建立才能往 L4 发展。

## 3. knowledge.jpeg — LLM 是知识的有损压缩

核心比喻：
- RAW = 人脑 / 全部知识
- PNG = Wikipedia / 教科书 / 文档
- **JPEG = LLM — 实用，但有损失**

幻觉不是 bug，是压缩率的代价。模型越大，精度越高。

## 4. 工具选择

| 工具 | 用途 |
|------|------|
| Codex | 写代码唯一选择 |
| Claude Code | 创意工作 |
| ChatGPT | Research |
| Playwright | MCP |

核心观点：**有人说 Codex 太慢了 — 靠谱才是真的快。**

## 5. 关于 Skills

比喻：Skills = 棋谱（人总结的最佳实践），但 LLM 会有自己的 AlphaZero 时刻。

- **Skill 有用的时候**：让 AI 快速掌握特殊工具；自己不熟悉、不容易判断好坏的领域
- **Skill 不太有用的时候**：模型已经很熟的领域（主流语言/框架）；skill 可能限制 AI 的灵活性；模型更新后 skill 可能变成瓶颈

即使没有 skill，agent 也能从文档学习 — skill 只是提炼出的索引。

## 6. CLI vs MCP

- **CLI**：快、可组合、透明可调试 → 开发内环
- **MCP**：可发现、跨客户端、结构化输入输出 → 集成外环

结论：**两者都很有用**，多数团队最终二者并存。CLI 做底层实现 + 专家入口，MCP 做标准化接口层。

推荐 `gh` CLI — Agent 友好、半结构化输出、可组合。

## 7. Workflow：Research → Plan → Implement → Review

不是线性流程，是一个 loop。

- Agent 的**内循环**（每次执行）：Plan → Edit → Run tests → Observe → Repair → Update
- 我们的 workflow 是更大的**外循环** — 跨 turn、可持久化、跨 session

**journey/ 目录结构**：把过程写进文件，跨 session 不丢 track。
```
journey/
├── research/
├── plans/
├── prompts/
├── logs/
└── ...
```
每个阶段是一个目录，输出 = 对开发过程和决策的 distill。

案例：[Justineo/swrv-next](https://github.com/Justineo/swrv-next/tree/main/journey)

## 8. Research 双模式

| 模式 | 工具 | 特点 |
|------|------|------|
| Context-free | ChatGPT Deep Research | 不带先入为主的 bias，基于第一性原理调研 |
| Context-rich | Claude Code / Codex | 理解当前设计决策和限制，在现有架构内寻找最佳方案 |

先不带预设地调研，再结合项目上下文落地 → 补完思考空间 → 更好的设计决策。

## 9. Prompt 经验

1. **基于第一性原理思考** — 不要套用模式，从根本推导
2. **从根源解决，避免 ad-hoc patch** — 找到问题的本质
3. **对我的思路保持中立** — 不要假设我之前的做法是正确的，该挑战就挑战
4. **先理解现有代码再动手** — 不要还没读完就开始改
5. **相信 AI 的基础能力** — 不限定文件路径，不给固定 context，让 AI 自己去找、去判断

核心：多使用，对 AI 能干什么不能干什么有完整的感受。**对于 AI 擅长的 → 相信 AI。**

## 10. 不只是 Vibe Coding

AI 不只能写代码，它能帮你沟通、协作、探索想法。

### 设计交互协作
开发者用 AI 快速出原型 → 和设计师一起看效果 → 迭代。交互细节不再靠文字描述和想象。
- 案例：[v0-kong-datakit-flow-editor](https://v0-kong-datakit-flow-editor.vercel.app/)

### 会议讨论准备
Deep Research 调研 → 结合自己的 insight 整理成文档 → 丢给 Claude Code 制作可交互的讨论材料。
- 案例：[vibe-hand-off](https://vibe-hand-off.vercel.app/)

### 辅助沟通理解
复杂技术方案用文字描述容易有理解偏差，**做个可交互的文档出来，比说一百句都清楚**。
- 案例：[v0-plugin-form-optimization](https://v0-plugin-form-optimization.vercel.app/)

## 11. 用 AI 做设计 — AI 味的本质

AI 味的本质 = **平均设计**：什么都有，但缺少取舍和个性。用 Skill 能去除 AI 味，但基于 Skill 做出来的版式，会不会成为新的 AI 味？

去 AI 味的方法：给它具体的、有个性的约束（品牌、风格、反例）。

## 12. 信息获取方式在变

从构造 query 到直接表达需求：
- 以前：精心构建 query → 扫 StackOverflow → 自己筛选
- 现在：直接描述问题和上下文 → 一次给出诊断 + 方案

**Google 使用量下降了 95%**，剩下 5% 是肌肉记忆。

## 13. 默认不信任「快」

用了 AI 以后，反而开始**信任「慢」**。
- 「快」给人一种不踏实的感觉 — AI 是不是跳过了什么？
- 「慢」说明它在认真思考，在做 research，在 plan

> 这和我们对人的直觉一样：**三秒给你答案的人，你信吗？**

## 14. Coding Agent = 通用 Agent

Coding agent 本质上是一个用代码解决问题的方法论实现。不要只当"写代码的工具"。

生活应用案例：
- 整理相册（按日期/人物自动分类）
- 帮妻子 refresh 简历
- 女儿足球赛赛历（自动生成 .ics 订阅）
- 做这个 Slides（多轮 review）

---

## 附：项目中的 Skill 资产

项目 journey/ 目录包含两个高质量 frontend skill：
- **frontend-design.md**：偏创意方向，强调独特美学、反 AI 味、bold aesthetic direction
- **frontend-skill.md**（taste-skill）：偏工程方向，严格的 design engineering 规范，包含 anti-slop rules、motion engine、bento paradigm
- **mcp-vs-cli.md**：深度研究报告，MCP vs CLI 的完整对比分析（用 ChatGPT Deep Research 生成）