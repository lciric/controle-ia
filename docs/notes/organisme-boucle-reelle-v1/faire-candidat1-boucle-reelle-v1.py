#!/usr/bin/env python3
"""Préenregistrement de la plus petite course réelle de la boucle complète de l'organisme : fabrication du candidat 1 (v1).

Écrit par le rédacteur des brouillons 2 et 3 (Claude Opus 5.5, sous-agent de la session mère
`session_01VJdZpSMxSdk2SJ1ScmdfNv`), sur la consigne `consigne-redaction-prereg-course-v66-b2-v1.md` (`bfdc52ad…`) et le
message de la mère qui porte les mots de Lazar (R-2265). Le script fait quatre choses, dans cet ordre, et rien d'autre :

1. il vérifie les empreintes de ses entrées (brouillon 3 ; registre des GO juste après l'inscription de GO-2026-11-10-11 ;
   blocs du développeur v66) ; toute différence arrête (R11) ; il lit dans le registre la ligne GO-2026-11-10-11 (une seule)
   et, dans sa référence, le mot de Lazar verbatim ;
2. il applique au brouillon 3 les couples du candidat (`COUPLES`) : mots de Lazar portés aux marqueurs (NL-1 option (b), avec
   les couples d'accompagnement tenus prêts au journal du brouillon 3 ; NL-2, GO-2026-11-10-11), passages préparés réglés
   (CLB-04), ligne de GO recopiée à l'octet ; chaque texte ancien trouvé une seule fois (ou le nombre de fois déclaré) ;
3. il contrôle le résultat : **aucun marqueur** au motif du lanceur ; blocs de la section 16 égaux à ceux du développeur,
   la ligne `go` portant GO-2026-11-10-11 ; plan aux règles de forme du lanceur ; aucune tournure périmée ;
4. il écrit le candidat et le fichier des couples sous des noms neufs, sans jamais écraser (R12).

Aucun appel réseau, aucun modèle, aucune écriture git, aucun module de l'organisme importé.

Usage : python3 -I -B faire-candidat1-boucle-reelle-v1.py --depot DEPOT --candidat SORTIE.md --couples SORTIE.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

D = "docs/notes/organisme-boucle-reelle-v1"
ENTREES = {
    "brouillon3": (f"{D}/preenregistrement-boucle-reelle-organisme-v1-brouillon3.md",
                   "04598de62300185806975ae5df5fcdd054557f9a46b935e40d7d3479c240ec23"),
    "registre_go": ("registres/go.md", "8de009e115e263225746e734812dc0d9b5dd46c0407bf1727255c2d37c8d72b1"),
    "blocs_v66": (f"{D}/code-v66/blocs-v66/blocs-pour-le-texte-v66.md",
                  "9933ee114687079bbf95af94b5e39cd898b69d1d197b4c48587d12692fee1b29"),
}
GO = "GO-2026-11-10-11"
SHA_REGISTRE = ENTREES["registre_go"][1]
COMMIT_REGISTRE = "8053801a"
NOM_SCELLE = "preenregistrement-boucle-reelle-organisme-v1-v1.md"
SECTIONS_GELEES = {"2. Hypothèse", "4. Prédictions chiffrées et signes attendus", "5. Métriques", "6. Seuils",
                   "7. Plan d'analyse", "8. Critères de lecture gelés", "9. Audit de symétrie (règle R4), écrit d'avance",
                   "10. Liste d'arrêt"}
MARQUEUR = re.compile(r"<<[A-Z0-9_-]+>>")  # même motif que le lanceur v66
MARQUES = ("<!-- empreintes-du-code-v66 : début -->", "<!-- empreintes-du-code-v66 : fin -->",
           "<!-- plan-gele-v66 : début -->", "<!-- plan-gele-v66 : fin -->",
           "<!-- jeu-plante-v65 : début -->", "<!-- jeu-plante-v65 : fin -->")
PERIMES = ("brouillon 3, non scellé", "Marqueurs restants", "texte candidat règle", "Vérification courte du différentiel jusqu'au",
           "v<N>", "attend la décision", "issue de ce cas est fixée à la", "issue de ce cas à la ligne C1",
           "(section 8, ligne C1)", "le marqueur de la ligne de GO", "les mots de Lazar sur NL-1 (ligne C1)",
           "GO_COURSE_V66", "MOT_LAZAR", "NOEUD_C1", "EMPREINTE_GO_MD")


class Arret(Exception):
    pass


def h(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def couples(ligne_go: str, verbatim: str) -> list:
    mot = (f"mot direct de Lazar dans la session mère, reçu vers 16:53 UTC, heure relevée par `date -u`, verbatim : "
           f"« {verbatim} »")
    c7 = ("| C7 | conditions de C1 tenues (P1, P4, P6 ; V-1 à V-7) **et** aucune carte réelle retenue en génération 1 (V-8) | "
          "**« la chaîne garde, boucle non éprouvée »** | les parties (a) et (b) de H-boucle tiennent (vraies survivantes, "
          "fausses refusées dans les deux générations) ; la partie (c) n'est pas éprouvée sur un contenu (sélection de la "
          "génération 1 vide : P5 sans copie, P6 sur {K1}) ; ouvre la proposition au directeur d'une course qui éprouve (c), "
          "non celle de plusieurs générations sur la foi de cette course ; ne dit rien de la classe non couverte ni des données "
          "réelles ; le programme gelé rend C1 dans ce cas, le lecteur du verdict écrit C7 (V-8) |\n")
    return [
        # --- en-tête -----------------------------------------------------------------------------------------------------
        {"id": "C1-01", "section": "titre", "constat": "CLB-04 (1)", "objet": "titre du texte candidat",
         "ancien": "l'organisme d'idéation, brouillon 3\n", "nouveau": "l'organisme d'idéation, v1 (candidat 1)\n"},
        {"id": "C1-02", "section": "en-tête", "constat": "CLB-04 (1) ; R-2265", "objet": "statut du candidat 1",
         "debut": "**Statut : brouillon 3, non scellé : il ne vaut pas préenregistrement (R1).**",
         "fin": "Le code v66 est écrit, essayé et contre-lu (section 12.1).",
         "nouveau": f"""**Statut : candidat 1 au scellement (R1).** Il devient le texte scellé, octet pour octet, sous le nom
