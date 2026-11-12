"""Essais R5 de `src/controle_ia/t07/controle_jeux_v1.py` (E-8, décision D-2 (a), R-2101) : rejeu du contrôle 9 des jeux contre les
textes de la course et remesure des jetons contre le journal du script, avant l'extraction ; dans l'étape A et dans la passe à
blanc. Jeux factices de `tests/test_t07_sondes_neuves_v1.py`, textes de course factices ; aucun texte de 7b n'est lu ici. Chaque
garde : un cas sain et au moins un artefact."""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller
from controle_ia.t07 import controle_jeux_v1 as cj
from controle_ia.t07 import lecture_v2 as lv
from controle_ia.t07 import passe_blanc_v1 as pb
from controle_ia.t07 import sondes_neuves_v1 as sn
from test_t07_lecture_v1 import RUN_T06
from test_t07_passe_blanc_v1 import COUCHES_JOUET, extracteur_jouet, memoire
from test_t07_sondes_neuves_v1 import _a, _resultat, construire_complet, enregistrements

RACINE_DEPOT = Path(__file__).resolve().parents[1]
SCRIPT = RACINE_DEPOT / "scripts" / "verifier_jeux_synthetiques_t07_v2.py"
TACHES_10 = [f"r{i:02d}" for i in range(3)]


def script():
    if not SCRIPT.is_file():
        pytest.skip("script de vérification des jeux absent")
    spec = importlib.util.spec_from_file_location("verifier_jeux_t07_v2_essai", SCRIPT)
    m = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = m
    spec.loader.exec_module(m)
    return m


class TokFactice:
    """Tokeniseur factice du script : un jeton par caractère."""

    class _E:
        def __init__(self, n):
            self.ids = list(range(n))

    def encode(self, texte, add_special_tokens=False):
        return self._E(len(texte))


def journal_du_script(recs_par_jeu: dict) -> str:
    """Journal écrit par les fonctions mêmes du script (`controle_6_longueurs`, `rapporter`) sur les jeux donnés."""
    s = script()
    paires: dict = {}
    for recs in recs_par_jeu.values():
        for r in recs:
            paires.setdefault((r["jeu"], r["tache"], r["paire"]), {})[r["etiquette"]] = r
    j = s.Journal()
    longueurs = s.controle_6_longueurs(paires, j, TokFactice())
    s.rapporter(j, {"valeurs_par_tache": {}, "groupes_par_etiquette": {k: {0: [], 1: []} for k in s.JEUX}}, longueurs)
    return j.texte() + f"jetons : mesurés (tokeniseur tokenizer.json, sha256 {cj.EMPREINTE_TOKENISEUR}, bibliothèque tokenizers)\n"


# ---------------------------------------------------------------------------------------------------------------- copies fidèles
def test_normaliser_et_n_grammes_egaux_au_script():
    """Les copies du module rendent ce que rendent les fonctions du script (`e53c9c27…`)."""
    s = script()
    for t in ("Élan d'ÉTÉ, 12 chats : ça va ?", "ACTION: ADD\nTITLE: Plan r00 — étude n°3", "", "un deux trois quatre cinq six sept huit neuf"):
        assert cj.normaliser(t) == s.normaliser(t)
        assert cj.n_grammes(cj.normaliser(t)) == s.n_grammes(s.normaliser(t))
    assert cj.N_GRAMME == s.N_GRAMME == 8


# ------------------------------------------------------------------------------------------------------------- rejeu du contrôle 9
def _huit(texte: str, debut: int = 0) -> str:
    return " ".join(texte.split()[debut:debut + 8])


def test_rejeu_cas_sain_rien_d_exclu():
    jeux = {"JD": enregistrements("dissimulation"), "JC": enregistrements("domaine-cout"), "JA": enregistrements("intention-autres-modes")}
    r = cj.rejouer_controle_9(jeux, ["une action de la course sans rapport avec les jeux, écrite pour l'essai"], None)
    assert all(len(r["jeux"][k]) == len(jeux[k]) for k in jeux)
    assert all(not x["paires_en_defaut"] and not x["taches_sorties"] and not x["insertion_non_isolee"] for x in r["rapport"]["jeux"].values())


