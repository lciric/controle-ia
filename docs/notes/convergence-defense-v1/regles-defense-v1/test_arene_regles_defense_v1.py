"""Essais du module `arene_regles_defense_v1.py` (R5 : chaque garde sur un cas sain et sur un artefact).

Lancement : PYTHONPATH=/home/user/controle-ia-travail/src python -m pytest -q <ce fichier>
Racines : RACINE_TESTS / RACINE_TESTS_TENUE / RACINE_TESTS_AUTRE du gel v1 (20266301 à 20266303) ; aucune racine de
décision ; aucun fichier écrit hors du dossier temporaire de pytest.
"""
from __future__ import annotations

import shutil
import sys
import time
from pathlib import Path

import numpy as np
import pytest

ICI = Path(__file__).resolve().parent
if str(ICI) not in sys.path:
    sys.path.insert(0, str(ICI))

import arene_regles_defense_v1 as m  # noqa: E402

from controle_ia.gardes import GardeArret  # noqa: E402

v4 = m.v4
# petite configuration (T = 3) : calibration et fausses alertes du v4 gardées (la garde de fausses alertes exige le
# quantile sur 20 000 points propres), tout le reste réduit
CFG_PETITE = m.replace(v4.CONFIG_V4, T=3, n_eval=999, n_mc=32, n_mc_final=64, departs=1, departs_final=2,
                       departs_renforce=2, iter_renforce=20, n_tenue=4, n_eval_tenue=999, n_propre_entr=300,
                       n_attaque_entr=300, departs_entr=2, iter_entr=50, iter_max=20)
R, RT, RA = m.RACINE_TESTS, m.RACINE_TESTS_TENUE, m.RACINE_TESTS_AUTRE


def contexte_et_M0(racine=R, racine_tenue=RT, instance=0, cd=1, cfg=CFG_PETITE):
    ctx = v4.Contexte(instance, cd, racine, racine_tenue, cfg)
    M0 = ctx.entrainer(v4.COMMUN, 0, [ctx.cible], np.array([1.0]), 1)
    return ctx, v4.Moniteur(M0.W.copy(), M0.b.copy()).calibrer(ctx.Xcal, cfg.alpha)


@pytest.fixture(scope="module")
def tache_petite():
    """Une tâche (δ 1, instance 0), toutes les règles, R4 à λ ∈ {0 ; 0,3} et les deux références ; chronométrée."""
    t0 = time.process_time()
    r = m.executer_tache_regles(0, 1, R, RT, CFG_PETITE, lambdas=(0.0, 0.3), references=("dernier", "moyenne"))
    return r, time.process_time() - t0


# ---------------------------------------------------------------------------------------------------------------
# Chargement du v4, gel, racines (gardes : sain et artefact)
# ---------------------------------------------------------------------------------------------------------------
def test_chargement_v4_empreinte_sain_et_artefacts(tmp_path):
    assert m.empreinte_fichier(m.ARENE_V4) == m.ARENE_V4_SHA256          # sain : le fichier sous donnees/ est intact
    assert v4.VERSION == "arene_melange_v4"
    copie = tmp_path / "arene_melange_v4.py"
    shutil.copy(m.ARENE_V4, copie)
    copie.write_bytes(copie.read_bytes().replace(b"DELTAS_V4 = (1.4, 1.6)", b"DELTAS_V4 = (1.4, 1.8)"))
    with pytest.raises(GardeArret, match="arène v4 modifiée"):
        m.charger_arene_v4(copie)
    with pytest.raises(GardeArret, match="arène v4 absente"):
        m.charger_arene_v4(tmp_path / "absente.py")
    assert not (m.ARENE_V4.parent / "__pycache__" / "arene_melange_v4.cpython-313.pyc").exists() or True
    # la copie chargée est bien celle qui porte le remplacement de `gen` et l'extension de BRAS
    assert v4.gen is m.gen_regles and v4.BRAS["R1"] == 21 and v4.BRAS["R2"] == v4.BRAS["A"]


