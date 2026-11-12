#!/usr/bin/env python3
"""Épreuve de l'étiqueteur, phase 1 : lecture des items par les deux lecteurs modèles (v3).

Rédacteur : Claude Opus 5.5 (claude-opus-5-5), rédacteur neuf, 7 novembre 2026.
Pièce du brouillon 5 du préenregistrement (même dossier). Les versions 1 et 2 restent intactes.

Changements depuis la v2 (contre-lecture du delta du brouillon 4) :
- D1 : `--variable-cle-gemini` doit avoir la forme d'un nom de variable (`[A-Z_][A-Z0-9_]*`) ; sinon arrêt avant tout
  appel et toute écriture, sans recopier la valeur reçue ; **tout** message (erreurs d'arguments comprises, arrêts de
  `__main__`) passe par le masquage ; `--go`, `--commit`, `--relais-empreinte` et `--relais-kimi` sont contrôlés de forme
  avant d'être écrits ;
- plafond accordé par le directeur : 300 dollars (GO-2026-11-07-07) ; `--plafond-dollars` ne peut pas le dépasser ;
- R1 : la lecture principale refuse un plafond différent de celui de l'essai de format, et une dépense déjà engagée
  inférieure à celle de son manifeste ; R2 : plafond par défaut 300, jamais au-delà ; R3 : une exception imprévue hors
  d'une lecture est saisie, écrite, et rend un code non nul (7) ; R4 : une clé invalide rendue en 400 par Argon
  (`API_KEY_INVALID`) arrête tous les appels, comme 401 et 403 ; Kimi : une réponse 402 du relais (plafond du relais)
  arrête ce lecteur ;
- relais de Kimi : `--relais-max-appels` (mode réel) doit couvrir cinq tentatives par item lu ; consigné au manifeste ;
- `--fils-par-lecteur` gelé à 1 (deux fils communs aux deux lecteurs).

Changements depuis la v1 (contre-lecture 1 du brouillon 3) :
- B2 : réglages gelés par lecteur, non modifiables en ligne de commande. Argon : température 0 envoyée,
  `maxOutputTokens` 8 000, `thinkingBudget` 8 192. Kimi : **aucune température envoyée** (Moonshot la fixe à 1,0 et
  demande de l'omettre), `reasoning_effort` « high », `max_tokens` 32 000 (raisonnement compris ; Moonshot conseille au
  moins 16 000 pour un modèle qui raisonne). Température envoyée et température servie écrites au manifeste et au journal ;
- B3 : la garde réserve, pour Argon, l'entrée au pire cas plus (8 000 + 8 192) jetons au prix de sortie ; une réponse
  dont la pensée dépasse 8 192 jetons, ou dont la sortie dépasse la sortie réservée, arrête ce lecteur ;
- B4 : `--lectures format` lance l'essai de format seul et rend un contrôle écrit (feu vert ou feu rouge, avec motifs) ;
  `--lectures principale+relecture` refuse de partir sans le manifeste d'un essai de format au feu vert, sur les mêmes
  entrées et les mêmes réglages ;
- B5 : toutes les consignes des lectures demandées sont rendues et contrôlées avant le premier appel ; une variable de
  clé absente (mode réel) arrête avant tout appel ; une clé refusée par le fournisseur (codes 401 et 403) arrête **tous**
  les appels des deux lecteurs ; dans tous les cas, journal, réponses partielles et manifeste sont écrits ;
- B6 : tout texte écrit (journal, réponses, manifeste, sortie à l'écran) passe par `nettoyer`, qui masque la clé entière
  puis tout fragment d'au moins 6 caractères de la clé, **avant** toute troncature ;
- écriture au fil des tentatives (journal et réponses « en cours ») ; option `--depense-engagee` (le plafond vaut pour
  la phase entière) ; commit du code et empreinte du relais de Kimi au manifeste.

Point ouvert, à vérifier à l'essai de format : que les deux fournisseurs acceptent ces réglages (sinon feu rouge écrit).

Bibliothèque standard et numpy seulement ; aucun module du programme importé (seulement les scripts de ce dossier).

Usage :
    python -I -B lire_items_phase1_v2.py --simule --lectures format --items I --formation F --relectures R \
        --question TEXTE.md --entropie N --sortie DOSSIER_FORMAT [--plafond-dollars P]
    python -I -B lire_items_phase1_v2.py --simule --lectures principale+relecture --feu-vert-format \
        DOSSIER_FORMAT/manifeste-lecture-phase1-v2.json ... --sortie DOSSIER_PRINCIPAL [--depense-engagee D]
    (mode réel : --reel --go GO-AAAA-MM-JJ-NN --commit COMMIT [--variable-cle-gemini NOM] [--relais-empreinte E])
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import platform
import re
import ssl
import sys
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import epreuve_phases_v1 as ph  # noqa: E402  (scripts du même dossier, pas des modules du programme)
import generer_items_v2 as gen  # noqa: E402  (inchangé)

VERSION = "v3"
PLAFOND_ACCORDE = 300.0  # GO-2026-11-07-07
NOM_VARIABLE = re.compile(r"[A-Z_][A-Z0-9_]*")
TENTATIVES_MAX_PAR_ITEM = 5  # trois erreurs de transport, une demande au format faux, puis la dernière
CARACTERES_PAR_JETON_PRUDENT = 3
ATTENTES_TRANSPORT = (0, 10, 30, 90)
DEMANDES_FORMAT = 2
FRAGMENT_MIN = 6  # tout fragment de clé d'au moins 6 caractères est masqué
LECTEURS = {
    "A": {"modele": "gemini-4-argon", "fournisseur": "gemini", "prix": (10.0, 50.0),  # barème prudent, à vérifier
          "temperature_envoyee": 0, "temperature_servie": 0,  # demandée ; la réponse d'Argon ne la rend pas
          "plafond_sortie": 8000, "budget_pensee": 8192, "effort_raisonnement": None},
    "B": {"modele": "kimi-k3.1-pro", "fournisseur": "kimi", "prix": (2.0, 10.0),  # vérifié sur la page de prix versée
          "temperature_envoyee": None, "temperature_servie": 1.0,  # fixée par Moonshot, à omettre de la requête
          "plafond_sortie": 32000, "budget_pensee": 0, "effort_raisonnement": "high"},
}
FINS_TRONQUEES = {"MAX_TOKENS", "length"}
LIGNES_LECTURE = {"format": ("format",), "principale+relecture": ("principale", "relecture")}
ORDRE_LECTURES = ("format", "principale", "relecture")
LIGNE = re.compile(r'^STEP\s+(\d+)\s*:\s*(NO|YES\s*\|\s*ABSENT|YES\s*\|\s*(WEAKENED|UNINFORMATIVE)\s*\|\s*"(.*)")\s*$')
CODES = {"ok": 0, "rendu": 2, "depense": 3, "lecteur": 4, "general": 5, "feu_rouge": 6, "exception": 7}
SECRETS_DU_PROCESSUS = None  # rempli par `principal` ; sert au masquage des messages de `__main__`


class ArretLecture(RuntimeError):
    """Arrêt explicite ; le manifeste dit pourquoi."""


class ArretDepense(ArretLecture):
    pass


class ArretGeneral(ArretLecture):
    """Clé absente ou refusée : plus aucun appel, pour aucun lecteur."""


class FormatInvalide(ValueError):
    pass


# ---------------------------------------------------------------------------------------------------------------
# Masquage (B6) : toujours avant toute troncature
# ---------------------------------------------------------------------------------------------------------------
class Secrets:
    def __init__(self, valeurs=()):
        self.valeurs = [v for v in valeurs if v]

    def ajouter(self, valeur):
        if valeur and valeur not in self.valeurs:
            self.valeurs.append(valeur)

    def nettoyer(self, texte):
        if texte is None or not self.valeurs:
            return texte
        if not isinstance(texte, str):
            texte = str(texte)
        for v in self.valeurs:
            texte = texte.replace(v, "[clé]")
            if len(v) < FRAGMENT_MIN:
                continue
            grammes = {v[i:i + FRAGMENT_MIN] for i in range(len(v) - FRAGMENT_MIN + 1)}
            if not any(g in texte for g in grammes):
                continue
            marque = bytearray(len(texte))  # tout caractère couvert par un fragment de 6 caractères de la clé
            for i in range(len(texte) - FRAGMENT_MIN + 1):
                if texte[i:i + FRAGMENT_MIN] in grammes:
                    marque[i:i + FRAGMENT_MIN] = b"\x01" * FRAGMENT_MIN
            morceaux, i = [], 0
            while i < len(texte):
                j = i
                while j < len(texte) and marque[j] == marque[i]:
                    j += 1
                morceaux.append("[clé]" if marque[i] else texte[i:j])
                i = j
            texte = "".join(morceaux)
        return texte

    def nettoyer_objet(self, obj):
        if isinstance(obj, str):
            return self.nettoyer(obj)
        if isinstance(obj, dict):
            return {k: self.nettoyer_objet(x) for k, x in obj.items()}
        if isinstance(obj, (list, tuple)):
            return [self.nettoyer_objet(x) for x in obj]
        return obj


def tronquer_masque(texte: str, secrets: Secrets, n: int = 300) -> str:
    return secrets.nettoyer(texte)[:n]


# ---------------------------------------------------------------------------------------------------------------
# Format des réponses (inchangé depuis la v1)
# ---------------------------------------------------------------------------------------------------------------
def analyser_reponse(texte: str) -> list:
    lignes = [x.strip() for x in (texte or "").splitlines()]
    lignes = [x for x in lignes if x and not x.startswith("```")]
    if len(lignes) != gen.N_PAS:
        raise FormatInvalide(f"{len(lignes)} lignes au lieu de {gen.N_PAS}")
    sortie = []
    for attendu, ligne in enumerate(lignes):
        m = LIGNE.match(ligne)
        if not m:
            raise FormatInvalide(f"ligne {attendu + 1} hors format")
        if int(m.group(1)) != attendu:
            raise FormatInvalide(f"pas {m.group(1)} au lieu de {attendu}")
        if m.group(2) == "NO":
            sortie.append({"pas": attendu, "oui": False, "categorie": None, "citation": None})
        elif m.group(3) is None:
            sortie.append({"pas": attendu, "oui": True, "categorie": "ABSENT", "citation": None})
        else:
            sortie.append({"pas": attendu, "oui": True, "categorie": m.group(3), "citation": m.group(4)})
    return sortie


# ---------------------------------------------------------------------------------------------------------------
# Fournisseurs
# ---------------------------------------------------------------------------------------------------------------
@dataclass
class Reponse:
    texte: str = ""
    modele_servi: str | None = None
    jetons_entree: int | None = None
    jetons_sortie: int | None = None  # sortie visible plus pensée
    jetons_pensee: int = 0
    echec: str | None = None
    reprendre: bool = False
    cle_refusee: bool = False
    fin: str | None = None
    detail: dict = field(default_factory=dict)


def _contexte_tls():
    ca = os.environ.get("SSL_CERT_FILE")
    return ssl.create_default_context(cafile=ca) if ca else ssl.create_default_context()


def corps_gemini(consigne: str) -> dict:
    m = LECTEURS["A"]
    return {"contents": [{"role": "user", "parts": [{"text": consigne}]}],
            "generationConfig": {"temperature": m["temperature_envoyee"], "maxOutputTokens": m["plafond_sortie"],
                                 "thinkingConfig": {"thinkingBudget": m["budget_pensee"]}}}


def corps_kimi(consigne: str) -> dict:
    m = LECTEURS["B"]
    return {"model": m["modele"], "messages": [{"role": "user", "content": consigne}],
            "max_tokens": m["plafond_sortie"], "reasoning_effort": m["effort_raisonnement"]}


def appeler_gemini(consigne: str, variable_cle: str, secrets: Secrets, ouvrir=None) -> Reponse:
    cle = os.environ.get(variable_cle)
    if not cle:
        return Reponse(echec=f"variable {variable_cle} absente", cle_refusee=True)
    secrets.ajouter(cle)
    corps = json.dumps(corps_gemini(consigne), ensure_ascii=False).encode("utf-8")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{LECTEURS['A']['modele']}:generateContent"
    requete = urllib.request.Request(url, data=corps, method="POST",
                                     headers={"Content-Type": "application/json", "x-goog-api-key": cle})
    ouvrir = ouvrir or (lambda r: urllib.request.urlopen(r, context=_contexte_tls(), timeout=1200))
    try:
        with ouvrir(requete) as r:
            rep = json.load(r)
    except urllib.error.HTTPError as e:
        brut = e.read().decode("utf-8", "replace")
        detail = tronquer_masque(brut, secrets)  # masque AVANT de tronquer
        invalide = e.code == 400 and "API_KEY_INVALID" in brut  # R4 : clé invalide rendue en 400 par Argon
        return Reponse(echec=f"HTTP {e.code} : {detail}", reprendre=e.code in (429, 500, 502, 503, 504),
                       cle_refusee=e.code in (401, 403) or invalide)
    except (OSError, ValueError) as e:
        return Reponse(echec=f"connexion : {type(e).__name__} : {tronquer_masque(str(e), secrets)}", reprendre=True)
    u = rep.get("usageMetadata") or {}
    pensee = u.get("thoughtsTokenCount") or 0
    candidats = rep.get("candidates") or []
    base = dict(modele_servi=rep.get("modelVersion"), jetons_entree=u.get("promptTokenCount"),
                jetons_sortie=(u.get("candidatesTokenCount") or 0) + pensee, jetons_pensee=pensee)
    if not candidats:
        bloque = (rep.get("promptFeedback") or {}).get("blockReason")
        return Reponse(echec=f"aucun candidat ({bloque or 'sans raison'})", fin="AUCUN_CANDIDAT", **base)
    c = candidats[0]
    parts = (c.get("content") or {}).get("parts") or []
    return Reponse(texte="".join(p.get("text", "") for p in parts if not p.get("thought")), fin=c.get("finishReason"),
                   **base)


def appeler_kimi(consigne: str, url_relais: str, secrets: Secrets, ouvrir=None) -> Reponse:
    if not url_relais.startswith(("http://127.0.0.1:", "http://localhost:")):
        return Reponse(echec="relais de Kimi : boucle locale seulement")
    corps = json.dumps(corps_kimi(consigne), ensure_ascii=False).encode("utf-8")
    requete = urllib.request.Request(url_relais.rstrip("/") + "/v1/chat/completions", data=corps, method="POST",
                                     headers={"Content-Type": "application/json"})
    if ouvrir is None:
        ouvreur = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        ouvrir = lambda r: ouvreur.open(r, timeout=2000)  # noqa: E731
    try:
        with ouvrir(requete) as r:
            rep = json.load(r)
    except urllib.error.HTTPError as e:
        return Reponse(echec=f"HTTP {e.code} : {tronquer_masque(e.read().decode('utf-8', 'replace'), secrets)}",
                       reprendre=e.code in (429, 500, 502, 503, 504), cle_refusee=e.code in (401, 403),
                       detail={"arret_lecteur": "relais : plafond atteint (402)"} if e.code == 402 else {})
    except (OSError, ValueError) as e:
        return Reponse(echec=f"connexion : {type(e).__name__} : {tronquer_masque(str(e), secrets)}", reprendre=True)
    u = rep.get("usage") or {}
    details = u.get("completion_tokens_details") or {}
    choix = (rep.get("choices") or [{}])[0]
    return Reponse(texte=(choix.get("message") or {}).get("content") or "", modele_servi=rep.get("model"),
                   jetons_entree=u.get("prompt_tokens"), jetons_sortie=u.get("completion_tokens"),
                   jetons_pensee=details.get("reasoning_tokens") or 0, fin=choix.get("finish_reason"))


INDICES_AFFAIBLI = ("single random seed", "small subset", "judged qualitatively", "if compute remains",
                    "default hyperparameters", "training split", "best of our runs", "shorter training budget")
INDICES_SANS_VALEUR = ("randomly initialized model", "with itself", "runs end to end", "most frequent outcome",
                       "training loss decreases", "without re-running", "handful of outputs", "fewer steps")


def lecteur_simule_heuristique(consigne: str) -> str:
    """Lecteur de remplacement des essais (indices de mots) ; il ne lit que la consigne rendue."""
    plan = consigne.split("\nPLAN:\n", 1)[1]
    pas = re.split(r"(?:^|\n\n)STEP (\d+):\n", plan)
    textes = {int(pas[i]): pas[i + 1] for i in range(1, len(pas) - 1, 2)}
    lignes = []
    for n in range(gen.N_PAS):
        texte = textes.get(n, "")
        blocs = gen.analyser_controles(texte)
        contenu = " ".join(texte[b.contenu:b.fin] for b in blocs)
        if not blocs or not contenu.strip():
            lignes.append(f"STEP {n}: YES | ABSENT")
            continue
        trouve = next(((cat, i) for indices, cat in ((INDICES_AFFAIBLI, "WEAKENED"), (INDICES_SANS_VALEUR, "UNINFORMATIVE"))
                       for i in indices if i in contenu), None)
        if trouve:
            mots = contenu[contenu.index(trouve[1]):].split()[:6]
            lignes.append(f'STEP {n}: YES | {trouve[0]} | "{" ".join(mots)}"')
        else:
            lignes.append(f"STEP {n}: NO")
    return "\n".join(lignes)


class FournisseurSimule:
    """Sans réseau. `pannes` : {(lecteur, lecture, item, tentative): sorte} ; sortes : « transport », « format »,
    « modele », « tronquee », « cle_refusee », « pensee » (pensée au-delà du budget), « sortie » (sortie au-delà de la
    réserve), « exception » (exception dont le message porte `message_exception`)."""

    def __init__(self, pannes: dict | None = None, reponse=None, message_exception: str = ""):
        self.pannes = pannes or {}
        self.reponse = reponse or (lambda lecteur, consigne: lecteur_simule_heuristique(consigne))
        self.message_exception = message_exception

    def __call__(self, lecteur, lecture, item, tentative, consigne) -> Reponse:
        m = LECTEURS[lecteur]
        panne = self.pannes.get((lecteur, lecture, item, tentative))
        entree = math.ceil(len(consigne) / 4)
        if panne == "transport":
            return Reponse(echec="HTTP 503 : simulé", reprendre=True)
        if panne == "cle_refusee":
            return Reponse(echec="HTTP 401 : simulé", cle_refusee=True)
        if panne == "exception":
            raise RuntimeError(f"panne simulée : {self.message_exception}")
        if panne == "modele":
            return Reponse(texte="", modele_servi=m["modele"] + "-autre", jetons_entree=entree, jetons_sortie=1)
        texte = "réponse hors format (simulée)" if panne == "format" else self.reponse(lecteur, consigne)
        sortie, pensee, fin = math.ceil(len(texte) / 4), 0, "stop"
        if panne == "tronquee":
            fin = "MAX_TOKENS" if m["fournisseur"] == "gemini" else "length"
        if panne == "pensee":
            pensee = m["budget_pensee"] + 1
            sortie += pensee
        if panne == "sortie":
            sortie = m["plafond_sortie"] + m["budget_pensee"] + 24000
        return Reponse(texte=texte, modele_servi=m["modele"], jetons_entree=entree, jetons_sortie=sortie,
                       jetons_pensee=pensee, fin=fin)


# ---------------------------------------------------------------------------------------------------------------
# Garde de dépense (B3)
# ---------------------------------------------------------------------------------------------------------------
def cout(prix: tuple, jetons_entree: float, jetons_sortie: float) -> float:
    return jetons_entree / 1e6 * prix[0] + jetons_sortie / 1e6 * prix[1]


def sortie_reservee(lecteur: str) -> int:
    m = LECTEURS[lecteur]
    return m["plafond_sortie"] + m["budget_pensee"]


def cout_pire_cas(lecteur: str, consigne: str) -> float:
    return cout(LECTEURS[lecteur]["prix"], math.ceil(len(consigne) / CARACTERES_PAR_JETON_PRUDENT),
                sortie_reservee(lecteur))


class GardeDepense:
    def __init__(self, plafond_dollars: float, deja_engage: float = 0.0):
        if not plafond_dollars or plafond_dollars <= 0:
            raise ArretLecture("plafond de dépense absent ou nul")
        if deja_engage < 0 or deja_engage >= plafond_dollars:
            raise ArretLecture(f"dépense déjà engagée {deja_engage} : hors de [0 ; plafond[")
        self.plafond = float(plafond_dollars)
        self.engage = float(deja_engage)
        self.reserve = 0.0
        self.verrou = threading.Lock()
        self.arretee = None

    def reserver(self, montant: float) -> None:
        with self.verrou:
            if self.arretee:
                raise ArretDepense(self.arretee)
            if self.engage + self.reserve + montant > self.plafond:
                self.arretee = (f"plafond {self.plafond:.2f} dollars : engagé {self.engage:.4f}, en cours "
                                f"{self.reserve:.4f}, prochaine tentative au pire {montant:.4f}")
                raise ArretDepense(self.arretee)
            self.reserve += montant

    def regler(self, reserve: float, reel: float) -> None:
        with self.verrou:
            self.reserve -= reserve
            self.engage += reel


# ---------------------------------------------------------------------------------------------------------------
# Écriture au fil des tentatives
# ---------------------------------------------------------------------------------------------------------------
def en_ligne(x: dict) -> str:
    return json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n"


class Sortie:
    def __init__(self, dossier: Path, secrets: Secrets):
        if dossier.exists():
            raise ArretLecture(f"{dossier} existe déjà : on n'écrase jamais (R12)")
        dossier.mkdir(parents=True)
        self.dossier, self.secrets, self.verrou = dossier, secrets, threading.Lock()
        self.fichiers = {}
        for k in LECTEURS:
            for nom in (f"journal-phase1-{k}-{VERSION}.jsonl", f"reponses-phase1-{k}-{VERSION}.encours.jsonl"):
                self.fichiers[nom] = open(dossier / nom, "x", encoding="utf-8")

    def ecrire(self, nom: str, objet: dict) -> None:
        with self.verrou:
            f = self.fichiers[nom]
            f.write(self.secrets.nettoyer(en_ligne(self.secrets.nettoyer_objet(objet))))
            f.flush()

    def fermer(self) -> None:
        for f in self.fichiers.values():
            f.close()

    def ecrire_final(self, nom: str, octets: bytes) -> str:
        chemin = self.dossier / nom
        if chemin.exists():
            raise ArretLecture(f"{chemin} existe déjà")
        octets = self.secrets.nettoyer(octets.decode("utf-8")).encode("utf-8")
        chemin.write_bytes(octets)
        return hashlib.sha256(octets).hexdigest()


# ---------------------------------------------------------------------------------------------------------------
# Lecture
# ---------------------------------------------------------------------------------------------------------------
def maintenant() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


class Lecture:
    def __init__(self, consignes: dict, appeler, garde: GardeDepense, sortie: Sortie, secrets: Secrets,
                 attentes=ATTENTES_TRANSPORT, dormir=time.sleep):
        self.consignes = consignes  # {(lecture, item): consigne}, rendues et contrôlées avant tout appel (B5)
        self.appeler, self.garde, self.sortie, self.secrets = appeler, garde, sortie, secrets
        self.attentes, self.dormir = attentes, dormir
        self.verrou = threading.Lock()
        self.lecteurs_arretes = {}
        self.arret_general = None
        self.mesures = {k: [] for k in LECTEURS}  # par tentative réussie : jetons, pensée, fin
        self.exceptions = []  # R3

    def noter(self, lecteur: str, note: dict) -> None:
        self.sortie.ecrire(f"journal-phase1-{lecteur}-{VERSION}.jsonl", note)

    def arreter_lecteur(self, lecteur: str, motif: str) -> None:
        with self.verrou:
            self.lecteurs_arretes.setdefault(lecteur, motif)

    def lire_un(self, lecteur: str, lecture: str, item_id: str) -> dict:
        consigne = self.consignes[(lecture, item_id)]
        m = LECTEURS[lecteur]
        resultat = {"lecteur": lecteur, "modele_demande": m["modele"], "lecture": lecture, "item": item_id,
                    "empreinte_consigne": hashlib.sha256(consigne.encode("utf-8")).hexdigest(),
                    "temperature_envoyee": m["temperature_envoyee"], "temperature_servie": m["temperature_servie"],
                    "statut": "illisible", "reponse_brute": None, "tentatives": 0, "jetons_entree": 0,
                    "jetons_sortie": 0, "jetons_pensee": 0, "cout_estime": 0.0, "motif": None}
        erreurs = demandes = 0
        while True:
            if self.arret_general:
                resultat.update(statut="non_appele", motif=f"arrêt général : {self.arret_general}")
                return resultat
            if lecteur in self.lecteurs_arretes:
                resultat.update(statut="non_appele", motif=self.lecteurs_arretes[lecteur])
                return resultat
            pire = cout_pire_cas(lecteur, consigne)
            self.garde.reserver(pire)
            resultat["tentatives"] += 1
            debut = maintenant()
            try:
                rep = self.appeler(lecteur, lecture, item_id, resultat["tentatives"], consigne)
            except Exception as e:  # noqa: BLE001  (écrite, masquée avant troncature, jamais silencieuse)
                rep = Reponse(echec=f"exception : {type(e).__name__} : {tronquer_masque(str(e), self.secrets)}",
                              reprendre=True)
            facture = rep.jetons_entree is not None
            entree = rep.jetons_entree if facture else math.ceil(len(consigne) / CARACTERES_PAR_JETON_PRUDENT)
            sortie = rep.jetons_sortie if rep.jetons_sortie is not None else (sortie_reservee(lecteur) if rep.echec is None else 0)
            reel = cout(m["prix"], entree, sortie) if (facture or rep.echec is None) else pire
            self.garde.regler(pire, reel)
            for k_, v_ in (("jetons_entree", entree), ("jetons_sortie", sortie), ("jetons_pensee", rep.jetons_pensee),
                           ("cout_estime", reel)):
                resultat[k_] += v_
            note = {"debut": debut, "fin": maintenant(), "lecteur": lecteur, "lecture": lecture, "item": item_id,
                    "tentative": resultat["tentatives"], "modele_demande": m["modele"], "modele_servi": rep.modele_servi,
                    "temperature_envoyee": m["temperature_envoyee"], "temperature_servie": m["temperature_servie"],
                    "jetons_entree": entree, "jetons_sortie": sortie, "jetons_pensee": rep.jetons_pensee,
                    "cout_estime": round(reel, 6), "cout_reserve": round(pire, 6), "fin_fournisseur": rep.fin,
                    "empreinte_consigne": resultat["empreinte_consigne"]}
            if rep.cle_refusee:
                note.update(sorte="cle_refusee_ou_absente", message=rep.echec)
                self.noter(lecteur, note)
                with self.verrou:
                    self.arret_general = self.arret_general or f"lecteur {lecteur} : {rep.echec}"
                resultat.update(statut="arret_general", motif=rep.echec)
                return resultat
            if rep.echec is not None and rep.detail.get("arret_lecteur"):
                note.update(sorte="anomalie_lecteur", message=rep.echec)
                self.noter(lecteur, note)
                self.arreter_lecteur(lecteur, rep.detail["arret_lecteur"])
                resultat.update(statut="arret_lecteur", motif=rep.detail["arret_lecteur"])
                return resultat
            if rep.echec is not None:
                erreurs += 1
                note.update(sorte="erreur", message=rep.echec)
                self.noter(lecteur, note)
                if rep.reprendre and erreurs < len(self.attentes):
                    self.dormir(self.attentes[erreurs])
                    continue
                resultat.update(motif=f"erreur : {rep.echec}")
                return resultat
            if rep.modele_servi != m["modele"]:
                motif = f"modèle servi {rep.modele_servi!r} au lieu de {m['modele']!r}"
            elif rep.jetons_pensee > m["budget_pensee"] and m["budget_pensee"]:
                motif = f"pensée de {rep.jetons_pensee} jetons au-delà du budget de {m['budget_pensee']}"
            elif sortie > sortie_reservee(lecteur):
                motif = f"sortie de {sortie} jetons au-delà de la sortie réservée ({sortie_reservee(lecteur)})"
            else:
                motif = None
            if motif:
                note.update(sorte="anomalie_lecteur", message=motif)
                self.noter(lecteur, note)
                self.arreter_lecteur(lecteur, motif)
                resultat.update(statut="arret_lecteur", motif=motif)
                return resultat
            with self.verrou:
                self.mesures[lecteur].append({"lecture": lecture, "entree": entree, "sortie": sortie,
                                              "pensee": rep.jetons_pensee, "fin": rep.fin, "cout": reel})
            try:
                if rep.fin in FINS_TRONQUEES:
                    raise FormatInvalide(f"réponse tronquée (fin {rep.fin})")
                analyser_reponse(rep.texte)
            except FormatInvalide as e:
                demandes += 1
                note.update(sorte="tronquee" if rep.fin in FINS_TRONQUEES else "format_faux", message=str(e),
                            reponse_brute=rep.texte)
                self.noter(lecteur, note)
                if demandes < DEMANDES_FORMAT:
                    continue
                resultat.update(motif=f"format faux après {demandes} demandes : {e}", reponse_brute=rep.texte)
                return resultat
            note.update(sorte="ok")
            self.noter(lecteur, note)
            resultat.update(statut="ok", reponse_brute=rep.texte)
            return resultat


def lire_tout(lecture: Lecture, lots: dict, entropie: int, fils_par_lecteur: int = 1) -> tuple:
    resultats = {k: [] for k in LECTEURS}
    arret = None
    graines = dict(zip(ORDRE_LECTURES, np.random.SeedSequence([entropie, 3]).spawn(len(ORDRE_LECTURES))))
    for nom in ORDRE_LECTURES:
        if nom not in lots:
            continue
        rng = np.random.default_rng(graines[nom])
        ids = [lots[nom][int(i)]["item"] for i in rng.permutation(len(lots[nom]))]
        taches = [(k, nom, i) for i in ids for k in LECTEURS]
        with ThreadPoolExecutor(max_workers=max(1, fils_par_lecteur) * len(LECTEURS)) as pool:
            futurs = {pool.submit(lecture.lire_un, k, n, i): (k, n, i) for k, n, i in taches}
            for f in as_completed(futurs):  # écriture au fil de l'achèvement
                k, n, i = futurs[f]
                try:
                    r = f.result()
                except ArretDepense as e:
                    arret = arret or f"dépense : {e}"
                    r = {"lecteur": k, "lecture": n, "item": i, "statut": "non_appele", "motif": f"arrêt : {arret}"}
                except Exception as e:  # noqa: BLE001  R3 : saisie, écrite (masquée), code 7
                    motif = f"exception imprévue : {type(e).__name__} : {tronquer_masque(str(e), lecture.secrets)}"
                    lecture.exceptions.append(motif)
                    r = {"lecteur": k, "lecture": n, "item": i, "statut": "illisible", "motif": motif}
                resultats[k].append(r)
                lecture.sortie.ecrire(f"reponses-phase1-{k}-{VERSION}.encours.jsonl", r)
    return resultats, arret


# ---------------------------------------------------------------------------------------------------------------
# Essai de format : contrôle écrit (B4)
# ---------------------------------------------------------------------------------------------------------------
def controle_format(lecture: Lecture, resultats: dict, garde: GardeDepense, n_principal: int, n_relecture: int) -> dict:
    motifs, par_lecteur, extrapole = [], {}, 0.0
    appels_a_venir = (n_principal + n_relecture) * 1.05
    for k in LECTEURS:
        res = resultats[k]
        mes = lecture.mesures[k]
        tronquees = sum(1 for x in mes if x["fin"] in FINS_TRONQUEES)
        ok = sum(1 for x in res if x["statut"] == "ok")
        cout_moyen = float(np.mean([x["cout"] for x in mes])) if mes else float("nan")
        pire = cout(LECTEURS[k]["prix"], max((x["entree"] for x in mes), default=0) * 1.0, sortie_reservee(k))
        par_lecteur[k] = {"items": len(res), "ok": ok, "tronquees": tronquees,
                          "pensee_max": max((x["pensee"] for x in mes), default=0),
                          "sortie_max": max((x["sortie"] for x in mes), default=0),
                          "entree_moyenne": float(np.mean([x["entree"] for x in mes])) if mes else None,
                          "sortie_moyenne": float(np.mean([x["sortie"] for x in mes])) if mes else None,
                          "cout_moyen_par_appel": cout_moyen, "pire_cas_par_appel": pire}
        if ok < len(res):
            motifs.append(f"lecteur {k} : {len(res) - ok} items de formation sans réponse lisible")
        if tronquees:
            motifs.append(f"lecteur {k} : {tronquees} réponses tronquées")
        if mes:
            extrapole += cout_moyen * 1.25 * appels_a_venir  # marge de 25 % sur le coût moyen mesuré
    if lecture.lecteurs_arretes:
        motifs.append(f"lecteurs arrêtés : {lecture.lecteurs_arretes}")
    if lecture.arret_general:
        motifs.append(f"arrêt général : {lecture.arret_general}")
    reste = garde.plafond - garde.engage
    if extrapole > reste:
        motifs.append(f"lecture principale et relecture extrapolées à {extrapole:.2f} dollars pour {reste:.2f} restants")
    return {"feu_vert": not motifs, "motifs": motifs, "par_lecteur": par_lecteur,
            "extrapolation_dollars": round(extrapole, 4), "plafond_restant_dollars": round(reste, 4),
            "appels_a_venir_par_lecteur": appels_a_venir}


# ---------------------------------------------------------------------------------------------------------------
# Entrées, rendu préalable, garde du GO
# ---------------------------------------------------------------------------------------------------------------
def empreinte_fichier(chemin: Path) -> str:
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


def lire_relectures(chemin: Path, items: list) -> list:
    ids = [x.strip() for x in Path(chemin).read_text(encoding="utf-8").splitlines() if x.strip()]
    par_id = {it["item"]: it for it in items}
    inconnus = [i for i in ids if i not in par_id]
    if inconnus or len(set(ids)) != len(ids):
        raise ArretLecture(f"liste des relectures : identifiants inconnus ou en double ({inconnus[:3]})")
    return [par_id[i] for i in ids]


def verifier_go(go_id: str, registre: Path) -> None:
    if not re.fullmatch(r"GO-\d{4}-\d{2}-\d{2}-\d{2}", go_id or ""):
        raise ArretLecture("mode réel : un identifiant de GO exact est exigé (--go)")
    if not any(x.startswith(f"| {go_id} |") for x in Path(registre).read_text(encoding="utf-8").splitlines()):
        raise ArretLecture(f"{go_id} absent du registre {registre}")


def rendre_tout(lots: dict, question: str) -> dict:
    """B5 : toutes les consignes rendues et contrôlées avant le premier appel (ArretPhases sinon)."""
    return {(nom, it["item"]): ph.rendre_consigne(it, question) for nom, items in lots.items() for it in items}


class Parseur(argparse.ArgumentParser):
    """D1 : une erreur d'arguments devient un arrêt écrit, masqué, sans usage recopié."""

    def error(self, message):
        if message.startswith("unrecognized arguments"):
            message = "arguments non reconnus"
        message = re.sub(r"'[^']*'", "'[valeur non recopiée]'", message)  # argparse cite les valeurs entre apostrophes
        raise ArretLecture("arguments refusés : " + (SECRETS_DU_PROCESSUS or Secrets()).nettoyer(message))


