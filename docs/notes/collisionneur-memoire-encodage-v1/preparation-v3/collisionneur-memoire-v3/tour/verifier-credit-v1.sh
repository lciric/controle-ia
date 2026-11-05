#!/usr/bin/env bash
# Le compte Anthropic de cette session a-t-il du crédit ? Un appel de 16 jetons au plus (rien n'est facturé si l'appel est
# refusé) ; message d'erreur seul, tronqué, clés masquées. Code 0 : crédit ; 1 : pas de crédit ou échec.
set -uo pipefail; set +x
cd "$(dirname "$0")"
r=$(env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" \
  NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY" ANTHROPIC_WORKSPACE_ID="$RR_ANTHROPIC_WORKSPACE_ID" \
  timeout 120 ../venv/bin/python -I -B diag_anthropic_v1.py 2>&1 | sed -E 's/(sk-ant|AIza)[A-Za-z0-9_-]+/[clé masquée]/g' | head -3)
echo "$(date -u +%FT%TZ) $(echo "$r" | tr '\n' ' ' | cut -c1-240)"
echo "$r" | grep -q '^échec : $' && exit 0
exit 1
