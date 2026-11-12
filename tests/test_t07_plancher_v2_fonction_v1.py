"""Essais de `src/controle_ia/t07/plancher_v2.py` (remède (a) de T0.7, règle « au-dessus du plancher » par différence appariée) —
v1, fichier neuf (consigne `consigne-code-plancher-v2-t07-v1.md`, `4efbdbf4…`, mandat, points 1 et 4).

- aires des tirages **égales au bit près** à `sondes.evaluation.aire_sous_courbe` sur les actions tirées (ex aequo, effectifs
  inégaux par tâche, tâches nommées par des chaînes) ; matrices de comparaisons égales au comptage direct de toutes les paires ;
- tirages **égaux à ceux d'`intervalle_blocs`** sous la même graine (nombre de blocs impair compris) ; aire, intervalle propre,
  quantile et plancher égaux à `plancher_v1.comparer_scores_au_plancher` ;
- R5 : chaque garde sur un cas sain et sur un artefact (tirages dégénérés, entrées, cohérence au paquet gelé, cohérence des
  tirages, borne perdue à l'addition) ; cas sain (sonde séparée : « au-dessus ») et artefact (sonde = une direction du
  plancher : « non au-dessus ») ;
- **reproduction du prototype** (`remede_a_prototype_v1.py`, `3e488d70…`) sur ses mondes de référence : mêmes tirages injectés,
  mêmes matrices, **même borne basse au bit près** et **même décision** (par `criteres_v1.etat_pour_sonde`) pour chaque sonde.
"""
from __future__ import annotations

import hashlib
import importlib.util
import subprocess
from pathlib import Path

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.sondes.evaluation import aire_sous_courbe, intervalle_blocs
from controle_ia.t07 import criteres_v1 as cr
from controle_ia.t07 import plancher_v1 as pl
from controle_ia.t07 import plancher_v2 as pl2

RACINE_DEPOT = Path(__file__).resolve().parents[1]
NIVEAU_DECISIF = 1 - 0.05 / 4
COMMIT_PIECES = "fecbbcfeaa3d319dc50fdd16e2c7186078db709d"
DOSSIER_PIECES = "docs/notes/g0-deux-semaines-v1/t07-module-v2/erreur-premiere-espece-t07-v1"
SHA_PROTOTYPE = "3e488d7036fe48ed7a291a728c1822d6f7a9698e0696ce2e376465dea757bb2c"
SHA_SCRIPT_V1 = "59453773ee08e06aa1abef3d7777935f19150ac84241ac6528639f7fc1c69970"


# ----------------------------------------------------------------------------------------------------------------- outils
def jeu(seed: int = 3, n: int = 12, inegaux: bool = False, ex_aequo: bool = False, signal: float = 0.0, k: int = 30,
        noms: bool = False):
    """Jeu synthétique : n tâches, actions positives et négatives par tâche (10 et 10, ou effectifs tirés de 3 à 12), une sonde
    (signal sur y) et k directions de plancher (bruit seul)."""
    rng = np.random.default_rng(seed)
    y, blocs = [], []
    for t in range(n):
        n1, n0 = (int(rng.integers(3, 13)), int(rng.integers(3, 13))) if inegaux else (10, 10)
        y += [1] * n1 + [0] * n0
        blocs += [t] * (n1 + n0)
    y, blocs = np.array(y, dtype=np.int64), np.array(blocs)
    if noms:
        blocs = np.array([f"t{b:03d}" for b in blocs])
    s = signal * y + rng.standard_normal(y.size)
    P = rng.standard_normal((k, y.size))
    if ex_aequo:
        s, P = np.round(s, 0), np.round(P, 0)
    return s, P, y, blocs


def paires(scores, y, blocs):
    """C[t, u] par comparaison de toutes les paires (voie directe, sans tri)."""
    uniques = np.unique(blocs)
    C = np.zeros((uniques.size, uniques.size))
    for a, t in enumerate(uniques):
        p = scores[(blocs == t) & (y == 1)]
        for b, u in enumerate(uniques):
            q = scores[(blocs == u) & (y == 0)]
            C[a, b] = (p[:, None] > q[None, :]).sum() + 0.5 * (p[:, None] == q[None, :]).sum()
    return C


def choix_intervalle_blocs(n_blocs: int, n_tirages: int, graine: int) -> list:
    """Les tirages d'`intervalle_blocs` (l. 50-53 du paquet gelé), rejoués."""
    rng = np.random.default_rng(int(graine))
    return [rng.integers(0, n_blocs, size=n_blocs) for _ in range(n_tirages)]


