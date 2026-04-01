# PKM 架构 & 发散思考（2026-04-01 深夜讨论）

## 核心架构：纯文本即 Ground Truth

```
纯文本 (Git Repo) — 唯一数据源
  ├── Obsidian（浏览/编辑 UI）
  ├── Kirby/Agent（自动化/对话/处理）
  ├── 提醒服务（读 TODO → 推通知）
  ├── Dashboard（读状态 → 可视化）
  ├── RSS 视图（读 inbox → 阅读体验）
  └── 未来任何新工具（都只读写文本）
```

- 数据永远在纯文本，任何 UI/工具都是视图层
- 不锁定任何平台，换 UI 不丢数据
- Git 天然同步 + 版本控制
- LLM 天然适合读写纯文本

---

## Agent vs UI 分工

**Agent 适合做的（后台、异步、处理型）：**
- feed 自动摄入（定时拉、去重、写 inbox）
- digest 生成（总结、提问、关联发现）
- 对话沉淀（聊天中有价值的内容写回 repo）
- 搜索查找、文件操作、commit/push
- 主动推送（发现相关内容时通知）
- 定期 review（周/月回顾）

**UI 适合做的（浏览、选择、快速交互型）：**
- RSS 阅读（扫标题、快速筛选）
- 待办管理（勾选、排序）
- inbox 分拣（标记 digest/跳过）
- 习惯追踪可视化
- 项目看板

---

## Digest 流程增强方向

1. **思考问题** — digest 末尾加 2-3 个苏格拉底式问题，在 Obsidian 里异步回答
2. **关联发现** — digest 时自动扫 repo 找相关内容，写入 `## 相关`
3. **对话消化** — 跟 Kirby 聊天讨论就是消化过程，要点自动写回文件
4. **观点挑战** — Agent 主动反驳或追问，不只是总结

---

## 多媒体消化（探索方向）

**消化路径：** 文字（摄入存档）→ 音频（通勤听）→ 对话（深化）→ 文字（沉淀）

- **NotebookLM 播客** — 把文章生成双人讨论播客，可接 MCP
- **TTS 语音版** — Agent 把 digest 用语音发出来
- **语音对话** — 飞书语音消息讨论，比打字快
- **生图辅助** — 对话中用图片帮助理解

多媒体加速理解环节，最终沉淀还是回到纯文本。

---

## 突破 Chat 界面限制

### 硬件方向
1. **智能音箱/树莓派** — 自建语音助手，"Kirby 今天有什么安排"
2. **手表通知** — Apple Watch 推飞书通知（现在就能做）
3. **墨水屏** — 桌面小屏显示待办/习惯/inbox 状态
4. **车载语音** — 自驾中的语音交互
5. **AR 眼镜** — 未来方向

### 软件方向
1. **Obsidian Dashboard** — 手机打开就是个人仪表盘
2. **飞书卡片交互** — 推送可点击的卡片（比纯文字效率高）
3. **Telegram Mini App** — Chat + 轻量 UI 混合
4. **邮件 digest** — 每天一封邮件汇总

### Ambient（环境式）
- 不是你来找我，是信息已经准备好等你
- 打开 Obsidian → daily brief 已生成
- 到某个地点 → 自动提醒相关事项
- 周五 → 自动 weekly review

---

## Kirby 作为个人助手的能力扩展

### 生活管理
- 习惯追踪（跑步、喝水、睡眠）
- 财务记账（随手报，月底汇总）
- 健康日志（追踪趋势）

### 信息代理
- 收到链接 → 抓取、翻译、digest、存 inbox
- 调研任务 → 后台做功课，整理好发给你
- 邮件/日历管理

### 旅行模式
- 实时路线建议
- 订酒店、查加油站、看天气
- 旅行日志（发照片+几句话 → 自动写游记）

### 自我进化
- 修改自己的配置文件优化行为
- 写新 skill 给自己用
- 学习用户偏好记到 memory
- 发现重复操作自动脚本化

---

## 潜在开源项目方向

"基于纯文本的个人操作系统" — Plain Text Life OS

- 纯文本 + Git 为数据层
- Obsidian 为 UI 层
- LLM Agent 为自动化层
- 多种视图/工具可插拔接入
- 对 plain text productivity 社区有吸引力

---

## 同步问题 & Agent-Native 文件系统

### 核心矛盾

> 对 AI 最友好的格式（纯文本）≠ 对实时应用最友好的格式（数据库）

纯文本是 Agent-Native 的：任何 LLM 天然就能读写 markdown，不需要学 API、SDK、schema。
但纯文本不支持实时同步，这是做成产品的最大阻碍。

