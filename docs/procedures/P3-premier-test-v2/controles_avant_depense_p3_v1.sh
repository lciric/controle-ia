#!/usr/bin/env bash
# Brouillon 4 (R-227) : égal au brouillon 3, sauf le dossier des copies versées, docs/procedures/P3-premier-test-v2/ (R12 : le versement du dossier v1 n'est pas réécrit), et, dans les contrôles, le chemin du candidat relu (candidat 4).
# Contrôles avant dépense du premier test boîte blanche sur l'organisme (i-a) (P3, R-192, R-202 ; préenregistrement
# prereg/P3-premier-test-i-a-v1.md), v1, brouillon 3 (contre-lecture R2 de la chaîne traitée : CH-01 à CH-23 ; brouillon 4
# du texte, configuration candidat 3, consignes candidat 2 ; relecture courte traitée : formes exactes de la révocation de
# R-192 et de l'accord de Lazar, borne de stockage, reliées au texte par le bloc 9, RCh-01 à RCh-04 ; candidat relu au
# chemin du candidat 2), déclinés des contrôles des notations refaites du pilote de
# T0.5 (docs/procedures/notations-T0.5-v2/controles_avant_depense_notations_v1.sh) sous un nom nouveau (R12). Sur un clone
# neuf du dépôt de travail au commit de scellement S ; aucun calcul payant ; code 0 si et seulement si tout est conforme ;
# code 2 si les épingles manquent ou sont mal formées, si le module commun manque, ou si le clone est impossible.
# Ce qui est contrôlé : S ajoute le sceau du préenregistrement et n'ajoute que le préenregistrement, la configuration, les
# consignes et leurs sceaux ; commit du code cité une seule fois, ancêtre de S, arbre gelé identique au code cité et au
# code relu épinglé ; modules gelés d'étapes antérieures inchangés (modules de lecture du pilote, pilote_a.py, harnais/,
# sondes/familles.py, modules des notations ; CH-08) ; dépendances égales à celles du commit de scellement du pilote ;
# empreintes des deux scripts de l'instance citées ; pièces présentes à S, scellées, citées par l'empreinte de leur fichier
# (consignes, tâches, provenance et fichiers des données génériques, verdict, préenregistrement et configuration du
# pilote ; la configuration de P3 : citée par son empreinte canonique, relue par les gardes du lanceur au bloc 9) ; GO de
# calcul (GO-2026-10-04-08, le seul accepté, CH-02) et décision de Lazar, non révoqués (CH-09), par le module commun
# verifications_p3_v1.py (le même texte que le scellement et le lanceur) ; texte, configuration et consignes de S égaux
# aux candidats relus, octet pour octet ; journal de la répétition jouet (candidat et consignes répétés, CH-15) ; rapports
# de la contre-lecture présents, scellés, cités, seuls de leur famille ; branche de résultats absente ; ligne
# « Lancement » ; problemes() vide ; sceaux ; verifier-arbre ; gardes du lanceur de P3 rejouées dans l'ordre
# d'executer(), jusqu'au manifeste (rien n'est écrit), paramètres de l'environnement et de la génération égaux à ceux du
# pilote, bornes de la chaîne reliées aux constantes des scripts (durées, crédit, prix, surveillance, cœurs, mémoire
# vive, téléchargement, stockage ; CH-04, CH-10, RCh-04), valeurs citées par le texte, dont les formes exactes de la
# révocation de R-192 et de l'accord de Lazar lues dans la copie versée du module commun (RCh-01 à RCh-03) ; vrai
# tokeniseur de l'agent (bloc 10) : format,
# longueurs des textes privés à l'encodage seul et dans le gabarit sur les 60 tâches, égales entre les trois conditions
# instruites et aux valeurs citées, sans tolérance (CH-12), faits exclus, empans des 2 000 textes « enjeux élevés » tirés
# par les graines du run ; versions de l'environnement de la session égales aux dépendances épinglées, puis suite
# complète des tests au commit S dans cet environnement (CH-20) ; garde de calcul ; lecture précoce du script de
# l'instance ; intitulés lus une fois chacun. Les citations qui peuvent passer à la ligne dans le texte (rapports,
# empreintes des scripts de l'instance) sont lues sur le texte aux espaces réduites. Aucun relancement : une relance
# passe par un nœud de Lazar et une chaîne suivante.
# Usage : controles_avant_depense_p3_v1.sh S DOSSIER_NEUF
set -uo pipefail
[ $# -eq 2 ] || { echo "usage : controles_avant_depense_p3_v1.sh S DOSSIER_NEUF (deux arguments ; aucun relancement)"; exit 2; }
S=$1; D=$(realpath -m "$2")
DEPOT=https://github.com/lciric/controle-ia-travail.git
CANDIDAT_RELU=d975e9817e88d30196930c2a351927c2091f2ac024d2a5b52556730fa36cb672                                                                    # texte relu et vérifié (contre-lecture R2), octet pour octet
CANDIDAT_RELU_CHEMIN=brouillons/P3-premier-test-i-a-v1-candidat4.md
CONFIG_RELUE=702303e9453f7c4ce8f0cf900f45fc8075b75744eedab0b1652dd8e52d55abde                                                                     # configuration relue, octet pour octet
CONFIG_RELUE_CHEMIN=brouillons/P3-premier-test-config-v1-candidat3.json
CONSIGNES_RELUES=a68468fef6286bbcaa31451ba461d0adab2af7d529dd5e4fa0695643e6d1d69c                                                                 # consignes relues, octet pour octet
CONSIGNES_RELUES_CHEMIN=brouillons/P3-consignes-v1-candidat2.md
RAPPORTS_ATTENDUS="P3-premier-test-v1-relecture-chaine-v1.md=57060da8f239f6c894978a187668f5f75d2b214cd25e9c7e3463b32dd7461db6 P3-premier-test-v1-relecture-courte-chaine-v1.md=dd9841f0f2e3342b2734417fecd44d75fd66b128e96272139176b509ff992069 P3-premier-test-v1-relecture-courte-code-v1.md=3589ad6f899ef676209ebd4a37f0ce8a7418e2108d3bfa3649171fde881e5adc P3-premier-test-v1-relecture-courte-texte-v1.md=c685659a120f7071e707503d16b978fa9830562fcf49b6d910a53d7b8c50e57a P3-premier-test-v1-relecture-texte-code-v1.md=98d7201b0c3671d28a8cc05e4f744a86cd6fa544a5eca02826339baaa2263c5f"                                                              # paires nom=empreinte (contre-lectures R2 et relecture courte)
CODE_RELU=7a54d431d89745839220f882b41b13e8c62ecfdd                                                                        # commit du code relu : arbre gelé de S égal
REPETITION_JOUET=1c1e86dd34095034667b7a2a486f51376db16decbd43bea70903c385cc5b7c8a                                                                 # empreinte du journal de la répétition jouet au code relu
REPETITION_JOUET_CHEMIN=docs/procedures/P3-premier-test-v2/repetition-jouet-p3-v1.log
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
H=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/p3-v1
VERIF=$H/verifications_p3_v1.py                      # module commun (égal à sa copie versée : le lanceur le vérifie)
VERSEES=docs/procedures/P3-premier-test-v2
P=prereg/P3-premier-test-i-a-v1.md; CFG=prereg/P3-premier-test-config-v1.json; CONSIGNES=prereg/P3-consignes-v1.md
S_PILOTE=1c6c900819640e8320ab85a07b3abd4937e22d5f            # commit de scellement du pilote (dépendances installées)
TACHES=donnees/t05-pilote-v1/taches-pilote-60-v1.json
PREREG_PILOTE=prereg/T0.5-pilote-8B-v1.md; CONFIG_PILOTE=prereg/T0.5-pilote-config-v1.json
PREREG_NOTATIONS=prereg/T0.5-pilote-notations-v1.md          # cite le commit du code des notations (modules gelés, CH-08)
VERDICT=docs/verdicts/verdict-T0.5-pilote-v1.md
PROVENANCE=docs/sources/donnees-T0.7/provenance-donnees-sondes-v1.md
FAITS=donnees/T0.7-faits-repe-v1/facts_true_false.csv; ENJEUX=donnees/T0.7-models-under-pressure-v1/training/train.jsonl
AMORCE=scripts/amorce_instance_p3.sh; INSTANCE=scripts/p3_instance.sh
BRANCHE=calcul/p3-reel-v1
echec=0; ok() { echo "OK  $*"; }; ko() { echo "KO  $*"; echec=1; }
plat() { tr '\n' ' ' < "$1" | tr -s ' '; }      # texte aux espaces réduites : citations passées à la ligne
[[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "S invalide"; exit 2; }
[ -n "$2" ] || { echo "dossier neuf absent"; exit 2; }
[ -e "$D" ] && { echo "$D existe déjà"; exit 2; }
[[ "$CODE_RELU" =~ ^[0-9a-f]{40}$ && "$REPETITION_JOUET" =~ ^[0-9a-f]{64}$ ]] || { echo "code relu ou répétition jouet non épinglés"; exit 2; }
[[ "$CANDIDAT_RELU" =~ ^[0-9a-f]{64}$ && "$CANDIDAT_RELU_CHEMIN" == brouillons/* ]] || { echo "candidat relu non épinglé"; exit 2; }
[[ "$CONFIG_RELUE" =~ ^[0-9a-f]{64}$ && "$CONFIG_RELUE_CHEMIN" == brouillons/* ]] || { echo "configuration relue non épinglée"; exit 2; }
[[ "$CONSIGNES_RELUES" =~ ^[0-9a-f]{64}$ && "$CONSIGNES_RELUES_CHEMIN" == brouillons/* ]] || { echo "consignes relues non épinglées"; exit 2; }
n_paires=0
for paire in $RAPPORTS_ATTENDUS; do [[ "$paire" =~ ^P3-premier-test-v1-[a-z0-9-]+-v1\.(md|json|tar)=[0-9a-f]{64}$ ]] \
    || { echo "rapports attendus mal formés : $paire"; exit 2; }; n_paires=$((n_paires+1)); done
[ "$n_paires" -ge 2 ] || { echo "rapports attendus : au moins les deux rapports des contre-lectures R2"; exit 2; }
W="$D.travail"                                   # fichiers de travail dans un dossier neuf, à côté du clone
[ -e "$W" ] && { echo "$W existe déjà"; exit 2; }
[ -e "$D.suite.txt" ] && { echo "$D.suite.txt existe déjà (R12)"; exit 2; }
[ -f "$VERIF" ] || { echo "module commun $VERIF absent"; exit 2; }
mkdir -p "$W" || exit 2
trap 'rm -rf "$W"' EXIT                          # fichiers de travail jamais laissés, même sur un arrêt précoce
git clone -q "$DEPOT" "$D" || { echo "clonage impossible"; exit 2; }
cd "$D" && git checkout -q "$S" || { echo "commit $S introuvable"; exit 2; }
# 1. contenu de S : les six fichiers, tous ajoutés par S
[ "$(git log --diff-filter=A -1 --format=%H -- "$P.sha256")" = "$S" ] && ok "S ajoute le sceau du préenregistrement" || ko "S n'est pas le commit qui ajoute $P.sha256"
attendus_s=$(printf '%s\n' "$CFG" "$CFG.sha256" "$CONSIGNES" "$CONSIGNES.sha256" "$P" "$P.sha256" | sort | tr '\n' ' ')
[ "$(git diff --name-only --no-renames "$S^" "$S" | sort | tr '\n' ' ')" = "$attendus_s" ] && \
    [ "$(git diff --name-only --no-renames --diff-filter=A "$S^" "$S" | sort | tr '\n' ' ')" = "$attendus_s" ] \
    && ok "S n'ajoute que le préenregistrement, la configuration, les consignes et leurs sceaux" \
    || ko "contenu de S inattendu : $(git diff --name-status --no-renames "$S^" "$S" | tr '\t\n' '  ')"
# 2. commit du code : cité une seule fois, ancêtre de S, arbre gelé identique au code cité et au code relu
NC=$(grep -c "Commit du code d'analyse : \`" "$P" || true)
CODE=$(sed -n "s/.*Commit du code d'analyse : \`\([0-9a-f]\{40\}\)\`.*/\1/p" "$P" | head -1)
if [ "$NC" = 1 ] && [[ "$CODE" =~ ^[0-9a-f]{40}$ ]] && git merge-base --is-ancestor "$CODE" "$S" 2>/dev/null; then ok "commit du code cité une fois, $CODE, ancêtre de S"
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
else ko "CHEMINS_GELES illisible"; fi      # garde redondante (module importé par tout le reste), sans artefact possible (CH-14)
# modules gelés d'étapes antérieures, que le texte dit non touchés (contre-lecture de la chaîne, CH-08) : égaux au commit
# cité par le préenregistrement du pilote (modules de lecture MODULES_LECTURE, pilote_a.py, harnais/, sondes/familles.py)
# et au commit cité par celui des notations (noter_pilote_a.py, lire_notations_pilote.py)
NCP=$(grep -c "^- Commit du code d'analyse : \`" "$PREREG_PILOTE" 2>/dev/null || true)
NCN=$(grep -c "^- Commit du code d'analyse : \`" "$PREREG_NOTATIONS" 2>/dev/null || true)
C_PILOTE=$(sed -n "s/^- Commit du code d'analyse : \`\([0-9a-f]\{40\}\)\`.*/\1/p" "$PREREG_PILOTE" 2>/dev/null | head -1)
C_NOTATIONS=$(sed -n "s/^- Commit du code d'analyse : \`\([0-9a-f]\{40\}\)\`.*/\1/p" "$PREREG_NOTATIONS" 2>/dev/null | head -1)
MODULES=$(PYTHONPATH=src "$PY" -c "from controle_ia.environnements.lire_pilote import MODULES_LECTURE; print(' '.join(MODULES_LECTURE))" 2>/dev/null)
if [ "$NCP" = 1 ] && [ "$NCN" = 1 ] && [[ "$C_PILOTE" =~ ^[0-9a-f]{40}$ && "$C_NOTATIONS" =~ ^[0-9a-f]{40}$ ]] && [ -n "$MODULES" ]; then
    # shellcheck disable=SC2086
    git diff --quiet "$C_PILOTE" "$S" -- $MODULES src/controle_ia/environnements/pilote_a.py src/controle_ia/harnais \
        src/controle_ia/sondes/familles.py; c1=$?
    git diff --quiet "$C_NOTATIONS" "$S" -- src/controle_ia/environnements/noter_pilote_a.py \
        src/controle_ia/environnements/lire_notations_pilote.py; c2=$?
    if [ "$c1" = 0 ] && [ "$c2" = 0 ]; then
        ok "modules gelés d'étapes antérieures inchangés (pilote ${C_PILOTE:0:12} : lecture, pilote_a.py, harnais/, sondes/familles.py ; notations ${C_NOTATIONS:0:12})"
    else ko "modules gelés d'étapes antérieures modifiés (pilote : code $c1 ; notations : code $c2)"; fi
else ko "commits cités par le pilote ou par les notations, ou MODULES_LECTURE, illisibles"; fi
# dépendances que l'instance installe : égales à celles du commit de scellement du pilote (le run de P3 n'a pas de garde
# des versions ; ses versions ne sont comparées à celles du pilote qu'à la récupération, contrôle 3f ; CH-20)
git diff --quiet "$S_PILOTE" "$S" -- requirements-cpu.txt requirements-gpu.txt requirements-donnees.txt; c=$?
[ "$c" = 0 ] && ok "dépendances (requirements-cpu, -gpu, -donnees) égales à celles du pilote (${S_PILOTE:0:12})" \
    || ko "dépendances différentes de celles du pilote (${S_PILOTE:0:12}), code $c"
for f in "$AMORCE" "$INSTANCE"; do
    e=$(git show "$S:$f" 2>/dev/null | sha256sum | cut -d' ' -f1)
    plat "$P" | grep -qF "\`$f\` (\`$e\`, sha256)" && ok "empreinte de $f citée ($e)" || ko "empreinte de $f ($e) non citée"
done
# 3. pièces : présentes à S avec leur sceau entier ; citées par l'empreinte de leur fichier (la configuration de P3 l'est
# par son empreinte canonique : bloc 9)
for f in "$CFG" "$CONSIGNES" "$TACHES" "$PREREG_PILOTE" "$CONFIG_PILOTE" "$VERDICT" "$PROVENANCE" "$FAITS" "$ENJEUX"; do
    if git cat-file -e "$S:$f" 2>/dev/null && git cat-file -e "$S:$f.sha256" 2>/dev/null && \
       [ "$(git show "$S:$f.sha256")" = "$(git show "$S:$f" | sha256sum | cut -d' ' -f1)  $(basename "$f")" ]; then
        ok "$f et son sceau entier dans l'arbre de S"
    else ko "$f ou son sceau absent ou non conforme"; fi
done
for f in "$CONSIGNES" "$TACHES" "$PREREG_PILOTE" "$CONFIG_PILOTE" "$VERDICT" "$PROVENANCE" "$FAITS" "$ENJEUX"; do
    e=$(git show "$S:$f" 2>/dev/null | sha256sum | cut -d' ' -f1)
    grep -qF "\`$e\`" "$P" && ok "$f cité par son empreinte ($e)" || ko "$f non cité par son empreinte"
done
# 4. GO de calcul et décision de Lazar : une ligne de forme fixe ; GO-2026-10-04-08 seulement, de type « calcul »,
# accordé par Lazar, non révoqué ; ligne R-… qui cite la décision, non révoquée (module commun)
python3 -I "$VERIF" go "$P" registres/go.md registres/decisions.md > "$W/bloc-go.txt" 2>&1 \
    && ok "GO de calcul et décision de Lazar : GO-2026-10-04-08, non révoqué, décision au registre, non révoquée" \
    || ko "GO de calcul et décision de Lazar (GO, révocation ou registre) : $(tail -1 "$W/bloc-go.txt")"
sed 's/^/    /' "$W/bloc-go.txt"
# 5. texte, configuration et consignes de S = candidats relus, versés et scellés à l'empreinte épinglée
releve() {   # $1 fichier de S, $2 chemin du relu versé, $3 empreinte épinglée, $4 nom du relu, $5 accord (e, es ou rien)
    [ "$(git show "$S:$2" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$3" ] && \
        [ "$(git show "$S:$2.sha256" 2>/dev/null)" = "$3  $(basename "$2")" ] \
        && ok "$4 versé$5, scellé$5, à l'empreinte épinglée" || ko "$4 absent$5, non scellé$5 ou d'empreinte différente"
    [ "$(sha256sum "$1" | cut -d' ' -f1)" = "$3" ] && ok "$1 de S = $4, octet pour octet" || ko "$1 de S ≠ $4"
}
releve "$P" "$CANDIDAT_RELU_CHEMIN" "$CANDIDAT_RELU" "candidat relu" ""
releve "$CFG" "$CONFIG_RELUE_CHEMIN" "$CONFIG_RELUE" "configuration relue" "e"
releve "$CONSIGNES" "$CONSIGNES_RELUES_CHEMIN" "$CONSIGNES_RELUES" "consignes relues" "es"
# 6. journal de la répétition jouet : épinglé, scellé, au code relu, au candidat et aux consignes relus (CH-15) ;
# passages et récupérations attendus, KO des artefacts compris ; scripts exécutés égaux à leurs copies versées à S
git show "$S:$REPETITION_JOUET_CHEMIN" > "$W/journal-repetition.txt" 2>/dev/null
python3 -I "$VERIF" repetition "$CODE_RELU" "$W/journal-repetition.txt" "$(basename "$CANDIDAT_RELU_CHEMIN")" "$CANDIDAT_RELU" \
    "$(basename "$CONSIGNES_RELUES_CHEMIN")" "$CONSIGNES_RELUES" > "$W/bloc-repetition.txt" 2>&1
c=$?
CAUSE_REP=""
[ "$c" = 0 ] || CAUSE_REP=$(tail -1 "$W/bloc-repetition.txt")
if [ -z "$CAUSE_REP" ]; then
    grep -E '^[a-z0-9_]+_v1\.(py|sh) [0-9a-f]{64}$' "$W/bloc-repetition.txt" > "$W/scripts-repetes.txt"
    # « deux scripts répétés » : garde redondante (le module exige déjà les deux, exactement), sans artefact possible (CH-14)
    [ "$(wc -l < "$W/scripts-repetes.txt")" = 2 ] || CAUSE_REP="deux scripts répétés attendus"
    while read -r s e; do
        [ "$(git show "$S:$VERSEES/$s" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$e" ] || CAUSE_REP="script répété ≠ copie versée à S : $s"
    done < "$W/scripts-repetes.txt"
fi
if [ -z "$CAUSE_REP" ]; then
    { [ "$(git show "$S:$REPETITION_JOUET_CHEMIN" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$REPETITION_JOUET" ] && \
      [ "$(git show "$S:$REPETITION_JOUET_CHEMIN.sha256" 2>/dev/null)" = "$REPETITION_JOUET  $(basename "$REPETITION_JOUET_CHEMIN")" ]; } \
        || CAUSE_REP="journal absent de S, d'une autre empreinte que l'épingle, ou sceau différent"
fi
if [ -z "$CAUSE_REP" ]; then
    ok "répétition jouet au code relu, au candidat et aux consignes relus : journal épinglé, scellé ; trois passages, quatre récupérations conformes et une des traces seules, dix-huit artefacts refusés à leur KO ; scripts exécutés = copies versées à S"
else ko "répétition jouet : $CAUSE_REP"; fi
# 7. rapports de la contre-lecture : présents à S, scellés, cités (texte aux espaces réduites) ; seuls de leur famille
for paire in $RAPPORTS_ATTENDUS; do
    nom=${paire%%=*}; e=${paire#*=}; f="prereg/contre-lectures/$nom"
    if [ "$(git show "$S:$f" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$e" ] && [ "$(git show "$S:$f.sha256" 2>/dev/null)" = "$e  $nom" ]; then
        plat "$P" | grep -qF "\`$f\` (\`$e\`)" && ok "rapport $nom présent, scellé, cité" || ko "rapport $nom présent et scellé, mais non cité par le texte"
    else ko "rapport $nom absent, non scellé ou d'empreinte différente"; fi
done
git ls-tree -r --name-only "$S" prereg/contre-lectures/ > "$W/contre-lectures.txt"
presents=$(grep -E '^prereg/contre-lectures/P3-premier-test-v1-' "$W/contre-lectures.txt" | grep -v '\.sha256$' | xargs -r -n1 basename | sort | tr '\n' ' ')
attendus=$(for paire in $RAPPORTS_ATTENDUS; do echo "${paire%%=*}"; done | sort | tr '\n' ' ')
[ "$presents" = "$attendus" ] && ok "rapports de P3 présents à S = rapports attendus ($n_paires)" || ko "rapports présents « $presents » ≠ attendus « $attendus »"
# 8. branche de résultats absente ; ligne « Lancement » ; problemes() ; sceaux ; arbre
git ls-remote --exit-code origin "refs/heads/$BRANCHE" >/dev/null 2>&1; c=$?
[ "$c" = 2 ] && ok "branche $BRANCHE absente" || ko "branche $BRANCHE : code $c (2 attendu)"
grep -qF "\`PREREG=$P\`, \`BRANCHE=$BRANCHE\`" "$P" && ok "PREREG et BRANCHE ($BRANCHE) cités par la ligne « Lancement »" || ko "PREREG ou BRANCHE : la ligne « Lancement » cite autre chose"
PYTHONPATH=src "$PY" -c "from controle_ia.prereg import problemes; p = problemes('$P'); print(p); raise SystemExit(1 if p else 0)" \
    && ok "problemes() vide" || ko "problemes() non vide"
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier "$P" "$CFG" "$CONSIGNES" "$TACHES" "$FAITS" "$ENJEUX" >/dev/null \
    && ok "sceaux du préenregistrement, de la configuration, des consignes, des tâches et des données génériques" || ko "sceaux"
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier-arbre . > "$W/verifier-arbre.txt" 2>&1
# dernière ligne de verifier-arbre : garde redondante (le code de sortie suffirait), sans artefact propre (CH-14)
if tail -1 "$W/verifier-arbre.txt" | grep -qx "arbre intact"; then ok "verifier-arbre : arbre intact"
else ko "verifier-arbre : $(grep '^ÉCHEC' "$W/verifier-arbre.txt" | head -5 | tr '\n' ' ')"; fi
# 9. gardes du lanceur de P3 rejouées dans l'ordre d'executer(), jusqu'au manifeste (rien n'est écrit ; la garde de la
# mémoire vive porte sur l'instance, pas sur cette machine) ; paramètres du pilote ; bornes de la chaîne reliées aux
# constantes des scripts de l'instance et des copies versées ; valeurs citées par le texte (aux espaces réduites)
PYTHONPATH=src "$PY" - "$P" "$CFG" "$TACHES" "$CONFIG_PILOTE" "$VERSEES" > "$W/bloc-gardes.txt" 2>&1 <<'EOF' && ok "gardes du lanceur de P3 (configuration, citations, tâches, consignes, données génériques, graines), paramètres du pilote, bornes de la chaîne, valeurs du texte" || ko "gardes du lanceur, paramètres, bornes ou valeurs : $(tail -1 "$W/bloc-gardes.txt")"
import json, re, sys
from pathlib import Path
from controle_ia.environnements.invites import charger_invite
from controle_ia.environnements.pilote_a import charger_taches
from controle_ia.harnais.validation_reelle import exiger_code_cite, exiger_code_importe_sous
from controle_ia.manifeste import graines
from controle_ia.premier_test_ia import donnees as dn
from controle_ia.premier_test_ia import run as rp
from controle_ia.premier_test_ia.conditions import charger_consignes
from controle_ia.scellement import verifier
p, cfg, taches, cfg_pilote, versees = sys.argv[1:6]
racine = Path(".")
c = json.loads(Path(cfg).read_text(encoding="utf-8"))
rp.exiger_config_p3(c)
assert c["mode"] == "reel", f"mode {c['mode']}"
assert c["duree_max_s"] == 16200 and c["budget_entrainement_s"] == 3600, "durées de la configuration"
assert c["n_faits_max"] is None, "n_faits_max non nul : les faits comptés au bloc 10 ne seraient plus ceux du run (CH-19)"
assert c["chemin_consignes"] == "prereg/P3-consignes-v1.md", "chemin des consignes de la configuration"
# environnement et génération : ceux du pilote (même agent, même révision, mêmes réglages d'épisode et de garde)
pil = json.loads(Path(cfg_pilote).read_text(encoding="utf-8"))
communs = ("N", "T", "actions_min_controle_negatif", "agent", "couches", "fils", "fraction_equivalence",
           "fraction_min_controle_negatif", "lot", "max_nouveaux", "noyau_attention", "positions_min_controle_negatif",
           "statistique_equivalence", "temperature", "tolerance_equivalence")
autres = [k for k in communs if c.get(k) != pil.get(k)]
assert not autres, f"paramètres différents de ceux du pilote : {autres}"
# bornes des scripts de l'instance (délai externe du run, plafond de l'amorce) et des copies versées (crédit, prix,
# surveillance, offre) : une seule ligne chacune, à la valeur du préenregistrement
inst = Path("scripts/p3_instance.sh").read_text(encoding="utf-8")
amorce = Path("scripts/amorce_instance_p3.sh").read_text(encoding="utf-8")
assert inst.count("DELAI=(timeout --signal=TERM --kill-after=5m 300m)") == 1, "délai externe du run"
assert amorce.count("timeout --signal=TERM --kill-after=5m 360m ") == 1, "plafond de l'amorce"
lanceur = Path(f"{versees}/lancer_p3_v1.sh").read_text(encoding="utf-8")
surv = Path(f"{versees}/surveiller_p3_v1.sh").read_text(encoding="utf-8")
cinq = Path(f"{versees}/controle_cinq_minutes_p3_v1.sh").read_text(encoding="utf-8")
def constante(texte, nom, motif=r"[0-9.]+"):
    return re.findall(rf"^{nom}=({motif}) ", texte, re.M)
assert constante(lanceur, "HEURES_CREDIT") == ["6.5"], "heures du crédit exigé"
assert constante(lanceur, "PRIX_MAX") == ["1.30"], "prix plafond du lanceur"
assert constante(cinq, "PRIX_MAX") == ["1.30"], "prix plafond du contrôle à cinq minutes"
assert constante(lanceur, "PLAFOND_SURVEILLANCE_S") == ["22200"], "plafond de la surveillance écrit par le lanceur"
assert constante(surv, "PLAFOND_S") == ["22200"], "plafond de la surveillance"
assert constante(lanceur, "COEURS_MIN") == ["16"], "cœurs effectifs exigés de l'offre"
assert constante(lanceur, "MEMOIRE_VIVE_MIN_MO") == ["128000"], "mémoire vive exigée de l'offre"
tel = constante(lanceur, "TELECHARGEMENT_MAX", r"[^ ]+")
assert len(tel) == 1 and re.fullmatch(r"0\.[0-9]{2,4}", tel[0]), f"borne de téléchargement du lanceur non fixée ({tel})"
sto = constante(lanceur, "STOCKAGE_MAX", r"[^ ]+")
assert len(sto) == 1 and re.fullmatch(r"0\.[0-9]{2,4}", sto[0]), f"borne de stockage du lanceur non fixée ({sto})"
# formes exactes de la révocation de R-192 et de l'accord de Lazar : lues dans la copie versée du module commun, citées
# mot pour mot par le texte (relecture courte, RCh-01 à RCh-03)
module = Path(f"{versees}/verifications_p3_v1.py").read_text(encoding="utf-8")
prefixes = [re.findall(rf'^{n} = "([^"]+)"', module, re.M) for n in ("PREFIXE_REVOCATION", "PREFIXE_ACCORD")]
assert all(len(x) == 1 for x in prefixes), f"formes exactes du module commun illisibles : {prefixes}"
texte = " ".join(Path(p).read_text(encoding="utf-8").split())
valeurs = ("16 200 s", "3 600 s", "300 minutes", "360 minutes", "22 200 s", "6,5 heures", "8,02 USD", "0,22 USD",
           "16 cœurs effectifs", "128 000 Mo", "72 heures", "7 faits", "200 sondes", "= 240 épisodes",
           "51 jetons pour chacune des trois consignes", "10 pour chacune des trois indications",
           "52 jetons pour les trois consignes sur 56 tâches et 51 sur 4", "10 pour les trois indications",
           f"téléchargement au plus {tel[0].replace('.', ',')} USD par Go",
           f"stockage au plus {sto[0].replace('.', ',')} USD de l'heure", prefixes[0][0], prefixes[1][0])
for s in valeurs:
    assert s in texte, f"valeur non citée par le texte : {s}"
# gardes d'executer(), dans l'ordre, jusqu'au manifeste
t = charger_taches(taches)
sha_t = verifier(taches)
consignes = charger_consignes(c["chemin_consignes"], c["consignes_sha256"])
charger_invite("H1-classification")
exiger_code_importe_sous(racine)
commit = exiger_code_cite(racine, Path(p))
ent = rp.exiger_citations_p3(Path(p), c, sha_t)
plan = rp.plan_p3(t)
assert len(plan) == 240, f"{len(plan)} épisodes au plan, 240 cités"
g = graines(rp.cles_des_graines(t, c), ent)
# données génériques : empreintes de la provenance (chargeurs du run)
faits = dn.charger_faits()
enjeux = dn.charger_enjeux()
print("commit cité :", commit, "; entropie citée :", ent, "; épisodes :", len(plan), "; graines :", len(g),
      "; faits :", len(faits), "; textes « enjeux élevés » :", len(enjeux), "; consignes :", consignes["sha256"][:12],
      "; téléchargement au plus", tel[0], "USD par Go ; stockage au plus", sto[0], "USD de l'heure")
EOF
sed 's/^/    /' "$W/bloc-gardes.txt"
# 10. vrai tokeniseur de l'agent (révision du pilote) : format et texte attendu dans l'ouverture ; longueurs des textes
# privés à l'encodage seul et dans le gabarit, sur les 60 tâches : égales tâche par tâche entre les trois conditions
# instruites et égales aux valeurs citées, sans tolérance (CH-12 ; un texte privé absent du gabarit, garde redondante avec
# celle des blocs vides des consignes, est refusé aussi) ; faits exclus au compte cité (n_faits_max appliqué comme au run,
# CH-19) ; 2 000 textes « enjeux élevés » tirés par les graines du run, empans vérifiés contre le rendu
HF_HOME="$W/cache-hf" PYTHONPATH=src "$PY" - "$P" "$CFG" "$TACHES" > "$W/bloc-tokeniseur.txt" 2>&1 <<'EOF' && ok "vrai tokeniseur de l'agent : format, textes privés (encodage seul et gabarit, 60 tâches), faits exclus, empans des textes « enjeux élevés »" || ko "vrai tokeniseur de l'agent : $(tail -1 "$W/bloc-tokeniseur.txt")"
import json, sys
from collections import Counter
from pathlib import Path
from controle_ia.environnements import lancer_pilote_a as lp
from controle_ia.environnements.invites import charger_invite
from controle_ia.environnements.pilote_a import charger_taches, tache_de
from controle_ia.manifeste import generateur, graines
from controle_ia.premier_test_ia import donnees as dn
from controle_ia.premier_test_ia import run as rp
from controle_ia.premier_test_ia.conditions import INSTRUITES, charger_consignes, environnement
from controle_ia.premier_test_ia.entrainement import preparer_enjeux, preparer_tromperie
from controle_ia.scellement import verifier
ENCODAGE = {"consigne": 51, "indication": 10}          # valeurs citées par le texte (bloc 9), encodage seul
GABARIT_CONSIGNES = {52: 56, 51: 4}                    # jetons ajoutés au premier pas : nombre de tâches par valeur
GABARIT_INDICATIONS = {10: 60}
p, cfg, taches = sys.argv[1:4]
c = json.loads(Path(cfg).read_text(encoding="utf-8"))
fmt = lp.charger_format_seul(c["agent"], "reel")
f = rp.controler_format_agent(fmt, c["agent"], "reel")
assert f["verifie"] is True, f"format de l'agent non vérifié : {f.get('motif')}"
print("format :", f["format"], "; texte attendu :", f["texte_attendu_ouverture"], "; jetons :", f["jetons"])
t = charger_taches(taches)
consignes = charger_consignes(c["chemin_consignes"], c["consignes_sha256"])
guide = charger_invite("H1-classification")
for k in INSTRUITES:
    for quoi, attendu in ENCODAGE.items():
        n = len(fmt.tok.encode(consignes[k][quoi], add_special_tokens=False))
        assert n == attendu, f"{k}, {quoi} : {n} jetons à l'encodage seul, {attendu} cités"
lc_tout, li_tout, inegales = Counter(), Counter(), []
for tache in t:
    envs = {k: environnement(k, tache_de(tache), c["T"], guide, consignes) for k in ("honnete",) + INSTRUITES}
    def n(k_sys, k_obs):
        return len(fmt.ouverture(envs[k_sys].consigne_privee(0), envs[k_obs].observation(0, 0, [])))
    base = n("honnete", "honnete")
    lc = [n(k, "honnete") - base for k in INSTRUITES]
    li = [n("honnete", k) - base for k in INSTRUITES]
    if len(set(lc)) != 1 or len(set(li)) != 1 or min(lc) <= 0 or min(li) <= 0:
        inegales.append(f"{tache['identifiant']} {lc} {li}")
    lc_tout[lc[0]] += 1
    li_tout[li[0]] += 1
print("jetons ajoutés dans le gabarit (valeur : tâches), consignes :", dict(lc_tout), "; indications :", dict(li_tout))
assert not inegales, f"longueurs inégales entre les conditions instruites, ou texte privé absent du gabarit : {inegales[:3]}"
assert dict(lc_tout) == GABARIT_CONSIGNES, f"consignes dans le gabarit {dict(lc_tout)} ≠ valeurs citées {GABARIT_CONSIGNES}"
assert dict(li_tout) == GABARIT_INDICATIONS, f"indications dans le gabarit {dict(li_tout)} ≠ valeurs citées {GABARIT_INDICATIONS}"
faits = dn.charger_faits()
if c["n_faits_max"] is not None:
    faits = faits[:int(c["n_faits_max"])]
ex_t, exclus = preparer_tromperie(fmt, dn.exemples_tromperie(faits), c["retrait_fin_tromperie"])
assert len(exclus) == c["faits_exclus_attendus"], f"{len(exclus)} faits exclus ({exclus}) ; {c['faits_exclus_attendus']} cités"
ent = rp.exiger_citations_p3(Path(p), c, verifier(taches))
g = graines(rp.cles_des_graines(t, c), ent)
tir = dn.tirer_enjeux(dn.charger_enjeux(), generateur(g["tirage-enjeux"]), c["n_par_classe_enjeux"])
ex_e = preparer_enjeux(fmt, tir, c["max_jetons_enjeux"])
print("faits exclus :", len(exclus), "; exemples de tromperie :", len(ex_t), "; textes « enjeux élevés » :", len(ex_e),
      "; jetons d'empan (tromperie, enjeux) :", sum(x["fin"] - x["debut"] for x in ex_t), sum(x["fin"] - x["debut"] for x in ex_e))
EOF
sed 's/^/    /' "$W/bloc-tokeniseur.txt"
rm -rf "$W/cache-hf"
# 11. environnement de la session (venv-gpu-neuf, déjà installé : pas un environnement neuf, CH-20) : versions égales aux
# dépendances épinglées de S ; puis suite complète des tests au commit S dans cet environnement
PYTHONPATH=src "$PY" - > "$W/bloc-versions.txt" 2>&1 <<'EOF' && ok "environnement des contrôles : versions égales aux dépendances épinglées de S" || ko "environnement des contrôles : $(tail -1 "$W/bloc-versions.txt")"
import re
from importlib import metadata
ecarts, n = [], 0
for f in ("requirements-cpu.txt", "requirements-gpu.txt", "requirements-donnees.txt"):
    for ligne in open(f, encoding="utf-8"):
        ligne = ligne.split("#")[0].strip()
        if not ligne or ligne.startswith("-r "):
            continue
        m = re.fullmatch(r"([A-Za-z0-9_.\-]+)==(\S+)", ligne)
        if not m:
            ecarts.append(f"{f} : ligne non épinglée « {ligne} »")
            continue
        n += 1
        try:
            v = metadata.version(m.group(1))
        except metadata.PackageNotFoundError:
            v = None
        if v != m.group(2):
            ecarts.append(f"{m.group(1)} {v} ≠ {m.group(2)}")
print(f"{n} dépendances épinglées relues ; écarts : {ecarts}")
raise SystemExit(1 if ecarts or not n else 0)
EOF
sed 's/^/    /' "$W/bloc-versions.txt"
a=$(sed -n "s/.*Tests attendus : \`\([0-9]*\)\`.*/\1/p" "$P" | head -1)
PYTHONPATH=src "$PY" -m pytest -q -p no:cacheprovider > "$W/suite.txt" 2>&1; cs=$?
derniere=$(grep -v '^$' "$W/suite.txt" | tail -1)
cp "$W/suite.txt" "$D.suite.txt" 2>/dev/null || true      # gardée à côté du clone (traces du lanceur), nom du dossier neuf
[ "$cs" = 0 ] && [[ "$derniere" =~ ^$a\ passed(,\ [0-9]+\ warnings?)?\ in\ [0-9.]+s(\ \([0-9]+:[0-9]{2}:[0-9]{2}\))?$ ]] \
    && ok "suite complète au commit S, environnement de la session : « $derniere »" || ko "suite complète : « $derniere » (code $cs ; $a attendus)"
# 12. garde de calcul sur le registre de S
echo '{"tool_input":{"command":"GO_ID=GO-2026-10-04-08 vastai create instance 1 --raw"}}' | python3 .claude/hooks/garde_calcul.py \
    && ok "garde de calcul : registres/go.md de S lisible, GO-2026-10-04-08 accepté" || ko "garde de calcul sur le registre de S"
# 13. lecture précoce du script de l'instance : chaque citation une seule fois, chemins attendus
lire_unique() { [ "$(grep -c "$1 : \`" "$P" || true)" = 1 ] && sed -n "s/.*$1 : \`\\([^\`]*\\)\`.*/\\1/p" "$P"; }
L_TESTS=$(lire_unique "Tests attendus"); L_CFG=$(lire_unique "Chemin de la configuration de P3")
L_T=$(lire_unique "Chemin des tâches de P3"); L_C=$(lire_unique "Chemin des consignes de P3")
echo "lecture précoce (script de l'instance, PREREG=$P) : tests $L_TESTS ; configuration $L_CFG ; tâches $L_T ; consignes $L_C"
[ "$L_TESTS" = "$a" ] && [ "$L_CFG" = "$CFG" ] && [ "$L_T" = "$TACHES" ] && [ "$L_C" = "$CONSIGNES" ] \
    && ok "lecture précoce : citations uniques, chemins attendus" || ko "lecture précoce : citation absente, en double, ou chemin inattendu"
# 14. chacun des intitulés lus par le lanceur de P3, le module commun et le script de l'instance : exactement une fois
INTITULES=("Configuration de P3 (empreinte canonique)" "Tâches de P3" "Commit du code d'analyse" "Entropie"
           "Tests attendus" "Chemin de la configuration de P3" "Chemin des tâches de P3" "Chemin des consignes de P3"
           "GO de calcul et décision de Lazar")
DOUBLES=""; for x in "${INTITULES[@]}"; do [ "$(grep -oF "$x : \`" "$P" | wc -l)" = 1 ] || DOUBLES="$DOUBLES « $x »"; done
[ -z "$DOUBLES" ] && ok "intitulés lus par le lanceur, le module commun et le script de l'instance : une fois chacun (${#INTITULES[@]})" \
    || ko "intitulés absents ou cités plusieurs fois :$DOUBLES"
[ "$echec" = 0 ] && echo "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES" || echo "CONTRÔLES AVANT DÉPENSE : ÉCHEC"
[ "$echec" = 0 ]
