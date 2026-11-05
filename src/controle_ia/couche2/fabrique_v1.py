"""Journal de fabrique des épisodes de la couche 2, ordre scellé d'avance, palier de rythme — v1 (P-23, P-28).

Sources (lues le 29 octobre 2026) :
- P-23 (E-5) du format décision v5 de conv-audit (`decision-pilote-couche-2-v5.md`, `255a364e…`, sur
  `refs/canal-local/conv-audit`) : « journal de fabrique (instance, horodatage, rang), ordre scellé, palier de rythmes
  (16 épisodes, arrêt au-delà de 189 s), au pilote comme à la banque. Défaut : obligatoires. »
- P-28 (2), même pièce : le palier de 189 s se lit en « secondes d'instance par épisode, génération comprise » ; au-delà,
  c'est un nœud de devis (P-14), jamais un relèvement silencieux. Le devis v1 de session-depot l'avait lu « moniteurs
  seuls » (`devis-pilote-couche-2-v1.md`, § 2.1) ; le devis v2 a repris la lecture de conv-audit.
- Synthèse du tour complémentaire du collisionneur (`synthese-pilote-complement-v1.md`, `5bde106a…`, § 3.1, A) :
  ordre tiré par graine ; journal (instance, horodatage, rang, version, cache).

Ce module ne fixe aucune valeur par une constante cachée : le seuil, la lecture (« génération comprise » ou « moniteurs
seuls »), la règle (« chaque épisode » ou « moyenne du palier »), la taille du palier et la liste des postes sont des
arguments obligatoires de `PalierRythme`. `palier_p23_p28` construit le palier aux valeurs sourcées, avec la règle,
qui n'est écrite nulle part, en argument obligatoire.

Format du journal : une ligne JSON canonique par événement (clés triées, sans espace), ajout seul. Chaque ligne porte
`n` (numéro consécutif), `type`, `horodatage` (UTC, ISO 8601), `precedent` (empreinte de la ligne précédente ; 64 zéros
pour la première), `contenu` et `empreinte` (sha256 de la ligne canonique sans le champ `empreinte`). Une ligne réécrite,
une chaîne cassée, un trou dans l'ordre, une ligne tronquée ou un ajout après la clôture lèvent `JournalCorrompu`.
La dernière ligne n'est protégée contre une réécriture complète (empreinte recalculée) que par une ancre tenue ailleurs
(`ancre()`, à consigner hors du journal) ou par le scellement à la clôture (`clore()`).

Ordre : liste de blocs joués l'un après l'autre (par exemple le palier : un épisode du lot D par tâche ; puis le reste),
chaque bloc permuté par une graine dérivée de l'entropie de l'ordre ; chaque épisode reçoit sa graine dérivée par
`numpy.random.SeedSequence` de (lot, tâche, exécution) (R9). Le fichier d'ordre est scellé (R6) et son empreinte est
engagée dans la première ligne du journal, avant toute génération. Au chargement, l'ordre est retiré de son entropie et
comparé : un ordre retouché à la main est refusé.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

import numpy as np

from ..gardes import GardeArret, exiger_numpy_minimal
from ..manifeste import cle_de_tache, generateur
from ..scellement import compagnon, sceller, verifier

VERSION = "fabrique-v1"
VERSION_ORDRE = "ordre-episodes-v1"
ZERO = "0" * 64
_HEX64 = re.compile(r"^[0-9a-f]{64}$")

# Valeurs sourcées (voir l'en-tête) ; elles n'entrent dans un palier que par `palier_p23_p28`, jamais par défaut.
SEUIL_P23_SECONDES = 189.0
TAILLE_PALIER_P23 = 16
LECTURE_P28 = "generation_comprise"
LECTURES = ("generation_comprise", "moniteurs_seuls")
REGLES = ("chaque_episode", "moyenne_du_palier")
POSTE_GENERATION = "generation"

CLE_ORDRE = cle_de_tache(f"{VERSION_ORDRE}:permutation")
CLE_EPISODE = cle_de_tache(f"{VERSION_ORDRE}:episode")

TYPES = ("ouverture", "debut", "episode", "interruption", "palier_lu", "arret_palier", "cloture")


class JournalCorrompu(GardeArret):
    """Le journal ne passe pas la vérification d'intégrité (chaîne, réécriture, trou d'ordre, troncature, sceau)."""


class HorsOrdre(GardeArret):
    """Génération demandée hors de l'ordre scellé."""


