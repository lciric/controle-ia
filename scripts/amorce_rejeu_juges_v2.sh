#!/usr/bin/env bash
# Amorce de l'instance du rejeu de la cellule de juge redéfinie (GO-2026-10-29-04), v2, copie adaptée de
# `amorce_rejeu_juges_v1.sh` sous un nom nouveau (R12 : la v1 n'est pas modifiée). Clone le dépôt
# au commit COMMIT (celui qui scelle la fiche de lancement, le devis et la configuration), puis lance la chaîne de
# l'instance `rejeu_juges_instance_v2.sh` sous un plafond de 120 minutes (TERM, puis KILL cinq minutes plus tard) ; le
# script de l'instance reçoit l'horodatage de ce plafond et borne le délai de son run en conséquence. Une seconde
# exécution refuse de repartir (R12) ; seule la session de pilotage arrête l'instance, par son identifiant (R10).
# Variables passées par --env à la création de l'instance (jamais affichées) :
#   COMMIT    commit de scellement de la fiche de lancement
#   GH_TOKEN  jeton GitHub à grain fin, limité au dépôt de travail privé lciric/controle-ia-travail (jamais la copie
#             expurgée publique lciric/controle-ia ; N-016)
#   HF_TOKEN  jeton Hugging Face en lecture (licences Llama 3.1 et Llama 3.2 acceptées sur le compte)
#   BRANCHE   (facultatif) défaut calcul/rejeu-juges-v2 ; une branche qui existe déjà arrête avant tout calcul
#   DEPOT_URL (facultatif) défaut https://github.com/lciric/controle-ia-travail.git
# Pour l'essai local seulement : RACINE_AMORCE, PLAFOND_MIN, et les variables du script de l'instance (MODE=jouet,
# VENV_EXISTANT, PREREG_ABSENT, CONFIG, TACHES, TESTS_ATTENDUS, SAUTER_TESTS), transmises telles quelles.
set -uo pipefail
: "${COMMIT:?COMMIT absent}" "${GH_TOKEN:?GH_TOKEN absent}" "${HF_TOKEN:?HF_TOKEN absent}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
BRANCHE="${BRANCHE:-calcul/rejeu-juges-v2}"
RACINE_AMORCE="${RACINE_AMORCE:-/root}"
PLAFOND_MIN="${PLAFOND_MIN:-120}"
[[ "$PLAFOND_MIN" =~ ^[0-9]+$ ]] && [ "$PLAFOND_MIN" -le 120 ] || { echo "AMORCE : PLAFOND_MIN entier ≤ 120 attendu"; exit 1; }
export HOME="${HOME:-/root}" DEPOT_URL BRANCHE
cd "$RACINE_AMORCE" || exit 1
echo "AMORCE $(date -u +%FT%TZ) : commit $COMMIT ; branche $BRANCHE ; plafond $PLAFOND_MIN minutes"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
if [ -e amorce-depot ] || [ -e rejeu ]; then
    echo "AMORCE : dossiers d'un essai précédent présents (R12) : relancer sur une instance neuve"; exit 1
fi
git -c credential.helper="$AIDE" clone -q "$DEPOT_URL" amorce-depot || { echo "AMORCE : clonage impossible (jeton GitHub ?)"; exit 1; }
git -C amorce-depot checkout -q "$COMMIT" || { echo "AMORCE : commit $COMMIT introuvable"; exit 1; }
[ -f amorce-depot/scripts/rejeu_juges_instance_v2.sh ] || { echo "AMORCE : script de l'instance absent du commit"; exit 1; }
T="$RACINE_AMORCE/rejeu"
ECHEANCE=$(( $(date -u +%s) + PLAFOND_MIN * 60 ))
timeout --signal=TERM --kill-after=5m "${PLAFOND_MIN}m" env COMMIT="$COMMIT" TRAVAIL="$T" ECHEANCE_AMORCE="$ECHEANCE" \
    bash amorce-depot/scripts/rejeu_juges_instance_v2.sh
code=$?
echo "AMORCE $(date -u +%FT%TZ) : fin, code $code"
# KILL après le plafond (le script n'a pas pu consigner) : résultats partiels et traces poussés d'ici, si le clone existe
if [ "$code" -eq 137 ] && [ -d "$T/controle-ia/.git" ]; then
    (
        cd "$T/controle-ia" && mkdir -p traces && d=$(mktemp -d "traces/rejeu-juges-v2-plafond-$(date -u +%Y%m%d-%H%M%S)-XXXX") &&
        for f in "$T/journal.txt" "$T/tests.txt" "$T/tests.err" "$T/run.err" "$T/run.json"; do [ -f "$f" ] && cp "$f" "$d/"; done
        (cd "$d" && sha256sum -- * > empreintes.sha256) || true
        git add -A runs diag "$d" && git commit -qm "Rejeu des juges v2 : plafond de l'amorce atteint (KILL) : résultats partiels et traces" || true
        git push -q origin "$BRANCHE" || echo "AMORCE : poussée impossible"
    )
fi
for f in "$T/journal.txt" "$T/tests.txt" "$T/tests.err"; do
    [ -s "$f" ] && { echo "----- $f"; tail -20 "$f"; }
done
[ -s "$T/run.err" ] && { echo "----- $T/run.err (dernières lignes, hors progression)"; grep -vE '^PROGRES ' "$T/run.err" | tail -15; }
exit $code
