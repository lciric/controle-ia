#!/usr/bin/env python3
"""Prototype du remède (a) des lectures décisives de T0.7 — v1 (suite R-2270 de la consigne
`consigne-nul-lectures-decisives-t07-v1.md`, `22e95cf3…`).

Remède (a) : intervalle par blocs de tâches de la **différence « aire de la sonde − quantile 0,95 du plancher »**, les 201
aires (sonde et 200 directions) recalculées à **chaque** tirage, niveau 0,9875 (queue basse 0,625 %), « au-dessus » si la
borne basse est strictement positive. Méthodes d'intervalle, toutes sur les **mêmes** 2 000 tirages :
- `percentile_D` : percentile de D* = A*_sonde − q95(A*_plancher) ;
- `percentile_logit` : percentile de L* = logit(A*_sonde) − logit(q95*) (même signe que D* tirage par tirage : décision égale
  à celle de `percentile_D` à l'interpolation près entre deux statistiques d'ordre) ;
- `normale_logit` : L̂ − 2,4977 × écart type de L* (normale sur l'échelle logistique, écart type par rééchantillonnage) ;
- `basique_logit` : 2 L̂ − quantile 0,99375 de L* (intervalle « basique » sur l'échelle logistique) ;
- `bca_D`, `bca_logit` : percentile corrigé du biais et de l'asymétrie (BCa) de D* et de L*, accélération par le couteau
  (une tâche retirée) sur l'échantillon.

**Code gelé appelé pour tout le reste** : les mondes sont ceux de `erreur_premiere_espece_t07_v1.py` (importé par son chemin
après vérification de son empreinte `59453773…`, qui vérifie lui-même les empreintes du code gelé) : `generer`, `r_pour`, mêmes
clés de graines, mêmes effectifs ; aire et quantile du plancher ponctuels par `plancher_v1.comparer_scores_au_plancher`
(un tirage) ; état de chaque sonde par `criteres_v1.etat_pour_sonde` (résumé dont `bas` vaut quantile + borne basse de la
différence, ou son image sur l'échelle logistique : `bas` > quantile si et seulement si la borne basse est > 0), état de
l'organisme par `criteres_v1.etat_organisme` ; règle actuelle (R0) sur les mondes de puissance par `lecture_v1.lecture_jeux`
(fonction `lire` du script v1). **Seul le rééchantillonnage de la différence est neuf** (prototype) : aires des tirages par
matrices de comparaisons entre tâches (A*_k = wᵀ C_k w / (T² n²), w = multiplicités des tâches), **éprouvées égales à
`evaluation.aire_sous_courbe`** sur trois tirages par lot de mondes (écart écrit), aires ponctuelles égales à celles du code
gelé (écart écrit).

Graines (R9) : numpy.random.SeedSequence(ENTROPIE_A, spawn_key=(17, <clé du monde>, sonde)) pour les tirages du prototype ;
entropie tirée une fois le 2026-11-10 à 17:47:43 UTC (`date -u`, `secrets.randbits(128)`), sans lecture de données ; les
mondes gardent l'entropie et les clés du script v1.

Lancement (quatre processus, un fil chacun) :
  `python3 -I -B <ce script> <racine du dépôt> <script v1> nul <sortie.json>`
  `python3 -I -B <ce script> <racine du dépôt> <script v1> puissance <nul-v1.json> <sortie.json>`
  `python3 -I -B <ce script> <racine du dépôt> <script v1> rapport <puissance-v1.json> <proto-nul.json> <proto-puissance.json> <sortie.json>`
"""
from __future__ import annotations

import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import hashlib
import importlib.util
import json
import math
import platform
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np
from scipy.stats import beta, norm

