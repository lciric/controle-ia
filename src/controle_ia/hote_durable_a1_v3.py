#!/usr/bin/env python3
"""Hôte durable de la troisième course d'A1-v3 (GO-2026-11-04-06), v1.

Deux parties, un seul fichier, bibliothèque standard seulement (il tourne aussi sur la machine louée, avant toute
installation) :

- `louer` (dans la session qui lance, la fille) : vérifie le GO par la garde de `main` (règle d'extension comprise) et le
  montant, contrôle l'offre de Vast choisie (aucune carte, prix horaire au plus le plafond écrit, fiabilité), puis crée la
  machine par l'outil `vastai` (forme des amorces antérieures du dépôt : `--env`, `--entrypoint bash --args -c`), les secrets
  dans les arguments d'un sous-processus, jamais affichés (toute sortie de l'outil filtrée), et écrit l'identifiant de la machine
  au journal local. Rien d'autre ne se fait de la session : la course ne dépend plus d'elle.
- `hote` (sur la machine, lancé par l'amorce `scripts/amorce_hote_durable_a1_v3_v1.sh`) : revérifie le GO sur `main`,
  copie le registre des GO de la source que fixe le texte v3, extrait les pièces gelées et vérifie leurs empreintes, clone le
  dépôt public au commit qui porte le texte scellé v3, vérifie l'empreinte du texte et l'ascendance du code gelé, lance le
  relais Argon 8805 neuf (la seule clé d'Argon dans son seul environnement), `--verifier-seulement` (code 0 exigé), puis la
  course détachée ; garde sans session (relevé daté chaque minute, relance du relais seulement, plafond de durée et de
  dépense de la machine) ; à la fin du lanceur, quel qu'en soit le code : relais arrêté par son identifiant, liste
  d'empreintes, contrôle des secrets, versement sur une branche de données neuve, poussée vérifiée, puis destruction de la
  machine par son identifiant (arrêt seulement, sans destruction, si la poussée n'est pas vérifiée).
- `inventaire` : instances du compte, champs filtrés (jamais l'environnement des machines, qui porte la clé).

Une reprise du conteneur par l'hôte (redémarrage) ne relance jamais rien (R12) : l'état est scellé tel quel, versé sur une
branche « …-interrompue-v1 », puis la machine est détruite.

Mode jouet (`--jouet`) : aucune location, aucun appel de modèle, aucun réseau ; Vast est simulé par un fichier, les dépôts sont
des dépôts locaux, le relais et le lanceur sont ceux que l'essai fournit ; mêmes gardes, mêmes chemins de code.
"""
from __future__ import annotations

import argparse
import base64
import dataclasses
import datetime as dt
import hashlib
import importlib.util
import io
import json
import os
import re
import shutil
import signal
import socket
import subprocess
import sys
import tarfile
import time
import urllib.error
import urllib.request
from contextlib import redirect_stderr
from pathlib import Path

VERSION = "hote-durable-a1-v3-v1"
GO_ATTENDU = "GO-2026-11-04-06"
PLAFOND_COURSE_USD = 400.0  # plafond_usd du bloc plan-gele, égal au montant du GO (le lanceur exige l'égalité exacte)
COMMIT_CODE_GELE = "9776ed0efee97146182ff2c4b409e5ec224a0bbf"
NOM_TEXTE = "orchestrator/prereg/preenregistrement-attaque-goodhart-v3-v3.md"
DEPOT_PUBLIC = "https://github.com/lciric/ideation-organism.git"
DEPOT_PRIVE = "https://github.com/lciric/controle-ia-travail.git"  # jamais lciric/controle-ia (copie expurgée publique)
BRANCHE_DONNEES = "donnees/attaque-goodhart-v3-a1v3-troisieme-v1"
BRANCHE_INTERROMPUE = "donnees/attaque-goodhart-v3-a1v3-troisieme-interrompue-v1"
BRANCHE_REFUS = "donnees/attaque-goodhart-v3-a1v3-troisieme-refus-v1"  # refus d'une garde avant la course : rien dépensé
# Pièces gelées (texte scellé v2, section 4 ; ordre de la fille v1, § 2) : réf. de la branche privée, chemin, empreinte.
REF_SOURCES = "donnees/recuperation-collisionneur-v8-v1"
REF_CONFIGURATION = "canal/session-depot-reprise-n120"
SOURCE_REGISTRE = "canal/conv-audit-n04"  # source du registre passé au lanceur (texte v3, section 4 ; comme la v2)
CHEMIN_CONF_DANS_REF = ("brouillons/canal-reprise-releve-v1/envois/session-depot/conf-a1-v3/"
                        "configuration-mini-course-kimi-argon-v3.json")
NUIT = "donnees/mini-course-kimi-argon-v1/orchestrateur/nuit"
EMPREINTES_GELEES = {
    f"{NUIT}/configuration-mini-course-kimi-argon-v3.json":
        "e5306c47e1b21a5e55b599411dba92c97e88aa98bb6d6fa91fc5d358a2bdde30",
    f"{NUIT}/commande_argon_v56_nuit_v2.py": "221df610681ed47bf66fbfef21d583006aa3e09a3147e22227faacd98622b851",
    f"{NUIT}/registre_depense_cumulee_v1.py": "8ba92066b358ffb8206dea9e70251388c30620484fab1ac578778d9f21e578ff",
    "donnees/espece-seule-v1/collisionneur_v7.py": "c9725f025407c3ece3e8c16d19cfdfdec078f084a811f0a3b6ea3209be5d98dc",
}
RACINE_SOURCES = "/home/user/controle-ia-travail"  # chemins absolus écrits dans la configuration gelée
# Relais : mêmes réglages que les deux premières courses (ordre de la fille v1, § 4).
PORT_RELAIS = 8805
PLAFOND_RELAIS_USD = 410
MAX_APPELS_RELAIS = 9000
# Machine : plafonds écrits (texte v3, section 8, « Troisième course »).
PRIX_MAX_H_USD = 0.40       # prix horaire total (dph_total) au plus
DUREE_MAX_MACHINE_H = 80.0  # au-delà de la garde de 72 h du lanceur : n'agit que si le lanceur ne s'arrête pas lui-même
PLAFOND_MACHINE_USD = 32.0  # = 0,40 × 80
PERIODE_GARDE_S = 60
DELAI_CLE_ARGON = "CLE_ARGON"  # nom de la variable qui porte la clé jusqu'à la machine (jamais GEMINI_API_KEY : R-1059)
SECRETS = ("CLE_ARGON", "GH_TOKEN", "CONTAINER_API_KEY")
API_VAST = "https://console.vast.ai/api/v0"
# Filtre d'offre « sans carte » (texte v3, section 8) ; la valeur de chaque champ est lue dans la réponse brute de Vast.
OFFRE_MIN = {"cpu_cores_effective": 4, "cpu_ram": 8000, "disk_space": 30, "reliability": 0.98}
IMAGE = "python:3.13-bookworm"  # image complète (git présent), comme les amorces antérieures (python:3.11-bookworm)
NUMPY = "numpy==2.5.3"
IDENT = re.compile(r"^[0-9]{1,12}$")
LIGNE_GO = re.compile(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2})\s*\|")
MONTANT = re.compile(r"^\s*(\d+(?:[.,]\d+)?)\s*USD\s*$")


