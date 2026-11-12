"""Greffon mitmproxy du mandataire de sortie **transparent** de la machine A, v1 — session-depot, 30 octobre 2026 (R-808).

Montage (voir `architecture-essai-a-blanc-v1.md` § 2) : le serveur de noms du réseau interne renvoie l'adresse du mandataire
pour tout nom, sauf `relais`. Les conteneurs, qui n'ont aucune route, ouvrent donc leurs connexions vers le mandataire.
Celui-ci tourne en mode `reverse` vers une adresse quelconque, et ce greffon remet la vraie destination tirée du nom TLS
annoncé (SNI) ou de l'en-tête `Host`, comme l'exemple `dns_spoofing` de mitmproxy (SUPPOSÉ pour la version installée :
**à éprouver à l'essai à blanc**, épreuve E1). Il applique ensuite `mandataire_regles_v1.decision` et journalise chaque
requête, permise ou refusée : heure, hôte, chemin, méthode, statut, motif. Pas de corps (choix de l'essai ; la course
réelle peut garder les corps si Lazar le décide).

Lancement (dans le conteneur du mandataire) :
    mitmdump --mode reverse:https://exemple.invalid --set keep_host_header=true --set listen_port=443 \
             -s /mandataire/mandataire_addon_v1.py --set journal_mandataire=/journal/mandataire-v1.jsonl
(un second processus pour le port 80, `reverse:http://exemple.invalid`).
"""
import datetime
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mandataire_regles_v1 import decision  # noqa: E402

try:
    from mitmproxy import ctx, http  # type: ignore
except ImportError:  # hors du conteneur du mandataire (essais) : le greffon reste importable
    ctx = http = None


class MandataireV1:
    def load(self, loader):
        loader.add_option("journal_mandataire", str, "/journal/mandataire-v1.jsonl", "journal JSON par ligne")

    def _consigner(self, **champs):
        champs["quand"] = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="milliseconds")
        with open(ctx.options.journal_mandataire, "a", encoding="utf-8") as f:
            f.write(json.dumps(champs, ensure_ascii=False) + "\n")

    def tls_clienthello(self, data):
        # destination réelle tirée du nom TLS annoncé ; sans nom, la connexion est refusée (pas de destination devinée)
        sni = data.client_hello.sni
        if not sni:
            self._consigner(evenement="tls_sans_sni", statut="refus")
            data.context.client.error = "sans nom TLS"
            return
        data.context.server.address = (sni, 443)

    def requestheaders(self, flow):
        hote = flow.request.host_header or flow.request.pretty_host
        flow.request.host = (hote or "").split(":", 1)[0]
        flow.request.port = 443 if flow.request.scheme == "https" else 80
        permis, motif = decision(flow.request.host, flow.request.path)
        if not permis:
            flow.response = http.Response.make(403, f"refusé par le mandataire : {motif}".encode("utf-8"),
                                               {"Content-Type": "text/plain; charset=utf-8"})
        self._consigner(evenement="requete", hote=flow.request.host, chemin=flow.request.path[:300],
                        methode=flow.request.method, statut="permis" if permis else "refus", motif=motif)


addons = [MandataireV1()]
