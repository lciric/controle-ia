#!/usr/bin/env bash
# Banc du lanceur de P3 (R5), v1, brouillon 3, décliné du banc v2 du lanceur des notations (docs/procedures/notations-T0.5-v3/,
# 142 cas) sous un nom nouveau (R12) : ses cas génériques, adaptés (heure, place des traces et du bloc-notes, contrôles,
# jetons, arguments, instances tolérées et autres projets, crédit sur 6,5 heures, crédit illisible, choix de l'offre la
# moins chère parmi les conformes avec ses pièges, offres relues gardées, création douteuse, jeton masqué dans la sortie et
# dans la réponse masquée, GO de calcul échu, S introuvable ou absent du distant, fetch en échec, amorce non citée,
# branche autre, preuves des essais, dossier de traces relatif), plus les cas propres à P3 : treize scripts de la chaîne
# égaux à leurs copies versées à S ; GO de calcul et décision de Lazar (ligne absente, GO révoqué, GO d'un autre type,
# GO de calcul d'un autre périmètre (GO-2026-10-17-01, CH-02), décision R-192 absente ou autre, registre des GO absent ;
# révocation de R-192 sous ses deux formes exactes seulement, relecture courte, RCh-01, RCh-02 : ligne « révocation » du
# registre des GO dont le périmètre nomme R-192 ou le GO, refusée, même si elle vise un autre GO ; ligne du registre des
# décisions qui commence par « **Révocation de R-192** », refusée ; cas sains : ligne qui décrit les formes (texte de
# R-215), ligne « aucune révocation de R-192 », texte libre sans la forme exacte) ; accord de Lazar du jour (CH-11 :
# absent, d'un autre jour, en double, argument mal formé ; forme exacte, RCh-03 : ligne du jour qui mentionne l'accord,
# P3 et le lancement sans le préfixe « **Accord de Lazar pour le lancement de P3** », ou avec le préfixe ailleurs qu'en
# tête, refusée) ; instances tolérées non épinglées ; instances d'autres projets tolérées seulement à l'étiquette « rr- »
# (CH-13) ; offres sans assez de cœurs effectifs, de mémoire vive, au téléchargement ou au stockage au-dessus de leur
# borne ou illisibles, écartées même moins chères (CH-04, CH-10, RCh-04) ; bornes de téléchargement et de stockage non
# fixées (code 2) ; aucune
# forme de relance acceptée. Aucun appel réel n'est possible : faux outil de location (n'appelle aucun service ;
# journalise le verbe, l'étiquette et les variables non secrètes de --env, jamais un jeton), faux contrôles, HOME
# redirigé, clé d'API retirée, jetons factices. Dépôt synthétique : préenregistrement minimal (empreinte de l'amorce, GO
# et décision, ligne « Lancement »), registres (GO de calcul et GO du pilote du papier C, ligne R-192, ligne d'accord du
# jour), garde de calcul du dépôt, copies versées des treize scripts (celle du lanceur : celle du banc) et des cinq
# journaux de preuve ; dépôt nu local en guise de dépôt distant. Si la borne de téléchargement du lanceur éprouvé était
# « A_FIXER », la copie jouée la fixerait à une valeur d'essai (ligne changée comptée et déclarée) ; les offres factices
# se placent sous les bornes de téléchargement et de stockage (la moitié), un cas au-dessus de chacune.
# Usage : essais_lanceur_p3_v1.sh RACINE_NEUVE
set -uo pipefail
E=$(realpath -m "${1:?racine neuve}")
BN=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
HN=${HN:-$BN/p3-v1}
D=/home/user/controle-ia-travail
P=prereg/P3-premier-test-i-a-v1.md
VERSEES=docs/procedures/P3-premier-test-v1
TEL_ESSAI=0.05                                    # borne de téléchargement d'essai, seulement si le lanceur éprouvé porte « A_FIXER »
AUTRES_SCRIPTS="sceller_p3_v1.sh surveiller_p3_v1.sh controle_cinq_minutes_p3_v1.sh recuperation_p3_v1.sh repetition_jouet_p3_v1.sh
                repetition_finale_p3_v1.sh essais_lanceur_p3_v1.sh essais_controles_p3_v1.sh essais_scellement_p3_v1.sh essais_surveillance_p3_v1.sh"
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
echo "script éprouvé : lancer_p3_v1.sh $(sha256sum "$HN/lancer_p3_v1.sh" | cut -d' ' -f1)"
echo "script éprouvé : verifications_p3_v1.py $(sha256sum "$HN/verifications_p3_v1.py" | cut -d' ' -f1)"
echo "script éprouvé : $(basename "$0") $(sha256sum "$(realpath "$0")" | cut -d' ' -f1)"
NON_CONFORMES=0
JOUR=$(date -u +%F); HIER=$(date -u -d yesterday +%F)
mkdir -p "$E/B/p3-v1" "$E/B/venv-vastai/bin" "$E/home" "$E/bin-heure" "$E/bin-df"
cat > "$E/B/venv-vastai/bin/vastai" <<'EOF'
#!/usr/bin/env bash
# faux vastai du banc du lanceur de P3 : n'appelle aucun service
J=${FAUX_VASTAI_JOURNAL:?}
echo "appel : $1 $2" >> "$J"
case "$1 $2" in
  "search offers") [ -n "${FAUX_OFFRES:-}" ] && { printf '%s\n' "$FAUX_OFFRES"; exit 0; }; printf '[{"id": 111, "gpu_name": "%s", "gpu_ram": 81920, "num_gpus": 1, "machine_id": 7101, "host_id": 8101, "dph_total": %s, "cpu_name": "%s", "cpu_arch": "amd64", "cpu_cores": 128, "cpu_cores_effective": %s, "cpu_ram": %s, "inet_down_cost": %s, "storage_total_cost": %s}, {"id": 222, "dph_total": 0.9, "cpu_name": "AMD EPYC 7513 32-Core Processor"}]\n' "${FAUX_GPU:-A100 SXM4}" "${FAUX_PRIX:-1.10}" "${FAUX_CPU:-AMD EPYC 7513 32-Core Processor}" "${FAUX_COEURS:-32.0}" "${FAUX_RAM:-128886}" "${FAUX_TEL:?}" "${FAUX_STO:?}" ;;
  "show user") [ -n "${FAUX_USER_ILLISIBLE:-}" ] && { echo "erreur factice"; exit 0; }; printf '{"credit": %s, "email": "x@invalid"}\n' "${FAUX_CREDIT:-20.0}" ;;
  "show instances") [ -n "${FAUX_INSTANCES_ECHEC:-}" ] && { echo "erreur factice" >&2; exit 1; }; d='[{"id": 55292763, "actual_status": "exited", "cur_state": "stopped", "extra_env": [["GH_TOKEN", "secret"]]}, {"id": 55458787, "actual_status": "exited", "cur_state": "stopped"}, {"id": 55538944, "actual_status": "exited", "cur_state": "stopped", "label": "t05-pilote-v1"}, {"id": 56438435, "actual_status": "exited", "cur_state": "stopped", "label": "t05-notations-v1"}]'; printf '%s\n' "${FAUX_INSTANCES:-$d}" ;;
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
    echo "go ${GO_ID:-absent}" >> "$J"
    d='{"success": true, "new_contract": 99999999}'; printf '%s\n' "${FAUX_CREATION:-$d}"; exit "${FAUX_CODE_CREATION:-0}" ;;
  *) echo "verbe inattendu" >&2; exit 9 ;;
