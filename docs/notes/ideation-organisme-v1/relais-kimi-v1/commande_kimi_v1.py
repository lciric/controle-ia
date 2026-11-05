#!/usr/bin/env python3
"""Commande externe de Kimi (kimi-k3.1-pro) pour le mode « juges seulement » de l'orchestrateur du pôle — version 1.

Lignée session-depot, 30 octobre 2026. Demande de Lazar : « demande à Kimi de juger les fiches de la course 1 ». Même contrat
que la commande d'Argon (`/opt/argon/commande_argon_v2.py`) pour `AdaptateurCommandeExterne` (`pole/adaptateurs.py`, v52) :

- la consigne arrive sur l'**entrée standard** (UTF-8) et part telle quelle, en un seul message utilisateur ;
- environnement minimal : plafond de la session dans `PLAFOND_SESSION_USD`, rôle dans `ROLE_POLE` (`juge_ideation`
  seulement ici), modèle demandé par le noyau dans `MODELE_DEMANDE_POLE` (lu : il doit être `--modele`, sinon code 2 ;
  d'où `--commande-externe-lit-modele` au lanceur) ;
- la **dernière ligne** de la sortie standard est toujours un objet JSON `{"texte", "cout_usd", "modele_servi", …}`, coût
  fini et strictement positif, aussi sur un échec.

**Aucune clé ici.** La commande parle au relais Kimi local (`relais_kimi_v2.py`, boucle locale seulement, sans mandataire),
qui tient la clé, la liste des modèles permis, la barrière du modèle servi (502 sur écart) et son propre plafond.

Garde avant envoi (même hypothèse que le relais : un jeton d'entrée fait au moins un octet du corps) :
    pire cas = (octets du corps + 1024) × prix d'entrée + max_tokens × prix de sortie ≤ PLAFOND_SESSION_USD
`max_tokens` = min(`--max-sortie-jetons`, ce que le reste du plafond paie) ; sous `--sortie-min-jetons` : refus sans envoi
(code 4). Les jetons de raisonnement de Kimi sont dans `completion_tokens` (convention compatible OpenAI, lue à l'essai réel
du 30 octobre : `completion_tokens_details.reasoning_tokens`), donc bornés par `max_tokens`.

Coût rendu : `prompt_tokens` × prix d'entrée + `completion_tokens` × prix de sortie (le cache n'est pas déduit : borne
haute) ; usage absent après envoi → pire cas ; rien envoyé ou refus du relais avant l'amont (4xx) → plancher 1e-6.

Codes : 0 conforme ; 2 réglage ou entrée refusés ; 3 relais ou amont (HTTP, connexion) ; 4 pire cas au-dessus du plafond ;
5 réponse non conforme (vide, tronquée `finish_reason == "length"`, modèle servi différent, usage absent, JSON illisible) ;
6 délai dépassé ou interruption.

Usage : python3 -I -B commande_kimi_v1.py [--url-relais http://127.0.0.1:8789] [--modele kimi-k3.1-pro]
            [--prix-entree 2] [--prix-sortie 10] [--max-sortie-jetons 32768] [--sortie-min-jetons 4096] [--delai-s 1500]
"""

import argparse
import json
import math
import signal
import sys
import urllib.error
import urllib.parse
import urllib.request

VERSION = "commande-kimi-v1"
ROLES = ("juge_ideation",)
PLANCHER = 1e-6


def rendre(code, texte="", cout=PLANCHER, **diag):
    cout = cout if (isinstance(cout, (int, float)) and math.isfinite(cout) and cout > 0) else PLANCHER
    print(json.dumps({"texte": texte, "cout_usd": round(float(cout), 6), "version": VERSION, **diag}, ensure_ascii=False))
    sys.stdout.flush()
    sys.exit(code)


def lire_arguments(argv):
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    a.add_argument("--url-relais", default="http://127.0.0.1:8789")
    a.add_argument("--modele", default="kimi-k3.1-pro")
    a.add_argument("--prix-entree", type=float, default=2.0)
    a.add_argument("--prix-sortie", type=float, default=10.0)
    a.add_argument("--max-sortie-jetons", type=int, default=32768)
    a.add_argument("--sortie-min-jetons", type=int, default=4096)
    a.add_argument("--delai-s", type=float, default=1500.0)
    return a.parse_args(argv)


def verifier_url(url):
    u = urllib.parse.urlsplit(url)
    if u.scheme != "http" or u.hostname not in ("127.0.0.1", "localhost") or u.path not in ("", "/"):
        raise ValueError("--url-relais : http://127.0.0.1:PORT seulement (le relais local tient la clé)")
    return url.rstrip("/") + "/v1/chat/completions"


def max_tokens_permis(octets, plafond, pe, ps, maxi, mini):
    """Sortie maximale que le plafond paie après le pire cas d'entrée ; None si sous le minimum."""
    reste = plafond - (octets + 1024) * pe / 1e6
    n = min(maxi, int(reste * 1e6 / ps)) if reste > 0 else 0
    return n if n >= mini else None


def cout_usage(usage, pe, ps):
    p, c = usage.get("prompt_tokens"), usage.get("completion_tokens")
    if not all(isinstance(x, int) and not isinstance(x, bool) and x >= 0 for x in (p, c)):
        return None
    return (p * pe + c * ps) / 1e6


