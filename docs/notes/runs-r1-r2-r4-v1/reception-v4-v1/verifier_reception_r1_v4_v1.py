#!/usr/bin/env python3
"""Vérificateur mécanique de la fiche de réception v4 de R1 (`fiche-reception-r1-v4-v1.md`, même dossier) — v1.

Addendum v4 scellé : `prereg/R1-addendum-relance-v4.md` (0f10881b…, commit de scellement 937f1317, versement du témoin
5bd62a00), étape 4 (« Attentes de réception », « Recalcul de réception »), écarts V4-E5, V4-E11, V4-E13, V4-E14,
« Liste d'arrêt ». Script neuf (R12) ; il ne modifie rien, n'écrit rien dans l'arbre reçu, n'appelle aucun réseau.

Deux sous-commandes :

`bloc` — imprime le bloc d'attendus (JSON aux clés triées) que la fiche porte entre ses marqueurs ; la fiche est
  écrite avec cette sortie, à l'identique.

`verifier` — sur une **copie récupérée** (arbre de travail du commit de versement sur `calcul/r1-r2-reel-v1`, dépôt git
  qui porte les objets du commit de versement, de la branche source et de 5bd62a00), dans l'ordre :
  fiche (bloc égal aux attendus, sceau égal) → textes scellés au commit du versement du témoin → versement (un parent,
  chemins ajoutés exactement les attendus, rien sous `traces/`) → octets (chaque fichier de l'arbre = blob du commit de
  versement = blob de la branche source, ou de 5bd62a00 pour le témoin) → présence (aucun fichier en plus ni en moins)
  → compagnons → témoin → réparation → table v4 → chaîne locale → commit du rejeu → rejeu → fichiers `.npz` (noms,
  tableaux, formes, types : en-têtes seulement) → recalcul de réception (sortie de
  `chaine_table_v4_v1 … --reception`, arbre `src/` du recalcul égal à 5bd62a00).

Ce qui n'est **jamais** lu : aucun tableau `.npz` (seuls les noms des membres et l'en-tête `.npy` : `descr`,
`fortran_order`, `shape`) ; du résultat du rejeu, seules les clés de `CHEMINS_LUS_REJEU` sont gardées dès le chargement
(`filtrer`), les valeurs observées de P-R5 et les lectures de l'instrument (`INTERDITS`) ne sont ni gardées, ni écrites,
ni affichées ; du résultat de la réparation, seules les clés de `extraire_reparation` ; du témoin, `run_id`,
`manifeste_sha256`, `resultat.etape`, `resultat.version`. Les grandeurs qui dépendent de la couverture (retrouvées, non
retrouvées) ne sont **comparées** qu'entre pièces (table, réparation, rejeu, recalcul) et ne sont jamais affichées : un
message d'arrêt nomme la clé, pas sa valeur. Aucune trace d'instance n'est ouverte.

Sorties : code 0 « RÉCEPTION CONFORME » (liste des gardes passées) ; code 2 « ARRÊT [garde] : … » au premier écart
(R5, aucun repli silencieux) ; code 3 « COURSE ARRÊTÉE » quand un `arret.json` est reçu à la place d'un résultat
(réception de l'arrêt seulement : motif fermé, rattachement, manifeste ; nœud porté à Lazar). Bibliothèque standard
seulement (`python -I`) ; `git` en lecture seule (`show`, `ls-tree`, `rev-parse`, `cat-file`, `merge-base`, `diff`).

  python3 -I verifier_reception_r1_v4_v1.py bloc
  python3 -I verifier_reception_r1_v4_v1.py verifier --fiche FICHE.md --depot DEPOT --racine ARBRE \\
      --commit-versement C --source REF --run-reparation R --run-rejeu J --scores-p3 SCORES \\
      --sortie-recalcul SORTIE.json --racine-recalcul ARBRE_RECALCUL
"""
import argparse
import ast
import hashlib
import json
import re
import subprocess
import sys
import zipfile
from pathlib import Path

NOM_SCRIPT = "verifier_reception_r1_v4_v1.py"
FORMAT = "attendus-reception-r1-v4-v1"
DEBUT_BLOC, FIN_BLOC = "<!-- attendus-machine : debut -->", "<!-- attendus-machine : fin -->"
SUFFIXE = ".sha256"

# ------------------------------------------------------------------ règles de code recopiées (5bd62a00, inchangées)
# `resolution_tokenisation_v1.METHODES_RECHERCHE`, `NIVEAUX_C6`, `METHODES` ; `resolution_graine_v1.METHODES_V3`,
# `CORRIGEES_V3` ; `rejeu_activations_v3.methode_resolution`
METHODES_RECHERCHE = ("fins", "une_paire", "deux_paires")
METHODES_C6 = ("trois_paires", "quatre_paires_meme_action", "copie", "fenetre", "fenetre_et_paire", "deux_fenetres",
               "fin_et_paire", "fin_et_fenetre", "fin_et_deux_paires", "deux_fins_et_paire")
METHODES_V3 = METHODES_RECHERCHE + METHODES_C6 + ("non_resolu", "identifiants")
CORRIGEES_V3 = METHODES_RECHERCHE + METHODES_C6 + ("identifiants",)


def methode_resolution(m):
    if m is None or m == "non_resolu":
        return "aucune"
    if m in METHODES_RECHERCHE:
        return "v1"
    if m in METHODES_C6:
        return "v2"
    if m == "identifiants":
        return "identifiants"
    raise Arret("table", f"méthode de table inconnue {m!r}")


