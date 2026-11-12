#!/usr/bin/env python3
"""Trois tables pour l'entretien avec le Transformative AI Fund, produites par script, sans cellule saisie à la main.

Sorties (dossier `livrables/registres-taif-v1/` par défaut) :
    promis-livre-v1.md     une ligne par critère de la porte G0 et par promesse de la candidature (sections 6, 7, 8) ;
    calibration-v1.md      une ligne par prédiction préenregistrée (préenregistrements scellés de `prereg/`) ;
    cout-par-resultat-v1.md une ligne par run décisif et par GO de calcul (registre des dépenses) ;
    sources-v1.json        chaque cellule non vide → chemin, ligne(s), empreinte sha256 du fichier lu.

Règles : toute cellule sans source reste vide ; aucune estimation ; déterministe et idempotent (mêmes sources, même jour
→ mêmes octets). Le script lit : la candidature, le programme, les registres (état, décisions, GO, dépenses, arrêts),
les verdicts scellés de `docs/verdicts/`, les préenregistrements scellés de `prereg/` (brouillons et gabarit exclus),
les manifestes de `runs/*/manifeste.json`. Il ne lit jamais `diag/` ni les résultats de `runs/`.
Un verdict ou un préenregistrement sans empreinte compagnon arrête le script (R5, R6 : aucun repli silencieux).
Une dépense sans GO est signalée (liste `signalements` de `sources-v1.json`, ligne « (sans GO) » de la table 3).

    PYTHONPATH=src python scripts/registres_taif_v1.py [--racine .] [--sortie livrables/registres-taif-v1] [--jour AAAA-MM-JJ]

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

VERSION = "registres-taif-v1"
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
_CONTRE_LECTURE = re.compile(r"Contre-lecture\s+(\d+)\s*\*{0,2}\s*(\(([^)]*)\))?")
LARGEUR_CELLULE = 220

# Dossiers lus (relatifs à la racine).
CHEMINS = {
    "candidature": "livrables/candidature-ea-funds-v1/proposal-v1.md",
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
ISSUES = [
    (r"non conforme", "réfutée (non conforme)"), (r"non prouvé", "non prouvée"), (r"non établi", "non établie"),
    (r"non concluant", "non concluante"), (r"non atteint|sans objet|n'est pas atteint", "non atteinte"),
    (r"non déclench", "non déclenchée"),
    (r"réfut", "réfutée"), (r"contraire", "réfutée (contraire)"),
    (r"conforme|confirm|établi|prouvé", "confirmée"),
]
MOTS_VERDICT_DECISIONS = re.compile(r"verdict (R13|scellé|de lecture|de porte)|prononc|prouvé|non concluant|réfut|prédictions confirmées"
                                    r"|arrêté[es]* par (sa|la|leur) garde|lecture gelée", re.I)


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
    if "k-" in identifiant:                       # « Rk-1 » (par bras) se lit « R1 » dans un verdict
        variantes.append(re.escape(identifiant.replace("k-", "")))
    return re.compile(r"(?<![\w.\-])(" + "|".join(variantes) + r")(?![\w.\-])")


def cellules_table(ligne: str) -> list[str]:
    """Cellules d'une ligne de table markdown (les `|` dans du code inline sont tolérés en coupant naïvement)."""
    if not ligne.startswith("|"):
        return []
    return [c.strip() for c in ligne.strip().strip("|").split("|")]


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
    """Une entrée par ligne de table ou par puce datée portant un montant en USD.

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


def predictions_du_prereg(f: Fichier) -> list[dict]:
    """Lignes de la section « Prédiction chiffrée et signe attendu » : tables (première cellule = identifiant) et puces
    `- **ID** …`. Sans l'un ni l'autre : une ligne « (section entière) » avec le premier paragraphe."""
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
            brut = c[0].strip("*").strip()
            identifiant = brut.split(" : ")[0].split(" :")[0] if " :" in brut else brut
            m_id = _ID_PRED.match(identifiant)
            identifiant = m_id.group(1) if m_id else tronquer(identifiant.split(",")[0], 40)
            texte = " ; ".join(cc for cc in c[1:] if cc) if _ID_PRED.match(c[0]) else " ; ".join(c)
            preds.append({"id": identifiant, "ligne": no, "texte": tronquer(texte)})
            continue
        m = re.match(r"^\s*-\s+\*\*([A-Za-z][\w.\-]*\d[\w.\-]*)\*\*\s*[:.\]\)]?\s*(.*)$", l) or \
            re.match(r"^\s*-\s+\*\*([A-Za-z][\w.\-]*\d[\w.\-]*)\*\*\s*(\[.*)$", l)
        if m:
            preds.append({"id": m.group(1), "ligne": no, "texte": tronquer(m.group(2))})
    if not preds and sect:
        paragraphe = [l for _, l in sect if l.strip()]
        if paragraphe:
            preds.append({"id": "(section entière)", "ligne": sect[0][0], "texte": tronquer(" ".join(paragraphe[:4]))})
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


def table_promis(racine: Path, jour: str, S: Sources, verdicts: list[dict], runs: list[dict]) -> list[dict]:
    T = "promis-livre-v1"
    cand = Fichier(racine, CHEMINS["candidature"], scelle=True)
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

    # (b) Candidature, section 6 « Progress to date » : chaque puce est une promesse de ce qui existe.
    s6 = cand.section(r"^6\. Progress to date")
    titre6 = next((l for _, l in cand.chercher(r"^## 6\. ")), "")
    periode6 = re.sub(r"^## 6\. Progress to date\s*", "", titre6).strip("() ")
    k = 0
    for no, l in s6:
        m = re.match(r"^- \*\*(.+?)\*\*\s*(.*)$", l)
        if m:
            k += 1
            lid = f"C6-{k}"
            texte = f"{m.group(1)} {m.group(2)}"
            tache = next((t for motif, t in REGLES_CANDIDATURE if re.search(motif, texte, re.I)), None)
            S.cellule(T, lid, "promesse", cand, [no])
            S.cellule(T, lid, "date_promise", cand, [no])
            piece, sha = piece_de_tache(tache, lid)
            lignes.append({"id": lid, "source": "candidature, section 6", "promesse": tronquer(texte, 260),
                           "date_promise": f"déclaré fait à la candidature ({periode6})", "etat": etat_de_tache(tache, lid),
                           "piece": piece, "sha256": sha, "glissement": glissement(tache, lid)})
        elif l.startswith("Gate G0"):
            lid = "C6-G0"
            S.cellule(T, lid, "promesse", cand, [no])
            S.cellule(T, lid, "date_promise", cand, [no])
            m2 = re.search(r"\(([^)]*\d{4})\)", l)
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
            lignes.append({"id": lid, "source": "candidature, section 6", "promesse": tronquer(l, 300),
                           "date_promise": m2.group(1) if m2 else "", "etat": etat_txt, "piece": "", "sha256": "",
                           "glissement": gl})

    # (c) Candidature, section 7 « Timeline » : une ligne par période.
    k = 0
    for no, l in cand.section(r"^7\. Timeline"):
        c = cellules_table(l)
        if len(c) >= 4 and re.match(r"^\d", c[0]):
            k += 1
            lid = f"C7-{k}"
            S.cellule(T, lid, "promesse", cand, [no])
            S.cellule(T, lid, "date_promise", cand, [no])
            etat_txt = etat_periode(c[1], jour)
            if etat_txt:
                S.cellule(T, lid, "etat", cand, [no], "période de la ligne comparée au jour du script")
            lignes.append({"id": lid, "source": "candidature, section 7", "promesse": tronquer(f"{c[2]} → {c[3]}", 260),
                           "date_promise": f"mois {c[0]} ({c[1]})", "etat": etat_txt, "piece": "", "sha256": "", "glissement": ""})

    # (d) Candidature, section 8 « Deliverables and success criteria ».
    k = 0
    for no, l in cand.section(r"^8\. Deliverables"):
        m = re.match(r"^(?:- |\d+\. )(.*)$", l)
        if m:
            k += 1
            lid = f"C8-{k}"
            S.cellule(T, lid, "promesse", cand, [no])
            S.cellule(T, lid, "date_promise", cand, [no])
            lignes.append({"id": lid, "source": "candidature, section 8", "promesse": tronquer(m.group(1), 260),
                           "date_promise": "fin des 12 mois (section 7)", "etat": "", "piece": "", "sha256": "",
                           "glissement": ""})
    return lignes


# --------------------------------------------------------------------------- table 2 : calibration
def classer(texte: str) -> str:
    for mot, issue in ISSUES:
        if re.search(mot, texte, re.I):
            return issue
    return ""


def issue_dans(lignes: list[tuple[int, str]], identifiant: str) -> tuple[str, list[int]]:
    """Issue d'une prédiction lue dans les lignes qui la citent ; contradictions signalées, jamais tranchées.

    Priorité : lignes de table dont la première cellule est l'identifiant (table de lecture du verdict, issue lue dans
    les autres cellules) ; sinon les lignes de prose qui le citent (les autres lignes de table, souvent recopiées du
    préenregistrement avec leur colonne « réfutation », sont ignorées)."""
    motif = motif_id(identifiant)
    trouvees: dict[str, list[int]] = {}
    tables = [(no, cellules_table(l)) for no, l in lignes if l.startswith("|")]
    for no, c in tables:
        if c and motif.fullmatch(c[0].strip("*").split(",")[0].strip()):
            issue = classer(" | ".join(c[1:]))
            if issue:
                trouvees.setdefault(issue, []).append(no)
    if trouvees:
        return _resoudre(trouvees)
    for no, l in lignes:
        if l.startswith("|") or not motif.search(l):
            continue
        issue = classer(l)
        if issue:
            trouvees.setdefault(issue, []).append(no)
    return _resoudre(trouvees)


def _resoudre(trouvees: dict[str, list[int]]) -> tuple[str, list[int]]:
    if not trouvees:
        return "", []
    if len(trouvees) == 1:
        issue, nos = next(iter(trouvees.items()))
        return issue, nos
    return "contradictoire (" + " / ".join(f"{i} l. {','.join(map(str, n))}" for i, n in trouvees.items()) + ")", \
        [n for ns in trouvees.values() for n in ns]


def issue_pour_verdict(f: Fichier, identifiant: str) -> tuple[str, list[int]]:
    """Tête du verdict (40 premières lignes), puis section « Verdict », puis tout le texte : la première lecture
    non contradictoire l'emporte ; sinon la première contradiction est rapportée telle quelle."""
    candidats = [[(i + 1, l) for i, l in enumerate(f.lignes[:40])], f.section(r"Verdict"),
                 [(i + 1, l) for i, l in enumerate(f.lignes)]]
    premiere = ("", [])
    for lignes in candidats:
        issue, nos = issue_dans(lignes, identifiant)
        if issue and not issue.startswith("contradictoire"):
            return issue, nos
        if issue and not premiere[0]:
            premiere = (issue, nos)
    return premiere


