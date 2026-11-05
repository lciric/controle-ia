"""Statistiques (vectorisees sur les lignes) et calibrage Monte-Carlo sous P0."""
import numpy as np
from eproc import logE

def eproc_max_logE(X, sigma, rho, one_sided):
    S = np.cumsum(X, axis=1)
    n = np.arange(1, X.shape[1] + 1)[None, :]
    return logE(S, n, sigma, rho, one_sided).max(axis=1)   # alarme ssi >= log(1/alpha)

def terminal_sum(X):
    return X.sum(axis=1)

def max_stat(X):
    return X.max(axis=1)

def scan(X, w):
    C = np.concatenate([np.zeros((X.shape[0], 1)), np.cumsum(X, axis=1)], axis=1)
    return (C[:, w:] - C[:, :-w]).max(axis=1)

def page_cusum(X, k=0.5):
    W = np.zeros(X.shape[0]); M = np.zeros(X.shape[0])
    for j in range(X.shape[1]):
        W = np.maximum(0.0, W + X[:, j] - k)
        M = np.maximum(M, W)
    return M

def lag1(X):
    Z = X - X.mean(axis=1, keepdims=True)
    return (Z[:, :-1] * Z[:, 1:]).sum(axis=1) / (Z**2).sum(axis=1)

def runs_neg(X):
    """moins le nombre de suites au-dessus/au-dessous de la mediane (grand = peu de suites = grappes)."""
    med = np.median(X, axis=1, keepdims=True)
    s = X > med
    return -(1 + (s[:, 1:] != s[:, :-1]).sum(axis=1))

def calib(stat_values_null, alpha):
    """seuil t tel que P0(stat >= t) <= alpha (conservateur pour les stats discretes)."""
    v = np.sort(stat_values_null)
    k = int(np.ceil((1 - alpha) * len(v)))
    t = v[min(k, len(v) - 1)]
    # rendre conservateur : si trop d'ex aequo a t, passer au-dessus
    if (stat_values_null >= t).mean() > alpha:
        bigger = v[v > t]
        t = bigger[0] if bigger.size else np.inf
    return t
