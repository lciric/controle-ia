"""Corpus de l'environnement (a) (T0.5) : sélection de papiers sur arXiv et chaîne LaTeX → texte.

Règle de sélection : `docs/procedures/T0.5-selection-papiers-v1.md`, scellée avant le tirage ; l'entropie du
tirage vient de l'empreinte de ce document (aucune liberté après le scellement).

Chaîne, par papier :
1. source (« e-print ») de la dernière version, lue en mémoire et empreintée ; l'archive n'est jamais écrite
   sur disque ;
2. seuls les fichiers texte des sources (.tex, .bbl, .sty, …) sont extraits, dans un dossier neuf par papier
   (données non fiables : chemins contrôlés, liens jamais suivis, tailles bornées) ;
3. fichier principal (\\documentclass et \\begin{document}), commentaires retirés, inclusions aplaties dans le
   dossier du papier ;
4. conversion par pandoc en bac à sable (`--sandbox`), figures retirées, titre et résumé gardés ;
5. bornes de longueur du texte converti.

Une source refusée est une exclusion consignée avec son motif (`SourceRefusee`), jamais une erreur avalée ; une
panne réseau ou un état incohérent de l'API arrête le run (`GardeArret`) : aucune exclusion par accident.
Les textes vivent sous `donnees/` (ignoré par git ; licences) ; le dépôt garde les empreintes.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
import re
import ssl
import subprocess
import sys
import tarfile
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
import zlib
from pathlib import Path, PurePosixPath

from ..gardes import GardeArret

API = "https://export.arxiv.org/api/query"
SOURCE = "https://export.arxiv.org/src/{}"
NS = {"a": "http://www.w3.org/2005/Atom", "o": "http://a9.com/-/spec/opensearch/1.1/",
      "x": "http://arxiv.org/schemas/atom"}
PAUSE_S = 3.0  # politesse demandée par arXiv : une requête toutes les trois secondes
AGENT = "controle-ia-corpus/1.0 (recherche ; usage non commercial)"

REQUETE_V1 = ('(cat:cs.LG OR cat:cs.CL OR cat:cs.CV OR cat:stat.ML) AND (co:"NeurIPS 2025" OR co:"ICLR 2026") '
              'AND submittedDate:[202506010000 TO 202606302359]')
CATEGORIES_PRINCIPALES = ("cs.LG", "cs.CL", "cs.CV", "stat.ML")
DATES_V1 = ("2025-06-01", "2026-06-30")
CONFERENCE = re.compile(r"neurips\s*2025|iclr\s*2026", re.I)
REFUS_COMMENTAIRE = re.compile(r"workshop|under review|in review|submitted|submission|withdrawn", re.I)
SUJETS_EXCLUS = re.compile(
    r"decepti|sabotag|jailbreak|red[- ]?team|backdoor|trojan|monitor|alignment|safety|steganograph|sandbag|"
    r"scheming|honest|persuas|sycophan|manipulat|oversight|\blie\b|\blies\b|\blying\b|\bai control\b", re.I)
EXTENSIONS_TEXTE = frozenset({".tex", ".bbl", ".sty", ".cls", ".bst", ".def", ".cfg", ".clo", ".ltx"})
TAILLE_MAX_FICHIER = 5_000_000
TAILLE_MAX_TOTALE = 50_000_000
TAILLE_MAX_DECOMPRESSEE = 300_000_000
CARACTERES_MIN, CARACTERES_MAX = 15_000, 300_000
PROFONDEUR_MAX = 12
DELAI_PANDOC_S = 180
FORMAT_SORTIE = "markdown-raw_tex-raw_html-raw_attribute-link_attributes-header_attributes"
FILTRE_LUA = "function Image(el) return {} end\nfunction Figure(el) return {} end\n"
NOMS_PRINCIPAUX = ("main.tex", "ms.tex", "paper.tex", "arxiv.tex", "article.tex")


class SourceRefusee(Exception):
    """Exclusion d'un papier par la règle (motif consigné) ; ce n'est pas une panne."""


def sha256(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


# --- API d'arXiv -----------------------------------------------------------------------------------------

_ID = re.compile(r"arxiv\.org/abs/(?P<id>[0-9]{4}\.[0-9]{4,5})v(?P<v>[0-9]+)$")


def _texte(e, chemin: str) -> str:
    n = e.find(chemin, NS)
    return " ".join(n.text.split()) if n is not None and n.text else ""


def lire_entrees(xml: bytes) -> tuple[int, list[dict]]:
    """Analyse une page de l'API ; renvoie le total annoncé et les entrées."""
    racine = ET.fromstring(xml)
    total_n = racine.find("o:totalResults", NS)
    if total_n is None or total_n.text is None:
        raise GardeArret("page de l'API sans total : réponse inattendue")
    entrees = []
    for e in racine.findall("a:entry", NS):
        brut = _texte(e, "a:id")
        if "api/errors" in brut:
            raise GardeArret(f"l'API d'arXiv signale une erreur : {_texte(e, 'a:summary')[:200]!r}")
        m = _ID.search(brut)
        if m is None:
            raise GardeArret(f"identifiant arXiv illisible : {brut!r}")
        pc = e.find("x:primary_category", NS)
        entrees.append({
            "id": m["id"], "version": int(m["v"]),
            "publie": _texte(e, "a:published")[:10], "mis_a_jour": _texte(e, "a:updated")[:10],
            "categorie_principale": pc.get("term") if pc is not None else None,
            "categories": [c.get("term") for c in e.findall("a:category", NS)],
            "commentaire": _texte(e, "x:comment"), "titre": _texte(e, "a:title"), "resume": _texte(e, "a:summary"),
        })
    return int(total_n.text), entrees


