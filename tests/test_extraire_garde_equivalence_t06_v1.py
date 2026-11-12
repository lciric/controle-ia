"""Essais R5 de `scripts/extraire_garde_equivalence_t06_v1.py` (lecture des comptes de la garde d'équivalence de T0.6).

Faux dossier de sortie construit avec les VRAIES clés de la chaîne (forme du manifeste d'E3 bis `runs/20261108-065822-t06-reel/
manifeste.json`, `e9f0cbb4…` ; enveloppe `{"run_id", "manifeste_sha256", "resultat"}` de `manifeste.ecrire_resultat` ;
`fiches[k].phase/condition/equivalence`, `controles_negatifs[<état>]`, `etats`, `controle_negatif_donnees`, `arret`) ; aucune sonde,
aucun score. Cas sain ; artefacts : clé absente → arrêt explicite ; dossier sans distillation → « non réglé, distillation absente » ;
arrêt de garde présent → rapporté (lectures (i) et (ii)) ; le rejeu du tirage est identique à celui de la chaîne
(`manifeste.generateur` + `pilote_a.graines_des_actions` + `gen.random(T)`)."""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
import pytest

RACINE = Path(__file__).resolve().parents[1]
SCRIPT = RACINE / "scripts" / "extraire_garde_equivalence_t06_v1.py"
_spec = importlib.util.spec_from_file_location("extraire_garde_equivalence_t06_v1", SCRIPT)
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)

from controle_ia.environnements.pilote_a import graines_des_actions  # noqa: E402
from controle_ia.manifeste import generateur, graines  # noqa: E402

T, FRACTION, TOL = 10, 0.5, 0.2
TACHES_EVAL = ["e1", "e2", "e3", "e4"]
TACHES_DIST = ["d1", "d2", "d3"]
K_DIST = 5
ETATS = {"dose0": {"adaptateur": None, "dose": 0.0, "conditions": ["honnete", "saboteur", "temoin", "mention"]},
         "S25": {"adaptateur": "saboteur", "dose": 0.25, "conditions": ["S25"]},
         "S50": {"adaptateur": "saboteur", "dose": 0.5, "conditions": ["S50"]},
         "S75": {"adaptateur": "saboteur", "dose": 0.75, "conditions": ["S75"]},
         "S100": {"adaptateur": "saboteur", "dose": 1.0, "conditions": ["S100"]},
         "T100": {"adaptateur": "temoin", "dose": 1.0, "conditions": ["T100"]}}
CONFIG = {"N": 1, "T": T, "lot": 8, "fraction_equivalence": FRACTION, "tolerance_equivalence": TOL, "statistique_equivalence": "q99",
          "actions_min_controle_negatif": 10, "positions_min_controle_negatif": 4, "fraction_min_controle_negatif": 0.95,
          "go_id": "GO-2026-11-08-11", "mode": "reel"}


def _cles_graines() -> list[str]:
    cles = ["modele-jouet", "injection", "adaptateur/saboteur", "adaptateur/temoin", "distillation/saboteur", "distillation/temoin"]
    cles += [f"tache/{t}" for t in TACHES_EVAL]
    cles += [f"distillation/tache/{t}/e{k}" for t in TACHES_DIST for k in range(K_DIST)]
    return cles


def _tirage_chaine(graine: dict) -> list[int]:
    """Le tirage tel que la chaîne le fait (lanceur.py l. 148-151 et 267-270), avec les fonctions mêmes de la chaîne."""
    gen = generateur(graine)
    graines_des_actions(gen, 1, T)
    tirages = gen.random(T)
    return [s for s in range(T) if tirages[s] < FRACTION]


def _bilan(comparables: int, courtes: int = 0, echecs=(), lecture: str = "conforme") -> dict:
    passent = comparables - len(echecs)
    return {"comparables": comparables, "passent": passent, "courtes": courtes, "echecs": list(echecs),
            "fraction": passent / comparables if comparables else None, "min_des_maxima": 1.09 if comparables else None,
            "positions_min": 4, "statistique": "q99", "lecture": lecture}