class ArretPalier(GardeArret):
    """Le palier de rythme a sonné : arrêt écrit au journal, nœud de devis (P-14). Ne jamais l'attraper pour continuer."""


def _canonique(obj) -> str:
    return json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":"), allow_nan=False)


def _sha(texte: str) -> str:
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def maintenant_utc() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="microseconds")


def _lire_horodatage(h, ou: str) -> datetime:
    if not isinstance(h, str):
        raise JournalCorrompu(f"{ou} : horodatage absent ou non textuel")
    try:
        d = datetime.fromisoformat(h)
    except ValueError:
        raise JournalCorrompu(f"{ou} : horodatage illisible {h!r}") from None
    if d.tzinfo is None or d.utcoffset().total_seconds() != 0:
        raise JournalCorrompu(f"{ou} : horodatage {h!r} hors UTC")
    return d


# --------------------------------------------------------------------------------------------------------------------
# Palier de rythme
# --------------------------------------------------------------------------------------------------------------------

@dataclass(frozen=True)
class PalierRythme:
    """Palier de rythme : `n_episodes` premiers rangs mesurés, arrêt écrit au-delà de `seuil_s` (strictement).

    - `lecture` : « generation_comprise » (somme de tous les postes) ou « moniteurs_seuls » (tous sauf `generation`) ;
    - `regle` : « chaque_episode » (un seul épisode du palier au-delà suffit, arrêt aussitôt) ou « moyenne_du_palier »
      (moyenne des `n_episodes` rythmes, lue quand le palier est complet) ;
    - `postes` : postes chronométrés, `generation` compris ; chaque épisode doit les donner tous, ni plus ni moins.
    """
    seuil_s: float
    lecture: str
    regle: str
    n_episodes: int
    postes: tuple[str, ...]

    def __post_init__(self):
        if not isinstance(self.seuil_s, (int, float)) or isinstance(self.seuil_s, bool) or not math.isfinite(
                self.seuil_s) or self.seuil_s <= 0:
            raise GardeArret(f"palier : seuil {self.seuil_s!r} invalide (réel fini > 0 exigé)")
        if self.lecture not in LECTURES:
            raise GardeArret(f"palier : lecture {self.lecture!r} inconnue ({', '.join(LECTURES)})")
        if self.regle not in REGLES:
            raise GardeArret(f"palier : règle {self.regle!r} inconnue ({', '.join(REGLES)})")
        if not isinstance(self.n_episodes, int) or isinstance(self.n_episodes, bool) or self.n_episodes < 1:
            raise GardeArret(f"palier : taille {self.n_episodes!r} invalide (entier ≥ 1)")
        postes = tuple(self.postes)
        if POSTE_GENERATION not in postes:
            raise GardeArret(f"palier : le poste {POSTE_GENERATION!r} doit être chronométré")
        if len(set(postes)) != len(postes) or any(not isinstance(p, str) or not p for p in postes):
            raise GardeArret(f"palier : postes en double ou vides : {postes}")
        if len(postes) < 2:
            raise GardeArret("palier : au moins un moniteur doit être chronométré en plus de la génération")
        object.__setattr__(self, "postes", postes)

    def en_dict(self) -> dict:
        return {"seuil_s": float(self.seuil_s), "lecture": self.lecture, "regle": self.regle,
                "n_episodes": self.n_episodes, "postes": list(self.postes)}

    @classmethod
    def depuis_dict(cls, d: dict) -> "PalierRythme":
        return cls(seuil_s=d["seuil_s"], lecture=d["lecture"], regle=d["regle"], n_episodes=d["n_episodes"],
                   postes=tuple(d["postes"]))

    def exiger_secondes(self, secondes: dict) -> dict:
        if not isinstance(secondes, dict):
            raise GardeArret("secondes par poste : dictionnaire exigé")
        manquants = [p for p in self.postes if p not in secondes]
        en_trop = [p for p in secondes if p not in self.postes]
        if manquants or en_trop:
            raise GardeArret(f"secondes par poste : manquants {manquants}, inattendus {en_trop} (aucun repli)")
        sortie = {}
        for p in self.postes:
            v = secondes[p]
            if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) or v < 0:
                raise GardeArret(f"secondes du poste {p!r} : {v!r} invalide (réel fini ≥ 0 exigé)")
            sortie[p] = float(v)
        return sortie

    def rythme(self, secondes: dict) -> float:
        s = self.exiger_secondes(secondes)
        if self.lecture == "generation_comprise":
            return float(sum(s[p] for p in self.postes))
        return float(sum(s[p] for p in self.postes if p != POSTE_GENERATION))

    def evaluer(self, rythmes: list[float]) -> dict:
        """Verdict sur les rythmes déjà mesurés des rangs du palier (dans l'ordre). `lu` : verdict acquis."""
        r = [float(x) for x in rythmes[: self.n_episodes]]
        if self.regle == "chaque_episode":
            au_dela = [i for i, x in enumerate(r) if x > self.seuil_s]
            if au_dela:
                return {"lu": True, "sonne": True, "regle": self.regle, "rangs_au_dela": au_dela,
                        "valeur": r[au_dela[0]], "n_mesures": len(r)}
            lu = len(r) >= self.n_episodes
            return {"lu": lu, "sonne": False, "regle": self.regle, "rangs_au_dela": [],
                    "valeur": max(r) if r else None, "n_mesures": len(r)}
        if len(r) < self.n_episodes:
            return {"lu": False, "sonne": False, "regle": self.regle, "valeur": None, "n_mesures": len(r)}
        moyenne = float(np.mean(r))
        return {"lu": True, "sonne": moyenne > self.seuil_s, "regle": self.regle, "valeur": moyenne,
                "n_mesures": len(r)}


