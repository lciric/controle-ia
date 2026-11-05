#!/usr/bin/env python3
"""Quatre règles de mise à jour de la défense dans l'arène coévolutive synthétique v4, plus le témoin « défense figée »
et la mesure X̄ — v2 (code d'essai et de pilote).

CE QUI CHANGE PAR RAPPORT À LA v1 (`arene_regles_defense_v1.py`, empreinte sha256
337c569bd90d5b8964a4e6b7491c0c5a67042d54333401b65540e889a15a2c97, jamais modifiée, R12) — gel v2 § 0 :
- mesure X̄ = moyenne des X_t sur les T tours (X_t = 1 − (iii)_t, déjà calculé par tour), rendue par trajectoire
  (`exploitabilite_moyenne_tours`) à côté de X finale = 1 − V ; contraste apparié contre R2 à l'analyse (code de
  rééchantillonnage j = 8 : 1000 + rang, pour ne pas heurter les codes des indicateurs) — CL-05, option (b) ;
- témoin R0 « défense figée » : M0 déployé à tous les tours, jamais réentraîné (zéro appel à l'entraînement après
  le tour 0), l'attaquant jouant en dernier à chaque tour ; code de graine neuf 20 (libre dans le v4 et la v1) ;
  matrice H à T + 1 lignes identiques (I2 = 0 par construction), cosinus consécutif 1 par construction — S6 (c) ;
- identité de préenregistrement PREREG-REGLES-DEFENSE-V2 ; gel v2 épinglé ; racines d'essai neuves (gel v2 § 1),
  racines d'essai de la v1 refusées comme employées ;
- CL-08 : le gel sur disque est revérifié en mode `decision` ; CL-11 : cosinus consécutif moyen par tâche et écart
  « standard seul / renforcé seul » des contrastes rendus par l'analyse.
Rien d'autre ne change : R2 = A et R3 = B au bit (essais clés), R4(λ = 0) = R2, gardes, graines de R1 à R4.

Règles (gel `gel-regles-defense-v2.md`, § 2 ; chacune à trajectoire propre sur T tours, moniteur commun M0 au tour 0,
l'attaquant jouant en dernier à chaque tour par meilleure réponse à la défense déployée) :
- R0 « défense figée » (témoin) : M0 déployé à tous les tours, aucun réentraînement ;
- R1 « dernière attaque » : moniteur linéaire réentraîné (oracle « détection » du v4) contre la seule attaque du tour ;
- R2 « historique » : = bras A du v4 (mélange uniforme de toutes les attaques passées) ; même code de graine que A,
  trajectoire identique au bit (essai clé) ;
- R3 « mélange d'équilibre des deux côtés » : = bras B du v4 (double oracle tronqué : moniteurs passés aux poids
  d'équilibre p, oracle du défenseur contre la stratégie d'équilibre q de l'attaquant) ; même code de graine que B ;
  lecture R3′ « attaquant à l'équilibre » = valeur du jeu restreint à chaque tour, sur la même trajectoire ;
- R4 « régularisation vers le passé » : comme R2, plus la pénalité sans échelle λ‖w/‖w‖ − u‖² = 2λ(1 − cos(w, u)),
  u = direction du moniteur déployé (« dernier ») ou moyenne des directions passées (« moyenne ») ; λ = 0 rend R2 au bit.

Le fichier `arene_melange_v4.py` n'est jamais modifié (R12) : il est chargé par chemin, empreinte vérifiée, et dans la
copie chargée en mémoire seulement : `gen` est remplacé par `gen_regles` (même schéma de graines, racines neuves du gel
v2 : le `gen` du v4 refuse toute racine hors de ses propres listes), le dictionnaire `BRAS` est étendu des codes des
règles (pour `phase_finale`), et `minimize` / `linprog` sont enveloppés d'un compteur (coût).

Commandes (PYTHONPATH=src ; OMP_NUM_THREADS=1 posé par le module) :
    python3 <ce fichier> essai --instances 0:6 --sortie FICHIER.json --processus 2 [--pids FICHIER] [--T 8]
    python3 <ce fichier> identite
    python3 <ce fichier> decision --prereg prereg/<scellé>.md --instances 0:N --run-id ID --lambda L --reference R
    python3 <ce fichier> orphelins --pids FICHIER [--arreter]
"""
from __future__ import annotations

import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import argparse  # noqa: E402
import hashlib  # noqa: E402
import importlib.util  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
import signal  # noqa: E402
import subprocess  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
from collections import Counter  # noqa: E402
from dataclasses import asdict, replace  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402

ICI = Path(__file__).resolve().parent
DEPOT = ICI.parents[3]
if str(DEPOT / "src") not in sys.path:
    sys.path.insert(0, str(DEPOT / "src"))

from controle_ia.gardes import GardeArret, exiger_numpy_minimal, lever_sur_term  # noqa: E402

VERSION = "arene_regles_defense_v2"
IDENTIFIANT_PREREG = "PREREG-REGLES-DEFENSE-V2"
ARENE_V4 = DEPOT / "donnees" / "argon-seul-convergence-v1" / "arene_melange_v4.py"
ARENE_V4_SHA256 = "70c77fd5c0ec72b63ae4c10e1e6b2fc423aacfedce9a4a0792869d92c5a2ae61"
GEL = ICI / "gel-regles-defense-v2.md"
GEL_SHA256 = "9977d7df7f87f081f3c89709c6f36ab2c3861cb06c972dffbabe0e777e9910f3"
FICHIERS_BIBLIOTHEQUE = ("src/controle_ia/gardes.py", "src/controle_ia/prereg.py", "src/controle_ia/scellement.py",
                         "src/controle_ia/manifeste.py")

# --- racines (R9) : toutes écrites dans le gel v2 AVANT toute exécution ; plage 20266001 à 20266999 ----------------
PLAGE_REGLES = (20266001, 20266999)
RACINE_DECISION, RACINE_DECISION_TENUE = 20266201, 20266202     # réservées : jamais employées hors décision autorisée
RACINE_ESSAI, RACINE_ESSAI_TENUE = 20266501, 20266502           # pilote d'essai v2
RACINE_TESTS, RACINE_TESTS_TENUE = 20266511, 20266512           # essais du code v2
RACINE_TESTS_AUTRE = 20266513                                   # essais : « une autre racine change le résultat »
RACINE_SIMULATION = 20266401                                    # réservée aux simulations (non employée)
RACINE_REPRISE_PILOTE = 20266521                                # réservée (reprise du pilote v2 ; non employée)
RACINES_DECISION = (RACINE_DECISION, RACINE_DECISION_TENUE)
RACINES_GELEES = (RACINE_ESSAI, RACINE_ESSAI_TENUE, RACINE_TESTS, RACINE_TESTS_TENUE, RACINE_TESTS_AUTRE,
                  RACINE_SIMULATION, RACINE_REPRISE_PILOTE)
