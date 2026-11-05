#!/bin/sh
# Contre-lecture GD6 (R2) : rejeu du script v6 de conv-audit sur un sous-ensemble, processeur seul.
# Usage : sh rejeu-v6-sous-ensemble.sh CHEMIN_DU_SCRIPT_V6 DOSSIER_DE_SORTIE
# Le script v6 est lancé tel quel (copie extraite du canal, empreinte vérifiée avant), en mode isolé (-I -B).
# Graines : le script v6 dérive chaque cellule par SeedSequence([graine, sha256(étiquette)]) (R9) ; graine maîtresse
# 20261029 (celle de l'auteur, pour l'identité des cellules communes) et graines neuves 61029917, 61029918.
set -u
S="$1"; O="$2"
PY="python3 -I -B $S"
SOUS="--repetitions 2000 --comparateurs 8 --taux 0.01 --deltas 0.05 --biais 0,0.0125 --tailles 288 --lecture-ebh A --m 8,2 --sans-n80"
date -u
# (a) même graine que l'auteur : les cellules K_h = 10 et 5, 288 unités, doivent être identiques à celles de ses sorties
$PY $SOUS --K 10,5 --graine 20261029 --sortie "$O/rejeu-meme-graine-sigma0.json"; echo "a sigma0 : code $?"
$PY $SOUS --K 10,5 --graine 20261029 --effet-unite-comparateurs 1.0 --sortie "$O/rejeu-meme-graine-sigma1.json"; echo "a sigma1 : code $?"
# (b) graine neuve
$PY $SOUS --K 10,5 --graine 61029917 --sortie "$O/rejeu-graine-neuve-sigma0.json"; echo "b sigma0 : code $?"
$PY $SOUS --K 10,5 --graine 61029917 --effet-unite-comparateurs 1.0 --sortie "$O/rejeu-graine-neuve-sigma1.json"; echo "b sigma1 : code $?"
# (c) K_s différent de K_h (paires zippées : (K_h, K_s) = (10, 5) et (5, 10)), graine neuve
$PY $SOUS --K 10,5 --K-sabotes 5,10 --graine 61029918 --sortie "$O/ks-different-sigma0.json"; echo "c sigma0 : code $?"
$PY $SOUS --K 10,5 --K-sabotes 5,10 --graine 61029918 --effet-unite-comparateurs 1.0 --sortie "$O/ks-different-sigma1.json"; echo "c sigma1 : code $?"
date -u
