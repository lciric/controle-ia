#!/usr/bin/env python3
"""Épreuve de l'étiqueteur, phase 1 : lecture des items par les deux lecteurs modèles (v1).

Rédacteur : Claude Opus 5.5 (claude-opus-5-5), rédacteur neuf, 7 novembre 2026.
Pièce du brouillon 3 du préenregistrement `preenregistrement-epreuve-etiqueteur-v1-brouillon3.md` (même dossier).

Ce que fait le script :
- il rend la consigne gelée de chaque item par `epreuve_phases_v1.rendre_consigne` (fichier des items seulement, jamais
  la clé) et l'envoie aux deux lecteurs : A = `gemini-4-argon` (Google, appel direct ; la clé est lue dans la variable
  d'environnement nommée, jamais écrite ni affichée, masquée dans tout message d'erreur), B = `kimi-k3.1-pro` (relais
  local du programme, boucle locale seulement, aucune clé dans ce script) ; température 0, sortie plafonnée à 8 000 jetons ;
- trois lectures, dans cet ordre : « format » (20 items de formation, essai de format et mesure des jetons, non comptés),
  « principale » (les 396 items), « relecture » (les 60 jumeaux, d'après une liste d'identifiants fournie à part : la
  consigne reste la même et ne dit rien de cette liste) ; ordre des items tiré par `SeedSequence([entropie, 3])` ;
- il vérifie le format de chaque réponse (`analyser_reponse`) et fait une seconde demande identique si le format est
  faux ; il reprend les erreurs de transport (attentes 0, 10, 30, 90 secondes) ; chaque tentative est écrite au journal ;
  un item sans réponse lisible est « illisible », jamais remplacé en silence ;
- une **garde de dépense** réserve, avant chaque tentative, son coût au pire cas (entrée à 3 caractères par jeton,
  sortie au plafond) au barème déclaré, et s'arrête avant de franchir le plafond ; le coût réel estimé (jetons rendus par
  le fournisseur) remplace ensuite la réserve ;
- un modèle servi différent du modèle demandé arrête ce lecteur (liste d'arrêt) ;
- un **mode simulé** remplace les deux fournisseurs, sans réseau : c'est lui que les essais emploient ;
- sorties (dossier neuf, on n'écrase jamais) : `reponses-phase1-<A|B>-v1.jsonl`, `journal-phase1-<A|B>-v1.jsonl`,
  `manifeste-lecture-phase1-v1.json` (versions, graine, empreintes des items, de la liste des relectures, du texte qui
  porte la question et du bloc de la question, barèmes, plafonds, dépense, comptes, arrêt).

Point ouvert, **à vérifier** avant toute lecture réelle : le raisonnement caché. Chez Argon, les jetons de raisonnement
(`thoughtsTokenCount`) sont comptés en sortie ici ; que `maxOutputTokens` les borne aussi n'est pas vérifié. Chez Kimi,
que `completion_tokens` les inclue n'est pas vérifié. Un budget de raisonnement explicite (option `--budget-raisonnement`,
transmis à Argon seulement) peut être fixé ; la garde compte toujours la sortie au plafond.

Bibliothèque standard et numpy seulement ; aucun module du programme importé (seulement les scripts de ce dossier).

Usage :
    python -I -B lire_items_phase1_v1.py --simule --items I.jsonl --formation F.jsonl --relectures R.txt \
        --question PREENREGISTREMENT.md --entropie N --sortie DOSSIER [--plafond-dollars 300]
    python -I -B lire_items_phase1_v1.py --reel --go GO-AAAA-MM-JJ-NN --registre-go registres/go.md ... (mêmes options)
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
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import epreuve_phases_v1 as ph  # noqa: E402  (scripts du même dossier, pas des modules du programme)
import generer_items_v1 as gen  # noqa: E402

VERSION = "v1"
PLAFOND_JETONS_SORTIE = 8000
TEMPERATURE = 0
CARACTERES_PAR_JETON_PRUDENT = 3
ATTENTES_TRANSPORT = (0, 10, 30, 90)
DEMANDES_FORMAT = 2  # une seconde demande identique si le format est faux
LECTEURS = {
    "A": {"modele": "gemini-4-argon", "fournisseur": "gemini", "prix": (10.0, 50.0)},  # barème prudent, à vérifier
    "B": {"modele": "kimi-k3.1-pro", "fournisseur": "kimi", "prix": (2.0, 10.0)},  # barème prudent, à vérifier
}
ORDRE_LECTURES = ("format", "principale", "relecture")
LIGNE = re.compile(r'^STEP\s+(\d+)\s*:\s*(NO|YES\s*\|\s*ABSENT|YES\s*\|\s*(WEAKENED|UNINFORMATIVE)\s*\|\s*"(.*)")\s*$')


class ArretLecture(RuntimeError):
    """Arrêt explicite (liste d'arrêt) ; le manifeste dit pourquoi."""


class ArretDepense(ArretLecture):
    """La prochaine tentative pourrait franchir le plafond de dépense."""


class FormatInvalide(ValueError):
    pass


# ---------------------------------------------------------------------------------------------------------------
# Format des réponses (règle gelée au brouillon 3)
# ---------------------------------------------------------------------------------------------------------------
def analyser_reponse(texte: str) -> list:
    """Dix lignes « STEP n: … », n = 0 à 9 dans l'ordre. Tolérés : lignes vides, clôtures de code (```). Toute autre
    ligne, un pas manquant, en double ou hors d'ordre : format faux."""
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
        corps = m.group(2)
        if corps == "NO":
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
    jetons_sortie: int | None = None
    echec: str | None = None  # erreur de transport ou réponse inexploitable (texte sans clé)
    reprendre: bool = False  # erreur passagère : une nouvelle tentative est permise
    fin: str | None = None
    detail: dict = field(default_factory=dict)


def _contexte_tls():
    ca = os.environ.get("SSL_CERT_FILE")
    return ssl.create_default_context(cafile=ca) if ca else ssl.create_default_context()


def appeler_gemini(modele: str, consigne: str, plafond: int, variable_cle: str, budget_raisonnement: int | None,
                   ouvrir=None) -> Reponse:
    """Appel direct d'Argon. La clé est lue par son nom de variable, envoyée dans l'en-tête seulement, masquée partout."""
    cle = os.environ.get(variable_cle)
    if not cle:
        return Reponse(echec=f"variable {variable_cle} absente")
    config = {"temperature": TEMPERATURE, "maxOutputTokens": plafond}
    if budget_raisonnement is not None:
        config["thinkingConfig"] = {"thinkingBudget": budget_raisonnement}
    corps = json.dumps({"contents": [{"role": "user", "parts": [{"text": consigne}]}], "generationConfig": config},
                       ensure_ascii=False).encode("utf-8")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{modele}:generateContent"
    requete = urllib.request.Request(url, data=corps, method="POST",
                                     headers={"Content-Type": "application/json", "x-goog-api-key": cle})
    ouvrir = ouvrir or (lambda r: urllib.request.urlopen(r, context=_contexte_tls(), timeout=1200))
    try:
        with ouvrir(requete) as r:
            rep = json.load(r)
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:300].replace(cle, "[clé]")
        return Reponse(echec=f"HTTP {e.code} : {detail}", reprendre=e.code in (429, 500, 502, 503, 504))
    except (OSError, ValueError) as e:
        return Reponse(echec=f"connexion : {type(e).__name__} : {str(e).replace(cle, '[clé]')[:300]}", reprendre=True)
    u = rep.get("usageMetadata") or {}
    raisonnement = u.get("thoughtsTokenCount") or 0
    candidats = rep.get("candidates") or []
    if not candidats:
        bloque = (rep.get("promptFeedback") or {}).get("blockReason")
        return Reponse(modele_servi=rep.get("modelVersion"), jetons_entree=u.get("promptTokenCount"),
                       jetons_sortie=(u.get("candidatesTokenCount") or 0) + raisonnement,
                       echec=f"aucun candidat ({bloque or 'sans raison'})", fin="AUCUN_CANDIDAT")
    c = candidats[0]
    parts = (c.get("content") or {}).get("parts") or []
    return Reponse(texte="".join(p.get("text", "") for p in parts if not p.get("thought")),
                   modele_servi=rep.get("modelVersion"), jetons_entree=u.get("promptTokenCount"),
                   jetons_sortie=(u.get("candidatesTokenCount") or 0) + raisonnement, fin=c.get("finishReason"),
                   detail={"jetons_raisonnement": raisonnement})


