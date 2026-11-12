#!/usr/bin/env bash
# Chaîne de session de T0.6, v1 (nom neuf, R12) : SANS COUPERET DE TEMPS (GO-2026-11-02-28), arrêt sur processus mort ou
# sur dépense, GO vérifié (GO-2026-11-02-28 seulement, `controle_ia.t06.session go`), minuterie de destruction posée par
# l'amorce (échéance passée à la création, au plus la fin du 16 novembre 2026). Déclinée du lanceur de P3
# (`docs/procedures/P3-premier-test-v2/lancer_p3_v1.sh`) et du lanceur SPARKS v12 : la session ne loue rien par ce script ;
# il VÉRIFIE, puis IMPRIME la commande littérale de création (`GO_ID=… vastai create instance …`), que
# `.claude/hooks/garde_calcul.py` revérifie à l'exécution (rejouée ici sur la commande imprimée). Aucun jeton n'est affiché.
# Usage :
#   bash scripts/lancer_t06_v1.sh controles DOSSIER_NEUF [JOUR]
#       GO conforme ; commit de scellement S du préenregistrement (ajout de son sceau), poussé sur origin/main ; le texte
#       cite la configuration, les tâches d'évaluation et l'entropie ; configuration, tâches et consignes citées présentes
#       et scellées à S ; amorce de S citée par son empreinte ; place disque ; jetons présents (jamais affichés) ; écrit
#       DOSSIER/lancement.txt. Codes : 0 ; 2 tout échec.
#   bash scripts/lancer_t06_v1.sh creation OFFRE PRIX_CARTE PRIX_STOCKAGE DOSSIER [ECHEANCE_UTC_S]
#       Après `controles` sur DOSSIER : relit S, encode l'amorce de S, vérifie le prix (≤ PRIX_MAX) et le GO, rejoue la garde
#       de calcul sur la commande, puis IMPRIME la commande de création (la session l'exécute elle-même).
#   bash scripts/lancer_t06_v1.sh apres-creation FICHIER CODE DOSSIER
#       Lit la réponse brute de `vastai create` (puis l'efface) : identifiant, heure de création écrite dans DOSSIER.
#   bash scripts/lancer_t06_v1.sh surveillance ID CREATION_S PRIX_CARTE PRIX_STOCKAGE DOSSIER [FACTURE_USD]
#       Boucle (INTERVALLE s, défaut 120) : journal de l'instance masqué, relevé cumulatif des lignes AMORCE et PROGRES,
#       décision par `controle_ia.t06.session surveillance` : POURSUIVRE ; ALERTE (plus de deux heures sans PROGRES :
#       écrite, aucun arrêt) ; ARRET mort ou ARRET depense (≥ 200 USD) : imprime `vastai stop instance ID` (arrêt par
#       l'identifiant, R10) et sort en code 3 ; FIN : imprime la même commande (disque gardé jusqu'au verdict) et sort en
#       code 0 ; REFUS : sort en code 4 (la minuterie détruit).
# Variables : CONTROLE_IA_GITHUB_TOKEN, HF_TOKEN (présence exigée, jamais affichés) ; T06_DEPOT (défaut : dépôt courant) ;
# T06_PREREG (défaut prereg/T0.6-organismes-v0-v1.md) ; T06_BRANCHE (défaut calcul/t06-reel-v1) ; T06_IMAGE ; VAST (outil).
set -uo pipefail
QUOI="${1:?controles, creation, apres-creation ou surveillance}"
DEPOT="${T06_DEPOT:-$(cd "$(dirname "$0")/.." && pwd)}"
P="${T06_PREREG:-prereg/T0.6-organismes-v0-v1.md}"
A=scripts/amorce_instance_t06_v1.sh
BRANCHE="${T06_BRANCHE:-calcul/t06-reel-v1}"
GO_ID=GO-2026-11-02-28
PRIX_MAX=1.30; STOCKAGE_MAX=0.03; TELECHARGEMENT_MAX=0.05; DISQUE_GO=150; ETIQUETTE=t06-v1
IMAGE="${T06_IMAGE:-python:3.11-bookworm}"
FIN_GO=1794873600
VAST="${VAST:-vastai}"
SESSION="import sys; sys.path.insert(0, '$DEPOT/src'); from controle_ia.t06 import session; sys.exit(session.main(sys.argv[1:]))"
masquer() { python3 -c '
import os, sys
t = sys.stdin.read()
for k in ("HF_TOKEN", "CONTROLE_IA_GITHUB_TOKEN", "GH_TOKEN", "VAST_API_KEY"):
    v = os.environ.get(k)
    if v and len(v) > 6:
        t = t.replace(v, "***")
sys.stdout.write(t)'; }
commit_s() { git -C "$DEPOT" log --diff-filter=A -1 --format=%H -- "$P.sha256"; }
case "$QUOI" in
controles)
    D=$(realpath -m "${2:?dossier neuf}"); JOUR="${3:-$(date -u +%F)}"
    [ -e "$D" ] && { echo "$D existe déjà (R12)"; exit 2; }
    mkdir -p "$D"
    python3 -I -B -c "$SESSION" go "$DEPOT/registres/go.md" "$JOUR" | tee -a "$D/lancement.txt" || { echo "GO : pas de création"; exit 2; }
    LIBRE=$(df -Pk "$D" | awk 'NR==2 {print $4}'); [ "$LIBRE" -ge 3000000 ] || { echo "place disque : $LIBRE ko libres (3 Go exigés)"; exit 2; }
    S=$(commit_s); [[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "commit de scellement de $P introuvable"; exit 2; }
    timeout 300 git -C "$DEPOT" fetch -q origin main || { echo "fetch impossible"; exit 2; }
    git -C "$DEPOT" merge-base --is-ancestor "$S" origin/main || { echo "commit de scellement $S absent de origin/main"; exit 2; }
    git -C "$DEPOT" show "$S:$P" > "$D/prereg-S.md" || { echo "préenregistrement absent de S"; exit 2; }
    for motif in "Entropie : \`[0-9]+\`" "Configuration de T0.6 \(empreinte canonique\) : \`[0-9a-f]{64}\`" "Tâches d'évaluation de T0.6 : \`[0-9a-f]{64}\`" \
                 "Tests attendus : \`[0-9]+\`" "Chemin de la configuration de T0.6 : \`[^\`]+\`" "Chemin des tâches d'évaluation de T0.6 : \`[^\`]+\`" \
                 "Chemin des tâches de distillation de T0.6 : \`[^\`]+\`" "Chemin des consignes de P3 : \`[^\`]+\`"; do
        n=$(grep -cE "$motif" "$D/prereg-S.md" || true); [ "$n" = 1 ] || { echo "citation « ${motif%% :*} » absente ou en double dans le texte de S ($n)"; exit 2; }
    done
    for cle in "Chemin de la configuration de T0.6" "Chemin des tâches d'évaluation de T0.6" "Chemin des tâches de distillation de T0.6" "Chemin des consignes de P3"; do
        f=$(sed -n "s/.*$cle : \`\\([^\`]*\\)\`.*/\\1/p" "$D/prereg-S.md")
        git -C "$DEPOT" cat-file -e "$S:$f" 2>/dev/null && git -C "$DEPOT" cat-file -e "$S:$f.sha256" 2>/dev/null || { echo "fichier cité $f ou son sceau absent de S"; exit 2; }
        [ "$(git -C "$DEPOT" show "$S:$f" | sha256sum | cut -d' ' -f1)" = "$(git -C "$DEPOT" show "$S:$f.sha256" | cut -d' ' -f1)" ] || { echo "sceau de $f non conforme à S"; exit 2; }
    done
    git -C "$DEPOT" show "$S:$A" > "$D/amorce.sh" || { echo "amorce absente de S"; exit 2; }
    E=$(sha256sum "$D/amorce.sh" | cut -d' ' -f1)
    tr '\n' ' ' < "$D/prereg-S.md" | tr -s ' ' | grep -qF "\`$A\` (\`$E\`" || { echo "empreinte de l'amorce ($E) non citée par le texte de S"; exit 2; }
    [ -n "${HF_TOKEN:-}" ] && [ -n "${CONTROLE_IA_GITHUB_TOKEN:-}" ] || { echo "jeton absent (HF_TOKEN ou CONTROLE_IA_GITHUB_TOKEN) : pas de création"; exit 2; }
    printf 'controles t06 v1 %s\ncommit %s\nprereg %s\nbranche %s\namorce %s\ngo %s\n' "$(date -u +%FT%TZ)" "$S" "$P" "$BRANCHE" "$E" "$GO_ID" >> "$D/lancement.txt"
    echo "CONTRÔLES CONFORMES : S=$S ; amorce $E ; GO $GO_ID" ;;
creation)
    OFFRE="${2:?offre}"; PC="${3:?prix carte}"; PS="${4:?prix stockage}"; D=$(realpath -m "${5:?dossier des contrôles}"); ECH="${6:-$FIN_GO}"
    [[ "$OFFRE" =~ ^[0-9]+$ ]] || { echo "offre : chiffres seuls"; exit 2; }
    [ -f "$D/lancement.txt" ] && grep -q '^commit ' "$D/lancement.txt" || { echo "contrôles absents ($D/lancement.txt) : pas de création"; exit 2; }
    S=$(sed -n 's/^commit //p' "$D/lancement.txt" | tail -1); [[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "commit illisible"; exit 2; }
    [ "$S" = "$(commit_s)" ] || { echo "commit de scellement changé depuis les contrôles"; exit 2; }
    python3 -c 'import sys; p=float(sys.argv[1]); s=float(sys.argv[2]); sys.exit(0 if 0 < p <= float(sys.argv[3]) and 0 <= s <= float(sys.argv[4]) else 1)' "$PC" "$PS" "$PRIX_MAX" "$STOCKAGE_MAX" \
        || { echo "prix $PC USD/h ou stockage $PS USD/h hors des bornes du texte ($PRIX_MAX, $STOCKAGE_MAX) : nœud, pas de création"; exit 3; }
    [[ "$ECH" =~ ^[0-9]+$ ]] && [ "$ECH" -le "$FIN_GO" ] && [ "$ECH" -gt "$(date +%s)" ] || { echo "échéance $ECH hors de ]maintenant, fin du GO]"; exit 2; }
    python3 -I -B -c "$SESSION" go "$DEPOT/registres/go.md" >/dev/null || { echo "GO non conforme au jour de la création"; exit 2; }
    [ -n "${HF_TOKEN:-}" ] && [ -n "${CONTROLE_IA_GITHUB_TOKEN:-}" ] || { echo "jeton absent : pas de création"; exit 2; }
    B64=$(base64 -w0 < "$D/amorce.sh")
    [ "$(printf %s "$B64" | base64 -d | sha256sum | cut -d' ' -f1)" = "$(sed -n 's/^amorce //p' "$D/lancement.txt" | tail -1)" ] || { echo "encodage de l'amorce"; exit 2; }
    CMD="GO_ID=$GO_ID timeout -k 10 300 $VAST create instance $OFFRE --raw --image $IMAGE --disk $DISQUE_GO --cancel-unavail --label $ETIQUETTE --env \"-e COMMIT=$S -e PREREG=$P -e BRANCHE=$BRANCHE -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e ECHEANCE_UTC_S=$ECH -e HF_TOKEN=\$HF_TOKEN -e GH_TOKEN=\$CONTROLE_IA_GITHUB_TOKEN\" --entrypoint bash --args -c \"echo $B64 | base64 -d > /root/amorce.sh && bash /root/amorce.sh\" > \"$D/creation-brute.json\" 2>&1; bash $DEPOT/scripts/lancer_t06_v1.sh apres-creation \"$D/creation-brute.json\" \$? \"$D\""
    printf '{"tool_input":{"command":%s}}' "$(python3 -c 'import json, sys; print(json.dumps(sys.argv[1]))' "$CMD")" | python3 "$DEPOT/.claude/hooks/garde_calcul.py" || { echo "garde de calcul : commande refusée"; exit 2; }
    printf 'creation preparee %s offre %s prix %s stockage %s echeance %s\n' "$(date -u +%FT%TZ)" "$OFFRE" "$PC" "$PS" "$ECH" >> "$D/lancement.txt"
    echo "COMMANDE DE CRÉATION (à exécuter par la session, jetons par leur nom seulement) :"
    echo "$CMD" ;;
apres-creation)
    F="${2:?fichier}"; C="${3:?code}"; D="${4:?dossier}"
    ID=$(grep -oE "new_contract['\"]?[[:space:]]*:[[:space:]]*[0-9]+" "$F" 2>/dev/null | grep -oE '[0-9]+$' | head -1 || true)
    OK=$(grep -cE "success['\"]?[[:space:]]*:[[:space:]]*(True|true)" "$F" 2>/dev/null || true)
    rm -f -- "$F"
    if [ "$C" = 0 ] && [ -n "$ID" ] && [ "${OK:-0}" -ge 1 ]; then
        CR=$(date +%s); printf 'instance %s\ncreation %s\n' "$ID" "$CR" >> "$D/lancement.txt"
        echo "CRÉÉE : instance $ID (création $CR ; sortie de vastai non affichée) ; surveillance : bash scripts/lancer_t06_v1.sh surveillance $ID $CR <PRIX_CARTE> <PRIX_STOCKAGE> $D"; exit 0
    fi
    echo "CRÉATION INCERTAINE (code $C, identifiant « ${ID:-aucun} ») : vérifier « vastai show instances » sans --raw ; aucune seconde création avant"; exit 4 ;;
