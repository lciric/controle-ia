#!/usr/bin/env python3
"""Relais Gemini local, version 1 : la commande d'Argon n'a plus **aucune clé** (ni fichier, ni variable réelle).

Lignée session-depot, 29 octobre 2026. Même modèle que le relais Claude du pôle (`orchestrateur-v45/pole/relais_reel.py`) :
un petit serveur HTTP dans **son propre processus**, sur la boucle locale seulement, lancé par le noyau sous `env -i` avec la
vraie clé dans **son seul environnement** (variable `--variable-cle`, `GEMINI_API_KEY` par défaut) ; la clé est lue au
démarrage, effacée de `os.environ`, gardée en mémoire, jamais journalisée ni affichée. La commande `commande_argon_v2.py`
(inchangée, R12) reçoit de l'enveloppe v3 `--url-base http://127.0.0.1:8788/v1beta` et une clé **factice**
(`GEMINI_API_KEY=factice-relais`) qu'elle pose dans l'en-tête `x-goog-api-key` ; le relais **retire** toute clé reçue du client
(en-tête `x-goog-api-key`, en-tête `Authorization`, paramètre `?key=`) et pose la vraie, puis transmet à l'amont
(`https://generativelanguage.googleapis.com`) par le mandataire `HTTPS_PROXY` et les certificats `SSL_CERT_FILE` de son
environnement. Corps relayé tel quel ; réponse relayée telle quelle (code, corps, type de contenu).

Ce que le relais refuse **sans rien envoyer** :
- tout chemin autre que `POST /v1beta/models/<modèle>:generateContent` et `POST /v1beta/models/<modèle>:countTokens`, et
  tout modèle hors de la liste blanche (`--modele`, répétable, défaut `gemini-4-argon`) : 403 ;
- au-delà de `--max-appels` (défaut 64) appels relayés, ou un corps de plus de `--max-octets-corps` (défaut 8 000 000) octets :
  429 ;
- une requête sans `Content-Length` : 411 ; une méthode autre que GET (`/relais/etat` seulement) et POST : 403.

Journal (`--journal`, JSON par ligne) par appel : heure UTC, méthode, chemin (sans paramètre de clé), modèle, taille du
corps, code amont, `usageMetadata` (ou `totalTokens` pour `countTokens`) si présent, durée — **jamais le texte, jamais la
clé**. Route `GET /relais/etat` : appels, refus, octets, bornes, liste blanche, et la preuve que la variable de clé n'est plus
dans l'environnement du processus.

Limite connue (reprise de `relais_reel.py`, contre-lecture F-C7) : effacer la variable de `os.environ` n'efface pas le bloc
initial que `/proc/<pid>/environ` expose ; tout processus du même utilisateur (ou root) peut l'y lire tant que le relais vit.
L'utilisateur distinct `argon`, qui exécute la commande, n'est pas cet utilisateur : c'est tout l'objet du montage.

Ce fichier n'est jamais exécuté avec une vraie clé dans ce dépôt : ses essais (`test_relais_gemini_v1.py`) le lancent avec une
clé factice devant un faux amont local. Aucune dépendance hors bibliothèque standard.

Lancement (noyau, clé par variable sous `env -i`, jamais en argument ni en fichier) :

    setsid nohup env -i PATH=/usr/bin:/bin LANG=C.UTF-8 GEMINI_API_KEY="$CLE" HTTPS_PROXY=http://127.0.0.1:40191 \\
        SSL_CERT_FILE=/root/.ccr/ca-bundle.crt python3 -I -B relais_gemini_v1.py --port 8788 --max-appels 64 \\
        --journal $DOS/relais-gemini-journal-v1.jsonl > $DOS/relais-gemini-v1.log 2>&1 & echo $! > $DOS/relais-gemini.pid
"""

import argparse
import datetime
import http.client
import json
import os
import re
import ssl
import sys
import threading
import time
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

