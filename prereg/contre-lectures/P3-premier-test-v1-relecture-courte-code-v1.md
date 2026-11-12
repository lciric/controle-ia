## Relecture courte du traitement de P3, angle code (relecteur C)

**Jugement d'ensemble : scellable après traitement.** Un constat majeur, quatre mineurs, sept pour information, aucun bloquant. Les deux suites de tests passent.

### Empreintes vérifiées
Toutes sont égales à ce qui est cité.
- **Candidat 1** : `8070b640…dd0`, égale à l'empreinte attendue.
- **Brouillon 4** : `94e5ff12…`. Il n'a pas de sceau compagnon (voir RC-12).
- **Contre-lecture texte-code** : `98d7201b…`. **Contre-lecture chaîne** : `57060da8…`. Leurs sceaux sont justes.
- **Commit du code** : `03cb53804e0b98fe671b62ebf5ef2d819741e282`, égal à `git rev-parse 03cb538`.
- **Fichiers au commit `03cb538`**, inchangés jusqu'à la tête `00075fc` (`git diff --stat 03cb538 HEAD -- src tests scripts` est vide) :
  - amorce `0bfaeaa6…` ;
  - script de l'instance `2bfc6939…` ;
  - tests des gardes `cf4ab7b8…`, 20 tests collectés ;
  - `traitement-CH-v1.md` `ad1d88d2…`.
- **Configuration candidat 3** : fichier `702303e9…` (égal à son sceau), empreinte canonique `2f343a6f…` (égale à la citation).
- **Consignes candidat 2** : `a68468fe…`, avec six blocs.
- **Arbre** : `verifier-arbre .` répond « arbre intact ».
- **Tests**, dans un clone au commit `03cb538` :
  - fichiers de P3 et `test_script_p3.py` : « 90 passed in 307.08s » ;
  - suite complète : « 893 passed in 1633.22s », égal aux tests attendus.

### Constats, du plus grave au moins grave

