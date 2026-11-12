"""Essais des commandes externes v3 du tour fermé, étage 1 (TF-01) : `commande_kimi_v3.py` et `commande_argon_v56_nuit_v3.py`
(sous-commande `appeler`), sans réseau, sans clé, sans dépense. Rédigés le 2 novembre 2026 (sous-agent de session-depot).

Chaque commande est lancée comme en production (`python -I -B`, environnement minimal de `AdaptateurCommandeExterne`,
consigne sur l'entrée standard) contre un **faux relais local** en processus (boucle locale, port éphémère), qui consigne chaque
requête reçue : on y lit `max_tokens`, et l'absence de toute clé. Aucun appel vers l'extérieur, aucun modèle.

    cd docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1 && nice -n 10 /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider test_commandes_tour_ferme_v3.py
"""

import importlib.util
import inspect
import json
import os
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

import pytest

ICI = os.path.dirname(os.path.abspath(__file__))
PY = "/home/user/controle-ia-travail/.venv/bin/python" if os.path.exists("/home/user/controle-ia-travail/.venv/bin/python") else sys.executable
KIMI, ARGON = os.path.join(ICI, "commande_kimi_v3.py"), os.path.join(ICI, "commande_argon_v56_nuit_v3.py")
ROLES_ATTENDUS = ("proposeur_ideation", "juge_ideation", "experimentateur_test", "lecteur_test")
CLE_FACTICE = "cle-factice-0123456789abcdef"  # jamais une clé : une chaîne témoin, cherchée dans ce que reçoit le faux relais


def charger(nom, chemin):
    """Importe un module de ce dossier par son chemin (sans le lancer : `__name__` ≠ `__main__`)."""
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# --- faux relais -------------------------------------------------------------------------------------------------------------


def fabriquer_faux_relais(fournisseur, journal, reglage):
    """Relais factice : `/v1/chat/completions` (façon relais Kimi) ou `/appel` (façon relais Argon) ; chaque requête reçue va au
    journal (chemin, en-têtes, corps) ; réponse conforme, texte d'une ligne."""
    class G(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_POST(self):
            corps = self.rfile.read(int(self.headers["Content-Length"]))
            d = json.loads(corps)
            journal.append({"chemin": self.path, "entetes": {k: v for k, v in self.headers.items()}, "corps": d, "brut": corps})
            if fournisseur == "kimi":
                attendu, rep = "/v1/chat/completions", {
                    "model": reglage.get("servi") or d["model"],
                    "choices": [{"message": {"content": "VERDICT: survit ; chiffre: 1.5 ; ligne: RESULTAT: 1.5"}, "finish_reason": "stop"}],
                    "usage": {"prompt_tokens": 10, "completion_tokens": 5}}
            else:
                attendu, rep = "/appel", {
                    "texte": "VERDICT: survit ; chiffre: 1.5 ; ligne: RESULTAT: 1.5", "modele_servi": reglage.get("servi") or d["modele"],
                    "fin": "STOP", "categorie": None, "statut": "OK", "usage": {"entree": 10, "sortie": 5}, "cout_usd": 0.00035,
                    "cout_origine": "usage", "pire_cas_relais_usd": d["pire_cas_usd"], "echec": None, "duree_s": 0.1}
            code = 200 if self.path == attendu else 404
            b = json.dumps(rep if code == 200 else {"erreur": "chemin"}, ensure_ascii=False).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(b)))
            self.end_headers()
            self.wfile.write(b)
    return G


class Commande:
    """Une commande sous essai : lancement comme en production, faux relais, lecture de la dernière ligne."""

    def __init__(self, nom, url, journal, reglage, tmp):
        self.nom, self.url, self.journal, self.reglage, self.tmp = nom, url, journal, reglage, str(tmp)
        self.modele = "kimi-k3.1-pro" if nom == "kimi" else "gemini-4-argon"
        self.version = "commande-kimi-v3" if nom == "kimi" else "commande-argon-v56-nuit-v3"
        self.registre = os.path.join(self.tmp, "registre.jsonl")

    def arguments(self, options=(), registre=True, plafond_cumule=True, url=True):
        base = [PY, "-I", "-B", KIMI] if self.nom == "kimi" else [PY, "-I", "-B", ARGON, "appeler"]
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

    def lancer(self, env, entree="Réponds seulement par VERDICT: survit ; chiffre: 1.5 ; ligne: RESULTAT: 1.5", options=(), **kw):
        p = subprocess.run(self.arguments(options, **kw), input=entree.encode("utf-8"), capture_output=True, env=env, timeout=60,
                           cwd=self.tmp)
        lignes = [l for l in p.stdout.decode("utf-8", "replace").splitlines() if l.strip()]
        objet = json.loads(lignes[-1]) if lignes else None
        return p.returncode, objet, p.stderr.decode("utf-8", "replace")

    def max_tokens_recus(self):
        assert len(self.journal) == 1, self.journal
        return self.journal[0]["corps"]["max_tokens"]


