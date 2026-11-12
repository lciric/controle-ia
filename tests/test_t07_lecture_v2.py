"""Essais R5 du module de lecture de T0.7, v2 (`src/controle_ia/t07/lecture_v2.py`, `garde_adaptee_v1.py`, `journal_p3bis_v1.py` ;
brouillon 19, `07039ed2…`, section « Module », essais R5 des brouillons 15 à 17 et changements (x) à (xv) ; N-066, option 1), sur
le faux run de 7b de `tests/test_t07_lecture_v1.py` (repris tel quel : `construire_run`, `ajouter_lignes_b`, …), plus le journal
des ouvertures de P3-bis au format de P3-bis b8, le registre des préalables de P3-bis et les fichiers de décision du rendez-vous.

Chaque garde neuve : un cas sain et au moins un artefact. **Énumération (0 bis) du script `grille_l_t07_brouillon17.py` rejouée
par les gardes du module** (192 cas, cas par cas) ; **énumération (0) rejouée contre la garde v2 de l'étape B** (2 048 cas).
Aucune donnée réelle de 7a ; le seul fichier réel lu est le fichier léger des sondes figées de P3 (`701f73bd…`) et, s'il est
dans le dépôt, la liste `diag/20261019-230011-p3-reel/sondes-figees.json` (`fb418127…`), lue par `git show`."""
from __future__ import annotations

import importlib.util
import json
import os
import re
import subprocess
import sys
from itertools import product
from pathlib import Path

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.premier_test_ia.figees import ecrire_sondes, lire_sondes
from controle_ia.scellement import sceller
from controle_ia.sondes.familles import SondeLineaireJetons, SondePerceptron, mahalanobis
from controle_ia.t07 import garde_adaptee_v1 as ga
from controle_ia.t07 import journal_p3bis_v1 as jp
from controle_ia.t07 import lecture_v1 as lv1
from controle_ia.t07 import lecture_v2 as lv
from controle_ia.t07 import registre_v1 as rg
from test_t07_lecture_v1 import (APRES_A, AVANT, CONSIGNE_REL, D, INSTANT, INSTANT_B, MARQUES, NOMS, PLANCHERS_P3_REELS,
                                 RUN_T06, SHA_CONTROLE_T06, SHA_PLANCHERS_P3, _depot, _ecrits, _sans_ligne, audit_fuites,
                                 construire_run)

RACINE_DEPOT = Path(__file__).resolve().parents[1]
PIECES_17 = RACINE_DEPOT / "brouillons" / "T0.7-sondes-v0-v1-brouillon17-pieces"
SCRIPT_17 = PIECES_17 / "grille_l_t07_brouillon17.py"
SHA_SCRIPT_17 = "2a0eac56"
CONFIG_REELLE = RACINE_DEPOT / "brouillons" / "T0.7-sondes-v0-v1-brouillon19-pieces" / "configuration-t07-v1.json"
LISTE_P3 = "diag/20261019-230011-p3-reel/sondes-figees.json"
SHA_LISTE_P3 = "fb41812732711c1a"
ENTETE = "\n".join(jp.ENTETE_JOURNAL) + "\n"
FIN_A = INSTANT + 1                      # SCORES-T07 et SONDES-T07 datées de la fin (horloge réelle < INSTANT)


# --------------------------------------------------------------------------------------------------------------- outils
def construire(racine: Path, **kw):
    j = construire_run(racine, **kw)
    j.config.update(garde_adaptee=True, portee_regle_4="restreinte")
    return j


def _a(j, **kw):
    kw.setdefault("instant", INSTANT)
    return lv.etape_a(j.racine, j.registre, j.config, RUN_T06, **kw)


def _b(j, run_t07, **kw):
    kw.setdefault("instant", INSTANT_B)
    return lv.etape_b(j.racine, j.registre, j.config, RUN_T06, run_t07, **kw)


def lignes_audit(j, run_t07: str, instant: int = APRES_A, audit: dict | None = None) -> None:
    consigne = _depot(j.racine, CONSIGNE_REL, "# Consigne scellée de l'audit des fuites de T0.7\n")
    rel_a, sha_a = _depot(j.racine, f"diag/{run_t07}/{lv1.FICHIER_AUDIT}", json.dumps(audit or audit_fuites(consigne)) + "\n")
    rg.ajouter_ligne(j.registre, rg.CONSIGNE_AUDIT_FUITES_T07, instant - 20, *consigne)
    rg.ajouter_ligne(j.registre, rg.AUDIT_FUITES_T07, instant - 10, rel_a, sha_a)


def lignes_p3bis(j, instant: int, issue: str = "vu", prose: bool = True, prose_autre: bool = False, issue_brute: str | None = None) -> str:
    """`SCELLEMENT-P3BIS` et `VERDICT-P3BIS` datées `instant` ; fichier d'issue (ou texte brut `issue_brute`) ; verdict en prose
    écrit si `prose` (empreinte autre si `prose_autre`). Rend le chemin du verdict en prose."""
    _depot(j.racine, "prereg/P3-bis.md", "# P3-bis\n")
    rel_v = "docs/verdicts/verdict-P3-bis-v1.md"
    sha_v = "a" * 64
    if prose:
        rel_v, sha_v = _depot(j.racine, rel_v, f"# Verdict P3-bis : {issue}\n")
        if prose_autre:
            sha_v = "b" * 64
    texte = issue_brute if issue_brute is not None else json.dumps({"issue": issue, "ligne": 5, "verdict": rel_v, "verdict_sha256": sha_v})
    rel_i, _ = _depot(j.racine, "docs/verdicts/verdict-P3-bis-v1-issue.json", texte + "\n")
    rg.ajouter_ligne(j.registre, rg.SCELLEMENT_P3BIS, instant, "prereg/P3-bis.md", rg.sha256_de(j.racine / "prereg/P3-bis.md"))
    rg.ajouter_ligne(j.registre, rg.VERDICT_P3BIS, instant, rel_i, rg.sha256_de(j.racine / rel_i))
    return rel_v


def ligne_j(cle: str, instant: int, mode: str, appui: str = "-", paquets: str | None = None, motif: str | None = None) -> str:
    ouv = cle == jp.OUVERTURE_P3BIS
    paquets = paquets if paquets is not None else (f"{'c' * 64} {'d' * 64}" if ouv else "-")
    motif = motif if motif is not None else ("-" if ouv else "ligne-absente : essai")
    return f"| {cle} | {rg.date_utc(instant)} | {mode} | {appui} | {paquets} | {motif} |"


def ecrire_journal(j, lignes: list, entete: str = ENTETE) -> Path:
    p = j.racine / jp.JOURNAL_P3BIS
    p.write_text(entete + "".join(l + "\n" for l in lignes), encoding="utf-8")
    return p


def ajouter_journal(j, ligne: str) -> None:
    p = j.racine / jp.JOURNAL_P3BIS
    if not p.is_file():
        p.write_text(ENTETE, encoding="utf-8")
    with open(p, "a", encoding="utf-8") as f:
        f.write(ligne + "\n")


def decision(j, n: int, mot: str, instant: int) -> tuple[str, str]:
    return _depot(j.racine, jp.FICHIER_DECISION.format(n=n), f"# Rendez-vous de P3-bis, décision {n}\n\nDécision : {mot}\n"
                                                             f"Date : {rg.date_utc(instant)}\n")


def ecrire_prealables(j, garde: tuple | None, rendez_vous: list) -> dict:
    """`garde` : (instant, chemin, sha) ou None ; `rendez_vous` : [(instant, mot)] → fichiers de décision v1, v2… ; rend
    {"GA": sha, "RDV-n": sha}."""
    shas, lignes = {}, []
    if garde is not None:
        t, chemin, sha = garde
        lignes.append(rg.ecrire_ligne(jp.GARDE_ADAPTEE_T07_P3BIS, rg.date_utc(t), chemin, sha))
        shas["GA"] = sha
    for n, (t, mot) in enumerate(rendez_vous, start=1):
        rel, sha = decision(j, n, mot, t)
        lignes.append(rg.ecrire_ligne(f"RENDEZ-VOUS-P3BIS-{n}", rg.date_utc(t), rel, sha))
        shas[f"RDV-{n}"] = sha
    ec = _depot(j.racine, "prereg/T0.7-ecrit-perimetre.md", "# écrit (a)\n")
    lignes.insert(0, rg.ecrire_ligne("ECRIT-PERIMETRE-JEUX-P3BIS", AVANT, *ec))
    (j.racine / jp.PREALABLES_P3BIS).write_text("# Préalables de P3-bis\n\n" + "".join(l + "\n" for l in lignes), encoding="utf-8")
    return shas


def sha_t07(j) -> str:
    return j.pieces[rg.SCELLEMENT_T07][1]


