#!/usr/bin/env python3
"""Lanceur de l'« épreuve fraîche » du pont fiche de course -> fiche-loi, version 2 (GO-2026-11-01-09, plafond 5 USD).

Rédigé le 1er novembre 2026 par un sous-agent neuf de session-depot ; rien n'a été lancé par le rédacteur. Le protocole fait
foi dans `preregistrement-epreuve-pont-v2.md` (scellé avant tout appel) ; ce module l'exécute.

Version 2 = version 1 (`lancer_epreuve_pont_v1.py`, inchangée, R12) avec les corrections de la contre-lecture 1 :
CL-01 symétrie R4 en miroir (six déclencheurs codés) ; CL-05 Argon appelé **sans reprise interne**
(`appeler_gemini(..., attentes=(0,))`), la seule reprise étant celle du lanceur, avec une nouvelle réservation au pire cas, et
un coût lu au-dessus de son pire cas arrête le tour ; CL-07 lecture partielle (prédictions et L5 « non lisibles » hors de leur
domaine) ; CL-09 témoins : contrôle par programme de leur transcription des six descriptions, étiquettes « T1 » à « T6 »
refusées, témoins scellés et inscrits au registre exigés au lancement, contrôle de la transcription du sous-agent
(`verifier-transcription`) ; CL-10 appels en cours comptés à leur pire cas si le processus est tué, réponses tronquées
rapportées à part, refus de la vraie garde v56 = anomalie (audit avant L3) ; CL-11 commit du dépôt et versions du Python des
appels écrits et scellés dans le dossier du run ; CL-04 garde du préambule du tour neuf.

Ce que fait le module :

- appelle `pont_v1.traduire_fiche` (module de conv-audit, inchangé) sur les fiches tirées (`fiches-tirees/`) et les six
  témoins (`temoins/`), mêlés et anonymes, dans l'ordre de passage tiré par `tirer_fiches_v2.py` ;
- traducteur Kimi (kimi-k3.1-pro, par le relais local `relais_kimi_v3.py`, aucune clé ici), contre-traducteur Argon
  (gemini-4-argon, fonction `appeler_gemini` du collisionneur v7) : règle fixe `pont_v1.affectation_recommandee("anthropic")`
  (auteur Fable ou témoin écrit par un sous-agent Claude : famille Anthropic) ;
- garde de plafond **cumulée** avant chaque appel : dépense réglée + réservations en cours + pire cas de l'appel <= plafond ;
  un appel sans usage lisible est compté à son pire cas ;
- liste d'arrêt du préenregistrement : `LectureEpreuveInterdite`, canari, plafond, trois refus, trois échecs techniques,
  modèle servi différent, toute autre erreur du module (aucun repli) ;
- refus (statut « REFUS » de l'API) : la fiche s'arrête (le module la renvoie, N10 ou N8) ; un **tour neuf** unique,
  reformulé par un préambule technique (règle R-750), est permis par `reprendre-refus`, sous le même GO et le même plafond
  cumulé ;
- échec de transport (aucune réponse reçue) : une seule reprise à l'identique, consignée ; une réponse reçue n'est jamais
  rejouée ;
- sorties brutes, fiches-lois et journal dans un dossier de run neuf (R12), compagnons `.sha256` (R6) ; agrégat mécanique
  des critères L1 à L5 pour le lecteur neuf ; aucune clé lue ni écrite par ce module (Argon : `GEMINI_API_KEY` lue par
  `appeler_gemini` dans l'environnement préparé sous `env -i` par le lanceur `.sh`).

Sous-commandes :
  preparer         --pole-v56 DOSSIER              catalogue public et état du noyau (Python du dépôt : numpy)
  verifier-temoins --pole-v56 DOSSIER              forme, garde A4, longueur, transcription des six descriptions
  verifier-transcription --transcription FICHIER   outils utilisés par le sous-agent metteur en forme (JSONL)
  lancer           --pole-v56 DOSSIER --sortie RUN [--parallele N]           (GO_ID exigé)
  restant          --run-precedent RUN             dollars restants sous le plafond cumulé
  reprendre-refus  --pole-v56 DOSSIER --run-precedent RUN --preambule FICHIER --sortie RUN2   (GO_ID exigé)
  agreger          --run RUN [--reprise RUN2]      agrégat mécanique (agregat-relu-v2.json)
"""

import argparse
import copy
import datetime
import functools
import hashlib
import importlib.metadata
import importlib.util
import json
import os
import platform
import re
import subprocess
import sys
import threading
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ICI = Path(__file__).resolve().parent
DEPOT = ICI.parents[1]
sys.path.insert(0, str(ICI / "pont"))
sys.path.insert(0, str(ICI))
import pont_v1 as pv  # noqa: E402
import tirer_fiches_v2 as tf  # noqa: E402

VERSION = "lanceur-epreuve-pont-v2"
PREREG = ICI / "preregistrement-epreuve-pont-v2.md"
CATALOGUE = ICI / "catalogue-public-t05-v2-pont-v1.json"
NOYAU = ICI / "noyau-pont-t05-v2-v1.json"
VERITE = ICI / "verite-temoins-v1.json"
TIREES = ICI / "fiches-tirees"
TEMOINS_DOSSIER = ICI / "temoins"
COLLISIONNEUR = DEPOT / "donnees" / "espece-seule-v1" / "collisionneur_v7.py"
SHA_COLLISIONNEUR = "c9725f025407c3ece3e8c16d19cfdfdec078f084a811f0a3b6ea3209be5d98dc"
SHA_ARCHIVE_V56 = "29b1b38cfee5e279a06c947fdf1f855628b574e81e44c2d7e48a029151c1b24c"
NOM_ARCHIVE_V56 = "CODE-orchestrateur-pole-v7-v56.zip"
BANQUE = "banque-t05-v2"
SHA_BANQUE = "f26cc85794f0e65bca6217911f862414f1489195b9bf3ada51d22a3af0fe0d71"
GRAINE_MONDE = 20261101
GO_ATTENDU = "GO-2026-11-01-09"
PLAFOND_USD = 5.0
TEMOINS = tf.TEMOINS
MODELES = {
    "traducteur": {"id": "kimi-k3.1-pro", "fournisseur": "kimi", "prix": (2.0, 10.0), "max_tokens": 24000},
    "contre_traducteur": {"id": "gemini-4-argon", "fournisseur": "gemini", "prix": (10.0, 50.0), "max_tokens": 12000},
}
AFFECTATION = {"famille_auteur": "anthropic", "traducteur": MODELES["traducteur"]["id"],
               "contre_traducteur": MODELES["contre_traducteur"]["id"]}
ALPHA, M_FICHES, POLITIQUE = 0.05, 8, "fraiche_seulement"
MAX_REFUS, MAX_ECHECS = 3, 3
LONGUEUR_SERVIE = (5382, 8251)  # fourchette des 15 fiches de Fable (mesure `tirer_fiches_v2.taille_servie`)
CHAMPS_GABARIT = ("nom", "type", "enonce", "loi_predictive", "perte_traduction", "questions_servies", "avantage",
                  "originalite", "demande_organisme", "cout", "piege", "cosmetique_si", "anteriorite")
VARIABLES_CLES = ("GEMINI_API_KEY", "GEMINI_API_KEY_2", "KIMI_API_KEY")
PAUSE_REPRISE_S = 30
REGISTRE_DECISIONS = "registres/decisions.md"
MOTIF_ETIQUETTE_T = re.compile(r"(?<![A-Za-z0-9_])T[1-6](?![0-9])")  # CL-09 : étiquette d'un témoin
STATUTS_TRONQUES = ("TRONQUE", "VIDE")
# CL-04 : le préambule n'ajoute que domaine et vocabulaire ; il ne nomme ni sortie, ni code, ni témoin, ni l'épreuve.
MOTIFS_PREAMBULE = (re.compile(r"(?<![A-Za-z0-9])N(?:1[01]|[1-9])(?![0-9])"), re.compile(r"non_testable"),
                    re.compile(r"loi_banque_existante"), re.compile(r"loi_couche_3"), MOTIF_ETIQUETTE_T)
