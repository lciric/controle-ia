"""v3 (pilote : 10 témoins + 10 saines renotées une seconde fois ; options des décisions ; banque d'usage ; durées). v2 : contrôle des graines par Gemini Argon, hors des familles des bras. Calculs du brouillon 1 du devis de l'essai « preuve formelle contre suite bon marché » (couche 4).

Aucun appel de modèle, aucun réseau. Graines par numpy.random.SeedSequence (R9).
(1) Puissance de la règle à trois zones sur la différence appariée de rappels (paires discordantes).
(2) Borne supérieure de Clopper-Pearson des fausses alertes.
(3) Devis attendu et pire cas par élément, à partir des paramètres écrits ci-dessous (tous SUPPOSÉS sauf les prix cités).
"""
import math
import numpy as np
from scipy import stats

GRAINE = 20261110
ss = np.random.SeedSequence(GRAINE)
rng_puiss, rng_fa = [np.random.default_rng(s) for s in ss.spawn(2)]

DELTA = 0.20       # gain utile de rappel (proposé, à geler par Lazar)
PHI_MAX = 0.30     # plafond des fausses alertes de la chaîne formelle (proposé)
Z = stats.norm.ppf(0.975)
REPS = 20000


def ic_apparie(n10, n01, n):
    """Intervalle de Wald ajusté (Agresti-Min : +0,5 dans chaque case) pour p10 - p01. Gabarit de dimensionnement
    seulement ; la méthode du préenregistrement sera vérifiée par simulation de couverture avant scellement."""
    a10, a01, m = n10 + 0.5, n01 + 0.5, n + 2.0
    d = (a10 - a01) / m
    v = ((a10 + a01) / m - d ** 2) / m
    h = Z * math.sqrt(max(v, 0.0))
    return (n10 - n01) / n, d - h, d + h


def issues(n, disc, delta_vrai):
    p10, p01 = (disc + delta_vrai) / 2, (disc - delta_vrai) / 2
    tirages = rng_puiss.multinomial(n, [p10, p01, 1 - disc], size=REPS)
    c = {"I1": 0, "I2": 0, "I3": 0}
    for n10, n01, _ in tirages:
        est, lb, ub = ic_apparie(n10, n01, n)
        if lb > 0 and est >= DELTA:
            c["I1"] += 1
        elif ub < DELTA:
            c["I2"] += 1
        else:
            c["I3"] += 1
    return {k: v / REPS for k, v in c.items()}


def n_requis(disc, h):
    return math.ceil(Z ** 2 * disc / h ** 2)


def cp_haut(k, n, niveau=0.975):
    return 1.0 if k >= n else stats.beta.ppf(niveau, k + 1, n - k)


print("== (1) Effectif par classe pour une demi-largeur h = delta/2 =", DELTA / 2)
for disc in (0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50):
    print(f"  discordance {disc:.2f} : n = {n_requis(disc, DELTA / 2)}")

print("\n== (1b) Probabilités des issues (I1 gain établi, I2 gain sous le seuil, I3 non concluante), delta =", DELTA)
for n in (60, 100, 150):
    for disc in (0.20, 0.30, 0.40):
        for dv in (0.0, 0.10, 0.20, 0.30):
            if dv > disc:
                continue
            r = issues(n, disc, dv)
            print(f"  n={n:3d} disc={disc:.2f} delta_vrai={dv:.2f} : I1 {r['I1']:.3f}  I2 {r['I2']:.3f}  I3 {r['I3']:.3f}")

print("\n== (2) P(borne haute Clopper-Pearson 97,5 % <= PHI_MAX) selon n saines et phi vrai")
for n_s in (60, 120, 200, 300):
    lig = []
    for phi in (0.10, 0.15, 0.20, 0.25, 0.30):
        k = rng_fa.binomial(n_s, phi, size=4000)
        ok = np.mean([cp_haut(int(x), n_s) <= PHI_MAX for x in k])
        lig.append(f"phi={phi:.2f}:{ok:.3f}")
    print(f"  n saines={n_s:3d} : " + "  ".join(lig))

# ---------------------------------------------------------------- (3) devis
# Prix par million de jetons (entrée, sortie), USD.
PRIX = {
    # référence locale claude-api, table « Current Models (cached: 2026-11-03) » ; à vérifier sur la page publique
    "opus-5-5": (4.0, 20.0),
    # collisionneur_v8.py l. 77 : « Prix vérifiés le 30 octobre »
    "kimi-k3-1-pro": (2.0, 10.0),
    # collisionneur_v8.py l. 80-82 : « Prix SUPPOSÉS … barème volontairement haut » ; à vérifier
    "gpt-6-astra": (10.0, 50.0),
    # collisionneur_v8.py l. 73-74 : « Prix de Gemini inconnu ici : valeur volontairement haute » ; à vérifier
    "gemini-4-argon": (10.0, 50.0),
}
CACHE_LECTURE = 0.10   # fraction du prix d'entrée pour une lecture en cache (référence locale : « ~0.1x cost »)
CACHE_ECRITURE = 1.25  # fraction pour une écriture en cache (référence locale : « ~1.25x cost »)


def cout(modele, entree, sortie, part_cache=0.0, part_ecrite=0.0):
    pe, ps = PRIX[modele]
    frais = entree * (1 - part_cache - part_ecrite)
    return (frais * pe + entree * part_cache * pe * CACHE_LECTURE + entree * part_ecrite * pe * CACHE_ECRITURE
            + sortie * ps) / 1e6


