# Self-Attention Mechanism

Transformer 的核心计算单元。让序列中每个 token 都能"看到"并加权聚合其他所有 token 的信息，替代了 RNN 的顺序处理。

## 计算步骤

1. **生成 Q/K/V 向量**：每个 token 的 embedding 分别乘以三个权重矩阵 Wq, Wk, Wv
   - 原始论文：d_model=512, d_k=d_v=64（512/8 heads）
2. **计算注意力分数**：`score = Q · Kᵀ`（点积）
3. **缩放**：`score / √d_k`（防止点积过大导致 softmax 梯度消失）
4. **Softmax**：归一化为概率分布
5. **加权求和**：`Attention(Q,K,V) = softmax(QKᵀ/√d_k) · V`

## Multi-Head Attention

不用单个大 attention，而是用多个小 attention 并行运行：

```
MultiHead(Q,K,V) = Concat(head₁, ..., headₕ) · W_O

headᵢ = Attention(QWᵢᑫ, KWᵢᴷ, VWᵢⱽ)
```

- **h=8** heads，每个 head 处理 d_k=64 维
- 不同 head 学习不同类型的关系（语法依赖、语义相似、位置关系等）
- 最终 concat 后通过 W_O 矩阵（512×512）投影回原始维度

## Masked Self-Attention

Decoder 中使用，防止 token 看到未来位置的信息：
- 把注意力矩阵中未来位置的分数设为 `-∞`
- Softmax 后这些位置权重变为 0
- 保证了自回归生成的因果性

## 复杂度分析

- 时间复杂度：O(n² · d)，n=序列长度，d=维度
- 空间复杂度：O(n²)（注意力矩阵）
- 这是长序列处理的瓶颈，催生了各种高效 attention 变体（Flash Attention, Sliding Window 等）

## 直觉理解

把 Q/K/V 理解为信息检索：
- **Q（Query）**：「我在找什么信息？」
- **K（Key）**：「我有什么信息可以提供？」
- **V（Value）**：「我的实际内容是什么？」

Q·K 的点积就是"查询和键的匹配度"，匹配度高的 V 权重就大。

> 来源：resources/jay-alammar/20260404-the-illustrated-transformer-jay-alammar-visualizin.md

→ [Transformer Architecture](transformer-architecture.md)
→ [KV Caching](kv-caching.md)
