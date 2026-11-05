#!/usr/bin/env bash
# Amorce de l'hôte durable de la troisième course d'A1-v3, v3 (machine : GO-2026-11-05-03, une carte ; course :
# GO-2026-11-04-06). Nom neuf (R12 : amorces v1 et v2 inchangées). v3 = v2 + C1 : l'interpréteur de l'image
# (`/usr/local/bin/python3`) doit être Python 3.13 ; `/usr/bin/python3` (chemin écrit dans la configuration gelée ; Debian y
# met 3.11.2 sur `python:3.13-bookworm`, sonde v10) devient un lien vers lui ; les deux versions, avant et après, au journal ;
# sinon, rien ne part (code 2 : destruction immédiate par la minuterie). Essai local : A1V3_PYTHON_IMAGE et
# A1V3_PYTHON_CONFIGURATION (chemins absolus). Lancée par le script de démarrage du conteneur
# (`script_de_demarrage` de `src/controle_ia/hote_durable_a1_v3_v3.py`) APRÈS la minuterie de destruction, sous un `timeout` borné
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
echo "AMORCE A1-V3 V3 $(date -u +%FT%TZ) : machine ${CONTAINER_ID:-?} ; GO de la course ${GO_ID:-?} ; GO de la machine ${GO_MACHINE:-?}"
for v in COMMIT_PRIVE COMMIT_PUBLIC SHA_TEXTE COMMIT_REGISTRE GO_ID GO_MACHINE PRIX_H_USD ECHEANCE_UTC_S CLE_ARGON GH_TOKEN; do
    [ -n "${!v:-}" ] || { echo "AMORCE A1-V3 V3 : variable $v absente : rien ne part"; exit 2; }
done
for v in $(compgen -e); do  # f2 : MOTIF_AMORCE du module (CLE_ARGON permise, la seule)
    case "$v" in GEMINI*|ANTHROPIC*|OPENAI*|MOONSHOT*|KIMI*|RR_*API_KEY*)
        [ -n "${!v:-}" ] && { echo "AMORCE A1-V3 V3 : variable de clé de modèle $v présente : rien ne part"; exit 2; } ;;
    esac
done
[ "$GO_ID" = "GO-2026-11-04-06" ] || { echo "AMORCE A1-V3 V3 : GO de la course $GO_ID au lieu de GO-2026-11-04-06"; exit 2; }
[ "$GO_MACHINE" = "GO-2026-11-05-03" ] || { echo "AMORCE A1-V3 V3 : GO de la machine $GO_MACHINE au lieu de GO-2026-11-05-03"; exit 2; }
command -v curl >/dev/null 2>&1 || { echo "AMORCE A1-V3 V3 : curl absent : rien ne part (la minuterie passe par python3)"; exit 2; }
case "$ECHEANCE_UTC_S" in ''|*[!0-9]*) echo "AMORCE A1-V3 V3 : ECHEANCE_UTC_S non entière : rien ne part"; exit 2;; esac
MEMINFO="${A1V3_MEMINFO:-/proc/meminfo}"; case "$MEMINFO" in /*) ;; *) MEMINFO=/proc/meminfo;; esac
MEM_KB=$(grep -m1 '^MemTotal:' "$MEMINFO" 2>/dev/null | tr -s ' ' | cut -d' ' -f2)
echo "$(date -u +%FT%TZ) MemTotal ${MEM_KB:-illisible} kB" >> "$RACINE_AMORCE/a1v3-memoire.txt"
case "$MEM_KB" in ''|*[!0-9]*) echo "AMORCE A1-V3 V3 : mémoire réelle illisible : rien ne part"; exit 2;; esac
[ "$MEM_KB" -ge 2097152 ] || { echo "AMORCE A1-V3 V3 : mémoire réelle $MEM_KB kB < 2 Go : rien ne part"; exit 2; }
echo "AMORCE A1-V3 V3 : mémoire réelle $MEM_KB kB (MemTotal)"
D="$RACINE_AMORCE/amorce-depot/src/controle_ia"
for f in hote_durable_a1_v3.py hote_durable_a1_v3_v3.py sonde_hote_durable_a1_v3.py sonde_hote_durable_a1_v3_v10.py; do
    [ -f "$D/$f" ] || { echo "AMORCE A1-V3 V3 : $f absent du commit $COMMIT_PRIVE : rien ne part"; exit 2; }
done
PY_IMAGE="${A1V3_PYTHON_IMAGE:-/usr/local/bin/python3}"; case "$PY_IMAGE" in /*) ;; *) PY_IMAGE=/usr/local/bin/python3;; esac
PY_CONF="${A1V3_PYTHON_CONFIGURATION:-/usr/bin/python3}"; case "$PY_CONF" in /*) ;; *) PY_CONF=/usr/bin/python3;; esac
version() { "$1" -c 'import sys; print("%d.%d" % sys.version_info[:2])' 2>/dev/null; }
complete() { "$1" --version 2>&1 | head -1; }
echo "AMORCE A1-V3 V3 : interpréteurs avant (C1) : $PY_IMAGE $(complete "$PY_IMAGE") ; $PY_CONF $(complete "$PY_CONF")"
[ "$(version "$PY_IMAGE")" = "3.13" ] || { echo "AMORCE A1-V3 V3 : $PY_IMAGE n'est pas Python 3.13 (C1) : rien ne part"; exit 2; }
if [ "${SAUTER_INSTALLATION:-0}" != "1" ] && [ ! -e "$RACINE_AMORCE/a1-v3-troisieme-v1/ETAT" ]; then
    export DEBIAN_FRONTEND=noninteractive
    t0=$(date +%s)
    command -v git >/dev/null || timeout -k 5 300 sh -c 'apt-get update -qq && apt-get install -y -qq git ca-certificates >/dev/null' \
        || { echo "AMORCE A1-V3 V3 : installation de git impossible : rien ne part"; exit 2; }
    "$PY_IMAGE" -c 'import numpy' 2>/dev/null || timeout -k 5 600 "$PY_IMAGE" -m pip install -q --no-cache-dir "numpy==2.5.3" \
        || { echo "AMORCE A1-V3 V3 : installation de numpy==2.5.3 impossible : rien ne part"; exit 2; }
    echo "AMORCE A1-V3 V3 $(date -u +%FT%TZ) : installations en $(( $(date +%s) - t0 )) s ; $(complete "$PY_IMAGE") ;" \
         "numpy $("$PY_IMAGE" -c 'import numpy; print(numpy.__version__)' 2>/dev/null || echo absent)"
fi
# C1 : le chemin de la configuration gelée devient un lien vers l'interpréteur de l'image, s'il n'est pas déjà 3.13
if [ "$(version "$PY_CONF")" != "3.13" ]; then
    ln -sfn "$PY_IMAGE" "$PY_CONF" 2>/dev/null || { echo "AMORCE A1-V3 V3 : lien $PY_CONF -> $PY_IMAGE impossible (C1) : rien ne part"; exit 2; }
fi
[ "$(version "$PY_CONF")" = "3.13" ] || { echo "AMORCE A1-V3 V3 : $PY_CONF n'est pas Python 3.13 (C1) : rien ne part"; exit 2; }
echo "AMORCE A1-V3 V3 : interpréteurs après (C1) : $PY_IMAGE $(complete "$PY_IMAGE") ; $PY_CONF -> $(readlink -f "$PY_CONF") $(complete "$PY_CONF")"
exec "$PY_IMAGE" -I -B "$D/hote_durable_a1_v3_v3.py" hote
