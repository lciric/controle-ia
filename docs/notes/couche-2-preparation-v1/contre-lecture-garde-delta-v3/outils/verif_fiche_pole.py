"""Q2 : la fiche simulée (sujet partagé) est-elle la fiche de `pari_apparie.evaluer` (v41) ? Longueurs propres comprises.

Pour chaque essai : tirage par la loi du script (LoiSynthetique, partagé ou non, effet d'unité ou non ; LoiReelle sur
fichiers fabriqués), puis
  - côté script : `processus` → gardes, contrastes prolongés → minimum → première atteinte de log(m/α) ;
  - côté pôle : `evaluer({Bj: v_j}, {Bj: g_j}, delta, alpha, m)` sur les mêmes g_j (longueur n_garde) et v_j (longueur n).
On compare la trajectoire du minimum (écart maximal), l'instant d'arrêt, la promotion, le seuil.
Usage : python3 -I -B verif_fiche_pole.py SORTIE.json
"""
import importlib.util
import json
import math
import os
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))


def charger(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


sim = charger("sim_garde_v3", os.path.join(ICI, "copie_script", "sim_garde_v3.py"))
pole = charger("pari_apparie", os.path.join(ICI, "copie_pole", "pari_apparie.py"))


def un_essai(rng, loi, n, n_garde, k, delta, m, alpha, biais):
    # on rejoue exactement `processus`, en gardant g et v pour le pôle
    graine = int(rng.integers(0, 2**31))
    r1 = np.random.default_rng(graine)
    g, v = loi.tirer(r1, 1, n, n_garde, k, biais)
    r2 = np.random.default_rng(graine)
    gardes, contrastes = sim.processus(loi, r2, 1, n, n_garde, k, delta, biais, loi)
    mini = np.minimum(gardes.min(axis=0), contrastes.min(axis=0))[0]
    seuil = m / alpha
    idx = int(sim.premiere_atteinte(mini[None, :], seuil)[0])
    gg = g[0] if g.shape[1] == k else np.repeat(g[0], k, axis=0)
    vv = v[0] if v.shape[1] == k else np.repeat(v[0], k, axis=0)
    res = pole.evaluer({f"B{j}": [float(x) for x in vv[j]] for j in range(k)},
                       {f"B{j}": [float(x) for x in gg[j]] for j in range(k)}, delta, alpha=alpha, m=m)
    tp = np.array(res["trajectoire_log_min"])
    return {
        "ecart_max": float(np.abs(tp - mini).max()) if tp.shape == mini.shape else float("inf"),
        "meme_longueur": tp.shape == mini.shape,
        "arret_script": (idx if idx > 0 else None), "arret_pole": res["instant_d_arret"],
        "seuil_egal": math.log(seuil) == res["seuil_log"],
        "promue_pole": res["promue"],
    }


def main():
    rng = np.random.default_rng(np.random.SeedSequence(20261029 + 3))
    essais = []
    for i in range(800):
        n = int(rng.integers(5, 260))
        n_garde = int(rng.choice([n, int(rng.integers(3, 260))]))
        k = int(rng.integers(1, 4))
        delta = float(rng.choice([0.05, 0.10, 0.20]))
        m = int(rng.choice([1, 8]))
        alpha = float(rng.choice([0.05, 0.01]))
        K = int(rng.choice([3, 10]))
        Ks = int(rng.choice([3, 10]))
        taux = float(rng.choice([0.0, 0.01, 0.10]))
        partage = bool(rng.integers(0, 2))
        effet = float(rng.choice([0.0, 0.05, 0.2]))
        biais = float(rng.choice([0.0, 0.025]))
        ecart = float(rng.choice([0.10, 0.30]))
        loi = sim.LoiSynthetique(K, Ks, taux, 0.4, ecart, partage, effet)
        r = un_essai(rng, loi, n, n_garde, k, delta, m, alpha, biais)
        r |= {"n": n, "n_garde": n_garde, "k": k, "delta": delta, "m": m, "alpha": alpha, "loi": loi.nom(), "biais": biais}
        essais.append(r)
    # loi réelle : fichiers fabriqués (écarts extrêmes compris, pour l'écrêtage), k fichiers, rééchantillonnage
    for i in range(200):
        N = int(rng.integers(10, 200))
        k = int(rng.integers(1, 4))
        eg = [np.clip(rng.normal(0, 0.3, N), -1, 1) for _ in range(k)]
        for e in eg:
            e[rng.integers(0, N)] = -1.0
            e[rng.integers(0, N)] = 1.0
        ev = [np.clip(rng.normal(0.05, 0.3, N), -1, 1) for _ in range(k)]
        loi = sim.LoiReelle(eg, ev, bool(rng.integers(0, 2)))
        n = int(rng.integers(5, 300))
        n_garde = int(rng.choice([n, int(rng.integers(3, 300))]))
        delta = float(rng.choice([0.05, 0.10]))
        r = un_essai(rng, loi, n, n_garde, k, delta, 8, 0.05, float(rng.choice([0.0, 0.02])))
        r |= {"n": n, "n_garde": n_garde, "k": k, "delta": delta, "m": 8, "alpha": 0.05, "loi": loi.nom()}
        essais.append(r)
    bilan = {
        "essais": len(essais),
        "dont_longueurs_differentes": sum(e["n"] != e["n_garde"] for e in essais),
        "ecart_max_trajectoire": max(e["ecart_max"] for e in essais),
        "longueurs_differentes_de_trajectoire": sum(not e["meme_longueur"] for e in essais),
        "arrets_differents": sum(e["arret_script"] != e["arret_pole"] for e in essais),
        "seuils_differents": sum(not e["seuil_egal"] for e in essais),
        "promues_pole": sum(e["promue_pole"] for e in essais),
        "promues_pole_longueurs_differentes": sum(e["promue_pole"] and e["n"] != e["n_garde"] for e in essais),
        "lois_reelles": sum(e["loi"].startswith("reelle") for e in essais),
    }
    json.dump({"bilan": bilan, "essais": essais}, open(sys.argv[1], "w"), indent=1, ensure_ascii=False)
    print(json.dumps(bilan, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
