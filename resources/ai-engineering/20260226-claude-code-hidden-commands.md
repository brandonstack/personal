---
source: "Khazix0918 (Twitter)"
url: "https://x.com/Khazix0918/status/2034842244600275340"
date: "2026-02-26"
tags: [claude-code, tips, shortcuts]
status: "promoted"
promoted_to: "areas/career/claude-code-workflow-commands.md, areas/career/skills-and-growth.md, areas/career/ai-engineer-roadmap.md"
---

# Claude Code 隐藏命令速查

## 命令

### /btw（2026-03-11 新增）
在 Claude 执行任务时插入提问，**不污染对话历史**。回答完按空格/回车消除。几乎不费 token（复用提示缓存）。适合长会话中随时问问题。

### /rewind（双击 Esc）
撤销/回退，支持四种模式：
1. 回退代码和对话
2. 回退对话，保留代码
3. 回退代码，保留对话
4. 从该点压缩对话，释放上下文空间

适合做实验：让 Claude 试方案，不行则代码回退、对话留着，Claude 记得之前聊过什么可以直接换方向。

### /insights
生成 HTML 报告，分析过去一个月的 Claude Code 使用习惯：常用命令、重复操作模式、推荐自定义命令和 Skills。建议每月跑一次。

### /model opusplan（隐藏命令）
规划阶段自动用 Opus 4.6（plan 模式），执行阶段切回 Sonnet 4.6。对 $20 Pro 订阅用户特别有用——省 Opus 额度，规划用强模型，写代码用快模型。`/model` 菜单中不显示，需手动输入。

### /simplify
三合一代码审查 Skill——同时启动三个并行 Agent，分别审查代码复用、代码质量、运行效率。每次大功能更新后跑一遍，清除 AI 写的冗余代码。

### /branch（原 /fork）
把当前对话分叉出新会话，原会话不受影响。与 /rewind 的区别：/rewind 是回退（后悔药），/branch 是分叉（平行宇宙）。

### /loop
定时重复执行任务。如 `/loop 5m 检查部署状态`（默认 10 min）。结果留在对话上下文中，Claude 可基于结果做后续判断。任务 3 天后自动过期。

### /remote-control（/rc）
生成 URL，手机打开后可远程操控 Claude Code 会话。完全同步，代码仍在本地跑，手机只是遥控器。

### /export
当前对话导出为 Markdown 文件。适合保存架构讨论、方案推敲，或导出给其他工具（如 Codex）做交叉审查。

## 快捷键

| 快捷键 | 功能 |
|--------|------|
| `Ctrl+V` | 直接粘贴截图（Mac 也是 Ctrl+V，不是 Cmd+V） |
| `Ctrl+J` / `Option+Enter` | 输入框换行 |
| `Ctrl+R` | 搜索历史 prompt |
| `Ctrl+U` | 删除整行输入 |

changelog: [github.com/anthropics/claude-code/blob/main/CHANGELOG.md](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)

---
<!-- 以下为消化内容，由 /digest 生成 -->

## 骨架

Claude Code 内置了一批未在菜单显示的命令，掌握它们可以显著提升长会话效率、控制成本、并将 AI 编程工具变成可编排的工作流组件。

- `/btw`：在任务执行中插入问题而不污染对话历史，几乎零 token 消耗
- `/rewind`：四模式回退（代码+对话 / 仅对话 / 仅代码 / 压缩上下文），让实验有代价可控的后路
- `/model opusplan`：规划用 Opus，执行用 Sonnet，在 Pro 订阅内最大化能力/成本比
- `/branch`（原 /fork）：分叉对话而非回退，允许并行探索方案
- `/loop`：定时重复任务，结果留在上下文中供 Claude 做后续判断
- `/remote-control`：手机远程操控本地 Claude Code 会话

## 连接

→ [areas/career/ai-engineer-roadmap.md](areas/career/ai-engineer-roadmap.md) **延伸** — roadmap 里列了"工作流工具链：Claude Code"，但只到 MCP/CLI 层面；这篇补充了 Claude Code 内部命令层的可编排性，是同一层的更深细节

## 行动

- [ ] 逐个探索 `/rewind`、`/loop`、`/branch` 的具体 use case，每个命令做一次真实场景试用 → [areas/career/skills-and-growth.md](areas/career/skills-and-growth.md)
- [ ] 用 `/loop` 跑起一个真正有用的自动化：URL list 批量抓取（维护 `inbox/pending-urls.txt`，定时扫描并 fetch） → [projects/](projects/)
- [ ] 定期查看 Claude Code CHANGELOG 和社区推荐，了解最新功能（每月一次） → [areas/career/skills-and-growth.md](areas/career/skills-and-growth.md)

---
<!-- 以下为个人思考 -->

### Q1: /rewind 沉没成本

确实从来没用过 rewind。平时遇到错误就在错误方向上越走越远。正确的做法应该是：发了错误指令、改了不对的东西时，及时回退一步。

对 rewind 的理解：本质是对 context 做分割/裁剪，把对话当文本来操作。需要系统学一下它的四种模式分别适合什么场景。

### Q2: opusplan 成本权衡

目前不是瓶颈，成本不需要考虑。跳过。

### Q3: /loop 和 /branch 的工作流可能性

两个具体想法：
1. **URL 批量处理**：维护一个 URL list（或从 Obsidian 拷过来），用 `/loop` 每 5-10 分钟自动扫描并处理，省掉逐个手动触发
2. **Branch 做任务隔离**：如果 context 比较确定，每个 task 拆独立 branch，减少冷启动时间

### Q4: 主动探索 vs 等待文档

Never. 从来没有主动探索过，一直是被动等文档。这是一个需要改变的习惯。
