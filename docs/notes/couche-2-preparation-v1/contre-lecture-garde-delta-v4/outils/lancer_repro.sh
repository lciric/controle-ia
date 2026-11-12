#!/bin/bash
# Reproduction v4 : même graine (20261029) et graine neuve (918273645). Usage : lancer_repro.sh
C=/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/relecture-garde-delta-v4/cl
S=$C/outils/copie_script/sim_garde_v4.py
O=$C/sorties
cd $O
SENS="--repetitions 4000 --sans-n80 --biais 0 --comparateurs 1,3 --tailles 160,400"
( python3 -I -B $S --repetitions 4000 > repro-principale.json 2> repro-principale.err ; echo "principale $?" >> codes.txt ) &
( python3 -I -B $S $SENS --effet-unite-a 0.5 > repro-effet-0.5.json 2> repro-effet-0.5.err ; echo "effet0.5 $?" >> codes.txt
  python3 -I -B $S $SENS --effet-unite-a 1.0 > repro-effet-1.0.json 2> repro-effet-1.0.err ; echo "effet1.0 $?" >> codes.txt
  python3 -I -B $S $SENS --effet-unite-a 0.5 --graine 918273645 > neuve-effet-0.5.json 2> neuve-effet-0.5.err ; echo "neuve0.5 $?" >> codes.txt
  python3 -I -B $S $SENS --effet-unite-a 1.0 --graine 918273645 > neuve-effet-1.0.json 2> neuve-effet-1.0.err ; echo "neuve1.0 $?" >> codes.txt ) &
( python3 -I -B $S --repetitions 4000 --graine 918273645 > neuve-principale.json 2> neuve-principale.err ; echo "neuve-principale $?" >> codes.txt ) &
wait
date -u >> codes.txt
