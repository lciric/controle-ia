#!/usr/bin/env bash
# Banc du lanceur v2 des notations refaites du pilote de T0.5 (R5 ; option (c) de R-180, R-190), décliné du banc v1 du
# lanceur des notations : tous ses cas, adaptés aux arguments du v2 (aucune offre), plus les cas propres au v2 : offre la
# moins chère choisie parmi les conformes, égalité de prix, offres non conformes écartées, aucune offre conforme (code 3),
# preuve du banc v2 versée au commit C3 (journal absent, verdict, empreintes, sceaux, C3 absent du distant), lanceur v2
# exécuté différent de sa copie versée. Contre-lecture R2 du v2 (LV-01 à LV-18) : prix nul, négatif, infini, booléen ou
# texte écartés ; offres de 40 Go ou de deux cartes écartées ; identifiant négatif (« offre choisie illisible ») ; preuve du
# banc v2 limitée aux trois scripts, lignes mal formées ou en double, banc v2 ou module commun éprouvés sous une autre
# empreinte, sceau faux du lanceur à C3 ; C3 qui touche un autre fichier, copie du sommet du distant autre ; constante du
# devis autre que celle du v1 de S ; dossier de traces purement numérique, forme du v1 à trois arguments ; relancement :
# offres de la machine ou de l'hôte du premier lancement écartées, machine illisible ; crédit calculé sur l'offre choisie
# parmi plusieurs (O08 refait) ; compteur de P13f dans le shell courant. Relecture courte (RC-01 à RC-13) : identifiant en
# double (O11), offres relues gardées sur le chemin du code 3 (O04), machine et hôte archivés (O01), machine ou hôte
# illisibles ou non entiers en relancement (R07, R08), C3 qui déplace un fichier du dossier v2 (Q16b), chacune des six
# constantes du devis et du filtre (K01 à K06), jeton dans la liste des instances lue en relancement. Le cas N06 du v1 (offre absente) est retiré :
# le v2 ne reçoit pas d'offre (O03 le couvre). Historique du banc v1 : décliné des bancs v1 et v2 du lanceur du pilote : un
# cas sain et un artefact par garde, plus les gardes propres aux notations (décision de Lazar sur N-021 à la forme
# exacte ; relance consignée « relancement », « notations », « infrastructure » ; instance du pilote 55538944 tolérée
# arrêtée ; crédit sur 7,5 heures ; plafond de la surveillance écrit à la création + 26 400 s ; étiquette et variables de
# l'amorce des notations, sans ETUDE ; treize scripts de la chaîne égaux à leurs copies versées à S). Aucun appel réel n'est
# possible : faux outil de location (n'appelle aucun service ; journalise le verbe, l'étiquette et les variables non
# secrètes de --env, jamais un jeton), faux contrôles, HOME redirigé, clé d'API retirée, jetons factices. Dépôt
# synthétique : préenregistrement minimal (empreinte de l'amorce, décision sur N-021, ligne « Lancement »), registre des
# décisions (colonne d'état de N-021 à la forme exacte), registre des GO et garde de calcul du dépôt, copies versées des
# faux contrôles et du lanceur (celle du banc) ; dépôt nu local en guise de dépôt distant.
# Usage : essais_lanceur_notations_v2.sh RACINE_NEUVE
set -uo pipefail
E=$(realpath -m "${1:?racine neuve}")
BN=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
HN=${HN:-$BN/notations-v1}
D=/home/user/controle-ia-travail
P=prereg/T0.5-pilote-notations-v1.md
VERSEES=docs/procedures/notations-T0.5-v2
VERSEES3=docs/procedures/notations-T0.5-v3
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
echo "script éprouvé : lancer_notations_v2.sh $(sha256sum "$HN/lancer_notations_v2.sh" | cut -d' ' -f1)"
echo "script éprouvé : verifications_notations_v1.py $(sha256sum "$HN/verifications_notations_v1.py" | cut -d' ' -f1)"
echo "script éprouvé : $(basename "$0") $(sha256sum "$(realpath "$0")" | cut -d' ' -f1)"
NON_CONFORMES=0
mkdir -p "$E/B/notations-v1" "$E/B/venv-vastai/bin" "$E/home" "$E/bin-heure" "$E/bin-df"
cat > "$E/B/venv-vastai/bin/vastai" <<'EOF'
#!/usr/bin/env bash
# faux vastai du banc des notations : n'appelle aucun service
J=${FAUX_VASTAI_JOURNAL:?}
echo "appel : $1 $2" >> "$J"
case "$1 $2" in
  "search offers") [ -n "${FAUX_OFFRES:-}" ] && { printf '%s\n' "$FAUX_OFFRES"; exit 0; }; printf '[{"id": 111, "gpu_name": "%s", "gpu_ram": 81920, "num_gpus": 1, "machine_id": 7101, "host_id": 8101, "dph_total": %s, "cpu_name": "%s", "cpu_arch": "amd64", "cpu_cores": 128}, {"id": 222, "dph_total": 0.9, "cpu_name": "AMD EPYC 7513 32-Core Processor"}]\n' "${FAUX_GPU:-A100 SXM4}" "${FAUX_PRIX:-1.10}" "${FAUX_CPU:-AMD EPYC 7513 32-Core Processor}" ;;
  "show user") printf '{"credit": %s, "email": "x@invalid"}\n' "${FAUX_CREDIT:-20.0}" ;;
  "show instances") [ -n "${FAUX_INSTANCES_ECHEC:-}" ] && { echo "erreur factice" >&2; exit 1; }; d='[{"id": 55292763, "actual_status": "exited", "cur_state": "stopped", "extra_env": [["GH_TOKEN", "secret"]]}, {"id": 55458787, "actual_status": "exited", "cur_state": "stopped"}, {"id": 55538944, "actual_status": "exited", "cur_state": "stopped", "label": "t05-pilote-v1"}]'; printf '%s\n' "${FAUX_INSTANCES:-$d}" ;;
  "create instance")
    echo "CREATION FACTICE" >> "$J"
    echo "offre créée $3" >> "$J"
    a=("$@")
    for ((i = 0; i < ${#a[@]}; i++)); do
      [ "${a[$i]}" = "--label" ] && echo "etiquette ${a[$((i + 1))]}" >> "$J"
      if [ "${a[$i]}" = "--env" ]; then
        for kv in ${a[$((i + 1))]}; do case "$kv" in ETUDE=*|PREREG=*|BRANCHE=*|DEPOT_URL=*) echo "env $kv" >> "$J" ;; COMMIT=*) echo "env COMMIT présent" >> "$J" ;; esac; done
      fi
    done
    d='{"success": true, "new_contract": 99999999}'; printf '%s\n' "${FAUX_CREATION:-$d}"; exit "${FAUX_CODE_CREATION:-0}" ;;
  *) echo "verbe inattendu" >&2; exit 9 ;;
esac
EOF
chmod +x "$E/B/venv-vastai/bin/vastai"
cat > "$E/B/notations-v1/controles_avant_depense_notations_v1.sh" <<'EOF'
#!/usr/bin/env bash
mkdir -p "$2" "$2.travail" && echo donnees > "$2/x"
echo "arguments : S=${1:0:12} mode=${3:-premier}"
if [ -n "${FAUX_KO:-}" ]; then echo "OK  essai"; echo "KO  essai : faute simulée"; echo "CONTRÔLES AVANT DÉPENSE : ÉCHEC"; exit 1; fi
if [ -n "${FAUX_DERNIERE:-}" ]; then echo "OK  essai"; echo "dernière ligne inattendue (essai)"; exit 0; fi
echo "OK  essai"; echo "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES"
EOF
cp "$HN/verifications_notations_v1.py" "$E/B/notations-v1/"
L=$E/B/notations-v1/lancer_notations_v2.sh
sed -e "s|^DEPOT=.*|DEPOT=$E/depot|" -e "s|^B=.*|B=$E/B|" "$HN/lancer_notations_v2.sh" > "$L"
echo "lignes changées dans la copie du lanceur : $(diff "$HN/lancer_notations_v2.sh" "$L" | grep -c '^>')"
[ "$(sed -n 's/^B=//p' "$L")" = "$E/B" ] && [ "$(sed -n 's/^V=//p' "$L")" = '$B/venv-vastai/bin/vastai' ] \
    && ! grep -q "$BN/venv-vastai" "$L" || { echo "copie du lanceur non sûre"; exit 2; }
cat > "$E/bin-heure/date" <<EOF
#!/usr/bin/env bash
if [ "\$*" = "-u +%H%M" ]; then
  n=\$(cat "$E/compteur-heure" 2>/dev/null || echo 0); n=\$((n+1)); echo \$n > "$E/compteur-heure"
  if [ "\$n" -ge 2 ]; then echo "\${FAUX_HEURE2:-2200}"; else echo "\${FAUX_HEURE1:-2200}"; fi; exit 0
fi
exec /usr/bin/date "\$@"
EOF
chmod +x "$E/bin-heure/date"
cat > "$E/bin-df/df" <<EOF
#!/usr/bin/env bash
if [ -n "\${FAUX_DF_TRACES:-}" ] && [ "\${@: -1}" = "$E" ]; then
  printf 'Filesystem 1024-blocks Used Available Capacity Mounted\n/dev/x 100 90 2900000 97%% /\n'; exit 0
