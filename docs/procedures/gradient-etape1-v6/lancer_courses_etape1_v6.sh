#!/usr/bin/env bash
# Lanceur des courses réelles de l'étape 1 du programme « gradient conçu par l'essaim », version 6, pour la v9 du
# préenregistrement (`prereg/gradient-etape1-sondes-v9.md`, scellé). Écrit par la lignée « session-depot » le 25 octobre
# 2026, décliné du lanceur v5 (relu par la contre-lecture n° 8, jamais versé) sous un nom nouveau (R12) : la question
# « structure » n'est plus posée aux courses A_r, seulement à la répétition (décision de Lazar sur CL8-01, R-410) ; la clé
# OpenAlex (`OPENALEX_API_KEY`), si elle est présente, est passée au noyau seul, sa présence consignée et exigée identique
# pour B_r (R-415), comme celle de Brave ; de même la clé Semantic Scholar (`SEMANTIC_SCHOLAR_API_KEY`, R-417). Le v5,
# décliné du v4, apportait : la question « structure » posée aux organismes à la
# première ronde de conception seulement (R-393 : `--question-ouverte … --question-ouverte-aux c001`, pièce versée à côté
# de ce fichier, empreinte lue au format littéral « question_c001_sha256 = … » du préenregistrement) ; la clé Anthropic
# choisie par son nom (`CLE_ANTHROPIC`, R-394), consignée et exigée identique pour A_r et B_r ; le chemin du
# préenregistrement lu corrigé (le v4 lisait `gradient-etape1-sondes-v5.md`, nom qu'aucune version scellée ne porte) ;
# la porte de la répétition vérifie que la question a été posée à `c001`, et nulle part ailleurs, et rapporte sans condition
# les statuts des appels par espèce, ceux qui ont réfléchi (R-402) et les plafonds demandés (réflexion comprise dans
# `max_tokens`, R-398) ; les tests de dépense sont imputés à GO-05 et exigent des jetons de sortie (R-403). Le v4 portait les
# corrections des contre-lectures n° 4 (CE4-04, CE4-07 a à g, CE4-08, CE4-09, CE4-12, CE4-13) et n° 5 (CL5-03 répétition à
# 5 USD par génération ; CL5-10 porte ; le noyau ferme CL5-01 et CL5-02). Indépendant de l'hôte : il tourne sur la machine
# retenue par Lazar, en root, où le noyau vérifie lui-même l'isolation. Une course (ou l'épreuve) par appel :
#   epreuve       épreuve de durée sans dépense (CE4-08) : un processus détaché bat toutes les 60 s pendant 2 h 15 et
#                 écrit `epreuve-duree.json` ; exigée, sur le même hôte, avant toute course décisive ;
#   repetition    répétition mécanique (Plan d'analyse, point 8) : lignées CLAUDE_FABLE_5_1, CLAUDE_OPUS_5_5,
#                 GEMINI_ARGON, deux rondes de conception à 2 USD, une génération à 5 USD, 20 appels, 900 s, deux
#                 entraînements de 60 s, moisson réduite (2 recherches, 1 téléchargement), vivier servi, question à
#                 `c001`, plafond 40 USD ;
#   repetition-B  le chemin réel du bras B : `--depuis repetition`, `--entrainements-max 0`, une génération, plafond
#                 10 USD (CE4-04 (4)) ; les deux répétitions sont exclues de toute analyse ;
#   A1, A2        bras avec gradient, réplique 1 ou 2 (point 3), sans question (R-410) ;
#   B1, B2        bras sans gradient, `--depuis` la course A de même réplique (point 3), une fois A terminée.
# Contrôles avant tout appel payant (code 2 si l'un échoue, avec une note dans `lancements.txt`) :
#   hôte (root ; `unshare` réseau ; espaces de noms de montage, de processus et de communication ; dossier en mémoire
#   montable dans un espace de montage privé ; `fs.protected_hardlinks`) et **même hôte** que les courses déjà lancées
#   dans ce dossier (empreinte de l'hôte, CE4-08) ; préenregistrement scellé et conforme (validateur du dépôt) qui cite
#   le commit ; chaque valeur littérale lue y figure **une fois au plus** (CE4-12) ; code à ce commit, arbre propre,
#   fichiers non suivis compris (CE4-07 b) ; dossier des courses à root en 0700 (CE3-06) ; entrées aux empreintes
#   citées, extraites une fois sous verrou (CE4-07 f) ; vivier présent au commit cité (CE4-07 c) ; question à l'empreinte
#   `question_c001_sha256` du préenregistrement (R-393) ; ligne d'engagement
#   de la course dans `registres/depenses.md` (CE3-15) ; GO de la course et GO des appels de contrôle acceptés par la
#   garde ; clé Anthropic nommée par `CLE_ANTHROPIC` parmi les noms admis, sans défaut (R-394) ; clés présentes (jamais
#   affichées, jamais dans une ligne de commande : CE4-13) ; pour un bras B, **mêmes noms de clés que A** (Anthropic,
#   Gemini et Brave, lus dans `<A>.cles.txt` écrit par le lanceur de A, et Brave aussi dans le manifeste de A :
#   CE4-07 d, e) ; sortie neuve (R12) ; verrou propre à la course ; pour un bras B, course A terminée
#   (verrou libre) avec au moins une génération 0 archivée ; pour une course décisive (A, B), **portes** de la
#   répétition, de la répétition B et de l'épreuve de durée passées (CE4-04 (2), CE4-08) ; graines lues au format
#   littéral « graine_r = <entier> » (CE3-16) ; appel de contrôle par espèce de la course, statut OK exigé.
# Imputation (CE4-09, R-403) : tests de dépense (appels de contrôle), répétitions et courses à GO-2026-10-24-05 (mot direct
# de Lazar, 25 octobre : GO-07, qui nommait les appels de contrôle, échoit le 26 octobre).
# Sorties : `<course>.sortie.json` (sortie du noyau : courbes et scores) en 0600, scellée, jamais ouverte avant la
# lecture ; `<course>.erreurs.txt`, scellé ; le lanceur n'affiche que l'extrait mécanique sans score
# (`<course>.extrait-mecanique.json`) ; après une répétition, `<course>.porte.json` (porte mécanique, scellée) ;
# `<course>.fin.json` écrit dès que la course est partie, quelle que soit sa fin (CE4-07 g ; un arrêt avant la course
# n'a que sa note dans `lancements.txt` ; un arrêt de l'hôte n'en écrit pas : course arrêtée, consignée, lue à la
# dernière génération valide commune, aucune relance).
# Mode `--controles` : tous les contrôles, sans appel de contrôle ni course (code 0 si tout passe) ; les portes absentes
# y sont signalées, non exigées.
# Codes : 0 course finie (ou épreuve partie) ; 2 arrêt avant la course ; autre : code de sortie du noyau.
# Usage : CODE_ETAPE1=<dossier de travail git> COMMIT_ETAPE1=<commit> CLE_ANTHROPIC=<nom de la variable de la clé>
#         lancer_courses_etape1_v6.sh [--controles] COURSE DOSSIER_DES_COURSES
# Noms admis pour CLE_ANTHROPIC (R-394) : RR_ANTHROPIC_API_KEY (avec l'en-tête d'espace de travail
# RR_ANTHROPIC_WORKSPACE_ID), RR_ANTHROPIC_API_KEY_2, RR_ANTHROPIC_API_KEY_3, RR_ANTHROPIC_API_KEY_LUC (sans en-tête).
set -euo pipefail
umask 077
CONTROLES=0
if [ "${1:-}" = "--controles" ]; then CONTROLES=1; shift; fi
[ $# -eq 2 ] || { echo "usage : lancer_courses_etape1_v6.sh [--controles] {epreuve|repetition|repetition-B|A1|A2|B1|B2} DOSSIER_DES_COURSES"; exit 2; }
COURSE=$1; RACINE=$(realpath -m "$2")
DEPOT=${DEPOT_ETAPE1:-/home/user/controle-ia-travail}
DEPOT_GIT=${DEPOT_GIT_ETAPE1:-$DEPOT}   # objets git des entrées (essais du lanceur : un clone partagé)
VENV=${VENV_ETAPE1:-/opt/essaim-m3-venv-v1}
PREREG=prereg/gradient-etape1-sondes-v9.md
Q_NOM=question-apprendre-structure-entrainement-generations-organismes-v2.md
Q_SOURCE="$DEPOT/docs/procedures/gradient-etape1-v6/$Q_NOM"   # pièce versée à côté du lanceur (R-393)
GO=GO-2026-10-24-05
GO_CONTROLE=GO-2026-10-24-05   # tests de dépense imputés à GO-05 (mot direct de Lazar, 25 octobre ; GO-07 échoit le 26 : R-403)
E_BANQUE=f1387a20cb272d2e8c205102147dfee71cd1d372f7f5d2ad4ff8233783cc83cc
E_TRAITS=add13e090a13b60e48983393ae376cc9df2542210b5328bc2abd94e661e25f17
case "$COURSE" in epreuve) DECALAGE= ;; repetition) DECALAGE=500 ;; repetition-B) DECALAGE=600 ;;
    A1) DECALAGE=100 ;; A2) DECALAGE=200 ;; B1) DECALAGE=300 ;; B2) DECALAGE=400 ;;
    *) echo "course inconnue : $COURSE"; exit 2 ;; esac
