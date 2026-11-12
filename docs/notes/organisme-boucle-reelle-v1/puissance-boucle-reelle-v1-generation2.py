"""Complément de `puissance-boucle-reelle-v1.py` (inchangé, R12) : la génération 2 du dessin du brouillon 1 — v1.

Rédacteur neuf (Claude Opus 5.5), 7 novembre 2026. Aucun appel de modèle, aucun réseau, aucune clé ; le dépôt de l'organisme
est importé en lecture seule.

Ce que le complément simule, pour chaque répétition : la génération 1 exactement comme le script v1 (mêmes graines, mêmes
tâches, donc mêmes retenues), puis la génération 2, dont l'archive de jugement est {K1} plus les lois vraies **retenues** en
génération 1 (promues puis survivantes) — la sélection lue par la génération suivante. Les huit lois plantées et T-ELIM sont
replantées et jugées avec ces membres d'archive (tâches neuves « generation=2 »).

Prédiction P5 du brouillon : toute loi vraie retenue en génération 1 est refusée en génération 2 (elle est devenue un membre du
nul v8) ; les fausses restent refusées. C'est la preuve, au niveau des verdicts, que la génération 2 lit la sélection : si
elle ne la lisait pas (archive de jugement {K1} seule), V1 et V2 seraient promues de nouveau (bras « artefact »).

Usage : /home/user/controle-ia-travail/.venv/bin/python -I -B puissance-boucle-reelle-v1-generation2.py SORTIE.json \
            --repetitions 1000 --processus 4 --graine 20261107
"""

import argparse
import datetime
import hashlib
import importlib.util
import json
import math
import os
import platform
import sys
from concurrent.futures import ProcessPoolExecutor

ICI = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("puissance_v1", os.path.join(ICI, "puissance-boucle-reelle-v1.py"))
P = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(P)

import numpy as np  # noqa: E402

VERSION = "puissance-boucle-reelle-v1-generation2"


def une_repetition(args):
    r, racine = args
    g1 = P.une_repetition((r, racine))
    m = P.monde()
    archive, vraies, fausses, instruments = P.lois_du_dessin(m)
    retenues = [v for v in vraies if g1["lois"][f"vraie|{v}"]["promue"] and g1["lois"][f"vraie|{v}"]["survit"] is True]
    archive2 = dict(archive)
    for v in retenues:
        archive2[v] = vraies[v]
    mfix = P.CARTES_REELLES + len(vraies) + len(fausses) + P.INSTRUMENTS
    seuil = math.log(mfix / P.ALPHA)
    tache = f"{P.VERSION}|rep={r}|generation=2"
    out = {"r": r, "retenues_g1": retenues, "lois": {}}
    for groupe, lois, arch in (("vraie", vraies, archive2), ("fausse", fausses, archive2), ("instrument", instruments, archive2),
                               ("vraie-sans-lecture-artefact", vraies, archive)):
        for nom, loi in lois.items():
            ev, d = P.A.juger_carte(loi, m, arch, racine, f"{tache}|{groupe}|{nom}")
            le = P.log_e_hors_famille(ev, seuil)
            out["lois"][f"{groupe}|{nom}"] = {"promue": bool(ev["promue"]) and le >= seuil,
                                              "log_w_max": round(ev["log_richesse_max"], 6),
                                              "membres_d_archive": d["membres_d_archive"]}
    return out


def main(argv=None):
    a = argparse.ArgumentParser()
    a.add_argument("sortie")
    a.add_argument("--repetitions", type=int, required=True)
    a.add_argument("--processus", type=int, default=1)
    a.add_argument("--graine", type=int, required=True)
    x = a.parse_args(argv)
    if os.path.exists(x.sortie):
        print(f"refus : {x.sortie} existe déjà (on n'écrase jamais)")
        return 2
    debut = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    ss = np.random.SeedSequence(x.graine)
    racines = [int(c.generate_state(1, dtype=np.uint64)[0]) for c in ss.spawn(x.repetitions)]
    with ProcessPoolExecutor(max_workers=x.processus) as ex:
        reps = list(ex.map(une_repetition, list(enumerate(racines)), chunksize=1))
    n = len(reps)
    m = P.monde()
    _, vraies, fausses, _ = P.lois_du_dessin(m)

    def part(f):
        k = sum(1 for r in reps if f(r))
        return {"x": k, "n": n, "p": round(k / n, 4), "wilson": [round(v, 4) for v in P.wilson(k, n)]}

    resume = {
        "P5_toute_vraie_retenue_en_g1_refusee_en_g2": part(
            lambda r: all(not r["lois"][f"vraie|{v}"]["promue"] for v in r["retenues_g1"])),
        "aucune_fausse_promue_en_g2": part(lambda r: not any(r["lois"][f"fausse|{f}"]["promue"] for f in fausses)),
        "artefact_g2_sans_lecture_une_vraie_retenue_promue_de_nouveau": part(
            lambda r: any(r["lois"][f"vraie-sans-lecture-artefact|{v}"]["promue"] for v in r["retenues_g1"])),
        "T_ELIM_refusee_en_g2_par_le_juge": part(lambda r: not r["lois"]["instrument|T-ELIM"]["promue"]),
        "par_loi": {},
    }
    for k in sorted(reps[0]["lois"]):
        resume["par_loi"][k] = {
            "promue": sum(1 for r in reps if r["lois"][k]["promue"]),
            "promue_parmi_retenues_g1": sum(1 for r in reps if r["lois"][k]["promue"] and k.split("|", 1)[1] in r["retenues_g1"]),
            "retenue_g1": sum(1 for r in reps if k.split("|", 1)[1] in r["retenues_g1"]),
            "log_w_max_max": round(max(r["lois"][k]["log_w_max"] for r in reps), 4), "n": n}
    sortie = {"version": VERSION, "debut_utc": debut,
              "fin_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
              "graine": x.graine, "repetitions": x.repetitions, "resume": resume,
              "versions": {"python": platform.python_version(), "numpy": np.__version__},
              "script_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
              "script_v1_sha256": hashlib.sha256(open(os.path.join(ICI, "puissance-boucle-reelle-v1.py"), "rb").read()).hexdigest(),
              "organisme_commit": "94bfd92", "repetitions_detail": reps}
    with open(x.sortie, "w", encoding="utf-8") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps({k: v for k, v in resume.items() if k != "par_loi"}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
