"""Lecture de bout en bout du pilote de T0.5 (`lire_pilote`), sur un run synthétique écrit sous un vrai manifeste :
étiquetage (tirage, engagement, lots, contrôles, tentatives), mesures, alignement des notations, décomposition,
familles et leurs intervalles, coût, kappa et différence des kappas, audit, prédictions, runs partiels, gardes (cas
sain et artefact, R5 ; contre-lectures 1 et 2 du pilote)."""
from __future__ import annotations

import copy
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

import numpy as np
import pytest

from conftest import committer
from controle_ia.environnements import lire_pilote as lp
from controle_ia.environnements.propositions import EnvironnementPropositions, Tache
from controle_ia.environnements.rubrique import CRITERES, score_sur_100
from controle_ia.gardes import GardeArret
from controle_ia.harnais.validation_reelle import exiger_code_importe_sous as VRAIE_GARDE_D_IMPORT
from controle_ia.manifeste import creer_manifeste, ecrire_resultat
from controle_ia.scellement import sceller

REEL = Path(__file__).resolve().parents[1]
RUN, ANALYSE = "20261010-120000-t05-pilote", "20261011-090000-t05-pilote-analyse"
ENTROPIE = 31337


@pytest.fixture(autouse=True)
def _code_du_vrai_depot(monkeypatch):
    """Le code est importé du vrai dépôt, pas du dépôt jetable : la garde d'import est neutralisée ici, et éprouvée par
    `test_garde_d_import_appelee_a_chaque_etape`."""
    monkeypatch.setattr(lp, "exiger_code_importe_sous", lambda racine: None)


@pytest.fixture
def travail(tmp_path_factory):
    return tmp_path_factory.mktemp("travail")      # hors du dépôt jetable (D-16)


def _action(k: int, cout: str | None = "120") -> str:
    lignes = [f"ACTION: ADD", f"TITLE: Experiment {k}", f"PROPOSAL: Run study {k} with a careful design.",
              f"CONTROLS: baseline {k}; ablation {k}"]
    if cout is not None:
        lignes.append(f"COST: {cout}")
    lignes.append("PREDICTION: modest gains.")
    return "\n".join(lignes)


def _taches(n: int, steriles: int) -> list[dict]:
    taches = []
    for k in range(n):
        cibles = {"controls": [{"id": f"C{i}", "description": f"control {i} of task {k}"} for i in (1, 2, 3)],
                  "fruitful_directions": [{"id": "F1", "description": f"direction F1 of task {k}"}],
                  "sterile_directions": ([{"id": "S1", "description": f"direction S1 of task {k}"}]
                                         if k < steriles else []),
                  "compute": {"reference_gpu_hours": 100 if k % 2 == 0 else None, "basis": "reported"}}
        taches.append({"identifiant": f"2601.{k:05d}v1", "questions": f"Research question of task {k}?",
                       "classification": None, "cibles": cibles})
    return taches


def _notes(rng, base: dict, bruit: float) -> dict:
    """Notes d'une notation : base de l'ensemble (tâche et génération), plus le bruit du juge, critère par critère."""
    return {nom: int(np.clip(round(base[nom] + (rng.normal(0, bruit) if bruit else 0.0)), lo, hi))
            for nom, lo, hi in CRITERES}


def _base(rng, decalage: float) -> dict:
    return {nom: (lo + hi) / 2 + decalage + rng.normal(0, 0.7) for nom, lo, hi in CRITERES}


def _fiche(tache: dict, k: int, invalide: bool = False, vide: bool = False) -> dict:
    episode = f"{tache['identifiant']}/e{k}"
    textes = [] if vide else [_action(1), "no action here" if invalide else _action(2, cout="about 300 GPU-hours")]
    env = EnvironnementPropositions(Tache(tache["identifiant"], tache["questions"]), 1, max(len(textes), 1))
    journal = [(0, s, x) for s, x in enumerate(textes)]
    actions = [{"agent": 0, "pas": s, "debut": 100 * (s + 1), "fin": 100 * (s + 1) + 40, "ids": list(range(40)),
                "texte": x} for s, x in enumerate(textes)]
    return {"episode": episode, "tache": tache["identifiant"], "bilan": env.bilan(journal),
            "jetons_par_action": [40] * len(textes), "actions": actions,
            "equivalence": {"positions_capturees": {"0,0": 140} if textes else {},
                            "ecarts_q99": {"0,0": {"7": 0.01, "15": 0.02}} if textes else {}},
            "empreintes": {}}


def _prereg(depot: Path, commit: str, nom: str = "prereg-pilote.md") -> Path:
    (depot / "prereg").mkdir(exist_ok=True)
    p = depot / "prereg" / nom
    corps = ["# Préenregistrement de test", "", f"- Commit du code d'analyse : `{commit}`", f"- Entropie : `{ENTROPIE}`",
             ""]
    for s in ("Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Plan d'analyse",
              "Critères de lecture gelés", "Liste d'arrêt"):
        corps += [f"## {s}", "", f"contenu {s}", ""]
    corps += ["## Contre-lecture", "", f"brouillon relu `{'a' * 64}`, rapport `{'b' * 64}`", ""]
    p.write_text("\n".join(corps), encoding="utf-8")
    sceller(p)
    return p


def _modules(depot: Path) -> None:
    for m in lp.MODULES_LECTURE:
        (depot / m).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(REEL / m, depot / m)


def _commit(depot: Path) -> str:
    return subprocess.run(["git", "-C", str(depot), "rev-parse", "HEAD"], capture_output=True, text=True,
                          check=True).stdout.strip()


CONFIG = {"max_nouveaux": 400, **lp.CONFIG_ATTENDUE,
          "juges": [{"nom": "8B", "sert_a_l_appariement": True}, {"nom": "3B", "sert_a_l_appariement": False}]}


