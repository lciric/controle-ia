"""Essais du module agrégation R1 v4 (préenregistrement « candidat 1 corrigé ») sur données synthétiques aux formats de la
fiche de réception v4 ; chaque garde testée sur un cas sain et sur un artefact (R5)."""
from __future__ import annotations

import json
import subprocess

import numpy as np
import pytest

from controle_ia.agregation_r1_v4 import agregateurs_v1 as ag
from controle_ia.agregation_r1_v4 import analyse_v1 as an
from controle_ia.agregation_r1_v4 import comparaisons_v1 as cp
from controle_ia.agregation_r1_v4 import entrees_v1 as en
from controle_ia.agregation_r1_v4.puissance_v1 import simuler
from controle_ia.gardes import GardeArret

CONDS = ("honnete", "saboteur", "temoin", "mention")


def jeu_synthetique(dossier, largeur=32, decalage=1.0, graine=0, retouche=None):
    """Trois fichiers aux formats de la fiche v4 (14 tableaux, identité égale à scores-p3.npz)."""
    rng = np.random.default_rng(graine)
    lignes = []
    ep = 0
    for t in range(60):
        for c in CONDS:
            for p in range(10):
                lignes.append((ep, p, c, f"tache-{t:02d}"))
            ep += 1
    n = len(lignes)
    episode = np.array([l[0] for l in lignes], dtype=np.int64)
    pas = np.array([l[1] for l in lignes], dtype=np.int64)
    condition = np.array([l[2] for l in lignes])
    tache = np.array([l[3] for l in lignes])
    direction = rng.normal(size=largeur)
    direction /= np.linalg.norm(direction)
    base = rng.normal(size=(n, 3, largeur))
    sab = condition == "saboteur"
    base[sab] += decalage * direction
    communs = {"jetons_empan": rng.integers(5, 100, n).astype(np.int64), "jetons_empan_rejeu": np.zeros(n, np.int64),
               "couches": np.array([7, 15, 23], dtype=np.int64), "conforme_longueur": np.ones(n, bool),
               "contexte_conforme": np.ones(n, bool), "fidele": np.ones(n, bool),
               "trajectoire_identique": np.ones(n, bool), "activations_identiques": np.ones(n, bool),
               "ecart_fidelite": np.zeros(n), "episode": episode, "pas": pas, "condition": condition, "tache": tache}
    maximum = {**communs, "maximum": (base + 0.5).astype("<f2")}
    moyenne = {**communs, "moyenne": base.astype("<f2")}
    noms = np.array(["autre-sonde", "tromperie-difference_moyennes-c15", "enjeux-lineaire-c15"])
    scores = rng.normal(size=(n, 3)) + 0.3 * sab[:, None]
    p3 = {"noms_sondes": noms, "scores": scores, "episode": episode, "condition": condition, "tache": tache, "pas": pas}
    if retouche:
        retouche(maximum, moyenne, p3)
    chemins = [dossier / "activations-p3-rejeu-v1-maximum.npz", dossier / "activations-p3-rejeu-v1.npz",
               dossier / "scores-p3.npz"]
    for ch, t in zip(chemins, (maximum, moyenne, p3)):
        np.savez(ch, **t)
    return chemins


def rngs(graine=1):
    return {t: np.random.default_rng(np.random.SeedSequence(graine, spawn_key=(k,)))
            for k, t in enumerate(an.TACHES_GRAINES)}


# ------------------------------------------------------------ agrégateurs

def test_agregateurs_valeurs_connues():
    z = np.array([1.0, -1.0, 2.0, 0.5])
    s = ag.toutes(z)
    assert s["somme"] == pytest.approx(2.5) and s["moyenne"] == pytest.approx(0.625) and s["max"] == 2.0
    assert s["page"] == pytest.approx(1.5)              # C : 0,5 ; 0 ; 1,5 ; 1,5
    assert s["balayage"] == pytest.approx(2.0)          # fenêtres : 2,0 ; 1,5
    assert s["dernier"] == 0.5
    assert ag.balayage(np.array([1.0, 2.0])) == 3.0


