import json

import pytest

from conftest import committer
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import verifier_resultat
from controle_ia.run_factice import executer


def test_sain_chaine_et_rejeu(depot):
    sortie = executer(depot, "20261004-120000-factice", entropie=2026)
    assert sortie["rejeu"] == "identique"
    # même entropie, autre run : mêmes tirages au bit près
    committer(depot)
    autre = executer(depot, "20261004-120001-factice", entropie=2026)
    a = json.loads(open(sortie["resultat"]).read())["resultat"]
    b = json.loads(open(autre["resultat"]).read())["resultat"]
    assert a == b


def test_artefact_resultat_altere(depot):
    sortie = executer(depot, "20261004-120000-factice", entropie=1)
    chemin = sortie["resultat"]
    corps = json.loads(open(chemin).read())
    corps["resultat"]["tirage-a"]["moyenne"] += 1e-12
    open(chemin, "w").write(json.dumps(corps))
    with pytest.raises(GardeArret, match="empreinte"):
        verifier_resultat(depot, chemin)