MOTS_PREAMBULE = ("temoin", "couche 3", "epreuve", "sortie 1", "sortie 2", "sortie 3", "renvoi")
# CL-09 : chemins que le metteur en forme ne doit jamais toucher (seuls sa consigne v2 et ses témoins lui sont permis).
INTERDITS_TRANSCRIPTION = ("/pont/", "pont_v1", "/entree", "entree/", "fiches-tirees", "preregistrement-epreuve-pont",
                           "verite-temoins", "conception-pont", "contre-lecture", "noyau-pont", "manifeste-tirage",
                           "tirer_fiches", "test_epreuve_pont", "LISEZMOI", "lancer_epreuve_pont_v1", "lancer-epreuve-pont",
                           "registres/", "consigne-metteur-en-forme-temoins-v1", "catalogue-public", "run-epreuve-pont")
LECTURES_SHELL = ("cat ", "sed ", "head ", "tail ", "less ", "more ", "grep ", "awk ", "python3 -c", "python -c", "open(",
                  "strings ", "xxd ", "od ")


class ArretDuTour(Exception):
    pass


class PlafondAtteint(ArretDuTour):
    pass


class EchecTechnique(Exception):
    pass


class LancementRefuse(Exception):
    pass


def maintenant():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def lire_json(chemin):
    return json.loads(Path(chemin).read_text(encoding="utf-8"))


# --- pièces, GO, préenregistrement --------------------------------------------------------------------------------------

def charger_collisionneur(chemin=COLLISIONNEUR, sha=SHA_COLLISIONNEUR):
    if tf.sha256_fichier(chemin) != sha:
        raise LancementRefuse(f"collisionneur v7 : empreinte différente de {sha[:12]}…")
    spec = importlib.util.spec_from_file_location("collisionneur_v7_epreuve_pont", str(chemin))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verifier_go(go_id, registre=DEPOT / "registres" / "go.md", aujourd_hui=None):
    """GO de type « calcul », non révoqué, non échu, plafond >= celui de l'épreuve."""
    if go_id != GO_ATTENDU:
        raise LancementRefuse(f"GO_ID {go_id!r} : l'épreuve ne court que sous {GO_ATTENDU}")
    aujourd_hui = aujourd_hui or datetime.datetime.now(datetime.timezone.utc).date().isoformat()
    lignes = [l for l in Path(registre).read_text(encoding="utf-8").splitlines() if l.startswith("|")]
    propres = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lignes]
    go = [c for c in propres if c and c[0] == go_id]
    if len(go) != 1 or len(go[0]) < 8:
        raise LancementRefuse(f"{go_id} : une seule ligne à 8 colonnes attendue dans registres/go.md ({len(go)})")
    _, accorde, genre, _, plafond, echeance, par, _ = go[0][:8]
    if genre != "calcul" or par != "Lazar":
        raise LancementRefuse(f"{go_id} : type « calcul » accordé par Lazar exigé ({genre!r}, {par!r})")
    if not (accorde <= aujourd_hui <= echeance):
        raise LancementRefuse(f"{go_id} : hors de sa période de validité ({accorde} à {echeance})")
    m = re.match(r"([0-9]+(?:[.,][0-9]+)?)\s*USD", plafond)
    if not m or float(m.group(1).replace(",", ".")) < PLAFOND_USD:
        raise LancementRefuse(f"{go_id} : plafond {plafond!r} inférieur à {PLAFOND_USD} USD")
    for c in propres:
        if len(c) >= 4 and c[2] == "révocation" and go_id in " ".join(c):
            raise LancementRefuse(f"{go_id} révoqué")
    return go[0]


MOTIF_PIECE = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*`?([0-9a-f]{64})`?\s*\|", re.M)


def pieces_gelees(texte_prereg):
    """Lignes « | `chemin depuis la racine du dépôt` | `sha256` | … » de la section « Pièces gelées »."""
    debut = texte_prereg.find("### Pièces gelées")
    if debut < 0:
        raise LancementRefuse("préenregistrement sans section « Pièces gelées »")
    fin = texte_prereg.find("\n## ", debut)
    pieces = MOTIF_PIECE.findall(texte_prereg[debut:fin if fin > 0 else None])
    if not pieces:
        raise LancementRefuse("section « Pièces gelées » vide")
    return pieces


def verifier_pieces(prereg=None, depot=None):
    """Préenregistrement scellé et conforme, puis chaque pièce gelée identique sur disque (aucun repli)."""
    prereg, depot = prereg or PREREG, depot or DEPOT
    sha = tf.prereg_scelle(prereg)
    verifiees = []
    for chemin, attendue in pieces_gelees(Path(prereg).read_text(encoding="utf-8")):
        p = Path(depot) / chemin
        if not p.is_file():
            raise LancementRefuse(f"pièce gelée absente sur disque : {chemin}")
        obtenue = tf.sha256_fichier(p)
        if obtenue != attendue:
            raise LancementRefuse(f"pièce gelée modifiée : {chemin} ({obtenue[:12]}… au lieu de {attendue[:12]}…)")
        verifiees.append({"chemin": chemin, "sha256": obtenue})
    return sha, verifiees


def charger_v56(dossier):
    """Code de l'orchestrateur v56 déplié (archive vérifiée par le `.sh` ; revérifiée ici si elle est à côté)."""
    dossier = Path(dossier)
    if not (dossier / "pole" / "proposeur.py").is_file():
        raise LancementRefuse(f"orchestrateur v56 absent de {dossier}")
    archive = dossier.parent / NOM_ARCHIVE_V56
    if archive.is_file() and tf.sha256_fichier(archive) != SHA_ARCHIVE_V56:
        raise LancementRefuse("archive v56 : empreinte non conforme")
    if str(dossier) not in sys.path:
        sys.path.insert(0, str(dossier))
    from pole import ideation_v2, proposeur
    return ideation_v2, proposeur


def fabriquer_garde_reelle(proposeur, catalogue):
    """La vraie `proposeur.valider_proposition` (v56). La couche v57 n'existe pas : la stratégie du pont est ajoutée au
    catalogue du proposeur **en mémoire**, dans ce processus seulement (aucun fichier v56 modifié ; écart déclaré)."""
    proposeur.CATALOGUE.setdefault(pv.STRATEGIE, "traduction d'une fiche de course (pont v1) — ajout en mémoire, épreuve v1")

    class MondeCatalogue:
        def __init__(self, description):
            self._d = description

        def description_publique(self):
            return copy.deepcopy(self._d)

    def garde(proposition, nom_banque):
        desc = (catalogue.get("banques") or {}).get(nom_banque)
        if desc is None:
            raise LancementRefuse(f"banque inconnue du catalogue : {nom_banque!r}")
        proposeur.valider_proposition(proposition, MondeCatalogue(desc), ALPHA, "pont-epreuve-v1", "pont-v1")
    return garde


# --- entrées de l'épreuve -----------------------------------------------------------------------------------------------

def charger_catalogue_noyau(catalogue=None, noyau=None):
    catalogue, noyau = catalogue or CATALOGUE, noyau or NOYAU
    for p in (catalogue, noyau):
        tf.verifier_compagnon(p)
    cat, noy = lire_json(catalogue), lire_json(noyau)
    entree_test = pv.construire_entree({"essai": "catalogue"}, cat)
    pv.garde_entree(entree_test, ())  # clés interdites dans le catalogue servi : arrêt avant tout appel
    noyau_pont = {k: noy[k] for k in ("predicteurs_connus", "registre_lectures", "epreuves_fraiches", "sondes")}
    if any(noyau_pont["epreuves_fraiches"].values()) or noy.get("politique_epreuve") != POLITIQUE:
        raise LancementRefuse("état du noyau : épreuves marquées lues et politique « fraîche seulement » exigées")
    return cat, noyau_pont, list(noy["canaris"])


def charger_fiches_tirees(dossier=None):
    dossier = Path(dossier or TIREES)
    if not (dossier / tf.MANIFESTE).is_file():
        raise LancementRefuse(f"fiches tirées absentes : {dossier / tf.MANIFESTE} (tirage à faire après le scellement)")
    tf.verifier_compagnon(dossier / tf.MANIFESTE)
    manifeste = lire_json(dossier / tf.MANIFESTE)
    fiches = {}
    for num, d in manifeste["fiches_tirees"].items():
        p = dossier / d["fichier"]
        if tf.verifier_compagnon(p) != d["sha256"]:
            raise LancementRefuse(f"fiche tirée {num} : empreinte différente du manifeste")
        vue = tf.vue_anonyme(lire_json(p))
        tf.garde_a4(vue, f"la fiche servie {num}")
        fiches[num] = vue
    ordre = manifeste["ordre_de_passage"]
    attendu = sorted(list(fiches) + list(TEMOINS))
    if sorted(ordre) != attendu:
        raise LancementRefuse("ordre de passage : il doit contenir chaque fiche tirée et chaque témoin une fois")
    return fiches, ordre, manifeste