| id | fichier et ligne | ce qui est écrit | ce qui est juste, et pourquoi | gravité | correction proposée |
|---|---|---|---|---|---|
| RC-01 | `lecture.py` l. 235, 296-299, 351-352, 366 ; candidat l. 343-345 | Un jeu avec fuite avérée est « non interprétable ». Le texte n'en tire la conséquence que pour saboteur contre honnête. | Le code applique deux règles. `issue()` écarte un jeu saboteur contre témoin non interprétable (`ok`, l. 366). `P3-P4.conforme` (l. 235) et T3 (l. 297-299) ne l'écartent pas. Essai sur les tables du test : avec une fuite de longueur propre à saboteur contre mention, ce jeu est marqué non interprétable, T3 est « établi » et la ligne dit « intention établie (T1 à T4) ». Avec une fuite propre à saboteur contre témoin, `conforme` vaut vrai mais la ligne dit « non concluant pour la validité ». Le texte gelé ne tranche pas : la lecture de H-P3c a deux chemins possibles (R1). | majeur | Écrire au texte qu'un jeu non interprétable ne compte jamais pour établir une prédiction (saboteur contre témoin, saboteur contre mention), mais compte contre elle (témoin ou mention contre honnête). Aligner `conforme` et T3 sur `issue()`, avec deux tests. Si la lecture d'une hypothèse change, c'est un nœud de Lazar. |
| RC-02 | `tests/test_script_p3.py` l. 278-311 (l. 310) ; amorce l. 47-50 | Le test du plafond dit que l'amorce pousse ses traces « avec les données légères ». | Le faux `timeout` laisse le script de P3 finir normalement, et ce script a déjà poussé les données (`p3_instance.sh` l. 275-281). L'assertion l. 310 est donc toujours vraie. Mutation dans un clone : l. 47-50 vidées, le test passe encore. Si l'on retire la poussée, il échoue, comme le dit R-215. Le code, lui, est juste. Dans mon essai, le script est tué après l'écriture des données et l'amorce rend 137. Le commit « plafond » contient alors les textes, les scores par jeton, les scores, les sondes légères et le sceau du fichier complet, sans le fichier complet. | mineur | Faire tuer le script par le faux `timeout` avant sa propre poussée (codes 124 et 137). Vérifier `git show --name-only` du dernier commit. Sinon, nuancer le candidat l. 453-454. |
| RC-03 | candidat l. 194 et 443 | TC-18 : « cas couvert par un test jouet ». | Ce test n'existe pas. Tous les appels à `plancher_apparie` dans les tests ont plus de jetons que de dimensions : sondes figées 60 jetons pour 6, notation environ 130 pour 12, `test_sondes_v0.py` pour 12, run jouet en largeur 32. Le commit `8bddc6b` n'ajoute aucun test de ce cas. Le cas tient pourtant : à 12 jetons pour 64 dimensions, la factorisation réussit et le résidu hors de l'espace des jetons vaut 2,8·10⁻⁴ pour une norme d'environ 37. | mineur | Ajouter ce test jouet, ou retirer la phrase du texte. |
| RC-04 | `lecture.py` l. 80-99 ; `tests/test_premier_test_ia_lecture.py` l. 204-229 | Lecture décisive : « code au commit cité » ; « chacune testée sur cas sain et artefact ». | La lecture n'appelle pas `exiger_code_importe_sous`. Tous les autres points d'entrée décisifs l'appellent à côté de `exiger_code_cite` : `run.py` l. 293-294, `lire_pilote.py` l. 476, `noter_pilote_a.py` l. 198-199. Le paquet peut donc être importé d'une autre copie que le dépôt contrôlé. Preuve : le cas sain du test réussit sur un dépôt jetable alors que le code vient du vrai dépôt, ce que la vraie garde refuserait (`test_lire_pilote.py` l. 632-641). Deux artefacts manquent aussi : un run décisif hors du mode réel, et un même chemin avec une autre empreinte de préenregistrement. | mineur | Appeler la garde d'import dans `exiger_lecture_sous_prereg`. La tester sur le modèle de `test_lire_pilote.py`. Ajouter les deux artefacts. |
| RC-05 | `lecture.py` l. 226-228, 154-155, 356-359 ; candidat l. 386 | Plus de 1 % de tirages dégénérés : « arrêt de la lecture concernée, écrit tel quel ». | La lecture décisive P3-P3 passe aussi par `descriptif`. Son échec est lu « non au-dessus ». Essai avec un échec simulé : la ligne est le nul « aucune sonde générique… », sans réserve. C'est un repli (R5), et la table gelée n'a pas de ligne pour ce cas. Il est presque inaccessible, car chaque bloc porte les deux conditions. | mineur | Ajouter une ligne gelée « P3-P3 non lue, échec écrit : nœud », calculée par `issue()`, avec un test. |
| RC-06 | `entrainement.py` l. 92-95 ; `familles.py` l. 226 | Perte non finie : arrêt (époque citée). | Seules les époques 0 et 299 sont journalisées. Une perte non finie se propage jusqu'à la dernière, donc la garde tient. Mais le message donne le rang dans le journal : un essai avec une perte non finie à l'époque 299 affiche « époque 1 ». | pour information | Citer `x["epoque"]` dans le message. |
| RC-07 | `run.py` l. 231-234 ; tests des gardes l. 376-378 | « Aucun contrôle de Mahalanobis sur les premiers lots : arrêt. » | La garde n'est évaluée qu'après les 30 lots. Le run joue donc environ 2,5 heures de carte, puis s'arrête sans écrire de scores. Aucun test ne force un lot sans action notable. | pour information | Évaluer la garde après le lot `lots_mahalanobis_identite − 1`, et ajouter ce test. |
| RC-08 | `run.py` l. 15-17 ; `lecture.py` l. 11-15 | La docstring de `run.py` dit « au moins un contrôle par lot … exigés ». Celle de `lecture.py` ne liste que T1 à T3. | Le code (l. 229-231) et le texte (l. 174) consignent un lot sans action notable, sans arrêt. T4 existe bien (l. 300-313). | pour information | Corriger les deux docstrings. |
| RC-09 | `run.py` l. 139-145 | « min(32, cœurs disponibles du processus) » | `os.sched_getaffinity` ne voit pas un quota de processeur (`cpu.max`). Si l'offre applique ses cœurs par quota, 32 fils peuvent dépasser les cœurs réellement alloués (le risque déjà nommé par TC-12), et le nombre consigné le surestime. La garde de mémoire lit déjà ces plafonds (`plafonds_cgroup`). | pour information | Borner aussi par `cpu.max`, et consigner les deux nombres. |
| RC-10 | `run.py` l. 365-381 | Budget de l'entraînement dépassé : « arrêt avant les épisodes ». | Le budget n'est jamais relu après les planchers. Cette remarque de TC-12 n'est pas traitée. Un dépassement au dernier plancher passe donc aux épisodes, qui restent bornés par `duree_max_s`. | pour information | Appeler `_echeance` après chaque plancher, ou écrire la limite dans le texte. |
| RC-11 | `conditions.py` l. 119-125 ; `propositions.py` l. 131-138 | Borne du champ `COST`. | Les bornes prennent la première clé, même si sa valeur est vide. `lire_action` prend la première non vide. Dans ce cas rare, T2 ne lit pas le même champ que le coût déclaré. | pour information | Sauter les occurrences vides, ou écrire la règle. |
| RC-12 | candidat l. 109 ; brouillon 4 ; `run.py` l. 317-318 ; `statistiques.py` l. 229-230 | divers | (a) Au candidat l. 109, un crochet ouvrant reste sans fermant ; il vient de `construire_candidat1.py`. (b) Le brouillon 4 est le seul des quatre brouillons sans `.sha256` (R6). (c) Deux gardes neuves n'ont pas d'artefact : le refus d'écraser les textes (inaccessible, le dossier est créé avec `exist_ok=False`) et la garde de forme de `detection_stratifiee`. | pour information | Retirer le crochet, sceller le brouillon 4, ajouter ou documenter ces deux artefacts. |

