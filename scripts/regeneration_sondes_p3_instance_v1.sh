#!/usr/bin/env bash
# Régénération du fichier complet des sondes figées de P3, sur l'instance de calcul (devis
# docs/notes/regeneration-sondes-p3-v1/devis-regeneration-sondes-p3-v1.md, GO-2026-10-28-11), v1. Déclinée de
# `p3_instance.sh` sous un nom nouveau (R12) : même mise en place (clone au commit de P3, lecture précoce du
# préenregistrement, environnement `requirements-gpu.txt`, suite des tests au nombre attendu), puis, au lieu du lanceur
# de P3, `regenerer_sondes_p3_v1.py` (copié hors du clone par l'amorce), qui appelle le lanceur de P3 sans en changer une
# ligne et s'arrête après les sondes figées. Le processus est borné à 30 cœurs (`taskset`), le nombre de fils effectifs
# consigné par P3 (`fils_entrainement_effectifs` = 30 : min(32, affinité, quota 30,72)).
# Poussé sur BRANCHE : manifeste et résultats du run, fichier léger, sceau du fichier complet, verdict, traces ; si le
# fichier complet existe et que son sceau est conforme (quel que soit le verdict), le fichier en morceaux de 90 Mio (scellés
# un à un, liste scellée, reconstitution vérifiée), pour que la couche 2 le lise. v1 après la contre-lecture R2 (CLR-01 à 10).
#
# Variables : COMMIT_P3 (commit de P3, 40 caractères), REGEN (dossier de l'amorce : script et références), BRANCHE,
# GH_TOKEN, HF_TOKEN, DEPOT_URL ; pour l'essai local seulement : MODE=jouet, PREREG_ABSENT=1, CONFIG, TACHES,
# VENV_EXISTANT, FILS (défaut 30), FILS_BLAS (défaut 64), TRAVAIL, SAUTER_TESTS=1, AUTORISER_DEPOT_SALE=1 (banc jouet seulement).
set -euo pipefail
: "${COMMIT_P3:?COMMIT_P3 obligatoire}" "${REGEN:?REGEN obligatoire}"
MODE="${MODE:-reel}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
BRANCHE="${BRANCHE:-calcul/regeneration-sondes-p3-v1}"
PREREG="${PREREG:-prereg/P3-premier-test-i-a-v1.md}"
TRAVAIL="${TRAVAIL:-$HOME/regeneration}"
PREREG_ABSENT="${PREREG_ABSENT:-0}"
FILS="${FILS:-30}"
case "$MODE" in reel|jouet) ;; *) echo "MODE=$MODE : reel ou jouet" >&2; exit 2 ;; esac
[ "$PREREG_ABSENT" = 1 ] && [ "$MODE" != jouet ] && { echo "PREREG_ABSENT=1 n'est permis qu'en mode jouet (R1)" >&2; exit 2; }
[[ "$FILS" =~ ^[0-9]+$ ]] || { echo "FILS : entier attendu" >&2; exit 2; }
MOTIF_PROGRES='^PROGRES [0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z( [a-z_]+=[^ ]+)+$'
mkdir -p "$TRAVAIL"
JOURNAL="$TRAVAIL/journal.txt"
journal() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$JOURNAL"; }
AIDE_GIT='!f() { echo username=x-access-token; echo "password=${GH_TOKEN:-}"; }; f'
journal "début : régénération des sondes de P3 ; MODE=$MODE COMMIT_P3=$COMMIT_P3 BRANCHE=$BRANCHE FILS=$FILS"
[ "$MODE" = reel ] && : "${HF_TOKEN:?HF_TOKEN obligatoire en mode reel}"
for f in regenerer_sondes_p3_v1.py ref/sondes-figees-legeres.npz ref/sondes-figees.json ref/manifeste.json; do
    [ -f "$REGEN/$f" ] && [ -f "$REGEN/$f.sha256" ] || { journal "$REGEN/$f ou son sceau absent : arrêt"; exit 2; }
    [ "$(sha256sum "$REGEN/$f" | cut -d' ' -f1)" = "$(cut -d' ' -f1 "$REGEN/$f.sha256")" ] || { journal "sceau de $f non conforme : arrêt"; exit 2; }
done

DEPOT="$TRAVAIL/controle-ia"
[ -e "$DEPOT" ] && { echo "$DEPOT existe déjà (R12)" >&2; exit 2; }
git -c credential.helper="$AIDE_GIT" clone -q "$DEPOT_URL" "$DEPOT"
cd "$DEPOT"
git config credential.helper "$AIDE_GIT"
git config user.name "instance de calcul (régénération des sondes de P3)"
git config user.email "instance-calcul@invalid"
git checkout -q "$COMMIT_P3"
code_branche=0
git ls-remote --exit-code origin "refs/heads/$BRANCHE" >/dev/null 2>"$TRAVAIL/ls-remote.err" || code_branche=$?
case "$code_branche" in
    0) journal "branche $BRANCHE déjà présente : arrêt avant l'installation (R12)"; exit 2 ;;
    2) ;;
    *) journal "vérification de la branche $BRANCHE impossible (code $code_branche) : arrêt avant l'installation"; exit 2 ;;
