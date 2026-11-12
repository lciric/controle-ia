#!/bin/bash
# Contre-lecture v10 : refus du mode réel du script v8 (inchangé), lancés sur le fichier synthétique de la répétition
# (copie dans le dossier de travail, 447dc136…) ; jamais sur les données réelles. Pour chaque cas : code, octets écrits sur
# la sortie standard, dernière ligne d'erreur.
# Usage : bash refus_mode_reel_cv10_v1.sh SCRIPT_V8 NPZ EFFECTIFS_DEPOSES DOSSIER_SORTIES
PY=/opt/venv-essaim-sim-v1/bin/python
SCRIPT="$1"; NPZ="$2"; EFF="$3"; W="$4"; mkdir -p "$W"
BON=447dc136dde083f68d1f9899344207bd5b8a6caf56c95b441d1c492dd72cb709
FAUX=0000000000000000000000000000000000000000000000000000000000000000
cas() {
  local nom="$1"; shift
  "$PY" -I -B "$SCRIPT" "$@" > "$W/$nom.out" 2> "$W/$nom.err"; local code=$?
  echo "$nom : code $code ; octets sortie $(wc -c < "$W/$nom.out") ; $(tail -1 "$W/$nom.err")"
}
cas effectifs_sans_empreinte --reel "$NPZ" --effectifs-seulement
cas effectifs_empreinte_vide --reel "$NPZ" --empreinte-attendue "" --effectifs-seulement
cas effectifs_empreinte_fausse --reel "$NPZ" --empreinte-attendue "$FAUX" --effectifs-seulement
cas effectifs_tirages_5 --reel "$NPZ" --empreinte-attendue "$BON" --effectifs-seulement --tirages 5
cas effectifs_bootstrap_300 --reel "$NPZ" --empreinte-attendue "$BON" --effectifs-seulement --bootstrap 300
cas tirages_5 --reel "$NPZ" --empreinte-attendue "$BON" --sondes-reelles 3 --sondes-placebo 2 --commit x --tirages 5
cas bootstrap_300 --reel "$NPZ" --empreinte-attendue "$BON" --sondes-reelles 3 --sondes-placebo 2 --commit x --bootstrap 300
cas sans_commit --reel "$NPZ" --empreinte-attendue "$BON" --sondes-reelles 3 --sondes-placebo 2
cas commit_vide --reel "$NPZ" --empreinte-attendue "$BON" --sondes-reelles 3 --sondes-placebo 2 --commit ""
cas sans_sondes_reelles --reel "$NPZ" --empreinte-attendue "$BON" --sondes-placebo 2 --commit x
cas sans_sondes_placebo --reel "$NPZ" --empreinte-attendue "$BON" --sondes-reelles 3 --commit x
cas effectif_reel_faux --reel "$NPZ" --empreinte-attendue "$BON" --sondes-reelles 30 --sondes-placebo 2 --commit x
cas effectif_placebo_faux --reel "$NPZ" --empreinte-attendue "$BON" --sondes-reelles 3 --sondes-placebo 400 --commit x
cas reel_et_synthetique --reel "$NPZ" --synthetique --empreinte-attendue "$BON" --sondes-reelles 3 --sondes-placebo 2 --commit x
cas effectifs_sain --reel "$NPZ" --empreinte-attendue "$BON" --effectifs-seulement
cmp -s "$W/effectifs_sain.out" "$EFF" && echo "effectifs_sain : identique à l'octet aux effectifs déposés (v10)" || echo "effectifs_sain : DIFFÈRE des effectifs déposés"
