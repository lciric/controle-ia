"""Essais du collisionneur v8 (cinq espèces, espèce E = GPT-6 Astra par l'API d'OpenAI), hors réseau.

Un faux serveur HTTP local (ThreadingHTTPServer dans un fil) imite l'API « chat completions » d'OpenAI ; `appeler_openai` le
joint par OPENAI_BASE_URL=http://127.0.0.1:PORT, avec une clé factice qui ne doit jamais apparaître dans un message d'erreur.
Aucun appel payant, aucun réseau : les autres espèces sont servies par des appelants factices injectés dans `principal`.
Lancement : python -m pytest -q test_collisionneur_v8.py (depuis ce dossier ; le v7 est lu dans donnees/ pour la non-régression).
"""
import hashlib
import importlib.util
import inspect
import json
import re
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import pytest

ICI = Path(__file__).resolve().parent
RACINE = ICI.parents[4]
CHEMIN_V7 = RACINE / "donnees" / "collisionneur-noeuds-v1" / "collisionneur_v7.py"
CHEMIN_V8 = ICI / "collisionneur_v8.py"
EMPREINTE_V7 = "c9725f025407c3ece3e8c16d19cfdfdec078f084a811f0a3b6ea3209be5d98dc"
CLE_FACTICE = "sk-factice-ABCDEF0123456789-NE-DOIT-JAMAIS-SORTIR"
MARQUEUR = "FIN-DE-CELLULE"


def charger(chemin, nom):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def v8():
    return charger(CHEMIN_V8, "collisionneur_v8")


@pytest.fixture(scope="module")
def v7():
    if not CHEMIN_V7.exists():
        pytest.skip("collisionneur_v7.py absent de donnees/ : non-régression impossible ici")
    return charger(CHEMIN_V7, "collisionneur_v7")


# ---------- faux serveur OpenAI ----------

class EtatServeur:
    """Réglages partagés entre les essais et le fil du serveur."""

    def __init__(self):
        self.defaut = "normal"      # scénario quand le prompt ne commence pas par SCENARIO=
        self.compteurs = {}         # appels par scénario
        self.requetes = []          # (en-têtes, corps) reçus
        self.verrou = threading.Lock()


def reponse_openai(scenario, modele, n):
    """Corps JSON d'une réponse « chat completion » selon le scénario ; None → réponse HTTP d'erreur gérée par le serveur."""
    usage = {"prompt_tokens": 100, "completion_tokens": 50, "total_tokens": 150}
    message = {"role": "assistant", "content": f"Réponse d'essai ({scenario}).\n\n{MARQUEUR}"}
    fin = "stop"
    if scenario == "length":
        fin = "length"
        message["content"] = "Texte coupé avant la fin"
    elif scenario == "content_filter":
        fin = "content_filter"
        message["content"] = ""
    elif scenario == "vide":
        message["content"] = ""
    elif scenario == "refusal":
        message["content"] = ""
        message["refusal"] = "I can't help with that."
    elif scenario == "tool_calls":
        fin = "tool_calls"
    elif scenario == "raisonnement":
        usage["completion_tokens_details"] = {"reasoning_tokens": 300}
    elif scenario == "autre-modele":
        modele = "gpt-5-nano"
    elif scenario == "sans-choix":
        return {"id": "chatcmpl-vide", "object": "chat.completion", "model": modele, "choices": [], "usage": usage}
    return {"id": f"chatcmpl-{scenario}-{n}", "object": "chat.completion", "created": 1_762_000_000,
            "model": modele, "choices": [{"index": 0, "message": message, "finish_reason": fin}], "usage": usage}


