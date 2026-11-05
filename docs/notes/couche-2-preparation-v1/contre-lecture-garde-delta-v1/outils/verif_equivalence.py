"""Contre-lecture de la garde δ : équivalence script ↔ pôle v40, plancher analytique, non finis, seuil dans `evaluer`.

Lancement : python3 -B verif_equivalence.py  (depuis n'importe où ; chemins relatifs à ce fichier).
Copies : copie_script/sim_garde.py (script conv-audit, sha256 37c3dc7a…), copie_pole/pari_apparie.py (v40, 56bc8e03…).
"""
import ast
import json
import math
import os
import sys
import warnings
from fractions import Fraction

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ICI, "copie_pole"))
sys.path.insert(0, os.path.join(ICI, "copie_script"))
import pari_apparie as pa  # noqa: E402
import sim_garde as sg  # noqa: E402

sortie = {}

# ------------------------------------------------------------------ 1. équivalence des trajectoires
rng = np.random.default_rng(np.random.SeedSequence([20261029, 1]))
cas = {
    "binomiale_K10_tau0.01": lambda n: rng.binomial(10, 0.01, n) / 10 - rng.binomial(10, 0.01, n) / 10,
    "binomiale_K10_tau0.10": lambda n: rng.binomial(10, 0.10, n) / 10 - rng.binomial(10, 0.10, n) / 10,
    "uniforme_-1_1": lambda n: rng.uniform(-1, 1, n),
    "extremes_pm1": lambda n: rng.choice([-1.0, 1.0], n),
}
equiv = {}
for nom, tirer in cas.items():
    for delta in (0.05, 0.10):
        ecarts_max, croisements_differents, n_ecrete = 0.0, 0, 0
        for rep in range(200):
            g = tirer(160)
            a = sg.log_richesse((delta - g)[None, :])[0]
            b = np.array(pa.trajectoire_log_garde([float(x) for x in g], delta))
            ecarts_max = max(ecarts_max, float(np.max(np.abs(a - b))))
            n_ecrete += int(np.sum((delta - g) > 1))
            for s in (20.0, 160.0):
                ia = np.argmax(a >= math.log(s)) if (a >= math.log(s)).any() else -1
                ib = np.argmax(b >= math.log(s)) if (b >= math.log(s)).any() else -1
                croisements_differents += int(ia != ib)
        equiv[f"{nom}|delta={delta}"] = {"ecart_max_log_richesse": ecarts_max, "unites_ecretees_par_le_pole": n_ecrete,
                                          "croisements_differents_sur_400": croisements_differents}
sortie["1_equivalence_trajectoires"] = equiv

# cas limite : g = -1 partout (A n'a aucun faux positif, B en a partout) ; v = δ + 1 > 1 : le pôle écrête à 1
g = [-1.0] * 6
sortie["1b_ecretage_g_moins_1"] = {
    "script": sg.log_richesse(np.array([[0.05 - x for x in g]]))[0].round(4).tolist(),
    "pole": [round(x, 4) for x in pa.trajectoire_log_garde(g, 0.05)]}

# cas limite : g > 1 + 1/λmax - δ (impossible pour des fractions, possible après recentrage + biais) : NaN dans le script
with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    lw = sg.log_richesse(np.array([[0.05 - 2.0, 0.05, 0.05]]))[0]
    sortie["1c_g_egal_2"] = {"script_log_richesse": [None if not np.isfinite(x) else float(x) for x in lw],
                             "script_avertissements": [str(x.message) for x in w],
                             "script_refuse": False}
try:
    sortie["1c_g_egal_2"]["pole"] = [round(x, 4) for x in pa.trajectoire_log_garde([2.0, 0.0, 0.0], 0.05)]
except Exception as e:  # noqa: BLE001
    sortie["1c_g_egal_2"]["pole"] = f"refus : {type(e).__name__}: {e}"

