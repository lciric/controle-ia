"""Lignes de registre de T0.7 (brouillon 14, section « Lignes de registre », CLT7B-02, CLT7B-03 ; règle du registre partagé :
brouillon 13, M-2, restreinte au brouillon 14, R-1924 (1)) et garde d'ouverture, v1.

Registre : **`registres/scellements-v1.md`** (créé à la première ligne, jamais réécrit : on y ajoute des lignes). Format exact,
celui de `scripts/controle_lecture_t06_v1.py` (`lire_registre`, branche `origin/prep/t06-candidat8-v1`, commit `1ae198b4`,
sha256 `ba2ba5cfe7484e7e30bb74e44420b46c9939dd5613bbb961b9725c3d46343c07`) : une ligne de table Markdown à quatre cellules,

    | CLÉ | AAAA-MM-JJTHH:MM:SSZ | chemin/relatif/depuis/la/racine | sha256 (64 caractères hexadécimaux) |

date en UTC au format strict (motif `DATE`), chemin relatif sans « .. », **empreinte du fichier entier cité, égale à son compagnon
`.sha256`** (`sceau_conforme`). Une ligne de GO cite un **extrait scellé** (`registres/go-extraits/<CLÉ>-v1.md`, la ligne du GO
recopiée à l'octet, avec compagnon), et le module vérifie que l'extrait est une ligne de `registres/go.md` (`extrait_est_une_ligne_de`).

`lire_registre_detail(registre, exigees, permises, refusees, marques_autres)` : mêmes motifs `DATE` et `SHA` et mêmes refus de forme
que `controle_lecture_t06_v1.lire_registre` (ligne exigée absente, en double, mal formée), essayée contre lui sur les deux clés
communes (`SCELLEMENT-T07`, `SCELLEMENT-P3BIS`) avec égalité des refus (`tests/test_t07_lecture_v1.py`) ; le script de T0.6 ignore
toute autre clé (l. 66-67), alors que T0.7 applique la **règle du registre partagé**, dans cet ordre, à chaque ligne du registre :
(0) clé dont la présence est refusée à l'étape lue (`REFUSEES_ETAPE_A` : `VERDICT-P3BIS`, garde d'ordre, brouillon 14 ;
`SCORES-T07`, `SONDES-T07`, étape déjà jouée) → refus ; (1) ligne à quatre cellules dont la deuxième est une date au format et
dont la première ne vérifie pas la forme de clé `[A-Z0-9]+(-[A-Z0-9]+)+` → refus ; toute autre ligne non conforme (titre, ligne
vide, texte) est ignorée (brouillon 14, m-06) ; (2) clé exigée ou permise → ses règles ; (3) clé portant la **marque d'une autre
tâche** de la liste fixée (`marques_autres_taches` de la configuration ; marque = segment entre tirets, en dernière position ou
entre deux tirets) → **ignorée et comptée**, sauf si son nom, marque retirée, égale `SCELLEMENT-JEUX-JD`, `-JC` ou `-JA` (liste
explicite) → refus ; (4) toute autre clé → refus. Les refus d'une ouverture sont **tous** relevés avant d'être rendus (une seule
`RefusRegistre`, motifs joints par « ; ») ; puis, dans `verifier_lignes` : date non **strictement antérieure** à l'instant
d'ouverture ; fichier cité absent, empreinte différente, compagnon absent ou différent. Chaque ouverture est journalisée dans
`<registre>.ouvertures.md` (`OUVERTURE-T07`), chaque refus aussi (`REFUS-T07`, écrit par `lecture_v1.ouvrir` après tous les
contrôles de la garde ; brouillon 14, m-01) ; le journal est partagé avec T0.6 (`OUVERTURE-SONDES-T06`).
"""
from __future__ import annotations

import hashlib
import re
from datetime import datetime, timezone
from pathlib import Path

from ..gardes import GardeArret

SHA = re.compile(r"[0-9a-f]{64}")
DATE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")
CLE = re.compile(r"[A-Z0-9]+(?:-[A-Z0-9]+)+")           # forme d'une clé de registre (SCELLEMENT-T07, GO-ETAPE-A-T07, …)
MARQUE = re.compile(r"[A-Z0-9]+")
FORMAT_DATE = "%Y-%m-%dT%H:%M:%SZ"
REGISTRE_DEFAUT = "registres/scellements-v1.md"
DOSSIER_GO, FICHIER_GO = "registres/go-extraits", "registres/go.md"

