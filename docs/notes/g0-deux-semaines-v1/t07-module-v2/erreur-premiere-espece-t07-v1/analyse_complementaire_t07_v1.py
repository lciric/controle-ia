#!/usr/bin/env python3
"""Analyse complémentaire de la simulation sous le nul des lectures décisives de T0.7 — v1.

Post-traitement seul des sorties de `erreur_premiere_espece_t07_v1.py` (phases nul, remèdes, puissance) : aucun appel au code
gelé, aucune donnée du programme, aucun tirage neuf hors du rééchantillonnage des intervalles de ce post-traitement (graine
fixée ci-dessous, dérivée de l'entropie du script principal).

1. Audit R4 (symétrie) de chaque cellule « propre » : demi-largeur basse moyenne (aire − borne basse) rapportée à l'écart
   type des aires entre mondes (2,4977 attendu à 0,9875) ; corrélation aire / demi-largeur ; biais et écart type du quantile
   du plancher ; probabilités gaussiennes attendues (borne seule ; règle, sonde et plancher indépendants).
2. **Multiplicateur de rétablissement** (approché) : m_A = quantile 0,99375 de (aire − aire vraie) / demi-largeur (nul A :
   borne seule) ; m_B = quantile 0,99375 de (aire_i − q95_j) / demi-largeur_i sur tous les couples (sonde i, plancher j) des
   réserves indépendantes (nul B, sonde « propre ») ; niveau bilatéral équivalent sous approximation normale :
   1 − 2 Φ(−m × 2,4977) ; intervalle à 95 % par rééchantillonnage (1 000 tirages pour m_A, 200 pour m_B, réserves
   rééchantillonnées toutes deux). Un multiplicateur m signifie : la
   demi-largeur basse devrait être m fois plus grande pour tenir 0,625 % par sonde.
3. Coût en puissance, gaussien (supposé) : écart d'aire minimal détectable à 80 % sous la règle actuelle et sous la règle
   d'un intervalle de la différence (sonde − quantile du plancher), en écarts types de l'aire.

Lancement : `python3 -I -B <ce script> <nul.json> <remedes.json> <puissance.json> <sortie.json>` (texte sur la sortie standard).
"""
from __future__ import annotations

import json
import math
import sys

import numpy as np
from scipy.stats import norm

ENTROPIE = 122652366722379967354654917555121075896
Z = float(norm.ppf(1 - 0.00625))


def niveau_equivalent(m: float) -> float:
    return 1 - 2 * norm.sf(m * Z)


def quantile_ic(x: np.ndarray, q: float, rng, b: int = 1000) -> tuple[float, list]:
    v = float(np.quantile(x, q))
    bs = [np.quantile(x[rng.integers(0, x.size, x.size)], q) for _ in range(b)]
    return v, [float(np.quantile(bs, 0.025)), float(np.quantile(bs, 0.975))]


