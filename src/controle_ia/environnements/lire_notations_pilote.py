"""Lecture des notations décisives refaites du pilote de T0.5 (N-021, option (a), GO-2026-10-12-02).

Écart de procédure déclaré au préenregistrement du pilote : le code de lecture gelé (`lire_pilote`, commit cité par le
pilote) ne lit les notations que dans le dossier du pilote, par un seul run d'analyse. Les notations refaites
(`noter_pilote_a`) vivent dans un run distinct. Ce module mince les lit **sans rien calculer lui-même** : toutes les
mesures, intervalles, prédictions, déclencheurs et tirages viennent du code gelé de `lire_pilote` (fonctions
`_ouvrir_analyse`, `charger_pilote`, `mesures_format`, `empreintes_des_ensembles`, `notes_alignees`, `lecture_juge`,
`decomposition_complete`, `difference_appariee`, `predictions`, `declencheurs_audit`, `tirer_relectures`,
`_serialisable`, `_familles_vides` ; constantes `TIRAGES` et `NIVEAU`), appelé avec les graines du manifeste de la
première analyse ; chaque graine passe par `generateur`, qui construit un générateur neuf par clé, et `predictions` et
`declencheurs_audit` ne tirent rien : l'ordre des appels, qui diffère de celui d'`analyser` pour `tirer_relectures`, est
sans effet sur les nombres. Le module n'ajoute que des gardes, le chargement du run des notations et l'écriture sous
manifeste. Son équivalence avec `analyser` est éprouvée par des tests sur un même pilote (notations écrites dans le
dossier du pilote et lues par `analyser`, ou dans un run distinct et lues ici) : mêmes juges, même différence appariée,
mêmes P1 à P7, mêmes réponses et actions tirées pour l'audit, mêmes déclencheurs hors familles (sans déclencheur, puis
avec un déclencheur propre aux juges, lecture suspendue des deux côtés).

Gardes : celles d'`_ouvrir_analyse` (préenregistrement du pilote intact, modules de lecture égaux au commit cité,
constantes et version de numpy du manifeste d'analyse) ; run des notations rattaché au même pilote ; lecture décisive
(préenregistrement passé) : run des notations décisif, en mode réel, lancé sous ce même préenregistrement, scellé et
intact (contre-lecture R2) ; issue du run des notations consignée par un seul `resume.json` ou un seul `arret.json`,
scellé et rattaché, dont les statuts des juges s'accordent avec les fichiers présents (un fichier pour chaque juge
« écrit », aucun pour les autres) : un run sans l'un ni l'autre n'est pas lu (nœud, comme au pilote) ; modules de ce
module et du lanceur des notations égaux au commit du run des notations ; aucune notation dans le dossier du pilote ;
format recalculé égal à la première lecture ; P1 et P4 à P7 recalculés avec les grandeurs scellées de la première
lecture, égaux à elles. Sortie : `diag/<run de lecture>/lecture-juges.json`, sous son propre manifeste.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from ..gardes import GardeArret
from ..manifeste import creer_manifeste, ecrire_resultat, generateur, graines, lire_manifeste, verifier_resultat
from ..prereg import exiger_prereg_scelle
from ..scellement import empreinte
from .lire_pilote import (NIVEAU, TIRAGES, _familles_vides, _ouvrir_analyse, _serialisable, charger_pilote,
                          declencheurs_audit, decomposition_complete, difference_appariee, empreintes_des_ensembles,
                          lecture_juge, mesures_format, notes_alignees, predictions, tirer_relectures)

COMMANDE = "python -m controle_ia.environnements.lire_notations_pilote"
MODULES_NOTATIONS = ("src/controle_ia/environnements/noter_pilote_a.py",
                     "src/controle_ia/environnements/lire_notations_pilote.py")
PREDICTIONS_DE_LA_PREMIERE_LECTURE = ("P1", "P4", "P5", "P6", "P7")


def exiger_modules_notations(racine: Path, commit: str) -> None:
    """Le lanceur et ce lecteur sont ceux du commit du run des notations (modifications non commitées comprises)."""
    absents = [x for x in MODULES_NOTATIONS if not (Path(racine) / x).is_file()]
    if absents:
        raise GardeArret(f"modules des notations absents du dépôt : {absents}")
    r = subprocess.run(["git", "-C", str(racine), "diff", "--quiet", commit, "--", *MODULES_NOTATIONS],
                       capture_output=True, text=True)
    if r.returncode == 1:
        raise GardeArret(f"modules des notations modifiés depuis le commit du run des notations {commit[:12]}")
    if r.returncode != 0:
        raise GardeArret(f"comparaison au commit {commit[:12]} impossible : {r.stderr.strip()}")


def exiger_run_sous_prereg(racine: Path, m: dict, prereg: str | Path) -> None:
    """Lecture décisive : le run des notations est décisif, en mode réel, et lancé sous ce préenregistrement, scellé
    et intact (même chemin, même empreinte que ceux de son manifeste)."""
    chemin = Path(prereg)
    if chemin.is_absolute():
        try:
            chemin = chemin.resolve().relative_to(Path(racine).resolve())
        except ValueError:
            raise GardeArret(f"préenregistrement {prereg} hors du dépôt") from None
    sha = exiger_prereg_scelle(Path(racine) / chemin)
    pr = m.get("preenregistrement") or {}
    if m.get("decisif") is not True:
        raise GardeArret("run des notations non décisif : il ne se lit pas sous un préenregistrement (R1)")
    if m["config"].get("mode") != "reel":
        raise GardeArret(f"run des notations hors mode réel ({m['config'].get('mode')!r})")
    if pr.get("chemin") != chemin.as_posix() or pr.get("sha256") != sha:
        raise GardeArret(f"run des notations lancé sous un autre préenregistrement ({pr.get('chemin')}, "
                         f"{str(pr.get('sha256'))[:12]}…) que {chemin.as_posix()} ({sha[:12]}…)")


def issue_des_notations(racine: Path, run_notations: str, juges: list[str]) -> dict:
    """Issue consignée du run des notations : un seul fichier, `resume.json` ou `arret.json`, scellé et rattaché ;
    statut de chaque juge (« écrit » ou non). Un run sans l'un ni l'autre n'est pas lu (ligne gelée du pilote)."""
    d = Path(racine) / "diag" / run_notations
    presents = [n for n in ("resume", "arret") if (d / f"{n}.json").exists()]
    if len(presents) != 1:
        raise GardeArret(f"run des notations {run_notations} : {presents or 'ni resume.json ni arret.json'} ; "
                         f"un seul attendu : run non lisible (nœud)")
    c = verifier_resultat(racine, d / f"{presents[0]}.json")
    if c["run_id"] != run_notations:
        raise GardeArret(f"{presents[0]}.json rattaché au run {c['run_id']}, non à {run_notations}")
    corps = c["resultat"] if presents[0] == "resume" else c["resultat"].get("partiel", {})
    statuts = {j: (corps.get("juges") or {}).get(j, {}).get("statut") for j in juges}
    return {"fichier": presents[0], "statuts": statuts}


