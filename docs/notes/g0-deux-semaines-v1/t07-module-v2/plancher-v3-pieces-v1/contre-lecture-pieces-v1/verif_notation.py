import numpy as np, tracemalloc
from controle_ia.t07 import plancher_v3 as p3, plancher_v1 as p1
from controle_ia.sondes.familles import SondeLineaireJetons
from controle_ia.sondes.evaluation import plancher_apparie
print("import", p3.__file__)
rng = np.random.default_rng(7)
pire = 0.0
for essai in range(10):
    d = int(rng.choice([16, 64, 256])); K = int(rng.integers(3, 60)); ag = ["max", "attention"][essai % 2]
    ent = [rng.standard_normal((int(rng.integers(1, 40)), d)).astype(np.float32) * rng.uniform(0.1, 30) for _ in range(40)]
    pl = plancher_apparie("x", 15, ent, ag, K, int(rng.integers(1, 10**9)))
    if essai >= 6:      # échelles extrêmes : logits d'attention très grands, biais grands
        pl = [SondeLineaireJetons(p.nom, p.couche, p.agregation, p.w * 50, p.b + 1e4, None if p.q is None else p.q * 200, p.famille) for p in pl]
    seqs = [rng.standard_normal((int(rng.integers(1, 300)), d)).astype(np.float32) * rng.uniform(0.1, 30) for _ in range(int(rng.integers(1, 70)))]
    ref = p1.scores_plancher(pl, seqs)
    for lot in (1, 7, 257, 4096, 10**6):
        v = p3.scores_plancher_vectorises(pl, seqs, taille_lot=lot, controle=0)
        e = p3.ecart_a_la_boucle(pl, seqs, v, range(K))
        pire = max(pire, e["ecart_relatif_max"])
        # écart rapporté au score lui-même (mesure indépendante de l'échelle du module)
        rel = float((np.abs(v - ref) / np.maximum(np.abs(ref), 1e-300)).max())
        if lot in (1, 4096):
            print(essai, ag, "d", d, "K", K, "actions", len(seqs), "lot", lot, "écart/échelle %.2e" % e["ecart_relatif_max"], "écart/|score| %.2e" % rel,
                  "rang égal", bool(all(np.array_equal(np.argsort(v[:, k], kind="stable"), np.argsort(ref[:, k], kind="stable")) for k in range(K))))
print("pire écart rapporté à l'échelle : %.3e" % pire)
# mémoire : 800 directions, largeur 4096, 300 actions de 225 jetons
d, K = 4096, 800
W = rng.standard_normal((K, d)); pl = [SondeLineaireJetons(f"p{k}", 15, "max", W[k], 0.1, None, "plancher") for k in range(K)]
seqs = [rng.standard_normal((225, d)).astype(np.float32) for _ in range(300)]
tracemalloc.start(); v = p3.scores_plancher_vectorises(pl, seqs, controle=0); cur, pic = tracemalloc.get_traced_memory(); tracemalloc.stop()
print("pic de mémoire (800 × 4096, lots de 4096 jetons) : %.0f Mo" % (pic / 1e6), v.shape)
