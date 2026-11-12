"""Essai de la revérification du barreau 6 sur T0.7 scellé : sorties jouets fabriquées par `lecture_v4` (C7 `b4cd9953`, étapes A et
B par la commande), passées à la lecture du barreau 6 (`accumulation_b6.lecture_v1.lire`, commit `6c98ea20`)."""
from __future__ import annotations

import json

import numpy as np
import pytest

from controle_ia.sondes.evaluation import plancher_apparie
from controle_ia.t07 import lecture_v1 as lv1
from controle_ia.t07 import lecture_v4 as lv4
from controle_ia.t07 import reextraction_p3_v1 as rx
from controle_ia.t07 import registre_v1 as rg
from controle_ia.accumulation_b6 import garde_v1 as gv
from controle_ia.accumulation_b6 import lecture_v1 as b6
import test_t07_lecture_v1 as t1
from test_t07_lecture_v1 import APRES_A, INSTANT, INSTANT_B, RUN_T06
from test_t07_lecture_v2 import construire, lignes_audit, lignes_p3bis
from test_accb6_lecture_v1 import PREREG_TEXTE, _depot, _ligne, code_jouet

METHODE = "difference_appariee_percentile"


def fabriquer(depot, monkeypatch, n_plancher, etabli=True, signal=1.0):
    monkeypatch.setattr(t1, "PAS", 10)                       # dix actions par épisode, comme 7b
    monkeypatch.setattr(b6, "N_TIRAGES", 300)
    j = construire(depot, signal=signal)
    j.config["methode_plancher"] = METHODE
    j.config["n_plancher"] = n_plancher
    j.config["plancher_figees"] = {"methode": rx.METHODE, "n_p3": 24, "tolerances": dict(rx.TOLERANCES), "garde_principale": "rapportee"}
    cfg = j.racine / "config-t07.json"
    cfg.write_text(json.dumps(j.config), encoding="utf-8")
    if etabli:
        def double(racine, config, figees, graine_de, n_pl, **kw):
            sortie = {}
            rng = np.random.default_rng(5)
            for c, s in figees.items():
                X = [rng.standard_normal((40, len(s.w))) for _ in range(3)]
                d = plancher_apparie(f"{s.nom}{rx.SUFFIXE_PLANCHER}", int(s.couche), X, s.agregation, n_pl, graine_de(f"plancher/{s.nom}"))
                carte = c == "tromperie"
                sortie[s.nom] = {"concept": c, "etat": "établi", "motif": None, "directions": d, "graine": f"plancher/{s.nom}",
                                 "palier": "carte" if carte else "identique", "reserve": rx.RESERVE_CARTE if carte else None,
                                 "reserve_principale": None, "n": len(d)}
            return {"par_sonde": sortie, "rapport": {"methode": rx.METHODE, "etat": "établi"}}
        monkeypatch.setattr(rx, "reextraire", double)
    assert lv4.main(["etape-a", str(j.racine), RUN_T06, str(cfg), "--registre", str(j.registre), "--instant", str(INSTANT)]) == 0
    run_t07 = sorted(p.name for p in (j.racine / "runs").iterdir() if p.name != RUN_T06)[-1]
    lignes_audit(j, run_t07)
    lignes_p3bis(j, APRES_A)
    assert lv4.main(["etape-b", str(j.racine), RUN_T06, run_t07, str(cfg), "--registre", str(j.registre), "--instant", str(INSTANT_B)]) == 0
    # registre propre du barreau 6
    rel_p, sha_p = _depot(j.racine, gv.PREREG, PREREG_TEXTE)
    rel_c, sha_c = code_jouet(j.racine)
    (j.racine / gv.REGISTRE_PROPRE).write_text("# Registre propre du barreau 6 (ACCB6)\n\n" + _ligne(gv.SCELLEMENT_ACCB6, INSTANT - 5000, rel_p, sha_p)
                                               + _ligne(gv.CODE_ACCB6, INSTANT - 4000, rel_c, sha_c), encoding="utf-8")
    return j, run_t07


def _resume(r):
    lec = r["lecture"]
    return {"aiguillage": r["aiguillage"]["ligne"], "issue_t07": r["aiguillage"]["issue_critere_3"],
            "k": r["sondes"]["k"], "etats_notation": {s["nom"]: s["etat_notation"] for s in r["sondes"]["sondes"]},
            "jeux": {n: {"etat": x["etat"], "couples": {s: (c["etat"], c.get("n_directions"), (c.get("aire_par_action") or {}).get("source"))
                                                        for s, c in x["couples"].items()}} for n, x in lec["jeux"].items()},
            "reserves": [x["id"] for x in r["reserves"]], "reserves_t07": [(x.get("id"), x["sondes_visees"]) for x in r["reserves_t07"]],
            "phrase": r["phrase"]["phrase_complete"]}


