"""Candidat 2 du préenregistrement de P3-bis : construction des couples C2 et des épingles proposées (v1).

Écrit le 2026-11-11 par un rédacteur neuf (Claude Opus 5.5, `claude-opus-5-5`), sous-agent de la session mère
`session_01VJdZpSMxSdk2SJ1ScmdfNv`, sur la consigne
`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-redaction-p3bis-candidat2-v1.md`
(`85a3d612…`), qui ne lit pas T0.7. Aucun appel externe ; aucune écriture git (`git show`, `git diff`, `git log`,
`git cat-file`, `git merge-base` en lecture seule) ; aucun fichier de T0.7 ni des interdits communs v2 ouvert.

Ce que fait le script, dans l'ordre, sans rien écrire tant qu'un contrôle échoue (R5) :
  1. vérifie ses entrées par leur empreinte et leur compagnon (consigne, candidat 1, relecture courte, brouillon 11) ;
  2. recalcule par `git show` au commit du code les empreintes des quinze fichiers de la chaîne v2, chacune égale à son
     compagnon au même commit et à la valeur relevée par le rédacteur ; vérifie la branche de scellement `d0d9fcb8` ;
  3. vérifie chaque pièce des épingles proposées sur `main` (fichier et compagnon égaux ; les longueurs attendues au
     commit `dfb1ed7b`, seul endroit où elles sont) et relève si `d0d9fcb8` la porte à l'empreinte voulue ;
  4. construit les couples C2 (chaque « ancien » trouvé exactement une fois dans le texte courant, appliqués dans
     l'ordre) ; le couple de la date tenue porte le jeton `R-NNNN`, une seule fois dans tout le fichier des couples,
     que `…-faire-v1.py` remplace par le numéro passé en argument ;
  5. écrit (R12 : aucune sortie ne doit exister) les couples, les épingles proposées (avec la liste des pièces à verser)
     et un journal de construction, dans le dossier donné.

Usage, depuis la racine du dépôt :
  PYTHONPATH=src python <ce script> DOSSIER_DE_SORTIE "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
"""
import hashlib
import json
import re
import subprocess
import sys
import textwrap
from pathlib import Path

# ------------------------------------------------------------------------------------------------ chemins et empreintes
DOSSIER = "brouillons/P3-bis-temoin-positif-v1"
C1 = f"{DOSSIER}/P3-bis-preenregistrement-v1-candidat1.md"
C2 = f"{DOSSIER}/P3-bis-preenregistrement-v1-candidat2.md"
PIECES2 = f"{DOSSIER}/P3-bis-preenregistrement-v1-candidat2-pieces"
B11 = f"{DOSSIER}/P3-bis-preenregistrement-v1-brouillon11.md"
RELECTURE = f"{DOSSIER}/P3-bis-candidat1-relecture-courte-v1.md"
CONSIGNE = "docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-redaction-p3bis-candidat2-v1.md"
NOM_COUPLES = "P3-bis-preenregistrement-v1-candidat2-couples-v1.json"
NOM_EPINGLES = "P3-bis-epingles-proposees-v1.json"
NOM_JOURNAL = "P3-bis-preenregistrement-v1-candidat2-construire-journal-v1.txt"

EMP = {
    CONSIGNE: "85a3d612f441083943d93e5c274e88d3aad58cd84311adc1ef71184bf1a58e58",
    C1: "9a56a657b1fad1e23b0cc11e41831f066eed48674159dbc55c2a869aa56c4271",
    RELECTURE: "85ee0b47078d18311bb70872877c0b73c54fc480219e87678e4cc6ae63551eec",
    B11: "409c37ed4aa4f149565d8b0a45ae94c16b572f35967f080a0df629985549b290",
}
CODE = "5e4575259478af3611e2c7fb1313342912caf484"           # commit du code cité (en-tête du candidat 1)
SCEL = "d0d9fcb8ddf82da3919736e9b97eb8aff4c71b45"           # branche scellement/p3bis-v1 (P-3, P-10 ; R-2345)
PHASE1 = "dfb1ed7b7040fa22fca95d931d0e0a8b4ea43527"         # phase 1 des préalables (R-2295)
CHAINE = "docs/procedures/P3-bis-temoin-positif-v1"
# ordre de `CHAINE` dans sceller_p3bis_v2.sh (l. 42) ; empreintes relevées par le rédacteur (git show, 13:27 UTC)
CHAINE_V2 = {
    "lancer_p3bis_v2.sh": "029bdb5c114a6166a21fa93724d71a2bf6158dc9686993424f6fbe8462352b08",
    "verifications_p3bis_v2.py": "1524df5f6432197fde4793a4fde56d4496407a107c88f5e294a6bc9716923054",
    "controles_avant_depense_p3bis_v2.sh": "67c3c28809f74808ec7fdfeeff4649f49dc9e4077e58253735b400531f3ef711",
    "surveiller_p3bis_v2.sh": "d65421073068466a3aa6cc90ef00e6c76b15ea7b3e61e254c1dbafad020afe9b",
    "controle_cinq_minutes_p3bis_v2.sh": "6f9213499687d655e290ab96c1ab8a1cdb9ecd373b1d6beecb7efda962f40864",
    "recuperation_p3bis_v2.sh": "f95c60b95e4e11563f29476560b0190228729f60c65162120c48a6bc6bdc467d",
    "detruire_p3bis_v2.sh": "cae56ec9cbd00485a9506a1af1bb9dfd8e4b493e966003cb0ed365fe6973ae46",
    "sceller_p3bis_v2.sh": "f0c002cc186beef4684c3eee4d9750c8a70760bb978ac09f14b4ce66987ff319",
    "repetition_jouet_p3bis_v2.sh": "2e4d16280399f9273c35c93190566152b66ade0f22755c64219e11ae05f5370f",
    "repetition_finale_p3bis_v2.sh": "b60157f83df7659b5dc747d571df60ee71bdf0569bb3d3cf1c437bf8a805c499",
    "essais_verifications_p3bis_v2.py": "03e4c2ab7ebfb3e872148518a67b7df6d9827ec7f6e960eac4a8fc89fef7ff33",
    "essais_lanceur_p3bis_v2.sh": "a89745be6e9aaea55bf71252fd504eae06617453b2e5985a720c071876813ef6",
    "essais_surveillance_p3bis_v2.sh": "08d1677571cc5c33f387b823c572a8389032053725c3898a2a812728fa629207",
    "essais_controles_p3bis_v2.sh": "98d03a603266ca851225f9f5c15c8aa62df832d3237756997b6f1c629370f2d2",
    "essais_recuperation_p3bis_v2.sh": "9e39f5ca204806b4b93c67917053fe03683ac393f39bc5c88281fc34d9975507",
}
JOURNAUX = ("banc-verifications-p3bis-v2.log", "banc-lanceur-p3bis-v2.log", "banc-surveillance-p3bis-v2.log",
            "banc-controles-p3bis-v2.log", "banc-recuperation-p3bis-v2.log", "repetition-jouet-p3bis-v2.log",
            "repetition-finale-p3bis-v2.log")
# épingles (valeurs citées par le texte) ; chaque pièce : (chemin, empreinte, commit où la vérifier)
CFG_RELUE = (f"{DOSSIER}/P3-bis-preenregistrement-v1-candidat1-pieces/P3-bis-temoin-positif-config-v1-candidat1.json",
             "612b0c6ce5c4263eb3016b72ad85155dd2307f9dd887379d2a1133ed644a9d05")
CONS_RELUES = (f"{DOSSIER}/P3-bis-consignes-v1-brouillon2.md",
               "7d35576d65c030edcc6441e142ea95732679b674edcb1fd1af86ab8f69c04367")
ESSAI = ("docs/notes/g0-deux-semaines-v1/p3bis-regle-plancher-v1/essai-fermeture-p3bis-v3-sortie-v1.txt",
         "9375628699e95fc6563d2da4ce0172371cfeb2e3fcb56b0fbe8e2aa6774b1464")
