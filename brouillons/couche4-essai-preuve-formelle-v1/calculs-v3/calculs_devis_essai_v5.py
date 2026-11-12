"""calculs_devis_essai_v5.py — devis du brouillon 3 (vérification courte du brouillon 2 appliquée : VL-02, VL-03, VL-04, VL-07 c).
Aucun appel, aucun réseau. Nouveau nom (R12) : la v4 (`calculs-v2/`) reste telle quelle ; les coûts unitaires sont recalculés ici
avec les mêmes prix et profils, et comparés à ceux de la v4 (contrôle d'identité).

- VL-04 : règle A8 écrite comme le script la calcule : graines payables = ⌊(plafond − réserve A7 − charges hors graines) / coût
  par graine⌋, charges hors graines = banque (72 graines plantées et contrôlées), planteur des 20 items de contrôle, ces 20 items
  vus par les deux bras et la lecture nue, leur audit (10), le tirage de 20 items non litigieux de l'adjudicateur ; coût par graine
  = deux items vus par les deux bras et la lecture nue, leur audit (50 %), leur adjudication (part litigieuse). Trois profils de
  l'agent formel : supposé, pire réaliste, tout item L au plafond de 4 USD. Plafond minimal pour 40 et 60 graines. Pistes : réserve
  ramenée à 12 (fin sans parallélisme), lecture nue abandonnée en dernier.
- VL-02 : minuteries de machine (destruction par identifiant) contre les plafonds de machine, au prix horaire de borne haute.
- VL-03 : somme des plafonds ; enveloppe au profil pire réaliste.
- VL-07 c : plafond indicatif de la phase 2 avec 60 % d'items litigieux.
- Sensibilité : prix de Gemini 4 Argon lu sur la page archivée `docs/sources/prix/page-prix-gemini-api-20261108T054611Z.html`
  (2 / 10 USD par million jusqu'au 30 novembre 2026, 4 / 20 à partir du 1er décembre) au lieu du 10 / 50 supposé.
"""
import math
import sys

sys.dont_write_bytecode = True
PRIX = {"opus-5-5": (4.0, 20.0), "kimi-k3-1-pro": (2.0, 10.0), "gpt-6-astra": (10.0, 50.0), "gemini-4-argon": (10.0, 50.0)}
CACHE_LECTURE, CACHE_ECRITURE = 0.10, 1.25
PLAFOND_ITEM = 4.0
PROFILS_L = {"supposé": (500_000, 30_000), "pire réaliste": (1_000_000, 100_000), "tout item L au plafond": None}
V4 = {"L supposé": 1.162, "L pire réaliste": 3.082, "S": 0.374, "N": 0.180, "T": 0.550, "G": 0.260, "A": 0.190, "ADJ": 0.260}


def cout(prix, modele, e, s, lu=0.0, ec=0.0):
    pe, ps = prix[modele]
    return (e * (1 - lu - ec) * pe + e * lu * pe * CACHE_LECTURE + e * ec * pe * CACHE_ECRITURE + s * ps) / 1e6


def unitaires(profil, prix=PRIX):
    u = {"S": cout(prix, "opus-5-5", 100_000, 10_000, .80, .10) + cout(prix, "kimi-k3-1-pro", 6_000, 4_000),
         "N": cout(prix, "opus-5-5", 5_000, 8_000), "T": cout(prix, "gpt-6-astra", 5_000, 10_000),
         "G": cout(prix, "gemini-4-argon", 6_000, 4_000), "A": cout(prix, "gemini-4-argon", 4_000, 3_000),
         "ADJ": cout(prix, "gemini-4-argon", 6_000, 4_000)}
    if PROFILS_L[profil] is None:
        u["L"] = PLAFOND_ITEM
    else:
        e, s = PROFILS_L[profil]
        u["L"] = min(PLAFOND_ITEM, cout(prix, "opus-5-5", e, s, .85, .10) + cout(prix, "kimi-k3-1-pro", 6_000, 3_000))
    return u


PIRE = {"L": 4.0, "S": 4.0, "N": cout(PRIX, "opus-5-5", 5_000, 32_000), "T": cout(PRIX, "gpt-6-astra", 8_000, 32_000),
        "G": cout(PRIX, "gemini-4-argon", 8_000, 16_000), "A": cout(PRIX, "gemini-4-argon", 6_000, 8_000),
        "ADJ": cout(PRIX, "gemini-4-argon", 8_000, 16_000)}
