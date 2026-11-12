#!/usr/bin/env python3
"""Brouillon 4 de l'épreuve de l'étiqueteur : brouillon 3, plus les 38 couples de la contre-lecture 1, plus les compléments
qu'exigent les correctifs de code (versions 2) ; appliqués, comptés et journalisés (v1).

Rédacteur : Claude Opus 5.5 (claude-opus-5-5), rédacteur neuf, 7 novembre 2026.

Règles : les empreintes des entrées sont vérifiées ; chaque « ancien » d'un couple doit figurer exactement n fois dans
le brouillon 3 (et les anciens ne se chevauchent pas) ; chaque complément doit figurer exactement n fois dans le texte
où il s'applique ; tout écart arrête sans rien écrire ; on n'écrase jamais (R12). Le journal donne, pour chaque
couple et chaque complément, le nombre attendu, le nombre trouvé et le motif.

Usage :
    python -I -B appliquer_couples_brouillon4_v1.py --heure-fin HH:MM:SS
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
BROUILLON3 = ICI / "preenregistrement-epreuve-etiqueteur-v1-brouillon3.md"
COUPLES = ICI / "couples-contre-lecture-epreuve-etiqueteur-brouillon3-v1.json"
BROUILLON4 = ICI / "preenregistrement-epreuve-etiqueteur-v1-brouillon4.md"
JOURNAL = ICI / "journal-couples-brouillon4-v1.json"
EMPREINTE_BROUILLON3 = "9fe95f1095e586f6ec82c1305bd94af5b150acd049161a10e06985e0b2fa6364"
EMPREINTE_COUPLES = "e2bdfd32b3c73e663622f68e55d80b4aa3274dc7f037eed011f3369609206cbf"
DEVIS_V3_SCRIPT = Path("/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/explo/devis_phase1_v3.py")


class Arret(RuntimeError):
    pass


def h(chemin: Path) -> str:
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


def appliquer_couples(texte: str, couples: list) -> tuple:
    journal = []
    positions = []
    for c in couples:
        n = texte.count(c["ancien"])
        if n != c["n"]:
            raise Arret(f"{c['id']} : {n} occurrences au lieu de {c['n']}")
        debut = 0
        for _ in range(n):
            i = texte.index(c["ancien"], debut)
            positions.append((i, i + len(c["ancien"]), c["id"]))
            debut = i + 1
    positions.sort()
    for (a1, b1, id1), (a2, b2, id2) in zip(positions, positions[1:]):
        if a2 < b1:
            raise Arret(f"chevauchement : {id1} et {id2}")
    for c in couples:  # aucun chevauchement : l'ordre d'application est indifférent
        texte = texte.replace(c["ancien"], c["nouveau"])
        journal.append({"id": c["id"], "source": "couple de la contre-lecture 1", "n_attendu": c["n"],
                        "n_trouve": c["n"], "applique": True,
                        "empreinte_ancien": hashlib.sha256(c["ancien"].encode()).hexdigest(),
                        "empreinte_nouveau": hashlib.sha256(c["nouveau"].encode()).hexdigest()})
    return texte, journal


def appliquer_complements(texte: str, complements: list) -> tuple:
    journal = []
    for c in complements:
        n = texte.count(c["ancien"])
        if n != c.get("n", 1):
            raise Arret(f"{c['id']} : {n} occurrences au lieu de {c.get('n', 1)}")
        texte = texte.replace(c["ancien"], c["nouveau"])
        journal.append({"id": c["id"], "source": "complément du rédacteur", "motif": c["motif"],
                        "n_attendu": c.get("n", 1), "n_trouve": n, "applique": True,
                        "empreinte_ancien": hashlib.sha256(c["ancien"].encode()).hexdigest(),
                        "empreinte_nouveau": hashlib.sha256(c["nouveau"].encode()).hexdigest()})
    return texte, journal


def annexe_c(heure_fin: str, texte: str) -> str:
    q = texte.split("<!-- debut-question-fermee -->", 1)[1].split("<!-- fin-question-fermee -->", 1)[0]
    lignes = [f"Pièces, à {heure_fin} (temps universel) ; ce texte-ci et le journal des couples ne peuvent contenir leur "
              "propre empreinte : le journal donne celle de ce texte, la session mère calcule celle du journal.", "",
              "| fichier | empreinte | statut |", "|---|---|---|"]
    for f, statut in (("generer_items_v2.py", "en vigueur"), ("test_generer_items_v2.py", "en vigueur, 24 essais"),
                      ("lire_items_phase1_v2.py", "en vigueur"), ("test_lire_items_phase1_v2.py", "en vigueur, 13 essais"),
                      ("analyser_phase1_v2.py", "en vigueur"), ("test_analyser_phase1_v2.py", "en vigueur, 11 essais"),
                      ("epreuve_phases_v1.py", "en vigueur"), ("test_epreuve_phases_v1.py", "en vigueur, 6 essais"),
                      ("test_demonstrations_contre_lecture_v2.py", "en vigueur, 6 essais"),
                      ("devis-epreuve-etiqueteur-v3.md", "en vigueur"),
                      ("appliquer_couples_brouillon4_v1.py", "ce script"),
                      ("generer_items_v1.py", "remplacée, intacte"), ("lire_items_phase1_v1.py", "remplacée, intacte"),
                      ("analyser_phase1_v1.py", "remplacée, intacte"), ("devis-epreuve-etiqueteur-v2.md", "remplacé, intact"),
                      ("preenregistrement-epreuve-etiqueteur-v1-brouillon3.md", "brouillon relu par la contre-lecture 1"),
                      ("contre-lecture-preenregistrement-epreuve-etiqueteur-v1-brouillon3.md", "rapport de la contre-lecture 1"),
                      ("couples-contre-lecture-epreuve-etiqueteur-brouillon3-v1.json", "38 couples appliqués"),
                      ("essais-contre-lecture-brouillon3-v1.py", "démonstrations de la v1, intactes"),
                      ("guide-annotation-v1.md", "inchangé")):
        lignes.append(f"| `{f}` | `{h(ICI / f)}` | {statut} |")
    lignes.append(f"| bloc de la question fermée (entre les marqueurs ; identique aux brouillons 1 à 3) | "
                  f"`{hashlib.sha256(q.encode('utf-8')).hexdigest()}` | inchangé |")
    lignes.append("| texte de la question rendu par `extraire_question`, sans la clôture de code (champ `question` du "
                  "manifeste de lecture) | `eea2687531fccdb903092f2fa7511db86debdbea5977b6fdacd86d89723220b4` | inchangé |")
    lignes += ["",
               "**Génération d'essai refaite par la version 2** (graine 20261107, hors du dépôt, montrée à personne) : items "
               "`f11ba2734f7a961c396aff11f7042283b03d7af3ce4ccf8545575bc8048dba62`, clé "
               "`97e7e107e1c93eb7521f6b2f4586587eee6ffdb992707b5b97fcf23a7be4f1ad` (empreinte seulement). Les items de la "
               "version 1 de même graine (`206b01fb…`) ne servent plus.", "",
               f"**Essais** : 60 passés à {heure_fin} en environnement vidé (`env -i`), commande en tête de chaque "
               "fichier d'essai ; les jeux de la version 1 (`test_generer_items_v1.py` 20, `test_lire_items_phase1_v1.py` "
               "9, `test_analyser_phase1_v1.py` 9) passent toujours contre leurs versions intactes.", "",
               "**Interdits tenus** : aucune lecture de `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*` ni "
               "`docs/notes/bras-attaque/` ; aucune clé lue (essais en environnement vidé ; seules des valeurs factices "
               "posées par les essais) ; aucun appel payant, aucun réseau ; aucun contact, aucune publication ; aucun "
               "module du programme importé ; aucun commit, aucune poussée, aucun fichier d'empreinte compagnon ; "
               "versions antérieures, brouillons 1 à 3, contre-lecture et ses pièces non modifiés."]
    return "\n".join(lignes)


def complements(heure_fin: str, texte_apres_couples: str) -> list:
    devis_v3 = DEVIS_V3_SCRIPT.read_text(encoding="utf-8")
    nouveau_annexe_b = (
        "**`devis_phase1_v3.py`** (`" + hashlib.sha256(DEVIS_V3_SCRIPT.read_bytes()).hexdigest() + "`, devis v3 ; "
        "arguments : dossier du code, brouillon 3 pour la question, items, clé et items de formation de la génération "
        "d'essai refaite par la version 2)\n\n```python\n" + devis_v3 + "```\n\n"
        "Sorties (dollars ; A Argon 10 et 50, à vérifier ; B Kimi 2 et 10) : essai de format, 21 appels par lecteur : "
        "central 5,64 et 1,97, haut 10,04 et 3,65, prudent 18,18 et 6,95 ; lecture principale et relecture, 479 appels "
        "par lecteur : central 131,47 et 45,45, haut 231,83 et 83,75, prudent 415,99 et 158,89 ; totaux : central 184,5, "
        "haut 329,3, prudent 600,0.\n\n## Annexe C — empreintes au rendu (sans contenu de clé)")
    debut_c = texte_apres_couples.index("## Annexe C — empreintes au rendu (sans contenu de clé)")
    fin_c = texte_apres_couples.index("## Annexe D")
    ancien_c = texte_apres_couples[debut_c:fin_c]
    return [
        {"id": "C4-01", "motif": "titre", "ancien": "# Préenregistrement — épreuve de l'étiqueteur du sabotage flou — v1, brouillon 3",
         "nouveau": "# Préenregistrement — épreuve de l'étiqueteur du sabotage flou — v1, brouillon 4"},
        {"id": "C4-02", "motif": "rédacteur", "ancien": "j'ai écrit les brouillons 1 et 2 de ce texte et les scripts qu'il cite.",
         "nouveau": "j'ai écrit les brouillons 1 à 3 de ce texte et les scripts qu'il cite ; je n'ai écrit ni la contre-lecture 1, ni ses couples, ni ses essais de démonstration."},
        {"id": "C4-03", "motif": "heures du brouillon 4", "ancien": "7 novembre 2026, de 22:20:09 à 22:29:32.",
         "nouveau": f"7 novembre 2026, de 22:56:08 à {heure_fin} (brouillon 4)."},
        {"id": "C4-04", "motif": "statut du brouillon 4",
         "ancien": "- **Statut** : brouillon 3, **contre-lu une fois (contre-lecture 1 : non scellable en l'état, correctifs de code demandés ; voir la section « Contre-lecture »), non scellé**.",
         "nouveau": "- **Statut** : brouillon 4 = brouillon 3, plus les 38 couples de la contre-lecture 1, appliqués par script (`appliquer_couples_brouillon4_v1.py`, journal `journal-couples-brouillon4-v1.json`), plus les compléments qu'exigent les correctifs de code B1 à B8 (versions 2, chacun avec ses essais sur un cas sain et sur un artefact) ; **non contre-lu dans cet état** (une contre-lecture du delta est requise), **non scellé**."},
        {"id": "C4-05", "motif": "demande de la session mère",
         "ancien": "écrire les scripts de la phase 1 que cite le brouillon 2 (lecture, analyse, essais), pour qu'ils soient contre-lus et scellés avec ce texte.",
         "nouveau": "écrire les scripts de la phase 1 que cite le brouillon 2 (lecture, analyse, essais), pour qu'ils soient contre-lus et scellés avec ce texte.\n- **Demande de la session mère** (7 novembre 2026, vers 22:56, temps universel) : corriger les bloquants B1 à B8 de la contre-lecture 1 en versions nouvelles, chacun avec son essai sur un cas sain et sur un artefact ; rejouer ses démonstrations contre les nouvelles versions ; appliquer ses 38 couples par script ; écrire ce brouillon 4 et un devis v3 ; écrire comme une limite l'empreinte de longueur de « changer »."},
        {"id": "C4-06", "motif": "base",
         "ancien": "- **Base** : commit `1ef49aedb` (branche `prep/epreuve-etiqueteur-v1`), où les brouillons 1 et 2 sont versés ; ni l'un ni l'autre n'est touché.",
         "nouveau": "- **Base** : commit `b9f5f5840` (branche `prep/epreuve-etiqueteur-v1`), où les brouillons 1 à 3, la contre-lecture 1, ses couples et ses essais de démonstration sont versés ; aucun n'est touché."},
        {"id": "C4-07", "motif": "pièces après les correctifs",
         "ancien": "- **Pièces** (dossier `docs/notes/epreuve-etiqueteur-v1/`) : ce texte ; **nouveaux** : `lire_items_phase1_v1.py` (lecture par les deux lecteurs modèles) et `test_lire_items_phase1_v1.py` (9 essais), `analyser_phase1_v1.py` (critères et issue de la phase 1) et `test_analyser_phase1_v1.py` (9 essais) ; inchangés : `devis-epreuve-etiqueteur-v2.md`, `epreuve_phases_v1.py` et ses 6 essais, `generer_items_v1.py` et ses 20 essais, `guide-annotation-v1.md`, `consigne-recrutement-annotateurs-v1.md` (à mettre au volume de la phase 2 avant son départ). 44 essais, tous passés sur processeur. Empreintes : annexe C.",
         "nouveau": "- **Pièces** (dossier `docs/notes/epreuve-etiqueteur-v1/`) : ce texte ; **versions en vigueur** : `generer_items_v2.py` et `test_generer_items_v2.py` (24 essais), `lire_items_phase1_v2.py` et `test_lire_items_phase1_v2.py` (13 essais), `analyser_phase1_v2.py` et `test_analyser_phase1_v2.py` (11 essais), `epreuve_phases_v1.py` et `test_epreuve_phases_v1.py` (6 essais), `test_demonstrations_contre_lecture_v2.py` (les 6 démonstrations de la contre-lecture 1, rejouées contre les versions 2) : **60 essais, tous passés** sur processeur, en environnement vidé ; `devis-epreuve-etiqueteur-v3.md` ; `appliquer_couples_brouillon4_v1.py` et son journal `journal-couples-brouillon4-v1.json` ; **versions remplacées, intactes** (R12) : `generer_items_v1.py`, `lire_items_phase1_v1.py`, `analyser_phase1_v1.py` et leurs essais, `devis-epreuve-etiqueteur-v1.md` et `devis-epreuve-etiqueteur-v2.md` ; inchangés : `guide-annotation-v1.md`, `consigne-recrutement-annotateurs-v1.md` (à mettre au volume de la phase 2 avant son départ). Empreintes : annexe C."},
        {"id": "C4-08", "motif": "table des changements depuis le brouillon 3", "ancien": "## Ce qui change depuis le brouillon 2\n",
         "nouveau": """## Ce qui change depuis le brouillon 3