class Imitation(BaseHTTPRequestHandler):
    etat = None  # fixé par la fixture

    def log_message(self, *args):  # silence
        pass

    def _envoyer(self, code, corps):
        octets = json.dumps(corps, ensure_ascii=False).encode("utf-8") if not isinstance(corps, bytes) else corps
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(octets)))
        self.end_headers()
        self.wfile.write(octets)

    def do_POST(self):
        taille = int(self.headers.get("Content-Length") or 0)
        corps = json.loads(self.rfile.read(taille).decode("utf-8"))
        with self.etat.verrou:
            self.etat.requetes.append((dict(self.headers), corps, self.path))
        if self.path != "/chat/completions":
            return self._envoyer(404, {"error": {"message": "chemin inconnu"}})
        if self.headers.get("Authorization") != f"Bearer {CLE_FACTICE}":
            return self._envoyer(401, {"error": {"message": "clé refusée"}})
        prompt = corps["messages"][0]["content"]
        m = re.match(r"SCENARIO=(\S+)", prompt)
        scenario = m.group(1) if m else self.etat.defaut
        with self.etat.verrou:
            n = self.etat.compteurs[scenario] = self.etat.compteurs.get(scenario, 0) + 1
        if scenario == "429-puis-succes" and n <= 2:
            return self._envoyer(429, {"error": {"message": "rate limit"}})
        if scenario == "503-puis-succes" and n == 1:
            return self._envoyer(503, {"error": {"message": "surcharge"}})
        if scenario == "400-echo":  # une erreur qui renverrait la clé : elle doit être masquée côté client
            return self._envoyer(400, {"error": {"message": f"en-tête reçu : {self.headers.get('Authorization')}"}})
        if scenario == "non-json":
            return self._envoyer(200, b"<html>pas du JSON</html>")
        return self._envoyer(200, reponse_openai(scenario, corps["model"], n))


@pytest.fixture(scope="module")
def serveur():
    etat = EtatServeur()
    Imitation.etat = etat
    srv = ThreadingHTTPServer(("127.0.0.1", 0), Imitation)
    fil = threading.Thread(target=srv.serve_forever, daemon=True)
    fil.start()
    try:
        yield f"http://127.0.0.1:{srv.server_address[1]}", etat
    finally:
        srv.shutdown()
        srv.server_close()


@pytest.fixture
def env_openai(monkeypatch, serveur):
    url, etat = serveur
    monkeypatch.setenv("OPENAI_API_KEY", CLE_FACTICE)
    monkeypatch.setenv("OPENAI_BASE_URL", url)
    monkeypatch.delenv("SSL_CERT_FILE", raising=False)
    etat.defaut = "normal"
    return etat


def appel(v8, scenario, max_tokens=1000):
    return v8.appeler_openai("gpt-6-astra", f"SCENARIO={scenario}\nQuestion d'essai.", max_tokens, attentes=(0, 0, 0))


# ---------- structure : cinq espèces ----------

def test_v7_intact():
    if not CHEMIN_V7.exists():
        pytest.skip("v7 absent ici")
    assert hashlib.sha256(CHEMIN_V7.read_bytes()).hexdigest() == EMPREINTE_V7


def test_lettres_modeles_et_appelants(v8):
    assert v8.LETTRES == ("A", "B", "C", "D", "E")
    assert v8.MODELES["E"] == {"id": "gpt-6-astra", "fournisseur": "openai", "prix": (10.0, 50.0),
                               "max": 32000, "max_relance": 65536}
    assert set(v8.MODELES) == set(v8.LETTRES)
    assert v8.APPELANTS["openai"] is v8.appeler_openai
    assert all(m["fournisseur"] in v8.APPELANTS for m in v8.MODELES.values())
    assert v8.VERSION != "collisionneur-v2.10-quatre-especes-opus46-noms-neutres"


