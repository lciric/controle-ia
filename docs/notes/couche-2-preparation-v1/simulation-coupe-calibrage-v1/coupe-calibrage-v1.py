"""Coupe des moitiés du calibrage honnête (contrôle 12 joint) : dans les tâches ou entre tâches — v1.

Analyste neuf, 29 octobre 2026. **Exploratoire, processeur seul, non préenregistré, non opposable.**
Part de `controle-12-joint-v1.py` (rapport du contrôle 12 joint) et importe la pièce A2
(`simulation-couche-2-executions-v1.py`, sha256 20bb005c…, lue sur place, non copiée, non modifiée) pour
`rng_de` (SeedSequence, R9), `TAU`, `Z_TAU`, `LAMBDAS`, `ndtri`.

Modèle latent gaussien (celui du rapport) :
- Calibrage honnête : T tâches × K_cal exécutions ; cellule c : Z = √a·U_t + √(1−a)·(√ρ·E_tj + √(1−ρ)·N_ctj)
  + dérive. Cellules : 8 critères (contrôle 12) + 1 sujet (blanc séquentiel, pour G1 seulement).
- Dérive dans la tâche, linéaire en rang d'exécution r = 0..K_cal−1 : d·(r − (K_cal−1)/2)·2/K_cal, de sorte que
  l'écart des moyennes des deux moitiés temporelles vaut exactement d (σ total) ; amplitude du premier au dernier ≈ 2d.
  Commune à toutes les cellules (dérive du générateur) ou propre à une cellule (variante).
- Variante « ordre des tâches » : décalage linéaire en indice de tâche, écart d entre première et seconde moitié des
  tâches (tâches fabriquées l'une après l'autre).
- Coupes : « dans_temporelle » (premières contre dernières exécutions de chaque tâche : code actuel) ;
  « dans_graine » (moitié des exécutions de chaque tâche tirée au hasard) ; « entre » (T/2 tâches tirées au hasard
  contre les autres) ; « entre_contigu » (premières T/2 tâches contre dernières, variante).
- Épreuve, chaque mode (2 ; 3 en variante, 24 contrôles) : 64 unités = les 64 premières tâches (même U que le calibrage), K = 10 sabotés,
  hétérogénéité h·H(unité, mode) commune aux cellules ; rappel de population 0,40 (critères), 0,50 (sujet). Sabotés
  sans dérive (milieu de la rampe).
- Contrôle 12 : v(t) = alerte(s1) − alerte(s2) ; richesse mélangée sur Λ ; 16 contrôles ; échec joint = au moins un
  promu ; unilatéral = sens « + » ; bilatéral = l'un ou l'autre. Seuils de diagnostic 20, 30, 40, 60.
- G1 (un mode) : seuils de chaque cellule sur tout le calibrage (les deux moitiés réunies, donc indépendants de la
  coupe) ; v_c(t) = alerte(sujet) − alerte(critère c) ; minimum des 8 processus (intersection-union), promotion au
  seuil 20. G1 « deux modes » = promue dans chaque mode (dans les 3 en variante).
- Nombres aléatoires communs : le monde (scores) est tiré d'un générateur qui ne dépend pas de la coupe ; le tirage de
  la coupe vient d'un second générateur. Les coupes sont donc comparées sur les mêmes mondes.
Usage : python3 -I -B coupe-calibrage-v1.py CHEMIN_A2 [--rapide] [--travailleurs 4] > sortie.json
"""
import argparse
import hashlib
import importlib.util
import json
import math
import platform
import sys
import time
from multiprocessing import Pool

import numpy as np

p = argparse.ArgumentParser()
p.add_argument("a2")
p.add_argument("--graine", type=int, default=202610291500)
p.add_argument("--rapide", action="store_true")
p.add_argument("--travailleurs", type=int, default=4)
args = p.parse_args()

spec = importlib.util.spec_from_file_location("simA2", args.a2)
A2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(A2)
G = args.graine
L = A2.LAMBDAS
Z_TAU = A2.Z_TAU
SEUILS = (20.0, 30.0, 40.0, 60.0)
N_EP, K = 64, 10
N_CRIT = 8


