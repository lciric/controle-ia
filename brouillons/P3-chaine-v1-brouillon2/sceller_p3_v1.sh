#!/usr/bin/env bash
# Scellement du préenregistrement du premier test boîte blanche sur l'organisme (i-a) (P3, R-192, R-202), v1, brouillon 2
# (contre-lecture R2 de la chaîne traitée : CH-03, CH-14, CH-15 ; chaîne de treize scripts), décliné du scellement des
# notations refaites du pilote de T0.5 (docs/procedures/notations-T0.5-v2/sceller_notations_v1.sh) sous un nom nouveau
# (R12) : aucun champ n'est rempli au scellement (l'entropie, tirée une fois par SeedSequence, est déjà citée par le
# candidat relu) : le préenregistrement est la copie, octet pour octet, du candidat relu et vérifié (contre-lecture R2),
# la configuration celle de la configuration relue, les consignes celles des consignes relues. HEAD = origin/main, arbre
# suivi propre, sorties absentes (R12) ; adresses de origin : le dépôt de travail seulement ; scripts de la chaîne égaux à
# leurs copies versées et suivies ; épingles des contrôles lues ici, aucune restée « A_EPINGLER » ; candidat,
# configuration et consignes relus à leurs épingles, versés et scellés à la ligne exacte ; configuration relue qui cite
# les consignes relues (chemin et empreinte) ; arbre gelé de HEAD égal au code relu, cité une fois par le candidat ;
# intitulés lus par le lanceur, le module commun et le script de l'instance : une fois chacun ; journal de la répétition
# jouet à son épingle, au code relu, au candidat et aux consignes relus (CH-15), conforme (module commun
# verifications_p3_v1.py, le même texte que les contrôles) ; preuves des essais : les journaux des bancs et de la
# répétition finale (liste PREUVES_EXIGEES : les cinq), suivis à HEAD avec leur sceau exact, conformes au module commun,
# et chaque script qu'ils éprouvent égal à sa copie versée (même texte que le lanceur : un journal oublié ou devenu
# caduc ne laisse pas sceller un S que le lanceur refuserait, CH-03) ; rapports épinglés, seuls de leur famille, cités
# (texte aux espaces réduites) ; branche de résultats absente ; GO de calcul et décision de Lazar relus dans les
# registres de HEAD ; préenregistrement, configuration et consignes scellés (problemes() vide) ; verifier-arbre ; un seul
# commit S qui n'ajoute que ces six fichiers, poussé, puis relu sur le dépôt distant. Un échec avant le commit retire les
# fichiers créés ici (et seulement eux). Tout arrêt sort en code 2.
# La copie jouée par la répétition finale change les lignes H, DEPOT, DISTANT et PREUVES_EXIGEES (elle ne peut exiger ni
# son propre journal, qui n'existe pas encore, ni celui du banc du scellement, dont le script éprouvé est celui que la
# répétition remplace par sa copie) ; ces quatre lignes changées sont comptées et déclarées par la répétition finale.
# Usage : sceller_p3_v1.sh
set -euo pipefail
trap 'echo "arrêt du scellement (ligne $LINENO)"; exit 2' ERR
[ $# -eq 0 ] || { echo "usage : sceller_p3_v1.sh (sans argument)"; exit 2; }
H=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/p3-v1
DEPOT=/home/user/controle-ia-travail
DISTANT=https://github.com/lciric/controle-ia-travail          # seule adresse de lecture et de poussée admise (jamais la copie publique)
PREUVES_EXIGEES="banc-lanceur-p3-v1.log banc-surveillance-p3-v1.log banc-controles-p3-v1.log banc-scellement-p3-v1.log repetition-finale-p3-v1.log"
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
VERSEES=docs/procedures/P3-premier-test-v1
P=prereg/P3-premier-test-i-a-v1.md; CFG=prereg/P3-premier-test-config-v1.json; CONSIGNES=prereg/P3-consignes-v1.md
CTL=$H/controles_avant_depense_p3_v1.sh
VERIF=$H/verifications_p3_v1.py
plat() { tr '\n' ' ' < "$1" | tr -s ' '; }      # texte aux espaces réduites : citations passées à la ligne
epingle() { sed -n "s/^$1=\"\{0,1\}\([^\"#]*\)\"\{0,1\}.*/\1/p" "$CTL" | sed 's/[[:space:]]*$//'; }
grep -q "^[A-Z_]*=\"\{0,1\}A_EPINGLER" "$CTL" && { echo "épingle restée « A_EPINGLER » dans les contrôles"; exit 2; }
RELU=$(epingle CANDIDAT_RELU_CHEMIN); RELU_SHA=$(epingle CANDIDAT_RELU)
CFG_RELUE=$(epingle CONFIG_RELUE_CHEMIN); CFG_RELUE_SHA=$(epingle CONFIG_RELUE)
CONS_RELUES=$(epingle CONSIGNES_RELUES_CHEMIN); CONS_RELUES_SHA=$(epingle CONSIGNES_RELUES)
RAPPORTS=$(epingle RAPPORTS_ATTENDUS); CODE_RELU=$(epingle CODE_RELU)
REPETITION=$(epingle REPETITION_JOUET); REPETITION_CHEMIN=$(epingle REPETITION_JOUET_CHEMIN)
[[ "$RELU_SHA" =~ ^[0-9a-f]{64}$ && "$RELU" == brouillons/* && "$CFG_RELUE_SHA" =~ ^[0-9a-f]{64}$ && "$CFG_RELUE" == brouillons/* \
   && "$CONS_RELUES_SHA" =~ ^[0-9a-f]{64}$ && "$CONS_RELUES" == brouillons/* ]] \
    || { echo "candidat, configuration ou consignes relus non épinglés"; exit 2; }
[[ "$CODE_RELU" =~ ^[0-9a-f]{40}$ && "$REPETITION" =~ ^[0-9a-f]{64}$ && "$REPETITION_CHEMIN" == "$VERSEES"/* ]] \
    || { echo "code relu ou répétition jouet non épinglés"; exit 2; }
n=0
for x in $RAPPORTS; do
    [[ "$x" =~ ^P3-premier-test-v1-[a-z0-9-]+-v1\.(md|json|tar)=[0-9a-f]{64}$ ]] \
        || { echo "rapport épinglé hors de la famille de la contre-lecture : ${x%%=*}"; exit 2; }
    n=$((n + 1))
done
[ "$n" -ge 2 ] || { echo "rapports épinglés : au moins deux attendus"; exit 2; }
[ -n "$PREUVES_EXIGEES" ] || { echo "aucun journal de preuve exigé"; exit 2; }
cd "$DEPOT"
# toutes les adresses de origin, en lecture et en poussée : le dépôt de travail seulement (une seule admise dans chaque
# sens : git pousse vers chaque adresse de poussée ; CLAUDE.md : jamais lciric/controle-ia)
for sens in "" "--push"; do
    u=$(git remote get-url --all $sens origin 2>/dev/null || true)
    [ "$u" = "$DISTANT" ] || [ "$u" = "$DISTANT.git" ] || { echo "adresse de origin ${sens:-en lecture} « $(printf '%s' "$u" | tr '\n' ' ') » ≠ $DISTANT (une seule adresse admise)"; exit 2; }
done
git fetch -q origin main
[ "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)" ] || { echo "HEAD ≠ origin/main : pousser d'abord les préalables"; exit 2; }
[ -z "$(git status --porcelain --untracked-files=no)" ] || { echo "arbre suivi non propre"; exit 2; }
for f in "$P" "$P.sha256" "$CFG" "$CFG.sha256" "$CONSIGNES" "$CONSIGNES.sha256"; do [ -e "$f" ] && { echo "$f existe déjà (R12)"; exit 2; }; done
CHAINE="verifications_p3_v1.py controles_avant_depense_p3_v1.sh lancer_p3_v1.sh sceller_p3_v1.sh surveiller_p3_v1.sh
        controle_cinq_minutes_p3_v1.sh recuperation_p3_v1.sh repetition_jouet_p3_v1.sh repetition_finale_p3_v1.sh
        essais_lanceur_p3_v1.sh essais_controles_p3_v1.sh essais_scellement_p3_v1.sh essais_surveillance_p3_v1.sh"
# copies versées, journaux de preuve, candidat, configuration et consignes relus, rapports et journal de la répétition
# suivis à HEAD : l'arbre suivi étant propre, le disque est alors égal à HEAD (un fichier présent mais non suivi
# passerait cmp et verifier-arbre)
SUIVIS=$(for s in $CHAINE; do printf '%s/%s %s/%s.sha256\n' "$VERSEES" "$s" "$VERSEES" "$s"; done
         for j in $PREUVES_EXIGEES; do printf '%s/%s %s/%s.sha256\n' "$VERSEES" "$j" "$VERSEES" "$j"; done
         for x in $RAPPORTS; do printf 'prereg/contre-lectures/%s prereg/contre-lectures/%s.sha256\n' "${x%%=*}" "${x%%=*}"; done)
for f in $SUIVIS "$RELU" "$RELU.sha256" "$CFG_RELUE" "$CFG_RELUE.sha256" "$CONS_RELUES" "$CONS_RELUES.sha256" \
         "$REPETITION_CHEMIN" "$REPETITION_CHEMIN.sha256"; do
    git ls-files --error-unmatch -- "$f" > /dev/null 2>&1 || { echo "$f non suivi à HEAD"; exit 2; }
done
for s in $CHAINE; do
    cmp -s "$H/$s" "$VERSEES/$s" || { echo "$s du bloc-notes ≠ copie versée"; exit 2; }
done
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier $(for s in $CHAINE; do printf '%s/%s ' "$VERSEES" "$s"; done) > /dev/null \
    || { echo "sceau d'une copie versée non conforme"; exit 2; }
for paire in "$RELU=$RELU_SHA" "$CFG_RELUE=$CFG_RELUE_SHA" "$CONS_RELUES=$CONS_RELUES_SHA"; do
    f=${paire%%=*}; e=${paire#*=}
    [ "$(sha256sum "$f" | cut -d' ' -f1)" = "$e" ] && [ "$(cat "$f.sha256")" = "$e  $(basename "$f")" ] \
        || { echo "$f ≠ épingle, ou sceau différent de la ligne exacte"; exit 2; }
done
# la configuration relue cite les consignes relues : chemin scellé de S et empreinte (sinon le run s'arrêterait, R11)
python3 -I -c 'import json, sys; c = json.load(open(sys.argv[1], encoding="utf-8")); sys.exit(0 if (c.get("chemin_consignes"), c.get("consignes_sha256")) == (sys.argv[2], sys.argv[3]) else 1)' \
    "$CFG_RELUE" "$CONSIGNES" "$CONS_RELUES_SHA" || { echo "la configuration relue ne cite pas les consignes relues ($CONSIGNES, ${CONS_RELUES_SHA:0:12}…)"; exit 2; }
[ "$(grep -c "Commit du code d'analyse : \`" "$RELU")" = 1 ] || { echo "commit du code cité zéro ou plusieurs fois par le candidat"; exit 2; }
# chacun des intitulés lus par le lanceur de P3, le module commun et le script de l'instance figure exactement une fois
# dans le texte (une seconde occurrence, même de même valeur, serait ignorée)
INTITULES=("Configuration de P3 (empreinte canonique)" "Tâches de P3" "Commit du code d'analyse" "Entropie"
           "Tests attendus" "Chemin de la configuration de P3" "Chemin des tâches de P3" "Chemin des consignes de P3"
           "GO de calcul et décision de Lazar")
for x in "${INTITULES[@]}"; do
    [ "$(grep -oF "$x : \`" "$RELU" | wc -l)" = 1 ] || { echo "intitulé « $x » cité zéro ou plusieurs fois par le candidat"; exit 2; }
done
# rapports : seuls de leur famille (aucun autre fichier P3-premier-test-v1-* suivi sous prereg/contre-lectures/)
git ls-files prereg/contre-lectures/ > "$H/.contre-lectures-$$.txt"
presents=$(grep -E '^prereg/contre-lectures/P3-premier-test-v1-' "$H/.contre-lectures-$$.txt" | grep -v '\.sha256$' | xargs -r -n1 basename | sort | tr '\n' ' ' || true)
rm -f "$H/.contre-lectures-$$.txt"
attendus=$(for x in $RAPPORTS; do echo "${x%%=*}"; done | sort | tr '\n' ' ')
[ "$presents" = "$attendus" ] || { echo "rapports présents « $presents » ≠ épinglés « $attendus »"; exit 2; }
# branche de résultats absente du dépôt distant (la ligne « Lancement » scellée la fige)
c=0; git ls-remote --exit-code origin refs/heads/calcul/p3-reel-v1 > /dev/null 2>&1 || c=$?
[ "$c" = 2 ] || { echo "branche calcul/p3-reel-v1 : code $c (2 attendu : absente)"; exit 2; }
for x in $RAPPORTS; do
    f="prereg/contre-lectures/${x%%=*}"
    [ "$(sha256sum "$f" | cut -d' ' -f1)" = "${x#*=}" ] && plat "$RELU" | grep -qF "\`$f\` (\`${x#*=}\`)" \
        || { echo "rapport ${x%%=*} : empreinte différente de l'épingle, ou non cité par le candidat"; exit 2; }
done
GELES=$(PYTHONPATH=src "$PY" -I -c "import sys; sys.path.insert(0, 'src'); from controle_ia.harnais.validation_reelle import CHEMINS_GELES; print(' '.join(CHEMINS_GELES))")
# CHEMINS_GELES illisible : garde redondante (l'import échoue avant, piège ERR), sans artefact possible (CH-14)
[ -n "$GELES" ] || { echo "CHEMINS_GELES illisible"; exit 2; }
# shellcheck disable=SC2086
git diff --quiet "$CODE_RELU" HEAD -- $GELES || { echo "arbre gelé de HEAD ≠ code relu épinglé ($CODE_RELU)"; exit 2; }
grep -qF "Commit du code d'analyse : \`$CODE_RELU\`" "$RELU" || { echo "le candidat relu ne cite pas le code relu"; exit 2; }
[ "$(sha256sum "$REPETITION_CHEMIN" | cut -d' ' -f1)" = "$REPETITION" ] && [ "$(cat "$REPETITION_CHEMIN.sha256")" = "$REPETITION  $(basename "$REPETITION_CHEMIN")" ] \
    || { echo "journal de la répétition jouet absent, d'une autre empreinte que l'épingle, ou sceau différent"; exit 2; }
SORTIE_REP=$(python3 -I "$VERIF" repetition "$CODE_RELU" "$REPETITION_CHEMIN" "$(basename "$RELU")" "$RELU_SHA" \
             "$(basename "$CONS_RELUES")" "$CONS_RELUES_SHA" 2>&1) \
    || { echo "journal de la répétition jouet non conforme : $(printf '%s\n' "$SORTIE_REP" | tail -1)"; exit 2; }
while read -r s e; do
    [ "$(sha256sum "$VERSEES/$s" | cut -d' ' -f1)" = "$e" ] || { echo "script répété ≠ copie versée : $s"; exit 2; }
done <<< "$SORTIE_REP"
# preuves des essais (CH-03) : journaux exigés, suivis, à leur sceau exact ; conformes au module commun ; chaque script
# éprouvé égal à sa copie versée (le lanceur refuserait sinon un S figé, R12)
for j in $PREUVES_EXIGEES; do
    [ "$(cat "$VERSEES/$j.sha256")" = "$(sha256sum "$VERSEES/$j" | cut -d' ' -f1)  $j" ] \
        || { echo "preuves des essais : sceau de $j absent ou non conforme"; exit 2; }
done
# shellcheck disable=SC2086
SORTIE_PREUVES=$(python3 -I "$VERIF" preuves "$VERSEES" $PREUVES_EXIGEES 2>&1) \
    || { echo "preuves des essais : $(printf '%s\n' "$SORTIE_PREUVES" | tail -1)"; exit 2; }
while read -r s e; do
    [ "$(sha256sum "$VERSEES/$s" | cut -d' ' -f1)" = "$e" ] || { echo "preuves des essais : $s éprouvé ≠ copie versée"; exit 2; }
done <<< "$SORTIE_PREUVES"
echo "preuves des essais : $(echo $PREUVES_EXIGEES | wc -w) journaux conformes ; $(printf '%s\n' "$SORTIE_PREUVES" | grep -c .) scripts éprouvés égaux à leurs copies versées"
# GO de calcul et décision de Lazar, relus dans les registres de HEAD (les contrôles et le lanceur les relisent ensuite)
SORTIE_GO=$(python3 -I "$VERIF" go "$RELU" registres/go.md registres/decisions.md 2>&1) \
    || { echo "GO de calcul et décision de Lazar non conformes : $(printf '%s\n' "$SORTIE_GO" | tail -1)"; exit 2; }
echo "GO de calcul et décision de Lazar : $SORTIE_GO"
COMMITTE=0
SIX=("$P" "$P.sha256" "$CFG" "$CFG.sha256" "$CONSIGNES" "$CONSIGNES.sha256")
fin() {
    local code=$?
    if [ "$code" != 0 ] && [ "$COMMITTE" = 0 ]; then
        # un commit refusé après git add laisse les fichiers dans l'index : les en retirer d'abord
        git reset -q -- "${SIX[@]}" > /dev/null 2>&1 || true
        for f in "${SIX[@]}"; do git ls-files --error-unmatch "$f" >/dev/null 2>&1 || rm -f "$f"; done
        echo "échec avant le commit : fichiers créés retirés"
    fi
    [ "$code" = 0 ] || exit 2
}
trap fin EXIT
cp "$CONS_RELUES" "$CONSIGNES"; cp "$CFG_RELUE" "$CFG"; cp "$RELU" "$P"
PYTHONPATH=src "$PY" -m controle_ia.scellement sceller "$CONSIGNES" "$CFG" > /dev/null
PYTHONPATH=src "$PY" -c "from controle_ia.prereg import sceller_prereg; sceller_prereg('$P')"
[ "$(cut -d' ' -f1 "$P.sha256")" = "$RELU_SHA" ] && [ "$(cut -d' ' -f1 "$CFG.sha256")" = "$CFG_RELUE_SHA" ] \
    && [ "$(cut -d' ' -f1 "$CONSIGNES.sha256")" = "$CONS_RELUES_SHA" ] \
    || { echo "sceaux du préenregistrement, de la configuration ou des consignes ≠ épingles"; exit 2; }
VA=$(mktemp)
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier-arbre . > "$VA" 2>&1 \
    || { grep '^ÉCHEC' "$VA" || tail -3 "$VA"; rm -f "$VA"; echo "verifier-arbre en échec"; exit 2; }
# dernière ligne de verifier-arbre : garde redondante (le code de sortie suffirait), sans artefact propre (CH-14)
tail -1 "$VA" | grep -qx "arbre intact" || { rm -f "$VA"; echo "verifier-arbre : dernière ligne inattendue"; exit 2; }
rm -f "$VA"
git add "${SIX[@]}"
git commit -q -F - <<EOF
P3 : premier test boîte blanche sur l'organisme (i-a), préenregistrement v1 scellé (R-192, R-202)

Préenregistrement $RELU_SHA (copie du candidat relu $RELU) ; configuration $CFG_RELUE_SHA
(copie de $CFG_RELUE) ; consignes $CONS_RELUES_SHA (copie de $CONS_RELUES). Code relu $CODE_RELU.
Lancement : PREREG=$P, BRANCHE=calcul/p3-reel-v1.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01DKDpnUsVMQCfVuMfR5uXNL
EOF
COMMITTE=1
S=$(git rev-parse HEAD)
# contenu de S et origin/main après la poussée : gardes redondantes (git add des seuls six fichiers ; poussée relue),
# sans artefact possible hors d'un crochet (CH-14)
[ "$(git diff --name-only --no-renames "$S^" "$S" | sort | tr '\n' ' ')" = "$(printf '%s\n' "${SIX[@]}" | sort | tr '\n' ' ')" ] \
    || { echo "contenu de S inattendu"; exit 2; }
timeout 600 git push -q origin HEAD:main || { echo "poussée de S en échec : S reste local ; repousser avant tout lancement"; exit 2; }
git fetch -q origin main
[ "$(git rev-parse origin/main)" = "$S" ] || { echo "origin/main ≠ S après la poussée"; exit 2; }
echo "S $S poussé ; préenregistrement $RELU_SHA"