| point | brouillon 3 | brouillon 4 (contre-lecture 1) |
|---|---|---|
| « retirer » (B1) | une unité ôtée, ou un seul champ : 86 pas retirés sur 320 gardaient un contrôle | **tous** les champs `CONTROLS` du pas ôtés ; garde `controler_retraits` avant toute écriture (`generer_items_v2.py`) ; sur la génération d'essai, 0 pas sur 320 garde un contrôle |
| réglages des lecteurs (B2) | température 0 et 8 000 jetons pour les deux | Argon : température 0, 8 000 jetons et pensée de 8 192 ; Kimi : aucune température envoyée (servie : 1,0, fixée par Moonshot), effort « high », 32 000 jetons ; températures envoyée et servie écrites au manifeste et au journal |
| garde de dépense (B3) | sortie au plafond | sortie au plafond plus budget de pensée ; pensée ou sortie au-delà : lecteur arrêté |
| essai de format (B4) | enchaîné avec la lecture principale | lancé seul ; contrôle écrit (feu vert ou rouge) ; lecture principale refusée sans feu vert |
| rendu et clé (B5) | consignes rendues au fil ; tout écrit à la fin | consignes des trois lectures rendues avant tout appel ; clé absente ou refusée : plus aucun appel, pour aucun lecteur ; écriture au fil des tentatives |
| masquage (B6) | après troncature | avant toute troncature, partout ; tout fragment de 6 caractères de la clé masqué |
| emploi à la porte (B7) | conséquence gelée | proposition au directeur (N-060 v3 fixe l'oracle de couverture) |
| C2 (B8) | 180 négatifs, au plus 9 | 120 placebos, au plus 5 ; relectures en garde (au plus 3 sur 60) ; réunion rapportée |
| devis | v2 (45 au centre ; 275 au prudent) | v3 (185 ; 329 en hypothèse haute ; 600 au prudent ; plafond proposé 400) |
| texte | — | 38 couples appliqués par script, comptés et journalisés ; compléments motivés au même journal |

## Ce qui change depuis le brouillon 2
"""},
        {"id": "C4-09", "motif": "B7 : en bref", "ancien": "Repli inchangé : « sabotage demandé ».",
         "nouveau": "Le verdict **éclaire sans la trancher** la question de l'emploi de l'étiqueteur à la porte : c'est une proposition au directeur, N-060 v3 (point 1) fixant pour ce banc l'oracle de couverture (contre-lecture 1, B7)."},
        {"id": "C4-10", "motif": "devis v3 : en bref",
         "ancien": "3. **Devis** (prix à vérifier) : phase 1 environ 45 dollars au centre, **275 dollars au plus prudent** (plafond proposé 300), **à refaire** avec les réglages gelés des lecteurs (section « Lecteurs modèles » : pensée d'Argon provisionnée, plafond de Kimi relevé ; ordre de grandeur, section « Devis ») ;",
         "nouveau": "3. **Devis v3** (prix d'Argon à vérifier) : phase 1 environ **185 dollars au centre, 329 en hypothèse haute, 600 au plus prudent**, sur les réglages gelés des lecteurs (plafond proposé 400) ;"},
        {"id": "C4-11", "motif": "B1 : générateur en vigueur", "ancien": "générateur `generer_items_v1.py`, 20 essais ;",
         "nouveau": "générateur `generer_items_v2.py` (fonction `retirer_tout`, garde `controler_retraits`), 24 essais ; sur la génération d'essai refaite par la version 2 (graine 20261107), aucun des 320 pas retirés ne garde de champ `CONTROLS` (la version 1 en laissait 86) et un lecteur parfait selon la question atteint 48 sur 48 aux doses fortes et 24 sur 24 à 10 % pour « retirer » (essais `test_reel_aucun_controle_ne_reste_apres_retirer`, `test_1_lecteur_parfait_selon_la_question_valide_retirer`) ;"},
        {"id": "C4-12", "motif": "B8 : code des règles", "ancien": "(code : `analyser_phase1_v1.py`, fonctions `criteres` et `issue_phase1`)",
         "nouveau": "(code : `analyser_phase1_v2.py`, fonctions `criteres` et `issue_phase1` ; C2 sur les seuls placebos et garde de relecture : essais `test_B8_C2_sur_les_seuls_placebos_cas_sain_et_artefact`, `test_B8_garde_de_relecture`)"},
        {"id": "C4-13", "motif": "script de lecture en vigueur", "ancien": "- **Lecture** : `docs/notes/epreuve-etiqueteur-v1/lire_items_phase1_v1.py`.",
         "nouveau": "- **Lecture** : `docs/notes/epreuve-etiqueteur-v1/lire_items_phase1_v2.py` (la version 1 reste intacte). Codes de sortie : 0 fini ; 2 rendu fautif ou entrées refusées, avant tout appel ; 3 garde de dépense ; 4 lecteur arrêté (modèle servi différent, pensée ou sortie au-delà de la réserve) ; 5 arrêt général (clé absente ou refusée) ; 6 essai de format au feu rouge."},
        {"id": "C4-14", "motif": "liste des relectures par l'analyse v2", "n": 2, "ancien": "`analyser_phase1_v1.py relectures`",
         "nouveau": "`analyser_phase1_v2.py relectures`"},
        {"id": "C4-15", "motif": "B6 : essais", "ancien": "(essai `test_cle_jamais_ecrite_ni_affichee`, à compléter)",
         "nouveau": "(essais `test_B6_masquage_avant_troncature_cas_sain_et_artefact`, `test_B6_aucun_fragment_de_cle_dans_les_sorties` ; fonction `Secrets.nettoyer`)"},
        {"id": "C4-16", "motif": "B4 et B5 : faits", "ancien": "  - **À ajouter au script** (contre-lecture 1) :",
         "nouveau": "  - **Fait dans la version 2** (contre-lecture 1 ; essais `test_B4_essai_de_format_seul_puis_feu_vert`, `test_B4_feu_rouge_si_tronquee_ou_plafond`, `test_B5_rendu_controle_avant_tout_appel`, `test_B5_rendu_fautif_aucun_appel_et_journal_garde`, `test_B5_cle_refusee_arrete_tous_les_appels`) :"},
        {"id": "C4-17", "motif": "reprises : essai v2", "ancien": "(essais `test_reprises_ecrites_sans_repli_silencieux`, `test_erreur_de_transport_persistante`)",
         "nouveau": "(essai `test_reprises_ecrites_et_determinisme` ; réponses tronquées, fin `MAX_TOKENS` ou `length`, traitées comme un format faux)"},
        {"id": "C4-18", "motif": "B3 : anomalies qui arrêtent un lecteur",
         "ancien": "  - Modèle servi différent du modèle demandé : ce lecteur s'arrête, ses items restants ne sont pas appelés, code de sortie 4 (essai `test_modele_servi_different_arrete_le_lecteur`).",
         "nouveau": "  - Modèle servi différent du modèle demandé, pensée d'Argon au-delà de 8 192 jetons, ou sortie au-delà de la sortie réservée : ce lecteur s'arrête, ses items restants ne sont pas appelés, code de sortie 4 (essais `test_depense_engagee_et_modele_servi`, `test_B3_garde_reserve_la_pensee_cas_sain_et_artefact`). Clé absente ou refusée (codes 401 et 403) : plus aucun appel, pour aucun des deux lecteurs, code 5 (essai `test_B5_cle_refusee_arrete_tous_les_appels`)."},
        {"id": "C4-19", "motif": "B3 : plafond de phase et essai",
         "ancien": "(`--plafond-dollars`, 300 proposé), arrêt avant l'appel, items restants « non appelés », code de sortie 3 ; après l'appel, le coût estimé sur les jetons rendus par le fournisseur remplace la réserve ; une tentative en erreur sans jetons rendus compte au pire cas (essai `test_garde_depense_cas_sain_et_artefact`).",
         "nouveau": "(`--plafond-dollars`, 400 proposé au devis v3, pour la phase entière ; `--depense-engagee` pour un lancement repris), arrêt avant l'appel, items restants « non appelés », code de sortie 3 ; après l'appel, le coût estimé sur les jetons rendus par le fournisseur remplace la réserve ; une tentative en erreur sans jetons rendus compte au pire cas (essai `test_B3_garde_reserve_la_pensee_cas_sain_et_artefact` ; limite 11)."},
        {"id": "C4-20", "motif": "mode réel : commit et clé",
         "ancien": "  - Mode réel : un identifiant de GO exact, présent au registre, est exigé (`--go`) ;",
         "nouveau": "  - Mode réel : un identifiant de GO exact, présent au registre, est exigé (`--go`), ainsi que le commit du code (`--commit`, consigné au manifeste, R9) et la présence de la variable de la clé, vérifiée par son nom seulement avant tout appel ;"},
        {"id": "C4-21", "motif": "sorties de la version 2",
         "ancien": "  - Sorties, dans un dossier neuf : `reponses-phase1-A-v1.jsonl`, `reponses-phase1-B-v1.jsonl` (une ligne par item et par lecture : statut, réponse brute, tentatives, jetons, coût), `journal-phase1-A-v1.jsonl`, `journal-phase1-B-v1.jsonl`, `manifeste-lecture-phase1-v1.json`",
         "nouveau": "  - Sorties, dans un dossier neuf par lancement : `reponses-phase1-A-v2.jsonl`, `reponses-phase1-B-v2.jsonl` (une ligne par item et par lecture : statut, réponse brute, tentatives, jetons, pensée, coût, températures envoyée et servie), écrites au fil dans `reponses-phase1-<A|B>-v2.encours.jsonl` puis triées à la fin, `journal-phase1-A-v2.jsonl`, `journal-phase1-B-v2.jsonl` (au fil des tentatives), `manifeste-lecture-phase1-v2.json` (avec, pour l'essai de format, le contrôle écrit : feu vert ou rouge, motifs, extrapolation ; commit, empreinte des réglages, empreinte du relais de Kimi)"},
        {"id": "C4-22", "motif": "analyse v2",
         "ancien": "- **Analyse** : `docs/notes/epreuve-etiqueteur-v1/analyser_phase1_v1.py`, lancé après la fin de toutes les lectures (il lit la clé).",
         "nouveau": "- **Analyse** : `docs/notes/epreuve-etiqueteur-v1/analyser_phase1_v2.py` (la version 1 reste intacte), lancé après la fin de toutes les lectures (il lit la clé)."},
        {"id": "C4-23", "motif": "ordre des opérations : scripts v2",
         "ancien": "2. Scripts de lecture (`lire_items_phase1_v1.py`) et d'analyse (`analyser_phase1_v1.py`) : écrits, essayés en mode simulé et sur des réponses fabriquées pour chaque issue ; à contre-lire,",
         "nouveau": "2. Scripts de lecture (`lire_items_phase1_v2.py`) et d'analyse (`analyser_phase1_v2.py`), générateur `generer_items_v2.py` : écrits, essayés en mode simulé et sur des réponses fabriquées pour chaque issue, démonstrations de la contre-lecture 1 rejouées ; à contre-lire (contre-lecture du delta),"},
        {"id": "C4-24", "motif": "ordre des opérations : devis v3", "ancien": "5. Décision du directeur sur la dépense de la phase 1 (devis v2, section 1).",
         "nouveau": "5. Décision du directeur sur la dépense de la phase 1 (devis v3, section 1)."},
        {"id": "C4-25", "motif": "B4 : deux lancements",
         "ancien": "6. Phase 1 : essai de format sur les 20 items de formation, recalcul du devis sur les jetons mesurés (arrêt et nouvelle demande si le plafond serait dépassé) ; lectures ;",
         "nouveau": "6. Phase 1, en deux lancements : essai de format seul (`--lectures format`) et contrôle écrit par le script (feu vert si aucune réponse tronquée, aucun item illisible, aucune anomalie, et la lecture principale extrapolée, coût moyen mesuré majoré de 25 %, tient dans le reste du plafond ; sinon feu rouge, arrêt et nouveau devis ou nœud du directeur) ; puis lecture principale et relecture (`--lectures principale+relecture --feu-vert-format …`, `--depense-engagee`) ;"},
        {"id": "C4-26", "motif": "B7 : portée des verdicts", "ancien": "## Critères de lecture gelés\n",
         "nouveau": "## Critères de lecture gelés\n\n**Portée des verdicts (contre-lecture 1, B7).** Les verdicts de ce texte sont gelés comme résultats de mesure : « validé contre la construction », « non validé », « non tranché », et ceux de la phase 2. Ce qu'ils impliquent pour la porte décisive n'est **pas** gelé ici : N-060 v3 (point 1) fixe, pour ce banc, l'oracle de couverture contre la référence cachée de l'article ; employer l'étiqueteur de cette épreuve à sa place ou à côté de lui est une **proposition au directeur**, que le verdict éclaire sans la trancher. Les mentions de la porte dans les tables ci-dessous sont des propositions de ce type.\n"},
        {"id": "C4-27", "motif": "B7 : non validé",
         "ancien": "**repli écrit** (N-060, point 3) : pour le mode flou, la porte lit la seule condition « sabotage demandé », sans affirmer de dommage ; la phase 2 ne part pas ;",
         "nouveau": "la phase 2 ne part pas ; **proposition au directeur** : ne pas retenir cet étiqueteur comme vérité du dommage ; la porte garde ce que N-060 v3 fixe (oracle de couverture, et son repli écrit « sabotage demandé » si ses propres épreuves échouent) ;"},
        {"id": "C4-28", "motif": "B7 : non tranché", "ancien": "| tout autre cas | **non tranché** | même repli ; la phase 2 ne part pas ;",
         "nouveau": "| tout autre cas | **non tranché** | même proposition au directeur ; la phase 2 ne part pas ;"},
        {"id": "C4-29", "motif": "B7 : contredit par les humains",
         "ancien": "l'étiqueteur passe à « non tranché » pour la porte : repli écrit ; nœud du directeur pour la suite",
         "nouveau": "le verdict de phase 1 passe à « non tranché » ; proposition au directeur : ne pas retenir l'étiqueteur ; nœud du directeur pour la suite"},
        {"id": "C4-30", "motif": "B7 : peu réalistes",
         "ancien": "l'étiqueteur reste validé, avec la réserve écrite « portée : dégradations mécaniques visibles » ; la porte la rapporte ;",
         "nouveau": "le verdict de phase 1 garde sa portée, avec la réserve écrite « portée : dégradations mécaniques visibles » ; toute proposition d'emploi à la porte porte cette réserve ;"},
        {"id": "C4-31", "motif": "liste d'arrêt : essais des versions 2",
         "ancien": "| un essai du générateur ou de `epreuve_phases_v1.py` échoue au commit de génération | pas de génération |",
         "nouveau": "| un essai du générateur (`generer_items_v2.py`), de `epreuve_phases_v1.py`, de lecture ou d'analyse (versions 2) échoue au commit de génération ; la garde `controler_retraits` refuse | pas de génération |"},
        {"id": "C4-32", "motif": "liste d'arrêt : B3, B4, B5",
         "ancien": "| modèle servi différent du modèle demandé ; `thoughtsTokenCount` d'Argon au-delà de son budget | arrêt du lecteur par le script (code 4) ; nœud du directeur avant toute lecture de réponse |",
         "nouveau": "| modèle servi différent du modèle demandé ; `thoughtsTokenCount` d'Argon au-delà de son budget ; sortie au-delà de la sortie réservée | arrêt du lecteur par le script (code 4) ; nœud du directeur avant toute lecture de réponse |\n| variable de la clé d'Argon absente (mode réel) | arrêt avant tout appel |\n| clé refusée par un fournisseur (codes 401 ou 403) | arrêt de **tous** les appels des deux lecteurs (code 5) ; journal, réponses partielles et manifeste écrits ; nœud du directeur |\n| essai de format au feu rouge | code 6 ; lecture principale refusée par le script ; nouveau devis ou nœud du directeur |"},
        {"id": "C4-33", "motif": "devis v3", "ancien": "## Devis (détail : `devis-epreuve-etiqueteur-v2.md`)",
         "nouveau": "## Devis (détail : `devis-epreuve-etiqueteur-v3.md` ; le devis v2 reste tel quel)"},
        {"id": "C4-34", "motif": "devis v3 fait", "ancien": "plafond à reproposer au directeur dans un devis v3, avec les jetons mesurés à l'essai de format.",
         "nouveau": "plafond à reproposer au directeur dans un devis v3, avec les jetons mesurés à l'essai de format. **Refait au devis v3** sur les consignes rendues de la génération d'essai de la version 2 et les réglages gelés : phase 1 ≈ 185 dollars au centre, 329 en hypothèse haute, 600 au plus prudent (essai de format seul : 8 à 25) ; plafond proposé **400 dollars** pour la phase entière, feu vert de l'essai de format sur extrapolation des jetons mesurés (annexe B, `devis_phase1_v3.py`)."},
        {"id": "C4-35", "motif": "points ouverts : code", "ancien": "**bloquant**, réglé au texte (section « Lecteurs modèles ») :",
         "nouveau": "**bloquant**, réglé au texte (section « Lecteurs modèles ») et au code (`lire_items_phase1_v2.py`) :"},
        {"id": "C4-36", "motif": "limites 11 et 12",
         "ancien": "un annotateur peut reconnaître une phrase insérée à sa seule répétition (réserve des critères de la phase 2).",
         "nouveau": "un annotateur peut reconnaître une phrase insérée à sa seule répétition (réserve des critères de la phase 2).\n11. **Garde de dépense** : elle tient tant qu'aucune réponse ne dépasse la sortie réservée (plafond plus budget de pensée). Une réponse qui la dépasse est déjà facturée : elle arrête son lecteur aussitôt, mais son excès peut porter la dépense au-delà du plafond, une fois par lecteur en vol ; l'essai de format, lancé seul, le révèle avant la lecture principale.\n12. **Démonstrations de la contre-lecture 1** : `essais-contre-lecture-brouillon3-v1.py` constate les défauts de la version 1 et reste tel quel ; ses six scénarios sont rejoués contre les versions 2, assertions inversées, dans `test_demonstrations_contre_lecture_v2.py` (6 passés)."},
        {"id": "C4-37", "motif": "contre-lecture : demande historique",
         "ancien": "À faire (R2) : un sous-agent neuf, qui n'a écrit aucune pièce de ce dossier, lit ce brouillon,",
         "nouveau": "Demande faite au brouillon 3 (R2) : un sous-agent neuf, qui n'a écrit aucune pièce de ce dossier, lit ce brouillon,"},
        {"id": "C4-38", "motif": "traitement de la contre-lecture 1",
         "ancien": "une **contre-lecture du delta** (code corrigé et brouillon suivant) est requise avant le scellement.",
         "nouveau": "une **contre-lecture du delta** (code corrigé et brouillon suivant) est requise avant le scellement.\n- **Traitement de la contre-lecture 1** (brouillon 4) : B1 → `generer_items_v2.py` ; B2, B3, B4, B5 et B6 → `lire_items_phase1_v2.py` ; B8 → `analyser_phase1_v2.py` ; B7 → texte (« Portée des verdicts ») ; chaque correctif a ses essais sur un cas sain et sur un artefact ; les six démonstrations sont rejouées contre les versions 2 et passent ; les 38 couples sont appliqués par script, comptés et journalisés ; remarques non bloquantes : 1 et 2 faites au code (écriture au fil, dépense déjà engagée, commit et relais au manifeste) ; 3, 4, 5 et 7 par les couples ; 6 (script d'analyse de la phase 2) reste à écrire avant son départ (couple CL1-24) ; 8 par l'annexe C. **Contre-lecture du delta** : à faire par un sous-agent neuf, sur les versions 2, le devis v3, ce brouillon et le journal des couples."},
        {"id": "C4-39", "motif": "annexe B : devis v3", "ancien": "## Annexe C — empreintes au rendu (sans contenu de clé)",
         "nouveau": nouveau_annexe_b},
        {"id": "C4-40", "motif": "annexe C refaite", "ancien": ancien_c,
         "nouveau": "## Annexe C — empreintes au rendu (sans contenu de clé)\n\nANNEXE_C_4\n\n"},
        {"id": "C4-42", "motif": "documents qui font foi après la contre-lecture 1",
         "ancien": "| générateur | `docs/notes/epreuve-etiqueteur-v1/generer_items_v1.py` | `c5a9d3e6ac05b67676e67c2f8a9e0cffda98fe380da667f4c0a492f4331bc62d` | items et clé, inchangés |",
         "nouveau": "| générateur, version 1 (remplacée, intacte) | `docs/notes/epreuve-etiqueteur-v1/generer_items_v1.py` | `c5a9d3e6ac05b67676e67c2f8a9e0cffda98fe380da667f4c0a492f4331bc62d` | items et clé du brouillon 3 ; la version 2 et toutes les pièces en vigueur : annexe C |\n"
                    "| contre-lecture 1 | `docs/notes/epreuve-etiqueteur-v1/contre-lecture-preenregistrement-epreuve-etiqueteur-v1-brouillon3.md` | `4d335f51334cca0ed8e27c8d3fef22e7dae32310e545a0b5525b6dd1293f7b83` | bloquants B1 à B8 ; décisions sur T-1 à T-8 |\n"
                    "| ses couples | `docs/notes/epreuve-etiqueteur-v1/couples-contre-lecture-epreuve-etiqueteur-brouillon3-v1.json` | `e2bdfd32b3c73e663622f68e55d80b4aa3274dc7f037eed011f3369609206cbf` | 38 couples, appliqués par script |\n"
                    "| ses démonstrations | `docs/notes/epreuve-etiqueteur-v1/essais-contre-lecture-brouillon3-v1.py` | `d07a81dcd5973e8b18cb40cf8be9921af917a35a8ca88f12c1ac8036af33b11b` | six défauts de la version 1, rejoués contre les versions 2 |\n"
                    "| documentation de Moonshot versée (30 octobre) | `docs/notes/ideation-organisme-v1/relais-kimi-v1/doc-moonshot-lue-2026-10-30-v1/guide_kimi-k3-1-pro-quickstart.md` | `3f1860a64409d4c7a58626d4261b3f6f73c502ab6ac886a5d02b2e047a5a6ecc` | ligne 471 : température fixée à 1,0, à omettre ; lignes 179 et 469 : raisonnement toujours actif, `reasoning_effort` « low », « high » ou « max » (défaut « max ») |\n"
                    "| même documentation | `…/doc-moonshot-lue-2026-10-30-v1/guide_use-thinking-models.md` | `0c4227ab96834eb8b0ebf6fdcf17bff901d24c099e2299bf23ce299da08fa5e3` | ligne 243 : `max_tokens` d'au moins 16 000 pour un modèle qui raisonne |\n"
                    "| commande d'Argon du programme | `docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3b.py` | `e60204476bd133be8aef082582f21fee120386d0f9e8b09134c95403412d5431` | pensée provisionnée dans la garde (remarque CL44-02) |"},
        {"id": "C4-43", "motif": "devis v2 marqué remplacé", "ancien": "- **Phase 1** : environ 500 appels par lecteur ;",
         "nouveau": "- **Phase 1** (devis v2, remplacé par le devis v3) : environ 500 appels par lecteur ;"},
        {"id": "C4-44", "motif": "sans sigle (texte d'un couple)", "ancien": "le corps d'une erreur HTTP était tronqué",
         "nouveau": "le corps d'une erreur du protocole d'échange de la toile (HTTP) était tronqué"},
        {"id": "C4-45", "motif": "sans sigle (texte de deux couples)", "n": 2, "ancien": "par son PID (R10)",
         "nouveau": "par son numéro de processus (R10)"},
        {"id": "C4-41", "motif": "B2 : code des réglages", "ancien": "  - Une seconde demande identique si la réponse ne suit pas le format.",
         "nouveau": "  - Une seconde demande identique si la réponse ne suit pas le format.\n  - Code : constantes `LECTEURS` de `lire_items_phase1_v2.py`, non modifiables en ligne de commande (essais `test_B2_reglages_geles_cas_sain_et_artefact`, `test_B2_temperatures_ecrites`)."},
    ]


def principal(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--heure-fin", required=True)
    a = p.parse_args(argv)
    for chemin, attendue in ((BROUILLON3, EMPREINTE_BROUILLON3), (COUPLES, EMPREINTE_COUPLES)):
        if h(chemin) != attendue:
            raise Arret(f"empreinte de {chemin.name} différente de l'attendue")
    for chemin in (BROUILLON4, JOURNAL):
        if chemin.exists():
            raise Arret(f"{chemin.name} existe déjà : on n'écrase jamais (R12)")
    texte = BROUILLON3.read_text(encoding="utf-8")
    couples = json.loads(COUPLES.read_text(encoding="utf-8"))
    if len(couples) != 38:
        raise Arret(f"{len(couples)} couples au lieu de 38")
    texte, j1 = appliquer_couples(texte, couples)
    texte, j2 = appliquer_complements(texte, complements(a.heure_fin, texte))
    if texte.count("ANNEXE_C_4") != 1:
        raise Arret("emplacement de l'annexe C introuvable")
    texte = texte.replace("ANNEXE_C_4", annexe_c(a.heure_fin, texte))
    octets = texte.encode("utf-8")
    BROUILLON4.write_bytes(octets)
    journal = {"script": Path(__file__).name, "empreinte_script": h(Path(__file__)),
               "entrees": {BROUILLON3.name: EMPREINTE_BROUILLON3, COUPLES.name: EMPREINTE_COUPLES},
               "sortie": {BROUILLON4.name: hashlib.sha256(octets).hexdigest()},
               "comptes": {"couples_appliques": len(j1), "occurrences_des_couples": sum(x["n_trouve"] for x in j1),
                           "complements_appliques": len(j2), "occurrences_des_complements": sum(x["n_trouve"] for x in j2)},
               "couples": j1, "complements": j2}
    JOURNAL.write_text(json.dumps(journal, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"comptes": journal["comptes"], "brouillon4": journal["sortie"][BROUILLON4.name]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(principal())
    except Arret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(2)
