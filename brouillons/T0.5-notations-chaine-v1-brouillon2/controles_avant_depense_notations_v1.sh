#!/usr/bin/env bash
# Contrôles avant dépense des notations décisives refaites du pilote de T0.5 (N-021, option (a), GO-2026-10-12-02 ;
# préenregistrement complémentaire prereg/T0.5-pilote-notations-v1.md), v1, déclinés des contrôles du pilote
# (docs/procedures/pilote-T0.5-v1/controles_avant_depense_pilote_v1.sh) selon l'état des lieux de la voie « notations
# seules » (brouillons/T0.5-notations-seules-etat-des-lieux-v1/chaine.md, section 4 ; critique adverse, constats 10 à
# 15). Sur un clone neuf du dépôt de travail au commit de scellement S ; aucun calcul payant ; code 0 si et seulement si
# tout est conforme ; code 2 si les épingles manquent ou sont mal formées, ou si le clone est impossible.
# Ce qui est contrôlé : S ajoute le sceau du préenregistrement et n'ajoute que le préenregistrement, la configuration et
# leurs sceaux ; commit du code cité une seule fois, ancêtre de S, arbre gelé identique au code cité et au code relu
# épinglé ; modules de lecture du pilote égaux au commit cité par le pilote (gel prolongé, R-160) ; empreintes des deux
# scripts de l'instance citées ; pièces du pilote présentes, scellées et citées par leur empreinte ; décision de Lazar
# sur N-021 (GO de type « revendication », accordé par Lazar, option (a), non révoqué ; colonne d'état de N-021 à la
# forme exacte ; ligne R-…) ; texte de S égal au candidat relu, octet pour octet ; configuration de S égale à la
# configuration relue ; rapports de la contre-lecture présents, scellés, cités, seuls de leur famille ; journal de la
# répétition jouet ; branche de résultats absente (relance : …-v1 sans fichier de notations) ; ligne « Lancement » ;
# problemes() vide ; sceaux ; verifier-arbre ; gardes du lanceur des notations rejouées jusqu'au manifeste (état du
# pilote, paramètres et versions égaux, 180 notations par juge, graines égales clé à clé) ; première lecture (juges en
# nœud) ; format des vrais tokeniseurs égal à celui, scellé, du début du pilote ; suite complète des tests au commit S
# dans l'environnement neuf ; garde de calcul ; lecture précoce du script de l'instance (citations uniques).
# Usage : controles_avant_depense_notations_v1.sh S DOSSIER_NEUF [relance]
# « relance » : relancement unique (préenregistrement, Critères de lecture gelés) : la branche …-v1 existe sans aucun
# fichier de notations, …-v2 est absente.
set -uo pipefail
S=${1:-}; D=$(realpath -m "${2:-}"); MODE_LANCEMENT=${3:-premier}
DEPOT=https://github.com/lciric/controle-ia-travail.git
CANDIDAT_RELU=A_EPINGLER                                     # texte relu et vérifié (contre-lecture R2), octet pour octet
CANDIDAT_RELU_CHEMIN=A_EPINGLER
CONFIG_RELUE=A_EPINGLER                                      # configuration relue, octet pour octet
CONFIG_RELUE_CHEMIN=A_EPINGLER
RAPPORTS_ATTENDUS="A_EPINGLER"                               # paires nom=empreinte (contre-lecture R2 et vérifications)
CODE_RELU=A_EPINGLER                                         # commit du code relu : arbre gelé de S égal
REPETITION_JOUET=A_EPINGLER                                  # empreinte du journal de la répétition jouet au code relu
REPETITION_JOUET_CHEMIN=docs/procedures/notations-T0.5-v1/repetition-jouet-notations-v1.log
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
VERSEES=docs/procedures/notations-T0.5-v1
P=prereg/T0.5-pilote-notations-v1.md; CFG=prereg/T0.5-pilote-notations-config-v1.json
PILOTE=20261012-105125-t05-pilote-reel; ANALYSE=20261012-150724-t05-pilote-analyse
CODE_PILOTE=2660b07220ec011674f871c47fd14a2cdd840fd7         # commit du code cité par le pilote (modules de lecture gelés)
TACHES=donnees/t05-pilote-v1/taches-pilote-60-v1.json
PREREG_PILOTE=prereg/T0.5-pilote-8B-v1.md; CONFIG_PILOTE=prereg/T0.5-pilote-config-v1.json
VERDICT=docs/verdicts/verdict-T0.5-pilote-v1.md; AUDIT=docs/verdicts/audit-R4-T0.5-pilote-v1.md
PROPOSITION=docs/decisions/proposition-N-021-notations-seules-v1.md
AMORCE=scripts/amorce_instance_t05_notations.sh; INSTANCE=scripts/notations_t05_instance.sh
case "$MODE_LANCEMENT" in premier) BRANCHE=calcul/t05-notations-reel-v1 ;; relance) BRANCHE=calcul/t05-notations-reel-v2 ;;
    *) echo "troisième argument : relance, ou rien"; exit 2 ;; esac