@pytest.fixture(params=["kimi", "argon"])
def commande(request, tmp_path):
    journal, reglage = [], {}
    s = HTTPServer(("127.0.0.1", 0), fabriquer_faux_relais(request.param, journal, reglage))
    threading.Thread(target=s.serve_forever, daemon=True).start()
    try:
        yield Commande(request.param, f"http://127.0.0.1:{s.server_address[1]}", journal, reglage, tmp_path)
    finally:
        s.shutdown()
        s.server_close()


def conforme(o, c, role):
    """La dernière ligne telle que l'adaptateur la lit (`lire_derniere_ligne`, `controle_modele`), plus les champs v3."""
    assert isinstance(o, dict) and isinstance(o["texte"], str)
    assert isinstance(o["cout_usd"], float) and o["cout_usd"] > 0
    assert o["role"] == role and o["version"] == c.version and "envoye" in o


# --- rôles -------------------------------------------------------------------------------------------------------------------


@pytest.mark.parametrize("role", ROLES_ATTENDUS)
def test_chaque_role_permis_accepte(commande, role):
    c = commande
    code, o, err = c.lancer(c.environnement(role=role, plafond="0.5"))
    assert code == 0, (o, err)
    conforme(o, c, role)
    assert o["texte"].startswith("VERDICT: survit") and o["modele_servi"] == c.modele and o["envoye"] is True
    assert o["cout_origine"] == "usage" and o["max_tokens"] == c.journal[0]["corps"]["max_tokens"]
    assert len(c.journal) == 1 and c.journal[0]["chemin"] in ("/v1/chat/completions", "/appel")
    lignes = [json.loads(l) for l in open(c.registre, encoding="utf-8")]
    assert [l["type"] for l in lignes] == ["debut", "fin"] and lignes[0]["role"] == role
    assert lignes[1]["code"] == 0 and lignes[1]["statut"] == "ok" and lignes[1]["cout_usd"] == o["cout_usd"]


def test_role_inconnu_refuse_code_2(commande):
    c = commande
    for role in ("juge", "verificateur", "experimentateur", "", "lecteur"):
        code, o, _ = c.lancer(c.environnement(role=role))
        assert code == 2 and o["envoye"] is False and o["role"] == role and o["version"] == c.version and "refusé" in o["erreur"]
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
    code, o, _ = c.lancer(c.environnement(role="experimentateur_test", ETAPE_POLE="tour_ferme_v63"))
    assert code == 2 and o["envoye"] is False and "ETAPE_POLE et PLAFOND_ETAPE_USD" in o["erreur"]
    code, o, _ = c.lancer(c.environnement(role="experimentateur_test", PLAFOND_ETAPE_USD="44.00"))
    assert code == 2 and o["envoye"] is False
    code, o, _ = c.lancer(c.environnement(role="experimentateur_test", ETAPE_POLE="tour_ferme_v63", PLAFOND_ETAPE_USD="abc"))
    assert code == 2 and o["envoye"] is False
    assert c.journal == []
    code, o, _ = c.lancer(c.environnement(role="experimentateur_test", ETAPE_POLE="tour_ferme_v63", PLAFOND_ETAPE_USD="44.00"))  # sain
    assert code == 0 and o["etape"] == "tour_ferme_v63"
    debut = json.loads(open(c.registre, encoding="utf-8").readline())
    assert debut["etape"] == "tour_ferme_v63" and debut["plafond_etape_usd"] == 44.0