# 0. dossier des courses : à root, 0700 (CE3-06) ; journal des lancements
[ "$(id -u)" = 0 ] || { echo "le noyau exige root (isolation d'utilisateur, CR-01)"; exit 2; }
if [ -e "$RACINE" ]; then
    [ -d "$RACINE" ] && [ ! -L "$RACINE" ] || { echo "$RACINE : vrai dossier attendu"; exit 2; }
    [ "$(stat -c '%u %a' "$RACINE")" = "0 700" ] || { echo "$RACINE : dossier à root en 0700 attendu (CE3-06), trouvé $(stat -c '%u %a' "$RACINE")"; exit 2; }
else
    mkdir -p -m 0700 "$RACINE"
fi
J="$RACINE/lancements.txt"
note() { printf '%s %s : %s\n' "$(date -u +%FT%TZ)" "$COURSE" "$*" | tee -a "$J"; }
stop() { note "$*"; exit 2; }
note "lanceur $(sha256sum "$0" | cut -d' ' -f1)$( [ $CONTROLES = 1 ] && printf ' (contrôles seulement)')"
# 1. hôte : isolation, protections du système de fichiers, même hôte pour toutes les courses du dossier (CE4-08)
unshare -n true 2>/dev/null || stop "hôte : unshare -n refusé (isolation réseau impossible) : hôte inadapté"
unshare --mount --pid --ipc --fork --kill-child --mount-proc true 2>/dev/null || stop "hôte : espaces de noms de montage, de processus et de communication refusés"
unshare --mount sh -c 'mount -t tmpfs -o size=1m tmpfs /tmp' 2>/dev/null || stop "hôte : dossier en mémoire privé impossible dans un espace de montage (RV-04)"
[ "$(cat /proc/sys/fs/protected_hardlinks 2>/dev/null)" = 1 ] || stop "hôte : fs.protected_hardlinks doit valoir 1"
HOTE=$(printf '%s|%s|%s|%s' "$(cat /etc/machine-id 2>/dev/null || true)" "$(hostname)" "$(uname -r)" "$(nproc)" | sha256sum | cut -c1-16)
if [ -f "$RACINE/hote.txt" ]; then
    [ "$(cat "$RACINE/hote.txt")" = "$HOTE" ] || stop "hôte : empreinte $HOTE ≠ $(cat "$RACINE/hote.txt") des courses déjà lancées ici : changement d'hôte = écart (CE4-08)"
