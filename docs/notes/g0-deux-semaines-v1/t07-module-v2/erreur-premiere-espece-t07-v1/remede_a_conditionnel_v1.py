#!/usr/bin/env python3
"""Remède (a) : audit R4 des cellules en échec du prototype, deux lectures du nul — v1 (suite R-2270).

Constat qui motive ce script (sortie `remede-a-rapport-v1.txt`) : à θ_F = 0,94 et ρ = 1 (directions du plancher étalées),
toutes les méthodes du prototype dépassent, la sonde « alignée » comprise. Hypothèse d'audit : le rééchantillonnage des tâches
ne voit pas le bruit du **tirage des 200 directions** ; le nul B du script v1 le compte (θ_F = quantile 0,95 sur une
infinité de directions), alors que le texte de T0.7 déclare ce bruit partagé et non répliqué (« Métrique », plancher de P3
réutilisé : « T7-P1 réplique la sonde sur des épisodes neufs, pas le tirage du plancher »).

Deux nuls, mêmes mondes (rejoués à l'identique : contrôle d'égalité au bit près avec `generer` du script v1) :
- **nul conditionnel** : aire vraie de la sonde = quantile 0,95 (interpolation de `np.quantile`, comme le code gelé) des aires
  vraies des **200 directions tirées** dans ce monde (θ_c, calculé exactement par `aire_plan`) ; même bruit propre de la sonde,
  signal réglé (sonde « propre » : r = r_pour(θ_c) ; « alignée » : charge c' sur l'axe commun telle que l'aire vraie vaille
  θ_c) ; lu par le remède (a1), tâches seules (fonctions du prototype `remede_a_prototype_v1.py`, `3e488d70…`, importé après
  vérification de son empreinte) ; et, sur deux cellules, par la règle actuelle R0 (`lecture_v1.lecture_jeux`, code gelé) ;
- **nul de population** (celui du script v1) : sonde d'aire vraie θ_F, lue par (a1) et par **(a2)** : à chaque tirage, les
  200 directions sont aussi tirées avec remise avant le quantile (le bruit du tirage du plancher entre dans l'intervalle).

Puissance de (a2) aux alternatives du prototype (64 tâches, 0,94 et 0,62 ; ρ = 4 et 1 ; mêmes mondes).

Graines : celles du prototype pour les tâches (spawn_key (17, …)) ; tirage des directions : (19, <clé du monde>, sonde).

Lancement : `python3 -I -B <ce script> <racine> <script v1> <prototype> calcul <nul-v1.json> <sortie.json>` puis
`… rapport <sortie.json> <rapport.json>`.
"""
from __future__ import annotations

import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import hashlib
import importlib.util
import json
import math
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np
from scipy.stats import beta

SHA_PROTO = "3e488d7036fe48ed7a291a728c1822d6f7a9698e0696ce2e376465dea757bb2c"
PA = V1 = None
CELLULES_NUL = (  # (n, θ_F, ρ, compo, clé du monde sans l'indice, mondes, R0 conditionnel)
    (64, 0.94, 1.0, "propre", (2, 64, 3, 1, 0, 0), 200, True),
    (36, 0.94, 1.0, "propre", (2, 36, 3, 1, 0, 0), 200, False),
    (64, 0.94, 1.0, "alignee", (1, 64, 3, 1, 1, 0), 100, False),
    (64, 0.94, 4.0, "propre", (1, 64, 3, 0, 0, 0), 100, True),
    (64, 0.62, 1.0, "propre", (2, 64, 1, 1, 0, 0), 100, False),
)
CELLULES_PUISSANCE = ((64, 0.94, 4.0, (1, 64, 3, 0, 0, 1)), (64, 0.94, 1.0, (1, 64, 3, 1, 0, 1)),
                      (64, 0.62, 4.0, (1, 64, 1, 0, 0, 1)), (64, 0.62, 1.0, (1, 64, 1, 1, 0, 1)))
W_PUISSANCE = 75


def charger(racine: str, chemin_v1: str, chemin_proto: str) -> None:
    global PA, V1
    sha = hashlib.sha256(Path(chemin_proto).read_bytes()).hexdigest()
    if sha != SHA_PROTO:
        raise SystemExit(f"prototype : empreinte {sha} ≠ {SHA_PROTO} : arrêt")
    spec = importlib.util.spec_from_file_location("remede_a_v1", chemin_proto)
    PA = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(PA)
    PA.charger(racine, chemin_v1)
    V1 = PA.V1