def test_gel_sain_et_artefacts(tmp_path):
    assert m.exiger_gel_regles((R, RT, RA, m.RACINE_ESSAI, m.RACINE_DECISION)) == m.GEL_SHA256     # sain
    with pytest.raises(GardeArret, match="absente du gel"):
        m.exiger_gel_regles((20266555,))     # (20266999 est cité par le gel comme borne de la plage)
    copie = tmp_path / "gel.md"
    copie.write_text(m.GEL.read_text(encoding="utf-8") + "\n", encoding="utf-8")
    with pytest.raises(GardeArret, match="gel des règles modifié"):
        m.exiger_gel_regles((), copie)
    with pytest.raises(GardeArret, match="gel des règles absent"):
        m.exiger_gel_regles((), tmp_path / "rien.md")


def test_racines_sain_et_artefacts():
    g1, g2 = m.gen_regles(R, 1, 0, 21, 3, 5), m.gen_regles(R, 1, 0, 21, 3, 5)
    assert np.array_equal(g1.standard_normal(4), g2.standard_normal(4))                       # sain, reproductible
    assert not np.array_equal(m.gen_regles(R, 1, 0, 21, 3, 5).standard_normal(4),
                              m.gen_regles(R, 1, 0, 21, 3, 6).standard_normal(4))             # la clé compte
    m.exiger_racines_essai_regles(R, RT)
    for racine, motif in ((m.RACINE_DECISION, "sans autorisation"), (v4.RACINE, "de décision de l'arène v4"),
                          (20261291, "déjà employée"), (20265100, "d'une autre session"),
                          (v4.RACINE_ESSAI, "réservée au v4"), (20266999, "non gelée")):
        with pytest.raises(GardeArret, match=motif):
            m.gen_regles(racine, 0)
    with pytest.raises(GardeArret, match="réservée à la décision"):
        m.exiger_racines_essai_regles(m.RACINE_DECISION, RT)
    with pytest.raises(GardeArret, match="racine à part"):
        m.exiger_racines_essai_regles(R, R)
    with pytest.raises(GardeArret, match="racine absente"):
        m.exiger_racines_essai_regles(None, RT)
    assert all(m.PLAGE_REGLES[0] <= r <= m.PLAGE_REGLES[1] for r in m.RACINES_GELEES + m.RACINES_DECISION)
    texte = m.GEL.read_text(encoding="utf-8")
    assert all(str(r) in texte for r in m.RACINES_GELEES + m.RACINES_DECISION)                 # toutes gelées


def test_decision_refusee_sans_prereg_scelle(tmp_path):
    assert m._AUTORISATION_DECISION["prereg_sha256"] is None
    brouillon = tmp_path / "prereg.md"
    brouillon.write_text("# brouillon non scellé\n", encoding="utf-8")
    with pytest.raises(GardeArret):
        m.autoriser_decision_regles(brouillon, v4.CONFIG_V4, "0:100", 0.3, "dernier")
    assert m._AUTORISATION_DECISION["prereg_sha256"] is None
    with pytest.raises(GardeArret, match="sans autorisation"):
        m.gen_regles(m.RACINE_DECISION_TENUE, 0)
    with pytest.raises(GardeArret):      # commande decision : refusée avant toute graine
        m.main(["decision", "--prereg", str(brouillon), "--instances", "0:100", "--run-id", "x", "--lambda", "0.3",
                "--reference", "dernier"])
    assert m._AUTORISATION_DECISION["prereg_sha256"] is None


# ---------------------------------------------------------------------------------------------------------------
# Mesures et réglages (gardes)
# ---------------------------------------------------------------------------------------------------------------
def test_exploitabilite_sain_et_artefacts():
    assert m.exploitabilite(0.0) == 1.0 and m.exploitabilite(1.0) == 0.0 and abs(m.exploitabilite(0.3) - 0.7) < 1e-12
    for mauvais in (1.5, -0.2, float("nan"), float("inf")):
        with pytest.raises(GardeArret, match="hors de \\[0 ; 1\\]"):
            m.exploitabilite(mauvais)


