#!/usr/bin/env bash
# Lanceur des courses réelles de l'étape 1 du programme « gradient conçu par l'essaim », version 2, pour la v4
# « économe » du préenregistrement (`prereg/gradient-etape1-sondes-v4.md`, scellé ; GO-2026-10-24-05). Écrit par la
# lignée « session-depot » le 24 octobre 2026, décliné de `lancer_courses_etape1_v1.sh` sous un nom nouveau (R12), avec
# les corrections de la contre-lecture n° 3 (CE3-05, CE3-06, CE3-08, CE3-09, CE3-13, CE3-15) et de la relecture de
# « conv-audit » (RE-02, RE-05). Indépendant de l'hôte : il tourne sur la machine retenue par Lazar, en root, où le
# noyau vérifie lui-même l'isolation. Une course par appel :
#   repetition  répétition mécanique (Plan d'analyse, point 8) : lignées CLAUDE_OPUS_5_5 et GEMINI_ARGON, deux rondes de
#               conception à 2 USD, une génération à 3 USD, 20 appels, 900 s, deux entraînements de 60 s, moisson
#               réduite (2 recherches, 1 téléchargement), vivier servi, plafond 25 USD ; exclue de toute analyse ;
#   A1, A2      bras avec gradient, réplique 1 ou 2 (point 3) ;
#   B1, B2      bras sans gradient, `--depuis` la course A de même réplique (point 3), une fois A terminée.
# Contrôles avant tout appel payant (code 2 si l'un échoue, avec une note dans `lancements.txt`) :
#   hôte (root, `unshare` réseau et espaces de noms, `fs.protected_hardlinks`) ;
#   préenregistrement scellé et conforme (validateur du dépôt) qui cite le commit ; code à ce commit, arbre propre ;
#   dossier des courses à root en 0700 (CE3-06) ; entrées aux empreintes citées (banque, traits extraits avec
#   `--strip-components=2` : CE3-08 ; vivier lu dans le préenregistrement) ; ligne d'engagement de la course dans
#   `registres/depenses.md` (CE3-15) ; GO de calcul accepté par la garde ; clés présentes (jamais affichées ; clé Gemini
#   n° 2 si elle existe, sinon n° 1 : GO-2026-10-24-07) ; présence de la clé Brave consignée, et la même que celle du
#   bras A pour un bras B (CE3-05) ; sortie neuve (R12) ; verrou propre à la course ; pour un bras B, course A
#   terminée (son verrou libre) avec au moins une génération 0 archivée ; graines lues au format littéral
#   « graine_r = <entier> » (CE3-09, CE3-16) ; appel de contrôle par espèce de la course, statut OK exigé.
# Sorties : `<course>.sortie.json` (sortie du noyau : courbes et scores) en 0600, scellée, jamais ouverte avant la
# lecture ; le lanceur n'affiche que l'extrait mécanique sans score (`<course>.extrait-mecanique.json`, CE3-13) ; `<course>.fin.json` écrit à la
# sortie du lanceur, quelle qu'elle soit (un arrêt de l'hôte n'en écrit pas : course arrêtée, consignée, lue à la
# dernière génération valide commune, aucune relance).
# Mode `--controles` : tous les contrôles, sans appel de contrôle ni course (code 0 si tout passe) : répétition à sec.
# Codes : 0 course finie ; 2 arrêt avant la course ; autre : code de sortie du noyau.
# Usage : [CODE_ETAPE1=<dossier de travail git> COMMIT_ETAPE1=<commit>] lancer_courses_etape1_v2.sh [--controles] COURSE DOSSIER_DES_COURSES
set -euo pipefail
umask 077
CONTROLES=0
if [ "${1:-}" = "--controles" ]; then CONTROLES=1; shift; fi
[ $# -eq 2 ] || { echo "usage : lancer_courses_etape1_v2.sh [--controles] {repetition|A1|A2|B1|B2} DOSSIER_DES_COURSES"; exit 2; }
COURSE=$1; RACINE=$(realpath -m "$2")
DEPOT=${DEPOT_ETAPE1:-/home/user/controle-ia-travail}
DEPOT_GIT=${DEPOT_GIT_ETAPE1:-$DEPOT}   # objets git des entrées (essais du lanceur : un clone partagé)
CODE=${CODE_ETAPE1:?CODE_ETAPE1 : dossier de travail git de outils/essaim-m3-gradient-v2-travail}
COMMIT=${COMMIT_ETAPE1:?COMMIT_ETAPE1 : commit cité par le préenregistrement scellé}
VENV=${VENV_ETAPE1:-/opt/essaim-m3-venv-v1}
PREREG=prereg/gradient-etape1-sondes-v4.md
GO=GO-2026-10-24-05
E_BANQUE=f1387a20cb272d2e8c205102147dfee71cd1d372f7f5d2ad4ff8233783cc83cc
E_TRAITS=add13e090a13b60e48983393ae376cc9df2542210b5328bc2abd94e661e25f17
case "$COURSE" in repetition) DECALAGE=500 ;; A1) DECALAGE=100 ;; A2) DECALAGE=200 ;; B1) DECALAGE=300 ;; B2) DECALAGE=400 ;;
    *) echo "course inconnue : $COURSE"; exit 2 ;; esac
