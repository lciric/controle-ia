"""Contre-lecture v6, CV6-4 : comparaisons aux bornes exactes en flottant.
(1) L tel que le script le calcule pour E = 60 (dix plis de 6, K = 39, rang 38) ; 0,4 L, 1,6 L, 2 L ; une cellule à 24/1 200.
(2) Excès apparié exactement égal à 0,02 en valeur rationnelle (taux du bras M4 : moyenne de cinq taux k/1 200 ; taux à
    τ = 0 : moyenne de cinq taux j/60), calculé comme le script (moyennes de booléens), comparé à 0,02.
(3) Différences de deux médianes de même valeur rationnelle (réelles k/60, mélange k/1 200) : nulles en flottant ?
Graine : numpy.random.default_rng(1) (identique au calcul en ligne qui a produit verif-flottant-sortie.txt)."""
from fractions import Fraction as F

import numpy as np

L = sum(6 * ((40 - 38) / 40) for _ in range(10)) / 60
print('L', repr(L), '0.4L', repr(0.4 * L), '1.6L', repr(1.6 * L), '2L', repr(2 * L), '0.02<0.4L', 0.02 < 0.4 * L,
      '24/1200<0.4L', np.mean(np.r_[np.ones(24), np.zeros(1176)].astype(bool)) < 0.4 * L)
rng = np.random.default_rng(1); n = 0; plus = 0; moins = 0
for it in range(20000):
    j = rng.integers(0, 8, size=5)
    J = j.sum()
    K = J * 20 + 120
    k = rng.multinomial(K, [0.2] * 5)
    A0 = [np.zeros(60, bool) for _ in range(5)]
    for s in range(5):
        A0[s][:j[s]] = True
    A2 = [np.zeros(1200, bool) for _ in range(5)]
    for s in range(5):
        A2[s][:k[s]] = True
    t2 = np.mean([a.mean() for a in A2]); t0 = np.mean([a.mean() for a in A0])
    d = t2 - t0
    assert F(int(K), 6000) - F(int(J), 300) == F(1, 50)
    n += 1; plus += d > 0.02; moins += d < 0.02
print('excès exactement 0,02 (rationnel) :', n, 'cas ;', plus, 'lus > 0,02 en flottant ;', moins, 'lus < 0,02')
# (3) D, D′ : médiane réelle (deux sondes du milieu, taux k/60) moins médiane du mélange (taux k/1 200), de même valeur
#     rationnelle : la différence flottante n'est pas toujours nulle (une borne basse « exactement 0 » peut être lue > 0).
n = 0; nz = 0; ex = []
for a in range(0, 8):
    for b in range(a, 8):
        r = float(np.median(np.array([a / 60, b / 60])))
        for c in range(0, 160):
            d = (a + b) * 20 - c
            if d < c or d > 160:
                continue
            m = float(np.median(np.array([c / 1200, d / 1200])))
            assert F(a + b, 120) == F(c + d, 2400)
            n += 1; z = r - m
            if z != 0:
                nz += 1; ex.append((a, b, c, d, z))
print(n, 'couples de médianes de même valeur rationnelle ;', nz, 'donnent une différence flottante non nulle ; exemples', ex[:3])
