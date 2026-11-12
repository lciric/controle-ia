"""CL11 : relance après contrôles Claude payés (0,4), réglages du devis v7 nonies (total 40, relais 40, réserve 4)."""
import importlib.util, json, os, sys
A = sys.argv[1]; sys.path.insert(0, A)
spec = importlib.util.spec_from_file_location("lanceur", os.path.join(A, "demonstrations", "ideation_v1.py"))
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
budgets = {("proposeur_ideation", "claude-opus-5-5"): 5.0, ("proposeur_ideation", "claude-fable-5-1"): 9.3,
           ("juge_ideation", "claude-opus-5-5"): 4.0, ("juge_ideation", "claude-fable-5-1"): 7.0}
juges = [("juge-fable", "claude-fable-5-1"), ("juge-opus", "claude-opus-5-5")]
repris = {k: {"repris_de_tentative": 1, "relais_apres_depense_usd": v} for k, v in
          (("cle-opus", 0.2), ("cle-fable", 0.4))}
res = {}
for nom, depense in (("relais relancé (dépense lue 0)", 0.0), ("relais gardé (dépense lue 0,4)", 0.4)):
    gardes, motifs = L.filtrer_reprises_claude(repris, lambda d=depense: {"depense_usd": d})
    n = 2 - len(gardes)
    somme = 0.4 + 0.2 * n + 2 * (5 + 9.3) + 4 + 7  # cout_tentatives_claude + contrôles à jouer + passes + juges (code)
    try:
        L.verifier_relais({"plafond_usd": 40.0, "reserve_par_appel_usd": 4.0, "depense_usd": depense}, 40.0, budgets, juges)
        relais = "accepté"
    except Exception as e:  # noqa: BLE001
        relais = "refus : " + str(e)[:160]
    res[nom] = {"controles_claude_rejoues": n, "motifs": motifs, "somme_claude_relance": round(somme, 4),
                "somme_refusee (> 40)": somme > 40 + 1e-9, "garde_du_relais": relais}
print(json.dumps(res, ensure_ascii=False, indent=1))
