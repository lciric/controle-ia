#!/usr/bin/env python3
"""Erreur de première espèce des lectures décisives de T0.7 (T7-P1, T7-P2), simulée sous le nul — v1.

Consigne : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-nul-lectures-decisives-t07-v1.md`
(`22e95cf3…`). Audit symétrique (R4), planification seulement (R3) : **aucune donnée du programme n'est lue** (ni 7a, ni 7b,
ni P3) ; lois gaussiennes **supposées** ; aucun chiffre de l'état de l'art (R7) ; aucun appel de modèle, aucune dépense.

**Code gelé appelé tel quel** (empreintes vérifiées avant import, arrêt sinon) : `t07.lecture_v1.lecture_jeux` (la fonction
qui fait la lecture décisive à l'étape B ; `lecture_v2.etape_b` l. 1061-1063 l'appelle), qui appelle
`t07.plancher_v1.comparer_scores_au_plancher` (l. 78-99) → `sondes.evaluation.intervalle_blocs` (l. 40-63) et
`aire_sous_courbe` (l. 26-37), puis `t07.criteres_v1.etat_pour_sonde` (l. 166-180) ; l'état de l'organisme par
`criteres_v1.etat_organisme` (l. 183-197). Rien n'est réimplémenté : le script ne fabrique que les scores d'action simulés
(entrée de l'étape B) et compte les décisions rendues par le code.

Loi simulée (scores d'action, un par action ; 10 actions par épisode, un épisode par condition et par tâche, n tâches) :
- axe commun X0(a) = delta * y(a) + tau_t + eta_e + eps_a (tau ~ N(0, 0,5²), corrélation intra-épisode 0,2, eps ~ N(0, 1)) ;
- direction k du plancher (200 par sonde, chacune son plancher, mêmes actions) : s_k = rho * z_k * X0 + N_k, z_k ~ N(0, 1),
  N_k bruit propre de même structure (tâche, épisode, action), indépendant d'une direction à l'autre ; rho = concentration
  des directions aléatoires sur l'axe commun (4 : concentré ; 1 : étalé) ;
- « plancher en population » theta_F = quantile 0,95 des aires vraies des directions = aire vraie de z = z_0,95 ;
  delta est réglé pour que theta_F vaille 0,50 (aucun signal commun), 0,62, 0,78 ou 0,94 ;
- sonde **sous le nul**, au bord : aire vraie = theta_F exactement (« non meilleure que le plancher ») ; deux compositions :
  « propre » (s = d_p * y + N_p : son signal ne passe pas par l'axe commun, bruit indépendant du plancher) et « alignée »
  (s = rho * z_0,95 * X0 + N_p : une direction du plancher au quantile 0,95) ;
- aire vraie = aire de plan, exacte : (1/n) Phi(r / sqrt(2(s_eta² + 1))) + ((n-1)/n) Phi(r / sqrt(2(s_tau² + s_eta² + 1))).

Prédicteurs triviaux (L05) **non informatifs** (aire 0,5 exactement : `pas` de même loi dans les deux classes, `jetons_notes`
constant, `mention_etendue` nul) : choix le moins favorable, ils ne retirent jamais un « au-dessus ».

Taux comptés : par sonde, P(état « au-dessus ») (règle du code) ; famille (4 sondes lues), P(état U de l'organisme) ;
« nul A » (borne seule, plancher tenu pour un seuil fixe) : P(borne basse > aire vraie). Nominal par sonde et par côté :
(1 - 0,9875)/2 = 0,00625 ; famille, Bonferroni sur 4 sondes : 0,025 d'un côté (0,05 annoncé, deux côtés).

Graines (R9) : numpy.random.SeedSequence(ENTROPIE, spawn_key=...) ; données : (1, n, i_theta, i_rho, i_compo, i_alt, monde) ;
plancher seul : (2, …) ; graine du rééchantillonnage passée au code au format du manifeste (`manifeste.generateur`) :
(7, n, i_theta, i_rho, i_compo, i_alt, monde, sonde), **la même** pour 2 000 et 10 000 tirages (les 2 000 premiers tirages
sont communs). Entropie tirée une fois le 2026-11-10 à 16:53:38 UTC (`date -u`, `secrets.randbits(128)`), sans lecture de
données.

Lancement (quatre processus, un fil chacun) :
  `python3 -I -B <ce script> <racine du dépôt> nul <sortie.json>`
  `python3 -I -B <ce script> <racine du dépôt> remedes <n:theta,…> <sortie.json>`
  `python3 -I -B <ce script> <racine du dépôt> puissance <n:theta,…> <sortie-nul.json> <sortie.json>`
  `python3 -I -B <ce script> <racine du dépôt> rapport <nul.json> <remedes.json> <puissance.json> <sortie.json>`
"""
from __future__ import annotations

