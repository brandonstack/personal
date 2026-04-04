# Transformer Architecture

2017 年 Vaswani et al. 提出的序列建模架构，彻底取代了 RNN/LSTM 成为 NLP 和 LLM 的基础。核心创新：完全基于 attention 机制，没有递归，可以高度并行化。

## 架构总览

```
Input → Embedding + Positional Encoding → [Encoder × N] → [Decoder × N] → Linear → Softmax → Output
```

- **Encoder**（N=6）：每层 = Self-Attention + Feed-Forward，各带残差连接 + LayerNorm
- **Decoder**（N=6）：每层 = Masked Self-Attention + Encoder-Decoder Attention + Feed-Forward
- **原始参数**：d_model=512, heads=8, d_ff=2048, 约 65M 参数

## 关键组件

### Positional Encoding
Transformer 没有序列顺序感知（不像 RNN），通过位置编码注入顺序信息：
- 原始论文：正弦/余弦函数（偶数维 sin，奇数维 cos）
- 现代变体：旋转位置编码（RoPE）、相对位置编码（ALiBi）

### Feed-Forward Network
每层的 FFN 是两个线性变换 + ReLU，维度先扩展 4 倍再压回：
```
FFN(x) = max(0, xW₁ + b₁)W₂ + b₂
```
512 → 2048 → 512。这是参数量最大的部分。

### 残差连接 + Layer Normalization
每个子层（attention / FFN）都有 `LayerNorm(x + Sublayer(x))`，使深层训练稳定。

## 原始论文结果

- **En→De**: 28.4 BLEU（当时 SOTA）
- **En→Fr**: 41.8 BLEU
- 训练成本：8 GPU × 3.5 天，远低于之前的 SOTA 模型

## 演进方向

| 变体 | 结构 | 代表模型 |
|------|------|----------|
| Encoder-only | 仅 encoder | BERT, RoBERTa |
| Decoder-only | 仅 decoder + masked attention | GPT 系列, Claude, LLaMA |
| Encoder-Decoder | 完整结构 | T5, BART, 原始 Transformer |

现代 LLM 几乎全部采用 **decoder-only** 架构。

> 来源：resources/jay-alammar/20260404-the-illustrated-transformer-jay-alammar-visualizin.md
> 来源：resources/vaswani-et-al/20260404-170603762-attention-is-all-you-need.md
> 来源：resources/nvidia/20260404-untitled.md

→ [Self-Attention Mechanism](self-attention-mechanism.md)
→ [Decoder-only Transformers](decoder-only-transformers.md)
→ [Seq2Seq 与 Attention 的起源](seq2seq-attention.md)
