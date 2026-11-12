#!/usr/bin/env python3
"""Nombre de directions du plancher (`n_plancher`) pour la règle (a) de T0.7 — v1 (suite R-2285 de la consigne
`consigne-nul-lectures-decisives-t07-v1.md`, `22e95cf3…` ; choix (a') de Lazar).

Règle (a) : celle du module préparé `src/controle_ia/t07/plancher_v2.py` de la branche `prep/t07-plancher-v2-v1`, commit
`adb5f415…` (fichier `a0f80e68…`), extrait par `git show` dans un paquet du bac à sable (copie de `src/` de `main`, `gardes` et
`evaluation` identiques) : percentile, par blocs de tâches, de D = aire de la sonde − quantile 0,95 des aires du plancher,
niveau 0,9875, « au-dessus » si la borne basse de D est > 0.

Mondes (loi du script v1, `erreur_premiere_espece_t07_v1.py`, `59453773…`, importé pour `bruit`, `aire_plan`, `r_pour`,
`delta_axe`) : **neufs**, chacun avec 1 600 directions par sonde ; les règles à 200, 400, 800 et 1 600 directions lisent les
200, 400, 800 et 1 600 **premières** (sous-ensembles emboîtés, décisions appariées). Deux lectures du nul :
- **population** : directions retirées à chaque monde ; sonde d'aire vraie θ_F (quantile 0,95 sur une infinité de
  directions) ;
- **conditionnelle** : sonde d'aire vraie θ_c(k) = quantile 0,95 (interpolation de `np.quantile`) des aires vraies des k
  directions lues (calcul exact par `aire_plan`), même bruit propre, signal réglé par `r_pour`.

**Ce qui vient du module et du code gelé** : tirages par `plancher_v2.poids_des_tirages` (la suite d'`intervalle_blocs` sous
la graine donnée) ; décision par `plancher_v2.resume_pour_critere` puis `criteres_v1.etat_pour_sonde` et `etat_organisme`.
**Ce qui est recalculé ici pour tenir le budget** (une seule passe pour les quatre valeurs de k) : matrices de comparaisons
par tri et aires des tirages par produit matriciel en simple précision (exact : entiers < 2²⁴), quantile du plancher et
percentile de D par `np.quantile`, comme `difference_sur_poids` (l. 126-128). **Contrôle** : sur la première sonde du premier
monde de chaque lot, `plancher_v2.comparer_difference_au_plancher` est appelée à k = 200 et à k = 1 600 sur les mêmes scores
et la même graine ; borne basse de D et décision doivent être égales au bit près (écart écrit ; arrêt sinon).

Phase `cout` : temps de `comparer_difference_au_plancher` (module) et de `plancher_v1.comparer_scores_au_plancher` (règle
actuelle) par sonde et par jeu, à 1 280 et 720 actions, 2 000 tirages, k = 200 à 3 200, un fil ; et temps de notation d'une
direction du plancher par action à l'étape A (`plancher_v1.scores_plancher`, boucle du harnais), sur séquences simulées.

Graines (R9) : numpy.random.SeedSequence(ENTROPIE, spawn_key=(30, n, i_theta, i_rho, nature, monde)) pour les mondes ;
graine entière du rééchantillonnage tirée de (31, …, sonde) ; entropie tirée une fois le 2026-11-10 à 23:54:09 UTC
(`date -u`, `secrets.randbits(128)`), sans lecture de données.

Lancement : `python3 -I -B <ce script> <racine> <paquet du bac à sable (src)> <script v1> <puissance-proto.json>
nul|puissance|cout|rapport …` (voir `__main__`).
"""
from __future__ import annotations

import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import hashlib
import importlib.util
import json
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np
from scipy.stats import beta

ENTROPIE = 125504699772186677556879717891676300652
SHA_V1 = "59453773ee08e06aa1abef3d7777935f19150ac84241ac6528639f7fc1c69970"
SHA_PAQUET = {"controle_ia/t07/plancher_v2.py": "a0f80e6826b77279dfb807863af106655c2515f69d6d415657b7b121598ee796",
              "controle_ia/sondes/evaluation.py": "1040674cb321766a0e2a7fa1e0c610384df6c4fac4109dd50c42dfbb03181ed3",
              "controle_ia/t07/criteres_v1.py": "12b999fecce093372a29fb70d8c11eb7fe965f34c8746a31b399baaecc5ae8c5",
              "controle_ia/t07/plancher_v1.py": "ac6e8263293ed30c807ef91f8eab0adbcbf8e1b91d5e4c56e73dbffa1a7099dc",
              "controle_ia/gardes.py": "a83c48ceba4877a2e226c3fd43669b464152f18169bb082e9b1c48ed92179439"}
