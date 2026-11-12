#!/usr/bin/env bash
# Banc des contrôles avant dépense du pilote de T0.5 (R5 ; relecture R2, CH-03), sur le modèle du banc des contrôles v7
# de la revalidation : un cas sain et des artefacts, chacun joué contre le script entier sur un dépôt jetable cloné du
# commit des préalables C et un dépôt nu local. La copie jouée est la copie versée à C (épingles réelles), dont changent
# seulement : l'adresse du dépôt, le bloc-notes (normaliseur versé), la suite complète des tests (bouchon qui écrit
# « N passed », N lu dans le texte, ou FAUX_SUITE) et le contrôle des vrais tokeniseurs (bouchon) : ces deux-là
# tournent en vrai dans la répétition finale à blanc. Décision de Lazar sur N-019 simulée dans le clone : GO fictif
# GO-2026-10-12-99 (revendication, Lazar, option (a)), colonne d'état exacte, ligne R-990. Préenregistrement sain
# produit par le générateur versé, en mode reel, normalisé égal à l'épingle. Chaque artefact touche d'abord la base
# (registres, fichiers cités ; un commit), puis le texte ou la configuration (commit S qui n'ajoute que les quatre
# fichiers), puis éventuellement le dépôt distant ; verdict : code attendu et ligne KO attendue présente.
# Usage : essais_controles_pilote_v1.sh DEPOT_SOURCE C RACINE_NEUVE
set -uo pipefail
SRC=$1; C=$2; R=$3
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
V=docs/procedures/pilote-T0.5-v1
P=prereg/T0.5-pilote-8B-v1.md; CFG=prereg/T0.5-pilote-config-v1.json; TACHES=donnees/t05-pilote-v1/taches-pilote-60-v1.json
CL=prereg/contre-lectures; GO=GO-2026-10-12-99; REG=R-990
LOGJ=$V/repetition-jouet-pilote-v1.log
[ -e "$R" ] && { echo "$R existe déjà (R12)"; exit 2; }
mkdir -p "$R/H" && cd "$R" || exit 2
git clone -q --no-local "$SRC" source && cd source && git checkout -q "$C" && git checkout -q -B main || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
echo "C = $(git rev-parse HEAD)"
grep -q "A_EPINGLER" "$V/controles_avant_depense_pilote_v1.sh" && { echo "épingles absentes de la copie versée des contrôles"; exit 2; }
cp "$V/normaliser_pilote_v1.py" "$R/H/"
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
git add -A registres && git commit -qm "essai : GO fictif de Lazar sur N-019" || exit 2
C1=$(git rev-parse HEAD)
git clone -q --bare . "$R/distant.git" || exit 2
# copie jouée des contrôles : quatre lignes changent (adresse, bloc-notes, bouchons de la suite et des tokeniseurs)
python3 - "$V/controles_avant_depense_pilote_v1.sh" "$R/controles-essai.sh" "$R/distant.git" "$R/H" <<'PYCOPIE' || exit 2
import re, sys
from pathlib import Path
src, dst, depot, h = sys.argv[1:5]
t = Path(src).read_text(encoding="utf-8")
def rep(a, b, regex=False):
    global t
    n = len(re.findall(a, t, re.M)) if regex else t.count(a)
    assert n == 1, (n, a)
    t = re.sub(a, lambda _: b, t, flags=re.M) if regex else t.replace(a, b)
rep(r"^DEPOT=.*$", f"DEPOT={depot}", regex=True)
rep(r"^H=.*$", f"H={h}", regex=True)
rep('PYTHONPATH=src "$PY" -m pytest -q -p no:cacheprovider > "$D/../suite-$$.txt" 2>&1; cs=$?',
    'printf \'%s passed in 1.00s\\n\' "${FAUX_SUITE:-$a}" > "$D/../suite-$$.txt"; cs=0   # bouchon du banc')
