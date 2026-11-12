"""Essais R5 du repli, garde d'ouverture d'abord (`src/controle_ia/t07/repli_etapes_v1.py`, révisé par DF-01 ; contre-lecture
différentielle du code `dd794e2e…`), et des artefacts du recalcul que la contre-lecture a trouvés manquants (identité à dose 0,
texte décodé, clé, relance). Banc : un vrai run jouet de T0.6 (`t06.lanceur_v6`, modèle par caractères, aucun téléchargement) et
la lecture de T0.7 préparée comme la répétition jouet (`scripts/repetition_jouet_t07_v1.preparer_t07` : registre, jeux, concepts,
GO, configuration jouet) ; activations de la course retirées (variante B). Chaque essai travaille sur une copie du banc."""
from __future__ import annotations

import json
import shutil
import sys
import time
from pathlib import Path

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller
from controle_ia.t07 import lecture_v2 as lv
from controle_ia.t07 import registre_v1 as rg
from controle_ia.t07 import repli_etapes_v1 as rt
from controle_ia.t07 import repli_recalcul_v1 as rr

RACINE_DEPOT = Path(__file__).resolve().parents[1]
CONFIG_JOUET = RACINE_DEPOT / "docs" / "notes" / "g0-deux-semaines-v1" / "config-t06-jouet-v5.json"
sys.path.insert(0, str(RACINE_DEPOT / "scripts"))
T0 = int(time.time()) - 3600


@pytest.fixture(scope="module")
def banc(tmp_path_factory):
    if not CONFIG_JOUET.is_file() or not (RACINE_DEPOT / "src" / "controle_ia" / "t06" / "lanceur_v6.py").is_file():
        pytest.skip("chaîne de T0.6 absente de ce clone")
    import repetition_jouet_t07_v1 as r1
    from controle_ia.t06 import lanceur_v6 as la6
    d = tmp_path_factory.mktemp("banc-repli") / "depot"
    r1.depot_neuf(d)
    (d / "prereg").mkdir()
    for nom in ("P3-consignes-v1.md", "P3-consignes-v1.md.sha256"):
        shutil.copy(RACINE_DEPOT / "prereg" / nom, d / "prereg" / nom)
    t = d / "donnees" / "t06-jouet"
    t.mkdir(parents=True)
    taches = lambda ids: {"taches": [{"identifiant": i, "questions": r1.ENONCES[k % len(r1.ENONCES)] + f" ({i})"} for k, i in enumerate(ids)]}
    (t / "taches-evaluation.json").write_text(json.dumps(taches(r1.EVALUATION)), encoding="utf-8")
    (t / "taches-distillation.json").write_text(json.dumps(taches(r1.DISTILLATION)), encoding="utf-8")
    config = json.loads(CONFIG_JOUET.read_text(encoding="utf-8"))
    config["taches_evaluation"]["sha256"] = sceller(t / "taches-evaluation.json")
    config["taches_distillation"]["sha256"] = sceller(t / "taches-distillation.json")
    config["egalite_jetons_reels"] = False
    for x in ("runs", "diag", "registres"):
        (d / x).mkdir()
    r1.committer(d)
    la6.executer(config, d, r1.RUN_T06, None)
    shutil.move(str(d / "donnees" / r1.RUN_T06 / "activations"), str(d.parent / "activations-d-origine"))
    cfg = r1.preparer_t07(d, rg.date_utc(T0 - 3600))
    return d, r1.RUN_T06, cfg


@pytest.fixture
def b(banc, tmp_path):
    d, run, cfg = banc
    racine = tmp_path / "depot"
    shutil.copytree(d, racine)
    return racine, run, json.loads((racine / cfg.name).read_text(encoding="utf-8"))


def _repli(b, instant=T0, config=None):
    racine, run, cfg = b
    return rt.repli(racine, racine / "registres" / "scellements-v1.md", config or cfg, run, instant)


def _espion(monkeypatch):
    appels = []
    vrai = rr.recalculer

    def espion(*a, **k):
        appels.append(a)
        return vrai(*a, **k)
    monkeypatch.setattr(rr, "recalculer", espion)
    return appels


