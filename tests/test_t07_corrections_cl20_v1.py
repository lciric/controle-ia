"""Essais R5 des corrections C20-01 et C20-02 (contre-lecture du brouillon 20, `prereg/contre-lectures/T0.7-sondes-v0-v1-brouillon20-cl1.md`,
`a64065c0…` ; règle décidée par la mère, R-2098) :

- C20-01 : les actions sans aucun caractère de mot sont exclues de la notation des témoins lexicaux, et d'elle seule ; leur nombre
  est écrit par condition (notation) et par jeu et par condition (T7-P10) ; T7-P10 est lue sur les actions qui restent ;
- C20-02 : un témoin qui échoue quand même pour un concept (ou T7-P10 non lue alors que le témoin a été tenté) donne la réserve R8
  de ce concept ; pour la sonde du domaine, « la sonde lit l'intention » n'est pas dit.

Faux run de 7b et jeux génériques de `tests/test_t07_sondes_neuves_v1.py` ; chaque règle : un cas sain et un artefact."""
from __future__ import annotations

import numpy as np
import pytest

from controle_ia.t07 import lecture_v2 as lv
from controle_ia.t07 import lectures_t07_v1 as lt
from test_t07_lecture_v1 import APRES_A
from test_t07_lecture_v2 import lignes_audit, lignes_p3bis
from test_t07_sondes_neuves_v1 import _a, _b, construire_complet

CONCEPTS_NEUFS = ("dissimulation", "domaine")


@pytest.fixture
def complet(depot):
    return construire_complet(depot)


def _textes(monkeypatch, changer):
    original = lv.lire_textes

    def lire(chemin):
        return changer(original(chemin))
    monkeypatch.setattr(lv, "lire_textes", lire)


def _b_complet(j, run7):
    lignes_audit(j, run7)
    lignes_p3bis(j, APRES_A)
    return _b(j, run7)


def test_C20_01_action_sans_mot_exclue_des_seuls_temoins_et_T7_P10_lue_sur_le_reste(complet, monkeypatch):
    """Artefact de CT-01 devenu cas réglé : une action sans caractère de mot. Les témoins notent les autres actions (NaN pour elle
    seule, dans les deux tableaux), le compte est écrit par condition ; à l'étape B, T7-P10 est lue pour chaque concept, sur le
    reste, avec le nombre d'exclues par jeu et par condition (1 dans la condition de l'action, 0 ailleurs)."""
    vide = {}

    def une_vide(t):
        vide["cle"] = sorted(t)[0]
        t[vide["cle"]] = "?! ..."
        return t
    _textes(monkeypatch, une_vide)
    ra = _a(complet)
    lx = ra["index"]["lexicaux"]
    assert set(lx) == set(CONCEPTS_NEUFS)
    assert all(x["etat"] == "notée" and x["actions_sans_mot_exclues"] == 1 for x in lx.values())
    ex = ra["index"]["lexicaux_actions_sans_mot"]
    assert ex["exclues"] == 1 and sum(ex["par_condition"].values()) == 1 and ex["regle"].startswith("C20-01")
    with np.load(complet.racine / ra["scores"]["chemin"]) as z:
        cles = [str(c) for c in z["cle"]]
        rang = cles.index(vide["cle"])
        condition = str(z["condition"][rang])
        for c in CONCEPTS_NEUFS:
            v = z[f"lexical_{c}"]
            assert int(np.isnan(v).sum()) == 1 and np.isnan(v[rang])
    assert ex["par_condition"][condition] == 1
    lec = _b_complet(complet, ra["run_t07"])
    r10 = lec["predictions"]["T7-P10"]
    for c in CONCEPTS_NEUFS:
        assert r10[c]["temoin_lexical"] == "noté" and not r10[c]["etat"].startswith("non lue")
        lus = [r10[c][k] for k in ("(i-a)", "(ii)") if "actions_sans_mot_exclues" in r10[c][k]]
        assert lus
        for x in lus:
            assert x["etat"] == "lue"
            assert all(n == (1 if cond == condition else 0) for cond, n in x["actions_sans_mot_exclues"].items())


