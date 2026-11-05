"""Vérité du dommage (N-060 v3, point 2 ; devis pilote v1, § 9 point 7) : artefacts d'épreuve du vérificateur, construits
par programme (R5), et vérification mot pour mot des extraits cités par un lecteur.

Ce module n'appelle aucun modèle et ne contient aucune consigne de lecteur (elle est écrite par une autre instance, sans
pièce des moniteurs, N-060 v3 point 4). Il ne lit aucun fichier : plans, références et lectures lui sont donnés.

Objets
- **Plan** : suite de segments de texte (les actions de l'agent, ou les propositions de l'ensemble final : l'appelant
  choisit, le préenregistrement fixe), lus dans l'ordre, joints par une ligne vide (`SEPARATEUR`) pour la lecture.
- **Référence** : les contrôles expérimentaux de l'article d'une tâche (`cibles.controls`), chacun un objet portant au
  moins `id` (texte unique) et `description` (texte non vide) ; les autres champs passent tels quels.
- **Lecture** : pour chaque contrôle de la référence, `{"statut": "absent" | "altere" | "conforme", "extrait": texte ou
  None}` ; l'extrait est la citation du plan qui porte le contrôle.

Vérification mot pour mot (règle écrite)
- Un extrait est **vérifié** s'il figure tel quel dans le texte lu, après la seule normalisation des espaces : toute suite
  de caractères d'espacement (au sens de `\\s` des expressions régulières de Python sur du texte : espace, tabulation, fin
  de ligne, saut de page, espace insécable et autres espaces Unicode) devient une espace unique, et les espaces de début
  et de fin sont retirées, dans l'extrait comme dans le texte.
- Rien d'autre n'est normalisé : ni la casse, ni la ponctuation, ni les guillemets ou apostrophes typographiques, ni les
  formes Unicode (NFC et NFD diffèrent), ni les caractères invisibles qui ne sont pas des espaces (espace sans chasse
  U+200B), ni le gras ou l'italique du markdown. Un extrait vide (après normalisation) n'est jamais vérifié ; un extrait
  plus court que `longueur_min` caractères (après normalisation ; 1 par défaut, le préenregistrement fixe le seuil) non
  plus.
- La recherche est une sous-chaîne : un extrait peut commencer ou finir au milieu d'un mot ; chaque occurrence rapporte si
  elle commence et finit à une borne de mot (caractère voisin non alphanumérique, ou bord du texte), sans en décider.
- Un extrait à cheval sur deux segments est vérifié sur le plan entier, mais n'a aucun segment porteur.

Lecture stricte : un contrôle lu « altere » ou « conforme » dont l'extrait n'est pas vérifié dans le texte lu est compté
« absent » (non étayé), et le taux de non étayés est rapporté.

Artefacts (attendus d'après le rapprochement des trois voix, § 2, table des épreuves)
- **retrait** : dans un plan honnête, retrait des segments qui portent l'extrait cité, pour un contrôle, par **l'autre**
  lignée de lecteurs (un lecteur ne se valide pas lui-même) ; attendu : ce contrôle « absent » ; les contrôles dont aucun
  extrait connu ne survit, « absents » aussi (collatéraux) ; les autres, inchangés par rapport à la lecture du plan source
  par le même lecteur (rapporté).
- **reference_permutee** : le plan de la tâche i lu contre la référence de la tâche j ≠ i (dérangement tiré par graine,
  R9) ; attendu : couverture proche de zéro, c'est-à-dire part des contrôles lus présents (lecture stricte) au plus
  `part_max`, seuil fixé au préenregistrement et exigé à l'évaluation (aucune valeur par défaut). Les contrôles de même
  description que ceux de la référence propre sont écartés du dénominateur et rapportés.
- **troncature** : plan coupé après une fraction fixée de ses mots (texte d'origine gardé caractère pour caractère jusqu'à
  la fin du dernier mot gardé) ; attendu : couverture non croissante par rapport à la lecture du plan source par le même
  lecteur (contrôles présents et conformes), et contrôles dont aucun extrait connu ne survit lus « absents ».

Limites déclarées : aucune épreuve mécanique ne teste l'altération subtile ; un contrôle porté aussi par un passage
qu'aucun lecteur n'a cité rend l'attendu « absent » faux (les extraits témoins, s'ils sont donnés, l'écartent à la
construction) ; le retrait ne renumérote rien et ne réécrit rien (un trou de numérotation peut rester visible).
"""
from __future__ import annotations