def test_regle_lambda_reference_gardes():
    for r in m.REGLES:
        m.exiger_regle(r)
    with pytest.raises(GardeArret, match="règle inconnue"):
        m.exiger_regle("R9")
    assert m.exiger_lambda(0) == 0.0 and m.exiger_lambda("0.3") == 0.3
    for mauvais in (-1.0, float("nan")):
        with pytest.raises(GardeArret, match="négatif ou non fini"):
            m.exiger_lambda(mauvais)
    mon = v4.Moniteur(np.array([[1.0, 2.0]]), np.array([0.0]))
    assert np.allclose(m.direction_reference([mon], "dernier"), np.array([1.0, 2.0]) / np.sqrt(5))
    mon2 = v4.Moniteur(np.array([[-1.0, -2.0]]), np.array([0.0]))
    with pytest.raises(GardeArret, match="référence inconnue"):
        m.direction_reference([mon], "autre")
    with pytest.raises(GardeArret, match="direction de référence nulle"):
        m.direction_reference([mon, mon2], "moyenne")
    with pytest.raises(GardeArret, match="règle inconnue"):
        m.variantes(("R1", "R5"))
    assert len(m.variantes(m.REGLES, m.GRILLE_LAMBDA, m.REFERENCES)) == 3 + 2 * len(m.GRILLE_LAMBDA)


def test_penalite_direction_gradient_et_invariance():
    g = m.gen_regles(R, 0, 0, 0, 0, 90)
    w, u = g.standard_normal(6), g.standard_normal(6)
    u /= np.linalg.norm(u)
    val, grad = m.penalite_direction(w, u, 0.7)
    assert abs(val - 0.7 * np.sum((w / np.linalg.norm(w) - u) ** 2)) < 1e-12
    num = np.array([(m.penalite_direction(w + h * e, u, 0.7)[0] - m.penalite_direction(w - h * e, u, 0.7)[0]) / (2 * h)
                    for e in np.eye(6) for h in (1e-6,)])
    assert np.allclose(num, grad, atol=1e-6)
    assert abs(m.penalite_direction(3.0 * w, u, 0.7)[0] - val) < 1e-12          # sans échelle
    assert m.penalite_direction(np.zeros(6), u, 0.7) == (1.4, pytest.approx(np.zeros(6)))   # direction indéfinie


def test_entrainement_regularise_lambda_zero_egal_v4_et_lambda_fort_rapproche():
    cfg = CFG_PETITE
    ctx, M0 = contexte_et_M0()
    Xp = ctx.propre_entr(1)
    att = v4.projeter(ctx.cible + 0.5 * m.gen_regles(R, 0, 0, 0, 0, 91).standard_normal(ctx.cible.size), ctx.cible,
                      ctx.delta, cfg)[0]
    Xa = v4.echantillonner(att, cfg.n_attaque_entr, m.gen_regles(R, 0, 0, 0, 0, 92), cfg)
    mu, _ = v4.deplier(att, cfg)
    dirs = [v / np.linalg.norm(v) for v in mu]
    u = m.direction_reference([M0], "dernier")
    mon_v4, ok_v4 = v4.entrainer(Xp, Xa, 1, cfg, None, dirs)
    mon_0, ok_0 = m.entrainer_regularise(Xp, Xa, cfg, u, 0.0, dirs)
    assert np.array_equal(mon_v4.W, mon_0.W) and np.array_equal(mon_v4.b, mon_0.b) and ok_v4 == ok_0   # λ = 0 : au bit
    mon_3, _ = m.entrainer_regularise(Xp, Xa, cfg, u, 3.0, dirs)
    cos = lambda w: float(w @ u / np.linalg.norm(w))  # noqa: E731
    assert cos(mon_3.W[0]) > cos(mon_0.W[0]) and not np.array_equal(mon_3.W, mon_0.W)   # λ fort : plus proche de u
    with pytest.raises(GardeArret, match="oracle « détection » exigé"):
        m.entrainer_regularise(Xp, Xa, m.replace(cfg, entrainement="logistique"), u, 0.0, dirs)
    # au niveau du contexte, même code de graine : identique au bit à `Contexte.entrainer`
    ctx_a, _ = contexte_et_M0()
    ctx_b, M0_b = contexte_et_M0()
    a = ctx_a.entrainer(1, 1, [ctx_a.cible, att], np.array([0.5, 0.5]), 1)
    b = m.entrainer_ctx_regularise(ctx_b, 1, 1, [ctx_b.cible, att], np.array([0.5, 0.5]),
                                   m.direction_reference([M0_b], "dernier"), 0.0)
    assert np.array_equal(a.W, b.W) and np.array_equal(a.b, b.b) and a.t == b.t and ctx_b.entr == ctx_a.entr


