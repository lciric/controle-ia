#!/usr/bin/env python3
"""Épreuve de l'étiqueteur, lecture exploratoire v2 : lecture des items par trois lecteurs modèles (v5).

Rédacteur : Claude Opus 5.5 (claude-opus-5-5), développeur neuf, 9 novembre 2026. Pièce de l'ordre exploratoire
`docs/procedures/ordre-exploratoire-etiqueteur-v2-brouillon1.md` (sections 3.2 à 3.5, 5 et 6) et de GO-2026-11-09-03.
EXPLORATOIRE, NON OPPOSABLE. La v4 (`lire_items_phase1_v4.py`) reste intacte ; la v5 en importe, sans les changer, le
masquage (`Secrets`, `tronquer_masque`), la garde de dépense (`GardeDepense`), le contrôle du GO, l'analyseur des
arguments, les réglages gelés et les corps des requêtes d'Argon et de Kimi, et l'appel du relais de Kimi
(`relais_kimi_v4.py`, inchangé).

Changements depuis la v4 (et seulement ceux-ci) :
1. Format : les réponses sont contrôlées par l'analyseur commun `format_reponse_v2.analyser_reponse` (champ HARM ; une
   ligne YES sans HARM, format v1, est hors format). La citation n'est pas vérifiée ici (elle l'est à l'analyse). Une
   question sans champ HARM (consigne v1) est refusée avant tout appel.
2. Trois lecteurs : A `gemini-4-argon` et B `kimi-k3.1-pro`, réglages gelés de la v4 ; C `claude-opus-5-5` par le
   paquet officiel `anthropic` 2.6.0 (version exigée en mode réel), réglages de la sonde `sonde_refus_lecteur_c_v1.py` :
   interface Messages sans flux, `max_tokens` 16 000, `output_config={"effort": "high"}`, ni `thinking`, ni température,
   ni message système, aucun repli (`fallbacks`), délai 900 s, `max_retries` 4. Clé par son nom seulement
   (`--variable-cle-claude`, défaut `RR_ANTHROPIC_API_KEY_RIGAUD`) ; barème (4, 20) dollars par million. Modèle servi
   différent : lecteur arrêté ; 401 : arrêt général ; 400, 403, 404, 422 avant toute réponse rendue dans ce lancement :
   lecteur arrêté (après une réponse rendue : statut `erreur` de l'item, sans reprise) ; 402 ou plafond de dépense du
   compte (`EnforcedSpendLimitReachedError`) : lecteur C arrêté. `--lecteurs` : sous-ensemble de A, B, C (défaut les trois).
3. Blocages : une réponse bloquée par le fournisseur est relancée une fois à l'identique ; bloquée encore : statut
   `bloque` (distinct de `illisible`), catégorie écrite. Argon : `promptFeedback.blockReason` (catégorie gardée : cette
   raison), aucun candidat, ou (décision relayée le 9 novembre, R-2005, R-2006) un candidat rendu sans texte dont la
   `finishReason` est SAFETY, PROHIBITED_CONTENT, BLOCKLIST ou SPII (catégorie gardée : cette `finishReason`) ; Claude :
   `stop_reason == "refusal"`, catégorie de `stop_details` gardée.
4. Relectures : la liste peut porter chaque identifiant deux fois ; chaque occurrence est une lecture distincte,
   numérotée par le champ `presentation` (1 ou 2 : rang de l'occurrence dans la liste, non l'ordre de lecture) ; plus de
   deux occurrences ou un identifiant inconnu : arrêt avant tout appel.
5. `--fils-par-lecteur` : 1 ou 2 ; chaque lecteur a son propre groupe de fils.
6. Deux plafonds séparés : `--plafond-hors-credits` (au plus 100 dollars, GO-2026-11-09-03) pour A et B ensemble, au
   barème prudent de la v4 ; `--plafond-claude` (au plus 50 dollars, même GO) pour C. Un lecteur dont le groupe atteint
   son plafond s'arrête ; les autres continuent. `--depense-engagee-hors-credits` et `--depense-engagee-claude` comme la
   `--depense-engagee` de la v4.
7. Sentinelle (R-2005, R-2006) : un lecteur dont les réponses illisibles de la lecture principale (après les demandes
   de format) font **plus de 2 % du nombre réel d'items de la lecture principale** est arrêté (comparaison en entiers :
   100 × illisibles > 2 × items ; pour 493 items, arrêt à la 10e illisible, 10/493 > 0,02 et 9/493 non ; pour 528, à
   la 11e) ; le manifeste le dit. Ni les blocages, ni les erreurs, ni les relectures ne comptent dans cette sentinelle.
8. Relais de Kimi : `--relais-max-appels` (mode réel, lecteur B demandé) couvre cinq tentatives par item lu, comme en v4.
9. Statuts : une erreur de transport persistante est `erreur` (la v4 l'écrivait `illisible`) ; un item dont la lecture
   est interrompue par un arrêt après au moins une tentative est `arret_lecteur` ou `arret_general` (la v4 l'écrivait
   `non_appele`) ; `non_appele` veut dire aucune tentative.
Le reste tel quel : masquage avant toute troncature, essai de format seul puis feu vert exigé (mêmes entrées, mêmes
réglages, même mode, mêmes plafonds, lecteurs de la lecture principale compris dans ceux de l'essai, dépenses engagées
au moins celles de l'essai), formes des options contrôlées sans recopier une valeur reçue, GO vérifié au registre,
manifeste, codes de sortie, écriture au fil des tentatives, rendu à l'écran sans texte de réponse.

Ordre de lecture : celui de la v4, sans changement (décision relayée le 9 novembre) : dans chaque lecture, les
items (format, principale) et les occurrences de la liste des relectures sont lus dans une permutation tirée par
`SeedSequence([entropie, 3]).spawn(3)` (une fille par lecture) ; l'ordre des fichiers d'entrée, celui que le générateur
a tiré compris (rangs, relectures sans présentations voisines), n'est donc pas l'ordre de lecture, et deux
présentations d'un même jumeau peuvent être lues l'une après l'autre (appels sans mémoire).

Tentatives par item : au plus 4 erreurs de transport (attentes 0, 10, 30 et 90 s), 2 demandes de format (une réponse
tronquée en est une) et, pour A et C, 2 demandes après blocage ; soit au plus 5 tentatives pour Kimi (6 pour A et C).

CONTRAT DE SORTIE (pour l'analyse v4). Dossier `--sortie`, neuf ; L parcourt les lecteurs demandés (A, B, C) :
- `reponses-phase1-L-v5.jsonl` : une ligne JSON (clés triées) par lecture d'un item, triées par lecture (format,
  principale, relecture), rang de l'item, présentation. Schéma de la v4 et quatre champs de plus :
    lecteur             « A », « B » ou « C » (identique au L du nom du fichier) ;
    modele_demande      `gemini-4-argon`, `kimi-k3.1-pro` ou `claude-opus-5-5` ;
    lecture             « format », « principale » ou « relecture » ;
    item                identifiant de l'item ;
    presentation        1 ou 2 (1 hors relecture ; en relecture, rang de l'occurrence dans la liste) — nouveau ;
    empreinte_consigne  SHA-256 de la consigne envoyée ;
    temperature_envoyee 0 (A), null (B, C) ; temperature_servie : 0 (A), 1.0 (B), null (C : non rendue) ;
    statut              parmi ok, illisible, bloque, erreur, non_appele, arret_lecteur, arret_general — étendu ;
    categorie_blocage   catégorie rendue par le fournisseur au dernier blocage (Argon : `blockReason`, ou la
                        `finishReason` d'un candidat sans texte ; Claude : `stop_details.category`), null sans blocage
                        ou sans catégorie rendue — nouveau ;
    blocages            nombre de tentatives bloquées pour cet item (0, 1 ou 2) — nouveau ;
    reponse_brute       texte de la dernière réponse rendue, masqué (ok, illisible ; bloque : texte du refus, null
                        s'il est vide) ; null pour les autres statuts — même champ que la v4 ;
    tentatives, jetons_entree, jetons_sortie (pensée comprise), jetons_pensee, cout_estime (dollars, barème du
    lecteur), motif (null pour ok).
  Sens des statuts : ok (réponse au format v2) ; illisible (format faux ou réponse tronquée après 2 demandes) ; bloque
  (bloquée deux fois) ; erreur (transport persistant, rejet HTTP après une réponse rendue, exception imprévue) ;
  non_appele (aucune tentative : lecteur ou lancement déjà arrêté, plafond) ; arret_lecteur (le lecteur s'arrête
  pendant cet item : anomalie, modèle servi, rejet avant toute réponse, plafond, relais plein, crédits) ; arret_general
  (clé refusée pendant cet item, ou arrêt général survenu entre deux de ses tentatives).
- `reponses-phase1-L-v5.encours.jsonl` : les mêmes lignes, écrites dans l'ordre d'achèvement.
- `journal-phase1-L-v5.jsonl` : une ligne par tentative (heures, présentation, jetons, coût, sorte : ok, format_faux,
  tronquee, bloque, erreur, rejet_http, anomalie_lecteur, cle_refusee_ou_absente ; catégorie de blocage ; identifiant
  du message de Claude ; réponse brute masquée pour format_faux, tronquee et bloque).
- `manifeste-lecture-phase1-v5.json` : réglages, entrées, plafonds et dépenses par groupe, comptes par statut et par
  lecteur, blocages, sentinelle, lecteurs arrêtés, empreintes des sorties.

Bibliothèque standard, numpy et, en mode réel avec le lecteur C, le paquet `anthropic` 2.6.0.

Usage :
    python -I -B lire_items_phase1_v5.py --simule --lectures format --items I --formation F --relectures R \
        --question ORDRE.md --entropie N --sortie DOSSIER_FORMAT [--lecteurs A,B,C]
    python -I -B lire_items_phase1_v5.py --simule --lectures principale+relecture --feu-vert-format \
        DOSSIER_FORMAT/manifeste-lecture-phase1-v5.json ... --sortie DOSSIER_PRINCIPAL \
        --depense-engagee-hors-credits D1 --depense-engagee-claude D2 [--fils-par-lecteur 2]
    (mode réel : --reel --go GO-AAAA-MM-JJ-NN --commit COMMIT [--variable-cle-gemini NOM] [--variable-cle-claude NOM]
     [--relais-empreinte E] --relais-max-appels N)
"""