echec=0; ok() { echo "OK  $*"; }; ko() { echo "KO  $*"; echec=1; }
[[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "S invalide"; exit 2; }
[ -n "${2:-}" ] || { echo "dossier neuf absent"; exit 2; }
[ -e "$D" ] && { echo "$D existe déjà"; exit 2; }
[[ "$CODE_RELU" =~ ^[0-9a-f]{40}$ && "$REPETITION_JOUET" =~ ^[0-9a-f]{64}$ ]] || { echo "code relu ou répétition jouet non épinglés"; exit 2; }
[[ "$CANDIDAT_RELU" =~ ^[0-9a-f]{64}$ && "$CANDIDAT_RELU_CHEMIN" == brouillons/* ]] || { echo "candidat relu non épinglé"; exit 2; }
[[ "$CONFIG_RELUE" =~ ^[0-9a-f]{64}$ && "$CONFIG_RELUE_CHEMIN" == brouillons/* ]] || { echo "configuration relue non épinglée"; exit 2; }
n_paires=0
for paire in $RAPPORTS_ATTENDUS; do [[ "$paire" =~ ^T0\.5-notations-v1-relecture-[a-z0-9-]+-v1\.(md|json|tar)=[0-9a-f]{64}$ ]] \
    || { echo "rapports attendus mal formés : $paire"; exit 2; }; n_paires=$((n_paires+1)); done
[ "$n_paires" -ge 2 ] || { echo "rapports attendus : au moins le rapport de la contre-lecture et ses fichiers de travail"; exit 2; }
W="$D.travail"                                   # fichiers de travail dans un dossier neuf, à côté du clone
[ -e "$W" ] && { echo "$W existe déjà"; exit 2; }
mkdir -p "$W" || exit 2
trap 'rm -rf "$W"' EXIT                          # fichiers de travail jamais laissés, même sur un arrêt précoce
git clone -q "$DEPOT" "$D" || { echo "clonage impossible"; exit 2; }
cd "$D" && git checkout -q "$S" || { echo "commit $S introuvable"; exit 2; }
# 1. contenu de S
[ "$(git log --diff-filter=A -1 --format=%H -- "$P.sha256")" = "$S" ] && ok "S ajoute le sceau du préenregistrement" || ko "S n'est pas le commit qui ajoute $P.sha256"
attendus_s=$(printf '%s\n' "$CFG" "$CFG.sha256" "$P" "$P.sha256" | sort | tr '\n' ' ')
[ "$(git diff --name-only "$S^" "$S" | sort | tr '\n' ' ')" = "$attendus_s" ] && ok "S n'ajoute que le préenregistrement, la configuration et leurs sceaux" || ko "contenu de S inattendu : $(git diff --name-only "$S^" "$S" | tr '\n' ' ')"
# 2. commit du code : cité une seule fois (constat 12), ancêtre de S, arbre gelé identique au code cité et au code relu
NC=$(grep -c "Commit du code d'analyse : \`" "$P" || true)
CODE=$(sed -n "s/.*Commit du code d'analyse : \`\([0-9a-f]\{40\}\)\`.*/\1/p" "$P" | head -1)
if [ "$NC" = 1 ] && [[ "$CODE" =~ ^[0-9a-f]{40}$ ]] && git merge-base --is-ancestor "$CODE" "$S"; then ok "commit du code cité une fois, $CODE, ancêtre de S"
else ko "commit du code cité illisible, cité $NC fois, ou non ancêtre de S"; CODE=$S; fi
GELES=$(PYTHONPATH=src "$PY" -c "from controle_ia.harnais.validation_reelle import CHEMINS_GELES; print(' '.join(CHEMINS_GELES))" 2>/dev/null)
if [ -n "$GELES" ]; then
    # shellcheck disable=SC2086
    git diff --quiet "$CODE" "$S" -- $GELES; c=$?
    case $c in 0) ok "arbre gelé (CHEMINS_GELES) identique au commit du code" ;; 1) ko "arbre gelé modifié depuis le commit du code" ;;
               *) ko "comparaison de l'arbre gelé impossible (code $c)" ;; esac
    # shellcheck disable=SC2086
    git diff --quiet "$CODE_RELU" "$S" -- $GELES; c=$?
    case $c in 0) ok "arbre gelé de S = code relu épinglé ($CODE_RELU)" ;; 1) ko "arbre gelé de S ≠ code relu épinglé ($CODE_RELU)" ;;
               *) ko "comparaison au code relu impossible (code $c)" ;; esac
