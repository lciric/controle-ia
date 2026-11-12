"""Contre-lecture GD8 (R2) — incertitude de graine de n80 par ajustement de la courbe de puissance (aucun tirage nouveau).

Lit les sorties de la v8 (graine 20261029 et compléments graines 1, 2, 3) pour la cellule la plus exigeante (K_h = 5, K_s = 10,
biais 0,0125, k = 8, A et B au même ρ ∈ {0,05 ; 0,17}) ; pour chaque mesure (retenue e-BH, « seuil 40 » ; atteinte de 160) prend
les points évalués par la dichotomie (n, puissance sur 2 000 répétitions, tirages indépendants d'un n à l'autre), garde ceux dont la
puissance est dans [0,5 ; 0,99], ajuste une régression logistique binomiale logit(P) = a + b·n (moindres carrés repondérés itérés,
poids 2 000) et rend n80 = (logit 0,8 − a)/b, n90 de même, leur écart-type par la méthode delta, et la déviance par degré de liberté
(contrôle de l'ajustement). Ajustement par graine puis sur les quatre graines réunies. Aucune graine : calcul déterministe.

Usage : python3 -I -B ajustement-n80-gd8-v1.py DOSSIER_V8 SORTIE.json
"""
import hashlib
import json
import math
import os
import re
import sys

import numpy as np

DOSSIER, SORTIE = sys.argv[1:3]
REPS = 2000
LOGIT = lambda p: math.log(p / (1 - p))


def fichiers(rho):
    d = {20261029: f"simulation-puissance-garde-delta-v8-sortie-meme-rho{rho}.json"}
    for g in (1, 2, 3):
        d[g] = f"simulation-puissance-garde-delta-v8-complement-graine{g}-meme-rho{rho}.json"
    return d


def points(chemin, mesure):
    d = json.load(open(chemin, encoding="utf-8"))
    for nom, loi in d["lois"].items():
        m = re.search(r"Kh(\d+)_Ks(\d+)_", nom)
        if int(m.group(1)) == 5 and int(m.group(2)) == 10 and "n_pour_puissance_0_8_fiche" in loi:
            v = loi["n_pour_puissance_0_8_fiche"].get("delta=0.05|biais=0.0125|k=8")
            if v is not None:
                pts = [(int(n), p[mesure]) for n, p in v["points_evalues"].items()]
                return sorted(pts), {c: v[c][mesure]["n_approx"] for c in ("n80", "n90")}
    raise SystemExit(f"cellule absente : {chemin}")


def ajuster(pts):
    pts = [(n, p) for n, p in pts if 0.5 <= p <= 0.99]
    n = np.array([x for x, _ in pts], dtype=float)
    y = np.array([p for _, p in pts], dtype=float)
    X = np.column_stack([np.ones_like(n), n])
    beta = np.array([0.0, 0.0])
    for _ in range(100):
        eta = X @ beta
        mu = 1 / (1 + np.exp(-eta))
        W = REPS * mu * (1 - mu)
        z = eta + (y - mu) / (mu * (1 - mu))
        A = X.T @ (W[:, None] * X)
        nouveau = np.linalg.solve(A, X.T @ (W * z))
        if np.max(np.abs(nouveau - beta)) < 1e-12:
            beta = nouveau
            break
        beta = nouveau
    mu = 1 / (1 + np.exp(-(X @ beta)))
    cov = np.linalg.inv(X.T @ ((REPS * mu * (1 - mu))[:, None] * X))
    with np.errstate(divide="ignore", invalid="ignore"):
        dev = 2 * REPS * np.sum(np.where(y > 0, y * np.log(y / mu), 0) + np.where(y < 1, (1 - y) * np.log((1 - y) / (1 - mu)), 0))
    ddl = len(y) - 2
    res = {"points_utilises": len(y), "a": float(beta[0]), "b": float(beta[1]), "deviance_par_ddl": float(dev / ddl) if ddl > 0 else None}
    for cible in (0.8, 0.9):
        a, b = beta
        nc = (LOGIT(cible) - a) / b
        grad = np.array([-1 / b, -(LOGIT(cible) - a) / b ** 2])
        sd = math.sqrt(float(grad @ cov @ grad))
        # surdispersion : l'écart-type est multiplié par √(déviance/ddl) si celle-ci dépasse 1
        f = math.sqrt(max(1.0, res["deviance_par_ddl"] or 1.0))
        res[f"n{int(round(cible * 100))}"] = {"estime": nc, "ecart_type": sd, "ecart_type_corrige_surdispersion": sd * f,
                                               "ecart_type_relatif_corrige": sd * f / nc}
    return res


sortie = {"script": os.path.basename(__file__), "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
          "numpy": np.__version__, "empreintes_entrees": {}, "lignes": {}}
for rho in ("0.05", "0.17"):
    for mesure in ("retenue_ebh", "atteinte_160"):
        ligne = {"par_graine": {}}
        tous = []
        for g, f in fichiers(rho).items():
            chemin = os.path.join(DOSSIER, f)
            sortie["empreintes_entrees"][f] = hashlib.sha256(open(chemin, "rb").read()).hexdigest()
            pts, dicho = points(chemin, mesure)
            tous += pts
            aj = ajuster(pts)
            ligne["par_graine"][str(g)] = {"dichotomie": dicho, "ajustement": aj}
        ligne["quatre_graines_reunies"] = ajuster(tous)
        sortie["lignes"][f"rho={rho}|{mesure}"] = ligne
with open(SORTIE, "x", encoding="utf-8") as fh:
    json.dump(sortie, fh, indent=1, ensure_ascii=False)
    fh.write("\n")
for k, l in sortie["lignes"].items():
    r = l["quatre_graines_reunies"]
    print(k, "dichotomie :", [v["dichotomie"]["n80"] for v in l["par_graine"].values()],
          "| ajusté n80 = %.1f ± %.1f (%.1f %%), n90 = %.1f ± %.1f, déviance/ddl %.2f" % (
              r["n80"]["estime"], r["n80"]["ecart_type_corrige_surdispersion"], 100 * r["n80"]["ecart_type_relatif_corrige"],
              r["n90"]["estime"], r["n90"]["ecart_type_corrige_surdispersion"], r["deviance_par_ddl"]),
          "| par graine :", ["%.1f" % v["ajustement"]["n80"]["estime"] for v in l["par_graine"].values()])
