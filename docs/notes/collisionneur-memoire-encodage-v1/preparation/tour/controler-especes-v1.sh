#!/usr/bin/env bash
# Appel de contrôle des trois espèces (un appel court chacune) avant le tour « mémoire du pôle », GO-2026-10-27-01 ;
# clés par variable, jamais affichées.
set -uo pipefail; set +x
cd "$(dirname "$0")"
[ ! -e appel-controle-especes-v2.json ] || { echo "appel-controle-especes-v2.json existe déjà (R12)" >&2; exit 2; }
exec env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 \
  HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" \
  SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY" ANTHROPIC_WORKSPACE_ID="$RR_ANTHROPIC_WORKSPACE_ID" GEMINI_API_KEY="$GEMINI_API_KEY" \
  ../venv/bin/python -I -B appel_controle_v5.py collisionneur_v2.py appel-controle-especes-v2.json GO-2026-10-27-01
