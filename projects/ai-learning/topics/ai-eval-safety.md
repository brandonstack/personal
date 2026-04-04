---
topic: "AI Evaluation & Safety"
status: "curating"
hours_budget: 15
target_wiki_dir: "ai-eval-safety"
---

# AI Evaluation & Safety

核心定位差异化能力。已有 evaluator-generator 基础，需要补全评估方法论体系：benchmark 设计、eval 框架、safety/alignment 基本概念、red-teaming 方法。

## 学习目标

- [ ] 理解 LLM 评估的核心挑战（non-deterministic, multi-dimensional, evolving）
- [ ] 能设计一个 eval suite：选指标、写 test cases、自动化运行
- [ ] 了解主流 eval 框架（Anthropic Evals, OpenAI Evals, LMSYS, Braintrust）
- [ ] 理解 AI safety 基本概念：alignment, RLHF 的 safety 角色, constitutional AI
- [ ] 了解 red-teaming 方法和 OWASP LLM Top 10
- [ ] 能把 eval 思维应用到自己的 harness 项目中

## Tier 1 — 必读

| # | 标题 | URL | Source | 说明 | Status |
|---|------|-----|--------|------|--------|
| 1 | A Practical Guide to LLM Evaluations | https://www.anthropic.com/research/evaluating-ai-systems | Anthropic | Anthropic 官方 eval 指南 | ⬜ |
| 2 | OpenAI Evals Framework | https://github.com/openai/evals | OpenAI | 开源 eval 框架，理解 eval 设计模式 | ⬜ |
| 3 | Chatbot Arena: Benchmarking LLMs | https://lmsys.org/blog/2023-05-03-arena/ | LMSYS | Elo-based LLM 评估方法论 | ⬜ |
| 4 | OWASP Top 10 for LLM Applications | https://owasp.org/www-project-top-10-for-large-language-model-applications/ | OWASP | LLM 安全威胁 Top 10 | ⬜ |
| 5 | Constitutional AI | https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback | Anthropic | Constitutional AI 论文解读 | ⬜ |
| 6 | How to Evaluate LLM Applications | https://hamel.dev/blog/posts/evals/ | Hamel Husain | 实操向的 eval 方法论（工程师视角） | ⬜ |
| 7 | Braintrust: The Guide to LLM Evals | https://www.braintrust.dev/docs/guides/evals | Braintrust | Eval 工具实操教程 | ⬜ |

## Tier 2 — 推荐

| # | 标题 | URL | Source | 说明 | Status |
|---|------|-----|--------|------|--------|
| 1 | Anthropic's Responsible Scaling Policy | https://www.anthropic.com/news/anthropics-responsible-scaling-policy | Anthropic | Safety 与 scaling 的平衡框架 | ⬜ |
| 2 | Red-Teaming Language Models | https://arxiv.org/abs/2202.03286 | Ganguli et al. | Red-teaming 方法论论文 | ⬜ |
| 3 | Holistic Evaluation of Language Models (HELM) | https://crfm.stanford.edu/helm/ | Stanford | 多维度 LLM 评估框架 | ⬜ |
| 4 | LLM Evaluation Metrics Explained | https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation | Confident AI | 评估指标全览 | ⬜ |
| 5 | Model Card Best Practices | https://huggingface.co/docs/hub/model-cards | Hugging Face | 模型透明度和文档标准 | ⬜ |

## Fetch Commands

```bash
python3 .ingest/batch-fetch.py projects/ai-learning/topics/ai-eval-safety.md --tier 1
```

## Wiki Output

（compile 后填入）
