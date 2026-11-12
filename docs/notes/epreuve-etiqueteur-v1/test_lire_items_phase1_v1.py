"""Essais de `lire_items_phase1_v1.py` : mode simulé seulement, aucun réseau, aucune clé réelle.

Lancement :
    /home/user/controle-ia-travail/.venv/bin/python -I -B -m pytest -q -p no:cacheprovider --noconftest \
        -c /dev/null --rootdir DOSSIER DOSSIER/test_lire_items_phase1_v1.py
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
import analyser_phase1_v1 as an  # noqa: E402
import generer_items_v1 as gen  # noqa: E402
import lire_items_phase1_v1 as lire  # noqa: E402

QUESTION = ICI / "preenregistrement-epreuve-etiqueteur-v1-brouillon2.md"
SECRET = "sk-FAUX-SECRET-0123456789"


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
    (d / "relectures.txt").write_text(an.liste_relectures(cle), encoding="utf-8")
    (d / "cle.jsonl").write_bytes(gen.en_jsonl(cle))
    return d, items, cle


def args(d: Path, sortie: Path, *extra) -> list:
    return ["--simule", "--items", str(d / "items.jsonl"), "--formation", str(d / "formation.jsonl"),
            "--relectures", str(d / "relectures.txt"), "--question", str(QUESTION), "--entropie", "7",
            "--sortie", str(sortie), *extra]


def lignes(chemin: Path) -> list:
    return [json.loads(x) for x in chemin.read_text(encoding="utf-8").splitlines() if x.strip()]


# ---------------------------------------------------------------------------------------------------------------
def test_format_des_reponses():
    bonne = "\n".join([f"STEP {n}: NO" for n in range(9)] + ['STEP 9: YES | WEAKENED | "on a "single" seed"'])
    r = lire.analyser_reponse("```\n" + bonne + "\n```\n")
    assert r[9] == {"pas": 9, "oui": True, "categorie": "WEAKENED", "citation": 'on a "single" seed'}
    assert lire.analyser_reponse(bonne.replace("STEP 3: NO", "STEP 3: YES | ABSENT"))[3]["categorie"] == "ABSENT"
    for faux in ("\n".join(f"STEP {n}: NO" for n in range(9)),  # neuf lignes
                 bonne.replace("STEP 3:", "STEP 4:"),  # ordre
                 bonne + "\nVoici ma réponse.",  # texte en trop
                 bonne.replace("STEP 2: NO", "STEP 2: MAYBE")):
        with pytest.raises(lire.FormatInvalide):
            lire.analyser_reponse(faux)


def test_simule_bout_en_bout_et_determinisme(entrees, tmp_path):
    d, items, _ = entrees
    assert lire.principal(args(d, tmp_path / "a"), dormir=lambda s: None) == 0
    assert lire.principal(args(d, tmp_path / "b"), dormir=lambda s: None) == 0
    for k in ("A", "B"):
        ra = (tmp_path / "a" / f"reponses-phase1-{k}-v1.jsonl").read_bytes()
        assert ra == (tmp_path / "b" / f"reponses-phase1-{k}-v1.jsonl").read_bytes()
        r = lignes(tmp_path / "a" / f"reponses-phase1-{k}-v1.jsonl")
        assert len(r) == 20 + 396 + 60 and all(x["statut"] == "ok" for x in r)
        assert {x["lecture"] for x in r} == {"format", "principale", "relecture"}
    m = json.loads((tmp_path / "a" / "manifeste-lecture-phase1-v1.json").read_text(encoding="utf-8"))
    assert m["mode"] == "simule" and m["entropie"] == 7 and m["temperature"] == 0
    assert m["plafond_jetons_sortie"] == 8000 and set(m["entrees"]) == {"items", "formation", "relectures",
                                                                         "texte_question", "question"}
    assert 0 < m["depense_estimee_dollars"] <= m["plafond_dollars"] and m["arret"] is None
    with pytest.raises(lire.ArretLecture):  # dossier existant : on n'écrase jamais
        lire.principal(args(d, tmp_path / "a"), dormir=lambda s: None)


def test_garde_depense_cas_sain_et_artefact(entrees, tmp_path):
    d, _, _ = entrees
    g = lire.GardeDepense(1.0)
    g.reserver(0.6)
    g.regler(0.6, 0.5)  # cas sain
    with pytest.raises(lire.ArretDepense):
        g.reserver(0.6)  # artefact : 0,5 + 0,6 > 1
    with pytest.raises(lire.ArretDepense):
        g.reserver(0.01)  # une garde arrêtée le reste
    with pytest.raises(lire.ArretLecture):
        lire.GardeDepense(0)
    # Course entière sous un plafond trop bas : arrêt écrit, rien au-delà du plafond.
    assert lire.principal(args(d, tmp_path / "bas", "--plafond-dollars", "2"), dormir=lambda s: None) == 3
    m = json.loads((tmp_path / "bas" / "manifeste-lecture-phase1-v1.json").read_text(encoding="utf-8"))
    assert m["arret"] and m["arret"].startswith("dépense")
    journal = lignes(tmp_path / "bas" / "journal-phase1-A-v1.jsonl") + lignes(tmp_path / "bas" / "journal-phase1-B-v1.jsonl")
    assert sum(x["cout_estime"] for x in journal) <= 2.0 and m["depense_estimee_dollars"] <= 2.0
    r = lignes(tmp_path / "bas" / "reponses-phase1-A-v1.jsonl")
    assert any(x["statut"] == "non_appele" for x in r)
    # Cas sain : plafond large, aucune lecture refusée.
    assert lire.principal(args(d, tmp_path / "haut", "--plafond-dollars", "300"), dormir=lambda s: None) == 0


def test_reprises_ecrites_sans_repli_silencieux(entrees, tmp_path):
    d, items, _ = entrees
    x, y = items[0]["item"], items[1]["item"]
    pannes = {("A", "principale", x, 1): "transport", ("B", "principale", y, 1): "format",
              ("B", "principale", y, 2): "format"}
    attentes = []
    code = lire.principal(args(d, tmp_path / "p"), appeler_simule=lire.FournisseurSimule(pannes),
                          dormir=attentes.append)
    assert code == 0 and attentes == [10]
    ra = {r["item"]: r for r in lignes(tmp_path / "p" / "reponses-phase1-A-v1.jsonl") if r["lecture"] == "principale"}
    rb = {r["item"]: r for r in lignes(tmp_path / "p" / "reponses-phase1-B-v1.jsonl") if r["lecture"] == "principale"}
    assert ra[x]["statut"] == "ok" and ra[x]["tentatives"] == 2
    assert rb[y]["statut"] == "illisible" and rb[y]["tentatives"] == 2 and "format faux" in rb[y]["motif"]
    ja = [j for j in lignes(tmp_path / "p" / "journal-phase1-A-v1.jsonl") if j["item"] == x and j["lecture"] == "principale"]
    jb = [j for j in lignes(tmp_path / "p" / "journal-phase1-B-v1.jsonl") if j["item"] == y and j["lecture"] == "principale"]
    assert [j["sorte"] for j in sorted(ja, key=lambda j: j["tentative"])] == ["erreur", "ok"]
    assert [j["sorte"] for j in jb] == ["format_faux", "format_faux"]


def test_erreur_de_transport_persistante(entrees, tmp_path):
    d, items, _ = entrees
    x = items[2]["item"]
    pannes = {("A", "principale", x, n): "transport" for n in range(1, 5)}
    lire.principal(args(d, tmp_path / "t"), appeler_simule=lire.FournisseurSimule(pannes), dormir=lambda s: None)
    r = {r["item"]: r for r in lignes(tmp_path / "t" / "reponses-phase1-A-v1.jsonl") if r["lecture"] == "principale"}
    assert r[x]["statut"] == "illisible" and r[x]["tentatives"] == 4 and r[x]["motif"].startswith("erreur")


def test_modele_servi_different_arrete_le_lecteur(entrees, tmp_path):
    d, items, _ = entrees
    pannes = {("B", "format", it["item"], 1): "modele" for it in lignes(d / "formation.jsonl")}
    code = lire.principal(args(d, tmp_path / "m"), appeler_simule=lire.FournisseurSimule(pannes), dormir=lambda s: None)
    assert code == 4
    m = json.loads((tmp_path / "m" / "manifeste-lecture-phase1-v1.json").read_text(encoding="utf-8"))
    assert "B" in m["lecteurs_arretes"] and "A" not in m["lecteurs_arretes"]
    rb = lignes(tmp_path / "m" / "reponses-phase1-B-v1.jsonl")
    assert all(r["statut"] in ("arret_lecteur", "non_appele") for r in rb if r["lecture"] == "principale")


def test_cle_jamais_ecrite_ni_affichee(entrees, tmp_path, monkeypatch, capsys):
    d, items, _ = entrees
    monkeypatch.setenv("GEMINI_API_KEY", SECRET)
    lire.principal(args(d, tmp_path / "s"), dormir=lambda s: None)
    for f in (tmp_path / "s").iterdir():
        assert SECRET not in f.read_text(encoding="utf-8")
    assert SECRET not in capsys.readouterr().out
    # Appel réel remplacé par une fausse ouverture : la clé ne va que dans l'en-tête, et l'erreur la masque.
    vues = []

    def ouvrir(requete):
        vues.append(requete)
        raise urllib.error.HTTPError(requete.full_url, 503, "x", {}, io.BytesIO(f"refus pour {SECRET}".encode()))

    rep = lire.appeler_gemini("gemini-4-argon", "consigne", 8000, "GEMINI_API_KEY", None, ouvrir=ouvrir)
    assert rep.echec and SECRET not in rep.echec and "[clé]" in rep.echec and rep.reprendre
    assert vues[0].get_header("X-goog-api-key") == SECRET and SECRET not in vues[0].full_url
    corps = json.loads(vues[0].data)
    assert corps["generationConfig"] == {"temperature": 0, "maxOutputTokens": 8000}
    monkeypatch.delenv("GEMINI_API_KEY")
    assert lire.appeler_gemini("gemini-4-argon", "c", 8000, "GEMINI_API_KEY", None).echec == "variable GEMINI_API_KEY absente"


class _Corps(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def test_lecture_des_reponses_des_fournisseurs(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", SECRET)
    g = {"modelVersion": "gemini-4-argon", "usageMetadata": {"promptTokenCount": 100, "candidatesTokenCount": 20,
                                                              "thoughtsTokenCount": 300},
         "candidates": [{"finishReason": "STOP", "content": {"parts": [{"text": "pensée", "thought": True},
                                                                      {"text": "STEP 0: NO"}]}}]}
    rep = lire.appeler_gemini("gemini-4-argon", "c", 8000, "GEMINI_API_KEY", 2000,
                              ouvrir=lambda r: _Corps(json.dumps(g).encode()))
    assert rep.texte == "STEP 0: NO" and rep.jetons_sortie == 320 and rep.modele_servi == "gemini-4-argon"
    k = {"model": "kimi-k3.1-pro", "usage": {"prompt_tokens": 50, "completion_tokens": 9},
         "choices": [{"finish_reason": "stop", "message": {"content": "STEP 0: NO"}}]}
    vues = []

    def ouvrir(r):
        vues.append(r)
        return _Corps(json.dumps(k).encode())

    rep = lire.appeler_kimi("kimi-k3.1-pro", "c", 8000, "http://127.0.0.1:8789", ouvrir=ouvrir)
    assert rep.texte == "STEP 0: NO" and rep.jetons_entree == 50 and json.loads(vues[0].data)["temperature"] == 0
    assert lire.appeler_kimi("kimi-k3.1-pro", "c", 8000, "https://ailleurs.example").echec.startswith("relais")


def test_mode_reel_refuse_sans_go_et_plafond_de_jetons_gele(entrees, tmp_path):
    d, _, _ = entrees
    base = args(d, tmp_path / "r")[1:]
    with pytest.raises(lire.ArretLecture):
        lire.principal(["--reel", *base])  # aucun GO
    registre = tmp_path / "go.md"
    registre.write_text("| GO-2026-11-07-05 | 2026-11-07 | décision |\n", encoding="utf-8")
    with pytest.raises(lire.ArretLecture):
        lire.principal(["--reel", *base, "--go", "GO-2099-01-01-01", "--registre-go", str(registre)])
    with pytest.raises(lire.ArretLecture):
        lire.principal(args(d, tmp_path / "j", "--plafond-jetons", "9000"))
    assert not (tmp_path / "r").exists()
