#!/usr/bin/env bash
# Création de l'instance de la revalidation (T0.5), v3, en un seul appel, sous GO-2026-10-04-08 (plan de lancement v4 ;
# vérifications du remplissage, P-1 à P-4, N-1, N-3, N-6, N-11, Q-8, Q-9). Rien ne s'affiche des jetons. Aucune création si un
# contrôle échoue : contrôles avant dépense (appelés ici, sur le même S), offre, crédit, instances, amorce, garde.
# Pendant l'appel, aucun sous-agent ne tourne (les jetons passent dans les arguments du processus vastai, N-11).
# Usage : lancer_revalidation_v3.sh OFFRE DOSSIER_TRACES
set -euo pipefail
OFFRE=${1:?offre}; T=${2:?dossier des traces}
PRIX_MAX=1.30                                    # devis de la phase 0 : 0,80 à 1,30 USD l'heure (Q-9)
DEPOT=/home/user/controle-ia-travail
B=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
V=$B/venv-vastai/bin/vastai
P=prereg/T0.5-revalidation-equivalence-pilote-v1.md
FILTRE="gpu_name in [A100_SXM4,A100_PCIE] gpu_ram>=79 num_gpus=1 cuda_vers>=13.0 verified=true datacenter=true reliability>=0.99 cpu_ram>=128 disk_space>=80 rentable=true"
[[ "$OFFRE" =~ ^[0-9]+$ ]] || { echo "offre invalide"; exit 2; }
[ -e "$T" ] && { echo "$T existe déjà (R12)"; exit 2; }
mkdir -p "$T"
# 1. commit de scellement, poussé sur le dépôt de travail
S=$(git -C "$DEPOT" log --diff-filter=A -1 --format=%H -- "$P.sha256")
[[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "commit de scellement introuvable"; exit 2; }
git -C "$DEPOT" fetch -q origin main
git -C "$DEPOT" merge-base --is-ancestor "$S" origin/main || { echo "commit de scellement $S absent du dépôt distant"; exit 2; }
# 2. contrôles avant dépense sur un clone neuf du même S (N-3) : tous conformes, sinon arrêt
if ! bash "$B/scellement-revalidation/controles_avant_depense_v3.sh" "$S" "$T/clone-controles" > "$T/controles.txt" 2>&1; then
    tail -5 "$T/controles.txt"; echo "contrôles avant dépense en échec : pas de création"; exit 2
fi
tail -1 "$T/controles.txt" | grep -qx "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES" || { echo "contrôles : dernière ligne inattendue"; exit 2; }
rm -rf "$T/clone-controles"
# 3. amorce du commit de scellement ; son empreinte doit être citée (fichier, pas de tube vers grep -q : N-1)
git -C "$DEPOT" show "$S:$P" > "$T/prereg-S.md"
git -C "$DEPOT" show "$S":scripts/amorce_instance_t05.sh > "$T/amorce.sh"
E=$(sha256sum "$T/amorce.sh" | cut -d' ' -f1)
grep -qF "\`scripts/amorce_instance_t05.sh\` (\`$E\`, sha256)" "$T/prereg-S.md" \
    || { echo "empreinte de l'amorce ($E) non citée par le préenregistrement"; exit 2; }
B64=$(base64 -w0 < "$T/amorce.sh")
[ "$(printf %s "$B64" | base64 -d | sha256sum | cut -d' ' -f1)" = "$E" ] || { echo "encodage de l'amorce"; exit 2; }
# 4. jetons présents (jamais affichés) ; le jeton de l'instance est CONTROLE_IA_GITHUB_TOKEN (P-3)
: "${HF_TOKEN:?HF_TOKEN absent}" "${CONTROLE_IA_GITHUB_TOKEN:?CONTROLE_IA_GITHUB_TOKEN absent}"
# 5. offre : relue par le filtre du plan, archivée ; crédit minimal = 6 h au prix de l'offre + 0,9 USD (N-6)
"$V" search offers "$FILTRE" -o 'dph_total' --storage 80 --raw > "$T/offres-brut.json"
DPH=$(python3 - "$OFFRE" "$T/offres-brut.json" "$T/offre.json" <<'EOF'
import json, sys
offre, brut, sortie = int(sys.argv[1]), sys.argv[2], sys.argv[3]
d = [o for o in json.load(open(brut)) if o.get("id") == offre]
if len(d) != 1:
    sys.exit(f"offre {offre} absente des offres conformes au filtre du plan")
champs = ("id", "gpu_name", "gpu_ram", "num_gpus", "cuda_max_good", "driver_version", "cpu_ram", "disk_space",
          "reliability2", "verification", "hosting_type", "rentable", "end_date", "dph_total", "storage_total_cost",
          "inet_down_cost", "inet_up_cost", "geolocation")
json.dump({k: d[0].get(k) for k in champs}, open(sortie, "w"), indent=1)
print(d[0]["dph_total"])
EOF
)
rm -f "$T/offres-brut.json"
python3 -c "import sys; sys.exit(0 if float('$DPH') <= $PRIX_MAX else 1)" \
    || { echo "prix $DPH USD/h au-dessus du devis ($PRIX_MAX) : nœud, pas de création (Q-9)"; exit 3; }
CREDIT=$("$V" show user --raw | python3 -c 'import json, sys; print(json.load(sys.stdin)["credit"])')
python3 -c "import sys; m = 6 * float('$DPH') + 0.9; print(f'prix {float(\"$DPH\"):.4f} USD/h ; crédit {float(\"$CREDIT\"):.2f} USD ; minimum {m:.2f} USD'); sys.exit(0 if float('$CREDIT') >= m else 1)" \
    | tee -a "$T/lancement.txt" || { echo "crédit insuffisant : pas de lancement (P-1) ; recharge demandée à Lazar"; exit 3; }
N=$("$V" show instances --raw | python3 -c 'import json, sys; print(len(json.load(sys.stdin)))')
[ "$N" = 0 ] || { echo "$N instance(s) déjà sur le compte : pas de création"; exit 2; }
# 6. garde de calcul rejouée sur la commande (elle n'est pas active dans cette session)
printf '{"tool_input":{"command":"GO_ID=GO-2026-10-04-08 vastai create instance %s --raw --image python:3.11-bookworm --disk 80"}}' "$OFFRE" \
    | python3 "$DEPOT/.claude/hooks/garde_calcul.py"
# 7. création
CREATION=$(date -u +%s)
export T_LANCEMENT="$T"
printf 'commit %s\noffre %s\ncreation %s\n' "$S" "$OFFRE" "$CREATION" >> "$T/lancement.txt"
GO_ID=GO-2026-10-04-08 "$V" create instance "$OFFRE" --raw --image python:3.11-bookworm --disk 80 --cancel-unavail \
    --label "t05-revalidation" \
    --env "-e COMMIT=$S -e ETUDE=revalidation -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" \
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
