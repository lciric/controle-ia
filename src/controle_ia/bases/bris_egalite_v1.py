"""Bris d'égalité aléatoire scellé (P-15, E-1) — v1. Module autonome, sans lien avec le pôle de conv-audit.

Pourquoi. Des scores discrets (juge lu par un jeton, grille de notes) font des ex æquo. Avec la convention conforme
stricte « alerte si score > s_(j) », le seuil tombe sur un niveau de la grille et le taux d'alerte saute d'un niveau
entier ; la simulation du contrôle 12 joint (`docs/notes/couche-2-preparation-v1/simulation-controle-12-joint-v1/`,
rapport `7600f2d0…`) mesure alors un échec joint de 0,35 à 0,54 en unilatéral, quelle que soit la taille du calibrage.
Un ordre tiré dans chaque niveau supprime le saut (0,016 en unilatéral, 0,031 en bilatéral à 9 600 et au seuil 40).
Ce module tire cet ordre, de façon déterministe une fois la clé révélée, et engagée avant tout épisode.

Protocole (dans cet ordre, chaque étape gardée) :
1. `tirer_cle()` : clé secrète de 64 bits, tirée de l'entropie du système (`secrets`). Ce n'est pas une graine de
   générateur (R9 vaut pour les graines) : c'est un secret, dont la reproductibilité vient de la révélation.
2. `engager(cle)` puis `ecrire_engagement(…)` : on publie l'**empreinte** de la clé, SHA-256(domaine ‖ clé), dans un
   fichier JSON scellé (empreinte compagnon `.sha256`, R6) et versé avant tout épisode ; la clé reste secrète.
3. `BrisEgalite.depuis_fichier(chemin)` : charge l'engagement scellé (refus s'il n'est pas intact) ; l'objet n'a pas
   de clé. Tout appel de dérivation avant la révélation est refusé.
4. `reveler(cle)` : refus si la clé ne correspond pas à l'empreinte engagée (comparaison à temps constant).
5. Dérivation : HMAC-SHA256(clé, domaine ‖ cellule ‖ épisode ‖ moniteur), chaque champ préfixé de sa longueur
   (aucune ambiguïté de concaténation). Chaque score (cellule, épisode, moniteur) reçoit son propre condensat de
   256 bits ; l'ordre de bris d'égalité est l'ordre lexicographique (score, condensat). Le rang est donc
   déterministe, indépendant d'une cellule à l'autre, et uniforme dans un niveau tant que la clé est inconnue.

Seuil et alerte (`seuil_conforme`, `alertes`) : même convention que le pôle — j = ⌊τ(n + 1)⌋, alerte si la clé de tri
(score, condensat) est strictement plus grande que la j-ième plus grande clé honnête du calibrage ; si j < 1, seuil
infini (« calibrage insuffisant »), jamais de repli. Avec des clés toutes distinctes, P(alerte d'un honnête neuf)
= j/(n + 1) pour des scores échangeables, ex æquo compris. Le condensat n'est calculé que pour les scores égaux au
score du seuil : c'est exactement l'ordre lexicographique complet (les autres comparaisons sont tranchées par le
score seul).

Refus (`GardeArret`, R5, aucun repli silencieux) : clé de mauvaise longueur ou de mauvais type ; clé qui ne correspond
pas à l'empreinte ; dérivation avant révélation ; seconde révélation d'une autre clé ; engagement incomplet, altéré ou
non scellé ; engagement postérieur au premier épisode (`verifier_anteriorite`) ; score non fini (la porte des scores
finis, P-16, vient avant) ; identifiant vide ; collision de condensats dans un niveau (épisode en double).

La mesure des ex æquo (`part_ex_aequo`) documente, ne déclenche rien (P-15).
"""
from __future__ import annotations

import hashlib
import hmac
import json
import math
import secrets
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from .. import scellement

VERSION = "bris-egalite-v1"
SCHEMA_ENGAGEMENT = "bris-egalite-engagement-v1"
ALGORITHME = "HMAC-SHA256"
TAILLE_CLE_OCTETS = 8  # 64 bits
DOMAINE_ENGAGEMENT = b"controle-ia|bris-egalite|v1|engagement\x00"
DOMAINE_DERIVATION = b"controle-ia|bris-egalite|v1|derivation\x00"
CHAMPS_ENGAGEMENT = ("schema", "algorithme", "taille_cle_bits", "empreinte_cle", "engage_le")


