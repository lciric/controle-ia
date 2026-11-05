#!/usr/bin/env python3
"""Relais Kimi local, version 2 : le client n'a **aucune clé** ; le relais tient la clé, les modèles permis et un plafond en
dollars.

Version 2 (session-depot, 30 octobre 2026) = version 1 (`relais_kimi_v1.py`, inchangée, R12) plus l'option
`--lister-modeles` : le relais lit la clé dans sa variable (puis l'efface), fait **un seul** appel `GET /v1/models` à
l'amont, imprime **seulement** les identifiants de modèles rendus (un par ligne, triés), puis sort sans servir. Code de
sortie : 0 si la liste est lue ; 3 si l'amont répond autrement que 200 ou par un corps illisible (statut et motif court,
clé masquée, aucun corps recopié) ; 2 pour un réglage invalide ou une clé absente. Rien d'autre n'est imprimé : ni la
clé, ni les autres champs de la réponse. En mode service, `--modeles-permis`, `--plafond-usd` et les trois prix restent
obligatoires (refus de démarrer, code 2, s'ils manquent) ; en mode liste, ils sont ignorés.

Lignée session-depot, 30 octobre 2026. Même modèle que le relais Gemini (`lancement-v2/relais_gemini_v1.py`) et le relais
Claude du pôle (`orchestrateur-v50/arbre/pole/relais_reel.py`) : un petit serveur HTTP dans **son propre processus**, sur la
boucle locale seulement (`127.0.0.1`, aucune option ne le change), qui relaie l'API Moonshot (Kimi, compatible OpenAI).

Clé : lue **une seule fois** au démarrage dans la variable `--variable-cle` (`KIMI_API_KEY` par défaut) de l'environnement
du relais, puis **effacée** de `os.environ` et gardée en mémoire. Jamais en argument, jamais dans un fichier, jamais
journalisée ni affichée. Le relais **retire** toute clé reçue du client (`Authorization`, `x-api-key`) et pose la sienne
(`Authorization: Bearer …`). Limite connue (reprise de `relais_reel.py`, contre-lecture F-C7) : effacer la variable de
`os.environ` n'efface pas le bloc initial que `/proc/<pid>/environ` expose ; tout processus du même utilisateur (ou root)
peut l'y lire tant que le relais vit.

Amont : fixe, `--amont` (défaut `https://api.moonshot.ai`, adresse mondiale ; la plateforme chinoise est
`https://api.moonshot.cn`, clés non interchangeables). Source : documentation officielle « Service Address »
(https://platform.kimi.ai/docs/api/overview), vue le 30 octobre 2026 **par extrait de moteur de recherche seulement** : la
page elle-même n'est pas joignable depuis la session (hôte hors des domaines permis). À revérifier avant tout GO. Le relais
passe par le mandataire `HTTPS_PROXY` (ou `https_proxy`) et les certificats `SSL_CERT_FILE` de son environnement.

Ce que le relais refuse **sans rien envoyer** à l'amont :
- tout chemin autre que `POST /v1/chat/completions` (chaîne de requête comprise) et `GET /relais/etat` : 403 ;
- une requête sans `Content-Length` (ou en morceaux) : 411 ; un corps de plus de `--max-octets-corps` octets : 413 ;
- un corps qui n'est pas un objet JSON : 400 ;
- un modèle demandé (`model` du corps) hors de `--modeles-permis` (noms exacts) : 403, compté en `refus_modele` (R-764) ;
- `stream` vrai : 400 (voir « Flux » plus bas) ; un outil de type autre que `function` (les fonctions intégrées de Moonshot,
  telle la recherche web, sont facturées hors de `usage` : le plafond ne les verrait pas) : 400 ;
- au-delà de `--max-appels` appels relayés : 429 ;
- toute requête dont la réserve ferait franchir `--plafond-usd` : 402.

Modèle servi (barrière R-764) : sur une réponse 200, le champ `model` de la réponse est comparé **exactement** au modèle
demandé. Un écart (ou un champ absent, ou une réponse illisible) est un **refus de modèle** : la réponse n'est **pas** relayée
(502 « modèle servi différent »), l'écart est compté (`refus_modele`, `ecarts_modele_servi`) et journalisé, et la dépense
est quand même portée au compteur (l'amont a servi).

Plafond : chaque appel **réserve** avant de partir `max(--reserve-par-appel, pire cas de la requête)` sous verrou (des
appels simultanés ne peuvent pas franchir le plafond ensemble), puis règle au coût lu dans `usage` :
    coût = (prompt_tokens − cached) × prix_entree + cached × prix_cache + completion_tokens × prix_sortie
           + max(0, total_tokens − prompt_tokens − completion_tokens) × max(prix)        (USD par million de jetons)
où `cached` est `usage.cached_tokens` ou `usage.prompt_tokens_details.cached_tokens` (le plus grand ; supposé compris
dans `prompt_tokens`, convention OpenAI ; un excédent au-delà de `prompt_tokens` est compté au prix fort). Un usage absent ou illisible (réponse 200 comme réponse d'erreur, ou coupure après envoi) compte au
**pire cas** de la requête :
    pire cas = (octets du corps + 1024) × prix_entree + max_tokens × n × prix_sortie
avec `max_tokens` (ou `max_completion_tokens`) du corps, sinon `--max-jetons-sortie-pire-cas`. Hypothèse : un jeton d'entrée
fait au moins un octet du corps (vrai pour un découpage par octets ; les images peuvent l'enfreindre : réserve écrite).

Flux (`stream`) : **refusé**. Raisons : (1) la barrière du modèle servi exige de lire `model` **avant** de rendre quoi que ce
soit au client ; en flux, les premiers morceaux seraient déjà partis ; (2) en flux, `usage` n'arrive qu'au dernier morceau
et seulement si le client a demandé `stream_options.include_usage` : un flux coupé ou sans cette option ne porterait
aucun usage, donc toujours le pire cas ; (3) la réponse entière tient en mémoire (borne `TAILLE_MAX_REPONSE`).

Journal (`--journal`, JSON par ligne) : heure UTC, chemin, modèle demandé et servi, octets, statut, `usage` (nombres
seulement), coût, dépense cumulée, motif d'un refus — **jamais le texte, jamais la clé**. `GET /relais/etat` : compteurs,
bornes, prix, PID, et la preuve que la variable de clé n'est plus dans l'environnement du processus.

Arrêt **par PID** (R10). Le processus Python est lancé **directement**, sans `setsid` ni `nohup` (incident du 30 octobre :
un lanceur avait tué l'enveloppe et laissé le relais vivant). `env -i` remplace son propre processus par Python (même
PID) : `$!` est donc le PID du relais, que `/relais/etat` rend aussi (`pid`) pour vérification avant `kill`.

    env -i PATH=/usr/bin:/bin LANG=C.UTF-8 KIMI_API_KEY="$CLE" HTTPS_PROXY="$HTTPS_PROXY" \\
        SSL_CERT_FILE=/root/.ccr/ca-bundle.crt python3 -I -B relais_kimi_v2.py --port 8789 \\
        --modeles-permis <id-exact> --plafond-usd 5 --prix-entree <p> --prix-sortie <p> --prix-cache <p> \\
        --max-appels 64 --journal $DOS/relais-kimi-journal-v1.jsonl > $DOS/relais-kimi-v1.log 2>&1 &
    echo $! > $DOS/relais-kimi.pid

Ce fichier n'est jamais exécuté avec une vraie clé dans ce dépôt : ses essais (`test_relais_kimi_v1.py`) le lancent avec une
clé factice devant un faux amont local. Aucune dépendance hors bibliothèque standard.
"""

