#!/usr/bin/env bash
# Chemins de la surveillance v4 non couverts par la suite de tests, avec un faux outil (bac à sable seulement).
SB=/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/contre-lecture-echelle-v5
S=/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-echelle-v1/echelle-v4/scripts
F=$SB/faux
surv() {  # nom, création passée (ou « meme »), état du faux conteneur, journal du faux conteneur
    local nom=$1 cr=$2 etat=$3 journal=$4 d=$F/s-$1
    rm -rf "$d"; mkdir -p "$d/lancement"; echo "$etat" > "$d/etat"; printf '%s\n' "$journal" > "$d/journal"
    local c=$(( $(date -u +%s) - 10 ))
    printf 'go GO-0000-00-00-00\ncreation %s\nduree_max_s 4500\nsuccès : True ; identifiant 12345678 ; message : essai\n' "$c" > "$d/lancement/lancement.txt"
    [ "$cr" = meme ] && cr=$c
    VASTAI=$F/faux-outil ETAT_FAUX=$d/etat JOURNAL_FAUX=$d/journal ARRETS_FAUX=$d/arrets DUREE_MAX_S=4500 PAS_S=1 \
        ATTENTE_ARRET_S=0 timeout 20 bash "$S/surveiller_echelle_v4.sh" 12345678 "$cr" "$d/lancement" "$d/sortie" > "$d/out.txt" 2>&1
    echo "$nom : code $? ; arrêts : $(tr '\n' ' ' < "$d/arrets" 2>/dev/null) ; $(tail -2 "$d/out.txt" | tr '\n' ' ')"
}
surv creation-differente 1793000000 running 'AMORCE 2026 : fin, code 0'
surv conteneur-sorti meme exited 'ECHELLE 2026 : mesure'
surv refus-precoce-puis-sortie meme exited 'AMORCE : DUREE_MAX_S absente ou hors de [4 500 ; 7 200] s : arrêt, aucun calcul'
