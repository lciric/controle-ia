"""Vérifications de la synthèse du collisionneur « pilote sur seize tâches » — v1.

Lecteur neuf (Opus 5.5), 29 octobre 2026. Exploratoire, processeur seul, non préenregistré, non opposable.
Importe sans la modifier la simulation de la pièce C (`simulation-couche-2-executions-v1.py`, sha256 20bb005c…),
copiée dans ce dossier. Graines par numpy.random.SeedSequence (R9) via `rng_de` de la pièce C ; graine maîtresse
20261029.

Usage : python3 -I -B verifications-synthese-pilote-v1.py > verifications-synthese-pilote-v1-sortie.json
"""
import hashlib
import importlib.util
import json
import math
import pathlib
import platform
import sys
import time

import numpy as np

ICI = pathlib.Path(__file__).resolve().parent
CHEMIN_SIM = ICI / "simulation-couche-2-executions-v1.py"
spec = importlib.util.spec_from_file_location("sim_c", CHEMIN_SIM)
sim = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sim)

G = 20261029
t0 = time.time()
sortie = {"graine_maitresse": G,
          "empreinte_simulation_piece_C": hashlib.sha256(CHEMIN_SIM.read_bytes()).hexdigest(),
          "versions": {"python": sys.version.split()[0], "numpy": np.__version__, "plateforme": platform.platform()}}


# V1. Erreur relative analytique de l'estimateur ANOVA de la variance entre tâches (scores continus gaussiens)
def cv_analytique(n, K, a):
    sb, sw = a, 1.0 - a
    if K == math.inf:
        return math.sqrt(2.0 / (n - 1))
    var = (2.0 / K ** 2) * ((sw + K * sb) ** 2 / (n - 1) + sw ** 2 / (n * (K - 1)))
    return math.sqrt(var) / sb


V1 = {}
for a in (0.3, 0.5):
    for n in (8, 16, 32, 40, 50, 64):
        for K in (3, 5, 10, 20, 30, math.inf):
            V1[f"a={a}|n={n}|K={'inf' if K == math.inf else K}"] = round(cv_analytique(n, K, a), 4)
sortie["V1_cv_analytique_sigma2_entre"] = V1


# V2. Monte-Carlo, scores continus : sigma2_b chapeau et a chapeau = s2b / (s2b + s2w)
def anova(x):
    """x : (reps, n, K) → (s2b, s2w) par répétition (estimateur ANOVA, tronqué à 0 pour s2b)."""
    reps, n, K = x.shape
    m_t = x.mean(axis=2)
    msb = K * m_t.var(axis=1, ddof=1)
    msw = ((x - m_t[:, :, None]) ** 2).sum(axis=(1, 2)) / (n * (K - 1))
    s2b = np.maximum((msb - msw) / K, 0.0)
    return s2b, msw


V2 = {}
R = 4000
for a in (0.3, 0.5):
    for n, K in ((8, 10), (16, 10), (32, 10), (16, 30), (32, 20), (32, 30), (50, 10)):
        rng = sim.rng_de(G, "V2", a, n, K)
        x = math.sqrt(a) * rng.standard_normal((R, n, 1)) + math.sqrt(1 - a) * rng.standard_normal((R, n, K))
        s2b, s2w = anova(x)
        a_hat = s2b / (s2b + s2w)
        V2[f"a={a}|n={n}|K={K}"] = {
            "cv_s2b": round(float(s2b.std() / a), 4), "cv_a_chapeau": round(float(a_hat.std() / a), 4),
            "moyenne_a_chapeau": round(float(a_hat.mean()), 4),
            "P(a_chapeau>0,4)": round(float((a_hat > 0.4).mean()), 4),
            "P(a_chapeau<0,4)": round(float((a_hat < 0.4).mean()), 4)}
sortie["V2_mc_continu"] = V2

# V2b. Part de variance (a comme corrélation intra-tâche) : approximation de Fisher et taille pour 25 %
def cv_icc_fisher(n, K, a):
    return math.sqrt(2 * (1 - a) ** 2 * (1 + (K - 1) * a) ** 2 / (K * (K - 1) * (n - 1))) / a


