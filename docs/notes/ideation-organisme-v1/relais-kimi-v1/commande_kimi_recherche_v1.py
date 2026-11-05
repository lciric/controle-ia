#!/usr/bin/env python3
"""Commande Kimi avec recherche Web officielle (boucle d'outil côté client), version 1.

Lignée session-depot, 30 octobre 2026. Demande du n° 263 de conv-audit (mot de Lazar « demande à Kimi ») : Kimi K3.1 Pro
lit des sources primaires avec la recherche Web de l'API Moonshot. Même contrat de sortie que `commande_kimi_v1.py` :
consigne sur l'entrée standard (UTF-8), un seul message utilisateur ; plafond dans `PLAFOND_SESSION_USD` ; `ROLE_POLE`
absent ou `lecteur_sources` ; `MODELE_DEMANDE_POLE`, s'il est posé, doit égaler `--modele` ; la **dernière ligne** de la
sortie standard est toujours un objet JSON `{"texte", "cout_usd", "modele_servi", "tours", "recherches", …}`, coût fini
et strictement positif, aussi sur un échec.

**Aucune clé ici.** La commande parle au relais Kimi local v4 (`relais_kimi_v4.py`, boucle locale, sans mandataire), lancé
avec `--max-recherches N --prix-recherche P` ; le relais tient la clé, la barrière du modèle servi, la barrière des outils
(seule la recherche officielle, déclarée à l'identique) et son propre plafond, qui compte le prix des recherches.

Boucle (forme lue dans https://platform.kimi.ai/docs/guide/use-official-tools, 30 octobre 2026) :
1. la déclaration de `web_search` est lue par le relais (`GET /v1/formulas/moonshot/web-search:latest/tools`), ou prise
   dans la documentation (`--declaration doc`) ;
2. `POST /v1/chat/completions` avec `tools: [déclaration]` ; si la réponse porte des `tool_calls`, le message assistant
   **entier** (`content`, `reasoning_content`, `tool_calls`) est gardé dans l'historique (consigne de K3.1 Pro :
   https://platform.kimi.ai/docs/guide/kimi-k3-1-pro-quickstart) ;
3. chaque appel `web_search` est exécuté par `POST /v1/formulas/moonshot/web-search:latest/fibers` avec `name` et
   `arguments` **recopiés tels quels** ; le résultat (`context.output`, sinon `context.encrypted_output`) part dans un
   message `role: "tool"` au `tool_call_id` aligné ; un appel non exécuté (autre nom, borne, budget, refus) reçoit quand
   même un message `tool` qui le dit, car l'API exige une réponse par appel ;
4. retour en 2, jusqu'à une réponse sans `tool_calls`.

Bornes : au plus `--max-tours` appels au modèle et `--max-recherches` recherches. Dès qu'une borne ou le budget empêche
une recherche, la commande passe `tool_choice: "none"` à l'appel suivant (réponse finale imposée) ; le dernier tour permis
l'est toujours. Une réponse qui porte encore des `tool_calls` sous `tool_choice: "none"`, ou au dernier tour : code 5.

Budget, avant chaque envoi (hypothèse du relais : un jeton d'entrée fait au moins un octet du corps) :
    appel au modèle : dépense + (octets du corps + 1024) × prix d'entrée + max_tokens × prix de sortie ≤ plafond,
                      `max_tokens` = min(`--max-sortie-jetons`, ce que le reste paie), refus sous `--sortie-min-jetons` ;
    recherches d'un tour (k appels) : dépense + k × prix de recherche + pire cas d'un appel final (corps actuel
                      + k × `--marge-resultat-octets`, `--sortie-min-jetons` en sortie) ≤ plafond, sinon aucune n'est faite.
Coût rendu (borne haute) : Σ (`prompt_tokens` × entrée + `completion_tokens` × sortie) des appels au modèle, cache non
déduit, + nombre de recherches **envoyées** × prix de recherche (un échec est compté). Usage absent → pire cas de l'appel.

Codes : 0 conforme ; 2 réglage ou entrée refusés ; 3 relais ou amont (HTTP, connexion) ; 4 budget insuffisant avant envoi ;
5 réponse non conforme (vide, tronquée, modèle servi différent, usage absent, JSON illisible, boucle non close) ; 6 délai
dépassé ou interruption.

Usage : python3 -I -B commande_kimi_recherche_v1.py [--url-relais http://127.0.0.1:8789] [--modele kimi-k3.1-pro]
            [--prix-entree 2] [--prix-sortie 10] [--prix-recherche 0.005] [--max-tours 12] [--max-recherches 40]
            [--max-sortie-jetons 32768] [--sortie-min-jetons 4096] [--reasoning-effort high] [--delai-s 1500]
"""

