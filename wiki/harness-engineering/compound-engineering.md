# Compound Engineering：从线性交接到指数积累

Compound Engineering（CE）解决了 Anthropic harness 博客未深入讨论的问题：跨 session 的知识积累。Harness 三支柱中"记忆治理"的具体实践方案。

## 核心区别：备忘录 vs 知识库

Anthropic 的 progress file 是**备忘录**：上一班留给下一班的交接，线性的，只服务相邻两个 session。

CE 的 `docs/solutions/` 是**知识库**：所有 session 都能查的项目记忆。备忘录解决连续性，知识库解决积累性。一个线性，一个指数。

"Compound" 的含义：每次工作的产出不只是代码，还有下次能复用的知识。用得越久，Agent 越懂你的项目。

## /ce:compound 的工作机制

做完一个功能或修完一个 bug 后，并行 spawn 三个 Agent：

1. **Context Analyzer**：回溯整个 session 对话，提取问题类型、涉及组件、症状
2. **Solution Extractor**：从 debug 过程提取——什么没用、什么管用、root cause、怎么预防
3. **Related Docs Finder**：搜已有 `docs/solutions/` 查重。高度重复就更新旧文档，不新建

三个 Agent 跑完，orchestrator 汇总，写结构化文档到 `docs/solutions/`：
- Problem（一两句问题描述）
- What Didn't Work（排查中试了什么没用的）
- Solution（最终解法和代码）
- Prevention（以后怎么避免）

每个文档带 YAML frontmatter，按 category 分目录存储。

## 知识复用路径

未来所有 `/ce:plan` 的 learnings-researcher 会搜索这些文档。不是给"下一个 session"用，是给"所有未来 session"用。

例：修了一个 edge runtime 兼容性 bug → compound 记录 → 三周后碰到类似 runtime 问题 → plan 阶段 Agent 自动翻出之前的坑和解法。

## 为什么不自动 Compound

CE 作者刻意选择不在全自动流程（/lfg）中包含 compound 步骤：

- 不是每个 session 都值得 compound——改 typo、调 CSS 不产生新知识
- 自动 compound 每个 session 会产生噪音，降低搜索质量
- 只有真正 debug 了一个坑、发现了一个 pattern 的 session 才值得

但人会忘记。可能的解法：**compound janitor**——每天 end of day 自动扫当天 session 的 git diff 和 conversation，判断哪些值得 compound，筛选后批量跑。

## gstack + CE：覆盖完整 Harness

对照 Anthropic 架构，gstack + CE 覆盖了所有角色：

| 层次 | 工具 | 功能 |
|------|------|------|
| 决策层 | gstack /plan-ceo-review, /plan-eng-review | 产品/架构视角把关 |
| 规划层 | CE /ce:plan | spawn research agents，读历史 learnings |
| 执行层 | CE /ce:work | 按 plan 增量执行 |
| 审查层 | CE /ce:review (6-15 reviewer) + gstack /qa | 专项 review + 浏览器实测 |
| 知识层 | CE /ce:compound | 写进可搜索的项目知识库 |

## 记忆系统的学术研究

(S)AGE 论文提出了多 Agent 共享知识库的可信性问题：

- **Proof of Experience 共识机制**：每个 Agent 有声誉权重（历史准确率 x 领域相关性 x 活跃度 x 独立验证数）
- 记忆需加权投票验证后才写入，防止幻觉通过共享知识库污染所有 Agent
- 性能：956 req/s 写入、21.6ms P95 查询

纵向学习论文的关键发现：**3 行 prompt + 记忆系统 ≈ 200 行专家 prompt**。差异在学习轨迹——有记忆的系统越跑越好，无记忆的系统停滞不前。记忆层带来的不是更高初始性能，而是组织级纵向学习能力。

## 与本 Repo 的关系

本 repo 的 wiki 模式（resources/pending → LLM 消化 → wiki 知识库 → 对话回流）本质上就是 Compound Engineering 在个人知识管理中的实践：每次消化都增强知识库，知识 compound。

→ [harness-generations.md](harness-generations.md) — 记忆治理是 Harness 三支柱之一
→ [evaluator-generator.md](evaluator-generator.md) — 评估闭环支柱
→ [agent-environment-design.md](agent-environment-design.md) — 架构约束支柱
→ [../knowledge-management/](../knowledge-management/) — 知识治理的通用原则

> 来源：resources/clippings/一个从执行到记忆的完整 Agent Harness gstack + Compound Engineering.md, resources/20260328-prompt-context-harness-paradigm-shift.md
