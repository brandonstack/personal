---
topic: "ML/DL Fundamentals"
status: "curating"
hours_budget: 25
target_wiki_dir: "ml-fundamentals"
---

# ML/DL Fundamentals

最大知识短板，所有 AI 领域的基础。目标不是成为 ML researcher，而是作为 AI Systems Engineer 能理解底层原理、做出合理的架构决策。

## 学习目标

- [ ] 理解 neural network 基本原理（forward/backward pass, gradient descent, loss function）
- [ ] 能画出 transformer 架构图，解释 self-attention 和 multi-head attention
- [ ] 理解 tokenization、embedding、positional encoding 的作用
- [ ] 能区分 pre-training / fine-tuning / RLHF / DPO 并解释适用场景
- [ ] 理解 LoRA / QLoRA 等参数高效微调方法
- [ ] 了解 scaling laws 和 emergent abilities 的基本概念

## Tier 1 — 必读

| # | 标题 | URL | Source | 说明 | Status |
|---|------|-----|--------|------|--------|
| 1 | The Illustrated Transformer | https://jalammar.github.io/illustrated-transformer/ | Jay Alammar | 最佳 Transformer 可视化讲解，必读经典 | ⬜ |
| 2 | The Illustrated GPT-2 | https://jalammar.github.io/illustrated-gpt2/ | Jay Alammar | 从 Transformer 到 GPT，可视化解读 | ⬜ |
| 3 | Visualizing Attention | https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/ | Jay Alammar | Attention 机制的直觉理解 | ⬜ |
| 4 | Neural Networks: Zero to Hero (intro) | https://karpathy.ai/zero-to-hero.html | Andrej Karpathy | Karpathy 经典课程主页，从零构建 neural net | ⬜ |
| 5 | Let's build GPT: from scratch | https://www.youtube.com/watch?v=kCc8FmEb1nY | Andrej Karpathy | 2h 手把手从零构建 GPT，必看 | ⬜ |
| 6 | What is a Transformer? | https://blogs.nvidia.com/blog/what-is-a-transformer-model/ | NVIDIA | 工程视角的 Transformer 概述 | ⬜ |
| 7 | Attention Is All You Need (论文) | https://arxiv.org/abs/1706.03762 | Vaswani et al. | 原始论文，至少读 abstract + architecture 图 | ⬜ |
| 8 | Hugging Face NLP Course — Transformers | https://huggingface.co/learn/nlp-course/chapter1 | Hugging Face | 实操向的 Transformer 入门课程 | ⬜ |

## Tier 2 — 推荐

| # | 标题 | URL | Source | 说明 | Status |
|---|------|-----|--------|------|--------|
| 1 | But what is a neural network? | https://www.youtube.com/watch?v=aircAruvnKk | 3Blue1Brown | 最佳入门动画，直觉理解 neural net | ⬜ |
| 2 | A Visual Guide to Quantization | https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization | Maarten Grootendorst | 量化技术可视化讲解 | ⬜ |
| 3 | LoRA: Low-Rank Adaptation | https://arxiv.org/abs/2106.09685 | Hu et al. | LoRA 原始论文，参数高效微调必读 | ⬜ |
| 4 | RLHF explained | https://huggingface.co/blog/rlhf | Hugging Face | RLHF 流程讲解 | ⬜ |
| 5 | The Scaling Hypothesis | https://gwern.net/scaling-hypothesis | Gwern | Scaling Laws 深度分析 | ⬜ |
| 6 | Intro to Large Language Models | https://www.youtube.com/watch?v=zjkBMFhNj_g | Andrej Karpathy | 1h LLM 概览，适合工程师 | ⬜ |

## Fetch Commands

```bash
# Tier 1
python3 .ingest/batch-fetch.py projects/ai-learning/topics/ml-fundamentals.md --tier 1

# 全部
python3 .ingest/batch-fetch.py projects/ai-learning/topics/ml-fundamentals.md
```

## Wiki Output

（compile 后填入）
