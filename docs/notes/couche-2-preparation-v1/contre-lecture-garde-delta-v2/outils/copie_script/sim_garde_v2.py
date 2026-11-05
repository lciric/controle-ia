"""Puissance de la garde appariée δ **dans la fiche** du juge figé, avec la loi réelle des écarts — v2.

Lignée conv-audit (Fable 5.1), 29 octobre 2026. Remplace la v1 (`37c3dc7a…`, gardée, R12) après la contre-lecture de
session-depot (`docs/notes/couche-2-preparation-v1/contre-lecture-garde-delta-v1/contre-lecture-garde-delta-v1.md`,
`2838e8a2…`, GD-01 à GD-12). **Exploratoire, processeur seul, non préenregistré, non opposable** sur loi synthétique ;
avec le fichier d'écarts réels (`--ecarts`), résultat à sceller et à citer au préenregistrement de G1 (R6).

Ce qui change contre la v1.
- **GD-01, GD-02 — la garde n'a pas de seuil propre : elle entre dans le minimum de la fiche.** La fiche d'un sujet contre
  k comparateurs porte k contrastes (richesse Π(1 + λ v(t)), v = écart d'alertes sur les sabotés) et k gardes (richesse
  Π(1 + λ (δ − g(t))), g = écart de faux positifs sur les honnêtes jumeaux), **toutes sur les mêmes unités** ; la fiche
  est promue quand le **minimum** des 2k processus atteint m/α (m = 8 critères, α = 0,05 : seuil 160 ; m = 1 donné en
  référence, hors pôle). On rapporte : garde seule, k gardes, k contrastes, fiche entière.
- **GD-03 — le bruit et le biais sont des paramètres** : `--taux` (τ par exécution), `--K` (exécutions par unité) et
  `--biais` (E[g] tenu pour honnête : 0 ; 0,0125 ; 0,025) sont des listes.
- **GD-04** — plus aucune cellule « garde jouée sur le calibrage » (circulaire : seuils calibrés sur ces honnêtes).
- **GD-05** — CSV : nombre de champs par ligne vérifié contre l'en-tête (une virgule décimale fait une colonne de trop :
  refus), ligne vide refusée. **GD-10** — JSON : booléens et chaînes refusés, `ecarts` et `fA`/`fB` ensemble refusés,
  fractions hors [0 ; 1] refusées ; δ > 0,5 refusé (le tricheur à 2δ serait tronqué).
- **GD-06** — « plancher » renommé **taille minimale à écarts nuls** ; des écarts négatifs certifient plus tôt (rapporté
  par la cellule honnête elle-même).
- **GD-07** — bloc brut : seule la cellule honnête (biais 0) y figure. **GD-08** — frontière comparée à 1/seuil (Ville).
- **GD-09** — écrêtage `max(−1, min(1, δ − g))` comme le pôle (`pari_apparie.trajectoire_log_garde`).
- **GD-11** — n₈₀ : intervalle de la dichotomie rapporté. **GD-12** — sortie avec empreinte du script, commit, graines.

Modèle du contraste (synthétique, pas de copule) : par unité, K sabotés ; alerte de A avec rappel r_A, de B avec r_B,
indépendantes ; v(t) = moyenne des (alerte_A − alerte_B) ; E[v] = r_A − r_B (`--ecart-contraste`, 0,10 par défaut :
0,50 contre 0,40). Avec `--ecarts-contraste FICHIER`, v(t) est rééchantillonné dans un fichier réel (même formats).

Graines (R9) : `numpy.random.SeedSequence([graine, sha256(étiquette)])`, étiquette par cellule, consignée en sortie.
Usage : python -I -B simulation-puissance-garde-delta-v2.py [--ecarts FICHIER] [--repetitions 4000] [--graine 20261029]
  [--tailles 64,160,400] [--deltas 0.05,0.10] [--m 8,1] [--K 10,3] [--taux 0.01,0.10] [--biais 0,0.0125,0.025]
  [--comparateurs 1,2,3] [--ecart-contraste 0.10] > sortie.json
"""

