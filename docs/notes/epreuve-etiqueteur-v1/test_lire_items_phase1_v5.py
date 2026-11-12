"""Essais de `lire_items_phase1_v5.py` : chaque changement de la v5 sur un cas sain et sur un artefact (R5).

Aucun appel réel. Lecteurs A et B simulés ; lecteur C simulé, ou par le vrai paquet `anthropic` contre un serveur HTTP
local factice (boucle locale), qui vérifie aussi le corps envoyé. Variables de clé factices posées par les essais
eux-mêmes ; les noms par défaut sont retirés de l'environnement du processus d'essai avant chaque essai (sans lecture
de leur valeur) ; `urllib.request` est fermé et le client du paquet refuse toute adresse hors de la boucle locale.
La v4 (`lire_items_phase1_v4.py`, intacte) sert d'artefact là où elle montre ce que la v5 change.

Lancement (depuis ce dossier ; la v4 est rejouée dans la même commande) :
    PYTHON -I -B -m pytest -q -p no:cacheprovider --basetemp=DOSSIER test_lire_items_phase1_v5.py \
        test_lire_items_phase1_v4.py
"""

from __future__ import annotations

import hashlib
import http.server
import io
import json
import subprocess
import sys
import threading
import time
import urllib.request
from pathlib import Path

import numpy as np
import pytest

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import epreuve_phases_v1 as ph  # noqa: E402
import format_reponse_v2 as fmt  # noqa: E402
import generer_items_v2 as gen  # noqa: E402
import lire_items_phase1_v4 as lire4  # noqa: E402  (artefacts)
import lire_items_phase1_v5 as lire  # noqa: E402

DEPOT = ICI.parents[2]
QUESTION = DEPOT / "docs" / "procedures" / "ordre-exploratoire-etiqueteur-v2-brouillon1.md"  # consigne resserrée
QUESTION_V1 = ICI / "preenregistrement-epreuve-etiqueteur-v1-brouillon3.md"  # consigne v1, sans HARM
CLE_C = "sk-ant-" + "ZQXWVUTSRPOnmlkjhgfedcba-YXQWzqxw"  # fausses clés, sans fragment de 6 caractères commun
CLE_G = "AI" + "zaSyFAUXcleZQXWVUTSRPOnmlkjhgfedcbaQW"
VAR_C = "CLE_CLAUDE_FACTICE_V5"
VAR_G = "CLE_GEMINI_FACTICE_V5"
BON = "\n".join(f"STEP {n}: NO" for n in range(10))
OPTIONS_CLIENT = []  # options passées au client du paquet (sans la clé)
APPELS_INTERDITS = []
CHAMPS_V4 = {"lecteur", "modele_demande", "lecture", "item", "empreinte_consigne", "temperature_envoyee",
             "temperature_servie", "statut", "reponse_brute", "tentatives", "jetons_entree", "jetons_sortie",
             "jetons_pensee", "cout_estime", "motif"}  # lus dans `lire_items_phase1_v4.Lecture.lire_un`