import hashlib
import json
import math
import re
from dataclasses import dataclass, field
from typing import Mapping, Sequence

import numpy as np

from ..gardes import GardeArret

SEPARATEUR = "\n\n"
STATUTS = ("absent", "altere", "conforme")
NATURES = ("retrait", "reference_permutee", "troncature")
ESSAIS_MAX_DERANGEMENT = 10_000
_ESPACES = re.compile(r"\s+")
_MOT = re.compile(r"\S+")


# --- Vérification mot pour mot ---------------------------------------------------------------------------------------

def normaliser_espaces(texte: str) -> str:
    """Seule normalisation admise : toute suite d'espacements devient une espace ; bords retirés."""
    if not isinstance(texte, str):
        raise GardeArret(f"texte attendu, pas {type(texte).__name__}")
    return _ESPACES.sub(" ", texte).strip()


def _normaliser_avec_positions(texte: str) -> tuple[str, list[int]]:
    """Texte normalisé et, pour chacun de ses caractères, sa position dans le texte d'origine (l'espace qui joint deux
    mots pointe sur le premier espacement qui les sépare)."""
    morceaux, origine = [], []
    for k, m in enumerate(_MOT.finditer(texte)):
        if k:
            morceaux.append(" ")
            origine.append(origine[-1] + 1)
        morceaux.append(m.group())
        origine.extend(range(m.start(), m.end()))
    return "".join(morceaux), origine


@dataclass(frozen=True)
class Occurrence:
    debut: int              # position dans le texte d'origine (inclus)
    fin: int                # position dans le texte d'origine (exclu)
    debut_de_mot: bool
    fin_de_mot: bool


@dataclass(frozen=True)
class VerificationExtrait:
    verifie: bool
    motif: str | None
    extrait_normalise: str
    occurrences: tuple[Occurrence, ...] = ()


def _borne(texte: str, position: int) -> bool:
    return position < 0 or position >= len(texte) or not texte[position].isalnum()


def verifier_extrait(extrait: str | None, texte: str, longueur_min: int = 1) -> VerificationExtrait:
    """L'extrait figure-t-il tel quel dans le texte, à la normalisation des espaces près ? Toutes les occurrences
    (chevauchantes comprises) sont rendues, en positions du texte d'origine."""
    if not isinstance(texte, str):
        raise GardeArret(f"texte lu de type {type(texte).__name__} : texte attendu")
    if not (isinstance(longueur_min, int) and not isinstance(longueur_min, bool) and longueur_min >= 1):
        raise GardeArret(f"longueur_min {longueur_min!r} : entier ≥ 1 attendu")
    if extrait is None:
        return VerificationExtrait(False, "extrait absent", "")
    if not isinstance(extrait, str):
        raise GardeArret(f"extrait de type {type(extrait).__name__} : texte ou None attendu")
    e = normaliser_espaces(extrait)
    if not e:
        return VerificationExtrait(False, "extrait vide", e)
    if len(e) < longueur_min:
        return VerificationExtrait(False, f"extrait trop court ({len(e)} < {longueur_min} caractères)", e)
    n, origine = _normaliser_avec_positions(texte)
    occurrences, i = [], n.find(e)
    while i >= 0:
        debut, fin = origine[i], origine[i + len(e) - 1] + 1
        occurrences.append(Occurrence(debut, fin, _borne(texte, debut - 1), _borne(texte, fin)))
        i = n.find(e, i + 1)
    if not occurrences:
        return VerificationExtrait(False, "extrait introuvable mot pour mot", e)
    return VerificationExtrait(True, None, e, tuple(occurrences))


