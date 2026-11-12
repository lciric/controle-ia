# Contre-lecture neuve (R2) de l'amorce v6, du lanceur v8, de l'ordre E3 v5 et du candidat 7 de T0.6, avec la question 7 (concurrence C08) — v1

## Consigne (messages de la session mère, recopiés mot pour mot)

> Mère — 16:35 UTC. **Contre-lecture de la v8, toute en lignée Opus** (R-1688) : lanceur v8, amorce v6, ordre E3 v5, candidat 7. L'autrice est la fille 10, Sonnet 5.5. Le code va à un **sous-agent neuf** (`model: opus`), qui n'a lu ni ces pièces ni leurs versions antérieures. L'ordre et le candidat, c'est toi. Vise une heure : E3 attend cette lecture, et la course du 11 aussi.
> **Pièces** (empreintes vérifiées par la mère) :
> - `prep/t06-lanceur-v2` à **`1921fc3e`** (code à `20f576db`, descendant de `0e52603c`, aucun fichier changé hors de T0.6) : `scripts/amorce_instance_t06_v6.sh` `78ad709f…`, `scripts/lancer_t06_v8.sh` `debcfa65…`, `src/controle_ia/t06/session_v7.py` `f3def7f2…`, `tests/test_t06_v6_amorce.py` `e95240a2…`, `tests/test_t06_v8_scripts.py` `87871692…`, `scripts/banc_mutations_t06_v8.py` `99ccdbbe…`, `tests/test_t06_cibles_invisibles_v1.py` `b7409f04…`, rapport `rapport-developpeur-lanceur-T0.6-v8.md` ;
> - ordre `brouillons/ordres-t06-e2-e3-v5/ordre-fille-6-t06-e3-v5.md` `f00e143d…` et son générateur ;
> - `prep/t06-candidat2-v1` à `3bf36bfa` : candidat 7 `a7ba0f4a…`.
> **Questions** :
> 1. **Différences** v5 → v6 et v7 → v8 : seulement tes six points de la v7, plus le point 7 (filtre `cuda_max_good>=13.0`, garde locale sur l'offre choisie, garde de l'amorce sur `torch.cuda.is_available()` en mode réel) ?
>    - États de présence : 0 / 1 / 3 / 2 pour `presente`, 0 / 4 / 2 pour `seule`, plus `ARRET inventaire` à trois relevés.
>    - Masquage par un tube, sans aucun fichier brut ; refus des clés de moins de 8 caractères ; `--tail 20000`.
>    - Message de `sparse-checkout` cité dans le refus ; extraction déclarée à 900 s.
> 2. **Rejoue** : les suites t06 (460) ; la suite complète sur un clone allégé (3 005 annoncés, 0 sauté) ; le banc (59 sur 59). Ses mutations couvrent-elles maintenant l'inventaire vide, `tail`, le masquage et le CUDA ?
> 3. La syntaxe `cuda_max_good>=13.0` est-elle valide pour la recherche de `vastai` 1.8.3 ? (Lis-la dans le code de `vastai` si tu peux ; aucun appel réseau.)
> 4. **Ordre E3 v5** : il est parti de l'ordre E3 scellé **v3** (`401468d7…`). Or le scellé en vigueur est la **v4** (`docs/procedures/ordre-fille-6-t06-e3-v4.md`, `1dc7cba6…`, couples de la mère `366d69e7…`). Vérifie que les changements de la v4 y sont repris : renvoi vers l'ordre E2 v4, condition d'E3 comptant les tentatives d'E2. Sinon, couples. Il faudra aussi y compter la dépense **finale** d'E2. Seul marqueur `<<COMMIT_EPREUVES>>`, rempli par quel commit ?
> 5. **Candidat 7** : il cite les ordres scellés v3. Les ordres en usage sont la v4 pour E2 et, bientôt, la v5 pour E3 : couples ou report au candidat final ?
> 6. **Verdict** par pièce.
> Rendu sur `prep/fille-9-contre-lectures-v2`, dossier `docs/notes/g0-deux-semaines-v1/contre-lecture-lanceur-T0.6-v8/`, puis message. Aucune donnée réelle, aucune clé, aucune location.
>
> Mère — 16:47 UTC. **Question 7, à ajouter à ta contre-lecture v8** (R-1689). E2-5, cas 2, au troisième démarrage de l'instance A, après l'heure de dépense épuisée : l'amorce a poussé les commits en attente puis demandé la destruction, mais l'instance a fini « exited », pas détruite.
> Mon analyse (amorce v5, l. 170-196, et minuterie, l. 89-93) :
> - la minuterie relancée voit l'heure de dépense épuisée passée, **sans** le marqueur `t06-depense-epuisee` (les runs précédents avaient fini avant cette heure) ;
> - elle prend donc la branche C08 : consignation, puis `PUT stopped` ;
> - l'arrêt tue le conteneur avant que la minuterie ne lise `t06-detruire`.
> C'est une **concurrence entre l'arrêt C08 et la destruction du second démarrage**.
> Confirme-la ou réfute-la, et dis si la v6 et la v8 l'ont encore. Propose le correctif le plus étroit : par exemple, poser le marqueur avant de lancer la minuterie lors d'un second démarrage après cette heure, ou faire primer `t06-detruire` dans la boucle. Dis aussi par quel essai l'éprouver (cas sain et artefact). Ce correctif ira dans la version suivante, avec tes couples.