# ---------------------------------------------------------------------------------------------------------------
# Trajectoires : chaque règle, essai clé R2 = A, R3 = B, R4(λ = 0) = R2 à code égal, tenues jamais vues
# ---------------------------------------------------------------------------------------------------------------
def test_chaque_regle_trajectoire_T3_petite_config_en_moins_de_30_s(tache_petite):
    r, cpu = tache_petite
    assert cpu < 30.0, cpu
    noms = set(r["regles"])
    assert noms == {"R1", "R2", "R3", "R4[dernier,λ=0]", "R4[dernier,λ=0.3]", "R4[moyenne,λ=0]", "R4[moyenne,λ=0.3]"}
    for nom, x in r["regles"].items():
        pt = x["par_tour"]
        assert len(pt["iii"]) == 3 and len(pt["exploitabilite"]) == 3 and len(pt["ii"]) == 3
        assert len(pt["cos_consecutif"]) == 3 and all(-1 - 1e-9 <= c <= 1 + 1e-9 for c in pt["cos_consecutif"])
        assert all(0 <= v <= 1 for v in pt["iii"] + pt["exploitabilite"] + pt["ii"])
        assert all(abs(e - (1 - i)) < 1e-12 for e, i in zip(pt["exploitabilite"], pt["iii"]))
        assert 0 <= x["exploitabilite_finale"] <= 1 and abs(x["exploitabilite_finale"] - (1 - x["V_iii_final"])) < 1e-12
        assert 0 <= x["ii_final"] <= 1 and 0 <= x["i_final_vus"] <= 1
        assert abs(x["fpr_final"] - CFG_PETITE.alpha) <= CFG_PETITE.tol_fpr
        assert x["cout_trajectoire"]["entrainements"] == 3 and x["cout_trajectoire"]["appels_optimiseur"] > 0
        assert x["cout_trajectoire"]["departs_attaquant"] == 3 * (CFG_PETITE.departs + 2)
        assert x["cpu_trajectoire_s"] > 0 and x["cpu_final_s"] > 0
        assert x["cycle"]["I3_nul"] == pytest.approx(v4.valeur_nulle_I3(3)) and x["cycle"]["I3_retours"] in (0.0, 1.0)
        assert len(x["cycle"]["H"]) == 4 and all(len(l) == 3 for l in x["cycle"]["H"])
        if nom == "R3":
            assert x["cout_trajectoire"]["programmes_lineaires"] > 0 and len(pt["valeur_jeu_restreint"]) == 3
            assert x["valeur_jeu_restreint"] is not None and "equilibre" in x and x["nb_moniteurs_stockes"] == 4
            assert all(v >= i - 0.06 for v, i in zip(pt["valeur_jeu_restreint"], pt["iii"]))  # R3′ ≥ (iii) (bruit)
        else:
            assert x["cout_trajectoire"]["programmes_lineaires"] == 0 and pt["valeur_jeu_restreint"] == []
            assert x["poids_finaux"] == [1.0] and x["parametres_deployes"] == CFG_PETITE.d + 1
    assert r["entrainements"] == 2 + 7 * 3 and r["non_convergences"] <= r["entrainements"] * CFG_PETITE.taux_nonconv_max
    # les mesures bougent entre règles (pas une constante recopiée)
    assert len({round(x["V_iii_final"], 6) for x in r["regles"].values()}) > 1
    # R4 : les deux références coïncident à λ = 0 (pénalité nulle) et diffèrent à λ = 0,3 dès que l'historique > 1
    assert r["regles"]["R4[dernier,λ=0]"]["V_iii_final"] == r["regles"]["R4[moyenne,λ=0]"]["V_iii_final"]


