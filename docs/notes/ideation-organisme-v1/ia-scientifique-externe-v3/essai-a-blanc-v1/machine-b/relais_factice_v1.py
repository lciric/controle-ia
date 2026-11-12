#!/usr/bin/env python3
"""Relais factice de l'essai à blanc de l'Agentic Scientist v3 (machine B), v1 — session-depot, 30 octobre 2026 (R-808).

Il imite l'interface des messages d'Anthropic, **n'appelle jamais Anthropic** et ne porte **aucune clé** : il sert à
éprouver la plomberie (tous les appels de modèle passent par B ; le plafond tient ; aucun contournement), pas la science.

- Points d'entrée acceptés : `POST /v1/messages` (réponse entière ou en flux d'événements), `POST
  /v1/messages/count_tokens`, `GET /relais/etat`. Tout autre chemin : 404.
- Authentification : jeton de course dans `Authorization: Bearer …` (voie `ANTHROPIC_AUTH_TOKEN` de Claude Code) ou
  `x-api-key`. Le jeton attendu est lu dans la variable `RELAIS_JETON_COURSE` au démarrage, puis la variable est retirée de
  l'environnement du processus ; seule son empreinte reste en mémoire. Comparaison à temps constant.
- Modèles : liste fermée (`--modeles-permis`) ; tout autre modèle : 403 et compté comme contournement.
- Plafond : chaque appel coûte un prix **fictif** fixe (`--cout-fictif-par-appel`) ; au-delà de `--plafond-fictif-usd`,
  402. Le plafond est éprouvé, pas la facture.
- Journal JSON par ligne : heure, chemin, modèle, statut, coût fictif, cumul ; **jamais** le jeton ni le corps des messages.

Usage (sur B, en root ou non) :
    RELAIS_JETON_COURSE=… python3 -I -B relais_factice_v1.py --hote 10.77.0.1 --port 8790 \
        --modeles-permis claude-opus-4-7,claude-opus-5-5 --plafond-fictif-usd 2 --cout-fictif-par-appel 0.05 \
        --journal /var/log/relais-factice/journal-v1.jsonl
"""
import argparse
import datetime
import hashlib
import hmac
import json
import os
import sys
import threading
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

VERSION = "relais-factice-v1"
TEXTE_FACTICE = "Réponse factice de l'essai à blanc : aucun modèle n'a été appelé."
TAILLE_MAX_CORPS = 8_000_000


class Compteur:
    """Plafond fictif : réservation sous verrou, pour que des appels simultanés ne le franchissent pas ensemble."""

    def __init__(self, plafond, cout):
        self.plafond, self.cout, self.depense, self.appels, self.refus = float(plafond), float(cout), 0.0, 0, {}
        self.verrou = threading.Lock()

    def reserver(self):
        with self.verrou:
            if self.depense + self.cout > self.plafond + 1e-12:
                return False
            self.depense += self.cout
            self.appels += 1
            return True

    def refuser(self, motif):
        with self.verrou:
            self.refus[motif] = self.refus.get(motif, 0) + 1

    def etat(self):
        with self.verrou:
            return {"version": VERSION, "plafond_fictif_usd": self.plafond, "cout_fictif_par_appel_usd": self.cout,
                    "depense_fictive_usd": round(self.depense, 6), "appels": self.appels, "refus": dict(self.refus),
                    "amont": "aucun (factice)"}


def reponse_message(modele, flux):
    ident = "msg_factice_" + uuid.uuid4().hex[:24]
    usage = {"input_tokens": 1, "output_tokens": 1}
    if not flux:
        return {"id": ident, "type": "message", "role": "assistant", "model": modele,
                "content": [{"type": "text", "text": TEXTE_FACTICE}], "stop_reason": "end_turn",
                "stop_sequence": None, "usage": usage}
    evenements = [
        ("message_start", {"type": "message_start", "message": {
            "id": ident, "type": "message", "role": "assistant", "model": modele, "content": [],
            "stop_reason": None, "stop_sequence": None, "usage": {"input_tokens": 1, "output_tokens": 0}}}),
        ("content_block_start", {"type": "content_block_start", "index": 0,
                                 "content_block": {"type": "text", "text": ""}}),
        ("content_block_delta", {"type": "content_block_delta", "index": 0,
                                 "delta": {"type": "text_delta", "text": TEXTE_FACTICE}}),
        ("content_block_stop", {"type": "content_block_stop", "index": 0}),
        ("message_delta", {"type": "message_delta", "delta": {"stop_reason": "end_turn", "stop_sequence": None},
                           "usage": {"output_tokens": 1}}),
        ("message_stop", {"type": "message_stop"}),
    ]
    return "".join(f"event: {nom}\ndata: {json.dumps(d, ensure_ascii=False)}\n\n" for nom, d in evenements)


