#!/usr/bin/env python3
"""Préenregistrement de la plus petite course réelle de la boucle complète de l'organisme : fabrication du brouillon 3 (v1).

Écrit par le rédacteur du brouillon 2 (Claude Opus 5.5, sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`),
sur la consigne `consigne-redaction-prereg-course-v66-b2-v1.md` (`bfdc52ad…`) et le message de la mère du 10 novembre 2026
(R-2253). Le script fait cinq choses, dans cet ordre, et rien d'autre :

1. il vérifie les empreintes de ses entrées (brouillon 2, rapport et couples de la contre-lecture 1) ; toute différence
   arrête (R11) ;
2. il applique au brouillon 2 les neuf couples CLC-01 à CLC-09 de la contre-lecture 1, **tels qu'écrits** dans le fichier de
   couples (chaque texte ancien trouvé une seule fois au moment de son application), puis exige que l'empreinte du texte
   obtenu soit `b19db56e…` (rapport de la contre-lecture 1, section 8 ; décision de la mère, R-2253) ;
3. il applique ensuite les couples du rédacteur du brouillon 3 (`COUPLES_B3`), qui portent les décisions de la mère
   (R-2253) et préparent les passages que la contre-lecture 1 dit périmés au candidat (CLB-04) ;
4. il contrôle le résultat : section 16 (blocs lus par le lanceur) égale à l'octet à celle du brouillon 2 ; marqueurs
   restants exactement ceux attendus, avec leur nombre d'occurrences, au motif du lanceur ; aucune mention restante d'un
   nœud « en attente » hors des marqueurs ;
5. il écrit le brouillon 3 et le fichier des couples (JSON : CLC recopiés, couples B3 avec section, section gelée ou non,
   constat ; empreintes) sous des noms neufs, sans jamais écraser (R12).

Aucun appel réseau, aucun modèle, aucune écriture git, aucun module de l'organisme importé.

Usage : python3 -I -B faire-brouillon3-boucle-reelle-v1.py --depot DEPOT --brouillon3 SORTIE.md --couples SORTIE.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

D = "docs/notes/organisme-boucle-reelle-v1"
CL = "prereg/contre-lectures/preenregistrement-boucle-reelle-organisme-v1-brouillon2-cl1"
ENTREES = {
    "brouillon2": (f"{D}/preenregistrement-boucle-reelle-organisme-v1-brouillon2.md",
                   "f87ad0e40f1b2941e66d343bfb4b5eeaaefa22a3e2eeb448f852900de112b8a7"),
    "rapport_cl1": (f"{CL}.md", "90ba927ec9ec390026f3d2dbbab2fe32f1e8ff8bb553f49a15842ce5e420395c"),
    "couples_cl1": (f"{CL}-couples.json", "a555f82c659907b273e47b913f0c48a4231a66115883c58d201383c0128ca514"),
}
EMPREINTE_APRES_CLC = "b19db56e58302d57ee3d1aa114a6038f9aceb54b93b233930da513d7b4846cc6"
IDS_CLC = [f"CLC-0{k}" for k in range(1, 10)]
SECTIONS_GELEES = {"2. Hypothèse", "4. Prédictions chiffrées et signes attendus", "5. Métriques", "6. Seuils",
                   "7. Plan d'analyse", "8. Critères de lecture gelés", "9. Audit de symétrie (règle R4), écrit d'avance",
                   "10. Liste d'arrêt"}
SECTIONS_CLC = {"CLC-01": "12.4", "CLC-02": "12.4", "CLC-03": "12.3", "CLC-04": "8. Critères de lecture gelés",
                "CLC-05": "8. Critères de lecture gelés", "CLC-06": "10. Liste d'arrêt", "CLC-07": "10. Liste d'arrêt",
                "CLC-08": "8. Critères de lecture gelés", "CLC-09": "8. Critères de lecture gelés"}
MARQUEUR = re.compile(r"<<[A-Z0-9_-]+>>")  # même motif que le lanceur v66
MARQUEURS_ATTENDUS = {"<<GO_COURSE_V66>>": 5, "<<MOT_LAZAR_NL2>>": 2, "<<EMPREINTE_GO_MD_APRES_NL2>>": 1,
                      "<<MOT_LAZAR_NL1>>": 1, "<<NOEUD_C1_SANS_RETENUE>>": 1}
DEBUT_16 = "\n## 16. Blocs gelés lus par le lanceur (code v66)\n"
PERIMES = ("attend la décision de Lazar", "attend un nœud", "issue du cas : nœud NL-1", "(section 8, nœud NL-1)",
           "(V-8, nœud NL-1)", "six préalables", "cinq autres préalables", "**Du texte : à faire**")


class Arret(Exception):
    pass


def h(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


R2253 = "décision de la mère, R-2253"

COUPLES_B3 = [
    # --- en-tête ------------------------------------------------------------------------------------------------------------
    {"id": "B3-01", "section": "titre", "constat": "brouillon 3", "objet": "titre : brouillon 3",
     "ancien": "l'organisme d'idéation, brouillon 2\n",
     "nouveau": "l'organisme d'idéation, brouillon 3\n"},

    {"id": "B3-02", "section": "en-tête", "constat": "brouillon 3 ; CLB-04 ; R-2253",
     "objet": "statut du brouillon 3 ; marqueurs restants (mots de Lazar) ; ce qui précède toute course",
     "debut": "**Statut : brouillon 2, texte non contre-lu (règle R2), non scellé : il ne vaut pas préenregistrement (R1).**",
     "fin": "(section 12.3). Le code v66 est écrit, essayé et contre-lu (section 12.1).",
     "nouveau": """**Statut : brouillon 3, non scellé : il ne vaut pas préenregistrement (R1).** Contre-lu une fois (contre-lecture 1,
Claude Fable 5.2 : « scellable après les mots de Lazar et corrections » ; section 15). Il porte au brouillon 2 (gardé intact,
`f87ad0e4…`) les neuf couples de la contre-lecture 1, tels qu'écrits (CLC-01 à CLC-09), puis les couples du rédacteur du
brouillon 3, qui appliquent les décisions de la mère (R-2253) : relais, nombres d'appels et prix (section 12.3, point 6) ;
condition de la machine dans la ligne de GO (section 13) ; validateur qui fait foi (section 12.2) ; passages préparés pour le
texte candidat ; entrée de la contre-lecture 1 (section 15). Script, couples et journal : section 15.
**Marqueurs restants**, tous remplis par les mots de Lazar (liste, occurrences et textes prêts au journal du brouillon 3 ; le
lanceur refuse tout texte qui en porte un) : `GO_COURSE_V66`, `MOT_LAZAR_NL2`, `EMPREINTE_GO_MD_APRES_NL2` (ligne de GO
neuve, NL-2) ; `MOT_LAZAR_NL1`, `NOEUD_C1_SANS_RETENUE` (issue de la course quand la génération 1 ne retient aucune carte
réelle, NL-1). **Aucune course réelle avant** : (i) les mots de Lazar sur NL-1 et NL-2 ; (ii) le texte candidat, marqueurs
remplis, passé au lanceur depuis une copie et vérifié en différentiel ; (iii) le scellement, le dépôt du texte scellé et sa
copie à l'octet dans l'arbre de l'organisme (section 12.2) ; (iv) les préalables sur la machine à `bwrap` (section 12.3).
Le code v66 est écrit, essayé et contre-lu (section 12.1)."""},

    {"id": "B3-03", "section": "en-tête", "constat": "brouillon 3", "objet": "rédacteur du brouillon 3",
     "ancien": """  devis, la puissance ou l'essai à blanc v1 ; il n'a lancé aucun essai, aucun appel de modèle, aucune dépense.""",
     "nouveau": """  devis, la puissance ou l'essai à blanc v1 ; il n'a lancé aucun essai, aucun appel de modèle, aucune dépense.
  **Brouillon 3** : le même rédacteur (R-2253), qui n'a écrit ni la contre-lecture 1 du brouillon 2 ni ses couples, appliqués
  tels qu'écrits ; mêmes abstentions."""},

    {"id": "B3-04", "section": "en-tête", "constat": "brouillon 3", "objet": "heures du brouillon 3",
     "ancien": """  14:29:39, couples écrits à partir de 14:41:50 (heure de fin au journal du brouillon 2).""",
     "nouveau": """  14:29:39, couples écrits à partir de 14:41:50 (heure de fin au journal du brouillon 2) ; brouillon 3, 10 novembre 2026,
  début de la tâche 15:14:15, couples écrits à partir de 15:18:42 (heure de fin au journal du brouillon 3)."""},

    {"id": "B3-05", "section": "en-tête", "constat": "brouillon 3 ; R-2253", "objet": "consigne et message du brouillon 3",
     "ancien": """  (`bfdc52ad2309636e42f28cc565a8e4e9c1a94c1b89a229224b4c000f90f9ac6d`, vérifiée), lancée en R-2244.""",
     "nouveau": """  (`bfdc52ad2309636e42f28cc565a8e4e9c1a94c1b89a229224b4c000f90f9ac6d`, vérifiée), lancée en R-2244. **Brouillon 3** : même
  consigne et mêmes interdits ; message de la mère du 10 novembre 2026 (R-2253) : appliquer la contre-lecture 1 et ses
  couples, avec ses décisions sur CLB-03, CLB-04, CLB-05, CLB-10 et Q-4."""},

    {"id": "B3-06", "section": "en-tête", "constat": "CLB-04 (point 2) ; NL-2",
     "objet": "lignes de GO : la ligne neuve, mot de Lazar et empreinte du registre après inscription (marqueurs)",
     "ancien": """  (contre-lecture du code v66, CLV66-07) : la course demande une ligne neuve (section 13).""",
     "nouveau": """  (contre-lecture du code v66, CLV66-07) : la course se lance sous la ligne neuve <<GO_COURSE_V66>> (section 13 ; mot de
  Lazar, verbatim et heure relevée : « <<MOT_LAZAR_NL2>> » ; `registres/go.md` après l'inscription :
  `<<EMPREINTE_GO_MD_APRES_NL2>>`)."""},

    {"id": "B3-07", "section": "en-tête", "constat": "brouillon 3", "objet": "registre : R-2253",
     "ancien": """  R-2243 (contre-lecture courte du code v66 : « utilisable pour la course ») ; R-2244 (ce brouillon lancé).""",
     "nouveau": """  R-2243 (contre-lecture courte du code v66 : « utilisable pour la course ») ; R-2244 (brouillon 2 lancé) ; R-2253
  (contre-lecture 1 du brouillon 2 rendue ; décisions de la mère ; brouillon 3 confié au même rédacteur)."""},

    # --- documents qui font foi -----------------------------------------------------------------------------------------------
    {"id": "B3-08", "section": "Documents qui font foi (chemin, empreinte sha256)", "constat": "CLB-05 ; brouillon 3",
     "objet": "pièces : contre-lecture 1 et ses couples ; relais Kimi",
     "ancien": """| décision N-065 (place de l'organisme dans le programme) | `docs/decisions/decision-N-065-v1.md` | `f820e90da0920d505d22bc7b33fad4906181d43bd5af7e79418a3c161a8a65c4` |""",
     "nouveau": """| décision N-065 (place de l'organisme dans le programme) | `docs/decisions/decision-N-065-v1.md` | `f820e90da0920d505d22bc7b33fad4906181d43bd5af7e79418a3c161a8a65c4` |
| contre-lecture 1 du brouillon 2 (brouillon 3) | `prereg/contre-lectures/preenregistrement-boucle-reelle-organisme-v1-brouillon2-cl1.md` | `90ba927ec9ec390026f3d2dbbab2fe32f1e8ff8bb553f49a15842ce5e420395c` |
| ses couples CLC-01 à CLC-09 | `prereg/contre-lectures/preenregistrement-boucle-reelle-organisme-v1-brouillon2-cl1-couples.json` | `a555f82c659907b273e47b913f0c48a4231a66115883c58d201383c0128ca514` |
| relais Kimi (hors du dossier de course ; section 12.3, point 6) | `docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v3.py` | `d54ed2bce54f5c89e9f078d1a03b5d8159894d6565ae560c3601c1e63ca76239` |"""},

    {"id": "B3-09", "section": "Documents qui font foi (chemin, empreinte sha256)", "constat": "brouillon 3",
     "objet": "pièces versées : brouillons 2 et 3",
     "ancien": """banc de mutations, paquet git et patch, contre-lecture courte du code v66) ; le brouillon 2, ses couples, son script et son
journal (section 15).""",
     "nouveau": """banc de mutations, paquet git et patch, contre-lecture courte du code v66) ; les brouillons 2 et 3, leurs couples, scripts
et journaux (section 15)."""},

    # --- section 0 ------------------------------------------------------------------------------------------------------------
    {"id": "B3-10", "section": "0. En dix lignes", "constat": "CLB-04 (point 3)", "objet": "point 6 : issue du cas fixée à la ligne C1",
     "ancien": """la phrase de résultat le dit en tête, et l'issue de ce cas attend un nœud
   de Lazar (section 8, NL-1).""",
     "nouveau": """la phrase de résultat le dit en tête, et l'issue de ce cas est fixée à la
   ligne C1 (section 8)."""},

    {"id": "B3-11", "section": "0. En dix lignes", "constat": "CLB-04 (point 3)", "objet": "point 8 : ce qui reste",
     "debut": "8. **Ce qui manque avant de sceller** (section 12) :",
     "fin": "lancement, la machine à `bwrap` et ses six préalables (section 12.3).",
     "nouveau": """8. **Ce qui reste** (section 12) : le code est fait (v66, tête `7e415cba`, contre-lu « utilisable pour la course » ;
   configuration v6 `4743ddbe…` ; blocs gelés en section 16) et ce texte est contre-lu une fois (section 15) ; **avant le
   scellement** : les mots de Lazar sur NL-1 (ligne C1) et NL-2 (ligne de GO neuve, section 13), puis le passage du texte
   candidat au lanceur et une vérification courte du différentiel ; **avant le lancement** : la machine à `bwrap` et les
   préalables de la section 12.3."""},

    # --- section 3 (dessin) ---------------------------------------------------------------------------------------------------
    {"id": "B3-12", "section": "3. Dessin", "constat": "CLB-11", "objet": "garde 22 : identité réglée sur l'exécuteur sondé ; mesure sur l'hôte par la sonde",
     "ancien": """  lanceur tourne **en superutilisateur**, seul moyen de passer à l'utilisateur dédié par `setpriv`, et vérifie après la sonde
  que l'identité du script sur l'hôte est 64097 : garde 22)""",
     "nouveau": """  lanceur tourne **en superutilisateur**, seul moyen de passer à l'utilisateur dédié par `setpriv`, et vérifie après la sonde
  que l'identité réglée sur l'exécuteur sondé est 64097, la sonde ayant vérifié sur l'hôte le propriétaire de son fichier
  témoin, `controler_hote_apres_sonde` : garde 22)"""},

    # --- section 8 (gelée) ----------------------------------------------------------------------------------------------------
    {"id": "B3-13", "section": "8. Critères de lecture gelés", "constat": "CLB-04 (point 4) ; NL-1",
     "objet": "ligne C1 : issue du cas sans carte retenue, fixée par Lazar (marqueurs du mot et de l'issue)",
     "ancien": """ ; l'issue de ce cas attend la décision de Lazar (nœud NL-1 du journal du brouillon 2) : <<NOEUD_C1_SANS_RETENUE>> |""",
     "nouveau": """ ; **issue de ce cas**, fixée par Lazar (mot verbatim, heure relevée : « <<MOT_LAZAR_NL1>> ») : <<NOEUD_C1_SANS_RETENUE>> |"""},

    {"id": "B3-14", "section": "8. Critères de lecture gelés", "constat": "CLB-04 (point 4)", "objet": "V-8 : renvoi à la ligne C1",
     "ancien": """| si oui et si l'issue est C1 : phrase en tête (ligne C1) ; issue du cas : nœud NL-1 |""",
     "nouveau": """| si oui, et si les conditions de C1 tiennent : phrase en tête et issue de ce cas, ligne C1 |"""},

    # --- section 10 (gelée) ---------------------------------------------------------------------------------------------------
    {"id": "B3-15", "section": "10. Liste d'arrêt", "constat": "CLB-11", "objet": "garde 22 : lettre de l'identité et de l'ordre",
     "ancien": """identité du script sur l'hôte, lue dans la description de l'exécuteur sondé, = 64097 ; ordre du mode réel : texte, monde, configuration, GO, garde 17, garde 22, garde 15, rôles réels en dernier |""",
     "nouveau": """identité réglée sur l'exécuteur sondé (sa description) = 64097, la sonde vérifiant sur l'hôte le propriétaire de son fichier témoin (`controler_hote_apres_sonde`) ; ordre du mode réel : texte, monde, empreinte de la configuration, GO, contenu de la configuration, garde 17, garde 22, sonde, garde 15, rôles réels en dernier |"""},

    # --- section 11 -----------------------------------------------------------------------------------------------------------
    {"id": "B3-16", "section": "11. Prémortem du rapport au directeur, et réponse du dessin", "constat": "CLC-03 (point 7 ajouté)",
     "objet": "préalables : renvoi sans nombre",
     "ancien": """avec les cinq autres préalables de la section 12.3 |""",
     "nouveau": """avec les autres préalables de la section 12.3 |"""},

    {"id": "B3-17", "section": "11. Prémortem du rapport au directeur, et réponse du dessin", "constat": "CLB-04 (point 5)",
     "objet": "renvoi à la ligne C1",
     "ancien": """la preuve est vide (V-8, nœud NL-1) |""",
     "nouveau": """la preuve est vide (V-8 ; issue de ce cas à la ligne C1) |"""},

    # --- section 12 -----------------------------------------------------------------------------------------------------------
    {"id": "B3-18", "section": "12. Ce qui est fait, ce qui reste avant le scellement, et les préalables sur la machine",
     "constat": "CLB-04 (point 6) ; Q-4 ; R-2253",
     "objet": "12.1 : GO de la course ; 12.2 réécrite : mots de Lazar, texte candidat, validateur qui fait foi",
     "debut": "| D1, D2, D3 | bras réel seul ;",
     "fin": "fait foi (R1), et l'empreinte de ses octets est la racine des graines.",
     "nouveau": """| D1, D2, D3 | bras réel seul ; génération 2 complète ; plafond de 40 USD de modèles (Kimi 33, Argon 7) et 5 USD de machine | décidés par Lazar (GO-2026-11-08-02) ; le GO de la course est la ligne neuve <<GO_COURSE_V66>> (section 13) |

### 12.2 Avant le scellement

1. **Mot de Lazar sur NL-1** (C1 sans carte retenue ; options et textes prêts aux journaux des brouillons 2 et 3) : il remplit
   `MOT_LAZAR_NL1` et `NOEUD_C1_SANS_RETENUE` (ligne C1) et, sous l'option d'une issue à part, ajoute sa ligne à la table de
   la section 8, par couples déclarés.
2. **Mot de Lazar sur NL-2 : ligne de GO neuve**, inscrite par Lazar (section 13) ; son identifiant remplace `GO_COURSE_V66`
   partout (en-tête, section 12.1, section 13, commande de la section 12.4, bloc `plan-gele-v66` de la section 16) ;
   `MOT_LAZAR_NL2` et `EMPREINTE_GO_MD_APRES_NL2` se remplissent au même moment. L'outil `preparer_boucle_reelle_v66.py`
   n'accepte que GO-2026-11-08-02 ou GO-2026-11-10-10 : l'identifiant neuf s'écrit donc à la main dans le bloc ; le lanceur lit
   tout identifiant de la forme `GO-AAAA-MM-JJ-NN` et le vérifie dans le registre.
3. Contre-lecture 1 faite (section 15). Texte candidat sous le nom `preenregistrement-boucle-reelle-organisme-v1-v<N>.md`
   (sans « brouillon »), sans marqueur, passages préparés réglés (journal du brouillon 3) ; passé au lanceur depuis une copie
   (`--verifier-seulement`, comme la contre-lecture 1, section 1 : refus attendu à la garde 22 hors de la machine à `bwrap`) ;
   vérification courte du différentiel ; scellé (`controle_ia.scellement sceller`), committé et poussé sur le dépôt de
   travail avant la course : c'est l'exemplaire qui fait foi (R1), et l'empreinte de ses octets est la racine des graines.
   **Le validateur qui fait foi pour ce texte est le lanceur de l'organisme** (`lire_preenregistrement` du lanceur v66 :
   chemin et nom fixés, sceau, aucun marqueur, 98 empreintes de code, plan gelé, jeu planté, entropie ≥ 2⁶⁴ ; """ + R2253 + """ ;
   contre-lecture 1, Q-4) ; `controle_ia.prereg` n'est sur aucun chemin de cette course et refuse les titres numérotés de ce
   texte, qui ne se renomment pas (le code gelé et les contre-lectures citent leurs numéros) ; la complétude au sens de R1 est
   vérifiée à la main (contre-lecture 1, section 2). Cette règle ne vaut que pour les textes de l'organisme lus par son
   lanceur."""},

    {"id": "B3-19", "section": "12. Ce qui est fait, ce qui reste avant le scellement, et les préalables sur la machine",
     "constat": "CLB-05 ; R-2253",
     "objet": "relais : nombre d'appels au pire cas du devis (calcul), prix du devis, plafonds égaux aux parts, commandes",
     "ancien": """et un `--max-appels` au moins égal au nombre d'appels de son pire cas (devis,
   section 3.4), sans quoi un refus du relais arrête la course (code 3). Les clés ne sont posées que dans l'environnement
   des relais, jamais dans celui du lanceur ni dans un fichier. Valeurs notées au rapport de course.""",
     "nouveau": """et un `--max-appels` **égal au nombre d'appels de son pire cas au devis** (""" + R2253 + """),
   sans quoi un refus du relais arrête la course (code 3). **Calcul** (devis, section 3.4, « chaîne cassée » : 37 cartes
   testées, soit 17 en génération 1 et 12 + 8 en génération 2 ; une session de commande externe compte pour un appel, comme
   au devis, section 3.3, la commande étant lancée une fois par session, `AdaptateurCommandeExterne.lancer`) :
   **Kimi** = 2 sessions de proposeur (une par génération) + 37 cartes × 12 tours d'expérimentateur au plus
   (`TOURS_MAX_PAR_FICHE` = 12, la borne de 0,80 USD par carte du devis) = **446** ; **Argon** = 2 sessions de proposeur
   + 37 cartes × 1 session de vérificateur = **39**. **Prix** (devis, section 2, `devis-boucle-reelle-organisme-v1.md`,
   `60643868de86bb5be71393283e6ecf8dc7c03998a072519bc479af8943a26437`, tous « à vérifier ») : Kimi, 2 USD par million de
   jetons d'entrée et 10 de sortie ; le devis ne donne pas de prix de cache, et le cache est compté au prix d'entrée (2), ce
   qui ne sous-compte jamais ; Argon, barème fixé dans la commande v6 (`PRIX = (10.0, 50.0)`, l. 234), le même que le devis.
   Les clés ne sont posées que dans l'environnement des relais, jamais dans celui du lanceur ni dans un fichier. Relais
   lancés directement (sans enveloppe), arrêtés par leur PID (R10) ; `RELAIS_KIMI` = la copie de `relais_kimi_v3.py` à son
   empreinte ; `CHEMIN_DU_COLLISIONNEUR_V7` = le collisionneur v7 de la machine ; valeurs notées au rapport de course :

   ```
   python3 -I -B RELAIS_KIMI --port 8804 --modeles-permis kimi-k3.1-pro --plafond-usd 33 \\
       --prix-entree 2 --prix-sortie 10 --prix-cache 2 --max-appels 446 --journal JOURNAL_KIMI
   python3 -I -B commandes-v6/commande_argon_v56_nuit_v6.py servir --port 8805 --plafond-usd 7 --max-appels 39 \\
       --journal JOURNAL_ARGON --collisionneur CHEMIN_DU_COLLISIONNEUR_V7 \\
       --sha-collisionneur c9725f025407c3ece3e8c16d19cfdfdec078f084a811f0a3b6ea3209be5d98dc
   ```"""},

    # --- section 13 -----------------------------------------------------------------------------------------------------------
    {"id": "B3-20", "section": "13. Devis", "constat": "CLB-04 (point 2) ; NL-2", "objet": "ligne de GO neuve : mot de Lazar (marqueur)",
     "ancien": """`registres/go.md` : **<<GO_COURSE_V66>>**. Ce qu'elle doit porter""",
     "nouveau": """`registres/go.md` : **<<GO_COURSE_V66>>** (mot de Lazar, verbatim et heure relevée : « <<MOT_LAZAR_NL2>> »). Ce qu'elle doit porter"""},

    {"id": "B3-21", "section": "13. Devis", "constat": "CLB-10 ; R-2253", "objet": "condition de la machine : louée sous cette ligne, validée à blanc avant tout appel payant ; texte nommé",
     "ancien": """machine jetable à `bwrap`
validée par l'essai à blanc `--bac reel` (section 12.3, point 3) ; ce préenregistrement scellé ;""",
     "nouveau": """machine jetable à `bwrap`
**louée sous cette ligne, validée par l'essai à blanc `--bac reel` avant tout appel payant** (section 12.3, point 3) ; ce
préenregistrement scellé (`preenregistrement-boucle-reelle-organisme-v1-v<N>.md`) ;"""},

    # --- section 14 -----------------------------------------------------------------------------------------------------------
    {"id": "B3-22", "section": "14. Portée", "constat": "CLB-04 (point 5)", "objet": "portée : renvoi à la ligne C1",
     "ancien": """retenue en génération 1, elle ne dit rien de la fermeture de la boucle sur un contenu (section 8, nœud NL-1).""",
     "nouveau": """retenue en génération 1, la course ne dit rien de la fermeture de la boucle sur un contenu (section 8, ligne C1)."""},

    # --- section 15 -----------------------------------------------------------------------------------------------------------
    {"id": "B3-23", "section": "15. Contre-lecture (règle R2)", "constat": "CLB-04 (point 7) ; Q-4 ; R-2253",
     "objet": "section 15 réécrite : entrée de la contre-lecture 1 (empreintes, traitement des constats), vérification courte à faire, contre-lectures du code",
     "debut": "**Du texte : à faire**, sur ce brouillon 2,",
     "fin": "de la ligne C1, V-8 et nœud NL-1 ;",
     "nouveau": """**Du texte. Contre-lecture 1** : sous-agent neuf, Claude Fable 5.2 (`claude-fable-5-2`), autre modèle que le rédacteur (N-052 nomme
  Fable 5.1 : écart de version déclaré par le contre-lecteur) ; consigne
  `consigne-contre-lecture-1-prereg-course-v66-b2-v1.md` (`0042d919…`). **Brouillon relu** : brouillon 2,
  `f87ad0e40f1b2941e66d343bfb4b5eeaaefa22a3e2eeb448f852900de112b8a7`. **Rapport** :
  `prereg/contre-lectures/preenregistrement-boucle-reelle-organisme-v1-brouillon2-cl1.md`,
  `90ba927ec9ec390026f3d2dbbab2fe32f1e8ff8bb553f49a15842ce5e420395c` ; couples : `…-cl1-couples.json`,
  `a555f82c659907b273e47b913f0c48a4231a66115883c58d201383c0128ca514`. Verdict : « scellable après les mots de Lazar et
  corrections ». Traitement (décisions de la mère, R-2253 ; brouillon 3 : script `faire-brouillon3-boucle-reelle-v1.py`,
  couples `couples-brouillon3-boucle-reelle-v1.json`, journal `journal-brouillon3-boucle-reelle-v1.md`, dans
  `docs/notes/organisme-boucle-reelle-v1/`, empreintes à leurs compagnons ; brouillon 2 : mêmes noms en « brouillon2 ») :
  - CLB-01, CLB-02, CLB-08 : couples CLC-01 à CLC-03, tels qu'écrits (sections 12.3 et 12.4) ;
  - CLB-03 : couple CLC-04 (une P2 manquée ne change pas l'issue ; mention en tête ; audit A3 : le comportement du
    programme gelé, écrit ; une P2 exigée pour C1 serait un changement de critère, dit à Lazar comme option non recommandée) ;
  - CLB-04 : passages réécrits au brouillon 3 là où ils ne dépendent pas des mots de Lazar ; ceux qui en dépendent portent
    des marqueurs, que le texte candidat règle d'un coup avec les autres passages préparés (journal du brouillon 3) ;
  - CLB-05 : relais nommés, plafonds égaux aux parts, `--max-appels` au pire cas du devis et prix du devis (section 12.3,
    point 6) ;
  - CLB-06 : couple CLC-05 ; CLB-07 : CLC-06 et CLC-07 ; CLB-09 : CLC-08 et CLC-09 ;
  - CLB-10 : condition « machine louée sous cette ligne, validée par l'essai à blanc avant tout appel payant » et nom du
    texte (section 13), et mot demandé à Lazar ;
  - CLB-11 : lettre de la garde 22 (sections 3.7 et 10) ; CLB-12 : information ; CLB-13 : dit à Lazar avec NL-2 ;
  - Q-4 : **le validateur qui fait foi pour ce texte est le lanceur de l'organisme** (section 12.2, point 3).

**Vérification courte du différentiel jusqu'au texte candidat** : à faire, marqueurs remplis, avec le passage du texte au
lanceur depuis une copie.

**Du code : faites**, par Claude Fable 5.2, autre modèle que les développeurs (N-052) ; traitement au texte :
- contre-lecture du code v65 (`code-v65/contre-lecture-code-v65-v2.md`, `c4ddfc7f…`) : « utilisable pour la course après
  corrections » ; CLV65-01 à CLV65-10 corrigés par le code v66 ; CLV65-11 et CLV65-13 traités au passage par le développeur
  v66 (reste, dit : une fausse ou une copie promue en génération 2 est encore testée, section 3.7) ; CLV65-12 (réponses)
  pris ;
- contre-lecture courte du code v66 (`code-v66/contre-lecture-code-v66-courte-v1.md`, `a2880368…`) : « utilisable pour la
  course », code inchangé, sous trois conditions hors du code, toutes portées ici : CLV66-01 (V-3, ligne C5), CLV66-02 (V-1,
  V-2, V-4, ligne C1), CLV66-07 (ligne de GO neuve, section 13). Autres : CLV66-03, vérifications V-4 à V-7 ; CLV66-04, phrase
  de la ligne C1, V-8 et issue de ce cas fixée par Lazar (ligne C1) ;"""},
]


