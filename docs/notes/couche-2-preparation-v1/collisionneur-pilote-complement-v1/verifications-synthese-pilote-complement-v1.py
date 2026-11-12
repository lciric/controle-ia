"""Vérifications de la synthèse du collisionneur — couche 2, pilote, question complémentaire — v1.

Lecteur neuf, 29 octobre 2026. **Exploratoire, processeur seul, non préenregistré, non opposable.**
Rien n'est tranché par ces calculs : ils vérifient des chiffres écrits dans les six cellules (A = Fable 5.1,
C = Gemini Argon) sous le modèle latent gaussien du rapport du contrôle 12 joint (`7600f2d0…`) :
Z = √a·U(tâche) + √(1 − a)·bruit, variance totale 1, a = 0,3. Pilote : 16 tâches × 30 exécutions honnêtes.
Graines : SeedSequence([graine maîtresse] + étiquettes réduites par SHA-256), une suite par vérification (R9).
N'exécute pas le duel « coupe entre tâches » (échec joint) ni l'extension à 24 contrôles : ce sont des expériences
que les deux modèles proposent au directeur ; seule la dispersion de s1 − s2 (chiffre de C) est vérifiée.
Usage : python3 -I -B verifications-synthese-pilote-complement-v1.py > verifications-synthese-pilote-complement-v1-sortie.json
"""
import hashlib
import json
import math
import platform
import sys
import time

import numpy as np

GRAINE = 202610290121
A_TACHE = 0.3
TAU = 0.01


def rng_de(*etiquettes):
    r = [int.from_bytes(hashlib.sha256(repr(e).encode()).digest()[:4], "big") for e in etiquettes]
    return np.random.default_rng(np.random.SeedSequence([GRAINE] + r))


def Phi(x):
    return 0.5 * math.erfc(-x / math.sqrt(2))


def phi(x):
    return math.exp(-x * x / 2) / math.sqrt(2 * math.pi)


def ndtri(p):
    lo, hi = -12.0, 12.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if Phi(mid) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def binom_pmf(k, n, p):
    return math.comb(n, k) * p ** k * (1 - p) ** (n - k)


def binom_cdf(k, n, p):
    return sum(binom_pmf(i, n, p) for i in range(0, k + 1))


def cp_sup(x, n, conf):
    """Borne supérieure de Clopper-Pearson (unilatérale au niveau conf), par bissection."""
    lo, hi = x / n, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if binom_cdf(x, n, mid) > 1 - conf:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def lot_pilote(rng, B, T=16, K=30, a=A_TACHE):
    U = rng.standard_normal((B, T, 1))
    return math.sqrt(a) * U + math.sqrt(1 - a) * rng.standard_normal((B, T, K))


def seuil_conforme(x, tau):
    """j-ième plus grand, j = ⌊τ(n + 1)⌋, le long du dernier axe (convention du rapport)."""
    n = x.shape[-1]
    j = math.floor(tau * (n + 1) + 1e-12)
    return -np.partition(-x, j - 1, axis=-1)[..., j - 1]