def test_rejeu_artefact_reponse_recopiee_paire_exclue_et_tache_sortie():
    """Une suite de 8 mots d'une réponse de J-C (tâche r01, paire 2) dans un texte de la course : paire exclue ; la tâche r01 garde 1
    paire sur 2 (seuil effectif min(8, 2) = 2) : elle sort de J-C, consignée ; les autres tâches et jeux sont intacts."""
    jc = enregistrements("domaine-cout")
    cible = next(x for x in jc if x["tache"] == "r01" and x["paire"] == 2 and x["membre"] == "B")
    r = cj.rejouer_controle_9({"JC": jc}, ["préambule " + _huit(cible["reponse"], 2) + " suite"], None)
    rap = r["rapport"]["jeux"]["JC"]
    assert [(d["tache"], d["paire"]) for d in rap["paires_en_defaut"]] == [("r01", 2)]
    assert rap["taches_sorties"] == [{"tache": "r01", "paires_restantes": 1, "paires_scellees": 2}]
    assert {x["tache"] for x in r["jeux"]["JC"]} == {"r00", "r02", "r03", "r04"} and len(r["jeux"]["JC"]) == len(jc) - 4


def test_rejeu_suite_de_l_enonce_ne_compte_pas():
    """Cas sain de la règle de l'énoncé : la même suite figure dans l'énoncé de la tâche → aucune paire en défaut ; artefact :
    énoncé d'une autre tâche → défaut."""
    jc = enregistrements("domaine-cout")
    cible = next(x for x in jc if x["tache"] == "r01" and x["paire"] == 2)
    suite = _huit(cible["reponse"], 2)
    assert not cj.rejouer_controle_9({"JC": jc}, [suite], {"r01": "énoncé : " + suite})["rapport"]["jeux"]["JC"]["paires_en_defaut"]
    assert cj.rejouer_controle_9({"JC": jc}, [suite], {"r02": "énoncé : " + suite})["rapport"]["jeux"]["JC"]["paires_en_defaut"]


def test_rejeu_bloc_de_J_D_et_contexte_de_base():
    """Le bloc de J-D (membre positif) est pris comme les suites de son contexte absentes du contexte du membre négatif : une
    suite du bloc dans la course → paire en défaut (« bloc ou rappel ») ; une suite du seul contexte de base → aucun défaut."""
    jd = enregistrements("dissimulation")
    pos = next(x for x in jd if x["etiquette"] == 1)
    base = next(x for x in jd if x["etiquette"] == 0)
    mots_pos = cj.normaliser(cj._contexte(pos))
    k = mots_pos.index("secret")
    r = cj.rejouer_controle_9({"JD": jd}, [" ".join(mots_pos[k - 3:k + 5])], None)
    assert all("bloc ou rappel" in m for d in r["rapport"]["jeux"]["JD"]["paires_en_defaut"] for m in d["motifs"])
    assert len(r["rapport"]["jeux"]["JD"]["paires_en_defaut"]) == len(jd) // 2
    r = cj.rejouer_controle_9({"JD": jd}, [" ".join(cj.normaliser(cj._contexte(base))[:8])], None)
    assert not r["rapport"]["jeux"]["JD"]["paires_en_defaut"]


def test_rejeu_incitation_de_J_C_sans_contexte_de_base_ecrite():
    """J-C seul (aucun contexte de base de la tâche) : l'incitation n'est pas isolée, c'est écrit (aucun repli silencieux) ; avec
    J-A chargé, elle l'est."""
    jc = enregistrements("domaine-cout")
    r = cj.rejouer_controle_9({"JC": jc}, ["rien"], None)
    assert r["rapport"]["jeux"]["JC"]["insertion_non_isolee"] == sorted({x["tache"] for x in jc})
    r = cj.rejouer_controle_9({"JC": jc, "JA": enregistrements("intention-autres-modes")}, ["rien"], None)
    assert r["rapport"]["jeux"]["JC"]["insertion_non_isolee"] == []


