"""Génération par lots du harnais (T0.4, préparation du modèle réel), sur modèle jouet à gabarit de conversation.

Couvre : remplissage à gauche et positions explicites (équivalence génération / passe unique sur des
contextes de longueurs différentes), indépendance des lignes d'un lot, graine par ligne, rejeu au bit
près à plan de lots identique, relecture des crochets par ligne, gardes d'équivalence et de contrôle
négatif (cas sain + artefacts : relecture désalignée, activations constantes le long des positions).
"""
import numpy as np
import pytest

import controle_ia.harnais.episode as E
from controle_ia.gardes import GardeArret
from controle_ia.harnais.activations import ecart_equivalence, exiger_controle_negatif
from controle_ia.harnais.episode import (EnvironnementJouet, empreinte_episode, generer_lot, jouer_episodes,
                                         relire_crochets_lot)
from controle_ia.harnais.formats import FormatChat
from controle_ia.harnais.modeles import modele_jouet, regler_determinisme, tokeniseur_caracteres_chat

regler_determinisme(1)
TOK = tokeniseur_caracteres_chat()
FIN = TOK.convert_tokens_to_ids("<|im_end|>")
FMT = FormatChat(TOK, fins={FIN, TOK.eos_token_id})


def _modele(graine=11):
    return modele_jouet(graine, len(TOK), couches=4, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)


def _graines(B, N, T, base=1000):
    return [{(i, t): base + 100 * b + 10 * i + t for t in range(T) for i in range(N)} for b in range(B)]


def _jouer(m, graines, B=3, N=2, T=3, echantillon=None, **kw):
    if echantillon is None:
        echantillon = {(b, i, t) for b in range(B) for i in range(N) for t in range(T)}
    return jouer_episodes(m, FMT, EnvironnementJouet(), [f"ep{b}" for b in range(B)], N, T, graines, [0, 1, 2],
                          max_nouveaux=12, echantillon_equivalence=echantillon, **kw)


def test_lot_equivalence_avec_remplissage():
    sorties = _jouer(_modele(), _graines(3, 2, 3))
    longueurs = {len(ep.transcriptions[0].ids) for ep, _, _ in sorties}
    assert len(longueurs) > 1                       # contextes de longueurs différentes : remplissage exercé
    for ep, acts, rapport in sorties:
        assert len(rapport["ecarts"]) == 6
        assert max(max(e.values()) for e in rapport["ecarts"].values()) < 1e-5
        zones = [z for z in rapport["controle_negatif_zone_generee"].values() if z is not None]
        assert zones and min(v["max"] for z in zones for v in z.values()) > 1e-4
        assert all(s == {"tableaux_distincts": True, "ulp_vu": True} for s in rapport["sondes"].values())
        for tr in ep.transcriptions:
            for a in tr.actions:
                assert tr.ids[a.debut:a.fin] == a.ids
                fermee = tr.ids[a.fin:a.fin + 2]      # clôture du tour : fin de tour (si non générée) puis saut de ligne
                assert FIN in a.ids[-1:] + fermee[:1]


def test_lot_lignes_independantes_et_graine_par_ligne():
    m = _modele()
    ctx = FMT.ouverture("Tu es l'agent 0.", "Pas 0.")
    a, _ = generer_lot(m, [ctx] * 3, 10, 1.0, [1, 2, 3], FMT.fins, TOK.pad_token_id)
    b, _ = generer_lot(m, [ctx] * 3, 10, 1.0, [1, 99, 3], FMT.fins, TOK.pad_token_id)
    assert a[0] == b[0] and a[2] == b[2] and a[1] != b[1]
    c, _ = generer_lot(m, [ctx] * 2, 10, 1.0, [5, 5], FMT.fins, TOK.pad_token_id)
    assert c[0] == c[1]
    with pytest.raises(GardeArret, match="graines en nombre"):
        generer_lot(m, [ctx] * 2, 10, 1.0, [5], FMT.fins, TOK.pad_token_id)


def test_lot_rejeu_au_bit_pres_et_graine_manquante():
    m = _modele()
    g = _graines(3, 2, 2)
    e1 = [empreinte_episode(ep, acts) for ep, acts, _ in _jouer(m, g, T=2, echantillon=set())]
    e2 = [empreinte_episode(ep, acts) for ep, acts, _ in _jouer(m, g, T=2, echantillon=set())]
    assert e1 == e2
    g[1] = dict(g[1])
    del g[1][(1, 1)]
    with pytest.raises(GardeArret, match="graine absente"):
        _jouer(m, g, T=2)


def test_relecture_des_crochets_par_ligne():
    rng = np.random.default_rng(0)
    morceaux = {0: [rng.standard_normal((2, 5, 4)).astype(np.float32)]
                + [rng.standard_normal((2, 1, 4)).astype(np.float32) for _ in range(4)]}
    plan = {"longueur_remplie": 5, "passes_decodage": 4}
    r = relire_crochets_lot(morceaux, 1, 3, plan, 2)[0]
    attendu = np.concatenate([morceaux[0][0][1, 2:], morceaux[0][1][1], morceaux[0][2][1]])
    assert r.shape == (5, 4) and np.array_equal(r, attendu)
    with pytest.raises(GardeArret, match="captures"):
        relire_crochets_lot(morceaux, 1, 3, {"longueur_remplie": 5, "passes_decodage": 5}, 2)


