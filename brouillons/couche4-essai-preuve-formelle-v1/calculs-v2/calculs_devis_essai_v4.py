"""calculs_devis_essai_v4.py — calculs du brouillon 2 du dessin et du devis de l'essai « preuve formelle contre suite
bon marché » (couche 4, pas (b) de R-2199), après la contre-lecture 1
(`prereg/contre-lectures/essai-preuve-formelle-devis-v1-brouillon1-cl1.md`, f565d51c…).

Aucun appel de modèle, aucun réseau. Graines par numpy.random.SeedSequence (R9). Nouveau nom (R12) : la v3
(`calculs-v1/calculs_devis_essai_v3.py`) reste telle quelle.

Changements par rapport à la v3 :
- C04 (CLP-03) : deux classes lues chacune à 97,5 % bilatéral (Bonferroni sur deux classes), sans porte ; règle d'effectif
  refaite avec z = 2,2414 ; erreur de famille simulée ; fréquences de O1a (borne basse >= delta) et de O1b.
- CLP-06 : lignes absentes chiffrées (planteur des témoins et des renotations bis, adjudication avec tirage de 20 items non
  litigieux (C13), audit étendu du § 1.8, banque refaite une fois (A6, découverte et confirmation), graines rejetées jusqu'à
  50 % (A5)) ; réserve de la coupure A7 (appels en vol en parallèle et prochain appel quel qu'il soit).
- CLP-09 : profil « pire réaliste » de l'agent formel (1 000 k d'entrée, 100 k de sortie) et effet sur A8.
- CLP-10 : machine chiffrée par durée allumée et prix horaire (paramètres à vérifier) ; écriture en cache marquée à vérifier ;
  variantes de modèle recalculées par fonction (plus de facteur global).
- CLP-15 : tous les coûts unitaires dérivés ici, en un seul lieu ; l'audit porte sur une part de tous les items.
"""
import math

import numpy as np
from scipy import stats

GRAINE = 20261110_4
ss = np.random.SeedSequence(GRAINE)
rng_issues, rng_famille, rng_fa = [np.random.default_rng(s) for s in ss.spawn(3)]

DELTA = 0.20          # gain utile de rappel (D-4 (i))
PHI_MAX = 0.30        # plafond des fausses alertes de la chaîne formelle (D-4 (i))
Z95 = stats.norm.ppf(0.975)
Z975 = stats.norm.ppf(1 - 0.025 / 2)   # 97,5 % bilatéral : Bonferroni sur deux classes
H = DELTA / 2
REPS = 40000
N_MAX, N_MIN = 150, 40


def intervalle(n10, n01, n, z):
    """Gabarit de dimensionnement : Wald ajusté (+0,5 par case) pour p10 - p01 (méthode du préenregistrement fixée à part, C09)."""
    a10, a01, m = n10 + 0.5, n01 + 0.5, n + 2.0
    d = (a10 - a01) / m
    v = ((a10 + a01) / m - d * d) / m
    h = z * np.sqrt(np.maximum(v, 0.0))
    return (n10 - n01) / n, d - h, d + h


def issues(rng, n, disc, dv, z):
    t = rng.multinomial(n, [(disc + dv) / 2, (disc - dv) / 2, 1 - disc], size=REPS)
    est, lb, ub = intervalle(t[:, 0], t[:, 1], n, z)
    gain = (lb > 0) & (est >= DELTA)
    o1a = lb >= DELTA
    sous = ub < DELTA
    return gain, o1a, sous


def n_regle(d_plus, z=Z975):
    return min(N_MAX, max(N_MIN, math.ceil(z ** 2 * d_plus / H ** 2)))


print(f"z à 95 % : {Z95:.4f} ; z à 97,5 % (Bonferroni, deux classes) : {Z975:.4f} ; rapport des carrés : {(Z975 / Z95) ** 2:.3f}")

print("\n== (1) Effectif par classe pour une demi-largeur h = 0,10, à 97,5 % (et à 95 % pour mémoire)")
for disc in (0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50):
    print(f"  discordance {disc:.2f} : n = {math.ceil(Z975 ** 2 * disc / H ** 2)} (à 95 % : {math.ceil(Z95 ** 2 * disc / H ** 2)})")

