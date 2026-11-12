#!/usr/bin/env python3
"""Commande externe de Kimi (kimi-k3.1-pro) pour le tour fermé, étage 1 (orchestrateur v63) — version 4.

Version 4, rédigée le 3 novembre 2026 (sous-agent de session-depot) ; rien n'a été lancé par le rédacteur. **Version 4 =
`commande_kimi_v3.py` (sha256 `bb303f50…`, inchangée, R12) avec quatre changements, et seulement ceux-là** (contre-lecture
neuve de la v3, `contre-lecture-v3/contre-lecture-commandes-tour-ferme-v3-v1.md`, sha256 `6b4eac8b…` : bloquant B1 et
mineur 2 ; cause de refus demandée pour la version 64 de l'étage, qui lira un code 4 « rien envoyé » comme
« budget_depasse ») :

1. **Clé d'étape propre au fournisseur (bloquant B1 de la contre-lecture)** : la garde d'étape du registre partagé (garde 2)
   est jugée sous la clé `ETAPE_POLE` suivie de `/kimi` (fonction `etape_du_registre`) ; si `ETAPE_POLE` finit déjà par
   `/kimi`, rien n'est ajouté (idempotent : un lanceur peut déjà passer l'étape par fournisseur). Raison : le lanceur v63
   donne aux deux relais le même `ETAPE_POLE=tour_ferme_v63` avec des parts différentes (`PLAFOND_ETAPE_USD` 44.00 pour
   Kimi, 6.00 pour Argon) et le même registre ; en v3, la dépense de Kimi entrait dans la garde d'étape d'Argon, qui refusait
   le vérificateur dès ≈ 5,95 USD dépensés par Kimi dans l'étape (expérience E1 de la contre-lecture). Le champ
   `etape` de la dernière ligne garde la valeur reçue ; le champ neuf `etape_registre` porte la clé passée au registre
   (celle de sa ligne `debut`). La garde cumulée (`--plafond-cumule-usd`, les deux fournisseurs ensemble, même registre)
   ne change pas ; `registre_depense_cumulee_v1.py` est identique (sha256 `8ba92066…`).
2. **Cause de refus lisible par programme** : toute sortie en code 4, et elle seule, porte le champ `cause_refus`, l'une des
   six valeurs de `CAUSES_REFUS` : `plafond_session` (pire cas au-dessus du plafond de session, sortie minimale du rôle
   comprise), `garde_etape`, `garde_cumulee`, `registre_illisible`, `relais_plafond` (HTTP 402 du relais) ou
   `relais_max_appels` (HTTP 429 du relais). La garde d'étape et la garde cumulée lèvent la même exception (`PlafondCumule`) :
   la commande les distingue par le **préfixe du message** (`cause_du_registre`, `PREFIXE_GARDE_ETAPE`), sans toucher au
   registre. Choix et raison : (a) le message est rédigé par la décision elle-même, sous le verrou exclusif du registre
   (`reserver`, l. 133-144) ; une comparaison refaite par la commande avant `reserver` lirait le registre hors de ce verrou,
   que l'autre commande peut changer entre la lecture et la décision (les deux partagent le registre), au point de tomber sur
   une ligne en cours d'écriture : la cause rendue pourrait ne pas être la garde qui a refusé ; (b) le registre est gelé
   (copie identique, sha256 `8ba92066…`, contrôlée par la suite d'essais) : ses préfixes « garde d'étape ( » (l. 143) et
   « garde cumulée : » (l. 137) ne bougent pas, et les essais éprouvent les deux cas contre le vrai registre ; (c) la garde
   cumulée est jugée la première (l. 135-138) : si les deux refuseraient, la cause est `garde_cumulee`. Les deux autres refus
   `PlafondCumule` du registre, « plafond cumulé invalide » et « pire cas invalide » (l. 127-130), sont les contrôles
   d'entrée de la garde cumulée : `garde_cumulee`. `RegistreIllisible` et `OSError` (ligne illisible, dossier absent, fichier
   ou verrou illisible) : `registre_illisible`.
3. **Refus du relais 402 et 429 en code 4 — changement de comportement** (mineur 2 de la contre-lecture ; alignement sur la
   commande d'Argon) : un 402 (plafond du relais) ou un 429 (nombre d'appels du relais) rédigé **par le relais lui-même**
   sortait en code 3 ; il sort en code 4, `envoye: false`, coût plancher, `cause_refus` `relais_plafond` ou
   `relais_max_appels`. Le relais Kimi signe ses propres refus (objet JSON portant `relais` = `relais-kimi-…` :
   `relais_kimi_v3.py`, `_refuser` et refus de `Compteur.admettre`) mais transmet tels quels le statut et le corps d'une
   erreur de l'amont (en-tête de `relais_kimi_v3.py`, l. 30-31) : un 429 de Moonshot (limite de débit, ou compte sans
   crédit, comme le 2 novembre : addendum 3 à la passation `2026-11-02-2006`) n'est pas un refus du relais, l'appel est
   bien parti, et il ne doit pas être lu « budget_depasse » ; il garde donc le comportement de la v3 (code 3 ; champ
   `envoye` et coût compté inchangés). Fonction `refus_du_relais`.
4. **Version** `commande-kimi-v4`, cet en-tête (différences numérotées, historiques gardés en dessous) et la ligne d'usage.
   Rien d'autre ne change : mêmes gardes, mêmes bornes de sortie par rôle, même calcul du pire cas, même registre, même
   protocole vers le relais Kimi local 8804, mêmes codes de sortie hors le point 3.

Historique de la version 3 — rédigée le 2 novembre 2026 (sous-agent de session-depot). **Version 3 =
`commande_kimi_v2.py` (sha256 `644dbb39…`, inchangée, R12) avec quatre changements, et seulement ceux-là** (défaut TF-01 :
la v2 refusait, code 2, les rôles de l'étage de tests de mort) :

1. **Rôles** : `ROLES` étendu à `experimentateur_test` (l'expérimentateur de l'étage, joué par Kimi) et `lecteur_test` (le
   vérificateur, témoin jamais décisif), en plus de `proposeur_ideation` et `juge_ideation` (`pole/adaptateurs.py`,
   `ROLES_ETAGE_TESTS` ; `pole/tests_de_mort_v5.py`, `ROLE_EXPERIMENTATEUR`, `ROLE_LECTEUR`).
2. **Sortie maximale et minimale par rôle** (`bornes_de_sortie`) : proposeur → `--max-sortie-proposeur` /
   `--sortie-min-jetons` ; tout autre rôle → `--max-sortie-court` / `--sortie-min-jetons` ; sauf `lecteur_test` → options
   neuves `--max-sortie-lecteur` (défaut 1 000) et `--sortie-min-jetons-lecteur` (défaut 200 : le vérificateur rend une
   seule ligne, sous un plafond de session de 0,10 USD).
3. **Dernière ligne** : le champ `role` est rendu sur toute sortie (aussi sur un refus de réglage, code 2, où il vaut ce
   que portait `ROLE_POLE`) et le champ `version` vaut `commande-kimi-v3` ; le champ `envoye` est conservé tel quel.
4. **Cet en-tête** (différences numérotées) et la ligne d'usage. Rien d'autre ne change : mêmes gardes (session, étape,
   registre cumulé, écart de modèle), même registre `registre_depense_cumulee_v1.py` (importé depuis ce dossier), même
   protocole vers le relais Kimi local 8804 (`relais_kimi_v3.py`, inchangé).

Historique de la version 2 — rédigée le 1er novembre 2026 (sous-agent de session-depot). Version 2 =
`docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_kimi_v1.py` (inchangée, R12 ; elle ne jouait que le juge) avec
quatre changements :

1. **Rôles** : `proposeur_ideation` (proposeur) et `juge_ideation` (juge, aiguilleur, lecteur d'étiquettes) ; sortie
   maximale par rôle (`--max-sortie-proposeur`, 65 536 ; `--max-sortie-court`, 16 000 : plafonds du devis, scénario B).
2. **Plafond dur de l'étape** (porte « environnement » du noyau v56, `adaptateurs_v56.py`) : `PLAFOND_ETAPE_USD` et
   `ETAPE_POLE` lus dans l'environnement ; présents, la garde d'étape du registre s'applique (deux variables ou aucune).
3. **Garde cumulée au pire cas avant chaque appel** (`registre_depense_cumulee_v1.py`, `--registre`, `--plafond-cumule-usd`) :
   réglé + engagé + pire cas <= 10 USD, sinon refus sans envoi (code 4) ; règlement après l'appel, au coût lu (usage), ou au
   pire cas s'il manque.
4. **Écart de modèle vu par le relais** (HTTP 502 « modèle servi différent ») : la dernière ligne porte
   `modele_servi = "ecart-signale-par-le-relais"`, pour que l'adaptateur le lise comme un refus R-764 (et que le lanceur de
   la mini-course arrête la course : liste d'arrêt).

Contrat de `AdaptateurCommandeExterne` (inchangé) : consigne sur l'entrée standard (UTF-8), un seul message utilisateur ;
environnement minimal (`PLAFOND_SESSION_USD`, `ROLE_POLE`, `MODELE_DEMANDE_POLE` égal à `--modele` sinon code 2) ; la
**dernière ligne** de la sortie standard est toujours un objet JSON `{"texte", "cout_usd", "modele_servi", …}`, coût fini et
strictement positif (plancher 1e-6), aussi sur un échec.

**Aucune clé ici** : la commande parle au relais Kimi local (`relais_kimi_v3.py`, boucle locale seulement, jamais de
mandataire), qui tient la clé, la liste des modèles permis, la barrière du modèle servi et son propre plafond (second
barrage).

Garde avant envoi (hypothèse du relais : un jeton d'entrée fait au moins un octet du corps) :
    pire cas = (octets du corps + 1024) × prix d'entrée + max_tokens × prix de sortie <= PLAFOND_SESSION_USD
`max_tokens` = min(sortie maximale du rôle, ce que le reste du plafond de session paie) ; sous `--sortie-min-jetons` : refus
sans envoi (code 4). Les jetons de raisonnement sont dans `completion_tokens`, donc bornés par `max_tokens`.

Codes : 0 conforme ; 2 réglage ou entrée refusés ; 3 relais (HTTP, connexion) ; 4 pire cas au-dessus d'un plafond (session,
étape ou cumulé), registre illisible, ou refus du relais lui-même pour son plafond (402) ou son nombre d'appels (429) —
rien envoyé, champ `cause_refus` (v4) ; 5 réponse non conforme (vide, tronquée, modèle servi différent, usage absent, JSON
illisible, coût au-dessus du pire cas réservé) ; 6 délai dépassé ou interruption.

Usage : python3 -I -B commande_kimi_v4.py --registre REGISTRE --plafond-cumule-usd 50 [--url-relais http://127.0.0.1:8804]
            [--modele kimi-k3.1-pro] [--prix-entree 2] [--prix-sortie 10] [--max-sortie-proposeur 65536]
            [--max-sortie-court 16000] [--sortie-min-jetons 4096] [--max-sortie-lecteur 1000]
            [--sortie-min-jetons-lecteur 200] [--delai-s 1750]
"""