def ouvrir_https(url: str, delai_s: float = 120.0) -> bytes:
    """Lecture HTTPS par le mandataire de l'environnement (autorités de `SSL_CERT_FILE` si posé)."""
    import os

    contexte = ssl.create_default_context(cafile=os.environ.get("SSL_CERT_FILE") or None)
    requete = urllib.request.Request(url, headers={"User-Agent": AGENT})
    with urllib.request.urlopen(requete, context=contexte, timeout=delai_s) as r:
        return r.read()


def _avec_reprises(ouvrir, url: str, essais: int, pause: float, dormir, journal: list) -> bytes:
    """Jusqu'à `essais` tentatives sur panne réseau ou erreur 5xx ; 403 et 404 remontent tels quels."""
    derniere = None
    for k in range(essais):
        if k:
            dormir(pause * (2 ** k))
        try:
            return ouvrir(url)
        except urllib.error.HTTPError as e:
            if e.code in (403, 404):
                raise
            derniere = f"HTTP {e.code}"
        except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as e:
            derniere = f"{type(e).__name__}: {e}"
        journal.append({"url": url, "tentative": k + 1, "panne": derniere})
    raise GardeArret(f"{url} : {essais} tentatives sans réponse ({derniere}) ; rien n'est exclu par accident")


def interroger(requete: str, taille_page: int, ouvrir=ouvrir_https, pause: float = PAUSE_S, dormir=time.sleep,
               essais: int = 4) -> tuple[list[bytes], list[dict], list]:
    """Toutes les pages de l'API pour `requete` (tri par date de soumission croissante)."""
    pages, entrees, journal, debut, total, vides = [], [], [], 0, None, 0
    while total is None or debut < total:
        url = API + "?" + urllib.parse.urlencode({"search_query": requete, "start": debut, "max_results": taille_page,
                                                  "sortBy": "submittedDate", "sortOrder": "ascending"})
        if pages or vides:
            dormir(pause)
        octets = _avec_reprises(ouvrir, url, essais, pause, dormir, journal)
        t, es = lire_entrees(octets)
        if total is None:
            total = t
        elif t != total:
            raise GardeArret(f"total de l'API changé en cours de lecture : {total} puis {t}")
        if not es:
            # l'API rend parfois une page vide passagère : nouvelle lecture, au plus `essais` fois, consignée
            vides += 1
            journal.append({"url": url, "page_vide": vides})
            if vides >= essais:
                raise GardeArret(f"page vide de l'API à {debut} sur {total}, {vides} fois")
            continue
        vides = 0
        pages.append(octets)
        entrees.extend(es)
        debut += len(es)
    ids = [e["id"] for e in entrees]
    if len(set(ids)) != len(ids) or len(ids) != total:
        raise GardeArret(f"{len(ids)} entrées lues, {len(set(ids))} distinctes, {total} annoncées : lecture incohérente")
    return pages, entrees, journal


