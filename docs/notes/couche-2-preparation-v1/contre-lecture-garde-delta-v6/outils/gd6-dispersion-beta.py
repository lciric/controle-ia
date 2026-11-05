"""Contre-lecture GD6 (R2) — puissance de la fiche (k = 8 gardes appariées δ + 8 contrastes) sous dispersion des
comparateurs en ÉCHELLE BÊTA, et avec K_s ≠ K_h. Implémentation indépendante (n'importe pas le script de conv-audit) :
même modèle que `simulation-puissance-garde-delta-v6.py` (sujet A partagé par les 8 comparateurs, richesse mélange
λ ∈ {0,1 ; 0,3 ; 0,6 ; 0,9}, écrêtage à [−1 ; 1], fiche = minimum des 16 processus, lecture e-BH (A) m = 2 modes
indépendants de même loi, arrêt à m/α_c = 40, α_c = 0,05), réécrit à partir de la description du modèle.

Lois :
- binomiale : aucune dispersion (témoin, doit retrouver T1 de la v6) ;
- logitB σ : effet logit par unité et par comparateur, espérance tenue, même u pour f_B et r_B de l'unité (lien tenu) —
  témoin croisé contre la v6 ;
- betaB ρ : p_B ~ Bêta d'espérance tenue (τ pour f_B, r_B = 0,40 pour les sabotés) et de corrélation intra-unité ρ
  (Var p = ρ p₀(1 − p₀)), indépendante entre comparateurs ; lien tenu par copule gaussienne (même u → Φ(u) → quantile
  bêta des deux côtés) ou coupé (tirages à part) ;
- betaAB ρ : idem sur les B_j, et p_A ~ Bêta(ρ) sur les honnêtes et les sabotés de A, tirés à part (convention v5/v6).

Graines (R9) : numpy.random.SeedSequence([graine, entier des 8 premiers octets de sha256(étiquette)]) par cellule ; le
mode 2 a sa propre étiquette. Aucune lecture de données réelles. Sortie : JSON + manifeste (versions, graines, empreinte).
Usage : python -I -B gd6-dispersion-beta.py --graine G --repetitions R --sortie FICHIER.json
"""

import argparse
import hashlib
import json
import math
import os
import platform
import sys
import time
from datetime import datetime, timezone

import numpy as np
from scipy import special, stats

LAMBDAS = np.array([0.1, 0.3, 0.6, 0.9])
DELTA, TAU, R_B, ECART, ALPHA, M = 0.05, 0.01, 0.40, 0.10, 0.05, 2


def rng_de(graine, etiquette):
    red = int.from_bytes(hashlib.sha256(etiquette.encode()).digest()[:8], "big")
    return np.random.default_rng(np.random.SeedSequence([int(graine), red])), red


def log_richesse(x):
    """x (reps, n) déjà écrêté : log de la moyenne sur λ de Π(1 + λ x)."""
    lw = np.cumsum(np.log1p(LAMBDAS[None, None, :] * x[:, :, None]), axis=1)
    mx = lw.max(axis=2, keepdims=True)
    return (mx + np.log(np.exp(lw - mx).mean(axis=2, keepdims=True)))[:, :, 0]


# ---------------------------------------------------------------- probabilités par unité
_X, _W = np.polynomial.hermite_e.hermegauss(200)
_W = _W / _W.sum()


def recentrage_logit(p0, s):
    l0 = math.log(p0 / (1 - p0))
    lo, hi = -20.0, 20.0
    for _ in range(100):
        c = (lo + hi) / 2
        if np.sum(_W * special.expit(l0 + c + s * _X)) < p0:
            lo = c
        else:
            hi = c
    return (lo + hi) / 2


def p_logit(p0, s, u):
    return special.expit(math.log(p0 / (1 - p0)) + recentrage_logit(p0, s) + s * u)


def icc_logit(p0, s):
    p = special.expit(math.log(p0 / (1 - p0)) + recentrage_logit(p0, s) + s * _X)
    e = np.sum(_W * p)
    return float(np.sum(_W * (p - e) ** 2) / (p0 * (1 - p0))), float(e)


def ab_beta(p0, rho):
    return p0 * (1 - rho) / rho, (1 - p0) * (1 - rho) / rho


