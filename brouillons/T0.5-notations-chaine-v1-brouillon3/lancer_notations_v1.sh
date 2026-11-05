#!/usr/bin/env bash
# Création de l'instance des notations décisives refaites du pilote de T0.5 (N-021, option (a), GO-2026-10-12-02 ;
# préenregistrement prereg/T0.5-pilote-notations-v1.md), v1, déclinée du lanceur v2 du pilote
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
# surveillance écrit (création + 26 400 s, porté par surveiller_notations_v1.sh). Contrôles, module commun et lanceur
# égaux à leurs copies versées à S : figés au commit des préalables, toute correction après S est un écart (nœud). En
# un seul appel, sous GO-2026-10-04-08 et la décision de Lazar
# sur N-021 (GO cité par S, relu dans le registre courant, sans ligne « révocation » qui le nomme ; colonne d'état de
# N-021 à la forme exacte « tranché (a) par Lazar : GO (R-…) »). Rien ne s'affiche des jetons. Aucune création si un
# contrôle échoue (contrôles avant dépense des notations, rejoués ici sur le même S, suite complète des tests comprise).
# Pendant l'appel, aucun sous-agent ne tourne.
# Codes : 0 création ; 3 heure, place, crédit ou prix ; 4 tout échec à partir de la ligne « creation » de lancement.txt
# (création douteuse : vérifier les instances, forme filtrée, jamais --raw sans filtre) ; 2 tout autre arrêt avant.
# Usage : lancer_notations_v1.sh OFFRE DOSSIER_TRACES AUTRES_PROJETS [relance R-NNN RELEVE_DU_PREMIER_LANCEMENT]
set -euo pipefail
trap 'echo "arrêt avant la création (ligne $LINENO)"; exit 2' ERR
{ [ $# -eq 3 ] || [ $# -eq 6 ]; } && [ -n "$1" ] && [ -n "$2" ] && [ -n "$3" ] \
    || { echo "usage : lancer_notations_v1.sh OFFRE DOSSIER_TRACES AUTRES_PROJETS [relance R-NNN RELEVE_DU_PREMIER_LANCEMENT]"; exit 2; }
OFFRE=$1; T=$(realpath -m "$2"); AUTRES=$3; MODE_LANCEMENT=premier; CAUSE=""; RELEVE=""   # traces en chemin absolu
[[ "$AUTRES" = "-" || "$AUTRES" =~ ^[0-9]{6,10}(,[0-9]{6,10})*$ ]] \
    || { echo "AUTRES_PROJETS : identifiants d'instances séparés par des virgules, ou « - »"; exit 2; }
if [ $# -eq 6 ]; then
    [ "$4" = relance ] && [[ "$5" =~ ^R-[0-9]{3,4}$ ]] && [ -n "$6" ] || { echo "relance : « relance R-NNN RELEVE » attendu"; exit 2; }
    MODE_LANCEMENT=relance; CAUSE=$5; RELEVE=$(realpath -m "$6")
fi
PRIX_MAX=1.30                                    # devis de la phase 0 : 0,80 à 1,30 USD l'heure (Q-9)
HEURES_CREDIT=7.5                                # devis de N-021 : 26 400 s de surveillance, plus la marge du pilote
PLAFOND_GO=10.5                                  # GO-2026-10-12-02 : plafond de l'étape, relancement compris
PLAFOND_SURVEILLANCE_S=26400                     # surveiller_notations_v1.sh : création + 26 400 s
DEPOT=/home/user/controle-ia-travail
B=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
H=$B/notations-v1
V=$B/venv-vastai/bin/vastai
VERSEES=docs/procedures/notations-T0.5-v1
P=prereg/T0.5-pilote-notations-v1.md
A=scripts/amorce_instance_t05_notations.sh
if [ "$MODE_LANCEMENT" = premier ]; then BRANCHE=calcul/t05-notations-reel-v1; ETIQUETTE=t05-notations-v1
else BRANCHE=calcul/t05-notations-reel-v2; ETIQUETTE=t05-notations-v1-relance; fi
ARRETEES_TOLEREES="55292763 55458787 55538944"   # instances du programme arrêtées, gardées (disque) : tolérées si arrêtées
FILTRE="gpu_name=A100_SXM4 gpu_ram>=79 num_gpus=1 cuda_vers>=13.0 verified=true datacenter=true reliability>=0.99 cpu_ram>=128 disk_space>=80 rentable=true"
[[ "$OFFRE" =~ ^[0-9]+$ ]] || { echo "offre invalide"; exit 2; }
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
    python3 - "$RELEVE" <<'EOF' || { echo "relevé du premier lancement : relancement interdit (voir la ligne ci-dessus)"; exit 2; }
import re, sys
try:
    lignes = open(sys.argv[1], encoding="utf-8").read().split("\n")
except OSError:
    sys.exit("relevé du premier lancement illisible : aucun juge fini ne s'établit, cause indéterminée")
if not any(re.match(r"^AMORCE \d{4}-\d{2}-\d{2}T[^ ]* : commit [0-9a-f]{40}$", x) for x in lignes):
    sys.exit("relevé du premier lancement sans ligne « AMORCE … : commit » : ce n'est pas un relevé de la surveillance")
# fin d'un juge : ligne « fin= », ou ligne du dernier lot (lot=N/N : le fichier s'écrit juste après ; fin possible)
fins = [x for x in lignes if x.startswith("PROGRES ") and (" fin=" in x or re.search(r" lot=(\d+)/\1(?: |$)", x))]
if fins:
    sys.exit(f"un juge a fini, ou peut avoir fini, au premier lancement ({fins[0][:100]}) : préséance, aucun relancement")
print("relevé du premier lancement : aucune fin de juge")
EOF
fi
# 2. scripts exécutés égaux à leurs copies versées à S (contrôles, lanceur)
for paire in "controles_avant_depense_notations_v1.sh=$H/controles_avant_depense_notations_v1.sh" \
             "verifications_notations_v1.py=$H/verifications_notations_v1.py" "lancer_notations_v1.sh=$0"; do
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
GO21=$(python3 - "$T/prereg-S.md" "$DEPOT/registres/go.md" "$DEPOT/registres/decisions.md" <<'PYGO'
import re, sys
texte, go_md, dec_md = (open(f, encoding="utf-8").read() for f in sys.argv[1:4])
m = re.findall(r"^- Décision de Lazar sur N-021 : `(GO-\d{4}-\d{2}-\d{2}-\d{2})` \((R-\d{3,4})\)", texte, re.M)
if len(m) != 1:
    sys.exit("GO de Lazar sur N-021 introuvable dans le préenregistrement de S")
go = m[0][0]
lignes = go_md.split("\n")
c = [[x.strip() for x in l.strip().strip("|").split("|")] for l in lignes if l.startswith(f"| {go} |")]
if len(c) != 1 or len(c[0]) != 8 or c[0][2] != "revendication" or c[0][6] != "Lazar" or "N-021" not in c[0][3] \
        or "(a)" not in c[0][3]:
    sys.exit(f"{go} : absent du registre courant, ou d'un autre type, ou non accordé par Lazar, ou sans N-021 et l'option (a)")
for g in (go, "GO-2026-10-04-08"):
    if [l for l in lignes if l.startswith("| GO-") and (lambda c: (len(c) == 8 and c[2].lower() == "révocation" and (g in c[3] or g in c[7])) or (len(c) != 8 and "révocation" in l.lower() and g in l))([x.strip() for x in l.strip().strip("|").split("|")])]:
        sys.exit(f"{g} révoqué dans le registre courant")
reg = m[0][1]
dec = dec_md.split("\n")
n21 = [l for l in dec if l.startswith("| N-021 |")]
etat = n21[0].rsplit("|", 2)[-2].strip() if len(n21) == 1 else ""
if not re.fullmatch(rf"tranché \(a\) par Lazar : {re.escape(go)} \({re.escape(reg)}\)", etat):
    sys.exit(f"N-021 : la colonne d'état courante n'est pas « tranché (a) par Lazar : {go} ({reg}) »")
r = [l for l in dec if l.startswith(f"| {reg} |")]
if len(r) != 1 or go not in r[0]:
    sys.exit(f"{reg} : absent du registre courant, en double, ou sans {go}")
print(go)
PYGO
) || { echo "décision de Lazar sur N-021 : ${GO21:-contrôle en échec}"; exit 2; }
B64=$(base64 -w0 < "$T/amorce.sh")
[ "$(printf %s "$B64" | base64 -d | sha256sum | cut -d' ' -f1)" = "$E" ] || { echo "encodage de l'amorce"; exit 2; }
# 4. jetons présents (jamais affichés) ; le jeton de l'instance est CONTROLE_IA_GITHUB_TOKEN
[ -n "${HF_TOKEN:-}" ] && [ -n "${CONTROLE_IA_GITHUB_TOKEN:-}" ] || { echo "jeton absent (HF_TOKEN ou CONTROLE_IA_GITHUB_TOKEN) : pas de création"; exit 2; }
# 5. offre : relue par le filtre du plan, carte et processeur du pilote exigés, archivée avec le processeur
"$V" search offers "$FILTRE" -o 'dph_total' --storage 80 --raw > "$T/offres-brut.json"
DPH=$(python3 - "$OFFRE" "$T/offres-brut.json" "$T/offre.json" <<'EOF'
import json, sys
offre, brut, sortie = int(sys.argv[1]), sys.argv[2], sys.argv[3]
d = [o for o in json.load(open(brut)) if o.get("id") == offre]
if len(d) != 1:
    sys.exit(f"offre {offre} absente des offres conformes au filtre du plan")
champs = ("id", "gpu_name", "gpu_ram", "num_gpus", "cuda_max_good", "driver_version", "cpu_name", "cpu_arch",
          "cpu_cores", "cpu_cores_effective", "cpu_ram", "disk_space",
          "reliability2", "verification", "hosting_type", "rentable", "end_date", "dph_total", "storage_total_cost",
          "inet_down_cost", "inet_up_cost", "geolocation")
json.dump({k: d[0].get(k) for k in champs}, open(sortie, "w"), indent=1)
if not isinstance(d[0].get("dph_total"), (int, float)):
    sys.exit(f"offre {offre} sans prix lisible")
if d[0].get("gpu_name") != "A100 SXM4":
    sys.exit(f"offre {offre} : carte {d[0].get('gpu_name')!r} ; seule l'A100 SXM4 du pilote est admise")
if d[0].get("cpu_name") != "AMD EPYC 7513 32-Core Processor":
    sys.exit(f"offre {offre} : processeur {d[0].get('cpu_name')!r} ; seul celui du pilote (AMD EPYC 7513) est admis")
print(d[0]["dph_total"])
EOF
)
rm -f "$T/offres-brut.json"
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
printf 'lanceur notations v1 %s ; autres projets %s\ncommit %s\noffre %s\nprereg %s\nbranche %s\netiquette %s\ngo N-021 %s\ncreation %s\nplafond de la surveillance %s (création + %s s ; surveiller_notations_v1.sh <id> %s <dossier neuf>)\n' \
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
