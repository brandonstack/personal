# Seq2Seq 与 Attention 的起源

Transformer 的前身。理解 seq2seq + attention 有助于理解为什么 Transformer 的 self-attention 是一次质的飞跃。

## Seq2Seq（Encoder-Decoder RNN）

2014 年 Sutskever et al. 提出，用两个 RNN 做序列到序列任务（翻译、摘要等）：

```
[输入序列] → Encoder RNN → [上下文向量 c] → Decoder RNN → [输出序列]
```

**核心问题**：整个输入序列被压缩成一个固定维度的上下文向量 c。长句子信息严重损失（"信息瓶颈"问题）。

## Attention 机制的诞生

### Bahdanau Attention (2014)
- 不再只用最后一个隐藏状态，而是让 decoder 每步都能"回看"encoder 所有时间步的隐藏状态
- 对每个 encoder 隐藏状态计算一个 alignment score（用一个小神经网络）
- 加权求和得到动态上下文向量
- 本质：**学习"该看哪里"**

### Luong Attention (2015)
- 简化了 alignment 计算：用点积代替神经网络
- 提出了多种 score 函数：dot、general、concat
- 更高效，效果相当

## 从 Seq2Seq Attention 到 Self-Attention 的飞跃

| 特征 | Seq2Seq Attention | Self-Attention |
|------|-------------------|----------------|
| 作用范围 | Decoder → Encoder（跨序列）| 序列内部（自身 → 自身）|
| 递归依赖 | 有（RNN 按时间步顺序处理）| 无（完全并行）|
| 长距离依赖 | 依赖 RNN 传递，衰减严重 | 任意两个位置直接连接（O(1)）|
| 计算效率 | 无法并行（O(n) 串行步骤）| 高度并行（O(1) 步骤，O(n²) 操作）|

关键突破：Self-Attention 让**每个位置都能直接注意到其他所有位置**，消除了 RNN 的序列瓶颈。这就是 "Attention Is All You Need" 的核心含义——不需要递归了，attention 本身就够了。

## 历史意义

Seq2Seq attention 是一个过渡技术，但它建立了关键直觉：
1. 动态地选择性关注输入的不同部分（attention）
2. 加权聚合比固定压缩更有效（attention > bottleneck）
3. 对齐（alignment）可以被学习

这些直觉直接被 Transformer 继承并推向极致。

> 来源：resources/jay-alammar/20260404-visualizing-a-neural-machine-translation-model-mec.md

→ [Transformer Architecture](transformer-architecture.md)
→ [Self-Attention Mechanism](self-attention-mechanism.md)
