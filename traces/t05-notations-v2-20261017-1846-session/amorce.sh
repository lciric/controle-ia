#!/usr/bin/env bash
# Amorce de l'instance de calcul pour les notations décisives refaites du pilote de T0.5 (N-021, option (a),
# GO-2026-10-12-02), lancement en mode « args ». Dérivée de `amorce_instance_t05.sh` sous un nom nouveau (R12 : l'amorce
# du pilote, citée par son préenregistrement, n'est pas modifiée) : une seule étude, script `notations_t05_instance.sh`,
# plafond de 430 minutes. Une seconde exécution refuse de repartir (dossiers présents, R12) : seule la session de
# pilotage arrête l'instance, par son identifiant (R10).
# Variables passées par --env à la création de l'instance :
#   COMMIT    commit de scellement du préenregistrement des notations
#   GH_TOKEN  jeton GitHub à grain fin, limité au dépôt de travail privé lciric/controle-ia-travail (jamais la copie
#             expurgée publique lciric/controle-ia ; N-016)
#   HF_TOKEN  jeton Hugging Face en lecture (licences Llama 3.1 et Llama 3.2 acceptées sur le compte)
#   BRANCHE   (facultatif) branche de résultats ; défaut calcul/t05-notations-<MODE>-v1 ; une branche qui existe déjà
#             arrête avant tout calcul : un relancement passe ici une branche nouvelle (…-v2)
# Sortie : journal sur la sortie standard (lu par `vastai logs <identifiant>`, lignes de progression comprises),
# résultats poussés sur la branche.
# Pour l'essai local seulement : DEPOT_URL, RACINE_AMORCE, MODE=jouet, VENV_EXISTANT, PREREG, PREREG_ABSENT, CONFIG,
# TACHES (transmis au script des notations).
set -uo pipefail
: "${COMMIT:?COMMIT absent}" "${GH_TOKEN:?GH_TOKEN absent}" "${HF_TOKEN:?HF_TOKEN absent}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
RACINE_AMORCE="${RACINE_AMORCE:-/root}"
export HOME="${HOME:-/root}" DEPOT_URL
cd "$RACINE_AMORCE" || exit 1
echo "AMORCE $(date -u +%FT%TZ) : commit $COMMIT"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
if [ -e amorce-depot ] || [ -e t05 ]; then
    echo "AMORCE : dossiers d'un essai précédent présents (R12) : relancer sur une instance neuve"; exit 1
fi
if ! git -c credential.helper="$AIDE" clone -q "$DEPOT_URL" amorce-depot; then
    echo "AMORCE : clonage impossible (jeton GitHub ?)"; exit 1
fi
if ! git -C amorce-depot checkout -q "$COMMIT"; then
    echo "AMORCE : commit $COMMIT introuvable"; exit 1
fi
T="$RACINE_AMORCE/t05"
# plafond de l'ensemble (mise en place, tests, run, poussées) : 430 minutes, au-dessus du délai externe du run (400
# minutes) et sous la surveillance de la session
timeout --signal=TERM --kill-after=5m 430m env COMMIT="$COMMIT" TRAVAIL="$T" \
    bash amorce-depot/scripts/notations_t05_instance.sh
code=$?
echo "AMORCE $(date -u +%FT%TZ) : fin, code $code"
if { [ "$code" -eq 124 ] || [ "$code" -eq 137 ]; } && [ -d "$T/controle-ia/.git" ]; then
    (
        cd "$T/controle-ia" && mkdir -p traces && d=$(mktemp -d "traces/t05-notations-plafond-$(date -u +%Y%m%d-%H%M%S)-XXXX") &&
        for f in "$T/journal.txt" "$T/tests.txt" "$T/tests.err" "$T/run.err" "$T/run.json"; do [ -f "$f" ] && cp "$f" "$d/"; done
        (cd "$d" && sha256sum -- * > empreintes.sha256) || true
        git add -A runs diag "$d" && git commit -qm "T0.5 — notations : plafond de l'amorce atteint : résultats partiels et traces" || true
        git push -q origin "${BRANCHE:-calcul/t05-notations-${MODE:-reel}-v1}" || echo "AMORCE : poussée impossible"
    )
fi
for f in "$T/journal.txt" "$T/tests.txt" "$T/tests.err"; do
    [ -s "$f" ] && { echo "----- $f"; tail -20 "$f"; }
done
[ -s "$T/run.err" ] && { echo "----- $T/run.err (dernières lignes, hors progression)"; grep -vE '^PROGRES ' "$T/run.err" | tail -15; }
exit $code
