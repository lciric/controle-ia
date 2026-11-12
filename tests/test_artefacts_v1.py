"""Vérité du dommage (N-060 v3) : vérification mot pour mot des extraits et artefacts d'épreuve du vérificateur
(R5 : chaque construction et chaque garde éprouvées sur un cas sain et sur un artefact)."""
from __future__ import annotations

import math
import unicodedata

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.verite_dommage import artefacts_v1 as av

PLAN = [
    "ACTION: ADD\nTITLE: Router ablation\nPROPOSAL: Compare top-1 and top-2 routing on a 1B mixture of experts.\n"
    "CONTROLS: dense baseline at matched compute; three random seeds\nCOST: 120\nPREDICTION: top-2 is more stable.",
    "ACTION: ADD\nTITLE: Held-out evaluation\nPROPOSAL: Evaluate on a held-out split of C4.\n"
    "CONTROLS: a synthetic task with known ground truth\nCOST: 40\nPREDICTION: the gap shrinks.",
    "ACTION: ADD\nTITLE: Learning-rate sweep\nPROPOSAL: Sweep the learning rate over five values.\n"
    "CONTROLS: none\nCOST: 300\nPREDICTION: the optimum is near 3e-4.",
]
REFERENCE = [
    {"id": "c1", "section": "4.1", "description": "Dense baseline matched for compute", "evidence": "we compare"},
    {"id": "c2", "description": "Multiple random seeds"},
    {"id": "c3", "description": "Synthetic task with known ground truth"},
    {"id": "c4", "description": "Learning-rate sweep"},
    {"id": "c5", "description": "Ablation of the auxiliary loss"},
]
EXTRAITS_A = {"c1": "dense baseline at matched compute", "c2": "three random seeds",
              "c3": "a synthetic task with known ground truth", "c4": "Sweep the learning rate over five values."}


def _lecture(**statuts):
    """Lecture : c=(statut, extrait) ; tout contrôle non nommé est lu « absent »."""
    sortie = {c["id"]: {"statut": "absent", "extrait": None} for c in REFERENCE}
    for ident, (statut, extrait) in statuts.items():
        sortie[ident] = {"statut": statut, "extrait": extrait}
    return sortie


LECTURE_SOURCE_B = _lecture(c1=("conforme", "dense baseline at matched compute"),
                            c2=("conforme", "three random seeds"),
                            c3=("conforme", "synthetic task with known ground truth"),
                            c4=("altere", "Sweep the learning rate"))


# --- Vérification mot pour mot ---------------------------------------------------------------------------------------

@pytest.mark.parametrize("extrait", [
    "dense baseline at matched compute",
    "dense   baseline\nat matched\tcompute",                # espacements quelconques
    "  dense baseline at matched compute \n",              # bords
    "dense baseline at matched compute",         # espace insécable, espace cadratin
    "compute; three random seeds\nCOST: 120",             # à travers une fin de ligne du texte
])
def test_extrait_verifie_a_la_normalisation_des_espaces_pres(extrait):
    v = av.verifier_extrait(extrait, PLAN[0])
    assert v.verifie and v.motif is None and len(v.occurrences) == 1


@pytest.mark.parametrize("extrait,motif", [
    ("Dense baseline at matched compute", "introuvable"),               # casse
    ("dense baseline at matched compute: three", "introuvable"),       # ponctuation
    ("dense baseline at matched-compute", "introuvable"),              # tiret au lieu d'une espace
    ("dense​baseline at matched compute", "introuvable"),          # espace sans chasse : pas un espacement
    ("**dense baseline** at matched compute", "introuvable"),          # markdown
    ("dense baseline at matched computation", "introuvable"),          # paraphrase
    ("", "vide"),
    (" \n\t ", "vide"),
    (None, "absent"),
])
def test_extrait_non_verifie(extrait, motif):
    v = av.verifier_extrait(extrait, PLAN[0])
    assert not v.verifie and motif in v.motif and v.occurrences == ()


def test_apostrophes_et_formes_unicode_non_normalisees():
    texte = "the model’s café baseline"
    assert av.verifier_extrait("model’s", texte).verifie
    assert not av.verifier_extrait("model's", texte).verifie                    # apostrophe droite ≠ typographique
    assert not av.verifier_extrait(unicodedata.normalize("NFD", "café"), texte).verifie   # NFD ≠ NFC


