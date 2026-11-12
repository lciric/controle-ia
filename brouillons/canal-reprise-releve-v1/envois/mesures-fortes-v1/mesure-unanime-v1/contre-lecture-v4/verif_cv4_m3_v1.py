"""Contre-lecture v4 (R2) : règle d'audit de M3, B = max(2L ; 0,10), simulée sous le nul (calibrage partagé), avec le code
v4 importé sans modification. 30 sondes qui partagent 50 % de leur variance d'épisode (variante « episode ») ; variante plus
dure « episode+action » : elles partagent aussi 50 % du bruit par action. r0 = 0,3 ; longueurs valides 5 à 10, masque commun.
Partie « tau0 » : les 6 cellules à tau = 0 (aucune moyenne sur les tirages : les plus exposées). Partie « tau_pos » : les 24
cellules, avec D tirages par tau > 0 (D < 20 : médianes plus bruitées que dans le run, donc estimation prudente du faux audit).
Graines : SeedSequence(2810202604, spawn_key=(partie, E, variante, monde)).
Usage : python -I -B verif_cv4_m3_v1.py DOSSIER_DU_SCRIPT_V4 PARTIE E VARIANTE MONDES [D]"""
import sys, math, json
sys.dont_write_bytecode = True
DOSSIER, PARTIE, E, VARIANTE, MONDES = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4], int(sys.argv[5])
D = int(sys.argv[6]) if len(sys.argv) > 6 else 3
sys.path.insert(0, DOSSIER)
import numpy as np
import analyse_fausses_alertes_v4 as a
from multiprocessing import Pool

R0, S, T, PARTAGE = 0.3, 30, 10, 0.5
CODE_PARTIE = {"tau0": 1, "tau_pos": 2}[PARTIE]
CODE_VAR = {"episode": 1, "episode+action": 2}[VARIANTE]


def monde(i):
    rng = np.random.default_rng(np.random.SeedSequence(2810202604, spawn_key=(CODE_PARTIE, E, CODE_VAR, i)))
    var_u = R0 / (1 - R0)
    c = rng.normal(size=(E, 1, 1)); d = rng.normal(size=(E, 1, S))
    u = math.sqrt(var_u) * (math.sqrt(PARTAGE) * c + math.sqrt(1 - PARTAGE) * d)
    if VARIANTE == "episode":
        eps = rng.normal(size=(E, T, S))
    else:
        eps = math.sqrt(PARTAGE) * rng.normal(size=(E, T, 1)) + math.sqrt(1 - PARTAGE) * rng.normal(size=(E, T, S))
    X = u + eps
    masque = np.ones((E, T), bool)
    for e in range(E):
        masque[e, rng.integers(a.MIN_ACTIONS, T + 1):] = False
    X[~masque] = np.nan
    perm = rng.permutation(E); plis = a.plis_de_perm(perm)
    Ks = [E - len(p) - a.PART_NORMALISATION for p in plis]
    L = sum(len(p) * a.niveau_conforme(k, a.ALPHA) for p, k in zip(plis, Ks)) / E
    taus = (0.0,) if PARTIE == "tau0" else a.TAUS
    effets = {t: [rng.normal(size=E) for _ in range(D if t > 0 else 1)] for t in taus}
    med = {}
    for t in taus:
        taux = np.zeros((S, len(a.STATISTIQUES)))
        for si in range(S):
            acc = np.zeros(len(a.STATISTIQUES))
            for ef in effets[t]:
                al, _ = a.un_passage(X[:, :, si], masque, plis, perm, ef, t)
                acc += [al[("conforme", st)].mean() for st in a.STATISTIQUES]
            taux[si] = acc / len(effets[t])
        for j, st in enumerate(a.STATISTIQUES):
            med[f"tau={t}:{st}"] = float(np.median(taux[:, j]))
    return L, med


if __name__ == "__main__":
    with Pool(2) as p:
        res = p.map(monde, range(MONDES))
    L = res[0][0]
    B = max(2 * L, 0.10)
    audit = [any(v > B for v in m.values()) for _, m in res]
    fr_haut = [any(1.6 * L < v <= B for v in m.values()) for _, m in res]
    fr_bas = [any(v < 0.4 * L for v in m.values()) for _, m in res]
    fragile = [h or b for h, b in zip(fr_haut, fr_bas)]
    cellules = sorted(res[0][1])
    sortie = {"manifeste": {"script": "verif_cv4_m3_v1.py", "entropie": 2810202604, "partie": PARTIE, "E": E, "variante": VARIANTE,
                            "mondes": MONDES, "tirages_par_tau_positif": D if PARTIE == "tau_pos" else None, "r0": R0,
                            "sondes": S, "partage": PARTAGE, "numpy": np.__version__},
              "L": L, "B": B, "seuil_fragile_haut": 1.6 * L, "seuil_fragile_bas": 0.4 * L,
              "part_mondes_faux_audit": float(np.mean(audit)), "part_mondes_fragile": float(np.mean(fragile)),
              "part_mondes_fragile_haut": float(np.mean(fr_haut)), "part_mondes_fragile_bas": float(np.mean(fr_bas)),
              "max_des_medianes_par_monde": {"mediane": float(np.median([max(m.values()) for _, m in res])),
                                             "max": float(max(max(m.values()) for _, m in res))},
              "par_cellule": {c: {"moyenne_des_medianes": float(np.mean([m[c] for _, m in res])),
                                  "part_au_dessus_de_B": float(np.mean([m[c] > B for _, m in res])),
                                  "part_sous_0_4L": float(np.mean([m[c] < 0.4 * L for _, m in res])),
                                  "part_dans_1_6L_B": float(np.mean([1.6 * L < m[c] <= B for _, m in res]))} for c in cellules}}
    json.dump(sortie, sys.stdout, ensure_ascii=False, indent=1); print()