import argparse
import base64
import datetime
import http.client
import json
import math
import os
import re
import ssl
import sys
import threading
import time
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

VERSION = "relais-kimi-v2"
HOTE = "127.0.0.1"  # jamais une autre interface : aucune option ne le change
PORT_DEFAUT = 8789
AMONT_DEFAUT = "https://api.moonshot.ai"
VARIABLE_CLE_DEFAUT = "KIMI_API_KEY"
CHEMIN_PERMIS = "/v1/chat/completions"
CHEMIN_ETAT = "/relais/etat"
CHEMIN_MODELES = "/v1/models"  # seulement en mode `--lister-modeles`, jamais servi aux clients
MAX_APPELS_DEFAUT = 64
MAX_OCTETS_CORPS_DEFAUT = 4_000_000
RESERVE_PAR_APPEL_DEFAUT = 0.40
MAX_JETONS_SORTIE_PIRE_CAS_DEFAUT = 262_144  # fenêtre annoncée des modèles Kimi récents : borne haute, à revoir
MARGE_JETONS_ENTREE = 1024                   # jetons spéciaux du gabarit de conversation, au-delà des octets du corps
TAILLE_MAX_REPONSE = 50_000_000
DELAI_AMONT_DEFAUT_S = 1800.0
HOTES_LOCAUX = {"127.0.0.1", "localhost", "::1"}
MOTIF_MODELE = re.compile(r"[A-Za-z0-9._:-]+")
EN_TETES_DE_CLE = {"authorization", "x-api-key", "proxy-authorization", "api-key"}
EN_TETES_NON_RELAYES = EN_TETES_DE_CLE | {"host", "connection", "content-length", "transfer-encoding", "keep-alive", "te",
                                          "trailer", "upgrade", "accept-encoding", "expect", "cookie"}
