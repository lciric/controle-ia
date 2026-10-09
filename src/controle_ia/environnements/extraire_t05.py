"""Extraction des tâches de T0.5 selon la procédure v1 (`docs/procedures/T0.5-extraction-v1.md`).

Préparation des dossiers des sous-agents neufs (un par papier et par tentative, ou par papier et par ronde de
contre-vérification), contrôle de leurs sorties, échantillon, lecture des avis, assemblage des tâches d'évaluation et
d'entraînement. Aucun appel à un modèle : la session lance chaque sous-agent avec l'invite fixe `INVITE_AGENT`, qui le
renvoie à la consigne d'enveloppe scellée copiée dans son dossier, puis transmet ses retours (dernière ligne rendue,
nombre de lancements) à l'étape de lecture.

Rangement : `diag/<run>/` (dépôt) reçoit les résultats sans texte des papiers : empreintes, codes d'anomalie, statuts,
compteurs. `donnees/<run>/` (hors du dépôt, règle de sélection, section 9) reçoit, scellés, ce qui porte du texte des
papiers : archives des sorties et des avis, détails des anomalies, tâches assemblées (nœud N-014 ouvert). Chaque
résultat est rattaché au manifeste du run (R9) et porte l'état git de l'étape ; rien n'est écrasé (R12) ; la
procédure, ses fichiers, les invites et les deux modules de décision sont contrôlés par empreinte à chaque étape ; tout
écart à la procédure arrête (`GardeArret`).

Commandes (depuis la racine du dépôt, PYTHONPATH=src) :
    python -m controle_ia.environnements.extraire_t05 preparer --run-id R --travail W --tentative K [--papiers A,B]
    … valider --run-id R --tentative K --retours FICHIER
    … echantillonner --run-id R
    … preparer-contre-verification --run-id R --travail W --role echantillon|theorie|audit|reprise [--papiers A,B]
    … lire-contre-verification --run-id R --ronde N --retours FICHIER
    … assembler --run-id R
    … controler --run-id R      (règle de perte rejouée, sans rien écrire si rien n'est perdu)
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
from dataclasses import dataclass
from pathlib import Path

from ..gardes import GardeArret, etat_git
from ..manifeste import creer_manifeste, ecrire_resultat, lire_manifeste, verifier_resultat
from ..scellement import empreinte, sceller, verifier
from . import extraction as ex
from .invites import RACINE_INVITES, charger_invite, empreinte_invite

INVITE_AGENT = ("This task is self-contained: ignore any project instructions or session routines, and open no file "
                "other than those named in the instructions. Read the file {consigne} and follow its instructions "
                "exactly.")
TACHE_GRAINE = "echantillon-contre-verification"
TAILLE_ECHANTILLON = 16
SEUIL_ECHECS = 4
TAILLE_AUDIT = 4
TAILLE_PILOTE, TAILLE_RESERVE = 64, 32
ROLES = ex.ROLES_VERDICT
LANCEMENTS_MAX = 3              # un lancement et deux relances au plus par sous-agent (contre-lecture 2, D-16)
AVIS_MAX_PAR_ROLE = 3           # un avis et deux avis refaits au plus par papier et par rôle (D-16)
SEUIL_EXCLUSIONS_VALIDATION = 16  # papiers invalides aux tentatives 1 et 2 au-delà desquels on arrête (D-17)
RETOUR_FORME = re.compile(r"(NOT )?OK: \d+ error\(s\)(, \d+ warning\(s\))?")
_ERREUR_SCRIPT = re.compile(r"ERROR: \[([a-z0-9_.]+)\]")
SOUS_DOSSIERS_D_ENTREE = ("papier", "invites", "a-verifier")   # un fichier ajouté ici est une entrée modifiée (E-7)
ARRETS_DEFINITIFS = ("arret-perte", "arret-desaccord-script")   # après eux, aucune étape du run (contre-lecture 3)
DELAI_SCRIPT_S = 600


@dataclass(frozen=True)
class Chemins:
    """Chemins relatifs à la racine du dépôt (modifiables pour les tests)."""
    procedure: str = "docs/procedures/T0.5-extraction-v1.md"
    dossier_procedure: str = "docs/procedures/T0.5-extraction-v1"
    corpus: str = "diag/20261006-134235-t05-corpus/corpus.json"
    textes: str = "donnees/T0.5-corpus-v1/textes"
    invites: Path = RACINE_INVITES
    modules: tuple = ("src/controle_ia/environnements/extraction.py", "src/controle_ia/environnements/extraire_t05.py",
                      "src/controle_ia/manifeste.py")


FICHIERS_PROCEDURE = {"invite_cibles": "invite-cibles-v1.txt", "consigne_extracteur": "consigne-extracteur-v1.txt",
                      "consigne_contre_verificateur": "consigne-contre-verificateur-v1.txt",
                      "verifier_sortie": "verifier-sortie-v1.py", "verifier_avis": "verifier-avis-v1.py"}


def _sha(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


# ------------------------------------------------------------------------------------------------ gardes communes

def fichiers_scelles(racine: Path, ch: Chemins) -> dict:
    """Empreintes de la procédure et de ses fichiers (sceaux vérifiés), des invites H.9 et H.10 (index vérifié) et
    des deux modules de décision (CL-8 : le code qui décide est épinglé pour tout le run)."""
    e = {"procedure": verifier(racine / ch.procedure)}
    for cle, nom in FICHIERS_PROCEDURE.items():
        e[cle] = verifier(racine / ch.dossier_procedure / nom)
    for ident in ("H9", "H10"):
        e[ident] = empreinte_invite(ident, ch.invites)
    for m in ch.modules:
        e[f"module:{Path(m).name}"] = empreinte(racine / m)
    return e


def papiers_du_corpus(racine: Path, ch: Chemins) -> list[dict]:
    """Les 96 papiers gardés par la sélection scellée, dans l'ordre du rang de garde (64 du pilote, puis 32 de
    réserve)."""
    corps = verifier_resultat(racine, racine / ch.corpus)
    gardes = sorted((f for f in corps["resultat"]["fiches"] if f["statut"] == "gardé"), key=lambda f: f["rang_garde"])
    if len(gardes) != TAILLE_PILOTE + TAILLE_RESERVE or [f["rang_garde"] for f in gardes] != list(range(len(gardes))):
        raise GardeArret(f"corpus : {len(gardes)} papiers gardés ou rangs non contigus")
    return [{"id": f"{f['id']}v{f['version']}", "texte_sha256": f["texte_sha256"]} for f in gardes]


def lire_texte(racine: Path, ch: Chemins, papier: dict) -> str:
    """Texte converti d'un papier, après contrôle de son empreinte contre le corpus scellé (R11)."""
    octets = (racine / ch.textes / f"{papier['id']}.md").read_bytes()
    if _sha(octets) != papier["texte_sha256"]:
        raise GardeArret(f"{papier['id']} : texte converti altéré (empreinte ≠ corpus)")
    return octets.decode("utf-8")


def _hors_depot(racine: Path, travail: Path) -> Path:
    t = travail.resolve()
    if t == racine.resolve() or racine.resolve() in t.parents:
        raise GardeArret(f"dossier de travail {t} dans le dépôt : il doit être hors du dépôt (textes des papiers)")
    return t


def _manifeste(racine: Path, run_id: str) -> Path:
    return racine / "runs" / run_id / "manifeste.json"


def _diag(racine: Path, run_id: str, nom: str) -> Path:
    return racine / "diag" / run_id / f"{nom}.json"


def _resultat(racine: Path, run_id: str, nom: str) -> dict:
    return verifier_resultat(racine, _diag(racine, run_id, nom))["resultat"]


def _git(racine: Path) -> dict:
    g = etat_git(racine)
    return {"commit": g["commit"], "propre": g["propre"]}


