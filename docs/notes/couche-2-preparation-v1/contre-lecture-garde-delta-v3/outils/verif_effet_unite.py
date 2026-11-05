"""Q4 : le modèle « effet d'unité sur A » du script v3 — ce qu'il déplace, et dans quel sens.

1. Espérance exacte de clip(p + u, 0, 1), u ~ N(0, σ) : le décalage écrêté change-t-il E[f_A] (donc E[g]) ?
2. Décomposition par simulation (machinerie `cellule` du script, 4 000 répétitions, seuil 160) :
   A  sans effet, biais 0 (référence)
   B  effet du script (σ)                         : ce que rapporte la v3
   C  sans effet, biais = décalage d'espérance de B : part due au seul déplacement de la moyenne
   D  effet à espérance tenue (p' tel que E[clip(p' + u)] = p, même pour r_A) : variance + lien garde-contraste
   E  comme D, mais u des sabotés tiré à part (aucun lien garde-contraste) : variance seule
   Le lien garde-contraste se lit sur la fiche : D contre E.
Usage : python3 -I -B verif_effet_unite.py SORTIE.json
"""
import importlib.util
import json
import math
import os
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("sim_garde_v3", os.path.join(ICI, "copie_script", "sim_garde_v3.py"))
sim = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sim)


def phi(x):
    return math.exp(-x * x / 2) / math.sqrt(2 * math.pi)


def Phi(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def esp_clip(p, s):
    """E[clip(p + U, 0, 1)], U ~ N(0, s²) : E[min(1, max(0, X))] = E[max(0,X)] − E[max(0, X − 1)]."""
    def emax0(mu):
        return mu * Phi(mu / s) + s * phi(mu / s)
    return emax0(p) - emax0(p - 1)


def p_tenu(p, s):
    bas, haut = -1.0, 1.0
    for _ in range(200):
        mil = (bas + haut) / 2
        if esp_clip(mil, s) < p:
            bas = mil
        else:
            haut = mil
    return (bas + haut) / 2


class LoiTenue(sim.LoiSynthetique):
    """Effet d'unité à espérance tenue ; `lie` : même u pour honnêtes et sabotés de l'unité (sinon tirés à part)."""

    def __init__(self, *a, lie=True, **kw):
        super().__init__(*a, **kw)
        self.lie = lie

    def tirer(self, rng, reps, n, n_garde, k, biais, biais_contraste=0.0):
        s = self.effet_unite
        pa_h = p_tenu(min(self.taux + biais, 1.0), s)
        ra = p_tenu(min(self.r_b + self.ecart + biais_contraste, 1.0), s)
        kk = 1 if self.partage else k
        u_h = rng.normal(0.0, s, size=(reps, kk, n_garde))
        if self.lie:
            u_s = u_h[:, :, :n] if n <= n_garde else np.concatenate([u_h, rng.normal(0.0, s, size=(reps, kk, n - n_garde))], 2)
        else:
            u_s = rng.normal(0.0, s, size=(reps, kk, n))
        fa = rng.binomial(self.K_h, np.clip(pa_h + u_h, 0, 1)) / self.K_h
        rA = rng.binomial(self.K_s, np.clip(ra + u_s, 0, 1)) / self.K_s
        fb = rng.binomial(self.K_h, self.taux, size=(reps, k, n_garde)) / self.K_h
        rB = rng.binomial(self.K_s, self.r_b, size=(reps, k, n)) / self.K_s
        return fa - fb, rA - rB


def lire(c, s="160.0"):
    b = c[s]
    return {x: b[x]["part"] for x in ("garde_seule", "k_gardes", "k_contrastes", "fiche_entiere")} | {
        "frontiere": b.get("frontiere_part"), "tricheur": b.get("tricheur_part")}


def main():
    sortie = {"esperances": {}, "decomposition": {}}
    for s in (0.05, 0.10):
        for p in (0.0, 0.01, 0.06, 0.10, 0.11, 0.20, 0.50):
            sortie["esperances"][f"sigma={s}|p={p}"] = {"E_clip": esp_clip(p, s), "decalage": esp_clip(p, s) - p}
    reps, graine = 4000, 777001
    for K, taux in ((10, 0.01), (10, 0.10), (3, 0.01), (3, 0.10)):
        for d in (0.05, 0.10):
            for k in (1, 3):
                sig = 0.05
                dec = esp_clip(taux, sig) - taux  # décalage de E[f_A] (B sans effet a l'espérance τ)
                dec_r = esp_clip(0.5, sig) - 0.5
                cas = {
                    "A_sans_effet": (sim.LoiSynthetique(K, K, taux, 0.4, 0.10, True, 0.0), 0.0),
                    "B_effet_du_script": (sim.LoiSynthetique(K, K, taux, 0.4, 0.10, True, sig), 0.0),
                    "C_biais_egal_au_decalage": (sim.LoiSynthetique(K, K, taux, 0.4, 0.10, True, 0.0), dec),
                    "D_effet_tenu_lie": (LoiTenue(K, K, taux, 0.4, 0.10, True, sig, lie=True), 0.0),
                    "E_effet_tenu_non_lie": (LoiTenue(K, K, taux, 0.4, 0.10, True, sig, lie=False), 0.0),
                }
                bloc = {"decalage_E_fA": dec, "decalage_E_rA": dec_r}
                for nom, (loi, b) in cas.items():
                    et = f"verif|{nom}|K{K}|taux{taux}|d{d}|k{k}"
                    c = sim.cellule(loi, loi, reps, 160, 160, d, [160.0], k, b, graine, et, True)
                    bloc[nom] = lire(c)
                sortie["decomposition"][f"K={K}|taux={taux}|delta={d}|k={k}"] = bloc
                print(K, taux, d, k, {n: bloc[n]["fiche_entiere"] for n in cas}, {n: bloc[n]["garde_seule"] for n in cas},
                      flush=True)
    json.dump(sortie, open(sys.argv[1], "w"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
