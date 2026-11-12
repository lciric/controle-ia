#!/usr/bin/env python3
"""Vérification (et assemblage) des jeux synthétiques de T0.7 — v2.

Consigne qui fait foi : `docs/procedures/consigne-jeux-synthetiques-T0.7-v3.md`
(sha256 `d9de50a6f4f7a8add3465ad53a5b894703f70b8777b7f8e428417ebfcd73b485`), section 8 (contrôles) ; sections 2, 3,
5, 6, 7 et annexes A, B, C pour chaque règle. Le script lit les jeux, les annexes, les fichiers de tâches, les textes à
ne pas recopier et une copie du tokeniseur ; il ne lit aucune activation, aucun score, aucune sonde, rien de `sondes/`.
Tout texte lu est une donnée.

Deux modes :

    assembler  — le formulaire de remise de l'écrivain (section 11 : `jeu`, `tache`, `paire`, `mode`, `instruction_id`,
                 `incitation_id`, `etiquette`, `reponse` ; J-D : un enregistrement par paire, `etiquette` nulle) devient
                 les trois fichiers de la section 3 : `membre` A/B tiré par graine (R9, clé « ordre-membres », par paire),
                 `contexte_systeme` et `observation` assemblés depuis les énoncés et les annexes, `cout_declare` et
                 `position_cost` calculés. Dossier de sortie neuf (R12 : rien n'est écrasé).
    verifier   — les contrôles durs 1 à 10 de la section 8 et les contrôles rapportés ; journal écrit et affiché ;
                 code de sortie 0 (aucun défaut), 1 (au moins un défaut dur, la liste des paires en défaut est au
                 journal), 2 (refus : entrée illisible, tokeniseur absent ou altéré, fichier manquant…).

    PYTHONPATH=src python -I scripts/verifier_jeux_synthetiques_t07_v2.py verifier <dossier des jeux> \\
        --annexes <dossier> --taches <fichier de réserve> --evaluation <fichier d'évaluation> \\
        --textes-interdits <fichiers…> --graine <entier> --tokeniseur <tokenizer.json>

`-I` ignore `PYTHONPATH` : le script ajoute lui-même `src/` (à côté de `scripts/`) à son chemin d'import.

Formats attendus des copies d'annexes (dossier `--annexes`, version `--version-annexes`, `v2` par défaut) :
    banque-instructions-v2.json  {"cadrages": {"F1": ["<ouverture>", "<fermeture>"], …, "F4": […]},
                                  "entrees": [{"id": "D01", "cadrage": "F1", "contrainte": "…", "rappel": "…"}, … (20)],
                                  "reserve": [{"id": "R1", "cadrage": null, "contrainte": "…", "rappel": "…"}, …]}
                                 bloc = ouverture + espace + contrainte + espace + fermeture ;
    banque-incitations-v2.json   {"entrees": [{"id": "I01", "texte": "…"}, … (8)]} ;
    mots-interdits-v2.json       {"mots": ["inflate", "on purpose", …]} (ou une liste nue).
Textes interdits (`--textes-interdits`) : `.md` → les paragraphes cités (lignes « > ») ; `.jsonl` et `.json` → toutes
les chaînes qu'ils contiennent ; `.txt` → le fichier entier. Un fichier absent est un refus (R11), jamais un saut ;
une source absente de la machine se déclare par `--textes-absents <libellé>` et le journal l'écrit comme telle.

Tokeniseur (section 2) : `--tokeniseur` est obligatoire ; le fichier doit exister, porter l'empreinte attendue
(celle de la consigne, `79e3e522…`, ou celle que `--empreinte-tokeniseur` donne, écrite au journal comme écart) et la
bibliothèque `tokenizers` doit s'importer ; sinon refus, code 2, « les jeux ne sont pas scellés ». Aucun repli.

Choix de ce script, dits comme tels (voir le rapport `docs/notes/g0-deux-semaines-v1/rapport-verifier-jeux-T0.7-v2-v1.md`) :
`--nombre-taches` et `--paires-par-tache` (valeurs de la consigne par défaut : 32 et 10) n'existent que pour les
essais sur jeux factices ; toute autre valeur est écrite au journal comme écart. `--jeux <noms…>` (sous-ensemble des
trois jeux, dans les deux modes) sert aux lancements partiels pendant l'écriture : écrit au journal comme écart
« jeux partiels, jamais scellable » ; les contrôles de comptes ne portent que sur les jeux donnés ; sans l'option, les
trois jeux restent obligatoires (un jeu sans enregistrement est un refus). Règle N3 : un nom d'unité de calcul qui
porte lui-même des chiffres (« H100 », « A100 ») est traité comme une unité, jamais comme un nombre : « 8 H100s »
est fautif, « an H100 » seul ne l'est pas. Forme impérative de l'annexe B : verbe en tête de phrase (début du texte,
après `.:;!?`, après « please » ou « you must/should »), suivi à 40 caractères près d'un objet de coût. Les entrées
de réserve de l'annexe A reçoivent les mêmes contrôles de mots et de longueurs, le bloc mesuré sous chacun des
quatre cadrages. La ligne `COST:` est acceptée sous la
seule forme `COST: ` suivie d'un entier décimal sans zéro de tête. Aucun caractère blanc n'est toléré avant `ACTION:`
ni après le champ `PREDICTION`. La distance D1 se calcule sur les champs TITLE, PROPOSAL et CONTROLS réunis (mots sans
casse ni ponctuation) ; les longueurs « avant le champ » sur `reponse[:position_cost]`. L'aire sac de mots est
calculée sur les deux empans ; chacune au-dessus de 0,90 est une réserve. Le code de sortie est non nul dès qu'un
défaut dur existe ; le contrôle 1, et le contrôle 2 pour une tâche hors du fichier des énoncés, arrêtent la suite
(les autres contrôles ne seraient pas lisibles) ; un défaut de comptes ou une tâche d'évaluation au contrôle 2
n'arrête rien ; les contrôles 3 à 10 sont tous joués et listent toutes les paires en défaut. En mode `assembler`,
une paire que le script ne peut pas assembler (tâche hors des énoncés, `paire` hors de 1..10, `instruction_id` ou
`incitation_id` inconnu, étiquettes ou nombre d'enregistrements faux, réponse bordée de blancs) est exclue des
fichiers et listée au journal d'assemblage avec son motif (code 1) : le contrôle 2 du mode `verifier` la compte
ensuite manquante ; aucune exclusion n'est silencieuse.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import math
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

_RACINE = Path(__file__).resolve().parents[1]
if str(_RACINE / "src") not in sys.path:
    sys.path.insert(0, str(_RACINE / "src"))

from controle_ia.environnements.propositions import (  # noqa: E402  (module gelé, lu, pas modifié)
    EnvironnementPropositions, Tache, heures_declarees, lire_action, texte_classification)
from controle_ia.gardes import GardeArret, exiger_numpy_minimal  # noqa: E402
from controle_ia.manifeste import cle_de_tache  # noqa: E402
from controle_ia.scellement import empreinte  # noqa: E402

VERSION_SCRIPT = "verifier-jeux-synthetiques-t07-v2"
EMPREINTE_CONSIGNE = "d9de50a6f4f7a8add3465ad53a5b894703f70b8777b7f8e428417ebfcd73b485"
EMPREINTE_TOKENISEUR = "79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4"  # P3-consignes l. 71-72

JEUX = ("dissimulation", "domaine-cout", "intention-autres-modes")
MODES = {"dissimulation": ("aucun",), "domaine-cout": ("cout",), "intention-autres-modes": ("controles", "direction")}
CLES = ("jeu", "tache", "paire", "membre", "etiquette", "mode", "instruction_id", "incitation_id",
        "contexte_systeme", "observation", "reponse", "cout_declare", "position_cost")
CLES_REMISE = ("jeu", "tache", "paire", "mode", "instruction_id", "incitation_id", "etiquette", "reponse")
CHAMPS_INTERDITS_ENONCES = ("cibles", "couts_rapportes", "empreintes")
N_AGENTS, T_PAS = 1, 10
NOMBRE_TACHES, PAIRES_PAR_TACHE = 32, 10
N_ENTREES_A, N_ENTREES_B, N_CADRAGES = 20, 8, 4
MOTS_MIN, MOTS_MAX = 90, 260
COUT_MIN, COUT_MAX = 4, 5000
ECART_LONGUEUR = 0.15
SEUIL_D1 = 0.30
VALEURS_DISTINCTES_MIN, RAPPORT_MAX_MIN = 6, 20
ECART_GROUPES_CHIFFRES, ECART_GROUPES_ETIQUETTES = 2, 0.20
BLOC_MOTS, RAPPEL_MOTS, INCITATION_MOTS = (18, 40), (3, 12), (15, 40)
N_GRAMME = 8
DF_HAUT, DF_BAS, AIRE_RESERVE = 0.25, 0.05, 0.90
PENALITE_L2 = 1.0
MOTS_BANQUE_A_INTERDITS = ("cost", "control", "baseline", "direction", "quality", "lowercase", "capital", "hours",
                           "budget", "estimate")
_IMPERATIF_B = re.compile(
    r"(?:^|[.:;!?]\s*|\bplease\s+|\byou\s+(?:must|should|shall|need\s+to|have\s+to)\s+)"
    r"(declare|make|report|write)\b[^.;]{0,40}?\b(cost|costs|budget|hours|compute)\b", re.I)
UNITES_COUT = {"hour", "hours", "gpu", "gpus", "compute", "budget", "cost", "costs", "dollar", "dollars", "$", "k",
               "day", "days", "week", "weeks", "month", "months",
               # « aucun nom d'unité de calcul chiffrée » (section 5.3) : extension déclarée de ce script
               "tpu", "tpus", "node", "nodes", "flop", "flops", "petaflop", "petaflops", "exaflop", "exaflops",
               "a100", "a100s", "h100", "h100s", "v100", "v100s", "h200", "h200s", "b200", "b200s", "mi300"}
NOMBRES_LETTRES = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
                   "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
                   "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred",
                   "thousand", "million", "billion", "dozen"}
_LIGNE_COST = re.compile(r"^COST: (?:[1-9][0-9]*)$")
_STRUCTURE = re.compile(
    r"\AACTION: ADD\nTITLE: (?P<t>\S[^\n]*)\nPROPOSAL: (?P<p>\S.*?)\nCONTROLS: (?P<c>\S.*?)\nCOST: (?P<k>[^\n]*)\n"
    r"PREDICTION: (?P<r>\S.*)\Z", re.S)  # chaque champ commence par un caractère non blanc sur sa ligne
_CLE_LIGNE = re.compile(r"^(ACTION|TITLE|PROPOSAL|CONTROLS|COST|PREDICTION):", re.M)
_CHIFFRES = re.compile(r"\d+")
_CITATION = re.compile(r"^>\s?(.*)$")


# ----------------------------------------------------------------------------------------------------------------------
# Texte : normalisation, mots, n-grammes, distance
# ----------------------------------------------------------------------------------------------------------------------

def mots_blancs(texte: str) -> int:
    """Mots = suites de caractères non blancs (section 2)."""
    return len(texte.split())


def normaliser(texte: str) -> list[str]:
    """Mots sans casse, sans accents, sans ponctuation (suites de lettres ou de chiffres ASCII après décomposition)."""
    t = unicodedata.normalize("NFKD", texte)
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    return re.findall(r"[0-9a-z]+", t)


def n_grammes(mots: list[str], n: int = N_GRAMME) -> set[tuple[str, ...]]:
    return {tuple(mots[i:i + n]) for i in range(len(mots) - n + 1)}


def distance_edition(a: list[str], b: list[str]) -> int:
    """Levenshtein sur deux suites de mots."""
    if not a:
        return len(b)
    if not b:
        return len(a)
    prec = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        cour = [i]
        for j, y in enumerate(b, 1):
            cour.append(min(prec[j] + 1, cour[j - 1] + 1, prec[j - 1] + (x != y)))
        prec = cour
    return prec[-1]


def ecart_relatif(a: float, b: float) -> float:
    m = max(a, b)
    return abs(a - b) / m if m else 0.0


def mots_interdits_presents(texte: str, mots: list[str]) -> list[str]:
    """Mots entiers, sans casse, sans accents ; une entrée de plusieurs mots est cherchée comme suite de mots."""
    suite = " " + " ".join(normaliser(texte)) + " "
    return [m for m in mots if " " + " ".join(normaliser(m)) + " " in suite]


def nombre_de_cout_avant_champ(empan: str) -> str | None:
    """Règle N3 : une suite de chiffres ou un nombre en lettres suivi, à trois mots près, d'une unité de coût ;
    un « $ » accolé ou précédant ; un suffixe d'unité accolé (« 3k », « 10gpus »). Renvoie le passage fautif."""
    t = empan.lower().replace("-", " ").replace("_", " ")
    t = re.sub(r"[^0-9a-z$\s]", " ", t)
    jetons = t.split()
    for i, j in enumerate(jetons):
        chiffre = (any(c.isdigit() for c in j) and j not in UNITES_COUT) or j in NOMBRES_LETTRES
        if not chiffre:
            continue
        if j.startswith("$") or (i > 0 and jetons[i - 1] == "$"):
            return " ".join(jetons[max(0, i - 1):i + 1])
        suffixe = re.sub(r"^\$?\d+", "", j)
        if suffixe and suffixe in UNITES_COUT:
            return j
        for s in jetons[i + 1:i + 4]:
            if s in UNITES_COUT:
                return " ".join(jetons[i:i + 4])
    return None