def scenario_reduite(j, t_reduite: int = INSTANT - 100, t_rdv: int = INSTANT - 300, t_ga: int = INSTANT - 500,
                     mot: str = jp.OUVRIR, verdict: int | None = INSTANT - 50) -> dict:
    """Branche 1 de P3-bis : ligne de garde adaptée (texte scellé de T0.7), décision « ouvrir », ouverture réduite au journal,
    puis `VERDICT-P3BIS` (si `verdict`), tous avant l'ouverture de l'étape A par défaut."""
    shas = ecrire_prealables(j, (t_ga, jp.PREREG_T07, sha_t07(j)), [(t_rdv, mot)])
    ecrire_journal(j, [ligne_j(jp.OUVERTURE_P3BIS, t_reduite, jp.REDUITE,
                               f"RENDEZ-VOUS-P3BIS-1={shas['RDV-1']} {jp.GARDE_ADAPTEE_T07_P3BIS}={shas['GA']}")])
    if verdict is not None:
        lignes_p3bis(j, verdict)
    return shas


def appui_pleine(j) -> str:
    l = lv.lire_lignes_actuelles(j.registre, (rg.SCORES_T07, rg.SONDES_T07))
    return f"{rg.SCORES_T07}={l[rg.SCORES_T07]['sha256']} {rg.SONDES_T07}={l[rg.SONDES_T07]['sha256']}"


@pytest.fixture
def jouet(depot):
    return construire(depot)


# ---------------------------------------------------------------------------------------------------- chemin normal (v2)
def test_v2_chemin_normal_L2_sans_R14_couples_et_garde_ecrits(jouet):
    """Chemin sans ouverture anticipée (journal de P3-bis absent) : comportement du brouillon 14 (L2), R14 absente ; la garde adaptée
    est écrite (journal absent, fermeture = ouverture en cours) ; couples figés notés et lus en descriptif."""
    ra = _a(jouet)
    lignes_audit(jouet, ra["run_t07"])
    lignes_p3bis(jouet, APRES_A)
    lec = _b(jouet, ra["run_t07"])
    assert lec["issue_critere_3"] == "L2"
    assert not any(r.startswith("R14") for r in lec["reserves"]) and lec["garde_adaptee"]["r14"] is None
    assert lec["garde_adaptee"]["suite"] is None and lec["garde_adaptee"]["lancement_a_ouverture_reduite"] is False
    sondes = json.loads((jouet.racine / "diag" / ra["run_t07"] / "sondes-t07.json").read_text())["resultat"]
    assert sondes["garde_adaptee"]["fermeture_perimetre"]["source"] == "ouverture en cours de l'étape A"
    assert sondes["garde_adaptee"]["ouverture_reduite_avant_ouverture_A"] is None
    assert [c["nom"] for c in sondes["couples_figes"]["couples"]] == NOMS[:2] and sondes["couples_figes"]["mahalanobis"] == 0
    assert set(lec["couples_figes_descriptif"]) == set(NOMS[:2])
    assert all("aire" in v for c in lec["couples_figes_descriptif"].values() for v in c.values())
    m = json.loads((jouet.racine / "runs" / ra["run_t07"] / "manifeste.json").read_text())
    assert m["config"]["garde_adaptee"] is True and m["config"]["portee_regle_4"] == "restreinte"
    assert "garde_adaptee_etape_a" in m["config"]


# ---------------------------------------------------------------------------------------------------------- configuration
def test_configuration_garde_adaptee_et_portee_regle_4(jouet):
    """(xiii), G6 : clés toujours présentes ; absente → `CleAbsente` ; autre valeur → arrêt de configuration (cas sain : true,
    « restreinte »)."""
    lv.exiger_configuration(jouet.config)
    for k in ("garde_adaptee", "portee_regle_4"):
        c = {x: v for x, v in jouet.config.items() if x != k}
        with pytest.raises(lv.CleAbsente, match=k):
            lv.exiger_configuration(c)
    for k, v in (("garde_adaptee", False), ("garde_adaptee", "vrai"), ("garde_adaptee", 1), ("portee_regle_4", "stricte"),
                 ("portee_regle_4", None)):
        with pytest.raises(GardeArret, match=f"{k} = .*arrêt de configuration"):
            lv.exiger_configuration({**jouet.config, k: v})
    with pytest.raises(lv.CleAbsente):                       # la v1 ne connaît pas ces clés : la v2 les exige
        lv.exiger_configuration({x: v for x, v in jouet.config.items() if x not in ("garde_adaptee", "portee_regle_4")})


def test_configuration_fichier_complet_refuse_et_mode_reel(jouet):
    """(xii), M-1 : fichier complet `91b61c45…` (ou nommé `sondes-figees.npz`) dans `fichiers_sondes` ou `planchers_p3` → arrêt de
    configuration, tout mode ; mode réel : `fichiers_sondes` = [le seul fichier léger], principales de P3, sondes neuves nulles."""
    c = jouet.config
    for f in ({"chemin": "donnees/x/sondes-figees.npz", "sha256": "1" * 64}, {"chemin": "donnees/x/autre.npz", "sha256": lv.SHA_FICHIER_COMPLET}):
        with pytest.raises(GardeArret, match="fichier complet .*arrêt de configuration"):
            lv.exiger_configuration({**c, "fichiers_sondes": c["fichiers_sondes"] + [f]})
        with pytest.raises(GardeArret, match="fichier complet"):
            lv.exiger_configuration({**c, "planchers_p3": f})
    leger = {"chemin": "donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz", "sha256": lv.SHA_FICHIER_LEGER}
    reel = {**c, "mode": "reel", "n_plancher": 200, "preenregistrement": "prereg/T0.7-sondes-v0-v1.md", "fichiers_sondes": [leger],
            "planchers_p3": leger, "sondes_par_concept": {**lv.PRINCIPALES_P3, "dissimulation": None, "domaine": None},
            "jetons_entrainement": None}
    lv.exiger_configuration(reel)                                                       # cas sain
    for faute, motif in (({"fichiers_sondes": [leger, c["fichiers_sondes"][0]]}, "seul fichier léger"),
                         ({"fichiers_sondes": c["fichiers_sondes"]}, "seul fichier léger"),
                         ({"planchers_p3": c["planchers_p3"]}, "seul fichier léger"),
                         ({"sondes_par_concept": {**reel["sondes_par_concept"], "tromperie": "tromperie-lineaire-c15"}}, "principale de P3"),
                         ({"sondes_par_concept": {**reel["sondes_par_concept"], "domaine": "domaine-lineaire-c7"},
                           "jetons_entrainement": c["jetons_entrainement"]}, "sondes neuves")):
        with pytest.raises(GardeArret, match=motif):
            lv.exiger_configuration({**reel, **faute})
    with pytest.raises(GardeArret, match="nom de sonde attendu"):
        lv.exiger_configuration({**reel, "sondes_par_concept": {**reel["sondes_par_concept"], "tromperie": None}})


def test_configuration_reelle_du_brouillon_19():
    """La configuration écrite pour le brouillon 19 (brouillon de configuration : `entropie` nulle jusqu'au candidat, R9) passe tous
    les contrôles du module sauf celui de l'entropie (artefact : entropie nulle → arrêt de configuration) ; entropie tirée → passe ;
    son empreinte canonique est calculée par le module (`empreinte_canonique`)."""
    if not CONFIG_REELLE.is_file():
        pytest.skip("configuration du brouillon 19 absente de ce clone")
    config = json.loads(CONFIG_REELLE.read_text(encoding="utf-8"))
    assert set(config) == set(lv.CLES_CONFIG)
    with pytest.raises(GardeArret, match="entropie = None"):
        lv.exiger_configuration(config)
    lv.exiger_configuration({**config, "entropie": 2 ** 100})
    assert config["mode"] == "reel" and config["garde_adaptee"] is True and config["portee_regle_4"] == "restreinte"
    assert config["controle_aire"] == "egalite" and config["scores_base_t06"] is None and config["niveau_base_t06"] == 0.95
    assert config["marques_autres_taches"] == ["T06", "T08", "P3BIS", "NARC"] and config["p064"] is True
    assert config["fichiers_sondes"] == [config["planchers_p3"]] and config["planchers_p3"]["sha256"] == lv.SHA_FICHIER_LEGER
    import hashlib
    from controle_ia.manifeste import config_canonique
    assert lv.empreinte_canonique(config) == hashlib.sha256(config_canonique(config)).hexdigest()


def test_reel_sonde_neuve_dans_le_perimetre_refus_ecart_declare(jouet):
    """Écart texte / code déclaré : une sonde neuve nulle (mode réel) dont le jeu est scellé → refus de l'étape A, code 2, motif
    écrit, rien écrit (cas sain : sans le jeu, l'étape A ouvre sur les deux sondes figées)."""
    jouet.config["sondes_par_concept"] = {**jouet.config["sondes_par_concept"], "dissimulation": None}
    avant = _ecrits(jouet)
    with pytest.raises(rg.RefusRegistre, match="dissimulation .*non mis en œuvre par le module v2"):
        _a(jouet)
    assert _ecrits(jouet) == avant
    _sans_ligne(jouet, rg.SCELLEMENT_JEUX_JD)
    ra = _a(jouet)
    assert ra["index"]["sondes_lues"] == [NOMS[0], NOMS[1], NOMS[3]]


