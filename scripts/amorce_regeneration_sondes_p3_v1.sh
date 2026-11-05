#!/usr/bin/env bash
# Amorce de l'instance de la régénération des sondes figées de P3 (GO-2026-10-28-11), v1, déclinée de
# `amorce_instance_p3.sh` sous un nom nouveau (R12). Clone le dépôt au commit COMMIT (celui qui porte ce script, le script
# de régénération et la chaîne de l'instance), copie hors du clone le script de régénération et les deux références de
# P3 (fichier léger des sondes figées et résultat `sondes-figees.json`, avec leurs sceaux), puis lance la chaîne de
# l'instance, qui extrait elle-même le commit de P3. Plafond de l'ensemble : 240 minutes. Une seconde exécution refuse de
# repartir (R12) ; seule la session de pilotage arrête l'instance, par son identifiant (R10).
# Variables passées par --env : COMMIT, COMMIT_P3, BRANCHE, GH_TOKEN, HF_TOKEN, DEPOT_URL.
set -uo pipefail
: "${COMMIT:?COMMIT absent}" "${COMMIT_P3:?COMMIT_P3 absent}" "${GH_TOKEN:?GH_TOKEN absent}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
RACINE_AMORCE="${RACINE_AMORCE:-/root}"
RUN_P3=20261019-230011-p3-reel
export HOME="${HOME:-/root}" DEPOT_URL
cd "$RACINE_AMORCE" || exit 1
echo "AMORCE $(date -u +%FT%TZ) : commit $COMMIT ; commit de P3 $COMMIT_P3"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
if [ -e amorce-depot ] || [ -e regen ] || [ -e regeneration ]; then
    echo "AMORCE : dossiers d'un essai précédent présents (R12) : relancer sur une instance neuve"; exit 1
fi
git -c credential.helper="$AIDE" clone -q "$DEPOT_URL" amorce-depot || { echo "AMORCE : clonage impossible"; exit 1; }
git -C amorce-depot checkout -q "$COMMIT" || { echo "AMORCE : commit $COMMIT introuvable"; exit 1; }
mkdir -p regen/ref
cp amorce-depot/scripts/regenerer_sondes_p3_v1.py regen/
(cd regen && sha256sum regenerer_sondes_p3_v1.py > regenerer_sondes_p3_v1.py.sha256)
for f in "donnees/$RUN_P3/sondes-figees-legeres.npz" "diag/$RUN_P3/sondes-figees.json" "runs/$RUN_P3/manifeste.json"; do
    cp "amorce-depot/$f" "amorce-depot/$f.sha256" regen/ref/ || { echo "AMORCE : référence $f absente"; exit 1; }
done
(cd regen/ref && sha256sum -c --quiet sondes-figees-legeres.npz.sha256 sondes-figees.json.sha256 manifeste.json.sha256) \
    || { echo "AMORCE : sceau d'une référence non conforme"; exit 1; }
timeout --signal=TERM --kill-after=5m 240m env COMMIT_P3="$COMMIT_P3" REGEN="$RACINE_AMORCE/regen" \
    TRAVAIL="$RACINE_AMORCE/regeneration" bash amorce-depot/scripts/regeneration_sondes_p3_instance_v1.sh
code=$?
echo "AMORCE $(date -u +%FT%TZ) : fin, code $code"
[ -s "$RACINE_AMORCE/regeneration/journal.txt" ] && { echo "----- journal"; tail -25 "$RACINE_AMORCE/regeneration/journal.txt"; }
exit $code
