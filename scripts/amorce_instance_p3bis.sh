#!/usr/bin/env bash
# Amorce de l'instance de calcul de P3-bis (témoin positif planté ; GO-2026-11-02-29), lancement en mode « args ». Copie de
# `scripts/amorce_instance_p3.sh` (0bfaeaa6…) sous un nom neuf (R12), avec ces seuls écarts (texte de P3-bis, brouillon 6,
# « Ce que le code et la chaîne doivent changer », point 5) : script `p3bis_instance.sh` ; **aucun `timeout`** (le plafond
# de 360 minutes de P3 est retiré : « aucun budget de temps qui coupe une étape ») et donc plus de poussée « plafond
# atteint » (celle de P3 poussait les fichiers du run en clair : ils ne partent qu'en second paquet, par le script de
# l'instance) ; dossiers `amorce-depot` et `p3bis`. Une seconde exécution refuse de repartir (dossiers présents, R12) : seule
# la session de pilotage arrête l'instance, par son identifiant (R10).
# Variables passées par --env à la création de l'instance :
#   COMMIT    commit de scellement du préenregistrement de P3-bis
#   GH_TOKEN  jeton GitHub à grain fin, limité au dépôt de travail privé lciric/controle-ia-travail (jamais la copie
#             expurgée publique lciric/controle-ia ; N-016)
#   HF_TOKEN  jeton Hugging Face en lecture (licence Llama 3.1 acceptée sur le compte)
#   BRANCHE   (facultatif) branche de résultats ; défaut calcul/p3bis-<MODE>-v1 ; une branche qui existe déjà arrête
#             avant tout calcul : une relance passe ici une branche nouvelle (…-v2)
# Sortie : journal sur la sortie standard (lu par `vastai logs <identifiant>`, lignes de progression comprises),
# résultats poussés sur la branche ; dernière ligne de l'amorce : « AMORCE … fin, code N ».
# Pour l'essai local seulement : DEPOT_URL, RACINE_AMORCE, MODE=jouet, VENV_EXISTANT, PREREG, PREREG_ABSENT, CONFIG,
# TACHES (transmis au script de P3-bis).
set -uo pipefail
: "${COMMIT:?COMMIT absent}" "${GH_TOKEN:?GH_TOKEN absent}" "${HF_TOKEN:?HF_TOKEN absent}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
RACINE_AMORCE="${RACINE_AMORCE:-/root}"
export HOME="${HOME:-/root}" DEPOT_URL
cd "$RACINE_AMORCE" || exit 1
echo "AMORCE $(date -u +%FT%TZ) : commit $COMMIT"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
if [ -e amorce-depot ] || [ -e p3bis ]; then
    echo "AMORCE : dossiers d'un essai précédent présents (R12) : relancer sur une instance neuve"; exit 1
fi
if ! git -c credential.helper="$AIDE" clone -q "$DEPOT_URL" amorce-depot; then
    echo "AMORCE : clonage impossible (jeton GitHub ?)"; exit 1
fi
if ! git -C amorce-depot checkout -q "$COMMIT"; then
    echo "AMORCE : commit $COMMIT introuvable"; exit 1
fi
T="$RACINE_AMORCE/p3bis"
# aucun plafond de durée : le script de l'instance va au bout de ses étapes ou s'arrête sur une garde
env COMMIT="$COMMIT" TRAVAIL="$T" bash amorce-depot/scripts/p3bis_instance.sh
code=$?
echo "AMORCE $(date -u +%FT%TZ) : fin, code $code"
for f in "$T/journal.txt" "$T/tests.txt" "$T/tests.err"; do
    [ -s "$f" ] && { echo "----- $f"; tail -20 "$f"; }
done
[ -s "$T/run.err" ] && { echo "----- $T/run.err (dernières lignes, hors progression)"; grep -vE '^PROGRES ' "$T/run.err" | tail -15; }
exit $code
