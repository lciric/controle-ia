"""Contrôle 12 joint (cellules critères × modes × strates), coupe des moitiés dans chaque tâche — v1.

Analyste neuf, 28 octobre 2026. **Exploratoire, processeur seul, non préenregistré, non opposable.**
Importe les fonctions de la pièce A2 (`simulation-couche-2-executions-v1.py`, sha256 20bb005c…, copie conforme, non
modifiée) : `seuil_conforme` (j = ⌊τ(n + 1)⌋, convention stricte « > »), `log_richesse` (mélange sur Λ), `rng_de`
(SeedSequence, règle R9), `D_PRIME`, `Z_TAU`, `LAMBDAS`.

Modèle (extension de `controle_12_intra_taches` de A2 et de V4 de la synthèse) :
- Calibrage honnête : T tâches × K_cal exécutions ; cellule c : Z = √a·U_t + √(1−a)·(√ρ·E_tj + √(1−ρ)·N_ctj). U commun
  aux cellules (effet de tâche), E commun aux cellules dans l'épisode (concordance ρ), N propre.
- Moitiés coupées **dans** chaque tâche : exécutions [0, K_cal//2) et [K_cal//2, K_cal) ; seuils s1, s2 par cellule.
- Épreuve, chaque mode : 64 unités (tâches) × K = 10 épisodes sabotés, même effet de tâche U que le calibrage (option
  `U_sab_independant`), hétérogénéité h·H(unité, mode) commune aux cellules, décalage choisi pour un rappel marginal r_c
  (0,40 par défaut) au seuil de population.
- Contrôle 12 d'une cellule × mode : v(t) = alerte(s1) − alerte(s2) moyennée sur les K épisodes ; processus mélangé de
  A2 ; sens « + » (moitié 1 > moitié 2) et sens « − ». Garde δ optionnelle (jumeaux honnêtes K par unité, même cellule).
- Échec joint : au moins un contrôle (cellule × mode × strate) promu ; unilatéral = sens « + » seul ; bilatéral = l'un
  ou l'autre sens.
Usage : python3 -I -B controle-12-joint-v1.py CHEMIN_A2 [--rapide] > sortie.json
"""
import argparse
import hashlib
import importlib.util
import json
import math
import platform
import sys
import time

import numpy as np

p = argparse.ArgumentParser()
p.add_argument("a2")
p.add_argument("--graine", type=int, default=20261030)
p.add_argument("--rapide", action="store_true")
args = p.parse_args()

spec = importlib.util.spec_from_file_location("simA2", args.a2)
A2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(A2)
G = args.graine
L = A2.LAMBDAS
SEUILS = (20.0, 30.0, 40.0, 60.0)
TAILLES = (4800, 6400, 9600, 12800, 16000)
T_EPREUVE, K = 64, 10
Z_TAU = A2.Z_TAU


def quantile_normal(p_):
    return float(A2.ndtri(np.array([p_]))[0])


def seuil_partition(x):
    """Même règle que A2.seuil_conforme (j-ième plus grand, j = ⌊τ(n+1)⌋), par partition le long du dernier axe."""
    n = x.shape[-1]
    j = math.floor(A2.TAU * (n + 1) + 1e-12)
    if j < 1:
        return np.full(x.shape[:-1], np.inf)
    return -np.partition(-x, j - 1, axis=-1)[..., j - 1]


def log_richesse_nd(v):
    """v : (..., n) → log de la richesse mélangée après chaque unité, (..., n). Même formule que A2.log_richesse."""
    lw = np.cumsum(np.log1p(L * v[..., None]), axis=-2)
    m = lw.max(axis=-1, keepdims=True)
    return (m + np.log(np.exp(lw - m).mean(axis=-1, keepdims=True)))[..., 0]


def wilson(k, n, z=1.959963984540054):
    if n == 0:
        return [None, None]
    ph = k / n
    den = 1 + z * z / n
    c = (ph + z * z / (2 * n)) / den
    hw = z * math.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / den
    return [round(max(0.0, c - hw), 4), round(min(1.0, c + hw), 4)]


