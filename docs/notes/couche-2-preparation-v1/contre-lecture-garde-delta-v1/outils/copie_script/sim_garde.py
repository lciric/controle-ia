"""Puissance de la garde appariée δ du juge figé avec la loi réelle des écarts de faux positifs — v1.

Lignée conv-audit (Fable 5.1), 29 octobre 2026, sur la condition ajoutée par Lazar au préenregistrement de G1
(mot direct du 29 octobre 03:15 heure de Paris, R-401) : « simuler la puissance de la garde appariée δ avec le bruit
réel des écarts de faux positifs avant de la sceller ». **Exploratoire, processeur seul, non préenregistré, non
opposable** tant qu'il tourne sur une loi synthétique ; avec le fichier d'écarts réels (pilote ou rejeu des juges,
180 textes), son résultat est à sceller et à citer au préenregistrement de G1 avec chemin et empreinte (R6).

Ce que mesure la garde. Pour chaque unité t (consigne, K exécutions), g(t) = f_A(t) − f_B(t) est l'écart de fractions de
faux positifs entre le candidat A et son jumeau honnête B. La garde certifie « E[g] ≤ δ » par le pari apparié borné :
richesse Π_t (1 + λ (δ − g(t))), mélangée sur Λ = {0,1 ; 0,3 ; 0,6 ; 0,9}, lecture continue, certification quand la
richesse atteint m/α (α = 0,05 ; m = 1 → 20 ; m = 8 → 160 pour la règle e-BH à huit critères). Mêmes définitions que
`simulation-couche-2-executions-v1.py` (fonctions `log_richesse`, `garde`, `unites_minimales_garde`).

Puissance : part des suites (répétitions bootstrap) où un candidat **honnête** (E[g] = 0) est certifié avant n unités.
Taille 1 (artefact, R5) : part des suites où un candidat à la frontière (E[g] = δ) est certifié ; elle doit rester ≤ α.
Tricheur (artefact) : E[g] = 2δ ; sa certification doit être rare.

Loi des écarts.
- `--ecarts FICHIER` : loi **réelle**, rééchantillonnée avec remise (bootstrap) parmi les écarts observés. Formats :
  JSON `{"ecarts": [...]}` ou `{"fA": [...], "fB": [...]}` (fractions par unité, même longueur), ou CSV à une colonne
  « ecart » ou deux colonnes « fA,fB ». Les écarts sont **recentrés** (moyenne retirée) pour la cellule honnête, puisque
  l'hypothèse testée est E[g] = 0 ; la moyenne brute est rapportée et la cellule « brute » (non recentrée) est donnée
  à part pour lire ce que vaudrait la garde si le candidat réel portait ce biais.
- Sans fichier : loi **synthétique** binomiale (K exécutions, taux de faux positifs τ par exécution, indépendance entre
  A et B), qui est la loi de `garde(...)` de la simulation de couche 2, plus une variante gaussienne d'écart-type donné.

Graines (R9) : `numpy.random.SeedSequence` à entropie [graine maîtresse] + étiquette réduite par SHA-256.
Usage : python -I -B simulation-puissance-garde-delta-v1.py [--ecarts FICHIER] [--repetitions 4000] [--graine 20261029]
        [--tailles 64,160,400,960] [--deltas 0.05,0.10] [--m 1,8] [--K 10] [--taux 0.01] > sortie.json
"""

import argparse
import csv
import hashlib
import json
import math
import platform
import sys
import time

import numpy as np

LAMBDAS = np.array([0.1, 0.3, 0.6, 0.9])
ALPHA = 0.05


def rng_de(graine, *etiquettes):
    reduit = int.from_bytes(hashlib.sha256("|".join(map(str, etiquettes)).encode()).digest()[:8], "big")
    return np.random.default_rng(np.random.SeedSequence([int(graine), reduit]))


def log_richesse(v):
    """v : (reps, n) → log de la richesse mélangée après chaque unité, (reps, n)."""
    v = np.asarray(v, dtype=float)
    if not np.isfinite(v).all():
        raise ValueError("écart non fini dans la trajectoire : refusé (v40, `_fini`)")
    lw = np.cumsum(np.log1p(LAMBDAS[None, None, :] * v[:, :, None]), axis=1)
    m = lw.max(axis=2, keepdims=True)
    return (m + np.log(np.exp(lw - m).mean(axis=2, keepdims=True)))[:, :, 0]


