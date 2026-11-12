"""Contre-lecture courte : attaque « un exemple retiré » et fautes d'étendue partielle sous les seuils v8, aux effectifs réels
de P3 (478 exemples d'entraînement de la tromperie, 1 591 des enjeux), données synthétiques du calibrage du développeur
(`calibrage_gardes_v1.py` importé tel quel : mêmes tirages, même spectre), paliers par `reextraction_p3_v1.palier` de l'arbre.

    python -I attaque_fautes_partielles_v8.py SRC PIECES SORTIE.json
"""
import importlib.util, json, sys, time
from pathlib import Path
import numpy as np

src, pieces, sortie = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
sys.path.insert(0, src)
spec = importlib.util.spec_from_file_location("cal", pieces / "calibrage_gardes_v1.py")
cal = importlib.util.module_from_spec(spec); spec.loader.exec_module(cal)
from controle_ia.t07 import reextraction_p3_v1 as rx

TOL = dict(rx.TOLERANCES)
assert TOL == {"processeur": 1e-6, "carte_sonde": 1e-3, "carte_directions": 1e-2}
CAS = {"tromperie": dict(n_ex=478, longueur=(2, 8)), "enjeux": dict(n_ex=1591, longueur=(20, 40))}
res = {"debut": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "tolerances": TOL, "cas": {}}

def pal(e, garde):
    x = {"identique": e["identique"], "ecart": max(e["ecart_w_max"], e["ecart_b_max"]), "motif": None}
    return rx.palier([x], TOL[f"carte_{garde}"], TOL)[0]

for concept, cas in CAS.items():
    seqs, y = cal.donnees(concept, 1, **cas)
    s_dec, _ = cal.donnees(concept, 1, decalage=True, **cas)
    mu_norme = float(np.linalg.norm(np.concatenate([s.astype(np.float64) for s in seqs]).mean(axis=0)))
    ref = {r: cal.recette(r, seqs, y) for r in ("difference_moyennes", "plancher")}
    out = {"exemples": len(seqs), "jetons": int(sum(len(s) for s in seqs)), "fautes": {}}
    def mesurer(nom, s2, y2, avec_plancher=True):
        m = {}
        for r, g in (("difference_moyennes", "sonde"), ("plancher", "directions")):
            if r == "plancher" and not avec_plancher:
                continue
            e = cal.ecarts(*cal.recette(r, s2, y2), *ref[r], mu_norme)
            m[g] = {"ecart": max(e["ecart_w_max"], e["ecart_b_max"]), "palier": pal(e, g)}
        paliers = [v["palier"] for v in m.values()]
        m["bras"] = "arrêté" if "échec" in paliers else "établi, palier " + max(paliers, key=rx.PALIERS.index)
        out["fautes"][nom] = m
        print(concept, nom, json.dumps(m, ensure_ascii=False), flush=True)
    mesurer("un exemple retiré (avant-dernier)", seqs[:-2] + seqs[-1:], np.concatenate([y[:-2], y[-1:]]))
    mesurer("un exemple retiré (le premier)", seqs[1:], y[1:])
    rng = np.random.default_rng(20261111)
    ordre = rng.permutation(len(seqs))
    for p in (0.005, 0.01, 0.02, 0.05, 0.10):
        k = max(1, int(round(p * len(seqs))))
        choisis = set(ordre[:k].tolist())
        mesurer(f"empan décalé d'un jeton sur {k} exemples ({100 * p:g} %)", [s_dec[i] if i in choisis else seqs[i] for i in range(len(seqs))], y)
    # exemples les plus longs seulement (troncature différente des seuls exemples longs)
    longs = np.argsort([-len(s) for s in seqs])
    for p in (0.02, 0.05):
        k = max(1, int(round(p * len(seqs))))
        choisis = set(longs[:k].tolist())
        mesurer(f"dernier jeton perdu sur les {k} exemples les plus longs ({100 * p:g} %)", [seqs[i][:-1] if i in choisis else seqs[i] for i in range(len(seqs))], y)
    res["cas"][concept] = out
    del seqs, s_dec, ref
res["fin"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
sortie.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
