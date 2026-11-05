#!/usr/bin/env python3
"""Faux amont Kimi, version 2 : la v1 (`faux_amont_kimi_v1.py`, inchangée) plus le flux SSE quand la requête porte
`stream: true`, pour éprouver le relais v3. Boucle locale, sans réseau ni clé ; imprime « faux amont prêt sur URL » puis
sert jusqu'à son arrêt par PID. Lignée session-depot, 30 octobre 2026.

Options d'essai (flux) : `--modele-servi X` ; `--modele-change-en-cours` (le 2e morceau porte un autre modèle) ;
`--sans-usage` ; `--usage-dans-le-choix` (variante où l'usage est dans le choix du dernier morceau) ; `--couper-apres N`
(ferme la connexion après N morceaux, sans [DONE]) ; `--pause-entre-morceaux S` ; `--morceaux-raisonnement K` (K deltas
`reasoning_content` d'abord) ; `--statut-erreur CODE` (rend une erreur JSON sans flux).
"""

import argparse
import json
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

USAGE = {"prompt_tokens": 12, "completion_tokens": 7, "total_tokens": 19}


def principal(argv=None):
    a = argparse.ArgumentParser(prog="faux_amont_kimi_v2")
    a.add_argument("--modeles", default="kimi-k3.1-pro,kimi-k2.5")
    a.add_argument("--modele-servi", default=None)
    a.add_argument("--modele-change-en-cours", action="store_true")
    a.add_argument("--sans-usage", action="store_true")
    a.add_argument("--usage-dans-le-choix", action="store_true")
    a.add_argument("--couper-apres", type=int, default=None)
    a.add_argument("--pause-entre-morceaux", type=float, default=0.0)
    a.add_argument("--morceaux-raisonnement", type=int, default=0)
    a.add_argument("--statut-erreur", type=int, default=None)
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
            if args.statut_erreur:
                return self._json(args.statut_erreur, {"error": {"message": "erreur simulée"}})
            servi = args.modele_servi or corps.get("model")
            if not corps.get("stream"):
                return self._json(200, {"id": "chatcmpl-a-blanc", "object": "chat.completion", "model": servi,
                                        "choices": [{"index": 0, "message": {"role": "assistant", "content": "OK"},
                                                     "finish_reason": "stop"}], "usage": USAGE})
            morceaux = []
            for i in range(args.morceaux_raisonnement):
                morceaux.append({"choices": [{"index": 0, "delta": {"reasoning_content": f"pensée {i}. "}}]})
            for mot in ("Bonjour ", "le ", "monde."):
                morceaux.append({"choices": [{"index": 0, "delta": {"content": mot}}]})
            dernier = {"choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}]}
            if not args.sans_usage:
                if args.usage_dans_le_choix:
                    dernier["choices"][0]["usage"] = USAGE
                else:
                    dernier["usage"] = USAGE
            morceaux.append(dernier)
            for n, m in enumerate(morceaux):
                m.update(id="chatcmpl-flux", object="chat.completion.chunk",
                         model=("autre-modele" if args.modele_change_en_cours and n == 1 else servi))
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.send_header("Connection", "close")
            self.end_headers()
            for n, m in enumerate(morceaux):
                if args.couper_apres is not None and n >= args.couper_apres:
                    self.close_connection = True
                    return
                if args.pause_entre_morceaux and n:
                    time.sleep(args.pause_entre_morceaux)
                self.wfile.write(b"data: " + json.dumps(m).encode("utf-8") + b"\n\n")
                self.wfile.flush()
            self.wfile.write(b"data: [DONE]\n\n")
            self.wfile.flush()
            self.close_connection = True

    serveur = ThreadingHTTPServer(("127.0.0.1", 0), Gestion)
    print(f"faux amont prêt sur http://127.0.0.1:{serveur.server_address[1]}", flush=True)
    try:
        serveur.serve_forever()
    except KeyboardInterrupt:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(principal())