KS = (200, 400, 800, 1600)
K_MAX = 1600
B = 2000
NIVEAU = 1 - 0.05 / 4
ALPHA = (1 - NIVEAU) / 2
QP = 0.95
N_SONDES = 4
CELLULES_NUL = ((64, 0.94, 1.0, 250), (36, 0.94, 1.0, 250), (64, 0.78, 1.0, 150))
ALTERNATIVES = ((64, 0.94), (64, 0.62), (36, 0.94), (36, 0.62))       # aires vraies : celles du prototype (même recette)
W_PUISSANCE = 60
RHO_PUISSANCE = 1.0

V1 = PV2 = CR = PL = EV = None


def charger(paquet: str, chemin_v1: str) -> None:
    global V1, PV2, CR, PL, EV
    for rel, sha in SHA_PAQUET.items():
        h = hashlib.sha256((Path(paquet) / rel).read_bytes()).hexdigest()
        if h != sha:
            raise SystemExit(f"{rel} : empreinte {h} ≠ {sha} : arrêt")
    h = hashlib.sha256(Path(chemin_v1).read_bytes()).hexdigest()
    if h != SHA_V1:
        raise SystemExit(f"script v1 : empreinte {h} ≠ {SHA_V1} : arrêt")
    spec = importlib.util.spec_from_file_location("nul_t07_v1", chemin_v1)
    V1 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(V1)                    # fonctions de la loi seulement ; `V1.charger` n'est pas appelé
    sys.path.insert(0, str(Path(paquet)))
    from controle_ia.sondes import evaluation
    from controle_ia.t07 import criteres_v1, plancher_v1, plancher_v2
    PV2, CR, PL, EV = plancher_v2, criteres_v1, plancher_v1, evaluation


def graine_entiere(spawn: tuple) -> int:
    return int(np.random.SeedSequence(ENTROPIE, spawn_key=spawn).generate_state(1, dtype=np.uint64)[0] >> np.uint64(1))


def comparaisons(X: np.ndarray, n: int) -> np.ndarray:
    T = V1.T
    k = X.shape[0]
    x = X.reshape(k, n, 2, T)
    pos, neg = x[:, :, 0, :].reshape(k, n * T), x[:, :, 1, :].reshape(k, n * T)
    tache_neg = np.repeat(np.arange(n), T)
    C = np.empty((k, n, n), dtype=np.float32)
    lignes = np.arange(1, n * T + 1)
    for j in range(k):
        ordre = np.argsort(neg[j], kind="stable")
        q = neg[j][ordre]
        cum = np.zeros((n * T + 1, n))
        cum[lignes, tache_neg[ordre]] = 1.0
        np.cumsum(cum, axis=0, out=cum)
        s, l = np.searchsorted(q, pos[j], side="left"), np.searchsorted(q, pos[j], side="right")
        C[j] = (0.5 * (cum[s] + cum[l])).reshape(n, T, n).sum(axis=1)
    return C


def aires_tirees(C32: np.ndarray, W: np.ndarray, n: int) -> np.ndarray:
    T = V1.T
    W32 = W.astype(np.float32)
    out = np.empty((C32.shape[0], W.shape[0]))
    for a in range(0, C32.shape[0], 100):
        M = np.matmul(W32[None], C32[a:a + 100])
        out[a:a + 100] = (M * W32[None]).sum(axis=-1, dtype=np.float32)
    den = (W @ np.full(n, float(T))) * (W @ np.full(n, float(T)))
    return out / den[None, :]


def monde(n, theta, rho, cle):
    rng = np.random.default_rng(np.random.SeedSequence(ENTROPIE, spawn_key=cle))
    y = np.tile(np.r_[np.ones(V1.T), np.zeros(V1.T)], n).astype(np.int64)
    delta = 0.0 if theta <= 0.5 else V1.delta_axe(theta, rho, n)
    x0 = delta * y + V1.bruit(rng, 1, n)[0]
    sortie = []
    for _ in range(N_SONDES):
        z = rng.standard_normal(K_MAX)
        F = (rho * z)[:, None] * x0[None, :] + V1.bruit(rng, K_MAX, n)
        sortie.append((z, F, V1.bruit(rng, 1, n)[0]))
    return y, delta, sortie


