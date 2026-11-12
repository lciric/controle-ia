#!/usr/bin/env bash
# Étage III standard du collisionneur v2.6 — « mémoire du pôle : encodage et redites », question v3 de conv-audit, faits v2
# (J2 ajoutée), GO-2026-10-27-01 (extensions, R-543, R-544 : plafond 35 USD) ; un refus arrête le tour. Clé Anthropic : RR_ANTHROPIC_API_KEY_LUC (mot de Lazar, R-547), sans en-tête d'espace de travail. Clés par variable, jamais affichées.
set -uo pipefail; set +x
[ -n "${RR_ANTHROPIC_API_KEY_LUC:-}" ] || { echo "RR_ANTHROPIC_API_KEY_LUC absente de cette session : rien n'est lancé (une session neuve, ou un processus redémarré, la lit)" >&2; exit 2; }
cd "$(dirname "$0")"
[ ! -e run-memoire-encodage-v3-e3-v1 ] || { echo "run-memoire-encodage-v3-e3-v1 existe déjà (R12)" >&2; exit 2; }
exec env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 \
  HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" \
  SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_LUC" GEMINI_API_KEY="$GEMINI_API_KEY" \
  ../venv/bin/python -I -B collisionneur_v2.py etage3 \
    --sortie run-memoire-encodage-v3-e3-v1 --faits faits-memoire-encodage-v2.md \
    --question question-memoire-encodage-v3.md --plafond-usd 35