else ko "CHEMINS_GELES illisible"; fi
# modules de lecture du pilote : égaux au commit cité par le pilote, jusqu'au verdict complémentaire (R-160 ; constat 4)
MODULES=$(PYTHONPATH=src "$PY" -c "from controle_ia.environnements.lire_pilote import MODULES_LECTURE; print(' '.join(MODULES_LECTURE))" 2>/dev/null)
if [ -n "$MODULES" ]; then
    # shellcheck disable=SC2086
    git diff --quiet "$CODE_PILOTE" "$S" -- $MODULES; c=$?
    [ "$c" = 0 ] && ok "modules de lecture du pilote égaux au commit cité par le pilote (${CODE_PILOTE:0:12})" \
        || ko "modules de lecture du pilote modifiés depuis ${CODE_PILOTE:0:12} (code $c) : la lecture des notations s'arrêterait"
else ko "MODULES_LECTURE illisible"; fi
for f in "$AMORCE" "$INSTANCE"; do
    e=$(git show "$S:$f" 2>/dev/null | sha256sum | cut -d' ' -f1)
    grep -qF "\`$f\` (\`$e\`, sha256)" "$P" && ok "empreinte de $f citée ($e)" || ko "empreinte de $f ($e) non citée"
done
# 3. pièces : présentes à S avec leur sceau entier ; citées par leur empreinte
for f in "$CFG" "$TACHES" "$PREREG_PILOTE" "$CONFIG_PILOTE" "$VERDICT" "$AUDIT" "$PROPOSITION" "runs/$PILOTE/manifeste.json" \
         "diag/$PILOTE/episodes.json" "diag/$PILOTE/appariements.json" "diag/$PILOTE/arret.json" \
         "runs/$ANALYSE/manifeste.json" "diag/$ANALYSE/lecture.json"; do
    if git cat-file -e "$S:$f" 2>/dev/null && git cat-file -e "$S:$f.sha256" 2>/dev/null && \
       [ "$(git show "$S:$f.sha256")" = "$(git show "$S:$f" | sha256sum | cut -d' ' -f1)  $(basename "$f")" ]; then
        ok "$f et son sceau entier dans l'arbre de S"
    else ko "$f ou son sceau absent ou non conforme"; fi
done
for f in "$PREREG_PILOTE" "$VERDICT" "$AUDIT" "$PROPOSITION" "diag/$ANALYSE/lecture.json" "runs/$PILOTE/manifeste.json" \
         "diag/$PILOTE/episodes.json" "diag/$PILOTE/arret.json" "$TACHES"; do
    e=$(git show "$S:$f" | sha256sum | cut -d' ' -f1)
    grep -qF "\`$e\`" "$P" && ok "$f cité par son empreinte ($e)" || ko "$f non cité par son empreinte"