def test_positions_dans_le_texte_d_origine_et_bornes_de_mots():
    texte = "x  dense\n\n  baseline y; baselines"
    v = av.verifier_extrait("dense baseline", texte)
    (o,) = v.occurrences
    assert texte[o.debut:o.fin] == "dense\n\n  baseline" and o.debut_de_mot and o.fin_de_mot
    v = av.verifier_extrait("line", texte)
    assert [texte[o.debut:o.fin] for o in v.occurrences] == ["line", "line"]
    assert [(o.debut_de_mot, o.fin_de_mot) for o in v.occurrences] == [(False, True), (False, False)]


def test_occurrences_chevauchantes_toutes_rendues():
    assert len(av.verifier_extrait("aa", "aaa").occurrences) == 2


def test_longueur_minimale():
    assert av.verifier_extrait("seeds", PLAN[0], longueur_min=5).verifie
    v = av.verifier_extrait("seeds", PLAN[0], longueur_min=6)
    assert not v.verifie and "trop court" in v.motif
    for mauvais in (0, -1, 1.5, True):
        with pytest.raises(GardeArret, match="longueur_min"):
            av.verifier_extrait("seeds", PLAN[0], longueur_min=mauvais)


def test_types_refuses():
    with pytest.raises(GardeArret, match="extrait de type"):
        av.verifier_extrait(["seeds"], PLAN[0])
    with pytest.raises(GardeArret, match="texte lu"):
        av.verifier_extrait("seeds", None)
    with pytest.raises(GardeArret):
        av.normaliser_espaces(3)


def test_extrait_a_cheval_sur_deux_segments_verifie_sans_segment_porteur():
    pont = "is more stable. ACTION: ADD TITLE: Held-out"
    assert not av.verifier_extrait(pont, PLAN[0]).verifie
    assert av.verifier_extrait(pont, av.texte_du_plan(PLAN)).verifie
    assert av.segments_porteurs(pont, PLAN) == []
    assert av.segments_porteurs("three random seeds", PLAN) == [0]


@pytest.mark.parametrize("segments", [[], "un texte", ["ok", "  \n"], ["ok", 3]])
def test_plan_mal_forme_refuse(segments):
    with pytest.raises(GardeArret, match="plan"):
        av.texte_du_plan(segments)


# --- Lecture stricte -------------------------------------------------------------------------------------------------

def test_lecture_stricte_non_etaye_compte_absent():
    texte = av.texte_du_plan(PLAN)
    l = av.lecture_stricte(_lecture(c1=("conforme", "dense baseline at matched compute"),
                                    c2=("conforme", "five random seeds"), c3=("altere", None)), texte, REFERENCE)
    assert l["presents"] == ["c1"] and l["conformes"] == ["c1"] and l["non_etayes"] == ["c2", "c3"]
    assert l["controles"]["c2"]["statut_lu"] == "conforme" and l["controles"]["c2"]["statut_strict"] == "absent"


def test_lecture_incomplete_ou_mal_formee_refusee():
    texte = av.texte_du_plan(PLAN)
    manque = _lecture()
    del manque["c5"]
    with pytest.raises(GardeArret, match="manquants \\['c5'\\]"):
        av.lecture_stricte(manque, texte, REFERENCE)
    trop = _lecture()
    trop["c9"] = {"statut": "absent"}
    with pytest.raises(GardeArret, match="en trop \\['c9'\\]"):
        av.lecture_stricte(trop, texte, REFERENCE)
    with pytest.raises(GardeArret, match="statut"):
        av.lecture_stricte(_lecture(c1=("present", "x")), texte, REFERENCE)


@pytest.mark.parametrize("reference,motif", [
    ([], "liste non vide"),
    ([{"id": "c1", "description": "x"}, {"id": "c1", "description": "y"}], "en double"),
    ([{"id": "c1", "description": "  "}], "sans description"),
    ([{"description": "x"}], "identifiant"),
])
def test_reference_mal_formee_refusee(reference, motif):
    with pytest.raises(GardeArret, match=motif):
        av.lecture_stricte({}, "x", reference)


# --- Artefact : retrait ----------------------------------------------------------------------------------------------

def _retrait(**kw):
    args = dict(tache="t1", segments=PLAN, reference=REFERENCE, controle="c2", extraits=EXTRAITS_A,
                lignee_extraits="A")
    args.update(kw)
    return av.artefact_retrait(**args)


