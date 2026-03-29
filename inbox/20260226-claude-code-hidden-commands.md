---
source: "Khazix0918 (Twitter)"
url: "https://x.com/Khazix0918/status/2034842244600275340"
date: "2026-02-26"
tags: [claude-code, tips, shortcuts]
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
