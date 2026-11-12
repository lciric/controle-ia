#!/usr/bin/env bash
# Premier test boîte blanche sur l'organisme (i-a) (P3, R-192) sur l'instance de calcul : mise en place, tests, un run du
# lanceur `controle_ia.premier_test_ia.run` (extraction générique, entraînement des sondes, sondes figées avant le premier
# épisode, épisodes des quatre conditions notés en ligne), poussée des résultats, des données légères et des traces (seul
# le fichier complet des sondes reste sur l'instance, son sceau poussé : leçon de N-012). Décliné de `notations_t05_instance.sh` sous un nom nouveau (R12 : le script
# des notations, cité par son préenregistrement, n'est pas modifié). Différences : étude « p3 » ; lecture précoce de la
# configuration, des tâches et des consignes citées ; données légères du run (sondes figées sans les matrices de
# Mahalanobis, scores par action, scores par jeton des sondes principales, textes des actions, et le sceau du fichier
# complet des sondes) poussées par ajout forcé ; délai externe de 300 minutes. Lignes de progression du lanceur (préfixe « PROGRES », couples clé=valeur) recopiées dans le journal que lit
# la surveillance. Rien ne se lance sans GO consigné.
#
#   COMMIT=<commit de scellement du préenregistrement de P3> bash p3_instance.sh
#
# Variables :
#   COMMIT        (obligatoire) commit à extraire ; le lanceur Python vérifie en plus le commit, la configuration, les
#                 tâches, les consignes, les données génériques et l'entropie
#   MODE          reel (défaut) ou jouet (répétition sur processeur)
#   PREREG        défaut prereg/P3-premier-test-i-a-v1.md ; il cite, une seule fois chacun, « Tests attendus : `N` »,
#                 « Chemin de la configuration de P3 : `…` », « Chemin des tâches de P3 : `…` », « Chemin des consignes de
#                 P3 : `…` », que ce script lit avant toute installation
#   PREREG_ABSENT 1 seulement en mode jouet : répétition sans préenregistrement ; CONFIG et TACHES donnent les chemins
#   DEPOT_URL     défaut https://github.com/lciric/controle-ia-travail.git (dépôt de travail privé ; N-016)
#   GH_TOKEN      jeton GitHub à grain fin ; lu par un assistant d'identification, jamais écrit
#   HF_TOKEN      jeton Hugging Face en lecture (mode reel)
#   BRANCHE       défaut calcul/p3-<MODE>-v1 ; une branche qui existe déjà arrête avant tout calcul
#   TESTS_ATTENDUS nombre de tests attendus (sans préenregistrement seulement)
#   TRAVAIL       défaut $HOME/p3
#   VENV_EXISTANT environnement Python déjà prêt à réutiliser (sinon : python3.11 -m venv + requirements-gpu.txt)
set -euo pipefail

: "${COMMIT:?COMMIT obligatoire (commit de scellement du préenregistrement de P3)}"
ETUDE=p3
MODE="${MODE:-reel}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
BRANCHE="${BRANCHE:-calcul/p3-$MODE-v1}"
PREREG="${PREREG:-prereg/P3-premier-test-i-a-v1.md}"
TRAVAIL="${TRAVAIL:-$HOME/p3}"
PREREG_ABSENT="${PREREG_ABSENT:-0}"
case "$MODE" in reel|jouet) ;; *) echo "MODE=$MODE : reel ou jouet" >&2; exit 2 ;; esac
if [ "$PREREG_ABSENT" = 1 ] && [ "$MODE" != jouet ]; then
    echo "PREREG_ABSENT=1 n'est permis qu'en mode jouet (R1)" >&2; exit 2
fi
# lignes de progression du lanceur recopiées au journal : préfixe fixe, horodatage, puis des couples clé=valeur sans
# espace (nombres, rangs, noms de sondes, empreintes, étapes) ; aucune autre ligne de la sortie d'erreur n'y passe (aucun texte)
MOTIF_PROGRES='^PROGRES [0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z( [a-z_]+=[^ ]+)+$'

mkdir -p "$TRAVAIL"
JOURNAL="$TRAVAIL/journal.txt"
journal() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$JOURNAL"; }
AIDE_GIT='!f() { echo username=x-access-token; echo "password=${GH_TOKEN:-}"; }; f'

journal "début : ETUDE=$ETUDE MODE=$MODE COMMIT=$COMMIT BRANCHE=$BRANCHE"
if [ "$MODE" = reel ]; then
    : "${HF_TOKEN:?HF_TOKEN obligatoire en mode reel}"
fi

