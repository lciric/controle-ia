"""Contre-lecture v5, questions 3 et 4 : doutes déclarés et contrôle d'erreur sous d'autres fiches nulles.

Outils de la v5 réutilisés tels quels (copie conforme 7d1239e1…) : `processus` (trajectoires), `retenues_famille` (arrêt au
premier instant + e-BH, vérifiée identique au pôle par verif_ebh_pole.py). Lois ajoutées ici (contre-lecteur) :
- `LoiCorr` : sujet A comme la v5 (binomial, sujet partagé) ; comparateurs B_j avec un effet d'unité sur leurs probabilités,
  **commun aux k comparateurs** (corrélation positive entre comparateurs) ou indépendant par comparateur ; forme logit
  (espérance tenue, `proba_decalee` de la v5) ou bêta (ρ, espérance tenue) ; option : le même effet logit aussi sur A
  (« unité difficile pour tous ») ;
- modes : indépendants (v5) ou **garde commune aux modes** (mêmes unités honnêtes : mêmes g pour tous les modes) ;
- fiches nulles : « contraste0 » (v5 : écart 0, biais 0) ; « garde_frontiere » (E[g] = δ, contraste vrai +0,10) ;
  « mode_frontiere » (le mode 2 entier a E[g] = δ : 1 fiche nulle en A, k fiches nulles en B, toutes liées).
Sortie : parts (A) et (B) comme la v5 (`retenue_une_fiche`, `retenues_fiches_du_sujet`, `retenues_toutes_vraies`) + parts
d'erreur (au moins une nulle retenue ; proportion de fausses découvertes moyenne) + corrélations entre comparateurs mesurées.

Usage : python3 -I -B verif_doutes.py SCRIPT_V5 SORTIE.json PLAN [repetitions]
"""
import hashlib
import importlib.util
import json
import math
import sys
import time

import numpy as np

SCRIPT, SORTIE, PLAN = sys.argv[1:4]
REPS = int(sys.argv[4]) if len(sys.argv) > 4 else 1000
spec = importlib.util.spec_from_file_location("sim_v5", SCRIPT)
v5 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v5)
ALPHA = 0.05


class LoiCorr:
    def __init__(self, K, taux, ecart=0.10, sigma_b=0.0, rho_b=0.0, commun=True, sigma_a_commun=0.0):
        self.K, self.taux, self.ecart = K, taux, ecart
        self.sigma_b, self.rho_b, self.commun, self.sigma_a = sigma_b, rho_b, commun, sigma_a_commun
        self.partage = True
        self.nuls = 0  # nombre de comparateurs « nuls » (r_B = r_A : E[v_j] = 0), les premiers indices

    def effet(self):
        return False

    def nom(self):
        return f"corr_K{self.K}_t{self.taux}_sb{self.sigma_b}_rb{self.rho_b}_commun{self.commun}_sa{self.sigma_a}"

    def _pb(self, rng, p0, forme, u=None):
        if self.sigma_b:
            return v5.proba_decalee(p0, self.sigma_b, u)
        if self.rho_b:
            return rng.beta(*v5.parametres_beta(p0, self.rho_b), size=forme)
        return None

    def tirer(self, rng, reps, n, ng, k, biais, biais_contraste=0.0, moments=None):
        K = self.K
        pa_h = self.taux + biais
        ra = 0.4 + self.ecart
        L = max(n, ng)
        kk = 1 if self.commun else k
        u = rng.normal(size=(reps, kk, L))  # effet d'unité des B (même unité : honnêtes et sabotés)
        if self.sigma_a:  # même effet sur A (unité difficile pour tous) : u commun, pris sur la 1re ligne
            pha = v5.proba_decalee(pa_h, self.sigma_a, u[:, :1, :ng])
            psa = v5.proba_decalee(ra, self.sigma_a, u[:, :1, :n])
            fa = rng.binomial(K, pha) / K
            rA = rng.binomial(K, psa) / K
        else:
            fa = rng.binomial(K, pa_h, size=(reps, 1, ng)) / K
            rA = rng.binomial(K, ra, size=(reps, 1, n)) / K
        pfb = self._pb(rng, self.taux, (reps, kk, ng), u[:, :, :ng])
        prb = self._pb(rng, 0.4, (reps, kk, n), u[:, :, :n])
        if pfb is None:
            fb = rng.binomial(K, self.taux, size=(reps, k, ng)) / K
            rB = rng.binomial(K, 0.4, size=(reps, k, n)) / K
        else:
            fb = rng.binomial(K, np.broadcast_to(pfb, (reps, k, ng))) / K
            rB = rng.binomial(K, np.broadcast_to(prb, (reps, k, n))) / K
        if self.nuls:
            rB = rB.copy()
            rB[:, :self.nuls, :] = rng.binomial(K, ra, size=(reps, self.nuls, n)) / K
        return fa - fb, rA - rB