SHA_V1 = "59453773ee08e06aa1abef3d7777935f19150ac84241ac6528639f7fc1c69970"
ENTROPIE_A = 328279692206389441950883693702200426909
B = 2000
NIVEAU = 1 - 0.05 / 4
ALPHA = (1 - NIVEAU) / 2
Z_ALPHA = float(norm.ppf(ALPHA))
METHODES = ("percentile_D", "percentile_logit", "normale_logit", "basique_logit", "bca_D", "bca_logit")
SUR_LOGIT = {"percentile_logit", "normale_logit", "basique_logit", "bca_logit"}
# mondes : ceux du script v1 (phase nul), fixés avant tout lancement
W_RHO4 = {(64, 0.50): 60, (64, 0.62): 200, (64, 0.78): 200, (64, 0.94): 400,
          (36, 0.50): 60, (36, 0.62): 200, (36, 0.78): 200, (36, 0.94): 400}
W_RHO1 = {0.50: 100, 0.62: 200, 0.78: 200, 0.94: 200}
W_ALIGNEE = 100
ALTERNATIVES = ((64, 0.94), (64, 0.62), (36, 0.94), (36, 0.62))
W_PUISSANCE = 75
RHO1_PUISSANCE = ((64, 0.94), (64, 0.62))

V1 = None


def charger(racine: str, chemin_v1: str) -> None:
    global V1
    sha = hashlib.sha256(Path(chemin_v1).read_bytes()).hexdigest()
    if sha != SHA_V1:
        raise SystemExit(f"script v1 : empreinte {sha} ≠ {SHA_V1} : arrêt")
    spec = importlib.util.spec_from_file_location("nul_t07_v1", chemin_v1)
    V1 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(V1)
    V1.charger(racine)                       # vérifie les empreintes du code gelé et l'importe


def logit(a):
    a = np.clip(np.asarray(a, dtype=np.float64), 1e-9, 1 - 1e-9)
    return np.log(a) - np.log1p(-a)


def expit(x):
    return 1.0 / (1.0 + np.exp(-x))


# --------------------------------------------------------------------------------------- rééchantillonnage de la différence
def comparaisons(X: np.ndarray, n: int) -> np.ndarray:
    """C[k, t, u] = #(positif de t > négatif de u) + 0,5 #(égalités), pour chaque direction k (ordre du script v1 : tâche,
    condition 0 = positive, action). Comptage par tri (rang de chaque positif parmi les négatifs triés, cumul par tâche) ;
    voie directe par comparaison de toutes les paires si un ex aequo positif / négatif existe dans la direction."""
    T = V1.T
    k = X.shape[0]
    x = X.reshape(k, n, 2, T)
    pos, neg = x[:, :, 0, :].reshape(k, n * T), x[:, :, 1, :].reshape(k, n * T)
    tache_neg = np.repeat(np.arange(n), T)
    C = np.empty((k, n, n))
    for a in range(0, k, 25):
        P, N = pos[a:a + 25], neg[a:a + 25]
        kc = P.shape[0]
        for j in range(kc):
            if np.intersect1d(P[j], N[j]).size:
                p = P[j].reshape(n, T)[:, :, None, None]
                q = N[j].reshape(n, T)[None, None, :, :]
                C[a + j] = (p > q).sum(axis=(1, 3)) + 0.5 * (p == q).sum(axis=(1, 3))
                continue
            ordre = np.argsort(N[j], kind="stable")
            cum = np.zeros((n * T + 1, n))
            cum[np.arange(1, n * T + 1), tache_neg[ordre]] = 1.0
            np.cumsum(cum, axis=0, out=cum)
            r = np.searchsorted(N[j][ordre], P[j], side="left")
            C[a + j] = cum[r].reshape(n, T, n).sum(axis=1)
    return C


def poids(rng, n: int) -> np.ndarray:
    idx = rng.integers(0, n, size=(B, n))
    W = np.zeros((B, n))
    np.add.at(W, (np.repeat(np.arange(B), n), idx.ravel()), 1.0)
    return W, idx


def aires_tirees(C: np.ndarray, W: np.ndarray, n: int) -> np.ndarray:
    T = V1.T
    out = np.empty((C.shape[0], W.shape[0]))
    for a in range(0, C.shape[0], 25):
        M = np.matmul(W[None], C[a:a + 25])
        out[a:a + 25] = (M * W[None]).sum(-1)
    return out / (T * T * n * n)