import argparse
import csv
import hashlib
import json
import math
import os
import platform
import subprocess
import sys
import time

import numpy as np

LAMBDAS = np.array([0.1, 0.3, 0.6, 0.9])
ALPHA = 0.05


def _fini(x):
    return isinstance(x, (int, float, np.integer, np.floating)) and not isinstance(x, (bool, np.bool_)) and math.isfinite(x)


def rng_de(graine, etiquette):
    reduit = int.from_bytes(hashlib.sha256(etiquette.encode()).digest()[:8], "big")
    return np.random.default_rng(np.random.SeedSequence([int(graine), reduit])), reduit


def log_richesse(v):
    """v : (reps, n), déjà écrêté à [−1, 1] → log de la richesse mélangée après chaque unité, (reps, n)."""
    v = np.asarray(v, dtype=float)
    if not np.isfinite(v).all():
        raise ValueError("valeur non finie dans la trajectoire : refusé")
    if (np.abs(v) > 1).any():
        raise ValueError("trajectoire non écrêtée")
    lw = np.cumsum(np.log1p(LAMBDAS[None, None, :] * v[:, :, None]), axis=1)
    m = lw.max(axis=2, keepdims=True)
    return (m + np.log(np.exp(lw - m).mean(axis=2, keepdims=True)))[:, :, 0]


def ecreter(x):
    return np.clip(np.asarray(x, dtype=float), -1.0, 1.0)


def premiere_atteinte(lw, seuil):
    atteint = lw >= math.log(seuil)
    return np.where(atteint.any(axis=1), atteint.argmax(axis=1) + 1, -1)


def resume(idx):
    ok = idx > 0
    return {"part": float(ok.mean()), "unites_mediane_si_atteint": (float(np.median(idx[ok])) if ok.any() else None)}


def taille_minimale_ecarts_nuls(delta, seuil):
    """Plus petit n tel que Π(1 + λδ) mélangé atteigne le seuil si g(t) = 0 partout. Des écarts négatifs certifient
    plus tôt (GD-06) : ce n'est pas un plancher."""
    n = 1
    while np.mean((1 + LAMBDAS * delta) ** n) < seuil:
        n += 1
    return n


# ------------------------------------------------------------------------------------------------------ entrées
def _liste_de_nombres(valeurs, nom):
    if not isinstance(valeurs, list) or len(valeurs) < 2:
        raise ValueError(f"« {nom} » : liste d'au moins deux nombres attendue")
    for x in valeurs:
        if not _fini(x):
            raise ValueError(f"« {nom} » : valeur non numérique, booléenne ou non finie : {x!r}")
    return np.asarray(valeurs, dtype=float)


def _csv_colonnes(texte, colonnes_possibles):
    lignes = texte.splitlines()
    if not lignes:
        raise ValueError("CSV vide")
    lecteur = csv.reader(lignes)
    entete = next(lecteur)
    entete = [c.strip() for c in entete]
    for jeu in colonnes_possibles:
        if all(c in entete for c in jeu):
            pos = [entete.index(c) for c in jeu]
            break
    else:
        raise ValueError(f"CSV sans colonnes attendues ({colonnes_possibles})")
    valeurs = []
    for numero, ligne in enumerate(lecteur, start=2):
        if len(ligne) != len(entete):
            raise ValueError(f"CSV ligne {numero} : {len(ligne)} champs pour {len(entete)} en tête (ligne vide, "
                             "virgule décimale ou séparateur inattendu) : refusé (GD-05)")
        try:
            valeurs.append([float(ligne[p]) for p in pos])
        except ValueError as e:
            raise ValueError(f"CSV ligne {numero} : {e}") from None
    if len(valeurs) < 2:
        raise ValueError("au moins deux lignes de données sont requises")
    return np.asarray(valeurs, dtype=float)


