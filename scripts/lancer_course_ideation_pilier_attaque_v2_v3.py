#!/usr/bin/env python3
"""Lanceur propre de la course de l'organisme d'idéation sur la question v2 scellée du pilier attaque — version 3.

Version 3 : corrections de la contre-lecture `docs/notes/ideation-organisme-v1/contre-lecture-lanceur-course-pilier-
attaque-v2-v2-v1.md` (`4591fe97…`, R-1984), sur la version 2 (`lancer_course_ideation_pilier_attaque_v2_v2.py`
`dc743fa8…`, inchangée, R12), elle-même la voie (a) de Lazar (R-1981) :
- M1 (cache d'octets) : refus si `git status --porcelain --ignored` n'est pas vide dans le clone, ou si un `__pycache__`, un
  `.pyc` ou un `.pyo` existe sous `orchestrator/` ; la sonde, la liste blanche et la course reçoivent un préfixe de cache
  neuf hors du clone (`<dossier de sortie>/pycache`), par `-X pycache_prefix=…` sur la ligne de l'interpréteur **et**
  `PYTHONPYCACHEPREFIX` dans l'environnement. Le premier est indispensable : sous `-I` (donc `-E`), Python **ignore**
  `PYTHONPYCACHEPREFIX` (vérifié sur 3.13 : `sys.pycache_prefix` reste `None`) ; la variable ne vaut que pour les
  sous-processus Python lancés sans `-E` ;
- m1 : la passe 2 d'Argon est rapportée à son seuil réel (fiche d'Argon la plus longue ≤ 17 901 caractères, au-delà refus
  de l'orchestrateur avant envoi, dépense alors bornée à 3,35 USD) ; la « marge » de la v2 (600 000 contre 414 778) est
  retirée ;
- m2 : le plafond de la ligne de GO est lu et exigé ≥ 12 + 8 = 20 USD ;
- m3 : le juge d'Argon (bras différé) est comparé à sa propre consigne maximale, rapporté sans garde ;
- m4 : l'environnement transmis est construit par filtrage des noms, sans copie intégrale préalable ;
- m5 : interpréteur absolu `/usr/local/bin/python3` pour la sonde, la liste blanche et la course, vérifié présent et
  exécutable, et égal à l'interpréteur qui exécute le lanceur ;
- m6 : artefacts d'essai ajoutés (`tests/test_lancer_course_ideation_pilier_attaque_v2_v3.py`).

Sous GO-2026-11-08-13 (plafond 20 USD = Claude 12 + externe 8, échéance 2026-11-15) et la décision de Lazar consignée en
R-1978 (« Oui, la règle » : une règle de permission pour une seule commande exacte, celle de ce lanceur neuf). La garde
d'empreinte du crochet `.claude/hooks/garde_calcul.py` (M2) bloque cette commande si le contenu du fichier diffère de
l'empreinte épinglée.

Usage, seul et exact (aucun argument admis, cwd = racine du dépôt de travail) :

    /usr/local/bin/python3 -I -B scripts/lancer_course_ideation_pilier_attaque_v2_v3.py

Ce que fait le lanceur, dans cet ordre ; tout refus rend 2, motif sur la sortie d'erreur, rien écrit, rien appelé :
0. interpréteur : `/usr/local/bin/python3`, présent, exécutable, celui qui exécute le lanceur ;
1. aucun argument ; ligne de GO lue dans `registres/go.md` (type calcul, accordée par Lazar, dans sa période, non révoquée,
   plafond ≥ 20 USD) ;
2. orchestrateur : clone `/home/user/ideation-organism`, commit épinglé, arbre propre **fichiers ignorés compris**, aucun
   cache d'octets sous `orchestrator/`, empreintes épinglées des fichiers de la chaîne de lancement (ideation_v8 → v7 → v6
   → v5 → v4 → v2, `pole/ideation_v2.py`, `pole/adaptateurs.py`, `pole/relais.py`) — **aucune modification**, aucun
   import de l'orchestrateur dans ce processus ;
3. pièces : question v2, synthèse v2b, témoins v1, enveloppe d'Argon v5, commande d'Argon v3d, devis, sondes — empreintes
   épinglées ;
4. commande : la commande canonique de la section 5 du devis `devis-course-ideation-pilier-attaque-v2-v1.md` (`531849e3…`),
   crochets résolus (Fable acceptée à la sonde : gardée ; aucun matériau : `--seconde-passe` gardée), plus les plafonds
   externes de la section 4 du devis, réglés selon la voie (a) : contrôle externe 1,25, passe 1 d'Argon 1,70, passe 2
   d'Argon 2,30, juge d'Argon 2,5 (voir `PLAFONDS_REGLES`) ; seule option d'interpréteur ajoutée : `-X pycache_prefix=…` ;
5. garde des drapeaux interdits (contournement du bac à sable, tolérances de somme, relèvement des gardes de taille), forme
   abrégée comprise (argparse accepte les préfixes) ;
6. garde des sommes : somme des plafonds externes **strictement sous** le total externe (8,0), somme des plafonds Claude
   au plus le total Claude (12,0), calculées comme l'orchestrateur les calcule (défauts compris) ;
6 bis. gardes de taille, **par calcul** (formules de `pole/ideation_v2.py` lues dans le code, reproduites ici, rien de
   l'orchestrateur chargé) sur les tailles mesurées (`mesurer-consignes-pilier-attaque-v2-v1.json`, épinglé) : garde de
   la course (contrôle et passe 2), passe 1, passe 2 aux fiches de 8 000 caractères ; seuil de fiche de la passe 2
   rapporté ; un refus ici évite le refus de l'orchestrateur ;
7. dossiers de run et de sortie neufs (R12), préfixe de cache hors du clone ;
8. garde du bac à sable : la sonde de l'orchestrateur (`pole.adaptateurs.etat_bac_a_sable_detaille`), appelée telle
   quelle dans un processus à part, en lecture seule ; `actif` et `proc_neuf` exigés vrais ;
9. clés : décision sur les **noms** seuls ; les variables de clé présentes sont retirées de l'environnement de
   l'orchestrateur (il refuse sinon : la clé reste dans le relais) et consignées, noms seuls ; aucune valeur de clé
   écrite, transmise ni consultée ;
10. liste blanche construite par l'orchestrateur lui-même (`--construire-liste-blanche`, sans appel), vérifiée ;
11. manifeste de départ scellé (`runs/<id>/manifeste-lanceur-depart.json` et `.sha256`), course, manifeste de fin scellé.

La sortie de la course (fiches) et ses journaux vont **hors du dépôt** (`/home/user/sorties-course-ideation-pilier-attaque-
v2-v3/<id>/`) : aucune fiche ne peut entrer dans un commit par mégarde ; le manifeste du dépôt en porte les empreintes.

Bibliothèque standard seulement (le lanceur tourne sous `-I`). Les essais (`tests/test_lancer_course_ideation_pilier_attaque_
v2_v3.py`) remplacent l'orchestrateur par un faux exécutable via `Reglages` ; la ligne de commande n'expose aucun réglage.
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import os
import re
import signal
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Mapping

VERSION = "lancer_course_ideation_pilier_attaque_v2_v3"
GO_ID = "GO-2026-11-08-13"
DEPOT = Path(__file__).resolve().parents[1]

# --- orchestrateur (dépôt public lciric/ideation-organism), épinglé ------------------------------------------------------
ORCHESTRATEUR = Path("/home/user/ideation-organism/orchestrator")
COMMIT_ORCHESTRATEUR = "f39a7f4ab9e3da1e11629b1be329304cd5b8a1b0"
EMPREINTES_ORCHESTRATEUR = {
    "demonstrations/ideation_v8.py": "2e2be8d72c548e183b94c14de20c971f241f998f54f64c5281b2427fdd64e9d1",  # = devis § 6
    "demonstrations/ideation_v7.py": "7b90e65e1308b1c230b3f804743cfc42b9dc571d93b73ed6c5f3f8c9d2b481b2",
    "demonstrations/ideation_v6.py": "4c302e5b97b229d5b3edd9e9a427f1e50796c10f7081f63132165ffeef854ba4",
    "demonstrations/ideation_v5.py": "1894f250264eaaccbf891dfa255e71dc587fe415c8d21e283391203a2fe73444",
    "demonstrations/ideation_v4.py": "4212d4c9d014a265847d4c4ed87a8cd804fdafa73f85fd8947874d63fca1c36d",
    "demonstrations/ideation_v2.py": "bc5e9c98acff41b97487e2345d33768c8cdf41f0ededf8b2eed0bf842c889845",
    "pole/ideation_v2.py": "67d2ad3591b21601ece4101154138f532ba519024761beb8c9738181f8f3fefc",
    "pole/adaptateurs.py": "a1a8ede8d38884a28365ee797dcd3018dbf09ea1baefa3f57cfcb3281c529c99",
    "pole/relais.py": "b5a76343e458cf8fb91ee1928244f9cb65d50c27ab9b1bae91c21a5c82349da3",
}
LANCEUR_ORCHESTRATEUR = "demonstrations/ideation_v8.py"

# --- pièces (dépôt de travail ; branche rapports/fille-ideation-1-v1 pour celles qui n'ont pas encore rejoint main) ------
PIECES = {
    "question": ("docs/notes/ideation-pilier-attaque-v1/question-remue-meninges-pilier-attaque-v2.md",
                 "2dbad4b75d20fadc3147be9eff07f2e77c2f82fe4f609ab1c29388ab46c4bb42"),
    "synthese": ("rapports/fille-ideation-1-v1/synthese-anteriorite-pilier-attaque-v2b.md",
                 "b828d800913c8960d04b6822de8f10fc51ee573c660c84f6658ea6ba68796b8d"),
    "temoins": ("docs/notes/ideation-pilier-attaque-v1/organisme-v1/temoins-pilier-attaque-v1.json",
                "7db0d82b624a2bf3c689be8197abbd0ec831bca5ba4b6e936cfe445efed13505"),
    "enveloppe_argon": ("rapports/fille-ideation-1-v1/appel-argon-v5.sh",
                        "37c0205e26f83cbdcdf5ad7f1e4094a21c7dcc70afb72d15ef0d260a770a132a"),
    "commande_argon": ("docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py",
                       "46c91df41b77a6d4cb7f5141993fda4a894118b5dd4ad1e5ba21a17dc2d67e46"),
    "devis": ("rapports/fille-ideation-1-v1/devis-course-ideation-pilier-attaque-v2-v1.md",
              "531849e3e4f55de3ae5f097033fdcb50bd209ac88670547b3060fb869b10eea3"),
    "sonde_claude": ("rapports/fille-ideation-1-v1/sonde-garde-claude-seule-v2-v1.json",
                     "b1ed4f2b2431a28d173578bade715487f1927108a390ba1f49ed4fcda918bed2"),
    "sonde_argon": ("rapports/fille-ideation-1-v1/sonde-garde-argon-v2-v1.json",
                    "6ec1efc574216e8a7f9b84886c5c60c8726a29e7ee400702cef3f42e5f648551"),
    "mesure_consignes": ("rapports/fille-ideation-1-v1/mesurer-consignes-pilier-attaque-v2-v1.json",
                         "db44b41efb40ab841eb22895677e2efe4cf2e1975b944c5133a1eb9f47ac0a85"),
}
# l'enveloppe d'Argon v5 lit commande_argon_v3d.py sous DEPOT_TRAVAIL, défaut /home/user/controle-ia-travail, et
# l'orchestrateur ne lui transmet pas cette variable : le dépôt doit être à cet endroit
DEPOT_ATTENDU_PAR_L_ENVELOPPE = Path("/home/user/controle-ia-travail")

# --- totaux et plafonds (devis § 4 ; GO-2026-11-08-13) ------------------------------------------------------------------
TOTAL_CLAUDE_USD = 12.0
TOTAL_EXTERNE_USD = 8.0
PLAFONDS_DEVIS = {
    "proposeur_ideation|claude-opus-5-5": 2.0,
    "proposeur_ideation|claude-fable-5-1": 2.0,
    "juge_ideation|claude-opus-5-5": 1.5,
    "proposeur_ideation|gemini-4-argon": 2.0,   # devis : par passe, deux passes
    "juge_ideation|gemini-4-argon": 2.5,
}
CONTROLE_EXTERNE_DEVIS_USD = 1.35
# Voie (a), R-1981 : passe 1 d'Argon ≤ 1,70, passe 2 ≥ 2,25, somme externe strictement sous 8,0.
# Retenu : contrôle externe 1,25 ; passe 1 1,70 (`proposeur_ideation|gemini-4-argon`) ; passe 2 2,30
# (`--budget-passe-2-externe-usd`) ; juge d'Argon 2,5 (inchangé) ; contrôle du bras 0,2 (défaut de l'orchestrateur).
# Somme externe : 1,25 + 1,70 + 2,30 + 2,5 + 0,2 = 7,95 < 8,0. Gardes (prix prudent 2,5e-6 USD par caractère) :
# course min(1,25 → 500 000 ; 2,30 → 920 000 − 480 000 = 440 000) = 440 000 ≥ 415 253 (marge 24 747) ; passe 1
# 1,70 → 680 000 − 320 000 = 360 000 ≥ 60 637 (marge 299 363) ; passe 2 (m1 de la contre-lecture `4591fe97…`) : avec
# des fiches de passe 1 de f caractères, l'orchestrateur compare une consigne ≈ 60 637 + 8 × (f + 9) à
# 920 000 − 8 × max(8 000, f) × 5 ; aux fiches de 8 000 : ≈ 124 709 contre 600 000 ; seuil f ≤ ⌊(920 000 − 60 637 − 72)
# / 48⌋ = 17 901 caractères ; au-delà, refus de l'orchestrateur avant l'envoi de la passe 2, dépense alors au plus
# contrôle externe 1,25 + contrôles Claude 2 × 0,2 + passe 1 d'Argon 1,70 = 3,35 USD (Argon joue ses deux passes avant
# les proposeurs Claude). Passe 2 à 2,25 laisserait 4 747 caractères de marge à la garde de la course (1,1 %) : 2,30.
PLAFONDS_REGLES = dict(PLAFONDS_DEVIS, **{"proposeur_ideation|gemini-4-argon": 1.70})
PASSE_2_EXTERNE_USD = 2.30
CONTROLE_EXTERNE_USD = 1.25
PLAFOND_REDUIT = {"voie": "(a), R-1981",
                  "controle_externe": {"option": "--budget-controle-externe-usd", "devis_usd": CONTROLE_EXTERNE_DEVIS_USD,
                                       "lanceur_usd": CONTROLE_EXTERNE_USD},
                  "passe_1_argon": {"option": "--budget proposeur_ideation|gemini-4-argon", "devis_usd": 2.0, "lanceur_usd": 1.70},
                  "passe_2_argon": {"option": "--budget-passe-2-externe-usd", "devis_usd": 2.0, "lanceur_usd": PASSE_2_EXTERNE_USD}}
# Gardes de taille de `pole/ideation_v2.py` (commit épinglé), reproduites par calcul :
#   taille_max_consigne_par_defaut(p, prov) = max(0, int(p / PRIX + 1e-6) − prov)
#   course : min(contrôle, passe 2 − provision_sortie_caracteres(8) = 8 × 12 000 × 5)  [CL42-01, CL43-01]
#   passe n : plafond de la passe − 8 × max(8 000, plus grande fiche admise) × 5         [CL43-02]
PRIX_CARACTERE_PRUDENT_USD = 10.0 / 1e6 / 4    # `--prix-entree-usd-par-million-jetons` 10 (défaut), 4 caractères par jeton
PROVISION_SORTIE_PAR_FICHE = 12_000
TAILLE_FICHE_PROVISIONNEE_PASSE = 8_000
RAPPORT_SORTIE_ENTREE = 5
# consigne de passe 2 ≈ consigne de passe 1 + nombre × (fiche + 9) : estimation de la contre-lecture (`4591fe97…`, m1),
# le « + 9 » étant l'enrobage par fiche servie ; sert au seuil rapporté, non à une garde de l'orchestrateur
ENROBAGE_PAR_FICHE_PASSE_2 = 9
PROVISION_SORTIE_PAR_NOTE = 2_000
CONTROLE_CLAUDE_ET_BRAS_DEFAUT_USD = 0.2   # orchestrateur : `--budget-controle-usd` absent → 0,2
DEFAUT_EXTERNE_PROPOSEUR_USD = 2.5         # orchestrateur : BUDGET_EXTERNE_PROPOSEUR
DEFAUT_EXTERNE_JUGE_USD = 3.5              # orchestrateur : BUDGET_EXTERNE_JUGE
DEFAUT_CONTROLE_EXTERNE_USD = 2.5          # orchestrateur : `--budget-controle-externe-usd` absent
DEFAUTS_CLAUDE = {"proposeur_ideation|claude-opus-5-5": 5.0, "proposeur_ideation|claude-fable-5-1": 9.3,
                  "juge_ideation|claude-opus-5-5": 4.0, "juge_ideation|claude-fable-5-1": 7.0}
PORT_RELAIS_CLAUDE = 8787
DOSSIER_SORTIES = Path("/home/user/sorties-course-ideation-pilier-attaque-v2-v3")
# m5 : l'interpréteur pour lequel le kit `claude-agent-sdk` est installé, celui qu'appelle l'enveloppe d'Argon v5 ; jamais
# celui du `PATH`
PYTHON_COURSE = "/usr/local/bin/python3"
# M1 : préfixe du cache d'octets, sous le dossier de sortie (neuf, hors du clone)
NOM_DOSSIER_PYCACHE = "pycache"

# --- drapeaux interdits (jamais dans la commande, même abrégés) -----------------------------------------------------------
DRAPEAUX_INTERDITS = (
    "--accepter-sans-bac-a-sable", "--motif-sans-bac-a-sable",
    "--tolerer-somme-plafonds", "--tolerer-somme-plafonds-claude", "--tolerer-somme-plafonds-externe",
    "--taille-max-consigne-externe", "--taille-max-consigne-externe-bras", "--prix-entree-usd-par-million-jetons",
)

# --- noms de variables de clé (ceux de l'orchestrateur, `pole/relais.py` épinglé, plus un motif large) ---------------------
NOMS_DE_CLE = ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "CLAUDE_CODE_OAUTH_TOKEN", "OPENAI_API_KEY", "GOOGLE_API_KEY",
               "GEMINI_API_KEY", "AWS_SECRET_ACCESS_KEY", "AWS_SESSION_TOKEN", "GITHUB_TOKEN", "GH_TOKEN", "HF_TOKEN")
MOTIF_NOM_DE_CLE = re.compile(r"(API_?KEY|TOKEN|SECRET|PASSWORD|PASSWD|CREDENTIAL)", re.I)

SONDE_BAC_A_SABLE = (
    "import json, sys\n"
    "sys.path.insert(0, sys.argv[1])\n"
    "from pole.adaptateurs import etat_bac_a_sable_detaille\n"
    "print(json.dumps(etat_bac_a_sable_detaille()))\n"
)


class Refus(RuntimeError):
    """Garde du lanceur : rien n'est lancé."""


