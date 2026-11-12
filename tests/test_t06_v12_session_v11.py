"""`session_v11` (contre-lecture de la v11, R-1746) : un identifiant différent de celui demandé n'est JAMAIS une absence établie. `show instance 123` qui rend `{"id": 456}`,
`{"instances": {"id": 456}}`, `[{"id": 456}]` ou une liste avec 456 est non concluant (en v9 et v10 : « absence établie », donc `ARRET mort` après deux relevés). L'absence reste établie par un 404 exact.
Cas sain et artefact (R5) : unités, puis lanceur."""
from __future__ import annotations

import pytest

from controle_ia.t06 import session_v10 as s10
from controle_ia.t06 import session_v11 as s11
from controle_ia.t06.session import GardeSession
from test_t06_v12_amorce import JOURNAL_BON
from test_t06_v12_instances_nulles import VASTAI_V11
from test_t06_v12_nouveaux_v10 import LANCEUR9, _surv

AUTRES = ['{"id": 456}', '{"instances": {"id": 456}}', '{"instances": [{"id": 456}]}', '[{"id": 456}]', '[{"id": 456}, {"id": 789}]', '{"id": 456, "label": "autre"}']


@pytest.mark.parametrize("texte", AUTRES)
def test_un_autre_identifiant_est_non_concluant(texte):
    with pytest.raises(GardeSession, match="non concluante"):
        s11.instance_seule(texte, "123")


@pytest.mark.parametrize("texte", AUTRES)
def test_artefact_v9_et_v10_concluaient_a_tort_a_l_absence(texte):
    assert s10.instance_seule(texte, "123") is False                     # le défaut de la v10 (hérité de la v9) : « absence établie »


@pytest.mark.parametrize("texte", ['{"id": 123}', '{"instances": {"id": 123}}', '[{"id": 123}]', '[{"id": 456}, {"id": 123}]', '{"id": "123"}'])
def test_cas_sain_l_instance_demandee_repond(texte):
    assert s11.instance_seule(texte, "123") is True


@pytest.mark.parametrize("texte", ['{"success": false, "status": 404, "msg": "Not Found"}', "Error 404: instance 123 not found", "404 not found"])
def test_le_404_exact_reste_une_absence_etablie(texte):
    assert s11.instance_seule(texte, "123") is False


@pytest.mark.parametrize("texte", ['{"instances": null}', '{"id": null}', "", "boum", '{}', '[]', '{"instances": []}'])
def test_les_autres_reponses_restent_non_concluantes(texte):
    with pytest.raises(GardeSession):
        s11.instance_seule(texte, "123")


def test_identifiants_nommes():
    assert s11.identifiants_nommes({"instances": [{"id": 1}, {"id": 2}]}) == ["1", "2"] and s11.identifiants_nommes({"a": 1}) == [] and s11.identifiants_nommes(None) == []


VASTAI_V12 = VASTAI_V11.replace("        vide) echo '{}' ;;", """        vide) echo '{}' ;;
        autreid) echo '{"id": 456}' ;;
        autreliste) echo '[{"id": 456}]' ;;
        instancesautre) echo '{"instances": {"id": 456}}' ;;""", 1)
assert VASTAI_V12 != VASTAI_V11


@pytest.mark.parametrize("seule", ["autreid", "autreliste", "instancesautre"])
def test_lanceur_un_autre_identifiant_donne_arret_inventaire_jamais_arret_mort(tmp_path, seule):
    (tmp_path / "a").mkdir()
    code, sortie, d = _surv(tmp_path / "a", LANCEUR9, JOURNAL_BON, {"FAUX_LISTE": "vide", "FAUX_SEULE": seule, "INTERVALLE": "1"}, vastai=VASTAI_V12, duree=60)
    assert code == 3 and "ARRET inventaire" in sortie and "ARRET mort" not in sortie, (seule, sortie[-800:])


def test_lanceur_cas_sain_l_instance_demandee_n_arrete_rien(tmp_path):
    (tmp_path / "b").mkdir()
    code, sortie, d = _surv(tmp_path / "b", LANCEUR9, JOURNAL_BON, {"FAUX_LISTE": "vide", "FAUX_SEULE": "repond"}, vastai=VASTAI_V12, duree=8)
    assert code is None or code == 0
    assert "ARRET" not in sortie