def _ouvrir_run(racine: Path, run_id: str, ch: Chemins, etape: str) -> dict:
    """À chaque étape : manifeste lu, fichiers épinglés inchangés depuis l'ouverture du run (CL-8), aucun arrêt
    définitif consigné, rien de perdu (règle de perte, contre-lecture 3, E-2)."""
    m, _ = lire_manifeste(_manifeste(racine, run_id))
    if str(Path(racine).resolve()) != m["config"]["racine"]:      # vérification 4, V-4 : jamais depuis une autre copie
        raise GardeArret(f"étape lancée depuis {Path(racine).resolve()}, hors de la racine du run "
                         f"({m['config']['racine']}) : rien n'est contrôlé ni écrit")
    if fichiers_scelles(racine, ch) != m["config"]["fichiers_scelles"]:
        raise GardeArret("procédure, invites, scripts ou modules de décision changés depuis l'ouverture du run")
    for nom in ARRETS_DEFINITIFS:
        if _diag(racine, run_id, nom).exists():
            raise GardeArret(f"run arrêté ({nom} consigné) : aucune étape ne suit ; run nouveau (procédure, section 8)")
    exiger_rien_de_perdu(racine, run_id, etape)
    return m


def _arreter(racine: Path, run_id: str, nom: str, contenu: dict, message: str) -> None:
    """Arrêt consigné par un résultat scellé dans `diag/` avant l'exception (contre-lecture 3, E-8) ; s'il l'est déjà,
    l'arrêt se répète sans rien écrire."""
    if not _diag(racine, run_id, nom).exists():
        _ecrire(racine, run_id, nom, contenu)
    raise GardeArret(message)


def fichiers_consignes(racine: Path, run_id: str) -> dict[str, str]:
    """Fichiers de `donnees/<run>/` dont l'empreinte est consignée dans `diag/` (nom → empreinte) : archives et détails
    des validations et des rondes lues, tâches assemblées."""
    f = {}
    for k in (1, 2, 3):
        if _diag(racine, run_id, f"validation-tentative-{k}").exists():
            r = _resultat(racine, run_id, f"validation-tentative-{k}")
            f[f"sorties-tentative-{k}.tar"] = r["archive_sorties_sha256"]
            f[f"details-validation-tentative-{k}.json"] = r["details_sha256"]
    n = 1
    while _diag(racine, run_id, f"preparation-contre-verification-ronde-{n}").exists():
        if _diag(racine, run_id, f"contre-verification-ronde-{n}").exists():
            r = _resultat(racine, run_id, f"contre-verification-ronde-{n}")
            f[f"avis-ronde-{n}.tar"] = r["archive_avis_sha256"]
            f[f"details-contre-verification-ronde-{n}.json"] = r["details_sha256"]
        n += 1
    if _diag(racine, run_id, "bilan-extraction").exists():
        r = _resultat(racine, run_id, "bilan-extraction")
        f["taches-evaluation.json"] = r["taches_evaluation_sha256"]
        f["taches-entrainement.json"] = r["taches_entrainement_sha256"]
    return f


def _preparations_non_lues(racine: Path, run_id: str) -> list[str]:
    noms = [f"preparation-tentative-{k}" for k in (1, 2, 3)
            if _diag(racine, run_id, f"preparation-tentative-{k}").exists()
            and not _diag(racine, run_id, f"validation-tentative-{k}").exists()]
    n = 1
    while _diag(racine, run_id, f"preparation-contre-verification-ronde-{n}").exists():
        if not _diag(racine, run_id, f"contre-verification-ronde-{n}").exists():
            noms.append(f"preparation-contre-verification-ronde-{n}")
        n += 1
    return noms


def exiger_rien_de_perdu(racine: Path, run_id: str, etape: str) -> None:
    """Règle de perte (procédure, section 8 ; contre-lecture 3, E-2), à chaque étape : chaque fichier de `donnees/<run>/`
    consigné dans `diag/` est présent, scellé, à l'empreinte consignée, et le dossier de travail de chaque préparation
    non lue existe ; sinon `arret-perte` scellé (étape, fichiers en cause), puis arrêt. Un dossier de papier disparu
    seul reste une entrée modifiée de ce papier (CL-5)."""
    en_cause = []
    for nom, sha in sorted(fichiers_consignes(racine, run_id).items()):
        chemin = racine / "donnees" / run_id / nom
        try:
            intact = verifier(chemin) == sha
        except (GardeArret, OSError, ValueError):      # compagnon illisible compris (vérification 4, V-7)
            intact = False
        if not intact:
            en_cause.append(f"donnees/{run_id}/{nom}")
    for nom in _preparations_non_lues(racine, run_id):
        d = Path(_resultat(racine, run_id, nom)["travail"])
        if not d.is_dir():
            en_cause.append(str(d))
    if en_cause:
        _arreter(racine, run_id, "arret-perte", {
            "etape": etape, "fichiers_en_cause": en_cause,
            "suite": "aucune sortie du run perdu n'est relue ; run nouveau sous la même procédure, à la tentative 1"},
            f"perte de données du run ({len(en_cause)} : {en_cause[:3]}) : arrêt consigné ; run nouveau")


def _ecrire(racine: Path, run_id: str, nom: str, contenu: dict) -> Path:
    return ecrire_resultat(racine, _manifeste(racine, run_id), nom, dict(contenu, git=_git(racine)))


