"""Candidat 3 du préenregistrement de P3-bis : construction des couples C3 et des épingles proposées v2 (v1).

Écrit le 2026-11-11, à partir de 14:53 UTC (`date -u`), par le rédacteur du candidat 2 (Claude Opus 5.5,
`claude-opus-5-5`, sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`), sur la demande de la session mère
(message ; décisions R-2367, R-2373, R-2374, sur `main` au commit `883a2432`). Aucun appel externe ; aucune écriture git
(`git show`, `git diff`, `git log`, `git cat-file`, `git merge-base`, `git rev-parse` en lecture seule) ; aucun fichier
de T0.7 ni des interdits communs v2 ouvert ; du rapport des bancs, de leur contre-lecture et de la relecture courte du
candidat 2, les seules empreintes.

Candidat 3 = candidat 2 (`eb7e5b8b…`) + couples C3, tous hors des sections gelées : (1) `CHAINE_P3BIS`, point (a) : les
trois bancs corrigés sur place (R-2367) cités au commit de correction `68ded698`, les douze autres fichiers au commit du
code ; (2) règle (b) : branche `scellement/p3bis-v2`, bancs égaux à `68ded698`, dix fichiers au commit du code,
compagnons des cinq fichiers changés réécrits (R-2360) ; ligne P-5 ; (3) onze rapports attendus (contre-lecture des
bancs, relecture courte du candidat 2 en plus) ; (4) date tenue inchangée ; (5) table « du candidat 2 au candidat 3 » et
en-tête ; (6) épingles proposées v2.

Ce que fait le script, sans rien écrire tant qu'un contrôle échoue (R5) : vérifie ses entrées par empreinte et
compagnon ; recalcule par `git show` les empreintes des quinze fichiers de la chaîne (douze au commit du code, trois au
commit de correction), chacune égale à son compagnon ; vérifie que le commit de correction ne change que les trois bancs
et leurs compagnons ; vérifie chaque pièce des épingles sur `main` (les longueurs attendues au commit `dfb1ed7b`) et
relève sa présence à `d0d9fcb8`, `a3116ff5` et `68ded698` ; construit les couples (chaque « ancien » trouvé une fois dans
le texte courant, appliqués dans l'ordre) ; vérifie que chaque valeur proposée est citée par le texte ; écrit (R12)
couples, épingles v2 et journal de construction.

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

DOSSIER = "brouillons/P3-bis-temoin-positif-v1"
C1 = f"{DOSSIER}/P3-bis-preenregistrement-v1-candidat1.md"
C2 = f"{DOSSIER}/P3-bis-preenregistrement-v1-candidat2.md"
C3 = f"{DOSSIER}/P3-bis-preenregistrement-v1-candidat3.md"
PIECES3 = f"{DOSSIER}/P3-bis-preenregistrement-v1-candidat3-pieces"
REL1 = f"{DOSSIER}/P3-bis-candidat1-relecture-courte-v1.md"
REL2 = f"{DOSSIER}/P3-bis-candidat2-relecture-courte-v1.md"
NOTES = "docs/notes/g0-deux-semaines-v1/p3bis-regle-plancher-v1"
RAPPORT_BANCS = f"{NOTES}/rapport-bancs-epingles-p3bis-v1.md"
CL_BANCS = f"{NOTES}/contre-lecture-courte-bancs-epingles-p3bis-v1.md"
NOM_COUPLES = "P3-bis-preenregistrement-v1-candidat3-couples-v1.json"
NOM_EPINGLES = "P3-bis-epingles-proposees-v2.json"
NOM_JOURNAL = "P3-bis-preenregistrement-v1-candidat3-construire-journal-v1.txt"
EPINGLES_V1 = f"{DOSSIER}/P3-bis-preenregistrement-v1-candidat2-pieces/P3-bis-epingles-proposees-v1.json"

EMP = {
    C2: "eb7e5b8b671a71a745323135fc6aed5b0f30ad28e515575518189a2d22d71ecc",
    REL2: "c559f2c8b63fb2562cb337502ccfb853d9b2963fef2b915d6bd16bb1dc65964f",
    RAPPORT_BANCS: "a4020e30797a0abe08fc12a3985a0f7dd2e32cb933c5db89dee0f0d47d495a48",
    CL_BANCS: "df732d18a8b7a65566f0ad8fd47bf59cb040ce3c12b73cc5991e770b23e267ae",
    EPINGLES_V1: "0fb1443aff22133c8aaaac1616bbc191a53cfd0b2de8c4ffbe8fe53e13240389",
}
CODE = "5e4575259478af3611e2c7fb1313342912caf484"           # commit du code cité
CORR = "68ded698ce1bbfd8815d7b7ab28557775e4d2e5b"           # commit de correction des trois bancs (R-2367, R-2373)
SCEL1 = "d0d9fcb8ddf82da3919736e9b97eb8aff4c71b45"          # scellement/p3bis-v1, P-3 et P-10 (R-2345)
TETE_V1 = "a3116ff529587121b283259b404684e07f9806f2"        # tête de scellement/p3bis-v1, abandonnée (R-2367)
PHASE1 = "dfb1ed7b7040fa22fca95d931d0e0a8b4ea43527"
CHAINE = "docs/procedures/P3-bis-temoin-positif-v1"
CHAINE_CODE = {      # ordre de `CHAINE` dans sceller_p3bis_v2.sh ; empreintes au commit du code
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
BANCS = {            # au commit de correction (R-2373)
    "essais_controles_p3bis_v2.sh": "36a88949fe435cb6dbf30de88789d2ccdd2829abdd1f83e2545605b434d6210d",
    "essais_recuperation_p3bis_v2.sh": "ae2e2d2f3525672c2d65fccbf41620897caf543d66b7ed6928251a28de35f954",
    "repetition_jouet_p3bis_v2.sh": "750ec2530cc4261a57a50a54c062e770e20399127247ba5918fa904267022e02",
}
ORDRE_BANCS = ("essais_controles_p3bis_v2.sh", "essais_recuperation_p3bis_v2.sh", "repetition_jouet_p3bis_v2.sh")
CFG_RELUE = (f"{DOSSIER}/P3-bis-preenregistrement-v1-candidat1-pieces/P3-bis-temoin-positif-config-v1-candidat1.json",
             "612b0c6ce5c4263eb3016b72ad85155dd2307f9dd887379d2a1133ed644a9d05")
CONS_RELUES = (f"{DOSSIER}/P3-bis-consignes-v1-brouillon2.md",
               "7d35576d65c030edcc6441e142ea95732679b674edcb1fd1af86ab8f69c04367")
ESSAI = (f"{NOTES}/essai-fermeture-p3bis-v3-sortie-v1.txt",
         "9375628699e95fc6563d2da4ce0172371cfeb2e3fcb56b0fbe8e2aa6774b1464")
LONGUEURS = ("docs/notes/g0-deux-semaines-v1/p3bis-prealables-v1/longueurs-attendues-p3bis-v1.json",
             "7c94d43cc7bea9a5af3c5c5ec34f552256bbcf258a0436d1a2295c91d45cfb21")
RAPPORTS = (   # onze, dans l'ordre de leur date
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
    (f"{NOTES}/contre-lecture-courte-code-p3bis-regle-a-v1.md",
     "03f1bb59d7fc2afed8bf8939f2457c177a36d477deae5bdb6e1c1dc2f3235141",
     "contre-lecture différentielle courte du code 5e457525 et de la chaîne v2"),
    (REL1, "85ee0b47078d18311bb70872877c0b73c54fc480219e87678e4cc6ae63551eec",
     "relecture courte de l'écart du brouillon 11 au candidat 1"),
    (REL2, "c559f2c8b63fb2562cb337502ccfb853d9b2963fef2b915d6bd16bb1dc65964f",
     "relecture courte de l'écart du candidat 1 au candidat 2 (R-2358)"),
    (CL_BANCS, "df732d18a8b7a65566f0ad8fd47bf59cb040ce3c12b73cc5991e770b23e267ae",
     "contre-lecture courte des bancs corrigés, commit 68ded698 (R-2374)"),
)


def h(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def git(*args: str) -> bytes:
    r = subprocess.run(["git", *args], capture_output=True)
    if r.returncode != 0:
        raise SystemExit(f"git {' '.join(args)} : code {r.returncode}")
    return r.stdout


def existe(ref: str, chemin: str) -> bool:
    return subprocess.run(["git", "cat-file", "-e", f"{ref}:{chemin}"], capture_output=True).returncode == 0


def piece(ref: str, chemin: str, e: str) -> str:
    if not existe(ref, chemin):
        return "absent"
    hf = h(git("show", f"{ref}:{chemin}"))
    comp = git("show", f"{ref}:{chemin}.sha256").decode().strip() if existe(ref, chemin + ".sha256") else None
    if hf != e:
        return f"autre empreinte ({hf[:12]}…)"
    if comp != f"{e}  {Path(chemin).name}":
        return "compagnon autre"
    return "OK"


def para(texte: str, i0: str, i1: str, largeur: int = 120) -> str:
    t = " ".join(texte.split())
    t = re.sub(r"`[^`]*`", lambda m: m.group(0).replace(" ", "\x00"), t)
    t = t.replace("« ", "«\x00").replace(" »", "\x00»").replace(" ;", "\x00;").replace(" :", "\x00:")
    return textwrap.fill(t, width=largeur, initial_indent=i0, subsequent_indent=i1, break_long_words=False,
                         break_on_hyphens=False).replace("\x00", " ")


def bt(x: str) -> str:
    return f"`{x}`"


def controles(journal: list) -> dict:
    for f, e in EMP.items():
        if h(Path(f).read_bytes()) != e or Path(f + ".sha256").read_text(encoding="utf-8").strip() != \
                f"{e}  {Path(f).name}":
            raise SystemExit(f"entrée {f} : empreinte ou compagnon inattendus")
        journal.append(f"entrée {f} : {e} (= compagnon)")
    main = git("rev-parse", "main").decode().strip()
    for f in (C2, REL2, RAPPORT_BANCS, CL_BANCS):
        if piece(main, f, EMP[f]) != "OK":
            raise SystemExit(f"{f} : absent de main ou autre empreinte")
    journal.append(f"candidat 2, relecture courte du candidat 2, rapport et contre-lecture des bancs : sur main ({main[:8]})")
    for c in (CODE, CORR, SCEL1, TETE_V1):
        if git("cat-file", "-t", c).strip() != b"commit":
            raise SystemExit(f"{c} absent")
    if subprocess.run(["git", "merge-base", "--is-ancestor", CODE, CORR]).returncode != 0:
        raise SystemExit("le commit de correction ne descend pas du commit du code")
    changes = git("diff", "--name-only", CODE, CORR).decode().split()
    attendu = sorted(f"{CHAINE}/{b}{s}" for b in BANCS for s in ("", ".sha256"))
    if sorted(changes) != attendu:
        raise SystemExit(f"le commit de correction change {changes}")
    journal.append(f"git diff --name-only {CODE[:8]} {CORR[:8]} : les trois bancs et leurs compagnons, rien d'autre")
    for s, e in CHAINE_CODE.items():
        if piece(CODE, f"{CHAINE}/{s}", e) != "OK":
            raise SystemExit(f"{s} au commit du code")
        ref, e2 = (CORR, BANCS[s]) if s in BANCS else (CORR, e)
        if piece(ref, f"{CHAINE}/{s}", e2) != "OK":
            raise SystemExit(f"{s} au commit de correction")
        journal.append(f"chaîne : {s} — commit du code {e} ; commit de correction {e2} (= compagnons)")
    pieces = []
    for role, (f, e), ref in (("CONFIG_RELUE", CFG_RELUE, main), ("CONSIGNES_RELUES", CONS_RELUES, main),
                              ("ESSAI_FERMETURE", ESSAI, main), ("LONGUEURS_ATTENDUES", LONGUEURS, PHASE1)):
        pieces.append((role, f, e, ref))
    for f, e, objet in RAPPORTS:
        pieces.append((f"RAPPORTS_ATTENDUS ({objet})", f, e, main))
    for b in ORDRE_BANCS:
        pieces.append((f"banc corrigé (règle (b)) : {b}", f"{CHAINE}/{b}", BANCS[b], CORR))
    lignes = []
    for role, f, e, ref in pieces:
        r = piece(ref, f, e)
        if r != "OK":
            raise SystemExit(f"pièce {f} à {ref[:8]} : {r}")
        etat = {k: piece(c, f, e) for k, c in (("d0d9fcb8", SCEL1), ("a3116ff5", TETE_V1), ("68ded698", CORR))}
        dernier = git("log", "-1", "--format=%H", ref, "--", f).decode().strip()
        lignes.append({"role": role, "chemin": f, "empreinte": e, "commit_ou_la_prendre": ref,
                       "dernier_commit_qui_la_change": dernier, "presence": etat})
        journal.append(f"pièce {f} : {e} = compagnon à {ref[:8]} ; présence : {etat}")
    return {"main": main, "pieces": lignes}


def couples_c3(t2: str) -> list:
    I2, I3 = "  ", "   "
    c = []

    def couple(i, section, decision, motif, ancien, nouveau):
        c.append({"id": f"C3-{i:02d}", "fichier": C2, "section": section, "section_gelee": None,
                  "decision": decision, "motif": motif, "ancien": ancien, "nouveau": nouveau})

    l_douze = " ; ".join(f"{bt(CHAINE + '/' + s)} ({bt(e)})" for s, e in CHAINE_CODE.items() if s not in BANCS)
    l_bancs = " ; ".join(f"{bt(CHAINE + '/' + s)} ({bt(BANCS[s])})" for s in ORDRE_BANCS)
    anciens_bancs = ", ".join(f"`{CHAINE_CODE[s][:8]}…`" for s in ORDRE_BANCS)
    l_rapports = " ; ".join(f"{bt(f)} ({bt(e)})" for f, e, _ in RAPPORTS)

    couple(1, "titre (non gelée)", "demande de la mère (R-2367)", "nom du texte : candidat 3",
           "que P3) — v1 — candidat 2\n", "que P3) — v1 — candidat 3\n")

    statut = "\n".join([
        para("- Statut : **candidat 3**, écrit le 2026-11-11 à partir de 14:53 UTC (heure relevée par `date -u`) par le "
             "**rédacteur du candidat 2** (Claude Opus 5.5, `claude-opus-5-5`, même sous-agent de la session mère "
             "`session_01VJdZpSMxSdk2SJ1ScmdfNv`), sur la demande de la session mère (message ; décisions R-2367, "
             "R-2373 et R-2374, sur `main` au commit `883a2432`). Ce rédacteur n'a écrit ni les brouillons 1 à 12, ni "
             "le candidat 1, ni le code de P3-bis, ni sa chaîne, ni les bancs corrigés, ni aucune de leurs "
             "contre-lectures ou relectures, ni P3, ni T0.6, ni T0.7 ; **il n'a ouvert aucun fichier de T0.7** ; du "
             "rapport des bancs, de leur contre-lecture et de la relecture courte du candidat 2, il n'a relevé que les "
             "empreintes. Révision par **couples appliqués par script** (couples C3, chacun trouvé une fois, tous hors "
             "des sections gelées ; pièces sous "
             f"{bt(PIECES3 + '/')} : couples {bt(NOM_COUPLES)}, scripts "
             "`P3-bis-preenregistrement-v1-candidat3-construire-couples-v1.py` et "
             "`P3-bis-preenregistrement-v1-candidat3-faire-v1.py`, journaux de la construction et du candidat 3, "
             f"épingles proposées {bt(NOM_EPINGLES)}, scellés avec ce texte, R6) ; ce texte est écrit par le script "
             "d'application quand la session mère le lance. Non scellé ; rien n'est lancé, rien n'est dépensé ; aucune "
             "écriture git. **Marqueurs restants au candidat 3 : aucun.**", "", I2),
        para("- **Candidat 3 = candidat 2 + bancs corrigés + règle d'épinglage mise à jour + onze rapports + état** "
             "(R-2367, R-2373, R-2374 ; sections non gelées seulement) : trois bancs de la chaîne v2 "
             "(`essais_controles_p3bis_v2.sh`, `essais_recuperation_p3bis_v2.sh`, `repetition_jouet_p3bis_v2.sh`) ne "
             "savaient jouer que contre des contrôles non épinglés, alors que P-6 veut les bancs rejoués après "
             "l'épinglage (R-2367) ; ils sont corrigés sur place, sous les mêmes noms, au commit de correction "
             f"{bt(CORR)} (R-2373), contre-lu « citable au scellement » (R-2374). (1) **`CHAINE_P3BIS`, point (a)** : "
             "les trois bancs cités à leur empreinte au commit de correction, les douze autres fichiers au commit du "
             "code ; (2) **règle (b)** : branche de scellement `scellement/p3bis-v2` (la v1, à `a3116ff5`, abandonnée "
             "et gardée, R-2367) ; les deux fichiers épinglés ne diffèrent de leur version au commit du code que par "
             "leurs lignes `A_EPINGLER`, les trois bancs sont égaux à leur version au commit de correction, les dix "
             "autres fichiers au commit du code, les compagnons des cinq fichiers changés réécrits à la forme de "
             "`scellement.sceller` (R-2360, R-2367) ; ligne P-5 et ligne `CHAINE_P3BIS` de « Marqueurs restants » "
             "mises d'accord ; (3) **onze rapports attendus** : la contre-lecture courte des bancs et la relecture "
             "courte du candidat 2 (R-2358) en plus ; l'écart du candidat 2 au candidat 3 est contrôlé par programme et "
             "relu au registre (il ne peut être cité ici) ; (4) **date tenue inchangée** (mot de Lazar, R-2352) ; (5) "
             "**état des préalables** au 2026-11-11 vers 14:55 UTC : P-1, P-2, P-4 (phase 1, R-2295), P-7 (R-2340), P-8, "
             "P-9 (R-2349), P-11 (R-2352) et la relecture courte du candidat 2 (R-2358) faits ; P-3 et P-10 faits sur "
             "`scellement/p3bis-v1` (R-2345), à porter sur `scellement/p3bis-v2` ; P-5 fait sur la v1 (R-2361), à "
             "refaire sur la v2 (l'épingle `CANDIDAT_RELU` devient l'empreinte de ce texte) ; restent P-6 (bancs et "
             "répétitions rejoués après l'épinglage, R-2367), la relecture de l'écart du candidat 2 au candidat 3, "
             "puis S. **Aucune section gelée ne change** (contrôlé par programme : les sept empreintes de section "
             "égales à celles du candidat 2, journal du candidat 3) ; ni le code d'analyse (commit du code inchangé) ni "
             "la configuration ne changent ; seuls trois bancs de la chaîne changent. Le reste du candidat 2 est gardé "
             f"mot pour mot. Candidat 2 : {bt(C2)} ({bt(EMP[C2])}, recalculée, égale à son compagnon, sur `main`), "
             "gardé tel quel (R12). Ce que faisait le candidat 2, gardé pour mémoire :", "", I2),
        "- Statut du **candidat 2** : écrit le 2026-11-11 à partir de 13:26 UTC"])
    couple(2, "en-tête, statut (non gelée)", "R-2367, R-2373, R-2374", "statut du candidat 3 ; statut du candidat 2 gardé",
           "- Statut : **candidat 2**, écrit le 2026-11-11 à partir de 13:26 UTC", statut)

    couple(3, "en-tête, auteur (non gelée)", "R-2367", "auteur du candidat 3",
           "couples appliqués par script (candidat 2). Aucun n'a écrit P3",
           "couples appliqués par script (candidat 2) ; même rédacteur, couples appliqués par script (candidat 3). "
           "Aucun n'a écrit P3")

    couple(4, "en-tête, « Lu » (non gelée)", "R-2367", "lectures du candidat 3",
           "- **Lu** (brouillons 4 à 12, candidats 1 et 2 ;", "- **Lu** (brouillons 4 à 12, candidats 1 à 3 ;")

    lu = para(
        "- **pour le candidat 3** (rédacteur du candidat 2) : message de la session mère ; `registres/decisions.md` sur "
        "`main`, le début des lignes R-2350 à R-2374 (une recherche de numéros), puis R-2358, R-2360, R-2361, R-2367, "
        "R-2373 et R-2374 entières ; candidat 2 (`eb7e5b8b…`, écrit par ses couples), point 6 de « Ce que le code et la "
        "chaîne doivent changer » (l. 2076-2170) et les lignes trouvées par des recherches de mots dans ce seul "
        "fichier ; au commit de correction `68ded698` : `git diff --name-status` depuis le commit du code et empreintes "
        "des trois bancs et de leurs compagnons, par `git show`, contenus non affichés ; du rapport des bancs, de leur "
        "contre-lecture et de la relecture courte du candidat 2 : les empreintes seules (`sha256sum`, compagnons) ; "
        "pièces des épingles hachées par `git show` sur `main`, au commit `dfb1ed7b` et aux commits `d0d9fcb8`, "
        "`a3116ff5` et `68ded698` ;", "  ", "    ")
    couple(5, "en-tête, « Lu » (non gelée)", "R-2367", "lectures du candidat 3",
           "  - **pour le candidat 2** (rédacteur neuf)", lu + "\n  - **pour le candidat 2** (rédacteur neuf)")

    nonlu = para(
        "Candidat 3 : aucun fichier de T0.7 ouvert ni haché ; aucun fichier ni branche des interdits communs v2 ; "
        "aucun `diag/`, `runs/` ni `donnees/` ouvert ; contenus du rapport des bancs, de leur contre-lecture et de la "
        "relecture courte du candidat 2 non ouverts (empreintes seules ; le verdict de la relecture lu à R-2358) ; "
        "contenus des trois bancs corrigés non ouverts. Geste déclaré : la recherche des numéros R-2350 à R-2374 dans "
        "le registre a affiché le début de lignes qui parlent de l'audit des fuites de T0.7 et de la course 7b "
        "(lignes de registre, aucun fichier ouvert).", "  ", "  ")
    couple(6, "en-tête, « Non lu » (non gelée)", "R-2367", "ce que le candidat 3 n'a pas ouvert",
           "- Auteur : sous-agent de rédaction (brouillon 1)", nonlu + "\n- Auteur : sous-agent de rédaction (brouillon 1)")

    pieces = para(
        "- **Pièces citées par le candidat 3** (chacune égale à son compagnon, sur `main`) : candidat 2 "
        f"{bt(C2)} ({bt(EMP[C2])}) ; commit de correction des bancs {bt(CORR)} (branche "
        "`prep/p3bis-bancs-epingles-v1`, partie du commit du code ; R-2373) ; rapport du développeur des bancs "
        f"{bt(RAPPORT_BANCS)} ({bt(EMP[RAPPORT_BANCS])}) ; contre-lecture courte des bancs {bt(CL_BANCS)} "
        f"({bt(EMP[CL_BANCS])}, R-2374) ; relecture courte du candidat 2 {bt(REL2)} ({bt(EMP[REL2])}, R-2358) ; "
        "branche de scellement `scellement/p3bis-v2` (R-2367 ; la v1, tête "
        f"{bt(TETE_V1)}, abandonnée et gardée). **Pièces neuves du candidat 3**, sous {bt(PIECES3 + '/')}, chacune "
        "scellée, citées par leur nom seul : couples, scripts de construction et d'application, journaux de la "
        f"construction et du candidat 3, épingles proposées {bt(NOM_EPINGLES)} (valeurs des épingles, sauf "
        "`CANDIDAT_RELU` et `PY`, et liste des pièces à verser sur `scellement/p3bis-v2`) ; les épingles proposées v1 "
        "restent telles quelles (R12) et ne servent plus.", "", "  ")
    couple(7, "en-tête, pièces (non gelée)", "R-2367", "pièces citées et pièces neuves du candidat 3",
           "à écrire ce texte.\n", "à écrire ce texte.\n" + pieces + "\n")

    table = "\n".join([
        "## Table « ce qui change du candidat 2 au candidat 3 »",
        "",
        "| # | sujet | candidat 2 | candidat 3 | raison | couples |",
        "|---|---|---|---|---|---|",
        "| 1 | titre, statut, auteur, lectures, pièces | candidat 2 | candidat 3, même rédacteur, couples appliqués par "
        "script ; état des préalables ; « Lu », « Non lu », auteur ; pièces citées et neuves ; cette table | demande "
        "de la mère | C3-01 à C3-08 |",
        "| 2 | `CHAINE_P3BIS`, point (a) | quinze fichiers au commit du code | douze au commit du code ; les trois bancs "
        f"au commit de correction `68ded698` (au commit du code : {anciens_bancs}) ; rapport et contre-lecture des "
        "bancs cités | R-2367, R-2373, R-2374 | C3-09 |",
        "| 3 | règle d'épinglage (b), ligne P-5, ligne `CHAINE_P3BIS` de « Marqueurs restants » | deux fichiers "
        "épinglés, treize autres égaux au commit du code ; branche non nommée (`scellement/p3bis-v1` à l'en-tête) | "
        "branche `scellement/p3bis-v2` (v1 abandonnée, `a3116ff5`) ; deux fichiers épinglés, trois bancs égaux au "
        "commit de correction, dix au commit du code ; compagnons des cinq fichiers changés réécrits | R-2360, R-2367 "
        "| C3-10, C3-11, C3-12, C3-14, C3-15 |",
        "| 4 | rapports attendus | neuf | onze : contre-lecture courte des bancs (`df732d18…`) et relecture courte du "
        "candidat 2 (`c559f2c8…`) en plus | R-2358, R-2374 | C3-10, C3-13, C3-16 |",
        "| 5 | marqueurs | aucun | aucun | — | C3-17 |",
        "| 6 | date tenue (P-11) | mot de Lazar, R-2352 | inchangée | R-2352 | — |",
        "",
        para("**Sections gelées** : aucun couple C3 n'en touche une ; les sept sections gelées sont égales à l'octet à "
             "celles du candidat 2 (contrôlé par programme : journal du candidat 3). Défaire les couples C3, dans "
             "l'ordre inverse, redonne le candidat 2 à l'octet (journal).", "", ""),
        "",
        "## Table « ce qui change du candidat 1 au candidat 2 »",
        ""])
    couple(8, "table neuve, en tête des tables (non gelée)", "demande de la mère", "table « du candidat 2 au candidat 3 »",
           "## Table « ce qui change du candidat 1 au candidat 2 »\n", table)

    # (a) et (b) du point 6 : les blocs du candidat 2, pris tels quels dans son texte
    i_a = t2.index("   - (a) **chaîne v2 au commit du code**")
    i_b = t2.index("   - (b) **règle d'épinglage** :")
    i_c = t2.index("   - (c) **journaux canoniques**")
    ancien_a, ancien_b = t2[i_a:i_b], t2[i_b:i_c]
    nouveau_a = para(
        f"- (a) **chaîne v2** : douze fichiers **au commit du code** {bt(CODE)}, empreintes recalculées par `git show` "
        f"à ce commit, chacune égale à son compagnon au même commit : {l_douze} ; **candidat 3** (R-2367, R-2373, "
        "R-2374) : les trois bancs qui ne savaient jouer que contre des contrôles non épinglés, corrigés sur place, "
        f"sous les mêmes noms, au **commit de correction** {bt(CORR)} (branche `prep/p3bis-bancs-epingles-v1`, partie "
        "du commit du code ; seuls ces trois fichiers et leurs compagnons y changent), empreintes recalculées par `git "
        f"show` à ce commit, chacune égale à son compagnon au même commit : {l_bancs} (au commit du code : "
        f"{anciens_bancs}) ; rapport du développeur {bt(RAPPORT_BANCS)} ({bt(EMP[RAPPORT_BANCS])}) ; contre-lecture "
        f"courte {bt(CL_BANCS)} ({bt(EMP[CL_BANCS])}), Claude Fable 5.2 : « citable au scellement : commit "
        "`68ded698` » ;", I3, I3 + "  ") + "\n"
    nouveau_b = para(
        "- (b) **règle d'épinglage** (candidat 3 : R-2360, R-2367) : sur la branche de scellement "
        f"`scellement/p3bis-v2` (la v1, à `a3116ff5`, est abandonnée et gardée, R-2367), "
        "`controles_avant_depense_p3bis_v2.sh` et `recuperation_p3bis_v2.sh` ne diffèrent de leurs versions au commit "
        "du code **que** par leurs lignes `NOM=A_EPINGLER` (treize et une), remplies des valeurs que ce texte cite : "
        "code relu (`CODE_RELU`, le commit du code ci-dessus et à l'en-tête) ; configuration relue et consignes relues "
        "(`CONFIG_RELUE`, `CONSIGNES_RELUES` et leurs chemins sous `brouillons/` : en-tête, ligne « Configuration de "
        "P3 ») ; sortie de l'essai de fermeture (`ESSAI_FERMETURE` et son chemin : plan, point 6, sortie v3 jouée au "
        "commit du code) ; longueurs attendues (`LONGUEURS_ATTENDUES` et son chemin : plan, point 2) ; rapports "
        "attendus (`RAPPORTS_ATTENDUS` : les paires chemin=empreinte des rapports de contre-lecture et de relecture de "
        "P3-bis, de son code et de sa chaîne que ce texte cite par leur chemin et leur empreinte entière, la "
        f"contre-lecture 4 comprise, soit onze : {l_rapports}) ; chemin du candidat relu (`CANDIDAT_RELU_CHEMIN`, "
        f"{bt(C3)}) ; sauf `CANDIDAT_RELU`, empreinte de ce texte, qu'il ne peut citer, et `PY` (contrôles et "
        "récupération), interpréteur de l'environnement de P-1 de la session qui scelle, écrit au registre des "
        "décisions. Les trois bancs y sont égaux à l'octet à leurs versions au commit de correction `68ded698` ; les "
        "dix autres fichiers de la chaîne, à leurs versions au commit du code (l'étape 5 de `sceller_p3bis_v2.sh` "
        "compare les quinze à leurs copies versées) ; les compagnons des cinq fichiers changés depuis le commit du code "
        "(les deux épinglés, les trois bancs) sont à la forme de `scellement.sceller` (`<sha256>  <nom>` et fin de "
        "ligne ; ceux des deux épinglés réécrits, R-2360). Vérification par programme avant S, constatée au registre : "
        "`git diff` des quinze fichiers et de leurs compagnons entre le commit de correction (qui porte le commit du "
        "code et les trois bancs) et la branche de scellement ne montre que ces quatorze lignes, aux valeurs citées, et "
        "les compagnons des deux fichiers épinglés ;", I3, I3 + "  ") + "\n"
    couple(9, "Ce que le code et la chaîne doivent changer, point 6, (a) (non gelée)", "R-2367, R-2373, R-2374",
           "trois bancs au commit de correction ; douze fichiers au commit du code", ancien_a, nouveau_a)
    couple(10, "Ce que le code et la chaîne doivent changer, point 6, (b) (non gelée)", "R-2360, R-2367 ; demande",
           "branche v2 ; bancs égaux à 68ded698 ; compagnons ; onze rapports ; chemin du candidat 3", ancien_b, nouveau_b)

    couple(11, "Ce que le code et la chaîne doivent changer, point 6 (non gelée)", "R-2367",
           "le marqueur cite trois bancs au commit de correction",
           "(constat de P-6).\n",
           "(constat de P-6).\n" + para("Candidat 3 (R-2367) : les trois bancs corrigés sont cités au commit de "
                                         "correction `68ded698`, les douze autres fichiers au commit du code (point "
                                         "(a)).", I3, I3) + "\n")

    couple(12, "Préalables, P-5 (non gelée)", "R-2360, R-2367",
           "branche v2, bancs, compagnons ; vérification de la règle",
           "aux valeurs citées (par programme, constaté au registre) |",
           "aux valeurs citées (par programme, constaté au registre) ; candidat 3 (R-2360, R-2367) : branche de "
           "scellement `scellement/p3bis-v2` (la v1, à `a3116ff5`, abandonnée et gardée) ; les trois bancs y sont égaux "
           "à leurs versions au commit de correction `68ded698`, les dix autres fichiers à leurs versions au commit du "
           "code, les compagnons des cinq fichiers changés à la forme de `scellement.sceller` ; `git diff` des quinze "
           "fichiers et de leurs compagnons entre `68ded698` et la branche : ces quatorze lignes et les compagnons des "
           "deux fichiers épinglés seulement |")

    rel2 = para(
        "**Candidat 3** (R-2358) : relecture courte de l'écart du candidat 1 au candidat 2 faite : relecteur neuf "
        "**Claude Fable 5.2**, sans lecture de T0.7 ; texte relu, le candidat 2 "
        f"{bt(C2)} ({bt(EMP[C2])}) ; rapport {bt(REL2)} ({bt(EMP[REL2])}) ; verdict **« relu, conforme »** (candidat 1 "
        "plus les vingt-deux couples v3, à l'octet ; six sections gelées égales, « Plan d'analyse » égal au candidat 1 "
        "plus N-1 seul ; aucun marqueur ; circularité levée) ; notes N-1 à N-3, dont N-2 (le contrôle de la règle (b) "
        "compte aussi les compagnons re-scellés), portée à la règle (b) du candidat 3. **Écart du candidat 2 au "
        "candidat 3** (couples C3, tous hors des sections gelées) : contrôlé par programme (journal du candidat 3) et "
        "relu par un relecteur neuf, consigné au registre des décisions ; il ne peut être cité ici, pour la même raison "
        "que l'empreinte du candidat ; l'épingle `CANDIDAT_RELU` est l'empreinte de ce texte, au chemin "
        f"{bt(C3)}.", "  ", "  ")
    couple(13, "Contre-lecture, relecture courte (non gelée)", "R-2358 ; demande",
           "relecture courte du candidat 2 citée ; écart du candidat 2 au candidat 3 au registre",
           "au texte de S.\n\n## Marqueurs restants", "au texte de S.\n" + rel2 + "\n\n## Marqueurs restants")

    couple(14, "Marqueurs restants, ligne CHAINE_P3BIS (non gelée)", "R-2367", "mise à jour au candidat 3",
           "| `CHAINE_P3BIS` — **rempli au candidat 2** (« Ce que le code et la chaîne doivent changer », point 6 ; "
           "R-2345) ;",
           "| `CHAINE_P3BIS` — **rempli au candidat 2** (« Ce que le code et la chaîne doivent changer », point 6 ; "
           "R-2345), **mis à jour au candidat 3** (R-2367) ;")
    couple(15, "Marqueurs restants, ligne CHAINE_P3BIS (non gelée)", "R-2360, R-2367", "définition au candidat 3",
           "| **candidat 2 (R-2345 ; la définition du candidat 1",
           "| **candidat 3 (R-2367)** : comme au candidat 2, sauf (a) les trois bancs corrigés cités au commit de "
           "correction `68ded698`, les douze autres fichiers au commit du code, et (b) sur la branche de scellement "
           "`scellement/p3bis-v2`, les trois bancs égaux à leurs versions au commit de correction, les dix autres "
           "fichiers au commit du code, les compagnons des cinq fichiers changés à la forme de `scellement.sceller` "
           "(R-2360) ; **candidat 2 (R-2345 ; la définition du candidat 1")
    couple(16, "Marqueurs restants, ligne CANDIDAT_RELU (non gelée)", "R-2358",
           "relecture du candidat 2 ; chemin du candidat 3",
           "écart du candidat 1 au candidat 2 au registre des décisions, R-2345) |",
           "écart du candidat 1 au candidat 2 au registre des décisions, R-2345 ; candidat 3 : relecture courte du "
           "candidat 2, `c559f2c8…`, « relu, conforme », R-2358 ; écart du candidat 2 au candidat 3 au registre ; "
           "chemin épinglé, celui du candidat 3) |")
    couple(17, "Marqueurs restants (non gelée)", "demande de la mère", "aucun marqueur au candidat 3",
           "Candidat 2 : **aucun marqueur**",
           "Candidat 3 : **aucun marqueur** (« Ce que le code et la chaîne doivent changer », point 6 : `CHAINE_P3BIS` "
           "mis à jour, R-2367).\nCandidat 2 : **aucun marqueur**")
    return c


def appliquer(texte: str, couples: list) -> str:
    for x in couples:
        n = texte.count(x["ancien"])
        if n != 1:
            raise SystemExit(f"{x['id']} : « ancien » trouvé {n} fois")
        texte = texte.replace(x["ancien"], x["nouveau"], 1)
    return texte


def main(argv: list) -> int:
    if len(argv) != 3 or not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", argv[2]):
        print("usage : DOSSIER_DE_SORTIE AAAA-MM-JJTHH:MM:SSZ", file=sys.stderr)
        return 2
    sortie, heure = Path(argv[1]), argv[2]
    cibles = [sortie / NOM_COUPLES, sortie / NOM_EPINGLES, sortie / NOM_JOURNAL]
    if any(p.exists() or Path(str(p) + ".sha256").exists() for p in cibles):
        raise SystemExit("une sortie existe déjà (R12)")
    journal = [f"Construction des couples C3 et des épingles proposées v2, {heure} (heure passée en argument, `date -u`)"]
    etat = controles(journal)
    t2 = Path(C2).read_text(encoding="utf-8")
    couples = couples_c3(t2)
    if re.search(r"<<[A-Z0-9_]+>>", "".join(x["nouveau"] for x in couples)):
        raise SystemExit("marqueur dans un « nouveau »")
    t3 = appliquer(t2, couples)
    plat = " ".join(t3.split())
    for s in BANCS:
        if CHAINE_CODE[s] in t3:
            raise SystemExit(f"empreinte entière de {s} au commit du code restée dans le texte")
    cites = [f"`{CHAINE}/{s}` (`{BANCS.get(s, e)}`" for s, e in CHAINE_CODE.items()]
    cites += [CODE, CORR, CFG_RELUE[1], f"`{CFG_RELUE[0]}`", CONS_RELUES[1], f"`{CONS_RELUES[0]}`",
              f"`{ESSAI[0]}` (`{ESSAI[1]}`", f"`{LONGUEURS[0]}` (`{LONGUEURS[1]}`", f"`{C3}`",
              "`scellement/p3bis-v2`"]
    cites += [f"`{f}`" for f, _, _ in RAPPORTS] + [e for _, e, _ in RAPPORTS]
    manque = [x for x in cites if x not in plat]
    if manque:
        raise SystemExit(f"non cité par le texte : {manque}")
    journal.append(f"{len(couples)} couples, chacun trouvé une fois ; texte : {h(t3.encode())}")
    journal.append(f"chaque valeur proposée et chaque fichier de la chaîne cités par le texte ({len(cites)} formes)")
    rapports = " ".join(f"{f}={e}" for f, e, _ in RAPPORTS)
    if not all(re.fullmatch(r"[a-zA-Z0-9_./-]+\.(md|json)=[0-9a-f]{64}", p) for p in rapports.split()) \
            or len(rapports.split()) != 11:
        raise SystemExit("RAPPORTS_ATTENDUS mal formé")
    ctl = git("show", f"{CODE}:{CHAINE}/controles_avant_depense_p3bis_v2.sh").decode()
    valeurs = {"CANDIDAT_RELU_CHEMIN": C3, "CONFIG_RELUE": CFG_RELUE[1], "CONFIG_RELUE_CHEMIN": CFG_RELUE[0],
               "CONSIGNES_RELUES": CONS_RELUES[1], "CONSIGNES_RELUES_CHEMIN": CONS_RELUES[0], "CODE_RELU": CODE,
               "ESSAI_FERMETURE": ESSAI[1], "ESSAI_FERMETURE_CHEMIN": ESSAI[0], "LONGUEURS_ATTENDUES": LONGUEURS[1],
               "LONGUEURS_ATTENDUES_CHEMIN": LONGUEURS[0], "RAPPORTS_ATTENDUS": rapports}
    lignes = {}
    for nom, v in valeurs.items():
        m = re.search(rf"^{nom}=A_EPINGLER(.*)$", ctl, re.M)
        lignes[nom] = {"ligne_au_commit_du_code": m.group(0),
                       "ligne_proposee": f"{nom}={chr(34) + v + chr(34) if ' ' in v else v}{m.group(1)}"}
    a_verser = [{"chemin": x["chemin"], "empreinte": x["empreinte"], "commit_ou_la_prendre": x["commit_ou_la_prendre"],
                 "avec_compagnon": True, "role": x["role"], "presence": x["presence"]} for x in etat["pieces"]]
    a_verser.append({"chemin": C3, "empreinte": "celle du candidat 3 écrit par le script au lancement (journal)",
                     "commit_ou_la_prendre": "commit de la session mère qui le verse (à venir)", "avec_compagnon": True,
                     "role": "CANDIDAT_RELU, CANDIDAT_RELU_CHEMIN", "presence": "à venir"})
    epingles = {
        "titre": "P3-bis : épingles proposées des contrôles avant dépense et de la récupération (chaîne v2), v2",
        "ecrit": heure, "redacteur": "Claude Opus 5.5 (claude-opus-5-5), rédacteur des candidats 2 et 3",
        "decisions": "R-2367, R-2373, R-2374 (main, commit 883a2432)",
        "remplace": f"{EPINGLES_V1} ({EMP[EPINGLES_V1]}), gardée telle quelle (R12)",
        "commit_du_code": CODE, "commit_de_correction_des_bancs": CORR,
        "branche_de_scellement": {"nom": "scellement/p3bis-v2", "v1_abandonnee": TETE_V1},
        "main_au_moment_de_la_verification": etat["main"],
        "regle": ("sur scellement/p3bis-v2 : controles_avant_depense_p3bis_v2.sh et recuperation_p3bis_v2.sh ne "
                  "diffèrent de leurs versions au commit du code que par leurs lignes NOM=A_EPINGLER (treize et une) ; "
                  "les trois bancs sont égaux à leurs versions au commit de correction 68ded698 ; les dix autres "
                  "fichiers à leurs versions au commit du code ; compagnons des cinq fichiers changés à la forme de "
                  "scellement.sceller (R-2360, R-2367) ; git diff des quinze fichiers et compagnons entre 68ded698 et "
                  "la branche : ces quatorze lignes et les compagnons des deux fichiers épinglés seulement"),
        "epingles_controles": {
            "CANDIDAT_RELU": "non proposée : empreinte du candidat 3 écrit par le script de la session mère (journal) ; "
                             "le texte ne peut la citer",
            **valeurs,
            "PY": "non proposée : interpréteur de l'environnement de P-1 de la session qui scelle, écrit au registre"},
        "epingles_recuperation": {"PY": "non proposée : la même que celle des contrôles"},
        "lignes": lignes,
        "rapports_attendus": [{"chemin": f, "empreinte": e, "objet": o} for f, e, o in RAPPORTS],
        "pieces_a_verser": a_verser,
        "note_pieces": ("chaque pièce vérifiée (fichier et compagnon égaux) au commit indiqué : main pour les "
                        "brouillons et le dossier docs/notes/g0-deux-semaines-v1/p3bis-regle-plancher-v1 ; dfb1ed7b "
                        "pour les longueurs attendues ; 68ded698 pour les trois bancs ; « presence » dit si d0d9fcb8 "
                        "(P-3, P-10), a3116ff5 (tête de la v1) et 68ded698 la portent déjà à l'empreinte voulue. Hors "
                        "épingles, le texte cite aussi le rapport du développeur des bancs (a4020e30…, sur main) ; la "
                        "chaîne épinglée et les sept journaux canoniques (P-5, P-6) viennent après ce texte."),
    }
    sortie.mkdir(parents=True, exist_ok=True)
    brut = json.dumps(couples, ensure_ascii=False, indent=1) + "\n"
    (sortie / NOM_COUPLES).write_text(brut, encoding="utf-8")
    (sortie / NOM_EPINGLES).write_text(json.dumps(epingles, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    journal.append(f"couples : {h(brut.encode())}")
    journal.append(f"épingles proposées v2 : {h((sortie / NOM_EPINGLES).read_bytes())}")
    journal.append(f"pièces à verser : {len(a_verser)}")
    journal.append("CONSTRUCTION : CONFORME")
    (sortie / NOM_JOURNAL).write_text("\n".join(journal) + "\n", encoding="utf-8")
    print("\n".join(journal))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
