"""Plancher neuf des deux sondes figées de P3 à l'étape A de T0.7 (remède (a') : 800 directions ; R-2285, R-2298), v1 — fichier
neuf (R12).

Source : note v3 de l'analyste (`docs/notes/g0-deux-semaines-v1/t07-module-v2/erreur-premiere-espece-lectures-decisives-t07-v3.md`,
`760a562c…`), section 6 ; consigne `consigne-code-plancher-v3-t07-v1.md` (`88879387…`), point 3.

Les 200 directions de P3 ne suffisent plus ; tirer 800 directions neuves demande Σ, la covariance des jetons d'entraînement
génériques de chaque sonde figée, que le dépôt n'a pas (R-1916). Elle est **réextraite** à l'étape A, sur la carte de
l'étape A, par **le code de P3 appelé tel quel** (étapes 1 à 4 de `premier_test_ia.run._executer_apres_manifeste`, code
inchangé depuis le commit de P3 `97dd8290`) :

1. **Entrées de P3** (clé de configuration `donnees_p3`, quatre fichiers à leur empreinte, `donnees_p3_t07_v1.controler`) :
   manifeste du run de P3 (configuration et graines), résultat `sondes-figees.json` (faits exclus, lignes des enjeux,
   effectifs, principales, fils de l'entraînement), faits et textes des enjeux.
2. **Réglages de P3** (`reglages_de_p3`) : `harnais.modeles.regler_determinisme(fils de P3, carte)` (algorithmes
   déterministes, TF32 coupé, réductions en précision réduite coupées, espace de cuBLAS `:4096:8`) avant tout calcul ; les
   réglages antérieurs du processus sont rétablis à la sortie. Modèle et format de l'agent **de P3** (révision, variables du
   gabarit : `charger_modele_et_format(config.agent de P3, …)` ; jouet : graine « modele-jouet » de P3), contrôle du format
   de P3 (`premier_test_ia.run.controler_format_agent`).
3. **Données et découpage de P3** : `charger_faits`, `exemples_tromperie`, `preparer_tromperie` (faits exclus faute d'empan
   **égaux** à la liste écrite par P3, sinon arrêt), `tirer_enjeux` (graine « tirage-enjeux » ; lignes **égales** à celles
   écrites par P3), `preparer_enjeux`, `decouper` (graines « decoupage-<concept> » ; effectifs **égaux** à ceux de P3).
4. **Extraction** des exemples d'entraînement à la couche de la sonde (`premier_test_ia.entrainement.extraire`, passe unique
   du harnais, simple précision) ; validation non extraite (Σ et les sondes ne lisent que l'entraînement).
5. **Garde d'identité** (R11), deux recettes de P3 rejouées sur les jetons réextraits, comparées au fichier léger
   (`sondes-figees-legeres.npz`, `701f73bd…`) :
   - **témoin déterministe** (décisif) : la sonde « différence de moyennes » du même concept et de la même couche
     (`tromperie-difference_moyennes-c15`, la principale de la tromperie elle-même ; `enjeux-difference_moyennes-c15` pour
     les enjeux), refaite par `sondes.familles.entrainer` ; fonction directe des jetons d'entraînement, sans tirage ni
     itération : elle garde l'identité des jetons dont on tire Σ ;
   - **sonde principale** refaite par la recette de P3 (famille, couche, agrégation de la sonde figée, graine « sonde/<nom> »
     du manifeste de P3, réglages par défaut, fils de torch de P3) ; pour une principale autre que le témoin (les enjeux :
     linéaire, Adam, 300 époques), **seuls les paliers « identique » et « processeur » passent** : le calibrage (rapport,
     données synthétiques de même spectre) montre cette recette **chaotique** (écart relatif des poids 0,49 pour un bruit de
     10⁻⁴ par jeton, 0,50 pour un exemple retiré) : aucune tolérance au-delà de l'arithmétique n'y sépare le bruit d'une faute.
     Clé `garde_principale` : « decisive » (lettre de la consigne : la principale refaite doit passer) ou « rapportee » (écart
     écrit, réserve écrite, le témoin porte la garde) ;
   - **seconde garde** (la graine « plancher/<concept> » se lit dans le manifeste de P3) : les 200 directions redonnées par
     `premier_test_ia.entrainement.plancher_de` sous cette graine égalent celles du fichier léger (décisive).
   Tolérances fixées d'avance (`TOLERANCES`, recopiées dans la configuration, contrôlées à l'égalité en mode réel), trois
   paliers :
   - « identique » : égalité au bit près ;
   - « processeur » : écart relatif ≤ 10⁻⁶ (ordre des sommes selon les fils et les noyaux d'algèbre linéaire : mesuré 0 pour
     la différence de moyennes et la sonde linéaire, ≤ 6 × 10⁻¹¹ pour les directions, fils 1 contre 4, calibrage) ;
   - « carte » : au-delà, jusqu'à `carte_sonde` = 10⁻³ (témoin) et `carte_directions` = 10⁻² (directions) (configuration v8,
     CLP3-01, R-2305 ; v7 : 10⁻² et 10⁻¹, trop larges : « un exemple retiré » y passait) : accepté **avec une réserve écrite**,
     « cause non établie » (carte, ou faute d'étendue partielle des jetons réextraits ; sous les réglages et sur la carte de
     P3, la régénération R-679 a redonné le fichier complet au bit près : un écart de cet ordre n'est pas attendu). Au
     calibrage (v3, rejoué), un bruit de 10⁻³ par jeton donne 4,4 × 10⁻⁴ et 2,2 × 10⁻⁴ (témoin), 8,3 × 10⁻³ et 2,2 × 10⁻³
     (directions) : il passe ; **toutes les fautes calibrées sont arrêtées par le témoin** (la plus petite, « un exemple
     retiré » des enjeux, 4,3 × 10⁻³, à 4,3 fois le plafond) ; une faute plus petite que le plafond (une part d'exemples assez
     faible) peut encore passer au palier « carte », avec sa réserve : la garde n'arrête pas **toute** faute ;
   - au-delà : **échec** du bras (motif écrit).
   Écart relatif : ‖x′ − x‖ / ‖x‖ pour `w` et `q` ; |b′ − b| / (|b| + ‖w‖ · max ‖h‖) pour `b` (max ‖h‖ : plus grande norme
   d'un jeton d'entraînement réextrait ; aucune moyenne sur les jetons), maximum sur les directions pour la seconde garde.
6. **800 directions neuves** par `sondes.evaluation.plancher_apparie` (recette gardée, A6 (2)) sur les mêmes jetons, graine
   de T0.7 dérivée sous la clé « plancher/<sonde> » (`SeedSequence` du manifeste de T0.7, R9), noms
   `<sonde>-t07-plancher-<k>` (ceux de P3 sont `<sonde>-plancher-plancher-<k>`). Les 200 directions de P3 restent lues dans le fichier léger, en lecture descriptive.

**Contrôle avant l'ouverture** (CLP3-03, R-2305 ; `controler_avant_ouverture`, joué par la passe à blanc v2) : sceaux des
quatre entrées de P3, principales de P3 égales à celles de la configuration, témoin et directions de P3 au fichier léger,
**révision du modèle de P3 dans le cache local** (mode réel ; `revision_au_cache`, lecture hors ligne) ; une faute refuse la
passe à blanc (code 2) : l'étape A ne part pas.

**Repli** (R5) : toute faute détectée (entrée, modèle, données, garde en échec ; exceptions de `FAUTES_DU_BRAS`) **arrête ce
seul bras** : la sonde figée concernée n'a pas de
plancher décisif (« échec », motif écrit dans `reextraction-p3-t07.json`, `notation-t07.json` et l'index des scores) ; aucune
bascule vers les 200 directions de P3.
"""
from __future__ import annotations

