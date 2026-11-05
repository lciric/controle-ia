#!/bin/bash
# Guetteur de la relance de R1 (GO-2026-11-02-27) : lit l'état de l'instance, les jalons du journal de l'amorce et la tête de
# la branche de résultats, toutes les 5 minutes ; ne lit jamais d'activations ni de scores ; ne détruit rien (la destruction
# se fait par la session, par identifiant). Sort (et réveille la session) sur : ligne « AMORCE … fin » ; instance absente ou
# arrêtée ; jalon inattendu (valeur de délai ou de plafond différente) ; 13 h écoulées.
#   bash guetteur_r1_relance_v3.sh ID JOURNAL
set -u
ID="$1"; J="$2"; VB=/opt/vastai-venv-v1/bin; T0=$(date -u +%s); DERNIER=""
note() { echo "$(date -u +%FT%TZ) $*" >> "$J"; }
note "guetteur : instance $ID"
while :; do
  E=$($VB/vastai show instance "$ID" --raw 2>/dev/null | python3 -I -c '
import json,sys
try:
    d=json.load(sys.stdin)
except Exception:
    print("illisible"); sys.exit(0)
print(d.get("actual_status"), d.get("cur_state"), round(float(d.get("dph_total") or 0),4))' 2>/dev/null)
  L=$($VB/vastai logs "$ID" --tail 400 2>/dev/null | grep -E 'AMORCE|branche .* poussée|tests :|passed|etape=|DELAI_REJEU_MIN|plafond de l.amorce|ARRÊT|arrêt|refus' | grep -vE 'activations?=|score' | tail -12)
  B=$(git -C /home/user/controle-ia-travail ls-remote origin refs/heads/calcul/r1-relance-v3-reel-v1 2>/dev/null | cut -c1-12)
  ETAT="état=[$E] branche=[$B]"
  if [ "$ETAT|$L" != "$DERNIER" ]; then note "$ETAT"; [ -n "$L" ] && echo "$L" | sed 's/^/    /' >> "$J"; DERNIER="$ETAT|$L"; fi
  if echo "$L" | grep -qE 'AMORCE.*fin'; then note "FIN : ligne de fin de l'amorce vue"; exit 0; fi
  if echo "$L" | grep -qE 'DELAI_REJEU_MIN=' && ! echo "$L" | grep -qE 'DELAI_REJEU_MIN=600'; then note "ANOMALIE : DELAI_REJEU_MIN différent de 600"; exit 3; fi
  if echo "$L" | grep -qE 'plafond de l.amorce [0-9]+ min' && ! echo "$L" | grep -qE 'plafond de l.amorce 720 min'; then note "ANOMALIE : plafond de l'amorce différent de 720"; exit 3; fi
  case "$E" in illisible*|"") note "instance illisible ou absente"; sleep 60; E2=$($VB/vastai show instances --raw 2>/dev/null | python3 -I -c "
import json,sys
d=json.load(sys.stdin); print(sum(1 for i in d if str(i.get('id'))=='$ID'))" 2>/dev/null); [ "$E2" = "0" ] && { note "FIN : instance absente du compte"; exit 4; } ;; esac
  case "$E" in exited*|stopped*|offline*) note "FIN : instance arrêtée ($E)"; exit 5;; esac
  [ $(( $(date -u +%s) - T0 )) -gt 46800 ] && { note "FIN : 13 h écoulées sans ligne de fin"; exit 6; }
  sleep 300
done
