# Compound Engineering (CE)

跨 session 的知识积累机制。让 Agent 每次工作的产出不只是代码，还有下次能复用的知识。

## 解决什么问题

Agent session 是一次性的——这次 debug 了一个坑，下次碰到类似问题又要从头来。CE 在 session 结束时把有价值的经验写进结构化知识库（`docs/solutions/`），让所有未来的 session 都能查到。

## 一句话区别

Anthropic 的 progress file 是**备忘录**（上一班交接给下一班），CE 的知识库是**公司 wiki**（所有人随时能查）。一个线性，一个指数——这就是"Compound"的含义。

→ 深度阅读：[compound-engineering 深度分析](../harness-engineering/compound-engineering.md)
