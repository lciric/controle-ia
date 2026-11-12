#!/usr/bin/env bash
# Scellement du préenregistrement du pilote de T0.5 (plan de lancement du pilote, étape 1), sur le modèle du scellement
# v5 de la revalidation et des constats de l'état des lieux (PL-09) : HEAD = origin/main, arbre suivi propre, sorties
# absentes (R12) ; scripts égaux à leurs copies versées ; candidat relu égal à son épingle, brute et normalisée ;
# entropie tirée ici par numpy.random.SeedSequence (R9), écrite une seule fois ; texte régénéré par le générateur en mode
# reel, normalisé égal à l'épingle ; configuration et préenregistrement scellés ; verifier-arbre ; un seul commit S qui
# n'ajoute que ces quatre fichiers, poussé, puis relu sur le dépôt distant. Un échec avant le commit retire les fichiers
# créés ici (et seulement eux) : aucun reste non suivi. Le dossier de travail (entropie tirée, texte, configuration) est
# retiré dans tous les cas ; tout arrêt sort en code 2 ; les lignes ÉCHEC de verifier-arbre sont affichées (CH-08).
# Tous les scripts de la chaîne (liste CHAINE, plan de lancement v2) doivent être égaux à leurs copies versées (CH-12).
# Décision de Lazar sur N-019 (relecture R2, NO-03) : son GO et la ligne R-… qui le consigne sont passés au générateur,
# qui les vérifie dans les registres de HEAD et les cite dans le texte (masqués par la normalisation).
# Usage : sceller_pilote_v1.sh GO-AAAA-MM-JJ-NN R-NNN
set -euo pipefail
trap 'echo "arrêt du scellement (ligne $LINENO)"; exit 2' ERR   # tout arrêt sous set -e : code 2, même avant le piège de sortie (VH-04 ; UH-07)
[ $# -eq 2 ] && [[ "$1" =~ ^GO-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}$ ]] && [[ "$2" =~ ^R-[0-9]{3,4}$ ]] \
    || { echo "usage : sceller_pilote_v1.sh GO-AAAA-MM-JJ-NN R-NNN (décision de Lazar sur N-019)"; exit 2; }
GO=$1; REG=$2
H=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/pilote-v1
DEPOT=/home/user/controle-ia-travail
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
VERSEES=docs/procedures/pilote-T0.5-v1
P=prereg/T0.5-pilote-8B-v1.md; CFG=prereg/T0.5-pilote-config-v1.json
TACHES=donnees/t05-pilote-v1/taches-pilote-60-v1.json
CTL=$H/controles_avant_depense_pilote_v1.sh
epingle() { sed -n "s/^$1=\"\{0,1\}\([^\"#]*\)\"\{0,1\}.*/\1/p" "$CTL" | sed 's/[[:space:]]*$//'; }
RELU=$(epingle CANDIDAT_RELU_CHEMIN); RELU_SHA=$(epingle CANDIDAT_RELU); NORMALISE=$(epingle CANDIDAT_NORMALISE)
RAPPORTS=$(epingle RAPPORTS_ATTENDUS)
[[ "$RELU_SHA" =~ ^[0-9a-f]{64}$ && "$NORMALISE" =~ ^[0-9a-f]{64}$ && "$RELU" == brouillons/* && -n "$RAPPORTS" && "$RAPPORTS" != A_EPINGLER ]] \
    || { echo "épingles absentes des contrôles"; exit 2; }
ETAT=$(for x in $RAPPORTS; do case $x in *etat-des-lieux*) printf '%s,' "$x" ;; esac; done); ETAT=${ETAT%,}
REL=$(for x in $RAPPORTS; do case $x in *relecture-b8*) printf '%s,' "$x" ;; esac; done); REL=${REL%,}
[ -n "$ETAT" ] && [ -n "$REL" ] || { echo "rapports de l'état des lieux ou de la relecture absents des épingles"; exit 2; }
# toute paire d'une autre famille est refusée ici, non après le scellement (vérification courte, VH-09)
for x in $RAPPORTS; do case $x in T0.5-pilote-v1-etat-des-lieux-*=*|T0.5-pilote-v1-relecture-b8-*=*) ;;
    *) echo "rapport épinglé hors des deux familles (état des lieux, relecture-b8) : ${x%%=*}"; exit 2 ;; esac; done
# aucune épingle restée « A_EPINGLER » ; code relu et journal de la répétition jouet lus ici, avant l'entropie (VH-01)
grep -q "A_EPINGLER" "$CTL" && { echo "épingle restée « A_EPINGLER » dans les contrôles"; exit 2; }
CODE_RELU=$(epingle CODE_RELU); REPETITION=$(epingle REPETITION_JOUET); REPETITION_CHEMIN=$(epingle REPETITION_JOUET_CHEMIN)
[[ "$CODE_RELU" =~ ^[0-9a-f]{40}$ && "$REPETITION" =~ ^[0-9a-f]{64}$ && "$REPETITION_CHEMIN" == "$VERSEES"/* ]] \
    || { echo "code relu ou répétition jouet non épinglés"; exit 2; }
cd "$DEPOT"
git fetch -q origin main
[ "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)" ] || { echo "HEAD ≠ origin/main : pousser d'abord les préalables"; exit 2; }
[ -z "$(git status --porcelain --untracked-files=no)" ] || { echo "arbre suivi non propre"; exit 2; }
for f in "$P" "$P.sha256" "$CFG" "$CFG.sha256"; do [ -e "$f" ] && { echo "$f existe déjà (R12)"; exit 2; }; done
CHAINE="deriver_taches_pilote_v1.py remplir_pilote_v1.py normaliser_pilote_v1.py controles_avant_depense_pilote_v1.sh
        lancer_pilote_v1.sh sceller_pilote_v1.sh recuperation_pilote_v1.sh repetition_jouet_pilote_v1.sh
        repetition_finale_pilote_v1.sh essais_lanceur_pilote_v1.sh essais_controles_pilote_v1.sh
        essais_generateur_pilote_v1.sh essais_scellement_pilote_v1.sh"
# copies versées et journal de la répétition suivis à HEAD : l'arbre suivi étant propre, le disque est alors égal à HEAD
# (vérification courte, VH-01, reste : un fichier présent mais non suivi passerait cmp et verifier-arbre)
for f in $(for s in $CHAINE; do printf '%s/%s %s/%s.sha256\n' "$VERSEES" "$s" "$VERSEES" "$s"; done) "$REPETITION_CHEMIN" "$REPETITION_CHEMIN.sha256"; do
    git ls-files --error-unmatch -- "$f" > /dev/null 2>&1 || { echo "$f non suivi à HEAD"; exit 2; }
done
for s in $CHAINE; do
    cmp -s "$H/$s" "$VERSEES/$s" || { echo "$s du bloc-notes ≠ copie versée"; exit 2; }
done
[ "$(sha256sum "$RELU" | cut -d' ' -f1)" = "$RELU_SHA" ] || { echo "candidat relu ≠ épingle brute"; exit 2; }
GELES=$(PYTHONPATH=src "$PY" -I -c "import sys; sys.path.insert(0, 'src'); from controle_ia.harnais.validation_reelle import CHEMINS_GELES; print(' '.join(CHEMINS_GELES))")
[ -n "$GELES" ] || { echo "CHEMINS_GELES illisible"; exit 2; }
# shellcheck disable=SC2086
git diff --quiet "$CODE_RELU" HEAD -- $GELES || { echo "arbre gelé de HEAD ≠ code relu épinglé ($CODE_RELU)"; exit 2; }
# deux gardes, deux messages : empreinte, puis commit du code répété (vérification c3, UH-02)
[ "$(sha256sum "$REPETITION_CHEMIN" | cut -d' ' -f1)" = "$REPETITION" ] && [ "$(cut -d' ' -f1 "$REPETITION_CHEMIN.sha256")" = "$REPETITION" ] \
    || { echo "journal de la répétition jouet absent ou d'une autre empreinte que l'épingle"; exit 2; }
grep -qxF "commit du code répété : $CODE_RELU" "$REPETITION_CHEMIN" \
    || { echo "journal de la répétition jouet d'un autre commit que le code relu"; exit 2; }
[ "$("$PY" -I "$H/normaliser_pilote_v1.py" "$RELU")" = "$NORMALISE" ] || { echo "candidat relu : normalisé ≠ épingle"; exit 2; }
COMMITTE=0; TRAVAIL=""
fin() {
    local code=$?
    if [ "$code" != 0 ] && [ "$COMMITTE" = 0 ]; then
        # un commit refusé après git add laisse les fichiers dans l'index : les en retirer d'abord (vérification c3, UH-14)
        git reset -q -- "$P" "$P.sha256" "$CFG" "$CFG.sha256" > /dev/null 2>&1 || true
        for f in "$P" "$P.sha256" "$CFG" "$CFG.sha256"; do git ls-files --error-unmatch "$f" >/dev/null 2>&1 || rm -f "$f"; done
        echo "échec avant le commit : fichiers créés retirés"
    fi
    [ -n "$TRAVAIL" ] && rm -rf "$TRAVAIL"           # entropie tirée, texte, configuration : jamais laissés (CH-08)
    [ "$code" = 0 ] || exit 2
}
trap fin EXIT
TRAVAIL=$(mktemp -d "$H/scellement-XXXX")
"$PY" -I -c "import numpy as np; print(np.random.SeedSequence().entropy)" > "$TRAVAIL/entropie.txt"
"$PY" -I "$H/remplir_pilote_v1.py" . "$(git rev-parse HEAD)" reel "$(date -u '+%Y-%m-%d %H:%M UTC')" "$TRAVAIL/entropie.txt" \
    "$TRAVAIL/prereg.md" "$TRAVAIL/config.json" --taches "$TACHES" --rapports-etat "$ETAT" --rapports-relecture "$REL" \
    --candidat-relu "$RELU" --go "$GO" --registre "$REG"
[ "$("$PY" -I "$H/normaliser_pilote_v1.py" "$TRAVAIL/prereg.md")" = "$NORMALISE" ] || { echo "texte régénéré ≠ candidat relu normalisé"; exit 2; }
cp "$TRAVAIL/config.json" "$CFG"; cp "$TRAVAIL/prereg.md" "$P"
PYTHONPATH=src "$PY" -m controle_ia.scellement sceller "$CFG" > /dev/null
PYTHONPATH=src "$PY" -c "from controle_ia.prereg import sceller_prereg; sceller_prereg('$P')"
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier-arbre . > "$TRAVAIL/verifier-arbre.txt" 2>&1 \
    || { grep '^ÉCHEC' "$TRAVAIL/verifier-arbre.txt" || tail -3 "$TRAVAIL/verifier-arbre.txt"; echo "verifier-arbre en échec"; exit 2; }
tail -1 "$TRAVAIL/verifier-arbre.txt" | grep -qx "arbre intact" || { echo "verifier-arbre : dernière ligne inattendue"; exit 2; }
SHA=$(cut -d' ' -f1 "$P.sha256")
git add "$P" "$P.sha256" "$CFG" "$CFG.sha256"
git commit -q -F - <<EOF
T0.5 : pilote 8B, préenregistrement v1 scellé (60 tâches, N-019 ; noyau « defaut », duree_max_s 15 000 s)

Préenregistrement $SHA ; configuration $(cut -d' ' -f1 "$CFG.sha256") ; empreinte normalisée égale au candidat
relu ($NORMALISE). Décision de Lazar sur N-019 : $GO ($REG). PREREG et BRANCHE passés à l'instance
(calcul/t05-pilote-reel-v1).

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01W5L3BRJg9Vso4Gru9tWAzM
EOF
COMMITTE=1
S=$(git rev-parse HEAD)
[ "$(git diff --name-only "$S^" "$S" | sort | tr '\n' ' ')" = "$(printf '%s\n' "$CFG" "$CFG.sha256" "$P" "$P.sha256" | sort | tr '\n' ' ')" ] \
    || { echo "contenu de S inattendu"; exit 2; }
timeout 600 git push -q origin HEAD:main || { echo "poussée de S en échec : S reste local ; repousser avant tout lancement"; exit 2; }
git fetch -q origin main
[ "$(git rev-parse origin/main)" = "$S" ] || { echo "origin/main ≠ S après la poussée"; exit 2; }
echo "S $S poussé ; préenregistrement $SHA"
