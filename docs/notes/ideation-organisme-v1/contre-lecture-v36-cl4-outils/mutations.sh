#!/bin/bash
# CL4 : essais de mutation — chaque mutation réintroduit un défaut ; on regarde si test_v7_ideation échoue.
B=/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad; R=$B/relecture-v36; O=$R/outils-cl4; PY=$B/venv-pole/bin/python
muter(){ nom=$1; fichier=$2; avant=$3; apres=$4
  D=$O/mut/$nom; rm -rf $D; mkdir -p $O/mut; cp -a $R/v36/orchestrateur-pole-v7 $D
  $PY -I - "$D/$fichier" "$avant" "$apres" <<'PYEOF'
import sys
p, a, b = sys.argv[1:4]
t = open(p, encoding="utf-8").read()
assert t.count(a) == 1, ("motif", t.count(a), a)
open(p, "w", encoding="utf-8").write(t.replace(a, b))
PYEOF
  cd $D && env -i PATH=/usr/bin:/bin HOME=/root $PY -B -m unittest essais.test_v7_ideation > $D.txt 2>&1
  echo "$nom : $(tail -1 $D.txt) ($(grep -c '^FAIL:\|^ERROR:' $D.txt) en échec)"; rm -rf $D
}
muter M1-sans-killpg pole/adaptateurs.py "os.killpg(p.pid, signal.SIGKILL)" "p.kill()"
muter M2-proposeur-simule-sur-reel pole/ideation.py "if a is None or (moteur == \"claude-sdk\" and getattr(a, \"nom\", None) != \"commande-externe\"):" "if a is None:"
muter M3-mediane-devenue-moyenne pole/ideation.py "agg = statistics.mean if nj <= 2 else statistics.median" "agg = statistics.mean"
muter M4-sans-attestation-materiau pole/ideation.py "if seconde_passe and proposeurs_externes and materiau_lu:" "if False:"
muter M5-cout-imprime-ignore pole/adaptateurs.py "if objet is not None:  # CL35-02" "if False:  # CL35-02"
muter M6-temoins-externe-ignores pole/ideation.py "lecture[\"lisible_L2_L4\"] = lecture_temoins_tous[\"temoins_ok\"]" "lecture[\"lisible_L2_L4\"] = lecture_course[\"temoins\"][\"temoins_ok\"]"
muter M7-sans-verif-principal pole/ideation.py "    _verifier_adaptateur_principal(adaptateur, moteur, proposeurs, juges)
    juges_externes" "    juges_externes"
muter M8-sceau-attestation-ignore pole/ideation.py "    if not verifier_scelle(chemin):
        raise CourseInterrompue(f\"attestation non scellée" "    if False:
        raise CourseInterrompue(f\"attestation non scellée"
muter M9-bras-moteur-ignore pole/ideation.py "        if moteur_course == \"claude-sdk\" and getattr(a, \"nom\", None) != \"commande-externe\":" "        if False:"
muter M10-description-non-consignee pole/ideation.py "commande_externe=commande_externe or [getattr(a, \"description\", lambda: None)() for _, _, a in juges_externes]," "commande_externe=commande_externe,"