[[ "$COMMIT" =~ ^[0-9a-f]{40}$ ]] || { echo "COMMIT_ETAPE1 : 40 caractères hexadécimaux attendus"; exit 2; }
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
# 1. hôte : isolation et protections du système de fichiers
unshare -n true 2>/dev/null || stop "hôte : unshare -n refusé (isolation réseau impossible) : hôte inadapté"
unshare --mount --pid --fork --kill-child --mount-proc true 2>/dev/null || stop "hôte : espaces de noms de montage et de processus refusés"
[ "$(cat /proc/sys/fs/protected_hardlinks 2>/dev/null)" = 1 ] || stop "hôte : fs.protected_hardlinks doit valoir 1"
note "hôte : $(uname -r) ; $(nproc) cœurs ; $(df -h "$RACINE" | awk 'NR==2{print $4}') libres ; protected_symlinks=$(cat /proc/sys/fs/protected_symlinks 2>/dev/null)"
# 2. préenregistrement scellé et conforme, qui cite le commit
python3 -I -B - "$DEPOT/src" "$DEPOT/$PREREG" > "$RACINE/.prereg-$COURSE.txt" 2>&1 <<'PY' || stop "préenregistrement non scellé ou non conforme : $(tail -1 "$RACINE/.prereg-$COURSE.txt")"
import sys
sys.path.insert(0, sys.argv[1])
from controle_ia import prereg
print(prereg.exiger_prereg_scelle(sys.argv[2]))
PY
grep -qF "$COMMIT" "$DEPOT/$PREREG" || stop "le préenregistrement ne cite pas le commit $COMMIT"
note "préenregistrement scellé $(head -c 16 "$RACINE/.prereg-$COURSE.txt")…"
# valeur littérale « nom = valeur » hors bloc de code (CE3-16) ; vide si absente
litteral() { grep -oE "(^|[[:space:]])$1 = [0-9a-zA-Z_./:-]+" "$DEPOT/$PREREG" | head -1 | sed -E "s/.*$1 = //" || true; }
# 3. code au commit cité, arbre propre
[ "$(git -C "$CODE" rev-parse HEAD)" = "$COMMIT" ] || stop "code : HEAD $(git -C "$CODE" rev-parse HEAD) ≠ $COMMIT"
[ -z "$(git -C "$CODE" status --porcelain --untracked-files=no)" ] || stop "code : arbre de travail modifié"
# 4. entrées aux empreintes citées (extraites une fois dans RACINE/entrees, jamais réécrites)
V_COMMIT=$(litteral vivier_commit); V_CHEMIN=$(litteral vivier_chemin); E_VIVIER=$(litteral vivier_sha256)
[[ "$V_COMMIT" =~ ^[0-9a-f]{40}$ ]] && [ -n "$V_CHEMIN" ] && [[ "$E_VIVIER" =~ ^[0-9a-f]{64}$ ]] \
    || stop "vivier : vivier_commit, vivier_chemin ou vivier_sha256 absent du préenregistrement"
