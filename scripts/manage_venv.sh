#!/usr/bin/env bash
set -euo pipefail

PYTHON_BIN=${PYTHON_BIN:-python3}
VENV_DIR=${VENV_DIR:-.venv}
REQ_FILE=${REQ_FILE:-requirements.txt}

if [ ! -d "$VENV_DIR" ]; then
    echo "[venv] Creating virtual environment at $VENV_DIR"
    "$PYTHON_BIN" -m venv "$VENV_DIR"
else
    echo "[venv] Reusing existing environment at $VENV_DIR"
fi

# shellcheck disable=SC1090
source "$VENV_DIR/bin/activate"

python -m pip install --upgrade pip
if [ -f "$REQ_FILE" ]; then
    pip install -r "$REQ_FILE"
else
    echo "[venv] WARNING: requirements file '$REQ_FILE' not found; skipping package install" >&2
fi

echo "[venv] Environment activated. Run 'deactivate' when you're done."