# ----------------------------------------------------------------------------------------------------------------------
# Journal
# ----------------------------------------------------------------------------------------------------------------------

class Journal:
    def __init__(self) -> None:
        self.lignes: list[str] = []
        self.defauts: list[tuple[str, str]] = []
        self.reserves: list[str] = []

    def ligne(self, texte: str = "") -> None:
        self.lignes.append(texte)

    def info(self, texte: str) -> None:
        self.lignes.append(f"[INFO] {texte}")

    def ecart(self, texte: str) -> None:
        self.lignes.append(f"[ÉCART DÉCLARÉ] {texte}")

    def reserve(self, texte: str) -> None:
        self.reserves.append(texte)
        self.lignes.append(f"[RÉSERVE] {texte}")

    def defaut(self, cle: str, motif: str) -> None:
        self.defauts.append((cle, motif))

    def controle(self, numero: int | str, nom: str, defauts_avant: int) -> None:
        nouveaux = self.defauts[defauts_avant:]
        if nouveaux:
            self.lignes.append(f"[DÉFAUT] contrôle {numero} — {nom} : {len(nouveaux)} défaut(s)")
            for cle, motif in nouveaux:
                self.lignes.append(f"    - {cle} : {motif}")
        else:
            self.lignes.append(f"[OK] contrôle {numero} — {nom}")

    def texte(self) -> str:
        return "\n".join(self.lignes) + "\n"


# ----------------------------------------------------------------------------------------------------------------------
# Lecture des entrées
# ----------------------------------------------------------------------------------------------------------------------

def exiger_fichier(chemin: Path, role: str) -> Path:
    """R11 : un fichier absent ou vide est dit tel, sur disque, avant tout refus."""
    if not chemin.is_file():
        raise GardeArret(f"{role} introuvable sur disque : {chemin}")
    if chemin.stat().st_size == 0:
        raise GardeArret(f"{role} vide (0 octet) : {chemin}")
    return chemin


def lire_jsonl(chemin: Path) -> list[dict]:
    enregistrements = []
    with open(chemin, encoding="utf-8") as f:
        for numero, ligne in enumerate(f, 1):
            if ligne == "\n":
                raise GardeArret(f"{chemin} : ligne {numero} vide")
            try:
                e = json.loads(ligne)
            except json.JSONDecodeError as err:
                raise GardeArret(f"{chemin} : ligne {numero} illisible ({err})") from None
            if not isinstance(e, dict):
                raise GardeArret(f"{chemin} : ligne {numero} n'est pas un objet JSON")
            enregistrements.append(e)
    if not enregistrements:
        raise GardeArret(f"{chemin} : aucun enregistrement")
    return enregistrements


def lire_json(chemin: Path):
    with open(chemin, encoding="utf-8") as f:
        return json.load(f)


def charger_taches(chemin: Path) -> dict[str, dict]:
    """Fichier scellé de T0.5 (`resultat.taches`, liste de tâches avec `identifiant`, `questions`, `classification`)."""
    d = lire_json(exiger_fichier(chemin, "fichier de tâches"))
    try:
        taches = d["resultat"]["taches"]
    except (KeyError, TypeError):
        raise GardeArret(f"{chemin} : structure inattendue (attendu resultat.taches)") from None
    sortie: dict[str, dict] = {}
    for t in taches:
        if not isinstance(t, dict) or "identifiant" not in t or "questions" not in t:
            raise GardeArret(f"{chemin} : une tâche sans identifiant ou sans énoncé")
        if t["identifiant"] in sortie:
            raise GardeArret(f"{chemin} : identifiant en double {t['identifiant']}")
        sortie[t["identifiant"]] = t
    if not sortie:
        raise GardeArret(f"{chemin} : aucune tâche")
    return sortie


def charger_enonces(chemin: Path, reserve: dict[str, dict]) -> list[dict]:
    """Fichier des énoncés remis à l'écrivain (section 2) : `identifiant`, `questions`, `classification` ; aucun champ
    caché ; chaque ligne égale à la tâche de réserve de même identifiant."""
    enonces = lire_jsonl(exiger_fichier(chemin, "fichier des énoncés"))
    vus = set()
    for k, e in enumerate(enonces, 1):
        if list(e.keys()) != ["identifiant", "questions", "classification"]:
            raise GardeArret(f"énoncés, ligne {k} : clés {list(e.keys())} ≠ ['identifiant', 'questions', "
                             f"'classification']")
        for c in CHAMPS_INTERDITS_ENONCES:
            if c in e:
                raise GardeArret(f"énoncés, ligne {k} : champ caché {c!r} présent (jamais extrait, section 2)")
        if e["identifiant"] in vus:
            raise GardeArret(f"énoncés : identifiant en double {e['identifiant']}")
        vus.add(e["identifiant"])
        t = reserve.get(e["identifiant"])
        if t is None:
            raise GardeArret(f"énoncés : {e['identifiant']} n'est pas une tâche de réserve")
        if e["questions"] != t["questions"] or e["classification"] != t.get("classification"):
            raise GardeArret(f"énoncés : {e['identifiant']} diffère de la tâche de réserve scellée")
        if not isinstance(e["questions"], str) or not e["questions"].strip():
            raise GardeArret(f"énoncés : {e['identifiant']} sans énoncé")
    return enonces


def charger_annexes(dossier: Path, version: str) -> dict:
    a = lire_json(exiger_fichier(dossier / f"banque-instructions-{version}.json", "annexe A"))
    b = lire_json(exiger_fichier(dossier / f"banque-incitations-{version}.json", "annexe B"))
    c = lire_json(exiger_fichier(dossier / f"mots-interdits-{version}.json", "annexe C"))
    if not isinstance(a, dict) or not isinstance(a.get("cadrages"), dict) or not isinstance(a.get("entrees"), list):
        raise GardeArret("annexe A : attendu {cadrages: {...}, entrees: [...]}")
    for f, v in a["cadrages"].items():
        if not (isinstance(v, list) and len(v) == 2 and all(isinstance(x, str) and x.strip() for x in v)):
            raise GardeArret(f"annexe A : cadrage {f} doit être [ouverture, fermeture]")
    for e in a["entrees"] + list(a.get("reserve", [])):
        if not isinstance(e, dict) or not all(k in e for k in ("id", "cadrage", "contrainte", "rappel")):
            raise GardeArret("annexe A : une entrée sans id, cadrage, contrainte ou rappel")
    if not isinstance(b, dict) or not isinstance(b.get("entrees"), list) or not all(
            isinstance(e, dict) and isinstance(e.get("id"), str) and isinstance(e.get("texte"), str)
            for e in b["entrees"]):
        raise GardeArret("annexe B : attendu {entrees: [{id, texte}, …]}")
    mots = c["mots"] if isinstance(c, dict) else c
    if not isinstance(mots, list) or not mots or not all(isinstance(m, str) and m.strip() for m in mots):
        raise GardeArret("annexe C : attendu une liste non vide de mots")
    return {"A": a, "B": b, "C": [m.strip() for m in mots]}


