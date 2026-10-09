#!/usr/bin/env bash
# Validation de T0.4 sur l'instance de calcul : mise en place, run A, run B (rejeu entre processus), poussée.
# Procédure : docs/procedures/validation-T0.4-modele-reel-v4.md. Rien ne se lance sans GO consigné.
#
#   COMMIT=<commit de scellement du préenregistrement> bash validation_t04_instance.sh
#
# Variables :
#   COMMIT        (obligatoire) commit à extraire ; le lanceur Python vérifie en plus le commit cité par le préenregistrement
#   MODE          reel (défaut), jouet (répétition sur processeur, sans modèle réel ni processeur graphique), ou sonde
#                 (sonde de mémoire de la carte en double précision, non décisive : ni run, ni lecture)
#   DEPOT_URL     défaut https://github.com/lciric/controle-ia.git
#   GH_TOKEN      jeton GitHub à grain fin (dépôt distant GitHub) ; lu par un assistant d'identification, jamais écrit
#   HF_TOKEN      jeton Hugging Face en lecture (mode reel) ; lu par huggingface_hub
#   BRANCHE       défaut calcul/t04-validation-v3 (les branches de la v1 et de la v2 existent déjà sur le dépôt distant)
#   TRAVAIL       défaut $HOME/t04
#   VENV_EXISTANT environnement Python déjà prêt à réutiliser (sinon : python3.11 -m venv + requirements-gpu.txt)
set -euo pipefail

: "${COMMIT:?COMMIT obligatoire (commit de scellement du préenregistrement)}"
MODE="${MODE:-reel}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia.git}"
BRANCHE="${BRANCHE:-calcul/t04-validation-v3}"
TRAVAIL="${TRAVAIL:-$HOME/t04}"
PREREG="prereg/T0.4-validation-modele-reel-v3.md"
case "$MODE" in reel|jouet|sonde) ;; *) echo "MODE=$MODE : reel, jouet ou sonde" >&2; exit 2 ;; esac

mkdir -p "$TRAVAIL"
JOURNAL="$TRAVAIL/journal.txt"
journal() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$JOURNAL"; }
AIDE_GIT='!f() { echo username=x-access-token; echo "password=${GH_TOKEN:-}"; }; f'

journal "début : MODE=$MODE COMMIT=$COMMIT BRANCHE=$BRANCHE"
if [ "$MODE" != jouet ]; then
    : "${HF_TOKEN:?HF_TOKEN obligatoire en mode reel ou sonde}"
fi

DEPOT="$TRAVAIL/controle-ia"
if [ -e "$DEPOT" ]; then
    echo "$DEPOT existe déjà : R12, aucune réécriture ; choisir un autre TRAVAIL" >&2
    exit 2
fi
git -c credential.helper="$AIDE_GIT" clone -q "$DEPOT_URL" "$DEPOT"
cd "$DEPOT"
git config credential.helper "$AIDE_GIT"
git config user.name "instance de calcul (T0.4)"
git config user.email "instance-calcul@invalid"
git checkout -q "$COMMIT"
git checkout -q -b "$BRANCHE"

pousser() { git push -q origin "$BRANCHE"; }
traces() {
    # journal, sorties des tests et des runs, versés sur la branche (hors arbre gelé) pour la session de pilotage ;
    # un dossier neuf à chaque versement, même deux fois dans la même seconde (R12)
    local d
    mkdir -p traces
    d=$(mktemp -d "traces/t04-$(date -u +%Y%m%d-%H%M%S)-XXXX")
    for f in "$JOURNAL" "$TRAVAIL/tests.txt" "$TRAVAIL/tests.err" "$TRAVAIL"/run-*.err "$TRAVAIL"/run-*.json \
             "$TRAVAIL"/sonde-*.json "$TRAVAIL"/sonde-*.err; do
        [ -f "$f" ] && cp "$f" "$d/"
    done
    (cd "$d" && sha256sum -- * > empreintes.sha256) || true          # R6 : traces scellées
    git add "$d" && git commit -qm "T0.4 — traces de l'instance ($1)" >/dev/null 2>&1 || true
}
CONSIGNE=""
consigner_arret() {
    CONSIGNE=1
    git add -A runs diag
    if git commit -qm "T0.4 — validation : arrêt pendant $1" >/dev/null 2>&1; then
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
    # plafond de l'amorce (TERM) : le signal passe au run en cours par son identifiant de processus (R10), qui consigne
    # son arrêt (arret.json) ; puis résultats partiels, traces et poussée, avant le KILL de l'amorce (cinq minutes)
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
    # filet : une sortie en échec que rien n'a consignée (commande en échec sous set -e, erreur imprévue) consigne
    # l'arrêt, verse les traces et pousse ; le code de sortie est conservé
    local code=$?
    if [ "$code" -ne 0 ] && [ -z "$CONSIGNE" ]; then
        trap '' TERM
        journal "sortie imprévue (code $code) pendant $ETAPE" || true
        consigner_arret "$ETAPE (sortie imprévue, code $code)" || true
    fi
    exit "$code"
}
trap sur_sortie EXIT

if [ "$MODE" != jouet ]; then
    nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv | tee -a "$JOURNAL"
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