done
# 4. décision de Lazar sur N-021 : GO cité par S (une ligne de forme fixe), de type « revendication », accordé par Lazar,
# qui cite N-021 et l'option (a), sans ligne « révocation » qui le nomme ; GO de calcul non révoqué ; colonne d'état de
# N-021 à la forme exacte « tranché (a) par Lazar : GO (R-…) » ; ligne R-… qui le consigne
python3 - "$P" registres/go.md registres/decisions.md > "$W/bloc-go.txt" 2>&1 <<'PYGO' && ok "décision de Lazar sur N-021 : GO conforme, non révoqué, N-021 tranché (a), registre" || ko "décision de Lazar sur N-021 (GO, révocation, N-021 ou registre) : $(tail -1 "$W/bloc-go.txt")"
import re, sys
texte, go_md, dec_md = (open(f, encoding="utf-8").read() for f in sys.argv[1:4])
m = re.findall(r"^- Décision de Lazar sur N-021 : `(GO-\d{4}-\d{2}-\d{2}-\d{2})` \((R-\d{3,4})\)", texte, re.M)
assert len(m) == 1 and len(re.findall(r"^- Décision de Lazar sur N-021 :", texte, re.M)) == 1, "ligne « Décision de Lazar sur N-021 »"
go, reg = m[0]
lignes = go_md.split("\n")
c = [[x.strip() for x in l.strip().strip("|").split("|")] for l in lignes if l.startswith(f"| {go} |")]
assert len(c) == 1 and len(c[0]) == 8, f"{go} absent, en double ou mal formé"
assert c[0][2] == "revendication" and c[0][6] == "Lazar" and "N-021" in c[0][3] and "(a)" in c[0][3], f"{go} : {c[0][2]}, {c[0][6]}"
for g in (go, "GO-2026-10-04-08"):
    assert not [l for l in lignes if l.startswith("| GO-") and (lambda c: (len(c) == 8 and c[2].lower() == "révocation" and (g in c[3] or g in c[7])) or (len(c) != 8 and "révocation" in l.lower() and g in l))([x.strip() for x in l.strip().strip("|").split("|")])], f"{g} révoqué"
dec = dec_md.split("\n")
n21 = [l for l in dec if l.startswith("| N-021 |")]
assert len(n21) == 1, "N-021 absent ou en double"
etat = n21[0].rsplit("|", 2)[-2].strip()
assert re.fullmatch(rf"tranché \(a\) par Lazar : {re.escape(go)} \({re.escape(reg)}\)", etat), \
    f"N-021 : colonne d'état ≠ « tranché (a) par Lazar : {go} ({reg}) »"
r = [l for l in dec if l.startswith(f"| {reg} |")]
assert len(r) == 1 and go in r[0], f"{reg} absent, en double ou sans {go}"
print(f"GO {go} ({reg}) conforme")
PYGO
sed 's/^/    /' "$W/bloc-go.txt"
# 5. texte et configuration de S = candidat et configuration relus, versés et scellés à l'empreinte épinglée
[ "$(git show "$S:$CANDIDAT_RELU_CHEMIN" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$CANDIDAT_RELU" ] && \
    [ "$(git show "$S:$CANDIDAT_RELU_CHEMIN.sha256" 2>/dev/null)" = "$CANDIDAT_RELU  $(basename "$CANDIDAT_RELU_CHEMIN")" ] \
    && ok "candidat relu versé, scellé, à l'empreinte épinglée" || ko "candidat relu absent, non scellé ou d'empreinte différente"
[ "$(sha256sum "$P" | cut -d' ' -f1)" = "$CANDIDAT_RELU" ] && ok "préenregistrement de S = candidat relu, octet pour octet" || ko "préenregistrement de S ≠ candidat relu"
[ "$(git show "$S:$CONFIG_RELUE_CHEMIN" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$CONFIG_RELUE" ] && \
    [ "$(git show "$S:$CONFIG_RELUE_CHEMIN.sha256" 2>/dev/null)" = "$CONFIG_RELUE  $(basename "$CONFIG_RELUE_CHEMIN")" ] \
    && ok "configuration relue versée, scellée, à l'empreinte épinglée" || ko "configuration relue absente, non scellée ou d'empreinte différente"
[ "$(sha256sum "$CFG" | cut -d' ' -f1)" = "$CONFIG_RELUE" ] && ok "configuration de S = configuration relue, octet pour octet" || ko "configuration de S ≠ configuration relue"
# 6. journal de la répétition jouet : épinglé, scellé, au code relu ; passages et récupérations attendus, KO des
# artefacts compris ; scripts exécutés égaux à leurs copies versées à S
git show "$S:$REPETITION_JOUET_CHEMIN" > "$W/journal-repetition.txt" 2>/dev/null
python3 - "$CODE_RELU" "$W/journal-repetition.txt" > "$W/bloc-repetition.txt" 2>&1 <<'PYREP'
import re, sys
code = sys.argv[1]
lignes = open(sys.argv[2], encoding="utf-8").read().split("\n")
exigees = [f"commit du code répété : {code}", "FIN DE LA RÉPÉTITION",
           "récupération (passage-1-premier) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES",
           "récupération (passage-4-relance) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES",
           "récupération (artefact-relance-apres-notations) : code 1 ; RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC",
           "récupération (artefact-notations-manquantes) : code 1 ; RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC",
           "récupération (artefact-ajout-dans-le-pilote) : code 1 ; RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC"]
