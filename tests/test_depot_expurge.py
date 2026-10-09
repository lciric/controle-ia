"""Copie expurgée du dépôt (`scripts/depot_expurge.py`, R-104, R-105) : l'appariement des retraits ne traverse pas
les dossiers, aucun fichier que le code charge n'est retiré, et aucun fichier retiré ne survit dans une archive gardée
(cas sain et artefact, R5)."""
from __future__ import annotations

import gzip
import hashlib
import importlib.util
import io
import subprocess
import tarfile
import zipfile
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("depot_expurge", RACINE / "scripts" / "depot_expurge.py")
de = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(de)


def test_appariement_par_segment():
    assert de.correspond("docs/sources/invites-2606.07054-v1/invites/B1.txt",
                         "docs/sources/invites-2606.07054-v1/invites/*.txt")       # appariement par segment
    assert not de.correspond("docs/sources/invites-2606.07054-v1/derivees/B1-env-a-v1.txt",
                             "docs/sources/invites-2606.07054-v1/*.txt")          # le défaut de la première version
    assert not de.correspond("docs/sources/invites-2606.07054-v1/verification.txt",
                             "docs/sources/invites-2606.07054-v1/invites/*.txt")
    assert de.correspond("donnees/run/sorties.tar", "donnees/**")
    assert not de.correspond("donnees-bis/x", "donnees/**")


def test_fichiers_charges_par_le_code_jamais_retires():
    suivis = subprocess.run(["git", "-C", str(RACINE), "ls-files"], capture_output=True, text=True,
                            check=True).stdout.split("\n")
    charges = [f for f in suivis if any(de.correspond(f, g) for g in de.GARDES)]
    assert len(charges) == 34                       # invites des deux papiers (18 + 7) et gabarits adaptés (6), index
    assert all(de.motif_de(f) is None for f in charges)


def test_retrait_d_un_fichier_charge_arrete(monkeypatch):
    monkeypatch.setattr(de, "RETRAITS", de.RETRAITS + [("docs/sources/invites-2606.07054-v1/derivees/*.txt", "x")])
    with pytest.raises(SystemExit, match="chargé par le code"):
        de.motif_de("docs/sources/invites-2606.07054-v1/derivees/B1-env-a-v1.txt")


def _zip(membres: dict[str, bytes]) -> bytes:
    tampon = io.BytesIO()
    with zipfile.ZipFile(tampon, "w") as z:
        for nom, contenu in membres.items():
            z.writestr(nom, contenu)
    return tampon.getvalue()


def _tar(membres: dict[str, bytes]) -> bytes:
    tampon = io.BytesIO()
    with tarfile.open(fileobj=tampon, mode="w") as t:
        for nom, contenu in membres.items():
            info = tarfile.TarInfo(nom)
            info.size = len(contenu)
            t.addfile(info, io.BytesIO(contenu))
    return tampon.getvalue()


def _git_factice(depot: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(depot), "-c", "user.name=essai", "-c", "user.email=essai@invalid",
                    "-c", "commit.gpgsign=false", *args], check=True, capture_output=True)


def test_fichier_retire_survivant_dans_une_archive(tmp_path):
    retire = b"page d'un papier de tiers"
    empreintes = {hashlib.sha256(retire).hexdigest(), hashlib.sha256(b"").hexdigest()}
    assert de.survivants("a.zip", _zip({"notes.md": b"notre texte", "vide.txt": b""}), empreintes) == []  # cas sain
    assert de.survivants("a.zip", _zip({"autre/nom.txt": retire}), empreintes) == ["a.zip!autre/nom.txt"]   # par empreinte
    assert de.survivants("a.tar", _tar({"./docs/sources/pdf/2601.00001v1.pdf": b"x"}), empreintes) == [
        "a.tar!docs/sources/pdf/2601.00001v1.pdf"]                                                           # par chemin
    assert de.survivants("a.zip", _zip({"dedans.tar": _tar({"p.txt": retire})}), empreintes) == [
        "a.zip!dedans.tar!p.txt"]                                                                            # imbriqué
    with pytest.raises(SystemExit, match="format non examiné"):
        de.survivants("a.zip", _zip({"b.gz": gzip.compress(retire)}), empreintes)
    # paquet git : un fichier retiré du dernier commit mais présent dans l'historique est trouvé
    depot = tmp_path / "depot"
    depot.mkdir()
    _git_factice(depot, "init", "-q", "-b", "main")
    (depot / "docs/sources/pdf").mkdir(parents=True)
    (depot / "docs/sources/pdf/2601.00001v1.pdf").write_bytes(b"%PDF de tiers")
    _git_factice(depot, "add", "-A")
    _git_factice(depot, "commit", "-q", "-m", "1")
    _git_factice(depot, "rm", "-q", "docs/sources/pdf/2601.00001v1.pdf")
    (depot / "a.md").write_text("notre texte", encoding="utf-8")
    _git_factice(depot, "add", "-A")
    _git_factice(depot, "commit", "-q", "-m", "2")
    _git_factice(depot, "bundle", "create", "-q", str(tmp_path / "p.bundle"), "main")
    assert de.survivants("p.bundle", (tmp_path / "p.bundle").read_bytes(), set()) == [
        "p.bundle!docs/sources/pdf/2601.00001v1.pdf"]


