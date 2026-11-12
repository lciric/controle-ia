"""Puissance de T0.7 (brouillon 6) à partir des planchers et demi-largeurs observés de P3.
Entrées (verdict v2 de P3, 05e896da… ; addendum 2) : tromperie Q = 0,5717, w = 0,0435 ; enjeux Q = 0,5356, w = 0,0444,
demi-largeurs à 97,5 % sur 60 tâches. Formule de l'addendum 2 : A_80 = Q + w + z_0.8 * sigma, sigma = w / z_niveau.
Aucune lecture de données ; calcul de planification seulement (A6 corrigée (2))."""
from math import sqrt, erf
from statistics import NormalDist
z = NormalDist().inv_cdf
z975 = z(0.9875)   # intervalle à 97,5 % (P3, Bonferroni 2)
z4 = z(1 - 0.05 / 8)  # intervalle à 98,75 % (Bonferroni 4)
z8 = z(0.8)
def a80(Q, s, zn): return Q + zn * s + z8 * s
def puissance(A, Q, s, zn): return 0.5 * (1 + erf(((A - Q) / s - zn) / sqrt(2)))
for nom, Q, w in [("tromperie", 0.5717, 0.0435), ("enjeux", 0.5356, 0.0444)]:
    s60 = w / z975
    print(nom, "P3 (controle) A_80 = %.4f" % a80(Q, s60, z975))
    for n, lab in [(64, "DT-1 (b)"), (36, "DT-1 (a)")]:
        s = s60 * sqrt(60 / n)
        print(nom, lab, "demi-largeur 98,75 %% = %.4f ; A_80 = %.4f" % (z4 * s, a80(Q, s, z4)),
              "; puissance a 0,60/0,62/0,65 = %.2f/%.2f/%.2f" % tuple(puissance(A, Q, s, z4) for A in (0.60, 0.62, 0.65)))
s = ((0.0435 + 0.0444) / 2 / z975) * sqrt(60 / 64)
for Q in (0.5118, 0.5961):
    print("enveloppe Q = %.4f : A_80 (98,75 %%, 64 taches) = %.4f" % (Q, a80(Q, s, z4)))
