#!/usr/bin/env python3
"""
This script updates the dates in markdown tables within the file.

`docs/aerial_autonomy_stacks.md`.

It performs the following steps:

1. Scans the markdown file for table rows.
2. If the first link in a row is a GitHub URL:
   - Extracts the owner/repo from the URL.
   - Queries the GitHub API for the latest commit date.
   - Replaces the row's final date cell with the commit date in MM/YYYY format.
3. Rows whose first link is not a GitHub URL are left untouched.

Requirements:
- Python 3.9+
- A valid GitHub token (optional) for authenticated API requests.

Environment Variables:
- `GITHUB_TOKEN`: Your GitHub personal access token for higher rate limits.

Usage:
    python docs/scripts/update_repo_dates.py
"""

import os
import re
import requests
from datetime import datetime
from pathlib import Path
from typing import Dict


# ───────────── Configuration ───────────────────────────────────────
MARKDOWN_FILE = Path("docs/aerial_autonomy_stacks.md")  # Adjust if needed
TIMEOUT_S = 10  # GitHub request timeout in seconds

# ───────────── Optional Auth Header ────────────────────────────────
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Set this in your shell
AUTH_HEADER = {"Authorization": f"Bearer {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
# If GITHUB_TOKEN is absent/empty, AUTH_HEADER will be {}

# ───────────── Regex Patterns ──────────────────────────────────────
LINK_RE = re.compile(r"\[([^\]]+)]\((https?://[^\)]+)\)")
GH_RE = re.compile(r"https://github\.com/([^/]+/[^/]+)")
LAST_UPDATED_RE = re.compile(r"_Table last updated on \*\*(.+)\*\*")

# ───────────── GitHub Helper with Simple Cache ─────────────────────
_cache: Dict[str, str] = {}  # Cache for owner/repo → MM/YYYY


def last_commit_mm_yyyy(repo: str) -> str:
    """
    Fetch the latest commit date for a given GitHub repository.

    Args:
        repo (str): The GitHub repository in the format 'owner/repo'.

    Returns:
        str: The latest commit date in MM/YYYY format,
        or "error" if the request fails.
    """
    if repo in _cache:
        return _cache[repo]

    url = f"https://api.github.com/repos/{repo}/commits"
    try:
        resp = requests.get(
            url,
            params={"per_page": 1},
            headers=AUTH_HEADER,
            timeout=TIMEOUT_S,
        )
        resp.raise_for_status()
        iso_date = resp.json()[0]["commit"]["committer"]["date"]
        dt = datetime.fromisoformat(iso_date.replace("Z", "+00:00"))
        _cache[repo] = dt.strftime("%m/%Y")
    except Exception as e:
        print(f"Error fetching data for {repo}: {e}")
        _cache[repo] = "error"

    return _cache[repo]


def refresh_row(line: str) -> str:
    """
    Update the date cell of a markdown table row with the latest commit date.

    If the first link in the row is a GitHub URL.

    Args:
        line (str): A single line from the markdown file.

    Returns:
        str: The updated line with the latest commit date,
        or the original line if no update is needed.
    """
    if not line.lstrip().startswith("|"):
        return line

    match = LINK_RE.search(line)
    if not match:
        return line

    url = match.group(2)
    gh_match = GH_RE.match(url)
    if not gh_match:
        return line

    owner_repo = "/".join(gh_match.group(1).split("/")[:2]).removesuffix(".git")
    new_date = last_commit_mm_yyyy(owner_repo)

    # Split the row on '|' while keeping leading/trailing empties
    parts = line.split("|")

    # Update the second-to-last cell (last non-empty element is after trailing '|')
    if len(parts) > 2:
        parts[-2] = f" {new_date} "

    return "|".join(parts)


def update_last_updated_sections(lines: list[str]) -> list[str]:
    """
    Update all "last updated" sections in the markdown file.

    Args:
        lines (list[str]): The lines of the markdown file.

    Returns:
        list[str]: The updated lines with all "last updated" sections updated.
    """
    now = datetime.utcnow().strftime("%B %dth, %Y at %I:%M:%S %p UTC")
    last_updated_text = f"_Table last updated on **{now}**_"

    updated_lines = []
    for line in lines:
        if LAST_UPDATED_RE.match(line):
            updated_lines.append(last_updated_text)
        else:
            updated_lines.append(line)

    return updated_lines


def main() -> None:
    """Process the markdown file and update GitHub-linked table rows."""
    if not MARKDOWN_FILE.exists():
        print(f"Error: Markdown file '{MARKDOWN_FILE}' not found.")
        return

    lines = MARKDOWN_FILE.read_text().splitlines()
    updated_lines = [refresh_row(line) for line in lines]
    updated_lines = update_last_updated_sections(updated_lines)
    MARKDOWN_FILE.write_text("\n".join(updated_lines))
    print("All GitHub-linked table rows updated.")


if __name__ == "__main__":
    main()