# ------------------------------------------------------------------ attendus réels (addendum v4 scellé)
SCELLEMENT = "937f13177892933955c9c34839b4b45a4db745df"
TEMOIN_VERSE = "5bd62a004279776c2718b3201c11001e16fa6527"
RUN_TEMOIN = "20261104-091009-r1-v4-temoin-reel"
PIECES = {   # chemin : (sha256 du fichier au commit du versement du témoin, compagnon exigé au même commit)
    "prereg/R1-addendum-relance-v4.md": ("0f10881b32fa4c0e5ec1eb02cf88fbd0fcb6ad13f70b59abc2d84e45a99f61c8", True),
    "prereg/R1-reparation-v4-config-v2.json": ("4d0655d1bac5b15d6cb604e5853bed0bfe1eb48d6235772e39b86a698b8d85e5", True),
    "prereg/R1-rejeu-config-v6.json": ("a9ebc6b0cd6c99e118ade7b304472b5452d2b43c63cc222d1adccd2ee4e95e75", True),
    "prereg/R1-table-tokenisation-v3.json": ("ead8a66851b2af5dfa02635297056872032878fbd2987ba780fb6c9096766423", True),
    "prereg/R1-R2-rejeu-p3-v1.md": ("80c85a0085f444dc10f36e4e226d015802d2e20294c4fff2ae67adb0aca4ddea", True),
    "src/controle_ia/runs_nuit/chaine_table_v4_v1.py": ("a015e89fd1cf39d887a05617298b7c930c939f60449b2c0ed9e75975d097bdd1", True),
    "src/controle_ia/runs_nuit/rejeu_activations_v4.py": ("d31dcec074b513b597a4920a5c6501326ee18c8cefe4bbd83d381f4ac4b25a08", True),
    "src/controle_ia/runs_nuit/resolution_graine_lot_v3.py": ("9ce6d17818a04853db57fdbb70e347bc9fdd0153ba91c14b9530818c6b29f6e3", True),
    "src/controle_ia/runs_nuit/resolution_graine_lot_v2.py": ("501ab45308f2ffe5e3cf25b0352b0d2e7f8bca0bb2ba7cd897c3b2c39b704f87", True),
    "src/controle_ia/runs_nuit/resolution_graine_lot_v1.py": ("5a9982b2a2248d5312c5a42bf34ac90c505ca579052985169aabb7e16c8c7156", True),
    "src/controle_ia/runs_nuit/resolution_graine_v1.py": ("cdc22b5ad2659f82f512c39545c52fc826a6be2dc60fb3aeafda0c5d014a9663", True),
    "src/controle_ia/manifeste.py": ("1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d", False),
    "src/controle_ia/scellement.py": ("93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2", False),
    "scripts/r1_v4_instance_v2.sh": ("a02eda0c4c8519a1d7d3ddd452001a7b8357c7e6925ca1e9c28be703d362b5ae", True),
    "scripts/amorce_instance_r1_v4_v2.sh": ("22e64d72745168f947a37690e9bb29170011ef38f0649b6bbc7ca6f8825445b1", True),
}
LOT = "python -m controle_ia.runs_nuit.resolution_graine_lot_v3"
ATTENDUS = {
    "format": FORMAT,
    "jouet": False,
    "commits": {"scellement": SCELLEMENT, "temoin_verse": TEMOIN_VERSE},
    "pieces": {k: {"sha256": v[0], "compagnon": v[1]} for k, v in PIECES.items()},
    "preenregistrement": {"chemin": "prereg/R1-addendum-relance-v4.md",
                          "sha256": "0f10881b32fa4c0e5ec1eb02cf88fbd0fcb6ad13f70b59abc2d84e45a99f61c8"},
    "config_reparation": {"chemin": "prereg/R1-reparation-v4-config-v2.json",
                          "sha256_canonique": "c34bf464177468d160975800da3cfe13d67e722a2e3b3c3e4c3c46d503ab680a"},
    "config_rejeu": {"chemin": "prereg/R1-rejeu-config-v6.json",
                     "sha256_canonique": "a3ef1bac5b8768604f2418da8b55c7adc8954f247485ea12c587bd00f407575f"},
    "table_v3": {"chemin": "prereg/R1-table-tokenisation-v3.json",
                 "sha256": "ead8a66851b2af5dfa02635297056872032878fbd2987ba780fb6c9096766423"},
    "table_v4": "prereg/R1-table-tokenisation-v4.json",
    "entropie": "36410133060804533274328900142752730279",
    "commandes": {"temoin": f"{LOT} --etape temoin", "reparation": f"{LOT} --etape reparation",
                  "rejeu": "python -m controle_ia.runs_nuit.rejeu_activations_v4"},
    "version_lot": "resolution_graine_lot_v3",
    "version_chaine": "chaine_table_v4_v1",
    "voie": "lot_fidele",
    "addendum_tokenisation": "prereg/R1-addendum-relance-v4.md",
    "table_en_session": "construite-en-session",
    "temoin": {"run": RUN_TEMOIN, "fichiers": {
        f"diag/{RUN_TEMOIN}/resolution-graine-lot-v3-temoin.json":
            "25d68f3335867e7222c1a6f24d024edff14a6141947d5e618696e8be88145dd2",
        f"diag/{RUN_TEMOIN}/resolution-graine-lot-v3-temoin.json.sha256":
            "23b4473468a806d889aa4e2aa9b73ff0beabe115b2eefdf4be87bd6465cc49c2",
        f"runs/{RUN_TEMOIN}/manifeste.json": "43e2dd5c605fc87f7aacd319ae258bbfd72a1dc27fcf6e7c3b5f6f3cc4e9ac01",
        f"runs/{RUN_TEMOIN}/manifeste.json.sha256": "d03f7bf13257554ed8b560e82f28e8a43bb9747997b205d01f1f8a76cc3f9ff4"}},
    "run_source_p3": "20261019-230011-p3-reel",
    "motifs_run": {"reparation": r"^[0-9]{8}-[0-9]{6}-r1-v4-reparation-reel$",
                   "rejeu": r"^[0-9]{8}-[0-9]{6}-r1-v4-rejeu-reel$"},
    "branches": {"source": ["calcul/r1-v4-reparation-reel-v1", "calcul/r1-v4-reparation-reel-v2"],
                 "versement": "calcul/r1-r2-reel-v1"},
    "comptes": {"episodes": 240, "T": 10, "actions": 2400, "cibles": 89, "lots": 28, "entrees_v3": 22,
                "identiques_base": 129, "seuil_non_conformes": 10},
    "npz": {"nom_sortie": "activations-p3-rejeu-v1", "couches": [7, 15, 23], "largeur": 4096,
            "principaux": {"activations-p3-rejeu-v1.npz": "moyenne", "activations-p3-rejeu-v1-maximum.npz": "maximum",
                           "activations-p3-rejeu-v1-complement-hors-cout.npz": "maximum_hors_cout"},
            "identite": ["episode", "pas", "condition", "tache"],
            "types": {"jetons_empan": "<i8", "jetons_empan_rejeu": "<i8", "couches": "<i8", "conforme_longueur": "|b1",
                      "contexte_conforme": "|b1", "ecart_fidelite": "<f8", "fidele": "|b1",
                      "trajectoire_identique": "|b1", "activations_identiques": "|b1"},
            "type_principal": "<f2"},
    "scores_p3": {"chemin": "donnees/20261019-230011-p3-reel/scores-p3.npz",
                  "sha256": "968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf"},
    "motifs_arret_rejeu": ["non conforme", "echec"],
}
# du résultat du rejeu, seules ces clés sont gardées (rien d'autre n'est conservé après le chargement)
CLES_TOKENISATION = ("addendum", "version_table", "table_sha256", "table_empreinte_citee", "non_conformes", "signales",
                     "trajectoires_identiques_base", "corrections_verifiees_au_chargement", "corrections_par_methode",
                     "par_methode_resolution", "methodes_resolution", "episodes_non_resolus", "actions_non_resolues",
                     "fideles_parmi_non_resolues", "seuil_non_conformes", "episodes_non_retrouves_v4",
                     "actions_non_retrouvees_v4")
CHEMINS_LUS_REJEU = (("run_id",), ("manifeste_sha256",), ("resultat", "verdict_fidelite"), ("resultat", "fichiers"),
                     ("resultat", "empreintes_p3", "episodes"), ("resultat", "empreintes_p3", "trajectoires_identiques"),
                     ("resultat", "fidelite_toutes", "actions")) + tuple(
    ("resultat", "tokenisation", k) for k in CLES_TOKENISATION)
CHEMINS_LUS_ARRET = (("run_id",), ("manifeste_sha256",), ("resultat", "verdict_fidelite"))
# valeurs observées de P-R5 et lectures de l'instrument : jamais gardées, écrites ni affichées (v3, section 6)
INTERDITS = ("fideles", "notees", "fideles_parmi_contextes_conformes", "notees_contextes_conformes", "egalite_exacte",
             "ecart_max", "ecart_mediane", "part_fideles_parmi_notees", "p_r5_au_moins_90_pour_cent",
             "fidelite_echantillon", "controle_negatif", "activations_identiques_au_bit", "lecture",
             "regle_repli_appliquee", "conformes_longueur", "contextes_conformes")
