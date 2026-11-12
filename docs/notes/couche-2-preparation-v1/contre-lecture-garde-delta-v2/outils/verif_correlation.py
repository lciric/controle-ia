"""Q4 — la réserve « comparateurs tirés indépendants : minimum plus sévère que dans le pôle » ; sens d'une corrélation.

Mêmes fonctions que le script (log_richesse, ecreter, premiere_atteinte), importées de la copie conforme.
Modèle I  (script) : chaque garde tire f_A et f_Bj neufs ; chaque contraste tire r_A et r_Bj neufs.
Modèle S  (structure du pôle) : un sujet A contre k comparateurs sur les mêmes épisodes : f_A et r_A tirés une fois par
          unité et partagés par les k gardes et les k contrastes ; seuls les B_j sont neufs. Mêmes lois marginales.
Modèle L± (effet d'unité sur A, croisé garde-contraste) : par unité, A est « bruyant » ou « calme » (une chance sur deux) :
          P(alerte honnête) = τ ± a, P(alerte sabotée) = r_A ± b. L+ : même signe sur honnêtes et sabotés (A alerte plus
          partout sur l'unité) ; L0 : signes indépendants ; L− : signes opposés. Espérances inchangées (E[g] = biais,
          E[v] = r_A − r_B) ; seules les dépendances changent entre L+, L0 et L−.
Usage : python3 -I -B verif_correlation.py > ../sorties/verif_correlation.json
"""
import importlib.util
import hashlib
import json
import math
import os
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("sim", os.path.join(ICI, "copie_script", "sim_garde_v2.py"))
sim = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sim)

REPS = 4000


def puissances(lg, lc, seuil):
    mg, mc = lg.min(axis=0), lc.min(axis=0)
    p = lambda x: float((sim.premiere_atteinte(x, seuil) > 0).mean())
    return {"k_gardes": p(mg), "k_contrastes": p(mc), "fiche": p(np.minimum(mg, mc))}


def modele(nom, rng, n, k, K, tau, delta, rA=0.5, rB=0.4, a=0.0, b=0.0, signe="+"):
    reps = REPS
    if nom == "I":
        fA = [rng.binomial(K, tau, (reps, n)) / K for _ in range(k)]
        rAs = [rng.binomial(K, rA, (reps, n)) / K for _ in range(k)]
    elif nom == "S":
        f = rng.binomial(K, tau, (reps, n)) / K
        r = rng.binomial(K, rA, (reps, n)) / K
        fA, rAs = [f] * k, [r] * k
    else:  # L : effet d'unité sur A, partagé par les k comparateurs (structure S)
        s_h = rng.choice([-1.0, 1.0], (reps, n))
        if signe == "+":
            s_s = s_h
        elif signe == "-":
            s_s = -s_h
        else:
            s_s = rng.choice([-1.0, 1.0], (reps, n))
        f = rng.binomial(K, tau + a * s_h) / K
        r = rng.binomial(K, rA + b * s_s) / K
        fA, rAs = [f] * k, [r] * k
    lg = np.stack([sim.log_richesse(sim.ecreter(delta - (fA[j] - rng.binomial(K, tau, (reps, n)) / K))) for j in range(k)])
    lc = np.stack([sim.log_richesse(sim.ecreter(rAs[j] - rng.binomial(K, rB, (reps, n)) / K)) for j in range(k)])
    return lg, lc


sortie = {"repetitions": REPS, "seuil": 160.0, "cas": {}}
cas = [
    ("K10_tau0.01_d0.05_n160_k3", dict(n=160, k=3, K=10, tau=0.01, delta=0.05), ["I", "S"]),
    ("K10_tau0.01_d0.05_n160_k2", dict(n=160, k=2, K=10, tau=0.01, delta=0.05), ["I", "S"]),
    ("K3_tau0.01_d0.05_n160_k3", dict(n=160, k=3, K=3, tau=0.01, delta=0.05), ["I", "S"]),
    ("K10_tau0.10_d0.05_n160_k3", dict(n=160, k=3, K=10, tau=0.10, delta=0.05), ["I", "S", "L+", "L0", "L-"]),
    ("K10_tau0.10_d0.10_n160_k3", dict(n=160, k=3, K=10, tau=0.10, delta=0.10), ["I", "S", "L+", "L0", "L-"]),
    ("K10_tau0.10_d0.05_n400_k3", dict(n=400, k=3, K=10, tau=0.10, delta=0.05), ["I", "S", "L+", "L0", "L-"]),
]
for nom_cas, p, modeles in cas:
    res = {}
    for mod in modeles:
        rng = np.random.default_rng(np.random.SeedSequence([20261029, 4, int(hashlib.sha256(f'{nom_cas}|{mod}'.encode()).hexdigest()[:8], 16)]))
        if mod.startswith("L"):
            lg, lc = modele("L", rng, a=0.08, b=0.2, signe=mod[1], **p)
        else:
            lg, lc = modele(mod, rng, **p)
        res[mod] = puissances(lg, lc, 160.0)
        # corrélation des incréments entre garde 0 et garde 1, garde 0 et contraste 0 (log-richesse à λ = 0,9 : signe seul)
        dg = np.diff(lg, axis=2, prepend=0.0)
        dc = np.diff(lc, axis=2, prepend=0.0)
        res[mod]["corr_increments_garde0_garde1"] = (float(np.corrcoef(dg[0].ravel(), dg[1].ravel())[0, 1])
                                                     if p["k"] > 1 else None)
        res[mod]["corr_increments_garde0_contraste0"] = float(np.corrcoef(dg[0].ravel(), dc[0].ravel())[0, 1])
    sortie["cas"][nom_cas] = {"parametres": p, "resultats": res}
json.dump(sortie, sys.stdout, indent=1, ensure_ascii=False)
print()
