#!/usr/bin/env bash
# Essai à blanc hors ligne de la boucle complète de l'organisme — v1 (rédacteur neuf, Claude Opus 5.5, 7 novembre 2026).
# Commandes jouées telles quelles le 7 novembre 2026 entre 23:28 et 23:43 UTC (journal : journal-essai-a-blanc-v1.md).
# Aucun appel de modèle, aucun réseau, aucune clé ; le dépôt de l'organisme est lu, jamais écrit (`git status` vide après).
# Les sorties complètes (scellées par le code de l'organisme, compagnons `.sha256` compris) sont écrites HORS de l'arbre de
# travail (la consigne interdit tout `.sha256` dans l'arbre) ; seules des copies sans compagnon sont versées sous `sorties/`.
set -u
ORG=/home/user/ideation-organism/orchestrator          # commit 94bfd92, lecture seule
PY=/home/user/controle-ia-travail/.venv/bin/python     # Python 3.13.18, numpy 2.4.6, scipy 1.17.1, pytest 9.1.1
ICI=$(cd "$(dirname "$0")" && pwd)
HORS_ARBRE=${HORS_ARBRE:?"dossier hors de l'arbre pour les sorties scellées, à donner"}
export TMPDIR=${TMPDIR_ESSAI:-$HORS_ARBRE/tmp-essai}
mkdir -p "$TMPDIR" "$ICI/sorties"
cd "$ORG"

# 1. Le vrai bac à sable est demandé : refus attendu sur une machine sans `bwrap` (code 2, aucun repli sur le factice).
{ date -u; "$PY" -I -B demonstrations/tour_ferme_v64.py "$HORS_ARBRE/refus-bac-reel" --etage 1 --a-blanc --graine 20261107 \
    --bac reel --generations 2 2>&1; echo "code=$?"; date -u; } > "$ICI/sorties/refus-bac-reel.txt"

# 2. Toute la boucle, deux générations, fournisseurs simulés (doublures), bac factice demandé explicitement.
nice -n 10 "$PY" -I -B demonstrations/tour_ferme_v64.py "$HORS_ARBRE/v64-factice-g2" --etage 1 --a-blanc --graine 20261107 \
    --bac factice --generations 2 > "$HORS_ARBRE/v64-factice-g2.stdout" 2> "$HORS_ARBRE/v64-factice-g2.stderr"
echo "code=$?" >> "$HORS_ARBRE/v64-factice-g2.stdout"

# 3. Lecture gelée du relevé (programme à part, lecteur v64, lecture v63 inchangée).
"$PY" -I -B demonstrations/lire_tour_ferme_v64.py "$HORS_ARBRE/v64-factice-g2" "$HORS_ARBRE/lecture-v64-factice-g2.json" \
    --releve-sha256 "$(sha256sum "$HORS_ARBRE/v64-factice-g2/tour-ferme-v1-etage1.json" | cut -c1-64)"

# 4. Essais de la boucle fermée et du tour fermé (bac réel déclaré non joué).
POLE_ESSAI_BAC_REEL_NON_JOUE=1 nice -n 10 "$PY" -I -B -m pytest -q -p no:cacheprovider essais/test_tour_ferme_v64.py \
    essais/test_gardes_tour_ferme_v64.py essais/test_v59_boucle_fermee.py essais/test_v57b_cablage_verdict.py \
    > "$HORS_ARBRE/essais-v64-v59.stdout" 2>&1

# 5. Copies sans compagnon dans l'arbre.
cp "$HORS_ARBRE/v64-factice-g2/tour-ferme-v1-etage1.json" "$ICI/sorties/releve-v64-factice-g2-tour-ferme-v1-etage1.json"
cp "$HORS_ARBRE/v64-factice-g2/manifeste.json" "$ICI/sorties/manifeste-v64-factice-g2.json"
cp "$HORS_ARBRE/lecture-v64-factice-g2.json" "$HORS_ARBRE/v64-factice-g2.stdout" "$HORS_ARBRE/v64-factice-g2.stderr" \
   "$HORS_ARBRE/essais-v64-v59.stdout" "$ICI/sorties/"

# 6. Le dessin exact (lois plantées, archive de départ, génération 2) n'a pas de lanceur dans l'organisme (pièces M1 à M6 du
#    journal) : il est joué hors ligne, juge compris, par les deux scripts de puissance du dossier parent.
cd "$ICI/.."
"$PY" -I -B puissance-boucle-reelle-v1.py sorties-puissance-v1/puissance-boucle-reelle-v1-r1000.json \
    --repetitions 1000 --processus 4 --graine 20261107
"$PY" -I -B puissance-boucle-reelle-v1-generation2.py sorties-puissance-v1/puissance-boucle-reelle-v1-generation2-r1000.json \
    --repetitions 1000 --processus 4 --graine 20261107

# 7. Mêmes jugements sous deux interpréteurs (numpy 2.4.6 de l'environnement virtuel, 2.5.3 du système, qui n'a pas scipy :
#    le script n'importe pas l'oracle) : les log W maximaux doivent être égaux à l'octet.
"$PY" -I -B "$ICI/comparer_numpy_v1.py" > "$ICI/sorties/comparaison-numpy-2.4.6.txt"
/usr/bin/python3 -I -B "$ICI/comparer_numpy_v1.py" > "$ICI/sorties/comparaison-numpy-2.5.3.txt"
diff <(cut -d' ' -f2- "$ICI/sorties/comparaison-numpy-2.4.6.txt") <(cut -d' ' -f2- "$ICI/sorties/comparaison-numpy-2.5.3.txt") \
    && echo "jugements égaux à l'octet"
