#!/bin/sh
# Comptes des manifestes sous runs/ commit par commit (lecture seule) ; tentative de 12:11:25Z.
# Usage : sh comptes_manifestes_v1.sh <arbre de lecture>
A="$1"
for c in b478ea39 adc1be82 c0c71757 b4d5ef74 4c0a4313 68ca4ddb e8e03a8f e13e5e28; do
  n=$(git -C "$A" ls-tree -r --name-only "$c" runs | grep -c '/manifeste.json$')
  echo "$c $(git -C "$A" log -1 --format='%cI %s' "$c" | cut -c1-110) : $n manifestes"
done
echo "--- manifestes ajoutés entre b478ea39 et 4c0a4313 (et nombre de fichiers diag/ ajoutés) :"
git -C "$A" diff --name-only b478ea39 4c0a4313 -- runs | grep -v sha256
git -C "$A" diff --name-only b478ea39 4c0a4313 -- diag | grep -v sha256 | cut -d/ -f1-2 | sort | uniq -c
echo "--- fichiers du commit 4c0a4313 :"
git -C "$A" show --name-only --format= 4c0a4313
echo "--- chemins 20261106-1211*/1212* dans tout l'historique (runs, diag) :"
git -C "$A" log --all --name-only --format= -- runs diag | grep -E '20261106-121[12]' | sort -u
echo "(fin)"
