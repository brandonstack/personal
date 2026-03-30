---
allowed-tools: Read, Write, Edit, Bash(mv:*), Bash(rm:*)
description: Reformat and compress an inbox file — restructure content, improve information density, and rename to standard format
---

## Input

$ARGUMENTS

## Your task

Determine the input type:
- **If the input is a file path** (e.g. `inbox/foo.md`): Read the file and process its content.
- **If the input is raw text**: Use the text directly as the content to process. Create a new file in `inbox/`.

Then do the following steps in order:

### 1. Analyze the content

Understand the topic, structure, and information density.

### 2. Restructure and compress

Rewrite the content with these goals:
- **Compress**: Remove redundancy, filler, repetitive phrasing, and low-density content. Keep information-rich parts.
- **Restructure**: Organize into clear sections with markdown headings, lists, and blockquotes where appropriate.
- **Preserve voice**: If the content is personal notes or journal, keep first-person. Don't add corporate/formal tone.
- **Remove fluff**: Cut AI-generated pleasantries, transitional phrases, and rhetorical questions that add no value.
- **Keep what matters**: Actionable insights, key decisions, concrete facts, personal realizations.

### 3. Add frontmatter

Ensure the file has proper YAML frontmatter:
```yaml
---
source: "<source name if known>"
url: "<url if applicable>"
date: "YYYY-MM-DD"
tags: [relevant, tags]
status: "raw"
---
```

If the file already has frontmatter, keep and update it. If `date` is missing, infer from filename or content.

### 4. Rename to standard format

Rename the file to match the inbox naming convention:
```
inbox/<YYYYMMDD>-<title-slug>.md
```

- `YYYYMMDD`: the date from frontmatter or filename
- `<title-slug>`: a short, descriptive, lowercase, hyphenated slug derived from the content topic (English)
- Remove the original file after writing the new one (if the name changed)

### 5. Report

Briefly tell the user what you did: what was removed/compressed, and the new filename.