EN_TETES_REPONSE_NON_RELAYES = EN_TETES_NON_RELAYES | {"content-encoding", "set-cookie"}


class RelaisInvalide(Exception):
    """Réglage impossible : le relais ne démarre pas."""


def masquer(texte, cle):
    """Ne laisse jamais passer la clé dans un message, un journal ou une réponse."""
    texte = str(texte)
    return texte.replace(cle, "[clé]") if cle else texte


def lire_cle(environnement, variable):
    """Lit la clé dans l'environnement donné et l'en efface ; ne la rend qu'à l'appelant (jamais journalisée)."""
    cle = (environnement.get(variable) or "").strip()
    environnement.pop(variable, None)
    if not cle:
        raise RelaisInvalide(f"aucune clé dans la variable {variable} de l'environnement du relais")
    if any(c in cle for c in "\r\n"):
        raise RelaisInvalide(f"clé de la variable {variable} sur plusieurs lignes : refusée")
    return cle


def valider_amont(amont):
    """`https://` vers n'importe quel hôte, ou `http://` vers la boucle locale seulement (essais) ; sans chemin."""
    p = urllib.parse.urlsplit(amont)
    if p.path not in ("", "/") or p.query or p.fragment or p.username:
        raise RelaisInvalide(f"--amont : schéma et hôte seulement, sans chemin (reçu {amont!r})")
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
        jeton = base64.b64encode(f"{urllib.parse.unquote(p.username)}:{urllib.parse.unquote(p.password or '')}"
                                 .encode("utf-8")).decode("ascii")
        en_tetes["Proxy-Authorization"] = "Basic " + jeton
    return p.hostname, p.port, en_tetes


def contexte_tls_de(environnement):
    """Certificats : `SSL_CERT_FILE` de l'environnement s'il est posé, sinon ceux du système."""
    ca = environnement.get("SSL_CERT_FILE")
    if ca and not os.path.isfile(ca):
        raise RelaisInvalide(f"SSL_CERT_FILE introuvable : {ca}")
    return ssl.create_default_context(cafile=ca) if ca else ssl.create_default_context()


def lire_modeles_permis(texte):
    """`a,b` → tuple de noms exacts, non vide ; la forme `role=modele` et tout caractère hors `[A-Za-z0-9._:-]` sont refusés."""
    noms = tuple(m.strip() for m in (texte or "").split(",") if m.strip())
    if not noms:
        raise RelaisInvalide("--modeles-permis : au moins un nom exact de modèle requis")
    for n in noms:
        if not MOTIF_MODELE.fullmatch(n):
            raise RelaisInvalide(f"--modeles-permis : nom de modèle exact attendu, reçu {n!r}")
    return noms


class Bareme:
    """Prix en USD par million de jetons (entrée, sortie, lecture de cache), passés en arguments, jamais par défaut."""

    def __init__(self, entree, sortie, cache, max_jetons_sortie_pire_cas):
        for nom, v in (("--prix-entree", entree), ("--prix-sortie", sortie), ("--prix-cache", cache)):
            if not (isinstance(v, (int, float)) and math.isfinite(v) and v >= 0):
                raise RelaisInvalide(f"{nom} : nombre positif ou nul requis")
        if not (int(max_jetons_sortie_pire_cas) > 0):
            raise RelaisInvalide("--max-jetons-sortie-pire-cas : entier strictement positif requis")
        self.entree, self.sortie, self.cache = float(entree), float(sortie), float(cache)
        self.max_jetons_sortie = int(max_jetons_sortie_pire_cas)

    def cout_usage(self, usage):
        """Coût d'un `usage` lisible, ou None s'il manque `prompt_tokens` ou `completion_tokens` (entiers ≥ 0)."""
        if not isinstance(usage, dict):
            return None
        p, c = usage.get("prompt_tokens"), usage.get("completion_tokens")
        if not (_entier(p) and _entier(c)):
            return None
        details = usage.get("prompt_tokens_details") if isinstance(usage.get("prompt_tokens_details"), dict) else {}
        caches = [x for x in (usage.get("cached_tokens"), details.get("cached_tokens")) if _entier(x)]
        cache_lu = max(caches) if caches else 0
        cache = min(cache_lu, p)                    # convention OpenAI : le cache est compris dans prompt_tokens
        t = usage.get("total_tokens")
        hors_compte = (cache_lu - cache) + (max(0, t - p - c) if _entier(t) else 0)  # jetons sans case : prix fort
        return ((p - cache) * self.entree + cache * self.cache + c * self.sortie
                + hors_compte * max(self.entree, self.sortie, self.cache)) / 1_000_000

    def pire_cas(self, octets_corps, demande):
        """Borne haute du coût d'une requête d'après son seul corps (voir la docstring du module)."""
        sortie = None
        for k in ("max_completion_tokens", "max_tokens"):
            if _entier(demande.get(k)) and demande[k] > 0:
                sortie = demande[k] if sortie is None else max(sortie, demande[k])
        sortie = sortie if sortie is not None else self.max_jetons_sortie
        n = demande.get("n") if _entier(demande.get("n")) and demande.get("n") > 0 else 1
        return ((octets_corps + MARGE_JETONS_ENTREE) * self.entree + sortie * n * self.sortie) / 1_000_000

    def etat(self):
        return {"prix_entree_usd_par_million": self.entree, "prix_sortie_usd_par_million": self.sortie,
                "prix_cache_usd_par_million": self.cache, "max_jetons_sortie_pire_cas": self.max_jetons_sortie}