EN="$RACINE/entrees"
if [ ! -e "$EN/pret" ]; then
    rm -rf "$EN"; mkdir -p -m 0700 "$EN" "$EN/traits" "$EN/vivier"
    git -C "$DEPOT_GIT" show bffe03c:essaim-m3-refonte-v1/banque/banque-confrontation-v1.json > "$EN/banque-confrontation-v1.json"
    git -C "$DEPOT_GIT" show bffe03c:essaim-m3-refonte-v1/banque/banque-confrontation-v1.json.sha256 > "$EN/banque-confrontation-v1.json.sha256"
    git -C "$DEPOT_GIT" archive 6479769 essaim-m3-refonte-v1/traits/etape1-v1 | tar -x -C "$EN/traits" --strip-components=2
    V_NOM=$(basename "$V_CHEMIN")
    git -C "$DEPOT_GIT" show "$V_COMMIT:$V_CHEMIN" > "$EN/vivier/$V_NOM"
    git -C "$DEPOT_GIT" show "$V_COMMIT:$V_CHEMIN.sha256" > "$EN/vivier/$V_NOM.sha256"
    touch "$EN/pret"
fi
V_FICHIER="$EN/vivier/$(basename "$V_CHEMIN")"
[ "$(sha256sum "$EN/banque-confrontation-v1.json" | cut -d' ' -f1)" = "$E_BANQUE" ] || stop "banque : empreinte différente"
[ -f "$EN/traits/etape1-v1/EMPREINTES-traits-etape1-v1.txt" ] && [ "$(sha256sum "$EN/traits/etape1-v1/EMPREINTES-traits-etape1-v1.txt" | cut -d' ' -f1)" = "$E_TRAITS" ] \
    || stop "traits : empreintes différentes"
(cd "$EN/traits/etape1-v1" && sha256sum -c --quiet EMPREINTES-traits-etape1-v1.txt) || stop "traits : un fichier diffère de ses empreintes"
[ -f "$V_FICHIER" ] && [ "$(sha256sum "$V_FICHIER" | cut -d' ' -f1)" = "$E_VIVIER" ] || stop "vivier : empreinte différente de vivier_sha256"
chmod -R go-rwx "$EN"
# 5. engagement de la course consigné avant (GO-2026-10-24-05, CE3-15)
if grep -qF "engagement : course $COURSE de l'étape 1" "$DEPOT/registres/depenses.md"; then
    note "engagement consigné dans registres/depenses.md"
elif [ $CONTROLES = 1 ]; then
    note "engagement : absent de registres/depenses.md (non exigé en mode contrôles ; exigé avant la course)"
else
    stop "aucune ligne « engagement : course $COURSE de l'étape 1 » dans registres/depenses.md"
fi
# 6. garde de calcul rejouée avec le GO ; extrait du registre
cp "$DEPOT/registres/go.md" "$RACINE/registre-go-$COURSE.md"
printf '{"tool_input":{"command":"GO_ID=%s vastai create instance 0"}}' "$GO" | python3 -I -B "$DEPOT/.claude/hooks/garde_calcul.py" 2>/dev/null \
    || stop "garde de calcul : $GO refusé"
# 7. clés présentes, jamais affichées ; clé Gemini n° 2 si elle existe ; clé Brave : présence consignée
GEMINI_NOM=GEMINI_API_KEY_2; [ -n "${GEMINI_API_KEY_2:-}" ] || GEMINI_NOM=GEMINI_API_KEY
GEMINI_CLE=${!GEMINI_NOM:-}
[ -n "${RR_ANTHROPIC_API_KEY:-}" ] && [ -n "${RR_ANTHROPIC_WORKSPACE_ID:-}" ] && [ -n "$GEMINI_CLE" ] \
    || stop "clé absente (RR_ANTHROPIC_API_KEY, RR_ANTHROPIC_WORKSPACE_ID, GEMINI_API_KEY_2 ou GEMINI_API_KEY)"
