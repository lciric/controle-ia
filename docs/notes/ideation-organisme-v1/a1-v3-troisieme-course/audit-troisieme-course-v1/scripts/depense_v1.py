"""Dépense et appariement : registre de dépense cumulée (début/fin par appel), journal du relais, trace ; jetons, coûts, durées."""
import json, sys
from collections import Counter
reg, rel, trace = sys.argv[1:4]
R = [json.loads(l) for l in open(reg, encoding="utf-8")]
J = [json.loads(l) for l in open(rel, encoding="utf-8")]
o = json.load(open(trace, encoding="utf-8"))
deb = {r["id"]: r for r in R if r["type"] == "debut"}; fin = {r["id"]: r for r in R if r["type"] == "fin"}
ap = [a for s in o["suites"] for t in s["tentatives"] for a in t["appels"]]
out = {"registre": {"debuts": len(deb), "fins": len(fin), "debuts_sans_fin": len(set(deb) - set(fin)), "fins_sans_debut": len(set(fin) - set(deb)),
                    "statuts_fin": dict(Counter(f["statut"] for f in fin.values())), "codes_fin": dict(Counter(f["code"] for f in fin.values())),
                    "depassement_reserve": sum(f["depassement_reserve"] for f in fin.values()), "cout_origine": dict(Counter(f["cout_origine"] for f in fin.values())),
                    "cout_usd": round(sum(f["cout_usd"] for f in fin.values()), 5), "pire_cas_max": max(d["pire_cas_usd"] for d in deb.values()),
                    "plafond_etape": sorted({d["plafond_etape_usd"] for d in deb.values()}), "modeles": dict(Counter(d["modele"] for d in deb.values())),
                    "premier": min(d["quand_utc"] for d in deb.values()), "dernier": max(f["quand_utc"] for f in fin.values())},
       "relais": {"appels": len(J), "statuts": dict(Counter(j["statut"] for j in J)), "echecs": dict(Counter(str(j["echec"]) for j in J)),
                  "fins": dict(Counter(j["fin"] for j in J)), "cout_usd": round(sum(j["cout_usd"] for j in J), 5), "cumul_final": J[-1]["depense_cumulee_usd"],
                  "jetons_entree": sum(j["usage"]["entree"] for j in J), "jetons_sortie": sum(j["usage"]["sortie"] for j in J),
                  "max_tokens": sorted({j["max_tokens"] for j in J}), "sortie_max": max(j["usage"]["sortie"] for j in J),
                  "duree_s_somme": round(sum(j["duree_s"] for j in J), 1), "duree_s_max": max(j["duree_s"] for j in J),
                  "modeles_servis": dict(Counter(j["modele_servi"] for j in J)), "numeros_continus": [j["appel"] for j in J] == list(range(1, len(J) + 1))},
       "trace": {"appels": len(ap), "cout_usd": round(sum(a["cout_usd"] for a in ap), 5), "depense_usd": o["depense_usd"], "duree_s": o["duree_s"]}}
# appariement des coûts : multiensembles égaux (trace, registre, relais)
c = lambda L: sorted(round(x, 5) for x in L)  # noqa: E731
out["appariement_couts_trace_registre_relais"] = c(a["cout_usd"] for a in ap) == c(f["cout_usd"] for f in fin.values()) == c(j["cout_usd"] for j in J)
print(json.dumps(out, ensure_ascii=False, indent=1))