SCELLEMENT_T07, SCELLEMENT_P3BIS, VERDICT_P3BIS = "SCELLEMENT-T07", "SCELLEMENT-P3BIS", "VERDICT-P3BIS"
RUN_CONFIRMATION_T06 = "RUN-CONFIRMATION-T06"
SCELLEMENT_JEUX_JD, SCELLEMENT_JEUX_JC, SCELLEMENT_JEUX_JA = ("SCELLEMENT-JEUX-T07-JD", "SCELLEMENT-JEUX-T07-JC",
                                                             "SCELLEMENT-JEUX-T07-JA")
SCELLEMENT_CONCEPTS_T07 = "SCELLEMENT-CONCEPTS-T07"
GO_ETAPE_A_T07, GO_LECTURE_T07 = "GO-ETAPE-A-T07", "GO-LECTURE-T07"
SCORES_T07, SONDES_T07 = "SCORES-T07", "SONDES-T07"
ISSUE_MOTS_ET_COUT_T06 = "ISSUE-MOTS-ET-COUT-T06"
AUDIT_FUITES_T07, CONSIGNE_AUDIT_FUITES_T07 = "AUDIT-FUITES-T07", "CONSIGNE-AUDIT-FUITES-T07"
CODE_T07 = "CODE-T07"
LIGNES_GO = (GO_ETAPE_A_T07, GO_LECTURE_T07)
CLES_CONNUES = (SCELLEMENT_T07, SCELLEMENT_P3BIS, VERDICT_P3BIS, RUN_CONFIRMATION_T06, SCELLEMENT_JEUX_JD, SCELLEMENT_JEUX_JC,
                SCELLEMENT_JEUX_JA, SCELLEMENT_CONCEPTS_T07, GO_ETAPE_A_T07, GO_LECTURE_T07, SCORES_T07, SONDES_T07,
                ISSUE_MOTS_ET_COUT_T06, AUDIT_FUITES_T07, CONSIGNE_AUDIT_FUITES_T07, CODE_T07)
MARQUE_T07 = "T07"
# Règle (3) restreinte (brouillon 14, R-1924 (1)) : forme sans marque des seules clés de T0.7 dont la présence fixe une lecture.
SANS_MARQUE_REFUSEES = ("SCELLEMENT-JEUX-JD", "SCELLEMENT-JEUX-JC", "SCELLEMENT-JEUX-JA")

# Clés par étape (brouillon 14, « Clés par étape »). Étape A : `GO-ETAPE-A-T07` (étape annexe) ou `GO-LECTURE-T07` (variante B) —
# l'une des deux est exigée, vérifié par `lecture_v1.ouvrir` ; `CODE-T07` exigée seulement si DS-3 bis est accordée (configuration).
# Brouillon 21, option (c) des phrases des concepts (R-2158 ; « Accord au code », point 20 (i)) : `SCELLEMENT-CONCEPTS-T07` passe
# des exigées aux permises ; lue seulement si elle précède strictement l'instant de fermeture (`lecture_v2.lire_jeux_et_phrases`).
EXIGEES_ETAPE_A = (RUN_CONFIRMATION_T06,)
PERMISES_ETAPE_A = (SCELLEMENT_JEUX_JD, SCELLEMENT_JEUX_JC, SCELLEMENT_JEUX_JA, SCELLEMENT_CONCEPTS_T07, GO_ETAPE_A_T07, GO_LECTURE_T07,
                    CODE_T07, SCELLEMENT_T07, AUDIT_FUITES_T07, CONSIGNE_AUDIT_FUITES_T07, SCELLEMENT_P3BIS, ISSUE_MOTS_ET_COUT_T06)