from __future__ import annotations

import dataclasses
import hashlib
import json
import math
import os
import platform
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import epreuve_phases_v1 as ph  # noqa: E402  (scripts du même dossier, intacts)
import format_reponse_v2 as fmt  # noqa: E402  (analyseur commun, obligatoire, intact)
import generer_items_v2 as gen  # noqa: E402  (intact : N_PAS et l'analyse des contrôles du lecteur simulé)
import lire_items_phase1_v4 as lire4  # noqa: E402  (intacte)
from format_reponse_v2 import FormatInvalide, analyser_reponse  # noqa: E402,F401  (réexportés : un seul analyseur)

VERSION = "v5"
ArretLecture = lire4.ArretLecture
ArretDepense = lire4.ArretDepense
ArretGeneral = lire4.ArretGeneral
GardeDepense = lire4.GardeDepense
Secrets = lire4.Secrets
tronquer_masque = lire4.tronquer_masque
cout = lire4.cout
en_ligne = lire4.en_ligne
maintenant = lire4.maintenant
empreinte_fichier = lire4.empreinte_fichier
verifier_go = lire4.verifier_go
Parseur = lire4.Parseur

PLAFONDS_ACCORDES = {"hors_credits": 100.0, "claude": 50.0}  # GO-2026-11-09-03
GROUPES = {"A": "hors_credits", "B": "hors_credits", "C": "claude"}
OPTION_PLAFOND = {"hors_credits": "--plafond-hors-credits", "claude": "--plafond-claude"}
ORDRE_LECTEURS_MODELES = ("A", "B", "C")
LECTEURS = {
    "A": dict(lire4.LECTEURS["A"]),  # gelés en v4 : température 0, sortie 8 000, pensée 8 192, barème prudent (10, 50)
    "B": dict(lire4.LECTEURS["B"]),  # gelés en v4 : aucune température envoyée, effort high, 32 000, barème (2, 10)
    "C": {"modele": "claude-opus-5-5", "fournisseur": "anthropic", "prix": (4.0, 20.0),
          "temperature_envoyee": None, "temperature_servie": None,  # aucune envoyée ; la valeur servie n'est pas rendue
          "plafond_sortie": 16000, "budget_pensee": 0, "effort_raisonnement": "high",
          "interface": "messages, sans flux", "reflexion": "non envoyée (adaptative par défaut)", "systeme": "aucun",
          "replis": "aucun", "delai_s": 900.0, "reprises_paquet": 4, "paquet": "anthropic 2.6.0"},
}
VERSION_PAQUET_ANTHROPIC = "2.6.0"
DELAI_S = LECTEURS["C"]["delai_s"]
REPRISES_PAQUET = LECTEURS["C"]["reprises_paquet"]
REJETS_AVANT_REPONSE = (400, 403, 404, 422)
NOM_VARIABLE = lire4.NOM_VARIABLE
BOUCLE_LOCALE = re.compile(r"http://(127\.0\.0\.1|localhost):\d{1,5}/?")
FORME_LECTEURS = re.compile(r"[ABC](,[ABC]){0,2}")
TENTATIVES_MAX_PAR_ITEM = lire4.TENTATIVES_MAX_PAR_ITEM  # 5 pour Kimi (aucun blocage chez ce fournisseur), comme en v4
CARACTERES_PAR_JETON_PRUDENT = lire4.CARACTERES_PAR_JETON_PRUDENT
ATTENTES_TRANSPORT = lire4.ATTENTES_TRANSPORT
DEMANDES_FORMAT = lire4.DEMANDES_FORMAT
DEMANDES_BLOCAGE = 2  # la demande bloquée et une relance identique
SENTINELLE_POURCENT = 2  # plus de 2 % des items réels de la lecture principale (R-2005, R-2006), en entiers
FINS_BLOCAGE_ARGON = ("SAFETY", "PROHIBITED_CONTENT", "BLOCKLIST", "SPII")  # candidat sans texte : blocage
FILS_PERMIS = (1, 2)
FINS_TRONQUEES = {"MAX_TOKENS", "length", "max_tokens", "model_context_window_exceeded"}
LIGNES_LECTURE = lire4.LIGNES_LECTURE
ORDRE_LECTURES = lire4.ORDRE_LECTURES
CODES = lire4.CODES
STATUTS = ("ok", "illisible", "bloque", "erreur", "non_appele", "arret_lecteur", "arret_general")
CHAMPS_RESULTAT = ("lecteur", "modele_demande", "lecture", "item", "presentation", "empreinte_consigne",
                   "temperature_envoyee", "temperature_servie", "statut", "categorie_blocage", "blocages",
                   "reponse_brute", "tentatives", "jetons_entree", "jetons_sortie", "jetons_pensee", "cout_estime",
                   "motif")
SECRETS_DU_PROCESSUS = None  # rempli par `principal` ; sert au masquage des messages de `__main__`


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
    bloque: bool = False  # v5 : réponse bloquée par le fournisseur
    categorie_blocage: str | None = None
    rejet_http: int | None = None  # v5 : 400, 403, 404 ou 422 rendu par l'interface de Claude


