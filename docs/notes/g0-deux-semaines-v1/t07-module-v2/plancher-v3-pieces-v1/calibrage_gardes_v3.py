"""Calibrage des gardes d'identité, v3 (CLP3-01, R-2305) : rejoue le calibrage v1 et v2 (mêmes données synthétiques, mêmes
recettes, même code : `calibrage_gardes_v1.py` importé) et y applique les paliers des seuils v7 (carte 10⁻², 10⁻¹) et v8
(carte 10⁻³, 10⁻²) : pour chaque recette et chaque perturbation, l'écart et le palier sous chaque jeu de seuils ; puis les deux
exigences de la mère : toute faute calibrée arrêtée par le témoin (v8), un bruit de 10⁻³ par jeton qui passe (v8).

    python -I calibrage_gardes_v3.py RACINE_SRC SORTIE.json
"""
import importlib.util
import json
import os
import subprocess
import sys
import time
from pathlib import Path

ICI = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("calibrage_gardes_v1", ICI / "calibrage_gardes_v1.py")
v1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v1)
SEUILS = {"v7": {"processeur": 1e-6, "carte_sonde": 1e-2, "carte_directions": 1e-1},
          "v8": {"processeur": 1e-6, "carte_sonde": 1e-3, "carte_directions": 1e-2}}
v1.RECETTES = {"tromperie": ["difference_moyennes", "plancher"], "enjeux": ["difference_moyennes", "lineaire", "plancher"]}


def palier(e: dict, plafond: float, s: dict) -> str:
    x = max(e["ecart_w_max"], e["ecart_b_max"])
    if e["identique"]:
        return "identique"
    if x <= s["processeur"]:
        return "processeur"
    if x <= plafond:
        return "carte"
    return "échec"


def main(argv):
    if "--cas" in argv:
        return v1.main(argv)
    src, sortie = argv[0], Path(argv[1])
    sys.path.insert(0, src)
    import numpy as np
    res = {"debut": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "seuils": SEUILS, "cas": {}}
    for concept in ("tromperie", "enjeux"):
        seqs, y = v1.donnees(concept, 1, **v1.CAS[concept])
        entree = sortie.parent / f"donnees-{concept}-v3.npz"
        v1.sauver(seqs, y, entree)
        out = {}
        for fils in (1, 4):
            f = sortie.parent / f"v3-{concept}-{fils}.npz"
            env = {**os.environ, "OPENBLAS_NUM_THREADS": str(fils), "OMP_NUM_THREADS": str(fils), "MKL_NUM_THREADS": str(fils)}
            subprocess.run([sys.executable, "-I", __file__, src, str(sortie), "--cas", concept, "--fils", str(fils), "--sortie-npz", str(f),
                            "--entree", str(entree)], check=True, env=env)
            out[fils] = dict(np.load(f))
            f.unlink()
        seqs, y = v1.charger(entree)
        mu_norme = float(np.linalg.norm(np.concatenate([s.astype(np.float64) for s in seqs]).mean(axis=0)))
        cas = {"jetons": int(sum(len(s) for s in seqs)), "exemples": len(seqs), "recettes": {}}
        for r in v1.RECETTES[concept]:
            W0, B0 = out[1][f"{r}_W"], out[1][f"{r}_B"]
            m = {"fils_1_contre_4": v1.ecarts(out[4][f"{r}_W"], out[4][f"{r}_B"], W0, B0, mu_norme)}
            for rr in (1e-4, 1e-3, 1e-2):
                m[f"carte_r{rr:g}"] = v1.ecarts(*v1.recette(r, v1.bruit(seqs, rr, 9), y), W0, B0, mu_norme)
            m["artefact_un_exemple_retire"] = v1.ecarts(*v1.recette(r, seqs[:-2] + seqs[-1:], np.concatenate([y[:-2], y[-1:]])), W0, B0, mu_norme)
            s_dec, _ = v1.donnees(concept, 1, decalage=True, **v1.CAS[concept])
            m["artefact_empan_decale"] = v1.ecarts(*v1.recette(r, s_dec, y), W0, B0, mu_norme)
            s_c, _ = v1.donnees(concept, 1, autre_couche=True, **v1.CAS[concept])
            m["artefact_autre_couche"] = v1.ecarts(*v1.recette(r, s_c, y), W0, B0, mu_norme)
            rng = np.random.default_rng(5)
            echange = set(rng.choice(len(seqs), size=len(seqs) // 5, replace=False).tolist())
            s_d, _ = v1.donnees(concept, 2, **v1.CAS[concept])
            m["artefact_autre_decoupage_20pc"] = v1.ecarts(*v1.recette(r, [s_d[i] if i in echange else seqs[i] for i in range(len(seqs))], y),
                                                           W0, B0, mu_norme)
            garde = "directions" if r == "plancher" else "sonde"
            for nom, e in m.items():
                e["paliers"] = {v: palier(e, s[f"carte_{garde}"], s) for v, s in SEUILS.items()}
            cas["recettes"][r] = m
            print(concept, r, json.dumps({k: (round(x["ecart_w_max"], 8), x["paliers"]) for k, x in m.items()}, ensure_ascii=False), flush=True)
        entree.unlink()
        res["cas"][concept] = cas
    t = {c: res["cas"][c]["recettes"]["difference_moyennes"] for c in res["cas"]}
    res["exigences_v8"] = {
        "fautes_arretees_par_le_temoin": {c: {k: x["paliers"]["v8"] for k, x in t[c].items() if k.startswith("artefact_")} for c in t},
        "bruit_1e-3_passe": {c: {g: res["cas"][c]["recettes"][r]["carte_r0.001"]["paliers"]["v8"]
                                 for g, r in (("temoin", "difference_moyennes"), ("directions", "plancher"))} for c in t}}
    res["toutes_les_fautes_arretees_par_le_temoin_v8"] = all(p == "échec" for c in t for p in res["exigences_v8"]["fautes_arretees_par_le_temoin"][c].values())
    res["bruit_1e-3_passe_v8"] = all(p != "échec" for c in t for p in res["exigences_v8"]["bruit_1e-3_passe"][c].values())
    res["fin"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    sortie.write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: res[k] for k in ("toutes_les_fautes_arretees_par_le_temoin_v8", "bruit_1e-3_passe_v8")}), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