print("\n== (1b) Règle d'effectif de la fiche de passage : d+ = borne haute unilatérale 80 % (Clopper-Pearson) sur les 60 fautives")
SCENARIOS = {}
for x in (6, 9, 12, 15, 18, 21, 24):
    dp = stats.beta.ppf(0.80, x + 1, 60 - x)
    nk = n_regle(dp)
    SCENARIOS[x] = nk
    print(f"  {x:2d}/60 discordantes (d = {x / 60:.2f}) : d+ = {dp:.3f} -> n_k = {nk} ; deux classes : {2 * nk} graines, "
          f"{2 * nk} saines, {4 * nk} items")

print("\n== (2) Issues par classe à 97,5 % (« gain » = borne basse > 0 et estimation >= delta ; O1a = borne basse >= delta ;"
      " « sous » = O3 ; reste = O4)")
for n in (74, 102, 129, 150):
    for disc in (0.20, 0.30, 0.40):
        lig = []
        for dv in (0.0, 0.10, 0.15, 0.20, 0.30):
            if dv > disc:
                continue
            g, a, s = issues(rng_issues, n, disc, dv, Z975)
            lig.append(f"D={dv:.2f}: gain {g.mean():.3f} (O1a {a.mean():.3f}) sous {s.mean():.3f} O4 {1 - g.mean() - s.mean():.3f}")
        print(f"  n={n:3d} disc={disc:.2f} | " + " | ".join(lig))

print("\n== (2b) Erreur de famille, deux classes indépendantes, même Delta vrai dans les deux, sans porte")
for n in (102, 129, 150):
    for disc in (0.30, 0.40):
        for dv in (0.10, 0.15, 0.19):
            g1, _, _ = issues(rng_famille, n, disc, dv, Z975)
            g2, _, _ = issues(rng_famille, n, disc, dv, Z975)
            g95, _, _ = issues(rng_famille, n, disc, dv, Z95)
            print(f"  n={n:3d} disc={disc:.2f} Delta vrai={dv:.2f} (< delta) : faux « gain » au moins une classe à 97,5 % "
                  f"{np.mean(g1 | g2):.3f} ; une classe à 97,5 % {g1.mean():.3f} ; une classe à 95 % {g95.mean():.3f}")
        _, _, s1 = issues(rng_famille, n, disc, DELTA, Z975)
        _, _, s2 = issues(rng_famille, n, disc, DELTA, Z975)
        print(f"  n={n:3d} disc={disc:.2f} Delta vrai=0.20 (= delta) : faux « sous le seuil » au moins une classe {np.mean(s1 | s2):.3f}")


print("\n== (2c) Erreur de famille des affirmations établies (lecture C01) : deux classes, même Delta vrai, sans porte, 97,5 %")
for n in (75, 102, 129, 150):
    for disc in (0.20, 0.30, 0.40):
        t1 = rng_famille.multinomial(n, [disc / 2, disc / 2, 1 - disc], size=REPS)
        t2 = rng_famille.multinomial(n, [disc / 2, disc / 2, 1 - disc], size=REPS)
        _, lb1, _ = intervalle(t1[:, 0], t1[:, 1], n, Z975)
        _, lb2, _ = intervalle(t2[:, 0], t2[:, 1], n, Z975)
        _, a1, s1 = issues(rng_famille, n, disc, DELTA, Z975)
        _, a2, s2 = issues(rng_famille, n, disc, DELTA, Z975)
        print(f"  n={n:3d} disc={disc:.2f} : Delta vrai 0 -> au moins une « borne basse > 0 » {np.mean((lb1 > 0) | (lb2 > 0)):.4f} ; "
              f"Delta vrai = delta -> au moins un O1a {np.mean(a1 | a2):.4f}, au moins un « sous le seuil » {np.mean(s1 | s2):.4f}")

def cp_haut(k, n, niveau=0.975):
    return 1.0 if k >= n else stats.beta.ppf(niveau, k + 1, n - k)


def cp_bas(k, n, niveau=0.975):
    return 0.0 if k <= 0 else stats.beta.ppf(1 - niveau, k, n - k + 1)


print("\n== (3) P(borne haute Clopper-Pearson 97,5 % de phi_L <= PHI_MAX), saines de la confirmation")
for n_s in (80, 148, 200, 258, 300):
    lig = []
    for phi in (0.10, 0.15, 0.20, 0.25):
        k = rng_fa.binomial(n_s, phi, size=4000)
        lig.append(f"phi={phi:.2f}:{np.mean([cp_haut(int(v), n_s) <= PHI_MAX for v in k]):.3f}")
    print(f"  {n_s:3d} saines : " + "  ".join(lig))