# Présence refusée à l'ouverture de l'étape A (brouillon 14, R-1924 (3) : `VERDICT_P3BIS` retirée des permises ; « Clés par
# étape » : `SCORES-T07` ou `SONDES-T07` présente → étape déjà jouée).
REFUSEES_ETAPE_A = {
    VERDICT_P3BIS: "garde d'ordre : VERDICT-P3BIS déjà inscrite à l'ouverture de l'étape A (SCORES-T07 et SONDES-T07 doivent lui "
                   "être strictement antérieures) : refus ; nœud de Lazar, pas une attente (brouillon 14, R-1924 (3))",
    SCORES_T07: "SCORES-T07 présente à l'ouverture de l'étape A : étape A déjà jouée",
    SONDES_T07: "SONDES-T07 présente à l'ouverture de l'étape A : étape A déjà jouée",
}
# Étape B (brouillon 13, B-1 (b) ; brouillons 12 et 13 pour l'audit des fuites) : toutes exigées ; absente → refus, code 2.
EXIGEES_ETAPE_B = (RUN_CONFIRMATION_T06, SCORES_T07, SONDES_T07, AUDIT_FUITES_T07, CONSIGNE_AUDIT_FUITES_T07, SCELLEMENT_P3BIS,
                   VERDICT_P3BIS, ISSUE_MOTS_ET_COUT_T06)
PERMISES_ETAPE_B = (SCELLEMENT_T07, SCELLEMENT_JEUX_JD, SCELLEMENT_JEUX_JC, SCELLEMENT_JEUX_JA, SCELLEMENT_CONCEPTS_T07,
                    GO_ETAPE_A_T07, GO_LECTURE_T07, CODE_T07)


class RefusRegistre(GardeArret):
    """Refus de la garde d'ouverture : aucune ouverture, motif écrit (code 2 en ligne de commande)."""


def sha256_de(chemin: Path) -> str:
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


def instant_utc(date: str) -> int:
    if not DATE.fullmatch(date):
        raise RefusRegistre(f"date {date!r} (AAAA-MM-JJTHH:MM:SSZ, UTC, attendue)")
    try:
        return int(datetime.strptime(date, FORMAT_DATE).replace(tzinfo=timezone.utc).timestamp())
    except ValueError:
        raise RefusRegistre(f"date {date!r} impossible") from None


def date_utc(instant: int) -> str:
    return datetime.fromtimestamp(int(instant), timezone.utc).strftime(FORMAT_DATE)


def sceau_conforme(chemin: Path, attendu: str | None = None) -> str:
    """Empreinte du fichier, après vérification de son compagnon `.sha256` (première colonne) ; `attendu` : empreinte exigée.
    Recopie de `controle_lecture_t06_v1.sceau_conforme` (`ba2ba5cf…`), exception `RefusRegistre`."""
    chemin = Path(chemin)
    if not chemin.is_file():
        raise RefusRegistre(f"{chemin} absent")
    sha = sha256_de(chemin)
    comp = Path(str(chemin) + ".sha256")
    if not comp.is_file():
        raise RefusRegistre(f"{chemin} : compagnon .sha256 absent")
    lu = (comp.read_text(encoding="utf-8").split() or [""])[0]
    if lu != sha:
        raise RefusRegistre(f"{chemin} : compagnon .sha256 ({lu[:12]}…) ≠ empreinte du fichier ({sha[:12]}…)")
    if attendu is not None and sha != attendu:
        raise RefusRegistre(f"{chemin} : empreinte {sha[:12]}… ≠ celle du registre ({attendu[:12]}…)")
    return sha


def marques_de(cle: str) -> list[str]:
    """Segments entre tirets en dernière position ou entre deux tirets (tout segment sauf le premier) : `…-T07`, `…-T07-…`."""
    return cle.split("-")[1:]


def retirer_marque(cle: str, marque: str) -> str:
    """Ôte le segment de la marque (sa première occurrence hors du premier segment) et un tiret adjacent."""
    segments = cle.split("-")
    i = segments.index(marque, 1)
    return "-".join(segments[:i] + segments[i + 1:])


def classer_cle_inconnue(cle: str, marques_autres) -> tuple[str, str | None]:
    """Règles (3) et (4) du registre partagé pour une clé de bonne forme, ni exigée ni permise : (« ignoree », None) ou
    (« refus », motif). Une clé qui porte aussi la marque `T07` est une clé de T0.7 inconnue (refus ; interprétation déclarée)."""
    marques = marques_de(cle)
    autres = [m for m in marques if m in tuple(marques_autres)]
    if autres and MARQUE_T07 not in marques:
        sans = retirer_marque(cle, autres[0])
        if sans in SANS_MARQUE_REFUSEES:
            return "refus", (f"registre : ligne {cle} : marque {autres[0]} d'une autre tâche, mais le nom sans marque {sans} est celui "
                             "d'une clé de jeux de T0.7 (règle (3) restreinte, brouillon 14, R-1924 (1)) : refus")
        return "ignoree", None
    return "refus", f"registre : ligne {cle} ni exigée ni permise à cette étape"


