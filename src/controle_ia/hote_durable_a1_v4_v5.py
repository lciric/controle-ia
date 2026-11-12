#!/usr/bin/env python3
"""Hôte durable de la course **A1-v4** (attaque de Goodhart contre le nul v9), **lanceur durable version 5**.

Version 5 (R12 : les lanceurs v1 à v4 d'A1-v3 restent inchangés ; fichiers neufs) : dérivée du lanceur durable v4
(`src/controle_ia/hote_durable_a1_v3_v4.py`, `8101d33b…`), dont elle garde la machine, la minuterie, le versement, les gardes des
sondes v2 à v10 et les corrections 1 à 8. Ce qui change, et rien d'autre :

- **Texte paramétré** : `orchestrator/prereg/preenregistrement-attaque-goodhart-v4-v<N>.md`, N passé par `--texte` (chemin local
  du texte dans le clone public, dont le nom donne N) ; son empreinte est passée par `--sha-texte` (lue au scellement, jamais en
  dur) et comparée au fichier et à son compagnon, chez le pilote puis sur la machine (`verifier_texte`). Le texte doit : n'avoir
  plus aucun marqueur `<<…>>` ; porter un bloc `plan-gele` dont `mondes` égale la ligne `mondes_texte` de la configuration des
  mondes, `go` = GO-2026-11-02-22, `plafond_usd` = 200, `fournisseurs` = argon, `mode` = course ; porter un bloc
  `empreintes-du-code` qui contient chaque fichier gelé public de la configuration avec la même empreinte.
- **Ligne de GO des appels** : GO-2026-11-02-22 à **exactement 200 USD** (constante `GO_COURSE`, `verifier_go_exact`).
- **Ligne de GO de la machine** : passée par la variable `GO_ID_MACHINE` (égale à `GO_ID`, convention de la garde de calcul),
  **aucun identifiant en dur** ; vérifiée contre `registres/go.md` de `main` par la garde de `main` (type calcul, Lazar, non échue,
  non révoquée), **plafond lu sur la ligne** et **périmètre lu** (mots « machine » et « A1-v4 » exigés : une ligne de course ou la
  ligne machine d'A1-v3 est refusée) ; même règle que la chaîne T0.6 v13 (`scripts/lancer_t06_v13.sh`, `plafond_ligne_go`).
- **Garde de dépense de la machine recomputée deux fois** : chez le pilote (vérification, puis à la création, sur l'offre
  retenue) et sur la machine (depuis `PRIX_H_USD`, contre le plafond relu sur la ligne de `main`).
- **Étiquette neuve** `a1-v4-v9` ; branches de données, de refus, d'interruption et de signe de vie neuves.
- **Mondes par configuration** : un fichier JSON (`configuration-mondes-variante-<i|ii>-v1.json`) et son compagnon `.sha256`,
  lus par le pilote (chemin local) et par la machine (`git show COMMIT_PRIVE:<chemin>`) ; variante (i) W1 et W2, variante (ii)
  W2 et W2 gradué ; la configuration porte aussi la **liste recalculée des fichiers gelés publics** (code d'attaque v4, nul v9,
  juge banc v9, lanceur v4, mondes) avec leurs empreintes, vérifiées sur le clone public et dans le bloc du texte, le commit du
  code gelé, le lanceur gelé et le dossier de sortie. Toute variante inconnue, tout compagnon absent ou faux : arrêt explicite.
- **Espèce Argon seule** : la clé vient de la variable **`GEMINI_API_KEY_2`, par son nom**, chez le pilote seulement, et voyage
  jusqu'à la machine sous le seul nom `CLE_ARGON` ; toute autre variable de clé de modèle est refusée (pilote et machine) ; aucune
  valeur de clé n'est écrite nulle part (journal masqué, sorties de `vastai` catégorisées, jamais recopiées).
- **Surveillance et destruction par identifiant d'instance** (R10), comme la v4 ; `controler` et `facturation` contrôlent
  l'étiquette `a1-v4-v9`.

Mode jouet des essais : aucune location, aucun appel de modèle, aucun réseau (dépôts locaux, Vast simulé, `vastai` factice).
"""
from __future__ import annotations

import argparse
import base64
import datetime as dt
import importlib.util
import io
import json
import os
import re
import shutil
import subprocess
import sys
import time
from contextlib import redirect_stderr
from pathlib import Path

try:  # paquet (essais sous `src/controle_ia`) ou fichier seul (machine, pilote : `python3 -I -B …/hote_durable_a1_v4_v5.py`)
    from . import hote_durable_a1_v3 as h
    from . import hote_durable_a1_v3_v4 as v4
    from . import sonde_hote_durable_a1_v3_v10 as s10
except ImportError:
    try:  # le paquet du dépôt, quand il est sur le chemin (essais joués depuis `docs/`) : mêmes objets que les essais v1 à v4
        from controle_ia import hote_durable_a1_v3 as h
        from controle_ia import hote_durable_a1_v3_v4 as v4
        from controle_ia import sonde_hote_durable_a1_v3_v10 as s10
    except ImportError:  # fichier seul : la v4 charge elle-même la v1 et la sonde v10 ; on reprend **ses** objets (une seule classe Refus)
        _ici = Path(__file__).resolve().parent
        _candidats = [_ici] + [p / "src" / "controle_ia" for p in _ici.parents]  # voisins, sinon `src/controle_ia` du dépôt
        _dossier = next((d for d in _candidats if (d / "hote_durable_a1_v3_v4.py").is_file()), None)
        if _dossier is None:
            raise ImportError("hote_durable_a1_v3_v4.py introuvable (voisin du module ou sous src/controle_ia du dépôt)")
        _spec = importlib.util.spec_from_file_location("hote_durable_a1_v3_v4", _dossier / "hote_durable_a1_v3_v4.py")
        v4 = importlib.util.module_from_spec(_spec)
        sys.modules["hote_durable_a1_v3_v4"] = v4
        _spec.loader.exec_module(v4)
        h, s10 = v4.h, v4.s10

VERSION = "hote-durable-a1-v4-v5"
GO_COURSE, MONTANT_GO_COURSE_USD = "GO-2026-11-02-22", 200.0  # appels à Argon : égalité exacte exigée sur chaque ligne
NOM_GO_MACHINE_ENV = "GO_ID_MACHINE"  # la ligne de GO de la machine, lue dans l'environnement du pilote ; jamais en dur
MOTS_PERIMETRE_MACHINE = ("machine", "a1-v4")  # le périmètre de la ligne machine doit porter ces mots (minuscules)
MOTIF_GO = re.compile(r"^GO-\d{4}-\d{2}-\d{2}-\d{2}$")
ETIQUETTE = "a1-v4-v9"
NOM_CLE_ARGON_PILOTE = "GEMINI_API_KEY_2"  # la seule source de la clé, par son nom, chez le pilote (R-1540)
NOMS_JETON_GITHUB = ("GH_TOKEN", "CONTROLE_IA_GITHUB_TOKEN_2")  # le premier présent l'emporte (chaîne T0.6 v13)
BRANCHE_DONNEES = "donnees/attaque-goodhart-v4-a1v4-v1"  # noms du brouillon 3 du texte A1-v4, section 8
BRANCHE_INTERROMPUE = "donnees/attaque-goodhart-v4-a1v4-interrompue-v1"
BRANCHE_REFUS = "donnees/attaque-goodhart-v4-a1v4-refus-v1"
BRANCHE_VIE = "donnees/attaque-goodhart-v4-a1v4-signe-de-vie-v1"
AMORCE = "scripts/amorce_hote_durable_a1_v4_v5.sh"
MODULE = "src/controle_ia/hote_durable_a1_v4_v5.py"
MODULES = v4.MODULES + ("hote_durable_a1_v4_v5.py",)
TRAVAIL = "a1-v4-reprise-v9-v1"  # dossier de travail sur la machine : /root/a1-v4-reprise-v9-v1 (brouillon 3, section 4)
LISTE_EMPREINTES = "EMPREINTES-sortie-a1-v4-v1.txt"
JOURNAL_HOTE = "journal-hote-a1-v4-v1.log"
DOSSIER_TEXTE = "orchestrator/prereg"
PREFIXE_TEXTE_DEFAUT = "preenregistrement-attaque-goodhart-v4-v"  # le lanceur gelé v4 exige `…-v4-v<N>.md` ; un code v5 pourrait exiger `-v5-v`
MOTIF_PREFIXE_TEXTE = re.compile(r"^preenregistrement-attaque-goodhart-v[1-9][0-9]*-v$")
MARQUEUR = re.compile(r"<<[A-Z0-9_]+>>")
DEBUT_PLAN, FIN_PLAN = "<!-- plan-gele : début -->", "<!-- plan-gele : fin -->"
DEBUT_EMPREINTES, FIN_EMPREINTES = "<!-- empreintes-du-code : début -->", "<!-- empreintes-du-code : fin -->"
VARIANTES_MONDES = {"i": ["W1", "W2"], "ii": ["W2", "W2g"]}  # (ii) : W2g = « W2 gradué » (note W2, brouillon 3) ; accord exigé
CLES_CONFIGURATION = {"version", "variante", "mondes", "mondes_texte", "etiquette", "go_course", "plafond_course_usd", "prefixe_texte",
                      "lanceur_gele", "dossier_sortie", "etape_depense", "commit_code_gele", "fichiers_geles_publics"}
CLES_CONFIGURATION_FACULTATIVES = {"pieces_privees", "note"}
SECRETS_PILOTE = (NOM_CLE_ARGON_PILOTE, "CLE_ARGON", "CONTROLE_IA_GITHUB_TOKEN_2") + s10.SECRETS_PILOTE
FICHIERS_DEMARRAGE = ("a1v4-minuterie.txt", "a1v4-minuterie.log", "a1v4-temps.txt", "amorce-a1v4-v5.log", "a1v4-memoire.txt")
DETRUIRE_MAINTENANT = "a1v4-detruire-maintenant"
PROTEGEES = v4.PROTEGEES
DUREE_MACHINE_S, DEMARRAGE_MAX_S, MARGE_MINUTERIE_S = v4.DUREE_MACHINE_S, v4.DEMARRAGE_MAX_S, v4.MARGE_MINUTERIE_S
VIE_APRES_ECHEANCE_S, ATTENTE_MINUTERIE_S, RESERVE_VERSEMENT_S = v4.VIE_APRES_ECHEANCE_S, v4.ATTENTE_MINUTERIE_S, v4.RESERVE_VERSEMENT_S
BORNE_SIGNE_DE_VIE_S, PREMIER_CONTROLE_S = v4.BORNE_SIGNE_DE_VIE_S, v4.PREMIER_CONTROLE_S
DELAI_GIT_S, DELAI_GIT_LOCAL_S = v4.DELAI_GIT_S, v4.DELAI_GIT_LOCAL_S
CODE_REFUS_AMORCE = v4.CODE_REFUS_AMORCE
cles_interdites = v4.cles_interdites  # CLE_ARGON permise, la seule (machine et corps)
cout_maximal_usd = v4.cout_maximal_usd
echeance_absolue = v4.echeance_absolue


