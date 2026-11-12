"""Essais des commandes externes v4 du tour fermé, étage 1 : `commande_kimi_v4.py` et `commande_argon_v56_nuit_v4.py`
(sous-commande `appeler` ; pour `servir`, identité avec la v3 et codes du relais), sans réseau hors boucle locale, sans clé,
sans dépense, sans modèle. Rédigés le 3 novembre 2026 (sous-agent de session-depot) à partir de la suite v3
(`test_commandes_tour_ferme_v3.py`, inchangée, qui reste la suite de la v3).

Chaque commande est lancée comme en production (`python -I -B`, environnement minimal de `AdaptateurCommandeExterne`, consigne
sur l'entrée standard) contre un **faux relais local** en processus (boucle locale, port éphémère, une requête par connexion,
connexion toujours fermée après la réponse, lecture bornée par un délai ; un relais lent est toujours libéré en fin d'essai),
qui consigne chaque requête reçue. Interpréteur des commandes : `PY_COMMANDES` s'il est donné (par exemple `/usr/bin/python3`),
sinon celui du dépôt. Tout processus lancé ici est arrêté par son PID (R10).

    cd docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1
    env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp nice -n 10 /home/user/controle-ia-travail/.venv/bin/python -B -m pytest \\
        -q -p no:cacheprovider test_commandes_tour_ferme_v4.py

Ce qui s'ajoute à la suite v3 : (a) B1, deux fournisseurs sur le même registre et la même `ETAPE_POLE` avec des parts
différentes, idempotence du suffixe, garde cumulée commune ; (b) les six essais de l'important I2 de la contre-lecture (modèle
servi différent, coût fini > 0 sur chaque code 4, 402 et 429 de Kimi, délai dépassé, signaux, coût d'un échec d'Argon au pire
cas réservé) ; (c) option refusée par argparse chez Argon ; (d) `cause_refus` présente et juste pour chacune des six causes,
absente hors du code 4.
"""

import hashlib
import importlib.util
import inspect
import json
import math
import os
import signal
import socket
import subprocess
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest

ICI = os.path.dirname(os.path.abspath(__file__))
PY_DEPOT = "/home/user/controle-ia-travail/.venv/bin/python"
PY = os.environ.get("PY_COMMANDES") or (PY_DEPOT if os.path.exists(PY_DEPOT) else sys.executable)
PY_SYSTEME = "/usr/bin/python3"  # interpréteur des commandes de la configuration v3 (mineur 4 de la contre-lecture)
KIMI, ARGON = os.path.join(ICI, "commande_kimi_v4.py"), os.path.join(ICI, "commande_argon_v56_nuit_v4.py")
ARGON_V3 = os.path.join(ICI, "commande_argon_v56_nuit_v3.py")  # pour l'identité du bloc `servir`
REGISTRE_MODULE = os.path.join(ICI, "registre_depense_cumulee_v1.py")
SHA_REGISTRE = "8ba92066b358ffb8206dea9e70251388c30620484fab1ac578778d9f21e578ff"
MARQUEUR_RELAIS = b"\n# --- relais (sous-commande `servir`) ---"  # lignes-marqueurs du bloc `servir` d'Argon
MARQUEUR_COMMANDE = b"\n# --- commande (sous-commande `appeler`) ---"
ROLES_ATTENDUS = ("proposeur_ideation", "juge_ideation", "experimentateur_test", "lecteur_test")
CAUSES_ATTENDUES = ("plafond_session", "garde_etape", "garde_cumulee", "registre_illisible", "relais_plafond", "relais_max_appels")
CLE_FACTICE = "cle-factice-0123456789abcdef"  # jamais une clé : une chaîne témoin, cherchée dans ce que reçoit le faux relais
ETAPE = "tour_ferme_v63"
CONSIGNE = "Réponds seulement par VERDICT: survit ; chiffre: 1.5 ; ligne: RESULTAT: 1.5"
REFUS_SIGNE_KIMI = {"erreur": "refus du relais", "relais": "relais-kimi-v3", "plafond_usd": 44.0, "appels": 3}
ERREUR_AMONT = {"error": {"message": "quota", "type": "exceeded_current_quota_error"}}  # forme d'une erreur de Moonshot


def charger(nom, chemin):
    """Importe un module de ce dossier par son chemin (sans le lancer : `__name__` ≠ `__main__`)."""
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def derniere_ligne(octets):
    lignes = [l for l in octets.decode("utf-8", "replace").splitlines() if l.strip()]
    return json.loads(lignes[-1]) if lignes else None


def cout_fini_positif(o):
    return isinstance(o["cout_usd"], float) and math.isfinite(o["cout_usd"]) and o["cout_usd"] > 0


# --- faux relais -------------------------------------------------------------------------------------------------------------


class FauxRelais:
    """Relais factice en processus : `/v1/chat/completions` (façon relais Kimi) ou `/appel` (façon relais Argon) ; chaque
    requête reçue va au journal. `reglage` : `servi` (modèle rendu), `usage`, `cout_usd` (nombre ou fonction du corps reçu),
    `cout_origine`, `echec`, `statut_http` + `corps_erreur` (réponse d'erreur), `lenteur_s` (attente avant de répondre,
    interrompue par `liberer`). `recu` est posé dès qu'une requête est lue."""

    def __init__(self, fournisseur):
        self.fournisseur, self.journal, self.reglage = fournisseur, [], {}
        self.recu, self.liberer = threading.Event(), threading.Event()
        self.serveur = ThreadingHTTPServer(("127.0.0.1", 0), fabriquer_faux_relais(self))  # fils démons : rien ne bloque l'arrêt
        self.fil = threading.Thread(target=self.serveur.serve_forever, daemon=True)
        self.fil.start()
        self.url = f"http://127.0.0.1:{self.serveur.server_address[1]}"

    def fermer(self):
        self.liberer.set()  # un relais lent rend la main
        self.serveur.shutdown()
        self.serveur.server_close()
        self.fil.join(timeout=10)


def fabriquer_faux_relais(relais):
    class G(BaseHTTPRequestHandler):
        timeout = 30  # aucune lecture bloquée sans fin (incident d'essai de la v3, LISEZMOI v1)
        protocol_version = "HTTP/1.0"  # une requête par connexion, fermée après la réponse

        def log_message(self, *a):
            pass

        def do_POST(self):
            r = relais.reglage
            corps = self.rfile.read(int(self.headers["Content-Length"]))
            d = json.loads(corps)
            relais.journal.append({"chemin": self.path, "entetes": dict(self.headers.items()), "corps": d, "brut": corps})
            relais.recu.set()
            if r.get("lenteur_s"):
                relais.liberer.wait(r["lenteur_s"])
            attendu = "/v1/chat/completions" if relais.fournisseur == "kimi" else "/appel"
            if self.path != attendu:
                code, rep = 404, {"erreur": "chemin"}
            elif r.get("statut_http"):
                code, rep = r["statut_http"], r.get("corps_erreur", {"erreur": "refus"})
            elif relais.fournisseur == "kimi":
                code, rep = 200, {
                    "model": r.get("servi") or d["model"],
                    "choices": [{"message": {"content": "VERDICT: survit ; chiffre: 1.5 ; ligne: RESULTAT: 1.5"}, "finish_reason": "stop"}],
                    "usage": r.get("usage") or {"prompt_tokens": 10, "completion_tokens": 5}}
            else:
                cout = r.get("cout_usd", 0.00035)
                code, rep = 200, {
                    "texte": "VERDICT: survit ; chiffre: 1.5 ; ligne: RESULTAT: 1.5", "modele_servi": r.get("servi") or d["modele"],
                    "fin": "STOP", "categorie": None, "statut": "OK", "usage": r.get("usage") or {"entree": 10, "sortie": 5},
                    "cout_usd": cout(d) if callable(cout) else cout, "cout_origine": r.get("cout_origine", "usage"),
                    "pire_cas_relais_usd": d["pire_cas_usd"], "echec": r.get("echec"), "duree_s": 0.1}
            b = rep if isinstance(rep, bytes) else json.dumps(rep, ensure_ascii=False).encode("utf-8")
            try:
                self.send_response(code)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(b)))
                self.send_header("Connection", "close")
                self.end_headers()
                self.wfile.write(b)
            except OSError:  # le client est parti (délai dépassé, signal) : rien à rendre
                pass
            self.close_connection = True
    return G