def test_garde_d_equivalence_sur_relecture_desalignee(monkeypatch):
    vrai = E.relire_crochets_lot

    def desalignee(brut, k, longueur_contexte, plan, n_generes):      # artefact : un jeton de remplissage gardé
        return vrai(brut, k, longueur_contexte + 1, plan, n_generes)
    monkeypatch.setattr(E, "relire_crochets_lot", desalignee)
    with pytest.raises(GardeArret, match="génération ≠ passe unique"):
        _jouer(_modele(), _graines(3, 2, 2), T=2)


def test_controle_negatif_zone_generee_artefact():
    """Contre-lecture 1, Rem-1 : activations constantes le long de la zone générée, des deux côtés, contexte intact.
    Le contrôle sur toutes les positions passerait ; restreint à la zone générée, la garde arrête."""
    from controle_ia.harnais.activations import ecart_decale_zone_generee
    from controle_ia.harnais.episode import bilan_controle_negatif, exiger_controle_negatif_phase
    rng = np.random.default_rng(1)
    lc, n = 20, 8
    p = {0: rng.standard_normal((lc + n, 6)).astype(np.float32)}
    g = {0: p[0].copy()}
    sain = ecart_decale_zone_generee(g, p, lc, 1e-4)
    assert sain[0]["max"] > 1e-4 and sain[0]["positions"] == n - 1
    for a in (g, p):
        a[0][lc:] = a[0][lc]                                   # artefact : zone générée constante
    assert ecart_equivalence(g, p, decalage=1)[0] > 1e-4       # l'ancien contrôle (toutes positions) passerait
    zone = ecart_decale_zone_generee(g, p, lc, 1e-4)
    assert zone[0]["max"] == 0.0
    rapport = {"tolerance": 1e-4, "controle_negatif_zone_generee": {f"0,{t}": zone for t in range(10)}}
    bilan = bilan_controle_negatif([rapport], positions_min=4)
    assert bilan["comparables"] == 10 and bilan["passent"] == 0 and bilan["fraction"] == 0.0
    with pytest.raises(GardeArret, match="aveugle"):
        exiger_controle_negatif_phase(bilan, 0.95, 10, "artefact")
    assert ecart_decale_zone_generee({0: g[0][:lc + 1]}, p, lc, 1e-4) is None   # une seule position décodée : trop court


def test_controle_negatif_de_phase():
    """Contre-lecture 2, N-14 : le contrôle négatif se juge sur la phase ; actions courtes comptées à part ; une action
    isolée sous le seuil ne fait pas tomber une phase qui voit le décalage partout ailleurs."""
    from controle_ia.harnais.episode import bilan_controle_negatif, exiger_controle_negatif_phase
    zone = lambda m, pos: {0: {"max": m, "au_dessus": 0, "positions": pos}, 1: {"max": m, "au_dessus": 0, "positions": pos}}
    r = {"episode": "episode-1", "tolerance": 0.1, "controle_negatif_zone_generee":
         {**{f"0,{t}": zone(1.2, 9) for t in range(40)}, "1,0": zone(0.003, 9), "1,1": zone(0.002, 2), "1,2": None}}
    b = bilan_controle_negatif([r], positions_min=4)
    assert (b["comparables"], b["passent"], b["courtes"], b["echecs"]) == (41, 40, 2, ["episode-1:1,0"])
    exiger_controle_negatif_phase(b, 0.95, 10, "sain")              # 40/41 ≥ 0,95
    with pytest.raises(GardeArret, match="aveugle"):
        exiger_controle_negatif_phase(b, 0.99, 10, "exigence plus haute")
    exiger_controle_negatif_phase(b, 0.95, 50, "trop peu d'actions : rien ne se juge")
    nan = bilan_controle_negatif([{"tolerance": 0.1, "controle_negatif_zone_generee": {"0,0": zone(float("nan"), 9)}}])
    assert nan["passent"] == 0 and nan["min_des_maxima"] == float("-inf")
    # M-10 : un NaN sur une seule couche fait échouer l'action quel que soit l'ordre des couches ; échecs nommés
    for ordre in ((7, 15, 23), (15, 7, 23)):
        z = {c: {"max": float("nan") if c == 15 else 1.2, "au_dessus": 0, "positions": 9} for c in ordre}
        b2 = bilan_controle_negatif([{"episode": "episode-3", "tolerance": 0.1, "controle_negatif_zone_generee": {"1,4": z}}])
        assert b2["passent"] == 0 and b2["echecs"] == ["episode-3:1,4"]


