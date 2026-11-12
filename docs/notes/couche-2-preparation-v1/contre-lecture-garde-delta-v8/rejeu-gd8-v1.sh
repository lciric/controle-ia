#!/bin/sh
# Contre-lecture GD8 (R2) — rejeu de quatre passages de la simulation de puissance de la garde δ, v8.
# Usage : sh rejeu-gd8-v1.sh DOSSIER_DE_TRAVAIL PYTHON NOM
#   DOSSIER_DE_TRAVAIL contient une copie du script simulation-puissance-garde-delta-v8.py (sha256 4c7c93a9…, vérifiée ici).
#   NOM ∈ meme-rho0.17 | meme-rho0.10 | neuf-k9-g0.05-nulle | neuf-k9-g0.05-rho0.17
# Mêmes options que lancer-passages-v8.sh (voie1, voie2, voie3), même graine maîtresse 20261029 (défaut du script) ;
# les graines sont dérivées par le script : SeedSequence([20261029, sha256(étiquette)]) (R9). Sortie, journal et manifeste
# écrits par le script lui-même (--sortie), nom préfixé « rejeu-gd8- » ; aucune sortie existante écrasée (le script refuse).
# Aucune commande git (GD7-09) ; processeur seul, sans dépense.
set -eu
W=$1; PY=$2; NOM=$3
S=simulation-puissance-garde-delta-v8
cd "$W"
echo "4c7c93a90e0be922e839f5826488edcc0745bde17f8a5de22f3a2a41bf75f1d1  $S.py" | sha256sum -c -
COMMIT="contre-lecture GD8 : script extrait de origin/canal/conv-audit-n04 par git archive, empreinte 4c7c93a9 vérifiée ; commit non lu par le script"
COMMUN="--repetitions 2000 --taux 0.01 --deltas 0.05 --biais 0,0.0125 --lecture-ebh A --m 8,2 --sans-n80"
TAILLES4="--tailles 288,400,500,650"
N80="--n80-fiche --cibles-n80 0.8,0.9"
COMB="--echelle-dispersion beta --combiner-dispersion-a-et-comparateurs"
R1="--comparateurs 8 --K 10,5 --K-s 10 $TAILLES4 $N80"
N9="--comparateurs 9 --K 10,5 --K-s 10 $TAILLES4 --n80-fiche"
case "$NOM" in
  meme-rho0.17) OPT="$R1 $COMB --effet-unite-beta 0.17 --rho-comparateurs 0.17" ;;
  meme-rho0.10) OPT="$R1 $COMB --effet-unite-beta 0.10 --rho-comparateurs 0.10" ;;
  neuf-k9-g0.05-nulle) OPT="$N9 --ecart-contraste-neuvieme 0.05" ;;
  neuf-k9-g0.05-rho0.17) OPT="$N9 --ecart-contraste-neuvieme 0.05 $COMB --effet-unite-beta 0.17 --rho-comparateurs 0.17" ;;
  *) echo "nom inconnu : $NOM"; exit 2 ;;
esac
# shellcheck disable=SC2086
$PY -I -B $S.py $COMMUN --commit-declare "$COMMIT" $OPT --sortie rejeu-gd8-$NOM.json
echo "$NOM : code $?"
