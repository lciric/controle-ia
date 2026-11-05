"""Contre-lecture v5, question 2 : la retenue e-BH simulée par la v5 est-elle celle du pôle ?

Trois volets, tirages et graines propres au contre-lecteur (graine 77001, différente de l'auteur) :
1. familles de trajectoires tirées par moi (marches aléatoires, valeurs quantifiées pour forcer des ex æquo, valeurs posées
   exactement au seuil d'arrêt et au bord e-BH, pics au-dessus de la valeur finale sans atteinte, trajectoires de longueurs
   différentes, m > f) : `retenues_famille` de la v5 contre `Course` (entrer, ajouter_trajectoire, lire) du pôle ;
2. chaîne entière : `cellule(..., ebh)` de la v5, tirages bruts capturés (enveloppe autour de `tirer`) puis relus par le pôle
   (`evaluer` pour chaque fiche, `Course` pour l'arrêt et l'e-BH) ; parts de la v5 contre parts recalculées ;
3. arrêt : une trajectoire qui dépasse le seuil puis redescend est-elle lue à l'instant d'atteinte (Course) ? une trajectoire
   qui frôle le seuil puis redescend est-elle lue à sa valeur finale (et non à son maximum) ?

Usage : python3 -I -B verif_ebh_pole.py SCRIPT_V5 PARI_APPARIE SORTIE.json
"""
import hashlib
import importlib.util
import json
import math
import sys

import numpy as np

SCRIPT, POLE, SORTIE = sys.argv[1:4]


