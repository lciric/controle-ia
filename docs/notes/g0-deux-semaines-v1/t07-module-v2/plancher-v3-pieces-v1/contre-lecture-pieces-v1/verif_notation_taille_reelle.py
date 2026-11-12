import numpy as np, time
from controle_ia.t07 import plancher_v3 as p3, plancher_v1 as p1
from controle_ia.sondes.evaluation import plancher_apparie
rng = np.random.default_rng(11)
d, K = 4096, 800
# covariance à spectre décroissant (rang plein), jetons en simple précision
ech = (1.0 / np.sqrt(1 + np.arange(d))).astype(np.float32)
ent = [(rng.standard_normal((60, d)).astype(np.float32) * ech * 20 + 3) for _ in range(120)]      # 7 200 jetons > largeur
seqs = [(rng.standard_normal((int(rng.integers(1, 400)), d)).astype(np.float32) * ech * 20 + 3) for _ in range(36)]
for ag in ("max", "attention"):
    t = time.time(); pl = plancher_apparie("x", 15, ent, ag, K, 123); t1 = time.time() - t
    t = time.time(); v = p3.scores_plancher_vectorises(pl, seqs); t2 = time.time() - t          # contrôle en ligne joué
    t = time.time(); ref = p1.scores_plancher(pl, seqs); t3 = time.time() - t
    e = p3.ecart_a_la_boucle(pl, seqs, v, range(K))
    rel = float((np.abs(v - ref) / np.maximum(np.abs(ref), 1e-300)).max())
    print(ag, "800 × 4096, 36 actions,", sum(len(s) for s in seqs), "jetons : écart/échelle %.2e ; écart/|score| %.2e ; égaux au bit %.3f ; tirage %.0f s, lots %.1f s, boucle %.1f s"
          % (e["ecart_relatif_max"], rel, e["egaux_au_bit_pres"], t1, t2, t3), flush=True)
    ech_mod = p3.echelle_par_action(p3.matrices_du_plancher(pl), seqs, range(K))
    print("   rapport médian échelle/|score| : %.1e ; max : %.1e" % (np.median(ech_mod / np.abs(ref)), (ech_mod / np.abs(ref)).max()))