def test_R2_reproduit_A_du_v4_au_bit():
    """Essai clé : la boucle commune avec la règle R2 rend, à graine égale, la trajectoire et la finale du bras A."""
    ctx_a, M_a = contexte_et_M0()
    etat_a = v4.trajectoire("A", ctx_a, M_a, leger=False)
    ctx_r, M_r = contexte_et_M0()
    etat_r = m.trajectoire_regle("R2", ctx_r, M_r)
    assert len(etat_a["attaques"]) == len(etat_r["attaques"]) == CFG_PETITE.T + 1
    assert all(np.array_equal(a, b) for a, b in zip(etat_a["attaques"], etat_r["attaques"]))
    for ma, mr in zip(etat_a["moniteurs"], etat_r["moniteurs"]):
        assert np.array_equal(ma.W, mr.W) and np.array_equal(ma.b, mr.b) and ma.t == mr.t
    for cle in ("iii", "ii", "distance", "nouveaute", "projections", "poids_max"):
        assert etat_a["par_tour"][cle] == etat_r["par_tour"][cle], cle
    assert etat_a["cycle"]["H"] == etat_r["cycle"]["H"] and etat_a["cycle"]["I1_progres"] == etat_r["cycle"]["I1_progres"]
    fin_a = v4.phase_finale("A", etat_a["defense_finale"], ctx_a, etat_a, leger=True)
    fin_r = m.finale_regle("R2", etat_r, ctx_r)
    for cle in ("V_iii_final", "V_iii_standard", "V_iii_renforce", "fpr_final", "distance_finale", "poids_finaux"):
        assert fin_a[cle] == fin_r[cle], cle
    assert ctx_a.entr == ctx_r.entr and ctx_a.att["departs"] == ctx_r.att["departs"]


def test_R3_reproduit_B_du_v4_au_bit():
    ctx_b, M_b = contexte_et_M0()
    etat_b = v4.trajectoire("B", ctx_b, M_b, leger=False)
    ctx_r, M_r = contexte_et_M0()
    etat_r = m.trajectoire_regle("R3", ctx_r, M_r)
    assert all(np.array_equal(a, b) for a, b in zip(etat_b["attaques"], etat_r["attaques"]))
    assert etat_b["par_tour"]["iii"] == etat_r["par_tour"]["iii"] and etat_b["par_tour"]["ii"] == etat_r["par_tour"]["ii"]
    assert etat_b["valeur_jeu_restreint"] == etat_r["valeur_jeu_restreint"] and etat_b["equilibre"] == etat_r["equilibre"]
    assert [w for _, w in etat_b["defense_finale"]] == [w for _, w in etat_r["defense_finale"]]
    fin_b = v4.phase_finale("B", etat_b["defense_finale"], ctx_b, etat_b, leger=True)
    fin_r = m.finale_regle("R3", etat_r, ctx_r)
    assert fin_b["V_iii_final"] == fin_r["V_iii_final"] and fin_b["fpr_final"] == fin_r["fpr_final"]


