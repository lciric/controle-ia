#!/usr/bin/env python3
"""Quatre tables pour l'entretien avec le Transformative AI Fund, produites par script, sans cellule saisie à la main — v3.

Sorties (dossier `livrables/registres-taif-v4/` par défaut ; `livrables/registres-taif-v3/` porte les sorties scellées de la v2) :
    promis-livre-v3.md        une ligne par critère de la porte G0 et par promesse de la candidature réellement envoyée au
                              fonds le 7 octobre 2026 (sections 6, 7, 8 du texte extrait du PDF) ;
    calibration-v3.md         une ligne par prédiction préenregistrée (préenregistrements scellés de `prereg/`), suivie
                              d'un bloc de comptes par issue calculé depuis les lignes de la table rendue elle-même ;
    cout-par-resultat-v3.md   une ligne par run décisif et par GO de calcul (registre des dépenses) ;
    total-depenses-v3.md      somme des dépenses de la phase 0 par un analyseur strict du registre des dépenses ;
    journal-depenses-v3.txt   chaque ligne du registre des dépenses non sommée, avec sa raison ;
    sources-v3.json           chaque cellule non vide → chemin, ligne(s), empreinte sha256 du fichier lu ; `comptes` ;
                              `signalements` ; `total_depenses_phase0`.

Changement par rapport à la v2 (`scripts/registres_taif_v2.py`, intacte) — seule la source des promesses change :
    la table « promis → livré » lit la candidature envoyée au fonds, `docs/sources/candidature-taif-2026-10-07/
    proposal_v2_TAIF_2026-10-07.txt` (texte extrait du PDF par `pdftotext -layout`, scellé), et non plus la version
    EA Funds `livrables/candidature-ea-funds-v1/proposal-v1.md`. Règles de lecture de la mise en page extraite
    (`section_texte`, `items_indentes`, `table_alignee`) : un titre de section est une ligne « N. Titre » à la colonne 0,
    la section court jusqu'au titre suivant ; les puces de la section 6 et de la section 8 ont perdu leur glyphe :
    une puce est une suite de lignes indentées, une puce nouvelle commence à une ligne indentée qui débute par une
    majuscule quand la puce courante finit par une fin de phrase (« . », « ! », « ? »), ou à une ligne numérotée
    « 1. », « 2. » ; une ligne à la colonne 0 ou vide clôt la puce ; le paragraphe « Gate G0 » est la suite des lignes
    à la colonne 0 qui commence par « Gate G0 » ; la table de la section 7 a ses colonnes alignées par espaces :
    les débuts de colonnes sont ceux des cellules de la ligne d'en-tête (« Months », « Period », « Work », « Gates… »),
    une ligne dont la cellule « Months » commence par un chiffre ouvre une ligne de calendrier, une ligne indentée
    dont la cellule « Months » est vide la continue (cellules recollées par un espace), une ligne vide ou à la colonne 0
    la clôt. Une section absente, un en-tête de table absent : aucune ligne pour cette section et un signalement
    (`signalements` de `sources-v3.json`), jamais une exception ni une ligne devinée. Les identifiants gardent la
    convention de la v2 : C6-k dans l'ordre du texte, C6-G0, C7-k par ligne du calendrier, C8-k par livrable puis par
    critère de succès. La date promise des lignes C8 vient du titre de la section 7 (« seven months from 1 December
    2026 »). Calibration, coût par résultat, total des dépenses, sources, déterminisme : inchangés.

Changements de règle de la v2 par rapport à la v1 (`scripts/registres_taif_v1.py`, intacte), repris tels quels :
    1. Comptes alignés sur la table : les comptes par issue, le total et le taux de confirmation parmi les tranchées
       (confirmées / (confirmées + réfutées + non concluantes)) sont recalculés depuis le texte markdown de la table de
       calibration rendue (`compter_issues_table_md`), jamais saisis ; ils sont écrits en fin de `calibration-v3.md` et
       sous la clé `comptes` de `sources-v3.json`.
    2. Règle de lecture de l'issue : la table de lecture du verdict (lignes de table dont la première cellule est
       l'identifiant de la prédiction, dans tout le verdict ; cellule de la colonne « conforme », « lecture », « issue »…
       quand l'en-tête en a une, « oui » / « non » compris) prime ; la recherche par mots-clés dans la prose ne sert qu'à
       défaut de ligne de table ; une table recopiée du préenregistrement (en-tête « réfutation », « prédiction ») n'est
       pas une table de lecture. Un identifiant de bras (« Rk-5 », « Rd-6 ») se lit aussi « R5 », « R6 ».
    3. Catégorie « sans objet » : un verdict qui dit « sans objet » donne l'issue « sans objet », distincte de « non
       atteinte » ; elle n'entre ni au numérateur ni au dénominateur du taux ; le compte la rapporte à part.
    4. Table des dépenses : analyseur strict (`analyser_depenses_strict`) : une ligne du registre = un montant en USD
       explicitement relevé ; « ≈ », « ≤ », « au plus », « environ », « estimé » → colonne « estimé », jamais dans le
       total relevé ; prix unitaires, cumuls, plafonds, devis, crédits, restes, montants d'autres projets → jamais
       sommés ; une ligne à plusieurs montants (hors un montant unique en gras, convention du registre pour le total de
       la ligne) → journal ; un « premier relevé » ou relevé partiel → journal ; une ligne qui dit remplacer une
       estimation par un relevé compte une fois (l'estimation antérieure du même GO sort de la colonne « estimé »).

Règles communes : toute cellule sans source reste vide ; aucune estimation ; déterministe et idempotent (mêmes sources,
même jour → mêmes octets). Le script lit : la candidature, le programme, les registres (état, décisions, GO, dépenses,
arrêts), les verdicts scellés de `docs/verdicts/`, les préenregistrements scellés de `prereg/` (brouillons et gabarit
exclus), les manifestes de `runs/*/manifeste.json`. Il ne lit jamais `diag/` ni les résultats de `runs/`.
Un verdict ou un préenregistrement sans empreinte compagnon arrête le script (R5, R6 : aucun repli silencieux).

    PYTHONPATH=src python scripts/registres_taif_v3.py [--racine .] [--sortie livrables/registres-taif-v4] [--jour AAAA-MM-JJ]

Le jour vient de `date -u` (jour seul, pour l'idempotence) sauf `--jour`.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

VERSION = "registres-taif-v3"
SUFFIXE = ".sha256"
_LIGNE_COMPAGNON = re.compile(r"^([0-9a-f]{64})  (\S.*)$")
_GO = re.compile(r"GO-\d{4}-\d{2}-\d{2}-\d{2}")
_RUN = re.compile(r"\b(2026[01]\d[0-3]\d-\d{6}-[a-z0-9][a-z0-9-]*[a-z0-9])\b")
_INSTANCE = re.compile(r"\b(5\d{7})\b")
_MONTANT = re.compile(r"(≈\s*)?(\d+(?:[,.]\d+)?)\s*USD")
_MONTANT_GRAS = re.compile(r"\*\*(≈\s*)?(\d+(?:[,.]\d+)?)\s*USD\*\*")
_GO_ABREGE = re.compile(r"\bGO-(\d{2})\b(?!-)")
# Un montant n'est pas une dépense s'il est un prix (par heure, par Go), un cumul, un plafond, un crédit ou un reste.
_PRIX_APRES = re.compile(r"^\s*(/\s*h\b|de l'heure|par heure|/\s*Go\b|par Go|le Go)")
_CONTEXTE_AVANT = re.compile(r"((cumul|plafond|enveloppe|crédit|solde|reste|alerte|devis|pire cas|projection|au plus|≤|plafonn)[^;]{0,45}"
                             r"|GO-\d{4}-\d{2}-\d{2}-\d{2}\W{0,3})$", re.I)
_MONTANT_SUR = re.compile(r"(\d+(?:[,.]\d+)?)\s*/\s*\d+(?:[,.]\d+)?\s*USD")
_CUMUL_APRES = re.compile(r"^\s*(sur|/)\s*\d")
_RELEVE = re.compile(r"crédit|recharg|solde|facture|relevé", re.I)
_PUCE_DATEE = re.compile(r"^- (\d{4}-\d{2}-\d{2})[^—]*—\s*(.*)$")
_ID_PRED = re.compile(r"^\**([A-Za-z][\w.\-]*\d[\w.\-]*|P\d+[a-z]?)\**(\s*\(.*\))?$")
_ID_BRAS = re.compile(r"^([A-Z])[a-z]-(\d)")
_CONTRE_LECTURE = re.compile(r"Contre-lecture\s+(\d+)\s*\*{0,2}\s*(\(([^)]*)\))?")
_SEGMENT = re.compile(r";|\.\s+(?=[A-ZÀ-Ý*«\[(])")        # séparateurs de segments de prose : « ; » ou une fin de phrase
LARGEUR_CELLULE = 220

# Dossiers lus (relatifs à la racine).
CHEMINS = {
    "candidature": "docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt",
    "programme": "docs/programme-controle-ia-v2.md",
    "etat": "registres/etat.md",
    "decisions": "registres/decisions.md",
    "go": "registres/go.md",
    "depenses": "registres/depenses.md",
    "arrets": "registres/arrets.md",
    "verdicts": "docs/verdicts",
    "prereg": "prereg",
    "runs": "runs",
}

# Règles de liaison (données du script, pas des cellules) : motif dans le texte d'une promesse ou d'un critère → tâche
# de la table de la phase 0 (`registres/etat.md`). Les tâches donnent l'état, les pièces (verdicts dont le nom porte la
# tâche ; runs cités par la ligne) et la cause du glissement (« Reste : … »).
REGLES_CRITERES_G0 = [
    (r"harnais", "T0.4"), (r"organismes", "T0.6"), (r"sondes", "T0.7"), (r"boîte noire", "T0.8"),
    (r"agrégateurs", "T0.3"), (r"papier C", "T0.9"), (r"état de l'art", "T0.2"), (r"\bG1\b", None),
]
REGLES_CANDIDATURE = [
    (r"literature", "T0.2"), (r"theory|lemma|simulation", "T0.3"), (r"harness", "T0.4"),
    (r"sabotage environment|pilot", "T0.5"), (r"code, with tests", "T0.1"), (r"pre-registration drafts", "T0.9"),
    (r"organism", "T0.6"), (r"probe", "T0.7"), (r"black-box baseline", "T0.8"), (r"compute spent", None),
]
# Mots-clés d'issue lus dans les lignes de verdict qui citent une prédiction (ordre : les négations d'abord).
# v2 : « sans objet » est une issue à part (changement 3), lue avant « non établi » (« sans objet (cible non établie) »).
ISSUES = [
    (r"non conforme", "réfutée (non conforme)"), (r"sans objet", "sans objet"), (r"non prouvé", "non prouvée"),
    (r"non établi", "non établie"), (r"non concluant|non tranché", "non concluante"), (r"non atteint|n'est pas atteint", "non atteinte"),
    (r"non déclench", "non déclenchée"),
    (r"réfut", "réfutée"), (r"contraire", "réfutée (contraire)"),
    (r"sans verdict", "rapportée sans verdict (descriptive)"),
    (r"conforme|confirm|établi|prouvé", "confirmée"),
]
# Cellule d'une colonne d'issue d'une table de lecture : « oui » / « non » sous un en-tête « conforme » (« non tranché » se lit
# « non concluante »).
OUI_NON = {"oui": "confirmée", "vrai": "confirmée", "non": "réfutée (non conforme)", "faux": "réfutée (non conforme)"}
# Colonnes d'issue d'une table de lecture, par ordre de préférence (la plus spécifique d'abord, « conforme » en dernier).
_ENTETES_ISSUE = [re.compile(m, re.I) for m in (r"\bissue\b", r"verdict", r"statut", r"conclusion", r"lecture", r"résultat", r"conforme",
                                                 r"réfutation.*atteinte")]
_OUI_NON_TETE = re.compile(r"^\**\s*(oui|non|vrai|faux)\s*(\*\*|\(|$|;|,|:|\.)", re.I)
# Colonne « réfutation (écrite) atteinte ? » : « non » = réfutation non atteinte = prédiction tenue (sens inverse de « conforme »).
_ENTETE_REFUTATION_ATTEINTE = re.compile(r"réfutation.*atteinte", re.I)
OUI_NON_REFUTATION = {"oui": "réfutée", "vrai": "réfutée", "non": "confirmée", "faux": "confirmée"}
_ENTETE_PREDICTION = re.compile(r"réfutation|prédiction|hypothèse|signe attendu", re.I)
MOTS_VERDICT_DECISIONS = re.compile(r"verdict (R13|scellé|de lecture|de porte)|prononc|prouvé|non concluant|réfut|prédictions confirmées"
                                    r"|arrêté[es]* par (sa|la|leur) garde|lecture gelée", re.I)

# Catégories de compte (changement 1) : préfixe de l'issue → catégorie ; sinon l'issue elle-même.
CATEGORIES_ISSUE = [
    ("confirmée", "confirmée"), ("réfutée", "réfutée"), ("non concluante", "non concluante"),
    ("non atteinte", "non atteinte"), ("sans objet", "sans objet"), ("non déclenchée", "non déclenchée"),
    ("non prouvée", "non prouvée"), ("non établie", "non établie"), ("rapportée sans verdict", "rapportée sans verdict (descriptive)"),
    ("mixte", "mixte (plusieurs identifiants, issues différentes)"),
    ("contradictoire", "contradictoire"), ("non citée par le verdict", "non citée par le verdict"),
    ("registre des décisions", "registre des décisions (sans verdict scellé)"),
    ("non encore lue", "non encore lue (run décisif fait, aucun verdict scellé)"),
    ("sans run décisif", "sans run décisif cité par un manifeste"),
]
TRANCHEES = ("confirmée", "réfutée", "non concluante")


class GardeArret(RuntimeError):
    """Arrêt commandé par une garde : jamais attrapé pour continuer."""


# --------------------------------------------------------------------------- empreintes et lecture
def empreinte(chemin: Path) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def verifier_scelle(chemin: Path) -> str:
    """Empreinte d'un dépôt scellé ; arrêt si le compagnon manque ou diffère (R6)."""
    compagnon = Path(str(chemin) + SUFFIXE)
    if not compagnon.is_file():
        raise GardeArret(f"{chemin} : empreinte compagnon absente, dépôt refusé (R6)")
    lignes = [l for l in compagnon.read_text(encoding="utf-8").splitlines() if l.strip()]
    m = _LIGNE_COMPAGNON.match(lignes[0]) if len(lignes) == 1 else None
    if not m or m.group(2) != chemin.name:
        raise GardeArret(f"{compagnon} : compagnon illisible ou nom différent")
    h = empreinte(chemin)
    if h != m.group(1):
        raise GardeArret(f"{chemin} : empreinte {h[:12]}… différente du compagnon {m.group(1)[:12]}…")
    return h