BRAVE=non; [ -n "${BRAVE_API_KEY:-}" ] && BRAVE=oui
note "clés : Anthropic (RR_ANTHROPIC_API_KEY, en-tête d'espace de travail) ; Gemini ($GEMINI_NOM) ; Brave : $BRAVE"
# 8. sortie neuve (R12) ; verrou propre à la course, tenu jusqu'à la fin du noyau
SORTIE="$RACINE/$COURSE"
[ -e "$SORTIE" ] && stop "$SORTIE existe déjà (R12)"
exec 9>"$RACINE/.verrou-$COURSE"
flock -n 9 || stop "course $COURSE déjà en cours (verrou tenu)"
# 9. paramètres de la course (Plan d'analyse, points 3, 4, 5, 8)
graine() { local g; g=$(litteral "graine_$1"); [[ "$g" =~ ^[0-9]+$ ]] && printf '%s' "$g"; }
COMMUNS=(--reel --go "$GO" --registre-go "$RACINE/registre-go-$COURSE.md" --taches "$EN/banque-confrontation-v1.json"
         --traits "$EN/traits/etape1-v1/traits-16384" --sortie "$SORTIE" --isoler-reseau --parallele-max 8 --relances-max 1
         --pas-max 5000 --delai-entrainement 60 --octets-max 40000000 --max-tokens-appel 4096 --decalage-uid "$DECALAGE")
