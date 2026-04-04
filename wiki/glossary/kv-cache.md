# KV Cache

自回归推理中缓存每层 attention 的 Key/Value 向量的优化技术。避免对已生成的 token 重复计算 K/V，将 decode 阶段的计算量从 O(n²) 降到 O(n)。

## 解决什么问题

自回归生成每步需要对所有已有 token 做 attention。不缓存的话，生成第 100 个 token 要重算前 99 个的 K/V。缓存后每步只增量计算新 token。

## 关键数字

Llama-2-70B（GQA, 8 KV heads）：约 320 KB/token/batch_element。是 LLM 推理内存的主要消耗之一。

→ 深度阅读：[ml-fundamentals/kv-caching](../ml-fundamentals/kv-caching.md)
→ 相关：[ai-infra/continuous-batching](../ai-infra/continuous-batching.md) — PagedAttention 解决 KV Cache 内存碎片
