#!/usr/bin/env bash
# Création de l'instance des notations décisives refaites du pilote de T0.5 (N-021, option (a), GO-2026-10-12-02 ;
# préenregistrement prereg/T0.5-pilote-notations-v1.md), v2 : option (c) de R-180, décidée par Lazar (R-190). Seule
# différence de fond avec le v1 : aucune offre en argument ; après les contrôles avant dépense, le lanceur relit les offres
# au filtre du plan et prend la moins chère des offres conformes (A100 SXM4 sur AMD EPYC 7513, prix lisible au plus
# PRIX_MAX ; à prix égal, le plus petit identifiant), au lieu d'exiger l'identifiant reçu une vingtaine de minutes plus tôt
# (huit appels du v1, huit arrêts avant la création, R-177 à R-190). Le lanceur v2 est égal à sa copie versée et scellée au
# commit C3 qui l'ajoute sous docs/procedures/notations-T0.5-v3/, descendant de S ; les douze autres scripts de la chaîne
# restent égaux à leurs copies versées à S ; la preuve de son banc (banc-lanceur-notations-v2.log, versé à C3) s'ajoute
# aux cinq journaux de S. Tout le reste est le v1, recopié. Contre-lecture R2 du v2 (18 constats, LV-01 à LV-18,
# traitement versé avec ce lanceur) : prix fini et strictement positif ; champs numériques du filtre (80 Go, une carte)
# relus localement ; machine et hôte archivés ; offres relues gardées (offres-relues.json) ; en relancement, offres de la
# machine ou de l'hôte du premier lancement écartées (option (a) de LV-02, nœud soumis à Lazar avant toute relance) ;
# constantes du devis et du filtre égales à celles du lanceur v1 versé à S ; C3 limité au dossier v3 et copie du sommet
# du dépôt distant égale au lanceur exécuté ; preuve du banc v2 limitée aux trois scripts éprouvés, module commun comparé
# à sa copie de S ; dossier de traces purement numérique refusé (forme du v1).
# Historique du v1 : déclinée du lanceur v2 du pilote
# (docs/procedures/pilote-T0.5-v1/lancer_pilote_v2.sh, 19 cas du banc v1 et 9 du banc v2) : amorce
# `scripts/amorce_instance_t05_notations.sh` (une seule étude, pas d'ETUDE) ; PREREG et BRANCHE passés explicitement et
# relus dans le préenregistrement de S ; DEPOT_URL du dépôt de travail, écrit en dur ; relancement unique sur …-v2,
# explicite, seulement pour une cause d'infrastructure consignée (ligne R-… : « relancement », « notations »,
# « infrastructure », « instance NNNNNNNN » une fois, « dépense engagée X,XX USD » une fois), sans juge fini (relevé
# cumulatif de la surveillance du premier lancement passé en argument : aucune ligne « fin= » ni de dernier lot
# « lot=N/N » ; contrôles rejoués en mode
# relance sur la branche …-v1) et dans le plafond de GO-2026-10-12-02 (dépense engagée + 7,5 h × prix + 0,5 USD au plus
# 10,5 USD ; contre-lecture R2 de la chaîne) ; instances du programme arrêtées tolérées si
# relues arrêtées (55292763, 55458787 et celle du pilote, 55538944, gardée jusqu'au verdict complémentaire) ; instances
# d'autres projets de Lazar nommées en argument, tolérées si leur étiquette ne commence pas par « t05 » ; crédit exigé
# 7,5 h × (prix de l'offre + somme des prix des autres projets en marche) + 1,2 USD (devis de N-021 : arrêt certain par
# la surveillance à la création + 26 400 s, plus la marge du pilote ; critique adverse, constats 2 et 3) ; plafond de la
# surveillance écrit (création + 26 400 s, porté par surveiller_notations_v1.sh). Les treize scripts de la chaîne
# égaux à leurs copies versées à S : figés au commit des préalables, toute correction après S est un écart (nœud). En
# un seul appel, sous GO-2026-10-04-08 et la décision de Lazar
# sur N-021 (GO cité par S, relu dans le registre courant, sans ligne « révocation » qui le nomme ; colonne d'état de
# N-021 à la forme exacte « tranché (a) par Lazar : GO (R-…) »). Rien ne s'affiche des jetons. Aucune création si un
# contrôle échoue (contrôles avant dépense des notations, rejoués ici sur le même S, suite complète des tests comprise).
# Pendant l'appel, aucun sous-agent ne tourne.
# Codes : 0 création ; 3 heure, place, crédit, prix ou aucune offre conforme ; 4 tout échec à partir de la ligne
# « creation » de lancement.txt (création douteuse : vérifier les instances, forme filtrée, jamais --raw sans filtre) ;
# 2 tout autre arrêt avant.
# Usage : lancer_notations_v2.sh DOSSIER_TRACES AUTRES_PROJETS [relance R-NNN RELEVE_DU_PREMIER_LANCEMENT]
set -euo pipefail
trap 'echo "arrêt avant la création (ligne $LINENO)"; exit 2' ERR
{ [ $# -eq 2 ] || [ $# -eq 5 ]; } && [ -n "$1" ] && [ -n "$2" ] \
    || { echo "usage : lancer_notations_v2.sh DOSSIER_TRACES AUTRES_PROJETS [relance R-NNN RELEVE_DU_PREMIER_LANCEMENT]"; exit 2; }
T=$(realpath -m "$1"); AUTRES=$2; MODE_LANCEMENT=premier; CAUSE=""; RELEVE=""; OFFRE=""   # traces en chemin absolu
[[ "$(basename "$1")" =~ ^[0-9]+$ ]] && { echo "DOSSIER_TRACES purement numérique ($1) : forme du v1 (offre en argument), refusée"; exit 2; }
[[ "$AUTRES" = "-" || "$AUTRES" =~ ^[0-9]{6,10}(,[0-9]{6,10})*$ ]] \
    || { echo "AUTRES_PROJETS : identifiants d'instances séparés par des virgules, ou « - »"; exit 2; }
if [ $# -eq 5 ]; then
    [ "$3" = relance ] && [[ "$4" =~ ^R-[0-9]{3,4}$ ]] && [ -n "$5" ] || { echo "relance : « relance R-NNN RELEVE » attendu"; exit 2; }
    MODE_LANCEMENT=relance; CAUSE=$4; RELEVE=$(realpath -m "$5")
fi
PRIX_MAX=1.30                                    # devis de la phase 0 : 0,80 à 1,30 USD l'heure (Q-9)
HEURES_CREDIT=7.5                                # devis de N-021 : 26 400 s de surveillance, plus la marge du pilote
PLAFOND_GO=10.5                                  # GO-2026-10-12-02 : plafond de l'étape, relancement compris
PLAFOND_SURVEILLANCE_S=26400                     # surveiller_notations_v1.sh : création + 26 400 s
DEPOT=/home/user/controle-ia-travail
B=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
H=$B/notations-v1
V=$B/venv-vastai/bin/vastai
VERSEES=docs/procedures/notations-T0.5-v2
VERSEES3=docs/procedures/notations-T0.5-v3       # lanceur v2, son banc et le journal du banc (commit C3)
P=prereg/T0.5-pilote-notations-v1.md
A=scripts/amorce_instance_t05_notations.sh
if [ "$MODE_LANCEMENT" = premier ]; then BRANCHE=calcul/t05-notations-reel-v1; ETIQUETTE=t05-notations-v1
else BRANCHE=calcul/t05-notations-reel-v2; ETIQUETTE=t05-notations-v1-relance; fi
ARRETEES_TOLEREES="55292763 55458787 55538944"   # instances du programme arrêtées, gardées (disque) : tolérées si arrêtées
FILTRE="gpu_name=A100_SXM4 gpu_ram>=79 num_gpus=1 cuda_vers>=13.0 verified=true datacenter=true reliability>=0.99 cpu_ram>=128 disk_space>=80 rentable=true"
[ -e "$T" ] && { echo "$T existe déjà (R12)"; exit 2; }
# 0. heure (la suite des tests de l'instance ne doit pas chevaucher minuit UTC, test_garde_calcul ; T-7) et place disque
H0=$(date -u +%H%M); [ "$H0" -lt 2330 ] || { echo "heure UTC $H0 : pas de création entre 23:30 et 00:00 (T-7)"; exit 3; }
LIBRE=$(df -Pk "$B" | awk 'NR==2 {print $4}'); [ "$LIBRE" -ge 3000000 ] || { echo "place disque : $LIBRE ko libres (3 Go exigés)"; exit 3; }
LIBRE_T=$(df -Pk "$(dirname "$T")" | awk 'NR==2 {print $4}'); [ "$LIBRE_T" -ge 3000000 ] || { echo "place disque des traces : $LIBRE_T ko"; exit 3; }
mkdir -p "$T"
trap 'rm -rf "$T/clone-controles" "$T/clone-controles.travail"' EXIT        # le clone des contrôles ne reste jamais
printf 'heure de départ %s UTC ; place libre %s ko ; mode %s\n' "$(date -u +%H:%M:%S)" "$LIBRE" "$MODE_LANCEMENT" >> "$T/lancement.txt"
# 1. commit de scellement, poussé sur le dépôt de travail ; colonne d'état de N-021 à la forme exacte ; relance consignée
S=$(git -C "$DEPOT" log --diff-filter=A -1 --format=%H -- "$P.sha256")
[[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "commit de scellement introuvable"; exit 2; }
git -C "$DEPOT" fetch -q origin main
git -C "$DEPOT" merge-base --is-ancestor "$S" origin/main || { echo "commit de scellement $S absent du dépôt distant"; exit 2; }
PREMIERE=$(python3 - "$DEPOT/registres/decisions.md" "$MODE_LANCEMENT" "$CAUSE" <<'EOF'
import re, sys
lignes = open(sys.argv[1], encoding="utf-8").read().split("\n")
n21 = [x for x in lignes if x.startswith("| N-021 |")]
# forme exacte de la colonne d'état : aucun mot-clé cherché ; une révocation de la décision de Lazar est une ligne de
# type « révocation » de registres/go.md, relue plus bas (bloc GO21)
etat = n21[0].rsplit("|", 2)[-2].strip() if len(n21) == 1 else ""
if not re.fullmatch(r"tranché \(a\) par Lazar : GO-\d{4}-\d{2}-\d{2}-\d{2} \(R-\d{3,4}\)", etat):
    sys.exit("N-021")
if sys.argv[2] == "relance":
    r = [x for x in lignes if x.startswith(f"| {sys.argv[3]} |")]
    if len(r) != 1 or not all(m in r[0].lower() for m in ("relancement", "notations", "infrastructure")):
        sys.exit("relance non consignée")
    # l'instance du premier lancement, arrêtée et gardée, est nommée par la ligne de la cause
    inst = re.findall(r"\binstance (\d{8})\b", r[0])
    if len(set(inst)) != 1:
        sys.exit("relance : la ligne de la cause ne nomme pas, une seule fois, l'instance du premier lancement")
    # la dépense engagée par l'étape, écrite une seule fois (plafond de GO-2026-10-12-02, contrôlé après le prix)
    dep = re.findall(r"dépense engagée (\d+[,.]\d{2}) USD", r[0])
    if len(dep) != 1:
        sys.exit("relance : la ligne de la cause ne porte pas, une seule fois, « dépense engagée X,XX USD »")
    print(inst[0], dep[0].replace(",", "."))
EOF
) || { echo "registre des décisions : N-021 non tranchée par Lazar (forme exacte), ou relance non consignée"; exit 2; }
ENGAGEE=0
if [ -n "$PREMIERE" ]; then ENGAGEE=${PREMIERE#* }; PREMIERE=${PREMIERE%% *}; ARRETEES_TOLEREES="$ARRETEES_TOLEREES $PREMIERE"; fi
# relance : relevé cumulatif de la surveillance du premier lancement (préséance : aucun juge fini, établi sur les pièces)
if [ "$MODE_LANCEMENT" = relance ]; then
    # le relevé passé en argument doit être la copie versée et scellée dans le dépôt, à HEAD, sous le dossier de l'instance
    # du premier lancement (nommée par la ligne R-…), et porter la ligne « AMORCE … : commit » du commit de scellement
    # (vérification courte de la chaîne, constat 5)
    RV=traces/t05-notations-releve-$PREMIERE/releve-cumulatif.txt
    git -C "$DEPOT" show "HEAD:$RV" > "$T/releve-verse.txt" 2>/dev/null \
        || { echo "relevé du premier lancement non versé au dépôt ($RV) : relancement interdit"; exit 2; }
    [ "$(git -C "$DEPOT" show "HEAD:$RV.sha256" 2>/dev/null)" = "$(sha256sum "$T/releve-verse.txt" | cut -d' ' -f1)  releve-cumulatif.txt" ] \
        || { echo "relevé du premier lancement : sceau absent ou non conforme ($RV.sha256) : relancement interdit"; exit 2; }
    cmp -s "$T/releve-verse.txt" "$RELEVE" || { echo "relevé passé en argument ≠ copie versée ($RV) : relancement interdit"; exit 2; }
    python3 - "$RELEVE" "$S" <<'EOF' || { echo "relevé du premier lancement : relancement interdit (voir la ligne ci-dessus)"; exit 2; }
import re, sys
try:
    lignes = open(sys.argv[1], encoding="utf-8").read().split("\n")
except OSError:
    sys.exit("relevé du premier lancement illisible : aucun juge fini ne s'établit, cause indéterminée")
if not any(x.startswith("AMORCE ") and x.endswith(f" : commit {sys.argv[2]}") for x in lignes):
    sys.exit("relevé du premier lancement sans ligne « AMORCE … : commit » du commit de scellement : pas un relevé de ce lancement")
# fin d'un juge : ligne « fin= », ou ligne du dernier lot (lot=N/N : le fichier s'écrit juste après ; fin possible)
fins = [x for x in lignes if x.startswith("PROGRES ") and (" fin=" in x or re.search(r" lot=(\d+)/\1(?: |$)", x))]
if fins:
    sys.exit(f"un juge a fini, ou peut avoir fini, au premier lancement ({fins[0][:100]}) : préséance, aucun relancement")
print("relevé du premier lancement : aucune fin de juge")
EOF
fi
# 2. scripts égaux à leurs copies versées : le lanceur v2, exécuté par son propre chemin, à sa copie versée et scellée au
# commit C3 qui l'ajoute (descendant de S, ancêtre du dépôt distant) ; les douze autres scripts de la chaîne, dont la
# surveillance qui tournera des heures après S, à leurs copies versées à S
C3=$(git -C "$DEPOT" log --diff-filter=A -1 --format=%H origin/main -- "$VERSEES3/lancer_notations_v2.sh.sha256")
[[ "$C3" =~ ^[0-9a-f]{40}$ ]] || { echo "commit C3 du lanceur v2 introuvable sur le dépôt distant"; exit 2; }
git -C "$DEPOT" merge-base --is-ancestor "$S" "$C3" || { echo "commit C3 du lanceur v2 non descendant de S"; exit 2; }
for f in lancer_notations_v2.sh essais_lanceur_notations_v2.sh; do
    [ "$(git -C "$DEPOT" show "$C3:$VERSEES3/$f.sha256" 2>/dev/null)" = "$(git -C "$DEPOT" show "$C3:$VERSEES3/$f" 2>/dev/null | sha256sum | cut -d' ' -f1)  $f" ] \
        || { echo "$f : copie versée à C3 sans son sceau exact"; exit 2; }
done
[ "$(git -C "$DEPOT" show "$C3:$VERSEES3/lancer_notations_v2.sh" | sha256sum | cut -d' ' -f1)" = "$(sha256sum "$0" | cut -d' ' -f1)" ] \
    || { echo "lancer_notations_v2.sh exécuté ≠ copie versée au commit C3"; exit 2; }
# C3 n'ajoute que le dossier v3 ; la copie du sommet du dépôt distant est celle du lanceur exécuté (LV-15)
D3=$(git -C "$DEPOT" diff --no-renames --name-only "$C3^" "$C3")    # un échec de git diff rend 2 (piège d'erreur)
HORS_V3=$(printf '%s\n' "$D3" | grep -v "^$VERSEES3/" || true)
[ -z "$HORS_V3" ] || { echo "commit C3 : fichiers hors de $VERSEES3 ($(printf '%s ' $HORS_V3))"; exit 2; }
[ "$(git -C "$DEPOT" show "origin/main:$VERSEES3/lancer_notations_v2.sh" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$(sha256sum "$0" | cut -d' ' -f1)" ] \
    || { echo "lancer_notations_v2.sh exécuté ≠ copie au sommet du dépôt distant"; exit 2; }
# constantes du devis et du filtre : mêmes lignes que le lanceur v1 versé à S, que le préenregistrement relie aux
# contrôles (LV-03)
git -C "$DEPOT" show "$S:$VERSEES/lancer_notations_v1.sh" > "$T/lanceur-v1-S.sh" 2>/dev/null || { echo "lanceur v1 absent de S"; exit 2; }
for k in PRIX_MAX HEURES_CREDIT PLAFOND_GO PLAFOND_SURVEILLANCE_S FILTRE ARRETEES_TOLEREES; do
    a=$(grep -m1 "^$k=" "$0" || true); b=$(grep -m1 "^$k=" "$T/lanceur-v1-S.sh" || true)
    [ -n "$a" ] && [ "$a" = "$b" ] || { rm -f "$T/lanceur-v1-S.sh"; echo "constante $k du lanceur v2 ≠ celle du lanceur v1 versé à S"; exit 2; }
done
rm -f "$T/lanceur-v1-S.sh"
for paire in $(for s in construire_pilote_jouet_v1.py verifications_notations_v1.py \
        controles_avant_depense_notations_v1.sh sceller_notations_v1.sh surveiller_notations_v1.sh recuperation_notations_v1.sh \
        repetition_jouet_notations_v1.sh repetition_finale_notations_v1.sh essais_lanceur_notations_v1.sh \
        essais_controles_notations_v1.sh essais_scellement_notations_v1.sh essais_surveillance_notations_v1.sh; do echo "$s=$H/$s"; done); do
    [ "$(git -C "$DEPOT" show "$S:$VERSEES/${paire%%=*}" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$(sha256sum "${paire#*=}" | cut -d' ' -f1)" ] \
        || { echo "${paire%%=*} exécuté ≠ copie versée au commit S"; exit 2; }
done
# 2 bis. preuves des essais (R5 ; contre-lecture R2 de la chaîne, critique de complétude, constat 2) : journaux des bancs
# et de la répétition finale versés à S avec leur sceau exact, au verdict conforme ; chaque script éprouvé égal à sa copie
# versée à S (une garde corrigée après son banc ne part jamais au lancement sans avoir été éprouvée)
PREUVES=$(mktemp -d)
for j in banc-lanceur-notations-v1.log banc-surveillance-notations-v1.log banc-controles-notations-v1.log \
         banc-scellement-notations-v1.log repetition-finale-notations-v1.log; do
    git -C "$DEPOT" show "$S:$VERSEES/$j" > "$PREUVES/$j" 2>/dev/null || { rm -rf "$PREUVES"; echo "preuves des essais : journal $j absent de S"; exit 2; }
    [ "$(git -C "$DEPOT" show "$S:$VERSEES/$j.sha256" 2>/dev/null)" = "$(sha256sum "$PREUVES/$j" | cut -d' ' -f1)  $j" ] \
        || { rm -rf "$PREUVES"; echo "preuves des essais : sceau de $j absent ou non conforme à S"; exit 2; }
done
python3 -I "$H/verifications_notations_v1.py" preuves "$PREUVES" > "$PREUVES/sortie.txt" 2>&1 \
    || { m=$(tail -1 "$PREUVES/sortie.txt"); rm -rf "$PREUVES"; echo "preuves des essais : $m"; exit 2; }
while read -r s e; do
    [ "$(git -C "$DEPOT" show "$S:$VERSEES/$s" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$e" ] \
        || { rm -rf "$PREUVES"; echo "preuves des essais : $s éprouvé ($e) ≠ copie versée à S"; exit 2; }
done < "$PREUVES/sortie.txt"
echo "preuves des essais : cinq journaux conformes ; $(wc -l < "$PREUVES/sortie.txt") scripts éprouvés égaux à leurs copies versées à S"
# 2 ter. preuve du banc du lanceur v2, versée et scellée à C3 : dernière ligne au verdict conforme, aucune ligne d'échec,
# lanceur v2 et banc v2 éprouvés sous les empreintes de leurs copies versées à C3
J2=banc-lanceur-notations-v2.log
git -C "$DEPOT" show "$C3:$VERSEES3/$J2" > "$PREUVES/$J2" 2>/dev/null || { rm -rf "$PREUVES"; echo "preuves des essais : journal $J2 absent de C3"; exit 2; }
[ "$(git -C "$DEPOT" show "$C3:$VERSEES3/$J2.sha256" 2>/dev/null)" = "$(sha256sum "$PREUVES/$J2" | cut -d' ' -f1)  $J2" ] \
    || { rm -rf "$PREUVES"; echo "preuves des essais : sceau de $J2 absent ou non conforme à C3"; exit 2; }
python3 - "$PREUVES/$J2" "$(git -C "$DEPOT" show "$C3:$VERSEES3/lancer_notations_v2.sh" | sha256sum | cut -d' ' -f1)" \
    "$(git -C "$DEPOT" show "$C3:$VERSEES3/essais_lanceur_notations_v2.sh" | sha256sum | cut -d' ' -f1)" \
    "$(git -C "$DEPOT" show "$S:$VERSEES/verifications_notations_v1.py" | sha256sum | cut -d' ' -f1)" <<'EOF' \
    || { rm -rf "$PREUVES"; echo "preuves des essais : banc du lanceur v2 non conforme (voir la ligne ci-dessus)"; exit 2; }
import re, sys
lignes = open(sys.argv[1], encoding="utf-8").read().split("\n")
non_vides = [x for x in lignes if x.strip()]
if not non_vides or non_vides[-1] != "FIN DU BANC DU LANCEUR V2 DES NOTATIONS ; cas non conformes : 0":
    sys.exit("journal du banc v2 : dernière ligne non conforme")
fautes = [x for x in lignes if "NON CONFORME" in x or x.lstrip().startswith(("Traceback", "JETON AFFICHÉ"))]
if fautes:
    sys.exit(f"journal du banc v2 : ligne d'échec avant le verdict : {fautes[0].strip()[:90]}")
vus = {}
for x in lignes:
    if x.startswith("script éprouvé : "):
        m = re.fullmatch(r"script éprouvé : ([a-z_]+_v[12]\.(?:py|sh)) ([0-9a-f]{64})", x)
        if not m or vus.setdefault(m.group(1), m.group(2)) != m.group(2):
            sys.exit(f"journal du banc v2 : ligne « script éprouvé » mal formée ou en double : {x[:90]}")
attendus = {"lancer_notations_v2.sh": sys.argv[2], "essais_lanceur_notations_v2.sh": sys.argv[3],
            "verifications_notations_v1.py": sys.argv[4]}
if set(vus) != set(attendus):
    sys.exit(f"journal du banc v2 : scripts éprouvés {sorted(vus)} ≠ les trois attendus {sorted(attendus)}")
for s, e in attendus.items():
    if vus[s] != e:
        sys.exit(f"journal du banc v2 : {s} éprouvé sous {vus[s]} ≠ copie versée ({e})")
print("preuve du banc du lanceur v2 : conforme ; lanceur v2 et banc v2 éprouvés égaux à leurs copies versées à C3, "
      "module commun à sa copie versée à S")
EOF
rm -rf "$PREUVES"
# jetons présents (jamais affichés), avant les contrôles qui durent environ 40 minutes
[ -n "${HF_TOKEN:-}" ] && [ -n "${CONTROLE_IA_GITHUB_TOKEN:-}" ] || { echo "jeton absent (HF_TOKEN ou CONTROLE_IA_GITHUB_TOKEN) : pas de création"; exit 2; }
ARG_RELANCE=(); [ "$MODE_LANCEMENT" = relance ] && ARG_RELANCE=(relance)
if ! timeout 5400 bash "$H/controles_avant_depense_notations_v1.sh" "$S" "$T/clone-controles" "${ARG_RELANCE[@]}" > "$T/controles.txt" 2>&1; then
    grep '^KO' "$T/controles.txt" || tail -5 "$T/controles.txt"; echo "contrôles avant dépense en échec : pas de création"; exit 2
fi
tail -1 "$T/controles.txt" | grep -qx "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES" || { echo "contrôles : dernière ligne inattendue"; exit 2; }
rm -rf "$T/clone-controles" "$T/clone-controles.travail"
# 3. amorce du commit de scellement ; son empreinte doit être citée (fichier, pas de tube vers grep -q)
git -C "$DEPOT" show "$S:$P" > "$T/prereg-S.md"
git -C "$DEPOT" show "$S:$A" > "$T/amorce.sh"
E=$(sha256sum "$T/amorce.sh" | cut -d' ' -f1)
grep -qF "\`$A\` (\`$E\`, sha256)" "$T/prereg-S.md" || { echo "empreinte de l'amorce ($E) non citée par le préenregistrement"; exit 2; }
grep -qF "\`PREREG=$P\`, \`BRANCHE=$BRANCHE\`" "$T/prereg-S.md" || { echo "PREREG ou BRANCHE : le préenregistrement de S cite autre chose"; exit 2; }
# décision de Lazar sur N-021 citée par S, relue dans les registres courants : GO de type « revendication », accordé
# par Lazar, qui cite N-021 et l'option (a) ; ni lui ni le GO de calcul révoqués ; colonne d'état de N-021 à la forme
# exacte, qui cite ce GO et sa ligne R-… ; ligne R-… qui le consigne
# lue par le module commun (le même texte que le scellement et les contrôles ; vérification courte de la chaîne,
# constat 7 : la copie propre du lanceur avait dérivé)
GO21=$(python3 -I "$H/verifications_notations_v1.py" go "$T/prereg-S.md" "$DEPOT/registres/go.md" "$DEPOT/registres/decisions.md" 2>&1) \
    || { echo "décision de Lazar sur N-021 : $(printf '%s\n' "$GO21" | tail -1)"; exit 2; }
GO21=${GO21%% *}
[[ "$GO21" =~ ^GO-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}$ ]] || { echo "décision de Lazar sur N-021 : sortie du module illisible"; exit 2; }
B64=$(base64 -w0 < "$T/amorce.sh")
[ "$(printf %s "$B64" | base64 -d | sha256sum | cut -d' ' -f1)" = "$E" ] || { echo "encodage de l'amorce"; exit 2; }
# 4. jetons présents (jamais affichés) ; le jeton de l'instance est CONTROLE_IA_GITHUB_TOKEN
[ -n "${HF_TOKEN:-}" ] && [ -n "${CONTROLE_IA_GITHUB_TOKEN:-}" ] || { echo "jeton absent (HF_TOKEN ou CONTROLE_IA_GITHUB_TOKEN) : pas de création"; exit 2; }
# 5. offre (v2) : relue par le filtre du plan après les contrôles ; conformes : carte et processeur du pilote, au moins
# 80 Go (79 000 Mo, comme le filtre), une seule carte, prix fini, strictement positif, au plus PRIX_MAX ; en relancement,
# hors de la machine et de l'hôte de l'instance du premier lancement (relus en forme filtrée) ; la moins chère est prise
# (à prix égal, le plus petit identifiant), archivée avec sa machine et son hôte ; la liste des offres conformes relues
# s'écrit dans lancement.txt, un extrait de toutes les offres lues dans offres-relues.json ; aucune offre conforme : code
# 3, pas de création
EXCLUES=-
if [ "$MODE_LANCEMENT" = relance ]; then
    EXCLUES=$("$V" show instances --raw | python3 -c '
import json, sys
p = sys.argv[1]
try:
    inst = json.load(sys.stdin)
except Exception:
    sys.exit("instances : réponse illisible")
d = [i for i in inst if isinstance(i, dict) and str(i.get("id")) == p] if isinstance(inst, list) else []
if len(d) != 1:
    sys.exit(f"instance du premier lancement {p} absente de la liste")
m, h = d[0].get("machine_id"), d[0].get("host_id")
if not all(isinstance(x, int) and not isinstance(x, bool) for x in (m, h)):
    sys.exit("machine ou hôte du premier lancement illisible")
print(f"machine:{m} hote:{h}")' "$PREMIERE") \
        || { echo "relance : machine et hôte du premier lancement illisibles (forme filtrée) : pas de création"; exit 2; }
    echo "relance : offres de la machine ou de l'hôte du premier lancement écartées ($EXCLUES)" | tee -a "$T/lancement.txt"
fi
"$V" search offers "$FILTRE" -o 'dph_total' --storage 80 --raw > "$T/offres-brut.json"
c=0                                              # « … || c=$? » : ni set -e ni le piège ERR ne jouent sur l'affectation
CHOIX=$(python3 - "$T/offres-brut.json" "$T/offre.json" "$PRIX_MAX" "$T/lancement.txt" "$T/offres-relues.json" "$EXCLUES" <<'EOF'
import json, math, sys
brut, sortie, prix_max, journal, relues, exclusion = sys.argv[1], sys.argv[2], float(sys.argv[3]), sys.argv[4], sys.argv[5], sys.argv[6]
exclues = set() if exclusion == "-" else set(exclusion.split())
try:
    offres = json.load(open(brut))
except Exception:
    print("offres : réponse illisible", file=sys.stderr); sys.exit(2)
if not isinstance(offres, list):
    print("offres : liste attendue", file=sys.stderr); sys.exit(2)
extrait = ("id", "machine_id", "host_id", "gpu_name", "gpu_ram", "num_gpus", "cpu_name", "dph_total", "inet_down_cost",
           "end_date")
json.dump([{k: o.get(k) for k in extrait} if isinstance(o, dict) else {"illisible": type(o).__name__} for o in offres],
          open(relues, "w"), indent=1)
vus = [repr(o.get("id")) for o in offres if isinstance(o, dict)]
if len(vus) != len(set(vus)):
    print("offres : identifiant en double dans la réponse (ambiguë) : pas de création", file=sys.stderr); sys.exit(2)
def nombre(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)
def prix(o):
    p = o.get("dph_total")
    return float(p) if nombre(p) and p > 0 else None
def entier(v):
    return isinstance(v, int) and not isinstance(v, bool)
def exclue(o):
    if not exclues:
        return False
    m, h = o.get("machine_id"), o.get("host_id")
    if not (entier(m) and entier(h)):
        return True                  # en relancement, une offre sans machine ou hôte lisible ne prouve rien : écartée
    return f"machine:{m}" in exclues or f"hote:{h}" in exclues
conformes = [o for o in offres if isinstance(o, dict) and entier(o.get("id"))
             and o.get("gpu_name") == "A100 SXM4" and o.get("cpu_name") == "AMD EPYC 7513 32-Core Processor"
             and nombre(o.get("gpu_ram")) and o["gpu_ram"] >= 79000 and entier(o.get("num_gpus")) and o["num_gpus"] == 1
             and prix(o) is not None and prix(o) <= prix_max]
ecartees = [o for o in conformes if exclue(o)]
conformes = sorted((o for o in conformes if not exclue(o)), key=lambda o: (prix(o), o["id"]))
with open(journal, "a", encoding="utf-8") as j:
    j.write("offres conformes relues : " + (", ".join(
        f"{o['id']} ({prix(o):.4f} USD/h ; machine {o.get('machine_id')} ; hôte {o.get('host_id')} ; "
        f"téléchargement {o.get('inet_down_cost')} USD/Go ; fin {o.get('end_date')})" for o in conformes) or "aucune") + "\n")
    if exclues:
        j.write("offres conformes écartées (machine ou hôte du premier lancement, ou illisibles) : "
                + (", ".join(str(o["id"]) for o in ecartees) or "aucune") + "\n")
if not conformes:
    print(f"aucune offre conforme au filtre du plan au plus {prix_max} USD/h : pas de création", file=sys.stderr); sys.exit(3)
o = conformes[0]
champs = ("id", "machine_id", "host_id", "gpu_name", "gpu_ram", "num_gpus", "cuda_max_good", "driver_version", "cpu_name",
          "cpu_arch", "cpu_cores", "cpu_cores_effective", "cpu_ram", "disk_space",
          "reliability2", "verification", "hosting_type", "rentable", "end_date", "dph_total", "storage_total_cost",
          "inet_down_cost", "inet_up_cost", "geolocation")
json.dump({k: o.get(k) for k in champs}, open(sortie, "w"), indent=1)
print(o["id"], prix(o))
EOF
) || c=$?
[ -s "$T/offres-relues.json" ] || head -c 2000 "$T/offres-brut.json" > "$T/offres-relues-brut.txt"
rm -f "$T/offres-brut.json"
[ "$c" = 3 ] && exit 3
[ "$c" = 0 ] || { echo "offres : relecture impossible (code $c)"; exit 2; }
OFFRE=${CHOIX%% *}; DPH=${CHOIX#* }
[[ "$OFFRE" =~ ^[0-9]+$ ]] || { echo "offre choisie illisible"; exit 2; }
echo "offre choisie : $OFFRE ($DPH USD/h), la moins chère des offres conformes" | tee -a "$T/lancement.txt"
python3 -c "import sys; sys.exit(0 if float('$DPH') <= $PRIX_MAX else 1)" \
    || { echo "prix $DPH USD/h au-dessus du devis ($PRIX_MAX) : nœud, pas de création"; exit 3; }
# plafond de l'étape (GO-2026-10-12-02, relancement compris) : dépense engagée + heures × prix + 0,5 USD au plus 10,5 USD
python3 -c "import sys; t = round(float('$ENGAGEE') + $HEURES_CREDIT * float('$DPH') + 0.5, 2); print(f'plafond de l étape : dépense engagée {float(\"$ENGAGEE\"):.2f} + $HEURES_CREDIT h × {float(\"$DPH\"):.4f} + 0,50 = {t:.2f} USD (au plus $PLAFOND_GO)'); sys.exit(0 if t <= $PLAFOND_GO else 1)" \
    | tee -a "$T/lancement.txt" || { echo "relancement hors du plafond de GO-2026-10-12-02 : nœud, pas de création"; exit 3; }
# dépense du premier lancement au-delà de laquelle un relancement à ce prix sortirait du plafond (contre-lecture R2 de la
# chaîne, critique de complétude, constat 3) : 10,5 − 0,5 − 7,5 h × prix
python3 -c "print(f'dépense maximale d un premier lancement qui permettrait encore un relancement à ce prix : {$PLAFOND_GO - 0.5 - $HEURES_CREDIT * float(\"$DPH\"):.2f} USD')" \
    | tee -a "$T/lancement.txt"
# instances : aucune, hors les instances du programme arrêtées tolérées (relues arrêtées) et les instances d'autres
# projets nommées en argument, dont l'étiquette ne commence pas par « t05 » ; seuls identifiants, états, étiquettes et
# prix s'affichent ; la somme des prix de celles qui sont en marche entre dans le crédit exigé
SOMME_AUTRES=$("$V" show instances --raw | python3 -c '
import json, sys
tol = set(sys.argv[1].split())
decl = set() if sys.argv[2] == "-" else set(sys.argv[2].split(","))
journal = open(sys.argv[3], "a", encoding="utf-8")
try:
    instances = json.load(sys.stdin)
except Exception:
    print("vastai show instances : réponse illisible ou commande en échec", file=sys.stderr); sys.exit(3)
vues, autres_vues, refusees, somme = [], [], [], 0.0
for i in instances:
    ident, etat, cur = str(i.get("id")), i.get("actual_status"), i.get("cur_state")
    etiquette = str(i.get("label") or "")
    arretee = etat in ("exited", "stopped") and cur == "stopped"
    if ident in tol and arretee:
        vues.append(f"{ident} ({etat}, {cur})")
    elif ident in decl and not etiquette.startswith("t05"):
        dph = i.get("dph_total")
        if isinstance(dph, bool) or not isinstance(dph, (int, float)):
            refusees.append(f"{ident} (prix illisible)")
            continue
        if not arretee:
            somme += float(dph)
        statut = "arrêtée" if arretee else "en marche, comptée"
        autres_vues.append(f"{ident} ({etat}, {cur}, {float(dph):.3f} USD/h, {statut})")
    else:
        refusees.append(f"{ident} ({etat}, {cur})")
lignes = ["instances arrêtées tolérées : " + (", ".join(vues) or "aucune"),
          "instances d\u0027autres projets tolérées : " + (", ".join(autres_vues) or "aucune")]
if refusees:
    lignes.append("autres instances sur le compte : " + ", ".join(refusees))
for ligne in lignes:
    print(ligne, file=sys.stderr)
    journal.write(ligne + "\n")
journal.close()
if refusees:
    sys.exit(1)
print(f"{somme:.4f}")' "$ARRETEES_TOLEREES" "$AUTRES" "$T/lancement.txt") \
    || { echo "instances : non tolérée(s), ou liste illisible (voir la ligne ci-dessus) : pas de création"; exit 2; }
CREDIT=$("$V" show user --raw | python3 -c 'import json, sys; print(json.load(sys.stdin)["credit"])')
python3 -c "import sys; m = round($HEURES_CREDIT * (float('$DPH') + float('$SOMME_AUTRES')) + 1.2, 2); print(f'prix {float(\"$DPH\"):.4f} USD/h ; autres projets en marche {float(\"$SOMME_AUTRES\"):.4f} USD/h ; crédit {float(\"$CREDIT\"):.2f} USD ; minimum {m:.2f} USD ($HEURES_CREDIT h)'); sys.exit(0 if round(float('$CREDIT'), 2) >= m else 1)" \
    | tee -a "$T/lancement.txt" || { echo "crédit insuffisant pour les notations et les autres projets en marche : pas de lancement ; recharge demandée à Lazar"; exit 3; }
# 6. garde de calcul rejouée sur la commande (elle lit, dans cette session, un autre registre : R-160)
printf '{"tool_input":{"command":"GO_ID=GO-2026-10-04-08 vastai create instance %s --raw --image python:3.11-bookworm --disk 80"}}' "$OFFRE" \
    | python3 "$DEPOT/.claude/hooks/garde_calcul.py"
# 7. création : heure relue juste avant ; à partir d'ici, tout échec rend 4
H1=$(date -u +%H%M); [ "$H1" -lt 2330 ] || { echo "heure UTC $H1 : pas de création entre 23:30 et 00:00 (T-7)"; exit 3; }
trap - ERR
set +e
CREATION=$(date -u +%s)
export T_LANCEMENT="$T"
printf 'lanceur notations v2 %s ; autres projets %s\ncommit %s\noffre %s\nprereg %s\nbranche %s\netiquette %s\ngo N-021 %s\ncreation %s\nplafond de la surveillance %s (création + %s s ; surveiller_notations_v1.sh <id> %s <dossier neuf>)\n' \
    "$(sha256sum "$0" | cut -d' ' -f1)" "$AUTRES" "$S" "$OFFRE" "$P" "$BRANCHE" "$ETIQUETTE" "$GO21" "$CREATION" \
    "$((CREATION + PLAFOND_SURVEILLANCE_S))" "$PLAFOND_SURVEILLANCE_S" "$CREATION" >> "$T/lancement.txt"
GO_ID=GO-2026-10-04-08 "$V" create instance "$OFFRE" --raw --image python:3.11-bookworm --disk 80 --cancel-unavail \
    --label "$ETIQUETTE" \
    --env "-e COMMIT=$S -e PREREG=$P -e BRANCHE=$BRANCHE -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" \
    --entrypoint bash --args -c "echo $B64 | base64 -d > /root/amorce.sh && bash /root/amorce.sh" 2>&1 | python3 -c '
import json, os, sys
t = sys.stdin.read()
for k in ("HF_TOKEN", "CONTROLE_IA_GITHUB_TOKEN", "GH_TOKEN", "VAST_API_KEY"):
    v = os.environ.get(k)
    if v and len(v) > 6:
        t = t.replace(v, "***")
try:
    d = json.loads(t)
except Exception:
    open(os.environ["T_LANCEMENT"] + "/reponse-masquee.txt", "w").write(t[:300])
    print("réponse illisible (300 premiers caractères masqués dans reponse-masquee.txt) ; vérifier par « vastai show instances », sans --raw")
    sys.exit(4)
ok = d.get("success") is True and isinstance(d.get("new_contract"), int)
print("succès :", d.get("success"), "; identifiant", d.get("new_contract"), "; message :", str(d.get("msg", ""))[:200])
sys.exit(0 if ok else 4)' | tee -a "$T/lancement.txt"
st=("${PIPESTATUS[@]}")
[ "${st[0]}" = 0 ] && [ "${st[1]}" = 0 ] && [ "${st[2]}" = 0 ] || { echo "création douteuse (statuts ${st[*]}) : vérifier « vastai show instances », sans --raw"; exit 4; }
exit 0