def appeler_gemini(consigne: str, variable_cle: str, secrets: Secrets, ouvrir=None) -> Reponse:
    """Argon : requête de la v4 (corps gelé, même adresse, même délai) ; seul le classement des blocages change."""
    cle = os.environ.get(variable_cle)
    if not cle:
        return Reponse(echec=f"variable {variable_cle} absente", cle_refusee=True)
    secrets.ajouter(cle)
    corps = json.dumps(lire4.corps_gemini(consigne), ensure_ascii=False).encode("utf-8")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{LECTEURS['A']['modele']}:generateContent"
    requete = urllib.request.Request(url, data=corps, method="POST",
                                     headers={"Content-Type": "application/json", "x-goog-api-key": cle})
    ouvrir = ouvrir or (lambda r: urllib.request.urlopen(r, context=lire4._contexte_tls(), timeout=1200))
    try:
        with ouvrir(requete) as r:
            rep = json.load(r)
    except urllib.error.HTTPError as e:
        brut = e.read().decode("utf-8", "replace")
        detail = tronquer_masque(brut, secrets)  # masque AVANT de tronquer
        invalide = e.code == 400 and "API_KEY_INVALID" in brut
        return Reponse(echec=f"HTTP {e.code} : {detail}", reprendre=e.code in (429, 500, 502, 503, 504),
                       cle_refusee=e.code in (401, 403) or invalide)
    except (OSError, ValueError) as e:
        return Reponse(echec=f"connexion : {type(e).__name__} : {tronquer_masque(str(e), secrets)}", reprendre=True)
    u = rep.get("usageMetadata") or {}
    pensee = u.get("thoughtsTokenCount") or 0
    candidats = rep.get("candidates") or []
    base = dict(modele_servi=rep.get("modelVersion"), jetons_entree=u.get("promptTokenCount"),
                jetons_sortie=(u.get("candidatesTokenCount") or 0) + pensee, jetons_pensee=pensee)
    raison = (rep.get("promptFeedback") or {}).get("blockReason")
    raison = None if raison is None else str(raison)
    if not candidats or raison:  # v5 : blocage du fournisseur, relancé une fois
        return Reponse(echec=f"bloquée par le fournisseur ({'aucun candidat' if not candidats else 'candidat présent'}"
                             f", raison {raison or 'non rendue'})", bloque=True, categorie_blocage=raison,
                       fin="AUCUN_CANDIDAT" if not candidats else candidats[0].get("finishReason"), **base)
    c = candidats[0]
    parts = (c.get("content") or {}).get("parts") or []
    texte = "".join(p.get("text", "") for p in parts if not p.get("thought"))
    fin = c.get("finishReason")
    if not texte.strip() and fin in FINS_BLOCAGE_ARGON:  # v5 (R-2005, R-2006) : candidat sans texte, fin de blocage
        return Reponse(echec=f"bloquée par le fournisseur (candidat sans texte, fin {fin})", bloque=True,
                       categorie_blocage=str(fin), texte=texte, fin=fin, **base)
    return Reponse(texte=texte, fin=fin, **base)


def appeler_kimi(consigne: str, url_relais: str, secrets: Secrets, ouvrir=None) -> Reponse:
    """Kimi : l'appel de la v4, inchangé (relais local `relais_kimi_v4.py`) ; seule la classe de la réponse change."""
    return Reponse(**dataclasses.asdict(lire4.appeler_kimi(consigne, url_relais, secrets, ouvrir=ouvrir)))


def classer_message_claude(msg) -> Reponse:
    """Classe un message rendu (HTTP 200) par l'interface Messages. Le texte n'est lu qu'au contrôle de format."""
    texte = "".join(getattr(b, "text", "") or "" for b in (getattr(msg, "content", None) or [])
                    if getattr(b, "type", None) == "text")
    u = getattr(msg, "usage", None)
    entree = getattr(u, "input_tokens", None)
    if entree is not None:  # prudent : toute entrée facturée, cache compris (aucun cache n'est demandé)
        entree += (getattr(u, "cache_creation_input_tokens", None) or 0) + (getattr(u, "cache_read_input_tokens", None) or 0)
    base = dict(texte=texte, modele_servi=getattr(msg, "model", None), jetons_entree=entree,
                jetons_sortie=getattr(u, "output_tokens", None), jetons_pensee=0, fin=getattr(msg, "stop_reason", None),
                detail={"identifiant": getattr(msg, "id", None)})
    if base["fin"] == "refusal":
        d = getattr(msg, "stop_details", None)
        categorie = d.get("category") if isinstance(d, dict) else getattr(d, "category", None)
        return Reponse(echec="bloquée par le fournisseur (refus)", bloque=True,
                       categorie_blocage=None if categorie is None else str(categorie), **base)
    return Reponse(**base)


def fabriquer_appelant_claude(variable_cle: str, secrets: Secrets, base_url: str | None = None):
    """Lecteur C par le paquet officiel ; rend (appeler(consigne) -> Reponse, version du paquet).

    La clé est lue par son nom ; sa valeur n'est jamais écrite ni rendue. Réglages de la sonde, sans écart."""
    valeur = os.environ.get(variable_cle)
    if not valeur:
        raise ArretLecture(f"variable {variable_cle} absente (vérifiée par son nom) : aucun appel")
    secrets.ajouter(valeur)
    try:
        import anthropic  # importé seulement quand le lecteur C est demandé en mode réel (ou par un essai)
    except ImportError:
        raise ArretLecture(f"paquet anthropic absent : installer la version {VERSION_PAQUET_ANTHROPIC}") from None
    options = {"api_key": valeur, "max_retries": REPRISES_PAQUET, "timeout": DELAI_S}
    if base_url:
        options["base_url"] = base_url
    client = anthropic.Anthropic(**options)
    m = LECTEURS["C"]

    def court(e) -> str:
        return tronquer_masque(f"{type(e).__name__} : {e}", secrets)  # masque AVANT de tronquer

    def appeler(consigne: str) -> Reponse:
        try:
            msg = client.messages.create(model=m["modele"], max_tokens=m["plafond_sortie"],
                                         output_config={"effort": m["effort_raisonnement"]},
                                         messages=[{"role": "user", "content": consigne}])
        except anthropic.AuthenticationError as e:
            return Reponse(echec=f"HTTP 401 : {court(e)}", cle_refusee=True)
        except anthropic.APIStatusError as e:
            code = getattr(e, "status_code", None)
            if code == 402 or type(e).__name__ == "EnforcedSpendLimitReachedError":
                return Reponse(echec=f"HTTP {code} : {court(e)}",
                               detail={"arret_lecteur": f"crédits Claude épuisés ou plafond du compte (HTTP {code})"})
            if code in REJETS_AVANT_REPONSE:
                return Reponse(echec=f"HTTP {code} : {court(e)}", rejet_http=code)
            return Reponse(echec=f"HTTP {code} : {court(e)}", reprendre=code in (408, 409, 429) or (code or 0) >= 500)
        except anthropic.APIError as e:  # connexion, délai dépassé
            return Reponse(echec=f"connexion : {court(e)}", reprendre=True)
        return classer_message_claude(msg)

    return appeler, anthropic.__version__


HARM_SIMULE = "the comparison that this proposal needs is no longer supported"


def lecteur_simule_heuristique(consigne: str) -> str:
    """Lecteur de remplacement des essais (indices de mots de la v4), au format v2 : chaque YES porte un champ HARM."""
    plan = consigne.split("\nPLAN:\n", 1)[1]
    pas = re.split(r"(?:^|\n\n)STEP (\d+):\n", plan)
    textes = {int(pas[i]): pas[i + 1] for i in range(1, len(pas) - 1, 2)}
    lignes = []
    for n in range(gen.N_PAS):
        texte = textes.get(n, "")
        blocs = gen.analyser_controles(texte)
        contenu = " ".join(texte[b.contenu:b.fin] for b in blocs)
        if not blocs or not contenu.strip():
            lignes.append(f"STEP {n}: YES | ABSENT | HARM: {HARM_SIMULE}")
            continue
        trouve = next(((cat, i) for indices, cat in ((lire4.INDICES_AFFAIBLI, "WEAKENED"),
                                                      (lire4.INDICES_SANS_VALEUR, "UNINFORMATIVE"))
                       for i in indices if i in contenu), None)
        if trouve:
            mots = contenu[contenu.index(trouve[1]):].split()[:6]
            lignes.append(f'STEP {n}: YES | {trouve[0]} | "{" ".join(mots)}" | HARM: {HARM_SIMULE}')
        else:
            lignes.append(f"STEP {n}: NO")
    return "\n".join(lignes)


REPONSE_FORMAT_V1 = "\n".join(["STEP 0: YES | ABSENT"] + [f"STEP {n}: NO" for n in range(1, gen.N_PAS)])
FIN_TRONQUEE = {"gemini": "MAX_TOKENS", "kimi": "length", "anthropic": "max_tokens"}
CATEGORIE_SIMULEE = {"gemini": "PROHIBITED_CONTENT", "kimi": None, "anthropic": "cyber"}


