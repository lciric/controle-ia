"""Q6 — chaque chiffre du rapport v2 contre la sortie scellée ; Q3 — même graine et graine neuve.

Usage : python3 -I -B verif_rapport.py SORTIE_AUTEUR [SORTIE_REPRO] [SORTIE_GRAINE_NEUVE] > ../sorties/verif_rapport.json
"""
import json
import sys

aut = json.load(open(sys.argv[1]))
autres = [json.load(open(p)) for p in sys.argv[2:]]
C = aut["cellules"]


def cel(loi, d, n, b, k):
    return C[f"{loi}|delta={d}|n={n}|biais={b}|k={k}"]


def p(c, s, quoi):
    return c[s][quoi]["part"] if isinstance(c[s][quoi], dict) else c[s][quoi]


out = {}
L = "binomiale_K10_taux0.01"
# Tableau principal, seuil 160
tab = {}
for d, n in [(0.05, 64), (0.05, 160), (0.05, 400), (0.1, 64), (0.1, 160)]:
    c3, c1 = cel(L, d, n, 0.0, 3), cel(L, d, n, 0.0, 1)
    tab[f"d={d}|n={n}"] = {"garde_seule": p(c3, "160.0", "garde_seule"), "3_gardes": p(c3, "160.0", "k_gardes"),
                           "3_contrastes": p(c3, "160.0", "k_contrastes"), "fiche_k3": p(c3, "160.0", "fiche_entiere"),
                           "fiche_k1": p(c1, "160.0", "fiche_entiere"), "garde_seule_dans_k1": p(c1, "160.0", "garde_seule")}
out["tableau_principal_seuil160"] = tab
# Biais honnête
out["biais"] = {f"d={d}|n={n}|b={b}": {"garde_seule_k1": p(cel(L, d, n, b, 1), "160.0", "garde_seule"),
                                       "garde_seule_dans_k3": p(cel(L, d, n, b, 3), "160.0", "garde_seule")}
                for d in (0.05, 0.1) for n in (160, 400) for b in (0.0, 0.0125, 0.025)}
# Bruit plus fort
out["bruit"] = {f"{loi}|n={n}": {"garde_seule_k1": p(cel(loi, 0.05, n, 0.0, 1), "160.0", "garde_seule"),
                                 "garde_seule_dans_k3": p(cel(loi, 0.05, n, 0.0, 3), "160.0", "garde_seule")}
                for loi in ("binomiale_K10_taux0.1", "binomiale_K3_taux0.01", "binomiale_K3_taux0.1") for n in (160, 400)}
# Contraste
out["contraste_k3"] = {f"{loi}|n={n}": p(cel(loi, 0.05, n, 0.0, 3), "160.0", "k_contrastes")
                       for loi in ("binomiale_K10_taux0.01", "binomiale_K3_taux0.01") for n in (64, 160, 400)}
out["contraste_k1"] = {f"{loi}|n={n}": p(cel(loi, 0.05, n, 0.0, 1), "160.0", "k_contrastes")
                       for loi in ("binomiale_K10_taux0.01", "binomiale_K3_taux0.01") for n in (64, 160, 400)}
# Fiche à 64 unités, seuil 160 : toutes lois
out["fiche_64_seuil160_max"] = max(c["160.0"]["fiche_entiere"]["part"] for e, c in C.items() if "|n=64|" in e)
# Artefacts
fr160 = max(c["160.0"]["frontiere_part"] for c in C.values())
fr20 = max(c["20.0"]["frontiere_part"] for c in C.values())
tr = max(max(c["160.0"]["tricheur_part"], c["20.0"]["tricheur_part"]) for c in C.values())
out["artefacts"] = {"frontiere_max_160": fr160, "frontiere_max_20": fr20, "tricheur_max": tr}
# Seuil 20, garde seule, biais 0
g20 = {}
for d, n in [(0.05, 64), (0.05, 160), (0.1, 64)]:
    vals = {loi: cel(loi, d, n, 0.0, 1)["20.0"]["garde_seule"]["part"] for loi in aut["lois_garde"]}
    g20[f"d={d}|n={n}"] = vals
out["seuil20_garde_seule_k1"] = g20
# n80
n80 = {}
for loi, v in aut["lois_garde"].items():
    for cle, r in v["n_pour_puissance_0_8_k_gardes"].items():
        if "seuil=160.0" in cle:
            n80[f"{loi}|{cle}"] = r["n"]
out["n80_seuil160"] = n80


# Q3 : comparaison avec d'autres sorties
def plat(s):
    res = {}
    for e, c in s["cellules"].items():
        for seuil in ("160.0", "20.0"):
            for q in ("garde_seule", "k_gardes", "k_contrastes", "fiche_entiere"):
                res[f"{e}|{seuil}|{q}"] = c[seuil][q]["part"]
            res[f"{e}|{seuil}|frontiere"] = c[seuil]["frontiere_part"]
            res[f"{e}|{seuil}|tricheur"] = c[seuil]["tricheur_part"]
    for loi, v in s["lois_garde"].items():
        for cle, r in v.get("n_pour_puissance_0_8_k_gardes", {}).items():
            res[f"n80|{loi}|{cle}"] = r["n"]
    return res


A = plat(aut)
comp = []
for s in autres:
    B = plat(s)
    sans_env = lambda x: {k: v for k, v in x.items() if k not in ("environnement", "commit")}
    identique = json.dumps(sans_env(aut), sort_keys=True) == json.dumps(sans_env(s), sort_keys=True)
    diffs = {k: (A[k], B[k]) for k in A if A[k] != B[k]}
    parts = [abs(A[k] - B[k]) for k in A if not k.startswith("n80") and A[k] is not None]
    n80d = {k: (A[k], B[k]) for k in A if k.startswith("n80") and A[k] != B[k]}
    rel80 = [abs(A[k] - B[k]) / A[k] for k in A if k.startswith("n80") and A[k] and B[k]]
    comp.append({"graine": s["reglages"]["graine"], "identique_hors_environnement_et_commit": identique,
                 "commit": s.get("commit"), "script_sha256": s.get("script_sha256"),
                 "cellules_differentes": len([k for k in diffs if not k.startswith("n80")]),
                 "ecart_max_part": max(parts), "n80_differents": len(n80d), "n80_ecart_relatif_max": max(rel80) if rel80 else 0,
                 "n80_exemples": dict(list(n80d.items())[:12]),
                 "ecarts_principaux": {k: (A[k], B[k]) for k in A if not k.startswith("n80") and abs(A[k] - B[k]) >= 0.03}})
out["comparaisons"] = comp
json.dump(out, sys.stdout, indent=1, ensure_ascii=False)
print()
