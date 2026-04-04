# KV Caching

自回归生成中避免重复计算的关键优化。缓存每一层 attention 的 Key 和 Value 向量，新 token 只需计算自己的 Q/K/V 并查询缓存。

## 为什么需要 KV Cache

自回归生成时，每生成一个新 token 都需要对之前所有 token 做 attention。如果不缓存：
- 生成第 100 个 token 时，要重算前 99 个 token 的 K/V（浪费 99% 计算）
- 计算量从 O(n) 变成 O(n²)

有了 KV Cache：
- 前面 token 的 K/V 已缓存，只需计算新 token 的 Q/K/V
- 用新 Q 和缓存的所有 K 算 attention score，再和所有 V 加权求和
- 每步只增量计算，不重复

## 内存消耗

KV Cache 是推理时最大的内存消耗之一：

```
KV Cache per token = 2 × n_layers × d_model × dtype_size
```

以 Llama-2-70B 为例：
- 80 层 × 8192 维 × 2（K+V）× 2 bytes（FP16）= **2.56 MB/token**
- 实际用 Grouped Query Attention（GQA）：8 个 KV heads（vs 64 attention heads），约 **320 KB/token**
- 批量推理时：batch_size × seq_len × 320KB = 快速占满 GPU 显存

## Grouped Query Attention (GQA)

为了降低 KV Cache 内存，让多个 query head 共享同一组 KV head：

| 方式 | KV Heads | 内存 |
|------|----------|------|
| Multi-Head Attention (MHA) | 64 | 1× |
| Grouped Query Attention (GQA) | 8 | 1/8× |
| Multi-Query Attention (MQA) | 1 | 1/64× |

Llama-2-70B 使用 GQA（8 KV heads），KV Cache 缩小到 MHA 的 1/8。

## 与推理性能的关系

- **Prefill 阶段**：不需要 KV Cache，一次计算所有 token 的 K/V 并写入缓存
- **Decode 阶段**：每步读取整个 KV Cache → memory-bandwidth bound
- KV Cache 越大（长上下文 / 大 batch），decode 越慢
- 这就是为什么 generation 远比 prompt processing 贵

→ [vLLM 的 PagedAttention](../ai-infra/continuous-batching.md) 解决了 KV Cache 的内存碎片问题。

> 来源：resources/jay-alammar/20260404-the-illustrated-gpt-2-visualizing-transformer-lang.md
> 来源：resources/cursor/20260404-untitled.md

→ [Decoder-only Transformers](decoder-only-transformers.md)
→ [LLM Inference Cost](../ai-infra/llm-inference-cost.md)
→ [Continuous Batching](../ai-infra/continuous-batching.md)