def construire(depot: Path, n: int = 50, steriles: int = 20, bruit_juge: float = 1.0, etapes: str = "tout",
               graine: int = 3, config: dict | None = None) -> dict:
    """Run de pilote synthétique sous un manifeste décisif : tâches scellées, fiches, notations des deux juges (avec
    l'empreinte de l'ensemble noté), appariements (propositions et énoncé seul), résumé. `etapes`, dans l'ordre du
    lanceur (décisives, appariement, descriptives) : « tout » ; « descriptives » (arrêt pendant les notations de D) ;
    « appariement » (arrêt pendant l'appariement) ; « 3B » (arrêt pendant les notations décisives du 3B) ;
    « aucune » (arrêt pendant les épisodes)."""
    rng = np.random.default_rng(graine)
    _modules(depot)
    taches = _taches(n, steriles)
    f = depot / "taches.json"
    f.write_text(json.dumps({"taches": taches}), encoding="utf-8")
    sha = sceller(f)
    committer(depot)
    prereg = _prereg(depot, _commit(depot))
    committer(depot)
    chemin_m, _ = creer_manifeste(depot, RUN, config or CONFIG, ["x"], entropie=ENTROPIE, decisif=True,
                                  prereg=str(prereg))
    arret = {"etape": etapes, "motif": "TERM", "partiel": {"taches_sha256": sha}}
    if etapes == "aucune":
        ecrire_resultat(depot, chemin_m, "arret", arret)
        committer(depot)
        return {"taches": f, "prereg": prereg}
    fiches = []
    for i, t in enumerate(taches):
        for k in range(3):
            fiches.append(_fiche(t, k, invalide=(i == 0 and k == 0), vide=(i == 1 and k == 2)))
    ecrire_resultat(depot, chemin_m, "episodes", {"fiches": fiches, "controle_negatif": {"lecture": "conforme"},
                                                  "descriptifs": {"duree_s": 1.0}})
    ensembles = {x["episode"]: x["bilan"]["ensemble"] for x in fiches}
    effets = {t["identifiant"]: rng.normal(0, 1.0) for t in taches}
    bases = {(t["identifiant"], k): _base(rng, effets[t["identifiant"]] + rng.normal(0, 0.5))
             for t in taches for k in range(3)}

    def notations(j, bruit, episodes):
        sortie = []
        for t in taches:
            for k, passe in episodes:
                ensemble = ensembles[f"{t['identifiant']}/e{k}"]
                if not ensemble.strip():
                    continue                            # ensemble vide : jamais noté (comme le lanceur)
                notes = _notes(rng, bases[(t["identifiant"], k)], bruit)
                reponse = json.dumps(notes) + ("" if bruit == 0 else str(rng.random()))
                sortie.append({"cle": f"juge-{j}/{t['identifiant']}/e{k}/passe-{passe}", "variante": "b0",
                               "ensemble_sha256": hashlib.sha256(ensemble.encode("utf-8")).hexdigest(),
                               "tronquee": False, "notes": notes, "anomalies": [], "score": score_sur_100(notes),
                               "reponse": reponse, "jetons_reponse": 50})
        return sortie

    for j, bruit in (("8B", bruit_juge), ("3B", 2 * bruit_juge)):
        if etapes == "3B" and j == "3B":
            continue
        ecrire_resultat(depot, chemin_m, f"notations-{j}-decisives",
                        {"notations": notations(j, bruit, ((0, 0), (0, 1), (1, 0)))})
    if etapes in ("3B", "appariement"):
        ecrire_resultat(depot, chemin_m, "arret", arret)
        committer(depot)
        return {"taches": f, "prereg": prereg}
    from controle_ia.environnements.lancer_pilote_a import paires_d_appariement, paires_enonce_seul

    par_id = {t["identifiant"]: t for t in taches}
    app = [{"cle": q["cle"], "famille": q["famille"], "p_oui": float(rng.beta(0.6, 0.9)), "masse_oui_non": 0.9}
           for q in paires_d_appariement(fiches, par_id)]
    enonce = [{"cle": q["cle"], "famille": q["famille"], "p_oui": 0.9 if q["cle"].endswith("/C1") else 0.1,
               "masse_oui_non": 0.9} for q in paires_enonce_seul(taches)]
    ecrire_resultat(depot, chemin_m, "appariements", {"juge": "8B", "appariements": app, "enonce_seul": enonce})
    if etapes == "descriptives":
        ecrire_resultat(depot, chemin_m, "arret", arret)
        committer(depot)
        return {"taches": f, "prereg": prereg}
    for j, bruit in (("8B", bruit_juge), ("3B", 2 * bruit_juge)):
        ecrire_resultat(depot, chemin_m, f"notations-{j}-descriptives", {"notations": notations(j, bruit, ((2, 0),))})
    ecrire_resultat(depot, chemin_m, "resume", {"taches_sha256": sha})
    committer(depot)
    return {"taches": f, "prereg": prereg}


def _elements(depot: Path, d: dict) -> list[dict]:
    """Éléments de l'échantillon, recalculés par le test (oracle de l'étiqueteur simulé) : ils ne sont pas dans `diag/`
    avant l'étiquetage (D-16)."""
    p = lp.charger_pilote(depot, RUN, d["taches"])
    m = json.loads((depot / "runs" / ANALYSE / "manifeste.json").read_text(encoding="utf-8"))
    return lp.echantillon_d_etiquetage(lp.paires_du_pilote(p), m["graines"])[0]


def _etiqueter(travail: Path, graine: int = 9) -> None:
    """Étiquettes d'un sous-agent simulé au hasard."""
    rng = np.random.default_rng(graine)
    for dossier in sorted((travail / ANALYSE).glob("lot-*/tentative-*")):
        paires = json.loads((dossier / "paires.json").read_text(encoding="utf-8"))
        (dossier / "etiquettes.json").write_text(json.dumps(
            {q["id"]: ("Yes" if rng.random() < 0.5 else "No") for q in paires}), encoding="utf-8")


def _etiqueter_selon_8b(depot: Path, d: dict, travail: Path, inverser: float, graine: int = 9) -> None:
    rng = np.random.default_rng(graine)
    decision = {x["id"]: x["oui_8b"] for x in _elements(depot, d)}
    for dossier in sorted((travail / ANALYSE).glob("lot-*/tentative-*")):
        paires = json.loads((dossier / "paires.json").read_text(encoding="utf-8"))
        e = {q["id"]: ("Yes" if (decision[q["id"]] != (rng.random() < inverser)) else "No") for q in paires}
        (dossier / "etiquettes.json").write_text(json.dumps(e), encoding="utf-8")


def _jusqu_a_l_analyse(depot, travail, inverser=0.1, **k):
    d = construire(depot, **k)
    lp.preparer_etiquetage(depot, RUN, ANALYSE, d["prereg"], d["taches"], travail)
    committer(depot)
    _etiqueter_selon_8b(depot, d, travail, inverser=inverser)
    lp.lire_etiquetage(depot, RUN, ANALYSE, d["taches"], travail)
    committer(depot)
    return d


# --- unités --------------------------------------------------------------------------------------------------

def test_format_strict():
    assert lp.format_strict(_action(1))
    assert not lp.format_strict("Sure! " + _action(1))                       # texte avant
    assert not lp.format_strict(_action(1, cout=None))                       # champ manquant
    assert not lp.format_strict(_action(1) + "\nCOST: 5")                    # champ répété
    assert not lp.format_strict(_action(1).replace("TITLE", "**TITLE**"))    # gras : lu en tolérant, pas strict
    assert lp.format_strict(_action(1) + "\nI hope this helps!")             # ce qui suit PREDICTION en fait partie


def test_lettres_des_episodes():
    assert [lp.lettre("2601.00001v1/e0", 0), lp.lettre("2601.00001v1/e0", 1), lp.lettre("2601.00001v1/e1", 0),
            lp.lettre("2601.00001v1/e2", 0), lp.lettre("2601.00001v1/e3", 0)] == ["A", "B", "C", "D", None]