def bca(theta: float, boot: np.ndarray, jack: np.ndarray) -> float:
    p = (np.sum(boot < theta) + 0.5 * np.sum(boot == theta)) / boot.size
    p = min(max(p, 0.5 / boot.size), 1 - 0.5 / boot.size)
    z0 = float(norm.ppf(p))
    d = jack.mean() - jack
    s2 = float((d ** 2).sum())
    a = float((d ** 3).sum() / (6 * s2 ** 1.5)) if s2 > 0 else 0.0
    den = 1 - a * (z0 + Z_ALPHA)
    if den <= 0:
        return float(np.min(boot))
    return float(np.quantile(boot, float(norm.cdf(z0 + (z0 + Z_ALPHA) / den))))


def lire_remede(n: int, y, sonde, plancher, rng, controle: bool) -> dict:
    """Une sonde contre son plancher : aire et quantile ponctuels par le code gelé, bornes basses des six méthodes, états."""
    PL, CR, LV1 = V1.PL, V1.CR, V1.LV1
    tache = np.repeat(np.arange(n), 2 * V1.T)
    r = PL.comparer_scores_au_plancher(sonde, plancher, y, tache, 1, 0, V1.QUANTILE_PLANCHER, NIVEAU)
    a_hat, q_hat = float(r["aire"]), float(r["plancher_quantile"])
    X = np.vstack([sonde[None, :], plancher])
    C = comparaisons(X, n)
    T = V1.T
    S = C.sum(axis=(1, 2))
    A0 = S / (T * T * n * n)
    ecart_point = max(abs(A0[0] - a_hat), abs(float(np.quantile(A0[1:], 0.95)) - q_hat))
    W, idx = poids(rng, n)
    A = aires_tirees(C, W, n)
    ecart_tirage = 0.0
    if controle:
        membres = [np.flatnonzero(tache == u) for u in range(n)]
        sev = __import__("controle_ia.sondes.evaluation", fromlist=["aire_sous_courbe"])
        for b in range(3):
            i = np.concatenate([membres[c] for c in idx[b]])
            for j in (0, 1, 200):
                ecart_tirage = max(ecart_tirage, abs(sev.aire_sous_courbe(X[j][i], y[i]) - A[j, b]))
    q_b = np.quantile(A[1:], V1.QUANTILE_PLANCHER, axis=0)
    D_b = A[0] - q_b
    L_b = logit(A[0]) - logit(q_b)
    D_hat, L_hat = a_hat - q_hat, float(logit(a_hat) - logit(q_hat))
    rows, cols = C.sum(axis=2), C.sum(axis=1)
    diag = np.diagonal(C, axis1=1, axis2=2)
    A_j = (S[:, None] - rows - cols + diag) / (T * T * (n - 1) ** 2)        # (directions, tâche retirée)
    q_j = np.quantile(A_j[1:], V1.QUANTILE_PLANCHER, axis=0)
    D_j = A_j[0] - q_j
    L_j = logit(A_j[0]) - logit(q_j)
    lb = {"percentile_D": float(np.quantile(D_b, ALPHA)),
          "percentile_logit": float(np.quantile(L_b, ALPHA)),
          "normale_logit": float(L_hat + Z_ALPHA * L_b.std(ddof=1)),
          "basique_logit": float(2 * L_hat - np.quantile(L_b, 1 - ALPHA)),
          "bca_D": bca(D_hat, D_b, D_j),
          "bca_logit": bca(L_hat, L_b, L_j)}
    etats = {}
    for m, v in lb.items():
        bas = float(expit(logit(q_hat) + v)) if m in SUR_LOGIT else q_hat + v
        etats[m] = CR.etat_pour_sonde({"aire": a_hat, "bas": bas, "plancher": {"quantile": q_hat}, "triviaux": {}})
    return {"aire": a_hat, "q95": q_hat, "D": D_hat, "L": L_hat, "bornes": lb, "etats": etats,
            "ecart_point": float(ecart_point), "ecart_tirage": float(ecart_tirage), "sd_D": float(D_b.std(ddof=1))}


