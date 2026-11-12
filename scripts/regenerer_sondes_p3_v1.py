"""Régénération du fichier complet des sondes figées de P3 (devis `docs/notes/regeneration-sondes-p3-v1/
devis-regeneration-sondes-p3-v1.md`, GO-2026-10-28-11), v1.

Rejoue les étapes 1 à 5 de P3 (contrôle du format, données génériques, extraction, entraînement des sondes et des
planchers, sondes figées) par **le lanceur de P3 lui-même** (`controle_ia.premier_test_ia.run.executer`), importé depuis
un arbre extrait au commit de P3, sans en changer une ligne ; s'arrête volontairement à la ligne de progression
`etape=sondes-figees` (aucun épisode, aucun juge), puis applique mécaniquement le critère d'acceptation du devis (§ 3) :

1. sceau du fichier complet régénéré = sceau attendu (`91b61c45…`) → `accepte-identique` ;
2. sinon : chaque sonde du fichier léger de P3 retrouvée dans le fichier léger régénéré (mêmes noms, classes, couches,
   tableaux), chaque tableau et chaque biais à une différence absolue maximale ≤ tolérance (1e-6), et les aires de
   validation de chaque sonde égales à celles de P3 à la tolérance près → `accepte-avec-declaration` (les matrices de
   Mahalanobis sont régénérées, non prouvées identiques au fichier perdu) ;
3. sinon → `refuse`.

Ce script vit hors de l'arbre de P3 (il est copié hors du clone sur l'instance) : l'arbre du run reste propre et égal au
commit cité par le préenregistrement (garde `exiger_code_cite`). Codes : 0 verdict écrit (quel qu'il soit) ; 1 arrêt
(garde, panne, run qui ne s'arrête pas où prévu) ; 2 usage.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import signal
import subprocess
import sys
from pathlib import Path

ETAPE_ARRET = "sondes-figees"
SCEAU_P3 = "91b61c45cdafd0ab979e261171b9661920715fa42c6cbc9751cd2697bfd3177a"


class ArretApresSondes(Exception):
    """Arrêt volontaire après l'écriture des sondes figées : la régénération ne joue aucun épisode."""


def importer_p3(racine: Path):
    """Importe le lanceur de P3 depuis `racine/src`, et nulle part ailleurs."""
    src = str((racine / "src").resolve())
    if "controle_ia" in sys.modules:
        mod = sys.modules["controle_ia"]
        if src not in [str(Path(p).resolve()) for p in getattr(mod, "__path__", [])] and \
                not str(Path(mod.__file__).resolve()).startswith(src):
            raise SystemExit(f"controle_ia déjà importé hors de {src}")
    else:
        sys.path.insert(0, src)
    from controle_ia.premier_test_ia import run as rp
    if not str(Path(rp.__file__).resolve()).startswith(src):
        raise SystemExit(f"lanceur de P3 importé hors de {src} : {rp.__file__}")
    return rp


def regler_openblas(fils: int) -> dict:
    """Fixe le nombre de fils de la bibliothèque d'algèbre linéaire de numpy (OpenBLAS livrée avec numpy), le relit et
    rend sa configuration. P3 tournait sans borne d'affinité (128 cœurs) : OpenBLAS y prenait son plafond compilé (64,
    inféré, non consigné par P3). `taskset` borne l'affinité à 30 cœurs pour torch ; OpenBLAS est remis à 64 par appel
    explicite (la variable d'environnement reste plafonnée par l'affinité). Arrêt si la bibliothèque est introuvable ou
    si le nombre relu diffère (aucun repli silencieux, R5)."""
    import ctypes
    import glob
    import os

    import numpy

    libs = sorted(glob.glob(os.path.join(os.path.dirname(numpy.__file__), os.pardir, "numpy.libs", "*openblas*")))
    if len(libs) != 1:
        raise SystemExit(f"bibliothèque OpenBLAS de numpy introuvable ou ambiguë : {libs}")
    lib = ctypes.CDLL(libs[0])
    lib.scipy_openblas_get_config64_.restype = ctypes.c_char_p
    avant = int(lib.scipy_openblas_get_num_threads64_())
    lib.scipy_openblas_set_num_threads64_(int(fils))
    apres = int(lib.scipy_openblas_get_num_threads64_())
    config = lib.scipy_openblas_get_config64_().decode("utf-8", "replace")
    if apres != int(fils):
        raise SystemExit(f"OpenBLAS : {apres} fils relus, {fils} demandés ({config})")
    return {"bibliotheque": os.path.basename(libs[0]), "config": config, "fils_avant": avant, "fils": apres,
            "numpy": numpy.__version__}


