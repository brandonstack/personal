# 工作流模式

Claude Code 社区发展出的高效工作流模式——从规划驱动到 vibe coding，从单会话到多会话并行。

## Plan-First 工作流

核心哲学：**规划 2 小时，执行 10 分钟，审查 1 小时**。

典型流程：
1. `/ce:plan` 或手动描述需求 → Claude 生成 plan 文件
2. 人审阅 plan，修改后确认
3. `/ce:work` 按 plan 执行
4. 审查结果，必要时迭代

实战数据（社区用户 30 天统计）：
- 70 个 plan 文件
- 263 个 git commits
- 大量时间花在规划和审查，执行是最快的部分

**Plan 文件的价值不止于执行**：plan 本身是知识产物——记录了设计决策、被否定的方案、约束条件。这与 Compound Engineering 的知识积累理念一致。

## Vibe Coding 两阶段法

阶段一：**全自动模式**（适合 greenfield 项目初期）
- 使用 Superpowers 等插件
- 给高层目标，让 Agent 自由发挥
- 快速生成原型
- 容忍不完美，频繁 git commit

阶段二：**半自动迭代模式**（项目成熟后）
- Plan → Execute → Review 循环
- 更细粒度的指令
- 人在 loop 中做架构决策
- 用最小约束 prompt——过度约束反而降低产出质量

**切换信号**：当全自动模式开始产出需要大量修改的代码时，切到半自动。

## 多会话并行

利用 git worktree 实现真正的并行开发：

```bash
# 开 4-6 个并行 session
git worktree add ../feature-a feature-a
git worktree add ../feature-b feature-b
# 每个 worktree 跑一个 Claude Code session
claude -w ../feature-a
```

关键约束：
- 每个 session 操作独立的文件集合
- 通过 worktree 隔离避免冲突
- 人的角色是"调度器"——分配任务到不同 session，审查合并结果

## 移动端与远程

- **`/remote-control`**：生成 URL，手机远程操控会话。代码仍在本地跑。通勤时审查代码
- **`--teleport`**：将 session 在设备间迁移
- **语音输入**：口述需求比打字更快，尤其是描述复杂意图时

## 实用技巧

| 技巧 | 效果 |
|------|------|
| 频繁 git commit | 安全网——可随时 revert Agent 的修改 |
| 卡住时换模型 | 不同模型对同一问题有不同解法 |
| `/btw` 插入提问 | 不污染对话历史，几乎零 token 开销 |
| `--bare` 最小启动 | 跳过 CLAUDE.md 加载，适合快速一次性任务 |
| `--add-dir` 多目录 | 让 Agent 同时看到多个相关项目 |
| 自动保存 + 热重载 | Zed 等编辑器配合，Agent 改代码后立即看到效果 |

→ [workflow-commands.md](workflow-commands.md) — 具体命令用法
→ [context-engineering.md](context-engineering.md) — 多会话的 context 管理策略
→ [plugins-ecosystem.md](plugins-ecosystem.md) — Superpowers / CE 等插件的工作流

> 来源：resources/20260323-claude-code-hacks.md, resources/20260325-vibe-coding-workflow-tips.md, resources/clippings/20260330-boris-claude-code-tips.md, resources/clippings/Claude Code 高效使用指南...md
