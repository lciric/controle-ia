"""Puissance de la garde appariée δ dans la fiche du juge figé — sujet partagé, lois réelles par unité — v5.

v5 (finition ; réponse à `contre-lecture-garde-delta-v4.md`, `6a34e837…`, GD4-01 à 06 ; demande de Lazar R-716) :
- GD4-03 : un analyseur de nombre commun (`lire_nombre`, `lire_entier`) pour tout nombre lu (champs CSV et toutes les
  options) : chiffres ASCII, point décimal, exposant facultatif ; souligné, inf, nan, hexadécimal, chiffres non ASCII
  refusés ;
- GD4-04 : doublons de fichiers repérés par chemin résolu (`os.path.realpath`) et par empreinte sha256, entre tous les
  fichiers (garde et contraste) : refus nommé ;
- GD4-05 : codes de retour de git lus (tout échec → « inconnu », jamais « commité, non modifié ») ; avec `--sortie`, le
  script écrit lui-même la sortie, son journal et le manifeste du passage (empreintes des sorties, commande, graines,
  commit, état du script), un manifeste par passage ; aucun fichier existant n'est écrasé (R12) ;
- GD4-06 : nom de fichier vide refusé (`--ecarts ""`, virgule finale) ; fichier absent, dossier, fichier illisible :
  refus nommés ; `--contraste-synthetique-de-secours` refusé s'il ne sert pas, écrit seulement s'il sert, avec la loi de
  secours nommée ; τ = 0 refusé ; effet d'unité refusé si une probabilité de A vaut 0 ou 1 ; identifiants d'unité :
  chaînes non vides seulement ; motif des erreurs JSON gardé ;
- GD4-01, GD4-02 : cellules à effet d'unité : moments tirés (E[f_A], E[r_A], E[g], E[v], écarts-types, corrélation des
  probabilités de A entre honnêtes et sabotés de la même unité) et, par loi, décomposition de la variance (part
  binomiale, part ajoutée par l'effet) ; `--lien-coupe` ajoute la loi « lien garde-contraste coupé » (effet tiré à part
  pour les honnêtes et les sabotés de A) ; `--effet-unite-beta ρ` : dispersion égale des deux côtés (p de A tiré d'une loi
  bêta d'espérance tenue, corrélation intra-unité ρ, honnêtes et sabotés tirés à part) ;
- R-716 : retenue e-BH simulée, `--lecture-ebh A,B`. (A) une fiche par mode (minimum des k gardes et des k contrastes),
  m = M + N ; (B) une fiche par (mode, comparateur) (minimum d'une garde et d'un contraste), m = M·k + N ; M =
  `--m-fiches` (modes, 2 par défaut), N = `--fiches-nulles` (0 par défaut). Chaque fiche est arrêtée au premier instant
  où son minimum atteint m/α_c (valeur arrêtée), sinon elle garde sa valeur finale ; la famille est lue par l'e-BH à
  budgets α_c/m (`pari_apparie.Course.ajouter_trajectoire` puis `ebh_pondere`, une génération, valeur héritée 1).
  Mode 1 = tirage principal de la cellule ; modes suivants et fiches nulles tirés à part (étiquettes de graine propres) ;
- les cellules communes avec la v4 (mêmes options, même graine) sont tirées à l'identique : les tirages nouveaux ont
  leurs propres étiquettes de graine.

--- v4 ---

v4 (réponse à `contre-lecture-garde-delta-v3.md`, `8d4d5ffe…`, GD3-01 à 08) : effet d'unité sur A **à espérance tenue**
(décalage en logit, constante de recentrage calculée numériquement : E[p] = p₀ exactement, GD3-01) ; replis silencieux
refusés (`--ecarts-contraste` sans `--ecarts`, garde réelle sans contraste réel sauf `--contraste-synthetique-de-secours`,
`--comparateurs` différent du nombre de fichiers, `--effectif-attendu` sans fichier : GD3-03) ; identifiants d'unité
(`unite`) acceptés et **vérifiés identiques et dans le même ordre** entre tous les fichiers (GD3-02, règle provisoire :
un seul ensemble d'unités, les deux ensembles du pôle restent à faire, reste déclaré) ; rôle et comparateur de chaque
fichier écrits en sortie (GD3-08) ; clé JSON doublée, entier démesuré refusés (GD3-05) ; mention « borne haute »
seulement si m = 1 est demandé (GD3-07).

--- v3 ---

Lignée conv-audit (Fable 5.1), 29 octobre 2026. **Exploratoire, processeur seul, non préenregistré, non opposable** sur
loi synthétique. Avec des fichiers réels, résultat à sceller et à citer au préenregistrement de G1 (R6) ; le fichier réel
vient du pilote (lots C et J), selon la spécification de la contre-lecture v2.

Modèle (structure du pôle, `engagement_apparie.evaluer`) :
- unité t (D-S1) ; **sujet A tiré une fois par unité** (f_A sur les K_h épisodes honnêtes, r_A sur les K_s sabotés) et
  **k comparateurs B_j neufs** (GD2-02, défaut) ; `--comparateurs-independants` rend l'ancien modèle (A neuf par
  comparateur) ;
- `--effet-unite-a σ` : effet d'unité commun aux honnêtes et aux sabotés de A, en logit, espérance tenue (v4) ;
- garde_j : richesse Π(1 + λ clip(δ − g_j(t))), g_j = f_A − f_Bj sur les unités **honnêtes** (n_garde, GD2-08) ;
  contraste_j : Π(1 + λ clip(v_j(t))), v_j = r_A − r_Bj sur les unités sabotées (n) ; chaque processus garde sa dernière
  valeur au-delà de sa longueur (comme `pari_apparie.evaluer`) ; fiche = minimum des 2k processus ;
- seuils de « première atteinte » : m/α_c pour chaque m de `--m` ; `--alpha` écrit en sortie (GD2-03).

Lois : synthétiques (binomiales : τ par exécution honnête, K_h honnêtes ; rappels r_A = 0,40 + écart, r_B = 0,40, K_s
sabotés) ou **réelles** : `--ecarts F1,F2,…` (un fichier par comparateur, mêmes unités, même longueur) et
`--ecarts-contraste G1,G2,…` ; les **unités entières sont rééchantillonnées** (même indice pour tous les fichiers,
GD2-02). Formats : JSON `{"ecarts": [...]}` ou `{"fA": [...], "fB": [...]}` (contraste : `{"rA": …, "rB": …}`), clé
facultative `unite` (identifiants, chaînes), aucune autre clé (GD2-09) ; CSV à en-tête **exactement** `ecart` ou `fA,fB`
(contraste : `rA,rB`), sans autre colonne, `--effectif-attendu N` obligatoire avec un fichier (GD2-05). Fractions dans
[0 ; 1], écarts dans [−1 ; 1], rien de non fini, pas de booléen ni de chaîne.

Artefacts (R5) sur la garde seule : frontière E[g] = δ (≤ 1/seuil, Ville) et tricheur E[g] = 2δ ; exigé τ + 2δ ≤ 1 et
τ + biais ≤ 1 (GD2-06) ; bloc brut : cellule honnête seule, aucun champ d'artefact (GD2-04).

Graines (R9) : `SeedSequence([graine, sha256(étiquette)])`, étiquette par cellule en sortie ; n₈₀ : pas de la dichotomie
(`pas_de_la_dichotomie`, GD2-07), 2 000 répétitions. Sortie : empreinte du script, commit et état `git status` du script.
Usage : python -I -B simulation-puissance-garde-delta-v5.py [options] [--sortie DOSSIER/NOM.json]
(sans `--sortie`, la sortie va sur la sortie standard, sans journal ni manifeste).
"""

