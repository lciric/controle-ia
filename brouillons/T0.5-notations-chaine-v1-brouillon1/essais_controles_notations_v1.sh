#!/usr/bin/env bash
# Banc des contrôles avant dépense des notations refaites du pilote de T0.5 (R5), décliné du banc des contrôles du
# pilote : un cas sain et des artefacts, chacun joué contre le script entier sur un dépôt jetable cloné du commit des
# préalables C et un dépôt nu local. La copie jouée est la copie versée à C (épingles réelles), dont changent seulement :
# l'adresse du dépôt, la suite complète des tests (bouchon qui écrit « N passed », N lu dans le texte, ou FAUX_SUITE) et
# le contrôle des vrais tokeniseurs (bouchon) : ces deux-là tournent en vrai dans la répétition finale à blanc. Registres
# réels (la décision de Lazar sur N-021 y est consignée). Texte et configuration sains : le candidat et la configuration
# relus, à l'identique. Chaque artefact touche d'abord la base (registres, fichiers cités ; un commit), puis le texte ou
# la configuration (commit S qui ajoute les quatre fichiers), puis éventuellement le dépôt distant ; verdict : code
# attendu et ligne KO attendue présente.
# Usage : essais_controles_notations_v1.sh DEPOT_SOURCE C RACINE_NEUVE
set -uo pipefail
SRC=$1; C=$2; R=$3
V=docs/procedures/notations-T0.5-v1
P=prereg/T0.5-pilote-notations-v1.md; CFG=prereg/T0.5-pilote-notations-config-v1.json
PILOTE=20261012-105125-t05-pilote-reel
[ -e "$R" ] && { echo "$R existe déjà (R12)"; exit 2; }
mkdir -p "$R" && cd "$R" || exit 2
git clone -q --no-local "$SRC" source && cd source && git checkout -q "$C" && git checkout -q -B main || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
C1=$(git rev-parse HEAD); echo "C = $C1"
grep -q "^[A-Z_]*=\"\{0,1\}A_EPINGLER" "$V/controles_avant_depense_notations_v1.sh" && { echo "épingles absentes de la copie versée des contrôles"; exit 2; }
git clone -q --bare . "$R/distant.git" || exit 2
python3 - "$V/controles_avant_depense_notations_v1.sh" "$R/controles-essai.sh" "$R/distant.git" <<'PYCOPIE' || exit 2
import re, sys
from pathlib import Path
src, dst, depot = sys.argv[1:4]
t = Path(src).read_text(encoding="utf-8")
def rep(a, b, regex=False):
    global t
    n = len(re.findall(a, t, re.M)) if regex else t.count(a)
    assert n == 1, (n, a)
    t = re.sub(a, lambda _: b, t, flags=re.M) if regex else t.replace(a, b)
rep(r"^DEPOT=.*$", f"DEPOT={depot}", regex=True)
rep('PYTHONPATH=src "$PY" -m pytest -q -p no:cacheprovider > "$W/suite.txt" 2>&1; cs=$?',
    'printf \'%s passed in 1.00s\\n\' "${FAUX_SUITE:-$a}" > "$W/suite.txt"; cs=0   # bouchon du banc')
rep('HF_HOME="$W/cache-hf" PYTHONPATH=src "$PY" - "$CFG" "$PILOTE" > "$W/bloc-format.txt" 2>&1 <<\'EOF\'',
    'cat > "$W/bloc-format.txt" <<\'EOF\'   # bouchon du banc')
