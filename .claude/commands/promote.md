---
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(mv:*), Bash(mkdir:*)
description: Promote a digested inbox article to areas/ — integrate distilled knowledge into the long-term knowledge base, then move the file to resources/
---

## Input

$ARGUMENTS

## Your task

The input is a path to an inbox file that has been digested (e.g. `inbox/anthropic/20260328-article.md`).

This skill promotes the distilled knowledge from a digested inbox file into the appropriate `areas/` file, then moves the inbox file to `resources/<topic>/` as a reference.

Follow these steps in order:

### 1. Read the file

Read the file at the given path. Check the `status` field:
- If `status: promoted`, tell the user it's already promoted (show `promoted_to`) and stop.
- If `status: digested`, proceed.
- If `status: raw` or no status, tell the user to run `/digest` first and stop.

### 2. Identify what to promote

From the file, extract:
- The **骨架** section — the logical structure worth preserving
- The **行动** section — any unchecked items `[ ]`
- Any user notes below the `<!-- 以下为个人思考 -->` comment (these are personal reflections worth integrating)

### 3. Find the target areas/ file

Read each `areas/*/README.md` to understand what files exist and their topics.

Based on the content's topic and tags, identify the best target file(s). Present the candidates to the user with one line explaining each:

```
建议写入：
- [areas/career/ai-engineer-roadmap.md] — 骨架内容与 AI 系统工程师路径直接相关
- [areas/career/skills-and-growth.md] — 行动项中的"保持亲手构建"属于这里
```

Ask the user to confirm the target(s) before writing.

### 4. Write to areas/

For each confirmed target file:
- Read the current content
- Append the relevant digest content at the end of the appropriate section (or at the file end if unclear)
- Format: use a dated subsection header `### YYYY-MM-DD: <topic>` to mark the addition
- Include a backref: `> 来源：[resources/<topic>/YYYYMMDD-<slug>.md](../resources/<topic>/YYYYMMDD-<slug>.md)`

If a new areas/ file is needed (no suitable existing file):
- Follow areas/ rules: specific slug (not generic), under 80 lines, no content in README
- Create the file with proper frontmatter-free markdown
- Add it to the areas/ README index

### 5. Determine resources/ topic directory

Based on the article's content and tags, suggest a topic directory under `resources/` (e.g. `ai-engineering/`, `mental-health/`, `productivity/`). Check if a suitable directory already exists:

```bash
ls resources/
```

If no suitable directory exists, create one. Ask the user to confirm the topic directory.

### 6. Move the file to resources/

Move the inbox file to `resources/<topic>/`:

```bash
mkdir -p resources/<topic>
mv <inbox-file-path> resources/<topic>/
```

### 7. Update frontmatter

Edit the file (now in resources/) to set:
```yaml
status: "promoted"
promoted_to: "areas/career/ai-engineer-roadmap.md"  # comma-separated if multiple
```

### 8. Report

Tell the user what was written and where:
- Which areas/ file(s) were updated
- Where the inbox file was moved to in resources/
- Show the areas/ file path(s) so they can navigate directly