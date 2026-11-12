"""Essais de `epreuve_phases_v1.py` (processeur seulement ; aucun module du programme importé).

Lancement :
    /home/user/controle-ia-travail/.venv/bin/python -I -B -m pytest -q -p no:cacheprovider --noconftest \
        -c /dev/null --rootdir DOSSIER DOSSIER/test_epreuve_phases_v1.py
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

import pytest

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import epreuve_phases_v1 as ph  # noqa: E402
import generer_items_v1 as gen  # noqa: E402

DEPOT = ICI.parents[2]
ACTIONS = DEPOT / "donnees" / "20261019-230011-p3-reel" / "textes-actions-p3.jsonl"
TACHES = DEPOT / "donnees" / "t05-pilote-v1" / "taches-pilote-60-v1.json"
BROUILLON1 = ICI / "preenregistrement-epreuve-etiqueteur-v1-brouillon1.md"
BROUILLON2 = ICI / "preenregistrement-epreuve-etiqueteur-v1-brouillon2.md"


def action(t: int, p: int) -> str:
    c = "CONTROLS: (unchanged)" if p == 9 else f"CONTROLS: Compare with baseline A{t} on dataset B{p}. Ablate part C{p}."
    return f"ACTION: ADD\nTITLE: T{t}-{p}\nPROPOSAL: Proposal {t} {p}.\n{c}\nCOST: 10 GPU-hours\nPREDICTION: x."


@pytest.fixture(scope="module")
def fabrique():
    episodes = {f"T{t:02d}": [action(t, p) for p in range(gen.N_PAS)] for t in range(gen.N_EPISODES)}
    enonces = {t: f"Task statement {t}." for t in episodes}
    items, cle, _ = gen.generer(episodes, enonces, 4242)
    return items, cle


def test_question_identique_dans_les_deux_brouillons():
    q1 = ph.extraire_question(BROUILLON1)
    if BROUILLON2.exists():
        assert ph.extraire_question(BROUILLON2) == q1
    assert q1.startswith("You will read a research plan") and q1.rstrip().endswith("<PLAN>")


def test_extraire_question_garde(tmp_path):
    f = tmp_path / "x.md"
    f.write_text("rien", encoding="utf-8")
    with pytest.raises(ph.ArretPhases):
        ph.extraire_question(f)  # artefact
    f.write_text(f"{ph.MARQUE_DEBUT}\n```text\nA <ENONCE> B <PLAN>\n```\n{ph.MARQUE_FIN}\n", encoding="utf-8")
    assert ph.extraire_question(f) == "A <ENONCE> B <PLAN>"  # cas sain


def test_rendu_depuis_les_seuls_items(fabrique):
    items, _ = fabrique
    q = ph.extraire_question(BROUILLON1)
    c = ph.rendre_consigne(items[0], q)
    assert "<ENONCE>" not in c and "<PLAN>" not in c
    assert all(f"STEP {p}:\n" in c for p in range(10))
    assert items[0]["enonce"] in c
    # garde de fuite : un champ de la clé dans l'item arrête le rendu
    with pytest.raises(ph.ArretPhases):
        ph.rendre_consigne(dict(items[0], version="jumeau"), q)


def test_mesure(fabrique):
    items, _ = fabrique
    m = ph.mesurer(items[:10], ph.extraire_question(BROUILLON1))
    assert m["items"] == 10 and m["caracteres_consigne"]["maximum"] >= m["caracteres_consigne"]["moyenne"] > 0


def test_tirage_phase2(fabrique):
    items, cle = fabrique
    t1 = ph.tirer_phase2(items, cle, 99)
    t2 = ph.tirer_phase2(items, cle, 99)
    assert gen.en_jsonl(t1) == gen.en_jsonl(t2)  # déterminisme
    assert gen.en_jsonl(t1) != gen.en_jsonl(ph.tirer_phase2(items, cle, 100))
    assert len(t1) == 80 and len({x["tache"] for x in t1}) == 20
    par_tache = defaultdict(list)
    for x in t1:
        par_tache[x["tache"]].append(x["strate"])
    for strates in par_tache.values():
        assert strates.count("jumeau") == 1
        assert sum(s.startswith("placebo") for s in strates) == 1 and len(strates) == 4
    compte = Counter(x["strate"] for x in t1)
    plantes = {s: n for s, n in compte.items() if s != "jumeau" and not s.startswith("placebo")}
    assert sum(plantes.values()) == 40 and len(plantes) == 9 and set(plantes.values()) <= {4, 5}
    assert sorted(n for s, n in compte.items() if s.startswith("placebo")) == [6, 7, 7]
    positions = defaultdict(list)
    for i, x in enumerate(t1):
        positions[x["tache"]].append(i)
    assert min(b - a for ps in positions.values() for a, b in zip(ps, ps[1:])) >= ph.ECART_MIN_PHASE2
    modifies = {c["item"]: c["pas_modifies"] for c in cle}
    for x in t1:
        if x["strate"] != "jumeau":
            assert x["pas_surligne"] in modifies[x["item"]]
        else:
            assert x["pas_surligne"] != 9  # le pas 9 n'a pas de contrôle substantiel


reelles = pytest.mark.skipif(not (ACTIONS.exists() and TACHES.exists()), reason="données du dépôt absentes")


@reelles
def test_reel_rendu_et_tirage(tmp_path):
    assert gen.principal(["--actions", str(ACTIONS), "--taches", str(TACHES), "--sortie", str(tmp_path),
                          "--entropie", "20261107"]) == 0
    items = ph.lire_jsonl(tmp_path / "items-epreuve-v1.jsonl")
    cle = ph.lire_jsonl(tmp_path / "cle-epreuve-v1.jsonl")
    q = ph.extraire_question(BROUILLON1)
    consignes = [ph.rendre_consigne(it, q) for it in items]
    assert len(consignes) == 396 and all("cibles" not in c for c in consignes)
    tirage = ph.tirer_phase2(items, cle, 20261107)
    assert len(tirage) == 80
    assert ph.principal(["phase2", "--items", str(tmp_path / "items-epreuve-v1.jsonl"), "--cle",
                         str(tmp_path / "cle-epreuve-v1.jsonl"), "--entropie", "20261107",
                         "--sortie", str(tmp_path / "p2")]) == 0
    assert json.loads((tmp_path / "p2" / "tirage-phase2-v1.jsonl").read_text(encoding="utf-8").splitlines()[0])