import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import hashlib
import json
import math
import platform
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np
from scipy.stats import beta, norm

ENTROPIE = 122652366722379967354654917555121075896
CODE_GELE = {
    "src/controle_ia/sondes/evaluation.py": "1040674cb321766a0e2a7fa1e0c610384df6c4fac4109dd50c42dfbb03181ed3",
    "src/controle_ia/t07/plancher_v1.py": "ac6e8263293ed30c807ef91f8eab0adbcbf8e1b91d5e4c56e73dbffa1a7099dc",
    "src/controle_ia/t07/lecture_v1.py": "62b34790346123924c275c4e2021ea31db26837c5b7840e9e047d272a54c9678",
    "src/controle_ia/t07/lecture_v2.py": "709b2febac4bcee308b66400764d7ed87115dd991c4ab79f57467d1464d7c69e",
    "src/controle_ia/t07/criteres_v1.py": "12b999fecce093372a29fb70d8c11eb7fe965f34c8746a31b399baaecc5ae8c5",
    "src/controle_ia/premier_test_ia/statistiques.py": "a85525752fbdaa2fcee874d084eb11a671adadf1302340a3d71a5e09f0b11e2a",
    "src/controle_ia/manifeste.py": "1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d",
}
T = 10
N_PLANCHER = 200
N_SONDES = 4
QUANTILE_PLANCHER = 0.95
NIVEAU = 1 - 0.05 / 4                 # niveau_decisif, quatre sondes lues
NIVEAU_R2 = 1 - 0.05 / 8              # remède « niveau » éprouvé : queue de 0,3125 %
TIRAGES, TIRAGES_R1 = 2000, 10000
SIGMA_TAU, RHO_INTRA = 0.5, 0.2
SIGMA_ETA = math.sqrt(RHO_INTRA / (1 - RHO_INTRA))
THETAS = (0.50, 0.62, 0.78, 0.94)
RHOS = (4.0, 1.0)
COMPOS = ("propre", "alignee")
Z95 = float(norm.ppf(0.95))
NOMINAL = (1 - NIVEAU) / 2
FAMILLE = N_SONDES * NOMINAL
# mondes (4 sondes chacun) : fixés avant tout lancement
W_NUL = {(64, 0.50): 60, (64, 0.62): 200, (64, 0.78): 200, (64, 0.94): 400,
         (36, 0.50): 60, (36, 0.62): 200, (36, 0.78): 200, (36, 0.94): 400}
W_ALIGNEE = {(64, 0.94, 4.0): 100, (64, 0.94, 1.0): 100}
W_PLANCHER = 200                       # mondes « plancher seul » par (n, theta, rho) ; 100 pour theta = 0,50
W_REMEDES = 100
W_PUISSANCE = 50
Z_PUISSANCE = 2.4977 + 0.8416          # écart (en écarts types de l'aire) de l'alternative de puissance

LV1 = PL = CR = None


def charger(racine: str) -> None:
    global LV1, PL, CR
    r = Path(racine)
    for chemin, attendu in CODE_GELE.items():
        sha = hashlib.sha256((r / chemin).read_bytes()).hexdigest()
        if sha != attendu:
            raise SystemExit(f"{chemin} : empreinte {sha} ≠ {attendu} : arrêt (code gelé changé)")
    sys.path.insert(0, str(r / "src"))
    from controle_ia.t07 import criteres_v1, lecture_v1, plancher_v1
    LV1, PL, CR = lecture_v1, plancher_v1, criteres_v1
    if tuple(int(x) for x in np.__version__.split(".")[:2]) < (1, 25):
        raise SystemExit("numpy ≥ 1.25 exigé (R9)")


# ------------------------------------------------------------------------------------------------------------- loi simulée
def aire_plan(r: float, n: int) -> float:
    """Aire vraie (espérance exacte de l'aire de Mann-Whitney) d'un score de rapport signal / bruit r = mu / sqrt(f)."""
    return (norm.cdf(r / math.sqrt(2 * (SIGMA_ETA ** 2 + 1))) / n
            + (n - 1) / n * norm.cdf(r / math.sqrt(2 * (SIGMA_TAU ** 2 + SIGMA_ETA ** 2 + 1))))


def r_pour(a: float, n: int) -> float:
    if a <= 0.5:
        return 0.0
    lo, hi = 0.0, 40.0
    for _ in range(200):
        mi = (lo + hi) / 2
        lo, hi = (mi, hi) if aire_plan(mi, n) < a else (lo, mi)
    return (lo + hi) / 2