DEPOT="$TRAVAIL/controle-ia"
if [ -e "$DEPOT" ]; then
    echo "$DEPOT existe déjà : R12, aucune réécriture ; choisir un autre TRAVAIL" >&2
    exit 2
fi
git -c credential.helper="$AIDE_GIT" clone -q "$DEPOT_URL" "$DEPOT"
cd "$DEPOT"
git config credential.helper "$AIDE_GIT"
git config user.name "instance de calcul (P3)"
git config user.email "instance-calcul@invalid"
git checkout -q "$COMMIT"
code_branche=0
git ls-remote --exit-code origin "refs/heads/$BRANCHE" >/dev/null 2>"$TRAVAIL/ls-remote.err" || code_branche=$?
case "$code_branche" in
    0) journal "branche $BRANCHE déjà présente sur le dépôt distant : relancement sous une branche nouvelle (BRANCHE=…) ; arrêt avant l'installation"
       exit 2 ;;
    2) ;;
    *) cause=$( (grep -E '^(fatal|error|remote):' "$TRAVAIL/ls-remote.err" || tail -n 2 "$TRAVAIL/ls-remote.err") | tr '\n' ' ' || true)
       journal "vérification de la branche $BRANCHE impossible (git ls-remote, code $code_branche : $cause) : arrêt avant l'installation"
       exit 2 ;;
esac
git checkout -q -b "$BRANCHE"

# Lecture précoce du préenregistrement, avant toute installation : chaque citation lue doit y figurer une seule fois
# (relecture du plan, constat 12 : jamais la première occurrence d'un intitulé recopié du pilote)
lire_unique() {
    local n
    n=$(grep -c "$1 : \`" "$PREREG" || true)
    if [ "$n" != 1 ]; then echo ""; return 0; fi
    sed -n "s/.*$1 : \`\\([^\`]*\\)\`.*/\\1/p" "$PREREG"
}
if [ "$PREREG_ABSENT" = 1 ]; then
    ATTENDUS="${TESTS_ATTENDUS:-}"
    : "${CONFIG:?CONFIG obligatoire sans préenregistrement}" "${TACHES:?TACHES obligatoire sans préenregistrement}"
else
    [ -f "$PREREG" ] || { journal "préenregistrement $PREREG absent au commit $COMMIT : arrêt avant l'installation"; exit 2; }
    ATTENDUS=$(lire_unique "Tests attendus")
    [[ "$ATTENDUS" =~ ^[0-9]+$ ]] || { journal "nombre de tests attendus introuvable ou cité plusieurs fois dans $PREREG : arrêt avant l'installation"; exit 2; }
    CONFIG=$(lire_unique "Chemin de la configuration de P3")
    TACHES=$(lire_unique "Chemin des tâches de P3")
    CONSIGNES=$(lire_unique "Chemin des consignes de P3")
    CITES=("$CONFIG" "$TACHES" "$CONSIGNES")
    for f in "${CITES[@]}"; do
        [ -n "$f" ] || { journal "chemin cité introuvable ou cité plusieurs fois dans $PREREG : arrêt avant l'installation"; exit 2; }
        if [ ! -f "$f" ] || [ ! -f "$f.sha256" ]; then
            journal "fichier cité $f ou son sceau absent de l'arbre du commit $COMMIT : arrêt avant l'installation"
            exit 2
        fi
    done
    if ! PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -u -m controle_ia.scellement verifier "${CITES[@]}" \
            >"$TRAVAIL/sceaux.txt" 2>&1; then
        cause=$(grep -v '^OK ' "$TRAVAIL/sceaux.txt" | tail -n 1 || true)
        journal "sceau non conforme parmi les fichiers cités ($cause) : arrêt avant l'installation"
        exit 2
    fi
    journal "préenregistrement lu : $ATTENDUS tests attendus ; configuration $CONFIG ; tâches $TACHES ; consignes $CONSIGNES : présents et scellés"
fi

poussee_initiale=0
for essai in 1 2 3; do
    if git push -q origin "$BRANCHE" 2>"$TRAVAIL/poussee-initiale.err"; then poussee_initiale=1; break; fi
    journal "poussée initiale de la branche $BRANCHE : tentative $essai refusée"
    if [ "$essai" -lt 3 ]; then sleep 5; fi
done
if [ "$poussee_initiale" != 1 ]; then
    cause=$( (grep -E '^(fatal|error|remote):' "$TRAVAIL/poussee-initiale.err" || tail -n 2 "$TRAVAIL/poussee-initiale.err") | tr '\n' ' ' || true)
    journal "poussée initiale de la branche $BRANCHE refusée ($cause) : droit d'écriture du jeton ? arrêt avant l'installation"
    exit 2