python -c "import torch; print('torch', torch.__version__, 'cuda', torch.version.cuda, 'disponible', torch.cuda.is_available())" | tee -a "$JOURNAL"
ETAPE="tests"
# sortie standard seule dans tests.txt (lue par P0) ; la sortie d'erreur à part, pour qu'un avertissement de fin de
# processus ne se lise pas comme une dernière ligne
if ! PYTHONPATH=src python -m pytest -q -p no:cacheprovider >"$TRAVAIL/tests.txt" 2>"$TRAVAIL/tests.err"; then
    tail -n 5 "$TRAVAIL/tests.txt" "$TRAVAIL/tests.err" | tee -a "$JOURNAL"
    journal "tests en échec : arrêt"
    consigner_arret "tests"
    exit 1
fi
journal "tests : $(tail -1 "$TRAVAIL/tests.txt")"

if [ "$MODE" = sonde ]; then
    # sonde de mémoire, non décisive : la révision est celle, figée, du préenregistrement scellé v1 (R-033)
    ETAPE="sonde de mémoire"
    R=$(sed -n 's/.*Révision du modèle : `\([0-9a-f]\{40\}\)`.*/\1/p' prereg/T0.4-validation-modele-reel-v1.md | head -1)
    [ -n "$R" ] || { journal "révision introuvable : arrêt"; exit 1; }
    journal "sonde de mémoire : révision $R"
    code=0
    PYTHONPATH=src timeout --signal=TERM --kill-after=2m 40m python -m controle_ia.harnais.sonde_memoire --revision "$R" \
        --sortie "$TRAVAIL/sonde-memoire.json" >"$TRAVAIL/sonde-resume.json" 2>"$TRAVAIL/sonde-memoire.err" || code=$?
    journal "sonde de mémoire : code $code ; $(cat "$TRAVAIL/sonde-resume.json" 2>/dev/null)"
    CONSIGNE=1
    traces "sonde de mémoire"
    if pousser; then journal "branche $BRANCHE poussée"; else journal "poussée impossible : résultats restés sur l'instance"; fi
    exit "$code"
fi

if [ "$MODE" = reel ]; then
    # révision citée par le préenregistrement (jamais la branche courante du dépôt du modèle)
    R=$(sed -n 's/.*Révision du modèle : `\([0-9a-f]\{40\}\)`.*/\1/p' "$PREREG" | head -1)
    [ -n "$R" ] || { journal "révision introuvable dans $PREREG : arrêt"; exit 1; }
    journal "révision du modèle (citée) : $R"
    ARGS=(--revision "$R" --prereg "$PREREG" --sortie-tests "$TRAVAIL/tests.txt")
    SUFFIXE=validation-reelle
else
    ARGS=(--repetition-jouet --sortie-tests "$TRAVAIL/tests.txt")
    SUFFIXE=repetition-jouet
fi
# délai externe par run, figé (R1) : la limite interne est de 2 h 30 (CONFIG_REELLE) ; TERM à 155 minutes, converti en
# arrêt consigné (arret.json), puis KILL cinq minutes plus tard si le processus ne rend pas la main. Le signal vise
# le processus lancé par timeout, par son identifiant (R10).
DELAI=(timeout --signal=TERM --kill-after=5m 155m)

# un run est complet si son résumé existe sans arrêt consigné, même si le délai externe a frappé pendant la fin
# du processus (code 124 après l'écriture du résumé)
complet() { [ -f "diag/$1/resume.json" ] && [ ! -f "diag/$1/arret.json" ]; }
# lancer <base des sorties> <arguments> : le run tourne en arrière-plan sous son délai, et le script l'attend ; ainsi
# un TERM reçu par le script est traité aussitôt (sur_term), et non à la fin du run
lancer() {
    local base=$1 code=0
    shift
    PYTHONPATH=src "${DELAI[@]}" python -m controle_ia.harnais.validation_reelle "$@" \
        >"$TRAVAIL/$base.json" 2>>"$TRAVAIL/$base.err" &
    PID_RUN=$!
    wait "$PID_RUN" || code=$?
    PID_RUN=""
    return "$code"
}

A="$(date -u +%Y%m%d-%H%M%S)-$SUFFIXE"
ETAPE="run A"
journal "run A : $A"
if ! lancer run-A "${ARGS[@]}" --run-id "$A"; then
    if complet "$A"; then
        journal "run A : code non nul, mais résumé écrit sans arrêt consigné : run complet"
    else
        consigner_arret "run A"; exit 1
    fi
fi
git add "runs/$A" "diag/$A"
git commit -qm "T0.4 — validation ($MODE), run A ($A)"
journal "run A terminé : $A"
ETAPE="entre les runs (A complet)"
pousser || journal "poussée du run A impossible : résultats restés sur l'instance"

sleep 1      # deux identifiants distincts même si le run A a duré moins d'une seconde
B="$(date -u +%Y%m%d-%H%M%S)-$SUFFIXE"
ETAPE="run B"
journal "run B (rejeu de $A) : $B"
if ! lancer run-B "${ARGS[@]}" --rejeu-de "$A" --run-id "$B"; then
    if complet "$B" && ls "diag/$B"/comparaison-*.json >/dev/null 2>&1; then
        journal "run B : code non nul, mais résumé et comparaison écrits sans arrêt consigné : run complet"
    else
        consigner_arret "run B"; exit 1
    fi
fi
git add "runs/$B" "diag/$B"
git commit -qm "T0.4 — validation ($MODE), run B ($B), rejeu entre processus de $A"
journal "run B terminé : $B"
ETAPE="fin (A et B complets)"
tee -a "$JOURNAL" <"$TRAVAIL/run-B.json"

journal "fin : A=$A B=$B ; arrêter l'instance par son identifiant (R10)"
traces "fin"
pousser
journal "branche $BRANCHE poussée"
