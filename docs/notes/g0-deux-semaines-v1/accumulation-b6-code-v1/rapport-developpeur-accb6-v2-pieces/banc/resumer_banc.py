"""Résumé des sorties du banc v2d (développeur accb6-v2) en lignes de tableau pour le rapport."""
import json
import re
import sys
from pathlib import Path

S = Path(sys.argv[1])
SURVIVANTES_CL = {"X02", "X04", "X05", "X06", "X07", "X08", "X10", "X13", "X14", "X21", "X22", "X25", "X30",
                  "G01", "G02", "G03", "G05", "G08", "G09", "G16", "G17", "G18"}          # contre-lecture, § 5 : survivantes aux 171 essais


def essai(x):
    p = x.get("premier_echec") or ""
    m = re.match(r"FAILED (tests/[^ ]+?)(?: - .*)?$", p)
    return (m.group(1) if m else p).replace("tests/", "")


for lot in ("mutations_temoin_v2", "mutations_accb6_code_v2", "mutations_cl_v1", "mutations_cl_v2", "mutations_accb6_v4"):
    lignes = [json.loads(l) for l in (S / f"banc-v2d-{lot}.jsonl").read_text(encoding="utf-8").splitlines()]
    print(f"\n### {lot} ({len(lignes)})")
    for x in lignes:
        etat = "erreur : " + x["erreur"] if x.get("erreur") else ("tuée" if x.get("tuee") else "SURVIT")
        enum = f" ; énumération : {x['enumeration']}" if x.get("enumeration") else ""
        cl = " (survivante aux 171 essais d'après la contre-lecture)" if x["id"] in SURVIVANTES_CL else ""
        print(f"| {x['id']} | {x['quoi']}{cl} | {etat} | {essai(x) if x.get('tuee') else x.get('derniere_ligne', '')} | {x.get('duree_s')}{enum} |")
