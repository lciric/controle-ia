#!/usr/bin/env bash
# Scellement du préenregistrement complémentaire des notations refaites du pilote de T0.5 (N-021, option (a)), v1,
# décliné du scellement du pilote (docs/procedures/pilote-T0.5-v1/sceller_pilote_v1.sh) : aucune entropie n'est tirée
# (celle du pilote est reprise et citée par le texte relu) et aucun champ n'est rempli au scellement : le préenregistrement
# est la copie, octet pour octet, du candidat relu et vérifié (contre-lecture R2), et la configuration celle de la
# configuration relue. HEAD = origin/main, arbre suivi propre, sorties absentes (R12) ; scripts de la chaîne égaux à
# leurs copies versées et suivies ; épingles des contrôles lues ici, aucune restée « A_EPINGLER » ; candidat et
# configuration relus à leurs épingles, versés et scellés ; arbre gelé de HEAD égal au code relu ; journal de la
# répétition jouet à son épingle, au code relu ; rapports épinglés de la seule famille de la contre-lecture ; décision de
# Lazar sur N-021 relue dans les registres de HEAD ; préenregistrement et configuration scellés (problemes() vide) ;
# verifier-arbre ; un seul commit S qui n'ajoute que ces quatre fichiers, poussé, puis relu sur le dépôt distant. Un
# échec avant le commit retire les fichiers créés ici (et seulement eux). Tout arrêt sort en code 2.
# Brouillon 3 (contre-lecture R2 de la chaîne) : décision de Lazar et journal de la répétition jouet lus par le module
# commun verifications_notations_v1.py, le même texte que les contrôles (ligne « candidat répété » comprise) ; rapports
# seuls de leur famille ; branche de résultats absente ; commit du code cité une seule fois ; sceaux du candidat et de la
# configuration relus à la ligne exacte : le scellement ne peut pas produire un S que les contrôles refuseraient sur ces
# points.
# Usage : sceller_notations_v1.sh
set -euo pipefail
trap 'echo "arrêt du scellement (ligne $LINENO)"; exit 2' ERR
[ $# -eq 0 ] || { echo "usage : sceller_notations_v1.sh (sans argument)"; exit 2; }
H=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/notations-v1
DEPOT=/home/user/controle-ia-travail
DISTANT=https://github.com/lciric/controle-ia-travail          # seule adresse de lecture et de poussée admise (jamais la copie publique)
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
VERSEES=docs/procedures/notations-T0.5-v1
P=prereg/T0.5-pilote-notations-v1.md; CFG=prereg/T0.5-pilote-notations-config-v1.json
CTL=$H/controles_avant_depense_notations_v1.sh
VERIF=$H/verifications_notations_v1.py
epingle() { sed -n "s/^$1=\"\{0,1\}\([^\"#]*\)\"\{0,1\}.*/\1/p" "$CTL" | sed 's/[[:space:]]*$//'; }
grep -q "^[A-Z_]*=\"\{0,1\}A_EPINGLER" "$CTL" && { echo "épingle restée « A_EPINGLER » dans les contrôles"; exit 2; }
RELU=$(epingle CANDIDAT_RELU_CHEMIN); RELU_SHA=$(epingle CANDIDAT_RELU)
CFG_RELUE=$(epingle CONFIG_RELUE_CHEMIN); CFG_RELUE_SHA=$(epingle CONFIG_RELUE)
RAPPORTS=$(epingle RAPPORTS_ATTENDUS); CODE_RELU=$(epingle CODE_RELU)
REPETITION=$(epingle REPETITION_JOUET); REPETITION_CHEMIN=$(epingle REPETITION_JOUET_CHEMIN)
[[ "$RELU_SHA" =~ ^[0-9a-f]{64}$ && "$RELU" == brouillons/* && "$CFG_RELUE_SHA" =~ ^[0-9a-f]{64}$ && "$CFG_RELUE" == brouillons/* ]] \
    || { echo "candidat ou configuration relus non épinglés"; exit 2; }
[[ "$CODE_RELU" =~ ^[0-9a-f]{40}$ && "$REPETITION" =~ ^[0-9a-f]{64}$ && "$REPETITION_CHEMIN" == "$VERSEES"/* ]] \
    || { echo "code relu ou répétition jouet non épinglés"; exit 2; }
n=0
for x in $RAPPORTS; do
    [[ "$x" =~ ^T0\.5-notations-v1-[a-z0-9-]+-v1\.(md|json|tar)=[0-9a-f]{64}$ ]] \
        || { echo "rapport épinglé hors de la famille de la contre-lecture : ${x%%=*}"; exit 2; }
    n=$((n + 1))
done
[ "$n" -ge 2 ] || { echo "rapports épinglés : au moins deux attendus"; exit 2; }
cd "$DEPOT"
# adresse de origin, en lecture et en poussée : le dépôt de travail seulement (contre-lecture R2 de la chaîne, critique
# de complétude, constat 7 ; CLAUDE.md : jamais lciric/controle-ia)
for sens in "" "--push"; do
    u=$(git remote get-url $sens origin 2>/dev/null || true)
    [ "$u" = "$DISTANT" ] || [ "$u" = "$DISTANT.git" ] || { echo "adresse de origin ${sens:-en lecture} « $u » ≠ $DISTANT"; exit 2; }
done
git fetch -q origin main
[ "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)" ] || { echo "HEAD ≠ origin/main : pousser d'abord les préalables"; exit 2; }
[ -z "$(git status --porcelain --untracked-files=no)" ] || { echo "arbre suivi non propre"; exit 2; }
for f in "$P" "$P.sha256" "$CFG" "$CFG.sha256"; do [ -e "$f" ] && { echo "$f existe déjà (R12)"; exit 2; }; done
CHAINE="construire_pilote_jouet_v1.py verifications_notations_v1.py controles_avant_depense_notations_v1.sh lancer_notations_v1.sh
        sceller_notations_v1.sh surveiller_notations_v1.sh recuperation_notations_v1.sh repetition_jouet_notations_v1.sh
        repetition_finale_notations_v1.sh essais_lanceur_notations_v1.sh essais_controles_notations_v1.sh
        essais_scellement_notations_v1.sh essais_surveillance_notations_v1.sh"
# copies versées, candidat, configuration relue, rapports et journal de la répétition suivis à HEAD : l'arbre suivi étant
# propre, le disque est alors égal à HEAD (un fichier présent mais non suivi passerait cmp et verifier-arbre)
SUIVIS=$(for s in $CHAINE; do printf '%s/%s %s/%s.sha256\n' "$VERSEES" "$s" "$VERSEES" "$s"; done
         for x in $RAPPORTS; do printf 'prereg/contre-lectures/%s prereg/contre-lectures/%s.sha256\n' "${x%%=*}" "${x%%=*}"; done)
for f in $SUIVIS "$RELU" "$RELU.sha256" "$CFG_RELUE" "$CFG_RELUE.sha256" "$REPETITION_CHEMIN" "$REPETITION_CHEMIN.sha256"; do
    git ls-files --error-unmatch -- "$f" > /dev/null 2>&1 || { echo "$f non suivi à HEAD"; exit 2; }
done
for s in $CHAINE; do
    cmp -s "$H/$s" "$VERSEES/$s" || { echo "$s du bloc-notes ≠ copie versée"; exit 2; }
done
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier $(for s in $CHAINE; do printf '%s/%s ' "$VERSEES" "$s"; done) > /dev/null \
    || { echo "sceau d'une copie versée non conforme"; exit 2; }
[ "$(sha256sum "$RELU" | cut -d' ' -f1)" = "$RELU_SHA" ] && [ "$(cat "$RELU.sha256")" = "$RELU_SHA  $(basename "$RELU")" ] \
    || { echo "candidat relu ≠ épingle, ou sceau différent de la ligne exacte"; exit 2; }
[ "$(sha256sum "$CFG_RELUE" | cut -d' ' -f1)" = "$CFG_RELUE_SHA" ] && [ "$(cat "$CFG_RELUE.sha256")" = "$CFG_RELUE_SHA  $(basename "$CFG_RELUE")" ] \
    || { echo "configuration relue ≠ épingle, ou sceau différent de la ligne exacte"; exit 2; }
[ "$(grep -c "Commit du code d'analyse : \`" "$RELU")" = 1 ] || { echo "commit du code cité zéro ou plusieurs fois par le candidat"; exit 2; }
# chacun des intitulés lus par le lanceur des notations et par le script de l'instance figure exactement une fois dans
# le texte (contre-lecture R2, angle « code du lanceur » : une seconde occurrence, même de même valeur, serait ignorée)
INTITULES=("Configuration des notations (empreinte canonique)" "Run du pilote noté" "Manifeste du pilote noté"
           "Épisodes du pilote noté" "Arrêt du pilote noté" "Commit du code d'analyse" "Entropie" "Tâches du pilote"
           "Tests attendus" "Chemin de la configuration des notations" "Chemin des tâches du pilote noté"
           "Chemin du manifeste du pilote noté" "Chemin des épisodes du pilote noté" "Chemin de l'arrêt du pilote noté")
for x in "${INTITULES[@]}"; do
    [ "$(grep -oF "$x : \`" "$RELU" | wc -l)" = 1 ] || { echo "intitulé « $x » cité zéro ou plusieurs fois par le candidat"; exit 2; }
done
# rapports : seuls de leur famille (aucun autre fichier T0.5-notations-v1-* suivi sous prereg/contre-lectures/)
git ls-files prereg/contre-lectures/ > "$H/.contre-lectures-$$.txt"
presents=$(grep -E '^prereg/contre-lectures/T0\.5-notations-v1-' "$H/.contre-lectures-$$.txt" | grep -v '\.sha256$' | xargs -r -n1 basename | sort | tr '\n' ' ' || true)
rm -f "$H/.contre-lectures-$$.txt"
attendus=$(for x in $RAPPORTS; do echo "${x%%=*}"; done | sort | tr '\n' ' ')
[ "$presents" = "$attendus" ] || { echo "rapports présents « $presents » ≠ épinglés « $attendus »"; exit 2; }
# branche de résultats absente du dépôt distant (la ligne « Lancement » scellée la fige)
c=0; git ls-remote --exit-code origin refs/heads/calcul/t05-notations-reel-v1 > /dev/null 2>&1 || c=$?
[ "$c" = 2 ] || { echo "branche calcul/t05-notations-reel-v1 : code $c (2 attendu : absente)"; exit 2; }
for x in $RAPPORTS; do
    f="prereg/contre-lectures/${x%%=*}"
    [ "$(sha256sum "$f" | cut -d' ' -f1)" = "${x#*=}" ] && grep -qF "\`$f\` (\`${x#*=}\`)" "$RELU" \
        || { echo "rapport ${x%%=*} : empreinte différente de l'épingle, ou non cité par le candidat"; exit 2; }
done
GELES=$(PYTHONPATH=src "$PY" -I -c "import sys; sys.path.insert(0, 'src'); from controle_ia.harnais.validation_reelle import CHEMINS_GELES; print(' '.join(CHEMINS_GELES))")
[ -n "$GELES" ] || { echo "CHEMINS_GELES illisible"; exit 2; }
# shellcheck disable=SC2086
git diff --quiet "$CODE_RELU" HEAD -- $GELES || { echo "arbre gelé de HEAD ≠ code relu épinglé ($CODE_RELU)"; exit 2; }
grep -qF "Commit du code d'analyse : \`$CODE_RELU\`" "$RELU" || { echo "le candidat relu ne cite pas le code relu"; exit 2; }
[ "$(sha256sum "$REPETITION_CHEMIN" | cut -d' ' -f1)" = "$REPETITION" ] && [ "$(cut -d' ' -f1 "$REPETITION_CHEMIN.sha256")" = "$REPETITION" ] \
    || { echo "journal de la répétition jouet absent ou d'une autre empreinte que l'épingle"; exit 2; }
grep -qxF "commit du code répété : $CODE_RELU" "$REPETITION_CHEMIN" \
    || { echo "journal de la répétition jouet d'un autre commit que le code relu"; exit 2; }
grep -qxF "FIN DE LA RÉPÉTITION" "$REPETITION_CHEMIN" || { echo "journal de la répétition jouet inachevé"; exit 2; }
SORTIE_REP=$(python3 -I "$VERIF" repetition "$CODE_RELU" "$REPETITION_CHEMIN" "$(basename "$RELU")" "$RELU_SHA" 2>&1) \
    || { echo "journal de la répétition jouet non conforme : $(printf '%s\n' "$SORTIE_REP" | tail -1)"; exit 2; }
while read -r s e; do
    [ "$(sha256sum "$VERSEES/$s" | cut -d' ' -f1)" = "$e" ] || { echo "script répété ≠ copie versée : $s"; exit 2; }
done <<< "$SORTIE_REP"
# décision de Lazar sur N-021, relue dans les registres de HEAD (les contrôles et le lanceur la relisent ensuite)
SORTIE_GO=$(python3 -I "$VERIF" go "$RELU" registres/go.md registres/decisions.md 2>&1) \
    || { echo "décision de Lazar sur N-021 non conforme : $(printf '%s\n' "$SORTIE_GO" | tail -1)"; exit 2; }
echo "décision de Lazar sur N-021 : $SORTIE_GO"
COMMITTE=0
fin() {
    local code=$?
    if [ "$code" != 0 ] && [ "$COMMITTE" = 0 ]; then
        # un commit refusé après git add laisse les fichiers dans l'index : les en retirer d'abord
        git reset -q -- "$P" "$P.sha256" "$CFG" "$CFG.sha256" > /dev/null 2>&1 || true
        for f in "$P" "$P.sha256" "$CFG" "$CFG.sha256"; do git ls-files --error-unmatch "$f" >/dev/null 2>&1 || rm -f "$f"; done
        echo "échec avant le commit : fichiers créés retirés"
    fi
    [ "$code" = 0 ] || exit 2
}
trap fin EXIT
cp "$CFG_RELUE" "$CFG"; cp "$RELU" "$P"
PYTHONPATH=src "$PY" -m controle_ia.scellement sceller "$CFG" > /dev/null
PYTHONPATH=src "$PY" -c "from controle_ia.prereg import sceller_prereg; sceller_prereg('$P')"
[ "$(cut -d' ' -f1 "$P.sha256")" = "$RELU_SHA" ] && [ "$(cut -d' ' -f1 "$CFG.sha256")" = "$CFG_RELUE_SHA" ] \
    || { echo "sceaux du préenregistrement ou de la configuration ≠ épingles"; exit 2; }
VA=$(mktemp)
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier-arbre . > "$VA" 2>&1 \
    || { grep '^ÉCHEC' "$VA" || tail -3 "$VA"; rm -f "$VA"; echo "verifier-arbre en échec"; exit 2; }
tail -1 "$VA" | grep -qx "arbre intact" || { rm -f "$VA"; echo "verifier-arbre : dernière ligne inattendue"; exit 2; }
rm -f "$VA"
git add "$P" "$P.sha256" "$CFG" "$CFG.sha256"
git commit -q -F - <<EOF
T0.5 : notations décisives refaites du pilote, préenregistrement complémentaire v1 scellé (N-021, option (a))

Préenregistrement $RELU_SHA (copie du candidat relu $RELU) ; configuration $CFG_RELUE_SHA
(copie de $CFG_RELUE). Code relu $CODE_RELU. Lancement : PREREG=$P, BRANCHE=calcul/t05-notations-reel-v1.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01VJdZpSMxSdk2SJ1ScmdfNv
EOF
COMMITTE=1
S=$(git rev-parse HEAD)
[ "$(git diff --name-only "$S^" "$S" | sort | tr '\n' ' ')" = "$(printf '%s\n' "$CFG" "$CFG.sha256" "$P" "$P.sha256" | sort | tr '\n' ' ')" ] \
    || { echo "contenu de S inattendu"; exit 2; }
timeout 600 git push -q origin HEAD:main || { echo "poussée de S en échec : S reste local ; repousser avant tout lancement"; exit 2; }
git fetch -q origin main
[ "$(git rev-parse origin/main)" = "$S" ] || { echo "origin/main ≠ S après la poussée"; exit 2; }
echo "S $S poussé ; préenregistrement $RELU_SHA"