RACINES_EMPLOYEES_V1 = (20266101, 20266102, 20266301, 20266302, 20266303)   # pilote et essais de la v1 : refusées
_PERMISES_HORS_DECISION = frozenset(RACINES_GELEES)

GRILLE_LAMBDA = (0.03, 0.1, 0.3, 1.0, 3.0)      # gel § 3
REFERENCES = ("dernier", "moyenne")
TOLERANCE_CHOIX_LAMBDA = 0.005                  # gel § 3 : égalité à 0,005 près → la plus petite λ


def empreinte_fichier(chemin: str | Path) -> str:
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


# =================================================================================================================
# Chargement de l'arène v4 par chemin (jamais modifiée), empreinte vérifiée
# =================================================================================================================
def charger_arene_v4(chemin: str | Path = ARENE_V4, sha_attendue: str = ARENE_V4_SHA256):
    """Charge `arene_melange_v4.py` comme module privé (aucun `.pyc` écrit sous `donnees/`). Garde : fichier présent,
    empreinte égale à celle épinglée."""
    p = Path(chemin)
    if not p.is_file():
        raise GardeArret(f"arène v4 absente : {p}")
    sha = empreinte_fichier(p)
    if sha != sha_attendue:
        raise GardeArret(f"arène v4 modifiée : empreinte {sha} ≠ épinglée {sha_attendue}")
    ancien = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec = importlib.util.spec_from_file_location("arene_melange_v4_pour_regles", p)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = mod        # exigé par `dataclass` (annotations différées) ; nom privé, sans collision
        spec.loader.exec_module(mod)
    finally:
        sys.dont_write_bytecode = ancien
    return mod


v4 = charger_arene_v4()

# --- règles et codes de graine (gel § 2) ; BRAS de la copie chargée étendu pour `phase_finale` --------------------
REGLES = ("R0", "R1", "R2", "R3", "R4")
CODES = {"R0": 20, "R1": 21, "R2": v4.BRAS["A"], "R3": v4.BRAS["B"], "R4": 24}
NOMS = {"R0": "défense figée (témoin : M0 jamais réentraîné)", "R1": "dernière attaque", "R2": "historique (= A)",
        "R3": "mélange d'équilibre des deux côtés (= B)", "R4": "régularisation vers le passé"}
assert CODES["R0"] not in v4.BRAS.values() and CODES["R0"] not in (CODES["R1"], CODES["R4"])   # code neuf, libre
for _r, _c in CODES.items():
    v4.BRAS.setdefault(_r, _c)

# --- compteurs de coût : chaque appel à l'optimiseur et au solveur linéaire de la copie chargée est compté ----------
COMPTEUR: Counter = Counter()
_minimize_v4, _linprog_v4 = v4.minimize, v4.linprog


def _minimize_compte(*a, **k):
    COMPTEUR["minimize"] += 1
    return _minimize_v4(*a, **k)


def _linprog_compte(*a, **k):
    COMPTEUR["linprog"] += 1
    return _linprog_v4(*a, **k)


v4.minimize, v4.linprog = _minimize_compte, _linprog_compte


# =================================================================================================================
# Graines (R9) : dérivation propre, même schéma que le v4, racines du gel v1 seulement
# =================================================================================================================
_AUTORISATION_DECISION: dict = {"prereg_sha256": None}


def exiger_racine_permise_regles(racine: int) -> None:
    """Garde : une racine de décision exige l'autorisation par préenregistrement scellé ; sont refusées les racines de
    décision du v4, toutes les racines déjà employées (arène v1 à v4), la plage 20265001–20265999 d'une autre session,
    la plage 20264001–20264999 du v4 (réservée au v4), et toute racine absente du gel v1."""
    r = int(racine)
    if r in RACINES_DECISION:
        if _AUTORISATION_DECISION["prereg_sha256"] is None:
            raise GardeArret(f"racine de décision {r} sans autorisation : préenregistrement scellé exigé "
                             "(autoriser_decision_regles)")
        return
    if r in v4.RACINES_DECISION:
        raise GardeArret(f"racine {r} de décision de l'arène v4 : interdite dans ce module")
    if r in v4._DEJA_EMPLOYEES:
        raise GardeArret(f"racine {r} déjà employée (arène v1 à v4, contre-lectures) : interdite")
    if r in RACINES_EMPLOYEES_V1:
        raise GardeArret(f"racine {r} déjà employée par la v1 des règles (pilote ou essais) : interdite en v2")
    if v4.PLAGE_SESSION_VOISINE[0] <= r <= v4.PLAGE_SESSION_VOISINE[1]:
        raise GardeArret(f"racine {r} dans la plage {v4.PLAGE_SESSION_VOISINE} d'une autre session : interdite")
    if v4.PLAGE_V4[0] <= r <= v4.PLAGE_V4[1]:
        raise GardeArret(f"racine {r} dans la plage {v4.PLAGE_V4} de l'arène v4 : réservée au v4, interdite ici")
    if r not in _PERMISES_HORS_DECISION:
        raise GardeArret(f"racine {r} non gelée : seules les racines du gel v2 des règles ({PLAGE_REGLES[0]} à "
                         f"{PLAGE_REGLES[1]}, § 1) sont permises hors décision")


def gen_regles(racine: int, *cle: int) -> np.random.Generator:
    """`SeedSequence(entropy=racine, spawn_key=cle)` (même schéma que le v4, `SCHEMA_GRAINES`), racine permise."""
    exiger_numpy_minimal()
    exiger_racine_permise_regles(racine)
    return np.random.default_rng(np.random.SeedSequence(entropy=int(racine), spawn_key=tuple(int(c) for c in cle)))


v4.gen = gen_regles   # remplacement dans la copie chargée : loi_cible, Contexte, lois_tenues, … tirent de cette dérivation


def exiger_racines_essai_regles(racine: int, racine_tenue: int) -> None:
    for r in (racine, racine_tenue):
        if r is None:
            raise GardeArret("racine absente : racine d'essai gelée exigée")
        if int(r) in RACINES_DECISION:
            raise GardeArret(f"racine {r} réservée à la décision : interdite hors décision")
        exiger_racine_permise_regles(r)
    if int(racine) == int(racine_tenue):
        raise GardeArret("racine des familles tenues à l'écart égale à la racine principale : racine à part exigée")


def exiger_gel_regles(racines=(), chemin: str | Path | None = None) -> str:
    """Garde : le gel v2 est présent, à l'empreinte épinglée, et cite chaque racine employée. Renvoie l'empreinte."""
    p = Path(GEL if chemin is None else chemin)
    if not p.is_file():
        raise GardeArret(f"gel des règles absent : {p}")
    sha = empreinte_fichier(p)
    if sha != GEL_SHA256:
        raise GardeArret(f"gel des règles modifié : empreinte {sha} ≠ épinglée {GEL_SHA256}")
    texte = p.read_text(encoding="utf-8")
    for r in racines:
        if not re.search(rf"\b{int(r)}\b", texte):
            raise GardeArret(f"racine {r} absente du gel des règles : elle doit y être écrite avant emploi")
    return sha