rep('HF_HOME="$D/../cache-hf-$$" PYTHONPATH=src "$PY" - "$CFG" <<\'EOF\'', 'cat > /dev/null <<\'EOF\'   # bouchon du banc')
Path(dst).write_text(t, encoding="utf-8")
PYCOPIE
echo "lignes changées dans la copie des contrôles : $(diff "$V/controles_avant_depense_pilote_v1.sh" "$R/controles-essai.sh" | grep -c '^>')"
epingle() { sed -n "s/^$1=\"\{0,1\}\([^\"#]*\)\"\{0,1\}.*/\1/p" "$R/controles-essai.sh" | sed 's/[[:space:]]*$//'; }
RELU=$(epingle CANDIDAT_RELU_CHEMIN); NORMALISE=$(epingle CANDIDAT_NORMALISE); RAPPORTS=$(epingle RAPPORTS_ATTENDUS)
ETAT=$(for x in $RAPPORTS; do case $x in *etat-des-lieux*) printf '%s,' "$x" ;; esac; done); ETAT=${ETAT%,}
REL=$(for x in $RAPPORTS; do case $x in *relecture-b8*) printf '%s,' "$x" ;; esac; done); REL=${REL%,}
"$PY" -I -c "import numpy as np; print(np.random.SeedSequence().entropy)" > "$R/entropie.txt"
"$PY" -I "$V/remplir_pilote_v1.py" . "$C1" reel "$(date -u '+%Y-%m-%d %H:%M UTC')" "$R/entropie.txt" "$R/prereg-sain.md" \
    "$R/config-saine.json" --taches "$TACHES" --rapports-etat "$ETAT" --rapports-relecture "$REL" --candidat-relu "$RELU" \
    --go "$GO" --registre "$REG" > "$R/remplissage.json" || { echo "génération du texte sain impossible"; exit 2; }
