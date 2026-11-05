"""Compare la reproduction de la simulation d'atteignabilité v3 à la trace citée par le brouillon v4."""
import json, sys
a = json.load(open(sys.argv[1], encoding="utf-8"))
b = json.load(open(sys.argv[2], encoding="utf-8"))
for k in ("analyse_sha256", "simulation_sha256", "stimuli_sha256", "n_boot", "repetitions", "commit_scripts",
          "arbre_scripts_propre", "python", "numpy"):
    print(f"{k:22s} {'identique' if a[k] == b[k] else 'DIFFÉRENT'} ({b[k]})")
cases = sorted(set(a["comptes"]) | set(b["comptes"]))
n_ok = sum(a["comptes"].get(c) == b["comptes"].get(c) for c in cases)
print(f"cases identiques : {n_ok} sur {len(cases)}")
for c in cases:
    if a["comptes"].get(c) != b["comptes"].get(c):
        print("  écart :", c, a["comptes"].get(c), b["comptes"].get(c))
n = sum(sum(v.values()) for v in b["comptes"].values())
n0 = sum(sum(v.values()) for c, v in b["comptes"].items() if c.startswith(("H0", "pas de fuite", "signature")))
pos = sum(v.get("positif", 0) + v.get("inverse", 0) for c, v in b["comptes"].items() if c.startswith(("H0", "pas de fuite", "signature")))
print(f"analyses : {n} ; sous H0, sans fuite et signature : {n0}, dont positif ou inverse : {pos}")
