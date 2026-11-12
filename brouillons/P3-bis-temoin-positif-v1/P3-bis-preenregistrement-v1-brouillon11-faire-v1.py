"""Brouillon 11 du préenregistrement de P3-bis : brouillon 10 + couples B11-01 à B11-47 (code proposé `a1de3915` et chaîne
`614fd5da` ; décisions D-1 à D-4 de R-2103 écrites à la lettre du code ; voie normale d'ouverture ; préalables vérifiables
du scellement ; calendrier ; ce que les auteurs savaient). Écrit par un rédacteur neuf, sous-agent de la session mère
`session_01QPDgKgACWyCkCN8HjqwNXy`, le 10 novembre 2026, sur l'ordre de la mère (R-2131), avec la méthode de la consigne
du brouillon 10, `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/consigne-redaction-p3bis-brouillon10-v1.md`
(`0fea27bd…`).

Chaque « ancien » doit apparaître exactement une fois dans le texte en cours d'application, sinon arrêt sans rien écrire
(R5) ; la sortie et le journal ne doivent pas exister (R12). Le journal consigne : empreintes de l'entrée, des couples et de
ce script ; chaque couple (section, gelée ou non) ; comparaison de chaque section gelée au brouillon 10 (et contrôle que les
couples non gelés n'en touchent aucune) ; marqueurs restants et marqueurs remplis ; `controle_ia.prereg.problemes` ; formes
que la chaîne de session lit dans le texte (recopiées de `verifications_p3bis_v1.py` et de
`controles_avant_depense_p3bis_v1.sh` au commit `614fd5da` de `prep/p3bis-lanceur-v1`) ; valeurs remplies, recalculées par
`git` en lecture seule (commit du code, identité avec P3, empreintes, pièces sur `main`, sortie v3 de l'essai de
fermeture) ; constantes du code (`a1de3915`) et de la chaîne (`614fd5da`) que le texte cite. Aucun appel externe, aucune
écriture git ; rien d'autre n'est écrit.

Usage, depuis la racine du dépôt :
  PYTHONPATH=src python <ce script> "$(date -u +%Y-%m-%dT%H:%M:%SZ)"            # écrit le brouillon 11 et le journal
  PYTHONPATH=src python <ce script> --essai COUPLES.json "$(date -u +…)"        # rien d'écrit dans le dépôt
L'heure passée en argument est relevée par `date -u` (règle des heures)."""
import ast
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

from controle_ia.prereg import problemes, sections

DOSSIER = Path("brouillons/P3-bis-temoin-positif-v1")
ENTREE = DOSSIER / "P3-bis-preenregistrement-v1-brouillon10.md"
SORTIE = DOSSIER / "P3-bis-preenregistrement-v1-brouillon11.md"
COUPLES = DOSSIER / "P3-bis-preenregistrement-v1-brouillon11-couples-v1.json"
JOURNAL = DOSSIER / "P3-bis-preenregistrement-v1-brouillon11-journal-v1.txt"
EMPREINTE_ENTREE = "9038a015c5756a289bebd2f08b1c33b1f2a26eb829bb2c4bc2afec04648fd1f9"
EMPREINTE_COUPLES = "52074c5da7a3e287ce3a59ff2ff952c19ab02630599f0c0f0589de2b3399cfbb"
GELEES = ("Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Plan d'analyse",
          "Critères de lecture gelés", "Liste d'arrêt")
MARQUEURS_ATTENDUS = {"CHAINE_P3BIS", "CONTRE_LECTURE_4_P3BIS", "EMPREINTE_CONFIG_P3BIS", "EMPREINTE_CONSIGNES_P3BIS",
                      "LONGUEURS_P3BIS", "TESTS_ATTENDUS_P3BIS"}
MARQUEURS_REMPLIS = ("COMMIT_CODE_P3BIS", "IDENTITE_CODE_P3BIS", "EMPREINTES_CODE_P3BIS", "PIECES_SUR_MAIN_P3BIS",
                     "ESSAI_FERMETURE_P3BIS")