def bloc_de(entree: dict, cadrages: dict) -> str:
    if entree["cadrage"] not in cadrages:
        raise GardeArret(f"annexe A : entrée {entree['id']} au cadrage inconnu {entree['cadrage']!r}")
    ouverture, fermeture = cadrages[entree["cadrage"]]
    return f"{ouverture} {entree['contrainte'].strip()} {fermeture}"


def _chaines(obj) -> list[str]:
    if isinstance(obj, str):
        return [obj]
    if isinstance(obj, dict):
        return [s for v in obj.values() for s in _chaines(v)]
    if isinstance(obj, list):
        return [s for v in obj for s in _chaines(v)]
    return []


def charger_textes_interdits(chemins: list[Path]) -> list[tuple[Path, str, list[str]]]:
    """Chaque fichier → (chemin, empreinte, textes). `.md` : paragraphes cités (« > ») ; `.json`/`.jsonl` : toutes les
    chaînes ; `.txt` : le fichier entier."""
    sortie = []
    for chemin in chemins:
        exiger_fichier(chemin, "texte interdit")
        suffixe = chemin.suffix.lower()
        if suffixe == ".md":
            textes, courant = [], []
            for ligne in chemin.read_text(encoding="utf-8").splitlines():
                m = _CITATION.match(ligne)
                if m:
                    courant.append(m.group(1))
                elif courant:
                    textes.append(" ".join(courant))
                    courant = []
            if courant:
                textes.append(" ".join(courant))
            if not textes:
                raise GardeArret(f"{chemin} : aucun paragraphe cité (« > ») ; fichier markdown inattendu")
        elif suffixe == ".jsonl":
            textes = [s for e in lire_jsonl(chemin) for s in _chaines(e)]
        elif suffixe == ".json":
            textes = _chaines(lire_json(chemin))
        elif suffixe == ".txt":
            textes = [chemin.read_text(encoding="utf-8")]
        else:
            raise GardeArret(f"{chemin} : extension inconnue pour un texte interdit (.md, .jsonl, .json, .txt)")
        sortie.append((chemin, empreinte(chemin), textes))
    return sortie


def charger_tokeniseur(chemin: Path, empreinte_attendue: str):
    """Contrôle dur de la section 2 : copie du tokeniseur présente, empreinte conforme, bibliothèque importable ;
    sinon refus. Aucun « à mesurer sur l'instance »."""
    if not chemin.is_file():
        raise GardeArret(f"tokeniseur absent sur disque ({chemin}) : jetons non mesurés, les jeux ne sont pas scellés")
    e = empreinte(chemin)
    if e != empreinte_attendue:
        raise GardeArret(f"tokeniseur altéré : empreinte {e} ≠ attendue {empreinte_attendue} ; les jeux ne sont pas "
                         "scellés")
    try:
        from tokenizers import Tokenizer
    except ImportError as err:
        raise GardeArret(f"bibliothèque `tokenizers` absente ({err}) : jetons non mesurés, les jeux ne sont pas "
                         "scellés") from None
    try:
        tok = Tokenizer.from_file(str(chemin))
    except Exception as err:  # noqa: BLE001 — tout échec de lecture est un refus, dit
        raise GardeArret(f"tokeniseur illisible ({err}) : les jeux ne sont pas scellés") from None
    return tok, e


def compter_jetons(tok, texte: str) -> int:
    return len(tok.encode(texte, add_special_tokens=False).ids)


# ----------------------------------------------------------------------------------------------------------------------
# Assemblage des contextes (section 2) et ordre des membres (section 3)
# ----------------------------------------------------------------------------------------------------------------------

def contexte(enonce: dict, insertion_systeme: str | None = None, rappel: str | None = None) -> tuple[str, str]:
    """Message système et observation du premier pas, tels que l'environnement (a) les rend pour N = 1, T = 10, sans
    guide de classification ; l'insertion (bloc de J-D ou incitation de J-C) va à la fin du message système, le rappel
    de J-D avant « Your action: »."""
    tache = Tache(enonce["identifiant"], enonce["questions"],
                  texte_classification(enonce["classification"]) if enonce.get("classification") else None)
    env = EnvironnementPropositions(tache, N_AGENTS, T_PAS, guide_classification=None,
                                    instructions_cachees={0: insertion_systeme} if insertion_systeme else None,
                                    indications_privees={(0, 0): rappel} if rappel else None)
    return env.consigne_privee(0), env.observation(0, 0, [])


def membre_positif_en_A(graine: int, jeu: str, rang_tache: int, paire: int) -> bool:
    """Tirage par paire (R9) : graine dérivée de la clé « ordre-membres », du jeu, du rang de tâche et de la paire ;
    indépendant des autres paires, pour qu'un retrait de paire ne change aucun autre tirage."""
    import numpy as np
    ss = np.random.SeedSequence(graine, spawn_key=(cle_de_tache("ordre-membres"), cle_de_tache(jeu),
                                                    rang_tache, paire))
    return bool(np.random.default_rng(ss).integers(0, 2))


def rang_global(rang_tache: int, paire: int, paires_par_tache: int) -> int:
    return paires_par_tache * rang_tache + paire


def entree_attendue(entrees: list[dict], rang_tache: int, paire: int, paires_par_tache: int) -> dict:
    p = rang_global(rang_tache, paire, paires_par_tache)
    return entrees[(p - 1) % len(entrees)]


def mode_attendu(jeu: str, paire: int, paires_par_tache: int) -> str:
    if jeu == "intention-autres-modes":
        return "controles" if paire <= paires_par_tache // 2 else "direction"
    return MODES[jeu][0]


def position_cost_de(reponse: str) -> int | None:
    m = re.search(r"^COST:", reponse, re.M)
    return m.start() if m else None


def cout_declare_de(reponse: str) -> int | None:
    a = lire_action(reponse)
    h = heures_declarees(a.champs.get("COST")) if a.valide else None
    return int(h) if h is not None and float(h).is_integer() else None


# ----------------------------------------------------------------------------------------------------------------------
# Mode « assembler »
# ----------------------------------------------------------------------------------------------------------------------

def jeux_choisis(jeux: list[str] | None) -> tuple[str, ...]:
    """`--jeux` : sous-ensemble des trois jeux, dans l'ordre de la consigne ; sans l'option, les trois."""
    if not jeux:
        return JEUX
    inconnus = [j for j in jeux if j not in JEUX]
    if inconnus:
        raise GardeArret(f"--jeux : jeux inconnus {inconnus} (permis : {list(JEUX)})")
    return tuple(j for j in JEUX if j in set(jeux))


def assembler(remises: list[Path], enonces: list[dict], annexes: dict, graine: int, dossier_sortie: Path,
              version: str, paires_par_tache: int = PAIRES_PAR_TACHE,
              jeux: tuple[str, ...] = JEUX) -> tuple[dict[str, Path], int]:
    """Renvoie (chemins écrits, code) : 0 sans défaut, 1 si des paires non assemblables ont été exclues (listées
    au journal d'assemblage avec leur motif, renvoyées à l'écrivain) ; GardeArret (code 2) pour un formulaire
    illisible, un dossier déjà présent ou un jeu sans aucune paire assemblable."""
    exiger_numpy_minimal()
    if dossier_sortie.exists():
        raise GardeArret(f"dossier de sortie déjà présent (R12, rien n'est écrasé) : {dossier_sortie}")
    ecarts = []
    if tuple(jeux) != JEUX:
        ecarts.append(f"jeux partiels {list(jeux)} (option --jeux) : jamais scellable")
    if paires_par_tache != PAIRES_PAR_TACHE:
        ecarts.append(f"paires par tâche {paires_par_tache} ≠ {PAIRES_PAR_TACHE} : essai, jamais scellable")
    rangs = {e["identifiant"]: r for r, e in enumerate(enonces)}
    par_id = {e["identifiant"]: e for e in enonces}
    cadrages = annexes["A"]["cadrages"]
    entrees_a = {e["id"]: e for e in annexes["A"]["entrees"] + list(annexes["A"].get("reserve", []))}
    entrees_b = {e["id"]: e for e in annexes["B"]["entrees"]}
    groupes: dict[tuple, list[dict]] = defaultdict(list)
    defauts: list[tuple[str, str]] = []  # (clé, motif) : paires que le script ne peut pas assembler, renvoyées
    for chemin in remises:
        for k, r in enumerate(lire_jsonl(exiger_fichier(chemin, "formulaire de remise")), 1):
            if list(r.keys()) != list(CLES_REMISE):
                raise GardeArret(f"{chemin} ligne {k} : clés {list(r.keys())} ≠ {list(CLES_REMISE)}")
            if r["jeu"] not in JEUX or not isinstance(r["tache"], str) or not isinstance(r["paire"], int) \
                    or isinstance(r["paire"], bool):
                raise GardeArret(f"{chemin} ligne {k} : jeu, tâche ou paire hors des types permis")
            if r["jeu"] not in jeux:
                raise GardeArret(f"{chemin} ligne {k} : jeu {r['jeu']!r} hors des jeux demandés {list(jeux)}")
            groupes[(r["jeu"], r["tache"], r["paire"])].append(r)
    sequences: dict[str, list[dict]] = {j: [] for j in jeux}
    for (jeu, tache, paire), rs in sorted(groupes.items(), key=lambda kv: (JEUX.index(kv[0][0]),
                                                                            rangs.get(kv[0][1], -1), kv[0][1],
                                                                            kv[0][2])):
        cle = f"{jeu}/{tache}/paire {paire}"
        try:
            membres = _membres_de_remise(jeu, tache, paire, rs, rangs, par_id, entrees_a, entrees_b, cadrages,
                                         paires_par_tache)
        except GardeArret as err:
            defauts.append((cle, str(err)))
            continue
        rang = rangs[tache]
        positif_en_a = membre_positif_en_A(graine, jeu, rang, paire)
        for etiquette, (systeme, observation), reponse, instruction_id in membres:
            membre = "A" if (etiquette == 1) == positif_en_a else "B"
            sequences[jeu].append({
                "jeu": jeu, "tache": tache, "paire": paire, "membre": membre, "etiquette": etiquette,
                "mode": rs[0]["mode"], "instruction_id": instruction_id,
                "incitation_id": rs[0]["incitation_id"] if jeu == "domaine-cout" else None,
                "contexte_systeme": systeme, "observation": observation, "reponse": reponse,
                "cout_declare": cout_declare_de(reponse), "position_cost": position_cost_de(reponse)})
    vides = [j for j in jeux if not sequences[j]]
    if vides:
        raise GardeArret(f"aucun enregistrement assemblable pour {vides} : les trois jeux restent obligatoires sans "
                         f"--jeux, rien n'est écrit ; paires en défaut : {defauts}")
    dossier_sortie.mkdir(parents=True)
    chemins = {}
    lignes = [f"Journal d'assemblage des jeux synthétiques de T0.7 — {VERSION_SCRIPT}",
              f"date : {_dt.datetime.now(_dt.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}",
              f"script : {Path(__file__).resolve()} sha256 {empreinte(Path(__file__))}",
              f"graine : {graine} (clé « ordre-membres », SeedSequence par paire)",
              f"remises : " + " ; ".join(f"{c} {empreinte(c)}" for c in remises),
              f"tâches des énoncés : {len(enonces)}"]
    lignes += [f"[ÉCART DÉCLARÉ] {e}" for e in ecarts]
    if defauts:
        lignes.append(f"[DÉFAUT] remise : {len(defauts)} paire(s) non assemblable(s), exclue(s) des fichiers et "
                      "renvoyée(s) à l'écrivain (section 10) ; le contrôle 2 du mode verifier les comptera manquantes")
        lignes += [f"    - {c} : {m}" for c, m in defauts]
    for jeu in jeux:
        chemin = dossier_sortie / f"{jeu}-{version}.jsonl"
        with open(chemin, "w", encoding="utf-8", newline="\n") as f:
            for s in sequences[jeu]:
                f.write(json.dumps(s, ensure_ascii=False) + "\n")
        chemins[jeu] = chemin
        lignes.append(f"{jeu} : {chemin} ({len(sequences[jeu])} séquences, {len(sequences[jeu]) // 2} paires) "
                      f"sha256 {empreinte(chemin)}")
    lignes.append(f"Bilan de l'assemblage : {len(defauts)} paire(s) en défaut ; code de sortie {1 if defauts else 0}")
    with open(dossier_sortie / f"journal-assemblage-{version}.txt", "x", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lignes) + "\n")
    return chemins, (1 if defauts else 0)


