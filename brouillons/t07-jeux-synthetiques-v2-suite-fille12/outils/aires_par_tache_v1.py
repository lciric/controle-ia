#!/usr/bin/env python3
"""Aires sac de mots par pli (une tâche laissée de côté), lues du script officiel (fonction importée, non modifiée).
Usage : aires_par_tache_v1.py DOSSIER_ASSEMBLE  → JSON {jeu/mode/empan: {tâche: aire}, moyenne}"""
import importlib.util, json, sys
from pathlib import Path
RACINE = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RACINE / "src"))
spec = importlib.util.spec_from_file_location("v", RACINE / "scripts/verifier_jeux_synthetiques_t07_v2.py")
v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
d = Path(sys.argv[1]); recs = [json.loads(l) for l in open(d / "intention-autres-modes-v2.jsonl")]
sortie = {}
for mode in ("controles", "direction"):
    for nom, ext in (("entiere", lambda s: s["reponse"]), ("avant_COST", v.empan_avant)):
        docs, et, ta = [], [], []
        for s in recs:
            if s["mode"] != mode: continue
            docs.append(v.normaliser(ext(s))); et.append(s["etiquette"]); ta.append(s["tache"])
        vus = []; orig = v.aire_sous_la_courbe
        def capte(sc, e):
            a = orig(sc, e); vus.append(a); return a
        v.aire_sous_la_courbe = capte
        moy, n = v.aire_sac_de_mots(docs, et, ta); v.aire_sous_la_courbe = orig
        taches = sorted(set(ta))
        sortie[f"{mode}/{nom}"] = {"moyenne": round(moy, 3), "plis": n,
                                   "par_tache": {t: round(a, 3) for t, a in zip(taches, vus)}}
print(json.dumps(sortie, indent=1))