print("   (C11) pilote, 60 saines : P(borne basse 95 % de phi_L > PHI_MAX)")
for phi in (0.30, 0.40, 0.50, 0.60):
    k = rng_fa.binomial(60, phi, size=4000)
    print(f"   phi vrai {phi:.2f} : {np.mean([cp_bas(int(v), 60) > PHI_MAX for v in k]):.3f}")

# ------------------------------------------------------------------------------------------------- (4) devis
# Prix par million de jetons (entrée, sortie), USD.
PRIX = {
    "opus-5-5": (4.0, 20.0),        # claude-api shared/models.md l. 83 ; à vérifier (page publique)
    "sonnet-5-5": (2.0, 10.0),      # shared/models.md l. 89 ; à vérifier
    "fable-5-2": (8.0, 40.0),       # shared/models.md l. 78 ; à vérifier
    "kimi-k3-1-pro": (2.0, 10.0),   # collisionneur_v8.py l. 76-77 : « Prix vérifiés le 30 octobre »
    "gpt-6-astra": (10.0, 50.0),    # collisionneur_v8.py l. 79-82 : SUPPOSÉS hauts ; à vérifier
    "gemini-4-argon": (10.0, 50.0), # collisionneur_v8.py l. 73-74 : « valeur volontairement haute » ; à vérifier
}
CACHE_LECTURE = 0.10    # prudent : shared/models.md l. 83 donne 0,20 par million pour Opus 5.5 (0,05 fois l'entrée)
CACHE_ECRITURE = 1.25   # À VÉRIFIER : absent de la ligne d'Opus 5.5 (CLP-10 a)


def cout(modele, entree, sortie, part_lue=0.0, part_ecrite=0.0):
    pe, ps = PRIX[modele]
    frais = entree * (1 - part_lue - part_ecrite)
    return (frais * pe + entree * part_lue * pe * CACHE_LECTURE + entree * part_ecrite * pe * CACHE_ECRITURE
            + sortie * ps) / 1e6


PLAFOND_ITEM = 4.0
PROFILS_L = {"supposé": (500_000, 30_000), "pire réaliste": (1_000_000, 100_000)}   # CLP-09


def unitaires(profil_L, modele_bras="opus-5-5"):
    eL, sL = PROFILS_L[profil_L]
    u = {
        "L_agent": cout(modele_bras, eL, sL, 0.85, 0.10),
        "L_fidelite": cout("kimi-k3-1-pro", 6_000, 3_000),
        "S_agent": cout(modele_bras, 100_000, 10_000, 0.80, 0.10),
        "S_relecteur": cout("kimi-k3-1-pro", 6_000, 4_000),
        "N": cout(modele_bras, 5_000, 8_000),
        "T": cout("gpt-6-astra", 5_000, 10_000),       # planteur, par graine ou par item de contrôle
        "G": cout("gemini-4-argon", 6_000, 4_000),     # contrôle de la graine saine
        "A": cout("gemini-4-argon", 4_000, 3_000),     # audit de fidélité, par item tiré
        "ADJ": cout("gemini-4-argon", 6_000, 4_000),   # adjudication à l'aveugle, par item soumis
    }
    u["L"] = min(PLAFOND_ITEM, u["L_agent"] + u["L_fidelite"])
    u["S"] = min(PLAFOND_ITEM, u["S_agent"] + u["S_relecteur"])
    return u


PIRE = {"L": PLAFOND_ITEM, "S": PLAFOND_ITEM, "N": cout("opus-5-5", 5_000, 32_000),
        "T": cout("gpt-6-astra", 8_000, 32_000), "G": cout("gemini-4-argon", 8_000, 16_000),
        "A": cout("gemini-4-argon", 6_000, 8_000), "ADJ": cout("gemini-4-argon", 8_000, 16_000)}
PARALLELE_L, PARALLELE_S = 3, 4
RESERVE_A7 = PARALLELE_L * PIRE["L"] + PARALLELE_S * PIRE["S"] + max(PIRE.values())   # C07 : en vol + prochain appel

for prof in PROFILS_L:
    u = unitaires(prof)
    print(f"\n== (4) Coûts unitaires, profil de l'agent L « {prof} » : " + ", ".join(f"{k} {v:.3f}" for k, v in u.items()))
    print(f"   rapport des coûts par item L/S : {u['L'] / u['S']:.2f}")
print("   pires cas unitaires :", ", ".join(f"{k} {v:.3f}" for k, v in PIRE.items()))
print(f"   réserve de la coupure A7 (3 items L et 4 items S en vol au plafond par item, plus le plus cher des appels suivants) : "
      f"{RESERVE_A7:.2f}")