class Fichier:
    """Un fichier lu : lignes numérotées (à partir de 1) et empreinte."""

    def __init__(self, racine: Path, rel: str, scelle: bool = False):
        self.rel = rel
        self.chemin = racine / rel
        if not self.chemin.is_file():
            raise GardeArret(f"{rel} : absent sur disque (R11)")
        self.sha256 = verifier_scelle(self.chemin) if scelle else empreinte(self.chemin)
        self.lignes = self.chemin.read_text(encoding="utf-8").splitlines()

    def chercher(self, motif: str | re.Pattern, flags=0) -> list[tuple[int, str]]:
        r = re.compile(motif, flags) if isinstance(motif, str) else motif
        return [(i + 1, l) for i, l in enumerate(self.lignes) if r.search(l)]

    def section(self, titre_motif: str) -> list[tuple[int, str]]:
        """Lignes d'une section `## …` dont le titre contient le motif, jusqu'au prochain titre de même niveau ou plus haut."""
        r = re.compile(titre_motif)
        for i, l in enumerate(self.lignes):
            m = re.match(r"^(#{1,6})\s+(.*)$", l)
            if m and r.search(m.group(2)):
                niveau = len(m.group(1))
                fin = len(self.lignes)
                for j in range(i + 1, len(self.lignes)):
                    m2 = re.match(r"^(#{1,6})\s", self.lignes[j])
                    if m2 and len(m2.group(1)) <= niveau:
                        fin = j
                        break
                return [(k + 1, self.lignes[k]) for k in range(i + 1, fin)]
        return []


def motif_id(identifiant: str) -> re.Pattern:
    variantes = [re.escape(identifiant)]
    if _ID_BRAS.match(identifiant):              # « Rk-1 » (par bras), « Rd-6 » se lisent « R1 », « R6 » dans un verdict
        variantes.append(re.escape(_ID_BRAS.sub(r"\1\2", identifiant)))
    # « [A2] » entre crochets est une référence de pièce (addendum 2), pas la prédiction A2 : exclu.
    return re.compile(r"(?<![\w.\-\[])(" + "|".join(variantes) + r")(?![\w.\-\]])")


def cellules_table(ligne: str) -> list[str]:
    """Cellules d'une ligne de table markdown (les `|` dans du code inline sont tolérés en coupant naïvement)."""
    if not ligne.startswith("|"):
        return []
    return [c.strip() for c in ligne.strip().strip("|").split("|")]


def est_separateur(cellules: list[str]) -> bool:
    return bool(cellules) and all(re.match(r"^:?-{3,}:?$", c) for c in cellules if c)


def tronquer(texte: str, n: int = LARGEUR_CELLULE) -> str:
    texte = re.sub(r"\s+", " ", texte).strip()
    return texte if len(texte) <= n else texte[: n - 1].rstrip() + "…"


def cellule_md(texte: str) -> str:
    return texte.replace("|", "¦").replace("\n", " ")


def nombre_fr(valeur: float) -> str:
    return f"{valeur:.2f}".replace(".", ",")


def montant_vers_float(texte: str) -> float:
    return float(texte.replace(",", "."))


# --------------------------------------------------------------------------- sources
class Sources:
    """Chaque cellule non vide → sa source (chemin, lignes, empreinte). Les fichiers lus → empreinte."""

    def __init__(self):
        self.fichiers: dict[str, str] = {}
        self.tables: dict[str, dict[str, dict[str, dict]]] = {}
        self.signalements: list[dict] = []

    def fichier(self, f: Fichier):
        self.fichiers[f.rel] = f.sha256

    def cellule(self, table: str, ligne_id: str, colonne: str, f: Fichier, lignes: list[int], note: str = ""):
        self.fichier(f)
        src = {"chemin": f.rel, "lignes": sorted(set(lignes)), "sha256": f.sha256}
        if note:
            src["note"] = note
        self.tables.setdefault(table, {}).setdefault(ligne_id, {})[colonne] = src

    def signaler(self, quoi: str, f: Fichier, ligne: int, texte: str):
        self.fichier(f)
        self.signalements.append({"quoi": quoi, "chemin": f.rel, "ligne": ligne, "sha256": f.sha256,
                                  "texte": tronquer(texte, 300)})


# --------------------------------------------------------------------------- registres
def lire_etat_taches(etat: Fichier) -> dict[str, dict]:
    """Table « Tâches de la phase 0 » : tâche → {ligne, etat, note, reste, runs, verdicts}."""
    taches = {}
    for no, l in etat.section(r"Tâches de la phase 0"):
        c = cellules_table(l)
        if len(c) < 4 or not re.match(r"^(T0\.\d|P\d)\b", c[0]):
            continue
        identifiant = re.match(r"^(T0\.\d|P\d)", c[0]).group(1)
        reste = re.search(r"Reste\s*:\s*(.*)$", c[3])
        taches[identifiant] = {
            "ligne": no, "nom": c[0], "etat": c[1], "note": c[3],
            "etat_court": " ; ".join(re.findall(r"\*\*(.+?)\*\*", c[1])) or tronquer(c[1], 120),
            "reste": tronquer(reste.group(1), 300) if reste else "",
            "runs": sorted(set(_RUN.findall(c[3]))),
            "verdicts": sorted(set(re.findall(r"docs/verdicts/([\w.\-]+\.md)", c[3]))),
        }
    return taches


def lire_criteres_g0_etat(etat: Fichier) -> dict:
    """Paragraphe « Derniers verdicts de porte » : critères prouvés et restants, avec la ligne."""
    for no, l in etat.section(r"Derniers verdicts de porte"):
        if "Critères de G0 prouvés" in l:
            prouves = re.findall(r"\*\*(\d)\*\*\s*\(([^)]*)\)", l)
            m = re.search(r"Restent les critères\s+(.*?)\.", l)
            restent = re.findall(r"(\d)\s*\(([^)]*)\)", m.group(1)) if m else []
            return {"ligne": no, "prouves": dict(prouves), "restent": dict(restent)}
    return {"ligne": None, "prouves": {}, "restent": {}}


def lire_go(go: Fichier) -> dict[str, list[dict]]:
    """Registre des GO : identifiant → lignes (type, périmètre, plafond, échéance, ligne)."""
    gos: dict[str, list[dict]] = {}
    for i, l in enumerate(go.lignes):
        c = cellules_table(l)
        if len(c) >= 8 and _GO.fullmatch(c[0]):
            gos.setdefault(c[0], []).append({"ligne": i + 1, "date": c[1], "type": c[2], "perimetre": c[3],
                                             "plafond": c[4], "echeance": c[5]})
    return gos


def montants_depense(texte: str) -> list[str]:
    """Montants en USD d'une ligne, sans les prix unitaires, cumuls, plafonds, crédits et restes (contexte lu autour)."""
    retenus = []
    couverts = []
    for m in _MONTANT_SUR.finditer(texte):           # « 4,30 / 12 USD » : dépensé / plafond
        retenus.append((m.start(), m.group(1)))
        couverts.append((m.start(), m.end()))
    for m in _MONTANT.finditer(texte):
        if any(a <= m.start() < b for a, b in couverts):
            continue
        apres = texte[m.end():m.end() + 16]
        avant = texte[max(0, m.start() - 60):m.start()]
        if _PRIX_APRES.match(apres) or _CUMUL_APRES.match(apres) or _CONTEXTE_AVANT.search(avant):
            continue
        retenus.append((m.start(), m.group(2)))
    return [v for _, v in sorted(retenus)]


def lire_depenses(dep: Fichier) -> list[dict]:
    """Une entrée par ligne de table ou par puce datée portant un montant en USD (table 3, règles de la v1).

    `montant` n'est rempli que si la ligne porte un seul montant, ou un seul montant en gras (convention du registre
    pour le total) ; sinon il reste vide et `montants` garde tous les montants lus. Les lignes d'engagement (« engagement »,
    « pire cas », « plafond », « projection ») sont marquées et exclues des sommes."""
    entrees = []
    for i, l in enumerate(dep.lignes):
        no = i + 1
        c = cellules_table(l)
        if c and re.match(r"^\d{4}-\d{2}-\d{2}$", c[0]):
            gos = sorted(set(_GO.findall(l)))
            montants = [m.group(2) for m in _MONTANT.finditer(l)]
            montant = ""
            if len(c) >= 7:                      # table à 9 colonnes : coût (USD) en colonne 7
                m = re.match(r"^\s*≈?\s*(\d+(?:[,.]\d+)?)", c[6])
                montant = m.group(1) if m else ""
            elif len(c) >= 3:
                nums = [m.group(1) for cc in c[1:] for m in [re.match(r"^\s*≈?\s*(\d+(?:[,.]\d+)?)\s*(USD)?\s*$", cc)] if m]
                montant = nums[0] if len(nums) == 1 else ""
            entrees.append({"ligne": no, "date": c[0], "forme": "table", "gos": gos, "gos_abreges": [], "montant": montant,
                            "montants": montants, "montants_retenus": montants, "instances": sorted(set(_INSTANCE.findall(l))),
                            "runs": sorted(set(_RUN.findall(l))), "engagement": False, "releve": False, "texte": l})
            continue
        m = _PUCE_DATEE.match(l)
        if m and "USD" in l:
            texte = m.group(2)
            gras = [g.group(2) for g in _MONTANT_GRAS.finditer(texte)]
            tous = [g.group(2) for g in _MONTANT.finditer(texte)]
            retenus = montants_depense(texte)
            montant = gras[0] if len(gras) == 1 else (retenus[0] if len(retenus) == 1 else "")
            engagement = bool(re.search(r"(?<!sans )\bengagement\b|pire cas|projection|\bdevis\b", texte, re.I))
            releve = bool(_RELEVE.search(texte)) and not retenus
            entrees.append({"ligne": no, "date": m.group(1), "forme": "puce", "gos": sorted(set(_GO.findall(texte))),
                            "gos_abreges": sorted(set(_GO_ABREGE.findall(texte))), "montant": montant, "montants": tous,
                            "montants_retenus": retenus, "instances": sorted(set(_INSTANCE.findall(texte))),
                            "runs": sorted(set(_RUN.findall(texte))), "engagement": engagement, "releve": releve, "texte": l})
    return entrees


def lire_arrets(arrets: Fichier) -> list[dict]:
    return [{"ligne": i + 1, "instances": sorted(set(_INSTANCE.findall(l))), "runs": sorted(set(_RUN.findall(l))),
             "gos": sorted(set(_GO.findall(l))), "texte": l}
            for i, l in enumerate(arrets.lignes) if l.startswith(("|", "-"))]


def texte_arret(a: dict) -> str:
    """Raison d'un arrêt : troisième cellule d'une ligne de table, sinon le texte après le tiret cadratin."""
    c = cellules_table(a["texte"])
    if len(c) >= 3:
        return tronquer(f"{c[0]} : {c[2]}", 200)
    return tronquer(re.sub(r"^- ", "", a["texte"]), 200)


# --------------------------------------------------------------------------- analyseur strict des dépenses (table 4)
FENETRE_AVANT = 160
_SEPARATEUR_PROPOSITION = re.compile(r";|\*\*\s*:|\)\s*:")
FENETRE_APRES = 40
# Un jeton de montant : « **≈ 1,23 USD** », « 48,49583 USD », « ≤ 0,037 USD », « 1,6 à 1,7 USD » (fourchette).
_JETON = re.compile(r"(?P<gras>\*\*)?\s*(?P<marque>≈|≤|≥|<|>|environ|au plus|au moins|estimée? à|estimé à)?\s*"
                    r"(?P<bas>\d+(?:[,.]\d+)?)(?:\s*(?:à|–|-)\s*(?P<haut>\d+(?:[,.]\d+)?))?\s*USD(?P<gras_fin>\*\*)?")