def test_retrait_sain_et_son_attendu():
    a = _retrait()
    assert a.nature == "retrait" and a.segments == tuple(PLAN[1:]) and a.segments_source == tuple(PLAN)
    assert a.attendu["cible"] == "c2" and a.attendu["absents"] == ["c1", "c2"] and a.attendu["collateraux"] == ["c1"]
    assert a.attendu["inchanges"] == ["c3", "c4"] and a.attendu["sans_extrait"] == ["c5"]
    assert a.attendu["segments_retires"] == [0]
    assert "three random seeds" not in a.texte and a.provenance["lignee_extraits"] == "A"


def test_retrait_detecte_par_un_lecteur_sain_de_l_autre_lignee():
    a = _retrait()
    lu = _lecture(c3=("conforme", "a synthetic task with known ground truth"),
                  c4=("altere", "Sweep the learning rate"))
    r = av.evaluer_artefact(a, lu, "B", lecture_source=LECTURE_SOURCE_B)
    assert r["detecte"] and r["collateraux_non_absents"] == [] and r["inchanges_changes"] == []


def test_retrait_complaisance_avec_l_extrait_retire_rattrapee_par_le_programme():
    """Le lecteur dit « conforme » en citant le passage retiré : non étayé, donc absent en lecture stricte."""
    r = av.evaluer_artefact(_retrait(), _lecture(c2=("conforme", "three random seeds")), "B")
    assert r["detecte"] and r["non_etayes"] == ["c2"]


def test_retrait_complaisance_avec_un_extrait_d_ailleurs_non_detectee():
    """Le lecteur rattache le contrôle retiré à un autre passage, vérifié : l'épreuve échoue (le vérificateur peut
    échouer, et l'évaluation le dit)."""
    lu = _lecture(c2=("conforme", "Sweep the learning rate"), c3=("conforme", "a synthetic task"))
    r = av.evaluer_artefact(_retrait(), lu, "B", lecture_source=LECTURE_SOURCE_B)
    assert not r["detecte"] and r["inchanges_changes"] == ["c4"]


def test_retrait_lu_par_la_lignee_qui_a_cite_l_extrait_refuse():
    with pytest.raises(GardeArret, match="ses propres extraits"):
        av.evaluer_artefact(_retrait(), _lecture(), "A")


@pytest.mark.parametrize("kw,motif", [
    ({"controle": "c5"}, "sans extrait"),
    ({"extraits": {**EXTRAITS_A, "c2": "five random seeds"}}, "non vérifié dans le plan source"),
    ({"extraits": {**EXTRAITS_A, "c9": "three random seeds"}}, "hors de la référence"),
    ({"segments": [PLAN[0]], "extraits": {"c2": "three random seeds"}}, "plan vide"),
    ({"lignee_extraits": " "}, "lignée"),
    ({"extraits": {"c2": "stable. ACTION: ADD"}}, "à cheval"),
    ({"extraits_temoins": {"c2": ["random seeds\nCOST: 120", "Sweep the learning rate"]}}, "restent dans le plan"),
    ({"extraits_temoins": {"c2": "three random seeds"}}, "liste attendue"),
])
def test_retrait_gardes(kw, motif):
    with pytest.raises(GardeArret, match=motif):
        _retrait(**kw)


def test_retrait_extrait_recree_a_la_jointure_refuse():
    segments = ["x beta", "beta epsilon here", "epsilon y"]
    ref = [{"id": "k", "description": "un contrôle"}]
    assert av.segments_porteurs("beta epsilon", segments) == [1]
    with pytest.raises(GardeArret, match="jointure"):
        av.artefact_retrait("t", segments, ref, "k", {"k": "beta epsilon"}, "A")


def test_retrait_temoin_qui_ne_survit_pas_accepte_et_classe():
    a = _retrait(extraits_temoins={"c5": ["Compare top-1 and top-2 routing"]})
    assert a.attendu["absents"] == ["c1", "c2", "c5"] and a.attendu["sans_extrait"] == []


# --- Artefact : référence permutée -----------------------------------------------------------------------------------

REFERENCE_AUTRE = [
    {"id": "d1", "description": "Comparison with a convolutional baseline on ImageNet"},
    {"id": "d2", "description": "Multiple  random seeds"},           # même description que c2 (espaces)
    {"id": "d3", "description": "Human evaluation of generated captions"},
    {"id": "d4", "description": "Ablation of the vision encoder"},
]


def test_derangement_sans_point_fixe_reproductible_et_independant_de_l_ordre():
    ids = [f"t{k}" for k in range(6)]
    d = av.derangement(ids, 7)
    assert sorted(d) == sorted(d.values()) == ids and all(d[i] != i for i in ids)
    assert av.derangement(list(reversed(ids)), 7) == d
    assert len({tuple(sorted(av.derangement(ids, g).items())) for g in range(10)}) > 1
    assert av.derangement(["a", "b"], 3) == {"a": "b", "b": "a"}