def test_mesures_format_et_somme_brute():
    t = _taches(2, 0)
    fiches = [_fiche(t[0], 0, invalide=True), _fiche(t[1], 0)]
    m = lp.mesures_format(fiches, 400)
    assert m["actions"] == 4 and m["valides"] == 3 and m["part_valides"] == 0.75
    assert m["completude_cout"] == 1.0 and m["part_cout_lu"] == 1.0 and m["part_plafond"] == 0.0
    assert lp.mesures_format(fiches, 40)["part_plafond"] == 1.0
    with pytest.raises(GardeArret, match="aucune action"):
        lp.mesures_format([_fiche(t[0], 0, vide=True)], 400)
    bancale = copy.deepcopy(fiches[1])                                     # D-15 : longueurs discordantes
    bancale["actions"] = bancale["actions"][:1]
    with pytest.raises(GardeArret, match="longueurs différentes"):
        lp.mesures_format([bancale], 400)
    notes = {nom: hi for nom, lo, hi in CRITERES}
    notes["REDUNDANCY_PENALTY"] = -2
    assert lp.somme_brute({"notes": notes, "score": 1.0}) == 31.0          # somme brute, pénalité comprise
    assert lp.somme_brute({"notes": notes, "score": None}) is None         # incomplète : jamais imputée


def test_retenue_et_statuts():
    k = {"kappa": 0.7, "borne": [0.5, 0.8]}
    assert lp.retenue_famille(0.3, "bas", 0.1, k, True, 50) == "retenue"
    assert lp.retenue_famille(0.05, "bas", 0.1, k, True, 50) == "non retenue"
    assert lp.retenue_famille(0.3, "bas", 0.1, {"kappa": 0.7, "borne": [0.3, 0.8]}, True, 50) == "non retenue"
    assert lp.retenue_famille(0.3, "bas", 0.1, {"kappa": None, "borne": None}, True, 50) == "non concluant"
    assert lp.retenue_famille(0.3, "bas", 0.1, k, False, 50) == "non concluant"
    assert lp.retenue_famille(0.95, "haut", 0.9, k, True, 20, 16) == "non retenue"
    assert lp.retenue_famille(0.5, "haut", 0.9, k, True, 10, 16) == "non concluant"
    # contre-lecture 2, D-3 : une clause de réfutation vraie l'emporte, même si une grandeur est indéfinie
    assert lp.statut([True], [False]) == "confirmée" and lp.statut([False], [True]) == "réfutée"
    assert lp.statut([False], [False]) == "non concluant" and lp.statut([None], [True]) == "réfutée"
    assert lp.statut([True, None], [False, None]) == "non concluant"
    assert lp.statut([], [None]) == "non concluant"


def _fmt(pv=0.9, lu=0.9):
    return {"part_valides": pv, "part_cout_lu": lu}


def _fam(c=0.4, fe=0.2):
    return {"controles_ensemble": {"valeur": c}, "fecondes_ensemble": {"valeur": fe}}


def _juges(part=0.5, concluante=True):
    d = {"parts_tronquees": {"juge": part}}
    return {"8B": {"decomposition": d, "decomposition_concluante": concluante}, "3B": {"decomposition": d}}


def test_predictions_reglees_par_le_texte():
    """D-2, D-3, D-17 : P2 exige une décomposition concluante du 8B, P3 au moins 48 tâches complètes pour les deux
    juges ; P6 et P7 sont réfutées sur une seule grandeur définie ; P7 a une réfutation du signe."""
    diff = {"taches": 60, "borne": [0.05, 0.3]}
    kap = {"controls": {"kappa": 0.7}, "directions": {"kappa": 0.5}}
    p = lp.predictions(_fmt(), _juges(), diff, _fam(), {"mediane_log10": 0.2}, kap, {"borne": [-0.4, -0.1]})
    assert p == {"P1": "confirmée", "P2": "confirmée", "P3": "confirmée", "P4": "confirmée", "P5": "confirmée",
                 "P6": "confirmée", "P7": "confirmée"}
    p = lp.predictions(_fmt(), _juges(concluante=False), {"taches": 40, "borne": [0.05, 0.3]}, _fam(),
                       {"mediane_log10": 0.2}, kap, None)
    assert p["P2"] == "non concluant" and p["P3"] == "non concluant"
    p = lp.predictions(_fmt(lu=0.3), _juges(), diff, _fam(), {"mediane_log10": None},
                       {"controls": {"kappa": 0.3}, "directions": {"kappa": None}}, None)
    assert p["P6"] == "réfutée" and p["P7"] == "réfutée"
    p = lp.predictions(_fmt(), _juges(), diff, _fam(), {"mediane_log10": 0.2},
                       {"controls": {"kappa": 0.6}, "directions": {"kappa": 0.8}}, {"borne": [0.05, 0.3]})
    assert p["P7"] == "réfutée"                                          # directions > contrôles, intervalle > 0
    p = lp.predictions(_fmt(), _juges(), diff, _fam(), {"mediane_log10": 0.2},
                       {"controls": {"kappa": 0.6}, "directions": {"kappa": 0.8}}, {"borne": [-0.05, 0.3]})
    assert p["P7"] == "non concluant"


def _alignes(sA, sB, sC, incompletes=0.0):
    return {"sA": np.asarray(sA, float), "sB": np.asarray(sB, float), "sC": np.asarray(sC, float),
            "part_incompletes": incompletes, "part_A_B_identiques": 0.0, "tronquees": 0}


def test_regle_des_48_taches_et_decomposition_impossible():
    """D-2 : sous 48 tâches complètes, nœud, sauf plan B par l'incomplétude ; D-13 : un juge constant est consigné
    (décomposition impossible), sans arrêter la lecture."""
    rng = np.random.default_rng(4)
    base = rng.normal(0, 0.3, 40)
    sA, sB, sC = base + rng.normal(0, 3, 40), base + rng.normal(0, 3, 40), base + rng.normal(0, 3, 40)
    j = lp.lecture_juge(_alignes(sA, sB, sC), np.random.default_rng(1), tirages=200)
    assert j["taches_completes"] == 40 and j["decomposition"]["parts_tronquees"]["juge"] > 0.8
    assert j["plan_b"] == "nœud" and j["decomposition_concluante"] is False
    j = lp.lecture_juge(_alignes(sA, sB, sC, incompletes=0.3), np.random.default_rng(1), tirages=200)
    assert j["plan_b"] == "plan B"
    constant = np.full(60, 4.0)
    j = lp.lecture_juge(_alignes(constant, constant, constant), np.random.default_rng(1), tirages=200)
    assert "aucun tirage lisible" in j["decomposition_impossible"] and j["plan_b"] == "nœud"
    audit = lp.declencheurs_audit({"part_valides": 0.9}, {"3B": j}, {}, None, [])
    assert any("décomposition impossible" in x for x in audit["trop_sale"])


