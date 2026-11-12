"""Puissance conjointe de T6-1 de T0.6, v3 (script neuf ; fille 10, 7 novembre 2026). Nom neuf, R12 : la v2 n'est pas dans cet arbre et n'est ni lue ni modifiée.

Ce que le candidat 2 fixe (section « Puissance ») et que ce script prend tel quel, sans aucune lecture de sonde ni de `diag/` :
- statistique de tâche en log10 du coût, écart type entre épisodes 0,795 (pilote) ou 1 (prudent) ;
- 64 tâches (plan b) ou 36 (plan a) par condition ; effet minimal détectable à 80 % d'**une** comparaison : 0,394 (b) et 0,525 (a)
  à 0,795 ; 0,495 et 0,660 à 1 (déduits ici : (z_{0,975} + z_{0,80}) × sd × √(2/n), reproduits par le script) ;
- T6-1 exige **deux** comparaisons : saboteur contre la base, saboteur contre l'adaptateur témoin ; test bilatéral à 5 % pour chacune
  (approximation normale, comme la contre-lecture), les deux dans le sens du saboteur ;
- adaptateur témoin neutre (effet 0) ou qui baisse le coût comme le témoin instruit de P3 (−0,3176).
Modèle : trois bras indépendants de n tâches, chacun de moyenne μ_bras et d'écart type sd ; les deux différences partagent le bras
saboteur, d'où une corrélation de 0,5 entre leurs statistiques. Puissance conjointe = P(Z1 > c et Z2 > c) pour la loi normale
bivariée de moyennes (δ1/se, δ2/se), corrélation 0,5, c = z_{0,975} (la queue dans le mauvais sens, négligeable, est comptée avec le
test bilatéral pour la puissance d'une comparaison seule). Deux calculs : exact (loi normale bivariée, scipy) et simulation de 2 000
répliques (graine par `numpy.random.SeedSequence`, R9, une clé nommée par scénario). Sortie déterministe.

    .venv/bin/python -I -B puissance_t06_v3.py > puissance-t06-v3.txt   (numpy et scipy du `.venv`)
"""
from __future__ import annotations

import hashlib
import sys

import numpy as np
from scipy.stats import multivariate_normal, norm

ALPHA, PUISSANCE_VISEE, RHO, REPLIQUES = 0.05, 0.80, 0.5, 2000
EFFET_TEMOIN_P3 = -0.3176
SD = (0.795, 1.0)
PLANS = {"b": (64, "b, 64 tâches"), "a": (36, "a, 36 tâches")}
ENTROPIE = 20261107


def erreur_type(sd: float, n: int) -> float:
    if not (sd > 0 and n >= 2):
        raise ValueError(f"écart type > 0 et n ≥ 2 attendus, {sd}, {n}")
    return sd * np.sqrt(2.0 / n)


def effet_minimal(sd: float, n: int, alpha: float = ALPHA, puissance: float = PUISSANCE_VISEE) -> float:
    """Effet minimal détectable à `puissance` d'une comparaison (bilatérale, approximation normale)."""
    if not (0 < alpha < 1 and 0 < puissance < 1):
        raise ValueError("alpha et puissance dans ]0, 1[")
    return float((norm.ppf(1 - alpha / 2) + norm.ppf(puissance)) * erreur_type(sd, n))


def puissance_une(effet: float, sd: float, n: int, alpha: float = ALPHA) -> float:
    mu, c = effet / erreur_type(sd, n), norm.ppf(1 - alpha / 2)
    return float(norm.sf(c - mu) + norm.cdf(-c - mu))


def puissance_conjointe(effet_base: float, effet_temoin: float, sd: float, n: int, alpha: float = ALPHA, rho: float = RHO) -> float:
    """P(les deux comparaisons significatives dans le sens du saboteur) : effet_base = saboteur − base ; effet_temoin = saboteur − témoin."""
    if not -1 < rho < 1:
        raise ValueError("corrélation dans ]-1, 1[")
    se, c = erreur_type(sd, n), norm.ppf(1 - alpha / 2)
    m1, m2 = effet_base / se, effet_temoin / se
    return float(multivariate_normal(mean=[0.0, 0.0], cov=[[1, rho], [rho, 1]]).cdf([m1 - c, m2 - c]))


def simulee(effet_base: float, effet_temoin: float, sd: float, n: int, cle: str, alpha: float = ALPHA, repliques: int = REPLIQUES) -> float:
    """Même quantité par simulation des trois bras (moyennes de n tâches), graine dérivée de la clé (R9)."""
    graine = np.random.SeedSequence([ENTROPIE, int.from_bytes(hashlib.sha256(cle.encode()).digest()[:8], "big")])
    rng = np.random.default_rng(graine)
    se_bras, c = sd / np.sqrt(n), norm.ppf(1 - alpha / 2)
    base = rng.normal(0.0, se_bras, repliques)
    temoin = rng.normal(effet_temoin_vers_temoin(effet_base, effet_temoin), se_bras, repliques)
    sab = rng.normal(effet_base, se_bras, repliques)
    se = se_bras * np.sqrt(2.0)
    return float(np.mean(((sab - base) / se > c) & ((sab - temoin) / se > c)))


def effet_temoin_vers_temoin(effet_base: float, effet_temoin: float) -> float:
    """Moyenne du bras témoin telle que saboteur − témoin = effet_temoin (la base est en 0, le saboteur en effet_base)."""
    return effet_base - effet_temoin


def main() -> int:
    print("# Puissance conjointe de T6-1, v3 (normale bivariée exacte ; simulation de 2 000 répliques)")
    print(f"# alpha {ALPHA} bilatéral, corrélation {RHO}, puissance visée {PUISSANCE_VISEE}, entropie {ENTROPIE}; script {hashlib.sha256(open(__file__, 'rb').read()).hexdigest()}")
    for sd in SD:
        for plan, (n, nom) in PLANS.items():
            e1 = effet_minimal(sd, n)
            print(f"\n## sd {sd}, plan {nom} : erreur type d'une différence {erreur_type(sd, n):.4f} ; effet minimal détectable à 80 % (une comparaison) {e1:.3f} ; puissance d'une comparaison à cet effet {puissance_une(e1, sd, n):.3f}")
            for nom_t, moyenne_t in (("témoin neutre (0)", 0.0), (f"témoin qui baisse le coût comme le témoin instruit de P3 ({EFFET_TEMOIN_P3})", EFFET_TEMOIN_P3)):
                for effet in (e1, 1.25 * e1):                      # l'effet minimal, puis 1,25 fois cet effet
                    eff_t = effet - moyenne_t
                    pe = puissance_conjointe(effet, eff_t, sd, n)
                    ps = simulee(effet, eff_t, sd, n, f"{sd}/{plan}/{nom_t}/{effet:.4f}")
                    print(f"- effet saboteur − base {effet:.3f} ; {nom_t} ; effet saboteur − témoin {eff_t:.3f} : puissance conjointe exacte {pe:.3f}, simulée {ps:.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
