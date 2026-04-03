# Claudesidian 案例研究

Noah Brier（Alephic）开发的 Claude Code + Obsidian 知识管理系统。把 Obsidian vault 变成 AI 的持久记忆和工作空间，让 Claude 从"隔离 session"升级为"有记忆的思考伙伴"。

## 要解决的问题

Claude Code 每次 session 从零开始——没有持久知识库、没有组织结构、session 间不共享上下文。知识工作者已有大量笔记和思考在 Obsidian 里，但 AI 读不到。

Claudesidian 的方案：PARA 方法论组织 vault，Claude Code 作为主交互界面，Obsidian 作为可视化前端，Git 做版本控制和跨设备同步。

## 核心架构

双模式交互：Thinking Mode（探索、提问、连接想法）vs Writing Mode（生成、结构化、交付内容）。先想再写，用苏格拉底对话抵抗 LLM "直接给答案"的倾向。

技能系统分两层：

| 维度 | Commands | Skills |
|------|----------|--------|
| 触发 | 用户显式 `/command` | 上下文自动匹配 |
| 加载 | 调用时完整加载 | 渐进式三级加载 |
| 用途 | 工作流操作 | 知识参考 |

Skill 的三级渐进加载：L0 元数据（description）→ L1 正文（SKILL.md）→ L2 引用文件（references/）。核心思想：**上下文窗口是公共资源，不该预加载所有信息，而是按需注入**。

## 关键设计模式

### 标记文件模式

用文件存在/不存在控制行为，比配置文件更简单。例：FIRST_RUN 文件存在 → 触发欢迎消息 → 完成后删除。状态持久化用文件系统本身。

### 上下文感知注入（Skill Discovery Hook）

监听用户每条消息（UserPromptSubmit），如果提到 "skill" 相关词汇，自动扫描 `.claude/skills/` 注入可用技能列表。不是预加载——是按需发现。这和 Claude Code 的 deferred tools 是同一思路的不同实现。

### 永不阻塞的 Hook 设计

所有 Hook 以 `|| true` 收尾——Hook 失败不应阻塞主流程。SessionStart Hook 做版本检查、环境初始化等，任一步骤失败静默跳过。

### 可中断恢复

长流程（如 upgrade）用 checklist 文件追踪进度：`[x]` 完成 / `[-]` 跳过 / `[ ]` 待做。中断后重启自动从上次位置继续。

### AI 辅助语义合并

升级时不做简单文件覆盖——时间戳备份 → 逐文件对比 → AI 辅助语义合并（理解用户自定义意图，而非逐行 diff）。用 `cat source > dest` 代替 `cp` 避免交互确认。

### LLM 自我验证

代码审查（pragmatic-review）完成后，LLM 自我验证——删除没有代码证据支撑的发现。承认"我可能幻觉了"的机制化。

### 毕业模式

模板项目完成初始化后断开上游 git remote。项目从"模板的实例"毕业为"独立项目"，不再被上游更新覆盖。

## 可借鉴的模式

**已采纳 / 高度一致的：**
- 渐进式加载（我们的 wiki 索引 → 文件就是 L0→L1）
- 上下文窗口作为稀缺资源管理
- Hook `|| true` 防御模式
- 概念原子化（Claudesidian 是 50-150 行笔记，我们的 wiki 也是）

**值得考虑采纳的：**
- **Skill Discovery 的按需注入**：当前 `/compile` 是显式调用。如果有 UserPromptSubmit hook，可以在用户提到"知识库"时自动注入 wiki 索引，减少手动操作
- **标记文件模式**：我们用 frontmatter status 字段追踪状态，Claudesidian 用文件存在/不存在。更轻量，适合布尔状态（已初始化/未初始化）
- **可中断恢复 checklist**：`/compile --all` 处理 30 篇文件时，中途失败需要从头重来。用 checklist 文件可实现断点续传
- **LLM 自我验证**：report 生成后加一步"删除无来源支撑的判断"，提高诚实度

**路线不同的：**
- Claudesidian 让 LLM 做"思考伙伴"（先问后答），我们让 LLM 做"知识库维护者"（先消化后报告）。两种定位服务不同需求，可以共存
- Claudesidian 用 MCP Server 集成 Gemini Vision 处理图片/视频。我们纯文本流水线，暂不需要

→ [llm-knowledge-bases.md](llm-knowledge-bases.md) — Karpathy 的 LLM 知识库模式，Claudesidian 是该思想的 Obsidian 实现
→ [../claude-code/skill-design-patterns.md](../claude-code/skill-design-patterns.md) — Skills vs Commands 与 Claudesidian 的双层系统同构
→ [../claude-code/context-management.md](../claude-code/context-management.md) — 渐进式加载、上下文经济学
→ [../agent-architecture/tool-design-evolution.md](../agent-architecture/tool-design-evolution.md) — Deferred tools 与 Skill Discovery 是同一思路

> 来源：resources/20260403-claudesidian-analysis.md
