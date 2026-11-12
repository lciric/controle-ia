"""Sondes figées de P3 : aller-retour exact (scores et empreintes), fichier scellé, refus d'écraser, altération vue."""
import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.harnais.sondes import SondeLineaire
from controle_ia.premier_test_ia.figees import ecrire_sondes, lire_sondes
from controle_ia.premier_test_ia.notation import Notation
from controle_ia.sondes.evaluation import plancher_apparie
from controle_ia.sondes.familles import Reglages, entrainer


def _sondes():
    rng = np.random.default_rng(3)
    seqs = [rng.standard_normal((5, 6)) + (k % 2) for k in range(12)]
    y = np.array([k % 2 for k in range(12)])
    s = [entrainer(f, f"{f}-{a}", 0, seqs, y, a, 1, Reglages(epoques=3))
         for f, a in (("difference_moyennes", "max"), ("lineaire", "attention"), ("perceptron", "max"),
                      ("perceptron", "attention"), ("attention", "attention"), ("mahalanobis", "max"))]
    s += plancher_apparie("pl", 0, seqs, "attention", 3, 2)
    s.append(SondeLineaire("h", 0, rng.standard_normal(6), 0.1, "max"))
    return s, rng


def test_aller_retour(tmp_path):
    sondes, rng = _sondes()
    sha = ecrire_sondes(tmp_path / "f.npz", sondes, {"principales": ["lineaire-attention"]})
    relues, meta, sha2 = lire_sondes(tmp_path / "f.npz", sha)
    assert sha2 == sha and meta == {"principales": ["lineaire-attention"]}
    assert [s.nom for s in relues] == [s.nom for s in sondes]
    assert [s.empreinte() for s in relues] == [s.empreinte() for s in sondes]
    seg = {0: rng.standard_normal((4, 6))}
    assert Notation(relues).noter(seg) == Notation(sondes).noter(seg)
    with pytest.raises(GardeArret, match="R12"):
        ecrire_sondes(tmp_path / "f.npz", sondes, {})
    with pytest.raises(GardeArret, match="attendue"):
        lire_sondes(tmp_path / "f.npz", "0" * 64)


def test_alteration_vue(tmp_path):
    sondes, _ = _sondes()
    ecrire_sondes(tmp_path / "f.npz", sondes, {})
    with open(tmp_path / "f.npz", "ab") as f:
        f.write(b"x")
    with pytest.raises(GardeArret):
        lire_sondes(tmp_path / "f.npz")