def _ecrire(chemin: Path, corps: dict) -> None:
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(json.dumps(corps, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def faux_dossier(tmp: Path, *, entropie: int = 12345, distillation: bool = True, episodes: bool = True, arret: str | None = None,
                 q99_faute: bool = False, lecture_cn: str = "conforme") -> tuple[Path, dict]:
    """Arbre `runs/<run>/manifeste.json` + `diag/<run>/…` aux vraies clés ; rend la racine et les comptes attendus."""
    run = "20261109-010203-t06-reel"
    m = {"run_id": run, "commit": "0" * 40, "config": CONFIG, "config_sha256": "x", "cree_le": "2026-11-09T01:02:03Z", "decisif": False,
         "depot_propre": True, "preenregistrement": None, "reserves": [], "versions": {"numpy": np.__version__},
         "graines": graines(_cles_graines(), entropie=entropie), "commande": "python -m controle_ia.t06.lanceur_v6"}
    chemin_m = tmp / "runs" / run / "manifeste.json"
    _ecrire(chemin_m, m)
    sha_m = ex._sha256(chemin_m)
    retenus_eval = {t: _tirage_chaine(m["graines"][f"tache/{t}"]) for t in TACHES_EVAL}
    retenus_dist = {f"{t}/e{k}": _tirage_chaine(m["graines"][f"distillation/tache/{t}/e{k}"]) for t in TACHES_DIST for k in range(K_DIST)}
    n_eval = sum(len(v) for v in retenus_eval.values())
    n_dist = sum(len(v) for v in retenus_dist.values())
    attendu = {"paires_eval": len(TACHES_EVAL) * T, "retenues_eval": n_eval, "paires_dist": len(TACHES_DIST) * K_DIST * T, "retenues_dist": n_dist,
               "actions_par_etat": {e: n_eval * len(v["conditions"]) for e, v in ETATS.items()}, "actions_dist": 2 * n_dist}
    diag = tmp / "diag" / run
    if distillation:
        _ecrire(diag / "distillation-t06.json", {"run_id": run, "manifeste_sha256": sha_m, "resultat": {
            "plan": "b", "controle_negatif_donnees": _bilan(2 * n_dist - 3, courtes=3), "duree_s": 1200.5, "journaux": {}}})
    if episodes:
        fiches, cn, etats = [], {}, {}
        for nom, e in ETATS.items():
            etats[nom] = {"adaptateur": e["adaptateur"], "dose": e["dose"], "empreinte": "e" * 64}
            for t in TACHES_EVAL:
                for c in e["conditions"]:
                    actions = [f"0,{s}" for s in retenus_eval[t]]
                    val = 0.05 if not (q99_faute and nom == "S50") else 0.31
                    fiches.append({"episode": f"{c}/{t}/e0", "condition": c, "tache": t, "phase": nom, "jetons_par_action": [12] * T,
                                   "equivalence": {"actions": actions, "tolerance": TOL, "statistique": "q99",
                                                   "ecarts_q99": {a: {"7": val, "15": val, "23": val} for a in actions},
                                                   "ecarts": {a: {"7": 0.9, "15": 0.9, "23": 0.9} for a in actions},
                                                   "controle_negatif_zone_generee": {a: {} for a in actions},
                                                   "profils": {}, "longueurs_contexte": {}, "lignes": {}, "positions_capturees": {},
                                                   "empreintes_capture": {}, "sondes": {}},
                                   "empreintes": {}, "etat_adaptateurs": etats[nom]})
            n = attendu["actions_par_etat"][nom]
            cn[nom] = _bilan(n - 1, courtes=1, lecture=lecture_cn)
        _ecrire(diag / "episodes-t06.json", {"run_id": run, "manifeste_sha256": sha_m, "resultat": {
            "fiches": fiches, "etats": etats, "controles_negatifs": cn,
            "descriptifs": {"duree_s": 3000.0, "memoire_pic_gio": 24.1, "longueur_remplie_max": 4321}, "duree_s": 4000.0}})
    if arret is not None:
        _ecrire(diag / "arret.json", {"run_id": run, "manifeste_sha256": sha_m, "resultat": {
            "etape": "épisodes", "motif": arret, "partiel": {}, "duree_s": 999.0}})
    return tmp, attendu


def test_le_rejeu_du_tirage_est_celui_de_la_chaine():
    g = graines(_cles_graines(), entropie=777)
    gen = ex._generateur()
    for cle in _cles_graines():
        if cle.startswith(("tache/", "distillation/tache/")):
            assert ex.rejouer_tirage(g[cle], 1, T, FRACTION, gen) == _tirage_chaine(g[cle]), cle


def test_cas_sain_comptes_et_e3_6_regle(tmp_path):
    racine, att = faux_dossier(tmp_path)
    r = ex.extraire(racine)
    assert r["statut"] == "EXPLORATOIRE, NON OPPOSABLE (R-522)"
    p = r["paires_independantes"]
    assert (p["evaluation"]["paires"], p["evaluation"]["retenues"]) == (att["paires_eval"], att["retenues_eval"])
    assert (p["distillation"]["paires"], p["distillation"]["retenues"]) == (att["paires_dist"], att["retenues_dist"])
    assert att["retenues_eval"] > 0 and att["retenues_dist"] > 0            # l'entropie 12345 à 0,5 retient des paires : le cas sain exerce la garde
    assert r["evaluation"]["etats"] == 6 and r["evaluation"]["phases_sans_fiche"] == []
    for nom, ph in r["evaluation"]["phases"].items():
        assert ph["actions_controlees"] == att["actions_par_etat"][nom] == ph["actions_attendues_du_tirage"]
        assert ph["ecart_q99_max_par_couche"] == {"7": 0.05, "15": 0.05, "23": 0.05}
        assert ph["ecart_max_par_couche"] == {"7": 0.9, "15": 0.9, "23": 0.9}
        assert ph["couches_q99_au_dessus_tolerance"] == [] and ph["tolerances"] == [TOL]
        assert ph["controle_negatif"]["lecture"] == "conforme"
    assert r["distillation"]["actions_controlees"] == att["actions_dist"] == r["distillation"]["actions_attendues_du_tirage"]
    assert r["arret"] == {"present": False}
    assert r["descriptifs"]["memoire_pic_gio"] == 24.1 and r["descriptifs"]["duree_s"] == 3000.0
    assert r["manifeste"]["rattachement_des_resultats_au_manifeste"] == {"episodes-t06": True, "distillation-t06": True}
    assert r["e3_6"]["verdict"] == "réglé" and r["e3_6"]["motifs"] == [] and r["e3_6"]["ligne"].startswith("E3-6 réglé")


def test_cas_sain_en_ligne_de_commande_ecrit_un_fichier_marque_exploratoire(tmp_path):
    racine, _ = faux_dossier(tmp_path)
    sortie = tmp_path / "lecture"
    r = subprocess.run([sys.executable, str(SCRIPT), str(racine), "--sortie", str(sortie)], capture_output=True, text=True,
                       env={"PYTHONPATH": str(RACINE / "src"), "PATH": "/usr/bin:/bin"})
    assert r.returncode == 0, r.stderr
    assert r.stderr.strip().endswith("(garde d'équivalence exercée de fait, contrôles négatifs conformes)")
    fichiers = list(sortie.glob("garde-equivalence-*-exploratoire-non-opposable-r522.json"))
    assert len(fichiers) == 1 and json.loads(fichiers[0].read_text(encoding="utf-8"))["e3_6"]["verdict"] == "réglé"
    r2 = subprocess.run([sys.executable, str(SCRIPT), str(racine), "--sortie", str(sortie)], capture_output=True, text=True,
                        env={"PYTHONPATH": str(RACINE / "src"), "PATH": "/usr/bin:/bin"})
    assert r2.returncode == 2 and "existe déjà (R12)" in r2.stderr                   # jamais écrasé


@pytest.mark.parametrize("fichier, cle, attendu", [
    ("episodes-t06.json", "controles_negatifs", "episodes-t06.resultat → controles_negatifs"),
    ("episodes-t06.json", "etats", "episodes-t06.resultat → etats"),
    ("episodes-t06.json", "fiches", "episodes-t06.resultat → fiches"),
    ("distillation-t06.json", "controle_negatif_donnees", "distillation-t06.resultat → controle_negatif_donnees"),
])
def test_artefact_cle_absente_arrete_explicitement(tmp_path, fichier, cle, attendu):
    racine, _ = faux_dossier(tmp_path)
    f = racine / "diag" / "20261109-010203-t06-reel" / fichier
    corps = json.loads(f.read_text(encoding="utf-8"))
    del corps["resultat"][cle]
    f.write_text(json.dumps(corps), encoding="utf-8")
    with pytest.raises(ex.CleAbsente) as e:
        ex.extraire(racine)
    assert attendu in e.value.message and e.value.code == 2
    r = subprocess.run([sys.executable, str(SCRIPT), str(racine)], capture_output=True, text=True,
                       env={"PYTHONPATH": str(RACINE / "src"), "PATH": "/usr/bin:/bin"})
    assert r.returncode == 2 and "clé absente" in r.stderr and r.stdout == ""


def test_artefact_cle_absente_dans_une_fiche(tmp_path):
    racine, _ = faux_dossier(tmp_path)
    f = racine / "diag" / "20261109-010203-t06-reel" / "episodes-t06.json"
    corps = json.loads(f.read_text(encoding="utf-8"))
    del corps["resultat"]["fiches"][3]["equivalence"]["actions"]
    f.write_text(json.dumps(corps), encoding="utf-8")
    with pytest.raises(ex.CleAbsente) as e:
        ex.extraire(racine)
    assert "equivalence.actions" in e.value.message


def test_artefact_manifeste_sans_fraction(tmp_path):
    racine, _ = faux_dossier(tmp_path)
    f = racine / "runs" / "20261109-010203-t06-reel" / "manifeste.json"
    corps = json.loads(f.read_text(encoding="utf-8"))
    del corps["config"]["fraction_equivalence"]
    f.write_text(json.dumps(corps), encoding="utf-8")
    with pytest.raises(ex.CleAbsente) as e:
        ex.extraire(racine)
    assert "fraction_equivalence" in e.value.message


def test_artefact_sans_distillation_non_regle(tmp_path):
    racine, _ = faux_dossier(tmp_path, distillation=False)
    r = ex.extraire(racine)
    assert r["distillation"] == {"present": False}
    assert r["e3_6"]["verdict"] == "non réglé" and "distillation absente" in r["e3_6"]["motifs"]
    assert r["e3_6"]["ligne"].startswith("E3-6 non réglé : distillation absente")


def test_artefact_sans_episodes_non_regle(tmp_path):
    racine, _ = faux_dossier(tmp_path, episodes=False)
    r = ex.extraire(racine)
    assert r["evaluation"] == {"present": False} and "épisodes absents" in r["e3_6"]["motifs"]
    assert r["descriptifs"]["memoire_pic_gio"] == "absent"


@pytest.mark.parametrize("motif, lecture", [
    ("GardeArret: S50/e3/e0, action (0, 7) : activations de génération ≠ passe unique (écarts, q99 {7: 0.31} > 0.2)", "(i) inéquivalence réelle à la tolérance"),
    ("GardeArret: T0.6, phase T100 : garde d'équivalence aveugle au décalage d'un jeton dans la zone générée pour 9 action(s) sur 120 ([...])",
     "(ii) contrôle négatif aveugle au décalage d'un jeton"),
    ("GardeArret: arrêt demandé par signal TERM", "autre"),
])
def test_artefact_arret_de_garde_rapporte(tmp_path, motif, lecture):
    racine, _ = faux_dossier(tmp_path, arret=motif, episodes=False)
    r = ex.extraire(racine)
    assert r["arret"]["present"] is True and r["arret"]["etape"] == "épisodes" and r["arret"]["lecture"] == lecture
    assert r["arret"]["motif"] == motif
    assert r["e3_6"]["verdict"] == "non réglé" and any(m.startswith("arrêt consigné") for m in r["e3_6"]["motifs"])


def test_artefact_q99_au_dessus_de_la_tolerance_et_controle_negatif_non_conforme(tmp_path):
    racine, _ = faux_dossier(tmp_path, q99_faute=True, lecture_cn="non concluant")
    r = ex.extraire(racine)
    assert r["evaluation"]["phases"]["S50"]["couches_q99_au_dessus_tolerance"] == ["7", "15", "23"]
    motifs = r["e3_6"]["motifs"]
    assert any(m.startswith("S50 : écart q99 > 0.2") for m in motifs)
    assert sum(m.endswith(")") and "« non concluant »" in m for m in motifs) == 6
    assert r["e3_6"]["verdict"] == "non réglé"


def test_artefact_zero_action_controlee_garde_non_exercee(tmp_path):
    racine, att = faux_dossier(tmp_path, entropie=5)
    # quelle que soit l'entropie, on vide les listes d'actions d'un état : la garde n'y est pas exercée
    f = racine / "diag" / "20261109-010203-t06-reel" / "episodes-t06.json"
    corps = json.loads(f.read_text(encoding="utf-8"))
    for fi in corps["resultat"]["fiches"]:
        if fi["phase"] == "T100":
            fi["equivalence"]["actions"] = []
            fi["equivalence"]["ecarts_q99"] = {}
            fi["equivalence"]["ecarts"] = {}
    f.write_text(json.dumps(corps), encoding="utf-8")
    r = ex.extraire(racine)
    assert r["evaluation"]["phases"]["T100"]["actions_controlees"] == 0
    assert r["evaluation"]["phases"]["T100"]["actions_attendues_du_tirage"] == att["actions_par_etat"]["T100"]
    assert "T100 : aucune action contrôlée (garde non exercée)" in r["e3_6"]["motifs"]


def test_artefact_deux_manifestes_sans_run_arrete(tmp_path):
    racine, _ = faux_dossier(tmp_path)
    autre = racine / "runs" / "20261109-020000-t06-reel" / "manifeste.json"
    autre.parent.mkdir(parents=True)
    autre.write_text("{}", encoding="utf-8")
    with pytest.raises(ex.CleAbsente) as e:
        ex.extraire(racine)
    assert "2 trouvé(s)" in e.value.message
    r = ex.extraire(racine, "20261109-010203-t06-reel")
    assert r["run_id"] == "20261109-010203-t06-reel"
