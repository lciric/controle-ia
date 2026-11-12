"""Q3, Q6 : chaque chiffre du rapport v3 relu dans les sorties (de l'auteur, ou à graine neuve).
Usage : python3 -I -B verif_rapport.py PRINCIPALE.json EFFET.json INDEP.json > SORTIE.json
"""
import json
import sys

P, E, I = (json.load(open(x)) for x in sys.argv[1:4])
LOIS = [(10, 0.01), (10, 0.1), (3, 0.01), (3, 0.1)]


def nom(K, t, suff=""):
    return f"binomiale_Kh{K}_Ks{K}_taux{t}{suff}"


def cel(d, K, t, delta, n, b, k, s="160.0", suff=""):
    return d["cellules"][f"{nom(K, t, suff)}|delta={delta}|n={n}|n_garde={n}|biais={b}|k={k}"][s]


def part(d, K, t, delta, n, b, k, champ, s="160.0", suff=""):
    return cel(d, K, t, delta, n, b, k, s, suff)[champ]["part"]


out = {}
# tableau principal
tab = []
for K, t in LOIS:
    for d in (0.05, 0.1):
        tab.append({"loi": f"K={K}, tau={t}", "delta": d,
                    "k1": [part(P, K, t, d, 160, 0.0, 1, c) for c in ("garde_seule", "k_contrastes", "fiche_entiere")],
                    "k3": [part(P, K, t, d, 160, 0.0, 3, c) for c in ("k_gardes", "k_contrastes", "fiche_entiere")]})
out["tableau_160"] = tab

# 64 unités : fiche « partout » ≤ 0,01 (sur toutes les cellules, seuil 160)
c64 = {k: v for k, v in P["cellules"].items() if "|n=64|" in k}
out["n64_seuil160"] = {
    "fiche_max_toutes_cellules": max(v["160.0"]["fiche_entiere"]["part"] for v in c64.values()),
    "fiche_max_biais0": max(v["160.0"]["fiche_entiere"]["part"] for k, v in c64.items() if "biais=0.0|" in k),
    "contrastes_k1": [min(v["160.0"]["k_contrastes"]["part"] for k, v in c64.items() if k.endswith("k=1")),
                      max(v["160.0"]["k_contrastes"]["part"] for k, v in c64.items() if k.endswith("k=1"))],
    "contrastes_k3": [min(v["160.0"]["k_contrastes"]["part"] for k, v in c64.items() if k.endswith("k=3")),
                      max(v["160.0"]["k_contrastes"]["part"] for k, v in c64.items() if k.endswith("k=3"))],
    "gardes_k_gardes": [min(v["160.0"]["k_gardes"]["part"] for v in c64.values()),
                        max(v["160.0"]["k_gardes"]["part"] for v in c64.values())],
    "gardes_k_gardes_biais0": [min(v["160.0"]["k_gardes"]["part"] for k, v in c64.items() if "biais=0.0|" in k),
                               max(v["160.0"]["k_gardes"]["part"] for k, v in c64.items() if "biais=0.0|" in k)],
}
# 400 unités, biais 0 et tous biais
r400 = {}
for K, t in LOIS:
    for filtre in ("biais=0.0|", ""):
        vals = [v["160.0"]["fiche_entiere"]["part"] for k, v in P["cellules"].items()
                if k.startswith(nom(K, t) + "|") and "|n=400|" in k and filtre in k]
        r400[f"K={K},tau={t},{'biais0' if filtre else 'tous_biais'}"] = [min(vals), max(vals)]
out["n400_fiche_min_max"] = r400
# indépendants contre partagé
out["independants_k3_160_d0.05"] = {f"K={K},tau={t}": {
    "independants": part(I, K, t, 0.05, 160, 0.0, 3, "fiche_entiere", suff="_independants"),
    "partage": part(P, K, t, 0.05, 160, 0.0, 3, "fiche_entiere")} for K, t in LOIS}
out["independants_k3_160_d0.10"] = {f"K={K},tau={t}": {
    "independants": part(I, K, t, 0.1, 160, 0.0, 3, "fiche_entiere", suff="_independants"),
    "partage": part(P, K, t, 0.1, 160, 0.0, 3, "fiche_entiere")} for K, t in LOIS}
# effet d'unité
eff = {}
for K, t in LOIS:
    for d in (0.05, 0.1):
        eff[f"K={K},tau={t},delta={d}"] = {
            "garde_seule_k1": [part(P, K, t, d, 160, 0.0, 1, "garde_seule"), part(E, K, t, d, 160, 0.0, 1, "garde_seule", suff="_effetA0.05")],
            "fiche_k3": [part(P, K, t, d, 160, 0.0, 3, "fiche_entiere"), part(E, K, t, d, 160, 0.0, 3, "fiche_entiere", suff="_effetA0.05")]}
out["effet_unite_sans_avec"] = eff
# biais
bia = {}
for K, t in LOIS:
    for d in (0.05, 0.1):
        for n in (160, 400):
            bia[f"K={K},tau={t},delta={d},n={n}"] = [part(P, K, t, d, n, b, 1, "garde_seule") for b in (0.0, 0.0125, 0.025)]
out["biais_garde_seule"] = bia
# n80
n80 = {}
for K, t in LOIS:
    L = P["lois"][nom(K, t)]["n_pour_puissance_0_8_k_gardes"]
    for d in (0.05, 0.1):
        for b in (0.0, 0.0125, 0.025):
            n80[f"K={K},tau={t},delta={d},biais={b}"] = [L[f"delta={d}|seuil=160.0|biais={b}|k={k}"]["n_approx"] for k in (1, 2, 3)]
out["n80_seuil160_k1_k2_k3"] = n80
# seuil 20
out["seuil20_fiche_k3"] = {
    "d0.05_n160": [part(P, K, t, 0.05, 160, 0.0, 3, "fiche_entiere", "20.0") for K, t in LOIS],
    "d0.10_n64": [part(P, K, t, 0.1, 64, 0.0, 3, "fiche_entiere", "20.0") for K, t in LOIS]}
# artefacts
fr160 = max(v["160.0"].get("frontiere_part", 0) for v in P["cellules"].values())
fr20 = max(v["20.0"].get("frontiere_part", 0) for v in P["cellules"].values())
tri = max(max(v["160.0"].get("tricheur_part", 0), v["20.0"].get("tricheur_part", 0)) for v in P["cellules"].values())
out["artefacts"] = {"frontiere_max_160": fr160, "frontiere_max_20": fr20, "tricheur_max": tri,
                    "effet_frontiere_max_160": max(v["160.0"]["frontiere_part"] for v in E["cellules"].values()),
                    "effet_frontiere_max_20": max(v["20.0"]["frontiere_part"] for v in E["cellules"].values()),
                    "indep_frontiere_max_160": max(v["160.0"]["frontiere_part"] for v in I["cellules"].values()),
                    "indep_frontiere_max_20": max(v["20.0"]["frontiere_part"] for v in I["cellules"].values())}
out["cellules"] = {"principale": len(P["cellules"]), "effet": len(E["cellules"]), "independants": len(I["cellules"]),
                   "duree_principale_s": P["environnement"]["duree_s"]}
json.dump(out, sys.stdout, indent=1, ensure_ascii=False)