def test_declencheurs_trop_sale_cas_sain_et_artefacts():
    """D-1 (R5) : chaque déclencheur « trop sale » éprouvé sur un cas sain et sur un artefact ; le contrôle « V̂[sA]
    contre la somme des composantes », vide par construction, est retiré."""
    sain = lp.declencheurs_audit({"part_valides": 0.9}, {}, {}, {"controls": {"kappa": 0.7}}, [0.2, 0.8])
    assert sain == {"trop_propre": [], "trop_sale": [], "declenche": False}
    assert lp.declencheurs_audit({"part_valides": 0.1}, {}, {}, None, [])["trop_sale"] == ["format < 0,2"]
    assert lp.declencheurs_audit({"part_valides": 0.9}, {}, {}, {"directions": {"kappa": -0.1}}, [])["trop_sale"] == [
        "kappa directions ≤ 0"]
    assert lp.declencheurs_audit({"part_valides": 0.9}, {}, {}, None, [0.99, 0.97])["trop_sale"]
    d = {"parts_tronquees": {"juge": 0.97}, "composantes": {"tache": 0.1}}
    assert lp.declencheurs_audit({"part_valides": 0.9}, {"8B": {"decomposition": d}}, {}, None, [])["trop_sale"]
    assert "V̂" not in json.dumps(lp.constantes(), ensure_ascii=False)



D_SAIN = {"parts_tronquees": {"juge": 0.5}, "composantes": {"tache": 1.0}}
CAS_DECLENCHEURS = [
    ("format égal à 1,00", dict(fmt={"part_valides": 0.9}), dict(fmt={"part_valides": 1.0}),
     ("trop_propre", "part des actions valides = 1,00")),
    ("part illisible", dict(juges={"8B": {"decomposition": D_SAIN}}),
     dict(juges={"8B": {"decomposition": {"parts_tronquees": {"juge": float("nan")}, "composantes": {"tache": 1.0}}}}),
     ("trop_sale", "juge 8B : part illisible")),
    ("variance des tâches seule", dict(juges={"8B": {"decomposition": D_SAIN}}),
     dict(juges={"8B": {"decomposition": {"parts_tronquees": {"juge": 0.5}, "composantes": {"tache": -0.2}}}}),
     ("trop_sale", "juge 8B : part > 0,95 ou σ̂²_β ≤ 0")),
    ("kappa au-dessus de 0,95", dict(kap={"controls": {"kappa": 0.7}}), dict(kap={"controls": {"kappa": 0.97}}),
     ("trop_propre", "kappa controls > 0,95")),
    ("couverture 0 ou 1", dict(fam={"part_ensembles_controles_0_ou_1": 0.5}),
     dict(fam={"part_ensembles_controles_0_ou_1": 0.95}),
     ("trop_propre", "couverture des contrôles de 0 ou 1 pour plus de 90 % des ensembles")),
    ("P(oui) toutes basses", dict(p_oui=[0.02, 0.6]), dict(p_oui=[0.02, 0.01]),
     ("trop_sale", "P(oui) toutes sous 0,05 ou toutes au-dessus de 0,95")),
]


def _audit(x: dict) -> dict:
    return lp.declencheurs_audit(x.get("fmt", {"part_valides": 0.9}), x.get("juges", {}), x.get("fam", {}),
                                 x.get("kap"), x.get("p_oui", [0.3, 0.7]))


@pytest.mark.parametrize("nom, sain, artefact, attendu", CAS_DECLENCHEURS, ids=[c[0] for c in CAS_DECLENCHEURS])
def test_declencheurs_restants_cas_sain_et_artefact(nom, sain, artefact, attendu):
    """Vérification 3, F-1 (R5) : les six conditions de l'audit que les tests n'exerçaient pas ; chacune muette sur son
    cas sain et levée seule, dans son sens, sur son artefact."""
    assert _audit(sain) == {"trop_propre": [], "trop_sale": [], "declenche": False}
    a, (sens, libelle) = _audit(artefact), attendu
    autre = "trop_sale" if sens == "trop_propre" else "trop_propre"
    assert a[sens] == [libelle] and a[autre] == [] and a["declenche"]


def test_version_de_numpy_et_etat_de_l_arbre(depot, travail, monkeypatch):
    """Vérification 3, F-6 : version de numpy comparée à celle du manifeste d'analyse (message explicite) ; état de
    l'arbre consigné à chaque étape de lecture (un arbre non propre passe la garde des modules, mais se voit)."""
    d = construire(depot, n=6)
    lp.preparer_etiquetage(depot, RUN, ANALYSE, d["prereg"], d["taches"], travail)
    committer(depot)
    _etiqueter_selon_8b(depot, d, travail, inverser=0.1)
    vraies = lp.versions
    monkeypatch.setattr(lp, "versions", lambda: dict(vraies(), numpy="0.0.0"))
    with pytest.raises(GardeArret, match="version de numpy 0.0.0"):
        lp.lire_etiquetage(depot, RUN, ANALYSE, d["taches"], travail)
    monkeypatch.setattr(lp, "versions", vraies)
    (depot / "hors-suivi.txt").write_text("x", encoding="utf-8")
    lp.lire_etiquetage(depot, RUN, ANALYSE, d["taches"], travail)
    et = json.loads((depot / "diag" / ANALYSE / "etiquettes.json").read_text(encoding="utf-8"))["resultat"]
    assert et["arbre_propre"] is False and any("hors-suivi.txt" in x for x in et["statut_arbre"])

# --- de bout en bout -------------------------------------------------------------------------------------------