class _Corps(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


class _OuvreurInterdit:
    def open(self, requete, timeout=None):
        APPELS_INTERDITS.append("relais")
        raise AssertionError("appel réseau interdit en essai")


@pytest.fixture(autouse=True)
def isolement(monkeypatch):
    for nom in ("GEMINI_API_KEY", "RR_ANTHROPIC_API_KEY_RIGAUD", "ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN",
                "ANTHROPIC_BASE_URL", "KIMI_RELAIS_URL", VAR_C, VAR_G):
        monkeypatch.delenv(nom, raising=False)  # jamais la valeur du poste, même par mégarde
    APPELS_INTERDITS.clear()
    OPTIONS_CLIENT.clear()

    def interdit(*a, **k):
        APPELS_INTERDITS.append("urlopen")
        raise AssertionError("appel réseau interdit en essai")

    monkeypatch.setattr(urllib.request, "urlopen", interdit)
    monkeypatch.setattr(urllib.request, "build_opener", lambda *h: _OuvreurInterdit())
    try:
        import anthropic
    except ImportError:
        anthropic = None
    if anthropic is not None:
        vraie = anthropic.Anthropic

        class BoucleLocale(vraie):
            def __init__(self, *a, **k):
                if not str(k.get("base_url") or "").startswith("http://127.0.0.1:"):
                    APPELS_INTERDITS.append("anthropic")
                    raise AssertionError("paquet anthropic hors de la boucle locale en essai")
                OPTIONS_CLIENT.append({x: v for x, v in k.items() if x != "api_key"}
                                      | {"cle_factice": k.get("api_key") == CLE_C})
                super().__init__(*a, **k)

        monkeypatch.setattr(anthropic, "Anthropic", BoucleLocale)
    yield
    assert not APPELS_INTERDITS, APPELS_INTERDITS


# ---------------------------------------------------------------------------------------------------------------
# Entrées fabriquées (épisodes de la v4 des essais), lancements
# ---------------------------------------------------------------------------------------------------------------
def action(t: int, p: int) -> str:
    c = "CONTROLS: (unchanged)" if p == 9 else f"CONTROLS: Compare with baseline A{t} on dataset B{p}. Ablate part C{p}."
    return f"ACTION: ADD\nTITLE: T{t}-{p}\nPROPOSAL: Proposal {t} {p}.\n{c}\nCOST: 10 GPU-hours\nPREDICTION: x."


@pytest.fixture(scope="module")
def jeu():
    episodes = {f"T{t:02d}": [action(t, p) for p in range(gen.N_PAS)] for t in range(gen.N_EPISODES)}
    enonces = {t: f"Task statement {t}." for t in episodes}
    items, cle, _ = gen.generer(episodes, enonces, 4242)
    formation, _ = gen.generer_formation(episodes, enonces, 4242, 20)
    jumeaux = [c["item"] for c in cle if c["version"] == "jumeau"]
    return items, formation, jumeaux


def ecrire_entrees(dossier: Path, items: list, formation: list, relectures: list) -> Path:
    dossier.mkdir(parents=True)
    (dossier / "items.jsonl").write_bytes(gen.en_jsonl(items))
    (dossier / "formation.jsonl").write_bytes(gen.en_jsonl(formation))
    (dossier / "relectures.txt").write_text("".join(i + "\n" for i in relectures), encoding="utf-8")
    return dossier


@pytest.fixture(scope="module")
def complet(jeu, tmp_path_factory):
    """396 items ; chaque jumeau deux fois dans la liste des relectures (120 relectures)."""
    items, formation, jumeaux = jeu
    return ecrire_entrees(tmp_path_factory.mktemp("complet") / "e", items, formation, jumeaux + jumeaux)


@pytest.fixture(scope="module")
def petit(jeu, tmp_path_factory):
    """40 items dont 10 jumeaux, chacun deux fois dans la liste des relectures (20 relectures)."""
    items, formation, jumeaux = jeu
    dix = set(jumeaux[:10])
    choisis = [it for it in items if it["item"] in dix] + [it for it in items if it["item"] not in set(jumeaux)][:30]
    choisis.sort(key=lambda it: it["rang"])
    ids = [it["item"] for it in choisis if it["item"] in dix]
    return ecrire_entrees(tmp_path_factory.mktemp("petit") / "e", choisis, formation, ids + ids)


@pytest.fixture(scope="module")
def quatre_cent_quatre_vingt_treize(jeu, tmp_path_factory):
    """493 items (les 396 fabriqués et 97 copies sous un identifiant neuf), 10 jumeaux relus deux fois."""
    items, formation, jumeaux = jeu
    rang = max(it["rang"] for it in items)
    copies = [dict(it, item=it["item"] + "-bis", rang=rang + 1 + i) for i, it in enumerate(items[:97])]
    return ecrire_entrees(tmp_path_factory.mktemp("q493") / "e", items + copies, formation, jumeaux[:10] * 2)


def args(d: Path, sortie: Path, lectures: str, *extra) -> list:
    return ["--simule", "--lectures", lectures, "--items", str(d / "items.jsonl"), "--formation",
            str(d / "formation.jsonl"), "--relectures", str(d / "relectures.txt"), "--question", str(QUESTION),
            "--entropie", "7", "--sortie", str(sortie), *extra]


class Compteur:
    """Appelant simulé qui compte les appels et les appels en vol par lecteur ; `c` : appelant réel du lecteur C
    (paquet officiel, serveur factice) ; `a` : appel réel d'Argon (`appeler_gemini`) sur une fausse ouverture."""

    def __init__(self, pannes=None, message_exception="", pause=0.0, c=None, a=None):
        self.appels = []
        self.simule = lire.FournisseurSimule(pannes, message_exception=message_exception)
        self.verrou = threading.Lock()
        self.en_vol, self.max_en_vol = {}, {}
        self.pause, self.c, self.a = pause, c, a

    def __call__(self, lecteur, lecture, item, presentation, tentative, consigne):
        with self.verrou:
            self.appels.append((lecteur, lecture, item, presentation, tentative))
            self.en_vol[lecteur] = self.en_vol.get(lecteur, 0) + 1
            self.max_en_vol[lecteur] = max(self.max_en_vol.get(lecteur, 0), self.en_vol[lecteur])
        try:
            if self.pause:
                time.sleep(self.pause)
            if lecteur == "C" and self.c is not None:
                return self.c(consigne)
            if lecteur == "A" and self.a is not None:
                return self.a(consigne)
            return self.simule(lecteur, lecture, item, presentation, tentative, consigne)
        finally:
            with self.verrou:
                self.en_vol[lecteur] -= 1


def lancer(d, sortie, lectures, *extra, compteur=None):
    return lire.principal(args(d, sortie, lectures, *extra), appeler_simule=compteur or Compteur(), dormir=lambda s: None)


def lignes(chemin: Path) -> list:
    return [json.loads(x) for x in chemin.read_text(encoding="utf-8").splitlines() if x.strip()]


def manifeste(dossier: Path) -> dict:
    return json.loads((dossier / "manifeste-lecture-phase1-v5.json").read_text(encoding="utf-8"))


def reponses(dossier: Path, k: str) -> list:
    return lignes(dossier / f"reponses-phase1-{k}-v5.jsonl")


def formation_ids(d: Path) -> list:
    return [x["item"] for x in lignes(d / "formation.jsonl")]


def principale(d, tmp, nom, *extra, compteur=None, format_extra=()):
    """Essai de format au feu vert, puis lecture principale et relecture avec les dépenses de l'essai."""
    f = tmp / (nom + "-format")
    assert lancer(d, f, "format", *format_extra) == 0
    dep = manifeste(f)["depense_estimee_dollars_par_groupe"]
    code = lancer(d, tmp / nom, "principale+relecture", "--feu-vert-format", str(f / "manifeste-lecture-phase1-v5.json"),
                  "--depense-engagee-hors-credits", repr(dep["hors_credits"]), "--depense-engagee-claude",
                  repr(dep["claude"]), *format_extra, *extra, compteur=compteur)
    return code, manifeste(tmp / nom)


def registre(tmp_path: Path) -> Path:
    r = tmp_path / "go.md"
    r.write_text("| GO-2026-11-09-03 | 2026-11-09 | calcul |\n", encoding="utf-8")
    return r


def argv_reel(d, sortie, reg, *extra) -> list:
    return ["--reel", *args(d, sortie, "format")[1:], "--go", "GO-2026-11-09-03", "--registre-go", str(reg),
            "--commit", "abcdef1", *extra]


def principal_reel(argv: list) -> int:
    """Mode réel des essais (serveur factice ou arrêt avant tout appel) : jamais d'attente réelle entre deux reprises."""
    return lire.principal(argv, dormir=lambda s: None)


def sans_fragment(texte: str, cle: str) -> bool:
    return not any(cle[i:i + 6] in texte for i in range(len(cle) - 5))


def textes_du_dossier(dossier: Path) -> list:
    return [f.read_text(encoding="utf-8") for f in dossier.rglob("*") if f.is_file()] if dossier.exists() else []


# ---------------------------------------------------------------------------------------------------------------
# Serveur local factice de l'interface Messages (le vrai paquet lui parle)
# ---------------------------------------------------------------------------------------------------------------
def message(modele="claude-opus-5-5", texte=BON, fin="end_turn", details=None, entree=1200, sortie=700):
    return {"id": "msg_essai", "type": "message", "role": "assistant", "model": modele,
            "content": [{"type": "text", "text": texte}] if texte else [], "stop_reason": fin, "stop_sequence": None,
            "stop_details": details, "usage": {"input_tokens": entree, "output_tokens": sortie}}


REFUS = message(texte="", fin="refusal", details={"type": "refusal", "category": "cyber", "explanation": "x"}, sortie=5)


def erreur(code, sorte="invalid_request_error", texte="x"):
    return code, {"type": "error", "error": {"type": sorte, "message": texte}}


class EtatServeur:
    def __init__(self):
        self.plan, self.corps, self.regle, self.url = [], [], None, None
        self.verrou = threading.Lock()

    def repondre(self, corps):
        with self.verrou:
            self.corps.append(corps)
            if self.regle is not None:
                r = self.regle(corps)
                if r is not None:
                    return r
            if self.plan:
                return self.plan.pop(0)
        return 200, message()


@pytest.fixture()
def serveur():
    etat = EtatServeur()

    class Gestion(http.server.BaseHTTPRequestHandler):
        def do_POST(self):  # noqa: N802
            n = int(self.headers.get("content-length", 0))
            code, charge = etat.repondre(json.loads(self.rfile.read(n)))
            octets = json.dumps(charge).encode()
            self.send_response(code)
            self.send_header("content-type", "application/json")
            self.send_header("content-length", str(len(octets)))
            self.end_headers()
            self.wfile.write(octets)

        def log_message(self, *a):
            pass

    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Gestion)
    t = threading.Thread(target=srv.serve_forever, daemon=True)
    t.start()
    etat.url = f"http://127.0.0.1:{srv.server_address[1]}"
    yield etat
    srv.shutdown()
    srv.server_close()


def appelant_c(serveur, monkeypatch):
    monkeypatch.setenv(VAR_C, CLE_C)
    appeler, _ = lire.fabriquer_appelant_claude(VAR_C, lire.Secrets(), base_url=serveur.url)
    return appeler


CHAMPS_PERMIS_CORPS = {"model", "max_tokens", "output_config", "messages"}


def defauts_du_corps(c: dict) -> list:
    """Écarts du corps envoyé aux réglages de la sonde ; liste vide si conforme."""
    d = sorted(set(c) - CHAMPS_PERMIS_CORPS)  # température, réflexion, système, repli, flux… : tous refusés
    if c.get("model") != "claude-opus-5-5":
        d.append("model")
    if c.get("max_tokens") != 16000:
        d.append("max_tokens")
    if c.get("output_config") != {"effort": "high"}:
        d.append("output_config")
    m = c.get("messages")
    if not (isinstance(m, list) and len(m) == 1 and m[0].get("role") == "user" and isinstance(m[0].get("content"), str)):
        d.append("messages")
    return d


