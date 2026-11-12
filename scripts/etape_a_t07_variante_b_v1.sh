#!/usr/bin/env bash
# Étape A de T0.7, VARIANTE B, sur une instance neuve (A100) — v1. Ordre d'exécution de l'étape A, brouillon 2
# (docs/procedures/ordre-execution-etape-a-t07-v1-brouillon2.md). Écrit sous $R/t07-etape-a-b-v1 seulement.
#
# Usage : etape_a_t07_variante_b_v1.sh S7 C7 RUN6 CONFIG BRANCHE BRANCHE_7B ATTENDU ECHEANCE_UTC_S
#   S7 : commit de scellement de T0.7 (descendant de C7, arbre gelé égal) ; C7 : commit du code ; RUN6 : run de 7b ;
#   CONFIG : configuration de T0.7 dans S7 ; BRANCHE : branche de sortie, neuve ; BRANCHE_7B : branche poussée par la course 7b ;
#   ATTENDU : dernière ligne attendue des essais de T0.7 (durée retirée) ; ECHEANCE_UTC_S : heure de destruction par la minuterie.
# Ordre des gestes (mère, R-2112 ; DF-01) : essais, CODE-T07 contrôlée, repli (garde d'ouverture, puis recalcul et garde
# d'équivalence), passe à blanc (CODE-T07 et mémoire de la notation comprises), étape A.
# Variables : GH_TOKEN (toujours), HF_TOKEN (réel), posées par la commande de création, par leur nom ; CONTAINER_ID et
# CONTAINER_API_KEY, posées par Vast. Aucune n'est jamais affichée.
# Essai local seulement (ESSAI_LOCAL=1) : RACINE_INSTANCE, DEPOT_URL (dépôt local), VENV_EXISTANT, ESSAIS_LISTE (liste réduite) ;
# aucune minuterie, aucun appel à Vast, aucun téléchargement de modèle, aucune carte exigée ; hors essai, ces variables sont refusées.
set -uo pipefail
[ "$#" = 8 ] || { echo "T07 REFUS : huit arguments attendus (S7 C7 RUN6 CONFIG BRANCHE BRANCHE_7B ATTENDU ECHEANCE_UTC_S)"; exit 2; }
S7="$1"; C7="$2"; RUN6="$3"; CONFIG="$4"; BR="$5"; BR7B="$6"; ATTENDU="$7"; ECH="$8"
ESSAI="${ESSAI_LOCAL:-0}"
DEPOT_OFFICIEL=https://github.com/lciric/controle-ia-travail.git
if [ "$ESSAI" = 1 ]; then R="${RACINE_INSTANCE:?RACINE_INSTANCE exigée en essai}"; URL="${DEPOT_URL:?DEPOT_URL exigée en essai}"
else
    for v in RACINE_INSTANCE DEPOT_URL VENV_EXISTANT ESSAIS_LISTE; do [ -z "${!v:-}" ] || { echo "T07 REFUS : $v n'est permise qu'en essai local"; exit 2; }; done
    R=/root; URL="$DEPOT_OFFICIEL"
fi
S6=935262b17ca95894a882b02f1526ee39d1738652
API=https://console.vast.ai/api/v0
T="$R/t07-etape-a-b-v1"; D="$T/depot"; X="$T/traces"; L="$X/journal-t07.txt"; XT=traces/t07-etape-a-b-v1
mkdir -p "$X" || { echo "T07 REFUS : $X impossible"; exit 2; }
export TZ=UTC PYTHONDONTWRITEBYTECODE=1                    # aucun __pycache__ sous src/ : CODE-T07 refuse un arbre de travail modifié
j() { printf '%s T07 %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$L"; }
BRANCHE_PRETE=0
fin_instance() {  # fin : réel, état voulu « stopped » demandé (la session détruit par l'identifiant, R10) ; essai : fichier, sortie
    if [ "$ESSAI" = 1 ]; then echo "fin $1" > "$T/fin-demandee"; exit "$1"; fi
    local c; c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X PUT -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
        -H 'Content-Type: application/json' -d '{"state": "stopped"}' "$API/instances/${CONTAINER_ID:-}/" 2>/dev/null) || c=000
    j "fin, code $1 ; état « stopped » demandé : HTTP $c ; la session détruit par l'identifiant"
    sleep infinity; exit "$1"; }