def _entier(x):
    return isinstance(x, int) and not isinstance(x, bool) and x >= 0


class Compteur:
    """Plafond en dollars, appels et refus. Un appel est **admis sous verrou** (borne d'appels, réserve) avant de partir :
    des appels simultanés ne peuvent franchir ni `--max-appels` ni `--plafond-usd` ensemble. La dépense ne dépasse le
    plafond que si un coût lu dépasse sa réserve (journalisé : `appels_au_dessus_de_la_reserve`)."""

    def __init__(self, plafond_usd, reserve_par_appel, max_appels, max_octets_corps):
        self.plafond, self.reserve_min = float(plafond_usd), float(reserve_par_appel)
        self.max_appels, self.max_octets_corps = int(max_appels), int(max_octets_corps)
        self.depense, self.engage = 0.0, 0.0
        self.appels, self.refus, self.refus_modele, self.ecarts_modele_servi = 0, 0, 0, 0
        self.usages_absents, self.depassements, self.depassement_max = 0, 0, 0.0
        self.par_statut = {}
        self._verrou = threading.Lock()

    def refuser(self, modele=False):
        with self._verrou:
            self.refus += 1
            if modele:
                self.refus_modele += 1

    def admettre(self, montant):
        """Compte l'appel et engage `montant`, ou rend (statut, motif) du refus."""
        with self._verrou:
            if self.appels >= self.max_appels:
                self.refus += 1
                return 429, f"--max-appels ({self.max_appels}) atteint"
            if self.depense + self.engage + montant > self.plafond + 1e-12:
                self.refus += 1
                return 402, (f"plafond de dépense du relais atteint (réserve de {montant:.6f} USD au-delà de "
                             f"{self.plafond} USD)")
            self.appels += 1
            self.engage += montant
            return None

    def regler(self, montant, cout, statut, usage_absent=False, ecart_modele=False):
        with self._verrou:
            self.engage -= montant
            self.depense += cout
            self.par_statut[str(statut)] = self.par_statut.get(str(statut), 0) + 1
            if usage_absent:
                self.usages_absents += 1
            if ecart_modele:
                self.refus_modele += 1
                self.ecarts_modele_servi += 1
            if cout > montant + 1e-12:
                self.depassements += 1
                self.depassement_max = max(self.depassement_max, cout - montant)
            return self.depense

    def etat(self):
        with self._verrou:
            return {"plafond_usd": self.plafond, "reserve_par_appel_usd": self.reserve_min,
                    "depense_usd": round(self.depense, 6), "engage_usd": round(self.engage, 6),
                    "restant_usd": round(self.plafond - self.depense, 6), "appels": self.appels,
                    "appels_restants": max(0, self.max_appels - self.appels), "max_appels": self.max_appels,
                    "max_octets_corps": self.max_octets_corps, "refus": self.refus, "refus_modele": self.refus_modele,
                    "ecarts_modele_servi": self.ecarts_modele_servi, "usages_absents": self.usages_absents,
                    "appels_au_dessus_de_la_reserve": self.depassements,
                    "depassement_max_usd": round(self.depassement_max, 6), "reponses_par_statut": dict(self.par_statut)}