fi
exec /usr/bin/df "\$@"
EOF
chmod +x "$E/bin-df/df"
mkdir -p "$E/depot" && cd "$E/depot" && git init -q -b main
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
mkdir -p prereg scripts registres .claude/hooks "$VERSEES"
git -C "$D" show HEAD:scripts/amorce_instance_t05_notations.sh > scripts/amorce_instance_t05_notations.sh
git -C "$D" show HEAD:registres/go.md > registres/go.md
git -C "$D" show HEAD:.claude/hooks/garde_calcul.py > .claude/hooks/garde_calcul.py
cat > registres/decisions.md <<'EOF'
# Registre des décisions (essai)

| id | date | décision | fondement |
|---|---|---|---|
| R-146 | 2026-10-12 | GO-2026-10-12-99 de Lazar sur N-021, option (a) (essai). | essai |

| id | ouvert le | objet | ce qu'il faut |
|---|---|---|---|
| N-021 | 2026-10-12 | notations refaites (essai) | tranché (a) par Lazar : GO-2026-10-12-99 (R-146) |
EOF
echo "| GO-2026-10-12-99 | 2026-10-12 | revendication | N-021, option (a) (essai) | — | — | Lazar | R-146 (essai) |" >> registres/go.md
git add -A && git commit -qm "base"
EA=$(sha256sum scripts/amorce_instance_t05_notations.sh | cut -d' ' -f1)
cat > "$P" <<EOF
# Préenregistrement des notations (essai du banc du lanceur)
- Scripts de l'instance, gelés par ce commit : \`scripts/amorce_instance_t05_notations.sh\` (\`$EA\`, sha256).
- Décision de Lazar sur N-021 : \`GO-2026-10-12-99\` (R-146)
- Lancement : \`PREREG=$P\`, \`BRANCHE=calcul/t05-notations-reel-v1\`, \`DEPOT_URL=https://github.com/lciric/controle-ia-travail.git\` ; relancement unique : \`PREREG=$P\`, \`BRANCHE=calcul/t05-notations-reel-v2\`, même commit.
EOF
(cd prereg && sha256sum "$(basename "$P")" > "$(basename "$P").sha256")
cp "$E/B/notations-v1/controles_avant_depense_notations_v1.sh" "$E/B/notations-v1/verifications_notations_v1.py" "$HN/lancer_notations_v1.sh" "$VERSEES/"
# preuves des essais (journaux des bancs et de la répétition finale) : copies versées des autres scripts éprouvés, puis
# cinq journaux factices conformes, dont les lignes « script éprouvé » portent les empreintes des copies versées ici
# les dix autres scripts de la chaîne, au bloc-notes factice et en copie versée (le lanceur compare les treize)
for s in construire_pilote_jouet_v1.py sceller_notations_v1.sh surveiller_notations_v1.sh recuperation_notations_v1.sh \
         repetition_jouet_notations_v1.sh repetition_finale_notations_v1.sh essais_lanceur_notations_v1.sh \
         essais_controles_notations_v1.sh essais_scellement_notations_v1.sh essais_surveillance_notations_v1.sh; do
    cp "$HN/$s" "$VERSEES/" && cp "$HN/$s" "$E/B/notations-v1/" || { echo "copie versée factice impossible : $s"; exit 2; }
done
ep() { for s in "$@"; do echo "script éprouvé : $s $(sha256sum "$VERSEES/$s" | cut -d' ' -f1)"; done; }
journal_preuve() {   # $1 nom du journal, $2 dernière ligne, puis les scripts éprouvés
    local n=$1 v=$2; shift 2
    { echo "journal factice du banc du lanceur"; ep "$@"; echo "$v"; } > "$VERSEES/$n"
    (cd "$VERSEES" && sha256sum "$n" > "$n.sha256")
}
journaux_preuves() {
    journal_preuve banc-lanceur-notations-v1.log "FIN DU BANC DU LANCEUR DES NOTATIONS ; cas non conformes : 0" lancer_notations_v1.sh verifications_notations_v1.py essais_lanceur_notations_v1.sh
    journal_preuve banc-surveillance-notations-v1.log "FIN DU BANC DE LA SURVEILLANCE DES NOTATIONS ; cas non conformes : 0" surveiller_notations_v1.sh essais_surveillance_notations_v1.sh
    journal_preuve banc-controles-notations-v1.log "FIN DU BANC DES CONTRÔLES DES NOTATIONS ; cas non conformes : 0" controles_avant_depense_notations_v1.sh verifications_notations_v1.py essais_controles_notations_v1.sh
    journal_preuve banc-scellement-notations-v1.log "FIN DU BANC DU SCELLEMENT DES NOTATIONS ; cas non conformes : 0" sceller_notations_v1.sh verifications_notations_v1.py essais_scellement_notations_v1.sh
    journal_preuve repetition-finale-notations-v1.log "RÉPÉTITION FINALE : CONFORME" sceller_notations_v1.sh controles_avant_depense_notations_v1.sh repetition_finale_notations_v1.sh
}
journaux_preuves
git add -A && git commit -qm "S : préenregistrement des notations scellé (essai)"
S=$(git rev-parse HEAD); echo "S = $S"
mkdir -p "$E/v3-sauve"
cp "$L" "$E/v3-sauve/lancer_notations_v2.sh"; cp "$(realpath "$0")" "$E/v3-sauve/essais_lanceur_notations_v2.sh"
journal_v2() {   # $1 dossier ; journal factice conforme du banc v2, aux empreintes des copies du dossier
    { echo "journal factice du banc v2"
      echo "script éprouvé : lancer_notations_v2.sh $(sha256sum "$1/lancer_notations_v2.sh" | cut -d' ' -f1)"
      echo "script éprouvé : essais_lanceur_notations_v2.sh $(sha256sum "$1/essais_lanceur_notations_v2.sh" | cut -d' ' -f1)"
      echo "script éprouvé : verifications_notations_v1.py $(sha256sum "$E/depot/$VERSEES/verifications_notations_v1.py" | cut -d' ' -f1)"
      echo "FIN DU BANC DU LANCEUR V2 DES NOTATIONS ; cas non conformes : 0"; } > "$1/banc-lanceur-notations-v2.log"
}
sceller_v3() { (cd "$1" && for f in lancer_notations_v2.sh essais_lanceur_notations_v2.sh banc-lanceur-notations-v2.log; do sha256sum "$f" > "$f.sha256"; done); }
journal_v2 "$E/v3-sauve"; sceller_v3 "$E/v3-sauve"
nouveau_c3() {   # $1 dossier des fichiers du v3 (défaut : la sauvegarde conforme) ; C3 refait par un retrait puis un ajout
    local src=${1:-$E/v3-sauve}
    if [ -d "$VERSEES3" ]; then git rm -q -r "$VERSEES3" && git commit -qm "essai : retrait du v3" || { echo "nouveau C3 : retrait impossible"; exit 2; }; fi
    mkdir -p "$VERSEES3" && cp "$src"/* "$VERSEES3/" && git add "$VERSEES3" && git commit -qm "essai : C3" || { echo "nouveau C3 : ajout impossible"; exit 2; }
    git remote get-url origin >/dev/null 2>&1 && { git push -q origin HEAD:main && git fetch -q origin || { echo "nouveau C3 : poussée impossible"; exit 2; }; }
    return 0
}
nouveau_c3
git clone -q --bare . "$E/distant.git" && git remote add origin "$E/distant.git" && git fetch -q origin
cp registres/decisions.md "$E/decisions-sauve.md"; cp registres/go.md "$E/go-sauve.md"
cas() {   # $1 nom ; $2 code attendu ; $3 arguments du lanceur (« - » : les arguments normaux) ; puis l'environnement
    local nom=$1 attendu=$2 args=$3; shift 3
    rm -rf "$E/traces" "$E/compteur-heure"; : > "$E/journal-$nom.txt"
    local a=("$E/traces" -); [ "$args" = "-" ] || read -r -a a <<<"$args"
    env -u VAST_API_KEY HOME="$E/home" PATH="$E/bin-heure:$E/bin-df:/usr/bin:/bin" \
        HF_TOKEN=factice-hf-0000000 CONTROLE_IA_GITHUB_TOKEN=factice-gh-0000000 FAUX_VASTAI_JOURNAL="$E/journal-$nom.txt" \
        "$@" bash "$L" "${a[@]}" > "$E/sortie-$nom.txt" 2>&1
    local c=$?
    local cree; cree=$(grep -c "CREATION FACTICE" "$E/journal-$nom.txt")
    local v="CONFORME"; [ "$c" = "$attendu" ] || v="NON CONFORME (attendu $attendu)"
    [ "$attendu" != 0 ] && [ "$cree" != 0 ] && [ "$attendu" != 4 ] && v="NON CONFORME (création alors qu'un arrêt était attendu)"
    [ "$attendu" = 0 ] && [ "$cree" != 1 ] && v="NON CONFORME (pas de création)"
    local tr; tr=$(realpath -m "${a[0]:-$E/traces}")
    { [ -e "$tr/clone-controles" ] || [ -e "$tr/clone-controles.travail" ]; } && v="NON CONFORME (clone des contrôles resté)"
    [ -n "${MOTIF_CAS:-}" ] && ! grep -qF -- "$MOTIF_CAS" "$E/sortie-$nom.txt" && v="NON CONFORME (motif « $MOTIF_CAS » absent)"
    [ "$v" = CONFORME ] || NON_CONFORMES=$((NON_CONFORMES + 1))
    echo "$nom : code $c ; créations factices $cree ; $v"
    grep -v '^$' "$E/sortie-$nom.txt" | tail -2 | sed 's/^/    | /' | cut -c1-200
    [ -f "$E/traces/lancement.txt" ] && cp "$E/traces/lancement.txt" "$E/lancement-$nom.txt"
}
printf 'AMORCE 2026-10-13T08:00:00Z : commit %s\nPROGRES 2026-10-13T09:00:00Z juge=8B lot=1/23 duree_s=344.1\n' "$S" > "$E/releve-sain.txt"
cp "$E/releve-sain.txt" "$E/releve-fin.txt"; echo "PROGRES 2026-10-13T11:20:00Z juge=8B fin=échu lots_faits=20/23 duree_s=12000.0" >> "$E/releve-fin.txt"
echo "PROGRES 2026-10-13T09:00:00Z juge=8B lot=1/23 duree_s=344.1" > "$E/releve-sans-amorce.txt"
cp "$E/releve-sain.txt" "$E/releve-dernier-lot.txt"; echo "PROGRES 2026-10-13T11:19:00Z juge=8B lot=23/23 duree_s=200.4" >> "$E/releve-dernier-lot.txt"
cp "$E/releve-sain.txt" "$E/releve-lot-2-sur-23.txt"; echo "PROGRES 2026-10-13T09:06:00Z juge=8B lot=2/23 duree_s=344.0" >> "$E/releve-lot-2-sur-23.txt"
cas P00-sain 0 - FAUX_X=1
grep -E "etiquette|env " "$E/journal-P00-sain.txt" | sed 's/^/    > /'
# vérifications du cas sain, comptées (vérification courte de la chaîne, constat 1) : plafond de la surveillance écrit à
# la création + 26 400 s, branche v1, étiquette, ETUDE absente, instances arrêtées tolérées
python3 - "$E/lancement-P00-sain.txt" "$E/journal-P00-sain.txt" <<'EOF' || { echo "    P00 : vérifications du cas sain : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
import re, sys
t = open(sys.argv[1], encoding="utf-8").read(); j = open(sys.argv[2], encoding="utf-8").read()
c = re.search(r"^creation (\d+)$", t, re.M); pl = re.search(r"^plafond de la surveillance (\d+) \(création \+ 26400 s ; surveiller_notations_v1\.sh <id> (\d+) <dossier neuf>\)$", t, re.M)
v = {"plafond de la surveillance = création + 26 400 s": bool(c and pl and int(pl.group(1)) - int(c.group(1)) == 26400 and pl.group(2) == c.group(1)),
     "branche v1": bool(re.search(r"^branche calcul/t05-notations-reel-v1$", t, re.M) and re.search(r"^env BRANCHE=calcul/t05-notations-reel-v1$", j, re.M)),
     "étiquette": bool(re.search(r"^etiquette t05-notations-v1$", j, re.M)),
     "ETUDE absente": "env ETUDE=" not in j, "instances arrêtées tolérées (dont 55538944)": "55538944 (exited, stopped)" in t}
print("    > " + " ; ".join(f"{k} : {x}" for k, x in v.items()))
sys.exit(0 if all(v.values()) else 1)
EOF
cas P01-creee-mais-code-1 4 - FAUX_CODE_CREATION=1
cas P02-reponse-illisible 4 - FAUX_CREATION=illisible
cas P03-echec-creation 4 - 'FAUX_CREATION={"success": false, "msg": "non"}'
cas P04-heure-2345-avant-creation 3 - FAUX_HEURE2=2345
cas P04b-heure-2340-au-depart 3 - FAUX_HEURE1=2340
cas P04c-heure-2329-au-depart 0 - FAUX_HEURE1=2329
cas P05-place-traces 3 - FAUX_DF_TRACES=1
cas P06-controles-ko 2 - FAUX_KO=1
MOTIF_CAS="aucune offre conforme" cas P07-offre-sans-prix 3 - FAUX_PRIX=null
MOTIF_CAS="aucune offre conforme" cas P07b-prix-au-dessus-du-devis 3 - FAUX_PRIX=1.35
MOTIF_CAS="aucune offre conforme" cas P07c-processeur-autre 3 - 'FAUX_CPU=Intel Xeon Platinum 8480+'
MOTIF_CAS="aucune offre conforme" cas P07d-processeur-voisin 3 - 'FAUX_CPU=AMD EPYC 7513'
MOTIF_CAS="aucune offre conforme" cas P07e-carte-pcie 3 - 'FAUX_GPU=A100 PCIE'
# crédit exigé : 7,5 h × 1,10 + 1,2 = 9,45 USD
MOTIF_CAS="crédit insuffisant pour les notations" cas P08-credit-insuffisant 3 - FAUX_CREDIT=9.44
MOTIF_CAS="minimum 9.45 USD (7.5 h)" cas P08b-credit-juste 0 - FAUX_CREDIT=9.45
cas P09-jeton-hf-absent 2 - HF_TOKEN=
cas P09b-jeton-github-absent 2 - CONTROLE_IA_GITHUB_TOKEN=
cas P10-argument-absent 2 "" FAUX_X=1
cas P10b-relance-sans-cause 2 "$E/traces - relance" FAUX_X=1
MOTIF_CAS="usage" cas P10c-relance-sans-releve 2 "$E/traces - relance R-151" FAUX_X=1
cas P11-instance-non-toleree 2 - 'FAUX_INSTANCES=[{"id": 1, "actual_status": "running", "cur_state": "running"}]'
cas P11b-pilote-en-marche 2 - 'FAUX_INSTANCES=[{"id": 55538944, "actual_status": "running", "cur_state": "running", "label": "t05-pilote-v1"}]'
cas P11c-aucune-instance 0 - 'FAUX_INSTANCES=[]'
cas P11d-liste-des-instances-illisible 2 - FAUX_INSTANCES_ECHEC=1
# colonne d'état de N-021 : forme exacte « tranché (a) par Lazar : GO (R-…) », rien d'autre ; aucun mot-clé
for variante in "P12-n021-forme-inexacte|tranché le 2026-10-12 par Lazar : option (a), GO-2026-10-12-99 (R-146)" \
                "P12b-n021-en-attente|en attente" "P12d-n021-option-b|tranché (b) par Lazar : GO-2026-10-12-99 (R-146)" \
                "P12e-n021-suite-ajoutee|tranché (a) par Lazar : GO-2026-10-12-99 (R-146) ; révoqué par Lazar" \
                "P12f-n021-texte-avant|révoqué par Lazar, puis tranché (a) par Lazar : GO-2026-10-12-99 (R-146)"; do
    cp "$E/decisions-sauve.md" registres/decisions.md
    sed -i "s/| tranché (a) par Lazar : GO-2026-10-12-99 (R-146) |\$/| ${variante#*|} |/" registres/decisions.md
    MOTIF_CAS="N-021 non tranchée par Lazar (forme exacte)" cas "${variante%%|*}" 2 - FAUX_X=1
done
cp "$E/decisions-sauve.md" registres/decisions.md
sed -i '/^| N-021 |/d' registres/decisions.md
MOTIF_CAS="N-021 non tranchée par Lazar (forme exacte)" cas P12c-n021-absente 2 - FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
echo "| R-150 | 2026-10-12 | N-021 non révoquée : rappel (essai). | essai |" >> registres/decisions.md
cas P12g-ligne-r-qui-mentionne-une-revocation 0 - FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
echo "| GO-2026-10-12-98 | 2026-10-12 | révocation | révoque GO-2026-10-12-99 (essai) | — | — | Lazar | essai |" >> registres/go.md
MOTIF_CAS="décision de Lazar sur N-021 : GO-2026-10-12-99 révoqué" cas P17-go-n021-revoque 2 - FAUX_X=1
cp "$E/go-sauve.md" registres/go.md
echo "| GO-2026-10-12-97 | 2026-10-12 | révocation | révoque GO-2026-10-04-08 (essai) | — | — | Lazar | essai |" >> registres/go.md
MOTIF_CAS="décision de Lazar sur N-021 : GO-2026-10-04-08 révoqué" cas P17b-go-calcul-revoque 2 - FAUX_X=1
cp "$E/go-sauve.md" registres/go.md
echo "| GO-2026-10-12-98 | 2026-10-12 | révocation de GO-2026-10-12-99 (essai) |" >> registres/go.md
MOTIF_CAS="décision de Lazar sur N-021 : GO-2026-10-12-99 révoqué" cas P17h-go-revoque-ligne-mal-formee 2 - FAUX_X=1
cp "$E/go-sauve.md" registres/go.md
echo "| GO-2026-10-12-97 | 2026-10-12 | revendication | essai : aucune révocation de GO-2026-10-12-99 | — | — | Lazar | essai |" >> registres/go.md
cas P17i-ligne-go-qui-mentionne-une-revocation 0 - FAUX_X=1
cp "$E/go-sauve.md" registres/go.md
sed -i '/^| GO-2026-10-12-99 |/d' registres/go.md
MOTIF_CAS="décision de Lazar sur N-021 : GO-2026-10-12-99 absent, en double ou mal formé" cas P17c-go-absent-du-registre 2 - FAUX_X=1
cp "$E/go-sauve.md" registres/go.md
sed -i 's/| tranché (a) par Lazar : GO-2026-10-12-99 (R-146) |$/| tranché (a) par Lazar : GO-2026-10-12-98 (R-146) |/' registres/decisions.md
MOTIF_CAS="décision de Lazar sur N-021 : N-021 : colonne d'état ≠" cas P17d-n021-autre-go 2 - FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
sed -i 's/| tranché (a) par Lazar : GO-2026-10-12-99 (R-146) |$/| tranché (a) par Lazar : GO-2026-10-12-99 (R-147) |/' registres/decisions.md
MOTIF_CAS="décision de Lazar sur N-021 : N-021 : colonne d'état ≠" cas P17e-n021-autre-registre 2 - FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
sed -i '/^| R-146 |/d' registres/decisions.md
MOTIF_CAS="décision de Lazar sur N-021 : R-146 absent, en double ou sans GO-2026-10-12-99" cas P17f-registre-du-go-absent 2 - FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
sed -i 's/| N-021, option (a) (essai) |/| N-021, option (b) (essai) |/' registres/go.md
MOTIF_CAS="GO de type « revendication », accordé par Lazar, sur N-021 (a), attendu" cas P17g-go-sur-l-option-b 2 - FAUX_X=1
cp "$E/go-sauve.md" registres/go.md
sed -i 's/| N-021, option (a) (essai) |/| N-019, option (a) (essai) |/' registres/go.md
MOTIF_CAS="GO de type « revendication », accordé par Lazar, sur N-021 (a), attendu" cas P17j-go-d-un-autre-noeud 2 - FAUX_X=1
cp "$E/go-sauve.md" registres/go.md
verser_releve() {   # $1 relevé : copie versée et scellée à HEAD, sous le dossier de l'instance du premier lancement (12345678)
    mkdir -p traces/t05-notations-releve-12345678 && cp "$1" traces/t05-notations-releve-12345678/releve-cumulatif.txt \
        && (cd traces/t05-notations-releve-12345678 && sha256sum releve-cumulatif.txt > releve-cumulatif.txt.sha256) \
        && git add traces && { git diff --cached --quiet || git commit -qm "essai : relevé versé"; } || { echo "relevé : versement impossible"; exit 2; }
}
verser_releve "$E/releve-sain.txt"
PREMIERE_ARRETEE='{"id": 12345678, "actual_status": "exited", "cur_state": "stopped", "machine_id": 7001, "host_id": 8001, "extra_env": [["GH_TOKEN", "secret"]]}'
MOTIF_CAS="relance non consignée" cas P13-relance-non-consignee 2 "$E/traces - relance R-151 $E/releve-sain.txt" FAUX_X=1
echo "| R-151 | 2026-10-12 | Notations : panne réseau de l'hôte (essai). | essai |" >> registres/decisions.md
MOTIF_CAS="relance non consignée" cas P13b-relance-cause-sans-infrastructure 2 "$E/traces - relance R-151 $E/releve-sain.txt" FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
echo "| R-151 | 2026-10-12 | Relancement du pilote : cause d'infrastructure (panne réseau de l'hôte, instance 12345678 arrêtée, essai). | essai |" >> registres/decisions.md
MOTIF_CAS="relance non consignée" cas P13g-relance-du-pilote-et-non-des-notations 2 "$E/traces - relance R-151 $E/releve-sain.txt" FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
echo "| R-151 | 2026-10-12 | Relancement des notations : cause d'infrastructure (panne réseau de l'hôte, dépense engagée 1,00 USD, essai). | essai |" >> registres/decisions.md
MOTIF_CAS="ne nomme pas, une seule fois, l'instance du premier lancement" cas P13d-relance-sans-instance-nommee 2 "$E/traces - relance R-151 $E/releve-sain.txt" FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
echo "| R-151 | 2026-10-12 | Relancement des notations : cause d'infrastructure (panne réseau de l'hôte, instance 12345678 arrêtée, essai). | essai |" >> registres/decisions.md
MOTIF_CAS="« dépense engagée X,XX USD »" cas P13k-relance-sans-depense-engagee 2 "$E/traces - relance R-151 $E/releve-sain.txt" FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
echo "| R-151 | 2026-10-12 | Relancement des notations : cause d'infrastructure (panne réseau de l'hôte, instance 12345678 arrêtée, dépense engagée 1,00 USD, essai). | essai |" >> registres/decisions.md
cas P13c-relance-saine 0 "$E/traces - relance R-151 $E/releve-sain.txt" 'FAUX_INSTANCES=[{"id": 55292763, "actual_status": "exited", "cur_state": "stopped"}, {"id": 12345678, "actual_status": "exited", "cur_state": "stopped", "machine_id": 7001, "host_id": 8001}]'
MOTIF_CAS="autres instances sur le compte : 12345678 (running, running)" cas P13e-relance-premiere-en-marche 2 "$E/traces - relance R-151 $E/releve-sain.txt" 'FAUX_INSTANCES=[{"id": 12345678, "actual_status": "running", "cur_state": "running", "machine_id": 7001, "host_id": 8001}]'
pushd "$E" > /dev/null && cas P13f-traces-en-chemin-relatif 0 "traces-relatives - relance R-151 $E/releve-sain.txt" "FAUX_INSTANCES=[$PREMIERE_ARRETEE]"; popd > /dev/null
grep -E "etiquette|env BRANCHE" "$E/journal-P13c-relance-saine.txt" | sed 's/^/    > /'
# relance : étiquette et branche exactes, comptées (vérification courte de la chaîne, second tour, constat 3)
if grep -qx "etiquette t05-notations-v1-relance" "$E/journal-P13c-relance-saine.txt" \
    && grep -qx "env BRANCHE=calcul/t05-notations-reel-v2" "$E/journal-P13c-relance-saine.txt" \
    && grep -qx "branche calcul/t05-notations-reel-v2" "$E/lancement-P13c-relance-saine.txt"; then
    echo "    P13c : étiquette t05-notations-v1-relance et branche calcul/t05-notations-reel-v2 : CONFORME"
else echo "    P13c : étiquette ou branche de la relance : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); fi
# relevé cumulatif du premier lancement (préséance) ; plafond de GO-2026-10-12-02 : 1,00 + 7,5 × 1,10 + 0,5 = 9,75 USD
verser_releve "$E/releve-fin.txt"
MOTIF_CAS="un juge a fini, ou peut avoir fini, au premier lancement" cas P13h-releve-avec-fin-de-juge 2 "$E/traces - relance R-151 $E/releve-fin.txt" "FAUX_INSTANCES=[$PREMIERE_ARRETEE]"
verser_releve "$E/releve-dernier-lot.txt"
MOTIF_CAS="peut avoir fini, au premier lancement (PROGRES 2026-10-13T11:19:00Z juge=8B lot=23/23" cas P13o-releve-avec-dernier-lot 2 "$E/traces - relance R-151 $E/releve-dernier-lot.txt" "FAUX_INSTANCES=[$PREMIERE_ARRETEE]"
verser_releve "$E/releve-lot-2-sur-23.txt"
MOTIF_CAS="relevé du premier lancement : aucune fin de juge" cas P13p-releve-lot-2-sur-23-sain 0 "$E/traces - relance R-151 $E/releve-lot-2-sur-23.txt" "FAUX_INSTANCES=[$PREMIERE_ARRETEE]"
MOTIF_CAS="relevé passé en argument ≠ copie versée" cas P13i-releve-absent 2 "$E/traces - relance R-151 $E/releve-absent.txt" "FAUX_INSTANCES=[$PREMIERE_ARRETEE]"
verser_releve "$E/releve-sans-amorce.txt"
MOTIF_CAS="sans ligne « AMORCE … : commit » du commit de scellement" cas P13j-releve-sans-amorce 2 "$E/traces - relance R-151 $E/releve-sans-amorce.txt" "FAUX_INSTANCES=[$PREMIERE_ARRETEE]"
sed "s/: commit $S/: commit $(printf '0%.0s' {1..40})/" "$E/releve-sain.txt" > "$E/releve-autre-commit.txt"; verser_releve "$E/releve-autre-commit.txt"
MOTIF_CAS="sans ligne « AMORCE … : commit » du commit de scellement" cas P13s-releve-d-un-autre-commit 2 "$E/traces - relance R-151 $E/releve-autre-commit.txt" "FAUX_INSTANCES=[$PREMIERE_ARRETEE]"
verser_releve "$E/releve-sain.txt"; echo "0000  releve-cumulatif.txt" > traces/t05-notations-releve-12345678/releve-cumulatif.txt.sha256; git add traces && git commit -qm "essai : sceau du relevé faussé"
MOTIF_CAS="relevé du premier lancement : sceau absent ou non conforme" cas P13r-releve-au-sceau-faux 2 "$E/traces - relance R-151 $E/releve-sain.txt" "FAUX_INSTANCES=[$PREMIERE_ARRETEE]"
git rm -q -r traces/t05-notations-releve-12345678 && git commit -qm "essai : relevé retiré"
MOTIF_CAS="relevé du premier lancement non versé au dépôt" cas P13q-releve-non-verse 2 "$E/traces - relance R-151 $E/releve-sain.txt" "FAUX_INSTANCES=[$PREMIERE_ARRETEE]"
verser_releve "$E/releve-sain.txt"
MOTIF_CAS="= 9.75 USD (au plus 10.5)" cas P13m-relance-dans-le-plafond 0 "$E/traces - relance R-151 $E/releve-sain.txt" "FAUX_INSTANCES=[$PREMIERE_ARRETEE]"
EPYC="AMD EPYC 7513 32-Core Processor"
off() {   # identifiant prix [carte [processeur [mémoire [cartes [machine [hôte]]]]]] : une offre du faux outil, en JSON
    printf '{"id": %s, "gpu_name": "%s", "cpu_name": "%s", "gpu_ram": %s, "num_gpus": %s, "machine_id": %s, "host_id": %s, "dph_total": %s}' \
        "$1" "${3:-A100 SXM4}" "${4:-$EPYC}" "${5:-81920}" "${6:-1}" "${7:-7100}" "${8:-8100}" "$2"
}
MOTIF_CAS="aucune offre conforme au filtre du plan" cas R01-relance-seule-offre-sur-la-machine-du-premier 3 "$E/traces - relance R-151 $E/releve-sain.txt" "FAUX_INSTANCES=[$PREMIERE_ARRETEE]" "FAUX_OFFRES=[$(off 111 1.10 "A100 SXM4" "$EPYC" 81920 1 7001 8009)]"
grep -qx "offres conformes écartées (machine ou hôte du premier lancement, ou illisibles) : 111" "$E/lancement-R01-relance-seule-offre-sur-la-machine-du-premier.txt" \
    && echo "    R01 : offre 111 écartée (machine du premier lancement) : CONFORME" \
    || { echo "    R01 : offre écartée : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
MOTIF_CAS="offre choisie : 112 (1.2 USD/h)" cas R02-relance-autre-machine-prise 0 "$E/traces - relance R-151 $E/releve-sain.txt" "FAUX_INSTANCES=[$PREMIERE_ARRETEE]" "FAUX_OFFRES=[$(off 111 1.05 "A100 SXM4" "$EPYC" 81920 1 7001 8009), $(off 112 1.20 "A100 SXM4" "$EPYC" 81920 1 7002 8002)]"
grep -qx "offre créée 112" "$E/journal-R02-relance-autre-machine-prise.txt" && echo "    R02 : offre créée 112 : CONFORME" \
    || { echo "    R02 : offre créée : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
MOTIF_CAS="offre choisie : 112 (1.2 USD/h)" cas R03-relance-meme-hote-ecarte 0 "$E/traces - relance R-151 $E/releve-sain.txt" "FAUX_INSTANCES=[$PREMIERE_ARRETEE]" "FAUX_OFFRES=[$(off 111 1.05 "A100 SXM4" "$EPYC" 81920 1 7003 8001), $(off 112 1.20 "A100 SXM4" "$EPYC" 81920 1 7002 8002)]"
MOTIF_CAS="machine ou hôte du premier lancement illisible" cas R04-relance-machine-du-premier-illisible 2 "$E/traces - relance R-151 $E/releve-sain.txt" 'FAUX_INSTANCES=[{"id": 12345678, "actual_status": "exited", "cur_state": "stopped"}]'
MOTIF_CAS="instance du premier lancement 12345678 absente de la liste" cas R05-relance-premier-absent-de-la-liste 2 "$E/traces - relance R-151 $E/releve-sain.txt" 'FAUX_INSTANCES=[]'
MOTIF_CAS="offre choisie : 111 (1.1 USD/h)" cas R06-premier-lancement-rien-d-ecarte 0 - "FAUX_OFFRES=[$(off 111 1.10 "A100 SXM4" "$EPYC" 81920 1 7001 8001)]"
MOTIF_CAS="offre choisie : 112 (1.2 USD/h)" cas R07-relance-offre-sans-machine-ni-hote-ecartee 0 "$E/traces - relance R-151 $E/releve-sain.txt" "FAUX_INSTANCES=[$PREMIERE_ARRETEE]" "FAUX_OFFRES=[{\"id\": 111, \"gpu_name\": \"A100 SXM4\", \"cpu_name\": \"$EPYC\", \"gpu_ram\": 81920, \"num_gpus\": 1, \"dph_total\": 0.9}, $(off 112 1.20 "A100 SXM4" "$EPYC" 81920 1 7002 8002)]"
grep -qx "offres conformes écartées (machine ou hôte du premier lancement, ou illisibles) : 111" "$E/lancement-R07-relance-offre-sans-machine-ni-hote-ecartee.txt" \
    && echo "    R07 : offre 111 sans machine ni hôte écartée : CONFORME" \
    || { echo "    R07 : offre écartée : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
MOTIF_CAS="offre choisie : 112 (1.2 USD/h)" cas R08-relance-machine-non-entiere-ecartee 0 "$E/traces - relance R-151 $E/releve-sain.txt" "FAUX_INSTANCES=[$PREMIERE_ARRETEE]" "FAUX_OFFRES=[$(off 111 0.9 "A100 SXM4" "$EPYC" 81920 1 7001.0 8001.0), $(off 112 1.20 "A100 SXM4" "$EPYC" 81920 1 7002 8002)]"
cp "$E/decisions-sauve.md" registres/decisions.md
echo "| R-151 | 2026-10-12 | Relancement des notations : cause d'infrastructure (panne réseau de l'hôte, instance 12345678 arrêtée, dépense engagée 2,00 USD, essai). | essai |" >> registres/decisions.md
MOTIF_CAS="relancement hors du plafond de GO-2026-10-12-02" cas P13l-relance-hors-plafond 3 "$E/traces - relance R-151 $E/releve-sain.txt" "FAUX_INSTANCES=[$PREMIERE_ARRETEE]"
cp "$E/decisions-sauve.md" registres/decisions.md
echo "| R-151 | 2026-10-12 | Relancement des notations : cause d'infrastructure (panne réseau de l'hôte, instance 12345678 arrêtée, dépense engagée 1,75 USD, essai). | essai |" >> registres/decisions.md
MOTIF_CAS="= 10.50 USD (au plus 10.5)" cas P13n-relance-au-plafond-juste 0 "$E/traces - relance R-151 $E/releve-sain.txt" "FAUX_INSTANCES=[$PREMIERE_ARRETEE]"
cp "$E/decisions-sauve.md" registres/decisions.md
cp "$E/B/notations-v1/controles_avant_depense_notations_v1.sh" "$E/ctl-sauve.sh"
echo "# modifié" >> "$E/B/notations-v1/controles_avant_depense_notations_v1.sh"
MOTIF_CAS="controles_avant_depense_notations_v1.sh exécuté ≠ copie versée au commit S" cas P14-controles-non-verses 2 - FAUX_X=1
cp "$E/ctl-sauve.sh" "$E/B/notations-v1/controles_avant_depense_notations_v1.sh"
cp "$E/B/notations-v1/surveiller_notations_v1.sh" "$E/surv-sauve.sh"; echo "# modifié" >> "$E/B/notations-v1/surveiller_notations_v1.sh"
MOTIF_CAS="surveiller_notations_v1.sh exécuté ≠ copie versée au commit S" cas P31-surveillance-non-versee 2 - FAUX_X=1
cp "$E/surv-sauve.sh" "$E/B/notations-v1/surveiller_notations_v1.sh"
cp "$L" "$E/lanceur-sauve.sh"; echo "# modifié" >> "$L"
MOTIF_CAS="lancer_notations_v2.sh exécuté ≠ copie versée au commit C3" cas P14b-lanceur-non-verse 2 - FAUX_X=1
cp "$E/lanceur-sauve.sh" "$L"
AVANT_P15=$(git -C "$E/distant.git" rev-parse refs/heads/main)     # C3 : le distant est rétabli tel quel
git -C "$E/distant.git" update-ref refs/heads/main "$(git -C "$E/depot" rev-parse "$S~1")"
MOTIF_CAS="absent du dépôt distant" cas P15-s-absent-du-distant 2 - FAUX_X=1
git -C "$E/distant.git" update-ref refs/heads/main "$AVANT_P15"
git -C "$E/depot" fetch -q origin
# v2 : C3 absent du distant (le distant ramené à S, avant tout S refait : aucune copie du v3 n'y précède S)
git -C "$E/distant.git" update-ref refs/heads/main "$S"
MOTIF_CAS="commit C3 du lanceur v2 introuvable sur le dépôt distant" cas Q08a-c3-absent-du-distant 2 - FAUX_X=1
git -C "$E/distant.git" update-ref refs/heads/main "$AVANT_P15"
git -C "$E/depot" fetch -q origin
cas P16-sain-rejoue 0 - FAUX_X=1
cp "$E/B/notations-v1/verifications_notations_v1.py" "$E/verif-sauve.py"; echo "# modifié" >> "$E/B/notations-v1/verifications_notations_v1.py"
MOTIF_CAS="verifications_notations_v1.py exécuté ≠ copie versée au commit S" cas P14c-module-commun-non-verse 2 - FAUX_X=1
cp "$E/verif-sauve.py" "$E/B/notations-v1/verifications_notations_v1.py"
MOTIF_CAS="contrôles : dernière ligne inattendue" cas N07-controles-derniere-ligne-autre 2 - FAUX_DERNIERE=1
mkdir -p "$E/traces-existantes"
MOTIF_CAS="existe déjà (R12)" cas N05-traces-existantes 2 "$E/traces-existantes -" FAUX_X=1
MOTIF_CAS="succès : True" cas N04-jeton-dans-la-reponse 0 - 'FAUX_CREATION={"success": true, "new_contract": 99999999, "msg": "jeton factice-hf-0000000 et factice-gh-0000000"}'
MOTIF_CAS="réponse illisible" cas N04b-jeton-dans-une-reponse-illisible 4 - 'FAUX_CREATION=erreur factice-gh-0000000 refusé'
cp registres/go.md "$E/go-avant-echeance.md"
python3 - <<'PYECH'
from pathlib import Path
g = Path("registres/go.md"); lignes = g.read_text(encoding="utf-8").split("\n")
i = [k for k, x in enumerate(lignes) if x.startswith("| GO-2026-10-04-08 |")]
assert len(i) == 1
c = lignes[i[0]].split("|"); c[6] = " 2026-10-11 "; lignes[i[0]] = "|".join(c)
g.write_text("\n".join(lignes), encoding="utf-8")
PYECH
MOTIF_CAS="période de validité" cas N03-go-calcul-echu 2 - FAUX_X=1
cp "$E/go-avant-echeance.md" registres/go.md
sed "s|^P=prereg/T0.5-pilote-notations-v1.md|P=prereg/absent-v1.md|" "$L" > "$E/lanceur-sans-s.sh"
[ "$(diff "$L" "$E/lanceur-sans-s.sh" | grep -c '^>')" = 1 ] || { echo "copie du lanceur (S introuvable) : une ligne exactement attendue"; exit 2; }
L_SAUVE=$L; L=$E/lanceur-sans-s.sh
MOTIF_CAS="commit de scellement introuvable" cas N08-s-introuvable 2 - FAUX_X=1
L=$L_SAUVE
# texte de S : amorce non citée, branche autre (S refait par un retrait puis un ajout du sceau, puis rétabli)
nouveau_s() {   # $1 expression sed sur le préenregistrement (vide : texte d'origine)
    git rm -q "$P" "$P.sha256" && git commit -qm "essai : retrait du préenregistrement"
    mkdir -p "$(dirname "$P")" && cp "$E/prereg-origine.md" "$P" || { echo "nouveau S : copie impossible"; exit 2; }
    [ -n "$1" ] && { sed -i "$1" "$P"; cmp -s "$P" "$E/prereg-origine.md" && { echo "nouveau S : l'expression n'a rien changé"; exit 2; }; }
    (cd prereg && sha256sum "$(basename "$P")" > "$(basename "$P").sha256")
    git add "$P" "$P.sha256" && git commit -qm "essai : S refait" && git push -q origin HEAD:main && git fetch -q origin \
        || { echo "nouveau S : commit ou poussée impossible"; exit 2; }
    nouveau_c3                                   # C3 doit descendre de S (lanceur v2)
}
cp "$P" "$E/prereg-origine.md"
nouveau_s "s/(\`[0-9a-f]\{64\}\`, sha256)/(\`$(printf '0%.0s' {1..64})\`, sha256)/"
MOTIF_CAS="empreinte de l'amorce" cas N01-amorce-non-citee 2 - FAUX_X=1
nouveau_s "s/BRANCHE=calcul\/t05-notations-reel-v1/BRANCHE=calcul\/t05-notations-reel-v9/"
MOTIF_CAS="PREREG ou BRANCHE : le préenregistrement de S cite autre chose" cas N02-branche-autre 2 - FAUX_X=1
nouveau_s ""
cas N00-sain-apres-retablissement 0 - FAUX_X=1
# preuves des essais : journal au verdict non conforme, empreinte d'un script éprouvé ≠ copie versée, journal absent,
# journal sans son sceau exact, script attendu non éprouvé ; chaque fois S refait, puis journaux rétablis
preuve_alteree() {   # $1 commande qui altère les journaux versés (dans le dépôt) ; puis S refait
    eval "$1" && git add -A "$VERSEES" && git commit -qm "essai : preuves altérées" || { echo "preuves : altération impossible"; exit 2; }
    nouveau_s ""
}
retablir_preuves() { journaux_preuves && git add -A "$VERSEES" && git commit -qm "essai : preuves rétablies" && nouveau_s "" || { echo "preuves : rétablissement impossible"; exit 2; }; }
preuve_alteree "sed -i 's/cas non conformes : 0/cas non conformes : 1/' $VERSEES/banc-controles-notations-v1.log && (cd $VERSEES && sha256sum banc-controles-notations-v1.log > banc-controles-notations-v1.log.sha256)"
MOTIF_CAS="preuves des essais : journal banc-controles-notations-v1.log : dernière ligne" cas P30a-preuve-verdict-non-conforme 2 - FAUX_X=1
retablir_preuves
preuve_alteree "sed -i \"s/^script éprouvé : sceller_notations_v1.sh .*/script éprouvé : sceller_notations_v1.sh $(printf '7%.0s' {1..64})/\" $VERSEES/banc-scellement-notations-v1.log $VERSEES/repetition-finale-notations-v1.log && (cd $VERSEES && sha256sum banc-scellement-notations-v1.log > banc-scellement-notations-v1.log.sha256 && sha256sum repetition-finale-notations-v1.log > repetition-finale-notations-v1.log.sha256)"
MOTIF_CAS="preuves des essais : sceller_notations_v1.sh éprouvé" cas P30b-preuve-script-autre-que-la-copie 2 - FAUX_X=1
retablir_preuves
preuve_alteree "git rm -q $VERSEES/banc-surveillance-notations-v1.log $VERSEES/banc-surveillance-notations-v1.log.sha256"
MOTIF_CAS="preuves des essais : journal banc-surveillance-notations-v1.log absent de S" cas P30c-preuve-absente 2 - FAUX_X=1
retablir_preuves
preuve_alteree "echo ajout >> $VERSEES/banc-lanceur-notations-v1.log"
MOTIF_CAS="preuves des essais : sceau de banc-lanceur-notations-v1.log" cas P30d-preuve-sans-son-sceau 2 - FAUX_X=1
retablir_preuves
preuve_alteree "sed -i '/^script éprouvé : essais_surveillance_notations_v1.sh /d' $VERSEES/banc-surveillance-notations-v1.log && (cd $VERSEES && sha256sum banc-surveillance-notations-v1.log > banc-surveillance-notations-v1.log.sha256)"
MOTIF_CAS="≠ les dix attendus (manquants ['essais_surveillance_notations_v1.sh'])" cas P30e-preuve-script-non-eprouve 2 - FAUX_X=1
retablir_preuves
preuve_alteree "sed -i '1a Traceback (most recent call last): essai' $VERSEES/banc-controles-notations-v1.log && (cd $VERSEES && sha256sum banc-controles-notations-v1.log > banc-controles-notations-v1.log.sha256)"
MOTIF_CAS="preuves des essais : journal banc-controles-notations-v1.log : ligne d'échec avant le verdict" cas P30g-preuve-echec-non-compte 2 - FAUX_X=1
retablir_preuves
preuve_alteree "sed -i \"s/^script éprouvé : sceller_notations_v1.sh .*/script éprouvé : sceller_notations_v1.sh $(printf '8%.0s' {1..64})/\" $VERSEES/repetition-finale-notations-v1.log && (cd $VERSEES && sha256sum repetition-finale-notations-v1.log > repetition-finale-notations-v1.log.sha256)"
MOTIF_CAS="preuves des essais : sceller_notations_v1.sh éprouvé sous deux empreintes" cas P30h-preuve-deux-empreintes 2 - FAUX_X=1
retablir_preuves
preuve_alteree "sed -i '1a script éprouvé : Autre.sh abc' $VERSEES/banc-lanceur-notations-v1.log && (cd $VERSEES && sha256sum banc-lanceur-notations-v1.log > banc-lanceur-notations-v1.log.sha256)"
MOTIF_CAS="ligne « script éprouvé » mal formée" cas P30i-preuve-ligne-mal-formee 2 - FAUX_X=1
retablir_preuves
preuve_alteree "sed -i '/^script éprouvé : /d' $VERSEES/banc-surveillance-notations-v1.log && (cd $VERSEES && sha256sum banc-surveillance-notations-v1.log > banc-surveillance-notations-v1.log.sha256)"
MOTIF_CAS="journal banc-surveillance-notations-v1.log : aucune ligne « script éprouvé »" cas P30j-preuve-sans-ligne 2 - FAUX_X=1
retablir_preuves
MOTIF_CAS="preuves des essais : cinq journaux conformes ; 10 scripts éprouvés égaux à leurs copies versées à S" cas P30f-preuves-saines-apres-retablissement 0 - FAUX_X=1
# instances d'autres projets nommées en argument ; crédit exigé : 7,5 h × (1,10 + 4,004) + 1,2 = 39,48 USD
ARRETEES='{"id": 55292763, "actual_status": "exited", "cur_state": "stopped"}, {"id": 55458787, "actual_status": "exited", "cur_state": "stopped"}'
AUTRE='{"id": 55555587, "actual_status": "running", "cur_state": "running", "label": "autre-projet-essai", "dph_total": 4.004, "extra_env": [["GH_TOKEN", "secret"]]}'
AUTRE_ARRETEE='{"id": 55555587, "actual_status": "exited", "cur_state": "stopped", "label": "autre-projet-essai", "dph_total": 4.004}'
AUTRE_T05='{"id": 55555587, "actual_status": "running", "cur_state": "running", "label": "t05-notations-v1", "dph_total": 1.1}'
AUTRE_SANS_PRIX='{"id": 55555587, "actual_status": "running", "cur_state": "running", "label": "autre-x", "dph_total": null}'
MOTIF_CAS="instances d'autres projets tolérées : 55555587 (running, running, 4.004 USD/h, en marche, comptée)" cas V01-autre-projet-en-marche-tolere 0 "$E/traces 55555587" "FAUX_INSTANCES=[$ARRETEES, $AUTRE]" FAUX_CREDIT=39.48
MOTIF_CAS="autres instances sur le compte : 55555587 (running, running)" cas V02-autre-projet-non-declare 2 - "FAUX_INSTANCES=[$ARRETEES, $AUTRE]" FAUX_CREDIT=50
MOTIF_CAS="crédit insuffisant pour les notations et les autres projets en marche" cas V03-credit-insuffisant-avec-autre-projet 3 "$E/traces 55555587" "FAUX_INSTANCES=[$ARRETEES, $AUTRE]" FAUX_CREDIT=39.47
MOTIF_CAS="autres instances sur le compte : 55555587 (running, running)" cas V04-autre-projet-etiquette-t05 2 "$E/traces 55555587" "FAUX_INSTANCES=[$ARRETEES, $AUTRE_T05]" FAUX_CREDIT=50
MOTIF_CAS="AUTRES_PROJETS : identifiants d'instances" cas V05-autres-mal-forme 2 "$E/traces abc" FAUX_X=1
MOTIF_CAS="instances d'autres projets tolérées : aucune" cas V06-autre-declare-absent 0 "$E/traces 55555587" FAUX_X=1
MOTIF_CAS="55555587 (exited, stopped, 4.004 USD/h, arrêtée)" cas V07-autre-projet-arrete-non-compte 0 "$E/traces 55555587" "FAUX_INSTANCES=[$ARRETEES, $AUTRE_ARRETEE]" FAUX_CREDIT=9.45
MOTIF_CAS="autres instances sur le compte : 55555587 (prix illisible)" cas V08-autre-projet-sans-prix 2 "$E/traces 55555587" "FAUX_INSTANCES=[$ARRETEES, $AUTRE_SANS_PRIX]" FAUX_CREDIT=50
# v2 : choix de l'offre parmi les conformes relues après les contrôles ; prix nul, négatif, infini, booléen ou texte,
# 40 Go, deux cartes, identifiant booléen : écartés, même moins chers (LV-01, LV-04, LV-09)
MOTIF_CAS="offre choisie : 112 (1.05 USD/h), la moins chère des offres conformes" cas O01-moins-chere-des-conformes 0 - "FAUX_OFFRES=[$(off 111 1.10), $(off 112 1.05), $(off 113 1.20), $(off 114 0.80 "A100 SXM4" "Intel Xeon"), $(off 115 0.70 "A100 PCIE"), $(off 116 1.35), $(off 117 null), $(off true 0.5), $(off 118 true), $(off 121 '"0.9"'), $(off 122 0), $(off 123 -0.5), $(off 124 -Infinity), $(off 125 0.9 "A100 SXM4" "$EPYC" 40960), $(off 126 0.9 "A100 SXM4" "$EPYC" 81920 2), $(off 127 0.9 "A100 SXM4" "$EPYC" null), $(off 128 0.9 "A100 SXM4" "$EPYC" 81920 true), $(off 129 0.9 "A100 SXM4" "$EPYC" Infinity)]"
python3 - "$E/lancement-O01-moins-chere-des-conformes.txt" "$E/journal-O01-moins-chere-des-conformes.txt" "$E/traces/offres-relues.json" <<'EOF' \
    && echo "    O01 : offre créée 112 ; conformes dans l'ordre des prix (112, 111, 113), machine et hôte écrits et archivés ; 18 offres relues gardées : CONFORME" \
    || { echo "    O01 : offre créée, liste des conformes ou offres relues : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
import json, re, sys
t = open(sys.argv[1], encoding="utf-8").read(); j = open(sys.argv[2], encoding="utf-8").read()
l = [x for x in t.split("\n") if x.startswith("offres conformes relues : ")]
o = json.load(open(sys.argv[3].replace("offres-relues.json", "offre.json")))
ok = (len(l) == 1 and re.findall(r"(?:: |, )(\d+) \(", l[0]) == ["112", "111", "113"] and "machine 7100 ; hôte 8100" in l[0]
      and re.search(r"^offre créée 112$", j, re.M) and len(json.load(open(sys.argv[3]))) == 18
      and o.get("id") == 112 and o.get("machine_id") == 7100 and o.get("host_id") == 8100)
sys.exit(0 if ok else 1)
EOF
MOTIF_CAS="offre choisie : 119 (1.05 USD/h)" cas O02-egalite-de-prix-plus-petit-identifiant 0 - "FAUX_OFFRES=[$(off 120 1.05), $(off 119 1.05)]"
grep -qx "offre créée 119" "$E/journal-O02-egalite-de-prix-plus-petit-identifiant.txt" && echo "    O02 : offre créée 119 : CONFORME" \
    || { echo "    O02 : offre créée : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
MOTIF_CAS="aucune offre conforme au filtre du plan" cas O03-aucune-offre 3 - "FAUX_OFFRES=[]"
MOTIF_CAS="aucune offre conforme au filtre du plan" cas O04-seulement-au-dessus-du-devis 3 - "FAUX_OFFRES=[$(off 130 1.31)]"
python3 -c 'import json, sys; d = json.load(open(sys.argv[1])); sys.exit(0 if len(d) == 1 and d[0]["id"] == 130 else 1)' "$E/traces/offres-relues.json" 2>/dev/null \
    && echo "    O04 : offres relues gardées sans offre conforme (code 3) : CONFORME" \
    || { echo "    O04 : offres relues non gardées sur le chemin du code 3 : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
MOTIF_CAS="offres : identifiant en double" cas O11-identifiant-en-double 2 - "FAUX_OFFRES=[$(off 112 1.05), $(off 112 1.25)]"
MOTIF_CAS="offres : relecture impossible" cas O05-offres-illisibles 2 - "FAUX_OFFRES=pas du json"
[ -s "$E/traces/offres-relues-brut.txt" ] && echo "    O05 : réponse illisible gardée (offres-relues-brut.txt) : CONFORME" \
    || { echo "    O05 : réponse illisible non gardée : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
MOTIF_CAS="offres : relecture impossible" cas O06-offres-pas-une-liste 2 - 'FAUX_OFFRES={"id": 1}'
MOTIF_CAS="offre choisie : 140 (1.3 USD/h)" cas O07-prix-au-plafond-juste 0 - "FAUX_OFFRES=[$(off 140 1.30)]" FAUX_CREDIT=50
# crédit exigé avec l'offre choisie parmi plusieurs : 7,5 h × 1,04 + 1,2 = 9,00 USD (9,45 à 1,10) (LV-05)
MOTIF_CAS="minimum 9.00 USD (7.5 h)" cas O08-credit-calcule-sur-l-offre-choisie 0 - "FAUX_OFFRES=[$(off 111 1.10), $(off 112 1.04)]" FAUX_CREDIT=9.00
MOTIF_CAS="crédit insuffisant pour les notations" cas O08b-credit-juste-sous-le-minimum 3 - "FAUX_OFFRES=[$(off 111 1.10), $(off 112 1.04)]" FAUX_CREDIT=8.99
MOTIF_CAS="offre choisie illisible" cas O09-identifiant-negatif 2 - "FAUX_OFFRES=[$(off -9 1.05)]"
MOTIF_CAS="aucune offre conforme au filtre du plan" cas O10-carte-de-40-go 3 - "FAUX_OFFRES=[$(off 150 0.9 "A100 SXM4" "$EPYC" 40960)]"
# dossier de traces purement numérique (habitude du v1) ; forme du v1 à trois arguments (LV-18)
MOTIF_CAS="DOSSIER_TRACES purement numérique" cas A01-traces-numeriques 2 "$E/29296808 -" FAUX_X=1
MOTIF_CAS="usage" cas A02-forme-du-v1-a-trois-arguments 2 "29296808 $E/traces -" FAUX_X=1
# v2 : preuve du banc v2 versée au commit C3 (chaque fois C3 refait, puis rétabli)
v3_altere() {   # $1 commande qui altère une copie du dossier v3 (variable $X), puis C3 refait sur cette copie
    rm -rf "$E/v3-altere" && cp -r "$E/v3-sauve" "$E/v3-altere" && X="$E/v3-altere" && eval "$1" && nouveau_c3 "$E/v3-altere" \
        || { echo "v3 : altération impossible"; exit 2; }
}
v3_altere 'rm "$X/banc-lanceur-notations-v2.log" "$X/banc-lanceur-notations-v2.log.sha256"'
MOTIF_CAS="preuves des essais : journal banc-lanceur-notations-v2.log absent de C3" cas Q01-journal-v2-absent 2 - FAUX_X=1
v3_altere 'sed -i "s/cas non conformes : 0/cas non conformes : 1/" "$X/banc-lanceur-notations-v2.log" && sceller_v3 "$X"'
MOTIF_CAS="journal du banc v2 : dernière ligne non conforme" cas Q02-journal-v2-verdict 2 - FAUX_X=1
v3_altere 'sed -i "s/^script éprouvé : lancer_notations_v2.sh .*/script éprouvé : lancer_notations_v2.sh $(printf "7%.0s" {1..64})/" "$X/banc-lanceur-notations-v2.log" && sceller_v3 "$X"'
MOTIF_CAS="journal du banc v2 : lancer_notations_v2.sh éprouvé sous 7777" cas Q03-journal-v2-autre-empreinte 2 - FAUX_X=1
v3_altere 'sed -i "1a Traceback (most recent call last): essai" "$X/banc-lanceur-notations-v2.log" && sceller_v3 "$X"'
MOTIF_CAS="journal du banc v2 : ligne d'échec avant le verdict" cas Q04-journal-v2-echec-non-compte 2 - FAUX_X=1
v3_altere 'echo ajout >> "$X/banc-lanceur-notations-v2.log"'
MOTIF_CAS="preuves des essais : sceau de banc-lanceur-notations-v2.log absent ou non conforme à C3" cas Q05-journal-v2-sans-son-sceau 2 - FAUX_X=1
v3_altere 'echo "# ajout" >> "$X/essais_lanceur_notations_v2.sh"'
MOTIF_CAS="essais_lanceur_notations_v2.sh : copie versée à C3 sans son sceau exact" cas Q06-banc-v2-sans-son-sceau 2 - FAUX_X=1
v3_altere 'echo "# ajout" >> "$X/lancer_notations_v2.sh" && sceller_v3 "$X"'
MOTIF_CAS="lancer_notations_v2.sh exécuté ≠ copie versée au commit C3" cas Q07-copie-versee-autre-que-l-execute 2 - FAUX_X=1
nouveau_c3
AVANT_Q08=$(git -C "$E/distant.git" rev-parse refs/heads/main)
S_COURANT=$(git -C "$E/depot" log --diff-filter=A -1 --format=%H -- "$P.sha256")
git -C "$E/distant.git" update-ref refs/heads/main "$S_COURANT"
MOTIF_CAS="commit C3 du lanceur v2 non descendant de S" cas Q08b-c3-anterieur-a-s 2 - FAUX_X=1
git -C "$E/distant.git" update-ref refs/heads/main "$AVANT_Q08"; git -C "$E/depot" fetch -q origin
MOTIF_CAS="preuve du banc du lanceur v2 : conforme" cas Q09-sain-apres-retablissement 0 - FAUX_X=1
v3_altere 'sed -i "1a script éprouvé : Autre.sh abc" "$X/banc-lanceur-notations-v2.log" && sceller_v3 "$X"'
MOTIF_CAS="ligne « script éprouvé » mal formée ou en double" cas Q10-journal-v2-ligne-mal-formee 2 - FAUX_X=1
v3_altere 'sed -i "1a script éprouvé : lancer_notations_v2.sh $(printf "6%.0s" {1..64})" "$X/banc-lanceur-notations-v2.log" && sceller_v3 "$X"'
MOTIF_CAS="ligne « script éprouvé » mal formée ou en double" cas Q11-journal-v2-deux-empreintes 2 - FAUX_X=1
v3_altere 'cp "$X/banc-lanceur-notations-v2.log" "$E/journal-ancien.log" && echo "# ajout" >> "$X/essais_lanceur_notations_v2.sh" && sceller_v3 "$X" && cp "$E/journal-ancien.log" "$X/banc-lanceur-notations-v2.log" && sceller_v3 "$X"'
MOTIF_CAS="journal du banc v2 : essais_lanceur_notations_v2.sh éprouvé sous" cas Q12-banc-v2-rescelle-journal-ancien 2 - FAUX_X=1
v3_altere 'echo "$(printf "0%.0s" {1..64})  lancer_notations_v2.sh" > "$X/lancer_notations_v2.sh.sha256"'
MOTIF_CAS="lancer_notations_v2.sh : copie versée à C3 sans son sceau exact" cas Q13-sceau-du-lanceur-faux 2 - FAUX_X=1
v3_altere 'sed -i "/^script éprouvé : verifications_notations_v1.py /d" "$X/banc-lanceur-notations-v2.log" && sceller_v3 "$X"'
MOTIF_CAS="≠ les trois attendus" cas Q14-journal-v2-sans-le-module-commun 2 - FAUX_X=1
v3_altere 'sed -i "s/^script éprouvé : verifications_notations_v1.py .*/script éprouvé : verifications_notations_v1.py $(printf "5%.0s" {1..64})/" "$X/banc-lanceur-notations-v2.log" && sceller_v3 "$X"'
MOTIF_CAS="journal du banc v2 : verifications_notations_v1.py éprouvé sous 5555" cas Q15-module-commun-autre-empreinte 2 - FAUX_X=1
git rm -q -r "$VERSEES3" && git commit -qm "essai : retrait du v3" && mkdir -p "$VERSEES3" && cp "$E/v3-sauve"/* "$VERSEES3/" \
    && echo autre > registres/autre-essai.txt && git add "$VERSEES3" registres/autre-essai.txt && git commit -qm "essai : C3 avec un autre fichier" \
    && git push -q origin HEAD:main && git fetch -q origin || { echo "Q16 : préparation impossible"; exit 2; }
MOTIF_CAS="commit C3 : fichiers hors de" cas Q16-c3-touche-un-autre-fichier 2 - FAUX_X=1
git rm -q registres/autre-essai.txt && git commit -qm "essai : retrait" && nouveau_c3
echo deplace > "$VERSEES/deplace-essai.txt" && git add "$VERSEES/deplace-essai.txt" && git commit -qm "essai : fichier du v2 à déplacer" \
    && git rm -q -r "$VERSEES3" && git commit -qm "essai : retrait du v3" && mkdir -p "$VERSEES3" && cp "$E/v3-sauve"/* "$VERSEES3/" \
    && git mv "$VERSEES/deplace-essai.txt" "$VERSEES3/deplace-essai.txt" && git add "$VERSEES3" \
    && git commit -qm "essai : C3 qui déplace un fichier du v2" && git push -q origin HEAD:main && git fetch -q origin \
    || { echo "Q16b : préparation impossible"; exit 2; }
MOTIF_CAS="commit C3 : fichiers hors de" cas Q16b-c3-deplace-un-fichier-du-v2 2 - FAUX_X=1
git rm -q "$VERSEES3/deplace-essai.txt" && git commit -qm "essai : retrait" && nouveau_c3
echo "# version suivante" >> "$VERSEES3/lancer_notations_v2.sh" && git add "$VERSEES3" && git commit -qm "essai : version suivante sans sceau" \
    && git push -q origin HEAD:main && git fetch -q origin || { echo "Q17 : préparation impossible"; exit 2; }
MOTIF_CAS="lancer_notations_v2.sh exécuté ≠ copie au sommet du dépôt distant" cas Q17-sommet-du-distant-autre 2 - FAUX_X=1
nouveau_c3
v3_altere 'sed -i "s/^PRIX_MAX=1.30 /PRIX_MAX=1.40 /" "$X/lancer_notations_v2.sh" && cmp -s "$X/lancer_notations_v2.sh" "$E/v3-sauve/lancer_notations_v2.sh" && exit 2; journal_v2 "$X" && sceller_v3 "$X"'
L_SAUVE=$L; L=$E/v3-altere/lancer_notations_v2.sh
MOTIF_CAS="constante PRIX_MAX du lanceur v2 ≠ celle du lanceur v1 versé à S" cas K01-constante-du-devis-autre 2 - FAUX_X=1
L=$L_SAUVE
for k in "K02-heures-credit|HEURES_CREDIT|s/^HEURES_CREDIT=7.5 /HEURES_CREDIT=8.0 /" "K03-plafond-go|PLAFOND_GO|s/^PLAFOND_GO=10.5 /PLAFOND_GO=11.5 /" \
         "K04-plafond-surveillance|PLAFOND_SURVEILLANCE_S|s/^PLAFOND_SURVEILLANCE_S=26400 /PLAFOND_SURVEILLANCE_S=27000 /" \
         "K05-filtre|FILTRE|s/^FILTRE=\"gpu_name=A100_SXM4 /FILTRE=\"gpu_name=A100_PCIE /" \
         "K06-arretees-tolerees|ARRETEES_TOLEREES|s/^ARRETEES_TOLEREES=\"55292763 /ARRETEES_TOLEREES=\"55292764 /"; do
    NOM=${k%%|*}; RESTE=${k#*|}; CONST=${RESTE%%|*}; SED=${RESTE#*|}
    v3_altere 'sed -i "$SED" "$X/lancer_notations_v2.sh" && cmp -s "$X/lancer_notations_v2.sh" "$E/v3-sauve/lancer_notations_v2.sh" && exit 2; journal_v2 "$X" && sceller_v3 "$X"'
    L=$E/v3-altere/lancer_notations_v2.sh
    MOTIF_CAS="constante $CONST du lanceur v2 ≠ celle du lanceur v1 versé à S" cas "$NOM" 2 - FAUX_X=1
    L=$L_SAUVE
done
nouveau_c3
MOTIF_CAS="preuve du banc du lanceur v2 : conforme" cas Q18-sain-apres-retablissement 0 - FAUX_X=1
# jeton affiché : compté (vérification courte de la chaîne, constat 2)
FUITES=$(grep -l 'secret\|factice-hf\|factice-gh' "$E"/sortie-*.txt "$E"/lancement-*.txt "$E"/journal-*.txt 2>/dev/null || true)
[ -z "$FUITES" ] && echo "aucun jeton affiché : CONFORME" || { printf '%s\n' $FUITES | sed 's/^/JETON AFFICHÉ : /'; NON_CONFORMES=$((NON_CONFORMES + 1)); }
echo "FIN DU BANC DU LANCEUR V2 DES NOTATIONS ; cas non conformes : $NON_CONFORMES"
[ "$NON_CONFORMES" = 0 ] || exit 1