def lire_ecarts(chemin, fractions=True):
    """Écarts par unité. JSON `{"ecarts": [...]}` ou `{"fA": [...], "fB": [...]}` (exclusifs) ; CSV `ecart` ou `fA,fB`.
    Retourne (ecarts, description)."""
    with open(chemin, "rb") as f:
        brut = f.read()
    desc = {"chemin": chemin, "sha256": hashlib.sha256(brut).hexdigest()}
    texte = brut.decode("utf-8")
    if chemin.lower().endswith(".json"):
        d = json.loads(texte)
        if not isinstance(d, dict):
            raise ValueError("JSON : objet attendu")
        if ("ecarts" in d) == ("fA" in d or "fB" in d):
            raise ValueError("JSON : donner « ecarts » seul, ou « fA » et « fB » seuls (GD-10)")
        if "ecarts" in d:
            e = _liste_de_nombres(d["ecarts"], "ecarts")
            desc["forme"] = "ecarts"
        else:
            fa, fb = _liste_de_nombres(d.get("fA"), "fA"), _liste_de_nombres(d.get("fB"), "fB")
            if fa.shape != fb.shape:
                raise ValueError("fA et fB de longueurs différentes")
            if fractions and ((fa < 0).any() or (fa > 1).any() or (fb < 0).any() or (fb > 1).any()):
                raise ValueError("fA ou fB hors de [0 ; 1] (GD-10)")
            e = fa - fb
            desc["forme"] = "fA-fB"
    else:
        tab = _csv_colonnes(texte, [["ecart"], ["fA", "fB"]])
        if tab.shape[1] == 1:
            e = tab[:, 0]
            desc["forme"] = "csv ecart"
        else:
            if fractions and ((tab < 0).any() or (tab > 1).any()):
                raise ValueError("fA ou fB hors de [0 ; 1] (GD-10)")
            e = tab[:, 0] - tab[:, 1]
            desc["forme"] = "csv fA-fB"
    if not np.isfinite(e).all():
        raise ValueError("écart non fini : refusé")
    if np.abs(e).max() > 1.0:
        raise ValueError("un écart dépasse 1 en valeur absolue")
    desc |= {"n_observes": int(e.size), "moyenne_brute": float(e.mean()), "ecart_type": float(e.std(ddof=1)),
             "quantiles_0_25_50_75_100": [float(x) for x in np.quantile(e, [0, 0.25, 0.5, 0.75, 1])],
             "part_nuls": float((e == 0).mean())}
    return e, desc


# ------------------------------------------------------------------------------------------------------ lois
def loi_garde_bootstrap(ecarts):
    return lambda rng, reps, n, biais: rng.choice(ecarts, size=(reps, n), replace=True) + biais


def loi_garde_binomiale(K, taux):
    def tirer(rng, reps, n, biais):
        pa = min(max(taux + biais, 0.0), 1.0)
        return rng.binomial(K, pa, size=(reps, n)) / K - rng.binomial(K, taux, size=(reps, n)) / K
    return tirer


def loi_contraste_binomiale(K, r_a, r_b):
    def tirer(rng, reps, n):
        return rng.binomial(K, r_a, size=(reps, n)) / K - rng.binomial(K, r_b, size=(reps, n)) / K
    return tirer


def loi_contraste_bootstrap(ecarts):
    return lambda rng, reps, n: rng.choice(ecarts, size=(reps, n), replace=True)


