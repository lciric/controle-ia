#!/bin/bash
# Mesure unanime — la séquence de lecture réelle, telle que le préenregistrement v6 la gèle (section « Plan d'analyse »,
# commandes (1) à (3)), à lancer **après** le scellement de la v6 et le commit qui le porte. Usage :
#   bash commandes-lecture-reelle-v6.sh COMMIT_DU_SCELLEMENT
# Tout s'exécute depuis le dossier du préenregistrement (CV5-5) ; données par chemin absolu ; une seule exécution réelle
# (R1) : le script refuse de relancer si `sortie-reelle-v6.json` existe (R12 : une relance = version nouvelle, dite).
set -euo pipefail
cd "$(dirname "$(readlink -f "$0")")"
COMMIT="${1:?commit du scellement obligatoire}"
PY=/opt/venv-essaim-sim-v1/bin/python
DONNEES=/home/claude/canal-conv-audit-n04/donnees/20261019-230011-p3-reel/scores-p3.npz
EMPREINTE=968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf
export PYTHONPATH=/home/claude/canal-conv-audit-n04/src

# 0. le préenregistrement v6 doit être scellé et intact
$PY -B -c "from controle_ia import prereg; print('préenregistrement v6 scellé, conforme et intact :', prereg.exiger_prereg_scelle('preenregistrement-mesure-unanime-v6.md'))"
[ -e sortie-reelle-v6.json ] && { echo "sortie-reelle-v6.json existe déjà : une relance est une version nouvelle (R12)" >&2; exit 3; }
sha256sum -c analyse_fausses_alertes_v6.py.sha256 table_m2bis_m4_v6.py.sha256 table-m2bis-m4-v6.json.sha256 lecture_mecanique_v2.py.sha256

# 1. effectifs seulement (E, K par pli, L, longueurs) : aucun taux
$PY -I -B analyse_fausses_alertes_v6.py --reel "$DONNEES" --empreinte-attendue "$EMPREINTE" --effectifs-seulement > effectifs-reel-v6.json
E=$($PY -I -B -c "import json; print(json.load(open('effectifs-reel-v6.json'))['effectifs']['E'])")
echo "E = $E"
TABLE=table-m2bis-m4-v6.json
if [ "$E" != "60" ]; then
  TABLE="table-m2bis-m4-v6-E${E}.json"
  $PY -I -B table_m2bis_m4_v6.py --E "$E" --longueurs-json effectifs-reel-v6.json > "$TABLE"
  $PY -B -m controle_ia.scellement sceller "$TABLE"
fi
$PY -B -m controle_ia.scellement sceller effectifs-reel-v6.json

# 2. la lecture réelle, une fois
$PY -I -B analyse_fausses_alertes_v6.py --reel "$DONNEES" --empreinte-attendue "$EMPREINTE" --sondes-reelles 30 --sondes-placebo 400 --commit "$COMMIT" > sortie-reelle-v6.json
$PY -B -m controle_ia.scellement sceller sortie-reelle-v6.json

# 3. lecture mécanique des seuils gelés
$PY -I -B lecture_mecanique_v2.py sortie-reelle-v6.json "$TABLE" > lecture-mecanique-reelle-v6.json
$PY -B -m controle_ia.scellement sceller lecture-mecanique-reelle-v6.json
echo "table utilisée : $TABLE"
$PY -I -B -c "
import json; d = json.load(open('lecture-mecanique-reelle-v6.json'))
print(json.dumps(d['verdicts'], ensure_ascii=False, indent=1)); print(d['ligne_de_lecture']); print('réserves :', d.get('reserves'))"
