#!/usr/bin/env bash
# Amorce de l'hôte durable de la course A1-v4 (attaque de Goodhart contre le nul v9), lanceur durable v5. Nom neuf (R12 :
# amorces v1 à v4 d'A1-v3 inchangées). v5 = amorce v4 (C1 interpréteur 3.13, correction 7 numpy 2.5.3, mémoire ≥ 2 Go, curl,
# clés de modèle refusées sauf CLE_ARGON) avec : GO_ID = GO-2026-11-02-22 (la ligne des appels, constante du lanceur v5) ;
# GO_MACHINE = GO-AAAA-MM-JJ-NN quelconque, différent de GO_ID (AUCUN identifiant de machine en dur : le module le vérifie
# contre registres/go.md de main, plafond et périmètre lus) ; variables neuves NOM_TEXTE, CHEMIN_CONFIGURATION_MONDES,
# SHA_CONFIGURATION_MONDES exigées ; modules de la v4 plus hote_durable_a1_v4_v5.py ; puis `exec` de la partie « hote » du v5.
# Lancée par le script de démarrage du conteneur (`script_de_demarrage` du module v5) APRÈS la minuterie de destruction, sous un
# `timeout` borné par la fin de vie. Un refus (code 2) fait demander la destruction immédiate par la minuterie (rien n'a tourné).
# Variables (corps de création, jamais affichées) : COMMIT_PRIVE COMMIT_PUBLIC SHA_TEXTE NOM_TEXTE COMMIT_REGISTRE GO_ID GO_MACHINE
# CHEMIN_CONFIGURATION_MONDES SHA_CONFIGURATION_MONDES PRIX_H_USD ECHEANCE_UTC_S DEPOT_URL CLE_ARGON GH_TOKEN ; posées par Vast :
# CONTAINER_ID CONTAINER_API_KEY. Essai local : RACINE_AMORCE (défaut /root), SAUTER_INSTALLATION=1, A1V4_MEMINFO,
# A1V4_PYTHON_IMAGE, A1V4_PYTHON_CONFIGURATION (chemins absolus), A1V4_MODULES (dossier des modules, défaut
# $RACINE_AMORCE/amorce-depot/src/controle_ia).
set -uo pipefail
RACINE_AMORCE="${RACINE_AMORCE:-/root}"
echo "AMORCE A1-V4 V5 $(date -u +%FT%TZ) : machine ${CONTAINER_ID:-?} ; GO des appels ${GO_ID:-?} ; GO de la machine ${GO_MACHINE:-?} ; texte ${NOM_TEXTE:-?}"
for v in COMMIT_PRIVE COMMIT_PUBLIC SHA_TEXTE NOM_TEXTE COMMIT_REGISTRE GO_ID GO_MACHINE CHEMIN_CONFIGURATION_MONDES SHA_CONFIGURATION_MONDES PRIX_H_USD ECHEANCE_UTC_S CLE_ARGON GH_TOKEN; do
    [ -n "${!v:-}" ] || { echo "AMORCE A1-V4 V5 : variable $v absente : rien ne part"; exit 2; }
done
for v in $(compgen -e); do  # f2 : MOTIF_AMORCE du module v4 (CLE_ARGON permise, la seule)
    case "$v" in GEMINI*|ANTHROPIC*|OPENAI*|MOONSHOT*|KIMI*|RR_*API_KEY*)
        [ -n "${!v:-}" ] && { echo "AMORCE A1-V4 V5 : variable de clé de modèle $v présente : rien ne part"; exit 2; } ;;
    esac