def arreter_apres_sondes(rp) -> dict:
    """Remplace `progres` du lanceur par une enveloppe qui relaie la ligne, puis lève `ArretApresSondes` juste après
    `etape=sondes-figees`. Rend un état où l'enveloppe note ce qu'elle a vu."""
    vu = {"etapes": [], "arret": False}
    vraie = rp.progres

    def progres(**champs):
        vraie(**champs)
        vu["etapes"].append(champs.get("etape"))
        if champs.get("etape") == ETAPE_ARRET:
            vu["arret"] = True
            vu["champs"] = {k: str(v) for k, v in champs.items()}
            raise ArretApresSondes("arrêt volontaire après les sondes figées (régénération, devis v1 ; aucun épisode)")

    rp.progres = progres
    return vu


def sha256_fichier(chemin: Path) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def _sondes_par_nom(chemin: Path) -> tuple[dict, dict]:
    """{nom: entrée de l'index} et {nom: {tableau: ndarray}}, lus sans pickle."""
    import numpy as np

    with np.load(chemin, allow_pickle=False) as z:
        index = json.loads(bytes(z["index"]).decode("utf-8"))
        entrees, tableaux = {}, {}
        for k, e in enumerate(index["sondes"]):
            entrees[e["nom"]] = e
            tableaux[e["nom"]] = {t: np.array(z[f"s{k}_{t}"]) for t in e["tableaux"]}
    return entrees, tableaux


def comparer_legeres(reference: Path, regenere: Path, tolerance: float) -> dict:
    """Compare deux fichiers légers sonde par sonde (par nom, jamais par position)."""
    import numpy as np

    e_ref, t_ref = _sondes_par_nom(reference)
    e_reg, t_reg = _sondes_par_nom(regenere)
    ecarts, problemes, empreintes_egales = {}, [], 0
    manquantes = sorted(set(e_ref) - set(e_reg))
    en_trop = sorted(set(e_reg) - set(e_ref))
    if manquantes:
        problemes.append(f"sondes absentes du fichier régénéré : {manquantes[:10]}")
    if en_trop:
        problemes.append(f"sondes en trop dans le fichier régénéré : {en_trop[:10]}")
    for nom in sorted(set(e_ref) & set(e_reg)):
        a, b = e_ref[nom], e_reg[nom]
        for cle in ("classe", "couche", "agregation", "famille", "tableaux"):
            if a.get(cle) != b.get(cle):
                problemes.append(f"{nom} : {cle} {a.get(cle)!r} ≠ {b.get(cle)!r}")
        empreintes_egales += a.get("empreinte") == b.get("empreinte")
        ecart = 0.0
        if (a.get("b") is None) != (b.get("b") is None):
            problemes.append(f"{nom} : biais présent d'un seul côté")
        elif a.get("b") is not None:
            if not (math.isfinite(float(a["b"])) and math.isfinite(float(b["b"]))):
                problemes.append(f"{nom} : biais non fini")
                ecart = math.inf
            else:
                ecart = abs(float(a["b"]) - float(b["b"]))
        for t in a.get("tableaux", []):
            x, y = t_ref[nom].get(t), t_reg[nom].get(t)
            if y is None or x.shape != y.shape:
                problemes.append(f"{nom}/{t} : forme {None if x is None else x.shape} ≠ {None if y is None else y.shape}")
                ecart = math.inf
                continue
            if not (np.all(np.isfinite(x)) and np.all(np.isfinite(y))):
                problemes.append(f"{nom}/{t} : valeur non finie")
                ecart = math.inf
                continue
            ecart = max(ecart, float(np.max(np.abs(x - y))) if x.size else 0.0)
        ecarts[nom] = ecart
    pire = max(ecarts.values()) if ecarts else math.inf
    if not ecarts:
        problemes.append("aucune sonde comparée")
    if pire > tolerance:
        problemes.append(f"écart maximal {pire:.3e} > tolérance {tolerance:.0e}")
    return {"sondes_reference": len(e_ref), "sondes_regenerees": len(e_reg), "sondes_comparees": len(ecarts),
            "empreintes_egales": empreintes_egales, "ecart_max": pire if math.isfinite(pire) else "infini",
            "pires": sorted(ecarts.items(), key=lambda kv: -kv[1])[:5], "problemes": problemes, "conforme": not problemes}