def test_preambule_et_critique_croisee(v8):
    assert "5×3" in v8.PREAMBULE and "entre cinq modèles" in v8.PREAMBULE
    assert "{lettre}" in v8.PREAMBULE and "{autres}" in v8.PREAMBULE and "{marqueur}" in v8.PREAMBULE
    for lettre in v8.LETTRES:
        assert len(v8.autres(lettre)) == 4 and lettre not in v8.autres(lettre)
    # chaque espèce critique les quatre autres, et répond aux quatre critiques qui la visent
    assert v8.entrees("E3-T2", "E", []) == [f"E3-T1-conception-{l}" for l in "ABCD"]
    assert v8.entrees("E3-T2", "A", []) == [f"E3-T1-conception-{l}" for l in "BCDE"]
    assert v8.entrees("E3-T3", "E", []) == ["E3-T1-conception-E"] + [f"E3-T2-critique-croisee-{l}" for l in "ABCD"]
    assert v8.entrees("E2-T2", "C", []) == [f"E2-T1-prog-maths-{l}" for l in "ABDE"]
    assert len(v8.entrees("E1-T2", "B", [])) == 5
    assert v8.entrees("E2-T1", "D", ["x", "y"]) == ["x", "y"]


def test_aucun_nombre_d_especes_code_en_dur(v8):
    code = [l for l in CHEMIN_V8.read_text(encoding="utf-8").splitlines() if not l.lstrip().startswith("#")]
    texte = "\n".join(code)
    for interdit in ("3×3", "4×3", "trois modèles", "quatre modèles", "quatre espèces", "3 cellules par tour",
                     'LETTRES = ("A", "B", "C", "D")', "cellules/12"):
        assert interdit not in texte, interdit
    # le pire cas de Jev suit le nombre d'espèces
    assert "len(LETTRES) * TOURS[t]" in texte


def test_lire_arbitrage_accepte_E(v8, tmp_path):
    f = tmp_path / "arb.md"
    f.write_text("RETENUES: E1-T2-critique-meta-E, E1-T2-critique-meta-A\n\nJustification.\n", encoding="utf-8")
    assert v8.lire_arbitrage(f)[1] == ["E1-T2-critique-meta-E", "E1-T2-critique-meta-A"]
    f.write_text("RETENUES: E1-T2-critique-meta-F\n", encoding="utf-8")
    with pytest.raises(v8.Arret):
        v8.lire_arbitrage(f)


# ---------- appeler_openai contre le faux serveur ----------

def test_appel_normal_et_corps_de_requete(v8, env_openai):
    rep = appel(v8, "normal", max_tokens=1234)
    assert rep.echec is None
    assert v8.statut_reponse("openai", rep) == "OK"
    assert rep.modele_servi == "gpt-6-astra" and v8.modele_conforme("gpt-6-astra", rep.modele_servi)
    assert rep.identifiant.startswith("chatcmpl-normal")
    assert rep.fin == "stop" and rep.categorie is None
    assert rep.usage == {"entree": 100, "sortie": 50, "sortie_visible": 50, "raisonnement": 0}
    assert rep.texte.rstrip().endswith(MARQUEUR)
    entetes, corps, chemin = env_openai.requetes[-1]
    assert chemin == "/chat/completions"
    assert entetes["Authorization"] == f"Bearer {CLE_FACTICE}"
    assert corps == {"model": "gpt-6-astra", "messages": [{"role": "user", "content": "SCENARIO=normal\nQuestion d'essai."}],
                     "max_completion_tokens": 1234}
    assert v8.cout(v8.MODELES["E"]["prix"], rep.usage) == pytest.approx(100 / 1e6 * 10 + 50 / 1e6 * 50)


def test_modele_servi_suffixe_date(v8):
    assert v8.modele_conforme("gpt-6-astra", "gpt-6-astra-2026-10-20")
    # propriété du v7, inchangée : tout suffixe après un tiret passe, donc une variante « -mini » servie passerait aussi ;
    # l'identifiant exact doit donc être confirmé en ligne (LISEZMOI, « à vérifier en ligne »)
    assert v8.modele_conforme("gpt-6-astra", "gpt-6-astra-mini")
    assert not v8.modele_conforme("gpt-6-astra", "gpt-5")
    assert not v8.modele_conforme("gpt-6-astra", None)