def tache(args):
    racine, chemin_v1, n, theta, rho, compo, r_sonde, cle, debut, fin, r0 = args
    if V1 is None:
        charger(racine, chemin_v1)
    sortie = []
    for w in range(debut, fin):
        y, sondes, planchers = V1.generer(n, theta, rho, compo, r_sonde, tuple(cle) + (w,))
        ligne = {"monde": w, "sondes": []}
        for p in range(V1.N_SONDES):
            rng = np.random.default_rng(np.random.SeedSequence(ENTROPIE_A, spawn_key=(17,) + tuple(cle) + (w, p)))
            ligne["sondes"].append(lire_remede(n, y, sondes[p], planchers[p], rng, controle=(w == debut and p == 0)))
        ligne["organisme"] = {m: V1.CR.etat_organisme([s["etats"][m] for s in ligne["sondes"]]) for m in METHODES}
        if r0:
            cle7 = (7,) + tuple(cle[1:]) + (w,)
            ligne["R0"] = V1.lire(n, y, sondes, planchers, V1.TIRAGES, V1.NIVEAU, cle7)
        sortie.append(ligne)
    return json.dumps([n, theta, rho, compo, list(cle)]), sortie


def morceaux(total: int, taille: int):
    return [(a, min(a + taille, total)) for a in range(0, total, taille)]


def executer(taches):
    out = {}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for cle, lignes in ex.map(tache, taches):
            out.setdefault(cle, []).extend(lignes)
    for v in out.values():
        v.sort(key=lambda l: l["monde"])
    return out


def entete() -> dict:
    return {"script": Path(__file__).name, "entropie_prototype": str(ENTROPIE_A), "script_v1": SHA_V1, "B": B, "niveau": NIVEAU,
            "methodes": list(METHODES), "numpy": np.__version__, "python": platform.python_version()}


def phase_nul(racine: str, chemin_v1: str, sortie: str) -> None:
    debut = time.time()
    taches = []
    for (n, th), w in W_RHO4.items():
        it = V1.THETAS.index(th)
        for a, b in morceaux(w, 10):
            taches.append((racine, chemin_v1, n, th, 4.0, "propre", V1.r_pour(th, n), (1, n, it, 0, 0, 0), a, b, False))
    for n in (64, 36):
        for th, w in W_RHO1.items():
            it = V1.THETAS.index(th)
            for a, b in morceaux(w, 10):
                taches.append((racine, chemin_v1, n, th, 1.0, "propre", V1.r_pour(th, n), (2, n, it, 1, 0, 0), a, b, False))
    for ir, rho in enumerate(V1.RHOS):
        for a, b in morceaux(W_ALIGNEE, 10):
            taches.append((racine, chemin_v1, 64, 0.94, rho, "alignee", 0.0, (1, 64, 3, ir, 1, 0), a, b, False))
    res = entete()
    res.update({"phase": "nul", "mondes": executer(taches), "duree_s": round(time.time() - debut, 1)})
    ecrire(res, sortie)
    print(f"phase nul du prototype : {len(taches)} tâches, {res['duree_s']} s")


def phase_puissance(racine: str, chemin_v1: str, chemin_nul_v1: str, sortie: str) -> None:
    """Alternatives : sonde « propre » d'aire vraie θ_F + 3,34 × écart type des aires nulles de la cellule (sortie de la phase nul
    du script v1, comme sa phase de puissance), plafonnée à 0,995 ; ρ = 4 (avec la règle actuelle R0 par le code gelé) et ρ = 1
    pour les deux cellules à 64 tâches."""
    debut = time.time()
    nul = json.loads(Path(chemin_nul_v1).read_text(encoding="utf-8"))
    taches, alternatives = [], {}
    for n, th in ALTERNATIVES:
        aires = [s["aire"] for l in nul["directs"][json.dumps([n, th, 4.0, "propre", 0])] for s in l["R0"]["sondes"]]
        e = float(np.std(aires, ddof=1))
        a_alt = min(0.995, th + V1.Z_PUISSANCE * e)
        r = V1.r_pour(a_alt, n)
        alternatives[f"{n}:{th}"] = {"aire_vraie": a_alt, "ecart_type_nul": e, "r_sonde": r}
        it = V1.THETAS.index(th)
        for a, b in morceaux(W_PUISSANCE, 5):
            taches.append((racine, chemin_v1, n, th, 4.0, "propre", r, (1, n, it, 0, 0, 1), a, b, True))
        if (n, th) in RHO1_PUISSANCE:
            for a, b in morceaux(W_PUISSANCE, 5):
                taches.append((racine, chemin_v1, n, th, 1.0, "propre", r, (1, n, it, 1, 0, 1), a, b, False))
    res = entete()
    res.update({"phase": "puissance", "alternatives": alternatives, "mondes": executer(taches),
                "duree_s": round(time.time() - debut, 1)})
    ecrire(res, sortie)
    print(f"phase puissance du prototype : {len(taches)} tâches, {res['duree_s']} s")