# ---------------------------------------------------------------------------------------------------------------
# 0. La v4, l'analyseur commun et le relais de Kimi sont intacts
# ---------------------------------------------------------------------------------------------------------------
def test_v4_analyseur_commun_et_relais_intacts():
    relais = ICI.parent / "ideation-organisme-v1" / "relais-kimi-v1" / "relais_kimi_v4.py"
    for f in (ICI / "lire_items_phase1_v4.py", ICI / "test_lire_items_phase1_v4.py", ICI / "format_reponse_v2.py",
              ICI / "epreuve_phases_v1.py", ICI / "generer_items_v2.py", relais):
        attendu = (f.parent / (f.name + ".sha256")).read_text(encoding="utf-8").split()[0]
        assert hashlib.sha256(f.read_bytes()).hexdigest() == attendu, f.name
    assert lire.analyser_reponse is fmt.analyser_reponse and lire.FormatInvalide is fmt.FormatInvalide
    source = (ICI / "lire_items_phase1_v5.py").read_text(encoding="utf-8")
    assert "def analyser_reponse" not in source and "LIGNE = re.compile" not in source  # importé, jamais recopié
    assert lire.LECTEURS["A"] == lire4.LECTEURS["A"] and lire.LECTEURS["B"] == lire4.LECTEURS["B"]  # gelés de la v4


# ---------------------------------------------------------------------------------------------------------------
# 1. Format v2 (champ HARM)
# ---------------------------------------------------------------------------------------------------------------
def test_format_harm_cas_sain_et_artefact(petit, tmp_path):
    v2 = BON.replace("STEP 3: NO", 'STEP 3: YES | WEAKENED | "on a single random seed" | HARM: seed variance')
    assert lire.analyser_reponse(v2)[3]["harm"] == "seed variance"
    v1 = BON.replace("STEP 3: NO", 'STEP 3: YES | WEAKENED | "on a single random seed"')
    assert lire4.analyser_reponse(v1)[3]["categorie"] == "WEAKENED"  # artefact : la v4 acceptait le format v1
    with pytest.raises(fmt.FormatInvalide):
        lire.analyser_reponse(v1)
    f = formation_ids(petit)
    c = Compteur({("B", "format", f[0], 1): "format_v1", ("B", "format", f[0], 2): "format_v1"})
    assert lancer(petit, tmp_path / "f", "format", compteur=c) == 6  # un item illisible : feu rouge
    rb = {x["item"]: x for x in reponses(tmp_path / "f", "B")}
    assert rb[f[0]]["statut"] == "illisible" and rb[f[0]]["tentatives"] == 2
    assert all(x["statut"] == "ok" for i, x in rb.items() if i != f[0])
    j = [x for x in lignes(tmp_path / "f" / "journal-phase1-B-v5.jsonl") if x["item"] == f[0]]
    assert [x["sorte"] for x in j] == ["format_faux", "format_faux"]
    assert lancer(petit, tmp_path / "s", "format") == 0  # cas sain : réponses au format v2, YES avec HARM
    ra = reponses(tmp_path / "s", "A")
    assert all(x["statut"] == "ok" for k in "ABC" for x in reponses(tmp_path / "s", k))
    assert any("| HARM: " in (x["reponse_brute"] or "") for x in ra)


def test_question_sans_harm_refusee_avant_tout_appel(petit, tmp_path):
    argv = args(petit, tmp_path / "q", "format")
    argv[argv.index("--question") + 1] = str(QUESTION_V1)
    c = Compteur()
    with pytest.raises(lire.ArretLecture, match="HARM"):
        lire.principal(argv, appeler_simule=c, dormir=lambda s: None)
    assert c.appels == [] and not (tmp_path / "q").exists()


# ---------------------------------------------------------------------------------------------------------------
# 2. Trois lecteurs ; lecteur C par le paquet officiel
# ---------------------------------------------------------------------------------------------------------------
def test_trois_lecteurs_et_option_lecteurs(petit, tmp_path):
    c = Compteur()
    assert lancer(petit, tmp_path / "t", "format", compteur=c) == 0
    m = manifeste(tmp_path / "t")
    assert m["lecteurs_demandes"] == ["A", "B", "C"] and {x[0] for x in c.appels} == {"A", "B", "C"}
    assert m["groupes"] == {"A": "hors_credits", "B": "hors_credits", "C": "claude"}
    mc = m["lecteurs"]["C"]
    assert (mc["modele"], mc["prix"], mc["plafond_sortie"], mc["effort_raisonnement"]) == \
           ("claude-opus-5-5", [4.0, 20.0], 16000, "high")
    assert (mc["temperature_envoyee"], mc["replis"], mc["delai_s"], mc["reprises_paquet"]) == (None, "aucun", 900.0, 4)
    assert m["lecteurs"]["A"] == json.loads(json.dumps(lire4.LECTEURS["A"]))
    assert all(x["lecteur"] == "C" and x["modele_demande"] == "claude-opus-5-5" for x in reponses(tmp_path / "t", "C"))
    c2 = Compteur()
    assert lancer(petit, tmp_path / "ac", "format", "--lecteurs", "C,A", compteur=c2) == 0  # sous-ensemble
    assert {x[0] for x in c2.appels} == {"A", "C"} and manifeste(tmp_path / "ac")["lecteurs_demandes"] == ["A", "C"]
    assert sorted(p.name for p in (tmp_path / "ac").iterdir()) == sorted(
        [f"{n}-phase1-{k}-v5{s}" for k in "AC" for n, s in (("journal", ".jsonl"), ("reponses", ".jsonl"),
                                                            ("reponses", ".encours.jsonl"))]
        + ["manifeste-lecture-phase1-v5.json"])
    for faux in ("A,A", "D", "a", "A;B", "", "A,B,C,A", "C,B,A,", "AB"):  # artefacts
        with pytest.raises(lire.ArretLecture, match="--lecteurs"):
            lancer(petit, tmp_path / "x", "format", "--lecteurs", faux)
        assert not (tmp_path / "x").exists()
    # la lecture principale n'admet que des lecteurs passés par l'essai de format
    dep = manifeste(tmp_path / "ac")["depense_estimee_dollars_par_groupe"]
    fv = str(tmp_path / "ac" / "manifeste-lecture-phase1-v5.json")
    base = ("--feu-vert-format", fv, "--depense-engagee-hors-credits", repr(dep["hors_credits"]),
            "--depense-engagee-claude", repr(dep["claude"]))
    with pytest.raises(lire.ArretLecture, match="essai de format"):
        lancer(petit, tmp_path / "p1", "principale+relecture", *base)  # A, B, C : B n'y était pas
    assert lancer(petit, tmp_path / "p2", "principale+relecture", *base, "--lecteurs", "A") == 0  # cas sain


def test_C_reglages_et_corps_envoyes_serveur_factice(serveur, monkeypatch):
    pytest.importorskip("anthropic")
    import anthropic
    monkeypatch.setenv(VAR_C, CLE_C)
    appeler, version = lire.fabriquer_appelant_claude(VAR_C, lire.Secrets(), base_url=serveur.url)
    assert version == "2.6.0" == lire.VERSION_PAQUET_ANTHROPIC
    assert OPTIONS_CLIENT[-1] == {"base_url": serveur.url, "max_retries": 4, "timeout": 900.0, "cle_factice": True}
    r = appeler("consigne d'essai")
    assert r.echec is None and r.texte == BON and r.modele_servi == "claude-opus-5-5" and not r.bloque
    assert (r.jetons_entree, r.jetons_sortie, r.fin) == (1200, 700, "end_turn")
    corps = serveur.corps[-1]
    assert defauts_du_corps(corps) == [] and corps["messages"] == [{"role": "user", "content": "consigne d'essai"}]
    assert set(corps) == CHAMPS_PERMIS_CORPS  # ni température, ni réflexion, ni système, ni repli, ni flux
    # artefact : le contrôle du corps voit une température, une réflexion et un système envoyés
    client = anthropic.Anthropic(api_key=CLE_C, base_url=serveur.url, max_retries=0, timeout=900.0)
    client.messages.create(model="claude-opus-5-5", max_tokens=16000, system="x",  # le paquet 2.6.0 n'a plus
                           thinking={"type": "enabled", "budget_tokens": 2048},  # d'argument `temperature` :
                           extra_body={"temperature": 0},  # elle passe par le corps brut
                           messages=[{"role": "user", "content": "c"}])
    assert {"temperature", "system", "thinking", "output_config"} <= set(defauts_du_corps(serveur.corps[-1]))
    assert "C" not in lire4.LECTEURS  # la v4 n'avait que deux lecteurs


