"""Tableaux du rapport de la coupe du calibrage — v1. Lit la sortie JSON, n'écrit que sur la sortie standard.
Usage : python3 -I -B tableaux-coupe-calibrage-v1.py coupe-calibrage-v1-sortie.json > tableaux-coupe-calibrage-v1.md
"""
import json
import sys

d = json.load(open(sys.argv[1]))
P = {r["etiquette"]: r for r in d["points"]}
NOM = {"dans_temporelle": "dans, temporelle", "dans_graine": "dans, par graine", "entre": "entre tâches",
       "entre_contigu": "entre, contiguë"}


def f(x):
    return f"{x:.3f}".replace(".", ",")


def ic(w):
    return f"[{f(w[0])}–{f(w[1])}]"


def c12(r, s=40):
    x = r[f"seuil={s}"]
    return f"{f(x['bilateral'])} {ic(x['bilateral_wilson95'])} ({f(x['unilateral'])})"


print("## Tableau principal (seuil 40 ; bilatéral [Wilson 95 %] (unilatéral) ; G1)\n")
print("| a | dérive d | coupe | échec joint c12, seuil 40 | seuil 20, bilatéral | moyenne s1 − s2 (σ) | é.-t. s1 − s2 (σ) "
      "| G1 par mode | G1 deux modes | G1 deux modes et c12 propre |")
print("|---|---|---|---|---|---|---|---|---|---|")
for a in (0.1, 0.3, 0.5):
    for dv in (0.0, 0.05, 0.10, 0.20):
        for c in ("dans_temporelle", "dans_graine", "entre"):
            r = P[f"principal|a={a}|derive={dv}|{c}"]
            g = r["G1"]
            print(f"| {f(a)[:3]} | {f(dv)[:4]} | {NOM[c]} | {c12(r)} | {f(r['seuil=20']['bilateral'])} "
                  f"| {r['moyenne_s1_moins_s2_cellule_1_sigma']:+.3f} | {f(r['ecart_type_s1_moins_s2_cellule_1_sigma'])} "
                  f"| {f(g['par_mode'])} | {f(g['deux_modes'])} {ic(g['deux_modes_wilson95'])} "
                  f"| {f(g['deux_modes_et_controle_12_propre_bilateral_40'])} "
                  f"{ic(g['deux_modes_et_controle_12_propre_bilateral_40_wilson95'])} |")
print(f"\nRépétitions : {P['principal|a=0.3|derive=0.0|dans_temporelle']['repetitions']} par point.\n")

print("## Variantes (a = 0,3 ; seuil 40, bilatéral (unilatéral) ; G1 deux modes ; G1 deux modes et c12 propre)\n")
print("| variante | dérive | dans, temporelle | dans, par graine | entre tâches | G1 deux modes |")
print("|---|---|---|---|---|---|")
for v, ds in (("rho08", (0.0, 0.10)), ("h0", (0.0, 0.10)), ("grille025_bris", (0.0, 0.10)),
              ("trois_modes_24_controles", (0.0, 0.10)), ("derive_une_cellule", (0.10, 0.20))):
    for dv in ds:
        rs = [P[f"{v}|derive={dv}|{c}"] for c in ("dans_temporelle", "dans_graine", "entre")]
        cel = " | ".join(f"{c12(r)} ; G1∧c12 {f(r['G1']['deux_modes_et_controle_12_propre_bilateral_40'])}" for r in rs)
        print(f"| {v} | {dv} | {cel} | {f(rs[0]['G1']['deux_modes'])} |")
for dv in (0.10, 0.20):
    rs = [P[f"derive_ordre_taches|d={dv}|{c}"] for c in ("dans_temporelle", "entre", "entre_contigu")]
    print(f"| dérive en ordre des tâches | {dv} | {c12(rs[0])} | — | aléatoire {c12(rs[1])} ; contiguë {c12(rs[2])} | "
          f"{f(rs[0]['G1']['deux_modes'])} |")
print(f"\nRépétitions : {P['rho08|derive=0.0|entre']['repetitions']} par point.\n")

print("## Taille (dérive nulle, h = 0,3, ρ = 0 ; seuil 40, bilatéral (unilatéral) ; é.-t. de s1 − s2)\n")
print("| coupe | a | tâches de calibrage | exécutions par tâche | N | échec joint c12, seuil 40 | é.-t. s1 − s2 (σ) |")
print("|---|---|---|---|---|---|---|")
for K_cal in (20, 30, 40, 50, 75, 100, 112, 150):
    r = P[f"taille|dans|T=64|K_cal={K_cal}"]
    print(f"| dans, temporelle | 0,3 | 64 | {K_cal} | {64 * K_cal} | {c12(r)} | {f(r['ecart_type_s1_moins_s2_cellule_1_sigma'])} |")
for a in (0.1, 0.3, 0.5):
    lignes = [(f"taille|entre|a={a}|T=64|K_cal={k}", 64, k) for k in (150, 300, 600, 1200)]
    lignes += [(f"taille|entre|a={a}|N=9600|T={t}", t, 9600 // t) for t in (128, 192, 320, 640, 1920, 9600)]
    lignes += [(f"taille|entre|a={a}|K_cal=150|T={t}", t, 150) for t in (128, 256, 512, 1024)]
    for e, t, k in lignes:
        r = P[e]
        print(f"| entre tâches | {f(a)[:3]} | {t} | {k} | {t * k} | {c12(r)} | {f(r['ecart_type_s1_moins_s2_cellule_1_sigma'])} |")
print(f"\nRépétitions : {P['taille|dans|T=64|K_cal=150']['repetitions']} par point.")
