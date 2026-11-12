"""Mesure du coût de la notation de Mahalanobis du paquet gelé (`sondes/familles.SondeMahalanobis.scores_par_jeton`,
einsum à trois opérandes sans optimisation) contre la même quantité par produit matriciel ((z @ P) * z).sum(1), sur
données synthétiques (bruit gaussien, largeur 4 096). Aucune donnée réelle. Usage : python mesure_mahalanobis_v1.py <src> N"""
import sys, time
import numpy as np
sys.path.insert(0, sys.argv[1])
from controle_ia.sondes.familles import SondeMahalanobis
n = int(sys.argv[2]); d = 4096
rng = np.random.default_rng(np.random.SeedSequence(20261105))
A = rng.standard_normal((d, d)) / np.sqrt(d); P = A @ A.T + np.eye(d)
s = SondeMahalanobis("mesure", 0, rng.standard_normal(d), P)
acts = rng.standard_normal((n, d)).astype(np.float32)
t = time.perf_counter(); r1 = s.scores_par_jeton(acts); t1 = time.perf_counter() - t
t = time.perf_counter(); z = np.asarray(acts, dtype=np.float64) - s.mu; r2 = ((z @ s.P) * z).sum(axis=1); t2 = time.perf_counter() - t
print(f"jetons {n} ; einsum gelé {t1:.2f} s ({1000*t1/n:.2f} ms/jeton) ; produit matriciel {t2:.3f} s ({1000*t2/n:.4f} ms/jeton) ; "
      f"rapport {t1/t2:.0f} ; écart relatif max {np.max(np.abs(r1-r2)/np.abs(r1)):.2e}")