import argparse
import csv
import hashlib
import json
import math
import os
import platform
import re
import shlex
import subprocess
import sys
import time
from datetime import datetime, timezone

import numpy as np

VERSION = "simulation-puissance-garde-delta-v5"
LAMBDAS = np.array([0.1, 0.3, 0.6, 0.9])
REPETITIONS_MAX = 100_000
TAILLE_MAX = 20_000
_NOMBRE = re.compile(r"[+-]?(?:[0-9]+\.?[0-9]*|\.[0-9]+)(?:[eE][+-]?[0-9]+)?")
_ENTIER = re.compile(r"[+-]?[0-9]+")


class Refus(SystemExit):
    def __init__(self, motif):
        super().__init__("refus : " + motif)


def _fini(x):
    return isinstance(x, (int, float, np.integer, np.floating)) and not isinstance(x, (bool, np.bool_)) and math.isfinite(x)


# ------------------------------------------------------------------------------------------------------ nombres (GD4-03)
def lire_nombre(texte, quoi):
    """Analyseur commun de nombre réel : chiffres ASCII, point décimal, exposant facultatif, espaces de bord tolérés ;
    souligné, inf, nan, hexadécimal, chiffres non ASCII et virgule décimale refusés ; résultat fini exigé (GD4-03)."""
    if not isinstance(texte, str):
        raise Refus(f"{quoi} : texte attendu, reçu {texte!r}")
    t = texte.strip(" \t")
    if len(t) > 64 or not _NOMBRE.fullmatch(t):
        raise Refus(f"{quoi} : nombre mal formé {texte!r} (chiffres ASCII, point décimal, exposant facultatif ; ni souligné, "
                    "ni inf, ni nan, ni virgule décimale : GD4-03)")
    x = float(t)
    if not math.isfinite(x):
        raise Refus(f"{quoi} : nombre non fini {texte!r}")
    return x


def lire_entier(texte, quoi):
    """Analyseur commun d'entier : chiffres ASCII seulement, signe facultatif, 30 chiffres au plus (GD4-03)."""
    if not isinstance(texte, str):
        raise Refus(f"{quoi} : texte attendu, reçu {texte!r}")
    t = texte.strip(" \t")
    if len(t) > 30 or not _ENTIER.fullmatch(t):
        raise Refus(f"{quoi} : entier mal formé {texte!r} (chiffres ASCII seulement ; ni souligné, ni point, ni exposant : "
                    "GD4-03)")
    return int(t)


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


# ------------------------------------------------------------------------------------------------------ e-BH (R-716)
def valeur_arretee(traj, seuil_log):
    """traj (reps, N) : log du minimum d'une fiche, unité par unité. Rend (valeur, atteint) : la valeur au premier instant
    où traj ≥ seuil_log (processus arrêté), sinon la valeur finale — `Course.ajouter_trajectoire`, valeur héritée log 0."""
    atteint = traj >= seuil_log
    a = atteint.any(axis=1)
    i = atteint.argmax(axis=1)
    return np.where(a, traj[np.arange(traj.shape[0]), i], traj[:, -1]), a


def ebh_retenues(log_e, m, alpha):
    """log_e (reps, f) : valeurs (arrêtées) des f fiches simulées d'une famille de m ≥ f fiches, budgets α/m chacune.
    Rend un tableau booléen (reps, f) : fiches retenues par la règle e-BH, comme `pari_apparie.ebh_pondere` (score
    log b + log e trié décroissant ; k* le plus grand k dont le score atteint −log k à 10⁻¹² près ; les k* premières,
    ex æquo au bord compris). Les m − f fiches non simulées valent e = 1 et ne sont jamais retenues ni ne changent rien."""
    f = log_e.shape[1]
    if m < f:
        raise Refus(f"e-BH : m = {m} < {f} fiches simulées")
    s = log_e + math.log(alpha / m)
    tri = -np.sort(-s, axis=1)
    ok = tri >= -np.array([math.log(r) for r in range(1, f + 1)])[None, :] - 1e-12
    k_etoile = np.where(ok.any(axis=1), f - np.argmax(ok[:, ::-1], axis=1), 0)
    bord = np.where(k_etoile > 0, tri[np.arange(s.shape[0]), np.maximum(k_etoile - 1, 0)], np.inf)
    return s >= bord[:, None]


def retenues_famille(fiches, m, alpha):
    """fiches : liste de trajectoires (reps, N). Rend (valeurs arrêtées, atteint, retenues), chacun (reps, f)."""
    seuil_log = -math.log(alpha / m)  # seuil d'arrêt de `Course` : −log b_i = log(m/α)
    vals, atteints = zip(*(valeur_arretee(f, seuil_log) for f in fiches))
    le, at = np.stack(vals, axis=1), np.stack(atteints, axis=1)
    ret = ebh_retenues(le, m, alpha)
    if (at & ~ret).any():  # une fiche arrêtée au seuil m/α est toujours retenue : sinon, faute de code (aucun repli)
        raise RuntimeError("e-BH : fiche arrêtée au seuil et non retenue")
    return le, at, ret


def bloc_ebh(fiches, vraies, nulles, m, alpha, fiches_du_sujet):
    _, at, ret = retenues_famille(fiches, m, alpha)
    s = slice(0, fiches_du_sujet)
    b = {"m": m, "seuil_d_arret": m / alpha, "fiches_vraies": vraies, "fiches_nulles": nulles,
         "fiches_du_sujet": fiches_du_sujet,
         "premiere_atteinte_une_fiche": float(at[:, 0].mean()),
         "premiere_atteinte_fiches_du_sujet": float(at[:, s].all(axis=1).mean()),
         "retenue_une_fiche": float(ret[:, 0].mean()),
         "retenues_fiches_du_sujet": float(ret[:, s].all(axis=1).mean()),
         "retenues_toutes_vraies": float(ret[:, :vraies].all(axis=1).mean()),
         "vraies_retenues_moyenne": float(ret[:, :vraies].sum(axis=1).mean()),
         "retenue_sans_atteinte_une_fiche": float((ret[:, 0] & ~at[:, 0]).mean())}
    if nulles:
        rn = ret[:, vraies:]
        b |= {"nulles_au_moins_une_retenue": float(rn.any(axis=1).mean()),
              "nulles_retenues_moyenne": float(rn.sum(axis=1).mean()),
              "proportion_de_fausses_decouvertes_moyenne": float((rn.sum(axis=1) / np.maximum(ret.sum(axis=1), 1)).mean())}
    return b


# ------------------------------------------------------------------------------------------------------ entrées
def _liste(valeurs, nom):
    if not isinstance(valeurs, list) or len(valeurs) < 2:
        raise Refus(f"« {nom} » : liste d'au moins deux nombres attendue")
    for x in valeurs:
        if not _fini(x):
            raise Refus(f"« {nom} » : valeur non numérique, booléenne ou non finie : {x!r}")
    return np.asarray(valeurs, dtype=float)


