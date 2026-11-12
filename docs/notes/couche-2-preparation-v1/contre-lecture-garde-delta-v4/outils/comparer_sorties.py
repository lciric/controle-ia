"""Compare deux sorties JSON du script champ par champ (tous seuils, toutes cellules, n80 compris).
Usage : python3 -I comparer_sorties.py A.json B.json [sortie.json]. Champs ignorés : en-tête de traçabilité."""
import json, sys
IGNORE = {"version", "script_sha256", "commit", "etat_du_script", "environnement", "statut"}
def aplatir(x, p=""):
    if isinstance(x, dict):
        for k, v in x.items():
            yield from aplatir(v, f"{p}/{k}")
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from aplatir(v, f"{p}[{i}]")
    else:
        yield p, x
a, b = (json.load(open(f)) for f in sys.argv[1:3])
fa = {k: v for k, v in aplatir({k: v for k, v in a.items() if k not in IGNORE})}
fb = {k: v for k, v in aplatir({k: v for k, v in b.items() if k not in IGNORE})}
seul_a = sorted(set(fa) - set(fb)); seul_b = sorted(set(fb) - set(fa))
diffs = [(k, fa[k], fb[k]) for k in sorted(set(fa) & set(fb)) if fa[k] != fb[k]]
num = [abs(x - y) for _, x, y in diffs if isinstance(x, (int, float)) and isinstance(y, (int, float)) and not isinstance(x, bool)]
res = {"A": sys.argv[1], "B": sys.argv[2], "champs_communs": len(set(fa) & set(fb)), "seuls_A": seul_a[:50], "n_seuls_A": len(seul_a),
       "seuls_B": seul_b[:50], "n_seuls_B": len(seul_b), "n_differences": len(diffs), "ecart_max": max(num) if num else 0.0,
       "differences_non_numeriques": [d for d in diffs if not (isinstance(d[1], (int, float)) and isinstance(d[2], (int, float)))][:50],
       "plus_grandes": sorted(diffs, key=lambda d: -abs(d[1] - d[2]) if isinstance(d[1], (int, float)) and isinstance(d[2], (int, float)) else 0)[:15]}
# parts seulement (puissances) au seuil 160
parts = [(k, x, y) for k, x, y in diffs if k.endswith("/part") or k.endswith("_part")]
res["n_differences_parts"] = len(parts)
res["ecart_max_parts"] = max((abs(x - y) for _, x, y in parts), default=0.0)
s = json.dumps(res, ensure_ascii=False, indent=1)
if len(sys.argv) > 3:
    open(sys.argv[3], "w").write(s)
print(json.dumps({k: res[k] for k in ["champs_communs", "n_seuls_A", "n_seuls_B", "n_differences", "ecart_max", "n_differences_parts", "ecart_max_parts"]}, ensure_ascii=False))
print("seuls_A", seul_a[:5]); print("seuls_B", seul_b[:5]); print("non num", res["differences_non_numeriques"][:5])
