"""Configuration v5 et lanceur v5 (E3 du 7 novembre) : la configuration d'épreuve d'E3 (plafond 4,27) était refusée par `configuration_v4` au démarrage du run
(« plafond 4.27 : (1.5, 3.5) USD attendus ») ; la suite complète échouée l'avait masqué. Cas sain et artefact (R5)."""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.t06 import configuration_v4 as cf4
from controle_ia.t06 import configuration_v5 as cf5

D = Path(__file__).resolve().parents[1] / "docs" / "notes" / "g0-deux-semaines-v1"
RACINE = Path(__file__).resolve().parents[1]


def _epreuve(plafond):
    c = json.loads((D / "config-t06-epreuve-e3-v3.json").read_text(encoding="utf-8"))          # configuration d'épreuve réelle du dépôt (E3 v3, plafond 4,3)
    c["plafond_usd"] = plafond
    for k in ("taches_evaluation", "taches_distillation"):
        if c.get(k) and len(c[k]["sha256"]) != 64:
            c[k]["sha256"] = "a" * 64
    return c


@pytest.mark.parametrize("plafond", [1.5, 3.5, 4.27, 4.3, 5.7, 8, 8.0, 0.01])
def test_v5_accepte_un_plafond_d_epreuve_de_zero_a_huit(plafond):
    cf5.exiger_config_t06_v5(_epreuve(plafond))


@pytest.mark.parametrize("plafond", [0, -1, 8.01, 9, float("nan"), float("inf"), True, "4.27", None])
def test_v5_refuse_un_plafond_d_epreuve_hors_de_zero_a_huit(plafond):
    with pytest.raises(GardeArret, match="plafond"):
        cf5.exiger_config_t06_v5(_epreuve(plafond))


def test_artefact_la_v4_refuse_4_27_et_5_7_au_demarrage_du_run():
    for p in (4.27, 5.7):
        with pytest.raises(GardeArret, match=r"\(1.5, 3.5\)"):
            cf4.exiger_config_t06_v4(_epreuve(p))


def test_la_course_est_inchangee_v5_valide_la_configuration_reelle_comme_la_v4():
    c = json.loads((D / "config-t06-reel-v1-brouillon5.json").read_text(encoding="utf-8"))
    cf4.exiger_config_t06_v4(c)
    cf5.exiger_config_t06_v5(c)
    c["plafond_usd"] = 150                                                   # une configuration de course n'a pas la règle d'épreuve : sa validation (v3) reste celle de la v4
    with pytest.raises(GardeArret):
        cf4.exiger_config_t06_v4(c)
    with pytest.raises(GardeArret):
        cf5.exiger_config_t06_v5(c)


def test_le_lanceur_v5_ne_differe_du_v4_que_par_l_import_la_commande_et_la_note():
    a = (RACINE / "src" / "controle_ia" / "t06" / "lanceur_v4.py").read_text(encoding="utf-8").splitlines()
    b = (RACINE / "src" / "controle_ia" / "t06" / "lanceur_v5.py").read_text(encoding="utf-8").splitlines()
    diff = [(x, y) for x, y in zip(a, b[1:]) if x != y]
    assert len(b) == len(a) + 1 and b[0].startswith("# [v5") and len(diff) == 2, diff
    assert "configuration_v5" in diff[0][1] and "lanceur_v5" in diff[1][1]


def test_configuration_d_e3_bis_seul_le_plafond_change_et_elle_passe_la_validation_v5():
    b = json.loads((D / "config-t06-epreuve-e3bis-v1.json").read_text(encoding="utf-8"))
    cf5.exiger_config_t06_v5(b)
    assert b["plafond_usd"] == 5.7 and b["go_id"] == "GO-2026-11-06-01" and b["offre"]["etiquette"] == "t06-e3" and b["offre"]["stockage_max_usd_h"] == 0.08
    assert b["offre"]["telechargement_max_usd_go"] == 0.03 and b["mode"] == "reel" and b["calendrier"] == {"dernier_jour_creation": "2026-11-09", "fin_go_utc": "2026-11-11T00:00:00Z"}
    from controle_ia.t06 import session_v10 as s10
    assert "≤ 7.9" in s10.verifier_plafond_epreuve(b["plafond_usd"], "2.092", "8")