# -- clé et engagement ----------------------------------------------------------------------------------------------
def _exiger_cle(cle) -> bytes:
    if not isinstance(cle, (bytes, bytearray)):
        raise GardeArret(f"clé de type {type(cle).__name__} : octets attendus ({TAILLE_CLE_OCTETS})")
    if len(cle) != TAILLE_CLE_OCTETS:
        raise GardeArret(f"clé de {len(cle)} octets : {TAILLE_CLE_OCTETS} attendus (64 bits)")
    return bytes(cle)


def tirer_cle() -> bytes:
    """Clé secrète de 64 bits, tirée de l'entropie du système d'exploitation."""
    return secrets.token_bytes(TAILLE_CLE_OCTETS)


def cle_depuis_hex(texte: str) -> bytes:
    """Clé révélée sous forme de 16 chiffres hexadécimaux."""
    if not isinstance(texte, str) or len(texte) != 2 * TAILLE_CLE_OCTETS:
        raise GardeArret(f"clé hexadécimale de {2 * TAILLE_CLE_OCTETS} caractères attendue")
    try:
        return _exiger_cle(bytes.fromhex(texte))
    except ValueError as e:
        raise GardeArret(f"clé hexadécimale illisible : {e}") from None


def empreinte_cle(cle) -> str:
    """SHA-256(domaine d'engagement ‖ clé), en hexadécimal."""
    return hashlib.sha256(DOMAINE_ENGAGEMENT + _exiger_cle(cle)).hexdigest()


def _horodatage(texte: str) -> datetime:
    try:
        t = datetime.fromisoformat(texte.replace("Z", "+00:00"))
    except (AttributeError, ValueError):
        raise GardeArret(f"horodatage illisible : {texte!r}") from None
    if t.tzinfo is None:
        raise GardeArret(f"horodatage sans fuseau : {texte!r} (UTC exigé)")
    return t.astimezone(timezone.utc)


def engager(cle, engage_le: str | None = None) -> dict:
    """Engagement publiable : contient l'empreinte de la clé, jamais la clé."""
    if engage_le is None:
        engage_le = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    _horodatage(engage_le)
    return {"schema": SCHEMA_ENGAGEMENT, "algorithme": ALGORITHME, "taille_cle_bits": 8 * TAILLE_CLE_OCTETS,
            "empreinte_cle": empreinte_cle(cle), "engage_le": engage_le}


def valider_engagement(engagement) -> dict:
    if not isinstance(engagement, dict):
        raise GardeArret("engagement : objet JSON attendu")
    manquants = [c for c in CHAMPS_ENGAGEMENT if c not in engagement]
    if manquants:
        raise GardeArret(f"engagement incomplet : {manquants}")
    if engagement["schema"] != SCHEMA_ENGAGEMENT or engagement["algorithme"] != ALGORITHME:
        raise GardeArret(f"engagement : schéma ou algorithme inattendu ({engagement['schema']!r}, "
                         f"{engagement['algorithme']!r})")
    if engagement["taille_cle_bits"] != 8 * TAILLE_CLE_OCTETS:
        raise GardeArret(f"engagement : clé de {engagement['taille_cle_bits']} bits, 64 attendus")
    e = engagement["empreinte_cle"]
    if not isinstance(e, str) or len(e) != 64 or any(c not in "0123456789abcdef" for c in e):
        raise GardeArret("engagement : empreinte de clé illisible (64 chiffres hexadécimaux minuscules)")
    _horodatage(engagement["engage_le"])
    return engagement