def appliquer(texte: str, c: dict) -> str:
    if "ancien" in c and "debut" not in c:
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
    c["ancien"] = texte[a:b]  # recopié dans le JSON
    return texte[:a] + c["nouveau"] + texte[b:]


def principal(argv=None) -> int:
    a = argparse.ArgumentParser()
    a.add_argument("--depot", required=True)
    a.add_argument("--brouillon3", required=True)
    a.add_argument("--couples", required=True)
    x = a.parse_args(argv)
    depot = Path(x.depot)
    try:
        for s in (Path(x.brouillon3), Path(x.couples)):
            if s.exists():
                raise Arret(f"{s} existe : on n'écrase jamais (R12)")
        lus = {}
        for nom, (rel, sha) in ENTREES.items():
            octets = (depot / rel).read_bytes()
            if h(octets) != sha:
                raise Arret(f"{rel} : empreinte {h(octets)} ≠ {sha} (R11)")
            lus[nom] = octets.decode("utf-8")
        b2 = lus["brouillon2"]
        clc = json.loads(lus["couples_cl1"])["couples"]
        if [c["id"] for c in clc] != IDS_CLC:
            raise Arret(f"couples de la contre-lecture 1 : {[c['id'] for c in clc]} ≠ {IDS_CLC}")
        texte = b2
        for c in clc:
            n = texte.count(c["ancien"])
            if n != 1:
                raise Arret(f"{c['id']} : texte ancien trouvé {n} fois (une exigée)")
            texte = texte.replace(c["ancien"], c["nouveau"], 1)
        sha_clc = h(texte.encode("utf-8"))
        if sha_clc != EMPREINTE_APRES_CLC:
            raise Arret(f"après CLC-01 à CLC-09 : {sha_clc} ≠ {EMPREINTE_APRES_CLC}")
        ids = [c["id"] for c in COUPLES_B3]
        if len(ids) != len(set(ids)):
            raise Arret("identifiants de couples B3 en double")
        for c in COUPLES_B3:
            texte = appliquer(texte, c)
        # contrôles
        if b2.count(DEBUT_16) != 1 or texte.count(DEBUT_16) != 1:
            raise Arret("section 16 absente ou en double")
        if texte[texte.index(DEBUT_16):] != b2[b2.index(DEBUT_16):]:
            raise Arret("section 16 (blocs lus par le lanceur) ≠ celle du brouillon 2")
        restants = {}
        for m in MARQUEUR.findall(texte):
            restants[m] = restants.get(m, 0) + 1
        if restants != MARQUEURS_ATTENDUS:
            raise Arret(f"marqueurs restants {restants} ≠ attendus {MARQUEURS_ATTENDUS}")
        perimes = [p for p in PERIMES if p in texte]
        if perimes:
            raise Arret(f"passages périmés restants : {perimes}")
        sortie = texte.encode("utf-8")
        Path(x.brouillon3).write_bytes(sortie)
        gel = lambda s: s in SECTIONS_GELEES  # noqa: E731
        doc = {"objet": "couples du brouillon 3 du préenregistrement de la course réelle de l'organisme (code v66, configuration v6)",
               "entrees": {k: {"chemin": v[0], "sha256": v[1]} for k, v in ENTREES.items()},
               "sections_gelees": sorted(SECTIONS_GELEES),
               "couples_contre_lecture_1": [dict(c, section=SECTIONS_CLC[c["id"]], gelee=gel(SECTIONS_CLC[c["id"]])) for c in clc],
               "sha256_apres_clc": sha_clc,
               "couples_redacteur_b3": [dict(c, gelee=gel(c["section"])) for c in COUPLES_B3],
               "nombre_de_couples": len(clc) + len(COUPLES_B3),
               "couples_en_section_gelee": [c["id"] for c in clc if gel(SECTIONS_CLC[c["id"]])]
               + [c["id"] for c in COUPLES_B3 if gel(c["section"])],
               "marqueurs_restants": restants,
               "sortie": {"chemin": x.brouillon3, "sha256": h(sortie)}}
        Path(x.couples).write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(json.dumps({"brouillon3_sha256": h(sortie), "sha256_apres_clc": sha_clc, "couples": doc["nombre_de_couples"],
                          "en_section_gelee": doc["couples_en_section_gelee"], "marqueurs": restants},
                         ensure_ascii=False, indent=1))
        return 0
    except Arret as e:
        print(f"arrêt : {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(principal())