# =================================================================================================================
# Identité et autorisation de décision (préenregistrement scellé exigé avant toute graine de décision)
# =================================================================================================================
def bloc_identite(cfg) -> str:
    import scipy

    lignes = [f"- Identifiant : {IDENTIFIANT_PREREG}",
              f"- Racines de décision : RACINE_DECISION = {RACINE_DECISION} ; RACINE_DECISION_TENUE = "
              f"{RACINE_DECISION_TENUE}",
              f"- Code : `{Path(__file__).name}` — {empreinte_fichier(__file__)}",
              f"- Arène v4 : `{ARENE_V4.name}` — {ARENE_V4_SHA256}",
              f"- Gel : `{GEL.name}` — {GEL_SHA256}",
              f"- Configuration (empreinte de la forme canonique) : {cfg.empreinte()}"]
    for f in FICHIERS_BIBLIOTHEQUE:
        lignes.append(f"- Bibliothèque `{f}` — {empreinte_fichier(DEPOT / f)}")
    lignes.append(f"- Versions : numpy {np.__version__} ; scipy {scipy.__version__} ; Python {sys.version.split()[0]}")
    lignes += ["", v4.DEBUT_CONFIG, "```json", json.dumps(asdict(cfg), indent=1, sort_keys=True, ensure_ascii=False),
               "```", v4.FIN_CONFIG]
    return "\n".join(lignes)


def exiger_identite_prereg_regles(texte: str, cfg, instances: str | None = None, lam: float | None = None,
                                  reference: str | None = None) -> None:
    """Garde : le préenregistrement est celui de ce module (identifiant, racines, configuration champ à champ,
    empreintes de ce code, de l'arène v4, du gel et de la bibliothèque, versions, N, λ* et référence gelés)."""
    import scipy

    if IDENTIFIANT_PREREG not in texte:
        raise GardeArret(f"préenregistrement sans l'identifiant {IDENTIFIANT_PREREG}")
    for nom, val in (("RACINE_DECISION", RACINE_DECISION), ("RACINE_DECISION_TENUE", RACINE_DECISION_TENUE)):
        if not re.search(rf"\b{nom}\s*=\s*{val}\b", texte):
            raise GardeArret(f"préenregistrement : {nom} = {val} absent ou différent du code")
    ecarts = v4.comparer_configuration(v4.extraire_configuration(texte), cfg)
    if ecarts:
        raise GardeArret("préenregistrement : configuration différente du code : " + " ; ".join(ecarts))
    for lib, sha in (("configuration", cfg.empreinte()), ("code", empreinte_fichier(__file__)),
                     ("arène v4", ARENE_V4_SHA256), ("gel", GEL_SHA256)):
        if not re.search(rf"\b{sha}\b", texte):
            raise GardeArret(f"préenregistrement : empreinte ({lib}) absente")
    for f in FICHIERS_BIBLIOTHEQUE:
        if not re.search(rf"\b{empreinte_fichier(DEPOT / f)}\b", texte):
            raise GardeArret(f"préenregistrement : empreinte de {f} absente")
    for nom, v in (("numpy", np.__version__), ("scipy", scipy.__version__)):
        if not re.search(rf"\b{nom} {re.escape(v)}(?![0-9.])", texte):
            raise GardeArret(f"préenregistrement : version {nom} {v} absente du texte")
    if instances is not None and instances != f"0:{cfg.n_instances}":
        raise GardeArret(f"--instances {instances} ≠ 0:{cfg.n_instances} (configuration gelée)")
    if lam is not None and not re.search(rf"LAMBDA_RETENU\s*=\s*{re.escape(f'{float(lam):g}')}(?![0-9.])", texte):
        raise GardeArret(f"préenregistrement : LAMBDA_RETENU = {float(lam):g} absent ou différent")
    if reference is not None and not re.search(rf"REFERENCE_RETENUE\s*=\s*{re.escape(reference)}\b", texte):
        raise GardeArret(f"préenregistrement : REFERENCE_RETENUE = {reference} absente ou différente")


def autoriser_decision_regles(chemin: str | Path, cfg, instances: str | None = None, lam=None, reference=None) -> str:
    from controle_ia.prereg import exiger_prereg_scelle

    sha = exiger_prereg_scelle(chemin)
    exiger_identite_prereg_regles(Path(chemin).read_text(encoding="utf-8"), cfg, instances, lam, reference)
    _AUTORISATION_DECISION["prereg_sha256"] = sha
    return sha


# =================================================================================================================
# Mesures
# =================================================================================================================
def exploitabilite(taux: float) -> float:
    """X = 1 − taux de détection de la meilleure réponse (valeur absolue, dans [0 ; 1]). Garde : taux dans [0 ; 1]."""
    t = float(taux)
    if not (np.isfinite(t) and -1e-12 <= t <= 1 + 1e-12):
        raise GardeArret(f"taux de détection hors de [0 ; 1] : {taux}")
    return float(min(max(1.0 - t, 0.0), 1.0))


def exploitabilite_moyenne_tours(x_par_tour) -> float:
    """X̄ = moyenne des X_t sur les T tours d'une trajectoire (gel v2 § 4). Garde : au moins un tour, valeurs finies
    dans [0 ; 1] ; résultat dans [0 ; 1]."""
    x = np.asarray(list(x_par_tour), float)
    if x.size == 0:
        raise GardeArret("X̄ : aucun tour")
    if not (np.all(np.isfinite(x)) and np.all(x >= -1e-12) and np.all(x <= 1 + 1e-12)):
        raise GardeArret(f"X̄ : exploitabilité par tour hors de [0 ; 1] : {x.tolist()}")
    return float(min(max(float(x.mean()), 0.0), 1.0))


def exiger_defense_figee(moniteurs: list, M0) -> None:
    """Garde de R0 : la liste des moniteurs est restée [M0] (aucun réentraînement, objet inchangé)."""
    if len(moniteurs) != 1 or moniteurs[0] is not M0:
        raise GardeArret("R0 : la défense figée a été modifiée (moniteur autre que M0, ou plus d'un moniteur)")


def exiger_regle(regle: str) -> None:
    if regle not in REGLES:
        raise GardeArret(f"règle inconnue : {regle!r} (règles : {', '.join(REGLES)})")


def exiger_lambda(lam) -> float:
    lam = float(lam)
    if not (np.isfinite(lam) and lam >= 0):
        raise GardeArret(f"R4 : λ négatif ou non fini : {lam}")
    return lam


# =================================================================================================================
# R4 : entraînement régularisé vers le passé (miroir de `entrainer` du v4 pour m = 1, plus la pénalité)
# =================================================================================================================
def penalite_direction(w: np.ndarray, u: np.ndarray, lam: float):
    """λ‖w/‖w‖ − u‖² = 2λ(1 − cos(w, u)), u unitaire ; renvoie (valeur, gradient). Direction indéfinie (w ≈ 0) :
    pénalité maximale 2λ et gradient nul (déclaré ; les départs ne sont jamais nuls)."""
    nw = float(np.linalg.norm(w))
    if not nw > 1e-12:
        return 2.0 * lam, np.zeros_like(w)
    c = float(w @ u) / nw
    return 2.0 * lam * (1.0 - c), -2.0 * lam * (u - c * w / nw) / nw