else
    printf '%s\n' "$HOTE" > "$RACINE/hote.txt"
fi
note "hôte $HOTE : $(uname -r) ; $(nproc) cœurs ; $(df -h "$RACINE" | awk 'NR==2{print $4}') libres ; protected_symlinks=$(cat /proc/sys/fs/protected_symlinks 2>/dev/null)"
# épreuve de durée (CE4-08) : aucune clé, aucun appel ; un processus détaché, consigné par son PID (R10)
if [ "$COURSE" = epreuve ]; then
    [ -e "$RACINE/epreuve-duree.json" ] || [ -e "$RACINE/epreuve" ] && stop "épreuve déjà faite ou en cours (R12)"
    [ $CONTROLES = 1 ] && { note "contrôles : tout passe (épreuve non lancée)"; exit 0; }
    mkdir -m 0700 "$RACINE/epreuve"
    setsid nohup bash -c '
        d=$1; h=$2; debut=$(date -u +%s)
        while [ $(( $(date -u +%s) - debut )) -lt 8100 ]; do date -u +%s >> "$d/battements.txt"; sleep 60; done
        python3 -I -B - "$d/battements.txt" "$h" "$debut" > "$d/../epreuve-duree.json" <<'"'"'PY'"'"'
import json, sys
b = [int(x) for x in open(sys.argv[1]).read().split()]
ecarts = [y - x for x, y in zip(b, b[1:])]
print(json.dumps({"hote": sys.argv[2], "debut": int(sys.argv[3]), "fin": b[-1], "duree_s": b[-1] - int(sys.argv[3]),
                  "battements": len(b), "ecart_max_s": max(ecarts) if ecarts else None}))
PY
        sha256sum "$d/../epreuve-duree.json" > "$d/../epreuve-duree.json.sha256"' epreuve "$RACINE/epreuve" "$HOTE" \
        > "$RACINE/epreuve/sortie.txt" 2>&1 < /dev/null &
    note "épreuve de durée partie : PID $! (8100 s, battement toutes les 60 s ; arrêt par ce PID seulement, R10)"
    exit 0
fi
CODE=${CODE_ETAPE1:?CODE_ETAPE1 : dossier de travail git de outils/essaim-m3-gradient-v2-travail}
COMMIT=${COMMIT_ETAPE1:?COMMIT_ETAPE1 : commit cité par le préenregistrement scellé}
[[ "$COMMIT" =~ ^[0-9a-f]{40}$ ]] || stop "COMMIT_ETAPE1 : 40 caractères hexadécimaux attendus"
# 2. préenregistrement scellé et conforme, qui cite le commit ; valeurs littérales uniques
python3 -I -B - "$DEPOT/src" "$DEPOT/$PREREG" > "$RACINE/.prereg-$COURSE.txt" 2>&1 <<'PY' || stop "préenregistrement non scellé ou non conforme : $(tail -1 "$RACINE/.prereg-$COURSE.txt")"
import sys
sys.path.insert(0, sys.argv[1])
from controle_ia import prereg
print(prereg.exiger_prereg_scelle(sys.argv[2]))
PY
grep -qF "$COMMIT" "$DEPOT/$PREREG" || stop "le préenregistrement ne cite pas le commit $COMMIT"
note "préenregistrement scellé $(head -c 16 "$RACINE/.prereg-$COURSE.txt")…"
# valeur littérale « nom = valeur » hors accents graves (CE3-16) ; vide si absente ; plus d'une occurrence : refus (CE4-12)
motif_litteral() { printf '(^|[[:space:]])%s = [0-9a-zA-Z_./:-]+' "$1"; }
for nom in vivier_commit vivier_chemin vivier_sha256 question_c001_sha256 graine_1 graine_2 entropie_analyse; do
    n=$({ grep -oE "$(motif_litteral "$nom")" "$DEPOT/$PREREG" || true; } | wc -l)
    [ "$n" -le 1 ] || stop "préenregistrement : « $nom = … » y figure $n fois (une seule occurrence permise, CE4-12)"
