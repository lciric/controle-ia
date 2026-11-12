#!/usr/bin/env python3
"""Commande externe d'Argon (gemini-4-argon) pour le tour fermé, étage 1 (orchestrateur v63) — v3.

Version 3, rédigée le 2 novembre 2026 (sous-agent de session-depot) ; rien n'a été lancé par le rédacteur. **Version 3 =
`commande_argon_v56_nuit_v2.py` (sha256 `221df610…`, inchangée, R12) avec quatre changements dans la seule sous-commande
`appeler`, et seulement ceux-là** (défaut TF-01 : la v2 refusait, code 2, les rôles de l'étage de tests de mort) :

1. **Rôles** : `ROLES` étendu à `experimentateur_test` (l'expérimentateur de l'étage) et `lecteur_test` (le vérificateur,
   joué par Argon, témoin jamais décisif), en plus de `proposeur_ideation` et `juge_ideation` (`pole/adaptateurs.py`,
   `ROLES_ETAGE_TESTS` ; `pole/tests_de_mort_v5.py`, `ROLE_EXPERIMENTATEUR`, `ROLE_LECTEUR`).
2. **Sortie maximale et minimale par rôle** (`bornes_de_sortie`) : proposeur → `--max-sortie-proposeur` /
   `--sortie-min-jetons` ; tout autre rôle → `--max-sortie-court` / `--sortie-min-jetons` ; sauf `lecteur_test` → options
   neuves de `appeler`, `--max-sortie-lecteur` (défaut 1 000) et `--sortie-min-jetons-lecteur` (défaut 200 : le
   vérificateur rend une seule ligne, sous un plafond de session de 0,10 USD).
3. **Dernière ligne** : le champ `role` est rendu sur toute sortie (aussi sur un refus de réglage, code 2, où il vaut ce
   que portait `ROLE_POLE`) et le champ `version` vaut `commande-argon-v56-nuit-v3` ; le champ `envoye` est conservé.
4. **Cet en-tête** (différences numérotées) et les lignes d'usage.

**La sous-commande `servir` (le relais Argon local, port 8805) est inchangée, ligne pour ligne, et se comporte à
l'identique** : aucune reprise ajoutée (`attentes=(0,)`), mêmes codes 402 (plafond du relais), 429 (nombre d'appels),
413 (corps trop grand), 411 (`Content-Length` exigé), 403, 400, mêmes journaux, même empreinte exigée du collisionneur. Le
relais est un instrument gelé d'une autre expérience (A1-v3) : il continue d'être servi depuis le fichier qui le sert
aujourd'hui ; seule la constante `VERSION`, partagée par les deux sous-commandes, change de nom (champ `version` de
`GET /relais/etat` et en-tête `Server` si l'on servait depuis ce fichier). Remarque : `COLLISIONNEUR_DEFAUT` est calculé
relativement au dossier du fichier (trois dossiers au-dessus, `espece-seule-v1/collisionneur_v7.py`) ; depuis
`docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/` il ne pointe sur rien : `servir` depuis ce fichier exigerait
`--collisionneur` explicite (inchangé, hors du périmètre de la v3).

Historique de la version 2 — rédigée le 1er novembre 2026 (sous-agent de session-depot). **Version 2** =
`commande_argon_v56_nuit_v1.py` (inchangée, R12) avec une seule correction, trouvée par la répétition v2 : sur un échec ou un
usage absent, le coût compté est le pire cas **réservé par la commande** (et non le nombre arrondi à 8 décimales rendu par le
relais, qui pouvait le dépasser de moins de 1e-8 et marquer à tort un « dépassement de réserve », devenu un arrêt de la course
en v2, CLM-02). Enveloppe la fonction
`appeler_gemini` du collisionneur v7 (`donnees/espece-seule-v1/collisionneur_v7.py`, empreinte vérifiée au démarrage),
**sans reprise interne** (`attentes=(0,)`, comme l'épreuve du pont, CL-05), dans le contrat de la commande externe que lit
`AdaptateurCommandeExterneV56` (`pole/adaptateurs_v56.py`).

Pourquoi deux processus. L'orchestrateur v56 **refuse** de partir si un nom de variable de clé (dont `GEMINI_API_KEY`) est
dans son environnement (`pole/relais.py`, `noms_de_cle_presents`), et ne transmet à la commande qu'un environnement minimal
(`PATH`, `HOME`, `LANG`, `LC_ALL`, `TMPDIR`, plus `PLAFOND_SESSION_USD`, `ROLE_POLE`, `MODELE_DEMANDE_POLE`, `ETAPE_POLE`,
`PLAFOND_ETAPE_USD`). La clé ne peut donc pas suivre le chemin orchestrateur → commande. Ce fichier a deux sous-commandes :

- `servir` : **relais Argon local**, lancé par `lancer-mini-course-v1.sh` sous `env -i` avec la clé dans la variable
  `GEMINI_API_KEY` de **son seul environnement** (valeur prise de `GEMINI_API_KEY_2`, jamais en argument ni en fichier) ;
  boucle locale seulement (`127.0.0.1`) ; `POST /appel` {modele, prompt, max_tokens, pire_cas_usd} appelle
  `appeler_gemini(modele, prompt, max_tokens, attentes=(0,))` et rend {texte, modele_servi, fin, statut, usage, cout_usd,
  cout_origine, echec} ; `GET /relais/etat` rend compteurs, plafond, PID et la seule **présence** de la clé (booléen).
  Second barrage : plafond propre (`--plafond-usd`, réserve au pire cas sous verrou), nombre d'appels borné
  (`--max-appels`), modèles permis (`--modeles-permis`). Journal (`--journal`, JSON par ligne) : jamais le texte, jamais la
  clé. Limite connue (comme `relais_kimi_v3.py`) : `/proc/<pid>/environ` expose la clé à tout processus du même utilisateur
  tant que le relais vit ; conteneur à un seul utilisateur.
- `appeler` (défaut, lancé par l'orchestrateur pour chaque appel) : consigne sur l'entrée standard ; garde du pire cas sur
  le plafond de session (`PLAFOND_SESSION_USD`), puis **garde cumulée** du registre partagé
  (`registre_depense_cumulee_v1.py` : réglé + engagé + pire cas <= 10 USD, et garde de l'étape si `PLAFOND_ETAPE_USD` est
  donné) ; envoi au relais local (jamais de mandataire) ; dernière ligne JSON `{texte, cout_usd > 0, modele_servi}`.

Pire cas (formule du collisionneur v7, `cout_pire_cas`) : caractères / 3 × prix d'entrée + max_tokens × prix de sortie, au
barème prudent 10 et 50 USD par million (`collisionneur_v7.py:62-63`, SUPPOSÉ) ; `max_tokens` = min(sortie maximale du rôle
— `--max-sortie-proposeur` 32 000, `--max-sortie-court` 4 000, plafonds du devis —, ce que le reste du plafond de session
paie) ; sous `--sortie-min-jetons` : refus sans envoi (code 4). Coût rendu : usage lu (`promptTokenCount` à l'entrée,
`candidatesTokenCount` + `thoughtsTokenCount` à la sortie, fonction `cout` du collisionneur) ; échec ou usage absent (entrée
nulle) → pire cas ; rien envoyé → plancher 1e-6.

Codes (`appeler`) : 0 conforme ; 2 réglage ou entrée refusés ; 3 relais ou interface (HTTP, connexion) ; 4 pire cas
au-dessus d'un plafond (session, étape, cumulé, relais) ou registre illisible ; 5 réponse non conforme (vide, tronquée,
refus du modèle, anomalie, modèle servi différent, coût au-dessus du pire cas réservé) ; 6 délai dépassé ou interruption.
Codes (`servir`) : 2 réglage refusé (clé absente, collisionneur à empreinte différente, modèle non permis) ; sinon sert
jusqu'à l'arrêt par PID (R10).

Usage :
  env -i PATH=/usr/bin:/bin LANG=C.UTF-8 GEMINI_API_KEY="$GEMINI_API_KEY_2" HTTPS_PROXY=… SSL_CERT_FILE=… \\
      python3 -I -B commande_argon_v56_nuit_v3.py servir --port 8805 --plafond-usd 10 --max-appels 50 --journal J.jsonl
  python3 -I -B commande_argon_v56_nuit_v3.py appeler --url-relais http://127.0.0.1:8805 --registre R.jsonl \\
      --plafond-cumule-usd 50 [--max-sortie-proposeur 32000] [--max-sortie-court 4000] [--sortie-min-jetons 1000] \\
      [--max-sortie-lecteur 1000] [--sortie-min-jetons-lecteur 200] [--delai-s 1750]
                                     (consigne sur l'entrée standard ; environnement fourni par l'orchestrateur)
"""