import contextlib
import json
import os
import time
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..manifeste import generateur
from ..premier_test_ia import donnees as dn
from ..premier_test_ia import entrainement as en
from ..sondes.evaluation import plancher_apparie
from ..sondes.familles import Reglages, SondeLineaireJetons, entrainer
from . import donnees_p3_t07_v1 as d3
from .plancher_v3 import N_PLANCHER_P3

METHODE = "reextraction_p3_v1"
CLE_CONFIG = "plancher_figees"
TOLERANCES = {"processeur": 1e-6, "carte_sonde": 1e-3, "carte_directions": 1e-2}     # v8 (CLP3-01, R-2305)
PALIERS = ("identique", "processeur", "carte")
GARDES_PRINCIPALE = ("rapportee", "decisive")
FAMILLE_TEMOIN = "difference_moyennes"
SUFFIXE_PLANCHER = "-t07"            # noms des directions neuves : <sonde>-t07-plancher-<k> (plancher_apparie)
CONCEPTS_P3 = ("tromperie", "enjeux")
FICHIER_PLANCHERS = "planchers-figees-t07.npz"
# fautes qui arrêtent le seul bras (motif écrit, type compris) : garde, fichier, modèle absent du cache, carte, clé absente
FAUTES_DU_BRAS = (GardeArret, OSError, RuntimeError, ValueError, KeyError, MemoryError, TypeError, AttributeError, IndexError)  # CLP3-07
RESERVE_CARTE = ("écart au palier « carte », cause non établie : au-delà de l'arithmétique du processeur, sous les plafonds "
                 "de la configuration v8 ; carte (non-déterminisme sous des réglages pourtant déterministes, que la régénération R-679 "
                 "n'a pas vu) ou faute d'étendue partielle des jetons réextraits ; écarts dans reextraction-p3-t07.json")