def lire_registre_detail(registre: Path, cles_exigees, cles_permises=(), cles_refusees: dict | None = None,
                         marques_autres=()) -> tuple[dict, list]:
    """Lignes du registre, clé → (instant, date, chemin, sha), et liste des clés ignorées (autres tâches, règle (3)). Contrôles de
    forme de `controle_lecture_t06_v1.lire_registre` (`ba2ba5cf…`, mêmes textes de refus) ; une exigée absente refuse ; une
    permise absente n'est pas rendue ; règle du registre partagé (docstring du module). Tous les refus sont relevés, puis rendus
    ensemble (une `RefusRegistre`, motifs joints par « ; », qui porte en `partiel` les lignes lues sans faute)."""
    registre = Path(registre)
    exigees, permises = tuple(cles_exigees), tuple(cles_permises)
    refusees = dict(cles_refusees or {})
    communes = (set(exigees) & set(permises)) | (set(refusees) & (set(exigees) | set(permises)))
    if communes:
        raise RefusRegistre(f"clés à la fois exigées, permises ou refusées : {sorted(communes)}")
    if not registre.is_file():
        raise RefusRegistre(f"registre {registre} absent")
    trouvees: dict = {k: [] for k in exigees + permises}
    fautes, ignorees = [], []
    for ligne in registre.read_text(encoding="utf-8").splitlines():
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if not cellules or not cellules[0]:
            continue
        c0 = cellules[0]
        if c0 in trouvees:
            trouvees[c0].append(cellules)
            continue
        if c0 in refusees:                                                   # règle (0) : présence refusée à cette étape
            fautes.append(f"registre : {refusees[c0]}")
            continue
        if not (len(cellules) == 4 and DATE.fullmatch(cellules[1])):
            continue                                                         # ligne non conforme : ignorée (m-06)
        if not CLE.fullmatch(c0):                                            # règle (1)
            fautes.append(f"registre : ligne {c0!r} : la première cellule n'a pas la forme d'une clé ([A-Z0-9]+(-[A-Z0-9]+)+) : "
                          "ligne non attribuable")
            continue
        decision, motif = classer_cle_inconnue(c0, marques_autres)          # règles (3) et (4)
        if decision == "ignoree":
            ignorees.append(c0)
        else:
            fautes.append(motif)
    sortie = {}
    for k, lignes in trouvees.items():
        if len(lignes) == 0 and k in permises:
            continue
        if len(lignes) != 1:
            fautes.append(f"registre : {len(lignes)} ligne(s) {k}, exactement une attendue")
            continue
        c = lignes[0]
        if len(c) != 4:
            fautes.append(f"registre : ligne {k} mal formée ({len(c)} colonnes, 4 attendues)")
            continue
        _, date, chemin, sha = c
        if not DATE.fullmatch(date):
            fautes.append(f"registre : ligne {k} : date {date!r} (AAAA-MM-JJTHH:MM:SSZ, UTC, attendue)")
            continue
        if not SHA.fullmatch(sha):
            fautes.append(f"registre : ligne {k} : empreinte {sha!r} (64 caractères hexadécimaux attendus)")
            continue
        if not chemin or chemin.startswith("/") or ".." in Path(chemin).parts:
            fautes.append(f"registre : ligne {k} : chemin {chemin!r} (relatif à la racine, sans « .. » attendu)")
            continue
        try:
            instant = int(datetime.strptime(date, FORMAT_DATE).replace(tzinfo=timezone.utc).timestamp())
        except ValueError:
            fautes.append(f"registre : ligne {k} : date {date!r} impossible")
            continue
        sortie[k] = (instant, date, chemin, sha)
    if fautes:
        e = RefusRegistre(" ; ".join(fautes))
        e.partiel = (sortie, ignorees)              # lignes lues sans faute : la garde poursuit ses autres contrôles
        raise e
    return sortie, ignorees


