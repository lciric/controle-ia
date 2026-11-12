"""Essais de `lire_items_phase1_v2.py` : mode simulé et fausses ouvertures seulement ; aucun réseau, aucune clé réelle.

Chaque correctif de la contre-lecture 1 (B2 à B6) a son essai sur un cas sain et sur un artefact ; la version 1
(`lire_items_phase1_v1.py`, intacte) sert d'artefact là où elle montre le défaut.

Lancement (environnement vidé, pour qu'aucune variable du poste ne soit visible) :
    env -i PATH=/usr/bin:/bin /home/user/controle-ia-travail/.venv/bin/python -I -B -m pytest -q -p no:cacheprovider \
        --noconftest -c /dev/null --rootdir DOSSIER DOSSIER/test_lire_items_phase1_v2.py
"""

from __future__ import annotations

import io
import json
import sys
import urllib.error
from pathlib import Path

import pytest

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import epreuve_phases_v1 as ph  # noqa: E402
import generer_items_v2 as gen  # noqa: E402
import lire_items_phase1_v1 as lire1  # noqa: E402
import lire_items_phase1_v2 as lire  # noqa: E402

QUESTION = ICI / "preenregistrement-epreuve-etiqueteur-v1-brouillon3.md"
FAUX = "FAUX-SECRET-zqxwvutsrponmlkjhgfedcba-QWERTY"


@pytest.fixture(autouse=True)
def sans_cle_du_poste(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)  # jamais la valeur du poste, même par mégarde


def action(t: int, p: int) -> str:
    c = "CONTROLS: (unchanged)" if p == 9 else f"CONTROLS: Compare with baseline A{t} on dataset B{p}. Ablate part C{p}."
    return f"ACTION: ADD\nTITLE: T{t}-{p}\nPROPOSAL: Proposal {t} {p}.\n{c}\nCOST: 10 GPU-hours\nPREDICTION: x."


@pytest.fixture(scope="module")
def entrees(tmp_path_factory):
    d = tmp_path_factory.mktemp("entrees")
    episodes = {f"T{t:02d}": [action(t, p) for p in range(gen.N_PAS)] for t in range(gen.N_EPISODES)}
    enonces = {t: f"Task statement {t}." for t in episodes}
    items, cle, _ = gen.generer(episodes, enonces, 4242)
    f_items, _ = gen.generer_formation(episodes, enonces, 4242, 20)
    (d / "items.jsonl").write_bytes(gen.en_jsonl(items))
    (d / "formation.jsonl").write_bytes(gen.en_jsonl(f_items))
    (d / "relectures.txt").write_text("".join(c["item"] + "\n" for c in cle if c["version"] == "jumeau"),
                                      encoding="utf-8")
    return d, items, cle


def args(d: Path, sortie: Path, lectures: str, *extra) -> list:
    return ["--simule", "--lectures", lectures, "--items", str(d / "items.jsonl"), "--formation",
            str(d / "formation.jsonl"), "--relectures", str(d / "relectures.txt"), "--question", str(QUESTION),
            "--entropie", "7", "--sortie", str(sortie), *extra]


class Compteur:
    def __init__(self, pannes=None, message_exception=""):
        self.appels = []
        self.simule = lire.FournisseurSimule(pannes, message_exception=message_exception)

    def __call__(self, lecteur, lecture, item, tentative, consigne):
        self.appels.append((lecteur, lecture, item))
        return self.simule(lecteur, lecture, item, tentative, consigne)


def lancer(d, sortie, lectures, *extra, compteur=None):
    return lire.principal(args(d, sortie, lectures, *extra), appeler_simule=compteur or Compteur(), dormir=lambda s: None)


def manifeste(dossier: Path) -> dict:
    return json.loads((dossier / "manifeste-lecture-phase1-v2.json").read_text(encoding="utf-8"))


def lignes(chemin: Path) -> list:
    return [json.loads(x) for x in chemin.read_text(encoding="utf-8").splitlines() if x.strip()]


