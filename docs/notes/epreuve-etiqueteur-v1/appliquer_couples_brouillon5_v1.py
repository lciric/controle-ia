#!/usr/bin/env python3
"""Brouillon 5 de l'épreuve de l'étiqueteur : brouillon 4, plus les 19 couples de la contre-lecture du delta, plus les
compléments qu'exigent les correctifs D1 et D2 (versions 3), le plafond accordé de 300 dollars (GO-2026-11-07-07) et les
remarques R1 à R4 ; appliqués, comptés et journalisés (v1).

Rédacteur : Claude Opus 5.5 (claude-opus-5-5), rédacteur neuf, 7 novembre 2026. Mêmes règles que
`appliquer_couples_brouillon4_v1.py`, dont les fonctions d'application sont reprises telles quelles (import).

Usage :
    python -I -B appliquer_couples_brouillon5_v1.py --heure-fin HH:MM:SS
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import appliquer_couples_brouillon4_v1 as b4  # noqa: E402  (fonctions d'application, inchangées)

BROUILLON4 = ICI / "preenregistrement-epreuve-etiqueteur-v1-brouillon4.md"
COUPLES = ICI / "couples-contre-lecture-delta-brouillon4-v1.json"
BROUILLON5 = ICI / "preenregistrement-epreuve-etiqueteur-v1-brouillon5.md"
JOURNAL = ICI / "journal-couples-brouillon5-v1.json"
EMPREINTE_BROUILLON4 = "4f186d8e9e435d64598d9f0b2b39a646e46934913cb27f39d7dc92a447687db5"
EMPREINTE_COUPLES = "8a533705a569c42816bae75f42941a2b06f9f9b0ae8a6d9212ddc186f854c0b9"
Arret = b4.Arret
h = b4.h

PIECES_B4 = ("- **Pièces** (dossier `docs/notes/epreuve-etiqueteur-v1/`) : ce texte ; **versions en vigueur** : `generer_items_v2.py` et `test_generer_items_v2.py` (24 essais), `lire_items_phase1_v2.py` et `test_lire_items_phase1_v2.py` (13 essais), `analyser_phase1_v2.py` et `test_analyser_phase1_v2.py` (11 essais), `epreuve_phases_v1.py` et `test_epreuve_phases_v1.py` (6 essais), `test_demonstrations_contre_lecture_v2.py` (les 6 démonstrations de la contre-lecture 1, rejouées contre les versions 2) : **60 essais, tous passés** sur processeur, en environnement vidé ; `devis-epreuve-etiqueteur-v3.md` ; `appliquer_couples_brouillon4_v1.py` et son journal `journal-couples-brouillon4-v1.json` ; **versions remplacées, intactes** (R12) : `generer_items_v1.py`, `lire_items_phase1_v1.py`, `analyser_phase1_v1.py` et leurs essais, `devis-epreuve-etiqueteur-v1.md` et `devis-epreuve-etiqueteur-v2.md` ; inchangés : `guide-annotation-v1.md`, `consigne-recrutement-annotateurs-v1.md` (à mettre au volume de la phase 2 avant son départ). Empreintes : annexe C.")


def annexe_c(heure_fin: str, texte: str) -> str:
    q = texte.split("<!-- debut-question-fermee -->", 1)[1].split("<!-- fin-question-fermee -->", 1)[0]
    lignes = [f"Pièces, à {heure_fin} (temps universel) ; ce texte-ci et le journal des couples ne peuvent contenir leur "
              "propre empreinte : le journal donne celle de ce texte, la session mère calcule celle du journal.", "",
              "| fichier | empreinte | statut |", "|---|---|---|"]
    for f, statut in (("generer_items_v2.py", "en vigueur"), ("test_generer_items_v2.py", "en vigueur, 24 essais"),
                      ("lire_items_phase1_v3.py", "en vigueur"), ("test_lire_items_phase1_v3.py", "en vigueur, 21 essais"),
                      ("analyser_phase1_v3.py", "en vigueur"), ("test_analyser_phase1_v3.py", "en vigueur, 12 essais"),
                      ("epreuve_phases_v1.py", "en vigueur"), ("test_epreuve_phases_v1.py", "en vigueur, 6 essais"),
                      ("test_demonstrations_contre_lecture_v2.py", "6 démonstrations, contre les versions 2"),
                      ("devis-epreuve-etiqueteur-v4.md", "en vigueur"), ("devis_phase1_v3.py", "script du devis"),
                      ("appliquer_couples_brouillon5_v1.py", "ce script"),
                      ("appliquer_couples_brouillon4_v1.py", "fonctions reprises par ce script"),
                      ("lire_items_phase1_v2.py", "remplacée, intacte"), ("analyser_phase1_v2.py", "remplacée, intacte"),
                      ("devis-epreuve-etiqueteur-v3.md", "remplacé, intact"),
                      ("preenregistrement-epreuve-etiqueteur-v1-brouillon4.md", "brouillon relu par la contre-lecture du delta"),
                      ("contre-lecture-delta-brouillon4-v1.md", "rapport de la contre-lecture du delta"),
                      ("couples-contre-lecture-delta-brouillon4-v1.json", "19 couples appliqués"),
                      ("guide-annotation-v1.md", "inchangé")):
        lignes.append(f"| `{f}` | `{h(ICI / f)}` | {statut} |")
    lignes.append(f"| bloc de la question fermée (entre les marqueurs ; identique aux brouillons 1 à 4) | "
                  f"`{hashlib.sha256(q.encode('utf-8')).hexdigest()}` | inchangé |")
    lignes.append("| texte de la question rendu par `extraire_question`, sans la clôture de code (champ `question` du "
                  "manifeste de lecture) | `eea2687531fccdb903092f2fa7511db86debdbea5977b6fdacd86d89723220b4` | inchangé |")
    lignes += ["",
               "**Génération d'essai de la version 2** (graine 20261107, hors du dépôt) : items "
               "`f11ba2734f7a961c396aff11f7042283b03d7af3ce4ccf8545575bc8048dba62`, clé "
               "`97e7e107e1c93eb7521f6b2f4586587eee6ffdb992707b5b97fcf23a7be4f1ad` (empreinte seulement).", "",
               f"**Essais** : 69 passés à {heure_fin} en environnement vidé (`env -i`) : les 63 des versions en vigueur "
               "et les 6 démonstrations de la contre-lecture 1 ; les jeux des versions remplacées passent toujours contre "
               "leurs versions intactes.", "",
               "**Prix d'Argon** : vérification tentée sur la page publique des prix de Google, sans appel payant : hôte "
               "`ai.google.dev` hors du réseau permis de cette session ; **toujours à vérifier**.", "",
               "**Interdits tenus** : aucune lecture de `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*` ni "
               "`docs/notes/bras-attaque/` ; aucune clé lue (seules des valeurs factices posées par les essais) ; aucun "
               "appel payant ; aucun contact, aucune publication ; aucun module du programme importé ; aucun commit, "
               "aucune poussée, aucun fichier d'empreinte compagnon ; versions antérieures, brouillons 1 à 4, "
               "contre-lectures et leurs pièces non modifiés."]
    return "\n".join(lignes)


def complements(heure_fin: str, texte: str, cd19: str) -> list:
    debut_c = texte.index("## Annexe C — empreintes au rendu (sans contenu de clé)")
    fin_c = texte.index("## Annexe D")
    return [
        {"id": "C5-01", "motif": "titre", "ancien": "# Préenregistrement — épreuve de l'étiqueteur du sabotage flou — v1, brouillon 4",
         "nouveau": "# Préenregistrement — épreuve de l'étiqueteur du sabotage flou — v1, brouillon 5"},
        {"id": "C5-02", "motif": "rédacteur",
         "ancien": "j'ai écrit les brouillons 1 à 3 de ce texte et les scripts qu'il cite ; je n'ai écrit ni la contre-lecture 1, ni ses couples, ni ses essais de démonstration.",
         "nouveau": "j'ai écrit les brouillons 1 à 4 de ce texte et les scripts qu'il cite ; je n'ai écrit ni les deux contre-lectures, ni leurs couples, ni leurs essais."},
        {"id": "C5-03", "motif": "heures", "ancien": "7 novembre 2026, de 22:56:08 à 23:12:13 (brouillon 4).",
         "nouveau": f"7 novembre 2026, de 23:33:23 à {heure_fin} (brouillon 5)."},
        {"id": "C5-04", "motif": "statut du brouillon 5", "ancien": "- **Statut** : brouillon 4 = brouillon 3,",
         "nouveau": "- **Statut** : brouillon 5 = brouillon 4, plus les 19 couples de la contre-lecture du delta (appliqués par `appliquer_couples_brouillon5_v1.py`, journal `journal-couples-brouillon5-v1.json`), plus les compléments qu'exigent les correctifs D1 et D2 (versions 3, chacun avec ses essais sur un cas sain et sur un artefact), le plafond accordé de 300 dollars (GO-2026-11-07-07) et les remarques R1 à R4 ; **non contre-lu dans cet état** (contre-lecture du delta suivante, bornée à ces correctifs, requise), **non scellé**. Historique : brouillon 4 = brouillon 3,"},
        {"id": "C5-05", "motif": "demande de la session mère", "ancien": "écrire comme une limite l'empreinte de longueur de « changer ».",
         "nouveau": "écrire comme une limite l'empreinte de longueur de « changer ».\n- **Demande de la session mère** (7 novembre 2026, vers 23:33, temps universel) : corriger D1 et D2 de la contre-lecture du delta en versions 3, avec leurs essais ; écrire partout le plafond accordé par le directeur, **300 dollars** (GO-2026-11-07-07), et recalculer le seuil du feu vert de l'essai de format ; relever `--max-appels` du relais de Kimi dans l'ordre d'exécution ; vérifier le prix d'Argon sans appel payant si possible ; ajouter les remarques R1 à R4 ; écrire ce brouillon 5 et un devis v4."},
        {"id": "C5-06", "motif": "base",
         "ancien": "- **Base** : commit `b9f5f5840` (branche `prep/epreuve-etiqueteur-v1`), où les brouillons 1 à 3, la contre-lecture 1, ses couples et ses essais de démonstration sont versés ; aucun n'est touché.",
         "nouveau": "- **Base** : commit `bcb73441e` (branche `prep/epreuve-etiqueteur-v1`), où les brouillons 1 à 4, les deux contre-lectures, leurs couples et leurs essais sont versés ; aucun n'est touché."},
        {"id": "C5-07", "motif": "pièces", "ancien": PIECES_B4,
         "nouveau": "- **Pièces** (dossier `docs/notes/epreuve-etiqueteur-v1/`) : ce texte ; **versions en vigueur** : `generer_items_v2.py` et `test_generer_items_v2.py` (24 essais), `lire_items_phase1_v3.py` et `test_lire_items_phase1_v3.py` (21 essais), `analyser_phase1_v3.py` et `test_analyser_phase1_v3.py` (12 essais), `epreuve_phases_v1.py` et `test_epreuve_phases_v1.py` (6 essais) : **63 essais**, plus les 6 démonstrations de la contre-lecture 1 (`test_demonstrations_contre_lecture_v2.py`, contre les versions 2, dont les versions 3 héritent) : **69 passés** sur processeur, en environnement vidé ; `devis-epreuve-etiqueteur-v4.md` ; `appliquer_couples_brouillon5_v1.py` et son journal `journal-couples-brouillon5-v1.json` ; **versions remplacées, intactes** (R12) : `generer_items_v1.py`, `lire_items_phase1_v1.py` et `lire_items_phase1_v2.py`, `analyser_phase1_v1.py` et `analyser_phase1_v2.py`, leurs essais, devis v1 à v3 ; inchangés : `guide-annotation-v1.md`, `consigne-recrutement-annotateurs-v1.md` (à mettre au volume de la phase 2 avant son départ). Empreintes : annexe C."},
        {"id": "C5-08", "motif": "table des changements depuis le brouillon 4", "ancien": "## Ce qui change depuis le brouillon 3\n",
         "nouveau": """## Ce qui change depuis le brouillon 4

