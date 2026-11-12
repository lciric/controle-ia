"""Essais de `commande_argon_v1.py` contre un **faux serveur local** (127.0.0.1, port libre) : aucun réseau sortant, aucune
vraie clé, aucun appel payant. Le dernier essai lance la commande par l'**adaptateur réel de la v43**
(`AdaptateurCommandeExterne`, `pole/adaptateurs.py` de l'arbre v43 copié, empreinte vérifiée contre la liste de la v43).

Lancer : `python -m pytest -q test_commande_argon_v1.py` (environnement /home/user/controle-ia-travail/.venv).
Arbre v43 : variable `ORCHESTRATEUR_V43` (dossier `orchestrateur-pole-v7`), sinon la copie de travail à côté de ce fichier.
"""

import hashlib
import json
import math
import os
import signal
import subprocess
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest

ICI = os.path.dirname(os.path.abspath(__file__))
COMMANDE = os.path.join(ICI, "commande_argon_v1.py")
V43 = os.environ.get("ORCHESTRATEUR_V43") or os.path.join(ICI, "travail", "v43-copie", "orchestrateur-pole-v7")
CLE = "cle-factice-AIzaTEST-0123456789-ne-jamais-imprimer"
PRIX_E, PRIX_S = 8.3e-6, 41.5e-6


# --- faux serveur ----------------------------------------------------------------------------------------------------

class FauxGemini:
    """Répond selon `mode` ; consigne chaque requête (chemin, en-têtes, corps)."""

    def __init__(self):
        self.mode = "sain"
        self.requetes = []
        self.total_tokens = None
        self.attente_s = 0.0
        faux = self

        class Gestion(BaseHTTPRequestHandler):
            def log_message(self, *a):
                pass

            def do_POST(self):
                n = int(self.headers.get("Content-Length") or 0)
                corps = json.loads(self.rfile.read(n).decode("utf-8"))
                faux.requetes.append({"chemin": self.path, "cle": self.headers.get("x-goog-api-key"), "corps": corps})
                if self.path.endswith(":countTokens"):
                    return self.repondre(200, {"totalTokens": faux.total_tokens})
                if faux.attente_s:
                    time.sleep(faux.attente_s)
                code, obj = faux.reponse()
                self.repondre(code, obj)

            def repondre(self, code, obj):
                brut = json.dumps(obj).encode("utf-8")
                try:
                    self.send_response(code)
                    self.send_header("Content-Type", "application/json")
                    self.send_header("Content-Length", str(len(brut)))
                    self.end_headers()
                    self.wfile.write(brut)
                except (BrokenPipeError, ConnectionResetError):
                    pass

        self.serveur = ThreadingHTTPServer(("127.0.0.1", 0), Gestion)
        self.serveur.daemon_threads = True
        self.url = f"http://127.0.0.1:{self.serveur.server_address[1]}/v1beta"
        threading.Thread(target=self.serveur.serve_forever, daemon=True).start()

    USAGE = {"promptTokenCount": 1000, "candidatesTokenCount": 10, "thoughtsTokenCount": 5, "totalTokenCount": 1015}

    def reponse(self):
        candidat = {"content": {"role": "model", "parts": [{"text": "OK"}]}, "finishReason": "STOP"}
        base = {"modelVersion": "gemini-4-argon", "responseId": "r1", "usageMetadata": dict(self.USAGE)}
        m = self.mode
        if m == "sain":
            return 200, dict(base, candidates=[candidat])
        if m == "vide":
            return 200, dict(base, candidates=[{"content": {"parts": [{"text": ""}]}, "finishReason": "STOP"}])
        if m == "sans_candidat":
            return 200, dict(base, candidates=[])
        if m == "usage_absent":
            b = dict(base, candidates=[candidat])
            del b["usageMetadata"]
            return 200, b
        if m == "tronquee":
            return 200, dict(base, candidates=[dict(candidat, finishReason="MAX_TOKENS")])
        if m == "bloquee":
            return 200, dict(base, candidates=[dict(candidat, finishReason="SAFETY")])
        if m == "autre_modele":
            return 200, dict(base, candidates=[candidat], modelVersion="gemini-3-pro")
        if m == "outil":
            return 200, dict(base, candidates=[{"content": {"parts": [{"functionCall": {"name": "lire"}}]},
                                                "finishReason": "STOP"}])
        if m == "http500":
            return 500, {"error": {"code": 500, "message": "panne ; clé reçue " + CLE}}
        if m == "http400":
            return 400, {"error": {"code": 400, "message": "requête refusée ; clé " + CLE}}
        raise AssertionError(m)

    def generations(self):
        return [r for r in self.requetes if r["chemin"].endswith(":generateContent")]

    def arreter(self):
        self.serveur.shutdown()
        self.serveur.server_close()


