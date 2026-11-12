#!/bin/bash
# Mise en place de la machine B (relais) pour l'essai à blanc de la v3, v1 — session-depot, 30 octobre 2026 (R-808).
# À RELIRE avant exécution. Jamais exécuté par la session. À lancer en root sur B (Debian 12), après création par Lazar.
# Essai à blanc : relais FACTICE, aucune clé Anthropic sur B. Pour la course réelle (étape 3), le relais réel remplacera le
# factice ; sa clé dédiée et plafonnée sera posée par Lazar à la main, par variable, jamais dans un fichier.
#
# Variables à poser par Lazar avant de lancer (aucune n'est une clé) :
#   IP_A        adresse publique de A (seule source admise pour WireGuard)
#   IP_LAZAR    adresse d'où Lazar se connecte en SSH
#   CLE_PUB_A   clé publique WireGuard de A (publique : pas un secret)
set -euo pipefail
: "${IP_A:?}" "${IP_LAZAR:?}" "${CLE_PUB_A:?}"
umask 077
apt-get update -q && DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends wireguard iptables python3

# (1) WireGuard : B = 10.77.0.1, A = 10.77.0.2 ; clé privée de B créée ici, jamais copiée ailleurs
install -d -m 700 /etc/wireguard
[ -f /etc/wireguard/b.key ] || wg genkey > /etc/wireguard/b.key
wg pubkey < /etc/wireguard/b.key > /etc/wireguard/b.pub
cat > /etc/wireguard/wg0.conf <<EOF
[Interface]
Address = 10.77.0.1/30
ListenPort = 51820
PostUp = wg set %i private-key /etc/wireguard/b.key
[Peer]
PublicKey = ${CLE_PUB_A}
AllowedIPs = 10.77.0.2/32
Endpoint = ${IP_A}:51820
EOF
systemctl enable --now wg-quick@wg0
echo "clé publique de B (à donner à A) : $(cat /etc/wireguard/b.pub)"

# (2) Pare-feu : SSH depuis Lazar ; WireGuard depuis A ; relais sur wg0 seulement ; tout le reste refusé ; IPv6 coupé
iptables -F INPUT; iptables -P INPUT DROP
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -s "$IP_LAZAR" -j ACCEPT
iptables -A INPUT -p udp --dport 51820 -s "$IP_A" -j ACCEPT
iptables -A INPUT -i wg0 -s 10.77.0.2 -p tcp --dport 8790 -j ACCEPT
ip6tables -P INPUT DROP; ip6tables -P FORWARD DROP

# (3) Relais factice : à copier depuis le dépôt (relais_factice_v1.py, empreinte vérifiée), lancé par Lazar :
#   install -d -m 700 /opt/relais /var/log/relais-factice
#   sha256sum -c relais_factice_v1.py.sha256
#   read -rs RELAIS_JETON_COURSE; export RELAIS_JETON_COURSE   # jeton de course (32 caractères au moins), pas une clé
#   python3 -I -B /opt/relais/relais_factice_v1.py --hote 10.77.0.1 --port 8790 \
#       --modeles-permis claude-opus-4-7,claude-opus-5-5 --plafond-fictif-usd 2 --cout-fictif-par-appel 0.05 \
#       --journal /var/log/relais-factice/journal-v1.jsonl
echo "B prête : relais à lancer à la main (voir (3))."
