#!/usr/bin/env bash
# Contrôles avant dépense du pilote de T0.5 (préenregistrement prereg/T0.5-pilote-8B-v1.md), v1, sur le modèle des
# contrôles v7 de la revalidation (docs/procedures/revalidation-T0.5-v2/) et des constats de l'état des lieux du pilote
# (PL-06, PF-02, PF-05, PL-07). Sur un clone neuf du dépôt de travail au commit de scellement S ; aucun calcul payant ;
# code 0 si et seulement si tout est conforme ; code 2 si les épingles manquent ou sont mal formées.
# Ce qui est contrôlé : S ajoute le sceau du préenregistrement ; commit du code cité, ancêtre de S, arbre gelé identique ;
# empreintes des deux scripts de l'instance citées ; configuration et tâches scellées, citées, égales à leur source
# (configuration du brouillon, noyau et duree_max_s mis à part ; 60 premières tâches de la source) ; valeurs du verdict
# recalculées depuis les résultats scellés de la revalidation et la formule gelée (noyau, durée projetée, duree_max_s) ;
# verdict, décision N-019 v1 (retirée) et proposition N-019 scellés et cités ; décision de Lazar sur N-019 (GO de type
# « revendication », accordé par Lazar, option (a), non révoqué ; N-019 tranchée ; ligne R-…) ; index des invites à son
# empreinte citée ; lecture gelée de la revalidation rejouée à 192 puis à 180 épisodes ; texte de S égal au candidat relu, normalisé (champs du scellement) ;
# rapports attendus présents, scellés, cités, et seuls de leur famille ; branche de résultats absente ; PREREG et
# BRANCHE cités ; problemes() vide ; sceaux ; verifier-arbre ; gardes du lanceur du pilote rejouées ; format des vrais
# tokeniseurs (8B, 3B) contrôlé comme au début du run ; suite complète des tests au commit S dans l'environnement neuf
# (dernière ligne « N passed », N = tests attendus) ; garde de calcul sur le registre de S.
# Usage : controles_avant_depense_pilote_v1.sh S DOSSIER_NEUF [relance]
# « relance » : relancement unique (plan, étape 5) : la branche …-v1 existe sans episodes.json, …-v2 est absente.
set -uo pipefail
S=$1; D=$(realpath -m "$2"); MODE_LANCEMENT=${3:-premier}   # dossier en chemin absolu (VH-10)
DEPOT=https://github.com/lciric/controle-ia-travail.git
CANDIDAT_RELU=74a8867168733e4110e27f7c6bba714eaf9c919092c98a7c5262790b1f6152d1                 # candidat relu (R2), brut
CANDIDAT_RELU_CHEMIN=brouillons/T0.5-pilote-8B-v1-candidat3.md
CANDIDAT_NORMALISE=83056d15157ef9043daab5275e7d4665aa7e087bbb3b5a1556e7d9830cf9ed63            # candidat relu, normalisé (champs du scellement masqués)
RAPPORTS_ATTENDUS="T0.5-pilote-v1-etat-des-lieux-fichiers-de-travail-v1.tar=59f2d2976b2350a8389b9e5a79735c223fa4b6c2d216a4cea8c068a4713e908b T0.5-pilote-v1-etat-des-lieux-resultats-v1.json=8ca0f843b17ba24e78280cd1bf0ba85e2f56639e31a0630ed9779ec96d883011 T0.5-pilote-v1-relecture-b8-fichiers-de-travail-v1.tar=25a27dd630a04f2281145e72fc69e8ed696cb16b91a08cc2a2dd3ddc1f33f4ed T0.5-pilote-v1-relecture-b8-resultats-v1.json=5d604efddf5ebe45adfff6dbe582b3cf28e29b30275239d897da692bf96c9f80 T0.5-pilote-v1-relecture-b8-verification-c2-fichiers-de-travail-v1.tar=d18df563693c89ea9b152e067c0b5728dfb27d26fa9475e8e0e2d5d7caa2dcfc T0.5-pilote-v1-relecture-b8-verification-c2-resultats-v1.json=1f78fa75e9361bcaed0a22666af2b2114267c4f2b9531db538be8f44ca0c402e T0.5-pilote-v1-relecture-b8-verification-c3-fichiers-de-travail-v1.tar=8f3557fa68ea09b08c371dfc9662b0c89f1942b3af6ab94f974d8b05cc67dfe3 T0.5-pilote-v1-relecture-b8-verification-c3-resultats-v1.json=fa6d0ac3b67eb4e267b73579b9ebf97f3c129626780096d663d7945c9740134d"           # paires nom=empreinte (état des lieux, relecture R2 et ses vérifications courtes)
CODE_RELU=7b073008585279a06251b08d6b456694320a3c58                     # commit du code relu et vérifié (relecture R2, CH-01) : arbre gelé de S égal
REPETITION_JOUET=531f2d79abb220174bca871c19953d5c20db6c51c5ce96f945042ae6a8a20c7f              # empreinte du journal de la répétition jouet au code relu (CH-12)
REPETITION_JOUET_CHEMIN=docs/procedures/pilote-T0.5-v1/repetition-jouet-pilote-v1.log
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
H=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/pilote-v1
P=prereg/T0.5-pilote-8B-v1.md; CFG=prereg/T0.5-pilote-config-v1.json
CFG_BROUILLON=brouillons/T0.5-pilote-config-v1-brouillon1.json
TACHES=donnees/t05-pilote-v1/taches-pilote-60-v1.json
SOURCE=donnees/20261007-082440-t05-extraction/taches-evaluation.json
SOURCE_SHA=76cdeace861d2fff45ca732c55c2d97611dcd47edc7c27d62bdad4c37755e67e
VERDICT=docs/verdicts/verdict-T0.5-revalidation-v2.md; DECISION=docs/decisions/decision-N-019-v1.md
PROPOSITION=docs/decisions/proposition-N-019-v2.md   # v2 (VN-01) ; la v1 est gardée
PREREG_REVAL=prereg/T0.5-revalidation-equivalence-pilote-v2.md; CONFIG_REVAL=prereg/T0.5-revalidation-config-v1.json   # VT-04
INDEX_INVITES=docs/sources/invites-2606.08892-v1/index.json
RUN_REVAL=20261011-225701-t05-revalidation-reel
case "$MODE_LANCEMENT" in premier) BRANCHE=calcul/t05-pilote-reel-v1 ;; relance) BRANCHE=calcul/t05-pilote-reel-v2 ;;
    *) echo "troisième argument : relance, ou rien"; exit 2 ;; esac