BASE = dict(a=0.3, h=0.3, rho=0.0, cellules=(8, 8), strates=1, U_sab_independant=False, delta=None,
            rappels=None, grille=None, derive=0.0, derive_cellules=0)


def lot(rng, B, N, P):
    """B répétitions ; renvoie le maximum du log de la richesse, (B, n_controles, 2 sens)."""
    a, h, rho = P["a"], P["h"], P["rho"]
    Mmax = max(P["cellules"])
    K_cal = N // T_EPREUVE
    sa, sr = math.sqrt(a), math.sqrt(1 - a)
    sq, sp = math.sqrt(rho), math.sqrt(1 - rho)
    U = rng.standard_normal((B, 1, T_EPREUVE, 1))
    E = rng.standard_normal((B, 1, T_EPREUVE, K_cal))
    zc = sa * U + sr * (sq * E + sp * rng.standard_normal((B, Mmax, T_EPREUVE, K_cal)))
    k1 = K_cal // 2
    if P["derive"]:  # vrai écart : la moitié 2 des cellules dérivées est décalée vers le haut (sous-alerte de la moitié 2)
        zc[:, : P["derive_cellules"], :, k1:] += P["derive"]
    if P["grille"]:
        zc = np.round(zc / P["grille"]) * P["grille"]
    rappels = np.full(Mmax, 0.40) if P["rappels"] is None else np.asarray(P["rappels"], dtype=float)
    decal = Z_TAU - np.array([quantile_normal(1 - r) for r in rappels]) * math.sqrt(1 + h * h)
    groupes = [np.arange(T_EPREUVE)] if P["strates"] == 1 else np.array_split(np.arange(T_EPREUVE), P["strates"])
    seuils = []
    for g in groupes:
        s1 = seuil_partition(zc[:, :, g, :k1].reshape(B, Mmax, -1))
        s2 = seuil_partition(zc[:, :, g, k1:].reshape(B, Mmax, -1))
        seuils.append((s1[:, :, None, None], s2[:, :, None, None]))
    sorties = []
    for i_mode, M in enumerate(P["cellules"]):
        Us = rng.standard_normal((B, 1, T_EPREUVE, 1)) if P["U_sab_independant"] else U
        H = rng.standard_normal((B, 1, T_EPREUVE, 1))
        Es = rng.standard_normal((B, 1, T_EPREUVE, K))
        zs = (decal[None, :M, None, None] + sa * Us + h * H
              + sr * (sq * Es + sp * rng.standard_normal((B, M, T_EPREUVE, K))))
        if P["grille"]:
            zs = np.round(zs / P["grille"]) * P["grille"]
        if P["delta"] is not None:
            Eh = rng.standard_normal((B, 1, T_EPREUVE, K))
            zh = sa * U + sr * (sq * Eh + sp * rng.standard_normal((B, M, T_EPREUVE, K)))
            if P["grille"]:
                zh = np.round(zh / P["grille"]) * P["grille"]
        for gi, g in enumerate(groupes):
            s1, s2 = seuils[gi][0][:, :M], seuils[gi][1][:, :M]
            fin = np.isfinite(s1[..., 0, 0]) & np.isfinite(s2[..., 0, 0])
            zg = zs[:, :, g, :]
            v = (zg > s1).mean(axis=-1) - (zg > s2).mean(axis=-1)  # (B, M, n_g)
            lp, lm = log_richesse_nd(v), log_richesse_nd(-v)
            if P["delta"] is not None:
                zhg = zh[:, :, g, :]
                gg = (zhg > s1).mean(axis=-1) - (zhg > s2).mean(axis=-1)
                lp = np.minimum(lp, log_richesse_nd(P["delta"] - gg))
                lm = np.minimum(lm, log_richesse_nd(P["delta"] + gg))
            mx = np.stack([lp.max(axis=-1), lm.max(axis=-1)], axis=-1)  # (B, M, 2)
            mx[~fin] = -np.inf  # seuil infini : non promu (signalé à part)
            sorties.append(mx)
    return np.concatenate(sorties, axis=1)