def _contient(texte, *morceaux):
    n = tf.normaliser_texte(texte)
    return all(tf.normaliser_texte(m) in n for m in morceaux)


def controle_temoin(t, vue):
    """CL-09 : la fiche transcrit-elle sa description (consigne v2, section 4) ? Rend la liste des écarts (vide si conforme)."""
    lp = vue.get("loi_predictive") or {}
    pred, signe, esp, met = str(lp.get("prediction", "")), lp.get("signe"), str(lp.get("espace_instances", "")), \
        str(lp.get("metrique", ""))
    nombres = pv.nombres_du_texte(pred)
    texte = json.dumps(vue, ensure_ascii=False)
    attendu = {
        "T1": [("type", vue.get("type") == "question"), ("signe +", signe == "+"),
               ("0,8 dans la prédiction", any(pv._egal(x, 0.8) for x in nombres)),
               ("8B:RIGOR, issue 2, trait", _contient(pred, "8B:RIGOR", "issue 2", "jetons_par_action_ecart_type")),
               ("banque nommée", _contient(esp, "banque-t05-v2"))],
        "T2": [("type", vue.get("type") == "question"), ("signe -", signe == "-"),
               ("0,6 dans la prédiction", any(pv._egal(x, 0.6) for x in nombres)),
               ("3B:COHERENCE, issue 0, deux traits, « diminue »",
                _contient(pred, "3B:COHERENCE", "issue 0", "actions_valides", "log_jetons_total", "diminue")),
               ("banque nommée", _contient(esp, "banque-t05-v2"))],
        "T3": [("type", vue.get("type") == "question"), ("signe +", signe == "+"),
               ("deux fois 0,40 et un écart de 0", sum(pv._egal(x, 0.4) for x in nombres) >= 2
                and any(x == 0 for x in nombres)),
               ("8B:NOVELTY, issue 1, trait", _contient(pred, "8B:NOVELTY", "issue 1", "actions_valides")),
               ("banque nommée", _contient(esp, "banque-t05-v2"))],
        "T4": [("type approche", vue.get("type") == "approche"), ("signe 0", signe == "0"),
               ("aucun nombre dans la prédiction", not nombres)],
        "T5": [("type", vue.get("type") == "question"), ("signe +", signe == "+"), ("Lean dans la métrique", _contient(met, "Lean"))],
        "T6": [("type", vue.get("type") == "question"), ("signe +", signe == "+"),
               ("3B:RIGOR, trait, « augmente »", _contient(pred, "3B:RIGOR", "log_jetons_total", "augmente")),
               ("aucun chiffre hors de « 3B:RIGOR »", not re.search(r"[0-9]", texte.replace("3B:RIGOR", "")))],
    }[t]
    ecarts = [nom for nom, ok in attendu if not ok]
    if MOTIF_ETIQUETTE_T.search(texte):
        ecarts.append("étiquette « T1 » à « T6 » dans la fiche")
    return ecarts


def verifier_registre_temoins(empreintes, registre=None):
    """CL-09 : les empreintes des six témoins scellés sont inscrites (en entier) au registre des décisions avant le lancement."""
    registre = Path(registre or (DEPOT / REGISTRE_DECISIONS))
    texte = registre.read_text(encoding="utf-8") if registre.is_file() else ""
    manquants = [t for t, e in sorted(empreintes.items()) if e["sha256"] not in texte]
    if manquants:
        raise LancementRefuse(f"empreintes des témoins absentes de {REGISTRE_DECISIONS} : {', '.join(manquants)} "
                              "(inscrire les six empreintes entières avant le lancement)")
    return True


def charger_temoins(dossier=None, valider=None, canaris=(), exiger_scelles=False):
    """Six témoins au gabarit de la course 1, validés par la vraie `ideation_v2.valider_fiche_ideation` (même validateur
    que les fiches réelles), servis sous leur forme canonique sans champs internes ; garde A4 ; longueur servie dans la
    fourchette des fiches de Fable ; aucun canari."""
    if valider is None:
        raise LancementRefuse("validateur des fiches d'idéation (v56) non fourni : aucun repli")
    dossier = dossier or TEMOINS_DOSSIER
    temoins, empreintes = {}, {}
    for k, t in enumerate(TEMOINS, 1):
        p = Path(dossier) / f"{t}.json"
        if not p.is_file():
            raise LancementRefuse(f"témoin absent : {p}")
        if exiger_scelles:  # CL-09 : témoins scellés exigés au lancement
            try:
                tf.verifier_compagnon(p)
            except tf.TirageRefuse as e:
                raise LancementRefuse(f"{t} non scellé ou modifié : {e}") from None
        brut = lire_json(p)
        if not isinstance(brut, dict) or set(brut) != set(CHAMPS_GABARIT):
            raise LancementRefuse(f"{t} : champs hors gabarit de la course 1")
        try:
            canon = valider(brut, "temoin", k, passe=1)
        except Exception as e:  # noqa: BLE001 — tout refus du validateur arrête : aucun repli
            raise LancementRefuse(f"{t} refusé par le validateur des fiches d'idéation : {e}") from None
        vue = tf.vue_anonyme(canon)
        tf.garde_a4(vue, f"le témoin {t}")
        n = tf.taille_servie(vue)
        if not LONGUEUR_SERVIE[0] <= n <= LONGUEUR_SERVIE[1]:
            raise LancementRefuse(f"{t} : longueur servie {n} hors de [{LONGUEUR_SERVIE[0]} ; {LONGUEUR_SERVIE[1]}]")
        if pv.canaris_dans(json.dumps(vue, ensure_ascii=False), canaris):
            raise LancementRefuse(f"{t} : canari d'épreuve dans le témoin")
        ecarts = controle_temoin(t, vue)
        if ecarts:
            raise LancementRefuse(f"{t} ne transcrit pas sa description : {' ; '.join(ecarts)}")
        temoins[t] = vue
        empreintes[t] = {"fichier": p.name, "sha256": tf.sha256_fichier(p), "taille_servie": n}
    return temoins, empreintes


def construire_items(ordre, fiches, temoins):
    items = []
    for k, source in enumerate(ordre, 1):
        nature = "temoin" if source in TEMOINS else "fiche"
        contenu = temoins[source] if nature == "temoin" else fiches[source]
        items.append({"item": f"item-{k:02d}", "nature": nature, "source": source, "fiche": contenu})
    return items


# --- état du tour, budget, journal ---------------------------------------------------------------------------------------

class EtatDuTour:
    def __init__(self, max_refus=MAX_REFUS, max_echecs=MAX_ECHECS):
        self._ev, self._v = threading.Event(), threading.Lock()
        self.motif, self.refus, self.echecs = None, 0, 0
        self.max_refus, self.max_echecs = max_refus, max_echecs

    def arreter(self, motif):
        with self._v:
            if self.motif is None:
                self.motif = motif
        self._ev.set()

    def arrete(self):
        return self._ev.is_set()

    def verifier(self):
        if self._ev.is_set():
            raise ArretDuTour(self.motif)

    def compter_refus(self):
        with self._v:
            self.refus += 1
            n = self.refus
        if n >= self.max_refus:
            self.arreter(f"refus : {n} refus, arrêt du tour (liste d'arrêt)")

    def compter_echec(self):
        with self._v:
            self.echecs += 1
            n = self.echecs
        if n >= self.max_echecs:
            self.arreter(f"échecs techniques : {n}, arrêt du tour (liste d'arrêt)")


class Budget:
    """Plafond cumulé : réglé + engagé + pire cas de l'appel <= plafond, sous verrou. Si l'appel ne tient pas et que rien
    n'est engagé, le plafond est atteint (arrêt du tour) ; sinon on attend le règlement des appels en cours."""

    def __init__(self, plafond, depense_initiale=0.0):
        self.plafond, self.depense, self.engage = float(plafond), float(depense_initiale), 0.0
        self._cv = threading.Condition()

    def reserver(self, montant, etat):
        with self._cv:
            while True:
                etat.verifier()
                if self.depense + self.engage + montant <= self.plafond + 1e-12:
                    self.engage += montant
                    return
                if self.engage <= 1e-12:
                    motif = (f"plafond : {self.depense:.4f} USD réglés + pire cas {montant:.4f} > {self.plafond} USD "
                             "(liste d'arrêt)")
                    etat.arreter(motif)
                    raise PlafondAtteint(motif)
                self._cv.wait(timeout=5)

    def regler(self, montant, cout):
        with self._cv:
            self.engage -= montant
            self.depense += cout
            self._cv.notify_all()
            return self.depense