_PRIX_UNITAIRE = re.compile(r"^\s*(/\s*h\b|/\s*Go\b|de l'heure|par heure|par Go|par jour|par mois|le Go|/\s*jour)")
_SUR_PLAFOND = re.compile(r"^\s*(sur|/)\s*\d")
_MARQUE_ESTIMATION = re.compile(r"≈|≤|≥|<|>|environ|au plus|au moins|estim|borne|approximativ|plus ou moins|de l'ordre", re.I)
_CONTEXTE_NON_DEPENSE = re.compile(
    r"cumul|plafond|enveloppe|crédit|solde|reste\b|restent|alerte|devis|pire cas|au pire\b|attendu|projection|plafonn|minimum|exigé|exige|seuil"
    r"|paiement|recharg|tarif|prix|dossier\b|poste\b|garde de|sans compter|non imput|hors du programme"
    r"|hors de ce programme|autre projet|pas de ce projet|d'un autre projet|déjà imputé|engagé au|écart|disponible", re.I)
# Montant collé à un identifiant de GO (« GO-2026-11-04-06, 400 USD ») ou précédé de « x / » (« 4,30 / 12 USD ») : plafond.
# Montant calculé par une formule (« … + 1,2 = 31,70 USD ») ou multiplié (« 2 × 0,00041 USD ») : pas un relevé.
_AVANT_HORS_DEPENSE = re.compile(r"(GO-\d{4}-\d{2}-\d{2}-\d{2}\W{0,3}|\d\s*/\s*|=\s*|×\s*)$")
_APRES_HORS_DEPENSE = re.compile(r"^\s*(au pire cas|par tour|par course|par dossier|par étape|chacun|de garde|au plus pour|[<>≤≥]\s*\d"
                                 r"|[^;.]{0,%d}(non imput|hors du programme|autre projet|déjà compt|inscrit à (la|sa) clôture|sans compter"
                                 r"|exigés?|chacun|conseillés?|demandés?|de crédits?|gratuit|cumulés|attendus?|d'ici))" % FENETRE_APRES, re.I)
_APRES_ESTIMATION = re.compile(r"^\s*(estimés?|environ|au plus|au moins|de marche|de carte|de location|[^;.]{0,25}au pire cas)\b", re.I)
_CONTEXTE_PARTIEL = re.compile(r"premier relevé|relevé partiel|en cours|cumulés|déjà|avant l'appel|à ce stade|jusqu'ici|provisoire", re.I)
# Titre d'une ligne (avant le premier « : ») qui reprend un montant déjà consigné : jamais sommé.
_TITRE_REPRISE = re.compile(r"inscrit à (la|sa) clôture|récapitulatif|bilan\b|rappel\b", re.I)
_MARQUE_REMPLACEMENT = re.compile(r"remplace (l'|une |cette |l'ancienne )?estim|corrige (l'|une |cette )?estim|relevé exact\s*:|facture relue\s*:", re.I)
_MARQUE_RELEVE_LOCAL = re.compile(r"relev|factur|réel|exact", re.I)
_TACHE = re.compile(r"\b(T0\.\d|P[1-9])\b(?![-.])")


def jetons_montants(texte: str) -> list[dict]:
    """Jetons de montant d'une ligne, chacun classé : prix (unitaire), hors_depense (cumul, plafond, crédit…),
    partiel (premier relevé, cumulé), fourchette, estime (≈, ≤, environ, borne…), releve (montant nu)."""
    jetons = []
    fin_precedent = 0
    for m in _JETON.finditer(texte):
        # Contexte avant : la proposition courante, depuis le dernier séparateur (« ; », fin d'un titre en gras « ** : »,
        # « ) : »), au plus FENETRE_AVANT caractères : un mot-clé (cumul, plafond, crédit…) qualifie tous les montants
        # de sa proposition. La marque d'estimation (≈, environ, estimé…) ne vaut que juste avant le montant, après le
        # montant précédent.
        avant = _SEPARATEUR_PROPOSITION.split(texte[max(0, m.start() - FENETRE_AVANT):m.start()])[-1]
        immediat = texte[max(fin_precedent, m.start() - 18):m.start()]
        apres = texte[m.end():m.end() + FENETRE_APRES]
        fin_precedent = m.end()
        gras = bool(m.group("gras")) and bool(m.group("gras_fin"))
        valeur = m.group("bas")
        if _PRIX_UNITAIRE.match(apres):
            classe = "prix"                                   # prix par heure, par Go, par jour
        elif (_SUR_PLAFOND.match(apres) or _APRES_HORS_DEPENSE.match(apres) or _AVANT_HORS_DEPENSE.search(avant)
              or _CONTEXTE_NON_DEPENSE.search(avant)):
            classe = "hors_depense"                           # cumul, plafond, devis, crédit, reste, autre projet, « x / plafond »
        elif _CONTEXTE_PARTIEL.search(avant):
            classe = "partiel"                                # premier relevé, cumulés, déjà imputé
        elif m.group("haut"):
            classe = "fourchette"                             # « 1,6 à 1,7 USD »
        elif m.group("marque") or _MARQUE_ESTIMATION.search(immediat) or _APRES_ESTIMATION.match(apres):
            classe = "estime"                                 # ≈, ≤, environ, au plus, estimé, attendu, borne
        else:
            classe = "releve"
        jetons.append({"valeur": valeur, "haut": m.group("haut") or "", "classe": classe, "gras": gras,
                       "debut": m.start(), "texte": texte[m.start():m.end()].strip()})
    return jetons


def analyser_ligne_depense(texte: str) -> dict:
    """Décision stricte pour une ligne : {'montant': str|'', 'nature': 'releve'|'estime'|'', 'raison': str, 'jetons': [...]}.

    Règles (écrites, sans devinette) :
      R1 les jetons « prix », « hors_depense » ne sont jamais des dépenses ;
      R2 aucun jeton restant → ligne de contexte seulement (journal) ;
      R3 un seul jeton restant → relevé ou estimé selon sa classe ; « partiel » et « fourchette » → journal ;
      R4 plusieurs jetons restants → le montant unique en gras vaut total de la ligne (convention du registre) ;
         sinon, un relevé unique dont le contexte immédiat dit « relevé », « facture », « réel », « exact » remplace
         les estimations de la même ligne (compté une fois) ; sinon → journal « plusieurs montants »."""
    jetons = jetons_montants(texte)
    restants = [j for j in jetons if j["classe"] not in ("prix", "hors_depense")]
    if not jetons:
        return {"montant": "", "nature": "", "raison": "aucun montant", "jetons": jetons}
    if _TITRE_REPRISE.search(texte.split(" : ")[0]):
        return {"montant": "", "nature": "", "raison": "reprise ou bilan d'un montant déjà consigné (titre de la ligne)", "jetons": jetons}
    if not restants:
        return {"montant": "", "nature": "", "raison": "montants de contexte seulement (prix unitaire, cumul, plafond, devis, crédit, reste…)", "jetons": jetons}

    def decider(j: dict, raison_sup: str = "") -> dict:
        if j["classe"] == "partiel":
            return {"montant": "", "nature": "", "raison": "relevé partiel ou intermédiaire (premier relevé, cumulé, déjà imputé)", "jetons": jetons}
        if j["classe"] == "fourchette":
            return {"montant": "", "nature": "", "raison": f"fourchette {j['valeur']} à {j['haut']} USD, pas un montant", "jetons": jetons}
        return {"montant": j["valeur"], "nature": j["classe"], "raison": raison_sup, "jetons": jetons}

    if len(restants) == 1:
        return decider(restants[0])
    gras = [j for j in restants if j["gras"]]
    if len(gras) == 1:
        return decider(gras[0], "montant unique en gras : total de la ligne (convention du registre)")
    if len(gras) > 1:
        return {"montant": "", "nature": "", "raison": "plusieurs montants en gras", "jetons": jetons}
    releves = [j for j in restants if j["classe"] == "releve"]
    estimes = [j for j in restants if j["classe"] in ("estime", "fourchette")]
    if len(releves) == 1 and estimes and len(releves) + len(estimes) == len(restants):
        j = releves[0]
        local = texte[max(0, j["debut"] - FENETRE_AVANT):j["debut"]]
        if _MARQUE_RELEVE_LOCAL.search(local):
            return decider(j, "relevé qui remplace les estimations de la même ligne (compté une fois)")
    return {"montant": "", "nature": "", "raison": "plusieurs montants (" + ", ".join(j["texte"] for j in restants) + ")", "jetons": jetons}


def analyser_depenses_strict(dep: Fichier, gos_registre: dict[str, list[dict]]) -> dict:
    """Analyse stricte de tout le registre des dépenses : une ligne physique = au plus un montant.

    Retour : {'sommees': [...], 'estimees': [...], 'journal': [...], 'par_go': {...}, 'par_tache': {...}, 'global': {...}}.
    Une puce indentée (« - » après des espaces) hérite de la date et des GO de la puce datée qui la précède.
    Une ligne de la table à 9 colonnes (« coût (USD) » en colonne 7) est lue dans cette colonne."""
    sommees, estimees, journal = [], [], []
    date_parent, gos_parent = "", []
    for i, l in enumerate(dep.lignes):
        no = i + 1
        c = cellules_table(l)
        if c and re.match(r"^\d{4}-\d{2}-\d{2}$", c[0]):
            date, gos, abreges, texte = c[0], sorted(set(_GO.findall(l))), sorted(set(_GO_ABREGE.findall(l))), l
            if len(c) >= 7 and re.match(r"^\s*(≈\s*)?\d+(?:[,.]\d+)?\s*$", c[6]):
                v = re.match(r"^\s*(≈\s*)?(\d+(?:[,.]\d+)?)\s*$", c[6])
                dec = {"montant": v.group(2), "nature": "estime" if v.group(1) else "releve",
                       "raison": "colonne « coût (USD) » de la table", "jetons": []}
            else:
                dec = analyser_ligne_depense(" | ".join(c[1:]))
                if not dec["jetons"] and not any("USD" in cc for cc in c):
                    continue
        else:
            m = _PUCE_DATEE.match(l)
            if m:
                date_parent, gos_parent = m.group(1), sorted(set(_GO.findall(l)))
                date, gos, abreges, texte = m.group(1), gos_parent, sorted(set(_GO_ABREGE.findall(l))), m.group(2)
            elif re.match(r"^\s+-\s", l) and date_parent:
                date, gos, abreges, texte = date_parent, gos_parent, sorted(set(_GO_ABREGE.findall(l))), l.strip()[2:]
            else:
                if "USD" in l and not l.startswith("|"):      # en-tête de table (« coût (USD) ») : pas une entrée
                    journal.append({"ligne": no, "date": "", "gos": [], "raison": "ligne hors entrée (ni table datée ni puce datée) portant un montant",
                                    "montants": [j["texte"] for j in jetons_montants(l)], "texte": l})
                continue
            if "USD" not in texte:
                continue
            dec = analyser_ligne_depense(texte)
        # Tâche de la phase 0 nommée sur la ligne ; sinon dans le périmètre du GO cité (registre des GO).
        taches = sorted(set(_TACHE.findall(texte))) or \
            sorted({t for g in gos for v in gos_registre.get(g, []) for t in _TACHE.findall(v["perimetre"])})
        entree = {"ligne": no, "date": date, "gos": gos, "gos_abreges": abreges, "taches": taches, "montant": dec["montant"],
                  "nature": dec["nature"], "raison": dec["raison"], "montants": [j["texte"] for j in dec["jetons"]],
                  "texte": l, "remplacement": bool(_MARQUE_REMPLACEMENT.search(texte))}
        if not dec["montant"]:
            journal.append(entree)
        elif dec["nature"] == "releve":
            sommees.append(entree)
        else:
            estimees.append(entree)
    # Estimation remplacée par un relevé (règle écrite) : une ligne de relevé qui dit remplacer une estimation sort de la
    # colonne « estimé » les estimations antérieures du même GO (comptée une fois). Les lignes d'A1-v3 du 5 novembre 2026
    # du registre réel (sondes v9 et v10, l. 358 à 362 ; troisième course, l. 371) ne portent que des bornes (« ≤ »,
    # « au plus », « estimation de la machine ») : elles vont en colonne « estimé » ou au journal, jamais au relevé ;
    # la paire « premier relevé … 0,35 USD » (l. 326) / « 41 appels, 4,25 USD » (l. 328) est tranchée par la classe
    # « partiel » du premier relevé : seul le relevé final est sommé.
    for s in sommees:
        if s["remplacement"] and s["gos"]:
            for e in estimees:
                if e["ligne"] < s["ligne"] and set(e["gos"]) & set(s["gos"]) and not e.get("remplacee_par"):
                    e["remplacee_par"] = s["ligne"]
    estimees_retenues = [e for e in estimees if not e.get("remplacee_par")]
    for e in estimees:
        if e.get("remplacee_par"):
            journal.append(dict(e, raison=f"estimation remplacée par le relevé de la l. {e['remplacee_par']} (comptée une fois)"))

    def cle_go(e: dict) -> str:
        if len(e["gos"]) == 1:
            return e["gos"][0]
        if len(e["gos"]) > 1:
            return "(plusieurs GO cités : " + ", ".join(e["gos"]) + ")"
        if e["gos_abreges"]:
            return "(GO abrégé, non résolu : GO-" + ", GO-".join(e["gos_abreges"]) + ")"
        return "(sans GO cité)"

    def cle_tache(e: dict) -> str:
        return " + ".join(e["taches"]) if e["taches"] else "(aucune tâche de la phase 0 nommée)"

    def agreger(cle) -> dict:
        agg: dict[str, dict] = {}
        for e in sommees:
            a = agg.setdefault(cle(e), {"releve": 0.0, "lignes_sommees": [], "estime": 0.0, "lignes_estimees": [], "lignes_non_sommees": []})
            a["releve"] += montant_vers_float(e["montant"])
            a["lignes_sommees"].append(e["ligne"])
        for e in estimees_retenues:
            a = agg.setdefault(cle(e), {"releve": 0.0, "lignes_sommees": [], "estime": 0.0, "lignes_estimees": [], "lignes_non_sommees": []})
            a["estime"] += montant_vers_float(e["montant"])
            a["lignes_estimees"].append(e["ligne"])
        for e in journal:
            if e.get("date") == "" and not e.get("gos"):
                continue
            a = agg.setdefault(cle(e), {"releve": 0.0, "lignes_sommees": [], "estime": 0.0, "lignes_estimees": [], "lignes_non_sommees": []})
            a["lignes_non_sommees"].append(e["ligne"])
        return dict(sorted(agg.items()))

    total = sum(montant_vers_float(e["montant"]) for e in sommees)
    total_estime = sum(montant_vers_float(e["montant"]) for e in estimees_retenues)
    journal.sort(key=lambda e: e["ligne"])
    return {"sommees": sommees, "estimees": estimees_retenues, "journal": journal, "par_go": agreger(cle_go),
            "par_tache": agreger(cle_tache),
            "global": {"releve": total, "lignes_sommees": len(sommees), "estime": total_estime,
                       "lignes_estimees": len(estimees_retenues), "lignes_non_sommees": len(journal)}}