def _depot_factice(depot: Path, copie_cachee: bool, compresse: bool = False) -> None:
    depot.mkdir()
    _git_factice(depot, "init", "-q", "-b", "main")
    (depot / "README.md").write_text("# essai\n\n" + de.PARAGRAPHE_README + "\n", encoding="utf-8")
    (depot / "docs/sources/pdf").mkdir(parents=True)
    (depot / "docs/sources/pdf/2601.00001v1.pdf").write_bytes(b"%PDF copie d'un papier de tiers")
    (depot / "livrables/candidature-ea-funds-v1").mkdir(parents=True)        # retiré ; sa feuille de style reste ailleurs
    (depot / "livrables/candidature-ea-funds-v1/style.css").write_bytes(b"body { margin: 0 }")
    (depot / "livrables/rendu-v1").mkdir()
    (depot / "livrables/rendu-v1/style.css").write_bytes(b"body { margin: 0 }")
    membres = {"notes.md": b"notre texte", "rendu-v1/style.css": b"body { margin: 0 }"}
    if copie_cachee:
        membres["copie/papier.pdf"] = b"%PDF copie d'un papier de tiers"
    (depot / "livrables/rendu-v1.zip").write_bytes(_zip(membres))
    if compresse:
        (depot / "livrables/journal.txt.gz").write_bytes(gzip.compress(b"journal"))
    _git_factice(depot, "add", "-A")
    _git_factice(depot, "commit", "-q", "-m", "factice")


def test_copie_de_bout_en_bout_saine_puis_artefact(tmp_path, monkeypatch, capsys):
    _depot_factice(tmp_path / "sain", copie_cachee=False)
    monkeypatch.setattr(de, "RACINE", tmp_path / "sain")
    assert de.main(["HEAD", str(tmp_path / "sortie-sain")]) == 0
    (paquet,) = (tmp_path / "sortie-sain").glob("*.bundle")
    clone = tmp_path / "clone"
    subprocess.run(["git", "clone", "-q", str(paquet), str(clone)], check=True, capture_output=True)  # sans -b
    assert not (clone / "docs/sources/pdf/2601.00001v1.pdf").exists()
    assert (clone / "docs/sources/pdf/2601.00001v1.pdf").name in (clone / "EXPURGE.md").read_text(encoding="utf-8")
    assert (clone / "livrables/rendu-v1.zip").exists()
    assert de.REMPLACEMENT_README in (clone / "README.md").read_text(encoding="utf-8")

    _depot_factice(tmp_path / "artefact", copie_cachee=True)
    monkeypatch.setattr(de, "RACINE", tmp_path / "artefact")
    capsys.readouterr()
    assert de.main(["HEAD", str(tmp_path / "sortie-artefact")]) == 1
    assert "livrables/rendu-v1.zip!copie/papier.pdf" in capsys.readouterr().err
    assert list((tmp_path / "sortie-artefact").glob("*.bundle")) == []


def test_archive_d_un_format_non_examine_arrete(tmp_path, monkeypatch):
    _depot_factice(tmp_path / "gz", copie_cachee=False, compresse=True)
    monkeypatch.setattr(de, "RACINE", tmp_path / "gz")
    with pytest.raises(SystemExit, match="format non examiné"):
        de.main(["HEAD", str(tmp_path / "sortie-gz")])
    assert list((tmp_path / "sortie-gz").glob("*.bundle")) == []