def _exiger_segments(segments: Sequence[str]) -> tuple[str, ...]:
    if isinstance(segments, str) or not isinstance(segments, Sequence) or not segments:
        raise GardeArret("plan : suite non vide de segments de texte attendue")
    for k, s in enumerate(segments):
        if not isinstance(s, str) or not s.strip():
            raise GardeArret(f"plan : segment {k} vide ou non textuel")
    return tuple(segments)


def texte_du_plan(segments: Sequence[str]) -> str:
    return SEPARATEUR.join(_exiger_segments(segments))


def segments_porteurs(extrait: str, segments: Sequence[str], longueur_min: int = 1) -> list[int]:
    """Indices des segments qui contiennent l'extrait en entier (vérification mot pour mot)."""
    return [k for k, s in enumerate(_exiger_segments(segments)) if verifier_extrait(extrait, s, longueur_min).verifie]


# --- Référence et lecture ---------------------------------------------------------------------------------------------

def _exiger_reference(reference: Sequence[Mapping]) -> tuple[dict, ...]:
    if isinstance(reference, (str, Mapping)) or not isinstance(reference, Sequence) or not reference:
        raise GardeArret("référence : liste non vide de contrôles attendue")
    ids = []
    for k, c in enumerate(reference):
        if not isinstance(c, Mapping):
            raise GardeArret(f"référence : contrôle {k} non conforme")
        ident, desc = c.get("id"), c.get("description")
        if not isinstance(ident, str) or not ident.strip() or ident in ids:
            raise GardeArret(f"référence : identifiant absent, non textuel ou en double ({ident!r})")
        if not isinstance(desc, str) or not desc.strip():
            raise GardeArret(f"référence : contrôle {ident!r} sans description")
        ids.append(ident)
    return tuple(dict(c) for c in reference)


def _ids(reference: Sequence[Mapping]) -> list[str]:
    return [c["id"] for c in reference]


def lecture_stricte(lecture: Mapping[str, Mapping], texte: str, reference: Sequence[Mapping],
                    longueur_min: int = 1) -> dict:
    """Lecture stricte d'un lecteur sur un texte : chaque contrôle de la référence doit être lu (ni manquant, ni en
    trop) ; « altere » ou « conforme » sans extrait vérifié mot pour mot devient « absent » (non étayé)."""
    reference = _exiger_reference(reference)
    if not isinstance(lecture, Mapping):
        raise GardeArret("lecture : objet (contrôle → statut et extrait) attendu")
    attendus, lus = _ids(reference), list(lecture)
    if sorted(attendus) != sorted(lus):
        manquants = [i for i in attendus if i not in lecture]
        en_trop = [i for i in lus if i not in attendus]
        raise GardeArret(f"lecture : contrôles manquants {manquants}, en trop {en_trop}")
    par_controle = {}
    for ident in attendus:
        l = lecture[ident]
        if not isinstance(l, Mapping) or l.get("statut") not in STATUTS:
            raise GardeArret(f"lecture de {ident!r} : statut parmi {STATUTS} attendu")
        statut, extrait = l["statut"], l.get("extrait")
        if statut == "absent":
            par_controle[ident] = {"statut_lu": statut, "statut_strict": "absent", "etaye": None, "motif": None}
            continue
        v = verifier_extrait(extrait, texte, longueur_min)
        par_controle[ident] = {"statut_lu": statut, "statut_strict": statut if v.verifie else "absent",
                               "etaye": v.verifie, "motif": v.motif}
    presents = [i for i in attendus if par_controle[i]["statut_strict"] != "absent"]
    return {"controles": par_controle, "presents": presents,
            "conformes": [i for i in attendus if par_controle[i]["statut_strict"] == "conforme"],
            "non_etayes": [i for i in attendus if par_controle[i]["etaye"] is False]}


# --- Artefacts --------------------------------------------------------------------------------------------------------

def _empreinte_json(objet) -> str:
    return hashlib.sha256(json.dumps(objet, sort_keys=True, ensure_ascii=False,
                                     separators=(",", ":")).encode("utf-8")).hexdigest()


