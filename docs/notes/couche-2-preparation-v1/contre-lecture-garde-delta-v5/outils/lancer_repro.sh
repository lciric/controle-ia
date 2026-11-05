#!/bin/bash
# Reproduction des passages v5 (même graine) et graine neuve 918273645. Script : copie conforme 7d1239e1…
CL=/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/relecture-garde-delta-v5/cl
S=$CL/outils/copie_script/sim_garde_v5.py
cd $CL/sorties
quoi=$1
case $quoi in
 principale) python3 -I -B $S --repetitions 2000 --comparateurs 1,3,8 --tailles 160,300,400,650 --K 10,3 --taux 0.01 --biais 0,0.0125 --deltas 0.05,0.075 --lecture-ebh A,B --m 8,2,16 --sans-n80 --sortie repro/principale.json ;;
 nulles) python3 -I -B $S --repetitions 2000 --comparateurs 8 --tailles 160,400,650 --K 10,3 --taux 0.01 --biais 0 --deltas 0.05,0.075 --lecture-ebh A,B --fiches-nulles 2 --m 8,4,18 --sans-n80 --sortie repro/fiches-nulles-2.json ;;
 taux) python3 -I -B $S --repetitions 2000 --comparateurs 8 --tailles 160,400,650 --K 10,3 --taux 0.10 --biais 0,0.0125 --deltas 0.05,0.075 --lecture-ebh A,B --m 8,2,16 --sans-n80 --sortie repro/taux-0.10.json ;;
 rejeu) python3 -I -B $S --repetitions 4000 --sortie repro/rejeu-v4-principale.json ;;
 beta) python3 -I -B $S --repetitions 4000 --sans-n80 --effet-unite-beta 0.17 --biais 0 --comparateurs 1,3,8 --tailles 160,400 --sortie repro/effet-beta-0.17.json ;;
 effet1) python3 -I -B $S --repetitions 4000 --sans-n80 --effet-unite-a 1.0 --biais 0 --comparateurs 1,3,8 --tailles 160,400 --lien-coupe --sortie repro/effet-unite-1.0.json ;;
 neuve-principale) python3 -I -B $S --graine 918273645 --repetitions 2000 --comparateurs 1,3,8 --tailles 160,300,400,650 --K 10,3 --taux 0.01 --biais 0,0.0125 --deltas 0.05,0.075 --lecture-ebh A,B --m 8,2,16 --sans-n80 --sortie neuve/principale.json ;;
 neuve-nulles) python3 -I -B $S --graine 918273645 --repetitions 2000 --comparateurs 8 --tailles 160,400,650 --K 10,3 --taux 0.01 --biais 0 --deltas 0.05,0.075 --lecture-ebh A,B --fiches-nulles 2 --m 8,4,18 --sans-n80 --sortie neuve/fiches-nulles-2.json ;;
 effet1-ebh) python3 -I -B $S --repetitions 2000 --comparateurs 8 --tailles 160,400,650 --K 10,3 --taux 0.01 --biais 0 --deltas 0.05 --lecture-ebh A,B --m 8,2,16 --sans-n80 --effet-unite-a 1.0 --lien-coupe --sortie doutes-script/effet-unite-1.0-ebh-k8.json ;;
 beta-ebh) python3 -I -B $S --repetitions 2000 --comparateurs 8 --tailles 160,400,650 --K 10,3 --taux 0.01 --biais 0 --deltas 0.05 --lecture-ebh A,B --m 8,2,16 --sans-n80 --effet-unite-beta 0.17 --sortie doutes-script/effet-beta-0.17-ebh-k8.json ;;
 alpha025) python3 -I -B $S --repetitions 2000 --comparateurs 8 --tailles 160,300,400,650 --K 10,3 --taux 0.01 --biais 0,0.0125 --deltas 0.05 --alpha 0.025 --lecture-ebh A,B --m 8,2,16 --sans-n80 --sortie doutes-script/alpha-0.025-ebh-k8.json ;;
esac
echo "$quoi code $?" >> $CL/sorties/codes.txt
