# 多 Agent 组织模式

当单 Agent 能力不够或任务可并行拆分时，需要多 Agent 协作。但"过早多 Agent"是反模式——先验证单 Agent 上限，再考虑拆分。

## 两种基本模式

| 模式 | 特点 | 适用场景 |
|------|------|----------|
| **指挥者（Conductor）** | 同步紧密互动，主 Agent 实时指挥子 Agent | 任务间强依赖，需要频繁协调 |
| **统筹者（Orchestrator）** | 异步委派，产出为 PR/分支等持久工件 | 任务可独立完成，结果可合并 |

## 组织方式

- 主 Agent 统筹 + 子 Agent 并行执行
- **通信**：JSONL inbox（append-only），崩溃可恢复
- **隔离**：Worktree 隔离（每个子 Agent 独立工作目录）
- **依赖管理**：任务图管理子任务间的先后关系

## 关键设计原则

1. **子 Agent 只回传摘要**——搜索/调试细节留自己上下文，减少主 Agent context 污染
2. **协作方式写成协议**——结构化消息格式，不依赖自然语言的模糊性
3. **幻觉会互相放大**——需要交叉验证打断错误链（一个 Agent 的输出不能直接被另一个 Agent 当作事实）
4. **子 Agent 最小系统提示**——不带 Skills/Memory，防权限外泄
5. **顺序：协议先定 → 隔离先做 → 再谈协作并行**

## 与编排器-工作者控制模式的关系

五种控制模式中的"编排器-工作者"是多 Agent 在单次任务内的体现：中央 LLM 动态分解任务、委派给工作者、综合结果。而本文讨论的多 Agent 模式更多是系统级的持久组织——跨 session、跨代码库、通过文件系统协作。

## 安全边界

> 安全边界先于功能。

- 白名单授权 → 工作空间路径隔离
- 审计日志 → Prompt Injection 防护（标注不可信内容边界）
- 敏感操作显式确认
- 关键路径用独立 LLM 验证

→ [control-flow-patterns.md](control-flow-patterns.md) — 五种控制模式（含编排器-工作者）
→ [../claude-code/plugins-ecosystem.md](../claude-code/plugins-ecosystem.md) — Superpowers 的 subagent-driven-dev 是多 Agent 的产品实现
→ [../harness-engineering/evaluator-generator.md](../harness-engineering/evaluator-generator.md) — 生产者-检查者分离也是一种多 Agent 模式

> 来源：resources/20260319-agent-architecture-engineering-practice.md