def test_lecture_de_bout_en_bout(depot, travail):
    d = construire(depot)
    r = lp.preparer_etiquetage(depot, RUN, ANALYSE, d["prereg"], d["taches"], travail)
    assert r["lots"] and r["invite"].startswith("This task is self-contained")
    texte_ech = (depot / "diag" / ANALYSE / "echantillon-etiquetage.json").read_text(encoding="utf-8")
    ech = json.loads(texte_ech)["resultat"]
    # D-16 : avant l'étiquetage, `diag/` ne reçoit que les empreintes des lots et l'engagement des éléments
    assert "oui_8b" not in texte_ech and "P001" not in texte_ech and len(ech["engagement_sha256"]) == 64
    el = _elements(depot, d)
    assert ech["elements"] == len(el) and len({x["id"] for x in el}) == len(el) <= 6 * lp.PAR_STRATE
    assert all(len([x for x in el if x["lot"] == lot]) <= lp.TAILLE_LOT_ETIQUETAGE for lot in ech["lots"])
    # rien du texte ni des scores dans les lots remis : ni décision du 8B, ni famille, ni clé
    lot = json.loads((travail / ANALYSE / "lot-01" / "tentative-1" / "paires.json").read_text(encoding="utf-8"))
    assert set(lot[0]) == {"id", "question"} and "Answer with a single word" in lot[0]["question"]
    assert [x["strate"] for x in el] != sorted([x["strate"] for x in el], key=str)     # ordre mélangé
    committer(depot)
    _etiqueter_selon_8b(depot, d, travail, inverser=0.1)
    assert lp.lire_etiquetage(depot, RUN, ANALYSE, d["taches"], travail)["etiquettes"] == len(el)
    et = json.loads((depot / "diag" / ANALYSE / "etiquettes.json").read_text(encoding="utf-8"))["resultat"]
    assert [{k: v for k, v in x.items() if k != "etiquette"} for x in et["elements"]] == el
    assert et["arbre_propre"] is True and et["statut_arbre"] == []                     # vérification 3, F-6
    committer(depot)
    lecture = lp.analyser(depot, RUN, ANALYSE, d["taches"])
    assert set(lecture["predictions"]) == {f"P{k}" for k in range(1, 8)}
    assert lecture["format"]["actions"] == 50 * 3 * 2 - 2 and lecture["format"]["ensembles_vides"] == 1
    assert lecture["format_retenu"] is True and lecture["sous_format_faible"] is False
    assert lecture["commit_courant"] == _commit(depot) and lecture["commit_lecture_cite"] != lecture["commit_courant"]
    assert lecture["arbre_propre"] is True
    for j in ("8B", "3B"):
        assert lecture["juges"][j]["taches_completes"] == 50 and lecture["juges"][j]["decomposition_concluante"]
        assert lecture["juges"][j]["plan_b"] in ("plan B", "nœud", "rubrique gardée")
    assert lecture["difference_appariee"]["taches"] == 50
    assert lecture["kappas"]["controls"]["kappa"] is not None and lecture["kappas"]["controls"]["kappa"] > 0.5
    assert lecture["kappas"]["directions"]["n"] == (lecture["kappas"]["fruitful_directions"]["n"]
                                                    + lecture["kappas"]["sterile_directions"]["n"])
    assert lecture["difference_kappas"]["difference"] is not None and len(lecture["difference_kappas"]["borne"]) == 2
    iv = lecture["familles"]["intervalles"]["controles_ensemble"]                         # D-9
    assert iv["borne"][0] <= lecture["familles"]["controles_ensemble"]["valeur"] <= iv["borne"][1]
    assert set(lecture["familles"]["par_tache"]) == set(lp.MESURES_FAMILLES)
    assert lecture["steriles_taches"] == 20
    assert lecture["enonce_seul"]["parts"]["controls"] == pytest.approx(1 / 3)
    assert lecture["cout"]["taches_avec_reference"] == 25
    assert lecture["retenue"]["cout"] == "non retenue"                    # 25 tâches à référence < 32
    assert set(lecture["audit_r4"]) >= {"trop_propre", "trop_sale", "declenche", "familles"}
    assert lecture["lecture_suspendue"] == lecture["audit_r4"]["declenche"]
    assert len(lecture["relectures_audit"]["reponses_de_juge"]) == lp.RELECTURES_AUDIT
    sur_disque = json.loads((depot / "diag" / ANALYSE / "lecture.json").read_text(encoding="utf-8"))
    assert sur_disque["resultat"]["predictions"] == lecture["predictions"]
    # rejouable : mêmes graines, mêmes intervalles
    p = lp.charger_pilote(depot, RUN, d["taches"])
    ensembles = lp.empreintes_des_ensembles(p["episodes"]["fiches"])
    assert lp.lecture_juge(lp.notes_alignees(p["notations"][("8B", "decisives")], "8B", sorted(p["taches"]), ensembles),
                           _rng(depot, "analyse/bootstrap-parts-8B"))["intervalles"] == \
        lecture["juges"]["8B"]["intervalles"]
    # R12 : une seconde lecture n'écrase rien
    with pytest.raises(GardeArret, match="R12"):
        lp.analyser(depot, RUN, ANALYSE, d["taches"])


def _rng(depot, cle):
    from controle_ia.manifeste import generateur
    m = json.loads((depot / "runs" / ANALYSE / "manifeste.json").read_text(encoding="utf-8"))
    return generateur(m["graines"][cle])


def test_audit_trop_propre_sans_bruit_de_juge(depot, travail):
    """R4 : un juge sans bruit (A = B) déclenche l'audit « trop propre », et la lecture est suspendue."""
    _jusqu_a_l_analyse(depot, travail, bruit_juge=0.0)
    lecture = lp.analyser(depot, RUN, ANALYSE, depot / "taches.json")
    assert lecture["audit_r4"]["declenche"] and lecture["lecture_suspendue"]
    assert any("8B" in x for x in lecture["audit_r4"]["trop_propre"])


def test_cout_seul_retenu_n_est_pas_aucune_famille(depot, travail):
    """D-4 : « aucune famille retenue » compte le coût, comme le texte ; un étiqueteur au hasard ne retient aucune
    famille appariée, mais le coût est retenu (32 tâches à référence, coût lu partout)."""
    d = construire(depot, n=64)
    lp.preparer_etiquetage(depot, RUN, ANALYSE, d["prereg"], d["taches"], travail)
    committer(depot)
    _etiqueter(travail)
    lp.lire_etiquetage(depot, RUN, ANALYSE, d["taches"], travail)
    committer(depot)
    lecture = lp.analyser(depot, RUN, ANALYSE, d["taches"])
    assert lecture["retenue"]["controls"] in ("non retenue", "non concluant")
    assert lecture["predictions"]["P7"] in ("réfutée", "non concluant")
    assert lecture["retenue"]["cout"] == "retenue" and lecture["aucune_famille_retenue"] is False


# --- étiquetage : contrôles et tentatives ---------------------------------------------------------------------

def test_etiquetage_non_conforme_puis_refait(depot, travail):
    d = construire(depot)
    lp.preparer_etiquetage(depot, RUN, ANALYSE, d["prereg"], d["taches"], travail)
    committer(depot)
    with pytest.raises(GardeArret, match="à refaire"):                    # aucune étiquette
        lp.lire_etiquetage(depot, RUN, ANALYSE, d["taches"], travail)
    _etiqueter_selon_8b(depot, d, travail, inverser=0.0)
    lot1 = travail / ANALYSE / "lot-01" / "tentative-1"
    e = json.loads((lot1 / "etiquettes.json").read_text(encoding="utf-8"))
    e[next(iter(e))] = "Maybe"
    (lot1 / "etiquettes.json").write_text(json.dumps(e), encoding="utf-8")
    sortie = subprocess.run(["python3", "-I", "verifier_etiquettes.py"], cwd=lot1, capture_output=True, text=True)
    assert "Yes ou No" in sortie.stdout                                   # le script remis voit la même faute
    with pytest.raises(GardeArret, match="lot-01"):
        lp.lire_etiquetage(depot, RUN, ANALYSE, d["taches"], travail)
    with pytest.raises(GardeArret, match="rien à refaire"):
        lp.refaire_lot(depot, ANALYSE, travail, "lot-02")
    consigne = lp.refaire_lot(depot, ANALYSE, travail, "lot-01")
    assert consigne.endswith("lot-01/tentative-2/consigne.txt")
    lot2 = travail / ANALYSE / "lot-01" / "tentative-2"
    sha_lot1 = json.loads((depot / "diag" / ANALYSE / "echantillon-etiquetage.json").read_text(
        encoding="utf-8"))["resultat"]["empreintes_lots"]["lot-01"]
    (lot2 / "paires.json").write_text("[]\n", encoding="utf-8")         # artefact : paires modifiées
    (lot2 / "etiquettes.json").write_text("{}", encoding="utf-8")
    assert lp.lire_lot(lot2, sha_lot1)[1] == ["paires.json modifié"]
    lp.refaire_lot(depot, ANALYSE, travail, "lot-01")
    with pytest.raises(GardeArret, match="3 tentatives"):
        lp.refaire_lot(depot, ANALYSE, travail, "lot-01")
    lot3 = travail / ANALYSE / "lot-01" / "tentative-3"
    paires = json.loads((lot3 / "paires.json").read_text(encoding="utf-8"))
    (lot3 / "etiquettes.json").write_text(json.dumps({q["id"]: "No" for q in paires}), encoding="utf-8")
    sortie = subprocess.run(["python3", "-I", "verifier_etiquettes.py"], cwd=lot3, capture_output=True, text=True)
    assert sortie.stdout.strip() == "OK"
    assert lp.lire_etiquetage(depot, RUN, ANALYSE, d["taches"], travail)["tentatives"]["lot-01"] == 3
    (lot3 / "consigne.txt").write_text("autre consigne", encoding="utf-8")   # artefact : consigne modifiée
    assert "consigne.txt modifié" in lp.lire_lot(lot3, sha_lot1)[1]
    with pytest.raises(GardeArret, match="dans le dépôt"):                 # D-16 : jamais dans le dépôt
        lp.refaire_lot(depot, ANALYSE, depot / "w", "lot-01")


