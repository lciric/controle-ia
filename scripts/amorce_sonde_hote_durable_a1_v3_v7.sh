#!/usr/bin/env bash
# Amorce de la sonde v7 de l'hôte durable d'A1-v3 (GO-2026-11-04-09, GO de la machine), copie de la v3 sous un nom neuf
# (R12 ; contre-lectures `contre-lecture-sonde-v1.md` à `contre-lecture-sonde-v3.md` ; v4 : chaque `apt-get` sous `timeout`, m-2 ;
# l'amorce entière tourne sous un `timeout` borné par la fin de vie, posé par le script de démarrage). Lancée par le script de démarrage du
# conteneur APRÈS la minuterie de destruction : quel que soit le code de sortie de cette amorce, la minuterie détruit la machine à
# l'échéance (minimum de l'échéance absolue du pilote et de départ + durée + marge), et le conteneur reste en vie jusque-là.
# m-c : `curl` exigé (la minuterie s'en sert) ; absent, rien ne part, refus visible au journal.
# v5 : mémoire réelle relevée (/proc/meminfo, MemTotal) dans sonde-v7-memoire.txt, versé ; sous 2 Go, rien ne part (la minuterie
# détruit) ; essai local : SONDE_MEMINFO (chemin absolu d'un faux meminfo).
# Course factice, sans clé d'Argon ni relais.
# Variables (jamais affichées) : COMMIT_PRIVE GO_ID PRIX_H_USD DUREE_MAX_S ECHEANCE_UTC_S TIR_MINUTERIE DEPOT_URL GH_TOKEN ;
# posées par Vast : CONTAINER_ID CONTAINER_API_KEY. Essai local : RACINE_AMORCE (défaut /root), SAUTER_INSTALLATION=1.
set -uo pipefail
RACINE_AMORCE="${RACINE_AMORCE:-/root}"
echo "AMORCE SONDE V7 $(date -u +%FT%TZ) : machine ${CONTAINER_ID:-?} ; GO ${GO_ID:-?}"
for v in COMMIT_PRIVE GO_ID PRIX_H_USD DUREE_MAX_S ECHEANCE_UTC_S GH_TOKEN; do
    [ -n "${!v:-}" ] || { echo "AMORCE SONDE V7 : variable $v absente : rien ne part (la minuterie détruira)"; exit 2; }
done
# f2 : même liste que `CLES_INTERDITES` du module v7 (MOTIF_AMORCE)
for v in $(compgen -e); do
    case "$v" in CLE_ARGON|GEMINI*|ANTHROPIC*|OPENAI*|MOONSHOT*|KIMI*|RR_*API_KEY*)
        [ -n "${!v:-}" ] && { echo "AMORCE SONDE V7 : variable de clé de modèle $v présente : rien ne part"; exit 2; } ;;
    esac
done
[ "$GO_ID" = "GO-2026-11-04-09" ] || { echo "AMORCE SONDE V7 : GO $GO_ID au lieu de GO-2026-11-04-09"; exit 2; }
command -v curl >/dev/null 2>&1 || { echo "AMORCE SONDE V7 : curl absent : rien ne part (la minuterie passe par python3)"; exit 2; }
case "$ECHEANCE_UTC_S" in ''|*[!0-9]*) echo "AMORCE SONDE V7 : ECHEANCE_UTC_S non entière : rien ne part"; exit 2;; esac
case "$DUREE_MAX_S" in ''|*[!0-9]*) echo "AMORCE SONDE V7 : DUREE_MAX_S non entière : rien ne part"; exit 2;; esac
MEMINFO="${SONDE_MEMINFO:-/proc/meminfo}"; case "$MEMINFO" in /*) ;; *) MEMINFO=/proc/meminfo;; esac
MEM_KB=$(grep -m1 '^MemTotal:' "$MEMINFO" 2>/dev/null | tr -s ' ' | cut -d' ' -f2)
echo "$(date -u +%FT%TZ) MemTotal ${MEM_KB:-illisible} kB" >> "$RACINE_AMORCE/sonde-v7-memoire.txt"
case "$MEM_KB" in ''|*[!0-9]*) echo "AMORCE SONDE V7 : mémoire réelle illisible : rien ne part (la minuterie détruit)"; exit 2;; esac
[ "$MEM_KB" -ge 2097152 ] || { echo "AMORCE SONDE V7 : mémoire réelle $MEM_KB kB < 2 Go : rien ne part (la minuterie détruit)"; exit 2; }
echo "AMORCE SONDE V7 : mémoire réelle $MEM_KB kB (MemTotal)"
M="$RACINE_AMORCE/amorce-depot/src/controle_ia/sonde_hote_durable_a1_v3_v7.py"
for f in "$M" "$RACINE_AMORCE/amorce-depot/src/controle_ia/sonde_hote_durable_a1_v3.py" \
         "$RACINE_AMORCE/amorce-depot/src/controle_ia/hote_durable_a1_v3.py"; do
    [ -f "$f" ] || { echo "AMORCE SONDE V7 : $(basename "$f") absent du commit $COMMIT_PRIVE"; exit 2; }
done
if [ "${SAUTER_INSTALLATION:-0}" != "1" ] && [ ! -e "$RACINE_AMORCE/sonde-a1-v3-v7/ETAT" ]; then
    export DEBIAN_FRONTEND=noninteractive
    t0=$(date +%s)
    command -v git >/dev/null || timeout -k 5 120 sh -c 'apt-get update -qq && apt-get install -y -qq git ca-certificates >/dev/null' \
        || { echo "AMORCE SONDE V7 : installation de git impossible"; exit 2; }
    # mesure pour la vraie course (la sonde n'a pas besoin de numpy) : un échec est écrit, jamais un arrêt
    python3 -c 'import numpy' 2>/dev/null || timeout 600 python3 -m pip install -q --no-cache-dir "numpy==2.5.3" \
        || echo "AMORCE SONDE V7 : MESURE : installation de numpy==2.5.3 impossible (la course devra le régler)"
    [ -x /usr/bin/python3 ] || ln -s "$(command -v python3)" /usr/bin/python3
    echo "AMORCE SONDE V7 $(date -u +%FT%TZ) : installations en $(( $(date +%s) - t0 )) s ; $(python3 --version 2>&1) ;" \
         "numpy $(python3 -c 'import numpy; print(numpy.__version__)' 2>/dev/null || echo absent)"
fi
exec python3 -I -B "$M" hote
