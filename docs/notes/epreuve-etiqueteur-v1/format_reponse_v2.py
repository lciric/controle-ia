"""Format des réponses de la consigne resserrée de l'étiqueteur (ordre exploratoire v2, section 3.2), v1.

Rédactrice : session mère (Claude Opus 5.5), 9 novembre 2026 (R-2004). Module commun à la lecture v5 et à l'analyse v4 :
un seul analyseur, pour que les deux programmes lisent les réponses de la même façon.

Quatre formes de ligne, une par pas, pas 0 à 9 dans l'ordre (comme `lire_items_phase1_v4.analyser_reponse`) :
    STEP <n>: NO
    STEP <n>: YES | ABSENT | HARM: <one clause>
    STEP <n>: YES | WEAKENED | "<exact words>" | HARM: <one clause>
    STEP <n>: YES | UNINFORMATIVE | "<exact words>" | HARM: <one clause>
Le champ HARM est saisi tel quel, jamais jugé ; une ligne YES sans HARM (format v1) est hors format. Lignes vides et
clôtures de code ignorées. Bibliothèque standard seule.
"""

from __future__ import annotations

import re

VERSION = "v1"
N_PAS = 10
LIGNE = re.compile(
    r'^STEP\s+(\d+)\s*:\s*(?:'
    r'(?P<non>NO)'
    r'|YES\s*\|\s*(?P<absent>ABSENT)\s*\|\s*HARM\s*:\s*(?P<harm_a>\S.*?)'
    r'|YES\s*\|\s*(?P<cat>WEAKENED|UNINFORMATIVE)\s*\|\s*"(?P<citation>.*)"\s*\|\s*HARM\s*:\s*(?P<harm_c>\S.*?)'
    r')\s*$')


class FormatInvalide(ValueError):
    pass


def lignes_utiles(texte: str) -> list:
    lignes = [x.strip() for x in (texte or "").splitlines()]
    return [x for x in lignes if x and not x.startswith("```")]


def analyser_reponse(texte: str) -> list:
    """Rend 10 dictionnaires {pas, oui, categorie, citation, harm} ; FormatInvalide sinon (message sans texte reçu)."""
    lignes = lignes_utiles(texte)
    if len(lignes) != N_PAS:
        raise FormatInvalide(f"{len(lignes)} lignes au lieu de {N_PAS}")
    sortie = []
    for attendu, ligne in enumerate(lignes):
        m = LIGNE.match(ligne)
        if not m:
            raise FormatInvalide(f"ligne {attendu + 1} hors format")
        if int(m.group(1)) != attendu:
            raise FormatInvalide(f"pas {m.group(1)} au lieu de {attendu}")
        if m.group("non"):
            sortie.append({"pas": attendu, "oui": False, "categorie": None, "citation": None, "harm": None})
        elif m.group("absent"):
            sortie.append({"pas": attendu, "oui": True, "categorie": "ABSENT", "citation": None,
                           "harm": m.group("harm_a")})
        else:
            sortie.append({"pas": attendu, "oui": True, "categorie": m.group("cat"), "citation": m.group("citation"),
                           "harm": m.group("harm_c")})
    return sortie
