---
date: "2026-04-03"
sources:
  - resources/anthropic/20260328-harness-design-long-running-apps-zh.md
  - resources/openai/20260211-harness-engineering-zh.md
  - resources/20260328-prompt-context-harness-paradigm-shift.md
  - resources/clippings/一个从执行到记忆的完整 Agent Harness gstack + Compound Engineering：.md
  - resources/clippings/别再卷模型了，2026 年 Agent 的胜负手在 Harness！给你的Agent 搭操作系统吧.md
wiki_updated:
  - wiki/harness-engineering/harness-generations.md
  - wiki/harness-engineering/evaluator-generator.md
  - wiki/harness-engineering/agent-environment-design.md
  - wiki/harness-engineering/compound-engineering.md
  - wiki/harness-engineering/_index.md
  - wiki/_index.md
---

# Harness Engineering：从 Prompt 到操作系统

## 这批材料在说什么

这批材料围绕同一个主题：2026 年初 Anthropic 和 OpenAI 几乎同时发布了各自的 Harness Engineering 实践，社区随即产生了大量解读和延伸。核心论点一致——模型能力趋同后，差距不在模型本身，而在包裹模型的运行时系统（Harness）。Anthropic 侧重 evaluator-generator 分离和 harness 随模型能力演进的简化，OpenAI 侧重零手写代码下的环境设计和架构约束机械执行，社区讨论则填补了记忆治理这一两家大厂都未深入的维度。

整体看，AI 工程正在经历第三次范式转移：Prompt Engineering → Context Engineering → Harness Engineering。每代包含前代，但核心问题完全不同——从"怎么说"到"知道什么"到"怎么持续稳定大规模地干活"。

## 关键洞察

1. **Agent 自评不可靠是第一性原理级别的发现。** Anthropic 和所有社区文章都把 evaluator-generator 分离放在最重要的位置。这不是可选优化，而是多 agent 系统的结构性需求。LLM 评价自己的产出永远偏正面——类似人类 confirmation bias，这是模型层面难以解决的问题，只能通过架构（分离）解决。

2. **Harness 组件编码模型局限性假设——这些假设有保质期。** Anthropic 从 Opus 4.5 到 4.6 的演进最能说明：sprint 分解和 context reset 从"必要"变为"可移除"，但 evaluator 仍然 load-bearing。识别哪些组件该留哪些该删，是 harness engineer 的核心判断力。Build to Delete 不是口号，是工程纪律。

3. **Anthropic 和 OpenAI 的方法互补而非竞争。** Anthropic 解决"如何确保质量"（评估闭环），OpenAI 解决"如何让 Agent 高效工作"（环境设计 + 架构约束）。两者加上记忆治理，构成完整 Harness 三支柱。社区已经开始做集成实践（gstack + CE 覆盖全部层次）。

4. **"地图而非手册"与本 repo 的 wiki 模式高度一致。** OpenAI 发现"一个大 AGENTS.md"不管用，需要结构化、可验证、有索引的知识库 + 渐进式披露。这正是我们刚建立的 wiki 架构的底层逻辑——CLAUDE.md 做目录表，wiki/ 做分层知识库。

5. **记忆层的价值在轨迹而非初始性能。** 学术研究显示 3 行 prompt + 记忆 ≈ 200 行专家 prompt，但差异在学习曲线——有记忆的系统 10 轮后显著提升，无记忆的系统停滞。这为"知识 compound"提供了实证支持。

6. **评分标准本身是 steering mechanism。** 这个发现对所有涉及 LLM 评估的工作都有启示：rubric 不仅衡量质量，更引导产出方向。标准的措辞直接影响 Agent 行为。

## 与已有知识的关系

- **wiki/ai-engineering/positioning-framework.md** 中定义的"能力迁移"路径（度量→评估、数据治理→记忆治理、后端设计→harness 架构）与这批材料高度验证。Harness Engineering 的三支柱（评估、架构、记忆）精确对应了这些迁移方向。
- **wiki/claude-code/workflow-commands.md** 中记录的 Claude Code 工具本身就是一个 harness 实现——/rewind, /branch 等命令对应 context 管理，skill 系统对应 tool 编排。
- 本 repo 从线性 workflow 到 wiki 模式的迁移，本质上就是从"备忘录"到"知识库"的转变——与 Compound Engineering 的核心洞察完全一致。

## 对你的具体建议

1. **你的 repo 本身就是 harness showcase。** areas/career/ai-engineer-roadmap.md 提到"这个 repo 本身就是小型 harness"——现在有了 wiki 模式后更是如此。在求职叙事中，可以用这个 repo 展示你对 harness 三支柱的理解：wiki 是记忆治理，compile skill 是评估闭环（LLM 消化 → report 生成 → 人审阅），CLAUDE.md + AGENTS.md 是架构约束。

2. **Multi-agent harness 项目方向可以直接对齐 evaluator-generator 模式。** roadmap 中提到的"设计 generator-evaluator 系统并调优评估标准"，现在有了 Anthropic 的具体实践（四维评分标准、sprint 合约、Playwright QA）作为参考，可以更具体地设计。

3. **4-7 月在职期，建议用微软的服务器资源做一次对比实验。** roadmap 提到"solo agent vs harness 同一任务，量化效果差异"。Anthropic 的数据（单 Agent 20min/$9 不可用 vs 完整 Harness 6h/$200 功能完整）是很好的 baseline，但用更小规模任务做可复现的对比会更有说服力。

4. **关注 CE 的 compound janitor 模式。** 这可能是你知识管理 agent 项目的一个具体切入点——判断哪些 session 值得 compound 本质上是一个知识价值评估问题，与你的度量工程背景高度相关。

## Wiki 更新摘要

- **wiki/harness-engineering/harness-generations.md**（新建）— 三代范式演进、Harness 三支柱、Build to Delete 原则、关键数据
- **wiki/harness-engineering/evaluator-generator.md**（新建）— Generator-Evaluator 分离模式全景：架构演进 V1→V2、评分标准设计、sprint 合约、调优实践
- **wiki/harness-engineering/agent-environment-design.md**（新建）— OpenAI 环境设计实践：地图式知识组织、架构约束机械执行、熵对抗机制
- **wiki/harness-engineering/compound-engineering.md**（新建）— 备忘录 vs 知识库、CE compound 机制、gstack+CE 全栈覆盖、记忆系统学术研究
- **wiki/harness-engineering/_index.md**（更新）— 新增 4 个文件的索引和核心概念
- **wiki/_index.md**（更新）— harness-engineering 文件数 0→4，新增跨主题概念

## 值得讨论的问题

1. **你认为 evaluator 调优的投入产出比在什么场景下最高？** Anthropic 说"开箱即用的 Claude 是糟糕的 QA agent"，需要多轮人工调优。在你的项目规划中，哪个场景最值得花这个调优成本？

2. **Build to Delete 原则如何应用到你的 wiki 架构？** wiki 文件也编码了"当前对知识结构的假设"。随着你消化更多材料，某些文件可能需要拆分或合并。你觉得目前的概念粒度（50-150 行/文件）会不会太粗或太细？

3. **OpenAI "零手写代码"的哲学在你的求职策略中怎么定位？** 这是一个激进的立场。你的目标公司会期望"懂得用 Agent"的工程师，还是"能证明不用 Agent 也行"的工程师？两种叙事的受众完全不同。

4. **记忆治理中的"知识价值评估"和你的度量工程背景有什么具体连接？** 判断什么值得 compound、什么是噪音，本质上是一个信号 vs 噪音问题——这正是你在 Bing Shopping Price Accuracy 中做过的事。这个连接能否成为一个更具体的项目方向？