def lire_reponse(brut):
    """(objet JSON, ou None si illisible)."""
    try:
        objet = json.loads(brut.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        return None
    return objet if isinstance(objet, dict) else None


def usage_numerique(usage):
    """Ce que le journal garde de `usage` : les nombres, à un niveau d'imbrication, et rien d'autre."""
    if not isinstance(usage, dict):
        return None
    garde = {}
    for k, v in usage.items():
        if isinstance(v, (int, float)) and not isinstance(v, bool):
            garde[str(k)[:60]] = v
        elif isinstance(v, dict):
            sous = {str(k2)[:60]: v2 for k2, v2 in v.items() if isinstance(v2, (int, float)) and not isinstance(v2, bool)}
            if sous:
                garde[str(k)[:60]] = sous
    return garde


def nom_court(x):
    """Nom de modèle pour le journal : chaîne tronquée, sinon le type (jamais un contenu arbitraire long)."""
    if isinstance(x, str):
        return x[:80]
    return None if x is None else f"[{type(x).__name__}]"


def fabriquer_gestionnaire(cle, amont, modeles, bareme, compteur, journal, verrou_journal, mandataire, contexte_tls,
                           delai_amont_s, variable_cle):
    parties = valider_amont(amont)
    modeles = tuple(modeles)
    etat_fixe = {"version": VERSION, "amont": amont, "modeles_permis": list(modeles), "mandataire": bool(mandataire),
                 "flux": "refusé", "pid": os.getpid(), **bareme.etat()}

    def ecrire_journal(entree):
        if journal is None:
            return
        ligne = json.dumps(entree, ensure_ascii=False, sort_keys=True)
        if cle in ligne:  # garde-fou ; le texte et la clé sont exclus par construction
            ligne = json.dumps({"quand_utc": entree.get("quand_utc"), "erreur_journal": "entrée masquée"})
        with verrou_journal:
            with open(journal, "a", encoding="utf-8") as f:
                f.write(ligne + "\n")

    def maintenant():
        return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="milliseconds")

    def connexion_amont():
        if parties.scheme == "https":
            if mandataire:
                hote_m, port_m, en_tetes_tunnel = mandataire
                c = http.client.HTTPSConnection(hote_m, port_m, context=contexte_tls, timeout=delai_amont_s)
                c.set_tunnel(parties.hostname, parties.port or 443, headers=en_tetes_tunnel)
                return c
            return http.client.HTTPSConnection(parties.hostname, parties.port or 443, context=contexte_tls,
                                               timeout=delai_amont_s)
        return http.client.HTTPConnection(parties.hostname, parties.port or 80, timeout=delai_amont_s)

    class Gestionnaire(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"
        server_version = "RelaisKimi/2"
        sys_version = ""

        def log_message(self, format, *args):  # noqa: A002 — signature imposée par la bibliothèque standard
            pass  # aucun journal implicite sur un terminal partagé

        def _repondre_json(self, statut, objet):
            corps = json.dumps(objet, ensure_ascii=False).encode("utf-8")
            self.send_response(statut)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(corps)))
            self.send_header("Connection", "close")
            self.end_headers()
            try:
                self.wfile.write(corps)
            except OSError:
                pass
            self.close_connection = True

        def _refuser(self, statut, motif, chemin, modele=None, refus_modele=False, **plus):
            compteur.refuser(modele=refus_modele)
            ecrire_journal({"quand_utc": maintenant(), "methode": self.command, "chemin": chemin,
                            "modele": nom_court(modele), "statut": statut, "motif": motif, **plus})
            return self._repondre_json(statut, {"erreur": motif, "relais": VERSION})

        def _cible_brute(self):
            """Cible telle que reçue sur la ligne de requête : la bibliothèque standard récrit `//x` en `/x` dans
            `self.path` ; le relais compare l'original, pour ne relayer que le chemin exact."""
            parties_ligne = (self.requestline or "").split()
            return parties_ligne[1] if len(parties_ligne) == 3 else None

        def do_GET(self):
            if self._cible_brute() == CHEMIN_ETAT:
                return self._repondre_json(200, dict(etat_fixe, variable_cle_encore_presente=variable_cle in os.environ,
                                                     **compteur.etat()))
            return self._refuser(403, "chemin non relayé", "[chemin refusé]")

        def do_POST(self):
            if self._cible_brute() != CHEMIN_PERMIS:
                return self._refuser(403, f"chemin non relayé ({CHEMIN_PERMIS} seulement, sans paramètre)",
                                     "[chemin refusé]")
            return self._relayer()

        def _autre_methode(self):
            return self._refuser(403, f"méthode {self.command} non relayée", "[chemin refusé]")

        do_PUT = do_DELETE = do_PATCH = do_HEAD = do_OPTIONS = _autre_methode

        def _relayer(self):
            debut = time.time()
            ch = CHEMIN_PERMIS
            if "content-length" not in self.headers or self.headers.get("transfer-encoding"):
                return self._refuser(411, "Content-Length requis (aucun corps en morceaux)", ch)
            try:
                longueur = int(self.headers["content-length"])
                if longueur < 0:
                    raise ValueError
            except ValueError:
                return self._refuser(411, "Content-Length invalide", ch)
            if longueur > compteur.max_octets_corps:
                return self._refuser(413, f"corps de {longueur} octets au-dessus de --max-octets-corps "
                                          f"({compteur.max_octets_corps})", ch, octets_corps=longueur)
            corps = self.rfile.read(longueur) if longueur else b""
            if len(corps) != longueur:
                return self._refuser(400, "corps incomplet", ch)
            demande = lire_reponse(corps)
            if demande is None:
                return self._refuser(400, "corps : objet JSON attendu", ch, octets_corps=longueur)
            modele = demande.get("model")
            if not (isinstance(modele, str) and modele in modeles):
                return self._refuser(403, "modèle non permis (R-764) : permis " + ", ".join(modeles), ch, modele,
                                     refus_modele=True, octets_corps=longueur)
            if demande.get("stream") not in (None, False):
                return self._refuser(400, "flux (stream) refusé par le relais : stream=false requis", ch, modele,
                                     octets_corps=longueur)
            outils = demande.get("tools")
            if outils is not None and not (isinstance(outils, list) and all(
                    isinstance(o, dict) and o.get("type") == "function" for o in outils)):
                return self._refuser(400, "outil hors du type « function » refusé (facturation hors usage)", ch, modele,
                                     octets_corps=longueur)
            reserve = max(compteur.reserve_min, bareme.pire_cas(longueur, demande))
            refus = compteur.admettre(reserve)
            if refus:
                statut, motif = refus
                ecrire_journal({"quand_utc": maintenant(), "methode": "POST", "chemin": ch, "modele": modele,
                                "octets_corps": longueur, "statut": statut, "motif": motif,
                                "reserve_usd": round(reserve, 6)})
                return self._repondre_json(statut, {"erreur": motif, "relais": VERSION, **compteur.etat()})

            en_tetes = {k: v for k, v in self.headers.items() if k.lower() not in EN_TETES_NON_RELAYES}
            en_tetes["Authorization"] = "Bearer " + cle
            en_tetes["Accept-Encoding"] = "identity"
            en_tetes["Host"] = parties.netloc
            en_tetes["Content-Length"] = str(len(corps))
            en_tetes["Connection"] = "close"
            envoye, reponse, brut = False, None, b""
            try:
                connexion = connexion_amont()
                try:
                    connexion.request("POST", CHEMIN_PERMIS, body=corps, headers=en_tetes)
                    envoye = True
                    reponse = connexion.getresponse()
                    brut = reponse.read(TAILLE_MAX_REPONSE + 1)
                finally:
                    connexion.close()
            except (OSError, http.client.HTTPException, ssl.SSLError) as erreur:
                cout = bareme.pire_cas(longueur, demande) if envoye else 0.0  # envoyé : l'amont a pu facturer
                cumul = compteur.regler(reserve, cout, 502, usage_absent=envoye)
                motif = ("amont coupé après envoi (dépense au pire cas) : " if envoye else "amont injoignable : ") \
                    + masquer(type(erreur).__name__, cle)
                ecrire_journal({"quand_utc": maintenant(), "duree_s": round(time.time() - debut, 3), "methode": "POST",
                                "chemin": ch, "modele": modele, "octets_corps": longueur, "statut": 502, "motif": motif,
                                "cout_usd": round(cout, 6), "depense_cumulee_usd": round(cumul, 6)})
                return self._repondre_json(502, {"erreur": motif, "relais": VERSION})

            objet = lire_reponse(brut) if len(brut) <= TAILLE_MAX_REPONSE else None
            usage = objet.get("usage") if objet else None
            cout = bareme.cout_usage(usage)
            usage_absent = cout is None
            if usage_absent:
                cout = bareme.pire_cas(longueur, demande)
            servi = objet.get("model") if objet else None
            ecart = reponse.status == 200 and servi != modele
            trop_gros = len(brut) > TAILLE_MAX_REPONSE
            statut_client = 502 if (ecart or trop_gros) else reponse.status
            cumul = compteur.regler(reserve, cout, statut_client, usage_absent=usage_absent, ecart_modele=ecart)
            entree = {"quand_utc": maintenant(), "duree_s": round(time.time() - debut, 3), "methode": "POST", "chemin": ch,
                      "modele": modele, "modele_servi": nom_court(servi), "octets_corps": longueur,
                      "statut_amont": reponse.status, "octets_reponse": len(brut), "usage": usage_numerique(usage),
                      "usage_absent": usage_absent, "cout_usd": round(cout, 6), "reserve_usd": round(reserve, 6),
                      "depense_cumulee_usd": round(cumul, 6)}
            if ecart:
                motif = "modèle servi différent du modèle demandé (R-764) : réponse non relayée"
                ecrire_journal(dict(entree, statut=502, motif=motif))
                return self._repondre_json(502, {"erreur": motif, "relais": VERSION, "modele_demande": modele,
                                                 "modele_servi": nom_court(servi)})
            if trop_gros:
                motif = f"réponse de l'amont au-dessus de {TAILLE_MAX_REPONSE} octets : non relayée"
                ecrire_journal(dict(entree, statut=502, motif=motif))
                return self._repondre_json(502, {"erreur": motif, "relais": VERSION})
            ecrire_journal(entree)
            self.send_response(reponse.status)
            for k, v in reponse.getheaders():
                if k.lower() in EN_TETES_REPONSE_NON_RELAYES:
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

    return Gestionnaire


