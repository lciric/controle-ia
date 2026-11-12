#!/usr/bin/env bash
# Répétition jouet de la chaîne de l'instance du pilote de T0.5 (ETUDE=pilote, MODE=jouet), au commit C du dépôt de
# travail (état des lieux, HR-04 et PL-14 : le chemin « pilote » n'a pas été joué depuis R-065, au script ancien).
# Dépôt jetable cloné de C, dépôt nu local en guise de dépôt distant, jetons factices, env -i. Le préenregistrement jouet
# est produit par le générateur du pilote en mode jouet (configuration réduite, quatre tâches dérivées de la source par
# deriver_taches_pilote_v1.py), puis scellé. Passages :
#   1. cas sain : BRANCHE=calcul/t05-pilote-jouet-a-v1 → code 0, résultats et traces poussés, vecteurs sur
#      donnees/t05/<run> (commit sans parent), empreinte égale à celle d'episodes.json ;
#   2. artefact : même branche, déjà présente → arrêt avant l'installation (code 2) ;
#   3. premier lancement manqué : BRANCHE=calcul/t05-pilote-jouet-b-v1, environnement absent (cause d'infrastructure
#      simulée, après la poussée initiale) → code 1, traces poussées, aucun episodes.json ;
#   4. relancement : BRANCHE=calcul/t05-pilote-jouet-b-v2 → code 0.
# Puis la récupération du pilote (copies dont changent l'adresse du dépôt, le préfixe des branches, le motif du run, le
# mode attendu, la carte absente) : mode premier sur le passage 1, mode relance sur le passage 4 (branche du premier
# lancement : b-v1, lue sans episodes.json) ; artefact : mode relance dont le premier lancement porte des épisodes (a-v1)
# → un contrôle en échec attendu (relecture R2, CH-09). Temps mesuré de la ligne « AMORCE » à la fin des tests (Z-5).
# Le journal commence par « commit du code répété : <C entier> », puis « script répété : <nom> <sha256> » pour chaque
# script exécuté (copiés au début dans RACINE/scripts et joués depuis ces copies), que les contrôles avant dépense
# comparent aux copies versées à S (CH-12 ; vérification courte, VH-02). Une récupération de plus, sur une branche dont
# un fichier de notations manque, attend un seul KO, 4c (VH-07). La récupération sort en code 1 quand un contrôle échoue.
# Usage : repetition_jouet_pilote_v1.sh C RACINE_NEUVE
set -uo pipefail
C=$1; R=$2
BN=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
H=$BN/pilote-v1
PY=$BN/scellement-revalidation/venv-gpu-neuf/bin/python
VENV=$BN/scellement-revalidation/venv-gpu-neuf
D=/home/user/controle-ia-travail
P=prereg/T0.5-pilote-8B-v1.md; CFG=prereg/T0.5-pilote-config-v1.json; TJ=donnees/t05-pilote-v1/taches-pilote-jouet-4-v1.json
[ -e "$R" ] && { echo "$R existe déjà (R12)"; exit 2; }
mkdir -p "$R" && cd "$R" || exit 2
git clone -q --no-local "$D" source && cd source && git checkout -q "$C" && git checkout -q -B main || exit 2
echo "commit du code répété : $(git rev-parse HEAD)"
mkdir -p "$R/scripts" || exit 2
SCRIPTS_REPETES="deriver_taches_pilote_v1.py remplir_pilote_v1.py normaliser_pilote_v1.py recuperation_pilote_v1.sh"
for s in $SCRIPTS_REPETES; do cp "$H/$s" "$R/scripts/$s" || exit 2; done
cp "$0" "$R/scripts/repetition_jouet_pilote_v1.sh" || exit 2
for s in $SCRIPTS_REPETES repetition_jouet_pilote_v1.sh; do echo "script répété : $s $(sha256sum "$R/scripts/$s" | cut -d' ' -f1)"; done
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
"$PY" -I "$R/scripts/deriver_taches_pilote_v1.py" donnees/20261007-082440-t05-extraction/taches-evaluation.json \
    76cdeace861d2fff45ca732c55c2d97611dcd47edc7c27d62bdad4c37755e67e 4 "$TJ" > "$R/derivation.json" || exit 2