`{NOM_SCELLE}`, si la vérification courte du différentiel le dit scellable (section 15).
Brouillons 1 à 3 gardés intacts (`736e3fd6…`, `f87ad0e4…`, `04598de6…`) ; contre-lu (contre-lecture 1 du brouillon 2,
section 15) ; mots de Lazar sur NL-1 et NL-2 portés (R-2265 : issue C7 de la section 8 ; ligne de GO {GO}, section 13) ;
aucun marqueur ; passé au lanceur de l'organisme depuis une copie, validateur qui fait foi (section 12.2 ; sortie au journal
du candidat 1). Script, couples et journal : section 15. **Aucune course réelle avant** : le scellement et le dépôt de ce
texte, et sa copie à l'octet dans l'arbre de l'organisme (section 12.2, point 4) ; les préalables sur la machine à `bwrap`
(section 12.3). Le code v66 est écrit, essayé et contre-lu (section 12.1)."""},
        {"id": "C1-03", "section": "en-tête", "constat": "CLB-04 (6)", "objet": "rédacteur du candidat 1",
         "ancien": "  tels qu'écrits ; mêmes abstentions.",
         "nouveau": """  tels qu'écrits ; mêmes abstentions. **Candidat 1** : le même rédacteur, sur le message de la mère qui porte les mots de
  Lazar (R-2265) ; mêmes abstentions, sauf le passage du texte au lanceur de l'organisme depuis une copie, demandé par la
  mère (section 12.2, point 3)."""},
        {"id": "C1-04", "section": "en-tête", "constat": "CLB-04 (6)", "objet": "heures du candidat 1",
         "ancien": "  début de la tâche 15:14:15, couples écrits à partir de 15:18:42 (heure de fin au journal du brouillon 3).",
         "nouveau": """  début de la tâche 15:14:15, couples écrits à partir de 15:18:42 (heure de fin au journal du brouillon 3) ; candidat 1,
  10 novembre 2026, début de la tâche 16:54:11, couples écrits à partir de 16:56:12 (heure de fin au journal du candidat 1)."""},
        {"id": "C1-05", "section": "en-tête", "constat": "CLB-04 (6) ; R-2265", "objet": "consigne et message du candidat 1",
         "ancien": "  couples, avec ses décisions sur CLB-03, CLB-04, CLB-05, CLB-10 et Q-4.",
         "nouveau": """  couples, avec ses décisions sur CLB-03, CLB-04, CLB-05, CLB-10 et Q-4. **Candidat 1** : même consigne ; message de la
  mère du 10 novembre 2026 portant les mots de Lazar (R-2265) : NL-1 (b), NL-2 ({GO}), passages préparés réglés, passage
  au lanceur.""".replace("{GO}", GO)},
        {"id": "C1-06", "section": "en-tête", "constat": "CLB-04 (2) ; NL-2 ; R-2265", "objet": "ligne de GO de la course, mot de Lazar, registre après inscription",
         "ancien": """la course se lance sous la ligne neuve <<GO_COURSE_V66>> (section 13 ; mot de
  Lazar, verbatim et heure relevée : « <<MOT_LAZAR_NL2>> » ; `registres/go.md` après l'inscription :
  `<<EMPREINTE_GO_MD_APRES_NL2>>`).""",
         "nouveau": f"""la course se lance sous la ligne neuve **{GO}**, inscrite le 10 novembre 2026
  (section 13 ; {mot} ; R-2265 ; `registres/go.md` après l'inscription : `{SHA_REGISTRE}`, commit `{COMMIT_REGISTRE}`)."""},
        {"id": "C1-07", "section": "en-tête", "constat": "R-2265", "objet": "registre : R-2265",
         "ancien": "brouillon 3 confié au même rédacteur). Décisions de",
         "nouveau": f"brouillon 3 confié au même rédacteur) ; R-2265 (mot de Lazar : NL-2, {GO} inscrit ; NL-1 (b) ; candidat 1).\n  Décisions de"},
        {"id": "C1-08", "section": "en-tête", "constat": "CLB-04 (6)", "objet": "arbres du candidat 1",
         "ancien": "`84ab119f0b3eefdd689b4be03f03bb776ebd2c7c1247b9d76e903181a419b1bc`).",
         "nouveau": f"`84ab119f0b3eefdd689b4be03f03bb776ebd2c7c1247b9d76e903181a419b1bc`). **Candidat 1** : mêmes arbres ; `main` du dépôt\n  de travail à `{COMMIT_REGISTRE}`."},
        # --- documents ---------------------------------------------------------------------------------------------------
        {"id": "C1-09", "section": "Documents qui font foi (chemin, empreinte sha256)", "constat": "NL-2", "objet": "pièce : ligne de GO de la course",
         "ancien": "| relais Kimi (hors du dossier de course ; section 12.3, point 6) | `docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v3.py` | `d54ed2bce54f5c89e9f078d1a03b5d8159894d6565ae560c3601c1e63ca76239` |",
         "nouveau": f"""| relais Kimi (hors du dossier de course ; section 12.3, point 6) | `docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v3.py` | `d54ed2bce54f5c89e9f078d1a03b5d8159894d6565ae560c3601c1e63ca76239` |
| ligne de GO de la course, {GO} (candidat 1 ; recopiée à l'octet en section 13) | `registres/go.md`, commit `{COMMIT_REGISTRE}` | registre entier `{SHA_REGISTRE}` |"""},
        {"id": "C1-10", "section": "Documents qui font foi (chemin, empreinte sha256)", "constat": "candidat 1", "objet": "pièces versées : candidat 1",
         "ancien": "les brouillons 2 et 3, leurs couples, scripts\net journaux (section 15).",
         "nouveau": "les brouillons 2 et 3 et le candidat 1, leurs\ncouples, scripts et journaux (section 15)."},
        # --- section 0 ---------------------------------------------------------------------------------------------------
        {"id": "C1-11", "section": "0. En dix lignes", "constat": "NL-1 (b)", "objet": "point 6 : issue C7",
         "ancien": "et l'issue de ce cas est fixée à la\n   ligne C1 (section 8).",
         "nouveau": "et l'issue de ce cas est C7 « la chaîne\n   garde, boucle non éprouvée » (section 8 ; NL-1, option (b), R-2265)."},
        {"id": "C1-12", "section": "0. En dix lignes", "constat": "CLB-04 (3)", "objet": "point 8 : ce qui reste",
         "debut": "8. **Ce qui reste** (section 12) :",
         "fin": "candidat au lanceur et une vérification courte du différentiel ; **avant le lancement** : la machine à `bwrap` et les\n   préalables de la section 12.3.",
         "nouveau": """8. **Ce qui reste** (section 12) : le code est fait (v66, tête `7e415cba`, contre-lu « utilisable pour la course » ;
   configuration v6 `4743ddbe…` ; blocs gelés en section 16) ; ce texte est contre-lu (section 15) et porte les mots de
   Lazar (R-2265) ; **avant le lancement** : son scellement et sa copie dans l'arbre de l'organisme (section 12.2), la
   machine à `bwrap` et les préalables de la section 12.3."""},
        # --- section 8 (gelée) -------------------------------------------------------------------------------------------
        {"id": "C1-13", "section": "8. Critères de lecture gelés", "constat": "NL-1 (b) ; R-2265", "objet": "fin de la ligne C1 : mot de Lazar et issue C7",
         "ancien": " ; **issue de ce cas**, fixée par Lazar (mot verbatim, heure relevée : « <<MOT_LAZAR_NL1>> ») : <<NOEUD_C1_SANS_RETENUE>> |",
         "nouveau": f" ; **issue de ce cas**, fixée par Lazar (NL-1, option (b) ; {mot} ; R-2265) : l'issue est C7 « la chaîne garde, boucle non éprouvée » (ligne C7, lue avant C1) |"},
        {"id": "C1-14", "section": "8. Critères de lecture gelés", "constat": "NL-1 (b) ; journal du brouillon 3, section 3", "objet": "ligne C7 insérée avant C1",
         "ancien": "| C1 | P1, P4 et P6 tenues, **et** V-1 à V-7 tenues",
         "nouveau": c7 + "| C1 | P1, P4 et P6 tenues, **et** V-1 à V-7 tenues"},
        {"id": "C1-15", "section": "8. Critères de lecture gelés", "constat": "NL-1 (b) ; journal du brouillon 3, section 3", "objet": "V-8 : issue C7",
         "ancien": "phrase en tête et issue de ce cas, ligne C1 |", "nouveau": "phrase en tête et issue C7 (ligne C7) |"},
        # --- section 9 (gelée) -------------------------------------------------------------------------------------------
        {"id": "C1-16", "section": "9. Audit de symétrie (règle R4), écrit d'avance", "constat": "NL-1 (b) ; journal du brouillon 3, section 3", "objet": "A1 d'office sous C1 ou C7",
         "ancien": "déclenché d'office si C1 (l'issue", "nouveau": "déclenché d'office si C1 ou C7 (l'issue"},
        # --- section 10 (gelée) ------------------------------------------------------------------------------------------
        {"id": "C1-17", "section": "10. Liste d'arrêt", "constat": "CLB-04 (8)", "objet": "nom du texte scellé (v1)",
         "ancien": "`orchestrator/prereg/preenregistrement-boucle-reelle-organisme-v1-v<N>.md`",
         "nouveau": f"`orchestrator/prereg/{NOM_SCELLE}`"},
        # --- section 11 --------------------------------------------------------------------------------------------------
        {"id": "C1-18", "section": "11. Prémortem du rapport au directeur, et réponse du dessin", "constat": "NL-1 (b)", "objet": "issue C7",
         "ancien": "(V-8 ; issue de ce cas à la ligne C1) |", "nouveau": "(V-8 ; issue C7) |"},
        # --- section 12 --------------------------------------------------------------------------------------------------
        {"id": "C1-19", "section": "12. Ce qui est fait, ce qui reste avant le scellement, et les préalables sur la machine",
         "constat": "CLB-04 (6) ; R-2265", "objet": "12.2, points 1 à 3 : faits (la phrase du validateur qui fait foi gardée)",
         "debut": "1. **Mot de Lazar sur NL-1** (C1 sans carte retenue",
         "fin": "travail avant la course : c'est l'exemplaire qui fait foi (R1), et l'empreinte de ses octets est la racine des graines.",
         "nouveau": f"""1. **Mot de Lazar sur NL-1** : option (b) (R-2265) ; portée à la section 8 (ligne C7 « la chaîne garde, boucle non
   éprouvée », fin de la ligne C1, V-8) et à la section 9 (A1 d'office sous C1 ou C7).
2. **Mot de Lazar sur NL-2** : ligne **{GO}** inscrite (R-2265 ; `registres/go.md` à `{SHA_REGISTRE[:8]}…`, commit
   `{COMMIT_REGISTRE}` ; recopiée en section 13) ; son identifiant est porté partout (en-tête, section 12.1, section 13,
   commande de la section 12.4, bloc `plan-gele-v66` de la section 16), écrit à la main dans le bloc, l'outil
   `preparer_boucle_reelle_v66.py` n'acceptant que GO-2026-11-08-02 ou GO-2026-11-10-10 ; le lanceur lit tout identifiant
   de la forme `GO-AAAA-MM-JJ-NN` et le vérifie dans le registre.
3. Contre-lecture 1 faite (section 15) ; passages préparés au brouillon 3 réglés dans ce candidat ; ce texte passé au
   lanceur depuis une copie (`--verifier-seulement`, sous le nom `{NOM_SCELLE}` : refus attendu à la garde 22
   hors d'une machine à `bwrap` ; sortie au journal du candidat 1) ; puis vérification courte du différentiel ; scellé
   (`controle_ia.scellement sceller`) sous le nom `{NOM_SCELLE}`, committé et poussé sur le dépôt de
   travail avant la course : c'est l'exemplaire qui fait foi (R1), et l'empreinte de ses octets est la racine des graines."""},
        {"id": "C1-20", "section": "12. Ce qui est fait, ce qui reste avant le scellement, et les préalables sur la machine",
         "constat": "CLB-04 (8)", "objet": "commande : nom du texte scellé",
         "ancien": "--preenregistrement prereg/preenregistrement-boucle-reelle-organisme-v1-v<N>.md",
         "nouveau": f"--preenregistrement prereg/{NOM_SCELLE}"},
        # --- section 13 --------------------------------------------------------------------------------------------------
        {"id": "C1-21", "section": "13. Devis", "constat": "CLB-04 (2) ; NL-2 ; R-2265", "objet": "ligne de GO : identifiant et mot de Lazar",
         "ancien": "`registres/go.md` : **<<GO_COURSE_V66>>** (mot de Lazar, verbatim et heure relevée : « <<MOT_LAZAR_NL2>> »).",
         "nouveau": f"`registres/go.md` : **{GO}** ({mot} ; R-2265)."},
        {"id": "C1-22", "section": "13. Devis", "constat": "CLB-04 (8)", "objet": "nom du texte scellé",
         "ancien": "préenregistrement scellé (`preenregistrement-boucle-reelle-organisme-v1-v<N>.md`)",
         "nouveau": f"préenregistrement scellé (`{NOM_SCELLE}`)"},
        {"id": "C1-23", "section": "13. Devis", "constat": "NL-2 ; R-2265", "objet": "ligne de GO recopiée à l'octet",
         "ancien": "dépense (`registres/depenses.md`, `registres/arrets.md`).",
         "nouveau": f"""dépense (`registres/depenses.md`, `registres/arrets.md`).

**La ligne inscrite**, recopiée à l'octet de `registres/go.md` (commit `{COMMIT_REGISTRE}`, registre `{SHA_REGISTRE[:8]}…`). Elle porte
le type « calcul », l'accord de Lazar, l'échéance du 30 novembre 2026, un plafond lu en montant seul (45 USD), aucune ligne
d'extension, et les conditions ci-dessus :

```
{ligne_go}
```"""},
        # --- section 14 --------------------------------------------------------------------------------------------------
        {"id": "C1-24", "section": "14. Portée", "constat": "NL-1 (b)", "objet": "issue C7",
         "ancien": "(section 8, ligne C1).", "nouveau": "(section 8, issue C7)."},
        # --- section 15 --------------------------------------------------------------------------------------------------
        {"id": "C1-25", "section": "15. Contre-lecture (règle R2)", "constat": "CLB-04 (7)", "objet": "consigne de la contre-lecture 1 : empreinte entière",
         "ancien": "`consigne-contre-lecture-1-prereg-course-v66-b2-v1.md` (`0042d919…`).",
         "nouveau": "`consigne-contre-lecture-1-prereg-course-v66-b2-v1.md`\n  (`0042d919954f945c53f736f82446e03c4744b56167c35d97448cfdb48c5e4d23`)."},
        {"id": "C1-26", "section": "15. Contre-lecture (règle R2)", "constat": "CLB-04 (7)", "objet": "pièces du candidat 1",
         "ancien": "empreintes à leurs compagnons ; brouillon 2 : mêmes noms en « brouillon2 ») :",
         "nouveau": "empreintes à leurs compagnons ; brouillon 2 : mêmes noms en « brouillon2 » ; candidat 1 :\n  `faire-candidat1-boucle-reelle-v1.py`, `couples-candidat1-boucle-reelle-v1.json`, `journal-candidat1-boucle-reelle-v1.md`) :"},
        {"id": "C1-27", "section": "15. Contre-lecture (règle R2)", "constat": "CLB-04 (7)", "objet": "CLB-04 réglé",
         "ancien": """ceux qui en dépendent portent
    des marqueurs, que le texte candidat règle d'un coup avec les autres passages préparés (journal du brouillon 3) ;""",
         "nouveau": """les autres, en marqueurs au
    brouillon 3, réglés dans ce candidat par les mots de Lazar (R-2265), avec les passages préparés (journal du brouillon 3,
    section 3) ;"""},
        {"id": "C1-28", "section": "15. Contre-lecture (règle R2)", "constat": "CLB-04 (7)", "objet": "vérification courte : sur ce texte, consignée au registre",
         "ancien": """**Vérification courte du différentiel jusqu'au texte candidat** : à faire, marqueurs remplis, avec le passage du texte au
lanceur depuis une copie.""",
         "nouveau": """**Vérification courte du différentiel brouillon 3 → candidat 1** : sur ce texte, avant son scellement ; son rapport, son
empreinte et son verdict sont consignés au registre (`registres/decisions.md`) avec le scellement, ce texte ne pouvant pas
porter l'empreinte d'un rapport qui le relit. Le passage de ce texte au lanceur depuis une copie, avant elle, est au journal
du candidat 1."""},
        {"id": "C1-29", "section": "15. Contre-lecture (règle R2)", "constat": "CLB-04 (7)", "objet": "contre-lecture du code v65 : empreinte entière",
         "ancien": "(`code-v65/contre-lecture-code-v65-v2.md`, `c4ddfc7f…`)",
         "nouveau": "(`code-v65/contre-lecture-code-v65-v2.md`,\n  `c4ddfc7ffd4b5cea1b0eb70e2a08ea551c8a8e8ef6f1a169ef8bebdab976ed03`)"},
        {"id": "C1-30", "section": "15. Contre-lecture (règle R2)", "constat": "CLB-04 (7)", "objet": "contre-lecture du code v66 : empreinte entière",
         "ancien": "(`code-v66/contre-lecture-code-v66-courte-v1.md`, `a2880368…`)",
         "nouveau": "(`code-v66/contre-lecture-code-v66-courte-v1.md`,\n  `a28803689558e6813f24f625915c823b6a8c1c17802e351ae3f0f4dd9d3b7b00`)"},
        {"id": "C1-31", "section": "15. Contre-lecture (règle R2)", "constat": "NL-1 (b)", "objet": "CLV66-04 : issue C7",
         "ancien": "V-8 et issue de ce cas fixée par Lazar (ligne C1) ;",
         "nouveau": "V-8 et issue C7 fixée par Lazar (NL-1, option (b), R-2265) ;"},
        # --- section 16 (intro ; blocs : C1-33) --------------------------------------------------------------------------
        {"id": "C1-32", "section": "16. Blocs gelés lus par le lanceur (code v66)", "constat": "NL-2", "objet": "intro : identifiant de la ligne de GO",
         "ancien": "qui porte le marqueur de la ligne de GO neuve (section 13) au lieu de GO-2026-11-08-02.",
         "nouveau": f"qui porte l'identifiant de la ligne de GO de la course, {GO} (section 13), au lieu de GO-2026-11-08-02."},
        {"id": "C1-33", "section": "12. et 16. (marqueur restant)", "constat": "NL-2 ; R-2265",
         "objet": f"marqueur de l'identifiant remplacé par {GO} partout où il reste (section 12.1, commande de 12.4, bloc plan-gele-v66)",
         "partout": "<<GO_COURSE_V66>>", "n": 3, "nouveau": GO},
    ]


