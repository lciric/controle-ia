set -euo pipefail
trap 'echo "arrêt avant la création (ligne $LINENO)"; exit 2' ERR
T=/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/contre-lecture-echelle-v6/chaine-lanceur/traces-GO-2026-10-27-10-600470b; COMMIT=600470b1b6a780193ccc4de590a362013ddae4ea; GO=GO-2026-10-27-10; DEPOT=/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/contre-lecture-echelle-v6/chaine-lanceur/depot; PREREG=prereg/test-echelle-conscience-eval-v6.md; PLAFOND_GO=8.00
mkdir -p "$T"
printf 'lanceur %s ; départ %s UTC\n' "$(sha256sum "$0" | cut -d' ' -f1)" "$(date -u +%FT%TZ)" >> "$T/lancement.txt"
# 0. préenregistrement scellé et conforme (R1, R2 ; CLH-08)
(cd "$DEPOT" && PYTHONPATH=src python3 -I -B -c 'import sys; sys.path.insert(0, "src"); from controle_ia.prereg import exiger_prereg_scelle; print(exiger_prereg_scelle(sys.argv[1]))' "$PREREG") \
    | sed 's/^/préenregistrement scellé : /' | tee -a "$T/lancement.txt" | grep -q 'scellé : [0-9a-f]\{64\}' \
    || { echo "préenregistrement non scellé ou non conforme : pas de création"; exit 2; }
EMPREINTE_PREREG=$(grep -o 'scellé : [0-9a-f]\{64\}' "$T/lancement.txt" | tail -1 | cut -d' ' -f3)
grep -qF "$COMMIT" "$DEPOT/$PREREG" \
    || { echo "le préenregistrement scellé ne cite pas le commit $COMMIT (CLW-04) : pas de création"; exit 2; }
echo "préenregistrement : cite le commit $COMMIT" | tee -a "$T/lancement.txt"
cp /tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/contre-lecture-echelle-v6/chaine-lanceur/verifier_go_v5.py "$T/verifier_go_v5.py"
python3 -I -B "$T/verifier_go_v5.py" "$DEPOT/registres/go.md" "$GO" "$(basename "$PREREG")" "$EMPREINTE_PREREG" "$PLAFOND_GO" \
    | tee -a "$T/lancement.txt" | grep -q ': conforme' || { echo "GO $GO non conforme pour cette expérience : pas de création"; exit 2; }
echo "passe"