def correlations(loi, rng, n, k):
    g, v = loi.tirer(rng, 400, n, n, k, 0.0)
    cg = np.corrcoef(g[:, 0, :].ravel(), g[:, 1, :].ravel())[0, 1] if k > 1 else None
    cv = np.corrcoef(v[:, 0, :].ravel(), v[:, 1, :].ravel())[0, 1] if k > 1 else None
    return {"corr_g_entre_comparateurs": float(cg), "corr_v_entre_comparateurs": float(cv),
            "E_g": float(g.mean()), "E_v": float(v.mean()), "sd_v": float(v.std()), "sd_g": float(g.std())}


def famille(loi, rng, reps, n, k, delta, biais, M, nulles, garde_commune):
    modes = []
    for i in range(M):
        b = biais
        if nulles == "mode_frontiere" and i == 1:
            b = delta
        g, c = v5.processus(loi, rng, reps, n, n, k, delta, b, None)
        modes.append([g, c])
    if garde_commune:
        if nulles == "mode_frontiere":
            raise SystemExit("garde commune et mode frontière : incompatibles")
        for m in modes[1:]:
            m[0] = modes[0][0]
    nulA, nulB = [], []
    if nulles == "un_comparateur_nul":
        l1 = LoiCorr(loi.K, loi.taux, loi.ecart, loi.sigma_b, loi.rho_b, loi.commun, loi.sigma_a)
        l1.nuls = 1
        for _ in range(2):
            g, c = v5.processus(l1, rng, reps, n, n, k, delta, 0.0, None)
            nulA.append(np.minimum(g.min(axis=0), c.min(axis=0)))
            nulB.append(np.minimum(g[0], c[0]))
    if nulles in ("contraste0", "garde_frontiere"):
        for _ in range(2):
            if nulles == "contraste0":
                l0 = LoiCorr(loi.K, loi.taux, 0.0, loi.sigma_b, loi.rho_b, loi.commun, loi.sigma_a)
                g, c = v5.processus(l0, rng, reps, n, n, k, delta, 0.0, None)
            else:
                g, c = v5.processus(loi, rng, reps, n, n, k, delta, delta, None)
            nulA.append(np.minimum(g.min(axis=0), c.min(axis=0)))
            nulB.append(np.minimum(g[0], c[0]))
    sortie = {}
    for lect in ("A", "B"):
        if lect == "A":
            fiches = [np.minimum(g.min(axis=0), c.min(axis=0)) for g, c in modes] + nulA
            vraies_idx = list(range(M))
            if nulles == "mode_frontiere":
                vraies_idx = [0] + list(range(2, M))
            du_sujet = [0]
        else:
            fiches = [np.minimum(g[j], c[j]) for g, c in modes for j in range(k)] + nulB
            vraies_idx = list(range(M * k))
            if nulles == "mode_frontiere":
                vraies_idx = list(range(k)) + list(range(2 * k, M * k))
            du_sujet = list(range(k))
        m = len(fiches)
        _, at, ret = v5.retenues_famille(fiches, m, ALPHA)
        nul_idx = [i for i in range(m) if i not in vraies_idx]
        d = {"m": m, "fiches_nulles": len(nul_idx),
             "retenue_une_fiche": float(ret[:, 0].mean()),
             "retenues_fiches_du_sujet": float(ret[:, du_sujet].all(axis=1).mean()),
             "retenues_toutes_vraies": float(ret[:, vraies_idx].all(axis=1).mean()),
             "premiere_atteinte_une_fiche": float(at[:, 0].mean())}
        if nul_idx:
            rn = ret[:, nul_idx]
            d |= {"nulles_au_moins_une_retenue": float(rn.any(axis=1).mean()),
                  "proportion_fausses_decouvertes_moyenne": float((rn.sum(axis=1) / np.maximum(ret.sum(axis=1), 1)).mean()),
                  "borne_e_BH_alpha_m0_sur_m": ALPHA * len(nul_idx) / m}
        sortie[lect] = d
    return sortie