done
[ "$GO_ID" = "GO-2026-11-02-22" ] || { echo "AMORCE A1-V4 V5 : GO des appels $GO_ID au lieu de GO-2026-11-02-22"; exit 2; }
case "$GO_MACHINE" in GO-[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]-[0-9][0-9]) ;; *) echo "AMORCE A1-V4 V5 : GO de la machine $GO_MACHINE illisible (GO-AAAA-MM-JJ-NN)"; exit 2;; esac
[ "$GO_MACHINE" != "$GO_ID" ] || { echo "AMORCE A1-V4 V5 : GO de la machine égal à la ligne des appels : rien ne part"; exit 2; }
case "$NOM_TEXTE" in orchestrator/prereg/preenregistrement-attaque-goodhart-v[1-9]*-v[1-9]*.md) ;; *) echo "AMORCE A1-V4 V5 : NOM_TEXTE $NOM_TEXTE hors de orchestrator/prereg/preenregistrement-attaque-goodhart-v<V>-v<N>.md"; exit 2;; esac
command -v curl >/dev/null 2>&1 || { echo "AMORCE A1-V4 V5 : curl absent : rien ne part (la minuterie passe par python3)"; exit 2; }
case "$ECHEANCE_UTC_S" in ''|*[!0-9]*) echo "AMORCE A1-V4 V5 : ECHEANCE_UTC_S non entière : rien ne part"; exit 2;; esac
MEMINFO="${A1V4_MEMINFO:-/proc/meminfo}"; case "$MEMINFO" in /*) ;; *) MEMINFO=/proc/meminfo;; esac
MEM_KB=$(grep -m1 '^MemTotal:' "$MEMINFO" 2>/dev/null | tr -s ' ' | cut -d' ' -f2)
echo "$(date -u +%FT%TZ) MemTotal ${MEM_KB:-illisible} kB" >> "$RACINE_AMORCE/a1v4-memoire.txt"
case "$MEM_KB" in ''|*[!0-9]*) echo "AMORCE A1-V4 V5 : mémoire réelle illisible : rien ne part"; exit 2;; esac
[ "$MEM_KB" -ge 2097152 ] || { echo "AMORCE A1-V4 V5 : mémoire réelle $MEM_KB kB < 2 Go : rien ne part"; exit 2; }
echo "AMORCE A1-V4 V5 : mémoire réelle $MEM_KB kB (MemTotal)"
D="${A1V4_MODULES:-$RACINE_AMORCE/amorce-depot/src/controle_ia}"
for f in hote_durable_a1_v3.py hote_durable_a1_v3_v4.py sonde_hote_durable_a1_v3.py sonde_hote_durable_a1_v3_v10.py hote_durable_a1_v4_v5.py; do
    [ -f "$D/$f" ] || { echo "AMORCE A1-V4 V5 : $f absent du commit $COMMIT_PRIVE : rien ne part"; exit 2; }
done
PY_IMAGE="${A1V4_PYTHON_IMAGE:-/usr/local/bin/python3}"; case "$PY_IMAGE" in /*) ;; *) PY_IMAGE=/usr/local/bin/python3;; esac
PY_CONF="${A1V4_PYTHON_CONFIGURATION:-/usr/bin/python3}"; case "$PY_CONF" in /*) ;; *) PY_CONF=/usr/bin/python3;; esac
version() { "$1" -c 'import sys; print("%d.%d" % sys.version_info[:2])' 2>/dev/null; }
complete() { "$1" --version 2>&1 | head -1; }
echo "AMORCE A1-V4 V5 : interpréteurs avant (C1) : $PY_IMAGE $(complete "$PY_IMAGE") ; $PY_CONF $(complete "$PY_CONF")"
[ "$(version "$PY_IMAGE")" = "3.13" ] || { echo "AMORCE A1-V4 V5 : $PY_IMAGE n'est pas Python 3.13 (C1) : rien ne part"; exit 2; }
if [ "${SAUTER_INSTALLATION:-0}" != "1" ] && [ ! -e "$RACINE_AMORCE/a1-v4-reprise-v9-v1/ETAT" ]; then
    export DEBIAN_FRONTEND=noninteractive
    t0=$(date +%s)
    command -v git >/dev/null || timeout -k 5 300 sh -c 'apt-get update -qq && apt-get install -y -qq git ca-certificates >/dev/null' \
        || { echo "AMORCE A1-V4 V5 : installation de git impossible : rien ne part"; exit 2; }
    "$PY_IMAGE" -c 'import numpy' 2>/dev/null || timeout -k 5 600 "$PY_IMAGE" -m pip install -q --no-cache-dir "numpy==2.5.3" \
        || { echo "AMORCE A1-V4 V5 : installation de numpy==2.5.3 impossible : rien ne part"; exit 2; }
    echo "AMORCE A1-V4 V5 $(date -u +%FT%TZ) : installations en $(( $(date +%s) - t0 )) s ; $(complete "$PY_IMAGE") ;" \
         "numpy $("$PY_IMAGE" -c 'import numpy; print(numpy.__version__)' 2>/dev/null || echo absent)"
fi
if [ "$(version "$PY_CONF")" != "3.13" ]; then  # C1
    ln -sfn "$PY_IMAGE" "$PY_CONF" 2>/dev/null || { echo "AMORCE A1-V4 V5 : lien $PY_CONF -> $PY_IMAGE impossible (C1) : rien ne part"; exit 2; }
fi
[ "$(version "$PY_CONF")" = "3.13" ] || { echo "AMORCE A1-V4 V5 : $PY_CONF n'est pas Python 3.13 (C1) : rien ne part"; exit 2; }
echo "AMORCE A1-V4 V5 : interpréteurs après (C1) : $PY_IMAGE $(complete "$PY_IMAGE") ; $PY_CONF -> $(readlink -f "$PY_CONF") $(complete "$PY_CONF")"
for p in "$PY_IMAGE" "$PY_CONF"; do  # correction 7
    NV=$("$p" -c 'import numpy; print(numpy.__version__)' 2>/dev/null)
    [ "$NV" = "2.5.3" ] || { echo "AMORCE A1-V4 V5 : numpy ${NV:-absent} sous $p au lieu de 2.5.3 (correction 7) : rien ne part"; exit 2; }
done
echo "AMORCE A1-V4 V5 : numpy 2.5.3 sous $PY_IMAGE et $PY_CONF (correction 7)"
exec "$PY_IMAGE" -I -B "$D/hote_durable_a1_v4_v5.py" hote