class Commande:
    """Une commande sous essai : lancement comme en production, faux relais, lecture de la dernière ligne."""

    def __init__(self, nom, relais, tmp, url=None):
        self.nom, self.relais, self.tmp = nom, relais, str(tmp)
        self.url = url or relais.url
        self.modele = "kimi-k3.1-pro" if nom == "kimi" else "gemini-4-argon"
        self.version = "commande-kimi-v4" if nom == "kimi" else "commande-argon-v56-nuit-v4"
        self.registre = os.path.join(self.tmp, "registre.jsonl")

    @property
    def journal(self):
        return self.relais.journal if self.relais is not None else []

    def arguments(self, options=(), registre=True, plafond_cumule=True, url=True, interprete=None):
        base = [interprete or PY, "-I", "-B"] + ([KIMI] if self.nom == "kimi" else [ARGON, "appeler"])
        if url:
            base += ["--url-relais", self.url]
        if registre:
            base += ["--registre", self.registre]
        if plafond_cumule:
            base += ["--plafond-cumule-usd", "50"]
        return base + list(options)

    def environnement(self, role="lecteur_test", plafond="0.5", **sup):
        env = {"PATH": "/usr/bin:/bin", "HOME": self.tmp, "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "TMPDIR": self.tmp,
               "MODELE_DEMANDE_POLE": self.modele, "ROLE_POLE": role}
        if plafond is not None:
            env["PLAFOND_SESSION_USD"] = plafond
        for k, v in sup.items():
            if v is None:
                env.pop(k, None)
            else:
                env[k] = v
        return env

    def lancer(self, env, entree=CONSIGNE, options=(), **kw):
        p = subprocess.run(self.arguments(options, **kw), input=entree.encode("utf-8"), capture_output=True, env=env, timeout=60,
                           cwd=self.tmp)
        return p.returncode, derniere_ligne(p.stdout), p.stderr.decode("utf-8", "replace")

    def max_tokens_recus(self):
        assert len(self.journal) == 1, self.journal
        return self.journal[0]["corps"]["max_tokens"]

    def lignes_registre(self):
        if not os.path.exists(self.registre):
            return []
        return [json.loads(l) for l in open(self.registre, encoding="utf-8") if l.strip()]


@pytest.fixture(params=["kimi", "argon"])
def commande(request, tmp_path):
    r = FauxRelais(request.param)
    try:
        yield Commande(request.param, r, tmp_path)
    finally:
        r.fermer()


@pytest.fixture
def deux(tmp_path):
    """Kimi et Argon, chacun avec son faux relais, sur le **même** registre (même dossier) : la configuration v3 (B1)."""
    rk, ra = FauxRelais("kimi"), FauxRelais("argon")
    try:
        yield Commande("kimi", rk, tmp_path), Commande("argon", ra, tmp_path)
    finally:
        rk.fermer()
        ra.fermer()


def conforme(o, c, role):
    """La dernière ligne telle que l'adaptateur la lit (`lire_derniere_ligne`, `controle_modele`), plus les champs v3 et v4."""
    assert isinstance(o, dict) and isinstance(o["texte"], str)
    assert cout_fini_positif(o)
    assert o["role"] == role and o["version"] == c.version and "envoye" in o


def refus_sans_envoi(code, o, c, cause, role=None):
    """Sortie en code 4 conforme : `cause_refus` attendue (l'une des six), rien envoyé, coût fini > 0, version, rôle."""
    assert code == 4, o
    assert o["cause_refus"] == cause and cause in CAUSES_ATTENDUES, o
    assert o["envoye"] is False and cout_fini_positif(o) and o["version"] == c.version and o["texte"] == "", o
    if role is not None:
        assert o["role"] == role, o


# --- rôles -------------------------------------------------------------------------------------------------------------------


@pytest.mark.parametrize("role", ROLES_ATTENDUS)
def test_chaque_role_permis_accepte(commande, role):
    c = commande
    code, o, err = c.lancer(c.environnement(role=role, plafond="0.5"))
    assert code == 0, (o, err)
    conforme(o, c, role)
    assert o["texte"].startswith("VERDICT: survit") and o["modele_servi"] == c.modele and o["envoye"] is True
    assert o["cout_origine"] == "usage" and o["max_tokens"] == c.journal[0]["corps"]["max_tokens"]
    assert "cause_refus" not in o and o["etape"] is None and o["etape_registre"] is None  # sans porte : aucune étape
    assert len(c.journal) == 1 and c.journal[0]["chemin"] in ("/v1/chat/completions", "/appel")
    lignes = c.lignes_registre()
    assert [l["type"] for l in lignes] == ["debut", "fin"] and lignes[0]["role"] == role and lignes[0]["etape"] is None
    assert lignes[1]["code"] == 0 and lignes[1]["statut"] == "ok" and lignes[1]["cout_usd"] == o["cout_usd"]


def test_role_inconnu_refuse_code_2(commande):
    c = commande
    for role in ("juge", "verificateur", "experimentateur", "", "lecteur"):
        code, o, _ = c.lancer(c.environnement(role=role))
        assert code == 2 and o["envoye"] is False and o["role"] == role and o["version"] == c.version and "refusé" in o["erreur"]
        assert "cause_refus" not in o and cout_fini_positif(o)
    code, o, _ = c.lancer(c.environnement(ROLE_POLE=None))
    assert code == 2 and o["envoye"] is False and o["role"] is None
    assert c.journal == [] and not os.path.exists(c.registre)


# --- réglage et entrée (code 2) ------------------------------------------------------------------------------------------------


def test_modele_demande_different_code_2(commande):
    c = commande
    code, o, _ = c.lancer(c.environnement(role="experimentateur_test", MODELE_DEMANDE_POLE=c.modele + "-autre"))
    assert code == 2 and o["envoye"] is False and "MODELE_DEMANDE_POLE" in o["erreur"] and o["role"] == "experimentateur_test"
    assert c.journal == []
    code, o, _ = c.lancer(c.environnement(role="experimentateur_test", MODELE_DEMANDE_POLE=None))  # sain : variable absente, permis
    assert code == 0 and o["modele_servi"] == c.modele


def test_plafond_session_absent_ou_invalide_code_2(commande):
    c = commande
    for plafond in (None, "", "abc", "0", "-1", "nan", "inf"):
        code, o, _ = c.lancer(c.environnement(role="lecteur_test", plafond=plafond))
        assert code == 2 and o["envoye"] is False and o["role"] == "lecteur_test", plafond
        assert "PLAFOND_SESSION_USD" in o["erreur"] or "float" in o["erreur"], plafond  # chaîne vide : erreur de conversion
    assert c.journal == []


