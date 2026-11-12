python3 -I -B "$T/verifier_go_v5.py" "$DEPOT/registres/go.md" "$GO" "$(basename "$PREREG")" "$EMPREINTE_PREREG" "$PLAFOND_GO" \
    | tee -a "$T/lancement.txt" | grep -q ': conforme' || { echo "GO $GO non conforme pour cette expérience : pas de création"; exit 2; }
