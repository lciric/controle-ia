#!/usr/bin/env bash
# Étage III standard du collisionneur v2.6 — « mémoire du pôle : encodage et redites » (question v2 de conv-audit),
# GO-2026-10-27-01 (R-539) ; un refus arrête le tour. Clés par variable, jamais affichées.
set -uo pipefail; set +x
cd "$(dirname "$0")"
[ ! -e run-memoire-encodage-e3-v1 ] || { echo "run-memoire-encodage-e3-v1 existe déjà (R12)" >&2; exit 2; }
exec env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 \
  HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" \
  SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY" ANTHROPIC_WORKSPACE_ID="$RR_ANTHROPIC_WORKSPACE_ID" GEMINI_API_KEY="$GEMINI_API_KEY" \
  ../venv/bin/python -I -B collisionneur_v2.py etage3 \
    --sortie run-memoire-encodage-e3-v1 --faits faits-memoire-encodage-v1.md \
    --question question-memoire-encodage-v2.md --plafond-usd 22