def appliquer(texte: str, c: dict) -> str:
    if "partout" in c:
        n = texte.count(c["partout"])
        if n != c["n"]:
            raise Arret(f"{c['id']} : {c['partout']} trouvé {n} fois ({c['n']} attendues)")
        c["ancien"] = c["partout"]
        return texte.replace(c["partout"], c["nouveau"])
    if "debut" not in c:
        n = texte.count(c["ancien"])
        if n != 1:
            raise Arret(f"{c['id']} : texte ancien trouvé {n} fois (une exigée)")
        return texte.replace(c["ancien"], c["nouveau"], 1)
    i, j = texte.count(c["debut"]), texte.count(c["fin"])
    if i != 1 or j != 1:
        raise Arret(f"{c['id']} : début trouvé {i} fois, fin {j} fois (une exigée)")
    a, b = texte.index(c["debut"]), texte.index(c["fin"]) + len(c["fin"])
    if b <= a:
        raise Arret(f"{c['id']} : fin avant le début")
    c["ancien"] = texte[a:b]
    return texte[:a] + c["nouveau"] + texte[b:]


def controler(texte: str, blocs: str) -> dict:
    restants = sorted(set(MARQUEUR.findall(texte)))
    if restants:
        raise Arret(f"marqueurs restants : {restants}")
    for m in MARQUES:
        if texte.count(m) != 1:
            raise Arret(f"marque {m!r} présente {texte.count(m)} fois")
    attendu = blocs.replace("go: GO-2026-11-08-02\n", f"go: {GO}\n", 1).rstrip("\n")
    a, b = texte.index(MARQUES[0]), texte.index(MARQUES[5]) + len(MARQUES[5])
    if texte[a:b] != attendu:
        raise Arret("blocs ≠ blocs du développeur avec la ligne go de la course")
    plan = dict(re.findall(r"^\s*([a-z0-9_]+)\s*:\s*(.+?)\s*$", texte[texte.index(MARQUES[2]):texte.index(MARQUES[3])], re.M))
    if plan.get("go") != GO or not re.fullmatch(r"GO-\d{4}-\d{2}-\d{2}-\d{2}", plan["go"]):
        raise Arret(f"plan : go = {plan.get('go')!r}")
    perimes = [p for p in PERIMES if p in texte]
    if perimes:
        raise Arret(f"tournures périmées restantes : {perimes}")
    return {"marqueurs_restants": [], "plan_go": plan["go"]}


