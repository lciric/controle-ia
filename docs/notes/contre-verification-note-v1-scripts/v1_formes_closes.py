"""V1 - formes closes du processus e de melange normal (bilateral et unilateral).
Integration numerique (en log, grille dense autour du pic) de
  int exp(lam*S - lam^2 sigma^2 n / 2) dW(lam),  W = N(0, rho^2)  (bilateral)
                                                W = 2 N(0, rho^2) restreinte a lam >= 0 (unilateral)."""
import numpy as np
from scipy import stats
from scipy.special import logsumexp, log_ndtr
from scipy.optimize import brentq

def logE_bi_note(S, n, sigma, rho):
    a = 1 + rho**2 * sigma**2 * n
    return -0.5 * np.log(a) + rho**2 * S**2 / (2 * a)

def logE_uni_closed(S, n, sigma, rho):
    a = 1 + rho**2 * sigma**2 * n
    return np.log(2) - 0.5 * np.log(a) + rho**2 * S**2 / (2 * a) + log_ndtr(rho * S / np.sqrt(a))

def logE_num(S, n, sigma, rho, one_sided):
    A = sigma**2 * n + 1 / rho**2          # precision du "posterior" en lambda
    lam_star, w = S / A, 1 / np.sqrt(A)
    lo, hi = lam_star - 60 * w, lam_star + 60 * w
    if one_sided:
        lo = max(lo, 0.0)
        hi = max(hi, 60 * w)
    lam = np.linspace(lo, hi, 400001)
    logf = lam * S - lam**2 * sigma**2 * n / 2 + stats.norm.logpdf(lam, 0, rho)
    dl = lam[1] - lam[0]
    # trapeze en log
    wts = np.full(lam.size, np.log(dl)); wts[0] = wts[-1] = np.log(dl / 2)
    v = logsumexp(logf + wts)
    return v + (np.log(2) if one_sided else 0.0)

wb = wu = wnu = 0.0
for S in [-30, -10, -3, -1, 0, 0.5, 2, 5, 12, 25]:
    for n in [1, 10, 100, 1000]:
        for sigma in [0.5, 1.0, 2.0]:
            for rho in [0.05, 0.3, 1.0]:
                nb = logE_num(S, n, sigma, rho, False)
                nu = logE_num(S, n, sigma, rho, True)
                wb = max(wb, abs(logE_bi_note(S, n, sigma, rho) - nb))
                wu = max(wu, abs(logE_uni_closed(S, n, sigma, rho) - nu))
                wnu = max(wnu, abs(logE_bi_note(S, n, sigma, rho) - nu))
print(f"bilateral  : |log E_note - log E_num|           max = {wb:.2e}")
print(f"unilateral : |log E_uni_closed - log E_num|     max = {wu:.2e}")
print(f"formule de la note utilisee comme unilaterale : max |ecart log| = {wnu:.2f}")

n, sigma, rho = 100, 1.0, 0.1
S = np.linspace(-40, 40, 9)
print("S       :", S)
print("E_bi    :", np.round(np.exp(logE_bi_note(S, n, sigma, rho)), 3))
print("E_uni   :", np.round(np.exp(logE_uni_closed(S, n, sigma, rho)), 3))

alpha = 0.05
def bound_bi(n, sigma, rho, alpha):
    a = 1 + rho**2 * sigma**2 * n
    return np.sqrt(a / rho**2 * (2 * np.log(1 / alpha) + np.log(a)))
def bound_uni(n, sigma, rho, alpha):
    return brentq(lambda s: logE_uni_closed(s, n, sigma, rho) - np.log(1 / alpha), 0, 1e5)
for n in [10, 100, 1000]:
    print(f"rho={rho} n={n:5d}  frontiere |S|>= {bound_bi(n,1,rho,alpha):7.2f} (bilat.)  S>= {bound_uni(n,1,rho,alpha):7.2f} (unilat.)  "
          f"z unilat. horizon fixe: {stats.norm.isf(alpha)*np.sqrt(n):6.2f}")
