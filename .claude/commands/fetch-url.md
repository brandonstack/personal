---
allowed-tools: Read, Write, Edit, Bash(python3:*), Bash(curl:*)
description: Fetch a URL via Jina Reader, save original, then translate to Chinese with summary and comments
---

## Input

$ARGUMENTS

The input should contain: `<url>` and optionally `--source SOURCE --tags tag1,tag2 --date YYYY-MM-DD`

If `--source` is not provided, infer from the URL domain (e.g. openai.com → OpenAI).
If `--tags` is not provided, infer from the article content after fetching.

## Your task

### Step 1: Fetch the original article

Run the fetch script:
```bash
python3 scripts/ingest/fetch-url.py <url> --source <SOURCE> --tags <TAGS> [--date <DATE>]
```

The script outputs the saved file path to stdout. Read that file.

If the script fails (e.g. Jina Reader unreachable), tell the user and stop.

### Step 2: Read the original article

Read the file created in step 1. Understand its structure and content.

### Step 3: Create the Chinese translation file

Create a `-zh.md` file alongside the original (same directory, same name but replace `.md` with `-zh.md`).

The file must contain:

1. **Same frontmatter** as the original (source, url, date, tags)
2. **`## Summary`** — A concise Chinese summary (3-5 sentences) of the entire article
3. **`---`** separator
4. **Full Chinese translation** — Translate every section faithfully. Do NOT compress or omit content. Keep all section headings (translated). Keep code blocks, lists, and structural elements.
5. **`---`** separator
6. **`## My Comments`** — Your analysis and insights in Chinese: key takeaways, implications, what's missing, how it relates to the reader's context.

### Important rules for translation

- **No lossy compression** — translate everything, do not summarize sections
- Keep technical terms in English where natural (e.g. agent, PR, CI, linter, worktree)
- Use 「」 for Chinese quotation marks
- Write in segments — use Edit tool to append sections rather than writing the entire file at once (avoids network timeout on large files)
- The original file name ends with `.md`, the translation file name should end with `-zh.md` (e.g. `20260211-harness-engineering.md` → `20260211-harness-engineering-zh.md`)

### Step 4: Report

Tell the user:
- Original file path
- Translation file path
- Brief summary of the article