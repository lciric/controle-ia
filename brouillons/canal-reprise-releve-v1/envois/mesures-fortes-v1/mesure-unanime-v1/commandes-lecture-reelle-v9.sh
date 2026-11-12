#!/bin/bash
# Mesure unanime — la séquence de lecture réelle, telle que le préenregistrement v9 la gèle (section « Plan d'analyse »,
# commandes (1) à (4)), à lancer **après** le scellement de la v9 et le commit qui le porte :
#   nohup bash commandes-lecture-reelle-v9.sh COMMIT_DU_SCELLEMENT > journal-lecture-reelle-v9.log 2>&1 &
# **Durée** (CV8-1) : l'étape (2) prend environ 30 minutes de processeur avec 430 sondes (20 tirages, 2 000 rééchantillonnages),
# plus environ 10 minutes pour la table si E ≠ 60 : lancer en arrière-plan, jamais au premier plan d'un appel borné.
# La sortie réelle est écrite dans un fichier **temporaire** (`.partiel`) renommé à la fin : un lancement interrompu ne laisse
# jamais un `sortie-reelle-v9.json` vide. S'il existe un `.partiel` au départ, l'exécution précédente a été interrompue : le
# script s'arrête ; l'auteur renomme le `.partiel` en `sortie-reelle-v9-interrompue-N.json.partiel`, le consigne dans la note
# et la passation, et **la relance est une version nouvelle** du préenregistrement (R12), dite — pas une seconde exécution v9.
# Répétition générale sur un fichier synthétique au format réel, **sans toucher aux données** :
#   bash commandes-lecture-reelle-v9.sh REPETITION CHEMIN.npz EMPREINTE N_REELLES N_PLACEBO
# Tout s'exécute depuis le dossier du préenregistrement (CV5-5) ; données par chemin absolu.
set -euo pipefail
cd "$(dirname "$(readlink -f "$0")")"
COMMIT="${1:?commit du scellement, ou REPETITION}"
PY=/opt/venv-essaim-sim-v1/bin/python
export PYTHONPATH=/home/claude/canal-conv-audit-n04/src
SCRIPT=analyse_fausses_alertes_v8.py
PREREG=preenregistrement-mesure-unanime-v9.md
EMP_SCRIPT=$(sha256sum "$SCRIPT" | cut -d' ' -f1)
if [ "$COMMIT" = "REPETITION" ]; then
  DONNEES="${2:?chemin du fichier synthétique}"; EMPREINTE="${3:?empreinte du fichier}"; NR="${4:-3}"; NP="${5:-2}"; SUF="-repetition"; COMMIT="repetition-generale"
  case "$DONNEES" in /home/claude/canal-conv-audit-n04/donnees/*) echo "la répétition ne lit jamais les données réelles" >&2; exit 4;; esac
else
  DONNEES=/home/claude/canal-conv-audit-n04/donnees/20261019-230011-p3-reel/scores-p3.npz
  EMPREINTE=968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf; NR=30; NP=400; SUF=""
  # 0. le préenregistrement v9 doit être scellé, conforme et intact ; une seule exécution réelle
  $PY -B -c "from controle_ia import prereg; print('préenregistrement v9 scellé, conforme et intact :', prereg.exiger_prereg_scelle('$PREREG'))"
  [ -e sortie-reelle-v9.json ] && { echo "sortie-reelle-v9.json existe déjà : une relance est une version nouvelle (R12)" >&2; exit 3; }
  [ -e sortie-reelle-v9.json.partiel ] && { echo "sortie-reelle-v9.json.partiel existe : l'exécution précédente a été interrompue ; la renommer -interrompue-N, la consigner ; la relance est une version nouvelle (R12)" >&2; exit 5; }
fi
# compagnons de tout ce qui sert (CV8-5 : le script de séquence et la rédaction compris)
sha256sum -c analyse_fausses_alertes_v8.py.sha256 table_m2bis_m4_v8.py.sha256 table-m2bis-m4-v8.json.sha256 lecture_mecanique_v5.py.sha256 rediger_note_lecture_v3.py.sha256 commandes-lecture-reelle-v9.sh.sha256

# 1. effectifs seulement (E, K par pli, L, longueurs) : aucun taux
$PY -I -B $SCRIPT --reel "$DONNEES" --empreinte-attendue "$EMPREINTE" --effectifs-seulement > "effectifs-reel-v9$SUF.json"
E=$($PY -I -B -c "import json; print(json.load(open('effectifs-reel-v9$SUF.json'))['effectifs']['E'])")
echo "E = $E ($(date -u +%H:%M:%S) UTC)"
TABLE=table-m2bis-m4-v8.json
if [ "$E" != "60" ]; then
  TABLE="table-m2bis-m4-v8-E${E}$SUF.json"
  $PY -I -B table_m2bis_m4_v8.py --E "$E" --longueurs-json "effectifs-reel-v9$SUF.json" > "$TABLE.partiel"
  mv "$TABLE.partiel" "$TABLE"
  $PY -B -m controle_ia.scellement sceller "$TABLE"
fi
$PY -B -m controle_ia.scellement sceller "effectifs-reel-v9$SUF.json"

# 2. la lecture réelle, une fois (fichier temporaire renommé à la fin, CV8-1)
echo "étape (2) lancée à $(date -u +%H:%M:%S) UTC (≈ 30 minutes avec 430 sondes)"
$PY -I -B $SCRIPT --reel "$DONNEES" --empreinte-attendue "$EMPREINTE" --sondes-reelles "$NR" --sondes-placebo "$NP" --commit "$COMMIT" > "sortie-reelle-v9$SUF.json.partiel"
mv "sortie-reelle-v9$SUF.json.partiel" "sortie-reelle-v9$SUF.json"
$PY -B -m controle_ia.scellement sceller "sortie-reelle-v9$SUF.json"
echo "étape (2) finie à $(date -u +%H:%M:%S) UTC"

# 3. lecture mécanique des seuils gelés
$PY -I -B lecture_mecanique_v5.py "sortie-reelle-v9$SUF.json" "$TABLE" --empreinte-donnees "$EMPREINTE" --empreinte-script "$EMP_SCRIPT" > "lecture-mecanique-reelle-v9$SUF.json"
$PY -B -m controle_ia.scellement sceller "lecture-mecanique-reelle-v9$SUF.json"

# 4. rédaction mécanique de la note (l'auteur n'y ajoute ensuite que ses réserves, à la main, sous le titre prévu)
HEURE=$(date -u +%H:%M:%S)
$PY -I -B rediger_note_lecture_v3.py "lecture-mecanique-reelle-v9$SUF.json" "sortie-reelle-v9$SUF.json" --prereg "$PREREG" --commit "$COMMIT" --heure "$HEURE" --table "$TABLE" > "note-lecture-mecanique-v9$SUF.md"
echo "table utilisée : $TABLE ; note : note-lecture-mecanique-v9$SUF.md"
$PY -I -B -c "
import json; d = json.load(open('lecture-mecanique-reelle-v9$SUF.json'))
print(json.dumps(d['verdicts'], ensure_ascii=False, indent=1)); print(d['ligne_de_lecture']); print('réserves :', d.get('reserves'))"
