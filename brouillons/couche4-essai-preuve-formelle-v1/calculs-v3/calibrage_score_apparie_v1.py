"""calibrage_score_apparie_v1.py — VL-01 (vérification courte du brouillon 2) : erreurs EXACTES par queue et par affirmation,
et valeurs critiques calibrées par affirmation, pour la statistique de score appariée (« score de Tango »), sur une grille de la
nuisance écrite d'avance. Aucun tirage, aucun appel, aucun réseau. Nouveau nom (R12).

Affirmations lues par classe (deux classes, cible 0,0125 par queue et par classe, famille de deux classes ≤ 0,025) :
  « B>0 »  : la borne basse de Delta dépasse 0      ; erreur sous Delta = 0       ; queue haute de S(0)
  « H<d »  : la borne haute de Delta est sous delta  ; erreur sous Delta = delta   ; queue basse de S(delta)
  « B>=d » : la borne basse de Delta atteint delta   ; erreur sous Delta = delta   ; queue haute de S(delta)
Grille de la nuisance : n de 40 à 150 (tous les entiers) ; sous Delta = 0, discordance de 0,01 à 0,80 par pas de 0,01 ; sous
Delta = delta, discordance de delta (bord p01 = 0) à 0,80 par pas de 0,01.

<<SOURCE_TANGO>> : la forme close ci-dessous (q, puis S) est celle que donne de mémoire la vérification courte
(`prereg/contre-lectures/essai-preuve-formelle-devis-v1-brouillon2-verification-courte-v1.md`, annexe, `score_tango`, « forme de
PropCIs::scoreci.mp ») et que le rédacteur se rappelle aussi de Tango (1998, Statistics in Medicine) ; AUCUNE source n'a pu être
lue ici (aucun réseau, aucune copie dans le dépôt). Contrôle fait à la place (bloc 0) : la racine q de la forme close est comparée
au maximum de vraisemblance sous la contrainte p10 - p01 = d0, calculé numériquement ; la variance du dénominateur est la variance
nulle de n10 - n01 à ce maximum. Si la source dément la forme close, le REPLI est la statistique définie par ces principes (score
sous contrainte calculé numériquement), qui ne dépend d'aucune attribution ; les valeurs critiques se recalibrent par ce même script.
"""
import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy import optimize, stats
from scipy.special import gammaln

sys.dont_write_bytecode = True
DELTA = 0.20
CIBLE = 0.0125
Z = stats.norm.ppf(1 - CIBLE)          # 2,2414 : niveau nominal de chaque queue
NS = range(40, 151)
DISC0 = np.round(np.arange(0.01, 0.801, 0.01), 2)
DISCD = np.round(np.arange(DELTA, 0.801, 0.01), 2)
PAS_Z = 0.0005
ZS = np.round(np.arange(Z, 3.0, PAS_Z), 4)


def q_forme_close(n10, n01, n, d0):
    b, c = np.asarray(n01, float), np.asarray(n10, float)
    A = 2.0 * n
    B = -b - c + (2.0 * n - c + b) * d0
    C = -b * d0 * (1.0 - d0)
    return (np.sqrt(B * B - 4 * A * C) - B) / (2 * A)


def score(n10, n01, n, d0):
    q = q_forme_close(n10, n01, n, d0)
    den = np.sqrt(np.maximum(n * (2 * q + d0 * (1 - d0)), 1e-300))
    return (np.asarray(n10, float) - np.asarray(n01, float) - n * d0) / den


def q_numerique(n10, n01, n, d0):
    n00 = n - n10 - n01
    bas, haut = max(0.0, -d0), (1 - d0) / 2      # p10 = q + d0 >= 0 ; p00 = 1 - 2q - d0 >= 0

    def moins_l(q):
        v = 0.0
        if n10: v += n10 * math.log(q + d0)
        if n01: v += n01 * math.log(q)
        if n00: v += n00 * math.log(1 - 2 * q - d0)
        return -v
    r = optimize.minimize_scalar(moins_l, bounds=(bas + 1e-12, haut - 1e-12), method="bounded", options={"xatol": 1e-12})
    cand = [r.x, bas + 1e-12, haut - 1e-12]       # maximum intérieur ou au bord
    return min(cand, key=moins_l)


