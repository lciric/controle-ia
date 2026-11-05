#!/usr/bin/env bash
# Création de l'instance du rejeu de la cellule de juge redéfinie sur les 180 notations, 120 textes, du pilote de T0.5
# (GO-2026-10-29-04, plafond 4 USD ; devis et fiche de lancement : docs/notes/couche-2-preparation-v1/rejeu-juges-v2/),
# v2. Copie adaptée de `lancer_rejeu_juges_v1.sh` (lanceur v4 sous vastai 1.8.3, offre choisie en Python juste avant la
# création) sous un nom nouveau (R12 : la v1 n'est pas modifiée) : commit poussé sur origin/main et porteur de la fiche, du
# devis, de la configuration (scellés),
# du module, de ses essais, de l'amorce et du script de l'instance ; fiche sans marqueur restant et citant un commit du code
# ancêtre du commit lancé ; branche de résultats absente ; garde de calcul avec le GO, dans un « if » ; aucune autre
# instance sur le compte ; crédit relu et au moins CREDIT_MIN ; offre A100 SXM4 80 Go, une carte, la moins chère, au plus
# 1,43 USD/h, fiabilité ≥ 0,98, CUDA ≥ 13.0, mémoire vive ≥ 64 Go, téléchargement ≤ 0,01 USD/Go (devis § 5 : pire cas
# sous 4 USD) ; amorce encodée, jetons passés par --env sans jamais s'afficher. Rien ne se crée si un contrôle échoue.
# Codes : 0 création ; 3 offre, prix ou crédit ; 4 création douteuse ; 2 autre arrêt.
# Usage : VASTAI=<vastai 1.8.3> lancer_rejeu_juges_v2.sh COMMIT DOSSIER_TRACES
set -euo pipefail
trap 'echo "arrêt avant la création (ligne $LINENO)"; exit 2' ERR
[ $# -eq 2 ] || { echo "usage : lancer_rejeu_juges_v2.sh COMMIT DOSSIER_TRACES"; exit 2; }
S=$1; T=$(realpath -m "$2")
[[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "COMMIT : 40 caractères hexadécimaux attendus"; exit 2; }
V=${VASTAI:?VASTAI : chemin de vastai 1.8.3}
[ "$("$V" --version 2>/dev/null | head -1)" = "1.8.3" ] || { echo "vastai : version différente de 1.8.3"; exit 2; }
GO=GO-2026-10-29-04
PRIX_MAX=1.43
DESCENTE_MAX=0.01            # USD par Go téléchargé (≈ 27 Go : modèles 8B et 3B, roues)
CREDIT_MIN=4.50              # plafond du GO (4 USD) et une marge
DEPOT=${DEPOT:-/home/user/controle-ia-travail}
BRANCHE=calcul/rejeu-juges-v2
ETIQUETTE=rejeu-juges-v2
NOTES=docs/notes/couche-2-preparation-v1/rejeu-juges-v2
FICHE=$NOTES/fiche-lancement-rejeu-juges-v2.md
[ -e "$T" ] && { echo "$T existe déjà (R12)"; exit 2; }
mkdir -p "$T"
trap 'rm -rf "$T/clone"' EXIT
printf 'lanceur %s ; départ %s UTC\n' "$(sha256sum "$0" | cut -d' ' -f1)" "$(date -u +%FT%TZ)" >> "$T/lancement.txt"
# 1. commit poussé sur main ; branche de résultats absente
git -C "$DEPOT" fetch -q origin main
git -C "$DEPOT" merge-base --is-ancestor "$S" FETCH_HEAD || { echo "commit $S absent de origin/main"; exit 2; }
rc=0; git -C "$DEPOT" ls-remote --exit-code --heads origin "$BRANCHE" >/dev/null 2>&1 || rc=$?
[ "$rc" = 2 ] || { echo "branche $BRANCHE présente sur le dépôt, ou ls-remote en erreur (code $rc)"; exit 2; }
# 2. pièces du commit ; fiche, devis et configuration scellés au commit ; fiche sans marqueur restant
git clone -q --no-checkout "$DEPOT" "$T/clone" && git -C "$T/clone" checkout -q "$S"
for f in "$FICHE" "$NOTES/devis-rejeu-juges-v2.md" "$NOTES/config-rejeu-juges-v2.json" \
         scripts/amorce_rejeu_juges_v2.sh scripts/rejeu_juges_instance_v2.sh \
         src/controle_ia/environnements/noter_rejeu_juges_v2.py tests/test_noter_rejeu_juges_v2.py \
         src/controle_ia/environnements/noter_rejeu_juges_v1.py tests/test_noter_rejeu_juges_v1.py; do
    [ -f "$T/clone/$f" ] || { echo "$f absent du commit $S"; exit 2; }
    echo "$f $(sha256sum "$T/clone/$f" | cut -d' ' -f1)" >> "$T/lancement.txt"
done
(cd "$T/clone/$NOTES" && sha256sum -c --quiet fiche-lancement-rejeu-juges-v2.md.sha256 devis-rejeu-juges-v2.md.sha256 \
        config-rejeu-juges-v2.json.sha256) \
    || { echo "fiche, devis ou configuration non scellés ou non conformes au commit"; exit 2; }
if grep -n -e 'À REMPLIR' -e '<<[A-Z0-9_]*>>' "$T/clone/$FICHE"; then
    echo "fiche : marqueur restant (contre-lecture, commit du code ou tests attendus non remplis)"; exit 2
fi
CODE=$(sed -n "s/.*Commit du code d'analyse : \`\\([0-9a-f]\\{40\\}\\)\`.*/\\1/p" "$T/clone/$FICHE")
[ "$(printf '%s\n' "$CODE" | grep -c .)" = 1 ] || { echo "fiche : commit du code absent ou cité plusieurs fois"; exit 2; }
git -C "$T/clone" merge-base --is-ancestor "$CODE" "$S" || { echo "commit du code $CODE non ancêtre du commit lancé"; exit 2; }
# arbre gelé identique entre le commit du code et le commit lancé (contre-lecture R2, CLR2-01) : mêmes chemins que
# `validation_reelle.CHEMINS_GELES`, que le module compare au début du run (code, essais, scripts, .claude,
# dépendances, configuration) ; sinon le run s'arrêterait après ≈ 25 minutes payées. Dans un « if » (set -e, trap ERR).
if ! git -C "$T/clone" diff --quiet "$CODE" "$S" -- . ':(exclude)prereg' ':(exclude)brouillons' ':(exclude)registres' \
        ':(exclude)docs' ':(exclude)diag' ':(exclude)runs' ':(exclude)donnees' ':(exclude)livrables' ':(exclude)papiers' \
        ':(exclude)traces' ':(exclude)CLAUDE.md'; then
    echo "arbre gelé (code, essais, scripts, dépendances) modifié entre le commit du code $CODE et le commit lancé $S : pas de création"
    exit 2
fi
echo "arbre gelé identique au commit du code" >> "$T/lancement.txt"
echo "commit du code $CODE" >> "$T/lancement.txt"
cp "$T/clone/scripts/amorce_rejeu_juges_v2.sh" "$T/amorce.sh"
E=$(sha256sum "$T/amorce.sh" | cut -d' ' -f1)
B64=$(base64 -w0 < "$T/amorce.sh")
[ "$(printf %s "$B64" | base64 -d | sha256sum | cut -d' ' -f1)" = "$E" ] || { echo "encodage de l'amorce"; exit 2; }
echo "amorce $E" >> "$T/lancement.txt"
# 3. jetons présents (jamais affichés)
[ -n "${HF_TOKEN:-}" ] && [ -n "${CONTROLE_IA_GITHUB_TOKEN:-}" ] || { echo "jeton absent (HF_TOKEN ou CONTROLE_IA_GITHUB_TOKEN) : pas de création"; exit 2; }
# 4. garde de calcul avec le GO, dans un « if » (jamais dans une liste « && » que « set -e » ne fait pas sortir)
if ! printf '{"tool_input":{"command":"GO_ID=%s vastai create instance %s --raw --image python:3.11-bookworm --disk 80"}}' "$GO" 0 \
        | python3 "$DEPOT/.claude/hooks/garde_calcul.py"; then
    echo "garde de calcul : $GO refusé : pas de création"; exit 2
fi
echo "garde de calcul : $GO accepté" | tee -a "$T/lancement.txt"
# 5. aucune autre instance sur le compte
N=$(timeout 60 "$V" show instances --raw 2>/dev/null | python3 -I -c 'import json, sys; print(len(json.load(sys.stdin)))')
[ "$N" = 0 ] || { echo "$N instance(s) sur le compte : pas de création"; exit 2; }
# 6. crédit relu, consigné, au moins CREDIT_MIN
CREDIT=$(timeout 60 "$V" show user --raw 2>/dev/null | python3 -I -c 'import json, sys; print(round(float(json.load(sys.stdin)["credit"]), 2))') \
    || { echo "crédit illisible"; exit 2; }
echo "crédit relu : $CREDIT USD" | tee -a "$T/lancement.txt"
python3 -I -c 'import sys; sys.exit(0 if float(sys.argv[1]) >= float(sys.argv[2]) else 1)' "$CREDIT" "$CREDIT_MIN" \
    || { echo "crédit $CREDIT USD < $CREDIT_MIN USD : pas de création"; exit 3; }
# 7. offre choisie juste avant la création (identifiants instables sous vastai 1.8.3)
LU=$(timeout 60 "$V" search offers "gpu_name=A100_SXM4 num_gpus=1" --storage 80 --raw 2>/dev/null | python3 -I -c '
import json, sys
p, d = float(sys.argv[1]), float(sys.argv[2])
def f(o, k, defaut):
    v = o.get(k)
    return float(v) if v is not None else defaut
ok = [o for o in json.load(sys.stdin) if o.get("gpu_name") == "A100 SXM4" and o.get("num_gpus") == 1
      and f(o, "gpu_ram", 0) >= 79 * 1024 and f(o, "cpu_ram", 0) >= 64000 and f(o, "cuda_max_good", 0) >= 13.0
      and 0 < f(o, "dph_total", 99) <= p and f(o, "reliability2", 0) >= 0.98 and f(o, "inet_down_cost", 99) <= d]
if not ok: sys.exit("aucune offre conforme")
o = min(ok, key=lambda o: (float(o["dph_total"]), o["id"]))
print(o["id"], o["dph_total"], o.get("machine_id"), o.get("cuda_max_good"), o.get("reliability2"), o.get("inet_down_cost"),
      str(o.get("cpu_name")).replace(" ", "_"), str(o.get("geolocation")).replace(" ", "_"))' "$PRIX_MAX" "$DESCENTE_MAX") \
    || { echo "aucune offre conforme"; exit 3; }
read -r OFFRE DPH MACHINE CUDA FIAB DESCENTE PROC LIEU <<< "$LU"
[[ "$OFFRE" =~ ^[0-9]+$ ]] || { echo "offre invalide"; exit 2; }
echo "offre $OFFRE : $DPH USD/h ; machine $MACHINE ; CUDA $CUDA ; fiabilité $FIAB ; téléchargement $DESCENTE USD/Go ; $PROC ; $LIEU" | tee -a "$T/lancement.txt"
# 8. création ; à partir d'ici, tout échec rend 4
trap - ERR
set +e
CREATION=$(date -u +%s)
export T_LANCEMENT="$T"
printf 'go %s\ncommit %s\noffre %s\nbranche %s\netiquette %s\ncreation %s\narret_au_plus_tard %s (création + 140 min : amorce 120 + 5, démarrage et arrêt 15)\n' \
    "$GO" "$S" "$OFFRE" "$BRANCHE" "$ETIQUETTE" "$CREATION" "$((CREATION + 8400))" >> "$T/lancement.txt"
# réveils de garde (contre-lecture, CLJ-04) : la session les programme (tâches « une fois ») dès la création, puis
# consigne leurs identifiants ici ; chacun inventorie, arrête par identifiant (R10) et consigne dans registres/arrets.md
printf 'reveils_de_garde %s %s (création + 135 min et + 150 min : à programmer par la session, identifiants à consigner ici)\n' \
    "$((CREATION + 8100))" "$((CREATION + 9000))" >> "$T/lancement.txt"
GO_ID=$GO "$V" create instance "$OFFRE" --raw --image python:3.11-bookworm --disk 80 --cancel-unavail \
    --label "$ETIQUETTE" \
    --env "-e COMMIT=$S -e BRANCHE=$BRANCHE -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" \
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
echo "créée ; surveillance par la session ; arrêt par identifiant (R10) à la fin de l'amorce, au plus tard $(date -u -d "@$((CREATION + 8400))" +%FT%TZ)"
echo "réveils de garde à programmer maintenant par la session : $(date -u -d "@$((CREATION + 8100))" +%FT%TZ) et $(date -u -d "@$((CREATION + 9000))" +%FT%TZ) (création + 135 et + 150 min) ; identifiants dans $T/lancement.txt"
exit 0
