#!/usr/bin/env python3
"""Commande externe d'Argon (gemini-4-argon) pour la course d'idéation du pôle — **appel nu**, version 1.

Lignée session-depot, 29 octobre 2026. Écrite pour le contrat de `AdaptateurCommandeExterne` (`pole/adaptateurs.py`,
orchestrateur du pôle v7, v43) :

- la consigne arrive sur l'**entrée standard** (UTF-8) ; elle est envoyée telle quelle, en un seul message utilisateur ;
- l'environnement est minimal : le plafond de la session est lu dans `PLAFOND_SESSION_USD`, le rôle dans `ROLE_POLE`
  (`proposeur_ideation` ou `juge_ideation`) ; la clé est lue dans **`GEMINI_API_KEY`** (nom fixe), jamais en argument,
  jamais dans un fichier lu par ce script ; elle n'est jamais écrite (sortie, erreurs, journal) ;
- la **dernière ligne** de la sortie standard est **toujours** un objet JSON `{"texte": …, "cout_usd": …}` (plus des
  champs de diagnostic que le noyau ignore), avec un coût **fini et strictement positif**, aussi sur un échec.

Appel nu : une requête `generateContent` de l'interface de génération de contenu de Google, **aucun outil ni fonction
déclarés**, aucune consigne système, aucune reprise automatique (un échec est nommé et rendu ; la relance appartient au
noyau et à ses tentatives). Le mandataire réseau est celui de l'environnement (`HTTPS_PROXY`, `SSL_CERT_FILE`) ; une
adresse en `http://` n'est permise que vers la boucle locale (essais), et alors sans mandataire.

Barème (dollars par million de jetons) :
- entrée **8,3** : borne lue par Lazar sur la console de facturation de la clé (R-718 ; « ≤ 8,3 ») ;
- sortie **41,5 : SUPPOSÉ**, non lu — rapport 5 entre sortie et entrée, la convention du barème du code (`BAREME_INCONNU`,
  50 / 10, `pole/relais_reel.py`), appliqué à 8,3 ; sources tierces non opposables : 10 (puis 20 après le 30 novembre)
  pour 2 (puis 4) en entrée, soit le même rapport 5. Les deux sont réglables (`--prix-entree`, `--prix-sortie`) et
  consignés au manifeste par la ligne de commande.

Garde du pire cas, **avant tout envoi** : entrée estimée = caractères / 4 (`--caracteres-par-jeton`), ou le compte exact de
l'interface `countTokens` (gratuit) s'il est plus grand (`--compter-jetons`) ; sortie maximale demandée =
min(`--max-sortie-jetons`, ce que le reste du plafond paie au prix de sortie) ; si cette sortie est sous
`--sortie-min-jetons`, autrement dit si entrée + sortie minimale dépassent le plafond, **refus sans envoi** (code 4).
Ainsi le pire cas facturable (entrée estimée + `maxOutputTokens` demandé) ne dépasse jamais `PLAFOND_SESSION_USD` (la
sortie est bornée : réponse à CL43-02, « vérifier que la vraie commande s'arrête au plafond »), à l'erreur d'estimation de
l'entrée près (d'où `--compter-jetons`).

Coût rendu : sur l'usage rendu (`usageMetadata` : `promptTokenCount` au prix d'entrée ; `candidatesTokenCount` +
`thoughtsTokenCount` au prix de sortie) ; usage absent après un envoi → **pire cas** compté (prudent) ; rien envoyé, ou
requête refusée par l'interface avant génération (HTTP 4xx) → coût plancher 1e-6 (le contrat interdit 0 ; `envoye` et
`cout_origine` le disent) ; erreur 5xx, connexion coupée après envoi, délai → pire cas.

Codes de sortie : 0 réponse conforme ; 2 réglage ou entrée refusés (rien envoyé) ; 3 interface (HTTP, connexion) ;
4 pire cas au-dessus du plafond (rien envoyé) ; 5 réponse non conforme (vide, usage absent, tronquée, bloquée, modèle servi
différent, JSON illisible) ; 6 délai dépassé ou interruption (SIGTERM, SIGINT).

Usage (sous l'utilisateur distinct d'Argon, la clé posée par l'enveloppe de changement d'utilisateur) :
    python3 -I -B commande_argon_v1.py [--modele gemini-4-argon] [--url-base URL] [--prix-entree 8.3] [--prix-sortie 41.5]
        [--max-sortie-jetons 65536] [--sortie-min-jetons 4096] [--compter-jetons] [--delai-s 1500]
"""

import argparse
import json
import math
import os
import signal
import socket
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request