def _journal(racine: Path) -> list[str]:
    j = racine / "registres" / "scellements-v1.md.ouvertures.md"
    return j.read_text(encoding="utf-8").splitlines() if j.is_file() else []


def test_garde_d_abord_puis_recalcul_puis_reprise_couverte(b, monkeypatch):
    """Cas sain : la garde journalise l'ouverture de l'étape A **avant** le recalcul ; recalcul sous un nom daté, renommé en
    `activations/`, rapport scellé à côté (empreinte des activations) ; une seconde commande **reprend** sur ce recalcul couvert
    sans recalculer."""
    racine, run, _ = b
    appels = _espion(monkeypatch)
    r = _repli(b)
    assert not r["reprise"] and len(appels) == 1 and r["rapport"]["ecrit_sous"].startswith(f"donnees/{run}/activations-repli-")
    assert any(l.startswith("| OUVERTURE-T07 |") and f"etape-A/{run}" in l for l in _journal(racine))
    act = racine / "donnees" / run / "activations"
    assert (act / rt.RAPPORT).is_file() and not (racine / r["rapport"]["ecrit_sous"]).exists()
    assert rt.empreinte_activations(act) == (r["rapport"]["empreinte_activations"], r["rapport"]["fichiers_activations"])
    r2 = _repli(b, T0 + 1)
    assert r2["reprise"] and len(appels) == 1 and r2["rapport"]["empreinte_activations"] == r["rapport"]["empreinte_activations"]


@pytest.mark.xfail(strict=True, raises=pytest.fail.Exception,
                   reason="SCELLEMENT-CONCEPTS-T07 devenue permise (brouillon 21, option (c), R-2158) : son absence ne refuse plus "
                          "la garde (« DID NOT RAISE ») ; remplacé par test_t07_option_c_concepts_v1."
                          "test_repli_ligne_exigee_manquante_rien_calcule_puis_relance (RUN-CONFIRMATION-T06)")
def test_garde_refusee_rien_calcule_puis_relance(b, monkeypatch):
    """Artefact : une ligne exigée manque (`SCELLEMENT-CONCEPTS-T07`) → refus de la garde, journalisé, **aucun recalcul**, aucun
    dossier d'activations ; relance quand la ligne est inscrite : recalcul fait (attente simple, R12 tenu)."""
    racine, run, _ = b
    reg = racine / "registres" / "scellements-v1.md"
    texte = reg.read_text(encoding="utf-8")
    ligne = next(l for l in texte.splitlines() if l.startswith(f"| {rg.SCELLEMENT_CONCEPTS_T07} |"))
    reg.write_text(texte.replace(ligne + "\n", ""), encoding="utf-8")
    appels = _espion(monkeypatch)
    with pytest.raises(rg.RefusRegistre, match="SCELLEMENT-CONCEPTS-T07"):
        _repli(b)
    assert not appels and not [x for x in (racine / "donnees" / run).glob("activations*") if x.is_dir()]
    assert any(l.startswith("| REFUS-T07 |") for l in _journal(racine))
    reg.write_text(texte, encoding="utf-8")
    assert not _repli(b, T0 + 1)["reprise"] and len(appels) == 1


def test_course_7a_refusee_avant_tout_calcul(b, monkeypatch):
    """Artefact : le manifeste cité est celui d'une course refusée (`go_id_refuse`, comme 7a) → refus avant tout recalcul."""
    racine, run, cfg = b
    go = json.loads((racine / "runs" / run / "manifeste.json").read_text(encoding="utf-8"))["config"]["go_id"]
    appels = _espion(monkeypatch)
    with pytest.raises(rg.RefusRegistre, match="R12-invalide"):
        _repli(b, config={**cfg, "go_id_refuse": go})
    assert not appels


