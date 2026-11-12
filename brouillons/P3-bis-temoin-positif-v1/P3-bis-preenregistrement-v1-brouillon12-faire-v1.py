"""Brouillon 12 du préenregistrement de P3-bis : brouillon 11 + couples CL4-C01 à CL4-C17 de la contre-lecture 4, tels
qu'écrits, + couples B12-01 à B12-23 du rédacteur (état des bloquants de procédure, en-tête, marqueurs ; tous hors des
sections gelées). Écrit par un rédacteur neuf, sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, le
10 novembre 2026, sur la consigne
`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-redaction-p3bis-brouillon12-v1.md`
(`e7917bb9…`). Méthode du brouillon 11 (`…-brouillon11-faire-v1.py`, `1015bd16…`), reprise sous un nom neuf.

Chaque « ancien » doit apparaître exactement une fois dans le texte en cours d'application, sinon arrêt sans rien écrire
(R5) ; la sortie et le journal ne doivent pas exister (R12). Les dix-sept couples de la contre-lecture 4 sont relus dans
son rapport (empreinte vérifiée) et doivent être égaux, à l'octet, à ceux du fichier des couples. Le journal consigne :
empreintes des entrées, des couples et de ce script ; chaque couple ; comparaison programmée de chaque section gelée au
brouillon 11 (et écarts, en différence de lignes) ; chaque couple gelé appliqué seul ; contrôle que les couples non gelés
ne touchent aucune section gelée ; marqueurs ; formes que la chaîne de session lit dans le texte ; module commun `go` et
`valeurs` de la chaîne (commit `614fd5da`) et `lire_go` de la garde de calcul, joués sur le texte et sur le registre des
GO (cas sain et artefact) ; état des bloquants de procédure recalculé par `git` en lecture seule ; `problemes()` ;
écarts du rédacteur et questions pour la mère. Aucun appel externe, aucune écriture git ; les fichiers temporaires vont
dans `TMPDIR` (le bac à sable du rédacteur), effacés à la fin ; rien d'autre n'est écrit.

Usage, depuis la racine du dépôt, `TMPDIR` pointant le bac à sable :
  PYTHONPATH=src python <ce script> "$(date -u +%Y-%m-%dT%H:%M:%SZ)"               # écrit le brouillon 12 et le journal
  PYTHONPATH=src python <ce script> --essai COUPLES.json "$(date -u +…)"           # rien d'écrit dans le dépôt
L'heure passée en argument est relevée par `date -u` (règle des heures)."""
import contextlib
import difflib
import hashlib
import io
import json
import re
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

from controle_ia.prereg import problemes, sections
from controle_ia.scellement import verifier_arbre

DOSSIER = Path("brouillons/P3-bis-temoin-positif-v1")
ENTREE = DOSSIER / "P3-bis-preenregistrement-v1-brouillon11.md"
RAPPORT_CL4 = DOSSIER / "contre-lecture-4-brouillon11-v1.md"
SORTIE = DOSSIER / "P3-bis-preenregistrement-v1-brouillon12.md"
COUPLES = DOSSIER / "P3-bis-preenregistrement-v1-brouillon12-couples-v1.json"
JOURNAL = DOSSIER / "P3-bis-preenregistrement-v1-brouillon12-journal-v1.md"
EMPREINTE_ENTREE = "409c37ed4aa4f149565d8b0a45ae94c16b572f35967f080a0df629985549b290"
EMPREINTE_CL4 = "90847ae2d017c6e100a15cf80ecee17645a4c71ecd33197187767cc2ff9d2c13"
EMPREINTE_COUPLES = "a8a93037558af52f9ffb7f72906673460b4b251778f1c05d25cf38ee6efe6850"
GELEES = ("Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Plan d'analyse",
          "Critères de lecture gelés", "Liste d'arrêt")
GELEES_ATTENDUES = {"CL4-C05": "Plan d'analyse", "CL4-C07": "Liste d'arrêt", "CL4-C08": "Plan d'analyse",
                    "CL4-C09": "Liste d'arrêt", "CL4-C10": "Plan d'analyse"}
INCHANGEES = ("Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Critères de lecture gelés")
SECTION_NEUVE = "Table « ce qui change du 11 au 12 »"
MARQUEURS_ATTENDUS = {"CANDIDAT_RELU", "CHAINE_P3BIS", "EMPREINTE_CONFIG_P3BIS", "EMPREINTE_CONSIGNES_P3BIS",
                      "LONGUEURS_P3BIS", "TESTS_ATTENDUS_P3BIS"}
MARQUEURS_REMPLIS = ("CONTRE_LECTURE_4_P3BIS", "COMMIT_CODE_P3BIS", "IDENTITE_CODE_P3BIS", "EMPREINTES_CODE_P3BIS",
                     "PIECES_SUR_MAIN_P3BIS", "ESSAI_FERMETURE_P3BIS")