def cles_interdites_pilote(environ: dict) -> list[str]:
    """Chez le pilote, la source de la clé d'Argon (`GEMINI_API_KEY_2`) est permise ; toute autre clé de modèle est refusée."""
    return [k for k in cles_interdites(environ) if k != NOM_CLE_ARGON_PILOTE]


def nom_du_jeton_github(environ: dict) -> str | None:
    return next((k for k in NOMS_JETON_GITHUB if environ.get(k)), None)


# --- GO : appels (constante, 200 USD exact) et machine (ligne lue, plafond et périmètre lus) --------------------------------


def verifier_go_course(chemin_registre: Path, chemin_garde: Path, go_id: str, aujourd_hui: dt.date) -> dict:
    """GO-2026-11-02-22 exigé, garde de `main`, plafond d'exactement 200 USD sur la ligne et sur chaque extension."""
    return v4.verifier_go_exact(chemin_registre, chemin_garde, go_id, GO_COURSE, MONTANT_GO_COURSE_USD, aujourd_hui)


def verifier_go_machine(chemin_registre: Path, chemin_garde: Path, go_id: str, aujourd_hui: dt.date) -> dict:
    """Ligne de GO de la machine, nommée par `GO_ID_MACHINE` : forme, garde de `main` (type calcul, Lazar, validité, révocation,
    extensions), ≠ GO des appels, **plafond lu sur la ligne** (une seule valeur sur la ligne et ses extensions), **périmètre lu**
    (`MOTS_PERIMETRE_MACHINE`). Rend le plafond en USD avec la ligne."""
    if not isinstance(go_id, str) or not MOTIF_GO.match(go_id):
        raise h.Refus(f"{NOM_GO_MACHINE_ENV} absent ou illisible ({go_id!r}) : GO-AAAA-MM-JJ-NN exigé")
    if go_id == GO_COURSE:
        raise h.Refus(f"{NOM_GO_MACHINE_ENV}={go_id} est la ligne des appels : la machine a sa propre ligne de GO")
    garde = h.charger_garde(chemin_garde, chemin_registre)
    tampon = io.StringIO()
    try:
        with redirect_stderr(tampon):
            garde.decider(f"GO_ID={go_id} vastai create instance 0", aujourd_hui)
    except SystemExit as e:
        if e.code not in (0, None):
            raise h.Refus(f"garde de main ({go_id}) : {tampon.getvalue().strip()}") from None
    lignes = h.lignes_du_go(chemin_registre, go_id)
    if not lignes:
        raise h.Refus(f"{go_id} absent du registre")
    plafonds = set()
    for cellules in lignes:
        m = h.MONTANT.match(cellules[4])
        if not m:
            raise h.Refus(f"{go_id} : plafond « {cellules[4]} » illisible (« N USD » exigé)")
        plafonds.add(float(m.group(1).replace(",", ".")))
    if len(plafonds) != 1:
        raise h.Refus(f"{go_id} : plafonds différents sur la ligne et ses extensions {sorted(plafonds)} : texte neuf exigé")
    plafond = plafonds.pop()
    if not plafond > 0:
        raise h.Refus(f"{go_id} : plafond {plafond:g} USD")
    perimetre = lignes[0][3].lower()
    absents = [m for m in MOTS_PERIMETRE_MACHINE if m not in perimetre]
    if absents:
        raise h.Refus(f"{go_id} : périmètre sans {absents} : cette ligne n'est pas celle de la machine d'A1-v4 (lu : "
                      f"« {lignes[0][3][:80]} »)")
    return {"go": go_id, "lignes": len(lignes), "plafond_usd": plafond, "registre_sha256": h.sha256_fichier(chemin_registre),
            "echeance": lignes[0][5], "accorde": lignes[0][1]}


def verifier_plafond(dph: float, plafond_usd: float, go_machine: str) -> float:
    """Garde de dépense de la machine : coût maximal (création + démarrage + 80 h + marge + vie + attente) ≤ plafond de la ligne."""
    if not isinstance(plafond_usd, (int, float)) or isinstance(plafond_usd, bool) or not plafond_usd > 0:
        raise h.Refus(f"plafond de la machine illisible ({plafond_usd!r})")
    c = cout_maximal_usd(dph)
    if c > plafond_usd:
        raise h.Refus(f"coût de la machine au plus {c:.4f} USD > plafond {plafond_usd:g} USD lu sur la ligne {go_machine}")
    return c


# --- configuration des mondes -------------------------------------------------------------------------------------------------


def lire_compagnon(chemin: Path) -> str:
    compagnon = Path(str(chemin) + ".sha256")
    if not compagnon.is_file():
        raise h.Refus(f"compagnon .sha256 absent : {compagnon.name}")
    mots = compagnon.read_text(encoding="utf-8").split()
    if not mots or not re.fullmatch(r"[0-9a-f]{64}", mots[0]):
        raise h.Refus(f"compagnon {compagnon.name} illisible")
    vu = h.sha256_fichier(chemin)
    if vu != mots[0]:
        raise h.Refus(f"{chemin.name} : empreinte {vu[:12]}… différente du compagnon {mots[0][:12]}…")
    return vu


def lire_configuration_mondes(chemin) -> dict:
    """Configuration JSON des mondes et du code gelé, avec compagnon égal ; variante connue et mondes accordés à la variante ;
    constantes de la course égales à celles du module ; fichiers gelés publics : chemin → empreinte (64 hexadécimaux)."""
    chemin = Path(chemin)
    if not chemin.is_file():
        raise h.Refus(f"configuration des mondes introuvable : {chemin}")
    sha = lire_compagnon(chemin)
    try:
        c = json.loads(chemin.read_text(encoding="utf-8"))
    except ValueError as e:
        raise h.Refus(f"configuration des mondes illisible (JSON) : {e}") from None
    if not isinstance(c, dict) or not CLES_CONFIGURATION <= set(c) or not set(c) <= CLES_CONFIGURATION | CLES_CONFIGURATION_FACULTATIVES:
        raise h.Refus(f"configuration des mondes : clés attendues {sorted(CLES_CONFIGURATION)}, trouvées "
                      f"{sorted(c) if isinstance(c, dict) else type(c).__name__}")
    if c["variante"] not in VARIANTES_MONDES:
        raise h.Refus(f"variante de mondes inconnue {c['variante']!r} (connues : {sorted(VARIANTES_MONDES)})")
    if c["mondes"] != VARIANTES_MONDES[c["variante"]]:
        raise h.Refus(f"variante {c['variante']} : mondes {c['mondes']!r}, attendus {VARIANTES_MONDES[c['variante']]!r}")
    if not isinstance(c["mondes_texte"], str) or not c["mondes_texte"].strip():
        raise h.Refus("configuration des mondes : mondes_texte (valeur exacte de la ligne « mondes: » du bloc plan-gele) vide")
    if c["etiquette"] != ETIQUETTE:
        raise h.Refus(f"configuration : étiquette {c['etiquette']!r}, le lanceur v5 exige {ETIQUETTE!r}")
    if c["go_course"] != GO_COURSE or c["plafond_course_usd"] != MONTANT_GO_COURSE_USD:
        raise h.Refus(f"configuration : go_course {c['go_course']!r} à {c['plafond_course_usd']!r} USD, attendu {GO_COURSE} à "
                      f"{MONTANT_GO_COURSE_USD:g}")
    if not isinstance(c["commit_code_gele"], str) or not re.fullmatch(r"[0-9a-f]{40}", c["commit_code_gele"]):
        raise h.Refus("configuration : commit_code_gele = hash complet de 40 caractères")
    if not isinstance(c["prefixe_texte"], str) or not MOTIF_PREFIXE_TEXTE.match(c["prefixe_texte"]):
        raise h.Refus(f"configuration : prefixe_texte {c['prefixe_texte']!r} hors de {MOTIF_PREFIXE_TEXTE.pattern}")
    for k in ("lanceur_gele", "dossier_sortie", "etape_depense"):
        if not isinstance(c[k], str) or not c[k].strip() or any(ch.isspace() for ch in c[k]):
            raise h.Refus(f"configuration : {k} illisible")
    f = c["fichiers_geles_publics"]
    if not isinstance(f, dict) or not f or not all(isinstance(k, str) and k and re.fullmatch(r"[0-9a-f]{64}", str(v)) for k, v in f.items()):
        raise h.Refus("configuration : fichiers_geles_publics = {chemin: empreinte sha256}, non vide")
    if c["lanceur_gele"] not in f:
        raise h.Refus(f"configuration : le lanceur gelé {c['lanceur_gele']} n'est pas dans fichiers_geles_publics")
    p = c.get("pieces_privees")
    if p is not None and (not isinstance(p, dict) or not all(re.fullmatch(r"[0-9a-f]{64}", str(v)) for v in p.values())):
        raise h.Refus("configuration : pieces_privees = {chemin: empreinte sha256}")
    return dict(c, sha256=sha, chemin=str(chemin))


def verifier_fichiers_geles(racine_publique: Path, conf: dict) -> int:
    """Chaque fichier gelé public de la configuration, présent sur le clone public à l'empreinte écrite ; sinon refus."""
    ecarts = []
    for relatif, attendu in sorted(conf["fichiers_geles_publics"].items()):
        p = racine_publique / "orchestrator" / relatif
        vu = h.sha256_fichier(p) if p.is_file() else "absent"
        if vu != attendu:
            ecarts.append(f"{relatif} : gelé {attendu[:12]}…, présent {vu[:12]}")
    if ecarts:
        raise h.Refus("fichier gelé modifié ou absent du clone public : " + " ; ".join(ecarts))
    return len(conf["fichiers_geles_publics"])