def test_a_bras_etabli_200_directions_lu(depot, monkeypatch, capsys):
    j, run_t07 = fabriquer(depot, monkeypatch, 200)
    e4 = json.loads((j.racine / "diag" / run_t07 / "lecture-t07.json").read_text())["resultat"]
    nota = json.loads((j.racine / "diag" / run_t07 / "notation-t07.json").read_text())["resultat"]
    r = b6.lire(j.racine, instant=INSTANT_B + 500, dossier_code=j.racine / "src/controle_ia/accumulation_b6")
    res = _resume(r)
    with capsys.disabled():
        print("\n=== A : bras établi, n_plancher = 200 ===")
        print("réserves de T0.7 (resultat.reserves, chaînes) :", [x for x in e4["reserves"] if "plancher neuf" in x])
        print("reserves_identifiees :", [x.get("id") for x in e4["reserves_identifiees"]])
        print("clés d'une entrée d'index :", sorted(nota["index"]["sondes"][0]))
        print("clés de jeux[sonde][(i-a)] :", sorted(e4["jeux"][e4["sondes_lues"][0]]["(i-a)"]))
        print(json.dumps(res, ensure_ascii=False, indent=1))
    assert res["aiguillage"] in ("G-3", "G-4") and (j.racine / r["chemin"]).is_file()
    for s, c in r["lecture"]["jeux"]["(i-a)"]["couples"].items():            # aire par action recoupée avec le champ de T0.7
        assert "égale au champ aire de T0.7" in c["aire_par_action"]["source"]
        assert c["n_directions"] == 200
    # la réserve du palier « carte » du plancher neuf (écrite par T0.7 dans resultat.reserves) n'est pas recopiée par le barreau 6
    assert [x for x in e4["reserves"] if "plancher neuf de" in x]
    assert not [x for x in r["reserves_t07"] if "plancher neuf" in json.dumps(x, ensure_ascii=False)]


def test_b_bras_etabli_800_directions_arret_code_3(depot, monkeypatch, capsys):
    j, run_t07 = fabriquer(depot, monkeypatch, 800)
    with np.load(j.racine / "donnees" / run_t07 / "scores-actions-t07.npz") as z:
        formes = {k: z[k].shape for k in z.files if k.startswith("plancher_")}
    with pytest.raises(b6.ArretAccb6) as e:
        b6.lire(j.racine, instant=INSTANT_B + 500, dossier_code=j.racine / "src/controle_ia/accumulation_b6")
    arrets = sorted(str(p.relative_to(j.racine)) for p in (j.racine / "diag").glob("*/arret-accb6.json"))
    with capsys.disabled():
        print("\n=== B : bras établi, n_plancher = 800 ===")
        print("formes :", formes)
        print("arrêt :", str(e.value)[:300])
        print("fichier d'arrêt :", arrets)
    assert "800 directions de plancher, 200 attendues" in str(e.value) and len(arrets) == 1
    with pytest.raises(gv.RefusAccb6, match="aucune relance"):                # la garde de non-relance ferme alors la lecture
        b6.lire(j.racine, instant=INSTANT_B + 900, dossier_code=j.racine / "src/controle_ia/accumulation_b6")


def test_c_bras_arrete_figees_en_echec(depot, monkeypatch, capsys):
    j, run_t07 = fabriquer(depot, monkeypatch, 200, etabli=False)
    nota = json.loads((j.racine / "diag" / run_t07 / "notation-t07.json").read_text())["resultat"]
    with np.load(j.racine / "donnees" / run_t07 / "scores-actions-t07.npz") as z:
        noms = sorted(k for k in z.files if k != "index")
    r = b6.lire(j.racine, instant=INSTANT_B + 500, dossier_code=j.racine / "src/controle_ia/accumulation_b6")
    res = _resume(r)
    figees = [j.config["sondes_par_concept"][c] for c in lv1.CONCEPTS_P3]
    with capsys.disabled():
        print("\n=== C : bras arrêté (figées en « échec ») ===")
        print("tableaux :", noms)
        print("motifs :", {e["nom"]: e.get("echec") for e in nota["index"]["sondes"] if e["etat"] != "notée"})
        print(json.dumps(res, ensure_ascii=False, indent=1))
        print({s: c.get("motif_echec") for s, c in r["lecture"]["jeux"]["(i-a)"]["couples"].items() if c["etat"] == "E"})
    for n in figees:
        assert res["etats_notation"][n] == "échec"
        for x in r["lecture"]["jeux"].values():
            assert x["couples"][n]["etat"] == "E"


def test_d_correction_proposee_800_directions_lu(depot, monkeypatch, capsys):
    """Correction proposée (E-1) : `etats_v1.N_DIRECTIONS` = 800 (ici par remplacement de la constante en mémoire) : la lecture passe
    sur des sorties de `lecture_v4` à 800 directions, bras établi."""
    from controle_ia.accumulation_b6 import etats_v1 as et
    monkeypatch.setattr(et, "N_DIRECTIONS", 800)
    j, run_t07 = fabriquer(depot, monkeypatch, 800)
    r = b6.lire(j.racine, instant=INSTANT_B + 500, dossier_code=j.racine / "src/controle_ia/accumulation_b6")
    with capsys.disabled():
        print("\n=== D : correction proposée, n_plancher = 800 ===")
        print({n: x["etat"] for n, x in r["lecture"]["jeux"].items()})
    for c in r["lecture"]["jeux"]["(i-a)"]["couples"].values():
        assert c["n_directions"] == 800 and "égale au champ aire de T0.7" in c["aire_par_action"]["source"]