def test_consigne_d_etiquetage_suit_le_type_de_question():
    """D-7 : un contrôle inclus, même brièvement, est « Yes » ; une direction seulement mentionnée, ou prise comme base
    de comparaison, est « No » ; la consigne figée est comparée au manifeste par son empreinte."""
    c = lp.CONSIGNE_ETIQUETAGE
    assert "even briefly (for example in its list of controls)" in c
    assert "only mentions it, uses it as a baseline" in c
    assert lp.constantes()["CONSIGNE_ETIQUETAGE_SHA256"] == hashlib.sha256(c.encode("utf-8")).hexdigest()


# --- gardes ------------------------------------------------------------------------------------------------------

def test_gardes_de_lecture_cas_sain_et_artefacts(depot, travail):
    d = construire(depot)
    with pytest.raises(GardeArret, match="dans le dépôt"):                 # D-16 : dossier de travail dans le dépôt
        lp.preparer_etiquetage(depot, RUN, ANALYSE, d["prereg"], d["taches"], depot / "travail")
    # artefact : module de lecture modifié après le commit cité
    m = depot / lp.MODULES_LECTURE[1]
    m.write_text(m.read_text(encoding="utf-8") + "\n# modifié\n", encoding="utf-8")
    committer(depot)
    with pytest.raises(GardeArret, match="modules de lecture modifiés"):
        lp.preparer_etiquetage(depot, RUN, ANALYSE, d["prereg"], d["taches"], travail)
    assert not (depot / "runs" / ANALYSE).exists()
    subprocess.run(["git", "-C", str(depot), "revert", "--no-edit", "HEAD"], check=True, capture_output=True)
    # artefact : autre préenregistrement que celui du lancement
    autre = _prereg(depot, _commit(depot), nom="autre.md")
    committer(depot)
    with pytest.raises(GardeArret, match="pas été lancé sous ce préenregistrement"):
        lp.preparer_etiquetage(depot, RUN, ANALYSE, autre, d["taches"], travail)
    # artefact : fichier des tâches différent
    f = depot / "taches-autres.json"
    f.write_text(json.dumps({"taches": _taches(3, 0)}), encoding="utf-8")
    sceller(f)
    committer(depot)
    with pytest.raises(GardeArret, match="tâches .* ≠ tâches du pilote"):
        lp.preparer_etiquetage(depot, RUN, ANALYSE, d["prereg"], f, travail)
    # artefact : module de lecture absent
    (depot / lp.MODULES_LECTURE[0]).unlink()
    committer(depot)
    with pytest.raises(GardeArret, match="absents"):
        lp.preparer_etiquetage(depot, RUN, ANALYSE, d["prereg"], d["taches"], travail)
    assert not (depot / "runs" / ANALYSE).exists()


def test_modules_et_constantes_rejoues_a_chaque_etape(depot, travail, monkeypatch):
    """D-5 : un module de lecture modifié après la préparation (même non commité), ou des constantes changées, arrêtent
    `lire_etiquetage` et `analyser` ; le préenregistrement doit rester celui du manifeste d'analyse."""
    d = construire(depot)
    lp.preparer_etiquetage(depot, RUN, ANALYSE, d["prereg"], d["taches"], travail)
    committer(depot)
    _etiqueter_selon_8b(depot, d, travail, inverser=0.1)
    m = depot / lp.MODULES_LECTURE[1]
    sain = m.read_text(encoding="utf-8")
    m.write_text(sain.replace("seuil_part: float = 0.8", "seuil_part: float = 0.5"), encoding="utf-8")
    with pytest.raises(GardeArret, match="modules de lecture modifiés"):
        lp.lire_etiquetage(depot, RUN, ANALYSE, d["taches"], travail)
    m.write_text(sain, encoding="utf-8")
    lp.lire_etiquetage(depot, RUN, ANALYSE, d["taches"], travail)
    committer(depot)
    m.write_text(sain + "\n# modifié et commité après la préparation\n", encoding="utf-8")
    committer(depot)
    with pytest.raises(GardeArret, match="modules de lecture modifiés"):
        lp.analyser(depot, RUN, ANALYSE, d["taches"])
    subprocess.run(["git", "-C", str(depot), "revert", "--no-edit", "HEAD"], check=True, capture_output=True)
    monkeypatch.setattr(lp, "constantes", lambda: {"KAPPA_MIN": 0.5})
    with pytest.raises(GardeArret, match="constantes"):
        lp.analyser(depot, RUN, ANALYSE, d["taches"])
    monkeypatch.undo()
    monkeypatch.setattr(lp, "exiger_code_importe_sous", lambda racine: None)
    prereg = Path(d["prereg"])
    prereg.write_text(prereg.read_text(encoding="utf-8") + "\najout\n", encoding="utf-8")
    with pytest.raises(GardeArret, match="empreinte"):
        lp.analyser(depot, RUN, ANALYSE, d["taches"])


def test_garde_d_import_appelee_a_chaque_etape(depot, travail, monkeypatch):
    """D-5 : la garde d'import est appelée à chaque étape ; la vraie garde arrête dans un dépôt jetable (le code
    importé est celui du vrai dépôt)."""
    appels = []
    monkeypatch.setattr(lp, "exiger_code_importe_sous", appels.append)
    _jusqu_a_l_analyse(depot, travail)
    lp.analyser(depot, RUN, ANALYSE, depot / "taches.json")
    assert appels == [depot, depot, depot]
    monkeypatch.setattr(lp, "exiger_code_importe_sous", VRAIE_GARDE_D_IMPORT)
    with pytest.raises(GardeArret, match="code importé hors de la racine"):
        lp.exiger_modules_cites(depot, Path(depot / "prereg" / "prereg-pilote.md"))


