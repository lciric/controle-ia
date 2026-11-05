#!/usr/bin/env bash
# Banc d'essai des contrôles avant dépense v7 (R5 ; R-137) : un cas sain et des artefacts,
# chacun joué contre le script entier sur un dépôt jetable et un dépôt nu local. La copie jouée ne diffère du script
# que par l'adresse du dépôt et les épingles du candidat final et des rapports (celles de l'essai). Le scellement y
# est simulé (GO fictif accordé par Lazar sur N-018, N-018 tranché, ligne R-990 fictive du GO, deux rapports fictifs :
# bancs finaux) ; la v2 saine est produite par remplir_revalidation_v2_r4.py en mode reel.
# Artefacts : ceux du banc v5d (A1 à A17, A3b, A9b), adaptés, et X1 à X10 tirés de la vérification (VC-01 à VC-04,
# VC-10, VT-09, VT-10), plus X11 (rapport non épinglé ajouté), X12 (candidat final altéré), Z1 et Z2 (épingle des
# rapports vide ou mal formée : code 2 attendu, sur la v2 saine ; CM-07).
# Usage : essais_controles_v7.sh DEPOT_SOURCE RACINE_NEUVE
set -uo pipefail
SRC=$1; R=$2
H=$(cd "$(dirname "$0")" && pwd)
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
P=prereg/T0.5-revalidation-equivalence-pilote-v2.md; P1=prereg/T0.5-revalidation-equivalence-pilote-v1.md
CL=prereg/contre-lectures; GO=GO-2026-10-11-99; REG=R-990
CAND=brouillons/T0.5-revalidation-equivalence-pilote-v2-candidat5.md
FICTIFS="T0.5-revalidation-v2-verification-banc-controles-final-v1.tar T0.5-revalidation-v2-verification-banc-lanceur-scellement-v1.tar"
NOMS="$FICTIFS"   # complétés plus bas par tous les rapports de la v2 présents (CM-07)
[ -e "$R" ] && { echo "$R existe déjà (R12)"; exit 2; }
mkdir -p "$R" && cd "$R" || exit 2
git clone -q --no-local "$SRC" source && cd source || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
python3 - <<EOF || exit 2
from pathlib import Path
d = Path("registres/decisions.md"); t = d.read_text(encoding="utf-8")
l = [x for x in t.split("\n") if x.startswith("| N-018 |")][0]
t = t.replace(l, l.rsplit("| en attente |", 1)[0] + "| tranché : option (a), $GO (essai) |")
t = t.rstrip("\n") + "\n| $REG | 2026-10-11 | essai : $GO consigné | — |\n"
d.write_text(t, encoding="utf-8")
g = Path("registres/go.md")
g.write_text(g.read_text(encoding="utf-8").rstrip("\n") + "\n| $GO | 2026-10-11 | revendication | N-018, option (a) (essai) | — | — | Lazar | $REG (essai) |\n", encoding="utf-8")
for n in "$FICTIFS".split():
    Path("$CL/" + n).write_text("rapport fictif (essai) " + n + "\n", encoding="utf-8")