@pytest.mark.parametrize("scenario, statut", [
    ("length", "TRONQUE"), ("content_filter", "REFUS"), ("vide", "VIDE"), ("refusal", "REFUS"),
    ("tool_calls", "ANOMALIE"), ("sans-choix", "VIDE"), ("raisonnement", "OK"),
])
def test_statuts(v8, env_openai, scenario, statut):
    rep = appel(v8, scenario)
    assert rep.echec is None
    assert v8.statut_reponse("openai", rep) == statut
    if scenario == "content_filter":
        assert rep.categorie == "content_filter"
    if scenario == "refusal":
        assert rep.categorie.startswith("I can't") and "refusal" in rep.types_blocs


def test_jetons_de_raisonnement_comptes_en_sortie(v8, env_openai):
    rep = appel(v8, "raisonnement")
    assert rep.usage == {"entree": 100, "sortie": 350, "sortie_visible": 50, "raisonnement": 300}
    assert v8.cout((10.0, 50.0), rep.usage) == pytest.approx(100 / 1e6 * 10 + 350 / 1e6 * 50)


def test_relances_429_et_503(v8, env_openai):
    rep = appel(v8, "429-puis-succes")
    assert rep.echec is None and v8.statut_reponse("openai", rep) == "OK"
    assert env_openai.compteurs["429-puis-succes"] == 3
    rep = appel(v8, "503-puis-succes")
    assert rep.echec is None and env_openai.compteurs["503-puis-succes"] == 2
    # une seule tentative permise : le 429 devient un échec, sans autre modèle
    env_openai.compteurs["429-puis-succes"] = 0
    rep = v8.appeler_openai("gpt-6-astra", "SCENARIO=429-puis-succes\n", 100, attentes=(0,))
    assert rep.echec.startswith("HTTP 429")


def test_cle_jamais_dans_les_messages(v8, env_openai, monkeypatch):
    rep = appel(v8, "400-echo")
    assert rep.echec.startswith("HTTP 400") and "[clé]" in rep.echec and CLE_FACTICE not in rep.echec
    rep = appel(v8, "non-json")
    assert rep.echec.startswith("connexion : JSONDecodeError") and CLE_FACTICE not in rep.echec
    monkeypatch.setenv("OPENAI_BASE_URL", "http://127.0.0.1:1")  # port fermé
    rep = v8.appeler_openai("gpt-6-astra", "x", 10, attentes=(0, 0))
    assert rep.echec.startswith("connexion :") and CLE_FACTICE not in rep.echec
    monkeypatch.setenv("OPENAI_BASE_URL", "https://exemple.invalid/v1")  # tiers : refusé sans réseau
    rep = v8.appeler_openai("gpt-6-astra", "x", 10, attentes=(0,))
    assert rep.echec.startswith("OPENAI_BASE_URL") and CLE_FACTICE not in rep.echec
    monkeypatch.delenv("OPENAI_API_KEY")
    assert v8.appeler_openai("gpt-6-astra", "x", 10).echec == "OPENAI_API_KEY absente"


def test_cle_mauvaise_rejetee_par_le_serveur(v8, env_openai, monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "sk-autre")
    rep = appel(v8, "normal")
    assert rep.echec.startswith("HTTP 401") and "sk-autre" not in rep.echec


# ---------- coûts et devis ----------

def test_cout_et_pire_cas(v8):
    prix = v8.MODELES["E"]["prix"]
    assert v8.cout(prix, {"entree": 1_000_000, "sortie": 1_000_000}) == pytest.approx(60.0)
    assert v8.cout_pire_cas(prix, 3000, 32000) == pytest.approx(3000 / 3 / 1e6 * 10 + 32000 / 1e6 * 50)
    assert v8.cout_pire_cas(prix, 0, v8.MODELES["E"]["max_relance"]) == pytest.approx(65536 / 1e6 * 50)