PLANS = {
    # doute « corrélation positive entre comparateurs » (k = 8, τ = 0,01, δ = 0,05, biais 0, M = 2, sans nulle)
    "correlation": [
        dict(nom="base_v5", K=K, n=n) for K, n in ((10, 160), (3, 400))] + [
        dict(nom=f"B_logit{s}_{'commun' if c else 'independant'}", K=K, n=n, sigma_b=s, commun=c)
        for s in (0.5, 1.0) for c in (True, False) for K, n in ((10, 160), (3, 400))] + [
        dict(nom=f"B_beta0.17_{'commun' if c else 'independant'}", K=K, n=n, rho_b=0.17, commun=c)
        for c in (True, False) for K, n in ((10, 160), (3, 400))] + [
        dict(nom="A_et_B_logit1.0_commun", K=K, n=n, sigma_b=1.0, commun=True, sigma_a=1.0)
        for K, n in ((10, 160), (3, 400))],
    # tailles au-delà pour K = 3 sous corrélation (la conclusion « ≈ 400 si K_h = 3 » tient-elle ?)
    "k3_tailles": [
        dict(nom=f"{lab}_n{n}", K=3, n=n, **kw) for n in (400, 650, 900)
        for lab, kw in (("base_v5", {}), ("B_logit1.0_commun", dict(sigma_b=1.0, commun=True)),
                        ("B_beta0.17_commun", dict(rho_b=0.17, commun=True)))],
    "k10_tailles": [
        dict(nom=f"{lab}_n{n}", K=10, n=n, **kw) for n in (220, 300, 400)
        for lab, kw in (("B_logit1.0_commun", dict(sigma_b=1.0, commun=True)), ("B_logit1.0_independant", dict(sigma_b=1.0, commun=False)),
                        ("B_beta0.17_independant", dict(rho_b=0.17, commun=False)))] + [
        dict(nom=f"B_logit1.0_independant_n{n}", K=3, n=n, sigma_b=1.0, commun=False) for n in (650, 900)],
    "nulles2": [dict(nom=f"un_comparateur_nul_K{K}_n{n}", K=K, n=n, nulles="un_comparateur_nul")
                for K, n in ((10, 160), (10, 400), (10, 650), (3, 400), (3, 650))],
    # contrôle d'erreur sous trois formes de fiches nulles, et garde commune aux modes
    "nulles": [
        dict(nom=f"{nl}_K{K}_n{n}", K=K, n=n, nulles=nl) for nl in ("contraste0", "garde_frontiere", "mode_frontiere")
        for K, n in ((10, 160), (10, 400), (3, 400))] + [
        dict(nom=f"garde_commune_K{K}_n{n}", K=K, n=n, garde_commune=True) for K, n in ((10, 160), (3, 400))],
}

graine = 918273645
res = {"script_sha256": hashlib.sha256(open(SCRIPT, "rb").read()).hexdigest(), "plan": PLAN, "repetitions": REPS,
       "graine": graine, "k": 8, "taux": 0.01, "delta": 0.05, "biais": 0.0, "M_modes": 2, "alpha_c": ALPHA, "cas": {}}
for i, c in enumerate(PLANS[PLAN]):
    t0 = time.time()
    loi = LoiCorr(c["K"], 0.01, 0.10, c.get("sigma_b", 0.0), c.get("rho_b", 0.0), c.get("commun", True), c.get("sigma_a", 0.0))
    rng = np.random.default_rng(np.random.SeedSequence([graine, i, int(hashlib.sha256(c["nom"].encode()).hexdigest()[:8], 16)]))
    r = {"reglage": c, "correlations_mesurees": correlations(loi, rng, 160, 8)}
    r |= famille(loi, rng, REPS, c["n"], 8, 0.05, 0.0, 2, c.get("nulles"), c.get("garde_commune", False))
    r["duree_s"] = round(time.time() - t0, 1)
    res["cas"][f"{c['nom']}|K={c['K']}|n={c['n']}"] = r
    print(c["nom"], c["K"], c["n"], {x: round(y, 3) for x, y in r["correlations_mesurees"].items()},
          "A", {x: round(y, 4) for x, y in r["A"].items() if isinstance(y, float)},
          "B", {x: round(y, 4) for x, y in r["B"].items() if isinstance(y, float)}, r["duree_s"], flush=True)
json.dump(res, open(SORTIE, "x"), indent=1, ensure_ascii=False)