# --- commits lus (lecture seule) ----------------------------------------------------------------------------------------
CODE = "a1de39151ebae29138a389829751397074239615"          # commit du code cité (R-2113, contre-lu R-2158)
CHAINE = "614fd5da4d63b3849f40d5dbf320ccb50d1a1330"        # tête de prep/p3bis-lanceur-v1 (CL4-11)
ESSAI_COMMIT = "8ad2927313570c743925d11518f4c4a83e0e715d"  # commit qui verse la sortie v3 et le rejeu de concordance
MAIN = "62a91e64b31ebcf78035bebd43c1505f12a20ed1"          # main à la rédaction ; renommage de l'orpheline (R-2233)
GO_COMMIT = "cbc9c5ce589f6b07aac26bd313ca581cadc5db42"     # dernier commit qui change registres/go.md (R-2198 puis R-2206)
GO_AVANT = "7e4ca090557169e898a091adbbee02490d84765f"      # registre à six colonnes sur trois lignes (CL4-07 : artefact)
GO_LU_B11 = ("709a84fcc899dad0460285d027a8c81425b0279c", "e682abb0db3a0da37c0d764a7c659f638d449df266f6c9580d3ec481c8d44155")
REF_CHAINE = "refs/remotes/origin/prep/p3bis-lanceur-v1"
GO_CALCUL = "GO-2026-11-10-02"
DEPOT_URL = "https://github.com/lciric/controle-ia-travail.git"
MOTIF_GO = r"GO-\d{4}-\d{2}-\d{2}-\d{2}"
VALEURS_TEXTE = (   # recopiées du script du brouillon 11 (formes du module commun `valeurs`, commit 614fd5da)
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
ESSAI_CHEMIN = "brouillons/P3-bis-temoin-positif-v1/essai-fermeture-p3bis-v2-sortie-v3.txt"
ESSAI_EMPREINTE = "57d3467c7b7d700932da64ac449ca6a6dd9aed9fda1eee64d88c79f531382c78"
REJEU_CHEMIN = "brouillons/P3-bis-temoin-positif-v1/concordance-journal-rejeu-v1/sortie-rejeu-a1de3915-v1.txt"
REJEU_EMPREINTE = "3e2fada31983e82c1b90aed64bc210b24e292a9de3182f6d847b1e3fb13a37b4"
INSTANCE = {"scripts/amorce_instance_p3bis_v2.sh": "b331e44f763f87744b9669998c8a7aa32308e449d07ba414e6c2bb0bc4ed22f4",
            "scripts/p3bis_instance_v2.sh": "83820dfd8ef7205c44f89e63450d801d60b95eddecb504cd2af992fa5b1eaa5d"}
CL_COURTE = ("brouillons/P3-bis-temoin-positif-v1/contre-lecture-differentielle-code-a1de3915-v1.md",
             "845c4de54e72207a320edf089c606bacf0cd87837d473ab654de48c3ddc839c9")
ORPH_DOSSIER = "docs/notes/ideation-organisme-v1/question-mere-reponses"
ORPH_ANCIEN = f"{ORPH_DOSSIER}/consigne-argon-question-mere-v3.txt.sha256"
ORPH_NEUF = f"{ORPH_DOSSIER}/consigne-argon-question-mere-v3-empreinte-orpheline-v1.txt"
ORPH_CONTENU = "cb810c6e1d65e342223fbb4e531345204801fc4d34018a99a1b0aa3099f08452"
CHEMINS_GELES = (".", ":(exclude)prereg", ":(exclude)brouillons", ":(exclude)registres", ":(exclude)docs",
                 ":(exclude)diag", ":(exclude)runs", ":(exclude)donnees", ":(exclude)livrables", ":(exclude)papiers",
                 ":(exclude)traces", ":(exclude)CLAUDE.md")
EN_TETE_CL4 = re.compile(r"^\*\*(CL4-C\d{2})\*\* — (GELÉE : (.+?)|non gelée) — (.+?) — constat (CL4-\d{2})$", re.M)
BLOC_CL4 = re.compile(r"\A\n\nancien :\n\n~~~\n(.*?)\n~~~\n\nnouveau :\n\n~~~\n(.*?)\n~~~\n", re.S)

ECARTS_ET_QUESTIONS = """## Écarts du rédacteur, déclarés

- **E-1 — marqueur `CONTRE_LECTURE_4_P3BIS` rempli par le rédacteur** (B12-19). La consigne le demande « si la consigne de
  ce marqueur le permet ». Sa ligne de table nomme ce qui le remplit (contre-lecteur, empreinte du texte relu, chemin et
  empreinte du rapport, traitement de chaque remarque), « avant le scellement », par « contre-lecteur neuf ; session
  mère » ; l'entrée dit « peut être faite sur le candidat ». Toutes les pièces existent et sont vérifiées ici (rapport
  `90847ae2…`, brouillon relu `409c37ed…`) ; le texte reprend celui que propose la contre-lecture 4 (« à adapter par la
  mère »), avec sa limite (CL4-12). Lu comme permis, puisque la mère l'ordonne : question Q-1.
- **E-2 — marqueur `CANDIDAT_RELU` neuf** (B12-20, B12-23). Il n'existait pas au brouillon 11 : `CANDIDAT_RELU` y est
  l'épingle de la chaîne (P-5). La consigne demande de le garder « une occurrence » ; il est donc écrit comme marqueur
  du texte, rempli au candidat par la relecture courte de l'écart du brouillon 11 au candidat (rapport et empreinte de
  départ), **jamais par l'empreinte du candidat lui-même** (un texte ne peut pas citer sa propre empreinte ; elle reste
  l'épingle). Question Q-2.
- **E-3 — P-10, « porter ce commit »** (B12-13). R-2233 dit que la branche de scellement « doit porter ce commit avant
  S ». `62a91e64` ne peut pas devenir ancêtre de la branche par une fusion de `main` sans changer l'arbre gelé depuis
  `a1de3915` (contrôle ci-dessus), ce que P-3 interdit ; le texte écrit donc que la branche porte le **renommage** (les
  deux chemins de `docs/` de `62a91e64`), comme P-3 porte `registres/go.md`. Question Q-3.
- **E-4 — préalable neuf P-11** (B12-14, B12-16, B12-18) pour CL4-13 (« écris-le » de la consigne) : hors des sections
  gelées ; le plan, point 8 (gelé), dit déjà qu'un mot de Lazar avant le scellement qui change la date fait une version
  neuve.
- **E-5 — « Lu » du brouillon 11 touché** (B12-05) : seule la citation du registre des GO change de forme (commit
  `709a84fc` ajouté, empreinte `e682abb0…` gardée), pour CL4-16 ; le commit est le seul état du registre à cette
  empreinte (contrôle ci-dessus).
- **E-6 — CL4-15 non porté** : la contre-lecture n'a écrit aucun couple (« une phrase au candidat, ou rien »).
  Question Q-4.
- **E-7 — non vérifié par ce rédacteur** : `verifier-arbre` sur toute l'extraction de la branche de scellement (il
  hacherait des fichiers de T0.7, interdits à ce rédacteur) ; seul le dossier de l'empreinte orpheline est vérifié ici.
  La vérification reste celle de P-10, par la mère.
- **E-8 — brouillon 11 lu en partie** (lignes citées au « Lu » du brouillon 12) : les sections que touchent les couples
  et leurs contextes, l'en-tête, les tables, les préalables, le devis, les décisions, la contre-lecture et les
  marqueurs ; le reste est comparé par programme (sections gelées égales à l'octet, couples non gelés hors d'elles).
- **E-9 — gestes déclarés** au « Non lu » du brouillon 12 (`git status`, `git ls-tree` limités, `git archive` d'un
  dossier dans le bac à sable, un `git diff --shortstat` de l'arbre gelé, nombres seuls). Le script a d'abord été joué
  en mode `--essai` dans le bac à sable (rien d'écrit dans le dépôt), puis une fois pour de bon. **Aucun refus de
  permissions ni de classifieur.**
- **E-10 — barre verticale dans une cellule de table, venue de CL4-C13** (appliqué tel qu'écrit) : le « nouveau »
  porte « « | GO-… » » dans la colonne « vérification » de P-3 ; en Markdown, cette barre ouvre une cellule de plus et
  décale l'affichage de la ligne P-3 (le texte est intact, aucune forme lue par la chaîne n'est touchée). Question Q-7.

## Questions pour la mère (avec recommandation)

- **Q-1 — `CONTRE_LECTURE_4_P3BIS` rempli au brouillon 12.** Enjeu : qui remplit l'entrée de R2. Options : (a) garder
  le remplissage (pièces vérifiables, texte proposé par la contre-lecture ; la relecture courte du candidat le
  confirme) ; (b) le retirer et le remplir toi-même au candidat (une version neuve de plus). Recommandation : (a),
  confiance 0,8.
- **Q-2 — `CANDIDAT_RELU` comme marqueur du texte.** Enjeu : la consigne nomme une épingle de la chaîne parmi les
  marqueurs. Options : (a) marqueur gardé, rempli au candidat par le rapport de la relecture courte (chemin, empreinte)
  et l'empreinte du brouillon de départ, l'empreinte du candidat restant l'épingle ; (b) pas de marqueur, l'épingle
  seule (le texte ne dirait pas qui a relu l'écart). Recommandation : (a), confiance 0,7.
- **Q-3 — P-10 : comment la branche de scellement « porte » `62a91e64`.** Options : (a) un commit de la branche qui
  reprend les deux chemins de `docs/` de `62a91e64` (renommage et compagnon neuf), rien de l'arbre gelé, vérifié par
  `verifier-arbre` sur l'extraction ; (b) fusion de `main` : refusée par P-3 (arbre gelé changé) ; (c) fusion « ours »
  qui rend `62a91e64` ancêtre sans en prendre l'arbre : ne porte pas le renommage, donc ne lève rien. Recommandation :
  (a), confiance 0,85 ; si tu tiens à la lettre « ce commit », dis-le et le texte changera.
- **Q-4 — CL4-15** (`ouvrir --date-paquet` fixée par l'appelant, ne commande que la réserve « écrit après la lecture
  fermée »). Options : (a) rien ; (b) une phrase au candidat, « Ce que le code et la chaîne doivent changer », point 2
  (c). Recommandation : (b) au candidat, sans effet sur l'issue, confiance 0,6 ; (a) acceptable.
- **Q-5 — CL4-06 et machine des préalables.** P-1 (environnement `PY` sous Python 3.11) doit être construit sur la même
  machine que P-2 et P-6, puisque N se compte dans `PY` et que les contrôles l'épinglent (P-5). Recommandation : P-1, P-2,
  P-4, P-5 (épingle `PY`) et P-6 sur une seule machine qui a ≥ 12 692 612 ko libres, confiance 0,8.
- **Q-6 — revue de l'écart du 11 au 12 avant le candidat.** Les cinq couples gelés viennent tels quels de la contre-lecture
  4, mais les vingt-trois couples B12 ne sont relus par personne. Recommandation : les faire relire avec l'écart du
  candidat, en une seule relecture courte (marqueur `CANDIDAT_RELU`), plutôt qu'une contre-lecture 5 à part, confiance 0,7.
- **Q-7 — barre verticale de CL4-C13 (E-10).** Options : (a) un couple non gelé au candidat, « « | GO-… » » →
  « « \\| GO-… » » (barre échappée) ou « ligne de table de GO » ; (b) laisser (affichage seul). Recommandation : (a),
  confiance 0,7.
"""


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def git(*args: str) -> bytes:
    r = subprocess.run(["git", *args], capture_output=True)
    if r.returncode != 0:
        raise SystemExit(f"git {' '.join(args)[:120]} : code {r.returncode} ({r.stderr.decode('utf-8', 'replace').strip()[:200]})")
    return r.stdout


def git_code(*args: str) -> int:
    return subprocess.run(["git", *args], capture_output=True).returncode


def couples_du_rapport(rapport: str) -> list[dict]:
    r = rapport[rapport.index("## Liste exacte des couples"):]
    tetes = list(EN_TETE_CL4.finditer(r))
    sortie = []
    for k, m in enumerate(tetes):
        fin = tetes[k + 1].start() if k + 1 < len(tetes) else len(r)
        b = BLOC_CL4.match(r[m.end():fin])
        if not b:
            sys.exit(f"rapport de la contre-lecture 4 : {m.group(1)} illisible ; rien n'est écrit")
        sortie.append({"id": m.group(1), "section_gelee": m.group(3), "ancien": b.group(1), "nouveau": b.group(2)})
    return sortie


def appliquer(t: str, couples: list) -> tuple[str, list]:
    lignes = []
    for c in couples:
        n = t.count(c["ancien"])
        if n != 1:
            sys.exit(f"couple {c['id']} : ancien trouvé {n} fois (1 exigé) ; rien n'est écrit")
        t = t.replace(c["ancien"], c["nouveau"])
        g = c["section_gelee"]
        forme = "ajout pur" if c["ancien"] in c["nouveau"] else "remplacement"
        lignes.append(f"{c['id']}\t{'GELÉE : ' + g if g else 'non gelée'}\t{c['section']}\tancien 1 fois\t"
                      f"{len(c['ancien'])} → {len(c['nouveau'])} caractères\t{forme}\t{c['motif']}")
    return t, lignes


def plat(t: str) -> str:
    return re.sub(r" +", " ", t.replace("\n", " "))


def sans_gras(t: str) -> str:
    return " ".join(t.replace("**", "").split())


def nombres(t: str) -> list[str]:
    return re.findall(r"(?<![0-9a-f])\d+(?:[.,]\d+)?(?![0-9a-f])", t)


def controles_couples(couples: list, rapport: str) -> list[tuple[bool, str]]:
    r = []
    lus = couples_du_rapport(rapport)
    cl4 = [c for c in couples if c["id"].startswith("CL4-")]
    b12 = [c for c in couples if not c["id"].startswith("CL4-")]
    egaux = len(lus) == 17 and len(cl4) == 17 and all(
        a["id"] == b["id"] and a["ancien"] == b["ancien"] and a["nouveau"] == b["nouveau"]
        and a["section_gelee"] == b["section_gelee"] for a, b in zip(lus, cl4))
    r.append((egaux and [c["id"] for c in lus] == [f"CL4-C{i:02d}" for i in range(1, 18)],
              f"couples CL4-C01 à CL4-C17 du fichier : {len(cl4)}, égaux à l'octet (id, ancien, nouveau, section gelée) "
              f"aux {len(lus)} couples du rapport {RAPPORT_CL4}, dans le même ordre"))
    r.append((couples[:17] == cl4, "les dix-sept couples de la contre-lecture 4 sont appliqués d'abord, dans l'ordre du rapport"))
    gel = {c["id"]: c["section_gelee"] for c in couples if c["section_gelee"]}
    r.append((gel == GELEES_ATTENDUES, f"couples dans des sections gelées : {gel} (attendu : CL4-C05, C08, C10 au plan ; "
              "C07, C09 à la liste d'arrêt)"))
    ids = [c["id"] for c in b12]
    r.append((ids == [f"B12-{i:02d}" for i in range(1, len(b12) + 1)] and all(c["section_gelee"] is None for c in b12),
              f"couples du rédacteur : {len(b12)}, B12-01 à B12-{len(b12):02d}, tous hors des sections gelées"))
    return r


def controles_texte(t11: str, t12: str, couples: list) -> tuple[list[tuple[bool, str]], list[str]]:
    r, ecarts = [], []
    s11, s12 = sections(t11), sections(t12)
    declarees = {}
    for c in couples:
        if c["section_gelee"]:
            declarees.setdefault(c["section_gelee"], []).append(c["id"])
    for g in GELEES:
        egale = s11.get(g) == s12.get(g)
        d = declarees.get(g, [])
        if egale:
            r.append((not d and g in INCHANGEES, f"section gelée « {g} » : égale à l'octet au brouillon 11"
                      + (f" (mais couples déclarés {d})" if d else "")))
        else:
            r.append((bool(d) and g not in INCHANGEES,
                      f"section gelée « {g} » : modifiée par {', '.join(d) if d else 'AUCUN COUPLE DÉCLARÉ'}"))
            ecarts.append(f"### « {g} » (brouillon 11 → brouillon 12)\n\n```diff")
            ecarts += [x.rstrip("\n") for x in difflib.unified_diff(
                s11[g].splitlines(), s12[g].splitlines(), "brouillon 11", "brouillon 12", n=0, lineterm="")]
            ecarts.append("```\n")
    # chaque couple gelé appliqué seul au brouillon 11 ne change que sa section
    for c in couples:
        if not c["section_gelee"]:
            continue
        seul = sections(t11.replace(c["ancien"], c["nouveau"])) if t11.count(c["ancien"]) == 1 else {}
        changees = [x for x in set(s11) | set(seul) if s11.get(x) != seul.get(x)]
        n_a, n_n = nombres(c["ancien"]), nombres(c["nouveau"])
        neufs = [x for x in n_n if x not in n_a]
        r.append((changees == [c["section_gelee"]],
                  f"{c['id']} appliqué seul au brouillon 11 : sections changées {changees} ; nombres de l'ancien {n_a}, "
                  f"nombres ajoutés {neufs} (renvois : C-n, (n) ; aucun seuil)"))
    t_ng, _ = appliquer(t11, [c for c in couples if not c["section_gelee"]])
    sng = sections(t_ng)
    touchees = [g for g in GELEES if sng.get(g) != s11.get(g)]
    r.append((not touchees, "couples non gelés appliqués seuls : aucune section gelée touchée" if not touchees
              else f"couples non gelés qui touchent {touchees}"))
    neuves = [x for x in s12 if x not in s11]
    ordre = list(s12)
    r.append((neuves == [SECTION_NEUVE] and ordre.index(SECTION_NEUVE) + 1 == ordre.index("Table « ce qui change du 10 au 11 »"),
              f"section neuve (hors des sections gelées) : {neuves}, placée avant la table « du 10 au 11 »"))
    r.append((all(x in s12 for x in s11), "aucune section du brouillon 11 retirée"))
    # en-tête
    r.append((t12.split("\n", 1)[0].endswith("— v1 — brouillon 12") and t12.count("- Statut : **brouillon 12**") == 1
              and t12.count("- Statut du **brouillon 11**") == 1, "titre et statut : brouillon 12 ; statut du brouillon 11 gardé"))
    # marqueurs
    trouves = re.findall(r"<<([A-Z0-9_]+)>>", t12)
    compte = {m: trouves.count(m) for m in sorted(set(trouves))}
    r.append((set(compte) == MARQUEURS_ATTENDUS and all(v == 1 for v in compte.values()),
              f"marqueurs restants : {len(compte)} distincts, {compte}"))
    r.append((not any(f"<<{m}>>" in t12 for m in MARQUEURS_REMPLIS),
              f"marqueurs remplis, absents avec chevrons : {', '.join(MARQUEURS_REMPLIS)}"))
    statut = t12[:t12.index("- **Brouillon 12 = brouillon 11")]
    r.append((all(f"`{m}`" in statut for m in MARQUEURS_ATTENDUS), "les six marqueurs restants sont listés au statut"))
    # contre-lecture 4 remplie : les deux empreintes dans son entrée
    cl = s12["Contre-lecture"]
    e4 = cl[cl.index("- **Contre-lecture 4**"):]
    r.append((EMPREINTE_ENTREE in e4 and EMPREINTE_CL4 in e4 and "Claude Fable 5.2" in e4,
              "entrée « Contre-lecture 4 » : brouillon relu (409c37ed…) et rapport (90847ae2…) cités en entier, contre-lecteur nommé"))
    # formes lues par la chaîne (recopiées du script du brouillon 11)
    m = re.findall(rf"^- GO : \*\*({MOTIF_GO})\*\*", t12, re.M)
    r.append((m == [GO_CALCUL] and len(re.findall(r"^- GO :", t12, re.M)) == 1,
              f"chaîne, `go` : une seule ligne « - GO : **…** », {m}"))
    lanc = [x for x in t12.split("\n") if x.startswith("- Lancement : ")]
    ok = len(lanc) == 1 and re.findall(rf"`GO_ID=({MOTIF_GO})`", lanc[0]) == [GO_CALCUL] \
        and set(re.findall(MOTIF_GO, lanc[0])) == {GO_CALCUL}
    r.append((ok, f"chaîne, `go` : première ligne « - Lancement : » unique, seul GO cité {GO_CALCUL}"))
    r.append(("`PREREG=prereg/P3-bis-temoin-positif-v1.md`, `BRANCHE=calcul/p3bis-reel-v1`" in t12
              and f"`DEPOT_URL={DEPOT_URL}`" in t12, "chaîne, contrôles bloc 12 : PREREG, BRANCHE, DEPOT_URL"))
    sg = sans_gras(t12)
    manquantes = [v for v in VALEURS_TEXTE if v not in sg]
    r.append((not manquantes, f"chaîne, `valeurs` (copie locale) : {len(VALEURS_TEXTE) - len(manquantes)} sur {len(VALEURS_TEXTE)}"
              + (f" ; manquantes {manquantes}" if manquantes else "")))
    doubles = {x: t12.count(f"{x} : `") for x in INTITULES if t12.count(f"{x} : `") != 1}
    r.append((not doubles, "chaîne, contrôles bloc 12 : huit intitulés lus une fois chacun" + (f" ; {doubles}" if doubles else "")))
    cites = re.findall(r"Commit du code d'analyse : `([0-9a-f]{40})`", t12)
    r.append((cites == [CODE] and t12.count("Commit du code d'analyse : `") == 1,
              f"chaîne, contrôles bloc 2 : commit du code cité une fois, {cites}"))
    r.append((t12.count(f"Tâches de P3 : `{TACHES_SHA}`") == 1, "chaîne, contrôles bloc 4 : tâches citées une fois par leur empreinte"))
    p = plat(t12)
    r.append((f"`{ESSAI_CHEMIN}` (`{ESSAI_EMPREINTE}`" in p,
              "chaîne, contrôles bloc 6 : sortie v3 de l'essai de fermeture citée « `chemin` (`sha256` »"))
    for f, e in INSTANCE.items():
        r.append((f"`{f}` (`{e}`" in p, f"chaîne, contrôles bloc 11 : {f} cité « `chemin` (`sha256` »"))
    r.append((f"`{CL_COURTE[0]}` (`{CL_COURTE[1]}`" in p or f"`{CL_COURTE[0]}`, `{CL_COURTE[1]}`" in p,
              "contre-lecture différentielle courte citée par son chemin et son empreinte entière (CL4-01, RAPPORTS_ATTENDUS)"))
    return r, ecarts


def charger(source: str, nom: str, fichier: Path) -> dict:
    espace = {"__name__": nom, "__file__": str(fichier)}   # module relu par git show, jamais lancé comme programme
    exec(compile(source, nom, "exec"), espace)
    return espace


def jouer(f, *args) -> tuple[bool, object, str]:
    err = io.StringIO()
    try:
        with contextlib.redirect_stderr(err):
            v = f(*args)
        return True, v, str(v if v is not None else "")
    except SystemExit as e:
        return False, None, f"SystemExit({e.code}) {err.getvalue().strip()}".strip()


def controles_git(t12: str, tmp: Path) -> list[tuple[bool, str]]:
    r = []
    # pièces citées (CL4-01, contre-lecture 4)
    for chemin, e in ((str(RAPPORT_CL4), EMPREINTE_CL4), CL_COURTE):
        b = Path(chemin).read_bytes()
        comp = Path(chemin + ".sha256").read_text(encoding="utf-8").split()[0]
        r.append((sha(b) == e == comp and sha(git("show", f"{MAIN}:{chemin}")) == e,
                  f"{chemin} : {sha(b)[:12]}…, compagnon égal, même fichier sur main au commit {MAIN[:8]}"))
    # registre des GO (CL4-07, CL4-16)
    hist = git("log", "--format=%H", MAIN, "--", "registres/go.md").decode().split()
    etats = {c: sha(git("show", f"{c}:registres/go.md")) for c in hist}
    r.append((hist[0] == GO_COMMIT and etats[GO_COMMIT] == sha(git("show", f"{MAIN}:registres/go.md")),
              f"registres/go.md : dernier commit qui le change jusqu'à {MAIN[:8]} = {hist[0][:8]} ({etats[hist[0]][:12]}…, "
              f"égal à l'arbre de {MAIN[:8]}) ; {len(hist)} commits relus"))
    a_e682 = [c for c, e in etats.items() if e == GO_LU_B11[1]]
    r.append((a_e682 == [GO_LU_B11[0]], f"registre lu par le brouillon 11 ({GO_LU_B11[1][:8]}…) : seul état au commit {a_e682}"))
    verif = charger(git("show", f"{CHAINE}:docs/procedures/P3-bis-temoin-positif-v1/verifications_p3bis_v1.py").decode("utf-8"),
                    "verifications_p3bis_v1", tmp / "verifications_p3bis_v1.py")
    garde = charger(git("show", f"{MAIN}:.claude/hooks/garde_calcul.py").decode("utf-8"), "garde_calcul",
                    tmp / ".claude" / "hooks" / "garde_calcul.py")
    texte = tmp / "texte-brouillon12.md"
    texte.write_text(t12, encoding="utf-8")
    for nom, commit, attendu in (("sain", GO_COMMIT, True), ("artefact", GO_AVANT, False)):
        reg = tmp / f"go-{commit[:8]}.md"
        reg.write_bytes(git("show", f"{commit}:registres/go.md"))
        ok_go, _, msg_go = jouer(verif["go"], str(texte), str(reg), "2026-11-10")
        ok_g, d, msg_g = jouer(garde["lire_go"], reg)
        if ok_g:
            msg_g = f"{len(d)} identifiants ; {GO_CALCUL} {'présent' if GO_CALCUL in d else 'ABSENT'}"
            ok_g = GO_CALCUL in d
        r.append((ok_go == attendu and ok_g == attendu,
                  f"registre des GO au commit {commit[:8]} ({nom}) : module commun `go` (texte du brouillon 12, jour "
                  f"2026-11-10, jour de la rédaction) → {'conforme' if ok_go else 'refus'} « {msg_go.strip()[:300]} » ; "
                  f"garde de calcul `lire_go` → {'lu' if ok_g else 'refus'} « {msg_g.strip()[:300]} »"))
    ok_v, _, msg_v = jouer(verif["valeurs"], str(texte))
    r.append((ok_v, f"module commun `valeurs` (commit {CHAINE[:8]}) sur le texte du brouillon 12 : « {msg_v.strip()[:300]} »"))
    # empreinte orpheline (CL4-08, R-2233)
    attendu_ns = {f"R100\t{ORPH_ANCIEN}\t{ORPH_NEUF}", f"A\t{ORPH_NEUF}.sha256", "M\tregistres/decisions.md"}
    ns = set(git("show", "--name-status", "--format=", MAIN).decode().splitlines()) - {""}
    meme_objet = git("rev-parse", f"{CODE}:{ORPH_ANCIEN}") == git("rev-parse", f"{MAIN}:{ORPH_NEUF}")
    r.append((ns == attendu_ns and meme_objet and sha(git("show", f"{MAIN}:{ORPH_NEUF}")) == ORPH_CONTENU
              and git("show", f"{MAIN}:{ORPH_NEUF}.sha256").decode().split()[0] == ORPH_CONTENU,
              f"commit {MAIN[:8]} : renommage de l'empreinte orpheline, contenu gardé à l'octet ({ORPH_CONTENU[:8]}…), "
              "compagnon neuf égal ; seuls changements : le renommage, le compagnon, registres/decisions.md"))
    res = {}
    for commit in (CODE, MAIN):
        racine = tmp / f"arbre-{commit[:8]}"
        racine.mkdir()
        with tarfile.open(fileobj=io.BytesIO(git("archive", "--format=tar", commit, "--", ORPH_DOSSIER))) as tar:
            tar.extractall(racine, filter="data")
        res[commit] = [(c, m) for c, m in verifier_arbre(racine, dossiers=("docs",))]
    r.append((res[CODE] == [(ORPH_ANCIEN, "empreinte orpheline : le fichier scellé est absent")] and res[MAIN] == [],
              f"verifier_arbre sur le seul dossier {ORPH_DOSSIER} extrait par git archive : au commit {CODE[:8]} "
              f"(artefact) {res[CODE]} ; au commit {MAIN[:8]} (cas sain) {res[MAIN]}"))
    gele_differe = git_code("diff", "--quiet", "--no-renames", CODE, MAIN, "--", *CHEMINS_GELES)
    r.append((git_code("merge-base", "--is-ancestor", CODE, MAIN) == 1 and gele_differe == 1,
              f"{CODE[:8]} n'est pas ancêtre de {MAIN[:8]} et l'arbre gelé diffère entre eux (git diff --quiet --no-renames : "
              f"code {gele_differe}) : une fusion de main changerait l'arbre gelé de la branche de scellement (P-3, P-10)"))
    # branche de la chaîne (CL4-11)
    r.append((git("rev-parse", REF_CHAINE).decode().strip() == CHAINE
              and git_code("merge-base", "--is-ancestor", ESSAI_COMMIT, CHAINE) == 0
              and git_code("merge-base", "--is-ancestor", CODE, CHAINE) == 0,
              f"{REF_CHAINE} = {CHAINE[:8]} ; {ESSAI_COMMIT[:8]} et {CODE[:8]} en sont ancêtres"))
    b = git("show", f"{ESSAI_COMMIT}:{ESSAI_CHEMIN}")
    derniere = [x for x in b.decode("utf-8").split("\n") if x.strip()][-1]
    r.append((sha(b) == ESSAI_EMPREINTE == git("show", f"{ESSAI_COMMIT}:{ESSAI_CHEMIN}.sha256").decode().split()[0]
              and derniere == "ESSAI DIFFÉRENTIEL DE FERMETURE : CONFORME",
              f"sortie v3 de l'essai de fermeture ({ESSAI_COMMIT[:8]}) : {ESSAI_EMPREINTE[:8]}…, compagnon égal, dernière ligne « {derniere} »"))
    b = git("show", f"{ESSAI_COMMIT}:{REJEU_CHEMIN}")
    r.append((sha(b) == REJEU_EMPREINTE == git("show", f"{ESSAI_COMMIT}:{REJEU_CHEMIN}.sha256").decode().split()[0],
              f"sortie du rejeu de concordance ({ESSAI_COMMIT[:8]}) : {REJEU_EMPREINTE[:8]}…, compagnon égal (contenu non affiché)"))
    finale = git("show", f"{CHAINE}:docs/procedures/P3-bis-temoin-positif-v1/repetition_finale_p3bis_v1.sh").decode("utf-8")
    r.append((bool(re.search(r"^PLACE_MIN_KO=12692612\b", finale, re.M)) and "12 692 612 ko" in " ".join(t12.split()),
              f"PLACE_MIN_KO=12692612 à repetition_finale_p3bis_v1.sh ({CHAINE[:8]}), seuil cité au texte, inchangé"))
    r.append((git("rev-parse", "--verify", f"{CODE}^{{commit}}").decode().strip() == CODE, f"commit du code {CODE[:8]} présent"))
    return r


def main(argv: list[str]) -> int:
    essai = len(argv) == 4 and argv[1] == "--essai"
    if not essai and len(argv) != 2:
        sys.exit(__doc__)
    heure = argv[-1]
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", heure):
        sys.exit("heure attendue AAAA-MM-JJTHH:MM:SSZ, relevée par date -u")
    b11 = ENTREE.read_bytes()
    if sha(b11) != EMPREINTE_ENTREE:
        sys.exit(f"empreinte de {ENTREE} inattendue")
    brap = RAPPORT_CL4.read_bytes()
    if sha(brap) != EMPREINTE_CL4:
        sys.exit(f"empreinte de {RAPPORT_CL4} inattendue")
    chemin_couples = Path(argv[2]) if essai else COUPLES
    bc = chemin_couples.read_bytes()
    if not essai and sha(bc) != EMPREINTE_COUPLES:
        sys.exit(f"empreinte de {COUPLES} inattendue")
    if not essai and (SORTIE.exists() or JOURNAL.exists()):
        sys.exit(f"{SORTIE} ou {JOURNAL} existe déjà (R12)")
    couples = json.loads(bc.decode("utf-8"))
    t11, rapport = b11.decode("utf-8"), brap.decode("utf-8")
    rc = controles_couples(couples, rapport)
    t12, lignes = appliquer(t11, couples)
    rt, ecarts = controles_texte(t11, t12, couples)
    with tempfile.TemporaryDirectory(prefix="p3bis-b12-") as d:
        rg = controles_git(t12, Path(d))
        if essai:
            tmp = Path(d) / "essai-brouillon12.md"
            tmp.write_text(t12, encoding="utf-8")
            pb = problemes(tmp)
        else:
            SORTIE.write_text(t12, encoding="utf-8")
            pb = problemes(SORTIE)
    attendu_pb = ["marqueurs de gabarit restants : " + ", ".join(f"<<{m}>>" for m in sorted(MARQUEURS_ATTENDUS))]
    ok_p = pb == attendu_pb
    tous = all(ok for ok, _ in rc + rt + rg) and ok_p

    def bloc(r):
        return ["```"] + [("CONFORME — " if ok else "NON CONFORME — ") + x for ok, x in r] + ["```"]

    n_gel = sum(1 for c in couples if c["section_gelee"])
    j = [f"# Journal du brouillon 12 de P3-bis — {heure} (heure relevée par `date -u`, passée en argument)", "",
         "## Entrées", "",
         f"- entrée `{ENTREE}` `{sha(b11)}`",
         f"- rapport de la contre-lecture 4 `{RAPPORT_CL4}` `{sha(brap)}`",
         f"- couples `{chemin_couples}` `{sha(bc)}` ({len(couples)} couples, dont {n_gel} dans des sections gelées)",
         f"- script `{Path(__file__).as_posix()}` `{sha(Path(__file__).read_bytes())}`", "",
         "## Couples appliqués, dans l'ordre", "", "```"] + lignes + ["```", "",
         "## Couples de la contre-lecture 4 contre son rapport", ""] + bloc(rc) + ["",
         f"## Sortie", "", f"- `{SORTIE}` `{sha(t12.encode('utf-8'))}`", "",
         "## Comparaison programmée des sections gelées au brouillon 11, et contrôles du texte", ""] + bloc(rt) + ["",
         "## Écarts des sections gelées (différence de lignes, brouillon 11 → brouillon 12)", ""] + ecarts + [
         "## Pièces, registre des GO, empreinte orpheline et branche de la chaîne, recalculés par git (lecture seule)",
         ""] + bloc(rg) + ["",
         "## `controle_ia.prereg.problemes` (attendu : les six marqueurs gardés, rien d'autre)", "", "```"] + pb + [
         ("CONFORME — " if ok_p else "NON CONFORME — ") + "problemes() égal à l'attendu", "```", "",
         "**BROUILLON 12 : " + ("CONTRÔLES CONFORMES" if tous else "CONTRÔLES NON CONFORMES") + "**", "",
         ECARTS_ET_QUESTIONS]
    texte = "\n".join(j)
    if essai:
        print(texte)
    else:
        JOURNAL.write_text(texte, encoding="utf-8")
        print(sha(SORTIE.read_bytes()), SORTIE)
        print(sha(JOURNAL.read_bytes()), JOURNAL)
        print("BROUILLON 12 : " + ("CONTRÔLES CONFORMES" if tous else "CONTRÔLES NON CONFORMES"))
    return 0 if tous else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