# --------------------------------------------------------------------------- verdicts, préenregistrements, runs
def lire_verdicts(racine: Path) -> list[dict]:
    dossier = racine / CHEMINS["verdicts"]
    verdicts = []
    for p in sorted(dossier.glob("*.md")):
        f = Fichier(racine, str(p.relative_to(racine)), scelle=True)
        # Ligne de verdict : première ligne portant « Verdict » en gras ou dans la section « Verdict », sinon la ligne 3.
        ligne_verdict = None
        for no, l in f.section(r"Verdict"):
            if l.strip():
                ligne_verdict = (no, l)
                break
        if ligne_verdict is None:
            for no, l in f.chercher(r"\*\*(Verdict|Nœud|Conclusion)"):
                ligne_verdict = (no, l)
                break
        if ligne_verdict is None and len(f.lignes) >= 3:
            ligne_verdict = (3, f.lignes[2])
        verdicts.append({"fichier": f, "nom": p.name, "ligne_verdict": ligne_verdict,
                         "prereg_cites": sorted(set(re.findall(r"prereg/([\w.\-]+\.md)", "\n".join(f.lignes)))),
                         "runs": sorted(set(_RUN.findall("\n".join(f.lignes)))),
                         "gos": sorted(set(_GO.findall("\n".join(f.lignes))))})
    return verdicts


def identifiants_cellule(cellule: str) -> list[str]:
    """Identifiants de prédiction d'une première cellule : « Rk-7, Rk-8 » → [« Rk-7 », « Rk-8 »] ; « P1 : énoncé » → [« P1 »]."""
    brut = cellule.strip("*").strip()
    brut = brut.split(" : ")[0].split(" :")[0] if " :" in brut else brut
    brut = brut.split(" (")[0]                     # « P3-P4 (validité, niveau 1) » → « P3-P4 »
    parts = [p.strip() for p in brut.split(",")]
    ids = [m.group(1) for m in (_ID_PRED.match(p) for p in parts) if m]
    if len(ids) == len(parts) and len(parts) > 1:  # « Rk-7, Rk-8 » : plusieurs identifiants, tous bien formés
        return ids
    return ids[:1]                                 # « A1, jeux qui demandent … » : un identifiant, une description


def predictions_du_prereg(f: Fichier) -> list[dict]:
    """Lignes de la section « Prédiction chiffrée et signe attendu » : tables (première cellule = identifiant, ou
    plusieurs identifiants séparés par des virgules) et puces `- **ID** …`. Sans l'un ni l'autre : une ligne
    « (section entière) » avec le premier paragraphe."""
    sect = f.section(r"Prédiction chiffrée et signe attendu")
    preds = []
    en_tete_vu = False
    for no, l in sect:
        c = cellules_table(l)
        if c:
            if re.match(r"^:?-{3,}:?$", c[0]) or re.match(r"^\s*(id|#|n°|prédiction|contrôle|grandeur)\s*$", c[0], re.I):
                en_tete_vu = True
                continue
            if not en_tete_vu and len(preds) == 0 and len(c) >= 2 and not _ID_PRED.match(c[0]):
                continue
            ids = identifiants_cellule(c[0])
            if ids:
                identifiant = ids[0]
            else:
                brut = c[0].strip("*").strip()
                identifiant = tronquer((brut.split(" : ")[0] if " :" in brut else brut).split(",")[0], 40)
                ids = [identifiant]
            texte = " ; ".join(cc for cc in c[1:] if cc) if _ID_PRED.match(c[0]) or identifiants_cellule(c[0]) else " ; ".join(c)
            preds.append({"id": identifiant, "ids": ids, "ligne": no, "texte": tronquer(texte)})
            continue
        m = re.match(r"^\s*-\s+\*\*([A-Za-z][\w.\-]*\d[\w.\-]*)\*\*\s*[:.\]\)]?\s*(.*)$", l) or \
            re.match(r"^\s*-\s+\*\*([A-Za-z][\w.\-]*\d[\w.\-]*)\*\*\s*(\[.*)$", l)
        if m:
            preds.append({"id": m.group(1), "ids": [m.group(1)], "ligne": no, "texte": tronquer(m.group(2))})
    if not preds and sect:
        paragraphe = [l for _, l in sect if l.strip()]
        if paragraphe:
            preds.append({"id": "(section entière)", "ids": ["(section entière)"], "ligne": sect[0][0], "texte": tronquer(" ".join(paragraphe[:4]))})
    return preds


def seuil_pour(f: Fichier, identifiant: str, tous_ids: list[str]) -> tuple[str, list[int]]:
    """Lignes de la section « Seuil » qui citent l'identifiant. Si la section ne cite aucun identifiant de prédiction
    (seuil écrit en prose), sa première ligne vaut pour toutes ; si elle en cite et pas celui-ci : cellule vide."""
    sect = [(no, l) for no, l in f.section(r"^Seuil") if l.strip()]
    if not sect:
        return "", []
    motifs = {i: motif_id(i) for i in tous_ids if i != "(section entière)"}
    if identifiant in motifs:
        citees = [(no, l) for no, l in sect if motifs[identifiant].search(l)]
        if citees:
            return tronquer(" / ".join(l.strip("- ").strip() for _, l in citees)), [no for no, _ in citees]
    if any(m.search(l) for m in motifs.values() for _, l in sect):
        return "", []
    return tronquer(sect[0][1]), [sect[0][0]]


def contre_lectures(f: Fichier) -> tuple[str, list[int]]:
    """Entrées « Contre-lecture k (…) » de la section « Contre-lecture » : nombre et descripteurs."""
    sect = f.section(r"^Contre-lecture")
    entrees, lignes = [], []
    for no, l in sect:
        m = _CONTRE_LECTURE.search(l)
        if m and (l.lstrip().startswith(("-", "*", "#")) or l.startswith("**Contre")):
            desc = (m.group(3) or "").strip()
            if not desc:
                for no2, l2 in sect:
                    if no2 > no and re.search(r"Contre-lecteur\s*:", l2):
                        desc = re.sub(r".*Contre-lecteur\s*:\s*", "", l2)
                        break
            entrees.append(f"n° {m.group(1)}" + (f" ({tronquer(desc, 90)})" if desc else ""))
            lignes.append(no)
    if not entrees:
        return "", []
    return f"{len(entrees)} : " + " ; ".join(entrees), lignes


def lire_preregs(racine: Path) -> list[dict]:
    dossier = racine / CHEMINS["prereg"]
    preregs = []
    for p in sorted(dossier.glob("*.md")):
        if "brouillon" in p.name or p.name.startswith("gabarit"):
            continue
        f = Fichier(racine, str(p.relative_to(racine)), scelle=True)
        preregs.append({"fichier": f, "nom": p.name, "predictions": predictions_du_prereg(f)})
    return preregs


def lire_manifestes(racine: Path) -> list[dict]:
    runs = []
    for m in sorted((racine / CHEMINS["runs"]).glob("*/manifeste.json")):
        f = Fichier(racine, str(m.relative_to(racine)), scelle=(m.with_name(m.name + SUFFIXE)).is_file())
        d = json.loads("\n".join(f.lignes))
        pre = d.get("preenregistrement") or {}
        runs.append({"fichier": f, "run_id": d.get("run_id", m.parent.name), "cree_le": d.get("cree_le", ""),
                     "decisif": bool(d.get("decisif")), "commit": d.get("commit", ""),
                     "prereg": pre.get("chemin", "") if isinstance(pre, dict) else "",
                     "prereg_sha256": pre.get("sha256", "") if isinstance(pre, dict) else ""})
    return runs


# --------------------------------------------------------------------------- table 1 : promis → livré
MOIS_EN = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6, "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12}


def etat_periode(periode: str, jour: str) -> str:
    """« Nov–Dec 2026 », « mid-Feb – Apr 2027 » → début de période comparé au jour du script (AAAA-MM-JJ)."""
    m = re.search(r"([A-Za-z]{3})[a-z]*\s*(?:[–-]\s*[A-Za-z]{3}[a-z]*)?\s*(\d{4})", periode)
    if not m:
        return ""
    mois = MOIS_EN.get(m.group(1).lower())
    if not mois:
        return ""
    debut = f"{m.group(2)}-{mois:02d}"
    if debut > jour[:7]:
        return "à venir (période non commencée au jour du script)"
    return "période en cours au jour du script"


# Mise en page du texte extrait du PDF envoyé (`pdftotext -layout`) : titres « N. Titre » à la colonne 0, puces sans glyphe,
# table du calendrier à colonnes alignées par espaces (v3).
_TITRE_SECTION_TEXTE = re.compile(r"^\x0c?(\d{1,2})\. \S")        # un saut de page (« \x0c ») peut précéder un titre
_ITEM_NUMEROTE = re.compile(r"^\s+(\d+)\.\s+(\S.*)$")
_FIN_DE_PHRASE = re.compile(r"[.!?]\s*$")
_LIGNE_INDENTEE = re.compile(r"^\s+(\S.*)$")
_CELLULE_ALIGNEE = re.compile(r"\S+(?: \S+)*")                # une cellule : des mots séparés d'un seul espace
_ENTETE_CALENDRIER = re.compile(r"^\s*Months\s{2,}Period\s{2,}Work\s{2,}\S")
TOLERANCE_COLONNE = 2


class FichierTexte(Fichier):
    """Texte extrait d'un PDF : lignes coupées sur « \\n » seul, pour que les numéros cités soient ceux du fichier
    (`str.splitlines` couperait aussi sur les sauts de page « \\x0c » de `pdftotext`, et décalerait tous les numéros)."""

    def __init__(self, racine: Path, rel: str, scelle: bool = False):
        super().__init__(racine, rel, scelle)
        self.lignes = self.chemin.read_text(encoding="utf-8").split("\n")
        if self.lignes and self.lignes[-1] == "":            # fin de fichier : pas une ligne de plus
            self.lignes.pop()


def section_texte(f: Fichier, numero: int) -> tuple[tuple[int, str] | None, list[tuple[int, str]]]:
    """Section « N. Titre » d'un texte extrait : (ligne de titre, lignes jusqu'au prochain titre « M. … » à la colonne 0).
    Sans titre portant ce numéro : (None, [])."""
    for i, l in enumerate(f.lignes):
        m = _TITRE_SECTION_TEXTE.match(l)
        if m and int(m.group(1)) == numero:
            fin = len(f.lignes)
            for j in range(i + 1, len(f.lignes)):
                if _TITRE_SECTION_TEXTE.match(f.lignes[j]):
                    fin = j
                    break
            return (i + 1, l), [(k + 1, f.lignes[k]) for k in range(i + 1, fin)]
    return None, []


