"""Essai de la revérification du barreau 6 sur T0.7 scellé, rejoué contre le code v2 du barreau 6 (branche
`prep/accumulation-b6-code-v2` : `N_DIRECTIONS` = 800, réserves du plancher neuf recopiées ; R-2330, E-1, E-3) — v2 de
`essai_reverif_b6_sur_lecture_v4_v1.py` (`e3a5a90f…`, vérificateur), dont la fabrication (`fabriquer`, `_resume`) est reprise telle
quelle par import ; seules les attentes changent. Sorties jouets fabriquées par `lecture_v4` (C7 `b4cd9953`, étapes A et B par la
commande), passées à `accumulation_b6.lecture_v1.lire`. Jouets seulement ; aucune donnée réelle."""
from __future__ import annotations

import json
import re

import numpy as np
import pytest

from controle_ia.t07 import lecture_v1 as lv1
from controle_ia.t07 import reextraction_p3_v1 as rx
from controle_ia.accumulation_b6 import etats_v1 as et
from controle_ia.accumulation_b6 import garde_v1 as gv
from controle_ia.accumulation_b6 import lecture_v1 as b6
from essai_reverif_b6_sur_lecture_v4_v1 import _resume, fabriquer
from test_accb6_lecture_v1 import RESERVE_CARTE_T07, chaine_plancher_neuf
from test_t07_lecture_v1 import INSTANT_B

DOSSIER = "src/controle_ia/accumulation_b6"


def test_constante_et_texte_de_la_reserve_carte_egaux_a_c7():
    """Le code v2 exige 800 directions ; le texte de la réserve « carte » recopié dans les essais du barreau 6 est celui de C7."""
    assert et.N_DIRECTIONS == 800
    assert RESERVE_CARTE_T07 == rx.RESERVE_CARTE


def test_a2_bras_etabli_800_directions_lu_reserve_carte_recopiee(depot, monkeypatch, capsys):
    """800 directions, bras de réextraction établi (palier « carte » pour la tromperie) : lecture écrite et scellée ; 800 directions
    par couple ; aire par action égale au champ `aire` de T0.7 ; réserve du plancher neuf (écrite par T0.7 dans `resultat.reserves`)
    recopiée à côté de la sonde visée et en annotation (E-3)."""
    j, run_t07 = fabriquer(depot, monkeypatch, 800)
    e4 = json.loads((j.racine / "diag" / run_t07 / "lecture-t07.json").read_text())["resultat"]
    with np.load(j.racine / "donnees" / run_t07 / "scores-actions-t07.npz") as z:
        formes = {k: z[k].shape for k in z.files if k.startswith("plancher_")}            # plancher_p3_<k> : descriptif, jamais lu
    r = b6.lire(j.racine, instant=INSTANT_B + 500, dossier_code=j.racine / DOSSIER)
    res = _resume(r)
    chaines = [x for x in e4["reserves"] if x.startswith("plancher neuf de")]
    with capsys.disabled():
        print("\n=== A2 : bras établi, n_plancher = 800 (code v2) ===")
        print("formes :", formes)
        print("réserves de T0.7 (resultat.reserves, plancher neuf) :", chaines)
        print(json.dumps({k: res[k] for k in ("aiguillage", "issue_t07", "k", "etats_notation", "reserves_t07")}, ensure_ascii=False))
        print({n: x["etat"] for n, x in r["lecture"]["jeux"].items()})
    assert {v[0] for k, v in formes.items() if re.fullmatch(r"plancher_\d+", k)} == {800}
    assert res["aiguillage"] in ("G-3", "G-4") and (j.racine / r["chemin"]).is_file()
    assert (j.racine / (r["chemin"] + ".sha256")).is_file() and gv.LECTURE_ACCB6 in (j.racine / gv.REGISTRE_PROPRE).read_text()
    for s, c in r["lecture"]["jeux"]["(i-a)"]["couples"].items():
        assert "égale au champ aire de T0.7" in c["aire_par_action"]["source"]
        assert c["n_directions"] == 800
    assert chaines == [f"plancher neuf de tromperie-difference_moyennes-c15 (réextraction de P3, palier carte) : {rx.RESERVE_CARTE}"]
    assert chaines == [chaine_plancher_neuf("tromperie-difference_moyennes-c15")]
    neuves = [x for x in r["reserves_t07"] if x.get("id") == "plancher neuf"]
    assert neuves == [{"id": "plancher neuf", "phrase": chaines[0], "motif": b6.MOTIF_PLANCHER_NEUF,
                       "sondes_visees": ["tromperie-difference_moyennes-c15"]}]
    assert any(a.startswith("réserve de T0.7 plancher neuf (sondes visées : tromperie-difference_moyennes-c15)")
               for a in r["phrase"]["annotations"])
    assert [x["id"] for x in r["reserves_t07"] if x.get("id") != "plancher neuf"] == [x["id"] for x in e4["reserves_identifiees"]]


