import json, sys, collections
D, S = sys.argv[1], sys.argv[2]
sys.path.insert(0, D)
import generer_items_v2 as gen
def jl(p): return [json.loads(x) for x in open(p, encoding="utf-8") if x.strip()]
i1 = {x["item"]: x for x in jl(f"{S}/gen1/items-epreuve-v1.jsonl")}
i2 = {x["item"]: x for x in jl(f"{S}/gen2/items-epreuve-v2.jsonl")}
c1 = {x["item"]: x for x in jl(f"{S}/gen1/cle-epreuve-v1.jsonl")}
c2 = {x["item"]: x for x in jl(f"{S}/gen2/cle-epreuve-v2.jsonl")}
print("mêmes identifiants :", set(i1) == set(i2), len(i2))
diff_non_retirer = [k for k in i2 if not (c2[k]["version"] == "plante" and c2[k]["type"] == "retirer") and i1[k] != i2[k]]
print("items hors « retirer » différents entre v1 et v2 :", len(diff_non_retirer))
diffcle = [k for k in c2 if not (c2[k]["version"] == "plante" and c2[k]["type"] == "retirer") and c1[k] != c2[k]]
print("clés hors « retirer » différentes :", len(diffcle))
# champs de clé des retirer : différences
ex = next(k for k in c2 if c2[k]["version"] == "plante" and c2[k]["type"] == "retirer")
print("champs clé retirer v1:", sorted(c1[ex].keys())); print("champs clé retirer v2:", sorted(c2[ex].keys()))
diffs = collections.Counter()
for k in c2:
    if c2[k]["version"] == "plante" and c2[k]["type"] == "retirer":
        for f in set(c1[k]) | set(c2[k]):
            if c1[k].get(f) != c2[k].get(f): diffs[f] += 1
print("champs de clé qui changent pour retirer :", dict(diffs))
# pas modifiés identiques ?
same_steps = sum(1 for k in c2 if c2[k]["version"]=="plante" and c2[k]["type"]=="retirer" and c1[k]["pas_modifies"]==c2[k]["pas_modifies"])
n_ret = sum(1 for k in c2 if c2[k]["version"]=="plante" and c2[k]["type"]=="retirer")
print("items retirer :", n_ret, "mêmes pas modifiés :", same_steps)
# aucun CONTROLS restant ; pas non modifiés inchangés vs jumeau
reste = tot = autres_changes = 0; pas_vides_jumeau = 0
jum = {c["tache"]: k for k, c in c2.items() if c["version"] == "jumeau"} if "tache" in next(iter(c2.values())) else None
for k, c in c2.items():
    if c["version"] != "plante" or c["type"] != "retirer": continue
    t2 = {x["pas"]: x["texte"] for x in i2[k]["pas"]}
    t1 = {x["pas"]: x["texte"] for x in i1[k]["pas"]}
    for p in c["pas_modifies"]:
        tot += 1
        if gen.analyser_controles(t2[p]): reste += 1
    for p in t2:
        if p not in c["pas_modifies"] and t2[p] != t1[p]: autres_changes += 1
print(f"pas retirés : {tot} ; gardant un champ CONTROLS : {reste} ; pas non visés modifiés : {autres_changes}")
# hors CONTROLS, le texte du pas retiré est-il égal au texte du jumeau privé de ses champs ?
print("clé exemple retirer :", {f: c2[ex][f] for f in c2[ex] if f not in ("modifications",)})
print("modification exemple :", c2[ex]["modifications"][0] if c2[ex].get("modifications") else None)
f1 = jl(f"{S}/gen1/items-formation-v1.jsonl"); f2 = jl(f"{S}/gen2/items-formation-v2.jsonl")
cf2 = jl(f"{S}/gen2/cle-formation-v2.jsonl")
print("formation : items différents v1/v2 :", sum(1 for a, b in zip(f1, f2) if a != b), "types :", collections.Counter((c.get("version"), c.get("type")) for c in cf2))