# --- règle de sélection ----------------------------------------------------------------------------------

def motif_exclusion(e: dict, dates=DATES_V1) -> str | None:
    """Premier motif d'exclusion de la règle, ou None si l'entrée est candidate."""
    if e["categorie_principale"] not in CATEGORIES_PRINCIPALES:
        return "catégorie principale hors de la liste"
    if not (dates[0] <= e["publie"] <= dates[1]):
        return "première version hors de la fenêtre de dates"
    if not CONFERENCE.search(e["commentaire"]):
        return "commentaire sans NeurIPS 2025 ni ICLR 2026"
    if REFUS_COMMENTAIRE.search(e["commentaire"]):
        return "commentaire : atelier, soumission, relecture ou retrait"
    if SUJETS_EXCLUS.search(e["titre"] + " " + e["resume"]):
        return "sujet exclu (titre ou résumé)"
    return None


def filtrer(entrees: list[dict], dates=DATES_V1) -> tuple[list[dict], list[dict]]:
    candidats, exclus = [], []
    for e in entrees:
        m = motif_exclusion(e, dates)
        if m is None:
            candidats.append(e)
        else:
            exclus.append({"id": e["id"], "motif": m})
    return candidats, exclus


def entropie_de_regle(chemin_regle: str | Path) -> tuple[int, str]:
    """Entropie du tirage : les 32 premiers chiffres hexadécimaux de l'empreinte scellée de la règle."""
    from ..scellement import verifier

    h = verifier(chemin_regle)
    return int(h[:32], 16), h


def ordre_de_tirage(ids: list[str], graine: dict) -> list[str]:
    """Permutation des identifiants triés, par le générateur de la graine consignée (R9)."""
    from ..manifeste import generateur

    tries = sorted(ids)
    if len(set(tries)) != len(tries):
        raise GardeArret("identifiants en double avant le tirage")
    return [tries[k] for k in generateur(graine).permutation(len(tries))]


# --- chaîne LaTeX → texte --------------------------------------------------------------------------------

def _decompresser_borne(octets: bytes, limite: int = TAILLE_MAX_DECOMPRESSEE) -> bytes:
    d = zlib.decompressobj(16 + zlib.MAX_WBITS)
    sortie = d.decompress(octets, limite + 1)
    if len(sortie) > limite or d.unconsumed_tail:
        raise SourceRefusee(f"archive décompressée au-delà de {limite} octets")
    return sortie


def _est_tar(octets: bytes) -> bool:
    try:
        with tarfile.open(fileobj=io.BytesIO(octets), mode="r:") as tf:
            tf.getmembers()
        return True
    except (tarfile.TarError, EOFError):
        return False


def nature_source(octets: bytes) -> tuple[str, bytes]:
    """« pdf », « tar », « tex-seul » ou « inconnu », et le contenu décompressé."""
    if octets[:4] == b"%PDF":
        return "pdf", b""
    if octets[:2] == b"\x1f\x8b":
        brut = _decompresser_borne(octets)
        if brut[:4] == b"%PDF":
            return "pdf", b""
        return ("tar", brut) if _est_tar(brut) else ("tex-seul", brut)
    if _est_tar(octets):
        return "tar", octets
    return "inconnu", b""


