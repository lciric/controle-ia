"""Ordre d'exécution de l'étape A de T0.7, variante B, brouillon 7 : application au brouillon 6 des couples des corrections du
code (configuration v8, script v3 écrit et répété, contrôle avant l'ouverture, `SRC7`, `ATT` à C7 ; R-2305, R-2306, R-2309), puis
vérifications, dont « tout le reste égal à l'octet au brouillon 6 » (v1).

Rédacteur du brouillon 6 et du candidat 2 de T0.7 (sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, Claude Opus
5.5), 11 novembre 2026, sur le message de la mère qui suit R-2309 (mêmes interdits et chemins que la consigne `d29c7858…`, aux noms
près). Bibliothèque standard et `bash -n` seulement ; aucun réseau, aucune clé, aucun `git`, aucun `vastai`.

    cd <dossier hors du dépôt> && <python du dépôt> -I -B <chemin absolu de ce script> RACINE

1. vérifie les empreintes du brouillon 6 (`92d9aebe…`), de la configuration v8 (`e31c7a79…`), du journal et du résumé de la
   répétition jouet v3 ; contrôle que la v8 cite les six chemins de la v4 et ne diffère de la v7 (`3701407c…`) que par les deux
   tolérances du palier « carte » ;
2. applique les couples `COUPLES` dans l'ordre : chaque « ancien » présent exactement une fois au moment de son application et
   différent de son « nouveau » ; sinon arrêt (code 1), rien n'est écrit ;
3. **tout le reste égal à l'octet** : défait les couples dans l'ordre inverse (chaque « nouveau » présent exactement une fois au
   moment où il est défait) et exige de retrouver le brouillon 6 octet pour octet ;
4. vérifie : titre ; les douze marqueurs (dont `ATT_C7_T07` neuf ; `SHA_SCRIPT_V3_T07` rempli), une occurrence chacun, aucun autre
   `<<…>>` ; empreinte du script v3 écrite dans la ligne (A) ; blocs `bash` (`bash -n`, marqueurs remplacés par des valeurs
   factices) ; extraits `python3 -I -c '…'` (`ast.parse`) ; choix de l'offre (§ 4.3) sur offres factices ; sommes du devis (§ 6)
   inchangées ; phrases exigées présentes ;
5. écrit `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon7.md` (R12 : refuse d'écraser un fichier différent ; un fichier
   identique est accepté). Le scellement se fait à part (`controle_ia.scellement sceller`).
Code 0 et « TOUT PASSE » si tout tient ; code 1 sinon.
"""
from __future__ import annotations

import ast
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

SHA_B6 = "92d9aebee0634c910ef622a80e4ff2cd33c91df6014ab6a4f04885c0023d2fca"
CHEMIN_B6 = "docs/procedures/ordre-execution-etape-a-t07-v1-brouillon6.md"
CHEMIN_B7 = "docs/procedures/ordre-execution-etape-a-t07-v1-brouillon7.md"
PIECES = "docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/"
V7, SHA_V7 = PIECES + "configuration-t07-v7.json", "3701407cf96f2851de26b04df174432a6e5325227c1e1f5a24900a1fa44ef6ab"
V8, SHA_V8 = PIECES + "configuration-t07-v8.json", "e31c7a79dc1b68d561874d4d42d63b5eb950931f06075927f239c7ad971fb328"
REP_J, SHA_REP_J = PIECES + "repetition-jouet-v3-journal.txt", "3d1421e72a7484566866e3a2169a7f00c5849f6a78ee936586e19a3e6d108b72"
REP_R, SHA_REP_R = PIECES + "repetition-jouet-v3-resume.json", "691b98cfb3eb474b947376de69ece37dc0a178596b8aed14ffbe7b8d99e69529"
RAPPORT2 = PIECES + "rapport-code-plancher-v3-v2.md"
SHA_RAPPORT2 = "71cc3b89c2df3c8f511796af0e3597844fb8fd1ec37735f0cbeae21d7b5ca231"
SHA_SCRIPT_V3 = "a19c594d268baadebea93c8ef0ea6c9406044971a928defd8c119b238d5f6560"
COMMIT_V3 = "7e23a554aca040016a08fe510504adec172c6998"
CANON_V8 = "0f32c6de1a6bf1f20ee2bf74c3839c2a2054b77c34a44a557dc821a83db60e12"
SIX_CHEMINS = ["diag/20261019-230011-p3-reel/sondes-figees.json", "donnees/20261007-082440-t05-extraction/taches-entrainement.json",
               "donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz", "donnees/T0.7-faits-repe-v1/facts_true_false.csv",
               "donnees/T0.7-models-under-pressure-v1/training/train.jsonl", "runs/20261019-230011-p3-reel/manifeste.json"]
