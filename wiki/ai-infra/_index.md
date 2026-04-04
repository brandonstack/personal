# AI Infra & Deployment

LLM 推理的硬件基础、成本模型和优化技术。从 GPU 架构到 continuous batching 到量化，理解"为什么 LLM 推理这么贵，以及怎么降低成本"。

## 文件

- [gpu-architecture.md](gpu-architecture.md) — GPU 设计哲学、SM/Warp/SIMT、Memory Hierarchy、H100/A100 参数
- [llm-inference-cost.md](llm-inference-cost.md) — Prefill vs Decode 成本差异（160×）、降成本方法
- [continuous-batching.md](continuous-batching.md) — 静态 vs 动态 batching、PagedAttention/vLLM（23× 吞吐提升）
- [quantization.md](quantization.md) — GPTQ/AWQ/BitsAndBytes 量化方法、精度与质量权衡

## 核心概念

- **Memory-bandwidth bound**：LLM decode 阶段的核心瓶颈——读数据比算数据慢
- **Continuous Batching**：iteration-level scheduling，请求动态进出
- **PagedAttention**：OS 虚拟内存思想管理 KV Cache，<4% 浪费
- **Quantization**：精度换速度/内存，INT8 几乎无损，INT4 可接受

## 跨主题连接

- → [ml-fundamentals/](../ml-fundamentals/) — KV Cache 和 decoder 架构是推理优化的对象
- → [ai-eval-safety/](../ai-eval-safety/) — 量化后需要 eval 验证质量
- → [ai-engineering/](../ai-engineering/) — infra 知识是 AI Systems Engineer 可信度的来源
