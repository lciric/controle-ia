"""Coût marginal d'une époque d'entraînement (familles de T0.7) à d = 4 096 : temps à E1 et E2 époques, pente par époque
et par millier de jetons. Usage : python -I pente_epoques.py FILS N_SEQUENCES LONGUEUR E1 E2"""
import sys
import time

import numpy as np
import torch

sys.path.insert(0, "/home/user/controle-ia-travail/src")
from controle_ia.sondes.familles import Reglages, entrainer  # noqa: E402

fils, n_seq, L, e1, e2 = (int(x) for x in sys.argv[1:6])
torch.set_num_threads(fils)
rng = np.random.default_rng(0)
seqs = [rng.standard_normal((L, 4096)).astype(np.float32) for _ in range(n_seq)]
y = np.array([i % 2 for i in range(n_seq)])
jetons = n_seq * L
for f, ag in [("lineaire", "max"), ("perceptron", "max"), ("attention", "attention")]:
    t = []
    for e in (e1, e2):
        t0 = time.time()
        entrainer(f, "x", 0, seqs, y, ag, 1, Reglages(epoques=e))
        t.append(time.time() - t0)
    pente = (t[1] - t[0]) / (e2 - e1)
    print(f"{f:12s} {e1} époques {t[0]:7.1f} s ; {e2} époques {t[1]:7.1f} s ; {pente * 1000:8.1f} ms par époque pour "
          f"{jetons} jetons, soit {pente * 1000 / (jetons / 1000):6.2f} ms par époque et par millier de jetons", flush=True)
