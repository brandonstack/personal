# PagedAttention

vLLM 提出的 KV Cache 内存管理技术，借鉴 OS 虚拟内存的 paging 机制。将 KV Cache 切成固定大小的 page，按需非连续分配。

## 解决什么问题

传统 KV Cache 按最大序列长度预分配连续内存，实际序列长度各异导致 60-80% 内存浪费。PagedAttention 用 page table 做逻辑→物理映射，浪费 < 4%。

## 关键意义

让 continuous batching 真正可行——更少的内存浪费意味着更大的 batch size，更高的吞吐量。vLLM 因此成为 LLM 推理服务的事实标准之一。

→ 深度阅读：[ai-infra/continuous-batching](../ai-infra/continuous-batching.md)