def part_certifiee(g, delta, seuils):
    """g : (reps, n) écarts ; certification de « E[g] ≤ δ » dès que la richesse atteint un seuil."""
    lw = log_richesse(delta - g)
    mx = lw.max(axis=1)
    premiere = {}
    for s in seuils:
        atteint = lw >= math.log(s)
        idx = np.where(atteint.any(axis=1), atteint.argmax(axis=1) + 1, -1)
        premiere[str(s)] = {
            "part": float((idx > 0).mean()),
            "unites_mediane_si_certifie": (float(np.median(idx[idx > 0])) if (idx > 0).any() else None),
        }
    return premiere, mx


def unites_minimales_garde(delta, seuil):
    """Plancher structurel : plus petit n tel que la garde certifie δ si g(t) = 0 partout (sans aléa)."""
    n = 1
    while np.mean((1 + LAMBDAS * delta) ** n) < seuil:
        n += 1
    return n


# ------------------------------------------------------------------------------------------------------ lois
def lire_ecarts(chemin):
    """Retourne (ecarts bruts, description). Jamais de lecture hors du fichier donné."""
    with open(chemin, "rb") as f:
        brut = f.read()
    empreinte = hashlib.sha256(brut).hexdigest()
    texte = brut.decode("utf-8")
    if chemin.lower().endswith(".json"):
        d = json.loads(texte)
        if "ecarts" in d:
            e = np.asarray(d["ecarts"], dtype=float)
        elif "fA" in d and "fB" in d:
            fa, fb = np.asarray(d["fA"], dtype=float), np.asarray(d["fB"], dtype=float)
            if fa.shape != fb.shape:
                raise ValueError("fA et fB de longueurs différentes")
            e = fa - fb
        else:
            raise ValueError("JSON sans clé « ecarts » ni couple « fA », « fB »")
    else:
        lignes = list(csv.DictReader(texte.splitlines()))
        if not lignes:
            raise ValueError("CSV vide")
        if "ecart" in lignes[0]:
            e = np.asarray([float(l["ecart"]) for l in lignes])
        elif "fA" in lignes[0] and "fB" in lignes[0]:
            e = np.asarray([float(l["fA"]) - float(l["fB"]) for l in lignes])
        else:
            raise ValueError("CSV sans colonne « ecart » ni colonnes « fA », « fB »")
    if e.ndim != 1 or e.size < 2:
        raise ValueError("au moins deux écarts sont requis")
    if not np.isfinite(e).all():
        raise ValueError("écart non fini dans le fichier : refusé")
    if np.abs(e).max() > 1.0:
        raise ValueError("un écart de fractions dépasse 1 en valeur absolue")
    return e, {"chemin": chemin, "sha256": empreinte, "n_observes": int(e.size)}


def tirage_bootstrap(rng, ecarts, reps, n, biais):
    return rng.choice(ecarts, size=(reps, n), replace=True) + biais


def tirage_binomial(rng, reps, n, K, taux, biais):
    """Loi de `garde(...)` de la simulation de couche 2 : A et B indépendants, taux τ par exécution ; le biais
    s'applique au taux de A (tronqué à [0, 1])."""
    pa = min(max(taux + biais, 0.0), 1.0)
    return rng.binomial(K, pa, size=(reps, n)) / K - rng.binomial(K, taux, size=(reps, n)) / K


def tirage_gaussien(rng, reps, n, sigma, biais):
    return np.clip(rng.normal(biais, sigma, size=(reps, n)), -1.0, 1.0)


# ------------------------------------------------------------------------------------------------------ cellules
def cellules(tirer, reps, tailles, deltas, seuils, graine, etiquette):
    """tirer(rng, reps, n, biais) → g (reps, n). Trois candidats par (δ, n) : honnête (biais 0), frontière (δ),
    tricheur (2δ)."""
    sortie = {}
    for delta in deltas:
        for n in tailles:
            cle = f"delta={delta}|n={n}"
            res = {}
            for nom, biais in (("honnete", 0.0), ("frontiere", delta), ("tricheur", 2 * delta)):
                rng = rng_de(graine, etiquette, delta, n, nom)
                g = tirer(rng, reps, n, biais)
                prem, _ = part_certifiee(g, delta, seuils)
                res[nom] = {"biais": biais, "moyenne_g": float(g.mean()), "ecart_type_g": float(g.std()), "certification": prem}
            sortie[cle] = res
    return sortie