# ------------------------------------------------------------------ 2. non finis et booléens
nf = {}
for val in (float("nan"), float("inf"), -float("inf"), True):
    r = {}
    try:
        sg.log_richesse(np.array([[0.05 - float(val)]]))
        r["script_log_richesse"] = "accepté"
    except Exception as e:  # noqa: BLE001
        r["script_log_richesse"] = f"refus {type(e).__name__}"
    try:
        pa.trajectoire_log_garde([val], 0.05)
        r["pole"] = "accepté"
    except Exception as e:  # noqa: BLE001
        r["pole"] = f"refus {type(e).__name__}"
    nf[repr(val)] = r
sortie["2_non_finis"] = nf

# ------------------------------------------------------------------ 3. plancher structurel exact (fractions)
def plancher_exact(delta, seuil):
    lam = [Fraction(1, 10), Fraction(3, 10), Fraction(6, 10), Fraction(9, 10)]
    d = Fraction(delta).limit_denominator(10000)
    n = 1
    while sum((1 + l * d) ** n for l in lam) / 4 < seuil:
        n += 1
    return n


pl = {}
for delta in (0.05, 0.10):
    for s in (20, 160):
        n = plancher_exact(delta, s)
        moy = lambda k: float(np.mean((1 + sg.LAMBDAS * delta) ** k))  # noqa: E731
        pl[f"delta={delta}|seuil={s}"] = {"exact": n, "script": sg.unites_minimales_garde(delta, s),
                                          "richesse_a_n_moins_1": round(moy(n - 1), 4), "richesse_a_n": round(moy(n), 4),
                                          "lambda_0.9_seul": math.ceil(math.log(4 * s) / math.log(1 + 0.9 * delta))}
sortie["3_plancher"] = pl

# ------------------------------------------------------------------ 4. la garde dans `evaluer` : seuil commun log(m/α)
contrastes = {"base_ii": [0.5] * 64, "base_iii": [0.5] * 64}  # contrastes très favorables : ils franchissent tôt
g0 = [0.0] * 64
ev = {}
for m in (1, 8):
    for delta in (0.05, 0.10):
        r = pa.evaluer(contrastes, ecarts_faux_positifs=g0, delta=delta, alpha=0.05, m=m)
        ev[f"m={m}|delta={delta}"] = {"seuil": round(math.exp(r["seuil_log"]), 3), "promue": r["promue"],
                                      "instant_d_arret": r["instant_d_arret"],
                                      "e_valeur": round(math.exp(r["log_e_valeur"]), 3),
                                      "garde_finale": round(math.exp(r["log_garde_finale"]), 3)}
sortie["4_evaluer_seuil_commun"] = ev

# 4b : e-BH du pôle (cycle.appliquer_multiplicite) : retenue à m/(α·k*) sur l'e-valeur arrêtée à m/α
src = open(os.path.join(ICI, "copie_pole", "cycle.py"), encoding="utf-8").read()
arbre = ast.parse(src)
fn = next(n for n in arbre.body if isinstance(n, ast.FunctionDef) and n.name == "appliquer_multiplicite")
espace = {"math": math}
exec(compile(ast.Module(body=[fn], type_ignores=[]), "appliquer_multiplicite", "exec"), espace)  # noqa: S102


def issue(traj):
    return {"pari": {"trajectoire_log_w": traj}, "verdict_final": "survit"}


ebh = {}
for k_vraies in (1, 8):
    # m = 8 fiches ; k_vraies fiches dont le minimum (garde δ = 0,10, 64 unités, g = 0) finit à ≈ 101 (entre 20 et 160)
    traj_garde = [r for r in pa.trajectoire_log_garde([0.0] * 64, 0.10)]
    issues = {f"f{i}": issue(traj_garde if i < k_vraies else [0.0] * 64) for i in range(8)}
    r = espace["appliquer_multiplicite"](issues, 0.05, m_fixe=8)
    ebh[f"{k_vraies}_fiche(s)_a_garde_finale_{round(math.exp(traj_garde[-1]), 1)}"] = {"retenues": len(r["retenues"])}
sortie["4b_ebh_retenue"] = ebh

print(json.dumps(sortie, indent=1, ensure_ascii=False))