def palier_p23_p28(*, regle: str, postes: tuple[str, ...] | list[str]) -> PalierRythme:
    """Palier aux valeurs sourcées : 189 s, 16 épisodes (P-23), génération comprise (P-28 (2)). La règle n'est écrite
    nulle part : argument obligatoire, à fixer au préenregistrement."""
    return PalierRythme(seuil_s=SEUIL_P23_SECONDES, lecture=LECTURE_P28, regle=regle, n_episodes=TAILLE_PALIER_P23,
                        postes=tuple(postes))


# --------------------------------------------------------------------------------------------------------------------
# Ordre scellé
# --------------------------------------------------------------------------------------------------------------------

def bloc(nom: str, lot: str, taches: list[str], executions: list[int] | range) -> dict:
    """Un bloc : toutes les paires (tâche, exécution) d'un lot, jouées dans un ordre permuté par graine."""
    return {"nom": nom, "elements": [{"lot": lot, "tache": t, "execution": int(e)} for t in taches
                                     for e in executions]}


def _exiger_blocs(blocs: list[dict]) -> None:
    if not isinstance(blocs, list) or not blocs:
        raise GardeArret("ordre : liste de blocs non vide exigée")
    noms, vus = set(), set()
    for b in blocs:
        if not isinstance(b, dict) or set(b) != {"nom", "elements"}:
            raise GardeArret(f"ordre : bloc mal formé {b!r}")
        if b["nom"] in noms:
            raise GardeArret(f"ordre : bloc {b['nom']!r} en double")
        noms.add(b["nom"])
        if not b["elements"]:
            raise GardeArret(f"ordre : bloc {b['nom']!r} vide")
        for el in b["elements"]:
            if set(el) != {"lot", "tache", "execution"}:
                raise GardeArret(f"ordre : élément mal formé {el!r}")
            if not isinstance(el["lot"], str) or not el["lot"] or not isinstance(el["tache"], str) or not el["tache"]:
                raise GardeArret(f"ordre : lot et tâche textuels non vides exigés {el!r}")
            if isinstance(el["execution"], bool) or not isinstance(el["execution"], int) or el["execution"] < 0:
                raise GardeArret(f"ordre : exécution entière ≥ 0 exigée {el!r}")
            cle = (el["lot"], el["tache"], el["execution"])
            if cle in vus:
                raise GardeArret(f"ordre : épisode {cle} en double (lot, tâche, exécution)")
            vus.add(cle)


def graine_episode(entropie: int, lot: str, tache: str, execution: int) -> dict:
    """Graine d'un épisode, dérivée de l'entropie de l'ordre et de (lot, tâche, exécution) ; lisible par
    `manifeste.generateur`."""
    cle = (CLE_EPISODE, cle_de_tache(lot), cle_de_tache(tache), int(execution))
    ss = np.random.SeedSequence(int(entropie), spawn_key=cle)
    return {"entropie": str(int(entropie)), "spawn_key": [str(k) for k in cle],
            "etat_controle": [int(x) for x in ss.generate_state(2)]}


