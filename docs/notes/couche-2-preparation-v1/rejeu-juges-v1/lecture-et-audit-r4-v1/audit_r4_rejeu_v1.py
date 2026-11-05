"""Audit R4 du rejeu des juges (fiche, plan d'analyse point 4) : relit les notations tirées par la lecture gelée.
Pour chaque cellule : motifs des scores non finis, notes écrites non admises (forme), et écart entre la note écrite
(entière part) et la lecture par probabilité aux critères concernés. Lecture seule ; aucune autre lecture n'en sort."""
import json, re, sys, collections
from pathlib import Path
run = Path(sys.argv[1]); lec = json.loads((run / "lecture-rejeu-v1.json").read_text())
cells = lec["resultat"]["cellules"] if "resultat" in lec else lec["cellules"]
out = {}
for cle_cell, c in cells.items():
    juge, var = cle_cell.split("/")
    charge = lambda v: {r["cle"]: r for r in json.loads((run / f"rejeu-{juge}-{v}.json").read_text())["resultat"]["notations"]}
    # « budget relevé » est composé (fiche) : b0 relu, remplacé par le rejeu au budget relevé là où il existe.
    recs = charge(var) if var != "budget-releve" else {**charge("b0-relu"), **charge("budget-releve")}
    tirees = c["audit_r4"]["notations"]
    motifs = collections.Counter(); formes = collections.Counter(); ecarts = []
    finis = 0; tronq = 0
    for k in tirees:
        r = recs[k]; p = r["proba"]
        tronq += bool(r.get("tronquee"))
        if p.get("score") is not None: finis += 1
        else: motifs[str(p.get("motif"))[:90]] += 1
        for a in r["ecrit"].get("anomalies", []):
            m = re.match(r"(\w+) : (.*?)\('([^']*)'\)", a)
            if not m: formes[a[:60]] += 1; continue
            crit, quoi, val = m.groups(); formes[quoi.strip() + " ex. " + val] += 1
            pc = p.get("criteres", {}).get(crit)
            try: v = float(val.replace(",", "."))
            except ValueError: continue
            if pc: ecarts.append(round(pc["esperance"] - v, 3))
    out[cle_cell] = {"tirees": len(tirees), "finies_parmi_tirees": finis, "tronquees": tronq,
                     "motifs_non_finis": motifs.most_common(6), "anomalies_ecrites": formes.most_common(8),
                     "esperance_moins_note_ecrite": {"n": len(ecarts),
                        "moyenne": round(sum(ecarts) / len(ecarts), 3) if ecarts else None,
                        "min": min(ecarts) if ecarts else None, "max": max(ecarts) if ecarts else None}}
print(json.dumps(out, ensure_ascii=False, indent=1))
