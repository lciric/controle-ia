"""Fermeture et ouverture des sorties de P3-bis (témoin positif planté), v1.

Texte : `prereg/P3-bis-temoin-positif-v1.md` (brouillon 6, `aeb1f63a…`), « Plan d'analyse », points 1 (second paquet),
3, 4, 6 (fermeture, classes, essai différentiel) et 8 (registre des préalables, garde d'ouverture, rendez-vous) ; « Liste
d'arrêt » ; « Ce que le code et la chaîne doivent changer », points 2 (c) et 5 ; corrections de la relecture courte du
brouillon 6 (`brouillons/P3-bis-temoin-positif-v1/contre-lecture-3-brouillon6-v1.md`, transmises par la session mère) :
taille du paquet 16 783 360 octets, corps comprimé puis bourré.

    python -m controle_ia.premier_test_ia.ouverture_p3bis_v1 fermer-run --run R [--partiel]
    python -m controle_ia.premier_test_ia.ouverture_p3bis_v1 exiger-aucun-clair --run R
    python -m controle_ia.premier_test_ia.ouverture_p3bis_v1 deplier-run --run R
    python -m controle_ia.premier_test_ia.ouverture_p3bis_v1 lectures-fermees --run R --lecture RL \
        --lecture-complementaire RLC [--prereg P --entropie E]
    python -m controle_ia.premier_test_ia.ouverture_p3bis_v1 fermer --run R --lecture RL --lecture-complementaire RLC [--entropie E]
    python -m controle_ia.premier_test_ia.ouverture_p3bis_v1 ouvrir --mode plein|reduit --run R --sortie DOSSIER \
        [--racine-paquets C] [--date-paquet AAAA-MM-JJTHH:MM:SSZ] [--instant S]
    python -m controle_ia.premier_test_ia.ouverture_p3bis_v1 exposer-issue FICHIER [--lecture-p3bis CHEMIN]
(toutes avec `--racine` : défaut le dossier courant, racine du clone.)

**Le texte nomme deux sous-commandes, `fermer` et `ouvrir`** ; cinq s'y ajoutent, déclarées : le second paquet (R-2021,
brouillon 6) demande `fermer-run` (sur l'instance, avant toute poussée), `exiger-aucun-clair` (garde de la poussée) et
`deplier-run` (dans le clone fermé, avant les lectures) ; `lectures-fermees` enchaîne, dans le clone fermé, le dépliage,
les deux lectures (points 3 et 4, sorties standard et d'erreur redirigées dans l'espace fermé) et `fermer`, et n'imprime que
les codes de sortie et l'empreinte du paquet (D2 (a)) ; `exposer-issue` affiche, sous l'ouverture réduite, les seules
valeurs `issue` et `ligne` du fichier d'issue. Tout reste dans ce module : trois modules neufs, comme le texte.

**Paquet des lectures** `diag/p3bis-ferme-<run>/paquet-ferme-v1.tar`, exactement `TAILLE_PAQUET_LECTURES` octets, archive
ustar à deux membres, métadonnées normalisées (date 0, propriétaire 0, mode 0644) : `sel.txt`, les 32 octets bruts de
`secrets.token_bytes(32)` ; `corps.bin`, exactement `TAILLE_CORPS_LECTURES` octets : le flux xz (`lzma`, contrôle CRC64)
d'une archive pax des sorties, **puis** la bourre, tirée par `secrets`. Les en-têtes ustar ne changent jamais d'une issue à
l'autre (mêmes noms, mêmes tailles, même place) ; tout le reste est à haute entropie (sel, flux comprimé, bourre) : la taille
de l'objet zlib de git ne dépend plus du contenu (correction 2). La taille 16 783 360 = 1 639 × 10 240 est un multiple de
la taille d'enregistrement de `tar` (correction 1) : 512 + 512 + 512 + 16 780 800 + 1 024. Seule l'empreinte du paquet est
imprimée ; son sel n'est jamais dérivé de l'entropie citée, qui est publique (garde à la relecture).

**Second paquet** `diag/<run>/paquet-run-ferme-v1.tar` : ustar à deux membres, `sel.txt` (32 octets de `secrets`) et
`sorties.tar` (archive pax de `donnees/<run>/` **entier**, fichier complet des sondes compris, et de
`diag/<run>/episodes-p3.json`, avec leurs compagnons) ; jamais écrit en entier sous `diag/` : seulement ses morceaux
`paquet-run-ferme-v1.tar.000`, `.001`, … d'au plus `TAILLE_MORCEAU_MAX` octets, chacun avec son compagnon, et l'index
`paquet-run-ferme-v1.json` (empreinte et taille du paquet, noms, empreintes et tailles des morceaux ; classe 1 et classe 3),
scellé. Choix déclarés : le second paquet n'est pas comprimé (sa taille est en classe 3 ; xz ne gagne que quelques pour cent
sur des flottants et coûterait plusieurs minutes de carte pour le fichier complet des sondes) ; le dépliage ne sort que les
fichiers que lisent les lectures (`FICHIERS_LUS` : épisodes, scores, scores par jeton, textes, avec leurs compagnons), le
paquet gardant le reste fermé (place disque du clone de la session). `fermer-run` ajoute d'abord à `.git/info/exclude` du
clone de l'instance les chemins des épisodes en clair (une poussée par `git add` ne les prend pas) ; `exiger-aucun-clair` le
vérifie dans l'index et dans le commit avant toute poussée.

**Lectures fermées** : dans le clone fermé, les sorties des deux lectures et de l'espace fermé (`espace-ferme-p3bis/`) et les
fichiers dépliés du second paquet ne sont suivis ni par git ni par son index : `deplier-run` et `lectures-fermees` les
ajoutent à `.git/info/exclude` du clone (local, jamais commité ; l'arbre gelé n'est pas touché) — sans quoi la garde
« arbre de travail non propre » du manifeste refuserait les lectures. `fermer` les met dans le paquet, relit le paquet,
puis les efface du clone et vérifie qu'aucun ne reste.

**Garde d'ouverture** (`ouvrir`, seule voie d'ouverture des deux paquets) : registre des préalables
`registres/prealables-p3bis-v1.md` (jamais le texte du préenregistrement, jamais le fichier le plus récent par son nom) ;
format de `registres/scellements-v1.md` (`| CLÉ | AAAA-MM-JJTHH:MM:SSZ | chemin relatif | sha256 |`, motifs recopiés de
`t07/registre_v1.py`, comparés par un essai) ; clés `ECRIT-PERIMETRE-JEUX-P3BIS`, `ECRIT-LANCEMENT-RELANCE-P3BIS`,
`ECRIT-ENGAGEMENT-ETAPE-A-P3BIS` (exactement une ligne chacune), `GARDE-ADAPTEE-T07-P3BIS` (au plus une),
`RENDEZ-VOUS-P3BIS-1`, `-2`… ; toute autre clé : refus. Puis chemin normal (lignes `SCORES-T07` et `SONDES-T07` du registre
des scellements, compagnon du fichier cité égal à la ligne, fichier vérifié seulement s'il est là, D8), ou décision écrite
« ouvrir » de Lazar (branche 1, ouverture réduite, si `SCELLEMENT-T07` et `GARDE-ADAPTEE-T07-P3BIS` citent le même texte
scellé de T0.7, inscrites au plus tard à la date de la décision ; branche 2 sinon, ouverture pleine). Refus : code 2, motif
imprimé, ligne `REFUS-P3BIS` au journal `registres/ouvertures-p3bis-v1.md`, rien d'ouvert ; ouverture : ligne
`OUVERTURE-P3BIS` (date, mode, empreintes). Choix déclarés : décision du rendez-vous dans
`docs/decisions/rendez-vous-P3-bis-v<n>.md` pour la ligne n (forme du texte) ; date de la décision au plus tôt à
`DATE_RENDEZ_VOUS` (date de ce texte, constante du module) et au plus tard à la date de sa ligne ; date de la mise en paquet
(réserve « écrit après la lecture fermée ») lue par `--date-paquet`, sinon dans `git log` du paquet.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import lzma
import os
import re
import secrets
import shutil
import subprocess
import sys
import tarfile
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..scellement import sceller, verifier

# --- tailles et noms -------------------------------------------------------------------------------------------------
TAILLE_PAQUET_LECTURES = 16_783_360        # 1 639 × 10 240 octets : multiple de tarfile.RECORDSIZE (correction 1)
TAILLE_CORPS_LECTURES = TAILLE_PAQUET_LECTURES - 3 * tarfile.BLOCKSIZE - 2 * tarfile.BLOCKSIZE   # 16 780 800 octets
TAILLE_SEL = 32
TAILLE_MORCEAU_MAX = 90_000_000            # « morceaux d'au plus 90 Mo » (GitHub refuse les fichiers de plus de 100 Mo)
NOM_SEL, NOM_CORPS, NOM_SORTIES_RUN = "sel.txt", "corps.bin", "sorties.tar"
PAQUET_LECTURES = "paquet-ferme-v1.tar"
PAQUET_RUN, INDEX_RUN = "paquet-run-ferme-v1.tar", "paquet-run-ferme-v1.json"
ESPACE_DEFAUT = "espace-ferme-p3bis"
DEPLIE = "deplie-run-v1.json"
SONDES_COMPLETES = "sondes-figees.npz"     # fichier complet des sondes (matrices de Mahalanobis) : dans le second paquet
DONNEES_EXIGEES = ("sondes-figees.npz", "sondes-figees-legeres.npz", "scores-p3.npz", "jetons-principales-p3.npz",
                   "textes-actions-p3.jsonl")
DONNEES_LUES = ("scores-p3.npz", "jetons-principales-p3.npz", "textes-actions-p3.jsonl")   # lus par `lecture.charger_source`
EPISODES = "episodes-p3.json"
PRESET_XZ = 6
# --- registres -------------------------------------------------------------------------------------------------------
REGISTRE_PREALABLES = "registres/prealables-p3bis-v1.md"
REGISTRE_SCELLEMENTS = "registres/scellements-v1.md"
JOURNAL_OUVERTURES = "registres/ouvertures-p3bis-v1.md"
CLES_ECRITS = ("ECRIT-PERIMETRE-JEUX-P3BIS", "ECRIT-LANCEMENT-RELANCE-P3BIS", "ECRIT-ENGAGEMENT-ETAPE-A-P3BIS")
CLE_GARDE_ADAPTEE = "GARDE-ADAPTEE-T07-P3BIS"
RENDEZ_VOUS = re.compile(r"RENDEZ-VOUS-P3BIS-([0-9]+)")
SCORES_T07, SONDES_T07, SCELLEMENT_T07, VERDICT_P3BIS = "SCORES-T07", "SONDES-T07", "SCELLEMENT-T07", "VERDICT-P3BIS"
CLES_T07_LUES = (SCORES_T07, SONDES_T07, SCELLEMENT_T07, VERDICT_P3BIS)
DATE_RENDEZ_VOUS = "2026-11-20T12:00:00Z"  # date de ce texte (proposée, défaut sous 48 heures, R-2021)
FICHIER_DECISION = "docs/decisions/rendez-vous-P3-bis-v{n}.md"
DECISION = re.compile(r"^Décision : (maintenir|ouvrir)$", re.M)
DATE_DECISION = re.compile(r"^Date : (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)$", re.M)
# motifs recopiés de `t07/registre_v1.py` (`914b8f37…`) : même format que le registre des scellements
SHA = re.compile(r"[0-9a-f]{64}")
DATE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")
CLE = re.compile(r"[A-Z0-9]+(?:-[A-Z0-9]+)+")
FORMAT_DATE = "%Y-%m-%dT%H:%M:%SZ"
# --- fichier d'issue (texte, « Critères », « Fichier d'issue ») -------------------------------------------------------
ISSUES = {"non lu": 1, "échec": 2, "non tranché": 3, "vu": 4, "non vu": 5}
CLES_ISSUE = ("issue", "ligne", "verdict", "verdict_sha256")
VERDICT = "docs/verdicts/verdict-P3-bis-v1.md"
MODES = ("plein", "reduit")


class RefusOuverture(GardeArret):
    """Refus de la garde d'ouverture : rien n'est ouvert (code 2 en ligne de commande)."""


# ================================================================================================= archives et paquets
def _info(nom: str, taille: int) -> tarfile.TarInfo:
    ti = tarfile.TarInfo(nom)
    ti.size, ti.mtime, ti.mode, ti.uid, ti.gid, ti.uname, ti.gname = taille, 0, 0o644, 0, 0, "", ""
    ti.type = tarfile.REGTYPE
    return ti


def tar_de(membres, format_tar=tarfile.USTAR_FORMAT) -> bytes:
    """Archive tar des membres (nom, octets), dans l'ordre donné, métadonnées normalisées : même contenu, mêmes octets."""
    flux = io.BytesIO()
    with tarfile.open(fileobj=flux, mode="w", format=format_tar, encoding="utf-8") as tf:
        for nom, octets in membres:
            tf.addfile(_info(nom, len(octets)), io.BytesIO(octets))
    return flux.getvalue()