case "$COURSE" in
    repetition)
        ESPECES_CONTROLE="CLAUDE_OPUS_5_5 GEMINI_ARGON"
        ARGS=("${COMMUNS[@]}" --generations 1 --graine 1 --especes CLAUDE_OPUS_5_5 GEMINI_ARGON --appels-max 20 --usd-par-generation 3
              --temps-max 900 --entrainements-max 2 --recherches-max 2 --telechargements-max 1 --rondes-conception-max 2
              --usd-max-conception 2 --appels-max-conception 20 --temps-max-conception 900 --pool-conception "$V_FICHIER"
              --plafond-total 25) ;;
    A1|A2)
        r=${COURSE#A}; g=$(graine "$r") || stop "graine_$r absente du préenregistrement (format « graine_$r = <entier> »)"
        ESPECES_CONTROLE="CLAUDE_FABLE_5_1 CLAUDE_OPUS_5_5 GEMINI_ARGON"
        ARGS=("${COMMUNS[@]}" --generations 3 --graine "$g" --especes CLAUDE_FABLE_5_1 CLAUDE_OPUS_5_5 GEMINI_ARGON --appels-max 160
              --usd-par-generation 20 --temps-max 1800 --entrainements-max 10 --recherches-max 10 --telechargements-max 4
              --rondes-conception-max 4 --usd-max-conception 12 --appels-max-conception 160 --temps-max-conception 1800
              --pool-conception "$V_FICHIER" --plafond-total 360) ;;
    B1|B2)
        r=${COURSE#B}; g=$(graine "$r") || stop "graine_$r absente du préenregistrement (format « graine_$r = <entier> »)"
        ESPECES_CONTROLE="CLAUDE_FABLE_5_1 CLAUDE_OPUS_5_5 GEMINI_ARGON"
        ORIGINE="$RACINE/A$r"
        [ -f "$RACINE/.verrou-A$r" ] && (exec 8<"$RACINE/.verrou-A$r"; flock -n 8) || stop "course A$r absente ou encore en cours : le bras B$r attend"
        [ -f "$ORIGINE/manifeste-run.json" ] && grep -q '"generation": 0' "$ORIGINE/archive/index.jsonl" 2>/dev/null \
            || stop "course A$r sans génération 0 archivée : rien à relancer (paires coupées)"
        grep -qF "A$r : clés : " "$J" && ! grep -F "A$r : clés : " "$J" | tail -1 | grep -qF "Brave : $BRAVE" \
            && stop "clé Brave : présence différente de celle de A$r (CE3-05)"
        [ -f "$RACINE/A$r.fin.json" ] && note "A$r : $(cat "$RACINE/A$r.fin.json")" || note "A$r : fin non écrite (arrêt hors lanceur) ; B$r part de ce qu'elle a archivé"
        ARGS=("${COMMUNS[@]}" --depuis "$ORIGINE" --generations 3 --graine "$g" --appels-max 160 --usd-par-generation 20
              --temps-max 1800 --entrainements-max 0 --recherches-max 10 --telechargements-max 4 --plafond-total 190) ;;
esac
if [ $CONTROLES = 1 ]; then
    note "contrôles : tout passe ; options : $(printf '%q ' "${ARGS[@]}" | sed "s#$RACINE#<courses>#g")"
    exit 0
fi
# 10. environnement du noyau : minimal ; clé Anthropic des runs sous ANTHROPIC_API_KEY, en-tête d'espace de travail par
# ANTHROPIC_CUSTOM_HEADERS, ANTHROPIC_BASE_URL absente (GO-2026-10-24-04) ; aucune valeur affichée ni écrite
noyau_env() {
    env -i PATH=/usr/bin:/bin HOME="$RACINE" LANG=C.UTF-8 \
        HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" \
        SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" \
        ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY" ANTHROPIC_CUSTOM_HEADERS="anthropic-workspace-id: $RR_ANTHROPIC_WORKSPACE_ID" \
        GEMINI_API_KEY="$GEMINI_CLE" ${BRAVE_API_KEY:+BRAVE_API_KEY="$BRAVE_API_KEY"} "$@"
}
# 11. appel de contrôle par espèce de la course (statut OK exigé, sinon la course ne part pas) ; coût consigné
controle=$(cd "$CODE/essaim-m3-refonte-v1" && noyau_env "$VENV/bin/python" -B - "$RACINE/controle-especes-$COURSE" "$GO" $ESPECES_CONTROLE <<'PY'
import json, sys
from essaim_m3.noyau.appels import Appelant, charger_collisionneur
cv = charger_collisionneur()
a = Appelant(sys.argv[1], 0.50, cv.APPELANTS, reel=True, go_id=sys.argv[2])
sortie = {}
for e in sys.argv[3:]:
    r = a.appeler(e, "controle", "Réponds par le seul mot : prêt.", max_tokens=512)
    sortie[e] = {"statut": r.statut, "modele_servi": r.modele_servi, "cout_usd": r.cout_usd}
print(json.dumps({"especes": sortie, "cout_usd": round(a.depense_usd, 4)}, ensure_ascii=False))
sys.exit(0 if all(v["statut"] == "OK" for v in sortie.values()) else 1)
PY
) || stop "appel de contrôle en échec : ${controle:-sans sortie}"
note "appel de contrôle : $controle"
note "départ : $(printf '%q ' "${ARGS[@]}" | sed "s#$RACINE#<courses>#g")"
# 12. course ; sortie du noyau scellée en 0600, jamais affichée ; fin écrite quoi qu'il arrive au lanceur
fin() {
    local code=$?
    printf '{"course": "%s", "code": %d, "fin_utc": "%s"}\n' "$COURSE" "$code" "$(date -u +%FT%TZ)" > "$RACINE/$COURSE.fin.json"
    [ -f "$RACINE/$COURSE.sortie.json" ] && (cd "$RACINE" && sha256sum "$COURSE.sortie.json" > "$COURSE.sortie.json.sha256")
    note "fin, code $code"
}
trap fin EXIT
set +e
(cd "$CODE/essaim-m3-refonte-v1" && noyau_env "$VENV/bin/python" -B -m essaim_m3 lancer "${ARGS[@]}") \
    > "$RACINE/$COURSE.sortie.json" 2> "$RACINE/$COURSE.erreurs.txt"
code=$?
set -e
# statuts : extrait mécanique sans aucun score (`essaim_m3.outils.extrait_mecanique`, PG2-01 du pilote : listes closes et
# garde finale sur les noms de clés), écrit hors de la course, scellé ; résumé par génération dans le journal
if (cd "$CODE/essaim-m3-refonte-v1" && env -i PATH=/usr/bin:/bin HOME="$RACINE" LANG=C.UTF-8 "$VENV/bin/python" -B -m essaim_m3.outils.extrait_mecanique \
        --course "$SORTIE" --sortie "$RACINE/$COURSE.extrait-mecanique.json") > "$RACINE/$COURSE.extrait.txt" 2>&1; then
    python3 -I -B - "$RACINE/$COURSE.extrait-mecanique.json" <<'PY' | tee -a "$J" || true
import json, sys
d = json.load(open(sys.argv[1], encoding="utf-8"))
for g in d.get("generations", []):
    print("statut :", {k: g.get(k) for k in ("lignee", "phase", "generation", "statut", "importee", "invalide", "cout_usd", "n_appels")})
PY
else
    note "extrait mécanique impossible : $(tail -1 "$RACINE/$COURSE.extrait.txt")"
fi
exit $code
