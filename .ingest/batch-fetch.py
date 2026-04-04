#!/usr/bin/env python3
"""
batch-fetch.py — Parse topic files for URL tables and batch-fetch them.

Reads markdown tables from topic files (projects/ai-learning/topics/*.md),
extracts URLs, and calls fetch-url.py for each one.

Usage:
    python3 .ingest/batch-fetch.py <topic-file> [--tier N] [--dry-run]
    python3 .ingest/batch-fetch.py projects/ai-learning/topics/ml-fundamentals.md --tier 1
    python3 .ingest/batch-fetch.py projects/ai-learning/topics/*.md --dry-run
"""

import argparse
import re
import subprocess
import sys
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_DIR = SCRIPT_DIR.parent
FETCH_SCRIPT = SCRIPT_DIR / "fetch-url.py"

# Delay between fetches (seconds) to avoid rate limiting
FETCH_DELAY = 3


def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter as a simple dict."""
    fm = {}
    if not content.startswith("---"):
        return fm
    end = content.find("---", 3)
    if end == -1:
        return fm
    for line in content[3:end].splitlines():
        line = line.strip()
        if ":" in line:
            key, val = line.split(":", 1)
            fm[key.strip()] = val.strip().strip('"').strip("'")
    return fm


def parse_urls_from_table(content: str, tier_filter: int | None = None) -> list[dict]:
    """Parse markdown tables to extract URLs with tier info.

    Returns list of dicts: {url, title, source, tier}
    """
    urls = []
    current_tier = None
    in_table = False
    header_cols = []

    for line in content.splitlines():
        line_stripped = line.strip()

        # Detect tier headers like "## Tier 1 — 必读" or "## Tier 2 — 推荐"
        tier_match = re.match(r"^#{1,3}\s+Tier\s+(\d+)", line_stripped)
        if tier_match:
            current_tier = int(tier_match.group(1))
            in_table = False
            header_cols = []
            continue

        # Skip if filtering by tier and this isn't the right one
        if tier_filter is not None and current_tier is not None and current_tier != tier_filter:
            continue

        # Detect table header row
        if "|" in line_stripped and not in_table:
            cols = [c.strip() for c in line_stripped.split("|")]
            # Check if this looks like a header row (has URL or 标题 columns)
            col_lower = [c.lower() for c in cols]
            if any(k in col_lower for k in ["url", "标题", "title", "#"]):
                header_cols = cols
                in_table = True
                continue

        # Skip separator row
        if in_table and re.match(r"^\|[\s\-:|]+\|$", line_stripped):
            continue

        # Parse data rows
        if in_table and "|" in line_stripped:
            cols = [c.strip() for c in line_stripped.split("|")]

            if len(cols) < len(header_cols):
                in_table = False
                continue

            # Find URL column
            url = None
            title = None
            source = None
            status = None

            for i, header in enumerate(header_cols):
                if i >= len(cols):
                    break
                h = header.lower()
                val = cols[i].strip()
                if h == "url":
                    url = val
                elif h in ("标题", "title"):
                    title = val
                elif h == "source":
                    source = val
                elif h == "status":
                    status = val

            if url and url.startswith("http") and status != "✅":
                urls.append({
                    "url": url,
                    "title": title or "Unknown",
                    "source": source or "Unknown",
                    "tier": current_tier or 0,
                })
        elif in_table and "|" not in line_stripped:
            # End of table
            in_table = False

    return urls


def update_status(file_path: Path, url: str, new_status: str = "✅"):
    """Update the status column for a URL in the topic file."""
    content = file_path.read_text(encoding="utf-8")
    # Find the line containing this URL and replace ⬜ with ✅
    lines = content.splitlines()
    for i, line in enumerate(lines):
        if url in line and "⬜" in line:
            lines[i] = line.replace("⬜", new_status, 1)
            break
    file_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def fetch_url(url: str, source: str, tags: list[str], dry_run: bool = False) -> bool:
    """Call fetch-url.py for a single URL. Returns True on success."""
    cmd = [
        "python3", str(FETCH_SCRIPT),
        url,
        "--source", source,
        "--tags", ",".join(tags),
        "--no-translate",
    ]
    if dry_run:
        cmd.append("--dry-run")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if result.returncode != 0:
            print(f"  ✗ Error: {result.stderr.strip()}", file=sys.stderr)
            return False
        # Print fetch-url.py's stderr (status messages)
        if result.stderr:
            for line in result.stderr.strip().splitlines():
                print(f"  {line}", file=sys.stderr)
        return True
    except subprocess.TimeoutExpired:
        print(f"  ✗ Timeout fetching {url}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description="Batch fetch URLs from topic files")
    parser.add_argument("files", nargs="+", help="Topic file(s) to process")
    parser.add_argument("--tier", type=int, help="Only fetch URLs from this tier (1, 2, or 3)")
    parser.add_argument("--dry-run", action="store_true", help="Print what would be fetched")
    args = parser.parse_args()

    total_fetched = 0
    total_skipped = 0
    total_errors = 0

    for file_arg in args.files:
        file_path = Path(file_arg)
        if not file_path.is_absolute():
            file_path = REPO_DIR / file_path
        if not file_path.exists():
            print(f"✗ File not found: {file_path}", file=sys.stderr)
            continue

        content = file_path.read_text(encoding="utf-8")
        fm = parse_frontmatter(content)
        topic = fm.get("topic", file_path.stem)

        # Derive tags from topic name
        tags = [w for w in re.split(r"[\s/&]+", topic) if len(w) > 1]

        urls = parse_urls_from_table(content, tier_filter=args.tier)

        tier_label = f" (Tier {args.tier})" if args.tier else ""
        print(f"\n{'='*60}", file=sys.stderr)
        print(f"Topic: {topic}{tier_label}", file=sys.stderr)
        print(f"URLs to fetch: {len(urls)}", file=sys.stderr)
        print(f"{'='*60}", file=sys.stderr)

        if not urls:
            print("  No URLs found (or all already fetched)", file=sys.stderr)
            continue

        for i, entry in enumerate(urls):
            url = entry["url"]
            title = entry["title"]
            source = entry["source"]
            tier = entry["tier"]

            print(f"\n[{i+1}/{len(urls)}] Tier {tier}: {title}", file=sys.stderr)
            print(f"  URL: {url}", file=sys.stderr)
            print(f"  Source: {source}", file=sys.stderr)

            if args.dry_run:
                print(f"  [DRY RUN] Would fetch", file=sys.stderr)
                total_fetched += 1
                continue

            success = fetch_url(url, source, tags, dry_run=False)
            if success:
                total_fetched += 1
                update_status(file_path, url, "✅")
            else:
                total_errors += 1

            # Rate limiting delay (skip for last URL)
            if i < len(urls) - 1:
                time.sleep(FETCH_DELAY)

    # Summary
    print(f"\n{'='*60}", file=sys.stderr)
    print(f"Done! Fetched: {total_fetched}, Errors: {total_errors}, Skipped: {total_skipped}", file=sys.stderr)


if __name__ == "__main__":
    main()
