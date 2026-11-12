"""Reproductibilité des rejeux d'audit sous le nul v8 (déjà lus) et lien entre lois non exactes et taux de rejeu — v1.

Rejoue, sous le juge v8 seulement (jamais le v9), deux lois promues de W2 avec les graines de l'audit de la course, et compare
les comptes à ceux de la sortie scellée. Relie aussi chaque loi promue à son compte d'audit et à son écart à la loi du monde.

Usage : python -I reproduire_rejeux_v8_v1.py <attaque-goodhart-v3.json> <manifeste.json> <arbre organisme 291e917>
"""
import json
import sys
import time


def main():
    sortie, manifeste, arbre = sys.argv[1:4]
    d = json.load(open(sortie, encoding="utf-8"))
    m = json.load(open(manifeste, encoding="utf-8"))
    entropie = int(m["reglages"]["entropie_racine"])
    sys.path.insert(0, arbre + "/orchestrator")
    from pole import attaque_goodhart_v2 as ag

    audit = {(r["carte"], r["etiquette"], r["k"]): r for r in d["audit_A2"] if r["monde"] == "W2"}
    lignes = []
    for s in d["suites"]:
        if s["monde"] != "W2" or s["juge"] != "v8" or s["premiere_promotion"] is None:
            continue
        t = [t for t in s["tentatives"] if t["k"] == s["premiere_promotion"]][0]
        etiquette = ag.etiquette_suite(s["monde"], s["fournisseur"], s["condition"], s["juge"])
        c = ag.carte(entropie, s["carte"], "W2")
        L, loi = c["L"], t["loi"]
        exacte = loi.get("lois", {}).get("0") == L["S1"] and loi.get("lois", {}).get("1") == L["S2"]
        r = audit[(s["carte"], etiquette, t["k"])]
        lignes.append({"carte": s["carte"], "condition": s["condition"], "k": t["k"], "loi_du_monde": exacte,
                       "audit": f'{r["promues"]}/{r["rejeux"]}', "etiquette": etiquette, "loi": loi})
    non_exactes = [x for x in lignes if not x["loi_du_monde"]]
    print("lois promues :", len(lignes), "; égales à la loi du monde (égalité exacte des objets) :",
          sum(x["loi_du_monde"] for x in lignes))
    print("lois non égales à la loi du monde et leur audit :",
          [(x["carte"], x["condition"], x["k"], x["audit"]) for x in non_exactes])
    exactes_audit = sorted(int(x["audit"].split("/")[0]) for x in lignes if x["loi_du_monde"])
    print("audit des lois égales à la loi du monde : min", exactes_audit[0], "max", exactes_audit[-1],
          "; à 200/200 :", sum(v == 200 for v in exactes_audit), "sur", len(exactes_audit))

    # Reproduction exacte de deux comptes d'audit sous v8 : la plus basse et une à 200/200
    choix = sorted(lignes, key=lambda x: int(x["audit"].split("/")[0]))
    for x in (choix[0], choix[-1]):
        t0 = time.time()
        res = ag._rejouer_loi((entropie, "W2", x["carte"], x["etiquette"], x["k"], x["loi"], "v8", 200, "audit"))
        print(f'carte {x["carte"]} {x["condition"]} k={x["k"]} : audit scellé {x["audit"]}, rejoué {res["promues"]}/{res["rejeux"]}'
              f' ({"identique" if f"{res['promues']}/{res['rejeux']}" == x["audit"] else "DIFFÉRENT"}), {time.time() - t0:.1f} s')


if __name__ == "__main__":
    main()
