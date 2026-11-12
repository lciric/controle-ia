"""Puissance, recalculée par simulation hors ligne, de la plus petite course réelle de la boucle complète de l'organisme — v1.

Rédacteur neuf (Claude Opus 5.5), 7 novembre 2026. Aucun appel de modèle, aucun réseau, aucune clé. Le dépôt de l'organisme
(`/home/user/ideation-organism`, commit 94bfd92) est lu en lecture seule et importé tel quel : ce script n'y écrit rien.

Ce que le script simule : le dessin exact du brouillon 1
(`preenregistrement-boucle-reelle-organisme-v1-brouillon1.md`, section 4) —
- monde planté : la loi S-V1 de `exemples/temoins-pari-demo-v1.json` (monde du tour fermé v64) ;
- archive de départ scellée : une loi connue, K1 = S-V1 restreinte au trait z0 (colonne z1 mise à zéro) ;
- quatre lois vraies plantées V1 à V4 (portent de l'information sur le monde au-delà de K1) ;
- quatre lois fausses plantées F1 à F4, **toutes dans la classe que le nul v8 couvre** (recombinaisons de K1 seule :
  copie renommée, mélange à l'uniforme, mélange à une loi aveugle fixe, tempérée et inclinée — lignes T17s, T03u, T03b et
  T05s du banc des tricheurs v8) ;
- chaque loi plantée jugée par la fonction du juge de la boucle (`pole/a_blanc_v59.juger_carte`, nul v8, 200 tirages frais,
  membres d'archive de K1), retenue si promue et si son log e atteint log(m/α) (règle « hors famille » de
  `pole/tour_ferme_v64.juger`, m fixé) ;
- test de mort de chaque loi retenue : la statistique gelée du tour fermé (gain moyen de log-score sur la marginale empirique
  de la tranche, comptes + 0,5), sur une tranche de 400 épisodes tirée du monde, seuil 0,02 nat (`SEUIL_TEST`).
Le bras « artefact » juge les mêmes fausses lois **sans** membres d'archive (canal des témoins de la v64) : il montre ce qui
arriverait si la chaîne les jugeait hors de la classe couverte.

Critère composé (prédiction P1 du brouillon) : au moins une vraie promue puis survivante ET aucune fausse promue.

Usage (depuis n'importe où) :
  /home/user/controle-ia-travail/.venv/bin/python -I -B puissance-boucle-reelle-v1.py SORTIE.json --repetitions 200 \
      --processus 4 --graine 20261107
"""

import argparse
import datetime
import hashlib
import json
import math
import os
import platform
import sys
from concurrent.futures import ProcessPoolExecutor

ORGANISME = "/home/user/ideation-organism/orchestrator"
if ORGANISME not in sys.path:
    sys.path.insert(0, ORGANISME)

import numpy as np  # noqa: E402

from pole import a_blanc_v59 as A  # noqa: E402
from pole import boucle_fermee_v59 as bf  # noqa: E402
from pole import selection_pari as sp  # noqa: E402
from pole import tour_ferme_v64 as T  # noqa: E402
from pole.oracle_tour_ferme_v60 import Oracle  # noqa: E402

ALPHA = 0.05
CARTES_REELLES = 12          # douze fiches des deux fournisseurs (six chacun)
INSTRUMENTS = 2              # T-ELIM et T-MAL (cas d'instrument, hors des 4 + 4)
SEUIL_MORT = 0.02            # « au moins 0,02 » nat (SEUIL_TEST du tour fermé)
VERSION = "puissance-boucle-reelle-v1"


def monde():
    m = A.charger_monde(ORGANISME)
    return m