def test_agregateurs_vectorises_egaux():
    Z = np.random.default_rng(3).normal(size=(40, 10))
    a, b = ag.statistiques_matrice(Z), ag.tableau_statistiques(list(Z))
    for k in ag.STATISTIQUES:
        np.testing.assert_allclose(a[k], b[k], atol=1e-12)


def test_agregateurs_gardes():
    with pytest.raises(GardeArret):
        ag.statistique("mediane", np.ones(3))
    with pytest.raises(GardeArret):
        ag.statistique("somme", np.array([]))
    with pytest.raises(GardeArret):
        ag.statistique("max", np.array([1.0, np.nan]))
    with pytest.raises(GardeArret):
        ag.statistiques_matrice(np.array([[1.0, np.inf]]))


# ------------------------------------------------------------ comparaisons

def test_holm():
    r = cp.holm({"a": 0.01, "b": 0.04, "c": 0.03}, 0.05)
    assert r["a"]["rejet"] and not r["c"]["rejet"] and not r["b"]["rejet"]
    r = cp.holm({"a": 0.01, "b": 0.02, "c": 0.04}, 0.05)
    assert all(v["rejet"] for v in r.values())
    with pytest.raises(GardeArret):
        cp.holm({}, 0.05)


def test_contraste_sain_et_artefacts():
    rng = np.random.default_rng(0)
    y = np.r_[np.zeros(30), np.ones(30)]
    blocs = np.r_[np.arange(30), np.arange(30)]
    a = y * 2 + rng.normal(size=60)
    b = rng.normal(size=60)
    r = cp.contraste_blocs([(a, b, y, blocs)], [1.0], 500, rng, "positif")
    assert r["contraste"] > 0.3 and r["p_unilaterale"] < 0.01 and r["bas"] > 0
    with pytest.raises(GardeArret):
        cp.contraste_blocs([(a, b, y, blocs)], [1.0], 10, rng, "autre")
    with pytest.raises(GardeArret):   # une seule classe : non calculable
        cp.contraste_blocs([(a, b, np.ones(60), blocs)], [1.0], 10, rng, "positif")
    with pytest.raises(GardeArret):   # trop de tirages dégénérés (une seule tâche porte les positifs)
        cp.contraste_blocs([(a[:31], b[:31], np.r_[np.zeros(30), 1.0], np.r_[np.arange(30), 99])], [1.0], 200, rng,
                           "positif")


def test_permutation_sain_et_artefact():
    rng = np.random.default_rng(1)
    y = np.r_[np.zeros(20), np.ones(20)]
    blocs = np.r_[np.arange(20), np.arange(20)]
    r = cp.permutation_dans_taches(y * 3 + rng.normal(size=40), y, blocs, 999, rng)
    assert r["p"] < 0.01
    r0 = cp.permutation_dans_taches(rng.normal(size=40), y, blocs, 999, rng)
    assert r0["p"] > 0.01
    with pytest.raises(GardeArret):
        cp.permutation_dans_taches(rng.normal(size=40), y, np.r_[np.arange(20), np.arange(20) % 10], 10, rng)


# ------------------------------------------------------------ simulation

def test_simulation_signes():
    r = simuler(0.99, 0.0, 0.0, 30, np.random.default_rng(2), ms=(10, 1))
    assert r["par_m"]["1"]["delta_somme_moins_max"]["moyenne"] < -0.1
    assert r["contraste_dense_moins_concentre"]["moyenne"] > 0.1


# ------------------------------------------------------------ entrées

def test_entrees_formats_exacts_fiche_v4(tmp_path):
    ch = jeu_synthetique(tmp_path, largeur=4096)
    e = en.charger(*ch)
    assert e.maximum.shape == (2400, 4096) and e.moyenne.dtype == np.float64
    assert set(e.scores_g) == {"Gt", "Ge"} and e.notee.all()
    assert en.eligibles(e).all()


