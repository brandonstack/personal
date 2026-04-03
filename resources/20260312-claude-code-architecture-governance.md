---
source: "Twitter @HiTw93"
url: "https://x.com/HiTw93/status/2032091246588518683"
date: "2026-03-12"
tags: [claude-code, context-engineering, skills, hooks, prompt-caching]
status: "compiled"
---

# Claude Code：架构、治理与工程实践

半年深度使用 Claude Code 的踩坑经验。核心发现：卡住的地方几乎从来不是模型不够聪明，而是上下文错了、或者产出无法验证。

## 六层架构

把 Claude Code 拆成六层：上下文层、控制层（Skills/Hooks）、工具层（Tools/MCP）、Subagents、验证层、CLAUDE.md 契约。只强化一层系统就会失衡。

核心循环：收集上下文 → 采取行动 → 验证结果 → 完成/回到收集。

排查思路：结果不稳定→查上下文加载顺序；自动化失控→查控制层；长会话质量下降→上下文被中间产物污染，开新会话比调 prompt 有用。

## 概念边界

- **Tool/MCP**：给 Claude 新动作能力
- **Skill**：给它一套工作方法
- **Subagent**：隔离执行环境
- **Hook**：强制约束和审计
- **Plugin**：跨项目分发

## 上下文工程

200K 上下文的真实分配：

```
固定开销 ~15-20K：系统指令 ~2K + Skill 描述符 ~1-5K + MCP 工具定义 ~10-20K + LSP ~2-5K
半固定 ~5-10K：CLAUDE.md ~2-5K + Memory ~1-2K
动态可用 ~160-180K：对话历史 + 文件内容 + 工具调用结果
```

**MCP 是最大隐形杀手**：5 个 Server 光工具定义就占 25K tokens（12.5%）。

**上下文分层**：
- 始终常驻 → CLAUDE.md（项目契约/构建命令/禁止事项）
- 按路径加载 → rules（语言/目录/文件类型）
- 按需加载 → Skills（工作流/领域知识）
- 隔离加载 → Subagents（大量探索/并行研究）
- 不进上下文 → Hooks（确定性脚本/审计/阻断）

**最佳实践**：
- CLAUDE.md 保持短硬可执行（Anthropic 官方约 2.5K tokens）
- 大型参考文档拆到 Skills supporting files
- 用 `.claude/rules/` 做路径规则
- `/context` 观察消耗，任务切换 `/clear`，同任务新阶段 `/compact`
- **Compact Instructions 写进 CLAUDE.md**——压缩保留什么由你控制

**Tool Output 噪声**：cargo test 几千行输出全进上下文。RTK（github.com/rtk-ai/rtk）通过 Hook 自动过滤，只留 pass/fail。

**压缩陷阱**：默认按"可重新读取"判断，会丢掉架构决策和约束理由。解法：写 Compact Instructions + HANDOFF.md（让 Claude 写进度/尝试/死路/下一步，新会话读这个文件接着做）。

**Plan Mode**：探索和执行分阶段，按 Shift+Tab 进入。进阶：一个 Claude 写计划，另一个审计划。

## Skills 设计

不是模板库，是按需加载的工作流。描述符常驻上下文，完整内容触发时加载。

**好 Skill 标准**：描述写"何时该用我"而非"我是干什么的"；有完整步骤/输入/输出/停止条件；正文只放核心约束，大资料拆 supporting files；有副作用的设 `disable-model-invocation: true`。

**三种典型类型**：
1. **检查清单型**（质量门禁）：发布前逐项验证
2. **工作流型**（标准化操作）：配置迁移等高风险操作，内置回滚
3. **领域专家型**（决策框架）：运行时诊断，按固定路径收集证据

**描述符要短**（~9 tokens vs ~45 tokens），每个启用的 Skill 常驻消耗上下文。

**频率策略**：高频保持 auto-invoke；低频 disable-auto-invoke 手动触发；极低频移除 Skill 改为文档。

**反模式**：描述过短（任何工作都触发）、正文过长、一个 Skill 覆盖五件事、有副作用允许自动调用。

## 工具设计

给 agent 的工具重点不是功能完整，是让它更容易用对。

