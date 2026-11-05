"""Q3a : l'espérance de l'effet d'unité en logit est-elle tenue ? Vérification indépendante de la quadrature du script.
(1) intégration numérique fine (trapèzes, 400 001 points sur [-12 ; 12]) de sigmoïde(logit p0 + c + σx) φ(x) ;
(2) Monte-Carlo indépendant (graine propre, 10⁷ tirages, erreur type) ;
(3) Monte-Carlo de bout en bout par LoiSynthetique.tirer (fa, rA) ;
(4) constante c (bornes de la dichotomie ±20 atteintes ?), écart-type de p ajouté contre écart-type binomial."""
import importlib.util, json, math, sys
import numpy as np
C = "/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/relecture-garde-delta-v4/cl"
spec = importlib.util.spec_from_file_location("sim4", f"{C}/outils/copie_script/sim_garde_v4.py")
sim = importlib.util.module_from_spec(spec); spec.loader.exec_module(sim)

def c_du_script(p0, s):
    # retrouve c à partir de la sortie du script en u = 0
    p = float(sim.proba_decalee(p0, s, np.array([0.0]))[0])
    return math.log(p / (1 - p)) - math.log(p0 / (1 - p0))

x = np.linspace(-12, 12, 400_001); phi = np.exp(-x * x / 2) / math.sqrt(2 * math.pi)
def esp_trap(p0, s):
    c = c_du_script(p0, s)
    f = 1 / (1 + np.exp(-(math.log(p0 / (1 - p0)) + c + s * x)))
    return float(np.trapezoid(f * phi, x))

rng = np.random.default_rng(np.random.SeedSequence([314159, 2718]))
res = {"esperances": [], "bout_en_bout": [], "ecarts_types": []}
for s in [0.5, 1.0, 2.0, 3.0]:
    for p0 in [1e-4, 0.01, 0.0225, 0.035, 0.06, 0.1, 0.11, 0.2, 0.5, 0.6, 0.9, 0.99, 0.9999]:
        u = rng.standard_normal(10_000_000)
        p = sim.proba_decalee(p0, s, u)
        mc, se = float(p.mean()), float(p.std() / math.sqrt(p.size))
        c = c_du_script(p0, s)
        res["esperances"].append({"sigma": s, "p0": p0, "c": c, "c_aux_bornes": abs(c) > 19.99, "E_trapezes": esp_trap(p0, s),
                                  "ecart_trapezes": esp_trap(p0, s) - p0, "E_mc": mc, "se_mc": se, "z_mc": (mc - p0) / se,
                                  "sd_p": float(p.std())})
# bout en bout : moyenne de fa et rA tirés par la loi du script
for K, tau in [(10, 0.01), (10, 0.10), (3, 0.01), (3, 0.10)]:
    for s in [0.0, 0.5, 1.0, 3.0]:
        loi = sim.LoiSynthetique(K, K, tau, 0.4, 0.10, True, s)
        g, v = loi.tirer(rng, 20000, 160, 160, 1, 0.0)
        # g = fa - fb ; E[g] attendu 0 ; v = rA - rB, E[v] attendu 0,10
        n = g.size
        res["bout_en_bout"].append({"K": K, "tau": tau, "sigma": s, "E_g": float(g.mean()), "se_g": float(g.std() / math.sqrt(n)),
                                    "E_v": float(v.mean()), "se_v": float(v.std() / math.sqrt(n)),
                                    "sd_g": float(g.std()), "sd_v": float(v.std())})
        for b in [0.05, 0.10]:  # frontière (biais = δ) : E[g] = δ exigé
            g2, _ = loi.tirer(rng, 20000, 160, 160, 1, b)
            res["bout_en_bout"].append({"K": K, "tau": tau, "sigma": s, "biais": b, "E_g": float(g2.mean()),
                                        "se_g": float(g2.std() / math.sqrt(g2.size))})
# écart-type ajouté par l'effet (σ_p) contre écart-type binomial d'une fraction sur K épisodes
for s in [0.5, 1.0]:
    for p0, K in [(0.01, 10), (0.10, 10), (0.01, 3), (0.10, 3), (0.5, 10), (0.5, 3)]:
        u = rng.standard_normal(2_000_000)
        sdp = float(sim.proba_decalee(p0, s, u).std())
        res["ecarts_types"].append({"sigma": s, "p0": p0, "K": K, "sd_p_ajoute": sdp, "sd_binomial": math.sqrt(p0 * (1 - p0) / K),
                                    "approx_sigma_p_1_moins_p": s * p0 * (1 - p0)})
json.dump(res, open(f"{C}/sorties/verif_esperance.json", "w"), indent=1, ensure_ascii=False)
E = res["esperances"]
print("max |E_trap - p0| :", max(abs(r["ecart_trapezes"]) for r in E), "max |z_mc| :", max(abs(r["z_mc"]) for r in E),
      "c aux bornes :", [ (r["sigma"], r["p0"]) for r in E if r["c_aux_bornes"]])
for r in E:
    if abs(r["ecart_trapezes"]) > 1e-6 or abs(r["z_mc"]) > 3: print("ECART", r)
for r in res["bout_en_bout"]:
    print({k: (round(v, 5) if isinstance(v, float) else v) for k, v in r.items()})
for r in res["ecarts_types"]:
    print({k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items()})
