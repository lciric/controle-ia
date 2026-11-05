#!/usr/bin/env bash
# Banc des contrôles avant dépense des notations refaites du pilote de T0.5 (R5), décliné du banc des contrôles du
# pilote : un cas sain et des artefacts, chacun joué contre le script entier sur un dépôt jetable cloné du commit des
# préalables C et un dépôt nu local. La copie jouée est la copie versée à C (épingles réelles), dont changent seulement :
# l'adresse du dépôt, la suite complète des tests (bouchon qui écrit « N passed », N lu dans le texte, ou FAUX_SUITE) et
# le contrôle des vrais tokeniseurs (bouchon) : ces deux-là tournent en vrai dans la répétition finale à blanc. Registres
# réels (la décision de Lazar sur N-021 y est consignée). Texte et configuration sains : le candidat et la configuration
# relus, à l'identique. Chaque artefact touche d'abord la base (registres, fichiers cités ; un commit), puis le texte ou
# la configuration (commit S qui ajoute les quatre fichiers), puis éventuellement le dépôt distant ; verdict : code
# attendu et ligne KO attendue présente (code 2 : motif sur la dernière ligne) ; nombre de KO attendu quand la cause est
# seule. Toute sortie précoce d'un cas (montage, commit, poussée) compte comme non conforme. Brouillon 3 (contre-lecture
# R2 de la chaîne) : épingles mal formées (code 2), épingles du candidat et de la configuration, sous-gardes du module
# commun sur des journaux altérés, relance (résumé, juge écrit, arrêt illisible, ligne de fin dans les traces), bornes
# du bloc 9 (délai du run, plafond de l'amorce, crédit, surveillance), sceau du préenregistrement ajouté avant S, sceaux.
# Usage : essais_controles_notations_v1.sh DEPOT_SOURCE C RACINE_NEUVE
set -uo pipefail
SRC=$(realpath "${1:?dépôt source}"); C=${2:?commit des préalables}; R=$(realpath -m "${3:?racine neuve}")
SOI=$(realpath "$0")
V=docs/procedures/notations-T0.5-v1
P=prereg/T0.5-pilote-notations-v1.md; CFG=prereg/T0.5-pilote-notations-config-v1.json
PILOTE=20261012-105125-t05-pilote-reel
[ -e "$R" ] && { echo "$R existe déjà (R12)"; exit 2; }
mkdir -p "$R" && cd "$R" || exit 2
git clone -q --no-local "$SRC" source && cd source && git checkout -q "$C" && git checkout -q -B main || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
C1=$(git rev-parse HEAD); echo "C = $C1"
# scripts éprouvés : les copies versées à C (la copie jouée n'en change que l'adresse du dépôt et deux bouchons), et ce banc
for s in controles_avant_depense_notations_v1.sh verifications_notations_v1.py; do echo "script éprouvé : $s $(sha256sum "$V/$s" | cut -d' ' -f1)"; done
echo "script éprouvé : $(basename "$SOI") $(sha256sum "$SOI" | cut -d' ' -f1)"
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
precoce() { echo "$1 : $2 : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
jouer() {   # $1 nom, $2 code attendu, $3 motif KO attendu (vide : cas sain), $4 base, $5 texte, $6 après, $7 copie des contrôles,
            # $8 nombre de KO attendu (vide : non compté)
    local nom=$1 attendu=$2 motif=$3 base=$4 texte=$5 apres=${6:-} ctl=${7:-$R/controles-essai.sh} nko=${8:-}
    git checkout -q -B "art-$nom" "$C1" || { precoce "$nom" "montage impossible"; return; }
    eval "$base"
    if [ -n "$(git status --porcelain)" ]; then git add -A . && git commit -qm "essai : base $nom" || { precoce "$nom" "commit de base impossible"; return; }; fi
    cp "$RELU" "$P" && cp "$CFG_RELUE" "$CFG" || { precoce "$nom" "copie impossible"; return; }
    eval "$texte"
    resceller "$P" "$CFG"
    git add "$P" "$P.sha256" "$CFG" "$CFG.sha256" && git commit -qm "essai : S $nom" || { precoce "$nom" "commit S impossible"; return; }
    local s; s=$(git rev-parse HEAD)
    git push -q "$R/distant.git" "art-$nom" || { precoce "$nom" "poussée impossible"; return; }
    eval "$apres"
    bash "$ctl" "$s" "$R/clone-$nom" ${MODE_CTL:-} > "$R/sortie-$nom.txt" 2>&1; local c=$?
    rm -rf "$R/clone-$nom" "$R/clone-$nom.travail"
    local verdict="CONFORME"
    [ "$c" = "$attendu" ] || verdict="NON CONFORME (code $c, attendu $attendu)"
    if [ "$attendu" = 2 ]; then
        tail -1 "$R/sortie-$nom.txt" | grep -qF -- "$motif" || verdict="NON CONFORME (motif « $motif » absent de la dernière ligne)"
        [ "$(grep -c '^OK\|^KO' "$R/sortie-$nom.txt")" = 0 ] || verdict="NON CONFORME (lignes OK ou KO avant l'arrêt en code 2)"
    elif [ -n "$motif" ] && ! grep -qF -- "KO  $motif" "$R/sortie-$nom.txt" && ! grep -q "^KO .*$motif" "$R/sortie-$nom.txt"; then verdict="NON CONFORME (KO « $motif » absent)"; fi
    if [ -n "$nko" ] && [ "$(grep -c '^KO' "$R/sortie-$nom.txt")" != "$nko" ]; then verdict="NON CONFORME ($(grep -c '^KO' "$R/sortie-$nom.txt") KO, $nko attendu(s))"; fi
    if [ -z "$motif" ] && [ "$attendu" = 0 ] && ! tail -1 "$R/sortie-$nom.txt" | grep -qx "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES"; then
        verdict="NON CONFORME (dernière ligne)"; fi
    [ "$verdict" = CONFORME ] || NON_CONFORMES=$((NON_CONFORMES + 1))
    echo "$nom : code $c ; $(grep -c '^OK' "$R/sortie-$nom.txt") OK, $(grep -c '^KO' "$R/sortie-$nom.txt") KO ; $verdict"
    grep '^KO' "$R/sortie-$nom.txt" | sed 's/^/    /' | cut -c1-220
    [ "$attendu" = 2 ] && tail -1 "$R/sortie-$nom.txt" | cut -c1-200 | sed 's/^/    | /'
    return 0
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
jouer A01-go-absent 1 "absent, en double ou mal formé" "sed -i '/^| $GO |/d' registres/go.md" ":" "" "" 1
jouer A02-go-autre-type 1 ": calcul, Lazar" "sed -i '/^| $GO |/s/| revendication |/| calcul |/' registres/go.md" ":" "" "" 1
jouer A03-go-option-b 1 ": revendication, Lazar" "sed -i '/^| $GO |/s/N-021, option (a)/N-021, option (b)/' registres/go.md" ":" "" "" 1
jouer A04-go-revoque 1 "$GO révoqué" "echo '| GO-2026-10-12-98 | 2026-10-12 | révocation | révoque $GO (essai) | — | — | Lazar | essai |' >> registres/go.md" ":" "" "" 1
jouer A05-go-calcul-revoque 1 "GO-2026-10-04-08 révoqué" "echo '| GO-2026-10-12-97 | 2026-10-12 | révocation | révoque GO-2026-10-04-08 (essai) | — | — | Lazar | essai |' >> registres/go.md" ":"
jouer A05b-go-revoque-ligne-mal-formee 1 "$GO révoqué" "echo '| GO-2026-10-12-98 | 2026-10-12 | révocation de $GO (essai) |' >> registres/go.md" ":"
jouer A05c-ligne-go-qui-mentionne-une-revocation 0 "" "echo '| GO-2026-10-12-97 | 2026-10-12 | revendication | essai : aucune révocation de $GO | — | — | Lazar | essai |' >> registres/go.md" ":"
jouer A06-n021-forme-inexacte 1 "N-021 : colonne d'état" "sed -i -E '${N21}| tranché le 2026-10-12 par Lazar : option (a), $GO (R-160) |/' registres/decisions.md" ":" "" "" 1
jouer A07-n021-suite-ajoutee 1 "N-021 : colonne d'état" "sed -i -E '${N21}| tranché (a) par Lazar : $GO (R-160) ; révoqué |/' registres/decisions.md" ":" "" "" 1
jouer A08-n021-en-attente 1 "N-021 : colonne d'état" "sed -i -E '${N21}| en attente du GO de Lazar |/' registres/decisions.md" ":" "" "" 1
jouer A09-registre-absent 1 "R-160 absent" "sed -i '/^| R-160 |/d' registres/decisions.md" ":" "" "" 1
jouer A10-texte-autre-go 1 "GO-2026-10-12-98 absent" ":" "sed -i 's/^- Décision de Lazar sur N-021 : \`$GO\`/- Décision de Lazar sur N-021 : \`GO-2026-10-12-98\`/' $P"
jouer A10b-texte-sans-decision 1 "ligne « Décision de Lazar sur N-021 »" ":" "sed -i '/^- Décision de Lazar sur N-021 :/d' $P"
# texte, configuration, pièces
jouer A11-texte-autre-que-le-candidat 1 "préenregistrement de S ≠ candidat relu" ":" "echo >> $P" "" "" 1
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
jouer A22b-intitule-en-double 1 "intitulés absents ou cités plusieurs fois : « Tâches du pilote »" ":" "sed -i 's/^- Tâches du pilote : \(.*\)$/&\n- Tâches du pilote : \1/' $P"
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
# épingles du candidat et de la configuration (une autre empreinte : texte et configuration de S refusés)
copie_ctl "$R/controles-A30b.sh" "s/^CANDIDAT_RELU=[0-9a-f]\{64\}/CANDIDAT_RELU=$(printf autre | sha256sum | cut -d' ' -f1)/"
jouer A30b-candidat-relu-autre 1 "préenregistrement de S ≠ candidat relu" ":" ":" "" "$R/controles-A30b.sh"
copie_ctl "$R/controles-A30c.sh" "s/^CONFIG_RELUE=[0-9a-f]\{64\}/CONFIG_RELUE=$(printf autre | sha256sum | cut -d' ' -f1)/"
jouer A30c-configuration-relue-autre 1 "configuration de S ≠ configuration relue" ":" ":" "" "$R/controles-A30c.sh" 2
# épingles mal formées ou absentes : code 2, rien n'est contrôlé
copie_ctl "$R/controles-Z1a.sh" "s/^CANDIDAT_RELU=[0-9a-f]\{64\}/CANDIDAT_RELU=A_EPINGLER/"
jouer Z1a-candidat-non-epingle 2 "candidat relu non épinglé" ":" ":" "" "$R/controles-Z1a.sh" 0
copie_ctl "$R/controles-Z1b.sh" "s|^CANDIDAT_RELU_CHEMIN=brouillons/|CANDIDAT_RELU_CHEMIN=prereg/|"
jouer Z1b-candidat-hors-des-brouillons 2 "candidat relu non épinglé" ":" ":" "" "$R/controles-Z1b.sh" 0
copie_ctl "$R/controles-Z1c.sh" "s/^CONFIG_RELUE=[0-9a-f]\{64\}/CONFIG_RELUE=A_EPINGLER/"
jouer Z1c-configuration-non-epinglee 2 "configuration relue non épinglée" ":" ":" "" "$R/controles-Z1c.sh" 0
copie_ctl "$R/controles-Z1d.sh" "s/^RAPPORTS_ATTENDUS=\"/RAPPORTS_ATTENDUS=\"T0.5-notations-v1-mal-forme.txt=00 /"
jouer Z1d-rapports-mal-formes 2 "rapports attendus mal formés" ":" ":" "" "$R/controles-Z1d.sh" 0
copie_ctl "$R/controles-Z1e.sh" "s/^RAPPORTS_ATTENDUS=\"\([^ \"]*\)[^\"]*\"/RAPPORTS_ATTENDUS=\"\1\"/"
jouer Z1e-un-seul-rapport 2 "au moins le rapport de la contre-lecture" ":" ":" "" "$R/controles-Z1e.sh" 0
copie_ctl "$R/controles-Z1f.sh" "s/^CODE_RELU=[0-9a-f]\{40\}/CODE_RELU=A_EPINGLER/"
jouer Z1f-code-non-epingle 2 "code relu ou répétition jouet non épinglés" ":" ":" "" "$R/controles-Z1f.sh" 0
copie_ctl "$R/controles-Z1g.sh" "s/^REPETITION_JOUET=[0-9a-f]\{64\}/REPETITION_JOUET=A_EPINGLER/"
jouer Z1g-repetition-non-epinglee 2 "code relu ou répétition jouet non épinglés" ":" ":" "" "$R/controles-Z1g.sh" 0
# arguments et dossiers (code 2, rien de contrôlé ; le dossier de travail existant n'est jamais supprimé)
direct() {   # $1 nom, $2 motif de la dernière ligne, puis les arguments des contrôles
    local nom=$1 motif=$2 c v="CONFORME"; shift 2
    bash "$R/controles-essai.sh" "$@" > "$R/sortie-$nom.txt" 2>&1; c=$?
    [ "$c" = 2 ] || v="NON CONFORME (code $c, attendu 2)"
    tail -1 "$R/sortie-$nom.txt" | grep -qF -- "$motif" || v="NON CONFORME (motif « $motif » absent)"
    [ "$(grep -c '^OK\|^KO' "$R/sortie-$nom.txt")" = 0 ] || v="NON CONFORME (lignes OK ou KO)"
    [ "$v" = CONFORME ] || NON_CONFORMES=$((NON_CONFORMES + 1))
    echo "$nom : code $c ; $v"; tail -1 "$R/sortie-$nom.txt" | cut -c1-160 | sed 's/^/    | /'
}
S_SAIN=$(git rev-parse art-A00-sain)
mkdir -p "$R/existant" "$R/travail-existe.travail"; echo garde > "$R/travail-existe.travail/temoin"
direct Z2a-dossier-existant "existe déjà" "$S_SAIN" "$R/existant"
direct Z2b-dossier-de-travail-existant "existe déjà" "$S_SAIN" "$R/travail-existe"
[ -f "$R/travail-existe.travail/temoin" ] && echo "    dossier de travail existant gardé : CONFORME" || { echo "    dossier de travail existant supprimé : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
direct Z2c-troisieme-argument-autre "troisième argument" "$S_SAIN" "$R/clone-Z2c" autre
direct Z2d-dossier-absent "dossier neuf absent" "$S_SAIN"
direct Z2e-s-invalide "S invalide" "abc" "$R/clone-Z2e"
echo garde > "$R/suite-existe.suite.txt"
direct Z2f-trace-de-la-suite-existante "suite.txt existe déjà (R12)" "$S_SAIN" "$R/suite-existe"
# candidat et configuration relus versés sans leur sceau
jouer A50-candidat-relu-sans-sceau 1 "candidat relu absent, non scellé ou d'empreinte différente" "git rm -q $RELU.sha256" ":"
jouer A51-configuration-relue-sans-sceau 1 "configuration relue absente, non scellée ou d'empreinte différente" "git rm -q $CFG_RELUE.sha256" ":"
# valeur de borne non citée par le texte
jouer A44b-borne-non-citee 1 "valeur non citée par le texte : 26 400 s" ":" "sed -i 's/26 400 s/26 401 s/g' $P"
# dépendances que l'instance installe, différentes de celles du pilote
jouer A53-dependances-autres 1 "dépendances différentes de celles du pilote" "echo 'paquet-essai==1.0' >> requirements-gpu.txt" ":"
# garde de calcul : GO de calcul échu dans le registre de S
jouer A52-go-de-calcul-echu 1 "garde de calcul" "sed -i -E '/^\\| GO-2026-10-04-08 \\|/s/\\| 2026-11-[0-9]{2} \\|/| 2026-10-11 |/' registres/go.md" ":"
# sceau du préenregistrement ajouté avant S (S ne l'ajoute pas) ; sceau des tâches altéré
jouer A39-sceau-ajoute-avant-s 1 "S n'est pas le commit qui ajoute" "cp $RELU $P && resceller $P" ":"
jouer A40-sceau-des-taches-altere 1 "sceaux" "echo '0000  autre' > donnees/t05-pilote-v1/taches-pilote-60-v1.json.sha256" ":"
# bornes du bloc 9 : délai du run, plafond de l'amorce (scripts de l'instance), crédit et surveillance (copies versées)
jouer A41-delai-du-run-change 1 "délai externe du run" "sed -i 's/--kill-after=5m 400m)/--kill-after=5m 410m)/' scripts/notations_t05_instance.sh" ":"
jouer A42-plafond-de-l-amorce-change 1 "plafond de l'amorce" "sed -i 's/--kill-after=5m 430m /--kill-after=5m 420m /' scripts/amorce_instance_t05_notations.sh" ":"
jouer A43-credit-change 1 "heures du crédit exigé" "sed -i 's/^HEURES_CREDIT=7.5 /HEURES_CREDIT=6 /' $V/lancer_notations_v1.sh && resceller $V/lancer_notations_v1.sh" ":"
jouer A44-plafond-de-la-surveillance-change 1 "plafond de la surveillance" "sed -i 's/^PLAFOND_S=26400 /PLAFOND_S=20000 /' $V/surveiller_notations_v1.sh && resceller $V/surveiller_notations_v1.sh" ":"
jouer A44c-plafond-ecrit-par-le-lanceur-change 1 "plafond de la surveillance écrit par le lanceur" "sed -i 's/^PLAFOND_SURVEILLANCE_S=26400 /PLAFOND_SURVEILLANCE_S=20000 /' $V/lancer_notations_v1.sh && resceller $V/lancer_notations_v1.sh" ":"
# branche de résultats ; relance
jouer A32-branche-presente 1 "branche calcul/t05-notations-reel-v1 : code 0" ":" ":" "git push -q $R/distant.git art-A32-branche-presente:refs/heads/calcul/t05-notations-reel-v1"
git -C "$R/distant.git" branch -D calcul/t05-notations-reel-v1 > /dev/null
export MODE_CTL=relance
jouer A33-relance-sans-premier 1 "-v1 absente ou illisible" ":" ":"
jouer A34-relance-saine 0 "" ":" ":" "git push -q $R/distant.git art-A34-relance-saine:refs/heads/calcul/t05-notations-reel-v1"
git -C "$R/distant.git" branch -D calcul/t05-notations-reel-v1 > /dev/null
jouer A35-relance-apres-notations 1 "-v1 porte un fichier de notations" ":" ":" "git checkout -q -b v1-a35 && mkdir -p diag/20261013-000000-t05-notations-reel && echo '{}' > diag/20261013-000000-t05-notations-reel/notations-8B-decisives.json && git add -A diag && git commit -qm 'essai : notations sur v1' && git push -q $R/distant.git v1-a35:refs/heads/calcul/t05-notations-reel-v1"
git -C "$R/distant.git" branch -D calcul/t05-notations-reel-v1 > /dev/null
jouer A37-relance-apres-un-juge-echu 1 "-v1 : arrêt consigné avec un juge fini" ":" ":" "git checkout -q -b v1-a37 && mkdir -p diag/20261013-000000-t05-notations-reel && printf '%s' '{\"resultat\": {\"etape\": \"notations decisives par 3B\", \"partiel\": {\"juges\": {\"8B\": {\"statut\": \"échu\"}, \"3B\": {\"statut\": \"en cours\"}}}}}' > diag/20261013-000000-t05-notations-reel/arret.json && git add -A diag && git commit -qm 'essai : 8B échu sur v1' && git push -q $R/distant.git v1-a37:refs/heads/calcul/t05-notations-reel-v1"
git -C "$R/distant.git" branch -D calcul/t05-notations-reel-v1 > /dev/null
jouer A38-relance-apres-un-arret-sans-juge-fini 0 "" ":" ":" "git checkout -q -b v1-a38 && mkdir -p diag/20261013-000000-t05-notations-reel && printf '%s' '{\"resultat\": {\"etape\": \"notations decisives par 8B\", \"partiel\": {\"juges\": {\"8B\": {\"statut\": \"en cours\"}}}}}' > diag/20261013-000000-t05-notations-reel/arret.json && git add -A diag && git commit -qm 'essai : arrêt pendant le 8B sur v1' && git push -q $R/distant.git v1-a38:refs/heads/calcul/t05-notations-reel-v1"
git -C "$R/distant.git" branch -D calcul/t05-notations-reel-v1 > /dev/null
v1() {   # $1 nom de la branche locale, $2 commande qui prépare l'ajout ; pousse la branche -v1 du dépôt distant
    git checkout -q -b "$1" && eval "$2" && git add -A . && git commit -qm "essai : $1" && git push -q "$R/distant.git" "$1:refs/heads/calcul/t05-notations-reel-v1"
}
RV1=diag/20261013-000000-t05-notations-reel
jouer A45-relance-apres-un-resume 1 "-v1 porte un résumé" ":" ":" "v1 v1-a45 \"mkdir -p $RV1 && echo '{}' > $RV1/resume.json\""
git -C "$R/distant.git" branch -D calcul/t05-notations-reel-v1 > /dev/null
jouer A46-relance-apres-un-juge-ecrit 1 "-v1 : arrêt consigné avec un juge fini" ":" ":" "v1 v1-a46 \"mkdir -p $RV1 && printf '%s' '{\\\"resultat\\\": {\\\"partiel\\\": {\\\"juges\\\": {\\\"8B\\\": {\\\"statut\\\": \\\"écrit\\\"}}}}}' > $RV1/arret.json\""
git -C "$R/distant.git" branch -D calcul/t05-notations-reel-v1 > /dev/null
jouer A47-relance-apres-un-arret-illisible 1 "arrêt illisible sur -v1" ":" ":" "v1 v1-a47 \"mkdir -p $RV1 && echo '{' > $RV1/arret.json\""
git -C "$R/distant.git" branch -D calcul/t05-notations-reel-v1 > /dev/null
jouer A48-relance-apres-une-fin-dans-les-traces 1 "-v1 : traces avec une ligne de fin de juge" ":" ":" "v1 v1-a48 \"mkdir -p traces/t05-notations-essai && printf 'PROGRES 2026-10-13T09:00:00Z juge=8B fin=échu lots_faits=3/23 duree_s=12000.0\\\\n' > traces/t05-notations-essai/journal.txt\""
git -C "$R/distant.git" branch -D calcul/t05-notations-reel-v1 > /dev/null
jouer A48b-relance-apres-un-dernier-lot 1 "-v1 : traces avec une ligne de fin de juge ou de dernier lot" ":" ":" "v1 v1-a48b \"mkdir -p traces/t05-notations-essai && printf 'PROGRES 2026-10-13T09:00:00Z juge=8B lot=23/23 duree_s=344.0\\\\n' > traces/t05-notations-essai/journal.txt\""
git -C "$R/distant.git" branch -D calcul/t05-notations-reel-v1 > /dev/null
jouer A48d-relance-apres-une-fin-dans-run-err 1 "-v1 : traces avec une ligne de fin de juge ou de dernier lot" ":" ":" "v1 v1-a48d \"mkdir -p traces/t05-notations-essai && printf 'PROGRES 2026-10-13T09:00:00Z juge=8B fin=échu lots_faits=3/23 duree_s=12000.0\\\\n' > traces/t05-notations-essai/run.err\""
git -C "$R/distant.git" branch -D calcul/t05-notations-reel-v1 > /dev/null
jouer A48c-relance-apres-un-lot-intermediaire 0 "" ":" ":" "v1 v1-a48c \"mkdir -p traces/t05-notations-essai && printf 'PROGRES 2026-10-13T09:00:00Z juge=8B lot=2/23 duree_s=344.0\\\\n' > traces/t05-notations-essai/journal.txt\""
git -C "$R/distant.git" branch -D calcul/t05-notations-reel-v1 > /dev/null
jouer A36-relance-branche-v2-presente 1 "branche de relance : code 0" ":" ":" "git push -q $R/distant.git art-A36-relance-branche-v2-presente:refs/heads/calcul/t05-notations-reel-v1 && git push -q $R/distant.git art-A36-relance-branche-v2-presente:refs/heads/calcul/t05-notations-reel-v2"
unset MODE_CTL
# sous-gardes du module commun sur des journaux de la répétition altérés (le module est le texte lu par les contrôles et le
# scellement ; A28 et A31 le jouent dans le script entier) : code 1 et motif attendu sur la dernière ligne
VERIF_V=$V/verifications_notations_v1.py
NOM_C=$(basename "$RELU"); SHA_C=$(sha256sum "$RELU" | cut -d' ' -f1); CODE_R=$(epingle CODE_RELU)
module() {   # $1 nom, $2 motif, $3 commande sed (ou awk) qui altère le journal
    local j="$R/journal-$1.txt" c
    git show "$C1:$LOGJ" > "$R/journal-sain.txt"
    eval "$3" < "$R/journal-sain.txt" > "$j"
    python3 -I "$VERIF_V" repetition "$CODE_R" "$j" "$NOM_C" "$SHA_C" > "$R/module-$1.txt" 2>&1; c=$?
    if [ "$c" = 1 ] && tail -1 "$R/module-$1.txt" | grep -qF -- "$2"; then echo "$1 : code 1 ; CONFORME"
    else echo "$1 : code $c ; NON CONFORME ($(tail -1 "$R/module-$1.txt" | cut -c1-160))"; NON_CONFORMES=$((NON_CONFORMES + 1)); fi
}
python3 -I "$VERIF_V" repetition "$CODE_R" <(git show "$C1:$LOGJ") "$NOM_C" "$SHA_C" > "$R/module-sain.txt" 2>&1 \
    && echo "M00-journal-sain : code 0 ; CONFORME" || { echo "M00-journal-sain : NON CONFORME ($(tail -1 "$R/module-sain.txt"))"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
module M01-candidat-absent "ligne absente ou en double : candidat répété" "sed '/^candidat répété : /d'"
module M02-candidat-autre "ligne absente ou en double : candidat répété" "sed 's/^candidat répété : .*/candidat répété : autre.md 0000/'"
module M03-deux-lignes-candidat "ligne absente ou en double" "sed 's/^candidat répété : .*/&\\n&/'"
module M04-passage-manquant "passage : passage 3-premier-manque : code 1" "sed '/^passage 3-premier-manque : /d'"
module M05-passage-autre-code "passage : passage 1-sain : code 0" "sed 's/^passage 1-sain : code 0 /passage 1-sain : code 1 /'"
module M06-recuperation-conforme-absente "ligne absente ou en double : récupération (arret-synthetique-sain)" "sed '/^récupération (arret-synthetique-sain) : /d'"
module M07-ko-dans-un-cas-sain "récupération (passage-1-premier) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES : KO" "sed '/^récupération (passage-1-premier) : /a\\    KO  6 essai'"
module M08-artefact-a-deux-ko "récupération (artefact-notations-manquantes)" "sed '/^récupération (artefact-notations-manquantes) : /a\\    KO  2b essai'"
module M09-artefact-autre-ko "récupération (artefact-ajout-dans-le-pilote)" "sed '/^    KO  1c /s/KO  1c /KO  1d /'"
module M10-ko-hors-du-bloc "récupération (artefact-relance-apres-notations)" "awk '/^    KO  0 /{next} {print} /^récupération \\(artefact-ajout-dans-le-pilote\\)/{print \"    KO  0 essai\"}'"
module M11-script-mal-forme "ligne « script répété » mal formée" "sed '0,/^script répété : /s/^script répété : \\([a-z_]*\\)_v1\\.\\([a-z]*\\) /script répété : \\1.\\2 /'"
module M12-script-en-double "script répété en double" "awk '/^script répété : /&&!d{print; d=1} {print}'"
module M13-script-manquant "les trois attendus exactement" "sed '0,/^script répété : /{/^script répété : /d}'"
module M14-fin-absente "ligne absente ou en double : FIN DE LA RÉPÉTITION" "sed '/^FIN DE LA RÉPÉTITION$/d'"
# sous-gardes de « preuves » (lues par le lanceur) sur des journaux synthétiques : cas sain, puis une ligne d'échec
# (« NON CONFORME », trace d'exception, jeton affiché) ajoutée avant le verdict ; seuls le code et un motif court s'affichent
PRV=$R/preuves; mkdir -p "$PRV/sain"
ecrire_preuves() {   # $1 dossier : les cinq journaux sains, empreintes factices cohérentes
    python3 - "$1" <<'PYP'
import sys
d = sys.argv[1]
J = {"banc-lanceur-notations-v1.log": ("FIN DU BANC DU LANCEUR DES NOTATIONS ; cas non conformes : 0", ["lancer_notations_v1.sh", "verifications_notations_v1.py", "essais_lanceur_notations_v1.sh"]),
     "banc-surveillance-notations-v1.log": ("FIN DU BANC DE LA SURVEILLANCE DES NOTATIONS ; cas non conformes : 0", ["surveiller_notations_v1.sh", "essais_surveillance_notations_v1.sh"]),
     "banc-controles-notations-v1.log": ("FIN DU BANC DES CONTRÔLES DES NOTATIONS ; cas non conformes : 0", ["controles_avant_depense_notations_v1.sh", "essais_controles_notations_v1.sh"]),
     "banc-scellement-notations-v1.log": ("FIN DU BANC DU SCELLEMENT DES NOTATIONS ; cas non conformes : 0", ["sceller_notations_v1.sh", "essais_scellement_notations_v1.sh"]),
     "repetition-finale-notations-v1.log": ("RÉPÉTITION FINALE : CONFORME", ["repetition_finale_notations_v1.sh"])}
for n, (v, s) in J.items():
    open(f"{d}/{n}", "w", encoding="utf-8").write("".join(f"script éprouvé : {x} {'a' * 64}\n" for x in s) + v + "\n")
PYP
}
ecrire_preuves "$PRV/sain"
python3 -I "$VERIF_V" preuves "$PRV/sain" > "$R/preuves-sain.txt" 2>&1 && echo "P00-preuves-saines : code 0 ; CONFORME" \
    || { echo "P00-preuves-saines : code 1 ; à revoir"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
for k in 1 2 3; do
    mkdir -p "$PRV/faute-$k"; ecrire_preuves "$PRV/faute-$k"
    case $k in 1) l="cas X : code 1 ; NON CONF""ORME (essai)" ;; 2) l="Traceback (most recent call last): essai" ;; 3) l="JETON AFFI""CHÉ : sortie-essai.txt" ;; esac
    sed -i "1a $l" "$PRV/faute-$k/banc-scellement-notations-v1.log"
    python3 -I "$VERIF_V" preuves "$PRV/faute-$k" > "$R/preuves-faute-$k.txt" 2>&1; c=$?
    if [ "$c" = 1 ] && tail -1 "$R/preuves-faute-$k.txt" | grep -qF "ligne d'échec avant le verdict"; then echo "P0$k-preuves-ligne-d-echec : code 1 ; CONFORME"
    else echo "P0$k-preuves-ligne-d-echec : code $c ; à revoir"; NON_CONFORMES=$((NON_CONFORMES + 1)); fi
done
cd "$R" && rm -rf "$R/source" "$R/distant.git"
echo "FIN DU BANC DES CONTRÔLES DES NOTATIONS ; cas non conformes : $NON_CONFORMES"
[ "$NON_CONFORMES" = 0 ] || exit 1