@pytest.mark.parametrize("retouche, motif", [
    (lambda mx, mo, p3: mx.__setitem__("maximum", mx["maximum"][:, :2]), "forme"),
    (lambda mx, mo, p3: mx.__setitem__("couches", np.array([7, 15, 31])), "couches"),
    (lambda mx, mo, p3: mx.__setitem__("en_trop", np.zeros(3)), "tableaux"),
    (lambda mx, mo, p3: mo.__setitem__("fidele", ~mo["fidele"]), "commun"),
    (lambda mx, mo, p3: p3.__setitem__("pas", p3["pas"][::-1].copy()), "identité"),
    (lambda mx, mo, p3: p3.__setitem__("noms_sondes", np.array(["a", "b", "enjeux-lineaire-c15"])), "absente"),
    (lambda mx, mo, p3: mx.__setitem__("maximum", mx["maximum"].astype("<f4")), "type"),
])
def test_entrees_artefacts(tmp_path, retouche, motif):
    ch = jeu_synthetique(tmp_path, retouche=retouche)
    with pytest.raises(GardeArret, match=motif):
        en.charger(*ch, largeur=32)


def test_entrees_fichier_absent(tmp_path):
    ch = jeu_synthetique(tmp_path)
    with pytest.raises(GardeArret, match="absent"):
        en.charger(tmp_path / "rien.npz", ch[1], ch[2], largeur=32)


