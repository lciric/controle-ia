"""Recalcul indépendant du devis v3 de T0.6 (`docs/notes/g0-deux-semaines-v1/devis-T0.6-dose-reponse-v3.md`, 10965742…).

Contre-lecture de la chaîne de la course (consigne dcb21799…), point 5. N'écrit rien ; imprime chaque poste.
Usage : python -I recalcul_devis_v3_v1.py
Les grandeurs d'entrée sont celles que le devis v3 écrit (heures, prix, stockage, disque, téléchargement) ; le script
refait les produits et les sommes, puis le pire cas aux deux prix (1,30 et 4,70 USD/h) et sous un débit de la H200 NVL
moindre que celui de l'A100 (hypothèse non mesurée du devis).
"""
from __future__ import annotations

PLAFOND = 200.0

# Postes « divers » (heures)
divers = {"installation": 0.10, "clonage": 0.02, "suite_v2": 67 / 60 * 1.02, "bras_b_nominal": 20 / 60, "fin_poussees_arret": 0.25}
borne_bras_b_s = 2400 + 1500 + 3 * 600 + 75
print("suite liste v2 : 67 min x 1,02 =", round(67 * 1.02, 2), "min =", round(divers["suite_v2"], 3), "h")
print("borne de l'annexe du bras B :", borne_bras_b_s, "s =", round(borne_bras_b_s / 3600, 3), "h")
tot_divers = sum(divers.values())
print("total divers :", round(tot_divers, 3), "h (devis : 1,84)")

# Heures de marche
gen, ev, dist_min, dist_max = 3.57, 6.43, 0.46, 6.14
h_min = gen + ev + dist_min + tot_divers
h_max = gen + ev + dist_max + tot_divers
print(f"heures de marche : {h_min:.2f} à {h_max:.2f} h (devis : 12,3 à 17,9)")

# Attendu
def attendu(h_bas, p_bas, h_haut, p_haut, disque=72 * 0.0417, tel=(1, 2)):
    c_bas, c_haut = h_bas * p_bas, h_haut * p_haut
    return c_bas, c_haut, c_bas + disque + tel[0], c_haut + disque + tel[1]

print("disque arrêté 72 h x 0,0417 =", round(72 * 0.0417, 2))
for nom, pb, ph in (("A100", 1.1083, 1.30), ("H200 NVL", 3.3617, 4.0417)):
    cb, ch, ab, ah = attendu(12.3, pb, 17.9, ph)
    print(f"attendu {nom} : calcul {cb:.1f} à {ch:.1f} USD ; attendu {ab:.1f} à {ah:.1f} USD")
print("A100 à 2,07 USD/h :", round(12.3 * 2.07, 1), "à", round(17.9 * 2.07, 1), "USD de calcul")

# Pire cas
lent = 2 * 17.9
bb = 1.61
disque_arrete = 72 * 0.08
print(f"hôte deux fois plus lent : {lent:.1f} h ; disque arrêté 72 h x 0,08 = {disque_arrete:.2f}")

def pires(prix_a100, prix_h200, facteur_h200=1.0, note=""):
    p1 = (lent + bb) * prix_a100 + disque_arrete + 2
    p2 = p1 + 22.2 * prix_a100 + 2
    calc_p3 = (lent * facteur_h200 + bb * facteur_h200) * prix_h200
    p3 = calc_p3 + disque_arrete + 2
    p4 = 9.1 * prix_a100 + 2.3 + calc_p3 + disque_arrete + 2
    print(f"{note} A100 {prix_a100} / H200 {prix_h200} x débit/{facteur_h200:.2f} : P1'={p1:.1f} P2'={p2:.1f} P3'={p3:.1f} P4'={p4:.1f} ; marge P4' = {PLAFOND - p4:.1f} USD")
    return p4

pires(1.30, 4.0417, note="prix constatés")
pires(1.30, 4.70, note="borne")
# P4' sans arrondi du 11,8 du devis (9,1 x 1,30 = 11,83)
print("P4' détail à la borne :", round(9.1 * 1.30, 2), "+ 2,3 +", round((lent + bb) * 4.70, 2), "+", round(disque_arrete, 2), "+ 2")

# Débit de la H200 NVL moindre : facteur au-delà duquel P4' (borne) dépasse 200 USD
fixe = 9.1 * 1.30 + 2.3 + disque_arrete + 2
f_lim = (PLAFOND - fixe) / ((lent + bb) * 4.70)
print(f"P4' à la borne dépasse 200 USD dès que la H200 NVL est {100 * (1 - 1 / f_lim):.1f} % plus lente que l'A100 (facteur de durée {f_lim:.4f})")
f_lim_p3 = (PLAFOND - disque_arrete - 2) / ((lent + bb) * 4.70)
print(f"P3' à la borne dépasse 200 USD dès un facteur de durée {f_lim_p3:.4f} (H200 {100 * (1 - 1 / f_lim_p3):.1f} % plus lente)")
for f in (1.05, 1.10, 1.25, 1.5):
    pires(1.30, 4.70, facteur_h200=f, note=f"H200 plus lente (durée x {f})")
# Cas où l'A100 est plus lente que la H200 n'est pas un pire cas ; débit H200 égal = hypothèse du devis.
# Coût du disque en marche, non compté au devis v3 ?
print("stockage en marche (17,9 h x 2 x 0,08) =", round(lent * 0.08, 2), "USD (borne du filtre ; inclus si le prix total compte le stockage)")
