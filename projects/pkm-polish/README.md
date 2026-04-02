# 🔧 PKM 完善（6月前）

> 启动日期: 2026-04-01
> 目标: 在现有 personal repo 基础上修补完善，让它真正自动化运转起来

## 架构

**纯文本 + Git + Obsidian(UI) + Agent(自动化)**

- **存储层**: Markdown 文件 + Git（不变）
- **浏览层**: Obsidian（手机+电脑都能用）
- **处理层**: Kirby/Agent（自动摄入、digest、连接、推送）
- **交互层**: 飞书对话（讨论、语音、生图）

## 完成标准

- [ ] Obsidian 配置好，手机电脑同步跑通
- [ ] RSS/Feed 自动摄入运行
- [ ] digest 流程优化完成（含思考问题 + 关联发现）
- [ ] 整套流程能无摩擦地日常使用

---

## 一、RSS / Feed

- [ ] 源列表整理更新（`scripts/ingest/sources.yaml`）
- [ ] feed 自动摄入定时运行（cron / heartbeat）
- [ ] Obsidian 里浏览 inbox 的体验优化

## 二、Digest 流程增强

- [ ] digest 末尾加 `## 思考问题`（2-3个苏格拉底式问题）
- [ ] digest 时自动扫 repo 找相关内容（关联发现），写入 `## 相关` 区域
- [ ] 回顾 Inquiry V3/V4/V5 中好的做法，迁移到 digest command
- [ ] 优化 digest 输出质量

## 三、多媒体消化（探索）

- [ ] **NotebookLM 主题播客** — 按 tag 聚合 inbox 同主题文章，上传 NotebookLM 生成播客，离线听建立整体理解，听完再回来 `/digest`
  - [ ] 手动试一轮验证流程：挑一个主题（如 harness-engineering），打包上传，生成播客，听后 digest，评估是否真的加速
  - [ ] 写脚本按 tag 聚合导出 markdown 文件包，方便批量上传
  - [ ] 探索 NotebookLM API / MCP 自动化可能性
- [ ] TTS 语音版 — 用 Kirby 语音发送 digest 摘要
- [ ] 语音对话消化 — 飞书语音讨论，要点自动写回文件
- [ ] 生图辅助 — 对话中用图片辅助理解

## 四、智能推送（Agent 主动）

- [ ] 主动推送 — inbox 有文章跟你最近关注的主题相关时通知你
- [ ] 项目 deadline 提醒
- [ ] 主题聚合 — 连续摄入同一主题时，自动归纳共同点

## 五、时间维度

- [ ] 每周自动生成 weekly review（本周消化了什么、想了什么）
- [ ] 每月 monthly review（关注主题变化趋势）

## 六、对话沉淀

- [ ] 飞书里有价值的讨论自动提取要点，写回 repo 对应文件
- [ ] 观点挑战 — 你写了想法后，Agent 主动反驳或追问

## 七、习惯养成

- [ ] 定一个最小可行节奏（比如每周 digest 2-3 篇）
- [ ] 跑两周看看摩擦点在哪里，再调整

---

*Created: 2026-04-01*