def objectif_regularise(p, Xp, Xa, cfg, u, lam):
    f, g = v4.objectif_detection(p, Xp, Xa, 1, cfg)
    if lam > 0:
        d = Xp.shape[1]
        pv, pg = penalite_direction(p[:d], u, lam)
        g = g.copy()
        g[:d] += pg
        return f + pv, g
    return f, g


def direction_reference(moniteurs: list, reference: str) -> np.ndarray:
    """u : direction unitaire du dernier moniteur déployé (« dernier ») ou moyenne des directions unitaires de tous
    les moniteurs passés (« moyenne » ; poids de moniteurs, non des jetons), renormalisée."""
    if reference == "dernier":
        w = np.asarray(moniteurs[-1].W[0], float)
    elif reference == "moyenne":
        w = np.mean([m.W[0] / np.linalg.norm(m.W[0]) for m in moniteurs], axis=0)
    else:
        raise GardeArret(f"R4 : référence inconnue : {reference!r} (« dernier » ou « moyenne »)")
    n = float(np.linalg.norm(w))
    if not n > 1e-12:
        raise GardeArret("R4 : direction de référence nulle")
    return w / n


def entrainer_regularise(Xp: np.ndarray, Xa: np.ndarray, cfg, u: np.ndarray, lam: float, directions=()):
    """Mêmes départs que `entrainer` du v4 (solution logistique, puis directions des moyennes jusqu'à `departs_entr`),
    même optimiseur (L-BFGS-B, `iter_entr`), objectif de détection plus pénalité ; à λ = 0, identique au bit à
    `entrainer`. Renvoie (moniteur linéaire, convergé)."""
    if cfg.entrainement != "detection":
        raise GardeArret(f"R4 : oracle « détection » exigé (configuration : {cfg.entrainement!r})")
    lam = exiger_lambda(lam)
    d = Xp.shape[1]
    res = v4._logistique(Xp, Xa, 1, cfg, np.zeros(d + 1))
    if not np.all(np.isfinite(res.x)) or not np.isfinite(res.fun):
        raise GardeArret("R4 : entraînement logistique : paramètres ou perte non finis")
    dirs = [np.asarray(v, float) for v in directions]
    departs = [res.x] + [np.concatenate([v, [0.0]]) for v in dirs[: max(cfg.departs_entr - 1, 0)]]
    meilleur = None
    for x in departs:
        r = v4.minimize(objectif_regularise, x, args=(Xp, Xa, cfg, u, lam), jac=True, method="L-BFGS-B",
                        options={"maxiter": cfg.iter_entr})
        if not np.all(np.isfinite(r.x)) or not np.isfinite(r.fun):
            raise GardeArret("R4 : entraînement régularisé : paramètres ou objectif non finis")
        if meilleur is None or r.fun < meilleur.fun:
            meilleur = r
    return v4.Moniteur(meilleur.x[:d].reshape(1, d), meilleur.x[d:]), bool(meilleur.success)


def entrainer_ctx_regularise(ctx, cb: int, tour: int, attaques, q, u: np.ndarray, lam: float):
    """Même échantillonnage des attaques, mêmes directions de départ et même calibration que `Contexte.entrainer`
    (m = 1), avec `entrainer_regularise` à la place de `entrainer`."""
    cfg = ctx.cfg
    q = v4.exiger_poids(q)
    n = cfg.n_attaque_entr // cfg.K
    comptes = np.floor(q * n).astype(int)
    reste = n - comptes.sum()
    comptes[np.argsort(-(q * n - comptes), kind="stable")[:reste]] += 1
    g = ctx.g(cb, tour, v4.ROLE_ATTAQUE_ENTR)
    Xa = np.vstack([v4.echantillonner(a, cfg.K * c, g, cfg) for a, c in zip(attaques, comptes) if c > 0])
    dirs = []
    for j in np.argsort(-q, kind="stable"):
        if q[j] <= 0:
            continue
        mu, _ = v4.deplier(attaques[j], cfg)
        dirs += [v / np.linalg.norm(v) for v in mu if np.linalg.norm(v) > 1e-12]
    mon, ok = entrainer_regularise(ctx.propre_entr(tour), Xa, cfg, u, lam, dirs)
    ctx.entr += 1
    ctx.nonconv += (not ok)
    return mon.calibrer(ctx.Xcal, cfg.alpha)


# =================================================================================================================
# Trajectoire commune aux quatre règles
# =================================================================================================================
def _cout_depuis(ctx, c0: dict, entr0: int, dep0: int) -> dict:
    return {"appels_optimiseur": COMPTEUR["minimize"] - c0.get("minimize", 0),
            "programmes_lineaires": COMPTEUR["linprog"] - c0.get("linprog", 0),
            "entrainements": ctx.entr - entr0, "departs_attaquant": ctx.att["departs"] - dep0}