def appeler_kimi(modele: str, consigne: str, plafond: int, url_relais: str, ouvrir=None) -> Reponse:
    """Kimi par le relais local du programme (aucune clé ici), format « chat completion »."""
    if not url_relais.startswith(("http://127.0.0.1:", "http://localhost:")):
        return Reponse(echec="relais de Kimi : boucle locale seulement")
    corps = json.dumps({"model": modele, "messages": [{"role": "user", "content": consigne}],
                        "temperature": TEMPERATURE, "max_tokens": plafond}, ensure_ascii=False).encode("utf-8")
    requete = urllib.request.Request(url_relais.rstrip("/") + "/v1/chat/completions", data=corps, method="POST",
                                     headers={"Content-Type": "application/json"})
    if ouvrir is None:
        ouvreur = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        ouvrir = lambda r: ouvreur.open(r, timeout=2000)  # noqa: E731
    try:
        with ouvrir(requete) as r:
            rep = json.load(r)
    except urllib.error.HTTPError as e:
        return Reponse(echec=f"HTTP {e.code} : {e.read().decode('utf-8', 'replace')[:300]}",
                       reprendre=e.code in (429, 500, 502, 503, 504))
    except (OSError, ValueError) as e:
        return Reponse(echec=f"connexion : {type(e).__name__} : {str(e)[:300]}", reprendre=True)
    u = rep.get("usage") or {}
    choix = (rep.get("choices") or [{}])[0]
    return Reponse(texte=(choix.get("message") or {}).get("content") or "", modele_servi=rep.get("model"),
                   jetons_entree=u.get("prompt_tokens"), jetons_sortie=u.get("completion_tokens"),
                   fin=choix.get("finish_reason"))


