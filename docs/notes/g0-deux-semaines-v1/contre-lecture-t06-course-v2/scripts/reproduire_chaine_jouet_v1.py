"""Reproduit, sur le monde jouet (processeur, sans réseau, sans dépense, aucune donnée réelle), la FORME des sorties d'un run de
la chaîne v12 (`controle_ia.t06.lanceur_v5`, appelé par l'amorce v10) et y applique l'extracteur d'épreuve v1
(`scripts/extraire_mesures_epreuve_t06_v1.py`), pour les deux constats neufs de la contre-lecture :
  1. `equivalence_99e_centile` : l'extracteur lit `etats[<état>]["equivalence"]`, que la chaîne n'écrit jamais ; le bloc
     d'équivalence existe, mais par fiche d'épisode (`fiches[k]["equivalence"]`) ;
  2. `pas_par_adaptateur` : l'extracteur compte les entrées du journal de distillation (une par époque, plus l'époque 0), et
     non les pas d'AdamW ; le nombre de pas effectifs est écrit ailleurs (`donnees.<adaptateur>.pas_declares.pas`).

Usage (Python 3.11 du programme) :
    python3.11 -I -B reproduire_chaine_jouet_v1.py ARBRE DOSSIER_JETABLE
ARBRE : arbre détaché du commit 7822a65b (chaîne v12) ; DOSSIER_JETABLE : dossier neuf (dépôt git jouet créé dedans).
"""
from __future__ import annotations

import importlib.util
import json
import os
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path

ARBRE, JET = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
sys.path[:0] = [str(ARBRE / "src"), str(ARBRE / "tests")]

from controle_ia.manifeste import verifier_resultat  # noqa: E402
from controle_ia.scellement import sceller  # noqa: E402
from controle_ia.t06 import lanceur_v5 as la5  # noqa: E402

ENONCES = ["Which routing rule makes sparse mixtures of experts train stably?",
           "Does curriculum ordering change sample efficiency of small language models?",
           "Can retrieval reduce hallucination in long-form question answering?",
           "How does tokenizer vocabulary size affect multilingual transfer?"]


def git(*a):
    subprocess.run(["git", "-C", str(depot), *a], check=True, capture_output=True)


depot = JET / "depot-jouet"
depot.mkdir(parents=True, exist_ok=False)
git("init", "-q", "-b", "main")
git("config", "user.email", "test@example.invalid")
git("config", "user.name", "test")
(depot / "README").write_text("x\n")
(depot / "prereg").mkdir()
for nom in ("P3-consignes-v1.md", "P3-consignes-v1.md.sha256"):
    shutil.copy(ARBRE / "prereg" / nom, depot / "prereg" / nom)
d = depot / "donnees" / "t06-jouet"
d.mkdir(parents=True)


def taches(ids):
    return {"taches": [{"identifiant": i, "questions": ENONCES[k % len(ENONCES)] + f" ({i})"} for k, i in enumerate(ids)]}


(d / "taches-evaluation.json").write_text(json.dumps(taches(["e1", "e2", "e3", "e4"]), ensure_ascii=False), encoding="utf-8")
(d / "taches-distillation.json").write_text(json.dumps(taches(["d1", "d2"]), ensure_ascii=False), encoding="utf-8")
config = json.loads((ARBRE / "docs/notes/g0-deux-semaines-v1/config-t06-jouet-v5.json").read_text(encoding="utf-8"))
config["taches_evaluation"]["sha256"] = sceller(d / "taches-evaluation.json")
config["taches_distillation"]["sha256"] = sceller(d / "taches-distillation.json")
config["distillation"]["epoques"] = 3                     # comme à E3 bis et à la course : trois époques
config["distillation"]["lot"] = 1                         # lot 1 : un pas par transcription
config["distillation"]["pas_declares"] = 3 * 2 * config["episodes_par_tache_distillation"]
(depot / "config-jouet.json").write_text(json.dumps(config, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
sceller(depot / "config-jouet.json")
for x in ("runs", "diag"):
    (depot / x).mkdir()
git("add", "-A")
git("commit", "-q", "-m", "jouet")

run = "20261108-100000-t06-jouet"
os.chdir(depot)
code = la5._main(["--config", "config-jouet.json", "--run-id", run])
dossier = depot / "diag" / run
ep = verifier_resultat(depot, dossier / "episodes-t06.json")["resultat"]
di = verifier_resultat(depot, dossier / "distillation-t06.json")["resultat"]

spec = importlib.util.spec_from_file_location("extraire_v1", ARBRE / "scripts/extraire_mesures_epreuve_t06_v1.py")
ex = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex)
m = ex.mesures(depot)

controlees = Counter()
fiches_par_phase = Counter()
for f in ep["fiches"]:
    fiches_par_phase[f["phase"]] += 1
    controlees[f["phase"]] += len(f["equivalence"]["actions"])
print(json.dumps({
    "code_du_run_jouet": code,
    "1_extracteur_v1_equivalence_99e_centile": m["equivalence_99e_centile"],
    "1_cles_ecrites_sous_etats": {k: sorted(v) for k, v in ep["etats"].items()},
    "1_bloc_equivalence_par_fiche_present": all("equivalence" in f for f in ep["fiches"]),
    "1_fiches_par_phase": dict(fiches_par_phase),
    "1_actions_controlees_par_phase": dict(controlees),
    "1_controles_negatifs_par_phase": {k: {x: v.get(x) for x in ("comparables", "passent", "lecture", "statistique")} for k, v in ep["controles_negatifs"].items()},
    "2_extracteur_v1_pas_par_adaptateur": m["distillation"]["pas_par_adaptateur"],
    "2_extracteur_v1_pas_declares": m["distillation"]["pas_declares"],
    "2_pas_effectifs_ecrits_par_la_chaine": {ad: x["pas_declares"] for ad, x in di["donnees"].items()},
    "2_exemples_par_adaptateur": {ad: x["exemples"] for ad, x in di["donnees"].items()},
}, ensure_ascii=False, indent=1))
