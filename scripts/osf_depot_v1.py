#!/usr/bin/env python3
"""Dépôt d'empreintes sur l'Open Science Framework — horodatage par un tiers des préenregistrements,
verdicts et décisions scellés (décision de Lazar du 5 novembre 2026, « go OSF »).

Sous-commandes :
    manifeste  (processeur, sans réseau) : construit `livrables/osf-manifeste-v1/manifeste-v1.json`
               et `livrables/osf-manifeste-v1/LISEZMOI.md` à partir des fichiers scellés (`*.md` avec
               compagnon `.sha256`) de `prereg/`, `docs/verdicts/`, `docs/decisions/`. Sans `--ref`, lit
               l'arbre de travail ; avec `--ref main --ref prep/x …`, lit chaque référence git (les
               préenregistrements de `main` d'abord, puis ceux des branches de préparation).
    deposer    (réseau) : crée ou réutilise le projet « Controle boite blanche des menaces diffuses — empreintes »
               (privé par défaut, `--public` sinon), téléverse le manifeste et le LISEZMOI, puis relit depuis
               l'interface l'identifiant, l'adresse, la date de dépôt et l'empreinte du manifeste. Idempotent :
               un fichier déjà présent avec la même empreinte n'est pas retéléversé, et le script le dit.
    deposer --a-blanc : appelle seulement `GET …/users/me/` et imprime le nom d'utilisateur rendu.

Le jeton est lu par le nom `OSF_TOKEN` ; il n'est jamais affiché ni écrit. Toute réponse d'erreur de l'interface
est imprimée (statut, adresse, corps) sans en-tête d'autorisation. Aucune tentative répétée : une réponse illisible
arrête le script (R5, aucun repli silencieux).

    PYTHONPATH=src python scripts/osf_depot_v1.py manifeste --ref main
    OSF_TOKEN=… python scripts/osf_depot_v1.py deposer --a-blanc
    OSF_TOKEN=… python scripts/osf_depot_v1.py deposer
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

TITRE_PROJET = "Controle boite blanche des menaces diffuses — empreintes"
API_DEFAUT = "https://api.osf.io/v2"
DEPOT_DISTANT = "https://github.com/lciric/controle-ia-travail"
DEPOT_PUBLIC = "https://github.com/lciric/controle-ia"
DOSSIERS = ("prereg", "docs/verdicts", "docs/decisions")
SORTIE_DEFAUT = "livrables/osf-manifeste-v1/manifeste-v1.json"
NOM_LISEZMOI = "LISEZMOI.md"
VERSION_MANIFESTE = "osf-manifeste-v1"
NOM_JETON = "OSF_TOKEN"
SUFFIXE = ".sha256"
DELAI_RESEAU = 60
PAGES_MAX = 50
_LIGNE_COMPAGNON = re.compile(r"^([0-9a-f]{64})  (\S.*)$")


class GardeArret(RuntimeError):
    """Arrêt commandé par une garde : jamais attrapé pour continuer."""


class ErreurInterface(RuntimeError):
    """Réponse d'erreur de l'interface (statut HTTP ≥ 400) : imprimée sans en-tête d'autorisation."""

    def __init__(self, statut: int, url: str, corps: str):
        super().__init__(f"interface : statut {statut} sur {url}\n{corps}")
        self.statut, self.url, self.corps = statut, url, corps


# --------------------------------------------------------------------------- secret
_SECRETS: list[str] = []


def _masquer(texte: str) -> str:
    for s in _SECRETS:
        if s:
            texte = texte.replace(s, "«jeton masqué»")
    return texte


def dire(texte: str = "", *, erreur: bool = False) -> None:
    """Toute sortie du script passe ici : le jeton, s'il y figurait, est masqué (défense en profondeur)."""
    print(_masquer(str(texte)), file=sys.stderr if erreur else sys.stdout, flush=True)