VERSION = "relais-gemini-v1"
HOTE = "127.0.0.1"  # jamais une autre interface : aucune option ne le change
PORT_DEFAUT = 8788
AMONT_DEFAUT = "https://generativelanguage.googleapis.com"
VARIABLE_CLE_DEFAUT = "GEMINI_API_KEY"
MODELES_DEFAUT = ("gemini-4-argon",)
MAX_APPELS_DEFAUT = 64
MAX_OCTETS_CORPS_DEFAUT = 8_000_000
TAILLE_MAX_REPONSE = 50_000_000  # au-delà : 502 (la commande refuse elle-même au-delà de cette taille)
DELAI_AMONT_DEFAUT_S = 1800.0    # ≥ délai de la commande (1 500 s) : c'est elle qui coupe en premier
HOTES_LOCAUX = {"127.0.0.1", "localhost", "::1"}
ACTIONS_PERMISES = ("generateContent", "countTokens")
MOTIF_CHEMIN = re.compile(r"^/v1beta/models/([A-Za-z0-9._-]+):(generateContent|countTokens)$")
EN_TETES_DE_CLE = {"x-goog-api-key", "authorization", "proxy-authorization"}
EN_TETES_NON_RELAYES = EN_TETES_DE_CLE | {"host", "connection", "content-length", "transfer-encoding", "keep-alive", "te",
                                          "trailer", "upgrade", "accept-encoding", "expect"}
PARAMETRES_DE_CLE = {"key", "access_token"}


class RelaisInvalide(Exception):
    """Réglage impossible : le relais ne démarre pas."""


def masquer(texte, cle):
    """Ne laisse jamais passer la clé dans un message, un journal ou une réponse."""
    texte = str(texte)
    return texte.replace(cle, "[clé]") if cle else texte


def lire_cle(environnement, variable):
    """Lit la clé dans l'environnement donné et l'en efface ; ne la rend qu'à l'appelant (jamais journalisée)."""
    cle = (environnement.get(variable) or "").strip()
    if not cle:
        raise RelaisInvalide(f"aucune clé dans la variable {variable} de l'environnement du relais")
    environnement.pop(variable, None)
    return cle


def valider_amont(amont):
    """`https://` vers n'importe quel hôte, ou `http://` vers la boucle locale seulement (essais)."""
    p = urllib.parse.urlsplit(amont)
    if p.scheme == "https" and p.hostname:
        return p
    if p.scheme == "http" and p.hostname in HOTES_LOCAUX:
        return p
    raise RelaisInvalide(f"--amont : https, ou http vers la boucle locale seulement (reçu {amont!r})")


def mandataire_de(environnement):
    """Mandataire HTTPS de l'environnement (`HTTPS_PROXY`, puis `https_proxy`) : (hôte, port, en-têtes du tunnel) ou None."""
    brut = environnement.get("HTTPS_PROXY") or environnement.get("https_proxy")
    if not brut:
        return None
    p = urllib.parse.urlsplit(brut if "://" in brut else "http://" + brut)
    if p.scheme != "http" or not p.hostname or not p.port:
        raise RelaisInvalide("HTTPS_PROXY : http://hôte:port attendu")
    en_tetes = {}
    if p.username is not None:
        import base64
        jeton = base64.b64encode(f"{urllib.parse.unquote(p.username)}:{urllib.parse.unquote(p.password or '')}"
                                 .encode("utf-8")).decode("ascii")
        en_tetes["Proxy-Authorization"] = "Basic " + jeton
    return p.hostname, p.port, en_tetes


def chemin_sans_cle(chemin):
    """Rend (chemin nettoyé, modèle, action) ; (None, None, None) si le chemin n'est pas permis. Retire tout paramètre de
    clé de la chaîne de requête ; garde les autres paramètres tels quels."""
    p = urllib.parse.urlsplit(chemin)
    m = MOTIF_CHEMIN.match(p.path)
    if not m:
        return None, None, None
    parametres = [(k, v) for k, v in urllib.parse.parse_qsl(p.query, keep_blank_values=True)
                  if k.lower() not in PARAMETRES_DE_CLE]
    propre = p.path + ("?" + urllib.parse.urlencode(parametres) if parametres else "")
    return propre, m.group(1), m.group(2)