# --------------------------------------------------------------------------------------------- égalités au paquet gelé
@pytest.mark.parametrize("inegaux,ex_aequo,noms", [(False, False, False), (True, True, True), (True, False, False)])
def test_aires_des_tirages_egales_au_bit_a_aire_sous_courbe(inegaux, ex_aequo, noms):
    s, P, y, blocs = jeu(inegaux=inegaux, ex_aequo=ex_aequo, noms=noms)
    X = np.vstack([s[None, :], P])
    comp = pl2.comparaisons_par_taches(X, y, blocs)
    for j in (0, 1, X.shape[0] - 1):
        assert np.array_equal(comp["C"][j], paires(X[j], y, blocs))
    uniques = np.unique(blocs)
    membres = [np.flatnonzero(blocs == u) for u in uniques]
    W = pl2.poids_des_tirages(uniques.size, 40, 11)
    choix = choix_intervalle_blocs(uniques.size, 40, 11)
    vus = 0
    for b in range(40):
        assert np.array_equal(W[b], np.bincount(choix[b], minlength=uniques.size))
        i = np.concatenate([membres[c] for c in choix[b]])
        if len(set(y[i].tolist())) < 2:
            continue
        A = pl2.aires_tirees(comp["C"], W[b:b + 1], comp["n1"], comp["n0"])[:, 0]
        for j in range(X.shape[0]):
            assert A[j] == aire_sous_courbe(X[j][i], y[i])          # au bit près
        vus += 1
    assert vus >= 35
    un = pl2.aires_tirees(comp["C"], np.ones((1, uniques.size)), comp["n1"], comp["n0"])[:, 0]
    assert all(un[j] == aire_sous_courbe(X[j], y) for j in range(X.shape[0]))


@pytest.mark.parametrize("n,inegaux", [(12, False), (7, True), (9, True)])
def test_memes_tirages_et_memes_ponctuels_que_plancher_v1(n, inegaux):
    """Aire, intervalle propre de la sonde, quantile, plancher, dégénérés : égaux à `comparer_scores_au_plancher` ; tirages
    d'`intervalle_blocs` (nombre de blocs impair compris)."""
    s, P, y, blocs = jeu(seed=n, n=n, inegaux=inegaux, signal=0.4)
    r1 = pl.comparer_scores_au_plancher(s, P, y, blocs, 300, 99, 0.95, NIVEAU_DECISIF)
    r2 = pl2.comparer_difference_au_plancher(s, P, y, blocs, 300, 99, 0.95, NIVEAU_DECISIF)
    for k in ("aire", "bas", "haut", "plancher_quantile", "plancher_mediane", "n_plancher", "degeneres", "tirages", "niveau",
              "plancher", "effectifs"):
        assert r2[k] == r1[k], k
    d = r2["difference"]
    assert d["methode"] == pl2.METHODE == "difference_appariee_percentile"
    assert d["estimation"] == r1["aire"] - r1["plancher_quantile"]
    assert d["bas"] <= d["haut"] and d["tirages"] == r1["tirages"] and d["degeneres"] == r1["degeneres"]
    assert r2["au_dessus_du_plancher"] is (d["bas"] > 0.0)


def test_difference_rejouee_a_la_main_sur_les_tirages_d_intervalle_blocs():
    """D* recalculée tirage par tirage par `aire_sous_courbe` (paquet gelé) sur les actions tirées, quantile du plancher par
    `np.quantile` : mêmes bornes au bit près que la fonction."""
    s, P, y, blocs = jeu(seed=5, n=10, inegaux=True, ex_aequo=True, signal=0.5, k=20)
    uniques = np.unique(blocs)
    membres = [np.flatnonzero(blocs == u) for u in uniques]
    D = []
    for c in choix_intervalle_blocs(uniques.size, 200, 4):
        i = np.concatenate([membres[x] for x in c])
        if len(set(y[i].tolist())) < 2:
            continue
        D.append(aire_sous_courbe(s[i], y[i]) - np.quantile([aire_sous_courbe(P[k][i], y[i]) for k in range(P.shape[0])], 0.95))
    r = pl2.comparer_difference_au_plancher(s, P, y, blocs, 200, 4, 0.95, 0.95)
    a = (1.0 - 0.95) / 2.0                                # comme `intervalle_blocs` (et non 0,025 écrit à la main)
    assert r["difference"]["bas"] == float(np.quantile(D, a)) and r["difference"]["haut"] == float(np.quantile(D, 1.0 - a))


