# Transformer

2017 年 Vaswani et al. 提出的序列建模架构（"Attention Is All You Need"）。完全基于 attention 机制，没有递归，可高度并行化。现代 LLM 的基础。

## 核心结构

Encoder + Decoder，各 N 层。每层 = Self-Attention + Feed-Forward + 残差连接 + LayerNorm。现代 LLM 几乎全部采用 decoder-only 变体（GPT、Claude、LLaMA）。

## 解决什么问题

取代 RNN/LSTM 的序列处理：消除了递归依赖，任意两个位置 O(1) 连接（vs RNN 的 O(n)），训练高度并行化。

→ 深度阅读：[ml-fundamentals/transformer-architecture](../ml-fundamentals/transformer-architecture.md)