import argparse
import datetime
import functools
import hashlib
import importlib.util
import json
import math
import os
import signal
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)  # -I n'ajoute pas le dossier du script : le registre partagé est chargé d'ici
import registre_depense_cumulee_v1 as reg  # noqa: E402

VERSION = "commande-argon-v56-nuit-v3"
ROLES = ("proposeur_ideation", "juge_ideation", "experimentateur_test", "lecteur_test")  # v3 (1)
PLANCHER = 1e-6
HOTE = "127.0.0.1"
COLLISIONNEUR_DEFAUT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(ICI))), "espece-seule-v1", "collisionneur_v7.py")
SHA_COLLISIONNEUR = "c9725f025407c3ece3e8c16d19cfdfdec078f084a811f0a3b6ea3209be5d98dc"
PRIX = (10.0, 50.0)  # collisionneur_v7.py:62-63, prix prudent (SUPPOSÉ)
MAX_OCTETS_CORPS = 4_000_000


def maintenant():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def pire_cas(caracteres, max_tokens, prix=PRIX):
    """Formule de `collisionneur_v7.cout_pire_cas` (caractères / 3 à l'entrée)."""
    return caracteres / 3 / 1e6 * prix[0] + max_tokens / 1e6 * prix[1]


# --- relais (sous-commande `servir`) ---------------------------------------------------------------------------------------