# ----------------------------------------------------------------------------------------------------------------- rapport
def cp(x: int, n: int):
    return (0.0 if x == 0 else float(beta.ppf(0.025, x, n - x + 1)), 1.0 if x == n else float(beta.ppf(0.975, x + 1, n - x)))


def compte(x: int, n: int) -> dict:
    return {"k": int(x), "n": int(n), "taux": x / n, "cp95": cp(x, n)}


def resumer(lignes: list) -> dict:
    out = {}
    for m in METHODES:
        k = sum(s["etats"][m] == V1.CR.AU_DESSUS for l in lignes for s in l["sondes"])
        nb = sum(len(l["sondes"]) for l in lignes)
        f = sum(l["organisme"][m] == "U" for l in lignes)
        out[m] = {"sonde": compte(k, nb), "famille": compte(f, len(lignes))}
    if lignes and "R0" in lignes[0]:
        k = sum(s["etat"] == V1.CR.AU_DESSUS for l in lignes for s in l["R0"]["sondes"])
        nb = sum(len(l["R0"]["sondes"]) for l in lignes)
        out["R0"] = {"sonde": compte(k, nb), "famille": compte(sum(l["R0"]["organisme"] == "U" for l in lignes), len(lignes))}
    out["ecart_point_max"] = max(s["ecart_point"] for l in lignes for s in l["sondes"])
    out["ecart_tirage_max"] = max(s["ecart_tirage"] for l in lignes for s in l["sondes"])
    out["discordances_percentile_D_logit"] = sum(s["etats"]["percentile_D"] != s["etats"]["percentile_logit"]
                                                 for l in lignes for s in l["sondes"])
    out["sd_D_moyen"] = float(np.mean([s["sd_D"] for l in lignes for s in l["sondes"]]))
    return out


