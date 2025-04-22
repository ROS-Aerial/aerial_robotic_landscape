#!/usr/bin/env python3
"""
update_repo_dates.py
------------------------------------------------
• Scans docs/aerial_autonomy_stacks.md
• Looks at every markdown table row (any table)
• If the row’s first link is a GitHub URL:
      – Extract owner/repo
      – Query GitHub API for the latest commit
      – Replace the row’s final date cell with MM/YYYY
• Rows whose first link is *not* GitHub are left untouched.
"""

import os
import re
import requests
from datetime import datetime
from pathlib import Path

# ───────────── configuration ───────────────────────────────────────
MARKDOWN_FILE = Path("docs/aerial_autonomy_stacks.md")   # adjust if needed
TIMEOUT_S     = 10                                       # GitHub request timeout

# ───────────── Optional auth header ───────────────────────────
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")        # set this in your shell
AUTH_HEADER = {"Authorization": f"Bearer {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
# If GITHUB_TOKEN is absent / empty, AUTH_HEADER will be {}

# ───────────── regexes ─────────────────────────────────────────────
LINK_RE   = re.compile(r"\[([^\]]+)]\((https?://[^\)]+)\)")
GH_REPO   = re.compile(r"https://github\.com/([^/]+/[^/]+)")

# ───────────── GitHub helper with simple cache ────────────────────
_cache: dict[str, str] = {}               # owner/repo → MM/YYYY

def last_commit_mm_yyyy(repo: str) -> str:
    if repo in _cache:
        return _cache[repo]
    url = f"https://api.github.com/repos/{repo}/commits"
    try:
        resp = requests.get(
            url,
            params={"per_page": 1},
            headers=AUTH_HEADER,
            timeout=TIMEOUT_S
        )
        # print(repo, resp.status_code, resp.text[:120])
        resp.raise_for_status()
        iso = resp.json()[0]["commit"]["committer"]["date"]
        dt  = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        _cache[repo] = dt.strftime("%m/%Y")
    except Exception as e:
        print(f"{repo}: {e}")
        _cache[repo] = "error"
    return _cache[repo]

# ───────────── row‑processing logic ────────────────────────────────
def refresh_row(line: str) -> str:
    """If first link is GitHub, replace final cell (|  MM/YYYY  |)."""
    if not line.lstrip().startswith("|"):
        return line              # not a table row
    m = LINK_RE.search(line)
    if not m:
        return line              # row without a link
    url = m.group(2)
    gh = GH_REPO.match(url)
    if not gh:
        return line              # link isn't GitHub

    repo = gh.group(1)
    # strip extra path segments (e.g. .../tree/main) if any
    owner_repo = "/".join(repo.split("/")[:2]).removesuffix(".git")
    new_date   = last_commit_mm_yyyy(owner_repo)
    # ─── DEBUG ──────────────────────────────────────────────
    before = line
    # ────────────────────────────────────────────────────────

    line = re.sub(r"\|\s*\d{2}/\d{4}\s*\|$", f"| {new_date} |", line)

    # # ─── DEBUG ──────────────────────────────────────────────
    # if before == line:
    #     print(f"[REGEX] no match on → {before.strip()}")
    # # ────────────────────────────────────────────────────────

    return line

# ───────────── main pass ───────────────────────────────────────────
def main() -> None:
    lines = MARKDOWN_FILE.read_text().splitlines()
    lines = [refresh_row(l) for l in lines]
    MARKDOWN_FILE.write_text("\n".join(lines))
    print("All GitHub‑linked table rows updated.")

if __name__ == "__main__":
    main()
