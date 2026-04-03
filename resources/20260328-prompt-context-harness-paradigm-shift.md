---
source: "GoSailGlobal (Twitter)"
url: "https://x.com/GoSailGlobal/status/2037805864367911394"
date: "2026-03-28"
tags: [AI, engineering, agents, harness-engineering]
status: "compiled"
---

# Prompt → Context → Harness：AI 工程三次范式转移

2026 年初，Anthropic 和 OpenAI 几乎同一周发了各自关于 Harness Engineering 的实践文章，加上两篇 Agent 记忆基础设施的学术论文，一个完整图景浮现。

## 三代范式

| 阶段 | 时间 | 核心问题 | 优化对象 |
|------|------|---------|---------|
| **Prompt Engineering** | 2023-2024 | 怎么跟模型说话 | 人与模型的接口（措辞、few-shot、CoT） |
| **Context Engineering** | 2025 | 单靠提示词不够 | 模型的输入空间（RAG、长上下文、tool use、memory） |
| **Harness Engineering** | 2026 | Agent 自主运行数小时/天 | Agent 的整个运行时环境（多 Agent 协作、评估闭环、架构约束、记忆治理） |

每一代包含前一代，但核心问题完全不同。

## Anthropic：让 Agent 互相评估

反直觉发现：**Agent 自评基本没用**——不管输出质量高低，自评永远正面。拆成生成 + 评估两个独立 Agent 后效果完全不同。

评估器用 Playwright 实际操作页面（点按钮、填表单），按四维度打分：设计质量、原创性、工艺细节、功能完整度。

**对比数据**：
- 单 Agent：20 min / $9 → 产出不可用
- 完整 harness：6h / $200 → 交付完整游戏（精灵动画 + AI 集成 + 导出）

关键洞察：随着 Opus 4.6 能力提升，sprint 分解可以去掉，但评估器不能去掉。Harness 的每个组件都编码了对模型局限性的假设——模型变强后有些假设失效，有些永远成立。**识别哪些该留哪些该删，是 harness engineering 的核心技能。**

## OpenAI：百万行代码零手写

五个月，小团队用 Codex Agent 构建 ~100 万行生产代码，零手写。应用逻辑、文档、CI 配置、可观测性、工具链全由 Agent 生成。

工程师角色变为三件事：设计开发环境、用结构化 prompt 表达意图、给 Agent 提供反馈循环。

**架构治理是关键**：依赖层级严格分六层（Types → Config → Repo → Service → Runtime → UI），边界用 linter + CI 机械化执行，Agent 违反约束的 PR 自动拒绝。

> Martin Fowler：Harness Engineering 把 context engineering、架构约束和垃圾回收编码成了机器可读的制品，Agent 可以系统性地执行。

## 记忆系统：最容易被忽略的一层

两家大厂都没深入讨论记忆，这由两篇学术论文填补。

**(S)AGE 论文——拜占庭容错的多 Agent 记忆基础设施**

核心问题：多 Agent 共享知识库时，如何保证写入可信（幻觉/对抗性攻击）。

方案：Proof of Experience 共识机制。每个 Agent 有声誉权重（历史准确率 × 领域相关性 × 活跃度 × 独立验证数），记忆需加权投票验证后才写入。4 节点 BFT 网络：956 req/s 写入、21.6ms P95 查询。有记忆 Agent 校准精度 = 2× 无记忆基线。

**纵向学习论文——有记忆的 Agent 真的会随时间变好吗？**

实验设计：
- 治疗组：3 行 prompt + (S)AGE 记忆，可查询历史轮次知识
- 对照组：50-200 行专家 prompt，无记忆，每轮从零开始

10 轮后结果：
- 治疗组红队难度 0.8 → 3.0（Spearman ρ=0.716, p=0.020）
- 对照组无增长趋势（ρ=0.040, p=0.901）
- 两组绝对性能无统计差异（Cohen's d = -0.07）

**结论：3 行 prompt + 记忆 ≈ 200 行专家 prompt，但差异在学习轨迹——有记忆的系统越跑越好。** 记忆层带来的不是更高初始性能，而是组织级纵向学习能力。

## 总结

完整 Harness = 评估机制 + 架构约束 + 记忆治理。少了任何一层，Agent 系统都会在某个维度失控。

来源：Anthropic Engineering Blog / OpenAI Blog / (S)AGE Paper / Longitudinal Learning Paper
