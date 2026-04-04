# Decoder-only Transformers

现代 LLM（GPT、Claude、LLaMA）的标准架构。只使用 Transformer 的 decoder 部分，通过 masked self-attention 实现自回归文本生成。

## 核心特征

- **自回归生成**：逐 token 生成，每个 token 只能看到之前的 token
- **Masked self-attention**：用 mask 遮住未来位置，保证因果性
- **无 encoder**：不需要单独的编码器，输入和输出共用同一个 decoder stack

## GPT-2 架构（以 124M 参数版本为例）

| 参数 | 值 |
|------|-----|
| 层数 | 12 |
| d_model | 768 |
| Heads | 12（每 head 64 维）|
| 上下文窗口 | 1024 tokens |
| 词汇表 | 50,257（BPE tokenizer）|
| FFN 扩展 | 4x（768 → 3072 → 768）|
| 参数量 | ~124M |

### 推理过程

1. Token embedding（50257 × 768）+ Position embedding（1024 × 768）
2. 通过 12 层 decoder block
3. 最后一层输出 → 线性投影到词汇表维度 → softmax → 概率分布
4. 采样策略：Top-k、Top-p（nucleus sampling）、Temperature

### 生成的两个阶段

| 阶段 | 操作 | 瓶颈 |
|------|------|------|
| **Prefill** | 一次性处理整个 prompt | Compute-bound |
| **Decode** | 逐 token 生成，每步利用 KV Cache | Memory-bound |

Prefill 可以高度并行（所有 prompt token 同时计算），decode 是串行的。

## Scaling 趋势

GPT-2 到 GPT-4 的演进说明了 scaling law 的有效性：

| 模型 | 参数量 | 上下文 |
|------|--------|--------|
| GPT-2 | 1.5B | 1024 |
| GPT-3 | 175B | 2048 |
| GPT-4 | ~1.8T (MoE) | 128K |
| Claude 3.5 | 未公开 | 200K |

## 与 Encoder-only 的区别

- **Decoder-only**（GPT）：生成任务（对话、写作、代码）
- **Encoder-only**（BERT）：理解任务（分类、NER、检索）
- 现代实践：decoder-only 模型通过 instruction tuning 也能做理解任务，因此成为主流

> 来源：resources/jay-alammar/20260404-the-illustrated-gpt-2-visualizing-transformer-lang.md
> 来源：resources/nvidia/20260404-untitled.md

→ [Transformer Architecture](transformer-architecture.md)
→ [KV Caching](kv-caching.md)
→ [Self-Attention Mechanism](self-attention-mechanism.md)