import argparse
import json
import math
import signal
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

VERSION = "commande-kimi-recherche-v1"
ROLES = (None, "lecteur_sources")
PLANCHER = 1e-6
NOM_OUTIL = "web_search"
CHEMIN_FIBRES = "/v1/formulas/moonshot/web-search:latest/fibers"
CHEMIN_DECLARATION = "/v1/formulas/moonshot/web-search:latest/tools"
DECLARATION_DOC = {"type": "function", "function": {
    "name": "web_search", "description": "Search the web for information",
    "parameters": {"type": "object", "properties": {"query": {"description": "What to search for", "type": "string"}},
                   "required": ["query"]}}}
REFUS_AVANT_AMONT = (400, 402, 403, 404, 411, 413, 429)  # refus du relais (corps à clé « relais ») : rien n'est parti


class Sortie(Exception):
    def __init__(self, code, **champs):
        super().__init__(code)
        self.code, self.champs = code, champs


def lire_arguments(argv):
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    a.add_argument("--url-relais", default="http://127.0.0.1:8789")
    a.add_argument("--modele", default="kimi-k3.1-pro")
    a.add_argument("--prix-entree", type=float, default=2.0)
    a.add_argument("--prix-sortie", type=float, default=10.0)
    a.add_argument("--prix-recherche", type=float, default=0.005)
    a.add_argument("--max-tours", type=int, default=12)
    a.add_argument("--max-recherches", type=int, default=40)
    a.add_argument("--max-sortie-jetons", type=int, default=32768)
    a.add_argument("--sortie-min-jetons", type=int, default=4096)
    a.add_argument("--marge-resultat-octets", type=int, default=60000)
    a.add_argument("--reasoning-effort", default=None, choices=(None, "low", "high", "max"))
    a.add_argument("--declaration", default="relais", choices=("relais", "doc"))
    a.add_argument("--delai-s", type=float, default=1500.0)
    return a.parse_args(argv)


def verifier_url(url):
    u = urllib.parse.urlsplit(url)
    if u.scheme != "http" or u.hostname not in ("127.0.0.1", "localhost") or u.path not in ("", "/"):
        raise ValueError("--url-relais : http://127.0.0.1:PORT seulement (le relais local tient la clé)")
    return url.rstrip("/")


def entier(x):
    return isinstance(x, int) and not isinstance(x, bool) and x >= 0


