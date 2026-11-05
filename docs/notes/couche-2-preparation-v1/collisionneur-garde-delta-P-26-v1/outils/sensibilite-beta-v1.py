"""Sensibilité « surdispersion bêta » pour la synthèse P-26 (session-depot, sous-agent de synthèse) — v1.

Réutilise les fonctions de la copie du script v4 (empreinte 5bf015b6…, non modifiée) : log_richesse, processus, cellule,
n_pour_puissance, rng_de. Seule la loi change : la probabilité d'alerte honnête de A par unité suit une loi bêta
d'espérance τ + biais et de corrélation intra-unité ρ (α = μ(1−ρ)/ρ, β = (1−μ)(1−ρ)/ρ), commune aux k comparateurs
(sujet partagé) ; côté sabotés de A, même ρ autour de r_B + écart (variante « B » de la contre-lecture v4, GD4-01, ρ = 0,17
à dispersion égale des deux côtés). Option --bj-beta : les B_j reçoivent aussi une bêta de même ρ (variante plus dure,
non simulée dans les pièces). Exploratoire, processeur seul, non opposable.

Usage : python3 -I -B sensibilite-beta-v1.py --graine G --rho R [--bj-beta] > sortie.json
"""
import argparse
import importlib.util
import json
import os
import platform
import sys
import time

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
CHEMIN_V4 = os.path.join(ICI, "script-v4-copie", "simulation-puissance-garde-delta-v4.py")
spec = importlib.util.spec_from_file_location("simv4", CHEMIN_V4)
simv4 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(simv4)


def beta_p(rng, mu, rho, forme):
    mu = min(max(mu, 1e-9), 1 - 1e-9)
    if rho <= 0:
        return np.full(forme, mu)
    a = mu * (1 - rho) / rho
    b = (1 - mu) * (1 - rho) / rho
    return rng.beta(a, b, size=forme)


class LoiBeta(simv4.LoiSynthetique):
    def __init__(self, K_h, K_s, taux, r_b, ecart, rho, bj_beta):
        super().__init__(K_h, K_s, taux, r_b, ecart, True, 0.0)
        self.rho, self.bj_beta = rho, bj_beta

    def nom(self):
        return f"beta_rho{self.rho}_Kh{self.K_h}_taux{self.taux}" + ("_Bj_beta" if self.bj_beta else "")

    def tirer(self, rng, reps, n, n_garde, k, biais, biais_contraste=0.0):
        pa = beta_p(rng, self.taux + biais, self.rho, (reps, 1, n_garde))
        fa = rng.binomial(self.K_h, pa) / self.K_h
        ra = beta_p(rng, self.r_b + self.ecart + biais_contraste, self.rho, (reps, 1, n))
        rA = rng.binomial(self.K_s, ra) / self.K_s
        if self.bj_beta:
            fb = rng.binomial(self.K_h, beta_p(rng, self.taux, self.rho, (reps, k, n_garde))) / self.K_h
        else:
            fb = rng.binomial(self.K_h, self.taux, size=(reps, k, n_garde)) / self.K_h
        rB = rng.binomial(self.K_s, self.r_b, size=(reps, k, n)) / self.K_s
        return fa - fb, rA - rB


def principal():
    p = argparse.ArgumentParser()
    p.add_argument("--graine", type=int, required=True)
    p.add_argument("--rho", default="0.05,0.17")
    p.add_argument("--bj-beta", action="store_true")
    p.add_argument("--repetitions", type=int, default=4000)
    p.add_argument("--K", default="10,3")
    p.add_argument("--taux", type=float, default=0.01)
    p.add_argument("--delta", type=float, default=0.05)
    p.add_argument("--biais", default="0,0.0125")
    p.add_argument("--comparateurs", default="1,8")
    p.add_argument("--tailles", default="160,288,400")
    p.add_argument("--seuils", default="160,40,20")
    p.add_argument("--n80", action="store_true", help="n80 (k gardes) pour le plus grand k, chaque seuil et biais")
    a = p.parse_args()
    debut = time.time()
    rhos = [float(x) for x in a.rho.split(",")]
    Ks = [int(x) for x in a.K.split(",")]
    biais = [float(x) for x in a.biais.split(",")]
    ks = [int(x) for x in a.comparateurs.split(",")]
    tailles = [int(x) for x in a.tailles.split(",")]
    seuils = [float(x) for x in a.seuils.split(",")]
    sortie = {"version": "sensibilite-beta-v1", "statut": "exploratoire, non opposable, lois synthétiques",
              "script_v4_sha256": simv4.hashlib.sha256(open(CHEMIN_V4, "rb").read()).hexdigest(),
              "reglages": vars(a), "cellules": {}, "n80": {}}
    for rho in rhos:
        for K in Ks:
            loi = LoiBeta(K, K, a.taux, 0.4, 0.10, rho, a.bj_beta)
            for n in tailles:
                for b in biais:
                    for k in ks:
                        et = f"{loi.nom()}|delta={a.delta}|n={n}|biais={b}|k={k}"
                        sortie["cellules"][et] = simv4.cellule(loi, loi, a.repetitions, n, n, a.delta, seuils, k, b,
                                                               a.graine, et, artefacts=True)
            if a.n80:
                kmax = max(ks)
                for s in seuils:
                    for b in biais:
                        cle = f"{loi.nom()}|delta={a.delta}|seuil={s}|biais={b}|k={kmax}"
                        sortie["n80"][cle] = simv4.n_pour_puissance(loi, loi, min(a.repetitions, 2000), a.delta, s, kmax, b,
                                                                     a.graine, cle)
    sortie["environnement"] = {"python": platform.python_version(), "numpy": np.__version__,
                               "duree_s": round(time.time() - debut, 1)}
    json.dump(sortie, sys.stdout, indent=1, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    principal()