def usage_d_une_reponse(corps):
    """Ce que le journal garde d'une réponse : `usageMetadata`, `totalTokens`, `modelVersion` s'ils sont présents, et c'est
    tout — jamais les candidats, jamais le texte."""
    try:
        objet = json.loads(corps.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        return {}
    if not isinstance(objet, dict):
        return {}
    garde = {}
    if isinstance(objet.get("usageMetadata"), dict):
        garde["usageMetadata"] = {k: v for k, v in objet["usageMetadata"].items() if isinstance(v, (int, float))}
    if isinstance(objet.get("totalTokens"), int):
        garde["totalTokens"] = objet["totalTokens"]
    if isinstance(objet.get("modelVersion"), str):
        garde["modele_servi"] = objet["modelVersion"][:80]
    if isinstance(objet.get("error"), dict) and isinstance(objet["error"].get("status"), str):
        garde["statut_erreur_amont"] = objet["error"]["status"][:40]
    return garde


class Compteur:
    """Bornes du relais : nombre d'appels relayés et taille du corps par appel. Un appel est **compté avant de partir**
    (sous verrou) : des appels simultanés ne peuvent pas franchir la borne ensemble."""

    def __init__(self, max_appels, max_octets_corps):
        self.max_appels, self.max_octets_corps = int(max_appels), int(max_octets_corps)
        self.appels, self.refus, self.octets_envoyes, self.octets_recus = 0, 0, 0, 0
        self.par_statut = {}
        self._verrou = threading.Lock()

    def admettre(self, longueur_corps):
        """Admet (compte) un appel ou rend le motif du refus."""
        with self._verrou:
            if longueur_corps > self.max_octets_corps:
                self.refus += 1
                return f"corps de {longueur_corps} octets au-dessus de --max-octets-corps ({self.max_octets_corps})"
            if self.appels >= self.max_appels:
                self.refus += 1
                return f"--max-appels ({self.max_appels}) atteint"
            self.appels += 1
            self.octets_envoyes += longueur_corps
            return None

    def refuser(self):
        with self._verrou:
            self.refus += 1

    def conclure(self, statut, octets_recus):
        with self._verrou:
            self.octets_recus += octets_recus
            self.par_statut[str(statut)] = self.par_statut.get(str(statut), 0) + 1

    def etat(self):
        with self._verrou:
            return {"appels": self.appels, "refus": self.refus, "octets_envoyes": self.octets_envoyes,
                    "octets_recus": self.octets_recus, "max_appels": self.max_appels,
                    "max_octets_corps": self.max_octets_corps, "appels_restants": max(0, self.max_appels - self.appels),
                    "reponses_par_statut": dict(self.par_statut)}


def fabriquer_gestionnaire(cle, amont, modeles, compteur, journal, verrou_journal, mandataire, contexte_tls, delai_amont_s,
                           variable_cle):
    parties = valider_amont(amont)
    modeles = frozenset(modeles)
    etat_fixe = {"version": VERSION, "amont": amont, "modeles": sorted(modeles), "mandataire": bool(mandataire),
                 "variable_cle_encore_presente": None}

    def ecrire_journal(entree):
        if journal is None:
            return
        ligne = json.dumps(entree, ensure_ascii=False, sort_keys=True)
        assert cle not in ligne, "la clé ne s'écrit jamais"  # garde-fou ; le texte est exclu par construction
        with verrou_journal:
            with open(journal, "a", encoding="utf-8") as f:
                f.write(ligne + "\n")

    def maintenant():
        return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="milliseconds")

    class Gestionnaire(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"
        server_version = "RelaisGemini/1"
        sys_version = ""

        def log_message(self, format, *args):  # noqa: A002 — signature imposée par la bibliothèque standard
            pass  # aucun journal implicite : il porterait les chemins (donc un éventuel ?key=) sur un terminal partagé

        def _repondre_json(self, statut, objet):
            corps = json.dumps(objet, ensure_ascii=False).encode("utf-8")
            self.send_response(statut)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(corps)))
            self.send_header("Connection", "close")
            self.end_headers()
            self.wfile.write(corps)
            self.close_connection = True

        def _refuser(self, statut, motif, methode, chemin_propre, modele=None):
            compteur.refuser()
            ecrire_journal({"quand_utc": maintenant(), "methode": methode, "chemin": chemin_propre, "modele": modele,
                            "statut": statut, "motif": motif})
            return self._repondre_json(statut, {"erreur": motif, "relais": VERSION})

        def do_GET(self):
            if urllib.parse.urlsplit(self.path).path == "/relais/etat":
                etat = dict(etat_fixe, variable_cle_encore_presente=variable_cle in os.environ, **compteur.etat())
                return self._repondre_json(200, etat)
            return self._refuser(403, "chemin non relayé", "GET", chemin_sans_cle(self.path)[0] or "[chemin refusé]")

        def do_POST(self):
            return self._relayer()

        def _autre_methode(self):
            return self._refuser(403, f"méthode {self.command} non relayée", self.command, "[chemin refusé]")

        do_PUT = do_DELETE = do_PATCH = do_HEAD = do_OPTIONS = _autre_methode

        def _relayer(self):
            debut = time.time()
            chemin_propre, modele, action = chemin_sans_cle(self.path)
            if chemin_propre is None:
                return self._refuser(403, "chemin non relayé (generateContent et countTokens de /v1beta/models seulement)",
                                     "POST", "[chemin refusé]")
            if modele not in modeles:
                return self._refuser(403, "modèle hors de la liste blanche du relais", "POST", chemin_propre, modele)
            if "content-length" not in self.headers or self.headers.get("transfer-encoding"):
                return self._refuser(411, "Content-Length requis (aucun corps en morceaux)", "POST", chemin_propre, modele)
            try:
                longueur = int(self.headers["content-length"])
                if longueur < 0:
                    raise ValueError
            except ValueError:
                return self._refuser(411, "Content-Length invalide", "POST", chemin_propre, modele)
            motif = compteur.admettre(longueur)
            if motif:
                ecrire_journal({"quand_utc": maintenant(), "methode": "POST", "chemin": chemin_propre, "modele": modele,
                                "octets_corps": longueur, "statut": 429, "motif": motif})
                return self._repondre_json(429, {"erreur": motif, "relais": VERSION, **compteur.etat()})
            corps = self.rfile.read(longueur) if longueur else b""
            en_tetes = {k: v for k, v in self.headers.items() if k.lower() not in EN_TETES_NON_RELAYES}
            en_tetes["x-goog-api-key"] = cle
            en_tetes["Accept-Encoding"] = "identity"
            en_tetes["Host"] = parties.netloc
            en_tetes["Content-Length"] = str(len(corps))
            en_tetes["Connection"] = "close"
            statut, octets_recus, garde = None, 0, {}
            try:
                if parties.scheme == "https":
                    if mandataire:
                        hote_m, port_m, en_tetes_tunnel = mandataire
                        connexion = http.client.HTTPSConnection(hote_m, port_m, context=contexte_tls, timeout=delai_amont_s)
                        connexion.set_tunnel(parties.hostname, parties.port or 443, headers=en_tetes_tunnel)
                    else:
                        connexion = http.client.HTTPSConnection(parties.hostname, parties.port or 443, context=contexte_tls,
                                                                timeout=delai_amont_s)
                else:
                    connexion = http.client.HTTPConnection(parties.hostname, parties.port or 80, timeout=delai_amont_s)
                try:
                    connexion.request("POST", chemin_propre, body=corps, headers=en_tetes)
                    reponse = connexion.getresponse()
                    brut = reponse.read(TAILLE_MAX_REPONSE + 1)
                finally:
                    connexion.close()
            except (OSError, http.client.HTTPException, ssl.SSLError) as erreur:
                compteur.conclure(502, 0)
                motif = "amont injoignable : " + masquer(type(erreur).__name__, cle)
                ecrire_journal({"quand_utc": maintenant(), "duree_s": round(time.time() - debut, 3), "methode": "POST",
                                "chemin": chemin_propre, "modele": modele, "octets_corps": len(corps), "statut": 502,
                                "motif": motif})
                return self._repondre_json(502, {"erreur": motif, "relais": VERSION})
            if len(brut) > TAILLE_MAX_REPONSE:
                compteur.conclure(502, len(brut))
                motif = f"réponse de l'amont au-dessus de {TAILLE_MAX_REPONSE} octets : non relayée"
                ecrire_journal({"quand_utc": maintenant(), "duree_s": round(time.time() - debut, 3), "methode": "POST",
                                "chemin": chemin_propre, "modele": modele, "octets_corps": len(corps), "statut": 502,
                                "statut_amont": reponse.status, "motif": motif})
                return self._repondre_json(502, {"erreur": motif, "relais": VERSION})
            statut, octets_recus, garde = reponse.status, len(brut), usage_d_une_reponse(brut)
            self.send_response(statut)
            for k, v in reponse.getheaders():
                if k.lower() in EN_TETES_NON_RELAYES or k.lower() in ("content-length", "transfer-encoding",
                                                                      "content-encoding"):
                    continue
                self.send_header(k, masquer(v, cle))
            self.send_header("Content-Length", str(len(brut)))
            self.send_header("Connection", "close")
            self.end_headers()
            try:
                self.wfile.write(brut)
                self.wfile.flush()
            except OSError:
                pass  # client parti : l'appel est compté quand même (l'amont l'a servi)
            self.close_connection = True
            compteur.conclure(statut, octets_recus)
            ecrire_journal({"quand_utc": maintenant(), "duree_s": round(time.time() - debut, 3), "methode": "POST",
                            "chemin": chemin_propre, "modele": modele, "action": action, "octets_corps": len(corps),
                            "statut_amont": statut, "octets_reponse": octets_recus, **garde})

    return Gestionnaire


