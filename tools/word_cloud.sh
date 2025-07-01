#!/usr/bin/env bash
set -euo pipefail

# repo root (one level up from this script)
BASE_DIR="$(cd "$(dirname "$0")"/.. && pwd)"
STOPWORDS="$BASE_DIR/tools/stopwords.txt"
OUT="$BASE_DIR/word_counts.txt"

# sanity check
[[ -f $STOPWORDS ]] || { echo "Error: stopwords file not found at $STOPWORDS" >&2; exit 1; }

# cat every .md under the repo, extract alnum tokens ≥2 chars, lowercase,
# drop pure-numbers, strip exact stopwords, then count & sort
find "$BASE_DIR" -type f -name '*.md' -print0 \
  | xargs -0 cat \
  | grep -Eo '[[:alnum:]]{2,}' \
  | tr '[:upper:]' '[:lower:]' \
  | grep -vE '^[0-9]+$' \
  | grep -v -xF -f "$STOPWORDS" \
  | sort \
  | uniq -c \
  | sort -rn \
  | tee "$OUT"

echo "Word counts streamed to stdout and saved to $OUT"
