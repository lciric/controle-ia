"""Ordre d'exécution de l'étape A de T0.7, variante B, brouillon 6 : application au brouillon 5 des couples du remède (a')
(R-2285, R-2298, R-2304), puis vérifications, dont « tout le reste égal à l'octet » (v1).

Rédacteur neuf du candidat 2 de T0.7 et de ce brouillon 6 (sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`,
Claude Opus 5.5), 11 novembre 2026 ; consigne
`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-redaction-t07-candidat2-v1.md` (`d29c7858…`),
« Mandat — ordre d'exécution brouillon 6 ». Bibliothèque standard et `bash -n` seulement ; aucun réseau, aucune clé, aucun `git`,
aucun `vastai`.

    cd <dossier hors du dépôt> && <python du dépôt> -I -B <chemin absolu de ce script> RACINE

1. vérifie l'empreinte du brouillon 5 (`d0b75d16…`) et celle de la configuration v7 (`3701407c…`) ; contrôle que la v7 cite les
   six chemins de la v4 (P12 inchangé) ;
2. applique les couples `COUPLES` dans l'ordre : chaque « ancien » présent exactement une fois au moment de son application et
   différent de son « nouveau » ; sinon arrêt (code 1), rien n'est écrit ;
3. **tout le reste égal à l'octet** : défait les couples dans l'ordre inverse (chaque « nouveau » présent exactement une fois au
   moment où il est défait) et exige de retrouver le brouillon 5 octet pour octet ; imprime le nombre de lignes changées ;
4. vérifie : titre ; les dix marqueurs du brouillon 5 et les deux neufs (`SHA_SCRIPT_V3_T07`, `COMMIT_SRC_CONTRE_LU_T07`), une
   occurrence chacun, aucun autre `<<…>>` ; plus aucun appel `lecture_v2` hors des mentions « au brouillon 5 » ; blocs `bash`
   (`bash -n`, marqueurs remplacés par des valeurs factices) ; extraits `python3 -I -c '…'` (`ast.parse`) ; essai du choix de
   l'offre (§ 4.3) sur des offres factices (un hôte EPYC passe avant un hôte moins cher qui ne l'est pas ; sans EPYC, la moins
   chère) ; devis : sommes de la table du § 6 et borne de la minuterie recalculées ; phrases exigées présentes ;
5. écrit `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon6.md` (R12 : refuse d'écraser un fichier différent ; un fichier
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

SHA_B5 = "d0b75d161e80efbd4b1e5e6ca8f2cc49476bf90801cae57617b2cc553a92108b"
CHEMIN_B5 = "docs/procedures/ordre-execution-etape-a-t07-v1-brouillon5.md"
CHEMIN_B6 = "docs/procedures/ordre-execution-etape-a-t07-v1-brouillon6.md"
CHEMIN_V7 = "docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/configuration-t07-v7.json"
SHA_V7 = "3701407cf96f2851de26b04df174432a6e5325227c1e1f5a24900a1fa44ef6ab"
SIX_CHEMINS = ["diag/20261019-230011-p3-reel/sondes-figees.json", "donnees/20261007-082440-t05-extraction/taches-entrainement.json",
               "donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz", "donnees/T0.7-faits-repe-v1/facts_true_false.csv",
               "donnees/T0.7-models-under-pressure-v1/training/train.jsonl", "runs/20261019-230011-p3-reel/manifeste.json"]
TITRE_B6 = "# Ordre d'exécution — étape A de T0.7, variante B (instance A100 neuve, activations recalculées) — v1, brouillon 6"
MARQUEURS = ["<<ID_SESSION_FILLE>>", "<<EMPREINTE_CONFIG_T07>>", "<<LIGNE_SCELLEMENT_T07>>", "<<DEPENSE_ANTERIEURE_USD>>",
             "<<RUN_T06_7B>>", "<<BRANCHE_7B>>", "<<COMMIT_CODE_T07>>", "<<COMMIT_SCELLEMENT_T07>>", "<<CHEMIN_CONFIG_T07>>",
             "<<PERIMETRE_T07>>", "<<SHA_SCRIPT_V3_T07>>", "<<COMMIT_SRC_CONTRE_LU_T07>>"]
FACTICES = {"<<DEPENSE_ANTERIEURE_USD>>": "0", "<<RUN_T06_7B>>": "20261112-000000-t06-reel",
            "<<BRANCHE_7B>>": "calcul/t06-confirmation-7b-v1", "<<COMMIT_CODE_T07>>": "0" * 40,
            "<<COMMIT_SCELLEMENT_T07>>": "1" * 40, "<<CHEMIN_CONFIG_T07>>": "prereg/T0.7-sondes-v0-v1-configuration-t07-v7.json",
            "<<PERIMETRE_T07>>": "JD,JA", "<<SHA_SCRIPT_V3_T07>>": "2" * 64, "<<COMMIT_SRC_CONTRE_LU_T07>>": "3" * 40}
REV_P3 = "0e9e39f249a16976918f6564b8830bc894c89659"
RAPPORT_CODE = ("rapport du code du plancher v3, `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/"
                "rapport-code-plancher-v3-v1.md` (`cb31edc844c6bc4ee285219a819d2943fd140bf9d70f56d1da2e9e031520db92`)")
CONSIGNE = ("`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-redaction-t07-candidat2-v1.md` "
            "(`d29c78585ee578127304d840851fa7017c6e756324f47caa9c401a84ee553eae`, vérifiée par `sha256sum -c` avant lecture)")

# ------------------------------------------------------------------------------------------------------------- couples
# (id, où, ancien, nouveau) ; « ancien » copié du brouillon 5 (ou du texte courant), présent une fois au moment de l'application.
COUPLES = [
    ("O6-01", "titre",
     "activations recalculées) — v1, brouillon 5\n",
     "activations recalculées) — v1, brouillon 6\n"),
    ("O6-02", "encadré : script de l'instance",
     "> Script de l'instance : **`scripts/etape_a_t07_variante_b_v2.sh`** (`e68d3306…`), neuf arguments.",
     "> Script de l'instance : **`scripts/etape_a_t07_variante_b_v3.sh`**, neuf arguments (**brouillon 6** : un script v3 est\n"
     "> **exigé** — le v2, `e68d3306…`, appelle `lecture_v2`, qui refuse la configuration v7 ; empreinte du v3 au marqueur de la\n"
     "> ligne (A) ; § 0 ter, § 13, S-12). **Brouillon 6 (remède (a'), R-2285, R-2298, R-2304)** : commandes `lecture_v4`,\n"
     "> configuration v7 (800 directions, règle (a)), plancher neuf des sondes figées de P3 réextrait au début de l'étape A,\n"
     "> devis relevé (+ 0,23 h attendu, + 0,66 h au pire), `ANT0` ≤ 3,6 USD."),
    ("O6-03", "statut du brouillon 6",
     "- **Statut** : **brouillon 5**, écrit le 2026-11-10 à partir de 16:12 UTC (`date -u`) par le rédacteur du brouillon 4, qui",
     "- **Statut** : **brouillon 6**, écrit le 2026-11-11 à partir de 03:00 UTC (`date -u`) par un **rédacteur neuf** (Claude Opus\n"
     "  5.5, `claude-opus-5-5`, sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`), qui n'a écrit ni T0.7 (brouillons,\n"
     "  candidat 1), ni son module, ni les brouillons 1 à 5 de cet ordre, ni leurs contre-lectures, ni les notes de l'erreur de\n"
     "  première espèce ; il écrit aussi le candidat 2 de T0.7 (ayant lu T0.7, il est exclu ensuite de tout rôle de lecteur de\n"
     "  P3-bis). Consigne : " + CONSIGNE + ". **Brouillon 6 = brouillon 5**\n"
     "  (`d0b75d161e80efbd4b1e5e6ca8f2cc49476bf90801cae57617b2cc553a92108b`, gardé tel quel, R12) **+ les couples O6-01 à O6-37**\n"
     "  du script `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon6-appliquer-v1.py`, chacun avec un « ancien » présent une\n"
     "  fois ; **tout le reste est égal à l'octet au brouillon 5** (vérifié par le script : les couples défaits dans l'ordre inverse\n"
     "  redonnent le brouillon 5 octet pour octet). Ce qui change et pourquoi : § 0 ter. **Non contre-lu** : à contre-lire (R2)\n"
     "  avant son scellement ; le script v3 de l'instance (§ 13, S-12) reste à écrire, répéter en jouet et contre-lire.\n"
     "- **Brouillon 5** (statut gardé pour mémoire) : **brouillon 5**, écrit le 2026-11-10 à partir de 16:12 UTC (`date -u`) par le\n"
     "  rédacteur du brouillon 4, qui"),
    ("O6-04", "section neuve « 0 ter »",
     "## 1. Cadre\n",
     "## 0 ter. Ce qui change depuis le brouillon 5 (brouillon 6 : remède (a'))\n\n"
     "Sources : mot de Lazar R-2285 (« (a') le remède, plus davantage de directions dans le plancher : un seuil du texte à changer :\n"
     "go ») ; R-2298 (`n_plancher` = 800, notation par lots, réextraction des sondes figées de P3) ; R-2304 (code rendu, commit\n"
     "`0d0c5da4061c28d808c3aa3b53c9a9a5e56a3a07`, configuration v7, `garde_principale` = « rapportee », repli) ; " + RAPPORT_CODE + ",\n"
     "§ 8 (devis) et § 9, point 5 (ce que l'ordre doit dire).\n\n"
     "| Point | Où | Brouillon 5 | Brouillon 6 | Source |\n"
     "|---|---|---|---|---|\n"
     "| Commandes du module | § 5, étapes 8, 11, 12, 13 ; § 9 | `lecture_v2` (`empreinte-config`, `repli-seul`, `passe-blanc`, "
     "`etape-a-apres-repli`) | **`lecture_v4`** (mêmes sous-commandes ; `repli-recalcul` **refusé** par la v4, code 2, jamais appelé) ; "
     "étape B par `lecture_v4 etape-b` seule | R-2304 ; rapport, § 2 et § 9.5 |\n"
     "| Script de l'instance | encadré, § 1, ligne (A), P9, P13, § 5, § 11, § 13 | v2, `e68d3306…`, celui de l'ordre | **v3 exigé** "
     "(`scripts/etape_a_t07_variante_b_v3.sh`, empreinte au marqueur `SHA_SCRIPT_V3_T07`) : le v2 appelle `lecture_v2` (l. 302, 357, 367, "
     "372), qui refuse la v7 (« n_plancher 800 ≠ 200 ») ; changements exigés au § 13, S-12 ; **écart déclaré** : la consigne ne nomme pas "
     "le script ; sans lui, les commandes `lecture_v4` ne seraient pas jouées | constat de ce rédacteur (script lu, configuration v7 "
     "rejouée) |\n"
     "| `CUBLAS_WORKSPACE_CONFIG` | § 5, étape 13 ; S-12 | posé par le module (`setdefault`) | **`:4096:8` exporté pour le processus de "
     "l'étape A** (le module le pose aussi avant tout calcul sur la carte) | rapport, § 9.5 |\n"
     "| Processeur hôte | § 1 (machine), § 4.3, § 5 (étape 13) | — | **préférence d'hôte EPYC** (processeur de P3) ; à défaut, "
     "`ATEN_CPU_CAPABILITY=avx2` et `MKL_CBWR=AVX2` pour l'étape A, **non éprouvé, déclaré** | rapport, § 5 et § 9.5 |\n"
     "| Modèle de P3 | P13 ; § 4.1 ; § 5, étape 8 | — | révision de P3 (`0e9e39f2…`) au cache local (la réextraction ne télécharge "
     "jamais) : révision de 7b relevée ; le v3 précharge celle de P3 si elle diffère | rapport, § 9.5 |\n"
     "| Dépense antérieure (P8) | P8 ; § 6 | `ANT0` ≤ 4,5 USD (pire cas 15,5 USD) | **`ANT0` ≤ 3,6 USD** (pire cas 16,4 USD) | rapport, § 8 ; "
     "R-2304 |\n"
     "| Devis, minuterie, marge | § 6 ; § 4.4 ; § 7 | 3,0 à 4,5 h ; 7,9 à 10,9 h ; 5,2 à 7,1 USD ; 11,6 à 15,5 USD ; borne 39 240 s ; "
     "marge 1,1 h | **3,2 à 4,7 h ; 8,6 à 11,6 h ; ≈ 5,5 à 7,4 USD ; ≈ 12,5 à 16,4 USD ; borne 41 616 s (11,56 h) ; marge ≈ 0,45 h** "
     "(réserve CLE-12 aggravée) ; sous 20 USD | rapport, § 8 ; R-2304 |\n"
     "| Configuration | § 1 ; marqueur `EMPREINTE_CONFIG_T07` | base v4 (`3d19b08c…`) | **v7**, chemin final "
     "`prereg/T0.7-sondes-v0-v1-configuration-t07-v7.json` (fichier `3701407c…`, canonique attendue `4ff92c8e…`) ; mêmes six chemins | "
     "R-2304 |\n"
     "| Code (C7, `CODE-T07`) | § 1 ; P6 ; P9 ; P13 ; ligne (A) ; § 4.1 ; § 5, étape 9 | `src/` de C7 égal à `37485ce5` ; dix-huit modules "
     "| `src/` de C7 égal à celui de `SRC7` (marqueur `COMMIT_SRC_CONTRE_LU_T07` : dernier commit contre-lu du code du remède (a'), "
     "fusionné dans `main`, fixé par la mère) ; **vingt-six modules** de `src/controle_ia/t07/` (huit neufs) dans `CODE-T07-v2.json` | "
     "R-2304 ; consigne (C7 et `CODE-T07` laissés à la mère) |\n"
     "| Sorties de l'étape A non lues par la fille | § 2.5 | — | plus `planchers-figees-t07.npz` et `reextraction-p3-t07.json` | rapport, § 2 |\n"
     "| Ligne d'essais `ATT`, P12 | ligne (A), P12, § 11 bis | `346 passed, 2 skipped, 4 xfailed` (arbres `79230a58…`, `744a9e16…`) | "
     "**texte inchangé** ; le code neuf change les arbres de S7 (cinq fichiers d'essais neufs) : « ATT valable pour S7 » sera absent et "
     "la mère **remesure** `ATT` par le § 11 bis avant la création (chemin prévu par P12) ; durée : 61 essais neufs, 63 à 76 s chez le développeur (rapport, § 6), dans la marge de la ligne « Essais » du § 6 (non ajoutée, déclaré) | constat de ce rédacteur |\n"
     "| Taille des sorties (§ 5 bis) | § 5 bis ; § 13, S-13 | ordre de grandeur à `P` = 200 | **texte inchangé** ; à `P` = 800 la formule "
     "lit `n_plancher` de la v7 ; elle ne compte ni `planchers-figees-t07.npz` (≈ 5,2·10⁷ octets) ni les 2 × 200 directions de P3 notées "
     "en descriptif : S-13 | constat de ce rédacteur |\n\n"
     "Tout le reste est égal à l'octet au brouillon 5 (vérifié par programme, statut).\n\n"
     "## 1. Cadre\n"),
    ("O6-05", "§ 1 : code de T0.7",
     "| Code de T0.7 | **C7** : commit de `main` dont `src/` égale celui de `37485ce50601b7d7ff9035bc34c734ec689ca731` (arbre `744a9e16…`) "
     "et dont `tests/` égale celui de S7, fixé après la fusion des essais CLC-04 et GARDES-CODE-01 (R-2231, R-2241 Q-5 et Q-6, R-2249) ;",
     "| Code de T0.7 | **C7** : commit de `main` dont `src/` égale celui de `SRC7` (ligne (A) ; **brouillon 6** : dernier commit "
     "contre-lu du code du remède (a'), vingt-six modules de `src/controle_ia/t07/`, `lecture_v4` compris, fusionné dans `main`, fixé "
     "par la mère, R-2304 ; au brouillon 5 : `37485ce50601b7d7ff9035bc34c734ec689ca731`, arbre `744a9e16…`, dix-huit modules) et dont "
     "`tests/` égale celui de S7, fixé après la fusion du code neuf et de ses essais (brouillon 6 ; au brouillon 5 : des essais CLC-04 "
     "et GARDES-CODE-01, R-2231, R-2241 Q-5 et Q-6, R-2249) ;"),
    ("O6-06", "§ 1 : script de l'instance",
     "| Script de l'instance | `scripts/etape_a_t07_variante_b_v2.sh`, sha256 `e68d3306bd76a549ec97eb6b153d03ec544c92944ae74293d8c0db8cfda62269` "
     "(commit `04bc14a2`, sur `main`) ; répété en jouet (rapport complémentaire 5, § 5, passage 4 ; rejoué par la contre-lecture "
     "`7a327462…`, § 2) |",
     "| Script de l'instance | **brouillon 6** : `scripts/etape_a_t07_variante_b_v3.sh`, sha256 au marqueur de la ligne (A) "
     "(`SHA_SCRIPT`) ; **à écrire** : le v2 plus les changements du § 13, S-12 (commandes `lecture_v4`, `CUBLAS_WORKSPACE_CONFIG`, "
     "révision de P3, variables du processeur hôte), répété en jouet et contre-lu avant que la mère remplisse le marqueur (décision de "
     "la mère) ; **au brouillon 5** : `scripts/etape_a_t07_variante_b_v2.sh`, sha256 `e68d3306…` (commit `04bc14a2`, sur `main`) ; "
     "répété en jouet (rapport complémentaire 5, § 5, passage 4 ; rejoué par la contre-lecture `7a327462…`, § 2) ; il appelle "
     "`lecture_v2` (l. 302, 357, 367, 372), qui refuse la configuration v7 |"),
    ("O6-07", "§ 1 : configuration",
     "| Configuration | `CFG` (ligne (A)), copiée sous `prereg/` et scellée dans S7 (base : "
     "`brouillons/T0.7-sondes-v0-v1-brouillon19-pieces/configuration-t07-v4.json`, `3d19b08c…`, `code_t07_exige` vrai) ; empreinte "
     "canonique `<<EMPREINTE_CONFIG_T07>>`, revérifiée sur l'instance ; **chemins qu'elle cite** (lus par le script, étape 2) : les six "
     "de la v4 (§ 11 bis), contrôlés par la fille (P12) |",
     "| Configuration | `CFG` (ligne (A)), copiée sous `prereg/` et scellée dans S7 ; **brouillon 6** : **configuration v7**, chemin "
     "final **`prereg/T0.7-sondes-v0-v1-configuration-t07-v7.json`** (copie octet pour octet, faite par la mère au scellement de "
     "T0.7, de `" + CHEMIN_V7 + "`, sha256 du fichier `3701407cf96f…`, avec son compagnon) : la v5 du candidat 1 plus `methode_plancher` "
     "« difference_appariee_percentile », `n_plancher` 800 et la clé `plancher_figees` (`reextraction_p3_v1`, `n_p3` 200, tolérances "
     "10⁻⁶, 10⁻², 10⁻¹, `garde_principale` « rapportee »), rien d'autre (R-2304) ; seule `lecture_v4` l'accepte (`lecture_v2` et "
     "`lecture_v3` la refusent) ; au brouillon 5 : base `brouillons/T0.7-sondes-v0-v1-brouillon19-pieces/configuration-t07-v4.json`, "
     "`3d19b08c…`, `code_t07_exige` vrai ; empreinte canonique `<<EMPREINTE_CONFIG_T07>>` (attendue pour la v7 : `4ff92c8e…`, "
     "`lecture_v4 empreinte-config`), revérifiée sur l'instance ; **chemins qu'elle cite** (lus par le script, étape 2) : les six de la "
     "v4, **inchangés dans la v7** (vérifié par programme ; § 11 bis), contrôlés par la fille (P12) |"),
    ("O6-08", "§ 1 : machine (préférence EPYC)",
     "≥ 16 cœurs, ≥ 128 Go de mémoire vive ; **disque 100 Go**",
     "≥ 16 cœurs, ≥ 128 Go de mémoire vive ; **brouillon 6** : **préférence d'hôte EPYC** (processeur de P3 et de sa régénération "
     "R-679, AMD EPYC 7513 : vise le palier « identique » de la sonde linéaire refaite par la réextraction ; § 4.3) ; à défaut, "
     "`ATEN_CPU_CAPABILITY=avx2` et `MKL_CBWR=AVX2` pour le processus de l'étape A (**non éprouvé, déclaré** ; § 5, étape 13) ; "
     "**disque 100 Go**"),
    ("O6-09", "P6 : CODE-T07 à vingt-six modules",
     "citant **`registres/code-t07/CODE-T07-v2.json`** (écrit par",
     "citant **`registres/code-t07/CODE-T07-v2.json`** (**brouillon 6** : vingt-six modules de `src/controle_ia/t07/` au commit C7, "
     "huit neufs ; non encore écrit ; écrit par"),
    ("O6-10", "P8 : dépense antérieure",
     "(§ 6 : 15,5 USD), soit `ANT0` ≤ 4,5 USD",
     "(§ 6 : **16,4 USD**, brouillon 6 ; 15,5 USD au brouillon 5), soit **`ANT0` ≤ 3,6 USD** (4,5 USD au brouillon 5)"),
    ("O6-11", "P9 : src de C7",
     "| P9 | **Code** (R-2231) : C7 ancêtre de S7 ; `src/` de C7 égal à `37485ce5` ;",
     "| P9 | **Code** (R-2231) : C7 ancêtre de S7 ; `src/` de C7 égal à celui de `SRC7` (brouillon 6 ; `37485ce5` au brouillon 5) ;"),
    ("O6-12", "P13 neuf",
     "| § 4.1 | remesure (mère), puis seulement création |\n",
     "| § 4.1 | remesure (mère), puis seulement création |\n"
     "| P13 | **Brouillon 6 (remède (a'))** : (i) **révision du modèle** du manifeste de `RUN6` (`config.agent.revision`, lue sur `BR7B`, "
     "rien d'autre affiché) comparée à celle de P3, `" + REV_P3 + "` (la réextraction lit le modèle de P3 au cache local et ne "
     "télécharge jamais : modèle absent → bras arrêté) ; (ii) **script v3** présent sur `main` à l'empreinte `SHA_SCRIPT`, répété en "
     "jouet et contre-lu (§ 13, S-12) ; (iii) **`SRC7`** fixé par la mère | § 4.1 | (i) égale : rien ; autre : écrit au journal, le v3 "
     "précharge la révision de P3 (§ 5, étape 8) ; (ii), (iii) absents : rien |\n"),
    ("O6-13", "ligne (A) : script v3, SRC7, révision de P3",
     "SCRIPT=scripts/etape_a_t07_variante_b_v2.sh; SHA_SCRIPT=e68d3306bd76a549ec97eb6b153d03ec544c92944ae74293d8c0db8cfda62269;",
     "SCRIPT=scripts/etape_a_t07_variante_b_v3.sh; SHA_SCRIPT=<<SHA_SCRIPT_V3_T07>>; SRC7=<<COMMIT_SRC_CONTRE_LU_T07>>; "
     "REV_P3=" + REV_P3 + ";"),
    ("O6-14", "§ 2.5 : sorties neuves de l'étape A",
     "`notation-t07.json`, `sondes-neuves-t07.npz`, ses morceaux,",
     "`notation-t07.json`, `sondes-neuves-t07.npz`, ses morceaux, `planchers-figees-t07.npz`, `reextraction-p3-t07.json` (brouillon 6),"),
    ("O6-15", "§ 4.1 : révision de 7b comparée à celle de P3 (P13)",
     "LA=$(grep '^| GO-LECTURE-T07 |' \"$REG\");",
     "git -C \"$M\" show \"refs/remotes/origin/$BR7B:runs/$RUN6/manifeste.json\" | python3 -I -c 'import json,sys; r=json.load(sys.stdin)"
     "[\"config\"][\"agent\"][\"revision\"]; print(\"révision de 7b égale à celle de P3\" if r == sys.argv[1] else \"révision de 7b autre "
     "que celle de P3 (P13)\")' \"$REV_P3\"\n"
     "LA=$(grep '^| GO-LECTURE-T07 |' \"$REG\");"),
    ("O6-16", "§ 4.1 : src de C7 égal à celui de SRC7",
     "git -C \"$M\" diff --quiet 37485ce50601b7d7ff9035bc34c734ec689ca731 \"$C7\" -- src",
     "git -C \"$M\" diff --quiet \"$SRC7\" \"$C7\" -- src"),
    ("O6-17", "§ 4.1 : attendus (P13)",
     "les messages « conforme », « inchangée », « code et script conformes »,",
     "les messages « conforme », « inchangée », « code et script conformes », « révision de 7b égale à celle de P3 » (brouillon 6, P13 ;\n"
     "l'autre message est écrit au journal, sans arrêt),"),
    ("O6-18", "§ 4.3 : préférence d'hôte EPYC",
     "x=o[0] if o else None; print(\"aucune offre\" if x is None else \"id=%s carte=%s prix_h=%.4f stockage_h=%s machine=%s cuda=%s "
     "offres=%d\" % (x[\"id\"], x[\"gpu_name\"], float(x[\"dph_total\"]), x.get(\"storage_total_cost\"), x.get(\"machine_id\"), "
     "x.get(\"cuda_max_good\"), len(o)))'",
     "o=sorted(o, key=lambda y: (0 if \"EPYC\" in str(y.get(\"cpu_name\") or \"\") else 1, float(y.get(\"dph_total\",9)))); "
     "x=o[0] if o else None; print(\"aucune offre\" if x is None else \"id=%s carte=%s prix_h=%.4f stockage_h=%s machine=%s cuda=%s "
     "cpu=%s offres=%d\" % (x[\"id\"], x[\"gpu_name\"], float(x[\"dph_total\"]), x.get(\"storage_total_cost\"), x.get(\"machine_id\"), "
     "x.get(\"cuda_max_good\"), x.get(\"cpu_name\"), len(o)))'"),
    ("O6-19", "§ 4.3 : texte (préférence EPYC)",
     "Une offre n'est retenue que si son stockage est ≤ 0,08 USD de l'heure",
     "**Brouillon 6** : parmi les offres retenues, un hôte dont `cpu_name` porte « EPYC » passe d'abord (prix croissant dans chaque "
     "groupe ; champ absent : hôte non EPYC) ; `cpu` imprimé et écrit au journal ; sans offre EPYC, la moins chère est prise et le "
     "script v3 pose `ATEN_CPU_CAPABILITY=avx2` et `MKL_CBWR=AVX2` pour l'étape A (non éprouvé, déclaré ; § 5, étape 13). "
     "Une offre n'est retenue que si son stockage est ≤ 0,08 USD de l'heure"),
    ("O6-20", "§ 4.4 : borne de la minuterie (commande)",
     "[ \"$HMAX\" -ge 39240 ]",
     "[ \"$HMAX\" -ge 41616 ]"),
    ("O6-21", "§ 4.4 : borne de la minuterie (texte)",
     "(39 240 s = 10,9 h, § 6)",
     "(41 616 s = 11,56 h, § 6 ; brouillon 6 ; 39 240 s = 10,9 h au brouillon 5)"),
    ("O6-22", "§ 5 : titre",
     "## 5. Ce que joue l'instance (`scripts/etape_a_t07_variante_b_v2.sh`, `e68d3306…`)",
     "## 5. Ce que joue l'instance (`scripts/etape_a_t07_variante_b_v3.sh` : le v2, `e68d3306…`, et les changements du § 13, S-12)"),
    ("O6-23", "§ 5, étape 8 : modèle de P3 et empreinte par lecture_v4",
     "8. **Modèle** descendu au cache local (`precharger_modele`, révision figée du manifeste de 7b, `HF_TOKEN`) ; tout le reste lit\n"
     "   hors ligne ; empreinte canonique de la configuration.",
     "8. **Modèle** descendu au cache local (`precharger_modele`, révision figée du manifeste de 7b, `HF_TOKEN`) ; **brouillon 6** : si\n"
     "   elle n'est pas celle de P3 (`0e9e39f2…`, lue dans `runs/20261019-230011-p3-reel/manifeste.json`, `config.agent`), le v3\n"
     "   précharge aussi celle de P3 (échec → arrêt de code 2, rien d'ouvert ; la réextraction ne télécharge jamais) ; tout le reste\n"
     "   lit hors ligne ; empreinte canonique de la configuration par `lecture_v4 empreinte-config` (brouillon 6 ; `lecture_v2` au\n"
     "   brouillon 5, qui refuse la v7)."),
    ("O6-24", "§ 5, étape 9 : CODE-T07",
     "9. **`CODE-T07`** : `python -m controle_ia.t07.code_t07_v1 verifier",
     "9. **`CODE-T07`** (vingt-six modules au brouillon 6) : `python -m controle_ia.t07.code_t07_v1 verifier"),
    ("O6-25", "§ 5, étape 11 : repli par lecture_v4",
     "11. **Repli** (`lecture_v2 repli-seul`, DF-01)",
     "11. **Repli** (`lecture_v4 repli-seul`, brouillon 6 ; `lecture_v2` au brouillon 5 ; DF-01 ; `repli-recalcul`, refusé par la\n"
     "    v4 (code 2), n'est jamais appelé)"),
    ("O6-26", "§ 5, étape 12 : passe à blanc par lecture_v4",
     "12. **Passe à blanc** : `lecture_v2 passe-blanc`",
     "12. **Passe à blanc** : `lecture_v4 passe-blanc` (brouillon 6 : `passe_blanc_v2`, configuration v7 ; `lecture_v2` au brouillon 5)"),
    ("O6-27", "§ 5, étape 13 : étape A par lecture_v4",
     "13. **Étape A** : `lecture_v2 etape-a-apres-repli` (rapport du repli relu et couvrant ;",
     "13. **Étape A** : `lecture_v4 etape-a-apres-repli` (brouillon 6 ; `lecture_v2` au brouillon 5), lancée avec\n"
     "    **`CUBLAS_WORKSPACE_CONFIG=:4096:8` exporté pour ce processus** (le module le pose aussi par `setdefault` avant tout calcul\n"
     "    sur la carte) et, sur un hôte dont le processeur n'est pas un EPYC (`/proc/cpuinfo`, écrit au journal), avec\n"
     "    `ATEN_CPU_CAPABILITY=avx2` et `MKL_CBWR=AVX2` (**non éprouvé, déclaré**) ; **réextraction des jetons d'entraînement des deux\n"
     "    sondes figées de P3 avant toute autre extraction** (réglages de P3, modèle de P3 au cache local, gardes d'identité,\n"
     "    800 directions neuves ; `planchers-figees-t07.npz` et `reextraction-p3-t07.json` scellés et poussés avec les sorties ; un\n"
     "    bras arrêté n'arrête pas l'étape A : texte de T0.7, liste d'arrêt) ; planchers notés par lots (`plancher_v3`) (rapport du\n"
     "    repli relu et couvrant ;"),
    ("O6-28", "§ 6 : lignes neuves du devis et total",
     "| **Total** | **3,0 à 4,5** | **7,9 à 10,9** | |",
     "| **Brouillon 6** : réextraction de P3 (modèle de P3 au cache, extraction des 2 069 exemples d'entraînement à la couche 15, "
     "témoins et principale refaits, seconde garde, 800 directions par sonde figée) | 0,12 | 0,29 | rapport du code du plancher v3 "
     "(`cb31edc8…`), § 8 ; R-679 (extraction en 78,5 s) |\n"
     "| **Brouillon 6** : notation des planchers par lots (≈ 12,5 planchers de 800 directions, ≈ 1,3 million de jetons par couche) et "
     "contrôle en ligne | 0,09 | 0,32 | id., § 4 et § 8 (mesuré sur quatre cœurs, mise à l'échelle supposée linéaire) |\n"
     "| **Brouillon 6** : poussée des scores en plus (≈ 0,46 Go) | 0,02 | 0,05 | id., § 8 |\n"
     "| **Total** | **3,2 à 4,7** (3,0 à 4,5 au brouillon 5) | **8,6 à 11,6** (7,9 à 10,9 au brouillon 5 ; 11,56 h au pire exact) | "
     "+ 0,23 h attendu, + 0,66 h au pire (rapport, § 8 ; rien retiré au devis) |"),
    ("O6-29", "§ 6 : coût",
     "attendu **≈ 3,9 à 5,9 USD** ; pire cas\n  ≈ 10,3 à 14,2 USD ;",
     "attendu **≈ 4,2 à 6,1 USD** (brouillon 6 ; 3,9 à 5,9\n  au brouillon 5) ; pire cas ≈ 11,1 à 15,0 USD (10,3 à 14,2 au brouillon 5) ;"),
    ("O6-30", "§ 6 : total en USD",
     "**Attendu ≈ 5,2 à 7,1 USD ; pire cas ≈ 11,6 à 15,5 USD.**",
     "**Attendu ≈ 5,5 à 7,4 USD ; pire cas ≈ 12,5 à 16,4 USD** (brouillon 6 : devis du brouillon 5, ≈ 5,2 à 7,1 et ≈ 11,6 à "
     "15,5 USD, plus 0,30 USD attendu et 0,86 USD au pire, rapport du code, § 8, arrondis vers le haut ; calcul direct : 5,5 à 7,4 et "
     "12,4 à 16,3 USD) : **sous 20 USD**."),
    ("O6-31", "§ 6 : plafond et ANT0",
     "P8 exige qu'elle couvre le pire cas (`ANT0` ≤ 4,5 USD).",
     "P8 exige qu'elle couvre le pire cas (`ANT0` ≤ 3,6 USD au brouillon 6 ; 4,5 USD au brouillon 5)."),
    ("O6-32", "§ 6 : marge à ECH",
     "; à `ANT0` = 4,5 USD, de 0,1 USD.",
     "; à `ANT0` = 3,6 USD (borne de P8 au brouillon 6), de 0,1 USD (au brouillon 5 : à `ANT0` = 4,5 USD)."),
    ("O6-33", "§ 7 : réserve CLE-12 aggravée",
     "pire cas du devis (10,9 h, § 6) et 12 h est de **1,1 h** (moins quand `HMAX` < 12 h, § 4.4)",
     "pire cas du devis (**11,56 h**, § 6 ; brouillon 6) et 12 h est d'environ **0,45 h** (**aggravée** au brouillon 6 par la\n"
     "  réextraction et la notation des planchers à 800 directions, R-2304 ; 1,1 h au brouillon 5 ; moins quand `HMAX` < 12 h, § 4.4 :\n"
     "  à `ANT0` = 3,6 USD et 1,30 USD de l'heure, `HMAX` ≈ 11,6 h, marge ≈ 0,05 h)"),
    ("O6-34", "§ 9 : étape B par lecture_v4",
     "**C-4** : étape B jouée à S7 (tête détachée)",
     "**C-4** : étape B jouée à S7 (tête détachée ; brouillon 6 : `lecture_v4 etape-b` seule, la v2 et la v3 refusent la v7)"),
    ("O6-35", "§ 12 : marqueurs neufs",
     "| `PERIMETRE_T07` | ligne (A) | lignes de jeux et de concepts présentes à `main` à la création (`JD,JA` à l'écriture de cet ordre), "
     "ou `aucun` |\n",
     "| `PERIMETRE_T07` | ligne (A) | lignes de jeux et de concepts présentes à `main` à la création (`JD,JA` à l'écriture de cet ordre), "
     "ou `aucun` |\n"
     "| `SHA_SCRIPT_V3_T07` (**neuf au brouillon 6**) | ligne (A) | sha256 de `scripts/etape_a_t07_variante_b_v3.sh` sur `main`, écrit, "
     "répété en jouet et contre-lu (§ 13, S-12) |\n"
     "| `COMMIT_SRC_CONTRE_LU_T07` (**neuf au brouillon 6**) | ligne (A) | dernier commit contre-lu du code du remède (a') (vingt-six "
     "modules ; à ce jour `0d0c5da4061c28d808c3aa3b53c9a9a5e56a3a07`, non fusionné, contre-lecture en cours), dont `src/` est celui de "
     "C7 après fusion (R-2304) |\n"),
    ("O6-36", "§ 13 : S-12, S-13 et phrase finale",
     "§ 7 (couple 5) |\n\nS-8 à S-11 viennent de la contre-lecture R2 (`88ea9f06…`, § 5). Aucun des onze ne bloque l'étape A ; tous restent en réserve pour\n"
     "une v3 éventuelle (décision de la mère) ; **le script v2 (`e68d3306…`) reste celui de cet ordre** (R-2255, R-2258).",
     "§ 7 (couple 5) |\n| **S-12** | **bloquant au brouillon 6** | Le v2 appelle `lecture_v2` aux lignes 302 (`empreinte-config`), 357 (`repli-seul`), "
     "367 (`passe-blanc`) et 372 (`etape-a-apres-repli`) : avec la configuration v7, l'étape 8 s'arrête (« n_plancher 800 ≠ 200 », "
     "code 2, rien d'ouvert) ; aucune commande de la v4 n'est jouée. | **script v3** (`scripts/etape_a_t07_variante_b_v3.sh`, nom neuf, "
     "R12) : (1) les quatre appels → `controle_ia.t07.lecture_v4` ; (2) l'étape A lancée avec `CUBLAS_WORKSPACE_CONFIG=:4096:8` dans "
     "son environnement ; (3) le modèle et le nom du processeur (`/proc/cpuinfo`) écrits au journal ; hors EPYC, l'étape A lancée en "
     "plus avec `ATEN_CPU_CAPABILITY=avx2` et `MKL_CBWR=AVX2` (non éprouvé) ; (4) étape 8 : si la révision de 7b n'est pas celle de "
     "P3 (`runs/20261019-230011-p3-reel/manifeste.json`, `config.agent`), préchargement de celle de P3 (échec → code 2) ; (5) "
     "`planchers-figees-t07.npz` et `reextraction-p3-t07.json` poussés avec les sorties (déjà sous `donnees/<run-t07>/` et "
     "`diag/<run-t07>/`) ; (6) S-1, S-3, S-4, S-8 à S-11 au choix de la mère ; répétition jouet (comme le v2, § 11) et contre-lecture "
     "courte avant que la mère remplisse `SHA_SCRIPT_V3_T07` | P9 et P13 : sans le v3, aucune création |\n"
     "| **S-13** | mineur (brouillon 6) | La borne de taille (§ 5 bis) lit `P` = `n_plancher` de la v7 (800) mais ne compte ni "
     "`planchers-figees-t07.npz` (2 × 800 directions de largeur 4 096 en double précision ≈ 5,2·10⁷ octets, au-delà des 5·10⁷ « autres "
     "sorties ») ni les 2 × 200 directions de P3 notées en descriptif (≈ 400 nombres par action) ; à `d` = 4 096, `K` = 2, `p6` = 1, "
     "`C` = 2 et ≈ 5 760 actions notées : sondes neuves ≈ 1,29·10⁹, scores ≈ 0,45·10⁹, total ≈ 1,85·10⁹ octets, sous la borne de "
     "2·10⁹ (marge ≈ 0,15·10⁹, au lieu d'environ 0,8·10⁹ à `P` = 200) | au v3 : ajouter `2·n_p3` à `F` et la taille de "
     "`planchers-figees-t07.npz` aux « autres sorties » | rien ; la borne reste de 2·10⁹ octets |\n\n"
     "S-8 à S-11 viennent de la contre-lecture R2 (`88ea9f06…`, § 5). Aucun des onze ne bloque l'étape A ; tous restent en réserve pour\n"
     "une v3 éventuelle (décision de la mère) ; **le script v2 (`e68d3306…`) reste celui de cet ordre** (R-2255, R-2258). **Brouillon 6** :\n"
     "il ne l'est plus : **S-12 exige un v3** (configuration v7, commandes `lecture_v4`) ; S-1 à S-11 y restent proposés (décision\n"
     "de la mère) ; S-13 est un constat du rédacteur du brouillon 6."),
    ("O6-37", "§ 11 : répétition du v3",
     "**Pas de répétition neuve dans ce\nbrouillon** (la consigne ne la demande pas ; le script est inchangé).",
     "**Pas de répétition neuve dans ce\nbrouillon** (la consigne ne la demande pas ; le script est inchangé). **Brouillon 6** : le script v3 "
     "(§ 13, S-12) est à répéter en jouet (même répétition, configuration v7, commandes `lecture_v4`, un bras de réextraction établi "
     "et un bras arrêté) avant que la mère remplisse `SHA_SCRIPT_V3_T07` ; non fait ici."),
]

EXIGEES = (
    "**`ANT0` ≤ 3,6 USD**", "41 616 s = 11,56 h", "[ \"$HMAX\" -ge 41616 ]", "**3,2 à 4,7**", "**8,6 à 11,6**",
    "**Attendu ≈ 5,5 à 7,4 USD ; pire cas ≈ 12,5 à 16,4 USD**", "d'environ **0,45 h**", "`lecture_v4 repli-seul`",
    "`lecture_v4 passe-blanc`", "`lecture_v4 etape-a-apres-repli`", "`repli-recalcul`, refusé par la", "`CUBLAS_WORKSPACE_CONFIG=:4096:8`",
    "`ATEN_CPU_CAPABILITY=avx2` et `MKL_CBWR=AVX2`", "**préférence d'hôte EPYC**", "`prereg/T0.7-sondes-v0-v1-configuration-t07-v7.json`",
    "`4ff92c8e…`", "vingt-six modules", REV_P3, "**S-12**", "**S-13**", "## 0 ter. Ce qui change depuis le brouillon 5",
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
    """Joue l'extrait Python du § 4.3 sur des offres factices : un hôte EPYC passe avant un hôte moins cher ; sans EPYC, la moins chère."""
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
    print("§ 4.3 : choix de l'offre essayé sur trois cas factices (EPYC d'abord ; sans EPYC, la moins chère ; aucune offre) : conforme")


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        echec("usage : appliquer RACINE")
    racine = Path(argv[0]).resolve()
    b5 = (racine / CHEMIN_B5).read_bytes()
    if sha(b5) != SHA_B5:
        echec(f"brouillon 5 : empreinte {sha(b5)[:12]}… ≠ {SHA_B5[:12]}…")
    v7 = (racine / CHEMIN_V7).read_bytes()
    if sha(v7) != SHA_V7:
        echec(f"configuration v7 : empreinte {sha(v7)[:12]}… ≠ {SHA_V7[:12]}…")
    cites = sorted(set(chemins_cites(json.loads(v7.decode("utf-8")))))
    if cites != SIX_CHEMINS:
        echec(f"configuration v7 : chemins cités {cites} ≠ les six de la v4")
    print(f"brouillon 5 {SHA_B5[:12]}… et configuration v7 {SHA_V7[:12]}… vérifiés ; la v7 cite les six chemins de la v4")
    texte5 = b5.decode("utf-8")
    texte = texte5
    ids = [c[0] for c in COUPLES]
    if len(set(ids)) != len(ids):
        echec("identifiants de couples en double")
    for ident, ou, ancien, nouveau in COUPLES:
        texte = remplacer(texte, f"{ident} ({ou})", ancien, nouveau)
    print(f"{len(COUPLES)} couples appliqués, chacun à une occurrence")
    # tout le reste égal à l'octet : défaire dans l'ordre inverse
    defait = texte
    for ident, ou, ancien, nouveau in reversed(COUPLES):
        n = defait.count(nouveau)
        if n != 1:
            echec(f"défaisage de {ident} : « nouveau » présent {n} fois (une attendue)")
        defait = defait.replace(nouveau, ancien)
    if defait != texte5:
        echec("les couples défaits ne redonnent pas le brouillon 5 octet pour octet")
    l5, l6 = texte5.split("\n"), texte.split("\n")
    print(f"tout le reste égal à l'octet : couples défaits dans l'ordre inverse → brouillon 5 retrouvé ({len(l5)} → {len(l6)} lignes)")
    # vérifications
    if l6[0] != TITRE_B6:
        echec("titre du brouillon 6")
    for m in MARQUEURS:
        if texte.count(m) != 1:
            echec(f"marqueur {m} : {texte.count(m)} occurrences (une attendue)")
    autres = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", texte)) - set(MARQUEURS))
    if autres:
        echec(f"marqueurs inattendus : {autres}")
    print(f"marqueurs : {len(MARQUEURS)}, une occurrence chacun (dont deux neufs), aucun autre")
    appels = [l for l in re.findall(r"`lecture_v2 [a-z-]+`[^\n]{0,60}", texte) if "au brouillon 5" not in l]
    if appels:
        echec(f"appels lecture_v2 restants hors des mentions « au brouillon 5 » : {appels}")
    if "controle_ia.t07.lecture_v2" in texte:
        echec("commande controle_ia.t07.lecture_v2 restante")
    print("aucune commande lecture_v2 restante hors des mentions « au brouillon 5 »")
    for p in EXIGEES:
        if p not in texte:
            echec(f"phrase exigée absente : {p!r}")
    print(f"phrases exigées : {len(EXIGEES)} présentes")
    # devis : sommes et borne
    s6 = texte[texte.index("## 6. Devis"):texte.index("## 7. Arrêts")]
    rangs = [l.split("|")[1:4] for l in s6.split("\n") if l.startswith("| ") and "---" not in l][1:]
    att, pir = 0.0, 0.0
    att_haut = 0.0
    for nom, a, p in rangs[:-1]:
        a, p = a.strip(), p.strip()
        if " à " in a:
            x, y = a.split(" à ")
            att += float(x.replace(",", ".")); att_haut += float(y.replace(",", "."))
            x, y = p.split(" à ")
            pir_bas, pir_haut = float(x.replace(",", ".")), float(y.replace(",", "."))
        else:
            att += float(a.replace(",", ".")); att_haut += float(a.replace(",", "."))
            pir += float(p.replace(",", "."))
    total_att = (round(att, 2), round(att_haut, 2))
    total_pire = (round(pir + pir_bas, 2), round(pir + pir_haut, 2))
    print(f"§ 6 : sommes de la table : attendu {total_att[0]} à {total_att[1]} h, pire {total_pire[0]} à {total_pire[1]} h")
    if total_att != (3.24, 4.74) or total_pire != (8.56, 11.56):
        echec("sommes de la table du § 6 ≠ 3,24 à 4,74 h et 8,56 à 11,56 h")
    if round(total_pire[1] * 3600) != 41616:
        echec("borne de la minuterie ≠ pire cas en secondes")
    hmax = min(43200, int((20.0 - 3.6 - 1.2 - 0.1) / 1.3 * 3600))
    print(f"borne de la minuterie : 11,56 h = {round(total_pire[1] * 3600)} s ; HMAX à ANT0 = 3,6 USD et 1,30 USD de l'heure : {hmax} s "
          f"(≥ 41 616 : {hmax >= 41616}) ; à ANT0 = 3,7 : {min(43200, int((20.0 - 3.7 - 1.3) / 1.3 * 3600))} s")
    if hmax < 41616:
        echec("HMAX à ANT0 = 3,6 USD sous la borne")
    # blocs bash et extraits Python
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
    sortie = racine / CHEMIN_B6
    octets = texte.encode("utf-8")
    if sortie.exists() and sortie.read_bytes() != octets:
        echec(f"{CHEMIN_B6} existe avec un autre contenu (R12)")
    if not sortie.exists():
        sortie.write_bytes(octets)
    print(f"écrit : {CHEMIN_B6} ({sha(octets)})")
    print("TOUT PASSE")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