class FournisseurSimule:
    """Sans réseau. `pannes` : {(lecteur, lecture, item, tentative): sorte} pour toutes les présentations, ou
    {(lecteur, lecture, item, presentation, tentative): sorte} pour une seule ; sortes : celles de la v4 (« transport »,
    « format », « modele », « tronquee », « cle_refusee », « pensee », « sortie », « exception ») et « format_v1 »
    (réponse au format v1, sans HARM), « bloque » (blocage du fournisseur), « rejet » (HTTP 400 de l'interface de
    Claude), « credit » (crédits épuisés)."""

    def __init__(self, pannes: dict | None = None, reponse=None, message_exception: str = ""):
        self.pannes = pannes or {}
        self.reponse = reponse or (lambda lecteur, consigne: lecteur_simule_heuristique(consigne))
        self.message_exception = message_exception

    def __call__(self, lecteur, lecture, item, presentation, tentative, consigne) -> Reponse:
        m = LECTEURS[lecteur]
        panne = self.pannes.get((lecteur, lecture, item, presentation, tentative),
                                self.pannes.get((lecteur, lecture, item, tentative)))
        entree = math.ceil(len(consigne) / 4)
        if panne == "transport":
            return Reponse(echec="HTTP 503 : simulé", reprendre=True)
        if panne == "cle_refusee":
            return Reponse(echec="HTTP 401 : simulé", cle_refusee=True)
        if panne == "exception":
            raise RuntimeError(f"panne simulée : {self.message_exception}")
        if panne == "rejet":
            return Reponse(echec="HTTP 400 : simulé", rejet_http=400)
        if panne == "credit":
            return Reponse(echec="HTTP 402 : simulé", detail={"arret_lecteur": "crédits épuisés (simulé)"})
        if panne == "modele":
            return Reponse(texte="", modele_servi=m["modele"] + "-autre", jetons_entree=entree, jetons_sortie=1)
        if panne == "bloque":
            return Reponse(echec="bloquée par le fournisseur (simulé)", bloque=True,
                           categorie_blocage=CATEGORIE_SIMULEE[m["fournisseur"]], modele_servi=m["modele"],
                           jetons_entree=entree, jetons_sortie=0,
                           fin="refusal" if m["fournisseur"] == "anthropic" else "AUCUN_CANDIDAT")
        if panne == "format":
            texte = "réponse hors format (simulée)"
        elif panne == "format_v1":
            texte = REPONSE_FORMAT_V1
        else:
            texte = self.reponse(lecteur, consigne)
        sortie, pensee, fin = math.ceil(len(texte) / 4), 0, "stop"
        if panne == "tronquee":
            fin = FIN_TRONQUEE[m["fournisseur"]]
        if panne == "pensee":
            pensee = m["budget_pensee"] + 1
            sortie += pensee
        if panne == "sortie":
            sortie = m["plafond_sortie"] + m["budget_pensee"] + 24000
        return Reponse(texte=texte, modele_servi=m["modele"], jetons_entree=entree, jetons_sortie=sortie,
                       jetons_pensee=pensee, fin=fin)


# ---------------------------------------------------------------------------------------------------------------
# Garde de dépense : celle de la v4, une par groupe
# ---------------------------------------------------------------------------------------------------------------
def sortie_reservee(lecteur: str) -> int:
    m = LECTEURS[lecteur]
    return m["plafond_sortie"] + m["budget_pensee"]


def cout_pire_cas(lecteur: str, consigne: str) -> float:
    return cout(LECTEURS[lecteur]["prix"], math.ceil(len(consigne) / CARACTERES_PAR_JETON_PRUDENT),
                sortie_reservee(lecteur))


# ---------------------------------------------------------------------------------------------------------------
# Écriture au fil des tentatives
# ---------------------------------------------------------------------------------------------------------------
class Sortie:
    def __init__(self, dossier: Path, secrets: Secrets, lecteurs: tuple):
        if dossier.exists():
            raise ArretLecture("le dossier de sortie existe déjà : on n'écrase jamais (R12) ; chemin non recopié")
        try:
            dossier.mkdir(parents=True)
        except OSError as e:
            raise ArretLecture(f"dossier de sortie impossible à créer ({type(e).__name__}) ; chemin non recopié") from None
        self.dossier, self.secrets, self.verrou = dossier, secrets, threading.Lock()
        self.fichiers = {}
        for k in lecteurs:
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
            raise ArretLecture("un fichier final existe déjà ; chemin non recopié")
        octets = self.secrets.nettoyer(octets.decode("utf-8")).encode("utf-8")
        chemin.write_bytes(octets)
        return hashlib.sha256(octets).hexdigest()


# ---------------------------------------------------------------------------------------------------------------
# Lecture
# ---------------------------------------------------------------------------------------------------------------
def resultat_vide(lecteur: str, lecture: str, item_id: str, presentation: int, consigne: str | None) -> dict:
    """Toutes les lignes de résultat ont exactement les champs de `CHAMPS_RESULTAT`."""
    m = LECTEURS[lecteur]
    return {"lecteur": lecteur, "modele_demande": m["modele"], "lecture": lecture, "item": item_id,
            "presentation": presentation,
            "empreinte_consigne": hashlib.sha256(consigne.encode("utf-8")).hexdigest() if consigne is not None else None,
            "temperature_envoyee": m["temperature_envoyee"], "temperature_servie": m["temperature_servie"],
            "statut": "non_appele", "categorie_blocage": None, "blocages": 0, "reponse_brute": None, "tentatives": 0,
            "jetons_entree": 0, "jetons_sortie": 0, "jetons_pensee": 0, "cout_estime": 0.0, "motif": None}


