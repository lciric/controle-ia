#!/usr/bin/env python3
"""Faux amont Kimi pour la variante à blanc de `essai_kimi_v1.sh` : sert `GET /v1/models` et
`POST /v1/chat/completions` sur la boucle locale, sans réseau ni clé ; imprime « faux amont prêt sur URL » puis sert
jusqu'à son arrêt par PID. La réponse porte le modèle demandé (ou `--modele-servi` s'il est donné, pour éprouver la
barrière du modèle servi) et un `usage` fixe. Lignée session-depot, 30 octobre 2026.
"""

import argparse
import json
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


def principal(argv=None):
    a = argparse.ArgumentParser(prog="faux_amont_kimi_v1")
    a.add_argument("--modeles", default="kimi-k3.1-pro,kimi-k2.5", help="identifiants rendus par GET /v1/models")
    a.add_argument("--modele-servi", default=None, help="modèle rendu dans les réponses (défaut : le modèle demandé)")
    args = a.parse_args(argv)
    modeles = [m.strip() for m in args.modeles.split(",") if m.strip()]

    class Gestion(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def log_message(self, *a):
            pass

        def _json(self, code, objet):
            brut = json.dumps(objet).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(brut)))
            self.end_headers()
            self.wfile.write(brut)

        def do_GET(self):
            if self.path != "/v1/models":
                return self._json(404, {"error": "chemin inconnu"})
            return self._json(200, {"object": "list", "data": [{"id": m, "object": "model"} for m in modeles]})

        def do_POST(self):
            corps = json.loads(self.rfile.read(int(self.headers.get("Content-Length") or 0)) or b"{}")
            if self.path != "/v1/chat/completions":
                return self._json(404, {"error": "chemin inconnu"})
            servi = args.modele_servi or corps.get("model")
            return self._json(200, {"id": "chatcmpl-a-blanc", "object": "chat.completion", "model": servi,
                                    "choices": [{"index": 0, "message": {"role": "assistant", "content": "OK"},
                                                 "finish_reason": "stop"}],
                                    "usage": {"prompt_tokens": 12, "completion_tokens": 2, "total_tokens": 14}})

    serveur = ThreadingHTTPServer(("127.0.0.1", 0), Gestion)
    print(f"faux amont prêt sur http://127.0.0.1:{serveur.server_address[1]}", flush=True)
    try:
        serveur.serve_forever()
    except KeyboardInterrupt:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(principal())
