"""Sondes CL6 : double définition d'executer_ideation ; valeurs non finies dans le juge apparié et la porte PACE.
Usage : python -I -B sondes_nan.py RACINE_DE_LA_COPIE"""
import ast, math, sys
racine = sys.argv[1]
sys.path.insert(0, racine)
src = open(f"{racine}/pole/ideation.py", encoding="utf-8").read()
defs = [n.lineno for n in ast.walk(ast.parse(src)) if isinstance(n, ast.FunctionDef) and n.name == "executer_ideation"]
from pole import ideation as idn
print("1. executer_ideation défini aux lignes", defs, "; actif :", idn.executer_ideation.__code__.co_firstlineno)
# corps de la première définition : noms libres non définis
arbre = ast.parse(src)
premiere = [n for n in arbre.body if isinstance(n, ast.FunctionDef) and n.name == "executer_ideation"][0]
params = {a.arg for a in premiere.args.args + premiere.args.kwonlyargs}
libres = sorted({n.id for n in ast.walk(premiere) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)} - params
                - set(dir(idn)) - set(dir(__builtins__)) - {"math", "e", "m", "nom_b", "b", "cle_b", "v", "role_modele", "nom", "h", "n", "t", "_", "passes", "somme_claude", "somme_externe", "liste", "question_lue", "pieces_lues", "materiau_lu", "pieces_juge_lues", "temoins_lus", "tous_proposeurs", "tous_juges", "att", "reel", "a"})
print("   première définition : noms non définis dans sa portée :", libres)
print("   dernière instruction de la première définition :", type(premiere.body[-1]).__name__, "ligne", premiere.body[-1].lineno)

from pole import pari_apparie as pa
nan, inf = float("nan"), float("inf")
print("2. pari_apparie")
for c in (nan, inf, -inf):
    try:
        pa.verifier_coefficients({"x": 0.5}, c); print(f"   verifier_coefficients(constante={c}) : ACCEPTÉ")
    except pa.ContrasteInvalide as e:
        print(f"   verifier_coefficients(constante={c}) : refusé ({e})")
print("   contraste(parts x=0, coef x=0,5, constante=NaN) =", pa.contraste({"x": 0.0}, {"x": 0.5}, nan))
print("   contraste(parts x=0,2, coef x=NaN, constante=0) =", pa.contraste({"x": 0.2}, {"x": nan}, 0.0))
print("   contraste(parts x=0,2, coef x=inf, constante=0) =", pa.contraste({"x": 0.2}, {"x": inf}, 0.0))
try:
    print("   contraste_plafonne(constante NaN) =", pa.contraste_plafonne({"x": 0.0}, {"x": 0.5}, nan, 3, 3))
except Exception as e:
    print("   contraste_plafonne : erreur", e)
# richesse avec v = +1 partout (ce que rend une constante NaN) : promotion ?
v = [pa.contraste({"x": 0.0}, {"x": 0.5}, nan)] * 12
r = pa.evaluer({"k": v}, alpha=0.05, m=1)
print("   evaluer(12 unités à v = contraste(constante NaN)) : promue =", r["promue"], "à l'instant", r["instant_d_arret"])
for nom, vals in (("NaN", [0.1, nan, 0.1]), ("+inf", [0.1, inf, 0.1]), ("5,0 (hors [-1;1])", [0.1, 5.0, 0.1])):
    try:
        t = pa.trajectoire_log_sans_remise(vals); print(f"   trajectoire_log_sans_remise avec {nom} : ACCEPTÉ, rend {[round(x, 3) if math.isfinite(x) else x for x in t]}")
    except Exception as e:
        print(f"   trajectoire_log_sans_remise avec {nom} : refusé ({type(e).__name__})")
for nom, vals in (("NaN", [0.1, nan]), ("5,0", [0.1, 5.0])):
    try:
        print(f"   borne_basse avec {nom} : ACCEPTÉ, rend", pa.borne_basse(vals * 30))
    except Exception as e:
        print(f"   borne_basse avec {nom} : refusé ({type(e).__name__})")
for nom, a in (("NaN", nan), ("inf", inf)):
    try:
        r = pa.evaluer({"k": [0.5] * 30}, alpha=a, m=1); print(f"   evaluer(alpha={nom}) : ACCEPTÉ, seuil_log={r['seuil_log']}, promue={r['promue']}")
    except Exception as e:
        print(f"   evaluer(alpha={nom}) : refusé ({type(e).__name__}: {e})")
try:
    r = pa.evaluer({"k": [0.5] * 30}, alpha=0.05, m=nan); print(f"   evaluer(m=NaN) : ACCEPTÉ, seuil_log={r['seuil_log']}, promue={r['promue']}")
except Exception as e:
    print(f"   evaluer(m=NaN) : refusé ({type(e).__name__})")
# ebh_pondere avec une e-valeur NaN ou +inf
for nom, x in (("NaN", nan), ("+inf", inf)):
    try:
        out = pa.ebh_pondere({"a": 1.0, "b": x, "c": 0.5}, {"a": 0.01, "b": 0.01, "c": 0.01}, 0.05)
        print(f"   ebh_pondere(log_e de b = {nom}) : ACCEPTÉ, retenues {sorted(out)}")
    except Exception as e:
        print(f"   ebh_pondere(log_e de b = {nom}) : refusé ({type(e).__name__})")
# NaN peut-il déranger l'ordre e-BH et promouvoir à tort ? recherche exhaustive sur de petites familles
import itertools
pires = 0
grille = [0.0, 1.5, 2.3, 3.0, 3.7, 4.4]
for k in range(2, 6):
    for vals in itertools.product(grille, repeat=k):
        for pos in range(k + 1):
            avec = list(vals[:pos]) + [nan] + list(vals[pos:])
            noms = [f"f{i}" for i in range(len(avec))]
            b = {n: 0.05 / len(avec) for n in noms}
            sans_nan = {n: (x if x == x else -1e9) for n, x in zip(noms, avec)}
            r1 = pa.ebh_pondere(dict(zip(noms, avec)), b, 0.05)
            r0 = pa.ebh_pondere(sans_nan, b, 0.05)
            if r1 - r0:
                pires += 1
                if pires <= 3:
                    print("   e-BH dérangé par NaN :", [round(x, 2) if x == x else "NaN" for x in avec], "retenues", sorted(r1), "au lieu de", sorted(r0))
print("   familles où un NaN fait retenir une fiche que la même famille (NaN → −∞) ne retient pas :", pires)
# Course : trajectoire avec NaN ou +inf
c = pa.Course(alpha=0.05, essai=True)
c.entrer("fam", ["a", "b"], 0.05)
c.ajouter_trajectoire("a", [0.5, inf], sans_identite=True)
c.ajouter_trajectoire("b", [0.5, nan, 0.2], sans_identite=True)
print("   Course.ajouter_trajectoire(+inf) : log_e(a) =", c.log_e["a"], "; (NaN au milieu) log_e(b) =", c.log_e["b"])
print("   Course.lire() → promues :", sorted(c.lire()))
from pole import porte_pace as pp
print("3. porte_pace")
for nom, kw in (("gain_reel NaN", {"gain_reel": nan}), ("delta NaN avec écarts", {"ecarts_faux_positifs": [0.0] * 40, "delta": nan})):
    s = pp.simuler_suite(__import__("random").Random(1), "gain", m=2, n_dev=40)
    s[0].update(kw)
    try:
        pp.comparer(s); print(f"   comparer({nom}) : ACCEPTÉ")
    except Exception as e:
        print(f"   comparer({nom}) : refusé ({type(e).__name__}: {str(e)[:80]})")
