#!/usr/bin/env python3
"""Devis de la course A1-v4 (attaque de Goodhart contre le nul v9), brouillon 3 — recalcul sur les taux mesurés de la
troisième course d'A1-v3 (note W2, `breche-w2-v1/couts-suite-w2-v1.txt`, ligne 1 : 0,0413 et 0,0632 USD, 8,5 et 9,4 s par appel).
Hypothèses du code v4 : `APPELS_PAR_UNITE` W1 (36, 48), W2 (34, 40) (`pole/attaque_goodhart_v4.py`, ligne 73) ; W2 gradué pris
comme W2 (deux suites sous v9 sans promotion = 32 appels, 2 à 8 sous v8 ; une promotion sous v9 raccourcit la suite : borne haute).
Aucune donnée de course lue ; arithmétique seule ; `python3 -I -B`."""
import math

Z = 1.959963984540054
def wilson(k, n):
    p = k / n; d = 1 + Z * Z / n; c = (p + Z * Z / (2 * n)) / d
    h = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))

TAUX = (0.0413, 0.0632)        # USD par appel, mesurés (W2, W1) à la troisième course
SEC = (8.5, 9.4)               # s par appel, mesurées (W2, W1) ; 40 s = hypothèse haute gardée (brouillon 2, § 4)
TAUX_CODE, SEC_CODE = 0.062, 7.6  # bloc plan-gele du brouillon 2 (A1, transcrit) : ce que le lanceur calcule lui-même
APU = {"W1": (36, 48), "W2": (34, 40), "W2g": (34, 40)}
CARTES = 24

def devis(mondes):
    bas = sum(CARTES * APU[w][0] for w in mondes); haut = sum(CARTES * APU[w][1] for w in mondes)
    maxi = CARTES * 64 * len(mondes)
    return {"appels_attendus": (bas, haut), "appels_max": maxi,
            "usd_attendus_taux_mesures": (round(bas * TAUX[0], 2), round(haut * TAUX[1], 2)),
            "usd_max_taux_mesure_haut": round(maxi * TAUX[1], 2), "usd_max_taux_code": round(maxi * TAUX_CODE, 2),
            "h_appels_attendues": (round(bas * SEC[0] / 3600, 2), round(haut * SEC[1] / 3600, 2)),
            "h_appels_max_9_4s": round(maxi * SEC[1] / 3600, 2), "h_appels_max_40s": round(maxi * 40 / 3600, 2)}

print("# devis A1-v4 brouillon 3 (arithmétique, aucune donnée de course)")
for m in (("W1", "W2"), ("W2", "W2g")):
    print("variante", "+".join(m), ":", devis(m))
# appels mesurés par monde à la troisième course (note W2, couts-suite-w2-v1.txt, lignes 2 et 3) : W1 859, W2 821 (34,21 par unité)
print("variante (i) aux appels mesurés : 859 + 821 =", 859 + 821, "appels ;",
      round(859 * 0.0632 + 821 * 0.0413, 1), "à", round((859 + 821) * 0.0632, 1), "USD")
print("variante (ii) aux appels mesurés : 2 × 821 =", 2 * 821, "appels ;", round(1642 * 0.0413, 1), "à", round(1642 * 0.0632, 1), "USD")
# rejeux : 24 unités × 2 mondes × 32 lois × 200 rejeux sous v9 (brouillon 2, § 12)
ev = 24 * 2 * 32 * 200
print("rejeux sous v9 :", ev, "évaluations ; h sur 2 cœurs à 0,5 s :", round(ev * 0.5 / 7200, 2), "; à 0,22 s :", round(ev * 0.22 / 7200, 2),
      "; à 0,19 s :", round(ev * 0.19 / 7200, 2))
# machine (hôte durable) : 0,0617 USD/h mesuré (registres/depenses.md l. 371) ; 0,40 USD/h = prix maximal admis ; vie au plus 80 h
for h in (4.7, 12, 24, 48, 80):
    print(f"machine {h} h : {h * 0.0617:.2f} USD à 0,0617/h ; {h * 0.40:.2f} USD à 0,40/h")
print("Wilson à 24 unités :", {k: tuple(round(x, 4) for x in wilson(k, 24)) for k in range(0, 13)})
print("plafond de multiplicité 1 − 0,95^16 =", round(1 - 0.95 ** 16, 4))