def rejouer(n, theta, rho, compo, r_sonde, cle):
    """Même suite de tirages que `V1.generer`, avec l'axe commun, les z et les bruits propres rendus."""
    rng = np.random.default_rng(np.random.SeedSequence(V1.ENTROPIE, spawn_key=cle))
    y = np.tile(np.r_[np.ones(V1.T), np.zeros(V1.T)], n).astype(np.int64)
    delta = 0.0 if theta <= 0.5 else V1.delta_axe(theta, rho, n)
    x0 = delta * y + V1.bruit(rng, 1, n)[0]
    zs, planchers, bruits = [], [], []
    for _ in range(V1.N_SONDES):
        z = rng.standard_normal(V1.N_PLANCHER)
        planchers.append((rho * z)[:, None] * x0[None, :] + V1.bruit(rng, V1.N_PLANCHER, n))
        bruits.append(V1.bruit(rng, 1, n)[0])
        zs.append(z)
    sondes = [(r_sonde * y + b) if compo == "propre" else (V1.Z95 * rho * x0 + b) for b in bruits]
    return y, delta, x0, zs, planchers, bruits, sondes


def theta_conditionnel(z, rho, delta, n) -> float:
    if delta == 0.0:
        return 0.5
    c = rho * z
    aires = np.array([V1.aire_plan(float(ci * delta / math.sqrt(ci * ci + 1)), n) for ci in c])
    return float(np.quantile(aires, V1.QUANTILE_PLANCHER))


def lire(n, y, sonde, plancher, rng_t, rng_d, avec_a2: bool) -> dict:
    """Bornes basses (six méthodes) de (a1) et, si demandé, de (a2) ; décisions par `etat_pour_sonde` (code gelé)."""
    CR = V1.CR
    tache = np.repeat(np.arange(n), 2 * V1.T)
    r = V1.PL.comparer_scores_au_plancher(sonde, plancher, y, tache, 1, 0, V1.QUANTILE_PLANCHER, PA.NIVEAU)
    a_hat, q_hat = float(r["aire"]), float(r["plancher_quantile"])
    X = np.vstack([sonde[None, :], plancher])
    C = PA.comparaisons(X, n)
    W, _ = PA.poids(rng_t, n)
    A = PA.aires_tirees(C, W, n)
    T = V1.T
    S = C.sum(axis=(1, 2))
    A_j = (S[:, None] - C.sum(axis=2) - C.sum(axis=1) + np.diagonal(C, axis1=1, axis2=2)) / (T * T * (n - 1) ** 2)
    q_j = np.quantile(A_j[1:], V1.QUANTILE_PLANCHER, axis=0)
    D_hat, L_hat = a_hat - q_hat, float(PA.logit(a_hat) - PA.logit(q_hat))
    D_j, L_j = A_j[0] - q_j, PA.logit(A_j[0]) - PA.logit(q_j)
    variantes = {"a1": np.quantile(A[1:], V1.QUANTILE_PLANCHER, axis=0)}
    if avec_a2:
        idx = rng_d.integers(0, V1.N_PLANCHER, size=(PA.B, V1.N_PLANCHER))
        G = A[1:][idx.T, np.arange(PA.B)[None, :]]
        variantes["a2"] = np.quantile(G, V1.QUANTILE_PLANCHER, axis=0)
    out = {"aire": a_hat, "q95": q_hat}
    for v, q_b in variantes.items():
        D_b, L_b = A[0] - q_b, PA.logit(A[0]) - PA.logit(q_b)
        lb = {"percentile_D": float(np.quantile(D_b, PA.ALPHA)), "percentile_logit": float(np.quantile(L_b, PA.ALPHA)),
              "normale_logit": float(L_hat + PA.Z_ALPHA * L_b.std(ddof=1)),
              "basique_logit": float(2 * L_hat - np.quantile(L_b, 1 - PA.ALPHA)),
              "bca_D": PA.bca(D_hat, D_b, D_j), "bca_logit": PA.bca(L_hat, L_b, L_j)}
        etats = {}
        for m, x in lb.items():
            bas = float(PA.expit(PA.logit(q_hat) + x)) if m in PA.SUR_LOGIT else q_hat + x
            etats[m] = CR.etat_pour_sonde({"aire": a_hat, "bas": bas, "plancher": {"quantile": q_hat}, "triviaux": {}})
        out[v] = {"bornes": lb, "etats": etats}
    return out