# --- texte préenregistré --------------------------------------------------------------------------------------------------------


def _bloc(texte: str, debut: str, fin: str, nom: str) -> str:
    i, j = texte.find(debut), texte.find(fin)
    if i < 0 or j < 0 or j < i or texte.count(debut) != 1 or texte.count(fin) != 1:
        raise h.Refus(f"texte : bloc {nom} absent ou en double")
    return texte[i + len(debut):j]


def version_du_texte(chemin, prefixe: str = PREFIXE_TEXTE_DEFAUT) -> int:
    """N de `orchestrator/prereg/<prefixe><N>.md` (préfixe de la configuration, `preenregistrement-attaque-goodhart-v4-v` par
    défaut) ; refus de tout autre nom (v3, brouillon, autre dossier)."""
    chemin = Path(chemin)
    if not MOTIF_PREFIXE_TEXTE.match(prefixe or ""):
        raise h.Refus(f"préfixe du nom du texte illisible ({prefixe!r})")
    m = re.match(rf"^{re.escape(prefixe)}([1-9][0-9]*)\.md$", chemin.name)
    if not m or chemin.parent.name != "prereg" or chemin.parent.parent.name != "orchestrator":
        raise h.Refus(f"nom du texte : {DOSSIER_TEXTE}/{prefixe}<N>.md exigé, reçu {'/'.join(chemin.parts[-3:])}")
    return int(m.group(1))


def nom_texte(version: int, prefixe: str = PREFIXE_TEXTE_DEFAUT) -> str:
    return f"{DOSSIER_TEXTE}/{prefixe}{int(version)}.md"


def verifier_texte(chemin, sha_attendu: str, conf: dict, go_machine: str | None = None) -> dict:
    """Le texte scellé, tel que le lanceur v5 l'attend : nom `<prefixe_texte><N>.md` sous `orchestrator/prereg` ; compagnon égal ;
    empreinte égale à `sha_attendu` (lue au scellement) ; aucun marqueur `<<…>>` ; bloc `plan-gele` (mode = course, mondes =
    `mondes_texte`, fournisseurs = argon, plafond_usd = 200, go = GO des appels ; `go_machine`, si la ligne existe, égal à la ligne
    vérifiée) ; bloc `empreintes-du-code` contenant chaque fichier gelé public de la configuration à la même empreinte. Rend version,
    empreinte, mondes, nombre de lignes du bloc."""
    chemin = Path(chemin)
    version = version_du_texte(chemin, conf["prefixe_texte"])
    if not chemin.is_file():
        raise h.Refus(f"texte introuvable : {chemin}")
    if not isinstance(sha_attendu, str) or not re.fullmatch(r"[0-9a-f]{64}", sha_attendu):
        raise h.Refus("empreinte attendue du texte : 64 caractères hexadécimaux (lue au scellement)")
    vu = lire_compagnon(chemin)
    if vu != sha_attendu:
        raise h.Refus(f"texte v4-v{version} : empreinte {vu[:12]}… différente de celle attendue {sha_attendu[:12]}… (non scellé, "
                      "ou autre version)")
    texte = chemin.read_text(encoding="utf-8")
    restants = sorted(set(MARQUEUR.findall(texte)))
    if restants:
        raise h.Refus(f"texte : marqueur(s) non rempli(s) {restants} : texte non scellable")
    lignes = {}
    for l in _bloc(texte, DEBUT_PLAN, FIN_PLAN, "plan-gele").splitlines():
        m = re.match(r"^\s*([a-z0-9_]+)\s*:\s*(.+?)\s*$", l)
        if m:
            if m.group(1) in lignes:
                raise h.Refus(f"plan-gele : clé {m.group(1)!r} en double")
            lignes[m.group(1)] = m.group(2)
    attendus = {"mode": "course", "mondes": conf["mondes_texte"], "fournisseurs": "argon", "go": GO_COURSE}
    for k, v in attendus.items():
        if lignes.get(k) != v:
            raise h.Refus(f"plan-gele : {k} = {lignes.get(k)!r}, le lanceur v5 et la configuration attendent {v!r}")
    try:
        plafond = float(lignes.get("plafond_usd", "").replace(",", "."))
    except ValueError:
        plafond = None
    if plafond is None or abs(plafond - MONTANT_GO_COURSE_USD) > 1e-9:
        raise h.Refus(f"plan-gele : plafond_usd = {lignes.get('plafond_usd')!r}, exactement {MONTANT_GO_COURSE_USD:g} exigé")
    if "go_machine" in lignes:
        if lignes["go_machine"] == GO_COURSE or not MOTIF_GO.match(lignes["go_machine"]):
            raise h.Refus(f"plan-gele : go_machine = {lignes['go_machine']!r} illisible ou égal à la ligne des appels")
        if go_machine is not None and lignes["go_machine"] != go_machine:
            raise h.Refus(f"plan-gele : go_machine = {lignes['go_machine']!r}, la ligne vérifiée ({NOM_GO_MACHINE_ENV}) est {go_machine!r}")
    gelees = dict((r, e) for e, r in re.findall(r"^([0-9a-f]{64})  (\S+)$", _bloc(texte, DEBUT_EMPREINTES, FIN_EMPREINTES,
                                                                                    "empreintes-du-code"), re.M))
    if not gelees:
        raise h.Refus("empreintes-du-code : bloc vide")
    ecarts = [f"{r} : texte {gelees.get(r, 'absent')[:12]}, configuration {e[:12]}" for r, e in
              sorted(conf["fichiers_geles_publics"].items()) if gelees.get(r) != e]
    if ecarts:
        raise h.Refus("fichiers gelés publics de la configuration absents du bloc du texte ou à une autre empreinte : "
                      + " ; ".join(ecarts))
    return {"version": version, "sha256": vu, "mondes": lignes["mondes"], "lignes_gelees": len(gelees), "plafond_usd": plafond,
            "go": lignes["go"], "go_machine": lignes.get("go_machine"), "nom": nom_texte(version, conf["prefixe_texte"])}


# --- script de démarrage : la minuterie d'abord, sans Python (celle de la v4, étiquette et noms de la v5) ----------------------

MINUTERIE = v4.MINUTERIE.replace("a1v3-", "a1v4-").replace('"a1-v3-troisieme-v1"', f'"{ETIQUETTE}"').replace(
    "pas a1-v3-troisieme-v1", f"pas {ETIQUETTE}")
assert "a1v3" not in MINUTERIE and "a1-v3" not in MINUTERIE and ETIQUETTE in MINUTERIE


def script_de_demarrage(commit_prive: str) -> str:
    """Processus principal du conteneur (séquence de la v4 : minuterie détachée, curl, clone partiel, amorce v5 sous `timeout`,
    destruction demandée si l'amorce refuse, vie puis attente de la minuterie) ; noms de la v5."""
    if not re.fullmatch(r"[0-9a-f]{40}", commit_prive):
        raise h.Refus("commit du dépôt privé : hash complet de 40 caractères exigé")
    m64 = base64.b64encode(MINUTERIE.encode()).decode("ascii")
    return f'''set -u
R="${{RACINE_A1V4:-/root}}"; case "$R" in /*) ;; *) R=/root;; esac
API="${{API_VAST:-{h.API_VAST}}}"; case "$API" in https://*) ;; *) API={h.API_VAST};; esac
D="${{A1V4_DUREE_S:-{DUREE_MACHINE_S}}}"; case "$D" in ''|*[!0-9]*) D={DUREE_MACHINE_S};; esac; [ "$D" -le {DUREE_MACHINE_S} ] || D={DUREE_MACHINE_S}
MARGE="${{A1V4_MARGE_S:-{MARGE_MINUTERIE_S}}}"; case "$MARGE" in ''|*[!0-9]*) MARGE={MARGE_MINUTERIE_S};; esac; [ "$MARGE" -le {MARGE_MINUTERIE_S} ] || MARGE={MARGE_MINUTERIE_S}
APRES="${{A1V4_VIE_APRES_S:-{VIE_APRES_ECHEANCE_S}}}"; case "$APRES" in ''|*[!0-9]*) APRES={VIE_APRES_ECHEANCE_S};; esac; [ "$APRES" -le {VIE_APRES_ECHEANCE_S} ] || APRES={VIE_APRES_ECHEANCE_S}
ABS="${{ECHEANCE_UTC_S:-}}"; case "$ABS" in ''|*[!0-9]*) ABS="";; esac
if [ -s "$R/a1v4-minuterie.txt" ]; then read T0 ECH < "$R/a1v4-minuterie.txt"
else T0=$(date +%s); ECH=$((T0 + D + MARGE)); if [ -n "$ABS" ] && [ "$ABS" -lt "$ECH" ]; then ECH=$ABS; fi
     echo "$T0 $ECH" > "$R/a1v4-minuterie.txt"; fi
FINVIE=$((ECH + APRES))
echo {m64} | base64 -d > "$R/a1v4-minuterie.sh"
setsid bash "$R/a1v4-minuterie.sh" "$ECH" "$R" "$API" "$FINVIE" < /dev/null >> "$R/a1v4-minuterie.log" 2>&1 &
PM=$!
reste() {{ r=$(( FINVIE - $(date +%s) )); [ "$r" -gt 1 ] && echo "$r" || echo 1; }}
borne() {{ r=$(reste); [ "$r" -lt "$1" ] && echo "$r" || echo "$1"; }}
command -v curl >/dev/null || timeout -k 5 "$(borne 120)" sh -c 'apt-get update -qq && apt-get install -y -qq curl git ca-certificates >/dev/null 2>&1'
echo "demarrage $(date -u +%FT%TZ) depart $T0 echeance $ECH absolue ${{ABS:-aucune}} curl $(command -v curl >/dev/null && echo oui || echo NON)" >> "$R/a1v4-temps.txt"
if [ ! -e "$R/{DETRUIRE_MAINTENANT}" ] && [ ! -d "$R/amorce-depot/.git" ]; then
  t=$(date +%s)
  (command -v git >/dev/null || timeout -k 5 "$(borne 120)" sh -c 'apt-get update -qq && apt-get install -y -qq git ca-certificates >/dev/null')
  A='!f() {{ echo username=x-access-token; echo "password=${{GH_TOKEN}}"; }}; f'
  git init -q "$R/amorce-depot" && git -C "$R/amorce-depot" remote add origin "$DEPOT_URL" &&
  git -C "$R/amorce-depot" sparse-checkout set scripts src/controle_ia &&
  timeout -k 5 "$(borne 600)" git -C "$R/amorce-depot" -c credential.helper="$A" fetch -q --filter=blob:none --depth 1 origin {commit_prive} &&
  timeout -k 5 "$(borne 600)" git -C "$R/amorce-depot" -c credential.helper="$A" checkout -q --detach FETCH_HEAD
  echo "clone $? en $(( $(date +%s) - t )) s" >> "$R/a1v4-temps.txt"
fi
if [ -e "$R/{DETRUIRE_MAINTENANT}" ]; then
  echo "reprise après un refus de l'amorce : rien n'est lancé" >> "$R/a1v4-temps.txt"; FINVIE=$(( $(date +%s) + APRES ))
elif [ -f "$R/amorce-depot/{AMORCE}" ]; then
  timeout -k 10 "$(reste)" bash "$R/amorce-depot/{AMORCE}" 2>&1 | tee -a "$R/amorce-a1v4-v5.log"; CODE=${{PIPESTATUS[0]}}
  echo "amorce finie $(date -u +%FT%TZ) code $CODE" >> "$R/a1v4-temps.txt"
  if [ "$CODE" = "{CODE_REFUS_AMORCE}" ]; then
    echo "amorce en refus : destruction demandée à la minuterie" >> "$R/a1v4-temps.txt"; : > "$R/{DETRUIRE_MAINTENANT}"; FINVIE=$(( $(date +%s) + APRES ))
  fi
else
  echo "amorce absente du clone : destruction demandée à la minuterie" >> "$R/a1v4-temps.txt"; : > "$R/{DETRUIRE_MAINTENANT}"; FINVIE=$(( $(date +%s) + APRES ))
fi
while [ "$(date +%s)" -lt "$FINVIE" ]; do sleep 5; done
[ -s "$R/a1v4-minuterie.pid" ] && PM=$(cat "$R/a1v4-minuterie.pid")
t=$(date +%s); while kill -0 "$PM" 2>/dev/null && [ $(( $(date +%s) - t )) -lt {ATTENTE_MINUTERIE_S} ]; do sleep 2; done
echo "fin du principal $(date -u +%FT%TZ)" >> "$R/a1v4-temps.txt"
'''