# --- commits lus (lecture seule, `git show` et `git diff`) ------------------------------------------------------------
CODE = "a1de39151ebae29138a389829751397074239615"         # commit du code proposé (R-2113)
CODE_V2 = "02217f1cf5255ef87c42285fc579d38c5a6ff003"      # commit du code du brouillon 10 (R-2085)
CHAINE = "614fd5da4d63b3849f40d5dbf320ccb50d1a1330"       # tête de prep/p3bis-lanceur-v1 à la rédaction
ESSAI_COMMIT = "8ad2927313570c743925d11518f4c4a83e0e715d" # commit qui verse la sortie v3 de l'essai de fermeture
CODE_P3 = "7a54d431d89745839220f882b41b13e8c62ecfdd"      # commit du code de P3 (identité)
MAIN = "ea4f519d70b59a14071ab639d3e248ae8944d296"         # commit de main où les pièces sont recalculées
# --- formes lues par la chaîne de session (commit 614fd5da) ------------------------------------------------------------
GO_CALCUL = "GO-2026-11-10-02"
DEPOT_URL = "https://github.com/lciric/controle-ia-travail.git"
MOTIF_GO = r"GO-\d{4}-\d{2}-\d{2}-\d{2}"
VALEURS_TEXTE = (
    "au plus 2,10 USD de l'heure", "fiabilité ≥ 0,98", "stockage au plus 0,08 USD de l'heure",
    "téléchargement au plus 0,05 USD par Go", "au moins 30 cœurs effectifs", "128 000 Mo de mémoire vive",
    "disque ≥ 80 Go", "processeur AMD EPYC 7513 exigé d'abord", "douze essais à 15 minutes d'intervalle",
    "plafond exactement 80 USD", "création au plus tard le 23 novembre 2026",
    "aucune création, relance comprise, après le 18 novembre 2026",
    "≥ 20 USD plus 10 heures du prix des instances nommées en marche",
    "l'absence de ligne `PROGRES` pendant deux heures donne une alerte",
    "`duree_max_s` et `budget_entrainement_s` à `null`", "aucun `timeout`", "16 783 360 octets",
    f"`DEPOT_URL={DEPOT_URL}`", f"`GO_ID={GO_CALCUL}`")
INTITULES = ("Configuration de P3 (empreinte canonique)", "Tâches de P3", "Commit du code d'analyse", "Entropie",
             "Tests attendus", "Chemin de la configuration de P3", "Chemin des tâches de P3", "Chemin des consignes de P3")
TACHES_SHA = "287e83485cba550098b80db809589398d8f2826c02dfa9cc2719a1063795d5aa"
# --- valeurs remplies par ce brouillon, recalculées ici ---------------------------------------------------------------
CHEMINS_IDENTITE = ("src/controle_ia/premier_test_ia src/controle_ia/sondes src/controle_ia/harnais "
                    "src/controle_ia/environnements src/controle_ia/organismes src/controle_ia/bases "
                    "src/controle_ia/manifeste.py src/controle_ia/gardes.py src/controle_ia/scellement.py "
                    "src/controle_ia/prereg.py requirements-gpu.txt requirements-cpu.txt requirements-donnees.txt").split()
IDENTITE_SHA = "65a09fb52ab479a69b109859899efa95c8b92966e0fa2c5d8e70002e8d0c7708"
CHANGES_V2_CODE = {"src/controle_ia/premier_test_ia/ouverture_p3bis_v2.py",
                   "src/controle_ia/premier_test_ia/ouverture_p3bis_v2.py.sha256",
                   "tests/test_premier_test_ia_ouverture_p3bis_v2.py", "tests/test_premier_test_ia_ouverture_p3bis_v2.py.sha256",
                   "tests/test_premier_test_ia_ouverture_p3bis_v2_exclusion_v1.py",
                   "tests/test_premier_test_ia_ouverture_p3bis_v2_exclusion_v1.py.sha256",
                   "tests/test_premier_test_ia_ouverture_p3bis_v2_journal_v1.py",
                   "tests/test_premier_test_ia_ouverture_p3bis_v2_journal_v1.py.sha256"}
# arbre gelé : copie de `CHEMINS_GELES` (`src/controle_ia/harnais/validation_reelle.py` l. 71-73, commit du code), relue
CHEMINS_GELES = (".", ":(exclude)prereg", ":(exclude)brouillons", ":(exclude)registres", ":(exclude)docs",
                 ":(exclude)diag", ":(exclude)runs", ":(exclude)donnees", ":(exclude)livrables", ":(exclude)papiers",
                 ":(exclude)traces", ":(exclude)CLAUDE.md")