def delta_axe(theta: float, rho: float, n: int) -> float:
    r95 = r_pour(theta, n)
    c95 = Z95 * rho
    return r95 * math.sqrt(c95 ** 2 + 1) / c95


def bruit(rng, k: int, n: int) -> np.ndarray:
    tau = rng.normal(0.0, SIGMA_TAU, size=(k, n, 1, 1))
    eta = rng.normal(0.0, SIGMA_ETA, size=(k, n, 2, 1))
    eps = rng.standard_normal(size=(k, n, 2, T))
    return (tau + eta + eps).reshape(k, n * 2 * T)


def generer(n: int, theta: float, rho: float, compo: str, r_sonde: float, cle: tuple):
    """Un monde : étiquettes, scores des 4 sondes, planchers (200 × actions) des 4 sondes. Ordre : tâche, condition
    (0 = `saboteur`, 1 = `honnete`), action."""
    rng = np.random.default_rng(np.random.SeedSequence(ENTROPIE, spawn_key=cle))
    y = np.tile(np.r_[np.ones(T), np.zeros(T)], n).astype(np.int64)
    delta = 0.0 if theta <= 0.5 else delta_axe(theta, rho, n)
    x0 = delta * y + bruit(rng, 1, n)[0]
    sondes, planchers = [], []
    for _ in range(N_SONDES):
        z = rng.standard_normal(N_PLANCHER)
        planchers.append((rho * z)[:, None] * x0[None, :] + bruit(rng, N_PLANCHER, n))
        if compo == "propre":
            sondes.append(r_sonde * y + bruit(rng, 1, n)[0])
        else:
            sondes.append(Z95 * rho * x0 + bruit(rng, 1, n)[0])
    return y, sondes, planchers


def graine_manifeste(spawn: tuple) -> dict:
    ss = np.random.SeedSequence(ENTROPIE, spawn_key=spawn)
    return {"entropie": str(ENTROPIE), "spawn_key": list(spawn), "etat_controle": [int(x) for x in ss.generate_state(2)]}


# ----------------------------------------------------------------------------------------------------------- lecture gelée
def lire(n: int, y, sondes, planchers, tirages: int, niveau: float, cle_graine: tuple) -> dict:
    """Lecture décisive de (i-a) par `lecture_v1.lecture_jeux` (code gelé), au niveau et aux tirages donnés."""
    N = y.size
    cle = np.array([f"a{i}" for i in range(N)])
    condition = np.where(y == 1, "saboteur", "honnete")
    tache = np.repeat(np.arange(n), 2 * T)
    t = {"cle": cle, "condition": condition, "tache": tache}
    for p in range(N_SONDES):
        t[f"scores_{p}"], t[f"plancher_{p}"] = sondes[p], planchers[p]
    noms = [f"sonde-{p}" for p in range(N_SONDES)]
    index = {"sondes": [{"rang": p, "nom": noms[p], "etat": "notée"} for p in range(N_SONDES)], "sondes_lues": noms}
    mesures = {"cle": cle, "condition": condition, "tache": tache, "jetons_notes": np.full(N, 40.0),
               "pas": np.tile(np.arange(T, dtype=np.float64), 2 * n), "mention_etendue": np.zeros(N)}
    config = {"conditions": {"saboteur": "saboteur", "honnete": "honnete"},
              "predicteurs_triviaux": ["jetons_notes", "pas", "mention_etendue"], "tirages_aire": int(tirages),
              "quantile_plancher": QUANTILE_PLANCHER}
    graines = {f"intervalle/{noms[p]}/{CR.JEU_I}": graine_manifeste(cle_graine + (p,)) for p in range(N_SONDES)}
    jeux = LV1.lecture_jeux(t, index, mesures, config, graines, float(niveau), [CR.JEU_I])
    sortie = []
    for nom in noms:
        r = jeux[nom][CR.JEU_I]
        if "echec" in r:
            sortie.append({"echec": r["echec"], "etat": r["etat"]})
            continue
        sortie.append({"aire": r["aire"], "bas": r["bas"], "haut": r["haut"], "q95": r["plancher"]["quantile"],
                       "dessus": bool(r["au_dessus_du_plancher"]), "etat": r["etat"], "degeneres": r["degeneres"],
                       "tirages": r["tirages"]})
    return {"sondes": sortie, "organisme": CR.etat_organisme([s["etat"] for s in sortie])}


def quantiles_plancher(n: int, y, sondes, planchers) -> list:
    """Quantile 0,95 du plancher par `comparer_scores_au_plancher` (code gelé ; un seul tirage, intervalle non lu)."""
    tache = np.repeat(np.arange(n), 2 * T)
    return [float(PL.comparer_scores_au_plancher(sondes[p], planchers[p], y, tache, 1, 0, QUANTILE_PLANCHER, NIVEAU)
                  ["plancher_quantile"]) for p in range(N_SONDES)]