def main(chemin_nul: str, chemin_rem: str, chemin_pui: str, sortie: str) -> None:
    nul = json.loads(open(chemin_nul, encoding="utf-8").read())
    rem = json.loads(open(chemin_rem, encoding="utf-8").read())
    pui = json.loads(open(chemin_pui, encoding="utf-8").read())
    rng = np.random.default_rng(np.random.SeedSequence(ENTROPIE, spawn_key=(11,)))
    out = {"audit": [], "multiplicateurs": [], "puissance_gaussienne": [], "remedes_multiplicateurs": []}
    txt = [f"Analyse complémentaire T0.7 — v1 ; z(0,99375) = {Z:.4f}", ""]
    for cle, lignes in nul["directs"].items():
        n, th, rho, compo, alt = json.loads(cle)
        S = [s for l in lignes for s in l["R0"]["sondes"]]
        a = np.array([s["aire"] for s in S]); b = np.array([s["bas"] for s in S]); q = np.array([s["q95"] for s in S])
        demi = a - b
        sd_a, sd_q = float(a.std(ddof=1)), float(q.std(ddof=1))
        corr_aq = float(np.corrcoef(a, q)[0, 1])
        pA = float(norm.sf(demi.mean() / sd_a))
        pB = float(norm.sf((demi.mean() + q.mean() - th) / math.sqrt(sd_a ** 2 + sd_q ** 2 - 2 * corr_aq * sd_a * sd_q)))
        e = {"n": n, "theta_F": th, "rho": rho, "compo": compo, "ecart_type_aire": sd_a, "demi_moyenne": float(demi.mean()),
             "demi_sur_ecart_type": float(demi.mean() / sd_a), "corr_aire_demi": float(np.corrcoef(a, demi)[0, 1]),
             "biais_q95": float(q.mean() - th), "ecart_type_q95": sd_q, "corr_aire_q95": corr_aq,
             "gaussien_borne_seule": pA, "gaussien_regle": pB}
        out["audit"].append(e)
        txt.append(f"audit {compo} n={n} θ_F={th:.2f} ρ={rho} : demi-largeur = {e['demi_sur_ecart_type']:.3f} e.t. de l'aire "
                   f"(2,498 visé) ; corr(aire, demi) {e['corr_aire_demi']:+.3f} ; q95 − θ_F {e['biais_q95']:+.4f}, e.t. q95 "
                   f"{sd_q:.4f} (e.t. aire {sd_a:.4f}) ; corr(aire, q95) {corr_aq:+.3f} ; gaussien : borne seule {pA:.4f}, règle {pB:.4f}")
        if compo != "propre" or th == 0.5:
            continue
        tA = (a - th) / demi
        mA, icA = quantile_ic(tA, 1 - 0.00625, rng)
        q_all = np.array([s["q95"] for s in S] + [v for monde in nul["planchers"][json.dumps([n, th, rho])] for v in monde])
        # couples (sonde i, plancher j) : sonde « propre » indépendante du plancher par construction
        tB = ((a[:, None] - q_all[None, :]) / demi[:, None]).ravel()
        mB = float(np.quantile(tB, 1 - 0.00625))
        bsB = []
        for _ in range(200):
            i = rng.integers(0, a.size, a.size); j = rng.integers(0, q_all.size, q_all.size)
            bsB.append(np.quantile(((a[i][:, None] - q_all[j][None, :]) / demi[i][:, None]).ravel(), 1 - 0.00625))
        icB = [float(np.quantile(bsB, 0.025)), float(np.quantile(bsB, 0.975))]
        m = {"n": n, "theta_F": th, "m_A": mA, "m_A_ic95": icA, "niveau_A": niveau_equivalent(mA), "m_B": mB, "m_B_ic95": icB,
             "niveau_B": niveau_equivalent(mB)}
        out["multiplicateurs"].append(m)
        txt.append(f"   multiplicateur nul A {mA:.3f} [{icA[0]:.3f} ; {icA[1]:.3f}] → niveau ≈ {m['niveau_A']:.5f} ; nul B (ρ=4) "
                   f"{mB:.3f} [{icB[0]:.3f} ; {icB[1]:.3f}] → niveau ≈ {m['niveau_B']:.5f}")
    txt.append("")
    # remèdes : mêmes multiplicateurs sur les mondes relus à R1 et R2 (nul A)
    for cle, lignes in rem["directs"].items():
        n, th, rho, compo, alt = json.loads(cle)
        for lec in ("R1", "R2"):
            S = [s for l in lignes for s in l[lec]["sondes"]]
            a = np.array([s["aire"] for s in S]); demi = a - np.array([s["bas"] for s in S])
            mA, icA = quantile_ic((a - th) / demi, 1 - 0.00625, rng)
            out["remedes_multiplicateurs"].append({"n": n, "theta_F": th, "lecture": lec, "m_A": mA, "m_A_ic95": icA})
            txt.append(f"remède {lec} n={n} θ_F={th:.2f} : multiplicateur nul A {mA:.3f} [{icA[0]:.3f} ; {icA[1]:.3f}] "
                       f"(1 = tenu ; référence R0 de la cellule ci-dessus)")
    txt.append("")
    # puissance gaussienne : écart minimal détectable à 80 %, en écarts types (s) de l'aire, plancher de même écart type
    z80 = float(norm.ppf(0.8))
    for nom, r in (("règle actuelle (borne basse > quantile bruité)", Z + z80 * math.sqrt(2)),
                   ("intervalle de la différence (même niveau)", (Z + z80) * math.sqrt(2)),
                   ("seuil connu (référence)", Z + z80)):
        out["puissance_gaussienne"].append({"regle": nom, "ecart_minimal_en_ecarts_types": r})
        txt.append(f"puissance gaussienne : {nom} : écart minimal détectable à 80 % = {r:.3f} écarts types de l'aire")
    for e in out["audit"]:
        if e["compo"] == "propre" and e["theta_F"] > 0.5:
            txt.append(f"   n={e['n']} θ_F={e['theta_F']:.2f} : 1 écart type de l'aire = {e['ecart_type_aire']:.4f} ; surcoût de "
                       f"l'intervalle de la différence ≈ {((Z + z80) * math.sqrt(2) - Z - z80 * math.sqrt(2)) * e['ecart_type_aire']:.4f} d'aire")
    txt.append("")
    alt = pui["alternatives"]
    txt.append(f"alternatives de la phase puissance : {json.dumps(alt, ensure_ascii=False)}")
    out["texte"] = txt
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    print("\n".join(txt))


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(__doc__)
    main(*sys.argv[1:])