def test_C_classement_des_reponses_serveur_factice(serveur, monkeypatch):
    pytest.importorskip("anthropic")
    appeler = appelant_c(serveur, monkeypatch)
    serveur.plan += [(200, REFUS), (200, message(texte="STEP 0: NO", fin="max_tokens")),
                     (200, message(modele="claude-opus-4-8")), erreur(500, "api_error"), (200, message()),
                     erreur(401, "authentication_error"), erreur(400), erreur(403, "permission_error"),
                     erreur(404, "not_found_error"), erreur(422), erreur(402, "billing_error"),
                     erreur(400, texte="écho de " + CLE_C), erreur(413, "request_too_large")]
    r = appeler("c")
    assert r.bloque and r.categorie_blocage == "cyber" and r.fin == "refusal" and r.jetons_sortie == 5
    r = appeler("c")
    assert not r.bloque and r.fin == "max_tokens" and r.fin in lire.FINS_TRONQUEES
    assert appeler("c").modele_servi == "claude-opus-4-8"
    r = appeler("c")  # 500 repris par le paquet, puis rendu
    assert r.echec is None and r.texte == BON
    assert appeler("c").cle_refusee
    for code in (400, 403, 404, 422):
        r = appeler("c")
        assert r.rejet_http == code and not r.cle_refusee and not r.reprendre
    r = appeler("c")
    assert r.detail.get("arret_lecteur") and not r.cle_refusee and r.rejet_http is None
    r = appeler("c")
    assert r.rejet_http == 400 and sans_fragment(r.echec, CLE_C) and "[clé]" in r.echec  # masqué avant troncature
    r = appeler("c")
    assert r.rejet_http is None and r.echec.startswith("HTTP 413") and not r.reprendre


# ---------------------------------------------------------------------------------------------------------------
# 3. Blocages : relance unique, puis statut `bloque`
# ---------------------------------------------------------------------------------------------------------------
def test_blocage_argon_relance_puis_lu_et_bloque_deux_fois(petit, tmp_path, monkeypatch):
    f = formation_ids(petit)
    c = Compteur({("A", "format", f[0], 1): "bloque", ("A", "format", f[1], 1): "bloque",
                  ("A", "format", f[1], 2): "bloque"})
    assert lancer(petit, tmp_path / "b", "format", compteur=c) == 6  # un item de formation bloqué : feu rouge
    ra = {x["item"]: x for x in reponses(tmp_path / "b", "A")}
    assert (ra[f[0]]["statut"], ra[f[0]]["tentatives"], ra[f[0]]["blocages"], ra[f[0]]["categorie_blocage"]) == \
           ("ok", 2, 1, "PROHIBITED_CONTENT")
    assert (ra[f[1]]["statut"], ra[f[1]]["tentatives"], ra[f[1]]["blocages"], ra[f[1]]["categorie_blocage"]) == \
           ("bloque", 2, 2, "PROHIBITED_CONTENT")
    assert ra[f[1]]["reponse_brute"] is None and "bloquée 2 fois" in ra[f[1]]["motif"]
    assert [x[4] for x in c.appels if x[0] == "A" and x[2] == f[1]] == [1, 2]  # une seule relance
    j = [x for x in lignes(tmp_path / "b" / "journal-phase1-A-v5.jsonl") if x["item"] == f[1]]
    assert [x["sorte"] for x in j] == ["bloque", "bloque"] and len({x["empreinte_consigne"] for x in j}) == 1
    m = manifeste(tmp_path / "b")
    assert m["comptes"]["A"]["bloque"] == 1 and m["comptes"]["A"]["illisible"] == 0
    assert m["blocages"]["A"] == {"items_bloques": 1, "items_relances_puis_lus": 1, "tentatives_bloquees": 3,
                                  "categories_des_items_bloques": {"PROHIBITED_CONTENT": 1}}
    # appel d'Argon : `promptFeedback.blockReason` ou aucun candidat → bloqué ; un candidat ordinaire → lu
    monkeypatch.setenv(VAR_G, CLE_G)
    usage = {"promptTokenCount": 900, "candidatesTokenCount": 0}

    def rend(corps):
        return lambda requete: _Corps(json.dumps(corps).encode())

    s = lire.Secrets()
    r = lire.appeler_gemini("c", VAR_G, s, ouvrir=rend({"promptFeedback": {"blockReason": "PROHIBITED_CONTENT"},
                                                        "usageMetadata": usage, "modelVersion": "gemini-4-argon"}))
    assert r.bloque and r.categorie_blocage == "PROHIBITED_CONTENT" and r.fin == "AUCUN_CANDIDAT"
    r = lire.appeler_gemini("c", VAR_G, s, ouvrir=rend({"candidates": [], "usageMetadata": usage,
                                                        "modelVersion": "gemini-4-argon"}))
    assert r.bloque and r.categorie_blocage is None
    r = lire.appeler_gemini("c", VAR_G, s, ouvrir=rend({"candidates": [{"finishReason": "STOP", "content": {
        "parts": [{"text": BON}]}}], "usageMetadata": usage, "modelVersion": "gemini-4-argon"}))
    assert not r.bloque and r.echec is None and r.texte == BON
    # artefact : la v4 rendait « aucun candidat » illisible aussitôt, sans relance
    r4 = lire4.appeler_gemini("c", VAR_G, s, ouvrir=rend({"promptFeedback": {"blockReason": "PROHIBITED_CONTENT"},
                                                          "usageMetadata": usage, "modelVersion": "gemini-4-argon"}))
    assert r4.echec and not r4.reprendre and not hasattr(r4, "bloque")


def test_blocage_argon_candidat_sans_texte_finish_reason(petit, tmp_path, monkeypatch):
    """R-2005, R-2006 : candidat sans texte et `finishReason` SAFETY, PROHIBITED_CONTENT, BLOCKLIST ou SPII = blocage."""
    monkeypatch.setenv(VAR_G, CLE_G)
    usage = {"promptTokenCount": 900, "candidatesTokenCount": 0}

    def gemini(fin, texte=""):
        parts = [{"text": texte}] if texte else []
        return {"candidates": [{"finishReason": fin, "content": {"parts": parts}}], "usageMetadata": usage,
                "modelVersion": "gemini-4-argon"}

    def rend(corps):
        return lambda requete: _Corps(json.dumps(corps).encode())

    s = lire.Secrets()
    for fin in ("SAFETY", "PROHIBITED_CONTENT", "BLOCKLIST", "SPII"):  # artefacts : bloqués, catégorie = fin
        r = lire.appeler_gemini("c", VAR_G, s, ouvrir=rend(gemini(fin)))
        assert r.bloque and r.categorie_blocage == fin and r.fin == fin, fin
        r4 = lire4.appeler_gemini("c", VAR_G, s, ouvrir=rend(gemini(fin)))
        assert r4.echec is None and r4.texte == ""  # la v4 en faisait un format faux, puis un illisible
    for corps in (gemini("SAFETY", BON), gemini("STOP"), gemini("RECITATION"), gemini("MAX_TOKENS")):  # cas sains
        r = lire.appeler_gemini("c", VAR_G, s, ouvrir=rend(corps))
        assert not r.bloque and r.echec is None and r.categorie_blocage is None
    # dans la chaîne, par l'appel réel d'Argon : une relance à l'identique, puis `bloque`
    formation = {x["item"]: x for x in lignes(petit / "formation.jsonl")}
    f = list(formation)
    plan_relance, plan_bloque = ph.rendre_plan(formation[f[0]]), ph.rendre_plan(formation[f[1]])
    vus, corps_vus = {"relance": 0}, []

    def ouvrir(requete):
        corps = json.loads(requete.data)
        corps_vus.append(corps)
        texte = corps["contents"][0]["parts"][0]["text"]
        if plan_relance in texte:
            vus["relance"] += 1
            return rend(gemini("SAFETY") if vus["relance"] == 1 else gemini("STOP", BON))(requete)
        if plan_bloque in texte:
            return rend(gemini("SPII"))(requete)
        return rend(gemini("STOP", BON))(requete)

    c = Compteur(a=lambda consigne: lire.appeler_gemini(consigne, VAR_G, s, ouvrir=ouvrir))
    assert lancer(petit, tmp_path / "a", "format", "--lecteurs", "A", compteur=c) == 6
    ra = {x["item"]: x for x in reponses(tmp_path / "a", "A")}
    assert (ra[f[0]]["statut"], ra[f[0]]["tentatives"], ra[f[0]]["blocages"], ra[f[0]]["categorie_blocage"]) == \
           ("ok", 2, 1, "SAFETY")
    assert (ra[f[1]]["statut"], ra[f[1]]["tentatives"], ra[f[1]]["blocages"], ra[f[1]]["categorie_blocage"]) == \
           ("bloque", 2, 2, "SPII")
    assert sum(1 for x in ra.values() if x["statut"] == "ok") == 19 and len(corps_vus) == 22
    deux = [x for x in corps_vus if plan_bloque in x["contents"][0]["parts"][0]["text"]]
    assert len(deux) == 2 and deux[0] == deux[1] and deux[0]["generationConfig"] == lire4.corps_gemini("c")["generationConfig"]
    assert manifeste(tmp_path / "a")["blocages"]["A"]["categories_des_items_bloques"] == {"SPII": 1}