def test_devis_compte_quinze_cellules_par_etage(v8, tmp_path, capsys):
    faits = tmp_path / "faits.md"
    faits.write_text("FAIT 1 (VÉRIFIÉ) : un fait factice.\n", encoding="utf-8")
    sous_totaux = v8.devis(str(faits), None, jev=True)
    sortie = capsys.readouterr().out
    lignes_cellules = [l for l in sortie.splitlines() if "pire cas" in l and l.startswith("E")]
    assert len(lignes_cellules) == 8 * 5 == 40
    assert len([l for l in lignes_cellules if l.startswith("E3-")]) == 15
    assert len([l for l in lignes_cellules if l.rstrip().split("USD")[0].strip() and "-E " in l]) == 8
    assert "étage 3 : 15 cellules" in sortie and "étage 2 : 15 cellules" in sortie and "étage 1 : 10 cellules" in sortie
    assert set(sous_totaux) == {1, 2, 3} and all(v > 0 for v in sous_totaux.values())
    # l'espèce E pèse 32000 jetons de sortie à 50 USD le million dans chacune de ses cellules
    e = [l for l in lignes_cellules if "gpt-6-astra" in l]
    assert len(e) == 8 and all(float(l.split("pire cas")[1].split()[0]) >= 1.6 for l in e)


# ---------- non-régression sur le v7 ----------

FONCTIONS_INCHANGEES = [
    "empreinte", "empreinte_fichier", "normaliser", "lire_entree", "maintenant", "ecrire_neuf", "lire_sceau",
    "ajouter_journal", "lire_journal", "essais_journal", "depense", "empreinte_script", "id_cellule", "chemin_cellule",
    "cellule_valide", "statut_courant", "autres", "entrees", "bloc_piece", "bloc_absent", "construire_prompt",
    "appeler_anthropic", "appeler_gemini", "lire_reponse_gemini", "appeler_jev", "appeler_kimi", "modele_conforme",
    "cout", "cout_pire_cas", "prochain_essai", "executer_cellule", "audits_jev", "audit_reussi", "prochain_audit",
    "auditer_jev", "verser_une_fois", "lire_arbitrage", "consigner_absences", "lancer_etage", "ecrire_etat",
    "resume_jev", "verifier",
]


def test_fonctions_inchangees_identiques_au_v7(v7, v8):
    differentes = [n for n in FONCTIONS_INCHANGEES if inspect.getsource(getattr(v7, n)) != inspect.getsource(getattr(v8, n))]
    assert differentes == []
    for nom in ("TOURS", "ORDRE_ETAGE", "CONSIGNES", "QUESTIONS_JEV", "JEV", "EFFORT", "MARQUEUR", "PLAFOND_DEFAUT_USD",
                "REFUS_GEMINI"):
        assert getattr(v7, nom) == getattr(v8, nom), nom
    for lettre in "ABCD":
        assert v7.MODELES[lettre] == v8.MODELES[lettre]


def test_statut_reponse_identique_pour_les_anciens_fournisseurs(v7, v8):
    fins = {"anthropic": ["refusal", "max_tokens", "end_turn", "tool_use", None],
            "kimi": ["content_filter", "length", "stop", "tool_calls", None],
            "gemini": ["SAFETY", "BLOCAGE_PROMPT", "MAX_TOKENS", "STOP", "AUCUN_CANDIDAT", "OTHER", None]}
    for fournisseur, liste in fins.items():
        for fin in liste:
            for texte in ("", "   ", "du texte"):
                a = v7.statut_reponse(fournisseur, v7.Reponse(texte=texte, fin=fin))
                b = v8.statut_reponse(fournisseur, v8.Reponse(texte=texte, fin=fin))
                assert a == b, (fournisseur, fin, texte)
    for usage in ({"entree": 0, "sortie": 0}, {"entree": 12345, "sortie": 67890}):
        for prix in ((10.0, 50.0), (2.0, 10.0)):
            assert v7.cout(prix, usage) == v8.cout(prix, usage)
            assert v7.cout_pire_cas(prix, 5000, 64000) == v8.cout_pire_cas(prix, 5000, 64000)


def test_preambule_v8_ne_differe_du_v7_que_par_le_nombre(v7, v8):
    assert v8.PREAMBULE == v7.PREAMBULE.replace("4×3", "5×3").replace("entre quatre", "entre cinq")


# ---------- étage III de bout en bout, cinq espèces, E par le faux serveur ----------