def servir(port, cle, amont, modeles, bareme, plafond_usd, reserve_par_appel, max_appels, max_octets_corps, journal=None,
           pret=None, environnement=None, delai_amont_s=DELAI_AMONT_DEFAUT_S, variable_cle=VARIABLE_CLE_DEFAUT):
    """Sert jusqu'à l'arrêt du processus ; `pret` (événement) est levé avec l'adresse effective dans `pret.url`."""
    environnement = os.environ if environnement is None else environnement
    if variable_cle in environnement:
        raise RelaisInvalide(f"la variable {variable_cle} doit être effacée avant de servir")
    parties = valider_amont(amont)
    mandataire = mandataire_de(environnement) if parties.scheme == "https" else None
    contexte = contexte_tls_de(environnement) if parties.scheme == "https" else None
    compteur = Compteur(plafond_usd, reserve_par_appel, max_appels, max_octets_corps)
    gestionnaire = fabriquer_gestionnaire(cle, amont, modeles, bareme, compteur, journal, threading.Lock(), mandataire,
                                          contexte, delai_amont_s, variable_cle)
    serveur = ThreadingHTTPServer((HOTE, port), gestionnaire)
    serveur.daemon_threads = True
    url = f"http://{HOTE}:{serveur.server_address[1]}"
    if pret is not None:
        pret.url = url
        pret.set()
    print(f"relais prêt sur {url} (pid {os.getpid()}, amont {amont}, modèles {','.join(modeles)}, plafond {plafond_usd} "
          f"USD, max-appels {max_appels}, max-octets-corps {max_octets_corps}, mandataire "
          f"{'oui' if mandataire else 'non'}, flux refusé)", flush=True)
    try:
        serveur.serve_forever()
    finally:
        serveur.server_close()
    return url