def extraire_textes(brut_tar: bytes, dossier: Path) -> dict:
    """Extrait les seuls fichiers texte des sources dans `dossier` (neuf) ; chemins et tailles contrôlés."""
    dossier.mkdir(parents=True, exist_ok=False)
    base = dossier.resolve()
    gardes, ignores, total = [], 0, 0
    with tarfile.open(fileobj=io.BytesIO(brut_tar), mode="r:") as tf:
        for m in tf.getmembers():
            p = PurePosixPath(m.name)
            if p.is_absolute() or ".." in p.parts:
                raise SourceRefusee(f"chemin dangereux dans l'archive : {m.name!r}")
            if not m.isfile():
                continue  # dossiers, liens, périphériques : jamais extraits ni suivis
            if p.suffix.lower() not in EXTENSIONS_TEXTE:
                ignores += 1
                continue
            if m.size > TAILLE_MAX_FICHIER:
                raise SourceRefusee(f"fichier texte de {m.size} octets dans l'archive : {m.name!r}")
            total += m.size
            if total > TAILLE_MAX_TOTALE:
                raise SourceRefusee(f"fichiers texte au-delà de {TAILLE_MAX_TOTALE} octets")
            cible = dossier.joinpath(*[x for x in p.parts if x not in ("", ".")])
            if not str(cible.resolve()).startswith(str(base) + "/"):
                raise SourceRefusee(f"chemin hors du dossier du papier : {m.name!r}")
            if cible.exists():
                raise SourceRefusee(f"nom en double dans l'archive : {m.name!r}")
            cible.parent.mkdir(parents=True, exist_ok=True)
            flux = tf.extractfile(m)
            cible.write_bytes(flux.read() if flux is not None else b"")
            gardes.append(str(cible.relative_to(dossier)))
    if not gardes:
        raise SourceRefusee("aucun fichier texte de source dans l'archive")
    return {"fichiers_texte": sorted(gardes), "fichiers_ignores": ignores, "octets_texte": total}


def lire_latex(chemin: Path) -> tuple[str, str]:
    """Texte d'un fichier de source et son encodage (UTF-8, sinon Latin-1, consigné)."""
    octets = chemin.read_bytes()
    try:
        return octets.decode("utf-8"), "utf-8"
    except UnicodeDecodeError:
        return octets.decode("latin-1"), "latin-1"


_COMMENTAIRE = re.compile(r"(?<!\\)%[^\n]*")


def retirer_commentaires(texte: str) -> str:
    """Retire chaque commentaire (de « % » non échappé à la fin de la ligne) ; garde les sauts de ligne."""
    return _COMMENTAIRE.sub("", texte)


_DOCCLASS = re.compile(r"\\documentclass")
_DEBUT_DOC = re.compile(r"\\begin\s*\{document\}")
_INCLUSION = re.compile(
    r"\\(?:input|include|subfile)\s*\{\s*(?P<a>[^{}]+?)\s*\}"
    r"|\\(?:import|subimport|inputfrom|includefrom|subinputfrom|subincludefrom)\s*\{\s*(?P<d>[^{}]*?)\s*\}\s*\{\s*(?P<f>[^{}]+?)\s*\}"
    r"|\\input\s+(?P<n>[A-Za-z0-9_./-]+)")


def fichier_principal(dossier: Path, fichiers: list[str]) -> tuple[str, list[str]]:
    candidats = []
    for f in fichiers:
        if not f.lower().endswith(".tex"):
            continue
        t = retirer_commentaires(lire_latex(dossier / f)[0])
        if _DOCCLASS.search(t) and _DEBUT_DOC.search(t):
            candidats.append(f)
    if not candidats:
        raise SourceRefusee("aucun fichier principal (\\documentclass et \\begin{document})")
    if len(candidats) == 1:
        return candidats[0], candidats
    usuels = [c for c in candidats if PurePosixPath(c).name.lower() in NOMS_PRINCIPAUX]
    if len(usuels) == 1:
        return usuels[0], candidats
    # sinon : le plus long texte aplati, puis l'ordre alphabétique (déterministe)
    tailles = sorted(((-len(aplatir(dossier, c)[0]), c) for c in candidats))
    return tailles[0][1], candidats


