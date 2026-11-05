#!/usr/bin/env bash
# cl5 : latence de la surveillance v5 entre le plafond et la demande d'arrêt, appels vastai lents mais sous 60 s.
SB=/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/contre-lecture-echelle-v6
WT=/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-echelle-v1
E=$SB/surveillance-latence
D=4500
MAINTENANT=$(date -u +%s)
CREATION=$((MAINTENANT - D + 5))            # le plafond tombe 5 s après le départ de la surveillance
mkdir -p $E/lancement
printf 'go GO-0000-00-00-00\ncreation %s\nduree_max_s %s\nsuccès : True ; identifiant 12345678 ; message : essai\n' "$CREATION" "$D" > $E/lancement/lancement.txt
echo "depart $MAINTENANT ; plafond $((CREATION + D))" > $E/resultat.txt
env VASTAI=$E/faux-vastai ARRETS_FAUX=$E/arrets.txt DUREE_MAX_S=$D ATTENTE_ARRET_S=0 \
    bash $WT/echelle-v5/scripts/surveiller_echelle_v5.sh 12345678 $CREATION $E/lancement $E/s > $E/sortie.txt 2>&1
echo "code $?" >> $E/resultat.txt
A=$(head -1 $E/arrets.txt | awk '{print $3}')
echo "arrêt demandé à $A ; retard sur le plafond : $((A - CREATION - D)) s" >> $E/resultat.txt