def charger(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


v5 = charger("sim_v5", SCRIPT)
pa = charger("pole", POLE)
emp = lambda c: hashlib.sha256(open(c, "rb").read()).hexdigest()
bilan = {"volet": "chaîne entière, cellules puissantes", "script_sha256": emp(SCRIPT), "pole_sha256": emp(POLE), "graine": 77001}
rng = np.random.default_rng(np.random.SeedSequence(77002))


def pole_famille(trajs, m, alpha):
    """trajs : liste de listes (log). Rend (valeurs Course, atteint, retenues) par le pôle."""
    c = pa.Course(alpha=alpha, essai=True)
    noms = [f"F{i:03d}" for i in range(m)]
    c.entrer("fam", noms, alpha)
    for i, t in enumerate(trajs):
        c.ajouter_trajectoire(noms[i], list(map(float, t)), sans_identite=True)
    sans = {noms[i]: "non simulée" for i in range(len(trajs), m)}
    ret = c.lire(sans_partie=sans)
    f = len(trajs)
    return ([c.log_e[noms[i]] for i in range(f)], [noms[i] in c.arretees for i in range(f)], [noms[i] in ret for i in range(f)],
            sorted(ret))


# --- 2. chaîne entière
class Enveloppe:
    def __init__(self, loi):
        self.loi, self.log = loi, []
        self.partage = loi.partage

    def effet(self):
        return self.loi.effet()

    def nom(self):
        return self.loi.nom()

    def tirer(self, *a, **k):
        g, v = self.loi.tirer(*a, **k)
        self.log.append((g.copy(), v.copy()))
        return g, v


def fiche_pole(g, v, delta, alpha, m):
    """g (k, n_garde), v (k, n) : evaluer du pôle, plusieurs gardes."""
    r = pa.evaluer({j: [float(x) for x in np.clip(v[j], -1, 1)] for j in range(v.shape[0])},
                   {j: [float(x) for x in g[j]] for j in range(g.shape[0])}, delta, alpha=alpha, m=m)
    return r


diff2, cel2, ecart_e = [], [], 0.0
for it in range(12):
    K = 10
    taux = 0.01
    k = int(rng.choice([2, 3, 8]))
    n = int(rng.choice([100, 140, 160]))
    ng = int(rng.choice([n, n - 20, n + 20]))
    delta = float(rng.choice([0.05, 0.075, 0.10]))
    biais = float(rng.choice([0.0, 0.0125]))
    M = int(rng.integers(1, 4))
    N0 = int(rng.choice([0, 2, 4]))
    alpha = 0.05
    effet = float(rng.choice([0.0, 0.0, 1.0]))
    reps = 40
    loi = v5.LoiSynthetique(K, K, taux, 0.4, 0.10, True, effet, True, 0.0)
    E, EA, EB = Enveloppe(loi), Enveloppe(loi.variante_nulle(True)), Enveloppe(loi.variante_nulle(False))
    ebh = {"lectures": ["A", "B"], "M": M, "N": N0, "alpha": alpha, "nulle_A": EA, "nulle_B": EB}
    et = f"cl|{it}"
    res = v5.cellule(E, E, reps, n, ng, delta, [8 / alpha], k, biais, 4242, et, artefacts=False, ebh=ebh)
    modes = [E.log[0]] + E.log[1:]  # tirage principal puis M-1 modes
    assert len(modes) == M, (len(modes), M)
    nullesA = EA.log
    nullesB = EB.log
    parts = {"A": [], "B": []}
    for r in range(reps):
        for lect in ("A", "B"):
            trajs, vraies, du_sujet = [], 0, 1
            if lect == "A":
                mfam = M + N0
                for g, v in modes:
                    trajs.append(fiche_pole(g[r], v[r], delta, alpha, mfam))
                vraies = M
                for g, v in nullesA:
                    trajs.append(fiche_pole(g[r], v[r], delta, alpha, mfam))
            else:
                mfam = M * k + N0
                for g, v in modes:
                    for j in range(k):
                        trajs.append(fiche_pole(g[r][j:j + 1], v[r][j:j + 1], delta, alpha, mfam))
                vraies, du_sujet = M * k, k
                if N0:
                    g, v = nullesB[0]
                    for j in range(N0):
                        trajs.append(fiche_pole(g[r][j:j + 1], v[r][j:j + 1], delta, alpha, mfam))
            pv, pat, pret, _ = pole_famille([t["trajectoire_log_min"] for t in trajs], mfam, alpha)
            # cohérence evaluer / Course (même seuil log(m/α)) : valeur arrêtée identique
            for t, x in zip(trajs, pv):
                ecart_e = max(ecart_e, abs(t["log_e_valeur"] - x))
            parts[lect].append((pat, pret, vraies, du_sujet))
    for lect in ("A", "B"):
        P = parts[lect]
        calc = {"premiere_atteinte_une_fiche": np.mean([p[0][0] for p in P]),
                "premiere_atteinte_fiches_du_sujet": np.mean([all(p[0][:p[3]]) for p in P]),
                "retenue_une_fiche": np.mean([p[1][0] for p in P]),
                "retenues_fiches_du_sujet": np.mean([all(p[1][:p[3]]) for p in P]),
                "retenues_toutes_vraies": np.mean([all(p[1][:p[2]]) for p in P]),
                "retenue_sans_atteinte_une_fiche": np.mean([p[1][0] and not p[0][0] for p in P])}
        if N0:
            calc["nulles_au_moins_une_retenue"] = np.mean([any(p[1][p[2]:]) for p in P])
        b = res[f"ebh_{lect}"]
        d = {x: (float(b[x]), float(y)) for x, y in calc.items() if abs(b[x] - y) > 1e-12}
        cel2.append({"cellule": f"K={K} τ={taux} k={k} n={n} ng={ng} δ={delta} biais={biais} M={M} N={N0} α={alpha} σ={effet}",
                     "lecture": lect, "parts_v5": {x: float(b[x]) for x in calc}, "differences": d})
        if d:
            diff2.append(cel2[-1])
bilan["chaine_entiere"] = {"cellules": 12, "repetitions": 40, "lectures": len(cel2), "differences": len(diff2),
                           "exemples": diff2[:5], "ecart_max_log_e_evaluer_contre_course": ecart_e,
                           "detail": cel2}

json.dump(bilan, open(SORTIE, "x"), indent=1, ensure_ascii=False)
for c in bilan["chaine_entiere"]["detail"]:
    print(c["lecture"], c["cellule"], {x: round(y, 3) for x, y in c["parts_v5"].items()}, c["differences"])
print({x: y for x, y in bilan["chaine_entiere"].items() if x != "detail"})