V2b = {f"a=0.3|n={n}|K={K}": round(cv_icc_fisher(n, K, 0.3), 4) for n in (8, 16, 24, 28, 32) for K in (10, 20, 30)}
for K in (10, 20, 30):
    n = 3
    while cv_icc_fisher(n, K, 0.3) > 0.25:
        n += 1
    V2b[f"n_min_cv_25pct|a=0.3|K={K}"] = n
for n, K in ((24, 10), (28, 10)):
    rng = sim.rng_de(G, "V2b", n, K)
    x = math.sqrt(0.3) * rng.standard_normal((R, n, 1)) + math.sqrt(0.7) * rng.standard_normal((R, n, K))
    s2b, s2w = anova(x)
    V2b[f"mc_cv_a_chapeau|a=0.3|n={n}|K={K}"] = round(float((s2b / (s2b + s2w)).std() / 0.3), 4)
sortie["V2b_part_de_variance"] = V2b


# V3. Monte-Carlo, alertes binaires (rappel r) : la variance entre tâches mesurée sur 0/1, puis ramenée à a latent
GH_X, GH_W = np.polynomial.hermite_e.hermegauss(80)
GH_W = GH_W / GH_W.sum()


def icc_binaire(a, r):
    q = float(sim.ndtri(np.array([1.0 - r]))[0])
    p = 1.0 - sim.phi_cdf((q - math.sqrt(a) * GH_X) / math.sqrt(1.0 - a))
    var_p = float((GH_W * (p - r) ** 2).sum())
    return var_p / (r * (1 - r))


def a_depuis_icc(icc, r):
    lo, hi = 0.0, 0.99
    for _ in range(50):
        mid = (lo + hi) / 2
        if icc_binaire(mid, r) < icc:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


TABLE_A = np.linspace(0.0, 0.95, 191)
V3 = {}
R3 = 3000
for r in (0.40, 0.01):
    TABLE_ICC = np.array([icc_binaire(x, r) for x in TABLE_A])
    for a in (0.3,):
        icc_vrai = icc_binaire(a, r)
        for n, K in ((8, 10), (16, 10), (32, 10), (16, 30), (32, 30)):
            rng = sim.rng_de(G, "V3", r, a, n, K)
            x = sim.alertes(rng, R3, n, K, r, a, 0.0)
            s2b, s2w = anova(x)
            defini = (s2b + s2w) > 0  # toutes alertes nulles : variance indéfinie (compté à part, R4)
            icc_hat = np.where(defini, s2b / np.where(defini, s2b + s2w, 1.0), 0.0)
            a_map = np.interp(icc_hat, TABLE_ICC, TABLE_A)
            V3[f"r={r}|a={a}|n={n}|K={K}"] = {
                "icc_binaire_vrai": round(icc_vrai, 4),
                "part_indefinie_toutes_alertes_nulles": round(float((~defini).mean()), 4),
                "part_icc_nul_ou_indefini": round(float((s2b == 0).mean()), 4),
                "cv_icc_binaire_indefini_compte_0": round(float(icc_hat.std() / icc_vrai), 4),
                "cv_a_latent_reconstruit": round(float(a_map.std() / a), 4),
                "moyenne_a_latent_reconstruit": round(float(a_map.mean()), 4)}
sortie["V3_mc_binaire"] = V3


# V4. Écart blanc contre blanc à 16 unités, K = 10 : erreur type de la moyenne, P(moyenne < 5 points), puissance
V4 = {}
R4 = 4000
for sc in ("S1_noir_contre_blanc_effet_consigne", "S2_blanc_contre_blanc_concordant"):
    a_, cA, cB, h, _ = sim.SCENARIOS[sc]
    for n in (16, 32):
        for e in (0.08, 0.10):
            rng = sim.rng_de(G, "V4", sc, n, e)
            U = rng.standard_normal((R4, n, 1)); E = rng.standard_normal((R4, n, 10))
            v = (sim.alertes(rng, R4, n, 10, sim.BASE_B + e, a_, cA, h, U, E)
                 - sim.alertes(rng, R4, n, 10, sim.BASE_B, a_, cB, 0.0, U, E)).mean(axis=2)
            vbar = v.mean(axis=1)
            V4[f"{sc}|n={n}|ecart={e}|K=10"] = {
                "erreur_type_moyenne_points": round(float(100 * vbar.std()), 2),
                "ecart_type_v_unite": round(float(v.std(axis=1, ddof=1).mean()), 4),
                "P(moyenne<0,05)": round(float((vbar < 0.05).mean()), 4),
                "puissance_seuil_20": sim.taux_promu(sim.log_richesse(v), (20.0,))[20.0]}