def test_rejeu_seuils_de_la_consigne_dix_paires():
    """Seuils de l'étape 4 au plein effectif : J-D à 10 paires par tâche garde la tâche à 8 paires (cas sain), la sort à 7
    (artefact) ; J-A, 5 paires par mode : 4 gardées par mode (sain), 3 → la tâche sort (artefact)."""
    jd = enregistrements("dissimulation", TACHES_10, paires=10)
    def course(recs, tache, paires):
        return [_huit(x["reponse"], 2) for x in recs if x["tache"] == tache and x["paire"] in paires and x["membre"] == "A"]
    r = cj.rejouer_controle_9({"JD": jd}, course(jd, "r00", (1, 2)), None)["rapport"]["jeux"]["JD"]
    assert len(r["paires_en_defaut"]) == 2 and r["taches_sorties"] == []
    r = cj.rejouer_controle_9({"JD": jd}, course(jd, "r00", (1, 2, 3)), None)["rapport"]["jeux"]["JD"]
    assert r["taches_sorties"] == [{"tache": "r00", "paires_restantes": 7, "paires_scellees": 10}]
    ja = enregistrements("intention-autres-modes", TACHES_10, paires=10)
    r = cj.rejouer_controle_9({"JA": ja}, course(ja, "r01", (1,)), None)["rapport"]["jeux"]["JA"]
    assert r["taches_sorties"] == []
    r = cj.rejouer_controle_9({"JA": ja}, course(ja, "r01", (1, 3)), None)["rapport"]["jeux"]["JA"]
    assert r["taches_sorties"] == [{"tache": "r01", "mode": "controles", "paires_restantes": 3, "paires_scellees": 5}]


# ------------------------------------------------------------------------------------------------------------ remesure des jetons
def _poser_journal(dossier: Path, texte: str, nom: str = "journal-verification-v2.txt") -> Path:
    p = dossier / nom
    p.write_text(texte, encoding="utf-8")
    sceller(p)
    return p


def test_remesure_egale_au_journal_ecrit_par_le_script(tmp_path):
    """Cas sain : le journal écrit par les fonctions du script, relu et remesuré (un jeton par caractère des deux côtés) : conforme,
    six mesures comparées pour J-C et J-A, trois pour J-D."""
    jeux = {"JD": enregistrements("dissimulation"), "JC": enregistrements("domaine-cout"), "JA": enregistrements("intention-autres-modes")}
    _poser_journal(tmp_path, journal_du_script(jeux))
    for k, recs in jeux.items():
        r = cj.remesurer_jetons(k, recs, tmp_path / f"{k}.jsonl", len, "reel")
        assert r["etat"] == "conforme" and len(r["comparees"]) == (3 if k == "JD" else 6)


def test_remesure_artefacts(tmp_path):
    """Artefacts : tokeniseur différent (un jeton de plus par texte) → arrêt ; journal absent → arrêt en réel, « non vérifiée » en
    jouet ; deux journaux qui portent le jeu → arrêt ; compagnon faux → arrêt ; tokeniseur du journal non cité en réel → arrêt."""
    recs = enregistrements("domaine-cout")
    with pytest.raises(GardeArret, match="aucun journal"):
        cj.remesurer_jetons("JC", recs, tmp_path / "JC.jsonl", len, "reel")
    assert cj.remesurer_jetons("JC", recs, tmp_path / "JC.jsonl", len, "jouet")["etat"].startswith("non vérifiée")
    texte = journal_du_script({"JC": recs})
    p = _poser_journal(tmp_path, texte)
    with pytest.raises(GardeArret, match="écart avec le journal"):
        cj.remesurer_jetons("JC", recs, tmp_path / "JC.jsonl", lambda x: len(x) + 1, "reel")
    autre = tmp_path / "autre"
    autre.mkdir()
    _poser_journal(autre, texte.replace(cj.EMPREINTE_TOKENISEUR, "0" * 64))
    with pytest.raises(GardeArret, match="ne cite pas le tokeniseur"):
        cj.remesurer_jetons("JC", recs, autre / "JC.jsonl", len, "reel")
    _poser_journal(tmp_path, texte, "journal-verification-v2-bis.txt")
    with pytest.raises(GardeArret, match="plusieurs journaux"):
        cj.remesurer_jetons("JC", recs, tmp_path / "JC.jsonl", len, "reel")
    (tmp_path / "journal-verification-v2-bis.txt").unlink()
    p.write_text(texte + "\n", encoding="utf-8")
    with pytest.raises(GardeArret):
        cj.remesurer_jetons("JC", recs, tmp_path / "JC.jsonl", len, "reel")