def items_indentes(lignes: list[tuple[int, str]]) -> list[dict]:
    """Puces d'une liste dont le glyphe a été perdu à l'extraction : [{'lignes': [n°…], 'texte': '…'}].
    Une puce est une suite de lignes indentées. Une puce nouvelle commence à une ligne indentée numérotée (« 1. »), ou à
    une ligne indentée qui débute par une majuscule quand la puce courante finit par une fin de phrase (« . », « ! »,
    « ? ») ; toute autre ligne indentée continue la puce courante (recollée par un espace). Une ligne vide ou à la
    colonne 0 clôt la puce courante (les étiquettes « Deliverables. », « Success. » et le paragraphe « Gate G0 » ne sont
    pas des puces)."""
    items: list[dict] = []
    courante: dict | None = None
    for no, l in lignes:
        m_num = _ITEM_NUMEROTE.match(l)
        m_ind = _LIGNE_INDENTEE.match(l)
        if m_num:
            courante = {"lignes": [no], "texte": m_num.group(2).strip()}
            items.append(courante)
        elif m_ind:
            texte = m_ind.group(1).strip()
            nouvelle = courante is None or (texte[:1].isupper() and bool(_FIN_DE_PHRASE.search(courante["texte"])))
            if nouvelle:
                courante = {"lignes": [no], "texte": texte}
                items.append(courante)
            else:
                courante["lignes"].append(no)
                courante["texte"] = f"{courante['texte']} {texte}"
        else:
            courante = None
    return items


def paragraphe_colonne_0(lignes: list[tuple[int, str]], debut: str) -> tuple[list[int], str]:
    """Paragraphe à la colonne 0 qui commence par `debut` : ses lignes consécutives non vides, recollées par un espace."""
    nos, textes = [], []
    for no, l in lignes:
        l = l.lstrip("\x0c")                                  # un saut de page devant la ligne ne l'indente pas
        if not nos:
            if l.startswith(debut):
                nos.append(no)
                textes.append(l.strip())
        elif l.strip() and not l.startswith((" ", "\t", "\x0c")):
            nos.append(no)
            textes.append(l.strip())
        else:
            break
    return nos, " ".join(textes)


def table_alignee(lignes: list[tuple[int, str]]) -> tuple[list[dict], str]:
    """Table d'un texte extrait avec `-layout` (section 7) : ([{'lignes': [n°…], 'cellules': [...]}], erreur).
    Les débuts de colonnes sont les positions des cellules de la ligne d'en-tête (« Months », « Period », « Work »,
    « Gates and outputs ») ; une cellule d'une ligne va à la dernière colonne dont le début est ≤ sa position + tolérance.
    Une ligne dont la première cellule commence par un chiffre ouvre une ligne de calendrier ; une ligne indentée dont la
    première cellule est vide la continue (cellules recollées par un espace) ; une ligne vide ou à la colonne 0 la clôt
    et finit la table. Sans en-tête : ([], raison)."""
    entete = next(((no, l) for no, l in lignes if _ENTETE_CALENDRIER.match(l)), None)
    if entete is None:
        return [], "en-tête « Months … Period … Work … » absent"
    debuts = [m.start() for m in _CELLULE_ALIGNEE.finditer(entete[1])]

    def cellules(l: str) -> list[str]:
        cells = [""] * len(debuts)
        for m in _CELLULE_ALIGNEE.finditer(l):
            k = max((i for i, d in enumerate(debuts) if d <= m.start() + TOLERANCE_COLONNE), default=0)
            cells[k] = f"{cells[k]} {m.group(0)}".strip()
        return cells

    rangs: list[dict] = []
    courante: dict | None = None
    for no, l in lignes:
        if no <= entete[0]:
            continue
        l = l.replace("\x0c", " ")                            # un saut de page garde la position des colonnes
        c = cellules(l)
        if c[0] and c[0][0].isdigit():
            courante = {"lignes": [no], "cellules": c}
            rangs.append(courante)
        elif courante is not None and not c[0] and l.startswith(" ") and l.strip():
            courante["lignes"].append(no)
            courante["cellules"] = [f"{a} {b}".strip() for a, b in zip(courante["cellules"], c)]
        elif rangs:
            break
    return rangs, "" if rangs else "aucune ligne de calendrier sous l'en-tête"


def table_promis(racine: Path, jour: str, S: Sources, verdicts: list[dict], runs: list[dict]) -> list[dict]:
    T = "promis-livre-v3"
    cand = FichierTexte(racine, CHEMINS["candidature"], scelle=True)
    prog = Fichier(racine, CHEMINS["programme"], scelle=True)
    etat = Fichier(racine, CHEMINS["etat"])
    deci = Fichier(racine, CHEMINS["decisions"])
    for f in (cand, prog, etat, deci):
        S.fichier(f)
    taches = lire_etat_taches(etat)
    crit_etat = lire_criteres_g0_etat(etat)
    lignes = []

    def piece_de_tache(tache: str | None, ligne_id: str) -> tuple[str, str]:
        """Pièce (verdict le plus récent dont le nom porte la tâche, sinon run décisif cité par la ligne d'état)."""
        if not tache:
            return "", ""
        vs = [v for v in verdicts if tache in v["nom"] and v["nom"].startswith("verdict-")]
        if vs:
            v = vs[-1]
            S.cellule(T, ligne_id, "piece", v["fichier"], [v["ligne_verdict"][0]] if v["ligne_verdict"] else [1])
            return f"`{v['fichier'].rel}`", v["fichier"].sha256
        t = taches.get(tache)
        if t:
            for r in runs:
                if r["decisif"] and r["run_id"] in t["runs"]:
                    S.cellule(T, ligne_id, "piece", r["fichier"], [1], "manifeste du run décisif cité par la ligne d'état")
                    return f"`{r['fichier'].rel}`", r["fichier"].sha256
        return "", ""

    def etat_de_tache(tache: str | None, ligne_id: str) -> str:
        t = taches.get(tache or "")
        if not t:
            return ""
        S.cellule(T, ligne_id, "etat", etat, [t["ligne"]])
        return tronquer(t["etat_court"], 160)

    def glissement(tache: str | None, ligne_id: str) -> str:
        t = taches.get(tache or "")
        if t and t["reste"]:
            S.cellule(T, ligne_id, "glissement", etat, [t["ligne"]], "segment « Reste : » de la ligne d'état")
            return "Reste : " + tronquer(t["reste"], 200)
        return ""

    # (a) Critères de la porte G0 (programme, phase 0) ; numérotés dans l'ordre du programme (huit : G1 et papier C séparés).
    porte = [(no, l) for no, l in prog.section(r"Phase 0") if l.startswith("**Porte G0")]
    date_g0 = [(no, l) for no, l in prog.chercher(r"^\| M0 .*porte G0")]
    noeud_g0 = [(no, l) for no, l in etat.section(r"Phase en cours") if "N-027" in l]
    n027 = [(no, l) for no, l in deci.chercher(r"^\| N-027 \|")]
    if porte:
        no_porte, l_porte = porte[0]
        corps = re.sub(r"^\*\*Porte G0[^*]*\*\*\s*:\s*", "", l_porte).rstrip(". ")
        items = []
        for it in [x.strip() for x in corps.split(";")]:
            m = re.match(r"préenregistrements de (G1) et du (papier C) (.*)$", it)
            if m:
                items += [f"préenregistrement de {m.group(1)} {m.group(3)}", f"préenregistrement du {m.group(2)} {m.group(3)}"]
            else:
                items.append(it)
        for k, it in enumerate(items, 1):
            lid = f"G0-{k}"
            tache = next((t for motif, t in REGLES_CRITERES_G0 if re.search(motif, it, re.I)), None)
            S.cellule(T, lid, "promesse", prog, [no_porte])
            promis_le = ""
            if date_g0:
                promis_le = re.sub(r"^\|\s*|\s*\|.*$", "", date_g0[0][1])
                S.cellule(T, lid, "date_promise", prog, [date_g0[0][0]])
            if str(k) in crit_etat["prouves"]:
                etat_txt = f"prouvé ({crit_etat['prouves'][str(k)]})"
                S.cellule(T, lid, "etat", etat, [crit_etat["ligne"]])
            elif str(k) in crit_etat["restent"]:
                etat_txt = f"reste ({crit_etat['restent'][str(k)]})"
                S.cellule(T, lid, "etat", etat, [crit_etat["ligne"]])
            else:
                etat_txt = etat_de_tache(tache, lid)
            piece, sha = "", ""
            vs = [v for v in verdicts if re.search(rf"critere-{k}-G0", v["nom"])]
            if vs:
                v = vs[-1]
                S.cellule(T, lid, "piece", v["fichier"], [v["ligne_verdict"][0]] if v["ligne_verdict"] else [1])
                piece, sha = f"`{v['fichier'].rel}`", v["fichier"].sha256
            else:
                piece, sha = piece_de_tache(tache, lid)
            gl = []
            if str(k) not in crit_etat["prouves"]:
                if noeud_g0:
                    gl.append(tronquer(re.sub(r"^.*?Porte de sortie\s*:\s*", "", noeud_g0[0][1]), 120))
                    S.cellule(T, lid, "glissement", etat, [noeud_g0[0][0]])
                g = glissement(tache, lid + "-reste")
                if g:
                    gl.append(g)
                if n027:
                    S.cellule(T, lid, "glissement_decision", deci, [n027[0][0]], "ligne N-027 du registre des décisions")
            lignes.append({"id": lid, "source": "programme v2, porte G0", "promesse": it, "date_promise": promis_le,
                           "etat": etat_txt, "piece": piece, "sha256": sha, "glissement": " — ".join(gl)})

    # (b) Candidature envoyée, section 6 « Progress to date » : chaque puce (glyphe perdu à l'extraction) est une promesse
    # de ce qui existe ; le paragraphe « Gate G0 » à la colonne 0 donne la ligne C6-G0.
    titre6, s6 = section_texte(cand, 6)
    if titre6 is None or not re.match(r"^6\. Progress to date", titre6[1]):
        S.signaler("section 6 « Progress to date » absente de la candidature : aucune ligne C6", cand, titre6[0] if titre6 else 0,
                   titre6[1] if titre6 else "")
        s6 = []
    periode6 = re.sub(r"^6\. Progress to date\s*", "", titre6[1]).strip("() ") if titre6 else ""
    for k, it in enumerate(items_indentes(s6), 1):
        lid = f"C6-{k}"
        texte = it["texte"]
        tache = next((t for motif, t in REGLES_CANDIDATURE if re.search(motif, texte, re.I)), None)
        S.cellule(T, lid, "promesse", cand, it["lignes"])
        S.cellule(T, lid, "date_promise", cand, it["lignes"] + [titre6[0]], "puce de la section 6 ; période lue dans le titre de la section")
        piece, sha = piece_de_tache(tache, lid)
        lignes.append({"id": lid, "source": "candidature, section 6", "promesse": tronquer(texte, 260),
                       "date_promise": f"déclaré fait à la candidature ({periode6})", "etat": etat_de_tache(tache, lid),
                       "piece": piece, "sha256": sha, "glissement": glissement(tache, lid)})
    nos_g0, texte_g0 = paragraphe_colonne_0(s6, "Gate G0")
    if nos_g0:
        lid = "C6-G0"
        S.cellule(T, lid, "promesse", cand, nos_g0)
        S.cellule(T, lid, "date_promise", cand, nos_g0)
        m2 = re.search(r"\(([^)]*\d{4})\)", texte_g0)
        etat_txt, gl = "", ""
        if crit_etat["ligne"]:
            etat_txt = (f"prouvés : {', '.join(sorted(crit_etat['prouves']))} ; "
                        f"restent : {', '.join(sorted(crit_etat['restent']))}")
            S.cellule(T, lid, "etat", etat, [crit_etat["ligne"]])
        if noeud_g0:
            gl = tronquer(re.sub(r"^.*?Porte de sortie\s*:\s*", "", noeud_g0[0][1]), 160)
            S.cellule(T, lid, "glissement", etat, [noeud_g0[0][0]])
        if n027:
            S.cellule(T, lid, "glissement_decision", deci, [n027[0][0]])
        lignes.append({"id": lid, "source": "candidature, section 6", "promesse": tronquer(texte_g0, 300),
                       "date_promise": m2.group(1) if m2 else "", "etat": etat_txt, "piece": "", "sha256": "",
                       "glissement": gl})
    elif s6:
        S.signaler("paragraphe « Gate G0 » absent de la section 6 : aucune ligne C6-G0", cand, titre6[0], titre6[1])

    # (c) Candidature envoyée, section 7 « Timeline » : une ligne par ligne du calendrier (table à colonnes alignées,
    # une ligne de calendrier peut courir sur plusieurs lignes physiques, recollées).
    titre7, s7 = section_texte(cand, 7)
    if titre7 is None or not re.match(r"^7\. Timeline", titre7[1]):
        S.signaler("section 7 « Timeline » absente de la candidature : aucune ligne C7", cand, titre7[0] if titre7 else 0,
                   titre7[1] if titre7 else "")
        titre7, s7 = None, []
    rangs, erreur7 = table_alignee(s7) if s7 else ([], "")
    if erreur7:
        S.signaler(f"table de la section 7 illisible ({erreur7}) : aucune ligne C7", cand, titre7[0], titre7[1])
    for k, r in enumerate(rangs, 1):
        lid = f"C7-{k}"
        c = r["cellules"] + [""] * max(0, 4 - len(r["cellules"]))
        S.cellule(T, lid, "promesse", cand, r["lignes"])
        S.cellule(T, lid, "date_promise", cand, r["lignes"])
        etat_txt = etat_periode(c[1], jour)
        if etat_txt:
            S.cellule(T, lid, "etat", cand, r["lignes"], "période de la ligne comparée au jour du script")
        lignes.append({"id": lid, "source": "candidature, section 7", "promesse": tronquer(f"{c[2]} → {c[3]}", 260),
                       "date_promise": f"mois {c[0]} ({c[1]})", "etat": etat_txt, "piece": "", "sha256": "", "glissement": ""})

    # (d) Candidature envoyée, section 8 « Deliverables and success criteria » : livrables (puces sans glyphe) puis
    # critères de succès (numérotés « 1. ») ; la date promise est la période du titre de la section 7.
    titre8, s8 = section_texte(cand, 8)
    if titre8 is None or not re.match(r"^8\. Deliverables", titre8[1]):
        S.signaler("section 8 « Deliverables and success criteria » absente de la candidature : aucune ligne C8", cand,
                   titre8[0] if titre8 else 0, titre8[1] if titre8 else "")
        s8 = []
    periode7 = re.sub(r"^7\. Timeline\s*", "", titre7[1]).strip("() ") if titre7 else ""
    date_c8 = f"fin de la période (section 7 : {periode7})" if periode7 else ""
    for k, it in enumerate(items_indentes(s8), 1):
        lid = f"C8-{k}"
        S.cellule(T, lid, "promesse", cand, it["lignes"])
        if date_c8:
            S.cellule(T, lid, "date_promise", cand, it["lignes"] + [titre7[0]], "période lue dans le titre de la section 7")
        lignes.append({"id": lid, "source": "candidature, section 8", "promesse": tronquer(it["texte"], 260),
                       "date_promise": date_c8, "etat": "", "piece": "", "sha256": "", "glissement": ""})
    return lignes


