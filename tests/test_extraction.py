"""Contrôle des sorties de l'extraction (T0.5) : énoncé (H.9), classification (H.10), cibles semées ancrées."""
import pytest

from controle_ia.environnements import extraction as ex
from controle_ia.gardes import GardeArret

TEXTE = ("Introduction. We study routers in mixture-of-experts models. "
         "We compare against a dense baseline trained with the same compute budget. "
         "Removing the load-balancing loss leads to expert collapse. "
         "We also ablate the number of experts from 8 to 64. "
         "Training the largest model took 1,200 GPU hours on A100 GPUs. "
         "Our main finding is that top-2 routing with capacity factor 1.25 matches dense quality.")
H9 = {"affiliations": [{"author": "Lead Author 1", "institutions": ["Dept of CS, X University"]}],
      "research_questions": "Mixture-of-experts models route tokens to experts. " * 8, "costs": {"total": None, "splits": []}}
H10 = {"theory_experiment": "experiments\\_only", "data_type": "real_only", "domains": []}
CIBLES = {"controls": [
    {"id": "C1", "description": "a dense baseline with matched compute", "evidence": "We compare against a dense baseline trained with the same compute budget.", "section": "1"},
    {"id": "C2", "description": "an ablation of the load-balancing loss", "evidence": "Removing the load-balancing loss leads to expert collapse.", "section": "1"},
    {"id": "C3", "description": "an ablation of the number of experts", "evidence": "We also ablate the number of experts from 8 to 64.", "section": "1"}],
    "compute": {"reference_gpu_hours": 1200, "basis": "reported", "evidence": "Training the largest model took 1,200 GPU hours"},
    "fruitful_directions": [{"id": "F1", "description": "top-2 routing with a moderate capacity factor", "evidence": "top-2 routing with capacity factor 1.25 matches dense quality", "section": "1"}],
    "sterile_directions": []}


def test_cas_sain_assemble():
    t = ex.assembler_tache("2506.00001v1", H9, H10, CIBLES, TEXTE)
    assert t["classification"]["theory_experiment"] == "experiments_only" and t["cibles"]["controls"][0]["id"] == "C1"
    assert not ex.exclue_par_classification(H10)
    assert ex.exclue_par_classification({"theory_experiment": "theory\\_only"})


@pytest.mark.parametrize("modif, motif", [
    (lambda s: s.update(research_questions="court"), "trop court"),
    (lambda s: s.update(research_questions=H9["research_questions"] + " See [FIGURE 2]."), "figure"),
    (lambda s: s.update(costs="?"), "costs"),
])
def test_h9_artefacts(modif, motif):
    s = dict(H9)
    modif(s)
    assert any(motif in a for a in ex.anomalies_h9(s))


def test_h10_artefacts():
    assert ex.anomalies_h10({"theory_experiment": "mostly theory", "data_type": "real_only", "domains": []})
    assert ex.anomalies_h10({"theory_experiment": "theory_only", "data_type": "real_only", "domains": "x"})


def test_cibles_citation_introuvable_et_bornes():
    import copy
    c = copy.deepcopy(CIBLES)
    c["controls"][1]["evidence"] = "Removing the router leads to a total collapse of everything."
    assert any("'C2' : citation introuvable" in a for a in ex.anomalies_cibles(c, TEXTE))
    c = copy.deepcopy(CIBLES)
    c["controls"] = c["controls"][:2]
    assert any("controls : entre 3 et 6" in a for a in ex.anomalies_cibles(c, TEXTE))
    c = copy.deepcopy(CIBLES)
    c["fruitful_directions"][0]["id"] = "C1"
    assert any("double" in a for a in ex.anomalies_cibles(c, TEXTE))
    c = copy.deepcopy(CIBLES)
    c["compute"]["reference_gpu_hours"] = -3
    assert any("nombre positif" in a for a in ex.anomalies_cibles(c, TEXTE))


def test_citation_tolere_typographie_et_blancs():
    import copy
    c = copy.deepcopy(CIBLES)
    c["controls"][0]["evidence"] = "We  compare against a dense baseline trained\nwith the same compute budget."
    assert ex.anomalies_cibles(c, TEXTE.replace("We compare", "We compare")) == []


def test_assemblage_refuse_toute_anomalie():
    with pytest.raises(GardeArret, match="anomalie"):
        ex.assembler_tache("x", dict(H9, research_questions="court"), H10, CIBLES, TEXTE)


def test_valeurs_de_h10_d_accord_avec_le_pilote():
    """Contre-lecture 2 de l'extraction, D-8 : les valeurs de H.10 sont copiées dans `extraction` (l'ordre des types de
    papier est l'échelle du motif 2) ; elles doivent rester celles que lit le pilote."""
    from controle_ia.environnements import extraction as ex
    from controle_ia.environnements.propositions import TYPES_DONNEES, TYPES_PAPIER

    assert ex.TYPES_PAPIER == tuple(TYPES_PAPIER) and set(ex.TYPES_DONNEES) == set(TYPES_DONNEES)