# --------------------------------------------------------------------------------------------------------- énoncés, configuration
def test_enonces_cle_facultative_exigee_en_reel_a_l_etape(tmp_path):
    """`enonces_reserve` : forme contrôlée ; en réel, le fichier scellé de T0.5 ; à l'étape A en réel, absente → refus ; en jouet,
    absente : permise. Lecture : sceau vérifié, seuls identifiant et questions rendus."""
    cj.exiger_enonces_config({"mode": "jouet"})
    cj.exiger_enonces_pour_l_etape({"mode": "jouet"})
    with pytest.raises(GardeArret, match="enonces_reserve absente"):
        cj.exiger_enonces_pour_l_etape({"mode": "reel"})
    with pytest.raises(GardeArret, match="attendu en mode réel"):
        cj.exiger_enonces_config({"mode": "reel", "enonces_reserve": {"chemin": "x.json", "sha256": "0" * 64}})
    cj.exiger_enonces_config({"mode": "reel", "enonces_reserve": {"chemin": cj.CHEMIN_ENONCES_REEL, "sha256": cj.SHA_ENONCES_REEL}})
    with pytest.raises(GardeArret, match="chemin, sha256"):
        cj.exiger_enonces_config({"mode": "jouet", "enonces_reserve": {"chemin": "x.json"}})
    f = tmp_path / "taches.json"
    f.write_text(json.dumps({"resultat": {"taches": [{"identifiant": "r00", "questions": "Q0", "cibles": {"x": 1}}]}}), encoding="utf-8")
    sha = sceller(f)
    assert cj.lire_enonces(tmp_path, {"enonces_reserve": {"chemin": "taches.json", "sha256": sha}}) == {"r00": "Q0"}
    with pytest.raises(GardeArret):
        cj.lire_enonces(tmp_path, {"enonces_reserve": {"chemin": "taches.json", "sha256": "1" * 64}})


# ----------------------------------------------------------------------------------------------------- dans l'étape A et la passe
@pytest.fixture
def complet(depot):
    return construire_complet(depot)


def test_etape_A_consigne_les_controles_et_exclut_les_paires_en_defaut(complet, monkeypatch):
    """Cas sain : rien d'exclu, remesure « non vérifiée » (extracteur factice des essais), contrôles écrits dans `sondes-t07.json` ;
    artefact : une suite de 8 mots d'une réponse de J-D dans les textes de la course → la paire est exclue avant l'apprentissage,
    la tâche sort de J-D (consigné), le découpage ne la porte plus pour la dissimulation."""
    ra = _a(complet)
    cjs = _resultat(complet, ra["run_t07"], "sondes-t07.json")["controles_jeux"]
    assert all(not x["paires_en_defaut"] for x in cjs["controle_9"]["jeux"].values())
    assert all(v["etat"].startswith("non vérifiée") for v in cjs["remesure_jetons"].values())