echec=0; ok() { echo "OK  $*"; }; ko() { echo "KO  $*"; echec=1; }
[[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "S invalide"; exit 2; }
[ -e "$D" ] && { echo "$D existe déjà"; exit 2; }
[[ "$CODE_RELU" =~ ^[0-9a-f]{40}$ && "$REPETITION_JOUET" =~ ^[0-9a-f]{64}$ ]] || { echo "code relu ou répétition jouet non épinglés"; exit 2; }
[[ "$CANDIDAT_RELU" =~ ^[0-9a-f]{64}$ && "$CANDIDAT_NORMALISE" =~ ^[0-9a-f]{64}$ && "$CANDIDAT_RELU_CHEMIN" == brouillons/* ]] \
    || { echo "candidat relu non épinglé"; exit 2; }
n_paires=0
for paire in $RAPPORTS_ATTENDUS; do [[ "$paire" =~ ^[^=]+=[0-9a-f]{64}$ ]] || { echo "rapports attendus mal formés : $paire"; exit 2; }; n_paires=$((n_paires+1)); done
[ "$n_paires" -ge 1 ] || { echo "liste des rapports attendus vide"; exit 2; }
git clone -q "$DEPOT" "$D" || { echo "clonage impossible"; exit 2; }
cd "$D" && git checkout -q "$S" || { echo "commit $S introuvable"; exit 2; }
[ "$(git log --diff-filter=A -1 --format=%H -- "$P.sha256")" = "$S" ] && ok "S ajoute le sceau du préenregistrement" || ko "S n'est pas le commit qui ajoute $P.sha256"
attendus_s=$(printf '%s\n' "$CFG" "$CFG.sha256" "$P" "$P.sha256" | sort | tr '\n' ' ')
[ "$(git diff --name-only "$S^" "$S" | sort | tr '\n' ' ')" = "$attendus_s" ] && ok "S n'ajoute que le préenregistrement, la configuration et leurs sceaux" || ko "contenu de S inattendu : $(git diff --name-only "$S^" "$S" | tr '\n' ' ')"
CODE=$(sed -n "s/.*Commit du code d'analyse : \`\([0-9a-f]\{40\}\)\`.*/\1/p" "$P" | head -1)
if [[ "$CODE" =~ ^[0-9a-f]{40}$ ]] && git merge-base --is-ancestor "$CODE" "$S"; then ok "commit du code cité $CODE, ancêtre de S"
else ko "commit du code cité illisible ou non ancêtre de S"; CODE=$S; fi
for f in scripts/amorce_instance_t05.sh scripts/pilote_t05_instance.sh; do
    e=$(git show "$S:$f" | sha256sum | cut -d' ' -f1)
    grep -qF "\`$f\` (\`$e\`, sha256)" "$P" && ok "empreinte de $f citée ($e)" || ko "empreinte de $f ($e) non citée"
done
GELES=$(PYTHONPATH=src "$PY" -c "from controle_ia.harnais.validation_reelle import CHEMINS_GELES; print(' '.join(CHEMINS_GELES))" 2>/dev/null)
if [ -n "$GELES" ]; then
    # shellcheck disable=SC2086
    git diff --quiet "$CODE" "$S" -- $GELES; c=$?
    case $c in 0) ok "arbre gelé (CHEMINS_GELES) identique au commit du code" ;; 1) ko "arbre gelé modifié depuis le commit du code" ;;
               *) ko "comparaison de l'arbre gelé impossible (code $c)" ;; esac
    # l'arbre gelé de S est celui du code relu et vérifié (épinglé), non celui de n'importe quel commit cité (CH-01)
    git diff --quiet "$CODE_RELU" "$S" -- $GELES; c=$?
    case $c in 0) ok "arbre gelé de S = code relu épinglé ($CODE_RELU)" ;; 1) ko "arbre gelé de S ≠ code relu épinglé ($CODE_RELU)" ;;
               *) ko "comparaison au code relu impossible (code $c)" ;; esac