def charger_collisionneur(chemin, sha):
    with open(chemin, "rb") as f:
        vu = hashlib.sha256(f.read()).hexdigest()
    if vu != sha:
        raise SystemExit(f"collisionneur {chemin} : empreinte {vu[:12]}… différente de {sha[:12]}… : refus de servir")
    spec = importlib.util.spec_from_file_location("collisionneur_v7_mini_course_v2", chemin)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class EtatRelais:
    def __init__(self, plafond, max_appels, modeles, journal, collisionneur_sha):
        self.plafond, self.max_appels, self.modeles, self.journal = float(plafond), int(max_appels), set(modeles), journal
        self.collisionneur_sha = collisionneur_sha
        self.depense, self.engage, self.appels, self.refus = 0.0, 0.0, 0, {}
        self.verrou = threading.Lock()

    def noter_refus(self, motif):
        self.refus[motif] = self.refus.get(motif, 0) + 1

    def ecrire_journal(self, entree):
        if not self.journal:
            return
        with open(self.journal, "a", encoding="utf-8") as f:
            f.write(json.dumps(dict(entree, quand_utc=maintenant()), ensure_ascii=False, sort_keys=True) + "\n")


def statut_et_cout(c, rep, pire):
    """(statut, coût, origine) d'une réponse du collisionneur ; usage absent (entrée nulle) ou échec → pire cas."""
    if rep.echec:
        return "ECHEC", pire, "pire_cas"
    statut = c.statut_reponse("gemini", rep)
    u = rep.usage or {}
    if not isinstance(u.get("entree"), int) or u.get("entree", 0) <= 0:
        return statut, pire, "pire_cas"
    return statut, c.cout(PRIX, u), "usage"