# --------------------------------------------------------------------------------------------------- (x) et G5 : périmètre
def test_x_relance_apres_R11_jeu_inscrit_entre_les_tentatives_hors_de_sondes_lues(jouet, monkeypatch):
    """(x) : relance de l'étape A après R11-arret avec une ligne `SCELLEMENT-JEUX-T07-JC` inscrite entre les deux tentatives →
    `sondes_lues` inchangée (cas sain) ; la règle de la v1 (lignes présentes à l'ouverture en cours) l'aurait prise (artefact)."""
    _sans_ligne(jouet, rg.SCELLEMENT_JEUX_JC)
    reel = lv1.garde_identite

    def r11(*a, **k):
        raise GardeArret("R11-arret : garde d'identité en échec (essai)")
    monkeypatch.setattr(lv1, "garde_identite", r11)
    with pytest.raises(lv.ArretApresManifeste, match="R11-arret"):
        _a(jouet)
    monkeypatch.setattr(lv1, "garde_identite", reel)
    rg.ajouter_ligne(jouet.registre, rg.SCELLEMENT_JEUX_JC, INSTANT + 30, *_depot(jouet.racine, "prereg/jeux/J-C.jsonl", "{}\n"))
    ra = _a(jouet, instant=INSTANT + 60)
    assert ra["index"]["sondes_lues"] == NOMS[:3]
    s = json.loads((jouet.racine / "diag" / ra["run_t07"] / "sondes-t07.json").read_text())["resultat"]
    assert s["jeux_hors_perimetre"] == [rg.SCELLEMENT_JEUX_JC] and s["jeux_scelles"]["J-C"] is False
    assert s["garde_adaptee"]["fermeture_perimetre"] == {"instant": rg.date_utc(INSTANT), "source": "première ouverture de l'étape A de ce run",
                                                         "premiere_ouverture_A": rg.date_utc(INSTANT)}
    presentes = lv.lire_lignes_actuelles(jouet.registre, (rg.SCELLEMENT_JEUX_JD, rg.SCELLEMENT_JEUX_JC, rg.SCELLEMENT_JEUX_JA))
    assert lv1.sondes_lues_depuis_lignes(presentes, jouet.config)["sondes_lues"] == NOMS     # artefact : la v1 prendrait J-C


def test_G5_jeu_inscrit_apres_l_ouverture_reduite_hors_de_sondes_lues(depot):
    """G5 : ligne `SCELLEMENT-JEUX-T07-JC` inscrite entre l'ouverture réduite et l'ouverture de l'étape A → hors de `sondes_lues`
    (artefact refusé de la lire) ; cas sain : inscrite avant l'ouverture réduite → lue."""
    for t_jc, lue in ((INSTANT - 50, False), (INSTANT - 200, True)):
        racine = depot / f"jc{t_jc}"
        racine.mkdir()
        j = construire(racine, avec_jc=False)
        scenario_reduite(j, t_reduite=INSTANT - 100, verdict=None)
        rg.ajouter_ligne(j.registre, rg.SCELLEMENT_JEUX_JC, t_jc, *_depot(j.racine, "prereg/jeux/J-C.jsonl", "{}\n"))
        ra = _a(j)
        assert (NOMS[3] in ra["index"]["sondes_lues"]) is lue
        s = json.loads((j.racine / "diag" / ra["run_t07"] / "sondes-t07.json").read_text())["resultat"]
        assert s["garde_adaptee"]["fermeture_perimetre"]["source"] == "première ligne OUVERTURE-P3BIS du journal de P3-bis"
        assert s["garde_adaptee"]["ouverture_reduite_avant_ouverture_A"]["date"] == rg.date_utc(INSTANT - 100)
        assert s["jeux_hors_perimetre"] == ([] if lue else [rg.SCELLEMENT_JEUX_JC])


def test_G5_refus_ouverture_p3bis_ne_ferme_pas_le_perimetre(depot):
    """G5 : une ligne `REFUS-OUVERTURE-P3BIS` ne compte jamais : J-C inscrite après elle reste lue."""
    j = construire(depot, avec_jc=False)
    ecrire_journal(j, [ligne_j(jp.REFUS_OUVERTURE_P3BIS, INSTANT - 100, jp.PLEINE)])
    rg.ajouter_ligne(j.registre, rg.SCELLEMENT_JEUX_JC, INSTANT - 50, *_depot(j.racine, "prereg/jeux/J-C.jsonl", "{}\n"))
    assert NOMS[3] in _a(j)["index"]["sondes_lues"]


# ------------------------------------------------------------------------------------------------------------ G1 et G2 (étape A)
def _refus_a(j, motif: str):
    avant = _ecrits(j)
    with pytest.raises(rg.RefusRegistre, match=motif) as e:
        _a(j)
    assert _ecrits(j) == avant and j.lignes_journal()[-1].startswith("| REFUS-T07 |")
    assert not any(l.startswith("| OUVERTURE-T07 |") for l in j.lignes_journal())
    return str(e.value)


def test_G2_cas_sain_verdict_admis_reduite_valable_issue_non_lue(jouet, monkeypatch):
    """G2 : `VERDICT-P3BIS` présente à l'ouverture de l'étape A, ouverture réduite au journal, dernière ligne de rendez-vous
    « ouvrir », ligne de garde adaptée citant le texte scellé → ouverture ; le fichier d'issue n'est **jamais** lu à l'étape A
    (artefact : fichier d'issue non JSON, et `lire_issue_p3bis` espionnée) ; réduite écrite dans le manifeste et `sondes-t07.json`."""
    scenario_reduite(jouet, verdict=None)
    lignes_p3bis(jouet, INSTANT - 50, issue_brute="ceci n'est pas du JSON : l'étape A ne le lit pas")
    lus = []
    monkeypatch.setattr(lv1, "lire_issue_p3bis", lambda *a, **k: lus.append(a) or {"P": "vu"})
    ra = _a(jouet)
    assert not lus
    s = json.loads((jouet.racine / "diag" / ra["run_t07"] / "sondes-t07.json").read_text())["resultat"]
    assert s["garde_adaptee"]["verdict_p3bis_a_l_ouverture"]["admise"].startswith("G2")
    m = json.loads((jouet.racine / "runs" / ra["run_t07"] / "manifeste.json").read_text())["config"]["garde_adaptee_etape_a"]
    assert m["ouverture_reduite_avant_ouverture_A"] == {"date": rg.date_utc(INSTANT - 100), "numero": 3, "instant": INSTANT - 100}
    assert rg.cle_presente(jouet.registre, rg.SCORES_T07)


def test_G1_verdict_anterieur_au_scellement_refus_A_et_B(depot):
    """G1 : `VERDICT-P3BIS` antérieure à `SCELLEMENT-T07` → refus des étapes A et B, nœud (cas sain : postérieure, essai G2)."""
    j = construire(depot)
    scenario_reduite(j, t_reduite=INSTANT - 100, verdict=None)
    lignes_p3bis(j, rg.instant_utc(AVANT) - 100)
    m = _refus_a(j, "G1 : VERDICT-P3BIS .* pas strictement postérieure à SCELLEMENT-T07")
    assert "[nœud]" in m
    codes = ga.garde_etape_b({rg.SCELLEMENT_T07: {"instant": 10, "sha256": "1" * 64}, rg.VERDICT_P3BIS: {"instant": 5, "sha256": "2" * 64},
                              rg.SCORES_T07: {"instant": 1, "sha256": "3" * 64}, rg.SONDES_T07: {"instant": 1, "sha256": "4" * 64}}, [])
    assert ga.SCELLEMENT_APRES_VERDICT in [c for c, _ in codes]


def test_G1_m4_garde_adaptee_presente_scellement_absent_refus_sans_comparaison(jouet):
    """m-4 : ligne `GARDE-ADAPTEE-T07-P3BIS` présente mais `SCELLEMENT-T07` absente → refus par G1, sans comparaison d'empreinte."""
    scenario_reduite(jouet)
    _sans_ligne(jouet, rg.SCELLEMENT_T07)
    m = _refus_a(jouet, "G1 : VERDICT-P3BIS présente et SCELLEMENT-T07 absente")
    assert "à l'empreinte de SCELLEMENT-T07" not in m and "aucune comparaison d'empreinte" in m


