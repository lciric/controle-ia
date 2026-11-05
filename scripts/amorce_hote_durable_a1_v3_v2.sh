#!/usr/bin/env bash
# Amorce de l'hôte durable de la troisième course d'A1-v3, v2 (machine : GO-2026-11-05-03, une carte ; course :
# GO-2026-11-04-06). Nom neuf (R12 : l'amorce v1 est inchangée). Lancée par le script de démarrage du conteneur
# (`script_de_demarrage` de `src/controle_ia/hote_durable_a1_v3_v2.py`) APRÈS la minuterie de destruction, sous un `timeout` borné
# par la fin de vie (m-2). Un refus de cette amorce (code 2) fait demander au script de démarrage la destruction immédiate par la
# minuterie (rien n'a tourné) ; tout autre code laisse la minuterie à son échéance.
# Contrôles (cas sain et artefact éprouvés, R5) : variables présentes ; aucune clé de modèle autre que CLE_ARGON (même liste que
# `CLES_INTERDITES` du module, f2) ; GO_ID = GO-2026-11-04-06 et GO_MACHINE = GO-2026-11-05-03 (v9 b) ; curl présent (m-c) ;
# ECHEANCE_UTC_S entière ; mémoire réelle relevée (/proc/meminfo, MemTotal) dans a1v3-memoire.txt, versé, et au moins 2 Go (v5 b) ;
# modules présents ; git et numpy==2.5.3 installés sous `timeout` (m-2) ; /usr/bin/python3 (chemin écrit dans la configuration
# gelée) ; puis `exec` de la partie « hote » du module (aucune ligne de ce fichier n'est relue après le départ).
# Variables (corps de création, jamais affichées) : COMMIT_PRIVE COMMIT_PUBLIC SHA_TEXTE COMMIT_REGISTRE GO_ID GO_MACHINE
# PRIX_H_USD ECHEANCE_UTC_S DEPOT_URL CLE_ARGON GH_TOKEN ; posées par Vast : CONTAINER_ID CONTAINER_API_KEY.
# Essai local : RACINE_AMORCE (défaut /root), SAUTER_INSTALLATION=1 (aucune installation, aucun réseau), A1V3_MEMINFO (chemin
# absolu d'un faux meminfo).
set -uo pipefail
RACINE_AMORCE="${RACINE_AMORCE:-/root}"
echo "AMORCE A1-V3 V2 $(date -u +%FT%TZ) : machine ${CONTAINER_ID:-?} ; GO de la course ${GO_ID:-?} ; GO de la machine ${GO_MACHINE:-?}"
for v in COMMIT_PRIVE COMMIT_PUBLIC SHA_TEXTE COMMIT_REGISTRE GO_ID GO_MACHINE PRIX_H_USD ECHEANCE_UTC_S CLE_ARGON GH_TOKEN; do
    [ -n "${!v:-}" ] || { echo "AMORCE A1-V3 V2 : variable $v absente : rien ne part"; exit 2; }
done
for v in $(compgen -e); do  # f2 : MOTIF_AMORCE du module (CLE_ARGON permise, la seule)
    case "$v" in GEMINI*|ANTHROPIC*|OPENAI*|MOONSHOT*|KIMI*|RR_*API_KEY*)
        [ -n "${!v:-}" ] && { echo "AMORCE A1-V3 V2 : variable de clé de modèle $v présente : rien ne part"; exit 2; } ;;
    esac
done
[ "$GO_ID" = "GO-2026-11-04-06" ] || { echo "AMORCE A1-V3 V2 : GO de la course $GO_ID au lieu de GO-2026-11-04-06"; exit 2; }
[ "$GO_MACHINE" = "GO-2026-11-05-03" ] || { echo "AMORCE A1-V3 V2 : GO de la machine $GO_MACHINE au lieu de GO-2026-11-05-03"; exit 2; }
command -v curl >/dev/null 2>&1 || { echo "AMORCE A1-V3 V2 : curl absent : rien ne part (la minuterie passe par python3)"; exit 2; }
case "$ECHEANCE_UTC_S" in ''|*[!0-9]*) echo "AMORCE A1-V3 V2 : ECHEANCE_UTC_S non entière : rien ne part"; exit 2;; esac
MEMINFO="${A1V3_MEMINFO:-/proc/meminfo}"; case "$MEMINFO" in /*) ;; *) MEMINFO=/proc/meminfo;; esac
MEM_KB=$(grep -m1 '^MemTotal:' "$MEMINFO" 2>/dev/null | tr -s ' ' | cut -d' ' -f2)
echo "$(date -u +%FT%TZ) MemTotal ${MEM_KB:-illisible} kB" >> "$RACINE_AMORCE/a1v3-memoire.txt"
case "$MEM_KB" in ''|*[!0-9]*) echo "AMORCE A1-V3 V2 : mémoire réelle illisible : rien ne part"; exit 2;; esac
[ "$MEM_KB" -ge 2097152 ] || { echo "AMORCE A1-V3 V2 : mémoire réelle $MEM_KB kB < 2 Go : rien ne part"; exit 2; }
echo "AMORCE A1-V3 V2 : mémoire réelle $MEM_KB kB (MemTotal)"
D="$RACINE_AMORCE/amorce-depot/src/controle_ia"
for f in hote_durable_a1_v3.py hote_durable_a1_v3_v2.py sonde_hote_durable_a1_v3.py sonde_hote_durable_a1_v3_v10.py; do
    [ -f "$D/$f" ] || { echo "AMORCE A1-V3 V2 : $f absent du commit $COMMIT_PRIVE : rien ne part"; exit 2; }
done
if [ "${SAUTER_INSTALLATION:-0}" != "1" ] && [ ! -e "$RACINE_AMORCE/a1-v3-troisieme-v1/ETAT" ]; then
    export DEBIAN_FRONTEND=noninteractive
    t0=$(date +%s)
    command -v git >/dev/null || timeout -k 5 300 sh -c 'apt-get update -qq && apt-get install -y -qq git ca-certificates >/dev/null' \
        || { echo "AMORCE A1-V3 V2 : installation de git impossible : rien ne part"; exit 2; }
    python3 -c 'import numpy' 2>/dev/null || timeout -k 5 600 python3 -m pip install -q --no-cache-dir "numpy==2.5.3" \
        || { echo "AMORCE A1-V3 V2 : installation de numpy==2.5.3 impossible : rien ne part"; exit 2; }
    [ -x /usr/bin/python3 ] || ln -s "$(command -v python3)" /usr/bin/python3
    echo "AMORCE A1-V3 V2 $(date -u +%FT%TZ) : installations en $(( $(date +%s) - t0 )) s ; $(python3 --version 2>&1) ;" \
         "numpy $(python3 -c 'import numpy; print(numpy.__version__)' 2>/dev/null || echo absent)"
fi
exec python3 -I -B "$D/hote_durable_a1_v3_v2.py" hote
