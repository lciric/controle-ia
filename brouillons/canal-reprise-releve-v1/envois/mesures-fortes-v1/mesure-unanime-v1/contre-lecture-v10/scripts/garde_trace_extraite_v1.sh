#!/bin/bash
# Contre-lecture v10 (CV9-2, CV10-1) : la garde « toute trace bloque » de commandes-lecture-reelle-v10.sh, ligne 41, extraite
# TELLE QUELLE (sed -n '41p') et exécutée seule dans des dossiers de test : aucune autre ligne de la séquence n'est lancée,
# aucune donnée n'est lue. Le dernier cas reproduit l'état du dossier déposé (commit 1ef46c7b) par des fichiers vides aux
# mêmes noms (liste prise par `ls` en lecture seule sur le dossier du préenregistrement).
# Usage : bash garde_trace_extraite_v1.sh SEQUENCE.sh DOSSIER_DU_PREREG DOSSIER_DE_TRAVAIL
set -u
SEQ="$1"; PREREG_DIR="$2"; W="$3"
LIGNE=$(sed -n '41p' "$SEQ")
echo "ligne 41 extraite : $LIGNE"
echo "empreinte de la séquence : $(sha256sum "$SEQ" | cut -d' ' -f1)"
essai() {  # $1 nom du cas ; fichiers à créer ensuite
  local nom="$1"; shift
  local d="$W/$nom"; rm -rf "$d"; mkdir -p "$d"
  for f in "$@"; do : > "$d/$f"; done
  # la ligne fait « exit 3 » dans le sous-shell si la garde lève ; sinon le sous-shell sort par « exit 0 »
  ( cd "$d" && eval "$LIGNE" ; exit 0 ) 2> "$d.err"
  local code=$?
  echo "cas $nom : code $code ; message : $(cat "$d.err")"
}
essai vide
essai sortie_finale sortie-reelle-v10.json
essai partiel sortie-reelle-v10.json.partiel
essai renommee sortie-reelle-v10-interrompue-1.json.partiel
essai repetition_seule sortie-reelle-v10-repetition.json sortie-reelle-v10-repetition.json.sha256
essai repetition_v9_seule sortie-reelle-v9-repetition.json sortie-reelle-v9-repetition.json.sha256
# état du dossier déposé : mêmes noms, fichiers vides
NOMS=$(cd "$PREREG_DIR" && ls -1 | grep -v '^contre-lecture-' )
essai etat_depose $NOMS
echo "noms du dossier déposé qui répondent au motif sortie-reelle-v10* : $(cd "$PREREG_DIR" && ls -1d sortie-reelle-v10* 2>/dev/null | tr '\n' ' ')"
