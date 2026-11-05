#!/bin/bash
cd /tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/relecture-garde-delta-v3/cl/sorties
S=/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/relecture-garde-delta-v3/cl/outils/copie_script/sim_garde_v3.py
python3 -I -B $S --repetitions 4000 > repro-principale.json 2> repro-principale.err &
python3 -I -B $S --repetitions 4000 --sans-n80 --effet-unite-a 0.05 --biais 0 --comparateurs 1,3 > repro-effet-unite.json 2> repro-effet-unite.err &
python3 -I -B $S --repetitions 4000 --sans-n80 --comparateurs-independants --biais 0 --comparateurs 3 --tailles 160 > repro-independants.json 2> repro-independants.err &
python3 -I -B $S --repetitions 4000 --graine 918273645 > neuve-principale.json 2> neuve-principale.err &
wait
python3 -I -B $S --repetitions 4000 --sans-n80 --effet-unite-a 0.05 --biais 0 --comparateurs 1,3 --graine 918273645 > neuve-effet-unite.json 2> neuve-effet-unite.err &
python3 -I -B $S --repetitions 4000 --sans-n80 --comparateurs-independants --biais 0 --comparateurs 3 --tailles 160 --graine 918273645 > neuve-independants.json 2> neuve-independants.err &
wait
date -u > fin-repro.txt