# --------------------------------------------------------------------------- table 2 : calibration
def classer(texte: str) -> str:
    for mot, issue in ISSUES:
        if re.search(mot, texte, re.I):
            return issue
    return ""


def tables_du_fichier(f: Fichier) -> list[dict]:
    """Tables markdown du fichier : [{'entete': [...] ou None, 'lignes': [(no, cellules), …]}]. Un en-tête est la
    première ligne d'une table suivie d'une ligne séparatrice `|---|`."""
    tables, courante = [], None
    for i, l in enumerate(f.lignes):
        c = cellules_table(l)
        if c:
            if courante is None:
                courante = {"entete": None, "lignes": []}
                tables.append(courante)
            if est_separateur(c):
                if courante["lignes"] and len(courante["lignes"]) == 1 and courante["entete"] is None:
                    courante["entete"] = courante["lignes"].pop()[1]
                continue
            courante["lignes"].append((i + 1, c))
        else:
            courante = None
    return tables


def issue_table_de_lecture(f: Fichier, identifiant: str) -> tuple[str, list[int]]:
    """Changement 2 : issue lue dans la table de lecture du verdict, dans tout le fichier — lignes de table dont la
    première cellule est l'identifiant. Si l'en-tête a une colonne d'issue (« conforme », « lecture », « issue »,
    « verdict », « résultat », « conclusion », « statut »), sa cellule est lue (« oui » / « non » compris) ; une table
    recopiée du préenregistrement (en-tête « réfutation », « prédiction », sans colonne d'issue) n'est pas lue ; sans
    en-tête, les autres cellules sont lues par mots-clés. Contradictions entre lignes rapportées, jamais tranchées."""
    motif = motif_id(identifiant)
    trouvees: dict[str, list[int]] = {}
    for t in tables_du_fichier(f):
        entete = t["entete"] or []
        cols_issue = []
        for r in _ENTETES_ISSUE:
            cols_issue += [k for k, h in enumerate(entete) if r.search(h) and k not in cols_issue]
        recopiee = bool(entete) and not cols_issue and any(_ENTETE_PREDICTION.search(h) for h in entete)
        for no, c in t["lignes"]:
            if not c or not motif.fullmatch(c[0].strip("*").split(",")[0].split(" (")[0].strip()):
                continue
            if recopiee:
                continue
            issue = ""
            for k in cols_issue:
                if k < len(c):
                    m_on = _OUI_NON_TETE.match(c[k])
                    table_oui_non = OUI_NON_REFUTATION if _ENTETE_REFUTATION_ATTEINTE.search(entete[k]) else OUI_NON
                    issue = table_oui_non[m_on.group(1).lower()] if m_on else classer(c[k])
                    if issue:
                        break
            if not issue:
                issue = classer(" | ".join(c[1:]))
            if issue:
                trouvees.setdefault(issue, []).append(no)
    return _resoudre(trouvees)


def issue_dans(lignes: list[tuple[int, str]], identifiant: str, tables_aussi: bool = False) -> tuple[str, list[int]]:
    """Issue d'une prédiction lue par mots-clés dans les lignes de prose qui la citent (contradictions signalées,
    jamais tranchées). Avec `tables_aussi`, seul « sans objet » est lu dans les cellules de table qui citent l'identifiant."""
    motif = motif_id(identifiant)
    trouvees: dict[str, list[int]] = {}
    # Prose : paragraphes (lignes consécutives non vides, hors tables et titres ; une puce ouvre un paragraphe), lus par
    # segments (séparés par « ; » ou par une fin de phrase) ; une phrase coupée par un retour à la ligne est ainsi lue
    # entière, et une ligne qui cite plusieurs prédictions ne donne à chacune que ses propres segments. Les lignes citées
    # sont celles du paragraphe qui portent l'identifiant.
    paragraphe: list[tuple[int, str]] = []

    def lire_paragraphe():
        if not paragraphe:
            return
        texte = " ".join(l.strip() for _, l in paragraphe)
        if motif.search(texte):
            for seg in _SEGMENT.split(texte):             # chaque segment est classé à part : contradictions visibles
                # Le code en ligne (« `controle_contraire` faux ») n'est pas une lecture : retiré avant les mots-clés.
                issue = classer(re.sub(r"`[^`]*`", " ", seg)) if motif.search(seg) else ""
                if issue:
                    for no, l in paragraphe:
                        if motif.search(l) and no not in trouvees.setdefault(issue, []):
                            trouvees[issue].append(no)
        paragraphe.clear()

    for no, l in lignes:
        if l.startswith("|"):
            lire_paragraphe()
            if not tables_aussi:
                continue
            cellules = [c for c in cellules_table(l) if motif.search(c)]
            if cellules and any(re.search(r"sans objet", c, re.I) for c in cellules):
                trouvees.setdefault("sans objet", []).append(no)
            continue
        if re.match(r"^\s*([-*]|\d+\.)\s", l):              # une puce ou un numéro ouvre un paragraphe
            lire_paragraphe()
        if not l.strip() or l.startswith("#"):
            lire_paragraphe()
            if l.startswith("#") and motif.search(l):
                issue = classer(l)
                if issue:
                    trouvees.setdefault(issue, []).append(no)
            continue
        paragraphe.append((no, l))
    lire_paragraphe()
    return _resoudre(trouvees)


def _resoudre(trouvees: dict[str, list[int]]) -> tuple[str, list[int]]:
    if not trouvees:
        return "", []
    if len(trouvees) == 1:
        issue, nos = next(iter(trouvees.items()))
        return issue, nos
    return "contradictoire (" + " / ".join(f"{i} l. {','.join(map(str, n))}" for i, n in trouvees.items()) + ")", \
        [n for ns in trouvees.values() for n in ns]


def issue_pour_verdict(f: Fichier, identifiant: str) -> tuple[str, list[int], str]:
    """Issue d'une prédiction dans un verdict : (issue, lignes, note de méthode).

    1. Table de lecture du verdict (tout le fichier) : prime, même contradictoire.
    2. Sinon mots-clés dans la prose : tête (40 premières lignes), section « Verdict », tout le texte ; la première
       lecture non contradictoire l'emporte, sinon la première contradiction est rapportée telle quelle.
    3. Sinon « sans objet » lu dans une cellule de table qui cite l'identifiant sans l'avoir en première cellule (seule
       lecture permise hors tête de ligne : les autres mots-clés y sont trop bruyants)."""
    issue, nos = issue_table_de_lecture(f, identifiant)
    if issue:
        return issue, nos, "table de lecture du verdict (ligne dont la première cellule est l'identifiant)"
    candidats = [[(i + 1, l) for i, l in enumerate(f.lignes[:40])], f.section(r"Verdict"),
                 [(i + 1, l) for i, l in enumerate(f.lignes)]]
    premiere = ("", [])
    for lignes in candidats:
        issue, nos = issue_dans(lignes, identifiant)
        if issue and not issue.startswith("contradictoire"):
            return issue, nos, "mots-clés d'issue lus dans les lignes de prose citées (aucune ligne de table de lecture)"
        if issue and not premiere[0]:
            premiere = (issue, nos)
    if premiere[0]:
        return premiere[0], premiere[1], "mots-clés d'issue lus dans les lignes de prose citées (aucune ligne de table de lecture)"
    issue, nos = issue_dans(candidats[2], identifiant, tables_aussi=True)
    if issue == "sans objet":                       # seule lecture permise dans une cellule qui n'est pas en tête de ligne
        return issue, nos, "« sans objet » lu dans une cellule de table qui cite l'identifiant (aucune ligne de prose ni de table de lecture ne le cite)"
    return "", [], ""


def issue_pour_prediction(f: Fichier, ids: list[str]) -> tuple[str, list[int], str]:
    """Une ligne de prédiction peut porter plusieurs identifiants (« Rk-7, Rk-8 ») : issue de chacun ; une seule issue
    partagée par tous → celle-ci ; sinon « mixte (…) » détaillée, jamais tranchée."""
    lectures = [(i, *issue_pour_verdict(f, i)) for i in ids]
    trouvees = [(i, iss, nos, note) for i, iss, nos, note in lectures if iss]
    if not trouvees:
        return "", [], ""
    if len(ids) == 1 or (len(trouvees) == len(ids) and len({iss for _, iss, _, _ in trouvees}) == 1):
        return trouvees[0][1], sorted({n for _, _, nos, _ in trouvees for n in nos}), trouvees[0][3]
    detail = " ; ".join(f"{i} : {iss} l. {','.join(map(str, nos))}" for i, iss, nos, _ in trouvees)
    manquants = [i for i in ids if i not in {t[0] for t in trouvees}]
    if manquants:
        detail += " ; " + ", ".join(manquants) + " : non cité"
    return f"mixte ({detail})", sorted({n for _, _, nos, _ in trouvees for n in nos}), "plusieurs identifiants sur la ligne de prédiction, lus séparément"


def table_calibration(racine: Path, S: Sources, preregs: list[dict], verdicts: list[dict], runs: list[dict]) -> list[dict]:
    T = "calibration-v3"
    deci = Fichier(racine, CHEMINS["decisions"])
    S.fichier(deci)
    lignes = []
    for pr in preregs:
        f = pr["fichier"]
        vs = [v for v in verdicts if pr["nom"] in v["prereg_cites"]]
        rs = [r for r in runs if r["prereg"].endswith("/" + pr["nom"]) or r["prereg"] == pr["nom"]]
        run_ids = [r["run_id"] for r in rs]
        cibles = [pr["nom"]] + run_ids
        deci_lignes = [(i + 1, l) for i, l in enumerate(deci.lignes)
                       if any(c in l for c in cibles) and MOTS_VERDICT_DECISIONS.search(l) and l.startswith("|")]
        cl_texte, cl_lignes = contre_lectures(f)
        for p in pr["predictions"]:
            lid = f"{pr['nom']}#{p['id']}"
            S.cellule(T, lid, "prediction", f, [p["ligne"]])
            seuil, seuil_lignes = seuil_pour(f, p["id"], [q["id"] for q in pr["predictions"]])
            if seuil:
                S.cellule(T, lid, "seuil", f, seuil_lignes)
            if cl_texte:
                S.cellule(T, lid, "contre_lecture", f, cl_lignes)
            verdict_txt, verdict_sha, issue = "", "", ""
            if vs:
                v = vs[-1]                                   # version la plus récente (tri par nom)
                verdict_txt = f"`{v['fichier'].rel}`"
                verdict_sha = v["fichier"].sha256
                S.cellule(T, lid, "verdict", v["fichier"], [v["ligne_verdict"][0]] if v["ligne_verdict"] else [1])
                issue, nos, note = issue_pour_prediction(v["fichier"], p.get("ids") or [p["id"]])
                if issue:
                    S.cellule(T, lid, "issue", v["fichier"], nos, note)
                else:
                    issue = "non citée par le verdict"
                    S.cellule(T, lid, "issue", v["fichier"], [1], "aucune ligne du verdict ne cite cet identifiant")
            elif deci_lignes:
                no, l = deci_lignes[-1]
                c = cellules_table(l)
                issue = (f"registre des décisions, {c[0] if c else 'l. ' + str(no)} (pas de verdict scellé) : "
                         + tronquer(c[2] if len(c) > 2 else l, 160))
                S.cellule(T, lid, "issue", deci, [no for no, _ in deci_lignes], "lignes du registre citant le préenregistrement ou son run et prononçant")
            elif any(r["decisif"] for r in rs):
                issue = "non encore lue (run décisif fait, aucun verdict scellé)"
                r = next(r for r in rs if r["decisif"])
                S.cellule(T, lid, "issue", r["fichier"], [1], "manifeste du run décisif")
            else:
                issue = "sans run décisif cité par un manifeste"
            if run_ids:
                S.cellule(T, lid, "runs", rs[0]["fichier"], [1], "manifestes citant ce préenregistrement")
            lignes.append({"id": lid, "prereg": f"`{f.rel}`", "prereg_sha256": f.sha256, "prediction_id": ", ".join(p.get("ids") or [p["id"]]),
                           "prediction": p["texte"], "seuil": seuil, "verdict": verdict_txt, "verdict_sha256": verdict_sha,
                           "issue": issue, "contre_lecture": cl_texte, "runs": ", ".join(run_ids)})
    return lignes


