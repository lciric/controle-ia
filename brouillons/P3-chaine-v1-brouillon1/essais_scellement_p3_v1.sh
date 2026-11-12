#!/usr/bin/env bash
# Banc du scellement du premier test boîte blanche sur l'organisme (i-a) (P3, R-192 ; R5), décliné du banc du scellement
# des notations refaites du pilote de T0.5 (docs/procedures/notations-T0.5-v2/essais_scellement_notations_v1.sh) sous un
# nom nouveau (R12). Clone jetable du commit des préalables C (épingles, candidat, configuration et consignes relus,
# rapports et copies versées réels ; registres réels : le GO de calcul et la décision de Lazar y sont consignés), dépôt
# nu local en guise de dépôt distant. Bloc-notes factice : copies versées à C, dont seules les lignes H, DEPOT et DISTANT
# de la copie du scellement changent (re-versée et rescellée dans le clone, comme dans la répétition finale). Après chaque
# passage : code, dernières lignes, tête et dépôt distant, restes non suivis. Sort en code 1 s'il reste un cas non
# conforme. Cas propres à P3 : consignes relues (épingle, sceau, présence au chemin scellé), configuration relue qui ne
# cite pas les consignes relues, GO de calcul et décision de Lazar (R-192) absents, d'un autre type, révoqués ou en
# double, intitulés de P3.
# Usage : essais_scellement_p3_v1.sh DEPOT_SOURCE C RACINE_NEUVE
set -uo pipefail
[ $# -eq 3 ] || { echo "usage : essais_scellement_p3_v1.sh DEPOT_SOURCE C RACINE_NEUVE"; exit 2; }
SRC=$(realpath "$1"); C=$2; E=$(realpath -m "$3")
SOI=$(realpath "$0")
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
V=docs/procedures/P3-premier-test-v1
P=prereg/P3-premier-test-i-a-v1.md; CFG=prereg/P3-premier-test-config-v1.json; CONSIGNES=prereg/P3-consignes-v1.md
GO=GO-2026-10-04-08; REG=R-192
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
mkdir -p "$E/H" && cd "$E" || exit 2
git clone -q --no-local "$SRC" depot && cd depot && git checkout -q "$C" && git checkout -q -B main || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
echo "C = $(git rev-parse HEAD)"
# scripts éprouvés : les copies versées à C (avant que la copie jouée du scellement n'en change les lignes H, DEPOT et DISTANT)
for s in sceller_p3_v1.sh verifications_p3_v1.py; do echo "script éprouvé : $s $(sha256sum "$V/$s" | cut -d' ' -f1)"; done
echo "script éprouvé : $(basename "$SOI") $(sha256sum "$SOI" | cut -d' ' -f1)"
CHAINE=$(sed -n '/^CHAINE="/,/"$/p' "$V/sceller_p3_v1.sh" | tr -d '"' | sed 's/^CHAINE=//')
for s in $CHAINE; do cp "$V/$s" "$E/H/$s" || { echo "copie versée absente : $s"; exit 2; }; done
grep -q "^[A-Z_]*=\"\{0,1\}A_EPINGLER" "$E/H/controles_avant_depense_p3_v1.sh" && { echo "épingles absentes"; exit 2; }
sed -e "s|^H=.*|H=$E/H|" -e "s|^DEPOT=.*|DEPOT=$E/depot|" -e "s|^DISTANT=.*|DISTANT=$E/distant.git|" "$V/sceller_p3_v1.sh" > "$E/H/sceller_p3_v1.sh"
echo "lignes changées dans la copie du scellement : $(diff "$V/sceller_p3_v1.sh" "$E/H/sceller_p3_v1.sh" | grep -c '^>')"
grep -n "controle-ia-travail\|github" "$E/H/sceller_p3_v1.sh" && { echo "COPIE NON SÛRE"; exit 2; }
cp "$E/H/sceller_p3_v1.sh" "$V/sceller_p3_v1.sh" && (cd "$V" && sha256sum sceller_p3_v1.sh > sceller_p3_v1.sh.sha256)
git add -A "$V" && git commit -qm "essai : copie du scellement du banc" || exit 2
J=$(git rev-parse HEAD); echo "J = $J"
git clone -q --bare . "$E/distant.git" && git remote set-url origin "$E/distant.git" && git fetch -q origin || exit 2
[ "$(git remote get-url --push origin)" = "$E/distant.git" ] || { echo "origine de poussée inattendue"; exit 2; }
CTL=$E/H/controles_avant_depense_p3_v1.sh
epingle() { sed -n "s/^$1=\"\{0,1\}\([^\"#]*\)\"\{0,1\}.*/\1/p" "$CTL" | sed 's/[[:space:]]*$//'; }
RELU=$(epingle CANDIDAT_RELU_CHEMIN); CFG_RELUE=$(epingle CONFIG_RELUE_CHEMIN); CONS_RELUES=$(epingle CONSIGNES_RELUES_CHEMIN)
LJ=$(epingle REPETITION_JOUET_CHEMIN); CODE_RELU=$(epingle CODE_RELU)
SIX=("$P" "$P.sha256" "$CFG" "$CFG.sha256" "$CONSIGNES" "$CONSIGNES.sha256")
NON_CONFORMES=0
passage() {   # $1 nom, $2 code attendu, $3 motif attendu dans la sortie, puis les arguments du scellement
    local n=$1 attendu=$2 motif=$3; shift 3
    local avant c v reste
    avant=$(git rev-parse HEAD)
    bash "$E/H/sceller_p3_v1.sh" "$@" > "$E/scellement-$n.log" 2>&1; c=$?
    reste=$(ls "${SIX[@]}" 2>/dev/null | tr '\n' ' ')
    v="CONFORME"
    [ "$c" = "$attendu" ] || v="NON CONFORME (code $c, attendu $attendu)"
    if [ -n "$motif" ] && ! grep -qF -- "$motif" "$E/scellement-$n.log"; then v="NON CONFORME (motif « $motif » absent)"; fi
    if [ "$attendu" != 0 ]; then
        [ "$(git rev-parse HEAD)" = "$avant" ] || [ "$n" = S03-poussee-refusee ] || v="NON CONFORME (commit fait malgré l'arrêt)"
        [ -z "$reste" ] || [ "$n" = S07-prereg-present ] || [ "$n" = S07b-consignes-presentes ] || [ "$n" = S03-poussee-refusee ] \
            || v="NON CONFORME (restes : $reste)"
    fi
    [ "$v" = CONFORME ] || NON_CONFORMES=$((NON_CONFORMES + 1))
    echo "$n : code $c ; $v"
    grep -v '^$' "$E/scellement-$n.log" | tail -2 | cut -c1-200 | sed 's/^/    | /'
}
remise() {   # clone et dépôt nu remis sur un commit (J par défaut) ; fichiers du scellement retirés ; adresses rétablies
    git checkout -q -f main; git reset -q --hard "${1:-$J}"; rm -f "${SIX[@]}"
    git config --unset-all remote.origin.pushurl 2>/dev/null; git remote set-url origin "$E/distant.git"; git remote set-url --push origin "$E/distant.git"
    git push -q -f "$E/distant.git" "${1:-$J}:refs/heads/main" || { echo "REMISE IMPOSSIBLE (dépôt nu)"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
    git fetch -q origin
    [ "$(git rev-parse origin/main)" = "$(git rev-parse "${1:-$J}")" ] || { echo "REMISE IMPOSSIBLE (origin/main)"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
}
resceller() { local f; for f in "$@"; do (cd "$(dirname "$f")" && sha256sum "$(basename "$f")" > "$(basename "$f").sha256"); done; }
cp "$CTL" "$E/ctl-sauve.sh"
epingle_versee() {   # $1 expression sed sur les contrôles, $2 message ; une ligne exactement changée ; bloc-notes et copie versée
    cp "$CTL" "$E/ctl-avant-epingle.sh"
    sed -i "$1" "$CTL" || return 1
    [ "$(diff "$E/ctl-avant-epingle.sh" "$CTL" | grep -c '^>')" = 1 ] || { echo "épingle : une ligne exactement attendue"; return 1; }
    cp "$CTL" "$V/" && resceller "$V/controles_avant_depense_p3_v1.sh" && git commit -qam "essai : $2" && remise "$(git rev-parse HEAD)"
}
candidat_change() {   # $1 expression sed sur le candidat (rescellé, ré-épinglé), $2 message ; le journal de la répétition
    # jouet nomme alors le candidat changé (rescellé, ré-épinglé) : sans quoi la garde de la répétition arrête avant la
    # garde visée
    local ancien nouveau nom
    nom=$(basename "$RELU"); ancien=$(sha256sum "$RELU" | cut -d' ' -f1)
    sed -i "$1" "$RELU" && resceller "$RELU" && git add -A "$RELU" "$RELU.sha256" || return 1
    nouveau=$(sha256sum "$RELU" | cut -d' ' -f1)
    [ "$nouveau" != "$ancien" ] || { echo "candidat inchangé"; return 1; }
    epingle_versee "s|^CANDIDAT_RELU=[0-9a-f]\{64\}|CANDIDAT_RELU=$nouveau|" "$2" || return 1
    sed -i "s|^candidat répété : $nom $ancien\$|candidat répété : $nom $nouveau|" "$LJ" && resceller "$LJ" || return 1
    grep -qxF "candidat répété : $nom $nouveau" "$LJ" || { echo "journal de la répétition : ligne du candidat non changée"; return 1; }
    epingle_versee "s|^REPETITION_JOUET=[0-9a-f]\{64\}|REPETITION_JOUET=$(sha256sum "$LJ" | cut -d' ' -f1)|" "$2 (journal de la répétition)"
}
retour() { cp "$E/ctl-sauve.sh" "$CTL"; remise; }
passage S00-sain 0 "poussé ; préenregistrement"
S=$(git rev-parse HEAD)
if [ "$S" != "$J" ] && [ "$(git rev-parse "$S^")" = "$J" ] && [ "$(git -C "$E/distant.git" rev-parse main)" = "$S" ] \
   && [ "$(git diff --name-only --no-renames "$J" "$S" | sort | tr '\n' ' ')" = "$(printf '%s\n' "${SIX[@]}" | sort | tr '\n' ' ')" ] \
   && cmp -s "$P" "$RELU" && cmp -s "$CFG" "$CFG_RELUE" && cmp -s "$CONSIGNES" "$CONS_RELUES" \
   && [ -z "$(git status --porcelain --untracked-files=no)" ]; then
    echo "    S $S : enfant de J, poussé, six fichiers seulement, copies exactes du candidat, de la configuration et des consignes relus, arbre propre : CONFORME"
else echo "    S $S : NON CONFORME (parent, poussée, contenu ou copie)"; NON_CONFORMES=$((NON_CONFORMES + 1)); fi
remise
echo "# essai" >> README.md
passage S01-arbre-sale 2 "arbre suivi non propre"
git checkout -q -- README.md
printf '%s  index.json\n' "$(printf '0%.0s' {1..64})" > docs/sources/invites-2606.08892-v1/index.json.sha256
git commit -qam "essai : sceau faussé hors de la chaîne" && remise "$(git rev-parse HEAD)"
passage S02-sceau-fausse-verifier-arbre 2 "ÉCHEC"
remise
# poussée refusée par le dépôt distant (adresse admise ; crochet qui refuse), puis crochet retiré
printf '#!/bin/sh\necho "refus (essai)" >&2\nexit 1\n' > "$E/distant.git/hooks/pre-receive" && chmod +x "$E/distant.git/hooks/pre-receive"
passage S03-poussee-refusee 2 "poussée de S en échec"
rm -f "$E/distant.git/hooks/pre-receive"
remise
epingle_versee "s|^CANDIDAT_RELU=[0-9a-f]\{64\}|CANDIDAT_RELU=$(printf '1%.0s' {1..64})|" "épingle du candidat fausse" || { echo "S04 : montage impossible"; exit 2; }
passage S04-epingle-candidat-fausse 2 "$RELU ≠ épingle"
retour
epingle_versee "s|^CONFIG_RELUE=[0-9a-f]\{64\}|CONFIG_RELUE=$(printf '2%.0s' {1..64})|" "épingle de la configuration fausse" || { echo "S04b : montage impossible"; exit 2; }
passage S04b-epingle-configuration-fausse 2 "$CFG_RELUE ≠ épingle"
retour
epingle_versee "s|^CONSIGNES_RELUES=[0-9a-f]\{64\}|CONSIGNES_RELUES=$(printf '7%.0s' {1..64})|" "épingle des consignes fausse" || { echo "S04c : montage impossible"; exit 2; }
passage S04c-epingle-consignes-fausse 2 "$CONS_RELUES ≠ épingle"
retour
echo "# modifié" >> "$E/H/recuperation_p3_v1.sh"
passage S05-recuperation-non-versee 2 "recuperation_p3_v1.sh du bloc-notes ≠ copie versée"
cp "$V/recuperation_p3_v1.sh" "$E/H/recuperation_p3_v1.sh"
git commit -q --allow-empty -m "essai : commit local non poussé"
passage S06-head-en-avance 2 "HEAD ≠ origin/main"
remise
echo x > "$P"
passage S07-prereg-present 2 "existe déjà (R12)"
rm -f "$P"
echo x > "$CONSIGNES"
passage S07b-consignes-presentes 2 "$CONSIGNES existe déjà (R12)"
rm -f "$CONSIGNES"
RF=$(grep -o 'P3-premier-test-v1-[a-z0-9-]*-v1\.[a-z]*' "$CTL" | head -1)
[ -n "$RF" ] || { echo "aucun rapport de la contre-lecture épinglé"; exit 2; }
git rm -q "prereg/contre-lectures/$RF" "prereg/contre-lectures/$RF.sha256" && git commit -qm "essai : rapport retiré" && remise "$(git rev-parse HEAD)"
passage S08-rapport-epingle-absent 2 "$RF non suivi à HEAD"
remise
# GO de calcul et décision de Lazar (module commun) : ligne de décision absente, GO d'un autre type, GO révoqué
sed -i "/^| $REG |/d" registres/decisions.md
git commit -qam "essai : décision de Lazar retirée du registre" && remise "$(git rev-parse HEAD)"
passage S09-decision-absente 2 "GO de calcul et décision de Lazar non conformes"
remise
sed -i "/^| $GO |/s/| calcul |/| revendication |/" registres/go.md
git commit -qam "essai : GO de calcul d'un autre type" && remise "$(git rev-parse HEAD)"
passage S09b-go-autre-type 2 "GO de calcul et décision de Lazar non conformes"
remise
echo "| GO-2026-10-17-98 | 2026-10-17 | révocation | révoque $GO (essai) | — | — | Lazar | essai |" >> registres/go.md
git commit -qam "essai : GO de calcul révoqué" && remise "$(git rev-parse HEAD)"
passage S09c-go-revoque 2 "$GO révoqué"
remise
sed -i "s|^REPETITION_JOUET=[0-9a-f]\{64\}|REPETITION_JOUET=A_EPINGLER|" "$CTL"
passage S13-epingle-restee 2 "A_EPINGLER"
cp "$E/ctl-sauve.sh" "$CTL"
AUTRE=$(git rev-parse "$(git rev-list --max-count=1 HEAD -- src/controle_ia/premier_test_ia/run.py)^")
epingle_versee "s|^CODE_RELU=[0-9a-f]\{40\}|CODE_RELU=$AUTRE|" "code relu autre" || { echo "S14 : montage impossible"; exit 2; }
passage S14-code-relu-autre 2 "arbre gelé de HEAD ≠ code relu"
retour
echo x >> "$LJ" && resceller "$LJ" && git commit -qam "essai : journal altéré" && remise "$(git rev-parse HEAD)"
passage S15-journal-repetition-altere 2 "journal de la répétition jouet absent, d'une autre empreinte que l'épingle"
remise
sed -i 's|^RAPPORTS_ATTENDUS="|RAPPORTS_ATTENDUS="T0.5-pilote-v1-autre-famille-v1.md='"$(printf '3%.0s' {1..64})"' |' "$CTL"
passage S16-rapport-autre-famille 2 "hors de la famille de la contre-lecture"
cp "$E/ctl-sauve.sh" "$CTL"
git rm -q --cached "$LJ" "$LJ.sha256" && git commit -qm "essai : journal non suivi" && remise "$(git rev-parse HEAD)"
[ -f "$LJ" ] && [ -z "$(git ls-files -- "$LJ")" ] || { echo "S17 : montage impossible"; exit 2; }
passage S17-journal-non-suivi 2 "non suivi à HEAD"
remise
sed -i "s/^commit du code répété : .*/commit du code répété : $AUTRE/" "$LJ" && resceller "$LJ" \
    && epingle_versee "s|^REPETITION_JOUET=[0-9a-f]\{64\}|REPETITION_JOUET=$(sha256sum "$LJ" | cut -d' ' -f1)|" "journal d'un autre commit, épinglé" \
    || { echo "S18 : montage impossible"; exit 2; }
passage S18-journal-autre-commit 2 "journal de la répétition jouet non conforme : ligne absente ou en double : commit du code répété"
retour
sed -i "s|^REPETITION_JOUET_CHEMIN=.*|REPETITION_JOUET_CHEMIN=diag/repetition-jouet-p3-v1.log|" "$CTL"
passage S19-journal-hors-du-dossier 2 "code relu ou répétition jouet non épinglés"
cp "$E/ctl-sauve.sh" "$CTL"
# dépôt distant injoignable à l'adresse admise : le fetch échoue, le piège ERR arrête (dépôt nu déplacé, puis remis)
mv "$E/distant.git" "$E/distant.git.cache"
passage S20-arret-avant-le-piege 2 "arrêt du scellement (ligne"
mv "$E/distant.git.cache" "$E/distant.git"
remise
printf '#!/bin/sh\nexit 1\n' > .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
passage S21-commit-refuse 2 "échec avant le commit : fichiers créés retirés"
git diff --cached --quiet && echo "    index propre après S21 : CONFORME" || { echo "    S21 : NON CONFORME (fichiers laissés dans l'index)"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
rm -f .git/hooks/pre-commit
remise
passage S10-avec-argument 2 "usage" "$GO"
# le candidat relu, changé et ré-épinglé : chaque garde sur son contenu
EXPR_RF="s|\\(\`prereg/contre-lectures/$RF\` (\`\\)[0-9a-f]\\{64\\}|\\1$(printf '4%.0s' {1..64})|"
candidat_change "$EXPR_RF" "candidat qui cite un autre rapport" || { echo "S22 : montage impossible"; exit 2; }
passage S22-rapport-non-cite 2 "non cité par le candidat"
retour
candidat_change "s|Commit du code d'analyse : \`$CODE_RELU\`|Commit du code d'analyse : \`$AUTRE\`|" "candidat qui cite un autre code" || { echo "S23 : montage impossible"; exit 2; }
passage S23-candidat-autre-code 2 "le candidat relu ne cite pas le code relu"
retour
candidat_change "/^- GO de calcul et décision de Lazar :/d" "candidat sans la ligne du GO" || { echo "S24 : montage impossible"; exit 2; }
passage S24-candidat-sans-go 2 "intitulé « GO de calcul et décision de Lazar » cité zéro ou plusieurs fois"
retour
candidat_change "s|^- GO de calcul et décision de Lazar : \`$GO\`|- GO de calcul et décision de Lazar : \`GO-2026-10-17-97\`|" "candidat qui cite un autre GO" || { echo "S24b : montage impossible"; exit 2; }
passage S24b-candidat-autre-go 2 "GO-2026-10-17-97 absent, en double ou mal formé"
retour
candidat_change "s|^## Contre-lecture$|## Contre-lecture retirée|" "candidat sans section Contre-lecture" || { echo "S25 : montage impossible"; exit 2; }
passage S25-candidat-non-conforme-r1-r2 2 "non conforme à R1/R2"
retour
S1=$(sed -n '/^CHAINE="/s/^CHAINE="\([^ ]*\) .*/\1/p' "$V/sceller_p3_v1.sh")
printf '%s  %s\n' "$(printf '5%.0s' {1..64})" "$S1" > "$V/$S1.sha256" && git commit -qam "essai : sceau d'une copie versée faussé" && remise "$(git rev-parse HEAD)"
passage S02b-sceau-d-une-copie-versee-fausse 2 "sceau d'une copie versée non conforme"
remise
sed -i '/^FIN DE LA RÉPÉTITION$/d' "$LJ" && resceller "$LJ" \
    && epingle_versee "s|^REPETITION_JOUET=[0-9a-f]\{64\}|REPETITION_JOUET=$(sha256sum "$LJ" | cut -d' ' -f1)|" "journal inachevé, épinglé" \
    || { echo "S26 : montage impossible"; exit 2; }
passage S26-journal-inacheve 2 "ligne absente ou en double : FIN DE LA RÉPÉTITION"
retour
sed -i "s|^CANDIDAT_RELU_CHEMIN=brouillons/|CANDIDAT_RELU_CHEMIN=prereg/|" "$CTL"
passage S27-candidat-hors-des-brouillons 2 "candidat, configuration ou consignes relus non épinglés"
cp "$E/ctl-sauve.sh" "$CTL"
sed -i "s|^CONFIG_RELUE=[0-9a-f]\{64\}|CONFIG_RELUE=$(printf '6%.0s' {1..63})|" "$CTL"
passage S27b-epingle-de-63-caracteres 2 "candidat, configuration ou consignes relus non épinglés"
cp "$E/ctl-sauve.sh" "$CTL"
sed -i "s|^CONSIGNES_RELUES_CHEMIN=brouillons/|CONSIGNES_RELUES_CHEMIN=prereg/|" "$CTL"
passage S27c-consignes-hors-des-brouillons 2 "candidat, configuration ou consignes relus non épinglés"
cp "$E/ctl-sauve.sh" "$CTL"
sed -i 's|^RAPPORTS_ATTENDUS="\([^ "]*\)[^"]*"|RAPPORTS_ATTENDUS="\1"|' "$CTL"
passage S28-une-seule-paire 2 "rapports épinglés : au moins deux attendus"
cp "$E/ctl-sauve.sh" "$CTL"
printf '%s *%s\n' "$(sha256sum "$RELU" | cut -d' ' -f1)" "$(basename "$RELU")" > "$RELU.sha256" && git commit -qam "essai : sceau du candidat en mode binaire" && remise "$(git rev-parse HEAD)"
passage S29-sceau-du-candidat-autre-forme 2 "$RELU ≠ épingle, ou sceau différent de la ligne exacte"
remise
printf '%s *%s\n' "$(sha256sum "$CFG_RELUE" | cut -d' ' -f1)" "$(basename "$CFG_RELUE")" > "$CFG_RELUE.sha256" && git commit -qam "essai : sceau de la configuration en mode binaire" && remise "$(git rev-parse HEAD)"
passage S29b-sceau-de-la-configuration-autre-forme 2 "$CFG_RELUE ≠ épingle, ou sceau différent de la ligne exacte"
remise
printf '%s *%s\n' "$(sha256sum "$CONS_RELUES" | cut -d' ' -f1)" "$(basename "$CONS_RELUES")" > "$CONS_RELUES.sha256" && git commit -qam "essai : sceau des consignes en mode binaire" && remise "$(git rev-parse HEAD)"
passage S29c-sceau-des-consignes-autre-forme 2 "$CONS_RELUES ≠ épingle, ou sceau différent de la ligne exacte"
remise
# configuration relue qui cite d'autres consignes (rescellée, ré-épinglée) : le run s'arrêterait (R11)
python3 - "$CFG_RELUE" <<'PYCFG' && resceller "$CFG_RELUE" || { echo "S40 : montage impossible"; exit 2; }
import json, sys
c = json.load(open(sys.argv[1], encoding="utf-8"))
c["consignes_sha256"] = "8" * 64
open(sys.argv[1], "w", encoding="utf-8").write(json.dumps(c, indent=1, sort_keys=True, ensure_ascii=False) + "\n")
PYCFG
git add -A "$CFG_RELUE" "$CFG_RELUE.sha256" && epingle_versee "s|^CONFIG_RELUE=[0-9a-f]\{64\}|CONFIG_RELUE=$(sha256sum "$CFG_RELUE" | cut -d' ' -f1)|" "configuration qui cite d'autres consignes" \
    || { echo "S40 : montage impossible"; exit 2; }
passage S40-configuration-autres-consignes 2 "la configuration relue ne cite pas les consignes relues"
retour
# ligne lue d'abord dans un fichier à part (grep refuse d'écrire dans le fichier qu'il lit), montage vérifié
grep "^| $REG |" registres/decisions.md > "$E/reg.txt" && cat "$E/reg.txt" >> registres/decisions.md \
    && [ "$(grep -c "^| $REG |" registres/decisions.md)" = 2 ] && git commit -qam "essai : $REG en double" && remise "$(git rev-parse HEAD)" \
    || { echo "S37 : montage impossible"; exit 2; }
passage S37-ligne-de-decision-en-double 2 "GO de calcul et décision de Lazar non conformes"
remise
# sceaux produits ≠ épingles : un faux cp, en tête du PATH pour ce seul passage, altère la copie de la configuration ;
# le piège de sortie retire les fichiers créés (restes nuls exigés par passage)
mkdir -p "$E/faux" && cat > "$E/faux/cp" <<'FAUXCP'
#!/usr/bin/env bash
/bin/cp "$@" || exit $?
case "${@: -1}" in *P3-premier-test-config-v1.json) echo " " >> "${@: -1}" ;; esac
FAUXCP
chmod +x "$E/faux/cp"
PATH="$E/faux:$PATH" passage S38-sceaux-produits-differents-des-epingles 2 "sceaux du préenregistrement, de la configuration ou des consignes ≠ épingles"
remise
echo x >> "prereg/contre-lectures/$RF" && resceller "prereg/contre-lectures/$RF" && git commit -qam "essai : rapport altéré" && remise "$(git rev-parse HEAD)"
passage S30-rapport-altere 2 "rapport $RF : empreinte différente de l'épingle"
remise
echo x > prereg/contre-lectures/P3-premier-test-v1-relecture-autre-v1.md && resceller prereg/contre-lectures/P3-premier-test-v1-relecture-autre-v1.md \
    && git add prereg/contre-lectures/ && git commit -qm "essai : rapport de la famille non épinglé" && remise "$(git rev-parse HEAD)"
passage S31-rapport-non-epingle 2 "≠ épinglés"
remise
git push -q "$E/distant.git" "$J:refs/heads/calcul/p3-reel-v1"
passage S32-branche-de-resultats-presente 2 "branche calcul/p3-reel-v1 : code 0"
git -C "$E/distant.git" branch -D calcul/p3-reel-v1 > /dev/null
remise
echo "# essai" >> "$V/recuperation_p3_v1.sh" && resceller "$V/recuperation_p3_v1.sh" && cp "$V/recuperation_p3_v1.sh" "$E/H/" \
    && git commit -qam "essai : copie versée de la récupération changée" && remise "$(git rev-parse HEAD)"
passage S33-script-repete-autre-que-la-copie 2 "script répété ≠ copie versée : recuperation_p3_v1.sh"
git show "$J:$V/recuperation_p3_v1.sh" > "$E/H/recuperation_p3_v1.sh"
remise
candidat_change 's/^- Tâches de P3 : \(.*\)$/&\n- Tâches de P3 : \1/' "candidat qui cite deux fois les tâches" || { echo "S35 : montage impossible"; exit 2; }
passage S35-intitule-en-double 2 "intitulé « Tâches de P3 » cité zéro ou plusieurs fois"
retour
candidat_change 's/^- Chemin des consignes de P3 : .*$//' "candidat sans le chemin des consignes" || { echo "S35b : montage impossible"; exit 2; }
passage S35b-intitule-absent 2 "intitulé « Chemin des consignes de P3 » cité zéro ou plusieurs fois"
retour
# adresse de origin autre que le dépôt de travail : un dépôt nu local nommé comme la copie publique (jamais la vraie
# adresse : si la garde régressait, rien ne partirait hors du banc), en lecture, en poussée, puis en seconde adresse de
# poussée ; le dépôt nu doit rester vide
git init -q --bare "$E/lciric/controle-ia.git"
vide() { [ -z "$(git -C "$E/lciric/controle-ia.git" for-each-ref)" ] && echo "    copie publique simulée restée vide : CONFORME" || { echo "    copie publique simulée NON VIDE : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }; }
git remote set-url origin "$E/lciric/controle-ia.git"
passage S39-origin-copie-publique 2 "adresse de origin en lecture"
vide; remise
git remote set-url --push origin "$E/lciric/controle-ia.git"
passage S39b-poussee-vers-la-copie-publique 2 "adresse de origin --push"
vide; remise
git remote set-url --add --push origin "$E/lciric/controle-ia.git"
[ "$(git remote get-url --all --push origin | wc -l)" = 2 ] || { echo "S39c : montage impossible"; exit 2; }
passage S39c-seconde-adresse-de-poussee 2 "une seule adresse admise"
vide; remise
passage S34-sain-apres-les-artefacts 0 "poussé ; préenregistrement"
remise
git status --short | head -5 | sed 's/^/    reste : /'
cd "$E" && rm -rf "$E/depot" "$E/distant.git"
echo "FIN DU BANC DU SCELLEMENT DE P3 ; cas non conformes : $NON_CONFORMES"
[ "$NON_CONFORMES" = 0 ] || exit 1