class Journal:
    def __init__(self, chemin):
        self.chemin, self._v = Path(chemin), threading.Lock()

    def ajouter(self, entree):
        ligne = json.dumps(dict(entree, quand_utc=maintenant()), ensure_ascii=False, sort_keys=True)
        with self._v, open(self.chemin, "a", encoding="utf-8") as f:
            f.write(ligne + "\n")


# --- appels de modèle injectés -------------------------------------------------------------------------------------------

class Appelant:
    """Fonction texte -> texte injectée dans `traduire_fiche`. Garde de plafond avant chaque appel ; une seule reprise à
    l'identique sur un échec de transport ; refus compté (la réponse, souvent vide, va au module, qui la renvoie) ; modèle
    servi différent : réponse mise à l'écart, arrêt du tour."""

    def __init__(self, role, c, appelants, budget, etat, dossier, journal, item, preambule="", pause_reprise=PAUSE_REPRISE_S):
        self.role, self.c, self.appelants, self.modele = role, c, appelants, MODELES[role]
        self.budget, self.etat, self.dossier, self.journal, self.item = budget, etat, Path(dossier), journal, item
        self.preambule, self.pause = preambule, pause_reprise
        self.appels, self.cout, self.refus, self.statuts = 0, 0.0, None, []

    def __call__(self, texte):
        m, c = self.modele, self.c
        prompt = (self.preambule.rstrip() + "\n\n" + texte) if self.preambule else texte
        chemin_prompt = self.dossier / "prompt.txt"
        if chemin_prompt.exists():
            if chemin_prompt.read_text(encoding="utf-8") != prompt:
                raise ArretDuTour(f"{self.item} : entrée du contre-traducteur différente de celle du traducteur")
        else:
            tf.ecrire_neuf(chemin_prompt, prompt)
        for essai in (1, 2):
            self.etat.verifier()
            pire = c.cout_pire_cas(m["prix"], len(prompt), m["max_tokens"])
            self.budget.reserver(pire, self.etat)
            self.journal.ajouter({"evenement": "debut_appel", "item": self.item, "role": self.role, "essai": essai,
                                  "pire_cas_usd": round(pire, 6)})
            t0 = time.time()
            try:
                rep = self.appelants[m["fournisseur"]](m["id"], prompt, m["max_tokens"])
            except Exception as e:  # noqa: BLE001 — une exception de l'appelant est un échec de transport consigné
                rep = c.Reponse(echec=f"exception de l'appelant : {type(e).__name__} : {str(e)[:300]}")
            duree = round(time.time() - t0, 1)
            statut = "ECHEC" if rep.echec else c.statut_reponse(m["fournisseur"], rep)
            cout = pire if (rep.echec or not rep.usage) else c.cout(m["prix"], rep.usage)
            depense = self.budget.regler(pire, cout)
            self.appels += 1
            self.cout += cout
            self.statuts.append(statut)
            base = f"{self.role}.essai{essai}"
            tf.ecrire_neuf(self.dossier / f"{base}.reponse.txt", rep.texte or "")
            meta = {"role": self.role, "essai": essai, "modele_demande": m["id"], "modele_servi": rep.modele_servi,
                    "identifiant": rep.identifiant, "statut": statut, "fin": rep.fin, "categorie": rep.categorie,
                    "usage": rep.usage, "cout_usd": round(cout, 6), "pire_cas_usd": round(pire, 6),
                    "cout_compte_au_pire_cas": bool(rep.echec or not rep.usage), "echec": rep.echec, "duree_s": duree,
                    "max_tokens": m["max_tokens"], "prix": list(m["prix"]),
                    "prompt_sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
                    "reponse_sha256": hashlib.sha256((rep.texte or "").encode("utf-8")).hexdigest()}
            tf.ecrire_json_neuf(self.dossier / f"{base}.meta.json", meta)
            self.journal.ajouter({"evenement": "fin_appel", "item": self.item, "role": self.role, "essai": essai,
                                  "statut": statut, "cout_usd": round(cout, 6), "depense_cumulee_usd": round(depense, 6),
                                  "modele_servi": rep.modele_servi, "duree_s": duree})
            if cout > pire + 1e-12:  # CL-05 : la garantie du plafond ne tient plus
                self.etat.arreter(f"dépassement de réserve ({self.item}, {self.role}) : coût {cout:.6f} > pire cas "
                                  f"{pire:.6f} USD, arrêt du tour (liste d'arrêt)")
                raise ArretDuTour(self.etat.motif)
            if rep.echec:
                if "modèle servi" in rep.echec:
                    self.etat.arreter(f"modèle servi différent ({self.item}, {self.role}) : arrêt du tour")
                    raise ArretDuTour(self.etat.motif)
                if "max-appels" in rep.echec or "plafond de dépense du relais" in rep.echec:
                    self.etat.arreter(f"borne du relais atteinte ({self.item}, {self.role}) : arrêt du tour")
                    raise ArretDuTour(self.etat.motif)
                if essai == 1:
                    self.journal.ajouter({"item": self.item, "role": self.role, "reprise_a_l_identique": True,
                                          "motif": "échec de transport, aucune réponse reçue"})
                    time.sleep(self.pause)
                    continue
                raise EchecTechnique(f"{self.role} : deux échecs de transport ({rep.echec[:200]})")
            if not c.modele_conforme(m["id"], rep.modele_servi):
                self.etat.arreter(f"modèle servi différent ({self.item}, {self.role} : {rep.modele_servi!r}) : réponse "
                                  "mise à l'écart, arrêt du tour")
                raise ArretDuTour(self.etat.motif)
            if statut == "REFUS":
                self.refus = str(rep.categorie or rep.fin)
                self.etat.compter_refus()
            return rep.texte or ""
        raise AssertionError("inaccessible")


# --- un item, un tour ----------------------------------------------------------------------------------------------------

def controle_garde_reelle(resultat, garde_reelle):
    """Information (non décisive) : la proposition compilée passe-t-elle la vraie garde du noyau v56 ?"""
    fl = resultat.get("fiche_loi") or {}
    prop = fl.get("proposition")
    if garde_reelle is None or not prop:
        return "sans objet"
    try:
        garde_reelle(prop, fl["signature"]["banque"][1])
    except Exception as e:  # noqa: BLE001 — rapporté, jamais avalé en silence
        return f"refusée : {str(e)[:300]}"
    return "acceptée"


def traiter_item(item, ctx):
    dossier = Path(ctx["sortie"]) / "items" / item["item"]
    rec = {"item": item["item"], "nature": item["nature"], "source": item["source"], "debut": maintenant(),
           "fiche_sha256": pv.empreinte(item["fiche"])}
    etat = ctx["etat"]
    if etat.arrete():
        rec.update(statut="non_lance", motif=etat.motif, fin=maintenant())
        return rec
    dossier.mkdir(parents=True, exist_ok=False)
    commun = (ctx["c"], ctx["appelants"], ctx["budget"], etat, dossier, ctx["journal"], item["item"])
    trad = Appelant("traducteur", *commun, preambule=ctx["preambule"], pause_reprise=ctx["pause"])
    contre = Appelant("contre_traducteur", *commun, preambule=ctx["preambule"], pause_reprise=ctx["pause"])
    try:
        r = pv.traduire_fiche(item["fiche"], catalogue=ctx["catalogue"], noyau=ctx["noyau"], traduire=trad,
                              contre_traduire=contre, affectation=AFFECTATION, canaris=ctx["canaris"], alpha=ALPHA,
                              m=M_FICHES, politique_epreuve=POLITIQUE, garde_forme_noyau=ctx["garde_reelle"])
    except pv.LectureEpreuveInterdite as e:
        etat.arreter(f"LectureEpreuveInterdite ({item['item']}) : {e}")
        rec.update(statut="arret_lecture_epreuve", detail=str(e))
    except PlafondAtteint as e:
        rec.update(statut="interrompu_plafond", detail=str(e))
    except ArretDuTour as e:
        rec.update(statut="interrompu", detail=str(e))
    except EchecTechnique as e:
        etat.compter_echec()
        rec.update(statut="echec_technique", detail=str(e))
    except Exception as e:  # noqa: BLE001 — erreur du module : arrêt du tour, aucun repli
        etat.arreter(f"erreur du module ({item['item']}) : {type(e).__name__} : {str(e)[:200]}")
        rec.update(statut="erreur_module", detail=f"{type(e).__name__} : {e}", trace=traceback.format_exc()[-4000:])
    else:
        rec.update(statut="traite", resultat=r, garde_reelle_v56=controle_garde_reelle(r, ctx["garde_reelle"]))
        if r.get("incident"):
            etat.arreter(f"canari ({item['item']}) : {r['incident']} (liste d'arrêt)")
    rec.update(refus={a.role: a.refus for a in (trad, contre) if a.refus},
               statuts_api={a.role: a.statuts for a in (trad, contre)}, appels=trad.appels + contre.appels,
               cout_usd=round(trad.cout + contre.cout, 6), preambule=bool(ctx["preambule"]), fin=maintenant())
    tf.ecrire_json_neuf(dossier / "resultat.json", rec)
    return rec