@pytest.fixture
def serveur():
    s = FauxGemini()
    yield s
    s.arreter()


def env_commande(plafond="3.1", role="proposeur_ideation", cle=CLE):
    env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "LANG": "C.UTF-8"}
    if plafond is not None:
        env["PLAFOND_SESSION_USD"] = plafond
    if role is not None:
        env["ROLE_POLE"] = role
    if cle is not None:
        env["GEMINI_API_KEY"] = cle
    return env


def lancer(serveur, consigne="x" * 4000, args=(), env=None, delai_test=60):
    p = subprocess.run([sys.executable, "-I", "-B", COMMANDE, "--url-base", serveur.url, *args],
                       input=consigne.encode("utf-8"), capture_output=True, env=env or env_commande(),
                       timeout=delai_test)
    lignes = [l for l in p.stdout.decode("utf-8").splitlines() if l.strip()]
    objet = json.loads(lignes[-1])
    sortie_complete = p.stdout.decode("utf-8") + p.stderr.decode("utf-8")
    assert CLE not in sortie_complete, "la clé ne sort jamais"
    return p.returncode, objet, p.stderr.decode("utf-8")


def contrat(objet):
    """Contrat du noyau : texte chaîne, coût fini strictement positif."""
    assert isinstance(objet["texte"], str)
    c = objet["cout_usd"]
    assert isinstance(c, float) and math.isfinite(c) and c > 0


COUT_SAIN = 1000 * PRIX_E + 15 * PRIX_S


# --- cas sain ----------------------------------------------------------------------------------------------------------

def test_cas_sain(serveur):
    code, o, err = lancer(serveur)
    assert code == 0 and err == ""
    contrat(o)
    assert o["texte"] == "OK" and o["cout_origine"] == "usage" and o["envoye"] is True
    assert o["cout_usd"] == pytest.approx(COUT_SAIN)
    assert o["modele_servi"] == "gemini-4-argon" and o["role"] == "proposeur_ideation"
    (r,) = serveur.generations()
    assert r["chemin"] == "/v1beta/models/gemini-4-argon:generateContent" and r["cle"] == CLE
    assert set(r["corps"]) == {"contents", "generationConfig"}, "aucun outil, aucune fonction, aucune consigne système"
    assert r["corps"]["contents"] == [{"role": "user", "parts": [{"text": "x" * 4000}]}]
    # sortie bornée par le plafond : min(65536, (3,1 − 0,0083) / 41,5e-6)
    assert r["corps"]["generationConfig"] == {"maxOutputTokens": 65536}
    assert o["pire_cas_usd"] <= 3.1


def test_sortie_bornee_par_le_reste_du_plafond(serveur):
    # 1 077 663 caractères (contrôle réel de la course mesuré) à 3,1 : entrée 2,236, reste ≈ 20 818 jetons de sortie
    consigne = "y" * 1_077_663
    code, o, _ = lancer(serveur, consigne=consigne)
    assert code == 0
    (r,) = serveur.generations()
    attendu = math.floor((3.1 - math.ceil(1_077_663 / 4) * PRIX_E) / PRIX_S)
    assert r["corps"]["generationConfig"]["maxOutputTokens"] == attendu
    assert 20_000 < attendu < 21_000
    assert o["pire_cas_usd"] <= 3.1 + 1e-9