esac
git checkout -q -b "$BRANCHE"

lire_unique() {
    local n
    n=$(grep -c "$1 : \`" "$PREREG" || true)
    if [ "$n" != 1 ]; then echo ""; return 0; fi
    sed -n "s/.*$1 : \`\\([^\`]*\\)\`.*/\\1/p" "$PREREG"
}
ARGS=()
if [ "$PREREG_ABSENT" = 1 ]; then
    ATTENDUS="${TESTS_ATTENDUS:-}"
    : "${CONFIG:?CONFIG obligatoire sans préenregistrement}" "${TACHES:?TACHES obligatoire sans préenregistrement}"
else
    [ -f "$PREREG" ] || { journal "préenregistrement $PREREG absent au commit $COMMIT_P3 : arrêt"; exit 2; }
    ATTENDUS=$(lire_unique "Tests attendus")
    [[ "$ATTENDUS" =~ ^[0-9]+$ ]] || { journal "nombre de tests attendus introuvable dans $PREREG : arrêt"; exit 2; }
    CONFIG=$(lire_unique "Chemin de la configuration de P3")
    TACHES=$(lire_unique "Chemin des tâches de P3")
    CONSIGNES=$(lire_unique "Chemin des consignes de P3")
    for f in "$CONFIG" "$TACHES" "$CONSIGNES"; do
        [ -n "$f" ] && [ -f "$f" ] && [ -f "$f.sha256" ] || { journal "fichier cité « $f » ou son sceau absent : arrêt"; exit 2; }
    done
    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -u -m controle_ia.scellement verifier "$CONFIG" "$TACHES" "$CONSIGNES" \
        >"$TRAVAIL/sceaux.txt" 2>&1 || { journal "sceau non conforme parmi les fichiers cités : arrêt"; exit 2; }
    ARGS=(--prereg "$PREREG" --commit-attendu "$COMMIT_P3")
    journal "préenregistrement lu : $ATTENDUS tests attendus ; configuration $CONFIG ; tâches $TACHES : présents et scellés"
fi

pousser() {
    local essai
    for essai in 1 2 3; do
        if git push -q origin "$BRANCHE" 2>"$TRAVAIL/poussee.err"; then return 0; fi
        journal "poussée de $BRANCHE : tentative $essai refusée ($(tail -n 1 "$TRAVAIL/poussee.err" | tr '\n' ' '))"
        [ "$essai" -lt 3 ] && sleep $((15 * essai * essai))
    done
    return 1
}
pousser || { journal "poussée initiale de $BRANCHE refusée : arrêt avant l'installation"; exit 2; }
journal "branche $BRANCHE poussée avant l'installation (droit d'écriture éprouvé)"