def lire_jeton() -> str:
    jeton = os.environ.get(NOM_JETON, "")
    if not jeton.strip():
        raise GardeArret(f"variable d'environnement {NOM_JETON} absente ou vide : rien n'est tenté")
    _SECRETS.append(jeton)
    return jeton


# --------------------------------------------------------------------------- outils
def sha256_octets(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def maintenant_utc() -> str:
    """L'heure vient de `date -u` (consigne), jamais de l'horloge Python."""
    r = subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], check=True, capture_output=True, text=True)
    return r.stdout.strip()


def git(racine: Path, *args: str) -> str:
    r = subprocess.run(["git", "-C", str(racine), *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise GardeArret(f"git {' '.join(args)} : {r.stderr.strip() or 'échec'}")
    return r.stdout


def lire_compagnon(texte: str, chemin_compagnon: str, nom_attendu: str) -> str:
    lignes = [l for l in texte.splitlines() if l.strip()]
    if len(lignes) != 1:
        raise GardeArret(f"{chemin_compagnon} : une seule ligne attendue, {len(lignes)} trouvées")
    m = _LIGNE_COMPAGNON.match(lignes[0])
    if not m:
        raise GardeArret(f"{chemin_compagnon} : ligne illisible {lignes[0]!r}")
    if m.group(2) != nom_attendu:
        raise GardeArret(f"{chemin_compagnon} : nom {m.group(2)!r} au lieu de {nom_attendu!r}")
    return m.group(1)


# --------------------------------------------------------------------------- manifeste
def _entrees_arbre(racine: Path, ignorer_non_scelles: bool) -> tuple[list[dict], list[dict]]:
    """Fichiers scellés de l'arbre de travail. Un `.md` sans compagnon, ou non commis, arrête (sauf option)."""
    if git(racine, "rev-parse", "--is-inside-work-tree").strip() != "true":
        raise GardeArret(f"{racine} n'est pas un dépôt git : le commit de chaque fichier ne peut pas être établi")
    entrees, exclus, fautes = [], [], []
    for dossier in DOSSIERS:
        base = racine / dossier
        if not base.is_dir():
            continue
        for p in sorted(base.glob("*.md")):
            rel = p.relative_to(racine).as_posix()
            compagnon = Path(str(p) + SUFFIXE)
            if not compagnon.is_file():
                fautes.append((rel, "aucun compagnon .sha256 : fichier non scellé"))
                continue
            octets = p.read_bytes()
            obtenue = sha256_octets(octets)
            try:
                attendue = lire_compagnon(compagnon.read_text(encoding="utf-8"), rel + SUFFIXE, p.name)
            except GardeArret as e:  # compagnon mal formé : scellement non conforme, excluable mais listé
                fautes.append((rel, f"compagnon mal formé : {e}"))
                continue
            if obtenue != attendue:
                raise GardeArret(f"{rel} : empreinte {obtenue[:12]}… ≠ scellée {attendue[:12]}… (fichier altéré)")
            etat = git(racine, "status", "--porcelain", "--", rel, rel + SUFFIXE).strip()
            if etat:
                fautes.append((rel, f"non commis ou modifié par rapport au dernier commit ({etat.splitlines()[0]})"))
                continue
            commit = git(racine, "log", "-1", "--format=%H", "--", rel).strip()
            entrees.append({"chemin": rel, "sha256": obtenue, "compagnon": rel + SUFFIXE,
                            "commit": commit, "source": "arbre de travail"})
    if fautes and not ignorer_non_scelles:
        details = "\n".join(f"  {c} : {m}" for c, m in fautes)
        raise GardeArret(f"{len(fautes)} fichier(s) refusé(s) ; rien n'est écrit :\n{details}\n"
                         "(scelle et commets, ou passe --ignorer-non-scelles pour les exclure, listés dans le manifeste)")
    exclus = [{"chemin": c, "motif": m, "source": "arbre de travail"} for c, m in fautes]
    return entrees, exclus


def _entrees_ref(racine: Path, ref: str, ignorer_non_scelles: bool) -> tuple[list[dict], list[dict], str]:
    """Fichiers scellés tels qu'ils sont dans une référence git (branche, étiquette ou commit)."""
    commit_ref = git(racine, "rev-parse", "--verify", f"{ref}^{{commit}}").strip()
    noms = git(racine, "ls-tree", "-r", "--name-only", commit_ref, "--", *DOSSIERS).splitlines()
    presents = set(noms)
    entrees, fautes = [], []
    for rel in sorted(n for n in noms if n.endswith(".md") and Path(n).parent.as_posix() in DOSSIERS):
        if rel + SUFFIXE not in presents:
            fautes.append((rel, "aucun compagnon .sha256 : fichier non scellé"))
            continue
        octets = subprocess.run(["git", "-C", str(racine), "show", f"{commit_ref}:{rel}"],
                                check=True, capture_output=True).stdout
        obtenue = sha256_octets(octets)
        try:
            attendue = lire_compagnon(git(racine, "show", f"{commit_ref}:{rel}{SUFFIXE}"), f"{ref}:{rel}{SUFFIXE}",
                                      Path(rel).name)
        except GardeArret as e:  # compagnon mal formé : scellement non conforme, excluable mais listé
            fautes.append((rel, f"compagnon mal formé : {e}"))
            continue
        if obtenue != attendue:
            raise GardeArret(f"{ref}:{rel} : empreinte {obtenue[:12]}… ≠ scellée {attendue[:12]}… (fichier altéré)")
        commit = git(racine, "rev-list", "-1", commit_ref, "--", rel).strip()
        entrees.append({"chemin": rel, "sha256": obtenue, "compagnon": rel + SUFFIXE, "commit": commit, "source": ref})
    if fautes and not ignorer_non_scelles:
        details = "\n".join(f"  {ref}:{c} : {m}" for c, m in fautes)
        raise GardeArret(f"{len(fautes)} fichier(s) refusé(s) dans {ref} ; rien n'est écrit :\n{details}\n"
                         "(--ignorer-non-scelles les exclut, listés dans le manifeste)")
    exclus = [{"chemin": c, "motif": m, "source": ref} for c, m in fautes]
    return entrees, exclus, commit_ref


def texte_lisezmoi(manifeste: dict) -> str:
    sources = ", ".join(f"{s} ({c[:12]}…)" for s, c in manifeste["references"].items()) or "arbre de travail"
    return f"""# Empreintes du programme « Contrôle boîte blanche des menaces diffuses »

Ce projet de l'Open Science Framework ne contient que des **empreintes** (SHA-256), jamais les documents eux-mêmes.
Il sert à faire horodater par un tiers que les préenregistrements, verdicts de porte et décisions du programme
existaient, tels quels, au plus tard à la date de dépôt que l'interface affiche pour chaque fichier.

## Ce que contient `{manifeste["nom"]}`

Pour chaque fichier scellé des dossiers `{"`, `".join(manifeste["dossiers"])}` du dépôt de travail
(`{DEPOT_DISTANT}`, copie expurgée publique : `{DEPOT_PUBLIC}`) : son chemin, son empreinte SHA-256,
le chemin de son empreinte compagnon `.sha256` et le dernier commit git qui l'a touché.
Références lues : {sources}. Nombre de fichiers : {manifeste["nombre"]}.

## Ce que les empreintes prouvent — et ce qu'elles ne prouvent pas

- Elles prouvent qu'un document dont l'empreinte figure ici **n'a pas été modifié après la date de dépôt** du manifeste :
  tout changement d'un seul octet change l'empreinte.
- Elles prouvent donc qu'une hypothèse, une prédiction chiffrée, un seuil ou un critère de lecture gelé
  a été écrit **avant** la lecture du résultat qu'il encadre, si la date de dépôt précède le résultat.
- Elles ne prouvent **ni** que le contenu est juste, **ni** que les résultats sont bons : seulement l'antériorité et l'intégrité.
- Le dépôt est fait par l'équipe du programme ; l'horodatage, lui, est rendu par l'Open Science Framework.

## Comment un tiers vérifie

1. Noter, dans l'interface de l'Open Science Framework, la date de dépôt et l'empreinte SHA-256 du manifeste
   (métadonnées du fichier). Télécharger le manifeste et recalculer : `sha256sum {manifeste["nom"]}` ;
   les deux empreintes doivent coïncider.
2. Pour un document donné, obtenir le fichier à son chemin dans le dépôt (au commit indiqué) :
   `git show <commit>:<chemin> | sha256sum` ; l'empreinte doit être celle du manifeste.
3. Si elle coïncide, le document est identique à celui qui existait à la date de dépôt du manifeste.
"""


def construire_manifeste(racine: Path, refs: list[str], sortie: Path, ignorer_non_scelles: bool = False) -> dict:
    """Construit le manifeste (déterministe : ni heure ni chemin d'écriture dedans, pour qu'un second dépôt du
    même état produise le même fichier) et écrit le manifeste et le LISEZMOI à côté. Refuse d'écraser un manifeste différent (R12)."""
    racine = Path(racine).resolve()
    entrees: list[dict] = []
    exclus: list[dict] = []
    references: dict[str, str] = {}
    vus: set[tuple[str, str]] = set()
    if refs:
        for ref in refs:
            e, x, c = _entrees_ref(racine, ref, ignorer_non_scelles)
            references[ref] = c
            for ent in e:
                cle = (ent["chemin"], ent["sha256"])
                if cle not in vus:
                    vus.add(cle)
                    entrees.append(ent)
            exclus.extend(x)
    else:
        entrees, exclus = _entrees_arbre(racine, ignorer_non_scelles)
    if not entrees:
        raise GardeArret("aucun fichier scellé trouvé : manifeste vide refusé")
    sortie = Path(sortie)
    manifeste = {
        "version": VERSION_MANIFESTE,
        "nom": sortie.name,
        "depot": DEPOT_DISTANT,
        "references": references,
        "dossiers": list(DOSSIERS),
        "nombre": len(entrees),
        "fichiers": entrees,
        "exclus": exclus,
    }
    octets = (json.dumps(manifeste, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
    chemin_sortie = (racine / sortie) if not sortie.is_absolute() else sortie
    if chemin_sortie.exists() and chemin_sortie.read_bytes() != octets:
        raise GardeArret(f"{chemin_sortie} existe avec un autre contenu : R12 interdit d'écraser, "
                         "une nouvelle version prend un nouveau nom (--sortie …-v2.json)")
    chemin_sortie.parent.mkdir(parents=True, exist_ok=True)
    chemin_sortie.write_bytes(octets)
    lisezmoi = chemin_sortie.parent / NOM_LISEZMOI
    lisezmoi.write_text(texte_lisezmoi(manifeste), encoding="utf-8")
    manifeste["_octets"] = octets
    manifeste["_chemin"] = chemin_sortie
    manifeste["_lisezmoi"] = lisezmoi
    return manifeste


def cmd_manifeste(args) -> int:
    m = construire_manifeste(Path(args.racine), args.ref, Path(args.sortie), args.ignorer_non_scelles)
    dire(f"manifeste : {m['_chemin']}  ({m['nombre']} fichiers scellés, {len(m['exclus'])} exclus)")
    dire(f"sha256 du manifeste : {sha256_octets(m['_octets'])}")
    dire(f"lisezmoi  : {m['_lisezmoi']}  sha256 {sha256_octets(m['_lisezmoi'].read_bytes())}")
    for x in m["exclus"]:
        dire(f"EXCLU {x['source']}:{x['chemin']} : {x['motif']}")
    return 0


# --------------------------------------------------------------------------- interface réseau
class Interface:
    """Appels HTTP minimaux vers l'interface v2 de l'Open Science Framework et vers son service de fichiers.
    Aucune tentative répétée ; aucune écriture du jeton ailleurs que dans l'en-tête d'autorisation."""

    def __init__(self, api: str, jeton: str):
        self.api = api.rstrip("/")
        self._jeton = jeton
        self.journal: list[tuple[str, str]] = []
        self._ouvreur = urllib.request.build_opener(urllib.request.ProxyHandler())

    def brut(self, methode: str, url: str, corps: bytes | None = None, type_contenu: str | None = None) -> bytes:
        entetes = {"Authorization": f"Bearer {self._jeton}", "Accept": "application/vnd.api+json, application/json"}
        if type_contenu:
            entetes["Content-Type"] = type_contenu
        self.journal.append((methode, url))
        req = urllib.request.Request(url, data=corps, method=methode, headers=entetes)
        try:
            with self._ouvreur.open(req, timeout=DELAI_RESEAU) as rep:
                return rep.read()
        except urllib.error.HTTPError as e:
            try:
                texte = e.read().decode("utf-8", "replace")
            except Exception:  # corps illisible : on imprime quand même le statut
                texte = "(corps illisible)"
            raise ErreurInterface(e.code, url, texte[:4000]) from None
        except urllib.error.URLError as e:
            raise GardeArret(f"réseau : {url} injoignable ({e.reason})") from None

    def json(self, methode: str, url: str, document: dict | None = None) -> dict:
        corps = None
        if document is not None:
            corps = json.dumps(document).encode("utf-8")
        octets = self.brut(methode, url, corps, "application/vnd.api+json" if corps else None)
        try:
            doc = json.loads(octets.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as e:
            raise GardeArret(f"réponse illisible de {methode} {url} ({e}) ; aucune nouvelle tentative : "
                             f"{octets[:200]!r}") from None
        if not isinstance(doc, dict) or "data" not in doc:
            raise GardeArret(f"réponse inattendue de {methode} {url} : sans champ « data »")
        return doc

    # --- usagers et projets
    def utilisateur(self) -> dict:
        return self.json("GET", f"{self.api}/users/me/")["data"]

    def projets_par_titre(self, titre: str) -> list[dict]:
        url = f"{self.api}/users/me/nodes/?" + urllib.parse.urlencode({"filter[title]": titre, "page[size]": 100})
        trouves: list[dict] = []
        for _ in range(PAGES_MAX):
            doc = self.json("GET", url)
            trouves.extend(n for n in doc["data"] if n.get("attributes", {}).get("title") == titre)
            url = (doc.get("links") or {}).get("next")
            if not url:
                return trouves
        raise GardeArret(f"plus de {PAGES_MAX} pages de projets : recherche interrompue")

    def creer_projet(self, titre: str, public: bool) -> dict:
        doc = {"data": {"type": "nodes", "attributes": {"title": titre, "category": "project", "public": public,
                                                        "description": "Empreintes SHA-256 des préenregistrements, "
                                                                       "verdicts et décisions scellés du programme."}}}
        return self.json("POST", f"{self.api}/nodes/", doc)["data"]

    def rendre_public(self, identifiant: str) -> dict:
        doc = {"data": {"id": identifiant, "type": "nodes", "attributes": {"public": True}}}
        return self.json("PATCH", f"{self.api}/nodes/{identifiant}/", doc)["data"]

    # --- fichiers
    def lien_televersement(self, identifiant: str) -> str:
        doc = self.json("GET", f"{self.api}/nodes/{identifiant}/files/")
        for p in doc["data"]:
            if p.get("attributes", {}).get("provider") == "osfstorage":
                lien = (p.get("links") or {}).get("upload")
                if lien:
                    return lien
        raise GardeArret("le fournisseur de stockage « osfstorage » ne rend pas de lien de téléversement")

    def fichiers(self, identifiant: str) -> dict[str, dict]:
        doc = self.json("GET", f"{self.api}/nodes/{identifiant}/files/osfstorage/")
        resultat = {}
        for f in doc["data"]:
            a = f.get("attributes", {})
            if a.get("kind") == "file":
                resultat[a.get("name")] = f
        return resultat

    def televerser(self, lien: str, nom: str, octets: bytes) -> dict:
        sep = "&" if "?" in lien else "?"
        url = f"{lien}{sep}" + urllib.parse.urlencode({"kind": "file", "name": nom})
        octets_rep = self.brut("PUT", url, octets, "application/octet-stream")
        try:
            return json.loads(octets_rep.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as e:
            raise GardeArret(f"réponse illisible du téléversement de {nom} ({e}) ; aucune nouvelle tentative") from None


def _sha_distant(fichier: dict) -> str | None:
    return (((fichier.get("attributes") or {}).get("extra") or {}).get("hashes") or {}).get("sha256")


def cmd_deposer(args) -> int:
    jeton = lire_jeton()
    iface = Interface(args.api, jeton)
    if args.a_blanc:
        u = iface.utilisateur()
        nom = (u.get("attributes") or {}).get("full_name")
        if not nom:
            raise GardeArret("l'interface a répondu sans nom d'utilisateur")
        dire(nom)
        return 0

    chemin_manifeste = Path(args.manifeste)
    if not chemin_manifeste.is_file():
        raise GardeArret(f"{chemin_manifeste} absent : lance d'abord la sous-commande manifeste")
    octets_manifeste = chemin_manifeste.read_bytes()
    try:
        doc = json.loads(octets_manifeste.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as e:
        raise GardeArret(f"{chemin_manifeste} illisible : {e}") from None
    if doc.get("version") != VERSION_MANIFESTE or not doc.get("fichiers"):
        raise GardeArret(f"{chemin_manifeste} n'est pas un manifeste {VERSION_MANIFESTE} ou est vide")
    chemin_lisezmoi = chemin_manifeste.parent / NOM_LISEZMOI
    if not chemin_lisezmoi.is_file():
        raise GardeArret(f"{chemin_lisezmoi} absent : lance d'abord la sous-commande manifeste")
    a_deposer = [(chemin_manifeste.name, octets_manifeste, False),
                 (NOM_LISEZMOI, chemin_lisezmoi.read_bytes(), args.remplacer_lisezmoi)]

    dire(f"lancement (date -u) : {maintenant_utc()}")
    projets = iface.projets_par_titre(TITRE_PROJET)
    if len(projets) > 1:
        raise GardeArret(f"{len(projets)} projets portent le titre « {TITRE_PROJET} » : ambiguïté, rien n'est fait "
                         f"({', '.join(p['id'] for p in projets)})")
    if projets:
        projet = projets[0]
        dire(f"projet réutilisé : {projet['id']}")
    else:
        projet = iface.creer_projet(TITRE_PROJET, args.public)
        dire(f"projet créé : {projet['id']} ({'public' if args.public else 'privé'})")
    public = bool((projet.get("attributes") or {}).get("public"))
    if args.public and not public:
        projet = iface.rendre_public(projet["id"])
        public = bool((projet.get("attributes") or {}).get("public"))
        dire(f"projet rendu public : {public}")

    presents = iface.fichiers(projet["id"])
    lien = None
    nouveaux = 0
    for nom, octets, remplacer in a_deposer:
        local = sha256_octets(octets)
        distant = presents.get(nom)
        if distant is not None:
            sha_d = _sha_distant(distant)
            if sha_d == local:
                dire(f"{nom} : déjà déposé avec la même empreinte ({local[:12]}…), rien de nouveau")
                continue
            if not remplacer:
                raise GardeArret(f"{nom} existe déjà dans le projet avec une autre empreinte "
                                 f"({(sha_d or '?')[:12]}… ≠ {local[:12]}…) : R12, une nouvelle version prend un "
                                 "nouveau nom ; rien n'est téléversé")
            lien_fichier = (distant.get("links") or {}).get("upload")
            if not lien_fichier:
                raise GardeArret(f"{nom} : aucun lien de mise à jour rendu par l'interface")
            url = f"{lien_fichier}{'&' if '?' in lien_fichier else '?'}kind=file"
            iface.brut("PUT", url, octets, "application/octet-stream")
            dire(f"{nom} : remplacé (nouvelle version du même fichier, l'ancienne reste dans l'historique)")
            nouveaux += 1
            continue
        lien = lien or iface.lien_televersement(projet["id"])
        rep = iface.televerser(lien, nom, octets)
        sha_rep = _sha_distant(rep.get("data") or {})
        dire(f"{nom} : téléversé (empreinte rendue par le service de fichiers : {sha_rep or 'non rendue'})")
        nouveaux += 1

    # relecture depuis l'interface : ce qui fait foi
    releves = iface.fichiers(projet["id"])
    adresse = (projet.get("links") or {}).get("html") or f"https://osf.io/{projet['id']}/"
    dire()
    dire(f"identifiant du projet : {projet['id']}")
    dire(f"adresse              : {adresse}")
    dire(f"visibilité           : {'public' if public else 'privé'}")
    dire(f"fichiers nouveaux    : {nouveaux}" + ("" if nouveaux else " (second dépôt du même manifeste : rien créé)"))
    ecarts = 0
    for nom, octets, _ in a_deposer:
        f = releves.get(nom)
        if f is None:
            raise GardeArret(f"relecture : {nom} absent du projet après dépôt ; aucune nouvelle tentative")
        a = f.get("attributes") or {}
        sha_d = _sha_distant(f)
        local = sha256_octets(octets)
        verdict = "CONFORME" if sha_d == local else "ÉCART"
        ecarts += verdict == "ÉCART"
        dire(f"{nom}")
        dire(f"  date de dépôt (interface) : {a.get('date_created') or '?'}  (dernière modification : {a.get('date_modified') or '?'})")
        dire(f"  sha256 relue (interface)  : {sha_d or 'non rendue'}")
        dire(f"  sha256 locale             : {local}  → {verdict}")
        dire(f"  identifiant du fichier    : {f.get('id') or '?'}")
    if ecarts:
        raise GardeArret(f"{ecarts} empreinte(s) relue(s) différente(s) de l'empreinte locale")
    return 0


# --------------------------------------------------------------------------- ligne de commande
def construire_analyseur() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="osf_depot_v1", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="commande", required=True)
    m = sp.add_parser("manifeste", help="construit le manifeste des empreintes (sans réseau)")
    m.add_argument("--racine", default=".", help="racine du dépôt git (défaut : dossier courant)")
    m.add_argument("--ref", action="append", default=[], help="référence git à lire (répétable ; d'abord main, puis prep/…)")
    m.add_argument("--sortie", default=SORTIE_DEFAUT, help=f"chemin du manifeste (défaut : {SORTIE_DEFAUT})")
    m.add_argument("--ignorer-non-scelles", action="store_true",
                   help="exclut (et liste dans le manifeste) les fichiers sans compagnon au lieu d'arrêter")
    m.set_defaults(fonction=cmd_manifeste)
    d = sp.add_parser("deposer", help="dépose le manifeste sur l'Open Science Framework (réseau)")
    d.add_argument("--api", default=API_DEFAUT, help=f"racine de l'interface (défaut : {API_DEFAUT})")
    d.add_argument("--manifeste", default=SORTIE_DEFAUT, help="manifeste à déposer")
    d.add_argument("--public", action="store_true", help="projet public (défaut : privé) ; réservé à la mère")
    d.add_argument("--a-blanc", action="store_true", help="appelle seulement …/users/me/ et imprime le nom d'utilisateur")
    d.add_argument("--remplacer-lisezmoi", action="store_true", help="autorise une nouvelle version du LISEZMOI.md")
    d.set_defaults(fonction=cmd_deposer)
    return p


def main(argv: list[str] | None = None) -> int:
    args = construire_analyseur().parse_args(argv)
    try:
        return args.fonction(args)
    except ErreurInterface as e:
        dire(f"ERREUR DE L'INTERFACE : statut {e.statut} sur {e.url}", erreur=True)
        dire(e.corps, erreur=True)
        return 1
    except GardeArret as e:
        dire(f"ARRÊT : {e}", erreur=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