def membres_de(octets: bytes) -> list[tuple[str, bytes]]:
    """Membres (nom, octets) d'une archive tar, fichiers ordinaires seulement ; noms relatifs sans « .. »."""
    sortie = []
    try:
        with tarfile.open(fileobj=io.BytesIO(octets), mode="r:", encoding="utf-8") as tf:
            for m in tf:
                if not m.isreg():
                    raise GardeArret(f"archive : membre {m.name!r} qui n'est pas un fichier ordinaire")
                if m.name.startswith("/") or ".." in Path(m.name).parts or not m.name:
                    raise GardeArret(f"archive : nom de membre {m.name!r} refusé")
                donnees = tf.extractfile(m).read()
                if len(donnees) != m.size:
                    raise GardeArret(f"archive : membre {m.name!r} tronqué")
                sortie.append((m.name, donnees))
    except (tarfile.TarError, OSError, EOFError) as e:
        raise GardeArret(f"archive illisible ({type(e).__name__}: {e})") from None
    noms = [n for n, _ in sortie]
    if len(set(noms)) != len(noms):
        raise GardeArret("archive : nom de membre en double")
    return sortie


def archive_des_fichiers(racine: Path, chemins) -> bytes:
    """Archive pax, déterministe, des fichiers nommés (chemins relatifs à la racine, triés)."""
    racine = Path(racine)
    return tar_de([(c, (racine / c).read_bytes()) for c in sorted(chemins)], tarfile.PAX_FORMAT)


