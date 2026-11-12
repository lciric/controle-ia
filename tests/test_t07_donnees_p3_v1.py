"""Essais R5 des données de P3 pour T7-P10 de la tromperie et des enjeux (`src/controle_ia/t07/donnees_p3_t07_v1.py` ; brouillon
19, plan, point 10 : témoin lexical « entraîné sur les données de P3 à la provenance scellée, même découpage que P3 »).

Les quatre fichiers réels (faits, enjeux, manifeste et résultat du run de P3 ; rien de 7a, rien sous embargo) sont extraits du
dépôt par `git show` dans un dossier jetable, avec leurs compagnons. Cas sain : découpage de P3 reproduit (478 / 120 et
1 591 / 409, les effectifs de P3), témoins appris, T7-P10 de la tromperie et des enjeux lu à l'étape B ; artefacts : empreinte
fausse → arrêt ; tirage des enjeux différent de celui de P3 → arrêt ; configuration hors forme ou autre que la provenance de P3
en mode réel → arrêt de configuration."""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller
from controle_ia.t07 import donnees_p3_t07_v1 as d3
from controle_ia.t07 import lecture_v2 as lv
from test_t07_lecture_v1 import APRES_A, RUN_T06
from test_t07_lecture_v2 import lignes_audit, lignes_p3bis
from test_t07_sondes_neuves_v1 import _a, _b, _resultat, construire_complet

RACINE_DEPOT = Path(__file__).resolve().parents[1]
CONFIG_V2 = RACINE_DEPOT / "brouillons" / "T0.7-sondes-v0-v1-brouillon19-pieces" / "configuration-t07-v2.json"


def config_reelle() -> dict:
    return {k: {"chemin": d3.CHEMINS_REELS[k], "sha256": d3.SHA_REELLES[k]} for k in d3.CLES}


def extraire_p3(racine: Path) -> None:
    for k in d3.CLES:
        for suffixe in ("", ".sha256"):
            rel = d3.CHEMINS_REELS[k] + suffixe
            p = subprocess.run(["git", "-C", str(RACINE_DEPOT), "show", f"HEAD:{rel}"], capture_output=True)
            if p.returncode != 0:
                pytest.skip(f"{rel} absent du dépôt")
            (racine / rel).parent.mkdir(parents=True, exist_ok=True)
            (racine / rel).write_bytes(p.stdout)


@pytest.fixture(scope="module")
def p3(tmp_path_factory):
    r = tmp_path_factory.mktemp("donnees-p3")
    extraire_p3(r)
    return r


def test_configuration_forme_et_provenance_reelle():
    """Forme de `donnees_p3` ; en mode réel, les chemins et empreintes de la provenance de P3 (cas sain) ; artefacts : clé
    absente, empreinte autre en mode réel → arrêt de configuration ; jouet : autre fichier permis."""
    d = config_reelle()
    d3.exiger_config(d, "reel")
    with pytest.raises(GardeArret, match="clés"):
        d3.exiger_config({k: v for k, v in d.items() if k != "enjeux"}, "reel")
    with pytest.raises(GardeArret, match="attendu en mode réel"):
        d3.exiger_config({**d, "faits": {"chemin": d3.CHEMINS_REELS["faits"], "sha256": "0" * 64}}, "reel")
    d3.exiger_config({**d, "faits": {"chemin": "donnees/x.csv", "sha256": "0" * 64}}, "jouet")


def test_configuration_v2_du_brouillon_19():
    """La configuration v2 (v1 plus `donnees_p3`) passe les contrôles du module, sauf l'entropie, nulle jusqu'au candidat."""
    if not CONFIG_V2.is_file():
        pytest.skip("configuration v2 absente")
    c = json.loads(CONFIG_V2.read_text(encoding="utf-8"))
    assert c["donnees_p3"] == config_reelle()
    with pytest.raises(GardeArret, match="entropie = None"):
        lv.exiger_configuration(c)
    lv.exiger_configuration({**c, "entropie": 1})
    v1 = json.loads((CONFIG_V2.parent / "configuration-t07-v1.json").read_text(encoding="utf-8"))
    assert {k: x for k, x in c.items() if k != "donnees_p3"} == v1


def test_sceaux_et_decoupage_de_p3_reproduit(p3, tmp_path):
    """Sceaux vérifiés ; découpage de P3 reproduit à ses effectifs ; artefacts : empreinte fausse → arrêt ; lignes des enjeux
    écrites par P3 différentes (résultat de P3 retouché et rescellé) → arrêt (R11)."""
    d = config_reelle()
    assert set(d3.controler(p3, d)) == set(d3.CLES)
    x = d3.exemples_p3(p3, d)
    assert (len(x["tromperie"]["e"]), len(x["tromperie"]["v"])) == (478, 120)
    assert (len(x["enjeux"]["e"]), len(x["enjeux"]["v"])) == (1591, 409)
    with pytest.raises(GardeArret, match="empreinte"):
        d3.controler(p3, {**d, "enjeux": {**d["enjeux"], "sha256": "0" * 64}})
    r = json.loads((p3 / d3.CHEMINS_REELS["sondes_figees_p3"]).read_text(encoding="utf-8"))
    r["resultat"]["donnees"]["lignes_enjeux"][0] += 1
    faux = tmp_path / "sondes-figees.json"
    faux.write_text(json.dumps(r), encoding="utf-8")
    sha = sceller(faux)
    with pytest.raises(GardeArret, match="tirage des enjeux"):
        d3.exemples_p3(p3, {**d, "sondes_figees_p3": {"chemin": str(faux), "sha256": sha}})


def test_etape_complete_avec_donnees_p3_T7P10_tromperie_et_enjeux(depot, p3):
    """Étape A complète avec `donnees_p3` : témoins lexicaux de la tromperie et des enjeux appris sur les données et le découpage
    de P3 (le témoin de la tromperie est au hasard : même texte sous les deux étiquettes), notés sur le texte des actions ;
    étape B : T7-P10 lu pour les quatre concepts ; sans la clé (essais de bout en bout du fichier des sondes neuves), il est
    « non lu », motif écrit."""
    j = construire_complet(depot)
    extraire_p3(j.racine)
    j.config["donnees_p3"] = config_reelle()
    ra = _a(j)
    s = _resultat(j, ra["run_t07"], "sondes-t07.json")["sondes_neuves"]
    lx = s["temoins_lexicaux"]
    assert {"tromperie", "enjeux", "dissimulation", "domaine"} <= set(lx)
    assert set(lx["tromperie"]["aires_validation"].values()) == {0.5} and lx["enjeux"]["textes_sans_mot_exclus"]["entrainement"] == 1
    assert lx["enjeux"]["n_entrainement"] == 1590 and lx["enjeux"]["source"] == "données et découpage de P3"
    lignes_audit(j, ra["run_t07"])
    lignes_p3bis(j, APRES_A)
    lec = _b(j, ra["run_t07"])
    r10 = lec["predictions"]["T7-P10"]
    assert all(r10[c]["(i-a)"]["etat"] == "lue" for c in ("tromperie", "enjeux"))
    assert all(not str(r10[c]["etat"]).startswith("non lue") for c in ("tromperie", "enjeux"))
