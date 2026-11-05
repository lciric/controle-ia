"""Contrôle du tableau d'atteignabilité du brouillon v8 : (1) lignes du texte = lignes du tableau versé ; (2) comptes de
chaque case recalculés depuis le détail (386 analyses) ; (3) comptes R3, issues atteintes."""
import json, re, collections
T = open("prereg/brouillon-test-echelle-conscience-eval-v8.md", encoding="utf-8").read().splitlines()
M = open("docs/notes/echelle-conscience-eval/v7/simulation-tableau/tableau-atteignabilite-v7.md", encoding="utf-8").read().splitlines()
lt = [l for l in T if l.startswith("| ") and (" | " in l) and ("tau" in l or l.count("|") == 5)]
deb = T.index("| vérité (α au 8B et au 70B) | tau 0,15 | tau 0,4 | tau 0,8 |")
rows_t = []
for l in T[deb:]:
    if not l.startswith("|"): break
    rows_t.append(l)
rows_m = [l for l in M if l.startswith("|")]
print("lignes texte", len(rows_t), "lignes tableau versé", len(rows_m), "identiques :", rows_t == rows_m)
for a, b in zip(rows_t, rows_m):
    if a != b: print("DIFF\n T:", a, "\n M:", b)
S = json.load(open("docs/notes/echelle-conscience-eval/v7/atteignabilite-echelle-v7.json"))
c = collections.defaultdict(collections.Counter)
for e in S["detail"]:
    n = len(e["reserves"])
    c[e["cas"]][e["lecture"] + (f" ({n} réserve(s))" if n else "")] += 1
ok = all(dict(c[k]) == v for k, v in S["comptes"].items()) and set(c) == set(S["comptes"])
print("comptes recalculés = comptes de la sortie :", ok, "; analyses :", len(S["detail"]), "; cases :", len(S["comptes"]))
# R3 : aucune lecture positif/inverse sous les cas H_0, sans fuite, signature d'un seul jeu, croisées
pos_inv = collections.Counter()
for e in S["detail"]:
    if e["lecture"] in ("positif", "inverse"):
        pos_inv[e["cas"]] += 1
print("cas où « positif » ou « inverse » est prononcé :")
for k, v in sorted(pos_inv.items()): print("  ", v, k)
lectures = collections.Counter(re.sub(r" \(sens .*\)$", "", e["lecture"]) for e in S["detail"])
noms = set(e["lecture"] for e in S["detail"])
print("noms atteints :", len(noms)); print(sorted(noms))
