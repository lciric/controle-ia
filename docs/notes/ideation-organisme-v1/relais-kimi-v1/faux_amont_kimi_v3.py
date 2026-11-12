#!/usr/bin/env python3
"""Faux amont Kimi, version 3 : la v2 (`faux_amont_kimi_v2.py`, inchangée, R12) plus l'aller-retour de la recherche Web
officielle (API Formula), pour éprouver le relais v4 et `commande_kimi_recherche_v1.py`. Boucle locale, sans réseau ni
clé ; imprime « faux amont prêt sur URL » puis sert jusqu'à son arrêt par PID. Lignée session-depot, 30 octobre 2026.

Imite la forme lue dans https://platform.kimi.ai/docs/guide/use-official-tools (30 octobre 2026) :
- `GET /v1/formulas/moonshot/web-search:latest/tools` : `{"object": "list", "tools": [déclaration de web_search]}` ;
- `POST /v1/chat/completions` en flux avec `tools` : tant qu'il reste des tours d'outil (`--tours-outil`) et que
  `tool_choice` n'est pas `none`, rend des `delta.tool_calls` (id et nom au premier morceau, arguments en deux morceaux,
  `finish_reason: "tool_calls"`) ; sinon la réponse finale ;
- `POST /v1/formulas/moonshot/web-search:latest/fibers` : `{"status": "succeeded", "context": {"encrypted_output": …}}`.

Contrôles du faux amont (400 s'ils échouent, pour que les essais voient les erreurs du client) : chaque message
assistant à `tool_calls` est suivi d'exactement un message `tool` par appel (`tool_call_id` aligné) ; le contenu de chaque
message `tool` est la sortie que la fibre a rendue pour les **mêmes** arguments (ou l'aveu du client « Recherche non
exécutée … ») ; un message assistant qui portait du
raisonnement le garde (`reasoning_content`, consigne de K3.1 Pro : renvoyer le message entier) ; une fibre reçoit
exactement `name` et `arguments` (chaîne), `name == "web_search"`.

Options v3 : `--tours-outil T` (1) ; `--appels-par-tour K` (1) ; `--toujours-outil` (ignore `tool_choice: none`, rend
toujours des appels : boucle infinie côté amont) ; `--declaration-variante` (déclaration différente de la documentation) ;
`--fibre-statut-erreur CODE` ; `--fibre-echec` (`status: "failed"`) ; `--usage-tour P,C` (usage de chaque réponse).
`GET /faux/compteurs` rend les nombres d'appels reçus (essais seulement). Options de la v2 gardées.
"""

import argparse
import base64
import json
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

USAGE = {"prompt_tokens": 12, "completion_tokens": 7, "total_tokens": 19}
FORMULE = "moonshot/web-search:latest"
DECLARATION = {"type": "function", "function": {
    "name": "web_search", "description": "Search the web for information",
    "parameters": {"type": "object", "properties": {"query": {"description": "What to search for", "type": "string"}},
                   "required": ["query"]}}}


def sortie_fibre(arguments):
    """Sortie déterministe d'une fibre pour des arguments donnés (chaîne)."""
    return ("----MOONSHOT ENCRYPTED BEGIN----" + base64.b64encode(arguments.encode("utf-8")).decode("ascii")
            + "----MOONSHOT ENCRYPTED END----")