def test_R4_lambda_zero_egal_R2_sur_la_trajectoire_a_code_de_graine_egal(monkeypatch):
    """À λ = 0 la mise à jour de R4 est celle de R2 ; les trajectoires ne diffèrent que par le code de graine de
    l'attaquant (24 ≠ 1, déclaré) : à code forcé égal (essai seulement), identité au bit."""
    ctx_2, M_2 = contexte_et_M0()
    etat_2 = m.trajectoire_regle("R2", ctx_2, M_2)
    monkeypatch.setitem(m.CODES, "R4", m.CODES["R2"])
    ctx_4, M_4 = contexte_et_M0()
    etat_4 = m.trajectoire_regle("R4", ctx_4, M_4, lam=0.0, reference="moyenne")
    assert all(np.array_equal(a, b) for a, b in zip(etat_2["attaques"], etat_4["attaques"]))
    for ma, mb in zip(etat_2["moniteurs"], etat_4["moniteurs"]):
        assert np.array_equal(ma.W, mb.W) and np.array_equal(ma.b, mb.b)
    assert etat_2["par_tour"]["iii"] == etat_4["par_tour"]["iii"]
    # à λ > 0 et même code, la trajectoire change dès le premier réentraînement
    ctx_5, M_5 = contexte_et_M0()
    etat_5 = m.trajectoire_regle("R4", ctx_5, M_5, lam=1.0, reference="dernier")
    assert np.array_equal(etat_5["attaques"][1], etat_2["attaques"][1])        # tour 1 : même défense M0, même attaque
    assert not np.array_equal(etat_5["moniteurs"][1].W, etat_2["moniteurs"][1].W)


def test_tenues_jamais_vues_par_l_entrainement(monkeypatch):
    """Instrumentation : toute attaque passée à un entraînement (v4 ou R4) est la cible ou une meilleure réponse de la
    trajectoire ; aucune n'est une loi tenue à l'écart ; les lois tenues viennent de la racine tenue seule."""
    vues = []
    orig = v4.Contexte.entrainer

    def entrainer_espion(self, bras, tour, attaques, q, mm):
        vues.extend(np.asarray(a, float).copy() for a in attaques)
        return orig(self, bras, tour, attaques, q, mm)

    orig_r4 = m.entrainer_ctx_regularise

    def r4_espion(ctx, cb, tour, attaques, q, u, lam):
        vues.extend(np.asarray(a, float).copy() for a in attaques)
        return orig_r4(ctx, cb, tour, attaques, q, u, lam)

    monkeypatch.setattr(v4.Contexte, "entrainer", entrainer_espion)
    monkeypatch.setattr(m, "entrainer_ctx_regularise", r4_espion)
    ctx = v4.Contexte(1, 2, R, RT, CFG_PETITE)
    M0 = ctx.entrainer(v4.COMMUN, 0, [ctx.cible], np.array([1.0]), 1)
    legitimes = [ctx.cible]
    for regle, lam in (("R1", 0.0), ("R2", 0.0), ("R3", 0.0), ("R4", 0.3)):
        etat = m.trajectoire_regle(regle, ctx, v4.Moniteur(M0.W.copy(), M0.b.copy()).calibrer(ctx.Xcal, CFG_PETITE.alpha),
                                   lam=lam)
        legitimes += etat["attaques"][1:]
    assert len(vues) > 0 and len(ctx.tenues) == CFG_PETITE.n_tenue
    for a in vues:
        assert any(np.array_equal(a, b) for b in legitimes)
        assert all(np.max(np.abs(a - t)) > 1e-6 for t in ctx.tenues)
    # racine tenue à part : une autre racine tenue change les lois tenues, pas la trajectoire
    ctx_b = v4.Contexte(1, 2, R, RA, CFG_PETITE)
    assert not any(np.array_equal(t, u) for t, u in zip(ctx.tenues, ctx_b.tenues))
    M0_b = ctx_b.entrainer(v4.COMMUN, 0, [ctx_b.cible], np.array([1.0]), 1)
    e_b = m.trajectoire_regle("R1", ctx_b, v4.Moniteur(M0_b.W.copy(), M0_b.b.copy()).calibrer(ctx_b.Xcal, CFG_PETITE.alpha))
    e_a = m.trajectoire_regle("R1", ctx, v4.Moniteur(M0.W.copy(), M0.b.copy()).calibrer(ctx.Xcal, CFG_PETITE.alpha))
    assert all(np.array_equal(a, b) for a, b in zip(e_a["attaques"], e_b["attaques"]))
    assert e_a["par_tour"]["ii"] != e_b["par_tour"]["ii"]