def trajectoire_regle(regle: str, ctx, M0, lam: float = 0.0, reference: str = "dernier") -> dict:
    """Trajectoire coévolutive d'une règle (T tours). Même ordre d'opérations et mêmes clés de graine que
    `trajectoire` du v4 pour A (R2) et B (R3). R0 : M0 reste déployé, aucun entraînement (témoin « défense figée »).
    Renvoie l'état final (moniteurs, défense finale, attaques, mesures, dont X̄ = `exploitabilite_moyenne_tours`)."""
    exiger_regle(regle)
    lam = exiger_lambda(lam)
    if regle == "R4":
        direction_reference([M0], reference)     # garde : référence connue, avant tout calcul
    cfg, cb = ctx.cfg, CODES[regle]
    melange = regle == "R3"
    figee = regle == "R0"
    t0 = time.process_time()
    c0, entr0, dep0 = dict(COMPTEUR), ctx.entr, ctx.att["departs"]
    attaques = [ctx.cible]
    moniteurs = [M0]
    historique = [M0]
    cles_eval = [("eval", v4.COMMUN, 0)]
    eval_X = {cles_eval[0]: lambda: v4.echantillonner(ctx.cible, cfg.n_eval, ctx.g(v4.COMMUN, 0, v4.ROLE_EVAL), cfg)}
    G = np.array([[M0.taux_cache(cles_eval[0], eval_X[cles_eval[0]])]]) if melange else None
    p = np.array([1.0])
    par_tour = {k: [] for k in ("iii", "exploitabilite", "ii", "ii_sous_familles", "poids_max", "distance",
                                "nouveaute", "projections", "cpu_s", "valeur_jeu_restreint", "cos_consecutif")}
    deplacements: list[np.ndarray] = []

    def defense_courante():
        return list(zip(moniteurs, p)) if melange else [(moniteurs[-1], 1.0)]

    for t in range(1, cfg.T + 1):
        tt = time.process_time()
        if melange:
            p, _, _ = v4.resoudre_jeu(G)
        dfs = defense_courante()
        a, info = ctx.meilleure_reponse(dfs, ctx.delta, ctx.g(cb, t, v4.ROLE_MC), ctx.g(cb, t, v4.ROLE_DEPARTS),
                                        departs_suppl=[attaques[-1]])
        cle = ("eval", cb, t)
        eval_X[cle] = (lambda a=a, t=t: v4.echantillonner(a, cfg.n_eval, ctx.g(cb, t, v4.ROLE_EVAL), cfg))
        iii = v4.taux_defense(dfs, eval_X[cle]())
        par_tour["iii"].append(iii)
        par_tour["exploitabilite"].append(exploitabilite(iii))
        tenues = ctx.taux_tenues(dfs)
        par_tour["ii"].append(float(np.mean(tenues)))
        par_tour["ii_sous_familles"].append([float(np.mean(tenues[0::2])), float(np.mean(tenues[1::2]))])
        par_tour["poids_max"].append(float(max(w for _, w in dfs)))
        par_tour["distance"].append(info["distance_consommee"])
        par_tour["projections"].append(info["projections"])
        v = a - ctx.cible
        par_tour["nouveaute"].append(v4.residu_relatif(v, deplacements))
        deplacements.append(v)
        attaques.append(a)
        cles_eval.append(cle)
        uniforme = np.full(len(attaques), 1.0 / len(attaques))
        if figee:
            # R0 : aucune mise à jour ; M0 reste déployé ; cosinus consécutif 1 par construction (recopié, hors S12)
            par_tour["cos_consecutif"].append(1.0)
            historique.append(M0)
            par_tour["cpu_s"].append(time.process_time() - tt)
            v4.exiger_plafond(t0, cfg, f"règle {regle}, tour {t}")
            continue
        if regle == "R1":
            mon = ctx.entrainer(cb, t, [a], np.array([1.0]), 1)
        elif regle == "R2":
            mon = ctx.entrainer(cb, t, attaques, uniforme, 1)
        elif regle == "R3":
            col = np.array([[m.taux_cache(cle, eval_X[cle]) for m in moniteurs]]).T
            G = np.hstack([G, col])
            _, q, valeur = v4.resoudre_jeu(G)        # R3′ : les deux joueurs à l'équilibre du jeu restreint
            par_tour["valeur_jeu_restreint"].append(float(valeur))
            mon = ctx.entrainer(cb, t, attaques, q, 1)
            ligne = np.array([[mon.taux_cache(c, eval_X[c]) for c in cles_eval]])
            G = np.vstack([G, ligne])
        else:
            u = direction_reference(moniteurs, reference)
            mon = entrainer_ctx_regularise(ctx, cb, t, attaques, uniforme, u, lam)
        # dégénérescence (descriptif) : cosinus entre le moniteur nouveau et le dernier moniteur entraîné
        w0, w1 = moniteurs[-1].W[0], mon.W[0]
        par_tour["cos_consecutif"].append(float(w0 @ w1 / (np.linalg.norm(w0) * np.linalg.norm(w1) + 1e-300)))
        moniteurs.append(mon)
        historique.append(mon)
        par_tour["cpu_s"].append(time.process_time() - tt)
        v4.exiger_plafond(t0, cfg, f"règle {regle}, tour {t}")
    valeur_restreinte, equilibre = None, None
    if melange:
        p, _, valeur_restreinte = v4.resoudre_jeu(G)
        equilibre = {"poids_max_min": v4.poids_max_min_equilibres(G, valeur_restreinte),
                     "indice_poids_max": int(np.argmax(p)), "pur": v4.est_pur(p)}
    H = np.array([[mon.taux_cache(c, eval_X[c]) for c in cles_eval[1:]] for mon in historique])
    cycle = v4.indicateurs_cycle(H, par_tour["iii"], deplacements)
    if figee:
        exiger_defense_figee(moniteurs, M0)
    x_barre = exploitabilite_moyenne_tours(par_tour["exploitabilite"])   # X̄ (gel v2 § 4)
    return {"regle": regle, "lam": lam, "reference": reference if regle == "R4" else None, "moniteurs": moniteurs,
            "defense_finale": defense_courante(), "attaques": attaques, "cles_eval": cles_eval, "eval_X": eval_X,
            "par_tour": par_tour, "exploitabilite_moyenne_tours": x_barre, "valeur_jeu_restreint": valeur_restreinte,
            "equilibre": equilibre, "cycle": cycle, "cpu_trajectoire_s": time.process_time() - t0,
            "cout_trajectoire": _cout_depuis(ctx, c0, entr0, dep0)}


def finale_regle(regle: str, etat: dict, ctx, complete: bool = False) -> dict:
    """Défense figée, l'attaquant joue en dernier : `phase_finale` du v4 (standard puis renforcée ; V = la plus basse).
    Finale « légère » complétée de (ii) finale et de (i) sur les attaques vues ; `complete` ajoute courbe et coût de
    contournement du v4."""
    c0, entr0, dep0 = dict(COMPTEUR), ctx.entr, ctx.att["departs"]
    dfin = etat["defense_finale"]
    res = v4.phase_finale(regle, dfin, ctx, etat, leger=not complete)
    if not complete:
        tenues = ctx.taux_tenues(dfin)
        res["ii_final"] = float(np.mean(tenues))
        res["ii_final_sous_familles"] = [float(np.mean(tenues[0::2])), float(np.mean(tenues[1::2]))]
        cles, ex = etat["cles_eval"], etat["eval_X"]
        res["i_final_vus"] = float(np.mean([sum(w * m.taux_cache(c, ex[c]) for m, w in dfin if w > 0)
                                            for c in cles[1:]]))
    res["exploitabilite_finale"] = exploitabilite(res["V_iii_final"])
    res["cout_finale"] = _cout_depuis(ctx, c0, entr0, dep0)
    return res


def nom_variante(regle: str, lam=None, reference=None) -> str:
    return regle if regle != "R4" else f"R4[{reference},λ={float(lam):g}]"


def variantes(regles=REGLES, lambdas=GRILLE_LAMBDA, references=("dernier",)) -> list[tuple]:
    out = []
    for r in regles:
        exiger_regle(r)
        if r == "R4":
            out += [(r, exiger_lambda(lam), ref) for ref in references for lam in lambdas]
        else:
            out.append((r, None, None))
    return out