# --------------------------------------------------------------------------------------------- cas sain et artefact (R5)
def test_cas_sain_sonde_separee_au_dessus():
    s, P, y, blocs = jeu(seed=21, n=30, signal=1.5, k=200)
    r = pl2.comparer_difference_au_plancher(s, P, y, blocs, 500, 8, 0.95, NIVEAU_DECISIF)
    assert r["au_dessus_du_plancher"] is True and r["difference"]["bas"] > 0.0
    e = cr.etat_pour_sonde({**pl2.resume_pour_critere(r), "triviaux": {}})
    assert e == cr.AU_DESSUS


@pytest.mark.parametrize("rang", [100, 190])
def test_artefact_sonde_egale_a_une_direction_du_plancher_non_au_dessus(rang):
    """La sonde est une des directions du plancher (au milieu, puis au quantile 0,95 des aires) : « non au-dessus »."""
    _, P, y, blocs = jeu(seed=22, n=30, k=200)
    aires = np.array([aire_sous_courbe(P[k], y) for k in range(P.shape[0])])
    s = P[np.argsort(aires, kind="stable")[rang]].copy()
    r = pl2.comparer_difference_au_plancher(s, P, y, blocs, 500, 8, 0.95, NIVEAU_DECISIF)
    assert r["au_dessus_du_plancher"] is False and r["difference"]["bas"] <= 0.0
    assert cr.etat_pour_sonde({**pl2.resume_pour_critere(r), "triviaux": {}}) == cr.NON_AU_DESSUS


def test_artefact_sonde_identique_a_un_plancher_constant_difference_nulle():
    """Toutes les directions du plancher égales à la sonde : D* = 0 exactement sur chaque tirage ; borne basse 0, « non
    au-dessus » (inégalité stricte), et `bas` = quantile exactement."""
    s, _, y, blocs = jeu(seed=23, n=10, signal=1.0)
    r = pl2.comparer_difference_au_plancher(s, np.tile(s, (40, 1)), y, blocs, 200, 3, 0.95, NIVEAU_DECISIF)
    assert r["difference"]["bas"] == 0.0 == r["difference"]["haut"] and r["au_dessus_du_plancher"] is False
    resume = pl2.resume_pour_critere(r)
    assert resume["bas"] == r["plancher_quantile"] and cr.etat_pour_sonde({**resume, "triviaux": {}}) == cr.NON_AU_DESSUS


def test_garde_degeneres_cas_sain_et_artefact():
    s, P, y, blocs = jeu(seed=2, n=10)
    sain = pl2.comparer_difference_au_plancher(s, P, y, blocs, 200, 1, 0.95, 0.95)
    assert sain["difference"]["degeneres"] == 0
    y2 = y.copy()
    y2[blocs != 0] = 0                                   # artefact : une seule tâche porte les positifs
    with pytest.raises(GardeArret) as e:
        pl2.comparer_difference_au_plancher(s, P, y2, blocs, 200, 1, 0.95, 0.95)
    with pytest.raises(GardeArret) as e_gele:
        intervalle_blocs(s, y2, blocs, 200, 1, 0.95)
    assert str(e.value) == str(e_gele.value) and "sans les deux classes" in str(e.value)


def test_garde_degeneres_au_seuil_de_un_pour_cent():
    """Fonction interne : 2 tirages dégénérés sur 200 (1 %) passent et sont comptés ; 3 (1,5 %) arrêtent."""
    s, P, y, blocs = jeu(seed=2, n=10)
    comp = pl2.comparaisons_par_taches(np.vstack([s[None, :], P]), y, blocs)
    W = pl2.poids_des_tirages(10, 200, 3)
    n1 = comp["n1"].copy()
    n1[1:] = 0                                            # positifs dans la seule tâche 0
    W[:, 0] = np.maximum(W[:, 0], 1)
    W[:2, 0] = 0
    d = pl2.difference_sur_poids(comp["C"], n1, comp["n0"], W, 0.95, 0.95)
    assert d["degeneres"] == 2 and d["tirages"] == 198
    W[2, 0] = 0
    with pytest.raises(GardeArret, match="3 tirages sur 200 sans les deux classes"):
        pl2.difference_sur_poids(comp["C"], n1, comp["n0"], W, 0.95, 0.95)


