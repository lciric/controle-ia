"""Ordre d'exécution de l'étape A de T0.7, variante B, brouillon 8 : application au brouillon 7 des couples du dernier tour (script
v4 et contrôle avant l'ouverture, R-2311 à R-2313 ; couples VC3-C et VC3-D de la vérification courte, tels qu'écrits, R-2312 ;
CLC-P3-04 et CLC-P3-07 ; réserves neuves), puis vérifications, dont « tout le reste égal à l'octet au brouillon 7 » (v1).

Rédacteur des brouillons 6 et 7 et des candidats 2 et 3 de T0.7 (sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`,
Claude Opus 5.5), 11 novembre 2026, sur le message de la mère qui suit R-2313 (mêmes interdits et chemins que la consigne
`d29c7858…`, aux noms près). Bibliothèque standard et `bash -n` seulement ; aucun réseau, aucune clé, aucun `git`, aucun `vastai`.

    cd <dossier hors du dépôt> && <python du dépôt> -I -B <chemin absolu de ce script> RACINE

1. vérifie les empreintes du brouillon 7 (`d799a01b…`), de la vérification courte du candidat 3 (`cfeeae9c…`), du rapport du code
   v3, de la contre-lecture courte, du journal et du résumé de la répétition jouet v4 (10 verdicts vrais sur 10) ;
2. lit VC3-C et VC3-D dans le bloc JSON du § 4 de la vérification courte et les applique **tels qu'écrits**, à leur place dans
   la suite des couples ; chaque « ancien » présent exactement une fois au moment de son application ; sinon arrêt (code 1) ;
3. **tout le reste égal à l'octet** : défait les couples dans l'ordre inverse et exige de retrouver le brouillon 7 octet pour octet ;
4. vérifie : titre ; douze marqueurs, une occurrence chacun, aucun autre ; empreinte du script v4 à la ligne (A) ; blocs `bash`
   (`bash -n`, valeurs factices) ; extraits `python3 -I -c '…'` (`ast.parse`) ; choix de l'offre (§ 4.3) sur offres factices ;
   § 6 (devis) égal au brouillon 7 ; phrases exigées présentes ;
5. écrit `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon8.md` (R12). Le scellement se fait à part.
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

CHEMIN_B7, SHA_B7 = "docs/procedures/ordre-execution-etape-a-t07-v1-brouillon7.md", "d799a01bd6008d73794a42dd8b4657c4498ca291bcbd64b771711cf6632a5916"
CHEMIN_B8 = "docs/procedures/ordre-execution-etape-a-t07-v1-brouillon8.md"
VC, SHA_VC = ("prereg/contre-lectures/T0.7-sondes-v0-v1-candidat3-verification-courte-v1.md",
              "cfeeae9c0a3425002f75be94abd9fa32de5e7bd8f7c810d2df4d10410e47aa06")
PIECES = "docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/"
RAP3, SHA_RAP3 = PIECES + "rapport-code-plancher-v3-v3.md", "be2c86e215a1a7a0e41f646e60acaa20a39f0b626c6cd1b0807066348305b159"
CLC, SHA_CLC = PIECES + "contre-lecture-courte-corrections-plancher-v3-v1.md", "6f3769116d2432be4f5b201774307bdfcdbf25cc5b8cb664c61740b8ce0aabf7"
CL1, SHA_CL1 = PIECES + "contre-lecture-code-plancher-v3-v1.md", "32cbc637386d02ad6b90983beb8f675fc1b92c129a20db93e8af22c6b79c9f80"
REP_J, SHA_REP_J = PIECES + "repetition-jouet-v4-journal.txt", "98412f28c9d0dc446db86d73d51e1aa1ae3615545d242b5478e8de8bb9fb265c"
REP_R, SHA_REP_R = PIECES + "repetition-jouet-v4-resume.json", "c36839fe2016ccea200ee5fa28c7a7116f457821d576ee93b88fbfb4d4b4f2e2"
SHA_SCRIPT_V4 = "4b17d1f05441f5206d9f4ac58fb5ccf2b755bd86c13bee622ccf3bc327df05c6"
COMMIT = "a621dcd3b929ce3ebd615fa852d4a7f5c103071d"
TITRE_B8 = "# Ordre d'exécution — étape A de T0.7, variante B (instance A100 neuve, activations recalculées) — v1, brouillon 8"
MARQUEURS = ["<<ID_SESSION_FILLE>>", "<<EMPREINTE_CONFIG_T07>>", "<<LIGNE_SCELLEMENT_T07>>", "<<DEPENSE_ANTERIEURE_USD>>",
             "<<RUN_T06_7B>>", "<<BRANCHE_7B>>", "<<COMMIT_CODE_T07>>", "<<COMMIT_SCELLEMENT_T07>>", "<<CHEMIN_CONFIG_T07>>",
             "<<PERIMETRE_T07>>", "<<COMMIT_SRC_CONTRE_LU_T07>>", "<<ATT_C7_T07>>"]
FACTICES = {"<<DEPENSE_ANTERIEURE_USD>>": "0", "<<RUN_T06_7B>>": "20261112-000000-t06-reel",
            "<<BRANCHE_7B>>": "calcul/t06-confirmation-7b-v1", "<<COMMIT_CODE_T07>>": "0" * 40,
            "<<COMMIT_SCELLEMENT_T07>>": "1" * 40, "<<CHEMIN_CONFIG_T07>>": "prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json",
            "<<PERIMETRE_T07>>": "JD,JA", "<<COMMIT_SRC_CONTRE_LU_T07>>": "3" * 40,
            "<<ATT_C7_T07>>": "530 passed, 23 skipped, 3 xfailed"}
CLC_CITE = f"contre-lecture courte des corrections, `{CLC}` (`6f3769116d2432be4f5b…`, Claude Fable 5.2, R-2311 : sans défaut bloquant)"
RAP3_CITE = f"rapport du code v3, `{RAP3}` (`be2c86e215a1…`)"
REPET4 = (f"journal `{REP_J}` (`{SHA_REP_J}`) et résumé `{REP_R}` (`{SHA_REP_R}`), scellés")

COUPLES = [
    ("O8-01", "titre", "activations recalculées) — v1, brouillon 7\n", "activations recalculées) — v1, brouillon 8\n"),
    ("O8-02", "encadré : script", "> Script de l'instance : **`scripts/etape_a_t07_variante_b_v3.sh`**, neuf arguments",
     "> Script de l'instance : **`scripts/etape_a_t07_variante_b_v4.sh`** (brouillon 8 ; v3 aux brouillons 6 et 7), neuf arguments"),
    ("O8-03", "encadré : brouillon 8",
     "> passe à blanc ; `SRC7` = commit de `main` qui fusionne la branche finale du code ; `ATT` mesurée à C7 (marqueur).\n",
     "> passe à blanc ; `SRC7` = commit de `main` qui fusionne la branche finale du code ; `ATT` mesurée à C7 (marqueur).\n"
     "> **Brouillon 8 (R-2311 à R-2313)** : script **v4** (`4b17d1f0…`, commit `a621dcd3`), qui joue `lecture_v4\n"
     "> controle-avant-ouverture` à l'étape 8, avant toute ouverture ; répétition jouet v4 (10 verdicts sur 10) ; arrêt technique\n"
     "> d'un bras de la réextraction (CLC-P3-04) ; nombre d'actions de 7b compté avant la création (P14) ; couples VC3-C et VC3-D.\n"),
    ("O8-04", "statut du brouillon 8",
     "- **Statut** : **brouillon 7**, écrit le 2026-11-11 à partir de 04:09 UTC",
     "- **Statut** : **brouillon 8**, écrit le 2026-11-11 à partir de 04:59 UTC (`date -u`) par le rédacteur des brouillons 6 et 7\n"
     "  (Claude Opus 5.5, `claude-opus-5-5`, même sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv` ; exclu de tout\n"
     "  rôle de lecteur de P3-bis), sur le message de la mère qui suit R-2313. **Brouillon 8 = brouillon 7**\n"
     f"  (`{SHA_B7}`, gardé tel quel, R12) **+ les couples O8-01 à O8-25**, dont **VC3-C et VC3-D de la vérification\n"
     "  courte du candidat 3, tels qu'écrits** (lus dans son § 4 par le script\n"
     "  `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon8-appliquer-v1.py`) ; **tout le reste est égal à l'octet au\n"
     "  brouillon 7** (vérifié par le script : couples défaits → brouillon 7). Ce qui change et pourquoi : § 0 quinquies. **Non\n"
     "  contre-lu** : à contre-lire (R2) avec le candidat 4 de T0.7 avant son scellement.\n"
     "- **Brouillon 7** (statut gardé pour mémoire) : **brouillon 7**, écrit le 2026-11-11 à partir de 04:09 UTC"),
    ("O8-05", "section neuve « 0 quinquies »", "\n## 1. Cadre\n",
     "\n## 0 quinquies. Ce qui change depuis le brouillon 7 (brouillon 8 : dernier tour du code, script v4)\n\n"
     f"Sources : R-2311 ({CLC_CITE}) ; R-2312 (vérification courte du candidat 3 et de l'ordre 7, `{VC}`, `cfeeae9c…`, « après "
     f"corrections », aucun nœud ; couples VC3-C et VC3-D) ; R-2313 ({RAP3_CITE} ; code final `{COMMIT}`).\n\n"
     "| Point | Où | Brouillon 7 | Brouillon 8 | Source |\n|---|---|---|---|---|\n"
     f"| Script de l'instance | encadré ; § 1 ; ligne (A) ; P13 ; § 5 ; § 11 ; § 12 ; § 13 | v3, `a19c594d…` | **v4**, `{SHA_SCRIPT_V4}` "
     "(commit `a621dcd3`) : le v3 plus `lecture_v4 controle-avant-ouverture` à l'étape 8 et les formes sûres sous `set -u` ; le v3 reste "
     "intact | R-2311 (CLC-P3-02, -05), R-2313 |\n"
     "| Contrôle avant l'ouverture | § 5, étape 8 | contrôle du cache seul avant le repli ; contrôle entier à la passe à blanc, après la "
     "garde d'ouverture | contrôle **entier** à l'étape 8, avant l'empreinte, `CODE-T07`, la branche, le repli et sa garde d'ouverture ; "
     "faute → code 2, rien d'ouvert | CLC-P3-02 |\n"
     "| Répétition jouet | § 11 | v3, 17 sur 17 | **v4, 10 sur 10** (artefact « témoin retiré » arrêté à l'étape 8) | R-2313 |\n"
     "| P12 (`ATT`) | § 3 | « elle vaut pour S7 parce que … » | **couple VC3-C tel qu'écrit** : `ATT` liée au commit de la mesure ; "
     "remesure à S7 si un fichier lu hors de `src/` et `tests/` change | R-2312 |\n"
     "| P13 (`SRC7`) | § 3 | `SRC7` fixé par la mère | **couple VC3-D tel qu'écrit** : la mère écrit que l'arbre `src/` de `SRC7` "
     "est celui du dernier commit contre-lu, ou nomme les fichiers qui diffèrent | R-2312 |\n"
     "| Nombre d'actions de 7b | P14 (neuf) ; § 5 bis | — | compté par la mère sur processeur avant la création ; ≤ ≈ 7 378, sinon "
     "arrêt | CLC-P3-07 |\n"
     "| Arrêt technique d'un bras | § 5, étape 13 ; § 7 ; § 8 | — | motif qui ne commence pas par `GardeArret` : arrêt technique, "
     "réserve, nœud de Lazar avant l'étape B ; la fille rapporte l'état des bras | CLC-P3-04 |\n"
     "| Réserves neuves | § 13 (S-14 à S-17) ; § 11 bis | — | bash < 4.4 non éprouvé (refus d'un classifieur rapporté, non "
     "contourné) ; branche « autre révision » non éprouvable hors ligne ; morceau de poids tronqué non vide admis ; suite "
     "`tests/test_t07_*` rejouée entière par la mère à C7 | R-2313 |\n"
     "| Mentions « en cours » | § 1 ; P13 ; § 12 | contre-lecture courte des corrections « en cours » | rendue, citée | R-2311 |\n\n"
     "Devis (§ 6), P8 et minuterie : inchangés. Tout le reste est égal à l'octet au brouillon 7 (vérifié par programme, statut).\n\n"
     "## 1. Cadre\n"),
    ("O8-06", "§ 1 : code (commit final, contre-lecture rendue)",
     "à ce jour `7e23a554…` sur `prep/t07-plancher-v3-v1`, non fusionnée ; contre-lecture courte des corrections en cours) : `src/` de "
     "C7 égal à son arbre `src/`, fixé par la mère ;",
     f"à ce jour **`{COMMIT[:8]}…`** sur `prep/t07-plancher-v3-v1` (brouillon 8 ; `7e23a554…` au brouillon 7), non fusionnée ; "
     f"{CLC_CITE} ; {RAP3_CITE}) : `src/` de C7 égal à son arbre `src/`, fixé par la mère (P13, (iii)) ;"),
    ("O8-07", "§ 1 : script v4", "| Script de l'instance | **brouillon 7** :",
     f"| Script de l'instance | **brouillon 8** : `scripts/etape_a_t07_variante_b_v4.sh`, sha256 `{SHA_SCRIPT_V4}` (commit "
     f"`{COMMIT}` de `prep/t07-plancher-v3-v1`, à fusionner dans `main` avec le code ; {RAP3_CITE}, § 2 et § 4 : le v3 plus "
     "l'étape 8 qui joue `lecture_v4 controle-avant-ouverture` avant l'empreinte, `CODE-T07`, la branche, le repli et sa garde "
     "d'ouverture, et les formes sûres sous `set -u` ; le v3 reste intact) ; **répété en jouet** "
     "(`scripts/repetition_jouet_variante_b_t07_v4.py`, `8b0e9590…` ; " + REPET4 + " : **10 verdicts sur 10**, l'artefact « témoin "
     "retiré » arrêté en code 2 à l'étape 8 sans rien ouvrir) ; **brouillon 7** :"),
    ("O8-08", "§ 1 : script (mention « en cours » du brouillon 7)",
     "**17 verdicts sur 17 conformes**) ; contre-lecture courte des corrections en cours ;",
     "**17 verdicts sur 17 conformes**) ; contre-lecture courte des corrections rendue depuis (R-2311) ;"),
    ("O8-09", "P12 (couple VC3-C)", "@@VC3-C@@", "@@VC3-C@@"),
    ("O8-10", "P13, (ii) : script v4", "répété en jouet, 17 verdicts sur 17 ; contre-lecture courte des corrections en cours ; § 13, S-12)",
     "répété en jouet, 17 verdicts sur 17 ; contre-lecture courte des corrections rendue depuis, R-2311 ; **brouillon 8** : script "
     "v4, `4b17d1f0…`, répété en jouet, 10 verdicts sur 10 ; § 13, S-12)"),
    ("O8-11", "P13, (iii) (couple VC3-D)", "@@VC3-D@@", "@@VC3-D@@"),
    ("O8-12", "P14 neuf : nombre d'actions de 7b",
     "| § 4.1 | (i) égale : rien ; autre : écrit au journal, le v3 précharge la révision de P3 (§ 5, étape 8) ; (ii), (iii) absents : "
     "rien |\n",
     "| § 4.1 | (i) égale : rien ; autre : écrit au journal, le v3 précharge la révision de P3 (§ 5, étape 8) ; (ii), (iii) absents : "
     "rien |\n"
     "| P14 | **Brouillon 8 (CLC-P3-07)** : **nombre d'actions notées de 7b** (`n` du § 5 bis : actions à `jetons_notes` > 0 de "
     "`donnees/<RUN6>/mesures-t06.npz` de 7b, sceau vérifié, colonne `jetons_notes` seule) **compté par la mère sur processeur**, "
     "compte seul écrit au journal (aucune autre colonne, aucune valeur de sonde) ; il doit tenir sous **≈ 7 378** (borne S-13 : "
     "total des sorties ≤ 2·10⁹ octets aux nombres du § 5 bis) | mère, avant la création | arrêt : aucune création (nœud ; la borne "
     "arrêterait l'instance en code 2 après les paquets et les essais, § 5 bis) |\n"),
    ("O8-13", "ligne (A) : script v4",
     "SCRIPT=scripts/etape_a_t07_variante_b_v3.sh; SHA_SCRIPT=a19c594d268baadebea93c8ef0ea6c9406044971a928defd8c119b238d5f6560;",
     f"SCRIPT=scripts/etape_a_t07_variante_b_v4.sh; SHA_SCRIPT={SHA_SCRIPT_V4};"),
    ("O8-14", "§ 5 : titre",
     "## 5. Ce que joue l'instance (`scripts/etape_a_t07_variante_b_v3.sh` : le v2, `e68d3306…`, et les changements du § 13, S-12)",
     "## 5. Ce que joue l'instance (`scripts/etape_a_t07_variante_b_v4.sh` : le v3, lui-même le v2, `e68d3306…`, et les changements "
     "du § 13, S-12 ; plus l'étape 8 du brouillon 8)"),
    ("O8-15", "§ 5, étape 8 : contrôle avant l'ouverture (v4)", "rien d'ouvert ; rapport v2, § 5, point 4) ;",
     "rien d'ouvert ; rapport v2, § 5, point 4) ; **brouillon 8** (script v4, CLC-P3-02 ; rapport v3, § 2) : ce contrôle isolé\n"
     "   est remplacé par"
     " **`lecture_v4 controle-avant-ouverture . CFG`** (`HF_HUB_OFFLINE=1`, lecture seule), qui le comprend, dans les deux\n"
     "   modes, **avant**"
     " l'empreinte de la configuration, `CODE-T07`, la branche, le repli et sa garde d'ouverture journalisée : contrôles de\n"
     "   configuration de la v4, sceaux des quatre entrées de P3, principales, témoin et directions de P3 au fichier léger, révision\n"
     "   du modèle de P3 au cache (mode réel ; index lu sous garde, morceaux annoncés tous présents, tailles non nulles : CLC-P3-03) ;\n"
     "   faute → code 2, motif au journal (« ARRET : contrôle avant l'ouverture (réextraction de P3) : … : rien n'est ouvert »),\n"
     "   rien d'ouvert ni de poussé ; passé : une ligne au journal ;"),
    ("O8-16", "§ 5, étape 13 : arrêt technique (CLC-P3-04)", "sans aire ni score (note 10)",
     "sans aire ni score (note 10) ; **brouillon 8** (CLC-P3-04) : la première ligne de\n"
     "    `etape-a.txt`, écrite au journal par le script (chemin des scores, sondes lues, état des bras ; aucun score), est rapportée\n"
     "    par la fille (§ 8) ; un bras arrêté (« échec ») dont le **motif ne commence pas par `GardeArret`**\n"
     "    (`diag/<run-t07>/reextraction-p3-t07.json`, `par_sonde`, champs `etat` et `motif` ; motif d'un bras seul : `<type> : …` ;\n"
     "    arrêt des deux bras : `réextraction impossible : <type> : …`, qui ne commence donc jamais par `GardeArret`) est un **arrêt\n"
     "    technique** (texte de T0.7, liste d'arrêt) : la mère lit ces deux seuls champs après l'étape A (aucun score, aucune aire,\n"
     "    aucun écart), écrit la réserve et revient à Lazar (nœud, R4) avant toute étape B"),
    ("O8-17", "§ 5 bis : P14", "la borne arrête avant toute ouverture, code 2).\n",
     "la borne arrête avant toute ouverture, code 2).\n\n"
     "**Brouillon 8** (CLC-P3-07) : la marge de la borne correspond à environ **7 378 actions notées** au plus ; la mère compte `n`\n"
     "sur processeur avant la création (P14) et ne crée pas au-delà.\n"),
    ("O8-18", "§ 7 : arrêts neufs",
     "- Plafond (§ 6), minuterie, refus d'un contrôle ou d'un classifieur : arrêt, compte rendu ; aucun contournement.",
     "- **Brouillon 8** : contrôle avant l'ouverture en échec à l'étape 8 (code 2) : rien n'est ouvert ni poussé ; la fille détruit\n"
     "  (§ 4.7), compte rendu ; création neuve sur un écrit de la mère quand la cause est levée. **Arrêt technique d'un bras**\n"
     "  (CLC-P3-04 ; § 5, étape 13) : l'étape A va au bout ; la mère écrit la réserve et revient à Lazar (nœud, R4) avant toute\n"
     "  étape B. P14 non tenu (plus d'environ 7 378 actions notées) : aucune création, nœud.\n"
     "- Plafond (§ 6), minuterie, refus d'un contrôle ou d'un classifieur : arrêt, compte rendu ; aucun contournement."),
    ("O8-19", "§ 8 : compte rendu", "étape A : code et run, **morceaux poussés**",
     "étape A : code et run, **état des bras de la réextraction** (« établi » ou « échec », ligne du journal ; brouillon 8),\n"
     "**contrôle avant l'ouverture de l'étape 8** (passé ou motif ; brouillon 8),\n"
     "**morceaux poussés**"),
    ("O8-20", "§ 11 : répétition v4", "marqueur `SHA_SCRIPT_V3_T07` rempli (ligne (A)).",
     "marqueur `SHA_SCRIPT_V3_T07` rempli (ligne (A)). **Brouillon 8** : répétition jouet **v4** "
     "(`scripts/repetition_jouet_variante_b_t07_v4.py`, `8b0e9590befafef97d96450def60138e6c835df90ee5ecf7e00a608f373737ba`, commit "
     "`be3191c9` ; passage du 2026-11-11 de 04:41:45 à 04:44:39 UTC ; " + REPET4 + ") : **10 verdicts sur 10** — passage normal "
     "(processeur Intel : contrôle de l'étape 8 avant l'empreinte, `CODE-T07`, le repli, la passe à blanc et l'étape A ; "
     "`CUBLAS_WORKSPACE_CONFIG` lu dans le processus), passage EPYC (`CPU_ESSAI` ; tableau `ENV_CPU` vide sous `set -u`), artefact "
     "« témoin retiré » (code 2 à l'étape 8 : ni empreinte, ni `CODE-T07`, ni branche, ni repli, ni ouverture), branche déjà "
     "poussée (code 2 après le contrôle, sans repli), découpage, `CPU_ESSAI` refusée hors essai ; la ligne (A) porte le v4."),
    ("O8-21", "§ 12 : SHA_SCRIPT (v4)", "(commit `7e23a554`) |\n",
     f"(commit `7e23a554`) ; **brouillon 8** : script v4, **`{SHA_SCRIPT_V4}`** (commit `a621dcd3`), à la ligne (A) |\n"),
    ("O8-22", "§ 12 : COMMIT_SRC_CONTRE_LU_T07 (commit final, contre-lecture rendue)",
     "non fusionnée ; contre-lecture courte des corrections en cours) : `src/` de C7 égal à son arbre `src/` ; au brouillon 6",
     f"non fusionnée ; **brouillon 8** : commit final `{COMMIT}`, contre-lecture courte des corrections rendue, R-2311 ; la mère "
     "écrit l'égalité des arbres `src/`, P13 (iii)) : `src/` de C7 égal à son arbre `src/` ; au brouillon 6"),
    ("O8-23", "§ 13 : réserves neuves (S-14 à S-17)", "| rien ; la borne reste de 2·10⁹ octets |\n",
     "| rien ; la borne reste de 2·10⁹ octets |\n"
     "| **S-14** | réserve (brouillon 8, R-2313) | **bash antérieur à 4.4 non éprouvé** : la construction de bash 4.3 a été refusée par "
     "un classifieur de permissions (rapporté, non contourné, R-2313) ; les formes `${t[@]+\"${t[@]}\"}` du v4 (CLC-P3-05) reposent sur "
     "leur définition documentée ; le mutant s5 (forme du v3) survit sous bash 5.2, équivalent | aucune (réserve écrite, "
     "R-2313) | l'image de l'instance a un bash 5 : sans effet attendu |\n"
     "| **S-15** | réserve (R-2313) | branche « autre révision » de l'étape 8 (préchargement de la révision de P3 quand elle n'est pas "
     "celle de 7b) non éprouvable hors ligne | — | P13 (i) la rend inattendue |\n"
     "| **S-16** | réserve (R-2313) | un morceau de poids **tronqué non vide** passe le contrôle du cache (l'index ne porte pas de "
     "tailles) ; le chargement échouerait après l'ouverture : les deux bras arrêtés, motif écrit, aucune bascule | lire les en-têtes "
     "des fichiers de poids (non fait) | § 5, étape 13 (arrêt technique : nœud) |\n"
     "| **S-17** | réserve (R-2313) | la suite `tests/test_t07_*` entière n'a pas été rejouée au commit final (arrêtée à 29 % faute de "
     "disque, sans échec ; `tests/test_t07_plancher_v3_*` : 92 passés) | la mère la rejoue entière à C7 (§ 11 bis) ; sa dernière ligne "
     "est `ATT` | P12 |\n"),
    ("O8-24", "§ 13 : phrase finale (v4)", "S-2, S-5, S-6, S-7 inchangés.",
     "S-2, S-5, S-6, S-7 inchangés. **Brouillon 8** : le script de cet ordre est le **v4** (`4b17d1f0…`, commit `a621dcd3`) :\n"
     "S-12 et S-13 y restent réglés ; CLC-P3-02 (contrôle entier à l'étape 8) et CLC-P3-05 (formes sûres sous `set -u`) y sont réglés ;\n"
     "S-14 à S-17 sont des réserves."),
    ("O8-25", "§ 11 bis : suite entière rejouée à C7", "- **Brouillon 7** (R-2306) : `ATT` se **mesure à C7**,",
     "- **Brouillon 8** (R-2313) : la suite `tests/test_t07_*` **entière** est rejouée par la mère à C7 (au commit final `a621dcd3`,\n"
     "  elle a été arrêtée à 29 % faute de disque, sans échec ; `tests/test_t07_plancher_v3_*` y passent, 92 sur 92) ; sa dernière\n"
     "  ligne, durée retirée, est la valeur du marqueur `ATT_C7_T07` (P12, couple VC3-C).\n"
     "- **Brouillon 7** (R-2306) : `ATT` se **mesure à C7**,"),
]

EXIGEES = (
    "## 0 quinquies. Ce qui change depuis le brouillon 7", f"SHA_SCRIPT={SHA_SCRIPT_V4};", "**10 verdicts sur 10**",
    "**`lecture_v4 controle-avant-ouverture . CFG`**", "**Arrêt technique d'un bras**", "technique** (texte de T0.7, liste d'arrêt)", "| P14 |", "≈ 7 378", "**S-14**", "**S-17**",
    "ATT='<<ATT_C7_T07>>';", "`prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json`", "**3,2 à 4,7**", "**`ANT0` ≤ 3,6 USD**",
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
                echec(f"§ 4.3 : choix de l'offre {r.stdout.strip()!r} (attendu {attendu!r})")
    print("§ 4.3 : choix de l'offre essayé sur trois cas factices : conforme")


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        echec("usage : appliquer RACINE")
    racine = Path(argv[0]).resolve()
    for chemin, attendu in ((CHEMIN_B7, SHA_B7), (VC, SHA_VC), (RAP3, SHA_RAP3), (CLC, SHA_CLC), (CL1, SHA_CL1),
                            (REP_J, SHA_REP_J), (REP_R, SHA_REP_R)):
        e = sha((racine / chemin).read_bytes())
        if e != attendu:
            echec(f"{chemin} : empreinte {e[:16]}… ≠ {attendu[:16]}…")
    resume = json.loads((racine / REP_R).read_text(encoding="utf-8"))
    verdicts = resume.get("verdicts", {})
    if resume.get("conforme") is not True or len(verdicts) != 10 or not all(v is True for v in verdicts.values()):
        echec(f"répétition v4 : conforme {resume.get('conforme')!r}, {len(verdicts)} verdicts")
    print(f"entrées vérifiées ; répétition v4 : conforme, {len(verdicts)} verdicts sur 10 vrais")
    vc = (racine / VC).read_text(encoding="utf-8")
    s4 = vc[vc.index("## 4. Couples proposés"):vc.index("## 5.")]
    vcs = {c["id"]: c for c in json.loads(re.search(r"```json\n(.*?)\n```", s4, re.S).group(1))}
    couples = []
    for ident, ou, ancien, nouveau in COUPLES:
        if ancien.startswith("@@VC3-"):
            c = vcs[ancien.strip("@")]
            if c["cible"] != "ordre, brouillon 7" or c["gelee"] is not None:
                echec(f"{c['id']} : cible {c['cible']!r}, gelée {c['gelee']!r}")
            ancien, nouveau = c["ancien"], c["nouveau"]
            print(f"{ident} = {c['id']} de la vérification courte, tel qu'écrit")
        couples.append((ident, ou, ancien, nouveau))
    texte7 = (racine / CHEMIN_B7).read_bytes().decode("utf-8")
    texte = texte7
    ids = [c[0] for c in couples]
    if ids != [f"O8-{k:02d}" for k in range(1, len(ids) + 1)]:
        echec("identifiants de couples")
    for ident, ou, ancien, nouveau in couples:
        texte = remplacer(texte, f"{ident} ({ou})", ancien, nouveau)
    print(f"{len(couples)} couples appliqués, chacun à une occurrence")
    for ident in ("VC3-C", "VC3-D"):
        if vcs[ident]["nouveau"] not in texte:
            echec(f"{ident} : « nouveau » absent du texte")
    defait = texte
    for ident, ou, ancien, nouveau in reversed(couples):
        n = defait.count(nouveau)
        if n != 1:
            echec(f"défaisage de {ident} : « nouveau » présent {n} fois (une attendue)")
        defait = defait.replace(nouveau, ancien)
    if defait != texte7:
        echec("les couples défaits ne redonnent pas le brouillon 7 octet pour octet")
    print(f"tout le reste égal à l'octet : couples défaits dans l'ordre inverse → brouillon 7 retrouvé "
          f"({texte7.count(chr(10))} → {texte.count(chr(10))} lignes)")
    if texte.split("\n", 1)[0] != TITRE_B8:
        echec("titre du brouillon 8")
    for m in MARQUEURS:
        if texte.count(m) != 1:
            echec(f"marqueur {m} : {texte.count(m)} occurrences (une attendue)")
    autres = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", texte)) - set(MARQUEURS))
    if autres:
        echec(f"marqueurs inattendus : {autres}")
    print(f"marqueurs : {len(MARQUEURS)}, une occurrence chacun, aucun autre")
    for p in EXIGEES:
        if p not in texte:
            echec(f"phrase exigée absente : {p!r}")
    if "SHA_SCRIPT=a19c594d" in texte:
        echec("empreinte du v3 encore à la ligne (A)")
    print(f"phrases exigées : {len(EXIGEES)} présentes ; ligne (A) au v4")
    s6 = texte[texte.index("## 6. Devis"):texte.index("## 7. Arrêts")]
    if s6 != texte7[texte7.index("## 6. Devis"):texte7.index("## 7. Arrêts")]:
        echec("§ 6 changé")
    print("§ 6 (devis, plafond, marge) égal à celui du brouillon 7")
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
    sortie = racine / CHEMIN_B8
    octets = texte.encode("utf-8")
    if sortie.exists() and sortie.read_bytes() != octets:
        echec(f"{CHEMIN_B8} existe avec un autre contenu (R12)")
    if not sortie.exists():
        sortie.write_bytes(octets)
    print(f"écrit : {CHEMIN_B8} ({sha(octets)})")
    print("TOUT PASSE")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
