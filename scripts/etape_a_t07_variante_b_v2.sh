#!/usr/bin/env bash
# Étape A de T0.7, VARIANTE B, sur une instance neuve (A100) — v2. Ordre d'exécution de l'étape A, brouillon 4
# (docs/procedures/ordre-execution-etape-a-t07-v1-brouillon4.md). Écrit sous $R/t07-etape-a-b-v1 seulement.
# v2 = v1 (99e4c926…) + la contre-lecture courte v3 (d0fe9053…) : O-1 essais joués AVANT la descente du modèle, et mode de
# mesure de la ligne d'essais (ARRET_APRES_ESSAIS, essai local) ; O-2 taille des sorties de l'étape A estimée et bornée avant
# toute ouverture, puis tout fichier de plus de SEUIL octets découpé en morceaux scellés (manifeste scellé, recomposition
# vérifiée) : légers poussés d'abord, morceaux ensuite par lots ; O-3 chaque DELETE de la minuterie journalisé (code HTTP) ;
# la minuterie, sous-processus du conteneur, meurt avec lui dès l'état « stopped » ; O-5 registres nommés seulement, jamais
# registres/index-bras-attaque* ; C-1 périmètre des jeux exigé en argument, contrôlé avant toute ouverture ; journaux du script
# des jeux recopiés comme les autres fichiers cités (extraction partielle comprise) ; O-6 en-tête.
#
# Usage : etape_a_t07_variante_b_v2.sh S7 C7 RUN6 CONFIG BRANCHE BRANCHE_7B ATTENDU ECHEANCE_UTC_S PERIMETRE
#   S7 : commit de scellement de T0.7 (descendant de C7, arbre gelé égal) ; C7 : commit du code ; RUN6 : run de 7b ;
#   CONFIG : configuration de T0.7 dans S7 ; BRANCHE : branche de sortie, neuve ; BRANCHE_7B : branche poussée par la course 7b ;
#   ATTENDU : dernière ligne attendue des essais de T0.7 (durée retirée ; « - » en mesure seulement) ; ECHEANCE_UTC_S : heure de
#   destruction par la minuterie ; PERIMETRE : lignes de scellement exigées à main, ni plus ni moins (C-1), parmi JD, JA, JC,
#   CONCEPTS, séparées par des virgules, ou « aucun ».
# Ordre des gestes (mère, R-2112 ; DF-01) : essais, taille bornée, modèle, CODE-T07 contrôlée, repli (garde d'ouverture, puis
# recalcul et garde d'équivalence), passe à blanc (CODE-T07 et mémoire de la notation comprises), étape A.
# Variables : GH_TOKEN (toujours), HF_TOKEN (réel), posées par la commande de création, par leur nom ; CONTAINER_ID et
# CONTAINER_API_KEY, posées par Vast. Aucune n'est jamais affichée.
# Essai local seulement (ESSAI_LOCAL=1) : RACINE_INSTANCE, DEPOT_URL (dépôt local), VENV_EXISTANT, ESSAIS_LISTE (liste réduite),
# ARRET_APRES_ESSAIS (mesure de la ligne d'essais, fin après eux), API_ESSAI (serveur local qui tient lieu de l'API de Vast pour
# la minuterie et la fin), MINUTERIE_PAUSE_S, SEUIL_ESSAI, MORCEAU_ESSAI, LOT_ESSAI, BORNE_ESSAI ; aucun modèle descendu, aucune
# carte exigée ; hors essai, ces variables sont refusées.
set -uo pipefail
[ "$#" = 9 ] || { echo "T07 REFUS : neuf arguments attendus (S7 C7 RUN6 CONFIG BRANCHE BRANCHE_7B ATTENDU ECHEANCE_UTC_S PERIMETRE)"; exit 2; }
S7="$1"; C7="$2"; RUN6="$3"; CONFIG="$4"; BR="$5"; BR7B="$6"; ATTENDU="$7"; ECH="$8"; PERIM="$9"
ESSAI="${ESSAI_LOCAL:-0}"
DEPOT_OFFICIEL=https://github.com/lciric/controle-ia-travail.git
VARS_ESSAI="RACINE_INSTANCE DEPOT_URL VENV_EXISTANT ESSAIS_LISTE ARRET_APRES_ESSAIS API_ESSAI MINUTERIE_PAUSE_S SEUIL_ESSAI MORCEAU_ESSAI LOT_ESSAI BORNE_ESSAI"
if [ "$ESSAI" = 1 ]; then R="${RACINE_INSTANCE:?RACINE_INSTANCE exigée en essai}"; URL="${DEPOT_URL:?DEPOT_URL exigée en essai}"
else
    for v in $VARS_ESSAI; do [ -z "${!v:-}" ] || { echo "T07 REFUS : $v n'est permise qu'en essai local"; exit 2; }; done
    R=/root; URL="$DEPOT_OFFICIEL"
