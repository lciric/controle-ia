"""Contre-lecture du lanceur T0.6 v3, C-V3-4 : (1) vitesse de `familles_v2` contre le paquet gelé ; (2) l'essai d'égalité
sur 256 jetons synthétiques prédit-il l'écart sur des jetons « réalistes » (activations en demi-précision, dimensions aberrantes
de grande amplitude, moyenne décalée, covariance apprise par `familles.mahalanobis` avec rétrécissement) ? Données synthétiques.
Usage : python -I egalite_mahalanobis_v1.py <src> N_APPRENTISSAGE N_NOTES"""
import sys, time
import numpy as np
sys.path.insert(0, sys.argv[1])
from controle_ia.sondes import familles as f1, familles_v2 as f2
n_app, n_not, d = int(sys.argv[2]), int(sys.argv[3]), 4096
rng = np.random.default_rng(np.random.SeedSequence(20261105, spawn_key=(9,)))
def jetons(n, decalage=0.0):
    x = rng.standard_normal((n, d)) * rng.gamma(2.0, 0.5, size=d)        # échelles hétérogènes par dimension
    x[:, :8] *= 300.0                                                     # dimensions aberrantes (activations massives)
    x += decalage
    return x.astype(np.float16).astype(np.float32)                         # passage par la demi-précision, comme le lanceur
seqs = [jetons(n_app // 20) for _ in range(20)]
s1 = f1.mahalanobis("m", 15, seqs, 0.1)
s2 = f2.en_produit_matriciel(s1)
ev = np.linalg.eigvalsh((s1.P + s1.P.T) / 2); print(f"conditionnement de P : {ev.max() / ev.min():.3e}")
synth = f2.verifier_egalite_au_paquet_gele(s2, 7)
print("essai d'égalité synthétique (256 jetons) : écart", f"{synth['ecart_relatif_max']:.2e}", "égal", synth["egal"])
for nom, dec in (("réalistes centrés", 0.0), ("réalistes décalés de 3", 3.0)):
    a = jetons(n_not, dec)
    t = time.perf_counter(); r1 = s1.scores_par_jeton(a); t1 = time.perf_counter() - t
    t = time.perf_counter(); r2 = s2.scores_par_jeton(a); t2 = time.perf_counter() - t
    e = np.max(np.abs(r2 - r1) / np.abs(r1))
    print(f"{nom} ({n_not} jetons) : gelé {t1:.2f} s, v2 {t2:.3f} s, rapport {t1 / t2:.0f} ; écart relatif max {e:.2e} ; "
          f"maximum par blocs de 222 égal : {np.array_equal(r1.reshape(-1, 222).max(1) if n_not % 222 == 0 else r1, r2.reshape(-1, 222).max(1) if n_not % 222 == 0 else r2)}")