def test_etape_sans_plafond_d_etape_code_2(commande):
    c = commande
    code, o, _ = c.lancer(c.environnement(role="experimentateur_test", ETAPE_POLE=ETAPE))
    assert code == 2 and o["envoye"] is False and "ETAPE_POLE et PLAFOND_ETAPE_USD" in o["erreur"]
    code, o, _ = c.lancer(c.environnement(role="experimentateur_test", PLAFOND_ETAPE_USD="44.00"))
    assert code == 2 and o["envoye"] is False
    code, o, _ = c.lancer(c.environnement(role="experimentateur_test", ETAPE_POLE=ETAPE, PLAFOND_ETAPE_USD="abc"))
    assert code == 2 and o["envoye"] is False
    assert c.journal == []
    code, o, _ = c.lancer(c.environnement(role="experimentateur_test", ETAPE_POLE=ETAPE, PLAFOND_ETAPE_USD="44.00"))  # sain
    assert code == 0 and o["etape"] == ETAPE and o["etape_registre"] == f"{ETAPE}/{c.nom}"  # v4 (1) : valeur reçue / clé
    debut = c.lignes_registre()[0]
    assert debut["etape"] == f"{ETAPE}/{c.nom}" and debut["plafond_etape_usd"] == 44.0 and debut["fournisseur"] == c.nom


def test_consigne_vide_code_2(commande):
    code, o, _ = commande.lancer(commande.environnement(), entree="  \n")
    assert code == 2 and o["envoye"] is False and "vide" in o["erreur"] and commande.journal == []


def test_arguments_obligatoires_absents_code_2(commande):
    """argparse refuse avant toute lecture ; v4 (3) : Argon rend aussi la dernière ligne JSON (Kimi le faisait déjà)."""
    c = commande
    env = c.environnement()
    for kw in ({"registre": False}, {"plafond_cumule": False}, {"registre": False, "plafond_cumule": False}):
        p = subprocess.run(c.arguments(**kw), input=b"consigne", capture_output=True, env=env, timeout=60, cwd=c.tmp)
        o = derniere_ligne(p.stdout)
        assert p.returncode == 2 and b"required" in p.stderr, kw
        assert o is not None and o["envoye"] is False and o["role"] == "lecteur_test" and o["version"] == c.version, (kw, p.stdout)
        assert o["texte"] == "" and cout_fini_positif(o) and "cause_refus" not in o
    assert c.journal == [] and not os.path.exists(c.registre)


@pytest.mark.parametrize("options", [["--option-inconnue", "1"], ["--delai-s", "abc"], ["--sortie-min-jetons-lecteur", "deux"]])
def test_option_refusee_par_argparse_derniere_ligne_json(commande, options):
    """Mineur 1 de la contre-lecture : faute de frappe ou valeur illisible dans la configuration → code 2 et dernière ligne JSON
    (`envoye: false`, `role`, `version`, coût plancher), rien envoyé, rien réservé ; `ROLE_POLE` absent → `role` nul."""
    c = commande
    p = subprocess.run(c.arguments(options), input=CONSIGNE.encode("utf-8"), capture_output=True, env=c.environnement(),
                       timeout=60, cwd=c.tmp)
    o = derniere_ligne(p.stdout)
    assert p.returncode == 2 and o is not None, p.stdout
    assert o["envoye"] is False and o["role"] == "lecteur_test" and o["version"] == c.version and o["texte"] == ""
    assert cout_fini_positif(o) and "cause_refus" not in o
    p = subprocess.run(c.arguments(options), input=b"x", capture_output=True, env=c.environnement(ROLE_POLE=None), timeout=60,
                       cwd=c.tmp)
    o = derniere_ligne(p.stdout)
    assert p.returncode == 2 and o["role"] is None and o["envoye"] is False
    assert c.journal == [] and not os.path.exists(c.registre)


def test_argon_sans_sous_commande_option_refusee_derniere_ligne_json(tmp_path):
    """Sans `appeler` en tête (sous-commande par défaut), même dernière ligne JSON."""
    env = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "HOME": str(tmp_path), "ROLE_POLE": "lecteur_test"}
    p = subprocess.run([PY, "-I", "-B", ARGON, "--option-inconnue"], input=b"x", capture_output=True, env=env, timeout=60,
                       cwd=str(tmp_path))
    o = derniere_ligne(p.stdout)
    assert p.returncode == 2 and o["envoye"] is False and o["role"] == "lecteur_test" and o["version"] == "commande-argon-v56-nuit-v4"


def test_servir_refus_d_argparse_inchange_depuis_la_v3(tmp_path):
    """`servir` : un refus d'argparse sort comme en v3 (code 2, rien sur la sortie standard, même sortie d'erreur au nom du
    fichier près) ; la v4 n'ajoute la dernière ligne JSON qu'à `appeler`."""
    env = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "HOME": str(tmp_path), "ROLE_POLE": "lecteur_test"}
    for args in (["servir"], ["servir", "--port", "abc", "--plafond-usd", "1", "--max-appels", "1", "--journal", "j"],
                 ["servir", "--option-inconnue"]):
        vu = {}
        for nom, chemin in (("v3", ARGON_V3), ("v4", ARGON)):
            p = subprocess.run([PY, "-I", "-B", chemin] + args, capture_output=True, env=env, timeout=60, cwd=str(tmp_path))
            vu[nom] = (p.returncode, p.stdout, p.stderr.replace(os.path.basename(chemin).encode(), b"COMMANDE"))
        assert vu["v4"] == vu["v3"] and vu["v4"][0] == 2 and vu["v4"][1] == b"" and b"usage:" in vu["v4"][2], (args, vu)


def test_url_relais_hors_boucle_locale_code_2(commande):
    c = commande
    for url in ("http://10.0.0.1:8804", "https://127.0.0.1:8804", "http://127.0.0.1:8804/autre"):
        p = subprocess.run(c.arguments(url=False) + ["--url-relais", url], input=b"consigne", capture_output=True, env=c.environnement(),
                           timeout=60, cwd=c.tmp)
        o = derniere_ligne(p.stdout)
        assert p.returncode == 2 and "--url-relais" in o["erreur"] and o["envoye"] is False, url
    assert c.journal == []


# --- sortie maximale et minimale selon le rôle --------------------------------------------------------------------------------


@pytest.mark.parametrize("role, attendu", [("proposeur_ideation", 3000), ("juge_ideation", 2000), ("experimentateur_test", 2000),
                                           ("lecteur_test", 500)])
def test_sortie_maximale_choisie_selon_le_role(commande, role, attendu):
    c = commande
    options = ["--max-sortie-proposeur", "3000", "--max-sortie-court", "2000", "--max-sortie-lecteur", "500",
               "--sortie-min-jetons", "1000", "--sortie-min-jetons-lecteur", "200"]
    code, o, err = c.lancer(c.environnement(role=role, plafond="5"), options=options)  # plafond large : la sortie maximale décide
    assert code == 0, (o, err)
    assert c.max_tokens_recus() == attendu and o["max_tokens"] == attendu


def test_defauts_des_options_par_role(commande):
    """Défauts de l'annexe A : 16 000 / 4 096 (Kimi) et 4 000 / 1 000 (Argon) pour le court ; 1 000 / 200 pour le lecteur."""
    c = commande
    court = 16000 if c.nom == "kimi" else 4000
    code, o, _ = c.lancer(c.environnement(role="experimentateur_test", plafond="5"))
    assert code == 0 and c.max_tokens_recus() == court
    c.journal.clear()
    code, o, _ = c.lancer(c.environnement(role="lecteur_test", plafond="5"))
    assert code == 0 and c.max_tokens_recus() == 1000


