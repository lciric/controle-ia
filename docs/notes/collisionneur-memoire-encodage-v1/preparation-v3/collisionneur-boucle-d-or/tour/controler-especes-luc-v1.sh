#!/usr/bin/env bash
# Appel de contrôle des trois espèces avant un tour ; $1 = GO, $2 = sortie neuve (R12). Clé Anthropic : RR_ANTHROPIC_API_KEY_LUC (mot de Lazar, R-547), sans en-tête d'espace de travail. Clés par variable, jamais affichées.
set -uo pipefail; set +x
[ -n "${RR_ANTHROPIC_API_KEY_LUC:-}" ] || { echo "RR_ANTHROPIC_API_KEY_LUC absente de cette session : rien n'est lancé (une session neuve, ou un processus redémarré, la lit)" >&2; exit 2; }
cd "$(dirname "$0")"
[ $# -eq 2 ] || { echo "usage : controler-especes-luc-v1.sh GO SORTIE" >&2; exit 2; }
[ ! -e "$2" ] || { echo "$2 existe déjà (R12)" >&2; exit 2; }
exec env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 \
  HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" \
  SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_LUC" GEMINI_API_KEY="$GEMINI_API_KEY" \
  ../venv/bin/python -I -B appel_controle_v5.py collisionneur_v2.py "$2" "$1"
