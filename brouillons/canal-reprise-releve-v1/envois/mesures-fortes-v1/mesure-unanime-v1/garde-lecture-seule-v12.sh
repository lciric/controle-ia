#!/bin/bash
# Garde d'arrêt isolée (R5) de la reprise LECTURE_SEULE : refuse de refaire une note déjà scellée (R12), sans jamais
# s'éteindre en silence quand la note est absente — c'est le défaut CV11-1 de la v11, où la ligne
#   [ -e note.sha256 ] && { echo …; exit 7; }
# renvoyait 1 lorsque la note n'était pas scellée et, sous `set -e`, tuait le script sans message ni reprise.
# Sortie 0 : rien n'est scellé, la reprise peut refaire la note (étapes 3 et 4). Sortie 7 : note déjà scellée, rien à reprendre.
set -euo pipefail
NOTE="${1:?chemin de la note (sans .sha256)}"
if [ -e "$NOTE.sha256" ]; then
  echo "LECTURE_SEULE : la note $NOTE est déjà scellée (R12) ; la séquence est allée au bout, rien à reprendre" >&2
  exit 7
fi
echo "LECTURE_SEULE : aucune note scellée pour $NOTE ; reprise des étapes (3) et (4) possible"
exit 0