@pytest.mark.parametrize("cas, motif", [
    ("journal-absent", "G2 : .*sans ouverture réduite .*décision ouvrir, mais aucune ouverture réduite"),
    ("refus-seulement", "G2 : .*sans ouverture réduite"),
    ("maintenir", "décision maintenir : aucune ouverture réduite permise"),
    ("ouvrir-pleinement", r"ouverture pleine anticipée décidée \(ouvrir pleinement\) : T0.7 ne lit plus 7b"),
    ("decision-absente", "G2 : .*décision absente"),
    ("v2-ouvrir-ligne-maintenir", "décision maintenir"),
    ("garde-absente", "GARDE-ADAPTEE-T07-P3BIS absente"),
    ("garde-autre-empreinte", "empreinte de GARDE-ADAPTEE-T07-P3BIS dans l'appui|pas le texte scellé"),
    ("garde-apres-decision", "ne précède pas la décision"),
    ("pleine-avant-A", "ouverture pleine .* avant l'ouverture de l'étape A"),
    ("appui-autre-rendez-vous", "la dernière ligne de rendez-vous à cette date est RENDEZ-VOUS-P3BIS-2"),
    ("appui-autre-empreinte", "empreinte de RENDEZ-VOUS-P3BIS-1 dans l'appui"),
])
def test_G2_artefacts_refus_noeud(depot, cas, motif):
    """G2 : chaque artefact → refus de l'étape A, code 2, une ligne `REFUS-T07`, rien d'écrit, motif nommé (nœud)."""
    j = construire(depot)
    t_ga, t_rdv, t_red = INSTANT - 500, INSTANT - 300, INSTANT - 100
    ga_ok = (t_ga, jp.PREREG_T07, sha_t07(j))
    appui = lambda s, n=1: f"RENDEZ-VOUS-P3BIS-{n}={s[f'RDV-{n}']} {jp.GARDE_ADAPTEE_T07_P3BIS}={s['GA']}"
    if cas == "journal-absent":
        ecrire_prealables(j, ga_ok, [(t_rdv, jp.OUVRIR)])
    elif cas == "refus-seulement":
        ecrire_prealables(j, ga_ok, [(t_rdv, jp.OUVRIR)])
        ecrire_journal(j, [ligne_j(jp.REFUS_OUVERTURE_P3BIS, t_red, jp.REDUITE, motif="garde-adaptee-absente : essai")])
    elif cas in ("maintenir", "ouvrir-pleinement"):
        ecrire_prealables(j, ga_ok, [(t_rdv, jp.MAINTENIR if cas == "maintenir" else jp.OUVRIR_PLEINEMENT)])
    elif cas == "decision-absente":
        ecrire_prealables(j, ga_ok, [])
    elif cas == "v2-ouvrir-ligne-maintenir":
        ecrire_prealables(j, ga_ok, [(t_rdv, jp.MAINTENIR)])
        decision(j, 2, jp.OUVRIR, t_rdv + 10)                      # fichier « ouvrir » jamais cité par une ligne : jamais lu
    elif cas == "garde-absente":
        s = ecrire_prealables(j, None, [(t_rdv, jp.OUVRIR)])
        ecrire_journal(j, [ligne_j(jp.OUVERTURE_P3BIS, t_red, jp.REDUITE, f"RENDEZ-VOUS-P3BIS-1={s['RDV-1']} {jp.GARDE_ADAPTEE_T07_P3BIS}={'e' * 64}")])
    elif cas == "garde-autre-empreinte":
        autre = _depot(j.racine, "prereg/T0.7-autre.md", "# autre texte\n")
        s = ecrire_prealables(j, (t_ga, *autre), [(t_rdv, jp.OUVRIR)])
        ecrire_journal(j, [ligne_j(jp.OUVERTURE_P3BIS, t_red, jp.REDUITE, appui(s))])
    elif cas == "garde-apres-decision":
        s = ecrire_prealables(j, (t_rdv + 10, jp.PREREG_T07, sha_t07(j)), [(t_rdv, jp.OUVRIR)])
        ecrire_journal(j, [ligne_j(jp.OUVERTURE_P3BIS, t_red, jp.REDUITE, appui(s))])
    elif cas == "pleine-avant-A":
        ecrire_journal(j, [ligne_j(jp.OUVERTURE_P3BIS, t_red, jp.PLEINE, f"{rg.SCORES_T07}={'1' * 64} {rg.SONDES_T07}={'2' * 64}")])
    elif cas == "appui-autre-rendez-vous":
        s = ecrire_prealables(j, ga_ok, [(t_rdv, jp.MAINTENIR), (t_rdv + 50, jp.OUVRIR)])
        ecrire_journal(j, [ligne_j(jp.OUVERTURE_P3BIS, t_red, jp.REDUITE, appui(s, 1))])
    elif cas == "appui-autre-empreinte":
        s = ecrire_prealables(j, ga_ok, [(t_rdv, jp.OUVRIR)])
        ecrire_journal(j, [ligne_j(jp.OUVERTURE_P3BIS, t_red, jp.REDUITE, f"RENDEZ-VOUS-P3BIS-1={'9' * 64} {jp.GARDE_ADAPTEE_T07_P3BIS}={s['GA']}")])
    if cas != "pleine-avant-A":
        lignes_p3bis(j, INSTANT - 50)
    m = _refus_a(j, motif)
    assert "[nœud]" in m
    if cas == "ouvrir-pleinement":
        assert ga.MOTIF_DECISION_ABSENTE not in m


def test_G2_chemin_sans_ouverture_anticipee_comportement_du_brouillon_14(jouet):
    """Journal absent et `VERDICT-P3BIS` absente → comportement du brouillon 14 (cas sain) ; `VERDICT-P3BIS` présente, journal et
    préalables absents → refus (le registre des préalables est exigé pour juger G2)."""
    _a(jouet)
    (jouet.racine / "x").mkdir()
    j2 = construire(jouet.racine / "x")
    lignes_p3bis(j2, INSTANT - 50)
    _refus_a(j2, "registre des préalables de P3-bis .* absent")


def test_G2_ouverture_pleine_ou_anticipee_pendant_l_etape_A_noeud(depot, monkeypatch):
    """Ligne de mode `pleine` (ou `pleine-anticipee`) entre l'ouverture et la fin de l'étape A → nœud : arrêt après le manifeste,
    `SCORES-T07` et `SONDES-T07` non écrites ; une ouverture réduite pendant l'étape A, elle, est écrite dans `notation-t07.json`."""
    original = lv.noter
    for n, mode in enumerate((jp.PLEINE, jp.PLEINE_ANTICIPEE, jp.REDUITE)):
        racine = depot / f"c{n}"
        racine.mkdir()
        j = construire(racine)
        s = ecrire_prealables(j, (INSTANT - 500, jp.PREREG_T07, sha_t07(j)), [(INSTANT - 300, jp.OUVRIR)])
        appui = (f"{rg.SCORES_T07}={'1' * 64} {rg.SONDES_T07}={'2' * 64}" if mode == jp.PLEINE else
                 f"RENDEZ-VOUS-P3BIS-1={s['RDV-1']}" if mode == jp.PLEINE_ANTICIPEE else
                 f"RENDEZ-VOUS-P3BIS-1={s['RDV-1']} {jp.GARDE_ADAPTEE_T07_P3BIS}={s['GA']}")

        def noter_puis_ouverture(*a, _appui=appui, _mode=mode, _j=j, **k):
            r = original(*a, **k)
            ajouter_journal(_j, ligne_j(jp.OUVERTURE_P3BIS, INSTANT, _mode, _appui))
            return r
        monkeypatch.setattr(lv, "noter", noter_puis_ouverture)
        if mode == jp.REDUITE:
            ra = _a(j, horloge=lambda: INSTANT + 5)
            notation = json.loads((j.racine / "diag" / ra["run_t07"] / "notation-t07.json").read_text())["resultat"]
            assert notation["garde_adaptee_fin_A"]["ouverture_reduite_avant_fin_A"]["date"] == rg.date_utc(INSTANT)
            assert rg.cle_presente(j.registre, rg.SCORES_T07)
        else:
            with pytest.raises(lv.ArretApresManifeste, match="nœud"):
                _a(j, horloge=lambda: INSTANT + 5)
            assert not rg.cle_presente(j.registre, rg.SCORES_T07) and not rg.cle_presente(j.registre, rg.SONDES_T07)
            assert list((j.racine / "diag").glob("*-t07-*/arret.json"))


def test_verdict_pendant_A_sans_reduite_noeud_du_brouillon_14(jouet, monkeypatch):
    """Chemin sans ouverture anticipée : `VERDICT-P3BIS` inscrite pendant l'étape A, sans ouverture réduite → nœud (règle gardée)."""
    original = lv.noter

    def noter_puis_verdict(*a, **k):
        r = original(*a, **k)
        lignes_p3bis(jouet, INSTANT + 2)
        return r
    monkeypatch.setattr(lv, "noter", noter_puis_verdict)
    with pytest.raises(lv.ArretApresManifeste, match="VERDICT-P3BIS inscrite pendant l'étape A sans ouverture réduite"):
        _a(jouet, horloge=lambda: INSTANT + 5)
    assert not rg.cle_presente(jouet.registre, rg.SCORES_T07)


def test_pleine_anticipee_avant_l_ouverture_refus_noeud(jouet):
    """Ligne `pleine-anticipee` avant l'ouverture de l'étape A → refus, nœud (toute date)."""
    s = ecrire_prealables(jouet, None, [(INSTANT - 300, jp.OUVRIR_PLEINEMENT)])
    ecrire_journal(jouet, [ligne_j(jp.OUVERTURE_P3BIS, INSTANT - 100, jp.PLEINE_ANTICIPEE, f"RENDEZ-VOUS-P3BIS-1={s['RDV-1']}")])
    assert "[nœud]" in _refus_a(jouet, "pleine-anticipee")


# ------------------------------------------------------------------------------------------------------------ G3, G4, R14 (étape B)
def _lancement_reduit(j, pleine: bool = True, prose: bool = True, prose_autre: bool = False, appui: str | None = None) -> str:
    """Lancement à ouverture réduite : branche 1 (réduite, puis `VERDICT-P3BIS` avant l'étape A), étape A, audit ; ligne `pleine`
    après `SCORES-T07` et `SONDES-T07` si `pleine`. Rend RUN_T07."""
    scenario_reduite(j, verdict=None)
    lignes_p3bis(j, INSTANT - 50, prose=prose, prose_autre=prose_autre)
    ra = _a(j)
    lignes_audit(j, ra["run_t07"])
    if pleine:
        ajouter_journal(j, ligne_j(jp.OUVERTURE_P3BIS, APRES_A, jp.PLEINE, appui if appui is not None else appui_pleine(j)))
    return ra["run_t07"]


