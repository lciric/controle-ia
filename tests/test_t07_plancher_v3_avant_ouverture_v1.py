"""Essais du dernier tour du plancher v3 de T0.7 (contre-lecture courte des corrections, R-2311) — v1, fichier neuf.

- **CLC-P3-03** (`reextraction_p3_v1.revision_au_cache`, caches factices, hors ligne) : index des poids illisible (JSON faux,
  `weight_map` absente, vide, mal formée, index qui est un dossier) → `GardeArret`, jamais une autre exception ; morceaux
  `model-<i>-of-<n>.safetensors` sans index ; index qui nomme moins de morceaux que leur nom n'en annonce ; morceau ou fichier
  essentiel de taille nulle ; révision donnée par un nom de branche (`refs/main`) : dossier du cache ≠ révision (mutation x3).
  Cas sains : morceaux complets ; un seul `model.safetensors`, sans index.
- **CLC-P3-06** (`controler_avant_ouverture`) : sonde figée absente du fichier léger (mutation x8) ; aucune sonde figée nommée
  (mutation x9).
- **CLC-P3-02** (sous-commande `lecture_v4 controle-avant-ouverture`, jouée par le script v4 à l'étape 8) : jouet, sur un vrai
  run jouet de P3 : code 0, résumé JSON ; artefacts → code 2, motif écrit, rien d'écrit sous la racine (sceau faux, témoin
  absent, sonde figée absente, garde de la principale inconnue, clé `plancher_figees` absente, fichier de configuration absent
  ou illisible, faute hors garde). Réel, sur les fichiers réels de P3 et la configuration v8 : cache factice complet → code 0 ;
  cache absent, index illisible, configuration v7, `n_plancher` 200 → code 2.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.t07 import lecture_v4 as lv4
from controle_ia.t07 import reextraction_p3_v1 as rx
from test_t07_plancher_v3_lecture_v1 import v7, v8
from test_t07_plancher_v3_reextraction_v1 import COMPLET, REV, RUN_P3, _cache, _config, p3  # noqa: F401 (fixture p3)

RACINE_DEPOT = Path(__file__).resolve().parents[1]
MODELE_P3 = "meta-llama/Llama-3.1-8B-Instruct"
REELS_P3 = ("runs/20261019-230011-p3-reel/manifeste.json", "diag/20261019-230011-p3-reel/sondes-figees.json",
            "donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz", "donnees/T0.7-faits-repe-v1/facts_true_false.csv",
            "donnees/T0.7-models-under-pressure-v1/training/train.jsonl")


# ------------------------------------------------------------------------------------------------------------ CLC-P3-03
def _ecrire(base, rel, contenu):
    d = base / ("models--org--nom") / "snapshots" / REV
    (d / rel).write_text(contenu, encoding="utf-8")


@pytest.fixture
def hors_ligne(monkeypatch):
    monkeypatch.setenv("HF_HUB_OFFLINE", "1")


def test_cache_cas_sains(tmp_path, hors_ligne):
    """Morceaux complets ; un seul fichier de poids sans index (forme admise : aucun morceau annoncé)."""
    r = rx.revision_au_cache("org/nom", REV, str(_cache(tmp_path / "morceaux", "org/nom", REV, COMPLET)))
    assert r["poids"] == 2 and r["dossier"].endswith(REV)
    seul = {k: v for k, v in COMPLET.items() if "safetensors" not in k} | {"model.safetensors": "x"}
    r = rx.revision_au_cache("org/nom", REV, str(_cache(tmp_path / "seul", "org/nom", REV, seul)))
    assert r["poids"] == 1


@pytest.mark.parametrize("index, motif", [
    ("{pas du json", "index des poids illisible \\(JSONDecodeError"),
    (json.dumps({"metadata": {}}), "index des poids illisible \\(KeyError"),
    (json.dumps({"weight_map": {}}), "index des poids illisible \\(ValueError : weight_map vide"),
    (json.dumps({"weight_map": ["model-00001-of-00002.safetensors"]}), "index des poids illisible \\(ValueError : weight_map vide ou mal"),
    (json.dumps([1, 2]), "index des poids illisible \\(TypeError"),
])
def test_cache_index_illisible_garde_arret(tmp_path, hors_ligne, index, motif):
    """CLC-P3-03 : toute faute de l'index → `GardeArret` (code 2 à la sous-commande), jamais `JSONDecodeError` ni `KeyError`."""
    base = _cache(tmp_path / "c", "org/nom", REV, COMPLET)
    _ecrire(base, "model.safetensors.index.json", index)
    with pytest.raises(GardeArret, match=motif):
        rx.revision_au_cache("org/nom", REV, str(base))