# ----------------------------------------------------------------------------------------------------------------- configuration
def exiger_config(pf, mode: str) -> None:
    """Clé `plancher_figees` : {"methode": "reextraction_p3_v1", "n_p3": 200 (réel), "tolerances": {processeur, carte_sonde,
    carte_directions}, "garde_principale": "rapportee" | "decisive"} ; en mode réel, les tolérances fixées d'avance de ce
    module, à l'égalité."""
    if not isinstance(pf, dict) or set(pf) != {"methode", "n_p3", "tolerances", "garde_principale"}:
        raise GardeArret(f"{CLE_CONFIG} : objet aux clés methode, n_p3, tolerances, garde_principale attendu")
    if pf["garde_principale"] not in GARDES_PRINCIPALE:
        raise GardeArret(f"{CLE_CONFIG}.garde_principale = {pf['garde_principale']!r} : {GARDES_PRINCIPALE} attendu")
    if pf["methode"] != METHODE:
        raise GardeArret(f"{CLE_CONFIG}.methode = {pf['methode']!r} : {METHODE!r} seule admise")
    n = pf["n_p3"]
    if isinstance(n, bool) or not isinstance(n, int) or n < 2 or (mode == "reel" and n != N_PLANCHER_P3):
        raise GardeArret(f"{CLE_CONFIG}.n_p3 = {n!r} : {N_PLANCHER_P3} en mode réel (directions de P3, lecture descriptive), "
                         "au moins 2 en jouet")
    t = pf["tolerances"]
    if not isinstance(t, dict) or set(t) != set(TOLERANCES):
        raise GardeArret(f"{CLE_CONFIG}.tolerances : clés {sorted(TOLERANCES)} attendues")
    for k, v in t.items():
        if isinstance(v, bool) or not isinstance(v, (int, float)) or not 0.0 < float(v) < 1.0:
            raise GardeArret(f"{CLE_CONFIG}.tolerances.{k} = {v!r} : nombre dans ]0, 1[ attendu")
    if not float(t["processeur"]) < min(float(t["carte_sonde"]), float(t["carte_directions"])):
        raise GardeArret(f"{CLE_CONFIG}.tolerances : processeur < carte attendu")
    if mode == "reel" and {k: float(v) for k, v in t.items()} != TOLERANCES:
        raise GardeArret(f"mode réel : {CLE_CONFIG}.tolerances = {t} ; {TOLERANCES} fixées d'avance attendues")


# ---------------------------------------------------------------------------------------------------------------- réglages
@contextlib.contextmanager
def reglages_de_p3(fils: int, appareil: str):
    """`regler_determinisme` de P3 pendant la réextraction ; réglages antérieurs de torch rétablis à la sortie (la variable
    d'environnement de cuBLAS, posée par `setdefault`, reste)."""
    import torch

    from ..harnais.modeles import regler_determinisme
    m, d = torch.backends.cuda.matmul, torch.backends.cudnn
    avant = {"det": torch.are_deterministic_algorithms_enabled(), "fils": torch.get_num_threads(), "tf32": m.allow_tf32,
             "tf32_cudnn": d.allow_tf32, "cudnn_det": d.deterministic, "bench": d.benchmark,
             "bf16": m.allow_bf16_reduced_precision_reduction, "fp16": m.allow_fp16_reduced_precision_reduction}
    cuda_avant = bool(torch.cuda.is_available() and torch.cuda.is_initialized())
    cublas_avant = os.environ.get("CUBLAS_WORKSPACE_CONFIG")
    try:
        r = regler_determinisme(int(fils), appareil)
        yield {"reglages": r, "carte_deja_initialisee": cuda_avant, "cublas_workspace_avant": cublas_avant,
               "cublas_workspace": os.environ.get("CUBLAS_WORKSPACE_CONFIG")}
    finally:
        torch.use_deterministic_algorithms(avant["det"])
        torch.set_num_threads(avant["fils"])
        m.allow_tf32, d.allow_tf32, d.deterministic, d.benchmark = avant["tf32"], avant["tf32_cudnn"], avant["cudnn_det"], avant["bench"]
        m.allow_bf16_reduced_precision_reduction, m.allow_fp16_reduced_precision_reduction = avant["bf16"], avant["fp16"]


@contextlib.contextmanager
def fils_torch(n: int):
    import torch
    avant = torch.get_num_threads()
    try:
        torch.set_num_threads(int(n))
        yield int(torch.get_num_threads())
    finally:
        torch.set_num_threads(avant)


# ------------------------------------------------------------------------------------------------------------- entrées de P3
def lire_p3(racine: Path, d: dict) -> dict:
    """Sceaux des quatre fichiers (`donnees_p3_t07_v1.controler`), puis manifeste et résultat `sondes-figees` de P3."""
    fichiers = d3.controler(racine, d)
    m = json.loads((Path(racine) / d["manifeste_p3"]["chemin"]).read_text(encoding="utf-8"))
    r = json.loads((Path(racine) / d["sondes_figees_p3"]["chemin"]).read_text(encoding="utf-8"))["resultat"]
    for k in ("config", "graines"):
        if k not in m:
            raise GardeArret(f"manifeste de P3 : clé {k} absente")
    for k in ("donnees", "effectifs", "principales", "fils_entrainement_effectifs"):
        if k not in r:
            raise GardeArret(f"sondes-figees de P3 : clé {k} absente")
    return {"config": m["config"], "graines": m["graines"], "resultat": r, "fichiers": fichiers, "run_id": m.get("run_id")}