print(f"z nominal par queue (97,5 % bilatéral) : {Z:.4f} ; cible {CIBLE} par queue et par classe")

# ---------------------------------------------------------------- bloc 0 : contrôle de la forme close
rng = np.random.default_rng(np.random.SeedSequence(20261110_5).spawn(1)[0])
ecart_max = 0.0
for _ in range(3000):
    n = int(rng.integers(40, 151))
    n10 = int(rng.integers(0, n + 1)); n01 = int(rng.integers(0, n - n10 + 1))
    d0 = float(rng.choice([0.0, DELTA, rng.uniform(-0.5, 0.5)]))
    if n10 + n01 == 0 and d0 == 0:
        continue
    qc = float(q_forme_close(n10, n01, n, d0)); qn = q_numerique(n10, n01, n, d0)
    ecart_max = max(ecart_max, abs(qc - qn))
mc = max(abs(float(score(c, b, n, 0.0)) - (c - b) / math.sqrt(c + b))
         for n in (40, 150) for c in range(0, 30) for b in range(0, 30) if c + b > 0)
print(f"\n== (0) forme close contre maximum numérique sous contrainte : écart maximal de q sur 3 000 cas tirés = {ecart_max:.2e}")
print(f"   réduction à McNemar pour d0 = 0 : écart maximal {mc:.2e}")


# ---------------------------------------------------------------- énumération exacte
def cellules(n):
    i, j = np.meshgrid(np.arange(n + 1), np.arange(n + 1), indexing="ij")
    ok = (i + j) <= n
    return i[ok], j[ok]


def lois(n, i, j, couples):
    k = n - i - j
    base = gammaln(n + 1) - gammaln(i + 1) - gammaln(j + 1) - gammaln(k + 1)
    out = []
    for p10, p01 in couples:
        p00 = 1 - p10 - p01
        with np.errstate(divide="ignore", invalid="ignore"):
            lp = base.copy()
            lp += np.where(i > 0, i * (np.log(p10) if p10 > 0 else -np.inf), 0.0)
            lp += np.where(j > 0, j * (np.log(p01) if p01 > 0 else -np.inf), 0.0)
            lp += np.where(k > 0, k * (np.log(p00) if p00 > 0 else -np.inf), 0.0)
        out.append(np.exp(lp))
    return np.array(out)


def queue_max(stat, probs, zs, sens):
    """max sur la nuisance de P(sens * stat >= z), pour chaque z de zs (rejet inclusif : prudent)."""
    v = sens * stat
    ordre = np.argsort(-v)
    vs = v[ordre]
    cum = np.cumsum(probs[:, ordre], axis=1)                       # P(v >= vs[k]) pour chaque nuisance
    k = np.searchsorted(-vs, -zs, side="right")                    # nombre de cellules avec v >= z
    tail = np.where(k[None, :] > 0, cum[:, np.maximum(k - 1, 0)], 0.0)
    return tail.max(axis=0), tail


def wald(n10, n01, n, z):
    a10, a01, m = n10 + .5, n01 + .5, n + 2.
    d = (a10 - a01) / m; v = ((a10 + a01) / m - d * d) / m; h = z * np.sqrt(np.maximum(v, 0))
    return d - h, d + h


AFF = ("B>0", "H<d", "B>=d")
ZSTAR = {a: {} for a in AFF}
NOMINAL_T = {a: (0.0, None) for a in AFF}
NOMINAL_W = {a: (0.0, None) for a in AFF}
for n in NS:
    i, j = cellules(n)
    P0 = lois(n, i, j, [(d / 2, d / 2) for d in DISC0])
    PD = lois(n, i, j, [((d + DELTA) / 2, max((d - DELTA) / 2, 0.0)) for d in DISCD])
    s0, sd = score(i, j, n, 0.0), score(i, j, n, DELTA)
    for a, (st, P, sens) in {"B>0": (s0, P0, +1), "H<d": (sd, PD, -1), "B>=d": (sd, PD, +1)}.items():
        mx, tail = queue_max(st, P, ZS, sens)
        ok = np.nonzero(mx <= CIBLE)[0]
        ZSTAR[a][n] = float(ZS[ok[0]]) if len(ok) else None
        e = float(mx[0])
        if e > NOMINAL_T[a][0]:
            disc = (DISC0 if a == "B>0" else DISCD)[int(np.argmax(tail[:, 0]))]
            NOMINAL_T[a] = (e, (n, float(disc)))
    lb, ub = wald(i, j, n, Z)
    for a, (mask, P, discs) in {"B>0": (lb > 0, P0, DISC0), "H<d": (ub < DELTA, PD, DISCD),
                                 "B>=d": (lb >= DELTA, PD, DISCD)}.items():
        e = P[:, mask].sum(axis=1)
        if e.max() > NOMINAL_W[a][0]:
            NOMINAL_W[a] = (float(e.max()), (n, float(discs[int(np.argmax(e))])))