else ko "CHEMINS_GELES illisible"; fi
for f in "$CFG" "$TACHES" "$SOURCE" "$VERDICT" "$DECISION" "$PROPOSITION" "$INDEX_INVITES" "$PREREG_REVAL" "$CONFIG_REVAL" "diag/$RUN_REVAL/resume.json" "diag/$RUN_REVAL/mesures-defaut.json" \
         "diag/$RUN_REVAL/lecture-defaut.json" "diag/$RUN_REVAL/lecture-math.json"; do
    if git cat-file -e "$S:$f" 2>/dev/null && git cat-file -e "$S:$f.sha256" 2>/dev/null && \
       [ "$(git show "$S:$f.sha256")" = "$(git show "$S:$f" | sha256sum | cut -d' ' -f1)  $(basename "$f")" ]; then
        ok "$f et son sceau entier dans l'arbre de S"
    else ko "$f ou son sceau absent ou non conforme"; fi
done
for f in "$VERDICT" "$DECISION" "$PROPOSITION" "$TACHES" "$INDEX_INVITES" "$PREREG_REVAL" "$CONFIG_REVAL"; do
    e=$(git show "$S:$f" | sha256sum | cut -d' ' -f1)
    grep -qF "$e" "$P" && ok "$f cité par son empreinte ($e)" || ko "$f non cité par son empreinte"
done
# décision de Lazar sur N-019 (relecture R2, NO-03) : GO cité par S, de type « revendication », accordé par Lazar, qui cite
# N-019 et l'option (a), sans ligne « révocation » qui le nomme ; colonne d'état de N-019 à la forme exacte (CH-10) ;
# ligne R-… qui le consigne ; GO de calcul non révoqué
python3 - "$P" registres/go.md registres/decisions.md > "$D/../bloc-go-$$.txt" 2>&1 <<'PYGO' && ok "décision de Lazar sur N-019 : GO conforme, non révoqué, N-019 tranché (a), registre" || ko "décision de Lazar sur N-019 (GO, révocation, N-019 ou registre) : $(tail -1 "$D/../bloc-go-$$.txt")"
import re, sys
texte, go_md, dec_md = (open(f, encoding="utf-8").read() for f in sys.argv[1:4])
m = re.search(r"^- Décision de Lazar sur N-019 : `(GO-\d{4}-\d{2}-\d{2}-\d{2})` \((R-\d{3,4})\)", texte, re.M)
assert m and len(re.findall(r"^- Décision de Lazar sur N-019 :", texte, re.M)) == 1, "ligne « Décision de Lazar sur N-019 »"
go, reg = m.groups()
lignes = go_md.split("\n")
c = [[x.strip() for x in l.strip().strip("|").split("|")] for l in lignes if l.startswith(f"| {go} |")]
assert len(c) == 1 and len(c[0]) == 8, f"{go} absent, en double ou mal formé"
assert c[0][2] == "revendication" and c[0][6] == "Lazar" and "N-019" in c[0][3] and "(a)" in c[0][3], f"{go} : {c[0][2]}, {c[0][6]}"
for g in (go, "GO-2026-10-04-08"):
    assert not [l for l in lignes if l.startswith("| GO-") and (lambda c: (len(c) == 8 and c[2].lower() == "révocation" and (g in c[3] or g in c[7])) or (len(c) != 8 and "révocation" in l.lower() and g in l))([x.strip() for x in l.strip().strip("|").split("|")])], f"{g} révoqué"
