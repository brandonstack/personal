# Quantization

将模型权重和/或激活值从高精度（FP32/FP16）压缩到低精度（INT8/INT4）的技术。减少内存占用和推理成本，轻微质量损失。

## 为什么量化有效

- LLM 推理是 memory-bandwidth bound（decode 阶段）
- 权重读取量 = 参数量 × 精度字节数
- FP16 → INT8：读取量减半 → 理论推理速度提升 2×
- FP16 → INT4：读取量减 3/4 → 理论推理速度提升 4×

## 精度对比

| 精度 | 字节/参数 | 70B 模型大小 | 特点 |
|------|----------|-------------|------|
| FP32 | 4 | 280 GB | 训练用，推理太贵 |
| FP16/BF16 | 2 | 140 GB | 推理标准精度 |
| INT8 | 1 | 70 GB | ~2× 压缩，质量损失极小 |
| INT4 | 0.5 | 35 GB | ~4× 压缩，单卡可跑 70B |

## 主要方法

### Post-Training Quantization (PTQ)
训练后直接量化，不需要重新训练：

| 方法 | 量化目标 | 特点 |
|------|---------|------|
| **GPTQ** | 权重 → INT4 | 基于 layer-wise Hessian，需要校准数据 |
| **AWQ** | 权重 → INT4 | 保护重要权重不量化，更精确 |
| **BitsAndBytes** | 权重 → INT8/INT4 | HuggingFace 集成好，零配置 |
| **llama.cpp (GGUF)** | 权重 → 多种精度 | CPU 友好，支持多种量化级别（Q4_0, Q5_K_M 等）|

### Quantization-Aware Training (QAT)
训练过程中模拟量化效果：
- 质量更好，但需要重新训练
- 成本高，通常模型提供方做

## 质量影响

Cursor 的分析：
- INT8 量化：质量几乎无损（<1% 下降），成本约减半
- INT4 量化：部分任务有明显下降，但对大多数应用可接受
- 越大的模型量化损失越小（冗余参数多）

## 与其他优化的配合

- **量化 + QLoRA**：4-bit 量化基础模型 + LoRA 微调 → 单卡微调 65B 模型
- **量化 + Continuous Batching**：模型更小 → KV Cache 更小 → 可支持更大 batch
- **量化 + Speculative Decoding**：draft model 可以用更激进的量化

> 来源：resources/cursor/20260404-untitled.md
> 来源：resources/wan-et-al/20260404-240414294-a-survey-on-efficient-inference-for-larg.md

→ [LLM Inference Cost](llm-inference-cost.md)
→ [GPU Architecture Fundamentals](gpu-architecture.md)
→ [Fine-tuning Methods](../ml-fundamentals/fine-tuning-methods.md)