def fabriquer_gestion(etat, appelant, c, masquer):
    class Gestion(BaseHTTPRequestHandler):
        server_version = VERSION

        def log_message(self, *a):  # aucun journal du serveur sur la sortie d'erreur (jamais de texte)
            pass

        def _json(self, code, objet):
            corps = json.dumps(objet, ensure_ascii=False).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(corps)))
            self.end_headers()
            self.wfile.write(corps)

        def do_GET(self):
            if self.path != "/relais/etat":
                return self._json(403, {"erreur": "chemin refusé"})
            return self._json(200, {"version": VERSION, "pid": os.getpid(), "appels": etat.appels, "max_appels": etat.max_appels,
                                    "depense_usd": round(etat.depense, 6), "engage_usd": round(etat.engage, 6),
                                    "plafond_usd": etat.plafond, "refus": etat.refus, "modeles_permis": sorted(etat.modeles),
                                    "cle_presente": bool(os.environ.get("GEMINI_API_KEY")),
                                    "collisionneur_sha256": etat.collisionneur_sha, "appelant": etat.nature_appelant,
                                    "reprise_interne": "aucune (attentes=(0,))"})

        def do_POST(self):
            if self.path != "/appel":
                return self._json(403, {"erreur": "chemin refusé"})
            longueur = self.headers.get("Content-Length")
            if longueur is None:
                return self._json(411, {"erreur": "Content-Length exigé"})
            if int(longueur) > MAX_OCTETS_CORPS:
                return self._json(413, {"erreur": "corps trop grand"})
            try:
                d = json.loads(self.rfile.read(int(longueur)))
                modele, prompt, mt, pire = d["modele"], d["prompt"], int(d["max_tokens"]), float(d["pire_cas_usd"])
                if not (isinstance(prompt, str) and prompt.strip() and mt > 0 and math.isfinite(pire) and pire >= 0):
                    raise ValueError
            except (ValueError, KeyError, TypeError):
                etat.noter_refus("requete_illisible")
                return self._json(400, {"erreur": "requête illisible"})
            if modele not in etat.modeles:
                etat.noter_refus("modele_non_permis")
                return self._json(403, {"erreur": f"modèle {modele!r} non permis"})
            pire_relais = max(pire, pire_cas(len(prompt), mt))
            with etat.verrou:
                if etat.appels >= etat.max_appels:
                    etat.noter_refus("max_appels")
                    return self._json(429, {"erreur": "max-appels atteint (relais Argon)"})
                if etat.depense + etat.engage + pire_relais > etat.plafond + 1e-9:
                    etat.noter_refus("plafond")
                    return self._json(402, {"erreur": f"plafond de dépense du relais Argon : {etat.depense:.4f} + pire cas "
                                                      f"{pire_relais:.4f} > {etat.plafond:g} USD"})
                etat.appels += 1
                etat.engage += pire_relais
                numero = etat.appels
            t0 = time.time()
            try:
                rep = appelant(modele, prompt, mt)
            except Exception as e:  # noqa: BLE001 — une exception de l'appel est un échec consigné, au pire cas
                rep = c.Reponse(echec=f"exception : {type(e).__name__} : {masquer(str(e))[:300]}")
            duree = round(time.time() - t0, 1)
            statut, cout, origine = statut_et_cout(c, rep, pire_relais)
            with etat.verrou:
                etat.engage -= pire_relais
                etat.depense += cout
            etat.ecrire_journal({"appel": numero, "modele_demande": modele, "modele_servi": rep.modele_servi, "statut": statut,
                                 "fin": rep.fin, "usage": rep.usage, "cout_usd": round(cout, 6), "cout_origine": origine,
                                 "pire_cas_usd": round(pire_relais, 6), "max_tokens": mt, "caracteres": len(prompt),
                                 "duree_s": duree, "echec": masquer(rep.echec)[:300] if rep.echec else None,
                                 "depense_cumulee_usd": round(etat.depense, 6)})
            return self._json(200, {"texte": rep.texte or "", "modele_servi": rep.modele_servi, "fin": rep.fin,
                                    "categorie": rep.categorie, "statut": statut, "usage": rep.usage, "cout_usd": round(cout, 8),
                                    "cout_origine": origine, "pire_cas_relais_usd": round(pire_relais, 8),
                                    "echec": masquer(rep.echec)[:300] if rep.echec else None, "duree_s": duree})
    return Gestion


