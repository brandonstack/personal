---
source: "@mvanhorn (X/Twitter)"
url: "https://x.com/mvanhorn/status/2035857346602340637"
date: "2026-03-23"
tags: [claude-code, workflow, productivity, AI-tooling]
---

# Every Claude Code Hack I Know

核心理念：No IDE. Just plan.md files and voice. Talk, plan, build.

## 1. 先 Plan 再写代码

有想法就 `/ce:plan`，不是先想或先写代码。产品创意、GitHub issue、终端报错截图——全部 `/ce:plan`。

- `/ce:plan` 并行启动多个 research agent：分析 codebase、搜已有 solutions、研究外部最佳实践
- 输出结构化 `plan.md`：问题描述、方案、涉及文件、验收标准、代码 patterns
- `/ce:work` 执行 plan：拆 task、实现、跑测试、逐条 check off
- Context 丢了？新 session 指向 plan 即可续上

> 传统开发 80% coding / 20% planning，这套反转为 80% planning / 20% coding。

插件：[Compound Engineering](https://github.com/EveryInc/compound-engineering-plugin)（`/plugin marketplace add EveryInc/compound-engineering-plugin`）

作者统计：70 个 plan 文件，近 30 天 263 commits。规则：除非一行改动，否则先写 plan.md。

## 2. 语音输入

语音 → LLM 不需要完美转录，Claude Code 理解上下文能自动补足。

工具推荐：
- **Monologue**（[@usemonologue](https://x.com/@usemonologue)）— 语音直接输入到聚焦应用
- **WhisperFlow** — 也好用
- 作者买了鹅颈麦克风放办公室

## 3. 同时跑 4–6 个 Session

多个 Ghostty 窗口各跑一个 Claude Code session：一个写 plan、一个执行 plan、一个跑 research、一个修 bug。窗口间轮转，各自自主运行。

前提：必须开 bypass permissions（否则每个动作都要确认，无法多窗口）。

## 4. 三个关键设置

**a) Bypass permissions** — `~/.claude/settings.json`：

```json
{
  "permissions": {
    "allow": ["WebSearch","WebFetch","Bash","Read","Write","Edit","Glob","Grep","Task","TodoWrite"],
    "deny": [],
    "defaultMode": "bypassPermissions"
  },
  "skipDangerousModePermissionPrompt": true
}
```

**b) 完成提示音** — hooks 配置：

```json
{
  "hooks": {
    "Stop": [{
      "hooks": [{"type": "command", "command": "afplay /System/Library/Sounds/Blow.aiff"}]
    }]
  }
}
```

**c) Zed 自动保存**（500ms）— Claude 编辑文件 → Zed 即时显示；你在 Zed 改 → Claude 1 秒内看到。效果像 Google Docs 协作。

## 5. 先 Research 再 Plan

`/last30days` 搜索 Reddit、X、YouTube、TikTok、HN 等并行研究话题。

示例：比较 Vercel agent-browser vs Playwright → 78 Reddit 帖、76 X 帖、22 YouTube 视频、15 HN 帖 → agent-browser 省 82–93% context tokens。研究结果直接输入 `/ce:plan`。

工具：[last30days-skill](https://github.com/mvanhorn/last30days-skill)（4.5K stars，开源）

## 6. 会议 → Plan

用 Granola 录会议 → 全文转录粘贴到 Claude Code → `/ce:plan` 生成产品提案。Claude Code 交叉引用 codebase + 之前的战略 plan 文件，输出带目标、用户故事、技术方案、里程碑的完整提案。

Granola 现已支持 MCP，可直接在 Claude Code 内使用。

## 7. Plan 不只写代码

战略文档、产品 spec、竞争分析、文章都用同一工作流：voice → Claude Code → markdown，迭代修改即时生效。Claude Code 有全部历史 plan 上下文，每个新 plan 都比上一个更好。

## 8. Mac Mini 远程 Claude Code

- **Telegram 集成**：手机发消息给 Mac Mini 上的 Claude Code，回来时 plan 已写好
- **tmux + 飞机**：先 tmux 到 Mac Mini，飞机 WiFi 断了也不影响 session，重连即续

## 开源贡献（均先写 plan.md）

Python（defaultdict repr）、OpenCV（HoughCircles）、Vercel Agent Browser、Zed、Paperclip、Compound Engineering 等。

## Token 用尽的对策

$200/月 Claude Max 不够 4–6 并行 Opus session。解法：加 $200/月 Codex 计划，用 `/ce:work --codex` 把实现委托给 Codex credits。Claude 做 planning，Codex 做 heavy implementation。

## 工具链总结

| 工具 | 用途 |
|------|------|
| [Compound Engineering](https://github.com/EveryInc/compound-engineering-plugin) | Plan + Work 插件 |
| [last30days](https://github.com/mvanhorn/last30days-skill) | 并行多平台 research |
| [Monologue](https://x.com/@usemonologue) | 语音输入 |
| [Granola](https://granola.ai/) | 会议录制 + MCP |
| [Ghostty](https://ghostty.org/) | 终端 |
| [Zed](https://zed.dev/) | 编辑器 |
