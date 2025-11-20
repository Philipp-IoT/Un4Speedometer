#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONFIG_FILE=${CONFIG_FILE:-"$ROOT_DIR/mkdocs.yml"}
DEV_ADDR=${DEV_ADDR:-"127.0.0.1:8000"}

if [ ! -f "$CONFIG_FILE" ]; then
    echo "[mkdocs] Config file not found at $CONFIG_FILE" >&2
    exit 1
fi

if command -v mkdocs >/dev/null 2>&1; then
    MKDOCS_BIN="mkdocs"
elif [ -x "$ROOT_DIR/.venv/bin/mkdocs" ]; then
    MKDOCS_BIN="$ROOT_DIR/.venv/bin/mkdocs"
else
    echo "[mkdocs] mkdocs executable not found. Activate your venv (source scripts/manage_venv.sh) before running this script." >&2
    exit 1
fi

cd "$ROOT_DIR"
"$MKDOCS_BIN" serve --config-file "$CONFIG_FILE" --dev-addr "$DEV_ADDR" "$@"
