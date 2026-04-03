---
source: "GitHub heyitsnoah/claudesidian"
url: "https://github.com/heyitsnoah/claudesidian"
date: "2026-04-03"
tags: [knowledge-management, claude-code, obsidian, PARA, AI-workflow]
status: "compiled"
---

# Claudesidian 项目深度分析

> Claude Code + Obsidian 知识管理系统。Noah Brier（Alephic）开发，2000+ stars。

## 项目定位

解决的问题：知识工作者用 Claude Code 时，AI 在隔离环境中运行——没有持久知识库、没有组织结构、每次会话从零开始。Claudesidian 把 Obsidian vault 变成 AI 的持久记忆和工作空间。

核心哲学："AI amplifies thinking, not just writing"——把 Claude 定位为思考伙伴而非写作工具。

## 架构

PARA 方法论组织 vault（00_Inbox → 01_Projects → 02_Areas → 03_Resources → 04_Archive → 05_Attachments → 06_Metadata）。Claude Code 作为主交互界面，Obsidian 作为可视化前端。Git 做版本控制 + 跨设备同步。

双模式交互：Thinking Mode（探索、提问、连接）vs Writing Mode（生成、结构化、交付）。

## 关键设计模式

### 1. SessionStart Hook 做会话增强

- **FIRST_RUN 标记文件**：文件存在时触发欢迎消息，完成后删除。状态持久化用文件系统本身。
- **自动版本检查**：curl GitHub 对比 package.json 版本号，有更新时提示。
- **`|| true` 防御**：Hook 永不失败、永不阻塞主流程。

### 2. Skill Discovery Hook（上下文感知注入）

监听用户每条消息（UserPromptSubmit），如果提到 "skill" 相关词汇，自动扫描 `.claude/skills/` 注入可用技能列表。核心思想：上下文窗口是公共资源，不该预加载所有信息，而是按需注入。

### 3. Skills vs Commands 双层系统

| 维度 | Commands | Skills |
|------|----------|--------|
| 触发 | 用户显式 `/command` | 上下文自动触发 |
| 加载 | 调用时完整加载 | 渐进式（元数据→正文→引用文件） |
| 用途 | 工作流 | 知识参考 |

Skill 的三级渐进加载：L0 元数据（description）→ L1 正文（SKILL.md）→ L2 引用文件（references/）。

### 4. 核心命令

- **init-bootstrap**（~855行）：10步安装向导。跨平台 vault 发现（扫描常见路径）、征求许可后 research 用户公开工作做个性化、完成后断开上游 git remote（"毕业"模式）。
- **upgrade**（~640行）：智能升级。时间戳备份 → 逐文件对比 → AI 辅助语义合并 → 进度追踪（`.upgrade-checklist.md`，`[x]/[-]/[ ]`）→ 可中断恢复。用 `cat source > dest` 代替 `cp` 避免交互确认。
- **thinking-partner**：苏格拉底模式。规则：Ask before answering / Track insights / Resist solutioning / Connect ideas / Surface assumptions。
- **de-ai-ify**：精确到词级别的 AI 味清除。四类模式：过渡词（Moreover/Furthermore）、陈词滥调（Let's dive in）、模糊对冲（It's important to note）、企业黑话（leverage→use）。保留原文创建 -HUMAN 副本。
- **pragmatic-review**：YAGNI/KISS 为核心的代码审查。反模式命名（GenericButton/Catch-Log-Exit/Premature Abstraction）。关键：审查后 LLM 自我验证，删除无证据的发现。
- **add-frontmatter**：按笔记类型（meeting/daily/reference/project）生成不同 schema 的 YAML frontmatter。

### 5. MCP Server：Gemini Vision 集成

7 个工具：analyze_image / analyze_multiple / extract_text / compare_images / suggest_image_filename / analyze_video / analyze_document。亮点：`suggest_image_filename` 用 AI 看图片内容命名文件。

### 6. Helper Scripts

- **update-attachment-links.js**：附件移动后自动更新 vault 中所有 wikilink 引用（4 种链接模式）
- **transcript-extract.sh**：yt-dlp 只下载字幕不下载视频 → 转 .md
- **firecrawl-batch.sh**：批量网页抓取，CJK 文件名感知
- **vault-stats.sh**：各目录笔记数、最近活跃度

### 7. 模板系统

三种模板（Research Note / Daily Note / Project），每个都包含 Connections 区块——强制思考与 vault 中其他内容的关联。

### 8. GitHub Actions

Issue/PR 中 @claude 触发自动处理。白名单制工具权限。

## 设计哲学总结

1. "上下文窗口是公共资源"——任何注入的信息都在跟用户任务抢空间
2. 渐进式加载——元数据常驻，内容按需
3. 标记文件模式——文件存在/不存在控制行为，比配置文件更简单
4. 先问后答——LLM 天然倾向立即回答，需要刻意纠正
5. 可中断恢复——长流程用 checklist 文件追踪进度
6. 永不阻塞——Hook 以 `|| true` 收尾
7. "毕业"模式——模板项目完成后脱离上游