def etat(aire: float, q: float, borne: float) -> str:
    r = PV2.resume_pour_critere({"plancher_quantile": q, "bas": 0.0, "haut": 0.0, "au_dessus_du_plancher": bool(borne > 0.0),
                                 "difference": {"bas": borne, "haut": borne}})
    return CR.etat_pour_sonde({"aire": aire, "bas": r["bas"], "plancher": {"quantile": q}, "triviaux": {}})


def tache(args):
    paquet, chemin_v1, nature, n, theta, rho, r_pop, cle, debut, fin = args
    if V1 is None:
        charger(paquet, chemin_v1)
    tache_ = np.repeat(np.arange(n), 2 * V1.T)
    sortie = []
    for w in range(debut, fin):
        cw = tuple(cle) + (w,)
        y, delta, sondes = monde(n, theta, rho, cw)
        ligne = {"monde": w, "pop": {str(k): [] for k in KS}, "cond": {str(k): [] for k in KS}, "theta_c": {str(k): [] for k in KS},
                 "controle": None}
        for p, (z, F, bruit) in enumerate(sondes):
            g = graine_entiere((31,) + cw + (p,))
            W = PV2.poids_des_tirages(n, B, g)
            CF = comparaisons(F, n)
            AF = aires_tirees(CF, W, n)
            AF0 = aires_tirees(CF, np.ones((1, n)), n)[:, 0]
            vraies = None
            if delta > 0 and nature == "nul":
                c = rho * z
                vraies = V1.aire_plan(c * delta / np.sqrt(c * c + 1), n)
            sondes_lues = {"pop": r_pop * y + bruit}
            for k in KS:
                if nature == "nul":
                    tc = float(np.quantile(vraies[:k], QP)) if vraies is not None else 0.5
                    ligne["theta_c"][str(k)].append(tc)
                    sondes_lues[f"cond{k}"] = V1.r_pour(tc, n) * y + bruit
            lignes_s = {nom: (comparaisons(s[None, :], n), s) for nom, s in sondes_lues.items()}
            for k in KS:
                qb = np.quantile(AF[:k], QP, axis=0)
                q0 = float(np.quantile(AF0[:k], QP))
                for lecture, nom in (("pop", "pop"), ("cond", f"cond{k}")):
                    if nom not in lignes_s:
                        continue
                    Cs, s = lignes_s[nom]
                    As = aires_tirees(Cs, W, n)[0]
                    a0 = float(aires_tirees(Cs, np.ones((1, n)), n)[0, 0])
                    borne = float(np.quantile(As - qb, ALPHA))
                    ligne[lecture][str(k)].append({"borne": borne, "etat": etat(a0, q0, borne), "aire": a0, "q95": q0})
                    if w == debut and p == 0 and lecture == "pop" and k in (200, 1600):
                        r = PV2.comparer_difference_au_plancher(s, F[:k], y, tache_, B, g, QP, NIVEAU)
                        e = abs(r["difference"]["bas"] - borne) + abs(r["plancher_quantile"] - q0) + abs(r["aire"] - a0)
                        if e != 0.0 or bool(r["au_dessus_du_plancher"]) != (borne > 0):
                            raise SystemExit(f"règle simulée ≠ module (k = {k}, monde {cw}) : écart {e}")
                        ligne["controle"] = (ligne["controle"] or 0.0) + e
        for lecture in ("pop", "cond"):
            ligne[f"organisme_{lecture}"] = {k: CR.etat_organisme([s["etat"] for s in v]) for k, v in ligne[lecture].items() if v}
        sortie.append(ligne)
    return json.dumps([nature, n, theta, rho]), sortie


def executer(taches):
    out = {}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for k, lignes in ex.map(tache, taches):
            out.setdefault(k, []).extend(lignes)
    for v in out.values():
        v.sort(key=lambda l: l["monde"])
    return out


def ecrire(res, sortie):
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")


def phase_nul(paquet, chemin_v1, sortie):
    debut = time.time()
    taches = []
    for n, th, rho, w in CELLULES_NUL:
        cle = (30, n, V1.THETAS.index(th), V1.RHOS.index(rho), 0)
        for a in range(0, w, 10):
            taches.append((paquet, chemin_v1, "nul", n, th, rho, V1.r_pour(th, n), cle, a, min(a + 10, w)))
    res = {"script": Path(__file__).name, "entropie": str(ENTROPIE), "ks": list(KS), "mondes": executer(taches)}
    res["duree_s"] = round(time.time() - debut, 1)
    ecrire(res, sortie)
    print(f"phase nul : {len(taches)} tâches, {res['duree_s']} s")


