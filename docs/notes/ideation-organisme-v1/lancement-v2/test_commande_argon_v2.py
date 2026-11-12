"""Essais de `commande_argon_v2.py` contre un **faux serveur local** (127.0.0.1, port libre) : aucun réseau sortant, aucune
vraie clé, aucun appel payant. Les trois derniers essais de la v1 (et un neuf) lancent la commande par l'**adaptateur réel
de la v43** (`AdaptateurCommandeExterne`, `pole/adaptateurs.py` de l'arbre v43 copié, empreinte vérifiée contre la liste
de la v43 ; fichier identique dans la v44).

Reprend les 29 essais de `lancement-v1/test_commande_argon_v1.py`, adaptés à ce qui change en v2 (compte exact par
défaut, marge d'entrée de 5 %, provision de pensée de 8 192 jetons, `thinkingConfig` posé), puis les essais neufs de
CL44-02 et CL44-03 (contre-lecture `contre-lecture-v44-cl11.md`, sections 4 et 6).

Lancer : `python -m pytest -q -p no:cacheprovider lancement-v2/` (environnement /home/user/controle-ia-travail/.venv,
`PYTHONDONTWRITEBYTECODE=1` pour ne rien écrire dans le dossier scellé).
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
COMMANDE = os.path.join(ICI, "commande_argon_v2.py")
V43 = os.environ.get("ORCHESTRATEUR_V43") or os.path.join(ICI, "travail", "v43-copie", "orchestrateur-pole-v7")
CLE = "cle-factice-AIzaTEST-0123456789-ne-jamais-imprimer"
PRIX_E, PRIX_S = 8.3e-6, 41.5e-6
PROVISION = 8192


# --- faux serveur ----------------------------------------------------------------------------------------------------

class FauxGemini:
    """Répond selon `mode` ; consigne chaque requête (chemin, en-têtes, corps). `countTokens` rend `total_tokens`, ou à
    défaut ⌈caractères / 4⌉ (le compte de l'estimation de la commande)."""

    USAGE = {"promptTokenCount": 1000, "candidatesTokenCount": 10, "thoughtsTokenCount": 5, "totalTokenCount": 1015}

    def __init__(self):
        self.mode = "sain"
        self.requetes = []
        self.total_tokens = None
        self.attente_s = 0.0
        self.usage = dict(self.USAGE)
        faux = self

        class Gestion(BaseHTTPRequestHandler):
            def log_message(self, *a):
                pass

            def do_POST(self):
                n = int(self.headers.get("Content-Length") or 0)
                corps = json.loads(self.rfile.read(n).decode("utf-8"))
                faux.requetes.append({"chemin": self.path, "cle": self.headers.get("x-goog-api-key"), "corps": corps})
                if self.path.endswith(":countTokens"):
                    texte = "".join(p.get("text", "") for c in corps["contents"] for p in c["parts"])
                    total = faux.total_tokens if faux.total_tokens is not None else math.ceil(len(texte) / 4)
                    return self.repondre(200, {"totalTokens": total})
                if faux.attente_s:
                    time.sleep(faux.attente_s)
                code, obj = faux.reponse(corps)
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

    def reponse(self, corps):
        candidat = {"content": {"role": "model", "parts": [{"text": "OK"}]}, "finishReason": "STOP"}
        base = {"modelVersion": "gemini-4-argon", "responseId": "r1", "usageMetadata": dict(self.usage)}
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
        if m == "refus_pensee":  # l'interface refuse le champ thinkingConfig, accepte le corps sans lui
            if "thinkingConfig" in corps.get("generationConfig", {}):
                return 400, {"error": {"code": 400, "status": "INVALID_ARGUMENT",
                                       "message": "Unknown name \"thinkingConfig\" at 'generation_config' ; clé " + CLE}}
            return 200, dict(base, candidates=[candidat])
        raise AssertionError(m)

    def generations(self):
        return [r for r in self.requetes if r["chemin"].endswith(":generateContent")]

    def comptes(self):
        return [r for r in self.requetes if r["chemin"].endswith(":countTokens")]

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


def garde(n, marge_num=21, marge_den=20):
    """Entrée gardée : ⌈n × (1 + marge)⌉, en entiers (marge par défaut 0,05 = 1/20)."""
    return -(-n * marge_num // marge_den)


def max_sortie_attendue(entree_jetons, plafond=3.1, provision=PROVISION, max_s=65536, garde_jetons=None):
    """Même calcul que la commande (mêmes opérations flottantes)."""
    e = garde(entree_jetons) if garde_jetons is None else garde_jetons
    cout_e = e * 8.3 / 1e6
    place = math.floor((plafond - cout_e) / (41.5 / 1e6)) if plafond > cout_e else 0
    return min(max_s, place - provision)


COUT_SAIN = 1000 * PRIX_E + 15 * PRIX_S
PIRE_CAS_DEFAUT = garde(1000) * PRIX_E + (65536 + PROVISION) * PRIX_S  # consigne de 4 000 caractères, plafond 3,1


# === essais repris de la v1 (29), adaptés ===============================================================================

# --- cas sain ----------------------------------------------------------------------------------------------------------

def test_cas_sain(serveur):
    code, o, err = lancer(serveur)
    assert code == 0 and err == ""
    contrat(o)
    assert o["texte"] == "OK" and o["cout_origine"] == "usage" and o["envoye"] is True
    assert o["cout_usd"] == pytest.approx(COUT_SAIN)
    assert o["modele_servi"] == "gemini-4-argon" and o["role"] == "proposeur_ideation"
    assert o["version"] == "commande-argon-v2" and o["code"] == 0 and o["avertissements"] == []
    (r,) = serveur.generations()
    assert r["chemin"] == "/v1beta/models/gemini-4-argon:generateContent" and r["cle"] == CLE
    assert set(r["corps"]) == {"contents", "generationConfig"}, "aucun outil, aucune fonction, aucune consigne système"
    assert r["corps"]["contents"] == [{"role": "user", "parts": [{"text": "x" * 4000}]}]
    # v2 : sortie bornée par le plafond moins la provision : min(65536, (3,1 − 1050 × 8,3e-6) / 41,5e-6 − 8192)
    assert r["corps"]["generationConfig"] == {"maxOutputTokens": 65536, "thinkingConfig": {"thinkingBudget": 8192}}
    assert o["entree_jetons_comptee"] == 1000 and o["entree_jetons_garde"] == 1050
    assert o["provision_pensee_jetons"] == 8192 and o["config_pensee"] is True and o["marge_entree"] == 0.05
    assert o["pire_cas_usd"] == pytest.approx(PIRE_CAS_DEFAUT, abs=1e-6) and o["pire_cas_usd"] <= 3.1


def test_sortie_bornee_par_le_reste_du_plafond(serveur):
    # 1 077 663 caractères (contrôle réel de la course mesuré) à 3,1 : entrée gardée 282 887 jetons (2,348 USD),
    # reste 18 121 jetons payables, moins 8 192 de provision : ≈ 9 929 jetons de sortie
    consigne = "y" * 1_077_663
    code, o, _ = lancer(serveur, consigne=consigne)
    assert code == 0
    (r,) = serveur.generations()
    attendu = max_sortie_attendue(math.ceil(1_077_663 / 4))
    assert r["corps"]["generationConfig"]["maxOutputTokens"] == attendu
    assert 9_000 < attendu < 11_000
    assert o["pire_cas_usd"] <= 3.1 + 1e-9


def test_juge_role_transmis(serveur):
    code, o, _ = lancer(serveur, env=env_commande(plafond="3.3", role="juge_ideation"))
    assert code == 0 and o["role"] == "juge_ideation"


# --- refus de pire cas -------------------------------------------------------------------------------------------------

def test_refus_de_pire_cas_sans_envoi(serveur):
    code, o, err = lancer(serveur, env=env_commande(plafond="0.01"))
    assert code == 4
    contrat(o)
    assert serveur.generations() == [], "aucune génération"
    assert [r["chemin"] for r in serveur.requetes] == ["/v1beta/models/gemini-4-argon:countTokens"], \
        "seul le compte gratuit est envoyé"
    assert o["envoye"] is False and o["cout_origine"] == "plancher" and o["cout_usd"] == 1e-6
    assert "pire cas" in o["erreur"] and "rien envoyé" in o["erreur"] and "pire cas" in err


def test_refus_de_pire_cas_au_compte_exact(serveur):
    # estimation 1000 jetons ; countTokens dit 380 000 : l'entrée seule dépasse 3,1 → refus, aucune génération
    serveur.total_tokens = 380_000
    code, o, _ = lancer(serveur, args=["--compter-jetons"])  # option de la v1, toujours acceptée
    assert code == 4 and serveur.generations() == [] and len(serveur.requetes) == 1
    assert o["entree_jetons_comptee"] == 380_000 and o["envoye"] is False


def test_compte_exact_reduit_la_sortie(serveur):
    serveur.total_tokens = 200_000
    code, o, _ = lancer(serveur, args=["--compter-jetons"])
    assert code == 0
    (r,) = serveur.generations()
    assert r["corps"]["generationConfig"]["maxOutputTokens"] == max_sortie_attendue(200_000)
    assert o["entree_jetons_garde"] == 210_000


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
    assert o["erreur"] and err.startswith("commande_argon_v2 :")


def test_usage_absent_pire_cas_compte(serveur):
    serveur.mode = "usage_absent"
    code, o, _ = lancer(serveur)
    assert code == 5
    contrat(o)
    assert o["texte"] == "" and o["cout_origine"] == "pire_cas" and "usage absent" in o["erreur"]
    # v2 : le pire cas compte l'entrée gardée (marge comprise) et la provision de pensée
    assert o["cout_usd"] == pytest.approx(PIRE_CAS_DEFAUT, rel=1e-5)


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
    assert r.statut == "erreur" and r.cout_declare_usd == pytest.approx(PIRE_CAS_DEFAUT, rel=1e-5)
    assert not getattr(r, "cout_inconnu", False)
    # refus de pire cas : aucune génération, coût plancher compté
    serveur.mode = "sain"
    avant = len(serveur.generations())
    r = a.lancer("proposeur_ideation", "x" * 4000, str(tmp_path), 0.01, 2)
    assert r.statut == "erreur" and r.cout_declare_usd == 1e-6 and len(serveur.generations()) == avant
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
    assert r.cout_declare_usd == pytest.approx(PIRE_CAS_DEFAUT, rel=1e-5)


def test_adaptateur_v43_refuse_une_cle_dans_son_environnement(serveur, tmp_path):
    """Pourquoi l'enveloppe : l'orchestrateur ne porte jamais GEMINI_API_KEY (CL34-09)."""
    A = _adaptateur_v43()
    a = A([_enveloppe(tmp_path), "--url-base", serveur.url], environnement={"PATH": "/usr/bin", "GEMINI_API_KEY": "x"})
    with pytest.raises(Exception, match="GEMINI_API_KEY"):
        a.lancer("proposeur_ideation", "x" * 4000, str(tmp_path), 3.1, 2)
    assert serveur.requetes == []


# === essais neufs de la v2 ==============================================================================================

# --- CL44-02 : garde avec provision de pensée (avant envoi) --------------------------------------------------------------

def test_garde_avec_provision_refus_sans_envoi(serveur):
    """Plafond 0,3 : entrée gardée (0,0087) + sortie minimale (0,170) = 0,179 tiendrait en v1 ; plus la provision
    (0,340) = 0,519 > 0,3 → refus, code 4, aucune génération."""
    code, o, err = lancer(serveur, env=env_commande(plafond="0.3"))
    assert code == 4 and serveur.generations() == [] and o["envoye"] is False
    assert o["cout_origine"] == "plancher" and o["cout_usd"] == 1e-6
    attendu = 1050 * PRIX_E + (4096 + 8192) * PRIX_S
    assert f"{attendu:.4f}" in o["erreur"] and "8192 jetons de pensée" in o["erreur"] and "rien envoyé" in err


def test_garde_avec_provision_cas_sain_temoin(serveur):
    """R5 : même plafond, provision nulle → la garde laisse passer (elle refuse à cause de la provision, pas d'autre
    chose). Le faux serveur ne pense pas ici : avec une provision nulle, 5 jetons de pensée rendraient le code 7."""
    serveur.usage = dict(FauxGemini.USAGE, thoughtsTokenCount=0)
    code, o, _ = lancer(serveur, env=env_commande(plafond="0.3"), args=["--provision-pensee-jetons", "0"])
    assert code == 0
    (r,) = serveur.generations()
    assert r["corps"]["generationConfig"]["maxOutputTokens"] == max_sortie_attendue(1000, plafond=0.3, provision=0)


@pytest.mark.parametrize("plafond", ["0.6", "0.75", "1", "2.5", "3.1", "3.5"])
def test_garde_pire_cas_provision_comprise_sous_le_plafond(serveur, plafond):
    """Pour chaque plafond accepté : entrée gardée + (maxOutputTokens + provision) au prix de sortie ≤ plafond."""
    code, o, _ = lancer(serveur, env=env_commande(plafond=plafond), consigne="z" * 40_000)
    assert code == 0, o
    (r,) = serveur.generations()
    mx = r["corps"]["generationConfig"]["maxOutputTokens"]
    assert mx >= 4096
    pire = garde(10_000) * PRIX_E + (mx + PROVISION) * PRIX_S
    assert pire <= float(plafond) + 1e-12 and o["pire_cas_usd"] == pytest.approx(pire, abs=1e-6)


def test_garde_au_bord_de_la_provision(serveur):
    """Bord exact : le plafond qui laisse juste 4096 + 8192 jetons passe ; un jeton de moins est refusé."""
    e = 1050 * 8.3 / 1e6
    juste = e + (4096 + 8192) * 41.5 / 1e6
    code, o, _ = lancer(serveur, env=env_commande(plafond=repr(juste + 1e-9)))
    assert code == 0 and serveur.generations()[-1]["corps"]["generationConfig"]["maxOutputTokens"] == 4096
    code, o, _ = lancer(serveur, env=env_commande(plafond=repr(juste - 41.5e-6)))
    assert code == 4 and len(serveur.generations()) == 1


def test_provision_reglable(serveur):
    code, o, _ = lancer(serveur, env=env_commande(plafond="1"), args=["--provision-pensee-jetons", "1024"])
    assert code == 0 and o["provision_pensee_jetons"] == 1024
    (r,) = serveur.generations()
    assert r["corps"]["generationConfig"] == {"maxOutputTokens": max_sortie_attendue(1000, plafond=1.0, provision=1024),
                                              "thinkingConfig": {"thinkingBudget": 1024}}


@pytest.mark.parametrize("valeur", ["-1", "x", "1.5"])
def test_provision_invalide_refusee_sans_envoi(serveur, valeur):
    code, o, _ = lancer(serveur, args=["--provision-pensee-jetons", valeur])
    assert code == 2 and serveur.requetes == [] and o["cout_usd"] == 1e-6


def test_defaut_8192_garde_les_tailles_mesurees_par_cl11(serveur):
    """Justification du défaut : les quatre tailles de CL11 § 4, à leur plafond, sont acceptées avec la marge de 5 % et
    la provision de 8 192 ; 16 384 refuserait la passe 2 (garde de la v44) sans envoi."""
    cas = [(1_077_663, "3.1"), (685_992, "2.5"), (1_173_975, "3.1"), (1_166_746, "3.5")]
    for taille, plafond in cas:
        code, o, _ = lancer(serveur, consigne="x" * taille, env=env_commande(plafond=plafond))
        assert code == 0, (taille, o["erreur"])
        assert o["max_sortie_jetons"] == max_sortie_attendue(math.ceil(taille / 4), plafond=float(plafond)) >= 4096
        assert o["pire_cas_usd"] <= float(plafond) + 1e-9
    n = len(serveur.generations())
    code, o, _ = lancer(serveur, consigne="x" * 1_173_975, args=["--provision-pensee-jetons", "16384"])
    assert code == 4 and len(serveur.generations()) == n


# --- CL44-02 : thinkingConfig posé, ou non ------------------------------------------------------------------------------

def test_corps_porte_thinking_config(serveur):
    code, o, _ = lancer(serveur)
    (r,) = serveur.generations()
    assert code == 0 and r["corps"]["generationConfig"]["thinkingConfig"] == {"thinkingBudget": PROVISION}
    assert set(r["corps"]["generationConfig"]) == {"maxOutputTokens", "thinkingConfig"}


def test_sans_config_pensee_le_corps_ne_la_porte_pas_et_la_provision_reste_comptee(serveur):
    code, o, _ = lancer(serveur, consigne="y" * 1_077_663, args=["--sans-config-pensee"])
    assert code == 0 and o["config_pensee"] is False
    (r,) = serveur.generations()
    assert r["corps"]["generationConfig"] == {"maxOutputTokens": max_sortie_attendue(math.ceil(1_077_663 / 4))}
    assert "thinkingConfig" not in json.dumps(r["corps"])


def test_refus_4xx_de_thinking_config_remonte_sans_repli(serveur):
    """R5 : l'interface refuse le champ → code 3, coût plancher, une seule génération tentée, aucune relance sans le
    champ ; l'erreur de l'interface remonte telle quelle (clé masquée)."""
    serveur.mode = "refus_pensee"
    code, o, err = lancer(serveur)
    assert code == 3
    contrat(o)
    assert o["cout_origine"] == "plancher" and o["cout_usd"] == 1e-6 and o["texte"] == ""
    assert "HTTP 400" in o["erreur"] and "thinkingConfig" in o["erreur"] and "INVALID_ARGUMENT" in o["erreur"]
    assert "aucun repli" in o["erreur"] and "[clé]" in o["erreur"] and "HTTP 400" in err
    assert len(serveur.generations()) == 1, "aucune relance automatique sans thinkingConfig"
    # témoin : la même interface accepte le corps sans le champ, sur décision explicite
    code, o, _ = lancer(serveur, args=["--sans-config-pensee"])
    assert code == 0 and o["texte"] == "OK"


# --- CL44-02 : pensées au-delà de la provision (après la réponse) ------------------------------------------------------

def test_pensees_au_dela_de_la_provision_code_7_cout_reel(serveur):
    serveur.usage = dict(FauxGemini.USAGE, thoughtsTokenCount=9000)
    code, o, err = lancer(serveur)
    assert code == 7
    contrat(o)
    assert o["texte"] == "" and o["cout_origine"] == "usage" and o["envoye"] is True
    assert o["cout_usd"] == pytest.approx(1000 * PRIX_E + (10 + 9000) * PRIX_S)
    assert o["pensees_jetons"] == 9000 and o["code"] == 7
    assert "pensées au-delà de la provision" in o["erreur"] and "9000 > provision 8192" in o["erreur"]
    assert "thinkingConfig posé" in o["erreur"]
    assert err.startswith("commande_argon_v2 : ErreurCommande : pensées au-delà de la provision")


def test_pensees_egales_a_la_provision_passent(serveur):
    serveur.usage = dict(FauxGemini.USAGE, thoughtsTokenCount=PROVISION)
    code, o, err = lancer(serveur)
    assert code == 0 and err == "" and o["texte"] == "OK" and o["pensees_jetons"] == PROVISION


def test_pensees_au_dela_sans_config_pensee(serveur):
    serveur.usage = dict(FauxGemini.USAGE, thoughtsTokenCount=8193)
    code, o, _ = lancer(serveur, args=["--sans-config-pensee"])
    assert code == 7 and "thinkingConfig non posé" in o["erreur"]


def test_pensees_au_dela_priment_sur_une_reponse_tronquee(serveur):
    serveur.mode = "tronquee"
    serveur.usage = dict(FauxGemini.USAGE, thoughtsTokenCount=20_000)
    code, o, _ = lancer(serveur)
    assert code == 7 and o["cout_usd"] == pytest.approx(1000 * PRIX_E + 20_010 * PRIX_S)


def test_lecture_des_pensees_hors_max_sortie(serveur):
    """Diagnostic du premier appel : candidats + pensées > maxOutputTokens prouve que les pensées n'y sont pas comptées."""
    serveur.usage = dict(FauxGemini.USAGE, candidatesTokenCount=65536, thoughtsTokenCount=100)
    code, o, _ = lancer(serveur)
    assert code == 0 and o["lecture_pensees"] == "hors_max_sortie"
    serveur.usage = dict(FauxGemini.USAGE)
    code, o, _ = lancer(serveur)
    assert code == 0 and o["lecture_pensees"] == "indetermine"


def test_adaptateur_v43_pensees_au_dela_compte_le_cout_reel(serveur, tmp_path):
    A = _adaptateur_v43()
    serveur.usage = dict(FauxGemini.USAGE, thoughtsTokenCount=9000)
    a = A([_enveloppe(tmp_path), "--url-base", serveur.url],
          environnement={"PATH": os.environ.get("PATH", "/usr/bin:/bin")}, delai_s=60)
    r = a.lancer("proposeur_ideation", "x" * 4000, str(tmp_path), 3.1, 2)
    assert r.statut == "erreur" and "code 7" in str(r.erreur) and "pensées au-delà de la provision" in str(r.erreur)
    assert r.cout_declare_usd == pytest.approx(1000 * PRIX_E + 9010 * PRIX_S) and not getattr(r, "cout_inconnu", False)


# --- CL44-03 : compte exact par défaut, marge d'entrée --------------------------------------------------------------------

def test_compte_exact_par_defaut_puis_desactivable(serveur):
    code, o, _ = lancer(serveur)
    assert code == 0 and [r["chemin"].split(":")[-1] for r in serveur.requetes] == ["countTokens", "generateContent"]
    assert serveur.comptes()[0]["corps"] == {"contents": [{"role": "user", "parts": [{"text": "x" * 4000}]}]}
    serveur.requetes.clear()
    code, o, _ = lancer(serveur, args=["--sans-compter-jetons"])
    assert code == 0 and serveur.comptes() == [] and o["entree_jetons_comptee"] is None
    assert o["entree_jetons_garde"] == 1050


def test_marge_entree_appliquee_a_la_garde(serveur):
    consigne = "y" * 1_077_663
    n = math.ceil(1_077_663 / 4)
    sorties = {}
    for marge, garde_jetons in (("0", n), ("0.05", garde(n)), ("0.1", -(-n * 11 // 10))):
        serveur.requetes.clear()
        code, o, _ = lancer(serveur, consigne=consigne, args=["--marge-entree", marge])
        assert code == 0 and o["entree_jetons_garde"] == garde_jetons, (marge, o["entree_jetons_garde"])
        (r,) = serveur.generations()
        sorties[marge] = r["corps"]["generationConfig"]["maxOutputTokens"]
        assert sorties[marge] == max_sortie_attendue(n, garde_jetons=garde_jetons)
    assert sorties["0"] > sorties["0.05"] > sorties["0.1"]


def test_marge_entree_refuse_sans_envoi(serveur):
    """Contrôle réel (1 077 663 caractères) à 3,1 : accepté à 5 % ; à 30 %, l'entrée gardée (2,907) + 4 096 + 8 192
    jetons dépassent le plafond → refus, aucune génération."""
    code, o, _ = lancer(serveur, consigne="y" * 1_077_663, args=["--marge-entree", "0.3"])
    assert code == 4 and serveur.generations() == [] and o["envoye"] is False and "marge 0.3" in o["erreur"]


@pytest.mark.parametrize("valeur", ["-0.01", "nan", "inf", "x"])
def test_marge_invalide_refusee_sans_envoi(serveur, valeur):
    code, o, _ = lancer(serveur, args=[f"--marge-entree={valeur}"])
    assert code == 2 and "--marge-entree" in o["erreur"] and serveur.requetes == []


def test_entree_facturee_au_dessus_de_la_garde_dite_au_journal(serveur):
    """CL44-03 : l'interface facture plus que le compte et la marge ; code inchangé (0), avertissement en clair, coût
    réel rendu (le noyau le compte)."""
    serveur.usage = dict(FauxGemini.USAGE, promptTokenCount=1200)
    code, o, err = lancer(serveur)
    assert code == 0 and o["texte"] == "OK"
    assert o["cout_usd"] == pytest.approx(1200 * PRIX_E + 15 * PRIX_S)
    (a,) = o["avertissements"]
    assert "entrée facturée 1200 jetons > entrée gardée 1050" in a
    assert err.startswith("commande_argon_v2 : avertissement : entrée facturée 1200")