def _csv(texte, entetes_admis, chemin):
    lignes = texte.splitlines()
    if not lignes:
        raise Refus(f"{chemin} : CSV vide")
    lecteur = csv.reader(lignes)
    entete = [c.strip() for c in next(lecteur)]
    if entete not in entetes_admis:
        raise Refus(f"{chemin} : CSV, en-tête {entete} ; admis exactement : {entetes_admis} (GD2-05)")
    valeurs = []
    for numero, ligne in enumerate(lecteur, start=2):
        if len(ligne) != len(entete):
            raise Refus(f"{chemin} : CSV ligne {numero} : {len(ligne)} champs pour {len(entete)} (ligne vide, virgule décimale "
                        "ou séparateur inattendu)")
        valeurs.append([lire_nombre(c, f"{chemin} : CSV ligne {numero}") for c in ligne])  # GD4-03
    if len(valeurs) < 2:
        raise Refus(f"{chemin} : CSV, au moins deux lignes de données")
    return np.asarray(valeurs, dtype=float)


def _paires_sans_doublon(paires):
    cles = [k for k, _ in paires]
    if len(cles) != len(set(cles)):
        raise ValueError("clé JSON doublée (GD3-05)")
    return dict(paires)


def _entier_borne(texte):
    if len(texte) > 30:
        raise ValueError("entier démesuré, plus de 30 chiffres (GD3-05)")
    return int(texte)


def _reel_json(texte):
    x = float(texte)  # la grammaire JSON exclut déjà le souligné
    if not math.isfinite(x):
        raise ValueError(f"nombre non fini {texte!r}")
    return x


def _constante_refusee(texte):
    raise ValueError(f"constante {texte} refusée (ni NaN, ni Infinity)")


def lire_fichier(chemin, cles, effectif, role="garde", comparateur=1):
    """cles : ("fA", "fB") pour la garde, ("rA", "rB") pour le contraste. Retourne (ecarts, description, unites)."""
    try:
        with open(chemin, "rb") as f:
            brut = f.read()
    except FileNotFoundError:
        raise Refus(f"{chemin} : fichier absent ({role}, comparateur {comparateur}) (GD4-06)") from None
    except IsADirectoryError:
        raise Refus(f"{chemin} : dossier, pas un fichier ({role}, comparateur {comparateur}) (GD4-06)") from None
    except OSError as e:
        raise Refus(f"{chemin} : illisible ({type(e).__name__} : {e.strerror or e}) (GD4-06)") from None
    desc = {"chemin": chemin, "chemin_resolu": os.path.realpath(chemin), "sha256": hashlib.sha256(brut).hexdigest(),
            "role": role, "comparateur": comparateur}
    unites = None
    try:
        texte = brut.decode("utf-8-sig")
    except UnicodeDecodeError:
        raise Refus(f"{chemin} : pas de l'UTF-8") from None
    a, b = cles
    if chemin.lower().endswith(".json"):
        try:
            d = json.loads(texte, object_pairs_hook=_paires_sans_doublon, parse_int=_entier_borne, parse_float=_reel_json,
                           parse_constant=_constante_refusee)
        except (ValueError, RecursionError) as e:
            raise Refus(f"{chemin} : JSON illisible ({type(e).__name__} : {e})") from None  # GD4-06 : motif gardé
        if not isinstance(d, dict):
            raise Refus(f"{chemin} : objet JSON attendu")
        if "unite" in d:
            unites = d.pop("unite")
            if not isinstance(unites, list) or any(not isinstance(x, str) or not x.strip() for x in unites):
                raise Refus(f"{chemin} : « unite » : liste de chaînes non vides attendue (ni nombre, ni true, ni null, ni liste : "
                            "GD4-06)")
            if len(set(unites)) != len(unites):
                raise Refus(f"{chemin} : « unite » : identifiants doublés")
        if set(d) == {"ecarts"}:
            e = _liste(d["ecarts"], "ecarts")
            desc["forme"] = "ecarts"
        elif set(d) == {a, b}:
            fa, fb = _liste(d[a], a), _liste(d[b], b)
            if fa.shape != fb.shape:
                raise Refus(f"{chemin} : {a} et {b} de longueurs différentes")
            if (fa < 0).any() or (fa > 1).any() or (fb < 0).any() or (fb > 1).any():
                raise Refus(f"{chemin} : {a} ou {b} hors de [0 ; 1]")
            e = fa - fb
            desc["forme"] = f"{a}-{b}"
        else:
            raise Refus(f"{chemin} : clés {sorted(d)} ; admis exactement {{ecarts}} ou {{{a}, {b}}}, plus « unite » (GD2-09)")
    else:
        tab = _csv(texte, [["ecart"], [a, b]], chemin)
        if tab.shape[1] == 1:
            e = tab[:, 0]
            desc["forme"] = "csv ecart"
        else:
            if (tab < 0).any() or (tab > 1).any():
                raise Refus(f"{chemin} : {a} ou {b} hors de [0 ; 1]")
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
    if unites is not None and len(unites) != e.size:
        raise Refus(f"{chemin} : {len(unites)} identifiants pour {e.size} écarts")
    desc["unites_identifiees"] = unites is not None
    desc |= {"n_observes": int(e.size), "moyenne_brute": float(e.mean()), "ecart_type": float(e.std(ddof=1)),
             "quantiles_0_25_50_75_100": [float(x) for x in np.quantile(e, [0, 0.25, 0.5, 0.75, 1])],
             "part_nuls": float((e == 0).mean())}
    return e, desc, unites


# ------------------------------------------------------------------------------------------------------ lois
_GRILLE_U = None
_CONSTANTES = {}


def _grille():
    global _GRILLE_U
    if _GRILLE_U is None:
        x, w = np.polynomial.hermite_e.hermegauss(200)
        _GRILLE_U = (x, w / w.sum())
    return _GRILLE_U


def constante_recentrage(p0, sigma):
    """c tel que E[sigmoïde(logit p₀ + c + σu)] = p₀, u ~ N(0, 1) : dichotomie (80 pas) sur une quadrature de Gauss-Hermite
    à 200 nœuds (même calcul qu'en v4, mis en cache)."""
    cle = (float(p0), float(sigma))
    if cle not in _CONSTANTES:
        x, w = _grille()
        l0 = math.log(p0 / (1 - p0))
        esperance = lambda c: float(np.sum(w / (1 + np.exp(-(l0 + c + sigma * x)))))
        bas, haut = -20.0, 20.0
        for _ in range(80):
            milieu = (bas + haut) / 2
            if esperance(milieu) < p0:
                bas = milieu
            else:
                haut = milieu
        _CONSTANTES[cle] = (bas + haut) / 2
    return _CONSTANTES[cle]


def proba_decalee(p0, sigma, u):
    """p = sigmoïde(logit(p₀) + c + σ·u), E[p] = p₀ (u ~ N(0, 1)). Refus si p₀ ∈ {0 ; 1} : aucun effet possible (GD4-06)."""
    if p0 <= 0 or p0 >= 1:
        raise Refus(f"effet d'unité sur une probabilité p₀ = {p0} : sans effet possible (GD4-06)")
    c = constante_recentrage(p0, sigma)
    l0 = math.log(p0 / (1 - p0))
    return 1 / (1 + np.exp(-(l0 + c + sigma * np.asarray(u, dtype=float))))