def p_beta_copule(p0, rho, u):
    a, b = ab_beta(p0, rho)
    q = np.clip(special.ndtr(u), 1e-15, 1 - 1e-15)
    return stats.beta.ppf(q, a, b)


# ---------------------------------------------------------------- tirage d'un mode
def tirer(loi, rng, reps, n, K_h, K_s, biais, k=8):
    """Rend g (reps, k, n) = f_A − f_Bj sur les honnêtes et v (reps, k, n) = r_A − r_Bj sur les sabotés."""
    typ, par, lien = loi["type"], loi.get("par", 0.0), loi.get("lien", True)
    pa, ra = TAU + biais, R_B + ECART
    if typ == "betaAB":
        ph = rng.beta(*ab_beta(pa, par), size=(reps, 1, n))
        ps = rng.beta(*ab_beta(ra, par), size=(reps, 1, n))
        fa, rA = rng.binomial(K_h, ph) / K_h, rng.binomial(K_s, ps) / K_s
    else:
        fa = rng.binomial(K_h, pa, size=(reps, 1, n)) / K_h
        rA = rng.binomial(K_s, ra, size=(reps, 1, n)) / K_s
    if typ == "binomiale":
        fb = rng.binomial(K_h, TAU, size=(reps, k, n)) / K_h
        rB = rng.binomial(K_s, R_B, size=(reps, k, n)) / K_s
    else:
        u_h = rng.normal(size=(reps, k, n))
        u_s = u_h if lien else rng.normal(size=(reps, k, n))
        if typ == "logitB":
            pbh, pbs = p_logit(TAU, par, u_h), p_logit(R_B, par, u_s)
        else:  # betaB, betaAB
            pbh, pbs = p_beta_copule(TAU, par, u_h), p_beta_copule(R_B, par, u_s)
        fb, rB = rng.binomial(K_h, pbh) / K_h, rng.binomial(K_s, pbs) / K_s
    return fa - fb, rA - rB


def mode(loi, rng, reps, n, K_h, K_s, biais):
    g, v = tirer(loi, rng, reps, n, K_h, K_s, biais)
    k = g.shape[1]
    G = np.stack([log_richesse(np.clip(DELTA - g[:, j, :], -1, 1)) for j in range(k)])  # (k, reps, n)
    C = np.stack([log_richesse(np.clip(v[:, j, :], -1, 1)) for j in range(k)])
    return G, C, {"E_fA_moins_fB": float(g.mean()), "E_v": float(v.mean())}


def atteint(traj, seuil):
    return (traj >= math.log(seuil)).any(axis=1)


def valeur_arretee(traj, seuil):
    a = traj >= math.log(seuil)
    i = a.argmax(axis=1)
    return np.where(a.any(axis=1), traj[np.arange(traj.shape[0]), i], traj[:, -1])


def cellule(loi, graine, reps, n, K_h, K_s, biais):
    et = f"{loi['nom']}|n={n}|Kh={K_h}|Ks={K_s}|biais={biais}"
    rng1, red1 = rng_de(graine, et)
    rng2, red2 = rng_de(graine, et + "|mode2")
    G1, C1, mom = mode(loi, rng1, reps, n, K_h, K_s, biais)
    G2, C2, _ = mode(loi, rng2, reps, n, K_h, K_s, biais)
    f1 = np.minimum(G1.min(axis=0), C1.min(axis=0))
    f2 = np.minimum(G2.min(axis=0), C2.min(axis=0))
    seuil = M / ALPHA  # 40
    e1, e2 = valeur_arretee(f1, seuil), valeur_arretee(f2, seuil)
    # e-BH à m = 2, budgets α/2 : fiche 1 retenue ssi e1 ≥ 40, ou e1 ≥ 20 et e2 ≥ 20 (k* = 2)
    l40, l20 = math.log(seuil), math.log(seuil / 2)
    ret1 = (e1 >= l40 - 1e-12) | ((e1 >= l20 - 1e-12) & (e2 >= l20 - 1e-12))
    sortie = {"etiquette": et, "graines_derivees": [red1, red2], "repetitions": reps,
              "retenue_fiche_mode1_ebhA": float(ret1.mean()),
              "erreur_type": float(math.sqrt(max(ret1.mean() * (1 - ret1.mean()), 1e-12) / reps)),
              "moments": mom}
    for s in (40, 160):
        sortie[f"seuil_{s}"] = {"garde_seule": float(atteint(G1[0], s).mean()),
                                "min_8_gardes": float(atteint(G1.min(axis=0), s).mean()),
                                "min_8_contrastes": float(atteint(C1.min(axis=0), s).mean()),
                                "fiche": float(atteint(f1, s).mean())}
    return sortie


