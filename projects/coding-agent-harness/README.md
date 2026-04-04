# Coding Agent Harness

> 启动日期: 2026-04-02
> 代码仓库: TBD (GitHub: xingli/coding-agent-harness)
> 目标: 用 Claude Agent SDK 构建 multi-agent coding harness，展示 generator-evaluator 模式的量化效果

## 定位

不是复刻 Claude Code，是造一个**带 evaluator 的 coding agent 系统**。

核心叙事：generator agent 写代码，evaluator agent 检查质量并反馈，量化对比 solo agent vs harness 的效果差异。

## 完成标准

- [ ] Generator agent 能接受任务描述 → 写代码 → 跑测试
- [ ] Evaluator agent 能检查代码质量并打分（测试通过率、lint、架构规则、复杂度）
- [ ] 反馈循环：evaluator → generator 迭代，直到收敛
- [ ] 量化对比实验：solo agent 一次生成 vs harness 多轮迭代，通过率差异
- [ ] 能面试讲 5 分钟：架构、evaluator 调优过程、量化数据、trade-off

## 架构草案

```
Orchestrator
  ├─ Generator Agent（简化版 coding agent）
  │   ├─ Tools: read, write, edit, bash, grep
  │   ├─ 接收任务描述 → 写代码 → 跑测试
  │   └─ 接收 evaluator 反馈 → 修改代码
  │
  ├─ Evaluator Agent（核心价值）
  │   ├─ 评分维度: 测试通过率、lint 结果、架构规则、代码复杂度
  │   ├─ 输出: 0-100 分 + 具体改进建议
  │   └─ 决定: pass / 需要修改 / 放弃
  │
  └─ 反馈循环
      ├─ generator → evaluator → feedback → generator（最多 N 轮）
      ├─ 记录每轮分数变化
      └─ 输出: 量化报告
```

## 关键 Trade-off（待验证）

- Evaluator 太严 → 死循环不收敛；太松 → 放过低质量代码
- 评分维度权重怎么定？哪些维度 LLM 评得准，哪些需要机械化检查？
- 每轮 token 成本 vs 质量提升的边际收益
- 什么任务 harness 提升大，什么任务 solo agent 就够了？

## 时间线

| 周 | 目标 | 产出 |
|----|------|------|
| 第 1 周 | Agent SDK 学习 + MVP agent loop | 能跑的 agent，3 个 tool（read/write/bash） |
| 第 2 周 | 完善 generator agent | 接受任务 → 写代码 → 跑测试 |
| 第 3 周 | 造 evaluator agent | 评分维度设计 + 打分逻辑 |
| 第 4 周 | 反馈循环 + 对比实验 | 量化报告：solo vs harness |

## 设计决策记录

（随项目推进记录）

## 灵感来源

- [OpenAI: Harness Engineering](../../resources/openai/20260211-harness-engineering-original.md) — 0 行手写代码，人设计环境 + agent 执行
- [Anthropic: Building Effective Agents](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering) — generator-evaluator 模式

---

*Created: 2026-04-02*
