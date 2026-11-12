#!/usr/bin/env bash
# Intégrité du verdict « agrégateurs sur R1 v4 » — lecture seule (git show, sha256sum). Aucun fetch.
set -u
D=/home/user/controle-ia-travail; W=/home/user/wt/verdictAG
cd "$D"
echo "== date"; date -u
echo "== consigne (b8abaabb)"
git show b8abaabb:docs/notes/g0-deux-semaines-v1/consigne-verdict-agregation-r1-v4-v1.md | sha256sum
git show b8abaabb:docs/notes/g0-deux-semaines-v1/consigne-verdict-agregation-r1-v4-v1.md.sha256
echo "== texte scellé sur trois commits"
for c in b8abaabb 60ddbedb 913a80cc; do echo "$c $(git show $c:prereg/agregation-r1-v4-v1.md | sha256sum | cut -d' ' -f1) | compagnon $(git show $c:prereg/agregation-r1-v4-v1.md.sha256)"; done
echo "== commits"; git rev-parse b8abaabb 60ddbedb 913a80cc 1fcb23d7 origin/agregation-r1-v4-sortie; git log -1 --format='913a80cc parent %P' 913a80cc
echo "== table de 21 lignes contre trois commits"
git show b8abaabb:prereg/agregation-r1-v4-v1.md | grep -E '^\| `(src|tests|brouillons)/' | while IFS='|' read -r _ f h _; do
  f=$(echo $f | tr -d '` '); h=$(echo $h | tr -d '` ')
  for c in 1fcb23d7 60ddbedb 913a80cc; do a=$(git show $c:$f | sha256sum | cut -d' ' -f1); [ "$a" = "$h" ] && r=OK || r="DIFF:$a"; echo "$c $r $f"; done
done
echo "== lignes de table : $(git show b8abaabb:prereg/agregation-r1-v4-v1.md | grep -cE '^\| `(src|tests|brouillons)/')"
echo "== fichiers changés 1fcb23d7..60ddbedb"; git diff --name-only 1fcb23d7 60ddbedb
echo "== fichiers ajoutés 60ddbedb..913a80cc"; git diff --name-status 60ddbedb 913a80cc
echo "== manifestes citant le texte (913a80cc)"
git ls-tree -r --name-only 913a80cc runs | grep 'manifeste.json$' | while read f; do git show 913a80cc:$f | grep -qE 'agregation-r1-v4-v1\.md|5916e62e' && echo "$f"; done
echo "== sorties et compagnons (arbre $W)"
cd "$W"; git rev-parse HEAD
for f in runs/20261106-130318-agregation-r1-v4/manifeste.json diag/20261106-130318-agregation-r1-v4/agregation-r1-v4-v1.json journaux/20261106-130318-agregation-r1-v4.log donnees/20261019-230011-p3-reel/scores-p3.npz; do
  echo "$f calcul=$( [ -f $f ] && sha256sum $f | cut -d' ' -f1 || echo absent) compagnon=$(cut -d' ' -f1 $f.sha256)"; done
cat journaux/20261106-130318-agregation-r1-v4.log; echo
echo "== compagnons d'activations de réception dans les références locales"
cd "$D"; for r in $(git for-each-ref --format='%(refname)'); do git ls-tree -r --name-only $r | grep -E 'donnees/20261105-021737-r1-v4-rejeu-reel/.*\.sha256$' | sed "s#^#$r #"; done; echo "(fin)"
echo "== pièce de rejeu J (analyses-r1-v4, commit du fichier)"
git log --format='%h %s' -1 origin/analyses-r1-v4 -- diag/20261105-021737-r1-v4-rejeu-reel/rejeu-activations.json
git show origin/analyses-r1-v4:diag/20261105-021737-r1-v4-rejeu-reel/rejeu-activations.json | sha256sum
git show origin/analyses-r1-v4:diag/20261105-021737-r1-v4-rejeu-reel/rejeu-activations.json.sha256
git show origin/analyses-r1-v4:diag/20261105-021737-r1-v4-rejeu-reel/rejeu-activations.json | sed -n '153,154p'
echo "== branche du verdict de l'étape F dans les références locales"
git for-each-ref --format='%(refname)' | grep -c 'verdict-etape-F' || true
echo "== registres (main b8abaabb)"
git show b8abaabb:registres/decisions.md | grep -E '^\| R-164(0|2|3) ' | cut -c1-400
