#!/usr/bin/env bash
set -euo pipefail

# locate repo root (one level up from this script)
BASE_DIR="$(cd "$(dirname "$0")"/.. && pwd)"
DOCS_DIR="$BASE_DIR/docs"
STOPWORDS="$BASE_DIR/tools/stopwords.txt"
OUT_FILE="$BASE_DIR/word_counts.txt"

# grab all markdown files under docs, concatenate, normalize, filter, count,
# then tee to both stdout and the output file
find "$DOCS_DIR" -type f -name "*.md" \
  -exec cat {} + \
  | tr '[:upper:]' '[:lower:]' \
  | tr -c '[:alpha:]' '[\n*]' \
  | grep -vE '^[[:space:]]*$' \
  | grep -vF -f "$STOPWORDS" \
  | sort \
  | uniq -c \
  | sort -rn \
  | tee "$OUT_FILE"

echo "Word counts also saved to $OUT_FILE"