def aplatir(dossier: Path, principal: str) -> tuple[str, dict]:
    """Texte du fichier principal, commentaires retirés, inclusions remplacées par leur contenu."""
    base = dossier.resolve()
    inclus, manquants, encodages = [], [], {}

    def resoudre(rel_dir: PurePosixPath, nom: str) -> Path | None:
        for essai in (nom, nom + ".tex"):
            p = (dossier / rel_dir / essai).resolve()
            if not str(p).startswith(str(base) + "/"):
                return None
            if p.is_file():
                return p
        return None

    def lire(chemin: Path, import_dir: PurePosixPath, profondeur: int) -> str:
        if profondeur > PROFONDEUR_MAX:
            raise SourceRefusee(f"inclusions imbriquées au-delà de {PROFONDEUR_MAX} niveaux")
        texte, enc = lire_latex(chemin)
        encodages[str(chemin.relative_to(base))] = enc
        texte = retirer_commentaires(texte)

        def remplacer(m: re.Match) -> str:
            if m["a"] is not None:
                rel, nom = import_dir, m["a"]
            elif m["f"] is not None:
                rel, nom = import_dir / m["d"], m["f"]
            else:
                rel, nom = import_dir, m["n"]
            cible = resoudre(rel, nom)
            if cible is None:
                manquants.append(str(rel / nom))
                return ""
            inclus.append(str(cible.relative_to(base)))
            sous_dir = PurePosixPath(cible.relative_to(base).parent.as_posix()) if m["f"] is not None else import_dir
            return "\n" + lire(cible, sous_dir, profondeur + 1) + "\n"

        return _INCLUSION.sub(remplacer, texte)

    texte = lire((dossier / principal).resolve(), PurePosixPath("."), 0)
    return texte, {"inclus": inclus, "manquants": manquants, "encodages": encodages}


def chemin_pandoc() -> Path:
    import pypandoc

    p = Path(pypandoc.__file__).parent / "files" / "pandoc"
    if not p.is_file():
        raise GardeArret("pandoc absent : la roue pypandoc_binary (requirements-donnees.txt) est attendue")
    return p


def version_pandoc() -> str:
    r = subprocess.run([str(chemin_pandoc()), "--version"], capture_output=True, text=True, timeout=60)
    return r.stdout.splitlines()[0] if r.returncode == 0 and r.stdout else "illisible"


def convertir(source: Path, sortie: Path, filtre: Path, delai_s: int = DELAI_PANDOC_S) -> dict:
    """LaTeX aplati → markdown, en bac à sable ; figures retirées par le filtre."""
    commande = [str(chemin_pandoc()), "--sandbox", "-s", "-f", "latex", "-t", FORMAT_SORTIE, "--wrap=none",
                "--lua-filter", str(filtre), str(source), "-o", str(sortie)]
    try:
        r = subprocess.run(commande, capture_output=True, text=True, timeout=delai_s)
    except subprocess.TimeoutExpired:
        raise SourceRefusee(f"pandoc : délai de {delai_s} s dépassé") from None
    if r.returncode != 0:
        raise SourceRefusee(f"pandoc a échoué (code {r.returncode}) : {r.stderr.strip()[-300:]}")
    return {"avertissements_pandoc": r.stderr.count("[WARNING]")}


