---
allowed-tools: Read, Edit, Glob, Grep
description: Digest an inbox article — extract skeleton, generate Socratic questions, find connections to existing knowledge, and produce action items. Appends digest content directly to the inbox file.
---

## Input

$ARGUMENTS

## Your task

The input is a path to an inbox file (e.g. `inbox/anthropic/20260328-article.md`).

This skill digests the article by appending structured analysis (skeleton, Socratic questions, connections, action items) directly to the inbox file. No separate digest file is created.

Follow these steps in order:

### 1. Read the source file

Read the file at the given path. If a `-zh.md` counterpart exists (same name with `-zh` before `.md`), prefer reading that version for Chinese comprehension.

### 2. Check status

Check the file's frontmatter `status` field:
- If `status: digested` or `status: promoted`, tell the user and stop — do not re-digest. Ask if they want to overwrite.
- If `status: raw` or no status field, proceed.

### 3. Extract the skeleton

Produce the logical backbone of the article:
- The central claim or thesis (one sentence)
- 3–5 supporting points, in order of the argument
- Any key data, numbers, or concrete examples that anchor the argument

This is NOT a summary. Do not reproduce the full content. Extract the structure.

### 4. Generate Socratic questions

Write 3–5 questions the user cannot answer by re-reading the article. Each question must require the user to:
- Connect the material to their own situation or experience
- Make a judgment or take a position
- Identify a gap between the article's claims and their current practice

Bad question: "什么是 harness engineering？"
Good question: "你现在这个 personal repo 算不算一个 harness？哪里还缺？"

Questions should be in Chinese, specific to this article's content, and challenging.

### 5. Scan areas/ for connections

Glob all `.md` files under `areas/` (exclude README.md files). Use the article's key topics and tags to Grep relevant files.

For each connection found, state clearly whether the article:
- **支持** — confirms or reinforces something already in areas/
- **矛盾** — contradicts or challenges existing notes
- **延伸** — extends or adds nuance to existing notes
- **已过时** — the areas/ note supersedes what's in this article

Format: `→ [areas/career/ai-engineer-roadmap.md] <one-line explanation>`

If no genuine connections exist, say so explicitly. Do not fabricate connections.

### 6. Generate action items

Write 2–4 concrete, specific next actions. Each action must:
- Be something the user can actually do (not "think about X")
- Point to the specific `projects/` or `areas/` file where it belongs

Format: `[ ] <action> → [areas/career/skills-and-growth.md]`

### 7. Append digest content to the inbox file

Use the Edit tool to append the following structure to the END of the inbox file:

```

---
<!-- 以下为消化内容，由 /digest 生成 -->

## 骨架

<central claim>

- <supporting point 1>
- <supporting point 2>
- <supporting point 3>
...

## 苏格拉底问题

1. <question>
2. <question>
3. <question>
...

## 连接

→ [areas/...] <explanation>
→ [areas/...] <explanation>

## 行动

- [ ] <action> → [projects/... or areas/...]
- [ ] <action> → [projects/... or areas/...]

---
<!-- 以下为个人思考 -->

```

### 8. Update frontmatter

Edit the frontmatter to set `status: "digested"`. If no `status` field exists, add it.

### 9. Report

Tell the user:
- The file path (same inbox file, now with digest appended)
- Show the **苏格拉底问题** section again so they see it immediately in the chat
- Invite them to answer the questions now in the conversation, or fill in the file directly