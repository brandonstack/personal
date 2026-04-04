# AI Evaluation & Safety

LLM 评估方法论、对齐技术、生产化模式。从 eval 驱动开发到 Constitutional AI，从 LLM-as-Judge 到生产护栏。

## 文件

- [llm-evaluation-methods.md](llm-evaluation-methods.md) — 三层评估体系：断言测试 → LLM/人工评估 → A/B Testing
- [llm-as-judge.md](llm-as-judge.md) — 用 LLM 评估 LLM 输出，G-Eval 框架，优势与局限
- [constitutional-ai.md](constitutional-ai.md) — Anthropic 的 RLAIF 对齐方法：自我批评 → 修正 → AI 偏好训练
- [eval-driven-development.md](eval-driven-development.md) — EDD：先写 eval 再优化系统，Lucy/Rechat 案例
- [llm-production-patterns.md](llm-production-patterns.md) — Eugene Yan 7 大模式：Evals, RAG, Fine-tuning, Caching, Guardrails, Defensive UX, Feedback

## 核心概念

- **Eval Driven Development**：LLM 应用最高 ROI 的投入——先写 eval，再优化
- **LLM-as-Judge**：用 GPT-4 评估输出质量，性价比远超人工
- **Constitutional AI**：用"宪法"原则引导 AI 自我对齐，减少人工依赖
- **生产护栏**：结构化、语法、语义、安全四层 guardrails

## 跨主题连接

- → [rag-retrieval/](../rag-retrieval/) — RAG evaluation 是 eval 方法的重要应用场景
- → [ml-fundamentals/](../ml-fundamentals/) — RLHF/RLAIF 基于 fine-tuning 技术
- → [harness-engineering/](../harness-engineering/) — guardrails 和 defensive UX 是 harness 设计的一部分
- → [ai-engineering/](../ai-engineering/) — eval 能力是 AI Systems Engineer 的核心技能