ESSAI_CHEMIN = "brouillons/P3-bis-temoin-positif-v1/essai-fermeture-p3bis-v2-sortie-v3.txt"
ESSAI_EMPREINTE = "57d3467c7b7d700932da64ac449ca6a6dd9aed9fda1eee64d88c79f531382c78"
LIGNE_ESSAI_CONFORME = "ESSAI DIFFÉRENTIEL DE FERMETURE : CONFORME"
EMPREINTES = {
    "src/controle_ia/premier_test_ia/run_v2.py": "83ebeac77d171d62832af47c95f6a00b94aa75a7afe3b29dacd600ccb8b9e6d5",
    "src/controle_ia/premier_test_ia/lecture_p3bis_v1.py": "bfe0effcfa0d7f525872410a7f9823c509cac878143a4fdcce7d207dfbddfea9",
    "src/controle_ia/premier_test_ia/ouverture_p3bis_v2.py": "1361382e669f26d5568c81044e160c7fc122f4264832ffb70ec8d9b4714d2a13",
    "src/controle_ia/premier_test_ia/ouverture_p3bis_v1.py": "8972bfb1c1b7530488ff26f31254bfcb71a96b5d43b6ded0c618b75f93a1a660",
    "tests/test_premier_test_ia_run_v2.py": "b93e6e8957afb2269a956240e9b64b0128fbe7459e18cb7a93b35ea515f53911",
    "tests/test_premier_test_ia_lecture_p3bis_v1.py": "27b56ced8fe821c9421b81fcc2240a5a3404fc45fb88b4bb8039d50a8d1b6b2f",
    "tests/test_premier_test_ia_lecture_p3bis_gardes_v1.py": "c0520b385b9c88cc8523844a1282048acebc9413c10a4efa9c4c95f5db692b7a",
    "tests/test_premier_test_ia_ouverture_p3bis_v1.py": "b767f6925c8b9f65b6f9e432c04c9f255eec8f21a2589256caa4fc7a9f63b0cc",
    "tests/test_premier_test_ia_ouverture_p3bis_v2.py": "8ba89a7bb5b8cedfa1acbec2383f81317eea3a70229158f00ce19bc3779b6e78",
    "tests/test_essai_fermeture_p3bis_v1.py": "855d2488880d85b4aac43d16e2bde92c5b29ccef3af95995ac442dfc95852ea0",
    "tests/test_essai_fermeture_p3bis_v2.py": "fc6bce8bc6a3c58f40d0bbce36279926efbfdd62bb1d76428f634bb0be51a5a5",
    "tests/test_script_p3bis_v1.py": "61aa739240b5a9de000818c1aa5681d8d0761670f660a858067966038a76835a",
    "tests/test_script_p3bis_v2.py": "86f020219dfc4806bd356fd538c6691bdc926d0fce87891bc6d1aa9bfc6f1eb7",
    "tests/test_premier_test_ia_ouverture_p3bis_v2_exclusion_v1.py": "259454a38e4888a866a4fe1ab09d82dd2609f0f44ad6d10ad5595ca5a98f5389",
    "tests/test_premier_test_ia_ouverture_p3bis_v2_journal_v1.py": "3ef82a97a266c6082ee517bca648d8e30870bd3e2ae9765aae74ef76ea4a979a",
    "scripts/essais-cibles-p3bis-v2.txt": "3ecf3cdaee807ec4e74059132b4bded1962fb576e3adba6c31e8f64206f62276",
    "scripts/essai_fermeture_p3bis_v2.py": "389ca52dbf145de6028667354180dac82ca4a87328262ef2ab18a290841987ef",
    "scripts/essai_fermeture_p3bis_v1.py": "166e08e4d05f13dfe4decbab0ff491ef0005d8bd8026a68d16ba398c8fdc1a0d",
    "scripts/amorce_instance_p3bis_v2.sh": "b331e44f763f87744b9669998c8a7aa32308e449d07ba414e6c2bb0bc4ed22f4",
    "scripts/p3bis_instance_v2.sh": "83820dfd8ef7205c44f89e63450d801d60b95eddecb504cd2af992fa5b1eaa5d",
    ".claude/hooks/garde_calcul.py": "184b3bbd92e95a10af2237c939b33ddce61c5bee7c7526076a1c91d863588502",
}
PIECES = {
    "brouillons/P3-bis-temoin-positif-v1/P3-bis-consignes-v1-brouillon2.md":
        "7d35576d65c030edcc6441e142ea95732679b674edcb1fd1af86ab8f69c04367",
    "brouillons/P3-bis-temoin-positif-v1/P3-bis-temoin-positif-config-v1-brouillon1.json":
        "8ab04d54531208b248fad8262283644c3ebd7e25cae10643657fdeccb6a6dbe1",
    "brouillons/P3-bis-temoin-positif-v1/puissance_p3_bis_v2.py":
        "c9d0b6c310743d33248cd21b9cc45c9ab0668addc88532c2bb6e72db9c3884bc",
    "brouillons/P3-bis-temoin-positif-v1/puissance-p3-bis-v2.txt":
        "1df8311fbdeceeb0a33c5f053d39eb7b7a6216b397f346eae8fb4af083240ae7",
    "brouillons/P3-bis-temoin-positif-v1/contre-lecture-brouillon2-v1/contre-lecture-p3-bis-brouillon2-v1.md":
        "8399dc55ae358712ca97b4cffa5f79d98e45207ad25494b8abc01c98b7921ae0",
    "brouillons/P3-bis-temoin-positif-v1/contre-lecture-brouillon2-v1/couples-contre-lecture-p3-bis-brouillon2-v1.json":
        "2c55346b8f3fd4d423642827ef8ead63fbbb73b88948cdc7ce6047bda281888c",
}
MODULE = "src/controle_ia/premier_test_ia/ouverture_p3bis_v2.py"
# (chaîne exacte dans le module au commit du code, chaîne que le texte doit porter), pour D-1 à D-4 et les constantes
CODE_ET_TEXTE = (
    ('PREREG_T07 = "prereg/T0.7-sondes-v0-v1.md"', "`prereg/T0.7-sondes-v0-v1.md`"),
    ('RENDEZ_VOUS = re.compile(r"RENDEZ-VOUS-P3BIS-([1-9][0-9]*)")', "`RENDEZ-VOUS-P3BIS-[1-9][0-9]*`"),
    ('DATE_RENDEZ_VOUS = "2026-11-20T12:00:00Z"', "2026-11-20T12:00:00Z"),
    ("mode suit le registre, jamais l'opérateur (D-2, R-2103)", "le mode suit le registre, jamais l'opérateur (D-2, R-2103)"),
    ("class HorlogeEnArriere(JournalImpossible)", "horloge antérieure à la date de la dernière ligne du journal"),
    ("exiger_horloge(racine, instant)", "refus sans ligne"),
    ("fichier vide (0 octet)", "fichier **vide** (0 octet)"),
    ("dates non décroissantes exigées (D-1)", "**les dates ne décroissent jamais**"),
    ("attendu (D-4, R-2103)", "attendu (D-4, R-2103)"),
    ('"ni-scores-ni-ouvrir"', "`ni-scores-ni-ouvrir`"),
)


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def git(*args: str) -> bytes:
    r = subprocess.run(["git", *args], capture_output=True)
    if r.returncode != 0:
        raise SystemExit(f"git {' '.join(args)[:120]} : code {r.returncode} ({r.stderr.decode('utf-8', 'replace').strip()[:200]})")
    return r.stdout


