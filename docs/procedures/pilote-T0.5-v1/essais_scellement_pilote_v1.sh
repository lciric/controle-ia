#!/usr/bin/env bash
# Banc du scellement du pilote de T0.5 (R5 ; relecture R2, CH-03 et CH-08), sur le modèle du banc du scellement v5b de la
# revalidation et du banc B0 à B12 de la relecture R2 (angle « chaîne »). Clone jetable du commit des préalables C (épingles,
# rapports et copies versées réels), dépôt nu local en guise de dépôt distant ; décision de Lazar sur N-019 simulée dans le
# clone (GO-2026-10-12-99, R-990). Bloc-notes factice : copies versées à C, dont seules les lignes H et DEPOT de la copie du
# scellement changent (re-versée et re-scellée dans le clone, comme dans la répétition finale). Après chaque passage : code,
# dernières lignes, tête et dépôt distant, restes non suivis, dossiers de travail laissés (CH-08).
# Usage : essais_scellement_pilote_v1.sh DEPOT_SOURCE C RACINE_NEUVE
set -uo pipefail
SRC=$1; C=$2; E=$3
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
V=docs/procedures/pilote-T0.5-v1
P=prereg/T0.5-pilote-8B-v1.md; CFG=prereg/T0.5-pilote-config-v1.json
GO=GO-2026-10-12-99; REG=R-990
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
mkdir -p "$E/H" && cd "$E" || exit 2
git clone -q --no-local "$SRC" depot && cd depot && git checkout -q "$C" && git checkout -q -B main || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
echo "C = $(git rev-parse HEAD)"
CHAINE=$(sed -n '/^CHAINE="/,/"$/p' "$V/sceller_pilote_v1.sh" | tr -d '"' | sed 's/^CHAINE=//')
for s in $CHAINE; do cp "$V/$s" "$E/H/$s" || { echo "copie versée absente : $s"; exit 2; }; done
grep -q "A_EPINGLER" "$E/H/controles_avant_depense_pilote_v1.sh" && { echo "épingles absentes"; exit 2; }
python3 - "$GO" "$REG" <<'PYGO' || exit 2
import sys
from pathlib import Path
go, reg = sys.argv[1:3]
d = Path("registres/decisions.md"); lignes = d.read_text(encoding="utf-8").split("\n")
i = [k for k, x in enumerate(lignes) if x.startswith("| N-019 |")]
assert len(i) == 1
lignes[i[0]] = lignes[i[0]].rsplit("|", 2)[0] + f"| tranché (a) par Lazar : {go} ({reg}) |"
d.write_text("\n".join(lignes).rstrip("\n") + f"\n| {reg} | 2026-10-12 | essai : {go} de Lazar sur N-019, option (a) | — |\n", encoding="utf-8")
g = Path("registres/go.md")
g.write_text(g.read_text(encoding="utf-8").rstrip("\n") + f"\n| {go} | 2026-10-12 | revendication | N-019, option (a) (essai) | — | 2026-10-12 | Lazar | {reg} (essai) |\n", encoding="utf-8")
PYGO
sed -e "s|^H=.*|H=$E/H|" -e "s|^DEPOT=.*|DEPOT=$E/depot|" "$V/sceller_pilote_v1.sh" > "$E/H/sceller_pilote_v1.sh"
echo "lignes changées dans la copie du scellement : $(diff "$V/sceller_pilote_v1.sh" "$E/H/sceller_pilote_v1.sh" | grep -c '^>')"
grep -n "controle-ia-travail\|github" "$E/H/sceller_pilote_v1.sh" && { echo "COPIE NON SÛRE"; exit 2; }
cp "$E/H/sceller_pilote_v1.sh" "$V/sceller_pilote_v1.sh" && (cd "$V" && sha256sum sceller_pilote_v1.sh > sceller_pilote_v1.sh.sha256)
git add -A "$V" registres && git commit -qm "essai : GO fictif, copie du scellement du banc" || exit 2
J=$(git rev-parse HEAD); echo "J = $J"
git clone -q --bare . "$E/distant.git" && git remote set-url origin "$E/distant.git" && git fetch -q origin || exit 2
[ "$(git remote get-url --push origin)" = "$E/distant.git" ] || { echo "origine de poussée inattendue"; exit 2; }
NON_CONFORMES=0   # décompte des cas non conformes ; le banc sort en code 1 s'il en reste (vérification c3, sceptique de UH-01)
passage() {   # $1 nom, $2 code attendu, $3 motif attendu dans la sortie (vide : cas sain), puis les arguments du scellement
    local n=$1 attendu=$2 motif=$3; shift 3
    local avant c v reste dossiers
    avant=$(git rev-parse HEAD)
    bash "$E/H/sceller_pilote_v1.sh" "$@" > "$E/scellement-$n.log" 2>&1; c=$?
    reste=$(ls "$P" "$P.sha256" "$CFG" "$CFG.sha256" 2>/dev/null | tr '\n' ' ')
    dossiers=$(ls -d "$E"/H/scellement-* 2>/dev/null | wc -l)
    v="CONFORME"
    [ "$c" = "$attendu" ] || v="NON CONFORME (code $c, attendu $attendu)"
    if [ -n "$motif" ] && ! grep -qF -- "$motif" "$E/scellement-$n.log"; then v="NON CONFORME (motif « $motif » absent)"; fi
    if [ "$attendu" != 0 ]; then
        [ "$(git rev-parse HEAD)" = "$avant" ] || [ "$n" = S03-poussee-refusee ] || v="NON CONFORME (commit fait malgré l'arrêt)"
        [ -z "$reste" ] || [ "$n" = S07-prereg-present ] || [ "$n" = S03-poussee-refusee ] || v="NON CONFORME (restes : $reste)"
    fi
    [ "$dossiers" = 0 ] || v="NON CONFORME ($dossiers dossier(s) de travail laissé(s))"
    [ "$v" = CONFORME ] || NON_CONFORMES=$((NON_CONFORMES + 1))
    echo "$n : code $c ; $v"
    grep -v '^$' "$E/scellement-$n.log" | tail -2 | cut -c1-200 | sed 's/^/    | /'
}
remise() {   # clone et dépôt nu remis sur J ; fichiers du scellement retirés ; adresses rétablies
    git checkout -q -f main; git reset -q --hard "${1:-$J}"; rm -f "$P" "$P.sha256" "$CFG" "$CFG.sha256"
    git remote set-url origin "$E/distant.git"; git remote set-url --push origin "$E/distant.git"
    # le dépôt nu n'a pas les commits faits dans le clone après sa copie : poussée forcée par chemin explicite,
    # jamais update-ref (vérification c3, UH-01)
    git push -q -f "$E/distant.git" "${1:-$J}:refs/heads/main" || { echo "REMISE IMPOSSIBLE (dépôt nu)"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
    git fetch -q origin
    [ "$(git rev-parse origin/main)" = "$(git rev-parse "${1:-$J}")" ] || { echo "REMISE IMPOSSIBLE (origin/main)"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
}
passage S00-sain 0 "poussé ; préenregistrement" "$GO" "$REG"
S=$(git rev-parse HEAD)
if [ "$S" != "$J" ] && [ "$(git rev-parse "$S^")" = "$J" ] && [ "$(git -C "$E/distant.git" rev-parse main)" = "$S" ] \
   && [ "$(git diff --name-only "$J" "$S" | sort | tr '\n' ' ')" = "$(printf '%s\n' "$CFG" "$CFG.sha256" "$P" "$P.sha256" | sort | tr '\n' ' ')" ] \
   && [ -z "$(git status --porcelain --untracked-files=no)" ]; then
    echo "    S $S : enfant de J, poussé, quatre fichiers seulement, arbre propre : CONFORME"
else echo "    S $S : NON CONFORME (parent, poussée ou contenu)"; NON_CONFORMES=$((NON_CONFORMES + 1)); fi
remise
echo "# essai" >> README.md
passage S01-arbre-sale 2 "arbre suivi non propre" "$GO" "$REG"
git checkout -q -- README.md
printf '%s  recuperation_pilote_v1.sh\n' "$(printf '0%.0s' {1..64})" > "$V/recuperation_pilote_v1.sh.sha256"
git commit -qam "essai : sceau faussé" && J2=$(git rev-parse HEAD) && remise "$J2"
passage S02-sceau-fausse-verifier-arbre 2 "ÉCHEC" "$GO" "$REG"
remise
git remote set-url --push origin "$E/inexistant.git"
passage S03-poussee-refusee 2 "poussée de S en échec" "$GO" "$REG"
remise
cp "$E/H/controles_avant_depense_pilote_v1.sh" "$E/ctl-sauve.sh"
# une épingle changée l'est dans le bloc-notes et dans la copie versée (commit poussé) : sinon le scellement s'arrête
# d'abord sur « bloc-notes ≠ copie versée » et la garde visée n'est jamais atteinte
epingle_versee() {   # $1 expression sed, $2 message du commit ; une ligne exactement changée (vérification c3, UH-02)
    cp "$E/H/controles_avant_depense_pilote_v1.sh" "$E/ctl-avant-epingle.sh"
    sed -i "$1" "$E/H/controles_avant_depense_pilote_v1.sh" || return 1
    [ "$(diff "$E/ctl-avant-epingle.sh" "$E/H/controles_avant_depense_pilote_v1.sh" | grep -c '^>')" = 1 ] \
        || { echo "épingle : une ligne exactement attendue"; return 1; }
    cp "$E/H/controles_avant_depense_pilote_v1.sh" "$V/" \
        && (cd "$V" && sha256sum controles_avant_depense_pilote_v1.sh > controles_avant_depense_pilote_v1.sh.sha256) \
        && git commit -qam "essai : $2" && remise "$(git rev-parse HEAD)"
}
epingle_versee "s|^CANDIDAT_NORMALISE=[0-9a-f]\{64\}|CANDIDAT_NORMALISE=$(printf '1%.0s' {1..64})|" "épingle normalisée fausse" \
    || { echo "S04 : montage impossible"; exit 2; }
passage S04-epingle-normalisee-fausse 2 "normalisé ≠ épingle" "$GO" "$REG"
cp "$E/ctl-sauve.sh" "$E/H/controles_avant_depense_pilote_v1.sh"
remise
echo "# modifié" >> "$E/H/remplir_pilote_v1.py"
passage S05-generateur-non-verse 2 "remplir_pilote_v1.py du bloc-notes ≠ copie versée" "$GO" "$REG"
cp "$V/remplir_pilote_v1.py" "$E/H/remplir_pilote_v1.py"
git commit -q --allow-empty -m "essai : commit local non poussé"
passage S06-head-en-avance 2 "HEAD ≠ origin/main" "$GO" "$REG"
remise
echo x > "$P"
passage S07-prereg-present 2 "existe déjà (R12)" "$GO" "$REG"
rm -f "$P"
RF=$(grep -o 'T0\.5-pilote-v1-relecture-b8[^ =]*' "$E/H/controles_avant_depense_pilote_v1.sh" | head -1)
[ -n "$RF" ] || { echo "aucun rapport de la relecture épinglé"; exit 2; }
git rm -q "prereg/contre-lectures/$RF" "prereg/contre-lectures/$RF.sha256" && git commit -qm "essai : rapport retiré" && J3=$(git rev-parse HEAD) && remise "$J3"
passage S08-rapport-epingle-absent 2 "$RF" "$GO" "$REG"
remise
sed -i -E 's/^(\| N-019 \|.*)\| tranché \(a\) par Lazar : [^|]*\|$/\1| en attente du GO de Lazar |/' registres/decisions.md
git commit -qam "essai : N-019 en attente" && J4=$(git rev-parse HEAD) && remise "$J4"
passage S09-n019-en-attente 2 "N-019 : colonne d'état" "$GO" "$REG"
remise
# VH-01, VH-09 : épingles relues par le scellement avant l'entropie
sed -i "s|^REPETITION_JOUET=[0-9a-f]\{64\}|REPETITION_JOUET=A_EPINGLER|" "$E/H/controles_avant_depense_pilote_v1.sh"
passage S13-epingle-restee 2 "A_EPINGLER" "$GO" "$REG"
cp "$E/ctl-sauve.sh" "$E/H/controles_avant_depense_pilote_v1.sh"
AUTRE=$(git rev-parse "$(git rev-list --max-count=1 HEAD -- src/controle_ia/environnements/lancer_pilote_a.py)^")
epingle_versee "s|^CODE_RELU=[0-9a-f]\{40\}|CODE_RELU=$AUTRE|" "code relu autre" || { echo "S14 : montage impossible"; exit 2; }
passage S14-code-relu-autre 2 "arbre gelé de HEAD ≠ code relu" "$GO" "$REG"
cp "$E/ctl-sauve.sh" "$E/H/controles_avant_depense_pilote_v1.sh"
remise
LJ=$(sed -n 's/^REPETITION_JOUET_CHEMIN=\([^ #]*\).*/\1/p' "$E/H/controles_avant_depense_pilote_v1.sh")
echo x >> "$LJ" && (cd "$(dirname "$LJ")" && sha256sum "$(basename "$LJ")" > "$(basename "$LJ").sha256") && git commit -qam "essai : journal altéré" \
    && J5=$(git rev-parse HEAD) && remise "$J5"
passage S15-journal-repetition-altere 2 "journal de la répétition jouet absent ou d'une autre empreinte que l'épingle" "$GO" "$REG"
remise
sed -i 's|^RAPPORTS_ATTENDUS="|RAPPORTS_ATTENDUS="T0.5-pilote-v1-autre-famille-v1.md='"$(printf '3%.0s' {1..64})"' |' "$E/H/controles_avant_depense_pilote_v1.sh"
passage S16-rapport-autre-famille 2 "hors des deux familles" "$GO" "$REG"
cp "$E/ctl-sauve.sh" "$E/H/controles_avant_depense_pilote_v1.sh"
# VH-01, restes : journal non suivi à HEAD ; journal d'un autre commit à son empreinte épinglée ; chemin hors du dossier
git rm -q --cached "$LJ" "$LJ.sha256" && git commit -qm "essai : journal non suivi" && J7=$(git rev-parse HEAD) && remise "$J7"
[ -f "$LJ" ] && [ -z "$(git ls-files -- "$LJ")" ] || { echo "S17 : montage impossible"; exit 2; }
passage S17-journal-non-suivi 2 "non suivi à HEAD" "$GO" "$REG"
remise
sed -i "s/^commit du code répété : .*/commit du code répété : $AUTRE/" "$LJ" && (cd "$(dirname "$LJ")" && sha256sum "$(basename "$LJ")" > "$(basename "$LJ").sha256") \
    && epingle_versee "s|^REPETITION_JOUET=[0-9a-f]\{64\}|REPETITION_JOUET=$(sha256sum "$LJ" | cut -d' ' -f1)|" "journal d'un autre commit, épinglé" \
    || { echo "S18 : montage impossible"; exit 2; }
passage S18-journal-autre-commit 2 "journal de la répétition jouet d'un autre commit que le code relu" "$GO" "$REG"
cp "$E/ctl-sauve.sh" "$E/H/controles_avant_depense_pilote_v1.sh"
remise
sed -i "s|^REPETITION_JOUET_CHEMIN=.*|REPETITION_JOUET_CHEMIN=diag/repetition-jouet-pilote-v1.log|" "$E/H/controles_avant_depense_pilote_v1.sh"
passage S19-journal-hors-du-dossier 2 "code relu ou répétition jouet non épinglés" "$GO" "$REG"
cp "$E/ctl-sauve.sh" "$E/H/controles_avant_depense_pilote_v1.sh"
# S20 : arrêt sous set -e avant le piège de sortie (lecture du dépôt distant impossible) : code 2 et ligne du piège ERR
git remote set-url origin "$E/inexistant.git"
passage S20-arret-avant-le-piege 2 "arrêt du scellement (ligne" "$GO" "$REG"
remise
# S21 : commit refusé après git add (crochet pre-commit) : code 2, fichiers retirés, index propre (UH-14)
printf '#!/bin/sh\nexit 1\n' > .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
passage S21-commit-refuse 2 "échec avant le commit : fichiers créés retirés" "$GO" "$REG"
git diff --cached --quiet && echo "    index propre après S21 : CONFORME" || { echo "    S21 : NON CONFORME (fichiers laissés dans l'index)"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
rm -f .git/hooks/pre-commit
remise
passage S10-sans-arguments 2 "usage"
passage S11-go-mal-forme 2 "usage" "GO-2026-10-12" "$REG"
passage S12-autre-go 2 "absent de registres/go.md" "GO-2026-10-12-98" "$REG"
remise
git status --short | head -5 | sed 's/^/    reste : /'
cd "$E" && rm -rf "$E/depot" "$E/distant.git"
echo "FIN DU BANC DU SCELLEMENT DU PILOTE ; cas non conformes : $NON_CONFORMES"
[ "$NON_CONFORMES" = 0 ] || exit 1