class _Corps(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


# ---------------------------------------------------------------------------------------------------------------
def test_format_des_reponses():
    bonne = "\n".join([f"STEP {n}: NO" for n in range(9)] + ['STEP 9: YES | WEAKENED | "on a single seed"'])
    assert lire.analyser_reponse("```\n" + bonne + "\n```")[9]["categorie"] == "WEAKENED"
    with pytest.raises(lire.FormatInvalide):
        lire.analyser_reponse(bonne + "\nVoici.")


def test_B2_reglages_geles_cas_sain_et_artefact(monkeypatch):
    g = lire.corps_gemini("c")["generationConfig"]
    assert g == {"temperature": 0, "maxOutputTokens": 8000, "thinkingConfig": {"thinkingBudget": 8192}}
    k = lire.corps_kimi("c")
    assert "temperature" not in k and k["max_tokens"] == 32000 and k["reasoning_effort"] == "high"
    vues = []

    def ouvrir(r):
        vues.append(json.loads(r.data))
        return _Corps(json.dumps({"model": "kimi-k3.1-pro", "usage": {"prompt_tokens": 1, "completion_tokens": 1},
                                  "choices": [{"finish_reason": "stop", "message": {"content": "x"}}]}).encode())

    lire.appeler_kimi("c", "http://127.0.0.1:8789", lire.Secrets(), ouvrir=ouvrir)  # cas sain : v2
    lire1.appeler_kimi("kimi-k3.1-pro", "c", 8000, "http://127.0.0.1:8789", ouvrir=ouvrir)  # artefact : v1
    assert "temperature" not in vues[0] and vues[0]["max_tokens"] == 32000
    assert vues[1]["temperature"] == 0 and vues[1]["max_tokens"] == 8000
    assert lire.LECTEURS["B"]["temperature_servie"] == 1.0 and lire.LECTEURS["A"]["temperature_servie"] == 0


def test_B2_temperatures_ecrites(entrees, tmp_path):
    d, _, _ = entrees
    assert lancer(d, tmp_path / "f", "format") == 0
    m = manifeste(tmp_path / "f")
    assert m["lecteurs"]["B"]["temperature_envoyee"] is None and m["lecteurs"]["B"]["temperature_servie"] == 1.0
    j = lignes(tmp_path / "f" / "journal-phase1-B-v2.jsonl")
    assert j and all(x["temperature_servie"] == 1.0 and x["temperature_envoyee"] is None for x in j)


def test_B3_garde_reserve_la_pensee_cas_sain_et_artefact(entrees, tmp_path):
    consigne = "x" * 3000
    pire_a = lire.cout_pire_cas("A", consigne)
    assert pire_a == pytest.approx(1000 / 1e6 * 10 + (8000 + 8192) / 1e6 * 50)
    assert lire1.cout_pire_cas((10.0, 50.0), consigne, 8000) < pire_a  # la v1 ne réservait pas la pensée
    d, items, _ = entrees
    # Cas sain : sorties dans la réserve, lecture complète sous le plafond.
    assert lancer(d, tmp_path / "s", "format") == 0 and manifeste(tmp_path / "s")["depense_estimee_dollars"] <= 300
    # Artefact : la pensée dépasse son budget, ou la sortie dépasse la réserve : le lecteur s'arrête aussitôt.
    f = [x["item"] for x in lignes(d / "formation.jsonl")]
    for sorte, dossier in (("pensee", "p"), ("sortie", "o")):
        c = Compteur({("A", "format", it, 1): sorte for it in f})
        assert lancer(d, tmp_path / dossier, "format", compteur=c) == 4
        m = manifeste(tmp_path / dossier)
        assert "A" in m["lecteurs_arretes"] and m["controle_format"]["feu_vert"] is False
        assert sum(1 for x in c.appels if x[0] == "A") <= 2  # au plus les appels déjà partis (deux fils)


def test_B4_essai_de_format_seul_puis_feu_vert(entrees, tmp_path):
    d, _, _ = entrees
    c = Compteur()
    assert lancer(d, tmp_path / "f", "format", compteur=c) == 0
    assert {x[1] for x in c.appels} == {"format"}  # l'essai de format est lancé seul
    m = manifeste(tmp_path / "f")
    assert m["controle_format"]["feu_vert"] is True and m["controle_format"]["motifs"] == []
    sans = Compteur()
    with pytest.raises(lire.ArretLecture):  # artefact : lecture principale sans feu vert
        lancer(d, tmp_path / "p0", "principale+relecture", compteur=sans)
    assert sans.appels == [] and not (tmp_path / "p0").exists()
    avec = Compteur()  # cas sain : avec le manifeste au feu vert
    assert lancer(d, tmp_path / "p", "principale+relecture", "--feu-vert-format",
                  str(tmp_path / "f" / "manifeste-lecture-phase1-v2.json"), compteur=avec) == 0
    assert {x[1] for x in avec.appels} == {"principale", "relecture"} and len(avec.appels) == 2 * (396 + 60)


def test_B4_feu_rouge_si_tronquee_ou_plafond(entrees, tmp_path):
    d, _, _ = entrees
    it = lignes(d / "formation.jsonl")[0]["item"]
    c = Compteur({("B", "format", it, 1): "tronquee", ("B", "format", it, 2): "tronquee"})
    assert lancer(d, tmp_path / "t", "format", compteur=c) == 6
    m = manifeste(tmp_path / "t")
    assert m["controle_format"]["feu_vert"] is False and any("tronquées" in x for x in m["controle_format"]["motifs"])
    with pytest.raises(lire.ArretLecture):
        lancer(d, tmp_path / "p", "principale+relecture", "--feu-vert-format",
               str(tmp_path / "t" / "manifeste-lecture-phase1-v2.json"))
    assert lancer(d, tmp_path / "b", "format", "--plafond-dollars", "2") in (3, 6)  # plafond trop bas : feu rouge
    assert manifeste(tmp_path / "b")["controle_format"]["feu_vert"] is False


def test_B5_rendu_controle_avant_tout_appel(entrees, tmp_path):
    d, items, _ = entrees
    faux = [dict(x) for x in items]
    faux[5]["type"] = "retirer"  # artefact : un champ de la clé glissé dans un item de la lecture principale
    e = tmp_path / "e"
    e.mkdir()
    (e / "items.jsonl").write_bytes(gen.en_jsonl(faux))
    for n in ("formation.jsonl", "relectures.txt"):
        (e / n).write_bytes((d / n).read_bytes())
    fautif = Compteur()
    assert lancer(e, tmp_path / "f", "format", compteur=fautif) == 2  # même l'essai de format rend les trois lectures
    assert fautif.appels == [] and manifeste(tmp_path / "f")["arret"].startswith("rendu")
    sain = Compteur()
    assert lancer(d, tmp_path / "ok", "format", compteur=sain) == 0 and sain.appels  # cas sain


def test_B5_rendu_fautif_aucun_appel_et_journal_garde(entrees, tmp_path):
    d, _, _ = entrees
    f = lignes(d / "formation.jsonl")
    f[3]["version"] = "jumeau"  # artefact dans les items de formation : refus au rendu, avant tout appel
    e = tmp_path / "e"
    e.mkdir()
    (e / "formation.jsonl").write_bytes(gen.en_jsonl(f))
    for n in ("items.jsonl", "relectures.txt"):
        (e / n).write_bytes((d / n).read_bytes())
    c = Compteur()
    assert lancer(e, tmp_path / "s", "format", compteur=c) == 2
    assert c.appels == []
    m = manifeste(tmp_path / "s")
    assert m["arret"].startswith("rendu") and (tmp_path / "s" / "journal-phase1-A-v2.jsonl").exists()


def test_B5_cle_refusee_arrete_tous_les_appels(entrees, tmp_path, monkeypatch):
    d, _, _ = entrees
    f = [x["item"] for x in lignes(d / "formation.jsonl")]
    c = Compteur({("A", "format", f[0], 1): "cle_refusee"})
    assert lancer(d, tmp_path / "k", "format", "--fils-par-lecteur", "1", compteur=c) == 5
    m = manifeste(tmp_path / "k")
    assert m["arret"].startswith("général")
    # après le refus, plus aucun appel ne part (au plus ceux déjà en vol : deux fils)
    rang_refus = c.appels.index(("A", "format", f[0]))
    assert len(c.appels) - rang_refus <= 2
    j = lignes(tmp_path / "k" / "journal-phase1-A-v2.jsonl")
    assert any(x["sorte"] == "cle_refusee_ou_absente" for x in j)  # journal gardé
    rb = lignes(tmp_path / "k" / "reponses-phase1-B-v2.jsonl")
    assert any(x["statut"] == "non_appele" for x in rb)  # l'autre lecteur s'arrête aussi
    # mode réel : variable absente, arrêt avant tout appel et avant toute sortie
    registre = tmp_path / "go.md"
    registre.write_text("| GO-2026-11-07-05 | 2026-11-07 | décision |\n", encoding="utf-8")
    base = args(d, tmp_path / "r", "format")[1:]
    with pytest.raises(lire.ArretLecture):
        lire.principal(["--reel", *base, "--go", "GO-2026-11-07-05", "--registre-go", str(registre), "--commit", "x"])
    assert not (tmp_path / "r").exists()


def test_B6_masquage_avant_troncature_cas_sain_et_artefact(monkeypatch):
    monkeypatch.setenv("CLE_FACTICE", FAUX)

    def ouvrir_corps(corps):
        def ouvrir(requete):
            raise urllib.error.HTTPError(requete.full_url, 400, "x", {}, io.BytesIO(corps.encode()))
        return ouvrir

    corps = "x" * 280 + FAUX
    v1 = lire1.appeler_gemini("gemini-4-argon", "c", 8000, "CLE_FACTICE", None, ouvrir=ouvrir_corps(corps))
    assert FAUX[:20] in v1.echec  # artefact : la v1 écrivait le préfixe
    s = lire.Secrets()
    v2 = lire.appeler_gemini("c", "CLE_FACTICE", s, ouvrir=ouvrir_corps(corps))
    assert not any(FAUX[i:i + 6] in v2.echec for i in range(len(FAUX) - 5))
    v2b = lire.appeler_gemini("c", "CLE_FACTICE", s, ouvrir=ouvrir_corps("refus : " + FAUX[:12] + " (tronquée)"))
    assert FAUX[:12] not in v2b.echec and "[clé]" in v2b.echec
    sain = lire.appeler_gemini("c", "CLE_FACTICE", s, ouvrir=ouvrir_corps("quota dépassé"))
    assert sain.echec == "HTTP 400 : quota dépassé"  # cas sain : rien à masquer, rien de changé


def test_B6_aucun_fragment_de_cle_dans_les_sorties(entrees, tmp_path, monkeypatch, capsys):
    d, _, _ = entrees
    monkeypatch.setenv("GEMINI_API_KEY", FAUX)
    f = [x["item"] for x in lignes(d / "formation.jsonl")]
    c = Compteur({("A", "format", f[1], 1): "exception"}, message_exception=f"jeton {FAUX[3:30]} refusé")
    lancer(d, tmp_path / "s", "format", compteur=c)
    sortie = capsys.readouterr().out
    fenetres = {FAUX[i:i + 8] for i in range(len(FAUX) - 7)}
    for fichier in (tmp_path / "s").iterdir():
        texte = fichier.read_text(encoding="utf-8")
        assert not any(w in texte for w in fenetres), fichier.name
    assert not any(w in sortie for w in fenetres)
    j = lignes(tmp_path / "s" / "journal-phase1-A-v2.jsonl")
    assert any("[clé]" in (x.get("message") or "") for x in j)  # l'exception est écrite, masquée


def test_reprises_ecrites_et_determinisme(entrees, tmp_path):
    d, _, _ = entrees
    f = [x["item"] for x in lignes(d / "formation.jsonl")]
    c = Compteur({("A", "format", f[0], 1): "transport", ("B", "format", f[1], 1): "format",
                  ("B", "format", f[1], 2): "format"})
    assert lancer(d, tmp_path / "r", "format", compteur=c) == 6  # un item illisible : feu rouge
    rb = {x["item"]: x for x in lignes(tmp_path / "r" / "reponses-phase1-B-v2.jsonl")}
    ra = {x["item"]: x for x in lignes(tmp_path / "r" / "reponses-phase1-A-v2.jsonl")}
    assert ra[f[0]]["statut"] == "ok" and ra[f[0]]["tentatives"] == 2
    assert rb[f[1]]["statut"] == "illisible" and rb[f[1]]["tentatives"] == 2
    assert (tmp_path / "r" / "reponses-phase1-B-v2.encours.jsonl").exists()
    assert lancer(d, tmp_path / "a", "format") == 0 and lancer(d, tmp_path / "b", "format") == 0
    for k in ("A", "B"):
        assert (tmp_path / "a" / f"reponses-phase1-{k}-v2.jsonl").read_bytes() == \
               (tmp_path / "b" / f"reponses-phase1-{k}-v2.jsonl").read_bytes()


def test_depense_engagee_et_modele_servi(entrees, tmp_path):
    d, _, _ = entrees
    assert lancer(d, tmp_path / "e", "format", "--plafond-dollars", "300", "--depense-engagee", "299.5") == 3
    assert manifeste(tmp_path / "e")["depense_estimee_dollars"] <= 300
    with pytest.raises(lire.ArretLecture):
        lancer(d, tmp_path / "x", "format", "--plafond-dollars", "300", "--depense-engagee", "300")
    f = [x["item"] for x in lignes(d / "formation.jsonl")]
    c = Compteur({("B", "format", it, 1): "modele" for it in f})
    assert lancer(d, tmp_path / "m", "format", compteur=c) == 4
    assert "B" in manifeste(tmp_path / "m")["lecteurs_arretes"]