def sha256_fichier(chemin: Path) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def date_u() -> str:
    """L'équivalent de `"$(date -u)"` de la commande canonique."""
    r = subprocess.run(["date", "-u"], capture_output=True, text=True, timeout=10)
    if r.returncode != 0 or not r.stdout.strip():
        raise Refus("`date -u` illisible : horodatage exigé par la commande canonique")
    return r.stdout.strip()


@dataclass
class Reglages:
    """Tout ce que le lanceur lit ou écrit. La ligne de commande n'en expose aucun : `production()` seul y sert."""
    depot: Path
    orchestrateur: Path
    commit_orchestrateur: str
    empreintes_orchestrateur: dict
    pieces: dict
    registre_go: Path
    dossier_runs: Path
    dossier_sorties: Path
    depot_attendu_par_l_enveloppe: Path
    python: str
    plafonds: dict = field(default_factory=lambda: dict(PLAFONDS_REGLES))
    controle_externe_usd: float = CONTROLE_EXTERNE_USD
    passe_2_externe_usd: float = PASSE_2_EXTERNE_USD
    arguments_en_plus: tuple = ()          # vide en production ; les essais y glissent des artefacts
    environnement: Mapping | None = None   # None : os.environ (lu par noms, jamais copié en entier)
    aujourd_hui: _dt.date | None = None    # None : date du jour (UTC)
    horodatage: object = date_u            # callable → texte

    @classmethod
    def production(cls) -> "Reglages":
        return cls(depot=DEPOT, orchestrateur=ORCHESTRATEUR, commit_orchestrateur=COMMIT_ORCHESTRATEUR,
                   empreintes_orchestrateur=dict(EMPREINTES_ORCHESTRATEUR), pieces=dict(PIECES),
                   registre_go=DEPOT / "registres" / "go.md", dossier_runs=DEPOT / "runs", dossier_sorties=DOSSIER_SORTIES,
                   depot_attendu_par_l_enveloppe=DEPOT_ATTENDU_PAR_L_ENVELOPPE, python=PYTHON_COURSE)