# --------------------------------------------------------------------------- comptes alignés sur la table (changement 1)
def categorie_issue(issue: str) -> str:
    for prefixe, cat in CATEGORIES_ISSUE:
        if issue.startswith(prefixe):
            return cat
    return issue or "(vide)"


def compter_issues_table_md(texte_md: str, nom_colonne: str = "issue") -> dict:
    """Comptes par issue lus dans le texte markdown de la table rendue (jamais saisis) : la première ligne de table est
    l'en-tête ; la colonne `nom_colonne` donne l'issue de chaque ligne de données. Taux de confirmation parmi les
    tranchées = confirmées / (confirmées + réfutées + non concluantes) ; « sans objet », « non atteinte », « non
    déclenchée », les contradictoires et les lignes sans verdict scellé n'entrent ni au numérateur ni au dénominateur."""
    entete, col, par_issue, total = None, None, {}, 0
    for l in texte_md.splitlines():
        c = cellules_table(l)
        if not c:
            continue
        if entete is None:
            entete = c
            col = next((k for k, h in enumerate(c) if h.strip().lower() == nom_colonne), None)
            if col is None:
                raise GardeArret(f"colonne « {nom_colonne} » absente de l'en-tête de la table rendue")
            continue
        if est_separateur(c):
            continue
        total += 1
        cat = categorie_issue(c[col] if col < len(c) else "")
        par_issue[cat] = par_issue.get(cat, 0) + 1
    confirmees = par_issue.get("confirmée", 0)
    tranchees = sum(par_issue.get(k, 0) for k in TRANCHEES)
    taux = confirmees / tranchees if tranchees else None
    return {"total": total, "par_issue": dict(sorted(par_issue.items())), "tranchees": tranchees, "confirmees": confirmees,
            "refutees": par_issue.get("réfutée", 0), "non_concluantes": par_issue.get("non concluante", 0),
            "sans_objet": par_issue.get("sans objet", 0),
            "taux_confirmation": f"{confirmees} / {tranchees} = {taux:.3f}".replace(".", ",") if taux is not None else "",
            "taux_confirmation_valeur": round(taux, 4) if taux is not None else None}


def bloc_comptes_md(comptes: dict) -> str:
    out = ["## Comptes par issue (calculés depuis les lignes de la table ci-dessus, jamais saisis)", "",
           "| issue (catégorie) | lignes |", "|---|---|"]
    for cat, n in comptes["par_issue"].items():
        out.append(f"| {cellule_md(cat)} | {n} |")
    out += [f"| **total** | **{comptes['total']}** |", "",
            f"Tranchées (confirmée + réfutée + non concluante) : {comptes['tranchees']} ; confirmées : {comptes['confirmees']} ; "
            f"réfutées : {comptes['refutees']} ; non concluantes : {comptes['non_concluantes']}.",
            f"Taux de confirmation parmi les tranchées : **{comptes['taux_confirmation'] or 'aucune tranchée'}**.",
            f"« Sans objet » (contrôle sans cible établie) : {comptes['sans_objet']}, rapportées à part, hors numérateur et hors dénominateur ; "
            "« non atteinte », « non déclenchée », contradictoires, mixtes et lignes sans verdict scellé : hors du taux.", ""]
    return "\n".join(out)


# --------------------------------------------------------------------------- table 3 : coût par résultat
def table_cout(racine: Path, S: Sources, verdicts: list[dict], runs: list[dict]) -> list[dict]:
    T = "cout-par-resultat-v3"
    dep = Fichier(racine, CHEMINS["depenses"])
    arr = Fichier(racine, CHEMINS["arrets"])
    go = Fichier(racine, CHEMINS["go"])
    for f in (dep, arr, go):
        S.fichier(f)
    entrees = lire_depenses(dep)
    arrets = lire_arrets(arr)
    gos = lire_go(go)
    lignes = []

    def sans_go(e: dict) -> bool:
        return (not e["gos"] and not e["gos_abreges"] and not e["engagement"] and not e["releve"]
                and bool(e["montant"] or e["montants_retenus"]))

    for e in entrees:                                   # dépense sans GO → signalée ; GO abrégé → signalé à part
        if sans_go(e):
            S.signaler("dépense sans GO cité sur la ligne", dep, e["ligne"], e["texte"])
        elif not e["gos"] and e["gos_abreges"] and not e["engagement"] and not e["releve"] and (e["montant"] or e["montants_retenus"]):
            S.signaler("GO cité sous forme abrégée, non résolu", dep, e["ligne"], e["texte"])

    # (a) Une ligne par run décisif.
    for r in [r for r in runs if r["decisif"]]:
        lid = r["run_id"]
        S.cellule(T, lid, "run", r["fichier"], [1])
        instances = sorted({i for a in arrets if r["run_id"] in a["runs"] for i in a["instances"]})
        if instances:
            S.cellule(T, lid, "instance", arr, [a["ligne"] for a in arrets if r["run_id"] in a["runs"]])
        lies = [e for e in entrees if (r["run_id"] in e["runs"] or any(i in e["instances"] for i in instances))
                and (e["montants_retenus"] or e["engagement"])]
        gos_run = sorted({g for e in lies for g in e["gos"]})
        montant, nos, montants_txt = "", [], []
        constatees = [e for e in lies if not e["engagement"]]
        if any(e["forme"] == "table" for e in constatees):   # la table du registre prime sur les puces (pas de double compte)
            constatees = [e for e in constatees if e["forme"] == "table"]
        if all(e["montant"] for e in constatees) and constatees:
            total = sum(montant_vers_float(e["montant"]) for e in constatees)
            montant = nombre_fr(total)
            nos = [e["ligne"] for e in constatees]
        for e in lies:
            montants_txt.append(f"l. {e['ligne']} : {', '.join(e['montants_retenus']) or '—'}" + (" (engagement)" if e["engagement"] else ""))
        if montant:
            S.cellule(T, lid, "montant", dep, nos, "somme des montants des lignes constatées citant le run ou son instance "
                                                   "(lignes de table d'abord, puces sinon)")
        elif lies:
            S.cellule(T, lid, "montants_lus", dep, [e["ligne"] for e in lies], "plusieurs montants par ligne : non tranché")
        if gos_run:
            S.cellule(T, lid, "go", dep, [e["ligne"] for e in lies if e["gos"]])
        vs = [v for v in verdicts if r["run_id"] in v["runs"]]
        if vs:
            S.cellule(T, lid, "resultat", vs[-1]["fichier"], [vs[-1]["ligne_verdict"][0]] if vs[-1]["ligne_verdict"] else [1])
        par_verdict = nombre_fr(montant_vers_float(montant) / len(vs)) if montant and vs else ""
        arrets_run = [a for a in arrets if r["run_id"] in a["runs"]]
        if arrets_run:
            S.cellule(T, lid, "arrets", arr, [a["ligne"] for a in arrets_run])
        lignes.append({"id": lid, "type": "run décisif", "date": r["cree_le"][:10], "instance": ", ".join(instances),
                       "arrets": " ; ".join(texte_arret(a) for a in arrets_run),
                       "go": ", ".join(gos_run), "montant": montant, "montants_lus": " ; ".join(montants_txt),
                       "resultat": " ; ".join(f"`{v['fichier'].rel}`" for v in vs), "nb_verdicts": str(len(vs)) if vs else "0",
                       "usd_par_verdict": par_verdict, "prereg": f"`{r['prereg']}`" if r["prereg"] else ""})

    # (b) Une ligne par GO de type calcul.
    for gid, versions in sorted(gos.items()):
        if not any(v["type"].strip() == "calcul" for v in versions):
            continue
        lid = gid
        S.cellule(T, lid, "go", go, [v["ligne"] for v in versions])
        plafond = versions[-1]["plafond"]
        lies = [e for e in entrees if gid in e["gos"]]
        constatees = [e for e in lies if not e["engagement"] and e["montant"]]
        montant = nombre_fr(sum(montant_vers_float(e["montant"]) for e in constatees)) if constatees else ""
        if montant:
            S.cellule(T, lid, "montant", dep, [e["ligne"] for e in constatees],
                      "somme des montants uniques (ou en gras) des lignes constatées citant le GO ; engagements exclus")
        non_tranchees = [e for e in lies if not e["engagement"] and not e["montant"]]
        if non_tranchees:
            S.cellule(T, lid, "montants_lus", dep, [e["ligne"] for e in non_tranchees], "lignes à plusieurs montants, non sommées")
        vs = [v for v in verdicts if gid in v["gos"]]
        if vs:
            S.cellule(T, lid, "resultat", vs[-1]["fichier"], [1])
        par_verdict = nombre_fr(montant_vers_float(montant) / len(vs)) if montant and vs else ""
        arrets_go = [a for a in arrets if gid in a["gos"]]
        if arrets_go:
            S.cellule(T, lid, "arrets", arr, [a["ligne"] for a in arrets_go])
        lignes.append({"id": lid, "type": "GO calcul", "date": versions[0]["date"], "instance": "",
                       "arrets": " ; ".join(texte_arret(a) for a in arrets_go),
                       "go": tronquer(plafond, 80), "montant": montant,
                       "montants_lus": f"{len(constatees)} ligne(s) sommée(s), {len(non_tranchees)} non tranchée(s), "
                                       f"{sum(1 for e in lies if e['engagement'])} engagement(s)",
                       "resultat": " ; ".join(f"`{v['fichier'].rel}`" for v in vs), "nb_verdicts": str(len(vs)) if vs else "0",
                       "usd_par_verdict": par_verdict, "prereg": ""})

    # (c) Dépenses sans GO.
    for e in [e for e in entrees if sans_go(e)]:
        lid = f"(sans GO) l. {e['ligne']}"
        S.cellule(T, lid, "montant", dep, [e["ligne"]], "dépense sans GO : signalée")
        lignes.append({"id": lid, "type": "dépense sans GO (signalée)", "date": e["date"], "instance": ", ".join(e["instances"]),
                       "go": "", "montant": e["montant"], "montants_lus": ", ".join(e["montants"]), "resultat": "",
                       "nb_verdicts": "", "usd_par_verdict": "", "prereg": ""})
    return lignes


# --------------------------------------------------------------------------- table 4 : total des dépenses (changement 4)
def table_total_depenses(racine: Path, S: Sources) -> tuple[dict, list[dict], list[dict]]:
    """Analyse stricte du registre des dépenses : (analyse, lignes par GO, lignes par tâche) ; chaque total cite ses lignes."""
    T = "total-depenses-v3"
    dep = Fichier(racine, CHEMINS["depenses"])
    go = Fichier(racine, CHEMINS["go"])
    S.fichier(dep)
    S.fichier(go)
    gos = lire_go(go)
    A = analyser_depenses_strict(dep, gos)

    def lignes_de(agg: dict, par: str) -> list[dict]:
        out = []
        for cle, a in agg.items():
            lid = f"{par}:{cle}"
            if a["lignes_sommees"]:
                S.cellule(T, lid, "releve", dep, a["lignes_sommees"], "somme des montants relevés, un par ligne")
            if a["lignes_estimees"]:
                S.cellule(T, lid, "estime", dep, a["lignes_estimees"], "somme des estimations (« ≈ », « ≤ », « au plus »…), jamais dans le relevé")
            if a["lignes_non_sommees"]:
                S.cellule(T, lid, "non_sommees", dep, a["lignes_non_sommees"], "lignes au journal, jamais sommées")
            perimetre, plafond = "", ""
            if par == "GO" and cle in gos:
                perimetre, plafond = tronquer(gos[cle][0]["perimetre"], 120), tronquer(gos[cle][-1]["plafond"], 60)
                S.cellule(T, lid, "perimetre", go, [v["ligne"] for v in gos[cle]])
            out.append({"cle": cle, "perimetre": perimetre, "plafond": plafond,
                        "releve": nombre_fr(a["releve"]) if a["lignes_sommees"] else "",
                        "n_sommees": str(len(a["lignes_sommees"])), "l_sommees": ", ".join(map(str, a["lignes_sommees"])),
                        "estime": nombre_fr(a["estime"]) if a["lignes_estimees"] else "",
                        "n_estimees": str(len(a["lignes_estimees"])), "l_estimees": ", ".join(map(str, a["lignes_estimees"])),
                        "n_non_sommees": str(len(a["lignes_non_sommees"])), "l_non_sommees": tronquer(", ".join(map(str, a["lignes_non_sommees"])), 160)})
        return out

    par_go = lignes_de(A["par_go"], "GO")
    par_tache = lignes_de(A["par_tache"], "tâche")
    g = A["global"]
    S.cellule(T, "global", "releve", dep, [e["ligne"] for e in A["sommees"]], "total relevé de la phase 0 : somme des lignes à un montant relevé")
    if A["estimees"]:
        S.cellule(T, "global", "estime", dep, [e["ligne"] for e in A["estimees"]], "estimations, jamais dans le total relevé")
    if A["journal"]:
        S.cellule(T, "global", "non_sommees", dep, [e["ligne"] for e in A["journal"]], "journal des lignes non sommées")
    for e in A["journal"]:
        S.signaler(f"dépense non sommée : {e['raison']}", dep, e["ligne"], e["texte"])
    return A, par_go, par_tache


