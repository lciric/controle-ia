"""Compare deux sorties JSON champ à champ (aplaties). Exclut l'en-tête de traçabilité (commit, état git, environnement,
chemin de sortie). Usage : python3 -I -B comparer_sorties.py A.json B.json SORTIE.json [--filtre SOUS_CHAINE]"""
import json
import sys

A, B, S = sys.argv[1:4]
filtre = sys.argv[5] if len(sys.argv) > 5 and sys.argv[4] == "--filtre" else None
EXCLUS = ("/commit", "/etat_du_script", "/environnement", "/reglages/sortie")


def aplatir(x, p="", out=None):
    out = {} if out is None else out
    if isinstance(x, dict):
        for k, v in x.items():
            aplatir(v, f"{p}/{k}", out)
    elif isinstance(x, list):
        for i, v in enumerate(x):
            aplatir(v, f"{p}/{i}", out)
    else:
        out[p] = x
    return out


a, b = aplatir(json.load(open(A))), aplatir(json.load(open(B)))
garde = lambda k: not any(k.startswith(e) for e in EXCLUS) and (filtre is None or filtre in k)
ka, kb = {k for k in a if garde(k)}, {k for k in b if garde(k)}
communs = sorted(ka & kb)
diffs = [(k, a[k], b[k]) for k in communs if a[k] != b[k]]
num = [abs(x - y) for _, x, y in diffs if isinstance(x, (int, float)) and isinstance(y, (int, float)) and not isinstance(x, bool)]
res = {"a": A, "b": B, "filtre": filtre, "champs_communs": len(communs), "differences": len(diffs),
       "ecart_max": max(num) if num else 0.0, "seulement_a": sorted(ka - kb)[:20], "nb_seulement_a": len(ka - kb),
       "seulement_b": sorted(kb - ka)[:20], "nb_seulement_b": len(kb - ka),
       "exemples": [{"champ": k, "a": x, "b": y} for k, x, y in sorted(diffs, key=lambda d: -abs(d[1] - d[2]) if isinstance(d[1], (int, float)) and isinstance(d[2], (int, float)) else 0)[:15]]}
json.dump(res, open(S, "x"), indent=1, ensure_ascii=False)
print(json.dumps({k: v for k, v in res.items() if k not in ("exemples",)}, ensure_ascii=False)[:1500])
print(json.dumps(res["exemples"][:6], ensure_ascii=False)[:1500])