### Scripts de l'instance changés au commit `03cb538`
Je n'y trouve aucun défaut de comportement.
- **Délais** : les bornes s'emboîtent. 16 200 s font 270 minutes, sous le délai externe de 300 minutes, sous le plafond de l'amorce de 360 minutes ; la surveillance coupe à 22 200 s, soit 370 minutes.
- **Contrôle par la chaîne** : `300m`, `360m` et `22200` sont liés au texte par `controles_avant_depense_p3_v1.sh` l. 238-249.
- **Marge** : la suite complète dure environ 27 minutes. Dans le pire cas, l'ensemble prend environ 345 minutes, sous le plafond de 360.
- **Données brutes** : elles sont poussées sur le chemin normal et sur le chemin d'arrêt, chacun testé ; sur le chemin du plafond, seul mon essai le montre (RC-02).
- **Copie publique** : la copie expurgée retire `donnees/**` (`depot_expurge.py`), donc les textes des actions n'y vont jamais.

### Gardes listées par TC-11
Chaque garde a un test qui la déclenche, avec un cas sain. Les messages attendus sont précis, donc c'est bien la garde visée qui s'arrête. Les tests cités sont dans le fichier des gardes, sauf indication.

| garde de TC-11 | test qui la déclenche |
|---|---|
| réponse imposée | `test_reponse_forcee…` |
| message utilisateur (quatre cas) | `test_message_utilisateur…` |
| format de dialogue exigé | `test_format_de_dialogue_exige` |
| extraction (empan hors des positions, activation non finie, échéance) | `test_extraire…` |
| échéance et budget | `test_echeance…`, `test_budget…` |
| couches et sondes principales de `jouer_p3` | `test_jouer_p3_gardes_d_entree` |
| citation absente | `test_citations_p3…`, plus `test_premier_test_ia_run.py` l. 141-157 |
| format de l'agent en mode réel | `test_format_de_l_agent_en_mode_reel` |
| configuration (mode inconnu, durées) | `test_configuration_de_p3…` |
| écriture des sondes figées | `test_ecrire_sondes…` |
| relecture des sondes (c'est l'index qui est cassé, plus le sceau) | `test_lire_sondes…` |
| notation (attention sans requête, score non fini) | `test_notation_…` |
| source de la lecture (arrêt présent, empreinte du résumé) | `test_charger_source_arret_present`, `test_charger_source_empreinte_du_resume_autre` |
| autre garde repropagée | `test_effet_ou_non_calculable…` |
| faits génériques | `test_charger_faits…` |
| découpage | `test_decouper…` |
| perte non finie | `test_premier_test_ia_entrainement.py::test_perte_non_finie_arrete` |

Les points que TC-11 disait non testés ont maintenant leur test :
- mêmes graines d'une condition à l'autre : `test_memes_graines…` ;
- plan de la garde d'identité : `test_plan_de_la_garde_d_identite` ;
- ligne « non concluant pour la validité » : test de lecture l. 146-148.

