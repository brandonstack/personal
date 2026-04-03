# Claude Code 工作流命令

日常使用中值得掌握的隐藏/进阶命令，重点是会话控制和工作流编排。

## 会话控制

- `/rewind`（双击 Esc）：四模式回退——回退代码+对话 / 仅对话 / 仅代码 / 压缩上下文释放空间。核心价值：回退代码但保留对话，Claude 记得之前的尝试，可以直接换方向
- `/branch`（原 /fork）：分叉当前对话为新会话，原会话不受影响。与 rewind 的区别：rewind 是后悔药，branch 是平行宇宙
- `/btw`：任务执行中插入提问，不污染对话历史，几乎零 token

## 工作流编排

- `/loop`：定时重复执行任务（默认 10 min），结果留在上下文中供后续判断。3 天自动过期
- `/remote-control`（/rc）：生成 URL，手机远程操控会话，代码仍在本地跑

## 模型切换

- `/model opusplan`：规划阶段用 Opus，执行阶段用 Sonnet。菜单中不显示，需手动输入

## 工作流编排应用

`/loop` 和 `/branch` 让 Claude Code 从对话工具变成可编排的工作流运行时：
- URL 批量处理：维护 pending-urls.txt，用 `/loop` 每 5-10 分钟自动扫描并 fetch
- Branch 做任务隔离：context 确定时，每个 task 拆独立 branch 减少冷启动

> 来源：resources/20260226-claude-code-hidden-commands.md（原文）
> 来源：areas/career/claude-code-workflow-commands.md（迁移）

→ [workflow-patterns.md](workflow-patterns.md) — 更多工作流模式和技巧
→ [architecture-overview.md](architecture-overview.md) — 命令在整体架构中的位置