def test_juge_role_transmis(serveur):
    code, o, _ = lancer(serveur, env=env_commande(plafond="3.3", role="juge_ideation"))
    assert code == 0 and o["role"] == "juge_ideation"


# --- refus de pire cas -------------------------------------------------------------------------------------------------

def test_refus_de_pire_cas_sans_envoi(serveur):
    code, o, err = lancer(serveur, env=env_commande(plafond="0.01"))
    assert code == 4
    contrat(o)
    assert serveur.requetes == [], "rien n'est envoyé"
    assert o["envoye"] is False and o["cout_origine"] == "plancher" and o["cout_usd"] == 1e-6
    assert "pire cas" in o["erreur"] and "rien envoyé" in o["erreur"] and "pire cas" in err


def test_refus_de_pire_cas_au_compte_exact(serveur):
    # estimation 1000 jetons ; countTokens dit 380 000 : l'entrée seule (3,154) dépasse 3,1 → refus, aucune génération
    serveur.total_tokens = 380_000
    code, o, _ = lancer(serveur, args=["--compter-jetons"])
    assert code == 4 and serveur.generations() == [] and len(serveur.requetes) == 1
    assert o["entree_jetons_comptee"] == 380_000 and o["envoye"] is False


def test_compte_exact_reduit_la_sortie(serveur):
    serveur.total_tokens = 200_000
    code, o, _ = lancer(serveur, args=["--compter-jetons"])
    assert code == 0
    (r,) = serveur.generations()
    assert r["corps"]["generationConfig"]["maxOutputTokens"] == min(65536, math.floor((3.1 - 200_000 * PRIX_E) / PRIX_S))


# --- réponses non conformes --------------------------------------------------------------------------------------------

@pytest.mark.parametrize("mode,motif", [("vide", "réponse vide"), ("sans_candidat", "aucun candidat"),
                                        ("tronquee", "tronquée"), ("bloquee", "SAFETY"), ("autre_modele", "modèle servi"),
                                        ("outil", "appel d'outil")])
def test_reponse_non_conforme_cout_sur_usage(serveur, mode, motif):
    serveur.mode = mode
    code, o, err = lancer(serveur)
    assert code == 5, (mode, o)
    assert motif in o["erreur"], (mode, o["erreur"])
    contrat(o)
    assert o["texte"] == "" and o["cout_origine"] == "usage" and o["cout_usd"] == pytest.approx(COUT_SAIN)
    assert o["erreur"] and err.startswith("commande_argon_v1 :")


def test_usage_absent_pire_cas_compte(serveur):
    serveur.mode = "usage_absent"
    code, o, _ = lancer(serveur)
    assert code == 5
    contrat(o)
    assert o["texte"] == "" and o["cout_origine"] == "pire_cas" and "usage absent" in o["erreur"]
    assert o["cout_usd"] == pytest.approx(1000 * PRIX_E + 65536 * PRIX_S, rel=1e-5)


# --- erreurs de l'interface ---------------------------------------------------------------------------------------------

def test_erreur_5xx_pire_cas_et_cle_masquee(serveur):
    serveur.mode = "http500"
    code, o, err = lancer(serveur)  # `lancer` vérifie que la clé n'est ni sur la sortie ni sur les erreurs
    assert code == 3
    contrat(o)
    assert o["cout_origine"] == "pire_cas" and "HTTP 500" in o["erreur"] and "[clé]" in o["erreur"]


def test_erreur_4xx_plancher(serveur):
    serveur.mode = "http400"
    code, o, _ = lancer(serveur)
    assert code == 3 and o["cout_origine"] == "plancher" and o["cout_usd"] == 1e-6 and "HTTP 400" in o["erreur"]


