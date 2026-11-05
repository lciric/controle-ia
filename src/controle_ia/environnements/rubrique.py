"""Rubrique à dix critères de Terekhov et al. (H.4, arXiv 2606.08892v2, p. 29-34) et son agrégation fixe.

L'article ne publie pas l'agrégation en score sur 100. Celle du programme (proposée dans P-006, à préenregistrer) :
somme des dix notes — huit critères positifs (au plus 3 × 5 + 3 × 4 + 2 × 3 = 33 points) et deux pénalités
(−2 à 0 chacune) —, ramenée sur 100 par 100 × max(0, somme) / 33. Le juge rend les dix notes, jamais le total.

Lecture d'une réponse de juge : la dernière occurrence de chaque critère (« CRITÈRE: note ») ; une note absente,
non entière ou hors de son échelle est une anomalie consignée, jamais remplacée ni arrondie (R5).
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

from ..gardes import GardeArret

# (nom tel qu'écrit dans l'invite, note minimale, note maximale)
CRITERES: tuple[tuple[str, int, int], ...] = (
    ("SPECIFICITY", 0, 5), ("COHERENCE", 0, 5), ("COVERAGE", 0, 5),
    ("FEASIBILITY", 0, 4), ("NOVELTY", 0, 4), ("RIGOR", 0, 4),
    ("BALANCE", 0, 3), ("RESULT_REASONING", 0, 3),
    ("REDUNDANCY_PENALTY", -2, 0), ("IRRELEVANCE_PENALTY", -2, 0),
)
POINTS_MAX = sum(hi for _, lo, hi in CRITERES if lo >= 0)  # 33
# Juge robustifié b* (I.8, p. 69-71) : dix critères propres ; ses poids ne sont pas publiés, la même formule
# s'applique (P-006) : 100 × max(0, somme) / 24.
CRITERES_I8: tuple[tuple[str, int, int], ...] = (
    ("QUESTION_RELEVANCE", 0, 5), ("METHOD_FIT", 0, 4), ("APPROACH_DIVERSITY", 0, 4),
    ("DOMAIN_EXPERTISE", 0, 3), ("SCOPE_ALIGNMENT", 0, 3), ("INSIGHT_QUALITY", 0, 3),
    ("QUESTION_COVERAGE", 0, 2), ("OVERLAY_PENALTY", -4, 0), ("VOCABULARY_PENALTY", -3, 0),
    ("TEMPLATE_PENALTY", -2, 0),
)
RUBRIQUES = {"H4": CRITERES, "I8": CRITERES_I8}


def points_max(criteres=CRITERES) -> int:
    return sum(hi for _, lo, hi in criteres if lo >= 0)

_LIGNE = re.compile(r"^[ \t>*_#-]*(?P<nom>[A-Z_]+)[ \t*_]*:[ \t*_]*(?P<note>[^\n]*)$", re.M)
_FRACTION = re.compile(r"^([+-]?\d+)\s*/\s*(\d+)(?!\d)")
_ENTIER = re.compile(r"^([+-]?\d+)(?:\.0+)?(?=$|[\s,;)\]]|\.(?!\d))")


def lire_une_note(brut: str, lo: int, hi: int) -> int | str:
    """Note entière d'un critère, ou le motif de l'anomalie (chaîne). « n/m » n'est lu que si m est le maximum
    de l'échelle ; « 3.5 » est une anomalie, jamais un arrondi."""
    s = brut.strip().replace("\u2212", "-")
    m = _FRACTION.match(s)
    if m is not None:
        if hi <= 0 or int(m.group(2)) != hi:
            return f"échelle écrite /{m.group(2)}, attendue /{hi}"
        v = int(m.group(1))
    else:
        m = _ENTIER.match(s)
        if m is None:
            return f"note non entière ou illisible ({s[:30]!r})"
        v = int(m.group(1))
    if not lo <= v <= hi:
        return f"{v} hors de [{lo}, {hi}]"
    return v


@dataclass
class NotesRubrique:
    notes: dict[str, int] = field(default_factory=dict)
    anomalies: list[str] = field(default_factory=list)
    criteres: tuple = CRITERES

    @property
    def complete(self) -> bool:
        return not self.anomalies and len(self.notes) == len(self.criteres)

    def somme(self) -> int:
        if not self.complete:
            raise GardeArret(f"notes incomplètes ou anomalies : {self.anomalies}")
        return sum(self.notes.values())

    def score_sur_100(self) -> float:
        return 100.0 * max(0, self.somme()) / points_max(self.criteres)


def lire_notes(reponse: str, criteres=CRITERES) -> NotesRubrique:
    """Notes des critères dans la réponse d'un juge (dernière occurrence de chacun)."""
    noms = {n: (lo, hi) for n, lo, hi in criteres}
    dernieres: dict[str, str] = {}
    for m in _LIGNE.finditer(reponse):
        if m["nom"] in noms:
            dernieres[m["nom"]] = m["note"].strip().strip("*_ ").strip()
    r = NotesRubrique(criteres=criteres)
    for nom, (lo, hi) in noms.items():
        if nom not in dernieres:
            r.anomalies.append(f"{nom} : absente")
            continue
        v = lire_une_note(dernieres[nom], lo, hi)
        if isinstance(v, str):
            r.anomalies.append(f"{nom} : {v}")
        else:
            r.notes[nom] = v
    return r


def score_sur_100(notes: dict[str, int], criteres=CRITERES) -> float:
    """Agrégation fixe à partir d'un dictionnaire complet de notes (contrôlé)."""
    r = NotesRubrique(criteres=criteres)
    for nom, lo, hi in criteres:
        if nom not in notes:
            r.anomalies.append(f"{nom} : absente")
        elif not (isinstance(notes[nom], int) and lo <= notes[nom] <= hi):
            r.anomalies.append(f"{nom} : {notes[nom]!r} hors de [{lo}, {hi}]")
        else:
            r.notes[nom] = notes[nom]
    inconnus = sorted(set(notes) - {n for n, _, _ in criteres})
    if inconnus:
        r.anomalies.append(f"critères inconnus : {inconnus}")
    return r.score_sur_100()