def lire_registre_t07(registre: Path, cles_exigees, cles_permises=(), cles_refusees: dict | None = None, marques_autres=()) -> dict:
    """`lire_registre_detail` sans la liste des clés ignorées (forme comparée à `controle_lecture_t06_v1.lire_registre`)."""
    return lire_registre_detail(registre, cles_exigees, cles_permises, cles_refusees, marques_autres)[0]


def extrait_est_une_ligne_de(extrait: Path, fichier: Path) -> str:
    """L'extrait scellé (une seule ligne non vide, recopiée à l'octet) est une ligne du fichier (texte UTF-8 exact) ; rend la ligne."""
    extrait, fichier = Path(extrait), Path(fichier)
    lignes = [l for l in extrait.read_text(encoding="utf-8").split("\n") if l.strip()]
    if len(lignes) != 1:
        raise RefusRegistre(f"{extrait} : une seule ligne non vide attendue, {len(lignes)} trouvée(s)")
    if not fichier.is_file():
        raise RefusRegistre(f"{fichier} absent")
    if lignes[0] not in fichier.read_text(encoding="utf-8").split("\n"):
        raise RefusRegistre(f"{extrait} : l'extrait n'est pas une ligne de {fichier} (texte UTF-8 exact)")
    return lignes[0]


def verifier_lignes(lignes: dict, racine: Path, instant: int) -> dict:
    """Pour chaque ligne lue : antériorité stricte à `instant` et sceau du fichier cité ; pour une ligne de GO, l'extrait scellé
    doit en plus être une ligne de `registres/go.md`. Rend clé → {date, chemin, sha256, instant, …} ; tous les refus sont relevés
    avant d'être rendus."""
    racine = Path(racine)
    sortie, fautes = {}, []
    for k, (t, date, chemin, sha) in lignes.items():
        try:
            if not t < int(instant):
                raise RefusRegistre(f"registre : ligne {k} datée {date}, pas strictement antérieure à l'ouverture ({date_utc(instant)})")
            sceau_conforme(racine / chemin, sha)
            entree = {"date": date, "instant": t, "chemin": chemin, "sha256": sha, "verifie": "fichier et compagnon .sha256"}
            if k in LIGNES_GO:
                entree["ligne_go"] = extrait_est_une_ligne_de(racine / chemin, racine / FICHIER_GO)
                entree["verifie"] += f" ; extrait égal à une ligne de {FICHIER_GO}"
            sortie[k] = entree
        except RefusRegistre as e:
            fautes.append(str(e))
    if fautes:
        e = RefusRegistre(" ; ".join(fautes))
        e.partiel = sortie
        raise e
    return sortie


def exiger_anteriorite(lignes: dict, avant: tuple, apres: str) -> None:
    """Chaque clé de `avant` strictement antérieure à `apres` (CLT7B-03 : `SCORES-T07`, `SONDES-T07` < `VERDICT-P3BIS` ; brouillon 13,
    M-1 : `CONSIGNE-AUDIT-FUITES-T07` < `AUDIT-FUITES-T07`). **Inconditionnelle** (brouillon 14, R-1924 (3)) : `apres` absente refuse."""
    if apres not in lignes:
        raise RefusRegistre(f"registre : ligne {apres} absente : antériorité de {', '.join(avant)} non vérifiable")
    for k in avant:
        if k not in lignes:
            raise RefusRegistre(f"registre : ligne {k} absente, exigée avant {apres}")
        if not lignes[k]["instant"] < lignes[apres]["instant"]:
            raise RefusRegistre(f"registre : ligne {k} ({lignes[k]['date']}) pas strictement antérieure à {apres} ({lignes[apres]['date']})")


def garde_ouverture(registre: Path, racine: Path, exigees, permises, instant: int, refusees: dict | None = None,
                    marques_autres=()) -> dict:
    lignes, ignorees = lire_registre_detail(registre, exigees, permises, refusees, marques_autres)
    verifiees = verifier_lignes(lignes, racine, instant)
    return {"registre": str(registre), "registre_sha256": sha256_de(registre), "instant": date_utc(instant),
            "exigees": list(exigees), "permises_presentes": [k for k in permises if k in verifiees],
            "permises_absentes": [k for k in permises if k not in verifiees], "lignes": verifiees,
            "cles_ignorees": {"nombre": len(ignorees), "noms": list(ignorees), "marques_autres_taches": list(marques_autres)}}