### 同步方案探讨

1. **Obsidian Git 插件** — 5分钟自动 pull/push（个人够用）
2. **Syncthing / iCloud** — 文件级 P2P 同步
3. **CRDTs (Automerge/Y.js)** — 多端同时编辑无冲突
4. **混合架构** — 实时层（SQLite/CRDT）+ 异步落盘到纯文本 Git

### 务实方案：分层架构

```
实时通道：飞书/语音（对话、提醒、快速交互）
    ↕ Agent 桥接
持久层：纯文本 Git（知识、项目、记录、状态）
    ↕ 5分钟同步
浏览层：Obsidian（阅读、编辑、仪表盘）
```

不需要让纯文本变实时——每一层做它擅长的事。

### 产品 Selling Point

"你的数据是纯文本，AI 直接读写，你用任何工具查看。简单、透明、不锁定。"

---

## App "卡比" — Kirby 的 UI 分身

两个开发路线：
1. **Obsidian 插件**（短期）— TypeScript，在 Obsidian 内加功能
2. **独立 App**（长期）— React Native / Flutter，读写同一个纯文本 repo

App 不拥有数据，只是纯文本的视图层。很好的简历项目。

建议：先用 Obsidian + 社区插件跑通，确认需求后再做独立 app。

### 最终决定（02:49）

**确定走 Obsidian 插件路线，不做独立 app。**

原因：
- iOS 独立 app 需要 $99/年 Apple Developer 账号 + 审核流程
- 网页方案在手机上体验不够好
- Obsidian 已在 App Store，插件直接本地加载，零发布成本

Kirby Plugin 可以做的功能：
- 今日 Dashboard（待办、inbox 数量、项目状态）
- 一键 digest（调 Agent API 或直接调 LLM）
- 习惯打卡面板
- 番茄钟
- inbox 浏览和分拣

做好了可以开源到 Obsidian 社区，"AI-powered personal OS plugin" 在社区有吸引力。

---

## Obsidian 社区插件调研（可直接用的现成插件）

### 📊 核心基础（必装）

| 插件 | 用途 |
|------|------|
| **Dataview** | 把笔记当数据库查询，做 dashboard、待办汇总、项目索引 |
| **Templater** | 动态模板（变量、日期、JS），自动生成 daily note 等 |
| **Tasks** | 跨文件追踪所有待办，支持截止日期、优先级、重复 |
| **Calendar** | 左边栏月历，点日期直接跳 daily note |
| **Periodic Notes** | 周/月/季/年 review 模板 |
| **Obsidian Git** | 自动 Git 同步，设 5 分钟间隔 |

### 📰 RSS / 信息摄入

| 插件 | 用途 |
|------|------|
| **RSS Dashboard** | 2025年新插件（Reddit 998 upvotes），在 Obsidian 里直接浏览 RSS，支持 YouTube、播客 |
| **ReadItLater** | 从浏览器保存文章到 vault，自动转 markdown |

### ⏱️ 专注 & 习惯

| 插件 | 用途 |
|------|------|
| **Pomodoro Timer** | 番茄钟，状态栏显示，完成后自动记录到 daily note |
| **Habit Tracker 21** | 习惯打卡，可视化连续天数 |
| **Tracker** | 把笔记中的数值数据生成图表（运动、体重、睡眠趋势） |

### 🎨 UI & 体验

| 插件 | 用途 |
|------|------|
| **Homepage** | 打开 Obsidian 自动显示指定首页（dashboard） |
| **Excalidraw** | 手绘图、思维导图，直接嵌入笔记 |
| **Linter** | 保存时自动格式化 markdown |
| **QuickAdd** | 一键捕捉想法，快速创建笔记到指定文件夹 |

### 与纯文本架构的结合方式

1. **Daily Dashboard**（Dataview + Homepage + Templater）— 打开 Obsidian 看到今日待办、inbox 数量、习惯完成率、项目进度
2. **RSS 阅读**（RSS Dashboard）— 直接在 Obsidian 浏览 feed，一键保存到 inbox/
3. **习惯追踪**（Habit Tracker + Tracker）— daily note 打勾，月底自动出趋势图
4. **番茄钟**（Pomodoro Timer）— 学习时用，记录自动写入笔记
5. **Git 同步**（Obsidian Git）— Agent 改文件 → push → Obsidian 5分钟内 pull

### 建议第一步

先装 Dataview + Calendar + Periodic Notes + Homepage + Obsidian Git，写一个 dashboard 模板放到 repo 里。

---

*记录于 2026-04-01 深夜发散讨论*