def servir(args, appelant=None, c=None, environ=None, nature_appelant=None):
    """Sert jusqu'à l'arrêt. `appelant` et `c` injectables (répétition sans réseau) ; défaut : collisionneur v7 vérifié,
    `appeler_gemini(..., attentes=(0,))` et clé lue dans l'environnement du relais."""
    environ = os.environ if environ is None else environ
    if c is None:
        c = charger_collisionneur(args.collisionneur, args.sha_collisionneur)
    if appelant is None:
        if not environ.get("GEMINI_API_KEY"):
            raise SystemExit("GEMINI_API_KEY absente de l'environnement du relais : refus de servir")
        appelant = functools.partial(c.appeler_gemini, attentes=(0,))
        nature_appelant = "collisionneur_v7.appeler_gemini(attentes=(0,))"
    elif nature_appelant is None:
        nature_appelant = "appelant injecté (répétition sans réseau)"
    cle = environ.get("GEMINI_API_KEY") or ""

    def masquer(texte):
        texte = str(texte)
        return texte.replace(cle, "[clé]") if len(cle) >= 8 else texte

    modeles = [m.strip() for m in args.modeles_permis.split(",") if m.strip()]
    if not modeles:
        raise SystemExit("--modeles-permis vide")
    etat = EtatRelais(args.plafond_usd, args.max_appels, modeles, args.journal, args.sha_collisionneur)
    etat.nature_appelant = nature_appelant
    serveur = HTTPServer((HOTE, args.port), fabriquer_gestion(etat, appelant, c, masquer))
    print(f"relais Argon prêt sur http://{HOTE}:{serveur.server_address[1]} (PID {os.getpid()})", flush=True)

    def arreter(signum, _frame):
        raise KeyboardInterrupt
    if threading.current_thread() is threading.main_thread():  # arrêt par PID (R10) : SIGTERM ferme le serveur proprement
        signal.signal(signal.SIGTERM, arreter)
    try:
        serveur.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        serveur.server_close()
    return 0


# --- commande (sous-commande `appeler`) ------------------------------------------------------------------------------------


def rendre(code, texte="", cout=PLANCHER, **diag):
    cout = cout if (isinstance(cout, (int, float)) and math.isfinite(cout) and cout > 0) else PLANCHER
    print(json.dumps({"texte": texte, "cout_usd": round(float(cout), 8), "version": VERSION, **diag}, ensure_ascii=False))
    sys.stdout.flush()
    sys.exit(code)


def verifier_url(url):
    u = urllib.parse.urlsplit(url)
    if u.scheme != "http" or u.hostname not in ("127.0.0.1", "localhost") or u.path not in ("", "/"):
        raise ValueError("--url-relais : http://127.0.0.1:PORT seulement (le relais local tient la clé)")
    return url.rstrip("/") + "/appel"


def bornes_de_sortie(role, args):
    """v3 (2) : (sortie maximale, sortie minimale) en jetons selon le rôle : proposeur → `--max-sortie-proposeur` /
    `--sortie-min-jetons` ; `lecteur_test` (vérificateur, une seule ligne rendue) → `--max-sortie-lecteur` /
    `--sortie-min-jetons-lecteur` ; tout autre rôle (juge, expérimentateur) → `--max-sortie-court` / `--sortie-min-jetons`."""
    if role == "proposeur_ideation":
        return args.max_sortie_proposeur, args.sortie_min_jetons
    if role == "lecteur_test":
        return args.max_sortie_lecteur, args.sortie_min_jetons_lecteur
    return args.max_sortie_court, args.sortie_min_jetons