surveillance)
    ID="${2:?identifiant}"; CR="${3:?création}"; PC="${4:?prix carte}"; PS="${5:?prix stockage}"; D="${6:?dossier}"; FACT="${7:-}"
    [[ "$ID" =~ ^[0-9]+$ && "$CR" =~ ^[0-9]+$ ]] || { echo "identifiant et création : chiffres seuls (R10)"; exit 2; }
    [ "${#HF_TOKEN}" -ge 8 ] && [ "${#CONTROLE_IA_GITHUB_TOKEN}" -ge 8 ] 2>/dev/null || { echo "jetons absents ou trop courts : masquage impossible, surveillance refusée"; exit 2; }
    command -v "$VAST" >/dev/null || { echo "outil de location introuvable : surveillance aveugle, arrêt"; exit 2; }
    mkdir -p "$D"; : >> "$D/progres.txt"
    INTERVALLE="${INTERVALLE:-120}"
    echo "surveillance de $ID : création $CR, sans couperet de temps ; arrêt sur processus mort ou dépense ≥ 200 USD ; alerte après 2 h sans PROGRES" >> "$D/surveillance.txt"
    while true; do
        now=$(date -u +%s)
        if timeout -k 5 120 "$VAST" logs "$ID" --tail 20000 > "$D/journal-tour.txt" 2>&1; then
            masquer < "$D/journal-tour.txt" > "$D/journal-dernier.txt"
            grep -E '^(AMORCE|PROGRES) ' "$D/journal-dernier.txt" | while IFS= read -r ligne; do grep -qxF -- "$ligne" "$D/progres.txt" || printf '%s\n' "$ligne" >> "$D/progres.txt"; done
        else
            echo "$(date -u +%FT%TZ) journal illisible (appel en échec) : dernier relevé gardé" >> "$D/surveillance.txt"
        fi
        rm -f "$D/journal-tour.txt"
        DEC=$(python3 -I -B -c "$SESSION" surveillance "$D/progres.txt" "$now" "$PC" "$PS" "$CR" ${FACT:+"$FACT"} 2>&1) || { echo "$(date -u +%FT%TZ) garde de dépense illisible : $DEC" >> "$D/surveillance.txt"; DEC="POURSUIVRE"; }
        echo "$(date -u +%FT%TZ) $DEC" >> "$D/surveillance.txt"
        case "$DEC" in
            ARRET*) echo "$DEC"; echo "ARRÊT PAR L'IDENTIFIANT (R10) : timeout -k 5 120 $VAST stop instance $ID"; exit 3 ;;
            FIN*) echo "$DEC"; echo "FIN : instance à arrêter par son identifiant, disque gardé jusqu'au verdict : timeout -k 5 120 $VAST stop instance $ID"; exit 0 ;;
            REFUS*) echo "$DEC"; exit 4 ;;
            ALERTE*) echo "$(date -u +%FT%TZ) $DEC" ;;
        esac
        sleep "$INTERVALLE"
    done ;;
*) echo "usage : controles | creation | apres-creation | surveillance" >&2; exit 2 ;;
esac
