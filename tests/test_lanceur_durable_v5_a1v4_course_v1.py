"""Essais neufs du lanceur durable v5 d'A1-v4 pour la course (m-2 et M-1 de la contre-lecture `260ec3f9…` ; R12 : fichier neuf,
`tests/test_lanceur_durable_v5_a1v4.py` inchangé).

Ce que ces essais exercent, que les essais commités n'exercent pas :
- la **configuration des mondes (ii) v2** livrée (`configuration-mondes-variante-ii-v2.json`, `1eaa090d…`) **avec son compagnon** ;
- le **texte scellé** `d306a8fa…`, lu sous son nom public dans le **second commit public** reconstitué ici depuis le paquet
  `commit-public-code-v5-a1-v4-v2.bundle` (sur `8947bc80…` du clone local `/home/user/ideation-organism`) : `verifier-texte` du
  lanceur durable (en fichier seul, comme le pilote) et `lire_preenregistrement` du lanceur gelé v5 ; préalables de M-2 et M-3 ;
- **M-1 sur le registre réel** : GO-2026-11-08-12 accepté par `verifier_go_machine` et `verifier_texte` ; GO-2026-11-08-14 accepté
  par `verifier_go_machine` le 9 novembre mais refusé par `verifier_texte` (ligne `go_machine` du texte), et de même par
  `louer --verifier-seulement` (aucune location, aucun réseau : clés factices, offre factice).
Chaque garde : un cas sain et un artefact (R5). Si le paquet v2, son compagnon ou le clone public local manquent, les essais qui en
dépendent sont **sautés avec leur raison écrite**, jamais réussis en silence.

Lancement (racine du dépôt privé, `.venv` actif) :
    PYTHONPATH=src python -m pytest -q -p no:cacheprovider tests/test_lanceur_durable_v5_a1v4_course_v1.py
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from controle_ia import hote_durable_a1_v3 as h
from controle_ia import hote_durable_a1_v4_v5 as v5

RACINE = Path(__file__).resolve().parents[1]
GARDE = RACINE / ".claude" / "hooks" / "garde_calcul.py"
REGISTRE = RACINE / "registres" / "go.md"
DOSSIER = RACINE / "docs/notes/ideation-organisme-v1/a1-v4-reprise-v9"
CONF_II_V2 = DOSSIER / "lanceur-durable-v5" / "configuration-mondes-variante-ii-v2.json"
CONF_II_V1 = DOSSIER / "lanceur-durable-v5" / "configuration-mondes-variante-ii-v1.json"
TEXTE_PRIVE = DOSSIER / "preenregistrement-attaque-goodhart-v5-v1.md"
PAQUET_V2 = DOSSIER / "commit-public-code-v5-a1-v4-v2.bundle"
CLONE_LOCAL = Path("/home/user/ideation-organism")
MODULE = RACINE / "src" / "controle_ia" / "hote_durable_a1_v4_v5.py"

SHA_TEXTE = "d306a8faa45b3d77f1edb653406ced1facd4752b2aa00c2e77593538399a7fe6"
SHA_CONF_II_V2 = "1eaa090d59ee9d3c96eaf93cdf9913bf831633d7bbf4a2bc29dbe5e4172c7587"
SHA_MODULE = "352380923e612e3456f4c533d2e2e61af5e7b1a69bd2f99bc5ab39c24beebae2"
COMMIT_BASE = "8947bc80a5c2fee0cfee4f3cafbdaaca8ed77f3e"  # tête du dépôt public avant le code v5
COMMIT_CODE = "b8c1db3add7cdda7fee876944c1e8f692a568e98"  # code v5 et lecteur de l'épreuve (commit_code_gele de la (ii) v2)
COMMIT_PUBLIC = "f39a7f4ab9e3da1e11629b1be329304cd5b8a1b0"  # second commit public : texte scellé et compagnon par-dessus
TETE_PAQUET = "refs/heads/a1-v4-v5-texte-scelle"
COMMIT_X = "52b39cbb51edc94f6ade9be79d8b4e06570576a2"  # commit privé du lanceur durable v5 à ses chemins d'exécution (R-1959)
COMMIT_TEMOIN = "c2255bd1ee044dd680c0a065eac923f9348fc683"  # livraison, sans l'amorce à son chemin d'exécution (témoin de R-1959)
COMMIT_REGISTRE = "740f49e2b27344b3188f9aba20b5f0115c3468ab"
NOM_TEXTE = "orchestrator/prereg/preenregistrement-attaque-goodhart-v5-v1.md"
GO_M, GO_14, GO_C = "GO-2026-11-08-12", "GO-2026-11-08-14", "GO-2026-11-02-22"
LE_9, LE_10 = dt.date(2026, 11, 9), dt.date(2026, 11, 10)
MAINTENANT = dt.datetime(2026, 11, 9, 3, 0, 0, tzinfo=dt.timezone.utc)
# M-2, point 1 : chemins exigés au commit privé et leurs empreintes (texte scellé § 8 ; contre-lecture § 5, point 6)
AU_COMMIT_PRIVE = {
    "scripts/amorce_hote_durable_a1_v4_v5.sh": "745040bf9a3a0fc5049cc41b9ad13f29e4776370819095edb021724c914b38ca",
    "src/controle_ia/hote_durable_a1_v4_v5.py": SHA_MODULE,
    "src/controle_ia/hote_durable_a1_v3.py": "5b853fde8987a472a191f769415068ecc15f1da8a042767bba4229dd5c29e0b1",
    "src/controle_ia/hote_durable_a1_v3_v4.py": "8101d33bdc259860290feb9a35fb3a93d50df06c84a4268a105f86a973ceef3f",
    "src/controle_ia/sonde_hote_durable_a1_v3.py": "f7c7f79ba974dd1e38743265caf88f09ce7d4d96ea4676f6d66e75cc9ebca69d",
    "src/controle_ia/sonde_hote_durable_a1_v3_v10.py": "37b70a0646874e3769a9e45ccf1438121f2126aecc8307234c3cc590f122b81c",
    "docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/lanceur-durable-v5/configuration-mondes-variante-ii-v2.json": SHA_CONF_II_V2,
    "docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/lanceur-durable-v5/configuration-mondes-variante-ii-v2.json.sha256":
        "e18d646ffd2f581294e304807193fbdc4d50952ec864a5dd6da0db070eb3e31f",
}
CLE_FACTICE, JETON_FACTICE, VAST_FACTICE = "cle-factice-argon-course-v1-QWERTY", "ghp_factice_course_v1_0123456789", "vast-factice-v1"
OFFRE = {"id": 77, "resource_type": "gpu", "num_gpus": 1, "gpu_name": "GTX_1070", "dph_total": 0.062, "cpu_cores_effective": 8,
         "cpu_ram": 16000, "disk_space": 60, "reliability": 0.995, "geolocation": "FR", "machine_id": 9}


def sha(o: bytes) -> str:
    return hashlib.sha256(o).hexdigest()


def git(cwd, *args, check=True) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(cwd), *args], check=check, capture_output=True, text=True, timeout=120)


def raison_de_saut() -> str | None:
    if not PAQUET_V2.is_file():
        return f"paquet {PAQUET_V2.name} absent : second commit public non reconstituable ici"
    comp = Path(str(PAQUET_V2) + ".sha256")
    if not comp.is_file():
        return f"compagnon {comp.name} absent : paquet non scellé"
    if comp.read_text().split()[0] != sha(PAQUET_V2.read_bytes()):
        return None  # empreinte fausse : pas un saut, un échec (essai test_paquet_v2_scelle)
    if not (CLONE_LOCAL / ".git").is_dir():
        return f"clone local {CLONE_LOCAL} absent : la base {COMMIT_BASE[:8]} du paquet manque"
    if git(CLONE_LOCAL, "cat-file", "-e", f"{COMMIT_BASE}^{{commit}}", check=False).returncode != 0:
        return f"commit de base {COMMIT_BASE[:8]} absent du clone local"
    return None


@pytest.fixture(scope="module")
def public(tmp_path_factory):
    """Le second commit public reconstitué : clone local de `/home/user/ideation-organism`, base `8947bc80`, paquet v2 récupéré,
    tête détachée au commit public. Rend le chemin du clone (jetable, sous le dossier temporaire de l'essai)."""
    r = raison_de_saut()
    if r:
        pytest.skip(r)
    d = tmp_path_factory.mktemp("public-v2") / "ideation-organism"
    subprocess.run(["git", "clone", "-q", "--no-local", "--no-checkout", str(CLONE_LOCAL), str(d)], check=True, capture_output=True,
                   timeout=300)
    git(d, "fetch", "-q", str(PAQUET_V2), f"{TETE_PAQUET}:{TETE_PAQUET}")
    git(d, "checkout", "-q", "--detach", COMMIT_PUBLIC)
    return d


@pytest.fixture
def public_v1_seul(public, tmp_path):
    """Artefact de M-3 : le commit du code seul (`b8c1db3a`, celui du paquet v1), sans texte ni compagnon, dans une copie neuve."""
    d = tmp_path / "ideation-organism-v1-seul"
    subprocess.run(["git", "clone", "-q", "--no-local", "--no-checkout", str(public), str(d)], check=True, capture_output=True, timeout=300)
    git(d, "checkout", "-q", "--detach", COMMIT_CODE)
    return d


def verifier_texte_cli(texte: Path, sha_texte=SHA_TEXTE, conf=CONF_II_V2) -> subprocess.CompletedProcess:
    """`verifier-texte` en fichier seul (`python3 -I -B …/hote_durable_a1_v4_v5.py`), comme le pilote de l'ordre de course."""
    return subprocess.run([sys.executable, "-I", "-B", str(MODULE), "verifier-texte", "--texte", str(texte), "--sha-texte", sha_texte,
                           "--configuration-mondes", str(conf)], capture_output=True, text=True, timeout=300, cwd=str(RACINE))


def arguments_louer(texte: Path, journal: Path, offres: Path, verifier=True) -> argparse.Namespace:
    return argparse.Namespace(registre_main=str(REGISTRE), garde_main=str(GARDE), offres=str(offres), offre=str(OFFRE["id"]),
                              commit_prive=COMMIT_X, commit_public=COMMIT_PUBLIC, texte=str(texte), sha_texte=SHA_TEXTE,
                              configuration_mondes=str(CONF_II_V2), commit_registre=COMMIT_REGISTRE, journal_local=str(journal),
                              racine_privee=None, verifier_seulement=verifier)


def env_factice(go_machine=GO_M, go_id=None, **modif) -> dict:
    """Environnement du pilote, **valeurs factices seulement** (jamais `os.environ` : aucune clé réelle n'entre dans l'essai)."""
    e = {"GO_ID": go_machine if go_id is None else go_id, v5.NOM_GO_MACHINE_ENV: go_machine, v5.NOM_CLE_ARGON_PILOTE: CLE_FACTICE,
         "CONTROLE_IA_GITHUB_TOKEN_2": JETON_FACTICE, "VAST_API_KEY": VAST_FACTICE, "PATH": "/usr/bin:/bin", "HOME": "/root"}
    for k, v in modif.items():
        e.pop(k) if v is None else e.__setitem__(k, v)
    return e


# --- le module essayé est le module gelé ------------------------------------------------------------------------------------


def test_module_essaye_est_le_module_gele():
    assert Path(v5.__file__).resolve() == MODULE.resolve()
    assert sha(MODULE.read_bytes()) == SHA_MODULE


# --- configuration (ii) v2, avec son compagnon --------------------------------------------------------------------------------


def test_configuration_ii_v2_livree_avec_compagnon_saine():
    c = v5.lire_configuration_mondes(CONF_II_V2)
    assert c["sha256"] == SHA_CONF_II_V2 and c["variante"] == "ii" and c["mondes"] == ["W2", "W2g"] and c["mondes_texte"] == "W2 et W2g"
    assert c["lanceur_gele"] == "demonstrations/attaque_goodhart_v5.py" and c["dossier_sortie"] == "sortie-attaque-goodhart-v5"
    assert c["prefixe_texte"] == "preenregistrement-attaque-goodhart-v5-v" and c["etape_depense"] == "attaque_goodhart_v5/argon"
    assert c["commit_code_gele"] == COMMIT_CODE and c["go_course"] == GO_C and c["plafond_course_usd"] == 200.0
    assert len(c["fichiers_geles_publics"]) == 13
    assert {"pole/attaque_goodhart_v5.py", "demonstrations/attaque_goodhart_v5.py"} <= set(c["fichiers_geles_publics"])
    assert v5.nom_texte(1, c["prefixe_texte"]) == NOM_TEXTE


def test_configuration_ii_v2_artefacts(tmp_path):
    """Copie à un octet près, compagnon retiré, compagnon d'une autre configuration (la v1) : refus, jamais un repli."""
    copie = tmp_path / CONF_II_V2.name
    copie.write_bytes(CONF_II_V2.read_bytes())
    with pytest.raises(h.Refus, match="compagnon .sha256 absent"):
        v5.lire_configuration_mondes(copie)
    Path(str(copie) + ".sha256").write_bytes(Path(str(CONF_II_V2) + ".sha256").read_bytes())
    assert v5.lire_configuration_mondes(copie)["sha256"] == SHA_CONF_II_V2  # cas sain de la copie
    copie.write_bytes(CONF_II_V2.read_bytes().replace(b"W2 et W2g", b"W2 et W2G"))
    with pytest.raises(h.Refus, match="différente du compagnon"):
        v5.lire_configuration_mondes(copie)
    copie.write_bytes(CONF_II_V1.read_bytes())  # la v1 (lanceur gelé v4) sous le compagnon de la v2
    with pytest.raises(h.Refus, match="différente du compagnon"):
        v5.lire_configuration_mondes(copie)


# --- paquet v2 et second commit public (M-2, point 2 ; M-3) -----------------------------------------------------------------


def test_paquet_v2_scelle():
    if not PAQUET_V2.is_file() or not Path(str(PAQUET_V2) + ".sha256").is_file():
        pytest.skip(f"paquet {PAQUET_V2.name} ou son compagnon absent : rien à vérifier ici")
    assert Path(str(PAQUET_V2) + ".sha256").read_text().split()[0] == sha(PAQUET_V2.read_bytes())


def test_raison_de_saut_saine_et_artefacts(tmp_path, monkeypatch):
    """La garde de saut (R5) : rien à dire quand tout est là ; une raison écrite quand le paquet, son compagnon ou le clone local
    manquent ; aucune raison (donc un échec, pas un saut) quand le compagnon ne correspond pas."""
    if not PAQUET_V2.is_file() or not (CLONE_LOCAL / ".git").is_dir():
        pytest.skip("paquet v2 ou clone local absent : le cas sain de la garde de saut n'est pas jouable ici")
    assert raison_de_saut() is None
    mod, vrai = sys.modules[__name__], PAQUET_V2
    monkeypatch.setattr(mod, "PAQUET_V2", tmp_path / "absent.bundle")
    assert "absent" in raison_de_saut()
    faux = tmp_path / vrai.name
    faux.write_bytes(vrai.read_bytes())
    monkeypatch.setattr(mod, "PAQUET_V2", faux)
    assert "non scellé" in raison_de_saut()
    Path(str(faux) + ".sha256").write_text("0" * 64 + f"  {faux.name}\n")
    assert raison_de_saut() is None  # empreinte fausse : pas de saut ; test_paquet_v2_scelle échouerait
    Path(str(faux) + ".sha256").write_text(sha(faux.read_bytes()) + f"  {faux.name}\n")
    monkeypatch.setattr(mod, "CLONE_LOCAL", tmp_path / "pas-de-clone")
    assert "clone local" in raison_de_saut()


def test_second_commit_public_reconstitue(public):
    assert git(public, "rev-parse", "HEAD").stdout.strip() == COMMIT_PUBLIC
    assert git(public, "rev-parse", "HEAD^").stdout.strip() == COMMIT_CODE
    assert git(public, "rev-parse", "HEAD^^").stdout.strip() == COMMIT_BASE
    assert git(public, "status", "--porcelain").stdout == ""
    noms = git(public, "diff", "--name-status", COMMIT_CODE, COMMIT_PUBLIC).stdout.split("\n")
    assert [n for n in noms if n] == [f"A\t{NOM_TEXTE}", f"A\t{NOM_TEXTE}.sha256"]  # un seul commit, deux fichiers neufs


def test_m2_commit_public_descend_du_code_gele_sain_et_artefact(public):
    assert git(public, "merge-base", "--is-ancestor", COMMIT_CODE, COMMIT_PUBLIC, check=False).returncode == 0
    assert git(public, "merge-base", "--is-ancestor", COMMIT_CODE, COMMIT_BASE, check=False).returncode == 1  # la base n'en descend pas


def test_m3_texte_et_compagnon_au_commit_public(public):
    texte = subprocess.run(["git", "-C", str(public), "show", f"{COMMIT_PUBLIC}:{NOM_TEXTE}"], capture_output=True, check=True).stdout
    assert sha(texte) == SHA_TEXTE and texte == TEXTE_PRIVE.read_bytes()  # octet pour octet
    comp = subprocess.run(["git", "-C", str(public), "show", f"{COMMIT_PUBLIC}:{NOM_TEXTE}.sha256"], capture_output=True, check=True).stdout
    assert comp == Path(str(TEXTE_PRIVE) + ".sha256").read_bytes() and comp.split()[0].decode() == SHA_TEXTE
    assert v5.lire_compagnon(public / NOM_TEXTE) == SHA_TEXTE  # au format de `lire_compagnon`


def test_m3_artefact_commit_du_code_seul(public_v1_seul):
    """Au commit du paquet v1 (`b8c1db3a`), ni texte ni compagnon : `git show` et `verifier-texte` refusent ; texte posé sans compagnon :
    refus « compagnon .sha256 absent » (ce que la machine ferait après son signe de vie, M-2)."""
    assert git(public_v1_seul, "cat-file", "-e", f"{COMMIT_CODE}:{NOM_TEXTE}", check=False).returncode != 0
    r = verifier_texte_cli(public_v1_seul / NOM_TEXTE)
    assert r.returncode == 2 and "texte introuvable" in r.stderr
    shutil.copyfile(TEXTE_PRIVE, public_v1_seul / NOM_TEXTE)
    r = verifier_texte_cli(public_v1_seul / NOM_TEXTE)
    assert r.returncode == 2 and "compagnon .sha256 absent" in r.stderr


# --- texte scellé au commit public : verifier-texte et lanceur gelé v5 ---------------------------------------------------------


def test_verifier_texte_fichier_seul_code_0(public):
    r = verifier_texte_cli(public / NOM_TEXTE)
    assert r.returncode == 0, r.stderr
    t = json.loads(r.stdout)
    assert (t["version"], t["sha256"], t["mondes"], t["lignes_gelees"], t["plafond_usd"], t["go"], t["go_machine"], t["nom"]) == (
        1, SHA_TEXTE, "W2 et W2g", 79, 200.0, GO_C, GO_M, NOM_TEXTE)
    assert t["variante"] == "ii" and t["fichiers_geles_publics_egaux"] == 13 and t["configuration_sha256"] == SHA_CONF_II_V2


@pytest.mark.parametrize("cas, motif", [
    ("sha_autre", "différente de celle attendue"),
    ("conf_v1", "compagnon .sha256 absent"),
    ("fichier_gele_modifie", "fichier gelé modifié ou absent du clone public"),
    ("texte_modifie", "différente du compagnon"),
])
def test_verifier_texte_fichier_seul_artefacts(public, tmp_path, cas, motif):
    texte = public / NOM_TEXTE
    if cas == "sha_autre":
        r = verifier_texte_cli(texte, sha_texte="e" * 64)
    elif cas == "conf_v1":  # la (ii) v1 livrée, sans compagnon (lanceur gelé v4) : refusée
        r = verifier_texte_cli(texte, conf=CONF_II_V1)
    else:  # copie de travail neuve du commit public, retouchée
        d = tmp_path / "copie"
        subprocess.run(["git", "clone", "-q", "--no-local", "--no-checkout", str(public), str(d)], check=True, capture_output=True)
        git(d, "checkout", "-q", "--detach", COMMIT_PUBLIC)
        if cas == "fichier_gele_modifie":
            with open(d / "orchestrator" / "pole" / "attaque_goodhart_v5.py", "a", encoding="utf-8") as f:
                f.write("# retouche\n")
        else:
            with open(d / NOM_TEXTE, "a", encoding="utf-8") as f:
                f.write("\n")
        r = verifier_texte_cli(d / NOM_TEXTE)
    assert r.returncode == 2 and motif in r.stderr, r.stderr


def test_lanceur_gele_v5_accepte_le_texte(public):
    """`lire_preenregistrement` du lanceur gelé v5, depuis `orchestrator/` du commit public : entropie = entier de l'empreinte,
    empreinte rendue, 79 fichiers gelés égaux à `FICHIERS_GELES` (fermeture exacte vérifiée par le lanceur gelé lui-même)."""
    code = ("import sys, hashlib, json; sys.path.insert(0, '.')\n"
            "from demonstrations import attaque_goodhart_v5 as l5\n"
            f"p = {NOM_TEXTE.removeprefix('orchestrator/')!r}\n"
            "r = l5.lire_preenregistrement(p)\n"
            "s = hashlib.sha256(open(p, 'rb').read()).hexdigest()\n"
            "print(json.dumps({'entropie': r[0] == int(s, 16), 'empreinte': r[1], 'n': len(r[2]), 'n_geles': len(l5.FICHIERS_GELES),"
            " 'egaux': sorted(r[2]) == sorted(l5.FICHIERS_GELES), 'dose': r[3].get('dose_w2g'), 'go_machine': r[3].get('go_machine')}))\n")
    r = subprocess.run([sys.executable, "-I", "-B", "-c", code], cwd=str(public / "orchestrator"), capture_output=True, text=True, timeout=300)
    assert r.returncode == 0, r.stderr[-2000:]
    o = json.loads(r.stdout.strip().splitlines()[-1])
    assert o["entropie"] is True and o["empreinte"] == SHA_TEXTE and o["n"] == 79 == o["n_geles"] and o["egaux"] is True
    assert o["go_machine"] == GO_M
    assert git(public, "status", "--porcelain").stdout == ""  # -B : aucun fichier écrit dans le clone


def test_lanceur_gele_v5_refuse_un_compagnon_faux(public, tmp_path):
    d = tmp_path / "copie"
    subprocess.run(["git", "clone", "-q", "--no-local", "--no-checkout", str(public), str(d)], check=True, capture_output=True)
    git(d, "checkout", "-q", "--detach", COMMIT_PUBLIC)
    (d / f"{NOM_TEXTE}.sha256").write_text("0" * 64 + "  preenregistrement-attaque-goodhart-v5-v1.md\n")
    code = ("import sys; sys.path.insert(0, '.')\n"
            "from demonstrations import attaque_goodhart_v5 as l5\n"
            f"l5.lire_preenregistrement({NOM_TEXTE.removeprefix('orchestrator/')!r})\n")
    r = subprocess.run([sys.executable, "-I", "-B", "-c", code], cwd=str(d / "orchestrator"), capture_output=True, text=True, timeout=300)
    assert r.returncode != 0


# --- M-1 sur le registre réel ---------------------------------------------------------------------------------------------------


def test_m1_go_12_accepte_par_la_garde_de_la_machine_le_9_et_le_10():
    for jour in (LE_9, LE_10):
        g = v5.verifier_go_machine(REGISTRE, GARDE, GO_M, jour)
        assert g["plafond_usd"] == 35.0 and g["echeance"] == "2026-11-16" and g["go"] == GO_M


def test_m1_go_14_accepte_par_la_garde_de_la_machine_le_9_refuse_le_10():
    """La brèche de M-1 : le périmètre de GO-2026-11-08-14 porte « machine » et « A1-v4 » ; la garde de `main` l'admet jusqu'à son
    échéance (9 novembre), à 150 USD."""
    g = v5.verifier_go_machine(REGISTRE, GARDE, GO_14, LE_9)
    assert g["plafond_usd"] == 150.0 and g["echeance"] == "2026-11-09"
    with pytest.raises(h.Refus, match="hors de sa période"):
        v5.verifier_go_machine(REGISTRE, GARDE, GO_14, LE_10)


def test_m1_go_des_appels_exact_sur_le_registre_reel():
    assert v5.verifier_go_course(REGISTRE, GARDE, GO_C, LE_9)["plafond_usd"] == 200.0
    with pytest.raises(h.Refus, match="est la ligne des appels"):
        v5.verifier_go_machine(REGISTRE, GARDE, GO_C, LE_9)


def test_m1_verifier_texte_accepte_go_12_refuse_go_14(public):
    conf = v5.lire_configuration_mondes(CONF_II_V2)
    t = v5.verifier_texte(public / NOM_TEXTE, SHA_TEXTE, conf, GO_M)
    assert t["go_machine"] == GO_M and t["lignes_gelees"] == 79
    with pytest.raises(h.Refus, match=r"go_machine = 'GO-2026-11-08-12', la ligne vérifiée \(GO_ID_MACHINE\) est 'GO-2026-11-08-14'"):
        v5.verifier_texte(public / NOM_TEXTE, SHA_TEXTE, conf, GO_14)


# --- M-1 au niveau de `louer --verifier-seulement` (aucune création, aucun réseau, valeurs factices) ---------------------------


def _louer(public, tmp_path, environ, jour=LE_9, verifier=True):
    offres = tmp_path / "offres.json"
    offres.write_text(json.dumps([OFFRE]))
    journal = tmp_path / "journal-location.log"
    code = v5.louer(arguments_louer(public / NOM_TEXTE, journal, offres, verifier), client=object(), aujourd_hui=jour,
                    environ=environ, maintenant=MAINTENANT)
    contenu = journal.read_text(encoding="utf-8") if journal.exists() else ""
    for valeur in (CLE_FACTICE, JETON_FACTICE, VAST_FACTICE):
        assert valeur not in contenu  # journal masqué
    return code, contenu, journal


def test_louer_verifier_seulement_go_12_code_0(public, tmp_path):
    code, j, journal = _louer(public, tmp_path, env_factice())
    assert code == 0, j
    assert "machine GO-2026-11-08-12 (plafond lu 35 USD, échéance 2026-11-16)" in j and "GO-2026-11-02-22 (200 USD exact)" in j
    assert f"texte {NOM_TEXTE} : empreinte {SHA_TEXTE}" in j and "79 lignes gelées, 13 fichiers gelés publics égaux" in j
    assert f"configuration des mondes : variante (ii) ['W2', 'W2g'] ; {CONF_II_V2.relative_to(RACINE).as_posix()} {SHA_CONF_II_V2}" in j
    assert "garde de dépense (1/2)" in j and "garde de dépense (2/2, sur le corps)" in j
    noms = ("CHEMIN_CONFIGURATION_MONDES, CLE_ARGON, COMMIT_PRIVE, COMMIT_PUBLIC, COMMIT_REGISTRE, DEPOT_URL, ECHEANCE_UTC_S, GH_TOKEN, "
            "GO_ID, GO_MACHINE, NOM_TEXTE, PRIX_H_USD, SHA_CONFIGURATION_MONDES, SHA_TEXTE")
    assert f"vérification seulement : rien créé (variables : {noms})" in j  # quatorze noms, aucune variable du mandataire
    for suffixe in (".identifiant", ".creation-incertaine", ".etat.json"):
        assert not Path(str(journal) + suffixe).exists()  # rien créé, aucun marqueur de location


@pytest.mark.parametrize("environ, jour, motif", [
    (env_factice(GO_14), LE_9, "go_machine = 'GO-2026-11-08-12', la ligne vérifiée (GO_ID_MACHINE) est 'GO-2026-11-08-14'"),
    (env_factice(GO_14), LE_10, "hors de sa période"),
    (env_factice(GO_M, go_id=GO_C), LE_9, "GO_ID=GO-2026-11-08-12 exigé en tête"),
    (env_factice(GO_M, go_id=GO_14), LE_9, "GO_ID=GO-2026-11-08-12 exigé en tête"),
    (env_factice("GO-2026-11-05-03"), LE_9, "périmètre sans"),
    (env_factice(GO_M, GEMINI_API_KEY="autre-cle-factice"), LE_9, "clé de modèle autre que GEMINI_API_KEY_2"),
    (env_factice(GO_M, CONTROLE_IA_GITHUB_TOKEN_2=None), LE_9, "jeton GitHub absent"),
])
def test_louer_verifier_seulement_artefacts(public, tmp_path, environ, jour, motif):
    code, j, _ = _louer(public, tmp_path, environ, jour)
    assert code == 2 and "REFUS" in j and motif in j, j


# --- M-2, point 1 : le commit privé porte l'amorce, les cinq modules, la configuration (ii) v2 et son compagnon -----------------


def _show_sha(commit: str, chemin: str) -> str | None:
    r = subprocess.run(["git", "-C", str(RACINE), "show", f"{commit}:{chemin}"], capture_output=True, timeout=60)
    return sha(r.stdout) if r.returncode == 0 else None


def test_m2_commit_prive_x_porte_les_pieces_aux_empreintes():
    if git(RACINE, "cat-file", "-e", f"{COMMIT_X}^{{commit}}", check=False).returncode != 0:
        pytest.skip(f"commit X {COMMIT_X[:8]} absent de ce clone du dépôt privé")
    for chemin, attendu in AU_COMMIT_PRIVE.items():
        assert git(RACINE, "cat-file", "-e", f"{COMMIT_X}:{chemin}", check=False).returncode == 0, chemin
        assert _show_sha(COMMIT_X, chemin) == attendu, chemin


def test_m2_commit_temoin_sans_amorce_refuse():
    if git(RACINE, "cat-file", "-e", f"{COMMIT_TEMOIN}^{{commit}}", check=False).returncode != 0:
        pytest.skip(f"commit témoin {COMMIT_TEMOIN[:8]} absent de ce clone du dépôt privé")
    assert git(RACINE, "cat-file", "-e", f"{COMMIT_TEMOIN}:scripts/amorce_hote_durable_a1_v4_v5.sh", check=False).returncode != 0
    assert git(RACINE, "cat-file", "-e", f"{COMMIT_TEMOIN}:src/controle_ia/hote_durable_a1_v4_v5.py", check=False).returncode != 0
