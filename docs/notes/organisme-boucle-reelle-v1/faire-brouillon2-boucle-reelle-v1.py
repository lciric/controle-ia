#!/usr/bin/env python3
"""Préenregistrement de la plus petite course réelle de la boucle complète de l'organisme : fabrication du brouillon 2 (v1).

Écrit par le rédacteur neuf du brouillon 2 (Claude Opus 5.5, sous-agent de la session mère
`session_01VJdZpSMxSdk2SJ1ScmdfNv`), sur la consigne
`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-redaction-prereg-course-v66-b2-v1.md`
(`bfdc52ad…`). Le script fait quatre choses, dans cet ordre, et rien d'autre :

1. il vérifie les empreintes de ses entrées (brouillon 1, blocs du développeur v66) ; toute différence arrête (R11) ;
2. il applique au brouillon 1, dans l'ordre, les couples « texte ancien → texte nouveau » écrits ci-dessous (`COUPLES`) :
   chaque texte ancien doit figurer **une seule fois** dans le texte au moment de son application ; un couple de forme
   « bloc » remplace tout ce qui va du début de `debut` à la fin de `fin` (chacun trouvé une seule fois) ;
3. il porte au texte les trois blocs du développeur v66 (section 16 neuve), **à l'octet**, sauf la ligne `go` du bloc
   `plan-gele-v66`, qui porte le marqueur de la ligne de GO neuve ;
4. il contrôle le résultat : chaque marque de bloc une seule fois ; blocs égaux à ceux du développeur hors la ligne `go` ;
   empreinte des octets JSON du bloc `jeu-plante-v65` égale à `jeu_plante_sha256` du plan ; plan conforme aux règles de forme
   du lanceur v66 (clés, sommes au centime) ; marqueurs restants exactement ceux attendus, avec leur nombre d'occurrences.

Il écrit le brouillon 2 et le fichier des couples (JSON : couples avec section, section gelée ou non, constat d'origine,
textes ancien et nouveau ; empreintes) sous des noms neufs et refuse d'écraser un fichier (R12). Aucun appel réseau, aucun
modèle, aucune écriture git, aucun module de l'organisme importé.

Usage : python3 -I -B faire-brouillon2-boucle-reelle-v1.py --depot DEPOT --brouillon2 SORTIE.md --couples SORTIE.json
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
    "brouillon1": (f"{D}/preenregistrement-boucle-reelle-organisme-v1-brouillon1.md",
                   "736e3fd63ad5ab4e1c5e9f930b0ce33b8a9d26a6ce87be7f0eea231f76e3a2db"),
    "blocs_v66": (f"{D}/code-v66/blocs-v66/blocs-pour-le-texte-v66.md",
                  "9933ee114687079bbf95af94b5e39cd898b69d1d197b4c48587d12692fee1b29"),
}
SECTIONS_GELEES = {"2. Hypothèse", "4. Prédictions chiffrées et signes attendus", "5. Métriques", "6. Seuils",
                   "7. Plan d'analyse", "8. Critères de lecture gelés", "9. Audit de symétrie (règle R4), écrit d'avance",
                   "10. Liste d'arrêt"}
MARQUEUR = re.compile(r"<<[A-Z0-9_-]+>>")  # même motif que le lanceur v66 (`MARQUEUR`)
MARQUEURS_ATTENDUS = {"<<GO_COURSE_V66>>": 3, "<<NOEUD_C1_SANS_RETENUE>>": 1}
LIGNE_GO_DEVELOPPEUR = "go: GO-2026-11-08-02\n"
LIGNE_GO_TEXTE = "go: <<GO_COURSE_V66>>\n"
MARQUES = ("<!-- empreintes-du-code-v66 : début -->", "<!-- empreintes-du-code-v66 : fin -->",
           "<!-- plan-gele-v66 : début -->", "<!-- plan-gele-v66 : fin -->",
           "<!-- jeu-plante-v65 : début -->", "<!-- jeu-plante-v65 : fin -->")
CLES_PLAN = {"generations", "cartes_par_proposeur", "m_e_bh", "bras", "d9", "plafond_modeles_usd", "plafond_kimi_usd",
             "plafond_argon_usd", "plafond_machine_usd", "go", "go_montant_usd", "duree_h", "configuration_sha256",
             "monde_sha256", "jeu_plante_sha256", "heritage_depart_sha256"}
ATTENDU_PLAN = {"generations": "2", "cartes_par_proposeur": "6", "m_e_bh": "22", "bras": "reel_seul", "d9": "mecanique",
                "plafond_modeles_usd": "40", "plafond_kimi_usd": "33", "plafond_argon_usd": "7", "plafond_machine_usd": "5",
                "go": "<<GO_COURSE_V66>>", "go_montant_usd": "45", "duree_h": "72",
                "configuration_sha256": "4743ddbe4d294643ac8e1924476dec056b1a08dac9f8010cd647dd1861160b0d",
                "monde_sha256": "fdf4d5c1ca0d2971b416ee5f694deff7a4696fe5defb3a6a1843dffef1231877",
                "jeu_plante_sha256": "21b4b0058672deb36a2312370324f2fcc5065576f18f2b69a97eda84f84eb41e",
                "heritage_depart_sha256": "93dcf51715f7a1aa4f313e9e1761c5a375a275d572ffcdb6969fbfaf2fb623c1"}
NOMBRE_FICHIERS_GELES = 98


class Arret(Exception):
    pass


def h(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


# ---------------------------------------------------------------------------------------------------------------------------
# Couples. Forme : {"id", "section", "constat", "objet", "ancien", "nouveau"} (ancien exact, trouvé une fois) ou
# {"id", "section", "constat", "objet", "debut", "fin", "nouveau"} (bloc du début de `debut` à la fin de `fin`).
# « section » : titre de la section de niveau 2 touchée (tel qu'au brouillon 1) ; la section gelée est déduite.
# ---------------------------------------------------------------------------------------------------------------------------

COUPLES = [
    # --- en-tête ------------------------------------------------------------------------------------------------------------
    {"id": "B2-01", "section": "titre", "constat": "brouillon 2", "objet": "titre : brouillon 2",
     "ancien": "l'organisme d'idéation, brouillon 1\n",
     "nouveau": "l'organisme d'idéation, brouillon 2\n"},

    {"id": "B2-02", "section": "en-tête", "constat": "brouillon 2 ; CLV66-04 ; CLV66-07", "objet": "statut du brouillon 2, marqueurs restants, ce qui précède toute course",
     "debut": "**Statut : brouillon 1, non contre-lu, non scellé.",
     "fin": "un feu vert de dépense du directeur sur le devis (`devis-boucle-reelle-organisme-v1.md`).**",
     "nouveau": """**Statut : brouillon 2, texte non contre-lu (règle R2), non scellé : il ne vaut pas préenregistrement (R1).** Il porte
