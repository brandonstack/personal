# AI 转型路线

## 定位

**AI Systems Engineer**：设计让 agent 可靠工作的系统——评估体系、架构约束、知识结构、反馈循环。

不是"会调 LLM API 的开发者"，是"能让 agent 在生产环境中可靠交付的系统设计者"。

**独特优势**：
- 度量工程 → AI 评估体系设计（evaluator 调优是 harness 最难的部分）
- 数据治理 → 记忆治理（多 agent 知识共享、可信验证）
- 后端系统设计 → harness 架构（分层、隔离、可观测、反馈循环）

## 技能：两层结构

### 底层——不贬值（30% 投入）

这些跨范式，不管下一个热点是什么都值钱：
- **系统设计**：已有 7 年底子，保持锐度
- **评估方法论**：从 Price Accuracy 延伸到 AI 评估（LLM-as-judge、Pass@k、generator-evaluator 分离）
- **知识结构化**：信息架构、agent 可读性（"给地图不给手册"）
- **批判性判断**：知道什么时候不该用 agent（Jeremy Howard 的警告：agent 放大坏模式）

### 表层——当前必会（70% 投入）

市场正在找的，用来求职和做项目：
- **Harness 设计**：generator-evaluator 分离、架构约束机械化执行、记忆治理
- **Agent 开发**：Claude Agent SDK、tool use、multi-agent 编排
- **工作流工具链**：Claude Code、MCP（外循环）vs CLI（内循环）
  - Claude Code 隐藏命令层：`/rewind`（会话版本控制）、`/loop`（定时任务编排）、`/branch`（对话分叉）让它从对话工具变成可编排的工作流运行时 → 详见 [claude-code-workflow-commands.md](claude-code-workflow-commands.md)
- **AI 工程基础**：embedding、context engineering、prompt caching

### 明确不做

- ML 数学（线性代数、反向传播）— ROI 太低
- 死磕某个框架 — 学概念不学库，框架半衰期太短
- 只读不做 — inbox 输入已经够了，需要输出

## 项目积累

**深化现有项目**：
- 这个 repo 本身就是小型 harness（CLAUDE.md + commands + memory + areas 规则），打磨成 showcase

**新项目方向**（对齐 harness engineering）：
- Multi-agent harness：设计 generator-evaluator 系统并调优评估标准
- 知识管理 agent：自动化 inbox → areas 的信息治理（记忆层实践）
- 对比实验：solo agent vs harness 同一任务，量化效果差异（发挥度量经验）

每个项目讲清 trade-off 和设计决策，不是 demo 级别。

## 持续输入

- inbox 习惯保持，每周扫描 AI 工程领域
- 关注信号：下一个范式转移的早期迹象（prompt→context→harness→???）
- 原则：每读完一篇问自己"这改变我的 70/30 分配吗？"

## 时间线

- **4-7月（在职期）**：70% 做项目 + 30% 基础，利用微软福利（服务器/token）
- **7-8月（自驾期）**：放松为主，碎片输入
- **9月起（求职期）**：集中求职，项目持续完善

## 求职策略

- **叙事**：AI Systems Engineer — 构建 + 评估双线能力
- **差异化**：多数候选人会调 API；我会设计评估体系、做对比实验量化效果、知道什么时候该手写什么时候该交给 agent
- **目标**：AI 应用公司、传统公司 AI 团队、AI infra 公司