class Refus(Exception):
    """Garde qui refuse : rien ne part (ou, sur la machine, on passe à la fin propre)."""


def maintenant() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_fichier(chemin) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def sha256_octets(o: bytes) -> str:
    return hashlib.sha256(o).hexdigest()


class Journal:
    """Journal daté (heure UTC). Toute ligne passe par `masquer` : une valeur de secret n'y entre jamais."""

    def __init__(self, chemin: Path, secrets: dict[str, str] | None = None):
        self.chemin = Path(chemin)
        self.secrets = {k: v for k, v in (secrets or {}).items() if v}
        self.chemin.parent.mkdir(parents=True, exist_ok=True)

    def masquer(self, texte: str) -> str:
        for nom, valeur in self.secrets.items():
            if valeur and valeur in texte:
                texte = texte.replace(valeur, f"[{nom} masquée]")
        return texte

    def ecrire(self, texte: str) -> None:
        ligne = self.masquer(f"{maintenant()} {texte}")
        with open(self.chemin, "a", encoding="utf-8") as f:
            f.write(ligne + "\n")
        print(ligne, flush=True)


# --- GO : garde de `main` (règle d'extension R-389) et montant ------------------------------------------------------------


def charger_garde(chemin_garde: Path, chemin_registre: Path):
    """Charge `.claude/hooks/garde_calcul.py` du commit lu et le fait lire le registre donné (même règle que `main`)."""
    spec = importlib.util.spec_from_file_location("garde_calcul_main", chemin_garde)
    if spec is None or spec.loader is None:
        raise Refus(f"garde illisible : {chemin_garde}")
    module = importlib.util.module_from_spec(spec)
    avant, sys.dont_write_bytecode = sys.dont_write_bytecode, True  # aucun __pycache__ à côté de la copie versée
    try:
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = avant
    module.REGISTRE_GO = Path(chemin_registre)
    return module


def lignes_du_go(chemin_registre: Path, go_id: str) -> list[list[str]]:
    lignes = []
    for ligne in Path(chemin_registre).read_text(encoding="utf-8").splitlines():
        m = LIGNE_GO.match(ligne)
        if m and m.group(1) == go_id:
            lignes.append([c.strip() for c in ligne.strip().strip("|").split("|")])
    return lignes


def verifier_go(chemin_registre: Path, chemin_garde: Path, go_id: str, plafond_usd: float,
                aujourd_hui: dt.date) -> dict:
    """GO de calcul valide selon la garde de `main` (type, Lazar, validité, révocation, extensions), montant exact.

    La garde est appelée telle quelle (`decider`) sur une commande de lancement qui cite le GO : son refus (sortie 2, motif
    sur la sortie d'erreur) devient un `Refus` avec le même motif. Montant : la cellule « plafond » de la première ligne et de
    chaque extension doit valoir exactement `plafond_usd` USD (une extension qui change le plafond demande un texte neuf).
    """
    if go_id != GO_ATTENDU:
        raise Refus(f"GO {go_id} : le texte v3 nomme {GO_ATTENDU} (aucun autre GO)")
    garde = charger_garde(chemin_garde, chemin_registre)
    tampon = io.StringIO()
    try:
        with redirect_stderr(tampon):
            garde.decider(f"GO_ID={go_id} vastai create instance 0", aujourd_hui)
    except SystemExit as e:
        if e.code not in (0, None):
            raise Refus(f"garde de main : {tampon.getvalue().strip()}") from None
    lignes = lignes_du_go(chemin_registre, go_id)
    if not lignes:  # la garde l'a déjà refusé ; garde redondante, jamais un repli silencieux (R5)
        raise Refus(f"{go_id} absent du registre")
    for cellules in lignes:
        m = MONTANT.match(cellules[4])
        if not m or abs(float(m.group(1).replace(",", ".")) - plafond_usd) > 1e-9:
            raise Refus(f"{go_id} : plafond « {cellules[4]} » au lieu de exactement {plafond_usd:g} USD")
    return {"go": go_id, "lignes": len(lignes), "extensions": len(lignes) - 1, "plafond_usd": plafond_usd,
            "registre_sha256": sha256_fichier(chemin_registre), "accorde": lignes[0][1], "echeance": lignes[0][5]}


def doublons_lecteur_du_lanceur(chemin_registre: Path) -> list[str]:
    """Identifiants en double : le lecteur du lanceur (`pole/configuration_v53.py:258-281`) refuse tout doublon."""
    vus, doubles = set(), []
    for ligne in Path(chemin_registre).read_text(encoding="utf-8").splitlines():
        m = LIGNE_GO.match(ligne)
        if m:
            if m.group(1) in vus:
                doubles.append(m.group(1))
            vus.add(m.group(1))
    return sorted(set(doubles))


# --- Offre et location -----------------------------------------------------------------------------------------------------


