#!/usr/bin/env bash
# Essai local de l amorce de T0.6 v7 (R-1677, R-1692, 0 USD, aucun appel à Vast, aucune clé) : joue l amorce v7 en essai local (AMORCE_ESSAI_LOCAL=1),
# avec la configuration d'une épreuve à blanc, dans le mode demandé, et mesure le clonage réduit. Deux formes :
#  - par défaut : contre un dépôt SOURCE RÉDUIT construit ici à partir des fichiers suivis (les dossiers exclus de la liste de l'amorce y sont
#    remplacés par de petits fichiers témoins : leur absence après le clonage prouve l'extraction partielle), servi par un miroir nu qui accepte
#    les clonages filtrés ; l'argument COMMIT est ignoré (le commit du dépôt réduit est utilisé). S'arrête (par le PID de l'amorce, R10) dès la
#    ligne « branche … poussée avant l'installation » : poussée initiale comprise (vers le miroir), installation et essais non joués ;
#  - REEL_DEPOT_URL=URL du dépôt distant réel (lecture seule, accès par l'environnement, aucune clé lue ici) : clone réel du COMMIT donné,
#    mesure de la taille et de la durée, arrêt dès la ligne CLONAGE (jamais de poussée vers le dépôt réel). Imprime : la ligne CLONAGE de l'amorce, la taille du dépôt `.git` et de l'arbre extrait, la
# liste des dossiers de premier niveau extraits, la présence des chemins exigés, l'absence de ceux qui sont exclus.
#   bash scripts/essai_amorce_t06_v7.sh DOSSIER_NEUF MODE(jouet|reel) COMMIT CONFIG_RELATIF [MIROIR_NU_EXISTANT]
# Variables : DEPOT_SOURCE (défaut : le dépôt de ce script) ; AMORCE (défaut : scripts/amorce_instance_t06_v7.sh du commit CITÉ, lu par `git show`).
set -euo pipefail
W=$(realpath -m "${1:?dossier neuf}"); MODE="${2:?jouet ou reel}"; COMMIT="${3:?commit}"; CONFIG="${4:?configuration relative}"; MIROIR="${5:-}"
case "$MODE" in jouet|reel) ;; *) echo "mode : jouet ou reel"; exit 2;; esac
[ -e "$W" ] && { echo "$W existe déjà (R12)"; exit 2; }
SRC="${DEPOT_SOURCE:-$(cd "$(dirname "$0")/.." && pwd)}"
command -v vastai >/dev/null 2>&1 && { echo "vastai présent : l'essai local n'appelle jamais Vast"; exit 2; }
mkdir -p "$W"
AMORCE_FICHIER="${AMORCE_FICHIER:-$SRC/scripts/amorce_instance_t06_v7.sh}"
if [ -n "${REEL_DEPOT_URL:-}" ]; then
    DEPOT_URL="$REEL_DEPOT_URL"; ARRET_SUR="CLONAGE mode="; cp "$AMORCE_FICHIER" "$W/amorce.sh"; MIROIR=""
else
    ARRET_SUR="poussée avant l'installation"
    if [ -z "$MIROIR" ]; then
        S="$W/source"; mkdir -p "$S"
        (cd "$SRC" && git ls-files -z | grep -zvE '^(docs/sources/pdf/|registres/passations/|livrables/|gemini/|brouillons/|papiers/|docs/sources/lecture-pdf)' | tar --null -T - -cf -) | tar -xf - -C "$S"
        for d in docs/sources/pdf registres/passations livrables gemini brouillons papiers; do mkdir -p "$S/$d"; echo "témoin exclu" > "$S/$d/temoin.txt"; done
        mkdir -p "$S/docs/sources/pdf" "$S/diag" "$S/runs"; : > "$S/runs/.gitkeep"
        (cd "$S" && git init -q -b main . && git config user.email e@example.invalid && git config user.name essai && git add -A && git add -f donnees diag runs prereg 2>/dev/null; git commit -qm "dépôt source réduit de l'essai local")
        COMMIT=$(git -C "$S" rev-parse HEAD); MIROIR="$W/distant.git"; git clone -q --bare "$S" "$MIROIR"
    fi
    git -C "$MIROIR" config uploadpack.allowFilter true; git -C "$MIROIR" config uploadpack.allowAnySHA1InWant true
    DEPOT_URL="file://$MIROIR"
    git -C "$MIROIR" cat-file -e "$COMMIT^{commit}" || { echo "commit $COMMIT absent du miroir"; exit 2; }
    cp "$AMORCE_FICHIER" "$W/amorce.sh"