def test_sortie_minimale_du_lecteur_est_la_sienne(commande):
    """Entre 200 et la sortie minimale générale (4 096 Kimi, 1 000 Argon), le lecteur passe (code 0) ; sous 200, refus sans envoi."""
    c = commande
    plafond_passe, plafond_refuse = ("0.005", "0.003") if c.nom == "kimi" else ("0.015", "0.005")
    code, o, err = c.lancer(c.environnement(role="lecteur_test", plafond=plafond_passe))
    assert code == 0, (o, err)
    assert 200 <= c.max_tokens_recus() < (4096 if c.nom == "kimi" else 1000)
    c.journal.clear()
    code, o, _ = c.lancer(c.environnement(role="experimentateur_test", plafond=plafond_passe))  # même plafond, rôle au minimum général
    refus_sans_envoi(code, o, c, "plafond_session", "experimentateur_test")
    assert c.journal == []
    code, o, _ = c.lancer(c.environnement(role="lecteur_test", plafond=plafond_refuse))
    refus_sans_envoi(code, o, c, "plafond_session", "lecteur_test")
    assert "plafond de session" in o["erreur"] and c.journal == []
    code, o, _ = c.lancer(c.environnement(role="lecteur_test", plafond=plafond_refuse), options=["--sortie-min-jetons-lecteur", "10"])
    assert code == 0 and c.max_tokens_recus() < 200  # l'option du lecteur est bien celle qui est lue


def test_verificateur_0_10_usd_consigne_courte(commande):
    c = commande
    code, o, err = c.lancer(c.environnement(role="lecteur_test", plafond="0.1"))
    assert code == 0, (o, err)
    conforme(o, c, "lecteur_test")
    assert c.max_tokens_recus() <= 1000 and o["max_tokens"] <= 1000 and o["pire_cas_usd"] <= 0.1


def test_verificateur_0_10_usd_consigne_trop_longue(commande):
    c = commande
    code, o, _ = c.lancer(c.environnement(role="lecteur_test", plafond="0.1"), entree="x" * 60000)
    refus_sans_envoi(code, o, c, "plafond_session", "lecteur_test")
    assert "plafond de session" in o["erreur"]
    assert c.journal == [] and not os.path.exists(c.registre)  # rien envoyé, rien réservé


def test_plafond_session_second_controle_code_4(commande):
    """Second contrôle du pire cas (Kimi : après le point fixe ; Argon : pire cas recalculé) : sortie minimale du lecteur à 0 et
    entrée seule au-dessus du plafond → code 4, cause `plafond_session`, rien envoyé, rien réservé."""
    c = commande
    code, o, _ = c.lancer(c.environnement(role="lecteur_test", plafond="0.001"), entree="x" * 1000,
                          options=["--sortie-min-jetons-lecteur", "0"])
    refus_sans_envoi(code, o, c, "plafond_session", "lecteur_test")
    assert "plafond de session" in o["erreur"] and "caractères" not in o["erreur"] and "octets" not in o["erreur"]  # le second
    assert c.journal == [] and not os.path.exists(c.registre)


def test_experimentateur_reste_de_la_borne(commande):
    """L'expérimentateur reçoit le reste de la borne de 0,80 USD : large → sortie courte entière ; petit → refus sans envoi (code 4,
    cause `plafond_session`, que la version 64 de l'étage lira « budget_depasse »)."""
    c = commande
    code, o, _ = c.lancer(c.environnement(role="experimentateur_test", plafond="0.8"))
    assert code == 0 and c.max_tokens_recus() == (16000 if c.nom == "kimi" else 4000)
    c.journal.clear()
    code, o, _ = c.lancer(c.environnement(role="experimentateur_test", plafond="0.02"))
    refus_sans_envoi(code, o, c, "plafond_session", "experimentateur_test")
    assert c.journal == []


# --- registre cumulé et garde d'étape (code 4) ---------------------------------------------------------------------------------


def test_registre_cumule_plein_code_4(commande):
    c = commande
    reg = charger("registre_v1_essai", REGISTRE_MODULE)
    i = reg.reserver(c.registre, plafond_cumule_usd=50, pire_cas_usd=49.99, fournisseur="autre", role="proposeur_ideation", modele="m")
    reg.regler(c.registre, i, cout_usd=49.99, pire_cas_usd=49.99, statut="ok", code=0, cout_origine="usage")
    code, o, _ = c.lancer(c.environnement(role="lecteur_test", plafond="0.1"))
    refus_sans_envoi(code, o, c, "garde_cumulee", "lecteur_test")
    assert o["erreur"].startswith("garde cumulée")
    assert c.journal == [] and reg.etat(c.registre)["appels"] == 1  # rien réservé
    code, o, _ = c.lancer(c.environnement(role="lecteur_test", plafond="0.1"), options=["--plafond-cumule-usd", "0"])
    refus_sans_envoi(code, o, c, "garde_cumulee", "lecteur_test")  # contrôle d'entrée de la garde cumulée
    assert o["erreur"] == "plafond cumulé invalide"
    code, o, _ = c.lancer(c.environnement(role="lecteur_test", plafond="0.1"), options=["--plafond-cumule-usd", "60"])  # sain
    assert code == 0 and reg.etat(c.registre)["appels"] == 2 and "cause_refus" not in o


def test_registre_illisible_code_4(commande):
    c = commande
    with open(c.registre, "w", encoding="utf-8") as f:
        f.write("ceci n'est pas du JSON\n")
    code, o, _ = c.lancer(c.environnement())
    refus_sans_envoi(code, o, c, "registre_illisible")
    assert "illisible" in o["erreur"] and c.journal == []
    absent = os.path.join(c.tmp, "absent", "registre.jsonl")  # dossier absent : RegistreIllisible
    code, o, _ = c.lancer(c.environnement(), options=["--registre", absent])
    refus_sans_envoi(code, o, c, "registre_illisible")
    assert "dossier du registre absent" in o["erreur"]
    dossier = os.path.join(c.tmp, "un_dossier")  # un dossier à la place du fichier : OSError (IsADirectoryError)
    os.makedirs(dossier)
    code, o, _ = c.lancer(c.environnement(), options=["--registre", dossier])
    refus_sans_envoi(code, o, c, "registre_illisible")
    assert c.journal == []


def test_garde_d_etape_code_4(commande):
    c = commande
    env = c.environnement(role="lecteur_test", plafond="0.1", ETAPE_POLE=ETAPE, PLAFOND_ETAPE_USD="0.001")
    code, o, _ = c.lancer(env)
    refus_sans_envoi(code, o, c, "garde_etape", "lecteur_test")
    assert o["erreur"].startswith(f"garde d'étape ({ETAPE}/{c.nom})") and c.journal == []
    assert o["etape"] == ETAPE and o["etape_registre"] == f"{ETAPE}/{c.nom}"
    env["PLAFOND_ETAPE_USD"] = "6.00"
    code, o, _ = c.lancer(env)  # sain : la part d'Argon
    assert code == 0 and o["etape"] == ETAPE and o["etape_registre"] == f"{ETAPE}/{c.nom}" and "cause_refus" not in o