def test_consigne_vide_code_2(commande):
    code, o, _ = commande.lancer(commande.environnement(), entree="  \n")
    assert code == 2 and o["envoye"] is False and "vide" in o["erreur"] and commande.journal == []


def test_arguments_obligatoires_absents_code_2(commande):
    c = commande
    env = c.environnement()
    for kw in ({"registre": False}, {"plafond_cumule": False}, {"registre": False, "plafond_cumule": False}):
        p = subprocess.run(c.arguments(**kw), input=b"consigne", capture_output=True, env=env, timeout=60, cwd=c.tmp)
        assert p.returncode == 2 and b"required" in p.stderr, kw  # argparse : refus avant toute lecture
    assert c.journal == []


def test_url_relais_hors_boucle_locale_code_2(commande):
    c = commande
    for url in ("http://10.0.0.1:8804", "https://127.0.0.1:8804", "http://127.0.0.1:8804/autre"):
        p = subprocess.run(c.arguments(url=False) + ["--url-relais", url], input=b"consigne", capture_output=True, env=c.environnement(),
                           timeout=60, cwd=c.tmp)
        o = json.loads(p.stdout.decode().strip().splitlines()[-1])
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
    assert code == 4 and o["envoye"] is False and o["role"] == "experimentateur_test" and c.journal == []
    code, o, _ = c.lancer(c.environnement(role="lecteur_test", plafond=plafond_refuse))
    assert code == 4 and o["envoye"] is False and o["role"] == "lecteur_test" and "plafond de session" in o["erreur"]
    assert c.journal == []
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
    assert code == 4 and o["envoye"] is False and o["role"] == "lecteur_test" and "plafond de session" in o["erreur"]
    assert c.journal == [] and not os.path.exists(c.registre)  # rien envoyé, rien réservé


def test_experimentateur_reste_de_la_borne(commande):
    """L'expérimentateur reçoit le reste de la borne de 0,80 USD : large → sortie courte entière ; petit → refus sans envoi (code 4,
    que l'adaptateur rend « erreur » : TF-02, voir le LISEZMOI)."""
    c = commande
    code, o, _ = c.lancer(c.environnement(role="experimentateur_test", plafond="0.8"))
    assert code == 0 and c.max_tokens_recus() == (16000 if c.nom == "kimi" else 4000)
    c.journal.clear()
    code, o, _ = c.lancer(c.environnement(role="experimentateur_test", plafond="0.02"))
    assert code == 4 and o["envoye"] is False and c.journal == []


# --- registre cumulé et garde d'étape (code 4) ---------------------------------------------------------------------------------


def test_registre_cumule_plein_code_4(commande):
    c = commande
    reg = charger("registre_v1_essai", os.path.join(ICI, "registre_depense_cumulee_v1.py"))
    i = reg.reserver(c.registre, plafond_cumule_usd=50, pire_cas_usd=49.99, fournisseur="autre", role="proposeur_ideation", modele="m")
    reg.regler(c.registre, i, cout_usd=49.99, pire_cas_usd=49.99, statut="ok", code=0, cout_origine="usage")
    code, o, _ = c.lancer(c.environnement(role="lecteur_test", plafond="0.1"))
    assert code == 4 and o["envoye"] is False and o["erreur"].startswith("garde cumulée") and o["role"] == "lecteur_test"
    assert c.journal == [] and reg.etat(c.registre)["appels"] == 1  # rien réservé
    code, o, _ = c.lancer(c.environnement(role="lecteur_test", plafond="0.1"), options=["--plafond-cumule-usd", "60"])  # sain
    assert code == 0 and reg.etat(c.registre)["appels"] == 2


def test_registre_illisible_code_4(commande):
    c = commande
    with open(c.registre, "w", encoding="utf-8") as f:
        f.write("ceci n'est pas du JSON\n")
    code, o, _ = c.lancer(c.environnement())
    assert code == 4 and o["envoye"] is False and "illisible" in o["erreur"] and c.journal == []


