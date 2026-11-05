#!/usr/bin/env bash
# Banc des contrôles avant dépense du premier test boîte blanche sur l'organisme (i-a) (P3, R-192, R-202 ; R5), v1,
# brouillon 2 (contre-lecture R2 de la chaîne traitée : CH-01, CH-02, CH-08, CH-09, CH-12, CH-14, CH-15, CH-19 ; bornes
# du brouillon 4 du texte), décliné du banc des contrôles des notations refaites du pilote de T0.5
# (docs/procedures/notations-T0.5-v2/essais_controles_notations_v1.sh) sous un nom nouveau (R12) : un cas sain et des
# artefacts, chacun joué contre le script entier sur un dépôt jetable cloné du commit des préalables C et un dépôt nu
# local. La copie jouée est la copie versée à C (épingles réelles), dont changent seulement : l'adresse du dépôt, la
# suite complète des tests (bouchon qui écrit « N passed », N lu dans le texte, ou FAUX_SUITE) et, dans la copie
# ordinaire, le bloc du vrai tokeniseur (bouchon ; une seconde copie le garde et joue les cas B, qui lisent le
# tokeniseur de l'agent sur Hugging Face). Registres réels (le GO de calcul et la décision de Lazar y sont consignés).
# Texte, configuration et consignes sains : les candidats relus, à l'identique. Chaque artefact touche d'abord la base
# (registres, fichiers cités ; un commit), puis le texte, la configuration ou les consignes (commit S qui ajoute les six
# fichiers), puis éventuellement le dépôt distant ; verdict : code attendu et ligne KO attendue présente (code 2 : motif
# sur la dernière ligne) ; nombre de KO attendu quand la cause est seule (A19 : deux KO, le sceau absent et
# verifier-arbre, CH-01). Toute sortie précoce d'un cas (montage, commit, poussée) compte comme non conforme. Sous-gardes
# du module commun (GO et décision, répétition jouet, preuves des essais) sur des registres, des textes et des journaux
# altérés ou synthétiques, appelées directement.
# Usage : essais_controles_p3_v1.sh DEPOT_SOURCE C RACINE_NEUVE
set -uo pipefail
[ $# -eq 3 ] || { echo "usage : essais_controles_p3_v1.sh DEPOT_SOURCE C RACINE_NEUVE"; exit 2; }
SRC=$(realpath "$1"); C=$2; R=$(realpath -m "$3")
SOI=$(realpath "$0")
V=docs/procedures/P3-premier-test-v1
P=prereg/P3-premier-test-i-a-v1.md; CFG=prereg/P3-premier-test-config-v1.json; CONSIGNES=prereg/P3-consignes-v1.md
GO=GO-2026-10-04-08; REG=R-192
[ -e "$R" ] && { echo "$R existe déjà (R12)"; exit 2; }
mkdir -p "$R" && cd "$R" || exit 2
git clone -q --no-local "$SRC" source && cd source && git checkout -q "$C" && git checkout -q -B main || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
C1=$(git rev-parse HEAD); echo "C = $C1"
# scripts éprouvés : les copies versées à C (la copie jouée n'en change que l'adresse du dépôt et des bouchons), et ce banc
for s in controles_avant_depense_p3_v1.sh verifications_p3_v1.py; do echo "script éprouvé : $s $(sha256sum "$V/$s" | cut -d' ' -f1)"; done
echo "script éprouvé : $(basename "$SOI") $(sha256sum "$SOI" | cut -d' ' -f1)"
grep -q "^[A-Z_]*=\"\{0,1\}A_EPINGLER" "$V/controles_avant_depense_p3_v1.sh" && { echo "épingles absentes de la copie versée des contrôles"; exit 2; }
git clone -q --bare . "$R/distant.git" || exit 2
python3 - "$V/controles_avant_depense_p3_v1.sh" "$R/controles-essai.sh" "$R/controles-essai-tok.sh" "$R/distant.git" <<'PYCOPIE' || exit 2
import re, sys
from pathlib import Path
src, dst, dst_tok, depot = sys.argv[1:5]
t = Path(src).read_text(encoding="utf-8")
def rep(t, a, b, regex=False):
    n = len(re.findall(a, t, re.M)) if regex else t.count(a)
    assert n == 1, (n, a)
    return re.sub(a, lambda _: b, t, flags=re.M) if regex else t.replace(a, b)
t = rep(t, r"^DEPOT=.*$", f"DEPOT={depot}", regex=True)
t = rep(t, 'PYTHONPATH=src "$PY" -m pytest -q -p no:cacheprovider > "$W/suite.txt" 2>&1; cs=$?',
        'printf \'%s passed in 1.00s\\n\' "${FAUX_SUITE:-$a}" > "$W/suite.txt"; cs=0   # bouchon du banc')
Path(dst_tok).write_text(t, encoding="utf-8")
t = rep(t, 'HF_HOME="$W/cache-hf" PYTHONPATH=src "$PY" - "$P" "$CFG" "$TACHES" > "$W/bloc-tokeniseur.txt" 2>&1 <<\'EOF\'',
        'cat > "$W/bloc-tokeniseur.txt" <<\'EOF\'   # bouchon du banc')
Path(dst).write_text(t, encoding="utf-8")
PYCOPIE
echo "lignes changées dans la copie des contrôles : $(diff "$V/controles_avant_depense_p3_v1.sh" "$R/controles-essai.sh" | grep -c '^>') ; copie au vrai tokeniseur : $(diff "$V/controles_avant_depense_p3_v1.sh" "$R/controles-essai-tok.sh" | grep -c '^>')"
epingle() { sed -n "s/^$1=\"\{0,1\}\([^\"#]*\)\"\{0,1\}.*/\1/p" "$R/controles-essai.sh" | sed 's/[[:space:]]*$//'; }
RELU=$(epingle CANDIDAT_RELU_CHEMIN); CFG_RELUE=$(epingle CONFIG_RELUE_CHEMIN); CONS_RELUES=$(epingle CONSIGNES_RELUES_CHEMIN)
RAPPORTS=$(epingle RAPPORTS_ATTENDUS); LOGJ=$(epingle REPETITION_JOUET_CHEMIN)
UN_RAPPORT=$(for x in $RAPPORTS; do echo "${x%%=*}"; break; done)
resceller() { local f; for f in "$@"; do (cd "$(dirname "$f")" && sha256sum "$(basename "$f")" > "$(basename "$f").sha256"); done; }
cfg_set() {   # $1 clé, $2 valeur JSON : la configuration de S changée (texte d'un cas)
    python3 - "$CFG" "$1" "$2" <<'PYS'
import json, sys
f, k, v = sys.argv[1:4]
c = json.load(open(f, encoding="utf-8"))
c[k] = json.loads(v)
open(f, "w", encoding="utf-8").write(json.dumps(c, indent=1, sort_keys=True, ensure_ascii=False) + "\n")
PYS
}
precoce() { echo "$1 : $2 : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
jouer() {   # $1 nom, $2 code attendu, $3 motif KO attendu (vide : cas sain), $4 base, $5 texte, $6 après, $7 copie des contrôles,
            # $8 nombre de KO attendu (vide : non compté)
    local nom=$1 attendu=$2 motif=$3 base=$4 texte=$5 apres=${6:-} ctl=${7:-$R/controles-essai.sh} nko=${8:-}
    git checkout -q -B "art-$nom" "$C1" || { precoce "$nom" "montage impossible"; return; }
    eval "$base"
    if [ -n "$(git status --porcelain)" ]; then git add -A . && git commit -qm "essai : base $nom" || { precoce "$nom" "commit de base impossible"; return; }; fi
    cp "$RELU" "$P" && cp "$CFG_RELUE" "$CFG" && cp "$CONS_RELUES" "$CONSIGNES" || { precoce "$nom" "copie impossible"; return; }
    eval "$texte"
    resceller "$P" "$CFG" "$CONSIGNES"
    git add "$P" "$P.sha256" "$CFG" "$CFG.sha256" "$CONSIGNES" "$CONSIGNES.sha256" && git commit -qm "essai : S $nom" || { precoce "$nom" "commit S impossible"; return; }
    local s; s=$(git rev-parse HEAD)
    git push -q "$R/distant.git" "art-$nom" || { precoce "$nom" "poussée impossible"; return; }
    eval "$apres"
    bash "$ctl" "$s" "$R/clone-$nom" > "$R/sortie-$nom.txt" 2>&1; local c=$?
    rm -rf "$R/clone-$nom" "$R/clone-$nom.travail" "$R/clone-$nom.suite.txt"
    local verdict="CONFORME"
    [ "$c" = "$attendu" ] || verdict="NON CONFORME (code $c, attendu $attendu)"
    if [ "$attendu" = 2 ]; then
        tail -1 "$R/sortie-$nom.txt" | grep -qF -- "$motif" || verdict="NON CONFORME (motif « $motif » absent de la dernière ligne)"
        [ "$(grep -c '^OK\|^KO' "$R/sortie-$nom.txt")" = 0 ] || verdict="NON CONFORME (lignes OK ou KO avant l'arrêt en code 2)"
    # motif cherché en texte fixe dans les lignes KO (une expression rationnelle lisait « ['temperature'] » comme une
    # classe de caractères : A45 refusé à tort au premier passage du banc ; awk et ENVIRON : ni tube, ni échappement)
    elif [ -n "$motif" ] && ! M="$motif" awk 'index($0, "KO") == 1 && index($0, ENVIRON["M"]) { t = 1 } END { exit !t }' "$R/sortie-$nom.txt"; then
        verdict="NON CONFORME (KO « $motif » absent)"; fi
    if [ -n "$nko" ] && [ "$(grep -c '^KO' "$R/sortie-$nom.txt")" != "$nko" ]; then verdict="NON CONFORME ($(grep -c '^KO' "$R/sortie-$nom.txt") KO, $nko attendu(s))"; fi
    if [ -z "$motif" ] && [ "$attendu" = 0 ] && ! tail -1 "$R/sortie-$nom.txt" | grep -qx "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES"; then
        verdict="NON CONFORME (dernière ligne)"; fi
    [ "$verdict" = CONFORME ] || NON_CONFORMES=$((NON_CONFORMES + 1))
    echo "$nom : code $c ; $(grep -c '^OK' "$R/sortie-$nom.txt") OK, $(grep -c '^KO' "$R/sortie-$nom.txt") KO ; $verdict"
    grep '^KO' "$R/sortie-$nom.txt" | sed 's/^/    /' | cut -c1-220
    [ "$attendu" = 2 ] && tail -1 "$R/sortie-$nom.txt" | cut -c1-200 | sed 's/^/    | /'
    return 0
}
copie_ctl() {   # $1 sortie, $2 expression sed sur la copie jouée (une épingle ou une constante changée), $3 copie de départ : une ligne exactement
    local depart=${3:-$R/controles-essai.sh}
    sed -e "$2" "$depart" > "$1"
    local n; n=$(diff "$depart" "$1" | grep -c '^>')
    [ "$n" = 1 ] || { echo "COPIE NON CONFORME : $1 change $n ligne(s) au lieu d'une : ARRÊT"; exit 2; }
}
NON_CONFORMES=0
NT=$(sed -n "s/^- Tests attendus : \`\([0-9]*\)\`.*/\1/p" "$RELU")
AUTRE_CODE=$(git rev-parse "$(git rev-list --max-count=1 "$C1" -- src/controle_ia/premier_test_ia/run.py)^")
TOK=$R/controles-essai-tok.sh
echo "tests $NT ; commit antérieur au dernier changement du lanceur de P3 : $AUTRE_CODE ; un rapport : $UN_RAPPORT"
jouer A00-sain 0 "" ":" ":"
# GO de calcul et décision de Lazar (module commun)
jouer A01-go-absent 1 "$GO absent, en double ou mal formé" "sed -i '/^| $GO |/d' registres/go.md" ":"
jouer A02-go-autre-type 1 "$GO : revendication, Lazar" "sed -i '/^| $GO |/s/| calcul |/| revendication |/' registres/go.md" ":"
jouer A03-go-accorde-par-un-autre 1 "$GO : calcul, session" "python3 -c \"import sys; f = 'registres/go.md'; L = open(f, encoding='utf-8').read().split('\\n'); L = ['|'.join(c if k != 7 else ' session ' for k, c in enumerate(l.split('|'))) if l.startswith('| $GO |') else l for l in L]; open(f, 'w', encoding='utf-8').write('\\n'.join(L))\"" ":"
jouer A04-go-revoque 1 "$GO révoqué" "echo '| GO-2026-10-17-98 | 2026-10-17 | révocation | révoque $GO (essai) | — | — | Lazar | essai |' >> registres/go.md" ":"
jouer A04b-go-revoque-ligne-mal-formee 1 "$GO révoqué" "echo '| GO-2026-10-17-98 | 2026-10-17 | révocation de $GO (essai) |' >> registres/go.md" ":"
jouer A04c-ligne-go-qui-mentionne-une-revocation 0 "" "echo '| GO-2026-10-17-97 | 2026-10-17 | revendication | essai : aucune révocation de $GO | — | — | Lazar | essai |' >> registres/go.md" ":"
jouer A05-decision-absente 1 "$REG absent, en double, ou sans la décision" "sed -i '/^| $REG |/d' registres/decisions.md" ":" "" "" 1
jouer A05b-decision-sans-son-texte 1 "$REG absent, en double, ou sans la décision" "sed -i '/^| $REG |/s/(b) P1 + P2 + P3 + pilote du papier C/(b) autre décision/' registres/decisions.md" ":" "" "" 1
jouer A06-texte-autre-go 1 "GO-2026-10-17-97 : seul $GO est accepté" ":" "sed -i 's/^- GO de calcul et décision de Lazar : \`$GO\`/- GO de calcul et décision de Lazar : \`GO-2026-10-17-97\`/' $P"
jouer A06b-texte-go-de-calcul-d-un-autre-perimetre 1 "GO-2026-10-17-01 : seul $GO est accepté" ":" "sed -i 's/^- GO de calcul et décision de Lazar : \`$GO\`/- GO de calcul et décision de Lazar : \`GO-2026-10-17-01\`/' $P"
jouer A07-texte-sans-ligne-go 1 "ligne « GO de calcul et décision de Lazar »" ":" "sed -i '/^- GO de calcul et décision de Lazar :/d' $P"
jouer A08-decision-revoquee-au-registre-des-go 1 "décision $REG révoquée au registre des GO" "echo '| GO-2026-10-17-96 | 2026-10-17 | révocation | révoque la décision $REG pour P3 (essai) | — | — | Lazar | essai |' >> registres/go.md" ":" "" "" 1
jouer A08b-decision-revoquee-au-registre-des-decisions 1 "décision $REG révoquée, retirée ou annulée par R-998" "echo '| R-998 | 2026-10-19 | Décision de Lazar (essai) : $REG retirée pour P3. | essai |' >> registres/decisions.md" ":" "" "" 1
# texte, configuration, consignes, pièces
jouer A11-texte-autre-que-le-candidat 1 "$P de S ≠ candidat relu" ":" "echo >> $P" "" "" 1
jouer A12-configuration-autre-que-la-relue 1 "$CFG de S ≠ configuration relue" ":" "cfg_set lot 4"
jouer A12b-consignes-autres-que-les-relues 1 "$CONSIGNES de S ≠ consignes relues" ":" "echo >> $CONSIGNES"
jouer A13-commit-du-code-cite-deux-fois 1 "cité 2 fois" ":" "sed -i '0,/^- Commit du code d.analyse : /{/^- Commit du code d.analyse : /p}' $P"
jouer A13b-commit-du-code-non-ancetre 1 "commit du code cité illisible, cité 1 fois, ou non ancêtre de S" "COTE=\$(git commit-tree '$C1^{tree}' -p '$C1' -m 'essai : commit de côté') && git push -q '$R/distant.git' \"\$COTE:refs/heads/cote-A13b\"" "sed -i \"s/^- Commit du code d.analyse : \\\`[0-9a-f]\\{40\\}\\\`/- Commit du code d'analyse : \\\`\$COTE\\\`/\" $P" "" "" 2
jouer A14-code-modifie-apres-cite 1 "arbre gelé modifié depuis le commit du code" "echo '# essai' >> src/controle_ia/premier_test_ia/run.py" ":"
jouer A16-script-de-l-instance-modifie 1 "empreinte de scripts/p3_instance.sh" "echo '# essai' >> scripts/p3_instance.sh" ":"
jouer A17-verdict-altere 1 "docs/verdicts/verdict-T0.5-pilote-v1.md non cité par son empreinte" "echo x >> docs/verdicts/verdict-T0.5-pilote-v1.md && resceller docs/verdicts/verdict-T0.5-pilote-v1.md" ":" "" "" 1
# A19 : le sceau retiré d'un fichier de docs/ (dossier scellé) donne deux KO, la pièce et verifier-arbre (CH-01)
jouer A19-provenance-sans-sceau 1 "docs/sources/donnees-T0.7/provenance-donnees-sondes-v1.md ou son sceau absent" "git rm -q docs/sources/donnees-T0.7/provenance-donnees-sondes-v1.md.sha256" ":" "" "" 2
jouer A20-faits-retires 1 "donnees/T0.7-faits-repe-v1/facts_true_false.csv ou son sceau absent" "git rm -q donnees/T0.7-faits-repe-v1/facts_true_false.csv donnees/T0.7-faits-repe-v1/facts_true_false.csv.sha256" ":"
jouer A21-s-ajoute-un-autre-fichier 1 "contenu de S inattendu" ":" "echo essai >> README.md && git add README.md"
jouer A21b-consignes-ajoutees-avant-s 1 "contenu de S inattendu" "cp $CONS_RELUES $CONSIGNES && resceller $CONSIGNES" ":"
jouer A22-lecture-precoce-citation-en-double 1 "lecture précoce" ":" "sed -i 's/^- Chemin des consignes de P3 : \(.*\)$/&\n- Chemin des consignes de P3 : \1/' $P"
jouer A22b-intitule-en-double 1 "intitulés absents ou cités plusieurs fois : « Tâches de P3 »" ":" "sed -i 's/^- Tâches de P3 : \(.*\)$/&\n- Tâches de P3 : \1/' $P"
jouer A23-problemes-non-vide 1 "problemes() non vide" ":" "sed -i 's/^## Contre-lecture$/## Contre-lecture retirée/' $P"
jouer A24-ligne-lancement-autre 1 "PREREG ou BRANCHE" ":" "sed -i 's/\`BRANCHE=calcul\/p3-reel-v1\`/\`BRANCHE=calcul\/p3-reel-v9\`/' $P"
jouer A25-suite-autre-nombre 1 "suite complète" ":" ":" "export FAUX_SUITE=$((NT + 1))"
unset FAUX_SUITE
# rapports et répétition jouet
jouer A26-rapport-altere 1 "rapport $UN_RAPPORT absent, non scellé" "echo x >> prereg/contre-lectures/$UN_RAPPORT && resceller prereg/contre-lectures/$UN_RAPPORT" ":"
jouer A26b-rapport-present-mais-non-cite 1 "rapport $UN_RAPPORT présent et scellé, mais non cité par le texte" ":" "sed -i 's|\`prereg/contre-lectures/$UN_RAPPORT\`|rapport non cité (essai)|' $P"
jouer A27-rapport-de-trop 1 "rapports présents" "echo x > prereg/contre-lectures/P3-premier-test-v1-relecture-autre-v1.md && resceller prereg/contre-lectures/P3-premier-test-v1-relecture-autre-v1.md" ":"
jouer A28-journal-repetition-altere 1 "répétition jouet" "echo x >> $LOGJ && resceller $LOGJ" ":"
jouer A29-copie-versee-de-la-recuperation-modifiee 1 "script répété ≠ copie versée à S : recuperation_p3_v1.sh" "echo '# essai' >> $V/recuperation_p3_v1.sh && resceller $V/recuperation_p3_v1.sh" ":"
copie_ctl "$R/controles-A30.sh" "s/^CODE_RELU=[0-9a-f]\{40\}/CODE_RELU=$AUTRE_CODE/"
jouer A30-code-relu-autre 1 "arbre gelé de S ≠ code relu" ":" ":" "" "$R/controles-A30.sh"
copie_ctl "$R/controles-A31.sh" "s/^REPETITION_JOUET=[0-9a-f]\{64\}/REPETITION_JOUET=$(git show "$C1:$LOGJ" | sed "s/^commit du code répété : .*/commit du code répété : $AUTRE_CODE/" | sha256sum | cut -d' ' -f1)/"
jouer A31-journal-autre-commit 1 "répétition jouet" "sed -i 's/^commit du code répété : .*/commit du code répété : $AUTRE_CODE/' $LOGJ && resceller $LOGJ" ":" "" "$R/controles-A31.sh"
# épingles des candidats (une autre empreinte : texte, configuration et consignes de S refusés ; la répétition jouet
# nomme le candidat et les consignes relus, CH-15 : un KO de plus pour le candidat et pour les consignes)
copie_ctl "$R/controles-A30b.sh" "s/^CANDIDAT_RELU=[0-9a-f]\{64\}/CANDIDAT_RELU=$(printf autre | sha256sum | cut -d' ' -f1)/"
jouer A30b-candidat-relu-autre 1 "$P de S ≠ candidat relu" ":" ":" "" "$R/controles-A30b.sh" 3
copie_ctl "$R/controles-A30c.sh" "s/^CONFIG_RELUE=[0-9a-f]\{64\}/CONFIG_RELUE=$(printf autre | sha256sum | cut -d' ' -f1)/"
jouer A30c-configuration-relue-autre 1 "$CFG de S ≠ configuration relue" ":" ":" "" "$R/controles-A30c.sh" 2
copie_ctl "$R/controles-A30d.sh" "s/^CONSIGNES_RELUES=[0-9a-f]\{64\}/CONSIGNES_RELUES=$(printf autre | sha256sum | cut -d' ' -f1)/"
jouer A30d-consignes-relues-autres 1 "$CONSIGNES de S ≠ consignes relues" ":" ":" "" "$R/controles-A30d.sh" 3
# épingles mal formées ou absentes, module commun absent, clonage impossible : code 2, rien n'est contrôlé
copie_ctl "$R/controles-Z1a.sh" "s/^CANDIDAT_RELU=[0-9a-f]\{64\}/CANDIDAT_RELU=A_EPINGLER/"
jouer Z1a-candidat-non-epingle 2 "candidat relu non épinglé" ":" ":" "" "$R/controles-Z1a.sh" 0
copie_ctl "$R/controles-Z1b.sh" "s|^CANDIDAT_RELU_CHEMIN=brouillons/|CANDIDAT_RELU_CHEMIN=prereg/|"
jouer Z1b-candidat-hors-des-brouillons 2 "candidat relu non épinglé" ":" ":" "" "$R/controles-Z1b.sh" 0
copie_ctl "$R/controles-Z1c.sh" "s/^CONFIG_RELUE=[0-9a-f]\{64\}/CONFIG_RELUE=A_EPINGLER/"
jouer Z1c-configuration-non-epinglee 2 "configuration relue non épinglée" ":" ":" "" "$R/controles-Z1c.sh" 0
copie_ctl "$R/controles-Z1c4.sh" "s|^CONFIG_RELUE_CHEMIN=brouillons/|CONFIG_RELUE_CHEMIN=prereg/|"
jouer Z1c4-configuration-hors-des-brouillons 2 "configuration relue non épinglée" ":" ":" "" "$R/controles-Z1c4.sh" 0
copie_ctl "$R/controles-Z1c2.sh" "s/^CONSIGNES_RELUES=[0-9a-f]\{64\}/CONSIGNES_RELUES=A_EPINGLER/"
jouer Z1c2-consignes-non-epinglees 2 "consignes relues non épinglées" ":" ":" "" "$R/controles-Z1c2.sh" 0
copie_ctl "$R/controles-Z1c3.sh" "s|^CONSIGNES_RELUES_CHEMIN=brouillons/|CONSIGNES_RELUES_CHEMIN=prereg/|"
jouer Z1c3-consignes-hors-des-brouillons 2 "consignes relues non épinglées" ":" ":" "" "$R/controles-Z1c3.sh" 0
copie_ctl "$R/controles-Z1d.sh" "s/^RAPPORTS_ATTENDUS=\"/RAPPORTS_ATTENDUS=\"P3-premier-test-v1-mal-forme.txt=00 /"
jouer Z1d-rapports-mal-formes 2 "rapports attendus mal formés" ":" ":" "" "$R/controles-Z1d.sh" 0
copie_ctl "$R/controles-Z1e.sh" "s/^RAPPORTS_ATTENDUS=\"\([^ \"]*\)[^\"]*\"/RAPPORTS_ATTENDUS=\"\1\"/"
jouer Z1e-un-seul-rapport 2 "au moins les deux rapports" ":" ":" "" "$R/controles-Z1e.sh" 0
copie_ctl "$R/controles-Z1f.sh" "s/^CODE_RELU=[0-9a-f]\{40\}/CODE_RELU=A_EPINGLER/"
jouer Z1f-code-non-epingle 2 "code relu ou répétition jouet non épinglés" ":" ":" "" "$R/controles-Z1f.sh" 0
copie_ctl "$R/controles-Z1g.sh" "s/^REPETITION_JOUET=[0-9a-f]\{64\}/REPETITION_JOUET=A_EPINGLER/"
jouer Z1g-repetition-non-epinglee 2 "code relu ou répétition jouet non épinglés" ":" ":" "" "$R/controles-Z1g.sh" 0
copie_ctl "$R/controles-Z1h.sh" "s|^VERIF=.*|VERIF=$R/module-absent/verifications_p3_v1.py|"
jouer Z1h-module-commun-absent 2 "module commun" ":" ":" "" "$R/controles-Z1h.sh" 0
copie_ctl "$R/controles-Z1i.sh" "s|^DEPOT=.*|DEPOT=$R/depot-absent.git|"
jouer Z1i-clonage-impossible 2 "clonage impossible" ":" ":" "" "$R/controles-Z1i.sh" 0
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
direct Z2c-troisieme-argument "usage" "$S_SAIN" "$R/clone-Z2c" relance
direct Z2d-dossier-vide "dossier neuf absent" "$S_SAIN" ""
direct Z2d2-un-seul-argument "usage" "$S_SAIN"
direct Z2e-s-invalide "S invalide" "abc" "$R/clone-Z2e"
echo garde > "$R/suite-existe.suite.txt"
direct Z2f-trace-de-la-suite-existante "suite.txt existe déjà (R12)" "$S_SAIN" "$R/suite-existe"
direct Z2g-s-bien-forme-mais-absent "introuvable" "$(printf '0%.0s' {1..40})" "$R/clone-Z2g"
rm -rf "$R/clone-Z2g"
# candidats relus versés sans leur sceau
jouer A50-candidat-relu-sans-sceau 1 "candidat relu absent, non scellé ou d'empreinte différente" "git rm -q $RELU.sha256" ":"
jouer A51-configuration-relue-sans-sceau 1 "configuration relue absente, non scellée ou d'empreinte différente" "git rm -q $CFG_RELUE.sha256" ":"
jouer A51b-consignes-relues-sans-sceau 1 "consignes relues absentes, non scellées ou d'empreinte différente" "git rm -q $CONS_RELUES.sha256" ":"
# valeurs de bornes non citées par le texte (aux espaces réduites)
jouer A44b-borne-non-citee 1 "valeur non citée par le texte : 22 200 s" ":" "sed -i 's/22 200 s/22 201 s/g' $P"
# dépendances que l'instance installe, différentes de celles du pilote
jouer A53-dependances-autres 1 "dépendances différentes de celles du pilote" "echo 'paquet-essai==1.0' >> requirements-gpu.txt" ":"
# un fichier scellé de docs/ altéré hors des pièces : seul verifier-arbre le voit (CH-14)
jouer A54-verifier-arbre-seul 1 "verifier-arbre" "echo x >> docs/notes/P3-mesures-v2/puissance-p3-v1.txt" ":" "" "" 1
# modules gelés d'étapes antérieures modifiés (CH-08) : le KO de la garde rétablie s'ajoute à ceux de l'arbre gelé
jouer A55-module-du-pilote-modifie 1 "modules gelés d'étapes antérieures modifiés (pilote : code 1" "echo '# essai' >> src/controle_ia/environnements/pilote_a.py" ":"
jouer A55b-module-des-notations-modifie 1 "modules gelés d'étapes antérieures modifiés (pilote : code 0 ; notations : code 1)" "echo '# essai' >> src/controle_ia/environnements/lire_notations_pilote.py" ":"
# garde de calcul : GO de calcul échu dans le registre de S
jouer A52-go-de-calcul-echu 1 "garde de calcul" "sed -i -E '/^\\| $GO \\|/s/\\| 2026-11-[0-9]{2} \\|/| 2026-10-11 |/' registres/go.md" ":"
# sceau du préenregistrement ajouté avant S (S ne l'ajoute pas) ; sceau des tâches altéré
jouer A39-sceau-ajoute-avant-s 1 "S n'est pas le commit qui ajoute" "cp $RELU $P && resceller $P" ":"
jouer A40-sceau-des-taches-altere 1 "sceaux" "echo '0000  autre' > donnees/t05-pilote-v1/taches-pilote-60-v1.json.sha256" ":"
# bornes du bloc 9 : délai du run, plafond de l'amorce (scripts de l'instance), crédit, prix, surveillance, offre (copies versées)
jouer A41-delai-du-run-change 1 "délai externe du run" "sed -i 's/--kill-after=5m 300m)/--kill-after=5m 310m)/' scripts/p3_instance.sh" ":"
jouer A42-plafond-de-l-amorce-change 1 "plafond de l'amorce" "sed -i 's/--kill-after=5m 360m /--kill-after=5m 350m /' scripts/amorce_instance_p3.sh" ":"
jouer A43-credit-change 1 "heures du crédit exigé" "sed -i 's/^HEURES_CREDIT=6.5 /HEURES_CREDIT=6.0 /' $V/lancer_p3_v1.sh && resceller $V/lancer_p3_v1.sh" ":"
jouer A43b-prix-plafond-change 1 "prix plafond du lanceur" "sed -i 's/^PRIX_MAX=1.30 /PRIX_MAX=1.40 /' $V/lancer_p3_v1.sh && resceller $V/lancer_p3_v1.sh" ":"
jouer A43c-prix-plafond-du-controle-a-cinq-minutes-change 1 "prix plafond du contrôle à cinq minutes" "sed -i 's/^PRIX_MAX=1.30 /PRIX_MAX=1.40 /' $V/controle_cinq_minutes_p3_v1.sh && resceller $V/controle_cinq_minutes_p3_v1.sh" ":"
jouer A44-plafond-de-la-surveillance-change 1 "plafond de la surveillance" "sed -i 's/^PLAFOND_S=22200 /PLAFOND_S=22000 /' $V/surveiller_p3_v1.sh && resceller $V/surveiller_p3_v1.sh" ":"
jouer A44c-plafond-ecrit-par-le-lanceur-change 1 "plafond de la surveillance écrit par le lanceur" "sed -i 's/^PLAFOND_SURVEILLANCE_S=22200 /PLAFOND_SURVEILLANCE_S=22000 /' $V/lancer_p3_v1.sh && resceller $V/lancer_p3_v1.sh" ":"
jouer A44d-coeurs-de-l-offre-changes 1 "cœurs effectifs exigés de l'offre" "sed -i 's/^COEURS_MIN=16 /COEURS_MIN=8 /' $V/lancer_p3_v1.sh && resceller $V/lancer_p3_v1.sh" ":"
jouer A44e-memoire-vive-de-l-offre-changee 1 "mémoire vive exigée de l'offre" "sed -i 's/^MEMOIRE_VIVE_MIN_MO=128000 /MEMOIRE_VIVE_MIN_MO=64000 /' $V/lancer_p3_v1.sh && resceller $V/lancer_p3_v1.sh" ":"
jouer A44f-borne-de-telechargement-autre 1 "valeur non citée par le texte : téléchargement au plus 0,99 USD par Go" "sed -i 's/^TELECHARGEMENT_MAX=[0-9.]* /TELECHARGEMENT_MAX=0.99 /' $V/lancer_p3_v1.sh && resceller $V/lancer_p3_v1.sh" ":"
jouer A44g-borne-de-telechargement-non-fixee 1 "borne de téléchargement du lanceur non fixée" "sed -i 's/^TELECHARGEMENT_MAX=[0-9.]* /TELECHARGEMENT_MAX=A_FIXER /' $V/lancer_p3_v1.sh && resceller $V/lancer_p3_v1.sh" ":"
# configuration de S changée : gardes du bloc 9 (le KO « ≠ configuration relue » s'y ajoute)
jouer A45-parametre-autre-que-celui-du-pilote 1 "paramètres différents de ceux du pilote : ['temperature']" ":" "cfg_set temperature 0.7"
jouer A46-chemin-des-consignes-autre 1 "chemin des consignes de la configuration" ":" "cfg_set chemin_consignes '\"prereg/P3-consignes-v2.md\"'"
jouer A47-durees-autres 1 "durées de la configuration" ":" "cfg_set duree_max_s 14000"
jouer A48-mode-jouet 1 "mode jouet" ":" "cfg_set mode '\"jouet\"'"
jouer A49-configuration-incomplete 1 "configuration de P3 incomplète" ":" "python3 -c \"import json; f = '$CFG'; c = json.load(open(f)); c.pop('n_plancher'); open(f, 'w').write(json.dumps(c, indent=1, sort_keys=True))\""
jouer A49b-n-faits-max-non-nul 1 "n_faits_max non nul" ":" "cfg_set n_faits_max 10"
# branche de résultats présente
jouer A32-branche-presente 1 "branche calcul/p3-reel-v1 : code 0" ":" ":" "git push -q $R/distant.git art-A32-branche-presente:refs/heads/calcul/p3-reel-v1"
git -C "$R/distant.git" branch -D calcul/p3-reel-v1 > /dev/null
# bloc 10 : vrai tokeniseur de l'agent (copie qui le garde) : cas sain et artefacts
allonger() {   # $1 rang du texte cité (0 à 5) allongé, empreinte des consignes reportée dans la configuration
    python3 - "$CONSIGNES" "$1" <<'PYT' && cfg_set consignes_sha256 "\"$(sha256sum "$CONSIGNES" | cut -d' ' -f1)\""
import sys
f, rang = sys.argv[1], int(sys.argv[2])
L = open(f, encoding="utf-8").read().split("\n")
blocs, k, dans = [], -1, False
for i, l in enumerate(L):
    if l.startswith("> "):
        if not dans:
            k += 1; blocs.append([])
        blocs[k].append(i); dans = True
    else:
        dans = False
assert len(blocs) == 6, len(blocs)
L[blocs[rang][-1]] += " Always keep this in mind."
open(f, "w", encoding="utf-8").write("\n".join(L))
PYT
}
jouer B00-sain-vrai-tokeniseur 0 "" ":" ":" "" "$TOK"
jouer B01-consigne-du-temoin-plus-longue 1 "temoin, consigne :" ":" "allonger 2" "" "$TOK"
jouer B01b-indication-du-temoin-plus-longue 1 "temoin, indication :" ":" "allonger 3" "" "$TOK"
jouer B01c-consigne-de-la-mention-plus-longue 1 "mention, consigne :" ":" "allonger 4" "" "$TOK"
jouer B02-faits-exclus-autre-compte 1 "faits exclus" ":" "cfg_set faits_exclus_attendus 6" "" "$TOK"
jouer B03-texte-attendu-absent-de-l-ouverture 1 "ouverture sans" ":" "python3 -c \"import json; f = '$CFG'; c = json.load(open(f)); c['agent']['texte_attendu_ouverture'] = 'Today Date: 1 Jan 2000'; open(f, 'w').write(json.dumps(c, indent=1, sort_keys=True))\"" "" "$TOK"
# valeurs citées du bloc 10 changées dans une copie (une ligne) : comparaison des mesures aux valeurs citées (CH-12)
copie_ctl "$R/controles-B04.sh" 's/^GABARIT_CONSIGNES = {52: 56, 51: 4} /GABARIT_CONSIGNES = {52: 55, 51: 5} /' "$TOK"
jouer B04-longueurs-dans-le-gabarit-autres-que-citees 1 "consignes dans le gabarit" ":" ":" "" "$R/controles-B04.sh" 1
copie_ctl "$R/controles-B05.sh" 's/^GABARIT_INDICATIONS = {10: 60}/GABARIT_INDICATIONS = {11: 60}/' "$TOK"
jouer B05-indications-dans-le-gabarit-autres-que-citees 1 "indications dans le gabarit" ":" ":" "" "$R/controles-B05.sh" 1
# sous-gardes du module commun : GO et décision, sur des textes et des registres synthétiques (CH-14) ; code 1 et motif
# attendu sur la dernière ligne, ou code 0
VERIF_V=$V/verifications_p3_v1.py
git show "$C1:registres/go.md" > "$R/go-sain.md"; git show "$C1:registres/decisions.md" > "$R/decisions-sain.md"
git show "$C1:$RELU" > "$R/texte-sain.md"
module_go() {   # $1 nom, $2 code attendu, $3 motif, $4 commande sur le texte, $5 sur le registre des GO, $6 sur celui des décisions
    local t="$R/go-$1-texte.md" g="$R/go-$1-go.md" dc="$R/go-$1-decisions.md" c
    eval "$4" < "$R/texte-sain.md" > "$t"; eval "$5" < "$R/go-sain.md" > "$g"; eval "$6" < "$R/decisions-sain.md" > "$dc"
    python3 -I "$VERIF_V" go "$t" "$g" "$dc" > "$R/module-go-$1.txt" 2>&1; c=$?
    if [ "$c" = "$2" ] && tail -1 "$R/module-go-$1.txt" | grep -qF -- "$3"; then echo "$1 : code $c ; CONFORME"
    else echo "$1 : code $c ; NON CONFORME ($(tail -1 "$R/module-go-$1.txt" | cut -c1-160))"; NON_CONFORMES=$((NON_CONFORMES + 1)); fi
}
module_go G00-go-sain 0 "$GO ($REG) conforme" cat cat cat
module_go G01-ligne-go-en-double 1 "absente, en double ou mal formée" "sed 's/^- GO de calcul et décision de Lazar : .*/&\n&/'" cat cat
module_go G02-ligne-go-mal-formee 1 "absente, en double ou mal formée" "sed 's/^\(- GO de calcul et décision de Lazar : \`$GO\`\) (\($REG\))/\1 \2/'" cat cat
module_go G03-go-en-double-au-registre 1 "$GO absent, en double ou mal formé" cat "sed 's/^| $GO |.*/&\n&/'" cat
module_go G04-go-a-sept-colonnes 1 "$GO absent, en double ou mal formé" cat "sed '/^| $GO |/s/| [^|]* |\$/|/'" cat
module_go G05-decision-qui-cite-r-192-sans-la-revoquer 0 "$GO ($REG) conforme" cat cat "sed '\$a | R-997 | 2026-10-19 | Suite de P3 sous $REG (essai), sans révocation. | essai |'"
module_go G06-revocation-d-un-autre-go-sous-r-192 0 "$GO ($REG) conforme" cat "sed '\$a | GO-2026-10-17-95 | 2026-10-17 | révocation | révoque GO-2026-10-17-01 (pilote du papier C, $REG ; essai) | — | — | Lazar | essai |'" cat
module_go G07-registre-des-decisions-absent 1 "absent ou illisible" cat cat "cat > /dev/null; rm -f '$R/go-G07-registre-des-decisions-absent-decisions.md'; :"
# sous-gardes du module commun sur des journaux de la répétition altérés (le module est le texte lu par les contrôles et le
# scellement ; A28 et A31 le jouent dans le script entier) : code 1 et motif attendu sur la dernière ligne
NOM_C=$(basename "$RELU"); SHA_C=$(git show "$C1:$RELU" | sha256sum | cut -d' ' -f1); CODE_R=$(epingle CODE_RELU)
NOM_K=$(basename "$CONS_RELUES"); SHA_K=$(git show "$C1:$CONS_RELUES" | sha256sum | cut -d' ' -f1)
module() {   # $1 nom, $2 motif, $3 commande sed (ou awk) qui altère le journal
    local j="$R/journal-$1.txt" c
    git show "$C1:$LOGJ" > "$R/journal-sain.txt"
    eval "$3" < "$R/journal-sain.txt" > "$j"
    python3 -I "$VERIF_V" repetition "$CODE_R" "$j" "$NOM_C" "$SHA_C" "$NOM_K" "$SHA_K" > "$R/module-$1.txt" 2>&1; c=$?
    if [ "$c" = 1 ] && tail -1 "$R/module-$1.txt" | grep -qF -- "$2"; then echo "$1 : code 1 ; CONFORME"
    else echo "$1 : code $c ; NON CONFORME ($(tail -1 "$R/module-$1.txt" | cut -c1-160))"; NON_CONFORMES=$((NON_CONFORMES + 1)); fi
}
python3 -I "$VERIF_V" repetition "$CODE_R" <(git show "$C1:$LOGJ") "$NOM_C" "$SHA_C" "$NOM_K" "$SHA_K" > "$R/module-sain.txt" 2>&1 \
    && echo "M00-journal-sain : code 0 ; CONFORME" || { echo "M00-journal-sain : NON CONFORME ($(tail -1 "$R/module-sain.txt"))"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
module M01-candidat-absent "ligne absente ou en double : candidat répété" "sed '/^candidat répété : /d'"
module M02-candidat-autre "ligne absente ou en double : candidat répété" "sed 's/^candidat répété : .*/candidat répété : autre.md 0000/'"
module M03-deux-lignes-candidat "ligne absente ou en double" "sed 's/^candidat répété : .*/&\\n&/'"
module M03b-deux-candidats-differents "plusieurs lignes « candidat répété »" "sed 's/^candidat répété : .*/&\\ncandidat répété : autre.md 0000/'"
module M04-passage-manquant "passage : passage 3-manque : code 1" "sed '/^passage 3-manque : /d'"
module M05-passage-autre-code "passage : passage 1-sain : code 0" "sed 's/^passage 1-sain : code 0 /passage 1-sain : code 1 /'"
module M06-recuperation-conforme-absente "ligne absente ou en double : récupération (arret-synthetique-episodes)" "sed '/^récupération (arret-synthetique-episodes) : /d'"
module M06b-gardes-reelles-absentes "ligne absente ou en double : récupération (gardes-reelles)" "sed '/^récupération (gardes-reelles) : /d'"
module M07-ko-dans-un-cas-sain "récupération (passage-1-sain) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES : KO" "sed '/^récupération (passage-1-sain) : /a\\    KO  6a essai'"
module M08-artefact-a-deux-ko "récupération (artefact-scores-manquants)" "sed '/^récupération (artefact-scores-manquants) : /a\\    KO  2b essai'"
module M09-artefact-autre-ko "récupération (artefact-ajout-hors-perimetre)" "sed '/^    KO  1c /s/KO  1c /KO  1d /'"
module M10-ko-hors-du-bloc "récupération (artefact-ajout-hors-perimetre)" "awk '/^    KO  1c /{next} {print} /^récupération \\(artefact-scores-alteres\\)/{print \"    KO  1c essai\"}'"
# M11 : « _v1 » retiré du nom du premier script répété (les noms de P3 portent un chiffre, « p3 » : la classe [a-z_] du
# banc des notations ne les lisait pas, et le journal restait sain : relevé au premier passage du banc)
module M11-script-mal-forme "ligne « script répété » mal formée" "sed '0,/^script répété : /s/^script répété : \\([a-z0-9_]*\\)_v1\\.\\([a-z]*\\) /script répété : \\1.\\2 /'"
module M12-script-en-double "script répété en double" "awk '/^script répété : /&&!d{print; d=1} {print}'"
module M13-script-manquant "les deux attendus exactement" "sed '0,/^script répété : /{/^script répété : /d}'"
module M14-fin-absente "ligne absente ou en double : FIN DE LA RÉPÉTITION" "sed '/^FIN DE LA RÉPÉTITION$/d'"
module M15-consignes-absentes "ligne absente ou en double : consignes répétées" "sed '/^consignes répétées : /d'"
module M16-consignes-autres "ligne absente ou en double : consignes répétées" "sed 's/^consignes répétées : .*/consignes répétées : autres.md 0000/'"
module M17-tous-conformes-de-trop "trois récupérations conformes et une récupération des traces seules attendues" "sed '\$a récupération (autre) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES'"
python3 -I "$VERIF_V" repetition "$CODE_R" "$R/journal-sain.txt" > "$R/module-usage.txt" 2>&1; c=$?
[ "$c" = 2 ] && grep -qF "usage" "$R/module-usage.txt" && echo "M18-usage-faux : code 2 ; CONFORME" || { echo "M18-usage-faux : code $c ; NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
# sous-gardes de « preuves » (lues par le lanceur et le scellement) sur des journaux synthétiques : cas sain (cinq
# journaux ; trois, comme la copie de la répétition finale), puis une ligne d'échec (« NON CONFORME », trace
# d'exception, jeton affiché) ajoutée avant le verdict, un script éprouvé sous deux empreintes, un script éprouvé
# manquant, un journal nommé inconnu ; seuls le code et un motif court s'affichent
PRV=$R/preuves; mkdir -p "$PRV/sain"
ecrire_preuves() {   # $1 dossier : les cinq journaux sains, empreintes factices cohérentes
    python3 - "$1" <<'PYP'
import sys
d = sys.argv[1]
J = {"banc-lanceur-p3-v1.log": ("FIN DU BANC DU LANCEUR DE P3 ; cas non conformes : 0", ["lancer_p3_v1.sh", "verifications_p3_v1.py", "essais_lanceur_p3_v1.sh"]),
     "banc-surveillance-p3-v1.log": ("FIN DU BANC DE LA SURVEILLANCE DE P3 ; cas non conformes : 0", ["surveiller_p3_v1.sh", "controle_cinq_minutes_p3_v1.sh", "essais_surveillance_p3_v1.sh"]),
     "banc-controles-p3-v1.log": ("FIN DU BANC DES CONTRÔLES DE P3 ; cas non conformes : 0", ["controles_avant_depense_p3_v1.sh", "verifications_p3_v1.py", "essais_controles_p3_v1.sh"]),
     "banc-scellement-p3-v1.log": ("FIN DU BANC DU SCELLEMENT DE P3 ; cas non conformes : 0", ["sceller_p3_v1.sh", "verifications_p3_v1.py", "essais_scellement_p3_v1.sh"]),
     "repetition-finale-p3-v1.log": ("RÉPÉTITION FINALE : CONFORME", ["sceller_p3_v1.sh", "controles_avant_depense_p3_v1.sh", "verifications_p3_v1.py", "repetition_finale_p3_v1.sh"])}
for n, (v, s) in J.items():
    open(f"{d}/{n}", "w", encoding="utf-8").write("".join(f"script éprouvé : {x} {'a' * 64}\n" for x in s) + v + "\n")
PYP
}
ecrire_preuves "$PRV/sain"
python3 -I "$VERIF_V" preuves "$PRV/sain" > "$R/preuves-sain.txt" 2>&1 && [ "$(grep -c . "$R/preuves-sain.txt")" = 11 ] \
    && echo "P00-preuves-saines : code 0 ; 11 scripts éprouvés ; CONFORME" \
    || { echo "P00-preuves-saines : à revoir ($(tail -1 "$R/preuves-sain.txt"))"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
python3 -I "$VERIF_V" preuves "$PRV/sain" banc-lanceur-p3-v1.log banc-surveillance-p3-v1.log banc-controles-p3-v1.log > "$R/preuves-trois.txt" 2>&1 \
    && [ "$(grep -c . "$R/preuves-trois.txt")" = 8 ] && echo "P00b-preuves-trois-journaux : code 0 ; 8 scripts éprouvés ; CONFORME" \
    || { echo "P00b-preuves-trois-journaux : à revoir ($(tail -1 "$R/preuves-trois.txt"))"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
for k in 1 2 3; do
    mkdir -p "$PRV/faute-$k"; ecrire_preuves "$PRV/faute-$k"
    case $k in 1) l="cas X : code 1 ; NON CONF""ORME (essai)" ;; 2) l="Traceback (most recent call last): essai" ;; 3) l="JETON AFFI""CHÉ : sortie-essai.txt" ;; esac
    sed -i "1a $l" "$PRV/faute-$k/banc-scellement-p3-v1.log"
    python3 -I "$VERIF_V" preuves "$PRV/faute-$k" > "$R/preuves-faute-$k.txt" 2>&1; c=$?
    if [ "$c" = 1 ] && tail -1 "$R/preuves-faute-$k.txt" | grep -qF "ligne d'échec avant le verdict"; then echo "P0$k-preuves-ligne-d-echec : code 1 ; CONFORME"
    else echo "P0$k-preuves-ligne-d-echec : code $c ; à revoir"; NON_CONFORMES=$((NON_CONFORMES + 1)); fi
done
mkdir -p "$PRV/deux-empreintes"; ecrire_preuves "$PRV/deux-empreintes"
sed -i "s/^script éprouvé : verifications_p3_v1.py a*$/script éprouvé : verifications_p3_v1.py $(printf 'b%.0s' {1..64})/" "$PRV/deux-empreintes/banc-lanceur-p3-v1.log"
python3 -I "$VERIF_V" preuves "$PRV/deux-empreintes" > "$R/preuves-deux.txt" 2>&1; c=$?
[ "$c" = 1 ] && tail -1 "$R/preuves-deux.txt" | grep -qF "éprouvé sous deux empreintes" && echo "P04-preuves-deux-empreintes : code 1 ; CONFORME" \
    || { echo "P04-preuves-deux-empreintes : code $c ; à revoir"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
mkdir -p "$PRV/manquant"; ecrire_preuves "$PRV/manquant"
sed -i '/^script éprouvé : essais_surveillance_p3_v1.sh /d' "$PRV/manquant/banc-surveillance-p3-v1.log"
python3 -I "$VERIF_V" preuves "$PRV/manquant" > "$R/preuves-manquant.txt" 2>&1; c=$?
[ "$c" = 1 ] && tail -1 "$R/preuves-manquant.txt" | grep -qF "essais_surveillance_p3_v1.sh" && echo "P05-preuves-script-manquant : code 1 ; CONFORME" \
    || { echo "P05-preuves-script-manquant : code $c ; à revoir"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
python3 -I "$VERIF_V" preuves "$PRV/sain" banc-autre-p3-v1.log > "$R/preuves-inconnu.txt" 2>&1; c=$?
[ "$c" = 1 ] && tail -1 "$R/preuves-inconnu.txt" | grep -qF "journaux nommés inconnus" && echo "P06-preuves-journal-inconnu : code 1 ; CONFORME" \
    || { echo "P06-preuves-journal-inconnu : code $c ; à revoir"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
cd "$R" && rm -rf "$R/source" "$R/distant.git"
echo "FIN DU BANC DES CONTRÔLES DE P3 ; cas non conformes : $NON_CONFORMES"
[ "$NON_CONFORMES" = 0 ] || exit 1