def executer_tache_regles(instance: int, code_delta: int, racine: int, racine_tenue: int, cfg, regles=REGLES,
                          lambdas=GRILLE_LAMBDA, references=("dernier",), complete: bool = False) -> dict:
    """Une tâche = (δ, instance) : contexte du v4, moniteur commun M0 (reproductibilité bit à bit exigée), puis chaque
    variante (règle, λ, référence) : trajectoire, finale, indicateurs, coût ; gardes du v4 en fin de tâche."""
    v4.exiger_config(cfg)
    vs = variantes(regles, lambdas, references)
    t0 = time.process_time()
    ctx = v4.Contexte(instance, code_delta, racine, racine_tenue, cfg)
    M0 = ctx.entrainer(v4.COMMUN, 0, [ctx.cible], np.array([1.0]), 1)
    M0_bis = ctx.entrainer(v4.COMMUN, 0, [ctx.cible], np.array([1.0]), 1)
    v4.exiger_meme_moniteur(M0, M0_bis)
    sortie = {"instance": instance, "code_delta": code_delta, "delta": ctx.delta, "racine": racine,
              "racine_tenue": racine_tenue, "config_sha256": cfg.empreinte(), "version": VERSION, "regles": {}}
    for regle, lam, ref in vs:
        M = v4.Moniteur(M0.W.copy(), M0.b.copy()).calibrer(ctx.Xcal, cfg.alpha)
        etat = trajectoire_regle(regle, ctx, M, lam or 0.0, ref or "dernier")
        res = finale_regle(regle, etat, ctx, complete)
        res.update({"regle": regle, "lam": lam, "reference": ref, "par_tour": etat["par_tour"],
                    "exploitabilite_moyenne_tours": etat["exploitabilite_moyenne_tours"],
                    "valeur_jeu_restreint": etat["valeur_jeu_restreint"], "cycle": etat["cycle"],
                    "cpu_trajectoire_s": etat["cpu_trajectoire_s"], "cout_trajectoire": etat["cout_trajectoire"],
                    "nb_moniteurs_stockes": len(etat["moniteurs"]),
                    "parametres_stockes": int(sum(m.nb_parametres for m in etat["moniteurs"]))})
        if etat["equilibre"] is not None:
            res["equilibre"] = etat["equilibre"]
        sortie["regles"][nom_variante(regle, lam, ref)] = res
        v4.exiger_plafond(t0, cfg, f"après la finale de {nom_variante(regle, lam, ref)}")
    sortie["entrainements"] = ctx.entr
    sortie["non_convergences"] = ctx.nonconv
    sortie["attaquant"] = {"departs": ctx.att["departs"], "non_finis": ctx.att["non_finis"],
                           "statuts": {str(k): v for k, v in sorted(ctx.att["statuts"].items())},
                           "iter_max": ctx.att["iter_max"], "reponses_a_la_limite": ctx.att["a_la_limite"]}
    v4.exiger_convergence(ctx.nonconv, ctx.entr, cfg)
    v4.exiger_departs_finis(ctx.att["non_finis"], ctx.att["departs"], cfg)
    sortie["cpu_tache_s"] = time.process_time() - t0
    return sortie


# =================================================================================================================
# Analyse : résumés par variante, contrastes appariés contre R2, intervalles par rééchantillonnage (comme le v4)
# =================================================================================================================
MESURES_CONTRASTE = (("V_iii_final", 0), ("ii_final", 1), ("exploitabilite_finale", 2),
                     ("exploitabilite_moyenne_tours", 8))   # X̄ : code 200 + 800 + rang = 1000 + rang (gel v2 § 4)
assert all(200 + 100 * j not in range(500, 800) for _, j in MESURES_CONTRASTE)   # aucune collision avec 500 à 799
MESURES_INDICATEUR = (("I1_progres", 0), ("I3_moins_nul", 1), ("I2_oubli", 2))


def _boot(x: np.ndarray, racine_reech: int, cd: int, code: int, n_reech: int) -> dict:
    g = gen_regles(racine_reech, cd, code, 0, 0, v4.ROLE_REECH)
    boot = x[g.integers(0, len(x), size=(n_reech, len(x)))].mean(1)
    return {"moyenne": float(x.mean()), "ecart_type": float(x.std(ddof=1)) if len(x) > 1 else float("nan"),
            "n": int(len(x)), "quantiles": v4._q(boot)}


def resume_variante(rs: list[dict], nom: str) -> dict:
    b = [r["regles"][nom] for r in rs]
    moy = lambda cle: float(np.mean([x[cle] for x in b]))   # noqa: E731
    out = {"V_iii_final": moy("V_iii_final"), "exploitabilite_finale": moy("exploitabilite_finale"),
           "exploitabilite_moyenne_tours": moy("exploitabilite_moyenne_tours"),
           "V_min_tache": float(np.min([x["V_iii_final"] for x in b])),
           "V_max_tache": float(np.max([x["V_iii_final"] for x in b])),
           "ii_final": moy("ii_final"), "i_final_vus": moy("i_final_vus"), "fpr_moyen": moy("fpr_final"),
           "standard_moins_renforce": float(np.mean([x["V_iii_standard"] - x["V_iii_renforce"] for x in b])),
           "iii_par_tour": [float(v) for v in np.mean([x["par_tour"]["iii"] for x in b], axis=0)],
           "exploitabilite_par_tour": [float(v) for v in np.mean([x["par_tour"]["exploitabilite"] for x in b], axis=0)],
           "ii_par_tour": [float(v) for v in np.mean([x["par_tour"]["ii"] for x in b], axis=0)],
           "cos_consecutif_moyen": float(np.mean([np.mean(x["par_tour"]["cos_consecutif"]) for x in b])),
           "cos_consecutif_par_tache": [float(np.mean(x["par_tour"]["cos_consecutif"])) for x in b],   # S12 (CL-11)
           "cycle": {k: (float(np.mean([x["cycle"][k] for x in b])) if all(x["cycle"][k] is not None for x in b)
                         else None) for k in ("I1_progres", "I2_oubli", "I3_retours", "I3_moins_nul")},
           "cout": {"cpu_trajectoire_s": moy("cpu_trajectoire_s"), "cpu_final_s": moy("cpu_final_s"),
                    **{k: float(np.mean([x["cout_trajectoire"][k] + x["cout_finale"][k] for x in b]))
                       for k in ("appels_optimiseur", "programmes_lineaires", "entrainements", "departs_attaquant")}},
           "parametres_deployes": int(b[0]["parametres_deployes"]), "parametres_stockes": int(b[0]["parametres_stockes"])}
    if all(x["valeur_jeu_restreint"] is not None for x in b):
        out["valeur_jeu_restreint_finale"] = moy("valeur_jeu_restreint")
        out["valeur_jeu_restreint_par_tour"] = [float(v) for v in
                                                np.mean([x["par_tour"]["valeur_jeu_restreint"] for x in b], axis=0)]
        out["poids"] = {"part_pure": float(np.mean([v4.est_pur(x["poids_finaux"]) for x in b])),
                        "support_moyen": float(np.mean([sum(v > 1e-6 for v in x["poids_finaux"]) for x in b]))}
    return out