import argparse
import json
import math
import os
import signal
import sys
import urllib.error
import urllib.parse
import urllib.request

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)  # -I n'ajoute pas le dossier du script : le registre partagé est chargé d'ici
import registre_depense_cumulee_v1 as reg  # noqa: E402

VERSION = "commande-kimi-v4"
ROLES = ("proposeur_ideation", "juge_ideation", "experimentateur_test", "lecteur_test")  # v3 (1)
PLANCHER = 1e-6
ECART_RELAIS = "ecart-signale-par-le-relais"
CAUSES_REFUS = ("plafond_session", "garde_etape", "garde_cumulee", "registre_illisible", "relais_plafond",
                "relais_max_appels")  # v4 (2) : valeurs de `cause_refus`, présent sur toute sortie en code 4 et sur elle seule
CAUSES_RELAIS = {402: "relais_plafond", 429: "relais_max_appels"}  # v4 (2) : refus du relais lui-même, rien envoyé
PREFIXE_GARDE_ETAPE = "garde d'étape ("  # v4 (2) : registre_depense_cumulee_v1.py l. 143 (fichier gelé, sha256 8ba92066…)


def rendre(code, texte="", cout=PLANCHER, **diag):
    cout = cout if (isinstance(cout, (int, float)) and math.isfinite(cout) and cout > 0) else PLANCHER
    print(json.dumps({"texte": texte, "cout_usd": round(float(cout), 6), "version": VERSION, **diag}, ensure_ascii=False))
    sys.stdout.flush()
    sys.exit(code)


