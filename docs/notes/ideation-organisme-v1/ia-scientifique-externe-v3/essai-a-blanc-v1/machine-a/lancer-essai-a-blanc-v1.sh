#!/bin/bash
# Lancement de l'essai à blanc de la v3 sur A, v1 — session-depot, 30 octobre 2026 (R-808). À RELIRE ; lancé par Lazar.
# Relais FACTICE sur B : aucun modèle n'est appelé ; les phases de la v3 échoueront faute de vrai contenu, c'est attendu.
# L'essai éprouve la plomberie (épreuves E1 à E8 de architecture-essai-a-blanc-v1.md § 3), pas la science.
#
# Le jeton de course n'est PAS une clé : il n'ouvre que le relais (factice ici, plafonné). La v3 n'accepte l'authentification
# des agents que par son fichier d'environnement filtré (lecture du code, point 1b) : on l'écrit donc dans un fichier en
# mémoire vive (tmpfs), mode 600, effacé à la fin. Aucun `.env` à la racine de /opt/v3 (point 3a).
set -euo pipefail
cd /opt/v3
[ ! -e .env ] || { echo "un .env existe à la racine de la v3 : refus (point 3a)" >&2; exit 2; }
install -d -m 700 /run/essai /var/lib/essai/auth-vide /var/lib/essai/temp
[ -z "$(ls -A /var/lib/essai/auth-vide)" ] || { echo "auth_root non vide : refus (point 3b)" >&2; exit 2; }
read -rsp "jeton de course : " JETON; echo
printf 'ANTHROPIC_AUTH_TOKEN=%s\n' "$JETON" > /run/essai/course.env; unset JETON; chmod 600 /run/essai/course.env
trap 'shred -u /run/essai/course.env 2>/dev/null || rm -f /run/essai/course.env' EXIT
# journal de tous les conteneurs créés pendant l'essai (épreuve E8)
docker events --format '{{json .}}' --filter type=container > /var/log/essai/docker-events-v1.jsonl &
PID_EV=$!
export AGENT_CONTAINER_DISABLE_HOST_GATEWAY=1 AGENT_CONTAINER_MOUNT_DOCKER_SOCK=0 AGENTIC_TEMP_ROOT=/var/lib/essai/temp
# phases sans « review » (pas d'OpenAI, point 5a) ; 1 cycle ; borne de durée de l'hôte : 2 h
timeout 7200 agsci run tache-essai-a-blanc \
    container.network=agsci-interne-v1 posthoc.container.network=agsci-interne-v1 \
    container.auth_root=/var/lib/essai/auth-vide container.env_file=/run/essai/course.env \
    container.image=agentic-scientist/agent-cli-derivee-essai-v1 \
    execution.phases=task_drafting,investigation investigation.execution.workers=1 \
    investigation.execution.max_idea_cycles=1 \
    > /var/log/essai/agsci-essai-v1.log 2>&1 || echo "agsci : code $? (attendu : échec des phases, relais factice)"
kill "$PID_EV" 2>/dev/null || true
echo "fin : lancer les épreuves (verifier-epreuves-v1.sh), puis rapatrier /var/log/essai et le journal de B."