dec = dec_md.split("\n")
n19 = [l for l in dec if l.startswith("| N-019 |")]
assert len(n19) == 1, "N-019 absent ou en double"
etat = n19[0].rsplit("|", 2)[-2].strip()
# forme exacte de la colonne d'état (relecture R2, CH-10) ; une révocation est une ligne « révocation » de go.md
assert re.fullmatch(rf"tranché \(a\) par Lazar : {re.escape(go)} \({re.escape(reg)}\)", etat), \
    f"N-019 : colonne d'état ≠ « tranché (a) par Lazar : {go} ({reg}) »"
r = [l for l in dec if l.startswith(f"| {reg} |")]
assert len(r) == 1 and go in r[0], f"{reg} absent, en double ou sans {go}"
print(f"GO {go} ({reg}) conforme")
PYGO
sed 's/^/    /' "$D/../bloc-go-$$.txt"; rm -f "$D/../bloc-go-$$.txt"
# index des invites : empreinte citée = empreinte à S (relecture R2, CO-07 ; état des lieux, PF-06)
ei=$(git show "$S:$INDEX_INVITES" | sha256sum | cut -d' ' -f1)
grep -qF "(\`$INDEX_INVITES\`, \`$ei\`)" "$P" && ok "index des invites cité à son empreinte de S ($ei)" || ko "index des invites : empreinte de S ($ei) non citée"
# texte de S = candidat relu, normalisé ; candidat versé, scellé, à l'empreinte épinglée
[ "$(git show "$S:$CANDIDAT_RELU_CHEMIN" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$CANDIDAT_RELU" ] && \
    [ "$(git show "$S:$CANDIDAT_RELU_CHEMIN.sha256" 2>/dev/null)" = "$CANDIDAT_RELU  $(basename "$CANDIDAT_RELU_CHEMIN")" ] \
    && ok "candidat relu versé, scellé, à l'empreinte épinglée" || ko "candidat relu absent, non scellé ou d'empreinte différente"
n=$("$PY" -I "$H/normaliser_pilote_v1.py" "$P")
[ "$n" = "$CANDIDAT_NORMALISE" ] && ok "préenregistrement de S = candidat relu, normalisé ($n)" || ko "préenregistrement de S ≠ candidat relu normalisé ($n)"
nc=$(git show "$S:$CANDIDAT_RELU_CHEMIN" | "$PY" -I "$H/normaliser_pilote_v1.py" -)
[ "$nc" = "$CANDIDAT_NORMALISE" ] && ok "épingle normalisée = candidat relu normalisé" || ko "épingle normalisée ≠ candidat relu normalisé ($nc)"
# parties masquées par la normalisation, reconstruites (CH-05) : lignes des rapports depuis les épingles, dates égales et
# à moins de deux heures du commit S, nombre de tests égal dans ses deux mentions
python3 - "$P" "$(git log -1 --format=%ct "$S")" "$RAPPORTS_ATTENDUS" > "$D/../bloc-masque-$$.txt" 2>&1 <<'PYREC' && ok "parties masquées reconstruites (rapports, dates, tests)" || ko "parties masquées : reconstruction différente : $(tail -1 "$D/../bloc-masque-$$.txt")"
import datetime, re, sys
texte, s_ct, paires = sys.argv[1], int(sys.argv[2]), sys.argv[3].split()
t = open(texte, encoding="utf-8").read()
cite = lambda famille: " ; ".join(f"`prereg/contre-lectures/{n}` (`{e}`)" for n, e in (x.split("=") for x in paires) if famille in n)
attendu_rel = ("- Relecture R2 du brouillon 8 et du différentiel du code depuis la relecture b6 (`e6ce058`), puis "
               "vérifications courtes des candidats suivants et du différentiel du code depuis le candidat 1 (`942c65e`), "
               "par des sous-agents neufs : rapports " + cite("relecture-b8") + ".")