RESERVE_A7 = 3 * PIRE["L"] + 4 * PIRE["S"] + max(PIRE.values())   # 32
RESERVE_A7_SERIE = PIRE["L"] + PIRE["S"] + max(PIRE.values())    # 12 : fin sans parallélisme

print("== (0) contrôle d'identité des coûts unitaires avec la v4")
for prof in ("supposé", "pire réaliste"):
    u = unitaires(prof)
    print(f"   L {prof} : {u['L']:.3f} (v4 {V4['L ' + prof]}) ; S {u['S']:.3f} (v4 {V4['S']}) ; N {u['N']:.3f} ; T {u['T']:.3f} ; "
          f"G {u['G']:.3f} ; A {u['A']:.3f} ; ADJ {u['ADJ']:.3f}")
print(f"   réserve A7 : {RESERVE_A7:.2f} ; en fin sans parallélisme : {RESERVE_A7_SERIE:.2f}")


def charges_A8(prof, part=0.3, nue=True, prix=PRIX):
    u = unitaires(prof, prix)
    nN = u["N"] if nue else 0.0
    fixe = 72 * (u["T"] + u["G"]) + 20 * u["T"] + 20 * (u["L"] + u["S"] + nN) + 10 * u["A"] + 20 * u["ADJ"]
    par_graine = 2 * (u["L"] + u["S"] + nN) + 2 * 0.5 * u["A"] + 2 * part * u["ADJ"]
    return fixe, par_graine