def exemples_p3(racine: Path, d: dict, p3: dict, fmt) -> dict:
    """Étape 2 de P3 (données génériques, identifiants et empans dans le gabarit de l'agent) et découpage par groupe, avec
    les fonctions de P3 et ses graines ; faits exclus, lignes des enjeux et effectifs égaux à ceux que P3 a écrits."""
    cfg, g, r = p3["config"], p3["graines"], p3["resultat"]
    faits = dn.charger_faits(Path(racine) / d["faits"]["chemin"], d["faits"]["sha256"])
    if cfg.get("n_faits_max") is not None:
        faits = faits[:int(cfg["n_faits_max"])]
    ex_t, exclus = en.preparer_tromperie(fmt, dn.exemples_tromperie(faits), int(cfg["retrait_fin_tromperie"]))
    if list(exclus) != list(r["donnees"]["faits_exclus"]):
        raise GardeArret(f"réextraction : faits sans empan {exclus[:10]} ≠ faits exclus écrits par P3 "
                         f"{list(r['donnees']['faits_exclus'])[:10]} (R11)")
    tir = dn.tirer_enjeux(dn.charger_enjeux(Path(racine) / d["enjeux"]["chemin"], d["enjeux"]["sha256"]),
                          generateur(g["tirage-enjeux"]), int(cfg["n_par_classe_enjeux"]))
    if [x["ligne"] for x in tir] != list(r["donnees"]["lignes_enjeux"]):
        raise GardeArret("réextraction : tirage des enjeux ≠ lignes écrites par P3 (R11)")
    ex_e = en.preparer_enjeux(fmt, tir, int(cfg["max_jetons_enjeux"]))
    sortie = {"faits_exclus": list(exclus)}
    for concept, ex in (("tromperie", ex_t), ("enjeux", ex_e)):
        if len(ex) != int(r["donnees"][f"exemples_{concept}"]):
            raise GardeArret(f"réextraction : {len(ex)} exemples de {concept}, {r['donnees'][f'exemples_{concept}']} écrits par P3 (R11)")
        idx_e, idx_v = dn.decouper([x["groupe"] for x in ex], generateur(g[f"decoupage-{concept}"]), float(cfg["part_entrainement"]))
        attendu = r["effectifs"][concept]
        if (len(idx_e), len(idx_v)) != (int(attendu["entrainement"]), int(attendu["validation"])):
            raise GardeArret(f"réextraction : découpage de {concept} {len(idx_e)}/{len(idx_v)} ≠ effectifs de P3 "
                             f"{attendu['entrainement']}/{attendu['validation']} (R11)")
        sortie[concept] = {"exemples": ex, "y": np.array([int(x["y"]) for x in ex], dtype=np.int64), "e": idx_e, "v": idx_v}
    return sortie


# ------------------------------------------------------------------------------------------------------------------ gardes
def _ecart(x, x0) -> float:
    x, x0 = np.asarray(x, dtype=np.float64), np.asarray(x0, dtype=np.float64)
    if x.shape != x0.shape:
        return float("inf")
    n0 = float(np.linalg.norm(x0))
    return float(np.linalg.norm(x - x0)) / n0 if n0 > 0 else (0.0 if not np.any(x) else float("inf"))


def ecarts_sonde(s, s0, h_max: float) -> dict:
    """Écarts relatifs de `w`, `b`, `q` d'une sonde refaite `s` à la sonde figée `s0`, et égalité au bit près."""
    for a in ("nom", "couche", "agregation", "famille"):
        if getattr(s, a, None) != getattr(s0, a, None):
            return {"identique": False, "ecart": float("inf"), "motif": f"{a} {getattr(s, a, None)!r} ≠ {getattr(s0, a, None)!r}"}
    if type(s) is not SondeLineaireJetons or type(s0) is not SondeLineaireJetons:
        return {"identique": False, "ecart": float("inf"), "motif": "sonde refaite ou figée hors de SondeLineaireJetons"}
    if (s.q is None) != (s0.q is None):
        return {"identique": False, "ecart": float("inf"), "motif": "requête q présente d'un seul côté"}
    w, w0 = np.asarray(s.w, dtype=np.float64), np.asarray(s0.w, dtype=np.float64)
    identique = bool(w.shape == w0.shape and np.array_equal(w, w0) and float(s.b) == float(s0.b)
                     and (s.q is None or np.array_equal(np.asarray(s.q, dtype=np.float64), np.asarray(s0.q, dtype=np.float64))))
    e = {"w": _ecart(w, w0), "b": abs(float(s.b) - float(s0.b)) / (abs(float(s0.b)) + float(np.linalg.norm(w0)) * h_max)}
    if s.q is not None:
        e["q"] = _ecart(s.q, s0.q)
    return {"identique": identique, "ecart": max(e.values()), "ecarts": e, "motif": None}


def palier(ecarts: list, plafond_carte: float, tolerances: dict) -> tuple[str, float]:
    """Palier d'une garde (le pire de ses éléments) : « identique », « processeur », « carte » ou « échec »."""
    if not ecarts:
        raise GardeArret("garde sans élément comparé")
    if any(x.get("motif") for x in ecarts):
        return "échec", float("inf")
    pire = max(float(x["ecart"]) for x in ecarts)
    if all(x["identique"] for x in ecarts):
        return "identique", pire
    if pire <= float(tolerances["processeur"]):
        return "processeur", pire
    if pire <= float(plafond_carte):
        return "carte", pire
    return "échec", pire


def garde_sonde(refaite, figee, h_max: float, tolerances: dict) -> dict:
    e = ecarts_sonde(refaite, figee, h_max)
    p, pire = palier([e], tolerances["carte_sonde"], tolerances)
    return {"palier": p, "ecart_max": pire, "detail": e, "tolerances": {"processeur": tolerances["processeur"],
                                                                         "carte": tolerances["carte_sonde"]}}


