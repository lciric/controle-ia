# Image dérivée de l'Agentic Scientist v3 pour l'essai à blanc, v1 — session-depot, 30 octobre 2026 (R-808).
# Le code de la v3 n'est PAS modifié : on part de l'image construite depuis le dépôt aux commits épinglés
# (SakanaAI/AI-Scientist-v3 @ df8313889a004f8a44a472e19a833cd547bb828a, headless-cli @ 93cd9b0…), puis on ajoute seulement :
#   1. les réglages gérés de Claude Code (adresse du relais, mandataire, trafic non essentiel coupé) — fichier, qui survit
#      à l'effacement d'environnement des figures de concept (lecture du code, point 1d) ; chemin SUPPOSÉ pour la version
#      de Claude Code de l'image, à éprouver (épreuve E5) ;
#   2. l'autorité du mandataire (magasin du système, Node, pip, requests).
# Aucune clé, aucun jeton dans l'image. Le jeton de course arrive à l'exécution par le fichier d'environnement de course
# (seule voie que le filtre du `.env` laisse passer : `ANTHROPIC_AUTH_TOKEN`).
#
# Construction (sur A, après `construire-image-v3.sh`) :
#   docker build --build-arg IMAGE_V3=agentic-scientist/agent-cli@sha256:<empreinte consignée> \
#                -t agentic-scientist/agent-cli-derivee-essai-v1 .
ARG IMAGE_V3
FROM ${IMAGE_V3}
USER root
COPY managed-settings.json /etc/claude-code/managed-settings.json
COPY mandataire-ca.crt /usr/local/share/ca-certificates/mandataire-essai-v1.crt
RUN chmod 0644 /etc/claude-code/managed-settings.json /usr/local/share/ca-certificates/mandataire-essai-v1.crt \
 && update-ca-certificates \
 && printf '[global]\ncert = /etc/ssl/certs/ca-certificates.crt\n' > /etc/pip.conf
ENV NODE_EXTRA_CA_CERTS=/usr/local/share/ca-certificates/mandataire-essai-v1.crt \
    REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt \
    SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt \
    AGENT_CONTAINER_DISABLE_HOST_GATEWAY=1
USER agent