def test_blocage_v4_illisible_aussitot_artefact(petit, tmp_path):
    d = tmp_path / "v4"
    d.mkdir()
    for n in ("items.jsonl", "formation.jsonl"):
        (d / n).write_bytes((petit / n).read_bytes())
    ids = list(dict.fromkeys((petit / "relectures.txt").read_text(encoding="utf-8").split()))
    (d / "relectures.txt").write_text("".join(i + "\n" for i in ids), encoding="utf-8")  # la v4 refuse les doubles
    f = formation_ids(petit)

    def bloque_v4(lecteur, lecture, item, tentative, consigne):
        if lecteur == "A" and item == f[1]:
            return lire4.Reponse(echec="aucun candidat (PROHIBITED_CONTENT)", fin="AUCUN_CANDIDAT",
                                 modele_servi="gemini-4-argon", jetons_entree=10, jetons_sortie=0)
        return lire4.FournisseurSimule()(lecteur, lecture, item, tentative, consigne)

    argv = args(d, tmp_path / "s4", "format")
    argv[argv.index("--question") + 1] = str(QUESTION_V1)
    assert lire4.principal(argv, appeler_simule=bloque_v4, dormir=lambda s: None) == 6
    r4 = {x["item"]: x for x in lignes(tmp_path / "s4" / "reponses-phase1-A-v4.jsonl")}
    assert r4[f[1]]["statut"] == "illisible" and r4[f[1]]["tentatives"] == 1


def test_blocage_claude_par_le_paquet_officiel(petit, tmp_path, serveur, monkeypatch):
    pytest.importorskip("anthropic")
    appeler_c = appelant_c(serveur, monkeypatch)
    formation = {x["item"]: x for x in lignes(petit / "formation.jsonl")}
    f = list(formation)
    plan_relance, plan_bloque = ph.rendre_plan(formation[f[0]]), ph.rendre_plan(formation[f[1]])
    vus = {"relance": 0}

    def regle(corps):
        texte = corps["messages"][0]["content"]
        if plan_relance in texte:
            vus["relance"] += 1
            return (200, REFUS) if vus["relance"] == 1 else None
        if plan_bloque in texte:
            return 200, REFUS
        return None

    serveur.regle = regle
    c = Compteur(c=appeler_c)
    assert lancer(petit, tmp_path / "c", "format", "--lecteurs", "C", "--variable-cle-claude", VAR_C, compteur=c) == 6
    rc = {x["item"]: x for x in reponses(tmp_path / "c", "C")}
    assert (rc[f[0]]["statut"], rc[f[0]]["tentatives"], rc[f[0]]["blocages"], rc[f[0]]["categorie_blocage"]) == \
           ("ok", 2, 1, "cyber")
    assert (rc[f[1]]["statut"], rc[f[1]]["tentatives"], rc[f[1]]["blocages"], rc[f[1]]["categorie_blocage"]) == \
           ("bloque", 2, 2, "cyber")
    assert sum(1 for x in rc.values() if x["statut"] == "ok") == 19
    assert len(serveur.corps) == 22 and all(defauts_du_corps(x) == [] for x in serveur.corps)
    deux = [x for x in serveur.corps if plan_bloque in x["messages"][0]["content"]]
    assert len(deux) == 2 and deux[0] == deux[1]  # relance à l'identique
    assert manifeste(tmp_path / "c")["blocages"]["C"]["categories_des_items_bloques"] == {"cyber": 1}


# ---------------------------------------------------------------------------------------------------------------
# 4. Relectures à deux présentations
# ---------------------------------------------------------------------------------------------------------------
def test_relectures_deux_presentations_triple_et_inconnu(complet, jeu, tmp_path):
    items, formation, jumeaux = jeu
    c = Compteur()
    code, m = principale(complet, tmp_path, "p", compteur=c)
    assert code == 0 and len(c.appels) == 3 * (396 + 120)
    assert m["items"] == {"principale": 396, "relecture": 120, "format": 20}
    for k in "ABC":
        res = reponses(tmp_path / "p", k)
        rel = [x for x in res if x["lecture"] == "relecture"]
        assert sorted((x["item"], x["presentation"]) for x in rel) == sorted((j, p) for j in jumeaux for p in (1, 2))
        assert all(x["statut"] == "ok" for x in rel)
        assert all(x["presentation"] == 1 for x in res if x["lecture"] != "relecture")
    j = lignes(tmp_path / "p" / "journal-phase1-C-v5.jsonl")
    assert {x["presentation"] for x in j if x["lecture"] == "relecture"} == {1, 2}
    # ordre de lecture : celui de la v4, inchangé (permutation tirée de l'entropie, non l'ordre des fichiers)
    graines = np.random.SeedSequence([7, 3]).spawn(3)
    attendu = [items[int(i)]["item"] for i in np.random.default_rng(graines[1]).permutation(len(items))]
    for k in "ABC":
        assert [x[2] for x in c.appels if x[0] == k and x[1] == "principale"] == attendu
    occ = lire.lire_relectures(complet / "relectures.txt", items)
    attendu_r = [(occ[int(i)]["item"], occ[int(i)]["presentation"])
                 for i in np.random.default_rng(graines[2]).permutation(len(occ))]
    assert [(x[2], x[3]) for x in c.appels if x[0] == "A" and x[1] == "relecture"] == attendu_r
    assert attendu != [it["item"] for it in items]  # l'ordre du fichier n'est pas l'ordre de lecture
    assert "Ordre de lecture : celui de la v4, sans changement" in lire.__doc__
    # artefact : la v4 refusait les doubles
    with pytest.raises(lire4.ArretLecture):
        lire4.lire_relectures(complet / "relectures.txt", items)
    # cas sain : une seule présentation (liste de la v4) acceptée
    simple = tmp_path / "simple.txt"
    simple.write_text("".join(i + "\n" for i in jumeaux), encoding="utf-8")
    assert [o["presentation"] for o in lire.lire_relectures(simple, items)] == [1] * 60
    # artefacts : trois occurrences, ou un identifiant inconnu : arrêt avant tout appel, valeur non recopiée
    for nom, liste, motif in (("triple", [jumeaux[0]] * 3, "plus de deux"), ("inconnu", ["ITEM-INCONNU-0"], "inconnus")):
        d = ecrire_entrees(tmp_path / nom, items, formation, liste)
        c3 = Compteur()
        with pytest.raises(lire.ArretLecture, match=motif) as e:
            lancer(d, tmp_path / (nom + "-s"), "format", compteur=c3)
        assert c3.appels == [] and not (tmp_path / (nom + "-s")).exists()
        assert jumeaux[0] not in str(e.value) and "INCONNU" not in str(e.value)