def garde_directions(redonnees: list, figees: list, h_max: float, tolerances: dict) -> dict:
    if [x.nom for x in redonnees] != [x.nom for x in figees]:
        return {"palier": "échec", "ecart_max": float("inf"), "motif": "noms des directions redonnées ≠ noms du fichier léger",
                "n": len(figees)}
    es = [ecarts_sonde(a, b, h_max) for a, b in zip(redonnees, figees)]
    p, pire = palier(es, tolerances["carte_directions"], tolerances)
    return {"palier": p, "ecart_max": pire, "n": len(es), "identiques": int(sum(e["identique"] for e in es)),
            "motif": next((e["motif"] for e in es if e.get("motif")), None),
            "tolerances": {"processeur": tolerances["processeur"], "carte": tolerances["carte_directions"]}}


# ----------------------------------------------------------------------------------------------------------------- réextraction
def charger_modele_p3(p3: dict, mode: str):
    """Modèle et format de l'agent de P3 (chaîne de P3 : `charger_modele_et_format`, graine « modele-jouet » de P3 en jouet ;
    réel : cache local seulement), puis contrôle du format de P3."""
    from ..environnements.lancer_pilote_a import charger_modele_et_format
    from ..harnais.run_harnais_factice import graine_entiere
    from ..premier_test_ia.run import controler_format_agent
    if p3["config"].get("mode") != mode:
        raise GardeArret(f"mode de P3 {p3['config'].get('mode')!r} ≠ mode de T0.7 {mode!r}")
    agent = p3["config"]["agent"]
    modele, fmt = charger_modele_et_format(agent, mode, graine_entiere(p3["graines"]["modele-jouet"]), hors_ligne=(mode == "reel"))
    return modele, fmt, controler_format_agent(fmt, agent, mode)


def reextraire(racine: Path, config: dict, figees: dict, graine_de, n_plancher: int,
               charger=charger_modele_p3, extraire=en.extraire) -> dict:
    """Étapes 1 à 6 (docstring du module) pour les sondes figées `figees` ({concept : sonde principale lue}). `graine_de(cle)` :
    graine entière de T0.7 pour la clé (dérivée du manifeste de T0.7). Rend {"par_sonde": {nom : {...}}, "rapport": {...}} ;
    une faute arrête le seul bras concerné (`etat` « échec », motif écrit), jamais l'étape A."""
    t0 = time.perf_counter()
    tol = {k: float(v) for k, v in config[CLE_CONFIG]["tolerances"].items()}
    n_p3 = int(config[CLE_CONFIG]["n_p3"])
    mode = config["mode"]
    par_sonde = {s.nom: {"concept": c, "etat": "échec", "motif": None, "directions": None} for c, s in figees.items()}
    rapport = {"methode": METHODE, "tolerances": tol, "n_plancher": int(n_plancher), "n_p3": n_p3, "durees_s": {}}
    if not figees:
        return {"par_sonde": {}, "rapport": {**rapport, "etat": "sans objet"}}

    def echec_global(motif: str) -> dict:
        for v in par_sonde.values():
            v["motif"] = motif
        rapport["etat"] = "échec"
        rapport["motif"] = motif
        rapport["durees_s"]["total"] = round(time.perf_counter() - t0, 2)
        return {"par_sonde": par_sonde, "rapport": rapport}

    try:
        d = config.get("donnees_p3")
        if d is None:
            raise GardeArret("donnees_p3 absente de la configuration : entrées de P3 non citées")
        d3.exiger_config(d, mode)
        p3 = lire_p3(racine, d)
        rapport["p3"] = {"run_id": p3["run_id"], "fichiers": p3["fichiers"], "agent": p3["config"].get("agent"),
                         "fils": p3["config"].get("fils"), "fils_entrainement_effectifs": p3["resultat"]["fils_entrainement_effectifs"]}
        for c, s in figees.items():
            if c not in CONCEPTS_P3 or p3["resultat"]["principales"].get(c) != s.nom:
                raise GardeArret(f"sonde figée {s.nom} ({c}) : principale de P3 {p3['resultat']['principales'].get(c)!r} attendue")
        appareil = "cuda" if mode == "reel" else "cpu"
        pile = contextlib.ExitStack()
        rapport["reglages"] = pile.enter_context(reglages_de_p3(int(p3["config"]["fils"]), appareil))
    except FAUTES_DU_BRAS as e:
        return echec_global(f"réextraction impossible : {type(e).__name__} : {e}")
    with pile:                                      # réglages de P3 jusqu'au dernier tirage ; rétablis ensuite
        jetons: dict = {}
        try:
            t = time.perf_counter()
            modele, fmt, controle_format = charger(p3, mode)
            rapport["format"] = controle_format
            rapport["durees_s"]["chargement"] = round(time.perf_counter() - t, 2)
            ex = exemples_p3(racine, d, p3, fmt)
            rapport["donnees"] = {"faits_exclus": ex["faits_exclus"],
                                  **{c: {"exemples": len(ex[c]["exemples"]), "entrainement": len(ex[c]["e"]), "validation": len(ex[c]["v"])}
                                     for c in CONCEPTS_P3}}
            t = time.perf_counter()
            for c, s in figees.items():
                couche = int(s.couche)
                seqs = extraire(modele, [ex[c]["exemples"][i] for i in ex[c]["e"]], [couche], None)[couche]
                jetons[c] = {"seqs": seqs, "y": ex[c]["y"][ex[c]["e"]], "couche": couche}
            rapport["durees_s"]["extraction"] = round(time.perf_counter() - t, 2)
            del modele
            _vider_carte()
        except FAUTES_DU_BRAS as e:
            return echec_global(f"réextraction impossible : {type(e).__name__} : {e}")
        rapport["jetons"] = {c: {"exemples": len(j["seqs"]), "jetons": int(sum(len(x) for x in j["seqs"])), "couche": j["couche"]}
                             for c, j in jetons.items()}
        for c, s in figees.items():
            _un_bras(racine, config, p3, c, s, jetons[c], par_sonde[s.nom], tol, n_p3, int(n_plancher), graine_de)
    rapport["etat"] = "établi" if all(v["etat"] == "établi" for v in par_sonde.values()) else (
        "échec" if all(v["etat"] == "échec" for v in par_sonde.values()) else "partiel")
    rapport["durees_s"]["total"] = round(time.perf_counter() - t0, 2)
    return {"par_sonde": par_sonde, "rapport": rapport}