# --- demande de la mère (R-1735) : les VRAIES configurations jusqu'à la validation par `lanceur_v5` ------------------------------------------------------------
class _ApresValidation(Exception):
    pass


def _jusqu_au_manifeste(config_fichier, monkeypatch, prereg=None):
    from controle_ia.t06 import lanceur_v5 as la5
    config = json.loads((D / config_fichier).read_text(encoding="utf-8"))

    def arret(*a, **k):
        raise _ApresValidation()
    monkeypatch.setattr(la5, "creer_manifeste", arret)
    la5.executer(config, RACINE, "20261108-000000-t06-reel", prereg)


@pytest.mark.parametrize("fichier", ["config-t06-epreuve-e3-v5.json", "config-t06-epreuve-e3bis-v1.json", "config-t06-epreuve-e3bis-v2.json"])
def test_les_vraies_configurations_d_epreuve_passent_validation_taches_pas_et_consignes_jusqu_au_manifeste(fichier, monkeypatch):
    """E3 v5 (plafond 4,27) et E3 bis (5,7), mode réel, sans préenregistrement : `lanceur_v5.executer` va jusqu'à la création du manifeste (l'essai s'arrête là)."""
    with pytest.raises(_ApresValidation):
        _jusqu_au_manifeste(fichier, monkeypatch)


@pytest.mark.parametrize("fichier", ["config-t06-epreuve-e3-v5.json", "config-t06-epreuve-e3bis-v1.json"])
def test_artefact_le_lanceur_v4_arrete_les_memes_configurations_a_la_validation(fichier, monkeypatch):
    from controle_ia.t06 import lanceur_v4 as la4
    config = json.loads((D / fichier).read_text(encoding="utf-8"))
    monkeypatch.setattr(la4, "creer_manifeste", lambda *a, **k: (_ for _ in ()).throw(_ApresValidation()))
    with pytest.raises(GardeArret, match=r"\(1.5, 3.5\)"):
        la4.executer(config, RACINE, "20261108-000100-t06-reel", None)


def test_la_configuration_de_la_course_passe_la_validation_du_lanceur_v5_et_attend_son_preenregistrement(monkeypatch):
    """Course (plafond 200, GO-2026-11-02-28) : la validation passe ; sans préenregistrement le lanceur refuse ENSUITE, pour le bon motif (R1)."""
    with pytest.raises(GardeArret, match="sans préenregistrement"):
        _jusqu_au_manifeste("config-t06-reel-v1-brouillon5.json", monkeypatch)


def test_le_lanceur_v5_utilise_la_validation_de_la_configuration_v5():
    from controle_ia.t06 import lanceur_v5 as la5
    assert la5.exiger_config_t06_v4 is cf5.exiger_config_t06_v5 and la5.COMMANDE.endswith("lanceur_v5")


def test_configuration_d_e3_bis_v2_cite_go_2026_11_07_08_echeance_12_novembre():
    """R-1746 : la configuration d'E3 bis cite GO-2026-11-07-08 (3 USD de plus, échéance 12 novembre ; création permise jusqu'au 11) ; seuls go_id et calendrier changent par rapport à la v1."""
    v1 = json.loads((D / "config-t06-epreuve-e3bis-v1.json").read_text(encoding="utf-8"))
    v2 = json.loads((D / "config-t06-epreuve-e3bis-v2.json").read_text(encoding="utf-8"))
    assert {k: x for k, x in v1.items() if k not in ("go_id", "calendrier")} == {k: x for k, x in v2.items() if k not in ("go_id", "calendrier")}
    assert v2["go_id"] == "GO-2026-11-07-08" and v2["plafond_usd"] == 5.7 and v2["calendrier"] == {"dernier_jour_creation": "2026-11-11", "fin_go_utc": "2026-11-13T00:00:00Z"}
    cf5.exiger_config_t06_v5(v2)
    assert cf5.est_epreuve(v2) and not cf4.est_epreuve(v2)                                  # la v4 ne la reconnaît pas comme épreuve : elle serait lue comme une configuration de course
