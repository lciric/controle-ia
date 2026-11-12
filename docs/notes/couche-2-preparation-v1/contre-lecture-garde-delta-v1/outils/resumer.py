"""Résume une sortie de simulation-puissance-garde-delta-v1 : tableau par loi, δ, n, candidat, seuil."""
import json, sys
d = json.load(open(sys.argv[1]))
print("plancher", d["plancher_structurel"])
for loi, bloc in d["lois"].items():
    print("==", loi)
    for cle, res in bloc["cellules"].items():
        ligne = [cle]
        for nom in ("honnete", "frontiere", "tricheur"):
            c = res[nom]["certification"]
            ligne.append(f"{nom[:4]} moy={res[nom]['moyenne_g']:+.4f} sd={res[nom]['ecart_type_g']:.4f} " +
                         " ".join(f"s{s}={v['part']:.4f}(med {v['unites_mediane_si_certifie']})" for s, v in c.items()))
        print(" | ".join(ligne))
    print("n80", bloc.get("n_pour_puissance_0_8"))