def rendre_total_depenses(A: dict, par_go: list[dict], par_tache: list[dict], jour: str) -> str:
    g = A["global"]
    cols = [("cle", "GO"), ("perimetre", "périmètre (registre des GO)"), ("plafond", "plafond"), ("releve", "relevé (USD)"),
            ("n_sommees", "lignes sommées"), ("l_sommees", "n° des lignes sommées"), ("estime", "estimé (USD, à part)"),
            ("n_estimees", "lignes estimées"), ("l_estimees", "n° des lignes estimées"), ("n_non_sommees", "lignes non sommées (journal)"),
            ("l_non_sommees", "n° des lignes non sommées")]
    cols_t = [(c, "tâche(s) nommée(s)" if c == "cle" else n) for c, n in cols if c not in ("perimetre", "plafond")]
    out = ["# Total des dépenses de la phase 0 — v3", "",
           "Somme des dépenses lues dans `registres/depenses.md` par un analyseur strict : une ligne du registre = au plus un "
           "montant en USD explicitement relevé. Les estimations (« ≈ », « ≤ », « au plus », « environ », « estimé », fourchettes) "
           "sont comptées à part, dans la colonne « estimé », jamais dans le total relevé. Les prix unitaires (par heure, par Go), "
           "cumuls, plafonds, devis, crédits, restes, montants d'autres projets ne sont jamais sommés. Une ligne à plusieurs "
           "montants (hors un montant unique en gras, convention du registre pour le total de la ligne), un relevé partiel "
           "(« premier relevé », « cumulés », « déjà imputé ») ou une fourchette vont au journal `journal-depenses-v3.txt`, "
           "jamais devinés ni sommés. Une ligne qui dit remplacer une estimation par un relevé compte une fois (l'estimation "
           "antérieure du même GO sort de la colonne « estimé »).", "",
           f"Jour du script (`date -u`) : {jour}. Version : `{VERSION}`. Sources de chaque cellule : `sources-v3.json`.", "",
           "## Global", "",
           "| total | USD | lignes sommées | lignes non sommées (journal) |", "|---|---|---|---|",
           f"| **relevé (phase 0)** | **{nombre_fr(g['releve'])}** | {g['lignes_sommees']} | {g['lignes_non_sommees']} |",
           f"| estimé (à part, jamais dans le relevé) | {nombre_fr(g['estime'])} | {g['lignes_estimees']} | — |", "",
           "Le total relevé est la valeur de la clé `total_depenses_phase0` de `sources-v3.json` (marqueur `<<TOTAL_DEPENSES_PHASE0>>` de la page pour le fonds).", "",
           "## Par GO", "", "| " + " | ".join(n for _, n in cols) + " |", "|" + "---|" * len(cols)]
    for l in par_go:
        out.append("| " + " | ".join(cellule_md(str(l.get(c, ""))) for c, _ in cols) + " |")
    out += ["", "## Par tâche de la phase 0 nommée sur la ligne ou dans le périmètre du GO", "",
            "| " + " | ".join(n for _, n in cols_t) + " |", "|" + "---|" * len(cols_t)]
    for l in par_tache:
        out.append("| " + " | ".join(cellule_md(str(l.get(c, ""))) for c, _ in cols_t) + " |")
    out += ["", f"Lignes sommées : {g['lignes_sommees']} ; lignes estimées : {g['lignes_estimees']} ; lignes au journal : {g['lignes_non_sommees']}.", ""]
    return "\n".join(out)


def rendre_journal_depenses(A: dict, jour: str) -> str:
    out = [f"Journal des lignes de registres/depenses.md non sommées — {VERSION} — jour {jour}",
           "Une entrée par ligne non sommée : n° de ligne, raison, montants lus, texte (tronqué). Aucune de ces lignes n'entre dans un total.", ""]
    for e in A["journal"]:
        out.append(f"l. {e['ligne']} [{e['raison']}] montants lus : {', '.join(e['montants']) or '—'} ; GO : {', '.join(e['gos']) or '—'}")
        out.append("    " + tronquer(e["texte"], 240))
    out += ["", f"Lignes au journal : {len(A['journal'])} ; lignes sommées (relevé) : {A['global']['lignes_sommees']} ; lignes estimées : {A['global']['lignes_estimees']}.", ""]
    return "\n".join(out)


# --------------------------------------------------------------------------- rendu
def rendre_table(titre: str, entete: str, colonnes: list[tuple[str, str]], lignes: list[dict], jour: str) -> str:
    out = [f"# {titre}", "", entete, "", f"Jour du script (`date -u`) : {jour}. Version : `{VERSION}`. "
           "Toute cellule vide est une cellule sans source ; aucune valeur n'est estimée. "
           "Sources de chaque cellule : `sources-v3.json`.", "",
           "| " + " | ".join(n for _, n in colonnes) + " |", "|" + "---|" * len(colonnes)]
    for l in lignes:
        out.append("| " + " | ".join(cellule_md(str(l.get(c, ""))) for c, _ in colonnes) + " |")
    vides = sum(1 for l in lignes for c, _ in colonnes if not str(l.get(c, "")).strip())
    out += ["", f"Lignes : {len(lignes)} ; cellules vides : {vides} sur {len(lignes) * len(colonnes)}.", ""]
    return "\n".join(out)


COLONNES_PROMIS = [("id", "id"), ("source", "source"), ("promesse", "promis"), ("date_promise", "date promise"),
                   ("etat", "état au jour du script"), ("piece", "pièce"), ("sha256", "empreinte de la pièce"),
                   ("glissement", "cause du glissement (registre)")]
COLONNES_CALIBRATION = [("prereg", "préenregistrement"), ("prereg_sha256", "empreinte"), ("prediction_id", "prédiction"),
                        ("prediction", "énoncé, signe, réfutation"), ("seuil", "seuil"), ("verdict", "verdict scellé"),
                        ("verdict_sha256", "empreinte du verdict"), ("issue", "issue"), ("contre_lecture", "contre-lu par"),
                        ("runs", "runs (manifestes)")]
COLONNES_COUT = [("id", "run ou GO"), ("type", "type"), ("date", "date"), ("instance", "instance"), ("go", "GO / plafond"),
                 ("montant", "montant (USD, registre des dépenses)"), ("montants_lus", "montants lus (lignes)"),
                 ("resultat", "résultat produit (verdict)"), ("nb_verdicts", "verdicts"), ("usd_par_verdict", "USD par verdict"),
                 ("prereg", "préenregistrement"), ("arrets", "arrêts et interruptions (registre des arrêts)")]


def jour_utc() -> str:
    r = subprocess.run(["date", "-u", "+%Y-%m-%d"], check=True, capture_output=True, text=True)
    return r.stdout.strip()


def construire(racine: Path, sortie: Path, jour: str) -> dict:
    racine = Path(racine).resolve()
    S = Sources()
    verdicts = lire_verdicts(racine)
    preregs = lire_preregs(racine)
    runs = lire_manifestes(racine)
    for r in runs:
        S.fichier(r["fichier"])
    promis = table_promis(racine, jour, S, verdicts, runs)
    calib = table_calibration(racine, S, preregs, verdicts, runs)
    cout = table_cout(racine, S, verdicts, runs)
    A, par_go, par_tache = table_total_depenses(racine, S)
    calib_md = rendre_table(
        "Registre de calibration des prédictions préenregistrées — v3",
        "Une ligne par prédiction des préenregistrements scellés de `prereg/` (brouillons et gabarit exclus). "
        "L'issue est lue d'abord dans la table de lecture du verdict scellé (ligne de table dont la première cellule est "
        "l'identifiant, colonne d'issue de l'en-tête), sinon par mots-clés dans la prose qui cite la prédiction (lignes "
        "citées dans `sources-v3.json`) ; « sans objet » est une issue à part ; sans verdict scellé : ligne du registre des "
        "décisions, sinon « non encore lue ».",
        COLONNES_CALIBRATION, calib, jour)
    comptes_calib = compter_issues_table_md(calib_md)            # lus dans le texte rendu, jamais dans les dicts
    calib_md = calib_md + "\n" + bloc_comptes_md(comptes_calib)
    sortie.mkdir(parents=True, exist_ok=True)
    fichiers = {
        "promis-livre-v3.md": rendre_table(
            "Promis → livré — v3", "Une ligne par critère de la porte G0 (programme v2) et par promesse de la candidature "
            "envoyée au fonds le 7 octobre 2026 (sections 6, 7, 8 de "
            f"`{CHEMINS['candidature']}`, texte extrait du PDF). L'état et la cause du glissement viennent de `registres/etat.md` ; "
            "la pièce est le verdict scellé le plus récent de la tâche, sinon le manifeste du run décisif cité.",
            COLONNES_PROMIS, promis, jour),
        "calibration-v3.md": calib_md,
        "cout-par-resultat-v3.md": rendre_table(
            "Coût réel par résultat — v3",
            "Une ligne par run décisif (manifeste `decisif` vrai) et par GO de type calcul. Le montant est la somme des "
            "montants des lignes du registre des dépenses qui citent le run, son instance (registre des arrêts) ou le GO, "
            "hors engagements ; une ligne à plusieurs montants n'est pas tranchée (cellule vide, montants listés). "
            "La dernière colonne cite les lignes du registre des arrêts qui nomment le run ou le GO (négatifs, R4). "
            "Le total strict de la phase 0 est dans `total-depenses-v3.md`.",
            COLONNES_COUT, cout, jour),
        "total-depenses-v3.md": rendre_total_depenses(A, par_go, par_tache, jour),
        "journal-depenses-v3.txt": rendre_journal_depenses(A, jour),
    }
    for nom, texte in fichiers.items():
        (sortie / nom).write_text(texte, encoding="utf-8")
    g = A["global"]
    resume = {"version": VERSION, "jour": jour, "racine": str(racine),
              "comptes": {"promis-livre-v3": len(promis), "calibration-v3": len(calib), "cout-par-resultat-v3": len(cout),
                          "total-depenses-v3": {"par_go": len(par_go), "par_tache": len(par_tache)},
                          "preregs_lus": len(preregs), "verdicts_lus": len(verdicts), "manifestes_lus": len(runs),
                          "calibration": comptes_calib},
              "total_depenses_phase0": nombre_fr(g["releve"]),
              "total_depenses_phase0_detail": {"releve_usd": nombre_fr(g["releve"]), "lignes_sommees": g["lignes_sommees"],
                                               "estime_usd_a_part": nombre_fr(g["estime"]), "lignes_estimees": g["lignes_estimees"],
                                               "lignes_non_sommees": g["lignes_non_sommees"]},
              "fichiers_lus": dict(sorted(S.fichiers.items())), "cellules": S.tables, "signalements": S.signalements}
    (sortie / "sources-v3.json").write_text(json.dumps(resume, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
                                            encoding="utf-8")
    return resume


def _main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--racine", default=".")
    ap.add_argument("--sortie", default="livrables/registres-taif-v4")
    ap.add_argument("--jour", default=None, help="AAAA-MM-JJ ; défaut : `date -u +%%Y-%%m-%%d`")
    a = ap.parse_args(argv)
    jour = a.jour or jour_utc()
    try:
        resume = construire(Path(a.racine), Path(a.racine) / a.sortie if not Path(a.sortie).is_absolute() else Path(a.sortie), jour)
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        return 2
    print(json.dumps(resume["comptes"], ensure_ascii=False))
    print(f"TOTAL RELEVÉ PHASE 0 : {resume['total_depenses_phase0']} USD ({resume['total_depenses_phase0_detail']['lignes_sommees']} lignes sommées, "
          f"{resume['total_depenses_phase0_detail']['lignes_non_sommees']} au journal)")
    for s in resume["signalements"]:
        if not s["quoi"].startswith("dépense non sommée"):
            print(f"SIGNALÉ : {s['quoi']} — {s['chemin']} l. {s['ligne']}")
    return 0


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