def executer_tour(sortie, items, *, catalogue, noyau, canaris, c, appelants, plafond=PLAFOND_USD, depense_initiale=0.0,
                  preambule="", parallele=1, garde_reelle=None, pause_reprise=PAUSE_REPRISE_S):
    sortie = Path(sortie)
    (sortie / "items").mkdir(parents=True, exist_ok=False)
    etat, budget = EtatDuTour(), Budget(plafond, depense_initiale)
    ctx = {"sortie": sortie, "catalogue": catalogue, "noyau": noyau, "canaris": list(canaris), "c": c,
           "appelants": appelants, "etat": etat, "budget": budget, "journal": Journal(sortie / "journal.jsonl"),
           "preambule": preambule, "garde_reelle": garde_reelle, "pause": pause_reprise}
    if parallele <= 1:
        enregistrements = [traiter_item(it, ctx) for it in items]
    else:
        with ThreadPoolExecutor(max_workers=parallele) as pool:  # soumis dans l'ordre de passage tiré
            enregistrements = list(pool.map(lambda it: traiter_item(it, ctx), items))
    return enregistrements, etat, budget


# --- agrégat mécanique (pour le lecteur neuf ; aucune interprétation) ---------------------------------------------------

def classer(rec):
    if rec.get("statut") != "traite":
        return "non_classe"
    r = rec["resultat"]
    if r["sortie"] == pv.SORTIE_BANQUE:
        return "sortie_1"
    if r["sortie"] == pv.SORTIE_COUCHE_3:
        manque = ((r.get("traductions") or {}).get("traducteur") or {}).get("manque")
        return "sortie_1_differee" if manque == [] else "sortie_2"
    return "sortie_3"


def signature_retrouvee(signature, verite):
    if not signature or signature.get("genre") != verite["genre"]:
        return False
    attendus = {"forme": verite["forme"], "banque": ["existant", verite["banque"]],
                "moniteur": ["existant", verite["moniteur"]], "traits": [["existant", t] for t in verite["traits"]],
                "issue_visee": verite["issue_visee"], "sens": verite["sens"],
                "sous_population_visee": verite["sous_population_visee"]}
    sig = json.loads(json.dumps(signature))  # tuples -> listes, comme une fois sérialisé
    if any(sig.get(k) != v for k, v in attendus.items()):
        return False
    e, v = sig.get("effet"), verite["effet"]
    return isinstance(e, (int, float)) and e > 0 and max(e / v, v / e) <= pv.RAPPORT_EFFET_MAX


def temoin_juste(rec, verite):
    if rec is None or rec.get("statut") != "traite":
        return None
    r = rec["resultat"]
    if verite["attendu"] == "signature":
        return classer(rec) in ("sortie_1", "sortie_1_differee", "sortie_2") and \
            signature_retrouvee((r.get("fiche_loi") or {}).get("signature"), verite["signature"])
    return r["sortie"] == pv.SORTIE_RENVOI and r["renvoi"]["code"] in verite["codes"]


def fusionner(principal, reprise=None):
    par_source = {r["source"]: dict(r, tour="principal") for r in principal}
    for r in reprise or ():
        if r.get("statut") == "traite" or par_source.get(r["source"], {}).get("statut") != "traite":
            par_source[r["source"]] = dict(r, tour="reprise")
    return par_source


def agreger(par_source, verite, *, depense_usd, motifs_arret, n_fiches_attendues=M_FICHES, premier_tour=None):
    fiches = [r for s, r in sorted(par_source.items()) if s not in TEMOINS]
    traitees = [r for r in fiches if r.get("statut") == "traite"]
    classes = {}
    for r in fiches:
        classes[classer(r)] = classes.get(classer(r), 0) + 1
    famille_pont = sum(1 for r in traitees if r["resultat"]["sortie"] == pv.SORTIE_RENVOI
                       and r["resultat"]["renvoi"]["famille"] == "pont")
    codes = {}
    for r in traitees:
        if r["resultat"]["sortie"] == pv.SORTIE_RENVOI:
            codes[r["resultat"]["renvoi"]["code"]] = codes.get(r["resultat"]["renvoi"]["code"], 0) + 1
    denominateur = accords = 0
    for r in traitees:
        t = r["resultat"].get("traductions") or {}
        etats = [(t.get(k) or {}).get("etat") for k in ("traducteur", "contre_traducteur")]
        if "loi" in etats:
            denominateur += 1
            accords += bool((r["resultat"].get("comparaison") or {}).get("accord"))
    temoins = {}
    for t in TEMOINS:
        rec = par_source.get(t)
        j = temoin_juste(rec, verite[t])
        temoins[t] = {"traite": j is not None, "juste": j, "classe": classer(rec) if rec else "absent",
                      "code": ((rec or {}).get("resultat") or {}).get("renvoi", {}).get("code") if rec else None}
    traites_t = sum(v["traite"] for v in temoins.values())
    justes_t = sum(bool(v["juste"]) for v in temoins.values())
    tous = list(par_source.values())
    incidents = sum(1 for r in tous if r.get("statut") == "arret_lecture_epreuve"
                    or ((r.get("resultat") or {}).get("incident")))
    utiles = classes.get("sortie_1", 0) + classes.get("sortie_1_differee", 0) + classes.get("sortie_2", 0)
    taux = accords / denominateur if denominateur else None
    l5_borne = int(0.3 * len(traitees) + 1e-9)
    anomalies_v56 = sorted(s for s, r in par_source.items() if str(r.get("garde_reelle_v56") or "").startswith("refusée"))
    tronquees = sorted([s, role, st] for s, r in par_source.items() for role, sts in (r.get("statuts_api") or {}).items()
                       for st in sts if st in STATUTS_TRONQUES)
    criteres = {
        "L1_dents": ("non lisible (témoins non tous traités)" if traites_t < len(TEMOINS) else
                     "dents" if justes_t >= 5 and temoins["T1"]["juste"] and temoins["T2"]["juste"] else "pas de dents"),
        "L2_fidelite": ("non lisible (moins de 3 fiches traduites)" if denominateur < 3 else
                        "fidélité" if taux >= 0.6 else "ambiguïté élevée"),
        "L3_utilite": ("audit requis (proposition refusée par la vraie garde v56 : anomalie du module)" if anomalies_v56 else
                       "utile" if utiles >= 1 else ("inutile en l'état" if len(traitees) == len(fiches) == n_fiches_attendues
                                                    else "non lisible (fiches non toutes traitées)")),
        "L4_surete": "sûr" if incidents == 0 else "incident",
        "L5_defauts": ("non lisible (aucune fiche traitée)" if not traitees else
                       "conforme" if famille_pont <= l5_borne else "consigne à revoir"),
    }
    comptes_lisibles = len(traitees) == n_fiches_attendues  # CL-07
    predictions = {
        "sortie_1_differee": {"observe": classes.get("sortie_1_differee", 0), "prevu": 1, "intervalle": [0, 2]},
        "sortie_2": {"observe": classes.get("sortie_2", 0), "prevu": 3, "intervalle": [2, 5]},
        "sortie_3": {"observe": classes.get("sortie_3", 0), "prevu": 4, "intervalle": [2, 6]},
        "famille_pont": {"observe": famille_pont, "prevu_au_plus": 2},
        "accord": {"observe": taux, "prevu_au_moins": 0.6},
        "temoins_justes": {"observe": justes_t, "prevu_au_moins": 5},
    }
    lisible = {"sortie_1_differee": comptes_lisibles, "sortie_2": comptes_lisibles, "sortie_3": comptes_lisibles,
               "famille_pont": comptes_lisibles, "accord": denominateur >= 3, "temoins_justes": traites_t == len(TEMOINS)}
    for nom, p in predictions.items():
        o = p["observe"]
        p["lisible"] = lisible[nom]
        p["tenue"] = None if (o is None or not lisible[nom]) else (
            p["intervalle"][0] <= o <= p["intervalle"][1] if "intervalle" in p else
            o <= p["prevu_au_plus"] if "prevu_au_plus" in p else o >= p["prevu_au_moins"])
    entrees = [r.get("fiche_sha256") for r in tous if r.get("statut") == "traite"]
    reponses = {}
    for r in tous:
        for role in ("traducteur", "contre_traducteur"):
            h = (((r.get("resultat") or {}).get("empreintes") or {}).get(f"reponse_{role}"))
            if h:
                reponses.setdefault(role, []).append(h)
    declencheurs = {  # CL-01 : symétrie en miroir ; l'une quelconque déclenche le même audit
        "propre : 6 témoins justes sur 6": justes_t == len(TEMOINS),
        "propre : accord égal à 1,0 sur au moins 3 fiches traduites": denominateur >= 3 and accords == denominateur,
        "propre : 8 fiches traduites sur 8": denominateur == n_fiches_attendues,
        "sale : 0 témoin juste sur au moins 3 traités": traites_t >= 3 and justes_t == 0,
        "sale : accord égal à 0 sur au moins 3 fiches traduites": denominateur >= 3 and accords == 0,
        "sale : 0 fiche traduite sur au moins 6 traitées": len(traitees) >= 6 and denominateur == 0,
    }
    return {
        "version": VERSION, "fiches_attendues": n_fiches_attendues, "fiches_traitees": len(traitees),
        "classes_fiches": classes, "renvois_par_code": codes, "famille_pont": famille_pont, "borne_L5": l5_borne,
        "accord": {"accords": accords, "fiches_traduites": denominateur, "taux": taux},
        "temoins": temoins, "temoins_traites": traites_t, "temoins_justes": justes_t, "incidents": incidents,
        "refus": sum(len(r.get("refus") or {}) for r in tous),
        "echecs_techniques": sum(1 for r in tous if r.get("statut") == "echec_technique"),
        "garde_reelle_v56": {s: r.get("garde_reelle_v56") for s, r in sorted(par_source.items()) if r.get("garde_reelle_v56")},
        "anomalies_garde_reelle_v56": anomalies_v56,
        "reponses_tronquees": tronquees,
        "reformules": sorted(s for s, r in par_source.items() if r.get("tour") == "reprise"),
        "reformules_premier_tour": premier_tour or {},
        "statuts": {s: r.get("statut") for s, r in sorted(par_source.items())},
        "depense_usd": round(depense_usd, 6), "plafond_usd": PLAFOND_USD, "motifs_arret": motifs_arret,
        "criteres_mecaniques": criteres, "predictions": predictions,
        "audit_symetrie": {"declenche": any(declencheurs.values()),
                           "declencheurs": [k for k, v in declencheurs.items() if v],
                           "entrees_distinctes": len(set(entrees)), "entrees_traitees": len(entrees),
                           "reponses_distinctes": {k: [len(set(v)), len(v)] for k, v in reponses.items()}},
    }