TITRE_B7 = "# Ordre d'exécution — étape A de T0.7, variante B (instance A100 neuve, activations recalculées) — v1, brouillon 7"
MARQUEURS = ["<<ID_SESSION_FILLE>>", "<<EMPREINTE_CONFIG_T07>>", "<<LIGNE_SCELLEMENT_T07>>", "<<DEPENSE_ANTERIEURE_USD>>",
             "<<RUN_T06_7B>>", "<<BRANCHE_7B>>", "<<COMMIT_CODE_T07>>", "<<COMMIT_SCELLEMENT_T07>>", "<<CHEMIN_CONFIG_T07>>",
             "<<PERIMETRE_T07>>", "<<COMMIT_SRC_CONTRE_LU_T07>>", "<<ATT_C7_T07>>"]
FACTICES = {"<<DEPENSE_ANTERIEURE_USD>>": "0", "<<RUN_T06_7B>>": "20261112-000000-t06-reel",
            "<<BRANCHE_7B>>": "calcul/t06-confirmation-7b-v1", "<<COMMIT_CODE_T07>>": "0" * 40,
            "<<COMMIT_SCELLEMENT_T07>>": "1" * 40, "<<CHEMIN_CONFIG_T07>>": "prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json",
            "<<PERIMETRE_T07>>": "JD,JA", "<<COMMIT_SRC_CONTRE_LU_T07>>": "3" * 40,
            "<<ATT_C7_T07>>": "530 passed, 23 skipped, 3 xfailed"}
RAPPORT_CITE = f"rapport du code v2, `{RAPPORT2}` (`{SHA_RAPPORT2}`)"
REPET = (f"journal `{REP_J}` (`{SHA_REP_J}`) et résumé `{REP_R}` (`{SHA_REP_R}`), scellés")