| point | brouillon 4 | brouillon 5 (contre-lecture du delta) |
|---|---|---|
| nom de la variable de la clé (D1) | non contrôlé ; une valeur de clé passée comme nom s'écrivait en clair (sortie d'erreur, manifeste) | forme `[A-Z_][A-Z0-9_]*` exigée avant tout appel et toute écriture, valeur refusée jamais recopiée ; **tout** message masqué, erreurs d'arguments et arrêts compris ; formes de `--go`, `--commit`, `--relais-empreinte`, `--relais-kimi` contrôlées (`lire_items_phase1_v3.py`) |
| réponses absentes (D2) | hors de la règle des 2 % ; fichier vide lu « non validé » | une ligne « principale » par item et une « relecture » par jumeau exigées, ni plus ni moins ; sinon aucun verdict (`analyser_phase1_v3.py`) |
| plafond de la phase 1 | 400 proposé | **300 accordé** (GO-2026-11-07-07), jamais dépassé par le script ; feu vert si la lecture principale mesurée reste sous ≈ 229 à 234 dollars |
| second lancement (R1) | plafond et dépense non contrôlés | même plafond que l'essai de format et dépense engagée au moins égale à la sienne, contrôlés |
| exception hors d'une lecture (R3) | manifeste au code 0, fichiers vides | saisie, écrite, masquée ; code 7 |
| clé invalide d'Argon en 400 (R4) | items illisibles | arrêt de tous les appels, comme 401 et 403 |
| relais de Kimi | défaut de 64 appels ; 402 sans arrêt | `--max-appels` 100 puis 2 280 dans l'ordre d'exécution, exigé et écrit par le script en mode réel ; 402 arrête le lecteur Kimi |
| devis | v3 | v4 (estimations inchangées ; plafond 300 ; seuil du feu vert ; réglages du relais) |
| texte | — | 19 couples appliqués par script, comptés et journalisés ; compléments au même journal |