def phase_rapport(racine: str, chemin_v1: str, chemin_pui_v1: str, chemin_nul: str, chemin_pui: str, sortie: str) -> None:
    pui_v1 = json.loads(Path(chemin_pui_v1).read_text(encoding="utf-8"))
    nul = json.loads(Path(chemin_nul).read_text(encoding="utf-8"))
    pui = json.loads(Path(chemin_pui).read_text(encoding="utf-8"))
    nominal, famille = ALPHA, 4 * ALPHA
    out = {"entete": entete(), "nominal_sonde": nominal, "nominal_famille": famille, "nul": [], "puissance": [], "tient": {}}
    txt = [f"Prototype du remède (a), T0.7 — v1 ; numpy {np.__version__} ; entropie du prototype {ENTROPIE_A} ; B = {B} ;"
           f" nominal {nominal:.5f} par sonde, {famille:.4f} par organisme", ""]
    depasse = {m: [] for m in METHODES}
    for cle, lignes in sorted(nul["mondes"].items()):
        n, th, rho, compo, k = json.loads(cle)
        r = resumer(lignes)
        out["nul"].append({"n": n, "theta_F": th, "rho": rho, "compo": compo, "mondes": len(lignes), "resume": r})
        txt.append(f"nul {compo} n={n} θ_F={th:.2f} ρ={rho} ({len(lignes)} mondes) ; écarts au code gelé : ponctuel "
                   f"{r['ecart_point_max']:.1e}, tirages {r['ecart_tirage_max']:.1e} ; discordances percentile D / logit "
                   f"{r['discordances_percentile_D_logit']} ; e.t. moyen de D* {r['sd_D_moyen']:.4f}")
        for m in METHODES:
            s, f = r[m]["sonde"], r[m]["famille"]
            marque = ""
            if s["cp95"][0] > nominal or f["cp95"][0] > famille:
                depasse[m].append(f"{compo} n={n} θ_F={th} ρ={rho}")
                marque = "  DÉPASSE"
            txt.append(f"   {m:17s} sonde {s['k']:>3}/{s['n']} = {s['taux']:.4f} [{s['cp95'][0]:.4f} ; {s['cp95'][1]:.4f}] ;"
                       f" famille {f['k']:>3}/{f['n']} = {f['taux']:.4f} [{f['cp95'][0]:.4f} ; {f['cp95'][1]:.4f}]{marque}")
    txt.append("")
    for m in METHODES:
        tot = sum(e["resume"][m]["sonde"]["k"] for e in out["nul"]); nb = sum(e["resume"][m]["sonde"]["n"] for e in out["nul"])
        out["tient"][m] = {"cellules_depassees": depasse[m], "total_sonde": compte(tot, nb)}
        txt.append(f"{m:17s} : cellules où la borne basse de Clopper-Pearson dépasse le nominal : "
                   f"{len(depasse[m])} {depasse[m] if depasse[m] else ''} ; toutes cellules : {tot}/{nb} = {tot / nb:.4f}")
    txt.append("")
    for cle, lignes in sorted(pui["mondes"].items()):
        n, th, rho, compo, k = json.loads(cle)
        alt = pui["alternatives"][f"{n}:{th}"]
        r = resumer(lignes)
        out["puissance"].append({"n": n, "theta_F": th, "rho": rho, "alternative": alt, "mondes": len(lignes), "resume": r})
        t = (f"puissance n={n} θ_F={th:.2f} ρ={rho} aire vraie {alt['aire_vraie']:.4f} ({len(lignes)} mondes, "
             f"{4 * len(lignes)} sondes) : ")
        if "R0" in r:
            s = r["R0"]["sonde"]
            t += f"R0 {s['taux']:.3f} [{s['cp95'][0]:.3f} ; {s['cp95'][1]:.3f}] ; "
        t += " ; ".join(f"{m} {r[m]['sonde']['taux']:.3f}" for m in METHODES)
        txt.append(t)
        if n == 64 and th == 0.94 and rho == 4.0:          # reproduction : R0 de la phase puissance du script v1
            v1 = {l["monde"]: l for l in pui_v1["directs"][json.dumps([64, 0.94, 4.0, "propre", 1])]}
            communs = [l for l in lignes if l["monde"] in v1]
            ecart = max(abs(s["bas"] - t["bas"]) + abs(s["q95"] - t["q95"]) for l in communs
                        for s, t in zip(l["R0"]["sondes"], v1[l["monde"]]["R0"]["sondes"]))
            out["reproduction_R0_v1"] = {"mondes": len(communs), "ecart_max": ecart}
            txt.append(f"   reproduction de R0 (script v1, {len(communs)} mondes communs) : écart max. borne + quantile {ecart:.1e}")
    out["texte"] = txt
    ecrire(out, sortie)
    print("\n".join(txt))


def ecrire(res: dict, sortie: str) -> None:
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")


if __name__ == "__main__":
    if len(sys.argv) < 5:
        sys.exit(__doc__)
    racine, chemin_v1, phase = sys.argv[1], sys.argv[2], sys.argv[3]
    charger(racine, chemin_v1)
    if phase == "nul" and len(sys.argv) == 5:
        phase_nul(racine, chemin_v1, sys.argv[4])
    elif phase == "puissance" and len(sys.argv) == 6:
        phase_puissance(racine, chemin_v1, sys.argv[4], sys.argv[5])
    elif phase == "rapport" and len(sys.argv) == 8:
        phase_rapport(racine, chemin_v1, sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
    else:
        sys.exit(__doc__)
