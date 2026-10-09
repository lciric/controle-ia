"""Copie expurgée du dépôt, à montrer à des évaluateurs (décision de Lazar, R-104).

Un seul commit, reproductible, tiré d'un commit cité du dépôt : sans les textes de tiers dont le code n'a pas besoin
(PDF d'arXiv, pages extraites par les lecteurs, texte complet ou extrait d'un papier, pages des cartes de modèles,
fichiers de travail des relecteurs de l'extraction, sorties de l'extraction), sans la candidature à un autre fonds.
Les empreintes des fichiers retirés restent, et `EXPURGE.md` les liste. Les invites transcrites ou adaptées que le
code et ses tests chargent restent, avec leur source : le README de la copie le dit. Avant d'écrire le paquet, le
script vérifie qu'aucun fichier retiré ne survit dans une archive gardée (zip, tar ou paquet git, à toute profondeur,
par empreinte et par chemin) ; une archive d'un format qu'il n'examine pas l'arrête.

Rien n'est poussé : le paquet git est écrit dans SORTIE. Sa mise en ligne sur un dépôt distant demande un GO de Lazar.
Le script n'écrit que dans SORTIE, qui ne doit pas exister ; il ne touche pas au dépôt.

    .venv/bin/python scripts/depot_expurge.py COMMIT SORTIE
"""
from __future__ import annotations

import fnmatch
import hashlib
import io
import json
import os
import subprocess
import sys
import tarfile
import tempfile
import zipfile
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]

# (motif sur le chemin suivi, motif du retrait) ; un fichier `.sha256` compagnon reste, sauf s'il est lui-même visé.
# Un `*` ne traverse pas les dossiers ; un motif qui finit par `/**` vise tout le dossier, à toute profondeur.
RETRAITS = [
    ("docs/sources/pdf/*.pdf", "copie d'un PDF d'arXiv de tiers"),
    ("docs/sources/lecture-pdf-niveau1/*.tar", "fichiers de travail d'un lecteur : pages extraites des PDF de tiers"),
    ("docs/sources/lecture-pdf-niveau2/*.tar", "fichiers de travail d'un lecteur : pages extraites des PDF de tiers"),
    ("docs/sources/invites-2606.08892-v1/extrait.tar", "texte complet extrait d'un papier de tiers"),
    ("docs/sources/invites-2606.07054-v1/*.tar", "texte extrait d'un papier de tiers"),
    ("docs/sources/invites-2606.07054-v1/derivees/contre-verification-v1/*.tar",
     "fichiers de travail d'une contre-vérification : texte extrait d'un papier de tiers"),
    ("docs/sources/cartes-modeles-20261006/*.html", "page d'une carte de modèle (site tiers)"),
    ("docs/procedures/T0.5-extraction-v1/contre-lecture/*.tar", "fichiers de travail des relecteurs de l'extraction"),
    ("prereg/contre-lectures/T0.5-pilote-contre-lecture-1-verifications-v1.tar",
     "fichiers de travail d'un relecteur : pages extraites d'un PDF de tiers"),
    ("donnees/**", "sortie de l'extraction : texte dérivé de papiers de tiers"),
    ("livrables/candidature-ea-funds-v1/**", "candidature à un autre fonds, confidentielle"),
    ("livrables/candidature-ea-funds-v1.zip", "candidature à un autre fonds, confidentielle"),
    ("livrables/candidature-ea-funds-v1.zip.sha256", "candidature à un autre fonds, confidentielle"),
    ("registres/**", "registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116)"),
    ("livrables/reponse-amitie-v1/**", "textes d'une candidature (séminaire AFFINE), privés (R-116)"),
    ("livrables/reponse-amitie-v1.zip", "textes d'une candidature (séminaire AFFINE), privés (R-116)"),
    ("livrables/reponse-amitie-v1.zip.sha256", "textes d'une candidature (séminaire AFFINE), privés (R-116)"),
    ("livrables/anteriorite-niveau1-v1/decisions-v2.md", "copie du registre des décisions (R-116)"),
    ("livrables/premier-rendu-v1/decisions-v1.md", "copie du registre des décisions (R-116)"),
    ("livrables/anteriorite-niveau1-v1.zip", "archive qui contient les registres de travail (R-116)"),
    ("livrables/premier-rendu-v1.zip", "archive qui contient les registres de travail (R-116)"),
    ("livrables/controle-ia-v1.bundle", "paquet git qui contient les registres de travail (R-116)"),
]
# L'ancien paquet git (`livrables/controle-ia-v1.bundle`, cinq commits du 2026-10-04, recopié dans
# `livrables/premier-rendu-v1.zip`) reste : aucun fichier de son historique n'est visé ici (garde des archives).