EOF
for n in $FICTIFS; do PYTHONPATH=src "$PY" -m controle_ia.scellement sceller "$CL/$n" > /dev/null || exit 2; done
git add -A registres $CL && git commit -qm "essai : préalables simulés du scellement de la v2" || exit 2
C1=$(git rev-parse HEAD)
NOMS=$(git ls-tree -r --name-only HEAD $CL/ | grep -E "^$CL/T0\\.5-revalidation-v2-(relecture|verification)-[a-z-]+-v1\\.(md|json|tar)$" | xargs -n1 basename)
echo "rapports attendus de l'essai : $(echo $NOMS | wc -w)"
PAIRES=""; for n in $NOMS; do PAIRES="$PAIRES $n=$(sha256sum "$CL/$n" | cut -d' ' -f1)"; done; PAIRES=${PAIRES# }
normaliser() { sed -E '3s/[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}/AAAA-MM-JJ HH:MM/; 8s/[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}/AAAA-MM-JJ HH:MM/' "$1" \
    | sed -E 's/^(- Version 2 \(N-018\) : .*) Pièces : .*$/\1 Pièces : (remplies au scellement)./' | sha256sum | cut -d' ' -f1; }
NV=$(normaliser "$CAND"); SV=$(sha256sum "$CAND" | cut -d' ' -f1)
git clone -q --bare . "$R/distant.git" || exit 2
sed -e "s|^DEPOT=.*|DEPOT=$R/distant.git|" -e "s|^CANDIDAT_FINAL=.*|CANDIDAT_FINAL=$SV|" \
    -e "s|^CANDIDAT_FINAL_CHEMIN=.*|CANDIDAT_FINAL_CHEMIN=$CAND|" -e "s|^CANDIDAT_NORMALISE=.*|CANDIDAT_NORMALISE=$NV|" \
    -e "s|^RAPPORTS_ATTENDUS=.*|RAPPORTS_ATTENDUS=\"$PAIRES\"|" "$H/controles_avant_depense_v7.sh" > "$R/controles-essai.sh"
diff "$H/controles_avant_depense_v7.sh" "$R/controles-essai.sh" | grep -c '^>' | sed 's/^/lignes changées dans la copie : /'
"$PY" -I "$H/remplir_revalidation_v2_r4.py" . 6ec7434119781a3abebac789174101b9ed6ae087 reel "$(date -u '+%Y-%m-%d %H:%M UTC')" \
    "$R/v2-saine.md" --controles "$R/controles-essai.sh" --candidat-relu brouillons/T0.5-revalidation-equivalence-pilote-v2-candidat2.md \
    --candidat-verifie brouillons/T0.5-revalidation-equivalence-pilote-v2-candidat3.md --candidat-final "$CAND" --go "$GO" --registre "$REG" || exit 2
NS=$(normaliser "$R/v2-saine.md"); echo "empreinte normalisée : candidat vérifié $NV ; v2 saine de l'essai $NS"
[ "$NV" = "$NS" ] || { echo "la v2 de l'essai ne se normalise pas en le candidat vérifié"; exit 2; }
sceller_v2() { PYTHONPATH=src "$PY" -c "from controle_ia.prereg import sceller_prereg; sceller_prereg('$P')" >/dev/null; }
resceller() { local f; for f in "$@"; do (cd "$(dirname "$f")" && sha256sum "$(basename "$f")" > "$(basename "$f").sha256"); done; }
jouer() {   # $1 nom, $2 code attendu, $3 motif KO attendu (vide : cas sain), $4 modification avant le commit, $5 après
    local nom=$1 attendu=$2 motif=$3 avant=$4 apres=${5:-}
    git checkout -q -B "art-$nom" "$C1" && cp "$R/v2-saine.md" "$P" && sceller_v2 || { echo "$nom : montage impossible"; return; }
    eval "$avant"
    git add -A . >/dev/null 2>&1; git commit -qm "essai : $nom" || { echo "$nom : commit impossible"; return; }
    local s; s=$(git rev-parse HEAD)
    git push -q "$R/distant.git" "art-$nom" >/dev/null 2>&1
    eval "$apres"
    bash "$R/controles-essai.sh" "$s" "$R/clone-$nom" > "$R/sortie-$nom.txt" 2>&1; local c=$?
    rm -rf "$R/clone-$nom"
    local verdict="CONFORME"
    [ "$c" = "$attendu" ] || verdict="NON CONFORME (code $c, attendu $attendu)"
    if [ -n "$motif" ] && ! grep -q "^KO .*$motif" "$R/sortie-$nom.txt"; then verdict="NON CONFORME (KO « $motif » absent)"; fi
    echo "$nom : code $c ; $(grep -c '^KO' "$R/sortie-$nom.txt") KO ; $verdict"
    grep '^KO' "$R/sortie-$nom.txt" | sed 's/^/    /' | cut -c1-200
}
pieces() { sed -i -E "$1" "$P" && resceller "$P"; }    # modifie la fin « Pièces » et re-scelle de façon cohérente
remplacer_rapport_chaine() {   # X1 : rapport réécrit et re-scellé avant la génération, fin « Pièces » qui cite sa nouvelle empreinte
    local f=$CL/T0.5-revalidation-v2-relecture-chaine-v1.md n
    echo ' réécrit' >> "$f"; resceller "$f"; n=$(sha256sum "$f" | cut -d' ' -f1)
    sed -i -E "s/(relecture-chaine-v1\.md\` \(\`)[0-9a-f]{64}/\1$n/" "$P"; resceller "$P"
}
jouer A0-sain 0 "" ":"
jouer A1-v1-alteree-rescellee 1 "v1 : sceau ou citation" "sed -i '1s/— v1/— v1 (altérée)/' $P1 && resceller $P1"
jouer A2-v1-alteree-sans-sceau 1 "v1 : sceau ou citation" "sed -i '1s/— v1/— v1 (altérée)/' $P1"
jouer A3-rapport-altere 1 "rapport T0.5-revalidation-v2-relecture-texte-v1.md" "echo x >> $CL/T0.5-revalidation-v2-relecture-texte-v1.md"
jouer A3b-rapport-altere-rescelle 1 "rapport T0.5-revalidation-v2-relecture-texte-v1.md" "echo x >> $CL/T0.5-revalidation-v2-relecture-texte-v1.md && resceller $CL/T0.5-revalidation-v2-relecture-texte-v1.md"
jouer A4-rapport-absent 1 "rapport T0.5-revalidation-v2-relecture-code-v1.md" "git rm -q $CL/T0.5-revalidation-v2-relecture-code-v1.md $CL/T0.5-revalidation-v2-relecture-code-v1.md.sha256"
jouer A5-rapport-non-cite 1 "fin « Pièces » différente" "pieces 's/ ; \`T0\.5-revalidation-v2-relecture-code-v1\.md\` \(\`[0-9a-f]{64}\`\)//'"
jouer A6-branche-v2-presente 1 "branche de résultats" ":" "git push -q $R/distant.git art-A6-branche-v2-presente:refs/heads/calcul/t05-revalidation-reel-v2"
git -C "$R/distant.git" branch -D calcul/t05-revalidation-reel-v2 >/dev/null
jouer A7-corps-modifie 1 "≠ candidat final" "sed -i '0,/0,15/s/0,15/0,25/' $P && resceller $P"
jouer A8-code-ajoute 1 "arbre gelé modifié" "echo '# essai' >> src/controle_ia/__init__.py"
jouer A9-pieces-sans-go 1 "fin « Pièces » différente" "pieces 's/ ; décision de Lazar : GO-[0-9-]+ \(R-990\)\././'"
jouer A9b-partie-fixe-reecrite 1 "≠ candidat final" "sed -i 's/relu avant le scellement par des sous-agents neufs/non relu/' $P && resceller $P"
jouer A10-entree-en-double 1 "entrée Version 2" "sed -i '10a - Version 2 (N-018) : contenu arbitraire. Pièces : rien.' $P && resceller $P"
jouer A11-go-absent 1 "GO $GO : ligne absente" "sed -i '/^| $GO |/d' registres/go.md"
jouer A12-n018-en-attente 1 "N-018 absent, en attente" "sed -i -E 's/^(\| N-018 \|.*)\| tranché : [^|]*\|$/\1| en attente |/' registres/decisions.md"
jouer A13-suite-alteree 1 "sortie de la suite" "echo x >> docs/procedures/revalidation-T0.5-v2/suite-6ec7434-environnement-neuf-v1.txt"
jouer A14-entree-deplacee 1 "entrée Version 2" "python3 -c \"
from pathlib import Path
p = Path('$P'); l = p.read_text(encoding='utf-8').split(chr(10))
i = next(k for k, x in enumerate(l) if x.startswith('- Version 2 (N-018) : '))
e = l.pop(i); j = next(k for k, x in enumerate(l) if x.startswith('- Contrôle mécanique des corrections du brouillon 6'))
l.insert(j, e); p.write_text(chr(10).join(l), encoding='utf-8')\" && resceller $P"
jouer A15-r136-absent 1 "R-136 absent" "sed -i '/^| R-136 |/d' registres/decisions.md"
jouer A16-candidat-relu-faux 1 "fin « Pièces » différente" "pieces 's/candidat relu (\`[^\`]*\`) \(\`af09c78b/candidat relu \1 (\`bf09c78b/'"
jouer A17-branche-citee-autre 1 "PREREG ou BRANCHE" "sed -i '3s/calcul\/t05-revalidation-reel-v2/calcul\/t05-revalidation-reel-v3/' $P && resceller $P"
jouer X1-rapport-remplace-avant 1 "rapport T0.5-revalidation-v2-relecture-chaine-v1.md" "remplacer_rapport_chaine"
jouer X2-texte-libre-dans-pieces 1 "fin « Pièces » différente" "pieces 's/ ; corrections : / ; NOTE : seuil relevé, Tests attendus : \`669\` ; corrections : /'"
jouer X3-go-revocation 1 "GO $GO : ligne absente" "sed -i -E 's/^\| $GO \| 2026-10-11 \| revendication \|(.*)\| Lazar \|/| $GO | 2026-10-11 | révocation |\1| session |/' registres/go.md"
jouer X4-registre-inexistant 1 "ligne R-999 absente" "pieces 's/\(R-990\)\.$/(R-999)./'"
jouer X5-n018-refuse 1 "N-018 absent, en attente" "sed -i -E 's/^(\| N-018 \|.*)\| tranché : [^|]*\|$/\1| refusé : option (b) retenue ($GO) |/' registres/decisions.md"
jouer X6-dates-libres 1 "dates des lignes 3 et 8" "sed -i -E '3s/[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}/2019-01-01 00:00/; 8s/[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}/2031-12-31 23:59/' $P && resceller $P"
jouer X7-candidat-relu-double 1 "fin « Pièces » différente" "pieces 's/Pièces : /Pièces : candidat relu \`x\` (\`0000\`) ; /'"
jouer X8-candidat-verifie-altere 1 "candidat brouillons/T0.5-revalidation-equivalence-pilote-v2-candidat3.md" "echo x >> brouillons/T0.5-revalidation-equivalence-pilote-v2-candidat3.md && resceller brouillons/T0.5-revalidation-equivalence-pilote-v2-candidat3.md"
jouer X9-processeur-altere 1 "pièce traces/t05-instance-55292763-processeur-20261011/processeur.json" "echo ' ' >> traces/t05-instance-55292763-processeur-20261011/processeur.json && (cd traces/t05-instance-55292763-processeur-20261011 && sha256sum processeur.json > empreintes.sha256)"
jouer X10-go-revoque-ensuite 1 "GO $GO révoqué" "echo '| GO-2026-10-11-98 | 2026-10-11 | révocation | révoque $GO (N-018) | — | — | Lazar | essai |' >> registres/go.md"
jouer X11-rapport-non-epingle 1 "rapports de la v2 présents à S" "echo x > $CL/T0.5-revalidation-v2-verification-supplement-v1.md && resceller $CL/T0.5-revalidation-v2-verification-supplement-v1.md"
jouer X12-candidat-final-altere 1 "candidat $CAND" "echo x >> $CAND && resceller $CAND"
# Z1, Z2 : épingle des rapports vide ou mal formée, sur la v2 saine (code 2 attendu, aucun contrôle joué)
git checkout -q -B art-Z "$C1" && cp "$R/v2-saine.md" "$P" && sceller_v2 && git add -A . && git commit -qm "essai : Z" && git push -q "$R/distant.git" art-Z
SZ=$(git rev-parse HEAD)
for z in Z1-rapports-vides Z2-paire-mal-formee; do
    case $z in Z1-*) v='RAPPORTS_ATTENDUS=""' ;; *) v='RAPPORTS_ATTENDUS="T0.5-revalidation-v2-relecture-texte-v1.md=abc"' ;; esac
    sed "s|^RAPPORTS_ATTENDUS=.*|$v|" "$R/controles-essai.sh" > "$R/controles-$z.sh"
    bash "$R/controles-$z.sh" "$SZ" "$R/clone-$z" > "$R/sortie-$z.txt" 2>&1; c=$?; rm -rf "$R/clone-$z"
    [ "$c" = 2 ] && grep -q "CM-07" "$R/sortie-$z.txt" && echo "$z : code $c ; CONFORME" || echo "$z : code $c ; NON CONFORME (code 2 et message CM-07 attendus)"
    sed 's/^/    /' "$R/sortie-$z.txt" | head -2
done
echo "FIN DU BANC"