NS=$("$PY" -I "$R/H/normaliser_pilote_v1.py" "$R/prereg-sain.md")
echo "texte sain : normalisé $NS ; épingle $NORMALISE"
[ "$NS" = "$NORMALISE" ] || { echo "le texte sain ne se normalise pas en l'épingle"; exit 2; }
DEBUT_BANC=$(date +%s)
resceller() { local f; for f in "$@"; do (cd "$(dirname "$f")" && sha256sum "$(basename "$f")" > "$(basename "$f").sha256"); done; }
jouer() {   # $1 nom, $2 code attendu, $3 motif KO attendu (vide : cas sain), $4 base, $5 texte, $6 après, $7 copie des contrôles
    local nom=$1 attendu=$2 motif=$3 base=$4 texte=$5 apres=${6:-} ctl=${7:-$R/controles-essai.sh}
    # les dates du texte sain doivent rester à moins de 7 200 s de chaque S (parties masquées) : banc borné (VH-06)
    [ $(( $(date +%s) - DEBUT_BANC )) -lt 6600 ] || { echo "$nom : banc trop long (texte sain daté de plus de 6 600 s) : ARRÊT"; exit 2; }
    git checkout -q -B "art-$nom" "$C1" || { echo "$nom : montage impossible"; return; }
    eval "$base"
    if [ -n "$(git status --porcelain)" ]; then git add -A . && git commit -qm "essai : base $nom" || { echo "$nom : commit de base impossible"; return; }; fi
    cp "$R/prereg-sain.md" "$P" && cp "$R/config-saine.json" "$CFG" || { echo "$nom : copie impossible"; return; }
    eval "$texte"
    resceller "$P" "$CFG"
    git add "$P" "$P.sha256" "$CFG" "$CFG.sha256" && git commit -qm "essai : S $nom" || { echo "$nom : commit S impossible"; return; }
    local s; s=$(git rev-parse HEAD)
    git push -q "$R/distant.git" "art-$nom" || { echo "$nom : poussée impossible"; return; }
    eval "$apres"
    bash "$ctl" "$s" "$R/clone-$nom" ${MODE_CTL:-} > "$R/sortie-$nom.txt" 2>&1; local c=$?
    rm -rf "$R/clone-$nom"
    local verdict="CONFORME"
    [ "$c" = "$attendu" ] || verdict="NON CONFORME (code $c, attendu $attendu)"
    if [ -n "$motif" ] && ! grep -q "^KO .*$motif" "$R/sortie-$nom.txt"; then verdict="NON CONFORME (KO « $motif » absent)"; fi
    if [ -z "$motif" ] && [ "$attendu" = 0 ] && ! tail -1 "$R/sortie-$nom.txt" | grep -qx "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES"; then
        verdict="NON CONFORME (dernière ligne)"; fi
    echo "$nom : code $c ; $(grep -c '^OK' "$R/sortie-$nom.txt") OK, $(grep -c '^KO' "$R/sortie-$nom.txt") KO ; $verdict"
    grep '^KO' "$R/sortie-$nom.txt" | sed 's/^/    /' | cut -c1-220
}
copie_ctl() {   # $1 sortie, $2 expression sed sur la copie jouée (épingle changée pour un artefact) : une ligne exactement
    sed -e "$2" "$R/controles-essai.sh" > "$1"
    local n; n=$(diff "$R/controles-essai.sh" "$1" | grep -c '^>')
    [ "$n" = 1 ] || { echo "COPIE NON CONFORME : $1 change $n ligne(s) au lieu d'une (VH-06) : ARRÊT"; exit 2; }
    echo "    (copie $1 : une ligne de plus changée)"
}
DATE_S=$(sed -n "s/^- Date (UTC) : \([0-9-]* [0-9:]*\) (.*/\1/p" "$R/prereg-sain.md")
VIEILLE=$(date -u -d "$DATE_S UTC 3 hours ago" '+%Y-%m-%d %H:%M')
NT=$(sed -n "s/^- Tests attendus : \`\([0-9]*\)\`.*/\1/p" "$R/prereg-sain.md")
INDEX_SHA=$(sha256sum docs/sources/invites-2606.08892-v1/index.json | cut -d' ' -f1)
UN_RAPPORT=$(for x in $RAPPORTS; do case $x in *relecture-b8*) echo "${x#*=}"; break ;; esac; done)
NOM_RAPPORT=$(for x in $RAPPORTS; do case $x in *relecture-b8*) echo "${x%%=*}"; break ;; esac; done)
AUTRE_CODE=$(git rev-list --max-count=1 "$C1" -- src/controle_ia/environnements/lancer_pilote_a.py)
AUTRE_CODE=$(git rev-parse "$AUTRE_CODE^")
LOG_AUTRE=$(sed "s/^commit du code répété : .*/commit du code répété : $AUTRE_CODE/" "$LOGJ" | sha256sum | cut -d' ' -f1)
echo "date de S $DATE_S ; tests $NT ; index $INDEX_SHA ; commit antérieur au dernier changement du lanceur du pilote : $AUTRE_CODE"
N19='s/^(\| N-019 \|.*)\| tranché \(a\) par Lazar : [^|]*\|$/\1'
jouer A00-sain 0 "" ":" ":"
jouer A01-go-absent 1 "absent, en double ou mal formé" "sed -i '/^| $GO |/d' registres/go.md" ":"
jouer A02-go-autre-type 1 ": calcul, Lazar" "sed -i 's/^| $GO | 2026-10-12 | revendication |/| $GO | 2026-10-12 | calcul |/' registres/go.md" ":"
jouer A03-go-option-b 1 ": revendication, Lazar" "sed -i 's/| N-019, option (a) (essai) |/| N-019, option (b) (essai) |/' registres/go.md" ":"
jouer A04-go-revoque 1 "GO-2026-10-12-99 révoqué" "echo '| GO-2026-10-12-98 | 2026-10-12 | révocation | révoque $GO (essai) | — | — | Lazar | essai |' >> registres/go.md" ":"
jouer A05-go-calcul-revoque 1 "GO-2026-10-04-08 révoqué" "echo '| GO-2026-10-12-97 | 2026-10-12 | révocation | révoque GO-2026-10-04-08 (essai) | — | — | Lazar | essai |' >> registres/go.md" ":"
jouer A05b-go-revoque-ligne-mal-formee 1 "GO-2026-10-12-99 révoqué" "echo '| GO-2026-10-12-98 | 2026-10-12 | révocation de $GO (essai) |' >> registres/go.md" ":"
jouer A05c-ligne-go-qui-mentionne-une-revocation 0 "" "echo '| GO-2026-10-12-97 | 2026-10-12 | revendication | essai : aucune révocation de $GO | — | — | Lazar | essai |' >> registres/go.md" ":"
jouer A06-n019-forme-inexacte 1 "N-019 : colonne d'état" "sed -i -E '${N19}| tranché le 2026-10-12 par Lazar : option (a), $GO ($REG) |/' registres/decisions.md" ":"
jouer A07-n019-suite-ajoutee 1 "N-019 : colonne d'état" "sed -i -E '${N19}| tranché (a) par Lazar : $GO ($REG) ; révoqué |/' registres/decisions.md" ":"
jouer A08-n019-en-attente 1 "N-019 : colonne d'état" "sed -i -E '${N19}| en attente du GO de Lazar |/' registres/decisions.md" ":"
jouer A09-registre-absent 1 "R-990 absent" "sed -i '/^| $REG |/d' registres/decisions.md" ":"
jouer A10-texte-autre-go 1 "GO-2026-10-12-98 absent" ":" "sed -i 's/^- Décision de Lazar sur N-019 : \`$GO\`/- Décision de Lazar sur N-019 : \`GO-2026-10-12-98\`/' $P"
jouer A11-index-autre-empreinte 1 "index des invites" ":" "sed -i 's/$INDEX_SHA/$(printf '0%.0s' {1..64})/' $P"
jouer A12-dates-anciennes 1 "du commit S" ":" "sed -i 's/$DATE_S/$VIEILLE/g' $P"
jouer A13-dates-differentes 1 "AssertionError: dates" ":" "sed -i '0,/version scellée le $DATE_S/s//version scellée le $VIEILLE/' $P"
jouer A14-tests-differents 1 "AssertionError: tests" ":" "sed -i 's/; au commit cité, $NT tests),/; au commit cité, $((NT + 1)) tests),/' $P"
jouer A15-rapport-autre-empreinte 1 "ligne de la relecture R2" ":" "sed -i 's/(\`$UN_RAPPORT\`)/(\`$(printf '1%.0s' {1..64})\`)/' $P"
jouer A16-journal-repetition-altere 1 "répétition jouet" "echo x >> $LOGJ && resceller $LOGJ" ":"
copie_ctl "$R/controles-A17.sh" "s/^REPETITION_JOUET=[0-9a-f]\{64\}/REPETITION_JOUET=$LOG_AUTRE/"
jouer A17-journal-autre-commit 1 "répétition jouet" "sed -i 's/^commit du code répété : .*/commit du code répété : $AUTRE_CODE/' $LOGJ && resceller $LOGJ" ":" "" "$R/controles-A17.sh"
copie_ctl "$R/controles-A18.sh" "s/^CODE_RELU=[0-9a-f]\{40\}/CODE_RELU=$AUTRE_CODE/"
jouer A18-code-relu-autre 1 "arbre gelé de S ≠ code relu" ":" ":" "" "$R/controles-A18.sh"
# garde des scripts répétés (vérification courte, VH-02, restes) : copie versée modifiée ; lignes absentes, en double,
# mal formées (journal re-épinglé à sa nouvelle empreinte, calculée sur le journal de C1 : seule la garde visée refuse ; UH-03)
jouer A31-copie-versee-du-generateur-modifiee 1 "script répété ≠ copie versée à S : remplir_pilote_v1.py" "echo '# essai' >> $V/remplir_pilote_v1.py && resceller $V/remplir_pilote_v1.py" ":"
copie_ctl "$R/controles-A32.sh" "s/^REPETITION_JOUET=[0-9a-f]\{64\}/REPETITION_JOUET=$(git show "$C1:$LOGJ" | sed '/^script répété : /d' | sha256sum | cut -d' ' -f1)/"
jouer A32-journal-sans-scripts-repetes 1 "les cinq attendus exactement" "sed -i '/^script répété : /d' $LOGJ && resceller $LOGJ" ":" "" "$R/controles-A32.sh"
copie_ctl "$R/controles-A33.sh" "s/^REPETITION_JOUET=[0-9a-f]\{64\}/REPETITION_JOUET=$(git show "$C1:$LOGJ" | sed '/^script répété : remplir_pilote_v1.py /p' | sha256sum | cut -d' ' -f1)/"
jouer A33-script-repete-en-double 1 "script répété en double : remplir_pilote_v1.py" "sed -i '/^script répété : remplir_pilote_v1.py /p' $LOGJ && resceller $LOGJ" ":" "" "$R/controles-A33.sh"
copie_ctl "$R/controles-A34.sh" "s/^REPETITION_JOUET=[0-9a-f]\{64\}/REPETITION_JOUET=$(git show "$C1:$LOGJ" | sed 's/^\(script répété : remplir_pilote_v1.py \)[0-9a-f]*$/\1abc/' | sha256sum | cut -d' ' -f1)/"
jouer A34-script-repete-mal-forme 1 "ligne « script répété » mal formée" "sed -i 's/^\(script répété : remplir_pilote_v1.py \)[0-9a-f]*$/\1abc/' $LOGJ && resceller $LOGJ" ":" "" "$R/controles-A34.sh"
jouer A19-code-modifie-apres-cite 1 "arbre gelé" "echo '# essai' >> src/controle_ia/environnements/lancer_pilote_a.py" ":"
jouer A20-config-duree-autre 1 "14940" ":" "sed -i 's/\"duree_max_s\": 15000/\"duree_max_s\": 14940/' $CFG"
jouer A20b-config-autre-cle 1 "configuration ≠ brouillon" ":" "sed -i 's/\"lot\": 8,/\"lot\": 4,/' $CFG"
jouer A21-lecture-math-alteree-rescellee 1 "lecture gelée rejouée à 192 épisodes" "sed -i -e 's/\"conforme\": false/\"conforme\": true/' -e 's/\"conforme_avec_marge\": false/\"conforme_avec_marge\": true/' diag/20261011-225701-t05-revalidation-reel/lecture-math.json && resceller diag/20261011-225701-t05-revalidation-reel/lecture-math.json" ":"
jouer A22-taches-alterees 1 "tâches ≠ 60 premières" "python3 -c \"
import json; from pathlib import Path
p = Path('$TACHES'); d = json.loads(p.read_text(encoding='utf-8')); d['taches'] = d['taches'][1:] + d['taches'][:1]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + chr(10), encoding='utf-8')\" && resceller $TACHES" ":"
jouer A23-proposition-alteree 1 "proposition-N-019-v2.md non cité" "echo ' ' >> docs/decisions/proposition-N-019-v2.md && resceller docs/decisions/proposition-N-019-v2.md" ":"
jouer A24-rapport-non-epingle 1 "rapports présents" "echo x > $CL/T0.5-pilote-v1-relecture-b8-supplement-v1.md && resceller $CL/T0.5-pilote-v1-relecture-b8-supplement-v1.md" ":"
jouer A25-rapport-altere-rescelle 1 "rapport $NOM_RAPPORT" "echo x >> $CL/$NOM_RAPPORT && resceller $CL/$NOM_RAPPORT" ":"
jouer A26-suite-autre-compte 1 "suite complète" ":" ":" "export FAUX_SUITE=$((NT - 1))"
unset FAUX_SUITE
jouer A27-branche-presente 1 "branche calcul/t05-pilote-reel-v1" ":" ":" "git push -q $R/distant.git HEAD:refs/heads/calcul/t05-pilote-reel-v1"
git -C "$R/distant.git" branch -D calcul/t05-pilote-reel-v1 >/dev/null
jouer A28-lancement-autre-branche 1 "PREREG et BRANCHE\|PREREG ou BRANCHE" ":" "sed -i 's/\`BRANCHE=calcul\/t05-pilote-reel-v1\`/\`BRANCHE=calcul\/t05-pilote-reel-v3\`/' $P"
jouer A29-corps-modifie 1 "≠ candidat relu normalisé" ":" "sed -i '0,/sous 48 tâches complètes pour ce juge/s//sous 47 tâches complètes pour ce juge/' $P"
# relance (plan, étape 5) : -v1 sans episodes.json, -v2 absente (sain) ; artefacts : -v1 avec episodes.json (arbre de taille
# réelle : la garde lit un fichier, jamais un tube vers grep -q ; CH-03), -v2 présente, -v1 absente
v1_avec_episodes() {   # branche -v1 = S plus un commit qui ajoute diag/<run>/episodes.json, poussée sur le dépôt nu
    local s; s=$(git rev-parse HEAD)
    git checkout -q -b "v1-episodes-$1" && mkdir -p diag/20261012-120000-t05-pilote-reel \
        && echo '{"essai": true}' > diag/20261012-120000-t05-pilote-reel/episodes.json && git add -A diag \
        && git commit -qm "essai : episodes.json sur -v1" && git push -q "$R/distant.git" HEAD:refs/heads/calcul/t05-pilote-reel-v1
    git checkout -q "art-$1"
}
nettoyer_branches() { for b in calcul/t05-pilote-reel-v1 calcul/t05-pilote-reel-v2; do git -C "$R/distant.git" branch -D "$b" >/dev/null 2>&1; done; }
MODE_CTL=relance
jouer R1-relance-saine 0 "" ":" ":" "git push -q $R/distant.git HEAD:refs/heads/calcul/t05-pilote-reel-v1"
nettoyer_branches
jouer R2-relance-v1-avec-episodes 1 "-v1 porte un episodes.json" ":" ":" "v1_avec_episodes R2-relance-v1-avec-episodes"
nettoyer_branches
jouer R3-relance-v2-presente 1 "branche de relance" ":" ":" "git push -q $R/distant.git HEAD:refs/heads/calcul/t05-pilote-reel-v1 && git push -q $R/distant.git HEAD:refs/heads/calcul/t05-pilote-reel-v2"
nettoyer_branches
jouer R4-relance-v1-absente 1 "-v1 absente" ":" ":" ":"
nettoyer_branches
MODE_CTL=
copie_ctl "$R/controles-A30.sh" "s/^CANDIDAT_RELU=[0-9a-f]\{64\}/CANDIDAT_RELU=$(printf '2%.0s' {1..64})/"
jouer A30-epingle-candidat-fausse 1 "candidat relu absent" ":" ":" "" "$R/controles-A30.sh"
# Z1 : épingles du code relu absentes (code 2, aucun contrôle joué)
copie_ctl "$R/controles-Z1.sh" "s/^CODE_RELU=[0-9a-f]\{40\}/CODE_RELU=A_EPINGLER/"
git checkout -q art-A00-sain
bash "$R/controles-Z1.sh" "$(git rev-parse HEAD)" "$R/clone-Z1" > "$R/sortie-Z1.txt" 2>&1; c=$?; rm -rf "$R/clone-Z1"
[ "$c" = 2 ] && grep -q "non épinglés" "$R/sortie-Z1.txt" && echo "Z1-code-relu-non-epingle : code $c ; CONFORME" || echo "Z1-code-relu-non-epingle : code $c ; NON CONFORME (code 2 et message attendus)"
cd "$R" && rm -rf "$R/source" "$R/distant.git"
echo "FIN DU BANC DES CONTRÔLES DU PILOTE"
