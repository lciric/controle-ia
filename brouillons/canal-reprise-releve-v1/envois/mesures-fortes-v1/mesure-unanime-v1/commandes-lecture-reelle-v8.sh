#!/bin/bash
# Mesure unanime — la séquence de lecture réelle, telle que le préenregistrement v8 la gèle (section « Plan d'analyse »,
# commandes (1) à (3)), à lancer **après** le scellement de la v8 et le commit qui le porte :
#   bash commandes-lecture-reelle-v8.sh COMMIT_DU_SCELLEMENT
# Répétition générale (CV7-1) sur un fichier synthétique au format réel, **sans toucher aux données** :
#   bash commandes-lecture-reelle-v8.sh REPETITION CHEMIN.npz EMPREINTE N_REELLES N_PLACEBO
#   (les sorties portent le suffixe « -repetition » ; le préenregistrement n'a pas besoin d'être scellé ; aucune lecture réelle)
# Tout s'exécute depuis le dossier du préenregistrement (CV5-5) ; données par chemin absolu ; une seule exécution réelle
# (R1) : le script refuse de relancer si `sortie-reelle-v8.json` existe (R12 : une relance = version nouvelle, dite).
set -euo pipefail
cd "$(dirname "$(readlink -f "$0")")"
COMMIT="${1:?commit du scellement, ou REPETITION}"
PY=/opt/venv-essaim-sim-v1/bin/python
export PYTHONPATH=/home/claude/canal-conv-audit-n04/src
SCRIPT=analyse_fausses_alertes_v8.py
EMP_SCRIPT=$(sha256sum "$SCRIPT" | cut -d' ' -f1)
if [ "$COMMIT" = "REPETITION" ]; then
  DONNEES="${2:?chemin du fichier synthétique}"; EMPREINTE="${3:?empreinte du fichier}"; NR="${4:-3}"; NP="${5:-2}"; SUF="-repetition"; COMMIT="repetition-generale"
  case "$DONNEES" in /home/claude/canal-conv-audit-n04/donnees/*) echo "la répétition ne lit jamais les données réelles" >&2; exit 4;; esac
else
  DONNEES=/home/claude/canal-conv-audit-n04/donnees/20261019-230011-p3-reel/scores-p3.npz
  EMPREINTE=968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf; NR=30; NP=400; SUF=""
  # 0. le préenregistrement v8 doit être scellé, conforme et intact
  $PY -B -c "from controle_ia import prereg; print('préenregistrement v8 scellé, conforme et intact :', prereg.exiger_prereg_scelle('preenregistrement-mesure-unanime-v8.md'))"
  [ -e sortie-reelle-v8.json ] && { echo "sortie-reelle-v8.json existe déjà : une relance est une version nouvelle (R12)" >&2; exit 3; }
fi
sha256sum -c analyse_fausses_alertes_v8.py.sha256 table_m2bis_m4_v8.py.sha256 table-m2bis-m4-v8.json.sha256 lecture_mecanique_v4.py.sha256

# 1. effectifs seulement (E, K par pli, L, longueurs) : aucun taux
$PY -I -B $SCRIPT --reel "$DONNEES" --empreinte-attendue "$EMPREINTE" --effectifs-seulement > "effectifs-reel-v8$SUF.json"
E=$($PY -I -B -c "import json; print(json.load(open('effectifs-reel-v8$SUF.json'))['effectifs']['E'])")
echo "E = $E"
TABLE=table-m2bis-m4-v8.json
if [ "$E" != "60" ]; then
  TABLE="table-m2bis-m4-v8-E${E}$SUF.json"
  $PY -I -B table_m2bis_m4_v8.py --E "$E" --longueurs-json "effectifs-reel-v8$SUF.json" > "$TABLE"
  $PY -B -m controle_ia.scellement sceller "$TABLE"
fi
$PY -B -m controle_ia.scellement sceller "effectifs-reel-v8$SUF.json"

# 2. la lecture réelle, une fois
$PY -I -B $SCRIPT --reel "$DONNEES" --empreinte-attendue "$EMPREINTE" --sondes-reelles "$NR" --sondes-placebo "$NP" --commit "$COMMIT" > "sortie-reelle-v8$SUF.json"
$PY -B -m controle_ia.scellement sceller "sortie-reelle-v8$SUF.json"

# 3. lecture mécanique des seuils gelés, puis note
$PY -I -B lecture_mecanique_v4.py "sortie-reelle-v8$SUF.json" "$TABLE" --empreinte-donnees "$EMPREINTE" --empreinte-script "$EMP_SCRIPT" > "lecture-mecanique-reelle-v8$SUF.json"
$PY -B -m controle_ia.scellement sceller "lecture-mecanique-reelle-v8$SUF.json"
echo "table utilisée : $TABLE"
$PY -I -B -c "
import json; d = json.load(open('lecture-mecanique-reelle-v8$SUF.json'))
print(json.dumps(d['verdicts'], ensure_ascii=False, indent=1)); print(d['ligne_de_lecture']); print('réserves :', d.get('reserves'))"
