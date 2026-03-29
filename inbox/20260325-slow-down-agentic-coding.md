---
source: "Mario Zechner"
url: "https://mariozechner.at/posts/2026-03-25-thoughts-on-slowing-the-fuck-down/"
date: "2026-03-25"
tags: [AI-coding, agents, code-quality, engineering-culture]
---

# Thoughts on Slowing the Fuck Down

Coding agents 出现一年后，我们开始看到在生产代码库中大规模使用的后果。

## Everything is Broken

软件变得越来越脆弱，98% uptime 成了常态。迹象：
- AWS 疑似 AI 引发宕机 → 内部 90 天整改
- Satya Nadella 宣传 Microsoft 30% 代码由 AI 编写，Windows 质量明显下降，微软自己也发了博文承认
- 声称 100% AI 写代码的公司，产出一致是内存泄漏、UI 故障、崩溃
- 越来越多团队反映：agentically coded themselves into a corner——无 code review、架构决策委托给 agent、堆砌无人要的功能

## 不该怎么用 Agent

### 错误复合 + 零学习 + 无瓶颈 + 延迟痛感

Agent 和人都会犯错，关键区别：
1. **人会学习**，agent 不会——同样的错一遍遍犯。AGENTS.md / memory 系统只能覆盖你观察到的特定错误类别
2. **人是瓶颈**——一天写不了多少代码，booboo 复合速率低，痛感积累到阈值人会主动修。Agent 军团没有瓶颈，微小错误以不可持续的速率复合，你脱离 loop 后感知不到，等痛感来时已太晚
3. 最终你无法信任代码库，更糟的是 agent 写的测试同样不可信，唯一可靠的验证变成手动测试

### Agent 是复杂性贩子

Agent 的决策永远是局部的——看不到彼此的 run、看不到完整代码库、看不到之前的决策。结果：大量代码重复、为抽象而抽象、cargo cult "最佳实践"堆砌。

人类企业代码库花数年才烂到那个程度（组织随复杂性慢慢演化）。Agent + 2 人团队，几周就能到达同等复杂度。

### Agentic Search 召回率低

Agent 修复混乱前需要找到所有相关代码——无论用 ripgrep、代码索引、LSP 还是向量数据库，代码库越大，recall 越低。低 recall 正是 agent 一开始就产生重复和不一致的根源。

## 该怎么用 Agent

好的 agent 任务特征：
- **可限定范围**，不需要理解完整系统
- **闭环可验证**，agent 能评估自己的输出
- **非关键路径**，临时工具 / 内部软件
- **或仅作为 rubber duck**，用来碰撞想法

Karpathy 的 auto-research 模式有效，前提是你理解：评估函数只捕获窄指标（如启动时间），agent 会忽略所有未被评估的维度（代码质量、复杂度、正确性）。

核心建议：

> **Slow the fuck down.** 给自己时间想清楚在建什么、为什么建。给自己机会说"不需要这个"。设定每天让 agent 生成代码的上限，匹配你实际的 review 能力。

- **定义系统 gestalt 的部分（架构、API）手写**，或跟 agent pair programming——亲自在代码里才能感受系统的"手感"，这是你的经验和品味发挥作用的地方
- 你理解代码库 → 弥补 agentic search 的低 recall → agent 输出更好 → 需要更少修正
- 出问题时你能修，设计不理想时你知道为什么以及怎么重构

结果：更少功能但更对的功能，可维护的系统，能安心入睡的工程师。

> All of this requires discipline and agency. All of this requires humans.
