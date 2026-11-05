"""Complément ex æquo du contrôle 12 joint — v1 (copie de controle-12-joint-v1.py jusqu'aux points ; ajoute un bris
d'égalité aléatoire : bruit uniforme sur [0, 0,999·grille) qui garde l'ordre entre niveaux et tire l'ordre dans un niveau).

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
            rappels=None, grille=None, bris=False, cellules_grille=None, derive=0.0, derive_cellules=0)


def discretiser(rng, z, P):
    """Arrondit à la grille les cellules [0, cellules_grille) (toutes si None) ; bris d'égalité aléatoire si demandé."""
    g = P["grille"]
    m = z.shape[1] if P["cellules_grille"] is None else min(P["cellules_grille"], z.shape[1])
    z = z.copy()
    z[:, :m] = np.round(z[:, :m] / g) * g
    if P["bris"]:
        z[:, :m] += rng.uniform(0.0, 0.999 * g, size=z[:, :m].shape)
    return z


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
        zc = discretiser(rng, zc, P)
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
            zs = discretiser(rng, zs, P)
        if P["delta"] is not None:
            Eh = rng.standard_normal((B, 1, T_EPREUVE, K))
            zh = sa * U + sr * (sq * Eh + sp * rng.standard_normal((B, M, T_EPREUVE, K)))
            if P["grille"]:
                zh = discretiser(rng, zh, P)
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
    rng = A2.rng_de(G, "c12joint-exaequo", etiquette, N)
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
R_SENS = 300 if args.rapide else 2000
s = {"script": "controle-12-joint-v1-complement-ex-aequo.py", "statut": "exploratoire, processeur, non préenregistré, non opposable",
     "graine_maitresse": G, "graines": "A2.rng_de(graine, 'c12joint-exaequo', étiquette, N)",
     "a2_sha256": hashlib.sha256(open(args.a2, "rb").read()).hexdigest(),
     "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
     "versions": {"python": sys.version.split()[0], "numpy": np.__version__, "plateforme": platform.platform()},
     "base": decrire(BASE)}
V = {
    "grille_0_25_toutes": params(grille=0.25),
    "grille_0_25_toutes_bris_aleatoire": params(grille=0.25, bris=True),
    "grille_0_05_toutes": params(grille=0.05),
    "grille_0_05_toutes_bris_aleatoire": params(grille=0.05, bris=True),
    "grille_0_25_trois_cellules": params(grille=0.25, cellules_grille=3),
    "grille_0_25_trois_cellules_bris_aleatoire": params(grille=0.25, cellules_grille=3, bris=True),
}
s["ex_aequo"] = {}
for nom, P in V.items():
    for N in (9600, 12800):
        s["ex_aequo"][f"{nom}|N={N}"] = {"parametres": decrire(P), **point(f"exaequo|{nom}", N, P, R_SENS)}
    print(nom, round(time.time() - t_debut), file=sys.stderr)
s["duree_totale_s"] = round(time.time() - t_debut, 1)
print(json.dumps(s, ensure_ascii=False, indent=1))