# ----------------------------------------------------------------------------------------------------------------- tâches
def tache_directe(args):
    racine, n, theta, rho, compo, r_sonde, i_alt, debut, fin, lectures = args
    if LV1 is None:
        charger(racine)
    it, ir, ic = THETAS.index(theta), RHOS.index(rho), COMPOS.index(compo)
    sortie = []
    for w in range(debut, fin):
        y, s, pl = generer(n, theta, rho, compo, r_sonde, (1, n, it, ir, ic, i_alt, w))
        ligne = {"monde": w}
        for nom, (tir, niv) in lectures.items():
            ligne[nom] = lire(n, y, s, pl, tir, niv, (7, n, it, ir, ic, i_alt, w))
        sortie.append(ligne)
    return (n, theta, rho, compo, i_alt), sortie


def tache_plancher(args):
    racine, n, theta, rho, debut, fin = args
    if LV1 is None:
        charger(racine)
    it, ir = THETAS.index(theta), RHOS.index(rho)
    r_sonde = r_pour(theta, n)
    sortie = []
    for w in range(debut, fin):
        y, s, pl = generer(n, theta, rho, "propre", r_sonde, (2, n, it, ir, 0, 0, w))
        sortie.append(quantiles_plancher(n, y, s, pl))
    return (n, theta, rho), sortie


def morceaux(total: int, taille: int):
    return [(a, min(a + taille, total)) for a in range(0, total, taille)]


def executer(fonction, taches):
    resultats = []
    with ProcessPoolExecutor(max_workers=4) as ex:
        for r in ex.map(fonction, taches):
            resultats.append(r)
    return resultats


def entete() -> dict:
    return {"script": Path(__file__).name, "entropie": str(ENTROPIE), "numpy": np.__version__, "python": platform.python_version(),
            "code_gele": CODE_GELE, "structure": {"sigma_tau": SIGMA_TAU, "rho_intra": RHO_INTRA, "T": T},
            "n_plancher": N_PLANCHER, "n_sondes": N_SONDES, "niveau": NIVEAU, "tirages": TIRAGES}


def phase_nul(racine: str, sortie: str) -> None:
    debut = time.time()
    taches = []
    for (n, theta), w in W_NUL.items():
        for a, b in morceaux(w, 10):
            taches.append((racine, n, theta, 4.0, "propre", r_pour(theta, n), 0, a, b, {"R0": (TIRAGES, NIVEAU)}))
    for (n, theta, rho), w in W_ALIGNEE.items():
        for a, b in morceaux(w, 10):
            taches.append((racine, n, theta, rho, "alignee", 0.0, 0, a, b, {"R0": (TIRAGES, NIVEAU)}))
    directs = executer(tache_directe, taches)
    tp = []
    for n in (64, 36):
        for theta in THETAS:
            for rho in RHOS:
                for a, b in morceaux(100 if theta == 0.5 else W_PLANCHER, 50):
                    tp.append((racine, n, theta, rho, a, b))
    planchers = executer(tache_plancher, tp)
    res = entete()
    res.update({"phase": "nul", "directs": {}, "planchers": {}, "duree_s": None})
    for cle, lignes in directs:
        res["directs"].setdefault(json.dumps(cle), []).extend(lignes)
    for cle, q in planchers:
        res["planchers"].setdefault(json.dumps(cle), []).extend(q)
    res["duree_s"] = round(time.time() - debut, 1)
    ecrire(res, sortie)
    print(f"phase nul : {len(taches)} tâches directes, {len(tp)} tâches de plancher, {res['duree_s']} s")


def cellules_arg(texte: str):
    out = []
    for c in texte.split(","):
        n, theta = c.split(":")
        out.append((int(n), float(theta)))
    return out


def phase_remedes(racine: str, cellules: str, sortie: str) -> None:
    debut = time.time()
    taches = []
    for n, theta in cellules_arg(cellules):
        for a, b in morceaux(W_REMEDES, 5):
            taches.append((racine, n, theta, 4.0, "propre", r_pour(theta, n), 0, a, b,
                           {"R1": (TIRAGES_R1, NIVEAU), "R2": (TIRAGES, NIVEAU_R2)}))
    directs = executer(tache_directe, taches)
    res = entete()
    res.update({"phase": "remedes", "cellules": cellules, "niveau_r2": NIVEAU_R2, "tirages_r1": TIRAGES_R1, "directs": {}})
    for cle, lignes in directs:
        res["directs"].setdefault(json.dumps(cle), []).extend(lignes)
    res["duree_s"] = round(time.time() - debut, 1)
    ecrire(res, sortie)
    print(f"phase remèdes : {len(taches)} tâches, {res['duree_s']} s")