def tache(args):
    racine, chemin_v1, chemin_proto, nature, n, theta, rho, compo, cle, r_pop, debut, fin, avec_r0 = args
    if PA is None:
        charger(racine, chemin_v1, chemin_proto)
    sortie = []
    for w in range(debut, fin):
        cw = tuple(cle) + (w,)
        y, delta, x0, zs, planchers, bruits, sondes = rejouer(n, theta, rho, compo, r_pop, cw)
        if w == debut:                                        # rejeu au bit près
            y1, s1, p1 = V1.generer(n, theta, rho, compo, r_pop, cw)
            if not (np.array_equal(y, y1) and all(np.array_equal(a, b) for a, b in zip(sondes, s1))
                    and all(np.array_equal(a, b) for a, b in zip(planchers, p1))):
                raise SystemExit(f"rejeu différent de V1.generer : {cw}")
        ligne = {"monde": w, "theta_c": [], "pop": [], "cond": []}
        cond_sondes = []
        for p in range(V1.N_SONDES):
            tc = theta_conditionnel(zs[p], rho, delta, n)
            ligne["theta_c"].append(tc)
            rc = V1.r_pour(tc, n)
            if compo == "propre":
                sc = rc * y + bruits[p]
            else:
                cp_ = rc / math.sqrt(delta ** 2 - rc ** 2) if delta > rc else 1e6
                sc = cp_ * x0 + bruits[p]
            cond_sondes.append(sc)
            base = (17,) + cw + (p,)
            if nature == "nul":
                ligne["pop"].append(lire(n, y, sondes[p], planchers[p], np.random.default_rng(np.random.SeedSequence(PA.ENTROPIE_A, spawn_key=base)),
                                         np.random.default_rng(np.random.SeedSequence(PA.ENTROPIE_A, spawn_key=(19,) + cw + (p,))), True))
                ligne["cond"].append(lire(n, y, sc, planchers[p], np.random.default_rng(np.random.SeedSequence(PA.ENTROPIE_A, spawn_key=base)),
                                          None, False))
            else:
                ligne["pop"].append(lire(n, y, sondes[p], planchers[p], np.random.default_rng(np.random.SeedSequence(PA.ENTROPIE_A, spawn_key=base)),
                                         np.random.default_rng(np.random.SeedSequence(PA.ENTROPIE_A, spawn_key=(19,) + cw + (p,))), True))
        if avec_r0:
            ligne["R0_cond"] = V1.lire(n, y, cond_sondes, planchers, V1.TIRAGES, V1.NIVEAU, (7,) + tuple(cle[1:]) + (w,))
        for k in ("pop", "cond"):
            if ligne[k]:
                ligne[f"organisme_{k}"] = {v: {m: V1.CR.etat_organisme([s[v]["etats"][m] for s in ligne[k]]) for m in PA.METHODES}
                                           for v in ("a1", "a2") if v in ligne[k][0]}
        sortie.append(ligne)
    return json.dumps([nature, n, theta, rho, compo, list(cle)]), sortie


def calcul(racine, chemin_v1, chemin_proto, chemin_nul_v1, sortie):
    debut = time.time()
    nul = json.loads(Path(chemin_nul_v1).read_text(encoding="utf-8"))
    taches = []
    for n, th, rho, compo, cle, w, r0 in CELLULES_NUL:
        for a in range(0, w, 10):
            taches.append((racine, chemin_v1, chemin_proto, "nul", n, th, rho, compo, cle, V1.r_pour(th, n), a, min(a + 10, w), r0))
    alternatives = {}
    for n, th, rho, cle in CELLULES_PUISSANCE:
        aires = [s["aire"] for l in nul["directs"][json.dumps([n, th, 4.0, "propre", 0])] for s in l["R0"]["sondes"]]
        a_alt = min(0.995, th + V1.Z_PUISSANCE * float(np.std(aires, ddof=1)))
        alternatives[f"{n}:{th}"] = a_alt
        for a in range(0, W_PUISSANCE, 5):
            taches.append((racine, chemin_v1, chemin_proto, "puissance", n, th, rho, "propre", cle, V1.r_pour(a_alt, n), a,
                           min(a + 5, W_PUISSANCE), False))
    res = {"script": Path(__file__).name, "prototype": SHA_PROTO, "alternatives": alternatives, "mondes": {}}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for k, lignes in ex.map(tache, taches):
            res["mondes"].setdefault(k, []).extend(lignes)
    for v in res["mondes"].values():
        v.sort(key=lambda l: l["monde"])
    res["duree_s"] = round(time.time() - debut, 1)
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    print(f"calcul : {len(taches)} tâches, {res['duree_s']} s")