assert attendu_rel in t.split("\n"), "ligne de la relecture R2"
assert ("synthèse et critique de complétude ; rapports " + cite("etat-des-lieux") + ".") in t, "ligne de l'état des lieux"
d1 = re.findall(r"version scellée le (\d{4}-\d{2}-\d{2} \d{2}:\d{2}) UTC", t)
d2 = re.findall(r"^- Date \(UTC\) : (\d{4}-\d{2}-\d{2} \d{2}:\d{2}) \(", t, re.M)
assert len(d1) == 1 and d1 == d2, f"dates {d1} {d2}"
quand = datetime.datetime.strptime(d1[0], "%Y-%m-%d %H:%M").replace(tzinfo=datetime.timezone.utc).timestamp()
assert abs(quand - s_ct) <= 7200, f"date {d1[0]} à {abs(quand - s_ct):.0f} s du commit S"
n1 = re.findall(r"^- Tests attendus : `(\d+)`", t, re.M); n2 = re.findall(r"au commit cité, (\d+) tests\)", t)
assert len(n1) == 1 and n1 == n2, f"tests {n1} {n2}"
PYREC
sed 's/^/    /' "$D/../bloc-masque-$$.txt"; rm -f "$D/../bloc-masque-$$.txt"
# journal de la répétition jouet : épinglé, scellé, au code relu ; passages et récupérations attendus, lignes KO des
# artefacts comprises ; scripts exécutés égaux à leurs copies versées à S (vérification courte, VH-02)
git show "$S:$REPETITION_JOUET_CHEMIN" > "$D/../journal-repetition-$$.txt" 2>/dev/null
python3 - "$CODE_RELU" "$D/../journal-repetition-$$.txt" > "$D/../bloc-repetition-$$.txt" 2>&1 <<'PYREP'
import re, sys
code = sys.argv[1]
lignes = open(sys.argv[2], encoding="utf-8").read().split("\n")
exigees = [f"commit du code répété : {code}", "FIN DE LA RÉPÉTITION",
           "récupération (passage-1-premier) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES",
           "récupération (passage-4-relance) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES",
           "récupération (artefact-premier-avec-episodes) : code 1 ; RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC",
           "récupération (artefact-notations-manquantes) : code 1 ; RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC"]
for e in exigees:
    assert e in lignes, f"ligne absente : {e}"
for p in ("passage 1-sain : code 0 ", "passage 2-artefact-branche-presente : code 2 ", "passage 3-premier-manque : code 1 ",
          "passage 4-relance : code 0 "):
    assert sum(l.startswith(p) for l in lignes) == 1, f"passage : {p}"
assert sum("RÉCUPÉRATION : TOUS CONFORMES" in l for l in lignes) == 2, "deux récupérations conformes attendues"
def ko_apres(etiquette, prefixe):
    i = lignes.index(etiquette)
    ko = [l for l in lignes[i + 1:i + 6] if l.startswith("    KO")]
    assert len(ko) == 1 and ko[0].startswith(prefixe), f"{etiquette} : KO {ko}"
ko_apres("récupération (artefact-premier-avec-episodes) : code 1 ; RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC",
         "    KO  0 calcul/t05-pilote-jouet-a-v1 porte un episodes.json")
ko_apres("récupération (artefact-notations-manquantes) : code 1 ; RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC",
         "    KO  4c fichiers d'un run complet")
# lignes « script répété » : une par script, empreinte de 64 caractères hexadécimaux, les cinq attendus exactement
# (vérification courte, VH-02, restes)
scripts = {}
for l in lignes:
    if l.startswith("script répété : "):
        m = re.fullmatch(r"script répété : ([a-z_]+_pilote_v1\.(?:py|sh)) ([0-9a-f]{64})", l)
        assert m, f"ligne « script répété » mal formée : {l[:90]}"
        assert m.group(1) not in scripts, f"script répété en double : {m.group(1)}"
        scripts[m.group(1)] = m.group(2)
cinq = {"deriver_taches_pilote_v1.py", "remplir_pilote_v1.py", "normaliser_pilote_v1.py", "recuperation_pilote_v1.sh",
        "repetition_jouet_pilote_v1.sh"}
assert set(scripts) == cinq, f"scripts répétés {sorted(scripts)} : les cinq attendus exactement"
for s in sorted(cinq):
    print(s, scripts[s])
PYREP
c=$?
CAUSE_REP=""                         # cause du refus, écrite dans la ligne KO (VH-02, restes)
[ "$c" = 0 ] || CAUSE_REP=$(tail -1 "$D/../bloc-repetition-$$.txt")
if [ -z "$CAUSE_REP" ]; then
    grep -E '^[a-z_]+_pilote_v1\.(py|sh) [0-9a-f]{64}$' "$D/../bloc-repetition-$$.txt" > "$D/../scripts-repetes-$$.txt"
    [ "$(wc -l < "$D/../scripts-repetes-$$.txt")" = 5 ] || CAUSE_REP="cinq scripts répétés attendus"
    while read -r s e; do
        [ "$(git show "$S:docs/procedures/pilote-T0.5-v1/$s" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$e" ] \
            || CAUSE_REP="script répété ≠ copie versée à S : $s"
    done < "$D/../scripts-repetes-$$.txt"
    rm -f "$D/../scripts-repetes-$$.txt"