done
litteral() { grep -oE "$(motif_litteral "$1")" "$DEPOT/$PREREG" | head -1 | sed -E "s/.*$1 = //" || true; }
# 3. code au commit cité, arbre propre (fichiers non suivis compris ; le bytecode est ignoré par le dépôt)
[ "$(git -C "$CODE" rev-parse HEAD)" = "$COMMIT" ] || stop "code : HEAD $(git -C "$CODE" rev-parse HEAD) ≠ $COMMIT"
[ -z "$(git -C "$CODE" status --porcelain --untracked-files=all)" ] || stop "code : arbre de travail modifié ou fichier non suivi"
# 4. entrées aux empreintes citées (extraites une fois sous verrou dans RACINE/entrees, jamais réécrites)
V_COMMIT=$(litteral vivier_commit); V_CHEMIN=$(litteral vivier_chemin); E_VIVIER=$(litteral vivier_sha256)
[[ "$V_COMMIT" =~ ^[0-9a-f]{40}$ ]] && [ -n "$V_CHEMIN" ] && [[ "$E_VIVIER" =~ ^[0-9a-f]{64}$ ]] \
    || stop "vivier : vivier_commit, vivier_chemin ou vivier_sha256 absent du préenregistrement"
git -C "$DEPOT_GIT" cat-file -e "$V_COMMIT:$V_CHEMIN" 2>/dev/null && git -C "$DEPOT_GIT" cat-file -e "$V_COMMIT:$V_CHEMIN.sha256" 2>/dev/null \
    || stop "vivier : $V_CHEMIN ou son compagnon .sha256 absent du commit $V_COMMIT"
E_QUESTION=$(litteral question_c001_sha256)
[[ "$E_QUESTION" =~ ^[0-9a-f]{64}$ ]] || stop "question : question_c001_sha256 absent du préenregistrement"
EN="$RACINE/entrees"
exec 7>"$RACINE/.verrou-entrees"
flock -w 600 7 || stop "entrées : verrou d'extraction tenu plus de 600 s"
if [ ! -e "$EN/pret" ]; then
    rm -rf "$EN"; mkdir -p -m 0700 "$EN" "$EN/traits" "$EN/vivier" "$EN/question"
    git -C "$DEPOT_GIT" show bffe03c:essaim-m3-refonte-v1/banque/banque-confrontation-v1.json > "$EN/banque-confrontation-v1.json"
    git -C "$DEPOT_GIT" show bffe03c:essaim-m3-refonte-v1/banque/banque-confrontation-v1.json.sha256 > "$EN/banque-confrontation-v1.json.sha256"
    git -C "$DEPOT_GIT" archive 6479769 essaim-m3-refonte-v1/traits/etape1-v1 | tar -x -C "$EN/traits" --strip-components=2
    V_NOM=$(basename "$V_CHEMIN")
    git -C "$DEPOT_GIT" show "$V_COMMIT:$V_CHEMIN" > "$EN/vivier/$V_NOM"
    git -C "$DEPOT_GIT" show "$V_COMMIT:$V_CHEMIN.sha256" > "$EN/vivier/$V_NOM.sha256"
    { [ -f "$Q_SOURCE" ] && [ ! -L "$Q_SOURCE" ] && cp "$Q_SOURCE" "$EN/question/$Q_NOM"; } || true  # vérifiée plus bas
    touch "$EN/pret"
fi
flock -u 7
V_FICHIER="$EN/vivier/$(basename "$V_CHEMIN")"
Q_FICHIER="$EN/question/$Q_NOM"
[ "$(sha256sum "$EN/banque-confrontation-v1.json" | cut -d' ' -f1)" = "$E_BANQUE" ] || stop "banque : empreinte différente"
[ -f "$EN/traits/etape1-v1/EMPREINTES-traits-etape1-v1.txt" ] && [ "$(sha256sum "$EN/traits/etape1-v1/EMPREINTES-traits-etape1-v1.txt" | cut -d' ' -f1)" = "$E_TRAITS" ] \
    || stop "traits : empreintes différentes"
(cd "$EN/traits/etape1-v1" && sha256sum -c --quiet EMPREINTES-traits-etape1-v1.txt) || stop "traits : un fichier diffère de ses empreintes"
[ -f "$V_FICHIER" ] && [ "$(sha256sum "$V_FICHIER" | cut -d' ' -f1)" = "$E_VIVIER" ] || stop "vivier : empreinte différente de vivier_sha256"
[ -f "$Q_FICHIER" ] && [ ! -L "$Q_FICHIER" ] && [ "$(sha256sum "$Q_FICHIER" | cut -d' ' -f1)" = "$E_QUESTION" ] \
    || stop "question : $Q_NOM absente des entrées ou d'empreinte différente de question_c001_sha256 (R-393)"
chmod -R go-rwx "$EN"
# 5. engagement de la course consigné avant (CE3-15)
if grep -qF "engagement : course $COURSE de l'étape 1" "$DEPOT/registres/depenses.md"; then
    note "engagement consigné dans registres/depenses.md"
elif [ $CONTROLES = 1 ]; then
    note "engagement : absent de registres/depenses.md (non exigé en mode contrôles ; exigé avant la course)"
else
    stop "aucune ligne « engagement : course $COURSE de l'étape 1 » dans registres/depenses.md"
fi
# 6. garde de calcul rejouée avec le GO de la course et celui des appels de contrôle ; extrait du registre
cp "$DEPOT/registres/go.md" "$RACINE/registre-go-$COURSE.md"
for g in "$GO" "$GO_CONTROLE"; do
    printf '{"tool_input":{"command":"GO_ID=%s vastai create instance 0"}}' "$g" | python3 -I -B "$DEPOT/.claude/hooks/garde_calcul.py" 2>/dev/null \
        || stop "garde de calcul : $g refusé"
