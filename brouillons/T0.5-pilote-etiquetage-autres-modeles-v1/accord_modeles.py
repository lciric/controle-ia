"""Accord des séries B et C (autres modèles) avec les séries 1 et 2 et leur consensus, sur les 480 paires du pilote.
Plan scellé : brouillons/T0.5-pilote-etiquetage-autres-modeles-v1-plan.md. Nombres seulement ; aucun texte de paire lu."""
import json
import sys
from pathlib import Path

etiquettes_scellees, serie2_json, dossier_b, dossier_c, sortie = (Path(x) for x in sys.argv[1:6])
elements = json.loads(etiquettes_scellees.read_text(encoding="utf-8"))
elements = elements.get("resultat", elements)["elements"]
s2 = json.loads(serie2_json.read_text(encoding="utf-8"))


def charger(dossier):
    out = {}
    for lot in sorted(p.name for p in dossier.iterdir() if p.is_dir()):
        e = json.loads((dossier / lot / "etiquettes.json").read_text(encoding="utf-8"))
        ids = [p["id"] for p in json.loads((dossier / lot / "paires.json").read_text(encoding="utf-8"))]
        assert isinstance(e, dict) and sorted(e) == sorted(ids) and set(e.values()) <= {"Yes", "No"}, (dossier, lot)
        out.update({(lot, i): v for i, v in e.items()})
    assert len(out) == 480
    return out


B, C = charger(dossier_b), charger(dossier_c)


def kappa(paires, poids=None):
    w = poids or [1.0] * len(paires)
    tot = sum(w)
    if not paires:
        return {"kappa": None, "accord": None, "n": 0}
    po = sum(wi for (a, b), wi in zip(paires, w) if a == b) / tot
    pa = sum(wi for (a, _), wi in zip(paires, w) if a) / tot
    pb = sum(wi for (_, b), wi in zip(paires, w) if b) / tot
    pe = pa * pb + (1 - pa) * (1 - pb)
    return {"accord": po, "kappa": None if pe == 1 else (po - pe) / (1 - pe), "oui_ref": pa, "oui_serie": pb,
            "n": len(paires), "desaccords": sum(1 for a, b in paires if a != b)}


groupes = {"tout": lambda e: True, "controls": lambda e: e["famille"] == "controls",
           "fruitful_directions": lambda e: e["famille"] == "fruitful_directions",
           "sterile_directions": lambda e: e["famille"] == "sterile_directions"}
res = {}
for g, f in groupes.items():
    sel = [e for e in elements if f(e)]
    r = {}
    for nom, serie in (("B", B), ("C", C)):
        x = [serie[(e["lot"], e["id"])] == "Yes" for e in sel]
        s1 = [e["etiquette"] == "Yes" for e in sel]
        s2v = [s2[e["lot"]][e["id"]] == "Yes" for e in sel]
        w = [float(e["poids"]) for e in sel]
        cons = [(a, xi, wi) for a, b, xi, wi in zip(s1, s2v, x, w) if a == b]
        r[nom] = {"contre_serie1_brut": kappa(list(zip(s1, x))), "contre_serie2_brut": kappa(list(zip(s2v, x))),
                  "contre_consensus_brut": kappa([(a, xi) for a, xi, _ in cons]),
                  "contre_consensus_pondere": kappa([(a, xi) for a, xi, _ in cons], [wi for _, _, wi in cons])}
    res[g] = r
sortie.write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
for g, r in res.items():
    for nom, v in r.items():
        print(g, nom, {k: (round(x["kappa"], 3) if x["kappa"] is not None else None, x.get("desaccords"),
                           round(x.get("oui_serie", 0), 3)) for k, x in v.items()})