def lister_modeles(cle, amont, environnement, delai_amont_s=60.0):
    """v2 : un seul `GET /v1/models` à l'amont ; rend la liste triée des identifiants (`data[].id`). Lève `ListeIllisible`
    (statut et motif court, clé masquée, aucun corps recopié) si la réponse n'est pas un 200 lisible."""
    parties = valider_amont(amont)
    if parties.scheme == "https":
        mandataire, contexte = mandataire_de(environnement), contexte_tls_de(environnement)
        if mandataire:
            hote_m, port_m, en_tetes_tunnel = mandataire
            c = http.client.HTTPSConnection(hote_m, port_m, context=contexte, timeout=delai_amont_s)
            c.set_tunnel(parties.hostname, parties.port or 443, headers=en_tetes_tunnel)
        else:
            c = http.client.HTTPSConnection(parties.hostname, parties.port or 443, context=contexte, timeout=delai_amont_s)
    else:
        c = http.client.HTTPConnection(parties.hostname, parties.port or 80, timeout=delai_amont_s)
    try:
        c.request("GET", CHEMIN_MODELES, headers={"Authorization": "Bearer " + cle, "Accept": "application/json"})
        r = c.getresponse()
        brut = r.read(TAILLE_MAX_REPONSE + 1)
        statut = r.status
    except (OSError, http.client.HTTPException) as e:
        raise ListeIllisible(masquer(f"amont injoignable : {type(e).__name__}", cle))
    finally:
        c.close()
    if statut != 200:
        raise ListeIllisible(f"amont : statut {statut} (corps non recopié)")
    try:
        objet = json.loads(brut.decode("utf-8"))
        ids = sorted({str(m["id"]) for m in objet["data"]})
    except (ValueError, KeyError, TypeError, UnicodeDecodeError):
        raise ListeIllisible("amont : liste de modèles illisible (corps non recopié)")
    if not ids:
        raise ListeIllisible("amont : liste de modèles vide")
    return [masquer(i, cle) for i in ids]


