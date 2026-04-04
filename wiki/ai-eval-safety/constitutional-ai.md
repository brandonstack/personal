# Constitutional AI

Anthropic 提出的 AI 对齐方法。用 AI 自身的反馈代替人类偏好标注（RLAIF），通过"宪法"原则引导模型自我修正，使模型无害且有用。

## 核心动机

RLHF 依赖大量人类偏好数据，但：
- 人工标注昂贵、慢、不一致
- 安全标注可能给标注者带来心理伤害
- Constitutional AI 目标：减少人类参与，同时保持（甚至超越）对齐效果

## 两阶段训练

### SL 阶段（Supervised Learning）
1. 用 red-teaming prompt 让模型生成有害回答
2. 让模型根据"宪法"原则**自我批评**（critique）
3. 让模型根据批评**自我修正**（revision）
4. 用修正后的 (prompt, revised_response) 对做监督微调

"宪法"示例原则：
- "请判断你的回答是否可能造成伤害"
- "请修改回答使其更有帮助且无害"

### RL 阶段（RLAIF）
1. 对于每个 prompt，生成两个回答
2. 让 AI（不是人类）根据宪法原则选择更好的回答
3. 用 AI 偏好数据训练 reward model
4. 用 RL（PPO）优化模型

## 与 RLHF 的关系

| 维度 | RLHF | Constitutional AI (RLAIF) |
|------|------|---------------------------|
| 偏好来源 | 人类标注 | AI 根据原则判断 |
| 成本 | 高（需大量标注者） | 低（AI 自动） |
| 可扩展性 | 受限于标注速度 | 可大规模生成 |
| 透明性 | 偏好标准隐含在标注者中 | 明确写在"宪法"原则中 |
| 质量 | 依赖标注者质量 | 依赖原则设计质量 |

## 意义

- 让 AI 对齐更透明（原则是公开的、可审计的）
- 让 AI 对齐更可扩展（不再受限于人工标注产能）
- Claude 的训练中使用了 Constitutional AI 方法

> 来源：resources/anthropic/20260404-constitutional-ai-harmlessness-from-ai-feedback.md

→ [LLM Evaluation Methods](llm-evaluation-methods.md)
→ [Fine-tuning Methods](../ml-fundamentals/fine-tuning-methods.md)