fi
journal "branche $BRANCHE poussée avant l'installation (droit d'écriture éprouvé)"

pousser() {
    local essai cause
    for essai in 1 2 3; do
        if git push -q origin "$BRANCHE" 2>"$TRAVAIL/poussee.err"; then return 0; fi
        cause=$( (grep -E '^(fatal|error|remote):' "$TRAVAIL/poussee.err" || tail -n 2 "$TRAVAIL/poussee.err") | tr '\n' ' ' || true)
        journal "poussée de la branche $BRANCHE : tentative $essai refusée ($cause)"
        if [ "$essai" -lt 3 ]; then sleep $((15 * essai * essai)); fi
    done
    return 1
}
traces() {
    local d
    mkdir -p traces
    d=$(mktemp -d "traces/p3-$(date -u +%Y%m%d-%H%M%S)-XXXX")
    for f in "$JOURNAL" "$TRAVAIL/tests.txt" "$TRAVAIL/tests.err" "$TRAVAIL"/run.json "$TRAVAIL"/run.err \
             "$TRAVAIL"/nvidia-smi.txt "$TRAVAIL"/pip-freeze.txt; do
        [ -f "$f" ] && cp "$f" "$d/"
    done
    (cd "$d" && sha256sum -- * > empreintes.sha256) || true
    git add "$d" && git commit -qm "P3 : traces de l'instance ($1)" >/dev/null 2>&1 || true
}
# données légères du run, par ajout forcé (donnees/ est ignoré par git) : sondes figées sans les matrices de Mahalanobis,
# scores par action, scores par jeton des sondes principales, textes des actions (dépôt de travail privé seulement, R-202),
# sceaux, et le sceau du fichier complet des sondes (le fichier complet, trop lourd, reste sur l'instance)
ajouter_donnees() {
    local f
    for f in donnees/*/sondes-figees-legeres.npz donnees/*/sondes-figees-legeres.npz.sha256 donnees/*/scores-p3.npz \
             donnees/*/scores-p3.npz.sha256 donnees/*/jetons-principales-p3.npz donnees/*/jetons-principales-p3.npz.sha256 \
             donnees/*/textes-actions-p3.jsonl donnees/*/textes-actions-p3.jsonl.sha256 donnees/*/sondes-figees.npz.sha256; do
        if [ -f "$f" ]; then git add -f "$f"; fi
    done
    return 0
}
CONSIGNE=""
consigner_arret() {
    CONSIGNE=1
    git add -A runs diag
    ajouter_donnees
    if git commit -qm "P3 : arrêt pendant $1" >/dev/null 2>&1; then
        journal "ARRÊT pendant $1 : résultats partiels committés (dont arret.json s'il existe)"
    else
        journal "ARRÊT pendant $1 : aucun résultat à committer"
    fi
    traces "arrêt pendant $1"
    if pousser; then journal "branche $BRANCHE poussée"; else journal "poussée impossible : résultats restés sur l'instance"; fi
}

ETAPE="mise en place"
PID_RUN=""
sur_term() {
    trap '' TERM
    journal "TERM reçu pendant $ETAPE (plafond de l'amorce)"
    if [ -n "$PID_RUN" ]; then
        kill -TERM "$PID_RUN" 2>/dev/null || true
        wait "$PID_RUN" 2>/dev/null || true
    fi
    consigner_arret "$ETAPE (plafond de l'amorce)" || true
    exit 124
}
trap sur_term TERM
sur_sortie() {
    local code=$?
    if [ "$code" -ne 0 ] && [ -z "$CONSIGNE" ]; then
        trap '' TERM
        journal "sortie imprévue (code $code) pendant $ETAPE" || true
        consigner_arret "$ETAPE (sortie imprévue, code $code)" || true
    fi
    exit "$code"
}
trap sur_sortie EXIT

if [ "$MODE" = reel ]; then
    nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv | tee -a "$JOURNAL" "$TRAVAIL/nvidia-smi.txt"
fi

if [ -n "${VENV_EXISTANT:-}" ]; then
    # shellcheck disable=SC1091
    . "$VENV_EXISTANT/bin/activate"
else
    python3.11 -m venv .venv
    # shellcheck disable=SC1091
    . .venv/bin/activate
    pip install -q -r requirements-gpu.txt
fi
if ! python -m pip freeze --all >"$TRAVAIL/pip-freeze.txt" 2>"$TRAVAIL/pip-freeze.err"; then
    journal "pip freeze impossible (descriptif, sans effet sur le run) : $(tail -n 1 "$TRAVAIL/pip-freeze.err" | tr '\n' ' ')"
fi

python -c "import torch; print('torch', torch.__version__, 'cuda', torch.version.cuda, 'disponible', torch.cuda.is_available())" | tee -a "$JOURNAL"
if [ "$MODE" = reel ] && ! python -c "import sys, torch; sys.exit(0 if torch.cuda.is_available() else 1)"; then
    journal "carte indisponible pour torch (pilote CUDA trop ancien ?) : arrêt avant les tests"
    consigner_arret "contrôle de la carte"
    exit 1
fi
ETAPE="tests"
if ! PYTHONPATH=src python -m pytest -q -p no:cacheprovider --color=no >"$TRAVAIL/tests.txt" 2>"$TRAVAIL/tests.err"; then
    tail -n 5 "$TRAVAIL/tests.txt" "$TRAVAIL/tests.err" | tee -a "$JOURNAL"
    journal "tests en échec : arrêt"
    consigner_arret "tests"
    exit 1
fi
DERNIERE=$(tail -1 "$TRAVAIL/tests.txt")
journal "tests : $DERNIERE"
if [ -n "$ATTENDUS" ] && ! printf '%s\n' "$DERNIERE" | grep -Eq "^$ATTENDUS passed(, [0-9]+ warnings?)? in [0-9.]+s( \([0-9]+:[0-9]{2}:[0-9]{2}\))?$"; then
    journal "tests : « $DERNIERE » ≠ « $ATTENDUS passed », sans test sauté ni en échec : arrêt"
    consigner_arret "tests"
    exit 1
fi

ETAPE="lancement"
ARGS=()
if [ "$PREREG_ABSENT" = 1 ]; then
    journal "répétition sans préenregistrement (jouet, non décisive)"
else
    ARGS=(--prereg "$PREREG")
fi
journal "configuration : $CONFIG ; tâches : $TACHES"
LANCEUR=(controle_ia.premier_test_ia.run --config "$CONFIG" --taches "$TACHES")
# délai externe du run, figé (R1) : TERM à 300 minutes, converti en arrêt consigné, puis KILL cinq minutes plus tard ; les
# échéances internes (duree_max_s, 16 200 s, et le budget de l'entraînement) sont plus courtes. Le signal vise le
# processus lancé par timeout, par son identifiant (R10).
DELAI=(timeout --signal=TERM --kill-after=5m 300m)
RUN="$(date -u +%Y%m%d-%H%M%S)-p3-$MODE"
ETAPE="run $RUN"
journal "run : $RUN"
code=0
: >"$TRAVAIL/run.err"
PYTHONPATH=src "${DELAI[@]}" python -m "${LANCEUR[@]}" --run-id "$RUN" "${ARGS[@]}" >"$TRAVAIL/run.json" \
    2>>"$TRAVAIL/run.err" &
PID_RUN=$!
# relais des lignes de progression : tail s'arrête de lui-même quand le run se termine (--pid), sans arrêt par motif
( tail -n +1 -F --pid="$PID_RUN" "$TRAVAIL/run.err" 2>/dev/null | grep --line-buffered -E "$MOTIF_PROGRES" \
    | while IFS= read -r ligne; do printf '%s\n' "$ligne" | tee -a "$JOURNAL"; done ) &
PID_RELAIS=$!
wait "$PID_RUN" || code=$?
PID_RUN=""
wait "$PID_RELAIS" 2>/dev/null || true
# un run est complet si son résumé existe sans arrêt consigné
if [ "$code" -ne 0 ]; then
    if [ -f "diag/$RUN/resume.json" ] && [ ! -f "diag/$RUN/arret.json" ]; then
        journal "run : code $code, mais résumé écrit sans arrêt consigné : run complet"
    else
        # diagnostic, comme au pilote : dernières lignes de la sortie d'erreur, hors de toute ligne de progression
        grep -v '^PROGRES ' "$TRAVAIL/run.err" | tail -n 5 | tee -a "$JOURNAL" || true
        consigner_arret "run (code $code)"; exit 1
    fi
fi
git add "runs/$RUN" "diag/$RUN"
ajouter_donnees
git commit -qm "P3 ($MODE), run $RUN"
# le résumé reste dans run.json, versé aux traces ; il n'est pas recopié au journal que lit la surveillance
journal "run terminé : $RUN"
ETAPE="poussée"
pousser || journal "poussée du run impossible : résultats restés sur l'instance"
ETAPE="fin"
journal "fin : $RUN ; arrêter l'instance par son identifiant (R10)"
CONSIGNE=1
traces "fin"
if pousser; then
    journal "branche $BRANCHE poussée (résultats et traces)"
else
    journal "run complet, mais poussée finale impossible après trois tentatives : résultats et traces restés sur l'instance"
    exit 1
fi
