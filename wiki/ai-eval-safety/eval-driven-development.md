# Eval Driven Development (EDD)

借鉴 TDD（Test Driven Development），把评估（eval）作为 LLM 应用开发的核心驱动力。先写 eval，再优化系统。

## 核心理念

> "如果你没有 eval，你就是在盲飞。"

传统软件：写代码 → 写测试 → 修 bug → 发布
LLM 应用：**写 eval → 改 prompt / 改 pipeline → 跑 eval → 迭代**

## 实践方法

### Step 1: 定义评估集
- 收集真实用户查询（或合成代表性查询）
- 每个查询配参考答案或评估标准
- 初始 50 条就够启动，持续增长

### Step 2: 建立评估 pipeline
- Level 1: 断言测试（格式、长度、关键词）
- Level 2: LLM-as-Judge（语义质量）
- 自动化，可以 `python run_evals.py` 一键跑

### Step 3: 以 eval 指导优化
- 每次改动（prompt、retrieval 参数、模型）都跑 eval
- 量化对比前后效果
- 避免"凭感觉调参"

## 案例：Hamel Husain 的实践

### Lucy（AI chatbot）
- 问题：prompt 越改越长，效果反而下降
- 解法：建 eval dataset → 发现问题出在 retrieval 而非 prompt → 修复 RAG pipeline
- 教训：没有 eval 就不知道真正的瓶颈在哪

### Rechat（房产 AI 助手）
- 通过系统化 eval 发现：85% 的失败来自 3 类问题
- 针对性修复后效果大幅提升
- 不需要换模型或改架构，只需要知道哪里出了问题

## 与传统软件测试的对比

| 维度 | 传统测试 | LLM Eval |
|------|---------|----------|
| 确定性 | 输入→输出确定 | 输入→输出不确定 |
| 通过标准 | 二值（pass/fail） | 连续分数 |
| 测试方法 | 单元测试、集成测试 | 断言 + LLM-as-Judge + 人工抽检 |
| 覆盖率 | 代码覆盖率 | 场景覆盖率 |

## 实践要点

- Eval 是 LLM 应用最高 ROI 的投入——比换模型、调 prompt 都重要
- 从小 eval set 开始，随着发现的 failure case 逐步扩充
- 把 eval 当成活文档——随着用户行为变化持续更新
- 和 CI/CD 集成：每个 PR 自动跑 eval

> 来源：resources/hamel-husain/20260404-untitled.md
> 来源：resources/eugene-yan/20260404-untitled.md

→ [LLM Evaluation Methods](llm-evaluation-methods.md)
→ [LLM-as-Judge](llm-as-judge.md)
→ [glossary/Evaluator-Generator](../glossary/evaluator-generator.md)
