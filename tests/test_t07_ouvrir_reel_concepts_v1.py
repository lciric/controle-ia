"""Essai R5 du lien « quatre concepts au moins en mode réel » de `lecture_v2.ouvrir` (l. 501 au commit `37485ce5` :
`4 if config["mode"] == "reel" else 1`), constat CLC-04 de la contre-lecture courte du code de T0.7, option (c)
(`docs/notes/g0-deux-semaines-v1/t07-module-v2/contre-lecture-code-t07-option-c-courte-v1.md`, `7a327462…`) ; consigne de la mère
`consigne-essai-clc04-t07-v1.md` (`d0714ffb…`). Fichier neuf (R12) : aucun fichier de `src/` ni aucun essai existant ne change.

L'essai (iv) existant, `test_trois_concepts_en_mode_reel_refus_quatre_exiges`, donne le minimum à la main à
`lire_jeux_et_phrases` ; celui-ci passe **par `ouvrir`**, sur le faux run de l'étape A complète
(`test_t07_sondes_neuves_v1.construire_complet`), fichier léger factice à 24 couples (`test_t07_lecture_v2._fichier_leger_24`,
pour que le contrôle des 24 couples du mode réel passe), ligne `SCELLEMENT-CONCEPTS-T07` strictement antérieure à la fermeture
(aucune ouverture antérieure de l'étape A, aucun journal de P3-bis : fermeture = ouverture en cours) :

- **artefact** : phrases de trois concepts (`test_t07_option_c_concepts_v1._trois_concepts`), configuration en mode réel →
  refus de la garde, le minimum de quatre pour **seul** motif, ligne `REFUS-T07` qui le porte, aucune ligne `OUVERTURE-T07` ;
- **cas sain** : phrases de quatre concepts, mode réel → ouverture, phrases « lues », motif absent ;
- **contre-épreuve** : le même artefact en mode jouet (minimum un) → ouverture, phrases lues, aucun refus de minimum.

Limite déclarée : la configuration est celle du jouet passée en `mode` « reel » ; `ouvrir` n'appelle pas `exiger_configuration`
(l'étape A l'appelle avant), qui la refuserait en mode réel (fichier léger réel `701f73bd…`, `n_plancher`, préenregistrement)."""
from __future__ import annotations

import json

import pytest

from controle_ia.t07 import journal_p3bis_v1 as jp
from controle_ia.t07 import lecture_v2 as lv
from controle_ia.t07 import lectures_t07_v1 as lt
from controle_ia.t07 import registre_v1 as rg
from test_t07_lecture_v1 import INSTANT, RUN_T06, _depot, _sans_ligne
from test_t07_lecture_v2 import _fichier_leger_24
from test_t07_option_c_concepts_v1 import _trois_concepts
from test_t07_sondes_neuves_v1 import construire_complet

MOTIF_MINIMUM = "au moins 4 attendus (plan, point 10)"
MOTIF_TROIS = f"phrases des concepts : 3 concept(s), {MOTIF_MINIMUM}"


@pytest.fixture
def complet(depot):
    return construire_complet(depot)


def _quatre_concepts() -> str:
    extra = [json.dumps({"concept": "rivieres", "indice": k, "phrase_concept": f"la rivière {k} coule",
                         "phrase_neutre": f"la colonne {k} coule"}, ensure_ascii=False) for k in (1, 2, 3)]
    return _trois_concepts() + "".join(l + "\n" for l in extra)


def _concepts(texte: str) -> set:
    return {json.loads(l)["concept"] for l in texte.splitlines()[1:] if l.strip()}


