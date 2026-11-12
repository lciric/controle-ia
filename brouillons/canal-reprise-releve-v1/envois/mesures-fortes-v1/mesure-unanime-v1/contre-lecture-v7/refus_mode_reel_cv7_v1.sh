#!/bin/bash
# Contre-lecture v7 : refus du mode réel, vérifiés en lançant, sur le fichier SYNTHÉTIQUE écrit par le test des gardes
# (jamais sur donnees/). À lancer depuis le dossier du préenregistrement.
S=/tmp/claude-0/-home-claude/c5a45195-121d-5962-9d0a-4896cc046231/scratchpad/contre-lecture-mesure-unanime-v7
NPZ=$S/gardes-cv7/scores-synthetique-gardes.npz
PETIT=$S/gardes-cv7/scores-synthetique-petit.npz
PY="/opt/venv-essaim-sim-v1/bin/python -I -B"
H=$(sha256sum "$NPZ" | cut -d' ' -f1)
HP=$(sha256sum "$PETIT" | cut -d' ' -f1)
essai() {  # $1 = étiquette ; le reste = arguments
  local nom="$1"; shift
  local out; out=$($PY analyse_fausses_alertes_v7.py "$@" 2>&1 >/dev/null | tail -1); local code=${PIPESTATUS[0]}
  echo "[$nom] arguments : $* | dernière ligne d'erreur : ${out:-<aucune>}"
}
essai "effectifs sans empreinte" --reel "$NPZ" --effectifs-seulement
essai "effectifs empreinte vide" --reel "$NPZ" --empreinte-attendue "" --effectifs-seulement
essai "effectifs empreinte fausse" --reel "$NPZ" --empreinte-attendue "$(printf '0%.0s' {1..64})" --effectifs-seulement
essai "effectifs tirages 5" --reel "$NPZ" --empreinte-attendue "$H" --effectifs-seulement --tirages 5
essai "effectifs bootstrap 300" --reel "$NPZ" --empreinte-attendue "$H" --effectifs-seulement --bootstrap 300
essai "réel tirages 5" --reel "$NPZ" --empreinte-attendue "$H" --sondes-reelles 3 --sondes-placebo 2 --commit x --tirages 5
essai "réel bootstrap 300" --reel "$NPZ" --empreinte-attendue "$H" --sondes-reelles 3 --sondes-placebo 2 --commit x --bootstrap 300
essai "réel sans commit" --reel "$NPZ" --empreinte-attendue "$H" --sondes-reelles 3 --sondes-placebo 2
essai "réel commit vide" --reel "$NPZ" --empreinte-attendue "$H" --sondes-reelles 3 --sondes-placebo 2 --commit ""
essai "réel sans sondes placebo" --reel "$NPZ" --empreinte-attendue "$H" --sondes-reelles 3 --commit x
essai "réel sans sondes réelles" --reel "$NPZ" --empreinte-attendue "$H" --sondes-placebo 2 --commit x
essai "réel sans empreinte" --reel "$NPZ" --sondes-reelles 3 --sondes-placebo 2 --commit x
essai "réel effectif réel faux" --reel "$NPZ" --empreinte-attendue "$H" --sondes-reelles 4 --sondes-placebo 2 --commit x
essai "réel effectif placebo faux" --reel "$NPZ" --empreinte-attendue "$H" --sondes-reelles 3 --sondes-placebo 1 --commit x
essai "réel et synthétique" --reel "$NPZ" --synthetique --empreinte-attendue "$H"
essai "effectifs E = 40" --reel "$PETIT" --empreinte-attendue "$HP" --effectifs-seulement
echo "--- passe : effectifs seulement, défauts écrits explicitement"
$PY analyse_fausses_alertes_v7.py --reel "$NPZ" --empreinte-attendue "$H" --effectifs-seulement --tirages 20 --bootstrap 2000 > $S/sortie-effectifs-synthetique-v7.json; echo "code de sortie : $?"
cat $S/sortie-effectifs-synthetique-v7.json | $PY -c "import json,sys; d=json.load(sys.stdin)['effectifs']; print({k: v for k, v in d.items() if k != 'actions_valides_par_episode'}); print('longueurs :', len(d['actions_valides_par_episode']))"
echo "empreinte attendue des données : $H"
echo "empreinte du script v7 sur disque : $(sha256sum analyse_fausses_alertes_v7.py | cut -d' ' -f1)"