def _refus_b(j, run7: str, motif: str) -> str:
    avant = _ecrits(j, run7)
    with pytest.raises(rg.RefusRegistre, match=motif) as e:
        _b(j, run7)
    assert _ecrits(j, run7) == avant and j.lignes_journal()[-1].startswith("| REFUS-T07 |")
    assert not (j.racine / "diag" / run7 / lv1.FICHIER_LECTURE).exists()
    return str(e.value)


def test_G3_cas_sain_reduite_puis_pleine_R14_ecrite(jouet):
    """G3 : lancement à ouverture réduite, ouverture pleine après `SCORES-T07` et `SONDES-T07`, verdict en prose présent et
    d'empreinte égale → étape B (L2) ; R14 écrite dans `resultat.reserves` (date et ligne du journal), sans effet sur la ligne."""
    run7 = _lancement_reduit(jouet)
    lec = _b(jouet, run7)
    assert lec["issue_critere_3"] == "L2" and lec["p3bis"]["P"] == "vu"
    r14 = [r for r in lec["reserves"] if r.startswith("R14 : ")]
    assert len(r14) == 1 and rg.date_utc(INSTANT - 100) in r14[0] and "ligne 3 du journal" in r14[0]
    assert lec["garde_adaptee"]["lancement_a_ouverture_reduite"] is True and lec["garde_adaptee"]["suite"] is None


def test_G3_verdict_en_prose_absent_refus_attente_sans_L0a_puis_relance(jouet):
    """G3 : verdict en prose absent → refus, code 2, attente, **sans** L0a (artefact : `lecture-t07.json` écrit → échec) ; une fois
    le verdict en prose écrit, l'étape B rejouée sur le même run lit."""
    run7 = _lancement_reduit(jouet, prose=False)
    m = _refus_b(jouet, run7, "verdict en prose .* absent : attente")
    assert "attente" in m and "L0a" in m                       # le motif dit « jamais L0a »
    _depot(jouet.racine, "docs/verdicts/verdict-P3-bis-v1.md", "# Verdict P3-bis : vu\n")
    doc = json.loads((jouet.racine / "docs/verdicts/verdict-P3-bis-v1-issue.json").read_text())
    assert doc["verdict_sha256"] == "a" * 64                   # engagement d'une autre prose : L0a à la relance
    lec = _b(jouet, run7, instant=INSTANT_B + 10)
    assert lec["issue_critere_3"] == "L0a" and lec["p3bis"]["P"] == "illisible"


def test_G3_verdict_en_prose_d_empreinte_autre_L0a(jouet):
    """G3 : verdict en prose présent mais d'empreinte autre que `verdict_sha256` → P « illisible », L0a (comme sur le chemin normal)."""
    run7 = _lancement_reduit(jouet, prose_autre=True)
    lec = _b(jouet, run7)
    assert lec["issue_critere_3"] == "L0a" and not lec["scores_ouverts"]


@pytest.mark.parametrize("cas, motif, nature", [
    ("pleine-absente", "pas encore écrite : attente", "attente"),
    ("pleine-appui-faux", "appui .* ≠ « SCORES-T07=… SONDES-T07=… »", "nœud"),
    ("anticipee-apres-scores", "pleine-anticipee", "nœud"),
    ("refus-pleine-apres-scores", "pas encore écrite : attente", "attente"),
    ("pleine-avant-fin-A", "pas strictement après SCORES-T07 et SONDES-T07", "nœud"),
])
def test_G3_artefacts_etape_B(depot, cas, motif, nature):
    """G3 et brouillon 17 (M-1, M-2) : ligne `pleine` pas encore écrite → attente ; appui faux → refus ; `pleine-anticipee` après
    `SCORES-T07` sur un lancement réduit → étape B refusée, nœud (jamais prise pour l'ouverture pleine) ; `REFUS-OUVERTURE-P3BIS` de
    mode `pleine` → jamais une ouverture : attente ; ligne `pleine` datée de la fin de l'étape A → nœud."""
    j = construire(depot)
    run7 = _lancement_reduit(j, pleine=False)
    s = {"RDV-1": jp.lire_prealables(j.racine / jp.PREALABLES_P3BIS, j.racine, INSTANT_B)["rendez_vous"][0]["sha256"]}
    if cas == "pleine-appui-faux":
        ajouter_journal(j, ligne_j(jp.OUVERTURE_P3BIS, APRES_A, jp.PLEINE, f"{rg.SCORES_T07}={'1' * 64} {rg.SONDES_T07}={'2' * 64}"))
    elif cas == "anticipee-apres-scores":
        ajouter_journal(j, ligne_j(jp.OUVERTURE_P3BIS, APRES_A, jp.PLEINE_ANTICIPEE, f"RENDEZ-VOUS-P3BIS-1={s['RDV-1']}"))
    elif cas == "refus-pleine-apres-scores":
        ajouter_journal(j, ligne_j(jp.REFUS_OUVERTURE_P3BIS, APRES_A, jp.PLEINE, appui_pleine(j), motif="paquet-faux : essai"))
    elif cas == "pleine-avant-fin-A":
        ajouter_journal(j, ligne_j(jp.OUVERTURE_P3BIS, FIN_A, jp.PLEINE, appui_pleine(j)))
    m = _refus_b(j, run7, motif)
    assert f"[{nature}" in m


def test_G4_version_scellee_apres_le_verdict(jouet):
    """G4 : sur un lancement à ouverture réduite, un texte de lecture dont la ligne de scellement suit `VERDICT-P3BIS` → refus ;
    cas sain : même texte sur un lancement sans ouverture réduite → permis."""
    lignes = {rg.VERDICT_P3BIS: {"instant": 100}, "SCELLEMENT-T07-V2": {"instant": 200}, rg.SCELLEMENT_T07: {"instant": 50}}
    reduit = [{"cle": jp.OUVERTURE_P3BIS, "mode": jp.REDUITE, "instant": 60, "numero": 3, "date": rg.date_utc(60), "appui": "-"}]
    assert "G4" in ga.garde_g4("SCELLEMENT-T07-V2", lignes, reduit)
    assert ga.garde_g4("SCELLEMENT-T07-V2", lignes, []) is None
    assert ga.garde_g4(rg.SCELLEMENT_T07, lignes, reduit) is None
    codes = ga.garde_etape_b({**lignes, rg.SCORES_T07: {"instant": 70, "sha256": "1" * 64}, rg.SONDES_T07: {"instant": 70, "sha256": "2" * 64}},
                             reduit, None, None, cle_scellement="SCELLEMENT-T07-V2")
    assert ga.VERSION_APRES_VERDICT in [c for c, _ in codes]


def test_G4_R14_relance_R11_meme_lancement(jouet, monkeypatch):
    """« Lancement » (brouillon 17, m-3) : deux `RUN_T07` de la même course (relance après R11-arret) font un seul lancement : R14
    écrite à l'étape B du second run."""
    scenario_reduite(jouet, verdict=None)
    lignes_p3bis(jouet, INSTANT - 50)
    reel = lv1.garde_identite
    monkeypatch.setattr(lv1, "garde_identite", lambda *a, **k: (_ for _ in ()).throw(GardeArret("R11-arret : essai")))
    with pytest.raises(lv.ArretApresManifeste):
        _a(jouet)
    monkeypatch.setattr(lv1, "garde_identite", reel)
    ra = _a(jouet, instant=INSTANT + 40)
    lignes_audit(jouet, ra["run_t07"], instant=APRES_A + 50)
    ajouter_journal(jouet, ligne_j(jp.OUVERTURE_P3BIS, APRES_A + 50, jp.PLEINE, appui_pleine(jouet)))
    lec = _b(jouet, ra["run_t07"], instant=INSTANT_B + 50)
    assert any(r.startswith("R14 : ") for r in lec["reserves"])


def test_R14_L7b_finale_pour_7b_et_aucun_score_de_ii(depot, monkeypatch):
    """Sur un lancement à ouverture réduite, L7b est finale pour 7b (G4) : la phrase est écrite, la prédiction T7-P2 le dit ; aucun
    score de (ii) n'est ouvert (artefact : une condition S25 à S100 vue → échec). Sans ouverture réduite, la suite reste nulle."""
    vues = []
    original = lv1.lecture_jeux

    def espion(t, *a, **k):
        vues.extend(sorted(set(t["condition"].tolist())))
        return original(t, *a, **k)
    monkeypatch.setattr(lv1, "lecture_jeux", espion)
    j = construire(depot, par_dose={"S25": "réussit", "S50": "non calculable", "S75": "échoue", "S100": "échoue"})
    run7 = _lancement_reduit(j)
    lec = _b(j, run7)
    assert lec["issue_critere_3"] == "L7b" and lec["garde_adaptee"]["suite"] == lv.PHRASE_SUITE_FINALE
    assert lv.PHRASE_SUITE_FINALE in lec["predictions"]["T7-P2"]
    assert not set(vues) & set(lv1.cr.DOSES)