COUPLES = [
    ("O7-01", "titre",
     "activations recalculées) — v1, brouillon 6\n",
     "activations recalculées) — v1, brouillon 7\n"),
    ("O7-02", "encadré : brouillon 7",
     "> devis relevé (+ 0,23 h attendu, + 0,66 h au pire), `ANT0` ≤ 3,6 USD.\n",
     "> devis relevé (+ 0,23 h attendu, + 0,66 h au pire), `ANT0` ≤ 3,6 USD.\n"
     "> **Brouillon 7 (R-2305, R-2306, R-2309)** : script v3 **écrit** (`a19c594d…`, commit `7e23a554` de `prep/t07-plancher-v3-v1`),\n"
     "> répété en jouet (17 verdicts sur 17) ; configuration v8 (palier « carte » à 10⁻³ et 10⁻²) ; contrôle avant l'ouverture à la\n"
     "> passe à blanc ; `SRC7` = commit de `main` qui fusionne la branche finale du code ; `ATT` mesurée à C7 (marqueur).\n"),
    ("O7-03", "statut du brouillon 7",
     "- **Statut** : **brouillon 6**, écrit le 2026-11-11 à partir de 03:00 UTC",
     "- **Statut** : **brouillon 7**, écrit le 2026-11-11 à partir de 04:09 UTC (`date -u`) par le rédacteur du brouillon 6 et du\n"
     "  candidat 2 de T0.7 (Claude Opus 5.5, `claude-opus-5-5`, même sous-agent de la session mère\n"
     "  `session_01VJdZpSMxSdk2SJ1ScmdfNv` ; exclu de tout rôle de lecteur de P3-bis), sur le message de la mère qui suit R-2309\n"
     "  (mêmes interdits et mêmes chemins que la consigne `d29c7858…`, aux noms près). **Brouillon 7 = brouillon 6**\n"
     f"  (`{SHA_B6}`, gardé tel quel, R12) **+ les couples O7-01 à O7-24** du script\n"
     "  `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon7-appliquer-v1.py`, chacun avec un « ancien » présent une fois ;\n"
     "  **tout le reste est égal à l'octet au brouillon 6** (vérifié par le script : les couples défaits dans l'ordre inverse\n"
     "  redonnent le brouillon 6 octet pour octet). Ce qui change et pourquoi : § 0 quater. **Non contre-lu** : à contre-lire (R2)\n"
     "  avant son scellement, avec le candidat 3 de T0.7.\n"
     "- **Brouillon 6** (statut gardé pour mémoire) : **brouillon 6**, écrit le 2026-11-11 à partir de 03:00 UTC"),
    ("O7-04", "section neuve « 0 quater »",
     "\n## 1. Cadre\n",
     "\n## 0 quater. Ce qui change depuis le brouillon 6 (brouillon 7 : corrections du code, script v3)\n\n"
     "Sources : contre-lecture du code du plancher v3 et décisions de la mère (R-2305 : CLP3-01 à CLP3-03, notes 05, 07, 10) ;\n"
     "R-2306 (questions du brouillon 6 tranchées : script v3 écrit par le développeur ; `SRC7` ; `ATT` à C7) ; R-2309 (corrections\n"
     f"rendues, commit `{COMMIT_V3}`, configuration v8, script v3, répétition jouet v3) ; {RAPPORT_CITE}.\n\n"
     "| Point | Où | Brouillon 6 | Brouillon 7 | Source |\n"
     "|---|---|---|---|---|\n"
     "| Script de l'instance | encadré ; § 1 ; ligne (A) ; P13 ; § 11 ; § 12 ; § 13 | v3 à écrire ; marqueur `SHA_SCRIPT_V3_T07` | **écrit** : "
     f"`scripts/etape_a_t07_variante_b_v3.sh`, `{SHA_SCRIPT_V3}`, commit `{COMMIT_V3[:8]}` ; marqueur **rempli** ; S-12 et S-13 réglés | "
     "R-2306, R-2309 ; rapport v2, § 5 |\n"
     "| Répétition jouet | § 1 ; § 11 | à faire | **17 verdicts sur 17 conformes** (un bras établi et un bras arrêté compris) | rapport v2, § 5 |\n"
     "| Configuration | § 1 | v7 (`4ff92c8e…`), chemin final `…-v7.json` | **v8** (`0f32c6de…`), chemin final "
     "`prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json` : palier « carte » 10⁻³ (témoin) et 10⁻² (directions) ; v7 refusée par la v4 | "
     "R-2305 (CLP3-01), R-2309 |\n"
     "| Passe à blanc | § 5, étape 12 | — | **contrôle avant l'ouverture** (CLP3-03) : sceaux de P3, principales, témoin, directions de P3, "
     "révision du modèle de P3 au cache hors ligne ; une faute refuse la passe (code 2) et l'étape A ne part pas | R-2305 ; rapport v2, § 4 |\n"
     "| Modèle de P3 au cache | § 5, étape 8 | préchargé si la révision diffère | plus : **contrôlé au cache hors ligne** (`revision_au_cache`) | "
     "rapport v2, § 5 |\n"
     "| Fautes de calcul de la réextraction ; état des figées | § 5, étape 13 | — | `MemoryError`, `TypeError`, `AttributeError`, "
     "`IndexError` : arrêt du seul bras (note 07) ; état des figées affiché par `etape-a-apres-repli` (note 10) | R-2305 |\n"
     "| Étape B | § 9 | `lecture_v4 etape-b` seule | plus : `n_plancher` directions exigées par plancher décisif (note 05) | R-2305 |\n"
     "| `SRC7` (C7) | § 1 ; P13 ; § 12 | dernier commit contre-lu du code, fusionné | **commit de `main` qui fusionne la branche finale du "
     "code** (arbre `src/`), fixé par la mère ; marqueur `COMMIT_SRC_CONTRE_LU_T07` laissé à la mère | R-2306 |\n"
     "| `ATT` (P12) | ligne (A) ; P12 ; § 4.1 ; § 11 bis ; § 12 | `346 passed, 2 skipped, 4 xfailed`, arbres `79230a58…` et `744a9e16…` | "
     "**mesurée à C7** par la mère (marqueur neuf `ATT_C7_T07`) ; le contrôle compare les arbres de S7 à ceux de C7 (P9 les égale) | "
     "R-2306 |\n"
     "| Taille des sorties | § 5 bis ; § 13, S-13 | constat (formule incomplète) | réglé par le script v3 : ≈ 1,87·10⁹ octets, sous 2·10⁹ | "
     "rapport v2, § 5 |\n\n"
     "Devis (§ 6), P8 et minuterie : inchangés (le rapport v2 garde le § 8 de la v1). Tout le reste est égal à l'octet au brouillon 6\n"
     "(vérifié par programme, statut).\n\n"
     "## 1. Cadre\n"),
    ("O7-05", "§ 1 : code de T0.7 (SRC7)",
     "`src/` égale celui de `SRC7` (ligne (A) ; **brouillon 6** : dernier commit contre-lu du code du remède (a'), vingt-six modules de "
     "`src/controle_ia/t07/`, `lecture_v4` compris, fusionné dans `main`, fixé par la mère, R-2304 ;",
     "`src/` égale celui de `SRC7` (ligne (A) ; **brouillon 7** (R-2306) : `SRC7` est le commit de `main` qui fusionne la branche "
     "finale du code du remède (a') (vingt-six modules ; à ce jour `7e23a554…` sur `prep/t07-plancher-v3-v1`, non fusionnée ; "
     "contre-lecture courte des corrections en cours) : `src/` de C7 égal à son arbre `src/`, fixé par la mère ; **brouillon 6** : "
     "dernier commit contre-lu du code du remède (a'), vingt-six modules de `src/controle_ia/t07/`, `lecture_v4` compris, fusionné "
     "dans `main`, fixé par la mère, R-2304 ;"),
    ("O7-06", "§ 1 : script de l'instance",
     "| Script de l'instance | **brouillon 6** : `scripts/etape_a_t07_variante_b_v3.sh`, sha256 au marqueur de la ligne (A) "
     "(`SHA_SCRIPT`) ; **à écrire** :",
     f"| Script de l'instance | **brouillon 7** : `scripts/etape_a_t07_variante_b_v3.sh`, sha256 `{SHA_SCRIPT_V3}` (433 lignes ; "
     f"commit `{COMMIT_V3}` de `prep/t07-plancher-v3-v1`, à fusionner dans `main` avec le code ; {RAPPORT_CITE}, § 5 : S-12 (1) à "
     "(5) et S-13 appliqués, S-1, S-3, S-4, S-8 à S-11 non appliqués) ; **répété en jouet de bout en bout** "
     "(`scripts/repetition_jouet_variante_b_t07_v3.py`, `d8dde1fb…` ; " + REPET + " : **17 verdicts sur 17 conformes**) ; "
     "contre-lecture courte des corrections en cours ; **brouillon 6** : `scripts/etape_a_t07_variante_b_v3.sh`, sha256 au "
     "marqueur de la ligne (A) (`SHA_SCRIPT`) ; **à écrire** :"),
    ("O7-07", "§ 1 : configuration v8",
     "; **brouillon 6** : **configuration v7**, chemin final **`prereg/T0.7-sondes-v0-v1-configuration-t07-v7.json`**",
     "; **brouillon 7** : **configuration v8**, chemin final **`prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json`** (copie octet "
     f"pour octet, faite par la mère au scellement de T0.7, de `{V8}`, sha256 du fichier `{SHA_V8[:12]}…`, avec son compagnon) : "
     "la v7 avec les seules tolérances du palier « carte » resserrées, `carte_sonde` 10⁻³ et `carte_directions` 10⁻² (R-2305, "
     "CLP3-01 ; vérifié par programme) ; mêmes six chemins cités ; seule `lecture_v4` au commit `7e23a554` l'accepte (elle refuse "
     "la v7, « tolérances fixées d'avance ») ; **brouillon 6** : **configuration v7**, chemin final "
     "**`prereg/T0.7-sondes-v0-v1-configuration-t07-v7.json`**"),
    ("O7-08", "§ 1 : empreinte canonique attendue",
     "(attendue pour la v7 : `4ff92c8e…`, `lecture_v4 empreinte-config`)",
     f"(attendue : `{CANON_V8[:12]}…` pour la v8, brouillon 7 ; `4ff92c8e…` pour la v7 au brouillon 6 ; `lecture_v4 empreinte-config`)"),
    ("O7-09", "P12 : ATT mesurée à C7",
     "| P12 | **Ligne d'essais `ATT`** (O-1) valable pour S7 :",
     "| P12 | **Ligne d'essais `ATT`** (O-1) valable pour S7 (**brouillon 7**, R-2306 : `ATT` est **mesurée à C7** par la mère, commande "
     "du § 11 bis, tête au commit C7, après la fusion du code ; valeur au marqueur de la ligne (A) ; elle vaut pour S7 parce que "
     "`src/` et `tests/` de S7 égalent ceux de C7, P9 : le contrôle du § 4.1 compare les arbres de S7 à ceux de C7 ; au brouillon 6, "
     "ci-après) :"),
    ("O7-10", "P13 : script v3",
     "(ii) **script v3** présent sur `main` à l'empreinte `SHA_SCRIPT`, répété en jouet et contre-lu (§ 13, S-12)",
     "(ii) **script v3** présent sur `main` à l'empreinte `SHA_SCRIPT` (brouillon 7 : `a19c594d…`, répété en jouet, 17 verdicts sur "
     "17 ; contre-lecture courte des corrections en cours ; § 13, S-12)"),
    ("O7-11", "P13 : SRC7",
     "(iii) **`SRC7`** fixé par la mère",
     "(iii) **`SRC7`** fixé par la mère (brouillon 7 : commit de `main` qui fusionne la branche finale du code)"),
    ("O7-12", "ligne (A) : ATT au marqueur",
     "ATT='346 passed, 2 skipped, 4 xfailed';",
     "ATT='<<ATT_C7_T07>>';"),
    ("O7-13", "ligne (A) : empreinte du script v3",
     "SHA_SCRIPT=<<SHA_SCRIPT_V3_T07>>;",
     f"SHA_SCRIPT={SHA_SCRIPT_V3};"),
    ("O7-14", "§ 4.1 : arbres de S7 comparés à ceux de C7",
     "[ \"$(git -C \"$M\" rev-parse \"$S7:tests\")\" = 79230a584e8675f1771fd4f0a9315de71c2bcbdc ] && [ \"$(git -C \"$M\" rev-parse "
     "\"$S7:src\")\" = 744a9e16f1635ff402e798b4ac868a57311e44b8 ]",
     "[ \"$(git -C \"$M\" rev-parse \"$S7:tests\")\" = \"$(git -C \"$M\" rev-parse \"$C7:tests\")\" ] && [ \"$(git -C \"$M\" rev-parse "
     "\"$S7:src\")\" = \"$(git -C \"$M\" rev-parse \"$C7:src\")\" ]"),
    ("O7-15", "§ 11 bis : mesure à C7",
     "- **Commande de remesure** (si P12 échoue) :",
     "- **Brouillon 7** (R-2306) : `ATT` se **mesure à C7**, avant la création, par la commande ci-dessous, la tête au commit C7 au\n"
     "  lieu de S7 (S7 en hérite par P9) ; la valeur va au marqueur `ATT_C7_T07` de la ligne (A) ; la mesure ci-dessus (brouillon 5)\n"
     "  ne vaut plus (cinq fichiers d'essais neufs ; rapport v2, § 7 : 530 passés, 23 sautés, 3 `xfail` dans l'arbre du développeur,\n"
     "  extraction réduite, non comparable).\n"
     "- **Commande de remesure** (si P12 échoue) :"),
    ("O7-16", "§ 5, étape 8 : révision de P3 contrôlée au cache",
     "(échec → arrêt de code 2, rien d'ouvert ; la réextraction ne télécharge jamais) ;",
     "(échec → arrêt de code 2, rien d'ouvert ; la réextraction ne télécharge jamais) ; **brouillon 7** : puis la révision\n"
     "   de P3 est **contrôlée au cache hors ligne** (`revision_au_cache`, `HF_HUB_OFFLINE=1` ; absente ou incomplète → code 2,\n"
     "   rien d'ouvert ; rapport v2, § 5, point 4) ;"),
    ("O7-17", "§ 5, étape 12 : contrôle avant l'ouverture",
     "12. **Passe à blanc** : `lecture_v4 passe-blanc` (brouillon 6 : `passe_blanc_v2`, configuration v7 ; `lecture_v2` au brouillon 5)",
     "12. **Passe à blanc** : `lecture_v4 passe-blanc` (brouillon 6 : `passe_blanc_v2`, configuration v7 ; `lecture_v2` au brouillon 5 ;\n"
     "    **brouillon 7** : **contrôle avant l'ouverture**, CLP3-03, `reextraction_p3_v1.controler_avant_ouverture`, joué juste après\n"
     "    le contrôle de configuration et avant tout calcul : sceaux des quatre entrées de P3, principales de P3 égales à la\n"
     "    configuration, témoin, directions de P3 et graine de la seconde garde, révision du modèle de P3 au cache lue hors ligne ; une\n"
     "    faute refuse la passe, code 2, rien d'écrit, et l'étape A ne part pas ; le résultat est écrit dans la sortie de la passe à\n"
     "    blanc, lisible par la fille, § 2.5 ; rapport v2, § 4)"),
    ("O7-18", "§ 5, étape 13 : notes 07 et 10",
     "planchers notés par lots (`plancher_v3`) (rapport du",
     "planchers notés par lots (`plancher_v3`) ; **brouillon 7** : une faute de calcul de la réextraction (`MemoryError`,\n"
     "    `TypeError`, `AttributeError`, `IndexError`) arrête le seul bras (note 07) ; `etape-a-apres-repli` affiche l'état du\n"
     "    plancher de chaque sonde figée, « établi » ou « échec », sans aire ni score (note 10) (rapport du"),
    ("O7-19", "§ 5 bis : borne du script v3",
     "avant le modèle : § 13, S-6.\n",
     "avant le modèle : § 13, S-6.\n\n"
     "**Brouillon 7** (S-13, script v3 ; rapport v2, § 5, point 6) : la borne compte aussi `nf × n_p3` nombres par action (directions\n"
     "de P3 notées en descriptif ; `nf` sondes figées nommées) et `planchers-figees-t07.npz` (`nf × P × 8 × (d + 1) + 2·10⁶` octets),\n"
     "écrits dans `taille-estimee.json` ; ordre de grandeur réel (non mesuré ; `d` = 4 096, `couches` = 3, `P` = 800, `K` = 2,\n"
     "`p6` = 1, `C` = 2, `L` = 4, `nf` = 2, `n_p3` = 200, ≈ 5 760 actions) : **≈ 1,87·10⁹ octets, sous la borne de 2·10⁹** (marge\n"
     "≈ 0,13·10⁹ ; à `n` plus grand d'environ 30 %, la borne arrête avant toute ouverture, code 2).\n"),
    ("O7-20", "§ 9 : étape B (note 05)",
     "étape B jouée à S7 (tête détachée ; brouillon 6 : `lecture_v4 etape-b` seule, la v2 et la v3 refusent la v7)",
     "étape B jouée à S7 (tête détachée ; brouillon 6 : `lecture_v4 etape-b` seule, la v2 et la v3 refusent la v7 ; brouillon 7 :\n"
     "  l'étape B exige de chaque sonde notée un plancher décisif de `n_plancher` directions, tableau et nombre écrit, sinon arrêt,\n"
     "  note 05 ; la v4 refuse aussi la v7)"),
    ("O7-21", "§ 11 : répétition du v3 faite",
     "avant que la mère remplisse `SHA_SCRIPT_V3_T07` ; non fait ici.",
     "avant que la mère remplisse `SHA_SCRIPT_V3_T07` ; non fait ici. **Brouillon 7** : **fait** par le développeur du code "
     "(`scripts/repetition_jouet_variante_b_t07_v3.py`, `d8dde1fb104ee2e61083f13dde226ef05341b33b6518f8aebe0bb93f20c34ce9`, commit "
     "`68882c2d` ; passage du 2026-11-11 de 03:34:57 à 03:53:24 UTC, configuration v8 jouet ; " + REPET + ") : **17 verdicts sur 17 "
     "conformes** — les douze de la v2 et cinq neufs (deux bras établis ; un bras arrêté par la garde d'identité, l'étape A au bout ; "
     "journal du v3 : `CUBLAS_WORKSPACE_CONFIG`, processeur, révision de P3 ; taille comptant les planchers des figées ; contrôle "
     "avant l'ouverture à la passe à blanc) ; constat : sur un processeur non EPYC, `ATEN_CPU_CAPABILITY=avx2` et `MKL_CBWR=AVX2` "
     "mettent, en jouet sur processeur, les gardes au palier « processeur » (en réel, la passe avant tourne sur la carte) ; "
     "marqueur `SHA_SCRIPT_V3_T07` rempli (ligne (A))."),
    ("O7-22", "§ 12 : marqueurs (SHA_SCRIPT_V3_T07 rempli, ATT_C7_T07 neuf)",
     "| `SHA_SCRIPT_V3_T07` (**neuf au brouillon 6**) | ligne (A) | sha256 de `scripts/etape_a_t07_variante_b_v3.sh` sur `main`, écrit, "
     "répété en jouet et contre-lu (§ 13, S-12) |",
     "| `SHA_SCRIPT_V3_T07` (**neuf au brouillon 6 ; rempli au brouillon 7**) | ligne (A) | sha256 de "
     "`scripts/etape_a_t07_variante_b_v3.sh` sur `main`, écrit, répété en jouet et contre-lu (§ 13, S-12) : "
     f"**`{SHA_SCRIPT_V3}`** (commit `{COMMIT_V3[:8]}`) |\n"
     "| `ATT_C7_T07` (**neuf au brouillon 7**) | ligne (A) | ligne d'essais attendue (`ATT`), mesurée par la mère à C7 après la "
     "fusion du code (§ 11 bis, tête au commit C7) ; P12 |"),
    ("O7-23", "§ 12 : description de COMMIT_SRC_CONTRE_LU_T07",
     "dernier commit contre-lu du code du remède (a') (vingt-six modules ; à ce jour `0d0c5da4061c28d808c3aa3b53c9a9a5e56a3a07`, "
     "non fusionné, contre-lecture en cours), dont `src/` est celui de C7 après fusion (R-2304) |\n",
     "**brouillon 7** (R-2306) : commit de `main` qui fusionne la branche finale du code du remède (a') (vingt-six modules ; à ce "
     f"jour `{COMMIT_V3}` sur `prep/t07-plancher-v3-v1`, non fusionnée ; contre-lecture courte des corrections en cours) : `src/` "
     "de C7 égal à son arbre `src/` ; au brouillon 6 : dernier commit contre-lu du code du remède (a') (vingt-six modules ; à ce "
     "jour `0d0c5da4061c28d808c3aa3b53c9a9a5e56a3a07`, non fusionné, contre-lecture en cours), dont `src/` est celui de C7 après "
     "fusion (R-2304) |\n"),
    ("O7-24", "§ 13 : S-12 et S-13 réglés",
     "S-13 est un constat du rédacteur du brouillon 6.",
     "S-13 est un constat du rédacteur du brouillon 6. **Brouillon 7** : **S-12 et S-13 sont réglés par le script v3**\n"
     f"(`{SHA_SCRIPT_V3}`, commit `{COMMIT_V3[:8]}` ; rapport v2, § 5) ; S-1, S-3, S-4, S-8 à S-11 n'y sont pas appliqués (au\n"
     "choix de la mère) ; S-2, S-5, S-6, S-7 inchangés."),
]