def appliquer(t: str, couples: list) -> tuple[str, list]:
    lignes = []
    for c in couples:
        n = t.count(c["ancien"])
        if n != 1:
            sys.exit(f"couple {c['id']} : ancien trouvé {n} fois (1 exigé) ; rien n'est écrit")
        t = t.replace(c["ancien"], c["nouveau"])
        g = c["section_gelee"]
        lignes.append(f"{c['id']}\t{'GELÉE : ' + g if g else 'non gelée'}\t{c['section']}\tancien 1 fois\t"
                      f"{len(c['ancien'])} → {len(c['nouveau'])} caractères\t{c['motif']}")
    return t, lignes


def plat(t: str) -> str:
    return re.sub(r" +", " ", t.replace("\n", " "))


def sans_gras(t: str) -> str:
    return " ".join(t.replace("**", "").split())


def controles_texte(t10: str, t11: str, couples: list) -> list[tuple[bool, str]]:
    r = []
    s10, s11 = sections(t10), sections(t11)
    declarees = {}
    for c in couples:
        if c["section_gelee"]:
            declarees.setdefault(c["section_gelee"], []).append(c["id"])
    for g in GELEES:
        egale = s10.get(g) == s11.get(g)
        d = declarees.get(g, [])
        if egale:
            r.append((not d, f"section gelée « {g} » : égale à l'octet au brouillon 10" + (f" (mais couples déclarés {d})" if d else "")))
        else:
            r.append((bool(d), f"section gelée « {g} » : modifiée par {', '.join(d) if d else 'AUCUN COUPLE DÉCLARÉ'}"))
    for g in declarees:
        r.append((g in GELEES, f"section déclarée gelée « {g} » connue"))
    t_ng, _ = appliquer(t10, [c for c in couples if not c["section_gelee"]])
    sng = sections(t_ng)
    touchees = [g for g in GELEES if sng.get(g) != s10.get(g)]
    r.append((not touchees, "couples non gelés appliqués seuls : aucune section gelée touchée" if not touchees
              else f"couples non gelés qui touchent {touchees}"))
    neuves = [x for x in s11 if x not in s10]
    r.append((neuves == ["0 ter. Ce que les auteurs savaient avant le scellement", "Table « ce qui change du 10 au 11 »",
                         "Préalables vérifiables du scellement (étapes du candidat)"]
              or sorted(neuves) == sorted(["0 ter. Ce que les auteurs savaient avant le scellement",
                                           "Table « ce qui change du 10 au 11 »",
                                           "Préalables vérifiables du scellement (étapes du candidat)"]),
              f"sections neuves (hors des sections gelées) : {neuves}"))
    r.append((all(x in s11 for x in s10), "aucune section du brouillon 10 retirée"))
    # marqueurs
    trouves = re.findall(r"<<([A-Z0-9_]+)>>", t11)
    compte = {m: trouves.count(m) for m in sorted(set(trouves))}
    r.append((set(compte) == MARQUEURS_ATTENDUS and all(v == 1 for v in compte.values()),
              f"marqueurs restants : {len(compte)} distincts, {compte}"))
    r.append((not any(f"<<{m}>>" in t11 for m in MARQUEURS_REMPLIS),
              f"marqueurs remplis, absents avec chevrons : {', '.join(MARQUEURS_REMPLIS)}"))
    # formes lues par la chaîne
    m = re.findall(rf"^- GO : \*\*({MOTIF_GO})\*\*", t11, re.M)
    r.append((m == [GO_CALCUL] and len(re.findall(r"^- GO :", t11, re.M)) == 1,
              f"chaîne, `go` : une seule ligne « - GO : **…** », {m}"))
    lanc = [x for x in t11.split("\n") if x.startswith("- Lancement : ")]
    ok = len(lanc) == 1 and re.findall(rf"`GO_ID=({MOTIF_GO})`", lanc[0]) == [GO_CALCUL] \
        and set(re.findall(MOTIF_GO, lanc[0])) == {GO_CALCUL}
    r.append((ok, f"chaîne, `go` : première ligne « - Lancement : » unique, seul GO cité {GO_CALCUL}"))
    r.append(("`PREREG=prereg/P3-bis-temoin-positif-v1.md`, `BRANCHE=calcul/p3bis-reel-v1`" in t11
              and f"`DEPOT_URL={DEPOT_URL}`" in t11, "chaîne, contrôles bloc 12 : PREREG, BRANCHE, DEPOT_URL"))
    sg = sans_gras(t11)
    manquantes = [v for v in VALEURS_TEXTE if v not in sg]
    r.append((not manquantes, f"chaîne, `valeurs` : {len(VALEURS_TEXTE) - len(manquantes)} sur {len(VALEURS_TEXTE)}"
              + (f" ; manquantes {manquantes}" if manquantes else "")))
    doubles = {x: t11.count(f"{x} : `") for x in INTITULES if t11.count(f"{x} : `") != 1}
    r.append((not doubles, "chaîne, contrôles bloc 12 : huit intitulés lus une fois chacun" + (f" ; {doubles}" if doubles else "")))
    cites = re.findall(r"Commit du code d'analyse : `([0-9a-f]{40})`", t11)
    r.append((cites == [CODE] and t11.count("Commit du code d'analyse : `") == 1,
              f"chaîne, contrôles bloc 2 : commit du code cité une fois, {cites}"))
    r.append((t11.count(f"Tâches de P3 : `{TACHES_SHA}`") == 1, "chaîne, contrôles bloc 4 : tâches citées une fois par leur empreinte"))
    p = plat(t11)
    r.append((f"`{ESSAI_CHEMIN}` (`{ESSAI_EMPREINTE}`" in p,
              "chaîne, contrôles bloc 6 : sortie v3 de l'essai de fermeture citée « `chemin` (`sha256` »"))
    for f in ("scripts/amorce_instance_p3bis_v2.sh", "scripts/p3bis_instance_v2.sh"):
        r.append((f"`{f}` (`{EMPREINTES[f]}`" in p, f"chaîne, contrôles bloc 11 : {f} cité « `chemin` (`sha256` »"))
    r.append(("06e84ff732ebd7b30c33e18bdab7ea979fadb7d290da92c71383ac82072dceb5" not in t11.split("## Plan d'analyse")[1].split("## Critères")[0],
              "plan d'analyse : la sortie v1 de l'essai n'y est plus citée en entier (remplacée par la v3)"))
    return r


