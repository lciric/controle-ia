#!/usr/bin/env bash
# Création de l'instance du pilote de T0.5 (préenregistrement prereg/T0.5-pilote-8B-v1.md), v1, sur le modèle du lanceur
# v7 de la revalidation (19 cas éprouvés) et des constats de l'état des lieux du pilote (PL-08, PL-12, PL-13, PF-01,
# ML-03, ML-04) : ETUDE=pilote, PREREG et BRANCHE passés explicitement et relus dans le préenregistrement de S,
# DEPOT_URL du dépôt de travail ; relancement unique sur la branche …-v2, explicite, seulement pour une cause
# d'infrastructure consignée et sans episodes.json sur …-v1 ; crédit ≥ 6 h × prix + 1,2 USD (deux modèles téléchargés) ;
# instances arrêtées 55292763 et 55458787 tolérées si relues arrêtées ; base de la surveillance écrite (CREATION − 3 900 s,
# soit un plafond de 17 700 s avec surveiller-instance-t04-v1.sh). En un seul appel, sous GO-2026-10-04-08, décision
# de Lazar sur N-019 (GO cité par S, relu dans le registre courant, sans ligne « révocation » qui le nomme ; colonne
# d'état de N-019 à la forme exacte « tranché (a) par Lazar : GO (R-…) » ; relecture R2, NO-03, CH-10). Rien ne s'affiche
# des jetons. Aucune création si un contrôle échoue (contrôles avant dépense du pilote, rejoués ici sur le même S, suite
# complète des tests comprise). Pendant l'appel, aucun sous-agent ne tourne.
# Codes : 0 création ; 3 heure, place, crédit ou prix ; 4 tout échec à partir de la ligne « creation » de lancement.txt
# (création douteuse : vérifier les instances, forme filtrée, jamais --raw sans filtre) ; 2 tout autre arrêt avant.
# Usage : lancer_pilote_v1.sh OFFRE DOSSIER_TRACES [relance R-NNN]
set -euo pipefail
trap 'echo "arrêt avant la création (ligne $LINENO)"; exit 2' ERR
{ [ $# -eq 2 ] || [ $# -eq 4 ]; } && [ -n "$1" ] && [ -n "$2" ] || { echo "usage : lancer_pilote_v1.sh OFFRE DOSSIER_TRACES [relance R-NNN]"; exit 2; }
OFFRE=$1; T=$(realpath -m "$2"); MODE_LANCEMENT=premier; CAUSE=""        # traces en chemin absolu (CH-11)
if [ $# -eq 4 ]; then
    [ "$3" = relance ] && [[ "$4" =~ ^R-[0-9]{3,4}$ ]] || { echo "relance : « relance R-NNN » attendu"; exit 2; }
    MODE_LANCEMENT=relance; CAUSE=$4
fi
PRIX_MAX=1.30                                    # devis de la phase 0 : 0,80 à 1,30 USD l'heure (Q-9)
DEPOT=/home/user/controle-ia-travail
B=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
H=$B/pilote-v1
V=$B/venv-vastai/bin/vastai
VERSEES=docs/procedures/pilote-T0.5-v1
P=prereg/T0.5-pilote-8B-v1.md
if [ "$MODE_LANCEMENT" = premier ]; then BRANCHE=calcul/t05-pilote-reel-v1; ETIQUETTE=t05-pilote-v1
else BRANCHE=calcul/t05-pilote-reel-v2; ETIQUETTE=t05-pilote-v1-relance; fi
ARRETEES_TOLEREES="55292763 55458787"            # instances du programme arrêtées, gardées (disque) : tolérées si arrêtées
FILTRE="gpu_name=A100_SXM4 gpu_ram>=79 num_gpus=1 cuda_vers>=13.0 verified=true datacenter=true reliability>=0.99 cpu_ram>=128 disk_space>=80 rentable=true"
[[ "$OFFRE" =~ ^[0-9]+$ ]] || { echo "offre invalide"; exit 2; }
[ -e "$T" ] && { echo "$T existe déjà (R12)"; exit 2; }
# 0. heure (la suite des tests de l'instance ne doit pas chevaucher minuit UTC, test_garde_calcul ; T-7) et place disque
H0=$(date -u +%H%M); [ "$H0" -lt 2330 ] || { echo "heure UTC $H0 : pas de création entre 23:30 et 00:00 (T-7)"; exit 3; }
LIBRE=$(df -Pk "$B" | awk 'NR==2 {print $4}'); [ "$LIBRE" -ge 3000000 ] || { echo "place disque : $LIBRE ko libres (3 Go exigés)"; exit 3; }
LIBRE_T=$(df -Pk "$(dirname "$T")" | awk 'NR==2 {print $4}'); [ "$LIBRE_T" -ge 3000000 ] || { echo "place disque des traces : $LIBRE_T ko"; exit 3; }
mkdir -p "$T"
trap 'rm -rf "$T/clone-controles"' EXIT        # le clone des contrôles ne reste jamais
printf 'heure de départ %s UTC ; place libre %s ko ; mode %s\n' "$(date -u +%H:%M:%S)" "$LIBRE" "$MODE_LANCEMENT" >> "$T/lancement.txt"
# 1. commit de scellement, poussé sur le dépôt de travail ; colonne d'état de N-019 à la forme exacte ; relance consignée
S=$(git -C "$DEPOT" log --diff-filter=A -1 --format=%H -- "$P.sha256")
[[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "commit de scellement introuvable"; exit 2; }
git -C "$DEPOT" fetch -q origin main
git -C "$DEPOT" merge-base --is-ancestor "$S" origin/main || { echo "commit de scellement $S absent du dépôt distant"; exit 2; }
PREMIERE=$(python3 - "$DEPOT/registres/decisions.md" "$MODE_LANCEMENT" "$CAUSE" <<'EOF'

import re, sys
lignes = open(sys.argv[1], encoding="utf-8").read().split("\n")
n19 = [x for x in lignes if x.startswith("| N-019 |")]
# forme exacte de la colonne d'état (relecture R2, CH-10) : aucun mot-clé cherché ; une révocation de la décision de
# Lazar est une ligne de type « révocation » de registres/go.md, relue plus bas (bloc GO19)
etat = n19[0].rsplit("|", 2)[-2].strip() if len(n19) == 1 else ""
if not re.fullmatch(r"tranché \(a\) par Lazar : GO-\d{4}-\d{2}-\d{2}-\d{2} \(R-\d{3,4}\)", etat):
    sys.exit("N-019")
if sys.argv[2] == "relance":
    r = [x for x in lignes if x.startswith(f"| {sys.argv[3]} |")]
    if len(r) != 1 or not all(m in r[0].lower() for m in ("relancement", "pilote", "infrastructure")):
        sys.exit("relance non consignée")
    # l'instance du premier lancement, arrêtée et gardée, est nommée par la ligne de la cause (CH-02)
    inst = re.findall(r"\binstance (\d{8})\b", r[0])
    if len(set(inst)) != 1:
        sys.exit("relance : la ligne de la cause ne nomme pas, une seule fois, l'instance du premier lancement")
    print(inst[0])
EOF
) || { echo "registre des décisions : N-019 non tranchée par Lazar (forme exacte), ou relance non consignée"; exit 2; }
[ -n "$PREMIERE" ] && ARRETEES_TOLEREES="$ARRETEES_TOLEREES $PREMIERE"
# 2. contrôles avant dépense sur un clone neuf du même S ; scripts exécutés égaux à leurs copies versées à S
for paire in "controles_avant_depense_pilote_v1.sh=$H/controles_avant_depense_pilote_v1.sh" \
             "normaliser_pilote_v1.py=$H/normaliser_pilote_v1.py" "lancer_pilote_v1.sh=$0"; do
    [ "$(git -C "$DEPOT" show "$S:$VERSEES/${paire%%=*}" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$(sha256sum "${paire#*=}" | cut -d' ' -f1)" ] \
        || { echo "${paire%%=*} exécuté ≠ copie versée au commit S"; exit 2; }
done
# jetons présents (jamais affichés), avant les contrôles qui durent environ 20 minutes (CH-11)
[ -n "${HF_TOKEN:-}" ] && [ -n "${CONTROLE_IA_GITHUB_TOKEN:-}" ] || { echo "jeton absent (HF_TOKEN ou CONTROLE_IA_GITHUB_TOKEN) : pas de création"; exit 2; }
ARG_RELANCE=(); [ "$MODE_LANCEMENT" = relance ] && ARG_RELANCE=(relance)
if ! timeout 3600 bash "$H/controles_avant_depense_pilote_v1.sh" "$S" "$T/clone-controles" "${ARG_RELANCE[@]}" > "$T/controles.txt" 2>&1; then
    grep '^KO' "$T/controles.txt" || tail -5 "$T/controles.txt"; echo "contrôles avant dépense en échec : pas de création"; exit 2
fi
tail -1 "$T/controles.txt" | grep -qx "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES" || { echo "contrôles : dernière ligne inattendue"; exit 2; }
rm -rf "$T/clone-controles"
# 3. amorce du commit de scellement ; son empreinte doit être citée (fichier, pas de tube vers grep -q)
git -C "$DEPOT" show "$S:$P" > "$T/prereg-S.md"
git -C "$DEPOT" show "$S":scripts/amorce_instance_t05.sh > "$T/amorce.sh"
E=$(sha256sum "$T/amorce.sh" | cut -d' ' -f1)
grep -qF "\`scripts/amorce_instance_t05.sh\` (\`$E\`, sha256)" "$T/prereg-S.md" \
    || { echo "empreinte de l'amorce ($E) non citée par le préenregistrement"; exit 2; }
grep -qF "\`PREREG=$P\`, \`BRANCHE=$BRANCHE\`" "$T/prereg-S.md" || { echo "PREREG ou BRANCHE : le préenregistrement de S cite autre chose"; exit 2; }
# décision de Lazar sur N-019 citée par S (relecture R2, NO-03), relue dans les registres courants, en Python (PL-18) :
# GO de type « revendication », accordé par Lazar, qui cite N-019 et l'option (a) ; ni lui ni le GO de calcul révoqués
# (K-3) ; colonne d'état de N-019 à la forme exacte, qui cite ce GO et sa ligne R-… ; ligne R-… qui le consigne
GO19=$(python3 - "$T/prereg-S.md" "$DEPOT/registres/go.md" "$DEPOT/registres/decisions.md" <<'PYGO'
import re, sys
texte, go_md, dec_md = (open(f, encoding="utf-8").read() for f in sys.argv[1:4])
m = re.findall(r"^- Décision de Lazar sur N-019 : `(GO-\d{4}-\d{2}-\d{2}-\d{2})` \((R-\d{3,4})\)", texte, re.M)
if len(m) != 1:
    sys.exit("GO de Lazar sur N-019 introuvable dans le préenregistrement de S")
go = m[0][0]
lignes = go_md.split("\n")
c = [[x.strip() for x in l.strip().strip("|").split("|")] for l in lignes if l.startswith(f"| {go} |")]
if len(c) != 1 or len(c[0]) != 8 or c[0][2] != "revendication" or c[0][6] != "Lazar" or "N-019" not in c[0][3] \
        or "(a)" not in c[0][3]:
    sys.exit(f"{go} : absent du registre courant, ou d'un autre type, ou non accordé par Lazar, ou sans N-019 et l'option (a)")
for g in (go, "GO-2026-10-04-08"):
    if [l for l in lignes if l.startswith("| GO-") and (lambda c: (len(c) == 8 and c[2].lower() == "révocation" and (g in c[3] or g in c[7])) or (len(c) != 8 and "révocation" in l.lower() and g in l))([x.strip() for x in l.strip().strip("|").split("|")])]:
        sys.exit(f"{g} révoqué dans le registre courant")
reg = m[0][1]
dec = dec_md.split("\n")
n19 = [l for l in dec if l.startswith("| N-019 |")]
etat = n19[0].rsplit("|", 2)[-2].strip() if len(n19) == 1 else ""
if not re.fullmatch(rf"tranché \(a\) par Lazar : {re.escape(go)} \({re.escape(reg)}\)", etat):
    sys.exit(f"N-019 : la colonne d'état courante n'est pas « tranché (a) par Lazar : {go} ({reg}) »")
r = [l for l in dec if l.startswith(f"| {reg} |")]
if len(r) != 1 or go not in r[0]:
    sys.exit(f"{reg} : absent du registre courant, en double, ou sans {go}")
print(go)
PYGO
) || { echo "décision de Lazar sur N-019 : ${GO19:-contrôle en échec}"; exit 2; }
B64=$(base64 -w0 < "$T/amorce.sh")
[ "$(printf %s "$B64" | base64 -d | sha256sum | cut -d' ' -f1)" = "$E" ] || { echo "encodage de l'amorce"; exit 2; }
# 4. jetons présents (jamais affichés) ; le jeton de l'instance est CONTROLE_IA_GITHUB_TOKEN
[ -n "${HF_TOKEN:-}" ] && [ -n "${CONTROLE_IA_GITHUB_TOKEN:-}" ] || { echo "jeton absent (HF_TOKEN ou CONTROLE_IA_GITHUB_TOKEN) : pas de création"; exit 2; }
# 5. offre : relue par le filtre du plan, processeur de la revalidation exigé (débit mesuré, AVX2 ; état des lieux),
#    archivée avec le processeur ; crédit minimal = 6 h au prix de l'offre + 1,2 USD
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
    sys.exit(f"offre {offre} : carte {d[0].get('gpu_name')!r} ; seule l'A100 SXM4 de la revalidation est admise (débit mesuré ; CH-04)")
if d[0].get("cpu_name") != "AMD EPYC 7513 32-Core Processor":
    sys.exit(f"offre {offre} : processeur {d[0].get('cpu_name')!r} ; seul celui de la revalidation (AMD EPYC 7513, débit mesuré, AVX2) est admis")
print(d[0]["dph_total"])
EOF
)
rm -f "$T/offres-brut.json"
python3 -c "import sys; sys.exit(0 if float('$DPH') <= $PRIX_MAX else 1)" \
    || { echo "prix $DPH USD/h au-dessus du devis ($PRIX_MAX) : nœud, pas de création"; exit 3; }
CREDIT=$("$V" show user --raw | python3 -c 'import json, sys; print(json.load(sys.stdin)["credit"])')
python3 -c "import sys; m = round(6 * float('$DPH') + 1.2, 2); print(f'prix {float(\"$DPH\"):.4f} USD/h ; crédit {float(\"$CREDIT\"):.2f} USD ; minimum {m:.2f} USD'); sys.exit(0 if round(float('$CREDIT'), 2) >= m else 1)" \
    | tee -a "$T/lancement.txt" || { echo "crédit insuffisant : pas de lancement ; recharge demandée à Lazar"; exit 3; }
# instances : aucune, hors les instances arrêtées tolérées, relues arrêtées ; seuls identifiants et états s'affichent
"$V" show instances --raw | python3 -c '
import json, sys
tol = set(sys.argv[1].split())
autres, vues = [], []
try:
    instances = json.load(sys.stdin)
except Exception:
    print("vastai show instances : réponse illisible ou commande en échec (CH-11)"); sys.exit(3)
for i in instances:
    ident, etat, cur = str(i.get("id")), i.get("actual_status"), i.get("cur_state")
    if ident in tol and etat in ("exited", "stopped") and cur == "stopped":
        vues.append(f"{ident} ({etat}, {cur})")
    else:
        autres.append(f"{ident} ({etat}, {cur})")
print("instances arrêtées tolérées :", ", ".join(vues) or "aucune")
if autres:
    print("autres instances sur le compte :", ", ".join(autres)); sys.exit(1)' "$ARRETEES_TOLEREES" | tee -a "$T/lancement.txt" \
    || { echo "instances : non tolérée(s), ou liste illisible (voir la ligne ci-dessus) : pas de création"; exit 2; }
# 6. garde de calcul rejouée sur la commande (elle n'est pas active dans cette session)
printf '{"tool_input":{"command":"GO_ID=GO-2026-10-04-08 vastai create instance %s --raw --image python:3.11-bookworm --disk 80"}}' "$OFFRE" \
    | python3 "$DEPOT/.claude/hooks/garde_calcul.py"
# 7. création : heure relue juste avant ; à partir d'ici, tout échec rend 4
H1=$(date -u +%H%M); [ "$H1" -lt 2330 ] || { echo "heure UTC $H1 : pas de création entre 23:30 et 00:00 (T-7)"; exit 3; }
trap - ERR
set +e
CREATION=$(date -u +%s)
export T_LANCEMENT="$T"
printf 'commit %s\noffre %s\nprereg %s\nbranche %s\netiquette %s\ngo N-019 %s\ncreation %s\nbase de la surveillance %s (plafond 17 700 s)\n' \
    "$S" "$OFFRE" "$P" "$BRANCHE" "$ETIQUETTE" "$GO19" "$CREATION" "$((CREATION - 3900))" >> "$T/lancement.txt"
GO_ID=GO-2026-10-04-08 "$V" create instance "$OFFRE" --raw --image python:3.11-bookworm --disk 80 --cancel-unavail \
    --label "$ETIQUETTE" \
    --env "-e COMMIT=$S -e ETUDE=pilote -e PREREG=$P -e BRANCHE=$BRANCHE -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" \
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
