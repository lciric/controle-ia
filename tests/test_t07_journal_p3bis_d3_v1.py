"""Essais R5 des corrections du lecteur du journal de P3-bis (`src/controle_ia/t07/journal_p3bis_v1.py`) décidées par la mère après
l'essai de concordance du journal (`docs/notes/g0-deux-semaines-v1/concordance-journal-p3bis-t07-v1/rapport-concordance-journal-v1.md`,
`c867a1b2…` ; R-2103) :

- **D-3** : le prédicat de format de l'écrivain (`premier_test_ia/ouverture_p3bis_v2.py`, `330915f6…`, l. 691-750) appliqué en
  entier : ligne vide, espace en tête, saut de ligne final manquant, cellules `appui`, `paquets` ou `motif` hors forme → refus
  (`JournalFautif`, nœud) ; le fichier vide reste refusé ;
- **clé `RENDEZ-VOUS-P3BIS-N`** : motif `[1-9][0-9]*`, celui de l'écrivain, au registre des préalables comme dans l'appui.

Chaque forme : un cas sain (lignes à la forme exacte de l'écrivain) et un artefact. Rien d'autre n'est changé au lecteur ; la règle
« dates non décroissantes » (CT-11) reste telle quelle."""
from __future__ import annotations

from pathlib import Path

import pytest

from controle_ia.scellement import sceller
from controle_ia.t07 import journal_p3bis_v1 as jp
from controle_ia.t07 import registre_v1 as rg

ENTETE = "\n".join(jp.ENTETE_JOURNAL) + "\n"
A, B, C, D = "a" * 64, "b" * 64, "c" * 64, "d" * 64
PAQUETS = f"{C} {D}"
REDUITE = f"| OUVERTURE-P3BIS | 2027-01-15T07:00:00Z | reduite | RENDEZ-VOUS-P3BIS-1={A} GARDE-ADAPTEE-T07-P3BIS={B} | {PAQUETS} | - |"
REFUS = "| REFUS-OUVERTURE-P3BIS | 2027-01-15T07:05:00Z | pleine | - | - | ligne-absente : SCORES-T07 absente |"
PLEINE = f"| OUVERTURE-P3BIS | 2027-01-15T07:10:00Z | pleine | SCORES-T07={A} SONDES-T07={B} | {PAQUETS} | - |"
ANTICIPEE = f"| OUVERTURE-P3BIS | 2027-01-15T07:10:00Z | pleine-anticipee | RENDEZ-VOUS-P3BIS-12={A} | {PAQUETS} | - |"


def _lire(tmp_path: Path, texte: str):
    p = tmp_path / "ouvertures-p3bis-v1.md"
    p.write_text(texte, encoding="utf-8")
    return jp.lire_journal_p3bis(p)


def test_D3_cas_sains_forme_exacte_de_l_ecrivain(tmp_path):
    """Lignes écrites à la forme exacte (une ligne par tentative, saut de ligne final) : lues ; ouvertures et refus distingués ;
    en-tête seul : aucune ligne ; refus à paquets `-` ou à deux empreintes ; clé de rendez-vous à deux chiffres."""
    j = _lire(tmp_path, ENTETE + REDUITE + "\n" + REFUS + "\n" + PLEINE + "\n")
    assert [x["mode"] for x in jp.ouvertures(j)] == ["reduite", "pleine"] and len(j) == 3
    assert [x["cle"] for x in j] == ["OUVERTURE-P3BIS", "REFUS-OUVERTURE-P3BIS", "OUVERTURE-P3BIS"] and j[2]["numero"] == 5
    assert _lire(tmp_path, ENTETE) == []
    assert len(_lire(tmp_path, ENTETE + REFUS.replace("| - | ligne", f"| {PAQUETS} | ligne") + "\n")) == 1
    assert jp.ouvertures(_lire(tmp_path, ENTETE + ANTICIPEE + "\n"))[0]["mode"] == "pleine-anticipee"