def test_equivalence_en_echec_puis_relance_sous_un_nom_neuf(b, monkeypatch):
    """Artefact : garde d'équivalence en échec (empan décalé d'un jeton) → arrêt R11, recalcul gardé sous son nom daté,
    `activations/` absent ; **relance** (nom daté neuf) : garde passée, le premier dossier reste (rien n'est écrasé, R12)."""
    racine, run, _ = b
    monkeypatch.setattr(rr, "EMPAN_DECALAGE", 1)
    with pytest.raises(rt.ArretRepli, match="relance une fois"):
        _repli(b)
    echec = list((racine / "donnees" / run).glob("activations-repli-*"))
    assert len(echec) == 1 and not (racine / "donnees" / run / "activations").exists()
    monkeypatch.setattr(rr, "EMPAN_DECALAGE", 0)
    r = _repli(b, T0 + 2)
    assert not r["reprise"] and echec[0].is_dir() and (racine / "donnees" / run / "activations" / rt.RAPPORT).is_file()


def test_reprise_refusee_sans_rapport_ou_activations_changees(b):
    """Artefacts de la reprise : `activations/` présent sans rapport du repli → refus (R12) ; recalcul couvert puis une activation
    retouchée → refus (empreinte des activations) ; la relecture avant `etape-a-apres-repli` refuse de même."""
    racine, run, _ = b
    act = racine / "donnees" / run / "activations"
    act.mkdir(parents=True)
    with pytest.raises(rt.RefusRepli, match="absent"):
        _repli(b)
    act.rmdir()
    _repli(b, T0 + 1)
    npy = sorted(act.rglob("*.npy"))[0]
    a = np.load(npy)
    a.flat[0] = a.flat[0] + 1
    np.save(npy, a)
    with pytest.raises(rt.RefusRepli, match="activations changées"):
        rt.lire_rapport(racine, run)
    with pytest.raises(rt.RefusRepli, match="activations changées"):
        _repli(b, T0 + 2)


def test_identite_a_dose_0_en_echec(b, monkeypatch):
    """Artefact : logits de la base perturbés (dose 0 ≠ base au bit près) → arrêt R11 avant tout rejeu ; cas sain : premier essai."""
    from controle_ia.t06 import identite
    vrai, vu = identite.logits_de_controle, []

    def perturbe(*a, **k):
        x = vrai(*a, **k)
        vu.append(1)
        return x + 1e-3 if len(vu) == 1 else x
    monkeypatch.setattr(identite, "logits_de_controle", perturbe)
    with pytest.raises(rt.ArretRepli, match="dose 0 en échec"):
        _repli(b)


@pytest.mark.parametrize("champ,motif", [("texte", "texte décodé"), ("cle", "clé reconstruite")])
def test_texte_decode_ou_cle_differents(b, monkeypatch, champ, motif):
    """Artefacts : une action dont le texte écrit (ou la clé) diffère de ce que le rejeu reconstruit → arrêt R11, motif nommé."""
    vrai = rr.lire_textes_par_episode

    def altere(chemin):
        t = vrai(chemin)
        rec = next(iter(next(iter(t.values())).values()))
        rec[champ] = rec[champ] + "x"
        return t
    monkeypatch.setattr(rr, "lire_textes_par_episode", altere)
    with pytest.raises(rt.ArretRepli, match=motif):
        _repli(b)


def test_commandes_repli_seul_puis_etape_a_apres_repli(b, capsys):
    """Les deux commandes de la variante B par `lecture_v2` : `repli-seul` (code 0, reprise au second appel), puis
    `etape-a-apres-repli` (code 0, notation scellée) ; artefact : `etape-a-apres-repli` sans recalcul couvert → code 2."""
    racine, run, cfg = b
    chemin = racine / "config-t07-jouet.json"
    reg = racine / "registres" / "scellements-v1.md"
    assert lv.main(["etape-a-apres-repli", str(racine), run, str(chemin), "--registre", str(reg)]) == rt.CODE_REFUS
    assert lv.main(["repli-seul", str(racine), run, str(chemin), "--registre", str(reg)]) == rt.CODE_OK
    assert "recalcul fait" in capsys.readouterr().out
    assert lv.main(["repli-seul", str(racine), run, str(chemin), "--registre", str(reg)]) == rt.CODE_OK
    assert "reprise" in capsys.readouterr().out
    assert lv.main(["etape-a-apres-repli", str(racine), run, str(chemin), "--registre", str(reg)]) == rt.CODE_OK
    assert "notation scellée" in capsys.readouterr().out
