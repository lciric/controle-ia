#!/usr/bin/env bash
# Brouillon 4 (R-227) : égal au brouillon 3, sauf le dossier des copies versées, docs/procedures/P3-premier-test-v2/ (R12 : le versement du dossier v1 n'est pas réécrit).
# Création de l'instance du premier test boîte blanche sur l'organisme (i-a) (P3, R-192, R-202 ; préenregistrement
# prereg/P3-premier-test-i-a-v1.md), v1, brouillon 3 (contre-lecture R2 de la chaîne traitée : CH-02, CH-04, CH-10, CH-11,
# CH-13, CH-14, CH-17, CH-22, CH-23 ; bornes du brouillon 4 du texte ; relecture courte traitée : stockage borné, RCh-04,
# RT-05 ; borne de téléchargement fixée), déclinée du lanceur v2 des notations refaites du
# pilote de T0.5 (docs/procedures/notations-T0.5-v3/lancer_notations_v2.sh, commit C3 `cbb1418`, 142 cas de banc, deux
# relectures) sous un nom nouveau (R12). Différences : aucun relancement (une relance, s'il en faut une, passe par un nœud
# de Lazar et un lanceur suivant, avec son banc) ; treize scripts de la chaîne de P3, le lanceur compris, égaux à leurs
# copies versées à S (docs/procedures/P3-premier-test-v2/), sans commit C3 ; preuves des essais : cinq journaux de la
# chaîne de P3 versés à S ; GO de calcul et décision de Lazar lus par le module commun verifications_p3_v1.py, qui
# n'accepte que GO-2026-10-04-08 (CH-02) ; le GO validé par le module est celui que portent la garde rejouée et la
# création ; accord de Lazar du jour pour l'appel payant, ligne R-… du registre des décisions nommée en argument et relue
# par le module commun avant et après les contrôles (R-185 ; CH-11) ; constantes de P3 : crédit exigé sur 6,5 heures,
# surveillance à la création + 22 200 s ; dépense de l'étape bornée à 22 200 s × PRIX_MAX (8,02 USD) + un arrêt en dix
# minutes (0,22 USD) + le téléchargement (au plus TELECHARGEMENT_MAX par Go) + le disque de l'instance arrêtée, gardée
# 72 heures au plus (texte, Plan d'analyse, points 1.6 et 4 ; CH-10). Repris du v2 : après les contrôles avant dépense
# (rejoués ici sur le même S, suite complète des tests comprise), le lanceur relit les offres au filtre du plan et prend
# la moins chère des offres conformes (A100 SXM4 80 Go sur AMD EPYC 7513, une carte, prix fini et strictement positif au
# plus PRIX_MAX ; en plus, CH-04 et CH-10 : au moins COEURS_MIN cœurs effectifs, au moins MEMOIRE_VIVE_MIN_MO Mo de
# mémoire vive, téléchargement fini, positif ou nul, au plus TELECHARGEMENT_MAX USD par Go ; stockage fini, positif ou
# nul, au plus STOCKAGE_MAX USD de l'heure (relecture courte, RCh-04, RT-05) ; à prix égal, le plus petit
# identifiant ; identifiants distincts) ; machine et hôte archivés ; offres relues gardées ; instances du programme
# arrêtées tolérées si relues arrêtées (56438435, notations refaites, ajoutée : CH-17) ; instances d'autres projets de
# Lazar nommées en argument, tolérées seulement si leur étiquette commence par « rr- » (liste positive, CH-13) ; crédit
# exigé 6,5 h × (prix de l'offre + somme des prix des autres projets en marche) + 1,2 USD, calculé dans un programme qui
# relit la réponse et en vérifie la forme (aucune valeur relue n'est insérée dans du code, CH-22) ; plafond de la
# surveillance et commande du contrôle à cinq minutes écrits (CH-23). Rien ne s'affiche des jetons. Aucune création si un
# contrôle échoue. Pendant l'appel, aucun sous-agent ne tourne.
# Codes : 0 création ; 3 heure, place, crédit, prix ou aucune offre conforme ; 4 tout échec à partir de la ligne
# « creation » de lancement.txt (création douteuse : vérifier les instances, forme filtrée, jamais --raw sans filtre) ;
# 2 tout autre arrêt avant.
# Usage : lancer_p3_v1.sh DOSSIER_TRACES AUTRES_PROJETS ACCORD
#   AUTRES_PROJETS : identifiants d'instances d'autres projets de Lazar séparés par des virgules, ou « - » ;
#   ACCORD : identifiant de la ligne R-… du registre des décisions qui consigne l'accord de Lazar du jour (R-185).
set -euo pipefail
trap 'echo "arrêt avant la création (ligne $LINENO)"; exit 2' ERR
[ $# -eq 3 ] && [ -n "$1" ] && [ -n "$2" ] && [ -n "$3" ] || { echo "usage : lancer_p3_v1.sh DOSSIER_TRACES AUTRES_PROJETS ACCORD"; exit 2; }
T=$(realpath -m "$1"); AUTRES=$2; ACCORD=$3; OFFRE=""                    # traces en chemin absolu
[[ "$(basename "$1")" =~ ^[0-9]+$ ]] && { echo "DOSSIER_TRACES purement numérique ($1) : refusé (une offre n'est jamais passée en argument)"; exit 2; }
[[ "$AUTRES" = "-" || "$AUTRES" =~ ^[0-9]{6,10}(,[0-9]{6,10})*$ ]] \
    || { echo "AUTRES_PROJETS : identifiants d'instances séparés par des virgules, ou « - »"; exit 2; }
[[ "$ACCORD" =~ ^R-[0-9]{3,4}$ ]] || { echo "ACCORD : identifiant R-… de la ligne qui consigne l'accord de Lazar du jour attendu (R-185)"; exit 2; }
PRIX_MAX=1.30                                    # devis de la phase 0 : 0,80 à 1,30 USD l'heure (Q-9)
HEURES_CREDIT=6.5                                # préenregistrement de P3 : 22 200 s de surveillance et dix minutes d'arrêt, arrondies
PLAFOND_SURVEILLANCE_S=22200                     # surveiller_p3_v1.sh : création + 22 200 s
COEURS_MIN=16                                    # cœurs effectifs de l'offre, cpu_cores_effective (texte, Calcul et bornes ; CH-04)
MEMOIRE_VIVE_MIN_MO=128000                       # mémoire vive de l'offre, cpu_ram en Mo (texte, Calcul et bornes ; CH-04)
TELECHARGEMENT_MAX=0.05                          # téléchargement de l'offre, inet_down_cost en USD par Go : borne citée par le texte (CH-10, R-215)
STOCKAGE_MAX=0.03                                # stockage de l'offre, storage_total_cost en USD de l'heure : borne citée par le texte (RCh-04, RT-05)
PREFIXE_AUTRES=rr-                               # étiquette des instances de l'autre projet de Lazar (liste positive ; CH-13)
DEPOT=/home/user/controle-ia-travail
B=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
H=$B/p3-v1
V=$B/venv-vastai/bin/vastai
VERSEES=docs/procedures/P3-premier-test-v2
P=prereg/P3-premier-test-i-a-v1.md
A=scripts/amorce_instance_p3.sh
BRANCHE=calcul/p3-reel-v1; ETIQUETTE=p3-v1
ARRETEES_TOLEREES="55292763 55458787 55538944 56438435"   # instances du programme arrêtées, gardées (disque) : tolérées si arrêtées (56438435 : notations refaites, arrêtée le 2026-10-18, CH-17)
FILTRE="gpu_name=A100_SXM4 gpu_ram>=79 num_gpus=1 cuda_vers>=13.0 verified=true datacenter=true reliability>=0.99 cpu_ram>=128 disk_space>=80 rentable=true"
[[ "$ARRETEES_TOLEREES" =~ ^[0-9]{6,10}( [0-9]{6,10})*$ ]] || { echo "instances tolérées non épinglées"; exit 2; }
[[ "$TELECHARGEMENT_MAX" =~ ^0\.[0-9]{2,4}$ ]] || { echo "borne de téléchargement non fixée ($TELECHARGEMENT_MAX) : à reprendre du texte scellé"; exit 2; }
[[ "$STOCKAGE_MAX" =~ ^0\.[0-9]{2,4}$ ]] || { echo "borne de stockage non fixée ($STOCKAGE_MAX) : à reprendre du texte scellé"; exit 2; }
[ -e "$T" ] && { echo "$T existe déjà (R12)"; exit 2; }
# 0. heure (la suite des tests de l'instance ne doit pas chevaucher minuit UTC, test_garde_calcul ; T-7) et place disque
H0=$(date -u +%H%M); [ "$H0" -lt 2330 ] || { echo "heure UTC $H0 : pas de création entre 23:30 et 00:00 (T-7)"; exit 3; }
LIBRE=$(df -Pk "$B" | awk 'NR==2 {print $4}'); [ "$LIBRE" -ge 3000000 ] || { echo "place disque : $LIBRE ko libres (3 Go exigés)"; exit 3; }
LIBRE_T=$(df -Pk "$(dirname "$T")" | awk 'NR==2 {print $4}'); [ "$LIBRE_T" -ge 3000000 ] || { echo "place disque des traces : $LIBRE_T ko"; exit 3; }
mkdir -p "$T"
trap 'rm -rf "$T/clone-controles" "$T/clone-controles.travail"' EXIT        # le clone des contrôles ne reste jamais
printf 'heure de départ %s UTC ; place libre %s ko\n' "$(date -u +%H:%M:%S)" "$LIBRE" >> "$T/lancement.txt"
# 1. commit de scellement, poussé sur le dépôt de travail
S=$(git -C "$DEPOT" log --diff-filter=A -1 --format=%H -- "$P.sha256")
[[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "commit de scellement introuvable"; exit 2; }
git -C "$DEPOT" fetch -q origin main
git -C "$DEPOT" merge-base --is-ancestor "$S" origin/main || { echo "commit de scellement $S absent du dépôt distant"; exit 2; }
# 2. scripts égaux à leurs copies versées à S : les treize scripts de la chaîne de P3 (liste CHAINE du scellement), dont
# la surveillance et le contrôle à cinq minutes, qui tourneront après S ; le lanceur exécuté par son propre chemin
for paire in "lancer_p3_v1.sh=$0" $(for s in verifications_p3_v1.py controles_avant_depense_p3_v1.sh sceller_p3_v1.sh \
        surveiller_p3_v1.sh controle_cinq_minutes_p3_v1.sh recuperation_p3_v1.sh repetition_jouet_p3_v1.sh \
        repetition_finale_p3_v1.sh essais_lanceur_p3_v1.sh essais_controles_p3_v1.sh essais_scellement_p3_v1.sh \
        essais_surveillance_p3_v1.sh; do echo "$s=$H/$s"; done); do
    [ "$(git -C "$DEPOT" show "$S:$VERSEES/${paire%%=*}" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$(sha256sum "${paire#*=}" | cut -d' ' -f1)" ] \
        || { echo "${paire%%=*} exécuté ≠ copie versée au commit S"; exit 2; }
done
# 2 bis. preuves des essais (R5) : journaux des bancs et de la répétition finale versés à S avec leur sceau exact, au
# verdict conforme ; chaque script éprouvé égal à sa copie versée à S (une garde corrigée après son banc ne part jamais
# au lancement sans avoir été éprouvée)
PREUVES=$(mktemp -d)
for j in banc-lanceur-p3-v1.log banc-surveillance-p3-v1.log banc-controles-p3-v1.log \
         banc-scellement-p3-v1.log repetition-finale-p3-v1.log; do
    git -C "$DEPOT" show "$S:$VERSEES/$j" > "$PREUVES/$j" 2>/dev/null || { rm -rf "$PREUVES"; echo "preuves des essais : journal $j absent de S"; exit 2; }
    [ "$(git -C "$DEPOT" show "$S:$VERSEES/$j.sha256" 2>/dev/null)" = "$(sha256sum "$PREUVES/$j" | cut -d' ' -f1)  $j" ] \
        || { rm -rf "$PREUVES"; echo "preuves des essais : sceau de $j absent ou non conforme à S"; exit 2; }
done
python3 -I "$H/verifications_p3_v1.py" preuves "$PREUVES" > "$PREUVES/sortie.txt" 2>&1 \
    || { m=$(tail -1 "$PREUVES/sortie.txt"); rm -rf "$PREUVES"; echo "preuves des essais : $m"; exit 2; }
while read -r s e; do
    [ "$(git -C "$DEPOT" show "$S:$VERSEES/$s" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$e" ] \
        || { rm -rf "$PREUVES"; echo "preuves des essais : $s éprouvé ($e) ≠ copie versée à S"; exit 2; }
done < "$PREUVES/sortie.txt"
echo "preuves des essais : cinq journaux conformes ; $(wc -l < "$PREUVES/sortie.txt") scripts éprouvés égaux à leurs copies versées à S"
rm -rf "$PREUVES"
# accord de Lazar du jour (R-185 ; CH-11), relu dans le registre courant des décisions par le module commun : avant les
# contrôles (environ 40 minutes) et de nouveau après, au jour de la création
accord() {
    local j r
    j=$(date -u +%F)
    r=$(python3 -I "$H/verifications_p3_v1.py" accord "$ACCORD" "$DEPOT/registres/decisions.md" "$j" 2>&1) \
        || { echo "accord de Lazar : $(printf '%s\n' "$r" | tail -1) : pas de création"; return 1; }
    printf 'accord %s\n' "$r" >> "$T/lancement.txt"
    echo "accord de Lazar : $r"
}
accord || exit 2
# jetons présents (jamais affichés), avant les contrôles qui durent environ 40 minutes ; le jeton de l'instance est
# CONTROLE_IA_GITHUB_TOKEN (le second contrôle des jetons du brouillon 1, redondant, est retiré : CH-14)
[ -n "${HF_TOKEN:-}" ] && [ -n "${CONTROLE_IA_GITHUB_TOKEN:-}" ] || { echo "jeton absent (HF_TOKEN ou CONTROLE_IA_GITHUB_TOKEN) : pas de création"; exit 2; }
if ! timeout 5400 bash "$H/controles_avant_depense_p3_v1.sh" "$S" "$T/clone-controles" > "$T/controles.txt" 2>&1; then
    grep '^KO' "$T/controles.txt" || tail -5 "$T/controles.txt"; echo "contrôles avant dépense en échec : pas de création"; exit 2
fi
tail -1 "$T/controles.txt" | grep -qx "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES" || { echo "contrôles : dernière ligne inattendue"; exit 2; }
rm -rf "$T/clone-controles" "$T/clone-controles.travail"
# 3. amorce du commit de scellement ; son empreinte doit être citée (fichier, pas de tube vers grep -q ; texte aux
# espaces réduites, la citation peut passer à la ligne)
git -C "$DEPOT" show "$S:$P" > "$T/prereg-S.md"
git -C "$DEPOT" show "$S:$A" > "$T/amorce.sh"
E=$(sha256sum "$T/amorce.sh" | cut -d' ' -f1)
tr '\n' ' ' < "$T/prereg-S.md" | tr -s ' ' > "$T/prereg-S-plat.txt"
grep -qF "\`$A\` (\`$E\`, sha256)" "$T/prereg-S-plat.txt" || { echo "empreinte de l'amorce ($E) non citée par le préenregistrement"; exit 2; }
rm -f "$T/prereg-S-plat.txt"
grep -qF "\`PREREG=$P\`, \`BRANCHE=$BRANCHE\`" "$T/prereg-S.md" || { echo "PREREG ou BRANCHE : le préenregistrement de S cite autre chose"; exit 2; }
# GO de calcul et décision de Lazar cités par S, relus dans les registres courants par le module commun (le même texte
# que le scellement et les contrôles) : GO-2026-10-04-08 seulement, de type « calcul », accordé par Lazar, non révoqué ;
# ligne R-… de la décision, non révoquée ; le GO ainsi validé est celui de la garde rejouée et de la création (CH-02)
GOP3=$(python3 -I "$H/verifications_p3_v1.py" go "$T/prereg-S.md" "$DEPOT/registres/go.md" "$DEPOT/registres/decisions.md" 2>&1) \
    || { echo "GO de calcul et décision de Lazar : $(printf '%s\n' "$GOP3" | tail -1)"; exit 2; }
GOP3=${GOP3%% *}
# forme de la sortie du module : garde redondante (le module n'écrit que ce GO), sans artefact possible (CH-14)
[ "$GOP3" = "GO-2026-10-04-08" ] || { echo "GO de calcul et décision de Lazar : sortie du module illisible"; exit 2; }
accord || exit 2
B64=$(base64 -w0 < "$T/amorce.sh")
# aller-retour de l'encodage de l'amorce : garde redondante, sans artefact possible (CH-14)
[ "$(printf %s "$B64" | base64 -d | sha256sum | cut -d' ' -f1)" = "$E" ] || { echo "encodage de l'amorce"; exit 2; }
# 5. offre : relue par le filtre du plan après les contrôles ; conformes : carte et processeur du pilote, au moins 80 Go
# (79 000 Mo, comme le filtre), une seule carte, cœurs effectifs, mémoire vive, téléchargement et stockage aux bornes du
# texte (CH-04, CH-10, RCh-04), prix fini, strictement positif, au plus PRIX_MAX ; la moins chère est prise (à prix égal, le plus petit
# identifiant), archivée avec sa machine et son hôte ; la liste des offres conformes relues s'écrit dans lancement.txt,
# un extrait de toutes les offres lues dans offres-relues.json ; aucune offre conforme : code 3, pas de création ; un
# identifiant en double : code 2
EXCLUES=-                                        # aucun relancement dans ce lanceur : aucune offre écartée
"$V" search offers "$FILTRE" -o 'dph_total' --storage 80 --raw > "$T/offres-brut.json"
c=0                                              # « … || c=$? » : ni set -e ni le piège ERR ne jouent sur l'affectation
CHOIX=$(python3 - "$T/offres-brut.json" "$T/offre.json" "$PRIX_MAX" "$T/lancement.txt" "$T/offres-relues.json" "$EXCLUES" \
        "$COEURS_MIN" "$MEMOIRE_VIVE_MIN_MO" "$TELECHARGEMENT_MAX" "$STOCKAGE_MAX" <<'EOF'
import json, math, sys
brut, sortie, prix_max, journal, relues, exclusion = sys.argv[1], sys.argv[2], float(sys.argv[3]), sys.argv[4], sys.argv[5], sys.argv[6]
coeurs_min, ram_min, tel_max, sto_max = float(sys.argv[7]), float(sys.argv[8]), float(sys.argv[9]), float(sys.argv[10])
exclues = set() if exclusion == "-" else set(exclusion.split())
try:
    offres = json.load(open(brut))
except Exception:
    print("offres : réponse illisible", file=sys.stderr); sys.exit(2)
if not isinstance(offres, list):
    print("offres : liste attendue", file=sys.stderr); sys.exit(2)
extrait = ("id", "machine_id", "host_id", "gpu_name", "gpu_ram", "num_gpus", "cpu_name", "cpu_cores_effective", "cpu_ram",
           "dph_total", "inet_down_cost", "storage_total_cost", "end_date")
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
             and nombre(o.get("cpu_cores_effective")) and o["cpu_cores_effective"] >= coeurs_min
             and nombre(o.get("cpu_ram")) and o["cpu_ram"] >= ram_min
             and nombre(o.get("inet_down_cost")) and 0 <= o["inet_down_cost"] <= tel_max
             and nombre(o.get("storage_total_cost")) and 0 <= o["storage_total_cost"] <= sto_max
             and prix(o) is not None and prix(o) <= prix_max]
ecartees = [o for o in conformes if exclue(o)]
conformes = sorted((o for o in conformes if not exclue(o)), key=lambda o: (prix(o), o["id"]))
with open(journal, "a", encoding="utf-8") as j:
    j.write("offres conformes relues : " + (", ".join(
        f"{o['id']} ({prix(o):.4f} USD/h ; machine {o.get('machine_id')} ; hôte {o.get('host_id')} ; "
        f"cœurs effectifs {o.get('cpu_cores_effective')} ; mémoire vive {o.get('cpu_ram')} Mo ; "
        f"téléchargement {o.get('inet_down_cost')} USD/Go ; stockage {o.get('storage_total_cost')} USD/h ; "
        f"fin {o.get('end_date')})" for o in conformes) or "aucune") + "\n")
    if exclues:
        j.write("offres conformes écartées (machine ou hôte du premier lancement, ou illisibles) : "
                + (", ".join(str(o["id"]) for o in ecartees) or "aucune") + "\n")
if not conformes:
    print(f"aucune offre conforme au filtre du plan au plus {prix_max} USD/h (au moins {coeurs_min:g} cœurs effectifs, "
          f"{ram_min:g} Mo de mémoire vive, téléchargement au plus {tel_max} USD/Go, stockage au plus {sto_max} USD/h) : "
          f"pas de création", file=sys.stderr)
    sys.exit(3)
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
# prix au-dessus du devis après le choix : garde redondante (le filtre local l'exclut déjà), sans artefact possible (CH-14)
python3 -c 'import sys; sys.exit(0 if float(sys.argv[1]) <= float(sys.argv[2]) else 1)' "$DPH" "$PRIX_MAX" \
    || { echo "prix $DPH USD/h au-dessus du devis ($PRIX_MAX) : nœud, pas de création"; exit 3; }
# instances : aucune, hors les instances du programme arrêtées tolérées (relues arrêtées) et les instances d'autres
# projets nommées en argument, dont l'étiquette commence par « rr- » (liste positive, CH-13) ; seuls identifiants, états,
# étiquettes et prix s'affichent ; la somme des prix de celles qui sont en marche entre dans le crédit exigé
SOMME_AUTRES=$("$V" show instances --raw | python3 -c '
import json, sys
tol = set(sys.argv[1].split())
decl = set() if sys.argv[2] == "-" else set(sys.argv[2].split(","))
prefixe = sys.argv[4]
journal = open(sys.argv[3], "a", encoding="utf-8")
try:
    instances = json.load(sys.stdin)
    assert isinstance(instances, list)
except Exception:
    print("vastai show instances : réponse illisible ou commande en échec", file=sys.stderr); sys.exit(3)
vues, autres_vues, refusees, somme = [], [], [], 0.0
for i in instances:
    if not isinstance(i, dict):
        refusees.append("entrée illisible"); continue
    ident, etat, cur = str(i.get("id")), i.get("actual_status"), i.get("cur_state")
    etiquette = str(i.get("label") or "")
    arretee = etat in ("exited", "stopped") and cur == "stopped"
    if ident in tol and arretee:
        vues.append(f"{ident} ({etat}, {cur})")
    elif ident in decl and etiquette.startswith(prefixe):
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
    lignes.append("autres instances sur le compte (non tolérées ; autre projet : étiquette « " + prefixe + "… » exigée) : " + ", ".join(refusees))
for ligne in lignes:
    print(ligne, file=sys.stderr)
    journal.write(ligne + "\n")
journal.close()
if refusees:
    sys.exit(1)
print(f"{somme:.4f}")' "$ARRETEES_TOLEREES" "$AUTRES" "$T/lancement.txt" "$PREFIXE_AUTRES") \
    || { echo "instances : non tolérée(s), ou liste illisible (voir la ligne ci-dessus) : pas de création"; exit 2; }
# crédit exigé : calculé dans un programme qui relit la réponse et en vérifie la forme ; aucune valeur relue n'est
# insérée dans du code (CH-22)
c=0
CREDIT_LIGNE=$("$V" show user --raw 2>/dev/null | python3 -c '
import json, math, sys
heures, dph, autres = (float(x) for x in sys.argv[1:4])
try:
    credit = json.load(sys.stdin)["credit"]
except Exception:
    print("crédit illisible (vastai show user)"); sys.exit(2)
if isinstance(credit, bool) or not isinstance(credit, (int, float)) or not math.isfinite(credit):
    print("crédit illisible (vastai show user)"); sys.exit(2)
m = round(heures * (dph + autres) + 1.2, 2)
print(f"prix {dph:.4f} USD/h ; autres projets en marche {autres:.4f} USD/h ; crédit {credit:.2f} USD ; minimum {m:.2f} USD ({heures:g} h)")
sys.exit(0 if round(credit, 2) >= m else 3)' "$HEURES_CREDIT" "$DPH" "$SOMME_AUTRES") || c=$?
printf '%s\n' "$CREDIT_LIGNE" | tee -a "$T/lancement.txt"
case $c in
    0) ;;
    3) echo "crédit insuffisant pour P3 et les autres projets en marche : pas de lancement ; recharge demandée à Lazar"; exit 3 ;;
    *) echo "crédit illisible (vastai show user, code $c) : pas de création"; exit 2 ;;
esac
# 6. garde de calcul rejouée sur la commande, avec le GO validé par le module commun (elle lit, dans cette session, un
# autre registre : R-160)
printf '{"tool_input":{"command":"GO_ID=%s vastai create instance %s --raw --image python:3.11-bookworm --disk 80"}}' "$GOP3" "$OFFRE" \
    | python3 "$DEPOT/.claude/hooks/garde_calcul.py"
# 7. création : heure relue juste avant ; à partir d'ici, tout échec rend 4
H1=$(date -u +%H%M); [ "$H1" -lt 2330 ] || { echo "heure UTC $H1 : pas de création entre 23:30 et 00:00 (T-7)"; exit 3; }
trap - ERR
set +e
CREATION=$(date -u +%s)
export T_LANCEMENT="$T"
printf 'lanceur p3 v1 %s ; autres projets %s\ncommit %s\noffre %s\nprereg %s\nbranche %s\netiquette %s\ngo %s\ncreation %s\nplafond de la surveillance %s (création + %s s ; surveiller_p3_v1.sh <id> %s <dossier neuf>)\ncontrôle à cinq minutes entre %s et %s (création + 180 à 300 s ; controle_cinq_minutes_p3_v1.sh <id> %s <dossier neuf>)\ninstance : arrêtée par son identifiant à la fin, gardée arrêtée jusqu au verdict, 72 heures au plus, puis détruite par son identifiant (R10 ; texte, Plan d analyse, point 1.6)\n' \
    "$(sha256sum "$0" | cut -d' ' -f1)" "$AUTRES" "$S" "$OFFRE" "$P" "$BRANCHE" "$ETIQUETTE" "$GOP3" "$CREATION" \
    "$((CREATION + PLAFOND_SURVEILLANCE_S))" "$PLAFOND_SURVEILLANCE_S" "$CREATION" "$((CREATION + 180))" "$((CREATION + 300))" "$T" >> "$T/lancement.txt"
GO_ID="$GOP3" "$V" create instance "$OFFRE" --raw --image python:3.11-bookworm --disk 80 --cancel-unavail \
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
