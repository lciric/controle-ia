"""Contre-lecture GD8 (R2) — compare les rejeux GD8 aux sorties de la v8 et recalcule les chiffres clés (aucun tirage).

Pour chaque passage rejoué NOM : `rejeu-gd8-NOM.json` (dossier REJEU) contre `simulation-puissance-garde-delta-v8-sortie-NOM.json` (dossier V8) :
- toutes les cellules : retenue e-BH de la fiche du sujet (« seuil 40 »), atteinte de 160 et de 40 par la fiche, parts des k gardes et des k contrastes ;
- tous les n80 et n90 de la fiche (retenue e-BH, atteinte 160) et tous les points évalués par la dichotomie ;
- différences comptées (égalité exacte) et écart absolu maximal.
Puis, depuis les rejeux seulement : fiche « pire » (minimum des quatre cellules K_h ∈ {10 ; 5} × biais ∈ {0 ; 0,0125}) à 288 et 400 unités, aux deux seuils,
tronquée à trois décimales comme le rapport ; n80, n90 pires (maximum des quatre cellules) ; n_h = max(288 ; 16·⌈1,06·n80/16⌉) ; pour le neuvième comparateur,
surcoût par cellule (n80 à 9 − n80 à 8, même cellule) et son maximum (définition du rapport), écart des n80 pires, écart des n_h.
Usage : python3 -I -B comparer-rejeu-gd8-v1.py DOSSIER_REJEU DOSSIER_V8 SORTIE.json
"""
import hashlib
import json
import math
import os
import sys

REJEU, V8, SORTIE = sys.argv[1:4]
NOMS = ["meme-rho0.17", "meme-rho0.10", "neuf-k9-g0.05-nulle", "neuf-k9-g0.05-rho0.17"]
BASE_K8 = {"neuf-k9-g0.05-nulle": "rho0", "neuf-k9-g0.05-rho0.17": "meme-rho0.17"}
tr = lambda x: math.floor(x * 1000 + 1e-9) / 1000
nh = lambda a: max(288, 16 * math.ceil(1.06 * a / 16))


def charger(chemin):
    brut = open(chemin, "rb").read()
    return json.loads(brut), hashlib.sha256(brut).hexdigest()


def valeurs_cellule(c):
    v = {"ebh40": c["ebh_A"]["retenues_fiches_du_sujet"]}
    for s in ("40.0", "160.0"):
        for b in ("fiche_entiere", "k_gardes", "k_contrastes"):
            v[f"{s}|{b}"] = c[s][b]["part"]
    return v


def n80s(d):
    out = {}
    for nom, loi in d["lois"].items():
        for cle, r in loi.get("n_pour_puissance_0_8_fiche", {}).items():
            for cible in ("n80", "n90"):
                if cible in r:
                    for mesure, x in r[cible].items():
                        out[f"{nom}|{cle}|{cible}|{mesure}"] = x["n_approx"]
            for n, p in r["points_evalues"].items():
                for mesure, x in p.items():
                    out[f"{nom}|{cle}|point|{n}|{mesure}"] = x
    return out


def cle_cellule(et):
    # étiquette : LOI|delta=…|n=…|n_garde=…|biais=…|k=…
    loi, _, n, _, b, k = et.split("|")
    K_h = int(loi.split("_Kh")[1].split("_")[0])
    return K_h, float(b.split("=")[1]), int(n.split("=")[1]), int(k.split("=")[1])


def resume(d):
    cel = {}
    for et, c in d["cellules"].items():
        K_h, b, n, k = cle_cellule(et)
        cel[(K_h, b, n)] = c
    pire = {}
    for n in (288, 400, 500, 650):
        pire[str(n)] = {"seuil40": min(cel[(K, b, n)]["ebh_A"]["retenues_fiches_du_sujet"] for K in (10, 5) for b in (0.0, 0.0125)),
                        "seuil160": min(cel[(K, b, n)]["160.0"]["fiche_entiere"]["part"] for K in (10, 5) for b in (0.0, 0.0125))}
    par_cellule = {}
    for nom, loi in d["lois"].items():
        K_h = int(nom.split("_Kh")[1].split("_")[0])
        for cle, r in loi.get("n_pour_puissance_0_8_fiche", {}).items():
            b = float(cle.split("biais=")[1].split("|")[0])
            par_cellule[f"K_h={K_h}|biais={b}"] = {f"{cible}|{m}": r[cible][m]["n_approx"] for cible in ("n80", "n90") if cible in r for m in r[cible]}
    n80p = {}
    for cle in next(iter(par_cellule.values())):
        vals = [v[cle] for v in par_cellule.values()]
        n80p[cle] = None if any(x is None for x in vals) else max(vals)
    return pire, par_cellule, n80p


