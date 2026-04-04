# Fine-tuning Methods

在预训练模型基础上，用任务特定数据进一步训练的技术族谱。从全参数微调到参数高效方法，从监督学习到人类偏好对齐。

## 方法分类

### 全参数微调（Full Fine-tuning）
- 更新模型所有参数
- 效果最好，但成本最高
- 需要和预训练同等规模的硬件
- 灾难性遗忘风险：在新任务上训练可能破坏通用能力

### 参数高效微调（PEFT）

只更新少量参数，冻结大部分预训练权重：

| 方法 | 原理 | 额外参数量 | 特点 |
|------|------|-----------|------|
| **LoRA** | 在每层的权重矩阵旁加低秩分解矩阵 ΔW=BA | ~0.1-1% | 最流行，可合并回原权重 |
| **QLoRA** | LoRA + 4-bit 量化基础模型 | ~0.1% | 单卡可微调 65B 模型 |
| **Prefix Tuning** | 在每层 attention 前加可学习的前缀向量 | ~0.1% | 不修改模型结构 |
| **Adapter** | 在 FFN 后插入小型 bottleneck 层 | ~1-3% | 模块化，可插拔 |
| **Soft Prompt Tuning** | 只学习 prompt 的 embedding | <0.01% | 最轻量，但效果有限 |

### Instruction Fine-tuning
- 在 (instruction, response) 对上训练
- 让模型学会遵循指令格式
- 代表：FLAN-T5, Alpaca, Vicuna
- 是 "base model → chat model" 的关键步骤

### RLHF（Reinforcement Learning from Human Feedback）
1. 收集人类偏好数据（A vs B 哪个回答更好）
2. 训练 reward model
3. 用 PPO 算法优化 LLM 使 reward 最大化
- 代表：ChatGPT, Claude（早期）

### RLAIF / Constitutional AI
- 用 AI 替代人类做偏好标注
- → [Constitutional AI](../ai-eval-safety/constitutional-ai.md)

## 何时用什么

| 场景 | 推荐方法 |
|------|---------|
| 通用能力提升 | Instruction fine-tuning |
| 特定领域知识 | LoRA/QLoRA + 领域数据 |
| 输出格式控制 | LoRA 或 instruction tuning |
| 对齐（安全、有用） | RLHF / RLAIF |
| 快速实验 | Soft prompt tuning |
| 显存受限 | QLoRA |

## 实践要点

- Fine-tuning 前先试 **few-shot prompting + RAG**——很多任务不需要微调
- LoRA rank（r）通常 8-64 就够，更大不一定更好
- 数据质量 >> 数据量。1000 条高质量数据 > 100K 条噪声数据
- 学习率要比预训练低 10-100 倍（1e-5 ~ 5e-5 常见）

> 来源：resources/nvidia/20260404-untitled.md
> 来源：resources/eugene-yan/20260404-untitled.md

→ [Transformer Architecture](transformer-architecture.md)
→ [Constitutional AI](../ai-eval-safety/constitutional-ai.md)