au brouillon 1 (gardé intact, `736e3fd6…`) les couples du rédacteur du brouillon 2, appliqués par programme (script, couples
et journal nommés en section 15) : blocs gelés du code v66 (section 16), clauses de lecture des constats CLV66-01 à CLV66-04
de la contre-lecture du code v66 (section 8), ligne de GO neuve (section 13), préalables sur la machine (section 12).
**Marqueurs restants** (liste et nombre d'occurrences au journal ; le lanceur refuse tout texte qui en porte un) :
`GO_COURSE_V66` (identifiant de la ligne de GO neuve que Lazar doit inscrire : sections 12.4, 13 et 16) et
`NOEUD_C1_SANS_RETENUE` (nœud de Lazar sur l'issue C1 quand la génération 1 ne retient aucune carte réelle : section 8).
**Aucune course réelle avant** : (i) la décision de Lazar sur ce nœud ; (ii) la ligne de GO neuve à identifiant neuf,
inscrite par Lazar ; (iii) la contre-lecture de ce texte par un sous-agent neuf (R2) ; (iv) le scellement, le dépôt du texte
scellé et sa copie à l'octet dans l'arbre de l'organisme (section 12.2) ; (v) les six préalables sur la machine à `bwrap`
(section 12.3). Le code v66 est écrit, essayé et contre-lu (section 12.1)."""},

    {"id": "B2-03", "section": "en-tête", "constat": "brouillon 2", "objet": "rédacteurs des brouillons 1 et 2",
     "ancien": """- **Rédacteur** : Claude Opus 5.5 (`claude-opus-5-5`), rédacteur neuf : je n'ai écrit aucune pièce de l'organisme ni du
  programme de contrôle (texte scellé, code, analyse, verdict).""",
     "nouveau": """- **Rédacteurs** : brouillon 1, Claude Opus 5.5 (`claude-opus-5-5`), rédacteur neuf, qui n'avait écrit aucune pièce de
  l'organisme ni du programme de contrôle (texte scellé, code, analyse, verdict) ; le « je » des sections 1 à 4 est le sien.
  **Brouillon 2** : Claude Opus 5.5 (`claude-opus-5-5`), rédacteur neuf, sous-agent de la session mère
  `session_01VJdZpSMxSdk2SJ1ScmdfNv`, qui n'a écrit ni le brouillon 1, ni le code v65 ou v66, ni leurs contre-lectures, ni le
  devis, la puissance ou l'essai à blanc v1 ; il n'a lancé aucun essai, aucun appel de modèle, aucune dépense."""},

    {"id": "B2-04", "section": "en-tête", "constat": "brouillon 2", "objet": "heures du brouillon 2",
     "ancien": """- **Heures** (temps universel, `date -u`, 7 novembre 2026) : début de la tâche 23:23:40 ; brouillon écrit de 23:44 à 23:54
  (dernière retouche relevée à 23:53:18).""",
     "nouveau": """- **Heures** (temps universel, relevées par `date -u`) : brouillon 1, 7 novembre 2026, début de la tâche 23:23:40,
  brouillon écrit de 23:44 à 23:54 (dernière retouche relevée à 23:53:18) ; brouillon 2, 10 novembre 2026, début de la tâche
  14:29:39, couples écrits à partir de 14:41:50 (heure de fin au journal du brouillon 2)."""},

    {"id": "B2-05", "section": "en-tête", "constat": "brouillon 2 ; CLV66-07", "objet": "consigne du brouillon 2, lignes de GO et de registre",
     "ancien": """  moyenne, environ 0,6. : go ». Inscrit en R-1735 (`registres/decisions.md`, même commit).""",
     "nouveau": """  moyenne, environ 0,6. : go ». Inscrit en R-1735 (`registres/decisions.md`, même commit).
- **Consigne du brouillon 2** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-redaction-prereg-course-v66-b2-v1.md`
  (`bfdc52ad2309636e42f28cc565a8e4e9c1a94c1b89a229224b4c000f90f9ac6d`, vérifiée), lancée en R-2244.
- **Lignes de GO qui touchent la course** (`registres/go.md` lu à `2c396b016d4ab86bd3f09cc7e21173f19d0c9765cc1a85b8efc08e59c2bc39f0`) :
  GO-2026-11-08-02 (D1 bras réel seul, D2 génération 2 complète, D3 plafond de 40 USD de modèles, Kimi 33 et Argon 7, et 5 USD
  de machine ; « après le code v65 contre-lu, la machine à bac à sable `bwrap` et le préenregistrement scellé ») ;
  GO-2026-11-10-10 (enveloppe de 120 USD ; part « organisme » 45 USD ; « code v65 contre-lu », « configuration v5
  (`995eb918…`) »). **Ni l'une ni l'autre ne suffit telle qu'écrite** pour une course au code v66 et à la configuration v6
  (contre-lecture du code v66, CLV66-07) : la course demande une ligne neuve (section 13).
- **Registre** (`registres/decisions.md`) : R-1738 (brouillon 1 et devis) ; R-2206 (enveloppe de 120 USD) ; R-2215
  (contre-lecture du code v65 ; v66 décidée) ; R-2220 et R-2234 (configuration `995eb918…` introuvable ; code v66 rendu) ;
  R-2243 (contre-lecture courte du code v66 : « utilisable pour la course ») ; R-2244 (ce brouillon lancé). Décisions de
  Lazar lues : N-058 (composition jugée sur l'oracle et le coût), N-064, N-065 (section 1)."""},

    {"id": "B2-06", "section": "en-tête", "constat": "brouillon 2", "objet": "arbres du brouillon 2 ; code v66",
     "ancien": """- **Arbre** : `/home/user/wt-boucle`, branche `prep/organisme-boucle-reelle-v1`, partie de `main` à `b014b784`. Dépôt de
  l'organisme lu seulement : `/home/user/ideation-organism`, commit `94bfd92`.""",
     "nouveau": """- **Arbres** : brouillon 1, `/home/user/wt-boucle`, branche `prep/organisme-boucle-reelle-v1`, partie de `main` à
  `b014b784` ; dépôt de l'organisme lu seulement : `/home/user/ideation-organism`, commit `94bfd92`. **Brouillon 2** : dépôt de
  travail `/home/user/controle-ia-travail`, `main` à `b33ed3ef` ; arbre de l'organisme `/home/user/organisme-v65-cl`, branche
  locale `prep/organisme-v66-boucle-reelle-v1`, tête **`7e415cbaaa3ff602db43a44dad6b4307c08352c7`** (code v66 ; parents
  `cef5ea60`, code v65, puis `94bfd92`), lu par `git show` seulement ; jamais poussé (paquet git versé :
  `code-v66/organisme-v66-boucle-reelle-v1.bundle`, `84ab119f0b3eefdd689b4be03f03bb776ebd2c7c1247b9d76e903181a419b1bc`)."""},

    # --- documents qui font foi -----------------------------------------------------------------------------------------------
    {"id": "B2-07", "section": "Documents qui font foi (chemin, empreinte sha256)", "constat": "brouillon 2",
     "objet": "pièces de l'organisme : code v66 et v65 réutilisé",
     "ancien": """Dépôt de l'organisme (commit `94bfd92`) :""",
     "nouveau": """Dépôt de l'organisme (commit `94bfd92` ; les rangées neuves du brouillon 2, en fin de table, à la tête `7e415cba`. Les
commits v65 et v66 n'ajoutent que des fichiers neufs : les pièces du commit `94bfd92` ont la même empreinte à `7e415cba`, et
les 98 fichiers gelés de la course sont au bloc `empreintes-du-code-v66`, section 16) :"""},

    {"id": "B2-08", "section": "Documents qui font foi (chemin, empreinte sha256)", "constat": "brouillon 2",
     "objet": "rangées neuves : code v66, v65 réutilisé, configuration v6",
     "ancien": """| monde planté | `orchestrator/exemples/temoins-pari-demo-v1.json` | `fdf4d5c1ca0d2971b416ee5f694deff7a4696fe5defb3a6a1843dffef1231877` |""",
     "nouveau": """| monde planté | `orchestrator/exemples/temoins-pari-demo-v1.json` | `fdf4d5c1ca0d2971b416ee5f694deff7a4696fe5defb3a6a1843dffef1231877` |
| cœur de la course v66 (jugements écrits au relevé dès la sortie du juge ; vue servie vérifiée, garde 23 ; garde 7 complète ; mesures) | `orchestrator/pole/boucle_reelle_v66.py` | `ea17a4b8645ab4fc81df4702479fbdcd7ced912d9575190779b23fc334fb45b6` |
| cœur v65, réutilisé sans changement (jeu planté, héritage de départ, gardes 17 à 21, copies) | `orchestrator/pole/boucle_reelle_v65.py` | `5d20d9fb4d8bc53ff6c4ffb8f3f2442200c8d51c9075828cd183277cdbe8ff13` |
| lecture gelée v66 (complétude, C1 à C6, A1 à A4, mesures sans issue) | `orchestrator/pole/lecture_boucle_reelle_v66.py` | `0152103a9f2b33271eddfb6493368e387d5a6c5ade010e217c7abdfda43d52c6` |
| lecteur du registre des GO v66 (règle de la garde de calcul ; GO à extension refusé ; part d'enveloppe) | `orchestrator/pole/registre_go_v66.py` | `4541ef7f53e2210bff7f74e1872ac46a10b29fda30f9cf4db568a99b03c04b4c` |
| lanceur de la course v66 | `orchestrator/demonstrations/boucle_reelle_v66.py` | `e2dd83ab6e4542de7c40ac4b5d59d8d817950d8327f4f9c4c595bb9b0f129d6b` |
| programme de lecture gelée v66 | `orchestrator/demonstrations/lire_boucle_reelle_v66.py` | `e2183565c5867255addf0c74d6de9f1498e3129ded1161e1cf0c6f5f96844db8` |
| configuration v6 (commandes v6 et pièces par chemins relatifs, sans GO) | `orchestrator/exemples/configuration-boucle-reelle-v6.json` | `4743ddbe4d294643ac8e1924476dec056b1a08dac9f8010cd647dd1861160b0d` |"""},

    {"id": "B2-09", "section": "Documents qui font foi (chemin, empreinte sha256)", "constat": "brouillon 2 ; N-064 ; N-065",
     "objet": "pièces du dépôt de travail : code v66, contre-lectures, dossier de course, N-064, N-065",
     "ancien": """| configuration du tour fermé v4 (fournisseurs, barème prudent) | `docs/notes/ideation-organisme-v1/tour-ferme-etage1-v1/configuration-tour-ferme-v4.json` | `15b34adf9329a33d9f8135160a6ea2443dc17ce786dc28fa0b5c61c4560a2e6b` |""",
     "nouveau": """| configuration du tour fermé v4 (fournisseurs, barème prudent) | `docs/notes/ideation-organisme-v1/tour-ferme-etage1-v1/configuration-tour-ferme-v4.json` | `15b34adf9329a33d9f8135160a6ea2443dc17ce786dc28fa0b5c61c4560a2e6b` |
| contre-lecture du code v65 (brouillon 2 ; `main` à `b33ed3ef` pour cette rangée et les suivantes) | `docs/notes/organisme-boucle-reelle-v1/code-v65/contre-lecture-code-v65-v2.md` | `c4ddfc7ffd4b5cea1b0eb70e2a08ea551c8a8e8ef6f1a169ef8bebdab976ed03` |
| rapport du développeur v66 | `docs/notes/organisme-boucle-reelle-v1/code-v66/rapport-developpeur-organisme-v66-v1.md` | `f6433d38c701934b6c2d04ed7011a4864088af4e4cb36e5b01f5ffdced62bd59` |
| blocs pour le texte v66 (section 16) | `docs/notes/organisme-boucle-reelle-v1/code-v66/blocs-v66/blocs-pour-le-texte-v66.md` | `9933ee114687079bbf95af94b5e39cd898b69d1d197b4c48587d12692fee1b29` |
| héritage de départ (génération 0, archive {K1}) | `docs/notes/organisme-boucle-reelle-v1/code-v66/blocs-v66/heritage-depart-v65.json` | `93dcf51715f7a1aa4f313e9e1761c5a375a275d572ffcdb6969fbfaf2fb623c1` |
| dossier de course v6 : configuration, `pieces/` (six pièces de la v4), `commandes-v6/` (commit `12f9e0e3` de `outils/commandes-tour-ferme-v1`, R-1129, octet pour octet) | `docs/notes/organisme-boucle-reelle-v1/code-v66/configuration-v6/` | configuration `4743ddbe…` ; `commande_kimi_v6.py` `889309305aeb37de9801c2f40c31769fd268abded1ac61ea94196fd0d51195ae` ; `commande_argon_v56_nuit_v6.py` `5eae1a0468430e243c3c4e099b3969f949f62add688531aafdd7f0f44e036e55` ; `registre_depense_cumulee_v1.py` `8ba92066b358ffb8206dea9e70251388c30620484fab1ac578778d9f21e578ff` |
| contre-lecture courte du code v66 (« utilisable pour la course ») | `docs/notes/organisme-boucle-reelle-v1/code-v66/contre-lecture-code-v66-courte-v1.md` | `a28803689558e6813f24f625915c823b6a8c1c17802e351ae3f0f4dd9d3b7b00` |
| décision N-064 (revendication O2 resserrée ; citations obligatoires) | `docs/decisions/decision-N-064-v1.md` | `387c9d4eda5a1b3d0e8ec61def715bb88c1bf9883081d5796ea291879be63f97` |
| décision N-065 (place de l'organisme dans le programme) | `docs/decisions/decision-N-065-v1.md` | `f820e90da0920d505d22bc7b33fad4906181d43bd5af7e79418a3c161a8a65c4` |"""},

    {"id": "B2-10", "section": "Documents qui font foi (chemin, empreinte sha256)", "constat": "brouillon 2",
     "objet": "pièces versées depuis le brouillon 1",
     "ancien": """(`fe2bc5027cd4f4eb7f4a96f286b7b37687b7b8fcfe608da3e186b75d75e7c111`) ; essai à blanc `essai-a-blanc-v1/` (journal, script,
copies des sorties).""",
     "nouveau": """(`fe2bc5027cd4f4eb7f4a96f286b7b37687b7b8fcfe608da3e186b75d75e7c111`) ; essai à blanc `essai-a-blanc-v1/` (journal, script,
copies des sorties). Versées depuis, chacune avec son compagnon `.sha256` : `code-v65/` (contre-lecture du code v65) ;
`code-v66/` (rapport du développeur, blocs, dossier de course `configuration-v6/`, essai à blanc v66 en 14 étapes, suite,
banc de mutations, paquet git et patch, contre-lecture courte du code v66) ; le brouillon 2, ses couples, son script et son
journal (section 15)."""},

    # --- section 0 ------------------------------------------------------------------------------------------------------------
    {"id": "B2-11", "section": "0. En dix lignes", "constat": "CLV66-04", "objet": "preuve de lecture de la sélection vide sans carte retenue",
     "ancien": """   si et seulement si la sélection est lue (section 3.7).""",
     "nouveau": """   si et seulement si la sélection est lue (section 3.7). **Sans carte réelle retenue en génération 1, cette preuve est
   vide** (la génération 2 lit une sélection vide) : la phrase de résultat le dit en tête, et l'issue de ce cas attend un nœud
   de Lazar (section 8, NL-1)."""},

    {"id": "B2-12", "section": "0. En dix lignes", "constat": "brouillon 2", "objet": "ce qui manque avant de sceller",
     "ancien": """8. **Ce qui manque avant de sceller** : le code v65 (héritage de départ, jeu planté, lois plantées jugées avec l'archive,
   bras réel seul, lecture gelée), les commandes v6 des relais versées dans l'arbre, et une machine avec `bwrap` (section 12).""",
     "nouveau": """8. **Ce qui manque avant de sceller** (section 12) : le code est fait (v66, tête `7e415cba`, contre-lu « utilisable pour
   la course » ; configuration v6 `4743ddbe…` ; blocs gelés en section 16) ; restent le nœud de Lazar sur C1 sans carte
   retenue (section 8), la ligne de GO neuve (section 13), la contre-lecture de ce texte et son scellement ; puis, avant le
   lancement, la machine à `bwrap` et ses six préalables (section 12.3)."""},

    # --- section 1 ------------------------------------------------------------------------------------------------------------
    {"id": "B2-13", "section": "1. Question, motivation, ce qui existe", "constat": "brouillon 2",
     "objet": "ce qui existe depuis le brouillon 1 : code v65, v66, contre-lectures",
     "ancien": """  aucun repli) ; 169 essais réussis.""",
     "nouveau": """  aucun repli) ; 169 essais réussis.

**Écrit pour cette course depuis le brouillon 1** (code neuf sous des noms neufs ; le code ci-dessus reste intact) : le code
v65 (pièces M1 à M5, commit `cef5ea60`), contre-lu « utilisable pour la course après corrections » (CLV65-01 à CLV65-13),
puis le code v66 (tête `7e415cba`, onze fichiers neufs, v65 intacte), qui corrige CLV65-01 à CLV65-10 : suite touchée 323
essais passés et 4 sautés (les essais du vrai bac à sable), banc de 133 mutations toutes tuées pour la raison attendue, essai
à blanc v66 en 14 étapes aux codes attendus ; le tout rejoué à l'identique par la contre-lecture courte du code v66
(« utilisable pour la course », code inchangé ; `a2880368…`). Reste non éprouvé faute de `bwrap` : la sonde réelle, l'identité
64097 du bac, les essais du vrai bac, l'étage au moteur réel (section 12.3)."""},

    {"id": "B2-14", "section": "1. Question, motivation, ce qui existe", "constat": "N-064 ; N-065",
     "objet": "voisins publiés cités (N-064, point 4) ; place de l'organisme (N-065)",
     "ancien": """test de mort) ; une archive de départ non vide.""",
     "nouveau": """test de mort) ; une archive de départ non vide.

**Voisins publiés, cités comme l'exige N-064 (point 4) dans tout texte qui présente l'organisme** (références et pages
recopiées de N-064, `387c9d4e…`, non relues pour ce texte ; aucun chiffre n'en est tiré, R7) : POPPER (Huang, Jin, Li, Li,
Candès, Leskovec, ICML 2025, PMLR 267, p. 2-5 et algorithme 1 p. 14 : e-valeurs et seuil posés hors des agents, zone occupée
en partie) ; Dwork et al. (arXiv 1506.02629, p. 20-21) et Blum et Hardt (« The Ladder », arXiv 1502.04585, p. 10-12) : un
analyste adaptatif qui trompe une réserve de test ; Co-Scientist (Nature 655, p. 487-496), voisin de la boucle
générer-classer-faire évoluer. Ce texte ne revendique aucune priorité : il éprouve la plomberie d'un dessin existant. **Place
dans le programme** (N-065, `f820e90d…`) : l'organisme est un second terrain du papier C et un atelier d'idées ; ses fiches
sont du matériau, jamais une preuve ; aucun score d'un moniteur du programme n'entre dans sa sélection (rappel de N-053)."""},

    # --- section 3 (dessin) ---------------------------------------------------------------------------------------------------
    {"id": "B2-15", "section": "3. Dessin", "constat": "brouillon 2", "objet": "règle des lois plantées : juge v65 et v66",
     "ancien": """(règle « hors famille »
  de `tour_ferme_v64.juger`).""",
     "nouveau": """(règle « hors famille »
  de `tour_ferme_v64.juger`, reprise avec l'archive de la génération par `boucle_reelle_v65.juger_v65` et
  `boucle_reelle_v66.juger_v66`)."""},

    {"id": "B2-16", "section": "3. Dessin", "constat": "CLV65-09 ; rapport v66, section 9", "objet": "utilisateur 64097, lanceur en superutilisateur",
     "ancien": """  de superutilisateur, utilisateur dédié sans privilège sur l'hôte (par exemple 64097) avec son dossier racine en 0700,""",
     "nouveau": """  de superutilisateur dans le bac, utilisateur dédié sans privilège sur l'hôte, **64097** (`--utilisateur-bac 64097` ; le
  lanceur tourne **en superutilisateur**, seul moyen de passer à l'utilisateur dédié par `setpriv`, et vérifie après la sonde
  que l'identité du script sur l'hôte est 64097 : garde 22), avec son dossier racine en 0700,"""},

    {"id": "B2-17", "section": "3. Dessin", "constat": "CLV65-03 ; CLV65-13 ; CLV66-08",
     "objet": "génération 2 : vue servie vérifiée (garde 23) ; lois plantées promues aussi testées (cas de brèche)",
     "ancien": """retenues) ; (ii) sert aux proposeurs la vue {K1} plus les lois retenues ; (iii) deux appels de proposeurs, gardien, juge
  avec l'archive {K1} plus retenues ; tests de mort des seules cartes réelles promues ;""",
     "nouveau": """retenues) ; (ii) sert aux proposeurs la vue {K1} plus les lois retenues (vérifiée au moment du service et consignée au
  relevé : garde 23) ; (iii) deux appels de proposeurs, gardien, juge avec l'archive {K1} plus retenues ; tests de mort des
  cartes réelles promues (et, comme le fait le code v66, de toute loi plantée promue : cas de brèche seulement, compté au
  devis, section 3.4 du devis ; l'issue C2 ou C4 se lit sur la promotion, non sur la survie) ;"""},

    # --- section 4 (gelée) ----------------------------------------------------------------------------------------------------
    {"id": "B2-18", "section": "4. Prédictions chiffrées et signes attendus", "constat": "CLV65-03",
     "objet": "P6 : la vue comparée est la vue servie (garde 23) ; aucun signe ni seuil changé",
     "ancien": """| P6 | lecture de la sélection : empreinte lue = écrite ; vue = {K1} ∪ retenues ;""",
     "nouveau": """| P6 | lecture de la sélection : empreinte lue = écrite ; vue servie aux proposeurs (consignée au moment du service, garde 23) = {K1} ∪ retenues ;"""},

    # --- section 5 (gelée) ----------------------------------------------------------------------------------------------------
    {"id": "B2-19", "section": "5. Métriques", "constat": "CLV65-03 ; CLV66-02", "objet": "lecture de la sélection : empreinte relue sur disque, vue servie, vérifications V",
     "ancien": """- **Lecture de la sélection** : égalité des empreintes ; identité ensembliste vue = {K1} ∪ retenues ; nombre de membres
  d'archive par carte ; issue des copies (P5).""",
     "nouveau": """- **Lecture de la sélection** : égalité des empreintes (écrite, lue, relue sur disque) ; identité ensembliste vue servie =
  {K1} ∪ retenues ; nombre de membres d'archive par carte et par loi plantée ; issue des copies (P5) ; vérifications V-1 à
  V-8 du lecteur du verdict (section 8)."""},

    {"id": "B2-20", "section": "5. Métriques", "constat": "CLV65-08 ; rapport v66, section 9", "objet": "intervalles de Wilson : les six parts par fournisseur de P7",
     "ancien": """- **Intervalles** : Wilson à 95 % pour les parts ; aucune moyenne sur des jetons.""",
     "nouveau": """- **Intervalles** : Wilson à 95 % pour les parts (z = 1,959964 ; `lecture_boucle_reelle_v66.wilson`) : celles de la
  simulation (section 4.2) et, pour P7, **six parts par fournisseur** : refusées au gardien sur proposées, promues sur
  proposées, survivantes sur testées, retenues sur proposées, vraies découvertes sur promues, fausses découvertes sur promues ;
  une part de dénominateur nul n'a pas d'intervalle, et c'est dit. Aucune moyenne ni médiane sur des jetons."""},

    {"id": "B2-21", "section": "5. Métriques", "constat": "CLV65-08 ; rapport v66, section 9", "objet": "jetons : champ usage des commandes, sommes par relais",
     "ancien": """- **Coût** : dollars par rôle et par fournisseur relevés au registre cumulé des relais ; appels ; jetons d'entrée et de sortie.""",
     "nouveau": """- **Coût** : dollars par rôle et par fournisseur relevés au registre cumulé des relais ; appels ; jetons d'entrée et de
  sortie **par appel**, lus dans le champ `usage` de la dernière ligne JSON que rend chaque commande externe (Kimi :
  `prompt_tokens` et `completion_tokens` ; Argon : `promptTokenCount` à l'entrée, `candidatesTokenCount` plus
  `thoughtsTokenCount` à la sortie), **sommés par relais** ; un appel sans champ `usage` est compté à part (« sans usage »),
  jamais estimé. Mesure sans issue, jamais vue sur une sortie réelle avant la course (section 12.3)."""},

    # --- section 7 (gelée) ----------------------------------------------------------------------------------------------------
    {"id": "B2-22", "section": "7. Plan d'analyse", "constat": "CLV65-11 ; CLV66-01 à CLV66-04",
     "objet": "ordre : programme de lecture v66, empreinte du relevé exigée, oracle lu, vérifications V",
     "ancien": """   promues, copies et fausses replantées, sélection scellée) → relevé scellé → lecture gelée par un programme à part, par un
   lecteur neuf (règle R13).""",
     "nouveau": """   promues, copies et fausses replantées, sélection scellée) → relevé scellé (`SORTIE/boucle-reelle-v66.json`) → lecture
   gelée par le programme à part `demonstrations/lire_boucle_reelle_v66.py SORTIE LECTURE.json --releve-sha256 <empreinte du
   relevé>` (empreinte **exigée** ; **sans** `--sans-oracle`, l'oracle étant lu une seule fois pour P7 et pour la fausse
   découverte d'une carte réelle), par un lecteur neuf (règle R13), qui applique ensuite au relevé brut les vérifications V-1
   à V-8 de la section 8 avant d'écrire l'issue."""},

    {"id": "B2-23", "section": "7. Plan d'analyse", "constat": "CLV65-08 ; rapport v66, section 9",
     "objet": "recherche de la loi plantée : échos de la loi gelée ; lignes de tranche servies",
     "ancien": """   touché hors de la loi gelée servie au test de mort (que l'expérimentateur doit voir).""",
     "nouveau": """   touché hors de la loi gelée servie au test de mort (que l'expérimentateur doit voir). Comptage (code v66, `EtageMesure`
   et `consigne_sans_loi_gelee`) : dans une consigne de l'étage, la loi gelée qui suit sa marque est comptée « dans la loi
   gelée », à part ; **ses échos** (la même loi recopiée ailleurs dans la consigne, par exemple dans un script précédent de
   l'expérimentateur) sont comptés « dans » s'ils sont écrits en JSON canonique (tel quel, échappé une ou deux fois), **« hors »
   sinon** ; toute touche « hors » est relue à la main avant d'être lue comme une fuite, et la relecture est écrite au
   rapport. Mesure aussi (reprise de la v64) : les **lignes de la tranche présentes dans les contextes servis aux
   proposeurs**, comparées à six décimales ; mesure sans issue."""},

    # --- section 8 (gelée) ----------------------------------------------------------------------------------------------------
    {"id": "B2-24", "section": "8. Critères de lecture gelés", "constat": "CLV66-01 ; CLV66-02 ; CLV66-03 ; CLV66-04",
     "objet": "programme et texte : l'issue du texte prime ; vérifications V-1 à V-8 du lecteur du verdict",
     "ancien": """Lus dans cet ordre ; la première ligne qui s'applique donne l'issue.""",
     "nouveau": """Lus dans cet ordre ; la première ligne qui s'applique donne l'issue.

**Programme et texte.** Le programme de lecture gelé v66 (`pole/lecture_boucle_reelle_v66.py`, `0152103a…`, appelé par
`demonstrations/lire_boucle_reelle_v66.py`, `e2183565…`) calcule ces lignes ; il exige la complétude du relevé avant toute
issue autre que C5 (`completude` : chaque manque écrit dans `cause_c5`). **Les issues sont celles de ce texte.** Avant
d'écrire l'issue, le lecteur du verdict (R13) applique au relevé brut (champ `releve` du fichier de course, à l'empreinte
donnée au programme) les vérifications V-1 à V-8 écrites sous la table, sous toute issue, C5 comprise (V-3 n'a d'objet qu'en
cas d'arrêt), et recopie au verdict, pour chacune, les champs lus et le résultat. Un manque relevé par une vérification compte comme un manque de complétude (C5) ; un écart, comme un écart de
P6 (C4, ou « C4 (partielle) » sous C5) ; l'issue se relit alors dans l'ordre de la table. **Quand le programme et ces
vérifications divergent, l'issue du texte prime** ; le verdict écrit les deux et la raison. Aucune issue autre que C5 ne se
prononce sans les huit vérifications recopiées au verdict."""},

    {"id": "B2-25", "section": "8. Critères de lecture gelés", "constat": "CLV65-01 ; CLV66-01 ; contre-lecture v66, section 3",
     "objet": "ligne C5 : relevé incomplet défini ; arrêt de la garde 18 en génération 2 lu C5 et « C4 (partielle) » ; écart de membres en génération 2 lu C4",
     "ancien": """| C5 | course arrêtée (code 3) ou relevé incomplet | **« non jugeable (arrêt) »** | rien sur la chaîne ; chiffres partiels rapportés comme tels ; cause écrite (infrastructure ou garde) ; **si le relevé partiel montre déjà une fausse ou une copie promue, ou une lecture de sélection en écart, C2 ou C4 s'écrit aussi, marquée « partielle »** : un arrêt ne masque jamais une brèche |""",
     "nouveau": """| C5 | course arrêtée (code 3) ; ou relevé incomplet : un manque de `completude` (programme), ou un manque relevé par V-1, V-2, V-5 ou V-7 | **« non jugeable (arrêt) »** | rien sur la chaîne ; chiffres partiels rapportés comme tels ; cause écrite (infrastructure ou garde ; manques du relevé) ; **si le relevé partiel montre déjà une fausse ou une copie promue, ou une lecture de sélection en écart, C2 ou C4 s'écrit aussi, marquée « partielle »** : un arrêt ne masque jamais une brèche. **Un arrêt de la garde 18 en génération 2** (V-3) se lit C5, cause écrite, **et « C4 (partielle) »** : la génération 2 a jugé ses lois plantées avec une autre archive que celle qu'impose {K1} ∪ retenues, ce qui est un écart de P6 ; le verdict et le rapport le disent, que le programme l'écrive ou non (contre-lecture du code v66, CLV66-01). En génération 1, un arrêt de la garde 18 se lit C5 seul, cause écrite. **En génération 2, une loi plantée ou une carte jugée sans arrêt avec un autre nombre de membres d'archive que celui qu'impose {K1} ∪ retenues relève de P6 (C4), non du relevé incomplet** |"""},

    {"id": "B2-26", "section": "8. Critères de lecture gelés", "constat": "CLV65-03 ; CLV66-02 ; CLV66-03",
     "objet": "ligne C4 : vue servie ; écarts relevés par V-4, V-5, V-6",
     "ancien": """| C4 | P6 manquée (empreinte lue ≠ écrite, vue ou archive de la génération 2 ≠ {K1} ∪ retenues), ou une copie de la génération 2 promue |""",
     "nouveau": """| C4 | P6 manquée (empreinte lue ≠ écrite, vue servie ou archive de la génération 2 ≠ {K1} ∪ retenues, écart relevé par V-4, V-5 ou V-6), ou une copie de la génération 2 promue |"""},

    {"id": "B2-27", "section": "8. Critères de lecture gelés", "constat": "CLV66-02 ; CLV66-04",
     "objet": "ligne C1 : V-1 à V-7 exigées ; sélection de la génération 1 vide dite en tête ; nœud de Lazar",
     "ancien": """| C1 | P1, P4 et P6 tenues | **« la chaîne garde (classe couverte, ce monde, cette taille) »** | ouvre la proposition au directeur de plusieurs générations ; ne dit rien de la classe non couverte ni des données réelles |""",
     "nouveau": """| C1 | P1, P4 et P6 tenues, **et** V-1 à V-7 tenues : le relevé porte la lecture de la sélection (sans refus ; empreinte écrite = lue = relue sur disque) et l'archive de jugement de la génération 2 ; sinon C5 (manque) ou C4 (écart) | **« la chaîne garde (classe couverte, ce monde, cette taille) »** | ouvre la proposition au directeur de plusieurs générations ; ne dit rien de la classe non couverte ni des données réelles. **Si aucune carte réelle n'est retenue en génération 1** (V-8), la génération 2 a lu une sélection vide et la phrase de résultat porte en tête : « sélection de la génération 1 vide : la lecture de la sélection par la génération 2 (H-boucle (c), P5, P6) n'est pas éprouvée sur un contenu » ; l'issue de ce cas attend la décision de Lazar (nœud NL-1 du journal du brouillon 2) : <<NOEUD_C1_SANS_RETENUE>> |"""},

    {"id": "B2-28", "section": "8. Critères de lecture gelés", "constat": "CLV66-01 ; CLV66-02 ; CLV66-03 ; CLV66-04",
     "objet": "table des vérifications V-1 à V-8 du lecteur du verdict sur le relevé brut",
     "ancien": """Mesures sans issue : P3 (puissance aux vraies faibles)""",
     "nouveau": """**Vérifications du lecteur du verdict sur le relevé brut** (champs du relevé `releve` de `SORTIE/boucle-reelle-v66.json`).
Elles ferment les cas où la lecture gelée tiendrait P6 à vide ou tairait un écart. D'après la contre-lecture du code v66
(CLV66-01 à CLV66-03), aucun de ces cas ne peut être produit par le cœur gelé : elles ne changent donc l'issue d'aucun relevé
qu'il produit, et empêchent une lecture à vide si l'un d'eux se produisait quand même :

| # | constat | vérification | si elle ne tient pas |
|---|---|---|---|
| V-1 | CLV66-02 | `lecture_selection` est un objet (non nul) | manque : C5 « relevé incomplet » (lecture de la sélection non consignée) |
| V-2 | CLV66-02 | `archives_de_jugement["2"]` est présente | manque : C5 « relevé incomplet » |
| V-3 | CLV66-01 | le champ `arret` nomme-t-il `PlanteeSansArchive` (garde 18) alors que `generations_jouees` vaut [1] (génération 1 finie : l'arrêt est en génération 2) ? | si oui : C5, cause écrite, **et « C4 (partielle) »** (ligne C5) |
| V-4 | CLV66-02, CLV66-03 | si `lecture_selection` est un objet : son `refus` est nul, et `attendu` = `lu` = `lu_sur_disque` (empreinte écrite, lue, relue sur disque) | un refus est un arrêt (C5 et « C4 (partielle) », déjà lus par le programme) ; une inégalité sans refus : écart de P6, C4 |
| V-5 | CLV66-03 | pour chaque génération g ∈ {1, 2} : `vues_servies[g].appels` porte deux appels (Kimi, Argon) et chaque `texte_recu_sha256` = `vues_servies[g].texte_sha256` | moins de deux appels : manque, C5 ; un texte reçu autre que le texte bâti : écart de P6, C4 |
| V-6 | CLV66-03 | si `selection_finale` est un objet : son `refus` est nul et `lu` = `bilan_sha256` (une sélection finale absente est déjà un manque de `completude`) | un refus est déjà lu par le programme (écart de P6) ; une inégalité sans refus : écart de P6, C4 |
| V-7 | CLV66-03 | `retenues["1"]` et `retenues["2"]` sont présentes (listes, vides permises) | manque : C5 « relevé incomplet » |
| V-8 | CLV66-04 | `retenues["1"]` est-elle vide ? | si oui et si l'issue est C1 : phrase en tête (ligne C1) ; issue du cas : nœud NL-1 |

Mesures sans issue : P3 (puissance aux vraies faibles)"""},

    # --- section 9 (gelée) ----------------------------------------------------------------------------------------------------
    {"id": "B2-29", "section": "9. Audit de symétrie (règle R4), écrit d'avance", "constat": "CLV65-01 ; CLV66-04",
     "objet": "A1 : champ absent jamais lu « vrai » ; sélection vide notée ; fichiers bruts",
     "ancien": """  du relais apparié appel par appel), que les fausses ont des log W maximaux ≤ 0 aux marges près, que la vue de la
  génération 2 ne contient aucune loi plantée.""",
     "nouveau": """  du relais apparié appel par appel), que les fausses ont des log W maximaux ≤ 0 aux marges près, que la vue de la
  génération 2 ne contient aucune loi plantée ; noter si la sélection de la génération 1 est vide (V-8 : alors P5 et P6 ne
  prouvent rien de la lecture d'une sélection non vide). Un champ d'audit absent n'y vaut jamais « vrai » ; les pièces
  brutes (fichiers témoins, journaux de `bwrap`, registre du relais apparié, dossier des sessions des proposeurs, gardé,
  chemin au rapport de course) se lisent hors du programme."""},

    # --- section 10 (gelée) ---------------------------------------------------------------------------------------------------
    {"id": "B2-30", "section": "10. Liste d'arrêt", "constat": "CLV65-05 ; rapport v66, section 9",
     "objet": "texte scellé au chemin fixé ; garde 7 complète",
     "ancien": """étage si la part restante est sous son pire cas) ; texte scellé exigé (nom sans « brouillon », sceau, aucun marqueur, code
gelé conforme) ; lois plantées jamais retenues ni servies ;""",
     "nouveau": """étage si la part restante est sous son pire cas) ; texte scellé exigé (chemin fixé
`orchestrator/prereg/preenregistrement-boucle-reelle-organisme-v1-v<N>.md`, nom sans « brouillon », sceau, aucun marqueur,
code gelé conforme au bloc de la section 16, plan et jeu planté conformes) ; lois plantées jamais retenues ni servies
(**garde 7 complète** en v66 : sélection de chaque génération, héritage lu avant la génération 2 et relecture finale,
`exiger_sans_temoin` ; incident consigné au relevé, lu comme écart de P6) ;"""},

    {"id": "B2-31", "section": "10. Liste d'arrêt", "constat": "CLV65-04 ; rapport v66",
     "objet": "gardes neuves : essayées (codes v65 et v66, banc v66)",
     "ancien": """folle, jamais un couperet). **Gardes neuves (code v65, à essayer sur cas sain et artefact avant le scellement)** :""",
     "nouveau": """folle, jamais un couperet). **Gardes neuves (codes v65 et v66 ; chacune essayée sur un artefact, et sur un cas sain
sauf la garde 22, dont le cas sain (vrai `bwrap`, identité 64097) ne se joue que sur la machine, section 12.3, points 1 et 3 ;
essais `essais/test_boucle_reelle_v65.py`, `essais/test_boucle_reelle_v66.py`, `essais/test_lecture_boucle_reelle_v66.py` ;
banc v66, 133 mutations toutes tuées pour la raison attendue ; branches restées sans artefact, dites : section 12.3,
point 3)** :"""},

    {"id": "B2-32", "section": "10. Liste d'arrêt", "constat": "CLV66-01", "objet": "garde 18 : lecture d'un arrêt en génération 2",
     "ancien": """| 18 | lois plantées jugées avec l'archive | nombre de membres d'archive de chaque loi plantée = celui de l'archive de sa génération | loi plantée jugée avec 0 membre → arrêt, code 3 |""",
     "nouveau": """| 18 | lois plantées jugées avec l'archive | nombre de membres d'archive de chaque loi plantée = celui de l'archive de sa génération | loi plantée jugée avec 0 membre ou avec une archive plus petite → arrêt, code 3 (en génération 2 : lu C5 et « C4 (partielle) », section 8, V-3) |"""},

    {"id": "B2-33", "section": "10. Liste d'arrêt", "constat": "CLV65-09 ; CLV65-03 ; rapport v66",
     "objet": "garde 22 précisée (superutilisateur, identité 64097 après la sonde, ordre) ; garde 23 neuve",
     "ancien": """| 22 | machine | `bwrap` ≥ 0.9, sonde du bac réussie, utilisateur dédié | sonde refusée → code 2 avant tout appel payant |""",
     "nouveau": """| 22 | machine | `bwrap` ≥ 0.9 ; lanceur en superutilisateur ; utilisateur dédié ≠ 0 (`--utilisateur-bac 64097`) ; sonde du bac réussie ; identité du script sur l'hôte, lue dans la description de l'exécuteur sondé, = 64097 ; ordre du mode réel : texte, monde, configuration, GO, garde 17, garde 22, garde 15, rôles réels en dernier | `bwrap` absent ou < 0.9, lanceur non superutilisateur, utilisateur 0 ou absent, sonde refusée, identité autre → code 2 avant tout appel payant et avant toute porte de plafond |
| 23 | vue servie (neuve, code v66) | avant le premier appel d'une génération, lois du contexte servi = {K1} ∪ retenues **écrites** par la génération 1 (fichier de sélection relu à part), chacune égale à sa loi d'archive, aucune loi plantée ; après chaque appel, empreinte du texte reçu par le proposeur = celle du texte bâti ; le tout consigné au relevé (`vues_servies`) | vue réduite à {K1}, loi d'un autre contenu, loi plantée servie, texte reçu autre → arrêt, code 3, incident consigné, lu « C4 (partielle) » |"""},

    {"id": "B2-34", "section": "10. Liste d'arrêt", "constat": "CLV65-02 (a)", "objet": "arrêt : jugements déjà au relevé partiel",
     "ancien": """Arrêt = relevé partiel scellé, code 3, aucune issue lue sauf C5 (et C2 ou C4 « partielle », section 8).""",
     "nouveau": """Arrêt = relevé partiel scellé, code 3, aucune issue lue sauf C5 (et C2 ou C4 « partielle », section 8) ; les jugements
d'une génération sont écrits au relevé dès la sortie du juge, avant ses étages, si bien qu'une promotion prononcée avant un
arrêt s'y lit (code v66, CLV65-02 (a)).""" },

    # --- section 11 -----------------------------------------------------------------------------------------------------------
    {"id": "B2-35", "section": "11. Prémortem du rapport au directeur, et réponse du dessin", "constat": "CLV65-09 ; contre-lecture v66, section 6",
     "objet": "essai à blanc --bac reel avec 64097, en superutilisateur",
     "ancien": """| vrai bac à sable jamais lancé | `bwrap` exigé, sonde avant tout appel payant, aucun repli (gardes 3 et 22) ; essai à blanc `--bac reel` rejoué sur la machine de la course avant le lancement |""",
     "nouveau": """| vrai bac à sable jamais lancé | `bwrap` exigé, sonde avant tout appel payant, aucun repli (gardes 3 et 22) ; essai à blanc `--bac reel --utilisateur-bac 64097`, lanceur en superutilisateur, rejoué sur la machine de la course avant le lancement, avec les cinq autres préalables de la section 12.3 |"""},

    {"id": "B2-36", "section": "11. Prémortem du rapport au directeur, et réponse du dessin", "constat": "CLV65-03 ; CLV66-04",
     "objet": "sélection non lue : garde 23 ; preuve vide sans carte retenue",
     "ancien": """| sélection non lue par la génération suivante | P6 et P5 (copies refusées par construction si et seulement si la sélection est lue) ; issue C4 |""",
     "nouveau": """| sélection non lue par la génération suivante | P6 et P5 (copies refusées par construction si et seulement si la sélection est lue) ; vue servie vérifiée au moment du service (garde 23) ; issue C4 ; vérifications V-1 à V-7 ; sans carte réelle retenue en génération 1, la preuve est vide (V-8, nœud NL-1) |"""},

    # --- section 12 -----------------------------------------------------------------------------------------------------------
    {"id": "B2-37", "section": "12. Ce qui manque avant de sceller (pièces et décisions)", "constat": "rapport v66 ; contre-lecture v66, section 6 ; CLV66-05 ; CLV66-07",
     "objet": "section 12 réécrite : fait, avant le scellement, préalables sur la machine, commandes exactes",
     "debut": "## 12. Ce qui manque avant de sceller (pièces et décisions)",
     "fin": "Bloc d'empreintes du code gelé v65 et commandes exactes : à écrire avec le code (marqueur volontaire : <<BLOC-V65>>).",
     "nouveau": r"""## 12. Ce qui est fait, ce qui reste avant le scellement, et les préalables sur la machine

### 12.1 Pièces et décisions faites depuis le brouillon 1

| repère | pièce | état au brouillon 2 |
|---|---|---|
| M0 | machine jetable avec `bwrap` ≥ 0.9 et utilisateur dédié 64097 | **reste** : section 12.3 (GO-2026-11-10-10 nomme une machine jetable Hetzner CPX32 pour les 5 USD de machine) |
| M1 | héritage de départ scellé (génération 0, K1 « connue, déclarée »), garde 17 | fait (code v65) : `heritage-depart-v65.json`, `93dcf517…` |
| M2 | jeu planté lu dans le texte scellé, garde 19 | fait (code v65) : bloc `jeu-plante-v65`, section 16 |
| M3 | lois plantées jugées avec l'archive de leur génération, garde 18 | fait (code v65) |
| M4 | bras réel seul (garde 20) ; génération 2 avec copies (garde 21) et fausses replantées | fait (code v65) ; vue servie vérifiée (garde 23) et garde 7 complète (code v66) |
| M5 | lecture gelée C1 à C6 et A1 à A4 | fait (code v66 : complétude exigée, arrêt qui ne masque pas, vue servie lue) ; vérifications V-1 à V-8 au texte (section 8) |
| M6 | commandes v6 et configuration qui les nomme | fait : configuration v6 `4743ddbe…`, dossier de course `configuration-v6/` |
| M7 | interpréteur de la machine ; suite et banc rejoués dessus | **reste** : section 12.3, points 1 et 2 |
| D1, D2, D3 | bras réel seul ; génération 2 complète ; plafond de 40 USD de modèles (Kimi 33, Argon 7) et 5 USD de machine | décidés par Lazar (GO-2026-11-08-02) ; le GO de la course est une ligne neuve (section 13) |

### 12.2 Avant le scellement

1. **Nœud NL-1** (section 8, C1 sans carte retenue) : décision de Lazar ; le marqueur `NOEUD_C1_SANS_RETENUE` est retiré ou
   remplacé selon elle, par un couple déclaré.
2. **Ligne de GO neuve**, inscrite par Lazar (section 13) ; son identifiant remplace le marqueur `GO_COURSE_V66` partout
   (bloc `plan-gele-v66` de la section 16, section 13, commande de la section 12.4). L'outil `preparer_boucle_reelle_v66.py`
   n'accepte que GO-2026-11-08-02 ou GO-2026-11-10-10 : l'identifiant neuf s'écrit donc à la main dans le bloc ; le lanceur lit
   tout identifiant de la forme `GO-AAAA-MM-JJ-NN` et le vérifie dans le registre.
3. Contre-lecture de ce texte par un sous-agent neuf (section 15) ; texte candidat sous le nom
   `preenregistrement-boucle-reelle-organisme-v1-v<N>.md` (sans « brouillon »), sans marqueur, scellé
   (`controle_ia.scellement sceller`), committé et poussé sur le dépôt de travail avant la course : c'est l'exemplaire qui
   fait foi (R1), et l'empreinte de ses octets est la racine des graines.
4. Copie **à l'octet** du texte scellé, avec son compagnon `.sha256`, dans l'arbre de l'organisme de la machine, sous
   `orchestrator/prereg/` (seul dossier que lit le lanceur) ; le manifeste dira « arbre modifié » (fichier non suivi), ce que
   le rapport de course écrit. La pousser sur le dépôt public de l'organisme est une publication : nœud de Lazar, qui peut
   venir après la course.

### 12.3 Sur la machine de la course, avant le lancement (préalables écrits ; contre-lecture du code v66, section 6)

Arbre de l'organisme à la tête `7e415cbaaa3ff602db43a44dad6b4307c08352c7` (paquet git versé, vérifié par
`git bundle verify`) ; interpréteur et version de numpy de la machine notés au rapport de course ; commandes lancées depuis
`orchestrator/`. Dans cet ordre :

1. La suite des neuf fichiers d'essais (`essais/test_registre_go_v66.py`, `test_boucle_reelle_v66.py`,
   `test_lecture_boucle_reelle_v66.py`, `test_boucle_reelle_v65.py`, `test_lecture_boucle_reelle_v65.py`,
   `test_tour_ferme_v64.py`, `test_gardes_tour_ferme_v64.py`, `test_v59_boucle_fermee.py`, `test_v57b_cablage_verdict.py`)
   **sans** `POLE_ESSAI_BAC_REEL_NON_JOUE` : code 0, aucun essai du vrai bac sauté (les essais du vrai registre sont déclarés
   non joués si le dépôt de travail n'est pas sur la machine).
2. Le banc : `python3 -I -B essais/mutations_boucle_reelle_v66.py --processus 4` → 133 tuées sur 133, code 0.
3. L'essai à blanc au vrai bac, lanceur en superutilisateur :
   `python3 -I -B demonstrations/boucle_reelle_v66.py SORTIE_ESSAI --a-blanc --graine 20261110 --bac reel --utilisateur-bac 64097`
   → code 0, tous les étages « factice : faux », puis sa lecture. C'est aussi le seul passage par la branche à blanc de la
   garde 22 qu'aucun essai ne joue sur artefact (K19 de la contre-lecture du code v66, CLV66-05) ; les deux autres
   survivantes, K01 et K17, sont sans effet sur une issue (dites).
4. Copier `registres/go.md` de `main` du dépôt de travail sur la machine, **après** l'inscription de la ligne de GO neuve ;
   **noter son empreinte sha256 au rapport de course** : le lanceur lit ce fichier-là (avant le point 5, car le lanceur
   vérifie le GO avant la machine, même avec `--verifier-seulement`).
5. La commande réelle avec `--verifier-seulement` (section 12.4) : « vérification : conforme », aucun appel, aucune porte de
   plafond posée ; y lire la description du bac (identité 64097) et les chemins résolus des commandes v6.
6. Lancer le relais Argon (`commandes-v6/commande_argon_v56_nuit_v6.py servir`, port 8805) avec **`--collisionneur`
   explicite** (chemin du collisionneur v7 sur la machine ; depuis le dossier de course, le chemin par défaut ne mène nulle
   part) et `--sha-collisionneur` à sa valeur par défaut
   (`c9725f025407c3ece3e8c16d19cfdfdec078f084a811f0a3b6ea3209be5d98dc`, vérifiée par la commande au démarrage). Chaque relais
   local est lancé avec un plafond au plus égal à la part de son fournisseur (Kimi 33 USD, Argon 7 USD) ; valeurs notées au
   rapport de course.

Un préalable manqué arrête avant tout appel payant. Il se corrige sans changer ce texte s'il ne touche ni le code gelé, ni la
configuration, ni le plan gelé ; sinon, par un texte neuf contre-lu.

### 12.4 Commandes exactes

Depuis `orchestrator/`, sur la machine à `bwrap`, **lanceur en superutilisateur**, après le scellement et les préalables ;
`DOSSIER_COURSE` = le dossier `configuration-v6/` versé, avec `heritage-depart-v65.json` ; `CHEMIN/registres/go.md` = la copie
du point 4 de la section 12.3 :

```
python3 -I -B demonstrations/boucle_reelle_v66.py SORTIE --preenregistrement prereg/preenregistrement-boucle-reelle-organisme-v1-v<N>.md \
    --heritage-depart DOSSIER_COURSE/heritage-depart-v65.json --configuration DOSSIER_COURSE/configuration-boucle-reelle-v6.json \
    --moteur reel --confirmer-moteur-reel --registre-go CHEMIN/registres/go.md --go <<GO_COURSE_V66>> \
    --bac reel --utilisateur-bac 64097 --verifier-seulement
(puis la même, sans --verifier-seulement)
python3 -I -B demonstrations/lire_boucle_reelle_v66.py SORTIE LECTURE.json --releve-sha256 <empreinte du relevé>
```

Codes du lanceur : 0, relevé écrit (le code ne décide rien) ; 2, refus avant tout appel ; 3, arrêt (relevé partiel scellé).
Le rapport de course note : l'empreinte du `registres/go.md` copié, les plafonds des relais, l'interpréteur, l'empreinte du
relevé, le chemin du dossier des sessions des proposeurs (gardé pour l'audit A1) et la phrase rendue par le programme de
lecture ; le verdict (R13) y ajoute les vérifications V-1 à V-8."""},

    # --- section 13 -----------------------------------------------------------------------------------------------------------
    {"id": "B2-38", "section": "13. Devis", "constat": "CLV66-07 ; CLV65-10", "objet": "GO de la course : ligne neuve à identifiant neuf ; machine",
     "ancien": """de la chaîne cassée pour qu'aucun arrêt de dépense ne masque une brèche ; 5 dollars pour la machine.""",
     "nouveau": """de la chaîne cassée pour qu'aucun arrêt de dépense ne masque une brèche ; 5 dollars pour la machine.

**GO de la course (contre-lecture du code v66, CLV66-07).** Ni GO-2026-11-08-02 (« après le code v65 contre-lu ») ni la part
« organisme » de GO-2026-11-10-10 (« code v65 contre-lu », « configuration v5 (`995eb918…`) », empreinte d'aucune
configuration de l'organisme : v5 = `bff138d8…`, v6 = `4743ddbe…`) ne suffisent tels qu'écrits : la course joue le code v66 et
la configuration v6. Elle ne se lance que sous une **ligne de GO neuve, à identifiant neuf, inscrite par Lazar** dans
`registres/go.md` : **<<GO_COURSE_V66>>**. Ce qu'elle doit porter pour que le lanceur la lise (`registre_go_v66.verifier_go_v66`)
et que la course la respecte : type « calcul » ; accordée par Lazar ; en cours de validité le jour du lancement ; **aucune
ligne d'extension, jamais** (le lanceur refuse un GO qui en porte une : une correction est une autre ligne neuve, citée par un
texte neuf) ; plafond lu **45 USD** (montant seul, ou part « organisme » égale à 45 d'une enveloppe) ; conditions, toutes
exigées : code v66 `7e415cbaaa3ff602db43a44dad6b4307c08352c7` contre-lu (`contre-lecture-code-v66-courte-v1.md`,
`a2880368…`) ; configuration v6 `4743ddbe4d294643ac8e1924476dec056b1a08dac9f8010cd647dd1861160b0d` ; machine jetable à `bwrap`
validée par l'essai à blanc `--bac reel` (section 12.3, point 3) ; ce préenregistrement scellé ; 45 USD en tout, 40 de
modèles (Kimi 33, Argon 7) et 5 de machine. Son identifiant est celui du bloc `plan-gele-v66` (section 16) et de la commande
(section 12.4) ; le lanceur le vérifie dans le registre copié sur la machine (identifiant exact, type, accordant, période de
validité, révocations, extensions, montant égal à 45 USD au centime). Le plafond de 5 USD de la machine n'est tenu par aucun
code : la session qui loue la machine cite cette ligne pour la louer, l'arrête par son identifiant (R10) et consigne la
dépense (`registres/depenses.md`, `registres/arrets.md`)."""},

    # --- section 14 -----------------------------------------------------------------------------------------------------------
    {"id": "B2-39", "section": "14. Portée", "constat": "CLV66-04", "objet": "portée : C1 sans carte retenue",
     "ancien": """N-058). Une issue C1 se rapporte toujours avec A1-v3 (brèche hors classe établie) et avec cette portée.""",
     "nouveau": """N-058). Une issue C1 se rapporte toujours avec A1-v3 (brèche hors classe établie) et avec cette portée ; sans carte réelle
retenue en génération 1, elle ne dit rien de la fermeture de la boucle sur un contenu (section 8, nœud NL-1)."""},

    # --- section 15 -----------------------------------------------------------------------------------------------------------
    {"id": "B2-40", "section": "15. Contre-lecture (règle R2)", "constat": "brouillon 2 ; contre-lectures v65 et v66",
     "objet": "contre-lecture du texte à faire ; contre-lectures du code faites et traitement de leurs constats",
     "debut": "## 15. Contre-lecture (règle R2)",
     "fin": "le chiffre de 1,00 est-il présenté sans ambiguïté ? les gardes 17 à 22 sont-elles essayées ?",
     "nouveau": """## 15. Contre-lecture (règle R2)

**Du texte : à faire**, sur ce brouillon 2, par un sous-agent neuf qui n'a écrit ni ce texte (brouillons 1 et 2), ni le code
v65 ou v66, ni leurs contre-lectures. Fichiers à lui donner : ce brouillon 2, le brouillon 1 (`736e3fd6…`), le fichier des
couples, le script et le journal du brouillon 2 (`docs/notes/organisme-boucle-reelle-v1/couples-brouillon2-boucle-reelle-v1.json`,
`faire-brouillon2-boucle-reelle-v1.py`, `journal-brouillon2-boucle-reelle-v1.md`, empreintes au journal et à leurs
compagnons) ; `puissance-boucle-reelle-v1.py` et `-generation2.py` et leurs sorties ; `essai-a-blanc-v1/` et
`code-v66/essai-a-blanc-v66/` ; `devis-boucle-reelle-organisme-v1.md` ; le rapport du développeur v66 et les blocs v66 ; les
contre-lectures du code v65 et v66 ; le code v66 (paquet git, ou arbre à `7e415cba` lu par `git show`) ; les pièces de la table
« Documents qui font foi ». Questions : celles du brouillon 1 (les fausses sont-elles dans la classe couverte, et jugées dans
le bon canal ? la preuve de lecture de la sélection suffit-elle si aucune carte réelle n'est retenue ? le chiffre de 1,00
est-il présenté sans ambiguïté ?) ; les vérifications V-1 à V-8 ferment-elles les cas où la lecture gelée tient P6 à vide, sans
changer l'issue d'un relevé que le cœur gelé peut produire ? les trois blocs de la section 16 sont-ils ceux du développeur à
l'octet, hors la ligne `go` ? les préalables de la section 12.3 suffisent-ils ? un couple touche-t-il une prédiction, un signe
ou un seuil ?

**Du code : faites**, par Claude Fable 5.2, autre modèle que les développeurs (N-052) ; traitement au texte :
- contre-lecture du code v65 (`code-v65/contre-lecture-code-v65-v2.md`, `c4ddfc7f…`) : « utilisable pour la course après
  corrections » ; CLV65-01 à CLV65-10 corrigés par le code v66 ; CLV65-11 et CLV65-13 traités au passage par le développeur
  v66 (reste, dit : une fausse ou une copie promue en génération 2 est encore testée, section 3.7) ; CLV65-12 (réponses)
  pris ;
- contre-lecture courte du code v66 (`code-v66/contre-lecture-code-v66-courte-v1.md`, `a2880368…`) : « utilisable pour la
  course », code inchangé, sous trois conditions hors du code, toutes portées ici : CLV66-01 (V-3, ligne C5), CLV66-02 (V-1,
  V-2, V-4, ligne C1), CLV66-07 (ligne de GO neuve, section 13). Autres : CLV66-03, vérifications V-4 à V-7 ; CLV66-04, phrase
  de la ligne C1, V-8 et nœud NL-1 ; CLV66-05, K19 jouée par l'essai à blanc au vrai bac (section 12.3, point 3), K01 et K17
  dites ; CLV66-06, empreintes de deux fichiers d'essais non gelés, non recopiées ici ; CLV66-08, informations ; sa section 3
  (écart de membres en génération 2 lu C4), phrase de la ligne C5 ; sa section 6, préalables de la section 12.3."""},
]


def appliquer(texte: str, c: dict) -> str:
    if "ancien" in c:
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


def section_16(blocs: str) -> str:
    if blocs.count(LIGNE_GO_DEVELOPPEUR) != 1:
        raise Arret("blocs v66 : ligne « go: GO-2026-11-08-02 » absente ou en double")
    corps = blocs.replace(LIGNE_GO_DEVELOPPEUR, LIGNE_GO_TEXTE, 1)
    return ("\n## 16. Blocs gelés lus par le lanceur (code v66)\n\n"
            "Recopiés à l'octet de `code-v66/blocs-v66/blocs-pour-le-texte-v66.md` "
            "(`9933ee114687079bbf95af94b5e39cd898b69d1d197b4c48587d12692fee1b29`), **sauf la ligne `go` du bloc `plan-gele-v66`**,\n"
            "qui porte le marqueur de la ligne de GO neuve (section 13) au lieu de GO-2026-11-08-02. Le lanceur exige chacun des trois\n"
            "blocs une seule fois dans le texte et refuse sinon : ce texte ne les nomme ailleurs que par leur nom. Les 98 empreintes sont\n"
            "celles des fichiers gelés à la tête `7e415cba` (fermeture statique des deux programmes v66) ; `configuration_sha256` est\n"
            "celle de la configuration v6 ; `heritage_depart_sha256`, celle de `heritage-depart-v65.json` ; `jeu_plante_sha256`, celle\n"
            "des octets JSON du bloc `jeu-plante-v65` ; `monde_sha256`, celle du monde planté. Le plan reprend les décisions D1, D2 et\n"
            "D3 et le devis (sections 6 et 13) ; il ne fixe aucun seuil scientifique neuf.\n\n" + corps)


def controler(texte: str, blocs: str) -> dict:
    for m in MARQUES:
        if texte.count(m) != 1:
            raise Arret(f"marque de bloc {m!r} présente {texte.count(m)} fois (une exigée)")
    attendu = blocs.replace(LIGNE_GO_DEVELOPPEUR, LIGNE_GO_TEXTE, 1)
    debut, fin = texte.index(MARQUES[0]), texte.index(MARQUES[5]) + len(MARQUES[5])
    if texte[debut:fin] != attendu.rstrip("\n"):
        raise Arret("blocs du texte ≠ blocs du développeur hors la ligne go")
    # plan : forme lue par le lanceur v66 (`lire_plan`), recopiée ici sans importer l'organisme
    corps_plan = texte[texte.index(MARQUES[2]) + len(MARQUES[2]):texte.index(MARQUES[3])]
    plan = {}
    for l in corps_plan.splitlines():
        m = re.match(r"^\s*([a-z0-9_]+)\s*:\s*(.+?)\s*$", l)
        if m:
            if m.group(1) in plan:
                raise Arret(f"plan : clé {m.group(1)} en double")
            plan[m.group(1)] = m.group(2)
    if set(plan) != CLES_PLAN or plan != ATTENDU_PLAN:
        raise Arret(f"plan ≠ plan attendu : {plan}")
    centimes = {k: round(float(plan[k]) * 100) for k in ("plafond_modeles_usd", "plafond_kimi_usd", "plafond_argon_usd",
                                                          "plafond_machine_usd", "go_montant_usd")}
    if centimes["plafond_kimi_usd"] + centimes["plafond_argon_usd"] != centimes["plafond_modeles_usd"] or \
            centimes["plafond_modeles_usd"] + centimes["plafond_machine_usd"] != centimes["go_montant_usd"]:
        raise Arret("plan : sommes au centime fausses")
    # jeu planté : empreinte des octets JSON du bloc (même découpe que `boucle_reelle_v65.bloc_du_jeu`)
    brut = texte[texte.index(MARQUES[4]) + len(MARQUES[4]):texte.index(MARQUES[5])]
    m = re.fullmatch(r"\s*```json\n(.*?)\n```\s*", brut, re.S)
    if not m:
        raise Arret("bloc jeu-plante-v65 mal formé")
    json.loads(m.group(1))
    sha_jeu = h(m.group(1).encode("utf-8"))
    if sha_jeu != plan["jeu_plante_sha256"]:
        raise Arret(f"jeu planté {sha_jeu} ≠ plan {plan['jeu_plante_sha256']}")
    corps_e = texte[texte.index(MARQUES[0]) + len(MARQUES[0]):texte.index(MARQUES[1])]
    gelees = re.findall(r"^([0-9a-f]{64})  (\S+)$", corps_e, re.M)
    if len(gelees) != NOMBRE_FICHIERS_GELES or len({r for _, r in gelees}) != NOMBRE_FICHIERS_GELES:
        raise Arret(f"{len(gelees)} empreintes de code gelé ; {NOMBRE_FICHIERS_GELES} attendues")
    restants = {}
    for x in MARQUEUR.findall(texte):
        restants[x] = restants.get(x, 0) + 1
    if restants != MARQUEURS_ATTENDUS:
        raise Arret(f"marqueurs restants {restants} ≠ attendus {MARQUEURS_ATTENDUS}")
    return {"marqueurs_restants": restants, "jeu_plante_sha256": sha_jeu, "fichiers_geles": len(gelees), "plan": plan}


def principal(argv=None) -> int:
    a = argparse.ArgumentParser()
    a.add_argument("--depot", required=True)
    a.add_argument("--brouillon2", required=True)
    a.add_argument("--couples", required=True)
    x = a.parse_args(argv)
    depot = Path(x.depot)
    sorties = [Path(x.brouillon2), Path(x.couples)]
    try:
        for s in sorties:
            if s.exists():
                raise Arret(f"{s} existe : on n'écrase jamais (R12)")
        lus = {}
        for nom, (rel, sha) in ENTREES.items():
            octets = (depot / rel).read_bytes()
            if h(octets) != sha:
                raise Arret(f"{rel} : empreinte {h(octets)} ≠ {sha} (R11)")
            lus[nom] = octets.decode("utf-8")
        texte = lus["brouillon1"]
        if MARQUEUR.findall(texte) != ["<<BLOC-V65>>"]:
            raise Arret("brouillon 1 : marqueurs inattendus")
        ids = [c["id"] for c in COUPLES]
        if len(ids) != len(set(ids)):
            raise Arret("identifiants de couples en double")
        for c in COUPLES:
            texte = appliquer(texte, c)
        texte = texte.rstrip("\n") + "\n" + section_16(lus["blocs_v66"])
        if not texte.endswith("\n"):
            texte += "\n"
        ctl = controler(texte, lus["blocs_v66"])
        sortie = texte.encode("utf-8")
        Path(x.brouillon2).write_bytes(sortie)
        sec = {c["id"]: c["section"] for c in COUPLES}
        doc = {"objet": "couples du brouillon 2 du préenregistrement de la course réelle de l'organisme (code v66, configuration v6)",
               "entrees": {k: {"chemin": v[0], "sha256": v[1]} for k, v in ENTREES.items()},
               "sections_gelees": sorted(SECTIONS_GELEES),
               "couples": [dict(c, gelee=sec[c["id"]] in SECTIONS_GELEES) for c in COUPLES],
               "ajout": {"id": "B2-41", "section": "16. Blocs gelés lus par le lanceur (code v66)", "gelee": False,
                         "constat": "rapport v66, section 7 ; CLV66-07",
                         "objet": "section 16 neuve : trois blocs du développeur à l'octet, ligne go portant le marqueur de la ligne de GO neuve"},
               "nombre_de_couples": len(COUPLES) + 1,
               "couples_en_section_gelee": [c["id"] for c in COUPLES if sec[c["id"]] in SECTIONS_GELEES],
               "controles": ctl,
               "sortie": {"chemin": x.brouillon2, "sha256": h(sortie)}}
        Path(x.couples).write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(json.dumps({"brouillon2_sha256": h(sortie), "couples": len(COUPLES) + 1,
                          "en_section_gelee": doc["couples_en_section_gelee"], "marqueurs": ctl["marqueurs_restants"],
                          "jeu_plante_sha256": ctl["jeu_plante_sha256"], "fichiers_geles": ctl["fichiers_geles"]},
                         ensure_ascii=False, indent=1))
        return 0
    except Arret as e:
        print(f"arrêt : {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(principal())