traces() {
    local d
    mkdir -p traces
    d=$(mktemp -d "traces/regeneration-sondes-p3-$(date -u +%Y%m%d-%H%M%S)-XXXX")
    for f in "$JOURNAL" "$TRAVAIL"/tests.txt "$TRAVAIL"/tests.err "$TRAVAIL"/regeneration.out "$TRAVAIL"/run.err \
             "$TRAVAIL"/machine.txt "$TRAVAIL"/pip-freeze.txt "$TRAVAIL"/verdict-regeneration-v1.json \
             "$TRAVAIL"/verdict-regeneration-v1.json.sha256 "$TRAVAIL"/morceaux.txt; do
        [ -f "$f" ] && cp "$f" "$d/"
    done
    (cd "$d" && sha256sum -- * > empreintes.sha256) || true
    git add "$d" && git commit -qm "Régénération des sondes de P3 : traces ($1)" >/dev/null 2>&1 || true
}
# fichier complet en morceaux de 90 Mio dès qu'il existe et que son sceau est conforme, quel que soit le verdict (CLR-04) ;
# reconstitution vérifiée avant la poussée (CLR-10) ; un commit et une poussée par morceau
verser_morceaux() {
    local r=$1 m n
    [ -f "donnees/$r/sondes-figees.npz" ] && [ -f "donnees/$r/sondes-figees.npz.sha256" ] || return 0
    [ "$(sha256sum "donnees/$r/sondes-figees.npz" | cut -d' ' -f1)" = "$(cut -d' ' -f1 "donnees/$r/sondes-figees.npz.sha256")" ] \
        || { journal "fichier complet ≠ son sceau : morceaux non versés"; return 1; }
    ls "donnees/$r"/sondes-figees.npz.morceau-* >/dev/null 2>&1 && return 0
    (cd "donnees/$r" && split -b 90M -d -a 2 sondes-figees.npz sondes-figees.npz.morceau-)
    [ "$(cat "donnees/$r"/sondes-figees.npz.morceau-* | sha256sum | cut -d' ' -f1)" = "$(cut -d' ' -f1 "donnees/$r/sondes-figees.npz.sha256")" ] \
        || { journal "morceaux : reconstitution ≠ sceau du fichier complet : non versés"; return 1; }
    (cd "donnees/$r" && sha256sum sondes-figees.npz.morceau-* > sondes-figees.npz.morceaux.txt \
        && sha256sum sondes-figees.npz.morceaux.txt > sondes-figees.npz.morceaux.txt.sha256)
    cp "donnees/$r/sondes-figees.npz.morceaux.txt" "$TRAVAIL/morceaux.txt"
    for m in "donnees/$r"/sondes-figees.npz.morceau-*; do
        git add -f "$m" && git commit -qm "Régénération des sondes de P3 : $(basename "$m")"
        pousser || { journal "poussée de $(basename "$m") impossible"; return 1; }
    done
    git add -f "donnees/$r/sondes-figees.npz.morceaux.txt" "donnees/$r/sondes-figees.npz.morceaux.txt.sha256"
    git commit -qm "Régénération des sondes de P3 : liste scellée des morceaux"
    n=$(wc -l < "donnees/$r/sondes-figees.npz.morceaux.txt")
    journal "fichier complet versé en $n morceaux (reconstitution vérifiée)"
}
RUN=""
CONSIGNE=""
consigner_arret() {
    CONSIGNE=1
    git add -A runs diag 2>/dev/null || true
    for f in donnees/*/sondes-figees-legeres.npz donnees/*/sondes-figees-legeres.npz.sha256 donnees/*/sondes-figees.npz.sha256; do
        [ -f "$f" ] && git add -f "$f"
    done
    git commit -qm "Régénération des sondes de P3 : arrêt pendant $1" >/dev/null 2>&1 || true
    [ -n "$RUN" ] && { verser_morceaux "$RUN" || true; }
    traces "arrêt pendant $1"
    pousser || journal "poussée impossible : résultats restés sur l'instance"
}
ETAPE="mise en place"; PID_RUN=""
sur_term() {
    trap '' TERM
    journal "TERM reçu pendant $ETAPE"
    [ -n "$PID_RUN" ] && { kill -TERM "$PID_RUN" 2>/dev/null || true; wait "$PID_RUN" 2>/dev/null || true; }
    consigner_arret "$ETAPE (TERM)" || true
    exit 124
}
trap sur_term TERM
sur_sortie() {
    local code=$?
    if [ "$code" -ne 0 ] && [ -z "$CONSIGNE" ]; then
        trap '' TERM; journal "sortie imprévue (code $code) pendant $ETAPE" || true
        consigner_arret "$ETAPE (code $code)" || true
    fi
    exit "$code"
}
trap sur_sortie EXIT

{ nproc; python3 -c 'import os; print("affinité", len(os.sched_getaffinity(0)))'; env | grep -i -E 'thread|omp|mkl|blas' || true; lscpu 2>/dev/null | grep -E '^(Model name|CPU\(s\)|Thread|Core|Socket)' || true;
  cat /sys/fs/cgroup/cpu.max 2>/dev/null || true; [ "$MODE" = reel ] && nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv; } \
    > "$TRAVAIL/machine.txt" 2>&1 || true
tee -a "$JOURNAL" < "$TRAVAIL/machine.txt" >/dev/null
# les FILS premiers cœurs de l'affinité réelle du conteneur (CLR-02) ; le quota est contrôlé par le script avant calcul
COEURS=$(python3 -c 'import os, sys; c = sorted(os.sched_getaffinity(0)); n = int(sys.argv[1]); print(",".join(map(str, c[:n])) if len(c) >= n else "")' "$FILS")
[ -n "$COEURS" ] || { journal "affinité du conteneur < $FILS cœurs : arrêt avant l'installation"; consigner_arret "contrôle des cœurs"; exit 1; }
taskset -c "$COEURS" true || { journal "taskset refusé sur les cœurs $COEURS : arrêt avant l'installation"; consigner_arret "contrôle des cœurs"; exit 1; }
journal "cœurs retenus : $COEURS"

if [ -n "${VENV_EXISTANT:-}" ]; then
    # shellcheck disable=SC1091
    . "$VENV_EXISTANT/bin/activate"
else
    python3.11 -m venv .venv
    # shellcheck disable=SC1091
    . .venv/bin/activate
    pip install -q -r requirements-gpu.txt
fi
python -m pip freeze --all >"$TRAVAIL/pip-freeze.txt" 2>/dev/null || journal "pip freeze impossible (descriptif)"
if [ "$MODE" = reel ] && ! python -c "import sys, torch; sys.exit(0 if torch.cuda.is_available() else 1)"; then
    journal "carte indisponible pour torch : arrêt avant les tests"; consigner_arret "contrôle de la carte"; exit 1
fi
ETAPE="tests"
if [ "${SAUTER_TESTS:-0}" = 1 ]; then
    [ "$MODE" = jouet ] || { journal "SAUTER_TESTS=1 n'est permis qu'en mode jouet : arrêt"; consigner_arret "tests"; exit 1; }
    journal "tests sautés (banc jouet seulement)"
elif ! PYTHONPATH=src python -m pytest -q -p no:cacheprovider --color=no >"$TRAVAIL/tests.txt" 2>"$TRAVAIL/tests.err"; then
    journal "tests en échec : arrêt"; consigner_arret "tests"; exit 1
fi
DERNIERE=$(tail -1 "$TRAVAIL/tests.txt" 2>/dev/null || true); [ -n "$DERNIERE" ] && journal "tests : $DERNIERE"
if [ "${SAUTER_TESTS:-0}" != 1 ] && [ -n "$ATTENDUS" ] && ! printf '%s\n' "$DERNIERE" | grep -Eq "^$ATTENDUS passed(, [0-9]+ warnings?)? in [0-9.]+s( \([0-9]+:[0-9]{2}:[0-9]{2}\))?$"; then
    journal "tests : « $DERNIERE » ≠ « $ATTENDUS passed » : arrêt"; consigner_arret "tests"; exit 1
fi

RUN="$(date -u +%Y%m%d-%H%M%S)-p3-regeneration-sondes"   # connu de consigner_arret (versement des morceaux)
ETAPE="régénération $RUN"
journal "run : $RUN ; borné à $FILS cœurs ($COEURS) ; OpenBLAS à ${FILS_BLAS:-64} fils"
code=0
: >"$TRAVAIL/run.err"
taskset -c "$COEURS" timeout --signal=TERM --kill-after=5m 150m \
    python -u "$REGEN/regenerer_sondes_p3_v1.py" --racine . --config "$CONFIG" --taches "$TACHES" --run-id "$RUN" \
    --reference-legeres "$REGEN/ref/sondes-figees-legeres.npz" --reference-diag "$REGEN/ref/sondes-figees.json" \
    --reference-manifeste "$REGEN/ref/manifeste.json" --fils-blas "${FILS_BLAS:-64}" \
    --sortie "$TRAVAIL/verdict-regeneration-v1.json" "${ARGS[@]}" ${AUTORISER_DEPOT_SALE:+--autoriser-depot-sale} \
    >"$TRAVAIL/regeneration.out" 2>>"$TRAVAIL/run.err" &
PID_RUN=$!
( tail -n +1 -F --pid="$PID_RUN" "$TRAVAIL/run.err" 2>/dev/null | grep --line-buffered -E "$MOTIF_PROGRES" \
    | while IFS= read -r ligne; do printf '%s\n' "$ligne" | tee -a "$JOURNAL"; done ) &
PID_RELAIS=$!
wait "$PID_RUN" || code=$?
PID_RUN=""
wait "$PID_RELAIS" 2>/dev/null || true
if [ "$code" -ne 0 ] || [ ! -f "$TRAVAIL/verdict-regeneration-v1.json" ]; then
    grep -v '^PROGRES ' "$TRAVAIL/run.err" | tail -n 5 | tee -a "$JOURNAL" || true
    consigner_arret "régénération (code $code)"; exit 1
fi
VERDICT=$(python3 -c 'import json, sys; print(json.load(open(sys.argv[1]))["verdict"])' "$TRAVAIL/verdict-regeneration-v1.json")
journal "verdict : $VERDICT ; $(tail -1 "$TRAVAIL/regeneration.out")"
ETAPE="versement"
git add "runs/$RUN" "diag/$RUN"
git add -f "donnees/$RUN/sondes-figees-legeres.npz" "donnees/$RUN/sondes-figees-legeres.npz.sha256" "donnees/$RUN/sondes-figees.npz.sha256"
git commit -qm "Régénération des sondes de P3, run $RUN : verdict $VERDICT"
pousser || journal "poussée du run impossible : résultats restés sur l'instance"
verser_morceaux "$RUN" || { consigner_arret "versement des morceaux"; exit 1; }
ETAPE="fin"
CONSIGNE=1
traces "fin"
if pousser; then journal "fin : $RUN, verdict $VERDICT ; branche $BRANCHE poussée ; arrêter l'instance par son identifiant (R10)"
else journal "poussée finale impossible : résultats restés sur l'instance"; exit 1; fi
