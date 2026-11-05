"""Q3 : compare deux sorties du script v3, champ par champ (hors commit, état git, environnement).
Usage : python3 -I -B comparer_sorties.py AUTEUR.json MIENNE.json [--graine-neuve] > rapport.json
Même graine : liste des différences (attendu : aucune). Graine neuve : écarts sur les parts et les n₈₀.
"""
import json
import sys

IGNORES = {"commit", "etat_du_script", "environnement"}


def aplatir(x, pre=""):
    if isinstance(x, dict):
        for k, v in x.items():
            if pre == "" and k in IGNORES:
                continue
            yield from aplatir(v, f"{pre}/{k}")
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from aplatir(v, f"{pre}[{i}]")
    else:
        yield pre, x


def main():
    a = dict(aplatir(json.load(open(sys.argv[1]))))
    b = dict(aplatir(json.load(open(sys.argv[2]))))
    neuve = "--graine-neuve" in sys.argv
    res = {"champs_auteur": len(a), "champs_miens": len(b), "seulement_auteur": sorted(set(a) - set(b))[:20],
           "seulement_miens": sorted(set(b) - set(a))[:20]}
    diff = [(k, a[k], b[k]) for k in sorted(set(a) & set(b)) if a[k] != b[k]]
    if not neuve:
        res["differences"] = len(diff)
        res["exemples"] = diff[:20]
    else:
        parts = [(k, x, y) for k, x, y in diff if k.endswith("/part") or k.endswith("_part")]
        ecarts = [abs(x - y) for k, x, y in parts if isinstance(x, (int, float)) and isinstance(y, (int, float))]
        res["parts_differentes"] = len(parts)
        res["ecart_max_parts"] = max(ecarts) if ecarts else 0.0
        res["pire_part"] = max(parts, key=lambda t: abs(t[1] - t[2])) if parts else None
        front = [(k, x, y) for k, x, y in diff if k.endswith("frontiere_part") or k.endswith("tricheur_part")]
        res["max_frontiere_neuve"] = {s: max([y for k, x, y in front if f"/{s}/frontiere_part" in k] or [0])
                                      for s in ("160.0", "20.0")}
        res["max_tricheur_neuve"] = max([y for k, x, y in front if "tricheur" in k] or [0])
        n80a = {k: v for k, v in a.items() if k.endswith("/n_approx")}
        n80b = {k: v for k, v in b.items() if k.endswith("/n_approx")}
        rel = []
        hors = 0
        for k in n80a:
            x, y = n80a[k], n80b.get(k)
            if x and y:
                rel.append((abs(x - y) / x, k, x, y))
                pas = a[k.replace("/n_approx", "/pas_de_la_dichotomie[0]")], a[k.replace("/n_approx", "/pas_de_la_dichotomie[1]")]
                if not (pas[0] <= y <= pas[1]):
                    hors += 1
        rel.sort(reverse=True)
        res["n80_compares"] = len(rel)
        res["n80_differents"] = sum(r[0] > 0 for r in rel)
        res["n80_hors_du_pas_auteur"] = hors
        res["n80_ecart_relatif_max"] = rel[0] if rel else None
        res["n80_cinq_pires"] = rel[:5]
    json.dump(res, sys.stdout, indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