done
# 7. clés présentes, jamais affichées ; clé Anthropic choisie par son nom, sans défaut (R-394) : l'en-tête d'espace de
# travail seulement pour RR_ANTHROPIC_API_KEY ; clé Gemini n° 2 si elle existe ; clé Brave : présence consignée
ANTHROPIC_NOM=${CLE_ANTHROPIC:-}
case "$ANTHROPIC_NOM" in
    RR_ANTHROPIC_API_KEY|RR_ANTHROPIC_API_KEY_2|RR_ANTHROPIC_API_KEY_3|RR_ANTHROPIC_API_KEY_LUC) ;;
    *) stop "CLE_ANTHROPIC : « ${ANTHROPIC_NOM} » n'est pas un nom admis (RR_ANTHROPIC_API_KEY, _2, _3, _LUC ; R-394)" ;;
esac
ANTHROPIC_CLE=${!ANTHROPIC_NOM:-}
[ -n "$ANTHROPIC_CLE" ] || stop "clé absente : $ANTHROPIC_NOM"
if [ "$ANTHROPIC_NOM" = RR_ANTHROPIC_API_KEY ]; then
    [ -n "${RR_ANTHROPIC_WORKSPACE_ID:-}" ] || stop "clé absente : RR_ANTHROPIC_WORKSPACE_ID (en-tête de RR_ANTHROPIC_API_KEY)"
    ANTHROPIC_ESPACE=$RR_ANTHROPIC_WORKSPACE_ID
else
    ANTHROPIC_ESPACE=
fi
GEMINI_NOM=GEMINI_API_KEY_2; [ -n "${GEMINI_API_KEY_2:-}" ] || GEMINI_NOM=GEMINI_API_KEY
GEMINI_CLE=${!GEMINI_NOM:-}
[ -n "$GEMINI_CLE" ] || stop "clé absente (GEMINI_API_KEY_2 ou GEMINI_API_KEY)"
BRAVE=non; [ -n "${BRAVE_API_KEY:-}" ] && BRAVE=oui
OPENALEX=non; [ -n "${OPENALEX_API_KEY:-}" ] && OPENALEX=oui   # R-415
S2=non; [ -n "${SEMANTIC_SCHOLAR_API_KEY:-}" ] && S2=oui   # R-417
CLES="anthropic=$ANTHROPIC_NOM gemini=$GEMINI_NOM brave=$BRAVE openalex=$OPENALEX semanticscholar=$S2"
note "clés : $CLES$( [ -n "$ANTHROPIC_ESPACE" ] && printf ' (en-tête d'"'"'espace de travail)')"
# 8. sortie neuve (R12) ; verrou propre à la course, tenu jusqu'à la fin du noyau
SORTIE="$RACINE/$COURSE"
[ -e "$SORTIE" ] && stop "$SORTIE existe déjà (R12)"
exec 9>"$RACINE/.verrou-$COURSE"
flock -n 9 || stop "course $COURSE déjà en cours (verrou tenu)"
# porte : une course décisive ne part qu'après la répétition, la répétition B et l'épreuve de durée réussies, sur cet hôte
porte() {  # $1 : fichier de porte ; rend 0 si la porte est passée
    python3 -I -B - "$1" "$HOTE" <<'PY'
import json, sys
try:
    p = json.load(open(sys.argv[1], encoding="utf-8"))
except (OSError, ValueError):
    sys.exit(1)
if "duree_s" in p:  # épreuve de durée
    ok = p.get("hote") == sys.argv[2] and int(p.get("duree_s") or 0) >= 7200 and (p.get("ecart_max_s") or 10**9) <= 180
else:
    ok = p.get("reussie") is True and p.get("hote") == sys.argv[2]
sys.exit(0 if ok else 1)
PY
}
case "$COURSE" in A*|B*)
    for p in repetition.porte.json repetition-B.porte.json epreuve-duree.json; do
        if [ -f "$RACINE/$p" ] && [ -f "$RACINE/$p.sha256" ] && (cd "$RACINE" && sha256sum -c --quiet "$p.sha256" 2>/dev/null) && porte "$RACINE/$p"; then
            note "porte $p : passée"
        elif [ $CONTROLES = 1 ]; then
            note "porte $p : absente ou non passée (non exigée en mode contrôles ; exigée avant la course)"
        else
            stop "porte $p : absente, altérée ou non passée sur cet hôte : la course décisive ne part pas (CE4-04, CE4-08)"
        fi
    done ;;
