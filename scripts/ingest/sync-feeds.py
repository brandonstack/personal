#!/usr/bin/env python3
"""
sync-feeds.py — Sync sources.yaml feeds to `feed` CLI database.

Usage:
    python3 scripts/ingest/sync-feeds.py [--dry-run] [--fetch]

Reads scripts/ingest/sources.yaml, adds missing feeds to feed CLI DB.
Does NOT remove feeds from DB that aren't in sources.yaml.

Requires: `feed` CLI, pyyaml
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
SOURCES_FILE = SCRIPT_DIR / "sources.yaml"


def load_sources():
    with open(SOURCES_FILE, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def get_existing_feeds() -> set:
    result = subprocess.run(["feed", "get", "feeds", "-o", "json"], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"feed CLI error: {result.stderr}", file=sys.stderr)
        return set()
    try:
        feeds = json.loads(result.stdout)
        return {f.get("feed_url", "").rstrip("/") for f in feeds}
    except Exception:
        return set()


def add_feed(url: str, dry_run: bool) -> bool:
    if dry_run:
        print(f"  [DRY] Would add: {url}", file=sys.stderr)
        return True
    result = subprocess.run(["feed", "add", "feed", url], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  Failed to add {url}: {result.stderr.strip()}", file=sys.stderr)
        return False
    return True


def main():
    parser = argparse.ArgumentParser(description="Sync sources.yaml -> feed CLI DB")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--fetch", action="store_true", help="Run feed fetch after sync")
    args = parser.parse_args()

    sources = load_sources()
    existing = get_existing_feeds()

    # Only sync non-podcast feeds (podcasts aren't managed through feed CLI)
    rss_feeds = [f for f in sources.get("feeds", []) if f.get("type") != "podcast"]

    added = 0
    skipped = 0
    for feed_cfg in rss_feeds:
        url = feed_cfg["url"].rstrip("/")
        if url in existing:
            skipped += 1
            continue
        print(f"  Adding: {feed_cfg['name']} ({url})", file=sys.stderr)
        if add_feed(url, args.dry_run):
            added += 1

    print(f"\nSync done: {added} added, {skipped} already tracked", file=sys.stderr)

    if args.fetch and not args.dry_run:
        print("Fetching new entries...", file=sys.stderr)
        subprocess.run(["feed", "fetch"], capture_output=True, text=True)
        print("  Done", file=sys.stderr)


if __name__ == "__main__":
    main()
