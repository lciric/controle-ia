#!/bin/bash
# Poursuite des tours 2 et 3 du run run-pilote-complement-e3-v1 avec Fable et Argon seuls (GO-2026-10-29-01), sur la décision de l'arbitre (Lazar,
# 2026-10-29 ≈ 00:56 UTC : « (a) go pour les deux ») : absence d'Opus 5.5 acceptée pour ses trois cellules (refus au tour 1,
# consigné, jamais reformulé, R-609). Clés passées par variable sous env -i ; jamais en argument ni en fichier.
set -uo pipefail; set +x
cd "$(dirname "$0")"
[ -n "${RR_ANTHROPIC_API_KEY_3:-}" ] || { echo "RR_ANTHROPIC_API_KEY_3 absente" >&2; exit 2; }
[ -n "${GEMINI_API_KEY_2:-}" ] || { echo "GEMINI_API_KEY_2 absente" >&2; exit 2; }
[ -d run-pilote-complement-e3-v1 ] || { echo "run-pilote-complement-e3-v1 absent" >&2; exit 2; }
sha256sum -c question-pilote-complement-v1.md.sha256 faits-pilote-complement-v1.md.sha256 collisionneur_v2.py.sha256 >/dev/null || { echo "empreintes non conformes" >&2; exit 2; }
exec env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 GO_ID=GO-2026-10-29-01 \
  HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" \
  SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_3" GEMINI_API_KEY="$GEMINI_API_KEY_2" \
  timeout 10800 ../../collisionneur-priorites/venv/bin/python -I -B collisionneur_v2.py etage3 \
    --sortie run-pilote-complement-e3-v1 --faits faits-pilote-complement-v1.md --question question-pilote-complement-v1.md --plafond-usd 30 \
    --accepter-absence E3-T1-conception-B --accepter-absence E3-T2-redteam-B --accepter-absence E3-T3-riposte-B
