#!/usr/bin/env bash
# Banc léger du lanceur v7 (R5 ; contrôle mécanique, CM-02 et CM-03), repris du banc du contrôleur (monter.sh, jouer.sh,
# archivés dans …-verification-controle-mecanique-fichiers-de-travail-v1.tar). Aucun appel réel n'est possible : faux
# outil de location (n'appelle aucun service ; journalise le verbe, jamais les arguments), faux contrôles égaux à leur
# copie versée, HOME redirigé, clé d'API retirée, jetons factices. Dépôt synthétique : v2 saine du banc v7 des contrôles,
# amorce, registre des GO, garde de calcul, copies versées du lanceur et des faux contrôles.
# Usage : essais_lanceur_v7.sh RACINE_NEUVE V2_SAINE
set -uo pipefail
E=$1; V2=$2
BN=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
D=/home/user/controle-ia-travail
P=prereg/T0.5-revalidation-equivalence-pilote-v2.md
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
mkdir -p "$E/B/revalidation-v2" "$E/B/venv-vastai/bin" "$E/home" "$E/bin-heure" "$E/bin-df"
cp "$BN/verification-v2-essais/lanceur/venv-vastai/bin/vastai" "$E/B/venv-vastai/bin/vastai" && chmod +x "$E/B/venv-vastai/bin/vastai"
cat > "$E/B/revalidation-v2/controles_avant_depense_v7.sh" <<'EOF'
#!/usr/bin/env bash
# faux contrôles : crée le dossier du clone, échoue si FAUX_KO est posé
mkdir -p "$2" && echo donnees > "$2/x"
if [ -n "${FAUX_KO:-}" ]; then echo "OK  essai"; echo "KO  essai : faute simulée"; echo "CONTRÔLES AVANT DÉPENSE : ÉCHEC"; exit 1; fi
echo "OK  essai"; echo "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES"
EOF
L=$E/B/revalidation-v2/lancer_revalidation_v7.sh
sed -e "s|^DEPOT=.*|DEPOT=$E/depot|" -e "s|^B=.*|B=$E/B|" "$BN/revalidation-v2/lancer_revalidation_v7.sh" > "$L"
echo "lignes changées dans la copie du lanceur : $(diff "$BN/revalidation-v2/lancer_revalidation_v7.sh" "$L" | grep -c '^>')"
[ "$(sed -n 's/^B=//p' "$L")" = "$E/B" ] || { echo "copie du lanceur non sûre"; exit 2; }
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
mkdir -p prereg scripts registres .claude/hooks docs/procedures/revalidation-T0.5-v2
git -C "$D" show HEAD:scripts/amorce_instance_t05.sh > scripts/amorce_instance_t05.sh
git -C "$D" show HEAD:registres/go.md > registres/go.md
git -C "$D" show HEAD:.claude/hooks/garde_calcul.py > .claude/hooks/garde_calcul.py
git add -A && git commit -qm "base"
cp "$V2" "$P" && (cd prereg && sha256sum "$(basename "$P")" > "$(basename "$P").sha256")
cp "$E/B/revalidation-v2/controles_avant_depense_v7.sh" "$L" docs/procedures/revalidation-T0.5-v2/
git add -A && git commit -qm "S : v2 scellée (essai)"
git clone -q --bare . "$E/distant.git" && git remote add origin "$E/distant.git" && git fetch -q origin
echo "S = $(git rev-parse HEAD)"
cas() {   # $1 nom ; $2 code attendu ; $3 arguments du lanceur (« - » : les deux arguments normaux) ; puis l'environnement
    local nom=$1 attendu=$2 args=$3; shift 3
    rm -rf "$E/traces" "$E/compteur-heure"; : > "$E/journal-$nom.txt"
    local a=(111 "$E/traces"); [ "$args" = "-" ] || read -r -a a <<<"$args"
    env -u VAST_API_KEY HOME="$E/home" PATH="$E/bin-heure:$E/bin-df:/usr/bin:/bin" \
        HF_TOKEN=factice-hf-0000000 CONTROLE_IA_GITHUB_TOKEN=factice-gh-0000000 FAUX_VASTAI_JOURNAL="$E/journal-$nom.txt" \
        "$@" bash "$L" "${a[@]}" > "$E/sortie-$nom.txt" 2>&1
    local c=$?
    local cree; cree=$(grep -c "CREATION FACTICE" "$E/journal-$nom.txt")
    local clone="absent"; [ -e "$E/traces/clone-controles" ] && clone="PRÉSENT"
    local v="CONFORME"; [ "$c" = "$attendu" ] || v="NON CONFORME (attendu $attendu)"
    [ "$attendu" != 0 ] && [ "$cree" != 0 ] && [ "$attendu" != 4 ] && v="NON CONFORME (création alors qu'un arrêt était attendu)"
    echo "$nom : code $c ; créations factices $cree ; clone des contrôles $clone ; $v"
    grep -v '^$' "$E/sortie-$nom.txt" | tail -2 | sed 's/^/    | /' | cut -c1-180
}
cas M0-sain 0 - FAUX_X=1
cas M1-creee-mais-code-1 4 - FAUX_CODE_CREATION=1
cas M2-reponse-illisible 4 - FAUX_CREATION=illisible
cas M3-echec-creation 4 - 'FAUX_CREATION={"success": false, "msg": "non"}'
cas M4-heure-2345-avant-creation 3 - FAUX_HEURE2=2345
cas M4b-heure-2340-au-depart 3 - FAUX_HEURE1=2340
cas M5-place-traces 3 - FAUX_DF_TRACES=1
cas M6-controles-ko 2 - FAUX_KO=1
cas M7-offre-sans-prix 2 - FAUX_PRIX=null
cas M7b-prix-au-dessus-du-devis 3 - FAUX_PRIX=1.35
cas M8-jeton-absent 2 - HF_TOKEN=
cas M8b-jeton-github-absent 2 - CONTROLE_IA_GITHUB_TOKEN=
cas M12-argument-absent 2 "111" FAUX_X=1
cas M13-instance-non-toleree 2 - 'FAUX_INSTANCES=[{"id": 1, "actual_status": "running", "cur_state": "running"}]'
cas M14-toleree-mais-en-marche 2 - 'FAUX_INSTANCES=[{"id": 55292763, "actual_status": "running", "cur_state": "running"}]'
cp "$E/depot/registres/go.md" "$E/go-sauve.md"
GOV=$(sed -n 's/^- Version 2 (N-018) : .* ; décision de Lazar : \(GO-[0-9-]*\) (R-[0-9]*)\.$/\1/p' "$E/depot/$P")
echo "| GO-2026-10-11-98 | 2026-10-11 | révocation | révoque $GOV (N-018) | — | — | Lazar | essai |" >> "$E/depot/registres/go.md"
cas M9-go-revoque-courant 2 - FAUX_X=1
cp "$E/go-sauve.md" "$E/depot/registres/go.md"
cp "$E/B/revalidation-v2/controles_avant_depense_v7.sh" "$E/ctl-sauve.sh"
echo "# modifié" >> "$E/B/revalidation-v2/controles_avant_depense_v7.sh"
cas M10-controles-non-verses 2 - FAUX_X=1
cp "$E/ctl-sauve.sh" "$E/B/revalidation-v2/controles_avant_depense_v7.sh"
cas M11-sain-rejoue 0 - FAUX_X=1
grep -l 'secret\|factice-hf\|factice-gh' "$E"/sortie-*.txt "$E"/traces/* 2>/dev/null | sed 's/^/JETON AFFICHÉ : /' || true
echo "FIN DU BANC DU LANCEUR"