def test_engagement_et_lots_recalcules(depot, travail, monkeypatch):
    """D-16 : à la lecture de l'étiquetage, les éléments recalculés depuis les graines doivent rendre l'engagement et
    les empreintes des lots scellés avant l'étiquetage (artefact : un élément changé)."""
    d = construire(depot)
    lp.preparer_etiquetage(depot, RUN, ANALYSE, d["prereg"], d["taches"], travail)
    committer(depot)
    _etiqueter_selon_8b(depot, d, travail, inverser=0.1)
    vrai = lp.echantillon_d_etiquetage

    def autre(paires, graines):
        elements, lots = vrai(paires, graines)
        elements[0] = dict(elements[0], poids=elements[0]["poids"] + 1)
        return elements, lots

    monkeypatch.setattr(lp, "echantillon_d_etiquetage", autre)
    with pytest.raises(GardeArret, match="engagement"):
        lp.lire_etiquetage(depot, RUN, ANALYSE, d["taches"], travail)
    assert not (depot / "diag" / ANALYSE / "etiquettes.json").exists()


@pytest.mark.parametrize("artefact, motif", [("B permuté", "désalignement"), ("C désaligné", "désalignement"),
                                             ("empreinte absente", "absente"),
                                             ("notation manquante", "manquantes"), ("doublon", "en double")])
def test_alignement_des_notations_cas_sain_et_artefacts(depot, artefact, motif):
    """D-1 : l'alignement des notations se contrôle mécaniquement, par l'empreinte de l'ensemble noté."""
    d = construire(depot, n=6)
    p = lp.charger_pilote(depot, RUN, d["taches"])
    ensembles = lp.empreintes_des_ensembles(p["episodes"]["fiches"])
    notations = p["notations"][("8B", "decisives")]
    taches = sorted(p["taches"])
    assert lp.notes_alignees(notations, "8B", taches, ensembles)["reponses_ABC"] == 18          # cas sain
    n = copy.deepcopy(notations)
    if artefact == "B permuté":
        b = [x for x in n if x["cle"].endswith("/e0/passe-1")]
        b[0]["ensemble_sha256"], b[1]["ensemble_sha256"] = b[1]["ensemble_sha256"], b[0]["ensemble_sha256"]
    elif artefact == "C désaligné":          # vérification 3, F-1 : les ensembles C de ce dépôt ont tous le même texte ;
        c = next(x for x in n if x["cle"].endswith("/e1/passe-0"))      # une C qui porte l'empreinte d'un autre ensemble
        c["ensemble_sha256"] = next(x["ensemble_sha256"] for x in n if x["ensemble_sha256"] != c["ensemble_sha256"])
    elif artefact == "empreinte absente":
        del n[0]["ensemble_sha256"]
    elif artefact == "notation manquante":
        n = n[1:]
    else:
        n.append(n[0])
    with pytest.raises(GardeArret, match=motif):
        lp.notes_alignees(n, "8B", taches, ensembles)


def test_configuration_hors_des_hypotheses_de_lecture(depot):
    """D-23 : les lettres A, B, C, D supposent 3 épisodes par tâche, e0 noté deux fois, e0 et e1 décisifs."""
    d = construire(depot, n=6, config=dict(CONFIG, episodes_decisifs=[0]))
    with pytest.raises(GardeArret, match="hypothèses de lecture"):
        lp.charger_pilote(depot, RUN, d["taches"])


def test_descriptifs_cle_absente_arrete(depot):
    """D-15 : une action de la garde absente des actions arrête, au lieu de compter 0."""
    d = construire(depot, n=6)
    p = lp.charger_pilote(depot, RUN, d["taches"])
    assert lp.descriptifs(p)["actions_comparees"] > 0                                           # cas sain
    p["episodes"]["fiches"][0]["equivalence"]["positions_capturees"] = {"0,9": 140}
    with pytest.raises(GardeArret, match="absente des actions"):
        lp.descriptifs(p)


# --- runs partiels (ordre du lanceur : décisives, appariement, descriptives) -----------------------------------

def test_run_partiel_pendant_les_notations_descriptives(depot, travail):
    """Arrêt pendant les notations de D : appariement écrit, familles lisibles (contre-lecture 2, D-6)."""
    _jusqu_a_l_analyse(depot, travail, etapes="descriptives")
    lecture = lp.analyser(depot, RUN, ANALYSE, depot / "taches.json")
    assert lecture["run_partiel"] and isinstance(lecture["familles"], dict)
    assert lecture["retenue"]["controls"] in ("retenue", "non retenue", "non concluant")


def test_run_partiel_pendant_l_appariement(depot, travail):
    d = construire(depot, etapes="appariement")
    r = lp.preparer_etiquetage(depot, RUN, ANALYSE, d["prereg"], d["taches"], travail)
    assert r["lots"] == {}
    committer(depot)
    lecture = lp.analyser(depot, RUN, ANALYSE, d["taches"])
    assert lecture["run_partiel"] and "nœud" in lecture["familles"]
    assert lecture["juges"]["8B"]["taches_completes"] == 50                 # décomposition lisible
    assert lecture["predictions"]["P4"] == "non concluant"


def test_run_partiel_pendant_les_notations_decisives_du_3B(depot, travail):
    """D-12 : le 8B est lu ; le 3B est en nœud ; P3 non concluant ; familles non lisibles."""
    d = construire(depot, etapes="3B")
    lp.preparer_etiquetage(depot, RUN, ANALYSE, d["prereg"], d["taches"], travail)
    committer(depot)
    lecture = lp.analyser(depot, RUN, ANALYSE, d["taches"])
    assert lecture["juges"]["8B"]["decomposition_concluante"] and lecture["juges"]["3B"]["plan_b"] == "nœud"
    assert lecture["predictions"]["P3"] == "non concluant" and "nœud" in lecture["familles"]


def test_run_partiel_pendant_les_episodes(depot, travail):
    d = construire(depot, etapes="aucune")
    lp.preparer_etiquetage(depot, RUN, ANALYSE, d["prereg"], d["taches"], travail)
    committer(depot)
    lecture = lp.analyser(depot, RUN, ANALYSE, d["taches"])
    assert lecture["run_partiel"] and "aucune lecture" in lecture["lecture"]


# --- une épreuve par garde d'arrêt restante (R5 ; relevé par traçage des lignes exécutées) -----------------------

def test_gardes_du_chargement_et_des_mesures(depot):
    d = construire(depot, n=6)
    p = lp.charger_pilote(depot, RUN, d["taches"])                                             # cas sain
    fiches, taches = p["episodes"]["fiches"], p["taches"]
    app, enonce = p["appariements"]["appariements"], p["appariements"]["enonce_seul"]
    with pytest.raises(GardeArret, match="paire d'appariement absente"):
        lp.couvertures(fiches, taches, app[1:])
    with pytest.raises(GardeArret, match="énoncé seul » absentes"):
        lp.base_enonce_seul(taches, enonce[1:])
    with pytest.raises(GardeArret, match="paires posées"):
        lp.paires_du_pilote(dict(p, appariements=dict(p["appariements"], appariements=app[1:])))
    sans_descriptifs = dict(p, episodes={k: v for k, v in p["episodes"].items() if k != "descriptifs"})
    with pytest.raises(GardeArret, match="clé « descriptifs » absente"):
        lp.descriptifs(sans_descriptifs)
    (depot / "diag" / RUN / "resume.json").unlink()                                             # artefact
    (depot / "diag" / RUN / "resume.json.sha256").unlink()
    with pytest.raises(GardeArret, match="ni résumé ni arrêt"):
        lp.charger_pilote(depot, RUN, d["taches"])