# Profils par appel ou par item (SUPPOSÉS ; le pilote les mesure) : (entrée cumulée, sortie cumulée, part en cache, part écrite)
PROFILS = {
    # agent formel : ~20 tours, contexte moyen ~25 k, sortie (raisonnement compris) ~30 k
    "L_agent": ("opus-5-5", 500_000, 30_000, 0.85, 0.10),
    # relecteur de fidélité de l'énoncé formel (autre famille) : un appel
    "L_fidelite": ("kimi-k3-1-pro", 6_000, 3_000, 0.0, 0.0),
    # agent de la suite : ~6 tours, contexte moyen ~15 k, sortie ~10 k
    "S_agent": ("opus-5-5", 100_000, 10_000, 0.80, 0.10),
    # relecteur indépendant de la preuve (autre famille) : un appel
    "S_relecteur": ("kimi-k3-1-pro", 6_000, 4_000, 0.0, 0.0),
    # lecture nue (diagnostic du pilote) : un appel sans outil
    "N_lecture": ("opus-5-5", 5_000, 8_000, 0.0, 0.0),
    # planteur : graine + version saine renotée + variante fautive + clé, par graine
    "T_graine": ("gpt-6-astra", 5_000, 10_000, 0.0, 0.0),
    # contrôle de la graine saine (famille hors planteur et hors bras : v2)
    "G_controle": ("gemini-4-argon", 6_000, 4_000, 0.0, 0.0),
    # audit de mesure de fidélité (quatrième famille), sur les acceptations de la chaîne formelle
    "A_audit": ("gemini-4-argon", 4_000, 3_000, 0.0, 0.0),
}
PLAFOND_ITEM = 4.0      # plafond de dépense par item et par bras (même plafond pour L et S : coût apparié)
PIRE = {                # pire cas par appel ou par item, en USD
    "L": PLAFOND_ITEM, "S": PLAFOND_ITEM,
    "N_lecture": cout("opus-5-5", 5_000, 32_000),
    "T_graine": cout("gpt-6-astra", 8_000, 32_000),
    "G_controle": cout("gemini-4-argon", 8_000, 16_000),
    "A_audit": cout("gemini-4-argon", 6_000, 8_000),
}
att = {k: cout(*v) for k, v in PROFILS.items()}
att_L = att["L_agent"] + att["L_fidelite"]
att_S = att["S_agent"] + att["S_relecteur"]
print("\n== (3) Coûts unitaires attendus (USD) :", {k: round(v, 3) for k, v in att.items()})
print(f"   item bras L : {att_L:.3f} ; item bras S : {att_S:.3f} ; rapport L/S : {att_L / att_S:.2f}")
print("   pires cas unitaires :", {k: round(v, 3) for k, v in PIRE.items()})


def phase(graines, surgeneration, temoins, lecture_nue, part_audit):
    g = math.ceil(graines * (1 + surgeneration))
    items = 2 * graines + temoins
    a = {
        "planteur": g * att["T_graine"],
        "controle des graines": g * att["G_controle"],
        "bras L": items * att_L,
        "bras S": items * att_S,
        "lecture nue": items * att["N_lecture"] if lecture_nue else 0.0,
        "audit de fidelite": math.ceil(part_audit * items) * att["A_audit"],
    }
    p = {
        "planteur": g * PIRE["T_graine"],
        "controle des graines": g * PIRE["G_controle"],
        "bras L": items * PIRE["L"],
        "bras S": items * PIRE["S"],
        "lecture nue": items * PIRE["N_lecture"] if lecture_nue else 0.0,
        "audit de fidelite": math.ceil(part_audit * items) * PIRE["A_audit"],
    }
    return items, a, p


PHASES = (
    ("pilote (60 graines, 12 par classe, 10 témoins, 10 saines renotées bis)", (60, 0.2, 20, True, 0.5)),
    ("confirmation centrale (2 classes x 96)", (192, 0.2, 0, False, 0.3)),
    ("confirmation au plafond d'effectif (2 classes x 150)", (300, 0.2, 0, False, 0.3)),
    ("option D-5 (ii) : une classe fixée, 150", (150, 0.2, 0, False, 0.3)),
    ("option D-5 (iii) : cinq classes x 150 (Holm)", (750, 0.2, 0, False, 0.3)),
)
for nom, args in PHASES:
    items, a, p = phase(*args)
    print(f"\n-- {nom} : {items} items")
    for k in a:
        print(f"   {k:22s} attendu {a[k]:8.2f}   pire cas {p[k]:8.2f}")
    print(f"   {'TOTAL':22s} attendu {sum(a.values()):8.2f}   pire cas {sum(p.values()):8.2f}")

# Banque d'usage (option D-6) : L0 + 21 lemmes de la carte v1, 22 items, deux bras, audit de fidélité sur la moitié.
u_items = 22
u_att = u_items * (att_L + att_S) + math.ceil(0.5 * u_items) * att["A_audit"]
u_pire = u_items * 2 * PLAFOND_ITEM + math.ceil(0.5 * u_items) * PIRE["A_audit"]
print(f"\n-- option D-6 banque d'usage (22 items) : attendu {u_att:.2f}   pire cas {u_pire:.2f}")

# Durées (SUPPOSÉES) : minutes de processus par item et par bras ; parallélisme du bras formel limité par la mémoire.
MIN_L, MIN_S, MIN_N, PARALLELE_L, PARALLELE_S = 15, 3, 1, 3, 4
for nom, items in (("pilote", 140), ("confirmation centrale", 384), ("confirmation plafond", 600)):
    hl = items * MIN_L / 60
    hs = items * (MIN_S + (MIN_N if nom == "pilote" else 0)) / 60
    print(f"   durée {nom:22s} : bras L {hl:6.1f} h-processus ({hl / PARALLELE_L:5.1f} h murales à {PARALLELE_L}) ; "
          f"bras S et lecture nue {hs:5.1f} h-processus ({hs / PARALLELE_S:4.1f} h murales à {PARALLELE_S})")