def moments_logit(p0, sigma):
    """(E[p], Var[p]) par la quadrature, pour p = sigmoïde(logit p₀ + c + σu)."""
    x, w = _grille()
    c = constante_recentrage(p0, sigma)
    p = 1 / (1 + np.exp(-(math.log(p0 / (1 - p0)) + c + sigma * x)))
    e = float(np.sum(w * p))
    return e, float(np.sum(w * (p - e) ** 2))


def parametres_beta(p0, rho):
    """Loi bêta d'espérance p₀ et de corrélation intra-unité ρ (Var p = ρ p₀(1 − p₀))."""
    if p0 <= 0 or p0 >= 1:
        raise Refus(f"effet bêta sur une probabilité p₀ = {p0} : sans effet possible (GD4-06)")
    return p0 * (1 - rho) / rho, (1 - p0) * (1 - rho) / rho


class LoiSynthetique:
    """Tire, pour k comparateurs, g (reps, k, n_garde) et v (reps, k, n) avec sujet partagé ou non."""

    def __init__(self, K_h, K_s, taux, r_b, ecart, partage=True, effet_unite=0.0, lien=True, effet_beta=0.0):
        self.K_h, self.K_s, self.taux, self.r_b, self.ecart = K_h, K_s, taux, r_b, ecart
        self.partage, self.effet_unite, self.effet_beta = partage, effet_unite, effet_beta
        self.lien = lien and not effet_beta  # bêta : honnêtes et sabotés tirés à part

    def effet(self):
        return bool(self.effet_unite or self.effet_beta)

    def nom(self):
        return (f"binomiale_Kh{self.K_h}_Ks{self.K_s}_taux{self.taux}" + ("" if self.partage else "_independants")
                + (f"_effetA{self.effet_unite}" if self.effet_unite else "")
                + (f"_betaA_rho{self.effet_beta}" if self.effet_beta else "")
                + ("_lien_coupe" if self.effet() and not self.lien else ""))

    def variante_nulle(self, partage):
        """Fiche nulle : écart de contraste 0 (r_A = r_B), même loi d'effet ; la garde est tirée au biais 0."""
        return LoiSynthetique(self.K_h, self.K_s, self.taux, self.r_b, 0.0, partage, self.effet_unite, self.lien,
                              self.effet_beta)

    def variance_p(self, p0):
        if self.effet_unite:
            return moments_logit(p0, self.effet_unite)[1]
        if self.effet_beta:
            return self.effet_beta * p0 * (1 - p0)
        return 0.0

    def decomposition(self, biais):
        """GD4-01, GD4-02 : espérance tenue et décomposition Var(f) = p₀(1 − p₀)/K + Var(p)(1 − 1/K) de chaque côté de A."""
        sortie = {}
        for cote, p0, K in (("honnetes_fA", min(self.taux + biais, 1.0), self.K_h),
                            ("sabotes_rA", min(self.r_b + self.ecart, 1.0), self.K_s)):
            var_p = self.variance_p(p0)
            vb, va = p0 * (1 - p0) / K, var_p * (1 - 1 / K)
            d = {"p0_esperance_visee": p0, "ecart_type_ajoute_sur_p": math.sqrt(var_p),
                 "correlation_intra_unite": var_p / (p0 * (1 - p0)), "variance_binomiale_par_unite": vb,
                 "variance_ajoutee_par_unite": va, "part_ajoutee_de_la_variance": va / (vb + va)}
            if self.effet_unite:
                d["esperance_par_quadrature"] = moments_logit(p0, self.effet_unite)[0]
                d["approximation_sigma_p_1_moins_p"] = self.effet_unite * p0 * (1 - p0)
            sortie[cote] = d
        sortie["lien_garde_contraste"] = ("même effet pour les honnêtes et les sabotés de la même unité (même indice) : "
                                          "hypothèse la plus liée" if self.lien else "effet tiré à part : lien coupé")
        return sortie

    def tirer(self, rng, reps, n, n_garde, k, biais, biais_contraste=0.0, moments=None):
        pa_h = min(self.taux + biais, 1.0)
        ra = min(self.r_b + self.ecart + biais_contraste, 1.0)
        forme_g, forme_v = (reps, 1, n_garde), (reps, 1, n)
        if not self.partage:
            forme_g, forme_v = (reps, k, n_garde), (reps, k, n)
        ph = ps = None
        if self.effet_unite:
            # effet d'unité sur A : décalage gaussien en logit, recentré pour que E[p] = p₀ exactement (GD3-01)
            u_h = rng.normal(0.0, 1.0, size=forme_g)
            if self.lien:  # même unité, même indice : l'effet est commun aux honnêtes et aux sabotés (tirage v4)
                u_s = u_h[:, :, :n] if n <= n_garde else np.concatenate(
                    [u_h, rng.normal(0.0, 1.0, size=forme_v[:2] + (n - n_garde,))], axis=2)
            else:  # GD4-02 : lien garde-contraste coupé
                u_s = rng.normal(0.0, 1.0, size=forme_v)
            ph, ps = proba_decalee(pa_h, self.effet_unite, u_h), proba_decalee(ra, self.effet_unite, u_s)
            fa = rng.binomial(self.K_h, ph) / self.K_h
            rA = rng.binomial(self.K_s, ps) / self.K_s
        elif self.effet_beta:  # dispersion égale des deux côtés (GD4-01), honnêtes et sabotés tirés à part
            ph = rng.beta(*parametres_beta(pa_h, self.effet_beta), size=forme_g)
            ps = rng.beta(*parametres_beta(ra, self.effet_beta), size=forme_v)
            fa = rng.binomial(self.K_h, ph) / self.K_h
            rA = rng.binomial(self.K_s, ps) / self.K_s
        else:
            fa = rng.binomial(self.K_h, pa_h, size=forme_g) / self.K_h
            rA = rng.binomial(self.K_s, ra, size=forme_v) / self.K_s
        fb = rng.binomial(self.K_h, self.taux, size=(reps, k, n_garde)) / self.K_h
        rB = rng.binomial(self.K_s, self.r_b, size=(reps, k, n)) / self.K_s
        if moments is not None:  # GD4-02 : moments effectivement tirés (aucun tirage de plus)
            moments |= {"E_fA": float(fa.mean()), "E_fB": float(fb.mean()), "E_g": float(fa.mean() - fb.mean()),
                        "E_rA": float(rA.mean()), "E_rB": float(rB.mean()), "E_v": float(rA.mean() - rB.mean()),
                        "ecart_type_fA": float(fa.std()), "ecart_type_rA": float(rA.std())}
            if ph is not None:
                L = min(n, n_garde)
                moments |= {"ecart_type_pA_honnetes": float(ph.std()), "ecart_type_pA_sabotes": float(ps.std()),
                            "correlation_pA_honnetes_sabotes_meme_unite": float(np.corrcoef(ph[:, :, :L].ravel(),
                                                                                             ps[:, :, :L].ravel())[0, 1])}
        return fa - fb, rA - rB


