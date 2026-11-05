#!/bin/bash
# Contre-lecture v2 : refus nouveaux de la v2 provoqués sur les entrées réelles. Aucune sortie ne doit rester.
L=/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/lentilles-p3
S=$L/script-v2/comparaison-jlens-logitlens-sondes-p3-v2
D=/home/user/controle-ia-travail/diag/20261019-230011-p3-reel
PY=/home/user/controle-ia-travail/.venv/bin/python
R=$L/relecture-v2/refus-reels-v2
E=$R/entrees; O=$R/sorties
mkdir -p $E $O
head -c 1048576 $L/entrees/lentille-Llama-3.1-8B-Instruct_jacobian_lens.pt > $E/lentille-tronquee.pt
sed 's/^  prompts_fitted: 461$/  prompts_fitted: 460/' $L/entrees/lentille-config.yaml > $E/lentille-config.yaml
grep -c "prompts_fitted: 460" $E/lentille-config.yaml
grep -v ' lentille-config.yaml$' $L/entrees/empreintes-entrees-v2.txt > $E/empreintes-incompletes.txt
sed 's/^79e3e522/00000000/' $L/entrees/empreintes-entrees-v2.txt > $E/empreintes-fausses.txt
python3 - "$S/concepts-sondes-p3-v2.json" "$E/concepts-mot-sans-jeton.json" <<'PYEOF'
import json, sys
d = json.load(open(sys.argv[1])); d["tromperie"] = d["tromperie"] + ["mislead"]
open(sys.argv[2], "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
PYEOF
(cd $E && sha256sum concepts-mot-sans-jeton.json > concepts-mot-sans-jeton.json.sha256)
BASE=(--sondes-json $D/sondes-figees.json --sondes-npz $L/entrees/sondes-figees-legeres.npz
      --desembedding $L/entrees/model-00004-of-00004.safetensors:lm_head.weight
      --norme-finale $L/entrees/model-00004-of-00004.safetensors:model.norm.weight
      --vocabulaire $L/entrees/tokenizer.json)
LENT=$L/entrees/lentille-Llama-3.1-8B-Instruct_jacobian_lens.pt
CFG=$L/entrees/lentille-config.yaml
CON=$S/concepts-sondes-p3-v2.json
cas() { n=$1; shift; echo "== $n"; ( cd /tmp && $PY -I -B $S/comparaison_jlens_logitlens_sondes_p3_v2.py "$@" ) 2>&1 | tail -2; echo "code ${PIPESTATUS[0]}"; }
cas "1 lentille-illisible (.pt tronqué, torch présent)" comparer "${BASE[@]}" --lentille $E/lentille-tronquee.pt --concepts $CON --sortie $O/s1.json
cas "2 lentille-config-discordante" comparer "${BASE[@]}" --lentille $LENT --lentille-config $E/lentille-config.yaml --concepts $CON --sortie $O/s2.json
cas "3 empreinte-attendue-absente" comparer "${BASE[@]}" --lentille $LENT --lentille-config $CFG --concepts $CON --empreintes-attendues $E/empreintes-incompletes.txt --sortie $O/s3.json
cas "4 empreinte-entree (vocabulaire)" comparer "${BASE[@]}" --lentille $LENT --lentille-config $CFG --concepts $CON --empreintes-attendues $E/empreintes-fausses.txt --sortie $O/s4.json
cas "5 mot-sans-jeton (comparer)" comparer "${BASE[@]}" --lentille $LENT --concepts $E/concepts-mot-sans-jeton.json --sortie $O/s5.json
cas "6 mot-sans-jeton (verifier-concepts)" verifier-concepts --vocabulaire $L/entrees/tokenizer.json --concepts $E/concepts-mot-sans-jeton.json
cas "7 empreinte-sondes-npz par option (CLJ-06)" comparer "${BASE[@]}" --sha256-sondes-npz 0000000000000000000000000000000000000000000000000000000000000000 --lentille $LENT --concepts $CON --sortie $O/s7.json
cas "8 un-seul-couple forme fausse" comparer "${BASE[@]}" --un-seul-couple tromperie-difference_moyennes-c15 --lentille $LENT --concepts $CON --sortie $O/s8.json
cas "9 un-seul-couple couche fausse" comparer "${BASE[@]}" --un-seul-couple tromperie-difference_moyennes,23 --lentille $LENT --concepts $CON --sortie $O/s9.json
cas "10 concepts sans sceau" comparer "${BASE[@]}" --lentille $LENT --concepts $E/lentille-config.yaml --sortie $O/s10.json
echo "== sorties laissées :"; ls -A $O; echo "(fin)"