def fabrique(empreinte_jeton, modeles, compteur, journal):
    verrou_journal = threading.Lock()

    def consigner(**champs):
        champs["quand"] = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="milliseconds")
        ligne = json.dumps(champs, ensure_ascii=False)
        with verrou_journal, open(journal, "a", encoding="utf-8") as f:
            f.write(ligne + "\n")

    class Gestionnaire(BaseHTTPRequestHandler):
        server_version = VERSION
        sys_version = ""

        def log_message(self, *args):  # pas de journal sur la sortie standard
            pass

        def _json(self, code, corps):
            donnees = json.dumps(corps, ensure_ascii=False).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(donnees)))
            self.end_headers()
            self.wfile.write(donnees)

        def _jeton_valide(self):
            presente = ""
            auth = self.headers.get("Authorization", "")
            if auth.startswith("Bearer "):
                presente = auth[len("Bearer "):].strip()
            elif self.headers.get("x-api-key"):
                presente = self.headers.get("x-api-key", "").strip()
            if not presente:
                return False
            return hmac.compare_digest(hashlib.sha256(presente.encode()).hexdigest(), empreinte_jeton)

        def do_GET(self):
            if self.path == "/relais/etat":
                return self._json(200, compteur.etat())
            compteur.refuser("chemin")
            consigner(chemin=self.path, methode="GET", statut=404)
            return self._json(404, {"erreur": "chemin refusé"})

        def do_POST(self):
            chemin = self.path.split("?", 1)[0]
            if chemin not in ("/v1/messages", "/v1/messages/count_tokens"):
                compteur.refuser("chemin")
                consigner(chemin=chemin, methode="POST", statut=404)
                return self._json(404, {"erreur": "chemin refusé"})
            if not self._jeton_valide():
                compteur.refuser("jeton")
                consigner(chemin=chemin, methode="POST", statut=401)
                return self._json(401, {"type": "error", "error": {"type": "authentication_error",
                                                                    "message": "jeton de course refusé"}})
            taille = int(self.headers.get("Content-Length") or 0)
            if taille <= 0 or taille > TAILLE_MAX_CORPS:
                compteur.refuser("taille")
                consigner(chemin=chemin, methode="POST", statut=413, octets=taille)
                return self._json(413, {"erreur": "corps absent ou trop grand"})
            try:
                corps = json.loads(self.rfile.read(taille))
            except (ValueError, UnicodeDecodeError):
                compteur.refuser("json")
                consigner(chemin=chemin, methode="POST", statut=400)
                return self._json(400, {"erreur": "corps illisible"})
            modele = str(corps.get("model", ""))
            if modele not in modeles:
                compteur.refuser("modele")
                consigner(chemin=chemin, methode="POST", statut=403, modele=modele)
                return self._json(403, {"type": "error", "error": {"type": "permission_error",
                                                                    "message": f"modèle non permis : {modele}"}})
            if chemin.endswith("/count_tokens"):
                consigner(chemin=chemin, methode="POST", statut=200, modele=modele, cout_fictif_usd=0.0)
                return self._json(200, {"input_tokens": 1})
            if not compteur.reserver():
                compteur.refuser("plafond")
                consigner(chemin=chemin, methode="POST", statut=402, modele=modele, **compteur.etat())
                return self._json(402, {"type": "error", "error": {"type": "billing_error",
                                                                    "message": "plafond du relais atteint"}})
            flux = bool(corps.get("stream"))
            etat = compteur.etat()
            consigner(chemin=chemin, methode="POST", statut=200, modele=modele, flux=flux,
                      cout_fictif_usd=compteur.cout, depense_fictive_usd=etat["depense_fictive_usd"])
            reponse = reponse_message(modele, flux)
            if not flux:
                return self._json(200, reponse)
            donnees = reponse.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.send_header("Content-Length", str(len(donnees)))
            self.end_headers()
            self.wfile.write(donnees)
            return None

    return Gestionnaire


def principal(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--hote", required=True, help="adresse d'écoute (celle du tunnel seulement, jamais 0.0.0.0)")
    p.add_argument("--port", type=int, default=8790)
    p.add_argument("--modeles-permis", required=True)
    p.add_argument("--plafond-fictif-usd", type=float, required=True)
    p.add_argument("--cout-fictif-par-appel", type=float, default=0.05)
    p.add_argument("--journal", required=True)
    a = p.parse_args(argv)
    if a.hote in ("0.0.0.0", "::", ""):
        sys.exit("refus : le relais n'écoute jamais sur toutes les adresses")
    jeton = os.environ.pop("RELAIS_JETON_COURSE", "")
    if len(jeton) < 32:
        sys.exit("refus : RELAIS_JETON_COURSE absent ou trop court (32 caractères au moins)")
    empreinte = hashlib.sha256(jeton.encode()).hexdigest()
    del jeton
    modeles = frozenset(m.strip() for m in a.modeles_permis.split(",") if m.strip())
    compteur = Compteur(a.plafond_fictif_usd, a.cout_fictif_par_appel)
    serveur = ThreadingHTTPServer((a.hote, a.port), fabrique(empreinte, modeles, compteur, a.journal))
    print(f"{VERSION} : écoute {a.hote}:{a.port}, modèles {sorted(modeles)}, plafond fictif {a.plafond_fictif_usd}",
          file=sys.stderr)
    serveur.serve_forever()


if __name__ == "__main__":
    principal()