def main(argv, environ, entree):
    try:
        args = lire_arguments(argv)
        cible = verifier_url(args.url_relais)
        plafond = float(environ.get("PLAFOND_SESSION_USD", "nan"))
        if not (math.isfinite(plafond) and plafond > 0):
            raise ValueError("PLAFOND_SESSION_USD absent ou invalide")
        role = environ.get("ROLE_POLE")
        if role not in ROLES:
            raise ValueError(f"ROLE_POLE {role!r} refusé (permis : {ROLES})")
        demande = environ.get("MODELE_DEMANDE_POLE")
        if demande is not None and demande != args.modele:
            raise ValueError(f"MODELE_DEMANDE_POLE {demande!r} ≠ --modele {args.modele!r}")
        consigne = entree.read()
        if not consigne.strip():
            raise ValueError("consigne vide")
    except (ValueError, SystemExit) as e:
        rendre(2, erreur=str(e)[:300], envoye=False)
    n = None
    corps = None
    for _ in range(3):  # le corps grandit avec le chiffre de max_tokens : point fixe en quelques tours
        corps = json.dumps({"model": args.modele, "messages": [{"role": "user", "content": consigne}],
                            "max_tokens": n or args.max_sortie_jetons}, ensure_ascii=False).encode("utf-8")
        n2 = max_tokens_permis(len(corps), plafond, args.prix_entree, args.prix_sortie, args.max_sortie_jetons,
                               args.sortie_min_jetons)
        if n2 is None:
            rendre(4, erreur=f"pire cas au-dessus du plafond {plafond} USD (corps {len(corps)} octets)", envoye=False)
        if n2 == n:
            break
        n = n2
    corps = json.dumps({"model": args.modele, "messages": [{"role": "user", "content": consigne}], "max_tokens": n},
                       ensure_ascii=False).encode("utf-8")
    pire = (len(corps) + 1024) * args.prix_entree / 1e6 + n * args.prix_sortie / 1e6
    if pire > plafond + 1e-12:
        rendre(4, erreur="pire cas au-dessus du plafond après point fixe", envoye=False)
    diag = {"max_tokens": n, "octets_corps": len(corps), "pire_cas_usd": round(pire, 6), "modele_demande": args.modele}

    def interrompu(signum, _frame):
        rendre(6, cout=pire, erreur=f"signal {signum}", envoye=True, cout_origine="pire_cas", **diag)
    signal.signal(signal.SIGTERM, interrompu)
    signal.signal(signal.SIGINT, interrompu)

    ouvreur = urllib.request.build_opener(urllib.request.ProxyHandler({}))  # boucle locale : jamais de mandataire
    requete = urllib.request.Request(cible, data=corps, method="POST",
                                     headers={"Content-Type": "application/json", "Content-Length": str(len(corps))})
    try:
        with ouvreur.open(requete, timeout=args.delai_s) as rep:
            brut = rep.read()
    except urllib.error.HTTPError as e:
        motif = e.read()[:300].decode("utf-8", "replace")
        avant_amont = e.code in (400, 402, 403, 411, 413, 429)  # refus du relais sans rien envoyer à l'amont
        rendre(3 if e.code != 502 else 5, cout=PLANCHER if avant_amont else pire, erreur=f"HTTP {e.code} : {motif}",
               envoye=not avant_amont, cout_origine="plancher" if avant_amont else "pire_cas", **diag)
    except urllib.error.URLError as e:
        if isinstance(e.reason, ConnectionRefusedError):  # relais absent : rien n'est parti
            rendre(3, erreur="relais injoignable (connexion refusée)", envoye=False, cout_origine="plancher", **diag)
        rendre(3, cout=pire, erreur="URLError : " + str(e.reason)[:200], envoye=True, cout_origine="pire_cas", **diag)
    except (TimeoutError, OSError) as e:
        rendre(6 if isinstance(e, TimeoutError) else 3, cout=pire, erreur=type(e).__name__ + " : " + str(e)[:200],
               envoye=True, cout_origine="pire_cas", **diag)
    try:
        objet = json.loads(brut)
        choix = objet["choices"][0]
        texte = choix["message"].get("content") or ""
        fin = choix.get("finish_reason")
    except (ValueError, KeyError, IndexError, TypeError, AttributeError):
        rendre(5, cout=pire, erreur="réponse illisible", envoye=True, cout_origine="pire_cas", **diag)
    servi = objet.get("model")
    cout = cout_usage(objet.get("usage") or {}, args.prix_entree, args.prix_sortie)
    origine = "usage"
    if cout is None:
        cout, origine = pire, "pire_cas"
    diag.update(modele_servi=servi, finish_reason=fin, usage={k: v for k, v in (objet.get("usage") or {}).items()
                                                             if isinstance(v, (int, float))}, cout_origine=origine)
    if servi != args.modele:
        rendre(5, cout=cout, erreur=f"modèle servi {servi!r} ≠ {args.modele!r}", envoye=True, **diag)
    if origine != "usage":
        rendre(5, cout=cout, erreur="usage absent", envoye=True, **diag)
    if fin == "length":
        rendre(5, cout=cout, erreur="réponse tronquée (finish_reason length)", envoye=True, **diag)
    if not texte.strip():
        rendre(5, cout=cout, erreur="réponse vide", envoye=True, **diag)
    rendre(0, texte=texte, cout=cout, envoye=True, **diag)


if __name__ == "__main__":
    main(sys.argv[1:], dict(__import__("os").environ), sys.stdin)