_LIGNE = re.compile(r"^([0-9a-f]{64})  (\S.*)$")
_HEX40 = re.compile(r"^[0-9a-f]{40}$")


class Arret(Exception):
    def __init__(self, garde, message):
        super().__init__(f"[{garde}] {message}")
        self.garde = garde


class CourseArretee(Exception):
    pass


class Controles:
    """Gardes passées, dans l'ordre ; une garde fausse arrête avec son nom (R5)."""

    def __init__(self):
        self.passees = []

    def exiger(self, garde, condition, message):
        try:
            ok = condition()
        except (KeyError, TypeError, ValueError, IndexError, AttributeError) as e:
            raise Arret(garde, f"{message() if callable(message) else message} (forme illisible : {type(e).__name__})")
        if not ok:
            raise Arret(garde, message() if callable(message) else message)
        if garde not in self.passees:
            self.passees.append(garde)


# ------------------------------------------------------------------ outils
def sha256_octets(b):
    return hashlib.sha256(b).hexdigest()


def sha256_fichier(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def blob_fichier(p):
    """Identifiant de blob git d'un fichier (sha1 de « blob <taille>\\0 » + octets), sans `git`."""
    taille = Path(p).stat().st_size
    h = hashlib.sha1(f"blob {taille}\0".encode())
    with open(p, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def canonique(config):
    """Règle de `controle_ia.manifeste.config_canonique` (clés triées, séparateurs compacts), recopiée."""
    return hashlib.sha256(json.dumps(config, sort_keys=True, ensure_ascii=False,
                                     separators=(",", ":")).encode("utf-8")).hexdigest()


def git(depot, *args, octets=False):
    r = subprocess.run(["git", "-C", str(depot), *args], capture_output=True)
    if r.returncode != 0:
        raise Arret("git", f"git {' '.join(args)} : {r.stderr.decode('utf-8', 'replace').strip()[:200]}")
    return r.stdout if octets else r.stdout.decode("utf-8")


def git_existe(depot, objet):
    return subprocess.run(["git", "-C", str(depot), "cat-file", "-e", objet], capture_output=True).returncode == 0


def arbre(depot, commit, prefixe=None):
    """{chemin : blob} des fichiers de `commit` (sous `prefixe` si donné)."""
    args = ["ls-tree", "-r", "-z", "--full-tree", commit] + ([prefixe] if prefixe else [])
    sortie = {}
    for x in git(depot, *args).split("\0"):
        if not x:
            continue
        meta, chemin = x.split("\t", 1)
        mode, genre, blob = meta.split()
        if genre == "blob":
            sortie[chemin] = blob
    return sortie


def lire_compagnon(c, nom):
    lignes = [x for x in Path(c).read_text(encoding="utf-8").splitlines() if x.strip()]
    if len(lignes) != 1:
        return None
    m = _LIGNE.match(lignes[0])
    return m.group(1) if m and m.group(2) == nom else None


def json_fichier(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def filtrer(doc, chemins):
    """Garde seulement les chemins nommés ; le reste du document n'est pas conservé."""
    garde = {}  # filtre
    for ch in chemins:
        src, dst = doc, garde
        for i, k in enumerate(ch):
            if not isinstance(src, dict) or k not in src:
                break
            if i == len(ch) - 1:
                dst[k] = src[k]
            else:
                src = src[k]
                dst = dst.setdefault(k, {})
    return garde


def lire_bloc(texte):
    if texte.count(DEBUT_BLOC) != 1 or texte.count(FIN_BLOC) != 1:
        raise Arret("fiche", "bloc d'attendus absent ou en double")
    corps = texte.split(DEBUT_BLOC, 1)[1].split(FIN_BLOC, 1)[0].strip()
    if not (corps.startswith("```json") and corps.endswith("```")):
        raise Arret("fiche", "bloc d'attendus hors de son cadre ```json")
    return json.loads(corps[len("```json"):-3])


def bloc(attendus=None):
    return json.dumps(ATTENDUS if attendus is None else attendus, indent=1, ensure_ascii=False, sort_keys=True)


def entete_npy(flux):
    """En-tête d'un membre `.npy` (format 1, 2 ou 3) : {descr, fortran_order, shape} ; aucune donnée lue."""
    magie = flux.read(8)
    if len(magie) != 8 or magie[:6] != b"\x93NUMPY" or magie[6] not in (1, 2, 3):
        raise ValueError("en-tête .npy illisible")
    n = int.from_bytes(flux.read(2 if magie[6] == 1 else 4), "little")
    if not 0 < n <= 65536:
        raise ValueError("en-tête .npy de longueur aberrante")
    texte = flux.read(n).decode("latin1" if magie[6] < 3 else "utf-8")
    d = ast.literal_eval(texte)
    if not isinstance(d, dict) or set(d) != {"descr", "fortran_order", "shape"}:
        raise ValueError("en-tête .npy de clés inattendues")
    return {"descr": d["descr"], "fortran_order": d["fortran_order"], "shape": list(d["shape"])}


def entetes_npz(p):
    """{nom du tableau : en-tête} d'un `.npz` ; membres lus jusqu'à la fin de l'en-tête seulement."""
    sortie = {}
    with zipfile.ZipFile(p) as z:
        for info in z.infolist():
            if not info.filename.endswith(".npy"):
                raise ValueError(f"membre {info.filename!r} hors format .npy")
            with z.open(info) as f:
                sortie[info.filename[:-4]] = entete_npy(f)
    return sortie


# ------------------------------------------------------------------ chemins attendus
def chemins_attendus(A, run_r, run_j):
    """Chemins ajoutés par le versement (course qui va au bout), compagnons compris."""
    c = A["comptes"]
    s = set(A["temoin"]["fichiers"])
    base = [f"runs/{run_r}/manifeste.json", f"diag/{run_r}/resolution-graine-lot-v3-reparation.json"]
    base += [f"diag/{run_r}/episodes-reparation/{k:03d}.json" for k in range(c["cibles"])]
    base += [A["table_v4"]]
    if run_j is not None:
        base += [f"runs/{run_j}/manifeste.json", f"diag/{run_j}/rejeu-activations.json"]
        base += [f"donnees/{run_j}/{n}" for n in A["npz"]["principaux"]]
    for x in base:
        s.add(x)
        s.add(x + SUFFIXE)
    return s


def dossiers_des_runs(A, run_r, run_j):
    t = A["temoin"]["run"]
    return [f"runs/{t}", f"diag/{t}", f"donnees/{t}", f"runs/{run_r}", f"diag/{run_r}", f"donnees/{run_r}",
            f"runs/{run_j}", f"diag/{run_j}", f"donnees/{run_j}"]


# ------------------------------------------------------------------ gardes
def garder_fiche(ctl, fiche, fiche_sha256, attendus_reels, jouet):
    p = Path(fiche)
    ctl.exiger("fiche", lambda: p.is_file() and Path(str(p) + SUFFIXE).is_file(),
               f"fiche {p} ou son sceau absent : la fiche doit être scellée avant la récupération (V4-E13)")
    sha = sha256_fichier(p)
    ctl.exiger("fiche", lambda: lire_compagnon(str(p) + SUFFIXE, p.name) == sha, "sceau de la fiche non conforme")
    ctl.exiger("fiche", lambda: fiche_sha256 is None or fiche_sha256 == sha,
               "empreinte de la fiche ≠ empreinte annoncée par conv-audit")
    b = lire_bloc(p.read_text(encoding="utf-8"))
    ctl.exiger("fiche", lambda: b.get("format") == FORMAT, "format du bloc d'attendus inattendu")
    if jouet:
        ctl.exiger("fiche", lambda: b.get("jouet") is True, "mode jouet sur une fiche réelle")
    else:
        ctl.exiger("fiche", lambda: b == attendus_reels, "bloc d'attendus de la fiche ≠ attendus du script")
    return b


def garder_textes(ctl, A, depot):
    c = A["commits"]
    ctl.exiger("textes", lambda: git_existe(depot, c["temoin_verse"] + "^{commit}"),
               "commit du versement du témoin absent du dépôt")
    ctl.exiger("textes", lambda: git(depot, "rev-parse", c["temoin_verse"] + "^").strip() == c["scellement"],
               "le commit du versement du témoin n'a pas pour parent le commit de scellement")
    diff = set(git(depot, "diff", "--name-only", c["scellement"], c["temoin_verse"]).split())
    ctl.exiger("textes", lambda: diff == set(A["temoin"]["fichiers"]),
               "entre scellement et versement du témoin, d'autres chemins que les quatre fichiers du témoin")
    for chemin, x in A["pieces"].items():
        b = git(depot, "show", f"{c['temoin_verse']}:{chemin}", octets=True)
        ctl.exiger("textes", lambda: sha256_octets(b) == x["sha256"], f"{chemin} : empreinte ≠ empreinte citée")
        if x["compagnon"]:
            comp = git(depot, "show", f"{c['temoin_verse']}:{chemin}{SUFFIXE}").strip()
            ctl.exiger("textes", lambda: comp == f"{x['sha256']}  {Path(chemin).name}",
                       f"{chemin} : compagnon au commit ≠ empreinte citée")
    for k in ("config_reparation", "config_rejeu"):
        conf = json.loads(git(depot, "show", f"{c['temoin_verse']}:{A[k]['chemin']}"))
        ctl.exiger("textes", lambda: canonique(conf) == A[k]["sha256_canonique"],
                   f"{A[k]['chemin']} : empreinte canonique ≠ empreinte citée")
    t = A["table_v4"]
    ctl.exiger("textes", lambda: t not in arbre(depot, c["temoin_verse"], "prereg"),
               "table v4 présente au commit du versement du témoin (R12)")
    return {k: json.loads(git(depot, "show", f"{c['temoin_verse']}:{A[k]['chemin']}"))
            for k in ("config_reparation", "config_rejeu")}, json.loads(
        git(depot, "show", f"{c['temoin_verse']}:{A['table_v3']['chemin']}"))


def garder_versement(ctl, A, depot, commit_versement, attendus_chemins, complet):
    ctl.exiger("versement", lambda: bool(_HEX40.match(commit_versement or "")) and git_existe(
        depot, commit_versement + "^{commit}"), "commit de versement absent ou non nommé par 40 hexadécimaux")
    parents = git(depot, "rev-list", "--parents", "-n", "1", commit_versement).split()[1:]
    ctl.exiger("versement", lambda: len(parents) == 1, "commit de versement à plusieurs parents (fusion interdite)")
    lignes = [x for x in git(depot, "diff", "--name-status", "--no-renames", parents[0], commit_versement).splitlines()
              if x.strip()]
    etats = {x.split("\t", 1)[1]: x.split("\t", 1)[0] for x in lignes}
    ctl.exiger("versement", lambda: all(v == "A" for v in etats.values()),
               "le versement modifie ou supprime un chemin existant (réécriture interdite)")
    # `traces/` (et tout autre chemin) hors des attendus : refusé par l'égalité ou l'inclusion ci-dessous
    if complet:
        ctl.exiger("versement", lambda: set(etats) == attendus_chemins,
                   lambda: f"chemins versés ≠ attendus (en trop : {len(set(etats) - attendus_chemins)}, en moins : "
                           f"{len(attendus_chemins - set(etats))})")
    else:
        ctl.exiger("versement", lambda: set(etats) <= attendus_chemins | {
            p for p in etats if p.endswith(("/arret.json", "/arret.json" + SUFFIXE))},
            "course arrêtée : chemins versés hors des runs et de la table attendus")
    return set(etats)


def garder_octets(ctl, A, depot, racine, commit_versement, source, chemins):
    av = arbre(depot, commit_versement)
    nom = re.sub(r"^(refs/remotes/origin/|origin/|refs/heads/)", "", source or "")
    ctl.exiger("octets", lambda: nom in A["branches"]["source"], f"branche source {source!r} non attendue")
    asrc = arbre(depot, source)
    atem = arbre(depot, A["commits"]["temoin_verse"])
    for p in sorted(chemins):
        f = Path(racine) / p
        ctl.exiger("octets", lambda: f.is_file() and blob_fichier(f) == av.get(p),
                   f"{p} : fichier de l'arbre reçu ≠ blob du commit de versement")
        ref = atem if p in A["temoin"]["fichiers"] else asrc
        ctl.exiger("octets", lambda: av.get(p) == ref.get(p),
                   f"{p} : versé ≠ {'5bd62a00' if ref is atem else 'branche source'} (à l'octet)")
    for p, sha in A["temoin"]["fichiers"].items():
        ctl.exiger("octets", lambda: sha256_fichier(Path(racine) / p) == sha, f"{p} : empreinte ≠ empreinte du témoin versé")


def garder_presence(ctl, A, racine, run_r, run_j, chemins):
    vus = set()
    for d in dossiers_des_runs(A, run_r, run_j):
        dd = Path(racine) / d
        if dd.exists():
            vus |= {str(x.relative_to(racine)) for x in dd.rglob("*") if x.is_file()}
    t4 = Path(racine) / A["table_v4"]
    vus |= {str(x.relative_to(racine)) for x in (t4, Path(str(t4) + SUFFIXE)) if x.is_file()}
    ctl.exiger("presence", lambda: vus == chemins,
               lambda: f"fichiers des runs reçus ≠ attendus (en trop : {sorted(vus - chemins)[:3]}, en moins : "
                       f"{sorted(chemins - vus)[:3]})")


def garder_compagnons(ctl, racine, chemins):
    for p in sorted(x for x in chemins if not x.endswith(SUFFIXE)):
        f = Path(racine) / p
        ctl.exiger("compagnon", lambda: Path(str(f) + SUFFIXE).is_file()
                   and lire_compagnon(str(f) + SUFFIXE, f.name) == sha256_fichier(f),
                   f"{p} : compagnon absent, mal formé ou ≠ empreinte du fichier")


def garder_manifeste(ctl, garde, A, racine, run, commande, cle_config, configs, commit_attendu, tache_entropie):
    p = Path(racine) / "runs" / run / "manifeste.json"
    m = json_fichier(p)
    ctl.exiger(garde, lambda: m["run_id"] == run, f"{run} : run_id du manifeste ≠ nom du run")
    ctl.exiger(garde, lambda: m["commande"] == commande, f"{run} : commande du manifeste ≠ « {commande} »")
    ctl.exiger(garde, lambda: m["decisif"] is True, f"{run} : manifeste non décisif")
    ctl.exiger(garde, lambda: m["preenregistrement"] == A["preenregistrement"],
               f"{run} : texte qui gouverne (`preenregistrement`) ≠ addendum v4 scellé")
    ctl.exiger(garde, lambda: m["config_sha256"] == A[cle_config]["sha256_canonique"] == canonique(m["config"]),
               f"{run} : empreinte de configuration ≠ configuration citée, ou incohérente")
    # `config` = fichier scellé : impliqué par l'égalité canonique ci-dessus et la garde `textes` (même empreinte)
    ctl.exiger(garde, lambda: commit_attendu(m["commit"]), f"{run} : commit du manifeste non attendu")
    ctl.exiger(garde, lambda: m["depot_propre"] is True and m["reserves"] == [],
               f"{run} : arbre non propre au lancement, ou réserves")
    ctl.exiger(garde, lambda: m["graines"][tache_entropie]["entropie"] == A["entropie"],
               f"{run} : entropie ≠ entropie citée")
    return m


def garder_rattachement(ctl, garde, racine, run, chemin_resultat):
    corps = json_fichier(chemin_resultat)
    sha_m = sha256_fichier(Path(racine) / "runs" / run / "manifeste.json")
    ctl.exiger(garde, lambda: corps["run_id"] == run and corps["manifeste_sha256"] == sha_m,
               f"{chemin_resultat} : non rattaché au manifeste de {run}")
    return corps


def garder_temoin(ctl, A, racine, configs):
    t = A["temoin"]["run"]
    garder_manifeste(ctl, "temoin", A, racine, t, A["commandes"]["temoin"], "config_reparation", configs,
                     lambda c: c == A["commits"]["scellement"], "aucun-tirage-propre")
    p = Path(racine) / "diag" / t / "resolution-graine-lot-v3-temoin.json"
    corps = garder_rattachement(ctl, "temoin", racine, t, p)
    r = corps["resultat"]
    ctl.exiger("temoin", lambda: r["etape"] == "temoin" and r["version"] == A["version_lot"],
               "résultat du témoin d'une autre étape ou version")
    return {"chemin": f"diag/{t}/resolution-graine-lot-v3-temoin.json", "sha256": sha256_fichier(p)}


def extraire_reparation(corps):
    """Seules clés gardées du résultat de la réparation ; ni lecture, ni comptes par condition, ni rapport des lots."""
    r = corps["resultat"]
    return {"run_id": corps["run_id"], "manifeste_sha256": corps["manifeste_sha256"], "etape": r["etape"],
            "version": r["version"], "voie": r["voie"], "run_source": r["run_source"],
            "table_v3_sha256": r["table_v3_sha256"], "cibles": list(r["cibles"]), "lots_a_cible": list(r["lots_a_cible"]),
            "temoin": {k: r["temoin"][k] for k in ("chemin", "sha256", "voie")},
            "episodes": [{"episode": x["episode"], "empreinte_retrouvee": x["empreinte_retrouvee"]} for x in r["episodes"]],
            "consignes": [{"fichier": x["fichier"], "sha256": x["sha256"]} for x in r["episodes_consignes"]]}


def garder_reparation(ctl, A, racine, run_r, configs, temoin):
    garder_manifeste(ctl, "reparation", A, racine, run_r, A["commandes"]["reparation"], "config_reparation", configs,
                     lambda c: c == A["commits"]["temoin_verse"], "aucun-tirage-propre")
    p = Path(racine) / "diag" / run_r / "resolution-graine-lot-v3-reparation.json"
    garder_rattachement(ctl, "reparation", racine, run_r, p)
    x = extraire_reparation(json_fichier(p))
    c = A["comptes"]
    ctl.exiger("reparation", lambda: x["etape"] == "reparation" and x["version"] == A["version_lot"],
               "résultat de la réparation d'une autre étape ou version")
    ctl.exiger("reparation", lambda: x["voie"] == A["voie"] and x["temoin"]["voie"] == A["voie"],
               "voie de la réparation ≠ « lot_fidele » (seule voie écrite d'avance)")
    ctl.exiger("reparation", lambda: x["temoin"]["chemin"] == temoin["chemin"] and x["temoin"]["sha256"] == temoin["sha256"],
               "la réparation ne cite pas le témoin versé (chemin et sceau)")
    ctl.exiger("reparation", lambda: x["table_v3_sha256"] == A["table_v3"]["sha256"]
               and x["run_source"] == A["run_source_p3"], "réparation sur une autre table v3 ou un autre run source")
    ctl.exiger("reparation", lambda: len(x["cibles"]) == len(set(x["cibles"])) == c["cibles"]
               and len(x["lots_a_cible"]) == c["lots"], "cibles ou lots ≠ comptes écrits d'avance")
    ctl.exiger("reparation", lambda: [e["episode"] for e in x["episodes"]] == x["cibles"]
               and all(isinstance(e["empreinte_retrouvee"], bool) for e in x["episodes"]),
               "épisodes du résultat ≠ cibles (ordre compris), ou marque de retrouvée non booléenne")
    ctl.exiger("reparation", lambda: [y["fichier"] for y in x["consignes"]] == [
        f"episodes-reparation/{k:03d}.json" for k in range(c["cibles"])], "épisodes consignés ≠ un fichier par cible")
    for y in x["consignes"]:
        f = Path(racine) / "diag" / run_r / y["fichier"]
        ctl.exiger("reparation", lambda: sha256_fichier(f) == y["sha256"],
                   f"{y['fichier']} : empreinte ≠ empreinte citée par le résultat")
    x["sha256"] = sha256_fichier(p)
    x["chemin"] = f"diag/{run_r}/resolution-graine-lot-v3-reparation.json"
    return x


# clés écrites par `construire_table_v4` par-dessus les métadonnées de la table v3 (5bd62a00, l. 1086-1090)
CLES_TABLE_V4 = {"version", "regle_v4", "table_v3_sha256", "resultat_reparation_sha256", "voie", "temoin", "comptes",
                 "corrections_verifiees", "non_resolus_v4", "episodes"}


def octets_de_table(table):
    """Sérialisation de `resolution_graine_lot_v3.ecrire_table_v4` (`chaine_table_v4_v1.octets_de_table`), recopiée."""
    return (json.dumps(table, sort_keys=True, ensure_ascii=False, indent=1) + "\n").encode("utf-8")


def garder_table(ctl, A, racine, table_v3, rep, temoin):
    p = Path(racine) / A["table_v4"]
    octets = p.read_bytes()
    t = json.loads(octets.decode("utf-8"))
    c = A["comptes"]
    ctl.exiger("table", lambda: octets == octets_de_table(t), "table v4 hors de la sérialisation de `ecrire_table_v4`")
    ctl.exiger("table", lambda: t["version"] == 4, "table de version autre que 4")
    ctl.exiger("table", lambda: t["resultat_reparation_sha256"] == rep["sha256"],
               "resultat_reparation_sha256 de la table ≠ sceau du résultat de la réparation versé")
    ctl.exiger("table", lambda: t["table_v3_sha256"] == A["table_v3"]["sha256"], "table v4 bâtie sur une autre table v3")
    ctl.exiger("table", lambda: t["voie"] == A["voie"] and t["temoin"]["sha256"] == temoin["sha256"]
               and t["temoin"]["chemin"] == temoin["chemin"], "table v4 : voie ou témoin cité ≠ attendus")
    meta_v3 = {k: v for k, v in table_v3.items() if k not in ("version", "comptes", "episodes")}
    ctl.exiger("table", lambda: set(t) == set(meta_v3) | CLES_TABLE_V4,
               "table v4 : clés ≠ clés de la table v3 plus celles de `construire_table_v4`")
    ctl.exiger("table", lambda: all(t[k] == v for k, v in meta_v3.items() if k not in CLES_TABLE_V4),
               "table v4 : métadonnées de la table v3 non reprises à l'identique")
    ctl.exiger("table", lambda: len(table_v3["episodes"]) == c["entrees_v3"]
               and t["episodes"][:c["entrees_v3"]] == table_v3["episodes"],
               "table v4 : les entrées de la table v3 ne sont pas reprises à l'identique, en tête")
    nouv = t["episodes"][c["entrees_v3"]:]
    ctl.exiger("table", lambda: [e["episode"] for e in nouv] == rep["cibles"],
               "table v4 : entrées neuves ≠ cibles de la réparation (une par cible, dans l'ordre)")
    ctl.exiger("table", lambda: all(e["methode"] in ("identifiants", "non_resolu") for e in nouv),
               "table v4 : méthode d'une entrée neuve ≠ identifiants / non_resolu")
    ctl.exiger("table", lambda: t["non_resolus_v4"] == [e["episode"] for e in nouv if e["methode"] == "non_resolu"],
               "table v4 : non_resolus_v4 ≠ entrées neuves non résolues")
    r_v4 = sum(1 for e in nouv if e["methode"] == "identifiants")
    attendu = {k: v for k, v in table_v3["comptes"].items() if k not in METHODES_V3 and k != "identiques_apres_table"}
    for m in METHODES_V3:
        attendu[m] = sum(1 for e in t["episodes"] if e["methode"] == m)
    attendu["identiques_apres_table"] = attendu["identiques_base"] + sum(attendu[m] for m in CORRIGEES_V3)
    attendu.update(non_conformes=c["cibles"], cibles_v4=c["cibles"], retrouvees_v4=r_v4)
    ctl.exiger("table", lambda: t["comptes"] == attendu, "table v4 : comptes ≠ comptes recalculés depuis ses entrées")
    ctl.exiger("table", lambda: t["corrections_verifiees"] == attendu["identiques_apres_table"] - attendu["identiques_base"],
               "table v4 : corrections_verifiees ≠ corrections de ses entrées")
    ctl.exiger("table", lambda: attendu["episodes"] == c["episodes"] and attendu["identiques_base"] == c["identiques_base"]
               and attendu["signales"] == c["entrees_v3"], "table v4 : comptes de base ≠ comptes écrits d'avance")
    return {"table": t, "sha256": sha256_fichier(p), "retrouvees": r_v4}


def garder_chaine_locale(ctl, rep, tab):
    """Partie de `chaine_table_v4_v1.exiger_chaine` faisable sans tokeniseur : identifiants = exactement les retrouvées,
    non_resolu = exactement les non retrouvées, chaque entrée « identifiants » cite le sceau du résultat."""
    retr = [e["episode"] for e in rep["episodes"] if e["empreinte_retrouvee"] is True]
    nouv = tab["table"]["episodes"][len(tab["table"]["episodes"]) - len(rep["cibles"]):]
    ident = [e["episode"] for e in nouv if e["methode"] == "identifiants"]
    ctl.exiger("chaine-locale", lambda: ident == retr, "entrées « identifiants » ≠ retrouvées de la réparation")
    ctl.exiger("chaine-locale", lambda: all(e["resolution_graine"]["resultat_sha256"] == rep["sha256"]
                                            for e in nouv if e["methode"] == "identifiants"),
               "une entrée « identifiants » ne cite pas le sceau du résultat de la réparation")


def garder_commit_rejeu(ctl, A, depot, run_r, commit, racine):
    """Commit lancé du rejeu : descendant de 5bd62a00, qui n'y ajoute que la réparation et la table v4 versées."""
    # forme (40 hexadécimaux) : garde du manifeste ; absence de l'objet : `merge-base` échoue, même arrêt
    tv = A["commits"]["temoin_verse"]
    ctl.exiger("commit-rejeu", lambda: subprocess.run(["git", "-C", str(depot), "merge-base", "--is-ancestor", tv, commit],
                                                       capture_output=True).returncode == 0,
               "commit du rejeu absent du dépôt (récupérer la branche source) ou qui ne descend pas du commit du "
               "versement du témoin")
    diff = {x for x in git(depot, "diff", "--name-only", "--no-renames", tv, commit).splitlines() if x.strip()}
    attendu = {x for x in chemins_attendus(A, run_r, "x") if x.startswith((f"runs/{run_r}/", f"diag/{run_r}/"))}
    attendu |= {A["table_v4"], A["table_v4"] + SUFFIXE}
    ctl.exiger("commit-rejeu", lambda: diff == attendu,
               "le commit du rejeu diffère de 5bd62a00 par d'autres chemins que la réparation et la table v4")
    a = arbre(depot, commit)
    ctl.exiger("commit-rejeu", lambda: all(a.get(p) == blob_fichier(Path(racine) / p) for p in attendu),
               "réparation ou table v4 au commit du rejeu ≠ versées (à l'octet)")


def garder_rejeu(ctl, A, depot, racine, run_r, run_j, configs, tab, table_v3):
    m = garder_manifeste(ctl, "rejeu", A, racine, run_j, A["commandes"]["rejeu"], "config_rejeu", configs,
                         lambda c: bool(_HEX40.match(c)), "fidelite")
    # table citée par la configuration (`prereg/R1-table-tokenisation-v4.json`, « construite-en-session ») : fixée par
    # l'égalité de `config` au fichier scellé v6 (garde du manifeste) et son empreinte canonique (garde `textes`)
    garder_commit_rejeu(ctl, A, depot, run_r, m["commit"], racine)
    p = Path(racine) / "diag" / run_j / "rejeu-activations.json"
    garder_rattachement(ctl, "rattachement", racine, run_j, p)
    d = filtrer(json_fichier(p), CHEMINS_LUS_REJEU)
    r, tk, c = d["resultat"], d["resultat"]["tokenisation"], A["comptes"]
    t = tab["table"]
    ctl.exiger("verdict", lambda: r["verdict_fidelite"] == "conforme", "verdict_fidelite ≠ « conforme »")
    ctl.exiger("table-comparee", lambda: tk["table_sha256"] == tab["sha256"]
               and t["resultat_reparation_sha256"] == sha256_fichier(
                   Path(racine) / "diag" / run_r / "resolution-graine-lot-v3-reparation.json"),
               "tokenisation.table_sha256 ≠ sceau de la table v4 versée, ou table qui ne cite pas la réparation versée")
    ctl.exiger("provenance", lambda: tk["addendum"] == A["addendum_tokenisation"],
               "tokenisation.addendum ≠ prereg/R1-addendum-relance-v4.md (V4-E14)")
    ctl.exiger("comptes", lambda: tk["version_table"] == 4 and tk["table_empreinte_citee"] is False,
               "version de table ≠ 4, ou empreinte de table dite citée")
    ctl.exiger("comptes", lambda: tk["non_conformes"] == c["cibles"] and tk["signales"] == c["entrees_v3"]
               and tk["trajectoires_identiques_base"] == c["identiques_base"]
               and tk["seuil_non_conformes"] == c["seuil_non_conformes"], "comptes fixés d'avance ≠ attendus")
    ctl.exiger("comptes", lambda: r["empreintes_p3"]["episodes"] == c["episodes"]
               and r["fidelite_toutes"]["actions"] == c["actions"], "épisodes ou actions ≠ attendus")
    ctl.exiger("comptes", lambda: tk["episodes_non_resolus"] == [] and tk["actions_non_resolues"] == 0
               and tk["fideles_parmi_non_resolues"] == 0, "règle B : non résolus parmi les signalés (aucun attendu)")
    n_retr = tab["retrouvees"]
    par_t = {e["episode"]: e["methode"] for e in t["episodes"]}
    ctl.exiger("coherence-table", lambda: tk["corrections_verifiees_au_chargement"] == t["corrections_verifiees"]
               and r["empreintes_p3"]["trajectoires_identiques"] == t["comptes"]["identiques_apres_table"],
               "corrections vérifiées ou trajectoires identiques du rejeu ≠ table v4 versée")
    ctl.exiger("coherence-table", lambda: tk["corrections_par_methode"] == {k: t["comptes"][k] for k in CORRIGEES_V3},
               "corrections_par_methode du rejeu ≠ comptes de la table v4")
    v1 = sum(1 for x in par_t.values() if methode_resolution(x) == "v1")
    v2 = sum(1 for x in par_t.values() if methode_resolution(x) == "v2")
    ctl.exiger("coherence-table", lambda: tk["par_methode_resolution"] == {
        "v1": v1, "v2": v2, "identifiants": t["comptes"]["identifiants"],
        "aucune": c["episodes"] - v1 - v2 - t["comptes"]["identifiants"]},
               "par_methode_resolution du rejeu ≠ table v4")
    ctl.exiger("coherence-table", lambda: len(tk["methodes_resolution"]) == c["episodes"] and all(
        tk["methodes_resolution"][e]["methode_table"] == mt
        and tk["methodes_resolution"][e]["methode_resolution"] == methode_resolution(mt) for e, mt in par_t.items())
               and all(v["methode_table"] is None for e, v in tk["methodes_resolution"].items() if e not in par_t),
               "methodes_resolution du rejeu ≠ méthodes de la table v4")
    ctl.exiger("coherence-table", lambda: sorted(tk["episodes_non_retrouves_v4"]) == sorted(t["non_resolus_v4"])
               and tk["actions_non_retrouvees_v4"] == c["T"] * len(t["non_resolus_v4"])
               and n_retr + len(t["non_resolus_v4"]) == c["cibles"],
               "non retrouvés v4 du rejeu ≠ non_resolus_v4 de la table versée")
    attendus_npz = set(A["npz"]["principaux"])
    ctl.exiger("fichiers", lambda: set(r["fichiers"]) == attendus_npz and all(
        r["fichiers"][n] == sha256_fichier(Path(racine) / "donnees" / run_j / n) for n in attendus_npz),
               "resultat.fichiers ≠ empreintes des trois .npz versés")
    return d


def garder_npz(ctl, A, racine, run_j, scores_p3):
    N, c = A["npz"], A["comptes"]
    ctl.exiger("npz", lambda: scores_p3 is not None and Path(scores_p3).is_file()
               and sha256_fichier(scores_p3) == A["scores_p3"]["sha256"],
               "fichier des scores de P3 absent ou d'empreinte ≠ citée (identité des tableaux)")
    ref = entetes_npz(scores_p3)   # tableaux d'identité absents ou d'autre forme : refusés plus bas (forme == [n])
    n, d = c["actions"], len(N["couches"])
    for nom, principal in N["principaux"].items():
        e = entetes_npz(Path(racine) / "donnees" / run_j / nom)
        attendus = {principal, *N["identite"], *N["types"]}
        ctl.exiger("npz", lambda: set(e) == attendus,
                   lambda: f"{nom} : tableaux ≠ attendus (en trop {sorted(set(e) - attendus)}, "
                           f"en moins {sorted(attendus - set(e))})")
        ctl.exiger("npz", lambda: all(not h["fortran_order"] for h in e.values()), f"{nom} : ordre Fortran")
        ctl.exiger("npz", lambda: e[principal]["descr"] == N["type_principal"]
                   and e[principal]["shape"] == [n, d, N["largeur"]], f"{nom} : `{principal}` hors forme ou type")
        for k, ty in N["types"].items():
            forme = [d] if k == "couches" else [n]
            ctl.exiger("npz", lambda: e[k]["descr"] == ty and e[k]["shape"] == forme, f"{nom} : `{k}` hors forme ou type")
        for k in N["identite"]:
            ctl.exiger("npz", lambda: e[k]["descr"] == ref[k]["descr"] and e[k]["shape"] == ref[k]["shape"] == [n],
                       f"{nom} : `{k}` ≠ forme ou type du tableau d'identité de P3")


def garder_recalcul(ctl, A, depot, sortie_recalcul, racine_recalcul, racine, run_r, rep, tab):
    ctl.exiger("recalcul", lambda: sortie_recalcul is not None and Path(sortie_recalcul).is_file(),
               "sortie du recalcul de réception absente (commande de l'étape 4 non jouée)")
    lignes = [x for x in Path(sortie_recalcul).read_text(encoding="utf-8").splitlines() if x.strip()]
    ctl.exiger("recalcul", lambda: len(lignes) == 1, "sortie du recalcul : une seule ligne JSON attendue")
    s = json.loads(lignes[0])
    ctl.exiger("recalcul", lambda: s["version"] == A["version_chaine"] and s["recalcul_egal_a_l_octet"] is True,
               "recalcul : chaîne non conforme ou table recalculée ≠ table versée (à l'octet)")
    ctl.exiger("recalcul", lambda: s["table"] == A["table_v4"] and s["table_sha256"] == tab["sha256"]
               and s["reparation"] == rep["chemin"] and s["resultat_reparation_sha256"] == rep["sha256"]
               and s["run_reparation"] == run_r and s["table_v3_sha256"] == A["table_v3"]["sha256"],
               "recalcul fait sur d'autres pièces que les pièces versées")
    ctl.exiger("recalcul", lambda: s["cibles"] == A["comptes"]["cibles"] and s["entrees_v3"] == A["comptes"]["entrees_v3"]
               and s["retrouvees"] == tab["retrouvees"] and s["non_retrouvees"] == A["comptes"]["cibles"] - tab["retrouvees"],
               "recalcul : comptes ≠ table versée")
    ctl.exiger("recalcul", lambda: racine_recalcul is not None and Path(racine_recalcul).is_dir(),
               "arbre du recalcul non donné")
    src = arbre(depot, A["commits"]["temoin_verse"], "src")
    rr = Path(racine_recalcul)
    vus = {str(x.relative_to(rr)) for x in (rr / "src").rglob("*") if x.is_file() and "__pycache__" not in x.parts
           and not any(q.endswith(".egg-info") for q in x.parts)}
    ctl.exiger("recalcul", lambda: vus == set(src) and all(blob_fichier(rr / p) == b for p, b in src.items()),
               "arbre `src/` du recalcul ≠ `src/` du commit 5bd62a00")
    for cle in ("config_reparation",):
        p = A[cle]["chemin"]
        ctl.exiger("recalcul", lambda: blob_fichier(rr / p) == arbre(depot, A["commits"]["temoin_verse"], p).get(p),
                   f"{p} de l'arbre du recalcul ≠ fichier scellé")
    for p in (rep["chemin"], f"runs/{run_r}/manifeste.json", A["table_v4"]):
        ctl.exiger("recalcul", lambda: blob_fichier(rr / p) == blob_fichier(Path(racine) / p),
                   f"{p} de l'arbre du recalcul ≠ fichier versé")


# ------------------------------------------------------------------ arrêts reçus
def garder_arret_recu(ctl, A, racine, run, garde, rejeu):
    p = Path(racine) / "diag" / run / "arret.json"
    corps = garder_rattachement(ctl, garde, racine, run, p)
    if rejeu:
        d = filtrer(corps, CHEMINS_LUS_ARRET)
        ctl.exiger(garde, lambda: d["resultat"]["verdict_fidelite"] in A["motifs_arret_rejeu"],
                   "arret.json du rejeu : motif hors de la liste fermée")
        return d["resultat"]["verdict_fidelite"]
    return None


# ------------------------------------------------------------------ verifier
def verifier(A, *, fiche, depot, racine, commit_versement, source, run_r, run_j, scores_p3, sortie_recalcul,
             racine_recalcul, fiche_sha256=None, jouet=False):
    ctl = Controles()
    b = garder_fiche(ctl, fiche, fiche_sha256, ATTENDUS, jouet)
    if jouet:
        A = b
    ctl.exiger("runs", lambda: bool(re.match(A["motifs_run"]["reparation"], run_r or ""))
               and (run_j is None or bool(re.match(A["motifs_run"]["rejeu"], run_j))),
               "noms des runs hors des formes attendues")
    configs, table_v3 = garder_textes(ctl, A, depot)
    chemins = chemins_attendus(A, run_r, run_j)
    arret_r = (Path(racine) / "diag" / run_r / "arret.json").is_file()
    arret_j = run_j is not None and (Path(racine) / "diag" / run_j / "arret.json").is_file()
    complet = run_j is not None and not (arret_r or arret_j)
    if complet:
        garder_versement(ctl, A, depot, commit_versement, chemins, True)
        garder_octets(ctl, A, depot, racine, commit_versement, source, chemins)
        garder_presence(ctl, A, racine, run_r, run_j, chemins)
        garder_compagnons(ctl, racine, chemins)
        temoin = garder_temoin(ctl, A, racine, configs)
        rep = garder_reparation(ctl, A, racine, run_r, configs, temoin)
        tab = garder_table(ctl, A, racine, table_v3, rep, temoin)
        garder_chaine_locale(ctl, rep, tab)
        garder_rejeu(ctl, A, depot, racine, run_r, run_j, configs, tab, table_v3)
        garder_npz(ctl, A, racine, run_j, scores_p3)
        garder_recalcul(ctl, A, depot, sortie_recalcul, racine_recalcul, racine, run_r, rep, tab)
        return ctl, "RÉCEPTION CONFORME"
    # course arrêtée : réception de l'arrêt seulement (manifestes, rattachement, motif fermé) ; aucune table, aucun npz
    verses = garder_versement(ctl, A, depot, commit_versement, chemins | {
        f"diag/{r}/arret.json{s}" for r in (run_r, run_j) if r for s in ("", SUFFIXE)}, False)
    garder_octets(ctl, A, depot, racine, commit_versement, source, verses)
    garder_compagnons(ctl, racine, verses)
    garder_temoin(ctl, A, racine, configs)
    garder_manifeste(ctl, "reparation", A, racine, run_r, A["commandes"]["reparation"], "config_reparation", configs,
                     lambda c: c == A["commits"]["temoin_verse"], "aucun-tirage-propre")
    if arret_r:
        garder_arret_recu(ctl, A, racine, run_r, "arret-reparation", False)
        raise CourseArretee(f"réparation {run_r} arrêtée (arret.json) : table et rejeu absents ; nœud porté à Lazar")
    if run_j is None:
        ctl.exiger("reparation", lambda: (Path(racine) / "diag" / run_r / "resolution-graine-lot-v3-reparation.json").is_file(),
                   "rejeu absent sans résultat de la réparation ni arret.json")
        raise CourseArretee("rejeu absent (étape « table-v4 » ou « chaine » arrêtée) : rien n'est lu ; nœud porté à Lazar")
    garder_manifeste(ctl, "rejeu", A, racine, run_j, A["commandes"]["rejeu"], "config_rejeu", configs,
                     lambda c: bool(_HEX40.match(c)), "fidelite")
    motif = garder_arret_recu(ctl, A, racine, run_j, "arret-rejeu", True)
    raise CourseArretee(f"rejeu {run_j} arrêté, verdict_fidelite « {motif} » : rien n'est lu ; nœud porté à Lazar")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("bloc", help="imprime le bloc d'attendus de la fiche")
    v = sp.add_parser("verifier", help="vérifie une copie récupérée contre la fiche")
    v.add_argument("--fiche", required=True)
    v.add_argument("--fiche-sha256", default=None, help="empreinte de la fiche annoncée par conv-audit")
    v.add_argument("--depot", required=True, help="dépôt git (objets du versement, de la source, de 5bd62a00)")
    v.add_argument("--racine", required=True, help="arbre de travail du commit de versement")
    v.add_argument("--commit-versement", required=True)
    v.add_argument("--source", required=True, help="référence de la branche source (calcul/r1-v4-reparation-reel-v1)")
    v.add_argument("--run-reparation", required=True)
    v.add_argument("--run-rejeu", default=None, help="absent : course arrêtée avant le rejeu")
    v.add_argument("--scores-p3", default=None)
    v.add_argument("--sortie-recalcul", default=None)
    v.add_argument("--racine-recalcul", default=None)
    v.add_argument("--jouet", action="store_true", help="essais seulement : attendus lus dans une fiche jouet")
    a = ap.parse_args(argv)
    if a.cmd == "bloc":
        print(bloc())
        return 0
    try:
        ctl, verdict = verifier(ATTENDUS, fiche=a.fiche, depot=a.depot, racine=a.racine,
                                commit_versement=a.commit_versement, source=a.source, run_r=a.run_reparation,
                                run_j=a.run_rejeu, scores_p3=a.scores_p3, sortie_recalcul=a.sortie_recalcul,
                                racine_recalcul=a.racine_recalcul, fiche_sha256=a.fiche_sha256, jouet=a.jouet)
    except Arret as e:
        print(f"ARRÊT {e}", file=sys.stderr)
        return 2
    except CourseArretee as e:
        print(f"COURSE ARRÊTÉE : {e}")
        return 3
    except (OSError, ValueError, KeyError, TypeError, zipfile.BadZipFile) as e:
        print(f"ARRÊT [lecture] {type(e).__name__} : {str(e)[:200]}", file=sys.stderr)
        return 2
    print(f"{verdict} ; gardes passées : {', '.join(ctl.passees)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