def test_cause_du_registre_sur_chaque_refus_du_registre_gele(tmp_path):
    """Tous les refus que le registre gelé peut lever, produits par le vrai registre, et la cause que chaque commande en tire :
    préfixe « garde d'étape ( » → `garde_etape` ; autres `PlafondCumule` → `garde_cumulee` (la cumulée est jugée d'abord) ;
    `RegistreIllisible` et `OSError` → `registre_illisible`."""
    k, a = charger("commande_kimi_v4_cause", KIMI), charger("commande_argon_v4_cause", ARGON)
    reg = k.reg
    assert a.reg is reg and inspect.getsourcefile(reg) == REGISTRE_MODULE

    def refus(chemin=str(tmp_path / "r.jsonl"), **kw):
        base = dict(plafond_cumule_usd=50, pire_cas_usd=1.0, fournisseur="essai", role="lecteur_test", modele="m")
        base.update(kw)
        with pytest.raises((reg.PlafondCumule, reg.RegistreIllisible, OSError)) as e:
            reg.reserver(chemin, **base)
        return e.value

    illisible = tmp_path / "illisible.jsonl"
    illisible.write_text("pas du JSON\n", encoding="utf-8")
    (tmp_path / "un_dossier").mkdir()
    cas = [(refus(plafond_cumule_usd=0), "garde_cumulee", "plafond cumulé invalide"),
           (refus(pire_cas_usd=-1.0), "garde_cumulee", "pire cas invalide"),
           (refus(pire_cas_usd=60.0), "garde_cumulee", "garde cumulée : "),
           (refus(etape="E/essai", plafond_etape_usd=0.5), "garde_etape", "garde d'étape (E/essai) : "),
           (refus(pire_cas_usd=60.0, etape="E/essai", plafond_etape_usd=0.5), "garde_cumulee", "garde cumulée : "),
           (refus(chemin=str(tmp_path / "absent" / "r.jsonl")), "registre_illisible", "dossier du registre absent"),
           (refus(chemin=str(illisible)), "registre_illisible", "ligne 1 illisible"),
           (refus(chemin=str(tmp_path / "un_dossier")), "registre_illisible", "")]
    for e, attendu, motif in cas:
        assert motif in str(e) and (str(e).startswith(motif) or motif in ("ligne 1 illisible", "")), (e, motif)
        assert k.cause_du_registre(e) == attendu and a.cause_du_registre(e) == attendu, (e, attendu)
    assert isinstance(cas[-1][0], OSError) and isinstance(cas[-3][0], reg.RegistreIllisible)
    assert k.PREFIXE_GARDE_ETAPE == a.PREFIXE_GARDE_ETAPE == "garde d'étape ("
    assert k.CAUSES_REFUS == a.CAUSES_REFUS == CAUSES_ATTENDUES
    assert k.CAUSES_RELAIS == a.CAUSES_RELAIS == {402: "relais_plafond", 429: "relais_max_appels"}


def test_registre_identique_a_la_v3():
    """Le registre partagé est la copie gelée (même empreinte que la v1 et la v3) : les préfixes lus par `cause_du_registre`
    ne peuvent pas bouger sans que cet essai échoue."""
    with open(REGISTRE_MODULE, "rb") as f:
        assert hashlib.sha256(f.read()).hexdigest() == SHA_REGISTRE


# --- B1 : deux fournisseurs, même registre, même ETAPE_POLE, parts différentes -------------------------------------------------


def kimi_regle(k, montant, part="44.00"):
    """Kimi règle `montant` USD dans l'étape **par la commande elle-même** (faux relais : jetons de sortie = montant / 10e-6),
    sous sa part ; pire cas réservé juste au-dessus du montant."""
    jetons = round(montant * 1e5)
    k.relais.reglage["usage"] = {"prompt_tokens": 0, "completion_tokens": jetons}
    try:
        code, o, err = k.lancer(k.environnement(role="experimentateur_test", plafond=f"{montant + 0.1:.2f}", ETAPE_POLE=ETAPE,
                                                PLAFOND_ETAPE_USD=part), options=["--max-sortie-court", str(jetons + 1000)])
    finally:
        k.relais.reglage.pop("usage")
    assert code == 0 and abs(o["cout_usd"] - montant) < 1e-9 and o["etape_registre"] == f"{ETAPE}/kimi", (o, err)
    return o


def argon_regle(a, montant, part="6.00"):
    """Argon règle `montant` USD dans l'étape par la commande elle-même (faux relais : coût rendu = montant, origine usage)."""
    a.relais.reglage["cout_usd"] = montant
    try:
        code, o, err = a.lancer(a.environnement(role="experimentateur_test", plafond=f"{montant + 0.05:.2f}", ETAPE_POLE=ETAPE,
                                                PLAFOND_ETAPE_USD=part),
                                options=["--max-sortie-court", str(int((montant + 0.025) / 50e-6))])
    finally:
        a.relais.reglage.pop("cout_usd")
    assert code == 0 and abs(o["cout_usd"] - montant) < 1e-9 and o["etape_registre"] == f"{ETAPE}/argon", (o, err)
    return o


def test_b1_depense_de_kimi_hors_de_la_garde_d_etape_d_argon(deux):
    """Expérience E1 de la contre-lecture, en v4 : Kimi a réglé 5,95 USD dans l'étape (part 44) ; le vérificateur d'Argon (part
    6.00, même ETAPE_POLE, même registre) est **accepté** (la v3 le refusait en code 4)."""
    k, a = deux
    kimi_regle(k, 5.95)
    reg = charger("registre_v1_b1", REGISTRE_MODULE)
    e = reg.etat(k.registre, f"{ETAPE}/kimi")
    assert abs(e["etape"]["regle_usd"] - 5.95) < 1e-9 and set(e["par_etape"]) == {f"{ETAPE}/kimi"}
    code, o, err = a.lancer(a.environnement(role="lecteur_test", plafond="0.1", ETAPE_POLE=ETAPE, PLAFOND_ETAPE_USD="6.00"))
    assert code == 0, (o, err)
    assert o["etape"] == ETAPE and o["etape_registre"] == f"{ETAPE}/argon" and len(a.journal) == 1 and "cause_refus" not in o
    debuts = [l for l in k.lignes_registre() if l["type"] == "debut"]
    assert [(d["fournisseur"], d["etape"]) for d in debuts] == [("kimi", f"{ETAPE}/kimi"), ("argon", f"{ETAPE}/argon")]


def test_b1_argon_refuse_sur_sa_propre_part(deux):
    """Argon a lui-même réglé 5,95 USD dans l'étape : son vérificateur (part 6.00) est refusé, code 4, `garde_etape` ; la
    dépense d'Argon n'entre pas dans la garde d'étape de Kimi (Kimi passe sous une part de 1.00, inférieure à 5,95)."""
    k, a = deux
    argon_regle(a, 5.95)
    code, o, _ = a.lancer(a.environnement(role="lecteur_test", plafond="0.1", ETAPE_POLE=ETAPE, PLAFOND_ETAPE_USD="6.00"))
    refus_sans_envoi(code, o, a, "garde_etape", "lecteur_test")
    assert o["erreur"].startswith(f"garde d'étape ({ETAPE}/argon)") and len(a.journal) == 1  # seul l'appel qui a réglé 5,95
    assert o["etape"] == ETAPE and o["etape_registre"] == f"{ETAPE}/argon"
    code, o, err = k.lancer(k.environnement(role="experimentateur_test", plafond="0.8", ETAPE_POLE=ETAPE, PLAFOND_ETAPE_USD="1.00"))
    assert code == 0 and o["etape_registre"] == f"{ETAPE}/kimi", (o, err)


