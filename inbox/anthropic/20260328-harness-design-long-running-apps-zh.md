---
source: "anthropic"
url: "https://www.anthropic.com/engineering/harness-design-long-running-apps"
date: "2026-03-28"
tags: [AI, agents, harness-design, Claude, engineering]
---

## Summary

本文是 Anthropic Labs 团队成员 Prithvi Rajasekaran 分享的多 agent 架构设计经验。作者从前端设计质量和长时间自主编码两个问题出发，借鉴 GAN 的思路，设计了 generator-evaluator 双 agent 架构，通过分离「生成」与「评估」来解决模型自我评价过于宽松的问题。在前端设计领域，作者制定了四个评分标准（设计质量、原创性、工艺、功能性），并通过多轮迭代显著提升了设计质量。随后将此模式扩展到全栈开发，形成 planner-generator-evaluator 三 agent 架构，能在数小时的自主编码中产出功能完整的 Web 应用。文章还讨论了随着模型能力提升（从 Opus 4.5 到 4.6），如何简化 harness 设计——移除 sprint 结构、减少 context reset，同时保留真正 load-bearing 的组件。

---

_作者：Prithvi Rajasekaran，Anthropic [Labs](https://www.anthropic.com/news/introducing-anthropic-labs) 团队成员。_

过去几个月来，我一直在研究两个相互关联的问题：让 Claude 产出高质量的前端设计，以及让它在无需人工干预的情况下构建完整的应用。这项工作源于我们此前在 [frontend design skill](https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md) 和[长时间运行的编码 agent harness](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) 上的努力。在这些早期工作中，我和同事们通过 prompt engineering 和 harness 设计将 Claude 的表现显著提升到了基线之上——但两者最终都遇到了天花板。

为了突破瓶颈，我探索了在两个截然不同的领域中都适用的新型 AI 工程方法——一个领域由主观审美定义，另一个由可验证的正确性和可用性定义。受 [生成对抗网络](https://en.wikipedia.org/wiki/Generative_adversarial_network)（GAN）的启发，我设计了一个包含 **generator**（生成器）和 **evaluator**（评估器）的多 agent 结构。构建一个能够可靠评分——且具有审美品味的评估器，意味着首先需要建立一套标准，将「这个设计好不好？」这类主观判断转化为具体的、可评分的维度。

随后我将这些技术应用到了长时间自主编码中，并延续了早期 harness 工作中的两个经验：将构建过程分解为可控的模块，以及使用结构化的 artifact 在会话之间传递上下文。最终的成果是一个三 agent 架构——planner（规划器）、generator（生成器）和 evaluator（评估器）——在数小时的自主编码会话中产出了功能丰富的全栈应用。

## 为什么朴素实现效果不佳

我们此前已经展示过，harness 设计对长时间 agentic 编码的效果有着显著影响。在早期的一次[实验](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)中，我们使用一个 initializer agent 将产品规格分解为任务列表，然后用一个 coding agent 逐个实现功能，再通过 artifact 在会话之间传递上下文。开发者社区也趋向了类似的洞察，比如「[Ralph Wiggum](https://ghuntley.com/ralph/)」方法，通过 hooks 或脚本让 agent 持续迭代。

但一些问题仍然持续存在。对于更复杂的任务，agent 仍然倾向于随时间推移而失控。在分析这个问题时，我们观察到了 agent 在执行这类任务时的两种常见失败模式。

**第一个问题**是，模型在冗长的任务中，随着 context window 填满，往往会失去连贯性（参见我们关于 [context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) 的文章）。一些模型还会表现出「context 焦虑」——当它们认为接近 context 容量上限时，会过早地开始收尾工作。Context reset——完全清空 context window 并启动新的 agent，同时通过结构化的 handoff 携带前一个 agent 的状态和后续步骤——可以同时解决这两个问题。

这与 compaction（压缩）不同。Compaction 是将对话早期部分就地摘要，让同一个 agent 在缩短后的历史上继续工作。虽然 compaction 保留了连续性，但它没有给 agent 一个全新的起点，这意味着 context 焦虑仍然可能持续。Reset 提供了一个干净的起点，代价是 handoff artifact 需要携带足够的状态，让下一个 agent 能够顺利接手工作。在我们早期的测试中，我们发现 Claude Sonnet 4.5 的 context 焦虑非常明显，仅靠 compaction 不足以支撑长任务的良好表现，因此 context reset 成为了 harness 设计的关键。这解决了核心问题，但也给每次 harness 运行增加了编排复杂性、token 开销和延迟。

**第二个问题**，我们此前未曾解决的，是自我评估。当被要求评估自己产出的工作时，agent 倾向于自信地称赞自己的工作——即使在人类观察者看来，质量明显平庸。这个问题在设计等主观任务中尤为突出，因为没有等价于可验证软件测试的二元检查。一个布局是精致还是平庸，是一个判断问题，而 agent 在评价自己的工作时始终偏向正面。

然而，即使在有可验证结果的任务上，agent 有时也会表现出影响其完成任务表现的糟糕判断。将「做工作的 agent」和「评判工作的 agent」分离，被证明是解决此问题的有力杠杆。这种分离本身并不能立即消除宽松倾向——evaluator 仍然是一个对 LLM 生成内容倾向慷慨的 LLM。但调优一个独立的 evaluator 使其持怀疑态度，比让 generator 对自己的工作持批判态度要容易得多，而一旦有了外部反馈，generator 就有了可以针对性迭代的具体内容。

## 前端设计：让主观质量变得可评分

我从前端设计入手进行实验，因为自我评估问题在这里最为明显。在没有任何干预的情况下，Claude 通常会倾向于安全、可预测的布局——技术上能用但视觉上毫无亮点。

构建前端设计 harness 的两个关键洞察。**第一**，虽然审美不能完全简化为分数——个人品味也总会有差异——但可以通过编码设计原则和偏好的评分标准来改善。「这个设计漂亮吗？」很难一致地回答，但「这是否遵循了我们的优秀设计原则？」给了 Claude 具体的评分依据。**第二**，通过将前端生成和前端评分分离，我们可以创建一个反馈循环，推动 generator 产出更强的输出。

基于此，我编写了四个评分标准，同时提供给 generator 和 evaluator agent 的 prompt：

- **设计质量：** 设计是否感觉像一个连贯的整体，而不是各部分的拼凑？这里的优秀表现意味着颜色、排版、布局、图像和其他细节结合在一起创造出独特的氛围和身份。
- **原创性：** 是否有自定义决策的痕迹，还是模板布局、库默认值和 AI 生成模式的堆砌？人类设计师应该能识别出刻意的创意选择。未修改的现成组件——或 AI 生成的典型特征如白色卡片上的紫色渐变——在此项不合格。
- **工艺：** 技术执行：排版层次、间距一致性、色彩和谐、对比度。这是能力检查而非创意检查。大多数合理的实现默认情况下都能通过；不合格意味着基本功有问题。
- **功能性：** 与审美无关的可用性。用户能否理解界面的功能、找到主要操作、并且不需要猜测就能完成任务？

我强调设计质量和原创性，而非工艺和功能性。Claude 在工艺和功能性上默认表现就不错，因为所需的技术能力对模型来说是自然而然的。但在设计和原创性上，Claude 的产出往往乏善可陈。评分标准明确惩罚高度通用的「AI slop」模式，通过更高权重的设计和原创性来推动模型承担更多审美风险。

我使用带有详细评分分解的 few-shot 示例来校准 evaluator。这确保了 evaluator 的判断与我的偏好一致，并减少了迭代过程中的评分漂移。

我基于 [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview) 构建了这个循环，使编排保持简洁。Generator agent 首先根据用户 prompt 创建了一个 HTML/CSS/JS 前端。我给 evaluator 配备了 Playwright MCP，让它能够在评分每个标准并撰写详细评论之前直接与实时页面交互。在实践中，evaluator 会自主导航页面，截图并仔细研究实现，然后给出评估。该反馈作为下一次迭代的输入流回 generator。每次生成我运行 5 到 15 次迭代，每次迭代通常将 generator 推向更独特的方向，因为它在响应 evaluator 的评论。由于 evaluator 是在主动导航页面而非评分静态截图，每个循环都需要实际的时钟时间。完整运行最长可达四小时。我还指示 generator 在每次评估后做出战略决策：如果分数趋势良好就改进当前方向，如果方法不奏效就彻底转向完全不同的审美。

在多次运行中，evaluator 的评估分数在迭代过程中持续改善然后趋于平稳，仍有提升空间。有些生成过程是渐进式改进，有些则在迭代之间发生了剧烈的审美转变。

评分标准的措辞以我未完全预料到的方式引导了 generator。包含诸如「最好的设计具有博物馆级品质」之类的短语推动设计向特定的视觉收敛，这表明与标准相关的 prompting 直接影响了产出的特征。

虽然分数通常随迭代改善，但模式并不总是线性的。后期的实现整体上往往更好，但我经常看到我更喜欢中间某次迭代而非最后一次的情况。实现复杂度也在各轮之间持续增加，generator 在 evaluator 反馈的推动下寻求更有雄心的解决方案。即使在第一次迭代中，产出也明显优于完全没有 prompting 的基线，这表明标准本身及相关语言就已经在任何 evaluator 反馈导致进一步改进之前，将模型引导远离了通用默认值。

一个值得注意的例子是，我提示模型为一家荷兰艺术博物馆创建网站。到第九次迭代时，它产出了一个为虚构博物馆设计的简洁、暗色主题着陆页。页面视觉上很精致，但基本在我的预期范围内。然后，在第十个循环中，它完全推翻了之前的方案，将网站重新构想为一种空间体验：一个用 CSS 透视渲染的带方格地板的 3D 房间，艺术品以自由形式的位置挂在墙上，并用门廊式导航在画廊房间之间切换，而非滚动或点击。这是一种我此前从未在单次生成中见过的创意飞跃。