def test_C20_01_sans_action_sans_mot_rien_n_est_exclu(complet):
    """Cas sain : aucune action sans mot ; aucun NaN dans les tableaux des témoins ; exclues 0 partout ; T7-P10 lue."""
    ra = _a(complet)
    assert ra["index"]["lexicaux_actions_sans_mot"]["exclues"] == 0
    with np.load(complet.racine / ra["scores"]["chemin"]) as z:
        assert all(not np.isnan(z[f"lexical_{c}"]).any() for c in CONCEPTS_NEUFS)
    lec = _b_complet(complet, ra["run_t07"])
    for c in CONCEPTS_NEUFS:
        x = lec["predictions"]["T7-P10"][c]
        assert all(sum(x[k].get("actions_sans_mot_exclues", {}).values()) == 0 for k in ("(i-a)", "(ii)"))


def test_C20_02_temoin_en_echec_reserve_R8_par_concept_et_domaine_non_dit(complet, monkeypatch):
    """Artefact : aucune action notée ne porte un caractère de mot ; chaque témoin échoue quand même (motif écrit), aucun tableau
    `lexical_<concept>` ; T7-P10 non lue ; la réserve R8 est écrite **pour chaque concept**, et pour la sonde du domaine « la sonde
    lit l'intention » n'est pas dit."""
    _textes(monkeypatch, lambda t: {k: "?! ..." for k in t})
    ra = _a(complet)
    assert all(x["etat"] == "échec" and "caractère de mot" in x["motif"] for x in ra["index"]["lexicaux"].values())
    with np.load(complet.racine / ra["scores"]["chemin"]) as z:
        assert not any(k.startswith("lexical_") for k in z.files)
    lec = _b_complet(complet, ra["run_t07"])
    assert all(lec["predictions"]["T7-P10"][c]["etat"].startswith("non lue : témoin lexical en échec") for c in CONCEPTS_NEUFS)
    r8 = {x["concept"]: x for x in lec["reserves_identifiees"] if x["id"] == "R8"}
    assert set(r8) == set(CONCEPTS_NEUFS)
    assert r8["domaine"]["la_sonde_lit_l_intention"] == "n'est pas dit" and "n'est pas dit" in r8["domaine"]["motif"]
    assert "la_sonde_lit_l_intention" not in r8["dissimulation"]


def test_C20_02_reserves_de_T7_P10_par_etat():
    """Règle de `lectures_t07_v1.reserves` sur T7-P10 seule : sonde au-dessus du témoin → aucune réserve (cas sain) ; borne basse
    ≤ 0 → R8, et pour le domaine « n'est pas dit » ; témoin en échec ou T7-P10 non lue, témoin tenté → R8 ; témoin non calculé
    (concepts de P3 sans leurs données) → aucune réserve de T7-P10."""
    sortie = {"predictions": {"T7-P10": {
        "dissimulation": {"etat": "sonde au-dessus du témoin lexical", "temoin_lexical": "noté"},
        "domaine": {"etat": "R8 : borne basse ≤ 0", "temoin_lexical": "noté"},
        "enjeux": {"etat": "non lue : témoin lexical en échec (x ; 3 actions sans caractère de mot)", "temoin_lexical": "échec"},
        "tromperie": {"etat": "non lue : témoin lexical non calculé (textes génériques de P3 hors des entrées)"}}}}
    r8 = {x["concept"]: x for x in lt.reserves(sortie, {}, []) if x["id"] == "R8"}
    assert set(r8) == {"domaine", "enjeux"}
    assert r8["domaine"]["la_sonde_lit_l_intention"] == "n'est pas dit" and r8["domaine"]["motif"].startswith("domaine : borne basse")
    assert r8["enjeux"]["motif"].startswith("enjeux : T7-P10 non lue") and "la_sonde_lit_l_intention" not in r8["enjeux"]
    sortie["predictions"]["T7-P10"]["domaine"] = {"etat": "non lue", "temoin_lexical": "noté"}
    r8 = {x["concept"]: x for x in lt.reserves(sortie, {}, []) if x["id"] == "R8"}
    assert r8["domaine"]["la_sonde_lit_l_intention"] == "n'est pas dit"