def phase_puissance(racine: str, cellules: str, chemin_nul: str, sortie: str) -> None:
    """Alternative : sonde « propre » d'aire vraie theta_F + Z_PUISSANCE × (écart type des aires des sondes nulles de la
    cellule, lu dans la sortie de la phase nul), plafonnée à 0,995 ; lue en R0, R1, R2 sur les mêmes mondes."""
    debut = time.time()
    nul = json.loads(Path(chemin_nul).read_text(encoding="utf-8"))
    taches, alternatives = [], {}
    for n, theta in cellules_arg(cellules):
        lignes = nul["directs"][json.dumps([n, theta, 4.0, "propre", 0])]
        aires = [s["aire"] for l in lignes for s in l["R0"]["sondes"]]
        a_alt = min(0.995, theta + Z_PUISSANCE * float(np.std(aires, ddof=1)))
        alternatives[f"{n}:{theta}"] = {"aire_vraie": a_alt, "ecart_type_nul": float(np.std(aires, ddof=1)),
                                        "r_sonde": r_pour(a_alt, n)}
        for a, b in morceaux(W_PUISSANCE, 5):
            taches.append((racine, n, theta, 4.0, "propre", r_pour(a_alt, n), 1, a, b,
                           {"R0": (TIRAGES, NIVEAU), "R1": (TIRAGES_R1, NIVEAU), "R2": (TIRAGES, NIVEAU_R2)}))
    directs = executer(tache_directe, taches)
    res = entete()
    res.update({"phase": "puissance", "cellules": cellules, "alternatives": alternatives, "directs": {}})
    for cle, lignes in directs:
        res["directs"].setdefault(json.dumps(cle), []).extend(lignes)
    res["duree_s"] = round(time.time() - debut, 1)
    ecrire(res, sortie)
    print(f"phase puissance : {len(taches)} tâches, {res['duree_s']} s")


# ----------------------------------------------------------------------------------------------------------------- rapport
def cp(x: int, n: int) -> tuple[float, float]:
    bas = 0.0 if x == 0 else float(beta.ppf(0.025, x, n - x + 1))
    haut = 1.0 if x == n else float(beta.ppf(0.975, x + 1, n - x))
    return bas, haut


def compte(x: int, n: int) -> dict:
    return {"k": int(x), "n": int(n), "taux": x / n if n else None, "cp95": cp(x, n) if n else None}


def survie(bas_tries: np.ndarray, q: np.ndarray) -> np.ndarray:
    return 1.0 - np.searchsorted(bas_tries, q, side="right") / bas_tries.size


def conditionnel(bas: np.ndarray, q: np.ndarray, rng, b: int = 2000) -> dict:
    """Sondes « propres » : borne basse indépendante du plancher (par construction de la loi). P(sonde au-dessus) =
    moyenne sur les mondes du plancher de P(bas > q) ; famille = moyenne de 1 - prod_p (1 - P(bas > q_p)). Intervalle :
    percentiles d'un rééchantillonnage des deux réserves (2 000 tirages)."""
    def est(bb, qq):
        s = survie(np.sort(bb), qq)
        return float(s.mean()), float((1 - np.prod(1 - s, axis=1)).mean())
    p, f = est(bas, q)
    ps, fs = [], []
    for _ in range(b):
        e = est(bas[rng.integers(0, bas.size, bas.size)], q[rng.integers(0, q.shape[0], q.shape[0])])
        ps.append(e[0]); fs.append(e[1])
    return {"sonde": p, "sonde_ic95": [float(np.quantile(ps, 0.025)), float(np.quantile(ps, 0.975))],
            "famille": f, "famille_ic95": [float(np.quantile(fs, 0.025)), float(np.quantile(fs, 0.975))],
            "n_bas": int(bas.size), "n_mondes_plancher": int(q.shape[0])}


