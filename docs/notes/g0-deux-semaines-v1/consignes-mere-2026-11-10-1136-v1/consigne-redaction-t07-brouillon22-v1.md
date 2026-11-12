# Consigne : rédiger le brouillon 22 de T0.7 (code `37485ce5`, C7 sur `main`, audit des fuites, base (A) scellée, réserves) — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-10 à 13:39 UTC (heure relevée par `date -u`), autonomie de 12 heures (R-2201) sous accord général (GO-2026-11-10-05, GO-2026-11-10-09). Destinataire : un **rédacteur neuf**, qui n'a écrit ni T0.7 (brouillons 1 à 21), ni son module, ni leurs contre-lectures, ni T0.6, ni P3-bis, ni la base (A), ni la consigne d'audit, ni le texte de validité de l'adaptateur. Ayant lu T0.7, il est exclu ensuite de tout rôle de lecteur de P3-bis.

## Interdits, recopiés mot pour mot (`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md`, `1ee3b370…`)

# Interdits communs aux sous-agents de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy` (10 novembre 2026, v2)

Écrit le 2026-11-09 vers 22:00 UTC (heure relevée par `date -u`). Recopié mot pour mot dans chaque consigne de cette série.

**v2** (R-2086) : v1 recopiée à l'identique (`851028fc…`), plus la règle 9 ; écrite après deux accès mécaniques par recherche récursive (R-2064, R-2086).


1. **Fichiers et branches qu'on n'ouvre jamais** (ni lecture, ni affichage, ni copie, ni passage à un script, ni `git show`, ni `git ls-tree`, ni `git fetch`) :
   - `diag/*/lecture-sondes-t06.json` de tout run, et nommément `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` (DT-4 : rien avant le verdict scellé de P3-bis) ;
   - la lecture B de la course 7a et la branche `donnees/lecture-b-7a-quarantaine-v1` (R-2041, R-2048) ;
   - tout `diag/` et tout `runs/` de la course 7a (`20261109-070232-t06-reel`) et la branche `essai/t06-explo-v3`, sauf permission écrite dans la consigne ;
   - `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` (le bras d'attaque n'est pas le mandat de la mère : N-056, R-2045, R-2047) ;
   - les items, clés et réponses de l'étiqueteur (branche `prep/etiqueteur-v2-lecture-interrompue-reprise-v1`).
