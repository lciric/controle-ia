"""Calibrage des tolérances des gardes d'identité des sondes figées de P3 (code du plancher v3 de T0.7), v1.

Données synthétiques seulement (aucune activation réelle) : jetons gaussiens de largeur 4 096, spectre de covariance pris
sur les 200 directions de P3 (`spectre-200-directions.npy`, estimé depuis le fichier léger `701f73bd…`), signal de classe
ajouté aux jetons des exemples positifs. Recettes appelées telles quelles : `sondes.familles.entrainer`
(« difference_moyennes », « lineaire », réglages par défaut) et `sondes.evaluation.plancher_apparie`.

Mesure, pour chaque recette, l'écart relatif des poids refaits aux poids de référence :
- arithmétique du processeur : mêmes données, autre nombre de fils (OpenBLAS de numpy, torch) — sous-processus ;
- « carte » : bruit relatif par jeton r (norme L2 du jeton) de 1e-4, 1e-3, 1e-2 (ordre de grandeur d'écarts de noyaux en
  bfloat16, propagés dans le flux résiduel) ;
- fautes de données (artefacts) : un exemple retiré ; empan décalé d'un jeton ; autre couche (jetons indépendants de même
  spectre) ; autre découpage (20 % des exemples d'entraînement échangés).

    python calibrage_gardes_v1.py RACINE_SRC SORTIE.json [--fils N --cas CAS --sortie-npz F]
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path

import numpy as np

ICI = Path(__file__).resolve().parent
D = 4096


def spectre(concept: str) -> np.ndarray:
    s = np.load(ICI / "spectre-200-directions.npy")[0 if concept == "tromperie" else 1]
    tete = np.sort(np.asarray(s))[::-1][:150]                       # 150 premières valeurs (bien estimées)
    reste = D - tete.size
    trace_cible = float(np.sum(s))                                    # ≈ trace de Σ (moyenne de ‖w‖² sur 200 tirages)
    queue_tot = max(trace_cible - tete.sum(), 1e-3)
    k = np.arange(1, reste + 1, dtype=np.float64)
    queue = k ** -1.0
    queue *= queue_tot / queue.sum()
    queue = np.minimum(queue, tete[-1])
    return np.concatenate([tete, queue])


def donnees(concept: str, graine: int, n_ex: int, longueur: tuple, decalage: bool = False, autre_couche: bool = False):
    """Séquences (jetons × 4 096, simple précision comme l'extraction), étiquettes alternées, signal de classe ; tous les jetons
    tirés d'un coup (un seul produit matriciel)."""
    rng = np.random.default_rng(graine + (777 if autre_couche else 0))
    lam = spectre(concept)
    base = np.random.default_rng(12345 + (777 if autre_couche else 0))
    R = np.linalg.qr(base.standard_normal((D, D)))[0]
    mu = base.standard_normal(D) * 0.3
    signal = R[:, :8] @ (np.sqrt(lam[:8]) * base.standard_normal(8)) * 0.4
    longueurs = rng.integers(longueur[0], longueur[1] + 1, size=n_ex) + 1
    Z = rng.standard_normal((int(longueurs.sum()), D)) * np.sqrt(lam)
    X = (mu + Z @ R.T).astype(np.float32)
    seqs, y, debut = [], [], 0
    for i, L in enumerate(longueurs.tolist()):
        S = X[debut:debut + L].astype(np.float64) + (signal if i % 2 else 0.0)
        debut += L
        S = S[1:] if decalage else S[:-1]                             # empan décalé d'un jeton : autre jeton de bord
        seqs.append(np.ascontiguousarray(S, dtype=np.float32))
        y.append(i % 2)
    return seqs, np.array(y)


def sauver(seqs, y, chemin):
    np.savez(chemin, X=np.concatenate(seqs), L=np.array([len(s) for s in seqs]), y=y)


def charger(chemin):
    with np.load(chemin) as z:
        X, L, y = z["X"], z["L"], z["y"]
    bornes = np.concatenate([[0], np.cumsum(L)])
    return [np.array(X[a:b]) for a, b in zip(bornes[:-1], bornes[1:])], y


def bruit(seqs, r: float, graine: int):
    rng = np.random.default_rng(graine)
    out = []
    for s in seqs:
        s64 = s.astype(np.float64)
        e = rng.standard_normal(s.shape)
        e *= (r * np.linalg.norm(s64, axis=1, keepdims=True) / np.linalg.norm(e, axis=1, keepdims=True))
        out.append((s64 + e).astype(np.float32))
    return out


def recette(nom: str, seqs, y):
    from controle_ia.sondes.familles import Reglages, entrainer
    from controle_ia.sondes.evaluation import plancher_apparie
    if nom == "difference_moyennes":
        s = entrainer("difference_moyennes", "t", 15, seqs, y, "max")
        return np.asarray(s.w)[None, :], np.array([s.b])
    if nom == "lineaire":
        s = entrainer("lineaire", "e", 15, seqs, y, "max", 3748102503887961549 % (2 ** 63 - 1), Reglages())
        return np.asarray(s.w)[None, :], np.array([s.b])
    p = plancher_apparie("p-plancher", 15, seqs, "max", 50, 15354747260773600555 % (2 ** 63 - 1))
    return np.stack([q.w for q in p]), np.array([q.b for q in p])


def ecarts(W, B, W0, B0, mu_norme: float) -> dict:
    ew = np.linalg.norm(W - W0, axis=1) / np.linalg.norm(W0, axis=1)
    eb = np.abs(B - B0) / (np.abs(B0) + np.linalg.norm(W0, axis=1) * mu_norme)
    return {"ecart_w_max": float(ew.max()), "ecart_b_max": float(eb.max()), "identique": bool(np.array_equal(W, W0) and np.array_equal(B, B0))}


CAS = {"tromperie": dict(n_ex=478, longueur=(2, 8)), "enjeux": dict(n_ex=400, longueur=(20, 40))}
RECETTES = {"tromperie": ["difference_moyennes", "plancher"], "enjeux": ["lineaire", "plancher"]}


def un_cas(concept: str, fils: int, sortie_npz: str, entree: str):
    """Sous-processus : recettes de référence avec `fils` fils (OpenBLAS par l'environnement, torch par appel), sur les
    mêmes données (lues sur disque : le tirage ne dépend pas des fils)."""
    import torch
    torch.set_num_threads(fils)
    seqs, y = charger(entree)
    t = {}
    for r in RECETTES[concept]:
        W, B = recette(r, seqs, y)
        t[f"{r}_W"], t[f"{r}_B"] = W, B
    np.savez(sortie_npz, **t)


def main(argv):
    src, sortie = argv[0], Path(argv[1])
    sys.path.insert(0, src)
    if "--cas" in argv:
        i = argv.index("--cas")
        un_cas(argv[i + 1], int(argv[argv.index("--fils") + 1]), argv[argv.index("--sortie-npz") + 1], argv[argv.index("--entree") + 1])
        return 0
    res = {"debut": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "largeur": D, "cas": {}}
    for concept in ("tromperie", "enjeux"):
        t0 = time.perf_counter()
        ref, alt = sortie.parent / f"ref-{concept}.npz", sortie.parent / f"alt-{concept}.npz"
        seqs, y = donnees(concept, 1, **CAS[concept])
        entree = sortie.parent / f"donnees-{concept}.npz"
        sauver(seqs, y, entree)
        for fils, f in ((1, ref), (4, alt)):
            env = {**os.environ, "OPENBLAS_NUM_THREADS": str(fils), "OMP_NUM_THREADS": str(fils), "MKL_NUM_THREADS": str(fils)}
            subprocess.run([sys.executable, "-I", __file__, src, str(sortie), "--cas", concept, "--fils", str(fils),
                            "--sortie-npz", str(f), "--entree", str(entree)], check=True, env=env)
        zr, za = np.load(ref), np.load(alt)
        seqs, y = charger(entree)
        mu_norme = float(np.linalg.norm(np.concatenate([s.astype(np.float64) for s in seqs]).mean(axis=0)))
        nb_jetons = int(sum(len(s) for s in seqs))
        cas = {"jetons": nb_jetons, "exemples": len(seqs), "recettes": {}}
        for r in RECETTES[concept]:
            W0, B0 = zr[f"{r}_W"], zr[f"{r}_B"]
            m = {"fils_1_contre_4": ecarts(za[f"{r}_W"], za[f"{r}_B"], W0, B0, mu_norme)}
            for rr in (1e-4, 1e-3, 1e-2):
                m[f"carte_r{rr:g}"] = ecarts(*recette(r, bruit(seqs, rr, 9), y), W0, B0, mu_norme)
            m["artefact_un_exemple_retire"] = ecarts(*recette(r, seqs[:-2] + seqs[-1:], np.concatenate([y[:-2], y[-1:]])), W0, B0, mu_norme)
            s_dec, _ = donnees(concept, 1, decalage=True, **CAS[concept])
            m["artefact_empan_decale"] = ecarts(*recette(r, s_dec, y), W0, B0, mu_norme)
            s_c, _ = donnees(concept, 1, autre_couche=True, **CAS[concept])
            m["artefact_autre_couche"] = ecarts(*recette(r, s_c, y), W0, B0, mu_norme)
            rng = np.random.default_rng(5)
            idx = np.arange(len(seqs))
            k = len(seqs) // 5
            echange = rng.choice(len(seqs), size=k, replace=False)
            s_d, _ = donnees(concept, 2, **CAS[concept])
            seqs_d = [s_d[i] if i in set(echange.tolist()) else seqs[i] for i in idx]
            m["artefact_autre_decoupage_20pc"] = ecarts(*recette(r, seqs_d, y), W0, B0, mu_norme)
            cas["recettes"][r] = m
            print(concept, r, json.dumps(m), flush=True)
        cas["duree_s"] = round(time.perf_counter() - t0, 1)
        res["cas"][concept] = cas
    res["fin"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    sortie.write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