fi
MESURE="${ARRET_APRES_ESSAIS:-0}"
S6=935262b17ca95894a882b02f1526ee39d1738652
API=https://console.vast.ai/api/v0; [ "$ESSAI" = 1 ] && [ -n "${API_ESSAI:-}" ] && API="$API_ESSAI"
SEUIL="${SEUIL_ESSAI:-90000000}"; MORCEAU="${MORCEAU_ESSAI:-50000000}"; LOT="${LOT_ESSAI:-10}"; BORNE="${BORNE_ESSAI:-2000000000}"
T="$R/t07-etape-a-b-v1"; D="$T/depot"; X="$T/traces"; L="$X/journal-t07.txt"; XT=traces/t07-etape-a-b-v1
mkdir -p "$X" || { echo "T07 REFUS : $X impossible"; exit 2; }
export TZ=UTC PYTHONDONTWRITEBYTECODE=1                    # aucun __pycache__ sous src/ : CODE-T07 refuse un arbre de travail modifié
j() { printf '%s T07 %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$L"; }
BRANCHE_PRETE=0; MPID=""
arreter_minuterie_essai() { [ "$ESSAI" = 1 ] && [ -n "$MPID" ] && kill "$MPID" 2>/dev/null && j "essai local : minuterie arrêtée par son PID ($MPID)"; return 0; }
fin_instance() {  # fin : état « stopped » demandé (la minuterie meurt avec le conteneur, O-3 ; la session détruit par l'identifiant,
    # R10) ; essai sans API_ESSAI : fichier, sortie ; essai avec API_ESSAI : la demande va au serveur local, puis fichier, sortie
    local c
    if [ "$ESSAI" = 1 ] && [ -z "${API_ESSAI:-}" ]; then arreter_minuterie_essai; echo "fin $1" > "$T/fin-demandee"; exit "$1"; fi
    c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X PUT -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
        -H 'Content-Type: application/json' -d '{"state": "stopped"}' "$API/instances/${CONTAINER_ID:-}/" 2>/dev/null) || c=000
    j "fin, code $1 ; état « stopped » demandé : HTTP $c ; la minuterie meurt avec le conteneur : la session détruit par l'identifiant"
    if [ "$ESSAI" = 1 ]; then arreter_minuterie_essai; echo "fin $1" > "$T/fin-demandee"; exit "$1"; fi
    sleep infinity; exit "$1"; }