def lois_du_dessin(m):
    """Archive de départ, quatre vraies, quatre fausses (classe couverte), deux cas d'instrument."""
    L = m["loi"]
    P, b = L["poids"], L["biais"]
    # K1 : la meilleure loi softmax du seul trait z0, ajustée une fois au maximum de vraisemblance attendue sous S-V1 sur les
    # 4 000 instances de l'oracle (racine SeedSequence(20261107, spawn_key=(2,)) ; script `essai-a-blanc-v1/ajuster_k1_v1.py`),
    # arrondie à 6 décimales et gelée ici en littéral (gain oracle 0,050571 nat : informative, faible).
    k1 = {"type": "softmax", "poids": [[0.0, 0.0], [-0.834964, 0.0], [-0.242046, 0.0]], "biais": [0.0, 0.941698, 0.721847]}
    v2 = {"type": "softmax", "poids": [[0.0, ligne[1]] for ligne in P], "biais": list(b)}
    uniforme = {"type": "fixe", "probas": [1.0, 1.0, 1.0]}
    aveugle = {"type": "fixe", "probas": [0.3, 0.4, 0.3]}
    vraies = {
        "V1-loi-du-monde": L,
        "V2-trait-z1-seul": v2,
        "V3-loi-du-monde-temperee-0.08": {"type": "transformee", "base": L, "puissance": 0.08},
        "V4-loi-du-monde-melee-uniforme-0.85": {"type": "melange", "composantes": [L, uniforme], "poids": [0.15, 0.85]},
    }
    fausses = {
        "F1-copie-renommee-de-K1": json.loads(json.dumps(k1)),
        "F2-K1-melee-uniforme-0.2": {"type": "melange", "composantes": [k1, uniforme], "poids": [0.8, 0.2]},
        "F3-K1-melee-aveugle-fixe-0.2": {"type": "melange", "composantes": [k1, aveugle], "poids": [0.8, 0.2]},
        "F4-K1-temperee-inclinee": {"type": "transformee", "base": k1, "puissance": 1.2, "inclinaison": [0.0, 0.05, -0.05]},
    }
    instruments = {"T-ELIM": {"type": "transformee", "base": L, "puissance": 1.25}}
    return {"K1": k1}, vraies, fausses, instruments


def tranche(m, racine, tache):
    rng = __import__("random").Random(bf.graine_de_tache(racine, f"{tache}|tranche"))
    out = []
    for x in sp.tirer_instances(rng, A.EPISODES_TRANCHE, A.DIM):
        y = sp.tirer_categorie(rng, sp.proba(m["loi"], x, [], 0))
        out.append((x, y))
    return out


def statistique(loi, lignes):
    """Même formule que `tour_ferme_v64.statistique_hors_bac`, sur les lignes en mémoire (aucun fichier)."""
    comptes = [0.5] * A.K
    for _, y in lignes:
        comptes[y] += 1
    s = sum(comptes)
    marg = [c / s for c in comptes]
    g = [math.log(max(sp.proba(loi, x, [], 0)[y], 1e-12)) - math.log(marg[y]) for x, y in lignes]
    return sum(g) / len(g)


def log_e_hors_famille(ev, seuil):
    if ev.get("marge_atteinte") is False:
        return -math.inf
    traj = ev["trajectoire_log_w"]
    return next((v for v in traj if v >= seuil), traj[-1])


def une_repetition(args):
    r, racine = args
    m = monde()
    archive, vraies, fausses, instruments = lois_du_dessin(m)
    mfix = CARTES_REELLES + len(vraies) + len(fausses) + INSTRUMENTS
    seuil = math.log(mfix / ALPHA)
    tache = f"{VERSION}|rep={r}"
    lignes = tranche(m, racine, tache)
    res = {"r": r, "racine": racine, "lois": {}}
    for groupe, lois, arch in (("vraie", vraies, archive), ("fausse", fausses, archive),
                               ("fausse-sans-archive-artefact", fausses, {}), ("instrument", instruments, archive),
                               ("vraie-sans-archive", vraies, {})):
        for nom, loi in lois.items():
            ev, d = A.juger_carte(loi, m, arch, racine, f"{tache}|{groupe}|{nom}")
            le = log_e_hors_famille(ev, seuil)
            promue = bool(ev["promue"]) and le >= seuil
            stat = statistique(loi, lignes) if promue else None
            seuil_mort = 2.0 if nom == "T-ELIM" else SEUIL_MORT
            res["lois"][f"{groupe}|{nom}"] = {
                "promue_seule": bool(ev["promue"]), "promue": promue,
                "log_e": None if math.isinf(le) else round(le, 6),
                "log_w_max": round(ev["log_richesse_max"], 6), "membres_d_archive": d["membres_d_archive"],
                "statistique_mort": None if stat is None else round(stat, 6),
                "survit": None if stat is None else stat >= seuil_mort}
    return res