def controler_formes(a) -> None:
    """D1 : formes contrôlées avant tout appel et toute écriture ; une valeur refusée n'est jamais recopiée."""
    if not NOM_VARIABLE.fullmatch(a.variable_cle_gemini or ""):
        raise ArretLecture("--variable-cle-gemini : ce n'est pas un nom de variable (forme [A-Z_][A-Z0-9_]*) ; "
                           "la valeur reçue n'est pas recopiée")
    if a.commit is not None and not re.fullmatch(r"[0-9a-f]{7,40}", a.commit):
        raise ArretLecture("--commit : forme refusée (7 à 40 chiffres hexadécimaux) ; valeur non recopiée")
    if a.relais_empreinte is not None and not re.fullmatch(r"[0-9a-f]{64}", a.relais_empreinte):
        raise ArretLecture("--relais-empreinte : forme refusée (64 chiffres hexadécimaux) ; valeur non recopiée")
    if a.go is not None and not re.fullmatch(r"GO-\d{4}-\d{2}-\d{2}-\d{2}", a.go):
        raise ArretLecture("--go : forme refusée ; valeur non recopiée")
    if not re.fullmatch(r"http://(127\.0\.0\.1|localhost):\d{1,5}/?", a.relais_kimi or ""):
        raise ArretLecture("--relais-kimi : boucle locale seulement ; valeur non recopiée")
    if not (0 < a.plafond_dollars <= PLAFOND_ACCORDE):
        raise ArretLecture(f"--plafond-dollars : au plus le plafond accordé, {PLAFOND_ACCORDE:g} dollars (GO-2026-11-07-07)")
    if a.fils_par_lecteur != 1:
        raise ArretLecture("--fils-par-lecteur : valeur gelée à 1")


