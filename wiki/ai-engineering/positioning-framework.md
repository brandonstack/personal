# AI Systems Engineer 定位框架

## 定位

**AI Systems Engineer**：设计让 agent 可靠工作的系统——评估体系、架构约束、知识结构、反馈循环。

不是"会调 LLM API 的开发者"，是"能让 agent 在生产环境中可靠交付的系统设计者"。

## 从传统工程到 AI 工程的能力迁移

- 度量工程 → AI 评估体系设计（evaluator 调优是 harness 最难的部分）
- 数据治理 → 记忆治理（多 agent 知识共享、可信验证）
- 后端系统设计 → harness 架构（分层、隔离、可观测、反馈循环）

## 技能投资的两层模型

### 底层——不贬值（30% 投入）

跨范式，不管下一个热点是什么都值钱：
- **系统设计**：分层、隔离、可观测性
- **评估方法论**：LLM-as-judge、Pass@k、generator-evaluator 分离
- **知识结构化**：信息架构、agent 可读性（"给地图不给手册"）
- **批判性判断**：知道什么时候不该用 agent

### 表层——当前必会（70% 投入）

市场正在找的，快速贬值但求职必要：
- **Harness 设计**：generator-evaluator 分离、架构约束机械化执行、记忆治理 → [harness-engineering/](../harness-engineering/)
- **Agent 开发**：Claude Agent SDK、tool use、multi-agent 编排 → [agent-architecture/](../agent-architecture/)
- **工作流工具链**：Claude Code、MCP（外循环）vs CLI（内循环）→ [claude-code/](../claude-code/)
- **AI 工程基础**：embedding、context engineering、prompt caching

### 明确不做

- ML 数学（线性代数、反向传播）— ROI 太低
- 死磕某个框架 — 学概念不学库，框架半衰期太短
- 只读不做 — 需要输出

## 差异化叙事

多数候选人会调 API；AI Systems Engineer 会设计评估体系、做对比实验量化效果、知道什么时候该手写什么时候该交给 agent。

> 来源：areas/career/ai-engineer-roadmap.md（迁移，提取通用框架部分）
