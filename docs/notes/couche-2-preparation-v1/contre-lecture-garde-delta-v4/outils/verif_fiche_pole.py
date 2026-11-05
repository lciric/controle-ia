"""Q4 : la fiche simulée par la v4 est-elle `pari_apparie.evaluer` (pôle v41) ? Pour chaque essai : tirage de g (k, n_garde)
et v (k, n) par une loi de la v4 (synthétique avec ou sans effet d'unité en logit, partagée ou non ; réelle brute ou
recentrée), puis fiche par `processus` + `premiere_atteinte` du script et par `evaluer` du pôle (gardes en dictionnaire)."""
import importlib.util, json, math, os, sys
import numpy as np
C = "/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/relecture-garde-delta-v4/cl"
spec = importlib.util.spec_from_file_location("sim4", f"{C}/outils/copie_script/sim_garde_v4.py")
sim = importlib.util.module_from_spec(spec); spec.loader.exec_module(sim)
sys.path.insert(0, f"{C}/outils/copie_pole")
import pari_apparie as pole

class Fixe:
    def __init__(self, g, v): self.g, self.v = g, v
    def tirer(self, *a, **k): return self.g, self.v

rng = np.random.default_rng(np.random.SeedSequence([2026, 1029, 4]))
stats = {"essais": 0, "ecart_max_trajectoire": 0.0, "longueurs_differentes": 0, "arrets_differents": 0, "promues": 0,
         "promues_longueurs_differentes": 0, "avec_effet_logit": 0, "reels": 0}
for essai in range(1200):
    k = int(rng.integers(1, 4)); n = int(rng.integers(5, 120)); ng = int(rng.choice([n, rng.integers(5, 120)]))
    delta = float(rng.choice([0.05, 0.10, 0.20])); m = int(rng.choice([1, 8])); alpha = float(rng.choice([0.05, 0.01]))
    biais = float(rng.choice([0.0, 0.0125, 0.025]))
    if essai < 1000:
        sig = float(rng.choice([0.0, 0.5, 1.0, 3.0])); K = int(rng.choice([3, 10])); tau = float(rng.choice([0.0, 0.01, 0.10]))
        ecart = float(rng.choice([0.1, 0.3, 0.5]))
        loi = sim.LoiSynthetique(K, K, tau, 0.4, ecart, bool(rng.integers(0, 2)), sig)
        stats["avec_effet_logit"] += sig > 0
    else:
        N = int(rng.integers(10, 60))
        eg = [np.round(rng.uniform(-1, 1, N) * rng.uniform(0, 1), 3) for _ in range(k)]
        ev = [np.round(rng.uniform(-1, 1, N) * rng.uniform(0, 1), 3) for _ in range(k)]
        for x in eg + ev: x[0] = -1.0; x[1] = 1.0
        loi = sim.LoiReelle(eg, ev, bool(rng.integers(0, 2)))
        stats["reels"] += 1
    g, v = loi.tirer(rng, 1, n, ng, k, biais)
    gardes, contrastes = sim.processus(Fixe(g, v), rng, 1, n, ng, k, delta, biais, None)
    mini = np.minimum(gardes.min(axis=0), contrastes.min(axis=0))[0]
    s = m / alpha
    idx = int(sim.premiere_atteinte(mini[None, :], s)[0])
    r = pole.evaluer({f"B{j}": [float(x) for x in v[0, j]] for j in range(k)},
                     {f"B{j}": [float(x) for x in g[0, j]] for j in range(k)}, delta, alpha, m)
    tp = np.array(r["trajectoire_log_min"])
    if tp.shape != mini.shape:
        stats["longueurs_differentes"] += 1
        continue
    stats["ecart_max_trajectoire"] = max(stats["ecart_max_trajectoire"], float(np.abs(tp - mini).max()))
    arr = r["instant_d_arret"] or -1
    stats["arrets_differents"] += int(arr != idx)
    stats["promues"] += int(r["promue"])
    stats["promues_longueurs_differentes"] += int(r["promue"] and n != ng)
    stats["essais"] += 1
stats["pole_sha256"] = __import__("hashlib").sha256(open(f"{C}/outils/copie_pole/pari_apparie.py", "rb").read()).hexdigest()
json.dump(stats, open(f"{C}/sorties/verif_fiche_pole.json", "w"), indent=1)
print(stats)
