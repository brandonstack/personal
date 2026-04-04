# GPU Architecture Fundamentals

理解 LLM 推理优化的硬件基础。GPU 为什么适合 LLM？瓶颈在哪？如何利用硬件特性优化？

## CPU vs GPU 设计哲学

| 维度 | CPU | GPU |
|------|-----|-----|
| 设计目标 | 低延迟（单任务快） | 高吞吐（并行任务多） |
| 核心数 | 8-64 个强核心 | 数千个弱核心 |
| 缓存 | 大缓存（减少延迟） | 小缓存（省面积给更多核心） |
| 控制逻辑 | 复杂（分支预测、乱序执行） | 简单（SIMT，一条指令多线程） |
| 适用场景 | 复杂逻辑、分支多 | 数据并行、矩阵运算 |

## GPU 关键概念

### Streaming Multiprocessor (SM)
- GPU 的基本计算单元
- H100: **132 个 SM**，每个 SM 有 64 个 CUDA cores = 8448 cores 总计
- A100: 108 个 SM

### Warp（线程束）
- **32 个线程**组成一个 warp
- 同一 warp 内所有线程执行同一条指令（SIMT）
- 分支（if-else）导致 warp divergence：部分线程空等 → 效率下降

### Memory Hierarchy

```
速度快 ←────────────────────────────→ 容量大
Registers > Shared Memory > L1 > L2 > Global Memory (HBM)
```

| 层级 | H100 规格 | 特点 |
|------|----------|------|
| Registers | 65,536 × 32bit/SM | 最快，线程私有 |
| Shared Memory | 228 KB/SM | SM 内线程共享，手动管理 |
| L1 Cache | 与 shared memory 共享 | 自动管理 |
| L2 Cache | 50 MB 全局共享 | |
| Global Memory (HBM) | **80 GB**, 3000 GB/s | 最慢，所有 SM 共享 |

### Occupancy（占用率）
- SM 上活跃 warp 数 / 最大 warp 数
- 高 occupancy = 更好地隐藏内存延迟（一个 warp 等内存时，切换到另一个 warp）
- 但不是越高越好——register 和 shared memory 是有限资源

## 为什么 LLM 推理受 Memory Bandwidth 限制

- Decode 阶段：每步只生成 1 个 token
- 需要从 HBM 读取所有模型权重 + 整个 KV Cache
- 计算量很小（一次矩阵-向量乘法），但数据读取量很大
- → **Memory-bandwidth bound**，不是 compute-bound
- 这就是为什么 H100 的 3000 GB/s 带宽比 8448 个核心更重要

## H100 vs A100 关键参数

| 参数 | A100 | H100 |
|------|------|------|
| FP32 TFLOPS | 19.5 | 67 |
| FP16 TFLOPS | 312 (Tensor Core) | 989 |
| HBM 容量 | 80 GB | 80 GB |
| HBM 带宽 | 2 TB/s | 3.35 TB/s |
| SMs | 108 | 132 |

## 与 LLM 推理优化的关系

理解 GPU 架构是理解以下优化技术的基础：
- → [Continuous Batching](continuous-batching.md)：更好地利用 GPU 计算资源
- → [LLM Inference Cost](llm-inference-cost.md)：compute-bound vs memory-bound 分析
- → [KV Caching](../ml-fundamentals/kv-caching.md)：KV Cache 占用 HBM

> 来源：resources/coding-confessions/20260404-untitled.md

→ [LLM Inference Cost](llm-inference-cost.md)
→ [Continuous Batching](continuous-batching.md)