VERSION = "commande-argon-v1"
MODELE_DEFAUT = "gemini-4-argon"
URL_BASE_DEFAUT = "https://generativelanguage.googleapis.com/v1beta"
VARIABLE_CLE = "GEMINI_API_KEY"
PRIX_ENTREE_DEFAUT = 8.3   # USD par million de jetons d'entrée : borne lue par Lazar (R-718)
PRIX_SORTIE_DEFAUT = 41.5  # SUPPOSÉ : rapport 5 du barème du code, non lu sur la console
CARACTERES_PAR_JETON_DEFAUT = 4.0
MAX_SORTIE_JETONS_DEFAUT = 65536
SORTIE_MIN_JETONS_DEFAUT = 4096
DELAI_DEFAUT_S = 1500.0    # sous le délai du noyau (1800 s) et sous l'arrêt dur de l'enveloppe (timeout 1700 s)
COUT_PLANCHER_USD = 1e-6   # le contrat exige un coût > 0 ; rien n'a été facturé
ROLES = ("proposeur_ideation", "juge_ideation")
HOTES_LOCAUX = {"127.0.0.1", "localhost", "::1"}
TAILLE_MAX_REPONSE = 50_000_000

OK, REGLAGE, INTERFACE, PIRE_CAS, NON_CONFORME, DELAI = 0, 2, 3, 4, 5, 6


class ErreurCommande(Exception):
    """Échec nommé : code de sortie, et ce qui a été envoyé ou non (pour le coût)."""

    def __init__(self, code, message, envoye=False, cout_origine="plancher"):
        super().__init__(message)
        self.code = code
        self.envoye = envoye
        self.cout_origine = cout_origine  # « plancher », « pire_cas » ou « usage »


class Interruption(Exception):
    """Délai global dépassé ou signal reçu."""


def masquer(texte, cle):
    """Ne laisse jamais passer la clé dans un message."""
    texte = str(texte)
    return texte.replace(cle, "[clé]") if cle else texte


def nombre_fini_positif(nom, valeur):
    try:
        v = float(valeur)
    except (TypeError, ValueError):
        raise ErreurCommande(REGLAGE, f"{nom} : nombre attendu (reçu {valeur!r})")
    if not math.isfinite(v) or v <= 0:
        raise ErreurCommande(REGLAGE, f"{nom} : réel fini strictement positif attendu (reçu {valeur!r})")
    return v


def valider_url_base(url):
    p = urllib.parse.urlparse(url)
    if p.scheme == "https" and p.hostname:
        return url.rstrip("/"), False
    if p.scheme == "http" and p.hostname in HOTES_LOCAUX:
        return url.rstrip("/"), True
    raise ErreurCommande(REGLAGE, f"--url-base : https, ou http vers la boucle locale seulement (reçu {url!r})")


def ouvreur(local):
    """Boucle locale : aucun mandataire. Sinon : mandataire et certificats de l'environnement."""
    if local:
        return urllib.request.build_opener(urllib.request.ProxyHandler({}))
    ca = os.environ.get("SSL_CERT_FILE")
    contexte = ssl.create_default_context(cafile=ca) if ca else ssl.create_default_context()
    return urllib.request.build_opener(urllib.request.HTTPSHandler(context=contexte))


def poster(ouv, url, cle, corps, delai_s):
    """POST JSON ; rend l'objet JSON. Lève HTTPError, URLError, OSError, ValueError."""
    requete = urllib.request.Request(url, data=json.dumps(corps, ensure_ascii=False).encode("utf-8"), method="POST",
                                     headers={"Content-Type": "application/json", "x-goog-api-key": cle})
    with ouv.open(requete, timeout=delai_s) as r:
        brut = r.read(TAILLE_MAX_REPONSE + 1)
    if len(brut) > TAILLE_MAX_REPONSE:
        raise ValueError("réponse trop longue")
    return json.loads(brut.decode("utf-8"))


def cout_usage(usage, prix_entree, prix_sortie):
    """(coût, détail) depuis `usageMetadata` ; lève ErreurCommande si l'usage est absent ou mal formé."""
    if not isinstance(usage, dict):
        raise ErreurCommande(NON_CONFORME, "usage absent de la réponse (usageMetadata) : pire cas compté",
                             envoye=True, cout_origine="pire_cas")
    def entier(nom, requis):
        v = usage.get(nom)
        if v is None and not requis:
            return 0
        if isinstance(v, bool) or not isinstance(v, int) or v < 0:
            raise ErreurCommande(NON_CONFORME, f"usage mal formé ({nom} = {v!r}) : pire cas compté",
                                 envoye=True, cout_origine="pire_cas")
        return v
    entree = entier("promptTokenCount", True)
    sortie = entier("candidatesTokenCount", False) + entier("thoughtsTokenCount", False)
    cout = entree * prix_entree / 1e6 + sortie * prix_sortie / 1e6
    return cout, {"entree": entree, "sortie": sortie, "brut": {k: usage[k] for k in sorted(usage)
                                                               if isinstance(usage[k], (int, float))}}