def quantile_normal(p_):
    return float(A2.ndtri(np.array([p_]))[0])


def seuil_partition(x):
    n = x.shape[-1]
    j = math.floor(A2.TAU * (n + 1) + 1e-12)
    if j < 1:
        return np.full(x.shape[:-1], np.inf)
    return -np.partition(-x, j - 1, axis=-1)[..., j - 1]


def log_richesse_nd(v):
    lw = np.cumsum(np.log1p(L * v[..., None]), axis=-2)
    m = lw.max(axis=-1, keepdims=True)
    return (m + np.log(np.exp(lw - m).mean(axis=-1, keepdims=True)))[..., 0]


def wilson(k, n, z=1.959963984540054):
    ph = k / n
    den = 1 + z * z / n
    c = (ph + z * z / (2 * n)) / den
    hw = z * math.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / den
    return [round(max(0.0, c - hw), 4), round(min(1.0, c + hw), 4)]


BASE = dict(N=9600, taches=64, a=0.3, h=0.3, rho=0.0, coupe="dans_temporelle", derive=0.0, derive_cellules=None,
            derive_taches=0.0, grille=None, G1=True, ecart_G1=0.10, modes=2)


def lot(rw, rc, B, P):
    a, h, rho, T = P["a"], P["h"], P["rho"], P["taches"]
    K_cal = P["N"] // T
    M = N_CRIT + (1 if P["G1"] else 0)  # sujet en dernière position
    sa, sr, sq, sp = math.sqrt(a), math.sqrt(1 - a), math.sqrt(rho), math.sqrt(1 - rho)
    U = rw.standard_normal((B, 1, T, 1))
    E = rw.standard_normal((B, 1, T, K_cal))
    zc = sa * U + sr * (sq * E + sp * rw.standard_normal((B, M, T, K_cal)))
    if P["derive"]:
        rampe = P["derive"] * (np.arange(K_cal) - (K_cal - 1) / 2) * 2.0 / K_cal
        nd = M if P["derive_cellules"] is None else P["derive_cellules"]
        zc[:, :nd] += rampe
    if P["derive_taches"]:
        zc += (P["derive_taches"] * (np.arange(T) - (T - 1) / 2) * 2.0 / T)[:, None]
    if P["grille"]:
        g = P["grille"]
        zc = np.round(zc / g) * g + rw.uniform(0.0, 0.999 * g, size=zc.shape)  # bris d'égalité aléatoire d'office
    # tirage de la coupe (générateur propre à la coupe)
    crit = zc[:, :N_CRIT]
    coupe = P["coupe"]
    if coupe == "dans_temporelle":
        k1 = K_cal // 2
        h1, h2 = crit[..., :k1], crit[..., k1:]
    elif coupe == "dans_graine":
        k1 = K_cal // 2
        idx = np.argsort(rc.random((B, 1, T, K_cal)), axis=-1)
        cp = np.take_along_axis(crit, np.broadcast_to(idx, crit.shape), axis=-1)
        h1, h2 = cp[..., :k1], cp[..., k1:]
    elif coupe == "entre":
        idx = np.argsort(rc.random((B, 1, T, 1)), axis=2)
        cp = np.take_along_axis(crit, np.broadcast_to(idx, crit.shape), axis=2)
        h1, h2 = cp[:, :, : T // 2], cp[:, :, T // 2:]
    elif coupe == "entre_contigu":
        h1, h2 = crit[:, :, : T // 2], crit[:, :, T // 2:]
    else:
        raise ValueError(coupe)
    s1 = seuil_partition(h1.reshape(B, N_CRIT, -1))[:, :, None, None]
    s2 = seuil_partition(h2.reshape(B, N_CRIT, -1))[:, :, None, None]
    S = seuil_partition(zc.reshape(B, M, -1))[:, :, None, None] if P["G1"] else None
    del zc, crit, h1, h2
    rappels = np.full(M, 0.40)
    if P["G1"]:
        rappels[-1] = 0.40 + P["ecart_G1"]
    decal = Z_TAU - np.array([quantile_normal(1 - r) for r in rappels]) * math.sqrt(1 + h * h)
    sorties, g1 = [], []
    Ue = U[:, :, :N_EP]
    for _mode in range(P["modes"]):
        H = rw.standard_normal((B, 1, N_EP, 1))
        Es = rw.standard_normal((B, 1, N_EP, K))
        zs = decal[None, :, None, None] + sa * Ue + h * H + sr * (sq * Es + sp * rw.standard_normal((B, M, N_EP, K)))
        if P["grille"]:
            g = P["grille"]
            zs = np.round(zs / g) * g + rw.uniform(0.0, 0.999 * g, size=zs.shape)
        zk = zs[:, :N_CRIT]
        v = (zk > s1).mean(axis=-1) - (zk > s2).mean(axis=-1)
        sorties.append(np.stack([log_richesse_nd(v).max(axis=-1), log_richesse_nd(-v).max(axis=-1)], axis=-1))
        if P["G1"]:
            al = (zs > S).mean(axis=-1)  # (B, M, 64)
            vg = al[:, -1:, :] - al[:, :N_CRIT, :]
            g1.append(log_richesse_nd(vg).min(axis=1).max(axis=-1) >= math.log(20.0))
    ds = (s1 - s2)[:, 0, 0, 0]
    return np.concatenate(sorties, axis=1), (np.stack(g1, axis=1) if P["G1"] else None), ds


def point(tache):
    etiquette, P, R = tache
    monde = {k: v for k, v in P.items() if k != "coupe"}
    rw = A2.rng_de(G, "monde", json.dumps(monde, sort_keys=True))
    rc = A2.rng_de(G, "coupe", P["coupe"], json.dumps(monde, sort_keys=True))
    cellules = P["taches"] * (P["N"] // P["taches"]) * (N_CRIT + 1)
    B = max(5, min(50, int(2.5e6 // cellules)))
    t0 = time.time()
    mxs, g1s, dss = [], [], []
    n = 0
    while n < R:
        b = min(B, R - n)
        mx, g1, ds = lot(rw, rc, b, P)
        mxs.append(mx); dss.append(ds)
        if g1 is not None:
            g1s.append(g1)
        n += b
    mx = np.concatenate(mxs); ds = np.concatenate(dss)
    res = {"etiquette": etiquette, "parametres": P, "repetitions": R, "controles": int(mx.shape[1]),
           "taille_lot": B, "duree_s": round(time.time() - t0, 1),
           "ecart_type_s1_moins_s2_cellule_1_sigma": round(float(ds.std()), 4),
           "moyenne_s1_moins_s2_cellule_1_sigma": round(float(ds.mean()), 4)}
    for s in SEUILS:
        ls = math.log(s)
        uni = int((mx[:, :, 0] >= ls).any(axis=1).sum())
        bi = int((mx >= ls).any(axis=(1, 2)).sum())
        res[f"seuil={int(s)}"] = {"unilateral": round(uni / R, 4), "unilateral_wilson95": wilson(uni, R),
                                  "bilateral": round(bi / R, 4), "bilateral_wilson95": wilson(bi, R)}
    if g1s:
        g1 = np.concatenate(g1s)
        propre40 = ~(mx >= math.log(40.0)).any(axis=(1, 2))
        k_mode, k_deux = int(g1.sum()), int(g1.all(axis=1).sum())
        nm = g1.shape[1]
        k_deux_propre = int((g1.all(axis=1) & propre40).sum())
        res["G1"] = {"par_mode": round(k_mode / (nm * R), 4), "par_mode_wilson95": wilson(k_mode, nm * R),
                     "deux_modes": round(k_deux / R, 4), "deux_modes_wilson95": wilson(k_deux, R),
                     "deux_modes_et_controle_12_propre_bilateral_40": round(k_deux_propre / R, 4),
                     "deux_modes_et_controle_12_propre_bilateral_40_wilson95": wilson(k_deux_propre, R)}
    return res


def params(**kw):
    P = dict(BASE)
    P.update(kw)
    return P


if __name__ == "__main__":
    t_debut = time.time()
    R_P = 300 if args.rapide else 4000
    R_S = 300 if args.rapide else 2000
    COUPES = ("dans_temporelle", "dans_graine", "entre")
    taches = []
    # 1. Tableau principal : coupe × dérive × effet de tâche (G1 compris)
    for a in (0.1, 0.3, 0.5):
        for d in (0.0, 0.05, 0.10, 0.20):
            for c in COUPES:
                taches.append((f"principal|a={a}|derive={d}|{c}", params(a=a, derive=d, coupe=c), R_P))
    # 2. Variantes (a = 0,3)
    for d in (0.0, 0.10):
        for c in COUPES:
            taches.append((f"rho08|derive={d}|{c}", params(rho=0.8, derive=d, coupe=c), R_S))
            taches.append((f"h0|derive={d}|{c}", params(h=0.0, derive=d, coupe=c), R_S))
            taches.append((f"grille025_bris|derive={d}|{c}", params(grille=0.25, derive=d, coupe=c), R_S))
    for d in (0.0, 0.10):
        for c in COUPES:
            taches.append((f"trois_modes_24_controles|derive={d}|{c}", params(modes=3, derive=d, coupe=c), R_S))
    for d in (0.10, 0.20):
        for c in COUPES:
            taches.append((f"derive_une_cellule|derive={d}|{c}", params(derive=d, derive_cellules=1, coupe=c), R_S))
    for d in (0.10, 0.20):
        for c in ("dans_temporelle", "entre", "entre_contigu"):
            taches.append((f"derive_ordre_taches|d={d}|{c}", params(derive_taches=d, coupe=c), R_S))
    # 3. Taille : dans les tâches (64 tâches) selon N ; entre tâches selon N (64 tâches) et selon le nombre de tâches
    for K_cal in (20, 30, 40, 50, 75, 100, 112, 150):
        taches.append((f"taille|dans|T=64|K_cal={K_cal}", params(N=64 * K_cal, coupe="dans_temporelle", G1=False), R_S))
    for a in (0.1, 0.3, 0.5):
        for K_cal in (150, 300, 600, 1200):
            taches.append((f"taille|entre|a={a}|T=64|K_cal={K_cal}",
                           params(a=a, N=64 * K_cal, coupe="entre", G1=False), R_S))
        for T in (128, 192, 320, 640, 1920, 9600):
            taches.append((f"taille|entre|a={a}|N=9600|T={T}", params(a=a, N=9600, taches=T, coupe="entre", G1=False), R_S))
        for T in (128, 256, 512, 1024):
            taches.append((f"taille|entre|a={a}|K_cal=150|T={T}",
                           params(a=a, N=150 * T, taches=T, coupe="entre", G1=False), R_S))
    sortie = {"script": "coupe-calibrage-v1.py", "statut": "exploratoire, processeur, non préenregistré, non opposable",
              "graine_maitresse": G,
              "graines": "A2.rng_de(graine, 'monde', paramètres hors coupe) pour les scores ; A2.rng_de(graine, 'coupe', "
                         "coupe, paramètres) pour le tirage de la coupe : SeedSequence([graine] + étiquettes réduites par "
                         "SHA-256), une suite par point",
              "a2_sha256": hashlib.sha256(open(args.a2, "rb").read()).hexdigest(),
              "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
              "versions": {"python": sys.version.split()[0], "numpy": np.__version__, "plateforme": platform.platform()},
              "base": BASE, "seuils_diagnostic": list(SEUILS), "unites_epreuve": N_EP, "K": K, "tau": A2.TAU}
    with Pool(args.travailleurs) as pool:
        res = []
        for i, r in enumerate(pool.imap(point, taches)):
            res.append(r)
            print(i + 1, len(taches), r["etiquette"], r["duree_s"], round(time.time() - t_debut), file=sys.stderr,
                  flush=True)
    sortie["points"] = res
    sortie["duree_totale_s"] = round(time.time() - t_debut, 1)
    print(json.dumps(sortie, ensure_ascii=False, indent=1))