def ecrire_donnees(racine: Path, run_id: str, nom: str, contenu: dict) -> str:
    """Résultat portant du texte des papiers : `donnees/<run>/<nom>.json`, hors du dépôt, scellé et rattaché au
    manifeste par son empreinte ; rend l'empreinte, à consigner dans `diag/`."""
    _, sha_m = lire_manifeste(_manifeste(racine, run_id))
    chemin = racine / "donnees" / run_id / f"{nom}.json"
    corps = {"run_id": run_id, "manifeste_sha256": sha_m, "resultat": contenu}
    try:
        octets = (json.dumps(corps, indent=2, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8")
    except UnicodeEncodeError as e:
        raise GardeArret(f"{chemin} : contenu non encodable en UTF-8 ({e.reason}) ; ce fichier n'est pas écrit") \
            from None
    return _ecrire_atomique(chemin, octets)


def _ecrire_atomique(cible: Path, octets: bytes) -> str:
    """Écrit puis scelle `cible` par un fichier provisoire renommé ; idempotent sur un contenu identique (une étape
    interrompue après cette écriture se refait), arrêt sur un contenu différent (R12 ; contre-lecture 2, D-10)."""
    if cible.exists():
        if cible.read_bytes() != octets:
            raise GardeArret(f"{cible} existe déjà avec un autre contenu (R12)")
        return sceller(cible)
    cible.parent.mkdir(parents=True, exist_ok=True)
    provisoire = cible.with_name(cible.name + ".provisoire")
    provisoire.write_bytes(octets)
    os.replace(provisoire, cible)
    return sceller(cible)


def lire_donnees(racine: Path, run_id: str, nom: str, sha: str) -> dict:
    chemin = racine / "donnees" / run_id / f"{nom}.json"
    if verifier(chemin) != sha:
        raise GardeArret(f"{chemin} : empreinte différente de celle consignée")
    return json.loads(chemin.read_text(encoding="utf-8"))["resultat"]


def archiver(cible: Path, membres: list[tuple[str, bytes]]) -> str:
    """Archive tar déterministe (noms triés, dates et propriétaires neutres), scellée ; rend son empreinte. Écriture
    atomique, idempotente sur un contenu identique (D-10)."""
    tampon = io.BytesIO()
    with tarfile.open(fileobj=tampon, mode="w", format=tarfile.PAX_FORMAT) as tar:
        for nom, octets in sorted(membres):
            info = tarfile.TarInfo(nom)
            info.size, info.mtime, info.mode = len(octets), 0, 0o644
            tar.addfile(info, io.BytesIO(octets))
    return _ecrire_atomique(cible, tampon.getvalue())


def lire_archive(chemin: Path, sha: str) -> dict[str, bytes]:
    if verifier(chemin) != sha:
        raise GardeArret(f"{chemin} : empreinte différente de celle consignée")
    with tarfile.open(chemin, mode="r") as tar:
        return {m.name: tar.extractfile(m).read() for m in tar.getmembers() if m.isfile()}


def _empreintes_dossier(d: Path) -> dict[str, str]:
    return {str(p.relative_to(d)): _sha(p.read_bytes()) for p in sorted(d.rglob("*")) if p.is_file()}


def _entrees_modifiees(d: Path, entrees: dict[str, str]) -> list[str]:
    """Entrées du dossier modifiées ou absentes depuis la préparation (CL-5), et fichiers ajoutés parmi les entrées
    (sous `SOUS_DOSSIERS_D_ENTREE` : un fichier ajouté sous `papier/` changerait le texte que lit le script ;
    contre-lecture 3, E-7)."""
    modifiees = {rel for rel, sha in entrees.items() if not (d / rel).is_file() or _sha((d / rel).read_bytes()) != sha}
    attendus = set(entrees) | {str(Path(rel).parent) for rel in entrees}
    for sous in SOUS_DOSSIERS_D_ENTREE:      # tout chemin ajouté : fichier, dossier, lien, tube (vérification 4, V-2)
        if (d / sous).is_dir():
            modifiees |= {str(p.relative_to(d)) for p in (d / sous).rglob("*") if str(p.relative_to(d)) not in attendus}
    # noms non UTF-8 écrits échappés : les résultats restent encodables (vérification 4, V-1)
    return sorted(os.fsencode(m).decode("utf-8", "backslashreplace") for m in modifiees)


def _exiger_retours(retours: dict, papiers: list[str]) -> None:
    """Une étape de lecture ne se lance qu'après le retour de tous les sous-agents (CL-13) : un retour par papier,
    avec la dernière ligne rendue et le nombre de lancements."""
    if sorted(retours) != sorted(papiers):
        raise GardeArret(f"retours des sous-agents incomplets ou en trop : manquants "
                         f"{sorted(set(papiers) - set(retours))[:5]}, en trop {sorted(set(retours) - set(papiers))[:5]}")
    for p, r in retours.items():
        if not (isinstance(r, dict) and set(r) == {"derniere_ligne", "lancements"}
                and isinstance(r["derniere_ligne"], str) and isinstance(r["lancements"], int)
                and not isinstance(r["lancements"], bool) and 1 <= r["lancements"] <= LANCEMENTS_MAX):
            raise GardeArret(f"{p} : retour mal formé (deux clés, dernière ligne textuelle, 1 à {LANCEMENTS_MAX} "
                             "lancements)")


def retour_sans_texte(r: dict, anomalies_module: bool) -> dict:
    """Ce que `diag/` garde d'un retour (contre-lecture 2, D-13) : lancements, forme de la dernière ligne, annonce
    (« OK » ou « NOT OK ») et son accord avec le module, consignés sans arrêt (D-2). La ligne brute, qui peut porter du
    texte du papier, ne va que dans `donnees/`."""
    m = RETOUR_FORME.fullmatch(r["derniere_ligne"].strip())
    annonce = None if m is None else ("NOT OK" if m.group(1) else "OK")
    return {"lancements": r["lancements"], "forme": "conforme" if m else "retour.hors_format", "annonce": annonce,
            "accord_avec_le_module": None if annonce is None else (annonce == "OK") == (not anomalies_module)}


def codes_du_script(script: Path, dossier: Path) -> list[str]:
    """Codes d'erreur que rend la copie scellée du script de contrôle (celle du dépôt, jamais celle du dossier du
    sous-agent) sur un dossier (contre-lecture 2, D-2). Une sortie hors forme, un code de retour inattendu ou un délai
    dépassé arrêtent : panne de processus, sans résultat écrit ; l'étape se relance (contre-lecture 3, E-8)."""
    try:
        r = subprocess.run([sys.executable, "-I", str(script), str(dossier)], capture_output=True,
                           timeout=DELAI_SCRIPT_S)
    except subprocess.TimeoutExpired:
        raise GardeArret(f"script de contrôle {script.name} : délai de {DELAI_SCRIPT_S} s dépassé sur {dossier.name} "
                         "(panne de processus ; l'étape n'a rien écrit et se relance)") from None
    lignes = r.stdout.decode("utf-8", errors="replace").splitlines()
    if r.returncode not in (0, 1) or not lignes or not RETOUR_FORME.fullmatch(lignes[-1].strip()):
        raise GardeArret(f"script de contrôle {script.name} hors forme sur {dossier.name} (code {r.returncode})")
    return [m.group(1) for ligne in lignes for m in [_ERREUR_SCRIPT.match(ligne)] if m]


def exiger_accord_script(pid: str, codes_script: list[str], codes_module: list[str]) -> None:
    """Désaccord du script scellé et du module en production, entrées intactes : arrêt (D-2)."""
    if sorted(codes_script) != sorted(codes_module):
        raise GardeArret(f"{pid} : le script scellé rend {sorted(codes_script)[:4]}, le module {sorted(codes_module)[:4]} :"
                         " désaccord en production")


def _accord_ou_arret(racine: Path, run_id: str, etape: str, pid: str, script: Path, dossier: Path,
                     codes_module: list[str]) -> None:
    """Accord du script scellé et du module ; un désaccord est définitif (scripts et modules épinglés) : arrêt scellé
    `arret-desaccord-script`, puis version 2 et run nouveau (contre-lecture 3, E-8)."""
    codes_script = codes_du_script(script, dossier)
    try:
        exiger_accord_script(pid, codes_script, codes_module)
    except GardeArret as e:
        _arreter(racine, run_id, "arret-desaccord-script", {
            "etape": etape, "papier": pid, "codes_script": sorted(codes_script), "codes_module": sorted(codes_module),
            "suite": "version 2 de la procédure, puis run nouveau"}, str(e))


def _encodable(objet) -> bool:
    try:
        json.dumps(objet, ensure_ascii=False).encode("utf-8")
        return True
    except UnicodeEncodeError:
        return False


# ------------------------------------------------------------------------------------------------ préparation

def _remplir(modele: str, dossier: Path, parties: list[Path]) -> str:
    texte = (modele.replace("<<DOSSIER>>", str(dossier)).replace("<<N>>", str(len(parties)))
             .replace("<<PARTIES>>", ", ".join(str(p) for p in parties)))
    if "<<" in texte:
        raise GardeArret("consigne : champ non rempli")
    return texte


def _dossier_agent(racine: Path, ch: Chemins, parties: list[str], d: Path, modele: str, script: str,
                   a_verifier: dict[str, bytes] | None = None) -> dict:
    """Dossier d'un sous-agent : invites, copie de lecture du papier, script de contrôle, réponses à vérifier (pour un
    contre-vérificateur), consigne remplie ; toutes ses entrées empreintées (CL-5)."""
    (d / "invites").mkdir(parents=True)
    (d / "papier").mkdir()
    (d / "invites" / "H9.txt").write_text(charger_invite("H9", ch.invites), encoding="utf-8")
    (d / "invites" / "H10.txt").write_text(charger_invite("H10", ch.invites), encoding="utf-8")
    shutil.copyfile(racine / ch.dossier_procedure / FICHIERS_PROCEDURE["invite_cibles"], d / "invites" / "cibles.txt")
    chemins = []
    for k, partie in enumerate(parties, start=1):
        p = d / "papier" / f"partie-{k:02d}.md"
        p.write_text(partie, encoding="utf-8")
        chemins.append(p)
    shutil.copyfile(racine / ch.dossier_procedure / FICHIERS_PROCEDURE[script], d / f"{script}.py")
    if a_verifier is not None:
        (d / "a-verifier").mkdir()
        for nom, octets in a_verifier.items():
            (d / "a-verifier" / f"{nom}.json").write_bytes(octets)
    consigne = _remplir(modele, d, chemins)
    (d / "consigne.txt").write_text(consigne, encoding="utf-8")
    return {"dossier": str(d), "entrees": _empreintes_dossier(d), "parties": len(parties),
            "invite_agent": INVITE_AGENT.format(consigne=d / "consigne.txt")}


def preparer(racine: Path, run_id: str, travail: Path, tentative: int, papiers: list[str] | None = None,
             ch: Chemins = Chemins(), commande: str | None = None) -> dict:
    """Prépare une tentative d'extraction. Tentative 1 : les 96 papiers. Tentatives 2 et 3 : exactement les papiers
    dus (invalides à la tentative 1 ; reprises dues après contre-vérification), tous à la fois."""
    racine = Path(racine)
    travail = _hors_depot(racine, Path(travail))
    tous = papiers_du_corpus(racine, ch)
    par_id = {p["id"]: p for p in tous}
    base = travail / f"tentative-{tentative}"
    if tentative == 1:
        if papiers:
            raise GardeArret("la tentative 1 porte sur les 96 papiers")
        if base.exists():
            raise GardeArret(f"{base} existe déjà (R12)")
        choisis = tous
        # tous les contrôles avant le manifeste (CL-12) : un arrêt ici ne « brûle » pas le run
        copies = {p["id"]: ex.copie_de_lecture(lire_texte(racine, ch, p)) for p in choisis}
        scelles = fichiers_scelles(racine, ch)
        config = {"tache": "T0.5 extraction des énoncés, classifications et cibles (procédure v1)",
                  "procedure": ch.procedure, "fichiers_scelles": scelles, "corpus": ch.corpus,
                  "corpus_sha256": empreinte(racine / ch.corpus), "textes": ch.textes,
                  "pilote": [p["id"] for p in tous[:TAILLE_PILOTE]], "reserve": [p["id"] for p in tous[TAILLE_PILOTE:]],
                  "copie_de_lecture": {"taille_partie": ex.TAILLE_PARTIE, "lignes_partie": ex.LIGNES_PARTIE},
                  "bornes_cibles": {k: list(v) for k, v in ex.BORNES_CIBLES.items()}, "mots_fuite": ex.MOTS_FUITE,
                  "echantillon": TAILLE_ECHANTILLON, "seuil_echecs": SEUIL_ECHECS, "audit": TAILLE_AUDIT,
                  "minimum_entrainement": ex.MINIMUM_ENTRAINEMENT, "invite_agent": INVITE_AGENT,
                  "travail": str(travail), "racine": str(racine.resolve())}
        creer_manifeste(racine, run_id, config, [TACHE_GRAINE], entropie=int(scelles["procedure"][:32], 16),
                        commande=commande)
    else:
        m = _ouvrir_run(racine, run_id, ch, f"preparation-tentative-{tentative}")
        if travail != Path(m["config"]["travail"]):
            raise GardeArret("dossier de travail différent de celui du manifeste")
        if _diag(racine, run_id, f"preparation-tentative-{tentative}").exists():
            raise GardeArret(f"tentative {tentative} déjà préparée (R12)")
        if base.exists():               # préparation interrompue avant son résultat : dossier mis de côté, sans destruction
            k = 1
            while base.with_name(f"{base.name}-interrompue-{k}").exists():
                k += 1
            base.rename(base.with_name(f"{base.name}-interrompue-{k}"))
        if tentative == 2:
            dus = sorted(_resultat(racine, run_id, "validation-tentative-1")["invalides"])
        elif tentative == 3:
            dus = reprises_dues(racine, run_id)
        else:
            raise GardeArret("tentatives 1, 2 et 3 seulement")
        if sorted(papiers or []) != dus or not dus:
            raise GardeArret(f"tentative {tentative} : les papiers dus sont {dus[:8]}, tous à la fois, et eux seuls")
        choisis = [par_id[i] for i in dus]
        copies = {p["id"]: ex.copie_de_lecture(lire_texte(racine, ch, p)) for p in choisis}
    modele = (racine / ch.dossier_procedure / FICHIERS_PROCEDURE["consigne_extracteur"]).read_text(encoding="utf-8")
    fiches = {}
    for p in choisis:
        d = base / p["id"]
        fiche = _dossier_agent(racine, ch, copies[p["id"]], d, modele, "verifier_sortie")
        (d / "sorties").mkdir()
        fiches[p["id"]] = fiche
    resultat = {"tentative": tentative, "travail": str(base), "papiers": fiches}
    _ecrire(racine, run_id, f"preparation-tentative-{tentative}", resultat)
    return resultat


# ------------------------------------------------------------------------------------------------ validation

def valider(racine: Path, run_id: str, tentative: int, retours: dict, ch: Chemins = Chemins()) -> dict:
    """Contrôle des sorties d'une tentative, archivage scellé des sorties (CL-11), résultats sans texte dans `diag/`
    (codes d'anomalie) et détails dans `donnees/`. Une entrée modifiée par un sous-agent est une anomalie de son seul
    papier (CL-5). Le module exécute la copie scellée du script sur chaque dossier aux entrées intactes et compare les
    codes : un écart arrête (contre-lecture 2, D-2) ; la dernière ligne rendue par le sous-agent est seulement
    consignée. Au-delà de `SEUIL_EXCLUSIONS_VALIDATION` papiers invalides à la tentative 2, arrêt scellé (D-17)."""
    racine = Path(racine)
    _ouvrir_run(racine, run_id, ch, f"validation-tentative-{tentative}")
    prep = _resultat(racine, run_id, f"preparation-tentative-{tentative}")
    _exiger_retours(retours, list(prep["papiers"]))
    par_id = {p["id"]: p for p in papiers_du_corpus(racine, ch)}
    script = racine / ch.dossier_procedure / FICHIERS_PROCEDURE["verifier_sortie"]
    fiches, details, membres = {}, {}, []
    for pid, info in sorted(prep["papiers"].items()):
        d = Path(info["dossier"])
        modifiees = _entrees_modifiees(d, info["entrees"])
        r = ex.lire_sorties(d / "sorties", lire_texte(racine, ch, par_id[pid]))
        if not modifiees:
            _accord_ou_arret(racine, run_id, f"validation-tentative-{tentative}", pid, script, d,
                             [ex.code_anomalie(a) for a in r["anomalies"]])
        anomalies = r["anomalies"] + ([f"[entrees.modifiees] entrées modifiées : {modifiees}"] if modifiees else [])
        for nom in ex.NOMS_SORTIES:
            chemin = d / "sorties" / f"{nom}.json"
            if chemin.is_file():
                octets = chemin.read_bytes()
                if _sha(octets) != r["empreintes"][nom]:      # on archive les octets mêmes qui ont été empreintés
                    raise GardeArret(f"{pid} : {nom}.json modifié pendant la validation")
                membres.append((f"tentative-{tentative}/{pid}/{nom}.json", octets))
        fiches[pid] = {"anomalies": [ex.code_anomalie(a) for a in anomalies], "alertes": r["alertes"],
                       "theory_only": not anomalies and r["theory_only"], "empreintes": r["empreintes"],
                       "entrees_modifiees": modifiees, "retour": retour_sans_texte(retours[pid], bool(anomalies))}
        details[pid] = {"anomalies": anomalies, "derniere_ligne": retours[pid]["derniere_ligne"]}
    sha_archive = archiver(racine / "donnees" / run_id / f"sorties-tentative-{tentative}.tar", membres)
    sha_details = ecrire_donnees(racine, run_id, f"details-validation-tentative-{tentative}", {"papiers": details})
    resultat = {"tentative": tentative, "papiers": fiches,
                "invalides": sorted(p for p, f in fiches.items() if f["anomalies"]),
                "theory_only": sorted(p for p, f in fiches.items() if f["theory_only"]),
                "avec_alertes": sorted(p for p, f in fiches.items() if f["alertes"]),
                "archive_sorties_sha256": sha_archive, "details_sha256": sha_details}
    _ecrire(racine, run_id, f"validation-tentative-{tentative}", resultat)
    if tentative == 2 and len(resultat["invalides"]) > SEUIL_EXCLUSIONS_VALIDATION:
        codes: dict[str, int] = {}
        for pid in resultat["invalides"]:
            for c in fiches[pid]["anomalies"]:
                codes[c] = codes.get(c, 0) + 1
        _ecrire(racine, run_id, "arret-exclusions-validation", {
            "exclus": resultat["invalides"], "codes": dict(sorted(codes.items())),
            "suite": "audit R4 des codes (faux positif systématique ?), porté à Lazar ; version 2 si établi"})
        raise GardeArret(f"{len(resultat['invalides'])} papiers invalides aux tentatives 1 et 2 (seuil "
                         f"{SEUIL_EXCLUSIONS_VALIDATION}) : audit R4, nœud")
    return resultat


def _validations(racine: Path, run_id: str) -> dict[int, dict]:
    v = {}
    for k in (1, 2, 3):
        if _diag(racine, run_id, f"validation-tentative-{k}").exists():
            v[k] = _resultat(racine, run_id, f"validation-tentative-{k}")["papiers"]
        elif _diag(racine, run_id, f"preparation-tentative-{k}").exists():
            raise GardeArret(f"tentative {k} préparée et non validée")
    return v


def _tentative_retenue(pid: str, validations: dict[int, dict]) -> int | None:
    """Tentative retenue à l'étape de validation (1, ou 2 si 1 est invalide) ; None si les deux sont invalides."""
    if validations[1][pid]["anomalies"]:
        if 2 not in validations or pid not in validations[2]:
            raise GardeArret(f"{pid} : invalide à la tentative 1 et non refait")
        return None if validations[2][pid]["anomalies"] else 2
    return 1


def echantillonner(racine: Path, run_id: str, ch: Chemins = Chemins()) -> dict:
    """Échantillon de contre-vérification (tiré après les tentatives 1 et 2) et liste des exclusions « theory_only »
    à vérifier (CL-25)."""
    racine = Path(racine)
    m = _ouvrir_run(racine, run_id, ch, "echantillon-contre-verification")
    validations = _validations(racine, run_id)
    if 3 in validations or _diag(racine, run_id, "preparation-tentative-3").exists():
        raise GardeArret("échantillon tiré après une tentative 3 : ordre de la procédure non suivi")
    v2 = validations.get(2)
    if _diag(racine, run_id, "arret-exclusions-validation").exists() or (
            v2 is not None and sum(bool(f["anomalies"]) for f in v2.values()) > SEUIL_EXCLUSIONS_VALIDATION):
        # le seuil se relit depuis la validation 2 : une interruption avant l'écriture de l'arrêt ne le contourne pas
        raise GardeArret("arrêt après la tentative 2 (exclusions au-delà du seuil) : rien ne se tire")
    ordre = m["config"]["pilote"] + m["config"]["reserve"]
    admissibles, theorie = set(), []
    for pid in ordre:
        k = _tentative_retenue(pid, validations)
        if k is None:
            continue
        if validations[k][pid]["theory_only"]:
            theorie.append(pid)
        else:
            admissibles.add(pid)
    retenus, permutation = ex.echantillon_contre_verification(ordre, m["graines"][TACHE_GRAINE], admissibles,
                                                              TAILLE_ECHANTILLON)
    resultat = {"echantillon": retenus, "permutation": permutation, "admissibles": sorted(admissibles),
                "theory_only": theorie, "graine": m["graines"][TACHE_GRAINE]}
    _ecrire(racine, run_id, "echantillon-contre-verification", resultat)
    return resultat


# ------------------------------------------------------------------------------------------------ contre-vérification

def _rondes(racine: Path, run_id: str) -> list[dict]:
    """Rondes préparées, dans l'ordre ; chacune doit avoir été lue (CL-4 : aucune ronde omise en silence)."""
    rondes, n = [], 1
    while _diag(racine, run_id, f"preparation-contre-verification-ronde-{n}").exists():
        if not _diag(racine, run_id, f"contre-verification-ronde-{n}").exists():
            raise GardeArret(f"ronde {n} préparée et non lue")
        rondes.append(_resultat(racine, run_id, f"contre-verification-ronde-{n}"))
        n += 1
    if _diag(racine, run_id, f"contre-verification-ronde-{n}").exists():
        raise GardeArret(f"ronde {n} lue sans préparation")
    return rondes


def _rondes_lues(racine: Path, run_id: str) -> list[dict]:
    """Rondes déjà lues, dans l'ordre (les rondes préparées et pas encore lues sont ignorées : rondes parallèles)."""
    rondes, n = [], 1
    while _diag(racine, run_id, f"preparation-contre-verification-ronde-{n}").exists():
        if _diag(racine, run_id, f"contre-verification-ronde-{n}").exists():
            rondes.append(_resultat(racine, run_id, f"contre-verification-ronde-{n}"))
        n += 1
    return rondes


def verdicts_lisibles(rondes: list[dict]) -> dict[str, list[dict]]:
    """Verdicts lisibles par papier, dans l'ordre des rondes."""
    v: dict[str, list[dict]] = {}
    for r in rondes:
        for pid, f in r["papiers"].items():
            if f["lisible"]:
                v.setdefault(pid, []).append({"role": r["role"], "tentative": f["tentative"], "motifs": f["motifs"],
                                              "cibles_defectueuses": f.get("cibles_defectueuses", 0),
                                              "cibles": f.get("cibles", 0), "ronde": r["ronde"]})
    return v


def _premier_verdict(verdicts: dict, pid: str, role: str, tentative: int | None) -> dict | None:
    return next((v for v in verdicts.get(pid, []) if v["role"] == role and v["tentative"] == tentative), None)


def bilan_echantillon(racine: Path, run_id: str, rondes: list[dict] | None = None) -> dict | None:
    """Échecs et cibles défectueuses de l'échantillon, au premier avis lisible de chaque papier ; None tant qu'un
    papier de l'échantillon n'a pas d'avis lisible."""
    rondes = _rondes(racine, run_id) if rondes is None else rondes
    ech = _resultat(racine, run_id, "echantillon-contre-verification")["echantillon"]
    validations = _validations(racine, run_id)
    verdicts = verdicts_lisibles(rondes)
    premiers = {p: _premier_verdict(verdicts, p, "echantillon", _tentative_retenue(p, validations)) for p in ech}
    if any(v is None for v in premiers.values()):
        return None
    echecs = [p for p in ech if premiers[p]["motifs"]]
    return {"echantillon": ech, "echecs": echecs,
            "cibles_defectueuses": sum(v["cibles_defectueuses"] for v in premiers.values()),
            "cibles": sum(v["cibles"] for v in premiers.values())}


def papiers_d_audit(bilan: dict) -> list[str] | None:
    """Audit R4 (CL-3), calculé par le code : côté propre (aucun échec, aucune cible défectueuse), les 4 premiers
    papiers de l'échantillon ; côté sale (plus de 4 échecs), les 4 premiers papiers en échec, dans l'ordre de
    l'échantillon ; sinon, pas d'audit."""
    if not bilan["echecs"] and not bilan["cibles_defectueuses"]:
        return bilan["echantillon"][:TAILLE_AUDIT]
    if len(bilan["echecs"]) > SEUIL_ECHECS:
        return bilan["echecs"][:TAILLE_AUDIT]
    return None


def reprises_dues(racine: Path, run_id: str) -> list[str]:
    """Papiers dont la reprise (tentative 3) est due : premier avis « echantillon » ou « audit » en échec, ou
    « theory_only » contesté par l'avis « theorie ». Ne se calcule qu'une fois tous les avis requis lisibles (CL-12)."""
    rondes = _rondes(racine, run_id)
    bilan = bilan_echantillon(racine, run_id, rondes)
    if bilan is None:
        raise GardeArret("reprises : un papier de l'échantillon n'a pas encore d'avis lisible")
    if len(bilan["echecs"]) > SEUIL_ECHECS:
        raise GardeArret("reprises : seuil d'échecs dépassé, extraction à refaire sous une version 2")
    validations = _validations(racine, run_id)
    verdicts = verdicts_lisibles(rondes)
    audit = papiers_d_audit(bilan) or []
    th = _resultat(racine, run_id, "echantillon-contre-verification")["theory_only"]
    manquants = ([p for p in audit if _premier_verdict(verdicts, p, "audit", _tentative_retenue(p, validations))
                  is None]
                 + [p for p in th if _premier_verdict(verdicts, p, "theorie", _tentative_retenue(p, validations))
                    is None])
    if manquants:
        raise GardeArret(f"reprises : avis d'audit ou de vérification « theory_only » manquants : {manquants[:5]}")
    dus = set()
    for p in bilan["echantillon"] + th:
        k = _tentative_retenue(p, validations)
        if any(v is not None and v["motifs"]
               for v in (_premier_verdict(verdicts, p, r, k) for r in ("echantillon", "audit", "theorie"))):
            dus.add(p)
    return sorted(dus)


def preparer_contre_verification(racine: Path, run_id: str, travail: Path, role: str,
                                 papiers: list[str] | None = None, ch: Chemins = Chemins()) -> dict:
    """Prépare la ronde suivante (numéro calculé : 1 + rondes déjà préparées, CL-4). Rôles :
    - « echantillon » : l'échantillon tiré ;
    - « theorie » : les papiers exclus « theory_only » (vérification de chaque exclusion, CL-25) ;
    - « audit » : les papiers que désigne `papiers_d_audit` (CL-3) ;
    - « reprise » : les papiers de la tentative 3 valides et non « theory_only ».
    Une fois une ronde de ce rôle préparée, une ronde nouvelle ne porte que sur des papiers nommés, encore sans avis
    lisible de ce rôle (avis illisible refait, CL-2)."""
    racine = Path(racine)
    if role not in ROLES:
        raise GardeArret(f"rôle {role!r} inconnu ({ROLES})")
    m = _ouvrir_run(racine, run_id, ch, f"preparation-contre-verification ({role})")
    travail = _hors_depot(racine, Path(travail))
    if travail != Path(m["config"]["travail"]):
        raise GardeArret("dossier de travail différent de celui du manifeste")
    ech = _resultat(racine, run_id, "echantillon-contre-verification")
    validations = _validations(racine, run_id)
    n = 1
    while _diag(racine, run_id, f"preparation-contre-verification-ronde-{n}").exists():
        n += 1
    deja = [k for k in range(1, n)
            if _resultat(racine, run_id, f"preparation-contre-verification-ronde-{k}")["role"] == role]
    non_lues = [k for k in deja if not _diag(racine, run_id, f"contre-verification-ronde-{k}").exists()]
    if non_lues:
        raise GardeArret(f"ronde(s) « {role} » {non_lues} préparée(s) et non lue(s) : les lire d'abord")
    rondes = _rondes(racine, run_id) if role in ("audit", "reprise") else _rondes_lues(racine, run_id)
    if role == "echantillon":
        candidats = {p: _tentative_retenue(p, validations) for p in ech["echantillon"]}
    elif role == "theorie":
        candidats = {p: _tentative_retenue(p, validations) for p in ech["theory_only"]}
    elif role == "audit":
        bilan = bilan_echantillon(racine, run_id, rondes)
        audit = papiers_d_audit(bilan) if bilan is not None else None
        if not audit:
            raise GardeArret("audit non requis, ou échantillon sans avis lisible complet")
        candidats = {p: _tentative_retenue(p, validations) for p in audit}
    else:
        if 3 not in validations:
            raise GardeArret("reprise : tentative 3 non validée")
        candidats = {p: 3 for p, f in validations[3].items() if not f["anomalies"] and not f["theory_only"]}
    lisibles = verdicts_lisibles(rondes)
    sans_avis = {p: t for p, t in candidats.items() if _premier_verdict(lisibles, p, role, t) is None}
    if deja:
        if not papiers:
            raise GardeArret(f"une ronde « {role} » existe déjà : nommer les papiers sans avis lisible à refaire "
                             f"({sorted(sans_avis)[:8]})")
        hors = sorted(set(papiers) - set(sans_avis))
        if hors:
            raise GardeArret(f"papiers {hors[:5]} hors des papiers sans avis lisible de ce rôle")
        for pid in papiers:
            faits = sum(1 for k in deja if pid in _resultat(racine, run_id,
                                                            f"preparation-contre-verification-ronde-{k}")["papiers"])
            if faits >= AVIS_MAX_PAR_ROLE:
                _arreter(racine, run_id, f"arret-avis-refaits-{role}-{pid}", {
                    "role": role, "papier": pid, "avis_prepares": faits, "suite": "nœud, porté à Lazar"},
                    f"{pid} : {faits} avis « {role} » préparés sans avis lisible : arrêt, nœud")
        choisis = {p: sans_avis[p] for p in papiers}
    else:
        if papiers:
            raise GardeArret(f"première ronde « {role} » : elle porte sur tous ses papiers, sans choix")
        choisis = sans_avis
    if not choisis:
        raise GardeArret("aucun papier à contre-vérifier")
    base = travail / f"contre-verification-{n}"
    if base.exists():
        raise GardeArret(f"{base} existe déjà (R12)")
    par_id = {p["id"]: p for p in papiers_du_corpus(racine, ch)}
    modele = (racine / ch.dossier_procedure /
              FICHIERS_PROCEDURE["consigne_contre_verificateur"]).read_text(encoding="utf-8")
    fiches = {}
    for pid, k in sorted(choisis.items()):
        vk = _resultat(racine, run_id, f"validation-tentative-{k}")
        sorties = lire_archive(racine / "donnees" / run_id / f"sorties-tentative-{k}.tar", vk["archive_sorties_sha256"])
        a_verifier = {}
        for nom in ex.NOMS_SORTIES:
            octets = sorties[f"tentative-{k}/{pid}/{nom}.json"]
            if _sha(octets) != vk["papiers"][pid]["empreintes"][nom]:
                raise GardeArret(f"{pid} : sortie {nom}.json de l'archive ≠ empreinte validée")
            a_verifier[nom] = octets
        copie = ex.copie_de_lecture(lire_texte(racine, ch, par_id[pid]))
        fiche = _dossier_agent(racine, ch, copie, base / pid, modele, "verifier_avis", a_verifier)
        fiches[pid] = dict(fiche, tentative=k)
    resultat = {"ronde": n, "role": role, "travail": str(base), "papiers": fiches}
    _ecrire(racine, run_id, f"preparation-contre-verification-ronde-{n}", resultat)
    return resultat


def lire_contre_verification(racine: Path, run_id: str, ronde: int, retours: dict, ch: Chemins = Chemins()) -> dict:
    """Lecture d'une ronde : avis contrôlés (forme), motifs d'échec, archive scellée des avis (CL-11) ; une entrée
    modifiée rend l'avis illisible (CL-5). Pour la ronde « echantillon », le seuil d'échecs est contrôlé dès que
    l'échantillon est complet (CL-12), avec un résultat d'arrêt scellé (CL-16)."""
    racine = Path(racine)
    _ouvrir_run(racine, run_id, ch, f"contre-verification-ronde-{ronde}")
    prep = _resultat(racine, run_id, f"preparation-contre-verification-ronde-{ronde}")
    _exiger_retours(retours, list(prep["papiers"]))
    script = racine / ch.dossier_procedure / FICHIERS_PROCEDURE["verifier_avis"]
    fiches, details, membres = {}, {}, []
    for pid, info in sorted(prep["papiers"].items()):
        d = Path(info["dossier"])
        modifiees = _entrees_modifiees(d, info["entrees"])
        fiche = {"tentative": info["tentative"], "role": prep["role"], "avis_sha256": None,
                 "entrees_modifiees": modifiees}
        avis, anomalies = None, []
        # mêmes codes que le script pour un avis absent ou illisible (contre-lecture 2, D-11)
        if not (d / "avis.json").is_file():
            anomalies.append("[fichier.absent] avis.json absent")
        else:
            octets = (d / "avis.json").read_bytes()
            try:
                avis = json.loads(octets.decode("utf-8"), parse_constant=ex._refuser_constante)
                fiche["avis_sha256"] = _sha(octets)
                membres.append((f"contre-verification-{ronde}/{pid}/avis.json", octets))
            except ValueError as e:
                anomalies.append(f"[json.illisible] avis.json illisible : {e}")
        if not anomalies and not modifiees:       # avis jugé sur des entrées intactes seulement (contre-lecture 3, E-1)
            h9, h10, cibles = (json.loads((d / "a-verifier" / f"{n}.json").read_bytes()) for n in ex.NOMS_SORTIES)
            anomalies = ex.anomalies_avis(avis, h9, h10, cibles)
        if not modifiees:
            _accord_ou_arret(racine, run_id, f"contre-verification-ronde-{ronde}", pid, script, d,
                             [ex.code_anomalie(a) for a in anomalies])
        else:
            anomalies.append(f"[entrees.modifiees] entrées modifiées : {modifiees}")
        fiche["retour"] = retour_sans_texte(retours[pid], bool(anomalies))
        fiche["codes"] = [ex.code_anomalie(a) for a in anomalies]
        fiche["lisible"] = not anomalies
        if fiche["lisible"]:
            if prep["role"] == "theorie":
                fiche["motifs"] = [] if avis["theory_experiment_correct"] else ["theory_only contesté"]
            else:
                fiche["motifs"] = ex.motifs_echec_avis(avis, cibles, h10)
            fiche["cibles_defectueuses"] = sum(not (t["grounded"] and t["observable"]) for t in avis["targets"])
            fiche["cibles"] = len(avis["targets"])
            fiche["classification"] = {k: avis[k] for k in ("theory_experiment_correct", "data_type_correct",
                                                             "domains_reasonable")}
            fiche["compute_plausible"] = avis["compute_plausible"]
        fiches[pid] = fiche
        details[pid] = {"anomalies": anomalies, "avis": avis if _encodable(avis) else None,
                        "derniere_ligne": retours[pid]["derniere_ligne"]}
    sha_archive = archiver(racine / "donnees" / run_id / f"avis-ronde-{ronde}.tar", membres)
    sha_details = ecrire_donnees(racine, run_id, f"details-contre-verification-ronde-{ronde}", {"papiers": details})
    lisibles = [f for f in fiches.values() if f["lisible"]]
    resultat = {"ronde": ronde, "role": prep["role"], "papiers": fiches,
                "illisibles": sorted(p for p, f in fiches.items() if not f["lisible"]),
                "echecs": sorted(p for p, f in fiches.items() if f["lisible"] and f["motifs"]),
                "cibles_defectueuses": sum(f["cibles_defectueuses"] for f in lisibles),
                "cibles": sum(f["cibles"] for f in lisibles),
                "archive_avis_sha256": sha_archive, "details_sha256": sha_details}
    _ecrire(racine, run_id, f"contre-verification-ronde-{ronde}", resultat)
    if prep["role"] == "audit" and _diag(racine, run_id, "arret-seuil-contre-verification").exists():
        _accord_audit_cote_sale(racine, run_id)
    if prep["role"] == "echantillon":
        bilan = bilan_echantillon(racine, run_id, _rondes_lues(racine, run_id))
        if bilan is not None and len(bilan["echecs"]) > SEUIL_ECHECS:
            _ecrire(racine, run_id, "arret-seuil-contre-verification",
                    {"echecs": bilan["echecs"], "audit": papiers_d_audit(bilan),
                     "suite": "audit R4 sur ces papiers, puis extraction à refaire sous une version 2"})
            raise GardeArret(f"{len(bilan['echecs'])} papiers sur {TAILLE_ECHANTILLON} en échec (seuil "
                             f"{SEUIL_ECHECS}) : audit R4, puis extraction à refaire sous une version 2")
    return resultat


def accord_audit(racine: Path, run_id: str, rondes: list[dict], bilan: dict, cote: str) -> dict | None:
    """Accord des avis d'audit et des premiers avis de l'échantillon, sur les papiers d'audit (CL-3) ; None tant
    qu'un papier d'audit n'a pas d'avis d'audit lisible."""
    validations = _validations(racine, run_id)
    verdicts = verdicts_lisibles(rondes)
    papiers = papiers_d_audit(bilan) or []
    avis_audit = {p: _premier_verdict(verdicts, p, "audit", _tentative_retenue(p, validations)) for p in papiers}
    if not papiers or any(v is None for v in avis_audit.values()):
        return None
    premiers = {p: _premier_verdict(verdicts, p, "echantillon", _tentative_retenue(p, validations)) for p in papiers}
    return {"cote": cote, "papiers": papiers,
            "accord_echec": sum(bool(avis_audit[p]["motifs"]) == bool(premiers[p]["motifs"]) for p in papiers),
            "echecs_audit": sorted(p for p in papiers if avis_audit[p]["motifs"])}


def _accord_audit_cote_sale(racine: Path, run_id: str) -> None:
    """Côté sale (seuil d'échecs dépassé), l'accord de l'audit est écrit dès que l'audit est complet (contre-lecture 2,
    D-6), pour la version 2 de la procédure."""
    rondes = _rondes_lues(racine, run_id)
    bilan = bilan_echantillon(racine, run_id, rondes)
    accord = accord_audit(racine, run_id, rondes, bilan, "sale") if bilan is not None else None
    if accord is not None and not _diag(racine, run_id, "accord-audit-cote-sale").exists():
        _ecrire(racine, run_id, "accord-audit-cote-sale", accord)


# ------------------------------------------------------------------------------------------------ assemblage

def intervalle_binomial(k: int, n: int, niveau: float = 0.95) -> list[float]:
    """Intervalle exact (Clopper-Pearson) d'une proportion k/n."""
    from scipy.stats import beta

    a = (1 - niveau) / 2
    bas = 0.0 if k == 0 else float(beta.ppf(a, k, n - k + 1))
    haut = 1.0 if k == n else float(beta.ppf(1 - a, k + 1, n - k))
    return [bas, haut]


_LIGNE_TABLEAU = re.compile(r"^\s*[|+]")


def citations_de_tableau(cibles: dict, texte: str) -> tuple[int, int]:
    """Citations retrouvées seulement dans des lignes de tableau (CL-30) : (nombre, total)."""
    lignes = texte.split("\n")
    tableau = ex.normaliser("\n".join(ligne for ligne in lignes if _LIGNE_TABLEAU.match(ligne)))
    prose = ex.normaliser("\n".join(ligne for ligne in lignes if not _LIGNE_TABLEAU.match(ligne)))
    n = total = 0
    for f in ex.FAMILLES_CIBLES:
        for it in cibles[f]:
            c = ex.normaliser(str(it["evidence"]))
            total += 1
            n += int(c in tableau and c not in prose)
    return n, total


def assembler(racine: Path, run_id: str, ch: Chemins = Chemins()) -> dict:
    racine = Path(racine)
    m = _ouvrir_run(racine, run_id, ch, "assemblage")
    pilote, reserve = m["config"]["pilote"], m["config"]["reserve"]
    validations = _validations(racine, run_id)
    rondes = _rondes(racine, run_id)
    bilan_ech = bilan_echantillon(racine, run_id, rondes)
    if bilan_ech is None:
        raise GardeArret("assemblage : un papier de l'échantillon n'a pas d'avis lisible")
    if len(bilan_ech["echecs"]) > SEUIL_ECHECS:
        raise GardeArret("assemblage : seuil d'échecs dépassé, extraction à refaire sous une version 2")
    verdicts = verdicts_lisibles(rondes)
    audit = None
    if papiers_d_audit(bilan_ech):
        audit = accord_audit(racine, run_id, rondes, bilan_ech, "propre")
        if audit is None:
            raise GardeArret("assemblage : audit R4 requis et incomplet")
        audit["reserve"] = "audit R4 déclenché (aucun échec, aucune cible défectueuse) : portée à Lazar"
    statuts = {pid: ex.statut_papier(pid, validations, verdicts.get(pid, [])) for pid in pilote + reserve}
    try:
        listes = ex.listes_de_taches(pilote, reserve, statuts)
    except GardeArret as e:
        _ecrire(racine, run_id, "arret-assemblage", {"motif": str(e), "statuts": statuts})
        raise
    par_id = {p["id"]: p for p in papiers_du_corpus(racine, ch)}
    archives = {k: lire_archive(racine / "donnees" / run_id / f"sorties-tentative-{k}.tar",
                                _resultat(racine, run_id, f"validation-tentative-{k}")["archive_sorties_sha256"])
                for k in validations}
    compte = {liste: {"reference_nulle": 0, "base": {"reported": 0, "estimated": 0}, "citations_tableau": 0,
                      "citations": 0} for liste in ("evaluation", "entrainement")}     # par liste (contre-lecture 3, E-11)

    def tache(pid: str, liste: str) -> dict:
        k = statuts[pid]["tentative"]
        sorties = {}
        for nom in ex.NOMS_SORTIES:
            octets = archives[k][f"tentative-{k}/{pid}/{nom}.json"]
            if _sha(octets) != validations[k][pid]["empreintes"][nom]:
                raise GardeArret(f"{pid} : sortie {nom}.json de l'archive ≠ empreinte validée")
            sorties[nom] = json.loads(octets)
        texte = lire_texte(racine, ch, par_id[pid])
        t = ex.assembler_tache(pid, sorties["h9"], sorties["h10"], sorties["cibles"], texte)
        calcul = sorties["cibles"]["compute"]
        if calcul.get("reference_gpu_hours") is None:
            compte[liste]["reference_nulle"] += 1
        else:                                   # bases comptées sur les seules références non nulles (D-7)
            compte[liste]["base"][calcul["basis"]] += 1
        n, total = citations_de_tableau(sorties["cibles"], texte)
        compte[liste]["citations_tableau"] += n
        compte[liste]["citations"] += total
        return dict(t, tentative=k, empreintes=validations[k][pid]["empreintes"])

    evaluation = [tache(p, "evaluation") for p in listes["evaluation"]]
    entrainement = [tache(p, "entrainement") for p in listes["entrainement"]]
    sha_eval = ecrire_donnees(racine, run_id, "taches-evaluation",
                              {"taches": evaluation, "remplacements": listes["remplacements"]})
    sha_entr = ecrire_donnees(racine, run_id, "taches-entrainement",
                              {"taches": entrainement, "insuffisant": listes["entrainement_insuffisant"]})
    classification: dict[str, dict] = {}       # par rôle (D-7)
    for r in rondes:
        if r["role"] == "theorie":
            continue
        c = classification.setdefault(r["role"], {"avis": 0, "desaccords_type_papier": 0,
                                                  "desaccords_type_donnees": 0, "domaines_discutables": 0,
                                                  "calcul_non_plausible": 0})
        for f in r["papiers"].values():
            if f["lisible"]:
                c["avis"] += 1
                c["desaccords_type_papier"] += int(not f["classification"]["theory_experiment_correct"])
                c["desaccords_type_donnees"] += int(not f["classification"]["data_type_correct"])
                c["domaines_discutables"] += int(not f["classification"]["domains_reasonable"])
                c["calcul_non_plausible"] += int(not f["compute_plausible"])
    alertes = {str(k): sum(bool(f["alertes"]) for f in v.values()) for k, v in validations.items()}
    # annonces des sous-agents contraires au module, ou hors forme, par tentative et par rôle (R4 ; E-11)
    annonces = {f"tentative-{k}": _compte_annonces(v.values()) for k, v in validations.items()}
    for r in rondes:
        c = annonces.setdefault(f"ronde-{r['role']}", {"desaccords": 0, "hors_format": 0})
        for cle, n in _compte_annonces(r["papiers"].values()).items():
            c[cle] += n
    k_ech = len(bilan_ech["echecs"])
    bilan = {"statuts": statuts, "evaluation": listes["evaluation"], "entrainement": listes["entrainement"],
             "remplacements": listes["remplacements"], "entrainement_insuffisant": listes["entrainement_insuffisant"],
             "echantillon": bilan_ech["echantillon"], "echecs_echantillon": bilan_ech["echecs"],
             "taux_echec_echantillon": {"echecs": k_ech, "papiers": TAILLE_ECHANTILLON,
                                        "intervalle_95": intervalle_binomial(k_ech, TAILLE_ECHANTILLON)},
             "cibles_defectueuses_echantillon": {"defectueuses": bilan_ech["cibles_defectueuses"],
                                                 "controlees": bilan_ech["cibles"]}, "audit": audit,
             "classification_et_calcul": classification, "alertes_lexicales_par_tentative": alertes,
             "annonces_des_sous_agents": annonces,
             "taches_assemblees": compte,
             "exclus": {p: s["motif"] for p, s in statuts.items() if s["statut"] == "exclu"},
             "taches_evaluation_sha256": sha_eval, "taches_entrainement_sha256": sha_entr}
    _ecrire(racine, run_id, "bilan-extraction", bilan)
    return bilan


def _compte_annonces(fiches) -> dict:
    fiches = list(fiches)
    return {"desaccords": sum(f["retour"]["accord_avec_le_module"] is False for f in fiches),
            "hors_format": sum(f["retour"]["forme"] != "conforme" for f in fiches)}


# ------------------------------------------------------------------------------------------------ ligne de commande

def _liste(v: str | None) -> list[str] | None:
    return [x.strip() for x in v.split(",") if x.strip()] if v else None


def _retours(racine: Path, run_id: str, chemin: str) -> dict:
    """Fichier des retours, écrit par la session dans `donnees/<run>/` et nulle part ailleurs : ses lignes brutes peuvent
    porter du texte des papiers (contre-lecture 3, E-10)."""
    p = Path(chemin).resolve()
    if p.parent != (Path(racine) / "donnees" / run_id).resolve():
        raise GardeArret(f"fichier de retours {chemin} hors de donnees/{run_id}/")
    return json.loads(p.read_text(encoding="utf-8"))


def _main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog="python -m controle_ia.environnements.extraire_t05")
    sous = ap.add_subparsers(dest="commande", required=True)
    s = sous.add_parser("preparer")
    s.add_argument("--run-id", required=True)
    s.add_argument("--travail", required=True)
    s.add_argument("--tentative", type=int, required=True)
    s.add_argument("--papiers")
    s = sous.add_parser("valider")
    s.add_argument("--run-id", required=True)
    s.add_argument("--tentative", type=int, required=True)
    s.add_argument("--retours", required=True)
    s = sous.add_parser("echantillonner")
    s.add_argument("--run-id", required=True)
    s = sous.add_parser("preparer-contre-verification")
    s.add_argument("--run-id", required=True)
    s.add_argument("--travail", required=True)
    s.add_argument("--role", required=True, choices=ROLES)
    s.add_argument("--papiers")
    s = sous.add_parser("lire-contre-verification")
    s.add_argument("--run-id", required=True)
    s.add_argument("--ronde", type=int, required=True)
    s.add_argument("--retours", required=True)
    s = sous.add_parser("assembler")
    s.add_argument("--run-id", required=True)
    s = sous.add_parser("controler")
    s.add_argument("--run-id", required=True)
    a = ap.parse_args(argv)
    racine = Path(".")
    if a.commande == "preparer":
        r = preparer(racine, a.run_id, Path(a.travail), a.tentative, _liste(a.papiers),
                     commande="python -m controle_ia.environnements.extraire_t05 " + " ".join(argv))
        print(json.dumps({"tentative": r["tentative"], "papiers": len(r["papiers"]), "travail": r["travail"]},
                         ensure_ascii=False))
    elif a.commande == "valider":
        r = valider(racine, a.run_id, a.tentative, _retours(racine, a.run_id, a.retours))
        print(json.dumps({k: r[k] for k in ("tentative", "invalides", "theory_only", "avec_alertes")},
                         ensure_ascii=False))
    elif a.commande == "echantillonner":
        r = echantillonner(racine, a.run_id)
        print(json.dumps({"echantillon": r["echantillon"], "theory_only": r["theory_only"]}, ensure_ascii=False))
    elif a.commande == "preparer-contre-verification":
        r = preparer_contre_verification(racine, a.run_id, Path(a.travail), a.role, _liste(a.papiers))
        print(json.dumps({"ronde": r["ronde"], "role": r["role"], "papiers": sorted(r["papiers"])}, ensure_ascii=False))
    elif a.commande == "lire-contre-verification":
        r = lire_contre_verification(racine, a.run_id, a.ronde, _retours(racine, a.run_id, a.retours))
        print(json.dumps({k: r[k] for k in ("ronde", "role", "illisibles", "echecs", "cibles_defectueuses", "cibles")},
                         ensure_ascii=False))
    elif a.commande == "controler":         # règle de perte rejouée, juste avant la copie de N-014 (V-10)
        _ouvrir_run(racine, a.run_id, Chemins(), "contrôle avant copie")
        print(json.dumps({"fichiers_consignes": fichiers_consignes(racine, a.run_id)}, ensure_ascii=False, indent=1))
    else:
        r = assembler(racine, a.run_id)
        print(json.dumps({"evaluation": len(r["evaluation"]), "entrainement": len(r["entrainement"]),
                          "remplacements": r["remplacements"], "exclus": r["exclus"],
                          "echecs_echantillon": r["echecs_echantillon"], "audit": r["audit"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