def ecrire_engagement(engagement: dict, chemin) -> str:
    """Écrit l'engagement en JSON et le scelle (R6). Refuse d'écraser un fichier existant (R12). Rend l'empreinte."""
    valider_engagement(engagement)
    p = Path(chemin)
    if p.exists():
        raise GardeArret(f"{p} existe déjà : un engagement ne se réécrit jamais (R12)")
    p.write_text(json.dumps(engagement, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    return scellement.sceller(p)


def charger_engagement(chemin) -> dict:
    """Lit un engagement **scellé** ; refus s'il n'a pas d'empreinte compagnon ou s'il a été altéré."""
    scellement.verifier(chemin)
    try:
        engagement = json.loads(Path(chemin).read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise GardeArret(f"{chemin} : JSON illisible ({e})") from None
    return valider_engagement(engagement)


# -- encodage du sel ------------------------------------------------------------------------------------------------
def _champ(nom: str, valeur) -> bytes:
    if not isinstance(valeur, str) or not valeur:
        raise GardeArret(f"identifiant {nom} : chaîne non vide attendue, reçu {valeur!r}")
    b = valeur.encode("utf-8")
    return len(b).to_bytes(4, "big") + b


def message_derivation(cellule: str, episode: str, moniteur: str) -> bytes:
    """Message salé : domaine ‖ (longueur, cellule) ‖ (longueur, épisode) ‖ (longueur, moniteur)."""
    return DOMAINE_DERIVATION + _champ("cellule", cellule) + _champ("épisode", episode) + _champ("moniteur", moniteur)


def _exiger_finis(x: np.ndarray, quoi: str) -> None:
    if not np.all(np.isfinite(x)):
        raise GardeArret(f"{quoi} : score non fini ({int((~np.isfinite(x)).sum())}) ; la porte des scores finis "
                         "(P-16) passe avant le bris d'égalité")


def part_ex_aequo(scores) -> float:
    """Part des scores qui partagent leur valeur avec au moins un autre (documente, ne déclenche rien)."""
    x = np.asarray(scores, dtype=float).ravel()
    _exiger_finis(x, "part d'ex æquo")
    if x.size == 0:
        return 0.0
    _, inverse, effectifs = np.unique(x, return_inverse=True, return_counts=True)
    return float((effectifs[inverse] > 1).mean())


@dataclass(frozen=True)
class SeuilDepartage:
    """j-ième plus grande clé (score, condensat) des honnêtes du calibrage. `condensat` est toujours calculé quand
    j ≥ 1 ; il vaut None (et `score` l'infini) seulement si le calibrage est insuffisant."""
    score: float
    condensat: bytes | None
    j: int
    n: int
    ex_aequo_au_niveau: int  # nombre de scores honnêtes égaux au score du seuil (lui compris)
    calibrage_insuffisant: bool


# -- objet principal ------------------------------------------------------------------------------------------------
class BrisEgalite:
    """Bris d'égalité engagé. Se construit sur un engagement, sans clé ; dérive seulement après `reveler`."""

    def __init__(self, engagement: dict):
        self.engagement = dict(valider_engagement(engagement))
        self._cle: bytes | None = None

    @classmethod
    def depuis_fichier(cls, chemin) -> "BrisEgalite":
        return cls(charger_engagement(chemin))

    @property
    def revele(self) -> bool:
        return self._cle is not None

    def reveler(self, cle) -> None:
        cle = _exiger_cle(cle)
        if not hmac.compare_digest(empreinte_cle(cle), self.engagement["empreinte_cle"]):
            raise GardeArret("clé refusée : son empreinte ne correspond pas à l'empreinte engagée")
        if self._cle is not None and not hmac.compare_digest(self._cle, cle):  # impossible sans collision SHA-256
            raise GardeArret("une autre clé a déjà été révélée")
        self._cle = cle

    def verifier_anteriorite(self, premier_episode_le: str) -> None:
        """Refus si l'engagement n'est pas strictement antérieur au premier épisode (P-15 : avant tout épisode)."""
        if not _horodatage(self.engagement["engage_le"]) < _horodatage(premier_episode_le):
            raise GardeArret(f"engagement du {self.engagement['engage_le']} non antérieur au premier épisode "
                             f"({premier_episode_le})")

    # -- dérivation --
    def condensat(self, cellule: str, episode: str, moniteur: str) -> bytes:
        if self._cle is None:
            raise GardeArret("bris d'égalité appelé avant la révélation de la clé engagée")
        return hmac.digest(self._cle, message_derivation(cellule, episode, moniteur), "sha256")

    def valeur(self, cellule: str, episode: str, moniteur: str) -> int:
        """Entier de 64 bits (les 8 premiers octets du condensat, gros-boutiste)."""
        return int.from_bytes(self.condensat(cellule, episode, moniteur)[:8], "big")

    def uniforme(self, cellule: str, episode: str, moniteur: str) -> float:
        """Réel dans [0 ; 1) (53 bits de poids fort de `valeur`) ; même ordre que le condensat hors égalité de 53 bits."""
        return (self.valeur(cellule, episode, moniteur) >> 11) * 2.0 ** -53

    def cle_de_tri(self, score: float, cellule: str, episode: str, moniteur: str) -> tuple[float, bytes]:
        score = float(score)
        _exiger_finis(np.array([score]), f"épisode {episode!r}")
        return (score, self.condensat(cellule, episode, moniteur))

    def ordre(self, scores, episodes, cellule: str, moniteur: str) -> list[int]:
        """Indices du plus suspect au moins suspect, selon (score, condensat) décroissant. Référence complète."""
        x = np.asarray(scores, dtype=float)
        if len(episodes) != x.size:
            raise GardeArret(f"{x.size} scores pour {len(episodes)} épisodes")
        _exiger_finis(x, f"cellule {cellule!r}")
        cles = [(float(x[i]), self.condensat(cellule, episodes[i], moniteur)) for i in range(x.size)]
        if len({c[1] for c in cles}) != len(cles):
            raise GardeArret(f"cellule {cellule!r} : condensats en double (épisode en double ?)")
        return sorted(range(x.size), key=lambda i: cles[i], reverse=True)

    def rangs(self, scores, episodes, cellule: str, moniteur: str) -> dict[str, int]:
        """Rang de bris d'égalité de chaque épisode (1 = le plus suspect)."""
        return {episodes[i]: r + 1 for r, i in enumerate(self.ordre(scores, episodes, cellule, moniteur))}

    # -- seuil et alertes --
    def seuil_conforme(self, scores, episodes, cellule: str, moniteur: str, tau: float) -> SeuilDepartage:
        """Seuil conforme strict départagé sur les honnêtes du calibrage. `episodes` : toute suite indexable alignée
        sur `scores` (seuls les identifiants des ex æquo du niveau du seuil sont lus)."""
        if not 0.0 < tau < 1.0:
            raise GardeArret(f"τ = {tau} hors de ]0 ; 1[")
        x = np.asarray(scores, dtype=float).ravel()
        if len(episodes) != x.size:
            raise GardeArret(f"{x.size} scores pour {len(episodes)} épisodes")
        _exiger_finis(x, f"calibrage de {cellule!r}")
        n = int(x.size)
        j = math.floor(tau * (n + 1) + 1e-12)
        if n == 0 or j < 1:
            return SeuilDepartage(math.inf, None, 0, n, 0, True)
        s = float(-np.partition(-x, j - 1)[j - 1])
        au_dessus = int((x > s).sum())
        niveau = np.flatnonzero(x == s)
        condensats = sorted((self.condensat(cellule, episodes[int(i)], moniteur) for i in niveau), reverse=True)
        if len(set(condensats)) != len(condensats):
            raise GardeArret(f"cellule {cellule!r} : condensats en double au niveau du seuil (épisode en double ?)")
        return SeuilDepartage(s, condensats[j - au_dessus - 1], j, n, int(niveau.size), False)

    def alertes(self, scores, episodes, seuil: SeuilDepartage, cellule: str, moniteur: str) -> np.ndarray:
        """Alerte si (score, condensat) > (seuil.score, seuil.condensat). Condensat lu seulement à égalité de score."""
        x = np.asarray(scores, dtype=float)
        if len(episodes) != x.size:
            raise GardeArret(f"{x.size} scores pour {len(episodes)} épisodes")
        _exiger_finis(x, f"lecture de {cellule!r}")
        if seuil.calibrage_insuffisant:
            return np.zeros(x.shape, dtype=bool)
        plat = x.ravel()
        a = plat > seuil.score
        for i in np.flatnonzero(plat == seuil.score):
            a[i] = self.condensat(cellule, episodes[int(i)], moniteur) > seuil.condensat
        return a.reshape(x.shape)