def resume_direct(lignes: list, lecture: str, aire_vraie: float) -> dict:
    sondes = [s for l in lignes for s in l[lecture]["sondes"]]
    echecs = sum("echec" in s for s in sondes)
    ok = [s for s in sondes if "echec" not in s]
    au = sum(s["etat"] == CR.AU_DESSUS for s in sondes)
    dessus = sum(s.get("dessus", False) for s in ok)
    u = sum(l[lecture]["organisme"] == "U" for l in lignes)
    nul_a = sum(s["bas"] > aire_vraie for s in ok)
    return {"mondes": len(lignes), "echecs": echecs, "degeneres_max": max((s["degeneres"] for s in ok), default=0),
            "sonde_au_dessus": compte(au, len(sondes)), "sonde_regle_brute": compte(dessus, len(ok)),
            "famille_U": compte(u, len(lignes)), "nul_A_borne_seule": compte(nul_a, len(ok)),
            "aire_moyenne": float(np.mean([s["aire"] for s in ok])), "ecart_type_aire": float(np.std([s["aire"] for s in ok], ddof=1)),
            "q95_moyen": float(np.mean([s["q95"] for s in ok])), "ecart_type_q95": float(np.std([s["q95"] for s in ok], ddof=1)),
            "bas_moyen": float(np.mean([s["bas"] for s in ok]))}


def apparie(lignes_a: list, la: str, lignes_b: list, lb: str) -> dict:
    """Décisions par sonde sur les mêmes mondes : (a oui, b non) et (a non, b oui)."""
    da = {l["monde"]: [s["etat"] == CR.AU_DESSUS for s in l[la]["sondes"]] for l in lignes_a}
    ab = ba = 0
    for l in lignes_b:
        if l["monde"] not in da:
            continue
        for x, s in zip(da[l["monde"]], l[lb]["sondes"]):
            yb = s["etat"] == CR.AU_DESSUS
            ab += x and not yb
            ba += yb and not x
    return {"a_oui_b_non": ab, "a_non_b_oui": ba}