def test_connexion_refusee_rien_envoye(serveur):
    port_ferme = serveur.serveur.server_address[1]
    serveur.arreter()
    p = subprocess.run([sys.executable, "-I", "-B", COMMANDE, "--url-base", f"http://127.0.0.1:{port_ferme}/v1beta"],
                       input=b"bonjour", capture_output=True, env=env_commande(), timeout=60)
    o = json.loads(p.stdout.decode().splitlines()[-1])
    assert p.returncode == 3 and o["envoye"] is False and o["cout_origine"] == "plancher"
    serveur.serveur = type("S", (), {"shutdown": lambda s: None, "server_close": lambda s: None})()


# --- délai et interruption ----------------------------------------------------------------------------------------------

def test_delai_depasse(serveur):
    serveur.attente_s = 5
    t0 = time.monotonic()
    code, o, _ = lancer(serveur, args=["--delai-s", "1"])
    assert time.monotonic() - t0 < 4.5
    assert code == 6
    contrat(o)
    assert o["cout_origine"] == "pire_cas" and o["envoye"] is True and "délai" in o["erreur"]


def test_sigterm_rend_une_ligne_conforme(serveur):
    """Chemin de l'arrêt par l'enveloppe (`timeout -k`, qui envoie SIGTERM d'abord)."""
    serveur.attente_s = 5
    p = subprocess.Popen([sys.executable, "-I", "-B", COMMANDE, "--url-base", serveur.url], stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env_commande())
    p.stdin.write(b"x" * 4000)
    p.stdin.close()
    deadline = time.monotonic() + 10
    while not serveur.generations() and time.monotonic() < deadline:
        time.sleep(0.05)
    p.send_signal(signal.SIGTERM)
    sortie, _ = p.communicate(timeout=10)
    o = json.loads(sortie.decode().splitlines()[-1])
    assert p.returncode == 6 and o["cout_origine"] == "pire_cas" and CLE not in sortie.decode()


# --- réglages refusés, rien envoyé -------------------------------------------------------------------------------------

@pytest.mark.parametrize("env,motif", [
    (env_commande(plafond=None), "PLAFOND_SESSION_USD absent"),
    (env_commande(plafond="nan"), "PLAFOND_SESSION_USD"),
    (env_commande(plafond="0"), "PLAFOND_SESSION_USD"),
    (env_commande(role="classeur"), "ROLE_POLE"),
    (env_commande(role=None), "ROLE_POLE"),
    (env_commande(cle=None), "GEMINI_API_KEY absente"),
])
def test_reglages_refuses_sans_envoi(serveur, env, motif):
    code, o, _ = lancer(serveur, env=env)
    assert code == 2 and motif in o["erreur"] and serveur.requetes == [] and o["cout_usd"] == 1e-6


def test_consigne_vide_refusee(serveur):
    code, o, _ = lancer(serveur, consigne="  \n")
    assert code == 2 and serveur.requetes == []


def test_url_non_locale_en_clair_refusee(serveur):
    p = subprocess.run([sys.executable, "-I", "-B", COMMANDE, "--url-base", "http://exemple.invalid/v1beta"],
                       input=b"bonjour", capture_output=True, env=env_commande(), timeout=60)
    o = json.loads(p.stdout.decode().splitlines()[-1])
    assert p.returncode == 2 and "boucle locale" in o["erreur"]


# --- sortie lue par l'adaptateur réel de la v43 ------------------------------------------------------------------------

def _adaptateur_v43():
    adapt = os.path.join(V43, "pole", "adaptateurs.py")
    liste = os.path.join(V43, "EMPREINTES-orchestrateur-pole-v7-v43.txt")
    assert os.path.isfile(adapt) and os.path.isfile(liste), f"arbre v43 introuvable : {V43}"
    attendu = [l.split()[0] for l in open(liste, encoding="utf-8") if l.rstrip().endswith("pole/adaptateurs.py")]
    assert attendu and hashlib.sha256(open(adapt, "rb").read()).hexdigest() == attendu[0], "adaptateurs.py ≠ v43"
    sys.path.insert(0, V43)
    from pole.adaptateurs import AdaptateurCommandeExterne
    return AdaptateurCommandeExterne