def contexte_tls_de(environnement):
    """Certificats : `SSL_CERT_FILE` de l'environnement s'il est posé, sinon ceux du système."""
    ca = environnement.get("SSL_CERT_FILE")
    if ca and not os.path.isfile(ca):
        raise RelaisInvalide(f"SSL_CERT_FILE introuvable : {ca}")
    return ssl.create_default_context(cafile=ca) if ca else ssl.create_default_context()


def servir(port, cle, amont, modeles, max_appels, max_octets_corps, journal=None, pret=None, environnement=None,
           delai_amont_s=DELAI_AMONT_DEFAUT_S, variable_cle=VARIABLE_CLE_DEFAUT):
    """Sert jusqu'à l'arrêt du processus ; `pret` (événement) est levé avec l'adresse effective dans `pret.url`."""
    environnement = os.environ if environnement is None else environnement
    if variable_cle in environnement:
        raise RelaisInvalide(f"la variable {variable_cle} doit être effacée avant de servir")
    parties = valider_amont(amont)
    mandataire = mandataire_de(environnement) if parties.scheme == "https" else None
    contexte = contexte_tls_de(environnement) if parties.scheme == "https" else None
    compteur = Compteur(max_appels, max_octets_corps)
    gestionnaire = fabriquer_gestionnaire(cle, amont, modeles, compteur, journal, threading.Lock(), mandataire, contexte,
                                          delai_amont_s, variable_cle)
    serveur = ThreadingHTTPServer((HOTE, port), gestionnaire)
    serveur.daemon_threads = True
    url = f"http://{HOTE}:{serveur.server_address[1]}"
    if pret is not None:
        pret.url = url
        pret.set()
    print(f"relais prêt sur {url} (amont {amont}, modèles {','.join(sorted(modeles))}, max-appels {max_appels}, "
          f"max-octets-corps {max_octets_corps}, mandataire {'oui' if mandataire else 'non'})", flush=True)
    try:
        serveur.serve_forever()
    finally:
        serveur.server_close()
    return url