def comprimer(octets: bytes) -> bytes:
    return lzma.compress(octets, format=lzma.FORMAT_XZ, check=lzma.CHECK_CRC64, preset=PRESET_XZ)


def decomprimer(octets: bytes, bourre_permise: bool) -> tuple[bytes, bytes]:
    """Flux xz en tête des octets : (archive, octets qui le suivent) ; flux illisible ou tronqué : garde."""
    d = lzma.LZMADecompressor(format=lzma.FORMAT_XZ)
    try:
        archive = d.decompress(octets)
    except lzma.LZMAError as e:
        raise GardeArret(f"flux xz illisible ({e})") from None
    if not d.eof:
        raise GardeArret("flux xz tronqué")
    if d.unused_data and not bourre_permise:
        raise GardeArret("octets après le flux xz, alors qu'aucune bourre n'est permise")
    return archive, d.unused_data


def tirer_sel() -> bytes:
    return secrets.token_bytes(TAILLE_SEL)


def tirer_bourre(n: int) -> bytes:
    return secrets.token_bytes(n)


def derives_de_l_entropie(entropie: int) -> set[bytes]:
    """Sels qu'on recalculerait depuis l'entropie citée (publique) : refusés à la relecture."""
    e = int(entropie)
    d = {hashlib.sha256(str(e).encode()).digest(), np.random.default_rng(e).bytes(TAILLE_SEL),
         np.random.SeedSequence(e).generate_state(8, np.uint32).tobytes()}
    if 0 <= e < 2 ** 256:
        d |= {e.to_bytes(32, "big"), e.to_bytes(32, "little"), hashlib.sha256(e.to_bytes(32, "big")).digest()}
    return d


def exiger_sel(sel: bytes, entropie: int | None) -> None:
    if len(sel) != TAILLE_SEL:
        raise GardeArret(f"sel absent ou de {len(sel)} octets ({TAILLE_SEL} attendus)")
    if sel == bytes(TAILLE_SEL):
        raise GardeArret("sel nul")
    if entropie is not None and sel in derives_de_l_entropie(entropie):
        raise GardeArret("sel dérivé de l'entropie citée : refusé")


def corps_lectures(archive: bytes) -> bytes:
    """Flux xz de l'archive des sorties, puis la bourre, jusqu'à `TAILLE_CORPS_LECTURES` octets exactement."""
    flux = comprimer(archive)
    if len(flux) > TAILLE_CORPS_LECTURES:
        raise GardeArret(f"sorties trop grosses pour la taille fixe : {len(flux)} octets comprimés, "
                         f"{TAILLE_CORPS_LECTURES} au plus")
    return flux + tirer_bourre(TAILLE_CORPS_LECTURES - len(flux))


def paquet_lectures(archive: bytes, sel: bytes) -> bytes:
    return tar_de([(NOM_SEL, sel), (NOM_CORPS, corps_lectures(archive))])


def exiger_taille_lectures(octets: bytes) -> None:
    if len(octets) != TAILLE_PAQUET_LECTURES:
        raise GardeArret(f"paquet des lectures de {len(octets)} octets, {TAILLE_PAQUET_LECTURES} exigés")


def exiger_taille_corps(corps: bytes) -> None:
    if len(corps) != TAILLE_CORPS_LECTURES:
        raise GardeArret(f"paquet des lectures : corps de {len(corps)} octets, {TAILLE_CORPS_LECTURES} exigés")


def relire_paquet_lectures(octets: bytes, entropie: int | None = None) -> tuple[bytes, bytes]:
    """(sel, archive des sorties) d'un paquet des lectures ; taille, membres, sel et flux contrôlés."""
    exiger_taille_lectures(octets)
    m = membres_de(octets)
    if [n for n, _ in m] != [NOM_SEL, NOM_CORPS]:
        raise GardeArret(f"paquet des lectures : membres {[n for n, _ in m]}, {[NOM_SEL, NOM_CORPS]} attendus")
    sel, corps = m[0][1], m[1][1]
    exiger_sel(sel, entropie)
    exiger_taille_corps(corps)
    archive, _ = decomprimer(corps, bourre_permise=True)
    return sel, archive


def paquet_run(archive: bytes, sel: bytes) -> bytes:
    return tar_de([(NOM_SEL, sel), (NOM_SORTIES_RUN, archive)])


def relire_paquet_run(octets: bytes) -> tuple[bytes, bytes]:
    m = membres_de(octets)
    if [n for n, _ in m] != [NOM_SEL, NOM_SORTIES_RUN]:
        raise GardeArret(f"second paquet : membres {[n for n, _ in m]}, {[NOM_SEL, NOM_SORTIES_RUN]} attendus")
    exiger_sel(m[0][1], None)
    return m[0][1], m[1][1]


def fichiers_lus(run: str) -> tuple[str, ...]:
    """Fichiers du second paquet que lisent les lectures (dépliés dans le clone fermé), avec leurs compagnons."""
    base = [f"donnees/{run}/{n}" for n in DONNEES_LUES] + [f"diag/{run}/{EPISODES}"]
    return tuple(sorted(base + [c + ".sha256" for c in base]))


