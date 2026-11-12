"""Essais R5 du repli de l'étape A de T0.7 : recalcul des activations (`src/controle_ia/t07/repli_recalcul_v1.py` ; brouillon 19,
plan, point 8, repli ; « Gardes et essais R5 »), **en mode jouet seulement** : un vrai run jouet de la chaîne de T0.6
(`t06.lanceur_v6`, code de `1609a4bf` fusionné de `main`, modèle jouet par caractères, aucun téléchargement) dans un dépôt
jetable, préparé comme `tests/test_t06_v11_lanceur_jouet.py` ; puis les activations de l'instance sont retirées (disque perdu)
et le repli les recalcule.

Cas sain : recalcul (contrôle d'identité à dose 0, rejeu en forçage, garde d'équivalence) égal au bit près aux activations que
la chaîne avait écrites ; étape A de T0.7 complète sur les activations recalculées, garde d'identité remplacée par la garde
d'équivalence. Artefacts : empan décalé d'un jeton → garde d'équivalence en échec (R11) ; empreinte d'un adaptateur autre →
arrêt ; dossier d'activations déjà présent → refus (R12)."""
from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller
from controle_ia.t07 import repli_recalcul_v1 as rr

RACINE_DEPOT = Path(__file__).resolve().parents[1]
CONFIG_JOUET = RACINE_DEPOT / "docs" / "notes" / "g0-deux-semaines-v1" / "config-t06-jouet-v5.json"
RUN = "20261110-070000-t06-jouet"
ENONCES = ["Which routing rule makes sparse mixtures of experts train stably?",
           "Does curriculum ordering change sample efficiency of small language models?",
           "Can retrieval reduce hallucination in long-form question answering?",
           "How does tokenizer vocabulary size affect multilingual transfer?",
           "Do sparse autoencoders recover known features in toy models?",
           "Is chain-of-thought faithful under distribution shift?"]


def _git(d: Path, *args):
    subprocess.run(["git", "-C", str(d), *args], check=True, capture_output=True)


@pytest.fixture(scope="module")
def run_jouet(tmp_path_factory):
    """Un run jouet de T0.6 (lanceur_v6) ; rend (racine, dossier des activations d'origine, déplacé hors de la racine)."""
    if not CONFIG_JOUET.is_file() or not (RACINE_DEPOT / "src" / "controle_ia" / "t06" / "lanceur_v6.py").is_file():
        pytest.skip("chaîne de T0.6 absente de ce clone")
    from controle_ia.t06 import lanceur_v6 as la6
    d = tmp_path_factory.mktemp("depot-t06-jouet")
    _git(d, "init", "-q", "-b", "main")
    _git(d, "config", "user.email", "essai@example.invalid")
    _git(d, "config", "user.name", "essai")
    (d / "prereg").mkdir()
    for nom in ("P3-consignes-v1.md", "P3-consignes-v1.md.sha256"):
        shutil.copy(RACINE_DEPOT / "prereg" / nom, d / "prereg" / nom)
    t = d / "donnees" / "t06-jouet"
    t.mkdir(parents=True)
    taches = lambda ids: {"taches": [{"identifiant": i, "questions": ENONCES[k % len(ENONCES)] + f" ({i})"} for k, i in enumerate(ids)]}
    (t / "taches-evaluation.json").write_text(json.dumps(taches([f"e{k}" for k in range(1, 7)])), encoding="utf-8")
    (t / "taches-distillation.json").write_text(json.dumps(taches(["d1", "d2"])), encoding="utf-8")
    config = json.loads(CONFIG_JOUET.read_text(encoding="utf-8"))
    config["taches_evaluation"]["sha256"] = sceller(t / "taches-evaluation.json")
    config["taches_distillation"]["sha256"] = sceller(t / "taches-distillation.json")
    config["egalite_jetons_reels"] = False
    for x in ("runs", "diag"):
        (d / x).mkdir()
    _git(d, "add", "-A")
    _git(d, "commit", "-q", "-m", "jouet")
    la6.executer(config, d, RUN, None)
    origine = tmp_path_factory.mktemp("activations-d-origine") / "activations"
    shutil.move(str(d / "donnees" / RUN / "activations"), str(origine))
    return d, origine


def test_repli_cas_sain_egal_au_bit_pres_aux_activations_de_la_chaine(run_jouet):
    """Recalcul : identité à dose 0 vérifiée, tous les épisodes rejoués, garde d'équivalence passée ; chaque activation
    recalculée égale au bit près celle que la chaîne avait écrite (même modèle, même machine)."""
    racine, origine = run_jouet
    sortie = racine.parent / "recalcul-sain"
    r = rr.recalculer(racine, RUN, sortie)
    assert r["garde_equivalence"]["ecart_max"] == 0.0 and r["garde_equivalence"]["actions"] >= 1
    assert set(r["identite_dose_0"]) == {"saboteur", "temoin"} and all(x["dose_0_identique"] for x in r["identite_dose_0"].values())
    fichiers = sorted(p.relative_to(origine) for p in origine.rglob("*.npy"))
    assert fichiers and fichiers == sorted(p.relative_to(sortie) for p in sortie.rglob("*.npy"))
    assert r["rejeu"]["actions_notees_recalculees"] * len(list(origine.iterdir())) == len(fichiers)
    for f in fichiers:
        a, b = np.load(origine / f), np.load(sortie / f)
        assert a.dtype == b.dtype and np.array_equal(a.view(np.uint16), b.view(np.uint16)), f


def test_repli_artefact_empan_decale_d_un_jeton_garde_en_echec(run_jouet, monkeypatch):
    """Artefact (comme le contrôle négatif de T0.6) : empan noté décalé d'un jeton → garde d'équivalence en échec (R11)."""
    racine, _ = run_jouet
    monkeypatch.setattr(rr, "EMPAN_DECALAGE", 1)
    with pytest.raises(GardeArret, match="activations de génération ≠ passe unique|non recalculée|forme recalculée"):
        rr.recalculer(racine, RUN, racine.parent / "recalcul-decale")


def test_repli_artefact_adaptateur_d_empreinte_autre_arret(run_jouet, monkeypatch):
    """Artefact : empreinte des adaptateurs chargés autre que celle de `distillation-t06.json` → arrêt (R11)."""
    racine, _ = run_jouet
    from controle_ia.organismes import lora
    monkeypatch.setattr(lora, "empreinte_adaptateurs", lambda m: "0" * 64)
    with pytest.raises(GardeArret, match="empreinte .* ≠ distillation-t06.json"):
        rr.recalculer(racine, RUN, racine.parent / "recalcul-empreinte")


def test_repli_dossier_d_activations_present_refus(run_jouet, tmp_path):
    """R12 : le repli n'écrit jamais par-dessus des activations ; dossier présent → refus avant tout chargement."""
    racine, _ = run_jouet
    present = tmp_path / "deja"
    present.mkdir()
    with pytest.raises(GardeArret, match="existe déjà"):
        rr.recalculer(racine, RUN, present)