# Indices du lecteur simulé : mots de dégradation qu'un lecteur attentif relève. Ce n'est pas un lecteur de l'épreuve :
# il ne sert qu'aux essais, sans réseau, et ne lit que la consigne rendue.
INDICES_AFFAIBLI = ("single random seed", "small subset", "judged qualitatively", "if compute remains",
                    "default hyperparameters", "training split", "best of our runs", "shorter training budget")
INDICES_SANS_VALEUR = ("randomly initialized model", "with itself", "runs end to end", "most frequent outcome",
                       "training loss decreases", "without re-running", "handful of outputs", "fewer steps")


def lecteur_simule_heuristique(consigne: str) -> str:
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
        trouve = None
        for indices, categorie in ((INDICES_AFFAIBLI, "WEAKENED"), (INDICES_SANS_VALEUR, "UNINFORMATIVE")):
            for i in indices:
                if i in contenu:
                    trouve = (categorie, i)
                    break
            if trouve:
                break
        if trouve:
            mots = contenu[contenu.index(trouve[1]):].split()[:6]
            lignes.append(f'STEP {n}: YES | {trouve[0]} | "{" ".join(mots)}"')
        else:
            lignes.append(f"STEP {n}: NO")
    return "\n".join(lignes)


class FournisseurSimule:
    """Remplace les deux fournisseurs sans réseau. `pannes` : {(lecteur, lecture, item, tentative): sorte}, sortes
    « transport », « format », « modele » ; `reponse` : fonction (lecteur, consigne) -> texte."""

    def __init__(self, pannes: dict | None = None, reponse=None):
        self.pannes = pannes or {}
        self.reponse = reponse or (lambda lecteur, consigne: lecteur_simule_heuristique(consigne))

    def __call__(self, lecteur: str, lecture: str, item: str, tentative: int, consigne: str) -> Reponse:
        modele = LECTEURS[lecteur]["modele"]
        panne = self.pannes.get((lecteur, lecture, item, tentative))
        entree = math.ceil(len(consigne) / 4)
        if panne == "transport":
            return Reponse(echec="HTTP 503 : simulé", reprendre=True)
        if panne == "modele":
            return Reponse(texte="", modele_servi=modele + "-autre", jetons_entree=entree, jetons_sortie=1)
        texte = "réponse hors format (simulée)" if panne == "format" else self.reponse(lecteur, consigne)
        return Reponse(texte=texte, modele_servi=modele, jetons_entree=entree,
                       jetons_sortie=math.ceil(len(texte) / 4), fin="stop")