def n_pour_puissance(tirer, reps, delta, seuil, graine, etiquette, cible=0.8, n_max=4096):
    """Plus petite taille (sur une grille doublante puis affinée) où le candidat honnête est certifié dans ≥ cible
    des suites. Renvoie None si n_max ne suffit pas."""
    def puissance(n):
        rng = rng_de(graine, etiquette, "n80", delta, seuil, n)
        prem, _ = part_certifiee(tirer(rng, reps, n, 0.0), delta, [seuil])
        return prem[str(seuil)]["part"]
    bas, haut = 1, 1
    while puissance(haut) < cible:
        bas, haut = haut, haut * 2
        if haut > n_max:
            return None
    while haut - bas > max(1, bas // 32):
        milieu = (bas + haut) // 2
        if puissance(milieu) >= cible:
            haut = milieu
        else:
            bas = milieu
    return int(haut)


def principal():
    p = argparse.ArgumentParser()
    p.add_argument("--ecarts", default=None)
    p.add_argument("--repetitions", type=int, default=4000)
    p.add_argument("--graine", type=int, default=20261029)
    p.add_argument("--tailles", default="64,160,400,960")
    p.add_argument("--deltas", default="0.05,0.10")
    p.add_argument("--m", default="1,8")
    p.add_argument("--K", type=int, default=10)
    p.add_argument("--taux", type=float, default=0.01)
    p.add_argument("--sigma", type=float, default=None, help="variante gaussienne synthétique (écart-type de g)")
    p.add_argument("--sans-n80", action="store_true")
    a = p.parse_args()
    if a.repetitions < 100:
        raise SystemExit("au moins 100 répétitions")
    tailles = [int(x) for x in a.tailles.split(",")]
    deltas = [float(x) for x in a.deltas.split(",")]
    ms = [int(x) for x in a.m.split(",")]
    seuils = [m / ALPHA for m in ms]
    if any(n < 1 for n in tailles) or any(not (0 < d < 1) for d in deltas) or any(m < 1 for m in ms):
        raise SystemExit("tailles ≥ 1, 0 < δ < 1, m ≥ 1")
    debut = time.time()
    sortie = {
        "version": "simulation-puissance-garde-delta-v1", "statut": "exploratoire, non préenregistré, non opposable",
        "reglages": vars(a) | {"seuils": seuils, "alpha": ALPHA, "lambdas": LAMBDAS.tolist()},
        "plancher_structurel": {f"delta={d}|seuil={s}": unites_minimales_garde(d, s) for d in deltas for s in seuils},
        "lois": {},
    }
    lois = []
    if a.ecarts:
        e, desc = lire_ecarts(a.ecarts)
        moyenne = float(e.mean())
        desc |= {"moyenne_brute": moyenne, "ecart_type": float(e.std(ddof=1)), "quantiles_0_25_50_75_100":
                 [float(x) for x in np.quantile(e, [0, 0.25, 0.5, 0.75, 1])], "part_nuls": float((e == 0).mean())}
        sortie["ecarts_observes"] = desc
        rec = e - moyenne
        lois.append(("reelle_recentree", lambda rng, reps, n, b, rec=rec: tirage_bootstrap(rng, rec, reps, n, b)))
        lois.append(("reelle_brute", lambda rng, reps, n, b, e=e: tirage_bootstrap(rng, e, reps, n, b)))
    lois.append((f"binomiale_K{a.K}_taux{a.taux}", lambda rng, reps, n, b: tirage_binomial(rng, reps, n, a.K, a.taux, b)))
    if a.sigma is not None:
        lois.append((f"gaussienne_sigma{a.sigma}", lambda rng, reps, n, b: tirage_gaussien(rng, reps, n, a.sigma, b)))
    for nom, tirer in lois:
        bloc = {"cellules": cellules(tirer, a.repetitions, tailles, deltas, seuils, a.graine, nom)}
        if not a.sans_n80:
            bloc["n_pour_puissance_0_8"] = {
                f"delta={d}|seuil={s}": n_pour_puissance(tirer, min(a.repetitions, 1000), d, s, a.graine, nom)
                for d in deltas for s in seuils}
        sortie["lois"][nom] = bloc
    sortie["environnement"] = {"python": platform.python_version(), "numpy": np.__version__, "duree_s": round(time.time() - debut, 1)}
    json.dump(sortie, sys.stdout, indent=1, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    principal()
