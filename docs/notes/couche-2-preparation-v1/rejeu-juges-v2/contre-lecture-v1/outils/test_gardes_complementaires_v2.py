"""Gardes du module v2 que la suite du rédacteur n'éprouve pas sur un artefact (R5) : cas sain et artefact."""
from types import SimpleNamespace
import pytest, torch
import test_noter_rejeu_juges_v2 as t2
from test_noter_rejeu_juges_v1 import CTX, _notations_artisanales
from controle_ia.environnements import noter_rejeu_juges_v2 as nrj2
from controle_ia.environnements.rubrique import CRITERES
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import verifier_resultat


class CacheMenteur(t2.BigrammeCache):
    """Rend un cache d'une longueur fausse (un de plus)."""
    def forward(self, *a, **k):
        s = super().forward(*a, **k)
        if s.past_key_values is not None:
            s.past_key_values.n += 1
        return s


class LignesEnMoins(t2.BigrammeCache):
    """Rend une ligne de logits de moins que demandé."""
    def forward(self, *a, **k):
        s = super().forward(*a, **k)
        return SimpleNamespace(logits=s.logits[:, :-1], past_key_values=s.past_key_values)


def test_passe_principale_cache_de_longueur_fausse_et_lignes_manquantes():
    t2._lire(t2._table())                                               # cas sain
    with pytest.raises(GardeArret, match="longueur ≠ la suite"):
        t2._lire(t2._table(), modele=CacheMenteur)
    with pytest.raises(GardeArret, match="lignes rendues|demandées"):
        t2._lire(t2._table(), modele=LignesEnMoins)


def test_prolongement_longueur_rendue_fausse():
    lignes, c = nrj2.prolonger(t2.BigrammeCache(t2._table()), t2.FauxCache(4), [t2._i("2")], 4)   # sain
    with pytest.raises(GardeArret, match="prolongement"):
        nrj2.prolonger(CacheMenteur(t2._table()), t2.FauxCache(4), [t2._i("2")], 4)


def test_lecture_sans_contexte():
    with pytest.raises(GardeArret, match="sans contexte"):
        nrj2.lire_par_probabilite_v2(t2.BigrammeCache(t2._table()), t2.TOK, [], t2.COMPLET, CRITERES, True, 0.5,
                                     t2.TERM)


def test_generer_lot_borne_lot_vide_et_graines():
    m = t2.BigrammeCache(t2._table())
    ctx = [t2.TOK.encode("ab", add_special_tokens=False)]
    nrj2.generer_lot_borne(m, ctx, 2, 1.0, [1], {t2.TOK.eos_token_id}, t2.TOK.pad_token_id, {t2.NL}, lambda j: False)
    for contextes, graines in (([], []), (ctx, [1, 2]), ([[]], [1])):
        with pytest.raises(GardeArret, match="lot vide"):
            nrj2.generer_lot_borne(m, contextes, 2, 1.0, graines, {t2.TOK.eos_token_id}, t2.TOK.pad_token_id,
                                   {t2.NL}, lambda j: False)


def test_encodage_du_3b_recharge_different_arrete_avant_toute_phase(depot, monkeypatch):
    f = _notations_artisanales(depot, monkeypatch)
    vrai, appels = nrj2.controler_encodage_v2, []

    def change(tok, mode, terminaux, *a):
        sortie = dict(vrai(tok, mode, terminaux, *a))
        appels.append(1)
        if len(appels) > 2:                     # rechargement hors ligne du 3B : encodage différent (artefact)
            sortie["valeurs_controlees_v2"] = -1
        return sortie

    monkeypatch.setattr(nrj2, "controler_encodage_v2", change)
    run = "20261029-120000-rejeu-v2-jouet"
    with pytest.raises(GardeArret, match="encodage chargé hors ligne"):
        nrj2.executer(t2._config(), depot, run, None, str(f), autoriser_depot_sale=True)
    r = verifier_resultat(depot, depot / "diag" / run / "arret.json")["resultat"]
    assert r["partiel"]["phases"] == []
