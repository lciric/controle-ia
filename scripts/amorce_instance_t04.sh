#!/usr/bin/env bash
# Amorce de l'instance de calcul pour la validation de T0.4 (lancement en mode « args », sans accès direct à la machine).
# La commande de lancement l'embarque encodée en base64 ; le conteneur l'exécute au démarrage et, à sa sortie, la relance :
# seule la session de pilotage arrête l'instance, par son identifiant (R10).
# Variables passées par --env à la création de l'instance (ou au niveau du compte de location) :
#   COMMIT    commit de scellement du préenregistrement
#   GH_TOKEN  jeton GitHub à grain fin, limité à lciric/controle-ia (contenu en lecture et écriture)
#   HF_TOKEN  jeton Hugging Face en lecture (licence Llama 3.1 acceptée sur le compte)
# Sortie : journal sur la sortie standard (lu par `vastai logs <identifiant>`), résultats poussés sur calcul/t04-validation-v3
# (ou sur BRANCHE).
# Pour l'essai local seulement : DEPOT_URL, RACINE_AMORCE, MODE=jouet, VENV_EXISTANT (transmis au script de validation).
set -uo pipefail
: "${COMMIT:?COMMIT absent}" "${GH_TOKEN:?GH_TOKEN absent}" "${HF_TOKEN:?HF_TOKEN absent}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia.git}"
RACINE_AMORCE="${RACINE_AMORCE:-/root}"
export HOME="${HOME:-/root}" DEPOT_URL
cd "$RACINE_AMORCE" || exit 1
echo "AMORCE $(date -u +%FT%TZ) : commit $COMMIT"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
if [ -e amorce-depot ] || [ -e t04 ]; then
    echo "AMORCE : dossiers d'un essai précédent présents (R12) : relancer sur une instance neuve"; exit 1
fi
if ! git -c credential.helper="$AIDE" clone -q "$DEPOT_URL" amorce-depot; then
    echo "AMORCE : clonage impossible (jeton GitHub ?)"; exit 1
fi
if ! git -C amorce-depot checkout -q "$COMMIT"; then
    echo "AMORCE : commit $COMMIT introuvable"; exit 1
fi
T="$RACINE_AMORCE/t04"
# plafond de l'ensemble (mise en place, tests, runs A et B) sous les 6 heures du devis
timeout --signal=TERM --kill-after=5m 345m env COMMIT="$COMMIT" TRAVAIL="$T" bash amorce-depot/scripts/validation_t04_instance.sh
code=$?
echo "AMORCE $(date -u +%FT%TZ) : fin, code $code"
if { [ "$code" -eq 124 ] || [ "$code" -eq 137 ]; } && [ -d "$T/controle-ia/.git" ]; then
    # plafond atteint (124 : TERM ; 137 : KILL cinq minutes plus tard) : le script d'instance a consigné l'arrêt s'il en a
    # eu le temps ; l'amorce verse en plus ses propres traces, au mieux
    (
        cd "$T/controle-ia" && mkdir -p traces && d=$(mktemp -d "traces/t04-plafond-$(date -u +%Y%m%d-%H%M%S)-XXXX") &&
        for f in "$T/journal.txt" "$T/tests.txt" "$T/tests.err" "$T"/run-*.err "$T"/run-*.json; do [ -f "$f" ] && cp "$f" "$d/"; done
        (cd "$d" && sha256sum -- * > empreintes.sha256) || true
        git add -A runs diag "$d" && git commit -qm "T0.4 — plafond de l'amorce atteint : résultats partiels et traces" || true
        git push -q origin "${BRANCHE:-calcul/t04-validation-v3}" || echo "AMORCE : poussée impossible"
    )
fi
for f in "$T/journal.txt" "$T/tests.txt" "$T/tests.err"; do
    [ -s "$f" ] && { echo "----- $f"; tail -20 "$f"; }
done
for f in "$T/run-A.err" "$T/run-B.err"; do
    [ -s "$f" ] && { echo "----- $f (dernières lignes)"; tail -15 "$f"; }
done
exit $code