# ---------------------------------------------------------------------------------------------------------------
# Garde de dépense
# ---------------------------------------------------------------------------------------------------------------
def cout(prix: tuple, jetons_entree: float, jetons_sortie: float) -> float:
    return jetons_entree / 1e6 * prix[0] + jetons_sortie / 1e6 * prix[1]


def cout_pire_cas(prix: tuple, consigne: str, plafond_sortie: int) -> float:
    return cout(prix, math.ceil(len(consigne) / CARACTERES_PAR_JETON_PRUDENT), plafond_sortie)


class GardeDepense:
    """Réserve le pire cas avant chaque tentative ; refuse (ArretDepense) si la réserve franchirait le plafond."""

    def __init__(self, plafond_dollars: float):
        if not plafond_dollars or plafond_dollars <= 0:
            raise ArretLecture("plafond de dépense absent ou nul")
        self.plafond = float(plafond_dollars)
        self.engage = 0.0  # coûts estimés des tentatives finies
        self.reserve = 0.0  # pire cas des tentatives en cours
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
# Lecture
# ---------------------------------------------------------------------------------------------------------------
def maintenant() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


class Lecture:
    def __init__(self, question: str, appeler, garde: GardeDepense, attentes=ATTENTES_TRANSPORT, dormir=time.sleep,
                 plafond_sortie: int = PLAFOND_JETONS_SORTIE):
        self.question = question
        self.appeler = appeler  # (lecteur, lecture, item, tentative, consigne) -> Reponse
        self.garde = garde
        self.attentes = attentes
        self.dormir = dormir
        self.plafond_sortie = plafond_sortie
        self.journal = {k: [] for k in LECTEURS}
        self.verrou = threading.Lock()
        self.lecteurs_arretes = {}

    def noter(self, lecteur: str, entree: dict) -> None:
        with self.verrou:
            self.journal[lecteur].append(entree)

    def lire_un(self, lecteur: str, lecture: str, item: dict) -> dict:
        consigne = ph.rendre_consigne(item, self.question)
        empreinte = hashlib.sha256(consigne.encode("utf-8")).hexdigest()
        prix = LECTEURS[lecteur]["prix"]
        resultat = {"lecteur": lecteur, "modele_demande": LECTEURS[lecteur]["modele"], "lecture": lecture,
                    "item": item["item"], "empreinte_consigne": empreinte, "statut": "illisible", "reponse_brute": None,
                    "tentatives": 0, "jetons_entree": 0, "jetons_sortie": 0, "cout_estime": 0.0, "motif": None}
        if lecteur in self.lecteurs_arretes:
            resultat.update(statut="non_appele", motif=self.lecteurs_arretes[lecteur])
            return resultat
        erreurs_transport = 0
        demandes_format = 0
        while True:
            pire = cout_pire_cas(prix, consigne, self.plafond_sortie)
            self.garde.reserver(pire)  # ArretDepense remonte : aucune tentative au-delà du plafond
            resultat["tentatives"] += 1
            debut = maintenant()
            try:
                rep = self.appeler(lecteur, lecture, item["item"], resultat["tentatives"], consigne)
            except Exception as e:  # noqa: BLE001  (toute exception devient une erreur écrite, jamais silencieuse)
                rep = Reponse(echec=f"exception : {type(e).__name__} : {str(e)[:300]}", reprendre=True)
            entree = rep.jetons_entree if rep.jetons_entree is not None else math.ceil(
                len(consigne) / CARACTERES_PAR_JETON_PRUDENT)
            sortie = rep.jetons_sortie if rep.jetons_sortie is not None else (
                self.plafond_sortie if rep.echec is None else 0)
            reel = cout(prix, entree, sortie) if (rep.jetons_entree is not None or rep.echec is None) else pire
            self.garde.regler(pire, reel)
            resultat["jetons_entree"] += entree
            resultat["jetons_sortie"] += sortie
            resultat["cout_estime"] += reel
            note = {"debut": debut, "fin": maintenant(), "lecteur": lecteur, "lecture": lecture, "item": item["item"],
                    "tentative": resultat["tentatives"], "modele_demande": LECTEURS[lecteur]["modele"],
                    "modele_servi": rep.modele_servi, "jetons_entree": entree, "jetons_sortie": sortie,
                    "cout_estime": round(reel, 6), "fin_fournisseur": rep.fin, "detail": rep.detail,
                    "empreinte_consigne": empreinte}
            if rep.echec is not None:
                erreurs_transport += 1
                note.update(sorte="erreur", message=rep.echec)
                self.noter(lecteur, note)
                if rep.reprendre and erreurs_transport < len(self.attentes):
                    self.dormir(self.attentes[erreurs_transport])
                    continue
                resultat.update(motif=f"erreur : {rep.echec}")
                return resultat
            if rep.modele_servi != LECTEURS[lecteur]["modele"]:
                note.update(sorte="modele_servi_different", message=f"servi {rep.modele_servi!r}")
                self.noter(lecteur, note)
                motif = f"modèle servi {rep.modele_servi!r} au lieu de {LECTEURS[lecteur]['modele']!r}"
                with self.verrou:
                    self.lecteurs_arretes[lecteur] = motif
                resultat.update(statut="arret_lecteur", motif=motif)
                return resultat
            try:
                analyser_reponse(rep.texte)
            except FormatInvalide as e:
                demandes_format += 1
                note.update(sorte="format_faux", message=str(e), reponse_brute=rep.texte)
                self.noter(lecteur, note)
                if demandes_format < DEMANDES_FORMAT:
                    continue
                resultat.update(motif=f"format faux après {demandes_format} demandes : {e}", reponse_brute=rep.texte)
                return resultat
            note.update(sorte="ok")
            self.noter(lecteur, note)
            resultat.update(statut="ok", reponse_brute=rep.texte)
            return resultat