def resumer(reps, vraies, fausses):
    n = len(reps)

    def part(f):
        x = sum(1 for r in reps if f(r))
        return {"x": x, "n": n, "p": round(x / n, 4), "wilson": [round(v, 4) for v in wilson(x, n)]}

    def ps(r, g, nom):
        e = r["lois"][f"{g}|{nom}"]
        return e["promue"] and e["survit"] is True

    out = {
        "P1_au_moins_une_vraie_promue_survivante_et_aucune_fausse_promue": part(
            lambda r: any(ps(r, "vraie", v) for v in vraies) and not any(r["lois"][f"fausse|{f}"]["promue"] for f in fausses)),
        "au_moins_une_vraie_promue_survivante": part(lambda r: any(ps(r, "vraie", v) for v in vraies)),
        "toutes_les_vraies_promues_survivantes": part(lambda r: all(ps(r, "vraie", v) for v in vraies)),
        "aucune_fausse_promue": part(lambda r: not any(r["lois"][f"fausse|{f}"]["promue"] for f in fausses)),
        "artefact_au_moins_une_fausse_promue_sans_archive": part(
            lambda r: any(r["lois"][f"fausse-sans-archive-artefact|{f}"]["promue"] for f in fausses)),
        "T_ELIM_promue_puis_eliminee": part(lambda r: r["lois"]["instrument|T-ELIM"]["promue"]
                                           and r["lois"]["instrument|T-ELIM"]["survit"] is False),
        "par_loi": {},
    }
    for g in ("vraie", "vraie-sans-archive", "fausse", "fausse-sans-archive-artefact", "instrument"):
        noms = sorted({k.split("|", 1)[1] for r in reps for k in r["lois"] if k.startswith(g + "|")})
        for nom in noms:
            k = f"{g}|{nom}"
            pr = sum(1 for r in reps if r["lois"][k]["promue"])
            sv = sum(1 for r in reps if r["lois"][k]["promue"] and r["lois"][k]["survit"] is True)
            lw = [r["lois"][k]["log_w_max"] for r in reps]
            out["par_loi"][k] = {"promue": pr, "promue_puis_survivante": sv, "n": n,
                                 "log_w_max_mediane": round(float(np.median(lw)), 4),
                                 "log_w_max_max": round(float(np.max(lw)), 4)}
    return out


def wilson(x, n, z=1.959963984540054):
    if n == 0:
        return (0.0, 1.0)
    p = x / n
    c = (p + z * z / (2 * n)) / (1 + z * z / n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return (max(0.0, c - h), min(1.0, c + h))


def oracle_des_lois(racine):
    m = monde()
    archive, vraies, fausses, instruments = lois_du_dessin(m)
    o = Oracle(m["loi"], racine, A.DIM)
    out = {}
    for nom, loi in list(vraies.items()) + list(fausses.items()) + list(instruments.items()) + [("K1", archive["K1"])]:
        out[nom] = o.mesurer(loi, {} if nom == "K1" else archive)
    for nom in ("S-F1", "S-F2", "S-F4"):
        out[f"temoin-v64-{nom}"] = o.mesurer(m["fausses"][nom], {})
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
    racine_oracle = int(np.random.SeedSequence(x.graine, spawn_key=(10 ** 6,)).generate_state(1, dtype=np.uint64)[0])
    with ProcessPoolExecutor(max_workers=x.processus) as ex:
        reps = list(ex.map(une_repetition, list(enumerate(racines)), chunksize=1))
    m = monde()
    archive, vraies, fausses, instruments = lois_du_dessin(m)
    sortie = {
        "version": VERSION, "debut_utc": debut,
        "fin_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "graine": x.graine, "regle_graines": "numpy.random.SeedSequence(graine).spawn(repetitions) ; tâches dérivées par "
                                            "boucle_fermee_v59.graine_de_tache(racine, tâche)",
        "repetitions": x.repetitions, "m_fixe": CARTES_REELLES + len(vraies) + len(fausses) + INSTRUMENTS, "alpha": ALPHA,
        "seuil_mort_nat": SEUIL_MORT, "tirages_par_loi": A.TIRAGES, "episodes_de_tranche": A.EPISODES_TRANCHE,
        "monde": {"source": m["source"], "sha256": m["sha256"], "loi_vraie": m["loi_vraie"]},
        "lois": {"archive": archive, "vraies": vraies, "fausses": fausses, "instruments": instruments},
        "oracle": oracle_des_lois(racine_oracle),
        "resume": resumer(reps, vraies, fausses),
        "versions": {"python": platform.python_version(), "numpy": np.__version__},
        "script_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
        "organisme_commit": "94bfd92",
        "repetitions_detail": reps,
    }
    with open(x.sortie, "w", encoding="utf-8") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps({"resume": {k: v for k, v in sortie["resume"].items() if k != "par_loi"},
                      "oracle": sortie["oracle"]}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