def controles_git(t11: str) -> tuple[list[tuple[bool, str]], list[str]]:
    r, identite = [], []
    p = plat(t11)
    # commit du code
    r.append((git("rev-parse", "--verify", f"{CODE}^{{commit}}").decode().strip() == CODE
              and subprocess.run(["git", "merge-base", "--is-ancestor", CODE_V2, CODE]).returncode == 0
              and subprocess.run(["git", "merge-base", "--is-ancestor", CODE, CHAINE]).returncode == 0,
              f"commit du code {CODE[:8]} : existe, descend de {CODE_V2[:8]}, ancêtre de {CHAINE[:8]}"))
    geles = git("show", f"{CODE}:src/controle_ia/harnais/validation_reelle.py").decode("utf-8")
    i0 = geles.index("CHEMINS_GELES = (")
    lus = ast.literal_eval(geles[i0 + len("CHEMINS_GELES = "):geles.index("\nREVISION_CITEE", i0)].strip())
    r.append((lus == CHEMINS_GELES, f"CHEMINS_GELES du commit du code égaux à la copie de ce script ({len(lus)} motifs)"))
    noms = set(git("diff", "--name-only", "--no-renames", CODE_V2, CODE, "--", *CHEMINS_GELES).decode().split())
    r.append((noms == CHANGES_V2_CODE, f"de {CODE_V2[:8]} à {CODE[:8]}, arbre gelé (CHEMINS_GELES) : {len(noms)} chemins, "
              "ceux que cite l'en-tête" if noms == CHANGES_V2_CODE else f"chemins inattendus : {sorted(noms ^ CHANGES_V2_CODE)}"))
    for chemin in (".claude", "requirements-gpu.txt", "requirements-cpu.txt", "requirements-donnees.txt"):
        r.append((git("diff", "--name-only", CODE_V2, CODE, "--", chemin) == b"", f"{chemin} inchangé de {CODE_V2[:8]} à {CODE[:8]}"))
    # identité avec P3
    sortie = git("diff", "--name-status", "--no-renames", CODE_P3, CODE, "--", *CHEMINS_IDENTITE)
    sortie_v2 = git("diff", "--name-status", "--no-renames", CODE_P3, CODE_V2, "--", *CHEMINS_IDENTITE)
    sans_renommage = git("diff", "--name-status", CODE_P3, CODE, "--", *CHEMINS_IDENTITE)
    lignes = sortie.decode().splitlines()
    identite = lignes
    r.append((sha(sortie) == IDENTITE_SHA and len(lignes) == 14 and all(x.startswith("A\t") for x in lignes)
              and sha(sortie_v2) == IDENTITE_SHA and sha(sans_renommage) == IDENTITE_SHA and IDENTITE_SHA in t11,
              f"identité avec P3 au commit du code : {len(lignes)} lignes, toutes « A », empreinte {sha(sortie)} "
              f"(égale à {CODE_V2[:8]} et sans --no-renames), citée"))
    # empreintes
    fautes = []
    for f, e in EMPREINTES.items():
        b = git("show", f"{CODE}:{f}")
        if sha(b) != e:
            fautes.append(f"{f} : {sha(b)} ≠ {e}")
        if f != ".claude/hooks/garde_calcul.py" and git("show", f"{CODE}:{f}.sha256").decode().split()[0] != e:
            fautes.append(f"{f} : compagnon ≠ {e}")
        if f"`{f}` (`{e}`" not in p:
            fautes.append(f"{f} : non cité « `chemin` (`sha256` »")
    r.append((not fautes, f"empreintes du code au commit {CODE[:8]} : {len(EMPREINTES)} fichiers recalculés, compagnons égaux, "
              "cités" + (f" ; {fautes}" if fautes else "")))
    # pièces sur main
    fautes = []
    for f, e in PIECES.items():
        b = git("show", f"{MAIN}:{f}")
        if sha(b) != e or git("show", f"{MAIN}:{f}.sha256").decode().split()[0] != e:
            fautes.append(f)
        if f"`{e[:8]}…`" not in t11 and e not in t11:
            fautes.append(f"{f} : empreinte non citée")
    r.append((not fautes and MAIN in t11, f"pièces sur main au commit {MAIN[:8]} : {len(PIECES)} fichiers égaux aux valeurs "
              "citées et à leurs compagnons" + (f" ; {fautes}" if fautes else "")))
    # sortie v3 de l'essai de fermeture
    b = git("show", f"{ESSAI_COMMIT}:{ESSAI_CHEMIN}")
    lignes_e = [x for x in b.decode("utf-8").split("\n") if x.strip()]
    comp = git("show", f"{ESSAI_COMMIT}:{ESSAI_CHEMIN}.sha256").decode().split()
    ok = (sha(b) == ESSAI_EMPREINTE and comp[0] == ESSAI_EMPREINTE and lignes_e[-1] == LIGNE_ESSAI_CONFORME
          and not any(x.startswith("NON CONFORME") for x in lignes_e)
          and sum(x.startswith("CONFORME") for x in lignes_e) == 18
          and "2026-11-10T08:30:58Z" in lignes_e[0]
          and f"fichier essayé : {MODULE} {EMPREINTES[MODULE]}" in lignes_e
          and sha(git("show", f"{CHAINE}:{ESSAI_CHEMIN}")) == ESSAI_EMPREINTE)
    r.append((ok, f"sortie v3 de l'essai de fermeture ({ESSAI_COMMIT[:8]}) : empreinte, compagnon, dernière ligne "
              f"« {lignes_e[-1]} », {sum(x.startswith('CONFORME') for x in lignes_e)} lignes conformes, aucune non conforme, "
              f"module essayé {EMPREINTES[MODULE][:8]}, même fichier à {CHAINE[:8]}"))
    # D-1 à D-4 et constantes du module, à la lettre
    src = git("show", f"{CODE}:{MODULE}").decode("utf-8")
    fautes = [f"code : {c!r}" for c, _ in CODE_ET_TEXTE if c not in src]
    fautes += [f"texte : {x!r}" for _, x in CODE_ET_TEXTE if x not in p and x not in t11]
    motifs = re.search(r"MOTIFS_REFUS = \(([^)]*)\)", src, re.S)
    liste = re.findall(r'"([a-z-]+)"', motifs.group(1)) if motifs else []
    attendu = ", ".join(f"`{x}`" for x in liste)
    if len(liste) != 17 or attendu not in p:
        fautes.append(f"liste fermée des codes ({len(liste)}) absente du texte dans l'ordre du module")
    for x in ("`| clé | date | mode | appui | paquets | motif |`", "`|---|---|---|---|---|---|`"):
        if x not in t11:
            fautes.append(f"en-tête du journal {x} absent du texte")
    entete = re.search(r'ENTETE_JOURNAL = \("([^"]+)", "([^"]+)"\)', src)
    if not entete or entete.groups() != ("| clé | date | mode | appui | paquets | motif |", "|---|---|---|---|---|---|"):
        fautes.append("ENTETE_JOURNAL du module")
    r.append((not fautes, f"module {MODULE} au commit {CODE[:8]} : D-1 à D-4, clé de rendez-vous, date du rendez-vous, "
              f"en-tête et {len(liste)} codes de refus cités à la lettre" + (f" ; {fautes}" if fautes else "")))
    # chaîne
    verif = git("show", f"{CHAINE}:docs/procedures/P3-bis-temoin-positif-v1/verifications_p3bis_v1.py").decode("utf-8")
    lanceur = git("show", f"{CHAINE}:docs/procedures/P3-bis-temoin-positif-v1/lancer_p3bis_v1.sh").decode("utf-8")
    finale = git("show", f"{CHAINE}:docs/procedures/P3-bis-temoin-positif-v1/repetition_finale_p3bis_v1.sh").decode("utf-8")
    ctl = git("show", f"{CHAINE}:docs/procedures/P3-bis-temoin-positif-v1/controles_avant_depense_p3bis_v1.sh").decode("utf-8")
    recup = git("show", f"{CHAINE}:docs/procedures/P3-bis-temoin-positif-v1/recuperation_p3bis_v1.sh").decode("utf-8")
    fautes = [v for v in VALEURS_TEXTE[:-2] if f'"{v}"' not in verif]
    fautes += [] if 'f"`DEPOT_URL={DEPOT_URL}`", f"`GO_ID={GO_CALCUL}`")' in verif else ["DEPOT_URL ou GO_ID"]
    if 'BORNE_CREATION = "2026-11-18"' not in verif or not re.search(r"^BORNE_CREATION=2026-11-18\b", lanceur, re.M):
        fautes.append("BORNE_CREATION")
    if not re.search(r"^PLACE_MIN_KO=12692612\b", finale, re.M) or "12 692 612 ko" not in sg_(t11):
        fautes.append("PLACE_MIN_KO")
    n_ctl = len(re.findall(r'^[A-Z_]+="?A_EPINGLER', ctl, re.M))
    n_recup = len(re.findall(r'^[A-Z_]+="?A_EPINGLER', recup, re.M))
    if (n_ctl, n_recup) != (13, 1) or "les treize de `controles_avant_depense_p3bis_v1.sh`" not in p \
            or "celle de `recuperation_p3bis_v1.sh`" not in p:
        fautes.append(f"épingles {n_ctl} et {n_recup}")
    r.append((not fautes, f"chaîne au commit {CHAINE[:8]} : 19 valeurs du module commun égales à celles de ce script, "
              f"borne du 18 novembre, seuil de place 12 692 612 ko, épingles {n_ctl} + {n_recup}"
              + (f" ; {fautes}" if fautes else "")))
    # registre des GO (CD-03)
    def n_go(texte: str) -> int:
        return sum(1 for x in texte.splitlines() if x.startswith(f"| {GO_CALCUL} |"))
    go_main = Path("registres/go.md").read_text(encoding="utf-8")
    go_code = git("show", f"{CODE}:registres/go.md").decode("utf-8")
    go_chaine = git("show", f"{CHAINE}:registres/go.md").decode("utf-8")
    r.append(((n_go(go_main), n_go(go_code), n_go(go_chaine)) == (1, 0, 0),
              f"registre des GO : ligne {GO_CALCUL} sur main {n_go(go_main)}, au commit du code {n_go(go_code)}, à la tête de la "
              f"chaîne {n_go(go_chaine)} (CD-03 : à porter sur la branche de scellement, préalable P-3)"))
    return r, identite