def traiter_papier(entree: dict, racine_donnees: Path, filtre: Path, ouvrir=ouvrir_https, pause: float = PAUSE_S,
                   dormir=time.sleep, essais: int = 4, journal: list | None = None) -> dict:
    """Fiche d'un papier : gardé (textes et empreintes) ou exclu (motif)."""
    idv = f"{entree['id']}v{entree['version']}"
    fiche = {"id": entree["id"], "version": entree["version"], "titre": entree["titre"]}
    try:
        octets = _avec_reprises(ouvrir, SOURCE.format(idv), essais, pause, dormir, journal if journal is not None else [])
    except urllib.error.HTTPError as e:
        return {**fiche, "statut": "exclu", "motif": f"source indisponible (HTTP {e.code})"}
    fiche.update(source_sha256=sha256(octets), source_octets=len(octets))
    try:
        nature, brut = nature_source(octets)
        fiche["nature"] = nature
        if nature == "pdf":
            raise SourceRefusee("source PDF seulement")
        if nature == "inconnu":
            raise SourceRefusee("format de source inconnu")
        dossier = racine_donnees / "sources" / idv
        if nature == "tar":
            info = extraire_textes(brut, dossier)
        else:
            dossier.mkdir(parents=True, exist_ok=False)
            (dossier / "source.tex").write_bytes(brut)
            info = {"fichiers_texte": ["source.tex"], "fichiers_ignores": 0, "octets_texte": len(brut)}
        fiche.update(info)
        principal, candidats = fichier_principal(dossier, info["fichiers_texte"])
        texte, inclusions = aplatir(dossier, principal)
        fiche.update(principal=principal, principaux_candidats=candidats, inclusions=inclusions)
        aplati = racine_donnees / "aplatis" / f"{idv}.tex"
        aplati.parent.mkdir(parents=True, exist_ok=True)
        if aplati.exists():
            raise GardeArret(f"{aplati} existe déjà : R12 interdit d'écraser")
        aplati.write_text(texte, encoding="utf-8")
        md = racine_donnees / "textes" / f"{idv}.md"
        md.parent.mkdir(parents=True, exist_ok=True)
        if md.exists():
            raise GardeArret(f"{md} existe déjà : R12 interdit d'écraser")
        fiche.update(convertir(aplati, md, filtre))
        contenu = md.read_text(encoding="utf-8")
        fiche.update(aplati_sha256=sha256(aplati.read_bytes()), texte_sha256=sha256(md.read_bytes()),
                     caracteres=len(contenu))
        if not (CARACTERES_MIN <= len(contenu) <= CARACTERES_MAX):
            raise SourceRefusee(f"texte converti de {len(contenu)} caractères, hors de [{CARACTERES_MIN}, {CARACTERES_MAX}]")
        fiche["statut"] = "gardé"
    except SourceRefusee as e:
        fiche.update(statut="exclu", motif=str(e))
    return fiche


def constituer(ordre: list[str], entrees: dict[str, dict], besoin: int, racine_donnees: Path, filtre: Path,
               ouvrir=ouvrir_https, pause: float = PAUSE_S, dormir=time.sleep, journal: list | None = None) -> list[dict]:
    """Parcourt l'ordre du tirage jusqu'à `besoin` papiers gardés ; chaque fiche porte son rang."""
    fiches, gardes = [], 0
    for rang, pid in enumerate(ordre):
        if gardes >= besoin:
            break
        if rang:
            dormir(pause)
        fiche = traiter_papier(entrees[pid], racine_donnees, filtre, ouvrir, pause, dormir, journal=journal)
        fiche["rang_tirage"] = rang
        if fiche["statut"] == "gardé":
            fiche["rang_garde"] = gardes
            gardes += 1
        fiches.append(fiche)
    return fiches


# --- run de sélection ------------------------------------------------------------------------------------