for e in exigees:
    assert e in lignes, f"ligne absente : {e}"
for p in ("passage 1-sain : code 0 ", "passage 2-artefact-branche-presente : code 2 ", "passage 3-premier-manque : code 1 ",
          "passage 4-relance : code 0 "):
    assert sum(l.startswith(p) for l in lignes) == 1, f"passage : {p}"
assert sum("RÉCUPÉRATION : TOUS CONFORMES" in l for l in lignes) == 2, "deux récupérations conformes attendues"
def ko_apres(etiquette, prefixe):
    i = lignes.index(etiquette)
    ko = [l for l in lignes[i + 1:i + 12] if l.startswith("    KO")]
    assert len(ko) == 1 and ko[0].startswith(prefixe), f"{etiquette} : KO {ko}"
ko_apres("récupération (artefact-relance-apres-notations) : code 1 ; RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC", "    KO  0 ")
ko_apres("récupération (artefact-notations-manquantes) : code 1 ; RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC", "    KO  4c ")
ko_apres("récupération (artefact-ajout-dans-le-pilote) : code 1 ; RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC", "    KO  1c ")
scripts = {}
for l in lignes:
    if l.startswith("script répété : "):
        m = re.fullmatch(r"script répété : ([a-z_]+_v1\.(?:py|sh)) ([0-9a-f]{64})", l)
        assert m, f"ligne « script répété » mal formée : {l[:90]}"
        assert m.group(1) not in scripts, f"script répété en double : {m.group(1)}"
        scripts[m.group(1)] = m.group(2)
attendus = {"construire_pilote_jouet_v1.py", "recuperation_notations_v1.sh", "repetition_jouet_notations_v1.sh"}
assert set(scripts) == attendus, f"scripts répétés {sorted(scripts)} : les trois attendus exactement"
for s in sorted(attendus):
    print(s, scripts[s])
PYREP
c=$?
CAUSE_REP=""
[ "$c" = 0 ] || CAUSE_REP=$(tail -1 "$W/bloc-repetition.txt")
if [ -z "$CAUSE_REP" ]; then
    grep -E '^[a-z_]+_v1\.(py|sh) [0-9a-f]{64}$' "$W/bloc-repetition.txt" > "$W/scripts-repetes.txt"
    [ "$(wc -l < "$W/scripts-repetes.txt")" = 3 ] || CAUSE_REP="trois scripts répétés attendus"
    while read -r s e; do
        [ "$(git show "$S:$VERSEES/$s" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$e" ] || CAUSE_REP="script répété ≠ copie versée à S : $s"
    done < "$W/scripts-repetes.txt"
fi
if [ -z "$CAUSE_REP" ]; then
    { [ "$(git show "$S:$REPETITION_JOUET_CHEMIN" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$REPETITION_JOUET" ] && \
      [ "$(git show "$S:$REPETITION_JOUET_CHEMIN.sha256" 2>/dev/null | cut -d' ' -f1)" = "$REPETITION_JOUET" ]; } \
        || CAUSE_REP="journal absent de S, d'une autre empreinte que l'épingle, ou sceau différent"
fi
if [ -z "$CAUSE_REP" ]; then
    ok "répétition jouet au code relu : journal épinglé, scellé ; quatre passages, deux récupérations conformes, trois artefacts refusés à leur KO ; scripts exécutés = copies versées à S"
else ko "répétition jouet : $CAUSE_REP"; fi
# 7. rapports de la contre-lecture : présents à S, scellés, cités ; seuls de leur famille
for paire in $RAPPORTS_ATTENDUS; do
    nom=${paire%%=*}; e=${paire#*=}; f="prereg/contre-lectures/$nom"
    [ "$(git show "$S:$f" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$e" ] && [ "$(git show "$S:$f.sha256" 2>/dev/null)" = "$e  $nom" ] \
        && grep -qF "\`$f\` (\`$e\`)" "$P" && ok "rapport $nom présent, scellé, cité" || ko "rapport $nom absent, non scellé, d'empreinte différente ou non cité"
done
git ls-tree -r --name-only "$S" prereg/contre-lectures/ > "$W/contre-lectures.txt"
presents=$(grep -E '^prereg/contre-lectures/T0\.5-notations-v1-' "$W/contre-lectures.txt" | grep -v '\.sha256$' | xargs -r -n1 basename | sort | tr '\n' ' ')
attendus=$(for paire in $RAPPORTS_ATTENDUS; do echo "${paire%%=*}"; done | sort | tr '\n' ' ')
[ "$presents" = "$attendus" ] && ok "rapports des notations présents à S = rapports attendus ($n_paires)" || ko "rapports présents « $presents » ≠ attendus « $attendus »"
# 8. branche de résultats ; relance : -v1 présente sans aucun fichier de notations (préséance)
case "$MODE_LANCEMENT" in
premier) git ls-remote --exit-code origin "refs/heads/$BRANCHE" >/dev/null 2>&1; c=$?
         [ "$c" = 2 ] && ok "branche $BRANCHE absente" || ko "branche $BRANCHE : code $c (2 attendu)" ;;