def lire_arguments(argv):
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    a.add_argument("--url-relais", default="http://127.0.0.1:8804")
    a.add_argument("--modele", default="kimi-k3.1-pro")
    a.add_argument("--prix-entree", type=float, default=2.0)
    a.add_argument("--prix-sortie", type=float, default=10.0)
    a.add_argument("--max-sortie-proposeur", type=int, default=65536)
    a.add_argument("--max-sortie-court", type=int, default=16000)
    a.add_argument("--sortie-min-jetons", type=int, default=4096)
    a.add_argument("--max-sortie-lecteur", type=int, default=1000)  # v3 (2) : lecteur_test, une seule ligne rendue
    a.add_argument("--sortie-min-jetons-lecteur", type=int, default=200)  # v3 (2)
    a.add_argument("--delai-s", type=float, default=1750.0)
    a.add_argument("--registre", required=True, help="registre de dépense cumulée du run (JSON par ligne)")
    a.add_argument("--plafond-cumule-usd", type=float, required=True)
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


def bornes_de_sortie(role, args):
    """v3 (2) : (sortie maximale, sortie minimale) en jetons selon le rôle : proposeur → `--max-sortie-proposeur` /
    `--sortie-min-jetons` ; `lecteur_test` (vérificateur, une seule ligne rendue) → `--max-sortie-lecteur` /
    `--sortie-min-jetons-lecteur` ; tout autre rôle (juge, expérimentateur) → `--max-sortie-court` / `--sortie-min-jetons`."""
    if role == "proposeur_ideation":
        return args.max_sortie_proposeur, args.sortie_min_jetons
    if role == "lecteur_test":
        return args.max_sortie_lecteur, args.sortie_min_jetons_lecteur
    return args.max_sortie_court, args.sortie_min_jetons


