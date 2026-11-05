"""CL8 : `relancable` (lanceur) contre la garde du relais à la relance, relais relancé à neuf (devis, point 4) ou non.
Usage : python3 -B sonde_relais_relance.py ARBRE"""
import importlib.util, json, os, sys
A = sys.argv[1]
sys.path.insert(0, A)
spec = importlib.util.spec_from_file_location("lanceur", os.path.join(A, "demonstrations", "ideation_v1.py"))
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
budgets = dict(L.BUDGETS_PAR_DEFAUT)
juges = [("juge-opus", "claude-opus-5-5"), ("juge-fable", "claude-fable-5-1")]
res = {}
for total, plafond_relais in ((40.0, 40.0), (41.0, 41.0)):
    verif = {"somme_claude": 0.4 + 2 * (5 + 9.3) + 4 + 7 - 40.0 + total - (total - 40.0), "somme_externe": 11.2}
    verif["somme_claude"] = 40.0  # somme de cette course aux réglages du devis
    relais = {"plafond_usd": plafond_relais, "reserve_par_appel_usd": 4.0, "depense_usd": 0.0}
    ok, motifs = L.relance_possible(1, verif, 0.4, 0.15, total, 11.6, False, False, True, relais, budgets, juges)
    def garde(depense):
        try:
            L.verifier_relais({"plafond_usd": plafond_relais, "reserve_par_appel_usd": 4.0, "depense_usd": depense}, total,
                              budgets, juges)
            return "acceptée"
        except Exception as e:  # noqa: BLE001
            return "refus : " + str(e)[:120]
    res[f"total {total}, relais {plafond_relais}"] = {"relancable": ok, "motifs": motifs,
                                                       "relance, relais relancé à neuf (dépense 0)": garde(0.0),
                                                       "relance, relais gardé (dépense 0,4)": garde(0.4)}
print(json.dumps(res, ensure_ascii=False, indent=1))
