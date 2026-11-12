"""Lecture des COMPTES de la garde d'équivalence d'une sortie de T0.6 (course exploratoire, ordre
`docs/notes/g0-deux-semaines-v1/e3-ter-v1/ordre-course-dose-reponse-exploratoire-v1-*.md`, § 4 A), v1.

EXPLORATOIRE, NON OPPOSABLE (R-522) : ce script ne lit ni sonde, ni score, ni aire, ni verdict ; il rend des comptes seuls.

Clés lues, et seulement elles (celles que la chaîne écrit réellement : `t06/lanceur.py` l. 147-151, 266-270, 292-305 ;
`lanceur_v5.py` / `lanceur_v6.py` l. 192, 262-268, 287-296 ; `manifeste.ecrire_resultat` enveloppe tout résultat sous
`{"run_id", "manifeste_sha256", "resultat"}`) :
- `runs/<run>/manifeste.json` : `config` (`fraction_equivalence`, `T`, `N`, tolérances), `graines` (clés `tache/<id>` et
  `distillation/tache/<id>/e<k>`), `commit`, `versions.numpy` ; le tirage des pas contrôlés est REJOUÉ à l'identique
  (`manifeste.generateur`, puis les deux tirages de `pilote_a.graines_des_actions` l. 73-76 et `gen.random(T)`) : il donne
  les PAIRES (tâche, pas) indépendantes retenues, les mêmes dans toutes les conditions d'un état ;
- `diag/<run>/episodes-t06.json` → `resultat.fiches[k].phase`, `.condition`, `.equivalence.{actions, tolerance, statistique,
  ecarts_q99, ecarts}` ; `resultat.controles_negatifs[<état>]` ; `resultat.etats` (`adaptateur`, `dose`, `empreinte` : rien
  d'autre n'y est écrit, CLE3T-06) ; `resultat.descriptifs.{memoire_pic_gio, duree_s, longueur_remplie_max}` (descriptifs) ;
- `diag/<run>/distillation-t06.json` → `resultat.controle_negatif_donnees` SEUL (aucun écart par action n'y est écrit :
  `comparables + courtes` tient lieu de nombre d'actions contrôlées), `resultat.duree_s` ;
- `diag/<run>/arret.json` → `resultat.etape`, `resultat.motif` (arrêt consigné par le lanceur de run, `GardeArret`).

Une clé obligatoire absente ARRÊTE le script (code 2, message qui nomme la clé) : jamais un zéro silencieux (R5). Les
descriptifs facultatifs absents sont marqués « absent ».

Règle de lecture « E3-6 réglé / non réglé » (transcription de l'ordre, § 0, § 2, § 3, § 4 A, § 6, § 9.1 ; à contre-lire) :
RÉGLÉ si, et seulement si : aucun `arret.json` ; distillation et épisodes présents ; les états d'évaluation annoncés
(`etats`) ont tous des fiches ; dans chaque état ET dans la distillation, au moins une action contrôlée (garde exercée de
fait, adaptateurs injectés compris) ; dans chaque état, le plus grand `ecarts_q99` par couche ≤ tolérance ; le contrôle
négatif de chaque état et de la distillation est lu « conforme » (comparables ≥ `actions_min_controle_negatif` et fraction
≥ `fraction_min_controle_negatif`, lecture écrite par la chaîne). Sinon NON RÉGLÉ, avec tous les motifs ; un arrêt est lu
d'avance : (i) « activations de génération ≠ passe unique » (inéquivalence réelle à la tolérance), (ii) « aveugle au
décalage d'un jeton » (contrôle négatif de phase), sinon « autre » ; dans les deux cas : nœud de Lazar (§ 6).

    PYTHONPATH=src python3 scripts/extraire_garde_equivalence_t06_v1.py RACINE [--run RUN_ID] [--sortie DOSSIER]

RACINE : racine d'un clone de la branche d'essai (`runs/`, `diag/`). Sans `--run`, un seul `runs/*-t06-*/manifeste.json` est
exigé. `--sortie` écrit `<DOSSIER>/garde-equivalence-<run>-exploratoire-non-opposable-r522.json` (R12 : jamais écrasé).
Bibliothèque standard et numpy ; `controle_ia.manifeste.generateur` (le même que la chaîne) ; aucun réseau.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

STATUT = "EXPLORATOIRE, NON OPPOSABLE (R-522)"
ABSENT = "absent"
MOTIF_I = "activations de génération ≠ passe unique"
MOTIF_II = "aveugle au décalage d'un jeton"
CONDITIONS_DISTILLATION = 2          # `configuration.SOURCES_DISTILLATION` : saboteur et témoin partagent le générateur (lanceur.py l. 147-151)
_RACINE_DEPOT = Path(__file__).resolve().parent.parent


class CleAbsente(SystemExit):
    """Clé obligatoire absente : arrêt explicite (code 2), jamais un zéro silencieux."""

    def __init__(self, message: str):
        super().__init__(2)
        self.message = message


def _generateur():
    try:
        from controle_ia.manifeste import generateur
    except ModuleNotFoundError:
        sys.path.insert(0, str(_RACINE_DEPOT / "src"))
        from controle_ia.manifeste import generateur
    return generateur


def _exiger(d, chemin: tuple, contexte: str):
    """Valeur à `chemin` dans `d` ; toute clé manquante arrête avec son nom complet."""
    x = d
    vus = []
    for k in chemin:
        vus.append(str(k))
        if not isinstance(x, dict) or k not in x:
            raise CleAbsente(f"clé absente : {contexte} → {'.'.join(vus)} (jamais lue comme zéro)")
        x = x[k]
    return x


def _lire_json(chemin: Path, contexte: str) -> dict:
    if not chemin.is_file():
        raise CleAbsente(f"fichier absent : {contexte} ({chemin})")
    return json.loads(chemin.read_text(encoding="utf-8"))


def _sha256(chemin: Path) -> str:
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def _compagnon(chemin: Path):
    c = chemin.with_name(chemin.name + ".sha256")
    if not c.is_file():
        return ABSENT
    return c.read_text(encoding="utf-8").split()[0] if c.read_text(encoding="utf-8").split() else ABSENT


def trouver_manifeste(racine: Path, run_id: str | None) -> Path:
    if run_id:
        return racine / "runs" / run_id / "manifeste.json"
    candidats = sorted(p for p in (racine / "runs").glob("*-t06-*/manifeste.json")) if (racine / "runs").is_dir() else []
    if len(candidats) != 1:
        raise CleAbsente(f"un seul runs/*-t06-*/manifeste.json attendu sous {racine}, {len(candidats)} trouvé(s) : préciser --run")
    return candidats[0]


def rejouer_tirage(graine: dict, N: int, T: int, fraction: float, generateur) -> list[int]:
    """Pas contrôlés d'un générateur, exactement comme la chaîne : `graines_des_actions(gen, N, T)` consomme
    `gen.integers(0, 2**31 - 1, size=N*T)` (pilote_a.py l. 73-76), puis `gen.random(T) < fraction` (lanceur.py l. 150-151, 269-270)."""
    gen = generateur(graine)
    gen.integers(0, 2 ** 31 - 1, size=N * T)
    tirages = gen.random(T)
    return [s for s in range(T) if tirages[s] < fraction]


def paires_independantes(manifeste: dict) -> dict:
    """Paires (tâche, pas) indépendantes retenues par le tirage, en évaluation (clés `tache/<id>`) et en génération des données
    de distillation (clés `distillation/tache/<id>/e<k>`)."""
    cfg = _exiger(manifeste, ("config",), "manifeste")
    fraction = float(_exiger(cfg, ("fraction_equivalence",), "manifeste.config"))
    T = int(_exiger(cfg, ("T",), "manifeste.config"))
    N = int(_exiger(cfg, ("N",), "manifeste.config"))
    graines = _exiger(manifeste, ("graines",), "manifeste")
    generateur = _generateur()
    evaluation = {k[len("tache/"):]: rejouer_tirage(g, N, T, fraction, generateur)
                  for k, g in sorted(graines.items()) if k.startswith("tache/")}
    distillation = {k[len("distillation/tache/"):]: rejouer_tirage(g, N, T, fraction, generateur)
                    for k, g in sorted(graines.items()) if k.startswith("distillation/tache/")}
    if not evaluation:
        raise CleAbsente("manifeste.graines : aucune clé `tache/<id>` (tâches d'évaluation)")
    if not distillation:
        raise CleAbsente("manifeste.graines : aucune clé `distillation/tache/<id>/e<k>` (générateurs de distillation)")

    def bilan(d: dict) -> dict:
        return {"generateurs": len(d), "paires": len(d) * T, "retenues": sum(len(v) for v in d.values()),
                "retenues_par_generateur": {k: len(v) for k, v in d.items()}, "pas_retenus": {k: v for k, v in d.items() if v}}
    return {"fraction_equivalence": fraction, "T": T, "N": N, "evaluation": bilan(evaluation), "distillation": bilan(distillation)}


def _max_par_couche(fiches: list[dict], cle: str) -> dict:
    """Plus grand écart par couche sur toutes les actions contrôlées des fiches (clé `ecarts_q99` ou `ecarts`)."""
    maxima: dict = {}
    for f in fiches:
        for action, par_couche in _exiger(f, ("equivalence", cle), "episodes-t06.resultat.fiches[k]").items():
            for couche, v in par_couche.items():
                v = float(v)
                if couche not in maxima or v != v or v > maxima[couche]:      # NaN illisible : gardé tel quel, lu comme faute
                    maxima[couche] = v
    return dict(sorted(maxima.items(), key=lambda kv: int(kv[0])))


def lire_evaluation(ep: dict, paires: dict, cfg: dict) -> dict:
    r = _exiger(ep, ("resultat",), "episodes-t06")
    fiches = _exiger(r, ("fiches",), "episodes-t06.resultat")
    cn = _exiger(r, ("controles_negatifs",), "episodes-t06.resultat")
    etats = _exiger(r, ("etats",), "episodes-t06.resultat")
    tol = float(_exiger(cfg, ("tolerance_equivalence",), "manifeste.config"))
    phases: dict = {}
    for nom in sorted(etats):
        f_phase = [f for f in fiches if _exiger(f, ("phase",), "fiche") == nom]
        conditions = sorted({_exiger(f, ("condition",), "fiche") for f in f_phase})
        actions = sum(len(_exiger(f, ("equivalence", "actions"), "fiche")) for f in f_phase)
        tolerances = sorted({float(_exiger(f, ("equivalence", "tolerance"), "fiche")) for f in f_phase})
        statistiques = sorted({str(_exiger(f, ("equivalence", "statistique"), "fiche")) for f in f_phase})
        q99 = _max_par_couche(f_phase, "ecarts_q99")
        maxi = _max_par_couche(f_phase, "ecarts")
        b = _exiger(cn, (nom,), "episodes-t06.resultat.controles_negatifs")
        bilan = {k: _exiger(b, (k,), f"controles_negatifs[{nom}]") for k in
                 ("comparables", "passent", "courtes", "echecs", "fraction", "min_des_maxima", "lecture")}
        bilan["echecs"] = {"nombre": len(bilan["echecs"]), "dix_premiers": list(bilan["echecs"])[:10]}
        phases[nom] = {"etat": etats[nom], "conditions": conditions, "fiches": len(f_phase), "actions_controlees": actions,
                       "actions_attendues_du_tirage": paires["evaluation"]["retenues"] * len(conditions),
                       "tolerances": tolerances, "statistiques": statistiques,
                       "ecart_q99_max_par_couche": q99, "ecart_max_par_couche": maxi,
                       "couches_q99_au_dessus_tolerance": sorted((c for c, v in q99.items() if not v <= tol), key=int),
                       "controle_negatif": bilan}
    return {"etats": len(etats), "fiches": len(fiches), "phases": phases,
            "phases_sans_fiche": [n for n, p in phases.items() if p["fiches"] == 0]}


def lire_distillation(di: dict, paires: dict) -> dict:
    r = _exiger(di, ("resultat",), "distillation-t06")
    b = _exiger(r, ("controle_negatif_donnees",), "distillation-t06.resultat")
    if b is None:
        raise CleAbsente("distillation-t06.resultat.controle_negatif_donnees est nul (plan DT-1 (a) : aucune génération, rien à lire)")
    bilan = {k: _exiger(b, (k,), "controle_negatif_donnees") for k in
             ("comparables", "passent", "courtes", "echecs", "fraction", "min_des_maxima", "lecture")}
    bilan["echecs"] = {"nombre": len(bilan["echecs"]), "dix_premiers": list(bilan["echecs"])[:10]}
    return {"present": True, "actions_controlees": int(bilan["comparables"]) + int(bilan["courtes"]),
            "actions_attendues_du_tirage": paires["distillation"]["retenues"] * CONDITIONS_DISTILLATION,
            "note": "aucun écart par action écrit par la chaîne : comparables + courtes tient lieu de nombre d'actions contrôlées",
            "controle_negatif_donnees": bilan, "duree_s": r.get("duree_s", ABSENT)}


def lire_arret(chemin: Path) -> dict:
    if not chemin.is_file():
        return {"present": False}
    r = _exiger(_lire_json(chemin, "arret"), ("resultat",), "arret")
    motif = str(_exiger(r, ("motif",), "arret.resultat"))
    lecture = "(i) inéquivalence réelle à la tolérance" if MOTIF_I in motif else (
        "(ii) contrôle négatif aveugle au décalage d'un jeton" if MOTIF_II in motif else "autre")
    return {"present": True, "etape": _exiger(r, ("etape",), "arret.resultat"), "motif": motif, "lecture": lecture,
            "duree_s": r.get("duree_s", ABSENT)}


def regler_e3_6(evaluation: dict | None, distillation: dict | None, arret: dict, cfg: dict) -> dict:
    motifs = []
    if arret["present"]:
        motifs.append(f"arrêt consigné ({arret['lecture']}) : {arret['motif'][:200]}")
    if distillation is None:
        motifs.append("distillation absente")
    if evaluation is None:
        motifs.append("épisodes absents")
    tol = float(_exiger(cfg, ("tolerance_equivalence",), "manifeste.config"))
    a_min = int(_exiger(cfg, ("actions_min_controle_negatif",), "manifeste.config"))
    f_min = float(_exiger(cfg, ("fraction_min_controle_negatif",), "manifeste.config"))
    if evaluation is not None:
        if evaluation["etats"] == 0:
            motifs.append("aucun état d'évaluation annoncé")
        for nom, p in evaluation["phases"].items():
            if p["fiches"] == 0:
                motifs.append(f"{nom} : aucune fiche")
                continue
            if p["actions_controlees"] == 0:
                motifs.append(f"{nom} : aucune action contrôlée (garde non exercée)")
            if p["couches_q99_au_dessus_tolerance"]:
                motifs.append(f"{nom} : écart q99 > {tol:g} aux couches {p['couches_q99_au_dessus_tolerance']}")
            if p["tolerances"] != [tol]:
                motifs.append(f"{nom} : tolérances {p['tolerances']} ≠ {tol:g} de la configuration")
            b = p["controle_negatif"]
            if b["lecture"] != "conforme":
                motifs.append(f"{nom} : contrôle négatif « {b['lecture']} » (comparables {b['comparables']}, fraction {b['fraction']})")
    if distillation is not None:
        b = distillation["controle_negatif_donnees"]
        if distillation["actions_controlees"] == 0:
            motifs.append("distillation : aucune action contrôlée")
        if b["lecture"] != "conforme":
            motifs.append(f"distillation : contrôle négatif « {b['lecture']} » (comparables {b['comparables']}, fraction {b['fraction']})")
    verdict = "réglé" if not motifs else "non réglé"
    return {"verdict": verdict, "motifs": motifs,
            "regle": (f"réglé ⇔ aucun arrêt ; distillation et épisodes présents ; chaque état annoncé a des fiches ; ≥ 1 action contrôlée par état "
                      f"et en distillation ; q99 max ≤ {tol:g} par couche ; contrôle négatif « conforme » partout (comparables ≥ {a_min}, "
                      f"fraction ≥ {f_min:g}) — ordre exploratoire v1 §§ 0, 2, 3, 4 A, 6, 9.1 ; aucune lecture de sonde"),
            "ligne": f"E3-6 {verdict}" + (" : " + " ; ".join(motifs) if motifs else " (garde d'équivalence exercée de fait, contrôles négatifs conformes)")}


def extraire(racine: Path, run_id: str | None = None) -> dict:
    racine = Path(racine)
    chemin_m = trouver_manifeste(racine, run_id)
    m = _lire_json(chemin_m, "manifeste")
    run = str(_exiger(m, ("run_id",), "manifeste"))
    cfg = _exiger(m, ("config",), "manifeste")
    sha_m = _sha256(chemin_m)
    diag = racine / "diag" / run
    paires = paires_independantes(m)
    arret = lire_arret(diag / "arret.json")
    rattachements = {}
    evaluation = distillation = None
    ep_chemin, di_chemin = diag / "episodes-t06.json", diag / "distillation-t06.json"
    if di_chemin.is_file():
        di = _lire_json(di_chemin, "distillation-t06")
        rattachements["distillation-t06"] = _exiger(di, ("manifeste_sha256",), "distillation-t06") == sha_m
        distillation = lire_distillation(di, paires)
    if ep_chemin.is_file():
        ep = _lire_json(ep_chemin, "episodes-t06")
        rattachements["episodes-t06"] = _exiger(ep, ("manifeste_sha256",), "episodes-t06") == sha_m
        evaluation = lire_evaluation(ep, paires, cfg)
        desc = ep["resultat"].get("descriptifs") if isinstance(ep["resultat"].get("descriptifs"), dict) else {}
        descriptifs = {k: desc.get(k, ABSENT) for k in ("memoire_pic_gio", "duree_s", "longueur_remplie_max", "generation_s", "passe_unique_s")}
        descriptifs["duree_episodes_fichier_s"] = ep["resultat"].get("duree_s", ABSENT)
    else:
        descriptifs = {k: ABSENT for k in ("memoire_pic_gio", "duree_s", "longueur_remplie_max", "generation_s", "passe_unique_s", "duree_episodes_fichier_s")}
    import numpy as np
    return {
        "statut": STATUT,
        "script": "scripts/extraire_garde_equivalence_t06_v1.py",
        "run_id": run,
        "manifeste": {"chemin": str(chemin_m), "sha256": sha_m, "sha256_compagnon": _compagnon(chemin_m), "commit": m.get("commit", ABSENT),
                      "numpy_du_manifeste": (m.get("versions") or {}).get("numpy", ABSENT), "numpy_ici": np.__version__,
                      "rattachement_des_resultats_au_manifeste": rattachements},
        "config": {k: cfg.get(k, ABSENT) for k in ("fraction_equivalence", "T", "N", "lot", "tolerance_equivalence", "statistique_equivalence",
                                                     "actions_min_controle_negatif", "positions_min_controle_negatif", "fraction_min_controle_negatif",
                                                     "go_id", "mode")},
        "paires_independantes": paires,
        "evaluation": evaluation if evaluation is not None else {"present": False},
        "distillation": distillation if distillation is not None else {"present": False},
        "arret": arret,
        "descriptifs": descriptifs,
        "e3_6": regler_e3_6(evaluation, distillation, arret, cfg),
    }


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("racine")
    p.add_argument("--run", default=None)
    p.add_argument("--sortie", default=None, help="dossier où écrire le JSON (nom marqué exploratoire, non opposable, R-522)")
    a = p.parse_args(argv)
    try:
        r = extraire(Path(a.racine), a.run)
    except CleAbsente as e:
        print(f"ARRÊT : {e.message}", file=sys.stderr)
        return 2
    texte = json.dumps(r, ensure_ascii=False, indent=1, sort_keys=True) + "\n"
    if a.sortie:
        d = Path(a.sortie)
        d.mkdir(parents=True, exist_ok=True)
        f = d / f"garde-equivalence-{r['run_id']}-exploratoire-non-opposable-r522.json"
        if f.exists():
            print(f"ARRÊT : {f} existe déjà (R12)", file=sys.stderr)
            return 2
        f.write_text(texte, encoding="utf-8")
    sys.stdout.write(texte)
    print(r["e3_6"]["ligne"], file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