def test_b1_suffixe_idempotent(commande):
    """`ETAPE_POLE=E/<fournisseur>` → clé `E/<fournisseur>`, jamais `E/<fournisseur>/<fournisseur>` ; c'est la **même** clé que
    `ETAPE_POLE=E` (la dépense de l'une compte dans la garde de l'autre) ; seul le suffixe du fournisseur lui-même est reconnu."""
    c = commande
    autre = "argon" if c.nom == "kimi" else "kimi"

    def env(etape, part):
        return c.environnement(role="lecteur_test", plafond="0.1", ETAPE_POLE=etape, PLAFOND_ETAPE_USD=part)
    code, o1, err = c.lancer(env(f"{ETAPE}/{c.nom}", "6.00"))
    assert code == 0, (o1, err)
    assert o1["etape"] == f"{ETAPE}/{c.nom}" and o1["etape_registre"] == f"{ETAPE}/{c.nom}"
    part = f"{o1['pire_cas_usd'] + o1['cout_usd'] / 2:.9f}"  # passe à vide, refusée si la dépense de l'appel 1 compte
    code, o2, _ = c.lancer(env(ETAPE, part))
    refus_sans_envoi(code, o2, c, "garde_etape", "lecteur_test")
    assert o2["etape"] == ETAPE and o2["etape_registre"] == f"{ETAPE}/{c.nom}"
    code, o3, _ = c.lancer(env("une_autre_etape", part))  # témoin : clé neuve, rien de réglé, passe sous la même part
    assert code == 0 and o3["etape_registre"] == f"une_autre_etape/{c.nom}"
    code, o4, _ = c.lancer(env(f"{ETAPE}/{autre}", "6.00"))
    assert code == 0 and o4["etape_registre"] == f"{ETAPE}/{autre}/{c.nom}"
    debuts = [l["etape"] for l in c.lignes_registre() if l["type"] == "debut"]
    assert debuts == [f"{ETAPE}/{c.nom}", f"une_autre_etape/{c.nom}", f"{ETAPE}/{autre}/{c.nom}"]


def test_b1_garde_cumulee_commune(deux):
    """La garde cumulée reste commune aux deux fournisseurs (même registre, `--plafond-cumule-usd 50`) : Kimi a réglé 49,98 USD
    → Argon refusé, `garde_cumulee` (et Kimi lui-même au-delà) ; plafond cumulé relevé → Argon passe."""
    k, a = deux
    kimi_regle(k, 49.98, part="50.00")
    code, o, _ = a.lancer(a.environnement(role="lecteur_test", plafond="0.1", ETAPE_POLE=ETAPE, PLAFOND_ETAPE_USD="6.00"))
    refus_sans_envoi(code, o, a, "garde_cumulee", "lecteur_test")
    assert o["erreur"].startswith("garde cumulée") and a.journal == []
    code, o, _ = k.lancer(k.environnement(role="experimentateur_test", plafond="0.8", ETAPE_POLE=ETAPE, PLAFOND_ETAPE_USD="50.00"))
    refus_sans_envoi(code, o, k, "garde_cumulee", "experimentateur_test")
    code, o, _ = a.lancer(a.environnement(role="lecteur_test", plafond="0.1", ETAPE_POLE=ETAPE, PLAFOND_ETAPE_USD="6.00"),
                          options=["--plafond-cumule-usd", "60"])
    assert code == 0 and len(a.journal) == 1


# --- relais : refus 402 et 429, autres codes, modèle servi, coût d'un échec ------------------------------------------------------


@pytest.mark.parametrize("statut, cause", [(402, "relais_plafond"), (429, "relais_max_appels")])
def test_refus_du_relais_402_429_code_4(commande, statut, cause):
    """Refus du relais lui-même (plafond, nombre d'appels) → code 4, `envoye: false`, coût plancher, `cause_refus` ; Kimi : v4 (3),
    changement de comportement (code 3 en v3). Kimi seulement : une erreur de l'amont transmise telle quelle par le relais (pas
    de signature `relais`), ou un corps illisible, garde le comportement de la v3 : code 3, sans cause."""
    c = commande
    corps = REFUS_SIGNE_KIMI if c.nom == "kimi" else {"erreur": "plafond de dépense du relais Argon"}
    c.relais.reglage.update(statut_http=statut, corps_erreur=corps)
    code, o, _ = c.lancer(c.environnement(role="experimentateur_test", plafond="0.8"))
    refus_sans_envoi(code, o, c, cause, "experimentateur_test")
    assert o["cout_usd"] == 1e-06 and o["cout_origine"] == "plancher" and o["erreur"].startswith(f"HTTP {statut}")
    assert len(c.journal) == 1  # reçu et refusé par le relais : rien n'est parti vers l'amont
    fin = c.lignes_registre()[-1]
    assert fin["type"] == "fin" and fin["code"] == 4 and fin["cout_usd"] == 1e-06 and fin["statut"] == "echec"
    if c.nom == "kimi":
        for corps_amont in (ERREUR_AMONT, b"<html>trop de requetes</html>", {"erreur": "x", "relais": 3}):
            c.relais.reglage["corps_erreur"] = corps_amont
            code, o, _ = c.lancer(c.environnement(role="experimentateur_test", plafond="0.8"))
            assert code == 3 and "cause_refus" not in o and o["erreur"].startswith(f"HTTP {statut}"), (corps_amont, o)
            assert o["envoye"] is False and cout_fini_positif(o)  # comportement de la v3, inchangé


def test_cause_refus_absente_hors_du_code_4(commande):
    """Codes 3 (403 du relais, relais absent) sans `cause_refus` ; les codes 0, 2, 5 et 6 sont vus dans leurs propres essais."""
    c = commande
    c.relais.reglage.update(statut_http=403, corps_erreur={"erreur": "modèle non permis", "relais": "relais-kimi-v3"})
    code, o, _ = c.lancer(c.environnement(role="lecteur_test", plafond="0.1"))
    assert code == 3 and "cause_refus" not in o and o["envoye"] is False and o["erreur"].startswith("HTTP 403")
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()  # port libre, rien n'y écoute : connexion refusée
    p = subprocess.run(c.arguments(url=False) + ["--url-relais", f"http://127.0.0.1:{port}"], input=CONSIGNE.encode("utf-8"),
                       capture_output=True, env=c.environnement(role="lecteur_test", plafond="0.1"), timeout=60, cwd=c.tmp)
    o = derniere_ligne(p.stdout)
    assert p.returncode == 3 and "cause_refus" not in o and o["envoye"] is False and "injoignable" in o["erreur"]


def test_kimi_ecart_de_modele_signale_par_le_relais_code_5(tmp_path):
    """Barrière du modèle servi du relais Kimi (HTTP 502 « modèle servi différent ») : code 5, `modele_servi` =
    « ecart-signale-par-le-relais » (que l'adaptateur lit comme un refus R-764), coût = pire cas réservé, sans `cause_refus` ; un
    autre 502 du relais reste un code 5 sans `modele_servi`. Ce bloc des erreurs HTTP est celui que le point 3 de la v4 touche."""
    r = FauxRelais("kimi")
    try:
        c = Commande("kimi", r, tmp_path)
        r.reglage.update(statut_http=502, corps_erreur={"erreur": "modèle servi différent du modèle demandé (R-764) : réponse non relayée",
                                                        "relais": "relais-kimi-v3", "modele_demande": "kimi-k3.1-pro", "modele_servi": "autre"})
        code, o, _ = c.lancer(c.environnement(role="experimentateur_test", plafond="0.8"))
        assert code == 5 and o["modele_servi"] == "ecart-signale-par-le-relais" and o["envoye"] is True, o
        assert o["cout_usd"] == o["pire_cas_usd"] and o["cout_origine"] == "pire_cas" and "cause_refus" not in o
        r.reglage["corps_erreur"] = {"erreur": "amont coupé après envoi (dépense au pire cas) : TimeoutError", "relais": "relais-kimi-v3"}
        code, o, _ = c.lancer(c.environnement(role="experimentateur_test", plafond="0.8"))
        assert code == 5 and "modele_servi" not in o and o["cout_usd"] == o["pire_cas_usd"] and "cause_refus" not in o, o
        assert [l["code"] for l in c.lignes_registre() if l["type"] == "fin"] == [5, 5]
    finally:
        r.fermer()


