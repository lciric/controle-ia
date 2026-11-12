#!/usr/bin/env bash
# Banc du lanceur des notations refaites du pilote de T0.5 (R5), décliné des bancs v1 et v2 du lanceur du pilote : un
# cas sain et un artefact par garde, plus les gardes propres aux notations (décision de Lazar sur N-021 à la forme
# exacte ; relance consignée « relancement », « notations », « infrastructure » ; instance du pilote 55538944 tolérée
# arrêtée ; crédit sur 7,5 heures ; base de la surveillance à la création + 4 800 s ; étiquette et variables de
# l'amorce des notations, sans ETUDE ; lanceur et contrôles égaux à leurs copies versées à S). Aucun appel réel n'est
# possible : faux outil de location (n'appelle aucun service ; journalise le verbe, l'étiquette et les variables non
# secrètes de --env, jamais un jeton), faux contrôles, HOME redirigé, clé d'API retirée, jetons factices. Dépôt
# synthétique : préenregistrement minimal (empreinte de l'amorce, décision sur N-021, ligne « Lancement »), registre des
# décisions (colonne d'état de N-021 à la forme exacte), registre des GO et garde de calcul du dépôt, copies versées des
# faux contrôles et du lanceur (celle du banc) ; dépôt nu local en guise de dépôt distant.
# Usage : essais_lanceur_notations_v1.sh RACINE_NEUVE
set -uo pipefail
E=$1
BN=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
HN=${HN:-$BN/notations-v1}
D=/home/user/controle-ia-travail
P=prereg/T0.5-pilote-notations-v1.md
VERSEES=docs/procedures/notations-T0.5-v1
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
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
echo "OK  essai"; echo "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES"
EOF
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
cp "$E/B/notations-v1/controles_avant_depense_notations_v1.sh" "$L" "$VERSEES/"
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
    echo "$nom : code $c ; créations factices $cree ; $v"
    grep -v '^$' "$E/sortie-$nom.txt" | tail -2 | sed 's/^/    | /' | cut -c1-200
    [ -f "$E/traces/lancement.txt" ] && cp "$E/traces/lancement.txt" "$E/lancement-$nom.txt"
}
cas P00-sain 0 - FAUX_X=1
grep -E "etiquette|env " "$E/journal-P00-sain.txt" | sed 's/^/    > /'
python3 - "$E/lancement-P00-sain.txt" "$E/journal-P00-sain.txt" <<'EOF'
import re, sys
t = open(sys.argv[1], encoding="utf-8").read(); j = open(sys.argv[2], encoding="utf-8").read()
c = int(re.search(r"^creation (\d+)$", t, re.M).group(1)); b = int(re.search(r"^base de la surveillance (\d+) ", t, re.M).group(1))
print("    > base de la surveillance = création + 4 800 s :", b - c == 4800, "; plafond de la surveillance (base + 6 h) = création + 26 400 s :",
      b + 6 * 3600 - c == 26400, "; branche v1 :", "branche calcul/t05-notations-reel-v1" in t,
      "; étiquette :", "etiquette t05-notations-v1" in j, "; ETUDE absente :", "env ETUDE=" not in j,
      "; instances arrêtées tolérées (dont 55538944) :", "55538944 (exited, stopped)" in t)
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
MOTIF_CAS="GO-2026-10-12-99 révoqué dans le registre courant" cas P17-go-n021-revoque 2 - FAUX_X=1
cp "$E/go-sauve.md" registres/go.md
echo "| GO-2026-10-12-97 | 2026-10-12 | révocation | révoque GO-2026-10-04-08 (essai) | — | — | Lazar | essai |" >> registres/go.md
MOTIF_CAS="GO-2026-10-04-08 révoqué dans le registre courant" cas P17b-go-calcul-revoque 2 - FAUX_X=1
cp "$E/go-sauve.md" registres/go.md
echo "| GO-2026-10-12-98 | 2026-10-12 | révocation de GO-2026-10-12-99 (essai) |" >> registres/go.md
MOTIF_CAS="GO-2026-10-12-99 révoqué dans le registre courant" cas P17h-go-revoque-ligne-mal-formee 2 - FAUX_X=1
cp "$E/go-sauve.md" registres/go.md
echo "| GO-2026-10-12-97 | 2026-10-12 | revendication | essai : aucune révocation de GO-2026-10-12-99 | — | — | Lazar | essai |" >> registres/go.md
cas P17i-ligne-go-qui-mentionne-une-revocation 0 - FAUX_X=1
cp "$E/go-sauve.md" registres/go.md
sed -i '/^| GO-2026-10-12-99 |/d' registres/go.md
MOTIF_CAS="GO-2026-10-12-99 : absent du registre courant, ou d'un autre type" cas P17c-go-absent-du-registre 2 - FAUX_X=1
cp "$E/go-sauve.md" registres/go.md
sed -i 's/| tranché (a) par Lazar : GO-2026-10-12-99 (R-146) |$/| tranché (a) par Lazar : GO-2026-10-12-98 (R-146) |/' registres/decisions.md
MOTIF_CAS="N-021 : la colonne d'état courante n'est pas" cas P17d-n021-autre-go 2 - FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
sed -i 's/| tranché (a) par Lazar : GO-2026-10-12-99 (R-146) |$/| tranché (a) par Lazar : GO-2026-10-12-99 (R-147) |/' registres/decisions.md
MOTIF_CAS="N-021 : la colonne d'état courante n'est pas" cas P17e-n021-autre-registre 2 - FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
sed -i '/^| R-146 |/d' registres/decisions.md
MOTIF_CAS="R-146 : absent du registre courant, en double" cas P17f-registre-du-go-absent 2 - FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
sed -i 's/| N-021, option (a) (essai) |/| N-021, option (b) (essai) |/' registres/go.md
MOTIF_CAS="GO-2026-10-12-99 : absent du registre courant, ou d'un autre type" cas P17g-go-sur-l-option-b 2 - FAUX_X=1
cp "$E/go-sauve.md" registres/go.md
sed -i 's/| N-021, option (a) (essai) |/| N-019, option (a) (essai) |/' registres/go.md
MOTIF_CAS="GO-2026-10-12-99 : absent du registre courant, ou d'un autre type" cas P17j-go-d-un-autre-noeud 2 - FAUX_X=1
cp "$E/go-sauve.md" registres/go.md
MOTIF_CAS="relance non consignée" cas P13-relance-non-consignee 2 "111 $E/traces - relance R-151" FAUX_X=1
echo "| R-151 | 2026-10-12 | Notations : panne réseau de l'hôte (essai). | essai |" >> registres/decisions.md
MOTIF_CAS="relance non consignée" cas P13b-relance-cause-sans-infrastructure 2 "111 $E/traces - relance R-151" FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
echo "| R-151 | 2026-10-12 | Relancement du pilote : cause d'infrastructure (panne réseau de l'hôte, instance 12345678 arrêtée, essai). | essai |" >> registres/decisions.md
MOTIF_CAS="relance non consignée" cas P13g-relance-du-pilote-et-non-des-notations 2 "111 $E/traces - relance R-151" FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
echo "| R-151 | 2026-10-12 | Relancement des notations : cause d'infrastructure (panne réseau de l'hôte, essai). | essai |" >> registres/decisions.md
MOTIF_CAS="ne nomme pas, une seule fois, l'instance du premier lancement" cas P13d-relance-sans-instance-nommee 2 "111 $E/traces - relance R-151" FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
echo "| R-151 | 2026-10-12 | Relancement des notations : cause d'infrastructure (panne réseau de l'hôte, instance 12345678 arrêtée, essai). | essai |" >> registres/decisions.md
cas P13c-relance-saine 0 "111 $E/traces - relance R-151" 'FAUX_INSTANCES=[{"id": 55292763, "actual_status": "exited", "cur_state": "stopped"}, {"id": 12345678, "actual_status": "exited", "cur_state": "stopped"}]'
cas P13e-relance-premiere-en-marche 2 "111 $E/traces - relance R-151" 'FAUX_INSTANCES=[{"id": 12345678, "actual_status": "running", "cur_state": "running"}]'
(cd "$E" && cas P13f-traces-en-chemin-relatif 0 "111 traces-relatives - relance R-151" 'FAUX_INSTANCES=[]')
grep -E "etiquette|env BRANCHE" "$E/journal-P13c-relance-saine.txt" | sed 's/^/    > /'
cp "$E/decisions-sauve.md" registres/decisions.md
cp "$E/B/notations-v1/controles_avant_depense_notations_v1.sh" "$E/ctl-sauve.sh"
echo "# modifié" >> "$E/B/notations-v1/controles_avant_depense_notations_v1.sh"
MOTIF_CAS="controles_avant_depense_notations_v1.sh exécuté ≠ copie versée au commit S" cas P14-controles-non-verses 2 - FAUX_X=1
cp "$E/ctl-sauve.sh" "$E/B/notations-v1/controles_avant_depense_notations_v1.sh"
cp "$L" "$E/lanceur-sauve.sh"; echo "# modifié" >> "$L"
MOTIF_CAS="lancer_notations_v1.sh exécuté ≠ copie versée au commit S" cas P14b-lanceur-non-verse 2 - FAUX_X=1
cp "$E/lanceur-sauve.sh" "$L"
git -C "$E/distant.git" update-ref refs/heads/main "$(git -C "$E/depot" rev-parse "$S~1")"
MOTIF_CAS="absent du dépôt distant" cas P15-s-absent-du-distant 2 - FAUX_X=1
git -C "$E/distant.git" update-ref refs/heads/main "$S"
git -C "$E/depot" fetch -q origin
cas P16-sain-rejoue 0 - FAUX_X=1
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
grep -l 'secret\|factice-hf\|factice-gh' "$E"/sortie-*.txt "$E"/lancement-*.txt "$E"/journal-*.txt 2>/dev/null | sed 's/^/JETON AFFICHÉ : /' || true
echo "FIN DU BANC DU LANCEUR DES NOTATIONS"