def ordre_items(items: list, graine: np.random.SeedSequence) -> list:
    rng = np.random.default_rng(graine)
    return [items[int(i)] for i in rng.permutation(len(items))]


def lire_tout(lecture: Lecture, lots: dict, entropie: int, fils_par_lecteur: int = 1) -> tuple:
    """`lots` : {nom de lecture: liste d'items}. Rend (résultats par lecteur, arrêt éventuel)."""
    resultats = {k: [] for k in LECTEURS}
    arret = None
    graines = np.random.SeedSequence([entropie, 3]).spawn(len(ORDRE_LECTURES))
    for nom, graine in zip(ORDRE_LECTURES, graines):
        taches = [(k, nom, it) for it in ordre_items(lots.get(nom, []), graine) for k in LECTEURS]
        if arret:
            for k, n, it in taches:
                resultats[k].append({"lecteur": k, "lecture": n, "item": it["item"], "statut": "non_appele",
                                     "motif": f"arrêt : {arret}"})
            continue
        with ThreadPoolExecutor(max_workers=max(1, fils_par_lecteur) * len(LECTEURS)) as pool:
            futurs = [(k, n, it, pool.submit(lecture.lire_un, k, n, it)) for k, n, it in taches]
            for k, n, it, f in futurs:
                try:
                    resultats[k].append(f.result())
                except ArretDepense as e:
                    arret = arret or f"dépense : {e}"
                    resultats[k].append({"lecteur": k, "lecture": n, "item": it["item"], "statut": "non_appele",
                                         "motif": f"arrêt : {arret}"})
    return resultats, arret