def corps(commit_prive: str, commit_public: str, sha_texte: str, nom_texte_relatif: str, commit_registre: str, go_machine: str,
          conf: dict, offre: dict, secrets: dict[str, str], echeance_utc_s: int) -> dict:
    """Corps de création : variables de la v4, plus `NOM_TEXTE`, `CHEMIN_CONFIGURATION_MONDES`, `SHA_CONFIGURATION_MONDES` ;
    `GO_ID` = GO des appels (constante), `GO_MACHINE` = ligne vérifiée chez le pilote ; la clé d'Argon sous le seul nom `CLE_ARGON`."""
    for nom, valeur, motif in (("commit_prive", commit_prive, r"[0-9a-f]{40}"), ("commit_public", commit_public, r"[0-9a-f]{40}"),
                               ("sha_texte", sha_texte, r"[0-9a-f]{64}"), ("commit_registre", commit_registre, r"[0-9a-f]{40}"),
                               ("go_machine", go_machine, MOTIF_GO.pattern.strip("^$"))):
        if not isinstance(valeur, str) or not re.fullmatch(motif, valeur):
            raise h.Refus(f"{nom} : forme exacte exigée ({motif})")
    if go_machine == GO_COURSE:
        raise h.Refus("go_machine égal au GO des appels : refus")
    version_du_texte(Path(nom_texte_relatif), conf.get("prefixe_texte", PREFIXE_TEXTE_DEFAUT))
    manquants = [k for k in ("CLE_ARGON", "GH_TOKEN") if not secrets.get(k)]
    if manquants:
        raise h.Refus(f"secrets absents : {', '.join(manquants)}")
    if not isinstance(echeance_utc_s, int) or isinstance(echeance_utc_s, bool) or echeance_utc_s <= 0:
        raise h.Refus("échéance absolue (M-B) : entier de secondes exigé")
    chemin_conf = conf.get("chemin_depot")
    if not chemin_conf or chemin_conf.startswith("/") or any(ch.isspace() for ch in chemin_conf):
        raise h.Refus("chemin de la configuration des mondes dans le dépôt privé (relatif, sans espace) exigé")
    env = {"COMMIT_PRIVE": commit_prive, "COMMIT_PUBLIC": commit_public, "SHA_TEXTE": sha_texte, "NOM_TEXTE": nom_texte_relatif,
           "COMMIT_REGISTRE": commit_registre, "GO_ID": GO_COURSE, "GO_MACHINE": go_machine,
           "CHEMIN_CONFIGURATION_MONDES": chemin_conf, "SHA_CONFIGURATION_MONDES": conf["sha256"],
           "PRIX_H_USD": f"{offre['dph_total']:.6f}", "DEPOT_URL": h.DEPOT_PRIVE, "ECHEANCE_UTC_S": str(echeance_utc_s),
           "CLE_ARGON": secrets["CLE_ARGON"], "GH_TOKEN": secrets["GH_TOKEN"]}
    if cles_interdites(env):
        raise h.Refus("clé de modèle autre que CLE_ARGON dans le corps")
    b64 = base64.b64encode(script_de_demarrage(commit_prive).encode("utf-8")).decode("ascii")
    return {"image": h.IMAGE, "disk": 30, "label": ETIQUETTE, "env": env,
            "script": f"echo {b64} | base64 -d > /root/demarrage-a1v4-v5.sh && bash /root/demarrage-a1v4-v5.sh"}


# --- côté pilote --------------------------------------------------------------------------------------------------------------


class ClientPiloteV5(v4.ClientPiloteV4):
    """Le client de la v4 (sonde v10 éprouvée en réel) ; la source de la clé d'Argon (`GEMINI_API_KEY_2`) est masquée aussi."""

    def __init__(self, environ: dict, outil: str = "vastai"):
        super().__init__(environ, outil)
        self.secrets = {k: environ.get(k, "") for k in SECRETS_PILOTE}


def _secrets_pilote(environ: dict) -> dict:
    return {k: environ.get(k, "") for k in SECRETS_PILOTE}


def chemin_dans_le_depot(chemin: Path, racine: Path | None) -> str:
    """Chemin de la configuration relatif à la racine du dépôt privé (pour `git show COMMIT_PRIVE:<chemin>` sur la machine)."""
    chemin = chemin.resolve()
    racine = racine.resolve() if racine else None
    if racine is None:  # la racine : le premier parent qui porte `registres/go.md` et `src/controle_ia`
        racine = next((p for p in chemin.parents if (p / "registres" / "go.md").is_file() and (p / "src" / "controle_ia").is_dir()), None)
    if racine is None:
        raise h.Refus(f"racine du dépôt privé introuvable au-dessus de {chemin}")
    try:
        return chemin.relative_to(racine).as_posix()
    except ValueError:
        raise h.Refus(f"configuration {chemin} hors du dépôt {racine}") from None


