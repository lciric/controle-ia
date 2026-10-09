"""Utilitaires : processus e de melange normal (formes closes verifiees en V1)."""
import numpy as np
from scipy.special import log_ndtr
from scipy.optimize import brentq, minimize_scalar

def logE(S, n, sigma, rho, one_sided):
    a = 1 + rho**2 * sigma**2 * n
    out = -0.5 * np.log(a) + rho**2 * S**2 / (2 * a)
    if one_sided:
        out = out + np.log(2) + log_ndtr(rho * S / np.sqrt(a))
    return out

def alarm_any(X, sigma, rho, alpha, one_sided, mu0=0.0, upto=None):
    """X : (reps, n). Renvoie (alarme d'ici n, premier indice d'alarme ou n si aucune)."""
    S = np.cumsum(X - mu0, axis=1)
    n = np.arange(1, X.shape[1] + 1)
    L = logE(S, n[None, :], sigma, rho, one_sided)
    hit = L >= np.log(1 / alpha)
    first = np.where(hit.any(axis=1), hit.argmax(axis=1), X.shape[1])
    return hit.any(axis=1), first

def rho_opt(n0, sigma, alpha, one_sided):
    """rho minimisant la frontiere d'alarme a n0 (calibrage du melange sur l'horizon)."""
    def bound(r):
        return brentq(lambda s: logE(s, n0, sigma, r, one_sided) - np.log(1 / alpha), 0, 1e6)
    res = minimize_scalar(lambda lr: bound(np.exp(lr)), bounds=(np.log(1e-3), np.log(10)), method="bounded")
    return float(np.exp(res.x)), float(res.fun)
