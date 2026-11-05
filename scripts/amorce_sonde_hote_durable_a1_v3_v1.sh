#!/usr/bin/env bash
# Amorce de la sonde de l'hôte durable d'A1-v3 (GO-2026-11-04-09, GO de la machine), v1 : course factice, sans clé d'Argon ni relais. Lancée
# par le script de démarrage écrit par `src/controle_ia/sonde_hote_durable_a1_v3.py louer`, qui a cloné le dépôt privé au commit
# COMMIT_PRIVE dans /root/amorce-depot. Mêmes installations que l'amorce de la course (git, numpy au numéro exact,
# /usr/bin/python3), chronométrées, puis exec de la partie « hote » de la sonde. Une reprise du conteneur ne relance rien.
# Variables (jamais affichées) : COMMIT_PRIVE GO_ID PRIX_H_USD DUREE_MAX_S DEPOT_URL GH_TOKEN ; posées par Vast : CONTAINER_ID
# CONTAINER_API_KEY. Essai local : RACINE_AMORCE (défaut /root), SAUTER_INSTALLATION=1.
set -uo pipefail
RACINE_AMORCE="${RACINE_AMORCE:-/root}"
echo "AMORCE SONDE $(date -u +%FT%TZ) : machine ${CONTAINER_ID:-?} ; GO ${GO_ID:-?}"
for v in COMMIT_PRIVE GO_ID PRIX_H_USD DUREE_MAX_S GH_TOKEN; do
    [ -n "${!v:-}" ] || { echo "AMORCE SONDE : variable $v absente : rien ne part"; exit 2; }
done
for v in $(compgen -e); do
    case "$v" in CLE_ARGON|GEMINI*|ANTHROPIC*|OPENAI*|MOONSHOT*|KIMI*)
        [ -n "${!v:-}" ] && { echo "AMORCE SONDE : variable de clé de modèle $v présente : rien ne part"; exit 2; } ;;
    esac
done
[ "$GO_ID" = "GO-2026-11-04-09" ] || { echo "AMORCE SONDE : GO $GO_ID au lieu de GO-2026-11-04-09"; exit 2; }
M="$RACINE_AMORCE/amorce-depot/src/controle_ia/sonde_hote_durable_a1_v3.py"
[ -f "$M" ] || { echo "AMORCE SONDE : module absent du commit $COMMIT_PRIVE"; exit 2; }
if [ "${SAUTER_INSTALLATION:-0}" != "1" ] && [ ! -e "$RACINE_AMORCE/sonde-a1-v3-v1/ETAT" ]; then
    export DEBIAN_FRONTEND=noninteractive
    t0=$(date +%s)
    command -v git >/dev/null || { apt-get update -qq && apt-get install -y -qq git ca-certificates >/dev/null; } \
        || { echo "AMORCE SONDE : installation de git impossible"; exit 2; }
    python3 -c 'import numpy' 2>/dev/null || python3 -m pip install -q --no-cache-dir "numpy==2.5.3" \
        || { echo "AMORCE SONDE : installation de numpy impossible"; exit 2; }
    [ -x /usr/bin/python3 ] || ln -s "$(command -v python3)" /usr/bin/python3
    echo "AMORCE SONDE $(date -u +%FT%TZ) : installations en $(( $(date +%s) - t0 )) s ; $(python3 --version 2>&1)"
fi
exec python3 -I -B "$M" hote