LONGUEURS = ("docs/notes/g0-deux-semaines-v1/p3bis-prealables-v1/longueurs-attendues-p3bis-v1.json",
             "7c94d43cc7bea9a5af3c5c5ec34f552256bbcf258a0436d1a2295c91d45cfb21")
# rapports de contre-lecture et de relecture de P3-bis (texte, code, chaîne) que le texte cite par chemin et empreinte
# entière (bloc 14) ; dans l'ordre de leur date
RAPPORTS = (
    (f"{DOSSIER}/contre-lecture-brouillon2-v1/contre-lecture-p3-bis-brouillon2-v1.md",
     "8399dc55ae358712ca97b4cffa5f79d98e45207ad25494b8abc01c98b7921ae0", "contre-lecture 1 (brouillon 2)"),
    (f"{DOSSIER}/contre-lecture-2-brouillon5-v1.md",
     "f12d7f211f0b1b92eb1a59ec543442d2d79aaa9e476507ec8a8b9ec408d4ef0e", "contre-lecture 2 (brouillon 5)"),
    (f"{DOSSIER}/contre-lecture-3-brouillon6-v1.md",
     "4c3cb62831a42f8e02e632ea1c7d111f94bb24b9ad066ace9e1ccfe148fde622", "contre-lecture 3 (brouillon 6)"),
    (f"{DOSSIER}/contre-lecture-code-p3bis-v1.md",
     "7a074ad1c0033b53560b0c50120036d9d9e914f72957bfe1cc078598c39f7242", "contre-lecture du code v1"),
    (f"{DOSSIER}/contre-lecture-differentielle-code-v2-chaine-v1.md",
     "011942534477d65627b961f09e814c2fe0693d44b7d525633466fd4a918c00d9",
     "contre-lecture différentielle du code v2 et de la chaîne"),
    (f"{DOSSIER}/contre-lecture-4-brouillon11-v1.md",
     "90847ae2d017c6e100a15cf80ecee17645a4c71ecd33197187767cc2ff9d2c13", "contre-lecture 4 (brouillon 11)"),
    (f"{DOSSIER}/contre-lecture-differentielle-code-a1de3915-v1.md",
     "845c4de54e72207a320edf089c606bacf0cd87837d473ab654de48c3ddc839c9",
     "contre-lecture différentielle courte du code a1de3915"),
    ("docs/notes/g0-deux-semaines-v1/p3bis-regle-plancher-v1/contre-lecture-courte-code-p3bis-regle-a-v1.md",
     "03f1bb59d7fc2afed8bf8939f2457c177a36d477deae5bdb6e1c1dc2f3235141",
     "contre-lecture différentielle courte du code 5e457525 et de la chaîne v2"),
    (RELECTURE, "85ee0b47078d18311bb70872877c0b73c54fc480219e87678e4cc6ae63551eec",
     "relecture courte de l'écart du brouillon 11 au candidat 1 (CANDIDAT_RELU)"),
)
# rapports de contre-lecture cités par chemin et empreinte entière, mais d'un autre objet que P3-bis : écartés de la
# proposition (question à la mère) ; ceux de T0.7 ne sont ni ouverts ni hachés (consigne : aucune lecture de T0.7)
ECARTES = (
    ("brouillons/entretien-taif-v3/socle-preuves-entretien-v1-contre-lecture-v1.md",
     "48c7fcc2ab823856a0de1c4fd18d48df8e42733e2b25dc800207f9beafd33ff1",
     "contre-lecture du socle de preuves de l'entretien (autre objet)", True),
    ("prereg/contre-lectures/T0.7-sondes-v0-v1-brouillon15-cl1.md",
     "29203bbcc20e6e52f1f1a2f4b95b802d644663981747daddeb90a16377343004",
     "contre-lecture du brouillon 15 de T0.7 (autre objet ; non ouverte ni hachée)", False),
    ("prereg/contre-lectures/T0.7-sondes-v0-v1-brouillon16-cl2.md",
     "fc728c18573061c0d4bcc7c1bbbd651944667b76420a6a215a7931f87f16ee38",
     "contre-lecture 2 du brouillon 16 de T0.7 (autre objet ; non ouverte ni hachée)", False),
)
JETON = "R-NNNN"