@pytest.mark.parametrize("cas,motif", [
    ("score_nan", "score non fini"), ("plancher_inf", "score non fini"), ("etiquette_2", "étiquettes 0/1"),
    ("une_classe", "les deux classes"), ("un_bloc", "au moins deux blocs"), ("forme", "attendues"),
    ("niveau", "hors de ]0,5 ; 1["), ("quantile", "quantile_plancher"), ("tirages", "au moins un tirage"),
    ("plancher_vide", "attendues")])
def test_gardes_des_entrees_artefacts(cas, motif):
    s, P, y, blocs = jeu(seed=4, n=6)
    args = dict(scores_sonde=s, scores_plancher=P, y=y, blocs=blocs, n_tirages=50, graine=1, quantile_plancher=0.95, niveau=0.95)
    if cas == "score_nan":
        args["scores_sonde"] = np.where(np.arange(s.size) == 3, np.nan, s)
    elif cas == "plancher_inf":
        P2 = P.copy()
        P2[2, 5] = np.inf
        args["scores_plancher"] = P2
    elif cas == "etiquette_2":
        args["y"] = np.where(np.arange(y.size) == 0, 2, y)
    elif cas == "une_classe":
        args["y"] = np.ones_like(y)
    elif cas == "un_bloc":
        args["blocs"] = np.zeros_like(blocs)
    elif cas == "forme":
        args["scores_plancher"] = P[:, :-1]
    elif cas == "niveau":
        args["niveau"] = 0.4
    elif cas == "quantile":
        args["quantile_plancher"] = 1.0
    elif cas == "tirages":
        args["n_tirages"] = 0
    elif cas == "plancher_vide":
        args["scores_plancher"] = P[:0]
    with pytest.raises(GardeArret, match=motif.replace("[", r"\[").replace("]", r"\]").replace("(", r"\(")):
        pl2.comparer_difference_au_plancher(**args)
    sain = {**args, "scores_sonde": s, "scores_plancher": P, "y": y, "blocs": blocs, "n_tirages": 50, "quantile_plancher": 0.95,
            "niveau": 0.95}
    assert pl2.comparer_difference_au_plancher(**sain)["difference"]["tirages"] == 50


def test_garde_comptage_egal_au_paquet_gele_cas_sain_et_artefact(monkeypatch):
    s, P, y, blocs = jeu(seed=6, n=8)
    assert pl2.comparer_difference_au_plancher(s, P, y, blocs, 60, 2)["aire"] == aire_sous_courbe(s, y)
    monkeypatch.setattr(pl2, "aire_sous_courbe", lambda sc, yy: aire_sous_courbe(sc, yy) + 1e-15)
    with pytest.raises(GardeArret, match="comptage inexact"):
        pl2.comparer_difference_au_plancher(s, P, y, blocs, 60, 2)


def test_garde_tirages_egaux_a_intervalle_blocs_cas_sain_et_artefact(monkeypatch):
    s, P, y, blocs = jeu(seed=7, n=8, signal=0.3)
    assert pl2.comparer_difference_au_plancher(s, P, y, blocs, 80, 5)["tirages"] == 80
    monkeypatch.setattr(pl2, "intervalle_blocs", lambda sc, yy, bl, nt, g, nv: intervalle_blocs(sc, yy, bl, nt, g + 1, nv))
    with pytest.raises(GardeArret, match="tirages de la différence"):
        pl2.comparer_difference_au_plancher(s, P, y, blocs, 80, 5)


def test_resume_pour_critere_sens_de_bas_et_garde_de_la_borne_perdue():
    base = {"aire": 0.7, "bas": 0.61, "haut": 0.79, "plancher_quantile": 0.6, "plancher": {"quantile": 0.6}, "triviaux": {}}
    for borne, attendu in ((1e-3, cr.AU_DESSUS), (0.0, cr.NON_AU_DESSUS), (-1e-3, cr.NON_AU_DESSUS), (-1e-18, cr.NON_AU_DESSUS)):
        r = pl2.resume_pour_critere({**base, "au_dessus_du_plancher": borne > 0, "difference": {"bas": borne, "haut": 0.2}})
        assert r["bas"] == 0.6 + borne and r["haut"] == 0.6 + 0.2 and r["bas_sonde"] == 0.61 and r["haut_sonde"] == 0.79
        assert r["sens_de_bas"] == pl2.SENS_DE_BAS and cr.etat_pour_sonde(r) == attendu
    with pytest.raises(GardeArret, match="borne perdue"):        # artefact : borne > 0 plus petite que l'écart entre flottants
        pl2.resume_pour_critere({**base, "au_dessus_du_plancher": True, "difference": {"bas": 1e-18, "haut": 0.2}})
    with pytest.raises(GardeArret, match="borne perdue"):        # artefact : drapeau contraire à la borne
        pl2.resume_pour_critere({**base, "au_dessus_du_plancher": False, "difference": {"bas": 1e-3, "haut": 0.2}})