def analyseur():
    a = argparse.ArgumentParser(prog="relais_gemini_v1",
                                description="Relais Gemini local : la commande d'Argon n'a aucune clé.")
    a.add_argument("--port", type=int, default=PORT_DEFAUT, help="0 : port libre choisi par le système (essais)")
    a.add_argument("--amont", default=AMONT_DEFAUT, help="https, ou http vers la boucle locale (essais)")
    a.add_argument("--variable-cle", default=VARIABLE_CLE_DEFAUT,
                   help="variable de l'environnement du relais qui porte la clé ; effacée après lecture")
    a.add_argument("--modele", action="append", default=None, help="modèle permis (répétable) ; défaut gemini-4-argon")
    a.add_argument("--max-appels", type=int, default=MAX_APPELS_DEFAUT, help="appels relayés au plus ; au-delà : 429")
    a.add_argument("--max-octets-corps", type=int, default=MAX_OCTETS_CORPS_DEFAUT,
                   help="taille maximale du corps d'un appel ; au-delà : 429 sans envoi")
    a.add_argument("--delai-amont-s", type=float, default=DELAI_AMONT_DEFAUT_S, help="délai d'un appel à l'amont")
    a.add_argument("--journal", help="journal des appels (JSON par ligne : jamais la clé, jamais le texte)")
    return a


def principal(argv=None):
    args = analyseur().parse_args(argv)
    try:
        cle = lire_cle(os.environ, args.variable_cle)
        if args.max_appels < 0 or args.max_octets_corps < 0:
            raise RelaisInvalide("--max-appels et --max-octets-corps : entiers positifs ou nuls requis")
        if not (args.delai_amont_s > 0):
            raise RelaisInvalide("--delai-amont-s : strictement positif requis")
        modeles = args.modele or list(MODELES_DEFAUT)
        for m in modeles:
            if not re.fullmatch(r"[A-Za-z0-9._-]+", m):
                raise RelaisInvalide(f"--modele : nom invalide {m!r}")
        servir(args.port, cle, args.amont, modeles, args.max_appels, args.max_octets_corps, args.journal,
               delai_amont_s=args.delai_amont_s, variable_cle=args.variable_cle)
    except RelaisInvalide as erreur:
        print(f"erreur : {erreur}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(principal())
