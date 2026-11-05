"""Q6 : chiffres du rapport v4 contre les sorties (de l'auteur, ou celles passées en arguments).
Usage : verif_rapport.py PRINCIPALE EFFET05 EFFET10 [sortie.json]"""
import json, sys
P, E5, E10 = (json.load(open(f)) for f in sys.argv[1:4])
def c(sortie, nom, d, n, b, k, s="160.0"):
    et = f"{nom}|delta={d}|n={n}|n_garde={n}|biais={b}|k={k}"
    x = sortie["cellules"][et][s]
    return {"garde_seule": x["garde_seule"]["part"], "k_gardes": x["k_gardes"]["part"], "k_contrastes": x["k_contrastes"]["part"],
            "fiche": x["fiche_entiere"]["part"], "frontiere": x.get("frontiere_part"), "tricheur": x.get("tricheur_part")}
res = {"tableau_s2": [], "quatre_cents": [], "lectures": {}, "artefacts_effet": []}
for K, t, d, k in [(10, 0.01, 0.05, 1), (10, 0.01, 0.05, 3), (10, 0.01, 0.1, 3), (10, 0.1, 0.05, 3), (3, 0.01, 0.05, 3), (3, 0.1, 0.1, 3)]:
    base = f"binomiale_Kh{K}_Ks{K}_taux{t}"
    l = {"K": K, "tau": t, "delta": d, "k": k, "s0": c(P, base, d, 160, 0.0, k)}
    l["s05"] = c(E5, base + "_effetA0.5", d, 160, 0.0, k); l["s10"] = c(E10, base + "_effetA1.0", d, 160, 0.0, k)
    res["tableau_s2"].append(l)
    f = lambda x: f"{x['k_gardes']:.3f}/{x['k_contrastes']:.3f}/{x['fiche']:.3f} (garde seule {x['garde_seule']:.3f})"
    print(K, t, d, k, "|", f(l["s0"]), "|", f(l["s05"]), "|", f(l["s10"]))
print("--- 400 unités, fiche")
for K in [10, 3]:
    for t in [0.01, 0.1]:
        for d in [0.05, 0.1]:
            for k in [1, 3]:
                base = f"binomiale_Kh{K}_Ks{K}_taux{t}"
                r = [c(P, base, d, 400, 0.0, k)["fiche"], c(E5, base + "_effetA0.5", d, 400, 0.0, k)["fiche"], c(E10, base + "_effetA1.0", d, 400, 0.0, k)["fiche"]]
                res["quatre_cents"].append({"K": K, "tau": t, "delta": d, "k": k, "fiche_s0_s05_s10": r})
                print(K, t, d, k, [round(x, 3) for x in r])
print("--- artefacts sous effet (frontière ≤ 1/seuil ?)")
mx = {}
for nomS, S in [("0.5", E5), ("1.0", E10)]:
    for et, cel in S["cellules"].items():
        for s in ["160.0", "20.0"]:
            b = cel[s]
            mx.setdefault((nomS, s), [0, 0, None])
            if b["frontiere_part"] > mx[(nomS, s)][0]: mx[(nomS, s)] = [b["frontiere_part"], b["tricheur_part"], et]
            mx[(nomS, s)][1] = max(mx[(nomS, s)][1], b["tricheur_part"]) if False else mx[(nomS, s)][1]
for kk, v in mx.items():
    print(kk, "frontière max", v[0], "à", v[2]); res["artefacts_effet"].append({"sigma": kk[0], "seuil": kk[1], "frontiere_max": v[0], "cellule": v[2]})
print("--- lectures § 3 (principale, seuil 160)")
L = res["lectures"]
L["64_fiche_max"] = max(c(P, f"binomiale_Kh{K}_Ks{K}_taux{t}", d, 64, b, k)["fiche"] for K in [10, 3] for t in [0.01, 0.1] for d in [0.05, 0.1] for b in [0.0, 0.0125, 0.025] for k in [1, 2, 3])
L["64_contrastes_k1"] = sorted({round(c(P, f"binomiale_Kh{K}_Ks{K}_taux{t}", d, 64, 0.0, 1)["k_contrastes"], 3) for K in [10, 3] for t in [0.01, 0.1] for d in [0.05, 0.1]})
L["64_gardes_k1_biais0"] = {f"K{K}_t{t}_d{d}": round(c(P, f"binomiale_Kh{K}_Ks{K}_taux{t}", d, 64, 0.0, 1)["k_gardes"], 3) for K in [10, 3] for t in [0.01, 0.1] for d in [0.05, 0.1]}
for K, t, d in [(10, 0.01, 0.05), (10, 0.1, 0.05), (3, 0.01, 0.05), (3, 0.1, 0.05), (3, 0.01, 0.1), (3, 0.1, 0.1)]:
    L[f"160_k3_K{K}_t{t}_d{d}"] = c(P, f"binomiale_Kh{K}_Ks{K}_taux{t}", d, 160, 0.0, 3)
L["biais_K10_t001_d005_k1"] = [c(P, "binomiale_Kh10_Ks10_taux0.01", 0.05, 160, b, 1)["garde_seule"] for b in [0.0, 0.0125, 0.025]]
L["tau_K10_d005_k1"] = [c(P, f"binomiale_Kh10_Ks10_taux{t}", 0.05, 160, 0.0, 1)["garde_seule"] for t in [0.01, 0.1]]
L["d010_biais0025_gardes_k1"] = {f"K{K}_t{t}": c(P, f"binomiale_Kh{K}_Ks{K}_taux{t}", 0.1, 160, 0.025, 1)["garde_seule"] for K in [10, 3] for t in [0.01, 0.1]}
L["d010_K3_t001_biais"] = [c(P, "binomiale_Kh3_Ks3_taux0.01", 0.1, 160, b, 1)["garde_seule"] for b in [0.0, 0.0125, 0.025]]
for kk, v in L.items(): print(kk, v)
if len(sys.argv) > 4:
    json.dump(res, open(sys.argv[4], "w"), indent=1, ensure_ascii=False)
