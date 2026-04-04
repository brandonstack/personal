---
topic: "AI Infra & Deployment"
status: "curating"
hours_budget: 15
target_wiki_dir: "ai-infra"
---

# AI Infra & Deployment

系统工程师可信度的关键领域。理解 LLM 从训练到推理到生产部署的全链路，特别是推理优化、serving 架构、成本控制。

## 学习目标

- [ ] 理解 LLM inference 的基本流程（prefill vs decode, KV cache, batching）
- [ ] 了解主流 serving 框架（vLLM, TGI, TensorRT-LLM）的架构差异
- [ ] 理解 GPU 选型基础（A100 vs H100, memory bandwidth vs compute）
- [ ] 了解 quantization 在部署中的实际应用和 trade-off
- [ ] 理解 serverless vs dedicated inference 的选型
- [ ] 能估算一个 LLM 应用的推理成本

## Tier 1 — 必读

| # | 标题 | URL | Source | 说明 | Status |
|---|------|-----|--------|------|--------|
| 1 | A Survey on Efficient Inference for LLMs | https://arxiv.org/abs/2404.14294 | Wan et al. | LLM 推理优化综述，全景图 | ✅ |
| 2 | vLLM: Easy, Fast, and Cheap LLM Serving | https://docs.vllm.ai/en/latest/ | vLLM | 最流行的开源 LLM serving 框架 | ✅ |
| 3 | Full Stack Optimization of Transformer Inference | https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/ | NVIDIA | NVIDIA 官方推理优化技术总览 | ✅ |
| 4 | The Illustrated LLM Inference | https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-llm-inference | Maarten Grootendorst | LLM 推理过程可视化 | ✅ |
| 5 | GPU Architecture Fundamentals | https://blog.codingconfessions.com/p/gpu-computing | Coding Confessions | 工程师视角的 GPU 计算入门 | ✅ |
| 6 | LLM Inference Cost Analysis | https://www.cursor.com/blog/llama-inference | Cursor | 真实的 LLM 推理成本分析 | ✅ |
| 7 | Serving LLMs in Production | https://www.anyscale.com/blog/continuous-batching-llm-inference | Anyscale | Continuous batching 详解 | ✅ |

## Tier 2 — 推荐

| # | 标题 | URL | Source | 说明 | Status |
|---|------|-----|--------|------|--------|
| 1 | TensorRT-LLM Overview | https://nvidia.github.io/TensorRT-LLM/ | NVIDIA | NVIDIA 推理引擎文档 | ⬜ |
| 2 | GGML / llama.cpp | https://github.com/ggerganov/llama.cpp | ggerganov | 本地推理方案，理解量化部署 | ⬜ |
| 3 | The GPU Inference Landscape | https://www.latent.space/p/gpu-inference | Latent Space | GPU 推理生态全景分析 | ⬜ |
| 4 | Serverless LLM Inference | https://modal.com/blog/serverless-llm-inference | Modal | Serverless 推理架构和成本 | ⬜ |
| 5 | FlashAttention | https://arxiv.org/abs/2205.02136 | Dao et al. | 改变推理性能的关键论文 | ⬜ |

## Fetch Commands

```bash
python3 .ingest/batch-fetch.py projects/ai-learning/topics/ai-infra.md --tier 1
```

## Wiki Output

（compile 后填入）