def test_cache_index_qui_est_un_dossier(tmp_path, hors_ligne):
    """Index présent sous la forme d'un dossier : lu comme absent ; les morceaux sans index sont refusés."""
    base = _cache(tmp_path / "c", "org/nom", REV, {k: v for k, v in COMPLET.items() if k != "model.safetensors.index.json"})
    (base / "models--org--nom" / "snapshots" / REV / "model.safetensors.index.json").mkdir()
    with pytest.raises(GardeArret, match="morceaux sans index"):
        rx.revision_au_cache("org/nom", REV, str(base))


def test_cache_formes_partielles_refusees(tmp_path, hors_ligne):
    """Les trois formes admises par le v3 (contre-lecture courte, § 3 (2)) et leurs voisines, refusées par `GardeArret`."""
    sans_index = {k: v for k, v in COMPLET.items() if k != "model-00002-of-00002.safetensors" and "index" not in k}
    with pytest.raises(GardeArret, match="morceaux sans index"):              # index absent, un morceau sur deux présent
        rx.revision_au_cache("org/nom", REV, str(_cache(tmp_path / "a", "org/nom", REV, sans_index)))
    nul = dict(COMPLET, **{"model-00002-of-00002.safetensors": ""})
    with pytest.raises(GardeArret, match="model-00002-of-00002.safetensors \\(taille nulle\\)"):
        rx.revision_au_cache("org/nom", REV, str(_cache(tmp_path / "b", "org/nom", REV, nul)))
    vide = {k: v for k, v in COMPLET.items() if "safetensors" not in k} | {"model.safetensors.index.json": json.dumps({"weight_map": {}})}
    with pytest.raises(GardeArret, match="weight_map vide"):                   # index à la carte vide, aucun poids
        rx.revision_au_cache("org/nom", REV, str(_cache(tmp_path / "c", "org/nom", REV, vide)))
    un_sur_deux = dict(COMPLET, **{"model.safetensors.index.json": json.dumps({"weight_map": {"a": "model-00001-of-00002.safetensors"}})})
    with pytest.raises(GardeArret, match="nombre annoncé par leurs noms différent"):
        rx.revision_au_cache("org/nom", REV, str(_cache(tmp_path / "d", "org/nom", REV, un_sur_deux)))
    melange = dict(COMPLET, **{"model.safetensors.index.json": json.dumps({"weight_map": {"a": "model-00001-of-00002.safetensors",
                                                                                            "b": "model-00002-of-00003.safetensors"}}),
                               "model-00002-of-00003.safetensors": "x"})
    with pytest.raises(GardeArret, match="nombre annoncé par leurs noms différent"):
        rx.revision_au_cache("org/nom", REV, str(_cache(tmp_path / "e", "org/nom", REV, melange)))
    config_nulle = dict(COMPLET, **{"config.json": ""})
    with pytest.raises(GardeArret, match="config.json \\(taille nulle\\)"):
        rx.revision_au_cache("org/nom", REV, str(_cache(tmp_path / "f", "org/nom", REV, config_nulle)))


def test_cache_revision_par_nom_de_branche_refusee(tmp_path, hors_ligne):
    """Mutation x3 (CLC-P3-06) : la révision « main », résolue par `refs/main` vers le dossier `REV`, est refusée (dossier ≠
    révision demandée) ; la révision exacte passe."""
    base = _cache(tmp_path / "c", "org/nom", REV, COMPLET)
    refs = base / "models--org--nom" / "refs"
    refs.mkdir()
    (refs / "main").write_text(REV, encoding="utf-8")
    with pytest.raises(GardeArret, match=f"dossier du cache {REV[:12]} ≠ révision main"):
        rx.revision_au_cache("org/nom", "main", str(base))
    assert rx.revision_au_cache("org/nom", REV, str(base))["revision"] == REV