# ======================================================================================================================
# gardes
# ======================================================================================================================

def lire_plafond_go(texte: str) -> float:
    """« 20 USD » → 20.0 ; tout autre forme est illisible (m2 : aucun repli silencieux)."""
    m = re.fullmatch(r"\s*(\d+(?:[.,]\d+)?)\s*USD\s*", texte)
    if not m:
        raise Refus(f"plafond du GO illisible : {texte!r} (forme « <nombre> USD » exigée)")
    return float(m.group(1).replace(",", "."))


def verifier_go(registre: Path, aujourd_hui: _dt.date, go_id: str = GO_ID) -> dict:
    """La ligne `go_id` du registre : une seule (hors extensions), 8 colonnes, type calcul, accordée par Lazar, dans sa
    période, non révoquée (ligne de type « révocation » qui la cite), plafond lu ≥ total Claude + total externe (m2)."""
    if not registre.is_file():
        raise Refus(f"registre des GO absent : {registre}")
    lignes = registre.read_text(encoding="utf-8").splitlines()
    ligne_go = re.compile(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2})\s*\|")
    trouvees, revocations = [], []
    for ligne in lignes:
        m = ligne_go.match(ligne)
        if not m:
            continue
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if m.group(1) == go_id:
            trouvees.append(cellules)
        elif len(cellules) == 8 and cellules[2] == "révocation" and (go_id in cellules[3] or go_id in cellules[7]):
            revocations.append(m.group(1))
    principales = [c for c in trouvees if not (len(c) == 8 and c[3].lower().startswith("extension"))]
    if len(principales) != 1:
        raise Refus(f"{go_id} : {len(principales)} ligne(s) principale(s) dans {registre.name} (une exigée)")
    c = principales[0]
    if len(c) != 8:
        raise Refus(f"{go_id} : ligne mal formée ({len(c)} colonnes, 8 attendues)")
    ident, accorde, typ, perimetre, plafond, echeance, par, ref = c
    if typ != "calcul":
        raise Refus(f"{go_id} : type {typ!r}, « calcul » exigé")
    if par != "Lazar":
        raise Refus(f"{go_id} : accordé par {par!r}, Lazar exigé")
    try:
        d_acc, d_ech = _dt.date.fromisoformat(accorde), _dt.date.fromisoformat(echeance)
    except ValueError:
        raise Refus(f"{go_id} : dates illisibles ({accorde!r}, {echeance!r})") from None
    if not d_acc <= aujourd_hui <= d_ech:
        raise Refus(f"{go_id} hors de sa période de validité ({d_acc} → {d_ech}, aujourd'hui {aujourd_hui})")
    if revocations:
        raise Refus(f"{go_id} révoqué par {', '.join(sorted(revocations))}")
    if "organisme d'idéation" not in perimetre.lower() or "question v2" not in perimetre.lower():
        raise Refus(f"{go_id} : périmètre sans « organisme d'idéation » ni « question v2 » — ce n'est pas le GO de cette course")
    plafond_usd = lire_plafond_go(plafond)
    if plafond_usd < TOTAL_CLAUDE_USD + TOTAL_EXTERNE_USD:
        raise Refus(f"{go_id} : plafond {plafond_usd} USD sous les totaux transmis "
                    f"{TOTAL_CLAUDE_USD} + {TOTAL_EXTERNE_USD} = {TOTAL_CLAUDE_USD + TOTAL_EXTERNE_USD} USD")
    return {"id": ident, "accorde": accorde, "echeance": echeance, "plafond": plafond, "plafond_usd": plafond_usd,
            "par": par,
            "ligne_sha256": hashlib.sha256(("|".join(c)).encode("utf-8")).hexdigest()}