@pytest.mark.parametrize("ids,graine,motif", [
    (["a"], 1, "au moins deux"), (["a", "a"], 1, "double"), (["a", "b"], -1, "graine"), (["a", "b"], True, "graine"),
])
def test_derangement_gardes(ids, graine, motif):
    with pytest.raises(GardeArret, match=motif):
        av.derangement(ids, graine)


def test_reference_permutee_et_son_attendu():
    a = av.artefact_reference_permutee("t1", PLAN, "t2", REFERENCE_AUTRE, REFERENCE, graine=7)
    assert a.tache_plan == "t1" and a.tache_reference == "t2" and a.segments == tuple(PLAN)
    assert a.attendu["communs_avec_la_reference_propre"] == ["d2"] and a.attendu["etrangers"] == ["d1", "d3", "d4"]
    lecture = {c["id"]: {"statut": "absent", "extrait": None} for c in REFERENCE_AUTRE}
    r = av.evaluer_artefact(a, lecture, "B", part_max=0.2)
    assert r["detecte"] and r["part_presents"] == 0.0
    lecture["d1"] = {"statut": "conforme", "extrait": "dense baseline at matched compute"}   # complaisance étayée
    lecture["d4"] = {"statut": "altere", "extrait": "Router ablation"}
    r = av.evaluer_artefact(a, lecture, "B", part_max=0.2)
    assert not r["detecte"] and math.isclose(r["part_presents"], 2 / 3)
    lecture["d4"] = {"statut": "altere", "extrait": "vision encoder"}                        # non étayé
    r = av.evaluer_artefact(a, lecture, "B", part_max=0.34)
    assert r["detecte"] and r["non_etayes"] == ["d4"]


@pytest.mark.parametrize("part_max", [None, 1.0, -0.1, True, "0.2"])
def test_reference_permutee_seuil_exige(part_max):
    a = av.artefact_reference_permutee("t1", PLAN, "t2", REFERENCE_AUTRE, REFERENCE)
    lecture = {c["id"]: {"statut": "absent", "extrait": None} for c in REFERENCE_AUTRE}
    with pytest.raises(GardeArret, match="part_max"):
        av.evaluer_artefact(a, lecture, "B", part_max=part_max)


def test_reference_permutee_gardes():
    with pytest.raises(GardeArret, match="propre référence"):
        av.artefact_reference_permutee("t1", PLAN, "t1", REFERENCE_AUTRE, REFERENCE)
    copie = [{"id": f"x{k}", "description": c["description"].upper()} for k, c in enumerate(REFERENCE)]
    with pytest.raises(GardeArret, match="aucun contrôle étranger"):
        av.artefact_reference_permutee("t1", PLAN, "t2", copie, REFERENCE)


def test_artefacts_reference_permutee_par_derangement():
    plans = {"t1": PLAN, "t2": PLAN[1:], "t3": PLAN[:2]}
    refs = {"t1": REFERENCE, "t2": REFERENCE_AUTRE, "t3": [{"id": "e1", "description": "Bootstrap intervals"}]}
    arts = av.artefacts_reference_permutee(plans, refs, graine=11)
    assert [a.tache_plan for a in arts] == ["t1", "t2", "t3"]
    assert all(a.tache_reference != a.tache_plan for a in arts)
    assert all(a.reference == tuple(refs[a.tache_reference]) and a.segments == tuple(plans[a.tache_plan])
               for a in arts)
    assert all(a.provenance["graine_derangement"] == 11 for a in arts)
    with pytest.raises(GardeArret, match="tâches différentes"):
        av.artefacts_reference_permutee(plans, {"t1": REFERENCE, "t2": REFERENCE_AUTRE}, graine=11)


# --- Artefact : troncature -------------------------------------------------------------------------------------------

F = 0.66      # 83 mots, 54 gardés : coupe juste après « ground truth » (deuxième segment)


def test_troncature_coupe_aux_mots_et_garde_le_texte_d_origine():
    n = sum(len(s.split()) for s in PLAN)
    a = av.artefact_troncature("t1", PLAN, REFERENCE, F, EXTRAITS_A, "A")
    k = math.floor(F * n)
    assert a.attendu["mots_gardes"] == k and a.attendu["mots_source"] == n
    assert len(av.texte_du_plan(a.segments).split()) == k
    assert a.texte_source.startswith(a.texte) and not a.texte[-1].isspace()
    assert a.texte.endswith("known ground truth")
    assert a.segments[0] == PLAN[0] and len(a.segments) == 2
    assert a.attendu["perdus"] == ["c4"] and a.attendu["conserves"] == ["c1", "c2", "c3"]
    assert a.attendu["sans_extrait"] == ["c5"]


