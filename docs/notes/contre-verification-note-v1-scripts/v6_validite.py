"""V6 - validite de la regle toujours valide 'E_n >= 1/alpha' (melange normal, mu0 et sigma supposes connus)
quand les hypotheses du cadre ne tiennent qu'en partie. alpha = 0.05 ; rho calibre sur n0.
On mesure P0(exists n <= n0 : E_n >= 1/alpha) par Monte-Carlo."""
import numpy as np
from scipy import stats
from eproc import alarm_any, rho_opt

alpha = 0.05
ss = np.random.SeedSequence(27182818)
seeds = iter(ss.spawn(64))

def fpr(gen, n0, reps, one_sided=True, sigma_used=1.0):
    rho, _ = rho_opt(n0, sigma_used, alpha, one_sided)
    X = gen(np.random.default_rng(next(seeds)), reps, n0)
    hit, _ = alarm_any(X, sigma_used, rho, alpha, one_sided)
    return hit.mean()

# lois standardisees (moyenne 0, variance 1) exactes ou par grand Monte-Carlo
rng_big = np.random.default_rng(next(seeds))
K = 50
mx = rng_big.standard_normal((400000, K)).max(axis=1); mx_mu, mx_sd = mx.mean(), mx.std()
g_mu, g_sd = np.euler_gamma, np.pi / np.sqrt(6)
be_a, be_b = 0.5, 5.0
be_mu = be_a / (be_a + be_b); be_sd = np.sqrt(be_a * be_b / ((be_a + be_b)**2 * (be_a + be_b + 1)))

gens = {
    "gaussien (reference)": lambda g, R, n: g.standard_normal((R, n)),
    f"max de {K} N(0,1), standardise": lambda g, R, n: (g.standard_normal((R, n, K)).max(axis=2) - mx_mu) / mx_sd,
    "Gumbel standardise": lambda g, R, n: (g.gumbel(size=(R, n)) - g_mu) / g_sd,
    "Exp(1) - 1": lambda g, R, n: g.exponential(size=(R, n)) - 1.0,
    "Beta(0.5,5) standardise (borne)": lambda g, R, n: (g.beta(be_a, be_b, size=(R, n)) - be_mu) / be_sd,
    "Student t5 standardise": lambda g, R, n: g.standard_t(5, size=(R, n)) / np.sqrt(5 / 3),
}
print("Taux d'alarme sous P0 (unilateral), sigma = vrai ecart-type")
for name, gen in gens.items():
    R200 = 20000 if "max de" not in name else 6000
    R1000 = 6000 if "max de" not in name else 1500
    print(f"  {name:34s} n0=200: {fpr(gen, 200, R200):.4f}   n0=1000: {fpr(gen, 1000, R1000):.4f}")

print("\nsigma mal estime (gaussien, n0=200, unilateral) :")
for f in [0.8, 0.9, 1.0, 1.1]:
    print(f"  sigma_utilise = {f:.1f} x sigma : {fpr(lambda g, R, n: g.standard_normal((R, n)), 200, 20000, sigma_used=f):.4f}")

print("\nmu0 estime sur K episodes honnetes de 200 actions (erreur ~ N(0, 1/(200K))), n0=200, unilateral :")
for Kep in [5, 20, 100]:
    def gen(g, R, n, Kep=Kep):
        bias = g.normal(0, 1 / np.sqrt(200 * Kep), size=(R, 1))   # mu0_hat - mu0 ; on observe X - mu0_hat
        return g.standard_normal((R, n)) - bias
    print(f"  K = {Kep:3d} episodes : {fpr(gen, 200, 20000):.4f}")

print("\nEffet episode (P0 echangeable, non iid) : X = u + eps, u ~ N(0, tau^2) par episode, var totale 1 :")
for tau in [0.05, 0.1, 0.2]:
    def gen(g, R, n, tau=tau):
        return g.normal(0, tau, size=(R, 1)) + np.sqrt(1 - tau**2) * g.standard_normal((R, n))
    print(f"  tau = {tau:.2f} : n0=200 {fpr(gen, 200, 20000):.4f} (bilat. {fpr(gen, 200, 20000, one_sided=False):.4f})   n0=1000 {fpr(gen, 1000, 6000):.4f}")

print("\nCorrelation entre agents au meme pas (N=5, lecture pas apres pas, T=40 -> n0=200), equicorrelation c :")
for c in [0.0, 0.1, 0.2, 0.4]:
    def gen(g, R, n, c=c, N=5):
        T = n // N
        common = g.standard_normal((R, T, 1)); own = g.standard_normal((R, T, N))
        return (np.sqrt(c) * common + np.sqrt(1 - c) * own).reshape(R, T * N)
    print(f"  c = {c:.1f} : {fpr(gen, 200, 20000):.4f}")
print("\nGraine : SeedSequence(27182818) ; erreur MC ~ 0.001 (20000 rep.) a 0.003 (1500-6000 rep.)")