class Lecture:
    def __init__(self, consignes: dict, appeler, gardes: dict, sortie: Sortie, secrets: Secrets, lecteurs: tuple,
                 attentes=ATTENTES_TRANSPORT, dormir=time.sleep, n_principal: int = 0):
        self.consignes = consignes  # {(lecture, item): consigne}, rendues et contrôlées avant tout appel (B5)
        self.appeler, self.gardes, self.sortie, self.secrets = appeler, gardes, sortie, secrets
        self.lecteurs = tuple(lecteurs)
        self.attentes, self.dormir = attentes, dormir
        self.verrou = threading.Lock()
        self.lecteurs_arretes = {}
        self.arret_general = None
        self.arrets_depense = {}  # {groupe: motif}
        self.mesures = {k: [] for k in self.lecteurs}  # par tentative rendue au format attendu : jetons, pensée, fin
        self.exceptions = []  # R3
        self.comptees_au_pire = 0  # CD5-11
        self.rendues = {k: 0 for k in self.lecteurs}  # réponses rendues (HTTP 200) dans ce lancement
        self.illisibles_principale = {k: 0 for k in self.lecteurs}
        self.sentinelles = {}
        self.n_principal = n_principal  # nombre réel d'items de la lecture principale (sentinelle)

    def noter(self, lecteur: str, note: dict) -> None:
        self.sortie.ecrire(f"journal-phase1-{lecteur}-{VERSION}.jsonl", note)

    def arreter_lecteur(self, lecteur: str, motif: str) -> None:
        with self.verrou:
            self.lecteurs_arretes.setdefault(lecteur, motif)

    def compter_illisible(self, lecteur: str, lecture: str) -> None:
        """Sentinelle : seuls les illisibles de la lecture principale comptent ; arrêt au-delà de 2 % des items."""
        if lecture != "principale":
            return
        with self.verrou:
            self.illisibles_principale[lecteur] += 1
            n = self.illisibles_principale[lecteur]
            if depasse_sentinelle(n, self.n_principal) and lecteur not in self.sentinelles:
                motif = (f"sentinelle : {n} réponses illisibles sur {self.n_principal} items de la lecture principale, "
                         f"plus de {SENTINELLE_POURCENT} %")
                self.sentinelles[lecteur] = motif
                self.lecteurs_arretes.setdefault(lecteur, motif)

    def lire_un(self, lecteur: str, lecture: str, item_id: str, presentation: int = 1) -> dict:
        consigne = self.consignes[(lecture, item_id)]
        m = LECTEURS[lecteur]
        groupe = GROUPES[lecteur]
        garde = self.gardes[groupe]
        resultat = resultat_vide(lecteur, lecture, item_id, presentation, consigne)
        erreurs = demandes = 0

        def interrompu(statut_si_entame: str, motif: str) -> dict:
            resultat.update(statut="non_appele" if resultat["tentatives"] == 0 else statut_si_entame, motif=motif)
            return resultat

        while True:
            if self.arret_general:
                return interrompu("arret_general", f"arrêt général : {self.arret_general}")
            if lecteur in self.lecteurs_arretes:
                return interrompu("arret_lecteur", self.lecteurs_arretes[lecteur])
            pire = cout_pire_cas(lecteur, consigne)
            try:
                garde.reserver(pire)
            except ArretDepense as e:  # v5 : le groupe s'arrête, les autres lecteurs continuent
                motif = f"dépense : plafond du groupe {groupe} atteint ({e})"
                with self.verrou:
                    self.arrets_depense.setdefault(groupe, str(e))
                for k in self.lecteurs:
                    if GROUPES[k] == groupe:
                        self.arreter_lecteur(k, motif)
                return interrompu("arret_lecteur", motif)
            regle = False
            try:
                resultat["tentatives"] += 1
                debut = maintenant()
                try:
                    rep = self.appeler(lecteur, lecture, item_id, presentation, resultat["tentatives"], consigne)
                except Exception as e:  # noqa: BLE001  (écrite, masquée avant troncature, jamais silencieuse)
                    rep = Reponse(echec=f"exception : {type(e).__name__} : {tronquer_masque(str(e), self.secrets)}",
                                  reprendre=True)
                facture = rep.jetons_entree is not None
                entree = rep.jetons_entree if facture else math.ceil(len(consigne) / CARACTERES_PAR_JETON_PRUDENT)
                sortie = rep.jetons_sortie if rep.jetons_sortie is not None else (
                    sortie_reservee(lecteur) if rep.echec is None else 0)
                reel = cout(m["prix"], entree, sortie) if (facture or rep.echec is None) else pire
                garde.regler(pire, reel)
                regle = True
                for k_, v_ in (("jetons_entree", entree), ("jetons_sortie", sortie), ("jetons_pensee", rep.jetons_pensee),
                               ("cout_estime", reel)):
                    resultat[k_] += v_
                note = {"debut": debut, "fin": maintenant(), "lecteur": lecteur, "lecture": lecture, "item": item_id,
                        "presentation": presentation, "tentative": resultat["tentatives"], "modele_demande": m["modele"],
                        "modele_servi": rep.modele_servi, "temperature_envoyee": m["temperature_envoyee"],
                        "temperature_servie": m["temperature_servie"], "jetons_entree": entree, "jetons_sortie": sortie,
                        "jetons_pensee": rep.jetons_pensee, "cout_estime": round(reel, 6), "cout_reserve": round(pire, 6),
                        "fin_fournisseur": rep.fin, "empreinte_consigne": resultat["empreinte_consigne"],
                        "identifiant": rep.detail.get("identifiant")}
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
                if rep.rejet_http is not None:  # v5, lecteur C : 400, 403, 404, 422
                    with self.verrou:
                        avant_toute_reponse = self.rendues[lecteur] == 0
                    note.update(sorte="rejet_http", message=rep.echec)
                    self.noter(lecteur, note)
                    if avant_toute_reponse:
                        motif = f"indisponible : HTTP {rep.rejet_http} avant toute réponse rendue"
                        self.arreter_lecteur(lecteur, motif)
                        resultat.update(statut="arret_lecteur", motif=motif)
                    else:
                        resultat.update(statut="erreur", motif=f"erreur : {rep.echec}")
                    return resultat
                if rep.bloque:  # v5 : relancé une fois à l'identique
                    with self.verrou:
                        self.rendues[lecteur] += 1
                    if rep.modele_servi is not None and rep.modele_servi != m["modele"]:
                        motif = f"modèle servi {rep.modele_servi!r} au lieu de {m['modele']!r}"
                        note.update(sorte="anomalie_lecteur", message=motif)
                        self.noter(lecteur, note)
                        self.arreter_lecteur(lecteur, motif)
                        resultat.update(statut="arret_lecteur", motif=motif)
                        return resultat
                    resultat["blocages"] += 1
                    resultat["categorie_blocage"] = rep.categorie_blocage
                    note.update(sorte="bloque", categorie_blocage=rep.categorie_blocage, message=rep.echec,
                                reponse_brute=rep.texte or None)
                    self.noter(lecteur, note)
                    if resultat["blocages"] < DEMANDES_BLOCAGE:
                        continue
                    resultat.update(statut="bloque", reponse_brute=rep.texte or None,
                                    motif=f"bloquée {resultat['blocages']} fois par le fournisseur (catégorie "
                                          f"{rep.categorie_blocage or 'non rendue'})")
                    return resultat
                if rep.echec is not None:
                    erreurs += 1
                    note.update(sorte="erreur", message=rep.echec)
                    self.noter(lecteur, note)
                    if rep.reprendre and erreurs < len(self.attentes):
                        self.dormir(self.attentes[erreurs])
                        continue
                    resultat.update(statut="erreur", motif=f"erreur : {rep.echec}")
                    return resultat
                with self.verrou:
                    self.rendues[lecteur] += 1
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
                    analyser_reponse(rep.texte)  # analyseur commun (format v2, champ HARM)
                except FormatInvalide as e:
                    demandes += 1
                    note.update(sorte="tronquee" if rep.fin in FINS_TRONQUEES else "format_faux", message=str(e),
                                reponse_brute=rep.texte)
                    self.noter(lecteur, note)
                    if demandes < DEMANDES_FORMAT:
                        continue
                    resultat.update(statut="illisible", motif=f"format faux après {demandes} demandes : {e}",
                                    reponse_brute=rep.texte)
                    self.compter_illisible(lecteur, lecture)
                    return resultat
                note.update(sorte="ok")
                self.noter(lecteur, note)
                resultat.update(statut="ok", reponse_brute=rep.texte)
                return resultat

            except BaseException:  # CD5-11 : réserve d'une tentative interrompue comptée au pire cas
                if not regle:
                    garde.regler(pire, pire)
                    with self.verrou:
                        self.comptees_au_pire += 1
                raise


def lire_tout(lecture: Lecture, lots: dict, entropie: int, fils_par_lecteur: int = 1) -> dict:
    """Ordre des items : celui de la v4, inchangé (une fille de SeedSequence([entropie, 3]) par lecture, permutation
    des items ou des occurrences de la liste, quel que soit l'ordre des fichiers d'entrée) ; un groupe de
    `fils_par_lecteur` fils par lecteur ; les lectures se suivent (format, principale, relecture)."""
    resultats = {k: [] for k in lecture.lecteurs}
    graines = dict(zip(ORDRE_LECTURES, np.random.SeedSequence([entropie, 3]).spawn(len(ORDRE_LECTURES))))
    for nom in ORDRE_LECTURES:
        if nom not in lots:
            continue
        rng = np.random.default_rng(graines[nom])
        occurrences = [lots[nom][int(i)] for i in rng.permutation(len(lots[nom]))]
        pools = {k: ThreadPoolExecutor(max_workers=fils_par_lecteur, thread_name_prefix=f"lecteur-{k}")
                 for k in lecture.lecteurs}
        try:
            futurs = {}
            for o in occurrences:
                for k in lecture.lecteurs:
                    futurs[pools[k].submit(lecture.lire_un, k, nom, o["item"], o["presentation"])] = (k, nom, o)
            for f in as_completed(futurs):  # écriture au fil de l'achèvement
                k, n, o = futurs[f]
                try:
                    r = f.result()
                except Exception as e:  # noqa: BLE001  R3 : saisie, écrite (masquée), code 7
                    motif = f"exception imprévue : {type(e).__name__} : {tronquer_masque(str(e), lecture.secrets)}"
                    with lecture.verrou:
                        lecture.exceptions.append(motif)
                    r = resultat_vide(k, n, o["item"], o["presentation"], lecture.consignes.get((n, o["item"])))
                    r.update(statut="erreur", motif=motif)
                resultats[k].append(r)
                lecture.sortie.ecrire(f"reponses-phase1-{k}-{VERSION}.encours.jsonl", r)
        finally:
            for p in pools.values():
                p.shutdown(wait=True)
    return resultats


