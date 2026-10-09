#!/usr/bin/env bash
# Amorce de l'instance de calcul pour le pilote 8B de T0.5 (lancement en mode « args », sans accès direct à la machine).
# La commande de lancement l'embarque encodée en base64 ; le conteneur l'exécute au démarrage ; une seconde exécution
# refuse de repartir (dossiers présents, R12) : seule la session de pilotage arrête l'instance, par son identifiant (R10).
# Variables passées par --env à la création de l'instance :
#   COMMIT    commit de scellement du préenregistrement
#   ETUDE     pilote (défaut) ou revalidation (revalidation courte de l'équivalence, P-007, lecture de R-085, avant le pilote)
#   GH_TOKEN  jeton GitHub à grain fin, limité à lciric/controle-ia (contenu en lecture et écriture)
#   HF_TOKEN  jeton Hugging Face en lecture (licences Llama 3.1 et Llama 3.2 acceptées sur le compte)
#   BRANCHE   (facultatif) branche de résultats ; défaut calcul/t05-<ETUDE>-<MODE>-v1. Une branche qui existe déjà sur le
#             dépôt distant arrête avant tout calcul : un relancement passe ici une branche nouvelle (…-v2 ; W-11)
# Sortie : journal sur la sortie standard (lu par `vastai logs <identifiant>`), résultats poussés sur
# calcul/t05-<ETUDE>-<MODE>-v1 (ou sur BRANCHE), vecteurs par action du pilote sur donnees/t05/<run>.
# Pour l'essai local seulement : DEPOT_URL, RACINE_AMORCE, MODE=jouet, VENV_EXISTANT, PREREG, PREREG_ABSENT, CONFIG,
# TACHES (transmis au script du pilote).
set -uo pipefail
: "${COMMIT:?COMMIT absent}" "${GH_TOKEN:?GH_TOKEN absent}" "${HF_TOKEN:?HF_TOKEN absent}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia.git}"
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
# plafond de l'ensemble (mise en place, tests, run, poussées) sous les 5 heures du devis
ETUDE="${ETUDE:-pilote}"
case "$ETUDE" in pilote|revalidation) ;; *) echo "AMORCE : ETUDE=$ETUDE inconnue"; exit 1 ;; esac
timeout --signal=TERM --kill-after=5m 300m env COMMIT="$COMMIT" TRAVAIL="$T" ETUDE="$ETUDE" \
    bash amorce-depot/scripts/pilote_t05_instance.sh
code=$?
echo "AMORCE $(date -u +%FT%TZ) : fin, code $code"
if { [ "$code" -eq 124 ] || [ "$code" -eq 137 ]; } && [ -d "$T/controle-ia/.git" ]; then
    # plafond atteint (124 : TERM ; 137 : KILL cinq minutes plus tard) : le script du pilote a consigné l'arrêt s'il en a
    # eu le temps ; l'amorce verse en plus ses propres traces, au mieux
    (
        cd "$T/controle-ia" && mkdir -p traces && d=$(mktemp -d "traces/t05-plafond-$(date -u +%Y%m%d-%H%M%S)-XXXX") &&
        for f in "$T/journal.txt" "$T/tests.txt" "$T/tests.err" "$T/run.err" "$T/run.json"; do [ -f "$f" ] && cp "$f" "$d/"; done
        (cd "$d" && sha256sum -- * > empreintes.sha256) || true
        git add -A runs diag "$d" && git commit -qm "T0.5 — plafond de l'amorce atteint : résultats partiels et traces" || true
        git push -q origin "${BRANCHE:-calcul/t05-$ETUDE-${MODE:-reel}-v1}" || echo "AMORCE : poussée impossible"
    )
fi
for f in "$T/journal.txt" "$T/tests.txt" "$T/tests.err"; do
    [ -s "$f" ] && { echo "----- $f"; tail -20 "$f"; }
done
[ -s "$T/run.err" ] && { echo "----- $T/run.err (dernières lignes)"; tail -15 "$T/run.err"; }
exit $code