ADJ_NON_LITIGIEUX = 20   # C13


def pilote(prof, part_litige):
    u = unitaires(prof)
    graines, analysables, controle = 60, 120, 20
    g = math.ceil(graines * 1.2)
    items = analysables + controle
    base = {
        "planteur des graines": g * u["T"],
        "planteur des témoins et renotations bis": controle * u["T"],
        "contrôle des graines": g * u["G"],
        "bras L": items * u["L"], "bras S": items * u["S"], "lecture nue": items * u["N"],
        "audit (50 %)": math.ceil(0.5 * items) * u["A"],
        "adjudication": (part_litige * analysables + ADJ_NON_LITIGIEUX) * u["ADJ"],
    }
    cond = {
        "audit étendu (§ 1.8)": (items - math.ceil(0.5 * items)) * u["A"],
        "banque refaite une fois (A6)": g * (u["T"] + u["G"]),
        "graines rejetées jusqu'à 50 % (A5)": (math.ceil(graines / 0.5) - g) * (u["T"] + u["G"]),
    }
    pire = {
        "planteur des graines": math.ceil(graines / 0.5) * 2 * PIRE["T"],   # rejet 50 % et banque refaite
        "planteur des témoins et renotations bis": controle * PIRE["T"],
        "contrôle des graines": math.ceil(graines / 0.5) * 2 * PIRE["G"],
        "bras L": items * PIRE["L"], "bras S": items * PIRE["S"], "lecture nue": items * PIRE["N"],
        "audit (tous les items)": items * PIRE["A"],
        "adjudication": (analysables + ADJ_NON_LITIGIEUX) * PIRE["ADJ"],
    }
    return base, cond, pire