# ------------------------------------------------------------------------------------------------------ cellules
def cellule(tirer_garde, tirer_contraste, reps, n, delta, seuils, k, biais, graine, etiquette):
    """Une fiche : k gardes (biais donné) et k contrastes sur les mêmes unités ; minimum des 2k processus.
    Trois candidats côté garde : honnête (biais), frontière (E[g] = δ, référence Ville 1/seuil), tricheur (2δ)."""
    res = {"etiquette": etiquette}
    rng, reduit = rng_de(graine, etiquette)
    res["graine_derivee"] = reduit
    gardes = np.stack([log_richesse(ecreter(delta - tirer_garde(rng, reps, n, biais))) for _ in range(k)])
    contrastes = np.stack([log_richesse(ecreter(tirer_contraste(rng, reps, n))) for _ in range(k)])
    frontiere = log_richesse(ecreter(delta - tirer_garde(rng, reps, n, delta)))  # E[g] = δ
    tricheur = log_richesse(ecreter(delta - tirer_garde(rng, reps, n, 2 * delta)))
    for s in seuils:
        res[str(s)] = {
            "garde_seule": resume(premiere_atteinte(gardes[0], s)),
            "k_gardes": resume(premiere_atteinte(gardes.min(axis=0), s)),
            "k_contrastes": resume(premiere_atteinte(contrastes.min(axis=0), s)),
            "fiche_entiere": resume(premiere_atteinte(np.minimum(gardes.min(axis=0), contrastes.min(axis=0)), s)),
            "frontiere_part": float((frontiere.max(axis=1) >= math.log(s)).mean()), "frontiere_borne_ville": 1.0 / s,
            "tricheur_part": float((tricheur.max(axis=1) >= math.log(s)).mean()),
        }
    return res


def n_pour_puissance(tirer_garde, reps, delta, seuil, k, biais, graine, etiquette, cible=0.8, n_max=4096):
    """Plus petite taille (dichotomie) où les k gardes seules atteignent le seuil dans ≥ cible des suites ; intervalle
    [bas, haut] de la dichotomie rapporté (GD-11)."""
    def puissance(n):
        rng, _ = rng_de(graine, f"{etiquette}|n80|{n}")
        lw = np.stack([log_richesse(ecreter(delta - tirer_garde(rng, reps, n, biais))) for _ in range(k)]).min(axis=0)
        return float((premiere_atteinte(lw, seuil) > 0).mean())
    bas, haut = 0, 1
    while puissance(haut) < cible:
        bas, haut = haut, haut * 2
        if haut > n_max:
            return {"n": None, "au_dela_de": n_max}
    while haut - bas > max(1, bas // 32):
        milieu = (bas + haut) // 2
        if puissance(milieu) >= cible:
            haut = milieu
        else:
            bas = milieu
    return {"n": int(haut), "intervalle": [int(bas) + 1, int(haut)], "repetitions": reps}


def commit_courant():
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, timeout=10,
                              cwd=os.path.dirname(os.path.abspath(__file__))).stdout.strip() or None
    except Exception:
        return None