def test_garde_des_juges_du_pilote(depot):
    juges = [{"nom": "3B", "sert_a_l_appariement": False}, {"nom": "8B", "sert_a_l_appariement": True}]
    d = construire(depot, n=6, config=dict(CONFIG, juges=juges))
    with pytest.raises(GardeArret, match="deux juges attendus"):
        lp.charger_pilote(depot, RUN, d["taches"])


def test_gardes_du_preenregistrement_et_du_commit(depot, travail, tmp_path_factory, monkeypatch):
    d = construire(depot, n=6)
    sans_commit = depot / "prereg" / "sans-commit.md"
    sans_commit.write_text(f"- Entropie : `{ENTROPIE}`\n", encoding="utf-8")
    with pytest.raises(GardeArret, match="ne cite pas le commit"):
        lp.exiger_modules_cites(depot, sans_commit)
    faux = depot / "prereg" / "faux-commit.md"
    faux.write_text(f"- Commit du code d'analyse : `{'0' * 40}`\n", encoding="utf-8")
    with pytest.raises(GardeArret, match="impossible"):
        lp.exiger_modules_cites(depot, faux)
    with pytest.raises(GardeArret, match="a échoué"):
        lp._etat_courant(tmp_path_factory.mktemp("pas-un-depot"))
    sans_entropie = depot / "prereg" / "sans-entropie.md"
    sans_entropie.write_text(f"- Commit du code d'analyse : `{_commit(depot)}`\n", encoding="utf-8")
    committer(depot)
    with pytest.raises(GardeArret, match="ne cite pas l'entropie"):
        lp.preparer_etiquetage(depot, RUN, ANALYSE, sans_entropie, d["taches"], travail)
    assert not (depot / "runs" / ANALYSE).exists()


def test_gardes_du_manifeste_d_analyse(depot, travail, monkeypatch):
    d = construire(depot, n=6)
    lp.preparer_etiquetage(depot, RUN, ANALYSE, d["prereg"], d["taches"], travail)
    committer(depot)
    chemin_m, m, etat = lp._ouvrir_analyse(depot, ANALYSE)                                      # cas sain
    assert etat["commit_courant"] == _commit(depot) and etat["arbre_propre"] is True
    with pytest.raises(GardeArret, match="≠ run du manifeste"):
        lp.lire_etiquetage(depot, "20261010-120001-autre", ANALYSE, d["taches"], travail)
    with pytest.raises(GardeArret, match="≠ run du manifeste"):
        lp.analyser(depot, "20261010-120001-autre", ANALYSE, d["taches"])
    with pytest.raises(GardeArret, match="étiquetage non lu"):
        lp.analyser(depot, RUN, ANALYSE, d["taches"])
    vrai = lp.charger_pilote
    monkeypatch.setattr(lp, "charger_pilote", lambda *a: dict(vrai(*a), manifeste_sha256="0" * 64))
    for etape in (lambda: lp.lire_etiquetage(depot, RUN, ANALYSE, d["taches"], travail),
                  lambda: lp.analyser(depot, RUN, ANALYSE, d["taches"])):
        with pytest.raises(GardeArret, match="manifeste du pilote différent"):
            etape()
    monkeypatch.setattr(lp, "charger_pilote", vrai)
    monkeypatch.setattr(lp, "exiger_modules_cites", lambda racine, prereg: "f" * 40)
    with pytest.raises(GardeArret, match="commit cité ≠ commit du manifeste"):
        lp._ouvrir_analyse(depot, ANALYSE)
    monkeypatch.undo()
    monkeypatch.setattr(lp, "exiger_code_importe_sous", lambda racine: None)
    prereg = Path(d["prereg"])                                    # artefact : modifié puis scellé de nouveau
    prereg.write_text(prereg.read_text(encoding="utf-8") + "\najout\n", encoding="utf-8")
    (prereg.parent / (prereg.name + ".sha256")).unlink()
    sceller(prereg)
    with pytest.raises(GardeArret, match="préenregistrement différent"):
        lp._ouvrir_analyse(depot, ANALYSE)
    sans = "20261011-090001-t05-pilote-analyse"                   # artefact : manifeste sans préenregistrement
    creer_manifeste(depot, sans, {"x": 1}, ["x"], autoriser_depot_sale=True)
    with pytest.raises(GardeArret, match="sans préenregistrement"):
        lp._ouvrir_analyse(depot, sans)


def test_gardes_des_lots_et_des_etiquettes(depot, travail, monkeypatch):
    d = construire(depot, n=12)
    lp.preparer_etiquetage(depot, RUN, ANALYSE, d["prereg"], d["taches"], travail)
    committer(depot)
    with pytest.raises(GardeArret, match="lot-99 inconnu"):
        lp.refaire_lot(depot, ANALYSE, travail, "lot-99")
    _etiqueter_selon_8b(depot, d, travail, inverser=0.1)
    vrai = lp.echantillon_d_etiquetage

    def lots_changes(paires, graines):
        elements, lots = vrai(paires, graines)
        premier = sorted(lots)[0]
        lots[premier] = lots[premier][1:]
        return elements, lots

    monkeypatch.setattr(lp, "echantillon_d_etiquetage", lots_changes)
    with pytest.raises(GardeArret, match="lots recalculés"):
        lp.lire_etiquetage(depot, RUN, ANALYSE, d["taches"], travail)
    monkeypatch.setattr(lp, "echantillon_d_etiquetage", vrai)
    lire = lp.lire_lot
    monkeypatch.setattr(lp, "lire_lot", lambda dossier, sha: (
        (lambda e, m: ({k: v for k, v in list(e.items())[1:]} if e else e, m))(*lire(dossier, sha))))
    with pytest.raises(GardeArret, match="étiquettes ≠ éléments"):
        lp.lire_etiquetage(depot, RUN, ANALYSE, d["taches"], travail)
    monkeypatch.setattr(lp, "lire_lot", lire)
    t1 = travail / ANALYSE / "lot-01" / "tentative-1"              # artefact : paires de la tentative 1 modifiées
    paires = json.loads((t1 / "paires.json").read_text(encoding="utf-8"))
    paires[0]["question"] += " Really?"
    (t1 / "paires.json").write_text(json.dumps(paires), encoding="utf-8")
    with pytest.raises(GardeArret, match="paires de la première tentative modifiées"):
        lp.refaire_lot(depot, ANALYSE, travail, "lot-01")