def premier_tour_des(principal, reprise):
    """CL-04 : réponses du premier tour gardées et rapportées (jamais fusionnées) pour les passages rejoués."""
    rejoues = {r["source"] for r in reprise or ()}
    sortie = {}
    for r in principal:
        if r["source"] in rejoues:
            res = r.get("resultat") or {}
            sortie[r["source"]] = {"statut": r.get("statut"), "refus": r.get("refus"),
                                   "code": (res.get("renvoi") or {}).get("code"), "sortie": res.get("sortie")}
    return sortie


# --- vérification des sorties -------------------------------------------------------------------------------------------

def sceller_existant(chemin):
    """Compagnon `.sha256` d'un fichier fini (journal en fin de tour) ; refuse d'écraser un compagnon (R12)."""
    chemin = Path(chemin)
    with open(str(chemin) + ".sha256", "x", encoding="utf-8", newline="\n") as f:
        f.write(f"{tf.sha256_fichier(chemin)}  {chemin.name}\n")


def _utilisations_d_outils(objet, sortie):
    if isinstance(objet, dict):
        if objet.get("type") == "tool_use" and "name" in objet and isinstance(objet.get("input"), dict):
            sortie.append((str(objet["name"]), objet["input"]))
        for v in objet.values():
            _utilisations_d_outils(v, sortie)
    elif isinstance(objet, list):
        for v in objet:
            _utilisations_d_outils(v, sortie)
    return sortie


def verifier_transcription(chemin):
    """CL-09 : transcription JSONL du sous-agent metteur en forme (format de Claude Code) ; rend {"utilisations", "signalees"}.
    Permis : lire sa consigne v2 ; lire, écrire, supprimer ses témoins `temoins/T1.json` … `T6.json` ; lancer
    `lancer_epreuve_pont_v2.py verifier-temoins`. Toute autre utilisation qui touche un chemin interdit est signalée.
    Aucune utilisation d'outil lisible : refus (aucun repli)."""
    utilisations = []
    for n, ligne in enumerate(Path(chemin).read_text(encoding="utf-8").splitlines(), 1):
        if not ligne.strip():
            continue
        try:
            _utilisations_d_outils(json.loads(ligne), utilisations)
        except ValueError:
            raise LancementRefuse(f"transcription : ligne {n} illisible (JSONL attendu), aucun repli") from None
    if not utilisations:
        raise LancementRefuse("transcription : aucune utilisation d'outil trouvée, conformité non vérifiable")
    permis_lecture = re.compile(r"(consigne-metteur-en-forme-temoins-v2\.md|/temoins/T[1-6]\.json|/temoins/?)$")
    signalees = []
    for nom, entree in utilisations:
        if nom == "Bash":
            cmd = str(entree.get("command", ""))
            mauvais = [x for x in INTERDITS_TRANSCRIPTION if x in cmd]
            if "lancer_epreuve_pont_v2.py" in cmd and ("verifier-temoins" not in cmd or any(v in cmd for v in LECTURES_SHELL)):
                mauvais.append("lancer_epreuve_pont_v2.py hors de « verifier-temoins »")
            if mauvais:
                signalees.append({"outil": nom, "entree": cmd[:300], "motifs": mauvais})
            continue
        chaines = [str(v) for k, v in entree.items() if k in ("file_path", "path", "notebook_path", "pattern", "glob")]
        for s in chaines:
            touche = "epreuve-fraiche-pont" in s or any(x in s for x in INTERDITS_TRANSCRIPTION)
            if touche and not permis_lecture.search(s.rstrip()):
                signalees.append({"outil": nom, "entree": s[:300], "motifs": ["chemin interdit"]})
    return {"utilisations": len(utilisations), "signalees": signalees}


def etat_du_depot(depot=None):
    """CL-11 : commit du dépôt (refus s'il est illisible : aucun repli)."""
    depot = depot or DEPOT
    try:
        r = subprocess.run(["git", "-C", str(depot), "rev-parse", "HEAD"], capture_output=True, text=True, check=True,
                           timeout=60)
    except (OSError, subprocess.SubprocessError) as e:
        raise LancementRefuse(f"commit du dépôt illisible : {type(e).__name__}") from None
    commit = r.stdout.strip()
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise LancementRefuse(f"commit du dépôt illisible : {commit[:60]!r}")
    return commit


def environnement_run(depot=None):
    """CL-11 : versions du Python des appels et commit, à écrire et sceller dans le dossier du run."""
    executable = os.path.realpath(sys.executable)
    return {"commit_depot": etat_du_depot(depot), "python": sys.version, "executable": executable,
            "executable_sha256": tf.sha256_fichier(executable), "plateforme": platform.platform(),
            "distributions": sorted(f"{d.metadata['Name']}=={d.version}" for d in importlib.metadata.distributions()),
            "modules_charges": {"pont_v1": tf.sha256_fichier(pv.__file__), "tirage": tf.sha256_fichier(tf.__file__),
                                "lanceur": tf.sha256_fichier(__file__)}}