def test_garde_d_etape_code_4(commande):
    c = commande
    env = c.environnement(role="lecteur_test", plafond="0.1", ETAPE_POLE="tour_ferme_v63", PLAFOND_ETAPE_USD="0.001")
    code, o, _ = c.lancer(env)
    assert code == 4 and o["envoye"] is False and o["erreur"].startswith("garde d'étape") and c.journal == []
    env["PLAFOND_ETAPE_USD"] = "6.00"
    code, o, _ = c.lancer(env)  # sain : la part d'Argon
    assert code == 0 and o["etape"] == "tour_ferme_v63"


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
    m = charger("commande_argon_v3_essai", ARGON)
    for f in (m.appeler, m.principal, m.rendre, m.verifier_url, m.plafond_etape, m.bornes_de_sortie):
        assert "API_KEY" not in inspect.getsource(f) and "Authorization" not in inspect.getsource(f)
    assert m.ROLES == ROLES_ATTENDUS and m.VERSION == "commande-argon-v56-nuit-v3"
    k = charger("commande_kimi_v3_essai", KIMI)
    assert k.ROLES == ROLES_ATTENDUS and k.VERSION == "commande-kimi-v3"


# --- relais Argon (`servir`) : comportement inchangé, et lecture de ses codes par `appeler` v3 --------------------------------------


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
    """Le vrai gestionnaire de `servir` (v3, inchangé de la v2), appelant factice, sans clé : plafond et nombre d'appels réglables."""
    m = charger("commande_argon_v3_relais", ARGON)
    reglage = {"plafond": 10.0, "max_appels": 10}
    tenu = {}

    def appelant(modele, prompt, mt):
        return _Reponse(texte="réponse", modele_servi="gemini-4-argon", fin="STOP", usage={"entree": 10, "sortie": 5})

    def demarrer():
        e = m.EtatRelais(reglage["plafond"], reglage["max_appels"], ["gemini-4-argon"], str(tmp_path / "journal.jsonl"), m.SHA_COLLISIONNEUR)
        e.nature_appelant = "essai"
        s = HTTPServer(("127.0.0.1", 0), m.fabriquer_gestion(e, appelant, _Collisionneur, str))
        threading.Thread(target=s.serve_forever, daemon=True).start()
        tenu["s"] = s
        return f"http://127.0.0.1:{s.server_address[1]}"
    yield demarrer, reglage, m
    if "s" in tenu:
        tenu["s"].shutdown()
        tenu["s"].server_close()


def test_servir_codes_402_429_411_413_inchanges(tmp_path, relais_argon_reel):
    import urllib.request
    demarrer, reglage, m = relais_argon_reel
    reglage["plafond"], reglage["max_appels"] = 0.05, 1  # sous le pire cas d'un appel du lecteur (≥ 0,01 USD + entrée) : 402 ; 1 appel : 429
    url = demarrer()
    c = Commande("argon", url, [], {}, tmp_path)
    code, o, _ = c.lancer(c.environnement(role="lecteur_test", plafond="0.1"))
    assert code == 4 and o["erreur"].startswith("HTTP 402") and o["envoye"] is False and o["role"] == "lecteur_test"
    reglage_large = (10.0, 1)
    reglage["plafond"], reglage["max_appels"] = reglage_large
    url2 = demarrer()
    c2 = Commande("argon", url2, [], {}, tmp_path)
    code, o, _ = c2.lancer(c2.environnement(role="lecteur_test", plafond="0.1"))
    assert code == 0 and o["modele_servi"] == "gemini-4-argon"  # sain : premier appel
    code, o, _ = c2.lancer(c2.environnement(role="lecteur_test", plafond="0.1"))
    assert code == 4 and o["erreur"].startswith("HTTP 429") and o["envoye"] is False
    import http.client
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
    m = charger("commande_argon_v3_servir", ARGON)
    faux = tmp_path / "collisionneur_factice.py"
    faux.write_text("# pas le collisionneur v7\n", encoding="utf-8")
    a = argparse.Namespace(port=0, plafond_usd=1.0, max_appels=1, journal=str(tmp_path / "j"), modeles_permis="gemini-4-argon",
                           collisionneur=str(faux), sha_collisionneur=m.SHA_COLLISIONNEUR)
    with pytest.raises(SystemExit, match="empreinte"):  # collisionneur à empreinte différente : refus de servir, avant toute clé
        m.servir(a, environ={"GEMINI_API_KEY": CLE_FACTICE})
    with pytest.raises(SystemExit, match="GEMINI_API_KEY absente"):
        m.servir(a, c=_Collisionneur, environ={})