@pytest.mark.parametrize("texte,motif", [
    ("", "en-tête"),                                                                       # fichier vide : reste refusé
    (ENTETE + REDUITE + "\n\n" + PLEINE + "\n", "ligne vide"),
    (ENTETE + REDUITE + "\n" + PLEINE + "\n\n", "ligne vide"),
    (ENTETE + REDUITE + "\n" + PLEINE, "sans saut de ligne"),
    (ENTETE + " " + REDUITE + "\n", "ne commence ou ne finit pas"),
    (ENTETE + REDUITE + " \n", "ne commence ou ne finit pas"),
    (ENTETE + REDUITE.replace(PAQUETS, "-") + "\n", "paquets"),
    (ENTETE + REDUITE.replace(f"RENDEZ-VOUS-P3BIS-1={A} GARDE-ADAPTEE-T07-P3BIS={B}", "-") + "\n", "hors de la forme du mode"),
    (ENTETE + REDUITE.replace("| - |", "| x |") + "\n", "motif"),
    (ENTETE + PLEINE.replace(f"SCORES-T07={A} SONDES-T07={B}", f"SONDES-T07={B} SCORES-T07={A}") + "\n", "hors de la forme du mode"),
    (ENTETE + PLEINE.replace(f"SONDES-T07={B}", "SONDES-T07=xyz") + "\n", "jeton"),
    (ENTETE + PLEINE.replace("SONDES-T07", "AUTRE-CLE") + "\n", "clé 'AUTRE-CLE' inconnue"),
    (ENTETE + REFUS.replace("ligne-absente : SCORES-T07 absente", "inconnu : texte") + "\n", "motif"),
    (ENTETE + REFUS.replace("ligne-absente : SCORES-T07 absente", "texte libre sans code") + "\n", "motif"),
    (ENTETE + REFUS.replace("| pleine | - |", "| pleine | x |") + "\n", "jeton"),
    (ENTETE + REFUS.replace("| - | ligne", "| zz | ligne") + "\n", "paquets"),
])
def test_D3_formes_tolerees_naguere_refusees(tmp_path, texte, motif):
    """Artefacts : chaque forme que l'écrivain tient pour hors format est refusée par le lecteur (nœud), motif écrit."""
    with pytest.raises(jp.JournalFautif, match=motif):
        _lire(tmp_path, texte)


def test_D3_CRLF_lu_comme_l_ecrivain(tmp_path):
    """Fins de ligne CRLF : ramenées à LF par la lecture en texte, comme chez l'écrivain (la table du rapport : « accepté »)."""
    p = tmp_path / "ouvertures-p3bis-v1.md"
    p.write_bytes((ENTETE + REDUITE + "\n").replace("\n", "\r\n").encode("utf-8"))
    assert len(jp.lire_journal_p3bis(p)) == 1


def test_D3_regle_des_dates_inchangee(tmp_path):
    """La règle « dates non décroissantes » (CT-11) reste telle quelle : égales permises (sain), décroissantes refusées (artefact)."""
    egal = PLEINE.replace("07:10:00", "07:00:00")
    assert len(_lire(tmp_path, ENTETE + REDUITE + "\n" + egal + "\n")) == 2
    with pytest.raises(jp.JournalFautif, match="antérieure à la ligne précédente"):
        _lire(tmp_path, ENTETE + PLEINE + "\n" + REFUS.replace("07:05:00", "06:00:00") + "\n")


def _prealables(tmp_path: Path, cles: list[str]) -> Path:
    lignes = []
    for k, cle in enumerate(cles):
        f = tmp_path / f"decision-{k}.md"
        f.write_text(f"Décision : maintenir\nDate : 2027-01-1{k}T00:00:00Z\n", encoding="utf-8")
        lignes.append(rg.ecrire_ligne(cle, f"2027-01-1{k}T01:00:00Z", f.name, sceller(f)))
    p = tmp_path / "prealables-p3bis-v1.md"
    p.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    return p


def test_cle_rendez_vous_motif_de_l_ecrivain(tmp_path):
    """`RENDEZ-VOUS-P3BIS-N`, N au motif `[1-9][0-9]*` : `-1`, `-2` lus (sain) ; `-01` et `-0` refusés, clé inconnue (artefacts) ;
    dans l'appui, `RENDEZ-VOUS-P3BIS-01` refusé aussi (D-3)."""
    r = jp.lire_prealables(_prealables(tmp_path, ["RENDEZ-VOUS-P3BIS-1", "RENDEZ-VOUS-P3BIS-2"]), tmp_path, 1_900_000_000)
    assert [e["numero"] for e in r["rendez_vous"]] == [1, 2]
    for faute in ("RENDEZ-VOUS-P3BIS-01", "RENDEZ-VOUS-P3BIS-0"):
        d = tmp_path / faute
        d.mkdir()
        with pytest.raises(rg.RefusRegistre, match="inconnue"):
            jp.lire_prealables(_prealables(d, [faute]), d, 1_900_000_000)
    with pytest.raises(jp.JournalFautif, match="clé 'RENDEZ-VOUS-P3BIS-01' inconnue"):
        _lire(tmp_path, ENTETE + ANTICIPEE.replace("RENDEZ-VOUS-P3BIS-12", "RENDEZ-VOUS-P3BIS-01") + "\n")