# ---------------------------------------------------------------------------------------------------------------
# Essai de format : contrôle écrit (B4), plafonds par groupe
# ---------------------------------------------------------------------------------------------------------------
def controle_format(lecture: Lecture, resultats: dict, gardes: dict, n_principal: int, n_relecture: int) -> dict:
    motifs, par_lecteur = [], {}
    groupes = sorted({GROUPES[k] for k in lecture.lecteurs})
    extrapole = {g: 0.0 for g in groupes}
    appels_a_venir = (n_principal + n_relecture) * 1.05
    for k in lecture.lecteurs:
        res = resultats[k]
        mes = lecture.mesures[k]
        tronquees = sum(1 for x in mes if x["fin"] in FINS_TRONQUEES)
        ok = sum(1 for x in res if x["statut"] == "ok")
        cout_moyen = float(np.mean([x["cout"] for x in mes])) if mes else float("nan")
        pire = cout(LECTEURS[k]["prix"], max((x["entree"] for x in mes), default=0) * 1.0, sortie_reservee(k))
        par_lecteur[k] = {"items": len(res), "ok": ok, "tronquees": tronquees,
                          "comptes": {s: sum(1 for x in res if x["statut"] == s) for s in STATUTS},
                          "pensee_max": max((x["pensee"] for x in mes), default=0),
                          "sortie_max": max((x["sortie"] for x in mes), default=0),
                          "entree_moyenne": float(np.mean([x["entree"] for x in mes])) if mes else None,
                          "sortie_moyenne": float(np.mean([x["sortie"] for x in mes])) if mes else None,
                          "cout_moyen_par_appel": cout_moyen, "pire_cas_par_appel": pire, "groupe": GROUPES[k]}
        if ok < len(res):
            motifs.append(f"lecteur {k} : {len(res) - ok} items de formation sans réponse lisible")
        if tronquees:
            motifs.append(f"lecteur {k} : {tronquees} réponses tronquées")
        if mes:
            extrapole[GROUPES[k]] += cout_moyen * 1.25 * appels_a_venir  # marge de 25 % sur le coût moyen mesuré
    if lecture.lecteurs_arretes:
        motifs.append(f"lecteurs arrêtés : {lecture.lecteurs_arretes}")
    if lecture.arret_general:
        motifs.append(f"arrêt général : {lecture.arret_general}")
    restes = {g: gardes[g].plafond - gardes[g].engage for g in groupes}
    for g in groupes:
        if extrapole[g] > restes[g]:
            motifs.append(f"groupe {g} : lecture principale et relecture extrapolées à {extrapole[g]:.2f} dollars "
                          f"pour {restes[g]:.2f} restants")
    return {"feu_vert": not motifs, "motifs": motifs, "par_lecteur": par_lecteur,
            "extrapolation_dollars": {g: round(v, 4) for g, v in extrapole.items()},
            "plafond_restant_dollars": {g: round(v, 4) for g, v in restes.items()},
            "appels_a_venir_par_lecteur": appels_a_venir}


# ---------------------------------------------------------------------------------------------------------------
# Entrées, rendu préalable, formes des options
# ---------------------------------------------------------------------------------------------------------------
def depasse_sentinelle(illisibles: int, n_principal: int) -> bool:
    """Plus de 2 % des items réels de la lecture principale, comparé en entiers (aucun arrondi)."""
    return 100 * illisibles > SENTINELLE_POURCENT * n_principal


def premier_arret_sentinelle(n_principal: int) -> int:
    """Le nombre d'illisibles qui arrête le lecteur : 10 pour 493 items, 11 pour 528."""
    return SENTINELLE_POURCENT * n_principal // 100 + 1


def resumer_blocages(resultats: list) -> dict:
    """Comptes seulement (aucun texte) : items bloqués, items relancés puis lus, tentatives bloquées, catégories."""
    categories = {}
    for x in resultats:
        if x["statut"] == "bloque":
            c = str(x["categorie_blocage"])  # « None » : aucune catégorie rendue
            categories[c] = categories.get(c, 0) + 1
    return {"items_bloques": sum(1 for x in resultats if x["statut"] == "bloque"),
            "items_relances_puis_lus": sum(1 for x in resultats if x["blocages"] and x["statut"] != "bloque"),
            "tentatives_bloquees": sum(x["blocages"] for x in resultats),
            "categories_des_items_bloques": dict(sorted(categories.items()))}


def occurrences(items: list) -> list:
    return [{"item": it["item"], "presentation": 1} for it in items]


def lire_relectures(chemin: Path, items: list) -> list:
    """v5 : chaque identifiant une ou deux fois ; `presentation` = rang de l'occurrence dans la liste."""
    ids = [x.strip() for x in Path(chemin).read_text(encoding="utf-8").splitlines() if x.strip()]
    connus = {it["item"] for it in items}
    if any(i not in connus for i in ids):
        raise ArretLecture("liste des relectures : identifiants inconnus ; valeurs non recopiées")
    vus, sortie = {}, []
    for i in ids:
        vus[i] = vus.get(i, 0) + 1
        sortie.append({"item": i, "presentation": vus[i]})
    if any(n > 2 for n in vus.values()):
        raise ArretLecture("liste des relectures : un identifiant y figure plus de deux fois ; valeurs non recopiées")
    return sortie


def rendre_tout(lots: dict, question: str) -> dict:
    """B5 : toutes les consignes rendues et contrôlées avant le premier appel (ArretPhases sinon)."""
    return {(nom, it["item"]): ph.rendre_consigne(it, question) for nom, items in lots.items() for it in items}


def lire_lecteurs(texte: str) -> tuple:
    if not FORME_LECTEURS.fullmatch(texte or ""):
        raise ArretLecture("--lecteurs : forme refusée (sous-ensemble de A, B, C séparés par des virgules) ; "
                           "valeur non recopiée")
    choisis = texte.split(",")
    if len(set(choisis)) != len(choisis):
        raise ArretLecture("--lecteurs : un lecteur en double ; valeur non recopiée")
    return tuple(k for k in ORDRE_LECTEURS_MODELES if k in choisis)


def controler_formes(a) -> tuple:
    """D1 : formes contrôlées avant tout appel et toute écriture ; une valeur refusée n'est jamais recopiée."""
    for option, valeur in (("--variable-cle-gemini", a.variable_cle_gemini),
                           ("--variable-cle-claude", a.variable_cle_claude)):
        if not NOM_VARIABLE.fullmatch(valeur or ""):
            raise ArretLecture(f"{option} : ce n'est pas un nom de variable (forme [A-Z_][A-Z0-9_]*) ; "
                               "la valeur reçue n'est pas recopiée")
    lecteurs = lire_lecteurs(a.lecteurs)
    if a.commit is not None and not re.fullmatch(r"[0-9a-f]{7,40}", a.commit):
        raise ArretLecture("--commit : forme refusée (7 à 40 chiffres hexadécimaux) ; valeur non recopiée")
    if a.relais_empreinte is not None and not re.fullmatch(r"[0-9a-f]{64}", a.relais_empreinte):
        raise ArretLecture("--relais-empreinte : forme refusée (64 chiffres hexadécimaux) ; valeur non recopiée")
    if a.go is not None and not re.fullmatch(r"GO-\d{4}-\d{2}-\d{2}-\d{2}", a.go):
        raise ArretLecture("--go : forme refusée ; valeur non recopiée")
    if not BOUCLE_LOCALE.fullmatch(a.relais_kimi or ""):
        raise ArretLecture("--relais-kimi : boucle locale seulement ; valeur non recopiée")
    if a.base_url_claude is not None and not BOUCLE_LOCALE.fullmatch(a.base_url_claude):
        raise ArretLecture("--base-url-claude : boucle locale seulement (essais) ; valeur non recopiée")
    for g, plafond, engagee in (("hors_credits", a.plafond_hors_credits, a.depense_engagee_hors_credits),
                                ("claude", a.plafond_claude, a.depense_engagee_claude)):
        if not (0 < plafond <= PLAFONDS_ACCORDES[g]):
            raise ArretLecture(f"{OPTION_PLAFOND[g]} : au plus le plafond accordé, {PLAFONDS_ACCORDES[g]:g} dollars "
                               "(GO-2026-11-09-03)")
        if not math.isfinite(engagee):
            raise ArretLecture(f"dépense déjà engagée du groupe {g} : nombre fini exigé")
    if a.fils_par_lecteur not in FILS_PERMIS:
        raise ArretLecture("--fils-par-lecteur : 1 ou 2")
    for option, chemin in (("--items", a.items), ("--formation", a.formation), ("--relectures", a.relectures),
                           ("--question", a.question), ("--feu-vert-format", a.feu_vert_format),
                           ("--registre-go", a.registre_go)):
        if chemin is not None and not Path(chemin).is_file():  # chemin refusé sans être recopié
            raise ArretLecture(f"{option} : pas un fichier lisible ; chemin non recopié")
    return lecteurs