def cp(x, n):
    return (0.0 if x == 0 else float(beta.ppf(0.025, x, n - x + 1)), 1.0 if x == n else float(beta.ppf(0.975, x + 1, n - x)))


def rapport(chemin, sortie):
    res = json.loads(Path(chemin).read_text(encoding="utf-8"))
    nom, fam = PA.ALPHA, 4 * PA.ALPHA
    txt, out = [f"Remède (a), deux lectures du nul — v1 ; nominal {nom:.5f} par sonde, {fam:.4f} par organisme", ""], []
    for k, lignes in sorted(res["mondes"].items()):
        nature, n, th, rho, compo, cle = json.loads(k)
        tcs = [t for l in lignes for t in l["theta_c"]]
        txt.append(f"{nature} {compo} n={n} θ_F={th} ρ={rho} ({len(lignes)} mondes) ; θ_c (quantile des 200 directions tirées) : "
                   f"moyenne {np.mean(tcs):.4f}, écart type {np.std(tcs):.4f}")
        e = {"nature": nature, "n": n, "theta_F": th, "rho": rho, "compo": compo, "mondes": len(lignes), "taux": {}}
        for lec, v in (("pop", "a1"), ("pop", "a2"), ("cond", "a1")):
            if not lignes[0][lec] or v not in lignes[0][lec][0]:
                continue
            for m in PA.METHODES:
                ks = sum(s[v]["etats"][m] == V1.CR.AU_DESSUS for l in lignes for s in l[lec])
                nb = 4 * len(lignes)
                kf = sum(l[f"organisme_{lec}"][v][m] == "U" for l in lignes)
                e["taux"][f"{lec}/{v}/{m}"] = {"sonde": [ks, nb, cp(ks, nb)], "famille": [kf, len(lignes), cp(kf, len(lignes))]}
                marque = "  DÉPASSE" if (nature == "nul" and (cp(ks, nb)[0] > nom or cp(kf, len(lignes))[0] > fam)) else ""
                txt.append(f"   {('nul ' + {'pop': 'de population', 'cond': 'conditionnel'}[lec]) if nature == 'nul' else 'puissance'}"
                           f" {v} {m:17s} sonde {ks:>3}/{nb} = {ks / nb:.4f} [{cp(ks, nb)[0]:.4f} ; {cp(ks, nb)[1]:.4f}] ; famille "
                           f"{kf:>3}/{len(lignes)} = {kf / len(lignes):.4f}{marque}")
        if "R0_cond" in lignes[0]:
            ks = sum(s["etat"] == V1.CR.AU_DESSUS for l in lignes for s in l["R0_cond"]["sondes"])
            kf = sum(l["R0_cond"]["organisme"] == "U" for l in lignes)
            nb = 4 * len(lignes)
            e["taux"]["cond/R0"] = {"sonde": [ks, nb, cp(ks, nb)], "famille": [kf, len(lignes), cp(kf, len(lignes))]}
            txt.append(f"   nul conditionnel, règle actuelle R0 : sonde {ks}/{nb} = {ks / nb:.4f} [{cp(ks, nb)[0]:.4f} ; "
                       f"{cp(ks, nb)[1]:.4f}] ; famille {kf}/{len(lignes)} = {kf / len(lignes):.4f} [{cp(kf, len(lignes))[0]:.4f} ; "
                       f"{cp(kf, len(lignes))[1]:.4f}]")
        out.append(e)
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump({"cellules": out, "texte": txt, "alternatives": res["alternatives"]}, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    print("\n".join(txt))


if __name__ == "__main__":
    racine, chemin_v1, chemin_proto, phase = sys.argv[1:5]
    charger(racine, chemin_v1, chemin_proto)
    if phase == "calcul" and len(sys.argv) == 7:
        calcul(racine, chemin_v1, chemin_proto, sys.argv[5], sys.argv[6])
    elif phase == "rapport" and len(sys.argv) == 7:
        rapport(sys.argv[5], sys.argv[6])
    else:
        sys.exit(__doc__)