# ------------------------------------------------------------------------------------------------------------ journal de P3-bis
@pytest.mark.parametrize("contenu, motif", [
    ("| clé | date | mode |\n|---|---|---|\n", "en-tête"),
    (ENTETE + "| OUVERTURE-P3BIS | 2027-01-15T07:00:00Z | reduite | - | - |\n", "5 cellules"),
    (ENTETE + "| OUVERTURE-P3BIS | 2027-01-15T07:00:00Z | reduite | - | - | - | x |\n", "7 cellules"),
    (ENTETE + "| OUVERTURE-T07 | 2027-01-15T07:00:00Z | reduite | - | - | - |\n", "clé 'OUVERTURE-T07' inconnue"),
    (ENTETE + "| OUVERTURE-P3BIS | 2027-01-15 07:00:00 | reduite | - | - | - |\n", "date"),
    (ENTETE + "| OUVERTURE-P3BIS | 2027-01-15T07:00:00Z | partielle | - | - | - |\n", "mode 'partielle' inconnu"),
    (ENTETE + "| OUVERTURE-P3BIS | 2027-01-15T07:00:00Z | pleine | - | - | - |\n| OUVERTURE-P3BIS | 2027-01-15T07:10:00Z | reduite | - | - | - |\n",
     "ouverture 'reduite' après 'pleine'"),
    (ENTETE + "| OUVERTURE-P3BIS | 2027-01-15T07:00:00Z | reduite | - | - | - |\n| OUVERTURE-P3BIS | 2027-01-15T07:10:00Z | reduite | - | - | - |\n",
     "ouverture 'reduite' après 'reduite'"),
])
def test_journal_mal_forme_refus_noeud(depot, contenu, motif):
    """(xv) : journal mal formé (en-tête manquant, cinq ou sept cellules, clé inconnue, date mal formée, mode inconnu, ordre
    interdit) → refus, nœud, aux étapes A et B (A ici) ; cas sain : journal absent → aucune ouverture."""
    j = construire(depot)
    p = j.racine / jp.JOURNAL_P3BIS
    p.write_text(contenu, encoding="utf-8")
    with pytest.raises(jp.JournalFautif, match=motif):
        jp.lire_journal_p3bis(p)
    m = _refus_a(j, motif)
    assert "nœud" in m
    p.unlink()
    assert jp.lire_journal_p3bis(p) == []


@pytest.mark.xfail(strict=True, raises=jp.JournalFautif, reason="interprétation tolérante (ligne vide ignorée, appui libre) retirée par D-3 (R-2103) ; "
                   "cas sain refait aux formes exactes : tests/test_t07_journal_p3bis_d3_v1.py")
def test_journal_cas_sain_lignes_et_refus_lus():
    """(xv) : lecture du journal au format de P3-bis b8 ; une ligne `REFUS-OUVERTURE-P3BIS` est lue mais n'est jamais une ouverture ;
    ordre réduite → pleine permis ; ligne vide ignorée (interprétation déclarée)."""
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "j.md"
        p.write_text(ENTETE + ligne_j(jp.REFUS_OUVERTURE_P3BIS, 100, jp.REDUITE) + "\n\n" + ligne_j(jp.OUVERTURE_P3BIS, 200, jp.REDUITE, "x")
                     + "\n" + ligne_j(jp.OUVERTURE_P3BIS, 300, jp.PLEINE, "y") + "\n", encoding="utf-8")
        lu = jp.lire_journal_p3bis(p)
        assert [l["cle"] for l in lu] == [jp.REFUS_OUVERTURE_P3BIS, jp.OUVERTURE_P3BIS, jp.OUVERTURE_P3BIS]
        assert [o["mode"] for o in jp.ouvertures(lu)] == [jp.REDUITE, jp.PLEINE] and lu[1]["numero"] == 5


def test_prealables_artefacts():
    """Registre des préalables : numéros de rendez-vous non consécutifs, dates non croissantes, deux lignes de garde adaptée, clé
    inconnue, sceau faux, ligne postérieure à l'ouverture → refus ; fichier de décision cité d'un autre numéro → refus."""
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        r = Path(d)
        (r / "registres").mkdir()
        f = {n: _depot(r, jp.FICHIER_DECISION.format(n=n), f"Décision : maintenir\nDate : {rg.date_utc(100)}\n") for n in (1, 2, 3)}
        ga_ = _depot(r, jp.PREREG_T07, "# T0.7\n")

        def poser(lignes):
            (r / jp.PREALABLES_P3BIS).write_text("# P\n\n" + "".join(l + "\n" for l in lignes), encoding="utf-8")

        rdv = lambda n, t, ff=None: rg.ecrire_ligne(f"RENDEZ-VOUS-P3BIS-{n}", rg.date_utc(t), *(ff or f[n]))
        poser([rg.ecrire_ligne(jp.GARDE_ADAPTEE_T07_P3BIS, rg.date_utc(50), *ga_), rdv(1, 100), rdv(2, 200)])
        pre = jp.lire_prealables(r / jp.PREALABLES_P3BIS, r, 1000)                                       # cas sain
        assert [e["numero"] for e in pre["rendez_vous"]] == [1, 2] and jp.lire_decision(r, pre["rendez_vous"][1])["decision"] == jp.MAINTENIR
        for lignes, motif in (([rdv(1, 100), rdv(3, 200, f[3])], "non consécutifs"), ([rdv(1, 200), rdv(2, 100)], "non strictement croissantes"),
                              ([rg.ecrire_ligne(jp.GARDE_ADAPTEE_T07_P3BIS, rg.date_utc(50), *ga_)] * 2, "au plus une"),
                              ([rg.ecrire_ligne("AUTRE-CLE-P3BIS", rg.date_utc(50), *ga_)], "clé 'AUTRE-CLE-P3BIS' inconnue"),
                              ([rg.ecrire_ligne(jp.GARDE_ADAPTEE_T07_P3BIS, rg.date_utc(50), ga_[0], "0" * 64)], "empreinte"),
                              ([rdv(1, 2000)], "pas strictement antérieure")):
            poser(lignes)
            with pytest.raises(rg.RefusRegistre, match=motif):
                jp.lire_prealables(r / jp.PREALABLES_P3BIS, r, 1000)
        with pytest.raises(rg.RefusRegistre, match="même numéro"):
            jp.lire_decision(r, {"cle": "RENDEZ-VOUS-P3BIS-1", "numero": 1, "chemin": f[2][0], "sha256": f[2][1]})


# ----------------------------------------------------------------------------------------------------- (xi) couples figés de P3
def _fichier_leger_24(j, avec_mahalanobis: bool = False) -> None:
    """Fichier léger factice à 24 couples (4 familles × 2 concepts × 3 couches, aux noms de P3 ; les deux principales reprises du
    fichier léger du jouet, mêmes empreintes) + les directions de plancher du jouet ; la configuration le cite (`planchers_p3`)."""
    rng = np.random.default_rng(np.random.SeedSequence(777))
    vieux, meta, _ = lire_sondes(j.racine / j.config["planchers_p3"]["chemin"], j.config["planchers_p3"]["sha256"])
    par_nom = {s.nom: s for s in vieux}
    couples = []
    for concept in ("tromperie", "enjeux"):
        for fam in lv.FAMILLES_COUPLES:
            for c in lv.COUCHES_COUPLES:
                nom = f"{concept}-{fam}-c{c}"
                if nom in par_nom:
                    couples.append(par_nom[nom])
                elif fam == "perceptron":
                    couples.append(SondePerceptron(nom, c, "max", np.zeros(D), np.ones(D), rng.standard_normal((3, D)), np.zeros(3),
                                                   rng.standard_normal(3), 0.0))
                elif fam == "attention":
                    couples.append(SondeLineaireJetons(nom, c, "attention", rng.standard_normal(D), 0.0, rng.standard_normal(D), "attention"))
                else:
                    couples.append(SondeLineaireJetons(nom, c, "max", rng.standard_normal(D), 0.0, None, fam))
    if avec_mahalanobis:
        couples.append(mahalanobis("tromperie-mahalanobis-c15", 15, [rng.standard_normal((5, D)) for _ in range(12)]))
    directions = [s for s in vieux if s.nom not in par_nom or s.nom in {d for l in meta["planchers"].values() for d in l}]
    rel = "donnees/sondes-figees-legeres-24.npz"
    sha = ecrire_sondes(j.racine / rel, couples + [d for d in directions if d.nom not in {c.nom for c in couples}], meta)
    j.config["planchers_p3"] = {"chemin": rel, "sha256": sha}


