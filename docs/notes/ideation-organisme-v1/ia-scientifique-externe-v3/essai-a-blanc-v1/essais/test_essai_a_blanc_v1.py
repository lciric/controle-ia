"""Essais locaux de l'essai à blanc de la v3, v1 : règles du mandataire et relais factice (sans réseau sortant).

    python3 -I -B -m unittest essais/test_essai_a_blanc_v1.py   (depuis le dossier essai-a-blanc-v1)
Le relais factice est lancé sur 127.0.0.1, port libre ; aucun appel ne quitte la machine.
"""
import json
import os
import socket
import subprocess
import sys
import tempfile
import time
import unittest
import urllib.error
import urllib.request

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
sys.path.insert(0, os.path.join(RACINE, "machine-a"))
from mandataire_regles_v1 import decision  # noqa: E402

JETON = "jeton-de-course-factice-" + "x" * 24


class Regles(unittest.TestCase):
    def test_copie_publique_refusee(self):
        for hote, chemin in [("github.com", "/lciric/controle-ia"), ("github.com", "/LCIRIC/Controle-IA/blob/main/x"),
                             ("github.com", "//lciric//controle-ia"), ("github.com", "/lciric%2Fcontrole-ia"),
                             ("github.com", "/lciric%252Fcontrole-ia"), ("raw.githubusercontent.com",
                                                                        "/lciric/controle-ia/main/README.md"),
                             ("codeload.github.com", "/lciric/controle-ia/zip/main"),
                             ("api.github.com", "/repos/lciric/controle-ia/contents"),
                             ("api.github.com", "/search/code?q=user:lciric"),
                             ("github.com", "/lciric/controle-ia-travail"), ("GitHub.com.", "/lciric/controle-ia"),
                             ("github.com:443", "/lciric/controle-ia.git/info/refs")]:
            with self.subTest(hote=hote, chemin=chemin):
                self.assertFalse(decision(hote, chemin)[0])

    def test_fournisseurs_refuses(self):
        for hote in ["api.anthropic.com", "api.openai.com", "chatgpt.com", "bedrock-runtime.us-east-1.amazonaws.com",
                     "generativelanguage.googleapis.com", "API.ANTHROPIC.COM"]:
            with self.subTest(hote=hote):
                self.assertFalse(decision(hote, "/v1/messages")[0])

    def test_cas_sains_permis(self):
        for hote, chemin in [("github.com", "/SakanaAI/AI-Scientist-v3"), ("github.com", "/lciric"),
                             ("github.com", "/lciric/autre-depot"), ("arxiv.org", "/abs/2610.18933"),
                             ("pypi.org", "/simple/numpy/"), ("api.github.com", "/repos/SakanaAI/AI-Scientist-v3"),
                             ("scholar.google.com", "/scholar?q=controle-ia")]:
            with self.subTest(hote=hote, chemin=chemin):
                self.assertEqual(decision(hote, chemin), (True, ""))


def _port_libre():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


class RelaisFactice(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dossier = tempfile.mkdtemp()
        cls.journal = os.path.join(cls.dossier, "journal.jsonl")
        cls.port = _port_libre()
        env = {"PATH": "/usr/bin:/bin", "RELAIS_JETON_COURSE": JETON}
        cls.proc = subprocess.Popen(
            [sys.executable, "-I", "-B", os.path.join(RACINE, "machine-b", "relais_factice_v1.py"), "--hote",
             "127.0.0.1", "--port", str(cls.port), "--modeles-permis", "claude-opus-4-7,claude-opus-5-5",
             "--plafond-fictif-usd", "0.10", "--cout-fictif-par-appel", "0.05", "--journal", cls.journal],
            env=env, stderr=subprocess.DEVNULL)
        for _ in range(50):
            try:
                urllib.request.urlopen(f"http://127.0.0.1:{cls.port}/relais/etat", timeout=1)
                break
            except OSError:
                time.sleep(0.1)

    @classmethod
    def tearDownClass(cls):
        cls.proc.terminate()
        cls.proc.wait(timeout=5)

    def _post(self, chemin, corps, jeton=JETON, entete="Authorization"):
        donnees = json.dumps(corps).encode()
        req = urllib.request.Request(f"http://127.0.0.1:{self.port}{chemin}", data=donnees, method="POST")
        req.add_header("Content-Type", "application/json")
        if jeton is not None:
            req.add_header(entete, f"Bearer {jeton}" if entete == "Authorization" else jeton)
        try:
            with urllib.request.urlopen(req, timeout=5) as r:
                return r.status, r.read().decode()
        except urllib.error.HTTPError as e:
            return e.code, e.read().decode()

    def test_1_jeton_et_modele(self):
        self.assertEqual(self._post("/v1/messages", {"model": "claude-opus-4-7"}, jeton=None)[0], 401)
        self.assertEqual(self._post("/v1/messages", {"model": "claude-opus-4-7"}, jeton="faux" * 10)[0], 401)
        self.assertEqual(self._post("/v1/messages", {"model": "claude-haiku-9"})[0], 403)
        self.assertEqual(self._post("/v1/autre", {"model": "claude-opus-4-7"})[0], 404)

    def test_2_reponses_puis_plafond(self):
        code, texte = self._post("/v1/messages", {"model": "claude-opus-4-7", "messages": []})
        self.assertEqual(code, 200)
        self.assertEqual(json.loads(texte)["stop_reason"], "end_turn")
        code, texte = self._post("/v1/messages", {"model": "claude-opus-5-5", "stream": True}, entete="x-api-key")
        self.assertEqual(code, 200)
        evenements = [l[len("event: "):] for l in texte.splitlines() if l.startswith("event: ")]
        self.assertEqual(evenements, ["message_start", "content_block_start", "content_block_delta",
                                      "content_block_stop", "message_delta", "message_stop"])
        self.assertEqual(self._post("/v1/messages", {"model": "claude-opus-4-7"})[0], 402)  # plafond fictif 0,10

    def test_3_journal_sans_jeton_ni_corps(self):
        with open(self.journal, encoding="utf-8") as f:
            contenu = f.read()
        self.assertNotIn(JETON, contenu)
        self.assertNotIn("Réponse factice", contenu)
        etat = json.loads(urllib.request.urlopen(f"http://127.0.0.1:{self.port}/relais/etat").read())
        self.assertEqual(etat["amont"], "aucun (factice)")

    def test_4_refus_sur_toutes_adresses(self):
        r = subprocess.run([sys.executable, "-I", "-B", os.path.join(RACINE, "machine-b", "relais_factice_v1.py"),
                            "--hote", "0.0.0.0", "--modeles-permis", "x", "--plafond-fictif-usd", "1", "--journal",
                            "/dev/null"], env={"RELAIS_JETON_COURSE": JETON}, capture_output=True, text=True)
        self.assertNotEqual(r.returncode, 0)
        r = subprocess.run([sys.executable, "-I", "-B", os.path.join(RACINE, "machine-b", "relais_factice_v1.py"),
                            "--hote", "127.0.0.1", "--modeles-permis", "x", "--plafond-fictif-usd", "1", "--journal",
                            "/dev/null"], env={"RELAIS_JETON_COURSE": "court"}, capture_output=True, text=True)
        self.assertNotEqual(r.returncode, 0)


if __name__ == "__main__":
    unittest.main()
