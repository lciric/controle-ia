# Incertitude du taux de fausses alertes à 1 % selon la taille du jeu bénin (préenregistrement P-041 malléabilité v3).
# Seuil posé au k-e score bénin le plus haut (k = 0,01 n) : vrai taux ~ Beta(k, n - k + 1).
# Mesure : k observés sur n, intervalle de Clopper-Pearson à 95 % par quantiles de lois bêta. Tirages de Monte-Carlo, graine R9.
import numpy as np
rng = np.random.default_rng(np.random.SeedSequence(20261031))
M = 400000
def q(a, b, p):
    return float(np.quantile(rng.beta(a, b, M), p))
for n in (1000, 800, 500, 400, 300, 200):
    k = int(round(0.01 * n))
    print(f"seuil n={n} : fausses alertes attendues {k} ; vrai taux 95 % [{q(k, n - k + 1, 0.025):.4f} ; {q(k, n - k + 1, 0.975):.4f}]")
for n in (1000, 300, 200):
    k = int(round(0.01 * n))
    print(f"mesure n={n} : {k}/{n} observés ; Clopper-Pearson 95 % [{q(k, n - k + 1, 0.025):.4f} ; {q(k + 1, n - k, 0.975):.4f}]")
