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
# scripts de l'instance citées ; pièces du pilote présentes, scellées et citées par l'empreinte de leur fichier (la
# configuration des notations : présente et scellée, citée par son empreinte canonique, relue par les gardes du lanceur
# au bloc 9) ; décision de Lazar
# sur N-021 (GO de type « revendication », accordé par Lazar, option (a), non révoqué ; colonne d'état de N-021 à la
# forme exacte ; ligne R-…) ; texte de S égal au candidat relu, octet pour octet ; configuration de S égale à la
# configuration relue ; rapports de la contre-lecture présents, scellés, cités, seuls de leur famille ; journal de la
# répétition jouet ; branche de résultats absente (relance : …-v1 sans fichier de notations) ; ligne « Lancement » ;
# problemes() vide ; sceaux ; verifier-arbre ; gardes du lanceur des notations rejouées jusqu'au manifeste (état du
# pilote, paramètres et versions égaux, 180 notations par juge, graines égales clé à clé) ; première lecture (juges en
# nœud) ; format des vrais tokeniseurs égal à celui, scellé, du début du pilote ; suite complète des tests au commit S
# dans l'environnement neuf ; garde de calcul ; lecture précoce du script de l'instance (citations uniques).
# Brouillon 3 (contre-lecture R2 de la chaîne) : décision de Lazar et journal de la répétition jouet lus par le module
# commun verifications_notations_v1.py (le même texte que le scellement) ; journal : blocs de KO bornés, ligne « candidat
# répété » exigée ; relance : résumé, arrêt illisible, juge fini ou ligne « fin= » des traces sur …-v1 refusés ; bornes
# du lanceur et de la surveillance reliées aux constantes ; trace de la suite nommée d'après le dossier neuf.
# Usage : controles_avant_depense_notations_v1.sh S DOSSIER_NEUF [relance]
# « relance » : relancement unique (préenregistrement, Critères de lecture gelés, Relancement) : la branche …-v1 existe
# sans fichier de notations, sans résumé, sans juge fini ; …-v2 est absente.
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
H=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/notations-v1
VERIF=$H/verifications_notations_v1.py                      # module commun (égal à sa copie versée : le lanceur le vérifie)
VERSEES=docs/procedures/notations-T0.5-v1
P=prereg/T0.5-pilote-notations-v1.md; CFG=prereg/T0.5-pilote-notations-config-v1.json
PILOTE=20261012-105125-t05-pilote-reel; ANALYSE=20261012-150724-t05-pilote-analyse
CODE_PILOTE=2660b07220ec011674f871c47fd14a2cdd840fd7         # commit du code cité par le pilote (modules de lecture gelés)
S_PILOTE=1c6c900819640e8320ab85a07b3abd4937e22d5f            # commit de scellement du pilote (dépendances installées)
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
for paire in $RAPPORTS_ATTENDUS; do [[ "$paire" =~ ^T0\.5-notations-v1-[a-z0-9-]+-v1\.(md|json|tar)=[0-9a-f]{64}$ ]] \
    || { echo "rapports attendus mal formés : $paire"; exit 2; }; n_paires=$((n_paires+1)); done
[ "$n_paires" -ge 2 ] || { echo "rapports attendus : au moins le rapport de la contre-lecture et ses fichiers de travail"; exit 2; }
W="$D.travail"                                   # fichiers de travail dans un dossier neuf, à côté du clone
[ -e "$W" ] && { echo "$W existe déjà"; exit 2; }
[ -e "$D.suite.txt" ] && { echo "$D.suite.txt existe déjà (R12)"; exit 2; }
[ -f "$VERIF" ] || { echo "module commun $VERIF absent"; exit 2; }
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
# dépendances que l'instance installe : égales à celles du commit de scellement du pilote (contre-lecture R2 de la chaîne,
# critique de complétude, constat 6 : la garde des versions du lanceur ne voit que l'environnement de l'instance)
git diff --quiet "$S_PILOTE" "$S" -- requirements-cpu.txt requirements-gpu.txt requirements-donnees.txt; c=$?
[ "$c" = 0 ] && ok "dépendances (requirements-cpu, -gpu, -donnees) égales à celles du pilote (${S_PILOTE:0:12})" \
    || ko "dépendances différentes de celles du pilote (${S_PILOTE:0:12}), code $c"
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
for f in "$PREREG_PILOTE" "$CONFIG_PILOTE" "$VERDICT" "$AUDIT" "$PROPOSITION" "diag/$ANALYSE/lecture.json" \
         "runs/$ANALYSE/manifeste.json" "runs/$PILOTE/manifeste.json" "diag/$PILOTE/episodes.json" \
         "diag/$PILOTE/appariements.json" "diag/$PILOTE/arret.json" "$TACHES"; do
    e=$(git show "$S:$f" | sha256sum | cut -d' ' -f1)
    grep -qF "\`$e\`" "$P" && ok "$f cité par son empreinte ($e)" || ko "$f non cité par son empreinte"