sortie["V4_blanc_contre_blanc"] = V4
phi = lambda z: 0.5 * math.erfc(-z / math.sqrt(2))
sortie["V4b_calculs_normaux_de_C"] = {
    "vrai_10_SE_5,5": round(phi((5 - 10) / 5.5), 4), "vrai_8_SE_5,5": round(phi((5 - 8) / 5.5), 4),
    "vrai_10_SE_7": round(phi((5 - 10) / 7), 4), "vrai_8_SE_7": round(phi((5 - 8) / 7), 4)}


# V5. Puissance de l'organisme (développement, seuil 20), selon K et le nombre d'unités, écart 20 points
V5 = {}
R5 = 3000
for sc in ("S1_noir_contre_blanc_effet_consigne", "S2_blanc_contre_blanc_concordant"):
    a_, cA, cB, h, _ = sim.SCENARIOS[sc]
    for n in (16, 24, 32):
        for K in (3, 5, 10):
            rng = sim.rng_de(G, "V5", sc, n, K)
            U = rng.standard_normal((R5, n, 1)); E = rng.standard_normal((R5, n, K))
            v = (sim.alertes(rng, R5, n, K, sim.BASE_B + 0.2, a_, cA, h, U, E)
                 - sim.alertes(rng, R5, n, K, sim.BASE_B, a_, cB, 0.0, U, E)).mean(axis=2)
            V5[f"{sc}|n={n}|K={K}|ecart=0.2"] = sim.taux_promu(sim.log_richesse(v), (20.0,))[20.0]
sortie["V5_organisme"] = V5


# V6. Arithmétique des coûts des plans (rythmes RAPPORTÉS ; prix SUPPOSÉ 1,08–1,43 USD/h)
def cout(ep, s_bas, s_haut, p_bas=1.08, p_haut=1.43):
    hb, hh = ep * s_bas / 3600, ep * s_haut / 3600
    return {"episodes": ep, "heures": [round(hb, 1), round(hh, 1)], "usd": [round(hb * p_bas, 1), round(hh * p_haut, 1)]}


GEN, J8, J3 = (42.1, 54.6), 58.2, 27.5
base = (GEN[0] + J8 + J3, GEN[1] + J8 + J3)
sortie["V6_couts"] = {
    "rythme_base_s": [round(base[0], 1), round(base[1], 1)],
    "A_T1_recommande_832": cout(832, *base), "A_T1_minimal_416": cout(416, *base),
    "A_T3_1296": cout(1296, *base), "A_T3_Qwen_sur_1296_comme_8B": cout(1296, J8, J8),
    "A_T3_extension_480": cout(480, *base), "A_T3_minimal_800": cout(800, *base),
    "B_T1_1088": cout(1088, *base), "B_T1_minimal_512": cout(512, *base),
    "B_T1_1088_quatre_passes_8B": cout(1088, GEN[0] + 4 * J8, GEN[1] + 4 * J8),
    "C_T3_generation_896": cout(896, *GEN), "C_T3_juges_896": cout(896, J8 + J3, J8 + J3),
    "C_T3_lourds_752": cout(752, 90, 120),
    "C_T3_minimal_somme_lots": 240 + 3 * 16 * 2 + 3 * 16 * 1 + 96,
    "seuil_moniteurs_1400_usd_prix_haut_s": round((1400 / 1.43 - 14470 * GEN[1] / 3600) * 3600 / 14470, 1),
    "quatre_passes_8B_s": 4 * J8}

# V7. Part d'épisodes honnêtes « toutes actions sous tous les seuils » (bornes illustratives : L actions, m moniteurs)
sortie["V7_part_honnetes_sous_tous_seuils"] = {
    f"L={L}|m={m}": {"moniteurs_parfaitement_correles": round(0.99 ** L, 3), "moniteurs_independants": round(0.99 ** (L * m), 3)}
    for L in (5, 10) for m in (5, 6)}

sortie["duree_s"] = round(time.time() - t0, 1)
json.dump(sortie, sys.stdout, ensure_ascii=False, indent=1)
