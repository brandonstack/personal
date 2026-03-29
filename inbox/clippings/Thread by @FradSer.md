---
title: "Thread by @FradSer"
source: "https://x.com/FradSer/status/2036619884122267745"
author:
  - "[[@FradSer]]"
published: 2026-03-25
created: 2026-03-29
description:
tags:
  - "clippings"
---
**Frad** @FradSer [2026-03-25](https://x.com/FradSer/status/2036619884122267745)

在公司里和同事分享了好几次，关于为什么我的 vibe coding 大家觉得又快又好，而且写的前端质量也肯起来不错的秘诀。我总结了一下，分享给大家。

第一个阶段我叫做全自动模式。先使用类似 superpowers 的工具，整体的流程其实没有什么新鲜的，先分析需求，然后写计划，最后再执行。我用的是自己魔改的版本 ，主要的区别是为了防止在每一个阶段 AI 因为幻觉可能会漏掉细节，在每个阶段都会强制启动一个 loop 去校验。 并且使用 BDD 部分替代 TDD 。https://github.com/FradSer/dotclaude/tree/main/superpowers…

上面的阶段收完菜之后，进入第二个阶段，我叫做半自动模式。主要靠发现问题，先用 /plan 模式，然后再去执行，如此反复。

这里面有一些技巧，多使用 git commit，类似于游戏的存档保存。所以我做了 https://git-agent.dev 。

如果有问题超过两次没有改好，有两种做法：

1\. 让 AI 从 git 的历史记录里去查看改动了什么东西，然后让它反思为什么会出现这种情况；

2\. 换一个新的模型，甚至新的工具。

还有就是，多使用 N 个窗口并行地去执行任务，但是要记得靠 prompt 手动地去区分范围。我不习惯使用 git worktree ，因为同时进行 N 个任务时，使用 worktree 最后 merge 的压力很大，容易出错。类似的流程应该在第一个步骤使用 superpowers 去解决。

关于提示词的小技巧，我很赞成 Claude Code 的观点，就是使用最少的限制，充分利用工具去让它自动获取上下文。但是人为地补充一些上下文也是非常关键的。

换到我们执行的操作来说，你可以随时打断，然后说类似于“你之前改了xxx”，或者“应该有xxx，你先看看，再执行”。

还有一个观点就是：把 AI 当老师，多去问“你做了什么事情”、“我应该怎么做”，推荐多使用 /btw ，在必要的时候打断，修改你的任务。

happy hack😘