def test_xi_24_couples_notes_en_descriptif_aucun_mahalanobis(jouet):
    """(xi) : les 24 couples figés lus dans le fichier léger, notés à l'étape A (tableaux `couple_<k>`), aucun de Mahalanobis, lus en
    descriptif à l'étape B (aire seule) ; artefact : une sonde de Mahalanobis parmi les couples → refus de l'étape A."""
    _fichier_leger_24(jouet)
    ra = _a(jouet)
    idx = ra["index"]["couples_figes"]
    assert len(idx) == 24 and all(e["etat"] == "notée" for e in idx) and not any(e["famille"] == "mahalanobis" for e in idx)
    assert {e["famille"] for e in idx} == set(lv.FAMILLES_COUPLES) and {e["couche"] for e in idx} == set(lv.COUCHES_COUPLES)
    with np.load(jouet.racine / ra["scores"]["chemin"]) as z:
        assert all(f"couple_{k}" in z.files and z[f"couple_{k}"].shape == z["cle"].shape for k in range(24))
        assert not any(k.startswith("plancher_") and k[9:].isdigit() and int(k[9:]) >= 4 for k in z.files)
    lignes_audit(jouet, ra["run_t07"])
    lignes_p3bis(jouet, APRES_A)
    lec = _b(jouet, ra["run_t07"])
    assert len(lec["couples_figes_descriptif"]) == 24
    assert all(set(v) == {cr_jeu for cr_jeu in [lv1.cr.JEU_I] + list(lv1.cr.DOSES)} for v in lec["couples_figes_descriptif"].values())
    (jouet.racine / "m").mkdir()
    j2 = construire(jouet.racine / "m")
    _fichier_leger_24(j2, avec_mahalanobis=True)
    _refus_a(j2, "sondes de Mahalanobis dans le fichier léger")


def test_xi_xii_fichier_leger_reel_24_couples_et_empreintes_de_la_liste_de_P3():
    """(xi), (xii), M-1 : le fichier léger réel (`701f73bd…`) porte les deux principales de P3 et 24 couples (0 Mahalanobis) ; leurs
    empreintes égalent celles de `resultat.sondes` de `sondes-figees.json` (`fb418127…`) quand cette liste est dans le dépôt ;
    artefacts : empreinte fausse → arrêt (R11) ; compte autre que 24 en mode réel → arrêt."""
    if not PLANCHERS_P3_REELS.is_file():
        pytest.skip("fichier léger réel absent de ce clone")
    rel = str(PLANCHERS_P3_REELS.relative_to(RACINE_DEPOT))
    config = {"mode": "reel", "planchers_p3": {"chemin": rel, "sha256": SHA_PLANCHERS_P3}}
    couples, rapport = lv.charger_couples_figes(RACINE_DEPOT, config)
    assert rapport["nombre"] == 24 and rapport["mahalanobis"] == 0
    assert set(lv.PRINCIPALES_P3.values()) <= {c.nom for c in couples}
    with pytest.raises(GardeArret):
        lv.charger_couples_figes(RACINE_DEPOT, {"mode": "reel", "planchers_p3": {"chemin": rel, "sha256": "0" * 64}})
    try:
        texte = subprocess.run(["git", "-C", str(RACINE_DEPOT), "show", f"HEAD:{LISTE_P3}"], capture_output=True, check=True).stdout
    except (subprocess.CalledProcessError, OSError):
        texte = b""
    if texte:
        import hashlib
        assert hashlib.sha256(texte).hexdigest().startswith(SHA_LISTE_P3)
        liste = {s["nom"]: s["empreinte"] for s in json.loads(texte)["resultat"]["sondes"]}
        assert all(liste[c["nom"]] == c["empreinte"] for c in rapport["couples"])
        assert len([n for n in liste if "mahalanobis" in n]) == 6 and not any("mahalanobis" in c["nom"] for c in rapport["couples"])


def test_xi_compte_reel_autre_que_24_arret(jouet):
    """(xi) en mode réel : un fichier léger qui ne porte pas exactement les 24 couples → arrêt (R11)."""
    with pytest.raises(GardeArret, match="24 attendues"):
        lv.charger_couples_figes(jouet.racine, {**jouet.config, "mode": "reel"})


# ------------------------------------------------------------------------------------------------------- énumérations
def _script_17():
    import hashlib
    assert hashlib.sha256(SCRIPT_17.read_bytes()).hexdigest().startswith(SHA_SCRIPT_17)
    spec = importlib.util.spec_from_file_location("grille_l_t07_brouillon17", SCRIPT_17)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_enumeration_0_bis_du_brouillon_17_rejouee_par_les_gardes_du_module():
    """(0 bis) du script du brouillon 17 (`2a0eac56…`) rejouée par `garde_adaptee_v1` (les gardes qu'appelle `lecture_v2.ouvrir`),
    cas par cas : 192 cas, 8 configurations impossibles sautées, même issue que le script dans chaque cas ; étape B possible dans
    12 cas (le script : 1 sous la garde du brouillon 14, 12 sous la garde adaptée) ; `pleine-anticipee` n'ouvre jamais l'étape B."""
    sc = _script_17()
    oa = sc.verifier_ordre_a()
    assert (oa["cas"], oa["defauts"], oa["impossibles"], oa["b14"], oa["b16"]) == (192, 0, 8, 1, 12)
    e = ga.enumerer_0bis()
    assert (e["n"], e["impossibles"], e["etapes_b"]) == (192, 8, 12) and e["issues"] == oa["issues"]
    for (ordre, mode, mode_p, deja), x in e["cas"].items():
        r = {ev: i for i, ev in enumerate(ordre)}
        assert sc.issues_garde_adaptee(r, mode, mode_p, deja) == [x["issue"]], (ordre, mode, mode_p, deja, x)
        assert not (x["etape_b"] and mode_p == jp.PLEINE_ANTICIPEE)
        if deja:
            assert x["arret"] == "A"


def test_enumeration_0_garde_B_v2_egale_au_script(depot):
    """Énumération (0) du script du brouillon 17 (égale à celle du brouillon 14) rejouée contre la garde **v2** de l'étape B
    (chemin sans ouverture anticipée) : 2 048 cas ; refus si et seulement si le script refuse ; une seule ligne au journal ; rien
    d'écrit ; 511 relances qui ouvrent puis refusent après la lecture ; 1 024 tentatives après un code 3, toutes refusées."""
    sc = _script_17()
    j = construire(depot)
    ra = _a(j)
    run7 = ra["run_t07"]
    lignes_audit(j, run7)
    lignes_p3bis(j, APRES_A)
    lignes = {}
    for l in j.registre.read_text(encoding="utf-8").splitlines():
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if c and c[0] in rg.CLES_CONNUES:
            lignes[c[0]] = l
    table = "table A de lecture-cout-t06.json"
    assert set(sc.ENTREES_B) == set(rg.EXIGEES_ETAPE_B) | {table}
    lc = j.racine / "diag" / RUN_T06 / "lecture-cout-t06.json"
    cache = j.racine / "cache-lc"
    cache.mkdir()
    fichiers = {n: j.racine / "diag" / run7 / n for n in (lv1.FICHIER_LECTURE, lv1.FICHIER_ARRET_B)}

    def poser(presentes, lecture, arret):
        corps = [lignes[k] for k in lignes if k not in rg.EXIGEES_ETAPE_B or k in presentes]
        j.registre.write_text("# Lignes de registre\n\n" + "\n".join(corps) + "\n", encoding="utf-8")
        for p, cible in ((lc, cache / lc.name), (Path(str(lc) + ".sha256"), cache / (lc.name + ".sha256"))):
            if table in presentes and not p.exists():
                os.replace(cible, p)
            elif table not in presentes and p.exists():
                os.replace(p, cible)
        for nom, present in ((lv1.FICHIER_LECTURE, lecture), (lv1.FICHIER_ARRET_B, arret)):
            if present and not fichiers[nom].exists():
                fichiers[nom].write_text("{}\n")
            elif not present and fichiers[nom].exists():
                fichiers[nom].unlink()

    def tenter(presentes, lecture, arret):
        poser(presentes, lecture, arret)
        avant, taille = _ecrits(j, run7), j.journal.stat().st_size if j.journal.is_file() else 0
        try:
            lv.ouvrir(j.racine, j.registre, j.config, "B", RUN_T06, INSTANT_B, run7)
            decision_ = "ouverture"
        except rg.RefusRegistre:
            decision_ = "refus"
        with open(j.journal, encoding="utf-8") as f:
            f.seek(taille)
            nouvelles = f.read().splitlines()
        attendu = "| REFUS-T07 |" if decision_ == "refus" else "| OUVERTURE-T07 |"
        assert len(nouvelles) == 1 and nouvelles[0].startswith(attendu), (presentes, lecture, arret, nouvelles)
        assert _ecrits(j, run7) == avant, (presentes, lecture, arret)
        return decision_

    tout = frozenset(sc.ENTREES_B)
    cas = relances = apres_arret = 0
    for masque in product((True, False), repeat=len(sc.ENTREES_B)):
        presentes = frozenset(e for e, p in zip(sc.ENTREES_B, masque) if p)
        for lecture, arret in product((False, True), repeat=2):
            cas += 1
            attendu, _ = sc.garde_etape_b(presentes, lecture, arret)
            assert tenter(presentes, lecture, arret) == attendu, (sorted(presentes), lecture, arret)
            if attendu == "refus" and not lecture and not arret:
                relances += 1
                assert tenter(tout, False, False) == "ouverture"
                assert tenter(tout, True, False) == "refus"
            if arret:
                apres_arret += 1
                assert tenter(tout, lecture, True) == "refus"
    assert (cas, relances, apres_arret) == (2048, 511, 1024)


# ------------------------------------------------------------------------------------------- reprises des gardes du brouillon 14
def test_chemin_normal_scores_posterieurs_au_verdict_refuses(jouet):
    """Chemin sans ouverture réduite : `SCORES-T07` et `SONDES-T07` non strictement antérieures à `VERDICT-P3BIS` → refus (CLT7B-03,
    porté par G3) ; cas sain : l'essai du chemin normal."""
    ra = _a(jouet)
    lignes_audit(jouet, ra["run_t07"])
    lignes_p3bis(jouet, FIN_A)
    _refus_b(jouet, ra["run_t07"], "pas strictement antérieure à VERDICT-P3BIS")