def comparer_aires(reference: dict, regenere: dict, tolerance: float) -> dict:
    """Aires de validation `{concept: {sonde: aire}}` de P3 contre celles de la régénération."""
    problemes, pire = [], 0.0
    if set(reference) != set(regenere):
        problemes.append(f"concepts {sorted(reference)} ≠ {sorted(regenere)}")
    for c in sorted(set(reference) & set(regenere)):
        a, b = reference[c], regenere[c]
        if set(a) != set(b):
            problemes.append(f"{c} : sondes {sorted(set(a) ^ set(b))[:10]} d'un seul côté")
        for n in sorted(set(a) & set(b)):
            x, y = a[n], b[n]
            if x is None or y is None or not (math.isfinite(x) and math.isfinite(y)):
                if x != y:
                    problemes.append(f"{c}/{n} : aire {x!r} ≠ {y!r}")
                continue
            pire = max(pire, abs(float(x) - float(y)))
    if pire > tolerance:
        problemes.append(f"écart d'aire maximal {pire:.3e} > tolérance {tolerance:.0e}")
    return {"ecart_max": pire, "problemes": problemes, "conforme": not problemes}


CLES_ETAPES_1_A_5 = ("tirage-enjeux", "decoupage-tromperie", "decoupage-enjeux")


def comparer_graines(reference: dict, regenere: dict) -> dict:
    """Graines des étapes 1 à 5 (tirage, découpages, sondes, planchers) : toutes présentes des deux côtés et égales."""
    cles = [k for k in reference if k in CLES_ETAPES_1_A_5 or k.startswith(("sonde/", "plancher/"))]
    problemes = [f"graine {k} absente de la régénération" for k in cles if k not in regenere]
    problemes += [f"graine {k} différente" for k in cles if k in regenere and regenere[k] != reference[k]]
    if not any(k.startswith("sonde/") for k in cles):
        problemes.append("aucune graine de sonde dans la référence")
    return {"cles_comparees": len(cles), "problemes": problemes, "conforme": not problemes}


def verdict(sceau_regenere: str, sceau_attendu: str, legeres: dict | None, aires: dict | None,
            graines: dict | None = None) -> str:
    if graines is not None and not graines["conforme"]:
        return "refuse"
    if sceau_regenere == sceau_attendu:
        return "accepte-identique"
    if legeres is not None and aires is not None and legeres["conforme"] and aires["conforme"]:
        return "accepte-avec-declaration"
    return "refuse"


def etat_git(racine: Path) -> dict:
    def g(*a):
        r = subprocess.run(["git", "-C", str(racine), *a], capture_output=True, text=True)
        return r.stdout.strip() if r.returncode == 0 else None
    return {"commit": g("rev-parse", "HEAD"), "propre": g("status", "--porcelain") == ""}


