#!/bin/bash
# Épreuves E1 à E8 de l'essai à blanc de la v3, sur A, v1 — session-depot, 30 octobre 2026 (R-808). À RELIRE ; lancé par Lazar.
# Chaque épreuve imprime « E… RÉUSSIE » ou « E… ÉCHOUÉE » ; une seule ÉCHOUÉE interdit la course réelle (étape 3).
# Les sondes tournent dans un conteneur jetable de l'image dérivée, sur le réseau interne, comme les agents.
set -uo pipefail
IMG=agentic-scientist/agent-cli-derivee-essai-v1
SONDE=(docker run --rm --network agsci-interne-v1 --entrypoint sh "$IMG" -c)
ok() { echo "$1 RÉUSSIE"; }; ko() { echo "$1 ÉCHOUÉE : $2"; ECHEC=1; }; ECHEC=0

# E1 aucun accès direct au Web hors du mandataire ; le Web passe par lui
"${SONDE[@]}" 'curl -sS --noproxy "*" --max-time 8 --resolve example.com:443:93.184.215.14 https://example.com -o /dev/null' \
  && ko E1 "sortie directe possible" || ok "E1a (aucune route directe)"
"${SONDE[@]}" 'curl -sS --noproxy "*" --max-time 15 https://example.com -o /dev/null' \
  && grep -q '"hote": "example.com"' /var/log/essai/mandataire-v1.jsonl && ok "E1b (Web par le mandataire, journalisé)" \
  || ko E1b "le Web ne passe pas par le mandataire"

# E2 copie publique bloquée (formes et casses), cas sain permis
for u in https://github.com/lciric/controle-ia https://github.com/LCIRIC/Controle-IA \
         https://raw.githubusercontent.com/lciric/controle-ia/main/README.md \
         https://api.github.com/repos/lciric/controle-ia; do
  code=$("${SONDE[@]}" "curl -s -o /dev/null -w '%{http_code}' --max-time 15 $u")
  [ "$code" = 403 ] && ok "E2 ($u)" || ko E2 "$u rend $code"
done
code=$("${SONDE[@]}" "curl -s -o /dev/null -w '%{http_code}' --max-time 15 https://github.com/SakanaAI/AI-Scientist-v3")
[ "$code" != 403 ] && ok "E2 cas sain" || ko E2 "cas sain refusé"

# E3 aucun identifiant de l'hôte dans les conteneurs ; aucune socket Docker
"${SONDE[@]}" 'ls -A ~/.claude ~/.codex ~/.config/gcloud 2>/dev/null; env | grep -i -E "AWS_|OPENAI|GEMINI|CLAUDE_CODE_OAUTH|ANTHROPIC_API_KEY"; ls /var/run/docker.sock 2>/dev/null' \
  | grep -q . && ko E3 "identifiant ou socket présent" || ok E3

# E4 aucun appel à OpenAI ni aux autres fournisseurs en direct
grep -E '"hote": "[^"]*(openai\.com|chatgpt\.com|anthropic\.com|amazonaws\.com|googleapis\.com)"' /var/log/essai/mandataire-v1.jsonl \
  | grep -v '"statut": "refus"' | grep -q . && ko E4 "appel direct à un fournisseur permis" || ok E4
grep -q -i "review" /var/log/essai/agsci-essai-v1.log && ko E4 "phase de relecture lancée" || ok "E4 (pas de relecture)"

# E5 tous les appels de modèle passent par B (le journal de B est rapatrié à côté, par Lazar)
[ -s /var/log/essai/journal-relais-b-v1.jsonl ] && ok "E5 (appels vus par B)" || ko E5 "aucun appel vu par B (réglages gérés non lus ?)"

# E6 le plafond de B tient : appels au-delà du plafond fictif → 402
"${SONDE[@]}" 'for i in $(seq 1 60); do curl -s -o /dev/null -w "%{http_code}\n" -H "Authorization: Bearer $J" -H "content-type: application/json" -d "{\"model\":\"claude-opus-4-7\"}" http://relais:8790/v1/messages; done' \
  | grep -q 402 && ok E6 || ko E6 "jamais de 402 (lancer E6 avec J posé à un jeton valide)"

# E7 destruction : faite par Lazar avec detruire-machines-v1.sh (identifiants consignés dans registres/arrets.md)
echo "E7 à faire à la fin : detruire-machines-v1.sh"

# E8 chaque conteneur créé : réseau agsci-interne-v1, pas de --privileged, pas de socket
python3 - <<'EOF' || ECHEC=1
import json, subprocess
ids = {json.loads(l).get("id") for l in open("/var/log/essai/docker-events-v1.jsonl") if '"create"' in l}
mauvais = []
for i in ids:
    try: d = json.loads(subprocess.check_output(["docker", "inspect", i]))[0]
    except Exception: continue
    hc = d["HostConfig"]
    if hc.get("Privileged") or "agsci-interne-v1" not in (hc.get("NetworkMode") or "") or \
       any("docker.sock" in m for m in hc.get("Binds") or []): mauvais.append(i[:12])
print("E8 RÉUSSIE" if not mauvais else f"E8 ÉCHOUÉE : {mauvais}")
raise SystemExit(1 if mauvais else 0)
EOF
[ "$ECHEC" = 0 ] && echo "ESSAI À BLANC : toutes les épreuves réussies" || echo "ESSAI À BLANC : au moins une épreuve échouée — pas de course réelle"