def tirer_ordre(blocs: list[dict], entropie: int | None) -> dict:
    """Tire l'ordre : chaque bloc trié canoniquement puis permuté par sa graine ; blocs joués dans l'ordre donné.
    `entropie=None` tire une entropie neuve, consignée dans l'ordre (R9)."""
    exiger_numpy_minimal()
    _exiger_blocs(blocs)
    racine = np.random.SeedSequence(entropie)
    ent = int(racine.entropy)
    elements, rang = [], 0
    for i, b in enumerate(blocs):
        tries = sorted(b["elements"], key=lambda e: (e["lot"], e["tache"], e["execution"]))
        rng = np.random.default_rng(np.random.SeedSequence(ent, spawn_key=(CLE_ORDRE, i)))
        for j in rng.permutation(len(tries)):
            el = tries[int(j)]
            elements.append({"rang": rang, "bloc": b["nom"], "lot": el["lot"], "tache": el["tache"],
                             "execution": el["execution"],
                             "graine": graine_episode(ent, el["lot"], el["tache"], el["execution"])})
            rang += 1
    return {"version": VERSION_ORDRE, "entropie": str(ent), "blocs": blocs, "elements": elements}


def empreinte_ordre(ordre: dict) -> str:
    return _sha(_canonique(ordre))


def exiger_ordre_retire(ordre: dict) -> str:
    """Retire l'ordre de son entropie et de ses blocs ; refuse toute différence (ordre retouché à la main)."""
    if not isinstance(ordre, dict) or ordre.get("version") != VERSION_ORDRE:
        raise GardeArret(f"ordre : version {ordre.get('version') if isinstance(ordre, dict) else None!r} "
                         f"≠ {VERSION_ORDRE!r}")
    try:
        ent = int(ordre["entropie"])
    except (KeyError, TypeError, ValueError):
        raise GardeArret("ordre : entropie absente ou illisible") from None
    retire = tirer_ordre(ordre["blocs"], ent)
    if _canonique(retire) != _canonique(ordre):
        raise GardeArret("ordre : ne se retire pas de son entropie et de ses blocs (retouché à la main ?)")
    return empreinte_ordre(ordre)


def ecrire_ordre(chemin: str | Path, ordre: dict) -> str:
    """Écrit l'ordre (JSON canonique) et le scelle (R6). Refuse d'écraser (R12). Renvoie l'empreinte du fichier."""
    p = Path(chemin)
    if p.exists() or compagnon(p).exists():
        raise GardeArret(f"{p} existe déjà : R12 interdit d'écraser un ordre")
    exiger_ordre_retire(ordre)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(_canonique(ordre) + "\n", encoding="utf-8")
    return sceller(p)