# ------------------------------------------------------------------------------------------------------------ CLC-P3-06
def test_controle_sonde_figee_absente_du_fichier_leger(p3, monkeypatch):
    """Mutation x8 : une sonde figée nommée par la configuration et absente du fichier léger → `GardeArret` nommant la sonde
    (non une `KeyError` plus loin)."""
    from controle_ia.premier_test_ia import figees as fg
    vraie = fg.lire_sondes

    def sans_tromperie(*a, **k):
        s, x, sha = vraie(*a, **k)
        return [e for e in s if e.nom != "tromperie-lineaire-c2"], x, sha
    monkeypatch.setattr(fg, "lire_sondes", sans_tromperie)
    with pytest.raises(GardeArret, match="sonde figée tromperie-lineaire-c2 absente du fichier léger"):
        rx.controler_avant_ouverture(p3, _config(p3))


def test_controle_aucune_sonde_figee_nommee(p3):
    """Mutation x9 : aucune sonde figée nommée (les deux concepts de P3 à `None`) → `GardeArret` ; une seule nommée passe."""
    c = _config(p3)
    c["sondes_par_concept"]["tromperie"] = None
    assert set(rx.controler_avant_ouverture(p3, c)["figees"]) == {"enjeux-difference_moyennes-c0"}
    c["sondes_par_concept"]["enjeux"] = None
    with pytest.raises(GardeArret, match="aucune sonde figée de P3 nommée"):
        rx.controler_avant_ouverture(p3, c)


# ------------------------------------------------------------------------------------------------------------ CLC-P3-02
def _config_commande(d) -> dict:
    """Configuration v8 en mode jouet sur le run jouet de P3 (sondes, fichier léger, données et clé `plancher_figees` du jouet)."""
    c, j = v8(), _config(d)
    c.update(mode="jouet", sondes_par_concept=j["sondes_par_concept"], planchers_p3=j["planchers_p3"],
             fichiers_sondes=j["fichiers_sondes"], donnees_p3=j["donnees_p3"])
    c[rx.CLE_CONFIG] = j[rx.CLE_CONFIG]
    return c


def _etat(racine: Path) -> dict:
    return {str(p.relative_to(racine)): (p.stat().st_size, p.stat().st_mtime_ns) for p in racine.rglob("*") if ".git" not in p.parts}


def _commande(racine, config, tmp_path, capsys, *extra):
    cfg = tmp_path / f"config-{len(list(tmp_path.glob('config-*')))}.json"
    if isinstance(config, dict):
        cfg.write_text(json.dumps(config), encoding="utf-8")
    elif config is not None:
        cfg.write_text(config, encoding="utf-8")
    capsys.readouterr()
    code = lv4.main(["controle-avant-ouverture", str(racine), str(cfg), *extra])
    sortie = capsys.readouterr()
    return code, sortie.out, sortie.err


def test_commande_controle_avant_ouverture_jouet(p3, tmp_path, capsys):
    """Cas sain : code 0, résumé JSON (figées, témoins, directions de P3, cache sans objet en jouet) ; artefacts : code 2, motif
    sur l'erreur, rien sur la sortie, rien d'écrit sous la racine."""
    avant = _etat(p3)
    code, out, err = _commande(p3, _config_commande(p3), tmp_path, capsys)
    assert code == lv4.CODE_OK and err == ""
    r = json.loads(out)
    assert set(r["figees"]) == {"tromperie-lineaire-c2", "enjeux-difference_moyennes-c0"}
    assert r["figees"]["tromperie-lineaire-c2"]["temoin"] == "tromperie-difference_moyennes-c2"
    assert r["modele_p3"]["etat"].startswith("sans objet")
    fautes = []
    c = _config_commande(p3); c["donnees_p3"]["sondes_figees_p3"]["sha256"] = "0" * 64; fautes.append((c, "empreinte"))
    c = _config_commande(p3); c["sondes_par_concept"]["enjeux"] = "enjeux-lineaire-c0"; fautes.append((c, "principale de P3"))
    c = _config_commande(p3); c[rx.CLE_CONFIG]["n_p3"] = 5; fautes.append((c, "directions"))
    c = _config_commande(p3); c[rx.CLE_CONFIG]["garde_principale"] = "aucune"; fautes.append((c, "garde_principale"))
    c = _config_commande(p3); del c[rx.CLE_CONFIG]; fautes.append((c, "plancher_figees"))
    fautes.append(("{illisible", "contrôle avant l'ouverture"))
    fautes.append((None, "contrôle avant l'ouverture"))                       # fichier de configuration absent
    for config, motif in fautes:
        code, out, err = _commande(p3, config, tmp_path, capsys)
        assert code == lv4.CODE_REFUS and out == "" and err.startswith("REFUS : ") and motif in err, (motif, err)
    assert _etat(p3) == avant


