"""Essais de `plancher_v3.py` (notation vectorisée des directions de plancher de T0.7, remède (a')) — v1, fichier neuf (consigne
`consigne-code-plancher-v3-t07-v1.md`, `88879387…`, point 2).

- **Égalité à la boucle** (`plancher_v1.scores_plancher`) : sur des tirages aléatoires (largeurs, longueurs d'action, nombre de
  directions, taille des lots, une action plus longue qu'un lot) et sur les activations du faux run de 7b (le jouet, lues comme
  l'étape A les lit), agrégations maximum et attention : écart rapporté à l'échelle ≤ 10⁻¹² ; part des scores égaux au bit
  près relevée (le produit par lots n'additionne pas dans l'ordre du produit matrice-vecteur) ;
- **agrégation au bit près** : à scores par jeton égaux (ceux de la boucle), maximum et attention rendent au bit près le score
  de `harnais.sondes.score_action` ;
- **R5** : contrôle en ligne (cas sain ; artefact : une matrice décalée de 10⁻⁹ relatif → arrêt) ; refus (plancher vide,
  agrégations ou couches mêlées, classe autre, attention sans requête, maximum avec requête, empan vide, largeur fausse,
  activation non finie, taille de lot nulle), chacun avec son cas sain ;
- aucune moyenne ni médiane sur les jetons (texte des modules neufs).
"""
from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.harnais.sondes import SondeLineaire
from controle_ia.sondes.evaluation import plancher_apparie
from controle_ia.sondes.familles import SondeLineaireJetons
from controle_ia.t07 import plancher_v1 as pl
from controle_ia.t07 import plancher_v3 as pl3

MODULES_NEUFS = ("plancher_v3.py", "reextraction_p3_v1.py", "lecture_v4.py", "passe_blanc_v2.py", "repli_etapes_v2.py")
MODULE = Path(pl3.__file__).resolve().parent


