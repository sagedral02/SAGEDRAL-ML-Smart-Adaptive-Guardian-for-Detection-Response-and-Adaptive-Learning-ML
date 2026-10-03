#!/bin/bash
# ==============================================================================
# SAGEDRAL-ML Root Installer Entry Point
# ==============================================================================
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec bash "${SCRIPT_DIR}/scripts/install.sh" "$@"