res = {"script": os.path.basename(__file__), "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(), "passages": {}}
resumes = {}
for nom in NOMS:
    r, hr = charger(os.path.join(REJEU, f"rejeu-gd8-{nom}.json"))
    o, ho = charger(os.path.join(V8, f"simulation-puissance-garde-delta-v8-sortie-{nom}.json"))
    diffs, n_champs, max_abs = [], 0, 0.0
    for et, co in o["cellules"].items():
        cr = r["cellules"].get(et)
        if cr is None:
            diffs.append(f"cellule absente du rejeu : {et}")
            continue
        vo, vr = valeurs_cellule(co), valeurs_cellule(cr)
        for k in vo:
            n_champs += 1
            if vo[k] != vr[k]:
                diffs.append(f"{et}|{k} : v8 {vo[k]} rejeu {vr[k]}")
                max_abs = max(max_abs, abs(vo[k] - vr[k]))
    no, nr = n80s(o), n80s(r)
    for k in no:
        n_champs += 1
        if no[k] != nr.get(k, "absent"):
            diffs.append(f"{k} : v8 {no[k]} rejeu {nr.get(k, 'absent')}")
            if isinstance(no[k], (int, float)) and isinstance(nr.get(k), (int, float)):
                max_abs = max(max_abs, abs(no[k] - nr[k]))
    pire, par_cellule, n80p = resume(r)
    resumes[nom] = (pire, par_cellule, n80p)
    res["passages"][nom] = {"sha256_rejeu": hr, "sha256_v8": ho, "graine_rejeu": r["reglages"]["graine"], "graine_v8": o["reglages"]["graine"],
                            "numpy_rejeu": r.get("environnement", {}).get("numpy") if isinstance(r.get("environnement"), dict) else None,
                            "champs_compares": n_champs, "differences": len(diffs), "ecart_absolu_maximal": max_abs, "premieres_differences": diffs[:20],
                            "fiche_pire_tronquee": {n: {s: tr(x) for s, x in v.items()} for n, v in pire.items()},
                            "fiche_pire_brute": pire, "n_pire": n80p, "n_par_cellule": par_cellule,
                            "n_h": {"seuil40": nh(n80p["n80|retenue_ebh"]) if n80p.get("n80|retenue_ebh") else None,
                                    "seuil160": nh(n80p["n80|atteinte_160"]) if n80p.get("n80|atteinte_160") else None}}
# neuvième comparateur : bases à huit comparateurs lues dans la v8 (rho0) ou dans le rejeu (meme-rho0.17)
for nom9, base in BASE_K8.items():
    if base in resumes:
        _, pc8, p8 = resumes[base]
    else:
        o, _ = charger(os.path.join(V8, f"simulation-puissance-garde-delta-v8-sortie-{base}.json"))
        _, pc8, p8 = resume(o)
    _, pc9, p9 = resumes[nom9]
    bloc = {"base_k8": base}
    for m in ("retenue_ebh", "atteinte_160"):
        c = f"n80|{m}"
        par = {cell: pc9[cell][c] - pc8[cell][c] for cell in pc9}
        bloc[m] = {"surcout_par_cellule": par, "surcout_maximal_definition_du_rapport": max(par.values()),
                   "n80_pire_k8": p8[c], "n80_pire_k9": p9[c], "ecart_des_n80_pires": p9[c] - p8[c],
                   "n_h_k8": nh(p8[c]), "n_h_k9": nh(p9[c]), "ecart_des_n_h": nh(p9[c]) - nh(p8[c])}
    res["passages"][nom9]["neuvieme"] = bloc
with open(SORTIE, "x", encoding="utf-8") as f:
    json.dump(res, f, indent=1, ensure_ascii=False)
    f.write("\n")
for nom, p in res["passages"].items():
    print(nom, "| champs", p["champs_compares"], "| différences", p["differences"], "| écart max", p["ecart_absolu_maximal"])
    print("   fiche pire 288 :", p["fiche_pire_tronquee"]["288"], "| 400 :", p["fiche_pire_tronquee"]["400"], "| n pires :", p["n_pire"], "| n_h :", p["n_h"])
    if "neuvieme" in p:
        for m in ("retenue_ebh", "atteinte_160"):
            q = p["neuvieme"][m]
            print("   neuvième", m, ": surcoût max (rapport)", q["surcout_maximal_definition_du_rapport"], "| n80 pire k8 → k9", q["n80_pire_k8"], "→", q["n80_pire_k9"],
                  "| n_h", q["n_h_k8"], "→", q["n_h_k9"], "(", q["ecart_des_n_h"], ")")