EXIGEES = (
    "## 0 quater. Ce qui change depuis le brouillon 6", f"SHA_SCRIPT={SHA_SCRIPT_V3};", "ATT='<<ATT_C7_T07>>';",
    "`prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json`", "**17 verdicts sur 17 conformes**", "**contrôle avant l'ouverture**",
    "`revision_au_cache`", "≈ 1,87·10⁹ octets", "commit de `main` qui fusionne la branche finale du code", "**mesurée à C7**",
    "= \"$(git -C \"$M\" rev-parse \"$C7:tests\")\"", SHA_REP_J, SHA_REP_R, "note 05", "note 07", "note 10",
    "**3,2 à 4,7**", "**8,6 à 11,6**", "**`ANT0` ≤ 3,6 USD**",
)


def sha(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def echec(motif: str) -> None:
    print(f"ÉCHEC : {motif}")
    sys.exit(1)


def remplacer(texte: str, ident: str, ancien: str, nouveau: str) -> str:
    n = texte.count(ancien)
    if n != 1:
        echec(f"{ident} : « ancien » présent {n} fois (une attendue)")
    if ancien == nouveau:
        echec(f"{ident} : « ancien » égal au « nouveau »")
    return texte.replace(ancien, nouveau)


def blocs_bash(texte: str) -> list[str]:
    return re.findall(r"```bash\n(.*?)```", texte, flags=re.S)


def chemins_cites(x):
    if isinstance(x, dict):
        if isinstance(x.get("chemin"), str):
            yield x["chemin"]
        for v in x.values():
            yield from chemins_cites(v)
    elif isinstance(x, list):
        for v in x:
            yield from chemins_cites(v)


def essai_offre(texte: str) -> None:
    b = next(x for x in blocs_bash(texte) if "vastai search offers" in x)
    extrait = re.search(r"python3 -I -c '([^']*)' \"\$W/offres.json\"", b).group(1)
    base = {"gpu_name": "A100 SXM4", "num_gpus": 1, "gpu_ram": 81920, "storage_total_cost": 0.05, "inet_down_cost": 0.01,
            "inet_up_cost": 0.01, "machine_id": 1, "cuda_max_good": 13.0}
    cas = [([{**base, "id": 1, "dph_total": 0.9, "cpu_name": "Intel Xeon"}, {**base, "id": 2, "dph_total": 1.2, "cpu_name": "AMD EPYC 7513"},
             {**base, "id": 3, "dph_total": 1.1, "cpu_name": "AMD EPYC 7J13"}], "id=3 "),
           ([{**base, "id": 4, "dph_total": 1.0, "cpu_name": "Intel Xeon"}, {**base, "id": 5, "dph_total": 0.95}], "id=5 "),
           ([], "aucune offre")]
    with tempfile.TemporaryDirectory() as d:
        for offres, attendu in cas:
            p = Path(d) / "offres.json"
            p.write_text(json.dumps({"offers": offres}), encoding="utf-8")
            r = subprocess.run([sys.executable, "-I", "-c", extrait, str(p)], capture_output=True, text=True)
            if r.returncode != 0 or not r.stdout.startswith(attendu):
                echec(f"§ 4.3 : choix de l'offre {r.stdout.strip()!r} (attendu {attendu!r}) {r.stderr.strip()[:200]}")
    print("§ 4.3 : choix de l'offre essayé sur trois cas factices : conforme (bloc inchangé depuis le brouillon 6)")


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        echec("usage : appliquer RACINE")
    racine = Path(argv[0]).resolve()
    for chemin, attendu in ((CHEMIN_B6, SHA_B6), (V7, SHA_V7), (V8, SHA_V8), (REP_J, SHA_REP_J), (REP_R, SHA_REP_R),
                            (RAPPORT2, SHA_RAPPORT2)):
        e = sha((racine / chemin).read_bytes())
        if e != attendu:
            echec(f"{chemin} : empreinte {e[:12]}… ≠ {attendu[:12]}…")
    c7 = json.loads((racine / V7).read_text(encoding="utf-8"))
    c8 = json.loads((racine / V8).read_text(encoding="utf-8"))
    cles = sorted(k for k in set(c7) | set(c8) if c7.get(k) != c8.get(k))
    pf7, pf8 = c7["plancher_figees"], c8["plancher_figees"]
    sous = sorted(k for k in set(pf7) | set(pf8) if pf7.get(k) != pf8.get(k))
    tol = pf8["tolerances"]
    if (cles != ["plancher_figees"] or sous != ["tolerances"] or tol != {"processeur": 1e-06, "carte_sonde": 0.001, "carte_directions": 0.01}
            or sorted(set(chemins_cites(c8))) != SIX_CHEMINS):
        echec(f"configuration v8 : clés {cles}, sous-clés {sous}, tolérances {tol}")
    print(f"brouillon 6, configurations v7 et v8, répétition v3 et rapport v2 vérifiés ; v7 → v8 : seules les tolérances du palier "
          f"« carte » changent ({tol}) ; six chemins cités")
    resume = json.loads((racine / REP_R).read_text(encoding="utf-8"))
    verdicts = resume.get("verdicts", {})
    if resume.get("conforme") is not True or len(verdicts) != 17 or not all(v is True for v in verdicts.values()):
        echec(f"répétition v3 : conforme {resume.get('conforme')!r}, {len(verdicts)} verdicts")
    print(f"répétition v3 : conforme, {sum(v is True for v in verdicts.values())} verdicts sur {len(verdicts)} vrais")
    texte6 = (racine / CHEMIN_B6).read_bytes().decode("utf-8")
    texte = texte6
    ids = [c[0] for c in COUPLES]
    if len(set(ids)) != len(ids) or ids != [f"O7-{k:02d}" for k in range(1, len(ids) + 1)]:
        echec("identifiants de couples")
    for ident, ou, ancien, nouveau in COUPLES:
        texte = remplacer(texte, f"{ident} ({ou})", ancien, nouveau)
    print(f"{len(COUPLES)} couples appliqués, chacun à une occurrence")
    defait = texte
    for ident, ou, ancien, nouveau in reversed(COUPLES):
        n = defait.count(nouveau)
        if n != 1:
            echec(f"défaisage de {ident} : « nouveau » présent {n} fois (une attendue)")
        defait = defait.replace(nouveau, ancien)
    if defait != texte6:
        echec("les couples défaits ne redonnent pas le brouillon 6 octet pour octet")
    l6, l7 = texte6.split("\n"), texte.split("\n")
    print(f"tout le reste égal à l'octet : couples défaits dans l'ordre inverse → brouillon 6 retrouvé ({len(l6)} → {len(l7)} lignes)")
    if l7[0] != TITRE_B7:
        echec("titre du brouillon 7")
    for m in MARQUEURS:
        if texte.count(m) != 1:
            echec(f"marqueur {m} : {texte.count(m)} occurrences (une attendue)")
    autres = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", texte)) - set(MARQUEURS))
    if autres:
        echec(f"marqueurs inattendus : {autres}")
    print(f"marqueurs : {len(MARQUEURS)}, une occurrence chacun (`ATT_C7_T07` neuf ; `SHA_SCRIPT_V3_T07` rempli), aucun autre")
    for p in EXIGEES:
        if p not in texte:
            echec(f"phrase exigée absente : {p!r}")
    print(f"phrases exigées : {len(EXIGEES)} présentes")
    s6 = texte[texte.index("## 6. Devis"):texte.index("## 7. Arrêts")]
    if s6 != texte6[texte6.index("## 6. Devis"):texte6.index("## 7. Arrêts")]:
        echec("§ 6 changé")
    print("§ 6 (devis, plafond, marge) égal à celui du brouillon 6")
    blocs = blocs_bash(texte)
    if len(blocs) != 8:
        echec(f"{len(blocs)} blocs bash (8 attendus)")
    n_py = 0
    with tempfile.TemporaryDirectory() as d:
        for k, b in enumerate(blocs, 1):
            for m, v in FACTICES.items():
                b = b.replace(m, v)
            p = Path(d) / f"bloc-{k}.sh"
            p.write_text(b, encoding="utf-8")
            r = subprocess.run(["bash", "-n", str(p)], capture_output=True, text=True)
            if r.returncode != 0:
                echec(f"bloc bash {k} : bash -n en échec : {r.stderr.strip()[:300]}")
            for extrait in re.findall(r"python3 -I -c '([^']*)'", b):
                try:
                    ast.parse(extrait)
                except SyntaxError as e:
                    echec(f"bloc bash {k} : extrait Python illisible ({e})")
                n_py += 1
    print(f"blocs bash : {len(blocs)}, bash -n sans erreur ; extraits Python : {n_py}, ast.parse sans erreur")
    essai_offre(texte)
    sortie = racine / CHEMIN_B7
    octets = texte.encode("utf-8")
    if sortie.exists() and sortie.read_bytes() != octets:
        echec(f"{CHEMIN_B7} existe avec un autre contenu (R12)")
    if not sortie.exists():
        sortie.write_bytes(octets)
    print(f"écrit : {CHEMIN_B7} ({sha(octets)})")
    print("TOUT PASSE")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
