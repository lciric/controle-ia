#!/usr/bin/env python3
"""Résumé du rejeu du banc de cl7 avec l'analyse v8 (lignée « session-depot », 27 octobre 2026 ; CLT-01). Lit les
sorties du rejeu (une ligne par analyse, la première est l'en-tête) et compte :
  - les intervalles de λ identiques à ceux du banc (écart maximal à l'arrondi) ;
  - les lectures v7 (consignées par le banc) et v8, au nom du désaccord près ;
  - les lectures fausses : « positif » ou « inverse » sous une vérité H_0, « nul » sous une vérité H_A (d'après le nom
    du scénario du banc), et celles qui portent une réserve de la v8 ;
  - les réserves de la v8 sur les autres lectures prononcées (témoins compris).
    python -I -B resumer_rejeu_cl7_v8.py REJEU_JSONL [REJEU_JSONL …]"""
import collections
import json
import sys

R1, R2 = "le λ du ", "jeux de force de contexte inégale"
lignes = []
for f in sys.argv[1:]:
    for l in open(f, encoding="utf-8"):
        d = json.loads(l)
        if "entete" in d:
            print(f"{f.rsplit('/', 1)[-1]} : en-tête {json.dumps(d['entete'], ensure_ascii=False)}")
        else:
            lignes.append(d)
print(f"analyses rejouées : {len(lignes)} ; arrêts : {sum(1 for d in lignes if 'code' in d)}")
ok = [d for d in lignes if "code" not in d]
print(f"écart maximal des intervalles de λ au banc : {max(d['ecart_max_lambda_ic_au_banc'] for d in ok)}")
chg = collections.Counter()
for d in ok:
    a, b = d["lecture_v7"], d["lecture"]
    if a != b:
        chg[(a, b)] += 1
print("lectures changées (v7 → v8) :", {f"{a} → {b}": n for (a, b), n in chg.items()} or "aucune")


def faux(d):
    """Vérité H_0 (« H0 » dans le nom du scénario) lue « positif » ou « inverse » ; vérité H_A (« HA ») lue « nul »."""
    s, l = d["scenario"], d["lecture"]
    return ("H0" in s and l in ("positif", "inverse")) or ("HA" in s and l == "nul")


r1 = lambda d: any(r.startswith(R1) for r in d["reserves"])
r2 = lambda d: any(r.startswith(R2) for r in d["reserves"])
f = [d for d in ok if faux(d)]
print(f"lectures fausses (« positif » ou « inverse » sous H_0 ; « nul » sous H_A) : {len(f)} ; "
      f"avec « λ change » : {sum(r1(d) for d in f)} ; avec « contexte inégal » : {sum(r2(d) for d in f)} ; "
      f"avec l'une ou l'autre : {sum(r1(d) or r2(d) for d in f)} ; sans : {sum(not (r1(d) or r2(d)) for d in f)}")
for d in f:
    print(f"  {d['scenario']} {d['graine']} n_boot {d['n_boot']} : {d['lecture']} ; λ change {r1(d)} ; contexte inégal "
          f"{r2(d)} ; e {d['ecart_sens']} {d['ecart_sens_ic']} ; q {d['rapport_Ec']}")
autres = [d for d in ok if not faux(d) and d["lecture"] in ("positif", "inverse", "nul")]
print(f"autres lectures prononcées « positif », « inverse », « nul » : {len(autres)} ; avec une réserve v8 : "
      f"{sum(r1(d) or r2(d) for d in autres)}")
for d in autres:
    if r1(d) or r2(d):
        print(f"  {d['scenario']} {d['graine']} : {d['lecture']} ; λ change {r1(d)} ; contexte inégal {r2(d)} ; "
              f"q {d['rapport_Ec']}")