Les nouvelles gardes « scores par jeton » et « Mahalanobis » sont testées dans `test_premier_test_ia_run.py` l. 181-199.

### Statut des constats d'origine (partie code)
| constat | statut | preuve |
|---|---|---|
| TC-01 | traité | `lecture.py` l. 241-267 et 332-374 ; tests `test_audit_R4…`, `test_autres_lignes…`. Voir RC-01 et RC-05. |
| TC-02 | traité en partie | Quatre gardes l. 80-99, testées l. 204-229 ; manquent la garde d'import et deux artefacts (RC-04). |
| TC-03 | traité | l. 54-55 et 256-263 (miroir, plancher au-dessus de 0,70, placebo) ; tests l. 154-168. |
| TC-04 | traité | `issue()` l. 363-373 ; test l. 146-148. |
| TC-05 | traité | Mentions (`conditions.py` l. 34-36 et 106-107), textes gardés (`run.py` l. 210 et 431), aires sans mention, corrélation, longueur (`lecture.py` l. 242, 265, 316-321), T1 à T4 (l. 268-315) ; tests `test_mesures_nouvelles` et les trois tests d'intention. |
| TC-06, TC-13, TC-16, TC-17 | sans objet pour le code | — |
| TC-07 | traité | `lecture.py` l. 342-350 ; test `test_reserves…`. |
| TC-08 | traité | `conditions.py` l. 32 et 79-89 ; `lecture.py` l. 210-212 ; test `test_mesures_nouvelles`. |
| TC-09 | traité | `conditions.py` l. 105-106, motifs égaux à ceux de `lire_action` ; test `test_mesures_nouvelles`. |
| TC-10 | traité | `run.py` l. 193-201 et 231-234 ; deux tests. Voir RC-07 et RC-08. |
| TC-11 | traité | Voir le tableau des gardes ci-dessus et RC-06. |
| TC-12 | traité en partie | Nombre de fils effectif consigné (`run.py` l. 361-363 et 405-406, `test_fils_effectifs`) ; budget après les planchers non traité (RC-10). |
| TC-14 | traité | `descriptif` l. 146-151 ; test l. 146-148. Voir RC-05. |
| TC-15 | traité | `charger_source` l. 106-112 ; réserve l. 340-341 ; effectifs l. 216 ; tests l. 169-170 et 259-260. |
| TC-18 | traité en partie | Le texte est écrit, le test jouet manque (RC-03). |
| TC-19 | sans objet pour le code | Scripts conformes : `p3_instance.sh` l. 152-158 ; test l. 147-151. |
| TC-20 | traité | (a) `conditions.py` l. 29-30 ; (b) `run.py` l. 297-304 et son test ; (c) l. 102-103 et son test ; (d) `__init__.py` ; (g) `notation.py` l. 59-61. Les points (e), (f) et (h) relèvent du texte et de la chaîne. |

### Ce que je n'ai pas pu vérifier
- Rien qui demande la carte ou le modèle : le vrai tokeniseur de Llama 3.1, les durées réelles, la mémoire, la poussée vers GitHub. Pour le coût du décodage cumulé des bornes, je n'ai qu'une estimation avec un tokeniseur de substitution entraîné sur place : environ 10 ms par action, environ 25 s pour 2 400 actions.
- Comment Vast.ai alloue les cœurs, par affinité ou par quota (utile pour RC-09).
- Les constats CH, les scripts de mesure de TC-06 et TC-13, et le texte hors des champs liés au code.
- La probabilité réelle des cas de RC-01 et RC-05 : mes essais portent sur des tables synthétiques.

### Fichiers de travail
Tous sont dans `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p3-relecture-courte/code/`. Aucun fichier du dépôt n'a été modifié ; `git status` reste propre.
- Essais de lecture (RC-01, RC-05) : `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p3-relecture-courte/code/essais/essai_lecture.py`
- Essai du plafond, script tué (RC-02) : `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p3-relecture-courte/code/essai-plafond/tests/test_relecture_plafond_tue.py`
- Sortie des tests de P3 : `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p3-relecture-courte/code/tests-p3.txt`
- Sortie de la suite complète : `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p3-relecture-courte/code/suite-complete.txt`