done
# 4. décision de Lazar sur N-021 : GO cité par S (une ligne de forme fixe), de type « revendication », accordé par Lazar,
# qui cite N-021 et l'option (a), sans ligne « révocation » qui le nomme ; GO de calcul non révoqué ; colonne d'état de
# N-021 à la forme exacte « tranché (a) par Lazar : GO (R-…) » ; ligne R-… qui le consigne
python3 -I "$VERIF" go "$P" registres/go.md registres/decisions.md > "$W/bloc-go.txt" 2>&1 \
    && ok "décision de Lazar sur N-021 : GO conforme, non révoqué, N-021 tranché (a), registre" \
    || ko "décision de Lazar sur N-021 (GO, révocation, N-021 ou registre) : $(tail -1 "$W/bloc-go.txt")"
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
python3 -I "$VERIF" repetition "$CODE_RELU" "$W/journal-repetition.txt" "$(basename "$CANDIDAT_RELU_CHEMIN")" "$CANDIDAT_RELU" \
    > "$W/bloc-repetition.txt" 2>&1
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
    ok "répétition jouet au code relu : journal épinglé, scellé ; quatre passages, trois récupérations conformes et une des traces seules, six artefacts refusés à leur KO ; scripts exécutés = copies versées à S"
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
         # fichiers AJOUTÉS par -v1 depuis S (jamais l'arbre entier : les runs anciens du dépôt y ont leurs résumés)
         if git fetch -q origin calcul/t05-notations-reel-v1 2>/dev/null && git merge-base --is-ancestor "$S" FETCH_HEAD \
                 && git diff --name-only --diff-filter=A "$S" FETCH_HEAD > "$W/arbre-v1.txt"; then
             if grep -qE '/notations-[^/]+\.json$' "$W/arbre-v1.txt"; then ko "-v1 porte un fichier de notations : relancement interdit (préséance)"
             else ok "-v1 présente, descendante de S, sans fichier de notations ($(wc -l < "$W/arbre-v1.txt") fichiers ajoutés lus)"; fi
             # résumé : run fini ; arrêts consignés : lisibles, aucun juge d'un statut autre que « en cours » (module
             # commun ; un arrêt illisible n'établit rien) ; traces poussées : aucune ligne « PROGRES … fin= »
             grep -E '^diag/[^/]+/(arret|resume)\.json$' "$W/arbre-v1.txt" > "$W/issues-v1.txt" || true
             if grep -q '/resume\.json$' "$W/issues-v1.txt"; then ko "-v1 porte un résumé : run fini, relancement interdit"
             elif [ -s "$W/issues-v1.txt" ]; then
                 mkdir -p "$W/arrets-v1"; k=0
                 while read -r f; do k=$((k + 1)); git show "FETCH_HEAD:$f" > "$W/arrets-v1/arret-$k.json"; done < "$W/issues-v1.txt"
                 if python3 -I "$VERIF" statuts-v1 "$W"/arrets-v1/*.json > "$W/statuts-v1.txt" 2>&1; then
                     ok "-v1 : arrêt consigné sans juge fini ($(tail -1 "$W/statuts-v1.txt"))"
                 else ko "-v1 : $(tail -1 "$W/statuts-v1.txt")"; fi
             else ok "-v1 : ni arrêt ni résumé consignés"; fi
             grep -E '^traces/[^/]+/journal\.txt$' "$W/arbre-v1.txt" > "$W/journaux-v1.txt" || true
             : > "$W/fins-v1.txt"
             # fin d'un juge : ligne « fin= », ou dernier lot « lot=N/N » (le fichier s'écrit juste après : fin possible)
             while read -r f; do git show "FETCH_HEAD:$f" | grep -E '^PROGRES .*( fin=| lot=([0-9]+)/\2( |$))' >> "$W/fins-v1.txt" || true; done < "$W/journaux-v1.txt"
             [ -s "$W/fins-v1.txt" ] && ko "-v1 : traces avec une ligne de fin de juge ou de dernier lot ($(head -1 "$W/fins-v1.txt" | cut -c1-120)) : relancement interdit" \
                 || ok "-v1 : aucune ligne de fin de juge ni de dernier lot dans les traces poussées ($(wc -l < "$W/journaux-v1.txt") journaux lus)"
         else ko "-v1 absente, illisible ou non descendante de S : pas de relancement"; fi ;;
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
PYTHONPATH=src "$PY" - "$P" "$CFG" "$TACHES" "$PILOTE" "$ANALYSE" "$VERSEES" > "$W/bloc-gardes.txt" 2>&1 <<'EOF' && ok "gardes du lanceur des notations (état du pilote, paramètres, versions, citations, 180 notations par juge, graines), valeurs du texte, première lecture" || ko "gardes du lanceur, valeurs ou première lecture : $(tail -1 "$W/bloc-gardes.txt")"
import json, sys
from pathlib import Path
from controle_ia.environnements import noter_pilote_a as npa
from controle_ia.environnements.lancer_pilote_a import exiger_invites
from controle_ia.environnements.pilote_a import charger_taches
from controle_ia.harnais.validation_reelle import exiger_code_cite, exiger_code_importe_sous
from controle_ia.manifeste import verifier_resultat
from controle_ia.scellement import verifier
p, cfg, taches, pilote, analyse, versees = sys.argv[1:7]
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
# marge d'un lot entre l'échéance globale et le délai externe : fixée par les deux égalités ci-dessus (24 000 − 23 100 s ;
# aucune garde propre, qu'aucun artefact ne pourrait atteindre : contre-lecture R2 de la chaîne)
# crédit et surveillance (copies versées) : 7,5 heures ; plafond de la surveillance à la création + 26 400 s, au-dessus du
# plafond de l'amorce et d'un démarrage du conteneur d'au plus 240 s
import re
lanceur = Path(f"{versees}/lancer_notations_v1.sh").read_text(encoding="utf-8")
surv = Path(f"{versees}/surveiller_notations_v1.sh").read_text(encoding="utf-8")
assert re.findall(r"^HEURES_CREDIT=([0-9.]+) ", lanceur, re.M) == ["7.5"], "heures du crédit exigé"
assert re.findall(r"^PLAFOND_S=([0-9]+) ", surv, re.M) == ["26400"], "plafond de la surveillance"
assert 26400 >= 430 * 60 + 240, "surveillance au-dessus du plafond de l'amorce"
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
cp "$W/suite.txt" "$D.suite.txt" 2>/dev/null || true      # gardée à côté du clone (traces du lanceur), nom du dossier neuf
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
# 14. chacun des intitulés lus par le lanceur des notations et par le script de l'instance : exactement une fois
INTITULES=("Configuration des notations (empreinte canonique)" "Run du pilote noté" "Manifeste du pilote noté"
           "Épisodes du pilote noté" "Arrêt du pilote noté" "Commit du code d'analyse" "Entropie" "Tâches du pilote"
           "Tests attendus" "Chemin de la configuration des notations" "Chemin des tâches du pilote noté"
           "Chemin du manifeste du pilote noté" "Chemin des épisodes du pilote noté" "Chemin de l'arrêt du pilote noté")
DOUBLES=""; for x in "${INTITULES[@]}"; do [ "$(grep -oF "$x : \`" "$P" | wc -l)" = 1 ] || DOUBLES="$DOUBLES « $x »"; done
[ -z "$DOUBLES" ] && ok "intitulés lus par le lanceur et le script de l'instance : une fois chacun (${#INTITULES[@]})" \
    || ko "intitulés absents ou cités plusieurs fois :$DOUBLES"
[ "$echec" = 0 ] && echo "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES" || echo "CONTRÔLES AVANT DÉPENSE : ÉCHEC"
[ "$echec" = 0 ]