def _preparer(j, texte: str, mode: str) -> None:
    """Jeu des phrases `texte` déposé sous un nom neuf (celui de `construire_complet` est scellé, R12) et cité par une ligne
    `SCELLEMENT-CONCEPTS-T07` datée une heure avant l'ouverture (la ligne du banc retirée), fichier léger à 24 couples, `mode` de
    la configuration ; préconditions vérifiées : étape A complète, ligne des concepts strictement avant la fermeture."""
    _sans_ligne(j, rg.SCELLEMENT_CONCEPTS_T07)
    rel, sha = _depot(j.racine, f"prereg/jeux-clc04/concepts-{len(_concepts(texte))}.jsonl", texte)
    rg.ajouter_ligne(j.registre, rg.SCELLEMENT_CONCEPTS_T07, INSTANT - 3600, rel, sha)
    _fichier_leger_24(j)
    j.config["mode"] = mode
    assert lv.etape_complete(j.config)
    ligne = lv.lire_lignes_actuelles(j.registre, (rg.SCELLEMENT_CONCEPTS_T07,))[rg.SCELLEMENT_CONCEPTS_T07]
    assert lv.premiere_ouverture_a(j.registre, RUN_T06) is None and ligne["instant"] < INSTANT
    assert not (j.racine / jp.JOURNAL_P3BIS).exists()                       # aucun journal de P3-bis : fermeture = ouverture


def _ouvrir(j) -> dict:
    return lv.ouvrir(j.racine, j.registre, j.config, "A", RUN_T06, INSTANT)


# ----------------------------------------------------------------------------------------------------------------- artefact
def test_ouvrir_mode_reel_trois_concepts_refus_minimum_de_quatre(complet):
    """Artefact (R5) : trois concepts, mode réel, par `ouvrir` → refus ; le minimum de quatre est le seul motif ; la garde
    journalise `REFUS-T07` et n'ouvre pas. Sous la mutation m13 (minimum ramené à 1), `ouvrir` ouvrirait : échec de l'essai."""
    texte = _trois_concepts()
    assert len(_concepts(texte)) == 3
    _preparer(complet, texte, "reel")
    with pytest.raises(rg.RefusRegistre) as e:
        _ouvrir(complet)
    assert str(e.value).split(" ; ") == [MOTIF_TROIS]
    journal = complet.lignes_journal()
    assert journal and journal[-1].startswith("| REFUS-T07 |") and MOTIF_MINIMUM in journal[-1]
    assert not any(l.startswith("| OUVERTURE-T07 |") for l in journal)


# ----------------------------------------------------------------------------------------------------------------- cas sain
def test_ouvrir_mode_reel_quatre_concepts_phrases_lues(complet):
    """Cas sain : quatre concepts, mode réel, par `ouvrir` → ouverture, phrases « lues » (quatre concepts), 24 couples figés
    chargés (contrôle du mode réel passé), fermeture à l'ouverture en cours ; motif du minimum absent du journal."""
    texte = _quatre_concepts()
    assert len(_concepts(texte)) == 4
    _preparer(complet, texte, "reel")
    sortie = _ouvrir(complet)
    jx = sortie["jeux_generiques"]
    assert jx["phrases_etat"]["etat"] == lt.ETAT_PHRASES_LUES and jx["phrases"] is not None
    assert set(jx["phrases"]["concepts"]) == _concepts(texte)
    assert sortie["rapport_couples"]["nombre"] == lv.N_COUPLES_FIGES_REEL
    assert sortie["garde_adaptee"]["fermeture_perimetre"]["instant"] == rg.date_utc(INSTANT)
    journal = complet.lignes_journal()
    assert journal[-1].startswith("| OUVERTURE-T07 |") and not any(l.startswith("| REFUS-T07 |") for l in journal)
    assert MOTIF_MINIMUM not in "\n".join(journal)


# ------------------------------------------------------------------------------------------------------------ contre-épreuve
def test_contre_epreuve_meme_artefact_en_mode_jouet_aucun_refus_de_minimum(complet):
    """Contre-épreuve : le même artefact (trois concepts), configuration en mode jouet (minimum un) → ouverture, phrases lues
    avec trois concepts, aucun refus. Elle tue aussi la mutation inverse (minimum de quatre en tout mode)."""
    texte = _trois_concepts()
    _preparer(complet, texte, "jouet")
    sortie = _ouvrir(complet)
    jx = sortie["jeux_generiques"]
    assert jx["phrases_etat"]["etat"] == lt.ETAT_PHRASES_LUES and set(jx["phrases"]["concepts"]) == _concepts(texte)
    journal = complet.lignes_journal()
    assert journal[-1].startswith("| OUVERTURE-T07 |") and not any(l.startswith("| REFUS-T07 |") for l in journal)