def test_modele_servi_different_code_5(commande):
    """Important I2 : le relais répond sous un autre identifiant → code 5, `modele_servi` rendu tel que servi (l'adaptateur en
    fait un refus R-764), coût de l'usage compté, texte non rendu."""
    c = commande
    c.relais.reglage["servi"] = c.modele + "-autre"
    code, o, err = c.lancer(c.environnement(role="lecteur_test", plafond="0.1"))
    assert code == 5, (o, err)
    assert o["modele_servi"] == c.modele + "-autre" and o["envoye"] is True and o["texte"] == "" and "modèle servi" in o["erreur"]
    assert cout_fini_positif(o) and o["cout_origine"] == "usage" and "cause_refus" not in o
    fin = c.lignes_registre()[-1]
    assert fin["type"] == "fin" and fin["code"] == 5 and fin["cout_usd"] == round(o["cout_usd"], 6)


def test_argon_cout_d_un_echec_au_pire_cas_reserve(tmp_path):
    """Important I2 (correction v2, CLM-02) : réponse du relais à `cout_origine = pire_cas` → coût rendu = pire cas **réservé**
    par la commande, exactement (jamais le chiffre du relais) ; aucun dépassement de réserve au registre."""
    r = FauxRelais("argon")
    try:
        c = Commande("argon", r, tmp_path)
        r.reglage.update(cout_origine="pire_cas", cout_usd=lambda d: d["pire_cas_usd"] + 0.01, usage={"entree": 0, "sortie": 0})
        code, o, _ = c.lancer(c.environnement(role="lecteur_test", plafond="0.1"))
        assert code == 5 and o["erreur"] == "usage absent" and o["cout_origine"] == "pire_cas", o
        assert o["cout_usd"] == o["pire_cas_usd"] and "cause_refus" not in o
        debut, fin = c.lignes_registre()
        assert fin["cout_usd"] == debut["pire_cas_usd"] and fin["depassement_reserve"] is False and fin["code"] == 5
        r.reglage["echec"] = "exception : TimeoutError : délai de l'interface"  # échec de transport rendu par le relais
        code, o, _ = c.lancer(c.environnement(role="lecteur_test", plafond="0.1"))
        assert code == 3 and o["cout_usd"] == o["pire_cas_usd"] and "modele_servi" not in o and "cause_refus" not in o
        assert c.lignes_registre()[-1]["depassement_reserve"] is False
    finally:
        r.fermer()


# --- délai dépassé et interruption (code 6, au pire cas) ------------------------------------------------------------------------


def test_delai_depasse_code_6_au_pire_cas(commande):
    """Important I2 : `--delai-s 1` contre un relais qui ne répond pas → code 6, coût = pire cas réservé, ligne `fin` au registre."""
    c = commande
    c.relais.reglage["lenteur_s"] = 30
    t0 = time.time()
    code, o, err = c.lancer(c.environnement(role="lecteur_test", plafond="0.1"), options=["--delai-s", "1"])
    duree = time.time() - t0
    c.relais.liberer.set()
    assert code == 6, (o, err)
    assert o["cout_usd"] == o["pire_cas_usd"] and o["cout_origine"] == "pire_cas" and o["envoye"] is True
    assert o["erreur"].startswith("TimeoutError") and "cause_refus" not in o and duree < 20
    debut, fin = c.lignes_registre()
    assert fin["type"] == "fin" and fin["code"] == 6 and fin["cout_usd"] == debut["pire_cas_usd"]


@pytest.mark.parametrize("sig", [signal.SIGTERM, signal.SIGINT], ids=["SIGTERM", "SIGINT"])
def test_signal_code_6_au_pire_cas(commande, sig):
    """Important I2 : SIGTERM ou SIGINT pendant l'appel (le relais a reçu la requête et ne répond pas) → code 6, coût = pire cas
    réservé, ligne `fin` au registre. Signal envoyé par PID (R10)."""
    c = commande
    c.relais.reglage["lenteur_s"] = 30
    p = subprocess.Popen(c.arguments(["--delai-s", "60"]), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         env=c.environnement(role="experimentateur_test", plafond="0.8"), cwd=c.tmp)
    try:
        p.stdin.write(CONSIGNE.encode("utf-8"))
        p.stdin.close()
        assert c.relais.recu.wait(30), "le faux relais n'a rien reçu"
        p.send_signal(sig)
        sortie, err = p.communicate(timeout=30)
    finally:
        if p.poll() is None:
            p.kill()
            p.wait(timeout=10)
        c.relais.liberer.set()
    o = derniere_ligne(sortie)
    assert p.returncode == 6 and o is not None, (p.returncode, sortie, err)
    assert o["erreur"] == f"signal {int(sig)}" and o["cout_usd"] == o["pire_cas_usd"] and o["cout_origine"] == "pire_cas"
    assert o["envoye"] is True and "cause_refus" not in o
    debut, fin = c.lignes_registre()
    assert fin["type"] == "fin" and fin["code"] == 6 and fin["cout_usd"] == debut["pire_cas_usd"]


# --- interpréteur de la configuration v3 ------------------------------------------------------------------------------------------


def test_commande_sous_usr_bin_python3(commande):
    """Mineur 4 de la contre-lecture : les deux commandes tournent sous `/usr/bin/python3 -I -B` (bibliothèque standard)."""
    c = commande
    p = subprocess.run(c.arguments(interprete=PY_SYSTEME), input=CONSIGNE.encode("utf-8"), capture_output=True,
                       env=c.environnement(role="lecteur_test", plafond="0.1", ETAPE_POLE=ETAPE, PLAFOND_ETAPE_USD="6.00"),
                       timeout=60, cwd=c.tmp)
    o = derniere_ligne(p.stdout)
    assert p.returncode == 0 and o["version"] == c.version and o["etape_registre"] == f"{ETAPE}/{c.nom}", (p.stdout, p.stderr)


# --- aucune clé --------------------------------------------------------------------------------------------------------------


def test_aucune_cle_lue_ni_transmise(commande):
    """Une chaîne témoin posée sous des noms de clé dans l'environnement de la commande (ce que l'orchestrateur ne fait jamais)
    n'apparaît ni dans la requête au relais, ni dans la dernière ligne, ni sur la sortie d'erreur."""
    c = commande
    env = c.environnement(role="lecteur_test", GEMINI_API_KEY=CLE_FACTICE, KIMI_API_KEY=CLE_FACTICE, MOONSHOT_API_KEY=CLE_FACTICE,
                          ANTHROPIC_API_KEY=CLE_FACTICE)
    code, o, err = c.lancer(env)
    assert code == 0
    requete = c.journal[0]
    assert CLE_FACTICE not in requete["brut"].decode("utf-8") and CLE_FACTICE not in json.dumps(requete["entetes"]) + err + json.dumps(o)
    assert not any(k.lower() in ("authorization", "x-api-key", "x-goog-api-key") for k in requete["entetes"])


def test_source_sans_lecture_de_cle():
    kimi = open(KIMI, encoding="utf-8").read()
    assert "API_KEY" not in kimi and "Authorization" not in kimi
    m = charger("commande_argon_v4_essai", ARGON)
    for f in (m.appeler, m.principal, m.rendre, m.verifier_url, m.plafond_etape, m.bornes_de_sortie, m.etape_du_registre,
              m.cause_du_registre):
        assert "API_KEY" not in inspect.getsource(f) and "Authorization" not in inspect.getsource(f)
    assert m.ROLES == ROLES_ATTENDUS and m.VERSION == "commande-argon-v56-nuit-v4"
    k = charger("commande_kimi_v4_essai", KIMI)
    assert k.ROLES == ROLES_ATTENDUS and k.VERSION == "commande-kimi-v4"


# --- relais Argon (`servir`) : identique à la v3, et lecture de ses codes par `appeler` v4 ------------------------------------------