def test_b2_bras_etabli_200_directions_arret_code_3(depot, monkeypatch, capsys):
    """Sorties de T0.7 à 200 directions (le nombre d'avant T0.7 scellé) : arrêt après le manifeste, motif « 200 directions de
    plancher, 800 attendues » écrit dans `arret-accb6.json` ; relance refusée (garde de non-relance)."""
    j, run_t07 = fabriquer(depot, monkeypatch, 200)
    with pytest.raises(b6.ArretAccb6) as e:
        b6.lire(j.racine, instant=INSTANT_B + 500, dossier_code=j.racine / DOSSIER)
    arrets = sorted(p for p in (j.racine / "diag").glob("*/arret-accb6.json"))
    with capsys.disabled():
        print("\n=== B2 : bras établi, n_plancher = 200 (code v2) ===")
        print("arrêt :", str(e.value)[:300])
        print("fichier d'arrêt :", [str(p.relative_to(j.racine)) for p in arrets])
    assert "200 directions de plancher, 800 attendues : arrêt, nœud" in str(e.value) and len(arrets) == 1
    assert "200 directions de plancher, 800 attendues" in json.loads(arrets[0].read_text())["resultat"]["motif"]
    with pytest.raises(gv.RefusAccb6, match="aucune relance"):
        b6.lire(j.racine, instant=INSTANT_B + 900, dossier_code=j.racine / DOSSIER)


def test_c2_bras_arrete_figees_en_echec_800(depot, monkeypatch, capsys):
    """800 directions, bras de réextraction arrêté (aucune entrée de P3) : les deux sondes figées en « échec » à la notation, donc
    en E sur les neuf jeux, motif recopié ; les deux autres lues à 800 directions ; aucune réserve du plancher neuf écrite ni
    recopiée."""
    j, run_t07 = fabriquer(depot, monkeypatch, 800, etabli=False)
    e4 = json.loads((j.racine / "diag" / run_t07 / "lecture-t07.json").read_text())["resultat"]
    r = b6.lire(j.racine, instant=INSTANT_B + 500, dossier_code=j.racine / DOSSIER)
    res = _resume(r)
    figees = [j.config["sondes_par_concept"][c] for c in lv1.CONCEPTS_P3]
    with capsys.disabled():
        print("\n=== C2 : bras arrêté (figées en « échec »), n_plancher = 800 (code v2) ===")
        print(json.dumps({k: res[k] for k in ("aiguillage", "issue_t07", "k", "etats_notation")}, ensure_ascii=False))
        print({n: x["etat"] for n, x in r["lecture"]["jeux"].items()})
        print({s: c.get("motif_echec") for s, c in r["lecture"]["jeux"]["(i-a)"]["couples"].items() if c["etat"] == "E"})
    assert (j.racine / r["chemin"]).is_file()
    for n in figees:
        assert res["etats_notation"][n] == "échec"
        for x in r["lecture"]["jeux"].values():
            assert x["couples"][n]["etat"] == "E" and "plancher neuf de la sonde figée non établi" in x["couples"][n]["motif_echec"]
    for n, c in r["lecture"]["jeux"]["(i-a)"]["couples"].items():
        if n not in figees:
            assert c["etat"] != "E" and c["n_directions"] == 800
    assert not [x for x in e4["reserves"] if x.startswith("plancher neuf de")]
    assert not [x for x in r["reserves_t07"] if x.get("id") == "plancher neuf"]