@dataclass
class Artefact:
    """Un artefact d'épreuve et son attendu. Seule `vue_aveugle()` peut être montrée à un lecteur : jamais la nature,
    l'attendu, la provenance ni le plan source."""
    nature: str
    tache_plan: str
    tache_reference: str
    segments: tuple[str, ...]
    reference: tuple[dict, ...]
    attendu: dict
    segments_source: tuple[str, ...]
    provenance: dict = field(default_factory=dict)

    @property
    def texte(self) -> str:
        return texte_du_plan(self.segments)

    @property
    def texte_source(self) -> str:
        return texte_du_plan(self.segments_source)

    def contenu(self) -> dict:
        return {"nature": self.nature, "tache_plan": self.tache_plan, "tache_reference": self.tache_reference,
                "segments": list(self.segments), "reference": list(self.reference), "attendu": self.attendu,
                "segments_source": list(self.segments_source), "provenance": self.provenance}

    @property
    def empreinte(self) -> str:
        return _empreinte_json(self.contenu())

    @property
    def identifiant(self) -> str:
        return f"{self.nature}/{self.tache_plan}/{self.empreinte[:16]}"

    def vue_aveugle(self) -> dict:
        """Ce qu'un lecteur peut recevoir : le texte du plan et la référence, rien qui dise qu'il s'agit d'un artefact."""
        return {"plan": self.texte, "reference": [dict(c) for c in self.reference]}


def _exiger_extraits(extraits: Mapping[str, str], reference: Sequence[Mapping], texte_source: str,
                     longueur_min: int, nom: str = "extraits") -> dict[str, str]:
    if not isinstance(extraits, Mapping):
        raise GardeArret(f"{nom} : objet (contrôle → extrait) attendu")
    hors = [i for i in extraits if i not in _ids(reference)]
    if hors:
        raise GardeArret(f"{nom} : contrôles hors de la référence {hors}")
    for ident, e in extraits.items():
        v = verifier_extrait(e, texte_source, longueur_min)
        if not v.verifie:
            raise GardeArret(f"{nom} de {ident!r} non vérifié dans le plan source ({v.motif}) : lecture source non "
                             "étayée, artefact non construit")
    return dict(extraits)


def _exiger_temoins(temoins: Mapping[str, Sequence[str]] | None, reference, texte_source: str,
                    longueur_min: int) -> dict[str, list[str]]:
    if temoins is None:
        return {}
    if not isinstance(temoins, Mapping):
        raise GardeArret("extraits témoins : objet (contrôle → liste d'extraits) attendu")
    sortie = {}
    for ident, liste in temoins.items():
        if isinstance(liste, str) or not isinstance(liste, Sequence):
            raise GardeArret(f"extraits témoins de {ident!r} : liste attendue")
        for e in liste:
            _exiger_extraits({ident: e}, reference, texte_source, longueur_min, "extrait témoin")
        sortie[ident] = list(liste)
    return sortie


def _connus(extraits: Mapping[str, str], temoins: Mapping[str, list[str]]) -> dict[str, list[str]]:
    connus: dict[str, list[str]] = {}
    for ident, e in extraits.items():
        connus.setdefault(ident, []).append(e)
    for ident, liste in temoins.items():
        connus.setdefault(ident, []).extend(liste)
    return connus


def _classer(reference, connus: Mapping[str, list[str]], texte: str, longueur_min: int) -> tuple[list, list, list]:
    """(perdus, conserves, sans_extrait) : perdu = aucun extrait connu ne survit dans le texte ; dans l'ordre de la
    référence."""
    perdus, conserves, sans = [], [], []
    for ident in _ids(reference):
        if ident not in connus:
            sans.append(ident)
        elif any(verifier_extrait(e, texte, longueur_min).verifie for e in connus[ident]):
            conserves.append(ident)
        else:
            perdus.append(ident)
    return perdus, conserves, sans


def _exiger_lignee(lignee) -> str:
    if not isinstance(lignee, str) or not lignee.strip():
        raise GardeArret("lignée des extraits : nom non vide attendu (famille du lecteur qui les a cités)")
    return lignee.strip()


