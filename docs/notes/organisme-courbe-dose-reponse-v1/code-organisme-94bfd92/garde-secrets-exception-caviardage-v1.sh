#!/bin/bash
# Garde des secrets de la session-dépôt, avec UNE exception étroite, écrite et éprouvée (règle 5).
# Exception : le motif d'en-tête de clé privée, quand il est précédé immédiatement du texte littéral « [A-Z ]* »,
# c'est-à-dire écrit comme expression régulière dans le module de caviardage de l'organisme, qui RECONNAÎT les clés
# pour les masquer. Ce n'est pas une clé. Les huit motifs comptent partout ailleurs.
# Lit un diff sur l'entrée standard ; écrit le nombre de correspondances (0 attendu avant tout commit).
motifs='sk-ant-api03-[A-Za-z0-9_-]{40,}|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-|PRIVATE[ ]KEY|sk[-]proj-|AIza[0-9A-Za-z_-]{35}|sk[-][A-Za-z0-9]{40,}'
sed -E 's/\[A-Z \]\*PRIVATE[ ]KEY/[A-Z ]*EXCEPTION_CAVIARDAGE/g' | grep -o -E "$motifs" | wc -l