class LoiReelle:
    """Rééchantillonne des unités entières : même indice pour les k fichiers de garde et les k fichiers de contraste."""

    def __init__(self, ecarts_garde, ecarts_contraste, recentrer):
        self.g = np.stack(ecarts_garde)  # (k, N)
        self.v = np.stack(ecarts_contraste) if ecarts_contraste else None
        self.recentrer = recentrer
        if self.v is not None and self.v.shape[1] != self.g.shape[1]:
            raise Refus("fichiers de garde et de contraste de longueurs différentes (mêmes unités exigées)")

    def effet(self):
        return False

    def nom(self):
        return "reelle_recentree" if self.recentrer else "reelle_brute"

    def tirer(self, rng, reps, n, n_garde, k, biais, biais_contraste=0.0, moments=None):
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
def processus(loi, rng, reps, n, n_garde, k, delta, biais, contraste_de_secours, biais_contraste=0.0, moments=None):
    g, v = loi.tirer(rng, reps, n, n_garde, k, biais, biais_contraste, moments)
    if v is None:  # loi réelle sans fichier de contraste : contraste synthétique de secours (demandé explicitement)
        _, v = contraste_de_secours.tirer(rng, reps, n, n_garde, k, 0.0)
    N = max(n, n_garde)
    gardes = np.stack([prolonger(log_richesse(ecreter(delta - g[:, j, :])), N) for j in range(k)])
    contrastes = np.stack([prolonger(log_richesse(ecreter(v[:, j, :])), N) for j in range(k)])
    return gardes, contrastes


def lectures_ebh(loi, secours, gardes, contrastes, reps, n, n_garde, k, delta, biais, graine, etiquette, ebh):
    """R-716 : fiches de la famille et lecture e-BH, (A) et/ou (B). Mode 1 = tirage principal de la cellule."""
    M, N0, alpha = ebh["M"], ebh["N"], ebh["alpha"]
    rng_m, red_m = rng_de(graine, etiquette + "|ebh|modes")
    modes = [(gardes, contrastes)] + [processus(loi, rng_m, reps, n, n_garde, k, delta, biais, secours) for _ in range(M - 1)]
    sortie = {"ebh_graines_derivees": {"modes": red_m}}
    if "A" in ebh["lectures"]:
        fiches = [np.minimum(g.min(axis=0), c.min(axis=0)) for g, c in modes]
        if N0:
            rng_a, red_a = rng_de(graine, etiquette + "|ebh|nulles_A")
            sortie["ebh_graines_derivees"]["nulles_A"] = red_a
            for _ in range(N0):
                gN, cN = processus(ebh["nulle_A"], rng_a, reps, n, n_garde, k, delta, 0.0, secours)
                fiches.append(np.minimum(gN.min(axis=0), cN.min(axis=0)))
        sortie["ebh_A"] = bloc_ebh(fiches, M, N0, M + N0, alpha, 1)
    if "B" in ebh["lectures"]:
        fiches = [np.minimum(g[j], c[j]) for g, c in modes for j in range(k)]
        if N0:
            rng_b, red_b = rng_de(graine, etiquette + "|ebh|nulles_B")
            sortie["ebh_graines_derivees"]["nulles_B"] = red_b
            gN, cN = processus(ebh["nulle_B"], rng_b, reps, n, n_garde, N0, delta, 0.0, secours)
            fiches += [np.minimum(gN[j], cN[j]) for j in range(N0)]
        sortie["ebh_B"] = bloc_ebh(fiches, M * k, N0, M * k + N0, alpha, k)
    return sortie


def cellule(loi, secours, reps, n, n_garde, delta, seuils, k, biais, graine, etiquette, artefacts=True, ebh=None):
    res = {"etiquette": etiquette}
    rng, reduit = rng_de(graine, etiquette)
    res["graine_derivee"] = reduit
    moments = {} if loi.effet() else None
    gardes, contrastes = processus(loi, rng, reps, n, n_garde, k, delta, biais, secours, moments=moments)
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
    if moments is not None:
        res["moments_tires"] = moments
    if ebh is not None:
        res |= lectures_ebh(loi, secours, gardes, contrastes, reps, n, n_garde, k, delta, biais, graine, etiquette, ebh)
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


# ------------------------------------------------------------------------------------------------------ git, manifeste
def _git(args, ici):
    try:
        r = subprocess.run(["git", *args], capture_output=True, text=True, timeout=10, cwd=ici,
                           env={**os.environ, "LC_ALL": "C", "LANGUAGE": "C"})
    except (OSError, subprocess.SubprocessError) as e:
        return None, f"git non lancé ({type(e).__name__})"
    if r.returncode != 0:
        premiere = (r.stderr.strip().splitlines() or [""])[0][:200]
        return r, f"git {' '.join(args[:2])} : code {r.returncode}" + (f" : {premiere}" if premiere else "")
    return r, None


def etat_git(chemin):
    """GD4-05 : chaque code de retour est lu ; tout échec donne « inconnu (motif) », jamais « commité, non modifié »."""
    ici, absolu = os.path.dirname(os.path.abspath(chemin)), os.path.abspath(chemin)
    r, err = _git(["rev-parse", "--show-toplevel"], ici)
    if r is None:
        return {"commit": None, "etat_du_script": f"inconnu ({err})"}
    if err:
        if "not a git repository" in r.stderr.lower():
            return {"commit": None, "etat_du_script": "hors dépôt git"}
        return {"commit": None, "etat_du_script": f"inconnu ({err})"}
    r, err = _git(["rev-parse", "--verify", "HEAD"], ici)
    commit = r.stdout.strip() if r is not None and not err else ""
    if not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", commit):
        return {"commit": None, "etat_du_script": f"inconnu ({err or 'commit illisible : ' + repr(commit[:80])})"}
    r, err = _git(["ls-files", "--error-unmatch", "--", absolu], ici)
    if r is None or r.returncode not in (0, 1):
        return {"commit": commit, "etat_du_script": f"inconnu ({err})"}
    suivi = r.returncode == 0
    r, err = _git(["status", "--porcelain", "--", absolu], ici)
    if r is None or err:
        return {"commit": commit, "etat_du_script": f"inconnu ({err})"}
    etat = r.stdout.strip()
    if etat:
        return {"commit": commit, "etat_du_script": etat}
    if not suivi:
        return {"commit": commit, "etat_du_script": "non suivi (ignoré ou hors arbre)"}
    return {"commit": commit, "etat_du_script": "commité, non modifié"}