def charger_notations(racine: Path, run_notations: str, run_pilote: str, juges: list[str],
                      prereg: str | Path | None = None) -> tuple[dict, str, dict, dict]:
    """Manifeste du run des notations, rattaché au pilote (et, pour une lecture décisive, lancé sous le
    préenregistrement) ; issue consignée ; notations décisives de chaque juge (None si son fichier n'est pas écrit :
    juge échu ou arrêt), en accord avec les statuts de l'issue."""
    chemin_m = Path(racine) / "runs" / run_notations / "manifeste.json"
    if not chemin_m.exists():
        raise GardeArret(f"manifeste du run des notations absent : {chemin_m}")
    m, sha_m = lire_manifeste(chemin_m)
    if m["config"].get("run_pilote") != run_pilote:
        raise GardeArret(f"run des notations rattaché au pilote {m['config'].get('run_pilote')!r}, non à {run_pilote}")
    if prereg is not None:
        exiger_run_sous_prereg(racine, m, prereg)
    issue = issue_des_notations(racine, run_notations, juges)
    notations = {}
    for j in juges:
        f = Path(racine) / "diag" / run_notations / f"notations-{j}-decisives.json"
        if not f.exists():
            notations[j] = None
            continue
        c = verifier_resultat(racine, f)
        if c["run_id"] != run_notations:
            raise GardeArret(f"{f.name} rattaché au run {c['run_id']}, non à {run_notations}")
        notations[j] = c["resultat"]["notations"]
    desaccords = [j for j in juges if (notations[j] is not None) != (issue["statuts"][j] == "écrit")]
    if desaccords:
        raise GardeArret(f"fichiers de notations et statuts de {issue['fichier']}.json en désaccord pour {desaccords}")
    return m, sha_m, notations, issue


