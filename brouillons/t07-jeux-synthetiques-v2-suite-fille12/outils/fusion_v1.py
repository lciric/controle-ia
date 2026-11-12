#!/usr/bin/env python3
"""Fusion (fille 12) : pour r08–r17, D + direction viennent de ../t07-...-brouillon1/taches/ (inchangés), les paires 1-5 « contrôles »
viennent de remises-controles/. Écrit taches/rNN-ID.jsonl (dossier neuf). Usage : fusion_v1.py rNN [rNN…]"""
import json, sys, glob
from pathlib import Path
ici = Path(__file__).resolve().parents[1]
anc = ici.parent / "t07-jeux-synthetiques-v2-brouillon1" / "taches"
(ici / "taches").mkdir(exist_ok=True)
for r in sys.argv[1:]:
    ancien = glob.glob(str(anc / f"{r}-*.jsonl"))[0]; nom = Path(ancien).name
    new = [json.loads(l) for l in open(ici / "remises-controles" / nom)]
    keep = [json.loads(l) for l in open(ancien)]
    keep = [d for d in keep if not (d["jeu"] == "intention-autres-modes" and d["mode"] == "controles")]
    allr = [d for d in keep if d["jeu"] == "dissimulation"] + sorted(new, key=lambda d: (d["paire"], d["etiquette"])) + \
           [d for d in keep if d["jeu"] == "intention-autres-modes"]
    out = ici / "taches" / nom
    assert not out.exists(), out
    with open(out, "w") as f:
        for d in allr: f.write(json.dumps(d, ensure_ascii=False) + "\n")
    print(out.name, len(allr))