# Paragraphe du README v3 et v4 sur les textes de tiers (R-112, R-113), remplacé dans la copie.
PARAGRAPHE_README = ("This repository holds copies of third-party material: arXiv PDFs (`docs/sources/pdf/`); working "
                     "files of the reader agents with pages extracted from those PDFs; the full text of arXiv 2606.08892 "
                     "and an extract of arXiv 2606.07054 (`extrait.tar` in `docs/sources/invites-2606.08892-v1/` and "
                     "`docs/sources/invites-2606.07054-v1/`); two model-card pages (`docs/sources/cartes-modeles-20261006/`); "
                     "and task-extraction outputs that contain text derived from the papers (`donnees/`). They remain under "
                     "their authors' licences: please do not reuse them.")
REMPLACEMENT_README = ("This copy omits the third-party material: the arXiv PDFs, the reader agents' working files with "
                       "pages extracted from them, the full text of arXiv 2606.08892 and the extract of arXiv 2606.07054, "
                       "the model-card pages and the task-extraction outputs; their SHA-256 hashes remain, and "
                       "`EXPURGE.md` lists every omitted file. It keeps the short prompt texts transcribed or adapted from "
                       "those two papers, because the code and its tests load them; they are attributed to their sources "
                       "and remain under their authors' licences.")

# Renvois du README vers les registres, absents de la copie (R-116) : remplacés s'ils sont présents.
REMPLACEMENTS_FACULTATIFS = [
    ("(my attestation: R-114 in `registres/decisions.md`)",
     "(my attestation, R-114, is recorded in the working registers, which this copy omits)"),
    ("4. The decision log and my approvals: `registres/decisions.md`, `registres/go.md`.",
     "4. The decision log and my approvals are kept in the working registers (`registres/`), which this copy omits."),
    ('Decisions are logged with their dates in `registres/decisions.md`, and my approvals in `registres/go.md`. Every working session ends with a sealed hand-over note in `registres/passations/`.',
     'Decisions are logged with their dates in the working registers (`registres/`), together with my approvals and a sealed hand-over note for every working session; this copy omits them.'),
    ('| `registres/` | Living registers: state, decisions, approvals, compute spending, instance stops, session hand-overs |',
     '| `registres/` | Living registers: state, decisions, approvals, compute spending, instance stops, session hand-overs (omitted from this copy) |'),
]


def _git(*args: str, cwd: Path | None = None, env: dict | None = None, entree: bytes | None = None) -> bytes:
    return subprocess.run(["git", *args], cwd=cwd or RACINE, env=env, input=entree, capture_output=True,
                          check=True).stdout


# fichiers que le code charge : jamais retirés (garde du script et de ses tests)
GARDES = ("docs/sources/invites-2606.08892-v1/invites/*.txt", "docs/sources/invites-2606.08892-v1/index.json",
          "docs/sources/invites-2606.07054-v1/invites/*.txt", "docs/sources/invites-2606.07054-v1/index.json",
          "docs/sources/invites-2606.07054-v1/derivees/*.txt", "docs/sources/invites-2606.07054-v1/derivees/index-v1.json")


def correspond(chemin: str, motif: str) -> bool:
    """Appariement par segment : `*` ne traverse pas les dossiers ; `/**` final vise tout le dossier."""
    if motif.endswith("/**"):
        return chemin.startswith(motif[:-2])
    c, m = chemin.split("/"), motif.split("/")
    return len(c) == len(m) and all(fnmatch.fnmatchcase(a, b) for a, b in zip(c, m))


def motif_de(chemin: str) -> str | None:
    for motif, raison in RETRAITS:
        if correspond(chemin, motif):
            if any(correspond(chemin, g) for g in GARDES):
                raise SystemExit(f"{chemin} : visé par « {motif} » mais chargé par le code : arrêt (aucun paquet écrit)")
            return raison
    return None


COMPRESSIONS_NON_EXAMINEES = (b"\x1f\x8b", b"BZh", b"\xfd7zXZ\x00", b"7z\xbc\xaf\x27\x1c", b"Rar!", b"\x28\xb5\x2f\xfd")


def est_archive(data: bytes) -> bool:
    return (data[:4] == b"PK\x03\x04" or data[257:262] == b"ustar"
            or data.startswith((b"# v2 git bundle", b"# v3 git bundle")))


