"""Essais du relais Kimi v3 (amont lu en flux, réponse entière au client) contre le faux amont v2 ; clé factice, aucun
réseau. Lancer : PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider test_relais_kimi_v3.py"""

import json
import os
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request

import pytest

ICI = os.path.dirname(os.path.abspath(__file__))
CLE = "cle-factice-essai-v3-0123456789abcdefghij"
MODELE = "kimi-k3.1-pro"


def port_libre():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


def lancer(cmd, env, motif, tmp, nom):
    journal = open(os.path.join(tmp, nom + ".log"), "w")
    proc = subprocess.Popen(cmd, env=env, stdout=journal, stderr=subprocess.STDOUT, cwd=ICI)
    for _ in range(100):
        texte = open(os.path.join(tmp, nom + ".log")).read()
        if motif in texte:
            return proc, texte
        if proc.poll() is not None:
            raise RuntimeError(texte)
        time.sleep(0.05)
    raise RuntimeError("pas prêt : " + nom)


@pytest.fixture
def banc(tmp_path):
    procs = []

    def fabriquer(options_amont=(), options_relais=()):
        amont, texte = lancer([sys.executable, "-I", "-B", "faux_amont_kimi_v2.py", *options_amont],
                              {"PATH": "/usr/bin:/bin"}, "faux amont prêt", str(tmp_path), "amont")
        procs.append(amont)
        url_amont = texte.strip().split()[-1]
        port = port_libre()
        journal = str(tmp_path / "journal.jsonl")
        relais, _ = lancer([sys.executable, "-I", "-B", "relais_kimi_v3.py", "--port", str(port), "--amont", url_amont,
                            "--modeles-permis", MODELE, "--plafond-usd", "5", "--reserve-par-appel", "0.05",
                            "--prix-entree", "2", "--prix-sortie", "10", "--prix-cache", "2",
                            "--max-jetons-sortie-pire-cas", "1000", "--journal", journal, *options_relais],
                           {"PATH": "/usr/bin:/bin", "KIMI_API_KEY": CLE}, "relais prêt", str(tmp_path), "relais")
        procs.append(relais)
        return f"http://127.0.0.1:{port}", journal

    yield fabriquer
    for p in procs:
        p.kill()
        p.wait()


def appeler(url, corps):
    brut = json.dumps(corps).encode()
    req = urllib.request.Request(url + "/v1/chat/completions", data=brut, method="POST",
                                 headers={"Content-Type": "application/json"})
    ouvreur = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        with ouvreur.open(req, timeout=30) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read() or b"{}")


def journal_lu(chemin):
    return [json.loads(l) for l in open(chemin) if l.strip()]


SAIN = {"model": MODELE, "messages": [{"role": "user", "content": "Bonjour"}], "max_tokens": 100}


def test_cas_sain_reassemble_contenu_raisonnement_usage(banc):
    url, j = banc(["--morceaux-raisonnement", "2"])
    statut, rep = appeler(url, SAIN)
    assert statut == 200
    msg = rep["choices"][0]["message"]
    assert msg["content"] == "Bonjour le monde."
    assert msg["reasoning_content"] == "pensée 0. pensée 1. "
    assert rep["choices"][0]["finish_reason"] == "stop" and rep["model"] == MODELE
    assert rep["usage"]["completion_tokens"] == 7
    e = journal_lu(j)[-1]
    assert e["cout_usd"] == pytest.approx((12 * 2 + 7 * 10) / 1e6) and not e["usage_absent"]


def test_usage_dans_le_choix_accepte(banc):
    url, _ = banc(["--usage-dans-le-choix"])
    statut, rep = appeler(url, SAIN)
    assert statut == 200 and rep["usage"]["prompt_tokens"] == 12


def test_flux_demande_par_le_client_refuse(banc):
    url, _ = banc()
    statut, _ = appeler(url, dict(SAIN, stream=True))
    assert statut == 400


def test_modele_servi_different_au_premier_morceau(banc):
    url, j = banc(["--modele-servi", "kimi-k3"])
    statut, rep = appeler(url, SAIN)
    assert statut == 502 and "modèle servi différent" in rep["erreur"]
    e = journal_lu(j)[-1]
    assert e["cout_usd"] > 0 and e["modele_servi"] == "kimi-k3"


def test_modele_qui_change_en_cours(banc):
    url, _ = banc(["--modele-change-en-cours"])
    statut, rep = appeler(url, SAIN)
    assert statut == 502 and "modèle servi différent" in rep["erreur"]


def test_usage_absent_compte_au_pire_cas_et_refuse_par_la_commande(banc):
    """Comme en v2 : la réponse est relayée (200) mais comptée au pire cas ; la commande la rejette (code 5)."""
    url, j = banc(["--sans-usage"])
    statut, rep = appeler(url, SAIN)
    assert statut == 200 and "usage" not in rep
    e = journal_lu(j)[-1]
    assert e["usage_absent"] and e["cout_usd"] == pytest.approx((len(json.dumps(SAIN)) + 1024) * 2 / 1e6 + 100 * 10 / 1e6, rel=0.05)
    r = subprocess.run([sys.executable, "-I", "-B", "commande_kimi_v1.py", "--url-relais", url], input="x",
                       capture_output=True, text=True, cwd=ICI,
                       env={"PATH": "/usr/bin:/bin", "PLAFOND_SESSION_USD": "3", "ROLE_POLE": "juge_ideation"})
    assert r.returncode == 5


def test_flux_coupe_avant_done(banc):
    url, j = banc(["--couper-apres", "2"])
    statut, rep = appeler(url, SAIN)
    assert statut == 502 and "coupé" in rep["erreur"]
    assert journal_lu(j)[-1]["cout_usd"] > 0


def test_silence_depasse(banc):
    url, j = banc(["--pause-entre-morceaux", "2"], ["--delai-silence-s", "0.5"])
    statut, _ = appeler(url, SAIN)
    assert statut == 502
    assert journal_lu(j)[-1]["cout_usd"] > 0


def test_delai_total_depasse(banc):
    url, _ = banc(["--pause-entre-morceaux", "0.4"], ["--delai-amont-s", "0.6", "--delai-silence-s", "5"])
    statut, rep = appeler(url, SAIN)
    assert statut == 502 and "délai total" in rep["erreur"]


def test_erreur_amont_relayee(banc):
    url, _ = banc(["--statut-erreur", "400"])
    statut, _ = appeler(url, SAIN)
    assert statut == 400


def test_plafond_402(banc):
    url, _ = banc((), ["--plafond-usd", "0.001"])
    statut, _ = appeler(url, dict(SAIN, max_tokens=100000))
    assert statut == 402


def test_cle_jamais_au_journal(banc):
    url, j = banc()
    appeler(url, SAIN)
    assert CLE not in open(j).read()


def test_commande_kimi_contre_relais_v3(banc):
    url, _ = banc(["--morceaux-raisonnement", "3"])
    r = subprocess.run([sys.executable, "-I", "-B", "commande_kimi_v1.py", "--url-relais", url], input="Juge ceci.",
                       capture_output=True, text=True, cwd=ICI,
                       env={"PATH": "/usr/bin:/bin", "PLAFOND_SESSION_USD": "3", "ROLE_POLE": "juge_ideation",
                            "MODELE_DEMANDE_POLE": MODELE})
    assert r.returncode == 0, r.stdout
    d = json.loads(r.stdout.strip().splitlines()[-1])
    assert d["texte"] == "Bonjour le monde." and d["modele_servi"] == MODELE and d["cout_usd"] > 0