def _actions(rng, n, d, lmin=1, lmax=40, longue=None):
    a = [rng.standard_normal((int(rng.integers(lmin, lmax + 1)), d)).astype(np.float32) * float(rng.uniform(0.2, 5.0))
         for _ in range(n)]
    if longue:
        a.insert(n // 2, rng.standard_normal((longue, d)).astype(np.float32))
    return a


@pytest.mark.parametrize("agregation", ["max", "attention"])
@pytest.mark.parametrize("d,k,taille_lot,graine", [(8, 1, 1, 1), (8, 3, 7, 2), (64, 50, 100, 3), (64, 50, 10_000, 4),
                                                  (33, 17, 64, 5)])
def test_egal_a_la_boucle_tirages_aleatoires(agregation, d, k, taille_lot, graine):
    rng = np.random.default_rng(graine)
    seqs = _actions(rng, 60, d, longue=3 * taille_lot if taille_lot < 1000 else None)
    P = plancher_apparie("x", 15, seqs[:20], agregation, k, graine + 100)
    boucle = pl.scores_plancher(P, seqs)
    v = pl3.scores_plancher_vectorises(P, seqs, taille_lot=taille_lot, controle=0)
    assert v.shape == boucle.shape == (len(seqs), k)
    e = pl3.ecart_a_la_boucle(P, seqs, v, range(k))
    assert e["ecart_relatif_max"] <= pl3.TOLERANCE_VECTORISEE
    assert e["ecart_relatif_max"] < 1e-14                    # mesuré : de l'ordre de 10⁻¹⁶
    assert 0.0 <= e["egaux_au_bit_pres"] <= 1.0


@pytest.mark.parametrize("agregation", ["max", "attention"])
def test_agregation_au_bit_pres_a_scores_par_jeton_egaux(agregation):
    rng = np.random.default_rng(7)
    seqs = _actions(rng, 50, 24)
    P = plancher_apparie("x", 15, seqs[:10], agregation, 9, 3)
    S = np.concatenate([np.stack([p.scores_par_jeton(s) for p in P], axis=1) for s in seqs])
    bornes = np.concatenate([[0], np.cumsum([len(s) for s in seqs])])
    if agregation == "max":
        agr = pl3._agreger_max(S, bornes)
    else:
        L = np.concatenate([np.stack([p.logits_attention(s) for p in P], axis=1) for s in seqs])
        agr = pl3._agreger_attention(S, L, bornes)
    assert np.array_equal(agr, pl.scores_plancher(P, seqs))


@pytest.mark.parametrize("agregation", ["max", "attention"])
def test_egal_a_la_boucle_sur_le_jouet(depot, agregation):
    """Activations du faux run de 7b, lues comme l'étape A (demi-précision sur disque → simple précision), directions tirées
    sur ses jetons d'entraînement de jouet."""
    from test_t07_lecture_v1 import RUN_T06, construire_run
    from controle_ia.t07 import lecture_v1 as lv1
    j = construire_run(depot)
    mesures = lv1.charger_mesures(depot / "donnees" / RUN_T06 / "mesures-t06.npz")
    notees = np.flatnonzero(mesures["jetons_notes"] > 0)
    D = np.load(depot / "donnees" / RUN_T06 / "activations" / "c15" / f"{mesures['cle'][notees[0]]}.npy").shape[1]
    seqs = [lv1.lire_activation(depot, RUN_T06, str(mesures["cle"][i]), 15, int(mesures["jetons_notes"][i]), D) for i in notees]
    P = plancher_apparie("jouet", 15, seqs[:40], agregation, 30, 11)
    v = pl3.scores_plancher_vectorises(P, seqs)                # contrôle en ligne joué (deux directions)
    e = pl3.ecart_a_la_boucle(P, seqs, v, range(len(P)))
    assert e["ecart_relatif_max"] <= pl3.TOLERANCE_VECTORISEE and e["actions"] == len(notees)
    assert j is not None


def test_controle_en_ligne_cas_sain_et_artefact():
    rng = np.random.default_rng(3)
    seqs = _actions(rng, 30, 16)
    P = plancher_apparie("x", 15, seqs, "max", 5, 9)
    v = pl3.scores_plancher_vectorises(P, seqs, controle=0)
    sain = pl3.controler_contre_la_boucle(P, seqs, v, 2)
    assert sain["ecart_relatif_max"] <= pl3.TOLERANCE_VECTORISEE and sain["directions"] == [0, 1]
    assert sain["actions_controlees"] == [0, 8, 16, 24, 29]
    for i in (0, 16, 29):                                    # actions contrôlées (une sur huit, et la dernière)
        faux = v.copy()
        faux[i, 1] *= 1.0 + 1e-9
        with pytest.raises(GardeArret, match="boucle du harnais"):
            pl3.controler_contre_la_boucle(P, seqs, faux, 2)
    for i, j in ((3, 1), (0, 4)):                            # action ou direction hors du contrôle : non vu (borne déclarée)
        faux = v.copy()
        faux[i, j] *= 1.0 + 1e-9
        pl3.controler_contre_la_boucle(P, seqs, faux, 2)
    faux = v.copy()
    faux[3, 1] *= 1.0 + 1e-9
    with pytest.raises(GardeArret, match="boucle du harnais"):
        pl3.controler_contre_la_boucle(P, seqs, faux, 2, pas=1)


def test_controle_en_ligne_joue_a_chaque_appel(monkeypatch):
    rng = np.random.default_rng(4)
    seqs = _actions(rng, 12, 8)
    P = plancher_apparie("x", 15, seqs, "max", 3, 1)
    vrai = pl3._scores_matrices
    monkeypatch.setattr(pl3, "_scores_matrices", lambda m, s, t: vrai(m, s, t) * (1.0 + 1e-8))
    with pytest.raises(GardeArret, match="aucune bascule silencieuse"):
        pl3.scores_plancher_vectorises(P, seqs)


def test_refus_et_cas_sains():
    rng = np.random.default_rng(5)
    seqs = _actions(rng, 8, 6)
    pm = plancher_apparie("x", 15, seqs, "max", 3, 1)
    pa = plancher_apparie("x", 15, seqs, "attention", 3, 1)
    assert pl3.scores_plancher_vectorises(pm, seqs).shape == (8, 3)
    assert pl3.scores_plancher_vectorises(pa, seqs).shape == (8, 3)
    with pytest.raises(GardeArret, match="plancher vide"):
        pl3.scores_plancher_vectorises([], seqs)
    with pytest.raises(GardeArret, match="agrégations mêlées"):
        pl3.scores_plancher_vectorises(pm[:2] + pa[:1], seqs)
    autre = SondeLineaireJetons("y", 7, "max", pm[0].w, pm[0].b, None, "plancher")
    with pytest.raises(GardeArret, match="couches mêlées"):
        pl3.scores_plancher_vectorises(pm[:2] + [autre], seqs)
    harnais = SondeLineaire("h", 15, pm[0].w, pm[0].b, "max")
    with pytest.raises(GardeArret, match="SondeLineaireJetons seule"):
        pl3.scores_plancher_vectorises([harnais], seqs)
    sans_q = SondeLineaireJetons("a", 15, "attention", pm[0].w, 0.0, None, "plancher")
    with pytest.raises(GardeArret, match="sans requête"):
        pl3.scores_plancher_vectorises([sans_q], seqs)
    avec_q = SondeLineaireJetons("m", 15, "max", pm[0].w, 0.0, pa[0].q, "plancher")
    with pytest.raises(GardeArret, match="porte une requête"):
        pl3.scores_plancher_vectorises([avec_q], seqs)
    moyenne = SondeLineaireJetons("z", 15, "moyenne", pm[0].w, 0.0, None, "plancher")
    with pytest.raises(GardeArret, match="jamais la moyenne"):
        pl3.scores_plancher_vectorises([moyenne], seqs)
    with pytest.raises(GardeArret, match="empan"):
        pl3.scores_plancher_vectorises(pm, seqs[:3] + [np.zeros((0, 6), dtype=np.float32)])
    with pytest.raises(GardeArret, match="attendue"):
        pl3.scores_plancher_vectorises(pm, seqs[:3] + [np.zeros((4, 5), dtype=np.float32)])
    mauvais = [s.copy() for s in seqs]
    mauvais[2][0, 0] = np.inf
    with pytest.raises(GardeArret, match="non fini"):
        pl3.scores_plancher_vectorises(pm, mauvais, controle=0)
    with pytest.raises(GardeArret, match="non fini"):
        pl.scores_plancher(pm, mauvais)                       # la boucle refuse aussi
    with pytest.raises(GardeArret, match="au moins un jeton"):
        pl3.scores_plancher_vectorises(pm, seqs, taille_lot=0)
    with pytest.raises(GardeArret, match="aucune action"):
        pl3.scores_plancher_vectorises(pm, [])


def test_lots_bornes():
    lots = list(pl3._lots([3, 3, 3, 10, 1, 1], 6))
    assert lots == [(0, 2), (2, 3), (3, 4), (4, 6)]
    assert list(pl3._lots([5], 1)) == [(0, 1)]
    assert sum(z - a for a, z in pl3._lots([2] * 17, 5)) == 17


def test_constantes():
    assert pl3.N_PLANCHER_REEL == 800 and pl3.N_PLANCHER_P3 == 200 and pl3.TOLERANCE_VECTORISEE == 1e-12
    assert pl3.CONTROLE_EN_LIGNE == 2 and pl3.PAS_CONTROLE == 8
    assert pl3.actions_controlees(1) == [0] and pl3.actions_controlees(17) == [0, 8, 16] and pl3.actions_controlees(18) == [0, 8, 16, 17]


def test_aucune_moyenne_ni_mediane_sur_les_jetons_dans_les_modules_neufs():
    motifs = re.compile(r"\.mean\(|np\.mean|\.median\(|np\.median|nanmean|nanmedian|[\"'](moyenne|médiane|mean|median)[\"']")
    for nom in MODULES_NEUFS:
        for n, ligne in enumerate((MODULE / nom).read_text(encoding="utf-8").splitlines(), 1):
            code = ligne.split("#")[0]
            if motifs.search(code):
                assert "refus" in code or "N-026" in code or "mot in" in code or "np.median(aires)" in code, f"{nom}:{n}: {ligne.strip()}"
