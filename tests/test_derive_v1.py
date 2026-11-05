"""Test de dérive paramétré (couche 2, v1, P-18) : chaque garde sur un cas sain et un artefact (R5)."""
import numpy as np
import pytest

from controle_ia.couche2 import derive_v1 as dv
from controle_ia.gardes import GardeArret

CELLULES = ("juge_8b", "trace_lite")


def banque(n_taches=64, n_par_tache=150, derive=0.0, entropie=2026, cellule_derivee=None):
    """Honnêtes synthétiques : effet de tâche, bruit unité, dérive linéaire en rang dans chaque tâche telle que l'écart
    des moyennes des deux moitiés vaille `derive` (en écart-type du bruit)."""
    rng = np.random.default_rng(np.random.SeedSequence(entropie))
    episodes, rang = [], 0
    ordre = [(t, e) for e in range(n_par_tache) for t in range(n_taches)]  # entrelacé
    effets = rng.normal(0, 0.5, size=n_taches)
    for t, e in ordre:
        pente = 2 * derive * (e / (n_par_tache - 1) - 0.5)
        scores = {}
        for c in CELLULES:
            d = pente if cellule_derivee in (None, c) else 0.0
            scores[c] = float(effets[t] + d + rng.normal())
        episodes.append({"tache": f"t{t:02d}", "rang": rang, "etiquette": "honnete", "scores": scores})
        rang += 1
    return episodes


def args(**kw):
    base = dict(statistique="ecart_premieres_dernieres", parametres={"part": 0.5}, seuil=0.10,
                consequence="noeud_avant_G1", cellules=CELLULES, n_min_par_tache=10, n_permutations=0, entropie=None)
    base.update(kw)
    return base


# ---------------------------------------------------------------- cas sains et artefacts de dérive

def test_sain_sans_derive_ne_sonne_pas():
    v = dv.tester_derive(banque(), **args())
    assert v["sonne"] is False and v["n_episodes"] == 9600 and v["n_taches"] == 64
    assert all(abs(x["valeur"]) < 0.06 for x in v["par_cellule"].values())
    assert dv.exiger_sans_derive(v) is v


def test_artefact_derive_injectee_sonne_et_noeud():
    v = dv.tester_derive(banque(derive=0.3), **args())
    assert v["sonne"] and v["cellules_qui_sonnent"] == list(CELLULES)
    assert all(0.15 < x["valeur"] < 0.45 for x in v["par_cellule"].values())
    with pytest.raises(dv.DeriveConstatee, match="nœud pour Lazar avant toute lecture de G1"):
        dv.exiger_sans_derive(v)


def test_artefact_derive_negative_sonne_bilateral():
    v = dv.tester_derive(banque(derive=-0.3), **args())
    assert v["sonne"] and all(x["valeur"] < -0.15 for x in v["par_cellule"].values())


def test_derive_d_une_seule_cellule():
    v = dv.tester_derive(banque(derive=0.3, cellule_derivee="trace_lite"), **args())
    assert v["cellules_qui_sonnent"] == ["trace_lite"]


def test_lecture_seule_consigne_sans_lever():
    v = dv.tester_derive(banque(derive=0.3), **args(consequence="lecture_seule"))
    assert v["sonne"] and dv.exiger_sans_derive(v)["texte_consequence"].startswith("P-18 (b)")


def test_spearman_sain_et_artefact():
    a = args(statistique="spearman_rang", parametres={}, seuil=0.05)
    assert dv.tester_derive(banque(), **a)["sonne"] is False
    v = dv.tester_derive(banque(derive=1.0), **a)
    assert v["sonne"] and all(x["valeur"] > 0.1 for x in v["par_cellule"].values())


def test_ordre_des_episodes_en_entree_indifferent():
    e = banque(n_taches=8, n_par_tache=20, derive=0.5)
    v1 = dv.tester_derive(e, **args())
    v2 = dv.tester_derive(list(reversed(e)), **args())
    assert v1["par_cellule"] == v2["par_cellule"]


def test_permutation_consignee_reproductible_et_ne_decide_pas():
    a = args(n_permutations=40, entropie=99)
    v1 = dv.tester_derive(banque(n_taches=8, n_par_tache=20), **a)
    v2 = dv.tester_derive(banque(n_taches=8, n_par_tache=20), **a)
    assert v1["par_cellule"] == v2["par_cellule"]
    assert all(0 < x["p_permutation_bilaterale"] <= 1 for x in v1["par_cellule"].values())
    fort = dv.tester_derive(banque(n_taches=8, n_par_tache=20, derive=2.0), **a)
    assert all(x["p_permutation_bilaterale"] < 0.05 for x in fort["par_cellule"].values())