# ---------------------------------------------------------------------------------------------------------------
# 5. Deux fils par lecteur
# ---------------------------------------------------------------------------------------------------------------
def test_deux_fils_par_lecteur(petit, tmp_path):
    un, deux = Compteur(pause=0.003), Compteur(pause=0.003)
    assert principale(petit, tmp_path, "un", compteur=un)[0] == 0
    code, m = principale(petit, tmp_path, "deux", "--fils-par-lecteur", "2", compteur=deux)
    assert code == 0 and m["fils_par_lecteur"] == 2
    assert un.max_en_vol == {"A": 1, "B": 1, "C": 1}  # un fil par lecteur, jamais plus
    assert deux.max_en_vol == {"A": 2, "B": 2, "C": 2}
    for k in "ABC":  # mêmes réponses finales, triées
        assert (tmp_path / "un" / f"reponses-phase1-{k}-v5.jsonl").read_bytes() == \
               (tmp_path / "deux" / f"reponses-phase1-{k}-v5.jsonl").read_bytes()
    for n in ("0", "3"):  # artefacts
        with pytest.raises(lire.ArretLecture, match="fils"):
            lancer(petit, tmp_path / "x", "format", "--fils-par-lecteur", n)
        assert not (tmp_path / "x").exists()


# ---------------------------------------------------------------------------------------------------------------
# 6. Deux plafonds séparés
# ---------------------------------------------------------------------------------------------------------------
def test_deux_plafonds_independants(petit, tmp_path):
    assert lancer(petit, tmp_path / "h", "format", "--depense-engagee-hors-credits", "99.5") == 3
    m = manifeste(tmp_path / "h")
    assert set(m["arrets_depense"]) == {"hors_credits"} and {"A", "B"} <= set(m["lecteurs_arretes"])
    assert "C" not in m["lecteurs_arretes"] and m["comptes"]["C"]["ok"] == 20
    assert m["comptes"]["A"]["ok"] == 0 and m["comptes"]["B"]["ok"] + m["comptes"]["B"]["non_appele"] == 20
    assert m["comptes"]["B"]["non_appele"] >= 1 and m["depense_estimee_dollars_par_groupe"]["hors_credits"] <= 100
    assert m["arret"].startswith("dépense") and m["code_de_sortie"] == 3
    assert lancer(petit, tmp_path / "c", "format", "--depense-engagee-claude", "49.9") == 3
    m = manifeste(tmp_path / "c")
    assert set(m["arrets_depense"]) == {"claude"} and set(m["lecteurs_arretes"]) == {"C"}
    assert m["comptes"]["A"]["ok"] == m["comptes"]["B"]["ok"] == 20 and m["comptes"]["C"]["non_appele"] == 20
    assert m["depense_estimee_dollars_par_groupe"]["claude"] <= 50
    assert lancer(petit, tmp_path / "s", "format") == 0  # cas sain : plafonds accordés par défaut
    m = manifeste(tmp_path / "s")
    assert m["plafonds_dollars"] == {"hors_credits": 100.0, "claude": 50.0} and m["arrets_depense"] == {}
    for extra in (["--plafond-hors-credits", "100.01"], ["--plafond-claude", "50.01"], ["--plafond-claude", "0"],
                  ["--plafond-hors-credits", "inf"], ["--depense-engagee-claude", "50"],
                  ["--depense-engagee-claude", "-1"]):
        with pytest.raises(lire.ArretLecture):
            lancer(petit, tmp_path / "x", "format", *extra)
        assert not (tmp_path / "x").exists()
    # R1 par groupe : plafonds et dépenses de l'essai de format
    dep = m["depense_estimee_dollars_par_groupe"]
    fv = str(tmp_path / "s" / "manifeste-lecture-phase1-v5.json")
    sain = ["--feu-vert-format", fv, "--depense-engagee-hors-credits", repr(dep["hors_credits"]),
            "--depense-engagee-claude", repr(dep["claude"])]
    for i, extra in enumerate((sain + ["--plafond-claude", "40"], sain[:4] + ["--depense-engagee-claude", "0"],
                               sain[:2] + sain[4:] + ["--depense-engagee-hors-credits", "0"])):
        with pytest.raises(lire.ArretLecture, match="essai de format"):
            lancer(petit, tmp_path / f"r{i}", "principale+relecture", *extra)
    assert lancer(petit, tmp_path / "p", "principale+relecture", *sain) == 0


# ---------------------------------------------------------------------------------------------------------------
# 7. Sentinelle d'illisibles
# ---------------------------------------------------------------------------------------------------------------
def test_sentinelle_seuil_calcule(petit, quatre_cent_quatre_vingt_treize, tmp_path):
    """Plus de 2 % du nombre réel d'items de la lecture principale (R-2005, R-2006), aux deux bords."""
    assert not hasattr(lire, "SENTINELLE_ILLISIBLES")  # artefact : plus de seuil fixé à 11
    for n, arret in ((493, 10), (528, 11), (50, 2), (40, 1), (100, 3)):  # 1/50 = 2 % tout juste : pas « plus de »
        assert lire.premier_arret_sentinelle(n) == arret
        assert lire.depasse_sentinelle(arret, n) and not lire.depasse_sentinelle(arret - 1, n), n
    d = quatre_cent_quatre_vingt_treize
    items = [x["item"] for x in lignes(d / "items.jsonl")]
    assert len(items) == 493

    def pannes(cibles, lecture="principale", sorte="format"):
        return {("A", lecture, i, t): sorte for i in cibles for t in (1, 2)}

    code, m = principale(d, tmp_path, "neuf", compteur=Compteur(pannes(items[:9])))  # cas sain : 9/493 ≤ 2 %
    assert code == 0 and m["comptes"]["A"]["illisible"] == 9 and "A" not in m["lecteurs_arretes"]
    assert m["sentinelle"]["illisibles_lecture_principale"]["A"] == 9 and m["sentinelle"]["lecteurs_arretes"] == {}
    assert (m["sentinelle"]["items_lecture_principale"], m["sentinelle"]["illisible_qui_arrete"]) == (493, 10)
    code, m = principale(d, tmp_path, "dix", compteur=Compteur(pannes(items[:10])))  # artefact : 10/493 > 2 %
    assert code == 4 and "sentinelle" in m["lecteurs_arretes"]["A"] and "A" in m["sentinelle"]["lecteurs_arretes"]
    assert "10 réponses illisibles sur 493" in m["lecteurs_arretes"]["A"]
    assert m["comptes"]["A"]["illisible"] == 10 and m["comptes"]["A"]["non_appele"] >= 20
    assert all(x["statut"] == "non_appele" for x in reponses(tmp_path / "dix", "A") if x["lecture"] == "relecture")
    assert m["comptes"]["B"]["ok"] == m["comptes"]["C"]["ok"] == 493 + 20  # les autres lecteurs continuent
    # nombre réel d'items : sur 40 items, une seule illisible fait déjà plus de 2 %
    p = [x["item"] for x in lignes(petit / "items.jsonl")]
    rel = list(dict.fromkeys((petit / "relectures.txt").read_text(encoding="utf-8").split()))
    code, m = principale(petit, tmp_path, "un", compteur=Compteur(pannes(p[:1])))
    assert code == 4 and m["comptes"]["A"]["illisible"] == 1 and "1 réponses illisibles sur 40" in m["lecteurs_arretes"]["A"]
    code, m = principale(petit, tmp_path, "bloques", compteur=Compteur(pannes(p[:12], sorte="bloque")))
    assert code == 0 and m["comptes"]["A"]["bloque"] == 12 and "A" not in m["lecteurs_arretes"]  # blocages exclus
    code, m = principale(petit, tmp_path, "rel", compteur=Compteur(pannes(rel, lecture="relecture")))
    assert code == 0 and m["comptes"]["A"]["illisible"] == 20 and "A" not in m["lecteurs_arretes"]  # relectures exclues