def graines_payables(prof, plafond, part_litige=0.3):
    """A8 : graines du pilote payables sous le plafond une fois la banque construite et les 20 items de contrôle passés,
    réserve A7 et adjudication comprises."""
    u = unitaires(prof)
    g = 72
    fixe = g * (u["T"] + u["G"]) + 20 * u["T"] + 20 * (u["L"] + u["S"] + u["N"]) + 10 * u["A"] \
        + ADJ_NON_LITIGIEUX * u["ADJ"] + RESERVE_A7
    par_graine = 2 * (u["L"] + u["S"] + u["N"]) + 2 * 0.5 * u["A"] + 2 * part_litige * u["ADJ"]
    return int((plafond - fixe) // par_graine)


for prof in PROFILS_L:
    for part in (0.3, 0.6):
        base, cond, pire = pilote(prof, part)
        print(f"\n-- PILOTE (D-1b), profil L « {prof} », part d'items litigieux {part:.0%} : 140 items")
        for k, v in base.items():
            print(f"   {k:42s} attendu {v:8.2f}")
        tb, tc = sum(base.values()), sum(cond.values())
        for k, v in cond.items():
            print(f"   {k:42s} conditionnel {v:8.2f}")
        print(f"   {'TOTAL attendu ordinaire':42s} {tb:8.2f} ; avec toutes les lignes conditionnelles {tb + tc:8.2f}")
        print(f"   {'PIRE CAS sans plafond':42s} {sum(pire.values()):8.2f}")

print("\n-- A8 : graines du pilote payables sous le plafond (après banque, 20 items de contrôle, réserve A7 ; adjudication 30 %)")
for plafond in (450, 500, 550, 600):
    print(f"   plafond {plafond} : " + " ; ".join(f"profil « {p} » {graines_payables(p, plafond)}" for p in PROFILS_L)
          + " (minimum de A8 : 40 ; complet : 60)")


def confirmation(prof, nk, part_litige):
    u = unitaires(prof)
    graines = 2 * nk
    items = 2 * graines
    g = math.ceil(graines * 1.2)
    base = {
        "planteur": g * u["T"], "contrôle des graines": g * u["G"],
        "bras L": items * u["L"], "bras S": items * u["S"],
        "audit (30 %)": math.ceil(0.3 * items) * u["A"],
        "adjudication": (part_litige * items + ADJ_NON_LITIGIEUX) * u["ADJ"],
    }
    cond = {
        "audit étendu (§ 1.8)": (items - math.ceil(0.3 * items)) * u["A"],
        "banque refaite une fois (A6)": g * (u["T"] + u["G"]),
        "graines rejetées jusqu'à 50 % (A5)": (math.ceil(graines / 0.5) - g) * (u["T"] + u["G"]),
    }
    pire = {
        "planteur": math.ceil(graines / 0.5) * 2 * PIRE["T"], "contrôle des graines": math.ceil(graines / 0.5) * 2 * PIRE["G"],
        "bras L": items * PIRE["L"], "bras S": items * PIRE["S"], "audit (tous)": items * PIRE["A"],
        "adjudication": (items + ADJ_NON_LITIGIEUX) * PIRE["ADJ"],
    }
    return items, base, cond, pire


print("\n-- CONFIRMATION (phase 2) selon la discordance du pilote, adjudication 30 % (60 % entre crochets)")
for x, nk in SCENARIOS.items():
    for prof in PROFILS_L:
        items, b, c, p = confirmation(prof, nk, 0.3)
        _, b6, _, _ = confirmation(prof, nk, 0.6)
        print(f"   {x:2d}/60 -> n_k={nk:3d}, {items:3d} items, profil « {prof:13s} » : attendu ordinaire {sum(b.values()):8.2f} "
              f"[{sum(b6.values()):8.2f}] ; avec conditionnelles {sum(b.values()) + sum(c.values()):8.2f} ; "
              f"pire cas {sum(p.values()):9.2f}")
items, b, c, p = confirmation("supposé", N_MAX, 0.3)
print("   détail au plafond d'effectif (2 x 150), profil « supposé » :")
for k, v in b.items():
    print(f"     {k:40s} attendu {v:8.2f}")
for k, v in c.items():
    print(f"     {k:40s} conditionnel {v:8.2f}")
for k, v in p.items():
    print(f"     {k:40s} pire cas {v:8.2f}")

print("\n-- Variantes du modèle des bras (recalculées par fonction, mêmes profils de jetons ; lecture en cache à 0,1 fois pour tous :"
      " approximation, CLP-10 c)")
for modele in ("opus-5-5", "sonnet-5-5", "fable-5-2"):
    u = unitaires("supposé", modele)
    pil = 140 * (u["L"] + u["S"] + u["N"])
    conf = 600 * (u["L"] + u["S"])
    base_p, _, _ = pilote("supposé", 0.3)
    _, base_c, _, _ = confirmation("supposé", N_MAX, 0.3)
    hors_bras_p = sum(base_p.values()) - base_p["bras L"] - base_p["bras S"] - base_p["lecture nue"]
    hors_bras_c = sum(base_c.values()) - base_c["bras L"] - base_c["bras S"]
    print(f"   {modele:11s} : item L {u['L']:.3f}, item S {u['S']:.3f} ; parts des bras au pilote {pil:7.2f} ; "
          f"au plafond d'effectif {conf:7.2f} ; total ordinaire du pilote {pil + hors_bras_p:7.2f} ; "
          f"de la phase 2 au plafond d'effectif {conf + hors_bras_c:7.2f}")

print("\n-- Machine dédiée (D-1a, D-2) : durée allumée x prix horaire (prix À VÉRIFIER, aucune source de prix de machine à processeur ;"
      " durées SUPPOSÉES : D-1a 48 h ; pilote et phase 2 = heures murales des bras + 12 h de construction de banque et de marge)")
MIN_L, MIN_S, MIN_N = 15, 3, 1
DUREES = {
    "D-1a outillage (installation, gardes R5, simulations)": 48,
    "D-1b pilote (140 items)": math.ceil(140 * MIN_L / 60 / PARALLELE_L + 140 * (MIN_S + MIN_N) / 60 / PARALLELE_S) + 12,
}
for x, nk in ((12, SCENARIOS[12]), (24, SCENARIOS[24])):
    it = 4 * nk
    DUREES[f"phase 2, {x}/60 discordantes ({it} items)"] = math.ceil(it * MIN_L / 60 / PARALLELE_L + it * MIN_S / 60 / PARALLELE_S) + 12
for nom, h in DUREES.items():
    print(f"   {nom:55s} : {h:4d} h allumées ; à 0,10 / 0,20 / 0,40 USD l'heure : {h * 0.10:6.2f} / {h * 0.20:6.2f} / {h * 0.40:6.2f} ; "
          f"borne haute à 1,30 : {h * 1.30:7.2f}")
print("   (1,30 USD l'heure : plafond des machines à carte graphique du devis de la phase 0, brouillons/P3-chaine-v1-brouillon4/"
      "lancer_p3_v1.sh l. 44 ; borne haute prudente, non un prix de machine à processeur)")