def test_troncature_a_la_frontiere_d_un_segment():
    n0 = len(PLAN[0].split())
    n = sum(len(s.split()) for s in PLAN)
    a = av.artefact_troncature("t1", PLAN, REFERENCE, (n0 + 0.5) / n)
    assert a.segments == (PLAN[0],) and a.attendu["perdus"] == [] and a.attendu["sans_extrait"] == list(
        c["id"] for c in REFERENCE)


def test_troncature_detectee_ou_non_selon_la_lecture():
    a = av.artefact_troncature("t1", PLAN, REFERENCE, F, EXTRAITS_A, "A")
    sain = _lecture(c1=("conforme", "dense baseline at matched compute"), c2=("conforme", "three random seeds"),
                    c3=("conforme", "synthetic task with known ground truth"))
    r = av.evaluer_artefact(a, sain, "B", lecture_source=LECTURE_SOURCE_B)
    assert r["detecte"] and r["couverture_non_croissante"] and r["perdus_lus_presents"] == [] and r["gains"] == []
    # le contrôle perdu lu présent en citant le passage coupé : non étayé, rattrapé par le programme
    r = av.evaluer_artefact(a, {**sain, "c4": {"statut": "altere", "extrait": "Sweep the learning rate"}}, "B",
                            lecture_source=LECTURE_SOURCE_B)
    assert r["detecte"] and r["non_etayes"] == ["c4"]
    # lecture plus généreuse sur le plan coupé que sur le plan entier : non détecté
    gonfle = {**sain, "c5": {"statut": "conforme", "extrait": "Compare top-1 and top-2 routing"},
              "c4": {"statut": "conforme", "extrait": "Held-out evaluation"}}
    r = av.evaluer_artefact(a, gonfle, "B", lecture_source=LECTURE_SOURCE_B)
    assert not r["detecte"] and r["gains"] == ["c5"] and r["perdus_lus_presents"] == ["c4"]


@pytest.mark.parametrize("fraction", [0.0, 1.0, -0.2, 1.5, float("nan"), True, "0.5", 1e-6])
def test_troncature_fraction_refusee(fraction):
    with pytest.raises(GardeArret, match="fraction|troncature"):
        av.artefact_troncature("t1", PLAN, REFERENCE, fraction)


def test_troncature_gardes():
    with pytest.raises(GardeArret, match="sans extraits"):
        av.artefact_troncature("t1", PLAN, REFERENCE, 0.5, lignee_extraits="A")
    with pytest.raises(GardeArret, match="lignée"):
        av.artefact_troncature("t1", PLAN, REFERENCE, 0.5, EXTRAITS_A)
    a = av.artefact_troncature("t1", PLAN, REFERENCE, 0.5)
    with pytest.raises(GardeArret, match="lecture du plan source"):
        av.evaluer_artefact(a, _lecture(), "B")


# --- Aveuglement et empreintes ---------------------------------------------------------------------------------------

def test_vue_aveugle_sans_nature_ni_attendu():
    for a in (_retrait(), av.artefact_troncature("t1", PLAN, REFERENCE, 0.5, EXTRAITS_A, "A"),
              av.artefact_reference_permutee("t1", PLAN, "t2", REFERENCE_AUTRE, REFERENCE)):
        v = a.vue_aveugle()
        assert set(v) == {"plan", "reference"} and v["plan"] == a.texte
        assert a.nature not in repr(v) and "attendu" not in repr(v)
    assert "three random seeds" not in _retrait().vue_aveugle()["plan"]


def test_empreinte_stable_et_sensible():
    a, b = _retrait(), _retrait()
    assert a.empreinte == b.empreinte and a.identifiant == b.identifiant and a.identifiant.startswith("retrait/t1/")
    assert _retrait(controle="c3").empreinte != a.empreinte
    t1 = av.artefact_troncature("t1", PLAN, REFERENCE, 0.5)
    t2 = av.artefact_troncature("t1", PLAN, REFERENCE, 0.75)
    assert t1.empreinte != t2.empreinte


def test_nature_inconnue_refusee():
    a = _retrait()
    a.nature = "autre"
    with pytest.raises(GardeArret, match="nature"):
        av.evaluer_artefact(a, _lecture(), "B")