def charger_ordre(chemin: str | Path) -> tuple[dict, str]:
    """Vérifie le sceau du fichier d'ordre, puis le retire de sa graine. Renvoie (ordre, empreinte du fichier)."""
    sha_fichier = verifier(chemin)
    try:
        ordre = json.loads(Path(chemin).read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise GardeArret(f"{chemin} : ordre illisible ({e})") from None
    exiger_ordre_retire(ordre)
    return ordre, sha_fichier


# --------------------------------------------------------------------------------------------------------------------
# Journal
# --------------------------------------------------------------------------------------------------------------------

def _ligne(n: int, type_: str, horodatage: str, precedent: str, contenu: dict) -> tuple[str, str]:
    corps = {"n": n, "type": type_, "horodatage": horodatage, "precedent": precedent, "contenu": contenu}
    emp = _sha(_canonique(corps))
    corps["empreinte"] = emp
    return _canonique(corps), emp


def _exiger_texte(v, nom: str) -> str:
    if not isinstance(v, str) or not v.strip():
        raise GardeArret(f"{nom} : texte non vide exigé (aucun repli)")
    return v


class JournalFabrique:
    """Journal de fabrique d'une instance : ouverture (ordre engagé), puis pour chaque rang `debut` → `episode`,
    lecture du palier, arrêt écrit s'il sonne, clôture scellée. Toute génération hors de l'ordre est refusée."""

    def __init__(self, chemin: Path, ordre: dict, palier: PalierRythme, instance: str, *,
                 horloge: Callable[[], str]):
        self.chemin = chemin
        self.ordre = ordre
        self.palier = palier
        self.instance = instance
        self._horloge = horloge
        self._n = 0
        self._dernier = ZERO
        self._taille = 0
        self._dernier_horodatage: datetime | None = None
        self.prochain_rang = 0
        self.en_cours: int | None = None
        self.rythmes: list[float] = []
        self.palier_lu = False
        self.arrete: dict | None = None
        self.clos = False

    # -- création et reprise --------------------------------------------------------------------------------------

    @classmethod
    def creer(cls, chemin: str | Path, chemin_ordre: str | Path, palier: PalierRythme, *, instance: str,
              run_id: str, horloge: Callable[[], str] = maintenant_utc) -> "JournalFabrique":
        """Ouvre un journal neuf. L'ordre est relu sur disque (sceau, retirage) et son empreinte engagée en ligne 0."""
        p = Path(chemin)
        if p.exists() or compagnon(p).exists():
            raise GardeArret(f"{p} existe déjà : R12 interdit d'écraser un journal (reprendre avec `reprendre`)")
        if not isinstance(palier, PalierRythme):
            raise GardeArret("palier : instance de PalierRythme exigée")
        ordre, sha_fichier = charger_ordre(chemin_ordre)
        if palier.n_episodes > len(ordre["elements"]):
            raise GardeArret(f"palier de {palier.n_episodes} épisodes plus long que l'ordre "
                             f"({len(ordre['elements'])}) : il ne pourrait jamais être lu")
        j = cls(p, ordre, palier, _exiger_texte(instance, "instance"), horloge=horloge)
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "x", encoding="utf-8"):
            pass
        j._ajouter("ouverture", {
            "version": VERSION, "run_id": _exiger_texte(run_id, "run_id"), "instance": j.instance,
            "ordre_chemin": str(chemin_ordre), "ordre_fichier_sha256": sha_fichier,
            "ordre_sha256": empreinte_ordre(ordre), "n_elements": len(ordre["elements"]), "ordre": ordre,
            "palier": palier.en_dict()})
        return j

    @classmethod
    def reprendre(cls, chemin: str | Path, *, ancre_attendue: str, motif_interruption: str | None = None,
                  horloge: Callable[[], str] = maintenant_utc) -> "JournalFabrique":
        """Relit et vérifie le journal, puis reprend l'ajout. `ancre_attendue` : empreinte de la dernière ligne tenue
        ailleurs (protège la dernière ligne). Un épisode commencé sans fin exige un motif d'interruption, consigné."""
        lecture = lire_journal(chemin, ancre_attendue=ancre_attendue)
        if lecture["clos"]:
            raise GardeArret(f"{chemin} : journal clos et scellé, aucun ajout permis")
        if lecture["arret"] is not None:
            raise ArretPalier(f"{chemin} : le palier a sonné ({lecture['arret']['motif']}) ; aucune reprise sans "
                              "décision écrite (nœud de devis)")
        o = lecture["ouverture"]
        j = cls(Path(chemin), o["ordre"], PalierRythme.depuis_dict(o["palier"]), o["instance"], horloge=horloge)
        j._n = lecture["n_lignes"]
        j._dernier = lecture["ancre"]
        j._taille = Path(chemin).stat().st_size
        j._dernier_horodatage = _lire_horodatage(lecture["lignes"][-1]["horodatage"], "reprise")
        j.prochain_rang = lecture["prochain_rang"]
        j.rythmes = [e["rythme_palier"] for e in lecture["episodes"] if e["rang"] < j.palier.n_episodes]
        j.palier_lu = lecture["palier_lu"] is not None
        if lecture["en_cours"] is not None:
            if motif_interruption is None:
                raise GardeArret(f"{chemin} : rang {lecture['en_cours']} commencé sans fin ; reprise refusée sans "
                                 "motif d'interruption écrit")
            j._ajouter("interruption", {"rang": lecture["en_cours"],
                                        "motif": _exiger_texte(motif_interruption, "motif d'interruption")})
        return j

    # -- écriture --------------------------------------------------------------------------------------------------

    def _ajouter(self, type_: str, contenu: dict) -> str:
        if self.clos:
            raise GardeArret(f"{self.chemin} : journal clos, aucun ajout")
        taille = self.chemin.stat().st_size
        if taille != self._taille:
            raise JournalCorrompu(f"{self.chemin} : taille {taille} ≠ {self._taille} attendue (écrit par un tiers ?)")
        h = self._horloge()
        d = _lire_horodatage(h, f"{self.chemin} (horloge)")
        if self._dernier_horodatage is not None and d < self._dernier_horodatage:
            raise GardeArret(f"horloge en recul : {h} avant {self._dernier_horodatage.isoformat()}")
        ligne, emp = _ligne(self._n, type_, h, self._dernier, contenu)
        donnees = (ligne + "\n").encode("utf-8")
        with open(self.chemin, "ab") as f:
            f.write(donnees)
            f.flush()
            os.fsync(f.fileno())
        self._n += 1
        self._dernier = emp
        self._taille += len(donnees)
        self._dernier_horodatage = d
        return emp

    def ancre(self) -> str:
        """Empreinte de la dernière ligne : à consigner hors du journal (ligne de progrès, registre)."""
        return self._dernier

    def _exiger_actif(self) -> None:
        if self.arrete is not None:
            raise ArretPalier(f"palier sonné au rang {self.arrete['rang']} : aucune génération (nœud de devis)")
        if self.clos:
            raise GardeArret("journal clos : aucune génération")

    def debut(self, rang: int) -> tuple[dict, np.random.Generator]:
        """Autorise la génération du rang demandé s'il est le suivant de l'ordre scellé ; écrit `debut`.
        Renvoie l'élément de l'ordre et le générateur de sa graine."""
        self._exiger_actif()
        if self.en_cours is not None:
            raise HorsOrdre(f"rang {self.en_cours} encore en cours : terminer avant de commencer {rang}")
        if isinstance(rang, bool) or not isinstance(rang, int) or rang != self.prochain_rang:
            raise HorsOrdre(f"rang {rang!r} demandé, {self.prochain_rang} attendu (ordre scellé)")
        if rang >= len(self.ordre["elements"]):
            raise HorsOrdre(f"rang {rang} : l'ordre scellé est épuisé ({len(self.ordre['elements'])} éléments)")
        el = self.ordre["elements"][rang]
        self._ajouter("debut", {"rang": rang, "lot": el["lot"], "tache": el["tache"], "execution": el["execution"],
                                "graine": el["graine"], "instance": self.instance})
        self.en_cours = rang
        return el, generateur(el["graine"])

    def fin(self, rang: int, *, secondes: dict, version: str, cache: str, empreinte_sortie: str) -> dict:
        """Consigne l'épisode (postes chronométrés, version, état du cache, empreinte de la sortie), puis lit le palier.
        S'il sonne : `arret_palier` est écrit, puis `ArretPalier` est levée."""
        self._exiger_actif()
        if self.en_cours is None or rang != self.en_cours:
            raise HorsOrdre(f"fin du rang {rang!r} sans début correspondant (en cours : {self.en_cours})")
        if not isinstance(empreinte_sortie, str) or not _HEX64.match(empreinte_sortie):
            raise GardeArret(f"empreinte de la sortie {empreinte_sortie!r} : sha256 hexadécimal exigé")
        s = self.palier.exiger_secondes(secondes)
        rythme = self.palier.rythme(s)
        el = self.ordre["elements"][rang]
        contenu = {"rang": rang, "lot": el["lot"], "tache": el["tache"], "execution": el["execution"],
                   "instance": self.instance, "version": _exiger_texte(version, "version"),
                   "cache": _exiger_texte(cache, "cache"), "secondes": s, "rythme_palier": rythme,
                   "lecture_palier": self.palier.lecture, "empreinte_sortie": empreinte_sortie}
        self._ajouter("episode", contenu)
        self.en_cours = None
        self.prochain_rang += 1
        if rang < self.palier.n_episodes:
            self.rythmes.append(rythme)
            self._lire_palier()
        return contenu

    def _lire_palier(self) -> None:
        if self.palier_lu:
            return
        v = self.palier.evaluer(self.rythmes)
        if not v["lu"]:
            return
        self.palier_lu = True
        verdict = {**v, "seuil_s": self.palier.seuil_s, "lecture": self.palier.lecture,
                   "rythmes": list(self.rythmes)}
        self._ajouter("palier_lu", verdict)
        if v["sonne"]:
            rang = self.prochain_rang - 1
            motif = (f"rythme {v['valeur']:.3f} s > {self.palier.seuil_s} s ({self.palier.lecture}, "
                     f"{self.palier.regle}) : arrêt, nœud de devis (P-14) ; aucun relèvement silencieux")
            self.arrete = {"rang": rang, "motif": motif, "verdict": verdict}
            self._ajouter("arret_palier", self.arrete)
            raise ArretPalier(motif)

    def clore(self, motif: str) -> str:
        """Écrit `cloture` et scelle le journal (R6). Renvoie l'empreinte du fichier."""
        if self.en_cours is not None:
            raise GardeArret(f"rang {self.en_cours} en cours : clôture refusée")
        self._ajouter("cloture", {"motif": _exiger_texte(motif, "motif de clôture"),
                                  "n_episodes": self.prochain_rang, "arrete": self.arrete is not None})
        self.clos = True
        return sceller(self.chemin)