def verifier_offre(offres: list[dict], offre_id: int, prix_max_h: float = PRIX_MAX_H_USD) -> dict:
    """L'offre choisie, prise dans la réponse brute de la recherche : aucune carte, prix ≤ plafond, minima tenus."""
    choisies = [o for o in offres if o.get("id") == offre_id]
    if len(choisies) != 1:
        raise Refus(f"offre {offre_id} : {len(choisies)} dans la réponse de la recherche (une exigée)")
    o = choisies[0]
    if o.get("num_gpus") != 0:
        raise Refus(f"offre {offre_id} : {o.get('num_gpus')!r} carte(s) ; machine sans carte exigée (GO-2026-11-04-06)")
    prix = o.get("dph_total")
    if not isinstance(prix, (int, float)) or isinstance(prix, bool) or not (0 < prix <= prix_max_h):
        raise Refus(f"offre {offre_id} : prix horaire {prix!r} hors de ]0 ; {prix_max_h}] USD")
    for champ, mini in OFFRE_MIN.items():
        v = o.get(champ)
        if not isinstance(v, (int, float)) or isinstance(v, bool) or v < mini:
            raise Refus(f"offre {offre_id} : {champ} = {v!r} < {mini}")
    return {"id": offre_id, "dph_total": float(prix), **{k: o.get(k) for k in OFFRE_MIN},
            "geolocation": o.get("geolocation"), "machine_id": o.get("machine_id")}


class ClientVastCli:
    """Côté session : l'outil `vastai` (sa clé est dans sa propre configuration), comme les amorces antérieures du dépôt.

    Les secrets passent par `--env` (forme éprouvée du dépôt) dans les arguments d'un sous-processus, jamais affichés : toute
    sortie de l'outil est filtrée (valeurs des secrets masquées) avant d'être lue ou écrite."""

    def __init__(self, outil: str = "vastai"):
        self.outil = outil

    def _lancer(self, args: list[str], secrets: dict[str, str]) -> str:
        r = lancer([self.outil, *args], delai=300)
        texte = (r.stdout + r.stderr).decode("utf-8", "replace")
        for nom, v in secrets.items():
            if v:
                texte = texte.replace(v, f"[{nom} masquée]")
        if r.returncode != 0:
            raise Refus(f"vastai {args[0]} {args[1] if len(args) > 1 else ''} : code {r.returncode} : {texte[-300:]}")
        return texte

    def creer(self, offre_id: int, corps: dict) -> int:
        env = " ".join(f"-e {k}={v}" for k, v in corps["env"].items())
        if any(c.isspace() or c in "\"'" for v in corps["env"].values() for c in v):
            raise Refus("valeur d'environnement avec espace ou guillemet : refus (forme -e K=V)")
        args = ["create", "instance", str(offre_id), "--raw", "--image", corps["image"], "--disk", str(corps["disk"]),
                "--cancel-unavail", "--label", corps["label"], "--env", env, "--entrypoint", "bash", "--args", "-c",
                corps["script"]]
        texte = self._lancer(args, {k: corps["env"][k] for k in ("CLE_ARGON", "GH_TOKEN")})
        rep = None
        for ligne in reversed(texte.strip().splitlines()):
            try:
                rep = json.loads(ligne)
                break
            except ValueError:
                continue
        if not isinstance(rep, dict):
            raise Refus("réponse de création illisible : vérifier par l'inventaire avant toute nouvelle location")
        ident = rep.get("new_contract")
        if not rep.get("success") or not isinstance(ident, int):
            raise Refus(f"création refusée par Vast (succès {rep.get('success')!r})")
        return ident

    def instances(self) -> list[dict]:
        return json.loads(self._lancer(["show", "instances", "--raw"], {}))