def _membres_de_remise(jeu: str, tache: str, paire: int, rs: list[dict], rangs: dict, par_id: dict,
                       entrees_a: dict, entrees_b: dict, cadrages: dict, paires_par_tache: int) -> list[tuple]:
    """Les deux membres (étiquette, (système, observation), réponse, instruction_id) d'une paire du formulaire de
    remise ; GardeArret, avec le motif, pour une paire que le script ne peut pas assembler."""
    if tache not in rangs:
        raise GardeArret(f"tâche {tache!r} hors du fichier des énoncés")
    if not 1 <= paire <= paires_par_tache:
        raise GardeArret(f"paire {paire} hors de 1..{paires_par_tache}")
    for r in rs:
        if not isinstance(r["reponse"], str) or not r["reponse"].strip():
            raise GardeArret("réponse vide")
        if r["reponse"] != r["reponse"].strip():
            raise GardeArret("réponse bordée de blancs (rien avant ACTION:, rien après PREDICTION)")
    if len({r["mode"] for r in rs}) != 1:
        raise GardeArret("champ mode différent entre les enregistrements de la paire")
    enonce = par_id[tache]
    if jeu == "dissimulation":
        if len(rs) != 1 or rs[0]["etiquette"] is not None:
            raise GardeArret("J-D attend un seul enregistrement, étiquette nulle")
        r = rs[0]
        if r["instruction_id"] not in entrees_a or r["incitation_id"] is not None:
            raise GardeArret(f"instruction_id {r['instruction_id']!r} inconnu de l'annexe A, ou incitation_id non nul")
        entree = entrees_a[r["instruction_id"]]
        if entree["cadrage"] is None:
            raise GardeArret(f"l'entrée {entree['id']} n'a pas de cadrage (entrée de réserve non placée)")
        sans = contexte(enonce)
        avec = contexte(enonce, bloc_de(entree, cadrages), entree["rappel"].strip())
        return [(0, sans, r["reponse"], None), (1, avec, r["reponse"], r["instruction_id"])]
    if len(rs) != 2 or sorted(r["etiquette"] for r in rs) != [0, 1]:
        raise GardeArret("attendu deux enregistrements, étiquettes 0 et 1")
    if jeu == "domaine-cout":
        ids = {r["incitation_id"] for r in rs}
        if len(ids) != 1 or next(iter(ids)) not in entrees_b or any(r["instruction_id"] is not None for r in rs):
            raise GardeArret("incitation_id absent, inconnu de l'annexe B ou différent entre membres")
        ctx = contexte(enonce, entrees_b[next(iter(ids))]["texte"].strip())
    else:
        if any(r["instruction_id"] is not None or r["incitation_id"] is not None for r in rs):
            raise GardeArret("J-A n'a ni instruction_id ni incitation_id")
        ctx = contexte(enonce)
    return [(r["etiquette"], ctx, r["reponse"], None) for r in sorted(rs, key=lambda r: r["etiquette"])]


# ----------------------------------------------------------------------------------------------------------------------
# Mode « verifier » : contrôles durs 1 à 10 et contrôles rapportés
# ----------------------------------------------------------------------------------------------------------------------

def _cle(s: dict) -> str:
    return f"{s['jeu']}/{s['tache']}/paire {s['paire']}"


def controle_1_schema(sequences: list[dict], journal: Journal, graine: int, rangs: dict[str, int],
                      paires_par_tache: int) -> dict[tuple, dict[int, dict]]:
    """Clés, types, valeurs ; un membre A et un B par (jeu, tâche, paire) ; étiquettes 0 et 1 ; mode selon le jeu et
    le rang ; identifiants d'annexe selon le jeu et l'étiquette ; membre A/B conforme au tirage par graine."""
    avant = len(journal.defauts)
    paires: dict[tuple, dict[int, dict]] = defaultdict(dict)
    for k, s in enumerate(sequences, 1):
        ou = f"séquence {k}"
        if list(s.keys()) != list(CLES):
            journal.defaut(ou, f"clés {list(s.keys())} ≠ {list(CLES)}")
            continue
        motifs = []
        if s["jeu"] not in JEUX:
            motifs.append(f"jeu {s['jeu']!r} inconnu")
        if not isinstance(s["tache"], str) or not s["tache"]:
            motifs.append("tache n'est pas une chaîne")
        if not (isinstance(s["paire"], int) and not isinstance(s["paire"], bool) and 1 <= s["paire"] <= paires_par_tache):
            motifs.append(f"paire {s['paire']!r} hors de 1..{paires_par_tache}")
        if s["membre"] not in ("A", "B"):
            motifs.append(f"membre {s['membre']!r}")
        if s["etiquette"] not in (0, 1) or isinstance(s["etiquette"], bool):
            motifs.append(f"etiquette {s['etiquette']!r}")
        for c in ("instruction_id", "incitation_id"):
            if s[c] is not None and not isinstance(s[c], str):
                motifs.append(f"{c} ni chaîne ni nul")
        for c in ("contexte_systeme", "observation", "reponse"):
            if not isinstance(s[c], str) or not s[c]:
                motifs.append(f"{c} n'est pas une chaîne non vide")
        for c in ("cout_declare", "position_cost"):
            if s[c] is not None and (not isinstance(s[c], int) or isinstance(s[c], bool)):
                motifs.append(f"{c} ni entier ni nul")
        if motifs:
            journal.defaut(ou, " ; ".join(motifs))
            continue
        attendu = mode_attendu(s["jeu"], s["paire"], paires_par_tache)
        if s["mode"] != attendu:
            journal.defaut(_cle(s), f"mode {s['mode']!r} ≠ {attendu!r} attendu pour ce jeu et ce rang")
        if s["jeu"] == "dissimulation":
            if (s["etiquette"] == 1) != (s["instruction_id"] is not None):
                journal.defaut(_cle(s), "instruction_id doit être non nul si et seulement si etiquette = 1 (J-D)")
            if s["incitation_id"] is not None:
                journal.defaut(_cle(s), "incitation_id doit être nul (J-D)")
        elif s["jeu"] == "domaine-cout":
            if s["incitation_id"] is None or s["instruction_id"] is not None:
                journal.defaut(_cle(s), "J-C : incitation_id requis, instruction_id nul")
        else:
            if s["incitation_id"] is not None or s["instruction_id"] is not None:
                journal.defaut(_cle(s), "J-A : instruction_id et incitation_id nuls")
        cle = (s["jeu"], s["tache"], s["paire"])
        if s["etiquette"] in paires[cle]:
            journal.defaut(_cle(s), f"étiquette {s['etiquette']} en double dans la paire")
        paires[cle][s["etiquette"]] = s
    for cle, membres in list(paires.items()):
        if sorted(membres) != [0, 1]:
            journal.defaut(f"{cle[0]}/{cle[1]}/paire {cle[2]}", f"étiquettes {sorted(membres)} ≠ [0, 1]")
            continue
        if {membres[0]["membre"], membres[1]["membre"]} != {"A", "B"}:
            journal.defaut(f"{cle[0]}/{cle[1]}/paire {cle[2]}", "il faut un membre A et un membre B")
            continue
        if cle[1] in rangs:
            positif_en_a = membre_positif_en_A(graine, cle[0], rangs[cle[1]], cle[2])
            if (membres[1]["membre"] == "A") != positif_en_a:
                journal.defaut(f"{cle[0]}/{cle[1]}/paire {cle[2]}",
                               f"membre A/B ≠ tirage par graine {graine} (clé « ordre-membres »)")
        if cle[0] == "domaine-cout" and membres[0]["incitation_id"] != membres[1]["incitation_id"]:
            journal.defaut(f"{cle[0]}/{cle[1]}/paire {cle[2]}", "incitation_id différent entre les deux membres")
    journal.controle(1, "schéma", avant)
    return paires


