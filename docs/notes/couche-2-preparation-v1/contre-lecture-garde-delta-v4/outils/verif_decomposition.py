"""Q3b-c : l'effet d'unité en logit est-il une dépendance pure ? Pourquoi le contraste baisse-t-il et la garde non ?
Variantes (4 000 répétitions, 160 unités, seuil 160, biais 0, graine propre par variante et cellule) :
 Z  : sans effet (σ = 0) ;
 S  : effet du script, σ logit = 1 (même u pour honnêtes et sabotés d'une unité, commun aux k comparateurs) ;
 E  : comme S, u des sabotés tiré à part (aucun lien garde-contraste) ;
 H  : effet sur les honnêtes de A seulement ; T : effet sur les sabotés de A seulement ;
 B  : effet bêta à espérance tenue et corrélation intra-unité ρ constante (ρ = 0,17, celle que le logit σ = 1 donne à
      p = 0,5), sur les deux côtés, u indépendants : même dispersion relative pour la garde et le contraste ;
 Bh : comme B, sur les honnêtes seulement.
Les fiches sont calculées par `cellule` du script (artefacts sans objet)."""
import importlib.util, json, math, time
import numpy as np
C = "/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/relecture-garde-delta-v4/cl"
spec = importlib.util.spec_from_file_location("sim4", f"{C}/outils/copie_script/sim_garde_v4.py")
sim = importlib.util.module_from_spec(spec); spec.loader.exec_module(sim)

def beta_p(rng, p0, rho, forme):
    if rho <= 0 or p0 <= 0 or p0 >= 1:
        return np.full(forme, p0)
    s = 1 / rho - 1  # a + b
    return rng.beta(p0 * s, (1 - p0) * s, size=forme)

class Variante(sim.LoiSynthetique):
    def __init__(self, K, tau, mode, sigma=1.0, rho=0.17):
        super().__init__(K, K, tau, 0.4, 0.10, True, 0.0)
        self.mode, self.sigma, self.rho = mode, sigma, rho
    def tirer(self, rng, reps, n, n_garde, k, biais, biais_contraste=0.0):
        pa_h = min(self.taux + biais, 1.0); ra = min(self.r_b + self.ecart, 1.0)
        fg, fv = (reps, 1, n_garde), (reps, 1, n)
        uh = rng.normal(size=fg)
        us = uh[:, :, :n] if (self.mode == "S" and n <= n_garde) else rng.normal(size=fv)
        sig_h = self.sigma if self.mode in ("S", "E", "H") else 0.0
        sig_s = self.sigma if self.mode in ("S", "E", "T") else 0.0
        if self.mode in ("B", "Bh"):
            ph = beta_p(rng, pa_h, self.rho, fg); ps = beta_p(rng, ra, self.rho if self.mode == "B" else 0.0, fv)
        else:
            ph = sim.proba_decalee(pa_h, sig_h, uh) if sig_h else np.full(fg, pa_h)
            ps = sim.proba_decalee(ra, sig_s, us) if sig_s else np.full(fv, ra)
        fa = rng.binomial(self.K_h, ph) / self.K_h
        rA = rng.binomial(self.K_s, ps) / self.K_s
        fb = rng.binomial(self.K_h, self.taux, size=(reps, k, n_garde)) / self.K_h
        rB = rng.binomial(self.K_s, self.r_b, size=(reps, k, n)) / self.K_s
        return fa - fb, rA - rB

cas = [(10, 0.01, 0.05, 1), (10, 0.01, 0.05, 3), (10, 0.01, 0.10, 3), (10, 0.10, 0.05, 3), (3, 0.01, 0.05, 3), (3, 0.10, 0.10, 3)]
modes = ["Z", "S", "E", "H", "T", "B", "Bh"]
res = []
t0 = time.time()
for K, tau, d, k in cas:
    ligne = {"K": K, "tau": tau, "delta": d, "k": k}
    for m in modes:
        loi = Variante(K, tau, m)
        c = sim.cellule(loi, loi, 4000, 160, 160, d, [160.0], k, 0.0, 777, f"decomp|{m}|{K}|{tau}|{d}|{k}", artefacts=False)["160.0"]
        ligne[m] = {"garde_seule": c["garde_seule"]["part"], "k_gardes": c["k_gardes"]["part"],
                    "k_contrastes": c["k_contrastes"]["part"], "fiche": c["fiche_entiere"]["part"]}
    res.append(ligne)
    print(K, tau, d, k, " | ".join(f"{m}: {ligne[m]['k_gardes']:.3f}/{ligne[m]['k_contrastes']:.3f}/{ligne[m]['fiche']:.3f}" for m in modes), flush=True)
# dispersion : corrélation intra-unité implicite du logit σ = 1 selon p
rng = np.random.default_rng(99)
icc = []
for p0 in [0.01, 0.035, 0.1, 0.2, 0.5]:
    u = rng.standard_normal(2_000_000)
    v = float(sim.proba_decalee(p0, 1.0, u).var())
    icc.append({"p0": p0, "var_p": v, "rho_implicite": v / (p0 * (1 - p0))})
print(icc)
json.dump({"variantes": res, "rho_implicite_logit_sigma1": icc, "duree_s": round(time.time() - t0, 1)},
          open(f"{C}/sorties/verif_decomposition.json", "w"), indent=1, ensure_ascii=False)
