# ML/DL Fundamentals

Transformer 架构、attention 机制、自回归生成等 LLM 核心基础。理解这些概念是深入 AI 工程所有其他领域的前提。

## 文件

- [transformer-architecture.md](transformer-architecture.md) — Transformer 架构总览：encoder-decoder、组件、演进方向
- [self-attention-mechanism.md](self-attention-mechanism.md) — Self-Attention 计算步骤、Multi-Head Attention、Masked Attention
- [decoder-only-transformers.md](decoder-only-transformers.md) — GPT 系列架构、自回归生成、Prefill vs Decode
- [kv-caching.md](kv-caching.md) — KV Cache 原理、内存消耗、Grouped Query Attention
- [seq2seq-attention.md](seq2seq-attention.md) — Seq2Seq + Attention 的历史演进，Transformer 的前身
- [fine-tuning-methods.md](fine-tuning-methods.md) — 微调方法族谱：LoRA、QLoRA、RLHF、Constitutional AI

## 核心概念

- **Transformer**：基于 self-attention 的序列建模架构，取代 RNN 成为 LLM 基础
- **Self-Attention**：让序列中每个位置直接关注所有其他位置，O(n²) 复杂度
- **KV Cache**：自回归推理的关键优化，缓存已计算的 Key/Value 避免重复计算
- **Decoder-only**：现代 LLM 的标准架构（GPT、Claude、LLaMA）

## 跨主题连接

- → [ai-infra/](../ai-infra/) — KV Cache 和 decode 阶段是推理优化的核心对象
- → [rag-retrieval/](../rag-retrieval/) — Embeddings 是 transformer encoder 的输出
- → [ai-eval-safety/](../ai-eval-safety/) — Constitutional AI 基于 fine-tuning + RLHF
- → [glossary/](../glossary/) — Transformer, Attention, KV Cache 等术语条目