traces() { mkdir -p "$D/$XT" && cp -f "$X"/* "$D/$XT/"; }
arret() {  # arrêt motivé : traces poussées si la branche est prête, puis fin
    j "ARRET : $1"
    if [ "$BRANCHE_PRETE" = 1 ]; then traces && pousser "T0.7 (variante B) : traces de l'arrêt" "$XT" "registres/scellements-v1.md.ouvertures.md" || true; fi
    fin_instance "${2:-4}"; }
# 0. échéance et minuterie (réel) : destruction de l'instance par son identifiant à l'échéance, quoi qu'il arrive
case "$ECH" in ''|*[!0-9]*) arret "ECHEANCE_UTC_S illisible" 2;; esac
[ "$ECH" -gt "$(date +%s)" ] && [ "$ECH" -le $(( $(date +%s) + 86400 )) ] || arret "échéance $ECH hors de [maintenant, maintenant + 24 h]" 2
if [ "$ESSAI" != 1 ]; then
    case "${CONTAINER_ID:-}" in ''|*[!0-9]*) arret "identifiant de l'instance illisible : aucune minuterie possible" 2;; esac
    ( while [ "$(date +%s)" -lt "$ECH" ]; do sleep 30; done
      printf '%s T07 MINUTERIE : échéance atteinte : destruction de l'\''instance %s\n' "$(date -u +%FT%TZ)" "$CONTAINER_ID" >> "$L"
      for n in 1 2 3 4 5; do c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X DELETE -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
          "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000; case "$c" in 2??) exit 0;; esac; sleep 60; done ) < /dev/null > /dev/null 2>&1 &
    j "minuterie lancée (PID $!, échéance $(date -u -d "@$ECH" +%FT%TZ))"
else j "essai local : aucune minuterie, aucun appel à Vast"; fi
# 1. machine
for o in git curl python3 sha256sum awk sed grep; do command -v "$o" > /dev/null || arret "outil absent : $o" 2; done
[ -n "${GH_TOKEN:-}" ] || arret "GH_TOKEN absent (par le nom)" 2
if [ "$ESSAI" != 1 ]; then
    [ -n "${HF_TOKEN:-}" ] || arret "HF_TOKEN absent (par le nom)" 2
    nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv,noheader > "$X/nvidia-smi.txt" 2>&1 || arret "carte invisible (nvidia-smi)" 2
    j "carte : $(head -n 1 "$X/nvidia-smi.txt")"
fi
# 2. dépôt de T0.7 au commit S7 (seule branche main, clone partiel : aucun contenu n'est descendu sans être lu)
[ ! -e "$D" ] || arret "$D existe déjà (R12)" 2
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
git -c credential.helper="$AIDE" clone -q --filter=blob:none --no-checkout --single-branch --branch main "$URL" "$D" || arret "clonage" 2
git -C "$D" config credential.helper "$AIDE"; git -C "$D" config user.name "instance de calcul (T0.7)"; git -C "$D" config user.email "instance-calcul@invalid"
MOTIFS='/*
!/*/
/.claude/
/src/
/tests/
/scripts/
!/scripts/extraire_mesures_epreuve_t06_v1.py
/brouillons/T0.7-*
/docs/*
!/docs/*/
/docs/decisions/
/docs/notes/g0-deux-semaines-v1/
/docs/sources/invites-2606.08892-v1/
/prereg/*
!/prereg/contre-lectures/
/registres/*.md
/registres/go-extraits/
!/diag/*/lecture-sondes-t06.json*'
CITES=$(git -C "$D" show "$S7:$CONFIG" | python3 -I -c 'import json, sys
def f(x):
    if isinstance(x, dict):
        if isinstance(x.get("chemin"), str):
            yield x["chemin"]
        for v in x.values():
            yield from f(v)
    elif isinstance(x, list):
        for v in x:
            yield from f(v)
for p in sorted(set(f(json.load(sys.stdin)))):
    print("/" + p); print("/" + p + ".sha256")') || arret "configuration illisible dans S7" 2
git -C "$D" sparse-checkout init --no-cone && printf '%s\n%s\n' "$MOTIFS" "$CITES" | git -C "$D" sparse-checkout set --no-cone --stdin || arret "extraction partielle" 2
git -C "$D" checkout -q "$S7" || arret "commit S7 introuvable" 2
[ "$(git -C "$D" rev-parse HEAD)" = "$S7" ] || arret "tête ≠ S7" 2
git -C "$D" merge-base --is-ancestor "$C7" "$S7" || arret "C7 n'est pas ancêtre de S7" 2
git -C "$D" diff --quiet "$C7" "$S7" -- src tests || arret "arbre gelé changé entre C7 et S7" 2
H=$(git -C "$D" rev-parse origin/main); git -C "$D" merge-base --is-ancestor "$S7" "$H" || arret "S7 n'est pas ancêtre de main" 2
git -C "$D" cat-file -e "$S6^{commit}" 2>/dev/null && { git -C "$D" diff --quiet "$S6" "$S7" -- requirements-cpu.txt requirements-gpu.txt || j "exigences de paquets changées depuis la course 7b : installées telles que S7 les fixe (écrit)"; }
j "code conforme : S7 $S7, C7 $C7, main $H"
# 3. registres de main, fichiers qu'ils citent (dont les quatre lignes de jeux et de concepts) et journaux du script des jeux
interdit() { case "$1" in *lecture-sondes-t06*|donnees/bras-attaque*|donnees/mode-tenu-a-l-ecart*|docs/notes/bras-attaque/*|donnees/lecture-b-7a-quarantaine-v1*|scripts/extraire_mesures_epreuve_t06_v1.py) return 0;; esac; return 1; }
apporter() {  # $1 = révision, $2 = chemin : fichier et compagnon recopiés s'ils existent à cette révision ; un fichier suivi à S7 hors
    # de l'extraction partielle y est d'abord ajouté (sinon git le retirerait de l'arbre au changement de branche ; vu à la répétition)
    local q; interdit "$2" && arret "chemin interdit cité : $2" 2
    for q in "$2" "$2.sha256"; do git -C "$D" cat-file -e "$1:$q" 2>/dev/null || continue
        if git -C "$D" cat-file -e "HEAD:$q" 2>/dev/null && [ ! -e "$D/$q" ]; then
            git -C "$D" sparse-checkout add "/$q" 2>/dev/null || arret "extraction partielle de $q" 2; fi
        mkdir -p "$D/$(dirname "$q")" && git -C "$D" show "$1:$q" > "$D/$q" || arret "copie de $q" 2; done; }
for f in $(git -C "$D" ls-tree -r --name-only "$H" -- registres/ | grep -E '^registres/([^/]+\.md(\.sha256)?|go-extraits/[^/]+)$'); do
    mkdir -p "$D/$(dirname "$f")" && git -C "$D" show "$H:$f" > "$D/$f" || arret "registre $f" 2; done
for p in $(awk -F'|' 'NF >= 6 { gsub(/ /, "", $4); if ($4 ~ /^[A-Za-z0-9._\/-]+$/ && $4 !~ /\.\./) print $4 }' "$D/registres/scellements-v1.md" "$D/registres/prealables-p3bis-v1.md" 2>/dev/null | sort -u); do
    case "$p" in runs/"$RUN6"/*|diag/"$RUN6"/*|donnees/"$RUN6"/*) continue;; esac
    apporter "$H" "$p"; done
for k in SCELLEMENT-JEUX-T07-JD SCELLEMENT-JEUX-T07-JA SCELLEMENT-JEUX-T07-JC SCELLEMENT-CONCEPTS-T07; do
    p=$(grep "^| $k |" "$D/registres/scellements-v1.md" | awk -F'|' '{ gsub(/ /, "", $4); print $4 }'); [ -n "$p" ] || { j "$k : ligne absente"; continue; }
    [ -f "$D/$p" ] && [ -f "$D/$p.sha256" ] || arret "$k : $p ou son compagnon absent de main" 2
    [ "$k" = SCELLEMENT-CONCEPTS-T07 ] && { j "$k : $p présent"; continue; }
    for f in $(git -C "$D" ls-tree --name-only "$H" -- "$(dirname "$p")/" | grep -E '/journal-verification[^/]*\.txt(\.sha256)?$'); do
        git -C "$D" show "$H:$f" > "$D/$f" || arret "journal du script $f" 2; done
    j "$k : $p présent ; journaux du script : $(ls "$D/$(dirname "$p")" | grep -c '^journal-verification.*\.txt$')"
done
[ -z "$(git -C "$D" status --porcelain -- src tests)" ] || arret "src ou tests changés par la recopie des registres" 2
j "registres de main recopiés ; registre $(sha256sum < "$D/registres/scellements-v1.md" | cut -c1-16)"
# 4. sortie de la course 7b, par refspec explicite ; seuls les fichiers nommés sont extraits (jamais diag/<run>/ en entier :
#    lecture-sondes-t06.json n'est ni listé, ni extrait, ni descendu, le clone étant partiel)
git -C "$D" fetch -q origin "refs/heads/$BR7B:refs/remotes/origin/$BR7B" || arret "branche de 7b $BR7B introuvable" 2
B7="refs/remotes/origin/$BR7B"
for f in "runs/$RUN6/manifeste.json" "diag/$RUN6/episodes-t06.json" "diag/$RUN6/distillation-t06.json"; do
    git -C "$D" cat-file -e "$B7:$f" 2>/dev/null || arret "$f absent de la branche de 7b" 2; apporter "$B7" "$f"; done
git -C "$D" cat-file -e "$B7:diag/$RUN6/arret.json" 2>/dev/null && { apporter "$B7" "diag/$RUN6/arret.json"; j "arret.json de 7b présent : la garde de l'étape A le lira (A1)"; }
N7=0
for f in $(git -C "$D" ls-tree --name-only "$B7" -- "donnees/$RUN6/" | grep -E "^donnees/$RUN6/(adaptateur-[a-z]+\.pt|mesures-t06\.npz|textes-actions-t06\.jsonl|activations-sous-ensemble-t06-manifeste\.json|activations-sous-ensemble-t06-[0-9]{3}\.npz)$"); do
    apporter "$B7" "$f"; N7=$((N7 + 1)); done
[ "$N7" -ge 5 ] || arret "sortie de 7b incomplète ($N7 fichiers de données)" 2
[ ! -e "$D/diag/$RUN6/lecture-sondes-t06.json" ] || arret "lecture-sondes-t06.json présent dans l'arbre de T0.7 : embargo" 2
for p in $(python3 -I -c 'import json, sys
c = json.load(open(sys.argv[1], encoding="utf-8"))["config"]
def f(x):
    if isinstance(x, dict):
        for k, v in x.items():
            if isinstance(v, str) and (k == "chemin" or k.startswith("chemin_")):
                yield v
            yield from f(v)
    elif isinstance(x, list):
        for v in x:
            yield from f(v)
print("\n".join(sorted(set(f(c)))))' "$D/runs/$RUN6/manifeste.json"); do apporter "$H" "$p"; done
j "sortie de 7b extraite : manifeste, épisodes, distillation, $N7 fichiers de données ; fichiers cités par la configuration de 7b recopiés de main"
# 5. environnement et modèle
if [ "$ESSAI" = 1 ]; then PY="${VENV_EXISTANT:?VENV_EXISTANT exigée en essai}/bin/python"
else
    python3 -m venv "$T/venv" && timeout -k 10 3600 "$T/venv/bin/pip" install -q -r "$D/requirements-gpu.txt" > "$X/pip.txt" 2>&1 || arret "installation des paquets" 2
    PY="$T/venv/bin/python"
    "$PY" -c 'import torch, sys; sys.exit(0 if torch.cuda.is_available() else 1)' || arret "torch ne voit pas la carte (pilote ?)" 2
    (cd "$D" && PYTHONPATH=src timeout -k 10 3600 "$PY" -c 'import json, sys
from controle_ia.harnais.modeles import precharger_modele
a = json.load(open(sys.argv[1], encoding="utf-8"))["config"]["agent"]
print(precharger_modele(a["modele"], a["revision"]))' "runs/$RUN6/manifeste.json" > "$X/modele.txt" 2>&1) || arret "descente du modèle (HF_TOKEN, révision figée)" 2
fi
"$PY" -m pip freeze --all > "$X/pip-freeze.txt" 2>/dev/null
cd "$D" || arret "dépôt" 2
# 6. essais figés de T0.7 (aucun couperet de temps)
LISTE="tests/test_t07_*.py"; [ "$ESSAI" = 1 ] && [ -n "${ESSAIS_LISTE:-}" ] && LISTE="$ESSAIS_LISTE"
sha256sum $LISTE > "$X/essais-liste.txt"
PYTHONPATH=src "$PY" -m pytest -q -p no:cacheprovider --color=no $LISTE --basetemp="$T/essais-tmp" -o tmp_path_retention_policy=failed > "$X/essais.txt" 2> "$X/essais.err"; c=$?
DL=$(tail -n 1 "$X/essais.txt" | sed -E 's/ in [0-9.]+s.*$//'); j "essais : code $c, $DL"
[ "$c" = 0 ] && [ "$DL" = "$ATTENDU" ] || arret "essais de T0.7 : code $c, « $DL » attendu « $ATTENDU »" 2
E=$(PYTHONPATH=src "$PY" -m controle_ia.t07.lecture_v2 empreinte-config "$CONFIG") || arret "empreinte de la configuration" 2
j "configuration $CONFIG, empreinte canonique $E"
# 7. CODE-T07 (ordre : 1. CODE-T07 inscrite et contrôlée, 2. repli, 3. passe à blanc, 4. étape A)
PYTHONPATH=src "$PY" -m controle_ia.t07.code_t07_v1 verifier . registres/scellements-v1.md > "$X/code-t07.txt" 2>&1 || arret "CODE-T07 non conforme (code-t07.txt)" 2
j "$(head -n 1 "$X/code-t07.txt")"
# 8. branche neuve et poussées (chemins présents seulement, ajout explicite, jamais -A ; aucun fichier de plus de 90 Mo)
git ls-remote --exit-code origin "refs/heads/$BR" > /dev/null 2>&1; [ $? = 2 ] || arret "branche $BR présente sur le dépôt distant (R12) ou dépôt injoignable" 2
git checkout -q -b "$BR" || arret "branche locale" 2
gros() { [ "$#" -gt 0 ] && find "$@" -type f -size +90M 2>/dev/null | head -n 1; }
pousser() {
    local m="$1" x a=(); shift; for x in "$@"; do [ -e "$x" ] && a+=("$x"); done
    [ "${#a[@]}" -gt 0 ] || { j "rien à pousser (« $m »)"; return 0; }
    [ -z "$(gros "${a[@]}")" ] || { BRANCHE_PRETE=0; arret "fichier de plus de 90 Mo : $(gros "${a[@]}") (nœud)"; }
    git add --sparse -f -- "${a[@]}" && git commit -q -m "$m" || { BRANCHE_PRETE=0; arret "commit « $m »"; }
    local n; for n in 1 2 3; do git push -q origin "HEAD:refs/heads/$BR" && { j "poussé : $(git rev-parse HEAD) « $m »"; return 0; }; sleep $((20 * n)); done
    BRANCHE_PRETE=0; arret "poussée « $m » impossible"; }
BRANCHE_PRETE=1
# 9. repli : garde d'ouverture de l'étape A (journalisée) PUIS recalcul sous un nom daté et garde d'équivalence (DF-01) ;
#    R11 : une relance sur la même carte, sous un nom daté neuf (le premier recalcul reste) ; refus de la garde : arrêt (attente)
RAPPORT="donnees/$RUN6/activations/rapport-repli-t07.json"
for essai in 1 2; do
    PYTHONPATH=src "$PY" -m controle_ia.t07.lecture_v2 repli-seul . "$RUN6" "$CONFIG" > "$X/repli-$essai.txt" 2> "$X/repli-$essai.err"; c=$?
    j "repli, essai $essai : code $c ; $(head -n 1 "$X/repli-$essai.txt")"
    [ "$c" = 0 ] && break
    [ "$c" = 3 ] && [ "$essai" = 1 ] && { j "garde d'équivalence ou identité en échec (R11) : une relance, même carte, même commit, nom neuf"; continue; }
    traces; pousser "T0.7 (variante B) : repli en arrêt, code $c (essai $essai)" registres/scellements-v1.md.ouvertures.md "$XT"
    arret "repli : code $c (essai $essai) : $( [ "$c" = 2 ] && echo 'refus de la garde (ligne manquante : attente, relance sur une instance neuve)' || echo 'nœud') (motif : repli-$essai.err)" 3
done
[ -f "$RAPPORT" ] || arret "rapport du repli introuvable ($RAPPORT)" 3
traces; pousser "T0.7 (variante B) : garde d'ouverture, repli du recalcul, garde d'équivalence passée" "$RAPPORT" "$RAPPORT.sha256" registres/scellements-v1.md.ouvertures.md "$XT"
# 10. passe à blanc (aucune donnée décisive)
PYTHONPATH=src "$PY" -m controle_ia.t07.lecture_v2 passe-blanc . "$RUN6" "$CONFIG" > "$X/passe-blanc.txt" 2> "$X/passe-blanc.err"; c=$?
j "passe à blanc : code $c ; $(head -n 1 "$X/passe-blanc.txt")"
traces; pousser "T0.7 (variante B) : passe à blanc de l'extracteur (aucune donnée décisive), code $c" passes-blanches-t07 "$XT"
[ "$c" = 0 ] || arret "passe à blanc : code $c : l'étape A ne part pas (motif : passe-blanc.err)" 3
# 11. étape A après le repli (garde d'identité remplacée par la garde d'équivalence)
PYTHONPATH=src "$PY" -m controle_ia.t07.lecture_v2 etape-a-apres-repli . "$RUN6" "$CONFIG" > "$X/etape-a.txt" 2> "$X/etape-a.err"; c=$?
RUN7=$(ls -1 runs 2>/dev/null | grep -- '-t07-lecture-' | sort | tail -n 1); j "étape A : code $c${RUN7:+, run $RUN7}"
CH=(registres/scellements-v1.md registres/scellements-v1.md.ouvertures.md "$XT")
[ -n "$RUN7" ] && CH+=("runs/$RUN7" "diag/$RUN7" "donnees/$RUN7")
traces; pousser "T0.7 (variante B), étape A : sorties scellées, code $c${RUN7:+, run $RUN7}" "${CH[@]}"
[ "$c" = 0 ] || arret "étape A : code $c : nœud, aucune relance sous ce texte (motif : etape-a.err)" 3
[ ! -e "$D/diag/$RUN6/lecture-sondes-t06.json" ] || arret "lecture-sondes-t06.json présent : embargo" 3
j "FIN : étape A menée au bout, run $RUN7, tête $(git rev-parse HEAD)"
fin_instance 0
