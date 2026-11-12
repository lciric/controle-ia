#!/usr/bin/env bash
# Banc 2 du scellement v5 (R5 ; contrôle mécanique, CM-03). Le banc 1 (essais_scellement_v5.sh) versait les copies des
# scripts sans leur sceau : son cas sain était refusé, à juste titre, par verifier-arbre (« 5 problème(s) »), et son
# contrôle « commit poussé » acceptait le commit de base. Ce banc 2 scelle les copies, vérifie l'arbre de base, re-scelle
# les copies modifiées par S2 et S4, et exige au cas sain un commit nouveau qui ajoute la v2 et son sceau.
# Banc du scellement v5 (R5 ; contrôle mécanique, CM-03) : sur un dépôt jetable et un dépôt nu local, avec un faux
# bloc-notes H qui porte les scripts (copie du scellement dont seules les lignes H et DEPOT changent ; contrôles v7
# épinglés pour l'essai). Préalables simulés : GO fictif accordé par Lazar sur N-018, N-018 tranché, ligne R-990 du GO,
# deux rapports fictifs (bancs finaux). Cas : artefacts S1 à S8 (code non nul attendu, aucun commit nouveau du
# scellement), puis cas sain S0 (code 0, un commit poussé), suivi des contrôles v7 joués sur le commit produit (copie
# dont seule la ligne DEPOT change) : bout en bout, de la v2 scellée aux contrôles avant dépense.
# Usage : essais_scellement_v5b.sh RACINE_NEUVE
set -uo pipefail
E=$1
BN=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
R=$BN/revalidation-v2
D=/home/user/controle-ia-travail
PY=$BN/scellement-revalidation/venv-gpu-neuf/bin/python
P=prereg/T0.5-revalidation-equivalence-pilote-v2.md; CL=prereg/contre-lectures; V=docs/procedures/revalidation-T0.5-v2
GO=GO-2026-10-11-99; REG=R-990; CAND=brouillons/T0.5-revalidation-equivalence-pilote-v2-candidat5.md
FICTIFS="T0.5-revalidation-v2-verification-banc-controles-final-v1.tar T0.5-revalidation-v2-verification-banc-lanceur-scellement-v1.tar"
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
mkdir -p "$E/H" && cd "$E" || exit 2
git clone -q --no-local "$D" depot && cd depot || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
python3 - <<EOF || exit 2
from pathlib import Path
d = Path("registres/decisions.md"); t = d.read_text(encoding="utf-8")
l = [x for x in t.split("\n") if x.startswith("| N-018 |")][0]
t = t.replace(l, l.rsplit("| en attente |", 1)[0] + "| tranché : option (a), $GO (essai) |")
d.write_text(t.rstrip("\n") + "\n| $REG | 2026-10-11 | essai : $GO consigné | — |\n", encoding="utf-8")
g = Path("registres/go.md")
g.write_text(g.read_text(encoding="utf-8").rstrip("\n") + "\n| $GO | 2026-10-11 | revendication | N-018, option (a) (essai) | — | — | Lazar | $REG (essai) |\n", encoding="utf-8")
for n in "$FICTIFS".split():
    Path("$CL/" + n).write_text("rapport fictif (essai) " + n + "\n", encoding="utf-8")