def appelants_factices(v8):
    def anthropic(modele_id, prompt, max_tokens):
        return v8.Reponse(texte=f"Cellule Claude.\n\n{MARQUEUR}", modele_servi=modele_id, identifiant="msg_1", fin="end_turn",
                          usage={"entree": 10, "sortie": 20}, types_blocs=["text"])

    def gemini(modele_id, prompt, max_tokens):
        return v8.Reponse(texte=f"Cellule Gemini.\n\n{MARQUEUR}", modele_servi=modele_id, identifiant="g_1", fin="STOP",
                          usage={"entree": 10, "sortie": 20}, types_blocs=["text"])

    def kimi(modele_id, prompt, max_tokens):
        return v8.Reponse(texte=f"Cellule Kimi.\n\n{MARQUEUR}", modele_servi=modele_id, identifiant="k_1", fin="stop",
                          usage={"entree": 10, "sortie": 20}, types_blocs=["text"])

    def jev(etat, questions):
        return {"echec": "Jev non appelé dans les essais"}

    return {"anthropic": anthropic, "gemini": gemini, "kimi": kimi, "openai": v8.appeler_openai, "jev": jev}


def preparer_entrees(tmp_path):
    faits = tmp_path / "faits.md"
    faits.write_text("FAIT 1 (VÉRIFIÉ) : fait factice pour les essais.\n", encoding="utf-8")
    question = tmp_path / "question.md"
    question.write_text("QUESTION : question factice de l'arbitre ?\n", encoding="utf-8")
    return faits, question


def test_etage3_cinq_especes(v8, env_openai, tmp_path):
    faits, question = preparer_entrees(tmp_path)
    dossier = tmp_path / "run"
    code = v8.principal(["etage3", "--sortie", str(dossier), "--faits", str(faits), "--question", str(question),
                         "--plafond-usd", "100"], appelants=appelants_factices(v8))
    assert code == v8.CODE_FINI
    cellules = sorted(p.stem for p in (dossier / "cellules").glob("*.md"))
    assert len(cellules) == 15 and [c[-1] for c in cellules] == list("ABCDE") * 3
    assert v8.verifier(dossier) == []
    etat = (dossier / "etat.md").read_text(encoding="utf-8")
    assert etat.count("| OK |") == 15 and "E3-T3-reponse-E" in etat and "Absences acceptées par l'arbitre : aucune." in etat
    # critique croisée : E lit les quatre autres ; A lit E ; la réponse d'E reçoit les quatre critiques
    prompt_e = (dossier / "essais" / "E3-T2-critique-croisee-E.essai1.prompt.txt").read_text(encoding="utf-8")
    pieces = v8.MOTIF_PIECE.findall(prompt_e)
    assert [p[0] for p in pieces] == [f"E3-T1-conception-{l}" for l in "ABCD"]
    assert "Tu es la proposition E. Les autres propositions portent les lettres A, B, C, D" in prompt_e
    prompt_a = (dossier / "essais" / "E3-T2-critique-croisee-A.essai1.prompt.txt").read_text(encoding="utf-8")
    assert [p[0] for p in v8.MOTIF_PIECE.findall(prompt_a)] == [f"E3-T1-conception-{l}" for l in "BCDE"]
    prompt_e3 = (dossier / "essais" / "E3-T3-reponse-E.essai1.prompt.txt").read_text(encoding="utf-8")
    assert len(v8.MOTIF_PIECE.findall(prompt_e3)) == 5
    # journal : l'espèce E porte le modèle demandé, l'usage détaillé et le coût au barème
    essais_e = v8.essais_journal(dossier, "E3-T1-conception-E")
    assert len(essais_e) == 1 and essais_e[0]["modele_demande"] == "gpt-6-astra" and essais_e[0]["effort"] is None
    assert essais_e[0]["usage"]["sortie_visible"] == 50 and essais_e[0]["cout_usd"] == round(100 / 1e6 * 10 + 50 / 1e6 * 50, 4)
    assert essais_e[0]["script"] == v8.VERSION
    # le texte complet des prompts servis à E est passé par le faux serveur, avec la clé factice en en-tête seulement
    assert all(CLE_FACTICE not in l for l in (dossier / "journal.jsonl").read_text(encoding="utf-8").splitlines())


