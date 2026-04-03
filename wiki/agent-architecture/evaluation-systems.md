# Agent 评测系统

评测系统本身的问题比 Agent 问题更难发现。**先修评测再改 Agent**——评测分数下降先查环境（资源不足/评分器 bug/测试脱节），再动 Agent。

## 三层结构

| 层级 | 职责 | 关键问题 |
|------|------|----------|
| **Task** | 定义测什么 | 是否覆盖真实失败场景？ |
| **Trial** | 跑多少次 | 采样次数够不够消除随机性？ |
| **Grader** | 怎么打分 | 评分器本身是否可靠？ |

评测必须同时覆盖 **transcript**（执行记录，Agent 怎么做的）和 **outcome**（环境最终状态，结果对不对）。

## 两个核心指标

| 指标 | 含义 | 用途 | 不能混用 |
|------|------|------|----------|
| **Pass@k** | k 次里至少一次通过 | 开发阶段验证能力边界 | 不适合上线质量评估 |
| **Pass^k** | k 次全部通过 | 回归测试保证上线质量 | 不适合探索能力上限 |

Pass@k 问的是"Agent 能不能做到"，Pass^k 问的是"Agent 每次都能做到吗"。

## 评分器类型

确定性从高到低：

1. **代码评分器**：有明确答案时优先使用（检查输出格式、断言条件、diff 匹配）
2. **模型评分器**：用 LLM 判断输出质量（需要评分 rubric，自身也有噪声）
3. **人工评分器**：最灵活但最贵，用于校准前两种评分器

## 搭建建议

1. **20-50 个真实失败案例**启动——不要用合成数据，用 Agent 实际犯过的错
2. **环境隔离**：每次评测从干净状态开始（避免上次残留影响结果）
3. **正例 + 反例都覆盖**：Agent 该做到的 + Agent 不该做的
4. **通过率接近 100% 时补更难的任务**：评测跑满了说明评测太简单
5. **第一个失败就建评测**：失败案例立刻转测试用例

## 两层可观测性

| 层 | 方式 | 覆盖率 |
|----|------|--------|
| **人工抽样标注** | 摸清失败模式 | 低但精准 |
| **LLM 自动评估** | 全量覆盖 | 高但有噪声 |

两层互相校准：人工发现新失败模式 → 写进自动评估 rubric；自动评估的异常 → 人工验证是否真的有问题。

## 采样策略

- 负反馈 100% 入队列
- 高 token 消耗优先检查
- 固定时间段随机采样
- 模型变更后 48h 全量评估

## 追踪（Trace）

每次执行记录：完整 Prompt + messages[] + 工具调用 + 推理链 + 输出 + token/延迟。

**事件流底座**：`tool_start` / `tool_end` / `turn_end` 三节点发事件，一次发布多路消费（日志/UI/评测/审查）。

→ [control-flow-patterns.md](control-flow-patterns.md) — 评估器-优化器控制模式
→ [../harness-engineering/evaluator-generator.md](../harness-engineering/evaluator-generator.md) — Evaluator-Generator 分离的设计模式
→ [../claude-code/verification-patterns.md](../claude-code/verification-patterns.md) — Claude Code 中评测思想的产品实现

> 来源：resources/20260319-agent-architecture-engineering-practice.md