class ClientVast:
    """Côté machine : interface REST de Vast, avec la clé d'instance (`CONTAINER_API_KEY`) ; jamais affichée."""

    def __init__(self, cle: str | None = None):
        if cle is None:
            cle = os.environ.get("VAST_API_KEY")
            if not cle:
                for p in (Path.home() / ".vast_api_key", Path.home() / ".config/vastai/vast_api_key"):
                    if p.is_file():
                        cle = p.read_text().strip()
                        break
        if not cle:
            raise Refus("clé de l'interface de Vast absente (VAST_API_KEY ou ~/.vast_api_key)")
        self._cle = cle

    def _requete(self, methode: str, chemin: str, corps: dict | None = None) -> dict:
        donnees = None if corps is None else json.dumps(corps).encode("utf-8")
        r = urllib.request.Request(f"{API_VAST}{chemin}", data=donnees, method=methode,
                                   headers={"Authorization": f"Bearer {self._cle}", "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(r, timeout=60) as rep:
                return json.loads(rep.read().decode("utf-8") or "{}")
        except urllib.error.HTTPError as e:  # le corps d'erreur ne contient pas nos secrets ; on n'en garde que le code
            raise Refus(f"Vast {methode} {chemin} : HTTP {e.code}") from None

    def creer(self, offre_id: int, corps: dict) -> int:
        rep = self._requete("PUT", f"/asks/{offre_id}/", corps)
        ident = rep.get("new_contract")
        if not rep.get("success") or not isinstance(ident, int):
            raise Refus(f"création refusée par Vast (succès {rep.get('success')!r})")
        return ident

    def instances(self) -> list[dict]:
        return self._requete("GET", "/instances/").get("instances", [])

    def detruire(self, ident: int) -> None:
        self._requete("DELETE", f"/instances/{ident}/")

    def arreter(self, ident: int) -> None:
        self._requete("PUT", f"/instances/{ident}/", {"state": "stopped"})


class ClientVastJouet:
    """Vast simulé dans un fichier JSON (mode jouet) : aucune location, aucun réseau."""

    def __init__(self, chemin: Path):
        self.chemin = Path(chemin)
        if not self.chemin.exists():
            self._ecrire({"instances": [], "gestes": []})

    def _lire(self):
        return json.loads(self.chemin.read_text())

    def _ecrire(self, e):
        self.chemin.write_text(json.dumps(e, ensure_ascii=False, indent=1))

    def creer(self, offre_id, corps):
        e = self._lire()
        ident = 90000000 + len(e["instances"]) + 1
        e["instances"].append({"id": ident, "offre": offre_id, "label": corps.get("label"), "etat": "running",
                               "env": sorted(corps.get("env", {}))})  # noms seulement : le jouet ne garde aucune valeur
        e["gestes"].append(["creer", ident])
        self._ecrire(e)
        return ident

    def instances(self):
        return self._lire()["instances"]

    def detruire(self, ident):
        e = self._lire()
        e["gestes"].append(["detruire", ident])
        e["instances"] = [i for i in e["instances"] if i["id"] != ident]
        self._ecrire(e)

    def arreter(self, ident):
        e = self._lire()
        e["gestes"].append(["arreter", ident])
        for i in e["instances"]:
            if i["id"] == ident:
                i["etat"] = "stopped"
        self._ecrire(e)


def champs_filtres(instance: dict) -> dict:
    """Inventaire sans fuite : jamais `extra_env`, `onstart`, ni rien qui porte l'environnement de la machine."""
    garder = ("id", "label", "actual_status", "cur_state", "intended_status", "dph_total", "num_gpus", "start_date",
              "etat", "offre")
    return {k: instance.get(k) for k in garder if k in instance}


def script_de_demarrage(commit_prive: str) -> str:
    """Processus principal du conteneur (`--entrypoint bash --args -c …`, forme des amorces du dépôt) : clone le dépôt privé au
    commit, puis l'amorce au premier plan ; au redémarrage du conteneur, le clone existe : l'amorce seule (qui ne relance rien)."""
    if not re.fullmatch(r"[0-9a-f]{40}", commit_prive):
        raise Refus("commit du dépôt privé : hash complet de 40 caractères exigé")
    return ("set -u; cd /root; "
            "if [ ! -d /root/amorce-depot/.git ]; then "
            "(command -v git >/dev/null || (apt-get update -qq && apt-get install -y -qq git ca-certificates >/dev/null)); "
            "A='!f() { echo username=x-access-token; echo \"password=${GH_TOKEN}\"; }; f'; "
            "git -c credential.helper=\"$A\" clone -q \"$DEPOT_URL\" /root/amorce-depot && "
            f"git -C /root/amorce-depot checkout -q --detach {commit_prive}; fi; "
            "bash /root/amorce-depot/scripts/amorce_hote_durable_a1_v3_v1.sh 2>&1 | tee -a /root/amorce-a1v3.log")


def corps_de_creation(commit_prive: str, commit_public: str, sha_texte: str, commit_registre: str,
                      offre: dict, secrets: dict[str, str]) -> dict:
    for nom, motif in (("commit_public", r"[0-9a-f]{40}"), ("sha_texte", r"[0-9a-f]{64}"),
                       ("commit_registre", r"[0-9a-f]{40}")):
        if not re.fullmatch(motif, locals()[nom]):
            raise Refus(f"{nom} : forme exacte exigée ({motif})")
    manquants = [k for k in ("CLE_ARGON", "GH_TOKEN") if not secrets.get(k)]
    if manquants:
        raise Refus(f"secrets absents de l'environnement : {', '.join(manquants)}")
    env = {"COMMIT_PRIVE": commit_prive, "COMMIT_PUBLIC": commit_public, "SHA_TEXTE": sha_texte,
           "COMMIT_REGISTRE": commit_registre, "GO_ID": GO_ATTENDU, "PRIX_H_USD": f"{offre['dph_total']:.6f}",
           "DEPOT_URL": DEPOT_PRIVE, "CLE_ARGON": secrets["CLE_ARGON"], "GH_TOKEN": secrets["GH_TOKEN"]}
    b64 = base64.b64encode(script_de_demarrage(commit_prive).encode("utf-8")).decode("ascii")
    return {"image": IMAGE, "disk": 30, "label": "a1-v3-troisieme-v1", "env": env,
            "script": f"echo {b64} | base64 -d > /root/demarrage-a1v3.sh && bash /root/demarrage-a1v3.sh"}


def louer(a, client=None, aujourd_hui=None) -> int:
    """Partie session : garde GO, garde d'offre, création ; écrit l'identifiant de la machine. Rend 0, ou 2 (refus)."""
    t = Path(a.journal_local)
    j = Journal(t, {k: os.environ.get(k, "") for k in SECRETS + ("VAST_API_KEY",)})
    try:
        aujourd_hui = aujourd_hui or dt.datetime.now(dt.timezone.utc).date()
        g = verifier_go(Path(a.registre_main), Path(a.garde_main), a.go, PLAFOND_COURSE_USD, aujourd_hui)
        j.ecrire(f"GO {g['go']} accepté par la garde de main : {g['lignes']} ligne(s), plafond {g['plafond_usd']:g} USD, "
                 f"registre {g['registre_sha256']}")
        offres = json.loads(Path(a.offres).read_text())
        offres = offres.get("offers", offres) if isinstance(offres, dict) else offres
        o = verifier_offre(offres, int(a.offre), PRIX_MAX_H_USD)
        j.ecrire(f"offre {o['id']} retenue : {o['dph_total']} USD/h ≤ {PRIX_MAX_H_USD} ; sans carte ; "
                 f"plafond machine {PLAFOND_MACHINE_USD} USD, {DUREE_MAX_MACHINE_H} h")
        secrets = {k: os.environ.get(k, "") for k in ("CLE_ARGON", "GH_TOKEN")}
        corps = corps_de_creation(a.commit_prive, a.commit_public, a.sha_texte, a.commit_registre, o, secrets)
        if a.verifier_seulement:
            j.ecrire("vérification seulement : rien créé (variables portées : " + ", ".join(sorted(corps["env"])) + ")")
            return 0
        client = client or ClientVastCli()
        ident = client.creer(o["id"], corps)
        j.ecrire(f"machine créée : identifiant {ident} (offre {o['id']}, {o['dph_total']} USD/h)")
        Path(str(t) + ".identifiant").write_text(f"{ident}\n")
        return 0
    except (Refus, OSError, ValueError, KeyError) as e:
        j.ecrire(f"REFUS : {e}")
        return 2


# --- Partie machine ------------------------------------------------------------------------------------------------------


@dataclasses.dataclass
class Reglages:
    """Tout ce qui diffère entre la vraie machine et le jouet ; défauts = valeurs écrites par le texte v3."""

    travail: Path = Path("/root/a1-v3-troisieme-v1")
    clone_prive: Path = Path("/root/amorce-depot")
    clone_public: Path = Path("/root/ideation-organism")
    depot_public: str = DEPOT_PUBLIC
    racine_sources: Path = Path(RACINE_SOURCES)
    empreintes: dict = dataclasses.field(default_factory=lambda: dict(EMPREINTES_GELEES))
    commit_code_gele: str = COMMIT_CODE_GELE
    python_relais: str = "/usr/bin/python3"
    python_course: str = "python3"
    port: int = PORT_RELAIS
    periode_s: float = PERIODE_GARDE_S
    duree_max_s: float = DUREE_MAX_MACHINE_H * 3600
    plafond_machine_usd: float = PLAFOND_MACHINE_USD
    attente_relais_s: float = 60.0
    essais_poussee: int = 6
    attente_poussee_s: float = 60.0
    jouet: bool = False
    vast_jouet: Path | None = None
    aujourd_hui: dt.date | None = None


def lancer(cmd, cwd=None, env=None, entree=None, delai=900) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, env=env, input=entree, capture_output=True, timeout=delai)


def git(*args, cwd=None, gh_token="", delai=900) -> str:
    aide = ['-c', 'credential.helper=!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f']
    env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": os.environ.get("HOME", "/root"),
           "GH_TOKEN": gh_token, "GIT_TERMINAL_PROMPT": "0", "LANG": "C.UTF-8"}
    r = lancer(["git", *aide, *args], cwd=cwd, env=env, delai=delai)
    if r.returncode != 0:
        raise Refus(f"git {args[0]} : code {r.returncode} : {r.stderr.decode('utf-8', 'replace')[-300:]}")
    return r.stdout.decode("utf-8", "replace")


