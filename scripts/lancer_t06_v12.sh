#!/usr/bin/env bash
# [v12 (GO-2026-11-08-01, contre-lecture de la v11 v2) : copie du lanceur v11 qui cite l'amorce v10 (bras B v4, liste figée v2) et valide `T06_TESTS_ATTENDUS` (^[0-9]*$ : sans cela une valeur comme « 7 -e PYTEST_ADDOPTS=… » s'insérerait dans la commande de création) ; rien d'autre ne change]
# [v11 (R-1746, contre-lecture de la v11) : le module de session est session_v11.py ; les épreuves se jouent sous GO-2026-11-06-01 (E2, E3 ; total 5 USD) ou GO-2026-11-07-08 (E3 bis ; total 8 USD, dépense antérieure ≥ 2,092 USD exigée), les deux lignes vérifiées au registre ; T06_TESTS_ARGS est refusé hors du mode jouet ; plus de variable T06_GO_EPREUVES_TOTAL_USD]
# [v11 (E3 du 7 novembre) : copie du lanceur v10 qui cite l'amorce v10 (suite ciblée et figée, liste scripts/tests-cibles-t06-v1.txt) ; rien d'autre ne change]
# Chaîne de session de T0.6, v10 (nom neuf, R12 ; les v1 à v9 restent telles quelles). v10 = v9 + (contre-lecture Opus de la v9, « Essais R5 à ajouter » 3) : le module de session est `session_v9.py` (`instance_seule` : « 404 » exact et message exact ; `{"id": null}` non concluant) ; le code et le motif du refus de plafond ne changent pas (code 2). Texte de la v9 (conservé) :
# [v10, intégration de la course : cite l amorce v8 (bras B en annexe), session_v9] Chaîne de session de T0.6, v9 (nom neuf, R12 ; les v1 à v8 restent telles quelles). v9 = v8 + (R-1692, épreuve E2 du 7 novembre) : le stockage n'est plus compté deux fois (`dph_total` inclut déjà `storage_total_cost` sous `--storage` : prix_carte = dph_total − storage_total_cost, module `session_v9.py`) ; l'amorce citée est `scripts/amorce_instance_t06_v7.sh` (correctif R-1689 : l'ordre de destruction de l'amorce l'emporte sur l'arrêt par dépense épuisée). Texte de la v8 (conservé) :
# Chaîne de session de T0.6, v8 (nom neuf, R12 ; les v1 à v7 restent telles quelles). v8 = v7 + (R-1683, contre-lecture Opus de la v7) : (1) une liste d'inventaire
# VIDE (ou `null`, illisible, ou un appel en échec) n'est pas une absence : ALERTE sur la sortie standard avec un compteur, puis `vastai show instance <ID>` (l'instance
# seule) ; `ARRET mort` seulement si une liste NON vide ne contient pas l'instance à deux relevés, ou si l'instance seule est introuvable à deux relevés ; présence non
# établie trois relevés de suite : `ARRET inventaire` ; (2) `vastai logs --tail 20000` (journal entier, comme la v6) ; (3) masquage PAR UN TUBE, aucun fichier brut
# (journal, inventaire et réponse de `show instance` masqués avant d'être écrits) ; toute clé présente (HF_TOKEN, CONTROLE_IA_GITHUB_TOKEN, GH_TOKEN, VAST_API_KEY) de moins
# de 8 caractères refuse la surveillance ; l'amorce citée est `scripts/amorce_instance_t06_v6.sh`. Texte de la v7 (conservé) : chaîne de session de T0.6, v7. v7 = v6 + (R-1677, défaut de chaîne d'E2) : (1) l'amorce citée
# est `scripts/amorce_instance_t06_v5.sh` (clonage réduit, débit journalisé, `refus` qui attend 180 s) ; (2) `surveillance` imprime `ARRET mort` quand
# l'instance n'est plus dans l'inventaire (deux relevés à 15 s d'écart) et recopie à chaque relevé le journal entier (`logs --tail 2000`, valeurs de
# clés masquées) dans `journal-instance.txt` (écrasé seulement par un journal qui porte des lignes AMORCE) ; (3) le filtre de création porte aussi
# `inet_down>=500` (module `session_v7.py`). Texte de la v6 (conservé) : chaîne de session de T0.6, v6 (nom neuf, R12 ; les v1 à v5 restent telles quelles). v6 = v5 + `reliability>=0.98` dans le filtre de la recherche
# de création (R-1660 : la création filtre exactement comme la lecture E2-1 des ordres d'épreuve), rien d'autre. Texte de la v5 :
# Chaîne de session de T0.6, v5 (contre-lecture du lanceur v4, R-1657) :
# C-V5-1 : `creation` ne relit plus l'offre par son identifiant (`search offers "id=<OFFRE>"` rend une liste VIDE sous vastai 1.8.3 et
# l'identifiant d'une même offre change d'une recherche à l'autre : R-577, R-578, confirmé en réel le 7 novembre) ; le premier argument
# est « auto » : recherche filtrée (`search offers '<filtre de la configuration>' -o dph_total --storage <disque> --raw`), première
# offre de la liste qui respecte les bornes (carte, mémoire, disque, prix de la carte, du stockage et du téléchargement), prix lus
# DANS LA LISTE, commande de création imprimée pour cet identifiant ; si la création échoue (offre retirée), `apres-creation`
# vérifie qu'aucune instance du programme n'existe, note la machine refusée et demande de relancer `creation auto …` (rang
# suivant) ; au plus trois essais, puis arrêt. C-V5-2 : `HF_TOKEN` n'est exigé par `surveillance` qu'en mode réel. C-V5-3 : le
# texte de la surveillance nomme le plafond de la configuration. L'amorce reste `scripts/amorce_instance_t06_v4.sh`. Texte de la v4
# (conservé) : chaîne de session de T0.6, v4 (nom neuf, R12 ; les v1 à v3 restent telles quelles). Contre-lecture du lanceur v3 : mêmes
# sous-commandes, mêmes arguments et mêmes codes que la v3 ; changent le nom du script (`_v4`), l'amorce citée par son empreinte
# dans le texte de S (`scripts/amorce_instance_t06_v4.sh`, C-V4-1), la branche par défaut (`calcul/t06-reel-v4`) et le lanceur joué
# (`controle_ia.t06.lanceur_v4`, C-V4-2). Texte de la v3 (conservé) : chaîne de session de T0.6, v3. Contre-lecture neuve du lanceur v2,
# C-V3-3 : l'offre est relue par `vastai search offers "id=<OFFRE>" --storage <offre.disque_min_go> --raw`, pour que `dph_total`
# et `storage_total_cost` soient lus au disque demandé (150 Go) ; amorce v4 citée ; branche par défaut `calcul/t06-reel-v4`.
# Mêmes sous-commandes et mêmes arguments que la v2. Inchangé de la v2 (contre-lecture du lanceur v1) :
# C08 (dépense cumulée sur toutes les tentatives : argument « dépense antérieure » relevée au registre des dépenses, forfait
# de téléchargement lu dans l'offre ; heure d'épuisement des 200 USD calculée à la création et passée à l'amorce),
# C09 (garde de dépense illisible : ALERTE, et arrêt imprimé après trois échecs de suite), C12 (offre relue par
# `vastai search offers "id=<OFFRE>" --raw` et vérifiée par `session_v2 offre` : carte, mémoire de carte, une seule carte,
# mémoire vive, cœurs effectifs, disque, prix de la carte, du stockage et du téléchargement ; prix jamais donnés à la main ;
# `vastai show instances --raw` sans instance du programme), C15 (prix maximal par carte lu dans la configuration, argument
# `carte` : course ou relance), L11 (fin du GO et dernier jour de création lus dans la configuration, vérifiés contre le
# registre des GO par `session_v2 calendrier` ; rien en dur). Inchangé de la v1 : SANS COUPERET DE TEMPS ; la session ne
# loue rien par ce script, il VÉRIFIE puis IMPRIME la commande littérale de création, revérifiée par la garde de calcul.
# Usage :
#   bash scripts/lancer_t06_v12.sh controles DOSSIER_NEUF [JOUR]
#       GO conforme ; commit de scellement S du préenregistrement, poussé sur origin/main ; huit citations du texte de S ;
#       configuration, tâches et consignes citées présentes et scellées à S ; configuration de S copiée dans DOSSIER ;
#       calendrier de la configuration conforme au registre (L11) ; amorce v4 de S citée par son empreinte ; place disque ;
#       jetons présents (jamais affichés) ; écrit DOSSIER/lancement.txt. Codes : 0 ; 2 tout échec.
#   bash scripts/lancer_t06_v12.sh creation auto CARTE DEPENSE_ANTERIEURE_USD DOSSIER [ECHEANCE_UTC_S]   (v5 : « auto » remplace l'identifiant d'offre)
#       CARTE = course | relance (DT-6). Après `controles` : relit S, relit l'offre et l'inventaire des instances par
#       l'outil (C12), vérifie le GO et le calendrier au jour de la création, calcule l'heure d'épuisement de la dépense
#       (C08), rejoue la garde de calcul, puis IMPRIME la commande de création. Codes : 0 ; 2 échec ; 3 nœud (offre hors des
#       bornes, instance présente, dépense déjà épuisée).
#   bash scripts/lancer_t06_v12.sh controles-epreuve DOSSIER_NEUF COMMIT CONFIG_CHEMIN [JOUR]     (C-V4-3, épreuves à blanc E2 et E3)
#       Variables : T06_BRANCHE_CODE (branche `prep/…` du code, dont COMMIT est un ancêtre au sens de `refs/remotes/origin/<branche>`,
#       relevée par un `git fetch origin refs/heads/<branche>:refs/remotes/origin/<branche>` explicite) ; GO-2026-11-06-01 conforme
#       (5 USD) ; configuration d'épreuve lue DANS COMMIT (go_id = GO-2026-11-06-01, plafond 1,5 ou 3,5 USD) ; calendrier au registre ;
#       amorce v4 de COMMIT ; place disque ; jetons ; écrit DOSSIER/lancement.txt (ligne « epreuve oui »). Aucune citation de
#       préenregistrement (une épreuve n'est jamais décisive). Codes : 0 ; 2 tout échec.
#       `creation` lit alors le GO, le plafond, le mode et la configuration dans DOSSIER ; la branche poussée doit commencer par
#       `essai/` (jamais `calcul/`) ; `T06_EPUISEMENT_SIMULE_S` (≥ 60, épreuves seulement) avance l'heure d'épuisement de la dépense
#       pour éprouver le redémarrage après une dépense épuisée ; `T06_TESTS_ATTENDUS` (vide à E3 : la dernière ligne est relevée) ;
#       `T06_TESTS_ARGS` (essais joués par l'amorce, séparés par des virgules, épreuves seulement ; jouet seulement, refusé en mode réel ; vide = la suite ciblée figée de l'amorce v10, jamais la suite complète).
#       Registre des GO : `T06_REGISTRE_GO` = `registres/go.md` d'un clone de `main` (qui fait foi), OBLIGATOIRE pour une épreuve (aux
#       contrôles et à la création) ; le registre du commit cloné doit porter aussi le GO (l'amorce le relit). Sans la variable (course),
#       le registre de l'arbre du script.
#   bash scripts/lancer_t06_v12.sh apres-creation FICHIER CODE DOSSIER
#   bash scripts/lancer_t06_v12.sh surveillance ID DOSSIER [FACTURE_USD]
#       Prix, dépense antérieure, forfait de téléchargement et heure de création relus dans DOSSIER/lancement.txt ; décision
#       par `session_v2 surveillance` : POURSUIVRE ; ALERTE ; ARRET mort ou ARRET depense : imprime `vastai stop instance
#       ID`, code 3 ; FIN : même commande, code 0 ; REFUS : code 4 ; garde illisible : ALERTE, puis ARRET au troisième échec
#       de suite (C09).
# Variables : CONTROLE_IA_GITHUB_TOKEN, HF_TOKEN (présence exigée, jamais affichés) ; T06_DEPOT ; T06_PREREG ; T06_BRANCHE
# (défaut calcul/t06-reel-v4) ; T06_IMAGE ; VAST (outil) ; INTERVALLE.
set -uo pipefail
QUOI="${1:?controles, creation, apres-creation ou surveillance}"
DEPOT="${T06_DEPOT:-$(cd "$(dirname "$0")/.." && pwd)}"
P="${T06_PREREG:-prereg/T0.6-organismes-v0-v1.md}"
A=scripts/amorce_instance_t06_v10.sh
BRANCHE="${T06_BRANCHE:-calcul/t06-reel-v4}"
GO_ID=GO-2026-11-02-28
REG="${T06_REGISTRE_GO:-$DEPOT/registres/go.md}"   # registre des GO lu par toutes les sous-commandes ; pour une épreuve : celui d'un clone de `main` (obligatoire)
GO_EPREUVE=GO-2026-11-06-01          # C-V4-3 : épreuves à blanc E2 et E3 (5 USD cumulés ; aucune donnée décisive)
GO_EPREUVE_BIS=GO-2026-11-07-08      # E3 bis : 3 USD de plus (8 USD pour E2, E3 et E3 bis) ; ligne du registre à 3 USD, échéance 12 novembre
go_epreuve() { case "$1" in "$GO_EPREUVE") echo 5;; "$GO_EPREUVE_BIS") echo 3;; *) return 1;; esac; }   # plafond de la LIGNE du registre du GO d'épreuve
IMAGE="${T06_IMAGE:-python:3.11-bookworm}"
VAST="${VAST:-vastai}"
SESSION="import sys; sys.path.insert(0, '$DEPOT/src'); from controle_ia.t06 import session_v2; sys.exit(session_v2.main(sys.argv[1:]))"
SESSION3="import sys; sys.path.insert(0, '$DEPOT/src'); from controle_ia.t06 import session_v3; sys.exit(session_v3.main(sys.argv[1:]))"
SESSION7="import sys; sys.path.insert(0, '$DEPOT/src'); from controle_ia.t06 import session_v11; sys.exit(session_v11.main(sys.argv[1:]))"
masquer() { python3 -c '
import os, sys
t = sys.stdin.read()
for k in ("HF_TOKEN", "CONTROLE_IA_GITHUB_TOKEN", "GH_TOKEN", "VAST_API_KEY"):
    v = os.environ.get(k)
    if v and len(v) >= 8:
        t = t.replace(v, "***")
sys.stdout.write(t)'; }
# R-1693 : sortie de vastai masquée PAR UN TUBE, avec lecture de TOUT le PIPESTATUS. $1 = fichier de sortie ; le reste = la commande. Code rendu : celui de la
# commande ; 121 si le masquage a échoué (aucun fichier écrit, l'ancien reste) ; stderr jeté (il n'est pas masqué).
vast_masque() {
    local sortie="$1"; shift
    "$@" 2>/dev/null | masquer > "$sortie.tmp"
    local ps=("${PIPESTATUS[@]}")
    if [ "${ps[1]:-1}" != 0 ]; then rm -f "$sortie.tmp"; return 121; fi
    mv -f "$sortie.tmp" "$sortie"; return "${ps[0]}"
}
commit_s() { git -C "$DEPOT" log --diff-filter=A -1 --format=%H -- "$P.sha256"; }
champ() { sed -n "s/^$1 //p" "$2" | tail -1; }           # dernière valeur d'un champ de lancement.txt
cle_config() { python3 -I -B -c 'import json, sys; c = json.load(open(sys.argv[1], encoding="utf-8"))
for k in sys.argv[2].split("."):
    c = c[k]
print(c)' "$1" "$2"; }
case "$QUOI" in
controles)
    D=$(realpath -m "${2:?dossier neuf}"); JOUR="${3:-$(date -u +%F)}"
    [ -e "$D" ] && { echo "$D existe déjà (R12)"; exit 2; }
    mkdir -p "$D"
    python3 -I -B -c "$SESSION" go "$REG" "$JOUR" | tee -a "$D/lancement.txt" || { echo "GO : pas de création"; exit 2; }
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
        [ "$cle" = "Chemin de la configuration de T0.6" ] && { git -C "$DEPOT" show "$S:$f" > "$D/config.json"; CONFIG_CHEMIN="$f"; }
    done
    CAL=$(python3 -I -B -c "$SESSION" calendrier "$D/config.json" "$REG" "$JOUR") || { echo "calendrier de la configuration (L11) : $CAL : pas de création"; exit 2; }
    git -C "$DEPOT" show "$S:$A" > "$D/amorce.sh" || { echo "amorce v10 absente de S"; exit 2; }
    E=$(sha256sum "$D/amorce.sh" | cut -d' ' -f1)
    tr '\n' ' ' < "$D/prereg-S.md" | tr -s ' ' | grep -qF "\`$A\` (\`$E\`" || { echo "empreinte de l'amorce v10 ($E) non citée par le texte de S"; exit 2; }
    [ -n "${HF_TOKEN:-}" ] && [ -n "${CONTROLE_IA_GITHUB_TOKEN:-}" ] || { echo "jeton absent (HF_TOKEN ou CONTROLE_IA_GITHUB_TOKEN) : pas de création"; exit 2; }
    printf 'controles t06 v12 %s\ncommit %s\nprereg %s\nconfig %s\nbranche %s\namorce %s\ngo %s\ncalendrier %s\n' "$(date -u +%FT%TZ)" "$S" "$P" "$CONFIG_CHEMIN" "$BRANCHE" "$E" "$GO_ID" "$CAL" >> "$D/lancement.txt"
    echo "CONTRÔLES CONFORMES : S=$S ; amorce v10 $E ; GO $GO_ID ; $CAL" ;;
controles-epreuve)
    D=$(realpath -m "${2:?dossier neuf}"); S="${3:?commit à cloner (40 caractères)}"; CFG="${4:?chemin de la configuration de l epreuve dans le commit}"; JOUR="${5:-$(date -u +%F)}"
    [ -e "$D" ] && { echo "$D existe déjà (R12)"; exit 2; }
    [[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "commit : 40 caractères hexadécimaux"; exit 2; }
    BC="${T06_BRANCHE_CODE:?T06_BRANCHE_CODE : branche prep/… du code}"
    [ -n "${T06_REGISTRE_GO:-}" ] && [ -f "$T06_REGISTRE_GO" ] || { echo "T06_REGISTRE_GO : registres/go.md d'un clone de main exigé pour une épreuve (le registre du commit du code peut être antérieur au GO)"; exit 2; }
    case "$BC" in prep/*) ;; *) echo "T06_BRANCHE_CODE doit commencer par prep/ ($BC)"; exit 2;; esac
    mkdir -p "$D"
    git -C "$DEPOT" cat-file -e "$S^{commit}" 2>/dev/null || { echo "commit $S absent du dépôt local (git fetch origin refs/heads/$BC:refs/remotes/origin/$BC d'abord)"; exit 2; }
    git -C "$DEPOT" merge-base --is-ancestor "$S" "refs/remotes/origin/$BC" 2>/dev/null || { echo "commit $S absent de refs/remotes/origin/$BC (fetch par refspec explicite d'abord)"; exit 2; }
    git -C "$DEPOT" show "$S:$CFG" > "$D/config.json" 2>/dev/null || { echo "configuration $CFG absente du commit $S"; exit 2; }
    GOC=$(cle_config "$D/config.json" go_id) && PLC=$(cle_config "$D/config.json" plafond_usd) && MODE_C=$(cle_config "$D/config.json" mode) || { echo "go_id, plafond_usd ou mode illisibles"; exit 2; }
    PGL=$(go_epreuve "$GOC") || { echo "go_id de la configuration ($GOC) ≠ $GO_EPREUVE et ≠ $GO_EPREUVE_BIS : cette sous-commande ne sert que les épreuves à blanc"; exit 2; }
    # R-1696 : plafond d'épreuve lu dans la configuration, borné par le reste du GO (plus de liste fermée) ; dépense réelle et finale des autres épreuves donnée explicitement
    ANT_EPR="${T06_DEPENSE_EPREUVES_ANTERIEURES_USD:-}"; [[ "$ANT_EPR" =~ ^[0-9]+([.][0-9]+)?$ ]] || { echo "T06_DEPENSE_EPREUVES_ANTERIEURES_USD : dépense réelle et finale des autres épreuves du GO, en USD (0 pour la première), exigée"; exit 2; }
    PLAF=$(python3 -I -B -c "$SESSION7" plafond "$PLC" "$ANT_EPR" "$GOC") || { echo "plafond_usd $PLC refusé : $PLAF"; exit 2; }
    case "$MODE_C" in jouet|reel) ;; *) echo "mode $MODE_C illisible"; exit 2;; esac
    python3 -I -B -c "$SESSION3" go "$REG" "$GOC" "$PGL" "$JOUR" | tee -a "$D/lancement.txt" || { echo "GO : pas de création"; exit 2; }
    # E3 bis : le total de 8 USD est LIÉ aux deux lignes du registre (GO-2026-11-06-01 à 5 USD et GO-2026-11-07-08 à 3 USD), vérifiées toutes deux
    [ "$GOC" != "$GO_EPREUVE_BIS" ] || python3 -I -B -c "$SESSION3" go "$REG" "$GO_EPREUVE" 5 "$JOUR" | tee -a "$D/lancement.txt" || { echo "GO $GO_EPREUVE (5 premiers USD) absent ou non conforme au registre : pas de création"; exit 2; }
    # l'amorce relit le registre DU COMMIT cloné : le GO doit y figurer aussi (sinon elle refuserait sur l'instance)
    git -C "$DEPOT" show "$S:registres/go.md" > "$D/go-commit.md" 2>/dev/null && python3 -I -B -c "$SESSION3" go "$D/go-commit.md" "$GOC" "$PGL" "$JOUR" >/dev/null || { echo "GO $GOC absent ou non conforme dans registres/go.md du commit $S (l'amorce le relit) : commit postérieur au GO exigé"; exit 2; }
    LIBRE=$(df -Pk "$D" | awk 'NR==2 {print $4}'); [ "$LIBRE" -ge 3000000 ] || { echo "place disque : $LIBRE ko libres (3 Go exigés)"; exit 2; }
    CAL=$(python3 -I -B -c "$SESSION3" calendrier "$D/config.json" "$REG" "$GOC" "$PGL" "$JOUR") || { echo "calendrier de la configuration : $CAL : pas de création"; exit 2; }
    git -C "$DEPOT" show "$S:$A" > "$D/amorce.sh" || { echo "amorce v10 absente de $S"; exit 2; }
    E=$(sha256sum "$D/amorce.sh" | cut -d' ' -f1)
    if [ "$MODE_C" = reel ]; then [ -n "${HF_TOKEN:-}" ] || { echo "HF_TOKEN absent (mode réel) : pas de création"; exit 2; }; fi
    [ -n "${CONTROLE_IA_GITHUB_TOKEN:-}" ] || { echo "jeton absent (CONTROLE_IA_GITHUB_TOKEN) : pas de création"; exit 2; }
    printf 'controles-epreuve t06 v4 %s\ncommit %s\nprereg -\nconfig %s\nbranche %s\namorce %s\ngo %s\nplafond %s\nepreuves_anterieures %s\nmode %s\nepreuve oui\ncalendrier %s\n' "$(date -u +%FT%TZ)" "$S" "$CFG" "$BRANCHE" "$E" "$GOC" "$PLC" "$ANT_EPR" "$MODE_C" "$CAL" >> "$D/lancement.txt"
    echo "CONTRÔLES D'ÉPREUVE CONFORMES : S=$S ; amorce v10 $E ; GO $GOC (plafond de l'épreuve $PLC USD sur $([ "$GOC" = "$GO_EPREUVE_BIS" ] && echo 8 || echo 5) ; $PLAF) ; mode $MODE_C ; $CAL" ;;
creation)
    OFFRE_ARG="${2:?auto}"; CARTE="${3:?carte : course ou relance}"; ANT="${4:?dépense antérieure en USD (registre des dépenses ; 0 pour la première tentative)}"; D=$(realpath -m "${5:?dossier des contrôles}"); ECH="${6:-}"
    [ "$OFFRE_ARG" = auto ] || { echo "offre : « auto » seulement (v5 : un identifiant donné à la main serait périmé, il change d'une recherche à l'autre ; l'offre est choisie dans la liste filtrée, juste avant la création)"; exit 2; }
    case "$CARTE" in course|relance) ;; *) echo "carte : course ou relance (DT-6)"; exit 2;; esac
    [[ "$ANT" =~ ^[0-9]+([.][0-9]+)?$ ]] || { echo "dépense antérieure : nombre positif en USD"; exit 2; }
    [ -f "$D/lancement.txt" ] && grep -q '^commit ' "$D/lancement.txt" && [ -f "$D/config.json" ] || { echo "contrôles absents ($D/lancement.txt, config.json) : pas de création"; exit 2; }
    S=$(champ commit "$D/lancement.txt"); [[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "commit illisible"; exit 2; }
    EPR=non; [ "$(champ epreuve "$D/lancement.txt")" = oui ] && EPR=oui
    GOC=$(cle_config "$D/config.json" go_id) && PLC=$(cle_config "$D/config.json" plafond_usd) && MODE_C=$(cle_config "$D/config.json" mode) || { echo "go_id, plafond_usd ou mode illisibles"; exit 2; }
    if [ "$EPR" = oui ]; then
        [ -n "${T06_REGISTRE_GO:-}" ] || { echo "épreuve : T06_REGISTRE_GO (registres/go.md d'un clone de main) exigé"; exit 2; }
        PGL=$(go_epreuve "$GOC") && [ "$(champ go "$D/lancement.txt")" = "$GOC" ] && [ "$(champ plafond "$D/lancement.txt")" = "$PLC" ] || { echo "épreuve : GO ou plafond de la configuration ≠ ceux des contrôles"; exit 2; }
        case "$BRANCHE" in essai/*) ;; *) echo "épreuve : la branche poussée doit commencer par essai/ ($BRANCHE) : jamais calcul/"; exit 2;; esac
        PGO=$PGL
        PLAF=$(python3 -I -B -c "$SESSION7" plafond "$PLC" "$(champ epreuves_anterieures "$D/lancement.txt")" "$GOC") || { echo "épreuve : plafond $PLC hors du reste du GO : $PLAF"; exit 2; }
    else
        [ "$S" = "$(commit_s)" ] || { echo "commit de scellement changé depuis les contrôles"; exit 2; }
        [ "$GOC" = "$GO_ID" ] && [ "$PLC" = 200 ] || { echo "course : GO ($GOC) ou plafond ($PLC) de la configuration ≠ $GO_ID, 200"; exit 2; }
        [ -z "${T06_EPUISEMENT_SIMULE_S:-}" ] || { echo "T06_EPUISEMENT_SIMULE_S : réservé aux épreuves à blanc"; exit 2; }
        PGO=200
    fi
    CAL=$(python3 -I -B -c "$SESSION3" calendrier "$D/config.json" "$REG" "$GOC" "$PGO") || { echo "calendrier (L11) au jour de la création : $CAL : nœud, pas de création"; exit 3; }
    FIN_GO=$(printf '%s\n' "$CAL" | sed -n 's/.*fin_go_utc_s=\([0-9]*\).*/\1/p'); [ -n "$ECH" ] || ECH="$FIN_GO"
    [[ "$ECH" =~ ^[0-9]+$ ]] && [ "$ECH" -le "$FIN_GO" ] && [ "$ECH" -gt "$(date +%s)" ] || { echo "échéance $ECH hors de ]maintenant, fin du GO $FIN_GO]"; exit 2; }
    python3 -I -B -c "$SESSION3" go "$REG" "$GOC" "$PGO" >/dev/null || { echo "GO non conforme au jour de la création"; exit 2; }
    [ "$EPR" != oui ] || [ "$GOC" != "$GO_EPREUVE_BIS" ] || python3 -I -B -c "$SESSION3" go "$REG" "$GO_EPREUVE" 5 >/dev/null || { echo "GO $GO_EPREUVE (5 premiers USD) non conforme au jour de la création de E3 bis"; exit 2; }
    [ -n "${CONTROLE_IA_GITHUB_TOKEN:-}" ] && { [ -n "${HF_TOKEN:-}" ] || [ "$MODE_C" = jouet ]; } || { echo "jeton absent : pas de création"; exit 2; }
    command -v "$VAST" >/dev/null || { echo "outil de location introuvable : offre non relue, pas de création"; exit 2; }
    DISQUE=$(cle_config "$D/config.json" offre.disque_min_go) || { echo "disque illisible"; exit 2; }
    [[ "$DISQUE" =~ ^[0-9]+([.][0-9]+)?$ ]] && [ "${DISQUE%%.*}" -gt 0 ] || { echo "offre.disque_min_go illisible ($DISQUE) : pas de création"; exit 2; }
    # C-V5-1 : au plus trois essais (une machine refusée est exclue du suivant) ; offre choisie DANS LA LISTE FILTRÉE, prix lus dans la liste,
    # au disque demandé (--storage, C-V3-3) ; aucune relecture par identifiant
    ESSAIS=$(grep -c '^essai_creation ' "$D/lancement.txt" || true)
    [ "${ESSAIS:-0}" -lt 3 ] || { echo "trois essais de création déjà faits (essai_creation = $ESSAIS) : arrêt, aucune création ; message à la mère"; exit 3; }
    EXCL=$(sed -n 's/^machine_refusee //p' "$D/lancement.txt" | paste -sd, -)
    FILTRE=$(python3 -I -B -c "$SESSION7" filtre "$D/config.json" "$CARTE") || { echo "filtre illisible : $FILTRE"; exit 2; }
    timeout -k 5 120 "$VAST" search offers "$FILTRE" -o dph_total --storage "$DISQUE" --raw > "$D/offres.json" 2>"$D/offres.err" || { echo "recherche filtrée impossible (--storage $DISQUE) : pas de création"; exit 2; }
    OF=$(python3 -I -B -c "$SESSION7" choisir "$D/offres.json" "$D/config.json" "$CARTE" "$EXCL") || { echo "aucune offre conforme dans la liste filtrée : $OF : nœud, pas de création"; exit 3; }
    OFFRE=$(printf '%s\n' "$OF" | sed -n 's/^id=\([0-9]*\) .*/\1/p'); MACH=$(printf '%s\n' "$OF" | sed -n 's/.* machine=\([^ ]*\) .*/\1/p'); RANG=$(printf '%s\n' "$OF" | sed -n 's/.* rang=\([0-9]*\) .*/\1/p')
    [[ "$OFFRE" =~ ^[0-9]+$ ]] && [ -n "$MACH" ] && [ -n "$RANG" ] || { echo "offre choisie illisible ($OF)"; exit 2; }
    PC=$(printf '%s\n' "$OF" | sed -n 's/.*prix_carte=\([0-9.]*\).*/\1/p'); PS=$(printf '%s\n' "$OF" | sed -n 's/.*prix_stockage=\([0-9.]*\).*/\1/p')
    TEL=$(printf '%s\n' "$OF" | sed -n 's/.*telechargement_forfait=\([0-9.]*\).*/\1/p')
    [ -n "$PC" ] && [ -n "$PS" ] && [ -n "$TEL" ] || { echo "prix illisibles dans la relecture de l'offre"; exit 2; }
    ETIQ=$(cle_config "$D/config.json" offre.etiquette) || { echo "étiquette illisible"; exit 2; }
    vast_masque "$D/instances.json" timeout -k 5 120 "$VAST" show instances --raw || { echo "inventaire des instances impossible ou masquage en échec (code $?) : pas de création"; exit 2; }
    INV=$(python3 -I -B -c "$SESSION" instances "$D/instances.json" "$ETIQ") || { echo "$INV : nœud, pas de création"; exit 3; }
    NOW=$(date +%s)
    DEP=$(python3 -I -B -c "$SESSION3" depense "$PLC" "$PC" "$PS" "$NOW" "$ANT" "$TEL" "$NOW" ${T06_EPUISEMENT_SIMULE_S:+- "$T06_EPUISEMENT_SIMULE_S"}); code_dep=$?
    [ "$code_dep" = 0 ] || { echo "dépense cumulée déjà au plafond ou illisible ($DEP) : nœud, pas de création"; exit 3; }
    EPUIS=$(printf '%s\n' "$DEP" | sed -n 's/.*epuisement_utc_s=\([0-9]*\).*/\1/p'); [[ "$EPUIS" =~ ^[0-9]+$ ]] || { echo "heure d'épuisement illisible"; exit 2; }
    B64=$(base64 -w0 < "$D/amorce.sh")
    [ "$(printf %s "$B64" | base64 -d | sha256sum | cut -d' ' -f1)" = "$(champ amorce "$D/lancement.txt")" ] || { echo "encodage de l'amorce"; exit 2; }
    EXTRA=""
    [[ "${T06_TESTS_ATTENDUS:-}" =~ ^[0-9]*$ ]] || { echo "T06_TESTS_ATTENDUS illisible (^[0-9]*$ exigé : un entier ou rien) : pas de création"; exit 2; }
    [ "$EPR" != oui ] || [ -z "${T06_TESTS_ARGS:-}" ] || [ "$MODE_C" = jouet ] || { echo "T06_TESTS_ARGS refusé en mode $MODE_C : la suite ciblée figée de l'amorce est la seule jouée hors de la répétition jouet"; exit 2; }
    [ "$EPR" = oui ] && EXTRA=" -e EPREUVE_GO_ID=$GOC -e MODE=$MODE_C -e PREREG_ABSENT=1 -e CONFIG=$(champ config "$D/lancement.txt") -e TESTS_ATTENDUS=${T06_TESTS_ATTENDUS:-}${T06_TESTS_ARGS:+ -e TESTS_ARGS=$T06_TESTS_ARGS}"
    CMD="GO_ID=$GOC timeout -k 10 300 $VAST create instance $OFFRE --raw --image $IMAGE --disk $DISQUE --cancel-unavail --label $ETIQ --env \"-e COMMIT=$S -e PREREG=$P -e BRANCHE=$BRANCHE -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e ECHEANCE_UTC_S=$ECH -e FIN_GO_UTC_S=$FIN_GO -e DEPENSE_EPUISEE_UTC_S=$EPUIS -e HF_TOKEN=\$HF_TOKEN -e GH_TOKEN=\$CONTROLE_IA_GITHUB_TOKEN$EXTRA\" --entrypoint bash --args -c \"echo $B64 | base64 -d > /root/amorce.sh && bash /root/amorce.sh\" > \"$D/creation-brute.json\" 2>&1; bash $DEPOT/scripts/lancer_t06_v12.sh apres-creation \"$D/creation-brute.json\" \$? \"$D\""
    printf '{"tool_input":{"command":%s}}' "$(python3 -c 'import json, sys; print(json.dumps(sys.argv[1]))' "$CMD")" | python3 "$DEPOT/.claude/hooks/garde_calcul.py" || { echo "garde de calcul : commande refusée"; exit 2; }
    printf 'creation preparee %s\noffre %s\ncarte %s\nstorage %s\nprix_carte %s\nprix_stockage %s\ntelechargement_forfait %s\nanterieure %s\necheance %s\nepuisement %s\ndepense %s\nplafond_creation %s\nessai_creation %s\nmachine_proposee %s\nrang %s\n' "$(date -u +%FT%TZ)" "$OFFRE" "$CARTE" "$DISQUE" "$PC" "$PS" "$TEL" "$ANT" "$ECH" "$EPUIS" "$DEP" "$PLC" "$((ESSAIS + 1))" "$MACH" "$RANG" >> "$D/lancement.txt"
    echo "OFFRE CONFORME : $OF ; $INV ; $DEP"
    echo "COMMANDE DE CRÉATION (à exécuter par la session, jetons par leur nom seulement) :"
    echo "$CMD" ;;
apres-creation)
    F="${2:?fichier}"; C="${3:?code}"; D="${4:?dossier}"
    ID=$(grep -oE "new_contract['\"]?[[:space:]]*:[[:space:]]*[0-9]+" "$F" 2>/dev/null | grep -oE '[0-9]+$' | head -1 || true)
    OK=$(grep -cE "success['\"]?[[:space:]]*:[[:space:]]*(True|true)" "$F" 2>/dev/null || true)
    NON=$(grep -cE "success['\"]?[[:space:]]*:[[:space:]]*(False|false)" "$F" 2>/dev/null || true)
    rm -f -- "$F"
    if [ "$C" = 0 ] && [ -n "$ID" ] && [ "${OK:-0}" -ge 1 ]; then
        CR=$(date +%s); printf 'instance %s\ncreation %s\n' "$ID" "$CR" >> "$D/lancement.txt"
        echo "CRÉÉE : instance $ID (création $CR ; sortie de vastai non affichée) ; surveillance : bash scripts/lancer_t06_v12.sh surveillance $ID $D"; exit 0
    fi
    if [ -z "$ID" ] && [ "${NON:-0}" -ge 1 ] && [ "${OK:-0}" -eq 0 ]; then
        # C-V5-1 : refus explicite (offre retirée) : retenter au rang suivant seulement si aucune instance du programme n'existe
        ETIQ=$(cle_config "$D/config.json" offre.etiquette) || { echo "étiquette illisible"; exit 4; }
        if vast_masque "$D/instances-apres.json" timeout -k 5 120 "$VAST" show instances --raw && python3 -I -B -c "$SESSION" instances "$D/instances-apres.json" "$ETIQ" >/dev/null; then
            printf 'machine_refusee %s\n' "$(champ machine_proposee "$D/lancement.txt")" >> "$D/lancement.txt"
            echo "OFFRE REFUSÉE À LA CRÉATION (retirée ?) : aucune instance du programme ; machine $(champ machine_proposee "$D/lancement.txt") exclue ; rang suivant : bash $DEPOT/scripts/lancer_t06_v12.sh creation auto $(champ carte "$D/lancement.txt") $(champ anterieure "$D/lancement.txt") $D $(champ echeance "$D/lancement.txt")"; exit 5
        fi
    fi
    echo "CRÉATION INCERTAINE (code $C, identifiant « ${ID:-aucun} ») : vérifier « vastai show instances » sans --raw ; aucune seconde création avant"; exit 4 ;;