def phase_puissance(paquet, chemin_v1, chemin_pui_proto, sortie):
    debut = time.time()
    alt = json.loads(Path(chemin_pui_proto).read_text(encoding="utf-8"))["alternatives"]
    taches, aires = [], {}
    for n, th in ALTERNATIVES:
        a = float(alt[f"{n}:{th}"]["aire_vraie"])
        aires[f"{n}:{th}"] = a
        cle = (30, n, V1.THETAS.index(th), V1.RHOS.index(RHO_PUISSANCE), 1)
        for d in range(0, W_PUISSANCE, 5):
            taches.append((paquet, chemin_v1, "puissance", n, th, RHO_PUISSANCE, V1.r_pour(a, n), cle, d, min(d + 5, W_PUISSANCE)))
    res = {"script": Path(__file__).name, "entropie": str(ENTROPIE), "ks": list(KS), "aires_alternatives": aires,
           "mondes": executer(taches)}
    res["duree_s"] = round(time.time() - debut, 1)
    ecrire(res, sortie)
    print(f"phase puissance : {len(taches)} tâches, {res['duree_s']} s")


def phase_cout(paquet, chemin_v1, sortie):
    """Temps mesurés sur le module (un fil), médiane de trois répétitions."""
    out = {"etape_B": [], "etape_A": None}
    for n in (64, 36):
        y, delta, sondes = monde(n, 0.94, 1.0, (32, n))
        tache_ = np.repeat(np.arange(n), 2 * V1.T)
        z, F, bruit = sondes[0]
        s = V1.r_pour(0.94, n) * y + bruit
        F2 = np.vstack([F, F + 1e-3 * np.random.default_rng(0).standard_normal(F.shape)])      # 3 200 directions
        t = []
        for _ in range(3):
            t0 = time.perf_counter(); PL.comparer_scores_au_plancher(s, F[:200], y, tache_, B, 5, QP, NIVEAU); t.append(time.perf_counter() - t0)
        out["etape_B"].append({"n": n, "regle": "actuelle (plancher_v1)", "k": 200, "secondes": float(np.median(t))})
        for k in (200, 400, 800, 1600, 3200):
            t = []
            for _ in range(3):
                t0 = time.perf_counter(); PV2.comparer_difference_au_plancher(s, F2[:k], y, tache_, B, 5, QP, NIVEAU)
                t.append(time.perf_counter() - t0)
            out["etape_B"].append({"n": n, "regle": "(a) plancher_v2", "k": k, "secondes": float(np.median(t))})
            print(out["etape_B"][-1], flush=True)
    # étape A : notation d'une direction du plancher (sonde linéaire, maximum) sur des actions simulées, boucle du harnais
    rng = np.random.default_rng(1)
    d, actions = 4096, 200
    res_a = []
    for jetons in (50, 200):
        seqs = [rng.standard_normal((jetons, d)).astype(np.float32) for _ in range(actions)]
        X = rng.standard_normal((4500, d))
        plancher = PL.plancher_pour_sonde(type("S", (), {"nom": "essai", "couche": 15, "agregation": "max", "w": np.ones(d)})(),
                                          X, 4, 3)
        t0 = time.perf_counter(); PL.scores_plancher(plancher, seqs); dt = time.perf_counter() - t0
        res_a.append({"jetons_par_action": jetons, "largeur": d, "secondes_par_direction_et_action": dt / (4 * actions)})
        print(res_a[-1], flush=True)
    out["etape_A"] = res_a
    ecrire(out, sortie)


def cp(x, n):
    return (0.0 if x == 0 else float(beta.ppf(0.025, x, n - x + 1)), 1.0 if x == n else float(beta.ppf(0.975, x + 1, n - x)))