esac
# 9. paramètres de la course (Plan d'analyse, points 3, 4, 5, 8)
graine() { local g; g=$(litteral "graine_$1"); [[ "$g" =~ ^[0-9]+$ ]] && printf '%s' "$g"; }
# bras B : origine terminée, génération 0 archivée, mêmes noms de clés (CE4-07 d, e)
origine_terminee() {  # $1 : nom de la course d'origine
    local o="$RACINE/$1"
    [ -f "$RACINE/.verrou-$1" ] && (exec 8<"$RACINE/.verrou-$1"; flock -n 8) || stop "course $1 absente ou encore en cours : $COURSE attend"
    [ -f "$o/manifeste-run.json" ] && grep -q '"generation": 0' "$o/archive/index.jsonl" 2>/dev/null \
        || stop "course $1 sans génération 0 archivée : rien à relancer (paires coupées)"
    [ -f "$RACINE/$1.cles.txt" ] || stop "$1.cles.txt absent : noms des clés de $1 inconnus"
    [ "$(cat "$RACINE/$1.cles.txt")" = "$CLES" ] || stop "clés : « $CLES » ici, « $(cat "$RACINE/$1.cles.txt") » pour $1 : conditions extérieures différentes (CE3-05, CE4-07 e)"
    python3 -I -B -c 'import json,sys; m=json.load(open(sys.argv[1])); sys.exit(0 if bool(m.get("cle_brave_presente")) == (sys.argv[2] == "oui") else 1)' \
        "$o/manifeste-run.json" "$BRAVE" || stop "clé Brave : présence différente de celle du manifeste de $1 (CE4-07 d)"
    python3 -I -B -c 'import json,sys; m=json.load(open(sys.argv[1])); sys.exit(0 if bool(m.get("cle_openalex_presente")) == (sys.argv[2] == "oui") else 1)' \
        "$o/manifeste-run.json" "$OPENALEX" || stop "clé OpenAlex : présence différente de celle du manifeste de $1 (R-415)"
    python3 -I -B -c 'import json,sys; m=json.load(open(sys.argv[1])); sys.exit(0 if bool(m.get("cle_semanticscholar_presente")) == (sys.argv[2] == "oui") else 1)' \
        "$o/manifeste-run.json" "$S2" || stop "clé Semantic Scholar : présence différente de celle du manifeste de $1 (R-417)"
    [ -f "$RACINE/$1.fin.json" ] && note "$1 : $(cat "$RACINE/$1.fin.json")" || note "$1 : fin non écrite (arrêt hors lanceur) ; $COURSE part de ce qu'elle a archivé"
}
COMMUNS=(--reel --go "$GO" --registre-go "$RACINE/registre-go-$COURSE.md" --taches "$EN/banque-confrontation-v1.json"
         --traits "$EN/traits/etape1-v1/traits-16384" --sortie "$SORTIE" --isoler-reseau --parallele-max 8 --relances-max 1
         --pas-max 5000 --delai-entrainement 60 --octets-max 40000000 --max-tokens-appel 4096 --decalage-uid "$DECALAGE")