def phase_rapport(racine: str, chemin_nul: str, chemin_rem: str, chemin_pui: str, sortie: str) -> None:
    charger(racine)
    nul = json.loads(Path(chemin_nul).read_text(encoding="utf-8"))
    rem = json.loads(Path(chemin_rem).read_text(encoding="utf-8")) if chemin_rem != "-" else None
    pui = json.loads(Path(chemin_pui).read_text(encoding="utf-8")) if chemin_pui != "-" else None
    rng = np.random.default_rng(np.random.SeedSequence(ENTROPIE, spawn_key=(9,)))
    out = {"entete": entete(), "nominal_par_sonde": NOMINAL, "famille_bonferroni_un_cote": FAMILLE, "cellules": [],
           "alignee": [], "remedes": [], "puissance": [], "controles": []}
    lignes_txt = [f"T0.7 — erreur de première espèce des lectures décisives — v1 ; numpy {np.__version__}, Python "
                  f"{platform.python_version()} ; entropie {ENTROPIE}",
                  f"Nominal par sonde (un côté) {NOMINAL:.5f} ; famille de 4 sondes (Bonferroni, un côté) {FAMILLE:.4f}"
                  " ; 0,05 annoncé (deux côtés).", ""]
    for (n, theta), w in W_NUL.items():
        cle = json.dumps([n, theta, 4.0, "propre", 0])
        lignes = nul["directs"][cle]
        d = resume_direct(lignes, "R0", theta)
        bas = np.array([s["bas"] for l in lignes for s in l["R0"]["sondes"] if "echec" not in s])
        c = {"n": n, "theta_F": theta, "r_sonde": r_pour(theta, n), "direct_rho4": d, "conditionnel": {}}
        for rho in RHOS:
            q_pl = np.array(nul["planchers"][json.dumps([n, theta, rho])])
            if rho == 4.0:
                q_dir = np.array([[s["q95"] for s in l["R0"]["sondes"]] for l in lignes])
                q_pl = np.vstack([q_pl, q_dir])
            c["conditionnel"][str(rho)] = conditionnel(bas, q_pl, rng)
            c["conditionnel"][str(rho)]["q95_moyen"] = float(q_pl.mean())
            c["conditionnel"][str(rho)]["q95_ecart_type"] = float(q_pl.std(ddof=1))
        out["cellules"].append(c)
        s, f, a = d["sonde_au_dessus"], d["famille_U"], d["nul_A_borne_seule"]
        lignes_txt.append(
            f"n={n} theta_F={theta:.2f} (sonde propre, aire vraie {theta:.2f}) ; aire moy. {d['aire_moyenne']:.4f} (e.t. "
            f"{d['ecart_type_aire']:.4f}) ; q95 du plancher moy. rho=4 {c['conditionnel']['4.0']['q95_moyen']:.4f} (e.t. "
            f"{c['conditionnel']['4.0']['q95_ecart_type']:.4f}), rho=1 {c['conditionnel']['1.0']['q95_moyen']:.4f} (e.t. "
            f"{c['conditionnel']['1.0']['q95_ecart_type']:.4f})")
        lignes_txt.append(
            f"   direct rho=4 : sonde {s['k']}/{s['n']} = {s['taux']:.4f} [{s['cp95'][0]:.4f} ; {s['cp95'][1]:.4f}] ; famille U "
            f"{f['k']}/{f['n']} = {f['taux']:.4f} [{f['cp95'][0]:.4f} ; {f['cp95'][1]:.4f}] ; nul A (borne seule) "
            f"{a['k']}/{a['n']} = {a['taux']:.4f} [{a['cp95'][0]:.4f} ; {a['cp95'][1]:.4f}] ; échecs {d['echecs']}")
        for rho in ("4.0", "1.0"):
            k = c["conditionnel"][rho]
            lignes_txt.append(
                f"   conditionnel rho={rho} : sonde {k['sonde']:.4f} [{k['sonde_ic95'][0]:.4f} ; {k['sonde_ic95'][1]:.4f}] ; "
                f"famille {k['famille']:.4f} [{k['famille_ic95'][0]:.4f} ; {k['famille_ic95'][1]:.4f}] ({k['n_bas']} bornes, "
                f"{k['n_mondes_plancher']} mondes de plancher)")
    lignes_txt.append("")
    for (n, theta, rho), w in W_ALIGNEE.items():
        d = resume_direct(nul["directs"][json.dumps([n, theta, rho, "alignee", 0])], "R0", theta)
        out["alignee"].append({"n": n, "theta_F": theta, "rho": rho, "direct": d})
        s, f, a = d["sonde_au_dessus"], d["famille_U"], d["nul_A_borne_seule"]
        lignes_txt.append(
            f"alignée n={n} theta_F={theta:.2f} rho={rho} : sonde {s['k']}/{s['n']} = {s['taux']:.4f} [{s['cp95'][0]:.4f} ; "
            f"{s['cp95'][1]:.4f}] ; famille U {f['k']}/{f['n']} [{f['cp95'][0]:.4f} ; {f['cp95'][1]:.4f}] ; nul A {a['k']}/{a['n']} = "
            f"{a['taux']:.4f} [{a['cp95'][0]:.4f} ; {a['cp95'][1]:.4f}] ; q95 moy. {d['q95_moyen']:.4f} ; aire moy. {d['aire_moyenne']:.4f}")
    if rem:
        lignes_txt.append("")
        for cle, lignes in rem["directs"].items():
            n, theta, rho, compo, i_alt = json.loads(cle)
            base = {l["monde"]: l for l in nul["directs"][cle]}
            ecart = max(max(abs(s["aire"] - b["aire"]), abs(s["q95"] - b["q95"]))
                        for l in lignes for s, b in zip(l["R1"]["sondes"], base[l["monde"]]["R0"]["sondes"]))
            out["controles"].append({"cellule": cle, "ecart_max_aire_q95_reproduits": ecart})
            r0 = resume_direct([base[l["monde"]] for l in lignes], "R0", theta)
            entree = {"n": n, "theta_F": theta, "mondes": len(lignes), "R0_memes_mondes": r0}
            bas_all = {}
            for lec in ("R1", "R2"):
                d = resume_direct(lignes, lec, theta)
                bas = np.array([s["bas"] for l in lignes for s in l[lec]["sondes"]])
                bas_all[lec] = bas
                cond = {}
                for rh in RHOS:
                    q_pl = np.array(nul["planchers"][json.dumps([n, theta, rh])])
                    if rh == 4.0:
                        q_pl = np.vstack([q_pl, np.array([[s["q95"] for s in l["R0"]["sondes"]] for l in nul["directs"][cle]])])
                    cond[str(rh)] = conditionnel(bas, q_pl, rng)
                entree[lec] = {"direct": d, "conditionnel": cond, "apparie_R0": apparie(lignes, lec, [base[l["monde"]] for l in lignes], "R0")}
            # même sous-ensemble, R0 conditionnel
            bas0 = np.array([s["bas"] for l in lignes for s in base[l["monde"]]["R0"]["sondes"]])
            entree["R0_memes_mondes_conditionnel"] = {}
            for rh in RHOS:
                q_pl = np.array(nul["planchers"][json.dumps([n, theta, rh])])
                if rh == 4.0:
                    q_pl = np.vstack([q_pl, np.array([[s["q95"] for s in l["R0"]["sondes"]] for l in nul["directs"][cle]])])
                entree["R0_memes_mondes_conditionnel"][str(rh)] = conditionnel(bas0, q_pl, rng)
            entree["bas_moyen"] = {"R0": float(bas0.mean()), "R1": float(bas_all["R1"].mean()), "R2": float(bas_all["R2"].mean())}
            out["remedes"].append(entree)
            lignes_txt.append(f"remèdes n={n} theta_F={theta:.2f} ({len(lignes)} mondes, mêmes données et mêmes graines que R0 ;"
                              f" écart max. aire/q95 reproduits {ecart:.1e}) ; borne basse moy. R0 {entree['bas_moyen']['R0']:.4f},"
                              f" R1 {entree['bas_moyen']['R1']:.4f}, R2 {entree['bas_moyen']['R2']:.4f}")
            for lec, d in (("R0", r0), ("R1", entree["R1"]["direct"]), ("R2", entree["R2"]["direct"])):
                s, f, a = d["sonde_au_dessus"], d["famille_U"], d["nul_A_borne_seule"]
                cond = entree["R0_memes_mondes_conditionnel"] if lec == "R0" else entree[lec]["conditionnel"]
                lignes_txt.append(
                    f"   {lec} : direct sonde {s['k']}/{s['n']} [{s['cp95'][0]:.4f} ; {s['cp95'][1]:.4f}] ; famille {f['k']}/{f['n']} ;"
                    f" nul A {a['k']}/{a['n']} = {a['taux']:.4f} [{a['cp95'][0]:.4f} ; {a['cp95'][1]:.4f}] ; conditionnel rho=4 sonde "
                    f"{cond['4.0']['sonde']:.4f} [{cond['4.0']['sonde_ic95'][0]:.4f} ; {cond['4.0']['sonde_ic95'][1]:.4f}] famille "
                    f"{cond['4.0']['famille']:.4f} ; rho=1 sonde {cond['1.0']['sonde']:.4f} famille {cond['1.0']['famille']:.4f}"
                    + (f" ; apparié à R0 : R0 seul {entree[lec]['apparie_R0']['a_non_b_oui']}, {lec} seul "
                       f"{entree[lec]['apparie_R0']['a_oui_b_non']}" if lec != "R0" else ""))
    if pui:
        lignes_txt.append("")
        for cle, lignes in pui["directs"].items():
            n, theta, rho, compo, i_alt = json.loads(cle)
            alt = pui["alternatives"][f"{n}:{theta}"]
            entree = {"n": n, "theta_F": theta, "alternative": alt, "mondes": len(lignes)}
            txt = f"puissance n={n} theta_F={theta:.2f} aire vraie {alt['aire_vraie']:.4f} ({len(lignes)} mondes) :"
            for lec in ("R0", "R1", "R2"):
                d = resume_direct(lignes, lec, theta)          # « nul A » se lit ici P(borne basse > theta_F)
                bas = np.array([s["bas"] for l in lignes for s in l[lec]["sondes"]])
                cond = {}
                for rh in RHOS:
                    q_pl = np.array(nul["planchers"][json.dumps([n, theta, rh])])
                    if rh == 4.0:
                        q_pl = np.vstack([q_pl, np.array([[s["q95"] for s in l["R0"]["sondes"]]
                                                          for l in nul["directs"][json.dumps([n, theta, 4.0, 'propre', 0])]])])
                    cond[str(rh)] = conditionnel(bas, q_pl, rng, b=500)
                entree[lec] = {"direct": d, "conditionnel": cond,
                               "apparie_R0": apparie(lignes, "R0", lignes, lec) if lec != "R0" else None}
                s = d["sonde_au_dessus"]
                txt += (f" {lec} direct {s['taux']:.3f} [{s['cp95'][0]:.3f} ; {s['cp95'][1]:.3f}], seuil fixe "
                        f"{d['nul_A_borne_seule']['taux']:.3f}, cond. rho=1 {cond['1.0']['sonde']:.3f}"
                        + (f" (perdues/gagnées vs R0 : {entree[lec]['apparie_R0']['a_oui_b_non']}/{entree[lec]['apparie_R0']['a_non_b_oui']})"
                           if lec != "R0" else "") + " ;")
            out["puissance"].append(entree)
            lignes_txt.append(txt)
    out["texte"] = lignes_txt
    ecrire(out, sortie)
    print("\n".join(lignes_txt))


def ecrire(res: dict, sortie: str) -> None:
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    racine, phase = sys.argv[1], sys.argv[2]
    charger(racine)
    if phase == "nul" and len(sys.argv) == 4:
        phase_nul(racine, sys.argv[3])
    elif phase == "remedes" and len(sys.argv) == 5:
        phase_remedes(racine, sys.argv[3], sys.argv[4])
    elif phase == "puissance" and len(sys.argv) == 6:
        phase_puissance(racine, sys.argv[3], sys.argv[4], sys.argv[5])
    elif phase == "rapport" and len(sys.argv) == 7:
        phase_rapport(racine, sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    else:
        sys.exit(__doc__)
