#!/usr/bin/env bash
# Cas C du banc : TERM envoyé, par PID (R10), au processus « timeout » de l'amorce (comme au plafond) pendant le run.
S=/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/relecture-rejeu-v2
B=$S/banc
$S/outils/banc_amorce.sh C 60 BRANCHE=calcul/rejeu-juges-v2-c &
PID_BANC=$!
J=$B/racine-C/rejeu/journal.txt
for i in $(seq 1 600); do grep -q "^PROGRES .*lot=1/2" "$J" 2>/dev/null && break; sleep 1; done
# chaîne : banc_amorce.sh -> env/bash amorce -> timeout -> bash instance
PID_AMORCE=$(ps -o pid= --ppid "$PID_BANC" | head -1 | tr -d ' ')
PID_TIMEOUT=$(ps -o pid=,comm= --ppid "$PID_AMORCE" | awk '$2=="timeout"{print $1}')
echo "banc $PID_BANC amorce $PID_AMORCE timeout $PID_TIMEOUT"
ps -o pid,ppid,comm --ppid "$PID_AMORCE"
kill -TERM "$PID_TIMEOUT"
wait "$PID_BANC"
