---
source: "Thariq Shihipar (Twitter / Anthropic)"
url: "https://x.com/trq212/status/2033949937936085378"
date: "2026-03-18"
tags: [claude-code, skills, agents, developer-tools]
status: "compiled"
---

# Lessons from Building Claude Code: How We Use Skills

Anthropic 内部有数百个 skills 在使用中。以下是分类、写法和分发的经验总结。

关键认知：Skills 不只是 markdown 文件——而是**文件夹**，可包含脚本、资产、数据等。Claude 会自主发现和使用这些内容。

## 9 类 Skills

### 1. Library & API Reference
解释如何正确使用库/CLI/SDK，包含代码片段和 gotchas。
- `billing-lib` — 内部计费库的边界情况
- `frontend-design` — 让 Claude 更好地使用你的设计系统

### 2. Product Verification
描述如何测试/验证代码。通常配合 Playwright、tmux 等外部工具。**值得花一个工程师一周专门优化**。考虑让 Claude 录制测试视频、在每步做程序化断言。
- `signup-flow-driver` — headless browser 走完注册→邮件验证→onboarding
- `checkout-verifier` — Stripe 测试卡驱动结账，验证发票状态

### 3. Data Fetching & Analysis
连接数据和监控系统，含凭据、dashboard ID、常见查询工作流。
- `funnel-query` — 注册→激活→付费的事件关联
- `grafana` — datasource UID + 问题→dashboard 查找表

### 4. Business Process & Team Automation
自动化重复工作流，前次执行的日志文件有助于模型保持一致。
- `standup-post` — 聚合 ticket tracker + GitHub + Slack → 格式化 standup
- `weekly-recap` — merged PRs + closed tickets + deploys → 周报

### 5. Code Scaffolding & Templates
生成框架样板代码，特别适合包含自然语言需求的脚手架。
- `new-migration` — 迁移文件模板 + 常见陷阱
- `create-app` — 新应用预配 auth/logging/deploy

### 6. Code Quality & Review
强制执行代码质量，可在 hooks 或 GitHub Action 中自动运行。
- `adversarial-review` — 生成子 agent 做批评，迭代直到只剩 nitpick
- `testing-practices` — 测试写法和覆盖范围指导

### 7. CI/CD & Deployment
- `babysit-pr` — 监控 PR → 重试 flaky CI → 解决合并冲突 → 自动 merge
- `deploy-<service>` — 构建→冒烟测试→灰度流量→回滚

### 8. Runbooks
接收症状（Slack 线程、告警、错误签名），走调查流程，产出结构化报告。
- `oncall-runner` — 拉取告警→检查常见原因→格式化结论
- `log-correlator` — 根据 request ID 拉取所有相关系统日志

### 9. Infrastructure Operations
日常维护和运维，含对破坏性操作的 guardrails。
- `<resource>-orphans` — 发现孤立资源→Slack 通知→浸泡期→确认→清理
- `cost-investigation` — 存储/流量账单飙升的排查

## 写好 Skill 的技巧

**不要说显而易见的事** — Claude 已经知道很多编码知识。聚焦于把 Claude 推出默认思维模式的信息。如 `frontend-design` skill 专门纠正 Claude 的默认设计偏好（Inter 字体、紫色渐变）。

**建立 Gotchas 部分** — 技能中信号最高的内容。从 Claude 的常见失败点积累，持续更新。

**利用文件系统做渐进式披露** — 把详细 API 签名放 `references/api.md`，模板放 `assets/`，Claude 会在适当时候自己去读。

**避免过度约束** — 给 Claude 信息但留灵活性。Skill 会被大量复用，过于具体的指令会限制适应性。

**设计初始化流程** — 需要用户配置的 skill（如 Slack channel），用 `config.json` 存储设置信息，未配置时让 agent 询问用户。可用 `AskUserQuestion` 工具呈现多选问题。

**description 字段是给模型看的** — Claude 启动时扫描所有 skill 的 description 来决定匹配。写的是**触发条件**，不是摘要。

**记忆与数据存储** — 可在 skill 中存日志/JSON/SQLite。如 `standup-post` 保留历史日志让 Claude 知道自上次以来的变化。数据应存在 `${CLAUDE_PLUGIN_DATA}` 稳定目录，避免升级时丢失。

**存入脚本和库** — 给 Claude 可复用的脚本让它专注于组合和决策，而非重建样板。如数据分析 skill 包含获取事件数据的函数库。

**On Demand Hooks** — Skill 可包含仅在调用期间激活的 hooks：
- `/careful` — 阻止 `rm -rf`、`DROP TABLE`、force-push 等破坏性操作
- `/freeze` — 阻止对特定目录外的文件编辑

## 分发 Skills

两种方式：
1. **提交到 repo**（`.claude/skills/`）— 适合小团队/少量 repo，但每个 skill 都会增加模型上下文
2. **插件市场** — 适合规模化，用户自选安装

市场管理：不设中心化审批团队，skill 先上传到 sandbox 目录让人试用，有牵引力后再 PR 进市场。注意防止劣质/冗余 skill 泛滥。

**组合 Skills**：skill 间可互相引用（按名称），模型会自动调用已安装的依赖 skill。

**衡量 Skills**：用 PreToolUse hook 记录 skill 使用日志，发现热门或触发不足的 skill。