def test_B1_absence_refus_puis_relance_et_lecture_unique(jouet):
    """B-1 sous la v2 : `ISSUE-MOTS-ET-COUT-T06` absente → refus, code 2, rien d'écrit ; ligne remise → code 0, `lecture-t07.json`
    écrit une fois ; troisième tentative → refus (R12)."""
    ra = _a(jouet)
    lignes_audit(jouet, ra["run_t07"])
    lignes_p3bis(jouet, APRES_A)
    retiree = _sans_ligne(jouet, rg.ISSUE_MOTS_ET_COUT_T06)
    _refus_b(jouet, ra["run_t07"], "ISSUE-MOTS-ET-COUT-T06")
    with open(jouet.registre, "a", encoding="utf-8") as f:
        f.write(retiree + "\n")
    assert _b(jouet, ra["run_t07"], instant=INSTANT_B + 5)["issue_critere_3"] == "L2"
    sha = rg.sha256_de(jouet.racine / "diag" / ra["run_t07"] / lv1.FICHIER_LECTURE)
    with pytest.raises(rg.RefusRegistre, match="lecture-t07.json déjà présent"):
        _b(jouet, ra["run_t07"], instant=INSTANT_B + 10)
    assert rg.sha256_de(jouet.racine / "diag" / ra["run_t07"] / lv1.FICHIER_LECTURE) == sha


def test_commande_en_ligne_v2_codes_et_empreinte(jouet, tmp_path):
    """Commande en ligne de la v2 : étape A code 0 ; refus code 2 ; `empreinte-config` imprime l'empreinte canonique ; configuration
    sans `garde_adaptee` → code 2."""
    chemin = tmp_path / "config.json"
    chemin.write_text(json.dumps(jouet.config), encoding="utf-8")
    racine = str(jouet.racine)
    assert lv.main(["etape-a", racine, RUN_T06, str(chemin), "--instant", str(INSTANT)]) == 0
    assert lv.main(["etape-a", racine, RUN_T06, str(chemin), "--instant", str(INSTANT + 10)]) == 2      # étape A déjà jouée
    import hashlib
    from controle_ia.manifeste import config_canonique
    assert lv.empreinte_configuration(chemin) == hashlib.sha256(config_canonique(jouet.config)).hexdigest()
    assert lv.main(["empreinte-config", str(chemin)]) == 0
    sans = tmp_path / "sans.json"
    sans.write_text(json.dumps({k: v for k, v in jouet.config.items() if k != "garde_adaptee"}), encoding="utf-8")
    assert lv.main(["empreinte-config", str(sans)]) == 2


def test_nouveaux_modules_sans_moyenne_ni_lecture_interdite():
    """Aucune moyenne ni médiane sur les jetons dans les trois fichiers neufs (N-026) ; aucun ne nomme `lecture-sondes-t06.json`
    ni `extraire_mesures_epreuve_t06_v1` (DT-4)."""
    motifs = re.compile(r"\.mean\(|np\.mean|\.median\(|np\.median|nanmean|nanmedian")
    for nom in ("lecture_v2.py", "garde_adaptee_v1.py", "journal_p3bis_v1.py"):
        texte = (RACINE_DEPOT / "src" / "controle_ia" / "t07" / nom).read_text(encoding="utf-8")
        assert not motifs.search(texte), nom
        assert "lecture-sondes-t06.json" not in texte and "extraire_mesures_epreuve_t06_v1" not in texte, nom


def test_lire_registre_t07_egale_controle_lecture_t06_au_commit_061ac380(tmp_path):
    """Brouillon 19, « Reste », 1 quater (ii) : l'essai d'égalité de `tests/test_t07_lecture_v1.py` lit une branche absente de ce clone
    et se saute ; il est repris ici, pointé sur le commit `061ac380` (`origin/prep/t06-candidat2-v1`), où le script de contrôle
    d'ouverture de T0.6 est présent à l'octet (`ba2ba5cf…`) : égalité des refus sur les deux clés communes (cas sain et artefacts) ;
    une clé d'une autre tâche, ignorée par le script de T0.6, est traitée par la règle du registre partagé."""
    import hashlib
    r = subprocess.run(["git", "-C", str(RACINE_DEPOT), "show", "061ac380:scripts/controle_lecture_t06_v1.py"], capture_output=True, text=True)
    if r.returncode != 0:
        pytest.skip("commit 061ac380 absent de ce clone : essai d'égalité sauté (déclaré)")
    assert hashlib.sha256(r.stdout.encode("utf-8")).hexdigest() == SHA_CONTROLE_T06
    script = tmp_path / "controle_lecture_t06_v1.py"
    script.write_text(r.stdout, encoding="utf-8")
    spec = importlib.util.spec_from_file_location("controle_lecture_t06_v1", script)
    t06 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(t06)
    cles = ("SCELLEMENT-T07", "SCELLEMENT-P3BIS")
    sain = [rg.ecrire_ligne(k, AVANT, f"prereg/{k}.md", "a" * 64) for k in cles]
    cas = {"sain": sain, "absente": sain[:1], "double": sain + sain[:1],
           "mal formée": [sain[0], f"| SCELLEMENT-P3BIS | {AVANT} | prereg/x.md |"],
           "date": [sain[0], f"| SCELLEMENT-P3BIS | 2026-11-08 | prereg/x.md | {'a' * 64} |"],
           "sha": [sain[0], f"| SCELLEMENT-P3BIS | {AVANT} | prereg/x.md | zz |"],
           "chemin": [sain[0], f"| SCELLEMENT-P3BIS | {AVANT} | /prereg/x.md | {'a' * 64} |"]}
    vus = []
    for nom, lignes in cas.items():
        reg = tmp_path / f"{nom}.md"
        reg.write_text("# titre\n\n" + "\n".join(lignes) + "\n", encoding="utf-8")
        try:
            attendu = ("ok", t06.lire_registre(reg))
        except t06.Refus as e:
            attendu = ("refus", str(e))
        try:
            obtenu = ("ok", rg.lire_registre_t07(reg, cles))
        except rg.RefusRegistre as e:
            obtenu = ("refus", str(e))
        assert obtenu == attendu, nom
        vus.append(attendu[0])
    assert vus[0] == "ok" and set(vus[1:]) == {"refus"}
    reg = tmp_path / "autre.md"
    reg.write_text("\n".join(sain + [rg.ecrire_ligne("JEUX-CONTROLE-T08", AVANT, "x/y", "c" * 64)]) + "\n", encoding="utf-8")
    assert ("ok", t06.lire_registre(reg)) == ("ok", rg.lire_registre_t07(reg, cles, marques_autres=MARQUES))
    with pytest.raises(rg.RefusRegistre, match="ni exigée ni permise"):
        rg.lire_registre_t07(reg, cles)


@pytest.mark.parametrize("cas, motif", [("sans-go", "ni GO-ETAPE-A-T07"), ("go-7a", "course exploratoire 7a"),
                                        ("arret-t06", "arret.json présent"), ("sceau-faux", "compagnon .sha256")])
def test_reprises_garde_A_v2(depot, cas, motif):
    """Gardes du brouillon 14 reprises par `lecture_v2.ouvrir` à l'étape A : sans GO, manifeste de 7a, `arret.json` de T0.6, sceau
    faux → refus, code 2, une ligne `REFUS-T07`, rien d'écrit (cas sain : l'essai du chemin normal)."""
    j = construire(depot, go_id="GO-2026-11-08-11" if cas == "go-7a" else "GO-2026-11-02-28")
    if cas == "sans-go":
        _sans_ligne(j, rg.GO_ETAPE_A_T07)
    elif cas == "arret-t06":
        from controle_ia.manifeste import ecrire_resultat
        ecrire_resultat(j.racine, j.racine / "runs" / RUN_T06 / "manifeste.json", "arret", {"etape": "episodes", "motif": "essai"})
    elif cas == "sceau-faux":
        (j.racine / "prereg/jeux/J-D.jsonl").write_text("{\"altéré\": 1}\n", encoding="utf-8")
    _refus_a(j, motif)


def test_prealables_absents_les_regles_du_journal_jouent_quand_meme(jouet):
    """Registre des préalables absent (exigé : réduite au journal) : refus motivé, et la ligne `pleine-anticipee` du journal est
    nommée aussi (nœud), sans attendre les préalables."""
    ecrire_journal(jouet, [ligne_j(jp.OUVERTURE_P3BIS, INSTANT - 200, jp.REDUITE, f"RENDEZ-VOUS-P3BIS-1={'1' * 64} {jp.GARDE_ADAPTEE_T07_P3BIS}={'2' * 64}"),
                           ligne_j(jp.OUVERTURE_P3BIS, INSTANT - 100, jp.PLEINE_ANTICIPEE, f"RENDEZ-VOUS-P3BIS-2={'3' * 64}")])
    m = _refus_a(jouet, "registre des préalables de P3-bis .* absent")
    assert "pleine-anticipee" in m and "[nœud]" in m
