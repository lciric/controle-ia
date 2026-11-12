#!/usr/bin/env bash
# Création de l'instance de la régénération des sondes figées de P3 (GO-2026-10-28-11 et son extension « par
# anticipation, en autonomie » ; devis docs/notes/regeneration-sondes-p3-v1/devis-regeneration-sondes-p3-v1.md), v1.
# Déclinée de `lancer_banque_t05_v4.sh` (prep/t05-banque-complete-v1, R-579) sous un nom nouveau (R12) : commit poussé et
# porteur de l'amorce, de la chaîne et du script ; branche de résultats absente ; garde de calcul avec le GO ; aucune autre
# instance sur le compte ; crédit relu ; offre choisie juste avant la création (identifiants instables sous vastai 1.8.3) :
# A100 SXM4 80 Go, une carte, **processeur AMD EPYC 7513 comme P3**, au moins 31 cœurs effectifs (30 fils sous l'affinité
# bornée, comme P3), au moins 128 Go de mémoire vive, CUDA ≥ 13.0, fiabilité ≥ 0,98 (une seule offre conforme relevée le
# 28 octobre à 22:10 UTC, 0,983 ; perte de l'hôte avant calcul couverte par une seconde instance au devis), prix ≤ 1,40 ;
# amorce encodée, jetons passés par --env sans jamais s'afficher. Rien ne se crée si un contrôle échoue.
# Codes : 0 création ; 3 offre, prix ou heure ; 4 création douteuse ; 2 autre arrêt.
# v1 après la contre-lecture R2 (CLR-03 garde de calcul dans un « if », éprouvée avec un GO inconnu ; CLR-05 fiche scellée).
# Usage : VASTAI=<vastai 1.8.3> lancer_regeneration_sondes_p3_v1.sh COMMIT DOSSIER_TRACES
set -euo pipefail
trap 'echo "arrêt avant la création (ligne $LINENO)"; exit 2' ERR
[ $# -eq 2 ] || { echo "usage : lancer_regeneration_sondes_p3_v1.sh COMMIT DOSSIER_TRACES"; exit 2; }
S=$1; T=$(realpath -m "$2")
[[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "COMMIT : 40 caractères hexadécimaux attendus"; exit 2; }
V=${VASTAI:?VASTAI : chemin de vastai 1.8.3}
[ "$("$V" --version 2>/dev/null | head -1)" = "1.8.3" ] || { echo "vastai : version différente de 1.8.3"; exit 2; }
GO=GO-2026-10-28-11
PRIX_MAX=1.40
COMMIT_P3=97dd82900cb120d5ce7328f8569d514fe987cc3c
DEPOT=/home/user/controle-ia-travail
BRANCHE=calcul/regeneration-sondes-p3-v1
ETIQUETTE=regeneration-sondes-p3-v1
[ -e "$T" ] && { echo "$T existe déjà (R12)"; exit 2; }
H0=$(date -u +%H%M); [ "$H0" -lt 2330 ] || { echo "heure UTC $H0 : pas de création entre 23:30 et 00:00 (T-7)"; exit 3; }
mkdir -p "$T"
trap 'rm -rf "$T/clone"' EXIT
printf 'lanceur %s ; départ %s UTC\n' "$(sha256sum "$0" | cut -d' ' -f1)" "$(date -u +%FT%TZ)" >> "$T/lancement.txt"
# 1. commit poussé sur main ; branche de résultats absente
git -C "$DEPOT" fetch -q origin main
git -C "$DEPOT" merge-base --is-ancestor "$S" FETCH_HEAD || { echo "commit $S absent de origin/main"; exit 2; }
rc=0; git -C "$DEPOT" ls-remote --exit-code --heads origin "$BRANCHE" >/dev/null 2>&1 || rc=$?
[ "$rc" = 2 ] || { echo "branche $BRANCHE présente sur le dépôt, ou ls-remote en erreur (code $rc)"; exit 2; }
rc=0; git -C "$DEPOT" ls-remote --exit-code --heads origin calcul/p3-reel-v1 >/dev/null 2>&1 || rc=$?
[ "$rc" = 0 ] || { echo "branche calcul/p3-reel-v1 absente : le commit de P3 ne serait pas cloné"; exit 2; }
# 2. amorce, chaîne et script du commit ; critère du devis scellé au commit
git clone -q --no-checkout "$DEPOT" "$T/clone" && git -C "$T/clone" checkout -q "$S"
for f in docs/notes/regeneration-sondes-p3-v1/fiche-lancement-regeneration-sondes-p3-v1.md scripts/amorce_regeneration_sondes_p3_v1.sh scripts/regeneration_sondes_p3_instance_v1.sh scripts/regenerer_sondes_p3_v1.py \
         docs/notes/regeneration-sondes-p3-v1/devis-regeneration-sondes-p3-v1.md; do
    [ -f "$T/clone/$f" ] || { echo "$f absent du commit $S"; exit 2; }
    echo "$f $(sha256sum "$T/clone/$f" | cut -d' ' -f1)" >> "$T/lancement.txt"
done
(cd "$T/clone/docs/notes/regeneration-sondes-p3-v1" && sha256sum -c --quiet devis-regeneration-sondes-p3-v1.md.sha256 \
        fiche-lancement-regeneration-sondes-p3-v1.md.sha256) \
    || { echo "devis ou fiche de lancement non scellés ou non conformes au commit (CLR-05)"; exit 2; }
grep -q 'SCEAU_P3 = "91b61c45cdafd0ab979e261171b9661920715fa42c6cbc9751cd2697bfd3177a"' "$T/clone/scripts/regenerer_sondes_p3_v1.py" \
    || { echo "sceau attendu de P3 absent du script"; exit 2; }
cp "$T/clone/scripts/amorce_regeneration_sondes_p3_v1.sh" "$T/amorce.sh"
E=$(sha256sum "$T/amorce.sh" | cut -d' ' -f1)
B64=$(base64 -w0 < "$T/amorce.sh")
[ "$(printf %s "$B64" | base64 -d | sha256sum | cut -d' ' -f1)" = "$E" ] || { echo "encodage de l'amorce"; exit 2; }
echo "amorce $E" >> "$T/lancement.txt"
# 3. jetons présents (jamais affichés)
[ -n "${HF_TOKEN:-}" ] && [ -n "${CONTROLE_IA_GITHUB_TOKEN:-}" ] || { echo "jeton absent (HF_TOKEN ou CONTROLE_IA_GITHUB_TOKEN) : pas de création"; exit 2; }
# 4. garde de calcul avec le GO
# (CLR-03 : la garde est dans un « if », jamais dans une liste « && » que « set -e » ne fait pas sortir)
if ! printf '{"tool_input":{"command":"GO_ID=%s vastai create instance %s --raw --image python:3.11-bookworm --disk 80"}}' "$GO" 0 \
        | python3 "$DEPOT/.claude/hooks/garde_calcul.py"; then
    echo "garde de calcul : $GO refusé : pas de création"; exit 2
fi
echo "garde de calcul : $GO accepté" | tee -a "$T/lancement.txt"
# 5. aucune autre instance
N=$(timeout 60 "$V" show instances --raw 2>/dev/null | python3 -I -c 'import json, sys; print(len(json.load(sys.stdin)))')
[ "$N" = 0 ] || { echo "$N instance(s) sur le compte : pas de création"; exit 2; }
# 6. crédit relu et consigné
timeout 60 "$V" show user --raw 2>/dev/null | python3 -I -c 'import json, sys; print("crédit relu :", round(float(json.load(sys.stdin)["credit"]), 2), "USD")' \
    | tee -a "$T/lancement.txt" || { echo "crédit illisible"; exit 2; }
# 7. offre choisie juste avant la création
LU=$(timeout 60 "$V" search offers "gpu_name=A100_SXM4 num_gpus=1" --storage 80 --raw 2>/dev/null | python3 -I -c '
import json, sys
p = float(sys.argv[1])
ok = [o for o in json.load(sys.stdin) if o.get("gpu_name") == "A100 SXM4" and o.get("num_gpus") == 1
      and o.get("cpu_name") == "AMD EPYC 7513 32-Core Processor" and float(o.get("cpu_cores_effective") or 0) >= 31
      and float(o.get("cpu_ram") or 0) >= 128000 and float(o.get("gpu_ram") or 0) >= 79 * 1024
      and float(o.get("cuda_max_good") or 0) >= 13.0 and 0 < float(o["dph_total"]) <= p
      and float(o.get("reliability2") or 0) >= 0.98 and o.get("machine_id") != 142924]
if not ok: sys.exit("aucune offre conforme")
o = min(ok, key=lambda o: (o["dph_total"], o["id"]))
print(o["id"], o["dph_total"], o.get("machine_id"), o.get("cuda_max_good"), o.get("cpu_cores_effective"), o.get("reliability2"), str(o.get("geolocation")).replace(" ", "_"))' "$PRIX_MAX") || { echo "aucune offre conforme"; exit 3; }
read -r OFFRE DPH MACHINE CUDA COEURS FIAB LIEU <<< "$LU"
[[ "$OFFRE" =~ ^[0-9]+$ ]] || { echo "offre invalide"; exit 2; }
echo "offre $OFFRE : $DPH USD/h ; machine $MACHINE ; CUDA $CUDA ; $COEURS cœurs effectifs ; fiabilité $FIAB ; $LIEU" | tee -a "$T/lancement.txt"
# 8. création ; à partir d'ici, tout échec rend 4
trap - ERR
set +e
CREATION=$(date -u +%s)
export T_LANCEMENT="$T"
printf 'go %s\ncommit %s\ncommit_p3 %s\noffre %s\nbranche %s\netiquette %s\ncreation %s\n' "$GO" "$S" "$COMMIT_P3" "$OFFRE" "$BRANCHE" "$ETIQUETTE" "$CREATION" >> "$T/lancement.txt"
GO_ID=$GO "$V" create instance "$OFFRE" --raw --image python:3.11-bookworm --disk 80 --cancel-unavail \
    --label "$ETIQUETTE" \
    --env "-e COMMIT=$S -e COMMIT_P3=$COMMIT_P3 -e BRANCHE=$BRANCHE -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" \
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
    print("réponse illisible (300 premiers caractères masqués) ; vérifier par « vastai show instances », sans --raw")
    sys.exit(4)
ok = d.get("success") is True and isinstance(d.get("new_contract"), int)
print("succès :", d.get("success"), "; identifiant", d.get("new_contract"), "; message :", str(d.get("msg", ""))[:200])
sys.exit(0 if ok else 4)' | tee -a "$T/lancement.txt"
st=("${PIPESTATUS[@]}")
[ "${st[0]}" = 0 ] && [ "${st[1]}" = 0 ] && [ "${st[2]}" = 0 ] || { echo "création douteuse (statuts ${st[*]}) : vérifier « vastai show instances », sans --raw"; exit 4; }
exit 0