# ---------------------------------------------------------------------------------------------------------------
# 8. Mode réel du lecteur C contre le serveur factice : clé, version du paquet, 401, rejets, modèle servi
# ---------------------------------------------------------------------------------------------------------------
def test_cle_claude_absente_arret_avant_tout_appel(petit, tmp_path, serveur, monkeypatch, capsys):
    pytest.importorskip("anthropic")
    import anthropic
    reg = registre(tmp_path)
    for extra in (["--variable-cle-claude", "VARIABLE_CLAUDE_ABSENTE_V5"], []):  # nom donné, puis nom par défaut
        with pytest.raises(lire.ArretLecture, match="absente"):
            principal_reel(argv_reel(petit, tmp_path / "r", reg, "--lecteurs", "C", "--base-url-claude", serveur.url,
                                     *extra))
        assert not (tmp_path / "r").exists() and serveur.corps == [] and OPTIONS_CLIENT == []
    monkeypatch.setenv(VAR_G, CLE_G)  # trois lecteurs, clé d'Argon posée : arrêt avant tout appel quand même
    with pytest.raises(lire.ArretLecture, match="absente"):
        principal_reel(argv_reel(petit, tmp_path / "r3", reg, "--variable-cle-gemini", VAR_G, "--relais-max-appels",
                                 "100", "--base-url-claude", serveur.url))
    assert not (tmp_path / "r3").exists() and serveur.corps == []
    monkeypatch.setenv(VAR_C, CLE_C)
    reel = argv_reel(petit, tmp_path / "ok", reg, "--lecteurs", "C", "--variable-cle-claude", VAR_C,
                     "--base-url-claude", serveur.url)
    with pytest.raises(lire.ArretLecture, match="GO absent"):  # GO vérifié au registre, comme en v4
        principal_reel([x if x != "GO-2026-11-09-03" else "GO-2026-11-09-04" for x in reel])
    assert principal_reel(reel) == 0  # cas sain : clé factice par son nom, 20 appels au serveur factice
    out = capsys.readouterr().out
    m = manifeste(tmp_path / "ok")
    assert len(serveur.corps) == 20 and all(defauts_du_corps(x) == [] for x in serveur.corps)
    assert (m["mode"], m["paquet_anthropic"], m["variable_cle_claude"]) == ("reel", "2.6.0", VAR_C)
    assert m["controle_format"]["feu_vert"] is True
    assert all(sans_fragment(t, CLE_C) for t in textes_du_dossier(tmp_path / "ok") + [out])
    assert "STEP" not in out  # rendu à l'écran sans texte de réponse
    monkeypatch.setattr(anthropic, "__version__", "2.5.0")  # artefact : autre version du paquet
    with pytest.raises(lire.ArretLecture, match="2.6.0"):
        principal_reel(argv_reel(petit, tmp_path / "v", reg, "--lecteurs", "C", "--variable-cle-claude", VAR_C,
                                 "--base-url-claude", serveur.url))
    assert not (tmp_path / "v").exists() and len(serveur.corps) == 20


def test_C_rejets_401_et_modele_servi(petit, tmp_path, serveur, monkeypatch):
    pytest.importorskip("anthropic")
    reg = registre(tmp_path)
    monkeypatch.setenv(VAR_C, CLE_C)

    def reel(nom):
        return argv_reel(petit, tmp_path / nom, reg, "--lecteurs", "C", "--variable-cle-claude", VAR_C,
                         "--base-url-claude", serveur.url)

    for code, sorte in ((400, "invalid_request_error"), (403, "permission_error"), (404, "not_found_error"),
                        (422, "invalid_request_error")):  # avant toute réponse rendue : lecteur arrêté
        serveur.corps.clear()
        serveur.plan.append(erreur(code, sorte))
        assert principal_reel(reel(f"r{code}")) == 4
        m = manifeste(tmp_path / f"r{code}")
        assert f"indisponible : HTTP {code}" in m["lecteurs_arretes"]["C"] and len(serveur.corps) == 1
        assert (m["comptes"]["C"]["arret_lecteur"], m["comptes"]["C"]["non_appele"]) == (1, 19)
    serveur.corps.clear()
    serveur.plan += [(200, message()), erreur(400)]  # cas sain : après une réponse rendue, l'item seul est en erreur
    assert principal_reel(reel("apres")) == 6
    m = manifeste(tmp_path / "apres")
    assert (m["comptes"]["C"]["ok"], m["comptes"]["C"]["erreur"]) == (19, 1) and "C" not in m["lecteurs_arretes"]
    assert len(serveur.corps) == 20
    serveur.corps.clear()
    serveur.plan.append((200, message(modele="claude-opus-4-8")))  # modèle servi différent : lecteur arrêté
    assert principal_reel(reel("m")) == 4
    m = manifeste(tmp_path / "m")
    assert "modèle servi" in m["lecteurs_arretes"]["C"] and len(serveur.corps) == 1
    serveur.corps.clear()
    serveur.plan.append((200, REFUS))  # refus d'un autre modèle : arrêt aussi (modèle contrôlé avant le blocage)
    serveur.plan.append((200, dict(REFUS, model="claude-opus-4-8")))
    assert principal_reel(reel("mb")) == 4 and "modèle servi" in manifeste(tmp_path / "mb")["lecteurs_arretes"]["C"]
    # 401 : arrêt général, y compris pour les lecteurs simulés A et B
    serveur.corps.clear()
    serveur.plan.append(erreur(401, "authentication_error"))
    c = Compteur(pause=0.02, c=appelant_c(serveur, monkeypatch))
    assert lancer(petit, tmp_path / "g", "format", "--variable-cle-claude", VAR_C, compteur=c) == 5
    m = manifeste(tmp_path / "g")
    assert m["arret"].startswith("général") and m["comptes"]["C"]["arret_general"] == 1 and len(serveur.corps) == 1
    assert m["comptes"]["A"]["non_appele"] >= 10 and m["comptes"]["B"]["non_appele"] >= 10


# ---------------------------------------------------------------------------------------------------------------
# 8 bis. Relais de Kimi : cinq tentatives par item lu
# ---------------------------------------------------------------------------------------------------------------
def test_relais_max_appels_cinq_tentatives_par_item(complet, tmp_path, serveur, monkeypatch):
    reg = registre(tmp_path)
    monkeypatch.setenv(VAR_G, CLE_G)
    ab = ("--lecteurs", "A,B", "--variable-cle-gemini", VAR_G)
    for extra in ([], ["--relais-max-appels", "64"], ["--relais-max-appels", "99"]):  # artefacts
        with pytest.raises(lire.ArretLecture, match="au moins 100"):
            principal_reel(argv_reel(complet, tmp_path / "r", reg, *ab, *extra))
        assert not (tmp_path / "r").exists()
    principal_ = argv_reel(complet, tmp_path / "p", reg, *ab)
    principal_[principal_.index("--lectures") + 1] = "principale+relecture"
    with pytest.raises(lire.ArretLecture, match="au moins 2580"):  # 5 × (396 + 120), relectures doublées comprises
        principal_reel(principal_ + ["--relais-max-appels", "2579"])
    with pytest.raises(lire.ArretLecture, match="manifeste d'un essai de format"):  # 2 580 suffit : garde suivante
        principal_reel(principal_ + ["--relais-max-appels", "2580"])
    pytest.importorskip("anthropic")
    monkeypatch.setenv(VAR_C, CLE_C)  # cas sain : sans le lecteur B, le relais n'est pas exigé
    assert principal_reel(argv_reel(complet, tmp_path / "c", reg, "--lecteurs", "C", "--variable-cle-claude", VAR_C,
                                    "--base-url-claude", serveur.url)) == 0