## Ce qui change depuis le brouillon 3
"""},
        {"id": "C5-09", "motif": "devis v4 en bref",
         "ancien": "3. **Devis v3** (prix d'Argon à vérifier) : phase 1 environ **185 dollars au centre, 329 en hypothèse haute, 600 au plus prudent**, sur les réglages gelés des lecteurs (plafond proposé 400) ;",
         "nouveau": "3. **Devis v4** (prix d'Argon à vérifier) : phase 1 environ **185 dollars au centre, 329 en hypothèse haute, 600 au plus prudent**, sur les réglages gelés des lecteurs ; **plafond accordé : 300 dollars** (GO-2026-11-07-07) ;"},
        {"id": "C5-10", "motif": "plafond accordé (table historique)",
         "ancien": "600 au prudent ; plafond proposé 400) |", "nouveau": "600 au prudent ; plafond proposé 400, accordé ensuite à 300 : brouillon 5) |"},
        {"id": "C5-11", "motif": "plafond accordé (garde)", "ancien": "(`--plafond-dollars`, 400 proposé au devis v3, pour la phase entière ;",
         "nouveau": "(`--plafond-dollars`, **300 accordé** par le directeur, GO-2026-11-07-07, pour la phase entière, jamais au-delà ;"},
        {"id": "C5-12", "motif": "plafond accordé (devis)", "ancien": "plafond proposé **400 dollars** pour la phase entière",
         "nouveau": "plafond proposé 400 dollars pour la phase entière, **accordé à 300 dollars** par le directeur (GO-2026-11-07-07 ; devis v4)"},
        {"id": "C5-13", "motif": "seuil du feu vert pour 300 dollars",
         "ancien": "Avec ce plafond, le feu vert n'est donné que si la lecture principale extrapolée (coût moyen mesuré majoré de 25 %) tient dans le reste : à l'hypothèse haute (lecture principale 316 dollars, essai de format 14), l'extrapolation vaut environ 394 dollars pour 386 restants et le feu est rouge ; le seuil se situe vers 309 dollars de lecture principale mesurée, soit entre l'hypothèse centrale (177) et l'hypothèse haute (estimation de la contre-lecture du delta, non opposable).",
         "nouveau": "Avec le plafond accordé de 300 dollars, le feu vert n'est donné que si la lecture principale extrapolée (coût moyen mesuré majoré de 25 %) tient dans 300 dollars moins la dépense de l'essai de format : le seuil vaut environ (300 − F) / 1,25 dollars de lecture principale mesurée, soit 234 si l'essai de format coûte 7,6 dollars (centre) et 229 s'il en coûte 13,7 (haut) ; l'hypothèse centrale passe (1,25 × 177 = 221 pour 292 restants), l'hypothèse haute donne un feu rouge (1,25 × 316 = 394 pour 286 restants) (devis v4 ; avec 400 dollars, la contre-lecture du delta situait ce seuil vers 309)."},
        {"id": "C5-14", "motif": "analyse v3 (règles)", "ancien": "(code : `analyser_phase1_v2.py`, fonctions `criteres` et `issue_phase1` ;",
         "nouveau": "(code : `analyser_phase1_v3.py`, fonctions `criteres` et `issue_phase1`, précédées de `controler_completude`, essai `test_D2_reponses_completes_cas_sain_et_artefacts` ;"},
        {"id": "C5-15", "motif": "lecture v3 (réglages)", "ancien": "  - Code : constantes `LECTEURS` de `lire_items_phase1_v2.py`,",
         "nouveau": "  - Code : constantes `LECTEURS` de `lire_items_phase1_v3.py` (inchangées depuis la v2),"},
        {"id": "C5-16", "motif": "lecture v3 et codes de sortie",
         "ancien": "- **Lecture** : `docs/notes/epreuve-etiqueteur-v1/lire_items_phase1_v2.py` (la version 1 reste intacte). Codes de sortie : 0 fini ; 2 rendu fautif ou entrées refusées, avant tout appel ;",
         "nouveau": "- **Lecture** : `docs/notes/epreuve-etiqueteur-v1/lire_items_phase1_v3.py` (les versions 1 et 2 restent intactes ; essais `test_D1_nom_de_variable_cas_sain_et_artefact`, `test_D1_sortie_d_erreur_masquee_en_mode_reel`, `test_D1_formes_des_autres_arguments`, `test_plafond_accorde_300_cas_sain_et_artefact`, `test_R1_second_lancement_controle_contre_l_essai_de_format`, `test_R3_exception_hors_d_une_lecture`, `test_R4_cle_invalide_en_400_et_402_du_relais`, `test_relais_max_appels_en_mode_reel`). Codes de sortie : 0 fini ; 2 rendu fautif, entrées ou arguments refusés (valeur refusée jamais recopiée), avant tout appel ; 7 exception imprévue hors d'une lecture (saisie, écrite, masquée) ;"},
        {"id": "C5-17", "motif": "liste des relectures par l'analyse v3", "n": 2, "ancien": "`analyser_phase1_v2.py relectures`",
         "nouveau": "`analyser_phase1_v3.py relectures`"},
        {"id": "C5-18", "motif": "analyse v3", "ancien": "- **Analyse** : `docs/notes/epreuve-etiqueteur-v1/analyser_phase1_v2.py` (la version 1 reste intacte),",
         "nouveau": "- **Analyse** : `docs/notes/epreuve-etiqueteur-v1/analyser_phase1_v3.py` (les versions 1 et 2 restent intactes),"},
        {"id": "C5-19", "motif": "ordre des opérations : scripts v3",
         "ancien": "2. Scripts de lecture (`lire_items_phase1_v2.py`) et d'analyse (`analyser_phase1_v2.py`), générateur `generer_items_v2.py`",
         "nouveau": "2. Scripts de lecture (`lire_items_phase1_v3.py`) et d'analyse (`analyser_phase1_v3.py`), générateur `generer_items_v2.py`"},
        {"id": "C5-20", "motif": "points ouverts : code v3", "ancien": "et au code (`lire_items_phase1_v2.py`)",
         "nouveau": "et au code (`lire_items_phase1_v3.py`)"},
        {"id": "C5-21", "motif": "R1 vérifié", "ancien": "(le script ne le vérifie pas : contre-lecture du delta)",
         "nouveau": "(vérifié par `lire_items_phase1_v3.py`, remarque R1 de la contre-lecture du delta)"},
        {"id": "C5-22", "motif": "relais : 402 et ordre d'exécution",
         "ancien": "ses réponses 402 (plafond) et 429 (appels) rendent l'item illisible sans arrêter le lecteur (arrêt du lecteur recommandé au code par la contre-lecture du delta).",
         "nouveau": "une réponse 402 du relais (son plafond) arrête le lecteur Kimi (`lire_items_phase1_v3.py`) ; une réponse 429 (appels) rend l'item illisible ; en mode réel, le script exige `--relais-max-appels` au moins égal à cinq fois le nombre d'items du lancement et l'écrit au manifeste. **Ordre d'exécution** : avant chaque lancement, le relais est relancé avec `--max-appels` 100 (essai de format) puis 2 280 (lecture principale et relecture), `--modeles-permis kimi-k3.1-pro` et `--plafond-usd` égal au reste du plafond de 300 dollars (devis v4)."},
        {"id": "C5-23", "motif": "R4 au code",
         "ancien": "le script la traite alors en « illisible », sans arrêt général, et l'essai de format passe au rouge ; arrêt général sur ce motif recommandé au code par la contre-lecture du delta)",
         "nouveau": "`lire_items_phase1_v3.py` en fait un arrêt général, comme 401 et 403 : remarque R4 de la contre-lecture du delta)"},
        {"id": "C5-24", "motif": "ordre des opérations : devis v4 et plafond accordé", "ancien": "5. Décision du directeur sur la dépense de la phase 1 (devis v3, section 1).",
         "nouveau": "5. Décision du directeur sur la dépense de la phase 1 : **300 dollars accordés** (GO-2026-11-07-07 ; devis v4, section 1)."},
        {"id": "C5-25", "motif": "ordre des opérations : relais et plafond",
         "ancien": "6. Phase 1, en deux lancements : essai de format seul (`--lectures format`) et contrôle écrit par le script (",
         "nouveau": "6. Phase 1, en deux lancements, le relais de Kimi relancé avant chacun avec `--max-appels` 100 puis 2 280 : essai de format seul (`--lectures format`, `--plafond-dollars 300`) et contrôle écrit par le script ("},
        {"id": "C5-26", "motif": "ordre des opérations : second lancement",
         "ancien": "puis lecture principale et relecture (`--lectures principale+relecture --feu-vert-format …`, `--depense-engagee`) ;",
         "nouveau": "puis lecture principale et relecture (`--lectures principale+relecture --feu-vert-format …`, même `--plafond-dollars 300`, `--depense-engagee` au moins égale à la dépense de l'essai de format : contrôlés par le script) ;"},
        {"id": "C5-27", "motif": "devis v4", "ancien": "## Devis (détail : `devis-epreuve-etiqueteur-v3.md` ; le devis v2 reste tel quel)",
         "nouveau": "## Devis (détail : `devis-epreuve-etiqueteur-v4.md` ; les devis v2 et v3 restent tels quels)"},
        {"id": "C5-28", "motif": "liste d'arrêt : D1, R1, R3",
         "ancien": "| essai de format au feu rouge | code 6 ; lecture principale refusée par le script ; nouveau devis ou nœud du directeur |",
         "nouveau": "| essai de format au feu rouge | code 6 ; lecture principale refusée par le script ; nouveau devis ou nœud du directeur |\n| argument de forme refusée (nom de la variable de la clé, commit, empreinte du relais, GO, adresse du relais), argument inconnu, ou plafond au-delà de 300 dollars | arrêt avant tout appel et toute écriture ; message masqué, valeur refusée jamais recopiée (code 2 ; D1) |\n| lecture principale avec un autre plafond que l'essai de format, ou une dépense engagée inférieure à la sienne | refus avant tout appel (remarque R1) |\n| exception imprévue hors d'une lecture | saisie, écrite et masquée ; code 7 ; nœud du directeur avant toute lecture de réponse (remarque R3) |"},
        {"id": "C5-29", "motif": "prix d'Argon : tentative de vérification", "ancien": "(barème corrigé en version nouvelle avant toute lecture, nœud du directeur).",
         "nouveau": "(barème corrigé en version nouvelle avant toute lecture, nœud du directeur). Vérification tentée le 7 novembre vers 23:37 sur la page publique des prix de Google, sans appel payant : hôte `ai.google.dev` hors du réseau permis de cette session ; **toujours à vérifier**."},
        {"id": "C5-30", "motif": "limite 13 : plafond accordé", "ancien": "dans `test_demonstrations_contre_lecture_v2.py` (6 passés).",
         "nouveau": "dans `test_demonstrations_contre_lecture_v2.py` (6 passés).\n13. **Plafond de 300 dollars** : sous l'hypothèse haute du devis (lecture principale ≈ 316 dollars), le feu vert de l'essai de format sera rouge ; l'épreuve peut donc s'arrêter après l'essai de format, sans verdict ni dépense de lecture principale, et appeler un nouveau devis."},
        {"id": "C5-31", "motif": "traitement de la contre-lecture du delta", "ancien": cd19,
         "nouveau": cd19 + "\n- **Traitement de la contre-lecture du delta** (brouillon 5) : D1 → `lire_items_phase1_v3.py` (forme du nom de variable, masquage de tout message, formes des autres arguments) ; D2 → `analyser_phase1_v3.py` (`controler_completude`) ; chacun avec ses essais sur un cas sain et sur un artefact (la version 2 sert d'artefact) ; R1 à R4 au code ; R5 (relais) : `--relais-max-appels` exigé en mode réel, réponse 402 arrêtant le lecteur, ordre d'exécution écrit ; R6 : `--fils-par-lecteur` gelé à 1 au code ; plafond accordé de 300 dollars écrit au script, au texte et au devis v4 ; 19 couples appliqués par script, comptés et journalisés. **Contre-lecture du delta suivante** : à faire par un sous-agent neuf, bornée aux versions 3, au devis v4, à ce brouillon et au journal des couples."},
        {"id": "C5-33", "motif": "devis v2 remplacé", "ancien": "- **Phase 1** (devis v2, remplacé par le devis v3) :",
         "nouveau": "- **Phase 1** (devis v2, remplacé par les devis v3 puis v4) :"},
        {"id": "C5-32", "motif": "annexe C refaite", "ancien": texte[debut_c:fin_c],
         "nouveau": "## Annexe C — empreintes au rendu (sans contenu de clé)\n\nANNEXE_C_5\n\n"},
    ]


def principal(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--heure-fin", required=True)
    a = p.parse_args(argv)
    for chemin, attendue in ((BROUILLON4, EMPREINTE_BROUILLON4), (COUPLES, EMPREINTE_COUPLES)):
        if h(chemin) != attendue:
            raise Arret(f"empreinte de {chemin.name} différente de l'attendue")
    for chemin in (BROUILLON5, JOURNAL):
        if chemin.exists():
            raise Arret(f"{chemin.name} existe déjà : on n'écrase jamais (R12)")
    texte = BROUILLON4.read_text(encoding="utf-8")
    couples = json.loads(COUPLES.read_text(encoding="utf-8"))
    if len(couples) != 19:
        raise Arret(f"{len(couples)} couples au lieu de 19")
    texte, j1 = b4.appliquer_couples(texte, couples)
    cd19 = next(c["nouveau"] for c in couples if c["id"].startswith("CD-19"))
    texte, j2 = b4.appliquer_complements(texte, complements(a.heure_fin, texte, cd19))
    if texte.count("ANNEXE_C_5") != 1:
        raise Arret("emplacement de l'annexe C introuvable")
    texte = texte.replace("ANNEXE_C_5", annexe_c(a.heure_fin, texte))
    octets = texte.encode("utf-8")
    BROUILLON5.write_bytes(octets)
    journal = {"script": Path(__file__).name, "empreinte_script": h(Path(__file__)),
               "fonctions_reprises": {"appliquer_couples_brouillon4_v1.py": h(ICI / "appliquer_couples_brouillon4_v1.py")},
               "entrees": {BROUILLON4.name: EMPREINTE_BROUILLON4, COUPLES.name: EMPREINTE_COUPLES},
               "sortie": {BROUILLON5.name: hashlib.sha256(octets).hexdigest()},
               "comptes": {"couples_appliques": len(j1), "occurrences_des_couples": sum(x["n_trouve"] for x in j1),
                           "complements_appliques": len(j2), "occurrences_des_complements": sum(x["n_trouve"] for x in j2)},
               "couples": [dict(x, source="couple de la contre-lecture du delta") for x in j1], "complements": j2}
    JOURNAL.write_text(json.dumps(journal, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"comptes": journal["comptes"], "brouillon5": journal["sortie"][BROUILLON5.name]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(principal())
    except Arret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(2)