def payables(prof, plafond, reserve=RESERVE_A7, nue=True, prix=PRIX):
    fixe, pg = charges_A8(prof, nue=nue, prix=prix)
    return int((plafond - reserve - fixe) // pg)


def plafond_min(prof, graines, reserve=RESERVE_A7, nue=True, prix=PRIX):
    fixe, pg = charges_A8(prof, nue=nue, prix=prix)
    return fixe + reserve + graines * pg


print("\n== (1) A8 : graines du pilote payables sous le plafond (charges hors graines et réserve A7 retranchées ; adjudication 30 %)")
for prof in PROFILS_L:
    fixe, pg = charges_A8(prof)
    print(f"   profil « {prof} » : charges hors graines {fixe:.2f} + réserve {RESERVE_A7:.0f} ; par graine {pg:.3f} ; "
          f"plafond minimal pour 40 graines {plafond_min(prof, 40):.2f}, pour 60 {plafond_min(prof, 60):.2f}")
    print("      " + " ; ".join(f"{p} : {payables(prof, p)}" for p in (450, 500, 550, 578, 600, 639, 650, 767)))
P_D1B = math.ceil(plafond_min("tout item L au plafond", 40))
print(f"\n   plafond de D-1b qui tient 40 graines même si chaque item L coûte 4 USD : {P_D1B}")
for prof in PROFILS_L:
    print(f"      à {P_D1B} : profil « {prof} » {payables(prof, P_D1B)} graines ; réserve 12 (fin sans parallélisme) "
          f"{payables(prof, P_D1B, RESERVE_A7_SERIE)} ; lecture nue abandonnée {payables(prof, P_D1B, nue=False)} ; les deux "
          f"{payables(prof, P_D1B, RESERVE_A7_SERIE, nue=False)}")
for prof in PROFILS_L:
    print(f"   blocs équilibrés (5 graines) à {P_D1B}, profil « {prof} » : {min(60, payables(prof, P_D1B)) // 5} blocs, "
          f"{5 * (min(60, payables(prof, P_D1B)) // 5)} graines équilibrées ({min(60, payables(prof, P_D1B)) // 5} par classe)")


def pilote(prof, part):
    u = unitaires(prof)
    g, items = 72, 140
    base = 72 * u["T"] + 20 * u["T"] + 72 * u["G"] + items * (u["L"] + u["S"] + u["N"]) + 70 * u["A"] + (part * 120 + 20) * u["ADJ"]
    cond = 70 * u["A"] + 72 * (u["T"] + u["G"]) + (120 - 72) * (u["T"] + u["G"])
    return base, base + cond


print("\n== (2) pilote (140 items) : attendu ordinaire et avec toutes les lignes conditionnelles (identique à la v4)")
for prof in PROFILS_L:
    print("   " + f"profil « {prof} » : " + " ; ".join(f"{int(p * 100)} % litigieux : {pilote(prof, p)[0]:.2f} / {pilote(prof, p)[1]:.2f}"
                                                   for p in (0.3, 0.6)))


def phase2(prof, nk, part):
    u = unitaires(prof)
    graines = 2 * nk; items = 2 * graines; g = math.ceil(graines * 1.2)
    base = g * (u["T"] + u["G"]) + items * (u["L"] + u["S"]) + math.ceil(0.3 * items) * u["A"] + (part * items + 20) * u["ADJ"]
    cond = (items - math.ceil(0.3 * items)) * u["A"] + g * (u["T"] + u["G"]) + (math.ceil(graines / 0.5) - g) * (u["T"] + u["G"])
    return base, base + cond


print("\n== (3) phase 2 au plafond d'effectif (2 x 150 graines, 600 items)")
for prof in PROFILS_L:
    print("   " + f"profil « {prof} » : " + " ; ".join(f"{int(p * 100)} % litigieux : ordinaire {phase2(prof, 150, p)[0]:.2f}, "
                                                   f"avec conditionnelles {phase2(prof, 150, p)[1]:.2f}" for p in (0.3, 0.6)))
P2 = math.ceil((phase2("supposé", 150, 0.6)[1] + RESERVE_A7) / 50) * 50
print(f"   plafond indicatif de la phase 2 (profil supposé, 60 % litigieux, lignes conditionnelles, réserve A7, arrondi à 50) : {P2}")

print("\n== (4) machine : minuterie de destruction par identifiant (R10) contre le plafond, au prix horaire de borne haute 1,30")
for nom, h, plaf in (("D-1a", 48, 65), ("D-1b", 26, 35), ("phase 2", 70, 91)):
    print(f"   {nom:7s} : minuterie {h} h ; coût à 1,30 USD l'heure {h * 1.30:6.2f} ≤ plafond {plaf} : {h * 1.30 <= plaf} ; "
          f"heures payables sous le plafond à 1,30 : {math.floor(plaf / 1.30)} ; à 0,40 : {math.floor(plaf / 0.40)}")

print("\n== (5) somme des plafonds et enveloppe au profil pire réaliste")
somme = 65 + P_D1B + 35 + P2 + 91
print(f"   somme des plafonds proposés ou indicatifs : 65 + {P_D1B} + 35 + {P2} + 91 = {somme}")
o30 = phase2("pire réaliste", 150, 0.3)[0] + RESERVE_A7
c60 = phase2("pire réaliste", 150, 0.6)[1] + RESERVE_A7
print(f"   phase 2 complète au profil pire réaliste : de {o30:.2f} (ordinaire, 30 % litigieux, réserve) à {c60:.2f} "
      f"(conditionnelles, 60 % litigieux, réserve)")
print(f"   enveloppe au profil pire réaliste (D-1a 65 + D-1b {P_D1B} + 35 + phase 2 + 91) : {65 + P_D1B + 35 + o30 + 91:.2f} à "
      f"{65 + P_D1B + 35 + c60 + 91:.2f}")
c30 = phase2("pire réaliste", 150, 0.3)[1] + RESERVE_A7
print(f"   pour mémoire, au calcul de la vérification courte (D-1b 550, 30 % litigieux) : {65 + 550 + 35 + o30 + 91:.2f} à "
      f"{65 + 550 + 35 + c30 + 91:.2f}")
print(f"   attendu au profil supposé (D-1b et phase 2, sans machine) : {pilote('supposé', 0.3)[0] + phase2('supposé', 150, 0.3)[0]:.2f} à "
      f"{pilote('supposé', 0.6)[1] + phase2('supposé', 150, 0.6)[1]:.2f}")

print("\n== (6) sensibilité : prix de Gemini 4 Argon lu sur la page archivée (au lieu de 10 / 50 supposés)")
for nom, pa in (("jusqu'au 30 novembre 2026 : 2 / 10", (2.0, 10.0)), ("à partir du 1er décembre 2026 : 4 / 20", (4.0, 20.0))):
    prix = dict(PRIX); prix["gemini-4-argon"] = pa
    u = unitaires("supposé", prix)
    pil = 72 * u["T"] + 20 * u["T"] + 72 * u["G"] + 140 * (u["L"] + u["S"] + u["N"]) + 70 * u["A"] + (0.3 * 120 + 20) * u["ADJ"]
    print(f"   Argon {nom} : G {u['G']:.3f}, A {u['A']:.3f}, ADJ {u['ADJ']:.3f} ; pilote ordinaire (supposé, 30 %) {pil:.2f} "
          f"(contre {pilote('supposé', 0.3)[0]:.2f}) ; plafond minimal pour 40 graines, tout item L au plafond : "
          f"{plafond_min('tout item L au plafond', 40, prix=prix):.2f}")
