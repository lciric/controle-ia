#!/usr/bin/env bash
# Enchaîne, dans l'ordre fixé par Lazar (R-543 ; plafond 35 USD par tour, R-544 ; clé RR_ANTHROPIC_API_KEY_LUC, R-547) : contrôle puis tour « mémoire du pôle » (v3, GO-2026-10-27-01), puis
# contrôle puis tour « Boucle d'or » (GO-2026-10-27-02). Un tour ne part que si son appel de contrôle rend les trois
# espèces OK. Journal : enchainer-tours-luc-v1.journal (heures, codes). Clés par variable, jamais affichées.
set -uo pipefail; set +x
[ -n "${RR_ANTHROPIC_API_KEY_LUC:-}" ] || { echo "RR_ANTHROPIC_API_KEY_LUC absente de cette session : rien n'est lancé (une session neuve, ou un processus redémarré, la lit)" >&2; exit 2; }
cd "$(dirname "$0")"
J=enchainer-tours-luc-v1.journal
[ ! -e "$J" ] || { echo "$J existe déjà (R12)" >&2; exit 2; }
log() { echo "$(date -u +%FT%TZ) $*" | tee -a "$J"; }
controle_ok() {  # $1 dossier, $2 GO, $3 sortie
    bash "$1/controler-especes-luc-v1.sh" "$2" "$3" >> "$J" 2>&1 || return 1
    python3 -I -c 'import json,sys; d=json.load(open(sys.argv[1])); sys.exit(0 if all(v["statut"]=="OK" for v in d["especes"].values()) else 1)' "$1/$3"
}
for t in "collisionneur-memoire-v3 GO-2026-10-27-01 appel-controle-especes-v3.json lancer-tour-memoire-v3-plafond35-luc.sh" \
         "collisionneur-boucle-d-or GO-2026-10-27-02 appel-controle-especes-v1.json lancer-tour-boucle-d-or-v1-plafond35-luc.sh"; do
    set -- $t
    if controle_ok "$1/tour" "$2" "$3"; then
        log "$1 : contrôle OK ($2), tour lancé"
        bash "$1/tour/$4" > "$1/tour/${4%.sh}.log" 2>&1; c=$?
        log "$1 : tour fini, code $c"
    else
        log "$1 : contrôle en échec ($2) : tour non lancé ; arrêt de l'enchaînement"; exit 3
    fi
done
log "enchaînement fini"
