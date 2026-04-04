---
date: "2026-04-04"
sources:
  - resources/jay-alammar/20260404-the-illustrated-transformer-jay-alammar-visualizin.md
  - resources/jay-alammar/20260404-the-illustrated-gpt-2-visualizing-transformer-lang.md
  - resources/jay-alammar/20260404-visualizing-a-neural-machine-translation-model-mec.md
  - resources/andrej-karpathy/20260404-neural-networks-zero-to-hero.md
  - resources/nvidia/20260404-untitled.md
  - resources/vaswani-et-al/20260404-170603762-attention-is-all-you-need.md
  - resources/hugging-face/20260404-untitled.md
wiki_updated:
  - wiki/ml-fundamentals/transformer-architecture.md (新建)
  - wiki/ml-fundamentals/self-attention-mechanism.md (新建)
  - wiki/ml-fundamentals/decoder-only-transformers.md (新建)
  - wiki/ml-fundamentals/kv-caching.md (新建)
  - wiki/ml-fundamentals/seq2seq-attention.md (新建)
  - wiki/ml-fundamentals/fine-tuning-methods.md (新建)
  - wiki/ml-fundamentals/_index.md (新建)
  - wiki/glossary/transformer.md (新建)
  - wiki/glossary/kv-cache.md (新建)
---

# ML/DL Fundamentals — Knowledge Sprint 消化报告

## 这批材料在说什么

这批 8 篇材料覆盖了从 seq2seq 到 Transformer 到 GPT-2 的架构演进线。核心是 Jay Alammar 的三篇可视化博文（信息密度极高），辅以 Karpathy 课程目录、NVIDIA 概述、Vaswani 原论文摘要和 HuggingFace NLP Course 入口。其中 Karpathy 的 YouTube 视频和 NVIDIA/HuggingFace 内容较浅（课程入口和概述），但 Jay Alammar 的 Transformer 和 GPT-2 两篇堪称最佳入门参考。

实际有效内容来自 3 篇（Jay Alammar ×3），其余为摘要/目录/CAPTCHA blocked。

## 关键洞察

1. **Self-Attention 的核心创新不是 attention 本身，而是"自"**：Bahdanau 2014 就有了 attention（decoder→encoder），但 Transformer 的 self-attention 让每个位置关注自身序列内所有位置。这消除了 RNN 的递归依赖，实现 O(1) 连接（vs O(n)），才是并行化的关键。

2. **Multi-Head Attention 是一种冗余设计策略**：8 个 head 各 64 维 vs 1 个 head 512 维——参数量一样，但多个 head 可以分别学习不同类型的关系（语法、语义、位置）。这种"用结构约束换多样性"的思路在 AI 工程中反复出现（如 MoE 的多专家）。

3. **Prefill vs Decode 的成本差异是理解 LLM 经济学的钥匙**：GPT-2 文章揭示了这个关键 insight——prefill（并行矩阵乘法，compute-bound）和 decode（逐 token，memory-bound）完全不同。这直接解释了为什么 API 定价分 input/output tokens，为什么 batch size 影响推理成本。

4. **Seq2Seq → Transformer 不是渐进改良而是范式跳跃**：Seq2Seq attention 仍依赖 RNN 的顺序处理（只是加了"回看"能力）。Transformer 直接去掉递归，把 attention 从"辅助机制"提升为"唯一机制"——这种架构勇气和本 wiki 记录的 Prompt→Context→Harness 范式跳跃有异曲同工之处。

5. **微调方法的演进反映了"少改动多收获"的工程哲学**：从全参数 fine-tuning 到 LoRA（<1% 参数）到 soft prompt tuning（<0.01%），每一代都在用更少的改动获得接近的效果。QLoRA 让单卡微调 65B 成为可能——这对个人项目实验很有意义。

## 与已有知识的关系

- **KV Cache 跨越了 ml-fundamentals 和 ai-infra**：ml-fundamentals 的 kv-caching.md 解释"是什么"，ai-infra 的 continuous-batching.md 和 llm-inference-cost.md 解释"为什么重要"和"怎么优化"。这种跨主题连接正是 wiki 概念原子化设计的价值。
- **Self-Attention 机制直接连接到 harness-engineering 中的 context 管理**：Transformer 的 O(n²) attention 复杂度就是为什么 wiki/claude-code 中讨论的"200K token 预算分配"如此重要——更长的上下文意味着更大的计算和内存开销。
- **Fine-tuning Methods 补全了 wiki/ai-eval-safety/constitutional-ai.md 的技术背景**：Constitutional AI 建立在 SFT + RLHF 之上，现在有了完整的方法族谱。

## 对你的具体建议

1. **Jay Alammar 的 Transformer 和 GPT-2 文章值得再读一遍**（带着 wiki 中的知识框架）。这两篇是你面试中"解释 Transformer 架构"的最佳备课材料——能画出 self-attention 流程图这个目标完全可以达成。

2. **Karpathy 视频系列建议选读而非全看**。你 4-7 月时间有限（~90h 基础输入），建议只看 "Let's build GPT from scratch"（建立 coding 直觉）和 "Tokenization"（理解 input 层）。不需要从零搭 neural network——你的目标是 AI Systems Engineer 不是 ML Researcher。

3. **KV Cache 理解是你最有价值的跨领域连接点**。作为后端工程师，你对内存管理和缓存策略有直觉——KV Cache 的 eviction、paging、内存碎片问题和传统后端的 Redis/Memcached 设计决策高度类似。面试中可以用这个桥接讲你的能力迁移。

## Wiki 更新摘要

- **wiki/ml-fundamentals/** — 新建 6 个概念文件 + _index.md，覆盖 Transformer → Self-Attention → Decoder-only → KV Cache → Seq2Seq → Fine-tuning 的完整知识链
- **wiki/glossary/transformer.md** — 新建 Transformer 术语条目
- **wiki/glossary/kv-cache.md** — 新建 KV Cache 术语条目

## 值得讨论的问题

1. **你面试时怎么定位 ML 基础的深度？** 目前 wiki 覆盖到了"能画 self-attention 流程图"和"能解释 KV Cache 内存开销"的水平。对 AI Systems Engineer 来说够了吗？还是需要深入到 training dynamics（loss landscape、gradient flow）？

2. **个人实验的优先级**：QLoRA 让单卡微调 65B 成为可能。考虑到你的 action-plan 中提到了利用微软福利（服务器/token），在项目 2（harness 项目）中加一个 fine-tuning 实验是否值得？还是纯用 prompting + RAG 更对齐你的定位？

3. **Jay Alammar 级别的可视化解释能力是面试加分项**。你在写博客计划中提到了"后端工程师视角的 Harness Engineering"——如果加一篇"后端工程师视角的 Transformer 架构"（用缓存/队列/内存管理的类比来解释），是否更能体现你的独特视角？