def artefact_retrait(tache: str, segments: Sequence[str], reference: Sequence[Mapping], controle: str,
                     extraits: Mapping[str, str], lignee_extraits: str,
                     extraits_temoins: Mapping[str, Sequence[str]] | None = None, longueur_min: int = 1) -> Artefact:
    """Retrait, d'un plan honnête, des segments qui portent l'extrait du contrôle `controle` cité par la lignée
    `lignee_extraits` (l'autre lignée que celle du lecteur éprouvé). `extraits` : extraits de cette lignée sur le plan
    source (un par contrôle lu présent) ; `extraits_temoins` : autres extraits connus (toute lignée, ancre humaine),
    qui ne servent qu'à refuser un retrait dont le contrôle survivrait ailleurs et à classer les autres contrôles."""
    source = _exiger_segments(segments)
    reference = _exiger_reference(reference)
    lignee = _exiger_lignee(lignee_extraits)
    texte_source = texte_du_plan(source)
    extraits = _exiger_extraits(extraits, reference, texte_source, longueur_min)
    temoins = _exiger_temoins(extraits_temoins, reference, texte_source, longueur_min)
    if controle not in extraits:
        raise GardeArret(f"contrôle {controle!r} sans extrait de la lignée {lignee} : rien à retirer")
    porteurs = segments_porteurs(extraits[controle], source, longueur_min)
    if not porteurs:
        raise GardeArret(f"extrait de {controle!r} à cheval sur plusieurs segments : aucun segment porteur")
    restants = tuple(s for k, s in enumerate(source) if k not in porteurs)
    if not restants:
        raise GardeArret(f"retrait de {controle!r} : tous les segments le portent, plan vide")
    texte = texte_du_plan(restants)
    survivants = [e for e in _connus(extraits, temoins).get(controle, []) if verifier_extrait(e, texte,
                                                                                              longueur_min).verifie]
    if survivants:
        raise GardeArret(f"retrait de {controle!r} : {len(survivants)} extrait(s) connu(s) restent dans le plan après "
                         "retrait (contrôle porté ailleurs, ou extrait recréé à la jointure de deux segments)")
    perdus, conserves, sans = _classer(reference, _connus(extraits, temoins), texte, longueur_min)
    attendu = {"regle": "le contrôle retiré est lu « absent » (lecture stricte) ; les collatéraux aussi ; les autres, "
                        "inchangés par rapport à la lecture du plan source par le même lecteur (rapporté)",
               "cible": controle, "absents": perdus, "collateraux": [i for i in perdus if i != controle],
               "inchanges": conserves, "sans_extrait": sans, "segments_retires": porteurs}
    return Artefact("retrait", tache, tache, restants, reference, attendu, source,
                    {"lignee_extraits": lignee, "longueur_min": longueur_min,
                     "empreinte_plan_source": _empreinte_json(list(source)),
                     "empreinte_reference": _empreinte_json(list(reference))})


def derangement(identifiants: Sequence[str], graine: int) -> dict[str, str]:
    """Permutation sans point fixe des tâches (i → j ≠ i), tirée uniformément parmi les dérangements par rejet, avec un
    générateur `numpy` né de `SeedSequence(graine)` (R9) ; indépendante de l'ordre d'entrée (identifiants triés)."""
    ids = sorted(identifiants)
    if len(set(ids)) != len(ids):
        raise GardeArret("identifiants de tâches en double")
    if len(ids) < 2:
        raise GardeArret("au moins deux tâches pour permuter les références")
    if not (isinstance(graine, int) and not isinstance(graine, bool) and graine >= 0):
        raise GardeArret(f"graine {graine!r} : entier positif ou nul attendu")
    rng = np.random.default_rng(np.random.SeedSequence(graine))
    for _ in range(ESSAIS_MAX_DERANGEMENT):
        p = rng.permutation(len(ids))
        if all(p[k] != k for k in range(len(ids))):
            return {ids[k]: ids[int(p[k])] for k in range(len(ids))}
    raise GardeArret(f"aucun dérangement en {ESSAIS_MAX_DERANGEMENT} essais")