fi
if [ -z "$CAUSE_REP" ]; then
    { [ "$(git show "$S:$REPETITION_JOUET_CHEMIN" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$REPETITION_JOUET" ] && \
      [ "$(git show "$S:$REPETITION_JOUET_CHEMIN.sha256" 2>/dev/null | cut -d' ' -f1)" = "$REPETITION_JOUET" ]; } \
        || CAUSE_REP="journal absent de S, d'une autre empreinte que l'épingle, ou sceau différent"
fi
if [ -z "$CAUSE_REP" ]; then
    ok "répétition jouet au code relu : journal épinglé, scellé ; quatre passages, deux récupérations conformes, deux artefacts refusés à leur KO ; scripts exécutés = copies versées à S"
else ko "répétition jouet : $CAUSE_REP"; fi
rm -f "$D/../bloc-repetition-$$.txt" "$D/../journal-repetition-$$.txt"
# rapports attendus : présents à S, scellés, cités ; seuls de leur famille
for paire in $RAPPORTS_ATTENDUS; do
    nom=${paire%%=*}; e=${paire#*=}; f="prereg/contre-lectures/$nom"
    [ "$(git show "$S:$f" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$e" ] && [ "$(git show "$S:$f.sha256" 2>/dev/null)" = "$e  $nom" ] \
        && grep -qF "\`$f\` (\`$e\`)" "$P" && ok "rapport $nom présent, scellé, cité" || ko "rapport $nom absent, non scellé, d'empreinte différente ou non cité"
done
presents=$(git ls-tree -r --name-only "$S" prereg/contre-lectures/ | grep -E '^prereg/contre-lectures/T0\.5-pilote-v1-(etat-des-lieux|relecture-b8)-[a-z0-9-]+-v1\.(md|json|tar)$' | xargs -r -n1 basename | sort | tr '\n' ' ')
attendus=$(for paire in $RAPPORTS_ATTENDUS; do echo "${paire%%=*}"; done | sort | tr '\n' ' ')
[ "$presents" = "$attendus" ] && ok "rapports du pilote présents à S = rapports attendus ($n_paires)" || ko "rapports présents « $presents » ≠ attendus « $attendus »"
# branche de résultats ; relance : -v1 présente sans episodes.json
case "$MODE_LANCEMENT" in
premier) git ls-remote --exit-code origin "refs/heads/$BRANCHE" >/dev/null 2>&1; c=$?
         [ "$c" = 2 ] && ok "branche $BRANCHE absente" || ko "branche $BRANCHE : code $c (2 attendu)" ;;
relance) git ls-remote --exit-code origin refs/heads/calcul/t05-pilote-reel-v2 >/dev/null 2>&1; c=$?
         [ "$c" = 2 ] && ok "branche de relance absente" || ko "branche de relance : code $c (2 attendu)"
         # liste de l'arbre écrite dans un fichier, code de git exigé, puis cherchée : jamais de tube vers grep -q sous
         # pipefail (une longue sortie interrompue par grep -q donne 141, lu à tort comme « absent » ; relecture R2, CH-03)
         if git fetch -q origin calcul/t05-pilote-reel-v1 2>/dev/null && git ls-tree -r --name-only FETCH_HEAD > "$D/../arbre-v1-$$.txt"; then
             if grep -q '/episodes\.json$' "$D/../arbre-v1-$$.txt"; then ko "-v1 porte un episodes.json : relancement interdit (préséance)"
             else ok "-v1 présente, sans episodes.json ($(wc -l < "$D/../arbre-v1-$$.txt") chemins lus)"; fi
         else ko "-v1 absente ou illisible : pas de relancement"; fi
         rm -f "$D/../arbre-v1-$$.txt" ;;
