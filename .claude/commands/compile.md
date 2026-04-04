---
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(mv:*), Bash(mkdir:*)
description: 批量消化 pending 文件 — LLM 全权更新 wiki 知识库并生成 report 供用户审阅
---

## Input

$ARGUMENTS

输入可以是：
- 具体文件路径（空格分隔多个）：`resources/pending/anthropic/20260328-harness-design.md resources/pending/openai/20260211-harness-engineering.md`
- glob 模式：`resources/pending/clippings/*.md`
- 主题关键词：`harness`（自动匹配相关 pending 文件）
- `--all`：处理所有未编译的 pending 文件（按主题自动分批）

## Your task

批量消化 pending 文件，更新 wiki 知识库，生成 report 供用户审阅。

Follow these steps in order:

### 1. 收集目标文件

根据输入类型：
- **文件路径**：直接使用
- **glob**：Glob 匹配
- **关键词**：Grep 搜索 resources/pending/ 下所有 .md 文件的标题、tags、正文
- **--all**：Glob `resources/pending/**/*.md`，按标题/tags 聚类分批

过滤规则：
- 跳过 `status: compiled` 的文件
- 跳过 `podcast/` 目录下的文件
- 如果有 `-zh.md` 版本，优先读中文版本

列出找到的文件，确认后继续。如果超过 10 个文件，建议分批处理。

### 2. 加载已有知识上下文

- 读 `wiki/_index.md`（全局索引）
- 读与本批主题相关的 `wiki/<topic>/_index.md`（判断哪些概念已存在）
- 读 `areas/*/README.md`（了解用户个人情况，以便给出针对性建议）

### 3. 逐篇消化 + 提取知识

读取每篇 pending 文件，提取：
- **概念**：可独立成文的知识点、框架、模式
- **实践**：具体做法、工具用法、workflow
- **观点**：作者的判断、立场、预测
- **数据**：具体数字、案例、对比

### 4. 更新 wiki

对于提取的每个知识点，决定：

**a) 追加到已有 wiki 文件**（概念已存在，新材料补充/验证/挑战）
- 在适当位置追加新内容
- 标注来源：`> 来源：resources/xxx/yyy.md`

**b) 创建新 wiki 文件**（全新概念）
- 一个文件 = 一个概念，50-150 行
- 包含：定义、关键要点、实践要点、来源
- 如果概念与其他 wiki 文件有关，添加链接：`→ [相关文件](../topic/file.md)`

**c) 创建新子目录**（3+ 相关文件形成新主题）
- 创建目录 + `_index.md`

**Wiki 文件格式要求：**
- 中文为主，技术术语保留英文
- 不要写成文章摘要（那是 report 的事），要写成**概念文档**——像 wiki 词条一样，跨来源综合
- 必须标注来源
- 跨主题引用用相对链接

### 5. 更新 wiki 索引

- 更新所有被修改/新增子目录的 `_index.md`（文件列表、核心概念、跨主题连接）
- 更新 `wiki/_index.md` 全局索引（目录表、文件数、最后更新时间）

### 6. 生成 report

写入 `wiki/reports/YYYYMMDD-<topic-slug>.md`：

```markdown
---
date: "YYYY-MM-DD"
sources:
  - resources/pending/xxx/yyy.md
  - resources/pending/xxx/zzz.md
wiki_updated:
  - wiki/topic/file.md
  - wiki/topic/new-file.md
---

# <Report 标题>

## 这批材料在说什么

<1-2 段概述，中文为主>

## 关键洞察

<跨文章的 pattern、矛盾、趋势。编号列表，每条 2-3 句>

## 与已有知识的关系

<新知识如何连接/挑战/延伸 wiki 中已有的内容。引用具体 wiki 文件路径>

## 对你的具体建议

<结合 areas/ 中的个人情况（时间线、项目计划、职业目标），给出 actionable 建议>

## Wiki 更新摘要

<本次更新/新建了哪些 wiki 文件，每个一行说明变更内容>

## 值得讨论的问题

<3-5 个开放问题，邀请用户对话。要求：>
<- 不能通过重读材料回答>
<- 需要用户结合自身情况判断>
<- 挑战性的，不是确认性的>
```

### 7. 标记并移动 pending 文件

为每个处理过的 pending 文件：

**a) 更新 frontmatter**
- 添加或修改 `status: "compiled"`
- 如果文件没有 `status` 字段，在 frontmatter 中添加
- 如果文件没有 frontmatter，添加最小 frontmatter：`status: "compiled"`

**b) 移到 resources/ 对应主题目录**
- 保持目录结构：`resources/pending/anthropic/xxx.md` → `resources/anthropic/xxx.md`
- 如果目标目录不存在，先 `mkdir -p`
- 同一来源的 `-zh.md` 翻译版本一起移动

**c) 更新 wiki 引用路径**
- 把本批 wiki 文件中的 `> 来源：resources/pending/xxx` 更新为 `> 来源：resources/xxx`
- 更新 report 中的 sources 路径（frontmatter + 正文）

### 8. 输出

告诉用户：
- Report 文件路径
- 在对话中直接显示 **关键洞察** 和 **值得讨论的问题** 两个部分
- 邀请用户审阅完整 report 并开始对话

```
📋 Report: wiki/reports/YYYYMMDD-<topic>.md
📚 Wiki 更新：X 个文件更新，Y 个新建

[显示关键洞察]

[显示值得讨论的问题]

请审阅完整 report，然后我们可以讨论任何你感兴趣的点。对话中产生的有价值内容会回流到 wiki 或 areas。
```