def _sha(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def _ecrire_neuf(chemin: Path, octets: bytes) -> None:
    if chemin.exists() or Path(str(chemin) + ".sha256").exists():
        raise GardeArret(f"{chemin} existe déjà (R12)")
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_bytes(octets)


def exclure_localement(racine: Path, motifs) -> None:
    """Ajoute des motifs à `.git/info/exclude` du clone (local, jamais commité)."""
    r = subprocess.run(["git", "-C", str(racine), "rev-parse", "--git-path", "info/exclude"], capture_output=True, text=True)
    if r.returncode != 0:
        raise GardeArret(f"{racine} n'est pas un clone git ({r.stderr.strip()})")
    chemin = Path(r.stdout.strip())
    if not chemin.is_absolute():
        chemin = Path(racine) / chemin
    chemin.parent.mkdir(parents=True, exist_ok=True)
    deja = chemin.read_text(encoding="utf-8").splitlines() if chemin.exists() else []
    with open(chemin, "a", encoding="utf-8") as f:
        for m in motifs:
            if m not in deja:
                f.write(m + "\n")


def _suivis(racine: Path, chemins) -> list[str]:
    """Chemins suivis par git, dans l'index ou dans le commit courant."""
    suivis = set()
    for args in (["ls-files", "--"], ["ls-tree", "-r", "--name-only", "HEAD", "--"]):
        r = subprocess.run(["git", "-C", str(racine), *args, *chemins], capture_output=True, text=True)
        if r.returncode != 0 and "HEAD" not in args:
            raise GardeArret(f"git {' '.join(args)} impossible : {r.stderr.strip()}")
        suivis |= {x for x in r.stdout.splitlines() if x}
    return sorted(suivis)


# ================================================================================================= second paquet
def fichiers_du_run(racine: Path, run: str, partiel: bool = False) -> list[str]:
    """`donnees/<run>/` entier (fichier complet des sondes compris) et `diag/<run>/episodes-p3.json` avec son compagnon ;
    hors du mode partiel (arrêt du run), les fichiers du run complet sont exigés et vérifiés par leurs compagnons."""
    racine = Path(racine)
    d = racine / "donnees" / run
    chemins = []
    if d.is_dir():
        chemins = [str(p.relative_to(racine)) for p in sorted(d.rglob("*")) if p.is_file()]
    for n in (EPISODES, EPISODES + ".sha256"):
        if (racine / "diag" / run / n).is_file():
            chemins.append(f"diag/{run}/{n}")
    if not partiel:
        exiges = [f"donnees/{run}/{n}" for n in DONNEES_EXIGEES] + [f"diag/{run}/{EPISODES}"]
        manquants = [c for c in exiges if c not in chemins or c + ".sha256" not in chemins]
        if manquants:
            raise GardeArret(f"second paquet : fichiers du run absents ou sans compagnon : {manquants}")
        for c in exiges:
            verifier(racine / c)
    return sorted(chemins)


def fermer_run(racine, run: str, partiel: bool = False, taille_morceau: int = TAILLE_MORCEAU_MAX) -> dict | None:
    """Second paquet, sur l'instance, avant toute poussée : morceaux scellés et index scellé sous `diag/<run>/`, relecture
    vérifiée (chaque fichier redonné à l'octet) ; les épisodes en clair exclus localement de git. Rend l'index (None en mode
    partiel s'il n'y a rien à fermer)."""
    racine = Path(racine)
    if not 0 < int(taille_morceau) <= TAILLE_MORCEAU_MAX:
        raise GardeArret(f"taille de morceau {taille_morceau} hors de ]0 ; {TAILLE_MORCEAU_MAX}]")
    exclure_localement(racine, [f"/diag/{run}/{EPISODES}", f"/diag/{run}/{EPISODES}.sha256"])   # d'abord : jamais ajoutés
    chemins = fichiers_du_run(racine, run, partiel)
    if not chemins:
        return None
    dossier = racine / "diag" / run
    if list(dossier.glob(PAQUET_RUN + "*")) or (dossier / INDEX_RUN).exists():
        raise GardeArret(f"second paquet de {run} déjà présent (R12)")
    archive = archive_des_fichiers(racine, chemins)
    ecrits = []
    try:
        octets = paquet_run(archive, tirer_sel())
        morceaux = []
        for k, debut in enumerate(range(0, len(octets), int(taille_morceau))):
            nom = f"{PAQUET_RUN}.{k:03d}"
            ecrits.append(dossier / nom)
            _ecrire_neuf(dossier / nom, octets[debut:debut + int(taille_morceau)])
            morceaux.append({"nom": nom, "sha256": sceller(dossier / nom), "taille": (dossier / nom).stat().st_size})
        index = {"version": 1, "run": run, "paquet": PAQUET_RUN, "sha256": _sha(octets), "taille": len(octets),
                 "taille_morceau_max": int(taille_morceau), "morceaux": morceaux}
        ecrits.append(dossier / INDEX_RUN)
        _ecrire_neuf(dossier / INDEX_RUN, (json.dumps(index, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode())
        sceller(dossier / INDEX_RUN)
        relu = relire_run(racine, run)
        if relu != {c: (racine / c).read_bytes() for c in chemins}:
            raise GardeArret("second paquet : la relecture ne redonne pas les fichiers du run à l'octet")
    except BaseException:
        for f in ecrits:                        # morceaux et index retirés : le paquet se refait (le run n'est pas rejoué)
            f.unlink(missing_ok=True)
            Path(str(f) + ".sha256").unlink(missing_ok=True)
        raise
    return index


def relire_run(racine, run: str) -> dict[str, bytes]:
    """Fichiers du second paquet (chemin → octets), après contrôle de l'index, des morceaux et du paquet."""
    racine = Path(racine)
    dossier = racine / "diag" / run
    verifier(dossier / INDEX_RUN)
    try:
        index = json.loads((dossier / INDEX_RUN).read_text(encoding="utf-8"))
        morceaux = list(index["morceaux"])
        noms = [m["nom"] for m in morceaux]
        [(m["sha256"], int(m["taille"])) for m in morceaux]
        int(index["taille"]), str(index["sha256"])
    except (ValueError, KeyError, TypeError):
        raise GardeArret(f"index du second paquet de {run} illisible") from None
    if index.get("version") != 1 or index.get("run") != run or index.get("paquet") != PAQUET_RUN:
        raise GardeArret(f"index du second paquet de {run} d'une autre version, d'un autre run ou d'un autre paquet")
    if noms != [f"{PAQUET_RUN}.{k:03d}" for k in range(len(morceaux))] or not morceaux:
        raise GardeArret("second paquet : noms des morceaux non consécutifs")
    octets = b""
    for m in morceaux:
        if verifier(dossier / m["nom"]) != m["sha256"]:
            raise GardeArret(f"second paquet : morceau {m['nom']} d'empreinte autre que celle de l'index")
        b = (dossier / m["nom"]).read_bytes()
        if len(b) > TAILLE_MORCEAU_MAX or len(b) != m["taille"]:
            raise GardeArret(f"second paquet : morceau {m['nom']} de {len(b)} octets (au plus {TAILLE_MORCEAU_MAX})")
        octets += b
    if _sha(octets) != index["sha256"] or len(octets) != index["taille"]:
        raise GardeArret("second paquet : morceaux réunis d'empreinte ou de taille autre que celle de l'index")
    _, archive = relire_paquet_run(octets)
    fichiers = dict(membres_de(archive))
    permis = (f"donnees/{run}/", f"diag/{run}/{EPISODES}")
    if any(not (c.startswith(permis[0]) or c in (permis[1], permis[1] + ".sha256")) for c in fichiers):
        raise GardeArret("second paquet : chemin hors de donnees/<run>/ et des épisodes")
    return fichiers


def exiger_aucun_clair(racine, run: str) -> None:
    """Avant toute poussée : aucun fichier de `donnees/<run>/` ni les épisodes en clair dans l'index ou le commit."""
    suivis = _suivis(Path(racine), [f"donnees/{run}", f"diag/{run}/{EPISODES}", f"diag/{run}/{EPISODES}.sha256"])
    if suivis:
        raise GardeArret(f"fichiers du run suivis en clair : {suivis}")


def deplier_run(racine, run: str, espace: str = ESPACE_DEFAUT) -> list[str]:
    """Dans le clone fermé, avant les lectures : fichiers lus du second paquet (`fichiers_lus`) dépliés aux chemins
    d'origine (aucun chemin présent ni suivi), compagnons relus, chemins exclus localement de git, liste écrite dans
    l'espace fermé."""
    racine = Path(racine)
    fichiers = {c: b for c, b in relire_run(racine, run).items() if c in fichiers_lus(run)}
    suivis = _suivis(racine, sorted(fichiers))
    presents = [c for c in fichiers if (racine / c).exists()]
    if suivis or presents:
        raise GardeArret(f"second paquet : chemins déjà suivis ou présents (R12) : {sorted(set(suivis) | set(presents))}")
    exclure_localement(racine, [f"/diag/{run}/{EPISODES}", f"/diag/{run}/{EPISODES}.sha256", f"/{espace}/"])
    ecrits = []
    try:
        for c, octets in sorted(fichiers.items()):
            (racine / c).parent.mkdir(parents=True, exist_ok=True)
            (racine / c).write_bytes(octets)
            ecrits.append(c)
        for c in fichiers:
            if c + ".sha256" in fichiers:
                verifier(racine / c)
    except BaseException:
        for c in ecrits:                        # rien ne reste en clair d'un dépliage refusé
            (racine / c).unlink(missing_ok=True)
        raise
    (racine / espace).mkdir(parents=True, exist_ok=True)
    (racine / espace / DEPLIE).write_text(json.dumps({"run": run, "fichiers": sorted(fichiers)}, ensure_ascii=False) + "\n",
                                          encoding="utf-8")
    return sorted(fichiers)


# ================================================================================================= paquet des lectures
def dossier_ferme(run: str) -> str:
    return f"diag/p3bis-ferme-{run}"


def sorties_des_lectures(racine: Path, lectures, espace: str) -> list[str]:
    racine = Path(racine)
    chemins = []
    for base in [f"runs/{x}" for x in lectures] + [f"diag/{x}" for x in lectures] + [espace]:
        d = racine / base
        if d.is_dir():
            chemins += [str(p.relative_to(racine)) for p in sorted(d.rglob("*")) if p.is_file()]
    return sorted(chemins)


def fermer(racine, run: str, lectures, espace: str = ESPACE_DEFAUT, entropie: int | None = None,
           imprimer=print) -> str:
    """Paquet des lectures : sorties des deux lectures et de l'espace fermé, sel, flux comprimé, bourre ; relecture ;
    effacement des fichiers en clair et des fichiers dépliés du second paquet ; compagnon ; seule l'empreinte est
    imprimée."""
    racine = Path(racine)
    chemins = sorties_des_lectures(racine, lectures, espace)
    if not chemins:
        raise GardeArret("aucune sortie de lecture à fermer")
    deplies = []
    if (racine / espace / DEPLIE).is_file():
        deplies = json.loads((racine / espace / DEPLIE).read_text(encoding="utf-8"))["fichiers"]
    cible = racine / dossier_ferme(run) / PAQUET_LECTURES
    if cible.exists() or Path(str(cible) + ".sha256").exists():
        raise GardeArret(f"{cible} existe déjà (R12)")
    archive = archive_des_fichiers(racine, chemins)
    sel = tirer_sel()
    exiger_sel(sel, entropie)
    octets = paquet_lectures(archive, sel)
    exiger_taille_lectures(octets)
    _ecrire_neuf(cible, octets)
    try:
        sel_relu, archive_relue = relire_paquet_lectures(cible.read_bytes(), entropie)
        if sel_relu != sel or archive_relue != archive:
            raise GardeArret("paquet des lectures : la relecture ne redonne ni le sel ni l'archive")
        if dict(membres_de(archive_relue)) != {c: (racine / c).read_bytes() for c in chemins}:
            raise GardeArret("paquet des lectures : la relecture ne redonne pas les sorties à l'octet")
    except BaseException:
        cible.unlink(missing_ok=True)           # paquet non scellé retiré : la mise en paquet se refait sur les mêmes fichiers
        raise
    for c in chemins + list(deplies):
        p = racine / c
        if p.is_file():
            p.unlink()
    for base in [f"runs/{x}" for x in lectures] + [f"diag/{x}" for x in lectures] + [espace]:
        if (racine / base).is_dir():
            shutil.rmtree(racine / base)
    for c in deplies:                           # dossiers laissés vides par les fichiers dépliés (donnees/<run>/)
        parent = (racine / c).parent
        while parent != racine and parent.is_dir() and not any(parent.iterdir()):
            parent.rmdir()
            parent = parent.parent
    restes = [c for c in chemins + list(deplies) if (racine / c).exists()]
    if restes:
        raise GardeArret(f"fichiers en clair restés dans le clone : {restes}")
    sha = sceller(cible)
    imprimer(sha)
    return sha


def commandes_des_lectures(run: str, lecture: str, lecture_c: str, prereg: str | None, entropie: int | None) -> list:
    """Commandes des points 3 et 4 du plan (le lanceur Python courant)."""
    fin = (["--prereg", prereg] if prereg is not None else []) + (["--entropie", str(entropie)] if entropie is not None else [])
    return [("lecture de P3", "lecture-p3", [sys.executable, "-m", "controle_ia.premier_test_ia.lecture", "--run-source", run,
                                              "--run-lecture", lecture, *fin]),
            ("lecture complémentaire", "lecture-p3bis",
             [sys.executable, "-m", "controle_ia.premier_test_ia.lecture_p3bis_v1", "--run-source", run, "--lecture",
              lecture, "--run-lecture", lecture_c, *fin])]


def lectures_fermees(racine, run: str, lecture: str, lecture_c: str, prereg: str | None = None,
                     entropie: int | None = None, espace: str = ESPACE_DEFAUT, imprimer=print) -> int:
    """Clone fermé : dépliage, deux lectures (sorties redirigées dans l'espace fermé), mise en paquet ; n'imprime que les
    codes de sortie et l'empreinte du paquet. Code 0 si chaque étape rend 0."""
    racine = Path(racine)
    exclure_localement(racine, [f"/runs/{lecture}/", f"/diag/{lecture}/", f"/runs/{lecture_c}/", f"/diag/{lecture_c}/",
                                f"/{espace}/"])
    codes = []
    try:
        deplier_run(racine, run, espace)
        codes.append(("dépliage du second paquet", 0))
    except GardeArret:
        imprimer("code dépliage du second paquet : 1")
        return 1
    for nom, fichier, commande in commandes_des_lectures(run, lecture, lecture_c, prereg, entropie):
        with open(racine / espace / f"{fichier}.sortie", "wb") as so, open(racine / espace / f"{fichier}.erreurs", "wb") as se:
            r = subprocess.run(commande, cwd=str(racine), stdout=so, stderr=se, stdin=subprocess.DEVNULL)
        codes.append((nom, r.returncode))
    sortie_fermer = []
    try:
        fermer(racine, run, [lecture, lecture_c], espace, entropie, imprimer=sortie_fermer.append)
        codes.append(("mise en paquet", 0))
    except GardeArret:
        codes.append(("mise en paquet", 1))
    for nom, code in codes:
        imprimer(f"code {nom} : {code}")
    if sortie_fermer:
        imprimer(f"paquet des lectures : {sortie_fermer[0]}")
    return 0 if all(c == 0 for _, c in codes) else 1


# ================================================================================================= garde d'ouverture
def instant_utc(date: str) -> int:
    if not DATE.fullmatch(date):
        raise RefusOuverture(f"date {date!r} (AAAA-MM-JJTHH:MM:SSZ, UTC, attendue)")
    try:
        return int(datetime.strptime(date, FORMAT_DATE).replace(tzinfo=timezone.utc).timestamp())
    except ValueError:
        raise RefusOuverture(f"date {date!r} impossible") from None


def date_utc(instant: int) -> str:
    return datetime.fromtimestamp(int(instant), timezone.utc).strftime(FORMAT_DATE)


def _cellules(ligne: str) -> list[str]:
    return [c.strip() for c in ligne.strip().strip("|").split("|")]


def _ligne_stricte(cle: str, c: list[str], fautes: list) -> dict | None:
    if len(c) != 4:
        fautes.append(f"ligne {cle} mal formée ({len(c)} colonnes, 4 attendues)")
        return None
    _, date, chemin, sha = c
    if not DATE.fullmatch(date):
        fautes.append(f"ligne {cle} mal formée : date {date!r}")
        return None
    try:
        instant = instant_utc(date)
    except RefusOuverture as e:
        fautes.append(f"ligne {cle} mal formée : {e}")
        return None
    if not SHA.fullmatch(sha):
        fautes.append(f"ligne {cle} mal formée : empreinte {sha!r}")
        return None
    if not chemin or chemin.startswith("/") or ".." in Path(chemin).parts:
        fautes.append(f"ligne {cle} mal formée : chemin {chemin!r}")
        return None
    return {"cle": cle, "date": date, "instant": instant, "chemin": chemin, "sha256": sha}


def lire_prealables(chemin: Path) -> dict:
    """Lignes du registre des préalables ; tous les refus de forme sont relevés, puis rendus ensemble."""
    chemin = Path(chemin)
    if not chemin.is_file():
        raise RefusOuverture(f"registre des préalables {REGISTRE_PREALABLES} absent")
    fautes, ecrits, gardes, rdv = [], {k: [] for k in CLES_ECRITS}, [], []
    for brute in chemin.read_text(encoding="utf-8").splitlines():
        if not brute.strip().startswith("|"):
            continue
        c = _cellules(brute)
        c0 = c[0] if c else ""
        m = RENDEZ_VOUS.fullmatch(c0)
        if c0 in CLES_ECRITS or c0 == CLE_GARDE_ADAPTEE or m:
            ligne = _ligne_stricte(c0, c, fautes)
            if ligne is None:
                continue
            if c0 in CLES_ECRITS:
                ecrits[c0].append(ligne)
            elif c0 == CLE_GARDE_ADAPTEE:
                gardes.append(ligne)
            else:
                ligne["numero_texte"] = m.group(1)
                rdv.append(ligne)
        elif CLE.fullmatch(c0):
            fautes.append(f"clé inconnue {c0} au registre des préalables")
        elif len(c) == 4 and DATE.fullmatch(c[1]):
            fautes.append(f"ligne {c0!r} au registre des préalables : la première cellule n'a pas la forme d'une clé")
    for k, lignes in ecrits.items():
        if len(lignes) != 1:
            fautes.append(f"{len(lignes)} ligne(s) {k}, exactement une attendue")
    if len(gardes) > 1:
        fautes.append(f"{len(gardes)} lignes {CLE_GARDE_ADAPTEE}, au plus une attendue")
    numeros = [x["numero_texte"] for x in rdv]
    if numeros != [str(n) for n in range(1, len(rdv) + 1)]:
        fautes.append(f"numéros de rendez-vous {numeros} : consécutifs depuis 1, dans l'ordre, attendus")
    if any(rdv[k]["instant"] >= rdv[k + 1]["instant"] for k in range(len(rdv) - 1)):
        fautes.append("dates des lignes de rendez-vous non strictement croissantes")
    if fautes:
        raise RefusOuverture(" ; ".join(fautes))
    return {"ecrits": {k: v[0] for k, v in ecrits.items()}, "garde": gardes[0] if gardes else None, "rendez_vous": rdv}


def _sha_fichier(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def sceau_conforme(chemin: Path, attendu: str) -> None:
    """Fichier présent, compagnon présent et égal, empreinte égale à celle de la ligne (comme `registre_v1.sceau_conforme`)."""
    chemin = Path(chemin)
    if not chemin.is_file():
        raise RefusOuverture(f"{chemin} absent")
    comp = Path(str(chemin) + ".sha256")
    if not comp.is_file():
        raise RefusOuverture(f"{chemin} : compagnon .sha256 absent")
    sha = _sha_fichier(chemin)
    lu = (comp.read_text(encoding="utf-8").split() or [""])[0]
    if lu != sha:
        raise RefusOuverture(f"{chemin} : compagnon .sha256 ({lu[:12]}…) ≠ empreinte du fichier ({sha[:12]}…)")
    if sha != attendu:
        raise RefusOuverture(f"{chemin} : empreinte {sha[:12]}… ≠ celle du registre ({attendu[:12]}…)")


def _anterieure(ligne: dict, instant: int) -> None:
    if not ligne["instant"] < int(instant):
        raise RefusOuverture(f"ligne {ligne['cle']} datée {ligne['date']}, pas strictement antérieure à l'ouverture "
                             f"({date_utc(instant)})")


def lire_decision(racine: Path, ligne: dict, n: int) -> dict:
    attendu = FICHIER_DECISION.format(n=n)
    if ligne["chemin"] != attendu:
        raise RefusOuverture(f"ligne {ligne['cle']} : fichier {ligne['chemin']!r}, {attendu!r} attendu")
    sceau_conforme(Path(racine) / ligne["chemin"], ligne["sha256"])
    texte = (Path(racine) / ligne["chemin"]).read_text(encoding="utf-8")
    d, t = DECISION.findall(texte), DATE_DECISION.findall(texte)
    if len(d) != 1 or len(t) != 1 or len(re.findall(r"^Décision :", texte, re.M)) != 1 or \
            len(re.findall(r"^Date :", texte, re.M)) != 1:
        raise RefusOuverture(f"décision {ligne['chemin']} mal formée (une ligne « Décision : maintenir|ouvrir » et une ligne "
                             f"« Date : AAAA-MM-JJTHH:MM:SSZ » attendues)")
    instant = instant_utc(t[0])
    if instant < instant_utc(DATE_RENDEZ_VOUS):
        raise RefusOuverture(f"décision {ligne['chemin']} datée {t[0]}, avant le rendez-vous ({DATE_RENDEZ_VOUS})")
    if instant > ligne["instant"]:
        raise RefusOuverture(f"décision {ligne['chemin']} datée {t[0]}, après sa ligne ({ligne['date']})")
    return {"numero": n, "decision": d[0], "date": t[0], "instant": instant, "fichier": ligne["chemin"],
            "sha256": ligne["sha256"]}


def lire_scellements_t07(chemin: Path) -> dict:
    """Lignes `SCORES-T07`, `SONDES-T07`, `SCELLEMENT-T07`, `VERDICT-P3BIS` du registre des scellements (les autres clés
    sont celles de T0.6 et de T0.7 : ni lues ni jugées ici) ; une ligne de ces clés mal formée ou en double : refus."""
    chemin = Path(chemin)
    if not chemin.is_file():
        return {}
    trouvees, fautes = {k: [] for k in CLES_T07_LUES}, []
    for brute in chemin.read_text(encoding="utf-8").splitlines():
        if not brute.strip().startswith("|"):
            continue
        c = _cellules(brute)
        if c and c[0] in trouvees:
            ligne = _ligne_stricte(c[0], c, fautes)
            if ligne is not None:
                trouvees[c[0]].append(ligne)
    for k, v in trouvees.items():
        if len(v) > 1:
            fautes.append(f"{len(v)} lignes {k} au registre des scellements, une au plus attendue")
    if fautes:
        raise RefusOuverture(" ; ".join(fautes))
    return {k: v[0] for k, v in trouvees.items() if v}


def ligne_t07_conforme(racine: Path, ligne: dict, instant: int) -> None:
    """D8 : date antérieure, compagnon du fichier cité présent et égal à l'empreinte de la ligne ; le fichier lui-même
    vérifié seulement s'il est présent (aucun fichier fermé de T0.7 n'est déplacé pour cela)."""
    _anterieure(ligne, instant)
    p = Path(racine) / ligne["chemin"]
    comp = Path(str(p) + ".sha256")
    if not comp.is_file():
        raise RefusOuverture(f"ligne {ligne['cle']} : compagnon {ligne['chemin']}.sha256 absent")
    if (comp.read_text(encoding="utf-8").split() or [""])[0] != ligne["sha256"]:
        raise RefusOuverture(f"ligne {ligne['cle']} : compagnon de {ligne['chemin']} ≠ empreinte de la ligne")
    if p.is_file() and _sha_fichier(p) != ligne["sha256"]:
        raise RefusOuverture(f"ligne {ligne['cle']} : {ligne['chemin']} présent, d'empreinte ≠ celle de la ligne")


def date_de_la_mise_en_paquet(racine_paquets: Path, run: str, date: str | None) -> int:
    if date is not None:
        return instant_utc(date)
    r = subprocess.run(["git", "-C", str(racine_paquets), "log", "-1", "--format=%ct", "--",
                        f"{dossier_ferme(run)}/{PAQUET_LECTURES}"], capture_output=True, text=True)
    if r.returncode != 0 or not r.stdout.strip().isdigit():
        raise RefusOuverture("date de la mise en paquet illisible (--date-paquet ou commit du paquet exigé)")
    return int(r.stdout.strip())


def garde_ouverture(racine, mode: str, instant: int, instant_paquet: int) -> dict:
    """Garde du plan, point 8 ; rend le mode autorisé, le chemin, les réserves et les empreintes, ou lève `RefusOuverture`
    (tous les motifs relevés)."""
    racine = Path(racine)
    if mode not in MODES:
        raise RefusOuverture(f"mode {mode!r} : {MODES} attendus")
    pre = lire_prealables(racine / REGISTRE_PREALABLES)
    fautes, reserves = [], []
    for k, ligne in pre["ecrits"].items():
        try:
            _anterieure(ligne, instant)
            sceau_conforme(racine / ligne["chemin"], ligne["sha256"])
            if ligne["instant"] > instant_paquet:
                reserves.append(f"{k} : écrit après la lecture fermée : sa cécité repose sur la fermeture")
        except RefusOuverture as e:
            fautes.append(str(e))
    garde = pre["garde"]
    if garde is not None:
        try:
            _anterieure(garde, instant)
            sceau_conforme(racine / garde["chemin"], garde["sha256"])
        except RefusOuverture as e:
            fautes.append(str(e))
    decisions = []
    for n, ligne in enumerate(pre["rendez_vous"], start=1):
        try:
            _anterieure(ligne, instant)
            decisions.append(lire_decision(racine, ligne, n))
        except RefusOuverture as e:
            fautes.append(str(e))
    if any(d["decision"] == "ouvrir" for d in decisions[:-1]):
        fautes.append("ligne de rendez-vous après une décision « ouvrir »")
    try:
        t07 = lire_scellements_t07(racine / REGISTRE_SCELLEMENTS)
    except RefusOuverture as e:
        fautes.append(str(e))
        t07 = {}
    if fautes:
        raise RefusOuverture(" ; ".join(fautes))
    normal, motifs_normal = True, []
    for k in (SCORES_T07, SONDES_T07):
        if k not in t07:
            normal = False
            motifs_normal.append(f"ligne {k} absente")
            continue
        try:
            ligne_t07_conforme(racine, t07[k], instant)
        except RefusOuverture as e:
            normal = False
            motifs_normal.append(str(e))
    derniere = decisions[-1]["decision"] if decisions else None
    if normal:
        autorise, chemin = "plein", "chemin normal" + ("" if not decisions else " (rendez-vous sans objet)")
    elif derniere == "ouvrir":
        d = decisions[-1]
        motifs_b1 = []
        s = t07.get(SCELLEMENT_T07)
        if s is None:
            motifs_b1.append("T0.7 non scellé (aucune ligne SCELLEMENT-T07)")
        else:
            try:
                ligne_t07_conforme(racine, s, instant)
                if s["instant"] > d["instant"]:
                    motifs_b1.append("SCELLEMENT-T07 inscrite après la décision « ouvrir »")
            except RefusOuverture as e:
                motifs_b1.append(str(e))
        if garde is None:
            motifs_b1.append(f"aucune ligne {CLE_GARDE_ADAPTEE}")
        else:
            if garde["instant"] > d["instant"]:
                motifs_b1.append(f"{CLE_GARDE_ADAPTEE} inscrite après la décision « ouvrir »")
            if s is not None and (garde["chemin"], garde["sha256"]) != (s["chemin"], s["sha256"]):
                motifs_b1.append(f"{CLE_GARDE_ADAPTEE} ne cite pas le texte scellé de T0.7 (ligne SCELLEMENT-T07)")
        if motifs_b1:
            autorise, chemin = "plein", "branche 2 (" + " ; ".join(motifs_b1) + ") : T0.7 ne lit plus la course 7b sous son texte, nœud de Lazar"
        else:
            autorise, chemin = "reduit", "branche 1 (ouverture réduite à l'issue)"
    elif derniere == "maintenir":
        raise RefusOuverture("décision « maintenir » : l'attente continue, rien n'est ouvert ("
                             + " ; ".join(motifs_normal) + ")")
    else:
        raise RefusOuverture("ni lignes SCORES-T07 et SONDES-T07 bien formées, ni ligne « ouvrir » ("
                             + " ; ".join(motifs_normal) + ")")
    if mode != autorise:
        if mode == "reduit" and chemin.startswith("branche 2"):
            raise RefusOuverture(f"ouverture réduite demandée sans ligne {CLE_GARDE_ADAPTEE} conforme : {chemin}")
        if mode == "reduit":
            raise RefusOuverture("chemin normal : ouverture pleine seulement (mode réduit refusé)")
        raise RefusOuverture("branche 1 : ouverture réduite seulement (T0.7 scellé avec la garde adaptée)")
    return {"mode": autorise, "chemin": chemin, "reserves": reserves, "decisions": decisions,
            "registre_prealables_sha256": _sha_fichier(racine / REGISTRE_PREALABLES),
            "registre_scellements_sha256": (_sha_fichier(racine / REGISTRE_SCELLEMENTS)
                                            if (racine / REGISTRE_SCELLEMENTS).is_file() else "absent")}


def _journal(racine: Path, ligne: str) -> None:
    j = Path(racine) / JOURNAL_OUVERTURES
    if not j.parent.is_dir():
        return
    if not j.exists():
        j.write_text("# Journal des ouvertures de P3-bis (garde `ouverture_p3bis_v1 ouvrir`) — lignes ajoutées, jamais "
                     "réécrites\n\n", encoding="utf-8")
    with open(j, "a", encoding="utf-8") as f:
        f.write(ligne + "\n")


def _propre(texte: str) -> str:
    return " ".join(str(texte).replace("|", "¦").split())


def extraire_paquets(racine_paquets: Path, run: str, sortie: Path) -> dict:
    """Les deux paquets extraits dans un dossier neuf (chemins d'origine sous lui) ; empreintes des paquets rendues."""
    racine_paquets, sortie = Path(racine_paquets), Path(sortie)
    if sortie.exists():
        raise GardeArret(f"{sortie} existe déjà (R12)")
    cible = racine_paquets / dossier_ferme(run) / PAQUET_LECTURES
    sha_l = verifier(cible)
    _, archive = relire_paquet_lectures(cible.read_bytes())
    fichiers = dict(membres_de(archive))
    run_f = relire_run(racine_paquets, run)
    index = json.loads((racine_paquets / "diag" / run / INDEX_RUN).read_text(encoding="utf-8"))
    communs = set(fichiers) & set(run_f)
    if communs:
        raise GardeArret(f"chemins présents dans les deux paquets : {sorted(communs)}")
    temp = Path(tempfile.mkdtemp(prefix=".ouverture-", dir=str(sortie.parent)))
    try:
        for c, octets in sorted({**fichiers, **run_f}.items()):
            (temp / c).parent.mkdir(parents=True, exist_ok=True)
            (temp / c).write_bytes(octets)
        os.rename(temp, sortie)
    except BaseException:
        shutil.rmtree(temp, ignore_errors=True)
        raise
    return {"paquet_lectures_sha256": sha_l, "paquet_run_sha256": index["sha256"]}


def ouvrir(racine, mode: str, run: str, sortie, racine_paquets=None, date_paquet: str | None = None,
           instant: int | None = None, imprimer=print) -> dict:
    racine = Path(racine)
    racine_paquets = Path(racine_paquets) if racine_paquets is not None else racine
    instant = int(time.time()) if instant is None else int(instant)
    try:
        g = garde_ouverture(racine, mode, instant, date_de_la_mise_en_paquet(racine_paquets, run, date_paquet))
    except RefusOuverture as e:
        sha_p = _sha_fichier(racine / REGISTRE_PREALABLES) if (racine / REGISTRE_PREALABLES).is_file() else "absent"
        _journal(racine, f"| REFUS-P3BIS | {date_utc(instant)} | {mode} | {_propre(e)} | registre des préalables {sha_p} |")
        raise
    try:
        e = extraire_paquets(racine_paquets, run, sortie)
    except GardeArret as x:
        _journal(racine, f"| REFUS-P3BIS | {date_utc(instant)} | {mode} | extraction des paquets : {_propre(x)} | garde "
                         f"passée |")
        raise
    _journal(racine, f"| OUVERTURE-P3BIS | {date_utc(instant)} | {g['mode']} ({_propre(g['chemin'])}) | paquet des lectures "
                     f"{e['paquet_lectures_sha256']} ; paquet du run {e['paquet_run_sha256']} | registre des préalables "
                     f"{g['registre_prealables_sha256']} ; registre des scellements {g['registre_scellements_sha256']} ; "
                     f"réserves : {_propre(' ; '.join(g['reserves']) or 'aucune')} |")
    if g["mode"] == "reduit":
        imprimer(f"ouverture réduite : paquets extraits dans {sortie}, remis au seul lecteur du verdict ; seules `issue` et "
                 f"`ligne` du fichier d'issue seront exposées (exposer-issue)")
    else:
        imprimer(f"ouverture pleine ({g['chemin']}) : paquets extraits dans {sortie}")
    for r in g["reserves"]:
        imprimer(f"réserve : {r}")
    return {**g, **e}


def exposer_issue(fichier, lecture_p3bis=None) -> dict:
    """Seules `issue` et `ligne` du fichier d'issue (quatre clés exactement, scellé) ; avec `lecture_p3bis`, accord exigé
    avec `resultat.issue_mecanique` pour les lignes 2 à 5."""
    fichier = Path(fichier)
    verifier(fichier)
    try:
        doc = json.loads(fichier.read_text(encoding="utf-8"))
    except ValueError:
        raise GardeArret(f"{fichier} : JSON illisible") from None
    if not isinstance(doc, dict) or sorted(doc) != sorted(CLES_ISSUE):
        raise GardeArret(f"{fichier} : clés {sorted(doc) if isinstance(doc, dict) else doc!r}, {list(CLES_ISSUE)} exactement")
    issue, ligne = doc["issue"], doc["ligne"]
    if issue not in ISSUES or isinstance(ligne, bool) or not isinstance(ligne, int) or ISSUES[issue] != ligne:
        raise GardeArret(f"{fichier} : issue {issue!r} et ligne {ligne!r} hors de la table gelée")
    if doc["verdict"] != VERDICT or not isinstance(doc["verdict_sha256"], str) or not SHA.fullmatch(doc["verdict_sha256"]):
        raise GardeArret(f"{fichier} : verdict ou empreinte du verdict hors de forme")
    if lecture_p3bis is not None and ligne != 1:
        im = json.loads(Path(lecture_p3bis).read_text(encoding="utf-8"))["resultat"]["issue_mecanique"]
        if (im["issue"], im["ligne"]) != (issue, ligne):
            raise GardeArret(f"désaccord entre le fichier d'issue ({issue}, {ligne}) et l'issue mécanique "
                             f"({im['issue']}, {im['ligne']}) : nœud de Lazar")
    return {"issue": issue, "ligne": ligne}


# ================================================================================================= ligne de commande
def _main(argv) -> int:
    ap = argparse.ArgumentParser(prog="python -m controle_ia.premier_test_ia.ouverture_p3bis_v1")
    sp = ap.add_subparsers(dest="commande", required=True)
    for nom in ("fermer-run", "exiger-aucun-clair", "deplier-run", "lectures-fermees", "fermer", "ouvrir"):
        p = sp.add_parser(nom)
        p.add_argument("--racine", default=".")
        p.add_argument("--run", required=True)
        if nom == "fermer-run":
            p.add_argument("--partiel", action="store_true")
        if nom in ("deplier-run", "lectures-fermees", "fermer"):
            p.add_argument("--espace", default=ESPACE_DEFAUT)
        if nom in ("lectures-fermees", "fermer"):
            p.add_argument("--lecture", required=True)
            p.add_argument("--lecture-complementaire", required=True)
            p.add_argument("--entropie", type=int, default=None)
        if nom == "lectures-fermees":
            p.add_argument("--prereg", default=None)
        if nom == "ouvrir":
            p.add_argument("--mode", required=True, choices=MODES)
            p.add_argument("--sortie", required=True)
            p.add_argument("--racine-paquets", default=None)
            p.add_argument("--date-paquet", default=None)
            p.add_argument("--instant", type=int, default=None)
    p = sp.add_parser("exposer-issue")
    p.add_argument("fichier")
    p.add_argument("--lecture-p3bis", default=None)
    a = ap.parse_args(argv)
    if a.commande == "fermer-run":
        index = fermer_run(a.racine, a.run, a.partiel)
        if index is None:
            print("second paquet : aucun fichier du run à fermer")
        else:
            print(f"paquet du run {index['sha256']} ; {len(index['morceaux'])} morceau(x) : "
                  + ", ".join(f"{m['nom']} {m['sha256']}" for m in index["morceaux"]))
        return 0
    if a.commande == "exiger-aucun-clair":
        exiger_aucun_clair(a.racine, a.run)
        return 0
    if a.commande == "deplier-run":
        deplier_run(a.racine, a.run, a.espace)
        return 0
    if a.commande == "lectures-fermees":
        return lectures_fermees(a.racine, a.run, a.lecture, a.lecture_complementaire, a.prereg, a.entropie, a.espace)
    if a.commande == "fermer":
        fermer(a.racine, a.run, [a.lecture, a.lecture_complementaire], a.espace, a.entropie)
        return 0
    if a.commande == "ouvrir":
        try:
            ouvrir(a.racine, a.mode, a.run, a.sortie, a.racine_paquets, a.date_paquet, a.instant)
        except RefusOuverture as e:
            print(f"REFUS : {e}", file=sys.stderr)
            return 2
        return 0
    print(json.dumps(exposer_issue(a.fichier, a.lecture_p3bis), ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