def _main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog="regenerer_sondes_p3_v1")
    ap.add_argument("--racine", required=True, help="arbre extrait au commit de P3")
    ap.add_argument("--commit-attendu", default=None, help="commit de P3 (obligatoire en mode réel)")
    ap.add_argument("--config", required=True)
    ap.add_argument("--taches", required=True)
    ap.add_argument("--prereg", default=None)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--reference-legeres", required=True, help="fichier léger des sondes figées de P3")
    ap.add_argument("--reference-diag", required=True, help="résultat `sondes-figees.json` de P3")
    ap.add_argument("--reference-manifeste", default=None, help="manifeste du run de P3 (graines ; obligatoire en mode réel)")
    ap.add_argument("--fils-blas", type=int, default=64, help="fils d'OpenBLAS (P3 : 64, inféré)")
    ap.add_argument("--sceau-attendu", default=SCEAU_P3)
    ap.add_argument("--sortie", required=True, help="verdict JSON (refus s'il existe, R12)")
    ap.add_argument("--autoriser-depot-sale", action="store_true", help="essais en mode jouet seulement")
    a = ap.parse_args(argv)
    racine, sortie = Path(a.racine).resolve(), Path(a.sortie)
    if sortie.exists():
        print(f"{sortie} existe déjà (R12)", file=sys.stderr)
        return 2
    git = etat_git(racine)
    config = json.loads(Path(a.config).read_text(encoding="utf-8"))
    if config.get("mode") == "reel":
        if a.autoriser_depot_sale or a.prereg is None or a.commit_attendu is None or a.reference_manifeste is None:
            print("mode réel : préenregistrement et commit attendu obligatoires, arbre propre exigé", file=sys.stderr)
            return 2
        if Path.cwd().resolve() != racine:
            print("mode réel : lancer depuis la racine de l'arbre de P3 (chemins des données relatifs)", file=sys.stderr)
            return 2
        if git["commit"] != a.commit_attendu or not git["propre"]:
            print(f"arbre {git} ≠ commit attendu {a.commit_attendu} ou non propre", file=sys.stderr)
            return 1
    # les sceaux des références sont vérifiés avant tout calcul (fichier léger de P3 et son résultat)
    for f in [a.reference_legeres, a.reference_diag] + ([a.reference_manifeste] if a.reference_manifeste else []):
        attendu = Path(f + ".sha256").read_text(encoding="utf-8").split()[0]
        if sha256_fichier(Path(f)) != attendu:
            print(f"sceau de la référence {f} non conforme", file=sys.stderr)
            return 1
    ref_diag = json.loads(Path(a.reference_diag).read_text(encoding="utf-8"))["resultat"]
    if ref_diag["sondes_figees_sha256"] != a.sceau_attendu:
        print("la référence ne porte pas le sceau attendu", file=sys.stderr)
        return 1

    rp = importer_p3(racine)
    blas = regler_openblas(a.fils_blas)
    fils_torch = rp.fils_effectifs(config["fils_entrainement"], rp.coeurs_disponibles())
    if config.get("mode") == "reel" and fils_torch != ref_diag.get("fils_entrainement_effectifs"):
        print(f"fils effectifs de l'entraînement {fils_torch} ≠ ceux de P3 {ref_diag.get('fils_entrainement_effectifs')} : "
              "arrêt avant tout calcul", file=sys.stderr)
        return 1
    vu = arreter_apres_sondes(rp)
    signal.signal(signal.SIGTERM, rp._signal_term)
    try:
        rp.executer(config, racine, a.run_id, a.prereg, a.taches, autoriser_depot_sale=a.autoriser_depot_sale)
    except ArretApresSondes:
        pass
    except BaseException as e:      # garde ou panne du lanceur : déjà consignée par lui (arret.json), propagée en code 1
        print(f"ARRÊT avant les sondes figées : {type(e).__name__}: {e}", file=sys.stderr)
        return 1
    else:
        print("le lanceur est allé au bout sans passer par les sondes figées : refus", file=sys.stderr)
        return 1
    if not vu["arret"]:
        print("arrêt sans ligne sondes-figees : refus", file=sys.stderr)
        return 1

    diag = json.loads((racine / "diag" / a.run_id / "sondes-figees.json").read_text(encoding="utf-8"))["resultat"]
    dossier = racine / "donnees" / a.run_id
    sceau = sha256_fichier(dossier / "sondes-figees.npz")
    if sceau != diag["sondes_figees_sha256"]:
        print("fichier complet régénéré ≠ son sceau consigné", file=sys.stderr)
        return 1
    tol = float(config.get("tolerance_identite", 1e-6))
    legeres = comparer_legeres(Path(a.reference_legeres), dossier / "sondes-figees-legeres.npz", tol)
    aires = comparer_aires(ref_diag["aires_validation"], diag["aires_validation"], tol)
    graines = None
    if a.reference_manifeste:
        m_ref = json.loads(Path(a.reference_manifeste).read_text(encoding="utf-8"))["graines"]
        m_reg = json.loads((racine / "runs" / a.run_id / "manifeste.json").read_text(encoding="utf-8"))["graines"]
        graines = comparer_graines(m_ref, m_reg)
    v = verdict(sceau, a.sceau_attendu, legeres, aires, graines)
    rapport = {
        "verdict": v, "sceau_attendu": a.sceau_attendu, "sceau_regenere": sceau,
        "sceau_legeres_regenere": diag["sondes_legeres_sha256"], "run_id": a.run_id, "git": git,
        "fils_entrainement_effectifs": {"p3": ref_diag.get("fils_entrainement_effectifs"),
                                        "regeneration": diag.get("fils_entrainement_effectifs")},
        "coeurs": {"p3": ref_diag.get("coeurs"), "regeneration": diag.get("coeurs")},
        "comparaison_legeres": legeres, "comparaison_aires": aires, "comparaison_graines": graines, "tolerance": tol,
        "conditions": {"openblas": blas, "fils_torch_avant_calcul": fils_torch,
                       "fils_openblas_p3": "64, inféré (affinité 128, plafond compilé 64), non consigné par P3"},
        "etapes_vues": vu["etapes"],
        "lecture": {"accepte-identique": "le fichier de P3, au bit près",
                    "accepte-avec-declaration": "matrices de Mahalanobis régénérées, non prouvées identiques au fichier "
                                                "perdu ; toute lecture le déclare",
                    "refuse": "rien n'est utilisé ; nœud pour Lazar"}[v]}
    sortie.write_text(json.dumps(rapport, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    Path(str(sortie) + ".sha256").write_text(f"{sha256_fichier(sortie)}  {sortie.name}\n", encoding="utf-8")
    print(f"VERDICT {v} sceau={sceau}")
    return 0


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