2. **Secrets** : ne jamais lire, afficher ni copier une valeur de clé ; jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ`, même avec la sortie jetée.
3. **Aucun appel** de modèle ni d'interface externe (Argon, Claude, autres), aucune location d'instance, aucun `vastai`, aucune dépense.
4. **Git** : aucun `checkout`, `switch`, `reset`, `stash`, `commit`, `push`, `fetch`, `merge`, `rebase`, ni modification de l'index ; les autres commits se lisent par `git show <commit>:<chemin>` seulement (ils sont déjà dans le clone local). Rien n'est écrit hors des chemins de sortie nommés dans la consigne.
5. **Essais** : ne pas lancer la suite complète (la session mère la fait tourner) ; des essais ciblés sont permis.
6. **Refus** : si un contrôle de permissions ou un classifieur refuse une action ou une réponse, s'arrêter sur ce point et le rapporter tel quel ; ni contournement, ni reformulation, ni transfert.
7. **Heures** : toute heure écrite est relevée par `date -u` et dite telle.
8. **Rapport final à la mère** : chemins écrits, empreintes sha256, verdict en une ligne, points ouverts ; **aucune valeur numérique tirée d'une sonde de 7a** (il ne doit d'ailleurs y en avoir aucune sous vos yeux).
9. **Recherches et parcours** : aucune recherche récursive (`grep -r`, `rg`, `find … -exec`, motif `**` ou `*/` développé par l'interpréteur) sur un dossier qui contient un chemin interdit sans l'exclure explicitement ; en pratique, chercher avec `git grep` et des exclusions de chemins (`git grep -n MOTIF -- . ':(exclude)docs/notes/bras-attaque' ':(exclude)scripts/extraire_mesures_epreuve_t06_v1.py' ':(exclude)diag' ':(exclude)runs'`) ou dans une liste de fichiers nommés ; `verifier-arbre` et tout outil qui hache un arbre entier ne se lancent que sur un arbre où `docs/notes/bras-attaque/` n'est pas extrait.

Exception à la règle 4 : aucune. Tu n'écris que sous `brouillons/` (noms neufs ci-dessous) et dans ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/t07-b22/`. Sceller : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN` (depuis `/home/user/controle-ia-travail`). Aucun commit : la mère commit.

## À lire (dans `/home/user/controle-ia-travail/`, empreintes à vérifier)

- `brouillons/T0.7-sondes-v0-v1-brouillon21.md` (`f7dcb226…`), son journal (`a7a358f4…`), ses couples et son script `…-brouillon21-faire-v1.py` (méthode à reprendre).
- Registre `registres/decisions.md` : R-2153, R-2158, R-2163, R-2166, R-2168, R-2171, R-2175, R-2193, R-2203, R-2209, R-2211, R-2212, R-2214, R-2216, R-2220, R-2229, R-2231, et toute ligne qui nomme T0.7 depuis R-2166 (`git grep -n "T0.7" -- registres/decisions.md`).
- Code : `docs/notes/g0-deux-semaines-v1/t07-module-v2/rapport-complementaire-5-option-c-v1.md` (table des 18 empreintes au commit `37485ce5`) ; contre-lecture courte `…/contre-lecture-code-t07-option-c-courte-v1.md` (CLC-01 à CLC-08) ; fichier `registres/code-t07/CODE-T07-v1.json` (non inscrit, R-2231) ; `src/controle_ia/t07/code_t07_v1.py` ; `scripts/etape_a_t07_variante_b_v2.sh` (l. 130-140).
- Audit des fuites : `brouillons/T0.7-audit-fuites-v1/T0.7-consigne-audit-fuites-v1-brouillon3.md` (`0d51099e…`) et son journal (§ 4 : couple A, couples B, C, D) ; contre-lecture `prereg/contre-lectures/T0.7-consigne-audit-fuites-v1-brouillon2-cl1.md` (Q3, CLAF-18).
- Base (A) **scellée** : `prereg/T0.8-base-A-mots-et-cout-v1.md` (`72b067d5…`), ligne `SCELLEMENT-T08-BASE-A` de `registres/scellements-v1.md` ; vérification courte `prereg/contre-lectures/T0.8-base-A-mots-et-cout-v1-brouillon2-verification-courte-v1.md` (VC-06, VC-08).
- Artefact d'adaptateur : `brouillons/validite-adaptateur-v1/validite-adaptateur-preenregistrement-v1-brouillon3.md` (`defd8ef0…`) et son journal ; `prereg/contre-lectures/validite-adaptateur-preenregistrement-v1-brouillon2-cl1.md` (dépendances envers T0.7) ; `docs/notes/rapports-directeur/premisses-trace-interne-v1.md` et `…-point-2a.md`.
- Concepts : `docs/procedures/consigne-concepts-sans-lien-T0.7-v3-corrigee-v1.md` (`ea5fe3f0…`, commit `0d4dd3ca`).
- T0.6 scellé : `prereg/T0.6-organismes-v0-v1.md` (`ef31feff…`), section « Concordance avec T0.7 ».

## Mandat

Révision par **couples** (`{id, section, motif, ancien, nouveau}`, chaque « ancien » présent une fois) appliqués par **un script à toi** (nom neuf), comme au brouillon 21. Contenu :

1. **Code (R-2229, R-2231)** : le « dernier commit contre-lu » devient `37485ce50601b7d7ff9035bc34c734ec689ca731` (contre-lecture courte `7a327462…`) ; les **18 empreintes** sont celles du rapport complémentaire 5 (trois changent : `lecture_v2.py`, `lectures_t07_v1.py`, `registre_v1.py`), recalculées par `git show 37485ce5:<chemin> | sha256sum`. **C7** : commit de `main` dont `src/` égale `37485ce5` (`git diff --quiet 37485ce5 C7 -- src`) et dont `tests/` égale celui de S7, fixé par la mère juste avant le scellement ; raison : `tests/test_lanceur_durable_v5_a1v4.py` corrigé sur `main` (R5) et l'essai CLC-04 ajouté, alors que le script de l'étape A exige `src` et `tests` égaux entre C7 et S7 ; la ligne `CODE-T07` citera `registres/code-t07/CODE-T07-v2.json` à ce commit ; `CODE-T07-v1.json` versé, jamais cité. Garde l'historique en une phrase.
2. **CLC-05** : phrase de la contre-lecture, à la table des réserves et à « Accord au code », point 20 (iii) : « écrite quand les scores sont ouverts ; sinon l'état des phrases est au manifeste de l'étape A et dans `sondes-t07.json` ». **CLC-04** : essai `tests/test_t07_ouvrir_reel_concepts_v1.py` (branche `prep/t07-essai-clc04-v1`, en cours) ajouté avant C7 : marqueur `<<ESSAI_CLC04_T07>>` (une occurrence ; la mère le remplit). **CLC-07** : déclaré en réserve.
3. **Ligne `AUDIT-FUITES-T07`** (R-2203, R-2212) : remplace le membre de phrase par le **couple A** du journal de la consigne d'audit (§ 4), mot pour mot ; applique aussi les **couples B, C, D** (imprécisions confirmées), chacun relu contre la ligne qu'il touche.
4. **Base (A) scellée** (R-2216) : l. ≈ 995 et ≈ 2006 (« le texte de T0.8 n'existe pas ») mises à jour (chemin, empreinte `72b067d5…`, ligne `SCELLEMENT-T08-BASE-A` datée `2026-11-10T12:21:55Z`, avant toute création de 7b) ; confirmation des clés `T08` (« ignorées et comptées », l. ≈ 2036-2037) ; **VC-08 / Q-4 (a) / CLBA-14** : phrase dans « Clés par étape » : « si BA-L2 s'applique (témoin positif de la base (A) en défaut), l'étape B attend le mot de Lazar » ; VC-06 en réserve tant que `scripts/controle_lecture_t06_v1.py` n'est pas dans `main`.
5. **Concepts** : cite la consigne v3 corrigée (`ea5fe3f0…`, commit `0d4dd3ca`) là où le texte cite la consigne des concepts.
6. **Artefact d'adaptateur** (ligne 5, R-2163, R-2168, R-2175 D-1 (b)) : renvoie au texte de validité de l'adaptateur (préenregistrement séparé, GO-2026-11-10-07) pour (i), (ii), (iv-a) `S100` contre `T100`, (iv-b), (iv-c), (iii) ; écris ce que ce texte lit des scores de l'étape A de T0.7 et lève, dans le brouillon 22, les dépendances qu'il attend de T0.7 (contre-lecture `validite-…-brouillon2-cl1`) ; **aucun critère de T0.7 ne change**.
7. **Puissance par dose** (R-2171) : aire minimale détectable par dose aux effectifs du texte, comparée au seuil de la base (0,70), calculée **par un script à nom neuf** versé avec sa sortie ; section des réserves, sans changer aucun seuil.
8. **P-064, P-065** : défauts échus le 10 novembre vers 17:13 UTC (R-2166) ; garde `<<MOT_LAZAR_P064>>` et `<<MOT_LAZAR_P065>>` tels quels (la mère les remplit après l'échéance).
9. **Marqueurs restants**, une occurrence chacun, listés à l'en-tête : `ENTROPIE_T07`, `EMPREINTE_CONFIG_T07`, `EMPREINTE_ORDRE_EXECUTION_ETAPE_A_T07`, `GO_ETAPE_A_T07`, `MOT_LAZAR_P064`, `MOT_LAZAR_P065`, `ESSAI_CLC04_T07` ; vérifie par `controle_ia.prereg.problemes` qu'il n'en reste pas d'autre.
10. **Sections gelées** (« Hypothèse », « Prédiction », « Métrique », « Seuil », « Plan d'analyse », « Critères de lecture gelés », « Liste d'arrêt ») : tout couple qui les touche est déclaré un par un, avec sa raison ; **aucune hypothèse, prédiction, signe ni seuil ne change** ; si un point l'exigeait, arrête-toi et signale-le (nœud).
11. En-tête : statut « brouillon 22 », titre vérifié.

## Sorties (noms neufs, scellés ; brouillon 21 intact)
`brouillons/T0.7-sondes-v0-v1-brouillon22.md`, `…-brouillon22-couples-v1.json`, `…-brouillon22-faire-v1.py`, `…-brouillon22-journal-v1.md` (couples, écarts, questions Q-n avec recommandation), et le script et la sortie du point 7. Rapport final : chemins, empreintes, nombre de couples, marqueurs restants, questions pour la mère.