def port_libre(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("127.0.0.1", port)) != 0


def etat_relais(port: int) -> dict | None:
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/relais/etat", timeout=10) as r:
            return json.loads(r.read().decode("utf-8"))
    except Exception:  # relais absent ou muet : rendu comme tel au relevé, jamais deviné
        return None


def arreter_par_pid(p: subprocess.Popen, j: Journal, nom: str, delai_s: float = 60) -> int | None:
    """R10 : arrêt par l'identifiant du processus que l'on a lancé soi-même (jamais par motif)."""
    if p.poll() is not None:
        return p.returncode
    j.ecrire(f"arrêt de {nom} par son identifiant {p.pid} (TERM)")
    os.killpg(p.pid, signal.SIGTERM)
    try:
        return p.wait(timeout=delai_s)
    except subprocess.TimeoutExpired:
        j.ecrire(f"{nom} {p.pid} toujours vivant après {delai_s:g} s : KILL")
        os.killpg(p.pid, signal.SIGKILL)
        return p.wait(timeout=delai_s)


class Machine:
    """Séquence de la machine ; chaque étape écrit au journal ; toute garde qui refuse mène à la fin propre."""

    def __init__(self, r: Reglages, environ: dict[str, str]):
        self.r = r
        self.env = environ
        self.secrets = {k: environ.get(k, "") for k in SECRETS}
        self.t = r.travail
        self.etat_fichier = self.t / "ETAT"
        self.relais = None
        self.course = None
        self.code_course = None
        self.debut = time.monotonic()
        self.prix_h = float(environ.get("PRIX_H_USD", "nan"))
        self.nature_fin = None

    # -- utilitaires
    def etat(self, valeur: str) -> None:
        self.etat_fichier.write_text(valeur + "\n")
        self.j.ecrire(f"ETAT {valeur}")

    def env_relais(self) -> dict:
        return {"PATH": "/usr/bin:/bin:/usr/local/bin", "LANG": "C.UTF-8", "GEMINI_API_KEY": self.secrets["CLE_ARGON"]}

    def env_course(self) -> dict:  # aucune variable de clé : le lanceur refuserait (et c'est voulu)
        return {"PATH": "/usr/local/bin:/usr/bin:/bin", "LANG": "C.UTF-8", "HOME": str(self.t), "TMPDIR": "/tmp"}

    def cout_machine(self) -> float:
        return self.prix_h * (time.monotonic() - self.debut) / 3600

    # -- entrée
    def principal(self) -> int:
        if self.etat_fichier.exists():  # reprise du conteneur : jamais de relance (R12)
            self.j = Journal(self.t / "journal-hote-a1-v3-troisieme-v1.log", self.secrets)
            avant = self.etat_fichier.read_text().strip()
            self.j.ecrire(f"REPRISE du conteneur : état précédent « {avant} » ; rien n'est relancé")
            if avant == "verse":  # tout est déjà versé et vérifié : seul reste le geste sur la machine
                return self.se_detruire(True)
            self.nature_fin = "reprise_du_conteneur"
            return self.fin(BRANCHE_INTERROMPUE)
        self.t.mkdir(parents=True, exist_ok=False)
        self.j = Journal(self.t / "journal-hote-a1-v3-troisieme-v1.log", self.secrets)
        self.j.ecrire(f"{VERSION} ; GO {self.env.get('GO_ID')} ; prix {self.prix_h} USD/h ; plafond machine "
                      f"{self.r.plafond_machine_usd} USD, {self.r.duree_max_s / 3600:g} h ; identifiant "
                      f"{self.env.get('CONTAINER_ID', '?')}")
        self.etat("demarrage")
        try:
            self.preparer()
            self.etat("course")
            self.garder()
        except Refus as e:
            self.j.ecrire(f"REFUS : {e}")
            self.nature_fin = "refus_avant_course" if self.course is None else "refus_pendant_la_course"
        except Exception as e:  # jamais un repli silencieux : écrit, puis fin propre
            self.j.ecrire(f"EXCEPTION {type(e).__name__} : {self.j.masquer(str(e))[:500]}")
            self.nature_fin = "exception_de_l_hote"
        return self.fin(BRANCHE_DONNEES if self.course is not None else BRANCHE_REFUS)

    # -- avant la course
    def preparer(self) -> None:
        r, e = self.r, self.env
        for k in ("CLE_ARGON", "GH_TOKEN", "COMMIT_PUBLIC", "SHA_TEXTE", "COMMIT_REGISTRE", "GO_ID", "PRIX_H_USD"):
            if not e.get(k):
                raise Refus(f"variable {k} absente")
        if not (0 < self.prix_h <= PRIX_MAX_H_USD):
            raise Refus(f"prix horaire {self.prix_h} hors de ]0 ; {PRIX_MAX_H_USD}]")
        gh = self.secrets["GH_TOKEN"]
        # 1. GO sur main, par la garde de main (règle d'extension) ; registre et garde lus au commit de main du moment
        git("fetch", "-q", "origin", *[f"+refs/heads/{b}:refs/remotes/origin/{b}" for b in
                                       ("main", SOURCE_REGISTRE, REF_SOURCES, REF_CONFIGURATION)],
            cwd=r.clone_prive, gh_token=gh)
        tete_main = git("rev-parse", "refs/remotes/origin/main", cwd=r.clone_prive).strip()
        reg_main = self.t / "registre-go-main.md"
        reg_main.write_bytes(lancer(["git", "show", f"{tete_main}:registres/go.md"], cwd=r.clone_prive).stdout)
        garde = self.t / "garde_calcul_main.py"
        garde.write_bytes(lancer(["git", "show", f"{tete_main}:.claude/hooks/garde_calcul.py"], cwd=r.clone_prive).stdout)
        g = verifier_go(reg_main, garde, e["GO_ID"], PLAFOND_COURSE_USD,
                        r.aujourd_hui or dt.datetime.now(dt.timezone.utc).date())
        self.j.ecrire(f"GO accepté par la garde de main {tete_main} : {json.dumps(g, ensure_ascii=False)}")
        self.j.ecrire("grep main : " + " ; ".join(self._grep(reg_main, e["GO_ID"])))
        # 2. Registre des GO passé au lanceur : copie entière, sans retouche, au commit que fixe le texte v3
        reg = self.t / "registre-go.md"
        if lancer(["git", "merge-base", "--is-ancestor", e["COMMIT_REGISTRE"], f"refs/remotes/origin/{SOURCE_REGISTRE}"],
                  cwd=r.clone_prive).returncode != 0:
            raise Refus(f"commit du registre {e['COMMIT_REGISTRE']} absent de la branche {SOURCE_REGISTRE}")
        sortie = lancer(["git", "show", f"{e['COMMIT_REGISTRE']}:registres/go.md"], cwd=r.clone_prive)
        if sortie.returncode != 0:
            raise Refus(f"registre au commit {e['COMMIT_REGISTRE']} introuvable")
        reg.write_bytes(sortie.stdout)
        doubles = doublons_lecteur_du_lanceur(reg)
        if doubles:
            raise Refus(f"registre {e['COMMIT_REGISTRE']} : identifiants en double {doubles} (le lanceur le refuserait)")
        verifier_go(reg, garde, e["GO_ID"], PLAFOND_COURSE_USD, r.aujourd_hui or dt.datetime.now(dt.timezone.utc).date())
        self.sha_registre = sha256_fichier(reg)
        self.j.ecrire(f"registre-go.md : commit {e['COMMIT_REGISTRE']}, sha256 {self.sha_registre} ; grep : "
                      + " ; ".join(self._grep(reg, e["GO_ID"])))
        # 3. Pièces gelées, extraites des branches privées, empreintes vérifiées
        self.extraire_sources()
        # 4. Dépôt public au commit qui porte le texte scellé v3 ; code gelé ancêtre ; arbre propre
        git("clone", "-q", r.depot_public, str(r.clone_public))
        git("checkout", "-q", "--detach", e["COMMIT_PUBLIC"], cwd=r.clone_public)
        if lancer(["git", "merge-base", "--is-ancestor", r.commit_code_gele, e["COMMIT_PUBLIC"]],
                  cwd=r.clone_public).returncode != 0:
            raise Refus(f"le commit {e['COMMIT_PUBLIC']} ne descend pas du code gelé {r.commit_code_gele}")
        texte = r.clone_public / NOM_TEXTE
        vu = sha256_fichier(texte) if texte.is_file() else None
        compagnon = Path(str(texte) + ".sha256")
        comp = compagnon.read_text().split()[0] if compagnon.is_file() else None
        if not (vu == e["SHA_TEXTE"] == comp):
            raise Refus(f"texte v3 : empreinte {vu}, attendue {e['SHA_TEXTE']}, compagnon {comp}")
        statut = git("status", "--porcelain", cwd=r.clone_public)
        if statut.strip():
            raise Refus("arbre du dépôt public modifié : " + statut[:200])
        self.j.ecrire(f"dépôt public {e['COMMIT_PUBLIC']} (descend de {r.commit_code_gele}) ; texte {vu} = compagnon ; "
                      "git status --porcelain vide")
        # 5. Relais neuf, seul à tenir la clé ; puis vérification, puis course
        if not port_libre(r.port):
            raise Refus(f"port {r.port} déjà pris : un autre relais vit (Argon seul)")
        self.lancer_relais()
        self.verifier_seulement()
        self.lancer_course()

    def _ref_existe(self, ref: str) -> bool:
        return lancer(["git", "rev-parse", "-q", "--verify", ref], cwd=self.r.clone_prive).returncode == 0

    @staticmethod
    def _grep(chemin: Path, motif: str) -> list[str]:
        return [f"{n}:{l[:120]}" for n, l in enumerate(chemin.read_text(encoding="utf-8").splitlines(), 1) if motif in l]

    def extraire_sources(self) -> None:
        r = self.r
        r.racine_sources.mkdir(parents=True, exist_ok=True)
        ref = f"refs/remotes/origin/{REF_SOURCES}"
        arch = lancer(["git", "archive", ref, NUIT, "donnees/espece-seule-v1/collisionneur_v7.py"], cwd=r.clone_prive)
        if arch.returncode != 0:
            raise Refus(f"git archive {ref} : code {arch.returncode}")
        with tarfile.open(fileobj=io.BytesIO(arch.stdout)) as tar:
            tar.extractall(r.racine_sources, filter="data")
        conf = lancer(["git", "show", f"refs/remotes/origin/{REF_CONFIGURATION}:{CHEMIN_CONF_DANS_REF}"],
                      cwd=r.clone_prive)
        if conf.returncode != 0:
            raise Refus("configuration gelée introuvable sur sa branche")
        (r.racine_sources / NUIT / "configuration-mini-course-kimi-argon-v3.json").write_bytes(conf.stdout)
        for chemin, attendu in r.empreintes.items():
            p = r.racine_sources / chemin
            vu = sha256_fichier(p) if p.is_file() else None
            if vu != attendu:
                raise Refus(f"pièce {chemin} : empreinte {vu}, attendue {attendu}")
        c = json.loads((r.racine_sources / NUIT / "configuration-mini-course-kimi-argon-v3.json").read_text())
        for nom, piece in c.get("pieces", {}).items():
            p = r.racine_sources / NUIT / piece["chemin"]
            if not p.is_file() or sha256_fichier(p) != piece["sha256"]:
                raise Refus(f"pièce {nom} de la configuration : empreinte différente ou fichier absent")
        self.j.ecrire(f"pièces gelées : {len(r.empreintes)} empreintes égales ; {len(c.get('pieces', {}))} pièces de la "
                      "configuration égales")

    def lancer_relais(self) -> None:
        r = self.r
        commande = r.racine_sources / NUIT / "commande_argon_v56_nuit_v2.py"
        self.journal_relais = self.t / "relais-argon-journal-a1-v3-troisieme.jsonl"
        self.cmd_relais = [r.python_relais, "-I", "-B", str(commande), "servir", "--port", str(r.port), "--plafond-usd",
                           str(PLAFOND_RELAIS_USD), "--max-appels", str(MAX_APPELS_RELAIS), "--journal",
                           str(self.journal_relais)]
        self._demarrer_relais()
        fin = time.monotonic() + r.attente_relais_s
        etat = None
        while time.monotonic() < fin:
            etat = etat_relais(r.port)
            if etat is not None:
                break
            if self.relais.poll() is not None:
                raise Refus(f"relais sorti en code {self.relais.returncode} au démarrage")
            time.sleep(0.5)
        if etat is None:
            raise Refus("relais muet au démarrage")
        attendu = {"plafond_usd": PLAFOND_RELAIS_USD, "max_appels": MAX_APPELS_RELAIS, "appels": 0, "cle_presente": True}
        ecarts = {k: etat.get(k) for k, v in attendu.items() if etat.get(k) != v}
        if ecarts:
            raise Refus(f"relais : réglages inattendus {ecarts}")
        self.j.ecrire(f"relais {r.port} PID {self.relais.pid} : plafond {etat['plafond_usd']} USD, "
                      f"{etat['max_appels']} appels, clé présente (booléen), dépense {etat.get('depense_usd')}")

    def _demarrer_relais(self) -> None:
        sortie = open(self.t / "relais-argon-stdout.log", "ab")
        self.relais = subprocess.Popen(self.cmd_relais, env=self.env_relais(), stdout=sortie, stderr=subprocess.STDOUT,
                                       stdin=subprocess.DEVNULL, start_new_session=True)

    def cmd_course(self, verifier: bool) -> list[str]:
        r, e = self.r, self.env
        conf = r.racine_sources / NUIT / "configuration-mini-course-kimi-argon-v3.json"
        cmd = ["nice", "-n", "10", r.python_course, "-I", "-B", "demonstrations/attaque_goodhart_v3.py",
               str(self.t / "sortie-attaque-goodhart-v3"), "--preenregistrement",
               NOM_TEXTE.removeprefix("orchestrator/"), "--configuration", str(conf), "--moteur", "reel",
               "--confirmer-moteur-reel", "--registre-go", str(self.t / "registre-go.md"), "--go", e["GO_ID"]]
        return cmd + (["--verifier-seulement"] if verifier else [])

    def verifier_seulement(self) -> None:
        res = lancer(self.cmd_course(True), cwd=self.r.clone_public / "orchestrator", env=self.env_course(), delai=900)
        (self.t / "verifier-seulement.log").write_bytes(res.stdout + res.stderr)
        self.j.ecrire(f"--verifier-seulement : code {res.returncode}")
        if res.returncode != 0:
            raise Refus(f"--verifier-seulement en code {res.returncode} : rien ne part")

    def lancer_course(self) -> None:
        sortie = open(self.t / "course-stdout-a1-v3-troisieme.log", "ab")
        self.course = subprocess.Popen(self.cmd_course(False), cwd=self.r.clone_public / "orchestrator",
                                       env=self.env_course(), stdout=sortie, stderr=subprocess.STDOUT,
                                       stdin=subprocess.DEVNULL, start_new_session=True)
        self.j.ecrire(f"course lancée : PID {self.course.pid} (processus lancé par l'hôte lui-même, sans coquille)")

    # -- pendant la course : garde sans session
    def garder(self) -> None:
        r = self.r
        releves = self.t / "garde-a1-v3-troisieme.jsonl"
        while True:
            code = self.course.poll()
            relais_vivant = self.relais.poll() is None
            etat = etat_relais(r.port) if relais_vivant else None
            ecoule = time.monotonic() - self.debut
            ligne = {"utc": maintenant(), "course_vivante": code is None, "relais_vivant": relais_vivant,
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
                self.j.ecrire(f"PLAFOND DE LA MACHINE atteint ({ecoule / 3600:.3f} h, {self.cout_machine():.2f} USD) : "
                              "la course est arrêtée par son identifiant (écart déclaré, section 8 du texte v3)")
                self.code_course = arreter_par_pid(self.course, self.j, "course")
                (self.t / "code-sortie-lanceur.txt").write_text(f"{self.code_course} (arrêt au plafond de la machine)\n")
                return
            time.sleep(r.periode_s)

    # -- fin propre, quel que soit le chemin
    def fin(self, branche: str) -> int:
        self.etat("scellement")
        if self.course is not None and self.course.poll() is None:
            self.code_course = arreter_par_pid(self.course, self.j, "course")
        if self.relais is not None:
            dernier = etat_relais(self.r.port)
            if dernier:
                self.j.ecrire(f"relais, relevé final : {dernier.get('appels')} appels, {dernier.get('depense_usd')} USD")
            arreter_par_pid(self.relais, self.j, "relais")
        if hasattr(self, "sha_registre"):
            apres = sha256_fichier(self.t / "registre-go.md")
            self.j.ecrire(f"registre-go.md après la course : {apres} ({'inchangé' if apres == self.sha_registre else 'CHANGÉ'})")
        self.j.ecrire(f"nature de la fin : {self.nature_fin} ; coût de la machine estimé {self.cout_machine():.4f} USD ; "
                      "scellement (liste d'empreintes de chaque fichier, puis copie versée, sans autre écriture)")
        liste = self.sceller()
        pousse = False
        try:
            fuite = self.fuites()
            if fuite:
                raise Refus(f"valeur de secret trouvée dans {fuite} : rien n'est versé")
            pousse = self.verser(branche, liste)
        except Refus as e:
            self.j.ecrire(f"VERSEMENT IMPOSSIBLE : {e}")
        return self.se_detruire(pousse)

    def fichiers_a_verser(self) -> list[Path]:
        return sorted(p for p in self.t.rglob("*") if p.is_file() and "__pycache__" not in p.parts)

    def sceller(self) -> Path:
        liste = self.t / "EMPREINTES-sortie-a1-v3-troisieme-v1.txt"
        lignes = [f"{sha256_fichier(p)}  {p.relative_to(self.t)}" for p in self.fichiers_a_verser() if p != liste]
        liste.write_text("\n".join(lignes) + "\n")
        return liste  # rien n'est écrit au journal entre la liste et la copie versée : la liste reste juste

    def fuites(self) -> list[str]:
        """Contrôle des secrets avant tout versement : la valeur exacte de chaque secret, dans chaque fichier versé."""
        valeurs = [v.encode() for v in self.secrets.values() if v and len(v) >= 8]
        return [str(p.relative_to(self.t)) for p in self.fichiers_a_verser() if any(v in p.read_bytes() for v in valeurs)]

    def verser(self, branche: str, liste: Path) -> bool:
        """Copie de travail à part (`versement`), jamais celle d'où l'amorce tourne ; branche neuve, partie de main."""
        r, gh = self.r, self.secrets["GH_TOKEN"]
        url = git("remote", "get-url", "origin", cwd=r.clone_prive).strip()
        distant = git("ls-remote", url, f"refs/heads/{branche}", gh_token=gh)
        if distant.strip():
            raise Refus(f"branche {branche} déjà présente (R12) : rien n'est écrasé")
        v = r.travail.parent / (r.travail.name + "-versement")
        if v.exists():
            raise Refus(f"copie de versement {v} déjà présente (R12)")
        git("clone", "-q", "--depth", "1", "--single-branch", "--branch", "main", url, str(v), gh_token=gh)
        git("checkout", "-q", "-b", branche, cwd=v)
        dest = v / branche
        dest.mkdir(parents=True, exist_ok=False)
        for p in self.fichiers_a_verser():
            cible = dest / p.relative_to(self.t)
            cible.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, cible)
        git("add", "-f", str(dest), cwd=v)
        git("-c", "user.name=hote-durable-a1-v3", "-c", "user.email=hote@invalid", "commit", "-q", "-m",
            f"A1-v3, troisième course : état scellé de l'hôte durable ({self.nature_fin}), liste "
            f"{sha256_fichier(liste)[:16]}…, versé avant toute lecture", cwd=v)
        local = git("rev-parse", "HEAD", cwd=v).strip()
        for essai in range(1, r.essais_poussee + 1):
            try:
                git("push", "-q", "origin", f"HEAD:refs/heads/{branche}", cwd=v, gh_token=gh)
                vu = git("ls-remote", "origin", f"refs/heads/{branche}", cwd=v, gh_token=gh).split()
                if vu and vu[0] == local:
                    self.j.ecrire(f"versé : {branche} = {local} (vérifié par ls-remote) ; liste {sha256_fichier(liste)}")
                    self.etat("verse")
                    return True
            except Refus as e:
                self.j.ecrire(f"poussée {essai}/{r.essais_poussee} : {e}")
            time.sleep(r.attente_poussee_s * essai)
        return False

    def se_detruire(self, pousse: bool) -> int:
        ident = self.env.get("CONTAINER_ID", "")
        if not IDENT.fullmatch(ident or ""):
            self.j.ecrire(f"identifiant de la machine illisible ({ident!r}) : aucun geste ; la session qui reprend "
                          "détruit par l'inventaire (R14)")
            return 4
        client = ClientVastJouet(self.r.vast_jouet) if self.r.jouet else ClientVast(self.secrets["CONTAINER_API_KEY"])
        if pousse:
            try:
                self.j.ecrire(f"destruction de la machine par son identifiant {ident}")
                client.detruire(int(ident))
                return 0
            except Refus as e:
                self.j.ecrire(f"destruction refusée ({e}) : arrêt de la machine {ident} par son identifiant")
        else:
            self.j.ecrire(f"versement non vérifié : la machine {ident} est ARRÊTÉE, non détruite (données gardées)")
        try:
            client.arreter(int(ident))
            return 3
        except Refus as e:
            self.j.ecrire(f"arrêt de la machine {ident} refusé : {e} ; la session qui reprend s'en charge (R14)")
            return 4