def verifier_interprete(r: Reglages) -> dict:
    """m5 : interpréteur absolu, présent, exécutable, et celui qui exécute ce lanceur (la commande permise le nomme)."""
    p = Path(r.python)
    if not p.is_absolute():
        raise Refus(f"interpréteur {r.python!r} non absolu : {PYTHON_COURSE} exigé, jamais le `PATH`")
    if not (p.is_file() and os.access(p, os.X_OK)):
        raise Refus(f"interpréteur {r.python} absent ou non exécutable")
    if os.path.abspath(sys.executable) != os.path.abspath(r.python):
        raise Refus(f"lanceur exécuté par {sys.executable}, la course le serait par {r.python} : un seul interpréteur admis")
    return {"chemin": r.python, "resolu": os.path.realpath(r.python), "version": sys.version.split()[0]}


def _git(dossier: Path, *args: str) -> str:
    r = subprocess.run(["git", "-C", str(dossier), *args], capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        raise Refus(f"git {' '.join(args)} dans {dossier} : code {r.returncode} ({r.stderr.strip()[:200]})")
    return r.stdout


def caches_d_octets(racine: Path) -> list:
    """M1 : tout `__pycache__`, `.pyc` ou `.pyo` sous `racine` (Python lirait ces octets à la place des sources)."""
    trouves = []
    for dossier, sous_dossiers, fichiers in os.walk(racine):
        if ".git" in sous_dossiers:
            sous_dossiers.remove(".git")
        for d in sous_dossiers:
            if d == "__pycache__":
                trouves.append(os.path.join(dossier, d))
        for f in fichiers:
            if f.endswith((".pyc", ".pyo")):
                trouves.append(os.path.join(dossier, f))
    return sorted(trouves)


def verifier_orchestrateur(r: Reglages) -> dict:
    """Clone au commit épinglé, arbre propre fichiers ignorés compris (aucun fichier modifié, ajouté ni ignoré), aucun
    cache d'octets sous l'orchestrateur, empreintes épinglées : aucune modification."""
    if not (r.orchestrateur / LANCEUR_ORCHESTRATEUR).is_file():
        raise Refus(f"orchestrateur absent : {r.orchestrateur / LANCEUR_ORCHESTRATEUR}")
    tete = _git(r.orchestrateur, "rev-parse", "HEAD").strip()
    if tete != r.commit_orchestrateur:
        raise Refus(f"orchestrateur au commit {tete}, {r.commit_orchestrateur} exigé")
    sale = _git(r.orchestrateur, "status", "--porcelain").strip()
    if sale:
        raise Refus("orchestrateur modifié (git status non vide) : aucune modification admise\n" + sale[:1000])
    ignores = _git(r.orchestrateur, "status", "--porcelain", "--ignored").strip()
    if ignores:
        raise Refus("clone de l'orchestrateur avec fichiers ignorés (git status --porcelain --ignored non vide : un cache "
                    "d'octets ou tout autre fichier hors du commit) : aucun admis\n" + ignores[:1000])
    caches = caches_d_octets(r.orchestrateur)
    if caches:
        raise Refus("cache d'octets sous l'orchestrateur (lu à la place des sources empreintées) : " + json.dumps(caches[:20]))
    ecarts = {}
    for rel, attendu in sorted(r.empreintes_orchestrateur.items()):
        p = r.orchestrateur / rel
        lu = sha256_fichier(p) if p.is_file() else None
        if lu != attendu:
            ecarts[rel] = lu
    if ecarts:
        raise Refus(f"orchestrateur : empreintes différentes ou fichiers absents : {ecarts}")
    racine_clone = Path(_git(r.orchestrateur, "rev-parse", "--show-toplevel").strip())
    return {"chemin": str(r.orchestrateur), "racine_clone": str(racine_clone), "commit": tete,
            "empreintes": dict(r.empreintes_orchestrateur), "fichiers_ignores": [], "caches_d_octets": []}


def options_interprete(prefixe_pycache: Path) -> list:
    """`-I -B` et le préfixe du cache d'octets (M1) : `-X pycache_prefix` tient sous `-I`, la variable d'environnement non."""
    return ["-I", "-B", "-X", f"pycache_prefix={prefixe_pycache}"]


def verifier_prefixe_pycache(prefixe: Path, racine_clone: Path) -> None:
    """M1 : préfixe neuf (absent), absolu, hors du clone."""
    if not prefixe.is_absolute():
        raise Refus(f"préfixe du cache d'octets non absolu : {prefixe}")
    if prefixe.exists():
        raise Refus(f"préfixe du cache d'octets déjà présent : {prefixe} (un dossier neuf est exigé)")
    p, c = Path(os.path.realpath(prefixe)), Path(os.path.realpath(racine_clone))
    if p == c or c in p.parents:
        raise Refus(f"préfixe du cache d'octets {prefixe} dans le clone {racine_clone}")


def verifier_pieces(r: Reglages) -> dict:
    if r.depot.resolve() != r.depot_attendu_par_l_enveloppe.resolve():
        raise Refus(f"dépôt de travail en {r.depot}, l'enveloppe d'Argon v5 attend {r.depot_attendu_par_l_enveloppe}")
    lues, ecarts = {}, {}
    for nom, (rel, attendu) in sorted(r.pieces.items()):
        p = r.depot / rel
        lu = sha256_fichier(p) if p.is_file() else None
        if lu != attendu:
            ecarts[nom] = {"chemin": rel, "attendu": attendu, "lu": lu}
        lues[nom] = {"chemin": rel, "sha256": attendu}
    if ecarts:
        raise Refus("pièces absentes ou d'empreinte différente (R11 : vérifiées sur disque et par empreinte) : "
                    + json.dumps(ecarts, ensure_ascii=False))
    return lues


def commande_course(r: Reglages, sortie: Path, liste_blanche: Path, horodatage: str, prefixe_pycache: Path) -> list:
    """La commande canonique du devis (§ 5, point 2), crochets résolus, plus les plafonds externes du § 4 (contrôle réduit) ;
    seule option d'interpréteur ajoutée : le préfixe du cache d'octets (M1)."""
    p = {nom: str(r.depot / rel) for nom, (rel, _) in r.pieces.items()}
    for nom in ("question", "synthese", "temoins", "enveloppe_argon"):
        if any(ch.isspace() for ch in p[nom]):
            raise Refus(f"chemin avec espace ({nom}) : la commande externe est découpée par l'orchestrateur")
    b = r.plafonds
    argv = [
        r.python, *options_interprete(prefixe_pycache), LANCEUR_ORCHESTRATEUR, str(sortie),
        "--liste-blanche", str(liste_blanche),
        "--question", p["question"],
        "--piece", p["synthese"],
        "--piece-juge", p["synthese"],
        "--temoins", p["temoins"],
        "--proposeur", "opus=claude-opus-5-5",
        "--proposeur", "fable=claude-fable-5-1",           # Fable acceptée à la sonde garde v2 (b5b198d1)
        "--proposeur-externe", "argon=gemini-4-argon",
        "--commande-externe", "bash " + p["enveloppe_argon"],
        "--juge", "opus-juge=claude-opus-5-5",
        "--juge-externe", "argon-juge=gemini-4-argon",
        "--seconde-passe",                                  # aucun matériau : aucune attestation de matériau exigée
        "--nombre", "8",
        "--budget-total-usd", _usd(TOTAL_CLAUDE_USD),
        "--budget-externe-usd", _usd(TOTAL_EXTERNE_USD),
        "--budget", f"proposeur_ideation|claude-opus-5-5={_usd(b['proposeur_ideation|claude-opus-5-5'])}",
        "--budget", f"proposeur_ideation|claude-fable-5-1={_usd(b['proposeur_ideation|claude-fable-5-1'])}",
        "--budget", f"juge_ideation|claude-opus-5-5={_usd(b['juge_ideation|claude-opus-5-5'])}",
        # devis § 4 : plafonds externes (sans eux, les défauts de l'orchestrateur font 11,20 > 8,0)
        "--budget", f"proposeur_ideation|gemini-4-argon={_usd(b['proposeur_ideation|gemini-4-argon'])}",
        "--budget", f"juge_ideation|gemini-4-argon={_usd(b['juge_ideation|gemini-4-argon'])}",
        "--budget-controle-externe-usd", _usd(r.controle_externe_usd),
        "--budget-passe-2-externe-usd", _usd(r.passe_2_externe_usd),       # voie (a), R-1981
        "--moteur", "claude-sdk",
        "--url-relais", f"http://127.0.0.1:{PORT_RELAIS_CLAUDE}",
        "--confirmer-moteur-reel",
        "--horodatage", horodatage,
    ]
    return argv + list(r.arguments_en_plus)


def _usd(x: float) -> str:
    return repr(float(x))


def garde_drapeaux(argv: list) -> None:
    """Refus si un drapeau interdit figure dans la commande, en entier, abrégé (préfixe admis par argparse) ou `=valeur`."""
    trouves = []
    for jeton in argv:
        if not isinstance(jeton, str) or not jeton.startswith("--") or len(jeton) <= 2:
            continue
        nom = jeton.split("=", 1)[0]
        if any(f == nom or f.startswith(nom) for f in DRAPEAUX_INTERDITS):
            trouves.append(jeton)
    if trouves:
        raise Refus(f"drapeau(x) interdit(s) dans la commande : {trouves} (contournement du bac à sable, tolérance de somme "
                    "ou relèvement d'une garde de taille : jamais dans ce lanceur)")


def _valeurs(argv: list, option: str) -> list:
    out = []
    for i, jeton in enumerate(argv):
        if jeton == option and i + 1 < len(argv):
            out.append(argv[i + 1])
        elif isinstance(jeton, str) and jeton.startswith(option + "="):
            out.append(jeton.split("=", 1)[1])
    return out


def _une(argv: list, option: str, defaut: float | None) -> float | None:
    v = _valeurs(argv, option)
    if len(v) > 1:
        raise Refus(f"{option} donné {len(v)} fois")
    return float(v[0]) if v else defaut


def sommes_plafonds(argv: list) -> dict:
    """Les deux sommes, comme l'orchestrateur les calcule avant tout appel (`verifier_reglages`, CL37-03, CL43-01), défauts
    de l'orchestrateur compris quand une option manque."""
    budgets = dict(DEFAUTS_CLAUDE)
    prop = [v.split("=", 1)[1] for v in _valeurs(argv, "--proposeur")]
    juges = [v.split("=", 1)[1] for v in _valeurs(argv, "--juge")]
    prop_ext = [v.split("=", 1)[1] for v in _valeurs(argv, "--proposeur-externe")]
    juges_ext = [v.split("=", 1)[1] for v in _valeurs(argv, "--juge-externe")]
    for m in juges_ext:
        budgets.setdefault(f"juge_ideation|{m}", DEFAUT_EXTERNE_JUGE_USD)
    for m in prop_ext:
        budgets.setdefault(f"proposeur_ideation|{m}", DEFAUT_EXTERNE_PROPOSEUR_USD)
    for v in _valeurs(argv, "--budget"):
        cle, valeur = v.split("=", 1)
        role, modele = cle.split("|", 1)
        budgets[f"{role.strip()}|{modele.strip()}"] = float(valeur)
    passes = 2 if "--seconde-passe" in argv else 1
    controle = _une(argv, "--budget-controle-usd", CONTROLE_CLAUDE_ET_BRAS_DEFAUT_USD)
    controle_ext = _une(argv, "--budget-controle-externe-usd", DEFAUT_CONTROLE_EXTERNE_USD)
    passe_2 = _une(argv, "--budget-passe-2-externe-usd", None)
    total_claude = _une(argv, "--budget-total-usd", 40.0)
    total_externe = _une(argv, "--budget-externe-usd", 11.6)
    modeles_claude = sorted(set(prop) | set(juges))
    somme_claude = controle * len(modeles_claude) + passes * sum(budgets[f"proposeur_ideation|{m}"] for m in prop) \
        + sum(budgets[f"juge_ideation|{m}"] for m in juges)
    somme_externe = controle_ext * len(prop_ext) \
        + sum((passe_2 if (n == 2 and passe_2 is not None) else budgets[f"proposeur_ideation|{m}"])
              for m in prop_ext for n in range(1, passes + 1)) \
        + sum(budgets[f"juge_ideation|{m}"] for m in juges_ext) + controle * len(juges_ext)
    return {"somme_claude": round(somme_claude, 6), "total_claude": total_claude,
            "somme_externe": round(somme_externe, 6), "total_externe": total_externe,
            "detail_externe": {"controle_externe": controle_ext, "passes": passes,
                               "proposeurs_externes": {m: budgets[f"proposeur_ideation|{m}"] for m in prop_ext},
                               "juges_externes": {m: budgets[f"juge_ideation|{m}"] for m in juges_ext},
                               "controle_du_bras": controle},
            "detail_claude": {"controle": controle, "modeles": modeles_claude}}


def garde_sommes(argv: list) -> dict:
    s = sommes_plafonds(argv)
    if s["total_externe"] != TOTAL_EXTERNE_USD or s["total_claude"] != TOTAL_CLAUDE_USD:
        raise Refus(f"totaux {s['total_claude']} + {s['total_externe']} ≠ {TOTAL_CLAUDE_USD} + {TOTAL_EXTERNE_USD} du GO")
    if not s["somme_externe"] < s["total_externe"]:
        raise Refus(f"somme des plafonds externes {s['somme_externe']:.2f} pas sous le total externe {s['total_externe']} : "
                    "réduire un plafond (jamais --tolerer-somme-plafonds-externe)")
    if s["somme_claude"] > s["total_claude"]:
        raise Refus(f"somme des plafonds Claude {s['somme_claude']:.2f} > total Claude {s['total_claude']}")
    return s


def taille_max(plafond_usd: float, provision: int = 0, prix: float = PRIX_CARACTERE_PRUDENT_USD) -> int:
    """`taille_max_consigne_par_defaut` de l'orchestrateur, recalculée (aucun import)."""
    return max(0, int(float(plafond_usd) / prix + 1e-6) - int(provision))


def seuil_fiche_passe_2(taille_max_passe_2_sans_provision: int, consigne_passe_1: int, nombre: int) -> int:
    """m1 : plus longue fiche de passe 1 (caractères) pour laquelle la consigne de passe 2, ≈ consigne_passe_1 + nombre ×
    (f + 9), tient sous taille_max(p2, 0) − nombre × f × 5 (cas f ≥ 8 000). Valeur de la contre-lecture : 17 901."""
    return (taille_max_passe_2_sans_provision - consigne_passe_1 - ENROBAGE_PAR_FICHE_PASSE_2 * nombre) \
        // (nombre * (1 + RAPPORT_SORTIE_ENTREE))


def garde_tailles(r: Reglages, argv: list) -> dict:
    """Gardes de taille de la course, par calcul, sur les tailles mesurées (pièce épinglée `mesure_consignes`) : garde de la
    course (consigne de contrôle d'Argon), passe 1 (sa consigne), passe 2 aux fiches de 8 000 caractères (consigne de passe
    2 estimée à ces fiches). Rend chaque garde et sa marge ; refus si l'une ne tient pas. Rapporte, sans garde : le seuil de
    fiche de la passe 2 (m1) et la dépense au plus si l'orchestrateur la refuse ; le juge d'Argon (bras différé,
    invocation à part) contre sa propre consigne maximale (m3)."""
    mesure = json.loads((r.depot / r.pieces["mesure_consignes"][0]).read_text(encoding="utf-8"))
    c = mesure.get("consignes") or {}
    try:
        controle, passe_1, passe_2_max = (int(c["consigne_de_controle_externe"]), int(c["consigne_passe_1"]),
                                          int(c["consigne_passe_2_maximale"]))
        nombre, fiches_juge = int(c["nombre_par_proposeur"]), int(c["fiches_au_juge_au_maximum"])
        juge_max = int(c["consigne_du_juge_maximale"])
    except (KeyError, TypeError, ValueError):
        raise Refus("mesure des consignes illisible : tailles absentes") from None
    if mesure.get("prix_entree_usd_par_million_jetons") != 10.0:
        raise Refus("mesure des consignes à un autre prix que le prix prudent (10)")
    s = sommes_plafonds(argv)
    if s["detail_externe"]["passes"] != 2 or nombre != int(_une(argv, "--nombre", 8)):
        raise Refus("gardes de taille calculées pour deux passes et --nombre de la mesure")
    (modele,) = s["detail_externe"]["proposeurs_externes"]
    p1 = s["detail_externe"]["proposeurs_externes"][modele]
    p2 = _une(argv, "--budget-passe-2-externe-usd", None)
    p2 = p1 if p2 is None else p2
    ctrl = s["detail_externe"]["controle_externe"]
    (juge,) = s["detail_externe"]["juges_externes"].values()
    prov_course = nombre * PROVISION_SORTIE_PAR_FICHE * RAPPORT_SORTIE_ENTREE
    prov_passe = nombre * TAILLE_FICHE_PROVISIONNEE_PASSE * RAPPORT_SORTIE_ENTREE
    consigne_p2_fiches_8000 = passe_1 + nombre * (TAILLE_FICHE_PROVISIONNEE_PASSE + ENROBAGE_PAR_FICHE_PASSE_2)
    gardes = {
        "course": {"taille_max": min(taille_max(ctrl), taille_max(p2, prov_course)), "consigne": controle,
                   "detail": {"controle": taille_max(ctrl), "passe_2": taille_max(p2, prov_course)}},
        "passe_1": {"taille_max": taille_max(p1, prov_passe), "consigne": passe_1},
        "passe_2_fiches_8000": {"taille_max": taille_max(p2, prov_passe), "consigne": consigne_p2_fiches_8000,
                                "consigne_estimee": f"consigne de passe 1 + {nombre} × (8 000 + "
                                                    f"{ENROBAGE_PAR_FICHE_PASSE_2})"},
    }
    for g in gardes.values():
        g["marge"] = g["taille_max"] - g["consigne"]
    trop = {n: g for n, g in gardes.items() if g["marge"] < 0}
    if trop:
        raise Refus("garde(s) de taille qui ne tiendrai(en)t pas — l'orchestrateur refuserait : "
                    + json.dumps(trop, ensure_ascii=False))
    seuil = seuil_fiche_passe_2(taille_max(p2), passe_1, nombre)
    controles_claude = s["detail_claude"]["controle"] * len(s["detail_claude"]["modeles"])
    gardes["passe_2_seuil_de_fiche"] = {
        "fiche_de_passe_1_la_plus_longue_admise": seuil,
        "formule": f"⌊(taille_max({p2}, 0) − {passe_1} − {ENROBAGE_PAR_FICHE_PASSE_2} × {nombre}) / ({nombre} × "
                   f"{1 + RAPPORT_SORTIE_ENTREE})⌋",
        "au_dela": "refus de l'orchestrateur avant l'envoi de la passe 2 d'Argon (garder_session_externe) ; course arrêtée",
        "depense_au_plus_si_refus_usd": round(ctrl + controles_claude + p1, 6),
        "depense_detail": {"controle_externe": ctrl, "controles_claude": round(controles_claude, 6), "passe_1_argon": p1},
        "consigne_passe_2_maximale_mesuree": passe_2_max,
        "taille_fiche_maximale_servie_mesuree": c.get("taille_fiche_maximale_servie"),
        "garde": "rapporté, non gardé ici : dépend des fiches réelles",
    }
    prov_juge = fiches_juge * PROVISION_SORTIE_PAR_NOTE * RAPPORT_SORTIE_ENTREE
    t_juge = taille_max(juge, prov_juge)
    gardes["juge_argon_rapporte"] = {
        "taille_max": t_juge, "fiches_au_juge_au_maximum": fiches_juge, "consigne_du_juge_maximale": juge_max,
        "marge_au_maximum_theorique": t_juge - juge_max,
        "lecture": ("passerait au maximum théorique" if t_juge >= juge_max else
                    "ne passerait pas au maximum théorique ; dépend des fiches réelles"),
        "garde": "bras différé, non jouée par cette course : rapporté sans garde"}
    gardes["mesure_sha256"] = r.pieces["mesure_consignes"][1]
    return gardes


def sonder_bac_a_sable(r: Reglages, env: dict, prefixe_pycache: Path) -> dict:
    """La sonde de l'orchestrateur, telle quelle, dans un processus à part (lecture seule : `bwrap … true`)."""
    try:
        p = subprocess.run([r.python, *options_interprete(prefixe_pycache), "-c", SONDE_BAC_A_SABLE, str(r.orchestrateur)],
                           cwd=str(r.orchestrateur),
                           env=env, capture_output=True, text=True, timeout=120)
    except (OSError, subprocess.SubprocessError) as e:
        raise Refus(f"sonde du bac à sable : non exécutée ({type(e).__name__})") from None
    lignes = [x for x in p.stdout.splitlines() if x.strip()]
    try:
        etat = json.loads(lignes[-1]) if p.returncode == 0 and lignes else None
    except json.JSONDecodeError:
        etat = None
    if not (isinstance(etat, dict) and isinstance(etat.get("actif"), bool) and isinstance(etat.get("proc_neuf"), bool)):
        raise Refus(f"sonde du bac à sable illisible (code {p.returncode}) : {p.stderr.strip()[-500:]!r}")
    if not etat["actif"]:
        raise Refus("bac à sable de l'orchestrateur inactif : " + str(etat.get("motif")))
    if not etat["proc_neuf"]:
        raise Refus("bac à sable sans /proc neuf : " + str(etat.get("motif")))
    return etat


def environnement_sans_cles(env: Mapping, prefixe_pycache: Path | None = None) -> tuple:
    """(environnement transmis, noms retirés). La décision porte sur les **noms** seuls ; l'environnement transmis est
    construit par filtrage, sans copie intégrale préalable (m4) : aucune valeur de clé écrite, transmise ni consultée.
    `PYTHONPYCACHEPREFIX` (M1) vaut pour les sous-processus Python lancés sans `-E` ; sous `-I`, c'est `-X
    pycache_prefix` qui tient."""
    retires = sorted(n for n in env if n in NOMS_DE_CLE or MOTIF_NOM_DE_CLE.search(n))
    exclus = set(retires)
    garde = {n: env[n] for n in env if n not in exclus}
    garde["GO_ID"] = GO_ID
    if prefixe_pycache is not None:
        garde["PYTHONPYCACHEPREFIX"] = str(prefixe_pycache)
    return garde, retires


# ======================================================================================================================
# écriture
# ======================================================================================================================

def ecrire_scelle(chemin: Path, contenu: dict) -> str:
    """JSON (refus s'il existe) et compagnon `.sha256` au format de `sha256sum` (R6, R12)."""
    if chemin.exists():
        raise Refus(f"{chemin} existe déjà (R12 : jamais écrasé)")
    donnees = (json.dumps(contenu, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")
    with open(chemin, "xb") as f:
        f.write(donnees)
    h = hashlib.sha256(donnees).hexdigest()
    with open(str(chemin) + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{h}  {chemin.name}\n")
    return h


def construire_liste_blanche(r: Reglages, chemin: Path, env: dict, prefixe_pycache: Path) -> dict:
    """Par l'orchestrateur lui-même (devis § 5, préalables), sans appel ; contenu vérifié contre les pièces épinglées."""
    fichiers = [str(r.depot / r.pieces[n][0]) for n in ("question", "synthese", "temoins")]
    p = subprocess.run([r.python, *options_interprete(prefixe_pycache), LANCEUR_ORCHESTRATEUR, str(chemin),
                        "--construire-liste-blanche", *fichiers],
                       cwd=str(r.orchestrateur), env=env, capture_output=True, text=True, timeout=120)
    if p.returncode != 0 or not chemin.is_file():
        raise Refus(f"liste blanche non construite (code {p.returncode}) : {p.stderr.strip()[-500:]!r}")
    lue = json.loads(chemin.read_text(encoding="utf-8"))
    attendue = {os.path.realpath(r.depot / r.pieces[n][0]): r.pieces[n][1] for n in ("question", "synthese", "temoins")}
    if lue != attendue:
        raise Refus(f"liste blanche différente des pièces épinglées : {lue}")
    return {"chemin": str(chemin), "sha256": sha256_fichier(chemin), "contenu": lue}


def _depot_git(r: Reglages) -> dict:
    try:
        return {"commit": _git(r.depot, "rev-parse", "HEAD").strip(),
                "arbre_modifie": bool(_git(r.depot, "status", "--porcelain", "--untracked-files=no").strip())}
    except Refus as e:
        return {"commit": None, "erreur": str(e)}


def executer(r: Reglages) -> int:
    env_lu = os.environ if r.environnement is None else r.environnement   # m4 : aucune copie intégrale
    aujourd_hui = r.aujourd_hui or _dt.datetime.now(_dt.timezone.utc).date()

    # --- gardes : rien écrit, rien appelé ---
    interprete = verifier_interprete(r)
    go = verifier_go(r.registre_go, aujourd_hui)
    orch = verifier_orchestrateur(r)
    pieces = verifier_pieces(r)
    horodatage = r.horodatage()
    ident = _dt.datetime.now(_dt.timezone.utc).strftime("%Y%m%d-%H%M%S") + "-course-ideation-pilier-attaque-v2-v3"
    dossier_run = r.dossier_runs / ident
    dossier_sortie = r.dossier_sorties / ident
    sortie = dossier_sortie / "sortie"
    prefixe_pycache = dossier_sortie / NOM_DOSSIER_PYCACHE
    liste_blanche = dossier_run / "liste-blanche.json"
    argv = commande_course(r, sortie, liste_blanche, horodatage, prefixe_pycache)
    garde_drapeaux(argv)
    sommes = garde_sommes(argv)
    tailles = garde_tailles(r, argv)
    if dossier_run.exists() or dossier_sortie.exists():
        raise Refus(f"{dossier_run} ou {dossier_sortie} existe déjà (R12)")
    verifier_prefixe_pycache(prefixe_pycache, Path(orch["racine_clone"]))
    env, retires = environnement_sans_cles(env_lu, prefixe_pycache)
    bac = sonder_bac_a_sable(r, env, prefixe_pycache)   # préfixe encore absent : sous -B, rien n'y est écrit ni lu

    # --- écritures ---
    dossier_run.mkdir(parents=True)
    dossier_sortie.mkdir(parents=True)
    prefixe_pycache.mkdir()
    lb = construire_liste_blanche(r, liste_blanche, env, prefixe_pycache)
    depart = {
        "lanceur": {"version": VERSION, "chemin": str(Path(__file__).resolve()), "sha256": sha256_fichier(Path(__file__))},
        "horodatage_canonique": horodatage, "id": ident, "go": go, "decision": "R-1978 (règle de permission, Lazar)",
        "orchestrateur": orch, "pieces": pieces, "liste_blanche": lb, "bac_a_sable": bac,
        "commande": argv, "cwd": str(r.orchestrateur), "sortie": str(sortie),
        "plafonds": {"devis": dict(PLAFONDS_DEVIS), "controle_externe_devis_usd": CONTROLE_EXTERNE_DEVIS_USD,
                     "reglage": PLAFOND_REDUIT, "sommes": sommes, "gardes_de_taille": tailles},
        "drapeaux_interdits_verifies_absents": list(DRAPEAUX_INTERDITS),
        "cles": {"noms_retires_de_l_environnement": retires,
                 "valeurs": "aucune valeur de clé écrite, transmise ni consultée (décision sur les noms)"},
        "cache_d_octets": {"prefixe": str(prefixe_pycache), "option": f"-X pycache_prefix={prefixe_pycache}",
                           "variable": "PYTHONPYCACHEPREFIX (sous-processus sans -E)"},
        "depot_travail": _depot_git(r), "python": interprete,
        "journaux": {"stdout": str(dossier_sortie / "course.stdout.txt"), "stderr": str(dossier_sortie / "course.stderr.txt")},
    }
    h_depart = ecrire_scelle(dossier_run / "manifeste-lanceur-depart.json", depart)
    print(json.dumps({"manifeste_depart": str(dossier_run / "manifeste-lanceur-depart.json"), "sha256": h_depart,
                      "sortie": str(sortie)}, ensure_ascii=False), flush=True)

    # --- course ---
    debut = _dt.datetime.now(_dt.timezone.utc)
    with open(dossier_sortie / "course.stdout.txt", "xb") as fo, open(dossier_sortie / "course.stderr.txt", "xb") as fe:
        enfant = subprocess.Popen(argv, cwd=str(r.orchestrateur), env=env, stdout=fo, stderr=fe)

        def relayer(num, _cadre):  # R10 : par PID, jamais par motif
            try:
                enfant.send_signal(num)
            except ProcessLookupError:
                pass
        anciens = {s: signal.signal(s, relayer) for s in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP)}
        try:
            code = enfant.wait()
        finally:
            for s, a in anciens.items():
                signal.signal(s, a)
    fin = _dt.datetime.now(_dt.timezone.utc)
    bilan = {"id": ident, "manifeste_depart_sha256": h_depart, "pid_orchestrateur": enfant.pid, "code": code,
             "debut_utc": debut.isoformat(), "fin_utc": fin.isoformat(),
             "journaux_sha256": {n: sha256_fichier(dossier_sortie / n) for n in ("course.stdout.txt", "course.stderr.txt")},
             "sortie_existe": sortie.exists()}
    h_fin = ecrire_scelle(dossier_run / "manifeste-lanceur-fin.json", bilan)
    print(json.dumps({"manifeste_fin": str(dossier_run / "manifeste-lanceur-fin.json"), "sha256": h_fin, "code": code},
                     ensure_ascii=False), flush=True)
    return code


def principal(argv: list | None = None, reglages: Reglages | None = None) -> int:
    argv = sys.argv[1:] if argv is None else list(argv)
    if argv:
        print(json.dumps({"refus": f"aucun argument admis (reçu {argv!r}) : la commande permise est exacte"},
                         ensure_ascii=False), file=sys.stderr)
        return 2
    try:
        return executer(reglages or Reglages.production())
    except Refus as e:
        print(json.dumps({"refus": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(principal())
