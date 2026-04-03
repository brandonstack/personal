# Git Worktree

为同一个 Git 仓库创建多个独立工作目录（工作区），每个可检出不同分支/提交，共享底层 `.git/objects`，实现真正的并行开发。

## 核心概念

- **一个仓库，多个工作目录**：每个 worktree 是一个轻量级独立工作区，共享对象库和索引
- **硬约束**：同一分支同一时刻只能在一个 worktree 被检出。要并行同一起点，用不同分支名或 `--detach`
- **vs 切分支+stash**：无需频繁 stash，上下文隔离更彻底，误操作风险更低
- **vs 多仓 clone**：共享对象库省磁盘/网络，创建/切换更快

## 典型场景

| 场景 | 做法 |
|------|------|
| 并行开发 + 热修 | 主区继续 main 开发，另起 worktree 做 release 热修 |
| 跨版本复现 | 为老版本建临时 worktree，不污染当前环境 |
| 长分支隔离 | 复杂重构放独立 worktree，远离日常开发 |
| 大仓多版本编译 | monorepo 多分支同时编译，复用对象库 |
| PR/评审验证 | 临时拉起 PR 对应提交，跑完验证即删 |
| **Claude Code 多会话并行** | 每个 worktree 跑一个独立 session，人做调度器 |

## 命令速查

```bash
# 查看所有工作区
git worktree list

# 基于远端分支新建 worktree
git worktree add ~/repo/.wt/feature-x -b feature/x origin/main

# 基于已有本地分支
git worktree add ~/repo/.wt/release-1-5 release/1.5

# 临时查看某个 commit（detached HEAD）
git worktree add --detach ~/repo/.wt/tmp-check 4f1e2c3

# 对目标 worktree 执行命令
git -C ~/repo/.wt/feature-x push -u origin feature/x

# 删除 worktree
git worktree remove ~/repo/.wt/feature-x

# 清理残留记录（目录已被手动删时）
git worktree prune

# 锁定保护（防误删）
git worktree lock ~/repo/.wt/release-1-5 --reason "hotfix in progress"

# 移动 worktree 路径
git worktree move ~/repo/.wt/old-name ~/repo/.wt/new-name

# 仓库整体移动后修复内部链接
git worktree repair
```

## 推荐实践

- **目录约定**：在仓库根目录旁建 `.wt/` 集中管理所有 worktree
- **命名规范**：worktree 目录名与分支名对应，便于识别
- **用完即清**：`remove` → `prune`，不要让 worktree 积累
- **保护关键分支**：`lock` 附加原因，防止被误清理
- **远端分支先 fetch**：`git fetch origin release/1.5:release/1.5` 再建 worktree，更稳妥

## 常见坑

| 问题 | 原因 & 解决 |
|------|-------------|
| `branch already checked out` | 同一分支已在另一 worktree。改用不同分支名或 `--detach` |
| `worktree is locked` | `unlock` 后再操作；异常终止后试 `repair` → `prune` |
| `remove` vs `prune` 混淆 | `remove` 删指定 worktree，`prune` 清理无效残留记录 |
| `remove -f` 丢数据 | 先 commit 或 stash，再 remove |

## 边界：何时不用 worktree

- 需要完全隔离的 `.git` 配置（不同 hooks/设置）→ 多仓 clone
- 只需部分目录检出 → `sparse-checkout`（可与 worktree 组合）
- 多仓协作组织 → `submodule` / `subtree`

→ [wiki/claude-code/workflow-patterns.md](../claude-code/workflow-patterns.md) — Claude Code 多会话并行使用 worktree 的具体模式

> 来源：resources/clippings/git worktree 实战指南：使用场景、常用命令、解决的问题与日常工作流.md