# --------------------------------------------------------------------------------------------------------------------
# Lecture et vérification
# --------------------------------------------------------------------------------------------------------------------

def lire_journal(chemin: str | Path, *, ancre_attendue: str | None = None) -> dict:
    """Relit et vérifie le journal entier. Lève `JournalCorrompu` sur : ligne tronquée ou illisible, ligne non
    canonique, empreinte propre fausse (ligne réécrite), chaîne cassée, numéro sauté, horodatage en recul ou hors UTC,
    type inconnu, ordre engagé qui ne se retire pas, rang hors ordre ou sauté (trou d'ordre), élément différent de
    l'ordre, palier incohérent avec les rythmes consignés, ajout après arrêt ou clôture, sceau absent ou faux à la
    clôture, ancre différente."""
    p = Path(chemin)
    if not p.is_file():
        raise JournalCorrompu(f"{p} : journal absent sur disque")
    brut = p.read_bytes()
    if not brut:
        raise JournalCorrompu(f"{p} : journal vide (aucune ouverture)")
    if not brut.endswith(b"\n"):
        raise JournalCorrompu(f"{p} : dernière ligne tronquée (pas de fin de ligne)")
    textes = brut.decode("utf-8").split("\n")[:-1]
    lignes, precedent, avant = [], ZERO, None
    for i, t in enumerate(textes):
        ou = f"{p} ligne {i}"
        try:
            d = json.loads(t)
        except json.JSONDecodeError:
            raise JournalCorrompu(f"{ou} : JSON illisible (tronquée ?)") from None
        if not isinstance(d, dict) or set(d) != {"n", "type", "horodatage", "precedent", "contenu", "empreinte"}:
            raise JournalCorrompu(f"{ou} : champs inattendus")
        if _canonique(d) != t:
            raise JournalCorrompu(f"{ou} : ligne non canonique (réécrite)")
        emp = d.pop("empreinte")
        if _sha(_canonique(d)) != emp:
            raise JournalCorrompu(f"{ou} : empreinte propre fausse (ligne réécrite)")
        d["empreinte"] = emp
        if d["n"] != i:
            raise JournalCorrompu(f"{ou} : numéro {d['n']} au lieu de {i} (ligne retirée ou insérée)")
        if d["precedent"] != precedent:
            raise JournalCorrompu(f"{ou} : chaîne cassée (précédent {d['precedent'][:12]}… ≠ {precedent[:12]}…)")
        if d["type"] not in TYPES:
            raise JournalCorrompu(f"{ou} : type {d['type']!r} inconnu")
        h = _lire_horodatage(d["horodatage"], ou)
        if avant is not None and h < avant:
            raise JournalCorrompu(f"{ou} : horodatage en recul")
        avant, precedent = h, emp
        lignes.append(d)
    if lignes[0]["type"] != "ouverture":
        raise JournalCorrompu(f"{p} : la ligne 0 n'est pas l'ouverture")
    ouv = lignes[0]["contenu"]
    try:
        sha_ordre = exiger_ordre_retire(ouv["ordre"])
        palier = PalierRythme.depuis_dict(ouv["palier"])
    except (GardeArret, KeyError, TypeError) as e:
        raise JournalCorrompu(f"{p} : ouverture invalide ({e})") from None
    if sha_ordre != ouv.get("ordre_sha256"):
        raise JournalCorrompu(f"{p} : empreinte de l'ordre engagé incohérente")
    elements = ouv["ordre"]["elements"]

    prochain, en_cours, episodes, rythmes = 0, None, [], []
    palier_lu, arret, clos = None, None, False
    for d in lignes[1:]:
        ou, c, ty = f"{p} ligne {d['n']}", d["contenu"], d["type"]
        if clos:
            raise JournalCorrompu(f"{ou} : ajout après la clôture")
        if arret is not None and ty != "cloture":
            raise JournalCorrompu(f"{ou} : {ty} après l'arrêt du palier")
        if ty == "ouverture":
            raise JournalCorrompu(f"{ou} : seconde ouverture")
        if ty in ("debut", "episode"):
            r = c.get("rang")
            if isinstance(r, bool) or r != prochain:
                raise JournalCorrompu(f"{ou} : rang {r!r} au lieu de {prochain} (trou ou désordre dans l'ordre)")
            el = elements[r] if isinstance(r, int) and 0 <= r < len(elements) else None
            if el is None or any(c.get(k) != el[k] for k in ("lot", "tache", "execution")):
                raise JournalCorrompu(f"{ou} : épisode du rang {r} différent de l'ordre engagé")
            if c.get("instance") != ouv["instance"]:
                raise JournalCorrompu(f"{ou} : instance {c.get('instance')!r} ≠ {ouv['instance']!r}")
        if ty == "debut":
            if en_cours is not None:
                raise JournalCorrompu(f"{ou} : début alors que le rang {en_cours} est en cours")
            if c.get("graine") != elements[c["rang"]]["graine"]:
                raise JournalCorrompu(f"{ou} : graine différente de l'ordre engagé")
            en_cours = c["rang"]
        elif ty == "interruption":
            if en_cours is None or c.get("rang") != en_cours:
                raise JournalCorrompu(f"{ou} : interruption sans épisode en cours")
            en_cours = None
        elif ty == "episode":
            if en_cours != c["rang"]:
                raise JournalCorrompu(f"{ou} : épisode sans début")
            try:
                s = palier.exiger_secondes(c.get("secondes"))
                r_calc = palier.rythme(s)
            except GardeArret as e:
                raise JournalCorrompu(f"{ou} : secondes invalides ({e})") from None
            if c.get("rythme_palier") != r_calc:
                raise JournalCorrompu(f"{ou} : rythme consigné ≠ rythme recalculé")
            episodes.append(c)
            if c["rang"] < palier.n_episodes:
                rythmes.append(r_calc)
            en_cours, prochain = None, prochain + 1
        elif ty == "palier_lu":
            if palier_lu is not None:
                raise JournalCorrompu(f"{ou} : palier lu deux fois")
            v = palier.evaluer(rythmes)
            attendu = {**v, "seuil_s": palier.seuil_s, "lecture": palier.lecture, "rythmes": rythmes}
            if not v["lu"] or _canonique(attendu) != _canonique(c):
                raise JournalCorrompu(f"{ou} : verdict du palier incohérent avec les rythmes consignés")
            palier_lu = c
        elif ty == "arret_palier":
            if palier_lu is None or not palier_lu["sonne"] or c.get("verdict") != palier_lu:
                raise JournalCorrompu(f"{ou} : arrêt du palier sans verdict qui sonne")
            arret = c
        elif ty == "cloture":
            if en_cours is not None:
                raise JournalCorrompu(f"{ou} : clôture avec le rang {en_cours} en cours")
            clos = True
    # Le palier doit avoir été lu dès qu'il est lisible : un verdict manquant serait un repli silencieux.
    if palier_lu is None and palier.evaluer(rythmes)["lu"]:
        raise JournalCorrompu(f"{p} : palier lisible mais aucun verdict consigné")
    if palier_lu is not None and palier_lu["sonne"] and arret is None:
        raise JournalCorrompu(f"{p} : le palier a sonné mais l'arrêt n'est pas écrit")
    if clos:
        try:
            verifier(p)
        except GardeArret as e:
            raise JournalCorrompu(f"{p} : journal clos mais sceau invalide ({e})") from None
    elif compagnon(p).exists():
        raise JournalCorrompu(f"{p} : sceau présent sans clôture")
    if ancre_attendue is not None and precedent != ancre_attendue:
        raise JournalCorrompu(f"{p} : ancre {precedent[:12]}… ≠ attendue {ancre_attendue[:12]}… "
                              "(dernière ligne réécrite ou retirée)")
    return {"lignes": lignes, "n_lignes": len(lignes), "ancre": precedent, "ouverture": ouv, "episodes": episodes,
            "prochain_rang": prochain, "en_cours": en_cours, "palier_lu": palier_lu, "arret": arret, "clos": clos}


__all__ = ["VERSION", "SEUIL_P23_SECONDES", "TAILLE_PALIER_P23", "LECTURE_P28", "LECTURES", "REGLES",
           "JournalCorrompu", "HorsOrdre", "ArretPalier", "PalierRythme", "palier_p23_p28", "bloc", "tirer_ordre",
           "graine_episode", "empreinte_ordre", "exiger_ordre_retire", "ecrire_ordre", "charger_ordre",
           "JournalFabrique", "lire_journal"]