esac
grep -qF "\`PREREG=$P\`, \`BRANCHE=$BRANCHE\`" "$P" && ok "PREREG et BRANCHE ($BRANCHE) cités par la ligne « Lancement »" || ko "PREREG ou BRANCHE : la ligne « Lancement » cite autre chose"
PYTHONPATH=src "$PY" -c "from controle_ia.prereg import problemes; p = problemes('$P'); print(p); raise SystemExit(1 if p else 0)" \
    && ok "problemes() vide" || ko "problemes() non vide"
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier "$P" "$CFG" "$TACHES" "$SOURCE" >/dev/null \
    && ok "sceaux du préenregistrement, de la configuration et des tâches" || ko "sceaux"
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier-arbre . > "$D/../verifier-arbre-$$.txt" 2>&1
if tail -1 "$D/../verifier-arbre-$$.txt" | grep -qx "arbre intact"; then ok "verifier-arbre : arbre intact"
else ko "verifier-arbre : $(grep '^ÉCHEC' "$D/../verifier-arbre-$$.txt" | head -5 | tr '\n' ' ')"; fi
rm -f "$D/../verifier-arbre-$$.txt"
# valeurs, configuration, tâches, gardes du lanceur, format des vrais tokeniseurs
PYTHONPATH=src "$PY" - "$P" "$CFG" "$CFG_BROUILLON" "$TACHES" "$SOURCE" "$SOURCE_SHA" "$RUN_REVAL" > "$D/../bloc-valeurs-$$.txt" 2>&1 <<'EOF' && ok "valeurs du verdict, configuration, tâches et gardes du lanceur" || ko "valeurs, configuration, tâches ou gardes du lanceur : $(tail -1 "$D/../bloc-valeurs-$$.txt")"
import hashlib, json, math, sys
from pathlib import Path
from controle_ia.environnements import lancer_pilote_a as lp
from controle_ia.environnements.pilote_a import charger_taches, exiger_config
from controle_ia.environnements.revalider_pilote_a import EPISODES_PILOTE, choisir_noyau, duree_projetee_pilote, lire_bras
from controle_ia.harnais.validation_reelle import exiger_code_cite, exiger_code_importe_sous
from controle_ia.manifeste import verifier_resultat
from controle_ia.scellement import verifier
p, cfg, brouillon, taches, source, source_sha, run = sys.argv[1:8]
mes = verifier_resultat(Path("."), Path(f"diag/{run}/mesures-defaut.json"))["resultat"]
res = verifier_resultat(Path("."), Path(f"diag/{run}/resume.json"))["resultat"]
lec_complete = verifier_resultat(Path("."), Path(f"diag/{run}/lecture-defaut.json"))["resultat"]
lec = lec_complete["lecture"]
lm = verifier_resultat(Path("."), Path(f"diag/{run}/lecture-math.json"))["resultat"]["lecture"]
config_reval = json.loads(Path(f"runs/{run}/manifeste.json").read_text(encoding="utf-8"))["config"]
assert res["noeud"] is True and res["noyau_retenu"] is None, "le verdict n'est pas le nœud tranché par N-019"
assert all(lec[k] is True for k in ("R1_garde_saine", "R1_marge", "R3_seuil_fonde", "R4_rejeu", "R5_domaine_couvert",
                                    "R6_chemin_defaut", "R7_memoire", "audit_conforme")) and lec["R2_controle_negatif"] == "conforme"
def lire(duree_s):
    ch = lec_complete.get("chemin")
    return lire_bras(mes["mesures"], mes["controle_negatif"], lec_complete["repere"], mes["rejeu_identique"], config_reval,
                     zone_generee=lec_complete["zone_generee"], audit=lec_complete["audit"],
                     chemin=ch["lecture"] if ch else None, bras="defaut", memoire_pic_gio=mes["memoire_pic_gio"],
                     duree_projetee_s=duree_s)
assert EPISODES_PILOTE == 192 and duree_projetee_pilote(mes["chrono"], 16) == mes["duree_projetee_episodes_pilote_s"]
assert lire(mes["duree_projetee_episodes_pilote_s"]) == lec and choisir_noyau({"defaut": lec, "math": lm}) == (None, None), \
    "lecture gelée rejouée à 192 épisodes ≠ lecture scellée (nœud)"
d = (mes["chrono"]["generation_s"] + mes["chrono"]["passe_unique_s"]) * 60 * 3 / 16
assert d <= 7800, d
duree = min(15000, math.ceil((1.2 * d + 7200) / 60) * 60)
l180 = lire(d)
assert sorted(k for k in set(lec) | set(l180) if lec.get(k) != l180.get(k)) == ["R8_duree", "conforme", "conforme_avec_marge"]
noyau, _ = choisir_noyau({"defaut": l180, "math": lm})
c = json.loads(Path(cfg).read_text(encoding="utf-8"))
b = json.loads(Path(brouillon).read_text(encoding="utf-8"))
assert c["noyau_attention"] == noyau == "defaut" and c["duree_max_s"] == duree == 15000, (c["noyau_attention"], c["duree_max_s"], noyau, duree)
assert {k: v for k, v in c.items() if k not in ("noyau_attention", "duree_max_s")} == \
       {k: v for k, v in b.items() if k not in ("noyau_attention", "duree_max_s")} and set(c) == set(b), "configuration ≠ brouillon"