def louer(a, client=None, aujourd_hui=None, environ=None, maintenant=None) -> int:
    """Partie pilote : GO des appels (200 exact) et GO de la machine (`GO_ID_MACHINE`, plafond et périmètre lus), configuration des
    mondes, texte scellé et fichiers gelés publics, offre, garde de dépense (deux fois), création ; état et ligne pour
    `registres/etat.md`. Rend 0 (créée, ou vérification seule) ou 2 (refus). Aucune valeur de clé n'est écrite."""
    environ = dict(os.environ) if environ is None else environ
    jl = Path(a.journal_local)
    j = h.Journal(jl, _secrets_pilote(environ))
    ident_f, incertain_f, etat_f = (Path(str(jl) + x) for x in (".identifiant", ".creation-incertaine", ".etat.json"))
    try:
        if ident_f.exists() or incertain_f.exists():  # m3, m-1 : une seule location ; incertaine : inventaire d'abord
            raise h.Refus("une location de l'hôte durable v5 a déjà eu lieu ou est incertaine (R12) : inventaire d'abord")
        go_machine = environ.get(NOM_GO_MACHINE_ENV, "")
        if not MOTIF_GO.match(go_machine or ""):
            raise h.Refus(f"{NOM_GO_MACHINE_ENV} absent ou illisible dans l'environnement (GO-AAAA-MM-JJ-NN : la ligne de GO de la "
                          "machine) : rien créé")
        if environ.get("GO_ID") != go_machine:  # f7 : la garde de calcul lit GO_ID en tête de la ligne de location
            raise h.Refus(f"GO_ID={go_machine} exigé en tête de la ligne de location (égal à {NOM_GO_MACHINE_ENV}, f7)")
        if cles_interdites_pilote(environ):
            raise h.Refus(f"clé de modèle autre que {NOM_CLE_ARGON_PILOTE} dans l'environnement du pilote : "
                          f"{cles_interdites_pilote(environ)} : rien créé")
        if not environ.get(NOM_CLE_ARGON_PILOTE):
            raise h.Refus(f"clé d'Argon absente par son nom ({NOM_CLE_ARGON_PILOTE}) : rien créé")
        nom_jeton = nom_du_jeton_github(environ)
        if not nom_jeton:
            raise h.Refus(f"jeton GitHub absent ({' ou '.join(NOMS_JETON_GITHUB)}) : rien créé")
        aujourd_hui = aujourd_hui or dt.datetime.now(dt.timezone.utc).date()
        gm = verifier_go_machine(Path(a.registre_main), Path(a.garde_main), go_machine, aujourd_hui)
        gc = verifier_go_course(Path(a.registre_main), Path(a.garde_main), GO_COURSE, aujourd_hui)
        j.ecrire(f"{VERSION} : machine {gm['go']} (plafond lu {gm['plafond_usd']:g} USD, échéance {gm['echeance']}) et appels "
                 f"{gc['go']} ({gc['plafond_usd']:g} USD exact) acceptés par la garde de main ; registre {gc['registre_sha256']}")
        conf = lire_configuration_mondes(a.configuration_mondes)
        conf["chemin_depot"] = chemin_dans_le_depot(Path(a.configuration_mondes), Path(a.racine_privee) if getattr(a, "racine_privee", None) else None)
        j.ecrire(f"configuration des mondes : variante ({conf['variante']}) {conf['mondes']} ; {conf['chemin_depot']} "
                 f"{conf['sha256']} ; {len(conf['fichiers_geles_publics'])} fichiers gelés publics ; code gelé {conf['commit_code_gele']}")
        t = verifier_texte(a.texte, a.sha_texte, conf, go_machine)
        racine_publique = Path(a.texte).resolve().parents[2]
        n = verifier_fichiers_geles(racine_publique, conf)
        j.ecrire(f"texte {t['nom']} : empreinte {t['sha256']} = compagnon = scellement ; mondes « {t['mondes']} » ; aucun marqueur ; "
                 f"{t['lignes_gelees']} lignes gelées, {n} fichiers gelés publics égaux sur {racine_publique}")
        j.ecrire(f"code (correction 4) : COMMIT_PRIVE {a.commit_prive} ; empreintes {json.dumps(empreintes_du_code(), ensure_ascii=False)}")
        offres = json.loads(Path(a.offres).read_text())
        offres = offres.get("offers", offres) if isinstance(offres, dict) else offres
        o = s10.offre_la_moins_chere_sonde(offres, int(a.offre))  # v9 a : « gpu », une carte, cpu_ram ≥ 8 000 Mo, …
        secrets = {"CLE_ARGON": environ[NOM_CLE_ARGON_PILOTE], "GH_TOKEN": environ[nom_jeton]}
        cout1 = verifier_plafond(o["dph_total"], gm["plafond_usd"], go_machine)  # garde de dépense, premier calcul
        j.ecrire(f"garde de dépense (1/2) : offre {o['id']} à {o['dph_total']} USD/h, coût au plus {cout1:.4f} USD ≤ {gm['plafond_usd']:g}")
        if a.verifier_seulement:
            c = corps(a.commit_prive, a.commit_public, a.sha_texte, t["nom"], a.commit_registre, go_machine, conf, o, secrets,
                      echeance_absolue(maintenant or dt.datetime.now(dt.timezone.utc)))
            lg = s10.longueurs_de_creation(o["id"], c)
            cout2 = verifier_plafond(float(c["env"]["PRIX_H_USD"]), gm["plafond_usd"], go_machine)
            j.ecrire(f"garde de dépense (2/2, sur le corps) : {cout2:.4f} USD ≤ {gm['plafond_usd']:g} ; longueurs : --args {lg['args_c']}, "
                     f"--env {lg['env']}, commande {lg['commande']}")
            j.ecrire("vérification seulement : rien créé (variables : " + ", ".join(sorted(c["env"])) + ")")
            return 0
        client = client or ClientPiloteV5(environ)
        autres = []  # v8 b : sur « no_such_ask », au plus 4 autres offres conformes, par prix croissant
        for x in sorted((x for x in offres if isinstance(x, dict) and x.get("id") != o["id"]),
                        key=lambda x: (x.get("dph_total") if isinstance(x.get("dph_total"), (int, float)) else 1e9, str(x.get("id")))):
            try:
                autres.append(s10.verifier_offre_sonde([x], x.get("id")))
            except h.Refus:
                continue
        candidates = [o] + autres[:s10.ESSAIS_NO_SUCH_ASK - 1]
        ident = None
        for k, oc in enumerate(candidates, 1):
            oc = s10.verifier_offre_sonde(offres, oc["id"])
            cout = verifier_plafond(oc["dph_total"], gm["plafond_usd"], go_machine)  # garde de dépense, second calcul
            t_creation = maintenant or dt.datetime.now(dt.timezone.utc)
            echeance = echeance_absolue(t_creation)
            c = corps(a.commit_prive, a.commit_public, a.sha_texte, t["nom"], a.commit_registre, go_machine, conf, oc, secrets, echeance)
            lg = s10.longueurs_de_creation(oc["id"], c)
            j.ecrire(f"essai {k}/{len(candidates)} : offre {oc['id']} ({oc.get('gpu_name')}) à {oc['dph_total']} USD/h ; garde de "
                     f"dépense (2/2) : coût au plus {cout:.4f} USD ≤ {gm['plafond_usd']:g} ; longueurs : --args {lg['args_c']}, --env "
                     f"{lg['env']}, commande {lg['commande']}")
            try:
                ident = client.creer(oc["id"], c)
                j.ecrire(f"réponse de création : contrat {ident} (essai {k})")
                o = oc
                break
            except s10.RefusNoSuchAsk as e:
                j.ecrire(f"essai {k} refusé : {e}")
                if k == len(candidates):
                    raise s10.RefusNoSuchAsk(f"{k} essai(s), tous « no_such_ask » : refus final (Vast : rien créé)") from None
            except s10.RefusAvantAppel:
                raise
            except h.Refus as e:  # m-1 : réponse illisible, erreur sans success faux, délai : marqueur, arrêt
                incertain_f.write_text(f"{h.maintenant()} {str(e)[:120]}\n")
                raise
        t0 = t_creation
        fmt = "%Y-%m-%dT%H:%M:%SZ"
        etat = {"identifiant": ident, "etiquette": ETIQUETTE, "t0_utc": t0.strftime(fmt),
                "borne_signe_de_vie_utc": (t0 + dt.timedelta(seconds=BORNE_SIGNE_DE_VIE_S)).strftime(fmt),
                "echeance_finale_utc": dt.datetime.fromtimestamp(echeance, dt.timezone.utc).strftime(fmt),
                "controles_utc": [(t0 + dt.timedelta(seconds=PREMIER_CONTROLE_S)).strftime(fmt),
                                  (dt.datetime.fromtimestamp(echeance, dt.timezone.utc)
                                   + dt.timedelta(seconds=VIE_APRES_ECHEANCE_S + ATTENTE_MINUTERIE_S + 300)).strftime(fmt)],
                "prix_h_usd": o["dph_total"], "cout_maximal_usd": round(cout, 4), "plafond_machine_usd": gm["plafond_usd"],
                "go_machine": go_machine, "go_course": GO_COURSE, "texte": t["nom"], "sha_texte": t["sha256"],
                "variante_mondes": conf["variante"], "mondes": conf["mondes"], "version": VERSION}
        ident_f.write_text(f"{ident}\n")
        etat_f.write_text(json.dumps(etat, ensure_ascii=False, indent=1) + "\n")
        j.ecrire(f"machine créée : identifiant {ident} (offre {o['id']}, {o['dph_total']} USD/h), étiquette {ETIQUETTE} ; T0 "
                 f"{etat['t0_utc']} ; signe de vie attendu avant {etat['borne_signe_de_vie_utc']} ; échéance finale "
                 f"{etat['echeance_finale_utc']}")
        j.ecrire("LIGNE POUR registres/etat.md : " + ligne_etat(etat))
        return 0
    except (h.Refus, OSError, ValueError, KeyError) as e:
        j.ecrire(f"REFUS : {e}")
        return 2


def empreintes_du_code() -> dict:
    """Correction 4 : empreinte des modules (voisins de ce fichier, ou sous src/controle_ia) et de l'amorce, sinon « absent »."""
    ici = Path(__file__).resolve().parent
    e = {}
    for m in MODULES:
        p = ici / m if (ici / m).is_file() else next((d / "src" / "controle_ia" / m for d in ici.parents
                                                      if (d / "src" / "controle_ia" / m).is_file()), None)
        e[m] = h.sha256_fichier(p) if p else "absent"
    amorce = next((d / AMORCE for d in [ici] + list(ici.parents) if (d / AMORCE).is_file()), None)
    e[Path(AMORCE).name] = h.sha256_fichier(amorce) if amorce else "absent de ce dossier"
    return e


def ligne_etat(e: dict) -> str:
    return (f"- Hôte durable v5 d'A1-v4 ({e['go_machine']}, plafond {e['plafond_machine_usd']:g} USD ; appels {e['go_course']}) : instance "
            f"**{e['identifiant']}**, étiquette `{e['etiquette']}`, créée {e['t0_utc']}, échéance {e['echeance_finale_utc']} ; texte "
            f"`{e['texte']}` ({e['sha_texte'][:12]}…), mondes {e['mondes']} ; contrôles à {' et '.join(e['controles_utc'])} ; toute "
            f"session qui reprend lance `hote_durable_a1_v4_v5.py controler` (étiquette contrôlée ; destruction par l'identifiant, "
            "avec -y, seulement sans signe de vie à T0 + 30 min).")


def _journal_pilote(a, environ) -> h.Journal:
    return h.Journal(Path(a.journal_local), _secrets_pilote(environ))