def _membres_paquet(data: bytes) -> list[tuple[str, bytes]]:
    """(chemin, contenu) de chaque fichier de chaque commit d'un paquet git, historique compris."""
    with tempfile.TemporaryDirectory() as d:
        paquet, depot = Path(d) / "paquet.bundle", Path(d) / "depot.git"
        paquet.write_bytes(data)
        _git("init", "-q", "--bare", str(depot), cwd=Path(d))
        tetes = [l.split()[0] for l in _git("bundle", "unbundle", str(paquet), cwd=depot).decode().splitlines() if l]
        paires = set()
        for commit in _git("rev-list", *tetes, cwd=depot).decode().split():
            for ligne in _git("ls-tree", "-r", "-z", commit, cwd=depot).decode().split("\0"):
                if ligne:
                    meta, chemin = ligne.split("\t", 1)
                    if meta.split()[1] == "blob":
                        paires.add((chemin, meta.split()[2]))
        objets = sorted({sha for _, sha in paires})
        sortie, contenus, i = _git("cat-file", "--batch", cwd=depot, entree="\n".join(objets).encode() + b"\n"), {}, 0
        for sha in objets:
            fin = sortie.index(b"\n", i)
            taille = int(sortie[i:fin].split()[2])
            contenus[sha] = sortie[fin + 1:fin + 1 + taille]
            i = fin + 1 + taille + 1
        return sorted((chemin, contenus[sha]) for chemin, sha in paires)


def _membres(nom: str, data: bytes) -> list[tuple[str, bytes]]:
    if data[:4] == b"PK\x03\x04":
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            membres = [(i.filename, z.read(i)) for i in z.infolist() if not i.is_dir()]
    elif data[257:262] == b"ustar":
        with tarfile.open(fileobj=io.BytesIO(data)) as t:
            membres = [(m.name, t.extractfile(m).read()) for m in t.getmembers() if m.isfile()]
    elif data.startswith((b"# v2 git bundle", b"# v3 git bundle")):
        membres = _membres_paquet(data)
    elif data.startswith(COMPRESSIONS_NON_EXAMINEES):
        raise SystemExit(f"{nom} : archive d'un format non examiné : arrêt (aucun paquet écrit)")
    else:
        return []
    return [(m[2:] if m.startswith("./") else m, c) for m, c in membres]