**原则**：名称按系统分层前缀（github_pr_*）、大响应支持 concise/detailed、错误响应教模型如何修正、合并高层任务工具。

**Claude Code 团队工具演进教训**：
- AskUserQuestion：加参数→约定格式→独立工具，独立工具最稳（要 Claude 停下来做的事就给专门工具）
- TodoWrite：模型弱时加的限制，模型变强后反成枷锁——定期检查限制是否还成立
- 搜索：RAG→Grep 工具（Claude 不喜欢用 RAG），附带发现"渐进式披露"模式

**不该加 Tool 的情况**：shell 可完成、只需静态知识、更适合 Skill 工作流、还没验证过能被模型稳定使用。

## Hooks

把不能交给 Claude 临场发挥的事收回确定性流程。

**适合**：阻断修改保护文件、Edit 后自动 lint、SessionStart 注入动态上下文、完成后通知。
**不适合**：复杂语义判断、长流程、多步推理。

注意限制输出长度（`| head -30`），避免 Hook 输出污染上下文。

**三层叠加**：CLAUDE.md 声明规则 + Skill 定义执行流程 + Hook 硬性校验阻断。少任何一层都有漏洞。

## Subagents

最大价值不是并行而是隔离。大量输出的任务（扫库/跑测试/审查）交给 Subagent，主线程只拿摘要。

内置三个：Explore（只读扫库，跑 Haiku）、Plan（规划调研）、General-purpose。

**约束**：限定工具集、选合适模型、设 maxTurns、需要动文件时 worktree 隔离。Ctrl+B 移长命令到后台。

**反模式**：子权限和主线程一样宽、输出格式不固定、子任务强依赖频繁共享状态。

## Prompt Caching

Claude Code 整个架构围绕 Prompt 缓存构建。高命中率省钱+速率限制更宽松。

**Prompt 顺序**：System Prompt（静态锁定）→ Tool Definitions（静态锁定）→ Chat History（动态）→ 当前输入。

**破坏缓存的陷阱**：系统 Prompt 放时间戳、打乱工具定义顺序、会话中途增删工具。动态信息用 `<system-reminder>` 放在用户消息里。

**会话中途不要切模型**：缓存是模型唯一的，切到 Haiku 要重建缓存反而更贵。需要切换时用 Subagent 交接。

**Compaction 实现**：fork 调用把完整历史喂给模型总结（命中缓存 1/10 价格），替换成 ~20K 摘要。

**Plan Mode 实现**：不切换工具集（会破坏缓存），而是 EnterPlanMode 作为工具调用。

**defer_loading**：MCP 工具先发轻量 stub（只有工具名），模型通过 ToolSearch 发现后才加载完整 schema，保持缓存前缀稳定。

## 验证闭环

"Claude 说完成了"没用，要能验证对不对、出问题能退回、过程能查。

**三层验证**：命令退出码/lint/test → 集成测试/截图对比/contract test → 生产日志/监控/人工审查。

> 如果你说不清楚"什么叫做完"，那大概率也不适合直接扔给 Claude。

## CLAUDE.md 写法

是协作契约，不是知识库。一开始可以什么都不写，发现重复纠正时再补。

**该放**：build/test/run 命令、目录结构与模块边界、代码风格约束、环境坑、NEVER 列表、Compact Instructions。

**不该放**：大段背景、完整 API 文档、空泛原则、Claude 读仓库可推断的信息、低频任务知识（放 Skills）。

**让 Claude 维护**：纠正错误后说 "Update your CLAUDE.md so you don't make that mistake again"，定期 review 过时条目。

## 工程化布局参考

```
Project/
├── CLAUDE.md                    # 全局契约
├── .claude/
│   ├── rules/                   # 路径/语言规则
│   ├── skills/                  # 工作流（按任务类型分目录）
│   ├── agents/                  # 自定义 Subagent
│   └── settings.json
└── docs/ai/                     # 架构细节/runbook
```

多项目：稳定基线放 `~/.claude/`，项目差异放项目级 `.claude/`。

## 配置健康检查

开源 Skill：`npx skills add tw93/claude-health`，跑 `/health` 一键检查配置状态。

## 三个阶段

1. 当 ChatBot 用
2. 学会工具和命令
3. 关注"怎么让 agent 在约束下自己跑起来"