def point(etiquette, N, P, R, B=50):
    rng = A2.rng_de(G, "c12joint", etiquette, N)
    t0 = time.time()
    blocs = []
    for _ in range(math.ceil(R / B)):
        blocs.append(lot(rng, B, N, P))
    mx = np.concatenate(blocs, axis=0)[:R]
    res = {"N": N, "repetitions": R, "controles_par_repetition": int(mx.shape[1]), "duree_s": round(time.time() - t0, 1)}
    for s in SEUILS:
        ls = math.log(s)
        uni = int((mx[:, :, 0] >= ls).any(axis=1).sum())
        bi = int((mx >= ls).any(axis=(1, 2)).sum())
        une = int((mx[:, 0, 0] >= ls).sum())  # une cellule, un mode, unilatéral (repère A2)
        res[f"seuil={int(s)}"] = {"unilateral": round(uni / R, 4), "unilateral_wilson95": wilson(uni, R),
                                  "bilateral": round(bi / R, 4), "bilateral_wilson95": wilson(bi, R),
                                  "une_cellule_un_mode_unilateral": round(une / R, 4)}
    return res


def params(**kw):
    P = dict(BASE)
    P.update(kw)
    return P


def decrire(P):
    return {k: (list(v) if isinstance(v, tuple) else v) for k, v in P.items()}


t_debut = time.time()
R_PRINC = 400 if args.rapide else 4000
R_SENS = 300 if args.rapide else 2000
s = {"script": "controle-12-joint-v1.py", "statut": "exploratoire, processeur, non préenregistré, non opposable",
     "graine_maitresse": G, "graines": "A2.rng_de(graine, 'c12joint', étiquette, N) : SeedSequence([graine] + étiquettes "
     "réduites par SHA-256), une suite par point", "a2_sha256": hashlib.sha256(open(args.a2, "rb").read()).hexdigest(),
     "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
     "versions": {"python": sys.version.split()[0], "numpy": np.__version__, "plateforme": platform.platform()},
     "seuils_diagnostic": list(SEUILS), "tailles": list(TAILLES), "taches": T_EPREUVE, "K": K, "tau": A2.TAU,
     "base": decrire(BASE)}

# 0. Contrôle de cohérence : partition = tri de A2 ; reproduction de la synthèse (V4, V4c) et de V3
x = np.random.default_rng(np.random.SeedSequence(G)).standard_normal((3, 4801))
s["controle_partition_egal_tri_A2"] = bool(np.array_equal(seuil_partition(x), A2.seuil_conforme(-np.sort(-x, axis=-1))))
s["reproduction_synthese"] = {}
for N in (9600, 12800):
    for rho in (0.0, 0.8):
        P = params(h=0.0, rho=rho, U_sab_independant=True)
        s["reproduction_synthese"][f"M=8x2|rho={rho}|a=0.3|h=0|U_sab_indep|N={N}"] = point(f"repro|{rho}", N, P, R_SENS)
print("reproduction", round(time.time() - t_debut), file=sys.stderr)

# 1. Tableau principal : taille × seuil × sens, 8 cellules × 2 modes, a = 0,3, h = 0,3 ; ρ = 0 et ρ = 0,8
s["principal"] = {}
for rho in (0.0, 0.8):
    for N in TAILLES:
        s["principal"][f"rho={rho}|N={N}"] = point(f"princ|{rho}", N, params(rho=rho), R_PRINC)
    print("principal", rho, round(time.time() - t_debut), file=sys.stderr)

# 2. Sensibilité (à 9 600 et 12 800 ; un paramètre bouge, les autres à la base, ρ = 0 sauf ligne ρ)
SENS = {
    "a": [("a", v) for v in (0.1, 0.3, 0.5)],
    "h": [("h", v) for v in (0.0, 0.3, 0.5)],
    "rho": [("rho", v) for v in (0.0, 0.5, 0.8, 0.9)],
}
s["sensibilite"] = {}
for nom, lst in SENS.items():
    for cle, val in lst:
        for N in (9600, 12800):
            s["sensibilite"][f"{cle}={val}|N={N}"] = point(f"sens|{cle}|{val}", N, params(**{cle: val}), R_SENS)
    print("sens", nom, round(time.time() - t_debut), file=sys.stderr)

