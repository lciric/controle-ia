"""Complément du calibrage v1 (même module, mêmes données, mêmes mesures) : le témoin « différence de moyennes » sur les
données de type « enjeux » (la sonde principale des enjeux, linéaire, s'est montrée chaotique au calibrage v1).

    python calibrage_gardes_v2.py RACINE_SRC SORTIE.json
"""
import importlib.util
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("calibrage_gardes_v1", ICI / "calibrage_gardes_v1.py")
v1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v1)
v1.RECETTES = {"enjeux": ["difference_moyennes"]}
_main = v1.main


def main(argv):
    if "--cas" in argv:
        return _main(argv)
    src, sortie = argv[0], Path(argv[1])
    sys.path.insert(0, src)
    import json, os, subprocess, time
    import numpy as np
    res = {"debut": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "cas": {}}
    concept = "enjeux"
    seqs, y = v1.donnees(concept, 1, **v1.CAS[concept])
    entree = sortie.parent / f"donnees-{concept}-v2.npz"
    v1.sauver(seqs, y, entree)
    out = {}
    for fils in (1, 4):
        f = sortie.parent / f"v2-{concept}-{fils}.npz"
        env = {**os.environ, "OPENBLAS_NUM_THREADS": str(fils), "OMP_NUM_THREADS": str(fils), "MKL_NUM_THREADS": str(fils)}
        subprocess.run([sys.executable, "-I", str(ICI / "calibrage_gardes_v2.py"), src, str(sortie), "--cas", concept, "--fils", str(fils),
                        "--sortie-npz", str(f), "--entree", str(entree)], check=True, env=env)
        out[fils] = np.load(f)
    seqs, y = v1.charger(entree)
    mu_norme = float(np.linalg.norm(np.concatenate([s.astype(np.float64) for s in seqs]).mean(axis=0)))
    r = "difference_moyennes"
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
    print(concept, r, json.dumps(m), flush=True)
    res["cas"][concept] = {"recettes": {r: m}, "jetons": int(sum(len(s) for s in seqs)), "exemples": len(seqs)}
    res["fin"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    sortie.write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