def test_commande_controle_temoin_et_sonde_absents(p3, tmp_path, capsys, monkeypatch):
    """Artefacts du fichier léger, par la commande : témoin absent ; sonde figée absente → code 2, motif écrit."""
    from controle_ia.premier_test_ia import figees as fg
    vraie = fg.lire_sondes
    for retire, motif in (("tromperie-difference_moyennes-c2", "témoin"), ("enjeux-difference_moyennes-c0", "absente du fichier léger")):
        monkeypatch.setattr(fg, "lire_sondes", lambda *a, _r=retire, **k: (lambda s: ([e for e in s[0] if e.nom != _r], s[1], s[2]))(vraie(*a, **k)))
        code, out, err = _commande(p3, _config_commande(p3), tmp_path, capsys)
        assert code == lv4.CODE_REFUS and motif in err, err


def test_commande_faute_hors_garde_code_2(p3, tmp_path, capsys, monkeypatch):
    """Une faute hors `GardeArret` levée pendant le contrôle (ici `KeyError`, `OSError`) → code 2, type et motif écrits."""
    for exc in (KeyError, OSError):
        monkeypatch.setattr(rx, "_temoin", lambda *a, _e=exc, **k: (_ for _ in ()).throw(_e("artefact")))
        code, out, err = _commande(p3, _config_commande(p3), tmp_path, capsys)
        assert code == lv4.CODE_REFUS and f"faute {exc.__name__}" in err, err


def _reels():
    for rel in REELS_P3:
        if not (RACINE_DEPOT / rel).is_file():
            pytest.skip(f"{rel} absent de l'extraction (fichiers réels de P3)")


def test_commande_controle_avant_ouverture_reel(tmp_path, capsys, hors_ligne):
    """Mode réel, configuration v8, fichiers réels de P3 : cache factice complet à la révision de P3 → code 0 ; cache absent,
    index illisible, révision par nom de branche → code 2, motif écrit."""
    _reels()
    rev = json.loads((RACINE_DEPOT / REELS_P3[0]).read_text(encoding="utf-8"))["config"]["agent"]["revision"]
    assert rev == REV
    sain = _cache(tmp_path / "sain", MODELE_P3, REV, COMPLET)
    code, out, err = _commande(RACINE_DEPOT, v8(), tmp_path, capsys, "--cache-dir", str(sain))
    assert code == lv4.CODE_OK, err
    r = json.loads(out)
    assert r["modele_p3"]["revision"] == REV and r["modele_p3"]["poids"] == 2
    assert set(r["figees"]) == {"tromperie-difference_moyennes-c15", "enjeux-lineaire-c15"}
    assert all(x["directions_p3"] == 200 for x in r["figees"].values())
    code, out, err = _commande(RACINE_DEPOT, v8(), tmp_path, capsys, "--cache-dir", str(tmp_path / "vide"))
    assert code == lv4.CODE_REFUS and "absent du cache local" in err
    illisible = _cache(tmp_path / "illisible", MODELE_P3, REV, dict(COMPLET, **{"model.safetensors.index.json": "{"}))
    code, out, err = _commande(RACINE_DEPOT, v8(), tmp_path, capsys, "--cache-dir", str(illisible))
    assert code == lv4.CODE_REFUS and "index des poids illisible" in err
    code, out, err = _commande(RACINE_DEPOT, v7(), tmp_path, capsys, "--cache-dir", str(sain))   # v7 : tolérances autres
    assert code == lv4.CODE_REFUS and "fixées d'avance" in err, err
    c = v8()
    c["n_plancher"] = 200                                       # contrôle de la v4 (non de la réextraction) : joué d'abord
    code, out, err = _commande(RACINE_DEPOT, c, tmp_path, capsys, "--cache-dir", str(sain))
    assert code == lv4.CODE_REFUS and "n_plancher 200 ≠ 800" in err, err
    c = v8()
    c["mode"] = "jouet"                                         # même fichiers, mode jouet : cache sans objet (pas de lecture)
    code, out, err = _commande(RACINE_DEPOT, c, tmp_path, capsys, "--cache-dir", str(tmp_path / "vide"))
    assert code == lv4.CODE_OK and json.loads(out)["modele_p3"]["etat"].startswith("sans objet"), err
    assert not os.path.exists(tmp_path / "vide")