def inventaire(client) -> list[dict]:
    return [champs_filtres(i) for i in client.instances()]


def principal(argv=None) -> int:
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sous = a.add_subparsers(dest="mode", required=True)
    l = sous.add_parser("louer")
    l.add_argument("--go", required=True)
    l.add_argument("--registre-main", required=True, help="registres/go.md de main, lu au moment du lancement")
    l.add_argument("--garde-main", required=True, help=".claude/hooks/garde_calcul.py du même commit")
    l.add_argument("--offres", required=True, help="réponse brute de la recherche d'offres (JSON)")
    l.add_argument("--offre", required=True)
    l.add_argument("--commit-prive", required=True)
    l.add_argument("--commit-public", required=True)
    l.add_argument("--sha-texte", required=True)
    l.add_argument("--commit-registre", required=True)
    l.add_argument("--journal-local", required=True)
    l.add_argument("--verifier-seulement", action="store_true")
    l.add_argument("--jouet", help="fichier de Vast simulé (aucune location)")
    sous.add_parser("hote")
    i = sous.add_parser("inventaire")
    i.add_argument("--jouet")
    args = a.parse_args(argv)
    if args.mode == "louer":
        return louer(args, ClientVastJouet(Path(args.jouet)) if args.jouet else None)
    if args.mode == "inventaire":
        client = ClientVastJouet(Path(args.jouet)) if args.jouet else ClientVastCli()
        print(json.dumps(inventaire(client), ensure_ascii=False, indent=1))
        return 0
    return Machine(Reglages(), dict(os.environ)).principal()


if __name__ == "__main__":
    sys.exit(principal())
