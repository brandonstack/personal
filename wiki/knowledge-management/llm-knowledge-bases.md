# LLM Knowledge Bases

用 LLM 编译和维护个人知识库。核心模式：raw 数据 → LLM compile → wiki → Q&A → 输出回流 → 健康检查。Karpathy 在 2026-04 提出，多位实践者（jumperz、omarsar0）独立验证并扩展。

## 核心架构

```
raw/（源文件）
  ↓ LLM compile
wiki/（.md 文件集合，概念化、索引化、互相链接）
  ↓ Q&A
输出（回答、可视化、slides）
  ↓ 回流
wiki/（知识增强）
  ↓ 健康检查
wiki/（去重、补缺、修正不一致）
```

关键特征：
- **LLM 写且维护 wiki 的全部数据**，人很少直接编辑
- Wiki 包含：源数据摘要、反向链接、概念分类、概念文章、互相链接
- LLM 自动维护 index 文件和简要摘要

## 复合循环

> The real insight is the loop... every query makes the wiki better. It compounds. Now that's a second brain building itself. — @jumperz

每次查询/探索的输出 "filed back" 到 wiki，使知识库持续增强。这不是线性积累，而是复合增长——查询本身产出新知识，新知识改善后续查询的质量。

## 为什么不需要 RAG

在 ~100 篇文章 / ~400K words 的规模下，LLM 通过自动维护的 index + 简要摘要就能准确找到相关内容。不需要向量存储。

> Agents that own their own knowledge layer do not need infinite context windows. They need good file organisation and the ability to read their own indexes. — @jumperz

更便宜、更可扩展、更可检查——比把所有东西塞进一个巨大 prompt 好得多。规模超几千条再考虑向量数据库。

## 工具链

- **摄入**：Obsidian Web Clipper 转 .md + 下载关联图片到本地
- **IDE**：Obsidian 作为前端（查看 raw、wiki、可视化）
- **输出**：Markdown、Marp slides、matplotlib 图片
- **搜索**：自建的简单搜索引擎（web UI + CLI 供 LLM 使用）
- **索引**：qmd CLI（omarsar0 使用，语义搜索 + 元数据）

## 变体：研究论文知识库

omarsar0 的实践扩展了 Karpathy 模式：
- 自动化论文筛选（trained Skill 筛选高信号论文）
- 交互式可视化（MCP tools + agent orchestrator 生成可交互 artifact）
- 核心发现："research 的质量取决于 research questions，research questions 的质量取决于 agents 能 access 的 insights"

## 与 Compound Engineering 的关系

LLM Knowledge Base 模式和 Claude Code 生态中的 Compound Engineering（CE）是同一思想在不同层面的实现：
- CE `/ce:compound`：从代码 session 中提取可复用知识 → docs/solutions/
- Karpathy 模式：从研究材料中编译知识 → wiki/
- 本 repo 的 `/compile`：从 inbox 中消化知识 → wiki/ + reports/

共同点：每次交互都让知识 compound，Agent 不只产出结果，还产出可复用知识。

→ [../agent-architecture/control-flow-patterns.md](../agent-architecture/control-flow-patterns.md) — Agent Loop 是知识编译的执行机制
→ [../harness-engineering/compound-engineering.md](../harness-engineering/compound-engineering.md) — Compound Engineering 的详细模式
→ [../claude-code/plugins-ecosystem.md](../claude-code/plugins-ecosystem.md) — CE 插件的三 Agent 知识提取架构

> 来源：resources/clippings/Thread by @karpathy.md
> 来源：resources/clippings/Thread by @jumperz.md
> 来源：resources/clippings/Thread by @omarsar0.md