def lire_notations(racine: Path, run_pilote: str, run_notations: str, run_analyse: str, chemin_taches: str | Path,
                   run_lecture: str, prereg: str | None = None, autoriser_depot_sale: bool = False) -> dict:
    racine = Path(racine)
    # gardes gelées de la première analyse (préenregistrement du pilote, modules, constantes, numpy, état de l'arbre)
    chemin_a, m_a, etat = _ouvrir_analyse(racine, run_analyse)
    if m_a["config"]["run_pilote"] != run_pilote:
        raise GardeArret(f"run du pilote {run_pilote} ≠ run du manifeste d'analyse {m_a['config']['run_pilote']}")
    p = charger_pilote(racine, run_pilote, chemin_taches)
    if p["manifeste_sha256"] != m_a["config"]["manifeste_pilote_sha256"]:
        raise GardeArret("manifeste du pilote différent de celui de l'analyse")
    if any(v is not None for (j, etape), v in p["notations"].items() if etape == "decisives"):
        raise GardeArret("le dossier du pilote porte des notations décisives : lecture par `analyser`, pas ici")
    m_n, sha_n, notations, issue = charger_notations(racine, run_notations, run_pilote, p["juges"], prereg)
    exiger_modules_notations(racine, m_n["commit"])
    chemin_l1 = racine / "diag" / run_analyse / "lecture.json"
    l1 = verifier_resultat(racine, chemin_l1)["resultat"]
    if l1.get("run_pilote") != run_pilote:
        raise GardeArret("première lecture d'un autre pilote")
    g = m_a["graines"]
    fiches, taches_ids = p["episodes"]["fiches"], sorted(p["taches"])
    fmt = mesures_format(fiches, p["config"]["max_nouveaux"])
    if _serialisable(fmt) != l1["format"]:
        raise GardeArret("format recalculé ≠ format de la première lecture")
    ensembles = empreintes_des_ensembles(fiches)
    # juges et différence appariée : mêmes fonctions, mêmes graines, même ordre qu'`analyser`
    juges, alignes = {}, {}
    for j in p["juges"]:
        if notations[j] is None:
            juges[j] = {"lecture": "notations décisives refaites absentes (juge échu ou arrêt) : nœud",
                        "plan_b": "nœud"}
            continue
        alignes[j] = notes_alignees(notations[j], j, taches_ids, ensembles)
        juges[j] = lecture_juge(alignes[j], generateur(g[f"analyse/bootstrap-parts-{j}"]))
        sensib = notes_alignees(notations[j], j, taches_ids, ensembles, mesure=lambda n: n["score"])
        try:
            juges[j]["sensibilite_sur_100"] = decomposition_complete(sensib["sA"], sensib["sB"], sensib["sC"])[
                "parts_tronquees"]
        except GardeArret as e:
            juges[j]["sensibilite_sur_100"] = f"impossible : {e}"
    diff = None
    if len(alignes) == 2:
        a8, a3 = (alignes[j] for j in p["juges"])
        try:
            diff = difference_appariee((a8["sA"], a8["sB"], a8["sC"]), (a3["sA"], a3["sB"], a3["sC"]), TIRAGES,
                                       generateur(g["analyse/bootstrap-difference"]), NIVEAU)
        except GardeArret as e:
            diff = {"impossible": str(e), "borne": None}
    # prédictions : P2 et P3 nouvelles ; les autres, recalculées sur les grandeurs scellées de la première lecture,
    # doivent lui être égales
    fam = l1["familles"] if isinstance(l1.get("familles"), dict) else _familles_vides()
    cout = l1.get("cout") or {"mediane_log10": None}
    preds = predictions(fmt, juges, diff, fam, cout, l1.get("kappas"), l1.get("difference_kappas"))
    ecarts = [k for k in PREDICTIONS_DE_LA_PREMIERE_LECTURE if preds[k] != l1["predictions"][k]]
    if ecarts:
        raise GardeArret(f"prédictions {ecarts} recalculées ≠ celles de la première lecture")
    p_oui = [a["p_oui"] for a in p["appariements"]["appariements"]] if p["appariements"] else []
    audit = declencheurs_audit(fmt, juges, fam if isinstance(l1.get("familles"), dict) else {}, l1.get("kappas"),
                               p_oui)
    p_notes = {**p, "notations": {(j, "decisives"): notations[j] for j in p["juges"]}}
    lecture = {"run_pilote": run_pilote, "run_notations": run_notations, "run_analyse": run_analyse,
               "issue_des_notations": issue,
               "commit_lecture_cite": m_a["config"]["commit_lecture_cite"], "commit_notations": m_n["commit"], **etat,
               "juges": juges, "difference_appariee": diff,
               "predictions": {"P2": preds["P2"], "P3": preds["P3"],
                               **{k: preds[k] for k in PREDICTIONS_DE_LA_PREMIERE_LECTURE}},
               "audit_r4_juges": audit, "lecture_suspendue": audit["declenche"],
               "relectures_audit": tirer_relectures(p_notes, generateur(g["analyse/audit"]))}
    config = {"run_pilote": run_pilote, "run_notations": run_notations, "manifeste_notations_sha256": sha_n,
              "run_analyse": run_analyse, "manifeste_analyse_sha256": empreinte(chemin_a),
              "premiere_lecture_sha256": empreinte(chemin_l1), "commit_lecture_cite": lecture["commit_lecture_cite"]}
    # graines tirées par cette lecture, consignées dans son propre manifeste (R9) : mêmes clés et même entropie que
    # le manifeste de la première analyse, d'où elles sont prises ; égalité exigée avant toute écriture
    cles = [f"analyse/bootstrap-parts-{j}" for j in p["juges"]] + ["analyse/bootstrap-difference", "analyse/audit"]
    entropies = {g[k]["entropie"] for k in cles}
    if len(entropies) != 1:
        raise GardeArret(f"graines de la première analyse d'entropies différentes : {sorted(entropies)}")
    entropie = int(entropies.pop())
    neuves = graines(cles, entropie)
    if any(neuves[k] != g[k] for k in cles):
        raise GardeArret("graines de la lecture ≠ celles du manifeste de la première analyse")
    chemin_m, _ = creer_manifeste(racine, run_lecture, config, cles, entropie=entropie, decisif=prereg is not None,
                                  prereg=prereg, autoriser_depot_sale=autoriser_depot_sale, commande=COMMANDE)
    ecrire_resultat(racine, chemin_m, "lecture-juges", _serialisable(lecture))
    return lecture


def _main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog=COMMANDE)
    for k in ("--run-pilote", "--run-notations", "--run-analyse", "--taches", "--run-lecture", "--prereg"):
        ap.add_argument(k, required=True)
    x = ap.parse_args(argv)
    lecture = lire_notations(Path("."), x.run_pilote, x.run_notations, x.run_analyse, x.taches, x.run_lecture,
                             x.prereg)
    print(json.dumps(_serialisable({k: lecture[k] for k in ("predictions", "audit_r4_juges", "lecture_suspendue")}),
                     ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
