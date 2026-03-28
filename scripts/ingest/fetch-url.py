#!/usr/bin/env python3
"""
fetch-url.py — Fetch a URL via Jina Reader, clean it, save as inbox markdown.

Usage:
    python3 scripts/ingest/fetch-url.py <url> --source SOURCE --tags tag1,tag2 [--date YYYY-MM-DD] [--dry-run]

Outputs the saved file path to stdout on success.
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_DIR = SCRIPT_DIR.parent.parent
INBOX_DIR = REPO_DIR / "inbox"


def slugify(text: str, max_len: int = 50) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = text.strip("-")
    return text[:max_len].rstrip("-")


def source_slug(name: str) -> str:
    return slugify(name, max_len=40)


def load_existing_urls(source_dir: Path) -> set:
    urls = set()
    if not source_dir.exists():
        return urls
    for md_file in source_dir.glob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8")
            for line in content.splitlines()[:20]:
                m = re.match(r'^url:\s*[\'"]?(.+?)[\'"]?\s*$', line)
                if m:
                    urls.add(m.group(1).strip())
                    break
        except Exception:
            pass
    return urls


def fetch_via_jina(url: str) -> str:
    jina_url = f"https://r.jina.ai/{url}"
    result = subprocess.run(
        ["curl", "-sL", "--max-time", "60", jina_url, "-H", "Accept: text/markdown"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(f"curl error: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    if not result.stdout.strip():
        print("Error: empty response from Jina Reader", file=sys.stderr)
        sys.exit(1)
    return result.stdout


def extract_title(content: str) -> str:
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return "Untitled"


def clean_content(raw: str) -> str:
    """Remove navigation, footers, and Jina metadata from fetched markdown."""
    lines = raw.splitlines()

    # Skip Jina metadata header (Title:, URL Source:, Markdown Content:)
    start = 0
    for i, line in enumerate(lines):
        if line.strip().startswith("# "):
            start = i
            break
        if line.strip() == "Markdown Content:":
            start = i + 1
            break

    # Find footer cutoff — look for common footer patterns
    footer_patterns = [
        r"^#{1,3}\s*(Keep reading|Our Research|Latest Advancements|Safety|Support|More|Terms|Footer)",
        r"^OpenAI © \d{4}",
        r"^\[View all\]",
    ]
    end = len(lines)
    # Only scan the last 40% of the document for footers
    scan_start = max(start, int(len(lines) * 0.6))
    for i in range(scan_start, len(lines)):
        for pat in footer_patterns:
            if re.match(pat, lines[i].strip(), re.IGNORECASE):
                end = i
                break
        if end != len(lines):
            break

    cleaned = lines[start:end]

    # Remove leading/trailing blank lines
    while cleaned and not cleaned[0].strip():
        cleaned.pop(0)
    while cleaned and not cleaned[-1].strip():
        cleaned.pop()

    return "\n".join(cleaned)


def main():
    parser = argparse.ArgumentParser(description="Fetch URL via Jina Reader → inbox/")
    parser.add_argument("url", help="URL to fetch")
    parser.add_argument("--source", required=True, help="Source name (e.g. OpenAI)")
    parser.add_argument("--tags", type=str, default="", help="Comma-separated tags")
    parser.add_argument("--date", type=str, help="Override date (YYYY-MM-DD), default: auto-detect or today")
    parser.add_argument("--dry-run", action="store_true", help="Print what would be created")
    args = parser.parse_args()

    tags = [t.strip() for t in args.tags.split(",") if t.strip()] if args.tags else []
    slug = source_slug(args.source)
    source_dir = INBOX_DIR / slug

    # Dedup check
    existing_urls = load_existing_urls(source_dir)
    if args.url in existing_urls:
        print(f"Skipped: URL already exists in {slug}/", file=sys.stderr)
        sys.exit(0)

    # Fetch
    print(f"Fetching {args.url} via Jina Reader...", file=sys.stderr)
    raw = fetch_via_jina(args.url)

    # Clean
    content = clean_content(raw)
    title = extract_title(content)

    # Date
    if args.date:
        date_str = args.date
    else:
        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    date_compact = date_str.replace("-", "")
    title_slug = slugify(title, max_len=50)
    filename = f"{date_compact}-{title_slug}.md"
    note_path = source_dir / filename

    if note_path.exists():
        print(f"Skipped: {filename} already exists", file=sys.stderr)
        sys.exit(0)

    # Build note
    tags_yaml = json.dumps(tags, ensure_ascii=False)
    fm = "\n".join([
        "---",
        f"source: {json.dumps(args.source, ensure_ascii=False)}",
        f"url: {json.dumps(args.url, ensure_ascii=False)}",
        f'date: "{date_str}"',
        f"tags: {tags_yaml}",
        "---",
        "",
    ])
    note_content = fm + content + "\n"

    if args.dry_run:
        print(f"[DRY] Would create: {slug}/{filename}", file=sys.stderr)
        print(f"  Title: {title}", file=sys.stderr)
        print(f"  Content: {len(content)} chars", file=sys.stderr)
        sys.exit(0)

    source_dir.mkdir(parents=True, exist_ok=True)
    note_path.write_text(note_content, encoding="utf-8")
    print(f"Created: {slug}/{filename}", file=sys.stderr)
    # Output path to stdout for skill to consume
    print(str(note_path))


if __name__ == "__main__":
    main()