# ------------------------------------------------------------------------------------------------ reproduction du prototype
def _piece(nom: str, sha: str, dossier: Path) -> Path:
    """La pièce scellée, lue sur disque (arbre complet) ou par `git show <commit>:<chemin>` (arbre réduit), à son empreinte."""
    p = RACINE_DEPOT / DOSSIER_PIECES / nom
    brut = p.read_bytes() if p.is_file() else subprocess.run(
        ["git", "-C", str(RACINE_DEPOT), "show", f"{COMMIT_PIECES}:{DOSSIER_PIECES}/{nom}"], capture_output=True, check=True).stdout
    assert hashlib.sha256(brut).hexdigest() == sha, nom
    sortie = dossier / nom
    sortie.write_bytes(brut)
    return sortie


@pytest.fixture(scope="module")
def prototype(tmp_path_factory):
    dossier = tmp_path_factory.mktemp("prototype")
    v1 = _piece("erreur_premiere_espece_t07_v1.py", SHA_SCRIPT_V1, dossier)
    chemin = _piece("remede_a_prototype_v1.py", SHA_PROTOTYPE, dossier)
    spec = importlib.util.spec_from_file_location("remede_a_prototype_v1_essai", chemin)
    pa = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(pa)
    pa.charger(str(RACINE_DEPOT), str(v1))          # vérifie les empreintes du code gelé (script v1)
    return pa


# mondes de référence du prototype : (n, θ_F, ρ, clé du monde) — phase « nul », cellules dures et une cellule courante
MONDES = [(64, 0.94, 1.0, (2, 64, 3, 1, 0, 0, 0)), (36, 0.94, 1.0, (2, 36, 3, 1, 0, 0, 1)), (64, 0.62, 4.0, (1, 64, 1, 0, 0, 0, 3))]


@pytest.mark.parametrize("n,theta,rho,cle", MONDES)
def test_reproduit_le_prototype_au_bit_sur_ses_mondes(prototype, n, theta, rho, cle):
    """Mêmes tirages que le prototype (injectés) : mêmes matrices, même borne basse de D* au bit près, même décision par
    `etat_pour_sonde` ; et la fonction publique rend les mêmes aire et quantile ponctuels que le prototype."""
    pa, v1 = prototype, prototype.V1
    y, sondes, planchers = v1.generer(n, theta, rho, "propre", v1.r_pour(theta, n), cle)
    tache = np.repeat(np.arange(n), 2 * v1.T)
    decisions = []
    for p in range(v1.N_SONDES):
        graine = np.random.SeedSequence(pa.ENTROPIE_A, spawn_key=(17,) + cle + (p,))
        ref = pa.lire_remede(n, y, sondes[p], planchers[p], np.random.default_rng(graine), controle=(p == 0))
        W, _ = pa.poids(np.random.default_rng(np.random.SeedSequence(pa.ENTROPIE_A, spawn_key=(17,) + cle + (p,))), n)
        X = np.vstack([sondes[p][None, :], planchers[p]])
        comp = pl2.comparaisons_par_taches(X, y, tache)
        assert np.array_equal(comp["C"], pa.comparaisons(X, n))
        d = pl2.difference_sur_poids(comp["C"], comp["n1"], comp["n0"], W, 0.95, pa.NIVEAU)
        assert d["bas"] == ref["bornes"]["percentile_D"] and d["degeneres"] == 0
        r = pl2.comparer_difference_au_plancher(sondes[p], planchers[p], y, tache, 50, 1, 0.95, pa.NIVEAU)
        assert r["aire"] == ref["aire"] and r["plancher_quantile"] == ref["q95"]
        resume = pl2.resume_pour_critere({**r, "au_dessus_du_plancher": d["bas"] > 0.0,
                                          "difference": {**r["difference"], "bas": d["bas"], "haut": d["haut"]}})
        etat = cr.etat_pour_sonde({**resume, "triviaux": {}})
        assert etat == ref["etats"]["percentile_D"]
        decisions.append(etat)
    if cle == MONDES[0][3]:
        assert decisions.count(cr.AU_DESSUS) >= 1                 # ce monde porte un « au-dessus » du prototype (nul de population)