def test_bloc_servir_identique_a_la_v3():
    """Le bloc `servir` (entre ses deux marqueurs) est identique octet pour octet à la v3 ; les constantes et fonctions qu'il lit,
    le sous-analyseur `servir` et son aiguillage dans `principal` aussi ; au-dessus du bloc, hors en-tête, seule `VERSION` change."""
    v3, v4 = open(ARGON_V3, "rb").read(), open(ARGON, "rb").read()
    for t in (v3, v4):  # chaque marqueur est une ligne du code, une seule fois
        assert t.count(MARQUEUR_RELAIS) == 1 and t.count(MARQUEUR_COMMANDE) == 1

    def bloc(t):
        return t[t.index(MARQUEUR_RELAIS):t.index(MARQUEUR_COMMANDE)]

    def entre_en_tete_et_bloc(t):
        return t[t.index(b"\nimport argparse\n"):t.index(MARQUEUR_RELAIS)].decode("utf-8").splitlines()
    assert bloc(v4) == bloc(v3) and len(bloc(v4)) > 8000
    h3, h4 = entre_en_tete_et_bloc(v3), entre_en_tete_et_bloc(v4)
    assert len(h3) == len(h4) and [(a, b) for a, b in zip(h3, h4) if a != b] == [
        ('VERSION = "commande-argon-v56-nuit-v3"', 'VERSION = "commande-argon-v56-nuit-v4"')]
    m3, m4 = charger("commande_argon_v3_identite", ARGON_V3), charger("commande_argon_v4_identite", ARGON)
    for nom in ("pire_cas", "maintenant", "charger_collisionneur", "statut_et_cout", "fabriquer_gestion", "servir"):
        assert inspect.getsource(getattr(m3, nom)) == inspect.getsource(getattr(m4, nom)), nom
    for nom in ("HOTE", "COLLISIONNEUR_DEFAUT", "SHA_COLLISIONNEUR", "PRIX", "MAX_OCTETS_CORPS", "PLANCHER", "ROLES"):
        assert getattr(m3, nom) == getattr(m4, nom), nom

    def servir_dans_principal(m):
        return [l for l in inspect.getsource(m.principal).splitlines() if 's.add_argument(' in l or '"servir"' in l
                or "args.port <= 0" in l or "return servir(args)" in l or "strictement positifs" in l]
    l4 = servir_dans_principal(m4)
    assert l4.count('        if argv[0] == "servir":') == 1  # v4 (3) : seul ajout, qui relève tel quel le refus d'argparse
    l4.remove('        if argv[0] == "servir":')
    assert l4 == servir_dans_principal(m3) and len(l4) == 13


class _Reponse:
    def __init__(self, texte=None, modele_servi=None, fin=None, usage=None, echec=None, categorie=None):
        self.texte, self.modele_servi, self.fin, self.usage, self.echec, self.categorie = texte, modele_servi, fin, usage, echec, categorie


class _Collisionneur:
    """Doublure minimale du collisionneur v7 pour `fabriquer_gestion` (sans réseau) : `Reponse`, `statut_reponse`, `cout`."""
    Reponse = _Reponse

    @staticmethod
    def statut_reponse(fournisseur, rep):
        return "OK" if rep.texte else "VIDE"

    @staticmethod
    def cout(prix, usage):
        return usage["entree"] / 1e6 * prix[0] + usage["sortie"] / 1e6 * prix[1]


@pytest.fixture
def relais_argon_reel(tmp_path):
    """Le vrai gestionnaire de `servir` (v4, identique à la v3), appelant factice, sans clé : plafond et nombre d'appels réglables."""
    m = charger("commande_argon_v4_relais", ARGON)
    reglage = {"plafond": 10.0, "max_appels": 10}
    tenus = []

    def appelant(modele, prompt, mt):
        return _Reponse(texte="réponse", modele_servi="gemini-4-argon", fin="STOP", usage={"entree": 10, "sortie": 5})

    def demarrer():
        e = m.EtatRelais(reglage["plafond"], reglage["max_appels"], ["gemini-4-argon"], str(tmp_path / "journal.jsonl"), m.SHA_COLLISIONNEUR)
        e.nature_appelant = "essai"
        s = ThreadingHTTPServer(("127.0.0.1", 0), m.fabriquer_gestion(e, appelant, _Collisionneur, str))
        threading.Thread(target=s.serve_forever, daemon=True).start()
        tenus.append(s)
        return f"http://127.0.0.1:{s.server_address[1]}"
    yield demarrer, reglage, m
    for s in tenus:
        s.shutdown()
        s.server_close()


def test_servir_codes_402_429_411_413_inchanges(tmp_path, relais_argon_reel):
    import http.client
    import urllib.request
    demarrer, reglage, m = relais_argon_reel
    reglage["plafond"], reglage["max_appels"] = 0.05, 1  # sous le pire cas d'un appel du lecteur (≥ 0,01 USD + entrée) : 402
    url = demarrer()
    c = Commande("argon", None, tmp_path, url=url)
    code, o, _ = c.lancer(c.environnement(role="lecteur_test", plafond="0.1"))
    refus_sans_envoi(code, o, c, "relais_plafond", "lecteur_test")
    assert o["erreur"].startswith("HTTP 402")
    reglage["plafond"], reglage["max_appels"] = 10.0, 1
    url2 = demarrer()
    c2 = Commande("argon", None, tmp_path, url=url2)
    code, o, _ = c2.lancer(c2.environnement(role="lecteur_test", plafond="0.1"))
    assert code == 0 and o["modele_servi"] == "gemini-4-argon"  # sain : premier appel
    code, o, _ = c2.lancer(c2.environnement(role="lecteur_test", plafond="0.1"))
    refus_sans_envoi(code, o, c2, "relais_max_appels", "lecteur_test")
    assert o["erreur"].startswith("HTTP 429")
    hote, port = url2[len("http://"):].split(":")
    for entetes, attendu in (({}, 411), ({"Content-Length": str(m.MAX_OCTETS_CORPS + 1)}, 413)):  # en-têtes écrits à la main
        conn = http.client.HTTPConnection(hote, int(port), timeout=5)
        try:  # la connexion est toujours fermée : un relais muté qui lirait un corps absent resterait bloqué, et le serveur avec lui
            conn.putrequest("POST", "/appel")
            conn.putheader("Content-Type", "application/json")
            for k, v in entetes.items():
                conn.putheader(k, v)
            conn.endheaders()
            assert conn.getresponse().status == attendu
        finally:
            conn.close()
    ouvreur = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    with ouvreur.open(url2 + "/relais/etat", timeout=5) as rep:
        etat = json.loads(rep.read())
    assert etat["reprise_interne"] == "aucune (attentes=(0,))" and etat["cle_presente"] is False and etat["appels"] == 1
    journal = [json.loads(l) for l in open(tmp_path / "journal.jsonl", encoding="utf-8")]
    assert len(journal) == 1 and "texte" not in journal[0] and journal[0]["statut"] == "OK"


def test_servir_refuse_sans_cle_et_sans_collisionneur_conforme(tmp_path):
    import argparse
    m = charger("commande_argon_v4_servir", ARGON)
    faux = tmp_path / "collisionneur_factice.py"
    faux.write_text("# pas le collisionneur v7\n", encoding="utf-8")
    a = argparse.Namespace(port=0, plafond_usd=1.0, max_appels=1, journal=str(tmp_path / "j"), modeles_permis="gemini-4-argon",
                           collisionneur=str(faux), sha_collisionneur=m.SHA_COLLISIONNEUR)
    with pytest.raises(SystemExit, match="empreinte"):  # collisionneur à empreinte différente : refus de servir, avant toute clé
        m.servir(a, environ={"GEMINI_API_KEY": CLE_FACTICE})
    with pytest.raises(SystemExit, match="GEMINI_API_KEY absente"):
        m.servir(a, c=_Collisionneur, environ={})
