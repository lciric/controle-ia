"""Puissance de la fiche quand plusieurs gardes (une par comparateur, K9-9) entrent dans le minimum de `evaluer`.
Lancement : python3 -B verif_gardes_multiples.py ; loi binomiale K = 10, τ = 0,01 (celle du script), 4 000 répétitions.
Gardes indépendantes (cas favorable : des comparateurs différents) ; contrastes supposés franchir tôt (non limitants)."""
import json, math, os, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "copie_script"))
import sim_garde as sg
out = {}
for delta, n, s in ((0.05, 160, 160.0), (0.05, 160, 20.0), (0.10, 64, 20.0), (0.10, 64, 160.0), (0.10, 93, 160.0)):
    for k in (1, 2, 3):
        rng = sg.rng_de(777, "multi", delta, n, s, k)
        lws = [sg.log_richesse(delta - sg.tirage_binomial(rng, 4000, n, 10, 0.01, 0.0)) for _ in range(k)]
        mn = np.minimum.reduce(lws)
        out[f"delta={delta}|n={n}|seuil={int(s)}|gardes={k}"] = round(float((mn >= math.log(s)).any(axis=1).mean()), 4)
print(json.dumps(out, indent=1))