def controler(a, client=None, signe_de_vie=None, maintenant=None, environ=None) -> int:
    """Comme la v4 (codes 0, 1, 2, 3, 5, 6, 7), étiquette `a1-v4-v9`, signe de vie sur la branche de la v5 ; destruction par
    l'identifiant seulement sans signe de vie à T0 + 30 min ; jamais après l'échéance finale."""
    environ = dict(os.environ) if environ is None else environ
    j = _journal_pilote(a, environ)
    try:
        e = json.loads(Path(a.etat).read_text())
        ident = int(e["identifiant"])
        if ident in PROTEGEES:
            raise h.Refus(f"instance {ident} protégée : jamais touchée")
        now = maintenant or dt.datetime.now(dt.timezone.utc)
        lire = lambda k: dt.datetime.strptime(e[k], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc)
        client = client or ClientPiloteV5(environ)
        listees = [i for i in client.instances() if i.get("id") == ident]
        if not listees:
            j.ecrire(f"contrôle : instance {ident} absente de l'inventaire (détruite) ; rien à faire")
            return 0
        lab = listees[0].get("label")
        if lab != ETIQUETTE:
            raise h.Refus(f"instance {ident} : étiquette {lab!r}, pas {ETIQUETTE} : aucun geste (f8)")
        etat_vast = listees[0].get("actual_status")
        if now >= lire("echeance_finale_utc") + dt.timedelta(seconds=VIE_APRES_ECHEANCE_S):
            j.ecrire(f"contrôle : instance {ident} ({etat_vast}) encore listée après l'échéance finale : AUCUN GESTE ; la session "
                     "décide (une machine arrêtée garde ses données) ; consigner")
            return 7
        vie = signe_de_vie() if signe_de_vie else s10.branche_existe(BRANCHE_VIE, environ)
        if now >= lire("borne_signe_de_vie_utc") and not vie:
            j.ecrire(f"contrôle : aucun signe de vie à T0 + 30 min (m2) : destruction de {ident} par son identifiant (-y)")
            client.detruire(ident)
            if [i for i in client.instances() if i.get("id") == ident]:
                j.ecrire(f"instance {ident} encore listée après la destruction : recommencer, puis consigner")
                return 3
            j.ecrire(f"instance {ident} détruite par le pilote, vérifiée par l'inventaire : consigner dans registres/arrets.md")
            return 1
        j.ecrire(f"contrôle : instance {ident} ({etat_vast}) ; signe de vie {'oui' if vie else 'non'} ; encore listée : "
                 f"RECONTRÔLER (au plus tard {e.get('controles_utc', ['?'])[-1]})")
        return 5
    except s10.RefusRecontroler as x:
        j.ecrire(f"RECONTRÔLER : {x}")
        return 6
    except subprocess.TimeoutExpired as x:
        j.ecrire(f"DÉLAI DÉPASSÉ : {x.cmd[0] if isinstance(x.cmd, (list, tuple)) else 'commande'} ; recontrôler")
        return 6
    except (h.Refus, OSError, ValueError, KeyError) as x:
        j.ecrire(f"REFUS : {x}")
        return 6 if ("délai dépassé" in str(x) or str(x).startswith("vastai ") or "inventaire illisible" in str(x)) else 2


def relever_facturation(a, client=None, environ=None) -> int:
    environ = dict(os.environ) if environ is None else environ
    j = _journal_pilote(a, environ)
    try:
        e = json.loads(Path(a.etat).read_text())
        ident = int(e["identifiant"])
        if ident in PROTEGEES:
            raise h.Refus(f"instance {ident} protégée : jamais touchée")
        client = client or ClientPiloteV5(environ)
        f = client.facturation(ident)
        if f.get("label") not in (None, ETIQUETTE):
            raise h.Refus(f"instance {ident} : étiquette {f.get('label')!r}, pas {ETIQUETTE} : aucun relevé écrit")
        champs = {k: f[k] for k in s10.CHAMPS_FACTURATION if k in f}
        j.ecrire(f"relevé de facturation de l'instance {ident} : {json.dumps(champs, ensure_ascii=False, sort_keys=True)}")
        return 0
    except subprocess.TimeoutExpired:
        j.ecrire("DÉLAI DÉPASSÉ : vastai ; recontrôler")
        return 6
    except (h.Refus, OSError, ValueError, KeyError) as x:
        j.ecrire(f"REFUS : {x}")
        return 6 if ("délai dépassé" in str(x) or "code" in str(x)) else 2


# --- côté machine ----------------------------------------------------------------------------------------------------------