relance) git ls-remote --exit-code origin "refs/heads/$BRANCHE" >/dev/null 2>&1; c=$?
         [ "$c" = 2 ] && ok "branche de relance absente" || ko "branche de relance : code $c (2 attendu)"
         # liste de l'arbre écrite dans un fichier, code de git exigé, puis cherchée : jamais de tube vers grep -q sous
         # pipefail (relecture R2 du pilote, CH-03)
         if git fetch -q origin calcul/t05-notations-reel-v1 2>/dev/null && git ls-tree -r --name-only FETCH_HEAD > "$W/arbre-v1.txt"; then
             if grep -qE '/notations-[^/]+\.json$' "$W/arbre-v1.txt"; then ko "-v1 porte un fichier de notations : relancement interdit (préséance)"
             else ok "-v1 présente, sans fichier de notations ($(wc -l < "$W/arbre-v1.txt") chemins lus)"; fi
             # arrêt consigné sur -v1 : aucun juge fini (ni « écrit », ni « échu ») ; un résumé interdit aussi le relancement
             grep -E '^diag/[^/]+-t05-notations-reel/(arret|resume)\.json$' "$W/arbre-v1.txt" > "$W/issues-v1.txt" || true
             if grep -q '/resume\.json$' "$W/issues-v1.txt"; then ko "-v1 porte un résumé : run fini, relancement interdit"
             elif [ -s "$W/issues-v1.txt" ]; then
                 statuts=$(while read -r f; do git show "FETCH_HEAD:$f"; done < "$W/issues-v1.txt" | python3 -c '
import json, sys
dec = json.JSONDecoder(); t = sys.stdin.read(); i = 0; s = []
while i < len(t):
    t2 = t[i:].lstrip()
    if not t2: break
    o, n = dec.raw_decode(t2); i = len(t) - len(t2) + n
    s += [j.get("statut") for j in o["resultat"].get("partiel", {}).get("juges", {}).values()]
print(" ".join(sorted(set(x or "absent" for x in s))) or "aucun")' 2>&1)
                 case " $statuts " in *" écrit "*|*" échu "*) ko "-v1 : arrêt consigné avec un juge fini ($statuts) : relancement interdit (préséance)" ;;
                     *) ok "-v1 : arrêt consigné sans juge fini (statuts : $statuts)" ;; esac
             else ok "-v1 : ni arrêt ni résumé consignés"; fi
         else ko "-v1 absente ou illisible : pas de relancement"; fi ;;
