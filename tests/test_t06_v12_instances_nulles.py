"""Texte réel de Vast pour une instance détruite (E3, 22:27:24Z) : `vastai show instance <ID> --raw` rend, en code 0, `{"instances": null}` sur trois lignes.
Ce texte seul est une absence PROBABLE (non concluante) ; l'absence n'est établie que par une liste d'inventaire non vide sans l'instance, à deux relevés.
Cas sains et artefacts (R5) : module `session_v10` et surveillance du lanceur v11."""
from __future__ import annotations

import pytest

from controle_ia.t06 import session_v10 as s10
from controle_ia.t06.session import GardeSession
import test_t06_v12_nouveaux_v10 as n
from test_t06_v12_amorce import JOURNAL_BON
from test_t06_v12_nouveaux_v10 import LANCEUR9, VASTAI_V9, _surv

TEXTE_REEL = '{\n  "instances": null\n}\n'
VASTAI_V11 = VASTAI_V9.replace("        vide) echo '{}' ;;", """        vide) echo '{}' ;;
        instancesnul) printf '{\\n  "instances": null\\n}\\n' ;;""", 1)
assert VASTAI_V11 != VASTAI_V9


def test_texte_reel_est_une_absence_probable_non_concluante():
    assert s10.absence_probable(TEXTE_REEL)
    with pytest.raises(GardeSession, match="absence probable"):
        s10.instance_seule(TEXTE_REEL, "59623267")


@pytest.mark.parametrize("texte", ['{"id": null}', '{"instances": []}', '{"instances": {}}', '{"instances": null, "autre": 1}', 'null', '{}', 'Internal Server Error 500',
                                   '{"success": false, "status": 404, "msg": "autre message"}'])
def test_les_autres_reponses_restent_non_concluantes_ou_inchangees(texte):
    assert not s10.absence_probable(texte)
    with pytest.raises(GardeSession):
        s10.instance_seule(texte, "59623267")


def test_absence_etablie_inchangee_pour_un_404_exact_et_instance_presente():
    assert s10.instance_seule('{"success": false, "status": 404, "msg": "Not Found"}', "5") is False        # v9 inchangé
    assert s10.instance_seule('{"id": 5, "x": 1}', "5") is True


def test_cas_sain_liste_non_vide_sans_l_instance_a_deux_releves_donne_arret_mort(tmp_path):
    (tmp_path / "a").mkdir()
    code, sortie, d = _surv(tmp_path / "a", LANCEUR9, JOURNAL_BON, {"FAUX_LISTE": "autre", "FAUX_SEULE": "instancesnul"}, vastai=VASTAI_V11)
    assert code == 3 and "ARRET mort" in sortie, sortie[-800:]


@pytest.mark.parametrize("liste", ["vide", "nul", "illisible", "panne"])
def test_artefact_texte_reel_sans_liste_non_vide_n_est_jamais_une_absence_etablie(tmp_path, liste):
    (tmp_path / "b").mkdir()
    code, sortie, d = _surv(tmp_path / "b", LANCEUR9, JOURNAL_BON, {"FAUX_LISTE": liste, "FAUX_SEULE": "instancesnul", "INTERVALLE": "1"}, vastai=VASTAI_V11, duree=60)
    assert code == 3 and "ARRET inventaire" in sortie and "ARRET mort" not in sortie, (liste, sortie[-900:])
    assert "absence probable" in (d / "surveillance.txt").read_text(encoding="utf-8")


# --- essai 11 : l'identifiant du message est comparé -------------------------------------------------------------------------------------------
@pytest.mark.parametrize("texte, ident, attendu", [
    ("Error 404: instance 123 not found", "123", False),            # cas sain : le message nomme l'instance demandée → absence établie
    ("404 instance 999 not found", "123", "non concluant"),         # artefact : autre instance → non concluant
    ("Error 404: instance 12 not found", "123", "non concluant"),   # 12 n'est pas 123 (pas de comparaison par préfixe)
    ("404 not found", "123", False),                                # sans identifiant : comportement de session_v9 inchangé
])
def test_essai_11_identifiant_du_message_compare_a_celui_demande(texte, ident, attendu):
    if attendu is False:
        assert s10.instance_seule(texte, ident) is False
    else:
        with pytest.raises(GardeSession, match=attendu):
            s10.instance_seule(texte, ident)