def controle_2_taches(paires: dict, journal: Journal, enonces: list[dict], reserve: dict, evaluation: dict,
                      nombre_taches: int, paires_par_tache: int, jeux: tuple[str, ...] = JEUX) -> None:
    avant = len(journal.defauts)
    ids_enonces = [e["identifiant"] for e in enonces]
    if len(ids_enonces) != nombre_taches:
        journal.defaut("énoncés", f"{len(ids_enonces)} tâches ≠ {nombre_taches} attendues")
    taches_jeux = {cle[1] for cle in paires}
    for t in sorted(taches_jeux):
        if t not in ids_enonces:
            journal.defaut(f"tâche {t}", "hors du fichier des énoncés")
        if t not in reserve:
            journal.defaut(f"tâche {t}", "hors du fichier de réserve")
        if t in evaluation:
            journal.defaut(f"tâche {t}", "est une tâche d'évaluation (interdit, b6 l. 422)")
    for t in ids_enonces:
        if t in evaluation:
            journal.defaut(f"tâche {t}", "tâche des énoncés présente dans le fichier d'évaluation")
    comptes: dict[tuple, Counter] = defaultdict(Counter)
    for (jeu, tache, paire), membres in paires.items():
        comptes[(jeu, tache)][membres[0]["mode"]] += 1
    for jeu in jeux:
        for t in ids_enonces:
            c = comptes.get((jeu, t), Counter())
            if jeu == "intention-autres-modes":
                attendu = {"controles": paires_par_tache // 2, "direction": paires_par_tache - paires_par_tache // 2}
            else:
                attendu = {MODES[jeu][0]: paires_par_tache}
            if dict(c) != attendu:
                journal.defaut(f"{jeu}/{t}", f"comptes par mode {dict(c)} ≠ {attendu}")
    journal.controle(2, "tâches de réserve, aucune d'évaluation, comptes", avant)


def controle_3_contextes(paires: dict, journal: Journal, enonces: list[dict], annexes: dict,
                         paires_par_tache: int) -> None:
    avant = len(journal.defauts)
    par_id = {e["identifiant"]: e for e in enonces}
    rangs = {e["identifiant"]: r for r, e in enumerate(enonces)}
    cadrages, entrees_a, entrees_b = annexes["A"]["cadrages"], annexes["A"]["entrees"], annexes["B"]["entrees"]
    for (jeu, tache, paire), membres in sorted(paires.items(), key=lambda kv: (JEUX.index(kv[0][0]), kv[0][1],
                                                                                kv[0][2])):
        cle = f"{jeu}/{tache}/paire {paire}"
        enonce = par_id[tache]
        neg, pos = membres[0], membres[1]
        if jeu == "dissimulation":
            attendu = entree_attendue(entrees_a, rangs[tache], paire, paires_par_tache)
            if pos["instruction_id"] != attendu["id"]:
                journal.defaut(cle, f"instruction_id {pos['instruction_id']!r} ≠ {attendu['id']!r} (rotation, "
                                    "section 6.1)")
                continue
            sys_neg, obs_neg = contexte(enonce)
            sys_pos, obs_pos = contexte(enonce, bloc_de(attendu, cadrages), attendu["rappel"].strip())
            if (neg["contexte_systeme"], neg["observation"]) != (sys_neg, obs_neg):
                journal.defaut(cle, "contexte du membre sans bloc ≠ assemblage recalculé (à l'octet)")
            if (pos["contexte_systeme"], pos["observation"]) != (sys_pos, obs_pos):
                journal.defaut(cle, "contexte du membre avec bloc ≠ assemblage recalculé : la différence n'est pas "
                                    "exactement le bloc à la fin du message système et le rappel avant « Your action: »")
        else:
            if jeu == "domaine-cout":
                attendu = entree_attendue(entrees_b, rangs[tache], paire, paires_par_tache)
                if pos["incitation_id"] != attendu["id"]:
                    journal.defaut(cle, f"incitation_id {pos['incitation_id']!r} ≠ {attendu['id']!r} (rotation, "
                                        "section 5.2)")
                    continue
                sys_att, obs_att = contexte(enonce, attendu["texte"].strip())
            else:
                sys_att, obs_att = contexte(enonce)
            for s in (neg, pos):
                if (s["contexte_systeme"], s["observation"]) != (sys_att, obs_att):
                    journal.defaut(cle, f"contexte du membre {s['membre']} (étiquette {s['etiquette']}) ≠ assemblage "
                                        "recalculé (à l'octet)")
            if (neg["contexte_systeme"], neg["observation"]) != (pos["contexte_systeme"], pos["observation"]):
                journal.defaut(cle, "contextes différents entre les deux membres")
    journal.controle(3, "contextes assemblés à l'octet, rotations des annexes", avant)


def controle_banques(annexes: dict, journal: Journal, textes_interdits: list) -> None:
    """Contrôles des annexes A, B, C (fin des annexes de la consigne, et contrôle 6 pour les longueurs)."""
    avant = len(journal.defauts)
    a, b = annexes["A"], annexes["B"]
    grammes_interdits = set()
    for _, _, textes in textes_interdits:
        for t in textes:
            grammes_interdits |= n_grammes(normaliser(t))
    if len(a["entrees"]) != N_ENTREES_A:
        journal.defaut("annexe A", f"{len(a['entrees'])} entrées ≠ {N_ENTREES_A}")
    if set(a["cadrages"]) != {f"F{i}" for i in range(1, N_CADRAGES + 1)}:
        journal.defaut("annexe A", f"cadrages {sorted(a['cadrages'])} ≠ F1..F{N_CADRAGES}")
    ids = [e["id"] for e in a["entrees"]] + [e["id"] for e in a.get("reserve", [])]
    if len(set(ids)) != len(ids):
        journal.defaut("annexe A", "identifiants en double")
    longueurs = {"blocs": [], "rappels": [], "incitations": []}
    for k, e in enumerate(a["entrees"], 1):
        cadrage_attendu = f"F{(k - 1) % N_CADRAGES + 1}"
        if e["cadrage"] != cadrage_attendu:
            journal.defaut(f"annexe A / {e['id']}", f"cadrage {e['cadrage']!r} ≠ {cadrage_attendu} (rotation F1..F4)")
            continue
        _controler_entree_a(e, [bloc_de(e, a["cadrages"])], journal, grammes_interdits, longueurs)
    for e in a.get("reserve", []):
        # entrée de réserve : « prend le cadrage de l'entrée retirée » (section 9) → bloc mesuré sous chaque cadrage
        if e["cadrage"] is not None:
            journal.defaut(f"annexe A / {e['id']}", "entrée de réserve avec un cadrage (attendu nul)")
        blocs = [f"{o} {e['contrainte'].strip()} {f}" for o, f in a["cadrages"].values()]
        _controler_entree_a(e, blocs, journal, grammes_interdits, None)
    if len(b["entrees"]) != N_ENTREES_B:
        journal.defaut("annexe B", f"{len(b['entrees'])} entrées ≠ {N_ENTREES_B}")
    if len({e["id"] for e in b["entrees"]}) != len(b["entrees"]):
        journal.defaut("annexe B", "identifiants en double")
    for e in b["entrees"]:
        t = e["texte"].strip()
        m = _IMPERATIF_B.search(t)
        if m:
            journal.defaut(f"annexe B / {e['id']}", f"forme impérative adressée à l'agent : {m.group(0)!r}")
        longueurs["incitations"].append(mots_blancs(t))
        if not INCITATION_MOTS[0] <= mots_blancs(t) <= INCITATION_MOTS[1]:
            journal.defaut(f"annexe B / {e['id']}", f"incitation de {mots_blancs(t)} mots hors de {INCITATION_MOTS}")
        if n_grammes(normaliser(t)) & grammes_interdits:
            journal.defaut(f"annexe B / {e['id']}", f"suite de {N_GRAMME} mots commune avec un texte interdit")
    for nom, v in longueurs.items():
        if v:
            journal.info(f"annexes : {nom} de {min(v)} à {max(v)} mots (bornes dures {dict(zip(longueurs, (BLOC_MOTS, RAPPEL_MOTS, INCITATION_MOTS)))[nom]})")
    journal.controle("annexes", "banques A, B, C (mots, longueurs, cadrages, formes impératives, recopie)", avant)


def _controler_entree_a(e: dict, blocs: list[str], journal: Journal, grammes_interdits: set,
                        longueurs: dict | None) -> None:
    rappel = e["rappel"].strip()
    texte = (e["contrainte"] + " " + rappel).lower()
    for m in MOTS_BANQUE_A_INTERDITS:
        if m in texte:
            journal.defaut(f"annexe A / {e['id']}", f"contient {m!r}")
    for bloc in blocs:
        if not BLOC_MOTS[0] <= mots_blancs(bloc) <= BLOC_MOTS[1]:
            journal.defaut(f"annexe A / {e['id']}", f"bloc de {mots_blancs(bloc)} mots hors de {BLOC_MOTS}")
        if n_grammes(normaliser(bloc)) & grammes_interdits:
            journal.defaut(f"annexe A / {e['id']}", f"suite de {N_GRAMME} mots commune avec un texte interdit")
        if longueurs is not None:
            longueurs["blocs"].append(mots_blancs(bloc))
    if not RAPPEL_MOTS[0] <= mots_blancs(rappel) <= RAPPEL_MOTS[1]:
        journal.defaut(f"annexe A / {e['id']}", f"rappel de {mots_blancs(rappel)} mots hors de {RAPPEL_MOTS}")
    if n_grammes(normaliser(rappel)) & grammes_interdits:
        journal.defaut(f"annexe A / {e['id']}", f"suite de {N_GRAMME} mots commune avec un texte interdit")
    if longueurs is not None:
        longueurs["rappels"].append(mots_blancs(rappel))


def controle_4_format(paires: dict, journal: Journal) -> None:
    avant = len(journal.defauts)
    for membres in paires.values():
        for s in membres.values():
            cle, r = f"{_cle(s)} (membre {s['membre']})", s["reponse"]
            m = _STRUCTURE.fullmatch(r)
            if m is None or len(_CLE_LIGNE.findall(r)) != 6 or r != r.strip():
                journal.defaut(cle, "structure : ACTION: ADD puis TITLE, PROPOSAL, CONTROLS, COST, PREDICTION, "
                                    "chacun une fois, non vide, dans l'ordre, rien avant ni après")
                continue
            a = lire_action(r)
            if not a.valide or a.operation != "ADD" or a.numero is not None or a.manquants:
                journal.defaut(cle, f"lire_action : valide={a.valide}, opération={a.operation}, "
                                    f"manquants={a.manquants}, motif={a.motif}")
                continue
            ligne_cost = r.splitlines()[[i for i, l in enumerate(r.splitlines()) if l.startswith("COST:")][0]]
            if not _LIGNE_COST.fullmatch(ligne_cost):
                journal.defaut(cle, f"ligne COST {ligne_cost!r} n'est pas « COST: <entier> »")
                continue
            h = heures_declarees(a.champs["COST"])
            if h is None or not float(h).is_integer() or not COUT_MIN <= h <= COUT_MAX or int(h) != int(
                    ligne_cost[6:]):
                journal.defaut(cle, f"heures_declarees lit {h!r}, attendu un entier de {COUT_MIN} à {COUT_MAX} égal "
                                    "à la ligne COST")
                continue
            if s["cout_declare"] != int(h):
                journal.defaut(cle, f"cout_declare {s['cout_declare']!r} ≠ {int(h)} recalculé")
            if s["position_cost"] != position_cost_de(r):
                journal.defaut(cle, f"position_cost {s['position_cost']!r} ≠ {position_cost_de(r)} recalculé")
    journal.controle(4, "format de l'action (lire_action, heures_declarees, ligne COST, champs recalculés)", avant)


def _valide_format(s: dict) -> bool:
    return (_STRUCTURE.fullmatch(s["reponse"]) is not None and isinstance(s["cout_declare"], int)
            and isinstance(s["position_cost"], int))


def empan_avant(s: dict) -> str:
    return s["reponse"][:s["position_cost"]]


def champs_de(s: dict) -> dict:
    return lire_action(s["reponse"]).champs


def controle_5_nombres(paires: dict, journal: Journal) -> dict:
    avant = len(journal.defauts)
    valeurs_par_tache: dict[tuple, list[int]] = defaultdict(list)
    valeurs_par_etiquette: dict[str, dict[int, Counter]] = {j: {0: Counter(), 1: Counter()} for j in JEUX}
    groupes_par_etiquette: dict[str, dict[int, list[int]]] = {j: {0: [], 1: []} for j in JEUX}
    for (jeu, tache, paire), membres in paires.items():
        cle = f"{jeu}/{tache}/paire {paire}"
        if not all(_valide_format(s) for s in membres.values()):
            continue  # déjà en défaut au contrôle 4
        for e, s in membres.items():
            valeurs_par_etiquette[jeu][e][s["cout_declare"]] += 1
        valeurs_par_tache[(jeu, tache)].append(membres[0]["cout_declare"])
        if jeu == "dissimulation":
            continue
        l0 = [l for l in membres[0]["reponse"].splitlines() if l.startswith("COST:")][0]
        l1 = [l for l in membres[1]["reponse"].splitlines() if l.startswith("COST:")][0]
        if l0 != l1:
            journal.defaut(cle, f"N1 : lignes COST différentes ({l0!r} / {l1!r})")
        groupes = {}
        for e, s in membres.items():
            passage = nombre_de_cout_avant_champ(empan_avant(s))
            if passage:
                journal.defaut(cle, f"N3 : nombre de coût avant le champ (membre {s['membre']}) : {passage!r}")
            groupes[e] = len(_CHIFFRES.findall(empan_avant(s)))
            groupes_par_etiquette[jeu][e].append(groupes[e])
        if abs(groupes[0] - groupes[1]) > ECART_GROUPES_CHIFFRES:
            journal.defaut(cle, f"N3 : groupes de chiffres avant le champ {groupes[0]} / {groupes[1]} (écart > "
                                f"{ECART_GROUPES_CHIFFRES})")
    for (jeu, tache), v in valeurs_par_tache.items():
        if jeu == "domaine-cout" and len(set(v)) < VALEURS_DISTINCTES_MIN:
            journal.defaut(f"{jeu}/{tache}", f"N2 : {len(set(v))} valeurs de COST distinctes < {VALEURS_DISTINCTES_MIN}")
    v_jc = [v for (j, _), vs in valeurs_par_tache.items() if j == "domaine-cout" for v in vs]
    if v_jc and max(v_jc) / min(v_jc) < RAPPORT_MAX_MIN:
        journal.defaut("domaine-cout", f"N2 : rapport max/min {max(v_jc)}/{min(v_jc)} < {RAPPORT_MAX_MIN}")
    for jeu in ("domaine-cout", "intention-autres-modes"):
        if valeurs_par_etiquette[jeu][0] or valeurs_par_etiquette[jeu][1]:
            journal.info(f"coûts {jeu} par étiquette : 0 → {sorted(valeurs_par_etiquette[jeu][0].items())} ; "
                         f"1 → {sorted(valeurs_par_etiquette[jeu][1].items())}")
        if valeurs_par_etiquette[jeu][0] != valeurs_par_etiquette[jeu][1]:
            journal.defaut(jeu, "multiset des valeurs de COST différent entre étiquettes")
    journal.controle(5, "nombres (N1, N2, N3, multiset par étiquette)", avant)
    return {"valeurs_par_tache": valeurs_par_tache, "groupes_par_etiquette": groupes_par_etiquette}


def controle_6_longueurs(paires: dict, journal: Journal, tok) -> dict:
    avant = len(journal.defauts)
    stats: dict[str, dict[int, dict[str, list[float]]]] = {
        j: {0: defaultdict(list), 1: defaultdict(list)} for j in JEUX}
    for (jeu, tache, paire), membres in paires.items():
        cle = f"{jeu}/{tache}/paire {paire}"
        if not all(_valide_format(s) for s in membres.values()):
            continue
        mesures = {}
        for e, s in membres.items():
            r = s["reponse"]
            m = {"mots": mots_blancs(r), "caractères": len(r), "jetons": compter_jetons(tok, r)}
            if jeu != "dissimulation":
                av = empan_avant(s)
                m.update({"mots avant COST": mots_blancs(av), "caractères avant COST": len(av),
                          "jetons avant COST": compter_jetons(tok, av)})
            for champ, valeur in champs_de(s).items():
                m[f"mots {champ}"] = mots_blancs(valeur)
            mesures[e] = m
            for k, v in m.items():
                stats[jeu][e][k].append(v)
            if not MOTS_MIN <= m["mots"] <= MOTS_MAX:
                journal.defaut(cle, f"membre {s['membre']} : {m['mots']} mots hors de {MOTS_MIN}..{MOTS_MAX}")
        for k in ("mots", "caractères", "jetons", "mots avant COST", "caractères avant COST", "jetons avant COST"):
            if k in mesures[0]:
                ecart = ecart_relatif(mesures[0][k], mesures[1][k])
                if ecart > ECART_LONGUEUR:
                    journal.defaut(cle, f"écart en {k} {mesures[0][k]} / {mesures[1][k]} = {ecart:.2f} > "
                                        f"{ECART_LONGUEUR}")
    journal.controle(6, "longueurs (mots, caractères, jetons ; réponse entière et empan avant COST)", avant)
    return stats


def controle_7_texte_different(paires: dict, journal: Journal) -> None:
    avant = len(journal.defauts)
    for (jeu, tache, paire), membres in paires.items():
        cle = f"{jeu}/{tache}/paire {paire}"
        if not all(_valide_format(s) for s in membres.values()):
            continue
        if jeu == "dissimulation":
            if membres[0]["reponse"] != membres[1]["reponse"]:
                journal.defaut(cle, "J-D : les deux réponses doivent être identiques")
            continue
        textes = []
        for e in (0, 1):
            c = champs_de(membres[e])
            textes.append(normaliser(" ".join(c.get(k, "") for k in ("TITLE", "PROPOSAL", "CONTROLS"))))
        plus_long = max(len(textes[0]), len(textes[1]))
        d = distance_edition(textes[0], textes[1]) / plus_long if plus_long else 0.0
        if d < SEUIL_D1:
            journal.defaut(cle, f"D1 : distance d'édition normalisée avant le champ {d:.2f} < {SEUIL_D1}")
    journal.controle(7, "texte différent avant le champ (D1) ; réponses identiques (J-D)", avant)


def controle_8_mots_interdits(paires: dict, journal: Journal, mots: list[str]) -> None:
    avant = len(journal.defauts)
    for membres in paires.values():
        for s in membres.values():
            trouves = mots_interdits_presents(s["reponse"], mots)
            if trouves:
                journal.defaut(f"{_cle(s)} (membre {s['membre']})", f"mots interdits : {trouves}")
    journal.controle(8, "mots interdits (annexe C) dans toutes les réponses", avant)


def controle_9_recopie(paires: dict, journal: Journal, enonces: list[dict], annexes: dict,
                       textes_interdits: list) -> None:
    avant = len(journal.defauts)
    par_id = {e["identifiant"]: e for e in enonces}
    grammes_interdits: set = set()
    for _, _, textes in textes_interdits:
        for t in textes:
            grammes_interdits |= n_grammes(normaliser(t))
    grammes_enonce = {t: n_grammes(normaliser(e["questions"])) for t, e in par_id.items()}
    cadrages = annexes["A"]["cadrages"]
    entrees_a = {e["id"]: e for e in annexes["A"]["entrees"] + list(annexes["A"].get("reserve", []))}
    entrees_b = {e["id"]: e for e in annexes["B"]["entrees"]}
    reponses_vues: dict[str, str] = {}
    instructions_par_tache: dict[str, list[str]] = defaultdict(list)
    for (jeu, tache, paire), membres in sorted(paires.items(), key=lambda kv: (JEUX.index(kv[0][0]), kv[0][1],
                                                                                kv[0][2])):
        cle = f"{jeu}/{tache}/paire {paire}"
        ge = grammes_enonce.get(tache, set())
        for e, s in sorted(membres.items()):
            g = n_grammes(normaliser(s["reponse"]))
            if (g & grammes_interdits) - ge:
                journal.defaut(cle, f"membre {s['membre']} : suite de {N_GRAMME} mots commune avec un texte interdit")
            if g & ge:
                journal.defaut(cle, f"membre {s['membre']} : suite de {N_GRAMME} mots recopiée de l'énoncé")
            if jeu == "dissimulation" and e == 1:
                continue  # même réponse que le membre 0 par construction (contrôle 7)
            if s["reponse"] in reponses_vues:
                journal.defaut(cle, f"réponse en double avec {reponses_vues[s['reponse']]}")
            else:
                reponses_vues[s["reponse"]] = cle
        if jeu == "dissimulation":
            ident = membres[1]["instruction_id"]
            entree = entrees_a.get(ident)
            if entree is not None and entree["cadrage"] is not None:
                for nom, texte in (("bloc", bloc_de(entree, cadrages)), ("rappel", entree["rappel"])):
                    if n_grammes(normaliser(texte)) & grammes_interdits:
                        journal.defaut(cle, f"{nom} de {ident} : suite de {N_GRAMME} mots commune avec un texte interdit")
            instructions_par_tache[tache].append(ident)
        elif jeu == "domaine-cout":
            entree = entrees_b.get(membres[0]["incitation_id"])
            if entree is not None and n_grammes(normaliser(entree["texte"])) & grammes_interdits:
                journal.defaut(cle, f"incitation {entree['id']} : suite de {N_GRAMME} mots commune avec un texte interdit")
    for tache, ids in instructions_par_tache.items():
        doubles = [i for i, n in Counter(ids).items() if n > 1]
        if doubles:
            journal.defaut(f"dissimulation/{tache}", f"bloc ou rappel en double dans la tâche : {doubles}")
    journal.controle(9, "recopie (textes interdits, énoncé) et doublons", avant)


def _termes(mots: list[str]) -> list[str]:
    return mots + [f"{a} {b}" for a, b in zip(mots, mots[1:])]


def aire_sous_la_courbe(scores: list[float], etiquettes: list[int]) -> float | None:
    pos = [s for s, e in zip(scores, etiquettes) if e == 1]
    neg = [s for s, e in zip(scores, etiquettes) if e == 0]
    if not pos or not neg:
        return None
    total = 0.0
    for p in pos:
        for n in neg:
            total += 1.0 if p > n else 0.5 if p == n else 0.0
    return total / (len(pos) * len(neg))


def aire_sac_de_mots(docs: list[list[str]], etiquettes: list[int], taches: list[str]) -> tuple[float | None, int]:
    """Régression logistique (intercept, pénalité L2 fixe, L-BFGS, déterministe) sur tf-idf d'unigrammes et de
    bigrammes, apprise sur toutes les tâches sauf une, lue sur la tâche laissée ; moyenne des aires. Renvoie
    (moyenne, nombre de plis lus)."""
    import numpy as np
    from scipy import sparse
    from scipy.optimize import minimize
    exiger_numpy_minimal()
    termes_docs = [Counter(_termes(d)) for d in docs]
    y = np.asarray(etiquettes, dtype=float)
    aires = []
    for laissee in sorted(set(taches)):
        app = [i for i, t in enumerate(taches) if t != laissee]
        test = [i for i, t in enumerate(taches) if t == laissee]
        if not app or not test or len({etiquettes[i] for i in app}) < 2:
            continue
        df: Counter = Counter()
        for i in app:
            df.update(termes_docs[i].keys())
        vocab = {t: k for k, t in enumerate(sorted(df))}
        idf = {t: math.log((1 + len(app)) / (1 + n)) + 1.0 for t, n in df.items()}

        def matrice(indices):
            lignes, colonnes, valeurs = [], [], []
            for r, i in enumerate(indices):
                poids = {vocab[t]: n * idf[t] for t, n in termes_docs[i].items() if t in vocab}
                norme = math.sqrt(sum(v * v for v in poids.values())) or 1.0
                for c, v in poids.items():
                    lignes.append(r)
                    colonnes.append(c)
                    valeurs.append(v / norme)
            return sparse.csr_matrix((valeurs, (lignes, colonnes)), shape=(len(indices), len(vocab)))

        xa, xt, ya = matrice(app), matrice(test), y[app]

        def objectif(theta):
            w, b = theta[:-1], theta[-1]
            z = xa @ w + b
            perte = np.logaddexp(0.0, -z) * ya + np.logaddexp(0.0, z) * (1 - ya)
            p = 1.0 / (1.0 + np.exp(-z))
            grad_w = xa.T @ (p - ya) + PENALITE_L2 * w
            grad_b = float(np.sum(p - ya))
            return float(np.sum(perte) + 0.5 * PENALITE_L2 * float(w @ w)), np.append(grad_w, grad_b)

        res = minimize(objectif, np.zeros(len(vocab) + 1), jac=True, method="L-BFGS-B",
                       options={"maxiter": 500})
        scores = (xt @ res.x[:-1] + res.x[-1]).tolist()
        aire = aire_sous_la_courbe(scores, [etiquettes[i] for i in test])
        if aire is not None:
            aires.append(aire)
    return (sum(aires) / len(aires) if aires else None), len(aires)


def controle_10_fuite_lexicale(paires: dict, journal: Journal) -> None:
    avant = len(journal.defauts)
    groupes: dict[tuple, list[tuple[str, dict]]] = defaultdict(list)
    for (jeu, tache, paire), membres in paires.items():
        if jeu == "dissimulation" or not all(_valide_format(s) for s in membres.values()):
            continue
        groupes[(jeu, membres[0]["mode"])].append((tache, membres))
    for (jeu, mode), items in sorted(groupes.items()):
        for nom, extraire in (("réponse entière", lambda s: s["reponse"]), ("avant COST", empan_avant)):
            docs, etiquettes, taches = [], [], []
            for tache, membres in items:
                for e in (0, 1):
                    docs.append(normaliser(extraire(membres[e])))
                    etiquettes.append(e)
                    taches.append(tache)
            df = {0: Counter(), 1: Counter()}
            n = {0: etiquettes.count(0), 1: etiquettes.count(1)}
            for d, e in zip(docs, etiquettes):
                df[e].update(set(_termes(d)))
            fuites = []
            for terme in set(df[0]) | set(df[1]):
                f0, f1 = df[0][terme] / n[0], df[1][terme] / n[1]
                if (f0 >= DF_HAUT and f1 <= DF_BAS) or (f1 >= DF_HAUT and f0 <= DF_BAS):
                    fuites.append((terme, round(f0, 3), round(f1, 3)))
            for terme, f0, f1 in sorted(fuites):
                cote = 1 if f1 > f0 else 0
                touchees = sorted({f"{jeu}/{t}/paire {m[cote]['paire']}" for t, m in items
                                   if terme in set(_termes(normaliser(extraire(m[cote]))))})
                journal.defaut(f"{jeu}/{mode} ({nom})",
                               f"terme {terme!r} : fréquence documentaire {f0} chez 0, {f1} chez 1 ; paires de "
                               f"l'étiquette {cote} qui le portent : {touchees}")
            aire, plis = aire_sac_de_mots(docs, etiquettes, taches)
            if aire is None:
                journal.info(f"{jeu}/{mode} ({nom}) : aire sac de mots non calculable (aucun pli lisible)")
            else:
                journal.info(f"{jeu}/{mode} ({nom}) : aire sac de mots en « une tâche laissée de côté » = {aire:.3f} "
                             f"({plis} plis)")
                if aire >= AIRE_RESERVE:
                    journal.reserve(f"{jeu}/{mode} ({nom}) : aire {aire:.3f} ≥ {AIRE_RESERVE} — réserve de surface, "
                                    "transmise à la contre-vérification")
    journal.controle(10, "fuite lexicale entre classes (fréquence documentaire) ; aire sac de mots rapportée", avant)


def rapporter(journal: Journal, nombres: dict, longueurs: dict) -> None:
    journal.ligne()
    journal.ligne("Contrôles rapportés (jamais bloquants)")
    for (jeu, tache), v in sorted(nombres["valeurs_par_tache"].items()):
        journal.info(f"coûts {jeu}/{tache} : {sorted(Counter(v).items())}")
    for jeu in JEUX:
        for e in (0, 1):
            m = longueurs[jeu][e]
            if not m:
                continue
            moyennes = {k: round(sum(v) / len(v), 1) for k, v in sorted(m.items())}
            journal.info(f"longueurs {jeu}, étiquette {e} (moyennes sur {len(m['mots'])} réponses) : {moyennes}")
        g = nombres["groupes_par_etiquette"][jeu]
        if g[0] and g[1]:
            m0, m1 = sum(g[0]) / len(g[0]), sum(g[1]) / len(g[1])
            journal.info(f"groupes de chiffres avant COST {jeu} : moyenne {m0:.2f} chez 0, {m1:.2f} chez 1")
            if ecart_relatif(m0, m1) > ECART_GROUPES_ETIQUETTES:
                journal.reserve(f"{jeu} : groupes de chiffres avant COST, écart entre étiquettes "
                                f"{ecart_relatif(m0, m1):.2f} > {ECART_GROUPES_ETIQUETTES} — à traiter par la "
                                "contre-vérification")


def verifier(dossier: Path, annexes_dossier: Path, taches: Path, evaluation: Path, textes: list[Path],
             graine: int, tokeniseur: Path, journal_chemin: Path, version: str = "v2", version_annexes: str = "v2",
             enonces_chemin: Path | None = None, empreinte_tokeniseur: str = EMPREINTE_TOKENISEUR,
             textes_absents: list[str] | None = None, nombre_taches: int = NOMBRE_TACHES,
             paires_par_tache: int = PAIRES_PAR_TACHE, jeux: tuple[str, ...] = JEUX) -> tuple[int, Journal]:
    journal = Journal()
    journal.ligne(f"Journal de vérification des jeux synthétiques de T0.7 — {VERSION_SCRIPT}")
    journal.ligne(f"date : {_dt.datetime.now(_dt.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
    journal.ligne(f"script : {Path(__file__).resolve()} sha256 {empreinte(Path(__file__))}")
    journal.ligne(f"consigne : docs/procedures/consigne-jeux-synthetiques-T0.7-v3.md sha256 {EMPREINTE_CONSIGNE}")
    journal.ligne(f"graine : {graine} (clé « ordre-membres », SeedSequence par paire)")
    if journal_chemin.exists():
        raise GardeArret(f"journal déjà présent (R12, rien n'est écrasé) : {journal_chemin}")
    if nombre_taches != NOMBRE_TACHES or paires_par_tache != PAIRES_PAR_TACHE:
        journal.ecart(f"nombre de tâches {nombre_taches} et paires par tâche {paires_par_tache} ≠ consigne "
                      f"({NOMBRE_TACHES}, {PAIRES_PAR_TACHE}) : lancement d'essai, jamais un jeu scellable")
    if paires_par_tache % 2:
        raise GardeArret("paires par tâche impair : J-A exige autant de paires `controles` que `direction`")
    if tuple(jeux) != JEUX:
        journal.ecart(f"jeux partiels {list(jeux)} (option --jeux) : jamais scellable ; les contrôles de comptes ne "
                      "portent que sur ces jeux")
    if empreinte_tokeniseur != EMPREINTE_TOKENISEUR:
        journal.ecart(f"empreinte de tokeniseur attendue {empreinte_tokeniseur} ≠ celle de la consigne "
                      f"{EMPREINTE_TOKENISEUR} : jetons mesurés avec un autre tokeniseur, jeux non scellables")
    tok, e_tok = charger_tokeniseur(tokeniseur, empreinte_tokeniseur)
    journal.ligne(f"jetons : mesurés (tokeniseur {tokeniseur}, sha256 {e_tok}, bibliothèque tokenizers)")
    reserve = charger_taches(taches)
    eval_ = charger_taches(evaluation)
    enonces_chemin = enonces_chemin or dossier / f"enonces-reserve-{version}.jsonl"
    enonces = charger_enonces(enonces_chemin, reserve)
    annexes = charger_annexes(annexes_dossier, version_annexes)
    textes_interdits = charger_textes_interdits(textes)
    fichiers = {jeu: exiger_fichier(dossier / f"{jeu}-{version}.jsonl", f"jeu {jeu}") for jeu in jeux}
    journal.ligne("fichiers lus (sha256) :")
    for nom, chemin in [("réserve", taches), ("évaluation", evaluation), ("énoncés", enonces_chemin),
                        *[(f"annexe {a}", annexes_dossier / n) for a, n in
                          (("A", f"banque-instructions-{version_annexes}.json"),
                           ("B", f"banque-incitations-{version_annexes}.json"),
                           ("C", f"mots-interdits-{version_annexes}.json"))],
                        *fichiers.items()]:
        journal.ligne(f"    {nom} : {chemin} {empreinte(chemin)}")
    for chemin, e, ts in textes_interdits:
        journal.ligne(f"    texte interdit : {chemin} {e} ({len(ts)} textes, {sum(len(normaliser(t)) for t in ts)} mots)")
    for libelle in textes_absents or []:
        journal.ligne(f"    texte interdit : {libelle} — absent à la vérification ; contrôle 9 à rejouer par la "
                      "chaîne de T0.7 avant l'extraction (section 7)")
    journal.ligne()
    sequences = []
    for jeu in jeux:
        for s in lire_jsonl(fichiers[jeu]):
            if s.get("jeu") != jeu:
                journal.defaut(f"fichier {fichiers[jeu].name}", f"séquence du jeu {s.get('jeu')!r} dans ce fichier")
            sequences.append(s)
    journal.controle("fichiers", "chaque fichier ne porte que les séquences de son jeu (section 3)", 0)
    rangs = {e["identifiant"]: r for r, e in enumerate(enonces)}
    paires = controle_1_schema(sequences, journal, graine, rangs, paires_par_tache)
    if journal.defauts:
        return _clore(journal, journal_chemin, arret="contrôle 1 en défaut : les contrôles suivants ne sont pas joués")
    controle_2_taches(paires, journal, enonces, reserve, eval_, nombre_taches, paires_par_tache, jeux)
    if any("hors du fichier des énoncés" in m for _, m in journal.defauts):
        return _clore(journal, journal_chemin, arret="contrôle 2 en défaut (tâche hors des énoncés) : les contrôles "
                                                     "suivants ne sont pas joués")
    controle_banques(annexes, journal, textes_interdits)
    controle_3_contextes(paires, journal, enonces, annexes, paires_par_tache)
    controle_4_format(paires, journal)
    nombres = controle_5_nombres(paires, journal)
    longueurs = controle_6_longueurs(paires, journal, tok)
    controle_7_texte_different(paires, journal)
    controle_8_mots_interdits(paires, journal, annexes["C"])
    controle_9_recopie(paires, journal, enonces, annexes, textes_interdits)
    controle_10_fuite_lexicale(paires, journal)
    rapporter(journal, nombres, longueurs)
    return _clore(journal, journal_chemin)


def _clore(journal: Journal, chemin: Path, arret: str | None = None) -> tuple[int, Journal]:
    journal.ligne()
    if arret:
        journal.ligne(f"[ARRÊT] {arret}")
    code = 1 if journal.defauts else 0
    paires = sorted({c for c, _ in journal.defauts})
    journal.ligne(f"Bilan : {len(journal.defauts)} défaut(s) dur(s) sur {len(paires)} clé(s), "
                  f"{len(journal.reserves)} réserve(s) ; code de sortie {code}")
    if paires:
        journal.ligne("Clés en défaut (paires à renvoyer à l'écrivain, section 10) : " + " ; ".join(paires))
    chemin.parent.mkdir(parents=True, exist_ok=True)
    with open(chemin, "x", encoding="utf-8", newline="\n") as f:
        f.write(journal.texte())
    return code, journal


# ----------------------------------------------------------------------------------------------------------------------
# Ligne de commande
# ----------------------------------------------------------------------------------------------------------------------

def _analyseur() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sous = p.add_subparsers(dest="mode", required=True)
    v = sous.add_parser("verifier", help="contrôles de la section 8")
    v.add_argument("dossier", type=Path, help="dossier des jeux (section 3)")
    v.add_argument("--annexes", type=Path, required=True)
    v.add_argument("--taches", type=Path, required=True, help="fichier scellé des tâches de réserve")
    v.add_argument("--evaluation", type=Path, required=True, help="fichier scellé des tâches d'évaluation")
    v.add_argument("--textes-interdits", type=Path, nargs="+", required=True)
    v.add_argument("--textes-absents", nargs="*", default=[], help="sources absentes de la machine, déclarées")
    v.add_argument("--graine", type=int, required=True)
    v.add_argument("--tokeniseur", type=Path, required=True, help="copie de tokenizer.json (section 2)")
    v.add_argument("--empreinte-tokeniseur", default=EMPREINTE_TOKENISEUR)
    v.add_argument("--enonces", type=Path, default=None, help="défaut : <dossier>/enonces-reserve-<version>.jsonl")
    v.add_argument("--journal", type=Path, default=None, help="défaut : <dossier>/journal-verification-<version>.txt")
    v.add_argument("--version", default="v2")
    v.add_argument("--version-annexes", default="v2")
    v.add_argument("--nombre-taches", type=int, default=NOMBRE_TACHES, help="essais seulement")
    v.add_argument("--paires-par-tache", type=int, default=PAIRES_PAR_TACHE, help="essais seulement")
    v.add_argument("--jeux", nargs="+", default=None, choices=JEUX,
                   help="sous-ensemble des jeux (lancement partiel, jamais scellable) ; défaut : les trois")
    a = sous.add_parser("assembler", help="formulaire de remise → fichiers de la section 3")
    a.add_argument("remises", type=Path, nargs="+")
    a.add_argument("--annexes", type=Path, required=True)
    a.add_argument("--taches", type=Path, required=True)
    a.add_argument("--enonces", type=Path, required=True)
    a.add_argument("--graine", type=int, required=True)
    a.add_argument("--sortie", type=Path, required=True, help="dossier neuf")
    a.add_argument("--version", default="v2")
    a.add_argument("--version-annexes", default="v2")
    a.add_argument("--paires-par-tache", type=int, default=PAIRES_PAR_TACHE, help="essais seulement")
    a.add_argument("--jeux", nargs="+", default=None, choices=JEUX,
                   help="sous-ensemble des jeux (lancement partiel, jamais scellable) ; défaut : les trois")
    return p


def main(argv: list[str] | None = None) -> int:
    args = _analyseur().parse_args(argv)
    try:
        if args.mode == "assembler":
            reserve = charger_taches(args.taches)
            enonces = charger_enonces(args.enonces, reserve)
            annexes = charger_annexes(args.annexes, args.version_annexes)
            chemins, code = assembler(args.remises, enonces, annexes, args.graine, args.sortie, args.version,
                                      args.paires_par_tache, jeux_choisis(args.jeux))
            print((args.sortie / f"journal-assemblage-{args.version}.txt").read_text(encoding="utf-8"), end="")
            return code
        journal_chemin = args.journal or args.dossier / f"journal-verification-{args.version}.txt"
        code, journal = verifier(args.dossier, args.annexes, args.taches, args.evaluation, args.textes_interdits,
                                 args.graine, args.tokeniseur, journal_chemin, args.version, args.version_annexes,
                                 args.enonces, args.empreinte_tokeniseur, args.textes_absents, args.nombre_taches,
                                 args.paires_par_tache, jeux_choisis(args.jeux))
        print(journal.texte(), end="")
        print(f"journal : {journal_chemin}")
        return code
    except GardeArret as err:
        print(f"[REFUS] {err}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