def table_calibration(racine: Path, S: Sources, preregs: list[dict], verdicts: list[dict], runs: list[dict]) -> list[dict]:
    T = "calibration-v1"
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
                issue, nos = issue_pour_verdict(v["fichier"], p["id"])
                if issue:
                    S.cellule(T, lid, "issue", v["fichier"], nos, "mots-clés d'issue lus dans les lignes citées")
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
            lignes.append({"id": lid, "prereg": f"`{f.rel}`", "prereg_sha256": f.sha256, "prediction_id": p["id"],
                           "prediction": p["texte"], "seuil": seuil, "verdict": verdict_txt, "verdict_sha256": verdict_sha,
                           "issue": issue, "contre_lecture": cl_texte, "runs": ", ".join(run_ids)})
    return lignes


# --------------------------------------------------------------------------- table 3 : coût par résultat
def table_cout(racine: Path, S: Sources, verdicts: list[dict], runs: list[dict]) -> list[dict]:
    T = "cout-par-resultat-v1"
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


# --------------------------------------------------------------------------- rendu
def rendre_table(titre: str, entete: str, colonnes: list[tuple[str, str]], lignes: list[dict], jour: str) -> str:
    out = [f"# {titre}", "", entete, "", f"Jour du script (`date -u`) : {jour}. Version : `{VERSION}`. "
           "Toute cellule vide est une cellule sans source ; aucune valeur n'est estimée. "
           "Sources de chaque cellule : `sources-v1.json`.", "",
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
    sortie.mkdir(parents=True, exist_ok=True)
    fichiers = {
        "promis-livre-v1.md": rendre_table(
            "Promis → livré — v1", "Une ligne par critère de la porte G0 (programme v2) et par promesse de la candidature "
            "(sections 6, 7, 8 de `proposal-v1.md`). L'état et la cause du glissement viennent de `registres/etat.md` ; "
            "la pièce est le verdict scellé le plus récent de la tâche, sinon le manifeste du run décisif cité.",
            COLONNES_PROMIS, promis, jour),
        "calibration-v1.md": rendre_table(
            "Registre de calibration des prédictions préenregistrées — v1",
            "Une ligne par prédiction des préenregistrements scellés de `prereg/` (brouillons et gabarit exclus). "
            "L'issue est lue dans les lignes du verdict scellé qui citent la prédiction (mots-clés, lignes citées dans "
            "`sources-v1.json`) ; sans verdict scellé : ligne du registre des décisions, sinon « non encore lue ».",
            COLONNES_CALIBRATION, calib, jour),
        "cout-par-resultat-v1.md": rendre_table(
            "Coût réel par résultat — v1",
            "Une ligne par run décisif (manifeste `decisif` vrai) et par GO de type calcul. Le montant est la somme des "
            "montants des lignes du registre des dépenses qui citent le run, son instance (registre des arrêts) ou le GO, "
            "hors engagements ; une ligne à plusieurs montants n'est pas tranchée (cellule vide, montants listés). "
            "La dernière colonne cite les lignes du registre des arrêts qui nomment le run ou le GO (négatifs, R4).",
            COLONNES_COUT, cout, jour),
    }
    for nom, texte in fichiers.items():
        (sortie / nom).write_text(texte, encoding="utf-8")
    resume = {"version": VERSION, "jour": jour, "racine": str(racine),
              "comptes": {"promis-livre-v1": len(promis), "calibration-v1": len(calib), "cout-par-resultat-v1": len(cout),
                          "preregs_lus": len(preregs), "verdicts_lus": len(verdicts), "manifestes_lus": len(runs)},
              "fichiers_lus": dict(sorted(S.fichiers.items())), "cellules": S.tables, "signalements": S.signalements}
    (sortie / "sources-v1.json").write_text(json.dumps(resume, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
                                            encoding="utf-8")
    return resume


def _main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--racine", default=".")
    ap.add_argument("--sortie", default="livrables/registres-taif-v1")
    ap.add_argument("--jour", default=None, help="AAAA-MM-JJ ; défaut : `date -u +%%Y-%%m-%%d`")
    a = ap.parse_args(argv)
    jour = a.jour or jour_utc()
    try:
        resume = construire(Path(a.racine), Path(a.racine) / a.sortie if not Path(a.sortie).is_absolute() else Path(a.sortie), jour)
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        return 2
    print(json.dumps(resume["comptes"], ensure_ascii=False))
    for s in resume["signalements"]:
        print(f"SIGNALÉ : {s['quoi']} — {s['chemin']} l. {s['ligne']}")
    return 0


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