def _journal(registre: Path) -> Path:
    return Path(str(registre) + ".ouvertures.md")


def _empreinte_registre(registre: Path) -> str:
    return sha256_de(registre) if Path(registre).is_file() else "absent"


def journaliser_ouverture(registre: Path, instant: int, quoi: str, empreinte_objet: str) -> Path:
    journal = _journal(registre)
    with open(journal, "a", encoding="utf-8") as f:
        f.write(f"| OUVERTURE-T07 | {date_utc(instant)} | {quoi} | {empreinte_objet} | registre {_empreinte_registre(registre)} |\n")
    return journal


def journaliser_refus(registre: Path, instant: int, quoi: str, motif: str) -> Path | None:
    """Ligne `| REFUS-T07 | <date UTC> | etape-A/<run> ou etape-B/<run> | clés ou fichiers manquants ou fautifs : motif | registre
    <sha256> |` (brouillon 14, m-01) ; le motif est mis sur une ligne, sans barre verticale. Rien n'est écrit si le dossier du
    registre n'existe pas (le motif imprimé le dit)."""
    journal = _journal(registre)
    if not journal.parent.is_dir():
        return None
    propre = " ".join(str(motif).replace("|", "¦").split())
    with open(journal, "a", encoding="utf-8") as f:
        f.write(f"| REFUS-T07 | {date_utc(instant)} | {quoi} | clés ou fichiers manquants ou fautifs : {propre} | "
                f"registre {_empreinte_registre(registre)} |\n")
    return journal


def ecrire_ligne(cle: str, date: str, chemin: str, sha: str) -> str:
    """Une ligne au format exact."""
    if not CLE.fullmatch(cle) or not DATE.fullmatch(date) or not SHA.fullmatch(sha):
        raise RefusRegistre(f"ligne {cle} : clé, date ou empreinte hors format")
    return f"| {cle} | {date} | {chemin} | {sha} |"


def cle_presente(registre: Path, cle: str) -> bool:
    """Une ligne du registre a-t-elle `cle` pour première cellule ?"""
    registre = Path(registre)
    if not registre.is_file():
        return False
    for l in registre.read_text(encoding="utf-8").splitlines():
        cellules = [c.strip() for c in l.strip().strip("|").split("|")]
        if cellules and cellules[0] == cle:
            return True
    return False


def ajouter_ligne(registre: Path, cle: str, instant: int, chemin: str, sha: str) -> str:
    """Ajoute une ligne au registre (créé à la première ligne, jamais réécrit) ; refuse si la clé y est déjà."""
    registre = Path(registre)
    ligne = ecrire_ligne(cle, date_utc(instant), chemin, sha)
    if registre.is_file():
        if cle_presente(registre, cle):
            raise RefusRegistre(f"registre : ligne {cle} déjà présente, jamais réécrite")
    else:
        registre.parent.mkdir(parents=True, exist_ok=True)
        registre.write_text("# Registre des scellements (T0.6, T0.7, P3-bis) — lignes ajoutées, jamais réécrites\n\n", encoding="utf-8")
    with open(registre, "a", encoding="utf-8") as f:
        f.write(ligne + "\n")
    return ligne


__all__ = ["RefusRegistre", "lire_registre_t07", "lire_registre_detail", "verifier_lignes", "garde_ouverture",
           "journaliser_ouverture", "journaliser_refus", "sceau_conforme", "sha256_de", "extrait_est_une_ligne_de",
           "exiger_anteriorite", "ecrire_ligne", "ajouter_ligne", "cle_presente", "instant_utc", "date_utc", "marques_de",
           "retirer_marque", "classer_cle_inconnue", "EXIGEES_ETAPE_A", "PERMISES_ETAPE_A", "REFUSEES_ETAPE_A", "EXIGEES_ETAPE_B",
           "PERMISES_ETAPE_B", "REGISTRE_DEFAUT", "CLES_CONNUES", "SANS_MARQUE_REFUSEES", "MARQUE_T07"]
