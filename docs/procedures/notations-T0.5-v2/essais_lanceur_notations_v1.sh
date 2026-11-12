#!/usr/bin/env bash
# Banc du lanceur des notations refaites du pilote de T0.5 (R5), décliné des bancs v1 et v2 du lanceur du pilote : un
# cas sain et un artefact par garde, plus les gardes propres aux notations (décision de Lazar sur N-021 à la forme
# exacte ; relance consignée « relancement », « notations », « infrastructure » ; instance du pilote 55538944 tolérée
# arrêtée ; crédit sur 7,5 heures ; plafond de la surveillance écrit à la création + 26 400 s ; étiquette et variables de
# l'amorce des notations, sans ETUDE ; treize scripts de la chaîne égaux à leurs copies versées à S). Aucun appel réel n'est
# possible : faux outil de location (n'appelle aucun service ; journalise le verbe, l'étiquette et les variables non
# secrètes de --env, jamais un jeton), faux contrôles, HOME redirigé, clé d'API retirée, jetons factices. Dépôt
# synthétique : préenregistrement minimal (empreinte de l'amorce, décision sur N-021, ligne « Lancement »), registre des
# décisions (colonne d'état de N-021 à la forme exacte), registre des GO et garde de calcul du dépôt, copies versées des
# faux contrôles et du lanceur (celle du banc) ; dépôt nu local en guise de dépôt distant.
# Usage : essais_lanceur_notations_v1.sh RACINE_NEUVE
set -uo pipefail
E=$(realpath -m "${1:?racine neuve}")
BN=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
HN=${HN:-$BN/notations-v1}
D=/home/user/controle-ia-travail
P=prereg/T0.5-pilote-notations-v1.md
VERSEES=docs/procedures/notations-T0.5-v2
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
echo "script éprouvé : lancer_notations_v1.sh $(sha256sum "$HN/lancer_notations_v1.sh" | cut -d' ' -f1)"
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
  "search offers") printf '[{"id": 111, "gpu_name": "%s", "dph_total": %s, "cpu_name": "%s", "cpu_arch": "amd64", "cpu_cores": 128}, {"id": 222, "dph_total": 0.9, "cpu_name": "AMD EPYC 7513 32-Core Processor"}]\n' "${FAUX_GPU:-A100 SXM4}" "${FAUX_PRIX:-1.10}" "${FAUX_CPU:-AMD EPYC 7513 32-Core Processor}" ;;
  "show user") printf '{"credit": %s, "email": "x@invalid"}\n' "${FAUX_CREDIT:-20.0}" ;;
  "show instances") [ -n "${FAUX_INSTANCES_ECHEC:-}" ] && { echo "erreur factice" >&2; exit 1; }; d='[{"id": 55292763, "actual_status": "exited", "cur_state": "stopped", "extra_env": [["GH_TOKEN", "secret"]]}, {"id": 55458787, "actual_status": "exited", "cur_state": "stopped"}, {"id": 55538944, "actual_status": "exited", "cur_state": "stopped", "label": "t05-pilote-v1"}]'; printf '%s\n' "${FAUX_INSTANCES:-$d}" ;;
  "create instance")
    echo "CREATION FACTICE" >> "$J"
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
L=$E/B/notations-v1/lancer_notations_v1.sh
sed -e "s|^DEPOT=.*|DEPOT=$E/depot|" -e "s|^B=.*|B=$E/B|" "$HN/lancer_notations_v1.sh" > "$L"
echo "lignes changées dans la copie du lanceur : $(diff "$HN/lancer_notations_v1.sh" "$L" | grep -c '^>')"
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
cp "$E/B/notations-v1/controles_avant_depense_notations_v1.sh" "$E/B/notations-v1/verifications_notations_v1.py" "$L" "$VERSEES/"
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
git clone -q --bare . "$E/distant.git" && git remote add origin "$E/distant.git" && git fetch -q origin
cp registres/decisions.md "$E/decisions-sauve.md"; cp registres/go.md "$E/go-sauve.md"
cas() {   # $1 nom ; $2 code attendu ; $3 arguments du lanceur (« - » : les arguments normaux) ; puis l'environnement
    local nom=$1 attendu=$2 args=$3; shift 3
    rm -rf "$E/traces" "$E/compteur-heure"; : > "$E/journal-$nom.txt"
    local a=(111 "$E/traces" -); [ "$args" = "-" ] || read -r -a a <<<"$args"
    env -u VAST_API_KEY HOME="$E/home" PATH="$E/bin-heure:$E/bin-df:/usr/bin:/bin" \
        HF_TOKEN=factice-hf-0000000 CONTROLE_IA_GITHUB_TOKEN=factice-gh-0000000 FAUX_VASTAI_JOURNAL="$E/journal-$nom.txt" \
        "$@" bash "$L" "${a[@]}" > "$E/sortie-$nom.txt" 2>&1
    local c=$?
    local cree; cree=$(grep -c "CREATION FACTICE" "$E/journal-$nom.txt")
    local v="CONFORME"; [ "$c" = "$attendu" ] || v="NON CONFORME (attendu $attendu)"
    [ "$attendu" != 0 ] && [ "$cree" != 0 ] && [ "$attendu" != 4 ] && v="NON CONFORME (création alors qu'un arrêt était attendu)"
    [ "$attendu" = 0 ] && [ "$cree" != 1 ] && v="NON CONFORME (pas de création)"
    { [ -e "$E/traces/clone-controles" ] || [ -e "$E/traces/clone-controles.travail" ]; } && v="NON CONFORME (clone des contrôles resté)"
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
cas P07-offre-sans-prix 2 - FAUX_PRIX=null
cas P07b-prix-au-dessus-du-devis 3 - FAUX_PRIX=1.35
cas P07c-processeur-autre 2 - 'FAUX_CPU=Intel Xeon Platinum 8480+'
cas P07d-processeur-voisin 2 - 'FAUX_CPU=AMD EPYC 7513'
cas P07e-carte-pcie 2 - 'FAUX_GPU=A100 PCIE'
# crédit exigé : 7,5 h × 1,10 + 1,2 = 9,45 USD
MOTIF_CAS="crédit insuffisant pour les notations" cas P08-credit-insuffisant 3 - FAUX_CREDIT=9.44
MOTIF_CAS="minimum 9.45 USD (7.5 h)" cas P08b-credit-juste 0 - FAUX_CREDIT=9.45
cas P09-jeton-hf-absent 2 - HF_TOKEN=
cas P09b-jeton-github-absent 2 - CONTROLE_IA_GITHUB_TOKEN=
cas P10-argument-absent 2 "111" FAUX_X=1
cas P10b-relance-sans-cause 2 "111 $E/traces - relance" FAUX_X=1
MOTIF_CAS="usage" cas P10c-relance-sans-releve 2 "111 $E/traces - relance R-151" FAUX_X=1
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
MOTIF_CAS="relance non consignée" cas P13-relance-non-consignee 2 "111 $E/traces - relance R-151 $E/releve-sain.txt" FAUX_X=1
echo "| R-151 | 2026-10-12 | Notations : panne réseau de l'hôte (essai). | essai |" >> registres/decisions.md
MOTIF_CAS="relance non consignée" cas P13b-relance-cause-sans-infrastructure 2 "111 $E/traces - relance R-151 $E/releve-sain.txt" FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
echo "| R-151 | 2026-10-12 | Relancement du pilote : cause d'infrastructure (panne réseau de l'hôte, instance 12345678 arrêtée, essai). | essai |" >> registres/decisions.md
MOTIF_CAS="relance non consignée" cas P13g-relance-du-pilote-et-non-des-notations 2 "111 $E/traces - relance R-151 $E/releve-sain.txt" FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
echo "| R-151 | 2026-10-12 | Relancement des notations : cause d'infrastructure (panne réseau de l'hôte, dépense engagée 1,00 USD, essai). | essai |" >> registres/decisions.md
MOTIF_CAS="ne nomme pas, une seule fois, l'instance du premier lancement" cas P13d-relance-sans-instance-nommee 2 "111 $E/traces - relance R-151 $E/releve-sain.txt" FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
echo "| R-151 | 2026-10-12 | Relancement des notations : cause d'infrastructure (panne réseau de l'hôte, instance 12345678 arrêtée, essai). | essai |" >> registres/decisions.md
MOTIF_CAS="« dépense engagée X,XX USD »" cas P13k-relance-sans-depense-engagee 2 "111 $E/traces - relance R-151 $E/releve-sain.txt" FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
echo "| R-151 | 2026-10-12 | Relancement des notations : cause d'infrastructure (panne réseau de l'hôte, instance 12345678 arrêtée, dépense engagée 1,00 USD, essai). | essai |" >> registres/decisions.md
cas P13c-relance-saine 0 "111 $E/traces - relance R-151 $E/releve-sain.txt" 'FAUX_INSTANCES=[{"id": 55292763, "actual_status": "exited", "cur_state": "stopped"}, {"id": 12345678, "actual_status": "exited", "cur_state": "stopped"}]'
cas P13e-relance-premiere-en-marche 2 "111 $E/traces - relance R-151 $E/releve-sain.txt" 'FAUX_INSTANCES=[{"id": 12345678, "actual_status": "running", "cur_state": "running"}]'
(cd "$E" && cas P13f-traces-en-chemin-relatif 0 "111 traces-relatives - relance R-151 $E/releve-sain.txt" 'FAUX_INSTANCES=[]')
grep -E "etiquette|env BRANCHE" "$E/journal-P13c-relance-saine.txt" | sed 's/^/    > /'
# relance : étiquette et branche exactes, comptées (vérification courte de la chaîne, second tour, constat 3)
if grep -qx "etiquette t05-notations-v1-relance" "$E/journal-P13c-relance-saine.txt" \
    && grep -qx "env BRANCHE=calcul/t05-notations-reel-v2" "$E/journal-P13c-relance-saine.txt" \
    && grep -qx "branche calcul/t05-notations-reel-v2" "$E/lancement-P13c-relance-saine.txt"; then
    echo "    P13c : étiquette t05-notations-v1-relance et branche calcul/t05-notations-reel-v2 : CONFORME"
else echo "    P13c : étiquette ou branche de la relance : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); fi
# relevé cumulatif du premier lancement (préséance) ; plafond de GO-2026-10-12-02 : 1,00 + 7,5 × 1,10 + 0,5 = 9,75 USD
verser_releve "$E/releve-fin.txt"
MOTIF_CAS="un juge a fini, ou peut avoir fini, au premier lancement" cas P13h-releve-avec-fin-de-juge 2 "111 $E/traces - relance R-151 $E/releve-fin.txt" 'FAUX_INSTANCES=[]'
verser_releve "$E/releve-dernier-lot.txt"
MOTIF_CAS="peut avoir fini, au premier lancement (PROGRES 2026-10-13T11:19:00Z juge=8B lot=23/23" cas P13o-releve-avec-dernier-lot 2 "111 $E/traces - relance R-151 $E/releve-dernier-lot.txt" 'FAUX_INSTANCES=[]'
verser_releve "$E/releve-lot-2-sur-23.txt"
MOTIF_CAS="relevé du premier lancement : aucune fin de juge" cas P13p-releve-lot-2-sur-23-sain 0 "111 $E/traces - relance R-151 $E/releve-lot-2-sur-23.txt" 'FAUX_INSTANCES=[]'
MOTIF_CAS="relevé passé en argument ≠ copie versée" cas P13i-releve-absent 2 "111 $E/traces - relance R-151 $E/releve-absent.txt" 'FAUX_INSTANCES=[]'
verser_releve "$E/releve-sans-amorce.txt"
MOTIF_CAS="sans ligne « AMORCE … : commit » du commit de scellement" cas P13j-releve-sans-amorce 2 "111 $E/traces - relance R-151 $E/releve-sans-amorce.txt" 'FAUX_INSTANCES=[]'
sed "s/: commit $S/: commit $(printf '0%.0s' {1..40})/" "$E/releve-sain.txt" > "$E/releve-autre-commit.txt"; verser_releve "$E/releve-autre-commit.txt"
MOTIF_CAS="sans ligne « AMORCE … : commit » du commit de scellement" cas P13s-releve-d-un-autre-commit 2 "111 $E/traces - relance R-151 $E/releve-autre-commit.txt" 'FAUX_INSTANCES=[]'
verser_releve "$E/releve-sain.txt"; echo "0000  releve-cumulatif.txt" > traces/t05-notations-releve-12345678/releve-cumulatif.txt.sha256; git add traces && git commit -qm "essai : sceau du relevé faussé"
MOTIF_CAS="relevé du premier lancement : sceau absent ou non conforme" cas P13r-releve-au-sceau-faux 2 "111 $E/traces - relance R-151 $E/releve-sain.txt" 'FAUX_INSTANCES=[]'
git rm -q -r traces/t05-notations-releve-12345678 && git commit -qm "essai : relevé retiré"
MOTIF_CAS="relevé du premier lancement non versé au dépôt" cas P13q-releve-non-verse 2 "111 $E/traces - relance R-151 $E/releve-sain.txt" 'FAUX_INSTANCES=[]'
verser_releve "$E/releve-sain.txt"
MOTIF_CAS="= 9.75 USD (au plus 10.5)" cas P13m-relance-dans-le-plafond 0 "111 $E/traces - relance R-151 $E/releve-sain.txt" 'FAUX_INSTANCES=[]'
cp "$E/decisions-sauve.md" registres/decisions.md
echo "| R-151 | 2026-10-12 | Relancement des notations : cause d'infrastructure (panne réseau de l'hôte, instance 12345678 arrêtée, dépense engagée 2,00 USD, essai). | essai |" >> registres/decisions.md
MOTIF_CAS="relancement hors du plafond de GO-2026-10-12-02" cas P13l-relance-hors-plafond 3 "111 $E/traces - relance R-151 $E/releve-sain.txt" 'FAUX_INSTANCES=[]'
cp "$E/decisions-sauve.md" registres/decisions.md
echo "| R-151 | 2026-10-12 | Relancement des notations : cause d'infrastructure (panne réseau de l'hôte, instance 12345678 arrêtée, dépense engagée 1,75 USD, essai). | essai |" >> registres/decisions.md
MOTIF_CAS="= 10.50 USD (au plus 10.5)" cas P13n-relance-au-plafond-juste 0 "111 $E/traces - relance R-151 $E/releve-sain.txt" 'FAUX_INSTANCES=[]'
cp "$E/decisions-sauve.md" registres/decisions.md
cp "$E/B/notations-v1/controles_avant_depense_notations_v1.sh" "$E/ctl-sauve.sh"
echo "# modifié" >> "$E/B/notations-v1/controles_avant_depense_notations_v1.sh"
MOTIF_CAS="controles_avant_depense_notations_v1.sh exécuté ≠ copie versée au commit S" cas P14-controles-non-verses 2 - FAUX_X=1
cp "$E/ctl-sauve.sh" "$E/B/notations-v1/controles_avant_depense_notations_v1.sh"
cp "$E/B/notations-v1/surveiller_notations_v1.sh" "$E/surv-sauve.sh"; echo "# modifié" >> "$E/B/notations-v1/surveiller_notations_v1.sh"
MOTIF_CAS="surveiller_notations_v1.sh exécuté ≠ copie versée au commit S" cas P31-surveillance-non-versee 2 - FAUX_X=1
cp "$E/surv-sauve.sh" "$E/B/notations-v1/surveiller_notations_v1.sh"
cp "$L" "$E/lanceur-sauve.sh"; echo "# modifié" >> "$L"
MOTIF_CAS="lancer_notations_v1.sh exécuté ≠ copie versée au commit S" cas P14b-lanceur-non-verse 2 - FAUX_X=1
cp "$E/lanceur-sauve.sh" "$L"
git -C "$E/distant.git" update-ref refs/heads/main "$(git -C "$E/depot" rev-parse "$S~1")"
MOTIF_CAS="absent du dépôt distant" cas P15-s-absent-du-distant 2 - FAUX_X=1
git -C "$E/distant.git" update-ref refs/heads/main "$S"
git -C "$E/depot" fetch -q origin
cas P16-sain-rejoue 0 - FAUX_X=1
cp "$E/B/notations-v1/verifications_notations_v1.py" "$E/verif-sauve.py"; echo "# modifié" >> "$E/B/notations-v1/verifications_notations_v1.py"
MOTIF_CAS="verifications_notations_v1.py exécuté ≠ copie versée au commit S" cas P14c-module-commun-non-verse 2 - FAUX_X=1
cp "$E/verif-sauve.py" "$E/B/notations-v1/verifications_notations_v1.py"
MOTIF_CAS="contrôles : dernière ligne inattendue" cas N07-controles-derniere-ligne-autre 2 - FAUX_DERNIERE=1
mkdir -p "$E/traces-existantes"
MOTIF_CAS="existe déjà (R12)" cas N05-traces-existantes 2 "111 $E/traces-existantes -" FAUX_X=1
MOTIF_CAS="offre 333 absente des offres conformes" cas N06-offre-absente 2 "333 $E/traces -" FAUX_X=1
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
MOTIF_CAS="instances d'autres projets tolérées : 55555587 (running, running, 4.004 USD/h, en marche, comptée)" cas V01-autre-projet-en-marche-tolere 0 "111 $E/traces 55555587" "FAUX_INSTANCES=[$ARRETEES, $AUTRE]" FAUX_CREDIT=39.48
MOTIF_CAS="autres instances sur le compte : 55555587 (running, running)" cas V02-autre-projet-non-declare 2 - "FAUX_INSTANCES=[$ARRETEES, $AUTRE]" FAUX_CREDIT=50
MOTIF_CAS="crédit insuffisant pour les notations et les autres projets en marche" cas V03-credit-insuffisant-avec-autre-projet 3 "111 $E/traces 55555587" "FAUX_INSTANCES=[$ARRETEES, $AUTRE]" FAUX_CREDIT=39.47
MOTIF_CAS="autres instances sur le compte : 55555587 (running, running)" cas V04-autre-projet-etiquette-t05 2 "111 $E/traces 55555587" "FAUX_INSTANCES=[$ARRETEES, $AUTRE_T05]" FAUX_CREDIT=50
MOTIF_CAS="AUTRES_PROJETS : identifiants d'instances" cas V05-autres-mal-forme 2 "111 $E/traces abc" FAUX_X=1
MOTIF_CAS="instances d'autres projets tolérées : aucune" cas V06-autre-declare-absent 0 "111 $E/traces 55555587" FAUX_X=1
MOTIF_CAS="55555587 (exited, stopped, 4.004 USD/h, arrêtée)" cas V07-autre-projet-arrete-non-compte 0 "111 $E/traces 55555587" "FAUX_INSTANCES=[$ARRETEES, $AUTRE_ARRETEE]" FAUX_CREDIT=9.45
MOTIF_CAS="autres instances sur le compte : 55555587 (prix illisible)" cas V08-autre-projet-sans-prix 2 "111 $E/traces 55555587" "FAUX_INSTANCES=[$ARRETEES, $AUTRE_SANS_PRIX]" FAUX_CREDIT=50
# jeton affiché : compté (vérification courte de la chaîne, constat 2)
FUITES=$(grep -l 'secret\|factice-hf\|factice-gh' "$E"/sortie-*.txt "$E"/lancement-*.txt "$E"/journal-*.txt 2>/dev/null || true)
[ -z "$FUITES" ] && echo "aucun jeton affiché : CONFORME" || { printf '%s\n' $FUITES | sed 's/^/JETON AFFICHÉ : /'; NON_CONFORMES=$((NON_CONFORMES + 1)); }
echo "FIN DU BANC DU LANCEUR DES NOTATIONS ; cas non conformes : $NON_CONFORMES"
[ "$NON_CONFORMES" = 0 ] || exit 1
