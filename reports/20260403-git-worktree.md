---
date: "2026-04-03"
sources:
  - resources/clippings/git worktree 实战指南：使用场景、常用命令、解决的问题与日常工作流.md
wiki_updated:
  - wiki/dev-tools/git-worktree.md (新建)
  - wiki/dev-tools/_index.md (新建)
  - wiki/_index.md (更新)
---

# Git Worktree 实战知识消化

## 这批材料在说什么

一篇来自知乎的 git worktree 全面指南，从原理到命令到日常工作流，覆盖了创建、清理、保护、迁移全生命周期。文章重点对比了 worktree 与传统方案（切分支+stash、多仓 clone）的差异，给出了明确的场景适用建议和常见坑的排查方法。

内容实用、结构清晰，属于"参考手册型"文章。核心知识点已提取到 wiki 概念文件。

## 关键洞察

1. **worktree 的核心价值不是"多一个目录"，是消除上下文切换的认知开销**。频繁 stash/unstash 不只是操作繁琐，更危险的是破坏工作心流——而 worktree 让每个任务有自己的物理空间。

2. **同一分支只能在一个 worktree 检出是硬约束，不是 bug**。这个设计防止了"两个地方同时修改同一分支"的数据一致性问题。绕过方式是 `--detach` 或建新分支名——理解这个约束才能用好 worktree。

3. **`.wt/` 目录约定是关键工程决策**。把所有 worktree 集中在仓库旁的 `.wt/` 下，比散落在文件系统各处更容易管理和清理。这是一个小但重要的约定。

4. **worktree 与 Claude Code 多会话并行是天然搭配**。你的 wiki 中已记录了 Claude Code 用 worktree 做多 session 并行的模式——这篇文章补全了 worktree 本身的知识基础，让那个模式更可操作。

## 与已有知识的关系

- **补全了 `wiki/claude-code/workflow-patterns.md` 的依赖知识**：该文件"多会话并行"部分引用了 `git worktree add` 命令，但没有解释 worktree 本身。新建的 `wiki/dev-tools/git-worktree.md` 填补了这个空白，两者互相链接。
- **开辟了 `dev-tools/` 主题**：wiki 之前聚焦于 AI/Agent/Harness 领域，缺少基础开发工具的知识积累。git worktree 是第一个条目，后续 git 高级用法、shell 技巧等可以归入这个目录。

## 对你的具体建议

1. **在你的个人项目中实践 `.wt/` 约定**：你的 `personal/` mono repo 本身就可以用 worktree——比如 compile 时一个 worktree，同时在另一个 worktree 做 areas 整理。尤其结合你已有的 Claude Code 多会话工作流。

2. **结合 4-7 月 action plan 的项目并行**：`areas/career/action-plan-apr-jul.md` 提到你有多个并行项目。如果这些项目在同一个 repo 里的不同分支，worktree 可以显著降低切换成本。

3. **Claude Code 的 `--add-dir` 和 worktree 可以组合**：一个 session 操作 worktree A，但通过 `--add-dir` 同时看到 worktree B 的文件——适合需要跨分支参考的场景。

## Wiki 更新摘要

- **新建 `wiki/dev-tools/git-worktree.md`**：Git Worktree 概念文件，含核心概念、场景表、命令速查、推荐实践、常见坑、边界
- **新建 `wiki/dev-tools/_index.md`**：Dev Tools 子目录索引
- **更新 `wiki/_index.md`**：添加 dev-tools 目录条目 + Git Worktree 跨主题概念

## 值得讨论的问题

1. **你在日常开发中用 worktree 还是切分支？** 如果一直用切分支，可能有些场景值得试试 worktree——特别是你在 Claude Code 多会话并行的工作流中。

2. **`.wt/` 目录约定要不要写进你的 CLAUDE.md？** 如果你希望 Claude Code 自动用 worktree 做并行任务，可能需要在项目规范里明确目录约定。

3. **dev-tools 这个 wiki 目录你觉得有价值吗？** 目前只有 git worktree 一个条目。你日常还有哪些工具/命令的知识值得系统化？比如 git rebase 策略、shell 脚本模式、Docker workflow 等。

4. **worktree 与你的 monorepo (personal/) 的编辑器集成体验如何？** VSCode/Zed 打开多个 worktree 目录时的体验差异可能影响你是否真的会用它。
