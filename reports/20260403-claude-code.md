---
date: "2026-04-03"
sources:
  - resources/20260312-claude-code-architecture-governance.md
  - resources/20260315-build-claude-code-from-scratch.md
  - resources/20260318-claude-code-skills-lessons.md
  - resources/20260323-claude-code-hacks.md
  - resources/20260325-vibe-coding-workflow-tips.md
  - resources/20260329-superpowers-plugin-structured-workflow.md
  - resources/clippings/20260330-boris-claude-code-tips.md
  - resources/clippings/Claude Code 高效使用指南...md
  - resources/clippings/ClaudeCode 你想知道的所有秘密...md
wiki_updated:
  - wiki/claude-code/architecture-overview.md
  - wiki/claude-code/context-engineering.md
  - wiki/claude-code/tool-governance.md
  - wiki/claude-code/skills-design.md
  - wiki/claude-code/verification-patterns.md
  - wiki/claude-code/workflow-patterns.md
  - wiki/claude-code/plugins-ecosystem.md
  - wiki/claude-code/workflow-commands.md
  - wiki/claude-code/_index.md
  - wiki/_index.md
---

# Claude Code：从工具到 Harness 实现的完整解剖

## 这批材料在说什么

9 篇材料覆盖了 Claude Code 的完整光谱：从底层架构源码分析（6 层架构、14 步 agent pipeline、prompt caching 机制）到上层使用模式（plan-first 工作流、vibe coding 两阶段法、多会话并行），再到社区生态（Superpowers 120K+ stars 的结构化工作流、Compound Engineering 的知识复利）。

关键发现：Claude Code 不只是一个"能写代码的 AI 聊天工具"，它本身就是一个**完整的 harness 实现**——Context 层管理 200K token 预算，Control 层通过 Skills/Hooks 编排行为，Tool 层治理 21 个内置工具 + MCP 扩展，Verification 层实现对抗性验证。理解这个架构，等于手握一个 harness 设计的参考实现。

材料的来源跨度也值得注意：从 Anthropic 内部经验（skills lessons）到社区大 V（Boris Power tips）到中文社区的系统化整理（两篇万字长文），信息密度和视角多样性都很高。中文社区的两篇源码分析尤其有价值——它们补充了官方文档不会讲的实现细节（deferred tools、speculative classification、cache-aware fork）。

## 关键洞察

1. **Context 经济学是一切的基础。** 200K token 听起来很多，但固定开销吃掉 20-30K，MCP 工具定义再吃一截，实际可用 context 可能只有 160K。Deferred tools 砍 40% 工具定义开销的做法，本质上是在 token 空间里做"零基预算"——每个工具的 schema 都要证明自己值得占用 context。这对任何 harness 设计都适用：先算清楚 context 预算再堆功能。

2. **验证的"对抗性"设计不是态度问题，是架构选择。** Claude Code 的 Verification Agent 和 Anthropic harness 博客的 evaluator 是同一个模式在不同粒度的实现。关键不是"让模型认真检查"（这做不到），而是**结构上分离生产者和检查者**，然后给检查者注入怀疑倾向。这和 code review 的 "assume the code is wrong" 原则一样——是制度设计而非个人意愿。

3. **Plan-first 翻转了时间分配。** "规划 2h → 执行 10min → 审查 1h" 意味着人的核心价值在"定义做什么"和"判断做得好不好"，而不是"怎么做"。这直接呼应了 Harness Engineering 的核心转变：工程师从 implementer 变成 designer + evaluator。70 个 plan 文件 / 263 commits 的实战数据是很好的量化支撑。

4. **6 阶段工具治理 pipeline 是"约束即加速"的微观体现。** 从 input validation → speculative classification → PreToolUse hooks → permission → execute → PostToolUse hooks，每一层都是约束。但这些约束不是减速带——speculative classification 减少等待，hooks 注入自动化修复指令。这与 OpenAI 的"linter 是加速器不是减速器"完全对齐。

5. **Skill 是可分发的 prompt 工程。** Anthropic 把 skills 分成 9 类、强调 "description 是触发条件"、推荐 "gotchas 区块"——这些经验可以直接搬到任何 harness 的 tool/capability 设计中。Skill 本质上是把"人对 Agent 的期望"编码成结构化指令，写好一次，复用 N 次。

6. **社区生态的分化暗示了两种用户画像。** Superpowers（全自动、高信任、"让 Agent 自己来"）和 CE（半自动、plan-first、"人在 loop"）代表了两种哲学。你需要在两者之间找到自己的平衡点——当前你的 personal repo 更接近 CE 模式（知识积累导向），但项目 2（可展示的 harness 项目）可能需要 Superpowers 式的高吞吐量。

## 与已有知识的关系

