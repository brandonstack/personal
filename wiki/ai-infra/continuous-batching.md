# Continuous Batching

动态批处理技术，解决静态 batching 的 GPU 利用率浪费问题。让推理服务器在请求级别动态调度，而非等一批全部完成。

## 静态 Batching 的问题

传统做法：收集 N 个请求 → 同时处理 → 等最长的完成 → 返回所有结果

```
Request A: [████████████████]
Request B: [████████░░░░░░░░]  ← 等待 A 完成
Request C: [████░░░░░░░░░░░░]  ← 等待 A 完成
```

问题：
- 短请求被长请求拖慢
- GPU 在等待期间空转
- 吞吐量远低于理论最大值

## Continuous Batching（Orca, OSDI'22）

核心思想：**iteration-level scheduling**——每个 decode 步骤后都可以插入新请求或移除已完成的请求。

```
Step 1: [A, B, C] 
Step 5: [A, B, -, D]     ← C 完成，D 插入
Step 8: [A, -, -, D, E]  ← B 完成，E 插入
```

- 不再等一批全部完成
- GPU 几乎始终满负荷
- 延迟和吞吐量同时改善

## PagedAttention（vLLM）

Continuous batching 的实际部署中，KV Cache 内存管理是关键挑战。

### 传统 KV Cache 的问题
- 预分配连续内存块（按最大序列长度）
- 实际序列长度各异 → 大量内存碎片和浪费
- 浪费高达 60-80% 的 KV Cache 内存

### PagedAttention 解决方案
受 **OS 虚拟内存** 启发：
- KV Cache 切成固定大小的 page（如 16 tokens/page）
- 不需要连续内存，按需分配 page
- 逻辑→物理地址映射（page table）
- **内存浪费 < 4%**

### 效果

| 方法 | 吞吐量提升（vs 静态 batching） |
|------|------|
| 静态 batching (baseline) | 1× |
| FasterTransformer（NVIDIA） | 4× |
| Naive continuous batching | 8× |
| **vLLM (PagedAttention)** | **23×** |

测试条件：OPT-13B on single A100 40GB，ShareGPT trace。

## vLLM 生态

vLLM 已成为 LLM 推理服务的事实标准之一：
- 支持：PagedAttention, speculative decoding, quantization（AWQ/GPTQ/BitsAndBytes）
- 支持：disaggregated prefill（prefill 和 decode 分离）
- 支持：LoRA serving, structured outputs, tool calling
- 兼容 OpenAI API 接口

## 其他推理框架

| 框架 | 维护方 | 特点 |
|------|--------|------|
| vLLM | UC Berkeley | PagedAttention, 社区活跃 |
| TGI | Hugging Face | 与 HF 生态集成 |
| TensorRT-LLM | NVIDIA | NVIDIA GPU 深度优化 |
| llama.cpp | Georgi Gerganov | CPU/边缘设备, GGUF 量化 |

## 实践要点

- 生产部署必用 continuous batching——静态 batching 的性能差距太大
- vLLM 是最安全的默认选择（社区活跃、功能完善、性能好）
- PagedAttention 的内存效率允许更大 batch size → 更低单位成本
- 监控 GPU utilization 和 KV Cache utilization 是运维关键指标

> 来源：resources/anyscale/20260404-untitled.md
> 来源：resources/vllm/20260404-vllm.md
> 来源：resources/wan-et-al/20260404-240414294-a-survey-on-efficient-inference-for-larg.md

→ [GPU Architecture Fundamentals](gpu-architecture.md)
→ [LLM Inference Cost](llm-inference-cost.md)
→ [KV Caching](../ml-fundamentals/kv-caching.md)