def cout_usage(usage, pe, ps):
    p, c = usage.get("prompt_tokens"), usage.get("completion_tokens")
    if not all(isinstance(x, int) and not isinstance(x, bool) and x >= 0 for x in (p, c)):
        return None
    return (p * pe + c * ps) / 1e6


def plafond_etape(environ):
    """(étape, plafond dur) de la porte « environnement », ou (None, None) ; une seule des deux variables : refus."""
    etape, brut = environ.get("ETAPE_POLE"), environ.get("PLAFOND_ETAPE_USD")
    if etape is None and brut is None:
        return None, None
    if etape is None or brut is None or not etape.strip():
        raise ValueError("porte « environnement » incomplète : ETAPE_POLE et PLAFOND_ETAPE_USD vont ensemble")
    p = float(brut)
    if not (math.isfinite(p) and p >= 0):
        raise ValueError("PLAFOND_ETAPE_USD invalide")
    return etape, p


def etape_du_registre(etape, fournisseur):
    """v4 (1, B1) : clé d'étape passée au registre, propre au fournisseur : `ETAPE_POLE` suivi de `/<fournisseur>` ; rien
    n'est ajouté s'il y finit déjà (idempotent) ; None sans porte « environnement » (garde d'étape inactive)."""
    if etape is None:
        return None
    suffixe = "/" + fournisseur
    return etape if etape.endswith(suffixe) else etape + suffixe