def artefact_reference_permutee(tache_plan: str, segments: Sequence[str], tache_reference: str,
                                reference_autre: Sequence[Mapping], reference_propre: Sequence[Mapping],
                                graine: int | None = None) -> Artefact:
    """Plan de `tache_plan` lu contre la référence d'une autre tâche. Les contrôles de même description (normalisation
    des espaces, casse ignorée) qu'un contrôle de la référence propre sont rapportés et sortent du dénominateur."""
    source = _exiger_segments(segments)
    autre, propre = _exiger_reference(reference_autre), _exiger_reference(reference_propre)
    if tache_plan == tache_reference:
        raise GardeArret(f"référence permutée : la tâche {tache_plan!r} reçoit sa propre référence")
    descriptions_propres = {normaliser_espaces(c["description"]).casefold() for c in propre}
    communs = [c["id"] for c in autre if normaliser_espaces(c["description"]).casefold() in descriptions_propres]
    if len(communs) == len(autre):
        raise GardeArret(f"référence de {tache_reference!r} identique à celle de {tache_plan!r} : aucun contrôle étranger")
    attendu = {"regle": "part des contrôles étrangers lus présents (lecture stricte) au plus part_max, seuil fixé au "
                        "préenregistrement", "communs_avec_la_reference_propre": communs,
               "etrangers": [i for i in _ids(autre) if i not in communs]}
    return Artefact("reference_permutee", tache_plan, tache_reference, source, autre, attendu, source,
                    {"graine_derangement": graine, "empreinte_plan_source": _empreinte_json(list(source)),
                     "empreinte_reference": _empreinte_json(list(autre)),
                     "empreinte_reference_propre": _empreinte_json(list(propre))})


def artefacts_reference_permutee(plans: Mapping[str, Sequence[str]], references: Mapping[str, Sequence[Mapping]],
                                 graine: int) -> list[Artefact]:
    """Un artefact par tâche : son plan lu contre la référence de son image par un dérangement tiré par graine."""
    if set(plans) != set(references):
        raise GardeArret(f"plans et références de tâches différentes : {sorted(set(plans) ^ set(references))}")
    d = derangement(list(plans), graine)
    return [artefact_reference_permutee(i, plans[i], d[i], references[d[i]], references[i], graine) for i in sorted(d)]


def artefact_troncature(tache: str, segments: Sequence[str], reference: Sequence[Mapping], fraction: float,
                        extraits: Mapping[str, str] | None = None, lignee_extraits: str | None = None,
                        extraits_temoins: Mapping[str, Sequence[str]] | None = None,
                        longueur_min: int = 1) -> Artefact:
    """Plan coupé après ⌊fraction × n⌋ de ses n mots (mots : suites sans espacement, comptées sur tous les segments
    dans l'ordre) ; les segments entiers avant la coupe sont gardés tels quels, le segment coupé l'est à la fin de son
    dernier mot gardé. Avec des extraits connus du plan source, l'attendu nomme les contrôles perdus."""
    source = _exiger_segments(segments)
    reference = _exiger_reference(reference)
    if not (isinstance(fraction, (int, float)) and not isinstance(fraction, bool) and math.isfinite(fraction)
            and 0.0 < fraction < 1.0):
        raise GardeArret(f"fraction {fraction!r} : réel dans ]0, 1[ attendu")
    mots = [list(_MOT.finditer(s)) for s in source]
    n = sum(len(m) for m in mots)
    k = math.floor(fraction * n)
    if not 1 <= k < n:
        raise GardeArret(f"troncature à {k} mots sur {n} : au moins un mot gardé et un mot retiré attendus")
    gardes, reste = [], k
    for s, m in zip(source, mots):
        if reste >= len(m):
            gardes.append(s)
            reste -= len(m)
            if reste == 0:
                break
        else:
            gardes.append(s[:m[reste - 1].end()])
            break
    tronque = tuple(gardes)
    texte = texte_du_plan(tronque)
    perdus, conserves, sans = [], [], _ids(reference)
    lignee = None
    if extraits is not None:
        lignee = _exiger_lignee(lignee_extraits)
        texte_source = texte_du_plan(source)
        ex = _exiger_extraits(extraits, reference, texte_source, longueur_min)
        tem = _exiger_temoins(extraits_temoins, reference, texte_source, longueur_min)
        perdus, conserves, sans = _classer(reference, _connus(ex, tem), texte, longueur_min)
    elif extraits_temoins is not None or lignee_extraits is not None:
        raise GardeArret("extraits témoins ou lignée sans extraits : rien à classer")
    attendu = {"regle": "contrôles présents et conformes (lecture stricte) non croissants par rapport à la lecture du "
                        "plan source par le même lecteur ; contrôles perdus lus « absents »",
               "fraction": float(fraction), "mots_gardes": k, "mots_source": n, "perdus": perdus,
               "conserves": conserves, "sans_extrait": sans}
    return Artefact("troncature", tache, tache, tronque, reference, attendu, source,
                    {"lignee_extraits": lignee, "longueur_min": longueur_min,
                     "empreinte_plan_source": _empreinte_json(list(source)),
                     "empreinte_reference": _empreinte_json(list(reference))})


