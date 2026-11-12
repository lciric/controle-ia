#!/bin/bash
# Tour du collisionneur « règle de repli de G0 » (GO-2026-10-29-07, plafond 15 USD), étage III seul.
# Appel de contrôle (trois espèces) puis tour. Clés passées par variable sous env -i (RR_ANTHROPIC_API_KEY_3 sans en-tête
# d'espace de travail, GEMINI_API_KEY_2) ; jamais en argument ni en fichier. Un refus arrête le tour (code 2) ; rien n'est relancé.
set -uo pipefail; set +x
cd "$(dirname "$0")"
[ -n "${RR_ANTHROPIC_API_KEY_3:-}" ] || { echo "RR_ANTHROPIC_API_KEY_3 absente" >&2; exit 2; }
[ -n "${GEMINI_API_KEY_2:-}" ] || { echo "GEMINI_API_KEY_2 absente" >&2; exit 2; }
[ ! -e run-repli-g0-e3-v1 ] || { echo "run-repli-g0-e3-v1 existe déjà (R12)" >&2; exit 2; }
sha256sum -c question-repli-g0-v1.md.sha256 faits-repli-g0-v1.md.sha256 collisionneur_v2.py.sha256 appel_controle_v6.py.sha256 >/dev/null || { echo "empreintes non conformes" >&2; exit 2; }
ENVI=(env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 GO_ID=GO-2026-10-29-07
  HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}"
  SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}"
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_3" GEMINI_API_KEY="$GEMINI_API_KEY_2")
PY=../../collisionneur-priorites/venv/bin/python
"${ENVI[@]}" timeout 300 $PY -I -B appel_controle_v6.py collisionneur_v2.py controle-repli-g0-v1.json GO-2026-10-29-07 || { echo "appel de contrôle en échec" >&2; exit 2; }
grep -q '"ECHEC"' controle-repli-g0-v1.json && { echo "une espèce en échec au contrôle" >&2; exit 2; }
exec "${ENVI[@]}" timeout 10800 $PY -I -B collisionneur_v2.py etage3 \
    --sortie run-repli-g0-e3-v1 --faits faits-repli-g0-v1.md \
    --question question-repli-g0-v1.md --plafond-usd 15