def _enveloppe(tmp_path):
    """Imite l'enveloppe d'utilisateur distinct : pose la clé (ici factice), puis lance la commande. Jamais de clé dans la
    ligne de commande ni dans l'environnement de l'orchestrateur."""
    s = tmp_path / "enveloppe-argon-essai.sh"
    s.write_text(f"#!/bin/sh\nGEMINI_API_KEY='{CLE}'\nexport GEMINI_API_KEY\nexec '{sys.executable}' -I -B '{COMMANDE}' \"$@\"\n")
    s.chmod(0o700)
    return str(s)


def test_adaptateur_v43_lit_la_sortie(serveur, tmp_path):
    A = _adaptateur_v43()
    env_orch = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": str(tmp_path)}
    a = A([_enveloppe(tmp_path), "--url-base", serveur.url], environnement=env_orch, delai_s=60)
    assert a.environnement_commande(3.1, "proposeur_ideation") == dict(env_orch, PLAFOND_SESSION_USD="3.1",
                                                                       ROLE_POLE="proposeur_ideation")
    r = a.lancer("proposeur_ideation", "x" * 4000, str(tmp_path), 3.1, 2)
    assert r.statut == "ok" and r.texte_final == "OK" and r.cout_declare_usd == pytest.approx(COUT_SAIN)
    assert not getattr(r, "cout_inconnu", False)
    # juge, plafond 3,3
    r = a.lancer("juge_ideation", "x" * 4000, str(tmp_path), 3.3, 2)
    assert r.statut == "ok"
    # usage absent : sortie ≠ 0, ligne conforme → le coût imprimé (pire cas) est compté, pas le plafond
    serveur.mode = "usage_absent"
    r = a.lancer("proposeur_ideation", "x" * 4000, str(tmp_path), 3.1, 2)
    assert r.statut == "erreur" and r.cout_declare_usd == pytest.approx(1000 * PRIX_E + 65536 * PRIX_S, rel=1e-5)
    assert not getattr(r, "cout_inconnu", False)
    # refus de pire cas : rien envoyé, coût plancher compté
    serveur.mode = "sain"
    avant = len(serveur.requetes)
    r = a.lancer("proposeur_ideation", "x" * 4000, str(tmp_path), 0.01, 2)
    assert r.statut == "erreur" and r.cout_declare_usd == 1e-6 and len(serveur.requetes) == avant
    # réponse vide : coût sur l'usage
    serveur.mode = "vide"
    r = a.lancer("proposeur_ideation", "x" * 4000, str(tmp_path), 3.1, 2)
    assert r.statut == "erreur" and r.cout_declare_usd == pytest.approx(COUT_SAIN)
    # description consignée au manifeste : la commande et l'empreinte de l'enveloppe, aucune clé
    d = a.description()
    assert CLE not in json.dumps(d) and list(d["empreintes"]) == [a.commande[0]]


def test_adaptateur_v43_delai_de_la_commande(serveur, tmp_path):
    A = _adaptateur_v43()
    serveur.attente_s = 5
    a = A([_enveloppe(tmp_path), "--url-base", serveur.url, "--delai-s", "1"],
          environnement={"PATH": os.environ.get("PATH", "/usr/bin:/bin")}, delai_s=30)
    r = a.lancer("proposeur_ideation", "x" * 4000, str(tmp_path), 3.1, 2)
    assert r.statut == "erreur" and "code 6" in str(r.erreur)
    assert r.cout_declare_usd == pytest.approx(1000 * PRIX_E + 65536 * PRIX_S, rel=1e-5)


def test_adaptateur_v43_refuse_une_cle_dans_son_environnement(serveur, tmp_path):
    """Pourquoi l'enveloppe : l'orchestrateur ne porte jamais GEMINI_API_KEY (CL34-09)."""
    A = _adaptateur_v43()
    a = A([_enveloppe(tmp_path), "--url-base", serveur.url], environnement={"PATH": "/usr/bin", "GEMINI_API_KEY": "x"})
    with pytest.raises(Exception, match="GEMINI_API_KEY"):
        a.lancer("proposeur_ideation", "x" * 4000, str(tmp_path), 3.1, 2)
    assert serveur.requetes == []