texte = Path(p).read_text(encoding="utf-8")
assert f"noyau d'attention du pilote : `{noyau}`" in texte and "`15 000` s" in texte and "`7 584,02` s" in texte, "valeurs non citées"
assert f"{d:.2f}" == "7584.02", d
# tâches : 60 premières de la source, à l'identique
verifier(source)
assert hashlib.sha256(Path(source).read_bytes()).hexdigest() == source_sha
t = charger_taches(taches)
src = json.loads(Path(source).read_text(encoding="utf-8"))["resultat"]["taches"]
assert t == src[:60] and len(t) == 60, "tâches ≠ 60 premières de la source"
# gardes du lanceur, dans l'ordre d'executer()
exiger_config(c)
assert not [k for k in lp.CLES_LANCEMENT if k not in c] and c["mode"] == "reel" and c["noyau_attention"] in lp.NOYAUX
assert not isinstance(c["duree_max_s"], bool) and 0 < c["duree_max_s"] <= lp.DUREE_MAX_S
sha_t = verifier(taches)
lp.exiger_cibles(t)
lp.exiger_invites(c)
exiger_code_importe_sous(Path("."))
print("commit cité :", exiger_code_cite(Path("."), Path(p)), "; entropie citée :", lp.exiger_citations_pilote(Path(p), c, sha_t))
print(f"durée projetée {d:.4f} s ; duree_max_s {duree} ; noyau {noyau}")
EOF
sed 's/^/    /' "$D/../bloc-valeurs-$$.txt"; rm -f "$D/../bloc-valeurs-$$.txt"
HF_HOME="$D/../cache-hf-$$" PYTHONPATH=src "$PY" - "$CFG" <<'EOF' && ok "format des vrais tokeniseurs (agent 8B, juge 3B) et jetons de l'appariement : gardes du run conformes" || ko "format des tokeniseurs réels"
import json, sys
from pathlib import Path
from controle_ia.environnements import lancer_pilote_a as lp
c = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
from controle_ia.environnements import pilote_a as pa
fmt_agent = lp.charger_format_seul(c["agent"], "reel")
print(lp.controler_format(fmt_agent, c["agent"], "agent", c)["texte_attendu_ouverture"])
print("jetons Yes/No de l'appariement (vrai tokeniseur du 8B) :", pa.jetons_oui_non(fmt_agent.tok))
for j in c["juges"]:
    fmt = fmt_agent if j["meme_modele_que_agent"] else lp.charger_format_seul(j, "reel")
    print(j["nom"], lp.controler_format(fmt, j, "juge", c)["texte_attendu_ouverture"])
EOF
rm -rf "$D/../cache-hf-$$"
a=$(sed -n "s/.*Tests attendus : \`\([0-9]*\)\`.*/\1/p" "$P" | head -1)
PYTHONPATH=src "$PY" -m pytest -q -p no:cacheprovider > "$D/../suite-$$.txt" 2>&1; cs=$?
derniere=$(grep -v '^$' "$D/../suite-$$.txt" | tail -1); cp "$D/../suite-$$.txt" "$D/../suite-pilote-S.txt" 2>/dev/null; rm -f "$D/../suite-$$.txt"
[ "$cs" = 0 ] && [[ "$derniere" =~ ^$a\ passed(,\ [0-9]+\ warnings?)?\ in\ [0-9.]+s(\ \([0-9]+:[0-9]{2}:[0-9]{2}\))?$ ]] \
    && ok "suite complète au commit S, environnement neuf : « $derniere »" || ko "suite complète : « $derniere » (code $cs ; $a attendus)"
echo '{"tool_input":{"command":"GO_ID=GO-2026-10-04-08 vastai create instance 1 --raw"}}' | python3 .claude/hooks/garde_calcul.py \
    && ok "garde de calcul : registres/go.md de S lisible, GO-2026-10-04-08 accepté" || ko "garde de calcul sur le registre de S"
lire() { sed -n "s/.*$1 : \`\\([^\`]*\\)\`.*/\\1/p" "$P" | head -1; }
echo "lecture précoce (script de l'instance, PREREG=$P) : tests $a ; configuration $(lire "Chemin de la configuration") ; tâches $(lire "Chemin des tâches")"
[ "$(lire "Chemin de la configuration")" = "$CFG" ] && [ "$(lire "Chemin des tâches")" = "$TACHES" ] && ok "lecture précoce : chemins attendus" || ko "lecture précoce : chemins inattendus"
[ "$echec" = 0 ] && echo "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES" || echo "CONTRÔLES AVANT DÉPENSE : ÉCHEC"
[ "$echec" = 0 ]