Path(dst).write_text(t, encoding="utf-8")
PYCOPIE
echo "lignes changées dans la copie des contrôles : $(diff "$V/controles_avant_depense_notations_v1.sh" "$R/controles-essai.sh" | grep -c '^>')"
epingle() { sed -n "s/^$1=\"\{0,1\}\([^\"#]*\)\"\{0,1\}.*/\1/p" "$R/controles-essai.sh" | sed 's/[[:space:]]*$//'; }
RELU=$(epingle CANDIDAT_RELU_CHEMIN); CFG_RELUE=$(epingle CONFIG_RELUE_CHEMIN); RAPPORTS=$(epingle RAPPORTS_ATTENDUS)
LOGJ=$(epingle REPETITION_JOUET_CHEMIN)
UN_RAPPORT=$(for x in $RAPPORTS; do echo "${x%%=*}"; break; done)
resceller() { local f; for f in "$@"; do (cd "$(dirname "$f")" && sha256sum "$(basename "$f")" > "$(basename "$f").sha256"); done; }
jouer() {   # $1 nom, $2 code attendu, $3 motif KO attendu (vide : cas sain), $4 base, $5 texte, $6 après, $7 copie des contrôles
    local nom=$1 attendu=$2 motif=$3 base=$4 texte=$5 apres=${6:-} ctl=${7:-$R/controles-essai.sh}
    git checkout -q -B "art-$nom" "$C1" || { echo "$nom : montage impossible"; return; }
    eval "$base"
    if [ -n "$(git status --porcelain)" ]; then git add -A . && git commit -qm "essai : base $nom" || { echo "$nom : commit de base impossible"; return; }; fi
    cp "$RELU" "$P" && cp "$CFG_RELUE" "$CFG" || { echo "$nom : copie impossible"; return; }
    eval "$texte"
    resceller "$P" "$CFG"
    git add "$P" "$P.sha256" "$CFG" "$CFG.sha256" && git commit -qm "essai : S $nom" || { echo "$nom : commit S impossible"; return; }
    local s; s=$(git rev-parse HEAD)
    git push -q "$R/distant.git" "art-$nom" || { echo "$nom : poussée impossible"; return; }
    eval "$apres"
    bash "$ctl" "$s" "$R/clone-$nom" ${MODE_CTL:-} > "$R/sortie-$nom.txt" 2>&1; local c=$?
    rm -rf "$R/clone-$nom" "$R/clone-$nom.travail"
    local verdict="CONFORME"
    [ "$c" = "$attendu" ] || verdict="NON CONFORME (code $c, attendu $attendu)"
    if [ -n "$motif" ] && ! grep -qF -- "KO  $motif" "$R/sortie-$nom.txt" && ! grep -q "^KO .*$motif" "$R/sortie-$nom.txt"; then verdict="NON CONFORME (KO « $motif » absent)"; fi
    if [ -z "$motif" ] && [ "$attendu" = 0 ] && ! tail -1 "$R/sortie-$nom.txt" | grep -qx "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES"; then
        verdict="NON CONFORME (dernière ligne)"; fi
    [ "$verdict" = CONFORME ] || NON_CONFORMES=$((NON_CONFORMES + 1))
    echo "$nom : code $c ; $(grep -c '^OK' "$R/sortie-$nom.txt") OK, $(grep -c '^KO' "$R/sortie-$nom.txt") KO ; $verdict"
    grep '^KO' "$R/sortie-$nom.txt" | sed 's/^/    /' | cut -c1-220
}
copie_ctl() {   # $1 sortie, $2 expression sed sur la copie jouée (une épingle changée) : une ligne exactement
    sed -e "$2" "$R/controles-essai.sh" > "$1"
    local n; n=$(diff "$R/controles-essai.sh" "$1" | grep -c '^>')
    [ "$n" = 1 ] || { echo "COPIE NON CONFORME : $1 change $n ligne(s) au lieu d'une : ARRÊT"; exit 2; }
}
NON_CONFORMES=0
NT=$(sed -n "s/^- Tests attendus : \`\([0-9]*\)\`.*/\1/p" "$RELU")
AUTRE_CODE=$(git rev-parse "$(git rev-list --max-count=1 "$C1" -- src/controle_ia/environnements/noter_pilote_a.py)^")
N21='s/^(\| N-021 \|.*)\| tranché \(a\) par Lazar : [^|]*\|$/\1'
GO=GO-2026-10-12-02
echo "tests $NT ; commit antérieur au dernier changement du lanceur des notations : $AUTRE_CODE ; un rapport : $UN_RAPPORT"
jouer A00-sain 0 "" ":" ":"
# décision de Lazar sur N-021
jouer A01-go-absent 1 "absent, en double ou mal formé" "sed -i '/^| $GO |/d' registres/go.md" ":"
jouer A02-go-autre-type 1 ": calcul, Lazar" "sed -i '/^| $GO |/s/| revendication |/| calcul |/' registres/go.md" ":"
jouer A03-go-option-b 1 ": revendication, Lazar" "sed -i '/^| $GO |/s/N-021, option (a)/N-021, option (b)/' registres/go.md" ":"
jouer A04-go-revoque 1 "$GO révoqué" "echo '| GO-2026-10-12-98 | 2026-10-12 | révocation | révoque $GO (essai) | — | — | Lazar | essai |' >> registres/go.md" ":"
jouer A05-go-calcul-revoque 1 "GO-2026-10-04-08 révoqué" "echo '| GO-2026-10-12-97 | 2026-10-12 | révocation | révoque GO-2026-10-04-08 (essai) | — | — | Lazar | essai |' >> registres/go.md" ":"
jouer A05b-go-revoque-ligne-mal-formee 1 "$GO révoqué" "echo '| GO-2026-10-12-98 | 2026-10-12 | révocation de $GO (essai) |' >> registres/go.md" ":"
jouer A05c-ligne-go-qui-mentionne-une-revocation 0 "" "echo '| GO-2026-10-12-97 | 2026-10-12 | revendication | essai : aucune révocation de $GO | — | — | Lazar | essai |' >> registres/go.md" ":"
jouer A06-n021-forme-inexacte 1 "N-021 : colonne d'état" "sed -i -E '${N21}| tranché le 2026-10-12 par Lazar : option (a), $GO (R-160) |/' registres/decisions.md" ":"
jouer A07-n021-suite-ajoutee 1 "N-021 : colonne d'état" "sed -i -E '${N21}| tranché (a) par Lazar : $GO (R-160) ; révoqué |/' registres/decisions.md" ":"
jouer A08-n021-en-attente 1 "N-021 : colonne d'état" "sed -i -E '${N21}| en attente du GO de Lazar |/' registres/decisions.md" ":"
jouer A09-registre-absent 1 "R-160 absent" "sed -i '/^| R-160 |/d' registres/decisions.md" ":"
jouer A10-texte-autre-go 1 "GO-2026-10-12-98 absent" ":" "sed -i 's/^- Décision de Lazar sur N-021 : \`$GO\`/- Décision de Lazar sur N-021 : \`GO-2026-10-12-98\`/' $P"
jouer A10b-texte-sans-decision 1 "ligne « Décision de Lazar sur N-021 »" ":" "sed -i '/^- Décision de Lazar sur N-021 :/d' $P"
# texte, configuration, pièces
jouer A11-texte-autre-que-le-candidat 1 "préenregistrement de S ≠ candidat relu" ":" "echo >> $P"
jouer A12-configuration-autre-que-la-relue 1 "configuration de S ≠ configuration relue" ":" "sed -i 's/\"lot_juge\": 8/\"lot_juge\": 4/' $CFG"
jouer A13-commit-du-code-cite-deux-fois 1 "cité 2 fois" ":" "sed -i '0,/^- Commit du code d.analyse : /{/^- Commit du code d.analyse : /p}' $P"
jouer A14-code-modifie-apres-cite 1 "arbre gelé modifié depuis le commit du code" "echo '# essai' >> src/controle_ia/environnements/noter_pilote_a.py" ":"
jouer A15-module-de-lecture-modifie 1 "modules de lecture du pilote modifiés" "echo '# essai' >> src/controle_ia/environnements/lire_pilote.py" ":"
jouer A16-script-de-l-instance-modifie 1 "empreinte de scripts/notations_t05_instance.sh" "echo '# essai' >> scripts/notations_t05_instance.sh" ":"
jouer A17-arret-du-pilote-altere 1 "diag/$PILOTE/arret.json non cité par son empreinte" "sed -i 's/\"etape\"/\"etape\" /' diag/$PILOTE/arret.json && resceller diag/$PILOTE/arret.json" ":"
jouer A18-notations-dans-le-pilote 1 "gardes du lanceur" "cp diag/$PILOTE/appariements.json diag/$PILOTE/notations-8B-decisives.json && resceller diag/$PILOTE/notations-8B-decisives.json" ":"
jouer A19-verdict-sans-sceau 1 "docs/verdicts/verdict-T0.5-pilote-v1.md ou son sceau absent" "git rm -q docs/verdicts/verdict-T0.5-pilote-v1.md.sha256" ":"
jouer A20-premiere-lecture-retiree 1 "diag/20261012-150724-t05-pilote-analyse/lecture.json ou son sceau absent" "git rm -q diag/20261012-150724-t05-pilote-analyse/lecture.json diag/20261012-150724-t05-pilote-analyse/lecture.json.sha256" ":"
jouer A21-s-ajoute-un-autre-fichier 1 "contenu de S inattendu" ":" "echo essai >> README.md && git add README.md"
jouer A22-lecture-precoce-citation-en-double 1 "lecture précoce" ":" "sed -i 's/^- Chemin des épisodes du pilote noté : \(.*\)$/&\n- Chemin des épisodes du pilote noté : \1/' $P"
jouer A23-problemes-non-vide 1 "problemes() non vide" ":" "sed -i 's/^## Contre-lecture$/## Contre-lecture retirée/' $P"
jouer A24-ligne-lancement-autre 1 "PREREG ou BRANCHE" ":" "sed -i 's/\`BRANCHE=calcul\/t05-notations-reel-v1\`/\`BRANCHE=calcul\/t05-notations-reel-v9\`/' $P"
jouer A25-suite-autre-nombre 1 "suite complète" ":" ":" "export FAUX_SUITE=$((NT + 1))"
unset FAUX_SUITE
# rapports et répétition jouet
jouer A26-rapport-altere 1 "rapport $UN_RAPPORT absent, non scellé" "echo x >> prereg/contre-lectures/$UN_RAPPORT && resceller prereg/contre-lectures/$UN_RAPPORT" ":"
jouer A27-rapport-de-trop 1 "rapports présents" "echo x > prereg/contre-lectures/T0.5-notations-v1-relecture-autre-v1.md && resceller prereg/contre-lectures/T0.5-notations-v1-relecture-autre-v1.md" ":"
jouer A28-journal-repetition-altere 1 "répétition jouet" "echo x >> $LOGJ && resceller $LOGJ" ":"
jouer A29-copie-versee-du-pilote-jouet-modifiee 1 "script répété ≠ copie versée à S : construire_pilote_jouet_v1.py" "echo '# essai' >> $V/construire_pilote_jouet_v1.py && resceller $V/construire_pilote_jouet_v1.py" ":"
copie_ctl "$R/controles-A30.sh" "s/^CODE_RELU=[0-9a-f]\{40\}/CODE_RELU=$AUTRE_CODE/"
jouer A30-code-relu-autre 1 "arbre gelé de S ≠ code relu" ":" ":" "" "$R/controles-A30.sh"
copie_ctl "$R/controles-A31.sh" "s/^REPETITION_JOUET=[0-9a-f]\{64\}/REPETITION_JOUET=$(git show "$C1:$LOGJ" | sed "s/^commit du code répété : .*/commit du code répété : $AUTRE_CODE/" | sha256sum | cut -d' ' -f1)/"
jouer A31-journal-autre-commit 1 "répétition jouet" "sed -i 's/^commit du code répété : .*/commit du code répété : $AUTRE_CODE/' $LOGJ && resceller $LOGJ" ":" "" "$R/controles-A31.sh"
# branche de résultats ; relance
jouer A32-branche-presente 1 "branche calcul/t05-notations-reel-v1 : code 0" ":" ":" "git push -q $R/distant.git art-A32-branche-presente:refs/heads/calcul/t05-notations-reel-v1"
git -C "$R/distant.git" branch -D calcul/t05-notations-reel-v1 > /dev/null
export MODE_CTL=relance
jouer A33-relance-sans-premier 1 "-v1 absente ou illisible" ":" ":"
jouer A34-relance-saine 0 "" ":" ":" "git push -q $R/distant.git art-A34-relance-saine:refs/heads/calcul/t05-notations-reel-v1"
git -C "$R/distant.git" branch -D calcul/t05-notations-reel-v1 > /dev/null
jouer A35-relance-apres-notations 1 "-v1 porte un fichier de notations" ":" ":" "git checkout -q -b v1-a35 && mkdir -p diag/20261013-000000-t05-notations-reel && echo '{}' > diag/20261013-000000-t05-notations-reel/notations-8B-decisives.json && git add -A diag && git commit -qm 'essai : notations sur v1' && git push -q $R/distant.git v1-a35:refs/heads/calcul/t05-notations-reel-v1"
git -C "$R/distant.git" branch -D calcul/t05-notations-reel-v1 > /dev/null
jouer A36-relance-branche-v2-presente 1 "branche de relance : code 0" ":" ":" "git push -q $R/distant.git art-A36-relance-branche-v2-presente:refs/heads/calcul/t05-notations-reel-v1 && git push -q $R/distant.git art-A36-relance-branche-v2-presente:refs/heads/calcul/t05-notations-reel-v2"
unset MODE_CTL
cd "$R" && rm -rf "$R/source" "$R/distant.git"
echo "FIN DU BANC DES CONTRÔLES DES NOTATIONS ; cas non conformes : $NON_CONFORMES"
[ "$NON_CONFORMES" = 0 ] || exit 1