def modele_conforme(demande, servi):
    return isinstance(servi, str) and (servi == demande or servi.startswith(demande + "-")
                                       or servi == "models/" + demande)


def lire_reponse(rep, modele):
    """(texte, fin, modèle servi) d'une réponse conforme ; lève ErreurCommande (code 5) sinon. L'usage est lu à part."""
    if not isinstance(rep, dict):
        raise ErreurCommande(NON_CONFORME, "réponse non JSON objet", envoye=True, cout_origine="pire_cas")
    bloque = (rep.get("promptFeedback") or {}).get("blockReason")
    if bloque:
        raise ErreurCommande(NON_CONFORME, f"consigne bloquée par l'interface ({bloque})", envoye=True, cout_origine="usage")
    servi = rep.get("modelVersion")
    if not modele_conforme(modele, servi):
        raise ErreurCommande(NON_CONFORME, f"modèle servi {servi!r} ≠ modèle demandé {modele!r} (aucun changement de "
                             "modèle sans GO)", envoye=True, cout_origine="usage")
    candidats = rep.get("candidates") or []
    if not candidats:
        raise ErreurCommande(NON_CONFORME, "aucun candidat dans la réponse (réponse vide)", envoye=True, cout_origine="usage")
    c = candidats[0]
    fin = c.get("finishReason")
    parts = (c.get("content") or {}).get("parts") or []
    if any(("functionCall" in p) or ("executableCode" in p) for p in parts if isinstance(p, dict)):
        raise ErreurCommande(NON_CONFORME, "appel d'outil dans la réponse alors qu'aucun outil n'est déclaré",
                             envoye=True, cout_origine="usage")
    texte = "".join(p.get("text", "") for p in parts if isinstance(p, dict) and not p.get("thought"))
    if fin == "MAX_TOKENS":
        raise ErreurCommande(NON_CONFORME, "sortie tronquée (MAX_TOKENS) : maxOutputTokens atteint", envoye=True,
                             cout_origine="usage")
    if fin != "STOP":
        raise ErreurCommande(NON_CONFORME, f"fin de génération {fin!r} (bloquée ou anormale)", envoye=True,
                             cout_origine="usage")
    if not texte.strip():
        raise ErreurCommande(NON_CONFORME, "réponse vide (texte vide, fin STOP)", envoye=True, cout_origine="usage")
    return texte, fin, servi


def analyseur():
    a = argparse.ArgumentParser(prog="commande_argon_v1", description="Appel nu à Argon (contrat du noyau v43).")
    a.add_argument("--modele", default=MODELE_DEFAUT)
    a.add_argument("--url-base", default=URL_BASE_DEFAUT)
    a.add_argument("--prix-entree", default=PRIX_ENTREE_DEFAUT, help="USD par million de jetons d'entrée (8,3 : Lazar)")
    a.add_argument("--prix-sortie", default=PRIX_SORTIE_DEFAUT, help="USD par million de jetons de sortie (41,5 : SUPPOSÉ)")
    a.add_argument("--caracteres-par-jeton", default=CARACTERES_PAR_JETON_DEFAUT)
    a.add_argument("--max-sortie-jetons", type=int, default=MAX_SORTIE_JETONS_DEFAUT)
    a.add_argument("--sortie-min-jetons", type=int, default=SORTIE_MIN_JETONS_DEFAUT)
    a.add_argument("--compter-jetons", action="store_true", help="compte exact de l'entrée par countTokens (gratuit)")
    a.add_argument("--delai-s", default=DELAI_DEFAUT_S, help="délai global de la commande, en secondes")
    return a