def sg_(t: str) -> str:
    return " ".join(t.split())


def main(argv: list[str]) -> int:
    essai = len(argv) == 4 and argv[1] == "--essai"
    if not essai and len(argv) != 2:
        sys.exit(__doc__)
    heure = argv[-1]
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", heure):
        sys.exit("heure attendue AAAA-MM-JJTHH:MM:SSZ, relevée par date -u")
    b10 = ENTREE.read_bytes()
    if sha(b10) != EMPREINTE_ENTREE:
        sys.exit(f"empreinte de {ENTREE} inattendue")
    chemin_couples = Path(argv[2]) if essai else COUPLES
    bc = chemin_couples.read_bytes()
    if not essai and sha(bc) != EMPREINTE_COUPLES:
        sys.exit(f"empreinte de {COUPLES} inattendue")
    couples = json.loads(bc.decode("utf-8"))
    t10 = b10.decode("utf-8")
    t11, lignes = appliquer(t10, couples)
    r = controles_texte(t10, t11, couples)
    rg, identite = controles_git(t11)
    j = [f"Journal du brouillon 11 de P3-bis — {heure} (heure relevée par date -u, passée en argument)",
         f"entrée {ENTREE} {sha(b10)}",
         f"couples {chemin_couples} {sha(bc)} ({len(couples)} couples, dont "
         f"{sum(1 for c in couples if c['section_gelee'])} dans des sections gelées)",
         f"script {Path(__file__).as_posix()} {sha(Path(__file__).read_bytes())}",
         "", "couples appliqués, dans l'ordre :"] + lignes
    j += ["", f"sortie {SORTIE} {sha(t11.encode('utf-8'))}", "", "contrôles du texte :"]
    j += [("CONFORME — " if ok else "NON CONFORME — ") + texte for ok, texte in r]
    j += ["", "valeurs remplies et constantes citées, recalculées par git en lecture seule :"]
    j += [("CONFORME — " if ok else "NON CONFORME — ") + texte for ok, texte in rg]
    j += ["", f"sortie de git diff --name-status --no-renames {CODE_P3} {CODE} -- <chemins de l'en-tête> "
              f"({len(identite)} lignes, empreinte des octets exacts {IDENTITE_SHA}) :"]
    j += [f"  {x}" for x in identite]
    if not essai:
        if SORTIE.exists() or JOURNAL.exists():
            sys.exit(f"{SORTIE} ou {JOURNAL} existe déjà (R12)")
        SORTIE.write_text(t11, encoding="utf-8")
        p = problemes(SORTIE)
    else:
        tmp = Path(argv[2]).with_name("essai-brouillon11.md")
        tmp.write_text(t11, encoding="utf-8")
        p = problemes(tmp)
        tmp.unlink()
    j += ["", "controle_ia.prereg.problemes (attendu : la contre-lecture 4 sans ses empreintes et les six marqueurs gardés) :"]
    j += [f"  {x}" for x in p]
    attendus = sorted(MARQUEURS_ATTENDUS)
    ok_p = len(p) == 2 and p[0] == "contre-lecture 4 sans ses deux empreintes (brouillon relu et rapport)" \
        and p[1] == "marqueurs de gabarit restants : " + ", ".join(f"<<{m}>>" for m in attendus)
    j += [("CONFORME — " if ok_p else "NON CONFORME — ") + "problemes() égal à l'attendu"]
    tous = all(ok for ok, _ in r + rg) and ok_p
    j += ["", "BROUILLON 11 : " + ("CONTRÔLES CONFORMES" if tous else "CONTRÔLES NON CONFORMES")]
    texte = "\n".join(j) + "\n"
    if essai:
        print(texte)
    else:
        JOURNAL.write_text(texte, encoding="utf-8")
        print(sha(SORTIE.read_bytes()), SORTIE)
        print(sha(JOURNAL.read_bytes()), JOURNAL)
        print(j[-1])
    return 0 if tous else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
