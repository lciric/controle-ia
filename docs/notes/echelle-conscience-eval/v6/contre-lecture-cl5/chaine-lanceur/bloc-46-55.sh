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