class MachineV5(v4.MachineV4):
    """La séquence de la v4 ; ce qui change : les deux GO (appels : 200 exact ; machine : `GO_MACHINE` relu sur `main`, plafond et
    périmètre lus, garde de dépense recomputée), la configuration des mondes lue au commit privé, le texte v4-v<N> vérifié
    (`verifier_texte`) et les fichiers gelés publics vérifiés sur le clone, la commande du lanceur gelé v4, les noms de la v5."""

    def __init__(self, r: h.Reglages, environ: dict[str, str], python_configuration: str = v4.PYTHON_CONFIGURATION):
        h.Machine.__init__(self, r, environ)
        self.racine = r.travail.parent
        self.python_configuration = python_configuration
        self.conf = None
        t0 = None
        try:
            t0 = float((self.racine / "a1v4-minuterie.txt").read_text().split()[0])
        except (OSError, ValueError, IndexError):
            pass
        self.depart_conteneur = t0
        if t0 is not None:
            self.debut = time.monotonic() - max(0.0, time.time() - t0)

    def principal(self) -> int:
        journal = self.t / JOURNAL_HOTE
        if self.etat_fichier.exists():  # reprise du conteneur : jamais de relance (R12)
            self.j = h.Journal(journal, self.secrets)
            avant = self.etat_fichier.read_text().strip()
            self.j.ecrire(f"REPRISE du conteneur : état précédent « {avant} » ; rien n'est relancé")
            if avant == "verse":
                return self.se_detruire(True)
            self.nature_fin = "reprise_du_conteneur"
            return self.fin(BRANCHE_INTERROMPUE)
        self.t.mkdir(parents=True, exist_ok=False)
        self.j = h.Journal(journal, self.secrets)
        try:
            self.j.ecrire(f"{VERSION} ; machine {self.env.get('GO_MACHINE')} ; appels {self.env.get('GO_ID')} ; texte {self.env.get('NOM_TEXTE')} ; "
                          f"prix {self.prix_h} USD/h ; plafond de la garde {self.r.plafond_machine_usd} USD, {self.r.duree_max_s / 3600:g} h ; "
                          f"identifiant {self.env.get('CONTAINER_ID', '?')} ; départ du conteneur {self.depart_conteneur}")
            self.j.ecrire(f"code (correction 4) : COMMIT_PRIVE {self.env.get('COMMIT_PRIVE', '?')} ; empreintes "
                          f"{json.dumps(empreintes_du_code(), ensure_ascii=False)}")
            self.etat("demarrage")
            self.preparer()
            self.etat("course")
            self.garder()
        except h.Refus as e:
            self._ecrire_sans_echec(f"REFUS : {e}")
            self.nature_fin = "refus_avant_course" if self.course is None else "refus_pendant_la_course"
        except Exception as e:
            self._ecrire_sans_echec(f"EXCEPTION {type(e).__name__} : {self.j.masquer(str(e))[:500]}")
            self.nature_fin = "exception_de_l_hote"
        return self.fin(BRANCHE_DONNEES if self.course is not None else BRANCHE_REFUS)

    def cmd_course(self, verifier: bool) -> list[str]:
        """Lanceur gelé v4 (`demonstrations/attaque_goodhart_v4.py`), texte v4-v<N>, configuration gelée d'Argon, registre copié,
        GO des appels ; `--verifier-seulement` d'abord."""
        r, e = self.r, self.env
        conf_argon = r.racine_sources / h.NUIT / "configuration-mini-course-kimi-argon-v3.json"
        cmd = ["nice", "-n", "10", r.python_course, "-I", "-B", self.conf["lanceur_gele"], str(self.t / self.conf["dossier_sortie"]),
               "--preenregistrement", e["NOM_TEXTE"].removeprefix("orchestrator/"), "--configuration", str(conf_argon), "--moteur",
               "reel", "--confirmer-moteur-reel", "--registre-go", str(self.t / "registre-go.md"), "--go", e["GO_ID"]]
        return cmd + (["--verifier-seulement"] if verifier else [])

    def lire_configuration_au_commit(self) -> dict:
        """La configuration des mondes et son compagnon, lus au commit privé (`git show`, clone partiel), empreinte égale à
        `SHA_CONFIGURATION_MONDES`, puis `lire_configuration_mondes` sur la copie locale."""
        e = self.env
        chemin = e["CHEMIN_CONFIGURATION_MONDES"]
        if chemin.startswith("/") or ".." in chemin.split("/"):
            raise h.Refus(f"CHEMIN_CONFIGURATION_MONDES illisible ({chemin!r})")
        d = self.t / "configuration-mondes"
        d.mkdir(exist_ok=True)
        local = d / Path(chemin).name
        local.write_bytes(self._show(e["COMMIT_PRIVE"], chemin))
        Path(str(local) + ".sha256").write_bytes(self._show(e["COMMIT_PRIVE"], chemin + ".sha256"))
        conf = lire_configuration_mondes(local)
        if conf["sha256"] != e["SHA_CONFIGURATION_MONDES"]:
            raise h.Refus(f"configuration des mondes au commit {e['COMMIT_PRIVE'][:12]} : empreinte {conf['sha256'][:12]}…, le pilote "
                          f"a vérifié {e['SHA_CONFIGURATION_MONDES'][:12]}…")
        conf["chemin_depot"] = chemin
        return conf

    def preparer(self) -> None:
        r, e = self.r, self.env
        for k in ("CLE_ARGON", "GH_TOKEN", "COMMIT_PRIVE", "COMMIT_PUBLIC", "SHA_TEXTE", "NOM_TEXTE", "COMMIT_REGISTRE", "GO_ID",
                  "GO_MACHINE", "CHEMIN_CONFIGURATION_MONDES", "SHA_CONFIGURATION_MONDES", "PRIX_H_USD", "ECHEANCE_UTC_S"):
            if not e.get(k):
                raise h.Refus(f"variable {k} absente")
        if cles_interdites(e):
            raise h.Refus(f"clé de modèle autre que CLE_ARGON dans l'environnement de la machine : {cles_interdites(e)}")
        if e["GO_ID"] != GO_COURSE:
            raise h.Refus(f"GO_ID={e['GO_ID']} : la ligne des appels est {GO_COURSE} (aucune autre)")
        if not MOTIF_GO.match(e["GO_MACHINE"]) or e["GO_MACHINE"] == GO_COURSE:
            raise h.Refus(f"GO_MACHINE={e['GO_MACHINE']!r} illisible ou égal à la ligne des appels")
        if not (0 < self.prix_h <= h.PRIX_MAX_H_USD):
            raise h.Refus(f"prix horaire {self.prix_h} hors de ]0 ; {h.PRIX_MAX_H_USD}]")
        self.verifier_interpreteurs()  # C1, correction 7
        if not re.fullmatch(r"[0-9]{9,11}", e["ECHEANCE_UTC_S"]):
            raise h.Refus("ECHEANCE_UTC_S (échéance absolue du pilote, M-B) illisible")
        depart = self.depart_conteneur or time.time()
        reste = int(e["ECHEANCE_UTC_S"]) - RESERVE_VERSEMENT_S - depart
        if reste <= 60:
            raise h.Refus(f"échéance absolue trop proche ({reste:.0f} s utiles) : rien ne part")
        r.duree_max_s = float(min(r.duree_max_s, reste))
        self.j.ecrire(f"durée de la course bornée à {r.duree_max_s:.0f} s (80 h au plus, échéance absolue moins 1 h)")
        gh, cr = self.secrets["GH_TOKEN"], e["COMMIT_REGISTRE"]
        jour = r.aujourd_hui or dt.datetime.now(dt.timezone.utc).date()
        # 1. Branches lues en clone partiel (m5)
        h.git("fetch", "-q", "--filter=blob:none", "--depth", "1", "origin",
              *[f"+refs/heads/{b}:refs/remotes/origin/{b}" for b in ("main", h.REF_SOURCES, h.REF_CONFIGURATION)],
              cwd=r.clone_prive, gh_token=gh, delai=DELAI_GIT_S)
        h.git("fetch", "-q", "--filter=blob:none", "--depth", str(s10.PROFONDEUR_CANAL), "origin",
              f"+refs/heads/{h.SOURCE_REGISTRE}:refs/remotes/origin/{h.SOURCE_REGISTRE}", cwd=r.clone_prive, gh_token=gh,
              delai=DELAI_GIT_S)
        # 2. Les deux GO sur main, par la garde de main ; plafond de la machine relu sur la ligne, garde de dépense recomputée
        tete_main = h.git("rev-parse", "refs/remotes/origin/main", cwd=r.clone_prive, delai=DELAI_GIT_S).strip()
        reg_main, garde = self.t / "registre-go-main.md", self.t / "garde_calcul_main.py"
        reg_main.write_bytes(self._show(tete_main, "registres/go.md"))
        garde.write_bytes(self._show(tete_main, ".claude/hooks/garde_calcul.py"))
        g = verifier_go_course(reg_main, garde, e["GO_ID"], jour)
        gm = verifier_go_machine(reg_main, garde, e["GO_MACHINE"], jour)
        cout = verifier_plafond(self.prix_h, gm["plafond_usd"], e["GO_MACHINE"])
        self.j.ecrire(f"GO acceptés par la garde de main {tete_main} : appels {json.dumps(g, ensure_ascii=False)} ; machine "
                      f"{json.dumps(gm, ensure_ascii=False)} ; garde de dépense (machine) : coût au plus {cout:.4f} USD ≤ {gm['plafond_usd']:g}")
        self.j.ecrire("grep main : " + " ; ".join(self._grep(reg_main, e["GO_ID"]) + self._grep(reg_main, e["GO_MACHINE"])))
        # 3. Registre passé au lanceur : copie entière du canal au commit fixé, sans retouche, sans doublon
        if h.lancer(["git", "merge-base", "--is-ancestor", cr, f"refs/remotes/origin/{h.SOURCE_REGISTRE}"],
                    cwd=r.clone_prive, delai=DELAI_GIT_S).returncode != 0:
            raise h.Refus(f"commit du registre {cr} absent de la branche {h.SOURCE_REGISTRE} (ou au-delà de "
                          f"{s10.PROFONDEUR_CANAL} commits)")
        reg = self.t / "registre-go.md"
        reg.write_bytes(self._show(cr, "registres/go.md"))
        doubles = h.doublons_lecteur_du_lanceur(reg)
        if doubles:
            raise h.Refus(f"registre {cr} : identifiants en double {doubles} (le lanceur le refuserait)")
        verifier_go_course(reg, garde, e["GO_ID"], jour)
        self.sha_registre = h.sha256_fichier(reg)
        self.j.ecrire(f"registre-go.md : commit {cr} de {h.SOURCE_REGISTRE}, aucun doublon, sha256 {self.sha_registre} ; grep : "
                      + " ; ".join(self._grep(reg, e["GO_ID"])))
        # 4. Configuration des mondes au commit privé
        self.conf = conf = self.lire_configuration_au_commit()
        if conf.get("pieces_privees"):
            r.empreintes = dict(conf["pieces_privees"])
        r.commit_code_gele = conf["commit_code_gele"]
        version_du_texte(Path(e["NOM_TEXTE"]), conf["prefixe_texte"])
        self.j.ecrire(f"configuration des mondes : variante ({conf['variante']}) {conf['mondes']} ; {conf['chemin_depot']} {conf['sha256']} ; "
                      f"{len(conf['fichiers_geles_publics'])} fichiers gelés publics ; code gelé {conf['commit_code_gele']} ; lanceur "
                      f"{conf['lanceur_gele']} ; étape de dépense {conf['etape_depense']}")
        # 5. Signe de vie (m2, C2), puis pièces privées, puis dépôt public
        if not self.signe_de_vie():
            raise h.Refus("signe de vie non vérifié par ls-remote (C2) : la course ne part pas")
        self.extraire_sources()
        h.git("clone", "-q", r.depot_public, str(r.clone_public))
        h.git("checkout", "-q", "--detach", e["COMMIT_PUBLIC"], cwd=r.clone_public)
        if h.lancer(["git", "merge-base", "--is-ancestor", r.commit_code_gele, e["COMMIT_PUBLIC"]],
                    cwd=r.clone_public).returncode != 0:
            raise h.Refus(f"le commit {e['COMMIT_PUBLIC']} ne descend pas du code gelé {r.commit_code_gele}")
        t = verifier_texte(r.clone_public / e["NOM_TEXTE"], e["SHA_TEXTE"], conf, e["GO_MACHINE"])
        n = verifier_fichiers_geles(r.clone_public, conf)
        statut = h.git("status", "--porcelain", cwd=r.clone_public)
        if statut.strip():
            raise h.Refus("arbre du dépôt public modifié : " + statut[:200])
        self.j.ecrire(f"dépôt public {e['COMMIT_PUBLIC']} (descend de {r.commit_code_gele}) ; texte {t['nom']} {t['sha256']} = compagnon = "
                      f"SHA_TEXTE ; mondes « {t['mondes']} » ; {t['lignes_gelees']} lignes gelées ; {n} fichiers gelés publics égaux ; "
                      "git status --porcelain vide")
        if not h.port_libre(r.port):
            raise h.Refus(f"port {r.port} déjà pris : un autre relais vit (Argon seul)")
        self.lancer_relais()
        self.verifier_seulement()
        statut = h.git("status", "--porcelain", cwd=r.clone_public)  # correction 5
        self.j.ecrire("git status --porcelain juste avant la course : " + (repr(statut[:200]) if statut.strip() else "vide"))
        if statut.strip():
            raise h.Refus("arbre du dépôt public modifié avant la course (correction 5) : " + statut[:200])
        self.lancer_course()

    def signe_de_vie(self) -> bool:
        f = self.t / "signe-de-vie.json"
        f.write_text(json.dumps({"utc": h.maintenant(), "machine": self.env.get("CONTAINER_ID"),
                                 "depart_conteneur": self.depart_conteneur, "version": VERSION}) + "\n")
        try:
            gh, url = self.secrets["GH_TOKEN"], self._url()
            if h.git("ls-remote", url, f"refs/heads/{BRANCHE_VIE}", gh_token=gh, delai=DELAI_GIT_S).strip():
                raise h.Refus(f"branche {BRANCHE_VIE} déjà présente (R12)")
            v = self.racine / "versement-signe-de-vie-a1v4"
            if v.exists():
                raise h.Refus(f"copie {v} déjà présente (R12)")
            h.git("init", "-q", "-b", "signe-de-vie", str(v), delai=DELAI_GIT_S)
            (v / BRANCHE_VIE).mkdir(parents=True)
            shutil.copy2(f, v / BRANCHE_VIE / f.name)
            h.git("add", "-f", "-A", cwd=v, delai=DELAI_GIT_S)
            h.git("-c", "user.name=hote-durable-a1-v4", "-c", "user.email=hote@invalid", "commit", "-q", "-m",
                  "A1-v4 : signe de vie de l'hôte durable v5 (aucune donnée de la course)", cwd=v, delai=DELAI_GIT_S)
            c = self._pousser(v, BRANCHE_VIE, url)
            self.j.ecrire(f"signe de vie poussé : {BRANCHE_VIE} = {c}" if c else "signe de vie non vérifié par ls-remote")
            return bool(c)
        except Exception as x:
            self.j.ecrire(f"signe de vie non poussé : {type(x).__name__} : {self.j.masquer(str(x))[:200]}")
            return False

    def copier_journaux_du_demarrage(self) -> None:
        d = self.t / "demarrage"
        for nom in FICHIERS_DEMARRAGE:
            p = self.racine / nom
            if p.is_file():
                d.mkdir(exist_ok=True)
                shutil.copy2(p, d / nom)

    def lancer_relais(self) -> None:
        """Comme la v1 (relais Argon neuf, seul à tenir la clé, réglages relevés), journal au nom de la v5."""
        r = self.r
        commande = r.racine_sources / h.NUIT / "commande_argon_v56_nuit_v2.py"
        self.journal_relais = self.t / "relais-argon-journal-a1-v4.jsonl"
        self.cmd_relais = [r.python_relais, "-I", "-B", str(commande), "servir", "--port", str(r.port), "--plafond-usd",
                           str(h.PLAFOND_RELAIS_USD), "--max-appels", str(h.MAX_APPELS_RELAIS), "--journal", str(self.journal_relais)]
        self._demarrer_relais()
        fin = time.monotonic() + r.attente_relais_s
        etat = None
        while time.monotonic() < fin:
            etat = h.etat_relais(r.port)
            if etat is not None:
                break
            if self.relais.poll() is not None:
                raise h.Refus(f"relais sorti en code {self.relais.returncode} au démarrage")
            time.sleep(0.5)
        if etat is None:
            raise h.Refus("relais muet au démarrage")
        attendu = {"plafond_usd": h.PLAFOND_RELAIS_USD, "max_appels": h.MAX_APPELS_RELAIS, "appels": 0, "cle_presente": True}
        ecarts = {k: etat.get(k) for k, v in attendu.items() if etat.get(k) != v}
        if ecarts:
            raise h.Refus(f"relais : réglages inattendus {ecarts}")
        self.j.ecrire(f"relais {r.port} PID {self.relais.pid} : plafond {etat['plafond_usd']} USD, {etat['max_appels']} appels, clé "
                      f"présente (booléen), dépense {etat.get('depense_usd')}")

    def lancer_course(self) -> None:
        sortie = open(self.t / "course-stdout-a1-v4.log", "ab")
        self.course = subprocess.Popen(self.cmd_course(False), cwd=self.r.clone_public / "orchestrator", env=self.env_course(),
                                       stdout=sortie, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL, start_new_session=True)
        self.j.ecrire(f"course lancée : PID {self.course.pid} (processus lancé par l'hôte lui-même, sans coquille)")

    def garder(self) -> None:
        """Comme la v1 : relevé daté chaque minute (`garde-a1-v4.jsonl`), relais mort relancé seulement, plafonds de la machine."""
        r = self.r
        releves = self.t / "garde-a1-v4.jsonl"
        while True:
            code = self.course.poll()
            relais_vivant = self.relais.poll() is None
            etat = h.etat_relais(r.port) if relais_vivant else None
            ecoule = time.monotonic() - self.debut
            ligne = {"utc": h.maintenant(), "course_vivante": code is None, "relais_vivant": relais_vivant,
                     "appels": (etat or {}).get("appels"), "depense_argon_usd": (etat or {}).get("depense_usd"),
                     "ecoule_h": round(ecoule / 3600, 4), "cout_machine_usd": round(self.cout_machine(), 4)}
            with open(releves, "a", encoding="utf-8") as f:
                f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
            if code is not None:
                self.code_course = code
                (self.t / "code-sortie-lanceur.txt").write_text(f"{code}\n")
                self.j.ecrire(f"fin du lanceur : code {code}")
                self.nature_fin = "fin_du_lanceur"
                return
            if not relais_vivant:  # règle des guetteurs : relancer seulement, jamais arrêter
                self.j.ecrire(f"relais mort (code {self.relais.returncode}) : relancé avec les mêmes réglages")
                self._demarrer_relais()
            if ecoule >= r.duree_max_s or self.cout_machine() >= r.plafond_machine_usd:
                self.nature_fin = "plafond_de_la_machine"
                self.j.ecrire(f"PLAFOND DE LA MACHINE atteint ({ecoule / 3600:.3f} h, {self.cout_machine():.2f} USD) : la course est "
                              "arrêtée par son identifiant (écart déclaré, section 8 du texte)")
                self.code_course = h.arreter_par_pid(self.course, self.j, "course")
                (self.t / "code-sortie-lanceur.txt").write_text(f"{self.code_course} (arrêt au plafond de la machine)\n")
                return
            time.sleep(r.periode_s)

    def sceller(self) -> Path:
        self.copier_journaux_du_demarrage()
        liste = self.t / LISTE_EMPREINTES
        lignes = [f"{h.sha256_fichier(p)}  {p.relative_to(self.t)}" for p in self.fichiers_a_verser() if p != liste]
        liste.write_text("\n".join(lignes) + "\n")
        return liste

    def verser(self, branche: str, liste: Path) -> bool:
        r, gh = self.r, self.secrets["GH_TOKEN"]
        url = self._url()
        if h.git("ls-remote", url, f"refs/heads/{branche}", gh_token=gh, delai=DELAI_GIT_S).strip():
            raise h.Refus(f"branche {branche} déjà présente (R12) : rien n'est écrasé")
        suffixe = "-versement-interrompue-v1" if branche == BRANCHE_INTERROMPUE else "-versement"  # C3
        v = r.travail.parent / (r.travail.name + suffixe)
        if v.exists():
            raise h.Refus(f"copie de versement {v} déjà présente (R12)")
        h.git("clone", "-q", "--depth", "1", "--filter=blob:none", "--sparse", "--single-branch", "--branch", "main", url,
              str(v), gh_token=gh, delai=DELAI_GIT_S)
        h.git("sparse-checkout", "set", branche, cwd=v, gh_token=gh, delai=DELAI_GIT_S)
        h.git("checkout", "-q", "-b", branche, cwd=v, delai=DELAI_GIT_LOCAL_S)
        dest = v / branche
        dest.mkdir(parents=True, exist_ok=False)
        for p in self.fichiers_a_verser():
            cible = dest / p.relative_to(self.t)
            cible.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, cible)
        h.git("add", "-f", str(dest), cwd=v, delai=DELAI_GIT_LOCAL_S)
        h.git("-c", "user.name=hote-durable-a1-v4", "-c", "user.email=hote@invalid", "commit", "-q", "-m",
              f"A1-v4 : état scellé de l'hôte durable v5 ({self.nature_fin}), liste {h.sha256_fichier(liste)[:16]}…, versé avant "
              "toute lecture", cwd=v, delai=DELAI_GIT_LOCAL_S)
        c = self._pousser(v, branche, url)
        if not c:
            return False
        self.j.ecrire(f"versé : {branche} = {c} (vérifié par ls-remote) ; liste {h.sha256_fichier(liste)}")
        self.etat("verse")
        return True

    def se_detruire(self, pousse: bool) -> int:
        """Comme la v4 (destruction vérifiée par l'inventaire, sinon arrêt ; aucun geste sans identifiant, sur une instance protégée
        ou sous une autre étiquette) ; étiquette `a1-v4-v9`."""
        ident = self.env.get("CONTAINER_ID", "")
        ecrire = self._ecrire_sans_echec
        if not re.fullmatch(r"[0-9]{1,12}", ident or "") or int(ident) in PROTEGEES:
            ecrire(f"identifiant de la machine illisible ou protégé ({ident!r}) : aucun geste ; la minuterie et la session qui "
                   "reprend s'en chargent (R14)")
            return 4
        n = int(ident)
        try:
            client = self.client_vast()
        except Exception as x:
            ecrire(f"client de Vast impossible ({type(x).__name__}) : aucun geste ; la minuterie détruit à l'échéance")
            return 4
        try:
            vues = [i for i in client.instances() if i.get("id") == n]
            lab = vues[0].get("label") if vues else None
            if lab is not None and lab != ETIQUETTE:
                ecrire(f"étiquette lue {lab!r}, pas {ETIQUETTE} : aucun geste")
                return 4
        except Exception as x:
            ecrire(f"étiquette non lue ({type(x).__name__}) : geste par l'identifiant posé par Vast")
        if pousse:
            try:
                ecrire(f"destruction de la machine par son identifiant {n}")
                client.detruire(n)
                if not self._encore_listee(client, n):
                    return 0
                ecrire(f"machine {n} encore listée après la destruction : arrêt par son identifiant (correction 2)")
            except Exception as x:
                ecrire(f"destruction refusée ({type(x).__name__}) : arrêt de la machine {n} par son identifiant")
        else:
            ecrire(f"versement non vérifié : la machine {n} est ARRÊTÉE, non détruite (données gardées ; l'arrêt arrête aussi "
                   "la minuterie) ; la session qui reprend décide (R14)")
        try:
            client.arreter(n)
            return 3
        except Exception as x:
            ecrire(f"arrêt de la machine {n} refusé ({type(x).__name__}) : la minuterie détruit à l'échéance ; la session qui "
                   "reprend s'en charge (R14)")
            return 4