def _main(argv: list[str]) -> int:
    from importlib import metadata

    from ..manifeste import creer_manifeste, ecrire_resultat, lire_manifeste
    from ..scellement import sceller

    ap = argparse.ArgumentParser(prog="python -m controle_ia.environnements.corpus_arxiv")
    sous = ap.add_subparsers(dest="commande", required=True)
    s = sous.add_parser("selectionner", help="sélection et chaîne de données selon la règle scellée")
    s.add_argument("--regle", required=True)
    s.add_argument("--run-id", required=True)
    s.add_argument("--donnees", required=True, help="dossier neuf sous donnees/ (ignoré par git)")
    s.add_argument("--besoin", type=int, default=96)
    s.add_argument("--taille-page", type=int, default=1000)
    a = ap.parse_args(argv)

    racine = Path(".")
    donnees = Path(a.donnees)
    if donnees.exists():
        raise GardeArret(f"{donnees} existe déjà : un run de sélection prend un dossier neuf (R12)")
    entropie, regle_sha = entropie_de_regle(a.regle)
    config = {"tache": "T0.5 sélection des papiers", "regle": a.regle, "regle_sha256": regle_sha,
              "requete": REQUETE_V1, "categories_principales": list(CATEGORIES_PRINCIPALES), "dates_v1": list(DATES_V1),
              "conference": CONFERENCE.pattern, "refus_commentaire": REFUS_COMMENTAIRE.pattern,
              "sujets_exclus": SUJETS_EXCLUS.pattern, "extensions_texte": sorted(EXTENSIONS_TEXTE),
              "bornes_caracteres": [CARACTERES_MIN, CARACTERES_MAX], "format_pandoc": FORMAT_SORTIE,
              "filtre_lua": FILTRE_LUA, "pandoc": version_pandoc(),
              "pypandoc_binary": metadata.version("pypandoc_binary"), "besoin": a.besoin, "taille_page": a.taille_page,
              "pause_s": PAUSE_S, "donnees": str(donnees)}
    chemin_m, manifeste = creer_manifeste(racine, a.run_id, config, ["tirage-corpus"], entropie=entropie,
                                          commande="python -m controle_ia.environnements.corpus_arxiv " + " ".join(argv))
    journal: list = []
    pages, entrees, journal_api = interroger(REQUETE_V1, a.taille_page)
    journal.extend(journal_api)
    dossier_diag = racine / "diag" / a.run_id
    dossier_diag.mkdir(parents=True, exist_ok=True)
    for k, p in enumerate(pages):
        chemin = dossier_diag / f"api-page-{k:02d}.xml"
        chemin.write_bytes(p)
        sceller(chemin)
    candidats, exclus = filtrer(entrees)
    # les entrées complètes (métadonnées, licence CC0) restent dans les pages scellées de l'API
    ecrire_resultat(racine, chemin_m, "candidats", {"total_api": len(entrees), "candidats": [e["id"] for e in candidats],
                                                    "exclus": exclus})
    ordre = ordre_de_tirage([e["id"] for e in candidats], manifeste["graines"]["tirage-corpus"])
    ecrire_resultat(racine, chemin_m, "tirage", {"ordre": ordre, "graine": manifeste["graines"]["tirage-corpus"]})
    donnees.mkdir(parents=True)
    filtre = donnees / "sans-figures.lua"
    filtre.write_text(FILTRE_LUA, encoding="utf-8")
    par_id = {e["id"]: e for e in candidats}
    fiches = constituer(ordre, par_id, a.besoin, donnees, filtre, journal=journal)
    gardes = [f for f in fiches if f["statut"] == "gardé"]
    resume = {"examines": len(fiches), "gardes": len(gardes), "exclus": len(fiches) - len(gardes),
              "pilote": [f"{f['id']}v{f['version']}" for f in gardes[:64]],
              "reserve": [f"{f['id']}v{f['version']}" for f in gardes[64:]],
              "motifs": sorted({f.get("motif") for f in fiches if f["statut"] == "exclu"}), "journal_reseau": journal}
    ecrire_resultat(racine, chemin_m, "corpus", {"resume": resume, "fiches": fiches})
    lire_manifeste(chemin_m)
    print(json.dumps({k: v for k, v in resume.items() if k not in ("pilote", "reserve", "journal_reseau")},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
