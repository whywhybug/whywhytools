#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(git -C "${SCRIPT_DIR}" rev-parse --show-toplevel 2>/dev/null || echo "")"

if [[ -z "${PROJECT_ROOT}" ]]; then
    echo "Error: unable to determine the project root." >&2
    exit 1
fi

# Run pytest on the tests directory using an absolute path, forwarding any additional arguments
uv run pytest "${PROJECT_ROOT}/tests" "$@"