surveillance)
    ID="${2:?identifiant}"; D="${3:?dossier}"; FACT="${4:-}"
    [[ "$ID" =~ ^[0-9]+$ ]] || { echo "identifiant : chiffres seuls (R10)"; exit 2; }
    [ -f "$D/lancement.txt" ] || { echo "dossier sans lancement.txt"; exit 2; }
    [ "$(champ instance "$D/lancement.txt")" = "$ID" ] || { echo "identifiant $ID ≠ instance créée d'après $D/lancement.txt (R10)"; exit 2; }
    CR=$(champ creation "$D/lancement.txt"); PC=$(champ prix_carte "$D/lancement.txt"); PS=$(champ prix_stockage "$D/lancement.txt")
    TEL=$(champ telechargement_forfait "$D/lancement.txt"); ANT=$(champ anterieure "$D/lancement.txt")
    PLC=$(champ plafond_creation "$D/lancement.txt"); [ -n "$PLC" ] || PLC=200               # C-V4-3 : plafond de la configuration (200 pour la course)
    [[ "$CR" =~ ^[0-9]+$ ]] && [ -n "$PC" ] && [ -n "$PS" ] && [ -n "$TEL" ] && [ -n "$ANT" ] || { echo "création, prix ou dépense antérieure illisibles dans lancement.txt"; exit 2; }
    # C-V5-2 : HF_TOKEN n'est exigé (masquage) qu'en mode réel ; une épreuve en mode jouet n'en a pas besoin
    JGH="${CONTROLE_IA_GITHUB_TOKEN:-}"      # R-1693 : sous `set -u`, `${#VAR}` d'une variable absente sortait en 127 au lieu de 2
    [ "${#JGH}" -ge 8 ] || { echo "jeton GitHub absent ou trop court : masquage impossible, surveillance refusée"; exit 2; }
    HF_L="${HF_TOKEN:-}"
    [ "$(champ mode "$D/lancement.txt")" = jouet ] || [ "${#HF_L}" -ge 8 ] || { echo "HF_TOKEN absent ou trop court (mode réel) : masquage impossible, surveillance refusée"; exit 2; }
    for K in HF_TOKEN CONTROLE_IA_GITHUB_TOKEN GH_TOKEN VAST_API_KEY; do          # R-1683 : une clé présente mais trop courte ne serait pas masquée
        V="${!K:-}"; { [ -z "$V" ] || [ "${#V}" -ge 8 ]; } || { echo "$K présente mais de moins de 8 caractères : masquage impossible, surveillance refusée"; exit 2; }
    done
    command -v "$VAST" >/dev/null || { echo "outil de location introuvable : surveillance aveugle, arrêt"; exit 2; }
    : >> "$D/progres.txt"
    INTERVALLE="${INTERVALLE:-120}"; ILLISIBLES=0; NONET=0
    alerte() { local m; m="$(date -u +%FT%TZ) $1"; echo "$m" >> "$D/surveillance.txt"; echo "$m"; }
    liste_presente() {   # LP : 0 présente, 1 absente d'une liste non vide, 3 liste vide, 2 illisible, 9 appel en échec
        timeout -k 5 120 "$VAST" show instances --raw 2>/dev/null | masquer > "$D/inventaire-tour.tmp"
        local ps=("${PIPESTATUS[@]}") st sm; st="${ps[0]}"; sm="${ps[1]:-1}"                          # R-1693 : tout le PIPESTATUS ; un échec du masquage n'est jamais lu comme une liste
        if [ "$sm" != 0 ]; then rm -f "$D/inventaire-tour.tmp"; LP=9; echo "masquage de l'inventaire en échec (code $sm) : relevé écarté, aucune copie vidée" > "$D/presence.txt"; alerte "ALERTE masquage en échec (inventaire, code $sm) : relevé écarté"; return; fi
        mv -f "$D/inventaire-tour.tmp" "$D/inventaire-tour.json"          # écriture atomique : jamais de fichier à demi écrit
        [ "$st" = 0 ] || { LP=9; : > "$D/presence.txt"; return; }
        python3 -I -B -c "$SESSION7" presente "$D/inventaire-tour.json" "$ID" > "$D/presence.txt" 2>&1; LP=$?
    }
    seule_presente() {   # SP : 0 répond, 4 introuvable, 2 illisible, 9 appel en échec sans texte d'introuvable
        timeout -k 5 120 "$VAST" show instance "$ID" --raw 2>&1 | masquer > "$D/instance-seule.tmp"
        local ps=("${PIPESTATUS[@]}") st sm; st="${ps[0]}"; sm="${ps[1]:-1}"
        if [ "$sm" != 0 ]; then rm -f "$D/instance-seule.tmp"; SP=9; echo "masquage de la réponse de show instance en échec (code $sm) : relevé écarté" > "$D/presence-seule.txt"; alerte "ALERTE masquage en échec (show instance, code $sm) : relevé écarté"; return; fi
        mv -f "$D/instance-seule.tmp" "$D/instance-seule.json"
        python3 -I -B -c "$SESSION7" seule "$D/instance-seule.json" "$ID" > "$D/presence-seule.txt" 2>&1; SP=$?
        [ "$SP" != 2 ] || [ "$st" = 0 ] || SP=9
    }
    echo "surveillance v12 de $ID : création $CR, carte $PC USD/h, stockage $PS USD/h, téléchargement $TEL USD, antérieur $ANT USD ; sans couperet de temps ; arrêt sur processus mort ou dépense cumulée ≥ $PLC USD (plafond de la configuration, C-V5-3) ; alerte après 2 h sans PROGRES" >> "$D/surveillance.txt"
    while true; do
        now=$(date -u +%s)
        # R-1683 : journal entier (--tail 20000), masqué PAR UN TUBE (aucun fichier brut sur le disque), copié à chaque relevé
        timeout -k 5 120 "$VAST" logs "$ID" --tail 20000 2>&1 | masquer > "$D/journal-dernier.tmp"; PSJ=("${PIPESTATUS[@]}"); ST="${PSJ[0]}"; SMJ="${PSJ[1]:-1}"
        if [ "$SMJ" != 0 ]; then
            rm -f "$D/journal-dernier.tmp"                       # R-1693 : masquage en échec = relevé écarté, ALERTE, jamais une copie vidée ni brute
            alerte "ALERTE masquage en échec (journal, code $SMJ) : relevé écarté, dernier relevé gardé"
        elif [ "$ST" = 0 ]; then
            mv -f "$D/journal-dernier.tmp" "$D/journal-dernier.txt"
            grep -q '^AMORCE ' "$D/journal-dernier.txt" && cp -f "$D/journal-dernier.txt" "$D/journal-instance.txt"      # copie entière à chaque relevé, la dernière bonne survit à la disparition de l'instance
            grep -E '^(AMORCE|PROGRES) ' "$D/journal-dernier.txt" | while IFS= read -r ligne; do grep -qxF -- "$ligne" "$D/progres.txt" || printf '%s\n' "$ligne" >> "$D/progres.txt"; done
        else
            rm -f "$D/journal-dernier.tmp"
            echo "$(date -u +%FT%TZ) journal illisible (appel en échec) : dernier relevé gardé" >> "$D/surveillance.txt"
        fi
        # R-1683 : présence. Une liste VIDE n'est pas une absence ; inventaire et réponse de `show instance` sont masqués par un tube avant d'être écrits.
        ARR=0; LP=9
        liste_presente
        if [ "$LP" = 1 ]; then sleep "${ABSENCE_ATTENTE_S:-15}"; liste_presente; [ "$LP" = 1 ] && ARR=1; fi
        if [ "$ARR" = 0 ] && [ "$LP" != 0 ]; then
            seule_presente
            if [ "$SP" = 4 ]; then sleep "${ABSENCE_ATTENTE_S:-15}"; seule_presente; [ "$SP" = 4 ] && ARR=1; fi
            if [ "$ARR" = 0 ]; then
                if [ "$SP" = 0 ]; then NONET=0; alerte "ALERTE liste d'inventaire non concluante (code $LP : $(head -c 120 "$D/presence.txt" 2>/dev/null | tr '\n' ' ')) : show instance $ID répond, instance présente"
                else
                    NONET=$((NONET + 1))
                    alerte "ALERTE inventaire ($NONET/3) : liste non concluante (code $LP : $(head -c 120 "$D/presence.txt" 2>/dev/null | tr '\n' ' ')) et show instance $ID non concluant (code $SP : $(head -c 120 "$D/presence-seule.txt" 2>/dev/null | tr '\n' ' ')) : présence non établie"
                    if [ "$NONET" -ge 3 ]; then
                        DEC="ARRET inventaire : présence de l'instance $ID non établie trois relevés de suite (ni la liste ni show instance ne concluent) : vérifier à la main (vastai show instances), puis message ; la minuterie de l'instance borne la dépense"
                        alerte "$DEC"; exit 3
                    fi
                fi
            fi
        else NONET=0
        fi
        if [ "$ARR" = 1 ]; then
            DEC="ARRET mort : instance $ID absente à deux relevés (liste non vide sans elle, ou instance seule introuvable) ; confirmer par show instance $ID avant de conclure à une destruction ; relever la cause dans $D/journal-instance.txt (dernières lignes AMORCE) et sur la branche poussée"
            alerte "$DEC"; exit 3
        fi
        if DEC=$(python3 -I -B -c "$SESSION3" surveillance "$PLC" "$D/progres.txt" "$now" "$PC" "$PS" "$CR" "$ANT" "$TEL" ${FACT:+"$FACT"} 2>&1); then ILLISIBLES=0
        else
            ILLISIBLES=$((ILLISIBLES + 1))
            if [ "$ILLISIBLES" -ge 3 ]; then DEC="ARRET garde : garde de dépense illisible trois fois de suite ($DEC) : arrêter l'instance par son identifiant (R10), sans garde la dépense n'est plus bornée"
            else DEC="ALERTE garde de dépense illisible ($ILLISIBLES/3) : $DEC"; fi
        fi
        echo "$(date -u +%FT%TZ) $DEC" >> "$D/surveillance.txt"
        case "$DEC" in
            ARRET*) echo "$DEC"; echo "ARRÊT PAR L'IDENTIFIANT (R10) : timeout -k 5 120 $VAST stop instance $ID"; exit 3 ;;
            FIN*) echo "$DEC"; echo "FIN : instance à arrêter par son identifiant, disque gardé jusqu'au verdict : timeout -k 5 120 $VAST stop instance $ID"; exit 0 ;;
            REFUS*) echo "$DEC"; exit 4 ;;
            ALERTE*) echo "$(date -u +%FT%TZ) $DEC" ;;
        esac
        sleep "$INTERVALLE"
    done ;;
*) echo "usage : controles | controles-epreuve | creation | apres-creation | surveillance" >&2; exit 2 ;;
esac