def principal(argv=None):
    a = argparse.ArgumentParser(prog="faux_amont_kimi_v3")
    a.add_argument("--modeles", default="kimi-k3.1-pro,kimi-k2.5")
    a.add_argument("--modele-servi", default=None)
    a.add_argument("--modele-change-en-cours", action="store_true")
    a.add_argument("--sans-usage", action="store_true")
    a.add_argument("--usage-dans-le-choix", action="store_true")
    a.add_argument("--couper-apres", type=int, default=None)
    a.add_argument("--pause-entre-morceaux", type=float, default=0.0)
    a.add_argument("--morceaux-raisonnement", type=int, default=0)
    a.add_argument("--statut-erreur", type=int, default=None)
    a.add_argument("--tours-outil", type=int, default=1)
    a.add_argument("--appels-par-tour", type=int, default=1)
    a.add_argument("--toujours-outil", action="store_true")
    a.add_argument("--declaration-variante", action="store_true")
    a.add_argument("--fibre-statut-erreur", type=int, default=None)
    a.add_argument("--fibre-echec", action="store_true")
    a.add_argument("--usage-tour", default=None, help="P,C : prompt_tokens et completion_tokens de chaque réponse")
    args = a.parse_args(argv)
    modeles = [m.strip() for m in args.modeles.split(",") if m.strip()]
    usage = dict(USAGE)
    if args.usage_tour:
        p, c = (int(x) for x in args.usage_tour.split(","))
        usage = {"prompt_tokens": p, "completion_tokens": c, "total_tokens": p + c}
    declaration = json.loads(json.dumps(DECLARATION))
    if args.declaration_variante:
        declaration["function"]["description"] = "Search the internet (variante de l'amont)"
    compteurs = {"chat": 0, "fibres": 0, "declarations": 0, "appels_outil_rendus": 0}
    verrou = threading.Lock()
    numero = [0]

    def controler_messages(messages):
        """Motif d'erreur (chaîne) si l'aller-retour des outils est mal formé, sinon None ; et le nombre de tours faits."""
        tours = 0
        i = 0
        while i < len(messages):
            m = messages[i]
            if isinstance(m, dict) and m.get("role") == "assistant" and m.get("tool_calls"):
                tours += 1
                appels = m["tool_calls"]
                ids = [c.get("id") for c in appels]
                suite = messages[i + 1:i + 1 + len(appels)]
                if len(suite) != len(appels) or any(s.get("role") != "tool" for s in suite):
                    return "tool_calls sans autant de messages tool", tours
                if sorted(s.get("tool_call_id") for s in suite) != sorted(ids):
                    return "tool_call_id non alignés", tours
                par_id = {c["id"]: c["function"]["arguments"] for c in appels}
                for s in suite:
                    contenu = s.get("content")
                    if contenu != sortie_fibre(par_id[s["tool_call_id"]]) and not (
                            isinstance(contenu, str) and contenu.startswith("Recherche non exécutée")):
                        return "contenu tool différent de la sortie de la fibre", tours
                if args.morceaux_raisonnement and not m.get("reasoning_content"):
                    return "reasoning_content absent du message assistant renvoyé", tours
                i += 1 + len(appels)
                continue
            if isinstance(m, dict) and m.get("role") == "tool":
                return "message tool orphelin", tours
            i += 1
        return None, tours

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
            if self.path == "/faux/compteurs":
                with verrou:
                    return self._json(200, dict(compteurs))
            if self.path == f"/v1/formulas/{FORMULE}/tools":
                with verrou:
                    compteurs["declarations"] += 1
                return self._json(200, {"object": "list", "tools": [declaration]})
            if self.path != "/v1/models":
                return self._json(404, {"error": "chemin inconnu"})
            return self._json(200, {"object": "list", "data": [{"id": m, "object": "model"} for m in modeles]})

        def _fibre(self, corps):
            with verrou:
                compteurs["fibres"] += 1
            if args.fibre_statut_erreur:
                return self._json(args.fibre_statut_erreur, {"error": {"message": "erreur de fibre simulée"}})
            if not (isinstance(corps, dict) and set(corps) == {"name", "arguments"} and corps["name"] == "web_search"
                    and isinstance(corps["arguments"], str)):
                return self._json(400, {"error": {"message": "fibre mal formée"}})
            if args.fibre_echec:
                return self._json(200, {"id": "fiber-echec", "object": "fiber", "status": "failed",
                                        "error": "échec simulé"})
            return self._json(200, {"id": "fiber-a-blanc", "object": "fiber", "status": "succeeded",
                                    "context": {"input": json.dumps(corps),
                                                "encrypted_output": sortie_fibre(corps["arguments"])},
                                    "formula": FORMULE})

        def do_POST(self):
            corps = json.loads(self.rfile.read(int(self.headers.get("Content-Length") or 0)) or b"{}")
            if self.path == f"/v1/formulas/{FORMULE}/fibers":
                return self._fibre(corps)
            if self.path != "/v1/chat/completions":
                return self._json(404, {"error": "chemin inconnu"})
            with verrou:
                compteurs["chat"] += 1
            if args.statut_erreur:
                return self._json(args.statut_erreur, {"error": {"message": "erreur simulée"}})
            motif, tours_faits = controler_messages(corps.get("messages") or [])
            if motif:
                return self._json(400, {"error": {"message": motif, "type": "invalid_request_error"}})
            servi = args.modele_servi or corps.get("model")
            avec_outil = bool(corps.get("tools")) and (
                args.toujours_outil or (corps.get("tool_choice") != "none" and tours_faits < args.tours_outil))
            if not corps.get("stream"):
                return self._json(200, {"id": "chatcmpl-a-blanc", "object": "chat.completion", "model": servi,
                                        "choices": [{"index": 0, "message": {"role": "assistant", "content": "OK"},
                                                     "finish_reason": "stop"}], "usage": usage})
            morceaux = []
            for i in range(args.morceaux_raisonnement):
                morceaux.append({"choices": [{"index": 0, "delta": {"reasoning_content": f"pensée {i}. "}}]})
            if avec_outil:
                for k in range(args.appels_par_tour):
                    with verrou:
                        numero[0] += 1
                        n = numero[0]
                        compteurs["appels_outil_rendus"] += 1
                    arguments = json.dumps({"query": f"requête {n}"}, ensure_ascii=False)
                    moitie = len(arguments) // 2
                    morceaux.append({"choices": [{"index": 0, "delta": {"tool_calls": [
                        {"index": k, "id": f"web_search:{n}", "type": "function",
                         "function": {"name": "web_search", "arguments": arguments[:moitie]}}]}}]})
                    morceaux.append({"choices": [{"index": 0, "delta": {"tool_calls": [
                        {"index": k, "function": {"arguments": arguments[moitie:]}}]}}]})
                dernier = {"choices": [{"index": 0, "delta": {}, "finish_reason": "tool_calls"}]}
            else:
                for mot in ("Bonjour ", "le ", "monde."):
                    morceaux.append({"choices": [{"index": 0, "delta": {"content": mot}}]})
                dernier = {"choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}]}
            if not args.sans_usage:
                if args.usage_dans_le_choix:
                    dernier["choices"][0]["usage"] = usage
                else:
                    dernier["usage"] = usage
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
                self.wfile.write(b"data: " + json.dumps(m, ensure_ascii=False).encode("utf-8") + b"\n\n")
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