ESPECES_CONTROLE="CLAUDE_FABLE_5_1 CLAUDE_OPUS_5_5 GEMINI_ARGON"
case "$COURSE" in
    repetition)
        ARGS=("${COMMUNS[@]}" --generations 1 --graine 1 --especes CLAUDE_FABLE_5_1 CLAUDE_OPUS_5_5 GEMINI_ARGON --appels-max 20
              --usd-par-generation 5 --temps-max 900 --entrainements-max 2 --recherches-max 2 --telechargements-max 1
              --rondes-conception-max 2 --usd-max-conception 2 --appels-max-conception 20 --temps-max-conception 900
              --pool-conception "$V_FICHIER" --question-ouverte "$Q_FICHIER" --question-ouverte-aux c001 --plafond-total 40) ;;
    repetition-B)
        origine_terminee repetition
        ARGS=("${COMMUNS[@]}" --depuis "$RACINE/repetition" --generations 1 --graine 1 --appels-max 20 --usd-par-generation 3
              --temps-max 900 --entrainements-max 0 --recherches-max 2 --telechargements-max 1 --plafond-total 10) ;;
    A1|A2)
        r=${COURSE#A}; g=$(graine "$r") || stop "graine_$r absente du préenregistrement (format « graine_$r = <entier> »)"
        ARGS=("${COMMUNS[@]}" --generations 3 --graine "$g" --especes CLAUDE_FABLE_5_1 CLAUDE_OPUS_5_5 GEMINI_ARGON --appels-max 160
              --usd-par-generation 20 --temps-max 1800 --entrainements-max 10 --recherches-max 10 --telechargements-max 4
              --rondes-conception-max 4 --usd-max-conception 12 --appels-max-conception 160 --temps-max-conception 1800
              --pool-conception "$V_FICHIER" --plafond-total 360) ;;  # sans question (R-410, CL8-01)
    B1|B2)
        r=${COURSE#B}; g=$(graine "$r") || stop "graine_$r absente du préenregistrement (format « graine_$r = <entier> »)"
        origine_terminee "A$r"
        ARGS=("${COMMUNS[@]}" --depuis "$RACINE/A$r" --generations 3 --graine "$g" --appels-max 160 --usd-par-generation 20
              --temps-max 1800 --entrainements-max 0 --recherches-max 10 --telechargements-max 4 --plafond-total 190) ;;
esac
if [ $CONTROLES = 1 ]; then
    note "contrôles : tout passe ; options : $(printf '%q ' "${ARGS[@]}" | sed "s#$RACINE#<courses>#g")"
    exit 0
fi
# 10. environnement du noyau : minimal, construit dans un sous-processus par des commandes internes (les valeurs des clés
# ne passent jamais par une ligne de commande, CE4-13) ; clé Anthropic choisie sous ANTHROPIC_API_KEY, en-tête d'espace
# de travail par ANTHROPIC_CUSTOM_HEADERS pour RR_ANTHROPIC_API_KEY seulement, ANTHROPIC_BASE_URL absente
# (GO-2026-10-24-04) ; aucune valeur affichée ni écrite
noyau_env() (
    garder=" HTTPS_PROXY https_proxy NO_PROXY no_proxy SSL_CERT_FILE REQUESTS_CA_BUNDLE "
    a_cle=$ANTHROPIC_CLE; a_esp=$ANTHROPIC_ESPACE; g_cle=$GEMINI_CLE; b_cle=${BRAVE_API_KEY:-}; o_cle=${OPENALEX_API_KEY:-}; s_cle=${SEMANTIC_SCHOLAR_API_KEY:-}
    for v in $(compgen -e); do case "$garder" in *" $v "*) ;; *) unset "$v" 2>/dev/null || true ;; esac; done
    export PATH=/usr/bin:/bin HOME="$RACINE" LANG=C.UTF-8
    export ANTHROPIC_API_KEY="$a_cle" GEMINI_API_KEY="$g_cle"
    if [ -n "$a_esp" ]; then export ANTHROPIC_CUSTOM_HEADERS="anthropic-workspace-id: $a_esp"; fi
    if [ -n "$b_cle" ]; then export BRAVE_API_KEY="$b_cle"; fi
    if [ -n "$o_cle" ]; then export OPENALEX_API_KEY="$o_cle"; fi   # R-415 : lue par le noyau seul
    if [ -n "$s_cle" ]; then export SEMANTIC_SCHOLAR_API_KEY="$s_cle"; fi   # R-417 : lue par le noyau seul
    # CL5-01 : le noyau cache au bac à sable de l'organisme le dépôt, ses objets git et l'arbre du code (ils portent la
    # banque et ses vérités, lisibles par tous sur l'hôte) ; /home, /root… sont cachés par défaut
    export ESSAIM_M3_CACHER="$DEPOT:$DEPOT_GIT:$CODE"
    exec "$@"
)
# 11. test de dépense par espèce (décision de Lazar, 25 octobre, 09:58 heure de Paris ; la recharge automatique est active) :
# un appel payant, consigne figée, 512 jetons au plus ; statut OK et jetons de sortie > 0 exigés, sinon la course ne part
# pas (un crédit épuisé, même sous HTTP 200, rend ECHEC_API : R-395) ; imputé à GO-2026-10-24-05 (R-403)
controle=$(cd "$CODE/essaim-m3-refonte-v1" && noyau_env "$VENV/bin/python" -B - "$RACINE/controle-especes-$COURSE" "$GO_CONTROLE" $ESPECES_CONTROLE <<'PY'
import json, sys
from essaim_m3.noyau.appels import Appelant, charger_collisionneur
cv = charger_collisionneur()
a = Appelant(sys.argv[1], 0.50, cv.APPELANTS, reel=True, go_id=sys.argv[2])
sortie = {}
for e in sys.argv[3:]:
    r = a.appeler(e, "controle", "Réponds par le seul mot : prêt.", max_tokens=512)
    sortie[e] = {"statut": r.statut, "modele_servi": r.modele_servi, "cout_usd": r.cout_usd,
                 "jetons_sortie": int((r.usage or {}).get("sortie") or 0)}
print(json.dumps({"especes": sortie, "cout_usd": round(a.depense_usd, 4), "go": sys.argv[2]}, ensure_ascii=False))
sys.exit(0 if all(v["statut"] == "OK" and v["jetons_sortie"] > 0 for v in sortie.values()) else 1)
PY
) || stop "appel de contrôle en échec : ${controle:-sans sortie}"
note "appel de contrôle : $controle"
# noms des clés de la course, écrits une fois (lus par le bras B, CE4-07 e)
( set -o noclobber; printf '%s\n' "$CLES" > "$RACINE/$COURSE.cles.txt" ) || stop "$COURSE.cles.txt existe déjà (R12)"
note "départ : $(printf '%q ' "${ARGS[@]}" | sed "s#$RACINE#<courses>#g")"
# 12. course ; sortie du noyau et erreurs scellées en 0600, jamais affichées ; fin écrite quoi qu'il arrive au lanceur
fin() {
    local code=$?
    printf '{"course": "%s", "code": %d, "fin_utc": "%s", "hote": "%s"}\n' "$COURSE" "$code" "$(date -u +%FT%TZ)" "$HOTE" > "$RACINE/$COURSE.fin.json"
    for f in "$COURSE.sortie.json" "$COURSE.erreurs.txt" "$COURSE.fin.json"; do
        [ -f "$RACINE/$f" ] && (cd "$RACINE" && sha256sum "$f" > "$f.sha256")
    done
    note "fin, code $code"
}
trap fin EXIT
set +e
(cd "$CODE/essaim-m3-refonte-v1" && noyau_env "$VENV/bin/python" -B -m essaim_m3 lancer "${ARGS[@]}") \
    > "$RACINE/$COURSE.sortie.json" 2> "$RACINE/$COURSE.erreurs.txt"
code=$?
set -e
# statuts : extrait mécanique sans aucun score (v2 : statuts des services, rondes importées marquées), écrit hors de la
# course, scellé ; résumé par génération dans le journal
if (cd "$CODE/essaim-m3-refonte-v1" && env -i PATH=/usr/bin:/bin HOME="$RACINE" LANG=C.UTF-8 "$VENV/bin/python" -B -m essaim_m3.outils.extrait_mecanique \
        --course "$SORTIE" --sortie "$RACINE/$COURSE.extrait-mecanique.json") > "$RACINE/$COURSE.extrait.txt" 2>&1; then
    python3 -I -B - "$RACINE/$COURSE.extrait-mecanique.json" <<'PY' | tee -a "$J" || true
