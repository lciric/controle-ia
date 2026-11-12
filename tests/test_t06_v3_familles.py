"""Mahalanobis par produit matriciel (`sondes/familles_v2`, C-V3-4) : même quantité que le paquet gelé (écart relatif
< 10⁻¹² sur 256 jetons tirés, et sur des actions entières par `score_action`), même interface et même empreinte ; essai
d'égalité sur un cas sain et sur un artefact (paramètres altérés → `GardeArret`) ; le paquet gelé reste intact (R5, R12)."""
from __future__ import annotations

import hashlib
from pathlib import Path

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.harnais.sondes import score_action
from controle_ia.sondes import familles as fg
from controle_ia.sondes import familles_v2 as fv2

RACINE = Path(__file__).resolve().parents[1]


def _donnees(d=64, n=40, graine=0):
    rng = np.random.default_rng(graine)
    seqs = [rng.standard_normal((int(rng.integers(3, 12)), d)) * (1 + rng.random(d)) + rng.standard_normal(d) for _ in range(n)]
    y = np.array([k % 2 for k in range(n)])
    return seqs, y


def test_sonde_v2_egale_au_paquet_gele_meme_interface():
    seqs, y = _donnees()
    gele = fg.entrainer("mahalanobis", "m", 5, seqs, y, "max", 0, fg.Reglages())
    v2 = fv2.entrainer_v2("mahalanobis", "m", 5, seqs, y, "max", 0, fg.Reglages(), fv2.PRODUIT_MATRICIEL_V2)
    assert isinstance(gele, fg.SondeMahalanobis) and not isinstance(gele, fv2.SondeMahalanobisV2) and isinstance(v2, fv2.SondeMahalanobisV2)
    assert (v2.nom, v2.couche, v2.agregation, v2.famille, v2.calcul) == ("m", 5, "max", "mahalanobis", fv2.PRODUIT_MATRICIEL_V2)
    assert v2.empreinte() == gele.empreinte() and np.array_equal(v2.P, gele.P) and np.array_equal(v2.mu, gele.mu)
    acts = np.random.default_rng(3).standard_normal((256, 64)) * 3
    a, b = gele.scores_par_jeton(acts), v2.scores_par_jeton(acts)
    assert a.shape == b.shape == (256,) and np.max(np.abs(a - b) / np.abs(a)) < 1e-12
    for s in seqs[:5]:                                                             # score d'action (maximum), par le harnais
        assert abs(score_action(gele, s, 0, len(s)) - score_action(v2, s, 0, len(s))) <= 1e-12 * abs(score_action(gele, s, 0, len(s)))
    with pytest.raises(GardeArret, match="maximum seulement"):
        v2.logits_attention(acts)
    # sous le calcul « paquet_gele », entrainer_v2 rend la sonde du paquet gelé telle quelle ; les autres familles sont intactes
    assert type(fv2.entrainer_v2("mahalanobis", "m", 5, seqs, y, "max", 0, fg.Reglages(), fv2.PAQUET_GELE)) is fg.SondeMahalanobis
    assert isinstance(fv2.entrainer_v2("lineaire", "l", 5, seqs, y, "max", 0, fg.Reglages(), fv2.PRODUIT_MATRICIEL_V2), fg.SondeLineaireJetons)
    with pytest.raises(GardeArret, match="inconnu"):
        fv2.entrainer_v2("mahalanobis", "m", 5, seqs, y, "max", 0, fg.Reglages(), "autre")
    with pytest.raises(GardeArret, match="paquet gelé est attendue"):
        fv2.en_produit_matriciel(fg.SondeLineaireJetons("l", 1, "max", np.ones(3), 0.0))


def test_essai_d_egalite_cas_sain_et_artefact():
    seqs, _ = _donnees(graine=1)
    v2 = fv2.mahalanobis_v2("m", 2, seqs)
    r = fv2.verifier_egalite_au_paquet_gele(v2, 2026)
    assert r["egal"] and r["n_jetons"] == 256 and r["graine"] == 2026 and r["ecart_relatif_max"] < 1e-12 and r["tolerance"] == 1e-12
    assert fv2.verifier_egalite_au_paquet_gele(v2, 2026) == r                       # déterministe (R9)
    # artefact : une v2 dont P diffère de 10⁻⁹ de la référence (le paquet gelé aux mêmes paramètres ne peut pas le voir :
    # l'essai compare deux formules sur les MÊMES paramètres ; on altère donc la formule par une sous-classe)
    class _Alteree(fv2.SondeMahalanobisV2):
        def scores_par_jeton(self, acts):
            return super().scores_par_jeton(acts) * (1 + 1e-9)
    alt = _Alteree(v2.nom, v2.couche, v2.mu, v2.P)
    with pytest.raises(GardeArret, match="Mahalanobis v2 ≠ paquet gelé"):
        fv2.verifier_egalite_au_paquet_gele(alt, 2026)
    with pytest.raises(GardeArret, match="porte sur une sonde de Mahalanobis v2"):
        fv2.verifier_egalite_au_paquet_gele(v2.en_paquet_gele(), 2026)
    with pytest.raises(GardeArret, match="non finie ou non positive"):
        fv2.verifier_egalite_au_paquet_gele(fv2.SondeMahalanobisV2("x", 1, np.zeros(2), -np.eye(2)), 1)


def test_paquet_gele_intact():
    """`sondes/familles.py` est le paquet gelé de T0.7 : même empreinte que sur `main` (`6758b651…`, relevée au départ de la
    v3) ; `scores_par_jeton` de Mahalanobis y reste l'einsum à trois opérandes (aucune modification, R12)."""
    gele = RACINE / "src" / "controle_ia" / "sondes" / "familles.py"
    assert hashlib.sha256(gele.read_bytes()).hexdigest() == "6758b651fdcbc6d0108a03263b79ffb1e7c5d0a8be57b0f10502c1645d2b457e"
    corps = gele.read_text(encoding="utf-8").split("class SondeMahalanobis")[1].split("def logits_attention")[0]
    assert 'np.einsum("nd,de,ne->n", z, self.P, z)' in corps and "optimize" not in corps
