---
allowed-tools: Bash(python3:*), Read
description: Fetch a URL (web, Twitter, WeChat auto-routing), save original, then translate to Chinese with summary and comments
---

## Input

$ARGUMENTS

The input should contain: `<url>` and optionally `--source SOURCE --tags tag1,tag2 --date YYYY-MM-DD`

If `--source` is not provided, infer from the URL domain (e.g. openai.com → OpenAI).
If `--tags` is not provided, infer 2-3 relevant tags from the URL/domain.

## Your task

### Step 1: Run the fetch + translate script

```bash
python3 .ingest/fetch-url.py <url> --source <SOURCE> --tags <TAGS> [--date <DATE>]
```

The script will:
1. Fetch the article via fetch-skill (auto-routes: web → Jina Reader, Twitter → FxTwitter, WeChat → wechat-exporter, with fallback chain)
2. Clean and save the original as `resources/pending/<source>/YYYYMMDD-<slug>.md`
3. Translate to Chinese via `claude` CLI and save as `resources/pending/<source>/YYYYMMDD-<slug>-zh.md`

The script outputs saved file paths to stdout (one per line).

### Step 2: Report

Tell the user the created file paths and a one-line summary of what was fetched.

If the script failed, show the error and suggest fixes (e.g. network issue, Jina Reader down).

### Options

- Add `--no-translate` to skip translation
- Add `--dry-run` to preview without writing files