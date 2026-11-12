"""e-BH pondéré avec une e-valeur NaN : familles énumérées où une fiche FINIE est retenue alors que la même famille,
la fiche NaN remplacée par −∞, ne la retient pas. Usage : python -I -B ebh_nan.py RACINE"""
import itertools, sys
sys.path.insert(0, sys.argv[1])
from pole import pari_apparie as pa
nan = float("nan")
grille = [0.0, 1.5, 2.3, 3.0, 3.7, 4.4]
total = touchees = 0
exemple = None
for k in range(2, 6):
    for vals in itertools.product(grille, repeat=k):
        for pos in range(k + 1):
            avec = list(vals[:pos]) + [nan] + list(vals[pos:])
            noms = [f"f{i}" for i in range(len(avec))]
            b = {n: 0.05 / len(avec) for n in noms}
            r1 = pa.ebh_pondere(dict(zip(noms, avec)), b, 0.05)
            r0 = pa.ebh_pondere({n: (x if x == x else -1e9) for n, x in zip(noms, avec)}, b, 0.05)
            finies_en_trop = (r1 - r0) - {noms[pos]}
            total += 1
            if finies_en_trop:
                touchees += 1
                exemple = exemple or ([("NaN" if x != x else x) for x in avec], sorted(r1), sorted(r0))
print(f"familles énumérées : {total} ; familles où une fiche finie est retenue à tort à cause du NaN : {touchees}")
print("exemple :", exemple)