def executer(argv, entree_octets, environ):
    """Rend (code, objet de la dernière ligne, message d'erreur ou None). Ne lève jamais."""
    etat = {"envoye": False, "pire_cas_usd": None, "usage": None, "cle": None}
    diag = {"version": VERSION, "role": environ.get("ROLE_POLE"), "modele_demande": None, "modele_servi": None,
            "fin": None, "envoye": False, "cout_origine": None, "pire_cas_usd": None, "max_sortie_jetons": None,
            "entree_jetons_estimee": None, "entree_jetons_comptee": None, "usage": None, "erreur": None, "code": None}

    def ligne(code, texte, cout, origine, erreur=None):
        diag.update(texte=texte, cout_usd=float(cout), cout_origine=origine, envoye=etat["envoye"], code=code,
                    erreur=masquer(erreur, etat["cle"]) if erreur else None, pire_cas_usd=etat["pire_cas_usd"])
        objet = {"texte": diag.pop("texte"), "cout_usd": diag.pop("cout_usd")}
        objet.update(diag)
        return code, objet, objet["erreur"]

    def sur_signal(num, _cadre):
        raise Interruption(f"signal {num} reçu")

    precedents = {}
    try:
        try:
            args = analyseur().parse_args(argv)
        except SystemExit:
            raise ErreurCommande(REGLAGE, "arguments refusés (voir la sortie d'erreur)")
        diag["modele_demande"] = args.modele
        prix_e = nombre_fini_positif("--prix-entree", args.prix_entree)
        prix_s = nombre_fini_positif("--prix-sortie", args.prix_sortie)
        cpj = nombre_fini_positif("--caracteres-par-jeton", args.caracteres_par_jeton)
        delai = nombre_fini_positif("--delai-s", args.delai_s)
        if args.max_sortie_jetons < 1 or args.sortie_min_jetons < 1 or args.sortie_min_jetons > args.max_sortie_jetons:
            raise ErreurCommande(REGLAGE, "1 ≤ --sortie-min-jetons ≤ --max-sortie-jetons requis")
        url_base, local = valider_url_base(args.url_base)
        if "PLAFOND_SESSION_USD" not in environ:
            raise ErreurCommande(REGLAGE, "PLAFOND_SESSION_USD absent de l'environnement")
        plafond = nombre_fini_positif("PLAFOND_SESSION_USD", environ["PLAFOND_SESSION_USD"])
        role = environ.get("ROLE_POLE")
        if role not in ROLES:
            raise ErreurCommande(REGLAGE, f"ROLE_POLE ∉ {ROLES} (reçu {role!r})")
        cle = environ.get(VARIABLE_CLE) or ""
        etat["cle"] = cle or None
        if not cle.strip():
            raise ErreurCommande(REGLAGE, f"{VARIABLE_CLE} absente ou vide : l'enveloppe d'utilisateur distinct la pose")
        try:
            consigne = entree_octets.decode("utf-8")
        except UnicodeDecodeError:
            raise ErreurCommande(REGLAGE, "consigne : UTF-8 invalide sur l'entrée standard")
        if not consigne.strip():
            raise ErreurCommande(REGLAGE, "consigne vide sur l'entrée standard")

        for s in (signal.SIGALRM, signal.SIGTERM, signal.SIGINT):
            precedents[s] = signal.signal(s, sur_signal)
        signal.setitimer(signal.ITIMER_REAL, delai)

        ouv = ouvreur(local)
        contenus = [{"role": "user", "parts": [{"text": consigne}]}]
        estime = math.ceil(len(consigne) / cpj)
        diag["entree_jetons_estimee"] = estime
        entree_jetons = estime
        if args.compter_jetons:  # gratuit : aucune génération
            try:
                rep = poster(ouv, f"{url_base}/models/{args.modele}:countTokens", cle, {"contents": contenus}, delai)
            except urllib.error.HTTPError as e:
                raise ErreurCommande(INTERFACE, f"countTokens : HTTP {e.code} : "
                                     + e.read(300).decode("utf-8", "replace"))
            except (urllib.error.URLError, OSError, ValueError) as e:
                raise ErreurCommande(INTERFACE, f"countTokens : {type(e).__name__} : {e}")
            compte = rep.get("totalTokens") if isinstance(rep, dict) else None
            if isinstance(compte, bool) or not isinstance(compte, int) or compte <= 0:
                raise ErreurCommande(NON_CONFORME, f"countTokens : totalTokens absent ou invalide ({compte!r})")
            diag["entree_jetons_comptee"] = compte
            entree_jetons = max(estime, compte)
        cout_entree = entree_jetons * prix_e / 1e6
        place = math.floor((plafond - cout_entree) / (prix_s / 1e6)) if plafond > cout_entree else 0
        max_sortie = min(args.max_sortie_jetons, place)
        pire_min = cout_entree + args.sortie_min_jetons * prix_s / 1e6
        if max_sortie < args.sortie_min_jetons:
            raise ErreurCommande(PIRE_CAS, f"pire cas {pire_min:.4f} USD (entrée ≈ {entree_jetons} jetons à {prix_e:g}, "
                                 f"plus {args.sortie_min_jetons} jetons de sortie à {prix_s:g}) > plafond de session "
                                 f"{plafond:g} USD : rien envoyé")
        diag["max_sortie_jetons"] = max_sortie
        etat["pire_cas_usd"] = round(cout_entree + max_sortie * prix_s / 1e6, 6)

        corps = {"contents": contenus, "generationConfig": {"maxOutputTokens": max_sortie}}  # ni outil, ni fonction
        try:
            etat["envoye"] = True
            rep = poster(ouv, f"{url_base}/models/{args.modele}:generateContent", cle, corps, delai)
        except urllib.error.HTTPError as e:
            detail = e.read(300).decode("utf-8", "replace")
            if 400 <= e.code < 500:  # refusée avant génération : non facturée (SUPPOSÉ)
                raise ErreurCommande(INTERFACE, f"HTTP {e.code} : {detail}", envoye=True, cout_origine="plancher")
            raise ErreurCommande(INTERFACE, f"HTTP {e.code} : {detail}", envoye=True, cout_origine="pire_cas")
        except urllib.error.URLError as e:
            refus = isinstance(e.reason, (ConnectionRefusedError, socket.gaierror))
            if refus:
                etat["envoye"] = False
            raise ErreurCommande(INTERFACE, f"connexion : {type(e.reason).__name__} : {e.reason}", envoye=not refus,
                                 cout_origine="plancher" if refus else "pire_cas")
        except (OSError, ValueError) as e:  # délai de socket, coupure, JSON illisible : peut-être facturé
            raise ErreurCommande(INTERFACE if isinstance(e, OSError) else NON_CONFORME,
                                 f"{type(e).__name__} : {e}", envoye=True, cout_origine="pire_cas")
        signal.setitimer(signal.ITIMER_REAL, 0)
        usage = rep.get("usageMetadata") if isinstance(rep, dict) else None
        diag["modele_servi"] = rep.get("modelVersion") if isinstance(rep, dict) else None
        cout, detail_usage = cout_usage(usage, prix_e, prix_s)  # lève (pire cas) si l'usage manque
        diag["usage"] = detail_usage
        etat["usage"] = cout
        if not (math.isfinite(cout) and cout > 0):
            raise ErreurCommande(NON_CONFORME, f"coût calculé sur l'usage non strictement positif ({cout!r})",
                                 envoye=True, cout_origine="pire_cas")
        candidats = rep.get("candidates") or []
        diag["fin"] = candidats[0].get("finishReason") if candidats and isinstance(candidats[0], dict) else None
        texte, fin, servi = lire_reponse(rep, args.modele)
        return ligne(OK, texte, cout, "usage")
    except ErreurCommande as e:
        signal.setitimer(signal.ITIMER_REAL, 0)
        if e.cout_origine == "usage" and etat["usage"] is not None:
            cout, origine = etat["usage"], "usage"
        elif e.cout_origine in ("usage", "pire_cas") and e.envoye and etat["pire_cas_usd"]:
            cout, origine = etat["pire_cas_usd"], "pire_cas"
        else:
            cout, origine = COUT_PLANCHER_USD, "plancher"
        etat["envoye"] = etat["envoye"] and e.envoye
        return ligne(e.code, "", cout, origine, f"{type(e).__name__} : {e}")
    except Interruption as e:
        signal.setitimer(signal.ITIMER_REAL, 0)
        if etat["envoye"] and etat["pire_cas_usd"]:
            cout, origine = etat["pire_cas_usd"], "pire_cas"
        else:
            cout, origine = COUT_PLANCHER_USD, "plancher"
        return ligne(DELAI, "", cout, origine, f"délai ou interruption : {e}")
    except Exception as e:  # noqa: BLE001 — jamais de sortie sans ligne JSON ; nommé
        signal.setitimer(signal.ITIMER_REAL, 0)
        cout, origine = ((etat["pire_cas_usd"], "pire_cas") if etat["envoye"] and etat["pire_cas_usd"]
                         else (COUT_PLANCHER_USD, "plancher"))
        return ligne(NON_CONFORME if etat["envoye"] else REGLAGE, "", cout, origine,
                     f"erreur inattendue {type(e).__name__} : {e}")
    finally:
        for s, h in precedents.items():
            try:
                signal.signal(s, h)
            except (ValueError, OSError):
                pass


def principal(argv=None):
    code, objet, erreur = executer(sys.argv[1:] if argv is None else argv, sys.stdin.buffer.read(), os.environ)
    if erreur:
        print(f"commande_argon_v1 : {erreur}", file=sys.stderr)
    sys.stdout.write(json.dumps(objet, ensure_ascii=False) + "\n")
    sys.stdout.flush()
    return code


if __name__ == "__main__":
    sys.exit(principal())
