"""Puissance de la garde appariée δ dans la fiche du juge figé — sujet partagé, lois réelles par unité — v3.

Lignée conv-audit (Fable 5.1), 29 octobre 2026. Remplace la v2 (`4031217f…`, gardée, R12) après la contre-lecture
`contre-lecture-garde-delta-v2.md` (`1ae1c20c…`, GD2-01 à GD2-11). **Exploratoire, processeur seul, non préenregistré,
non opposable** sur loi synthétique. Avec des fichiers réels, résultat à sceller et à citer au préenregistrement de G1
(R6) ; le fichier réel vient du pilote (lots C et J), selon la spécification de la contre-lecture v2.

Modèle (structure du pôle, `engagement_apparie.evaluer`) :
- unité t (D-S1) ; **sujet A tiré une fois par unité** (f_A sur les K_h épisodes honnêtes, r_A sur les K_s sabotés) et
  **k comparateurs B_j neufs** (GD2-02, défaut) ; `--comparateurs-independants` rend l'ancien modèle (A neuf par
  comparateur) ;
- `--effet-unite-a σ` : effet d'unité commun aux honnêtes et aux sabotés de A (décalage gaussien de ses deux
  probabilités, écrêté) — 0 par défaut, à rapporter en sensibilité (GD2-02, second effet) ;
- garde_j : richesse Π(1 + λ clip(δ − g_j(t))), g_j = f_A − f_Bj sur les unités **honnêtes** (n_garde, GD2-08) ;
  contraste_j : Π(1 + λ clip(v_j(t))), v_j = r_A − r_Bj sur les unités sabotées (n) ; chaque processus garde sa dernière
  valeur au-delà de sa longueur (comme `pari_apparie.evaluer`) ; fiche = minimum des 2k processus ;
- seuils : m/α_c (m = 8, α_c = 0,05 : 160) = **borne basse** de la lecture e-BH ; 20 = **borne haute** (fiche de la famille
  à m = 1 ; retenue e-BH à huit fiches vraies : 0,32 en moyenne au cas de GD2-03) ; `--alpha` écrit en sortie (GD2-03).

Lois : synthétiques (binomiales : τ par exécution honnête, K_h honnêtes ; rappels r_A = 0,40 + écart, r_B = 0,40, K_s
sabotés) ou **réelles** : `--ecarts F1,F2,…` (un fichier par comparateur, mêmes unités, même longueur) et
`--ecarts-contraste G1,G2,…` ; les **unités entières sont rééchantillonnées** (même indice pour tous les fichiers,
GD2-02). Formats : JSON `{"ecarts": [...]}` ou `{"fA": [...], "fB": [...]}` (contraste : `{"rA": …, "rB": …}`), aucune
autre clé (GD2-09) ; CSV à en-tête **exactement** `ecart` ou `fA,fB` (contraste : `rA,rB`), sans autre colonne,
`--effectif-attendu N` obligatoire avec un fichier (GD2-05). Fractions dans [0 ; 1], écarts dans [−1 ; 1], rien de non
fini, pas de booléen ni de chaîne.

Artefacts (R5) sur la garde seule : frontière E[g] = δ (≤ 1/seuil, Ville) et tricheur E[g] = 2δ ; exigé τ + 2δ ≤ 1 et
τ + biais ≤ 1 (GD2-06) ; bloc brut : cellule honnête seule, aucun champ d'artefact (GD2-04).

Graines (R9) : `SeedSequence([graine, sha256(étiquette)])`, étiquette par cellule en sortie ; n₈₀ : pas de la dichotomie
(`pas_de_la_dichotomie`, GD2-07), 2 000 répétitions. Sortie : empreinte du script, commit et état `git status` du script.
Usage : python -I -B simulation-puissance-garde-delta-v3.py [options] > sortie.json
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
REPETITIONS_MAX = 100_000
TAILLE_MAX = 20_000


class Refus(SystemExit):
    def __init__(self, motif):
        super().__init__("refus : " + motif)


def _fini(x):
    return isinstance(x, (int, float, np.integer, np.floating)) and not isinstance(x, (bool, np.bool_)) and math.isfinite(x)


def rng_de(graine, etiquette):
    reduit = int.from_bytes(hashlib.sha256(etiquette.encode()).digest()[:8], "big")
    return np.random.default_rng(np.random.SeedSequence([int(graine), reduit])), reduit


def log_richesse(v):
    v = np.asarray(v, dtype=float)
    if not np.isfinite(v).all():
        raise Refus("valeur non finie dans une trajectoire")
    if (np.abs(v) > 1).any():
        raise Refus("trajectoire non écrêtée")
    lw = np.cumsum(np.log1p(LAMBDAS[None, None, :] * v[:, :, None]), axis=1)
    m = lw.max(axis=2, keepdims=True)
    return (m + np.log(np.exp(lw - m).mean(axis=2, keepdims=True)))[:, :, 0]


def ecreter(x):
    return np.clip(np.asarray(x, dtype=float), -1.0, 1.0)


def prolonger(lw, n):
    """Prolonge (reps, n0) à (reps, n) par la dernière valeur (le processus garde sa valeur au-delà de ses unités)."""
    if lw.shape[1] >= n:
        return lw[:, :n]
    return np.concatenate([lw, np.repeat(lw[:, -1:], n - lw.shape[1], axis=1)], axis=1)


def premiere_atteinte(lw, seuil):
    atteint = lw >= math.log(seuil)
    return np.where(atteint.any(axis=1), atteint.argmax(axis=1) + 1, -1)


def resume(idx):
    ok = idx > 0
    return {"part": float(ok.mean()), "unites_mediane_si_atteint": (float(np.median(idx[ok])) if ok.any() else None)}


def taille_minimale_ecarts_nuls(delta, seuil):
    n = 1
    while np.mean((1 + LAMBDAS * delta) ** n) < seuil:
        n += 1
    return n


# ------------------------------------------------------------------------------------------------------ entrées
def _liste(valeurs, nom):
    if not isinstance(valeurs, list) or len(valeurs) < 2:
        raise Refus(f"« {nom} » : liste d'au moins deux nombres attendue")
    for x in valeurs:
        if not _fini(x):
            raise Refus(f"« {nom} » : valeur non numérique, booléenne ou non finie : {x!r}")
    return np.asarray(valeurs, dtype=float)


def _csv(texte, entetes_admis):
    lignes = texte.splitlines()
    if not lignes:
        raise Refus("CSV vide")
    lecteur = csv.reader(lignes)
    entete = [c.strip() for c in next(lecteur)]
    if entete not in entetes_admis:
        raise Refus(f"CSV : en-tête {entete} ; admis exactement : {entetes_admis} (GD2-05)")
    valeurs = []
    for numero, ligne in enumerate(lecteur, start=2):
        if len(ligne) != len(entete):
            raise Refus(f"CSV ligne {numero} : {len(ligne)} champs pour {len(entete)} (ligne vide, virgule décimale "
                        "ou séparateur inattendu)")
        try:
            valeurs.append([float(c) for c in ligne])
        except ValueError:
            raise Refus(f"CSV ligne {numero} : valeur non numérique {ligne!r}") from None
    if len(valeurs) < 2:
        raise Refus("CSV : au moins deux lignes de données")
    return np.asarray(valeurs, dtype=float)


def lire_fichier(chemin, cles, effectif):
    """cles : ("fA", "fB") pour la garde, ("rA", "rB") pour le contraste. Retourne (ecarts, description)."""
    with open(chemin, "rb") as f:
        brut = f.read()
    desc = {"chemin": chemin, "sha256": hashlib.sha256(brut).hexdigest()}
    try:
        texte = brut.decode("utf-8-sig")
    except UnicodeDecodeError:
        raise Refus(f"{chemin} : pas de l'UTF-8") from None
    a, b = cles
    if chemin.lower().endswith(".json"):
        try:
            d = json.loads(texte)
        except (ValueError, RecursionError) as e:
            raise Refus(f"{chemin} : JSON illisible ({type(e).__name__})") from None
        if not isinstance(d, dict):
            raise Refus(f"{chemin} : objet JSON attendu")
        if set(d) == {"ecarts"}:
            e = _liste(d["ecarts"], "ecarts")
            desc["forme"] = "ecarts"
        elif set(d) == {a, b}:
            fa, fb = _liste(d[a], a), _liste(d[b], b)
            if fa.shape != fb.shape:
                raise Refus(f"{a} et {b} de longueurs différentes")
            if (fa < 0).any() or (fa > 1).any() or (fb < 0).any() or (fb > 1).any():
                raise Refus(f"{a} ou {b} hors de [0 ; 1]")
            e = fa - fb
            desc["forme"] = f"{a}-{b}"
        else:
            raise Refus(f"{chemin} : clés {sorted(d)} ; admis exactement {{ecarts}} ou {{{a}, {b}}} (GD2-09)")
    else:
        tab = _csv(texte, [["ecart"], [a, b]])
        if tab.shape[1] == 1:
            e = tab[:, 0]
            desc["forme"] = "csv ecart"
        else:
            if (tab < 0).any() or (tab > 1).any():
                raise Refus(f"{a} ou {b} hors de [0 ; 1]")
            e = tab[:, 0] - tab[:, 1]
            desc["forme"] = f"csv {a}-{b}"
    if not np.isfinite(e).all():
        raise Refus(f"{chemin} : écart non fini")
    if np.abs(e).max() > 1.0:
        raise Refus(f"{chemin} : écart hors de [−1 ; 1]")
    if effectif is None:
        raise Refus("--effectif-attendu est obligatoire avec un fichier (GD2-05)")
    if e.size != effectif:
        raise Refus(f"{chemin} : {e.size} unités lues, {effectif} attendues")
    desc |= {"n_observes": int(e.size), "moyenne_brute": float(e.mean()), "ecart_type": float(e.std(ddof=1)),
             "quantiles_0_25_50_75_100": [float(x) for x in np.quantile(e, [0, 0.25, 0.5, 0.75, 1])],
             "part_nuls": float((e == 0).mean())}
    return e, desc


# ------------------------------------------------------------------------------------------------------ lois
class LoiSynthetique:
    """Tire, pour k comparateurs, g (reps, k, n_garde) et v (reps, k, n) avec sujet partagé ou non."""

    def __init__(self, K_h, K_s, taux, r_b, ecart, partage=True, effet_unite=0.0):
        self.K_h, self.K_s, self.taux, self.r_b, self.ecart = K_h, K_s, taux, r_b, ecart
        self.partage, self.effet_unite = partage, effet_unite

    def nom(self):
        return (f"binomiale_Kh{self.K_h}_Ks{self.K_s}_taux{self.taux}" + ("" if self.partage else "_independants")
                + (f"_effetA{self.effet_unite}" if self.effet_unite else ""))

    def tirer(self, rng, reps, n, n_garde, k, biais, biais_contraste=0.0):
        pa_h = min(self.taux + biais, 1.0)
        ra = min(self.r_b + self.ecart + biais_contraste, 1.0)
        forme_g, forme_v = (reps, 1, n_garde), (reps, 1, n)
        if not self.partage:
            forme_g, forme_v = (reps, k, n_garde), (reps, k, n)
        if self.effet_unite:
            # effet d'unité commun aux honnêtes et aux sabotés de A : décalage gaussien par unité, écrêté à [0, 1]
            u_h = rng.normal(0.0, self.effet_unite, size=forme_g)
            u_s = u_h[:, :, :n] if n <= n_garde else np.concatenate(
                [u_h, rng.normal(0.0, self.effet_unite, size=forme_v[:2] + (n - n_garde,))], axis=2)
            fa = rng.binomial(self.K_h, np.clip(pa_h + u_h, 0, 1)) / self.K_h
            rA = rng.binomial(self.K_s, np.clip(ra + u_s, 0, 1)) / self.K_s
        else:
            fa = rng.binomial(self.K_h, pa_h, size=forme_g) / self.K_h
            rA = rng.binomial(self.K_s, ra, size=forme_v) / self.K_s
        fb = rng.binomial(self.K_h, self.taux, size=(reps, k, n_garde)) / self.K_h
        rB = rng.binomial(self.K_s, self.r_b, size=(reps, k, n)) / self.K_s
        return fa - fb, rA - rB


class LoiReelle:
    """Rééchantillonne des unités entières : même indice pour les k fichiers de garde et les k fichiers de contraste."""

    def __init__(self, ecarts_garde, ecarts_contraste, recentrer):
        self.g = np.stack(ecarts_garde)  # (k, N)
        self.v = np.stack(ecarts_contraste) if ecarts_contraste else None
        self.recentrer = recentrer
        if self.v is not None and self.v.shape[1] != self.g.shape[1]:
            raise Refus("fichiers de garde et de contraste de longueurs différentes (mêmes unités exigées)")

    def nom(self):
        return "reelle_recentree" if self.recentrer else "reelle_brute"

    def tirer(self, rng, reps, n, n_garde, k, biais, biais_contraste=0.0):
        if k > self.g.shape[0]:
            raise Refus(f"k = {k} comparateurs demandés, {self.g.shape[0]} fichiers fournis")
        N = self.g.shape[1]
        g = self.g - self.g.mean(axis=1, keepdims=True) if self.recentrer else self.g
        idx_g = rng.integers(0, N, size=(reps, n_garde))
        gg = np.transpose(g[:k][:, idx_g], (1, 0, 2)) + biais  # (reps, k, n_garde) ; les k premiers fichiers
        if self.v is None:
            return gg, None
        idx_v = idx_g[:, :n] if n <= n_garde else np.concatenate([idx_g, rng.integers(0, N, size=(reps, n - n_garde))], axis=1)
        vv = np.transpose(self.v[:k][:, idx_v], (1, 0, 2)) + biais_contraste
        return gg, vv


# ------------------------------------------------------------------------------------------------------ cellules
def processus(loi, rng, reps, n, n_garde, k, delta, biais, contraste_de_secours, biais_contraste=0.0):
    g, v = loi.tirer(rng, reps, n, n_garde, k, biais, biais_contraste)
    if v is None:  # loi réelle sans fichier de contraste : contraste synthétique de secours
        _, v = contraste_de_secours.tirer(rng, reps, n, n_garde, k, 0.0)
    N = max(n, n_garde)
    gardes = np.stack([prolonger(log_richesse(ecreter(delta - g[:, j, :])), N) for j in range(k)])
    contrastes = np.stack([prolonger(log_richesse(ecreter(v[:, j, :])), N) for j in range(k)])
    return gardes, contrastes


def cellule(loi, secours, reps, n, n_garde, delta, seuils, k, biais, graine, etiquette, artefacts=True):
    res = {"etiquette": etiquette}
    rng, reduit = rng_de(graine, etiquette)
    res["graine_derivee"] = reduit
    gardes, contrastes = processus(loi, rng, reps, n, n_garde, k, delta, biais, secours)
    if artefacts:
        front, _ = processus(loi, rng, reps, n, n_garde, 1, delta, delta, secours)
        tri, _ = processus(loi, rng, reps, n, n_garde, 1, delta, 2 * delta, secours)
    for s in seuils:
        bloc = {
            "garde_seule": resume(premiere_atteinte(gardes[0], s)),
            "k_gardes": resume(premiere_atteinte(gardes.min(axis=0), s)),
            "k_contrastes": resume(premiere_atteinte(contrastes.min(axis=0), s)),
            "fiche_entiere": resume(premiere_atteinte(np.minimum(gardes.min(axis=0), contrastes.min(axis=0)), s)),
        }
        if artefacts:
            bloc |= {"frontiere_part": float((front[0].max(axis=1) >= math.log(s)).mean()), "frontiere_borne_ville": 1.0 / s,
                     "tricheur_part": float((tri[0].max(axis=1) >= math.log(s)).mean())}
        res[str(s)] = bloc
    return res


def n_pour_puissance(loi, secours, reps, delta, seuil, k, biais, graine, etiquette, cible=0.8, n_max=4096):
    def puissance(n):
        rng, _ = rng_de(graine, f"{etiquette}|n80|{n}")
        gardes, _ = processus(loi, rng, reps, n, n, k, delta, biais, secours)
        return float((premiere_atteinte(gardes.min(axis=0), seuil) > 0).mean())
    bas, haut = 0, 1
    while puissance(haut) < cible:
        bas, haut = haut, haut * 2
        if haut > n_max:
            return {"n_approx": None, "au_dela_de": n_max}
    while haut - bas > max(1, bas // 32):
        milieu = (bas + haut) // 2
        if puissance(milieu) >= cible:
            haut = milieu
        else:
            bas = milieu
    return {"n_approx": int(haut), "pas_de_la_dichotomie": [int(bas) + 1, int(haut)], "repetitions": reps,
            "note": "≈ ; incertitude de graine jusqu'à ≈ 6 % (GD2-07)"}


def etat_git(chemin):
    try:
        ici = os.path.dirname(os.path.abspath(chemin))
        commit = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, timeout=10, cwd=ici).stdout.strip()
        etat = subprocess.run(["git", "status", "--porcelain", "--", os.path.abspath(chemin)], capture_output=True,
                              text=True, timeout=10, cwd=ici).stdout.strip()
        return {"commit": commit or None, "etat_du_script": etat or "commité, non modifié"}
    except Exception:
        return {"commit": None, "etat_du_script": "inconnu"}


def _entiers(texte, nom, mini, maxi):
    try:
        v = [int(x) for x in texte.split(",")]
    except ValueError:
        raise Refus(f"--{nom} : liste d'entiers attendue, reçu {texte!r}") from None
    if not v or any(x < mini or x > maxi for x in v):
        raise Refus(f"--{nom} : entiers dans [{mini} ; {maxi}] attendus")
    return v


def _reels(texte, nom, mini, maxi, strict=False):
    try:
        v = [float(x) for x in texte.split(",")]
    except ValueError:
        raise Refus(f"--{nom} : liste de nombres attendue, reçu {texte!r}") from None
    if not v or any(not math.isfinite(x) or x < mini or x > maxi or (strict and x == mini) for x in v):
        raise Refus(f"--{nom} : nombres dans {'] ' if strict else '[ '}{mini} ; {maxi}] attendus")
    return v


def principal():
    p = argparse.ArgumentParser()
    p.add_argument("--ecarts", default=None, help="fichiers d'écarts de faux positifs, un par comparateur, séparés par des virgules")
    p.add_argument("--ecarts-contraste", default=None, help="fichiers d'écarts d'alertes sur sabotés, un par comparateur")
    p.add_argument("--effectif-attendu", type=int, default=None)
    p.add_argument("--repetitions", type=int, default=4000)
    p.add_argument("--graine", type=int, default=20261029)
    p.add_argument("--tailles", default="64,160,400", help="unités sabotées (contrastes)")
    p.add_argument("--tailles-garde", default=None, help="unités honnêtes (gardes) ; défaut : égales aux tailles")
    p.add_argument("--deltas", default="0.05,0.10")
    p.add_argument("--m", default="8,1")
    p.add_argument("--alpha", type=float, default=0.05, help="α_c de la famille (GD2-03)")
    p.add_argument("--K", default="10,3", help="épisodes honnêtes par unité (K_h)")
    p.add_argument("--K-sabotes", default=None, help="épisodes sabotés par unité (K_s) ; défaut : K")
    p.add_argument("--taux", default="0.01,0.10")
    p.add_argument("--biais", default="0,0.0125,0.025")
    p.add_argument("--comparateurs", default="1,2,3")
    p.add_argument("--comparateurs-independants", action="store_true", help="ancien modèle (A neuf par comparateur)")
    p.add_argument("--effet-unite-a", type=float, default=0.0)
    p.add_argument("--ecart-contraste", type=float, default=0.10)
    p.add_argument("--sans-n80", action="store_true")
    a = p.parse_args()
    if not (100 <= a.repetitions <= REPETITIONS_MAX):
        raise Refus(f"--repetitions dans [100 ; {REPETITIONS_MAX}]")
    if a.graine < 0:
        raise Refus("--graine : entier positif ou nul")
    if not (0 < a.alpha < 1) or not math.isfinite(a.alpha):
        raise Refus("--alpha dans ]0 ; 1[")
    if not (0 <= a.effet_unite_a <= 0.5) or not (0 < a.ecart_contraste < 0.6):
        raise Refus("--effet-unite-a dans [0 ; 0,5] ; --ecart-contraste dans ]0 ; 0,6[")
    tailles = _entiers(a.tailles, "tailles", 1, TAILLE_MAX)
    tailles_garde = _entiers(a.tailles_garde, "tailles-garde", 1, TAILLE_MAX) if a.tailles_garde else None
    if tailles_garde and len(tailles_garde) != len(tailles):
        raise Refus("--tailles-garde : autant de valeurs que --tailles (appariées)")
    deltas = _reels(a.deltas, "deltas", 0.0, 0.5, strict=True)
    ms = _entiers(a.m, "m", 1, 10_000)
    Ks = _entiers(a.K, "K", 1, 10_000)
    Kss = _entiers(a.K_sabotes, "K-sabotes", 1, 10_000) if a.K_sabotes else Ks
    if len(Kss) != len(Ks):
        raise Refus("--K-sabotes : autant de valeurs que --K")
    taux = _reels(a.taux, "taux", 0.0, 1.0)
    biais = _reels(a.biais, "biais", 0.0, 0.5)
    ks = _entiers(a.comparateurs, "comparateurs", 1, 64)
    for t in taux:
        for d in deltas:
            if t + 2 * d > 1:
                raise Refus(f"τ + 2δ > 1 (τ = {t}, δ = {d}) : tricheur tronqué (GD2-06)")
        for b in biais:
            if t + b > 1:
                raise Refus(f"τ + biais > 1 (τ = {t}, biais = {b}) (GD2-06)")
    seuils = [m / a.alpha for m in ms]
    debut = time.time()
    with open(os.path.abspath(__file__), "rb") as f:
        empreinte_script = hashlib.sha256(f.read()).hexdigest()
    sortie = {
        "version": "simulation-puissance-garde-delta-v3",
        "statut": "exploratoire, non préenregistré, non opposable" + ("" if a.ecarts else " ; lois synthétiques seulement"),
        "script_sha256": empreinte_script, **etat_git(__file__),
        "reglages": vars(a) | {"seuils": seuils, "lambdas": LAMBDAS.tolist(),
                               "lecture_des_seuils": "m/α_c : borne basse de la lecture e-BH ; 20 (m = 1) : borne haute, lâche (GD2-03)"},
        "taille_minimale_ecarts_nuls": {f"delta={d}|seuil={s}": taille_minimale_ecarts_nuls(d, s) for d in deltas for s in seuils},
        "lois": {}, "cellules": {},
    }
    paires = list(zip(tailles, tailles_garde or tailles))
    lois = []  # (loi, contraste de secours, biais essayés, artefacts)
    if a.ecarts:
        fichiers = a.ecarts.split(",")
        if a.ecarts_contraste and len(a.ecarts_contraste.split(",")) != len(fichiers):
            raise Refus("autant de fichiers de contraste que de garde")
        descs = []
        eg = []
        for f in fichiers:
            e, d = lire_fichier(f, ("fA", "fB"), a.effectif_attendu)
            eg.append(e)
            descs.append(d)
        ev = []
        if a.ecarts_contraste:
            for f in a.ecarts_contraste.split(","):
                e, d = lire_fichier(f, ("rA", "rB"), a.effectif_attendu)
                ev.append(e)
                descs.append(d)
        sortie["fichiers_observes"] = descs
        secours = LoiSynthetique(Ks[0], Kss[0], taux[0], 0.4, a.ecart_contraste, True, 0.0)
        lois.append((LoiReelle(eg, ev, True), secours, biais, True))
        lois.append((LoiReelle(eg, ev, False), secours, [0.0], False))  # GD2-04 : honnête seul, sans artefact
        ks = [len(fichiers)]
    for K, Ks_ in zip(Ks, Kss):
        for t in taux:
            loi = LoiSynthetique(K, Ks_, t, 0.4, a.ecart_contraste, not a.comparateurs_independants, a.effet_unite_a)
            lois.append((loi, loi, biais, True))
    for loi, secours, biais_loi, artefacts in lois:
        nom = loi.nom()
        sortie["lois"][nom] = {"biais_essayes": biais_loi, "artefacts": artefacts}
        for d in deltas:
            for n, ng in paires:
                for b in biais_loi:
                    for k in ks:
                        et = f"{nom}|delta={d}|n={n}|n_garde={ng}|biais={b}|k={k}"
                        sortie["cellules"][et] = cellule(loi, secours, a.repetitions, n, ng, d, seuils, k, b, a.graine, et, artefacts)
        if not a.sans_n80:
            sortie["lois"][nom]["n_pour_puissance_0_8_k_gardes"] = {
                f"delta={d}|seuil={s}|biais={b}|k={k}": n_pour_puissance(loi, secours, min(a.repetitions, 2000), d, s, k, b,
                                                                           a.graine, f"{nom}|{d}|{s}|{b}|{k}")
                for d in deltas for s in seuils for b in biais_loi for k in ks}
    sortie["environnement"] = {"python": platform.python_version(), "numpy": np.__version__, "duree_s": round(time.time() - debut, 1)}
    json.dump(sortie, sys.stdout, indent=1, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    principal()