def h(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def git(*args: str) -> bytes:
    r = subprocess.run(["git", *args], capture_output=True)
    if r.returncode != 0:
        raise SystemExit(f"git {' '.join(args)} : code {r.returncode} : {r.stderr.decode()[:200]}")
    return r.stdout


def existe(ref: str, chemin: str) -> bool:
    return subprocess.run(["git", "cat-file", "-e", f"{ref}:{chemin}"], capture_output=True).returncode == 0


def piece(ref: str, chemin: str, e: str) -> str:
    """« OK » si le fichier et son compagnon sont à l'empreinte e à ref ; sinon l'écart."""
    if not existe(ref, chemin):
        return "absent"
    hf = h(git("show", f"{ref}:{chemin}"))
    comp = git("show", f"{ref}:{chemin}.sha256").decode().strip() if existe(ref, chemin + ".sha256") else None
    if hf != e:
        return f"empreinte {hf}"
    if comp != f"{e}  {Path(chemin).name}":
        return f"compagnon {comp!r}"
    return "OK"


def para(texte: str, i0: str, i1: str, largeur: int = 120) -> str:
    """Un paragraphe enveloppé (espaces réduites), sans couper un mot ni un trait d'union."""
    t = " ".join(texte.split())
    # espaces tenues le temps de l'enveloppe : dans les accents graves, après « et avant », ; et :
    t = re.sub(r"`[^`]*`", lambda m: m.group(0).replace(" ", "\x00"), t)
    t = t.replace("« ", "«\x00").replace(" »", "\x00»").replace(" ;", "\x00;").replace(" :", "\x00:")
    return textwrap.fill(t, width=largeur, initial_indent=i0, subsequent_indent=i1, break_long_words=False,
                         break_on_hyphens=False).replace("\x00", " ")


def bt(x: str) -> str:
    return f"`{x}`"


# ------------------------------------------------------------------------------------------------ 1-3. contrôles
def controles(journal: list[str]) -> dict:
    for f, e in EMP.items():
        b = Path(f).read_bytes()
        comp = Path(f + ".sha256").read_text(encoding="utf-8").strip()
        if h(b) != e or comp != f"{e}  {Path(f).name}":
            raise SystemExit(f"entrée {f} : empreinte ou compagnon inattendus")
        journal.append(f"entrée {f} : {e} (= compagnon)")
    if git("cat-file", "-t", CODE).strip() != b"commit" or git("cat-file", "-t", SCEL).strip() != b"commit":
        raise SystemExit("commit du code ou de la branche de scellement absent du clone")
    if not subprocess.run(["git", "merge-base", "--is-ancestor", CODE, SCEL]).returncode == 0:
        raise SystemExit("le commit du code n'est pas ancêtre de la branche de scellement")
    noms = sorted(Path(x).name for x in git("ls-tree", "--name-only", CODE, CHAINE + "/").decode().split()
                  if re.search(r"_p3bis_v2\.(sh|py)$", x))
    if noms != sorted(CHAINE_V2):
        raise SystemExit(f"chaîne v2 au commit du code : {noms}")
    for s, e in CHAINE_V2.items():
        r = piece(CODE, f"{CHAINE}/{s}", e)
        if r != "OK":
            raise SystemExit(f"chaîne v2, {s} au commit du code : {r}")
        journal.append(f"chaîne v2 au commit du code : {s} {e} (= compagnon)")
    d = subprocess.run(["git", "diff", "--quiet", CODE, SCEL, "--", CHAINE + "/"]).returncode
    journal.append(f"git diff --quiet {CODE[:8]} {SCEL[:8]} -- {CHAINE}/ : code {d} (0 : chaîne non épinglée, égale)")
    if d != 0:
        raise SystemExit("la branche de scellement change déjà la chaîne")
    # épingles A_EPINGLER au commit du code : treize et une, aux noms attendus
    ctl = git("show", f"{CODE}:{CHAINE}/controles_avant_depense_p3bis_v2.sh").decode()
    rec = git("show", f"{CODE}:{CHAINE}/recuperation_p3bis_v2.sh").decode()
    l_ctl = re.findall(r"^([A-Z_]+)=A_EPINGLER.*$", ctl, re.M)
    l_rec = re.findall(r"^([A-Z_]+)=A_EPINGLER.*$", rec, re.M)
    attendu = ["CANDIDAT_RELU", "CANDIDAT_RELU_CHEMIN", "CONFIG_RELUE", "CONFIG_RELUE_CHEMIN", "CONSIGNES_RELUES",
               "CONSIGNES_RELUES_CHEMIN", "CODE_RELU", "ESSAI_FERMETURE", "ESSAI_FERMETURE_CHEMIN",
               "LONGUEURS_ATTENDUES", "LONGUEURS_ATTENDUES_CHEMIN", "RAPPORTS_ATTENDUS", "PY"]
    if l_ctl != attendu or l_rec != ["PY"]:
        raise SystemExit(f"épingles : contrôles {l_ctl}, récupération {l_rec}")
    journal.append("épingles A_EPINGLER au commit du code : treize dans les contrôles, une (PY) dans la récupération")
    sc = git("show", f"{CODE}:{CHAINE}/sceller_p3bis_v2.sh").decode()
    m = re.search(r'^PREUVES_EXIGEES="([^"]*)"', sc, re.M)
    if not m or tuple(m.group(1).split()) != JOURNAUX:
        raise SystemExit("PREUVES_EXIGEES de sceller_p3bis_v2.sh ≠ sept journaux attendus")
    journal.append("PREUVES_EXIGEES de sceller_p3bis_v2.sh (étape 5) = les sept journaux canoniques, dans cet ordre")
    # pièces des épingles : sur main (longueurs : dfb1ed7b) ; présence à d0d9fcb8
    pieces = []
    main = git("rev-parse", "main").decode().strip()
    for role, (f, e), ref in (("CONFIG_RELUE", CFG_RELUE, main), ("CONSIGNES_RELUES", CONS_RELUES, main),
                              ("ESSAI_FERMETURE", ESSAI, main), ("LONGUEURS_ATTENDUES", LONGUEURS, PHASE1)):
        pieces.append((role, f, e, ref))
    for f, e, objet in RAPPORTS:
        pieces.append((f"RAPPORTS_ATTENDUS ({objet})", f, e, main))
    lignes = []
    for role, f, e, ref in pieces:
        r = piece(ref, f, e)
        if r != "OK":
            raise SystemExit(f"pièce {f} à {ref[:8]} : {r}")
        a = piece(SCEL, f, e)
        dernier = git("log", "-1", "--format=%H", ref, "--", f).decode().strip()
        lignes.append({"epingle": role, "chemin": f, "empreinte": e, "verifiee_a": ref,
                       "dernier_commit_qui_la_change": dernier, "a_d0d9fcb8": a})
        journal.append(f"pièce {f} : {e} = compagnon à {ref[:8]} ; à {SCEL[:8]} : {a}")
    if any(re.search(r"\s", x["chemin"]) for x in lignes):
        raise SystemExit("chemin avec espace")
    socle = ECARTES[0]
    r = piece(main, socle[0], socle[1])
    journal.append(f"écarté (question), {socle[0]} : {r} sur main ; à {SCEL[:8]} : {piece(SCEL, socle[0], socle[1])}")
    return {"main": main, "pieces": lignes}


# ------------------------------------------------------------------------------------------------ 4. couples
def couples_c2() -> list[dict]:
    I2, I3 = "  ", "   "
    l_chaine = " ; ".join(f"{bt(CHAINE + '/' + s)} ({bt(e)})" for s, e in CHAINE_V2.items())
    l_journaux = ", ".join(bt(j) for j in JOURNAUX)
    l_rapports = " ; ".join(f"{bt(f)} ({bt(e)})" for f, e, _ in RAPPORTS)
    c = []

    def couple(i, section, gelee, decision, motif, ancien, nouveau):
        c.append({"id": f"C2-{i:02d}", "fichier": C1, "section": section, "section_gelee": gelee,
                  "decision": decision, "motif": motif, "ancien": ancien, "nouveau": nouveau})

    couple(1, "titre (non gelée)", None, "consigne de la mère", "nom du texte : candidat 2",
           "que P3) — v1 — candidat 1\n", "que P3) — v1 — candidat 2\n")

    statut = "\n".join([
        para("- Statut : **candidat 2**, écrit le 2026-11-11 à partir de 13:26 UTC (heure relevée par `date -u`) par un "
             "**rédacteur neuf** (Claude Opus 5.5, `claude-opus-5-5`, sous-agent de la session mère "
             "`session_01VJdZpSMxSdk2SJ1ScmdfNv`), sur la consigne "
             f"{bt(CONSIGNE)} ({bt(EMP[CONSIGNE])}, recalculée avant lecture, égale à son compagnon ; interdits communs "
             "v2 recopiés dedans). Ce rédacteur n'a écrit ni les brouillons 1 à 12, ni le candidat 1, ni le code de "
             "P3-bis, ni sa chaîne, ni aucune de leurs contre-lectures ou relectures, ni P3, ni T0.6, ni T0.7 ; **il n'a "
             "ouvert aucun fichier de T0.7** (consigne). Révision par **couples appliqués par script** (couples C2, "
             "chacun trouvé une fois ; pièces sous "
             f"{bt(PIECES2 + '/')} : couples {bt(NOM_COUPLES)}, scripts "
             "`P3-bis-preenregistrement-v1-candidat2-construire-couples-v1.py` et "
             "`P3-bis-preenregistrement-v1-candidat2-faire-v1.py`, journaux de la construction et du candidat 2, "
             f"épingles proposées {bt(NOM_EPINGLES)}, scellés avec ce texte, R6) ; ce texte est écrit par le script "
             "quand la session mère le lance avec le numéro de la ligne du registre qui constate la date tenue "
             "(P-11). Non scellé ; rien n'est lancé, rien n'est dépensé ; aucune écriture git. **Marqueurs restants au "
             "candidat 2 : aucun.**", "", I2),
        para("- **Candidat 2 = candidat 1 + N-1 + `CHAINE_P3BIS` et `CANDIDAT_RELU` remplis + date tenue + état** "
             "(consigne ci-dessus ; R-2344, R-2345) : (1) **N-1** de la relecture courte (R-2344), seul changement "
             "d'une section gelée (« Plan d'analyse », point 10) : « niveau tenu » devient « aucun dépassement établi "
             "du niveau » ; (2) **`CHAINE_P3BIS` rempli sans circularité** (R-2345 ; « Ce que le code et la chaîne "
             "doivent changer », point 6) : chaîne v2 au commit du code (quinze fichiers, chemins et empreintes), "
             "règle d'épinglage des deux fichiers épinglés, noms des sept journaux canoniques, cités par leur empreinte "
             "au registre des décisions (constat de P-6) et jamais ici ; la définition du marqueur, la ligne P-5, "
             "l'en-tête et les autres phrases qui disaient que ce texte citerait la chaîne épinglée ou les journaux "
             "par leur empreinte sont corrigés (table « du candidat 1 au candidat 2 ») ; (3) **`CANDIDAT_RELU` "
             "rempli** (section « Contre-lecture ») : brouillon 11 (`409c37ed…`), rapport de la relecture courte "
             "(`85ee0b47…`), « relu, conforme » sur le candidat 1 ; l'écart du candidat 1 au candidat 2 est contrôlé "
             "par programme et relu par un relecteur neuf, consigné au registre des décisions (il ne peut être cité "
             "ici) ; (4) **date tenue** (P-11), à « Décisions pour Lazar » ; (5) **état des préalables** au "
             "2026-11-11 vers 13:26 UTC (R-2345) : P-1 et P-2 faits, P-4 relevé avec sa réserve de place avant P-6 "
             "(phase 1, R-2295) ; P-7 (R-2340), la relecture courte (R-2344), P-8 (aucun marqueur, par ce texte), P-3 et "
             "P-10 (branche de scellement `scellement/p3bis-v1`, commit "
             f"{bt(SCEL)}, tiré du commit du code, R-2345 ; à revérifier le jour de S sur le registre de `main` du "
             "jour) faits ; P-11 à « Décisions pour Lazar » ; restent P-5, P-6, P-9, la relecture de l'écart du "
             "candidat 1 au candidat 2, puis S. **Aucune hypothèse, prédiction, aucun signe, aucune métrique, aucun "
             "seuil, critère de lecture ni aucune liste d'arrêt ne change** ; le « Plan d'analyse » ne change que par "
             "N-1 (contrôlé par programme : empreintes des sept sections gelées, journal du candidat 2) ; aucun code ni "
             "aucune configuration ne change. Le reste du candidat 1 est gardé mot pour mot. Candidat 1 : "
             f"{bt(C1)} ({bt(EMP[C1])}, recalculée, égale à son compagnon), gardé tel quel (R12). Ce que faisait le "
             "candidat 1, gardé pour mémoire :", "", I2),
        "- Statut du **candidat 1** : écrit le 2026-11-11 à partir de 12:44 UTC"])
    couple(2, "en-tête, statut (non gelée)", None, "consigne de la mère ; R-2344, R-2345",
           "statut du candidat 2, ce qu'il change, état des préalables ; le statut du candidat 1 gardé pour mémoire",
           "- Statut : **candidat 1**, écrit le 2026-11-11 à partir de 12:44 UTC", statut)

    couple(3, "en-tête, statut du candidat 1 (non gelée)", None, "R-2345 (définition de CHAINE_P3BIS circulaire)",
           "phrase qui définissait CHAINE_P3BIS par la chaîne épinglée : corrigée",
           "(chaîne v2 épinglée, journaux canoniques des bancs et des répétitions : phase 2 des\n  préalables, P-5 et P-6)",
           "(chaîne v2 et journaux canoniques des bancs et des répétitions : phase 2 des\n" + para(
               "préalables, P-5 et P-6 ; **définition corrigée au candidat 2**, R-2345 : la chaîne est citée au commit "
               "du code, les deux fichiers épinglés par une règle, les journaux par leurs noms, leurs empreintes au "
               "registre des décisions ; ni la chaîne épinglée ni les journaux ne sont cités ici par leur empreinte, ce "
               "qui serait circulaire)", I2, I2))

    couple(4, "en-tête, auteur (non gelée)", None, "consigne de la mère", "auteur du candidat 2",
           "par script (candidat 1). Aucun n'a écrit P3",
           "par script (candidat 1) ; rédacteur neuf, couples appliqués par script (candidat 2). Aucun n'a écrit P3")

    couple(5, "en-tête, « Lu » (non gelée)", None, "consigne de la mère", "lectures du candidat 2",
           "- **Lu** (brouillons 4 à 12 et candidat 1 ;", "- **Lu** (brouillons 4 à 12, candidats 1 et 2 ;")

    lu = para(
        "- **pour le candidat 2** (rédacteur neuf) : consigne de la rédaction du candidat 2 (empreinte ci-dessus, "
        "entière) ; `registres/decisions.md` sur `main`, lignes R-2342 à R-2345, puis R-2346 et le début de R-2347 "
        "(affichées par des recherches sur ce seul fichier) ; candidat 1 (`9a56a657…`) : en-tête et table « du 12 au candidat 1 » (l. 1-675), « Ce que le "
        "code et la chaîne doivent changer », « Préalables », « Décisions pour Lazar », « Contre-lecture », "
        "« Marqueurs restants », le contexte de « niveau tenu » (plan, point 10), les points 2 et 6 du plan (citations "
        "des longueurs et de l'essai de fermeture), et les lignes trouvées par des recherches de mots dans ce seul "
        "fichier (`CHAINE_P3BIS`, `CANDIDAT_RELU`, « épingl », « journaux canoniques », « à verser », intitulés lus "
        "par la chaîne, rapports de contre-lecture cités) ; ses couples C1 (forme) et son script (en-tête, l. 1-80) ; "
        "relecture courte `85ee0b47…` (entière) ; `prereg/P3-premier-test-i-a-v1.md` l. 468-487 (`d975e981…`, égale à "
        "son compagnon) ; `src/controle_ia/prereg.py` (entier) et `scellement.py` (extraits des l. 1-80) ; au commit du code "
        "`5e457525`, par `git show` : `controles_avant_depense_p3bis_v2.sh` et `sceller_p3bis_v2.sh` (entiers), "
        "`recuperation_p3bis_v2.sh` (l. 1-42) et `repetition_finale_p3bis_v2.sh` (l. 1-47), `verifications_p3bis_v2.py` "
        "(`valeurs`, `constantes`, `preuves`, `main`), constantes de `lancer_p3bis_v2.sh`, recherche de `A_EPINGLER` "
        "dans les quinze fichiers, `harnais/validation_reelle.py` (`CHEMINS_GELES`, par recherche) ; empreintes des "
        "quinze fichiers de la chaîne, de l'amorce, du script de l'instance et du fichier des tâches de P3, par `git "
        "show` ; branche de scellement `d0d9fcb8` (`git log`, `git diff --name-status` depuis `5e457525`, chemins "
        "interdits exclus) ; pièces des épingles hachées par `git show` sur `main` et à `d0d9fcb8`, les longueurs "
        "attendues au commit `dfb1ed7b` ;", "  ", "    ")
    couple(6, "en-tête, « Lu » (non gelée)", None, "consigne de la mère", "lectures du candidat 2",
           "  - **pour le candidat 1** (rédacteur neuf)", lu + "\n  - **pour le candidat 1** (rédacteur neuf)")

    nonlu = para(
        "Candidat 2 : aucun fichier de T0.7 ouvert ni haché (ni `brouillons/T0.7-*`, ni `prereg/T0.7*`, ni "
        "`prereg/contre-lectures/T0.7-*`, ni `src/controle_ia/t07/`, `plancher_v2.py` compris, ni "
        "`docs/notes/g0-deux-semaines-v1/t07-*`) ; aucun fichier ni branche des interdits communs v2 ; aucun `diag/` ni "
        "`runs/` ouvert ; de `donnees/`, la seule empreinte du fichier des tâches de P3, recalculée par `git show` au "
        "commit du code ; recherches par `grep` dans des fichiers nommés ou par `git` sur des chemins nommés (règle "
        "9). Gestes déclarés : `git branch -a` filtré par `grep` (noms de branches seuls, aucun interdit affiché) ; "
        "`git diff --name-status 5e457525 d0d9fcb8` sur l'arbre entier, `docs/notes/bras-attaque`, `diag`, `runs` et "
        "`donnees` exclus (trois chemins affichés) ; `git status --short` (noms de fichiers non suivis affichés, dont deux "
        "chemins sous `brouillons/T0.7-audit-fuites-v1/`, non ouverts) ; une recherche de R-2346 et R-2347 dans "
        "`registres/decisions.md` a affiché R-2346, ligne qui parle de l'audit des fuites de T0.7 (ligne de registre, "
        "aucun fichier de T0.7).", "  ", "  ")
    couple(7, "en-tête, « Non lu » (non gelée)", None, "consigne de la mère", "ce que le candidat 2 n'a pas ouvert",
           "- Auteur : sous-agent de rédaction (brouillon 1)", nonlu + "\n- Auteur : sous-agent de rédaction (brouillon 1)")

    couple(8, "en-tête, GO et borne de création (non gelée)", None, "R-2345",
           "« à épingler au candidat, marqueur CHAINE_P3BIS » : la borne est tenue par la chaîne au commit du code, "
           "que le marqueur cite",
           "à épingler au candidat, marqueur `CHAINE_P3BIS`",
           "à épingler au candidat, marqueur `CHAINE_P3BIS` ; candidat 2 : tenue par la chaîne v2 au commit du code, "
           "que ce marqueur cite par ses chemins et empreintes, R-2345")

    ancien9 = "et candidat 1 (`612b0c6ce5c4263eb3016b72ad85155dd2307f9dd887379d2a1133ed644a9d05`), chacune scellée.\n"
    pieces = para(
        "- **Pièces citées par le candidat 2** (chacune égale à son compagnon) : relecture courte du candidat 1 "
        f"{bt(RELECTURE)} ({bt(EMP[RELECTURE])}, sur `main`, R-2344) ; chaîne v2 au commit du code `5e457525` (quinze "
        "fichiers : « Ce que le code et la chaîne doivent changer », point 6) ; branche de scellement "
        f"`scellement/p3bis-v1` au commit {bt(SCEL)} (P-3 et P-10, R-2345). **Pièces neuves du candidat 2**, sous "
        f"{bt(PIECES2 + '/')}, chacune scellée, citées par leur nom seul (leurs empreintes, qui dépendent de ce texte "
        "ou le contiennent, sont au journal du candidat 2 et au registre) : couples, scripts de construction et "
        "d'application, journaux de la construction et du candidat 2, épingles proposées "
        f"{bt(NOM_EPINGLES)} (valeurs des épingles des contrôles, sauf `CANDIDAT_RELU` et `PY`, et liste des pièces à "
        "verser sur la branche de scellement), sortie à blanc `P3-bis-preenregistrement-v1-candidat2-a-blanc.md` "
        "(produite avec un numéro fictif, pour un essai à blanc de la chaîne seulement ; jamais scellée comme texte).",
        "", "  ")
    couple(9, "en-tête, pièces (non gelée)", None, "consigne de la mère", "pièces citées et pièces neuves du candidat 2",
           ancien9, ancien9 + pieces + "\n")

    table = "\n".join([
        "## Table « ce qui change du candidat 1 au candidat 2 »",
        "",
        "| # | sujet | candidat 1 | candidat 2 | raison | couples |",
        "|---|---|---|---|---|---|",
        "| 1 | titre, statut, auteur, lectures, pièces | candidat 1 | candidat 2, rédacteur neuf, couples appliqués par "
        "script ; état des préalables (R-2345) ; « Lu », « Non lu », auteur ; pièces citées et neuves ; cette table | "
        "consigne de la mère | C2-01, C2-02, C2-04 à C2-07, C2-09, C2-10 |",
        "| 2 | plan, point 10 (**section gelée « Plan d'analyse »**, seul changement d'une section gelée) | « niveau "
        "tenu » | « aucun dépassement établi du niveau » (relecture courte, N-1 : la note `1613d5bd…` et R-2320 disent « ne "
        "dépasse le nominal de façon établie à aucun k » ; au plafond, l'intervalle [0,0115 ; 0,0323] contient le nominal "
        "0,025) ; chiffres inchangés | relecture courte, N-1 (`85ee0b47…`) ; R-2344 | C2-11 |",
        "| 3 | `CHAINE_P3BIS` | marqueur, défini comme les chemins et empreintes de la chaîne **épinglée** et des sept "
        "journaux canoniques, que ce texte devait citer : circulaire (l'épingle `CANDIDAT_RELU` est l'empreinte de ce "
        "texte ; les journaux sont joués après lui) | rempli : (a) chaîne v2 au commit du code, quinze fichiers, "
        "chemins et empreintes ; (b) règle d'épinglage (deux fichiers, quatorze lignes `A_EPINGLER`, valeurs citées "
        "ici sauf `CANDIDAT_RELU` et `PY`), vérifiée par programme avant S ; (c) noms des sept journaux, versés et "
        "scellés avant S, cités par leur empreinte au registre des décisions | R-2345 ; texte scellé de P3, l. 470-485 "
        "| C2-12 |",
        "| 4 | phrases qui disaient que ce texte citerait les versions épinglées ou les journaux par leur empreinte | "
        "en-tête (statut du candidat 1 ; borne de création) ; « Ce que le code et la chaîne doivent changer », point 6 "
        "(« Ce qui dépend du rapport complémentaire du lanceur » ; « Restent pour `CHAINE_P3BIS` ») ; préalable P-5 ; "
        "ligne `CHAINE_P3BIS` de « Marqueurs restants » | corrigées (le texte d'origine est gardé quand il est "
        "historique, la correction ajoutée à côté) | R-2345 | C2-03, C2-08, C2-13, C2-14, C2-15, C2-19, C2-20 |",
        "| 5 | `CANDIDAT_RELU` | marqueur | rempli : brouillon 11 (`409c37ed…`), rapport `85ee0b47…`, « relu, conforme » "
        "sur le candidat 1 ; écart du candidat 1 au candidat 2 contrôlé par programme et relu par un relecteur neuf, "
        "consigné au registre (non cité : même circularité) | R-2344 ; R-2345 | C2-17, C2-21 |",
        "| 6 | date du rendez-vous (P-11) | place préparée à « Décisions pour Lazar » | « date tenue : défaut échu, R-… » "
        "(numéro de la ligne du registre qui constate le défaut, donné au script par la session mère) | R-2021 ; P-11 "
        "| C2-16 |",
        "| 7 | marqueurs | deux | aucun | — | C2-12, C2-17, C2-18 |",
        "",
        para("**Sections gelées** : seul C2-11 (N-1) touche une section gelée (« Plan d'analyse ») ; les six autres "
             "sections gelées (« Hypothèse », « Prédiction chiffrée et signe attendu », « Métrique », « Seuil », "
             "« Critères de lecture gelés », « Liste d'arrêt ») sont égales à l'octet à celles du candidat 1, et "
             "« Plan d'analyse » est celle du candidat 1 où seul N-1 est appliqué (contrôlé par programme : journal du "
             "candidat 2). Aucune hypothèse, prédiction, aucun signe, aucune métrique, aucun seuil, critère de lecture, "
             "aucune liste d'arrêt, aucun code ni aucune configuration ne change. Défaire les couples C2, dans l'ordre "
             "inverse, redonne le candidat 1 à l'octet (journal).", "", ""),
        "",
        "## Table « ce qui change du 12 au candidat 1 »",
        ""])
    couple(10, "table neuve, en tête des tables (non gelée)", None, "consigne de la mère",
           "table « du candidat 1 au candidat 2 »", "## Table « ce qui change du 12 au candidat 1 »\n", table)

    couple(11, "Plan d'analyse, point 10 (GELÉE)", "Plan d'analyse", "relecture courte, N-1 (R-2344) ; consigne",
           "« niveau tenu » dit un peu plus que la pièce (`1613d5bd…`, R-2320 : aucun dépassement établi) ; chiffres "
           "et intervalles inchangés", "**niveau tenu** — 0,0100", "**aucun dépassement établi du niveau** — 0,0100")

    regle = [
        para("répétition finale à blanc, journaux versés : marqueur `CHAINE_P3BIS`, **rempli au candidat 2** (R-2345), "
             "sans circularité : ce texte ne cite ni les versions épinglées des contrôles et de la récupération, ni les "
             "journaux canoniques par leur empreinte, car l'épingle `CANDIDAT_RELU` des contrôles est l'empreinte de "
             "ce texte (bloc 4, `releve` : le texte de S égal, octet pour octet, au candidat relu épinglé) et les sept "
             "journaux sont joués après l'épinglage (P-6), la répétition finale sur ce texte même ; comme le texte "
             "scellé de P3 (`prereg/P3-premier-test-i-a-v1.md` l. 470-485), qui citait sa chaîne par ses noms et dont "
             "les copies versées ne différaient que par les épingles :", I3, I3),
        para("- (a) **chaîne v2 au commit du code** "
             f"{bt(CODE)}, quinze fichiers, empreintes recalculées par `git show` à ce commit, chacune égale à son "
             f"compagnon au même commit : {l_chaine} ;", I3, I3 + "  "),
        para("- (b) **règle d'épinglage** : sur la branche de scellement, `controles_avant_depense_p3bis_v2.sh` et "
             "`recuperation_p3bis_v2.sh` ne diffèrent de ces versions **que** par leurs lignes `NOM=A_EPINGLER` "
             "(treize et une), remplies des valeurs que ce texte cite : code relu (`CODE_RELU`, le commit du code "
             "ci-dessus et à l'en-tête) ; configuration relue et consignes relues (`CONFIG_RELUE`, `CONSIGNES_RELUES` "
             "et leurs chemins sous `brouillons/` : en-tête, ligne « Configuration de P3 ») ; sortie de l'essai de "
             "fermeture (`ESSAI_FERMETURE` et son chemin : plan, point 6, sortie v3 jouée au commit du code) ; "
             "longueurs attendues (`LONGUEURS_ATTENDUES` et son chemin : plan, point 2) ; rapports attendus "
             "(`RAPPORTS_ATTENDUS` : les paires chemin=empreinte des rapports de contre-lecture et de relecture de "
             "P3-bis, de son code et de sa chaîne que ce texte cite par leur chemin et leur empreinte entière, la "
             f"contre-lecture 4 comprise, soit neuf : {l_rapports}) ; chemin du candidat relu "
             f"(`CANDIDAT_RELU_CHEMIN`, {bt(C2)}) ; sauf `CANDIDAT_RELU`, empreinte de ce texte, qu'il ne peut citer, et "
             "`PY` (contrôles et récupération), interpréteur de l'environnement de P-1 de la session qui scelle, écrit "
             "au registre des décisions. Les treize autres fichiers de la chaîne restent, sur la branche de "
             "scellement, égaux à l'octet à leurs versions au commit du code (l'étape 5 de `sceller_p3bis_v2.sh` les "
             "compare à leurs copies versées). Vérification par programme avant S, constatée au registre : `git diff` "
             "des quinze fichiers entre le commit du code et la branche de scellement ne montre que ces quatorze "
             "lignes, aux valeurs citées ;", I3, I3 + "  "),
        para("- (c) **journaux canoniques**, nommés ici : "
             f"{l_journaux} ; joués après ce texte (P-6 : les cinq bancs et la répétition jouet après l'épinglage, puis "
             "la répétition finale en mode décisif), versés et scellés sous "
             f"{bt(CHAINE + '/')} sur la branche de scellement avant S, exigés par l'étape 5 de `sceller_p3bis_v2.sh` "
             "(`PREUVES_EXIGEES` : dernière ligne de verdict, scripts éprouvés égaux aux copies versées) ; **cités par "
             "leur empreinte au registre des décisions** (constat de P-6 par la session mère), jamais dans ce texte.",
             I3, I3 + "  "),
    ]
    couple(12, "Ce que le code et la chaîne doivent changer, point 6 (non gelée)", None, "R-2345 ; consigne",
           "CHAINE_P3BIS rempli sans circularité : (a) chaîne au commit du code, (b) règle d'épinglage, (c) journaux "
           "nommés, cités au registre",
           "   répétition finale à blanc, journaux versés (`<<CHAINE_P3BIS>>`).\n", "\n".join(regle) + "\n")

    couple(13, "Ce que le code et la chaîne doivent changer, point 6 (non gelée)", None, "R-2345",
           "« chemins et empreintes de la chaîne épinglée, journaux canoniques … tout passe par le marqueur » : corrigé",
           "tout passe par le marqueur `CHAINE_P3BIS`, rempli au\n   candidat ; rien d'autre de ce texte n'en dépend.\n",
           "tout passe par le marqueur `CHAINE_P3BIS`, rempli au\n   candidat ; rien d'autre de ce texte n'en dépend.\n"
           + para("**Candidat 2 (R-2345)** : ce texte ne cite ni les empreintes de la chaîne épinglée ni celles des "
                  "journaux canoniques (citation circulaire : l'épingle `CANDIDAT_RELU` est l'empreinte de ce texte, et "
                  "les journaux sont joués après lui) ; le marqueur cite la chaîne v2 au commit du code, la règle "
                  "d'épinglage et les noms des journaux (ci-dessus) ; leurs empreintes sont au registre des décisions "
                  "(constat de P-6).", I3, I3) + "\n")

    couple(14, "Ce que le code et la chaîne doivent changer, point 6 (non gelée)", None, "R-2345",
           "« Restent pour CHAINE_P3BIS : épingles, passages canoniques » : corrigé",
           "   complément v2) : section « Préalables ».\n",
           "   complément v2) : section « Préalables ».\n"
           + para("Candidat 2 (R-2345) : ces épingles et ces passages se font après ce texte, qui ne les cite pas par "
                  "leur empreinte ; le marqueur est rempli ci-dessus sans eux.", I3, I3) + "\n")

    couple(15, "Préalables, P-5 (non gelée)", None, "R-2345",
           "« les versions épinglées sont celles que cite le marqueur » : corrigé ; vérification de la règle ajoutée",
           "les versions épinglées sont celles que cite le marqueur `CHAINE_P3BIS` | session mère, ou le développeur de "
           "la chaîne sur son ordre, après la contre-lecture 4 | aucune ligne « `NOM=A_EPINGLER` » dans les deux "
           "fichiers ; tant qu'une épingle reste, les contrôles, le scellement et la répétition finale refusent (code 2) |",
           "candidat 2 (R-2345) : les versions épinglées ne sont pas citées par ce texte (l'épingle `CANDIDAT_RELU` est "
           "son empreinte : citation circulaire) ; elles ne diffèrent des versions au commit du code que cite le "
           "marqueur `CHAINE_P3BIS` (chaîne v2 : `controles_avant_depense_p3bis_v2.sh`, treize lignes ; "
           "`recuperation_p3bis_v2.sh`, une ligne) que par leurs lignes « `NOM=A_EPINGLER` », remplies des valeurs que "
           f"cite ce texte, sauf `CANDIDAT_RELU` (empreinte de ce texte, chemin {bt(C2)}) et `PY` (écrit au registre "
           "des décisions) | session mère, ou le développeur de la chaîne sur son ordre, après la contre-lecture 4 | "
           "aucune ligne « `NOM=A_EPINGLER` » dans les deux fichiers ; tant qu'une épingle reste, les contrôles, le "
           "scellement et la répétition finale refusent (code 2) ; candidat 2 : avant S, `git diff` des quinze fichiers "
           "de la chaîne entre le commit du code et la branche de scellement ne montre que ces quatorze lignes, aux "
           "valeurs citées (par programme, constaté au registre) |")

    couple(16, "Décisions pour Lazar, date du rendez-vous (non gelée)", None, "P-11 ; R-2021 ; consigne",
           "phrase « date tenue », à la place préparée ; numéro donné au script par la session mère",
           "Lazar recopiés, écrite par la version qui remplit `CHAINE_P3BIS` et `CANDIDAT_RELU`, avant S (P-11).\n",
           "Lazar recopiés, écrite par la version qui remplit `CHAINE_P3BIS` et `CANDIDAT_RELU`, avant S (P-11).\n"
           f"  **Candidat 2** : date tenue : défaut échu, {JETON} (ligne du registre des décisions qui constate le défaut "
           "échu de R-2021,\n  datée avant S ; P-11).\n")

    ancien17 = ("  appliqués par script, sections gelées comparées au brouillon 11), n'est pas faite ») : "
                "`<<CANDIDAT_RELU>>` — par un\n  agent qui n'a écrit ni ce texte ni ses couples : couples des brouillons 12 "
                "et suivants réappliqués par script au\n  brouillon 11, sections gelées comparées au brouillon 11, marqueurs "
                "remplis contrôlés ; empreinte du texte de départ,\n  chemin et empreinte de son rapport, ici. L'empreinte "
                "du candidat lui-même n'est pas écrite dans ce texte (il ne peut\n  pas se citer) : c'est l'épingle "
                "`CANDIDAT_RELU` de `controles_avant_depense_p3bis_v1.sh` (P-5), que le bloc 4 des\n  contrôles exige "
                "égale, octet pour octet, au texte de S.\n")
    nouveau17 = para(
        "appliqués par script, sections gelées comparées au brouillon 11), n'est pas faite ») : "
        "relecture par un agent qui n'a écrit ni ce texte ni ses couples : couples des brouillons 12 et suivants "
        "réappliqués par script au brouillon 11, sections gelées comparées au brouillon 11, marqueurs remplis "
        "contrôlés ; empreinte du texte de départ, chemin et empreinte de son rapport, ici. **Faite ; marqueur rempli "
        "au candidat 2** (R-2344) : relecteur neuf **Claude Fable 5.2** (`claude-fable-5-2`), autre modèle que le "
        "rédacteur du candidat 1 (Opus 5.5), qui n'a écrit ni P3-bis, ni son code, ni sa chaîne, ni aucune de leurs "
        "contre-lectures ni aucun de leurs couples, et qui n'a lu de T0.7 que `src/controle_ia/t07/plancher_v2.py`, que "
        "P3-bis importe ; 11 novembre 2026, de 13:06 à 13:15 UTC ; texte de départ, le brouillon 11 "
        f"{bt(B11)} ({bt(EMP[B11])}) ; texte relu, le candidat 1 {bt(C1)} ({bt(EMP[C1])}) ; rapport {bt(RELECTURE)} "
        f"({bt(EMP[RELECTURE])}) ; verdict **« relu, conforme »** sur le candidat 1 : brouillon 11, plus les couples "
        "du brouillon 12, les couples RA et les couples C1, égal au candidat 1 à l'octet ; trente et un couples gelés, "
        "chacun rattaché à sa décision ; « Hypothèse » et « Prédiction chiffrée et signe attendu » égales au brouillon "
        "11 ; marqueurs remplis vérifiés sur leurs pièces ; aucun couple de correction exigé, aucun nœud ; notes N-1 "
        "(retenue, R-2344 : au plan, point 10, couple C2-11 du candidat 2) à N-5. **Écart du candidat 1 au candidat "
        "2** (couples C2, dont N-1, seul couple gelé) : contrôlé par programme (journal du candidat 2 : couples "
        "défaits, empreintes des sept sections gelées) et relu par un relecteur neuf, consigné au registre des "
        "décisions ; il ne peut être cité ici, pour la même raison que l'empreinte du candidat. L'empreinte du "
        "candidat lui-même n'est pas écrite dans ce texte (il ne peut pas se citer) : c'est l'épingle `CANDIDAT_RELU` "
        "de `controles_avant_depense_p3bis_v2.sh` (P-5 ; `_v1` aux brouillons), que le bloc 4 des contrôles exige "
        "égale, octet pour octet, au texte de S.", "  ", "  ")
    couple(17, "Contre-lecture, relecture courte (non gelée)", None, "R-2344 ; R-2345 ; consigne",
           "CANDIDAT_RELU rempli : texte de départ, rapport, verdict ; écart du candidat 1 au candidat 2 au registre",
           ancien17, nouveau17 + "\n")

    couple(18, "Marqueurs restants (non gelée)", None, "consigne de la mère", "aucun marqueur au candidat 2",
           "Candidat 1 : **deux marqueurs distincts**",
           para("Candidat 2 : **aucun marqueur** : `CHAINE_P3BIS` rempli sans circularité (« Ce que le code et la "
                "chaîne doivent changer », point 6 ; R-2345 : définition corrigée, ligne de la table ci-dessous) et "
                "`CANDIDAT_RELU` rempli (section « Contre-lecture » ; R-2344) ; la date tenue (P-11) est écrite à "
                "« Décisions pour Lazar ».", "", "") + "\nCandidat 1 : **deux marqueurs distincts**")

    couple(19, "Marqueurs restants, ligne CHAINE_P3BIS (non gelée)", None, "R-2345", "marqueur rempli au candidat 2",
           "| `CHAINE_P3BIS` — **candidat 1 : chaîne v2** (",
           "| `CHAINE_P3BIS` — **rempli au candidat 2** (« Ce que le code et la chaîne doivent changer », point 6 ; "
           "R-2345) ; **candidat 1 : chaîne v2** (")

    couple(20, "Marqueurs restants, ligne CHAINE_P3BIS (non gelée)", None, "R-2345 (définition circulaire)",
           "définition du marqueur corrigée",
           "| chemins et empreintes de la chaîne `docs/procedures/P3-bis-temoin-positif-v1/` (quinze fichiers, versions "
           "épinglées des contrôles et de la récupération), des cinq journaux canoniques des bancs et des deux des "
           "répétitions (la finale en mode décisif), chacun avec son compagnon, versés sur la branche de scellement "
           "avant S, sous la forme `` `docs/procedures/P3-bis-temoin-positif-v1/<fichier>` (`<sha256>`) `` ;",
           "| **candidat 2 (R-2345 ; la définition du candidat 1 faisait citer à ce texte les versions épinglées et les "
           "sept journaux par leur empreinte : circulaire)** : (a) chemins et empreintes des quinze fichiers de la "
           "chaîne `docs/procedures/P3-bis-temoin-positif-v1/` **au commit du code**, sous la forme "
           "`` `docs/procedures/P3-bis-temoin-positif-v1/<fichier>` (`<sha256>`) `` ; (b) règle d'épinglage : sur la "
           "branche de scellement, `controles_avant_depense_p3bis_v2.sh` et `recuperation_p3bis_v2.sh` ne diffèrent "
           "de ces versions que par leurs lignes `NOM=A_EPINGLER` (treize et une), aux valeurs que cite ce texte, sauf "
           "`CANDIDAT_RELU` (empreinte de ce texte) et `PY` (registre des décisions), vérifiée par programme avant S ; "
           "(c) noms des cinq journaux canoniques des bancs et des deux des répétitions (la finale en mode décisif), "
           "joués après ce texte, versés et scellés avec leur compagnon sur la branche de scellement avant S, exigés "
           "par l'étape 5 de `sceller_p3bis_v2.sh`, cités par leur empreinte au registre des décisions (constat de "
           "P-6), jamais dans ce texte ;")

    couple(21, "Marqueurs restants, ligne CANDIDAT_RELU (non gelée)", None, "R-2344 ; R-2345",
           "marqueur rempli au candidat 2",
           "| `CANDIDAT_RELU` — **neuf au brouillon 12** (section « Contre-lecture ») |",
           "| `CANDIDAT_RELU` — **neuf au brouillon 12 ; rempli au candidat 2** (section « Contre-lecture » ; R-2344 : "
           "relecture courte `85ee0b47…`, « relu, conforme » sur le candidat 1 ; écart du candidat 1 au candidat 2 au "
           "registre des décisions, R-2345) |")
    return c


def appliquer(texte: str, couples: list[dict]) -> str:
    for x in couples:
        n = texte.count(x["ancien"])
        if n != 1:
            raise SystemExit(f"{x['id']} : « ancien » trouvé {n} fois")
        texte = texte.replace(x["ancien"], x["nouveau"], 1)
    return texte


def main(argv: list[str]) -> int:
    if len(argv) != 3 or not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", argv[2]):
        print("usage : construire DOSSIER_DE_SORTIE AAAA-MM-JJTHH:MM:SSZ", file=sys.stderr)
        return 2
    sortie, heure = Path(argv[1]), argv[2]
    cibles = [sortie / NOM_COUPLES, sortie / NOM_EPINGLES, sortie / NOM_JOURNAL]
    if any(p.exists() or Path(str(p) + ".sha256").exists() for p in cibles):
        raise SystemExit("une sortie existe déjà (R12)")
    journal = [f"Construction des couples C2 et des épingles proposées, {heure} (heure passée en argument, `date -u`)"]
    etat = controles(journal)
    couples = couples_c2()
    t1 = Path(C1).read_text(encoding="utf-8")
    if JETON in t1:
        raise SystemExit("jeton déjà présent dans le candidat 1")
    brut = json.dumps(couples, ensure_ascii=False, indent=1) + "\n"
    if brut.count(JETON) != 1 or sum(x["nouveau"].count(JETON) for x in couples) != 1:
        raise SystemExit("jeton R-NNNN : une seule occurrence attendue dans les couples")
    if re.search(r"<<[A-Z0-9_]+>>", "".join(x["nouveau"] for x in couples)):
        raise SystemExit("marqueur dans un « nouveau »")
    t2 = appliquer(t1, couples)
    journal.append(f"{len(couples)} couples, chacun trouvé une fois ; texte à blanc (jeton non remplacé) : "
                   f"{h(t2.encode())}")
    for x in couples:
        if x["section_gelee"]:
            journal.append(f"couple gelé : {x['id']} ({x['section_gelee']})")
    # épingles proposées
    rapports = " ".join(f"{f}={e}" for f, e, _ in RAPPORTS)
    for f, e, _ in RAPPORTS:
        if not re.fullmatch(r"[a-zA-Z0-9_./-]+\.(md|json)=[0-9a-f]{64}", f"{f}={e}"):
            raise SystemExit(f"paire mal formée : {f}")
    ctl = git("show", f"{CODE}:{CHAINE}/controles_avant_depense_p3bis_v2.sh").decode()
    valeurs = {"CANDIDAT_RELU_CHEMIN": C2, "CONFIG_RELUE": CFG_RELUE[1], "CONFIG_RELUE_CHEMIN": CFG_RELUE[0],
               "CONSIGNES_RELUES": CONS_RELUES[1], "CONSIGNES_RELUES_CHEMIN": CONS_RELUES[0], "CODE_RELU": CODE,
               "ESSAI_FERMETURE": ESSAI[1], "ESSAI_FERMETURE_CHEMIN": ESSAI[0],
               "LONGUEURS_ATTENDUES": LONGUEURS[1], "LONGUEURS_ATTENDUES_CHEMIN": LONGUEURS[0],
               "RAPPORTS_ATTENDUS": rapports}
    lignes = {}
    for nom, v in valeurs.items():
        m = re.search(rf"^{nom}=A_EPINGLER(.*)$", ctl, re.M)
        val = f'"{v}"' if " " in v else v
        lignes[nom] = {"ligne_au_commit_du_code": m.group(0), "ligne_proposee": f"{nom}={val}{m.group(1)}"}
    # contrôle : chaque valeur proposée est citée par le texte (forme des blocs 2, 6, 7, 14 ; chemins entre accents)
    plat = " ".join(t2.split())
    cites = [CODE, CFG_RELUE[1], f"`{CFG_RELUE[0]}`", CONS_RELUES[1], f"`{CONS_RELUES[0]}`",
             f"`{ESSAI[0]}` (`{ESSAI[1]}`", f"`{LONGUEURS[0]}` (`{LONGUEURS[1]}`", f"`{C2}`"]
    cites += [f"`{f}`" for f, _, _ in RAPPORTS] + [e for _, e, _ in RAPPORTS]
    manque = [x for x in cites if x not in plat]
    if manque:
        raise SystemExit(f"valeurs proposées non citées par le texte : {manque}")
    journal.append(f"chaque valeur proposée est citée par le texte à blanc ({len(cites)} formes cherchées)")
    a_verser = [x for x in etat["pieces"] if x["a_d0d9fcb8"] != "OK"]
    epingles = {
        "titre": "P3-bis : épingles proposées des contrôles avant dépense et de la récupération (chaîne v2), v1",
        "ecrit": heure, "redacteur": "Claude Opus 5.5 (claude-opus-5-5), rédacteur neuf du candidat 2",
        "consigne": f"{CONSIGNE} ({EMP[CONSIGNE]})",
        "commit_du_code": CODE, "branche_de_scellement": {"nom": "scellement/p3bis-v1", "commit": SCEL},
        "main_au_moment_de_la_verification": etat["main"],
        "regle": ("controles_avant_depense_p3bis_v2.sh et recuperation_p3bis_v2.sh ne diffèrent de leurs versions au "
                  "commit du code que par leurs lignes NOM=A_EPINGLER (treize et une) ; les treize autres fichiers de "
                  "la chaîne sont égaux à leurs versions au commit du code ; CANDIDAT_RELU et PY ne sont pas proposés "
                  "ici (R-2345)"),
        "epingles_controles": {
            "CANDIDAT_RELU": "non proposée : empreinte du texte de S (le candidat 2 écrit par le script de la session "
                             "mère, rapportée par son journal) ; le texte ne peut la citer",
            **valeurs,
            "PY": "non proposée : interpréteur de l'environnement de P-1 de la session qui scelle, écrit au registre"},
        "epingles_recuperation": {"PY": "non proposée : la même que celle des contrôles"},
        "lignes": lignes,
        "rapports_attendus": [{"chemin": f, "empreinte": e, "objet": o} for f, e, o in RAPPORTS],
        "rapports_ecartes_question": [
            {"chemin": f, "empreinte": e, "objet": o,
             "verifie": "fichier et compagnon égaux sur main" if v else "non vérifié (fichier de T0.7, non ouvert)"}
            for f, e, o, v in ECARTES],
        "pieces_verifiees": etat["pieces"],
        "pieces_a_verser": [
            {"chemin": x["chemin"], "empreinte": x["empreinte"], "commit_ou_la_prendre": x["verifiee_a"],
             "avec_compagnon": True, "epingle": x["epingle"], "a_d0d9fcb8": x["a_d0d9fcb8"]} for x in a_verser]
        + [{"chemin": C2, "empreinte": "celle du candidat 2 écrit par le script au lancement (journal du candidat 2)",
            "commit_ou_la_prendre": "commit de la session mère qui le verse (à venir)", "avec_compagnon": True,
            "epingle": "CANDIDAT_RELU, CANDIDAT_RELU_CHEMIN", "a_d0d9fcb8": "absent"}],
        "deja_a_d0d9fcb8": [x["chemin"] for x in etat["pieces"] if x["a_d0d9fcb8"] == "OK"],
        "hors_liste": ("ne sont pas des pièces des épingles, mais le texte les dit versées sur la branche avant S : la "
                       "chaîne épinglée et les sept journaux canoniques (P-5, P-6) ; les pièces de la phase 1 au commit "
                       "dfb1ed7b (sortie de P-2 et autres, en-tête) ; la sortie v3 de l'essai v2 et le rejeu de "
                       "concordance au commit 8ad29273 (en-tête, pièces du brouillon 11) ; non vérifiées ici"),
    }
    sortie.mkdir(parents=True, exist_ok=True)
    (sortie / NOM_COUPLES).write_text(brut, encoding="utf-8")
    (sortie / NOM_EPINGLES).write_text(json.dumps(epingles, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    journal.append(f"couples : {h(brut.encode())}")
    journal.append(f"épingles proposées : {h((sortie / NOM_EPINGLES).read_bytes())}")
    journal.append(f"pièces à verser : {len(epingles['pieces_a_verser'])} ; déjà à d0d9fcb8 : "
                   f"{len(epingles['deja_a_d0d9fcb8'])}")
    journal.append("CONSTRUCTION : CONFORME")
    (sortie / NOM_JOURNAL).write_text("\n".join(journal) + "\n", encoding="utf-8")
    print("\n".join(journal))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
