"""Contre-lecture des corrections (CLC) : artefacts de la garde du 3B rechargé hors ligne, sur le banc jouet du module.
À copier dans tests/ d'une copie du dépôt ; s'appuie sur les auxiliaires de tests/test_noter_rejeu_juges_v2.py."""
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.manifeste import verifier_resultat
from test_noter_rejeu_juges_v2 import TOK, _config, _notations_artisanales, nrj2


def test_artefact_fins_de_ligne_du_3b_recharge_differentes(depot, monkeypatch):
    """Vocabulaire du 3B rechargé avec un jeton de fin de ligne en plus (3e appel à fins vides) : arrêt avant phase."""
    f = _notations_artisanales(depot, monkeypatch)
    vrai, n = nrj2.jetons_terminaux, []

    def faux(tok, fins):
        s = vrai(tok, fins)
        if not set(fins):
            n.append(1)
            if len(n) == 3:
                s = sorted(set(s) | {TOK.convert_tokens_to_ids("a")})
        return s

    monkeypatch.setattr(nrj2, "jetons_terminaux", faux)
    run = "20261029-130000-rejeu-v2-jouet"
    with pytest.raises(GardeArret, match="encodage chargé hors ligne"):
        nrj2.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    r = verifier_resultat(depot, depot / "diag" / run / "arret.json")["resultat"]
    assert r["partiel"]["phases"] == []


def test_trou_fin_du_modele_sur_un_chiffre_passe(depot, monkeypatch):
    """Trou : une « fin du modèle » qui est un chiffre (configuration de génération fautive) passe la garde corrigée ;
    elle entre dans les terminaux de la lecture du 3B. Ce test PASSE si le trou existe."""
    f = _notations_artisanales(depot, monkeypatch)
    vrai = nrj2.charger_modele_et_format
    CHIFFRE = TOK.convert_tokens_to_ids("0")

    def charger(spec, mode, graine, hors_ligne=False):
        m, fmt = vrai(spec, mode, graine, hors_ligne=hors_ligne)
        if hors_ligne:
            fmt.fins = set(fmt.fins) | {CHIFFRE}
        return m, fmt

    monkeypatch.setattr(nrj2, "charger_modele_et_format", charger)
    run = "20261029-130001-rejeu-v2-jouet"
    resume = nrj2.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    assert [p["statut"] for p in resume["phases"]] == ["écrit", "écrit"]