def principal(argv=None) -> int:
    a = argparse.ArgumentParser()
    a.add_argument("--depot", required=True)
    a.add_argument("--candidat", required=True)
    a.add_argument("--couples", required=True)
    x = a.parse_args(argv)
    depot = Path(x.depot)
    try:
        for s in (Path(x.candidat), Path(x.couples)):
            if s.exists():
                raise Arret(f"{s} existe : on n'écrase jamais (R12)")
        lus = {}
        for nom, (rel, sha) in ENTREES.items():
            octets = (depot / rel).read_bytes()
            if h(octets) != sha:
                raise Arret(f"{rel} : empreinte {h(octets)} ≠ {sha} (R11)")
            lus[nom] = octets.decode("utf-8")
        lignes = [l for l in lus["registre_go"].split("\n") if l.startswith(f"| {GO} |")]
        if len(lignes) != 1:
            raise Arret(f"registre : {len(lignes)} ligne(s) {GO} (une exigée)")
        ligne_go = lignes[0]
        m = re.search(r"verbatim : « (.+?) » \|$", ligne_go)
        if not m:
            raise Arret("registre : mot de Lazar verbatim introuvable dans la ligne")
        verbatim = m.group(1)
        texte = lus["brouillon3"]
        cs = couples(ligne_go, verbatim)
        ids = [c["id"] for c in cs]
        if len(ids) != len(set(ids)):
            raise Arret("identifiants en double")
        for c in cs:
            texte = appliquer(texte, c)
        ctl = controler(texte, lus["blocs_v66"])
        sortie = texte.encode("utf-8")
        Path(x.candidat).write_bytes(sortie)
        gel = [c["id"] for c in cs if c["section"] in SECTIONS_GELEES]
        doc = {"objet": "couples du candidat 1 du préenregistrement de la course réelle de l'organisme (code v66, configuration v6)",
               "entrees": {k: {"chemin": v[0], "sha256": v[1]} for k, v in ENTREES.items()},
               "ligne_go_recopiee": ligne_go, "mot_de_lazar_verbatim": verbatim,
               "sections_gelees": sorted(SECTIONS_GELEES),
               "couples": [dict(c, gelee=c["section"] in SECTIONS_GELEES) for c in cs],
               "nombre_de_couples": len(cs), "couples_en_section_gelee": gel, "controles": ctl,
               "sortie": {"chemin": x.candidat, "sha256": h(sortie)}}
        Path(x.couples).write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(json.dumps({"candidat_sha256": h(sortie), "couples": len(cs), "en_section_gelee": gel, "controles": ctl},
                         ensure_ascii=False, indent=1))
        return 0
    except Arret as e:
        print(f"arrêt : {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(principal())