class Boucle:
    def __init__(self, args, plafond, consigne):
        self.a, self.plafond = args, plafond
        self.base = verifier_url(args.url_relais)
        self.ouvreur = urllib.request.build_opener(urllib.request.ProxyHandler({}))  # jamais de mandataire
        self.messages = [{"role": "user", "content": consigne}]
        self.cout_modele, self.cout_recherches, self.en_vol = 0.0, 0.0, 0.0
        self.tours, self.recherches, self.non_executees = 0, 0, 0
        self.requetes, self.servi, self.fin, self.usages = [], None, None, []

    # --- comptes ---
    def depense(self):
        return self.cout_modele + self.cout_recherches

    def diag(self):
        return {"tours": self.tours, "recherches": self.recherches, "recherches_non_executees": self.non_executees,
                "requetes_recherche": self.requetes, "cout_modele_usd": round(self.cout_modele, 6),
                "cout_recherches_usd": round(self.cout_recherches, 6), "modele_demande": self.a.modele,
                "modele_servi": self.servi, "finish_reason": self.fin, "usages": self.usages}

    def pire_appel(self, octets, n):
        return (octets + 1024) * self.a.prix_entree / 1e6 + n * self.a.prix_sortie / 1e6

    # --- transport ---
    def envoyer(self, methode, chemin, objet=None):
        """(statut, objet JSON ou None, envoyé) ; une erreur HTTP du relais avant l'amont n'est pas « envoyée »."""
        corps = None if objet is None else json.dumps(objet, ensure_ascii=False).encode("utf-8")
        en_tetes = {"Accept": "application/json"}
        if corps is not None:
            en_tetes.update({"Content-Type": "application/json", "Content-Length": str(len(corps))})
        requete = urllib.request.Request(self.base + chemin, data=corps, method=methode, headers=en_tetes)
        try:
            with self.ouvreur.open(requete, timeout=self.a.delai_s) as rep:
                brut, statut = rep.read(), rep.status
        except urllib.error.HTTPError as e:
            brut = e.read()
            try:
                du_relais = isinstance(json.loads(brut), dict) and "relais" in json.loads(brut)
            except ValueError:
                du_relais = False
            # refus du relais (corps à clé « relais », statut de refus) : rien n'est parti ; sinon l'amont a pu servir
            avant_amont = du_relais and e.code in REFUS_AVANT_AMONT
            return e.code, {"motif": brut[:300].decode("utf-8", "replace")}, not avant_amont
        except urllib.error.URLError as e:
            if isinstance(e.reason, ConnectionRefusedError):
                raise Sortie(3, erreur="relais injoignable (connexion refusée)", envoye=False)
            raise Sortie(3, erreur="URLError : " + str(e.reason)[:200], envoye=True, en_vol=True)
        except TimeoutError as e:
            raise Sortie(6, erreur="délai dépassé : " + str(e)[:200], envoye=True, en_vol=True)
        except OSError as e:
            raise Sortie(3, erreur=type(e).__name__ + " : " + str(e)[:200], envoye=True, en_vol=True)
        try:
            return statut, json.loads(brut), True
        except ValueError:
            return statut, None, True

    # --- étapes ---
    def declaration(self):
        if self.a.declaration == "doc":
            return DECLARATION_DOC
        statut, objet, _ = self.envoyer("GET", CHEMIN_DECLARATION)
        outils = objet.get("tools") if (statut == 200 and isinstance(objet, dict)) else None
        if not (isinstance(outils, list) and len(outils) == 1 and isinstance(outils[0], dict)
                and (outils[0].get("function") or {}).get("name") == NOM_OUTIL):
            raise Sortie(3, erreur=f"déclaration de web_search illisible par le relais (HTTP {statut})", envoye=False)
        return outils[0]

    def corps_appel(self, outil, choix):
        """Corps et max_tokens payables par le reste du plafond (point fixe : le corps grandit avec le chiffre)."""
        reste = self.plafond - self.depense()
        n = self.a.max_sortie_jetons
        for _ in range(4):
            corps = {"model": self.a.modele, "messages": self.messages, "max_tokens": n, "tools": [outil],
                     "tool_choice": choix}
            if self.a.reasoning_effort:
                corps["reasoning_effort"] = self.a.reasoning_effort
            octets = len(json.dumps(corps, ensure_ascii=False).encode("utf-8"))
            libre = reste - (octets + 1024) * self.a.prix_entree / 1e6
            n2 = min(self.a.max_sortie_jetons, int(libre * 1e6 / self.a.prix_sortie)) if libre > 0 else 0
            if n2 < self.a.sortie_min_jetons:
                raise Sortie(4, erreur=f"budget insuffisant pour l'appel {self.tours + 1} (corps {octets} octets, "
                                       f"reste {reste:.6f} USD)", envoye=self.tours > 0)
            if n2 == n:
                return corps, n, octets
            n = n2
        corps["max_tokens"] = n
        octets = len(json.dumps(corps, ensure_ascii=False).encode("utf-8"))
        if self.depense() + self.pire_appel(octets, n) > self.plafond + 1e-12:
            raise Sortie(4, erreur="budget insuffisant après point fixe", envoye=self.tours > 0)
        return corps, n, octets

    def appeler_modele(self, outil, choix):
        corps, n, octets = self.corps_appel(outil, choix)
        pire = self.pire_appel(octets, n)
        self.en_vol = pire
        self.tours += 1
        statut, objet, envoye = self.envoyer("POST", "/v1/chat/completions", corps)
        self.en_vol = 0.0
        if statut != 200:
            if envoye:
                self.cout_modele += pire
            raise Sortie(5 if statut == 502 else 3, erreur=f"HTTP {statut} : {(objet or {}).get('motif', '')}",
                         envoye=envoye)
        try:
            choix0 = objet["choices"][0]
            message = choix0["message"]
            if not isinstance(message, dict):
                raise TypeError
        except (TypeError, KeyError, IndexError):
            self.cout_modele += pire
            raise Sortie(5, erreur="réponse illisible", envoye=True)
        self.servi, self.fin = objet.get("model"), choix0.get("finish_reason")
        usage = objet.get("usage") if isinstance(objet.get("usage"), dict) else {}
        p, c = usage.get("prompt_tokens"), usage.get("completion_tokens")
        if entier(p) and entier(c):
            self.cout_modele += (p * self.a.prix_entree + c * self.a.prix_sortie) / 1e6
            self.usages.append({"prompt_tokens": p, "completion_tokens": c})
        else:
            self.cout_modele += pire
            raise Sortie(5, erreur="usage absent", envoye=True)
        if self.servi != self.a.modele:
            raise Sortie(5, erreur=f"modèle servi {self.servi!r} ≠ {self.a.modele!r}", envoye=True)
        if self.fin == "length":
            raise Sortie(5, erreur="réponse tronquée (finish_reason length)", envoye=True)
        return message, octets

    def rechercher(self, appel):
        """Contenu du message `tool` pour un appel exécuté ; compte la recherche dès qu'elle est envoyée."""
        f = appel["function"]
        self.en_vol = self.a.prix_recherche
        statut, objet, envoye = self.envoyer("POST", CHEMIN_FIBRES, {"name": f["name"], "arguments": f["arguments"]})
        self.en_vol = 0.0
        if envoye:
            self.recherches += 1
            self.cout_recherches += self.a.prix_recherche
            self.requetes.append(f["arguments"][:500])
        if statut != 200 or not isinstance(objet, dict):
            return None, f"Recherche non aboutie (HTTP {statut})."
        contexte = objet.get("context") if isinstance(objet.get("context"), dict) else {}
        if objet.get("status") == "succeeded":
            sortie = contexte.get("output") or contexte.get("encrypted_output")
            if isinstance(sortie, str) and sortie:
                return sortie, None
        erreur = objet.get("error") or contexte.get("error") or "erreur inconnue"
        return None, "Error: " + str(erreur)[:300]

    def executer(self):
        outil = self.declaration()
        forcer_fin = False
        while True:
            dernier = self.tours + 1 >= self.a.max_tours
            choix = "none" if (forcer_fin or dernier) else "auto"
            message, octets = self.appeler_modele(outil, choix)
            appels = message.get("tool_calls") or []
            if not appels:
                texte = message.get("content") or ""
                if not texte.strip():
                    raise Sortie(5, erreur="réponse vide", envoye=True)
                return texte
            if choix == "none":
                raise Sortie(5, erreur="boucle non close : tool_calls malgré tool_choice none (borne de tours ou de "
                                       "recherches atteinte)", envoye=True)
            if not all(isinstance(t, dict) and isinstance(t.get("id"), str) and isinstance(t.get("function"), dict)
                       and isinstance(t["function"].get("arguments"), str) for t in appels):
                raise Sortie(5, erreur="tool_calls mal formés", envoye=True)
            self.messages.append({k: v for k, v in message.items() if v is not None})  # message entier (K3.1 Pro)
            budget_ok = (self.depense() + len(appels) * self.a.prix_recherche
                         + self.pire_appel(octets + len(appels) * self.a.marge_resultat_octets, self.a.sortie_min_jetons)
                         <= self.plafond + 1e-12)
            for appel in appels:
                motif = None
                if appel["function"].get("name") != NOM_OUTIL:
                    motif = "outil inconnu : seule web_search existe"
                elif self.recherches >= self.a.max_recherches:
                    motif = "borne de recherches atteinte"
                elif not budget_ok:
                    motif = "budget insuffisant pour rechercher et conclure"
                contenu = None
                if motif is None:
                    contenu, motif = self.rechercher(appel)
                if contenu is None:
                    self.non_executees += 1
                    forcer_fin = forcer_fin or motif.startswith(("borne", "budget", "Recherche non aboutie"))
                    contenu = f"Recherche non exécutée ({motif}). Réponds avec ce que tu as déjà lu et dis ce qui manque."
                self.messages.append({"role": "tool", "tool_call_id": appel["id"], "content": contenu})