def test_structure_artefact():
    ep = np.repeat(np.arange(240), 10)
    pas = np.tile(np.arange(10), 240)
    cond = np.array([CONDS[(i // 10) % 4] for i in range(2400)])
    tache = np.array([f"t{i // 40}" for i in range(2400)])
    en.verifier_structure(ep, pas, cond, tache)
    pas2 = pas.copy()
    pas2[5] = 4
    with pytest.raises(GardeArret, match="pas 0"):
        en.verifier_structure(ep, pas2, cond, tache)
    with pytest.raises(GardeArret, match="tâches"):
        en.verifier_structure(ep, pas, cond, np.array([f"t{i // 80}" for i in range(2400)]))


def test_activation_non_finie_sur_eligible(tmp_path):
    def r(mx, mo, p3):
        a = mx["maximum"].copy()
        a[7, 1, 0] = np.inf
        mx["maximum"] = a
    e = en.charger(*jeu_synthetique(tmp_path, retouche=r), largeur=32)
    with pytest.raises(GardeArret, match="non finie"):
        en.eligibles(e)
    e.fidele[7] = False                     # inéligible : la même valeur n'arrête plus
    assert not en.eligibles(e)[7]


# ------------------------------------------------------------ analyse

def test_regression_l2_separe():
    rng = np.random.default_rng(0)
    X = rng.normal(size=(200, 5))
    y = (X[:, 0] > 0).astype(int)
    w, b = an.regression_l2(X, y)
    assert w[0] > 1 and abs(b) < 1


def test_reduction_ecart_type_nul(tmp_path):
    e = en.charger(*jeu_synthetique(tmp_path), largeur=32)
    el = en.eligibles(e)
    pli = np.zeros(2400, int)
    with pytest.raises(GardeArret, match="écart type"):
        an.reduire(np.ones(2400), e, el, pli)


def test_analyse_bout_en_bout_petite_largeur(tmp_path):
    e = en.charger(*jeu_synthetique(tmp_path, largeur=32, decalage=1.5), largeur=32)
    r = an.analyser(e, rngs(), n_tirages=300, n_permutations=300, n_tirages_descriptifs=200, repliques_porte=20)
    assert set(r["confirmatoires"]) == {"C1", "C2", "C3"}
    assert r["H_AG"] in ("appuyée", "contredite", "non concluante")
    assert set(r["descriptives"]) == set(an.SOURCES)
    assert r["descriptives"]["W"]["comptes_hybrides"][1]["hybrides"] == 600
    json.dumps(r, ensure_ascii=False)         # sérialisable
    # reproductible à graines égales
    r2 = an.analyser(e, rngs(), n_tirages=300, n_permutations=300, n_tirages_descriptifs=200, repliques_porte=20)
    assert json.dumps(r, sort_keys=True) == json.dumps(r2, sort_keys=True)


def test_analyse_taches_exclues(tmp_path):
    def r(mx, mo, p3):
        f = mx["fidele"].copy()
        f[(mx["condition"] == "saboteur") & np.isin(mx["tache"], [f"tache-{t:02d}" for t in range(7)])] = False
        mx["fidele"] = f
        mo["fidele"] = f
    e = en.charger(*jeu_synthetique(tmp_path, retouche=r), largeur=32)
    res = an.analyser(e, rngs(), n_tirages=100, n_permutations=100, n_tirages_descriptifs=100, repliques_porte=10)
    assert len(res["comptes"]["taches_exclues"]) == 7
    assert all(v["verdict"].startswith("non concluant par construction (données")
               for v in res["confirmatoires"].values())
    assert any("éligibilité dégradée" in x for x in res["reserves"])


def test_lecture_gelee():
    t = {"sens": "positif", "bas": -0.2, "haut": -0.01}
    assert an.lire(t, None, False) == "réfuté"
    assert an.lire({**t, "haut": 0.1}, None, False) == "non concluant"
    assert an.lire(t, None, True) == "confirmé à cette puissance"
    assert an.lire(t, "motif", False).startswith("non concluant par construction")
    assert an.lire_hag({"C1": "non concluant", "C2": "non concluant", "C3": "confirmé à cette puissance"}) == "appuyée"
    assert an.lire_hag({"C1": "réfuté", "C2": "non concluant", "C3": "confirmé à cette puissance"}) == "contredite"
    assert an.lire_hag({"C1": "non concluant", "C2": "confirmé à cette puissance", "C3": "non concluant"}) == \
        "non concluante"


PREREG_MINIMAL = """# essai
## Hypothèse
h
## Prédiction chiffrée et signe attendu
p
## Métrique
m
## Seuil
s
## Plan d'analyse
p
## Critères de lecture gelés
c
## Liste d'arrêt
l
## Contre-lecture
- Contre-lecture 1 : {a} {b}
"""


def test_commande_decisive_formats_exacts(tmp_path):
    """Chaîne complète au format exact (4 096 dimensions) : manifeste décisif, résultat scellé ; refus sans prereg."""
    depot = tmp_path / "depot"
    depot.mkdir()
    ch = jeu_synthetique(tmp_path, largeur=4096, decalage=3.0)
    pr = depot / "prereg.md"
    pr.write_text(PREREG_MINIMAL.format(a="0" * 64, b="1" * 64), encoding="utf-8")
    from controle_ia.scellement import sceller
    sceller(pr)
    for c in (["git", "init", "-q"], ["git", "add", "-A"],
              ["git", "-c", "user.email=e@x", "-c", "user.name=essai", "commit", "-qm", "essai"]):
        subprocess.run(c, cwd=depot, check=True)
    args = ["--racine", str(depot), "--run-id", "20261106-120000-agregation-r1-v4",
            "--activations-maximum", str(ch[0]), "--activations-moyenne", str(ch[1]), "--scores-p3", str(ch[2]),
            "--prereg", str(pr)]
    orig = an.analyser                                    # essai rapide : moins de tirages, même code par ailleurs
    an.main.__globals__["analyser"] = lambda e, r, *a: orig(e, r, 200, 200, 100, 10)
    try:
        assert an.main(args) == 0
    finally:
        an.main.__globals__["analyser"] = orig
    sortie = depot / "diag" / "20261106-120000-agregation-r1-v4" / f"{an.NOM_SORTIE}.json"
    corps = json.loads(sortie.read_text(encoding="utf-8"))
    assert corps["resultat"]["aires_action"]["W"] > 0.7      # décalage net sur 4 096 dimensions bruitées
    with pytest.raises(GardeArret, match="existe déjà"):
        an.main(args)


@pytest.mark.filterwarnings("ignore::RuntimeWarning")
def test_regression_l2_non_convergee():
    X = np.ones((10, 3))
    X[0, 0] = np.nan
    with pytest.raises(GardeArret, match="non convergée"):
        an.regression_l2(X, np.r_[np.zeros(5), np.ones(5)])