def phase_rapport(nul_json, pui_json, cout_json, sortie):
    nul = json.loads(Path(nul_json).read_text(encoding="utf-8"))
    pui = json.loads(Path(pui_json).read_text(encoding="utf-8"))
    cout = json.loads(Path(cout_json).read_text(encoding="utf-8"))
    nom, fam = ALPHA, 4 * ALPHA
    txt = [f"n_plancher pour la règle (a) de T0.7 — v1 ; entropie {ENTROPIE} ; nominal {nom:.5f} par sonde, {fam:.4f} par organisme", ""]
    out = {"nul": [], "puissance": [], "cout": cout, "tient": {}}
    tient = {(l, k): True for l in ("pop", "cond") for k in KS}
    for cle, lignes in sorted(nul["mondes"].items()):
        nature, n, th, rho = json.loads(cle)
        ctrl = [l["controle"] for l in lignes if l["controle"] is not None]
        txt.append(f"nul n={n} θ_F={th} ρ={rho} ({len(lignes)} mondes, {4 * len(lignes)} sondes) ; contrôles au module : {len(ctrl)} "
                   f"sondes, écart max. {max(ctrl) if ctrl else float('nan'):.1e}")
        e = {"n": n, "theta_F": th, "rho": rho, "mondes": len(lignes), "taux": {}}
        for k in KS:
            tc = [t for l in lignes for t in l["theta_c"][str(k)]]
            for lecture in ("pop", "cond"):
                ks = sum(s["etat"] == CR.AU_DESSUS for l in lignes for s in l[lecture][str(k)])
                nb = sum(len(l[lecture][str(k)]) for l in lignes)
                kf = sum(l[f"organisme_{lecture}"][str(k)] == "U" for l in lignes)
                cs, cf = cp(ks, nb), cp(kf, len(lignes))
                dep = cs[0] > nom or cf[0] > fam
                if dep:
                    tient[(lecture, k)] = False
                e["taux"][f"{lecture}/{k}"] = {"sonde": [ks, nb, cs], "famille": [kf, len(lignes), cf], "depasse": dep}
                txt.append(f"   k={k:>4} {'population ' if lecture == 'pop' else 'conditionnel'} : sonde {ks:>3}/{nb} = {ks / nb:.4f} "
                           f"[{cs[0]:.4f} ; {cs[1]:.4f}] ; famille {kf:>3}/{len(lignes)} = {kf / len(lignes):.4f} [{cf[0]:.4f} ; "
                           f"{cf[1]:.4f}]{'  DÉPASSE' if dep else ''}"
                           + (f" ; θ_c moy. {np.mean(tc):.4f}, e.t. {np.std(tc):.4f}" if lecture == "cond" else ""))
        out["nul"].append(e)
    txt.append("")
    for (l, k), v in sorted(tient.items(), key=lambda x: (x[0][0], x[0][1])):
        txt.append(f"lecture {l} k={k} : {'aucun dépassement établi' if v else 'DÉPASSE dans au moins une cellule'}")
        out["tient"][f"{l}/{k}"] = v
    txt.append("")
    for cle, lignes in sorted(pui["mondes"].items()):
        nature, n, th, rho = json.loads(cle)
        a = pui["aires_alternatives"][f"{n}:{th}"]
        e = {"n": n, "theta_F": th, "rho": rho, "aire": a, "puissance": {}}
        t = f"puissance n={n} θ_F={th} ρ={rho} aire vraie {a:.4f} ({4 * len(lignes)} sondes) :"
        for k in KS:
            ks = sum(s["etat"] == CR.AU_DESSUS for l in lignes for s in l["pop"][str(k)])
            nb = sum(len(l["pop"][str(k)]) for l in lignes)
            kf = sum(l["organisme_pop"][str(k)] == "U" for l in lignes)
            e["puissance"][str(k)] = {"sonde": [ks, nb, cp(ks, nb)], "famille": [kf, len(lignes)]}
            t += f" k={k} {ks / nb:.3f} [{cp(ks, nb)[0]:.3f} ; {cp(ks, nb)[1]:.3f}] (famille {kf / len(lignes):.3f}) ;"
        out["puissance"].append(e)
        txt.append(t)
    txt.append("")
    for c in cout["etape_B"]:
        txt.append(f"coût étape B : n={c['n']} règle {c['regle']} k={c['k']} : {c['secondes']:.2f} s par sonde et par jeu (un fil)")
    for c in cout["etape_A"]:
        txt.append(f"coût étape A : {c['jetons_par_action']} jetons par action, largeur {c['largeur']} : "
                   f"{c['secondes_par_direction_et_action'] * 1e6:.1f} µs par direction et par action (boucle du harnais, un fil)")
    out["texte"] = txt
    ecrire(out, sortie)
    print("\n".join(txt))


if __name__ == "__main__":
    racine, paquet, chemin_v1, phase = sys.argv[1:5]
    charger(paquet, chemin_v1)
    if phase == "nul":
        phase_nul(paquet, chemin_v1, sys.argv[5])
    elif phase == "puissance":
        phase_puissance(paquet, chemin_v1, sys.argv[5], sys.argv[6])
    elif phase == "cout":
        phase_cout(paquet, chemin_v1, sys.argv[5])
    elif phase == "rapport":
        phase_rapport(sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8])
    else:
        sys.exit(__doc__)
