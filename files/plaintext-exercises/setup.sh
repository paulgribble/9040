#!/usr/bin/env bash
# setup.sh — Download the APA 7th edition CSL file for citation formatting
# Run this once before the exercises.

set -e

CSL_URL="https://raw.githubusercontent.com/citation-style-language/styles/master/apa.csl"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Downloading APA 7th edition citation style..."

if command -v curl &>/dev/null; then
  curl -sL "$CSL_URL" -o "$SCRIPT_DIR/apa.csl"
elif command -v wget &>/dev/null; then
  wget -q "$CSL_URL" -O "$SCRIPT_DIR/apa.csl"
else
  echo "Error: Neither curl nor wget found. Please install one of them."
  exit 1
fi

if [ ! -s "$SCRIPT_DIR/apa.csl" ]; then
  echo "Error: Download failed. Please download manually from:"
  echo "  https://www.zotero.org/styles/apa"
  echo "Save as apa.csl in each exercise folder."
  exit 1
fi

echo "Copying apa.csl into exercise folders..."
for dir in exercise1 exercise2 exercise3; do
  if [ -d "$SCRIPT_DIR/$dir" ]; then
    cp "$SCRIPT_DIR/apa.csl" "$SCRIPT_DIR/$dir/apa.csl"
    echo "  → $dir/apa.csl"
  fi
done

echo ""
echo "Done! You're ready for the exercises."
echo ""