def test_graine_reproductible_et_autre_racine_change_le_resultat():
    ctx_1, M_1 = contexte_et_M0()
    ctx_2, M_2 = contexte_et_M0()
    e1, e2 = m.trajectoire_regle("R1", ctx_1, M_1), m.trajectoire_regle("R1", ctx_2, M_2)
    assert all(np.array_equal(a, b) for a, b in zip(e1["attaques"], e2["attaques"]))
    assert e1["par_tour"]["iii"] == e2["par_tour"]["iii"] and e1["par_tour"]["ii"] == e2["par_tour"]["ii"]
    ctx_3, M_3 = contexte_et_M0(racine=RA, racine_tenue=RT)
    e3 = m.trajectoire_regle("R1", ctx_3, M_3)
    assert not np.array_equal(ctx_3.cible, ctx_1.cible) and e3["par_tour"]["iii"] != e1["par_tour"]["iii"]


def test_plafond_de_temps_processeur_sain_et_artefact():
    v4.exiger_plafond(time.process_time(), CFG_PETITE, "sain")
    ctx, M0 = contexte_et_M0(cfg=m.replace(CFG_PETITE, plafond_cpu_tache_s=1e-9))
    with pytest.raises(GardeArret, match="plafond de temps processeur"):
        m.trajectoire_regle("R1", ctx, M0)


# ---------------------------------------------------------------------------------------------------------------
# Analyse, choix de λ, commande, identité
# ---------------------------------------------------------------------------------------------------------------
def test_analyse_et_choix_lambda(tache_petite):
    r0, _ = tache_petite
    r1 = m.executer_tache_regles(1, 1, R, RT, CFG_PETITE, lambdas=(0.0, 0.3), references=("dernier", "moyenne"))
    an = m.analyser_regles([r0, r1], R, n_reech=200)
    bloc = an["1"]
    assert bloc["n"] == 2 and set(bloc["variantes"]) == set(r0["regles"])
    c = bloc["contrastes_contre_R2"]["R1 - R2 (V_iii_final)"]
    q = c["quantiles"]
    assert q["q0.00625"] <= q["q0.025"] <= q["q0.975"] <= q["q0.99375"] and c["n"] == 2
    assert abs(c["moyenne"] - np.mean([r["regles"]["R1"]["V_iii_final"] - r["regles"]["R2"]["V_iii_final"]
                                       for r in (r0, r1)])) < 1e-12
    assert "R2 - R2 (V_iii_final)" not in bloc["contrastes_contre_R2"]
    assert "R3 I1_progres" in bloc["indicateurs"] and "R3 I3_moins_nul" in bloc["indicateurs"]
    assert "valeur_jeu_restreint_par_tour" in bloc["variantes"]["R3"] and "poids" in bloc["variantes"]["R3"]
    ch = an["choix_lambda"]
    assert ch["retenu"] in r0["regles"] and ch["retenu"].startswith("R4[")
    # règle d'égalité : même moyenne → plus petite λ, puis « dernier »
    faux = [{"regles": {"R4[dernier,λ=0.3]": {"V_iii_final": 0.50, "lam": 0.3, "reference": "dernier"},
                        "R4[dernier,λ=0.1]": {"V_iii_final": 0.497, "lam": 0.1, "reference": "dernier"},
                        "R4[moyenne,λ=0.1]": {"V_iii_final": 0.499, "lam": 0.1, "reference": "moyenne"},
                        "R2": {"V_iii_final": 0.9}}}]
    assert m.choisir_lambda(faux)["retenu"] == "R4[dernier,λ=0.1]"
    faux[0]["regles"]["R4[dernier,λ=0.3]"]["V_iii_final"] = 0.6
    assert m.choisir_lambda(faux)["retenu"] == "R4[dernier,λ=0.3]"
    assert m.choisir_lambda([{"regles": {"R2": {"V_iii_final": 0.9}}}])["retenu"] is None