def choisir_lambda(resultats: list[dict]) -> dict:
    """Règle du gel § 3 : parmi les variantes de R4 présentes dans toutes les tâches (les deux δ confondus), celle qui
    maximise la moyenne de V(R4) ; égalité à `TOLERANCE_CHOIX_LAMBDA` près → la plus petite λ (puis « dernier »)."""
    noms = [n for n in resultats[0]["regles"] if n.startswith("R4[") and all(n in r["regles"] for r in resultats)]
    if not noms:
        return {"retenu": None, "par_variante": {}}
    moyennes = {n: float(np.mean([r["regles"][n]["V_iii_final"] for r in resultats])) for n in noms}
    cles = {n: (resultats[0]["regles"][n]["lam"], 0 if resultats[0]["regles"][n]["reference"] == "dernier" else 1)
            for n in noms}
    meilleur = max(moyennes.values())
    candidats = [n for n in noms if moyennes[n] >= meilleur - TOLERANCE_CHOIX_LAMBDA]
    retenu = min(candidats, key=lambda n: cles[n])
    return {"retenu": retenu, "lam": cles[retenu][0], "reference": resultats[0]["regles"][retenu]["reference"],
            "par_variante": moyennes, "tolerance": TOLERANCE_CHOIX_LAMBDA, "regle": "max de la moyenne de V sur "
            "toutes les tâches ; égalité à la tolérance près → plus petite λ, puis « dernier »"}


def analyser_regles(resultats: list[dict], racine_reech: int, n_reech: int = 20000) -> dict:
    sortie = {}
    for cd in sorted({r["code_delta"] for r in resultats}):
        rs = sorted((r for r in resultats if r["code_delta"] == cd), key=lambda r: r["instance"])
        noms = [n for n in rs[0]["regles"] if all(n in r["regles"] for r in rs)]
        bloc = {"n": len(rs), "delta": rs[0]["delta"], "variantes": {n: resume_variante(rs, n) for n in noms},
                "contrastes_contre_R2": {}, "indicateurs": {}}
        for k, nom in enumerate(noms):
            if nom != "R2" and "R2" in noms:
                for mes, j in MESURES_CONTRASTE:
                    d = np.array([r["regles"][nom][mes] - r["regles"]["R2"][mes] for r in rs])
                    bloc["contrastes_contre_R2"][f"{nom} - R2 ({mes})"] = {
                        **_boot(d, racine_reech, cd, 200 + 100 * j + k, n_reech), "zeros_exacts": int(np.sum(d == 0))}
                # déclencheur 5 (CL-11) : le contraste sur V, attaquant standard seul contre renforcé seul
                d_std = np.array([r["regles"][nom]["V_iii_standard"] - r["regles"]["R2"]["V_iii_standard"] for r in rs])
                d_ren = np.array([r["regles"][nom]["V_iii_renforce"] - r["regles"]["R2"]["V_iii_renforce"] for r in rs])
                bloc["contrastes_contre_R2"][f"{nom} - R2 (V standard seul / renforce seul)"] = {
                    "moyenne_standard": float(d_std.mean()), "moyenne_renforce": float(d_ren.mean()),
                    "ecart": float(d_std.mean() - d_ren.mean())}
            for mes, j in MESURES_INDICATEUR:
                if all(r["regles"][nom]["cycle"][mes] is not None for r in rs):
                    x = np.array([r["regles"][nom]["cycle"][mes] for r in rs])
                    bloc["indicateurs"][f"{nom} {mes}"] = _boot(x, racine_reech, cd, 500 + 100 * j + k, n_reech)
        att = [r["attaquant"] for r in rs]
        bloc["attaquant"] = {"departs": int(sum(a["departs"] for a in att)),
                             "non_finis": int(sum(a["non_finis"] for a in att)),
                             "reponses_a_la_limite": int(sum(a["reponses_a_la_limite"] for a in att))}
        bloc["entrainements"] = int(sum(r["entrainements"] for r in rs))
        bloc["non_convergences"] = int(sum(r["non_convergences"] for r in rs))
        bloc["cpu_tache_s"] = {"moyenne": float(np.mean([r["cpu_tache_s"] for r in rs])),
                               "max": float(np.max([r["cpu_tache_s"] for r in rs]))}
        sortie[str(cd)] = bloc
    sortie["choix_lambda"] = choisir_lambda(resultats)
    return sortie


# =================================================================================================================
# Processus de travail (pool `spawn`, PID consignés, arrêt par PID : fonctions du v4 réemployées)
# =================================================================================================================
def _travail(args):
    instance, cd, racine, racine_tenue, cfg_dict, regles, lambdas, references, complete, prereg, lam_dec, ref_dec = args
    cfg = v4.Config(**{k: tuple(v) if isinstance(v, list) else v for k, v in cfg_dict.items()})
    if (racine in RACINES_DECISION or racine_tenue in RACINES_DECISION) and \
            _AUTORISATION_DECISION["prereg_sha256"] is None:
        if prereg is None:
            raise GardeArret("racine de décision dans un processus de travail sans préenregistrement")
        autoriser_decision_regles(prereg, cfg, None, lam_dec, ref_dec)
    return executer_tache_regles(instance, cd, racine, racine_tenue, cfg, tuple(regles), tuple(lambdas),
                                 tuple(references), complete)


def _lancer(taches, processus: int, fichier_pids=None, sceller_pids: bool = False) -> list:
    import multiprocessing as mp

    if processus <= 1:
        return [_travail(t) for t in taches]
    ancien = signal.signal(signal.SIGTERM, lever_sur_term)
    pids = []
    try:
        with mp.get_context("spawn").Pool(processus) as pool:
            pids = [(p.pid, v4._debut_processus(p.pid)) for p in pool._pool]
            v4._consigner_pids(pids, fichier_pids, sceller_pids)
            res = pool.map(_travail, taches, chunksize=1)
    finally:
        signal.signal(signal.SIGTERM, ancien)
        v4.arreter_par_pid(pids)
        v4.exiger_aucun_orphelin(pids)
    return res


def executer(instances, racine, racine_tenue, cfg, processus=2, regles=REGLES, lambdas=GRILLE_LAMBDA,
             references=("dernier",), complete=False, prereg=None, lam_dec=None, ref_dec=None, fichier_pids=None,
             sceller_pids=False):
    taches = [(i, cd, racine, racine_tenue, asdict(cfg), tuple(regles), tuple(lambdas), tuple(references), complete,
               None if prereg is None else str(prereg), lam_dec, ref_dec)
              for cd in range(1, len(cfg.deltas) + 1) for i in instances]
    m0 = time.perf_counter()
    res = _lancer(taches, processus, fichier_pids, sceller_pids)
    temps = {"mur_s": time.perf_counter() - m0, "cpu_somme_taches_s": float(sum(r["cpu_tache_s"] for r in res)),
             "processus": processus, "taches": len(taches)}
    return res, temps


def _versions() -> dict:
    import platform

    import scipy

    try:
        commit = subprocess.run(["git", "-C", str(DEPOT), "rev-parse", "HEAD"], capture_output=True,
                                text=True).stdout.strip()
    except OSError:
        commit = None
    return {"python": sys.version.split()[0], "numpy": np.__version__, "scipy": scipy.__version__,
            "plateforme": platform.platform(), "commit": commit, "code_sha256": empreinte_fichier(__file__),
            "arene_v4_sha256": ARENE_V4_SHA256, "gel_sha256": GEL_SHA256,
            "bibliotheque_sha256": {f: empreinte_fichier(DEPOT / f) for f in FICHIERS_BIBLIOTHEQUE}}


