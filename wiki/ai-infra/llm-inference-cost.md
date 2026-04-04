# LLM Inference Cost

LLM 推理的成本结构分析。理解 prompt processing 和 token generation 的成本差异，以及影响每 token 成本的关键因素。

## 两阶段成本模型

| 阶段 | 操作 | 瓶颈 | 每 1K tokens 成本（Llama-2-70B, 2×A100） |
|------|------|------|------|
| **Prefill** | 并行处理整个 prompt | Compute-bound | ~$0.00042 |
| **Decode** | 逐 token 生成 | Memory-bandwidth-bound | ~$0.066（batch=1）|

Token generation 比 prompt processing 贵 **~160 倍**（batch=1 时）。

## 为什么 Generation 这么贵？

### Compute-bound vs Memory-bound

**Prefill（Compute-bound）**：
- 所有 prompt tokens 并行计算 → 矩阵-矩阵乘法
- GPU 的数千核心被充分利用
- 瓶颈是计算速度（FLOPS）

**Decode（Memory-bound）**：
- 每步只生成 1 个 token → 矩阵-向量乘法
- 需要从 HBM 读取所有模型权重（70B × 2 bytes = 140 GB）
- GPU 核心大部分时间在等数据
- 瓶颈是内存带宽（GB/s）

### FLOPs 分析

```
Forward pass FLOPs ≈ 2 × P（P = 参数量）

Llama-2-70B:
- 每个 token 需要 ~140 GFLOP
- A100 FP16: 312 TFLOPS → 理论上 0.45ms/token
- 但实际受限于内存带宽：140GB / 2TB/s = 70ms（batch=1）
```

## 降低成本的方法

### 增大 Batch Size
- Batch 越大，多个请求共享一次权重读取
- 内存带宽成本被分摊
- batch=32 时，generation 成本降到约 $0.0039/1K tokens（比 batch=1 便宜 17 倍）
- 但受限于 KV Cache 内存：batch_size × seq_len × 320KB/token

### Grouped Query Attention (GQA)
- Llama-2-70B 使用 8 个 KV heads（vs 64 query heads）
- KV Cache 缩小到 1/8，允许更大 batch → 更低成本
- → [KV Caching](../ml-fundamentals/kv-caching.md)

### Quantization（量化）
- FP16 → INT8：内存减半，成本约减半
- FP16 → INT4：内存减 3/4，质量损失可控
- GPTQ, AWQ, BitsAndBytes 等方法

### Speculative Decoding（推测解码）
- 小模型快速生成多个候选 token
- 大模型并行验证
- 正确率高时（如 70-90%），显著加速

### Continuous Batching
- → [Continuous Batching](continuous-batching.md)
- 动态插入/移除请求，最大化 GPU 利用率

## 与商业 API 的对比

Cursor 的分析（2023 年数据）：
- Llama-70B on 2×A100 prompt processing 成本约 GPT-3.5 的 1/3
- 但 self-hosting 需要运维成本、硬件折旧、利用率管理
- 低流量场景 API 更划算，高流量场景 self-hosting 更划算

> 来源：resources/cursor/20260404-untitled.md

→ [GPU Architecture Fundamentals](gpu-architecture.md)
→ [Continuous Batching](continuous-batching.md)
→ [KV Caching](../ml-fundamentals/kv-caching.md)