def cause_du_registre(e):
    """v4 (2) : cause d'un refus du registre, lue sur la décision elle-même (message rédigé sous le verrou du registre) :
    préfixe « garde d'étape ( » → `garde_etape` ; tout autre `PlafondCumule` (garde cumulée et ses deux contrôles
    d'entrée) → `garde_cumulee` ; `RegistreIllisible` ou `OSError` → `registre_illisible`."""
    if isinstance(e, reg.PlafondCumule):
        return "garde_etape" if str(e).startswith(PREFIXE_GARDE_ETAPE) else "garde_cumulee"
    return "registre_illisible"


def refus_du_relais(corps):
    """v4 (3) : vrai si le corps d'une réponse d'erreur est un refus rédigé par le relais Kimi lui-même (objet JSON portant
    `relais` = `relais-kimi-…`), faux pour une erreur de l'amont que le relais transmet telle quelle (statut et corps)."""
    try:
        objet = json.loads(corps)
    except (ValueError, RecursionError):
        return False
    return isinstance(objet, dict) and isinstance(objet.get("relais"), str) and objet["relais"].startswith("relais-kimi-")


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
        etape, plafond_dur = plafond_etape(environ)
        consigne = entree.read()
        if not consigne.strip():
            raise ValueError("consigne vide")
    except (ValueError, SystemExit) as e:
        rendre(2, erreur=str(e)[:300], envoye=False, role=environ.get("ROLE_POLE"))  # v3 (3)
    maxi, mini = bornes_de_sortie(role, args)  # v3 (2)
    n = None
    corps = None
    for _ in range(3):  # le corps grandit avec le chiffre de max_tokens : point fixe en quelques tours
        corps = json.dumps({"model": args.modele, "messages": [{"role": "user", "content": consigne}],
                            "max_tokens": n or maxi}, ensure_ascii=False).encode("utf-8")
        n2 = max_tokens_permis(len(corps), plafond, args.prix_entree, args.prix_sortie, maxi, mini)
        if n2 is None:
            rendre(4, erreur=f"pire cas au-dessus du plafond de session {plafond} USD (corps {len(corps)} octets)", envoye=False,
                   role=role, cause_refus="plafond_session")  # v3 (3), v4 (2)
        if n2 == n:
            break
        n = n2
    corps = json.dumps({"model": args.modele, "messages": [{"role": "user", "content": consigne}], "max_tokens": n},
                       ensure_ascii=False).encode("utf-8")
    pire = (len(corps) + 1024) * args.prix_entree / 1e6 + n * args.prix_sortie / 1e6
    if pire > plafond + 1e-12:
        rendre(4, erreur="pire cas au-dessus du plafond de session après point fixe", envoye=False, role=role,
               cause_refus="plafond_session")  # v3 (3), v4 (2)
    etape_registre = etape_du_registre(etape, "kimi")  # v4 (1)
    diag = {"max_tokens": n, "octets_corps": len(corps), "pire_cas_usd": round(pire, 6), "modele_demande": args.modele,
            "role": role, "etape": etape, "etape_registre": etape_registre}  # v4 (1) : `etape` = la valeur reçue
    try:
        ident = reg.reserver(args.registre, plafond_cumule_usd=args.plafond_cumule_usd, pire_cas_usd=pire, fournisseur="kimi",
                             role=role, modele=args.modele, etape=etape_registre, plafond_etape_usd=plafond_dur)  # v4 (1)
    except (reg.PlafondCumule, reg.RegistreIllisible, OSError) as e:
        rendre(4, erreur=str(e)[:300], envoye=False, cause_refus=cause_du_registre(e), **diag)  # v4 (2)

    def fin(code, texte="", cout=PLANCHER, origine="plancher", statut="echec", **extra):
        envoye = extra.pop("envoye", True)
        depasse = reg.regler(args.registre, ident, cout_usd=cout, pire_cas_usd=pire, statut=statut, code=code,
                             cout_origine=origine)
        if depasse and code == 0:  # le coût lu passe le pire cas réservé : la garantie du plafond ne tient plus
            extra.pop("erreur", None)
            rendre(5, cout=cout, erreur="coût lu au-dessus du pire cas réservé (liste d'arrêt)", envoye=True,
                   cout_origine=origine, depassement_reserve=True, **dict(diag, **extra))
        rendre(code, texte=texte, cout=cout, envoye=envoye, cout_origine=origine, **dict(diag, **extra))

    def interrompu(signum, _frame):
        fin(6, cout=pire, origine="pire_cas", erreur=f"signal {signum}")
    signal.signal(signal.SIGTERM, interrompu)
    signal.signal(signal.SIGINT, interrompu)

    ouvreur = urllib.request.build_opener(urllib.request.ProxyHandler({}))  # boucle locale : jamais de mandataire
    requete = urllib.request.Request(cible, data=corps, method="POST",
                                     headers={"Content-Type": "application/json", "Content-Length": str(len(corps))})
    try:
        with ouvreur.open(requete, timeout=args.delai_s) as rep:
            brut = rep.read()
    except urllib.error.HTTPError as e:
        corps_erreur = e.read()  # v4 (3) : lu en entier (refus signé par le relais ?) ; motif borné comme en v3
        motif = corps_erreur[:300].decode("utf-8", "replace")
        avant_amont = e.code in (400, 402, 403, 411, 413, 429)  # refus du relais sans rien envoyer à l'amont
        extra = {}
        if e.code == 502 and "modèle servi" in motif:
            extra["modele_servi"] = ECART_RELAIS  # lu par l'adaptateur comme un refus R-764 (point 4 de l'en-tête)
        code = 3 if e.code != 502 else 5
        if e.code in CAUSES_RELAIS and refus_du_relais(corps_erreur):  # v4 (3) : refus du relais lui-même, rien envoyé
            code, extra["cause_refus"] = 4, CAUSES_RELAIS[e.code]
        fin(code, cout=PLANCHER if avant_amont else pire, origine="plancher" if avant_amont else "pire_cas",
            erreur=f"HTTP {e.code} : {motif}", envoye=not avant_amont, **extra)
    except urllib.error.URLError as e:
        if isinstance(e.reason, ConnectionRefusedError):  # relais absent : rien n'est parti
            fin(3, erreur="relais injoignable (connexion refusée)", envoye=False)
        fin(3, cout=pire, origine="pire_cas", erreur="URLError : " + str(e.reason)[:200])
    except (TimeoutError, OSError) as e:
        fin(6 if isinstance(e, TimeoutError) else 3, cout=pire, origine="pire_cas", erreur=type(e).__name__ + " : " + str(e)[:200])
    try:
        objet = json.loads(brut)
        choix = objet["choices"][0]
        texte = choix["message"].get("content") or ""
        fin_raison = choix.get("finish_reason")
    except (ValueError, KeyError, IndexError, TypeError, AttributeError):
        fin(5, cout=pire, origine="pire_cas", erreur="réponse illisible")
    servi = objet.get("model")
    cout = cout_usage(objet.get("usage") or {}, args.prix_entree, args.prix_sortie)
    origine = "usage"
    if cout is None:
        cout, origine = pire, "pire_cas"
    extra = {"modele_servi": servi, "finish_reason": fin_raison,
             "usage": {k: v for k, v in (objet.get("usage") or {}).items() if isinstance(v, (int, float))}}
    if servi != args.modele:
        fin(5, cout=cout, origine=origine, erreur=f"modèle servi {servi!r} ≠ {args.modele!r}", **extra)
    if origine != "usage":
        fin(5, cout=cout, origine=origine, erreur="usage absent", **extra)
    if fin_raison == "length":
        fin(5, cout=cout, origine=origine, statut="tronque", erreur="réponse tronquée (finish_reason length)", **extra)
    if fin_raison == "content_filter":
        fin(5, cout=cout, origine=origine, statut="refus", refus=True, erreur="refus du modèle (content_filter)", **extra)
    if not texte.strip():
        fin(5, cout=cout, origine=origine, statut="vide", erreur="réponse vide", **extra)
    fin(0, texte=texte, cout=cout, origine=origine, statut="ok", **extra)


if __name__ == "__main__":
    main(sys.argv[1:], dict(os.environ), sys.stdin)