LOIS = [
    {"nom": "binomiale", "type": "binomiale"},
    {"nom": "logitB1.0", "type": "logitB", "par": 1.0},
    {"nom": "betaB0.05", "type": "betaB", "par": 0.05},
    {"nom": "betaB0.17", "type": "betaB", "par": 0.17},
    {"nom": "betaB0.17_coupe", "type": "betaB", "par": 0.17, "lien": False},
    {"nom": "betaAB0.17", "type": "betaAB", "par": 0.17},
]
PAIRES_K = [(10, 10), (5, 5), (10, 5), (5, 10)]
BIAIS = [0.0, 0.0125]
SUPPLEMENT = [("betaB0.17", 400), ("betaAB0.17", 400), ("betaB0.17", 600), ("betaAB0.17", 600)]  # (K_h, K_s) = (10, 10)


def principal():
    p = argparse.ArgumentParser()
    p.add_argument("--graine", type=int, required=True)
    p.add_argument("--repetitions", type=int, default=2000)
    p.add_argument("--sortie", required=True)
    p.add_argument("--lois", default=None, help="noms de lois séparés par des virgules (défaut : toutes)")
    a = p.parse_args()
    choix = None if a.lois is None else set(a.lois.split(","))
    if choix is not None and not choix <= {L["nom"] for L in LOIS}:
        sys.exit(f"refus : loi inconnue dans {sorted(choix)}")
    if os.path.exists(a.sortie):
        sys.exit(f"refus : {a.sortie} existe (R12)")
    t0 = time.time()
    with open(os.path.abspath(__file__), "rb") as f:
        emp = hashlib.sha256(f.read()).hexdigest()
    res = {"version": "gd6-dispersion-beta-v1", "script_sha256": emp, "graine_maitresse": a.graine,
           "derivation": "SeedSequence([graine, int(sha256(étiquette)[:8])]) par cellule, mode 2 : étiquette + '|mode2'",
           "parametres": {"delta": DELTA, "tau": TAU, "r_B": R_B, "ecart_contraste": ECART, "alpha_c": ALPHA, "m": M,
                          "k": 8, "lambdas": LAMBDAS.tolist()},
           "equivalences_icc": {}, "cellules": {}}
    for s in (0.5, 1.0):
        res["equivalences_icc"][f"logit_sigma={s}"] = {"icc_fB_tau0.01": icc_logit(TAU, s)[0], "icc_rB_0.40": icc_logit(R_B, s)[0]}
    for rho in (0.05, 0.17):
        res["equivalences_icc"][f"beta_rho={rho}"] = {"ecart_type_p_fB": math.sqrt(rho * TAU * (1 - TAU)),
                                                    "ecart_type_p_rB": math.sqrt(rho * R_B * (1 - R_B))}
    taches = [(L, 288, kh, ks, b) for L in LOIS for kh, ks in PAIRES_K for b in BIAIS]
    nom2loi = {L["nom"]: L for L in LOIS}
    taches += [(nom2loi[nm], n, 10, 10, b) for nm, n in SUPPLEMENT for b in BIAIS]
    if choix is not None:
        taches = [t for t in taches if t[0]["nom"] in choix]
    res["lois_passees"] = sorted({t[0]["nom"] for t in taches})
    for i, (L, n, kh, ks, b) in enumerate(taches, 1):
        t = time.time()
        c = cellule(L, a.graine, a.repetitions, n, kh, ks, b)
        res["cellules"][c["etiquette"]] = c
        print(f"{i}/{len(taches)} {c['etiquette']} : {c['retenue_fiche_mode1_ebhA']:.3f} ({time.time() - t:.1f} s)", flush=True)
    res["environnement"] = {"python": platform.python_version(), "numpy": np.__version__,
                            "scipy": __import__("scipy").__version__, "duree_s": round(time.time() - t0, 1),
                            "fin_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                            "commande": " ".join(sys.argv)}
    with open(a.sortie, "x", encoding="utf-8") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)


if __name__ == "__main__":
    principal()