esac
grep -qF "\`PREREG=$P\`, \`BRANCHE=$BRANCHE\`" "$P" && ok "PREREG et BRANCHE ($BRANCHE) cités par la ligne « Lancement »" || ko "PREREG ou BRANCHE : la ligne « Lancement » cite autre chose"
PYTHONPATH=src "$PY" -c "from controle_ia.prereg import problemes; p = problemes('$P'); print(p); raise SystemExit(1 if p else 0)" \
    && ok "problemes() vide" || ko "problemes() non vide"
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier "$P" "$CFG" "$TACHES" >/dev/null \
    && ok "sceaux du préenregistrement, de la configuration et des tâches" || ko "sceaux"
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier-arbre . > "$W/verifier-arbre.txt" 2>&1
if tail -1 "$W/verifier-arbre.txt" | grep -qx "arbre intact"; then ok "verifier-arbre : arbre intact"
else ko "verifier-arbre : $(grep '^ÉCHEC' "$W/verifier-arbre.txt" | head -5 | tr '\n' ' ')"; fi
# 9. gardes du lanceur des notations rejouées dans l'ordre d'executer(), jusqu'au manifeste (rien n'est écrit) ; valeurs
# du texte ; première lecture
PYTHONPATH=src "$PY" - "$P" "$CFG" "$TACHES" "$PILOTE" "$ANALYSE" > "$W/bloc-gardes.txt" 2>&1 <<'EOF' && ok "gardes du lanceur des notations (état du pilote, paramètres, versions, citations, 180 notations par juge, graines), valeurs du texte, première lecture" || ko "gardes du lanceur, valeurs ou première lecture : $(tail -1 "$W/bloc-gardes.txt")"
import json, sys
from pathlib import Path
from controle_ia.environnements import noter_pilote_a as npa
from controle_ia.environnements.lancer_pilote_a import exiger_invites
from controle_ia.environnements.pilote_a import charger_taches
from controle_ia.harnais.validation_reelle import exiger_code_cite, exiger_code_importe_sous
from controle_ia.manifeste import verifier_resultat
from controle_ia.scellement import verifier
p, cfg, taches, pilote, analyse = sys.argv[1:6]
racine = Path(".")
c = json.loads(Path(cfg).read_text(encoding="utf-8"))
npa.exiger_config_notations(c)
assert c["mode"] == "reel" and c["run_pilote"] == pilote, (c["mode"], c["run_pilote"])
assert c["duree_max_juges_s"] == {"8B": 12000, "3B": 10000} and c["duree_globale_s"] == 23100, "durées de la configuration"
assert c["notations_attendues_par_juge"] == 180, "180 notations par juge"
assert npa.DUREE_EXTERNE_S == 24000 and npa.DUREE_GLOBALE_MAX_S == 23100, "constantes du lanceur"
# bornes des scripts de l'instance liées aux constantes du lanceur (contre-lecture R2, angle « chaîne ») : délai externe
# du run = DUREE_EXTERNE_S ; plafond de l'amorce au-dessus du délai externe et de son KILL ; échéance globale sous le
# délai externe avec la marge d'un lot
inst = Path("scripts/notations_t05_instance.sh").read_text(encoding="utf-8")
amorce = Path("scripts/amorce_instance_t05_notations.sh").read_text(encoding="utf-8")
assert inst.count("DELAI=(timeout --signal=TERM --kill-after=5m 400m)") == 1 and 400 * 60 == npa.DUREE_EXTERNE_S, "délai externe du run"
assert amorce.count("timeout --signal=TERM --kill-after=5m 430m ") == 1 and 430 * 60 >= npa.DUREE_EXTERNE_S + 5 * 60 + 1500, "plafond de l'amorce"
assert npa.DUREE_GLOBALE_MAX_S + 500 <= npa.DUREE_EXTERNE_S, "échéance globale sous le délai externe, marge d'un lot"
texte = Path(p).read_text(encoding="utf-8")
for s in ("12 000 s", "10 000 s", "23 100 s", "400 minutes", "430 minutes", "26 400 s", "180 par juge"):
    assert s in texte, f"valeur non citée par le texte : {s}"
t = charger_taches(taches)
sha_t = verifier(taches)
exiger_invites(c)
pil = npa.charger_pilote_note(racine, c["run_pilote"])
assert pil["arret"]["partiel"]["taches_sha256"] == sha_t, "tâches ≠ celles du pilote"
assert pil["arret"]["etape"] == "notations decisives par 8B", pil["arret"]["etape"]
npa.exiger_egal_au_pilote(c, pil, "reel")
exiger_code_importe_sous(racine)
commit = exiger_code_cite(racine, Path(p))
ent = npa.exiger_citations_notations(Path(p), c, sha_t, pil)
par_id = {x["identifiant"]: x for x in t}
dem = {j["nom"]: npa.demandes_decisives(pil, par_id, c, j["nom"]) for j in c["juges"]}
assert {k: len(v) for k, v in dem.items()} == {"8B": 180, "3B": 180}, {k: len(v) for k, v in dem.items()}
lots = [len(dem["8B"][k:k + c["lot_juge"]]) for k in range(0, 180, c["lot_juge"])]
assert lots == [8] * 22 + [4], lots
npa.exiger_graines_du_pilote(npa.cles_des_graines(dem), ent, pil)
lec = verifier_resultat(racine, Path(f"diag/{analyse}/lecture.json"))["resultat"]
assert lec["run_pilote"] == pilote and {j: lec["juges"][j]["plan_b"] for j in ("8B", "3B")} == {"8B": "nœud", "3B": "nœud"}, \
    "première lecture : juges non en nœud"