def _un_bras(racine: Path, config: dict, p3: dict, c: str, s, j: dict, v: dict, tol: dict, n_p3: int, n_plancher: int, graine_de) -> None:
    """Garde d'identité (témoin déterministe ; sonde principale refaite), seconde garde, puis 800 directions neuves, pour une
    sonde figée ; une faute → « échec » de ce bras."""
    try:
        h_max = max(float(np.linalg.norm(np.asarray(x, dtype=np.float64), axis=1).max()) for x in j["seqs"])
        mode_principale = config[CLE_CONFIG]["garde_principale"]
        temoin = _temoin(racine, config, c, s)
        t = time.perf_counter()
        refait = entrainer(FAMILLE_TEMOIN, temoin.nom, int(temoin.couche), j["seqs"], j["y"], "max")
        v["garde_identite"] = {**garde_sonde(refait, temoin, h_max, tol), "sonde": temoin.nom, "role": "témoin déterministe "
                               "(différence de moyennes, même concept, même couche, mêmes jetons d'entraînement)",
                               "duree_s": round(time.perf_counter() - t, 2)}
        decisifs = [v["garde_identite"]["palier"]]
        if s.nom == temoin.nom:
            v["garde_principale"] = {"palier": v["garde_identite"]["palier"], "sonde": s.nom, "role": "la principale est le témoin"}
        else:
            t = time.perf_counter()
            with fils_torch(int(p3["resultat"]["fils_entrainement_effectifs"])) as fils:
                refaite = entrainer(s.famille, s.nom, int(s.couche), j["seqs"], j["y"], s.agregation, _graine_p3(p3, f"sonde/{s.nom}"),
                                    Reglages())
            e = ecarts_sonde(refaite, s, h_max)
            p, pire = palier([e], tol["processeur"], tol)              # aucun palier « carte » : recette chaotique (calibrage)
            v["garde_principale"] = {"palier": p, "ecart_max": pire, "detail": e, "sonde": s.nom, "fils_torch": fils,
                                     "mode": mode_principale, "tolerances": {"processeur": tol["processeur"], "carte": None},
                                     "duree_s": round(time.perf_counter() - t, 2)}
            if mode_principale == "decisive":
                decisifs.append(p)
            elif p == "échec":
                v["reserve_principale"] = (f"sonde principale {s.nom} refaite par la recette de P3 à un écart {pire:.3e} > "
                                           f"{tol['processeur']:g} (au-delà de l'arithmétique du processeur) ; rapportée, non décisive "
                                           "(garde_principale = rapportee) : le témoin déterministe porte la garde d'identité")
        cle_p3 = f"plancher/{c}"
        if cle_p3 in p3["graines"]:
            figees_p3 = _directions_p3(racine, config, s, n_p3)
            t = time.perf_counter()
            redonnees = en.plancher_de(s, {int(s.couche): j["seqs"]}, list(range(len(j["seqs"]))), n_p3, _graine_p3(p3, cle_p3))
            gd = {**garde_directions(redonnees, figees_p3, h_max, tol), "graine_p3": cle_p3, "duree_s": round(time.perf_counter() - t, 2)}
            decisifs.append(gd["palier"])
        else:
            gd = {"palier": "sans objet", "motif": f"graine {cle_p3} absente du manifeste de P3 : seconde garde non jouée"}
        v["garde_directions_p3"] = gd
        if "échec" in decisifs:
            raise GardeArret(f"garde d'identité en échec : témoin {v['garde_identite']['palier']} (écart "
                             f"{v['garde_identite']['ecart_max']:.3e}), principale {v['garde_principale']['palier']}, directions de P3 "
                             f"{gd['palier']} (écart {gd.get('ecart_max', float('nan')):.3e}) ; R11 : arrêt de ce bras, aucune bascule "
                             "vers les 200 directions de P3")
        v["palier"] = max(decisifs, key=PALIERS.index)
        v["reserve"] = RESERVE_CARTE if v["palier"] == "carte" else None
        t = time.perf_counter()
        cle = f"plancher/{s.nom}"
        directions = plancher_apparie(f"{s.nom}{SUFFIXE_PLANCHER}", int(s.couche), j["seqs"], s.agregation, int(n_plancher), graine_de(cle))
        v.update(directions=directions, graine=cle, n=len(directions), duree_tirage_s=round(time.perf_counter() - t, 2), etat="établi",
                 motif=None)
    except FAUTES_DU_BRAS as e:
        v["etat"], v["motif"], v["directions"] = "échec", f"{type(e).__name__} : {e}", None