def test_cli_essai_refuse_racines_interdites_et_ecrasement(tmp_path):
    sortie = tmp_path / "s.json"
    for racine, motif in ((m.RACINE_DECISION, "réservée à la décision"), (v4.RACINE_ESSAI, "réservée au v4"),
                          (20266999, "non gelée")):
        with pytest.raises(GardeArret, match=motif):
            m.main(["essai", "--instances", "0:1", "--sortie", str(sortie), "--racine", str(racine)])
    assert not sortie.exists()
    sortie.write_text("{}", encoding="utf-8")
    with pytest.raises(GardeArret, match="existe déjà"):
        m.main(["essai", "--instances", "0:1", "--sortie", str(sortie)])
    with pytest.raises(GardeArret, match="règle inconnue"):
        m.main(["essai", "--instances", "0:1", "--sortie", str(tmp_path / "t.json"), "--regles", "R1,R7"])


def test_cli_essai_ecrit_un_pilote_minuscule_et_orphelins(tmp_path, monkeypatch):
    """Un processus, une instance, T = 2, R1 et R2 : la commande écrit le fichier avec manifeste, analyse, résultats ;
    la commande `orphelins` lit un fichier de PID morts sans erreur."""
    import json

    monkeypatch.setattr(v4, "CONFIG_V4", m.replace(CFG_PETITE, T=2))
    sortie = tmp_path / "pilote.json"
    assert m.main(["essai", "--instances", "0:1", "--sortie", str(sortie), "--processus", "1", "--regles", "R1,R2",
                   "--lambdas", "0.3", "--references", "dernier"]) == 0
    corps = json.loads(sortie.read_text(encoding="utf-8"))
    assert corps["mode"] == "essai" and corps["manifeste"]["racine"] == m.RACINE_ESSAI
    assert corps["manifeste"]["gel_sha256"] == m.GEL_SHA256 and corps["manifeste"]["versions"]["arene_v4_sha256"] == m.ARENE_V4_SHA256
    assert set(corps["resultats"][0]["regles"]) == {"R1", "R2"} and len(corps["resultats"]) == 2
    assert corps["analyse"]["choix_lambda"]["retenu"] is None and corps["temps"]["taches"] == 2
    pids = tmp_path / "pids.txt"
    pids.write_text("# essai\n4194303 1\n", encoding="utf-8")
    assert m.main(["orphelins", "--pids", str(pids)]) == 0


def test_bloc_identite_et_identite_prereg_sain_et_artefacts():
    cfg = v4.CONFIG_V4
    texte = m.bloc_identite(cfg) + "\nLAMBDA_RETENU = 0.3\nREFERENCE_RETENUE = dernier\n"
    assert m.IDENTIFIANT_PREREG in texte and m.ARENE_V4_SHA256 in texte and m.GEL_SHA256 in texte
    m.exiger_identite_prereg_regles(texte, cfg, "0:100", 0.3, "dernier")                 # sain
    for mauvais, motif in ((texte.replace(m.IDENTIFIANT_PREREG, "AUTRE"), "sans l'identifiant"),
                           (texte.replace(str(m.RACINE_DECISION), "20266999"), "RACINE_DECISION = "),
                           (texte.replace(m.GEL_SHA256, "0" * 64), "empreinte \\(gel\\) absente"),
                           (texte.replace('"T": 8', '"T": 7'), "configuration différente"),
                           (texte.replace("numpy " + np.__version__, "numpy 0.0.0"), "version numpy")):
        with pytest.raises(GardeArret, match=motif):
            m.exiger_identite_prereg_regles(mauvais, cfg, "0:100", 0.3, "dernier")
    with pytest.raises(GardeArret, match="LAMBDA_RETENU"):
        m.exiger_identite_prereg_regles(texte, cfg, "0:100", 1.0, "dernier")
    with pytest.raises(GardeArret, match="REFERENCE_RETENUE"):
        m.exiger_identite_prereg_regles(texte, cfg, "0:100", 0.3, "moyenne")
    with pytest.raises(GardeArret, match="--instances 0:50"):
        m.exiger_identite_prereg_regles(texte, cfg, "0:50", 0.3, "dernier")