def reglages() -> h.Reglages:
    """Défauts de la v4 (80 h, 32 USD de garde, relevé chaque minute, interpréteur 3.13), dossier de travail de la v5."""
    return h.Reglages(travail=Path("/root") / TRAVAIL, essais_poussee=v4.ESSAIS_POUSSEE, attente_poussee_s=v4.ATTENTE_POUSSEE_S,
                      python_relais=v4.PYTHON_IMAGE, python_course=v4.PYTHON_IMAGE)


def principal(argv=None) -> int:
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sous = a.add_subparsers(dest="mode", required=True)
    l = sous.add_parser("louer", help=f"pilote : {NOM_GO_MACHINE_ENV} et GO_ID dans l'environnement ; la clé par {NOM_CLE_ARGON_PILOTE}")
    for nom in ("--registre-main", "--garde-main", "--offres", "--offre", "--commit-prive", "--commit-public", "--texte", "--sha-texte",
                "--configuration-mondes", "--commit-registre", "--journal-local"):
        l.add_argument(nom, required=True)
    l.add_argument("--racine-privee", help="racine du dépôt privé (défaut : déduite du chemin de la configuration)")
    l.add_argument("--verifier-seulement", action="store_true")
    vt = sous.add_parser("verifier-texte", help="le texte scellé et la configuration des mondes, sans rien créer")
    for nom in ("--texte", "--sha-texte", "--configuration-mondes"):
        vt.add_argument(nom, required=True)
    for nom in ("controler", "facturation"):
        c = sous.add_parser(nom)
        c.add_argument("--etat", required=True)
        c.add_argument("--journal-local", required=True)
    o = sous.add_parser("offre")
    o.add_argument("--offres", required=True)
    sous.add_parser("inventaire")
    sous.add_parser("hote")
    args = a.parse_args(argv)
    if args.mode == "louer":
        return louer(args)
    if args.mode == "verifier-texte":
        try:
            conf = lire_configuration_mondes(args.configuration_mondes)
            t = verifier_texte(args.texte, args.sha_texte, conf)
            n = verifier_fichiers_geles(Path(args.texte).resolve().parents[2], conf)
            print(json.dumps(dict(t, variante=conf["variante"], fichiers_geles_publics_egaux=n, configuration_sha256=conf["sha256"]),
                             ensure_ascii=False, indent=1))
            return 0
        except (h.Refus, OSError, ValueError, KeyError) as e:
            print(f"REFUS : {e}", file=sys.stderr)
            return 2
    if args.mode == "controler":
        return controler(args)
    if args.mode == "facturation":
        return relever_facturation(args)
    if args.mode == "offre":
        offres = json.loads(Path(args.offres).read_text())
        offres = offres.get("offers", offres) if isinstance(offres, dict) else offres
        conformes = []
        for x in offres:
            try:
                conformes.append(s10.verifier_offre_sonde([x], x.get("id")))
            except h.Refus:
                continue
        if not conformes:
            print("aucune offre conforme", file=sys.stderr)
            return 2
        print(min(conformes, key=lambda x: (x["dph_total"], x["id"]))["id"])
        return 0
    if args.mode == "inventaire":
        try:
            print(json.dumps([h.champs_filtres(i) for i in ClientPiloteV5(dict(os.environ)).instances()], ensure_ascii=False, indent=1))
            return 0
        except h.Refus as e:
            print(f"REFUS : {e}", file=sys.stderr)
            return 2
    return MachineV5(reglages(), dict(os.environ)).principal()


if __name__ == "__main__":
    sys.exit(principal())