def appelants_reels(c):
    """CL-05 : Argon sans reprise interne (`attentes=(0,)`) ; la seule reprise est celle du lanceur, avec une nouvelle
    réservation au pire cas. Kimi : une seule tentative par appel (`appeler_kimi`), relais local."""
    return {"kimi": c.appeler_kimi, "gemini": functools.partial(c.appeler_gemini, attentes=(0,))}


def garde_preambule(texte):
    """CL-04 : refuse un préambule qui nomme une sortie, un code, un témoin ou l'épreuve."""
    trouves = [m.pattern for m in MOTIFS_PREAMBULE if m.search(texte)]
    plat = tf.normaliser_texte(texte)
    trouves += [m for m in MOTS_PREAMBULE if re.search(r"(?<![0-9a-z])" + re.escape(m), plat)]
    if trouves:
        raise LancementRefuse(f"préambule : mention interdite ({', '.join(trouves)}) ; domaine et vocabulaire seulement")
    return True


def chercher_cles(dossier, environnement=None):
    """Noms des variables de clé dont la valeur figure dans un fichier du dossier (jamais la valeur elle-même)."""
    environnement = os.environ if environnement is None else environnement
    valeurs = {n: environnement.get(n) for n in VARIABLES_CLES if environnement.get(n) and len(environnement.get(n)) >= 8}
    trouvees = set()
    for p in Path(dossier).rglob("*"):
        if p.is_file():
            octets = p.read_bytes()
            for n, v in valeurs.items():
                if v.encode("utf-8") in octets:
                    trouvees.add(n)
    return sorted(trouvees)


# --- sous-commandes -----------------------------------------------------------------------------------------------------