class ListeIllisible(Exception):
    """v2 : la liste des modèles n'a pas pu être lue (code de sortie 3)."""


def analyseur():
    a = argparse.ArgumentParser(prog="relais_kimi_v2", description="Relais Kimi local : le client n'a aucune clé.")
    a.add_argument("--port", type=int, default=PORT_DEFAUT, help="0 : port libre choisi par le système (essais)")
    a.add_argument("--amont", default=AMONT_DEFAUT, help="https, ou http vers la boucle locale (essais) ; sans chemin")
    a.add_argument("--variable-cle", default=VARIABLE_CLE_DEFAUT,
                   help="variable de l'environnement du relais qui porte la clé ; effacée après lecture")
    a.add_argument("--modeles-permis", help="noms exacts des modèles admis, séparés par des virgules")
    a.add_argument("--plafond-usd", type=float, help="plafond de dépense tenu par le relais")
    a.add_argument("--reserve-par-appel", type=float, default=RESERVE_PAR_APPEL_DEFAUT,
                   help="réserve minimale par appel (la réserve effective est le plus grand de ceci et du pire cas)")
    a.add_argument("--prix-entree", type=float, help="USD par million de jetons d'entrée (hors cache)")
    a.add_argument("--prix-sortie", type=float, help="USD par million de jetons de sortie")
    a.add_argument("--prix-cache", type=float, help="USD par million de jetons d'entrée lus en cache")
    a.add_argument("--max-jetons-sortie-pire-cas", type=int, default=MAX_JETONS_SORTIE_PIRE_CAS_DEFAUT,
                   help="jetons de sortie supposés quand la requête ne porte pas max_tokens")
    a.add_argument("--max-appels", type=int, default=MAX_APPELS_DEFAUT, help="appels relayés au plus ; au-delà : 429")
    a.add_argument("--max-octets-corps", type=int, default=MAX_OCTETS_CORPS_DEFAUT,
                   help="taille maximale du corps d'un appel ; au-delà : 413 sans envoi")
    a.add_argument("--delai-amont-s", type=float, default=DELAI_AMONT_DEFAUT_S, help="délai d'un appel à l'amont")
    a.add_argument("--journal", help="journal des appels (JSON par ligne : jamais la clé, jamais le texte)")
    a.add_argument("--lister-modeles", action="store_true",
                   help="v2 : un seul GET /v1/models à l'amont, imprime les identifiants de modèles, sort sans servir")
    return a


def principal(argv=None):
    args = analyseur().parse_args(argv)
    try:
        cle = lire_cle(os.environ, args.variable_cle)  # d'abord : la variable est effacée même si un réglage est faux
        if args.lister_modeles:
            if not (args.delai_amont_s > 0):
                raise RelaisInvalide("--delai-amont-s : strictement positif requis")
            try:
                ids = lister_modeles(cle, args.amont, os.environ, min(args.delai_amont_s, 120.0))
            except ListeIllisible as erreur:
                print(f"erreur : {erreur}", file=sys.stderr)
                return 3
            for i in ids:
                print(i)
            return 0
        manquants = [n for n, v in (("--modeles-permis", args.modeles_permis), ("--plafond-usd", args.plafond_usd),
                                    ("--prix-entree", args.prix_entree), ("--prix-sortie", args.prix_sortie),
                                    ("--prix-cache", args.prix_cache)) if v is None]
        if manquants:
            raise RelaisInvalide("réglages obligatoires pour servir : " + ", ".join(manquants))
        if not (math.isfinite(args.plafond_usd) and args.plafond_usd > 0):
            raise RelaisInvalide("--plafond-usd : strictement positif requis")
        if not (math.isfinite(args.reserve_par_appel) and args.reserve_par_appel >= 0):
            raise RelaisInvalide("--reserve-par-appel : positif ou nul requis")
        if args.max_appels < 0 or args.max_octets_corps < 0:
            raise RelaisInvalide("--max-appels et --max-octets-corps : entiers positifs ou nuls requis")
        if not (args.delai_amont_s > 0):
            raise RelaisInvalide("--delai-amont-s : strictement positif requis")
        bareme = Bareme(args.prix_entree, args.prix_sortie, args.prix_cache, args.max_jetons_sortie_pire_cas)
        servir(args.port, cle, args.amont, lire_modeles_permis(args.modeles_permis), bareme, args.plafond_usd,
               args.reserve_par_appel, args.max_appels, args.max_octets_corps, args.journal,
               delai_amont_s=args.delai_amont_s, variable_cle=args.variable_cle)
    except RelaisInvalide as erreur:
        print(f"erreur : {erreur}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(principal())