def test_refus_d_astra_regle_R831(v8, env_openai, tmp_path, capsys):
    """Un refus d'E ferme la porte comme un refus de A ou B ; l'arbitre accepte l'absence de ses cellules et le run continue."""
    faits, question = preparer_entrees(tmp_path)
    dossier = tmp_path / "run-refus"
    env_openai.defaut = "content_filter"
    args = ["etage3", "--sortie", str(dossier), "--faits", str(faits), "--question", str(question), "--plafond-usd", "100"]
    assert v8.principal(args, appelants=appelants_factices(v8)) == v8.CODE_PORTE
    assert "porte fermée après E3-T1 : ['E3-T1-conception-E']" in capsys.readouterr().err
    assert v8.statut_courant(dossier, "E3-T1-conception-E") == "REFUS"
    assert len(v8.essais_journal(dossier, "E3-T1-conception-E")) == 1  # un refus n'est jamais relancé
    assert len(list((dossier / "cellules").glob("*.md"))) == 4
    # relance sans accepter l'absence : le refus est définitif, la porte reste fermée, aucun nouvel appel à E
    env_openai.defaut = "normal"
    assert v8.principal(args, appelants=appelants_factices(v8)) == v8.CODE_PORTE
    assert len(v8.essais_journal(dossier, "E3-T1-conception-E")) == 1
    # R-831 : absence acceptée pour les trois cellules d'E, suite du même run avec les quatre autres espèces
    absences = ["E3-T1-conception-E", "E3-T2-critique-croisee-E", "E3-T3-reponse-E"]
    code = v8.principal(args + [x for a in absences for x in ("--accepter-absence", a)], appelants=appelants_factices(v8))
    assert code == v8.CODE_FINI
    assert len(list((dossier / "cellules").glob("*.md"))) == 12
    assert v8.verifier(dossier) == []
    prompt_a = (dossier / "essais" / "E3-T2-critique-croisee-A.essai1.prompt.txt").read_text(encoding="utf-8")
    assert "<<<DÉBUT PIÈCE ABSENTE E3-T1-conception-E>>>" in prompt_a and "statut : REFUS" in prompt_a
    assert [p[0] for p in v8.MOTIF_PIECE.findall(prompt_a)] == [f"E3-T1-conception-{l}" for l in "BCD"]
    etat = (dossier / "etat.md").read_text(encoding="utf-8")
    assert "| E3-T1-conception-E | REFUS | 1 |" in etat and "Absences acceptées par l'arbitre : " + ", ".join(absences) in etat
    assert env_openai.compteurs.get("content_filter", 0) + env_openai.compteurs.get("normal", 0) >= 1


def test_modele_different_arrete_le_run(v8, env_openai, tmp_path):
    faits, question = preparer_entrees(tmp_path)
    dossier = tmp_path / "run-modele"
    env_openai.defaut = "autre-modele"
    code = v8.principal(["etage3", "--sortie", str(dossier), "--faits", str(faits), "--question", str(question),
                         "--plafond-usd", "100"], appelants=appelants_factices(v8))
    assert code == v8.CODE_MODELE
    assert v8.statut_courant(dossier, "E3-T1-conception-E") == "MODELE_DIFFERENT"


def test_plafond_tient_compte_d_E(v8, env_openai, tmp_path):
    """Pire cas d'E (32000 jetons à 50 USD le million = 1,60 USD) : un plafond de 1 USD arrête avant tout appel."""
    faits, question = preparer_entrees(tmp_path)
    dossier = tmp_path / "run-plafond"
    code = v8.principal(["etage3", "--sortie", str(dossier), "--faits", str(faits), "--question", str(question),
                         "--plafond-usd", "1"], appelants=appelants_factices(v8))
    assert code == v8.CODE_PLAFOND