def preparer(pole_v56):
    """Catalogue public (description publique réelle de la banque T0.5 v2) et état du noyau (jamais servi) ; Python du
    dépôt (numpy pour le prédicteur connu). Aucune issue n'est écrite : connus ajustés sur le calibrage par le vrai code
    v56, sondes = traits du calibrage, canaris = identifiants des instances d'épreuve."""
    charger_v56(pole_v56)
    from pole import monde_banque
    chemin = Path(pole_v56) / "exemples" / f"{BANQUE}.json"
    if tf.sha256_fichier(chemin) != SHA_BANQUE:
        raise LancementRefuse(f"{BANQUE} : empreinte non conforme")
    for p in (CATALOGUE, NOYAU):
        if p.exists():
            raise LancementRefuse(f"{p.name} existe déjà (R12)")
    monde = monde_banque.MondeBanque(str(chemin), graine=GRAINE_MONDE, nul_informe=True)
    desc = monde.description_publique()
    catalogue = {"banques": {desc["nom"]: desc}, "banques_scores": {}}
    pv.garde_entree(pv.construire_entree({"essai": "catalogue"}, catalogue), ())
    connus = monde.predicteurs_connus_publics()
    lignes = monde.banque["instances"]
    noyau = {"version": "noyau-pont-t05-v2-v1", "jamais_servi": True, "banque": desc["nom"], "banque_sha256": SHA_BANQUE,
             "source": f"archive {NOM_ARCHIVE_V56} ({SHA_ARCHIVE_V56}), exemples/{BANQUE}.json",
             "graine_monde": GRAINE_MONDE, "politique_epreuve": POLITIQUE,
             "predicteurs_connus": {f"{desc['nom']}|{m}": loi for m, loi in sorted(connus.items())},
             "registre_lectures": [], "epreuves_fraiches": {desc["nom"]: False},
             "sondes": {desc["nom"]: [{"z": list(l["z"]), "g": l["g"]} for l in lignes if l.get("partie") == "calibrage"]},
             "canaris": sorted(l["identifiant"] for l in lignes if l.get("partie", "epreuve") == "epreuve")}
    h1 = tf.ecrire_neuf(CATALOGUE, json.dumps(catalogue, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    h2 = tf.ecrire_neuf(NOYAU, json.dumps(noyau, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    return {"catalogue": h1, "noyau": h2, "connus": len(connus), "moniteurs": len(desc["moniteurs"]),
            "sonde": len(noyau["sondes"][desc["nom"]]), "canaris": len(noyau["canaris"])}


def lire_fin(run):
    """Manifeste de fin d'un run ; s'il manque (processus tué, par exemple par `timeout`), il est reconstruit et marqué :
    dépense = dépense initiale + somme des coûts du journal, items sans résultat comptés « non lancés »."""
    run = Path(run)
    p = run / "manifeste-run-fin.json"
    if p.is_file():
        tf.verifier_compagnon(p)
        return lire_json(p)
    debut, journal = run / "manifeste-run.json", run / "journal.jsonl"
    if not debut.is_file():
        raise LancementRefuse(f"{run} : ni manifeste de fin ni manifeste de début : run illisible, aucun repli")
    d = lire_json(debut)
    total = float(d.get("depense_initiale_usd", 0.0))
    debuts, fins = {}, set()
    if journal.is_file():
        for ligne in journal.read_text(encoding="utf-8").splitlines():
            e = json.loads(ligne)
            cle = (e.get("item"), e.get("role"), e.get("essai"))
            if e.get("evenement") == "debut_appel":
                debuts[cle] = float(e.get("pire_cas_usd", 0.0))
            elif "cout_usd" in e:
                total += float(e["cout_usd"])
                fins.add(cle)
    en_cours = sorted(str(k) for k in debuts if k not in fins)
    total += sum(v for k, v in debuts.items() if k not in fins)  # CL-10 (a) : appel commencé sans fin, au pire cas
    return {"version": VERSION, "mode": d["mode"], "reconstruit": True, "depense_usd": round(total, 6),
            "appels_en_cours_comptes_au_pire_cas": en_cours,
            "motif_arret": "processus interrompu avant la fin (manifeste de fin absent, reconstruit)",
            "enregistrements": [{"item": o["item"], "source": o["source"], "statut": "non_lance"} for o in d["ordre"]]}


def depense_d_un_run(run):
    return float(lire_fin(run)["depense_usd"])


def preparer_reprise(precedent, items, chemin_preambule, canaris):
    """Tour neuf de la règle R-750 : une seule reformulation, depuis un run principal fini, arrêté au plus par des refus,
    qui a connu au moins un refus ; rejoue les fiches non classées ou refusées, avec le préambule scellé."""
    precedent = Path(precedent)
    fin_p = precedent / "manifeste-run-fin.json"
    if not fin_p.is_file():
        raise LancementRefuse("run précédent sans manifeste de fin : pas de reprise")
    tf.verifier_compagnon(fin_p)
    fin = lire_json(fin_p)
    if fin.get("mode") != "principal":
        raise LancementRefuse("une seule reformulation par fiche (R-750) : la reprise part d'un run principal")
    if fin.get("motif_arret") and not str(fin["motif_arret"]).startswith("refus"):
        raise LancementRefuse(f"run précédent arrêté pour une autre cause que des refus : {fin['motif_arret']}")
    if not any(r.get("refus") for r in fin["enregistrements"]):
        raise LancementRefuse("aucun refus au run précédent : pas de tour neuf (R-750)")
    if (precedent / "reprise-faite.json").exists():
        raise LancementRefuse("une reprise de ce run a déjà eu lieu : une seule reformulation par fiche (R-750)")
    a_rejouer = {r["source"] for r in fin["enregistrements"] if r.get("statut") != "traite" or r.get("refus")}
    tf.verifier_compagnon(chemin_preambule)
    preambule = Path(chemin_preambule).read_text(encoding="utf-8")
    if not preambule.strip() or pv.canaris_dans(preambule, canaris):
        raise LancementRefuse("préambule vide ou porteur d'un canari")
    tf.garde_a4(preambule, "le préambule de reformulation")
    garde_preambule(preambule)
    return [it for it in items if it["source"] in a_rejouer], preambule, depense_d_un_run(precedent)


def marquer_reprise(precedent, sortie):
    try:
        with open(Path(precedent) / "reprise-faite.json", "x", encoding="utf-8") as f:
            f.write(json.dumps({"reprise": str(sortie), "quand_utc": maintenant()}, ensure_ascii=False) + "\n")
    except FileExistsError:
        raise LancementRefuse("une reprise de ce run a déjà eu lieu : une seule reformulation par fiche (R-750)") from None


def lancer(args, *, reprise=False, appelants=None, c=None, environnement=None):
    environnement = os.environ if environnement is None else environnement
    verifier_go(environnement.get("GO_ID", ""))
    sha_prereg, pieces = verifier_pieces(PREREG, DEPOT)
    c = c or charger_collisionneur()
    appelants = appelants or appelants_reels(c)
    ideation_v2, proposeur = charger_v56(args.pole_v56)
    catalogue, noyau, canaris = charger_catalogue_noyau(CATALOGUE, NOYAU)
    fiches, ordre, manifeste_tirage = charger_fiches_tirees(TIREES)
    temoins, empreintes_temoins = charger_temoins(TEMOINS_DOSSIER, valider=ideation_v2.valider_fiche_ideation,
                                                  canaris=canaris, exiger_scelles=True)
    verifier_registre_temoins(empreintes_temoins, DEPOT / REGISTRE_DECISIONS)
    tf.verifier_compagnon(VERITE)
    verite = lire_json(VERITE)
    items = construire_items(ordre, fiches, temoins)
    depense_initiale, preambule, precedent = 0.0, "", None
    if reprise:
        precedent = Path(args.run_precedent)
        items, preambule, depense_initiale = preparer_reprise(precedent, items, args.preambule, canaris)
    sortie = Path(args.sortie)
    if (sortie / "items").exists() or (sortie / "manifeste-run.json").exists():
        raise LancementRefuse(f"{sortie} contient déjà un run (R12)")
    if reprise:
        marquer_reprise(precedent, sortie)
    env_run = environnement_run(DEPOT)  # CL-11 : avant tout appel ; refus si le commit est illisible
    sortie.mkdir(parents=True, exist_ok=True)
    h_env = tf.ecrire_json_neuf(sortie / "environnement-run.json", env_run)
    garde_reelle = fabriquer_garde_reelle(proposeur, catalogue)
    debut = {"version": VERSION, "mode": "reprise" if reprise else "principal", "go": environnement.get("GO_ID"),
             "debut": maintenant(), "preenregistrement_sha256": sha_prereg, "pieces_verifiees": pieces,
             "catalogue_sha256": tf.sha256_fichier(CATALOGUE), "noyau_sha256": tf.sha256_fichier(NOYAU),
             "verite_temoins_sha256": tf.sha256_fichier(VERITE), "tirage_manifeste_sha256":
                 tf.sha256_fichier(Path(TIREES) / tf.MANIFESTE), "temoins": empreintes_temoins,
             "modeles": MODELES, "affectation": AFFECTATION, "alpha": ALPHA, "m": M_FICHES, "politique_epreuve": POLITIQUE,
             "plafond_usd": PLAFOND_USD, "depense_initiale_usd": depense_initiale, "parallele": args.parallele,
             "consigne_traducteur_sha256": pv.empreinte(pv.CONSIGNE_TRADUCTEUR),
             "preambule_sha256": tf.sha256_fichier(args.preambule) if reprise else None,
             "run_precedent": str(precedent) if precedent else None,
             "commit_depot": env_run["commit_depot"], "environnement_sha256": h_env,
             "appel_argon": "appeler_gemini(..., attentes=(0,)) : aucune reprise interne (CL-05)",
             "ordre": [{"item": it["item"], "source": it["source"]} for it in items]}
    tf.ecrire_json_neuf(sortie / "manifeste-run.json", debut)
    recs, etat, budget = executer_tour(sortie, items, catalogue=catalogue, noyau=noyau, canaris=canaris, c=c,
                                       appelants=appelants, plafond=PLAFOND_USD, depense_initiale=depense_initiale,
                                       preambule=preambule, parallele=args.parallele, garde_reelle=garde_reelle)
    fin = {"version": VERSION, "mode": debut["mode"], "fin": maintenant(), "depense_usd": round(budget.depense, 6),
           "motif_arret": etat.motif, "refus": etat.refus, "echecs_techniques": etat.echecs,
           "enregistrements": [{k: r.get(k) for k in ("item", "source", "nature", "statut", "refus", "appels", "cout_usd")}
                               for r in recs]}
    if (sortie / "journal.jsonl").is_file():
        sceller_existant(sortie / "journal.jsonl")
    tf.ecrire_json_neuf(sortie / "manifeste-run-fin.json", fin)
    principal = lire_resultats(precedent) if reprise else recs
    par_source = fusionner(principal, recs if reprise else None)
    motifs = ([lire_json(precedent / "manifeste-run-fin.json").get("motif_arret")] if reprise else []) + [etat.motif]
    agregat = agreger(par_source, verite, depense_usd=budget.depense, motifs_arret=motifs,
                      premier_tour=premier_tour_des(principal, recs) if reprise else None)
    cles = chercher_cles(sortie, environnement)
    agregat["cles_trouvees_dans_les_sorties"] = cles
    tf.ecrire_json_neuf(sortie / ("agregat-reprise-v2.json" if reprise else "agregat-v2.json"), agregat)
    return (6 if cles else 0), agregat


def lire_resultats(run):
    recs = []
    for p in sorted((Path(run) / "items").glob("item-*/resultat.json")):
        tf.verifier_compagnon(p)
        recs.append(lire_json(p))
    fin = lire_fin(run)
    vus = {r["source"] for r in recs}
    recs += [r for r in fin["enregistrements"] if r["source"] not in vus]  # non lancés : sans dossier d'item
    return recs


def principal(argv=None):
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sous = a.add_subparsers(dest="commande", required=True)
    p = sous.add_parser("preparer")
    p.add_argument("--pole-v56", required=True)
    p = sous.add_parser("verifier-temoins")
    p.add_argument("--pole-v56", required=True)
    p = sous.add_parser("verifier-transcription")
    p.add_argument("--transcription", required=True)
    for nom in ("lancer", "reprendre-refus"):
        p = sous.add_parser(nom)
        p.add_argument("--pole-v56", required=True)
        p.add_argument("--sortie", required=True)
        p.add_argument("--parallele", type=int, default=3)
        if nom == "reprendre-refus":
            p.add_argument("--run-precedent", required=True)
            p.add_argument("--preambule", required=True)
    p = sous.add_parser("restant")
    p.add_argument("--run-precedent", required=True)
    p = sous.add_parser("agreger")
    p.add_argument("--run", required=True)
    p.add_argument("--reprise")
    args = a.parse_args(argv)
    try:
        if args.commande == "preparer":
            print(json.dumps(preparer(args.pole_v56), ensure_ascii=False))
            return 0
        if args.commande == "verifier-temoins":
            ideation_v2, _ = charger_v56(args.pole_v56)
            _, _, canaris = charger_catalogue_noyau(CATALOGUE, NOYAU)
            _, emp = charger_temoins(TEMOINS_DOSSIER, valider=ideation_v2.valider_fiche_ideation, canaris=canaris)
            print(json.dumps(emp, ensure_ascii=False, indent=1))
            return 0
        if args.commande == "verifier-transcription":
            r = verifier_transcription(args.transcription)
            print(json.dumps(r, ensure_ascii=False, indent=1))
            return 2 if r["signalees"] else 0
        if args.commande == "restant":
            print(f"{max(0.0, PLAFOND_USD - depense_d_un_run(args.run_precedent)):.4f}")
            return 0
        if args.commande == "agreger":
            fin = lire_fin(args.run)
            recs = lire_resultats(args.run)
            rep = lire_resultats(args.reprise) if args.reprise else None
            depense = depense_d_un_run(args.reprise) if args.reprise else float(fin["depense_usd"])
            motifs = [fin.get("motif_arret")] + ([lire_fin(args.reprise).get("motif_arret")] if args.reprise else [])
            tf.verifier_compagnon(VERITE)
            agregat = agreger(fusionner(recs, rep), lire_json(VERITE), depense_usd=depense, motifs_arret=motifs,
                              premier_tour=premier_tour_des(recs, rep) if rep else None)
            nom = "agregat-relu-v2.json"
            cible = Path(args.reprise or args.run) / nom
            tf.ecrire_json_neuf(cible, agregat)
            print(json.dumps(agregat["criteres_mecaniques"], ensure_ascii=False))
            return 0
        code, agregat = lancer(args, reprise=args.commande == "reprendre-refus")
        print(json.dumps({"criteres_mecaniques": agregat["criteres_mecaniques"], "depense_usd": agregat["depense_usd"],
                          "motifs_arret": agregat["motifs_arret"]}, ensure_ascii=False))
        return code
    except (LancementRefuse, tf.TirageRefuse, pv.PontErreur, FileExistsError) as e:
        print(f"REFUS : {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(principal())