def rendre(code, texte="", cout=PLANCHER, **diag):
    cout = cout if (isinstance(cout, (int, float)) and math.isfinite(cout) and cout > 0) else PLANCHER
    print(json.dumps({"texte": texte, "cout_usd": round(float(cout), 6), "version": VERSION, **diag}, ensure_ascii=False))
    sys.stdout.flush()
    sys.exit(code)


def main(argv, environ, entree):
    try:
        args = lire_arguments(argv)
        verifier_url(args.url_relais)
        plafond = float(environ.get("PLAFOND_SESSION_USD", "nan"))
        if not (math.isfinite(plafond) and plafond > 0):
            raise ValueError("PLAFOND_SESSION_USD absent ou invalide")
        if environ.get("ROLE_POLE") not in ROLES:
            raise ValueError(f"ROLE_POLE {environ.get('ROLE_POLE')!r} refusé (permis : lecteur_sources ou absent)")
        demande = environ.get("MODELE_DEMANDE_POLE")
        if demande is not None and demande != args.modele:
            raise ValueError(f"MODELE_DEMANDE_POLE {demande!r} ≠ --modele {args.modele!r}")
        for nom in ("prix_entree", "prix_sortie", "prix_recherche"):
            v = getattr(args, nom)
            if not (math.isfinite(v) and v > 0):
                raise ValueError(f"--{nom.replace('_', '-')} : strictement positif requis")
        if args.max_tours < 1 or args.max_recherches < 0 or args.sortie_min_jetons < 1:
            raise ValueError("--max-tours ≥ 1, --max-recherches ≥ 0, --sortie-min-jetons ≥ 1 requis")
        consigne = entree.read()
        if not consigne.strip():
            raise ValueError("consigne vide")
    except (ValueError, SystemExit) as e:
        rendre(2, erreur=str(e)[:300], envoye=False)
    boucle = Boucle(args, plafond, consigne)
    debut = time.time()

    def interrompu(signum, _frame):
        rendre(6, cout=boucle.depense() + boucle.en_vol, erreur=f"signal {signum}", envoye=True, **boucle.diag())
    signal.signal(signal.SIGTERM, interrompu)
    signal.signal(signal.SIGINT, interrompu)
    try:
        texte = boucle.executer()
    except Sortie as s:
        en_vol = s.champs.pop("en_vol", False)
        cout = boucle.depense() + (boucle.en_vol if en_vol else 0.0)
        rendre(s.code, cout=cout, duree_s=round(time.time() - debut, 3), **s.champs, **boucle.diag())
    rendre(0, texte=texte, cout=boucle.depense(), envoye=True, duree_s=round(time.time() - debut, 3), **boucle.diag())


if __name__ == "__main__":
    main(sys.argv[1:], dict(__import__("os").environ), sys.stdin)
