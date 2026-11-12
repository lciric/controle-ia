"""Extraction des activations génériques, entraînement des 30 sondes de P3, choix des sondes principales, planchers.

- `preparer_tromperie`, `preparer_enjeux` : identifiants et empans des exemples génériques (module `empans`) ; un fait de
  `retrait_fin` jetons ou moins n'a pas d'empan : il sort de la recette (ses deux exemples), nommé et compté ; le run exige
  le compte cité par le préenregistrement (garde exacte : tokeniseur figé) ;
- `extraire` : passe unique du harnais par exemple, activations de l'empan aux couches lues, simple précision ;
- `entrainer_concept` : cinq familles × couches par `sondes.familles.entrainer` tel quel (réglages par défaut, une graine
  par sonde, dérivée du manifeste), aires sur la validation générique par la notation vectorisée (garde d'identité sur le
  premier exemple de validation, toutes familles), sonde principale : meilleure aire, ex aequo départagés par l'ordre
  famille puis couche ; pertes de chaque sonde relevées (première et dernière consignées ; une perte non finie arrête) ;
- `plancher_de` : 200 sondes aléatoires appariées en covariance des jetons d'entraînement de la principale, à sa couche,
  même agrégation (`sondes.evaluation.plancher_apparie`).
"""
from __future__ import annotations

import time

import numpy as np

from ..gardes import GardeArret, exiger_sans_signal
from ..harnais.activations import passe_unique
from ..harnais.formats import _ids
from ..sondes.evaluation import aire_sous_courbe, plancher_apparie
from ..sondes.familles import Reglages, entrainer
from .empans import jetons_message_utilisateur, jetons_reponse_forcee
from .notation import Notation, exiger_identite

FAMILLES_P3 = ("difference_moyennes", "lineaire", "perceptron", "attention", "mahalanobis")


def agregation_de(famille: str) -> str:
    return "attention" if famille == "attention" else "max"


def noms_des_sondes(concept: str, couches) -> list[str]:
    return [f"{concept}-{f}-c{c}" for f in FAMILLES_P3 for c in couches]


def preparer_tromperie(fmt, exemples: list[dict], retrait_fin: int = 5) -> tuple[list[dict], list[str]]:
    sortie, exclus = [], []
    for e in exemples:
        if len(_ids(fmt.tok, e["reponse"].strip())) <= retrait_fin:
            if e["groupe"] not in exclus:
                exclus.append(e["groupe"])
            continue
        r = jetons_reponse_forcee(fmt, "", e["utilisateur"], e["reponse"], retrait_fin)
        sortie.append({**r, "y": e["y"], "groupe": e["groupe"]})
    return sortie, exclus


def preparer_enjeux(fmt, exemples: list[dict], max_jetons: int = 128) -> list[dict]:
    return [{**jetons_message_utilisateur(fmt, "", e["texte"], max_jetons), "y": e["y"], "groupe": e["groupe"]}
            for e in exemples]


def _echeance(echeance, quoi):
    exiger_sans_signal(quoi)
    if echeance is not None and time.perf_counter() > echeance:
        raise GardeArret(f"limite de durée dépassée pendant {quoi}")


def extraire(modele, exemples: list[dict], couches, echeance: float | None = None) -> dict[int, list[np.ndarray]]:
    sortie = {int(c): [] for c in couches}
    for k, ex in enumerate(exemples):
        _echeance(echeance, f"l'extraction (exemple {k})")
        acts = passe_unique(modele, ex["ids"], list(sortie))
        for c in sortie:
            a = acts[c][ex["debut"]:ex["fin"]]
            if a.shape[0] != ex["fin"] - ex["debut"] or a.shape[0] < 1:
                raise GardeArret(f"exemple {k} : empan [{ex['debut']}, {ex['fin']}[ hors des {acts[c].shape[0]} positions")
            if not np.all(np.isfinite(a)):
                raise GardeArret(f"exemple {k} : activation non finie à la couche {c}")
            sortie[c].append(np.ascontiguousarray(a, dtype=np.float32))
    return sortie


def entrainer_concept(concept: str, sequences: dict, y, idx_e: list[int], idx_v: list[int], couches,
                      graines: dict[str, int], appareil: str = "cpu", echeance: float | None = None) -> dict:
    y = np.asarray(y)
    if len(set(y[idx_v].tolist())) < 2 or len(set(y[idx_e].tolist())) < 2:
        raise GardeArret(f"{concept} : les deux classes sont nécessaires à l'entraînement et à la validation")
    candidates, durees, pertes = [], {}, {}
    for famille in FAMILLES_P3:
        for c in couches:
            nom = f"{concept}-{famille}-c{c}"
            _echeance(echeance, f"l'entraînement de {nom}")
            depart = time.perf_counter()
            r = Reglages()
            s = entrainer(famille, nom, int(c), [sequences[c][i] for i in idx_e], y[idx_e], agregation_de(famille),
                          int(graines[nom]), r)
            durees[nom] = round(time.perf_counter() - depart, 2)
            p = [float(x["perte"]) for x in r.journal]
            mauvaise = next((x for x in r.journal if not np.isfinite(float(x["perte"]))), None)
            if mauvaise is not None:            # époque réelle du journal, pas le rang de la ligne (RC-06)
                raise GardeArret(f"{nom} : perte non finie pendant l'entraînement (époque {mauvaise.get('epoque')})")
            pertes[nom] = {"premiere": p[0], "derniere": p[-1], "relevees": len(p)} if p else None
            candidates.append(s)
    notation = Notation(candidates, appareil)
    valeurs = {s.nom: [] for s in candidates}
    identite = None
    for k, i in enumerate(idx_v):
        if k % 50 == 0:
            _echeance(echeance, f"la validation de {concept}")
        seg = {c: sequences[c][i] for c in couches}
        sc = notation.noter(seg)
        if k == 0:
            identite = exiger_identite(notation, seg, sc)
        for n, v in sc.items():
            valeurs[n].append(v)
    aires = {n: aire_sous_courbe(np.array(v), y[idx_v]) for n, v in valeurs.items()}
    k = max(range(len(candidates)), key=lambda j: (aires[candidates[j].nom], -j))
    return {"sondes": candidates, "aires_validation": aires, "principale": candidates[k].nom,
            "durees_entrainement_s": durees, "pertes": pertes, "identite_validation": identite,
            "n_entrainement": len(idx_e), "n_validation": len(idx_v)}


def plancher_de(principale, sequences: dict, idx_e: list[int], n_sondes: int, graine: int) -> list:
    c = int(principale.couche)
    return plancher_apparie(f"{principale.nom}-plancher", c, [sequences[c][i] for i in idx_e], principale.agregation,
                            int(n_sondes), int(graine))