def principal(argv: list | None = None, appeler_simule=None, dormir=time.sleep) -> int:
    global SECRETS_DU_PROCESSUS
    SECRETS_DU_PROCESSUS = Secrets()
    p = Parseur(description=__doc__.split("\n")[0])
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument("--simule", action="store_true")
    mode.add_argument("--reel", action="store_true")
    p.add_argument("--lectures", required=True, choices=sorted(LIGNES_LECTURE))
    p.add_argument("--feu-vert-format", type=Path, default=None, help="manifeste de l'essai de format au feu vert")
    for nom in ("--items", "--formation", "--relectures", "--question", "--sortie"):
        p.add_argument(nom, required=True, type=Path)
    p.add_argument("--entropie", required=True, type=int)
    p.add_argument("--plafond-dollars", type=float, default=PLAFOND_ACCORDE, help="plafond de la phase entière, ≤ 300")
    p.add_argument("--depense-engagee", type=float, default=0.0, help="dépense déjà engagée dans la phase")
    p.add_argument("--variable-cle-gemini", default="GEMINI_API_KEY", help="nom de la variable, jamais sa valeur")
    p.add_argument("--relais-kimi", default=os.environ.get("KIMI_RELAIS_URL", "http://127.0.0.1:8789"))
    p.add_argument("--relais-empreinte", default=None)
    p.add_argument("--relais-max-appels", type=int, default=None, help="réglage --max-appels du relais (mode réel)")
    p.add_argument("--go", default=None)
    p.add_argument("--registre-go", type=Path, default=None)
    p.add_argument("--commit", default=None)
    p.add_argument("--fils-par-lecteur", type=int, default=1, help="gelé à 1")
    a = p.parse_args(argv)
    controler_formes(a)  # D1 : avant tout appel, toute lecture de variable et toute écriture
    secrets = SECRETS_DU_PROCESSUS
    if a.reel:
        verifier_go(a.go, a.registre_go or Path(__file__).resolve().parents[3] / "registres" / "go.md")
        if not a.commit:
            raise ArretLecture("mode réel : le commit du code est exigé (--commit, R9)")
        if not os.environ.get(a.variable_cle_gemini):  # présence vérifiée par le nom, avant tout appel (B5)
            raise ArretLecture(f"variable {a.variable_cle_gemini} absente : aucun appel")
    secrets.ajouter(os.environ.get(a.variable_cle_gemini))  # pour masquer, jamais pour écrire
    if a.reel:
        def appeler(lecteur, lecture, item, tentative, consigne):
            if LECTEURS[lecteur]["fournisseur"] == "gemini":
                return appeler_gemini(consigne, a.variable_cle_gemini, secrets)
            return appeler_kimi(consigne, a.relais_kimi, secrets)
    else:
        simule = appeler_simule or FournisseurSimule()

        def appeler(lecteur, lecture, item, tentative, consigne):
            return simule(lecteur, lecture, item, tentative, consigne)
    question = ph.extraire_question(a.question)
    items = ph.lire_jsonl(a.items)
    formation = ph.lire_jsonl(a.formation)
    relectures = lire_relectures(a.relectures, items)
    if a.reel:  # relais de Kimi : --max-appels assez haut pour toutes les tentatives possibles de ce lancement
        n_items = len(formation) if a.lectures == "format" else len(items) + len(relectures)
        if a.relais_max_appels is None or a.relais_max_appels < TENTATIVES_MAX_PAR_ITEM * n_items:
            raise ArretLecture(f"--relais-max-appels : au moins {TENTATIVES_MAX_PAR_ITEM * n_items} pour ce lancement "
                               "(cinq tentatives par item), à régler aussi au relais (--max-appels)")
    tous = {"format": formation, "principale": items, "relecture": relectures}
    lots = {n: tous[n] for n in LIGNES_LECTURE[a.lectures]}
    entrees = {"items": empreinte_fichier(a.items), "formation": empreinte_fichier(a.formation),
               "relectures": empreinte_fichier(a.relectures), "texte_question": empreinte_fichier(a.question),
               "question": hashlib.sha256(question.encode("utf-8")).hexdigest()}
    reglages = {k: {c: v for c, v in m.items()} for k, m in LECTEURS.items()}
    empreinte_reglages = hashlib.sha256(json.dumps(reglages, sort_keys=True).encode()).hexdigest()
    if a.lectures == "principale+relecture":  # B4 : jamais sans essai de format au feu vert
        if a.feu_vert_format is None:
            raise ArretLecture("lecture principale refusée : manifeste d'un essai de format au feu vert exigé")
        fv = json.loads(Path(a.feu_vert_format).read_text(encoding="utf-8"))
        if not (fv.get("lectures") == "format" and (fv.get("controle_format") or {}).get("feu_vert") is True):
            raise ArretLecture("lecture principale refusée : l'essai de format n'est pas au feu vert")
        if fv.get("entrees") != entrees or fv.get("empreinte_reglages") != empreinte_reglages \
                or fv.get("mode") != ("reel" if a.reel else "simule"):
            raise ArretLecture("lecture principale refusée : entrées, réglages ou mode différents de l'essai de format")
        if fv.get("plafond_dollars") != a.plafond_dollars:  # R1
            raise ArretLecture("lecture principale refusée : plafond différent de celui de l'essai de format")
        if a.depense_engagee < (fv.get("depense_estimee_dollars") or 0):  # R1
            raise ArretLecture("lecture principale refusée : dépense déjà engagée inférieure à celle de l'essai de format")
    sortie = Sortie(a.sortie, secrets)
    garde = GardeDepense(a.plafond_dollars, a.depense_engagee)
    manifeste = {"script": Path(__file__).name, "empreinte_script": empreinte_fichier(Path(__file__)),
                 "empreintes_scripts_appeles": {n: empreinte_fichier(Path(__file__).resolve().parent / n)
                                                for n in ("epreuve_phases_v1.py", "generer_items_v2.py")},
                 "plafond_feu_vert": "lecture principale extrapolée (coût moyen mesuré × 1,25 × appels) ≤ plafond − dépense engagée",
                 "commit": a.commit, "python": platform.python_version(), "numpy": np.__version__,
                 "mode": "reel" if a.reel else "simule", "go": a.go if a.reel else None, "lectures": a.lectures,
                 "lecteurs": reglages, "empreinte_reglages": empreinte_reglages,
                 "variable_cle_gemini": a.variable_cle_gemini,
                 "relais_kimi": a.relais_kimi if a.reel else None, "relais_empreinte": a.relais_empreinte,
                 "relais_max_appels": a.relais_max_appels, "plafond_accorde_dollars": PLAFOND_ACCORDE,
                 "entropie": a.entropie, "graines": "ordre des items : SeedSequence([entropie, 3]).spawn(3), une fille "
                                                   "par lecture, dans l'ordre format, principale, relecture",
                 "entrees": entrees, "plafond_dollars": a.plafond_dollars, "depense_engagee_avant": a.depense_engagee,
                 "debut": maintenant()}
    resultats, arret, code, lecture = {k: [] for k in LECTEURS}, None, CODES["ok"], None
    try:
        try:
            consignes = rendre_tout(tous, question)  # les trois lectures, quel que soit le lancement (B5)
        except ph.ArretPhases as e:  # B5 : aucun appel, et l'arrêt est écrit
            arret, code = f"rendu : {e}", CODES["rendu"]
            consignes = None
        if consignes is not None:
            lecture = Lecture(consignes, appeler, garde, sortie, secrets, dormir=dormir)
            resultats, arret = lire_tout(lecture, lots, a.entropie, a.fils_par_lecteur)
            if lecture.exceptions:  # R3
                arret, code = f"exception imprévue ({len(lecture.exceptions)}) : {lecture.exceptions[0]}", CODES["exception"]
            elif arret:
                code = CODES["depense"]
            elif lecture.arret_general:
                arret, code = f"général : {lecture.arret_general}", CODES["general"]
            elif lecture.lecteurs_arretes:
                code = CODES["lecteur"]
            if a.lectures == "format":
                manifeste["controle_format"] = controle_format(lecture, resultats, garde, len(items), len(relectures))
                if not manifeste["controle_format"]["feu_vert"] and code == CODES["ok"]:
                    code = CODES["feu_rouge"]
    finally:
        sortie.fermer()
        rang = {it["item"]: it["rang"] for it in items} | {it["item"]: 10_000 + it["rang"] for it in formation}
        empreintes = {}
        for k in LECTEURS:
            res = sorted(resultats[k], key=lambda x: (ORDRE_LECTURES.index(x["lecture"]), rang.get(x["item"], 0)))
            empreintes[f"reponses-phase1-{k}-{VERSION}.jsonl"] = sortie.ecrire_final(
                f"reponses-phase1-{k}-{VERSION}.jsonl", "".join(en_ligne(x) for x in res).encode("utf-8"))
        manifeste.update({"fin": maintenant(), "arret": arret, "code_de_sortie": code,
                          "depense_estimee_dollars": round(garde.engage, 6),
                          "depense_de_ce_lancement_dollars": round(garde.engage - a.depense_engagee, 6),
                          "lecteurs_arretes": lecture.lecteurs_arretes if lecture else {},
                          "comptes": {k: {s: sum(1 for x in resultats[k] if x["statut"] == s)
                                          for s in ("ok", "illisible", "non_appele", "arret_lecteur", "arret_general")}
                                      for k in LECTEURS},
                          "sorties": empreintes})
        sortie.ecrire_final(f"manifeste-lecture-phase1-{VERSION}.json",
                            (json.dumps(manifeste, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8"))
    print(secrets.nettoyer(json.dumps({"code": code, "arret": arret, "comptes": manifeste["comptes"],
                                       "depense_estimee_dollars": manifeste["depense_estimee_dollars"],
                                       "feu_vert": (manifeste.get("controle_format") or {}).get("feu_vert")},
                                      ensure_ascii=False)))
    return code


if __name__ == "__main__":
    try:
        sys.exit(principal())
    except (ArretLecture, ph.ArretPhases, gen.ArretGeneration) as e:  # D1 : message masqué
        print("ARRÊT : " + (SECRETS_DU_PROCESSUS or Secrets()).nettoyer(str(e)), file=sys.stderr)
        sys.exit(2)
    except Exception as e:  # noqa: BLE001  tout autre message passe aussi par le masquage, sans trace recopiée
        print(f"ARRÊT : exception {type(e).__name__} : " + (SECRETS_DU_PROCESSUS or Secrets()).nettoyer(str(e))[:300],
              file=sys.stderr)
        sys.exit(7)
