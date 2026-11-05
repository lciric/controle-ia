#!/usr/bin/env bash
# Création de l'instance de la revalidation (T0.5), v7 : après le contrôle mécanique (R-137 : CM-02 argument ou jeton
# absent → code 2 ; CM-06 commentaires ; contrôles v7). v6 : après la vérification des corrections (R-136 : VC-03 GO lu dans
# la v2 de S et non révoqué, VC-05 codes de sortie, VC-06 scripts exécutés égaux à leurs copies versées à S, VC-08 heure
# relue avant la création et place disque des traces, VC-09 clone des contrôles toujours supprimé, lignes KO affichées).
# v5 : préenregistrement v2 (N-018), passé au script de l'instance par
# PREREG, avec la branche BRANCHE=calcul/t05-revalidation-reel-v2 (la v1 occupe les défauts) ; après la relecture R2 du
# candidat 2 (R-135 : L-01 instance arrêtée tolérée par son identifiant, L-11 place disque, T-7 minuit, C-4 et C-6
# processeur archivé avec l'offre, L-13 PREREG et BRANCHE relus dans la v2 et consignés, étiquette propre). Depuis la v3
# (plan de lancement v5 ; vérifications du remplissage, P-1 à P-4, N-1, N-3, N-6, N-11, Q-8, Q-9), en un seul appel,
# sous GO-2026-10-04-08. Rien ne s'affiche des jetons. Aucune création si un contrôle échoue : contrôles avant dépense
# v7 (appelés ici, sur le même S), offre, crédit, instances, amorce, garde.
# Pendant l'appel, aucun sous-agent ne tourne (les jetons passent dans les arguments du processus vastai, N-11).
# Codes : 0 création ; 3 heure, place, crédit ou prix ; 4 tout échec à partir de la ligne « creation » de lancement.txt
# (création douteuse : vérifier les instances, forme filtrée) ; 2 tout autre arrêt avant la création.
# Usage : lancer_revalidation_v7.sh OFFRE DOSSIER_TRACES
set -euo pipefail
trap 'echo "arrêt avant la création (ligne $LINENO)"; exit 2' ERR
[ $# -eq 2 ] && [ -n "$1" ] && [ -n "$2" ] || { echo "usage : lancer_revalidation_v7.sh OFFRE DOSSIER_TRACES"; exit 2; }   # CM-02
OFFRE=$1; T=$2
PRIX_MAX=1.30                                    # devis de la phase 0 : 0,80 à 1,30 USD l'heure (Q-9)
DEPOT=/home/user/controle-ia-travail
B=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
V=$B/venv-vastai/bin/vastai
P=prereg/T0.5-revalidation-equivalence-pilote-v2.md
BRANCHE=calcul/t05-revalidation-reel-v2
ARRETEES_TOLEREES="55292763"                     # instances du programme arrêtées, gardées (disque) : tolérées si arrêtées
FILTRE="gpu_name in [A100_SXM4,A100_PCIE] gpu_ram>=79 num_gpus=1 cuda_vers>=13.0 verified=true datacenter=true reliability>=0.99 cpu_ram>=128 disk_space>=80 rentable=true"
[[ "$OFFRE" =~ ^[0-9]+$ ]] || { echo "offre invalide"; exit 2; }
[ -e "$T" ] && { echo "$T existe déjà (R12)"; exit 2; }
# 0. heure (T-7 : la suite des tests de l'instance, environ 1 à 12 minutes après la création, ne doit pas chevaucher
#    minuit UTC, à cause de test_garde_calcul) et place disque (L-11 : au moins 3 Go libres pour les contrôles et les traces)
H=$(date -u +%H%M); [ "$H" -lt 2330 ] || { echo "heure UTC $H : pas de création entre 23:30 et 00:00 (T-7)"; exit 3; }
LIBRE=$(df -Pk "$B" | awk 'NR==2 {print $4}'); [ "$LIBRE" -ge 3000000 ] || { echo "place disque : $LIBRE ko libres (3 Go exigés, L-11)"; exit 3; }
LIBRE_T=$(df -Pk "$(dirname "$T")" | awk 'NR==2 {print $4}'); [ "$LIBRE_T" -ge 3000000 ] || { echo "place disque des traces : $LIBRE_T ko (VC-08)"; exit 3; }
mkdir -p "$T"
trap 'rm -rf "$T/clone-controles"' EXIT        # le clone des contrôles ne reste jamais (VC-09)
printf 'heure de départ %s UTC ; place libre %s ko\n' "$(date -u +%H:%M:%S)" "$LIBRE" >> "$T/lancement.txt"
# 1. commit de scellement, poussé sur le dépôt de travail
S=$(git -C "$DEPOT" log --diff-filter=A -1 --format=%H -- "$P.sha256")
[[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "commit de scellement introuvable"; exit 2; }
git -C "$DEPOT" fetch -q origin main
git -C "$DEPOT" merge-base --is-ancestor "$S" origin/main || { echo "commit de scellement $S absent du dépôt distant"; exit 2; }
# 2. contrôles avant dépense sur un clone neuf du même S (N-3) : tous conformes, sinon arrêt
# les scripts exécutés sont ceux versés à S (VC-06)
for paire in "controles_avant_depense_v7.sh=$B/revalidation-v2/controles_avant_depense_v7.sh" "lancer_revalidation_v7.sh=$0"; do
    [ "$(git -C "$DEPOT" show "$S:docs/procedures/revalidation-T0.5-v2/${paire%%=*}" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$(sha256sum "${paire#*=}" | cut -d' ' -f1)" ] \
        || { echo "${paire%%=*} exécuté ≠ copie versée au commit S"; exit 2; }
done
if ! bash "$B/revalidation-v2/controles_avant_depense_v7.sh" "$S" "$T/clone-controles" > "$T/controles.txt" 2>&1; then
    grep '^KO' "$T/controles.txt" || tail -5 "$T/controles.txt"; echo "contrôles avant dépense en échec : pas de création"; exit 2
fi
tail -1 "$T/controles.txt" | grep -qx "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES" || { echo "contrôles : dernière ligne inattendue"; exit 2; }
rm -rf "$T/clone-controles"
# 3. amorce du commit de scellement ; son empreinte doit être citée (fichier, pas de tube vers grep -q : N-1)
git -C "$DEPOT" show "$S:$P" > "$T/prereg-S.md"
git -C "$DEPOT" show "$S":scripts/amorce_instance_t05.sh > "$T/amorce.sh"
E=$(sha256sum "$T/amorce.sh" | cut -d' ' -f1)
grep -qF "\`scripts/amorce_instance_t05.sh\` (\`$E\`, sha256)" "$T/prereg-S.md" \
    || { echo "empreinte de l'amorce ($E) non citée par le préenregistrement"; exit 2; }
grep -qF "\`PREREG=$P\`, \`BRANCHE=$BRANCHE\`" "$T/prereg-S.md" || { echo "PREREG ou BRANCHE : la v2 de S cite autre chose (L-13)"; exit 2; }
GO18=$(sed -n 's/^- Version 2 (N-018) : .* ; décision de Lazar : \(GO-[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}-[0-9]\{2\}\) (R-[0-9]*)\.$/\1/p' "$T/prereg-S.md")
[[ "$GO18" =~ ^GO-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}$ ]] || { echo "GO de Lazar sur N-018 introuvable dans la v2 de S (VC-03)"; exit 2; }
if grep '^| GO-' "$DEPOT/registres/go.md" | grep 'révocation' | grep -qF "$GO18"; then echo "$GO18 révoqué dans le registre courant"; exit 2; fi
B64=$(base64 -w0 < "$T/amorce.sh")
[ "$(printf %s "$B64" | base64 -d | sha256sum | cut -d' ' -f1)" = "$E" ] || { echo "encodage de l'amorce"; exit 2; }
# 4. jetons présents (jamais affichés) ; le jeton de l'instance est CONTROLE_IA_GITHUB_TOKEN (P-3)
[ -n "${HF_TOKEN:-}" ] && [ -n "${CONTROLE_IA_GITHUB_TOKEN:-}" ] || { echo "jeton absent (HF_TOKEN ou CONTROLE_IA_GITHUB_TOKEN) : pas de création (CM-02)"; exit 2; }
# 5. offre : relue par le filtre du plan, archivée ; crédit minimal = 6 h au prix de l'offre + 0,9 USD (N-6)
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
print(d[0]["dph_total"])
EOF
)
rm -f "$T/offres-brut.json"
python3 -c "import sys; sys.exit(0 if float('$DPH') <= $PRIX_MAX else 1)" \
    || { echo "prix $DPH USD/h au-dessus du devis ($PRIX_MAX) : nœud, pas de création (Q-9)"; exit 3; }
CREDIT=$("$V" show user --raw | python3 -c 'import json, sys; print(json.load(sys.stdin)["credit"])')
python3 -c "import sys; m = 6 * float('$DPH') + 0.9; print(f'prix {float(\"$DPH\"):.4f} USD/h ; crédit {float(\"$CREDIT\"):.2f} USD ; minimum {m:.2f} USD'); sys.exit(0 if float('$CREDIT') >= m else 1)" \
    | tee -a "$T/lancement.txt" || { echo "crédit insuffisant : pas de lancement (P-1) ; recharge demandée à Lazar"; exit 3; }
# instances : aucune, hors les instances arrêtées tolérées, relues arrêtées (L-01) ; seuls identifiants et états s'affichent
"$V" show instances --raw | python3 -c '
import json, sys
tol = set(sys.argv[1].split())
autres, vues = [], []
for i in json.load(sys.stdin):
    ident, etat, cur = str(i.get("id")), i.get("actual_status"), i.get("cur_state")
    if ident in tol and etat in ("exited", "stopped") and cur == "stopped":
        vues.append(f"{ident} ({etat}, {cur})")
    else:
        autres.append(f"{ident} ({etat}, {cur})")
print("instances arrêtées tolérées :", ", ".join(vues) or "aucune")
if autres:
    print("autres instances sur le compte :", ", ".join(autres)); sys.exit(1)' "$ARRETEES_TOLEREES" | tee -a "$T/lancement.txt" \
    || { echo "instance(s) non tolérée(s) sur le compte : pas de création"; exit 2; }
# 6. garde de calcul rejouée sur la commande (elle n'est pas active dans cette session)
printf '{"tool_input":{"command":"GO_ID=GO-2026-10-04-08 vastai create instance %s --raw --image python:3.11-bookworm --disk 80"}}' "$OFFRE" \
    | python3 "$DEPOT/.claude/hooks/garde_calcul.py"
# 7. création : heure relue juste avant (VC-08) ; à partir d'ici, tout échec rend 4 (VC-05)
H=$(date -u +%H%M); [ "$H" -lt 2330 ] || { echo "heure UTC $H : pas de création entre 23:30 et 00:00 (T-7, VC-08)"; exit 3; }
trap - ERR
set +e
CREATION=$(date -u +%s)
export T_LANCEMENT="$T"
printf 'commit %s\noffre %s\nprereg %s\nbranche %s\ngo N-018 %s\ncreation %s\n' "$S" "$OFFRE" "$P" "$BRANCHE" "$GO18" "$CREATION" >> "$T/lancement.txt"
GO_ID=GO-2026-10-04-08 "$V" create instance "$OFFRE" --raw --image python:3.11-bookworm --disk 80 --cancel-unavail \
    --label "t05-revalidation-v2" \
    --env "-e COMMIT=$S -e ETUDE=revalidation -e PREREG=$P -e BRANCHE=$BRANCHE -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" \
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