## Verdict par pièce

| pièce | verdict | ce qui bloque E3 | ce qui peut attendre la course |
|---|---|---|---|
| ordre E3 v5 | **scellable après 3 couples** (`couples-ordre-e3-v5.json`) ; **`<<COMMIT_EPREUVES>>` = `1921fc3e`** | les 3 couples | — |
| amorce v6 | conforme aux 7 points ; **porte encore la concurrence C08** (question 7) | rien pour E3 (aucun redémarrage prévu) | correctif C08 (v7 de l'amorce) |
| lanceur v8 | conforme aux 7 points, avec deux défauts | échec de `masquer` non détecté (`PIPESTATUS[1]`) : à corriger si l'on refait un commit, sinon couvert par la relecture humaine | inventaires bruts de `creation` et `apres-creation` ; `set -u` (l. 239) ; libellés « v4 » |
| `session_v7` | un défaut : `instance_seule` | réponse non concluante lue comme « introuvable » ; **couvert pour E3 par le couple 3** | correction dans le code (v9) ; `NaN` dans la garde CUDA |
| essais | verts | rien | **439** collectés, et non 460 : écart à expliquer par l'autrice ; essais R5 ci-dessous |
| banc | journal lu, **aucun passage complet unique du fichier final** | rien | un passage complet ; mutations manquantes |
| `tests/test_t06_cibles_invisibles_v1.py` (fichier existant modifié) | conforme, additif | rien | tension avec R12 à consigner ; artefact pour `_fuit` sur un nombre seul |
| candidat 7 | égal au candidat 6 plus ses couples, à l'octet ; **citations des ordres et du commit d'E2 dépassées** | — | report au candidat final (point 5) |

### Qui lit quoi
- **Code, essais, banc, syntaxe CUDA, fichier modifié** (questions 1 à 3) : sous-agent neuf de **lignée Claude Opus**, qui n'a lu ni ces pièces ni leurs versions antérieures, ni mes contre-lectures. Il a lu de 16:31 à 17:18 UTC. J'ai recoupé dans le code son constat bloquant (`session_v7.py`, l. 60-83).
- **Ordre E3 v5, commit d'épreuve, candidat 7, question 7** : fille 9, **lignée Claude Opus 5.5**. Le 7 novembre 2026, de 16:30 à 17:20 UTC (`date -u`). L'autrice est la fille 10, Sonnet 5.5.
- Rien de loué, aucune clé lue, aucun appel à `vastai`, aucune donnée réelle.

## 1. Différences (sous-agent Opus)
- **Les sept points annoncés sont faits.**
  - États de présence : une liste non vide sans l'identifiant, à deux relevés, donne `ARRET mort`. Une liste vide, illisible ou en échec mène à l'instance seule, puis à une ALERTE, puis à `ARRET inventaire` au troisième relevé. Jamais de `ARRET mort` sur une liste vide.
  - Masquage par un tube, couvrant les quatre clés.
  - `--tail 20000`.
  - Message de `sparse-checkout` cité dans le refus.
  - Garde CUDA :
    - filtre `cuda_max_good>=13.0` ;
    - garde locale qui refuse une offre sans la clé ; cette clé existe bien dans des sorties brutes réelles de Vast versées au dépôt (`traces/t04-offres-20261005-144349/offres.json`, valeurs 13.0 et 13.2) ;
    - garde `torch.cuda.is_available()` limitée au mode réel ;
    - une clé absente en mode jouet n'est pas refusée.
- **Écarts jugés acceptables** :
  - carte invisible en mode réel : refus et destruction au lieu de l'arrêt, ce qui est annoncé au point 7 ;
  - seuil de masquage `>= 8`, cohérent avec le refus des clés courtes ;
  - `ARRET inventaire` sans commande d'arrêt imprimée, par choix.
- **Défaut, `instance_seule`** (`session_v7.py`, l. 60-83, recoupé par moi) :
  - un objet JSON d'erreur sans `id` (`{"success": false, "error": …}`) est rendu « introuvable » ;
  - le motif `"404"` est cherché comme sous-chaîne, si bien qu'un texte d'erreur 500 qui cite un identifiant contenant « 404 » est rendu « introuvable » ;
  - avec une liste vide, comme celle vue à E2, deux réponses de ce genre donnent un **faux `ARRET mort`**, et la surveillance s'arrête sur une instance vivante.
- **Défaut, échec de `masquer`** (`lancer_t06_v8.sh`, l. 252, 258, 266) : seul `PIPESTATUS[0]` est lu. Rien ne fuit, mais la copie est vidée sans ALERTE (R5).
- **À la course** :
  - `creation` et `apres-creation` écrivent `instances.json` et `instances-apres.json` bruts (l. 195, 224), alors que `extra_env` peut porter des clés ;
  - `${#CONTROLE_IA_GITHUB_TOKEN}` sous `set -u` sort en 127 au lieu de 2 (l. 239) ;
  - `NaN` passe la garde CUDA.

## 2. Comptes (sous-agent Opus)
- **Suites t06** : **439 réussis**, 0 échec. Le rapport annonce **460**, alors que la collecte de `tests/test_t06_*.py` à `1921fc3e` donne 439 : écart à expliquer par l'autrice.
- **Suite complète** sur un clone allégé (28 motifs de l'amorce v6, 329 Mo) : **3 005 collectés, 3 002 réussis, 3 échecs, 0 sauté**.
  - Les 3 échecs sont `test_corpus_arxiv` : `pypandoc` est absent du venv local, ce qui n'est pas un défaut.
  - Les tranches coupées à 900 s ont été rejouées isolément, toutes vertes.
- **Banc** : non rejoué, faute de temps. D'après son journal, 57 mutations sont tuées au premier passage, plus 2 réécrites et rejouées seules ; **aucun passage complet unique du fichier final** `99ccdbbe…`.
  - Il couvre maintenant l'inventaire vide, `tail`, le masquage et le CUDA.
  - Il manque : le retrait d'une clé de `masquer`, l'échec de `masquer`, un objet d'erreur ou un « 404 » dans un identifiant pour `seule`, et la partie numérique de `_fuit`.

## 3. Syntaxe `cuda_max_good>=13.0`
**Non vérifiée.** Aucun paquet `vastai` n'est installé localement, il n'y a aucun `vast.py`, et les `vastai` du dépôt sont des faux d'essai.
- Un champ inconnu ne produirait, au plus, qu'un avertissement sur la sortie d'erreur, que le lanceur range dans `offres.err` sans le lire. La garde locale sur l'offre choisie reste le vrai rideau, et elle est correcte, au `NaN` près.
- **Recommandation à 0 USD, avant E3** : à l'étape 2 de l'ordre (lecture facultative), relire `offres.err` après la recherche filtrée, et vérifier que `cuda_max_good` vaut au moins 13 dans chaque offre rendue.

## 4. Ordre E3 v5 (fille 9)
- **Générateur rejoué** : il part de l'ordre scellé **v3** (`401468d7…`, sur `main`) et produit la v5 **à l'octet** (`f00e143d…`) par 5 remplacements uniques. Le filtre de lecture est celui de `session_v7.filtre_recherche` : `… reliability>=0.98 inet_down>=500 cuda_max_good>=13.0 …`. Seul marqueur : `<<COMMIT_EPREUVES>>` (2 occurrences).
- **Changements de la v4 scellée** (`1dc7cba6…`, révision R-1685) par rapport à la v3, et leur sort dans la v5 :
  - renvoi vers l'ordre E2 **v4** : **absent**. La v5 renvoie à `docs/procedures/ordre-fille-6-t06-e2-v3.md`. **Couple 1.**
  - condition comptant les deux tentatives d'E2 (instances 59555071 **et 59589344**) : **absente**, la v5 ne compte que 59555071. **Couple 2**, qui compte aussi la dépense **finale** d'E2 (toutes ses instances, reprise comprise, par la facture ou par relevé), et qui exige qu'E2 soit terminée avant toute création d'E3.
  - commit d'épreuve neuf `0e52603c` : sans objet, puisque la v5 porte le marqueur.
- **Couple 3** : conduite sur `ARRET mort`, face au défaut d'`instance_seule` (point 1). Une réponse JSON sans `id`, ou un texte d'erreur qui ne dit pas « not found », n'est pas « introuvable ». L'instance est alors réputée vivante : nouvelle vérification toutes les 2 minutes pendant 20 minutes au plus, et destruction par l'identifiant dès qu'elle répond.
- **`<<COMMIT_EPREUVES>>` = `1921fc3e`** :
  - il descend de `0e52603c` (compagnons des tâches d'épreuve) et de `20f576db` (code v8) ; de `20f576db` à `1921fc3e`, seuls le rapport v8 et un journal changent ;
  - `registres/go.md` porte GO-2026-11-06-01 ;
  - `config-t06-epreuve-e3-v2.json` et les deux fichiers de tâches d'E3 ont des compagnons égaux à leurs empreintes.
  - Si la mère fait corriger le code avant E3, il faudra un nouveau commit d'épreuve.

## 5. Candidat 7 (fille 9)
- Rejoué par script : le candidat 6 (`3250b1f8…`) plus les 11 couples, avec les valeurs du script remplies, donne le candidat 7 **à l'octet** (`a7ba0f4a…`).
  - Valeurs du script : heure ; 12 empreintes recalculées sur `1921fc3e` ; 4 pièces de `main` ; `COMMIT_MAIN` = `d44373e7`.
  - Cinq marqueurs présents, aucun `<OFFRE>`.
- **Citations dépassées** (l. 186) : le candidat cite les ordres scellés **v3** d'E2 et d'E3, les couples de la mère v3, et le « commit d'épreuve de l'ordre d'E2 : `04d89122` ». Or l'ordre d'E2 en vigueur est la **v4** (`docs/procedures/ordre-fille-6-t06-e2-v4.md`, couples de la mère `366d69e7…`, commit `0e52603c`), et celui d'E3 sera la v5, avec son commit.
- **Recommandation : report au candidat final**, pas de couple maintenant.
  - Raison : les empreintes de la v5 d'E3 et du commit d'épreuve définitif ne seront connues qu'après le scellement de la v5, puis la fin d'E3. Un couple écrit aujourd'hui serait dépassé à son tour.
  - Ces citations sont documentaires : la chaîne ne les lit pas mécaniquement (la liste des citations lues est en fin de candidat).
  - Le candidat final doit citer : l'ordre E2 v4 et ses couples ; l'ordre E3 v5 scellé et ses couples ; le commit d'épreuve de chacun ; et, si la v9 existe, le code de la course.

## 6. Question 7 : concurrence entre l'arrêt C08 et la destruction (fille 9)

**Confirmée**, et **toujours présente dans l'amorce v6** : minuterie, l. 91-96 ; lancement, l. 185 ; second démarrage, l. 189-196. La v5 et la v6 ont le même code à cet endroit. Le lanceur v8 n'y touche pas.

Déroulé, d'après le code :
1. À tout démarrage, l'amorce lance la minuterie (`setsid … t06-minuterie.sh "$ECH" "$DEP"`, v6 l. 185) **avant** de traiter le second démarrage (l. 189).
2. Au premier tour de boucle, la minuterie teste `date ≥ DEP` et l'absence du marqueur `t06-depense-epuisee` (l. 92). Si les runs précédents ont fini avant l'heure d'épuisement, le marqueur est absent : elle entre dans la branche C08, pose le marqueur, consigne (`consigner`, jusqu'à 2 400 s, sous le verrou), puis `PUT stopped` (l. 96).
3. Pendant ce temps, l'amorce consigne de son côté (jusqu'à 1 200 s, même verrou), puis `detruire` pose `t06-detruire` et attend la minuterie.
4. La boucle ne relit `t06-detruire` qu'à son **prochain** tour (l. 91). Or le `PUT stopped` du tour en cours arrête le conteneur avant ce tour : la minuterie meurt avec lui, et le `DELETE` n'est jamais envoyé.
5. L'instance finit « exited », non détruite. Elle facture son stockage jusqu'à ce que quelqu'un la détruise, puisque l'échéance de la minuterie ne joue plus sur un conteneur arrêté.

Portée :
- Même concurrence au **premier** démarrage après l'heure d'épuisement : la minuterie entre en C08 pendant que l'amorce demande la destruction.
- Elle ne touche pas un run qui atteint l'épuisement en cours de route, car l'amorce ne demande alors pas de destruction concurrente.
- Les essais actuels ne la voient pas : les essais de l'amorce tournent en essai local, sans minuterie (`AMORCE_ESSAI_LOCAL=1`), et ceux de la minuterie n'y posent jamais `t06-detruire` pendant C08.

**Correctif le plus étroit**, en deux lignes. Il faut les deux : chacune seule laisse une fenêtre.
1. **Amorce, avant de lancer la minuterie** (v6, juste avant l. 185) : si `date ≥ DEP` et que le marqueur est absent, poser `t06-depense-epuisee` (« épuisement constaté au démarrage »).
   - La minuterie saute alors C08 et attend `t06-detruire`.
   - Tous les chemins qui suivent mènent à `detruire` : premier démarrage (« démarrage après l'heure de dépense épuisée »), second démarrage (C08 / C-V3-2) et run interrompu (`refus`). Le `sommeil` n'est atteint que si `date < DEP`.
   - Effet de bord à déclarer : un run interrompu redémarré après l'épuisement suit la branche « dépense épuisée » (consignation, puis destruction, sans les 180 s du refus). Le résultat est le même, la destruction ; seul le message change.
2. **Minuterie, branche C08** (v6, l. 96) : après `consigner`, n'envoyer `PUT stopped` que si `t06-detruire` est absent. Sinon, sortir de la boucle vers la destruction (`raison="ordre de l'amorce"`).
   - Cela fait primer la destruction dans toute concurrence restante, par exemple si l'amorce demande la destruction pendant la consignation C08 d'un run en cours.

**Essais (R5)**, dans le style de `test_minuterie_depense_epuisee_puis_echeance_consignent_et_poussent` (faux `curl` qui journalise méthode et corps) :
- **Cas sain 1, minuterie** : DEP dans le passé, marqueur absent, `t06-consigner.sh` factice qui dort 2 s puis pose `t06-detruire` (comme l'amorce le ferait). Attendu : **aucun `PUT stopped`**, un `DELETE` envoyé, et « instance … détruite » au journal.
- **Artefact 1** : même scénario contre la minuterie actuelle (v6), où l'on attend `PUT stopped` puis aucun `DELETE`. C'est l'essai rouge qui montre le défaut ; il passe au vert avec le correctif 2.
- **Cas sain 2, amorce** (essai local, une minuterie factice qui relève l'état du marqueur à son lancement) : second démarrage après une fin normale, avec DEP passé et sans marqueur. Attendu : le marqueur existe **avant** le lancement de la minuterie, puis la destruction est demandée.
- **Artefact 2** : DEP dans le futur. Le marqueur n'est **pas** posé, et le second démarrage finit en `sommeil`. Cela garde le cas 1 de C13.
- **Mutations** : retrait du test de `t06-detruire` avant `PUT` ; retrait de la pose anticipée du marqueur. Chacune doit être tuée par l'essai correspondant.

## Corrections proposées pour la version suivante (amorce v7, lanceur v9, `session_v8`)
1. C08 : les deux correctifs ci-dessus, avec leurs essais et mutations.
2. `instance_seule` : un objet sans `id` ni `instances` est **illisible**, et non introuvable. Le motif `404` doit être un mot entier ou être retiré, au profit de « not found » ou « no such instance ». Essais :
   - objet d'erreur → illisible ;
   - texte d'erreur 500 citant un identifiant qui contient « 404 » → illisible ;
   - liste vide et objet d'erreur trois fois → `ARRET inventaire`, jamais `ARRET mort`.
3. `PIPESTATUS[1]` de `masquer` : ALERTE, et jamais de copie vidée en silence.
4. `creation` et `apres-creation` : inventaires masqués avant écriture.
5. `set -u`, l. 239 : code 2 et message, au lieu de 127.
6. Garde CUDA : `math.isfinite`.
7. Banc : un passage complet unique du fichier final, plus les mutations manquantes (point 2).
8. Compte d'essais du rapport : 439 et non 460, ou bien expliquer l'écart.