def survivants(nom: str, data: bytes, empreintes: set[str]) -> list[str]:
    """Fichiers retirés qui survivent dans une archive gardée (zip, tar ou paquet git, à toute profondeur) : même
    empreinte qu'un fichier retiré, ou chemin visé par un retrait."""
    trouves = []
    for membre, contenu in _membres(nom, data):
        chemin = f"{nom}!{membre}"
        if (contenu and hashlib.sha256(contenu).hexdigest() in empreintes) or any(
                correspond(membre, motif) for motif, _ in RETRAITS):
            trouves.append(chemin)
        trouves += survivants(chemin, contenu, empreintes)
    return trouves


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    commit = _git("rev-parse", "--verify", argv[0] + "^{commit}").decode().strip()
    sortie = Path(argv[1]).resolve()
    if sortie.exists():
        print(f"{sortie} existe déjà : on n'écrase jamais (R12)", file=sys.stderr)
        return 2
    if RACINE.resolve() in (sortie, *sortie.parents):
        print("SORTIE ne doit pas être dans le dépôt", file=sys.stderr)
        return 2
    arbre = sortie / "controle-ia-expurge"
    arbre.mkdir(parents=True)
    retraits, gardes, archives, empreintes_gardees = [], 0, [], set()
    with tarfile.open(fileobj=io.BytesIO(_git("archive", "--format=tar", commit))) as tar:
        for membre in tar.getmembers():
            if not membre.isfile():
                continue
            contenu = tar.extractfile(membre).read()
            raison = motif_de(membre.name)
            if raison:
                retraits.append({"chemin": membre.name, "sha256": hashlib.sha256(contenu).hexdigest(),
                                 "octets": len(contenu), "motif": raison})
                continue
            cible = arbre / membre.name
            cible.parent.mkdir(parents=True, exist_ok=True)
            cible.write_bytes(contenu)
            os.chmod(cible, membre.mode & 0o777)
            gardes += 1
            empreintes_gardees.add(hashlib.sha256(contenu).hexdigest())
            if est_archive(contenu) or contenu.startswith(COMPRESSIONS_NON_EXAMINEES):
                archives.append((membre.name, contenu))
    # un contenu retiré qui reste aussi en fichier gardé (la feuille de style commune aux deux propositions) n'est pas
    # caché par une archive : seuls comptent les contenus que la copie n'a plus
    empreintes = {r["sha256"] for r in retraits if r["octets"]} - empreintes_gardees
    trouves = [t for nom, contenu in archives for t in survivants(nom, contenu, empreintes)]
    if trouves:
        print("fichiers retirés qui survivent dans une archive gardée : arrêt (aucun paquet écrit)\n  "
              + "\n  ".join(trouves), file=sys.stderr)
        return 1
    readme = arbre / "README.md"
    texte = readme.read_text(encoding="utf-8")
    if texte.count(PARAGRAPHE_README) != 1:
        print("paragraphe du README introuvable : arrêt (aucun paquet écrit)", file=sys.stderr)
        return 1
    texte = texte.replace(PARAGRAPHE_README, REMPLACEMENT_README)
    for avant, apres in REMPLACEMENTS_FACULTATIFS:
        if texte.count(avant) > 1:
            print(f"renvoi du README ambigu : {avant!r} : arrêt (aucun paquet écrit)", file=sys.stderr)
            return 1
        texte = texte.replace(avant, apres)
    readme.write_text(texte, encoding="utf-8")
    pdf = sorted(r["chemin"] for r in retraits if r["chemin"].startswith("docs/sources/pdf/"))
    lignes = ["# What this copy omits", "",
              f"Copy of the private repository `controle-ia` at commit `{commit}`, made for evaluators by "
              "`scripts/depot_expurge.py` (same commit). Third-party texts that the code does not need are omitted, "
              "together with an application to another funder, the working registers (`registres/`, which quote private messages) and the texts of another application. Their SHA-256 hashes remain (companion `.sha256` "
              "files, and the table below), so anyone holding the originals can check them. Before writing the "
              f"copy, the script checked that no omitted file survives inside a kept archive ({len(archives)} files in "
              "zip, tar or git bundle format, Word and NumPy files included, searched at any depth, by hash and "
              "by path).", "",
              "`python -m controle_ia.scellement verifier-arbre .` reports each omitted sealed file as an orphan "
              "hash; that is expected. The README's paragraph on third-party material was adapted for this copy.", "",
              f"- Files kept: {gardes}. Files omitted: {len(retraits)} ({sum(r['octets'] for r in retraits) / 1e6:.1f} MB).",
              "- Kept on purpose: the prompt texts transcribed from arXiv 2606.08892 "
              "(`docs/sources/invites-2606.08892-v1/invites/`) and from arXiv 2606.07054 "
              "(`docs/sources/invites-2606.07054-v1/invites/`), and the templates adapted from the latter "
              "(`docs/sources/invites-2606.07054-v1/derivees/`): the code and its tests load them after checking "
              "their hashes.", "",
              "## arXiv papers whose PDF copies are omitted", ""]
    lignes += [f"- [{Path(p).stem}](https://arxiv.org/abs/{Path(p).stem})" for p in pdf]
    lignes += ["", "## Omitted files", "", "| path | SHA-256 | reason (in French) |", "|---|---|---|"]
    lignes += [f"| `{r['chemin']}` | `{r['sha256']}` | {r['motif']} |" for r in retraits]
    (arbre / "EXPURGE.md").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    date = _git("show", "-s", "--format=%cI", commit).decode().strip()
    env = dict(os.environ, GIT_AUTHOR_NAME="controle-ia (copie expurgée)", GIT_AUTHOR_EMAIL="copie-expurgee@invalid",
               GIT_COMMITTER_NAME="controle-ia (copie expurgée)", GIT_COMMITTER_EMAIL="copie-expurgee@invalid",
               GIT_AUTHOR_DATE=date, GIT_COMMITTER_DATE=date)
    _git("init", "-q", "-b", "main", cwd=arbre, env=env)
    _git("add", "-A", cwd=arbre, env=env)
    _git("-c", "commit.gpgsign=false", "commit", "-q", "-m",
         f"Copie expurgée de controle-ia au commit {commit} (textes de tiers omis ; voir EXPURGE.md)", cwd=arbre, env=env)
    copie = _git("rev-parse", "HEAD", cwd=arbre).decode().strip()
    paquet = sortie / f"controle-ia-expurge-{commit[:7]}.bundle"
    _git("bundle", "create", "-q", str(paquet), "HEAD", "main", cwd=arbre, env=env)
    bilan = {"commit_source": commit, "commit_copie": copie, "fichiers_gardes": gardes, "fichiers_retires": len(retraits),
             "archives_examinees": len(archives),
             "paquet": paquet.name, "paquet_sha256": hashlib.sha256(paquet.read_bytes()).hexdigest(),
             "retraits": retraits}
    (sortie / "bilan.json").write_text(json.dumps(bilan, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in bilan.items() if k != "retraits"}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