def test_etape_A_artefact_paire_en_defaut_exclue(depot, monkeypatch):
    j = construire_complet(depot)
    jd = enregistrements("dissimulation")
    cible = next(x for x in jd if x["tache"] == "r03" and x["paire"] == 1)
    original = lv.lire_textes

    def lire(chemin):
        t = original(chemin)
        t[sorted(t)[0]] = "copie " + _huit(cible["reponse"], 1)
        return t
    monkeypatch.setattr(lv, "lire_textes", lire)
    vus = {}
    vrai = sn.apprendre

    def espion(jeux, *a, **k):
        vus["JD"] = {x["tache"] for x in jeux["JD"]}
        return vrai(jeux, *a, **k)
    monkeypatch.setattr(sn, "apprendre", espion)
    ra = _a(j)
    rap = _resultat(j, ra["run_t07"], "sondes-t07.json")["controles_jeux"]["controle_9"]["jeux"]["JD"]
    assert [(d["tache"], d["paire"]) for d in rap["paires_en_defaut"]] == [("r03", 1)]
    assert [s["tache"] for s in rap["taches_sorties"]] == ["r03"] and "r03" not in vus["JD"]


def test_passe_a_blanc_remesure_cas_sain_et_artefact(depot):
    """Passe à blanc : journal du script (moyennes au tokeniseur jouet) à côté des jeux → remesure conforme, passe tenue ; journal
    d'une moyenne fausse → arrêt motivé « remesure des jetons »."""
    j = construire_complet(depot)
    j.config["couches"] = list(COUCHES_JOUET)
    ext = extracteur_jouet()
    from controle_ia.harnais.formats import _ids
    jeux = {k: sn.lire_jeu(j.racine / f"prereg/jeux-v3/scellement-jeux-t07-{k.lower()}.jsonl", n)
            for k, n in (("JD", sn.JEU_JD), ("JC", sn.JEU_JC), ("JA", sn.JEU_JA))}
    lignes = []
    for recs in jeux.values():
        for e, x in sorted(cj.mesurer_longueurs(recs, lambda t: len(_ids(ext.fmt.tok, t))).items()):
            lignes.append(f"[INFO] longueurs {recs[0]['jeu']}, étiquette {e} (moyennes sur {x['n']} réponses) : {dict(sorted(x['moyennes'].items()))}")
    dossier = j.racine / "prereg" / "jeux-v3"
    p = _poser_journal(dossier, "\n".join(lignes) + "\n")
    r = pb.passe_a_blanc(j.racine, j.registre, j.config, RUN_T06, instant=1_800_000_000, extracteur=ext, mesure=memoire())
    assert r["issue"] == "tenue" and all(v["etat"] == "conforme" for v in r["sortie"]["remesure_jetons"].values())
    p.unlink()
    Path(str(p) + ".sha256").unlink()
    faux = "\n".join(lignes).replace("'jetons': ", "'jetons': 1", 1) + "\n"
    _poser_journal(dossier, faux, "journal-verification-v3.txt")
    r = pb.passe_a_blanc(j.racine, j.registre, j.config, RUN_T06, instant=1_800_000_001, extracteur=ext, mesure=memoire())
    assert r["issue"] == "arrêt" and any(m.startswith("remesure des jetons de JD") for m in r["motifs"])


# ------------------------------------------------------------------------------------- DF-03 (contre-lecture différentielle)
def test_DF03_jeu_vide_par_le_rejeu_garde_nommee(depot, monkeypatch):
    """DF-03 : une suite de 8 mots commune à toutes les réponses de J-D (et de J-C) dans les textes de la course vide ces jeux :
    l'étape A s'arrête par une garde nommée (« vidé par le rejeu »), `arret.json` écrit, jamais une `KeyError` ; cas sain : les
    essais de l'étape A plus haut (rien d'exclu)."""
    from controle_ia.t07.lecture_v1 import ArretApresManifeste
    j = construire_complet(depot)
    commune = "soignée sobre CONTROLS: témoins COST: 120 PREDICTION: gain modeste"
    original = lv.lire_textes

    def lire(chemin):
        t = original(chemin)
        t[sorted(t)[0]] = "copie : " + commune
        return t
    monkeypatch.setattr(lv, "lire_textes", lire)
    with pytest.raises(ArretApresManifeste, match="vidé par le rejeu"):
        _a(j)
    arrets = list(j.racine.glob("diag/*-t07-*/arret.json"))
    assert len(arrets) == 1 and "vidé par le rejeu" in json.loads(arrets[0].read_text(encoding="utf-8"))["resultat"]["motif"]
