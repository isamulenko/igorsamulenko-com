#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

python3 -m unittest discover -s tests

tmpdir="$(mktemp -d)"
trap 'rm -rf "$tmpdir"' EXIT

python3 minify.py index.html "$tmpdir/index.html" >/dev/null

if ! cmp -s "$tmpdir/index.html" s3/index.html; then
  echo "verify: s3/index.html is out of date. Run python3 minify.py." >&2
  exit 1
fi

required_files=(
  "index.html"
  "s3/index.html"
  "images/avatar.jpeg"
  "s3/images/avatar.jpeg"
  "Igor_Samulenko_Staff_SWE_2026.pdf"
  "s3/Igor_Samulenko_Staff_SWE_2026.pdf"
)

for file in "${required_files[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "verify: missing required file: $file" >&2
    exit 1
  fi
done

if git ls-files | grep -Eq '(^|/)\.DS_Store$'; then
  echo "verify: .DS_Store must not be tracked" >&2
  exit 1
fi

echo "verify: OK"
