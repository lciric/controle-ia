"""Table de M2 bis refaite avec le code v2 (15 épisodes de normalisation, effet commun aux sondes) — SYNTHÉTIQUE seulement.
Graine : SeedSequence(20261027234500). Ville à τ = 0 et τ = 2, moyenne sur 8 sondes et 4 tirages, r0 ∈ {0 ; 0,2 ; 0,5 ; 0,8}."""
import importlib.util
import json
import math
import sys

import numpy as np

ENTROPIE = 20261027234500


def main():
    spec = importlib.util.spec_from_file_location("v2", sys.argv[1]); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    rng = np.random.default_rng(np.random.SeedSequence(ENTROPIE))
    out = {"manifeste": {"entropie": ENTROPIE, "numpy": np.__version__}}
    for r0 in (0.0, 0.2, 0.5, 0.8):
        E, S, T = 60, 8, 10
        u = rng.normal(0, math.sqrt(r0), size=(E, 1, S))
        X = u + rng.normal(0, math.sqrt(1 - r0), size=(E, T, S))
        mk = np.ones((E, T), bool)
        for e in range(E):
            mk[e, rng.integers(5, T + 1):] = False
        X[~mk] = np.nan
        perm = rng.permutation(E); plis = m.plis_de_perm(perm)
        v0, v2, pa0 = [], [], []
        effets = [rng.normal(size=E) for _ in range(4)]
        for si in range(S):
            al, _ = m.un_passage(X[:, :, si], mk, plis, perm, np.zeros(E), 0.0)
            v0.append(al[("ville", "processus_e")].mean()); pa0.append(al[("par_action", "max")].mean())
            v2.append(np.mean([m.un_passage(X[:, :, si], mk, plis, perm, ef, 2.0)[0][("ville", "processus_e")].mean() for ef in effets]))
        out[f"r0={r0}"] = {"ville_tau0": float(np.mean(v0)), "ville_tau2": float(np.mean(v2)), "difference": float(np.mean(v2) - np.mean(v0)),
                           "par_action_tau0": float(np.mean(pa0))}
    json.dump(out, sys.stdout, ensure_ascii=False, indent=1); print()


if __name__ == "__main__":
    main()