def test_positions_explicites_avec_remplissage():
    """Contre-lecture 3, M-3 : les positions transmises au modèle repartent de 0 au premier jeton réel de chaque
    ligne remplie (un décalage constant par ligne échappe à l'équivalence, invariante par translation)."""
    m = _modele()
    vues = []
    vrai = m.forward

    def espion(*args, **kw):
        vues.append(kw["position_ids"].clone())
        return vrai(*args, **kw)
    m.forward = espion
    court, long_ = FMT.ouverture("A.", "B."), FMT.ouverture("Tu es l'agent 0, longuement.", "Pas 0. Journal : x")
    generer_lot(m, [court, long_], 3, 1.0, [1, 2], FMT.fins, TOK.pad_token_id)
    pref = vues[0]
    marge = len(long_) - len(court)
    assert pref[0, marge].item() == 0 and pref[0, -1].item() == len(court) - 1
    assert pref[1, 0].item() == 0 and pref[1, -1].item() == len(long_) - 1
    assert vues[1][0, 0].item() == len(court) and vues[1][1, 0].item() == len(long_)


def test_controle_negatif_sain_et_aveugle():
    exiger_controle_negatif({0: 0.5, 1: 0.2}, 1e-4, "sain")
    constantes = {0: np.ones((6, 4), np.float32)}                       # artefact : rien ne varie le long des positions
    decale = ecart_equivalence(constantes, {0: np.ones((8, 4), np.float32)}, decalage=1)
    with pytest.raises(GardeArret, match="aveugle"):
        exiger_controle_negatif(decale, 1e-4, "artefact")


def test_defaut_d1_injecte_dans_les_positions_decodees():
    """Version 2, contrôle positif : `decalage_positions` décale les positions des jetons décodés (défaut D1), et
    seulement elles ; 0 (usage normal) les laisse à la suite du contexte."""
    m = _modele()
    vues = []
    vrai = m.forward

    def espion(*args, **kw):
        vues.append(kw["position_ids"].clone())
        return vrai(*args, **kw)
    m.forward = espion
    court, long_ = FMT.ouverture("A.", "B."), FMT.ouverture("Tu es l'agent 0, longuement.", "Pas 0. Journal : x")
    for decalage in (0, 1):
        vues.clear()
        generer_lot(m, [court, long_], 3, 1.0, [1, 2], set(), TOK.pad_token_id, decalage_positions=decalage)
        assert vues[0][1, -1].item() == len(long_) - 1                       # prérempli intact
        assert vues[1][0, 0].item() == len(court) + decalage and vues[1][1, 0].item() == len(long_) + decalage
        assert vues[2][1, 0].item() == len(long_) + 1 + decalage


def test_chrono_longueur_remplie_maximale():
    """Version 2 : le chrono consigne le plus long contexte rempli d'un lot, qui fixe le pic de mémoire du
    préremplissage ; c'est le maximum, sur les pas, du plus long contexte du lot (toutes lignes, pas seulement
    l'échantillon d'équivalence)."""
    chrono = {}
    sorties = _jouer(_modele(), _graines(3, 2, 3), echantillon={(0, 0, 0)}, chrono=chrono)
    attendu = max(a.debut for ep, _, _ in sorties for tr in ep.transcriptions for a in tr.actions)
    assert chrono["longueur_remplie_max"] == attendu
    assert attendu > max(a.debut for tr in sorties[0][0].transcriptions for a in tr.actions if a.pas == 0)


class _EnvMarque(EnvironnementJouet):
    """Environnement jouet dont la consigne porte une marque (une tâche par épisode)."""

    def __init__(self, marque):
        self.marque = marque

    def consigne_privee(self, agent):
        return f"Tâche {self.marque}. " + super().consigne_privee(agent)


def test_un_environnement_par_episode():
    m, g = _modele(), _graines(3, 2, 2)
    commun = jouer_episodes(m, FMT, EnvironnementJouet(), [f"ep{b}" for b in range(3)], 2, 2, g, [0, 1, 2],
                            max_nouveaux=8)
    liste = jouer_episodes(m, FMT, [EnvironnementJouet() for _ in range(3)], [f"ep{b}" for b in range(3)], 2, 2, g,
                           [0, 1, 2], max_nouveaux=8)
    assert [empreinte_episode(ep, a) for ep, a, _ in commun] == [empreinte_episode(ep, a) for ep, a, _ in liste]
    marques = jouer_episodes(m, FMT, [_EnvMarque(k) for k in "ABC"], [f"ep{b}" for b in range(3)], 2, 2, g,
                             [0, 1, 2], max_nouveaux=8)
    for (ep, _, _), k in zip(marques, "ABC"):
        assert f"Tâche {k}." in TOK.decode(ep.transcriptions[0].ids)
        assert all(f"Tâche {x}." not in TOK.decode(ep.transcriptions[0].ids) for x in "ABC" if x != k)


def test_nombre_d_environnements_controle():
    with pytest.raises(GardeArret, match="environnements pour"):
        jouer_episodes(_modele(), FMT, [EnvironnementJouet()] * 2, ["a", "b", "c"], 1, 1, _graines(3, 1, 1),
                       [0, 1, 2], max_nouveaux=4)