print("\n== (1) erreurs exactes au z nominal, pire case de la grille (par classe ; famille de deux classes indépendantes)")
for nom, tab in (("gabarit de Wald ajusté (brouillon 2)", NOMINAL_W), ("score de Tango", NOMINAL_T)):
    for a in AFF:
        e, (n, d) = tab[a]
        print(f"   {nom:38s} {a:5s} : {e:.4f} ; famille {1 - (1 - e) ** 2:.4f} (n={n}, discordance {d:.2f}) "
              f"{'AU-DESSUS' if e > CIBLE else 'sous'} la cible")

print("\n== (2) valeurs critiques calibrées z*(n) du score de Tango (plus petit z >= z nominal, pas de 0,0005, qui tient la cible "
      "sur toute la grille de la nuisance)")
for a in AFF:
    vals = [v for v in ZSTAR[a].values() if v is not None]
    manque = [n for n, v in ZSTAR[a].items() if v is None]
    nmax = max(ZSTAR[a], key=lambda n: ZSTAR[a][n] or 0)
    print(f"   {a:5s} : min {min(vals):.4f} ; max {max(vals):.4f} (n={nmax}) ; effectif à largeur égale × {(max(vals) / Z) ** 2:.3f} ; "
          f"n sans valeur : {manque or 'aucun'}")
    for n0 in (40, 60, 75, 102, 129, 150):
        print(f"      n={n0:3d} : z* = {ZSTAR[a][n0]:.4f}")

# ---------------------------------------------------------------- (3) probabilités des issues avec les z* calibrés (exactes)
print("\n== (3) issues exactes avec le score de Tango et les z* calibrés (« gain » = B>0 calibré et estimation >= delta ; O1a = "
      "B>=d calibré ; O3 = H<d calibré)")
for n in (102, 150):
    i, j = cellules(n)
    s0, sd = score(i, j, n, 0.0), score(i, j, n, DELTA)
    est = (i - j) / n
    for disc in (0.30, 0.40):
        lig = []
        for dv in (0.0, 0.10, 0.15, 0.20, 0.30):
            pr = lois(n, i, j, [((disc + dv) / 2, (disc - dv) / 2)])[0]
            gain = pr[(s0 >= ZSTAR["B>0"][n]) & (est >= DELTA)].sum()
            o1a = pr[sd >= ZSTAR["B>=d"][n]].sum()
            o3 = pr[sd <= -ZSTAR["H<d"][n]].sum()
            lig.append(f"D={dv:.2f}: gain {gain:.3f} (O1a {o1a:.3f}) O3 {o3:.3f} O4 {1 - gain - o3:.3f}")
        print(f"   n={n} disc={disc:.2f} | " + " | ".join(lig))

sortie = Path(__file__).with_name("valeurs-critiques-calibrees-v1.json")
sortie.write_text(json.dumps({"methode": "score apparié (forme close dite de Tango, <<SOURCE_TANGO>>)",
                              "cible_par_queue": CIBLE, "z_nominal": round(float(Z), 6), "pas": PAS_Z,
                              "grille": {"n": [40, 150], "disc_sous_delta_0": [0.01, 0.80, 0.01],
                                         "disc_sous_delta": [DELTA, 0.80, 0.01]},
                              "z_etoile": {a: {str(n): v for n, v in ZSTAR[a].items()} for a in AFF}},
                             ensure_ascii=False, indent=1), encoding="utf-8")
print(f"\nvaleurs critiques écrites : {sortie.name}")