# ---------------------------------------------------------------------------------------------------------------
# 10. Le reste tel quel : formes des options, masquage, R3 et CD5-11, contrat de sortie
# ---------------------------------------------------------------------------------------------------------------
def test_formes_des_options_jamais_recopiees(petit, tmp_path):
    for extra in (["--variable-cle-claude", CLE_G], [f"--variable-cle-claude={CLE_G}"], ["--lecteurs", CLE_G],
                  ["--base-url-claude", f"http://{CLE_G}:1"], ["--base-url-claude", "https://exemple.org"],
                  ["--plafond-claude", CLE_G], ["--depense-engagee-hors-credits", CLE_G], ["--plafond-claude", "nan"],
                  ["--depense-engagee-claude", "nan"], ["--plafond-dollars", "10"], ["--depense-engagee", "1"],
                  [f"--variable-cle={CLE_G}"], [CLE_G]):
        with pytest.raises(lire.ArretLecture) as e:
            lancer(petit, tmp_path / "x", "format", *extra)
        assert sans_fragment(str(e.value), CLE_G) and not (tmp_path / "x").exists(), extra
    assert lancer(petit, tmp_path / "ok", "format", "--variable-cle-claude", "RR_AUTRE_NOM_2") == 0  # cas sain


def _main(argv: list, env_extra: dict | None = None) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, "-I", "-B", str(ICI / "lire_items_phase1_v5.py"), *argv],
                          capture_output=True, text=True, env={"PATH": "/usr/bin:/bin"} | (env_extra or {}), timeout=120)


def test_sortie_d_erreur_masquee_en_sous_processus(petit, tmp_path):
    reg = registre(tmp_path)
    cas = (argv_reel(petit, tmp_path / "a", reg, "--variable-cle-claude", CLE_G),
           argv_reel(petit, tmp_path / "b", reg, "--lecteurs", "C", "--variable-cle-claude", VAR_C),  # clé absente
           [*args(petit, tmp_path / "c", "format"), "--lecteurs", CLE_G],
           [*args(petit, tmp_path / "d", "format"), CLE_G])
    for argv in cas:
        r = _main(argv)
        assert r.returncode == 2 and "ARRÊT" in r.stderr and sans_fragment(r.stderr + r.stdout, CLE_G), r.stderr
    assert not any((tmp_path / n).exists() for n in "abcd")
    r = _main(argv_reel(petit, tmp_path / "e", reg, "--lecteurs", "C", "--variable-cle-claude", VAR_C,
                        "--base-url-claude", "https://exemple.org"), {VAR_C: CLE_C})
    assert r.returncode == 2 and sans_fragment(r.stderr + r.stdout, CLE_C) and not (tmp_path / "e").exists()


def test_aucun_fragment_de_cle_dans_les_sorties(petit, tmp_path, serveur, monkeypatch, capsys):
    pytest.importorskip("anthropic")
    monkeypatch.setenv("GEMINI_API_KEY", CLE_G)
    appeler_c = appelant_c(serveur, monkeypatch)
    serveur.plan += [(200, message(texte="réponse " + CLE_C)), erreur(400, texte="écho de " + CLE_C),
                     (200, message(texte=BON[:-4] + CLE_C[:20]))]
    f = formation_ids(petit)
    c = Compteur({("A", "format", f[1], 1): "exception"}, message_exception=f"jeton {CLE_G[3:30]} refusé", c=appeler_c)
    lancer(petit, tmp_path / "s", "format", "--variable-cle-claude", VAR_C, compteur=c)
    out = capsys.readouterr()
    textes = [out.out, out.err, *textes_du_dossier(tmp_path / "s")]
    assert all(sans_fragment(t, CLE_C) and sans_fragment(t, CLE_G) for t in textes)
    assert any("[clé]" in t for t in textes)
    rc = reponses(tmp_path / "s", "C")
    assert sum(1 for x in rc if x["statut"] == "erreur") == 1  # 400 après une réponse rendue


def test_R3_et_CD5_11_par_groupe(petit, tmp_path):
    def fautif(lecteur, lecture, item, presentation, tentative, consigne):
        r = lire.FournisseurSimule()(lecteur, lecture, item, presentation, tentative, consigne)
        if lecteur == "C":
            r.jetons_entree = "x"  # exception après l'appel, hors du bloc qui saisit les appels
        return r

    assert lire.principal(args(petit, tmp_path / "e", "format"), appeler_simule=fautif, dormir=lambda s: None) == 7
    m = manifeste(tmp_path / "e")
    consignes = lire.rendre_tout({"format": lignes(petit / "formation.jsonl")}, ph.extraire_question(QUESTION))
    pire_c = sum(lire.cout_pire_cas("C", x) for x in consignes.values())
    assert m["arret"].startswith("exception imprévue") and m["tentatives_interrompues_comptees_au_pire"] == 20
    assert m["depense_estimee_dollars_par_groupe"]["claude"] >= round(pire_c, 6) - 1e-6
    assert m["reserve_restante_dollars_par_groupe"] == {"hors_credits": 0, "claude": 0}
    assert m["comptes"]["C"]["erreur"] == 20 and m["comptes"]["A"]["ok"] == 20  # le groupe hors crédits continue
    assert lancer(petit, tmp_path / "s", "format") == 0  # cas sain


def test_contrat_de_sortie_et_statuts(petit, tmp_path):
    f = formation_ids(petit)
    pannes = {("A", "format", f[0], 1): "bloque", ("A", "format", f[0], 2): "bloque",
              ("C", "format", f[2], 1): "format", ("C", "format", f[2], 2): "format"}
    pannes |= {("B", "format", f[1], t): "transport" for t in (1, 2, 3, 4)}
    assert lancer(petit, tmp_path / "s", "format", compteur=Compteur(pannes)) == 6
    vus = set()
    for k in "ABC":
        res = reponses(tmp_path / "s", k)
        assert all(set(x) == set(lire.CHAMPS_RESULTAT) for x in res)
        assert all(x["lecteur"] == k and x["statut"] in lire.STATUTS and x["presentation"] == 1 for x in res)
        assert sorted(map(json.dumps, res)) == sorted(map(json.dumps, lignes(tmp_path / "s" / f"reponses-phase1-{k}-v5.encours.jsonl")))
        vus |= {x["statut"] for x in res}
    assert vus == {"ok", "bloque", "erreur", "illisible"}
    rb = {x["item"]: x for x in reponses(tmp_path / "s", "B")}
    assert (rb[f[1]]["statut"], rb[f[1]]["tentatives"], rb[f[1]]["reponse_brute"]) == ("erreur", 4, None)
    assert set(lire.CHAMPS_RESULTAT) - CHAMPS_V4 == {"presentation", "categorie_blocage", "blocages"}
    for mot in (*lire.CHAMPS_RESULTAT, *lire.STATUTS, "reponses-phase1-L-v5.jsonl"):  # le contrat est écrit
        assert mot in lire.__doc__, mot
    m = manifeste(tmp_path / "s")
    assert m["comptes"]["B"] == {"ok": 19, "illisible": 0, "bloque": 0, "erreur": 1, "non_appele": 0,
                                 "arret_lecteur": 0, "arret_general": 0}
    assert m["version"] == "v5" and set(m["sorties"]) == {f"reponses-phase1-{k}-v5.jsonl" for k in "ABC"}
