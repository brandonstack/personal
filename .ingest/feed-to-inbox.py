#!/usr/bin/env python3
"""
feed-to-inbox.py — Pull entries from `feed` CLI, write new ones into resources/pending/<source>/.

Usage:
    python3 .ingest/feed-to-inbox.py [--hours 24] [--dry-run] [--keywords AI,LLM] [--min-points N]

Requires: `feed` CLI (go install github.com/odysseus0/feed/cmd/feed@latest)
          pyyaml (pip install pyyaml)
"""

import argparse
import json
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_DIR = SCRIPT_DIR.parent
INBOX_DIR = REPO_DIR / "resources" / "pending"
SOURCES_FILE = SCRIPT_DIR / "sources.yaml"

try:
    import yaml
except ImportError:
    print("Error: pyyaml required. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


def load_sources() -> dict:
    with open(SOURCES_FILE, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def slugify(text: str, max_len: int = 50) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = text.strip("-")
    return text[:max_len].rstrip("-")


def source_slug(name: str) -> str:
    return slugify(name, max_len=40)


def load_existing_urls(source_dir: Path) -> set:
    """Scan existing markdown files and extract their url: frontmatter lines."""
    urls = set()
    if not source_dir.exists():
        return urls
    for md_file in source_dir.glob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8")
            # Only scan frontmatter (first ~20 lines)
            for line in content.splitlines()[:20]:
                m = re.match(r"^url:\s*['\"]?(.+?)['\"]?\s*$", line)
                if m:
                    urls.add(m.group(1).strip())
                    break
        except Exception:
            pass
    return urls


def get_feed_id_to_name() -> dict:
    """Map feed_id → feed name from feed CLI."""
    result = subprocess.run(["feed", "get", "feeds", "-o", "json"], capture_output=True, text=True)
    if result.returncode != 0:
        return {}
    try:
        feeds = json.loads(result.stdout)
        return {f["id"]: f.get("name", "") or f.get("title", "") for f in feeds}
    except Exception:
        return {}


def get_feed_id_to_url() -> dict:
    result = subprocess.run(["feed", "get", "feeds", "-o", "json"], capture_output=True, text=True)
    if result.returncode != 0:
        return {}
    try:
        feeds = json.loads(result.stdout)
        return {f["id"]: f.get("feed_url", "") or f.get("url", "") for f in feeds}
    except Exception:
        return {}


def get_entries(hours: int, limit: int, allowed_urls: set) -> list:
    result = subprocess.run(
        ["feed", "get", "entries", "--limit", str(limit), "-o", "json"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(f"feed CLI error: {result.stderr}", file=sys.stderr)
        return []

    entries = json.loads(result.stdout)

    # Filter to sources.yaml feeds only
    if allowed_urls:
        id_to_url = get_feed_id_to_url()
        entries = [e for e in entries if id_to_url.get(e.get("feed_id"), "") in allowed_urls]

    # Filter by time window
    cutoff = time.time() - (hours * 3600)
    filtered = []
    for e in entries:
        published = e.get("published_at", "")
        try:
            dt = datetime.fromisoformat(published.replace("Z", "+00:00"))
            if dt.timestamp() < cutoff:
                continue
        except Exception:
            pass
        filtered.append(e)

    return filtered


def matches_keywords(entry: dict, keywords: list) -> bool:
    if not keywords:
        return True
    text = (entry.get("title", "") + " " + (entry.get("content_md", "") or entry.get("content", ""))).lower()
    return any(kw.lower() in text for kw in keywords)


def extract_hn_points(entry: dict) -> int:
    content = entry.get("content_md", "") or entry.get("content", "")
    m = re.search(r"Points:\s*(\d+)", content)
    return int(m.group(1)) if m else 0


def passes_min_points(entry: dict, min_points: int) -> bool:
    if min_points <= 0:
        return True
    if "Hacker News" not in entry.get("feed_title", ""):
        return True
    return extract_hn_points(entry) >= min_points


def write_note(entry: dict, feed_name: str, feed_tags: list, dry_run: bool) -> bool:
    """Write a single entry as an inbox note. Returns True if created, False if skipped."""
    title = entry.get("title", "Untitled")
    url = entry.get("url", "")
    content = entry.get("content_md", "") or entry.get("content", "")
    published = entry.get("published_at", "")

    # Normalize date
    try:
        dt = datetime.fromisoformat(published.replace("Z", "+00:00"))
        date_str = dt.strftime("%Y-%m-%d")
        date_iso = dt.isoformat()
    except Exception:
        dt = datetime.now(timezone.utc)
        date_str = dt.strftime("%Y-%m-%d")
        date_iso = dt.isoformat()

    slug = source_slug(feed_name)
    title_slug = slugify(title, max_len=50)
    note_date = date_str.replace("-", "")  # 20260328
    filename = f"{note_date}-{title_slug}.md"

    source_dir = INBOX_DIR / slug
    note_path = source_dir / filename

    # Dedup: check URL against existing files in this source dir
    existing_urls = load_existing_urls(source_dir)
    if url and url in existing_urls:
        return False
    if note_path.exists():
        return False

    tags_yaml = json.dumps(feed_tags, ensure_ascii=False)

    # Build frontmatter
    fm_lines = [
        "---",
        f"source: {json.dumps(feed_name, ensure_ascii=False)}",
        f"url: {json.dumps(url, ensure_ascii=False)}",
        f"date: \"{date_str}\"",
        f"tags: {tags_yaml}",
        "---",
        "",
    ]

    # Body: title + content (truncated)
    body_lines = [f"# {title}", ""]
    if content:
        body_lines.append(content[:3000])

    note_content = "\n".join(fm_lines + body_lines)

    if dry_run:
        print(f"  [DRY] {slug}/{filename}", file=sys.stderr)
        return True

    source_dir.mkdir(parents=True, exist_ok=True)
    note_path.write_text(note_content, encoding="utf-8")
    return True


def main():
    parser = argparse.ArgumentParser(description="feed CLI → resources/pending/")
    parser.add_argument("--hours", type=int, default=24, help="Look back N hours (default: 24)")
    parser.add_argument("--dry-run", action="store_true", help="Print what would be created, don't write files")
    parser.add_argument("--keywords", type=str, help="Comma-separated keywords to filter (e.g. AI,LLM)")
    parser.add_argument("--limit", type=int, default=200, help="Max entries to fetch (default: 200)")
    parser.add_argument("--min-points", type=int, default=0, help="Min HN points (0=no filter)")
    args = parser.parse_args()

    keywords = [k.strip() for k in args.keywords.split(",")] if args.keywords else []

    sources = load_sources()
    # Build name → config map for blog/aggregator feeds (not podcasts)
    feed_configs = {
        f["url"].rstrip("/"): f
        for f in sources.get("feeds", [])
        if f.get("type") != "podcast"
    }
    allowed_urls = set(feed_configs.keys())

    # Also need url → name lookup
    url_to_config = feed_configs

    print(f"Fetching entries (last {args.hours}h, limit {args.limit})...", file=sys.stderr)
    entries = get_entries(args.hours, args.limit, allowed_urls)
    print(f"  {len(entries)} entries from whitelisted feeds", file=sys.stderr)

    if keywords:
        entries = [e for e in entries if matches_keywords(e, keywords)]
        print(f"  After keyword filter: {len(entries)}", file=sys.stderr)

    if args.min_points > 0:
        before = len(entries)
        entries = [e for e in entries if passes_min_points(e, args.min_points)]
        print(f"  After points filter (>={args.min_points}): {len(entries)} (dropped {before - len(entries)})", file=sys.stderr)

    # Need feed_id → url to look up config
    id_to_url = get_feed_id_to_url()

    created = 0
    skipped = 0
    for entry in entries:
        feed_url = id_to_url.get(entry.get("feed_id"), "").rstrip("/")
        cfg = url_to_config.get(feed_url, {})
        feed_name = cfg.get("name") or entry.get("feed_title", "unknown")
        feed_tags = cfg.get("tags", ["rss"])

        if write_note(entry, feed_name, feed_tags, args.dry_run):
            created += 1
        else:
            skipped += 1

    print(f"\nDone: {created} created, {skipped} skipped (already exists)", file=sys.stderr)


if __name__ == "__main__":
    main()