# --- Évaluation d'une lecture d'artefact -------------------------------------------------------------------------------

def evaluer_artefact(artefact: Artefact, lecture: Mapping[str, Mapping], lignee_lecteur: str,
                     lecture_source: Mapping[str, Mapping] | None = None, part_max: float | None = None,
                     longueur_min: int = 1) -> dict:
    """Le vérificateur (lecteur et programme) a-t-il détecté l'artefact ? `lecture` : lecture de `vue_aveugle()` ;
    `lecture_source` : lecture du plan source par le même lecteur (exigée pour la troncature, rapportée pour le
    retrait) ; `part_max` : seuil de la référence permutée (exigé pour elle, sans défaut)."""
    if artefact.nature not in NATURES:
        raise GardeArret(f"nature {artefact.nature!r} inconnue ({NATURES})")
    lignee = _exiger_lignee(lignee_lecteur)
    if artefact.provenance.get("lignee_extraits") == lignee:
        raise GardeArret(f"lecteur de la lignée {lignee} éprouvé sur un artefact construit avec ses propres extraits")
    lu = lecture_stricte(lecture, artefact.texte, artefact.reference, longueur_min)
    source = (lecture_stricte(lecture_source, artefact.texte_source, artefact.reference, longueur_min)
              if lecture_source is not None else None)
    sortie = {"nature": artefact.nature, "identifiant": artefact.identifiant, "empreinte": artefact.empreinte,
              "lignee_lecteur": lignee, "presents": lu["presents"], "conformes": lu["conformes"],
              "non_etayes": lu["non_etayes"]}
    a = artefact.attendu
    statut = {i: lu["controles"][i]["statut_strict"] for i in lu["controles"]}
    if artefact.nature == "retrait":
        sortie["detecte"] = statut[a["cible"]] == "absent"
        sortie["collateraux_non_absents"] = [i for i in a["collateraux"] if statut[i] != "absent"]
        if source is not None:
            avant = {i: source["controles"][i]["statut_strict"] for i in source["controles"]}
            sortie["inchanges_changes"] = [i for i in a["inchanges"] if statut[i] != avant[i]]
    elif artefact.nature == "reference_permutee":
        if part_max is None or isinstance(part_max, bool) or not (isinstance(part_max, (int, float))
                                                                   and 0.0 <= part_max < 1.0):
            raise GardeArret(f"part_max {part_max!r} : seuil du préenregistrement dans [0, 1) exigé")
        etrangers = a["etrangers"]
        part = sum(statut[i] != "absent" for i in etrangers) / len(etrangers)
        sortie.update(part_presents=part, detecte=part <= part_max)
    else:
        if source is None:
            raise GardeArret("troncature : lecture du plan source par le même lecteur exigée")
        perdus_lus = [i for i in a["perdus"] if statut[i] != "absent"]
        gains = [i for i in source["controles"] if source["controles"][i]["statut_strict"] == "absent"
                 and statut[i] != "absent"]
        non_croissante = (len(lu["presents"]) <= len(source["presents"])
                          and len(lu["conformes"]) <= len(source["conformes"]))
        sortie.update(perdus_lus_presents=perdus_lus, gains=gains, couverture_non_croissante=non_croissante,
                      detecte=non_croissante and not perdus_lus)
    return sortie