PYTHONPATH=src "$PY" -m controle_ia.scellement sceller "$TJ" > /dev/null || exit 2
git add -f "$TJ" "$TJ.sha256" && git commit -qm "essai : tâches jouet" || exit 2
N=$(PYTHONPATH=src "$PY" -m pytest --collect-only -q -p no:cacheprovider 2>/dev/null | sed -n 's/^\([0-9]*\) tests\{0,1\} collected.*/\1/p')
echo "tests collectés : $N"
echo 20261012 > "$R/entropie.txt"
TESTS_JOUET=$N "$PY" -I "$R/scripts/remplir_pilote_v1.py" . "$(git rev-parse HEAD)" jouet "$(date -u '+%Y-%m-%d %H:%M UTC')" "$R/entropie.txt" \
    "$P" "$CFG" --taches "$TJ" --rapports-etat "essai-etat=$(printf '0%.0s' {1..64})" \
    --rapports-relecture "essai-relecture=$(printf '0%.0s' {1..64})" > "$R/remplissage.json" || exit 2
PYTHONPATH=src "$PY" -m controle_ia.scellement sceller "$CFG" > /dev/null || exit 2
PYTHONPATH=src "$PY" -c "from controle_ia.prereg import sceller_prereg; sceller_prereg('$P')" || exit 2
git add "$P" "$P.sha256" "$CFG" "$CFG.sha256" && git commit -qm "essai : préenregistrement jouet du pilote" || exit 2
ESSAI=$(git rev-parse HEAD); echo "$ESSAI" > "$R/commit-essai.txt"
git clone -q --bare "$R/source" "$R/distant.git" || exit 2
cd "$R"
passage() {   # $1 nom, $2 BRANCHE, $3 environnement Python (défaut : l'environnement neuf existant)
    local n=$1 b=$2 venv=${3:-$VENV} debut fin code
    mkdir -p "$R/racine-$n"
    debut=$(date +%s)
    env -i PATH="/usr/bin:/bin" LANG=C.UTF-8 HOME="$R/racine-$n" COMMIT="$ESSAI" GH_TOKEN=factice HF_TOKEN=factice \
        ETUDE=pilote MODE=jouet DEPOT_URL="$R/distant.git" RACINE_AMORCE="$R/racine-$n" VENV_EXISTANT="$venv" \
        PREREG="$P" BRANCHE="$b" bash "$R/source/scripts/amorce_instance_t05.sh" > "$R/amorce-$n.log" 2>&1
    code=$?
    fin=$(date +%s)
    echo "passage $n : code $code ; durée totale $((fin - debut)) s"
    grep -h "^AMORCE" "$R/amorce-$n.log" 2>/dev/null | cut -c1-200 | sed 's/^/    | /'
    grep -h "tests :\|run :\|vecteurs\|arrêt\|ARRÊT\|poussée\|pip freeze\|format" "$R"/racine-"$n"/t05/journal.txt 2>/dev/null | cut -c1-200 | sed 's/^/    | /'
    # place disque (environ 770 Mo par clone) : les clones du passage partent, journaux et sorties restent
    rm -rf "$R/racine-$n/t05/controle-ia" "$R/racine-$n/amorce-depot"
}
passage 1-sain calcul/t05-pilote-jouet-a-v1
passage 2-artefact-branche-presente calcul/t05-pilote-jouet-a-v1
passage 3-premier-manque calcul/t05-pilote-jouet-b-v1 "$R/environnement-absent"
passage 4-relance calcul/t05-pilote-jouet-b-v2
git -C "$R/distant.git" branch -a | sed 's/^/branche distante : /'
# récupération du pilote (copies dont changent l'adresse du dépôt, le préfixe des branches et le motif du run jouets,
# le mode attendu « jouet », la carte non exigée et la ligne « disponible False »)
copie_recuperation() {   # $1 préfixe des branches jouets (a ou b), $2 sortie, $3 branche du premier lancement (option)
    sed -e "s|https://github.com/lciric/controle-ia-travail.git|$R/distant.git|" \
        -e "s|calcul/t05-pilote-reel-v|calcul/t05-pilote-jouet-$1-v|g" \
        -e "s|-t05-pilote-reel\\$|-t05-pilote-jouet\$|" -e 's|m\["config"\].get("mode") == "reel"|m["config"].get("mode") == "jouet"|' \
        -e 's|^CARTE_EXIGEE=oui|CARTE_EXIGEE=non|' -e 's|^COPIE_EXIGEE=oui|COPIE_EXIGEE=non|' -e 's|"disponible True"|"disponible False"|' \
        ${3:+-e "s|^PREMIERE=.*|PREMIERE=$3|"} "$R/scripts/recuperation_pilote_v1.sh" > "$2"
    echo "lignes changées dans la copie de la récupération ($2) : $(diff "$R/scripts/recuperation_pilote_v1.sh" "$2" | grep -c '^>')"
}
recuperer() {   # $1 nom, $2 copie, $3 mode (premier ou relance)
    local c
    env HF_TOKEN=factice-hf-0000 CONTROLE_IA_GITHUB_TOKEN=factice-gh-0000 GH_TOKEN=factice-gh-0000 VAST_API_KEY=factice-vast-0000 \
        bash "$2" "$ESSAI" "$R/recuperation-$1" ${3/premier/} > "$R/recuperation-$1.txt" 2>&1; c=$?
    echo "récupération ($1) : code $c ; $(tail -1 "$R/recuperation-$1.txt")"
    grep -E '^(KO|--)|^branche du premier' "$R/recuperation-$1.txt" | sed 's/^/    /'
    grep -h '^OK  6c' "$R/recuperation-$1.txt" | cut -c1-160 | sed 's/^/    /'
    rm -rf "$R/recuperation-$1" "$R/recuperation-$1.travail"
}
copie_recuperation a "$R/recuperation-a.sh"; copie_recuperation b "$R/recuperation-b.sh"
copie_recuperation b "$R/recuperation-artefact.sh" calcul/t05-pilote-jouet-a-v1
recuperer passage-1-premier "$R/recuperation-a.sh" premier
recuperer passage-4-relance "$R/recuperation-b.sh" relance
recuperer artefact-premier-avec-episodes "$R/recuperation-artefact.sh" relance
# artefact : branche c-v1 = a-v1 moins notations-3B-descriptives.json (commit d'auteur « instance de calcul (T0.5) ») :
# un seul KO attendu, 4c (VH-07)
git clone -q "$R/distant.git" "$R/clone-c" && git -C "$R/clone-c" checkout -q -b c calcul/t05-pilote-jouet-a-v1 2>/dev/null \
    || git -C "$R/clone-c" checkout -q -b c origin/calcul/t05-pilote-jouet-a-v1 || exit 2
NOT=$(git -C "$R/clone-c" ls-files 'diag/*/notations-3B-descriptives.json' | head -1)
[ -n "$NOT" ] || { echo "notations-3B-descriptives.json introuvable sur a-v1"; exit 2; }
git -C "$R/clone-c" rm -q "$NOT" "$NOT.sha256" && git -C "$R/clone-c" -c user.name="instance de calcul (T0.5)" -c user.email=instance@invalid \
    commit -qm "essai : notations retirées" && git -C "$R/clone-c" push -q origin c:refs/heads/calcul/t05-pilote-jouet-c-v1 || exit 2
rm -rf "$R/clone-c"
copie_recuperation c "$R/recuperation-c.sh"
recuperer artefact-notations-manquantes "$R/recuperation-c.sh" premier
rm -rf "$R/source" "$R/distant.git"
echo "FIN DE LA RÉPÉTITION"