def plafond_etape(environ):
    etape, brut = environ.get("ETAPE_POLE"), environ.get("PLAFOND_ETAPE_USD")
    if etape is None and brut is None:
        return None, None
    if etape is None or brut is None or not etape.strip():
        raise ValueError("porte « environnement » incomplète : ETAPE_POLE et PLAFOND_ETAPE_USD vont ensemble")
    p = float(brut)
    if not (math.isfinite(p) and p >= 0):
        raise ValueError("PLAFOND_ETAPE_USD invalide")
    return etape, p


def appeler(args, environ, entree):
    try:
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
        prompt = entree.read()
        if not prompt.strip():
            raise ValueError("consigne vide")
    except (ValueError, SystemExit) as e:
        rendre(2, erreur=str(e)[:300], envoye=False, role=environ.get("ROLE_POLE"))  # v3 (3)
    maxi, mini = bornes_de_sortie(role, args)  # v3 (2)
    entree_usd = pire_cas(len(prompt), 0)
    mt = min(maxi, int((plafond - entree_usd) * 1e6 / PRIX[1])) if plafond > entree_usd else 0
    if mt < mini:  # v3 (2)
        rendre(4, erreur=f"pire cas au-dessus du plafond de session {plafond} USD ({len(prompt)} caractères)", envoye=False,
               role=role)  # v3 (3)
    pire = pire_cas(len(prompt), mt)
    if pire > plafond + 1e-12:
        rendre(4, erreur="pire cas au-dessus du plafond de session", envoye=False, role=role)  # v3 (3)
    diag = {"max_tokens": mt, "caracteres": len(prompt), "pire_cas_usd": round(pire, 8), "modele_demande": args.modele,
            "role": role, "etape": etape}
    try:
        ident = reg.reserver(args.registre, plafond_cumule_usd=args.plafond_cumule_usd, pire_cas_usd=pire, fournisseur="argon",
                             role=role, modele=args.modele, etape=etape, plafond_etape_usd=plafond_dur)
    except (reg.PlafondCumule, reg.RegistreIllisible, OSError) as e:
        rendre(4, erreur=str(e)[:300], envoye=False, **diag)

    def fin(code, texte="", cout=PLANCHER, origine="plancher", statut="echec", **extra):
        envoye = extra.pop("envoye", True)
        depasse = reg.regler(args.registre, ident, cout_usd=cout, pire_cas_usd=pire, statut=statut, code=code,
                             cout_origine=origine)
        if depasse and code == 0:
            extra.pop("erreur", None)
            rendre(5, cout=cout, erreur="coût lu au-dessus du pire cas réservé (liste d'arrêt)", envoye=True,
                   cout_origine=origine, depassement_reserve=True, **dict(diag, **extra))
        rendre(code, texte=texte, cout=cout, envoye=envoye, cout_origine=origine, **dict(diag, **extra))

    def interrompu(signum, _frame):
        fin(6, cout=pire, origine="pire_cas", erreur=f"signal {signum}")
    signal.signal(signal.SIGTERM, interrompu)
    signal.signal(signal.SIGINT, interrompu)

    corps = json.dumps({"modele": args.modele, "prompt": prompt, "max_tokens": mt, "pire_cas_usd": pire},
                       ensure_ascii=False).encode("utf-8")
    ouvreur = urllib.request.build_opener(urllib.request.ProxyHandler({}))  # boucle locale : jamais de mandataire
    requete = urllib.request.Request(cible, data=corps, method="POST",
                                     headers={"Content-Type": "application/json", "Content-Length": str(len(corps))})
    try:
        with ouvreur.open(requete, timeout=args.delai_s) as r:
            brut = r.read()
    except urllib.error.HTTPError as e:
        motif = e.read()[:300].decode("utf-8", "replace")
        avant = e.code in (400, 402, 403, 411, 413, 429)  # refus du relais : rien n'est parti vers l'interface
        fin(4 if e.code in (402, 429) else 3, cout=PLANCHER if avant else pire, origine="plancher" if avant else "pire_cas",
            erreur=f"HTTP {e.code} : {motif}", envoye=not avant)
    except urllib.error.URLError as e:
        if isinstance(e.reason, ConnectionRefusedError):
            fin(3, erreur="relais Argon injoignable (connexion refusée)", envoye=False)
        fin(3, cout=pire, origine="pire_cas", erreur="URLError : " + str(e.reason)[:200])
    except (TimeoutError, OSError) as e:
        fin(6 if isinstance(e, TimeoutError) else 3, cout=pire, origine="pire_cas", erreur=type(e).__name__ + " : " + str(e)[:200])
    try:
        o = json.loads(brut)
        texte, statut, cout, origine = o["texte"], o["statut"], float(o["cout_usd"]), o["cout_origine"]
    except (ValueError, KeyError, TypeError):
        fin(5, cout=pire, origine="pire_cas", erreur="réponse du relais illisible")
    if origine == "pire_cas":
        cout = pire  # v2 : le pire cas réservé, exactement (jamais l'arrondi du relais, qui pouvait le dépasser de 1e-8)
    servi = o.get("modele_servi")
    extra = {"modele_servi": servi, "fin_interface": o.get("fin"), "usage": o.get("usage"), "statut_interface": statut}
    if o.get("echec"):
        extra.pop("modele_servi")  # échec de transport : aucun modèle n'a répondu
        fin(3, cout=cout, origine=origine, erreur="interface : " + str(o["echec"])[:300], **extra)
    if servi != args.modele:  # identifiant exact (servi observé à l'épreuve du pont : « gemini-4-argon »)
        fin(5, cout=cout, origine=origine, erreur=f"modèle servi {servi!r} ≠ {args.modele!r}", **extra)
    if statut == "REFUS":
        fin(5, cout=cout, origine=origine, statut="refus", refus=True, erreur=f"refus du modèle ({o.get('categorie') or o.get('fin')})",
            **extra)
    if statut in ("TRONQUE", "VIDE", "ANOMALIE"):
        fin(5, cout=cout, origine=origine, statut=statut.lower(), erreur=f"réponse non conforme ({statut}, fin {o.get('fin')!r})",
            **extra)
    if origine != "usage":
        fin(5, cout=cout, origine=origine, erreur="usage absent", **extra)
    fin(0, texte=texte, cout=cout, origine=origine, statut="ok", **extra)