def _temoin(racine: Path, config: dict, c: str, s):
    """Témoin déterministe de la garde d'identité : la sonde « différence de moyennes » du même concept et de la même couche,
    lue dans le fichier léger (pour la tromperie, la principale elle-même)."""
    from ..premier_test_ia.figees import lire_sondes
    nom = f"{c}-{FAMILLE_TEMOIN}-c{int(s.couche)}"
    if s.nom == nom:
        return s
    f = config["planchers_p3"]
    sondes, _, _ = lire_sondes(Path(racine) / f["chemin"], f["sha256"])
    par = {x.nom: x for x in sondes}
    if nom not in par:
        raise GardeArret(f"témoin {nom} absent du fichier léger de P3")
    x = par[nom]
    if int(x.couche) != int(s.couche) or x.agregation != "max" or getattr(x, "famille", None) != FAMILLE_TEMOIN:
        raise GardeArret(f"témoin {nom} : couche, agrégation ou famille inattendues")
    return x


def _graine_p3(p3: dict, cle: str) -> int:
    from ..harnais.run_harnais_factice import graine_entiere
    if cle not in p3["graines"]:
        raise GardeArret(f"graine {cle} absente du manifeste de P3")
    return graine_entiere(p3["graines"][cle])


def _directions_p3(racine: Path, config: dict, s, n: int) -> list:
    """Les 200 directions de P3 de la sonde `s` (fichier léger, `lecture_v1.charger_planchers_p3` à 200 directions)."""
    from . import lecture_v1 as lv1
    concept_de = {v: k for k, v in config["sondes_par_concept"].items() if v is not None}
    r = lv1.charger_planchers_p3(racine, {**config, "n_plancher": int(n)}, [s])
    if s.nom not in r.get("directions", {}) or concept_de.get(s.nom) not in CONCEPTS_P3:
        raise GardeArret(f"directions de P3 de {s.nom} introuvables dans le fichier léger")
    return r["directions"][s.nom]


def _vider_carte() -> None:
    import gc

    import torch
    gc.collect()
    if torch.cuda.is_available() and torch.cuda.is_initialized():
        torch.cuda.empty_cache()


FICHIERS_MODELE = ("config.json", "tokenizer.json", "tokenizer_config.json")


def revision_au_cache(modele: str, revision: str, cache_dir: str | None = None) -> dict:
    """La révision `revision` de `modele` est-elle entière dans le cache local ? Lecture hors ligne seulement
    (`snapshot_download(local_files_only=True)`, aucun accès au réseau) : dossier de la révision, fichiers essentiels non vides,
    poids non vides ; avec des morceaux `model-<i>-of-<n>.safetensors`, index exigé, lisible, `weight_map` non vide, autant de
    morceaux que le nom en annonce, chacun présent (CLC-P3-03, R-2311). Toute faute → `GardeArret`."""
    import json as _json
    import re

    from huggingface_hub import snapshot_download
    try:
        dossier = Path(snapshot_download(repo_id=modele, revision=revision, local_files_only=True, cache_dir=cache_dir))
    except Exception as e:                                      # absente du cache : l'API rend une erreur de lecture locale
        raise GardeArret(f"modèle de P3 {modele}@{revision[:12]} absent du cache local ({type(e).__name__}) : la réextraction ne "
                         "télécharge jamais") from None
    if dossier.name != revision:
        raise GardeArret(f"modèle de P3 : dossier du cache {dossier.name[:12]} ≠ révision {revision[:12]}")
    manquants = [n for n in FICHIERS_MODELE if not (dossier / n).is_file()]
    index = dossier / "model.safetensors.index.json"
    poids = sorted(x.name for x in dossier.glob("*.safetensors"))
    nommes = [x for x in poids if re.fullmatch(r"model-\d+-of-\d+\.safetensors", x)]
    if nommes and not index.is_file():
        manquants.append("model.safetensors.index.json (morceaux sans index)")
    if index.is_file():
        try:
            carte = _json.loads(index.read_text(encoding="utf-8"))["weight_map"]
            if not isinstance(carte, dict) or not carte:
                raise ValueError("weight_map vide ou mal formée")
            attendus = sorted(set(str(v) for v in carte.values()))
        except (OSError, ValueError, KeyError, TypeError) as e:
            raise GardeArret(f"modèle de P3 {modele}@{revision[:12]} : index des poids illisible ({type(e).__name__} : {e})") from None
        annonces = {int(m.group(1)) for x in attendus if (m := re.fullmatch(r"model-\d+-of-(\d+)\.safetensors", x))}
        if len(annonces) > 1 or (annonces and len(attendus) != annonces.pop()):
            manquants.append(f"index : {len(attendus)} morceaux, nombre annoncé par leurs noms différent")
        manquants += [x for x in attendus if not (dossier / x).is_file()]
    elif not poids:
        manquants.append("*.safetensors")
    manquants += [f"{x} (taille nulle)" for x in list(FICHIERS_MODELE) + poids if (dossier / x).is_file() and (dossier / x).stat().st_size == 0]
    if manquants:
        raise GardeArret(f"modèle de P3 {modele}@{revision[:12]} incomplet au cache local : {manquants}")
    return {"modele": modele, "revision": revision, "dossier": str(dossier), "poids": len(poids)}


