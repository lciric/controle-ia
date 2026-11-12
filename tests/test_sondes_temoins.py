"""Témoins de concept et de lexique (T0.7, brouillon 3, étape 8 ; module `sondes/temoins.py`). Données synthétiques : des
phrases « du concept » qui portent un décalage sur un axe, des phrases neutres appariées qui ne le portent pas, et des
actions qui ont un jeton du concept ou n'en ont pas ; des textes dont une classe contient un mot marqueur. Gardes testées
sur cas sain et artefact (R5)."""
from __future__ import annotations

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.sondes import evaluation as ev
from controle_ia.sondes import temoins as te

D = 10


def _phrases(graine, n=24, decalage=2.5, concept=True):
    rng = np.random.default_rng(graine)
    u = np.zeros(D)
    u[2] = 1.0
    sortie = []
    for _ in range(n):
        h = rng.standard_normal((int(rng.integers(5, 9)), D))
        h[:, 0] *= 5.0                                          # axe de nuisance de grande variance
        if concept:
            h += decalage * u
        sortie.append(h)
    return sortie


def _actions(graine, n=120):
    rng = np.random.default_rng(graine)
    u = np.zeros(D)
    u[2] = 1.0
    seqs, y, blocs = [], [], []
    for i in range(n):
        h = rng.standard_normal((int(rng.integers(4, 11)), D))
        h[:, 0] *= 5.0
        porte = int(rng.random() < 0.5)
        if porte:
            h[int(rng.integers(0, len(h)))] += 3.0 * u           # un seul jeton du concept : le maximum le voit
        seqs.append(h)
        y.append(porte)
        blocs.append(i // 6)
    return seqs, np.array(y), np.array(blocs)


PC, PN = _phrases(1), _phrases(2, concept=False)


def test_direction_concept_cas_sain_lue_par_le_maximum_et_au_dessus_de_son_plancher():
    sonde, rapport = te.direction_concept("chats", 15, PC, PN)
    assert sonde.agregation == "max" and sonde.famille == "concept" and sonde.couche == 15
    assert np.argmax(np.abs(sonde.w)) == 2
    assert rapport["paires"] == len(PC) and len(rapport["jetons_concept"]) == len(PC)
    assert rapport["empreinte"] == sonde.empreinte()
    seqs, y, blocs = _actions(3)
    plancher = te.plancher_concept("chats", 15, PC, PN, n_directions=60, graine=4)
    assert len(plancher) == 60 and all(p.agregation == "max" for p in plancher)
    r = ev.comparer_au_plancher(sonde, plancher, seqs, y, blocs, n_tirages=400, graine=5)
    assert r["aire"] > 0.8 and r["au_dessus_du_plancher"], r


def test_direction_concept_rapporte_l_ecart_de_longueur_des_paires():
    pc = [np.ones((6, D)), np.ones((4, D))]
    pn = [np.zeros((5, D)), np.zeros((4, D))]
    _, rapport = te.direction_concept("meteo", 7, pc, pn)
    assert rapport["jetons_concept"] == (6, 4) and rapport["jetons_neutres"] == (5, 4)
    assert rapport["ecart_longueur_max"] == 1


def test_direction_concept_deterministe():
    a, _ = te.direction_concept("sports", 23, PC, PN)
    b, _ = te.direction_concept("sports", 23, PC, PN)
    assert a.empreinte() == b.empreinte()


@pytest.mark.parametrize("phrases_concept,phrases_neutres,motif", [
    (PC[:3], PN[:2], "paires"),                                  # nombres de phrases différents
    (PC[:1], PN[:1], "deux paires"),                             # une seule paire
    ([np.ones((4, D))] * 2, [np.ones((4, D + 1))] * 2, "largeurs"),
    ([np.ones((4, D))] * 2, [np.ones((4, D))] * 2, "direction nulle"),
    ([np.full((4, D), np.nan)] * 2, PN[:2], "non finie"),
])
def test_direction_concept_artefacts(phrases_concept, phrases_neutres, motif):
    with pytest.raises(GardeArret, match=motif):
        te.direction_concept("geographie", 7, phrases_concept, phrases_neutres)


@pytest.mark.parametrize("nom", ["chats", "météo", "sports", "géographie", "ambassade", "étranger"])
def test_concepts_sans_affect_admis(nom):
    te.exiger_concept_sans_affect(nom)


@pytest.mark.parametrize("nom", ["douleur", "Peur", "tristesse", "émotion négative", "valence", "souffrance", "affect",
                                 "pain", "Fear", "sadness", "détresse"])
def test_concepts_d_affect_refuses(nom):
    with pytest.raises(GardeArret, match="P-013"):
        te.exiger_concept_sans_affect(nom)
    with pytest.raises(GardeArret, match="P-013"):
        te.direction_concept(nom, 7, PC, PN)
    with pytest.raises(GardeArret, match="P-013"):
        te.plancher_concept(nom, 7, PC, PN, n_directions=3, graine=0)


def _textes(graine, n=80):
    rng = np.random.default_rng(graine)
    fond = ["la", "proposition", "ajoute", "un", "contrôle", "sur", "le", "coût", "de", "la", "mesure", "révisée"]
    textes, y = [], []
    for _ in range(n):
        mots = list(rng.choice(fond, size=int(rng.integers(6, 12))))
        classe = int(rng.random() < 0.5)
        if classe:
            mots.insert(int(rng.integers(0, len(mots))), "marqueur")
        textes.append(" ".join(mots))
        y.append(classe)
    return textes, np.array(y)


def test_temoin_lexical_cas_sain_et_deterministe():
    # 300 textes d'entraînement : avec 80, le sac de bigrammes de hasard surapprend (aire de test ≈ 0,86)
    textes, y = _textes(1, n=300)
    t = te.temoin_lexical("lex-chats", textes, y, penalite=1.0)
    test_textes, test_y = _textes(2, n=200)
    assert ev.aire_sous_courbe(t.scores(test_textes), test_y) > 0.95
    assert "marqueur" in t.vocabulaire and "la proposition" in t.vocabulaire     # unigrammes et bigrammes
    assert t.empreinte() == te.temoin_lexical("lex-chats", textes, y, penalite=1.0).empreinte()


def test_temoin_lexical_etiquettes_melangees_au_hasard():
    textes, y = _textes(1, n=300)
    melange = np.random.default_rng(0).permutation(y)
    t = te.temoin_lexical("lex", textes, melange, penalite=1.0)
    test_textes, test_y = _textes(2, n=200)
    assert abs(ev.aire_sous_courbe(t.scores(test_textes), test_y) - 0.5) < 0.1


def test_temoin_lexical_vocabulaire_de_l_entrainement_seulement():
    textes, y = _textes(1)
    t = te.temoin_lexical("lex", textes, y, penalite=1.0)
    s = t.scores(["inconnu jamais vu", "autre texte absent"])
    assert "inconnu" not in t.vocabulaire
    assert np.allclose(s, t.b)                                   # aucun terme connu : la constante seule


@pytest.mark.parametrize("textes,y,penalite,motif", [
    (["un texte", ""], [0, 1], 1.0, "vide"),
    (["un texte", "  "], [0, 1], 1.0, "vide"),
    (["un texte", "deux textes"], [1, 1], 1.0, "deux classes"),
    (["un texte", "deux textes"], [0, 2], 1.0, "0/1"),
    (["un texte", "deux textes"], [0, 1, 1], 1.0, "0/1"),
    (["un texte", "deux textes"], [0, 1], 0.0, "strictement positive"),
    (["un texte", "deux textes"], [0, 1], -1.0, "strictement positive"),
    ([], [], 1.0, "aucun texte"),
])
def test_temoin_lexical_artefacts(textes, y, penalite, motif):
    with pytest.raises(GardeArret, match=motif):
        te.temoin_lexical("lex", textes, y, penalite=penalite)


def test_temoin_lexical_non_convergence_arrete():
    textes, y = _textes(1)
    with pytest.raises(GardeArret, match="non convergé"):
        te.temoin_lexical("lex", textes, y, penalite=1e-6, iterations_max=1)


def test_temoin_lexical_texte_vide_a_la_lecture_arrete():
    textes, y = _textes(1)
    t = te.temoin_lexical("lex", textes, y, penalite=1.0)
    with pytest.raises(GardeArret, match="vide"):
        t.scores(["un texte", ""])


def test_difference_aires_appariee_cas_sain():
    rng = np.random.default_rng(7)
    y = np.array([0, 1] * 60)
    blocs = np.repeat(np.arange(20), 6)
    bon = y + 0.3 * rng.standard_normal(y.size)
    hasard = rng.standard_normal(y.size)
    r = te.difference_aires_appariee(bon, hasard, y, blocs, n_tirages=500, graine=8)
    assert r["difference"] > 0.3 and r["a_au_dessus_de_b"] and r["bas"] > 0.0, r
    assert r["aire_a"] - r["aire_b"] == pytest.approx(r["difference"])
    nul = te.difference_aires_appariee(bon, bon, y, blocs, n_tirages=200, graine=8)
    assert nul["difference"] == 0.0 and nul["bas"] == 0.0 and nul["haut"] == 0.0 and not nul["a_au_dessus_de_b"]


def test_difference_aires_appariee_artefacts():
    y = np.array([0, 1, 0, 1])
    with pytest.raises(GardeArret, match="même longueur"):
        te.difference_aires_appariee([0.1, 0.2, 0.3], [0.1, 0.2, 0.3, 0.4], y, [0, 0, 1, 1], 10, 0)
    with pytest.raises(GardeArret, match="deux blocs"):
        te.difference_aires_appariee([0.1, 0.2, 0.3, 0.4], [0.4, 0.3, 0.2, 0.1], y, [0, 0, 0, 0], 10, 0)
    # deux blocs d'une seule classe chacun : beaucoup de tirages n'ont qu'une classe
    with pytest.raises(GardeArret, match="déséquilibrés"):
        te.difference_aires_appariee([0.1, 0.2, 0.3, 0.4], [0.4, 0.3, 0.2, 0.1], [0, 0, 1, 1], [0, 0, 1, 1], 200, 0)