def principal(argv=None, environ=None, entree=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] not in ("servir", "appeler"):
        argv = ["appeler"] + argv
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sous = a.add_subparsers(dest="mode", required=True)
    s = sous.add_parser("servir")
    s.add_argument("--port", type=int, required=True)
    s.add_argument("--plafond-usd", type=float, required=True)
    s.add_argument("--max-appels", type=int, required=True)
    s.add_argument("--journal", required=True)
    s.add_argument("--modeles-permis", default="gemini-4-argon")
    s.add_argument("--collisionneur", default=COLLISIONNEUR_DEFAUT)
    s.add_argument("--sha-collisionneur", default=SHA_COLLISIONNEUR)
    p = sous.add_parser("appeler")
    p.add_argument("--url-relais", default="http://127.0.0.1:8805")
    p.add_argument("--modele", default="gemini-4-argon")
    p.add_argument("--max-sortie-proposeur", type=int, default=32000)
    p.add_argument("--max-sortie-court", type=int, default=4000)
    p.add_argument("--sortie-min-jetons", type=int, default=1000)
    p.add_argument("--max-sortie-lecteur", type=int, default=1000)  # v3 (2) : lecteur_test, une seule ligne rendue
    p.add_argument("--sortie-min-jetons-lecteur", type=int, default=200)  # v3 (2)
    p.add_argument("--delai-s", type=float, default=1750.0)
    p.add_argument("--registre", required=True)
    p.add_argument("--plafond-cumule-usd", type=float, required=True)
    args = a.parse_args(argv)
    if args.mode == "servir":
        if args.port <= 0 or args.plafond_usd <= 0 or args.max_appels <= 0:
            raise SystemExit("servir : --port, --plafond-usd, --max-appels strictement positifs")
        return servir(args)
    return appeler(args, dict(os.environ) if environ is None else environ, sys.stdin if entree is None else entree)


if __name__ == "__main__":
    sys.exit(principal())