fi
R="$W/instance"; mkdir -p "$R"
BRANCHE="essai/t06-essai-local-v5-$MODE-$(date -u +%H%M%S)"
echo "ESSAI : $(date -u +%FT%TZ) : mode $MODE, commit $COMMIT, configuration $CONFIG, miroir $MIROIR, branche $BRANCHE"
EXTRA=()
if [ -n "${REEL_DEPOT_URL:-}" ]; then      # lecture du dépôt réel : variables de passage réseau seulement (jamais affichées), configuration git globale lue sans modification
    for v in HTTPS_PROXY https_proxy NO_PROXY no_proxy SSL_CERT_FILE GIT_SSL_CAINFO CURL_CA_BUNDLE REQUESTS_CA_BUNDLE; do [ -n "${!v:-}" ] && EXTRA+=("$v=${!v}"); done
    [ -f "$HOME/.gitconfig" ] && EXTRA+=("GIT_CONFIG_GLOBAL=$HOME/.gitconfig")
fi
set +e
env -i "${EXTRA[@]}" PATH="$PATH" HOME="$W" LANG="${LANG:-C.UTF-8}" TMPDIR="${TMPDIR:-/tmp}" COMMIT="$COMMIT" MODE="$MODE" DEPOT_URL="$DEPOT_URL" GH_TOKEN=jeton-factice-essai \
    HF_TOKEN=jeton-hf-factice RACINE_AMORCE="$R" PREREG_ABSENT=1 EPREUVE_GO_ID=GO-2026-11-06-01 BRANCHE="$BRANCHE" CONFIG="$CONFIG" TESTS_ATTENDUS=1 \
    AMORCE_ESSAI_LOCAL=1 FIN_GO_UTC_S=1794355200 ECHEANCE_UTC_S=1794355200 DEPENSE_EPUISEE_UTC_S=1794355200 POUSSEE_ATTENTE_S=0 \
    bash "$W/amorce.sh" > "$W/amorce-sortie.txt" 2>&1 &
PID=$!
for _ in $(seq 1 900); do
    grep -q "$ARRET_SUR" "$W/amorce-sortie.txt" 2>/dev/null && break
    kill -0 "$PID" 2>/dev/null || break
    sleep 1
done
kill -0 "$PID" 2>/dev/null && { kill "$PID" 2>/dev/null; wait "$PID" 2>/dev/null; }
set -e
echo "## sortie de l'amorce (lignes AMORCE, journal) "; grep -aE "^AMORCE|poussée|refus" "$W/amorce-sortie.txt" | cut -c1-260
echo "## clonage"; grep -a "CLONAGE" "$W/amorce-sortie.txt" || echo "(ligne CLONAGE absente)"
echo "## dépôt .git (octets)"; du -sb "$R/amorce-depot/.git" | cut -f1
echo "## arbre extrait hors .git (octets)"; du -sb --exclude=.git "$R/amorce-depot" | cut -f1
echo "## dossiers de premier niveau extraits (octets)"; (cd "$R/amorce-depot" && du -sb --exclude=.git ./* ./.claude 2>/dev/null | sort -rn | head -20)
echo "## chemins exigés présents / exclus absents"
for p in src tests scripts prereg donnees docs/notes registres/go.md "$CONFIG" "$CONFIG.sha256" pyproject.toml requirements-gpu.txt; do [ -e "$R/amorce-depot/$p" ] && echo "présent  $p" || echo "ABSENT   $p (exigé)"; done
for p in docs/sources/pdf registres/passations brouillons livrables gemini; do [ -e "$R/amorce-depot/$p" ] && echo "PRÉSENT  $p (exclu !)" || echo "absent   $p (exclu)"; done
[ -n "$MIROIR" ] && { echo "## branche poussée au miroir"; git -C "$MIROIR" branch --list "$BRANCHE"; }
echo "ESSAI : $(date -u +%FT%TZ) : fin"