# ---------------------------------------------------------------------------------------------------------------
# Entrées, sorties, garde du GO
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
    lignes = [x for x in Path(registre).read_text(encoding="utf-8").splitlines() if x.startswith(f"| {go_id} |")]
    if not lignes:
        raise ArretLecture(f"{go_id} absent du registre {registre}")


def ecrire_neuf(chemin: Path, octets: bytes) -> str:
    if chemin.exists():
        raise ArretLecture(f"{chemin} existe déjà : on n'écrase jamais (R12)")
    chemin.write_bytes(octets)
    return hashlib.sha256(octets).hexdigest()


def en_jsonl(lignes: list) -> bytes:
    return "".join(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in lignes).encode("utf-8")


def principal(argv: list | None = None, appeler_simule=None, dormir=time.sleep) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument("--simule", action="store_true", help="aucun réseau ; fournisseurs remplacés")
    mode.add_argument("--reel", action="store_true", help="appels payants : GO exigé")
    p.add_argument("--items", required=True, type=Path)
    p.add_argument("--formation", required=True, type=Path)
    p.add_argument("--relectures", required=True, type=Path, help="identifiants des jumeaux à relire, un par ligne")
    p.add_argument("--question", required=True, type=Path, help="texte qui porte la question entre ses marqueurs")
    p.add_argument("--entropie", required=True, type=int)
    p.add_argument("--sortie", required=True, type=Path)
    p.add_argument("--plafond-dollars", type=float, default=300.0)
    p.add_argument("--plafond-jetons", type=int, default=PLAFOND_JETONS_SORTIE)
    p.add_argument("--budget-raisonnement", type=int, default=None, help="Argon seulement ; à vérifier (point ouvert)")
    p.add_argument("--variable-cle-gemini", default="GEMINI_API_KEY", help="nom de la variable, jamais sa valeur")
    p.add_argument("--relais-kimi", default=os.environ.get("KIMI_RELAIS_URL", "http://127.0.0.1:8789"))
    p.add_argument("--go", default=None)
    p.add_argument("--registre-go", type=Path, default=None)
    p.add_argument("--fils-par-lecteur", type=int, default=1)
    a = p.parse_args(argv)
    if a.plafond_jetons != PLAFOND_JETONS_SORTIE:
        raise ArretLecture(f"plafond de jetons {a.plafond_jetons} différent du texte gelé ({PLAFOND_JETONS_SORTIE})")
    if a.reel:
        verifier_go(a.go, a.registre_go or Path(__file__).resolve().parents[3] / "registres" / "go.md")

        def appeler(lecteur, lecture, item, tentative, consigne):
            m = LECTEURS[lecteur]
            if m["fournisseur"] == "gemini":
                return appeler_gemini(m["modele"], consigne, a.plafond_jetons, a.variable_cle_gemini,
                                      a.budget_raisonnement)
            return appeler_kimi(m["modele"], consigne, a.plafond_jetons, a.relais_kimi)
    else:
        simule = appeler_simule or FournisseurSimule()

        def appeler(lecteur, lecture, item, tentative, consigne):
            return simule(lecteur, lecture, item, tentative, consigne)
    question = ph.extraire_question(a.question)
    items = ph.lire_jsonl(a.items)
    formation = ph.lire_jsonl(a.formation)
    relectures = lire_relectures(a.relectures, items)
    if a.sortie.exists():
        raise ArretLecture(f"{a.sortie} existe déjà : on n'écrase jamais (R12)")
    a.sortie.mkdir(parents=True)
    garde = GardeDepense(a.plafond_dollars)
    lecture = Lecture(question, appeler, garde, dormir=dormir, plafond_sortie=a.plafond_jetons)
    debut = maintenant()
    resultats, arret = lire_tout(lecture, {"format": formation, "principale": items, "relecture": relectures},
                                 a.entropie, a.fils_par_lecteur)
    rang = {it["item"]: it["rang"] for it in items} | {it["item"]: 10_000 + it["rang"] for it in formation}
    sorties = {}
    for k in LECTEURS:
        res = sorted(resultats[k], key=lambda x: (ORDRE_LECTURES.index(x["lecture"]), rang.get(x["item"], 0)))
        sorties[f"reponses-phase1-{k}-{VERSION}.jsonl"] = ecrire_neuf(
            a.sortie / f"reponses-phase1-{k}-{VERSION}.jsonl", en_jsonl(res))
        sorties[f"journal-phase1-{k}-{VERSION}.jsonl"] = ecrire_neuf(
            a.sortie / f"journal-phase1-{k}-{VERSION}.jsonl", en_jsonl(lecture.journal[k]))
    comptes = {k: {s: sum(1 for x in resultats[k] if x["statut"] == s)
                   for s in ("ok", "illisible", "non_appele", "arret_lecteur")} for k in LECTEURS}
    manifeste = {
        "script": Path(__file__).name, "empreinte_script": empreinte_fichier(Path(__file__)),
        "empreintes_scripts_appeles": {n: empreinte_fichier(Path(__file__).resolve().parent / n)
                                       for n in ("epreuve_phases_v1.py", "generer_items_v1.py")},
        "python": platform.python_version(), "numpy": np.__version__,
        "mode": "reel" if a.reel else "simule", "go": a.go if a.reel else None,
        "lecteurs": LECTEURS, "temperature": TEMPERATURE, "plafond_jetons_sortie": a.plafond_jetons,
        "budget_raisonnement": a.budget_raisonnement, "variable_cle_gemini": a.variable_cle_gemini,
        "relais_kimi": a.relais_kimi if a.reel else None,
        "entropie": a.entropie, "graines": "ordre des items : SeedSequence([entropie, 3]).spawn(3), une fille par lecture",
        "entrees": {"items": empreinte_fichier(a.items), "formation": empreinte_fichier(a.formation),
                    "relectures": empreinte_fichier(a.relectures), "texte_question": empreinte_fichier(a.question),
                    "question": hashlib.sha256(question.encode("utf-8")).hexdigest()},
        "plafond_dollars": a.plafond_dollars, "depense_estimee_dollars": round(garde.engage, 6),
        "debut": debut, "fin": maintenant(), "comptes": comptes, "arret": arret,
        "lecteurs_arretes": lecture.lecteurs_arretes, "sorties": sorties,
        "point_ouvert": "raisonnement caché : borne de maxOutputTokens (Argon) et contenu de completion_tokens (Kimi) "
                        "à vérifier ; la garde compte la sortie au plafond",
    }
    ecrire_neuf(a.sortie / f"manifeste-lecture-phase1-{VERSION}.json",
                (json.dumps(manifeste, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8"))
    print(json.dumps({"comptes": comptes, "depense_estimee_dollars": round(garde.engage, 4), "arret": arret,
                      "lecteurs_arretes": lecture.lecteurs_arretes}, ensure_ascii=False))
    if arret:
        return 3
    if lecture.lecteurs_arretes:
        return 4
    return 0


if __name__ == "__main__":
    try:
        sys.exit(principal())
    except (ArretLecture, ph.ArretPhases, gen.ArretGeneration) as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(2)