esac
EOF
chmod +x "$E/B/venv-vastai/bin/vastai"
cat > "$E/B/p3-v1/controles_avant_depense_p3_v1.sh" <<'EOF'
#!/usr/bin/env bash
mkdir -p "$2" "$2.travail" && echo donnees > "$2/x"
echo "arguments : S=${1:0:12} ; $# arguments"
[ $# = 2 ] || { echo "KO  essai : nombre d'arguments"; echo "CONTRÔLES AVANT DÉPENSE : ÉCHEC"; exit 1; }
if [ -n "${FAUX_KO:-}" ]; then echo "OK  essai"; echo "KO  essai : faute simulée"; echo "CONTRÔLES AVANT DÉPENSE : ÉCHEC"; exit 1; fi
if [ -n "${FAUX_DERNIERE:-}" ]; then echo "OK  essai"; echo "dernière ligne inattendue (essai)"; exit 0; fi
echo "OK  essai"; echo "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES"
EOF
cp "$HN/verifications_p3_v1.py" "$E/B/p3-v1/"
L=$E/B/p3-v1/lancer_p3_v1.sh
sed -e "s|^DEPOT=.*|DEPOT=$E/depot|" -e "s|^B=.*|B=$E/B|" -e "s|^TELECHARGEMENT_MAX=A_FIXER |TELECHARGEMENT_MAX=$TEL_ESSAI |" "$HN/lancer_p3_v1.sh" > "$L"
echo "lignes changées dans la copie du lanceur : $(diff "$HN/lancer_p3_v1.sh" "$L" | grep -c '^>') (DEPOT, B$(grep -q '^TELECHARGEMENT_MAX=A_FIXER ' "$HN/lancer_p3_v1.sh" && echo ", TELECHARGEMENT_MAX : borne d'essai $TEL_ESSAI, celle du texte n'étant pas fixée"))"
[ "$(sed -n 's/^B=//p' "$L")" = "$E/B" ] && [ "$(sed -n 's/^V=//p' "$L")" = '$B/venv-vastai/bin/vastai' ] \
    && ! grep -q "$BN/venv-vastai" "$L" || { echo "copie du lanceur non sûre"; exit 2; }
TEL=$(sed -n 's/^TELECHARGEMENT_MAX=\([0-9.]*\) .*/\1/p' "$L")
[[ "$TEL" =~ ^0\.[0-9]{2,4}$ ]] || { echo "borne de téléchargement de la copie illisible"; exit 2; }
TEL_SOUS=$(python3 -c 'import sys; print(float(sys.argv[1]) / 2)' "$TEL"); TEL_SUR=$(python3 -c 'import sys; print(round(float(sys.argv[1]) + 0.01, 4))' "$TEL")
export FAUX_TEL=$TEL_SOUS
STO=$(sed -n 's/^STOCKAGE_MAX=\([0-9.]*\) .*/\1/p' "$L")
[[ "$STO" =~ ^0\.[0-9]{2,4}$ ]] || { echo "borne de stockage de la copie illisible"; exit 2; }
STO_SOUS=$(python3 -c 'import sys; print(float(sys.argv[1]) / 2)' "$STO"); STO_SUR=$(python3 -c 'import sys; print(round(float(sys.argv[1]) + 0.001, 4))' "$STO")
export FAUX_STO=$STO_SOUS
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
if [ -n "\${FAUX_DF_BLOC_NOTES:-}" ] && [ "\${@: -1}" = "$E/B" ]; then
  printf 'Filesystem 1024-blocks Used Available Capacity Mounted\n/dev/x 100 90 2900000 97%% /\n'; exit 0
fi
exec /usr/bin/df "\$@"
EOF
chmod +x "$E/bin-df/df"
mkdir -p "$E/depot" && cd "$E/depot" && git init -q -b main
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
mkdir -p prereg scripts registres .claude/hooks "$VERSEES"
git -C "$D" show HEAD:scripts/amorce_instance_p3.sh > scripts/amorce_instance_p3.sh
git -C "$D" show HEAD:registres/go.md > registres/go.md
git -C "$D" show HEAD:.claude/hooks/garde_calcul.py > .claude/hooks/garde_calcul.py
cat > registres/decisions.md <<EOF
# Registre des décisions (essai)

| id | date | décision | fondement |
|---|---|---|---|
| R-192 | 2026-10-17 | Décision de Lazar (essai) : « (b) P1 + P2 + P3 + pilote du papier C » ; P3 : premier test boîte blanche. | essai |
| R-999 | $JOUR | **Accord de Lazar pour le lancement de P3** (essai, dans la session). | essai |
EOF
git add -A && git commit -qm "base"
EA=$(sha256sum scripts/amorce_instance_p3.sh | cut -d' ' -f1)
cat > "$P" <<EOF
# Préenregistrement de P3 (essai du banc du lanceur)
- Scripts de l'instance, gelés par ce commit : \`scripts/amorce_instance_p3.sh\`
  (\`$EA\`, sha256), citation passée à la ligne.
- GO de calcul et décision de Lazar : \`GO-2026-10-04-08\` (R-192)
- Lancement : \`PREREG=$P\`, \`BRANCHE=calcul/p3-reel-v1\`, \`DEPOT_URL=https://github.com/lciric/controle-ia-travail.git\`.
EOF
(cd prereg && sha256sum "$(basename "$P")" > "$(basename "$P").sha256")
# copies versées à S des treize scripts : les faux contrôles et le module commun du bloc-notes factice, le lanceur du banc,
# et les dix autres scripts, au bloc-notes factice et en copie versée (le lanceur compare les treize)
cp "$E/B/p3-v1/controles_avant_depense_p3_v1.sh" "$E/B/p3-v1/verifications_p3_v1.py" "$L" "$VERSEES/"
for s in $AUTRES_SCRIPTS; do
    cp "$HN/$s" "$VERSEES/" && cp "$HN/$s" "$E/B/p3-v1/" || { echo "copie versée factice impossible : $s"; exit 2; }
done
ep() { for s in "$@"; do echo "script éprouvé : $s $(sha256sum "$VERSEES/$s" | cut -d' ' -f1)"; done; }
journal_preuve() {   # $1 nom du journal, $2 dernière ligne, puis les scripts éprouvés
    local n=$1 v=$2; shift 2
    { echo "journal factice du banc du lanceur"; ep "$@"; echo "$v"; } > "$VERSEES/$n"
    (cd "$VERSEES" && sha256sum "$n" > "$n.sha256")
}
journaux_preuves() {
    journal_preuve banc-lanceur-p3-v1.log "FIN DU BANC DU LANCEUR DE P3 ; cas non conformes : 0" lancer_p3_v1.sh verifications_p3_v1.py essais_lanceur_p3_v1.sh
    journal_preuve banc-surveillance-p3-v1.log "FIN DU BANC DE LA SURVEILLANCE DE P3 ; cas non conformes : 0" surveiller_p3_v1.sh controle_cinq_minutes_p3_v1.sh essais_surveillance_p3_v1.sh
    journal_preuve banc-controles-p3-v1.log "FIN DU BANC DES CONTRÔLES DE P3 ; cas non conformes : 0" controles_avant_depense_p3_v1.sh verifications_p3_v1.py essais_controles_p3_v1.sh
    journal_preuve banc-scellement-p3-v1.log "FIN DU BANC DU SCELLEMENT DE P3 ; cas non conformes : 0" sceller_p3_v1.sh verifications_p3_v1.py essais_scellement_p3_v1.sh
    journal_preuve repetition-finale-p3-v1.log "RÉPÉTITION FINALE : CONFORME" sceller_p3_v1.sh controles_avant_depense_p3_v1.sh verifications_p3_v1.py repetition_finale_p3_v1.sh
}
journaux_preuves
git add -A && git commit -qm "S : préenregistrement de P3 scellé (essai)"
S=$(git rev-parse HEAD); echo "S = $S"
git clone -q --bare . "$E/distant.git" && git remote add origin "$E/distant.git" && git fetch -q origin
cp registres/decisions.md "$E/decisions-sauve.md"; cp registres/go.md "$E/go-sauve.md"
cas() {   # $1 nom ; $2 code attendu ; $3 arguments du lanceur (« - » : les arguments normaux) ; puis l'environnement
    local nom=$1 attendu=$2 args=$3; shift 3
    rm -rf "$E/traces" "$E/compteur-heure"; : > "$E/journal-$nom.txt"
    local a=("$E/traces" - R-999); [ "$args" = "-" ] || read -r -a a <<<"$args"
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
    [ -f "$tr/lancement.txt" ] && cp "$tr/lancement.txt" "$E/lancement-$nom.txt"
    [ -f "$tr/reponse-masquee.txt" ] && cp "$tr/reponse-masquee.txt" "$E/reponse-$nom.txt"
    return 0
}
cas P00-sain 0 - FAUX_X=1
grep -E "etiquette|env |^go " "$E/journal-P00-sain.txt" | sed 's/^/    > /'
python3 - "$E/lancement-P00-sain.txt" "$E/journal-P00-sain.txt" "$JOUR" <<'EOF' || { echo "    P00 : vérifications du cas sain : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
import re, sys
t = open(sys.argv[1], encoding="utf-8").read(); j = open(sys.argv[2], encoding="utf-8").read(); jour = sys.argv[3]
c = re.search(r"^creation (\d+)$", t, re.M)
pl = re.search(r"^plafond de la surveillance (\d+) \(création \+ 22200 s ; surveiller_p3_v1\.sh <id> (\d+) <dossier neuf>\)$", t, re.M)
cq = re.search(r"^contrôle à cinq minutes entre (\d+) et (\d+) \(création \+ 180 à 300 s ; controle_cinq_minutes_p3_v1\.sh <id> \S+ <dossier neuf>\)$", t, re.M)
v = {"plafond de la surveillance = création + 22 200 s": bool(c and pl and int(pl.group(1)) - int(c.group(1)) == 22200 and pl.group(2) == c.group(1)),
     "contrôle à cinq minutes = création + 180 à 300 s": bool(c and cq and int(cq.group(1)) - int(c.group(1)) == 180 and int(cq.group(2)) - int(c.group(1)) == 300),
     "branche calcul/p3-reel-v1": bool(re.search(r"^branche calcul/p3-reel-v1$", t, re.M) and re.search(r"^env BRANCHE=calcul/p3-reel-v1$", j, re.M)),
     "PREREG et DEPOT_URL": bool(re.search(r"^env PREREG=prereg/P3-premier-test-i-a-v1\.md$", j, re.M) and re.search(r"^env DEPOT_URL=https://github\.com/lciric/controle-ia-travail\.git$", j, re.M)),
     "étiquette p3-v1": bool(re.search(r"^etiquette p3-v1$", j, re.M)), "ETUDE absente": "env ETUDE=" not in j,
     "GO GO-2026-10-04-08 écrit et porté par la création": bool(re.search(r"^go GO-2026-10-04-08$", t, re.M) and re.search(r"^go GO-2026-10-04-08$", j, re.M)),
     "accord de Lazar du jour relu deux fois": len(re.findall(rf"^accord R-999 : accord de Lazar du {jour} pour le lancement de P3 : conforme$", t, re.M)) == 2,
     "instances arrêtées tolérées (dont 56438435)": "56438435 (exited, stopped)" in t,
     "destruction écrite (72 heures)": "72 heures au plus" in t}
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
MOTIF_CAS="place disque : " cas P05b-place-bloc-notes 3 - FAUX_DF_BLOC_NOTES=1
MOTIF_CAS="contrôles avant dépense en échec" cas P06-controles-ko 2 - FAUX_KO=1
MOTIF_CAS="aucune offre conforme" cas P07-offre-sans-prix 3 - FAUX_PRIX=null
MOTIF_CAS="aucune offre conforme" cas P07b-prix-au-dessus-du-devis 3 - FAUX_PRIX=1.35
MOTIF_CAS="aucune offre conforme" cas P07c-processeur-autre 3 - 'FAUX_CPU=Intel Xeon Platinum 8480+'
MOTIF_CAS="aucune offre conforme" cas P07d-processeur-voisin 3 - 'FAUX_CPU=AMD EPYC 7513'
MOTIF_CAS="aucune offre conforme" cas P07e-carte-pcie 3 - 'FAUX_GPU=A100 PCIE'
MOTIF_CAS="aucune offre conforme" cas P07f-quinze-coeurs 3 - FAUX_COEURS=15.0
MOTIF_CAS="aucune offre conforme" cas P07g-memoire-vive-64-go 3 - FAUX_RAM=64000
MOTIF_CAS="aucune offre conforme" cas P07h-telechargement-au-dessus-de-la-borne 3 - FAUX_TEL="$TEL_SUR"
MOTIF_CAS="aucune offre conforme" cas P07i-coeurs-illisibles 3 - FAUX_COEURS=null
MOTIF_CAS="aucune offre conforme" cas P07j-telechargement-illisible 3 - FAUX_TEL=null
cas P07k-seize-coeurs-juste 0 - FAUX_COEURS=16.0
# stockage borné (relecture courte, RCh-04, RT-05) : au-dessus de la borne, illisible, au plafond juste
MOTIF_CAS="aucune offre conforme" cas P07l-stockage-au-dessus-de-la-borne 3 - FAUX_STO="$STO_SUR"
MOTIF_CAS="aucune offre conforme" cas P07m-stockage-illisible 3 - FAUX_STO=null
cas P07n-stockage-au-plafond-juste 0 - FAUX_STO="$STO"
# crédit exigé : 6,5 h × 1,10 + 1,2 = 8,35 USD
MOTIF_CAS="crédit insuffisant pour P3" cas P08-credit-insuffisant 3 - FAUX_CREDIT=8.34
MOTIF_CAS="minimum 8.35 USD (6.5 h)" cas P08b-credit-juste 0 - FAUX_CREDIT=8.35
MOTIF_CAS="crédit illisible (vastai show user" cas P08c-credit-illisible 2 - FAUX_USER_ILLISIBLE=1
MOTIF_CAS="crédit illisible (vastai show user" cas P08d-credit-non-numerique 2 - "FAUX_CREDIT=\"8.35'); import os; print('\""
MOTIF_CAS="jeton absent" cas P09-jeton-hf-absent 2 - HF_TOKEN=
MOTIF_CAS="jeton absent" cas P09b-jeton-github-absent 2 - CONTROLE_IA_GITHUB_TOKEN=
MOTIF_CAS="usage" cas P10-argument-absent 2 "" FAUX_X=1
MOTIF_CAS="usage" cas P10a-deux-arguments-sans-accord 2 "$E/traces -" FAUX_X=1
MOTIF_CAS="usage" cas P10b-quatre-arguments 2 "$E/traces - R-999 relance" FAUX_X=1
MOTIF_CAS="usage" cas P10c-forme-de-relance-refusee 2 "$E/traces - relance R-151 $E/releve.txt" FAUX_X=1
MOTIF_CAS="ACCORD : identifiant R-" cas P10d-accord-mal-forme 2 "$E/traces - 999" FAUX_X=1
MOTIF_CAS="autres instances sur le compte" cas P11-instance-non-toleree 2 - 'FAUX_INSTANCES=[{"id": 1, "actual_status": "running", "cur_state": "running"}]'
MOTIF_CAS="55538944 (running, running)" cas P11b-instance-du-programme-en-marche 2 - 'FAUX_INSTANCES=[{"id": 55538944, "actual_status": "running", "cur_state": "running", "label": "t05-pilote-v1"}]'
cas P11c-aucune-instance 0 - 'FAUX_INSTANCES=[]'
MOTIF_CAS="instances : non tolérée(s), ou liste illisible" cas P11d-liste-des-instances-illisible 2 - FAUX_INSTANCES_ECHEC=1
MOTIF_CAS="56438435 (running, running)" cas P11e-instance-des-notations-en-marche 2 - 'FAUX_INSTANCES=[{"id": 56438435, "actual_status": "running", "cur_state": "running", "label": "t05-notations-v1"}]'
# instances tolérées non épinglées ; borne de téléchargement non fixée (copies du lanceur, versées à S : une ligne change)
sed 's/^ARRETEES_TOLEREES="[0-9 ]*"/ARRETEES_TOLEREES="A_EPINGLER"/' "$L" > "$E/lanceur-non-epingle.sh"
[ "$(diff "$L" "$E/lanceur-non-epingle.sh" | grep -c '^>')" = 1 ] || { echo "copie non épinglée : une ligne exactement attendue"; exit 2; }
L_SAUVE=$L; L=$E/lanceur-non-epingle.sh
MOTIF_CAS="instances tolérées non épinglées" cas Z01-instances-tolerees-non-epinglees 2 - FAUX_X=1
L=$L_SAUVE
sed "s/^TELECHARGEMENT_MAX=[0-9.]* /TELECHARGEMENT_MAX=A_FIXER /" "$L" > "$E/lanceur-sans-borne.sh"
[ "$(diff "$L" "$E/lanceur-sans-borne.sh" | grep -c '^>')" = 1 ] || { echo "copie sans borne : une ligne exactement attendue"; exit 2; }
L_SAUVE=$L; L=$E/lanceur-sans-borne.sh
MOTIF_CAS="borne de téléchargement non fixée" cas Z02-borne-de-telechargement-non-fixee 2 - FAUX_X=1
L=$L_SAUVE
sed "s/^STOCKAGE_MAX=[0-9.]* /STOCKAGE_MAX=A_FIXER /" "$L" > "$E/lanceur-sans-borne-de-stockage.sh"
[ "$(diff "$L" "$E/lanceur-sans-borne-de-stockage.sh" | grep -c '^>')" = 1 ] || { echo "copie sans borne de stockage : une ligne exactement attendue"; exit 2; }
L_SAUVE=$L; L=$E/lanceur-sans-borne-de-stockage.sh
MOTIF_CAS="borne de stockage non fixée" cas Z03-borne-de-stockage-non-fixee 2 - FAUX_X=1
L=$L_SAUVE
# treize scripts égaux à leurs copies versées à S
for s in controles_avant_depense_p3_v1.sh surveiller_p3_v1.sh controle_cinq_minutes_p3_v1.sh verifications_p3_v1.py recuperation_p3_v1.sh; do
    cp "$E/B/p3-v1/$s" "$E/sauve-$s"; echo "# modifié" >> "$E/B/p3-v1/$s"
    MOTIF_CAS="$s exécuté ≠ copie versée au commit S" cas "P14-$s-non-verse" 2 - FAUX_X=1
    cp "$E/sauve-$s" "$E/B/p3-v1/$s"
done
cp "$L" "$E/lanceur-sauve.sh"; echo "# modifié" >> "$L"
MOTIF_CAS="lancer_p3_v1.sh exécuté ≠ copie versée au commit S" cas P14b-lanceur-non-verse 2 - FAUX_X=1
cp "$E/lanceur-sauve.sh" "$L"
AVANT_P15=$(git -C "$E/distant.git" rev-parse refs/heads/main)
git -C "$E/distant.git" update-ref refs/heads/main "$(git -C "$E/depot" rev-parse "$S~1")"
MOTIF_CAS="absent du dépôt distant" cas P15-s-absent-du-distant 2 - FAUX_X=1
git -C "$E/distant.git" update-ref refs/heads/main "$AVANT_P15"
git -C "$E/depot" fetch -q origin
cas P16-sain-rejoue 0 - FAUX_X=1
# fetch du dépôt distant en échec (adresse de origin rendue injoignable, puis rétablie) : arrêt par le piège ERR (CH-14)
git -C "$E/depot" remote set-url origin "$E/distant-absent.git"
MOTIF_CAS="arrêt avant la création (ligne" cas N09-fetch-en-echec 2 - FAUX_X=1
git -C "$E/depot" remote set-url origin "$E/distant.git"
MOTIF_CAS="contrôles : dernière ligne inattendue" cas N07-controles-derniere-ligne-autre 2 - FAUX_DERNIERE=1
mkdir -p "$E/traces-existantes"
MOTIF_CAS="existe déjà (R12)" cas N05-traces-existantes 2 "$E/traces-existantes - R-999" FAUX_X=1
MOTIF_CAS="succès : True" cas N04-jeton-dans-la-reponse 0 - 'FAUX_CREATION={"success": true, "new_contract": 99999999, "msg": "jeton factice-hf-0000000 et factice-gh-0000000"}'
MOTIF_CAS="réponse illisible" cas N04b-jeton-dans-une-reponse-illisible 4 - 'FAUX_CREATION=erreur factice-gh-0000000 refusé'
[ -s "$E/reponse-N04b-jeton-dans-une-reponse-illisible.txt" ] && echo "    N04b : réponse masquée gardée (reponse-masquee.txt), relue pour les jetons ci-dessous : CONFORME" \
    || { echo "    N04b : réponse masquée absente : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
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
# GO de calcul et décision de Lazar (registres courants)
echo "| GO-2026-10-17-98 | 2026-10-17 | révocation | révoque GO-2026-10-04-08 (essai) | — | — | Lazar | essai |" >> registres/go.md
MOTIF_CAS="GO de calcul et décision de Lazar : GO-2026-10-04-08 révoqué" cas G02-go-revoque 2 - FAUX_X=1
cp "$E/go-sauve.md" registres/go.md
echo "| GO-2026-10-17-97 | 2026-10-17 | revendication | essai : aucune révocation de GO-2026-10-04-08 | — | — | Lazar | essai |" >> registres/go.md
cas G02b-ligne-go-qui-mentionne-une-revocation 0 - FAUX_X=1
cp "$E/go-sauve.md" registres/go.md
echo "| GO-2026-10-17-96 | 2026-10-17 | révocation | révoque la décision R-192 pour P3 (essai) | — | — | Lazar | essai |" >> registres/go.md
MOTIF_CAS="décision R-192 révoquée au registre des GO" cas G06-decision-revoquee-au-registre-des-go 2 - FAUX_X=1
cp "$E/go-sauve.md" registres/go.md
# forme (a) : une ligne « révocation » dont le périmètre nomme R-192 est une révocation, même si elle vise un autre GO
echo "| GO-2026-10-17-95 | 2026-10-17 | révocation | révoque GO-2026-10-17-01 (pilote du papier C, R-192 ; essai) | — | — | Lazar | essai |" >> registres/go.md
MOTIF_CAS="décision R-192 révoquée au registre des GO (GO-2026-10-17-95)" cas G06b-revocation-qui-nomme-r-192-pour-un-autre-go 2 - FAUX_X=1
cp "$E/go-sauve.md" registres/go.md
# forme (b) : cellule de décision qui commence exactement par « **Révocation de R-192** »
echo "| R-998 | $JOUR | **Révocation de R-192** pour P3 (essai). | essai |" >> registres/decisions.md
MOTIF_CAS="décision R-192 révoquée par R-998 (registre des décisions" cas G07-forme-exacte-au-registre-des-decisions 2 - FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
echo "| R-997 | $JOUR | Suite de P3 sous R-192 (essai), sans révocation. | essai |" >> registres/decisions.md
cas G07b-decision-qui-cite-r-192-sans-la-revoquer 0 - FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
# cas sains : la ligne R-215 du registre réel, qui décrit les formes sans révoquer ; « aucune révocation de R-192 » ; un
# texte libre sans la forme exacte (plus aucune recherche en texte libre) ; le préfixe ailleurs qu'en tête de la cellule
git -C "$D" show HEAD:registres/decisions.md | grep '^| R-215 |' >> registres/decisions.md
[ "$(grep -c '^| R-215 |' registres/decisions.md)" = 1 ] || { echo "G07c : montage impossible (ligne R-215)"; exit 2; }
cas G07c-ligne-r-215-qui-decrit-les-formes 0 - FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
echo "| R-996 | $JOUR | Décision de Lazar (essai) : aucune révocation de R-192. | essai |" >> registres/decisions.md
cas G07d-aucune-revocation-de-r-192 0 - FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
echo "| R-995 | $JOUR | Décision de Lazar (essai) : révoque R-192 pour P3, sans la forme exacte. | essai |" >> registres/decisions.md
cas G07e-texte-libre-sans-la-forme-exacte 0 - FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
echo "| R-994 | $JOUR | Note (essai) : la forme « **Révocation de R-192** » est décrite ici, sans révoquer. | essai |" >> registres/decisions.md
cas G07f-forme-exacte-ailleurs-qu-en-tete 0 - FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
sed -i '/^| R-192 |/d' registres/decisions.md
MOTIF_CAS="GO de calcul et décision de Lazar : R-192 absent, en double, ou sans la décision de Lazar" cas G03-decision-absente 2 - FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
sed -i 's/« (b) P1 + P2 + P3 + pilote du papier C »/« (a) P1 seulement »/' registres/decisions.md
MOTIF_CAS="GO de calcul et décision de Lazar : R-192 absent, en double, ou sans la décision de Lazar" cas G03b-decision-autre 2 - FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
mv registres/go.md "$E/go-deplace.md"
MOTIF_CAS="registres/go.md absent ou illisible" cas G08-registre-des-go-absent 2 - FAUX_X=1
mv "$E/go-deplace.md" registres/go.md
# accord de Lazar du jour (CH-11) : absent, d'un autre jour, sans la forme exacte (RCh-03), en double
sed -i '/^| R-999 |/d' registres/decisions.md
MOTIF_CAS="accord de Lazar : accord R-999 absent ou en double" cas A10-accord-absent 2 - FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
sed -i "s/^| R-999 | $JOUR |/| R-999 | $HIER |/" registres/decisions.md
MOTIF_CAS="accord du jour de l'appel ($JOUR) attendu" cas A11-accord-d-un-autre-jour 2 - FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
sed -i "/^| R-999 |/s/^| R-999 | $JOUR | .* | essai |\$/| R-999 | $JOUR | Délégation de Lazar (essai, comme R-208, R-215 ou R-217) : aucun appel payant sans l'accord de Lazar pour le lancement de P3. | essai |/" registres/decisions.md
grep -q "^| R-999 | $JOUR | Délégation de Lazar" registres/decisions.md || { echo "A12 : montage impossible"; exit 2; }
MOTIF_CAS="accord R-999 : la cellule de décision ne commence pas par « **Accord de Lazar pour le lancement de P3** »" cas A12-mention-de-l-accord-sans-la-forme-exacte 2 - FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
sed -i "/^| R-999 |/s/^| R-999 | $JOUR | .* | essai |\$/| R-999 | $JOUR | Note (essai) : **Accord de Lazar pour le lancement de P3** attendu plus tard. | essai |/" registres/decisions.md
grep -q "^| R-999 | $JOUR | Note (essai)" registres/decisions.md || { echo "A12b : montage impossible"; exit 2; }
MOTIF_CAS="la cellule de décision ne commence pas par" cas A12b-forme-exacte-ailleurs-qu-en-tete 2 - FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
grep '^| R-999 |' registres/decisions.md > "$E/accord.txt" && cat "$E/accord.txt" >> registres/decisions.md    # lue à part (grep refuse d'écrire dans le fichier qu'il lit)
[ "$(grep -c '^| R-999 |' registres/decisions.md)" = 2 ] || { echo "A13 : montage impossible"; exit 2; }
MOTIF_CAS="accord R-999 absent ou en double" cas A13-accord-en-double 2 - FAUX_X=1
cp "$E/decisions-sauve.md" registres/decisions.md
sed "s|^P=prereg/P3-premier-test-i-a-v1.md|P=prereg/absent-v1.md|" "$L" > "$E/lanceur-sans-s.sh"
[ "$(diff "$L" "$E/lanceur-sans-s.sh" | grep -c '^>')" = 1 ] || { echo "copie du lanceur (S introuvable) : une ligne exactement attendue"; exit 2; }
L_SAUVE=$L; L=$E/lanceur-sans-s.sh
MOTIF_CAS="commit de scellement introuvable" cas N08-s-introuvable 2 - FAUX_X=1
L=$L_SAUVE
# texte de S : amorce non citée, branche autre, GO absent, GO d'un autre type, GO de calcul d'un autre périmètre (S refait
# par un retrait puis un ajout du sceau, puis rétabli)
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
nouveau_s "s/BRANCHE=calcul\/p3-reel-v1/BRANCHE=calcul\/p3-reel-v9/"
MOTIF_CAS="PREREG ou BRANCHE : le préenregistrement de S cite autre chose" cas N02-branche-autre 2 - FAUX_X=1
nouveau_s "/^- GO de calcul et décision de Lazar/d"
MOTIF_CAS="ligne « GO de calcul et décision de Lazar » absente, en double ou mal formée" cas G01-ligne-go-absente 2 - FAUX_X=1
nouveau_s "s/GO-2026-10-04-08/GO-2026-10-12-01/"
MOTIF_CAS="GO-2026-10-12-01 : seul GO-2026-10-04-08 est accepté" cas G04-go-d-un-autre-type 2 - FAUX_X=1
nouveau_s "s/GO-2026-10-04-08/GO-2026-10-17-01/"
MOTIF_CAS="GO-2026-10-17-01 : seul GO-2026-10-04-08 est accepté" cas G05-go-de-calcul-d-un-autre-perimetre 2 - FAUX_X=1
nouveau_s ""
cas N00-sain-apres-retablissement 0 - FAUX_X=1
# preuves des essais : journal au verdict non conforme, empreinte d'un script éprouvé ≠ copie versée, journal absent,
# journal sans son sceau exact, script attendu non éprouvé, échec non compté, deux empreintes, ligne mal formée ou absente
preuve_alteree() { eval "$1" && git add -A "$VERSEES" && git commit -qm "essai : preuves altérées" || { echo "preuves : altération impossible"; exit 2; }; nouveau_s ""; }
retablir_preuves() { journaux_preuves && git add -A "$VERSEES" && git commit -qm "essai : preuves rétablies" && nouveau_s "" || { echo "preuves : rétablissement impossible"; exit 2; }; }
preuve_alteree "sed -i 's/cas non conformes : 0/cas non conformes : 1/' $VERSEES/banc-controles-p3-v1.log && (cd $VERSEES && sha256sum banc-controles-p3-v1.log > banc-controles-p3-v1.log.sha256)"
MOTIF_CAS="preuves des essais : journal banc-controles-p3-v1.log : dernière ligne" cas P30a-preuve-verdict-non-conforme 2 - FAUX_X=1
retablir_preuves
preuve_alteree "sed -i \"s/^script éprouvé : sceller_p3_v1.sh .*/script éprouvé : sceller_p3_v1.sh $(printf '7%.0s' {1..64})/\" $VERSEES/banc-scellement-p3-v1.log $VERSEES/repetition-finale-p3-v1.log && (cd $VERSEES && sha256sum banc-scellement-p3-v1.log > banc-scellement-p3-v1.log.sha256 && sha256sum repetition-finale-p3-v1.log > repetition-finale-p3-v1.log.sha256)"
MOTIF_CAS="preuves des essais : sceller_p3_v1.sh éprouvé" cas P30b-preuve-script-autre-que-la-copie 2 - FAUX_X=1
retablir_preuves
preuve_alteree "git rm -q $VERSEES/banc-surveillance-p3-v1.log $VERSEES/banc-surveillance-p3-v1.log.sha256"
MOTIF_CAS="preuves des essais : journal banc-surveillance-p3-v1.log absent de S" cas P30c-preuve-absente 2 - FAUX_X=1
retablir_preuves
preuve_alteree "echo ajout >> $VERSEES/banc-lanceur-p3-v1.log"
MOTIF_CAS="preuves des essais : sceau de banc-lanceur-p3-v1.log" cas P30d-preuve-sans-son-sceau 2 - FAUX_X=1
retablir_preuves
preuve_alteree "sed -i '/^script éprouvé : essais_surveillance_p3_v1.sh /d' $VERSEES/banc-surveillance-p3-v1.log && (cd $VERSEES && sha256sum banc-surveillance-p3-v1.log > banc-surveillance-p3-v1.log.sha256)"
MOTIF_CAS="scripts éprouvés ≠ attendus (manquants ['essais_surveillance_p3_v1.sh']" cas P30e-preuve-script-non-eprouve 2 - FAUX_X=1
retablir_preuves
preuve_alteree "sed -i '1a Traceback (most recent call last): essai' $VERSEES/banc-controles-p3-v1.log && (cd $VERSEES && sha256sum banc-controles-p3-v1.log > banc-controles-p3-v1.log.sha256)"
MOTIF_CAS="preuves des essais : journal banc-controles-p3-v1.log : ligne d'échec avant le verdict" cas P30g-preuve-echec-non-compte 2 - FAUX_X=1
retablir_preuves
preuve_alteree "sed -i \"s/^script éprouvé : sceller_p3_v1.sh .*/script éprouvé : sceller_p3_v1.sh $(printf '8%.0s' {1..64})/\" $VERSEES/repetition-finale-p3-v1.log && (cd $VERSEES && sha256sum repetition-finale-p3-v1.log > repetition-finale-p3-v1.log.sha256)"
MOTIF_CAS="preuves des essais : sceller_p3_v1.sh éprouvé sous deux empreintes" cas P30h-preuve-deux-empreintes 2 - FAUX_X=1
retablir_preuves
preuve_alteree "sed -i '1a script éprouvé : Autre.sh abc' $VERSEES/banc-lanceur-p3-v1.log && (cd $VERSEES && sha256sum banc-lanceur-p3-v1.log > banc-lanceur-p3-v1.log.sha256)"
MOTIF_CAS="ligne « script éprouvé » mal formée" cas P30i-preuve-ligne-mal-formee 2 - FAUX_X=1
retablir_preuves
preuve_alteree "sed -i '/^script éprouvé : /d' $VERSEES/banc-surveillance-p3-v1.log && (cd $VERSEES && sha256sum banc-surveillance-p3-v1.log > banc-surveillance-p3-v1.log.sha256)"
MOTIF_CAS="journal banc-surveillance-p3-v1.log : aucune ligne « script éprouvé »" cas P30j-preuve-sans-ligne 2 - FAUX_X=1
retablir_preuves
MOTIF_CAS="preuves des essais : cinq journaux conformes ; 11 scripts éprouvés égaux à leurs copies versées à S" cas P30f-preuves-saines-apres-retablissement 0 - FAUX_X=1
# instances d'autres projets nommées en argument, tolérées seulement à l'étiquette « rr- » (CH-13) ; crédit exigé :
# 6,5 h × (1,10 + 4,004) + 1,2 = 34,38 USD
ARRETEES='{"id": 55292763, "actual_status": "exited", "cur_state": "stopped"}, {"id": 55458787, "actual_status": "exited", "cur_state": "stopped"}'
AUTRE='{"id": 55555587, "actual_status": "running", "cur_state": "running", "label": "rr-autre-projet-essai", "dph_total": 4.004, "extra_env": [["GH_TOKEN", "secret"]]}'
AUTRE_ARRETEE='{"id": 55555587, "actual_status": "exited", "cur_state": "stopped", "label": "rr-autre-projet-essai", "dph_total": 4.004}'
AUTRE_T05='{"id": 55555587, "actual_status": "running", "cur_state": "running", "label": "t05-notations-v1", "dph_total": 1.1}'
AUTRE_P3='{"id": 55555587, "actual_status": "running", "cur_state": "running", "label": "p3-v1", "dph_total": 1.1}'
AUTRE_T09='{"id": 55555587, "actual_status": "running", "cur_state": "running", "label": "t09-pilote-c-v1", "dph_total": 1.1}'
AUTRE_SANS_PREFIXE='{"id": 55555587, "actual_status": "running", "cur_state": "running", "label": "autre-projet-essai", "dph_total": 1.1}'
AUTRE_SANS_PRIX='{"id": 55555587, "actual_status": "running", "cur_state": "running", "label": "rr-autre-x", "dph_total": null}'
MOTIF_CAS="instances d'autres projets tolérées : 55555587 (running, running, 4.004 USD/h, en marche, comptée)" cas V01-autre-projet-en-marche-tolere 0 "$E/traces 55555587 R-999" "FAUX_INSTANCES=[$ARRETEES, $AUTRE]" FAUX_CREDIT=34.38
MOTIF_CAS="autres instances sur le compte" cas V02-autre-projet-non-declare 2 - "FAUX_INSTANCES=[$ARRETEES, $AUTRE]" FAUX_CREDIT=50
MOTIF_CAS="crédit insuffisant pour P3 et les autres projets en marche" cas V03-credit-insuffisant-avec-autre-projet 3 "$E/traces 55555587 R-999" "FAUX_INSTANCES=[$ARRETEES, $AUTRE]" FAUX_CREDIT=34.37
MOTIF_CAS="55555587 (running, running)" cas V04-autre-projet-etiquette-t05 2 "$E/traces 55555587 R-999" "FAUX_INSTANCES=[$ARRETEES, $AUTRE_T05]" FAUX_CREDIT=50
MOTIF_CAS="55555587 (running, running)" cas V04b-autre-projet-etiquette-p3 2 "$E/traces 55555587 R-999" "FAUX_INSTANCES=[$ARRETEES, $AUTRE_P3]" FAUX_CREDIT=50
MOTIF_CAS="55555587 (running, running)" cas V04c-autre-projet-etiquette-t09 2 "$E/traces 55555587 R-999" "FAUX_INSTANCES=[$ARRETEES, $AUTRE_T09]" FAUX_CREDIT=50
MOTIF_CAS="55555587 (running, running)" cas V04d-autre-projet-sans-prefixe-rr 2 "$E/traces 55555587 R-999" "FAUX_INSTANCES=[$ARRETEES, $AUTRE_SANS_PREFIXE]" FAUX_CREDIT=50
MOTIF_CAS="AUTRES_PROJETS : identifiants d'instances" cas V05-autres-mal-forme 2 "$E/traces abc R-999" FAUX_X=1
MOTIF_CAS="instances d'autres projets tolérées : aucune" cas V06-autre-declare-absent 0 "$E/traces 55555587 R-999" FAUX_X=1
MOTIF_CAS="55555587 (exited, stopped, 4.004 USD/h, arrêtée)" cas V07-autre-projet-arrete-non-compte 0 "$E/traces 55555587 R-999" "FAUX_INSTANCES=[$ARRETEES, $AUTRE_ARRETEE]" FAUX_CREDIT=8.35
MOTIF_CAS="55555587 (prix illisible)" cas V08-autre-projet-sans-prix 2 "$E/traces 55555587 R-999" "FAUX_INSTANCES=[$ARRETEES, $AUTRE_SANS_PRIX]" FAUX_CREDIT=50
# choix de l'offre parmi les conformes relues après les contrôles ; prix nul, négatif, infini, booléen ou texte, 40 Go,
# deux cartes, mémoire nulle ou infinie, identifiant booléen, cœurs, mémoire vive ou téléchargement hors bornes : écartés,
# même moins chers
EPYC="AMD EPYC 7513 32-Core Processor"
off() {   # identifiant prix [carte [processeur [mémoire [cartes [machine [hôte [cœurs [mémoire vive [téléchargement [stockage]]]]]]]]]]
    printf '{"id": %s, "gpu_name": "%s", "cpu_name": "%s", "gpu_ram": %s, "num_gpus": %s, "machine_id": %s, "host_id": %s, "dph_total": %s, "cpu_cores_effective": %s, "cpu_ram": %s, "inet_down_cost": %s, "storage_total_cost": %s}' \
        "$1" "${3:-A100 SXM4}" "${4:-$EPYC}" "${5:-81920}" "${6:-1}" "${7:-7100}" "${8:-8100}" "$2" "${9:-32.0}" "${10:-128886}" "${11:-$TEL_SOUS}" "${12:-$STO_SOUS}"
}
MOTIF_CAS="offre choisie : 112 (1.05 USD/h), la moins chère des offres conformes" cas O01-moins-chere-des-conformes 0 - "FAUX_OFFRES=[$(off 111 1.10), $(off 112 1.05), $(off 113 1.20), $(off 114 0.80 "A100 SXM4" "Intel Xeon"), $(off 115 0.70 "A100 PCIE"), $(off 116 1.35), $(off 117 null), $(off true 0.5), $(off 118 true), $(off 121 '"0.9"'), $(off 122 0), $(off 123 -0.5), $(off 124 -Infinity), $(off 125 0.9 "A100 SXM4" "$EPYC" 40960), $(off 126 0.9 "A100 SXM4" "$EPYC" 81920 2), $(off 127 0.9 "A100 SXM4" "$EPYC" null), $(off 128 0.9 "A100 SXM4" "$EPYC" 81920 true), $(off 129 0.9 "A100 SXM4" "$EPYC" Infinity), $(off 131 0.9 "A100 SXM4" "$EPYC" 81920 1 7100 8100 15.0), $(off 132 0.9 "A100 SXM4" "$EPYC" 81920 1 7100 8100 32.0 64000), $(off 133 0.9 "A100 SXM4" "$EPYC" 81920 1 7100 8100 32.0 128886 "$TEL_SUR"), $(off 134 0.9 "A100 SXM4" "$EPYC" 81920 1 7100 8100 null)]"
python3 - "$E/lancement-O01-moins-chere-des-conformes.txt" "$E/journal-O01-moins-chere-des-conformes.txt" "$E/traces/offres-relues.json" <<'EOF' \
    && echo "    O01 : offre créée 112 ; conformes dans l'ordre des prix (112, 111, 113), machine, hôte, cœurs, mémoire vive et téléchargement écrits ; 22 offres relues gardées : CONFORME" \
    || { echo "    O01 : offre créée, liste des conformes ou offres relues : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
import json, re, sys
t = open(sys.argv[1], encoding="utf-8").read(); j = open(sys.argv[2], encoding="utf-8").read()
l = [x for x in t.split("\n") if x.startswith("offres conformes relues : ")]
o = json.load(open(sys.argv[3].replace("offres-relues.json", "offre.json")))
ok = (len(l) == 1 and re.findall(r"(?:: |, )(\d+) \(", l[0]) == ["112", "111", "113"] and "machine 7100 ; hôte 8100" in l[0]
      and "cœurs effectifs 32.0 ; mémoire vive 128886 Mo" in l[0]
      and re.search(r"^offre créée 112$", j, re.M) and len(json.load(open(sys.argv[3]))) == 22
      and o.get("id") == 112 and o.get("machine_id") == 7100 and o.get("host_id") == 8100 and o.get("cpu_cores_effective") == 32.0)
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
MOTIF_CAS="offres : relecture impossible" cas O05-offres-illisibles 2 - "FAUX_OFFRES=pas du json"
[ -s "$E/traces/offres-relues-brut.txt" ] && echo "    O05 : réponse illisible gardée (offres-relues-brut.txt) : CONFORME" \
    || { echo "    O05 : réponse illisible non gardée : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
MOTIF_CAS="offres : relecture impossible" cas O06-offres-pas-une-liste 2 - 'FAUX_OFFRES={"id": 1}'
MOTIF_CAS="offre choisie : 140 (1.3 USD/h)" cas O07-prix-au-plafond-juste 0 - "FAUX_OFFRES=[$(off 140 1.30)]" FAUX_CREDIT=50
# crédit exigé avec l'offre choisie parmi plusieurs : 6,5 h × 1,00 + 1,2 = 7,70 USD (8,35 à 1,10)
MOTIF_CAS="minimum 7.70 USD (6.5 h)" cas O08-credit-calcule-sur-l-offre-choisie 0 - "FAUX_OFFRES=[$(off 111 1.10), $(off 112 1.00)]" FAUX_CREDIT=7.70
MOTIF_CAS="crédit insuffisant pour P3" cas O08b-credit-juste-sous-le-minimum 3 - "FAUX_OFFRES=[$(off 111 1.10), $(off 112 1.00)]" FAUX_CREDIT=7.69
MOTIF_CAS="offre choisie illisible" cas O09-identifiant-negatif 2 - "FAUX_OFFRES=[$(off -9 1.05)]"
MOTIF_CAS="aucune offre conforme au filtre du plan" cas O10-carte-de-40-go 3 - "FAUX_OFFRES=[$(off 150 0.9 "A100 SXM4" "$EPYC" 40960)]"
MOTIF_CAS="offres : identifiant en double" cas O11-identifiant-en-double 2 - "FAUX_OFFRES=[$(off 112 1.05), $(off 112 1.25)]"
MOTIF_CAS="offre choisie : 161 (1.2 USD/h)" cas O12-moins-chere-sans-assez-de-coeurs-ecartee 0 - "FAUX_OFFRES=[$(off 160 0.9 "A100 SXM4" "$EPYC" 81920 1 7100 8100 15.9), $(off 161 1.20)]"
MOTIF_CAS="offre choisie : 163 (1.2 USD/h)" cas O13-moins-chere-sans-assez-de-memoire-vive-ecartee 0 - "FAUX_OFFRES=[$(off 162 0.9 "A100 SXM4" "$EPYC" 81920 1 7100 8100 32.0 127999), $(off 163 1.20)]"
MOTIF_CAS="offre choisie : 165 (1.2 USD/h)" cas O14-moins-chere-au-telechargement-trop-cher-ecartee 0 - "FAUX_OFFRES=[$(off 164 0.9 "A100 SXM4" "$EPYC" 81920 1 7100 8100 32.0 128886 "$TEL_SUR"), $(off 165 1.20)]"
MOTIF_CAS="offre choisie : 167 (1.2 USD/h)" cas O15-moins-chere-au-telechargement-negatif-ecartee 0 - "FAUX_OFFRES=[$(off 166 0.9 "A100 SXM4" "$EPYC" 81920 1 7100 8100 32.0 128886 -0.01), $(off 167 1.20)]"
MOTIF_CAS="offre choisie : 169 (1.2 USD/h)" cas O16-moins-chere-au-stockage-trop-cher-ecartee 0 - "FAUX_OFFRES=[$(off 168 0.9 "A100 SXM4" "$EPYC" 81920 1 7100 8100 32.0 128886 "$TEL_SOUS" "$STO_SUR"), $(off 169 1.20)]"
MOTIF_CAS="offre choisie : 171 (1.2 USD/h)" cas O17-moins-chere-au-stockage-negatif-ecartee 0 - "FAUX_OFFRES=[$(off 170 0.9 "A100 SXM4" "$EPYC" 81920 1 7100 8100 32.0 128886 "$TEL_SOUS" -0.01), $(off 171 1.20)]"
MOTIF_CAS="offre choisie : 173 (1.2 USD/h)" cas O18-moins-chere-au-stockage-illisible-ecartee 0 - "FAUX_OFFRES=[$(off 172 0.9 "A100 SXM4" "$EPYC" 81920 1 7100 8100 32.0 128886 "$TEL_SOUS" '"0.01"'), $(off 173 1.20)]"
# dossier de traces purement numérique ; dossier de traces relatif (écrit en chemin absolu) ; trois arguments sans accord
MOTIF_CAS="DOSSIER_TRACES purement numérique" cas A01-traces-numeriques 2 "$E/29296808 - R-999" FAUX_X=1
MOTIF_CAS="usage" cas A02-arguments-dans-le-desordre 2 "29296808 $E/traces - R-999" FAUX_X=1
pushd "$E" > /dev/null && cas A03-traces-en-chemin-relatif 0 "traces-relatives - R-999" FAUX_X=1; popd > /dev/null
[ -s "$E/traces-relatives/lancement.txt" ] && grep -q "^creation " "$E/traces-relatives/lancement.txt" \
    && echo "    A03 : traces écrites sous $E/traces-relatives (chemin absolu) : CONFORME" \
    || { echo "    A03 : traces relatives : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
# jeton affiché : compté (sorties, lancements, journaux du faux outil, réponses masquées)
FUITES=$(grep -l 'secret\|factice-hf\|factice-gh' "$E"/sortie-*.txt "$E"/lancement-*.txt "$E"/journal-*.txt "$E"/reponse-*.txt 2>/dev/null || true)
[ -z "$FUITES" ] && echo "aucun jeton affiché : CONFORME" || { printf '%s\n' $FUITES | sed 's/^/JETON AFFICHÉ : /'; NON_CONFORMES=$((NON_CONFORMES + 1)); }
echo "FIN DU BANC DU LANCEUR DE P3 ; cas non conformes : $NON_CONFORMES"
[ "$NON_CONFORMES" = 0 ] || exit 1