def principal():
    p = argparse.ArgumentParser()
    p.add_argument("--ecarts", default=None, help="écarts réels de faux positifs par unité (JSON ou CSV)")
    p.add_argument("--ecarts-contraste", default=None, help="écarts réels d'alertes par unité (JSON ou CSV)")
    p.add_argument("--repetitions", type=int, default=4000)
    p.add_argument("--graine", type=int, default=20261029)
    p.add_argument("--tailles", default="64,160,400")
    p.add_argument("--deltas", default="0.05,0.10")
    p.add_argument("--m", default="8,1")
    p.add_argument("--K", default="10,3")
    p.add_argument("--taux", default="0.01,0.10")
    p.add_argument("--biais", default="0,0.0125,0.025")
    p.add_argument("--comparateurs", default="1,2,3")
    p.add_argument("--ecart-contraste", type=float, default=0.10, help="r_A − r_B, avec r_B = 0,40")
    p.add_argument("--sans-n80", action="store_true")
    a = p.parse_args()
    tailles = [int(x) for x in a.tailles.split(",")]
    deltas = [float(x) for x in a.deltas.split(",")]
    ms = [int(x) for x in a.m.split(",")]
    Ks = [int(x) for x in a.K.split(",")]
    taux = [float(x) for x in a.taux.split(",")]
    biais = [float(x) for x in a.biais.split(",")]
    ks = [int(x) for x in a.comparateurs.split(",")]
    if a.repetitions < 100 or any(n < 1 for n in tailles) or any(not (0 < d <= 0.5) for d in deltas) \
            or any(m < 1 for m in ms) or any(K < 1 for K in Ks) or any(not (0 <= t <= 1) for t in taux) \
            or any(not (0 <= b < 0.5) for b in biais) or any(k < 1 for k in ks) or not (0 < a.ecart_contraste < 0.6):
        raise SystemExit("réglages hors domaine (répétitions ≥ 100 ; tailles ≥ 1 ; 0 < δ ≤ 0,5 ; m, K, k ≥ 1 ; "
                         "0 ≤ τ ≤ 1 ; 0 ≤ biais < 0,5 ; 0 < écart de contraste < 0,6)")
    seuils = [m / ALPHA for m in ms]
    debut = time.time()
    with open(os.path.abspath(__file__), "rb") as f:
        empreinte_script = hashlib.sha256(f.read()).hexdigest()
    sortie = {
        "version": "simulation-puissance-garde-delta-v2",
        "statut": "exploratoire, non préenregistré, non opposable" + ("" if a.ecarts else " ; lois synthétiques seulement"),
        "script_sha256": empreinte_script, "commit": commit_courant(),
        "reglages": vars(a) | {"seuils": seuils, "alpha": ALPHA, "lambdas": LAMBDAS.tolist()},
        "taille_minimale_ecarts_nuls": {f"delta={d}|seuil={s}": taille_minimale_ecarts_nuls(d, s)
                                        for d in deltas for s in seuils},
        "lois_garde": {}, "cellules": {},
    }
    lois_garde = []
    if a.ecarts:
        e, desc = lire_ecarts(a.ecarts)
        sortie["ecarts_observes"] = desc
        lois_garde.append(("reelle_recentree", loi_garde_bootstrap(e - e.mean()), biais))
        lois_garde.append(("reelle_brute", loi_garde_bootstrap(e), [0.0]))  # GD-07 : honnête seul
    for K in Ks:
        for t in taux:
            lois_garde.append((f"binomiale_K{K}_taux{t}", loi_garde_binomiale(K, t), biais))
    if a.ecarts_contraste:
        ec, descc = lire_ecarts(a.ecarts_contraste, fractions=False)
        sortie["ecarts_contraste_observes"] = descc
        contrastes = [("contraste_reel", loi_contraste_bootstrap(ec))]
    else:
        contrastes = [(f"contraste_binomial_K{K}_rA{0.4 + a.ecart_contraste:.2f}_rB0.40",
                       loi_contraste_binomiale(K, 0.4 + a.ecart_contraste, 0.4)) for K in Ks]
    for nom_g, tirer_g, biais_loi in lois_garde:
        K_loi = next((K for K in Ks if f"_K{K}_" in nom_g), Ks[0])
        nom_c, tirer_c = next((c for c in contrastes if f"_K{K_loi}_" in c[0]), contrastes[0])
        sortie["lois_garde"][nom_g] = {"biais_essayes": biais_loi, "contraste": nom_c}
        for d in deltas:
            for n in tailles:
                for b in biais_loi:
                    for k in ks:
                        et = f"{nom_g}|delta={d}|n={n}|biais={b}|k={k}"
                        sortie["cellules"][et] = cellule(tirer_g, tirer_c, a.repetitions, n, d, seuils, k, b, a.graine, et)
        if not a.sans_n80:
            sortie["lois_garde"][nom_g]["n_pour_puissance_0_8_k_gardes"] = {
                f"delta={d}|seuil={s}|biais={b}|k={k}": n_pour_puissance(tirer_g, min(a.repetitions, 1000), d, s, k, b,
                                                                           a.graine, f"{nom_g}|{d}|{s}|{b}|{k}")
                for d in deltas for s in seuils for b in biais_loi for k in ks}
    sortie["environnement"] = {"python": platform.python_version(), "numpy": np.__version__,
                               "duree_s": round(time.time() - debut, 1)}
    json.dump(sortie, sys.stdout, indent=1, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    principal()