import json, sys
d = json.load(open(sys.argv[1], encoding="utf-8"))
for g in d.get("generations", []):
    print("statut :", {k: g.get(k) for k in ("lignee", "phase", "generation", "statut", "importee", "invalide", "n_appels", "services")})
print("totaux hors importées :", d.get("totaux_hors_importees"))
PY
else
    note "extrait mécanique impossible : $(tail -1 "$RACINE/$COURSE.extrait.txt")"
fi
# porte mécanique d'une répétition (CE4-04 (2)), écrite une fois et scellée ; lue avant toute course décisive
case "$COURSE" in repetition|repetition-B)
    python3 -I -B - "$RACINE/$COURSE.extrait-mecanique.json" "$COURSE" "$code" "$HOTE" $ESPECES_CONTROLE > "$RACINE/$COURSE.porte.json.neuf" <<'PY' || true
import json, sys
chemin, course, code, hote, especes = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4], sys.argv[5:]
raisons, info = [], {}
try:
    e = json.load(open(chemin, encoding="utf-8"))
except (OSError, ValueError):
    e, raisons = {}, ["extrait mécanique absent ou illisible"]
if code != 0:
    raisons.append(f"noyau sorti avec le code {code}")
attendu = "ORGANISME_VALIDE" if course == "repetition" else "ORGANISME_IMPOSE_VALIDE"
amorcage = {x.get("lignee"): x.get("statut") for x in e.get("evenements", []) if x.get("etape") == "amorcage"}
gens = [g for g in e.get("generations", []) if not g.get("importee")]
totaux = {"entrainements": [0, 0], "recherches": [0, 0], "telechargements": [0, 0]}
for esp in especes:
    lignee = esp.lower().replace("_", "-")
    if amorcage.get(lignee) != attendu:
        raisons.append(f"{lignee} : amorçage {amorcage.get(lignee)} (attendu {attendu})")
    g0 = [g for g in gens if g.get("lignee") == lignee and g.get("generation") == 0 and not g.get("phase")]
    if not g0 or g0[0].get("invalide"):
        raisons.append(f"{lignee} : aucune génération 0 valide archivée")
    else:
        info[lignee] = {k: g0[0].get(k) for k in ("statut", "n_reponses_test", "indisponibles", "n_appels")}
    if course == "repetition":  # R-393 : question posée à c001, et à aucune autre ronde ni génération de la lignée
        posees = sorted((g.get("phase") or "", g.get("generation")) for g in gens if g.get("lignee") == lignee
                        and (g.get("question_ouverte") or {}).get("posee") is True)
        if posees != [("conception", 1)]:
            raisons.append(f"{lignee} : question posée à {posees} (attendu : c001 seulement)")
        c1 = [g for g in gens if g.get("lignee") == lignee and g.get("phase") == "conception" and g.get("generation") == 1]
        info.setdefault(lignee, {})["reponse_question_c001"] = bool(c1 and (c1[0].get("question_ouverte") or {}).get("reponse"))
for g in gens:
    s = g.get("services") or {}
    for k in ("entrainements", "telechargements"):
        totaux[k][0] += sum((s.get(k) or {}).values()); totaux[k][1] += (s.get(k) or {}).get("OK", 0)
    for src in (s.get("recherches") or {}).values():
        totaux["recherches"][0] += sum(src.values()); totaux["recherches"][1] += src.get("OK", 0)
for k, (n, ok) in totaux.items():
    if n > 0 and ok == 0:
        raisons.append(f"{k} : {n} demandés, aucun OK")
# appels des organismes par espèce et par statut, et plafonds demandés (journal du noyau, via l'extrait) : rapportés sans
# condition (un appel coupé peut venir du plafond choisi par l'organisme, CL5-10) ; vérification humaine avant les courses
appels, plafonds, reflexion = {}, {}, {}
for g in gens:
    a = g.get("appels") or {}
    for esp, e in (a.get("par_espece") or {}).items():
        for st, n in (e.get("par_statut") or {}).items():
            appels.setdefault(esp, {})[st] = appels.setdefault(esp, {}).get(st, 0) + int(n)
        for st, n in (e.get("reflexion_par_statut") or {}).items():  # R-402 : appels qui ont réfléchi, par statut
            reflexion.setdefault(esp, {})[st] = reflexion.setdefault(esp, {}).get(st, 0) + int(n)
    for mt, n in (a.get("max_tokens_demandes") or {}).items():
        plafonds[mt] = plafonds.get(mt, 0) + int(n)
print(json.dumps({"course": course, "hote": hote, "reussie": not raisons, "raisons": raisons, "services": totaux, "info": info,
                  "appels_par_espece": appels, "max_tokens_demandes": plafonds, "reflexion_par_espece": reflexion}, ensure_ascii=False))
PY
    if [ -s "$RACINE/$COURSE.porte.json.neuf" ] && [ ! -e "$RACINE/$COURSE.porte.json" ]; then
        mv "$RACINE/$COURSE.porte.json.neuf" "$RACINE/$COURSE.porte.json"
        (cd "$RACINE" && sha256sum "$COURSE.porte.json" > "$COURSE.porte.json.sha256")
        note "porte : $(cat "$RACINE/$COURSE.porte.json")"
    else
        note "porte : non écrite (calcul impossible ou porte déjà écrite)"
    fi ;;
esac
exit $code
