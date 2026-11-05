"""Accord entre la série 1 (scellée, etiquettes.json) et la série 2 (double étiquetage à l'aveugle) des paires du pilote.
Plan scellé : brouillons/T0.5-pilote-double-etiquetage-v1-plan.md. Nombres seulement ; aucun texte de paire n'est lu."""
import json
import sys
from pathlib import Path

etiquettes_scellees, dossier_serie2, sortie = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
r = json.loads(etiquettes_scellees.read_text(encoding="utf-8"))
elements = r.get("resultat", r)["elements"]

serie2 = {}
for lot in sorted(p.name for p in dossier_serie2.iterdir() if p.is_dir()):
    e = json.loads((dossier_serie2 / lot / "etiquettes.json").read_text(encoding="utf-8"))
    ids = [p["id"] for p in json.loads((dossier_serie2 / lot / "paires.json").read_text(encoding="utf-8"))]
    assert isinstance(e, dict) and sorted(e) == sorted(ids) and set(e.values()) <= {"Yes", "No"}, lot
    for i, v in e.items():
        serie2[(lot, i)] = v
assert len(serie2) == len(elements) == 480, (len(serie2), len(elements))


def kappa(paires, poids=None):
    """Kappa de Cohen (pondéré par les poids de tirage si donnés) entre deux listes binaires."""
    w = poids or [1.0] * len(paires)
    tot = sum(w)
    po = sum(wi for (a, b), wi in zip(paires, w) if a == b) / tot
    pa = sum(wi for (a, _), wi in zip(paires, w) if a) / tot
    pb = sum(wi for (_, b), wi in zip(paires, w) if b) / tot
    pe = pa * pb + (1 - pa) * (1 - pb)
    return {"accord": po, "kappa": None if pe == 1 else (po - pe) / (1 - pe), "oui_1": pa, "oui_2": pb, "n": len(paires)}


resultats = {}
groupes = {"tout": lambda e: True, "controls": lambda e: e["famille"] == "controls",
           "fruitful_directions": lambda e: e["famille"] == "fruitful_directions",
           "sterile_directions": lambda e: e["famille"] == "sterile_directions",
           "directions": lambda e: e["famille"] != "controls"}
for g, f in groupes.items():
    sel = [e for e in elements if f(e)]
    s1 = [e["etiquette"] == "Yes" for e in sel]
    s2 = [serie2[(e["lot"], e["id"])] == "Yes" for e in sel]
    o8 = [bool(e["oui_8b"]) for e in sel]
    w = [float(e["poids"]) for e in sel]
    resultats[g] = {
        "serie1_serie2_brut": kappa(list(zip(s1, s2))),
        "serie1_serie2_pondere": kappa(list(zip(s1, s2)), w),
        "8B_serie1_pondere": kappa(list(zip(o8, s1)), w),
        "8B_serie2_pondere": kappa(list(zip(o8, s2)), w),
    }
sortie.write_text(json.dumps(resultats, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
for g, v in resultats.items():
    print(g, {k: (round(x["kappa"], 3) if x["kappa"] is not None else None, round(x["accord"], 3), x["n"]) for k, x in v.items()})