def test_valeur_attendue_sur_cas_construit():
    # deux tâches, scores 0,0,1,1 : écart des moitiés = 1 ; σ intra groupé = sqrt(2 × 1 / 6)
    ep = []
    for t in ("a", "b"):
        for i, x in enumerate([0.0, 0.0, 1.0, 1.0]):
            ep.append({"tache": t, "rang": len(ep), "etiquette": "honnete", "scores": {"c": x}})
    v = dv.tester_derive(ep, **args(cellules=("c",), n_min_par_tache=4))
    assert v["par_cellule"]["c"]["valeur"] == pytest.approx(1 / np.sqrt(2 / 6))


# ---------------------------------------------------------------- paramètres obligatoires

@pytest.mark.parametrize("manquant", ["statistique", "parametres", "seuil", "consequence", "cellules",
                                      "n_min_par_tache", "n_permutations", "entropie"])
def test_artefact_parametre_manquant(manquant):
    a = args()
    del a[manquant]
    with pytest.raises(TypeError):
        dv.tester_derive(banque(n_taches=4, n_par_tache=10), **a)


@pytest.mark.parametrize("modif,motif", [
    (dict(statistique="mediane"), "inconnue"),
    (dict(parametres={}), "aucun défaut"),
    (dict(parametres={"part": 0.5, "autre": 1}), "aucun défaut"),
    (dict(parametres={"part": 0.7}), "hors"),
    (dict(statistique="spearman_rang", parametres={"part": 0.5}), "aucun défaut"),
    (dict(seuil=0.0), "positif"), (dict(seuil=float("nan")), "fini"),
    (dict(consequence="jeter"), "conséquence"),
    (dict(cellules=()), "cellules"), (dict(cellules=("juge_8b", "juge_8b")), "cellules"),
    (dict(n_min_par_tache=1), "effectif"),
    (dict(n_permutations=-1), "n_permutations"),
    (dict(n_permutations=10, entropie=None), "R9"),
    (dict(n_permutations=0, entropie=3), "incohérent")])
def test_artefact_parametre_invalide(modif, motif):
    with pytest.raises(GardeArret, match=motif):
        dv.tester_derive(banque(n_taches=4, n_par_tache=10), **args(**modif))


# ---------------------------------------------------------------- gardes sur les données

def test_artefact_episode_sabote_refuse():
    e = banque(n_taches=4, n_par_tache=10)
    e[3]["etiquette"] = "sabote"
    with pytest.raises(GardeArret, match="ne lit que les honnêtes"):
        dv.tester_derive(e, **args())


@pytest.mark.parametrize("valeur", [float("nan"), float("inf"), None, True])
def test_artefact_score_non_fini(valeur):
    e = banque(n_taches=4, n_par_tache=10)
    e[5]["scores"]["juge_8b"] = valeur
    with pytest.raises(GardeArret, match="imputation"):
        dv.tester_derive(e, **args())


def test_artefact_cellule_manquante_ou_en_trop():
    e = banque(n_taches=4, n_par_tache=10)
    del e[0]["scores"]["trace_lite"]
    with pytest.raises(GardeArret, match="manquantes"):
        dv.tester_derive(e, **args())
    e = banque(n_taches=4, n_par_tache=10)
    e[0]["scores"]["qwen"] = 0.0
    with pytest.raises(GardeArret, match="inattendues"):
        dv.tester_derive(e, **args())


def test_artefact_rang_en_double_ou_invalide():
    e = banque(n_taches=4, n_par_tache=10)
    e[1]["rang"] = e[0]["rang"]
    with pytest.raises(GardeArret, match="double"):
        dv.tester_derive(e, **args())
    e = banque(n_taches=4, n_par_tache=10)
    e[1]["rang"] = -1
    with pytest.raises(GardeArret, match="rang"):
        dv.tester_derive(e, **args())


def test_artefact_tache_trop_courte():
    e = banque(n_taches=4, n_par_tache=10)
    e = [x for x in e if not (x["tache"] == "t00" and x["rang"] > 20)]
    with pytest.raises(GardeArret, match="t00"):
        dv.tester_derive(e, **args())
    with pytest.raises(GardeArret, match="= 0 épisode"):
        dv.tester_derive(banque(n_taches=4, n_par_tache=10), **args(parametres={"part": 0.05}))


def test_artefact_scores_constants():
    e = banque(n_taches=4, n_par_tache=10)
    for x in e:
        x["scores"]["juge_8b"] = 1.0
    with pytest.raises(GardeArret, match="intra-tâche nul"):
        dv.tester_derive(e, **args())
    with pytest.raises(GardeArret, match="Spearman indéfini"):
        dv.tester_derive(e, **args(statistique="spearman_rang", parametres={}))


def test_artefact_champs_d_episode_et_liste_vide():
    with pytest.raises(GardeArret, match="non vide"):
        dv.tester_derive([], **args())
    e = banque(n_taches=4, n_par_tache=10)
    e[0]["horodatage"] = "x"
    with pytest.raises(GardeArret, match="champs attendus"):
        dv.tester_derive(e, **args())


def test_artefact_verdict_illisible():
    with pytest.raises(GardeArret, match="illisible"):
        dv.exiger_sans_derive({"version": "derive-v0", "consequence": "lecture_seule", "sonne": True})