- **wiki/harness-engineering/** 的三支柱（评估、架构、记忆）在 Claude Code 中全部有对应实现：Verification Agent 对应评估支柱，6 层架构 + hooks 对应架构支柱，CE /compound 对应记忆支柱。Claude Code 是目前最好的"harness 参考实现"。

- **wiki/harness-engineering/evaluator-generator.md** 中的 V1/V2 演进在 Claude Code 中有微观映射：早期更多约束（strict permissions）→ 模型变强后放松约束（auto-accept edits），但验证层不移除。

- **wiki/harness-engineering/agent-environment-design.md** 中 OpenAI 的"地图而非手册"、"架构约束机械执行"、"错误消息注入修复指令"在 Claude Code 中全部有具体实现：CLAUDE.md 做地图、hooks/linter 做机械执行、tool failure 消息注入 context 做自动修复。

- **wiki/harness-engineering/compound-engineering.md** 中讨论的 CE 知识积累机制，现在有了完整的产品实现参考（/ce:compound 的三 agent 架构、去重逻辑、docs/solutions/ 结构）。

## 对你的具体建议

1. **你的 personal repo 现在是一个三层 harness showcase。** 从 Batch 1 report 建议的"这个 repo 是 harness showcase"更进一步——现在你可以精确对照：CLAUDE.md = 架构约束层，/compile skill = evaluator 闭环，wiki/ = 记忆层（CE /compound 的个人知识版）。在面试中可以用 Claude Code 的 6 层架构作为 framing，然后展示你的 repo 如何实现了其中的关键层。

2. **项目 1（深化 personal repo）的 `/ingest` multi-agent 改造有了具体参考架构。** CE 的三 agent compound 模式（Context Analyzer + Solution Extractor + Related Docs Finder）可以直接映射到 ingest 场景：Content Analyzer（内容质量评估）+ Knowledge Extractor（知识点提取）+ Dedup Checker（与 wiki 已有知识去重）。这比"一个 agent 评估质量"更有架构说服力。

3. **项目 2（可展示的 harness 项目）现在可以更具体了。** 建议方向：**用 Claude Agent SDK 复刻 Claude Code 的验证层**——做一个"mini Claude Code"，聚焦 generator-evaluator 循环 + tool governance pipeline。scope 控制在 3-5 个工具、1 个 evaluator、1 个 generator。可以跑两组对比：有/无 evaluator 的代码质量差异 + 有/无 tool governance 的执行安全性差异。

4. **Context 经济学的理解是一个可讲的面试故事。** "200K token 中实际可用多少"这个问题，大多数人没有具体认知。你可以在面试中用这个作为切入点："我在构建 harness 时发现 context 预算管理是第一个瓶颈…"，然后展开到 deferred tools、prompt caching、context compaction 等优化手段。

5. **每周 inbox 阅读时，建议开始追踪 Claude Code 的 changelog。** 从 Opus 4.5 → 4.6 的变化（sprint 分解变为可移除）说明工具演进很快。作为 AI 工程师，了解工具演进是"保质期"意识的实践。

## Wiki 更新摘要

- **wiki/claude-code/architecture-overview.md**（新建）— 6 层架构、14 步 agent pipeline、system prompt 动态组装、cache-aware fork
- **wiki/claude-code/context-engineering.md**（新建）— 200K token 预算分配、MCP 隐形成本、deferred tools、prompt caching、成本控制策略
- **wiki/claude-code/tool-governance.md**（新建）— 6 阶段工具执行 pipeline、三种权限模式、hooks 系统、settings.json 配置
- **wiki/claude-code/skills-design.md**（新建）— 9 大 skill 类别、description 作为触发条件、gotchas 区块、渐进式披露、分发策略
- **wiki/claude-code/verification-patterns.md**（新建）— Verification Agent 对抗性设计、验证闭环、验证层级、与 evaluator-generator 的关系
- **wiki/claude-code/workflow-patterns.md**（新建）— Plan-first、vibe coding 两阶段、多会话并行、移动端/远程、实用技巧
- **wiki/claude-code/plugins-ecosystem.md**（新建）— Superpowers 5-skill 工作流、CE 知识复利机制、插件架构
- **wiki/claude-code/workflow-commands.md**（更新）— 修复来源引用路径 inbox/ → resources/
- **wiki/claude-code/_index.md**（更新）— 从 1 个文件扩展到 8 个，重写核心概念和跨主题连接
- **wiki/_index.md**（更新）— claude-code 文件数 1→8，新增跨主题概念

## 值得讨论的问题

1. **你目前使用 Claude Code 的模式更接近 Superpowers 还是 CE？** 两种模式适合不同场景——Superpowers 适合快速迭代出原型，CE 适合需要长期维护的项目。你的 personal repo 显然是 CE 模式，但你的项目 2（面试 showcase）可能需要不同策略。你怎么规划两个项目的工作流差异？

2. **Context 经济学对你当前的 /compile skill 有什么实际影响？** /compile 需要读大量文件（inbox + wiki + areas），每次调用可能消耗大量 context。你有没有感觉到某些操作因为 context 不够而质量下降？是否需要给 /compile 加入 context budget 管理？

3. **Deferred tools 的设计思路能否应用到你的 wiki 架构？** Wiki 的 _index.md 做的就是类似"延迟加载"——先读索引，按需读具体文件。但这依赖 LLM 自己的判断力。有没有办法让这个"渐进式披露"更结构化，比如给不同 wiki 文件加权重或热度标签？

4. **"规划 2h 执行 10min 审查 1h"这个时间分配在你当前每天 1-2h 的约束下现实吗？** 如果每天只有 1-2h，你可能没时间做完整的 plan-first 循环。是否需要一种"轻量 plan"模式——比如 10min 规划 + 执行 + 10min 审查？或者把规划集中在周末，工作日只做执行和审查？

5. **社区源码分析（中文）的信息可靠性如何验证？** 两篇中文万字长文提供了大量实现细节，但它们是基于逆向工程/源码阅读得出的。这些细节可能随版本更新而过时。你觉得这类"非官方但详细"的信息在 wiki 中应该怎么标注可信度？