def _plage(s: str) -> list[int]:
    a, b = s.split(":")
    return list(range(int(a), int(b)))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sp = ap.add_subparsers(dest="mode", required=True)
    e = sp.add_parser("essai", help="racine d'essai gelée : pilote d'essai")
    e.add_argument("--instances", default="0:6")
    e.add_argument("--sortie", required=True)
    e.add_argument("--processus", type=int, default=2)
    e.add_argument("--racine", type=int, default=RACINE_ESSAI)
    e.add_argument("--racine-tenue", type=int, default=RACINE_ESSAI_TENUE)
    e.add_argument("--pids", default=None)
    e.add_argument("--T", type=int, default=None, help="tours (défaut : configuration v4, T = 8)")
    e.add_argument("--regles", default=",".join(REGLES))
    e.add_argument("--lambdas", default=",".join(f"{x:g}" for x in GRILLE_LAMBDA))
    e.add_argument("--references", default=",".join(REFERENCES))
    e.add_argument("--complete", action="store_true", help="finale complète du v4 (courbe et coût de contournement)")
    sp.add_parser("identite", help="bloc d'identité à recopier dans le préenregistrement")
    dc = sp.add_parser("decision", help="racine de décision : exige le préenregistrement scellé")
    dc.add_argument("--prereg", required=True)
    dc.add_argument("--instances", required=True)
    dc.add_argument("--run-id", required=True)
    dc.add_argument("--processus", type=int, default=2)
    dc.add_argument("--lambda", dest="lam", type=float, required=True, help="λ* gelé (LAMBDA_RETENU du texte)")
    dc.add_argument("--reference", required=True, help="référence gelée (REFERENCE_RETENUE du texte)")
    o = sp.add_parser("orphelins", help="R10 : vérifie (et, avec --arreter, arrête par PID) les processus consignés")
    o.add_argument("--pids", required=True)
    o.add_argument("--arreter", action="store_true")
    a = ap.parse_args(argv)
    cfg = v4.exiger_config(v4.CONFIG_V4)
    if a.mode == "identite":
        print(bloc_identite(cfg))
        return 0
    if a.mode == "orphelins":
        pids = v4.lire_pids(a.pids)
        if a.arreter:
            print(f"arrêtés par PID : {v4.arreter_par_pid(pids)}")
        v4.exiger_aucun_orphelin(pids)
        print("aucun processus de travail consigné ne tourne")
        return 0
    if a.mode == "essai":
        exiger_racines_essai_regles(a.racine, a.racine_tenue)
        sha_gel = exiger_gel_regles((a.racine, a.racine_tenue))
        if a.T is not None:
            cfg = v4.exiger_config(replace(cfg, T=int(a.T)))
        regles = tuple(a.regles.split(","))
        lambdas = tuple(float(x) for x in a.lambdas.split(","))
        references = tuple(a.references.split(","))
        sortie = v4._exiger_absent(Path(a.sortie))
        res, temps = executer(_plage(a.instances), a.racine, a.racine_tenue, cfg, a.processus, regles, lambdas,
                              references, a.complete, fichier_pids=a.pids)
        corps = {"mode": "essai", "version": VERSION,
                 "manifeste": {"racine": a.racine, "racine_tenue": a.racine_tenue, "schema_graines": cfg.schema_graines,
                               "codes_regles": CODES, "config": asdict(cfg), "config_sha256": cfg.empreinte(),
                               "versions": _versions(), "gel_sha256": sha_gel, "regles": regles, "lambdas": lambdas,
                               "references": references, "complete": a.complete, "commande": " ".join(sys.argv)},
                 "temps": temps, "analyse": analyser_regles(res, a.racine), "resultats": res}
        v4._ecrire_nouveau(sortie, corps)
        print(f"essai écrit : {sortie} ; {temps}")
        return 0
    # décision : le préenregistrement scellé est exigé AVANT toute graine de décision ; manifeste et résultats
    # rattachés sous runs/ et diag/ (bibliothèque du dépôt), comme le v4
    from controle_ia import manifeste as man

    sha = autoriser_decision_regles(a.prereg, cfg, a.instances, a.lam, a.reference)
    sha_gel = exiger_gel_regles(RACINES_DECISION)      # CL-08 : gel sur disque revérifié en décision (v2)
    chemin_m, _ = man.creer_manifeste(DEPOT, a.run_id, {"config": asdict(cfg), "config_sha256": cfg.empreinte(),
                                                        "racine": RACINE_DECISION, "racine_tenue": RACINE_DECISION_TENUE,
                                                        "instances": a.instances, "prereg_sha256": sha,
                                                        "lambda": a.lam, "reference": a.reference,
                                                        "gel_sha256": sha_gel,
                                                        "schema_graines": cfg.schema_graines, "codes_regles": CODES,
                                                        "versions": _versions()},
                                      ["regles-defense"], entropie=RACINE_DECISION, decisif=True, prereg=a.prereg,
                                      commande=" ".join(sys.argv))
    res, temps = executer(_plage(a.instances), RACINE_DECISION, RACINE_DECISION_TENUE, cfg, a.processus, REGLES,
                          (a.lam,), (a.reference,), False, prereg=a.prereg, lam_dec=a.lam, ref_dec=a.reference,
                          fichier_pids=chemin_m.parent / "pids-travail.txt", sceller_pids=True)
    man.ecrire_resultat(DEPOT, chemin_m, "resultats-regles-defense", {"temps": temps, "resultats": res})
    man.ecrire_resultat(DEPOT, chemin_m, "analyse-regles-defense", analyser_regles(res, RACINE_DECISION))
    print(f"run de décision écrit sous diag/{a.run_id}/")
    return 0


__all__ = ["v4", "REGLES", "CODES", "GRILLE_LAMBDA", "REFERENCES", "RACINE_ESSAI", "RACINE_ESSAI_TENUE",
           "RACINE_TESTS", "RACINE_TESTS_TENUE", "RACINE_TESTS_AUTRE", "RACINE_DECISION", "RACINE_DECISION_TENUE",
           "RACINES_EMPLOYEES_V1", "RACINE_REPRISE_PILOTE",
           "gen_regles", "exiger_racine_permise_regles", "exiger_racines_essai_regles", "exiger_gel_regles",
           "charger_arene_v4", "exploitabilite", "exploitabilite_moyenne_tours", "exiger_defense_figee", "trajectoire_regle", "finale_regle", "executer_tache_regles",
           "entrainer_regularise", "penalite_direction", "direction_reference", "analyser_regles", "choisir_lambda",
           "bloc_identite", "exiger_identite_prereg_regles", "autoriser_decision_regles", "COMPTEUR", "replace"]

if __name__ == "__main__":
    sys.exit(main())
