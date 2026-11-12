#!/bin/bash
# Mise en place de la machine A (agents, Docker) pour l'essai à blanc de la v3, v1 — session-depot, 30 octobre 2026 (R-808).
# À RELIRE avant exécution. Jamais exécuté par la session. À lancer en root sur A (Debian 12), après création par Lazar.
# Aucune clé : A ne reçoit que le jeton de course (pas une clé ; il n'ouvre que le relais plafonné de B).
#
# Variables à poser par Lazar (aucune n'est une clé) :
#   IP_B, IP_LAZAR, CLE_PUB_B (clé publique WireGuard de B)
# Fichiers du dépôt copiés dans /opt/essai (empreintes vérifiées) : dnsmasq-interne-v1.conf, pare-feu-machine-a-v1.rules,
#   mandataire_regles_v1.py, mandataire_addon_v1.py, image-derivee/{Dockerfile,managed-settings.json}.
set -euo pipefail
: "${IP_B:?}" "${IP_LAZAR:?}" "${CLE_PUB_B:?}"
umask 077
cd /opt/essai && sha256sum -c --quiet *.sha256 image-derivee/*.sha256
apt-get update -q && DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
    docker.io wireguard iptables git ca-certificates
# (1) démon Docker : espace d'utilisateurs remappé, aucun nouveau privilège, IPv6 coupé, pas de communication libre
cat > /etc/docker/daemon.json <<'EOF'
{ "userns-remap": "default", "no-new-privileges": true, "ipv6": false, "icc": false, "live-restore": false,
  "log-driver": "json-file", "dns": ["172.30.0.4"] }
EOF
systemctl restart docker

# (2) WireGuard : A = 10.77.0.2
install -d -m 700 /etc/wireguard
[ -f /etc/wireguard/a.key ] || wg genkey > /etc/wireguard/a.key
wg pubkey < /etc/wireguard/a.key > /etc/wireguard/a.pub
cat > /etc/wireguard/wg0.conf <<EOF
[Interface]
Address = 10.77.0.2/30
ListenPort = 51820
PostUp = wg set %i private-key /etc/wireguard/a.key
[Peer]
PublicKey = ${CLE_PUB_B}
AllowedIPs = 10.77.0.1/32
Endpoint = ${IP_B}:51820
EOF
systemctl enable --now wg-quick@wg0

# (3) réseaux : interne sans route (agents), sortie (mandataire et passe-relais seulement)
docker network create --internal --subnet 172.30.0.0/24 -o com.docker.network.bridge.name=br-agsci-int agsci-interne-v1
docker network create --subnet 172.31.0.0/24 -o com.docker.network.bridge.name=br-agsci-sor agsci-sortie-v1

# (4) pare-feu (adresses de Lazar et de B remplacées), IPv6 coupé
sed -e "s#203.0.113.10/32#${IP_LAZAR}/32#" -e "s#198.51.100.20/32#${IP_B}/32#" pare-feu-machine-a-v1.rules | iptables-restore -n
ip6tables -P INPUT DROP; ip6tables -P FORWARD DROP

# (5) serveur de noms, mandataire, passe-relais ; journaux dans /var/log/essai (rapatriés et scellés à la fin)
install -d -m 755 /var/log/essai /opt/essai/ca
docker run -d --name dns-v1 --network agsci-interne-v1 --ip 172.30.0.4 --cap-add NET_ADMIN \
    -v /opt/essai/dnsmasq-interne-v1.conf:/etc/dnsmasq.conf:ro -v /var/log/essai:/journal \
    docker.io/4km3/dnsmasq:2.90-r3 -k   # image à épingler par empreinte avant usage (R9)
docker create --name mandataire-v1 --network agsci-sortie-v1 --ip 172.31.0.2 \
    -v /opt/essai:/mandataire:ro -v /var/log/essai:/journal -v /opt/essai/ca:/home/mitmproxy/.mitmproxy \
    docker.io/mitmproxy/mitmproxy:11.0.2 \
    mitmdump --mode reverse:https://exemple.invalid@443 --mode reverse:http://exemple.invalid@80 --mode regular@3128 \
    --set keep_host_header=true -s /mandataire/mandataire_addon_v1.py --set journal_mandataire=/journal/mandataire-v1.jsonl
docker network connect --ip 172.30.0.2 agsci-interne-v1 mandataire-v1
docker start mandataire-v1
docker run -d --name passe-relais-v1 --network agsci-sortie-v1 --ip 172.31.0.3 docker.io/alpine/socat:1.8.0.0 \
    TCP-LISTEN:8790,fork,reuseaddr TCP:10.77.0.1:8790
docker network connect --ip 172.30.0.3 agsci-interne-v1 passe-relais-v1

# (6) v3 aux commits épinglés, image construite une fois, empreinte consignée (R9), puis image dérivée
git clone https://github.com/SakanaAI/AI-Scientist-v3.git /opt/v3 && git -C /opt/v3 checkout df8313889a004f8a44a472e19a833cd547bb828a
echo "construire l'image de la v3 selon /opt/v3/docs/install.md, puis :"
echo "  docker image inspect agentic-scientist/agent-cli:latest --format '{{index .RepoDigests 0}} {{.Id}}' >> /var/log/essai/images-v1.txt"
echo "  cp /opt/essai/ca/mitmproxy-ca-cert.pem /opt/essai/image-derivee/mandataire-ca.crt"
echo "  docker build --build-arg IMAGE_V3=<empreinte> -t agentic-scientist/agent-cli-derivee-essai-v1 /opt/essai/image-derivee"
echo "A prête. Clé publique de A (à donner à B) : $(cat /etc/wireguard/a.pub)"