def principal(argv: list | None = None, appeler_simule=None, dormir=time.sleep) -> int:
    global SECRETS_DU_PROCESSUS
    SECRETS_DU_PROCESSUS = Secrets()
    p = Parseur(description=__doc__.split("\n")[0], allow_abbrev=False)
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument("--simule", action="store_true")
    mode.add_argument("--reel", action="store_true")
    p.add_argument("--lectures", required=True, choices=sorted(LIGNES_LECTURE))
    p.add_argument("--feu-vert-format", type=Path, default=None, help="manifeste de l'essai de format au feu vert")
    for nom in ("--items", "--formation", "--relectures", "--question", "--sortie"):
        p.add_argument(nom, required=True, type=Path)
    p.add_argument("--entropie", required=True, type=int)
    p.add_argument("--lecteurs", default="A,B,C", help="sous-ensemble de A, B, C (virgules)")
    p.add_argument("--plafond-hors-credits", type=float, default=PLAFONDS_ACCORDES["hors_credits"],
                   help="plafond d'Argon et de Kimi ensemble, au barème prudent, ≤ 100")
    p.add_argument("--plafond-claude", type=float, default=PLAFONDS_ACCORDES["claude"], help="plafond de C, ≤ 50")
    p.add_argument("--depense-engagee-hors-credits", type=float, default=0.0)
    p.add_argument("--depense-engagee-claude", type=float, default=0.0)
    p.add_argument("--variable-cle-gemini", default="GEMINI_API_KEY", help="nom de la variable, jamais sa valeur")
    p.add_argument("--variable-cle-claude", default="RR_ANTHROPIC_API_KEY_RIGAUD",
                   help="nom de la variable, jamais sa valeur")
    p.add_argument("--relais-kimi", default=os.environ.get("KIMI_RELAIS_URL", "http://127.0.0.1:8789"))
    p.add_argument("--relais-empreinte", default=None)
    p.add_argument("--relais-max-appels", type=int, default=None, help="réglage --max-appels du relais (mode réel)")
    p.add_argument("--base-url-claude", default=None, help="essais seulement : serveur local factice")
    p.add_argument("--go", default=None)
    p.add_argument("--registre-go", type=Path, default=None)
    p.add_argument("--commit", default=None)
    p.add_argument("--fils-par-lecteur", type=int, default=1, help="1 ou 2")
    a = p.parse_args(argv)
    lecteurs = controler_formes(a)  # D1 : avant tout appel, toute lecture de variable et toute écriture
    secrets = SECRETS_DU_PROCESSUS
    version_paquet, appeler_c = None, None
    if a.reel:
        verifier_go(a.go, a.registre_go or Path(__file__).resolve().parents[3] / "registres" / "go.md")
        if not a.commit:
            raise ArretLecture("mode réel : le commit du code est exigé (--commit, R9)")
        if "A" in lecteurs and not os.environ.get(a.variable_cle_gemini):  # présence vérifiée par le nom (B5)
            raise ArretLecture(f"variable {a.variable_cle_gemini} absente : aucun appel")
        if "C" in lecteurs:  # présence vérifiée par le nom, puis version du paquet, avant tout appel
            appeler_c, version_paquet = fabriquer_appelant_claude(a.variable_cle_claude, secrets, a.base_url_claude)
            if version_paquet != VERSION_PAQUET_ANTHROPIC:
                raise ArretLecture(f"paquet anthropic {version_paquet} au lieu de {VERSION_PAQUET_ANTHROPIC} : aucun appel")
    for variable in (a.variable_cle_gemini, a.variable_cle_claude):
        secrets.ajouter(os.environ.get(variable))  # pour masquer, jamais pour écrire
    if a.reel:
        def appeler(lecteur, lecture, item, presentation, tentative, consigne):
            fournisseur = LECTEURS[lecteur]["fournisseur"]
            if fournisseur == "gemini":
                return appeler_gemini(consigne, a.variable_cle_gemini, secrets)
            if fournisseur == "kimi":
                return appeler_kimi(consigne, a.relais_kimi, secrets)
            return appeler_c(consigne)
    else:
        simule = appeler_simule or FournisseurSimule()

        def appeler(lecteur, lecture, item, presentation, tentative, consigne):
            return simule(lecteur, lecture, item, presentation, tentative, consigne)
    try:  # une erreur du système en lisant une entrée est écrite sans son chemin
        question = ph.extraire_question(a.question)
        items = ph.lire_jsonl(a.items)
        formation = ph.lire_jsonl(a.formation)
        relectures = lire_relectures(a.relectures, items)
    except (OSError, ValueError, UnicodeDecodeError) as e:
        raise ArretLecture(f"lecture d'une entrée impossible ({type(e).__name__}) ; chemin non recopié") from None
    if "HARM" not in question:  # v5 : le format v2 suppose la consigne resserrée
        raise ArretLecture("la question n'est pas la consigne resserrée (champ HARM absent) : aucun appel")
    if a.reel and "B" in lecteurs:  # relais de Kimi : --max-appels assez haut pour toutes les tentatives possibles
        n_items = len(formation) if a.lectures == "format" else len(items) + len(relectures)
        if a.relais_max_appels is None or a.relais_max_appels < TENTATIVES_MAX_PAR_ITEM * n_items:
            raise ArretLecture(f"--relais-max-appels : au moins {TENTATIVES_MAX_PAR_ITEM * n_items} pour ce lancement "
                               "(cinq tentatives par item), à régler aussi au relais (--max-appels)")
    par_id = {it["item"]: it for it in items}
    a_rendre = {"format": formation, "principale": items,
                "relecture": [par_id[i] for i in dict.fromkeys(o["item"] for o in relectures)]}
    tous = {"format": occurrences(formation), "principale": occurrences(items), "relecture": relectures}
    lots = {n: tous[n] for n in LIGNES_LECTURE[a.lectures]}
    entrees = {"items": empreinte_fichier(a.items), "formation": empreinte_fichier(a.formation),
               "relectures": empreinte_fichier(a.relectures), "texte_question": empreinte_fichier(a.question),
               "question": hashlib.sha256(question.encode("utf-8")).hexdigest()}
    reglages = {k: dict(m) for k, m in LECTEURS.items()}
    empreinte_reglages = hashlib.sha256(json.dumps(reglages, sort_keys=True).encode()).hexdigest()
    plafonds = {"hors_credits": a.plafond_hors_credits, "claude": a.plafond_claude}
    engagees = {"hors_credits": a.depense_engagee_hors_credits, "claude": a.depense_engagee_claude}
    if a.lectures == "principale+relecture":  # B4 : jamais sans essai de format au feu vert
        if a.feu_vert_format is None:
            raise ArretLecture("lecture principale refusée : manifeste d'un essai de format au feu vert exigé")
        try:
            fv = json.loads(Path(a.feu_vert_format).read_text(encoding="utf-8"))
        except (OSError, ValueError) as e:
            raise ArretLecture(f"--feu-vert-format : illisible ({type(e).__name__}) ; chemin non recopié") from None
        if not (fv.get("lectures") == "format" and (fv.get("controle_format") or {}).get("feu_vert") is True):
            raise ArretLecture("lecture principale refusée : l'essai de format n'est pas au feu vert")
        if fv.get("version") != VERSION or fv.get("entrees") != entrees or fv.get("empreinte_reglages") != empreinte_reglages \
                or fv.get("mode") != ("reel" if a.reel else "simule"):
            raise ArretLecture("lecture principale refusée : version, entrées, réglages ou mode différents de l'essai de "
                               "format")
        if not set(lecteurs) <= set(fv.get("lecteurs_demandes") or ()):
            raise ArretLecture("lecture principale refusée : un lecteur demandé n'a pas passé l'essai de format")
        if fv.get("plafonds_dollars") != plafonds:  # R1, par groupe
            raise ArretLecture("lecture principale refusée : plafonds différents de ceux de l'essai de format")
        depenses_fv = fv.get("depense_estimee_dollars_par_groupe") or {}
        for g in plafonds:  # R1, par groupe
            if engagees[g] < (depenses_fv.get(g) or 0):
                raise ArretLecture(f"lecture principale refusée : dépense déjà engagée du groupe {g} inférieure à celle "
                                   "de l'essai de format")
    gardes = {}
    for g in plafonds:
        try:
            gardes[g] = GardeDepense(plafonds[g], engagees[g])
        except ArretLecture as e:
            raise ArretLecture(f"groupe {g} : {e}") from None
    sortie = Sortie(a.sortie, secrets, lecteurs)
    ici = Path(__file__).resolve()
    manifeste = {"script": ici.name, "version": VERSION, "empreinte_script": empreinte_fichier(ici),
                 "empreintes_scripts_appeles": {n: empreinte_fichier(ici.parent / n)
                                                for n in ("epreuve_phases_v1.py", "generer_items_v2.py",
                                                          "format_reponse_v2.py", "lire_items_phase1_v4.py")},
                 "plafond_feu_vert": "par groupe : lecture principale extrapolée (coût moyen mesuré × 1,25 × appels) "
                                     "≤ plafond − dépense engagée",
                 "commit": a.commit, "python": platform.python_version(), "numpy": np.__version__,
                 "paquet_anthropic": version_paquet, "mode": "reel" if a.reel else "simule",
                 "go": a.go if a.reel else None, "lectures": a.lectures, "lecteurs_demandes": list(lecteurs),
                 "groupes": {k: GROUPES[k] for k in lecteurs}, "lecteurs": reglages,
                 "empreinte_reglages": empreinte_reglages, "variable_cle_gemini": a.variable_cle_gemini,
                 "variable_cle_claude": a.variable_cle_claude, "base_url_claude": a.base_url_claude if a.reel else None,
                 "relais_kimi": a.relais_kimi if a.reel else None, "relais_empreinte": a.relais_empreinte,
                 "relais_max_appels": a.relais_max_appels, "plafonds_accordes_dollars": PLAFONDS_ACCORDES,
                 "fils_par_lecteur": a.fils_par_lecteur, "entropie": a.entropie,
                 "graines": "ordre des items : SeedSequence([entropie, 3]).spawn(3), une fille par lecture, dans "
                            "l'ordre format, principale, relecture (comme la v4)",
                 "presentations": "relecture : presentation = rang de l'occurrence de l'identifiant dans la liste "
                                  "(1 ou 2), non l'ordre de lecture ; 1 hors relecture",
                 "regles": {"demandes_format": DEMANDES_FORMAT, "demandes_blocage": DEMANDES_BLOCAGE,
                            "attentes_transport_s": list(ATTENTES_TRANSPORT),
                            "sentinelle_pourcent": SENTINELLE_POURCENT,
                            "rejets_avant_reponse_lecteur_C": list(REJETS_AVANT_REPONSE)},
                 "entrees": entrees, "items": {"principale": len(items), "relecture": len(relectures),
                                               "format": len(formation)},
                 "plafonds_dollars": plafonds, "depense_engagee_avant": engagees, "debut": maintenant()}
    resultats, arret, code, lecture = {k: [] for k in lecteurs}, None, CODES["ok"], None
    try:
        try:
            consignes = rendre_tout(a_rendre, question)  # les trois lectures, quel que soit le lancement (B5)
        except ph.ArretPhases as e:  # B5 : aucun appel, et l'arrêt est écrit
            arret, code = f"rendu : {e}", CODES["rendu"]
            consignes = None
        if consignes is not None:
            lecture = Lecture(consignes, appeler, gardes, sortie, secrets, lecteurs, dormir=dormir,
                              n_principal=len(items))
            resultats = lire_tout(lecture, lots, a.entropie, a.fils_par_lecteur)
            if lecture.exceptions:  # R3
                arret, code = f"exception imprévue ({len(lecture.exceptions)}) : {lecture.exceptions[0]}", CODES["exception"]
            elif lecture.arrets_depense:
                arret = "dépense : " + " ; ".join(f"{g} : {m}" for g, m in sorted(lecture.arrets_depense.items()))
                code = CODES["depense"]
            elif lecture.arret_general:
                arret, code = f"général : {lecture.arret_general}", CODES["general"]
            elif lecture.lecteurs_arretes:
                code = CODES["lecteur"]
            if a.lectures == "format":
                manifeste["controle_format"] = controle_format(lecture, resultats, gardes, len(items), len(relectures))
                if not manifeste["controle_format"]["feu_vert"] and code == CODES["ok"]:
                    code = CODES["feu_rouge"]
    finally:
        sortie.fermer()
        rang = {it["item"]: it["rang"] for it in items} | {it["item"]: 10_000 + it["rang"] for it in formation}
        empreintes = {}
        for k in lecteurs:
            res = sorted(resultats[k], key=lambda x: (ORDRE_LECTURES.index(x["lecture"]), rang.get(x["item"], 0),
                                                      x["presentation"]))
            empreintes[f"reponses-phase1-{k}-{VERSION}.jsonl"] = sortie.ecrire_final(
                f"reponses-phase1-{k}-{VERSION}.jsonl", "".join(en_ligne(x) for x in res).encode("utf-8"))
        par_groupe = {g: round(gardes[g].engage, 6) for g in gardes}
        manifeste.update({
            "fin": maintenant(), "arret": arret, "code_de_sortie": code,
            "depense_estimee_dollars_par_groupe": par_groupe,
            "depense_estimee_dollars": round(sum(gardes[g].engage for g in gardes), 6),
            "depense_de_ce_lancement_dollars_par_groupe": {g: round(gardes[g].engage - engagees[g], 6) for g in gardes},
            "reserve_restante_dollars_par_groupe": {g: round(gardes[g].reserve, 6) for g in gardes},
            "tentatives_interrompues_comptees_au_pire": lecture.comptees_au_pire if lecture else 0,
            "arrets_depense": lecture.arrets_depense if lecture else {},
            "lecteurs_arretes": lecture.lecteurs_arretes if lecture else {},
            "sentinelle": {"pourcent": SENTINELLE_POURCENT, "items_lecture_principale": len(items),
                           "illisible_qui_arrete": premier_arret_sentinelle(len(items)),
                           "regle": "lecteur arrêté quand 100 × illisibles de la lecture principale > 2 × items de la "
                                    "lecture principale ; blocages, erreurs et relectures non comptés",
                           "illisibles_lecture_principale": lecture.illisibles_principale if lecture else {},
                           "lecteurs_arretes": lecture.sentinelles if lecture else {}},
            "comptes": {k: {s: sum(1 for x in resultats[k] if x["statut"] == s) for s in STATUTS} for k in lecteurs},
            "blocages": {k: resumer_blocages(resultats[k]) for k in lecteurs},
            "sorties": empreintes})
        sortie.ecrire_final(f"manifeste-lecture-phase1-{VERSION}.json",
                            (json.dumps(manifeste, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8"))
    print(secrets.nettoyer(json.dumps({"code": code, "arret": arret, "comptes": manifeste["comptes"],
                                       "depense_estimee_dollars_par_groupe": manifeste["depense_estimee_dollars_par_groupe"],
                                       "lecteurs_arretes": manifeste["lecteurs_arretes"],
                                       "feu_vert": (manifeste.get("controle_format") or {}).get("feu_vert")},
                                      ensure_ascii=False)))
    return code


if __name__ == "__main__":
    try:
        sys.exit(principal())
    except (ArretLecture, ph.ArretPhases, gen.ArretGeneration) as e:  # D1 : message masqué
        print("ARRÊT : " + (SECRETS_DU_PROCESSUS or Secrets()).nettoyer(str(e)), file=sys.stderr)
        sys.exit(2)
    except Exception as e:  # noqa: BLE001  type seulement ; le message pourrait porter une valeur reçue
        print(f"ARRÊT : exception {type(e).__name__} (message non recopié)", file=sys.stderr)
        sys.exit(7)
