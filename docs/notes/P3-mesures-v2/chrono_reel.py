"""Durée d'entraînement des familles de sondes de P3 à la taille réelle du jeu « enjeux élevés » (constat TC-12 de la
contre-lecture R2 du texte) : 1 600 séquences d'entraînement de 69 jetons (≈ 110 000 jetons, 80 % des 2 000 textes tronqués
à 128 jetons, longueur moyenne recomptée au vrai tokeniseur), largeur 4 096, réglages par défaut du code de T0.7 tel quel
(300 époques). Données gaussiennes (la durée ne dépend pas des valeurs) ; une famille à la fois, au nombre de fils donné.
Usage : python chrono_reel.py FILS FAMILLE [FAMILLE …]"""
import sys
import time

import numpy as np
import torch

sys.path.insert(0, "/home/user/controle-ia-travail/src")
from controle_ia.sondes.familles import Reglages, entrainer  # noqa: E402

fils, familles = int(sys.argv[1]), sys.argv[2:]
torch.set_num_threads(fils)
rng = np.random.default_rng(20261017)
n_seq, L, d = 1600, 69, 4096
seqs = [rng.standard_normal((L, d)).astype(np.float32) for _ in range(n_seq)]
y = np.array([i % 2 for i in range(n_seq)])
print(f"fils {fils} ; {n_seq} séquences × {L} jetons = {n_seq * L} jetons ; largeur {d} ; torch {torch.__version__}", flush=True)
for f in familles:
    ag = "attention" if f == "attention" else "max"
    r = Reglages()
    t = time.time()
    entrainer(f, "x", 0, seqs, y, ag, 1, r)
    dt = time.time() - t
    pertes = [x["perte"] for x in r.journal]
    print(f"{f:20s} {dt:9.1f} s ({r.epoques} époques) ; pertes : {len(pertes)} relevées, première "
          f"{pertes[0] if pertes else float('nan'):.4f}, dernière {pertes[-1] if pertes else float('nan'):.4f}", flush=True)
