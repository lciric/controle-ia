# Contre-lecture n° 7 — préenregistrement « gradient conçu par l'essaim », étape 1 (sondes), v7

## Identité
Relecteur **neuf (R2)**, limité aux corrections CL6-01 à CL6-05 de la contre-lecture n° 6 et à ce qu'elles touchent.
Je n'ai écrit ni le préenregistrement (v1 à v7), ni le code, ni les lanceurs, ni aucune contre-lecture ni revérification
précédente. Je ne refais ni les contre-lectures n° 4/5/6 ni la revérification du code ; je ne change aucune hypothèse,
prédiction, métrique, seuil ni table de lecture (R1). `python -B`, aucun appel payant, aucun organisme hors du bac à
sable de pytest, aucune clé ni secret lu ou affiché.

## Heures (UTC)
- Début : 2026-10-25 03:54:50.
- Fin : 2026-10-25 04:06:49.

## Texte relu + empreinte
- `gradient-etape1-sondes-v7.md` (marqueurs de scellement `<<…>>` non remplis — attendu).
- sha256 = `84708a9222dd4eddb809bff3bb8994051ea85fe485f13736ee4e547adaaeb0e7` ; compagnon `.sha256` concordant ;
  `EMPREINTES-pieces.txt` concordant.

## VERDICT : **scellable**
Compte par gravité : **0 bloquante, 0 majeure, 1 mineure (non bloquante, CL7-01), 0 de forme.**
Les deux remarques qui rendaient la v6 non scellable (bloquante CL6-01 et majeure/bloquante-pour-l'exécution CL6-02)
sont traitées et éprouvées par preuve rejouée ; CL6-03/04/05 sont traitées. La seule remarque nouvelle (CL7-01) est une
note de traçabilité de pièces hors de mon périmètre de vérification, sans effet sur aucun énoncé : elle ne s'oppose pas
au scellement.

## Suivi CL6-01 à CL6-05

| Remarque | État | Preuve rejouée |
|---|---|---|
| **CL6-01** (bloquante) — le script de scellement v6 refusait de sceller (cherchait l'entrée « Contre-lecture 6 » au libellé « lanceur v3 corrigé » absent du texte v6) | **traitée** | Scellement à blanc de `sceller_etape1_v7.py` (`python -I -B`, `depot_src` vide) : il passe la vérification d'empreinte, remplace les cinq marqueurs `<<…>>`, **trouve** l'entrée « Contre-lecture 7 », et échoue **uniquement** sur `from controle_ia import prereg` (`ModuleNotFoundError`) ; **aucune** sortie écrite. Contrôle négatif (R5) : entrée « Contre-lecture 7 » altérée (« lanceur v4 »→« lanceur v3 corrigé ») → `refus : entrée « Contre-lecture 7 » introuvable` (exit 2). La chaîne `ancienne` du script concorde donc au caractère près avec le texte. « lanceur v3 corrigé » n'apparaît qu'une fois (l. 7, en citation du bug corrigé) ; « lanceur v4 » : 10 occurrences. Docstring du script juste (CL6-04). |
| **CL6-02** (majeure, bloquante pour l'exécution) — la boucle `prives` de `ABAISSER_SOURCE` abandonnait sur un dossier inscriptible par tous imbriqué sous un temporaire déjà rendu privé (errno 2) | **traitée** | Diff `224de13`→`bef2c2f` minuscule : +3 lignes dans `bac_a_sable.py` (`if ctypes.get_errno() == 2: continue` dans la boucle `prives`) + `test_cl6_02`. Les boucles `prives` et `caches` traitent errno 2 à l'identique ; `ABAISSER_SOURCE` est partagé, sans branchement par bras → correction valable pour **les deux bras** A/B. Banc de mutation `muter_cl6_v1.py` rejoué : **témoin PASSE, mutant ÉCHOUE**. `test_cl6_02` seul : 1 passed (3.43 s). Suite complète : **133 passés, 3 désélectionnés** (= sortie fournie). |
| **CL6-03** (mineure) — contradiction interne sur la présence de `BRAVE_API_KEY` au scellement | **traitée** | La clause dit maintenant que le **nom** de Brave est défini dans la session « session-depot » au scellement (renvoi à « État au scellement »), et conditionne les **cinq** comparaisons par paire (au lieu de quatre) à la présence de la clé **au lancement**, en accord avec le paragraphe « État au scellement » (noms définis, aucune valeur lue). Plus de contradiction. Aucune valeur de clé affichée. Le compte 4/5 et le renvoi « (Seuil) » sont inchangés (pas de changement de seuil). |
| **CL6-04** (forme) — docstring du script inexacte (« contre-lecture n° 4 », « `sceller_etape1_v4.py` ») | **traitée** | Docstring de `sceller_etape1_v7.py` : dit « la contre-lecture n° 7 » (l. 4) et « Décliné de `sceller_etape1_v6.py` sous un nom nouveau (R12) » (l. 6). Aucune occurrence de « n° 4 » ni « `sceller_etape1_v4.py` ». |
| **CL6-05** (forme) — noms des pièces de mutation discordants (l. 37) | **traitée** | Texte v7 (l. 45-46) : `mutations-rv-v2.txt`, `sortie-mutations-cl5-v1.txt`, `sortie-mutations-cl6-v1.txt` ; cohérent avec l'entrée CL5-11 (l. 677) et l'entrée CL6-05 (l. 695). `sortie-mutations-cl6-v1.txt` existe et montre témoin vert / mutant rouge. |

## Remarques nouvelles

- **CL7-01 (mineure, non bloquante).** Le bloc commit, puce « Lanceur des courses », renomme le dossier de pièces
  `prereg/pieces-gradient-etape1-v6/` → `prereg/pieces-gradient-etape1-v7/` pour deux sorties du lanceur
  (`sortie-essais-lanceur-v4.txt` `0f510c17…`, `sortie-options-analyseur-v4.txt` `16984f05…`). Ce renommage n'est pas dans
  l'énumération littérale de la consigne R1, mais il relève de l'entretien de version (comme le numéro de version) : les
  empreintes tronquées citées sont **inchangées** par rapport à la v6, donc les fichiers sont le même contenu, seulement
  reclassés. Il ne touche aucune hypothèse, prédiction, métrique, seuil ni table de lecture, et le validateur ne contrôle
  pas ces chemins — d'où « non bloquante ». À confirmer au scellement (R6) : que le dossier `pieces-gradient-etape1-v7/`
  contient bien ces deux fichiers aux empreintes citées (hors de mon jeu de pièces, voir « ce que je n'ai pas pu
  vérifier »).

## Vérification R1 (invariants)
Le patch `diff-texte-v6-v7.patch` appliqué à la v6 (`ce78d5e5…`) **reconstruit exactement** la v7 (`84708a92…`,
`diff` reconstruit vs réel vide) : j'ai donc vu **tous** les changements v6→v7 (7 hunks, pas un de plus). Ils se répartissent :
1. Numéro de version (titre v6→v7) et paragraphe de version (réécrit ; « lanceur v4 (inchangé) » ; historique relabellisé
   « lanceur v4 » — fermeture CL6-01 ; déclare ne changer aucun énoncé).
2. Bloc commit : commit `224de13`→`bef2c2f` ; **132→133** essais ; **seize→dix-sept** mutations ; noms de pièces (CL6-05) ;
   empreinte `bac_a_sable.py` `8f52ec88…`→`a84279e5…` et arbre du noyau `f43946a3…`→`062eebcc…` ; renommage du dossier de
   pièces du lanceur (CL7-01).
3. Passage Brave, Plan d'analyse l. 310 (CL6-03) — seule modification dans « Plan d'analyse ».
4. Entrée CE3-16 : « la 6 dans cette v6 »→« la 7 dans cette v7 ».
5. En-tête de traitement CL5 : « texte de cette v6 »→« texte de la v6 ».
6. Lignes CL5-11 (noms de pièces, CL6-05) et CL5-12 (`sceller_etape1_v7.py`, docstring juste, CL6-04) ; entrée
   « Contre-lecture 6 » remplie (date, texte relu + empreinte, rapport + empreinte, verdict, table CL6-01..05) ; nouvelle
   entrée « Contre-lecture 7 » (gabarit).

Sections invariantes repérées et **hors** des régions modifiées (donc byte-identiques à la v6) : Hypothèse (l. 119),
Prédiction chiffrée et signe attendu (l. 154), Métrique (l. 166), Seuil (l. 237, dont les 0,71 %/0,76 % binomiaux
l. 263-266), Critères de lecture gelés (l. 493), Liste d'arrêt (l. 526). **Aucune** hypothèse, prédiction chiffrée,
métrique, seuil ni table de lecture ne change. R1 tenue.

## Ce que j'ai rejoué (commandes, sorties, empreintes)
1. `sha256sum -c EMPREINTES-pieces.txt` → 15/15 OK ; v7 = `84708a92…`, compagnon concordant.
2. `git -C GR rev-parse HEAD` = `bef2c2f9f9c684f414aa36c2f08e04e0ed90e6fa` ; `git status --short` vide.
   `bac_a_sable.py` = `a84279e536b348def1eff2d61526e1fa0b55a240f311a2a81060df04b316b287` (= texte l. 59) ;
   `boucle.empreinte_arbre('essaim_m3/noyau')` = `062eebccf2cb026c0e57e8b734bc07ebd4144d76453db95f7a430f2bc6cafb56`
   (= texte l. 63) ; `analyse_gradient.py` = `4b54d380c171cf9e89c9f95bb5a9f3f357d262a27500b3a0e2f9b272eeb2e380`
   (= texte l. 48). Copies des pièces `code/bac_a_sable.py` et `code/analyse_gradient.py` identiques à GR.
3. Scellement à blanc : `python -I -B sceller_etape1_v7.py config.json` (`depot_src` vide) → remplacement des 5 marqueurs
   + entrée « Contre-lecture 7 » trouvée, échec `ModuleNotFoundError: controle_ia`, aucune sortie. Contrôle négatif →
   `refus : entrée « Contre-lecture 7 » introuvable`. (`controle_ia` non importable du venv seul en `-I` — vérifié ;
   numpy 2.4.6 ≥ 1.25, R9.)
4. Banc de mutation `muter_cl6_v1.py` : témoin PASSE (5.32 s), mutant ÉCHOUE (3.41 s). `test_cl6_02` seul : 1 passed.
   Suite complète (3 désélectionnés) : `133 passed, 3 deselected` (exit 0).
5. Validateur : vrai scellement vers une sortie **jetable** (scratchpad, `depot_src`=`/home/user/controle-ia-travail/src`)
   → exit 0 ; vérification indépendante `prereg.problemes(sortie)` = `[]` ; entrées « Contre-lecture » 1 à 7 détectées
   (chacune avec ses deux empreintes une fois remplie). Sortie jetable supprimée. `src/controle_ia/prereg.py` identique à
   la copie `code/prereg.py`.
6. R1 : reconstruction v7 depuis v6 + patch → empreinte identique `84708a92…`.

## Ce que je n'ai pas pu vérifier
- L'existence sur disque des deux sorties du lanceur `sortie-essais-lanceur-v4.txt` (`0f510c17…`) et
  `sortie-options-analyseur-v4.txt` (`16984f05…`) au **nouveau** chemin `prereg/pieces-gradient-etape1-v7/` (CL7-01) :
  hors de mon jeu de pièces. Les empreintes tronquées sont inchangées depuis la v6 (même contenu, reclassé).
- L'existence sur disque des pièces de mutation des rondes antérieures `mutations-rv-v2.txt` (v5) et
  `sortie-mutations-cl5-v1.txt` (CL5) : non fournies (seule `sortie-mutations-cl6-v1.txt` m'a été remise). J'ai vérifié la
  **cohérence des noms** dans le texte, pas les fichiers eux-mêmes.
- Il n'existe **aucun** essai pytest nommé `test_cl6_01` (CL6-01 est une correction du script de scellement, éprouvée par
  le scellement à blanc, non par pytest) ; j'ai donc lancé `test_cl6_02` seul, pas `test_cl6_01`.

## Hygiène
- Tous mes dossiers temporaires du scratchpad (`tmp-cl7`, `tmp-mut`, `tmp-r1`, `tmp-valid`, HOME de pytest) ont été
  retirés ; sortie de scellement jetable supprimée.
- `GR/_home`, créé par le banc de mutation (témoin lancé dans GR), a été retiré ; **GR reste propre** (`git status`
  vide, HEAD `bef2c2f`) ; je n'ai pas touché à `essaim_m3/`. Aucune écriture de ma part dans le dépôt du code.
- **Non retiré :** 108 espaces de travail éphémères créés par mes exécutions de pytest sous `/var/lib/essaim-m3`
  (ESPACE_BASE du cadre de test). La suppression récursive a été **refusée par le classifieur de sécurité auto** (action
  jugée dangereuse) ; je n'ai pas contourné ce refus. Ces dossiers (paires `archive_vue`/`travail`) sont inoffensifs : le
  cadre de test les accumule par conception (782 préexistaient de sessions antérieures). Laissés en l'état.
- Aucune instance de calcul touchée ; aucun appel payant ; aucune clé ni secret lu ou affiché ; aucun sous-agent.

## EMPREINTES (mes sorties)
- Texte relu `gradient-etape1-sondes-v7.md` : `84708a9222dd4eddb809bff3bb8994051ea85fe485f13736ee4e547adaaeb0e7`
- Ce rapport `contre-lecture-preenregistrement-gradient-etape1-v7.md` : empreinte calculée après écriture, transmise dans
  la passation à l'appelant (un fichier ne peut contenir sa propre empreinte).
