#!/bin/bash
# Mesure des consignes réelles de la course (v43, --mesurer-consignes, aucun appel). Usage : mesurer_v1.sh LISTE(4|5) VARIANTE
set -u
S=/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad
W=/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/lancement-ideation-v1/travail
B=$W/branche/brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1
V=$1; VAR=$2
cd /tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/relecture-v44/cl11/copie/v44s
ARGS=(--mesurer-consignes --liste-blanche $W/liste-blanche-mesure-v$V.json
  --question $B/question-collisionneur-priorites-sept-questions-v3.md)
for f in extraits-v1/brief-notre-marque-v1.md extraits-v1/questions-section-A-v1.md extraits-v1/classement-v2-sections-1-a-4-v1.md \
  extraits-v1/anteriorite-Q{1,2,3,4,5,6,7,pont}-sections-1-a-3-v1.md anteriorite-coevolution-et-boite-blanche-v1.md \
  anteriorite-universalite-metriques-v1.md conception-pole-scientifique-v1.md integration-proposeurs-ia-v1.md; do ARGS+=(--piece $B/$f); done
CORPUS=$(ls $B/corpus-primaire-v1/extrait-*.md $B/corpus-primaire-v2/extrait-*.md $B/corpus-primaire-v3/extrait-*.md)
[ "$V" = 5 ] && CORPUS="$CORPUS $B/corpus-primaire-v4/extrait-2606.08106-v1.md"
for f in $CORPUS; do ARGS+=(--piece $f); done
for f in extraits-v1/anteriorite-Q{1,2,3,4,5,6,7,pont}-sections-1-a-3-v1.md anteriorite-coevolution-et-boite-blanche-v1.md; do ARGS+=(--piece-juge $B/$f); done
for f in $CORPUS; do ARGS+=(--piece-juge $f); done
ARGS+=(--materiau $B/preideation-interne-v1/fiches-anonymes.md --seconde-passe ${SANS_TEMOINS:+} ${SANS_TEMOINS:---temoins $S/temoins-ideation-tiers-v1.json}
  --proposeur opus=claude-opus-5-5 --proposeur fable=claude-fable-5-1
  --juge juge-fable=claude-fable-5-1 --juge juge-opus=claude-opus-5-5
  --proposeur-externe argon=gemini-argon --juge-externe argon-juge=gemini-argon
  --nombre 8 --graine 20261028 --taille-max-pieces 750000
  --prix-entree-usd-par-million-jetons 8.3 --budget-externe-usd 12.8 --budget-controle-externe-usd 3.1)
case $VAR in
  beta1) ARGS+=(--budget "proposeur_ideation|gemini-argon=3.1" --budget "juge_ideation|gemini-argon=3.3") ;;
  beta1-garde) ARGS+=(--budget "proposeur_ideation|gemini-argon=3.1" --budget "juge_ideation|gemini-argon=3.3" --taille-max-consigne-externe 1490000) ;;
  v44) ARGS+=(--budget-passe-2-externe-usd 3.1) ;;
  v44-garde) ARGS+=(--budget-passe-2-externe-usd 3.1 --taille-max-consigne-externe 1490000) ;;
esac
echo "# commande : python3 -I -B demonstrations/ideation_v1.py ${ARGS[*]}" | sed "s#$W#\$TRAVAIL#g; s#$S#\$BLOC#g"
env -i PATH=/usr/bin:/bin HOME=$W LANG=C.UTF-8 ${PYCMD:-python3 -I -B demonstrations/ideation_v1.py} "${ARGS[@]}"
echo "# code de sortie : $?"