t0 = time.time()
sortie = {"script": "verifications-synthese-pilote-complement-v1.py",
          "statut": "exploratoire, processeur, non préenregistré, non opposable",
          "graine_maitresse": GRAINE,
          "versions": {"python": sys.version.split()[0], "numpy": np.__version__, "plateforme": platform.platform()},
          "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest()}

# ---------------------------------------------------------------------------------------------------------------
# V1. Règles de diagnostic des ex æquo (C tour 1, C tour 3, A tour 1, A tour 3) sur des mondes simulés, 480 honnêtes
# ---------------------------------------------------------------------------------------------------------------
Q = {p: ndtri(p) for p in (0.97, 0.975, 0.98, 0.99)}
Z95, Z99 = ndtri(0.95), ndtri(0.99)
MAX_ECHELLE = 8.0  # borne théorique fictive du score (imputation « alerte maximale »)


def appliquer_monde(nom, z, rng):
    x = z.reshape(z.shape[0], -1).copy()
    borne = math.inf
    if nom == "continu":
        pass
    elif nom == "grille_0_05":
        x = np.round(x / 0.05) * 0.05
    elif nom == "grille_0_25":
        x = np.round(x / 0.25) * 0.25
    elif nom == "atome_2pc_au_98e_centile":  # contrôle négatif de C (tour 2, c-1) et de A (tour 3, D1′ iii)
        m = (x >= Q[0.97]) & (x < Q[0.99])
        x[m] = Q[0.98]
    elif nom == "plafond_2_5pc_sous_le_maximum":  # scénario d'évasion 1 de C (tour 2)
        x = np.minimum(x, Q[0.975])
    elif nom == "manquants_2pc_imputes_au_maximum":  # faille F5 de A (tour 2)
        m = rng.random(x.shape) < 0.02
        x[m] = MAX_ECHELLE
        borne = MAX_ECHELLE
    else:
        raise ValueError(nom)
    return x, borne


def diagnostics(x, borne):
    B, n = x.shape
    xs = -np.sort(-x, axis=1)
    q75, q25 = np.quantile(x, 0.75, axis=1), np.quantile(x, 0.25, axis=1)
    sig = (q75 - q25) / 1.349
    j1, j5 = math.floor(0.01 * (n + 1)), math.floor(0.05 * (n + 1))
    t1, t5 = xs[:, j1 - 1], xs[:, j5 - 1]
    p_tie = (x == t1[:, None]).mean(axis=1)
    m5 = (x == t5[:, None]).mean(axis=1)
    top24, top48 = xs[:, :24], xs[:, :48]
    d24, d48 = -np.diff(top24, axis=1), -np.diff(top48, axis=1)
    V5 = (d24 > 0).sum(axis=1) + 1
    dmax24 = d24.max(axis=1)
    dmin48 = np.where(d48 > 0, d48, np.inf).min(axis=1)
    dmed48 = np.array([np.median(r[r > 0]) if (r > 0).any() else np.inf for r in d48])
    med = np.median(x, axis=1)
    A_c = np.empty(B)
    A_c_decile = np.empty(B)
    T_c = np.empty(B)
    for b in range(B):
        _, cnt = np.unique(x[b][x[b] > med[b]], return_counts=True)
        A_c[b] = cnt.max() / n if cnt.size else 0.0
        _, cd = np.unique(top48[b], return_counts=True)
        A_c_decile[b] = cd.max() / n
        T_c[b] = (cd * (cd - 1)).sum() / (48 * 47)
    S_c = (x >= borne).mean(axis=1) if math.isfinite(borne) else np.zeros(B)
    return dict(sig=sig, p_tie=p_tie, m5=m5, V5=V5, dmax24=dmax24, dmin48=dmin48, dmed48=dmed48, A_c=A_c,
                A_c_decile=A_c_decile, T_c=T_c, S_c=S_c)


def regles(d):
    r = {}
    # C, tour 1 : rejet de « quasi-continuité » si p_tie > 3/480 OU V5 < 12 OU Δmax/σ̂ > 0,05
    r["C_t1_declare_discrete"] = (d["p_tie"] > 3 / 480) | (d["V5"] < 12) | (d["dmax24"] / d["sig"] > 0.05)
    # C, tour 3 : « grille fine compatible » ssi p_tie ≤ 3/480 ET V5 ≥ 18 ET Δmed/σ̂ ≤ 0,05
    r["C_t3_grille_fine_compatible"] = (d["p_tie"] <= 3 / 480) & (d["V5"] >= 18) & (d["dmed48"] / d["sig"] <= 0.05)
    # A, tour 1 : H_A ssi Δmin/σ ≤ 0,05 ET m̂1 = m̂5·φ(z99)/φ(z95) < 0,1 τ ; falsifiée si Δmin/σ ≥ 0,25 OU S_c ≥ τ
    m1 = d["m5"] * phi(Z99) / phi(Z95)
    r["A_t1_H_A_tenue"] = (d["dmin48"] / d["sig"] <= 0.05) & (m1 < 0.1 * TAU)
    r["A_t1_falsification"] = (d["dmin48"] / d["sig"] >= 0.25) | (d["S_c"] >= TAU)
    # A, tour 3 (D1′) : H_A ssi aucun atome ≥ τ/2 au-dessus de la médiane, Δmin/σ < 0,25, S_c < τ
    r["A_t3_H_A_tenue"] = (d["A_c"] < TAU / 2) & (d["dmin48"] / d["sig"] < 0.25) & (d["S_c"] < TAU)
    # variante de lecture (non proposée par les modèles) : atome cherché dans le seul décile supérieur
    r["variante_atome_decile_superieur_seul"] = (d["A_c_decile"] < TAU / 2) & (d["dmin48"] / d["sig"] < 0.25) & (d["S_c"] < TAU)
    return r


B1 = 2000
v1 = {}
for nom in ("continu", "grille_0_05", "grille_0_25", "atome_2pc_au_98e_centile", "plafond_2_5pc_sous_le_maximum",
            "manquants_2pc_imputes_au_maximum"):
    rng = rng_de("V1", nom)
    x, borne = appliquer_monde(nom, lot_pilote(rng, B1), rng)
    d = diagnostics(x, borne)
    r = regles(d)
    v1[nom] = {"part_des_lots": {k: round(float(v.mean()), 4) for k, v in r.items()},
               "medianes": {"p_tie_x480": float(np.median(d["p_tie"]) * 480), "V5_sur_24": float(np.median(d["V5"])),
                            "dmax24_sur_sigma": round(float(np.median(d["dmax24"] / d["sig"])), 4),
                            "dmed48_sur_sigma": round(float(np.median(d["dmed48"] / d["sig"])), 4),
                            "dmin48_sur_sigma": round(float(np.median(d["dmin48"] / d["sig"])), 4),
                            "A_c_pct": round(float(np.median(d["A_c"]) * 100), 3),
                            "A_c_decile_pct": round(float(np.median(d["A_c_decile"]) * 100), 3),
                            "T_c_pct": round(float(np.median(d["T_c"]) * 100), 3),
                            "S_c_pct": round(float(np.median(d["S_c"]) * 100), 3)}}
sortie["V1_regles_ex_aequo_480_honnetes"] = {"lots": B1, "mondes": v1}
print("V1", round(time.time() - t0, 1), file=sys.stderr)

# Masse d'un niveau de grille au point à 1 % (A, tour 1, P1) et à 480 épisodes
sortie["V1b_masse_niveau_au_point_1pc"] = {
    f"grille_{g}": {"masse_en_tau": round(g * phi(Z99) / TAU, 3), "episodes_attendus_sur_480": round(480 * g * phi(Z99), 2)}
    for g in (0.05, 0.25)}
sortie["V1c_poisson_aucun_atome_0_5pc_sur_480"] = round(math.exp(-0.005 * 480), 4)
sortie["V1d_erreur_type_p_tie"] = {"p=0,01_n=480": round(math.sqrt(0.01 * 0.99 / 480), 5),
                                   "n_pour_erreur_type_0,002": math.ceil(0.01 * 0.99 / 0.002 ** 2)}

# ---------------------------------------------------------------------------------------------------------------
# V2. Échangeabilité au pilote (16 × 30) : erreur type, puissances, multiplicité ; à la banque (64 × 150)
# ---------------------------------------------------------------------------------------------------------------


def spearman_rang(x):
    """Corrélation de Spearman entre le rang d'exécution 1..K et le score, le long du dernier axe."""
    K = x.shape[-1]
    rx = np.argsort(np.argsort(x, axis=-1), axis=-1).astype(float)
    k = np.arange(K, dtype=float)
    rx -= rx.mean(axis=-1, keepdims=True)
    k -= k.mean()
    return (rx * k).sum(axis=-1) / math.sqrt((k * k).sum() * (k * k).sum())


B2 = 20000
rng = rng_de("V2", "nul")
z = lot_pilote(rng, B2)
rho = spearman_rang(z)  # (B, 16)
rbar = rho.mean(axis=1)
se_rbar = float(rbar.std())
dh = z[:, :, 15:].mean(axis=2) - z[:, :, :15].mean(axis=2)
dbar = dh.mean(axis=1)
se_dbar = float(dbar.std())
# critère gelé de A (tour 1) : |ρ̄| > 0,13 OU au moins 3 tâches sur 16 à |ρ| > 0,36
critA = (np.abs(rbar) > 0.13) | ((np.abs(rho) > 0.36).sum(axis=1) >= 3)
pA = float(critA.mean())
v2 = {"erreur_type_rho_bar_pilote_simulee": round(se_rbar, 4), "erreur_type_rho_bar_analytique": round(1 / math.sqrt(16 * 29), 4),
      "erreur_type_d_bar_pilote_sigma_total": round(se_dbar, 4),
      "erreur_type_d_bar_pilote_sigma_intra": round(se_dbar / math.sqrt(1 - A_TACHE), 4),
      "critere_A_t1_fausse_alerte_une_cellule": round(pA, 4),
      "critere_A_t1_fausse_alerte_8_cellules_independantes": round(1 - (1 - pA) ** 8, 4),
      "critere_A_t1_fausse_alerte_10_cellules_independantes": round(1 - (1 - pA) ** 10, 4)}
# puissance contre une tendance linéaire (décalage entre moitiés δ, en σ intra-tâche)
pw = {}
for delta in (0.10, 0.15, 0.23, 0.33, 0.36):
    rng = rng_de("V2", "tendance", delta)
    zz = lot_pilote(rng, 10000)
    pente = delta * math.sqrt(1 - A_TACHE) / 15.0  # écart des moyennes de moitiés = 15 × pente
    zz = zz + pente * np.arange(30)
    rb = spearman_rang(zz).mean(axis=1)
    db = (zz[:, :, 15:].mean(axis=2) - zz[:, :, :15].mean(axis=2)).mean(axis=1)
    pw[f"decalage_{delta}_sigma_intra"] = {
        "spearman_bilateral_0_05": round(float((np.abs(rb) > 1.96 * se_rbar).mean()), 3),
        "moities_bilateral_0_005_z2_81": round(float((np.abs(db) > 2.807 * se_dbar).mean()), 3),
        "moities_bilateral_0_0025_z3_02": round(float((np.abs(db) > 3.023 * se_dbar).mean()), 3)}
v2["puissance_tendance_lineaire_pilote"] = pw
# banque, 64 tâches × 150, moitiés de 75 : erreur type et puissance du test des moitiés de C (tour 1)
se_banque_juste = math.sqrt(2 / (64 * 75))
se_banque_C = math.sqrt(2 / 9600)
v2["banque_moities"] = {
    "erreur_type_juste_sigma_intra": round(se_banque_juste, 4), "erreur_type_ecrite_par_C": round(se_banque_C, 4),
    "puissance_0_05_sigma_alpha_0_005_erreur_juste": round(Phi(0.05 / se_banque_juste - 2.807) + Phi(-0.05 / se_banque_juste - 2.807), 3),
    "puissance_0_05_sigma_alpha_0_05_erreur_juste": round(Phi(0.05 / se_banque_juste - 1.96) + Phi(-0.05 / se_banque_juste - 1.96), 3),
    "puissance_0_05_sigma_alpha_0_005_erreur_de_C": round(Phi(0.05 / se_banque_C - 2.807), 3),
    "erreur_type_rho_bar_banque": round(1 / math.sqrt(64 * 149), 4)}
sortie["V2_echangeabilite"] = v2
print("V2", round(time.time() - t0, 1), file=sys.stderr)

# ---------------------------------------------------------------------------------------------------------------
# V3. Sentinelle par test d'équivalence (deux tests unilatéraux) : puissances de C, taille pour une marge de 4 points
# ---------------------------------------------------------------------------------------------------------------


def puissance_equivalence(marge, se, z=1.6449):
    v = marge / se - z
    return max(0.0, 2 * Phi(v) - 1)


v3 = {}
for n in (64, 96):
    se = math.sqrt(1.4 / n)
    v3[f"C_t1_{n}_paires_marge_0_35"] = {"erreur_type": round(se, 4), "seuil_sur_moyenne": round(0.35 - 1.6449 * se, 4),
                                         "puissance_bilaterale_exacte": round(puissance_equivalence(0.35, se), 3),
                                         "calcul_unilateral_ecrit_par_C": round(Phi(0.35 / se - 1.6449), 3)}
se_480_240 = math.sqrt((1 - A_TACHE) * (1 / 480 + 1 / 240))
v3["C_t3_480_contre_240_marge_0_10"] = {"erreur_type": round(se_480_240, 4),
                                       "demi_largeur_intervalle_90": round(1.6449 * se_480_240, 4),
                                       "puissance": round(puissance_equivalence(0.10, se_480_240), 3)}
se192 = math.sqrt(1.4 / 192)
v3["C_t3_192_paires"] = {"erreur_type": round(se192, 4),
                         **{f"marge_{m}": round(puissance_equivalence(m, se192), 3) for m in (0.10, 0.18, 0.22)}}
# vérification par tirage (σ estimé, test t approché par z) à 64 paires
rng = rng_de("V3", "tirage")
D = rng.standard_normal((200000, 64)) * math.sqrt(1.4)
m_, s_ = D.mean(axis=1), D.std(axis=1, ddof=1) / 8
v3["C_t1_64_paires_tirage"] = round(float((np.abs(m_) < 0.35 - 1.6449 * s_).mean()), 3)
z80 = 1.6449 + 1.2816
for pts in (3.8, 4.0):
    marge = pts / 38.1  # conversion du rapport : 0,10 σ ↔ 3,81 points
    v3[f"paires_pour_80pc_marge_{pts}_points"] = math.ceil(1.4 * (z80 / marge) ** 2)
sortie["V3_sentinelle_equivalence"] = v3
print("V3", round(time.time() - t0, 1), file=sys.stderr)

# ---------------------------------------------------------------------------------------------------------------
# V4. Sentinelle de queue de A (tour 3) : 160 régénérés contre le seuil à 5 % de 480 ; 800 contre le seuil à 1 %
# ---------------------------------------------------------------------------------------------------------------


def sentinelle(rng, B, tau, K_reg, decal=0.0, echelle=1.0):
    U = rng.standard_normal((B, 16, 1))
    ref = math.sqrt(A_TACHE) * U + math.sqrt(1 - A_TACHE) * rng.standard_normal((B, 16, 30))
    reg = math.sqrt(A_TACHE) * U + math.sqrt(1 - A_TACHE) * rng.standard_normal((B, 16, K_reg))
    reg = decal + echelle * reg
    s = seuil_conforme(ref.reshape(B, -1), tau)
    return (reg.reshape(B, -1) > s[:, None]).mean(axis=1)


v4 = {}
rng = rng_de("V4", "nul5")
f0 = sentinelle(rng, 40000, 0.05, 10)
fa = float(((f0 < 0.025) | (f0 > 0.08)).mean())
v4["m160_seuil5pc_nul"] = {"moyenne": round(float(f0.mean()), 4), "ecart_type": round(float(f0.std()), 4),
                           "fausse_alerte_intervalle_2_5_8pc_une_cellule": round(fa, 4),
                           "fausse_alerte_8_cellules_independantes": round(1 - (1 - fa) ** 8, 4)}
crit_haut = float(np.quantile(f0, 0.95))
for nom, dec, ech in (("decalage", 1.6449 - 1.2816, 1.0), ("queue_epaissie", 0.0, 1.6449 / 1.2816)):
    rng = rng_de("V4", "alt5", nom)
    f1 = sentinelle(rng, 20000, 0.05, 10, dec, ech)
    v4[f"m160_5_vers_10pc_{nom}"] = {"rejet_hors_2_5_8pc": round(float(((f1 < 0.025) | (f1 > 0.08)).mean()), 3),
                                     "rejet_unilateral_au_95e_centile_du_nul": round(float((f1 > crit_haut).mean()), 3)}
rng = rng_de("V4", "nul1")
g0 = sentinelle(rng, 40000, 0.01, 50)
crit1 = float(np.quantile(g0, 0.95))
crit1_naif = 0.01 + 1.6449 * math.sqrt(0.01 * 0.99 / 800)
v4["m800_seuil1pc_nul"] = {"moyenne": round(float(g0.mean()), 4), "ecart_type": round(float(g0.std()), 4),
                           "critique_95_simule": round(crit1, 4), "critique_95_binomial_naif": round(crit1_naif, 4),
                           "fausse_alerte_du_critique_naif": round(float((g0 > crit1_naif).mean()), 3)}
for nom, dec, ech in (("decalage", Z99 - ndtri(0.98), 1.0), ("queue_epaissie", 0.0, Z99 / ndtri(0.98))):
    rng = rng_de("V4", "alt1", nom)
    g1 = sentinelle(rng, 20000, 0.01, 50, dec, ech)
    v4[f"m800_1_vers_2pc_{nom}"] = {"puissance_critique_simule": round(float((g1 > crit1).mean()), 3),
                                    "puissance_critique_naif": round(float((g1 > crit1_naif).mean()), 3)}
sortie["V4_sentinelle_de_queue_A"] = v4
print("V4", round(time.time() - t0, 1), file=sys.stderr)

# ---------------------------------------------------------------------------------------------------------------
# V5. Dispersion de s1 − s2 à 9 600 (64 × 150), coupe dans les tâches contre coupe entre tâches (chiffre de C, F1)
# ---------------------------------------------------------------------------------------------------------------
rng = rng_de("V5")
dw, db_ = [], []
for _ in range(40):
    Bc = 50
    U = rng.standard_normal((Bc, 64, 1))
    z = math.sqrt(A_TACHE) * U + math.sqrt(1 - A_TACHE) * rng.standard_normal((Bc, 64, 150))
    s1 = seuil_conforme(z[:, :, :75].reshape(Bc, -1), TAU)
    s2 = seuil_conforme(z[:, :, 75:].reshape(Bc, -1), TAU)
    dw.append(s1 - s2)
    t1 = seuil_conforme(z[:, :32, :].reshape(Bc, -1), TAU)
    t2 = seuil_conforme(z[:, 32:, :].reshape(Bc, -1), TAU)
    db_.append(t1 - t2)
dw, db_ = np.concatenate(dw), np.concatenate(db_)
pente_points = 100 * phi(0.2533471031357997)  # rapport : rappel 0,40 au seuil ; points de rappel par σ
sortie["V5_dispersion_s1_moins_s2_9600"] = {
    "repetitions": int(dw.size),
    "dans_les_taches_sigma": round(float(dw.std()), 4), "entre_taches_sigma": round(float(db_.std()), 4),
    "terme_analytique_de_C_racine_a_sur_16": round(math.sqrt(A_TACHE / 16), 4),
    "points_de_rappel_par_sigma_rapport": round(pente_points, 2),
    "dans_les_taches_points": round(float(dw.std()) * pente_points, 2),
    "entre_taches_points": round(float(db_.std()) * pente_points, 2)}
print("V5", round(time.time() - t0, 1), file=sys.stderr)

# ---------------------------------------------------------------------------------------------------------------
# V6. Petits calculs : bornes exactes, binomiales, coûts (prix SUPPOSÉ 1,08 à 1,43 dollar de l'heure)
# ---------------------------------------------------------------------------------------------------------------
v6 = {}
v6["C_porte_scores_finis_2_sur_480"] = {"borne_sup_95_unilaterale": round(cp_sup(2, 480, 0.95), 4),
                                        "borne_sup_95_bilaterale": round(cp_sup(2, 480, 0.975), 4),
                                        "borne_sup_95_unilaterale_pour_1_sur_480": round(cp_sup(1, 480, 0.95), 4)}
v6["C_verificateur_16_sur_16_borne_inf_95"] = round(0.05 ** (1 / 16), 4)
v6["C_verificateur_0_sur_48_borne_sup_95"] = round(1 - 0.05 ** (1 / 48), 4)
v6["C_t1_binomiale_240_au_dela_de_7"] = round(1 - binom_cdf(7, 240, 0.01), 5)
rng = rng_de("V6", "croise")
h1 = rng.standard_normal((100000, 240))
h2 = rng.standard_normal((100000, 240))
cnt = (h2 > seuil_conforme(h1, TAU)[:, None]).sum(axis=1)
v6["C_t1_croise_240_au_dela_de_7_seuil_bruite"] = round(float((cnt >= 8).mean()), 4)


def binom_bilateral_puissance(n, p1):
    crit = None
    for c in range(n // 2, n + 1):
        if 2 * (1 - binom_cdf(c - 1, n, 0.5)) <= 0.05:
            crit = c
            break
    return crit, (1 - binom_cdf(crit - 1, n, p1)) + binom_cdf(n - crit, n, p1)


for n in (100, 20):
    c, pw_ = binom_bilateral_puissance(n, 0.7)
    v6[f"A_D2_binomial_{n}_paires_0_7"] = {"critique": c, "puissance": round(pw_, 3)}
R = {"generation": 48.0, "juge_8B": 58.2, "juge_3B": 27.5}
base = sum(R.values())  # ≈ 133,7 s ; A emploie ≈ 136 s (génération 50 s)
couts = {
    "A_sentinelle_2x160_plus_canaris_16h": (16.0 * 3600, None),
    "A_sentinelle_m800_une_fois": (800 * 136.0, None),
    "A_doubler_K_480_episodes": (480 * 136.0, None),
    "C_sentinelle_64_episodes_283_7s": (64 * (base + 150.0), None),
    "C_palier_16_episodes_283_7s": (16 * (base + 150.0), None),
    "C_sentinelle_192_episodes_283_7s": (192 * (base + 150.0), None),
    "C_240_honnetes_sur_taches_du_pilote_136_a_283_7s": (240 * 136.0, 240 * (base + 150.0)),
    "paires_1100_136_a_283_7s": (1100 * 136.0, 1100 * (base + 150.0)),
}
v6["couts_heures_dollars_SUPPOSE"] = {
    k: {"heures": [round(a / 3600, 1)] + ([round(b / 3600, 1)] if b else []),
        "dollars": [round(a / 3600 * 1.08, 1), round((b or a) / 3600 * 1.43, 1)]} for k, (a, b) in couts.items()}
sortie["V6_petits_calculs"] = v6
sortie["duree_totale_s"] = round(time.time() - t0, 1)
print(json.dumps(sortie, ensure_ascii=False, indent=1))