def controler_avant_ouverture(racine: Path, config: dict, cache_dir: str | None = None) -> dict:
    """CLP3-03 : ce dont la réextraction a besoin, contrôlé avant l'ouverture de l'étape A (passe à blanc) : clé
    `plancher_figees`, sceaux des quatre entrées de P3, principales de P3 égales à celles de la configuration, témoin et
    directions de P3 de chaque sonde figée au fichier léger, révision du modèle de P3 dans le cache local (mode réel ;
    jouet : sans objet). Faute → `GardeArret` (refus de la passe à blanc)."""
    from ..premier_test_ia.figees import lire_sondes
    if CLE_CONFIG not in config:
        raise GardeArret(f"configuration : clé {CLE_CONFIG} absente")
    mode = config["mode"]
    exiger_config(config[CLE_CONFIG], mode)
    d = config.get("donnees_p3")
    if d is None:
        raise GardeArret("donnees_p3 absente de la configuration : entrées de P3 non citées")
    d3.exiger_config(d, mode)
    p3 = lire_p3(racine, d)
    f = config["planchers_p3"]
    sondes, _, sha = lire_sondes(Path(racine) / f["chemin"], f["sha256"])
    par = {x.nom: x for x in sondes}
    figees = {}
    for c in CONCEPTS_P3:
        nom = config["sondes_par_concept"].get(c)
        if nom is None:
            continue
        if p3["resultat"]["principales"].get(c) != nom:
            raise GardeArret(f"sonde figée {nom} ({c}) : principale de P3 {p3['resultat']['principales'].get(c)!r}")
        if nom not in par:
            raise GardeArret(f"sonde figée {nom} absente du fichier léger")
        s = par[nom]
        temoin = _temoin(racine, config, c, s)
        n = len(_directions_p3(racine, config, s, int(config[CLE_CONFIG]["n_p3"])))
        figees[nom] = {"concept": c, "couche": int(s.couche), "temoin": temoin.nom, "directions_p3": n,
                       "graine_seconde_garde": f"plancher/{c}" in p3["graines"]}
    if not figees:
        raise GardeArret("aucune sonde figée de P3 nommée par la configuration")
    agent = p3["config"].get("agent") or {}
    if mode == "reel":
        cache = revision_au_cache(str(agent.get("modele")), str(agent.get("revision")), cache_dir)
    else:
        cache = {"etat": "sans objet (mode jouet : modèle jouet, aucun cache)"}
    return {"regle": "CLP3-03 (R-2305) : entrées de la réextraction contrôlées avant l'ouverture de l'étape A", "p3": p3["fichiers"],
            "fichier_leger": {"chemin": f["chemin"], "sha256": sha}, "figees": figees, "modele_p3": cache}


def rapport_serialisable(r: dict) -> dict:
    """Le rapport et l'état de chaque bras, sans les directions (objets)."""
    return {"rapport": r["rapport"], "par_sonde": {n: {k: v for k, v in x.items() if k != "directions"} for n, x in r["par_sonde"].items()}}


def ecrire_planchers(racine_sortie: Path, run_t07: str, r: dict) -> dict | None:
    """`donnees/<run-t07>/planchers-figees-t07.npz` (`figees.ecrire_sondes`, scellé) : les directions neuves des bras établis."""
    from ..premier_test_ia.figees import ecrire_sondes
    etablis = {n: x for n, x in r["par_sonde"].items() if x["etat"] == "établi"}
    if not etablis:
        return None
    rel = f"donnees/{run_t07}/{FICHIER_PLANCHERS}"
    sondes = [p for x in etablis.values() for p in x["directions"]]
    sha = ecrire_sondes(Path(racine_sortie) / rel, sondes, {"planchers": {n: [p.nom for p in x["directions"]] for n, x in etablis.items()},
                                                            "graines": {n: x["graine"] for n, x in etablis.items()}, "methode": METHODE})
    return {"chemin": rel, "sha256": sha, "directions": {n: len(x["directions"]) for n, x in etablis.items()}}


__all__ = ["revision_au_cache", "controler_avant_ouverture", "FICHIERS_MODELE", "METHODE", "CLE_CONFIG", "TOLERANCES", "PALIERS", "SUFFIXE_PLANCHER", "FICHIER_PLANCHERS", "RESERVE_CARTE", "exiger_config",
           "reglages_de_p3", "lire_p3", "exemples_p3", "ecarts_sonde", "palier", "garde_sonde", "garde_directions",
           "charger_modele_p3", "reextraire", "rapport_serialisable", "ecrire_planchers"]
