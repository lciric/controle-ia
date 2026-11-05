"""Extrait le tableau du § 2 du rapport v5 (k = 8) d'une sortie principale, et quelques lectures.
Usage : python3 -I -B tableau_k8.py SORTIE_PRINCIPALE.json [SORTIE_NULLES.json] [SORTIE_TAUX.json]"""
import json
import sys

d = json.load(open(sys.argv[1]))
C = d["cellules"]


def cel(K, t, delta, n, b, k=8):
    return C[f"binomiale_Kh{K}_Ks{K}_taux{t}|delta={delta}|n={n}|n_garde={n}|biais={b}|k={k}"]


print("K δ biais | n : A retenue (A atteinte 40) · B 8 du mode 1 retenues (B 8 atteignent 320) · A toutes · B toutes")
for K in (10, 3):
    for delta in (0.05, 0.075):
        for b in (0.0, 0.0125):
            ligne = []
            for n in (160, 300, 400, 650):
                c = cel(K, 0.01, delta, n, b)
                A, B = c["ebh_A"], c["ebh_B"]
                ligne.append(f"{n}: {A['retenue_une_fiche']:.3f} ({A['premiere_atteinte_une_fiche']:.3f}) · "
                             f"{B['retenues_fiches_du_sujet']:.3f} ({B['premiere_atteinte_fiches_du_sujet']:.3f}) · "
                             f"{A['retenues_toutes_vraies']:.3f} · {B['retenues_toutes_vraies']:.3f}")
            print(K, delta, b, " | ".join(ligne))
print("contraste limite K = 3, δ = 0,05, biais 0, k = 8 : min des 8 contrastes / min des 8 gardes au seuil 40")
for n in (160, 300, 400, 650):
    c = cel(3, 0.01, 0.05, n, 0.0)
    print(n, c["40.0"]["k_contrastes"]["part"], c["40.0"]["k_gardes"]["part"], "fiche 40", c["40.0"]["fiche_entiere"]["part"],
          "= A atteinte", c["ebh_A"]["premiere_atteinte_une_fiche"])
print("effet de k (fiche, première atteinte de 160, biais 0) : K = 10 n = 160 ; K = 3 n = 400")
for K, n in ((10, 160), (3, 400)):
    print(K, n, [round(cel(K, 0.01, 0.05, n, 0.0, k)["160.0"]["fiche_entiere"]["part"], 3) for k in (1, 3, 8)])
print("tailles minimales", d.get("taille_minimale_ecarts_nuls"), d["lecture_ebh"]["taille_minimale_ecarts_nuls"])
print("lecture 4 : ajout de la valeur finale (A retenue − A atteinte), max", max(
    (c["ebh_A"]["retenue_une_fiche"] - c["ebh_A"]["premiere_atteinte_une_fiche"], et) for et, c in C.items() if "k=8" in et))
print("lecture 3 : |A − B| (toutes vraies), max", max((abs(c["ebh_A"]["retenues_toutes_vraies"] - c["ebh_B"]["retenues_toutes_vraies"]), et)
                                                     for et, c in C.items() if "k=8" in et))
print("artefacts : frontière / borne max ; tricheur max", max(v["frontiere_part"] / v["frontiere_borne_ville"] for c in C.values() for s, v in c.items() if isinstance(v, dict) and "frontiere_part" in v),
      max(v["tricheur_part"] for c in C.values() for s, v in c.items() if isinstance(v, dict) and "tricheur_part" in v))
if len(sys.argv) > 2:
    N = json.load(open(sys.argv[2]))["cellules"]
    print("fiches nulles : A au moins une nulle retenue / B / pfd moy A / B ; vraies (A retenue, B 8 retenues)")
    for et, c in N.items():
        A, B = c["ebh_A"], c["ebh_B"]
        print(et.split("|", 1)[1], A["nulles_au_moins_une_retenue"], B["nulles_au_moins_une_retenue"],
              round(A["proportion_de_fausses_decouvertes_moyenne"], 5), round(B["proportion_de_fausses_decouvertes_moyenne"], 5),
              "|", A["retenue_une_fiche"], B["retenues_fiches_du_sujet"], A["m"], B["m"])
if len(sys.argv) > 3:
    T = json.load(open(sys.argv[3]))["cellules"]
    print("τ = 0,10 : A retenue · B 8 retenues")
    for et, c in T.items():
        print(et.split("|", 1)[1], round(c["ebh_A"]["retenue_une_fiche"], 3), round(c["ebh_B"]["retenues_fiches_du_sujet"], 3))
