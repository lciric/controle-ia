"""Diagnostic de l'essai B5 (lecture de l'étiqueteur) : rejoue l'essai scellé tel quel, puis avec une latence simulée.
Ne modifie aucun fichier scellé : importe le module d'essais du commit 64e67cbd depuis une copie détachée."""
import sys, time
from pathlib import Path
import pytest
sys.path.insert(0, "/tmp/claude-0/-home-user-ideation-organism/86976e6f-3fae-57b1-a905-26802f445363/scratchpad/code-64e67cbd/docs/notes/epreuve-etiqueteur-v1")
import test_lire_items_phase1_v4 as T
from test_lire_items_phase1_v4 import entrees  # noqa: F401  (fixture réutilisée)


class CompteurLent(T.Compteur):
    def __call__(self, lecteur, lecture, item, tentative, consigne):
        self.appels.append((lecteur, lecture, item))
        time.sleep(0.02)  # latence d'un appel réel, très réduite (un vrai appel : 20 à 30 s)
        return self.simule(lecteur, lecture, item, tentative, consigne)


@pytest.mark.parametrize("i", range(40))
def test_b5_tel_quel(entrees, tmp_path, monkeypatch, i):
    T.test_B5_cle_refusee_arrete_tous_les_appels(entrees, tmp_path, monkeypatch)


@pytest.mark.parametrize("i", range(40))
def test_b5_latence_20ms(entrees, tmp_path, monkeypatch, i):
    monkeypatch.setattr(T, "Compteur", CompteurLent)
    T.test_B5_cle_refusee_arrete_tous_les_appels(entrees, tmp_path, monkeypatch)