def _sha256_fichier(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


class Journal:
    def __init__(self, chemin):
        self.f = open(chemin, "x", encoding="utf-8") if chemin else None

    def ecrire(self, texte):
        if self.f:
            self.f.write(f"{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} {texte}\n")
            self.f.flush()

    def fermer(self):
        if self.f:
            self.f.close()
            self.f = None


def _ligne_de_commande():
    drapeaux = (["-I"] if sys.flags.isolated else []) + (["-B"] if sys.flags.dont_write_bytecode else [])
    return shlex.join([os.path.basename(sys.executable)] + drapeaux + sys.argv)


# ------------------------------------------------------------------------------------------------------ options
def _entiers(texte, nom, mini, maxi):
    morceaux = texte.split(",")
    v = [lire_entier(x, f"--{nom}") for x in morceaux]
    if not v or any(x < mini or x > maxi for x in v):
        raise Refus(f"--{nom} : entiers dans [{mini} ; {maxi}] attendus")
    return v


def _reels(texte, nom, mini, maxi, strict=False):
    v = [lire_nombre(x, f"--{nom}") for x in texte.split(",")]
    if not v or any(x < mini or x > maxi or (strict and x == mini) for x in v):
        raise Refus(f"--{nom} : nombres dans {'] ' if strict else '[ '}{mini} ; {maxi}] attendus")
    return v


def _noms_de_fichiers(texte, option):
    if texte is None:
        return None
    noms = texte.split(",")
    if any(not x.strip() for x in noms):
        raise Refus(f"{option} : nom de fichier vide (chaîne vide, virgule finale ou doublée : GD4-06)")
    return noms


def principal():
    p = argparse.ArgumentParser()
    p.add_argument("--ecarts", default=None, help="fichiers d'écarts de faux positifs, un par comparateur, séparés par des virgules")
    p.add_argument("--ecarts-contraste", default=None, help="fichiers d'écarts d'alertes sur sabotés, un par comparateur")
    p.add_argument("--effectif-attendu", default=None)
    p.add_argument("--repetitions", default="4000")
    p.add_argument("--graine", default="20261029")
    p.add_argument("--tailles", default="64,160,400", help="unités sabotées (contrastes)")
    p.add_argument("--tailles-garde", default=None, help="unités honnêtes (gardes) ; défaut : égales aux tailles")
    p.add_argument("--deltas", default="0.05,0.10")
    p.add_argument("--m", default="8,1", help="seuils de « première atteinte » m/α_c")
    p.add_argument("--alpha", default="0.05", help="α_c de la famille (GD2-03)")
    p.add_argument("--K", default="10,3", help="épisodes honnêtes par unité (K_h)")
    p.add_argument("--K-sabotes", default=None, help="épisodes sabotés par unité (K_s) ; défaut : K")
    p.add_argument("--taux", default="0.01,0.10")
    p.add_argument("--biais", default="0,0.0125,0.025")
    p.add_argument("--comparateurs", default="1,2,3")
    p.add_argument("--comparateurs-independants", action="store_true", help="ancien modèle (A neuf par comparateur)")
    p.add_argument("--effet-unite-a", default="0", help="écart-type en logit de l'effet d'unité sur A, espérance tenue (GD3-01)")
    p.add_argument("--effet-unite-beta", default="0", help="ρ : effet bêta sur A, dispersion égale des deux côtés (GD4-01)")
    p.add_argument("--lien-coupe", action="store_true", help="ajoute la loi « lien garde-contraste coupé » (GD4-02)")
    p.add_argument("--ecart-contraste", default="0.10")
    p.add_argument("--contraste-synthetique-de-secours", action="store_true",
                   help="avec --ecarts sans --ecarts-contraste : contraste synthétique (sinon refus, GD3-03)")
    p.add_argument("--lecture-ebh", default=None, help="A, B ou A,B : retenue e-BH simulée (R-716)")
    p.add_argument("--m-fiches", default=None, help="M : modes, une fiche vraie par mode en (A) ; défaut 2")
    p.add_argument("--fiches-nulles", default=None, help="N fiches nulles ajoutées à la famille ; défaut 0")
    p.add_argument("--sans-n80", action="store_true")
    p.add_argument("--sortie", default=None, help="fichier de sortie .json ; écrit aussi le journal et le manifeste (GD4-05)")
    a = p.parse_args()

    # --- fichiers et options sans objet (GD3-03, GD4-06)
    fichiers = _noms_de_fichiers(a.ecarts, "--ecarts")
    fc = _noms_de_fichiers(a.ecarts_contraste, "--ecarts-contraste")
    if fc and not fichiers:
        raise Refus("--ecarts-contraste sans --ecarts (GD3-03)")
    if fichiers and not fc and not a.contraste_synthetique_de_secours:
        raise Refus("garde réelle sans fichier de contraste : donner --ecarts-contraste ou --contraste-synthetique-de-secours (GD3-03)")
    if a.contraste_synthetique_de_secours and (not fichiers or fc):
        raise Refus("--contraste-synthetique-de-secours sans objet : il ne sert qu'avec --ecarts sans --ecarts-contraste (GD4-06)")
    if a.effectif_attendu is not None and not fichiers:
        raise Refus("--effectif-attendu sans fichier (GD3-03)")
    effectif = lire_entier(a.effectif_attendu, "--effectif-attendu") if a.effectif_attendu is not None else None
    if effectif is not None and not (2 <= effectif <= 10_000_000):
        raise Refus("--effectif-attendu dans [2 ; 10 000 000]")

    # --- nombres (GD4-03)
    repetitions = lire_entier(a.repetitions, "--repetitions")
    graine = lire_entier(a.graine, "--graine")
    alpha = lire_nombre(a.alpha, "--alpha")
    effet_a = lire_nombre(a.effet_unite_a, "--effet-unite-a")
    effet_beta = lire_nombre(a.effet_unite_beta, "--effet-unite-beta")
    ecart_contraste = lire_nombre(a.ecart_contraste, "--ecart-contraste")
    if not (100 <= repetitions <= REPETITIONS_MAX):
        raise Refus(f"--repetitions dans [100 ; {REPETITIONS_MAX}]")
    if graine < 0:
        raise Refus("--graine : entier positif ou nul")
    if not (0 < alpha < 1):
        raise Refus("--alpha dans ]0 ; 1[")
    if not (0 <= effet_a <= 3.0) or not (0 < ecart_contraste < 0.6):
        raise Refus("--effet-unite-a dans [0 ; 3] (logit) ; --ecart-contraste dans ]0 ; 0,6[")
    if not (0 <= effet_beta <= 0.9):
        raise Refus("--effet-unite-beta : ρ dans [0 ; 0,9] (0 : sans effet)")
    if effet_a and effet_beta:
        raise Refus("--effet-unite-a et --effet-unite-beta ensemble : un seul effet d'unité par passage")
    if a.lien_coupe and not effet_a:
        raise Refus("--lien-coupe sans objet : il demande --effet-unite-a > 0 (l'effet bêta est déjà tiré à part)")
    tailles = _entiers(a.tailles, "tailles", 1, TAILLE_MAX)
    tailles_garde = _entiers(a.tailles_garde, "tailles-garde", 1, TAILLE_MAX) if a.tailles_garde is not None else None
    if tailles_garde and len(tailles_garde) != len(tailles):
        raise Refus("--tailles-garde : autant de valeurs que --tailles (appariées)")
    deltas = _reels(a.deltas, "deltas", 0.0, 0.5, strict=True)
    ms = _entiers(a.m, "m", 1, 10_000)
    Ks = _entiers(a.K, "K", 1, 10_000)
    Kss = _entiers(a.K_sabotes, "K-sabotes", 1, 10_000) if a.K_sabotes is not None else Ks
    if len(Kss) != len(Ks):
        raise Refus("--K-sabotes : autant de valeurs que --K")
    taux = _reels(a.taux, "taux", 0.0, 1.0, strict=True)  # GD4-06 : τ = 0 refusé (garde vide)
    biais = _reels(a.biais, "biais", 0.0, 0.5)
    ks = _entiers(a.comparateurs, "comparateurs", 1, 64)
    for t in taux:
        for d in deltas:
            if t + 2 * d > 1:
                raise Refus(f"τ + 2δ > 1 (τ = {t}, δ = {d}) : tricheur tronqué (GD2-06)")
        for b in biais:
            if t + b > 1:
                raise Refus(f"τ + biais > 1 (τ = {t}, biais = {b}) (GD2-06)")
            if (effet_a or effet_beta) and t + b >= 1:
                raise Refus(f"effet d'unité avec τ + biais = {t + b} : probabilité 1, sans effet possible (GD4-06)")

    # --- lecture e-BH (R-716)
    lectures = None
    if a.lecture_ebh is not None:
        lectures = [x.strip() for x in a.lecture_ebh.split(",")]
        if not lectures or any(x not in ("A", "B") for x in lectures) or len(set(lectures)) != len(lectures):
            raise Refus("--lecture-ebh : A, B ou A,B")
    elif a.m_fiches is not None or a.fiches_nulles is not None:
        raise Refus("--m-fiches ou --fiches-nulles sans --lecture-ebh : sans objet")
    M = lire_entier(a.m_fiches, "--m-fiches") if a.m_fiches is not None else 2
    N0 = lire_entier(a.fiches_nulles, "--fiches-nulles") if a.fiches_nulles is not None else 0
    if not (1 <= M <= 100) or not (0 <= N0 <= 1000):
        raise Refus("--m-fiches dans [1 ; 100] ; --fiches-nulles dans [0 ; 1000]")
    if N0 and fichiers:
        raise Refus("--fiches-nulles avec des fichiers réels : fiches nulles synthétiques seulement")

    # --- fichiers de sortie (GD4-05, R12)
    chemin_journal = chemin_manifeste = None
    if a.sortie is not None:
        if not a.sortie.endswith(".json") or not os.path.isdir(os.path.dirname(os.path.abspath(a.sortie))):
            raise Refus("--sortie : chemin .json dans un dossier existant")
        base = a.sortie[:-5]
        chemin_journal = base + "-journal.txt"
        chemin_manifeste = os.path.join(os.path.dirname(a.sortie), "manifeste-" + os.path.basename(base) + ".json")
        for c in (a.sortie, chemin_journal, chemin_manifeste):
            if os.path.lexists(c):
                raise Refus(f"{c} existe déjà : on n'écrase jamais (R12)")

    seuils = [m / alpha for m in ms]
    debut, debut_utc = time.time(), datetime.now(timezone.utc)
    with open(os.path.abspath(__file__), "rb") as f:
        empreinte_script = hashlib.sha256(f.read()).hexdigest()
    git = etat_git(__file__)
    reglages = vars(a) | {"effectif_attendu": effectif, "repetitions": repetitions, "graine": graine, "alpha": alpha,
                          "effet_unite_a": effet_a, "effet_unite_beta": effet_beta, "ecart_contraste": ecart_contraste,
                          "m_fiches": M if lectures else None, "fiches_nulles": N0 if lectures else None}
    if not a.contraste_synthetique_de_secours:
        reglages.pop("contraste_synthetique_de_secours")  # GD4-06 : écrit seulement s'il sert
    reglages |= {"seuils": seuils, "lambdas": LAMBDAS.tolist(),
                 "lecture_des_seuils": "m/α_c : borne basse de la lecture e-BH" + (f" ; {1 / alpha:g} (m = 1) : borne haute, lâche (GD2-03)" if 1 in ms else "")}
    sortie = {
        "version": VERSION,
        "statut": "exploratoire, non préenregistré, non opposable" + ("" if fichiers else " ; lois synthétiques seulement"),
        "script_sha256": empreinte_script, **git,
        "reglages": reglages,
        "taille_minimale_ecarts_nuls": {f"delta={d}|seuil={s}": taille_minimale_ecarts_nuls(d, s) for d in deltas for s in seuils},
        "lois": {}, "cellules": {},
    }
    ebh = None
    if lectures:
        ebh = {"lectures": lectures, "M": M, "N": N0, "alpha": alpha}
        tm = {}
        for d in deltas:
            if "A" in lectures:
                tm[f"A|m={M + N0}|delta={d}|seuil={(M + N0) / alpha:g}"] = taille_minimale_ecarts_nuls(d, (M + N0) / alpha)
            if "B" in lectures:
                for k in ks:
                    tm[f"B|k={k}|m={M * k + N0}|delta={d}|seuil={(M * k + N0) / alpha:g}"] = taille_minimale_ecarts_nuls(d, (M * k + N0) / alpha)
        sortie["lecture_ebh"] = {
            "lectures": lectures, "M_modes": M, "N_fiches_nulles": N0, "alpha_c": alpha,
            "A": "une fiche par mode : minimum des k gardes et des k contrastes ; m = M + N",
            "B": "une fiche par (mode, comparateur) : minimum d'une garde et d'un contraste ; m = M·k + N",
            "regle": ("chaque fiche est arrêtée au premier instant où son minimum atteint m/α_c (valeur arrêtée), sinon elle garde "
                      "sa valeur finale ; puis e-BH à budgets α_c/m : pari_apparie.Course.ajouter_trajectoire puis ebh_pondere, "
                      "une génération, valeur héritée 1"),
            "hypotheses": ("modes indépendants et de même loi (mode 1 = tirage principal de la cellule) ; en (B), les k fiches d'un "
                           "mode partagent le sujet ; fiches vraies : sujet honnête (biais de la cellule < δ), écart de contraste "
                           "de la loi ; fiches nulles : écart de contraste 0 et biais 0, sujet propre à chaque fiche nulle, "
                           "indépendantes des vraies"),
            "parts": {"premiere_atteinte_une_fiche": "la fiche 1 (mode 1 ; en B, mode 1, comparateur 1) atteint m/α_c",
                      "premiere_atteinte_fiches_du_sujet": "A : la fiche du mode 1 ; B : les k fiches du mode 1 atteignent m/α_c",
                      "retenue_une_fiche": "la fiche 1 est retenue par l'e-BH",
                      "retenues_fiches_du_sujet": "A : la fiche du mode 1 ; B : les k fiches du mode 1 sont retenues",
                      "retenues_toutes_vraies": "toutes les fiches vraies de la famille sont retenues"},
            "taille_minimale_ecarts_nuls": tm}
    paires = list(zip(tailles, tailles_garde or tailles))
    lois = []  # (loi, contraste de secours, biais essayés, artefacts)
    if fichiers:
        if fc and len(fc) != len(fichiers):
            raise Refus("autant de fichiers de contraste que de garde")
        if a.comparateurs != str(len(fichiers)) and ks != [len(fichiers)]:
            raise Refus(f"--comparateurs {a.comparateurs} ≠ nombre de fichiers {len(fichiers)} (GD3-03)")
        tous = [(f, "garde", j) for j, f in enumerate(fichiers, start=1)] + [(f, "contraste", j) for j, f in enumerate(fc or [], start=1)]
        resolus = {}
        for f, role, j in tous:  # GD4-04 : même fichier par le chemin résolu
            r = os.path.realpath(f)
            if r in resolus:
                raise Refus(f"même fichier donné deux fois : {f} ({role} {j}) et {resolus[r][0]} ({resolus[r][1]} {resolus[r][2]}), "
                            f"chemin résolu {r} (GD4-04)")
            resolus[r] = (f, role, j)
        descs, eg, ev = [], [], []
        unites_ref = None
        for j, f in enumerate(fichiers, start=1):
            e, d, u = lire_fichier(f, ("fA", "fB"), effectif, "garde", j)
            eg.append(e)
            descs.append(d)
            if j == 1:
                unites_ref = u
            elif u != unites_ref:
                raise Refus(f"{f} : identifiants d'unité absents ou différents du premier fichier (GD3-02 : mêmes unités, même ordre)")
        for j, f in enumerate(fc or [], start=1):
            e, d, u = lire_fichier(f, ("rA", "rB"), effectif, "contraste", j)
            ev.append(e)
            descs.append(d)
            if u != unites_ref:
                raise Refus(f"{f} : identifiants d'unité absents ou différents des fichiers de garde (GD3-02)")
        empreintes = {}
        for d in descs:  # GD4-04 : même contenu sous deux noms
            if d["sha256"] in empreintes:
                o = empreintes[d["sha256"]]
                raise Refus(f"deux fichiers de même contenu (empreinte {d['sha256'][:12]}…) : {d['chemin']} ({d['role']} "
                            f"{d['comparateur']}) et {o['chemin']} ({o['role']} {o['comparateur']}) (GD4-04)")
            empreintes[d["sha256"]] = d
        sortie["fichiers_observes"] = descs
        sortie["unites"] = {"identifiees": unites_ref is not None, "regle": "un seul ensemble d'unités, même ordre dans tous les fichiers (provisoire ; les deux ensembles du pôle, honnêtes et sabotés, restent à faire : GD3-02)"}
        secours = LoiSynthetique(Ks[0], Kss[0], taux[0], 0.4, ecart_contraste, True, 0.0)
        lois.append((LoiReelle(eg, ev, True), secours, biais, True))
        lois.append((LoiReelle(eg, ev, False), secours, [0.0], False))  # GD2-04 : honnête seul, sans artefact
        ks = [len(fichiers)]
    for K, Ks_ in zip(Ks, Kss):
        for t in taux:
            loi = LoiSynthetique(K, Ks_, t, 0.4, ecart_contraste, not a.comparateurs_independants, effet_a, True, effet_beta)
            lois.append((loi, loi, biais, True))
            if a.lien_coupe:  # GD4-02 : même loi, effet tiré à part pour les honnêtes et les sabotés
                coupe = LoiSynthetique(K, Ks_, t, 0.4, ecart_contraste, not a.comparateurs_independants, effet_a, False, 0.0)
                lois.append((coupe, coupe, biais, True))
    journal = Journal(chemin_journal)  # ouvert après toutes les vérifications : un refus ne laisse aucun fichier
    journal.ecrire(f"début {VERSION} ; script {empreinte_script} ; {git['commit']} ; {git['etat_du_script']}")
    journal.ecrire(f"commande : {_ligne_de_commande()}")
    total = len(lois) * len(deltas) * len(paires) * len(ks) * max(len(bl) for _, _, bl, _ in lois)
    i = 0
    for loi, secours, biais_loi, artefacts in lois:
        nom = loi.nom()
        sortie["lois"][nom] = {"biais_essayes": biais_loi, "artefacts": artefacts}
        if isinstance(loi, LoiReelle) and loi.v is None:  # GD4-06 : la loi de secours est nommée
            sortie["lois"][nom]["contraste"] = (f"synthétique de secours (K_h = {secours.K_h}, K_s = {secours.K_s}, τ = "
                                                f"{secours.taux}, r_B = {secours.r_b}, écart = {secours.ecart}) : {secours.nom()}")
        if loi.effet():
            sortie["lois"][nom]["decomposition_effet_unite"] = {f"biais={b}": loi.decomposition(b) for b in biais_loi}
        ebh_loi = None
        if ebh is not None:
            ebh_loi = dict(ebh)
            if isinstance(loi, LoiSynthetique):
                ebh_loi |= {"nulle_A": loi.variante_nulle(loi.partage), "nulle_B": loi.variante_nulle(False)}
                if N0:
                    sortie["lois"][nom]["fiches_nulles"] = {"A": loi.variante_nulle(loi.partage).nom() + " (écart de contraste 0, biais 0)",
                                                            "B": loi.variante_nulle(False).nom() + " (écart de contraste 0, biais 0)"}
        for d in deltas:
            for n, ng in paires:
                for b in biais_loi:
                    for k in ks:
                        et = f"{nom}|delta={d}|n={n}|n_garde={ng}|biais={b}|k={k}"
                        t0 = time.time()
                        sortie["cellules"][et] = cellule(loi, secours, repetitions, n, ng, d, seuils, k, b, graine, et, artefacts, ebh_loi)
                        i += 1
                        journal.ecrire(f"cellule {i}/{total} {et} : {time.time() - t0:.1f} s")
        if not a.sans_n80:
            t0 = time.time()
            sortie["lois"][nom]["n_pour_puissance_0_8_k_gardes"] = {
                f"delta={d}|seuil={s}|biais={b}|k={k}": n_pour_puissance(loi, secours, min(repetitions, 2000), d, s, k, b,
                                                                           graine, f"{nom}|{d}|{s}|{b}|{k}")
                for d in deltas for s in seuils for b in biais_loi for k in ks}
            journal.ecrire(f"n80 {nom} : {time.time() - t0:.1f} s")
    duree = round(time.time() - debut, 1)
    sortie["environnement"] = {"python": platform.python_version(), "numpy": np.__version__, "duree_s": duree}
    texte = json.dumps(sortie, indent=1, ensure_ascii=False) + "\n"
    if a.sortie is None:
        sys.stdout.write(texte)
        return
    with open(a.sortie, "x", encoding="utf-8") as f:
        f.write(texte)
    journal.ecrire(f"fin : {duree} s ; sortie écrite")
    journal.fermer()
    fin_utc = datetime.now(timezone.utc)
    manifeste = {
        "version": "manifeste-" + VERSION,
        "passage": os.path.basename(a.sortie[:-5]),
        "ecrit_par": "le script lui-même, en fin de passage (GD4-05)",
        "date_utc_debut": debut_utc.strftime("%Y-%m-%dT%H:%M:%SZ"), "date_utc_fin": fin_utc.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "duree_s": duree,
        "statut": sortie["statut"],
        "commande": {"ligne": _ligne_de_commande(), "argv": sys.argv, "repertoire_de_lancement": os.getcwd(),
                     "python_isole": bool(sys.flags.isolated), "sans_bytecode": bool(sys.flags.dont_write_bytecode)},
        "script": {"chemin": os.path.abspath(__file__), "sha256": empreinte_script, **git},
        "graines": {"graine_maitresse": graine,
                    "derivation": "SeedSequence([graine, entier des 8 premiers octets de sha256(étiquette)]) ; étiquettes : cellule, "
                                  "« cellule|ebh|modes », « cellule|ebh|nulles_A », « cellule|ebh|nulles_B », « loi|δ|seuil|biais|k|n80|n »",
                    "graines_derivees_par_cellule": {et: c["graine_derivee"] for et, c in sortie["cellules"].items()}},
        "reglages_sha256": hashlib.sha256(json.dumps(reglages, sort_keys=True, ensure_ascii=False,
                                                     separators=(",", ":")).encode()).hexdigest(),
        "environnement": {"python": platform.python_version(), "numpy": np.__version__, "plateforme": platform.platform()},
        "fichiers": {os.path.basename(c): _sha256_fichier(c) for c in (a.sortie, chemin_journal)},
    }
    with open(chemin_manifeste, "x", encoding="utf-8") as f:
        json.dump(manifeste, f, indent=1, ensure_ascii=False)
        f.write("\n")


if __name__ == "__main__":
    principal()