print("commit cité :", commit, "; entropie citée :", ent, "; lots :", len(lots))
EOF
sed 's/^/    /' "$W/bloc-gardes.txt"
# 10. format des vrais tokeniseurs (juges 8B et 3B) = format scellé du début du pilote (épisodes du pilote)
HF_HOME="$W/cache-hf" PYTHONPATH=src "$PY" - "$CFG" "$PILOTE" > "$W/bloc-format.txt" 2>&1 <<'EOF' && ok "format des vrais tokeniseurs (8B, 3B) = format scellé du début du pilote" || ko "format des tokeniseurs réels : $(tail -1 "$W/bloc-format.txt")"
import json, sys
from pathlib import Path
from controle_ia.environnements import lancer_pilote_a as lp
from controle_ia.manifeste import verifier_resultat
c = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
formats = verifier_resultat(Path("."), Path(f"diag/{sys.argv[2]}/episodes.json"))["resultat"]["formats"]
fmt_agent = lp.charger_format_seul(c["agent"], "reel")
for j in c["juges"]:
    fmt = fmt_agent if j["meme_modele_que_agent"] else lp.charger_format_seul(j, "reel")
    f = lp.controler_format(fmt, j, "juge", c)
    assert f == formats[f"juge-{j['nom']}"], f"juge {j['nom']} : format ≠ celui du début du pilote"
    print(j["nom"], f["texte_attendu_ouverture"], f["jetons"])
EOF
sed 's/^/    /' "$W/bloc-format.txt"
rm -rf "$W/cache-hf"
# 11. suite complète des tests au commit S, environnement neuf
a=$(sed -n "s/.*Tests attendus : \`\([0-9]*\)\`.*/\1/p" "$P" | head -1)
PYTHONPATH=src "$PY" -m pytest -q -p no:cacheprovider > "$W/suite.txt" 2>&1; cs=$?
derniere=$(grep -v '^$' "$W/suite.txt" | tail -1)
cp "$W/suite.txt" "$(dirname "$D")/suite-notations-S.txt" 2>/dev/null || true   # gardée à côté du clone (traces du lanceur)
[ "$cs" = 0 ] && [[ "$derniere" =~ ^$a\ passed(,\ [0-9]+\ warnings?)?\ in\ [0-9.]+s(\ \([0-9]+:[0-9]{2}:[0-9]{2}\))?$ ]] \
    && ok "suite complète au commit S, environnement neuf : « $derniere »" || ko "suite complète : « $derniere » (code $cs ; $a attendus)"
# 12. garde de calcul sur le registre de S
echo '{"tool_input":{"command":"GO_ID=GO-2026-10-04-08 vastai create instance 1 --raw"}}' | python3 .claude/hooks/garde_calcul.py \
    && ok "garde de calcul : registres/go.md de S lisible, GO-2026-10-04-08 accepté" || ko "garde de calcul sur le registre de S"
# 13. lecture précoce du script de l'instance : chaque citation une seule fois, chemins attendus
lire_unique() { [ "$(grep -c "$1 : \`" "$P" || true)" = 1 ] && sed -n "s/.*$1 : \`\\([^\`]*\\)\`.*/\\1/p" "$P"; }
L_TESTS=$(lire_unique "Tests attendus"); L_CFG=$(lire_unique "Chemin de la configuration des notations")
L_T=$(lire_unique "Chemin des tâches du pilote noté"); L_M=$(lire_unique "Chemin du manifeste du pilote noté")
L_E=$(lire_unique "Chemin des épisodes du pilote noté"); L_A=$(lire_unique "Chemin de l'arrêt du pilote noté")
echo "lecture précoce (script de l'instance, PREREG=$P) : tests $L_TESTS ; configuration $L_CFG ; tâches $L_T ; manifeste $L_M ; épisodes $L_E ; arrêt $L_A"
[ "$L_TESTS" = "$a" ] && [ "$L_CFG" = "$CFG" ] && [ "$L_T" = "$TACHES" ] && [ "$L_M" = "runs/$PILOTE/manifeste.json" ] \
    && [ "$L_E" = "diag/$PILOTE/episodes.json" ] && [ "$L_A" = "diag/$PILOTE/arret.json" ] \
    && ok "lecture précoce : citations uniques, chemins attendus" || ko "lecture précoce : citation absente, en double, ou chemin inattendu"
[ "$echec" = 0 ] && echo "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES" || echo "CONTRÔLES AVANT DÉPENSE : ÉCHEC"
[ "$echec" = 0 ]