EOF
for n in $FICTIFS; do PYTHONPATH=src "$PY" -m controle_ia.scellement sceller "$CL/$n" > /dev/null || exit 2; done
# faux bloc-notes : scripts, contrôles épinglés pour l'essai, scellement dont H et DEPOT changent
NOMS=$(git ls-files "$CL" ; for n in $FICTIFS; do echo "$CL/$n"; done)
NOMS=$(printf '%s\n' $NOMS | grep -E "^$CL/T0\\.5-revalidation-v2-(relecture|verification)-[a-z-]+-v1\\.(md|json|tar)$" | sort -u)
PAIRES=""; for f in $NOMS; do PAIRES="$PAIRES $(basename "$f")=$(sha256sum "$f" | cut -d' ' -f1)"; done; PAIRES=${PAIRES# }
normaliser() { sed -E '3s/[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}/AAAA-MM-JJ HH:MM/; 8s/[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}/AAAA-MM-JJ HH:MM/' "$1" \
    | sed -E 's/^(- Version 2 \(N-018\) : .*) Pièces : .*$/\1 Pièces : (remplies au scellement)./' | sha256sum | cut -d' ' -f1; }
cp "$R/remplir_revalidation_v2_r4.py" "$R/lancer_revalidation_v7.sh" "$R/recuperation_revalidation_v2.sh" "$E/H/"
sed -e "s|^CANDIDAT_FINAL=.*|CANDIDAT_FINAL=$(sha256sum "$CAND" | cut -d' ' -f1)|" -e "s|^CANDIDAT_FINAL_CHEMIN=.*|CANDIDAT_FINAL_CHEMIN=$CAND|" \
    -e "s|^CANDIDAT_NORMALISE=.*|CANDIDAT_NORMALISE=$(normaliser "$CAND")|" -e "s|^RAPPORTS_ATTENDUS=.*|RAPPORTS_ATTENDUS=\"$PAIRES\"|" \
    "$R/controles_avant_depense_v7.sh" > "$E/H/controles_avant_depense_v7.sh"
sed -e "s|^H=.*|H=$E/H|" -e "s|^DEPOT=.*|DEPOT=$E/depot|" "$R/sceller_revalidation_v5.sh" > "$E/H/sceller_revalidation_v5.sh"
echo "lignes changées dans la copie du scellement : $(diff "$R/sceller_revalidation_v5.sh" "$E/H/sceller_revalidation_v5.sh" | grep -c '^>')"
mkdir -p "$V" && for s in remplir_revalidation_v2_r4.py controles_avant_depense_v7.sh lancer_revalidation_v7.sh sceller_revalidation_v5.sh recuperation_revalidation_v2.sh; do cp "$E/H/$s" "$V/$s"; PYTHONPATH=src "$PY" -m controle_ia.scellement sceller "$V/$s" > /dev/null || exit 2; done
git add -A registres "$CL" "$V" && git commit -qm "essai : préalables du scellement et copies versées" || exit 2
git clone -q --bare . "$E/distant.git" && git remote set-url origin "$E/distant.git" && git fetch -q origin || exit 2
BASE=$(git rev-parse HEAD); echo "base $BASE"
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier-arbre . | tail -1 | grep -q "arbre intact" && echo "base : arbre intact" || { echo "base : arbre non intact"; exit 2; }
resceller() { (cd "$(dirname "$1")" && sha256sum "$(basename "$1")" > "$(basename "$1").sha256"); }
remettre() { git reset -q --hard "$BASE"; git clean -fdq; git push -q -f origin "$BASE:main"; git fetch -q origin; cp "$V/controles_avant_depense_v7.sh" "$V/remplir_revalidation_v2_r4.py" "$E/H/"; }
cas() {   # $1 nom ; $2 code attendu (« non nul » ou 0) ; $3 préparation
    local nom=$1 attendu=$2 prep=$3 avant apres c
    remettre; eval "$prep"
    avant=$(git rev-parse HEAD)
    bash "$E/H/sceller_revalidation_v5.sh" "$GO" "$REG" > "$E/sortie-$nom.txt" 2>&1; c=$?
    apres=$(git rev-parse HEAD)
    local v="CONFORME"
    if [ "$attendu" = 0 ]; then [ "$c" = 0 ] && [ "$avant" != "$apres" ] || v="NON CONFORME (code $c)"
    else [ "$c" != 0 ] && [ "$avant" = "$apres" ] && [ ! -e "$P.sha256" ] || v="NON CONFORME (code $c, commit nouveau : $([ "$avant" = "$apres" ] && echo non || echo oui))"; fi
    echo "$nom : code $c ; $v"; grep -v '^$' "$E/sortie-$nom.txt" | tail -1 | sed 's/^/    | /' | cut -c1-180
}
pousser() { git add -A . && git commit -qm "essai : $1" && git push -q origin HEAD:main && git fetch -q origin; }
cas S1-candidat-final-altere 1 "echo x >> $CAND && (cd brouillons && sha256sum \$(basename $CAND) > \$(basename $CAND).sha256) && pousser S1"
cas S2-normalise-epingle-faux 1 "sed -i 's/^CANDIDAT_NORMALISE=.*/CANDIDAT_NORMALISE=$(printf '0%.0s' {1..64})/' $V/controles_avant_depense_v7.sh && resceller $V/controles_avant_depense_v7.sh && cp $V/controles_avant_depense_v7.sh $E/H/ && pousser S2"
cas S3-candidat-relu-altere 1 "echo x >> brouillons/T0.5-revalidation-equivalence-pilote-v2-candidat2.md && (cd brouillons && sha256sum T0.5-revalidation-equivalence-pilote-v2-candidat2.md > T0.5-revalidation-equivalence-pilote-v2-candidat2.md.sha256) && pousser S3"
cas S4-epingles-absentes 1 "sed -i 's/^CANDIDAT_FINAL=.*/CANDIDAT_FINAL=A_EPINGLER/' $V/controles_avant_depense_v7.sh && resceller $V/controles_avant_depense_v7.sh && cp $V/controles_avant_depense_v7.sh $E/H/ && pousser S4"
cas S5-script-different-de-sa-copie 1 "echo '# modifié' >> $E/H/remplir_revalidation_v2_r4.py"
cas S6-head-non-pousse 1 "echo x > essai-local.txt && git add essai-local.txt && git commit -qm 'essai : S6 local'"
cas S7-v2-deja-presente 1 "echo x > $P && pousser S7"
cas S8-go-absent 1 "sed -i '/^| $GO |/d' registres/go.md && pousser S8"
cas S0-sain 0 ":"
S=$(git rev-parse HEAD)
if [ "$S" != "$BASE" ] && [ "$(git -C "$E/distant.git" rev-parse main)" = "$S" ] && [ "$(git rev-parse "$S^")" = "$BASE" ] \
   && [ "$(git diff --name-only "$BASE" "$S" | sort | tr '\n' ' ')" = "$P $P.sha256 " ] && [ -z "$(git status --porcelain)" ]; then
    echo "S0 : commit $S poussé, enfant de la base, qui ajoute la v2 et son sceau seulement ; arbre propre"
else echo "S0 : NON CONFORME (commit absent, non poussé, ou contenu inattendu)"; fi
sed "s|^DEPOT=.*|DEPOT=$E/distant.git|" "$E/H/controles_avant_depense_v7.sh" > "$E/controles-bout-en-bout.sh"
bash "$E/controles-bout-en-bout.sh" "$S" "$E/clone-bout-en-bout" > "$E/sortie-bout-en-bout.txt" 2>&1; c=$?; rm -rf "$E/clone-bout-en-bout"
echo "bout en bout : contrôles v7 sur le commit scellé, code $c ; $(tail -1 "$E/sortie-bout-en-bout.txt") ; $(grep -c '^OK' "$E/sortie-bout-en-bout.txt") OK, $(grep -c '^KO' "$E/sortie-bout-en-bout.txt") KO"
grep '^KO' "$E/sortie-bout-en-bout.txt" | sed 's/^/    /'
echo "FIN DU BANC DU SCELLEMENT"
