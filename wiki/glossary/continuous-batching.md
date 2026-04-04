# Continuous Batching

LLM 推理服务的动态批处理技术。在每个 decode 步骤后都可以插入新请求或移除已完成的请求，而非等一批全部完成。

## 解决什么问题

静态 batching 中，短请求被长请求拖慢，GPU 大量空转。Continuous batching（iteration-level scheduling）让请求动态进出，GPU 利用率最大化。

## 关键数字

vLLM（PagedAttention）实现的 continuous batching 可达到 23× 吞吐量提升（vs 静态 batching，OPT-13B on A100）。

→ 深度阅读：[ai-infra/continuous-batching](../ai-infra/continuous-batching.md)