traces() { mkdir -p "$D/$XT" && cp -f "$X"/* "$D/$XT/"; }
arret() {  # arrêt motivé : traces poussées si la branche est prête, puis fin
    j "ARRET : $1"
    if [ "$BRANCHE_PRETE" = 1 ]; then traces && pousser "T0.7 (variante B) : traces de l'arrêt" "$XT" "registres/scellements-v1.md.ouvertures.md" || true; fi
    fin_instance "${2:-4}"; }
# 0. arguments, échéance et minuterie (réel ; essai seulement avec API_ESSAI) : destruction de l'instance par son identifiant à
#    l'échéance, tant que le conteneur vit ; chaque DELETE journalisé avec son code HTTP (jamais la clé)
case "$ECH" in ''|*[!0-9]*) arret "ECHEANCE_UTC_S illisible" 2;; esac
[ "$ECH" -gt "$(date +%s)" ] && [ "$ECH" -le $(( $(date +%s) + 86400 )) ] || arret "échéance $ECH hors de [maintenant, maintenant + 24 h]" 2
for v in SEUIL MORCEAU LOT BORNE; do case "${!v}" in ''|*[!0-9]*|0) arret "$v illisible" 2;; esac; done
[ "$MORCEAU" -le "$SEUIL" ] || arret "MORCEAU ($MORCEAU) > SEUIL ($SEUIL)" 2
case "$PERIM" in aucun) PER=",";; *) PER=",$PERIM,"; for k in ${PERIM//,/ }; do case "$k" in JD|JA|JC|CONCEPTS) ;; *) arret "PERIMETRE : élément $k inconnu (JD, JA, JC, CONCEPTS ou « aucun »)" 2;; esac; done;; esac
if [ "$ATTENDU" = - ] && [ "$MESURE" != 1 ]; then arret "ATTENDU « - » permis en mesure seulement" 2; fi
if [ "$MESURE" = 1 ] && [ "$ESSAI" != 1 ]; then arret "ARRET_APRES_ESSAIS en essai local seulement" 2; fi
if [ "$ESSAI" != 1 ] || [ -n "${API_ESSAI:-}" ]; then
    case "${CONTAINER_ID:-}" in ''|*[!0-9]*) arret "identifiant de l'instance illisible : aucune minuterie possible" 2;; esac
    PAUSE_MIN=60; ATTENTE=30; [ "$ESSAI" = 1 ] && { PAUSE_MIN="${MINUTERIE_PAUSE_S:-2}"; ATTENTE=1; }
    minuterie() {
        local n c
        while [ "$(date +%s)" -lt "$ECH" ]; do sleep "$ATTENTE"; done
        j "MINUTERIE : échéance atteinte : destruction de l'instance $CONTAINER_ID par son identifiant (DELETE)"
        for n in 1 2 3 4 5; do
            c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X DELETE -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
                "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000
            j "MINUTERIE : DELETE, essai $n : HTTP $c"
            case "$c" in 2??) return 0;; esac; sleep "$PAUSE_MIN"; done
        j "MINUTERIE : cinq DELETE sans succès : destruction laissée à la session (R10)"; }
    minuterie < /dev/null &
    MPID=$!
    j "minuterie lancée (PID $MPID, échéance $(date -u -d "@$ECH" +%FT%TZ)) ; elle meurt avec le conteneur à l'état « stopped »"
else j "essai local : aucune minuterie, aucun appel à Vast"; fi
# 1. machine
for o in git curl python3 sha256sum awk sed grep split stat find sort; do command -v "$o" > /dev/null || arret "outil absent : $o" 2; done
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
# registres/go.md : lu par la garde (extrait d'une ligne GO-*, registre_v1.verifier_lignes) ; nommé ici (reprise, R-2166 : la v1
# le recopiait avec tous les registres/*.md, la première forme de la v2 l'avait perdu)
REGISTRES="registres/scellements-v1.md registres/scellements-v1.md.ouvertures.md registres/ouvertures-p3bis-v1.md registres/prealables-p3bis-v1.md registres/go.md"
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
!/diag/*/lecture-sondes-t06.json*'
NOMMES=$(for f in $REGISTRES; do printf '/%s\n/%s.sha256\n' "$f" "$f"; done)
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
git -C "$D" sparse-checkout init --no-cone && printf '%s\n%s\n%s\n' "$MOTIFS" "$NOMMES" "$CITES" | git -C "$D" sparse-checkout set --no-cone --stdin || arret "extraction partielle" 2
git -C "$D" checkout -q "$S7" || arret "commit S7 introuvable" 2
[ "$(git -C "$D" rev-parse HEAD)" = "$S7" ] || arret "tête ≠ S7" 2
git -C "$D" merge-base --is-ancestor "$C7" "$S7" || arret "C7 n'est pas ancêtre de S7" 2
git -C "$D" diff --quiet "$C7" "$S7" -- src tests || arret "arbre gelé changé entre C7 et S7" 2
H=$(git -C "$D" rev-parse origin/main); git -C "$D" merge-base --is-ancestor "$S7" "$H" || arret "S7 n'est pas ancêtre de main" 2
git -C "$D" cat-file -e "$S6^{commit}" 2>/dev/null && { git -C "$D" diff --quiet "$S6" "$S7" -- requirements-cpu.txt requirements-gpu.txt || j "exigences de paquets changées depuis la course 7b : installées telles que S7 les fixe (écrit)"; }
j "code conforme : S7 $S7, C7 $C7, main $H"
# 3. registres NOMMÉS de main (O-5), fichiers qu'ils citent, périmètre des jeux (C-1) et journaux du script des jeux
interdit() { case "$1" in *lecture-sondes-t06*|donnees/bras-attaque*|donnees/mode-tenu-a-l-ecart*|docs/notes/bras-attaque/*|donnees/lecture-b-7a-quarantaine-v1*|scripts/extraire_mesures_epreuve_t06_v1.py|registres/index-bras-attaque*) return 0;; esac; return 1; }
apporter() {  # $1 = révision, $2 = chemin : fichier et compagnon recopiés s'ils existent à cette révision ; un fichier suivi à S7 hors
    # de l'extraction partielle y est d'abord ajouté (sinon git le retirerait de l'arbre au changement de branche ; vu à la répétition)
    local q; interdit "$2" && arret "chemin interdit cité : $2" 2
    for q in "$2" "$2.sha256"; do git -C "$D" cat-file -e "$1:$q" 2>/dev/null || continue
        if git -C "$D" cat-file -e "HEAD:$q" 2>/dev/null && [ ! -e "$D/$q" ]; then
            git -C "$D" sparse-checkout add "/$q" 2>/dev/null || arret "extraction partielle de $q" 2; fi
        mkdir -p "$D/$(dirname "$q")" && git -C "$D" show "$1:$q" > "$D/$q" || arret "copie de $q" 2; done; }
for f in $REGISTRES; do
    if git -C "$D" cat-file -e "$H:$f" 2>/dev/null; then apporter "$H" "$f"; j "registre $f recopié de main"; else j "registre $f : absent de main"; fi; done
[ -f "$D/registres/scellements-v1.md" ] || arret "registres/scellements-v1.md absent de main" 2
for p in $(awk -F'|' 'NF >= 6 { gsub(/ /, "", $4); if ($4 ~ /^[A-Za-z0-9._\/-]+$/ && $4 !~ /\.\./) print $4 }' "$D/registres/scellements-v1.md" "$D/registres/prealables-p3bis-v1.md" 2>/dev/null | sort -u); do
    case "$p" in runs/"$RUN6"/*|diag/"$RUN6"/*|donnees/"$RUN6"/*) continue;; esac
    apporter "$H" "$p"; done
for k in JD JA JC CONCEPTS; do   # C-1 : la première ouverture ferme le périmètre des jeux ; ni plus ni moins que PERIMETRE
    case "$k" in CONCEPTS) cle=SCELLEMENT-CONCEPTS-T07;; *) cle=SCELLEMENT-JEUX-T07-$k;; esac
    n=$(grep -c "^| $cle |" "$D/registres/scellements-v1.md"); case "$PER" in *",$k,"*) e=1;; *) e=0;; esac
    [ "$n" -le 1 ] || arret "$cle : $n lignes au registre (au plus une)" 2
    [ "$n" = "$e" ] || arret "périmètre (C-1) : $cle $([ "$n" = 1 ] && echo présente || echo absente) à main, $([ "$e" = 1 ] && echo exigée || echo non exigée) par PERIMETRE=$PERIM : rien n'est ouvert" 2
    [ "$n" = 1 ] || { j "$cle : absente, hors du périmètre"; continue; }
    p=$(grep "^| $cle |" "$D/registres/scellements-v1.md" | awk -F'|' '{ gsub(/ /, "", $4); print $4 }')
    [ -f "$D/$p" ] && [ -f "$D/$p.sha256" ] || arret "$cle : $p ou son compagnon absent de main" 2
    [ "$k" = CONCEPTS ] && { j "$cle : $p présent"; continue; }
    for f in $(git -C "$D" ls-tree --name-only "$H" -- "$(dirname "$p")/" | grep -E '/journal-verification[^/]*\.txt$'); do apporter "$H" "$f"; done
    j "$cle : $p présent ; journaux du script : $(ls "$D/$(dirname "$p")" | grep -c '^journal-verification.*\.txt$')"
done
[ -z "$(git -C "$D" status --porcelain -- src tests)" ] || arret "src ou tests changés par la recopie des registres" 2
j "registres nommés de main recopiés ; registre $(sha256sum < "$D/registres/scellements-v1.md" | cut -c1-16) ; périmètre $PERIM"
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
# 5. environnement : paquets, carte vue par torch (le modèle descend APRÈS les essais et la borne de taille, O-1)
if [ "$ESSAI" = 1 ]; then PY="${VENV_EXISTANT:?VENV_EXISTANT exigée en essai}/bin/python"
else
    python3 -m venv "$T/venv" && timeout -k 10 3600 "$T/venv/bin/pip" install -q -r "$D/requirements-gpu.txt" > "$X/pip.txt" 2>&1 || arret "installation des paquets" 2
    PY="$T/venv/bin/python"
    "$PY" -c 'import torch, sys; sys.exit(0 if torch.cuda.is_available() else 1)' || arret "torch ne voit pas la carte (pilote ?)" 2
fi
"$PY" -m pip freeze --all > "$X/pip-freeze.txt" 2>/dev/null
cd "$D" || arret "dépôt" 2
# 6. essais figés de T0.7 (aucun couperet de temps), avant la descente du modèle (O-1)
LISTE="tests/test_t07_*.py"; [ "$ESSAI" = 1 ] && [ -n "${ESSAIS_LISTE:-}" ] && LISTE="$ESSAIS_LISTE"
sha256sum $LISTE > "$X/essais-liste.txt"
PYTHONPATH=src "$PY" -m pytest -q -rsxX -p no:cacheprovider --color=no $LISTE --basetemp="$T/essais-tmp" -o tmp_path_retention_policy=failed > "$X/essais.txt" 2> "$X/essais.err"; c=$?
DL=$(tail -n 1 "$X/essais.txt" | sed -E 's/ in [0-9.]+s.*$//'); j "essais : code $c, $DL"
[ -z "$(git status --porcelain --untracked-files=all -- src tests)" ] || arret "les essais ont écrit sous src ou tests" 2
if [ "$MESURE" = 1 ]; then
    printf '%s\n' "$DL" > "$T/ligne-essais-mesuree.txt"
    grep -E '^(SKIPPED|XFAIL|XPASS|FAILED|ERROR)' "$X/essais.txt" > "$X/essais-sauts.txt"
    j "MESURE : ligne d'essais « $DL » (code $c) ; arrêt après les essais (mesure seulement, rien d'ouvert)"; fin_instance 0
fi
[ "$c" = 0 ] && [ "$DL" = "$ATTENDU" ] || arret "essais de T0.7 : code $c, « $DL » attendu « $ATTENDU »" 2
# 7. taille des sorties de l'étape A, estimée et bornée AVANT toute ouverture (O-2) ; calcul écrit (ordre, brouillon 4, § 5 bis)
"$PY" -I - "$RUN6" "$CONFIG" registres/scellements-v1.md "$PERIM" "$BORNE" "$SEUIL" "$MORCEAU" > "$X/taille-estimee.json" 2> "$X/taille-estimee.err" <<'PYEOF'
import glob, hashlib, json, math, sys, zipfile
import numpy as np
run6, cfg_path, reg_path, perim = sys.argv[1:5]
borne, seuil, morceau = (int(x) for x in sys.argv[5:8])
def sceau(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    with open(p + ".sha256", encoding="utf-8") as f:
        if h.hexdigest() != f.read().split()[0]:
            raise SystemExit(f"sceau faux : {p}")
mes = f"donnees/{run6}/mesures-t06.npz"
sceau(mes)
with np.load(mes, allow_pickle=False) as z:
    n = int((np.asarray(z["jetons_notes"]) > 0).sum())
    s = sum(int(z[k].dtype.itemsize) * int(np.prod(z[k].shape[1:], dtype=np.int64)) for k in ("cle", "condition", "tache", "pas"))
morceaux = sorted(glob.glob(f"donnees/{run6}/activations-sous-ensemble-t06-[0-9][0-9][0-9].npz"))
if not morceaux:
    raise SystemExit("aucun morceau du sous-ensemble d'activations de 7b : largeur inconnue")
sceau(morceaux[0])
largeurs = set()
with zipfile.ZipFile(morceaux[0]) as zf:
    for nom in zf.namelist():
        with zf.open(nom) as f:
            v = np.lib.format.read_magic(f)
            forme = (np.lib.format.read_array_header_1_0 if v == (1, 0) else np.lib.format.read_array_header_2_0)(f)[0]
        if len(forme) == 2:
            largeurs.add(int(forme[1]))
if len(largeurs) != 1:
    raise SystemExit(f"largeur des activations illisible : {sorted(largeurs)}")
d = largeurs.pop()
cfg = json.load(open(cfg_path, encoding="utf-8"))
P, nc, spc = int(cfg["n_plancher"]), len(cfg["couches"]), cfg["sondes_par_concept"]
per = set() if perim == "aucun" else set(perim.split(","))
K = len(per & {"JD", "JC"})                      # concepts neufs appris (dissimulation, domaine)
p6 = int({"JA", "JC"} <= per)                    # T7-P6 : sonde et témoin
L = min(len(spc), sum(1 for v in spc.values() if v) + K)   # sondes lues, chacune avec P directions de plancher
C = 0
if "CONCEPTS" in per:
    ligne = [l for l in open(reg_path, encoding="utf-8") if l.startswith("| SCELLEMENT-CONCEPTS-T07 |")][0]
    noms = set()
    for l in open(ligne.split("|")[3].strip(), encoding="utf-8"):
        x = json.loads(l) if l.strip() else None
        if isinstance(x, dict) and "concept" in x:
            noms.add(str(x["concept"]))
    C = len(noms)
D = C * nc                                       # directions des concepts (T7-P9), chacune avec P directions de plancher
F = L * (1 + P) + 8 * nc + 5 * nc * K + 2 * p6 * (1 + P) + D * (1 + P) + K + 1
scores = n * (8 * F + s) + 5_000_000
maha = d * d + d
neuves = 8 * (nc * K * maha + nc * K * (22 * d + 64) + 2 * p6 * maha + (K + 2 * p6) * P * 2 * d + D * d) + 5_000_000
autres = 50_000_000
total = scores + neuves + autres
prevus = sum(math.ceil(x / morceau) for x in (scores, neuves) if x > seuil)
print(json.dumps({
    "regle": "O-2 : borne haute des sorties de l'étape A, avant toute ouverture ; float64, np.savez sans compression",
    "entrees": {"actions_notees": n, "octets_cles_par_action": s, "largeur": d, "n_plancher": P, "couches": nc,
                "sondes_lues_max": L, "concepts_neufs": K, "p6": p6, "concepts_t7p9": C, "directions": D},
    "scores_actions_t07": {"nombres_par_action": F, "octets": scores,
                           "formule": "n × (8 × F + s) + 5e6 ; F = L(1+P) + 8·couches + 5·couches·K + 2·p6·(1+P) + D(1+P) + K + 1"},
    "sondes_neuves_t07": {"octets": neuves,
                          "formule": "8 × [couches·K·(d²+d) + couches·K·(22d+64) + 2·p6·(d²+d) + (K+2·p6)·P·2d + D·d] + 5e6"},
    "autres_octets": autres, "total_octets": total, "borne_octets": borne, "seuil_octets": seuil, "morceau_octets": morceau,
    "morceaux_prevus": prevus, "tient": total <= borne}, ensure_ascii=False, indent=1))
sys.exit(0 if total <= borne else 3)
PYEOF
c=$?
case "$c" in
    0) j "taille estimée des sorties de l'étape A (O-2) : $("$PY" -I -c 'import json, sys
t = json.load(open(sys.argv[1], encoding="utf-8"))
print("%d octets ≤ borne %d (scores %d, sondes neuves %d, %d morceaux prévus)" % (t["total_octets"], t["borne_octets"],
      t["scores_actions_t07"]["octets"], t["sondes_neuves_t07"]["octets"], t["morceaux_prevus"]))' "$X/taille-estimee.json")";;
    3) arret "taille estimée des sorties de l'étape A au-dessus de la borne (O-2, taille-estimee.json) : nœud, rien n'est ouvert" 2;;
    *) arret "taille des sorties de l'étape A non estimable (code $c, taille-estimee.err) : rien n'est ouvert" 2;;
esac
j "disque libre : $(df -P -B1 "$T" | awk 'NR == 2 { print $4 }') octets"
# 8. modèle, au cache local (réel) ; tout le reste lit hors ligne
if [ "$ESSAI" != 1 ]; then
    PYTHONPATH=src timeout -k 10 3600 "$PY" -c 'import json, sys
from controle_ia.harnais.modeles import precharger_modele
a = json.load(open(sys.argv[1], encoding="utf-8"))["config"]["agent"]
print(precharger_modele(a["modele"], a["revision"]))' "runs/$RUN6/manifeste.json" > "$X/modele.txt" 2>&1 || arret "descente du modèle (HF_TOKEN, révision figée)" 2
    j "modèle au cache local"
fi
E=$(PYTHONPATH=src "$PY" -m controle_ia.t07.lecture_v2 empreinte-config "$CONFIG") || arret "empreinte de la configuration" 2
j "configuration $CONFIG, empreinte canonique $E"
# 9. CODE-T07 (ordre : 1. CODE-T07 inscrite et contrôlée, 2. repli, 3. passe à blanc, 4. étape A)
PYTHONPATH=src "$PY" -m controle_ia.t07.code_t07_v1 verifier . registres/scellements-v1.md > "$X/code-t07.txt" 2>&1 || arret "CODE-T07 non conforme (code-t07.txt)" 2
j "$(head -n 1 "$X/code-t07.txt")"
# 10. branche neuve et poussées (chemins présents seulement, ajout explicite, jamais -A) ; O-2 : légers d'abord (aucun fichier de
#     plus de SEUIL octets), puis chaque fichier de plus de SEUIL octets découpé en morceaux scellés, poussés par lots de LOT
git ls-remote --exit-code origin "refs/heads/$BR" > /dev/null 2>&1; [ $? = 2 ] || arret "branche $BR présente sur le dépôt distant (R12) ou dépôt injoignable" 2
git checkout -q -b "$BR" || arret "branche locale" 2
envoyer() { local n; for n in 1 2 3; do git push -q origin "HEAD:refs/heads/$BR" && { j "poussé : $(git rev-parse HEAD) « $1 »"; return 0; }; sleep $((20 * n)); done
    BRANCHE_PRETE=0; arret "poussée « $1 » impossible"; }
decouper() {  # $1 = fichier de plus de SEUIL octets : morceaux de MORCEAU octets, chacun scellé ; recomposition vérifiée contre le
    # fichier et son compagnon ; manifeste scellé (`<fichier>.morceaux.json`) ; original déplacé hors du dépôt ($T/hors-depot)
    local f="$1" t sha p
    t=$(stat -c %s "$f"); sha=$(sha256sum < "$f" | cut -d' ' -f1)
    [ ! -f "$f.sha256" ] || [ "$(cut -d' ' -f1 "$f.sha256")" = "$sha" ] || arret "découpage : $f ne répond pas à son compagnon (nœud)" 3
    [ -f "$f.sha256" ] || PYTHONPATH=src "$PY" -m controle_ia.scellement sceller "$f" > /dev/null || arret "découpage : sceau de $f" 3
    ! ls "$f".morceau-* > /dev/null 2>&1 || arret "découpage : morceaux de $f déjà présents (R12)" 3
    split -b "$MORCEAU" -d -a 3 -- "$f" "$f.morceau-" || arret "découpage de $f" 3
    [ "$(cat "$f".morceau-[0-9][0-9][0-9] | sha256sum | cut -d' ' -f1)" = "$sha" ] || arret "découpage : recomposition de $f différente (nœud)" 3
    for p in "$f".morceau-[0-9][0-9][0-9]; do PYTHONPATH=src "$PY" -m controle_ia.scellement sceller "$p" > /dev/null || arret "sceau de $p" 3
        printf '%s\n' "$p" >> "$X/morceaux-a-pousser.txt"; done
    "$PY" -I -c 'import json, os, sys
f, t, sha, m = sys.argv[1], int(sys.argv[2]), sys.argv[3], int(sys.argv[4])
pieces = sorted(x for x in os.listdir(os.path.dirname(f) or ".") if x.startswith(os.path.basename(f) + ".morceau-") and not x.endswith(".sha256"))
d = os.path.dirname(f) or "."
corps = {"fichier": f, "octets": t, "sha256": sha, "morceau_octets": m, "regle": "O-2 (ordre, brouillon 4) : fichier de plus du seuil découpé par split -b, morceaux scellés",
         "morceaux": [{"fichier": x, "octets": os.path.getsize(os.path.join(d, x)), "sha256": open(os.path.join(d, x + ".sha256"), encoding="utf-8").read().split()[0]} for x in pieces],
         "recomposer": "cd %s && cat %s.morceau-[0-9][0-9][0-9] > %s && sha256sum -c %s.sha256" % (d, os.path.basename(f), os.path.basename(f), os.path.basename(f))}
open(f + ".morceaux.json", "w", encoding="utf-8").write(json.dumps(corps, ensure_ascii=False, indent=1) + "\n")' "$f" "$t" "$sha" "$MORCEAU" || arret "manifeste des morceaux de $f" 3
    PYTHONPATH=src "$PY" -m controle_ia.scellement sceller "$f.morceaux.json" > /dev/null || arret "sceau du manifeste de $f" 3
    mkdir -p "$T/hors-depot/$(dirname "$f")" && mv -- "$f" "$T/hors-depot/$f" || arret "déplacement de $f hors du dépôt" 3
    j "découpé (O-2) : $f, $t octets, $(ls "$f".morceau-[0-9][0-9][0-9] | wc -l) morceaux de ≤ $MORCEAU octets, manifeste $f.morceaux.json scellé ; original hors du dépôt"; }
pousser() {  # $1 = message ; puis chemins
    local m="$1" x a=() g=() ex=() p n k lot; shift; for x in "$@"; do [ -e "$x" ] && a+=("$x"); done
    [ "${#a[@]}" -gt 0 ] || { j "rien à pousser (« $m »)"; return 0; }
    while IFS= read -r -d '' x; do case "$x" in *.morceau-[0-9][0-9][0-9]|*.morceau-[0-9][0-9][0-9].sha256) ;; *) g+=("$x"); ex+=(":(exclude,literal)$x");; esac
    done < <(find "${a[@]}" -type f -size +"${SEUIL}"c -print0 2>/dev/null | sort -z)
    git add --sparse -f -- "${a[@]}" "${ex[@]}" ':(exclude,glob)**/*.morceau-[0-9][0-9][0-9]' ':(exclude,glob)**/*.morceau-[0-9][0-9][0-9].sha256' || { BRANCHE_PRETE=0; arret "ajout « $m »"; }
    while IFS= read -r -d '' x; do [ "$(stat -c %s "$x")" -le "$SEUIL" ] || { BRANCHE_PRETE=0; arret "fichier de plus de $SEUIL octets dans l'index : $x (nœud)"; }; done < <(git diff --cached --name-only -z --diff-filter=AM)
    if git diff --cached --quiet; then j "rien de neuf parmi les légers (« $m »)"; else git commit -q -m "$m" || { BRANCHE_PRETE=0; arret "commit « $m »"; }; envoyer "$m"; fi
    [ "${#g[@]}" -gt 0 ] || return 0
    : > "$X/morceaux-a-pousser.txt"
    for x in "${g[@]}"; do decouper "$x"; done
    mapfile -t p < "$X/morceaux-a-pousser.txt"; n=${#p[@]}; k=0
    while [ "$k" -lt "$n" ]; do
        lot=("${p[@]:k:LOT}"); a=(); for x in "${lot[@]}"; do a+=("$x" "$x.sha256"); done
        [ "$k" = 0 ] && for x in "${g[@]}"; do a+=("$x.sha256" "$x.morceaux.json" "$x.morceaux.json.sha256"); done
        git add --sparse -f -- "${a[@]}" && git commit -q -m "$m : morceaux $((k + 1)) à $((k + ${#lot[@]})) sur $n" || { BRANCHE_PRETE=0; arret "commit des morceaux « $m »"; }
        envoyer "$m : morceaux $((k + 1)) à $((k + ${#lot[@]})) sur $n"; k=$((k + LOT)); done; }
BRANCHE_PRETE=1
# 11. repli : garde d'ouverture de l'étape A (journalisée) PUIS recalcul sous un nom daté et garde d'équivalence (DF-01) ;
#     R11 : une relance sur la même carte, sous un nom daté neuf (le premier recalcul reste) ; refus de la garde : arrêt (attente)
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
# 12. passe à blanc (aucune donnée décisive)
PYTHONPATH=src "$PY" -m controle_ia.t07.lecture_v2 passe-blanc . "$RUN6" "$CONFIG" > "$X/passe-blanc.txt" 2> "$X/passe-blanc.err"; c=$?
j "passe à blanc : code $c ; $(head -n 1 "$X/passe-blanc.txt")"
traces; pousser "T0.7 (variante B) : passe à blanc de l'extracteur (aucune donnée décisive), code $c" passes-blanches-t07 "$XT"
[ "$c" = 0 ] || arret "passe à blanc : code $c : l'étape A ne part pas (motif : passe-blanc.err)" 3
# 13. étape A après le repli (garde d'identité remplacée par la garde d'équivalence) ; légers d'abord, morceaux ensuite (O-2)
PYTHONPATH=src "$PY" -m controle_ia.t07.lecture_v2 etape-a-apres-repli . "$RUN6" "$CONFIG" > "$X/etape-a.txt" 2> "$X/etape-a.err"; c=$?
RUN7=$(ls -1 runs 2>/dev/null | grep -- '-t07-lecture-' | sort | tail -n 1); j "étape A : code $c${RUN7:+, run $RUN7}"
CH=(registres/scellements-v1.md registres/scellements-v1.md.ouvertures.md "$XT")
[ -n "$RUN7" ] && CH+=("runs/$RUN7" "diag/$RUN7" "donnees/$RUN7")
traces; pousser "T0.7 (variante B), étape A : sorties scellées, code $c${RUN7:+, run $RUN7}" "${CH[@]}"
traces; pousser "T0.7 (variante B), étape A : traces après les morceaux" "$XT"
[ "$c" = 0 ] || arret "étape A : code $c : nœud, aucune relance sous ce texte (motif : etape-a.err)" 3
[ ! -e "$D/diag/$RUN6/lecture-sondes-t06.json" ] || arret "lecture-sondes-t06.json présent : embargo" 3
j "FIN : étape A menée au bout, run $RUN7, tête $(git rev-parse HEAD)"
fin_instance 0