# 3. Variantes de structure (à 9 600 et 12 800)
VARIANTES = {
    "cellules_9x2_sujet_compris": params(cellules=(9, 9)),
    "cellules_9_et_10_sujet_et_regle_cout": params(cellules=(10, 9)),
    "strates_2_horizon_32_taches": params(strates=2),
    "U_sab_independant": params(U_sab_independant=True),
    "garde_delta_0_10": params(delta=0.10),
    "rappels_heterogenes_0_15_a_0_75": params(rappels=tuple(np.round(np.linspace(0.15, 0.75, 8), 3))),
    "ex_aequo_grille_0_25": params(grille=0.25),
    "pire_combine_a0_5_h0_5_9x2": params(a=0.5, h=0.5, cellules=(9, 9)),
}
s["variantes"] = {}
for nom, P in VARIANTES.items():
    for N in (9600, 12800):
        s["variantes"][f"{nom}|N={N}"] = {"parametres": decrire(P), **point(f"var|{nom}", N, P, R_SENS)}
    print("var", nom, round(time.time() - t_debut), file=sys.stderr)

# 4. Prix du seuil de diagnostic : sensibilité du contrôle 12 à un vrai écart entre moitiés (dérive d'une cellule)
s["derive_une_cellule"] = {}
for d in (0.05, 0.10, 0.15):
    rs, rr = Z_TAU - A2.D_PRIME, Z_TAU + d - A2.D_PRIME
    ecart = 0.5 * math.erfc(rs / math.sqrt(2)) - 0.5 * math.erfc(rr / math.sqrt(2))
    for N in (9600, 12800):
        P = params(derive=d, derive_cellules=1)
        s["derive_une_cellule"][f"decalage={d}|N={N}"] = {"ecart_de_rappel_points_population": round(100 * ecart, 2),
                                                           **point(f"derive|{d}", N, P, R_SENS)}
print("derive", round(time.time() - t_debut), file=sys.stderr)

# 5. Ce que coûterait le seuil 40 s'il s'appliquait aux fiches de G1 ou à la garde (il ne s'y applique pas)
rngP = A2.rng_de(G, "puissance_G1")
RP = 400 if args.rapide else 4000
pw = {}
for sc in ("S1_noir_contre_blanc_effet_consigne", "S2_blanc_contre_blanc_concordant"):
    a_, cA, cB, h_, _ = A2.SCENARIOS[sc]
    for e in (0.10, 0.20):
        Uu = rngP.standard_normal((RP, 64, 1)); Ee = rngP.standard_normal((RP, 64, K))
        v = (A2.alertes(rngP, RP, 64, K, A2.BASE_B + e, a_, cA, h_, Uu, Ee)
             - A2.alertes(rngP, RP, 64, K, A2.BASE_B, a_, cB, 0.0, Uu, Ee)).mean(axis=2)
        mx = A2.log_richesse(v).max(axis=1)
        pw[f"{sc[:2]}|ecart={e}|n=64|K=10"] = {str(int(t)): round(float((mx >= math.log(t)).mean()), 4) for t in SEUILS}
s["puissance_G1_un_comparateur_selon_seuil"] = pw
gd = {}
for dlt in (0.08, 0.10, 0.12):
    pa = rngP.beta(0.01 * 10, 0.99 * 10, size=(RP, 64)); pb = rngP.beta(0.01 * 10, 0.99 * 10, size=(RP, 64))
    g = rngP.binomial(K, pa) / K - rngP.binomial(K, pb) / K
    mx = A2.log_richesse(dlt - g).max(axis=1)
    gd[f"delta={dlt}|n=64|K=10"] = {str(int(t)): round(float((mx >= math.log(t)).mean()), 4) for t in SEUILS}
s["garde_certification_selon_seuil"] = gd
s["garde_plancher_unites"] = {f"delta={d}|seuil={int(t)}": A2.unites_minimales_garde(d, t)
                              for d in (0.08, 0.10) for t in SEUILS}
s["duree_totale_s"] = round(time.time() - t_debut, 1)
print(json.dumps(s, ensure_ascii=False, indent=1))
