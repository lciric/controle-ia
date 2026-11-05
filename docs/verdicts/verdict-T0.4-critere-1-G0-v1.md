# Verdict R13 — T0.4, validation du harnais sur modèle réel — run A `20261005-102042-validation-reelle` — critère 1 de la porte G0 — v1

**Verdict.** Le critère 1 de G0 est **non concluant**. La preuve n'est pas acquise, et la logique du harnais n'est pas réfutée non plus.
La ligne gelée qui s'applique est « P2 : écart ≤ 1e-2, diffus ». Sa lecture : « non concluant : précision probable (noyau, réglage), pas logique ».
L'écart maximal vaut 1,2665e-4 pour un seuil de 1e-4. Il est diffus : 1,2665e-4 dans le contexte, 9,8217e-5 dans la zone générée (rapport 1,29). P0, P1 et P3 sont conformes. P4 à P8 ne sont pas atteints. P9 n'est pas déclenché en logique.

---

## 0. En-tête

**Qui je suis.**
- Je suis le juge neuf de R13, en contexte vierge.
- Je ne suis ni l'auteur du préenregistrement, ni celui de l'analyse, ni celui du code. Je n'ai vu aucune des conversations qui les ont produits.
- Transparence : je tourne dans la même session et sur le même modèle (Claude Opus 5.5) que l'auteur et les cinq contre-lecteurs. Seul mon contexte est neuf. Un biais commun reste donc possible.
- Date : 2026-10-05 (UTC).

**Ce que je juge.** Je lis le run A d'après les critères gelés de `prereg/T0.4-validation-modele-reel-v1.md`, et seulement d'après eux. J'en tire le verdict du critère 1 de G0 : « Harnais validé : déterminisme, équivalence d'activations, gardes testées ».

**Dépôt lu.**
- `/home/user/controle-ia`, branche `main`, HEAD `e77cfed44f0dfc0c2487c478d900e7b164e28dbb`, arbre propre.
- Je n'y ai rien modifié. J'ai travaillé sur un clone (`git clone --no-hardlinks`) dans mon espace.
- Contrôle final : `git --no-optional-locks status` est vide, et aucun fichier du dépôt n'est plus récent que mon clone.

**Fichiers lus et empreintes vérifiées.** Chaque sha256 a été recalculé. « Compagnon » veut dire égal au `.sha256`. « Chaîne » veut dire contrôlé par `verifier_resultat` : résultat intact, manifeste intact, rattachement par empreinte.

```
Règles et documents qui font foi
18fac81371503475d58e0d07a6da03e06ad7f1e203e5a510aefe052d8692ae64  CLAUDE.md (non scellé ; lu à HEAD)
3d0589c80fe97b134b193a797881395ec710966867c47ca9e87506c187cb8c96  prereg/T0.4-validation-modele-reel-v1.md (compagnon ; empreinte attendue ; inchangé depuis 6cf7f20)
155e8149f065e620c8669d27829e356ebee9725972a198fce4fd7e9d32829add  docs/procedures/validation-T0.4-modele-reel-v1.md (compagnon)
e8a596c35f4f5e57c102f247cd39feed7debed8860b47ed2cb12d9bbcd7eb634  docs/procedures/validation-T0.4-modele-reel-v2.md (compagnon)
5188c13c8f52746dcb5ba5aa52c6df0671eb9618411a6950299d080658eb526d  docs/procedures/surveiller-instance-t04-v1.sh (compagnon)
9261932a11f29e8643175bc6e150d5455067f58a3cb1e57dca99e02cb17aa3b2  docs/brief-claude-code-programme-complet-v2.md (sha256sums-lancement-v2 : OK ; égal à la citation)
2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c  docs/programme-controle-ia-v2.md (idem)
16d71febf1491780ab1230ed1fb8e4d8b1bec47fbed202e0ef26ca666def04c2  livrables/premier-rendu-v1/devis-v1.md (égal à la citation)

Résultats du run : compagnon et chaîne conformes pour chacun (diag/… = diag/20261005-102042-validation-reelle)
0fd394347184b9236e41ae4e41a59c90898be8deab6b349cc9cd27b406560697  runs/20261005-102042-validation-reelle/manifeste.json
4eb2d92069e270631bf3e4d25345b44191cbe419d71a4f06725659c32846aeed  diag/…/arret.json
30b3d9706cff8a723871105bac1bc1a46d131f2868f71e89a6f528bd08ba2b68  diag/…/tests-instance.json
d884086902dfecd6741ede6b571980947c29a4bd1e07fda1a0014fb6fcf8091b  diag/…/environnement-python.json
7dc785755634a5f9466b557953811adca24fb7bc57dcbfbcc5fbec940bfcba7f  diag/…/logique-episode-0-trajectoire.json
1b67ad9571e9aa350843af7bef8422778919b71ab51b293265a005b9575f7125  diag/…/logique-episode-1-trajectoire.json
84e374e3117e9c89a541548e5ae0aeba0fba36a4ac195509b5754d362ebf45d6  diag/…/logique-episode-2-trajectoire.json
93885946065920ed34e6436c0498b1a9e24d21101da28ad12692bb56e03f037c  diag/…/logique-episode-3-trajectoire.json
8c4bcea6f442cd0091151600160a9e9e121aad41e1f68c4022676b7a5c0250f2  diag/…/logique-episode-4-trajectoire.json
ade81170b22e5f1d154a53dfb94c8b6c9514817d06f76aed880facb3274a51fe  diag/…/logique-episode-5-trajectoire.json
f4c5de5c57003f742973a1fecd22e10ad4db702b525a300870f93b482ab701c5  diag/…/logique-episode-6-trajectoire.json
cd8973d5e931643af0ebed3d77d9921f99813fdaa8980b7816f7feadac275ef4  diag/…/logique-episode-7-trajectoire.json

Traces : sha256sum -c empreintes.sha256 conforme dans chaque dossier
e0764df4de9bd1e2b9e1f9afa5845c7f1c6ac2fa12bf3502f99d5e791f5d9f2f  traces/t04-20261005-102856-G431/empreintes.sha256 (5 fichiers ; run-A.json et tests.err vides sur disque, et scellés vides : e3b0c442…)
1f6449ba1330956af09dd2c1b9a90e68b7dfd773775429847f44d91ee123b718  traces/t04-instance-54298522-20261005-103247/empreintes.sha256 (3 fichiers)
75eaa6562dab658403339d882f69448aaa1a7d4158e4c85dd4a677d4b2d0a0df  traces/t04-instance-54183350-20261004-181301/empreintes.sha256 (lancement 1)
998660efa7138f8ecad28c2ef4d033f183bf66e62155c40a14f3a3049dec605b  traces/t04-instance-54285455-20261005-083202/empreintes.sha256 (lancement 2)

Code au commit cité 3a7b5e0 (git show <commit>:<chemin> | sha256sum)
4d6ba9c873a4b32fdecd7d25909ed3baaf906686830a2992aa8d44ae53c33b8b  src/controle_ia/harnais/validation_reelle.py
33a6bf960621cc9a4cd085ed6c4a3591f11462d8ceb4a26f33af58b2b1a41a84  src/controle_ia/harnais/episode.py
3ebc18df1197d5d050c9e836a8516231ec786479624df3486b681e5494d995af  src/controle_ia/harnais/activations.py
e8624dfeaf1e4f168534c83a457bfa28ac0ddf8211dfcbfabb19e9b07636d4f3  src/controle_ia/harnais/modeles.py
98dbfa9b13578946c4d731c4bb1cfcfb85b9fd0cacdfd56a786042c93e6ef6b4  src/controle_ia/harnais/formats.py
1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d  src/controle_ia/manifeste.py
33730961ed76b2e173684ebdc3750e10721d2b677f755776146a0c75d70e8b88  scripts/validation_t04_instance.sh (égal à la citation)
76d3621c7aed28dd4e840c34107c8fe8257afc026854cfd6c47d97774ca203cd  scripts/amorce_instance_t04.sh (égal à la citation)

Registres, pour le contexte (non scellés ; lus à HEAD)
76410799a2998e07e7939826ea6fbb436c4d105317526510c41197c697d89997  registres/decisions.md (R-031 à R-040, N-009, N-010)
551cd43812c4094b92805bb874ef930d225d206273c24e2748c66bcddf1a246e  registres/etat.md
36eb13de61456369628708f67aee16784da53b057215a464d1617442cf56d3f4  registres/depenses.md
a68b9a309b1cb19e0a8c36ecb465b2fe0ebe77fe607c765a58a60c1195acb938  registres/arrets.md
a367db6b6bc517147ecd3dfb9604eb1459ea6810ead0dd08970e348cdd45a24a  registres/go.md
```

En plus : `python -m controle_ia.scellement verifier-arbre .` sur mon clone répond « arbre intact ».

**Méthode.**
1. J'ai vérifié les empreintes et la chaîne de rattachement (ci-dessus).
2. Conformité : j'ai comparé les commits par `git diff`. J'ai comparé la configuration du manifeste à `CONFIG_REELLE`, importé depuis le code du commit cité. J'ai recalculé l'empreinte de configuration et les 518 graines.
3. J'ai recalculé moi-même, sur processeur, P2, P3, P9 et la couverture. Source : les profils par action de `arret.json` (40 actions × 3 couches). Je n'ai pas recopié `lecture_partielle` : je l'ai comparée ensuite.
4. J'ai recalculé le plan des lots depuis les huit trajectoires scellées : longueur de contexte, remplissage, ligne finie avant les autres, passes de décodage, positions capturées, comparaisons décalées.
5. J'ai rejoué `lire` (code du commit cité) sur le résumé partiel. C'est un contrôle de cohérence seulement : la table prime.
6. J'ai relancé la suite de tests du commit cité, sur processeur, dans un clone séparé : `178 passed`. Ses fichiers temporaires vont dans le dossier temporaire du système, hors du dépôt.
7. Aucun calcul sur carte graphique. Aucun téléchargement. Aucun contact externe. Aucune poussée.

**Limites.**
- Les activations de la phase de logique ne sont jamais écrites sur disque : c'est un choix du code. Je recalcule donc depuis les profils consignés (médiane, quantile 0,99, maximum, écarts nuls, par zone), pas depuis les écarts par jeton. Les positions des maxima restent inconnues.
- Les empreintes publiées des fichiers du modèle ne figurent pas dans le dépôt. Leur conformité repose sur la garde exécutée sur l'instance.
- Trois réglages consignés sont des constantes écrites par le code, pas des relectures : format TF32, réductions en précision réduite, mode déterministe (section 4.1).
- Un scellé prouve qu'un fichier n'a pas changé depuis son écriture. Il ne prouve pas que le calcul était juste.

---

## 1. Intégrité et conformité

| point | constat | statut |
|---|---|---|
| Empreintes | Les 12 résultats du run sont conformes à leur compagnon et rattachés au manifeste `0fd39434…`. `arret.json` cite ce manifeste. Les traces sont conformes. L'arbre est intact. | conforme |
| Provenance | Résultats et traces viennent des commits de l'instance `a0dd78b` puis `eaf0352` (auteur « instance de calcul (T0.4) », 10:28:56 UTC). Le parent de `a0dd78b` est `6cf7f20` : l'instance a tourné sur le commit de scellement. Rien n'a changé depuis sur `main` (`git diff` vide). | conforme |
| Commit | Le manifeste cite `6cf7f2072f479b5d6dcc13696e6258531fd3e22d`, commit de scellement du préenregistrement. Il ne diffère du code cité `3a7b5e0523864f386c7ef528b663dbae83e046dd` que dans les dossiers documentaires et les sorties. Le résumé partiel porte `commit_cite` = `3a7b5e0…` : la garde de l'arbre gelé a passé sur l'instance. Les scripts de l'instance ont les empreintes citées. | conforme |
| Révision | `config.revision` = `0e9e39f249a16976918f6564b8830bc894c89659`, la révision citée. | conforme |
| Entropie | Les 518 graines portent l'entropie citée `70063659890082353632224480608012444681`. Recalculées par `graines(taches(config), entropie)`, elles sont identiques. | conforme |
| Préenregistrement | Le manifeste cite `prereg/T0.4-validation-modele-reel-v1.md`, `3d0589c8…6c96`. `decisif` vrai, `depot_propre` vrai, aucune réserve. | conforme |
| Configuration | `config` = `CONFIG_REELLE` du commit cité, plus la révision, à l'identique. Empreinte recalculée `5628f36e52447f3e2bd2f45e10d62d9927fbf3df445c836c1946a25217025558` = celle du manifeste. | conforme |
| Paramètres | Aucun changement : configuration, révision, entropie, code, scripts et préenregistrement sont ceux qui sont cités. | conforme |
| Versions | torch 2.14.1 (+cu130), transformers 5.18.0, tokenizers 0.23.2, safetensors 0.8.0, huggingface_hub 1.33.0, numpy 2.4.6, scipy 1.17.1, matplotlib 3.11.2 : ce sont les versions figées. 67 distributions sont scellées. | conforme |
| Machine | Carte A100-SXM4-80GB, pilote 580.159.03, CUDA 13.0. Offre 29019328 : vérifiée, en centre de données, à la demande, fiabilité 0,9986, 129 Go de mémoire vive (registre des dépenses). Mémoire de la carte 79,25 Gio. Mémoire vive effective 259,5 Go. | conforme |
| Lancements 1 et 2 | Instances 54183350 et 54285455 : 43 et 10 échecs « clonage impossible » (refus 403). Aucune ligne de tests ni de run. Un seul run `validation-reelle` existe. | aucun run ; R1 intact |
| Chronologie | Tests 10:20:42 ; manifeste 10:20:44 ; arrêt 10:28:56 (491 s) ; poussée 10:29:17 ; fin de l'amorce, code 1. Puis 15 relances du conteneur, toutes refusées par la garde R12 (« dossiers d'un essai précédent présents »). | cohérente |
| Run B | Non lancé : le script d'instance gelé s'arrête après l'arrêt de A (`consigner_arret "run A"; exit 1`). | conforme au plan |

---

## 2. Prédictions P0 à P9

Sources : `diag/20261005-102042-validation-reelle/arret.json` (`partiel`), `tests-instance.json`, les huit trajectoires, et les traces. Mon recalcul égale le bilan du code sur chaque agrégat : écart maximal, maxima par zone, couverture, contrôle négatif, écarts nuls. `lire`, rejouée, rend exactement la `lecture_partielle` consignée. Il n'y a donc aucun désaccord entre la table et le code à trancher.

| id | issue observée | lecture | justification |
|---|---|---|---|
| P0 | Dernière ligne « 178 passed in 33.77s » (`tests-instance.json`, égale à `traces/t04-20261005-102856-G431/tests.txt`). Sortie d'erreur de pytest vide. | **conforme** | Forme exacte gelée ; 178 est le nombre gelé. Recompté sur processeur au commit cité : 178 réussis. |
| P1 | Garde de format passée (144 jetons, 3 tours). Ouverture avec « Today Date: 26 Jul 2024 ». 10 fichiers du modèle « conformes » (4 poids par sha256, 6 par identifiant git). Carte 79,25 Gio ≥ 75. Mémoire vive 259,5 Go ≥ 64. | **conforme** | Toutes ces gardes ont passé avant la génération. Réserve : les empreintes publiées ne sont vérifiées que par l'instance. |
| P2 | Écart maximal 1,2665e-4 > 1e-4 (épisode 1, action (0,9), couche 23, dans le contexte). Maximum du contexte 1,2665e-4. Maximum de la zone générée 9,8217e-5 (épisode 1, action (0,3), couche 15). 4 actions sur 40 dépassent le seuil : toutes à la couche 23, toutes dans l'épisode 1, toutes avec leur maximum dans le contexte. | **non concluant : précision probable** | Règle « diffus » recalculée : 1,2665e-4 ≤ 1e-2 ; 1,2665e-4 ≥ 1e-5 et 9,8217e-5 ≥ 1e-5 ; rapport 1,29 ≤ 3. Couverture complète : 29 actions remplies à gauche, 30 finies avant les autres, 1 984 positions générées, lignes 1 et 6 (aucune en tête du lot). |
| P3 | 40 actions comparables sur 40 ; 40 passent (100 %). Minimum des maxima décalés : 1,0965. Au moins 11 comparaisons décalées par action. Toutes les positions décalées dépassent le seuil, aux 3 couches. | **conforme** | ≥ 95 % des actions comparables, et ≥ 10 actions comparables. |
| P4 | Phase de production non jouée. | **non atteint** | Arrêt en phase de logique. |
| P5 | Idem. | **non atteint** | Idem. |
| P6 | Rejeu du lot 0 dans le processus (phase de production) non joué. | **non atteint** | Idem. |
| P7 | Run B non lancé. | **non atteint** | Le script d'instance s'arrête après A. |
| P8 | Stockage et relecture (phase de production) non joués. | **non atteint** | Arrêt en phase de logique. |
| P9 | Logique : 0 écart nul sur 1 984 positions générées, à chacune des 3 couches. Production : non jouée. | **non déclenché en logique** (conforme pour cette phase) ; **non atteint en production** | Il y a des écarts non nuls dans la zone générée de la seule phase jouée. |

**Détail de P2.**
- Maxima par couche, contexte puis zone générée : couche 7, 2,45e-5 et 1,73e-5 ; couche 15, 9,02e-5 et 9,82e-5 ; couche 23, 1,27e-4 et 4,40e-5.
- La règle « diffus » tient aussi couche par couche : rapports 1,41 ; 1,09 ; 2,88.
- Médiane des médianes par action (couches 7, 15, 23) : contexte 5,2e-6, 5,9e-6, 5,1e-6 ; zone générée 4,7e-6, 4,3e-6, 3,6e-6.
- Actions au-dessus de 1e-5 : 29, 37 et 38 sur 40 (couches 7, 15, 23). À la couche 23 : 14 au-dessus de 5e-5, 4 au-dessus de 1e-4.
- Les 4 fautes : (0,9) 1,2665e-4 ; (1,7), (1,8), (1,9) 1,0720e-4 chacune (même valeur au bit près).
- Domaine observé : contexte jusqu'à 1 184 jetons, 101 jetons générés relus, lot de 8.

---

## 3. Ligne de la table gelée qui s'applique

La ligne, telle qu'elle est scellée :

> | P2 : écart ≤ 1e-2, diffus (maxima du contexte et de la zone générée tous deux ≥ 1e-5 et dans un rapport ≤ 3) | non concluant : précision probable (noyau, réglage), pas logique | diagnostic du noyau et des réglages consignés ; nœud ; aucune révision à la hausse du seuil de logique, ni sur le repère de précision ni sur un maximum observé, sans contrôle positif (défaut D1 injecté sur le modèle réel, vu au seuil révisé) |

**Suite, mot pour mot :** « diagnostic du noyau et des réglages consignés ; nœud ; aucune révision à la hausse du seuil de logique, ni sur le repère de précision ni sur un maximum observé, sans contrôle positif (défaut D1 injecté sur le modèle réel, vu au seuil révisé) ».

**Pourquoi les autres lignes ne s'appliquent pas.**
- Ligne de validation : elle exige P0 à P8 conformes, B lu et P7 conforme. Ce n'est pas le cas.
- « P2 contraire (écart > 1e-4), sauf la ligne suivante » : la ligne suivante est celle-ci, et l'exception joue.
- « P2 non concluant (couverture) » : la couverture est complète.
- Arrêts pour cause d'infrastructure, déterministe ou indéterminée : l'arrêt vient de la garde d'équivalence, nommée dans `arret.json` et dans `run-A.err`. Ce n'est aucune de ces causes. La table lit cet arrêt par P2 : « les issues contraires de P2 à P5 et P8 arrêtent le run ; elles se lisent dans `arret.json` ».
- P3 est conforme, P4 à P8 ne sont pas atteints, P9 n'est pas déclenché : aucune autre ligne ne joue.

**Rappels gelés qui encadrent cette suite.**
- Section « Seuil » : « Le seuil de logique ne se révise jamais à la hausse sans contrôle positif : ni sur le repère de précision demi/simple, qui ne mesure pas la logique, ni sur un maximum observé. Un contrôle positif, par exemple le défaut de décodage D1 injecté sur le modèle réel, doit rester vu au seuil révisé. »
- Liste d'arrêt : « Aucun relancement automatique. Aucun paramètre ne change sans nouvelle version du préenregistrement : tailles, seuils, lots, échantillons, couches, modèle, révision, entropie, délais. »

---

## 4. Audit de symétrie (R4)

Deux questions. L'échec pourrait-il venir d'un artefact (réglage, alignement, capture, conversion) plutôt que de l'arrondi ? Et, à l'inverse, l'étiquette « diffus » pourrait-elle masquer un défaut de logique ?

### 4.1 Réglages

| réglage | ce qui est consigné | nature de la valeur | ce que j'en tire |
|---|---|---|---|
| Format TF32 | « tf32 : false » | Constante écrite par `regler_determinisme` après `allow_tf32 = False` (produits matriciels et cuDNN). Aucune relecture. | Sur processeur, avec la même version de torch (2.14.1), cette ancienne interface bascule la nouvelle sur « ieee », c'est-à-dire la simple précision stricte. Par défaut, le format TF32 est déjà coupé pour les produits matriciels (précision « highest »). Forte présomption, mais pas une mesure du run. |
| Réductions en précision réduite | « false » | Constante. | Elles ne touchent que les produits en demi-précision. Sans effet sur la phase de logique, qui est en simple précision. |
| Noyau d'attention « math » | « noyau_attention : math » | Valeur de configuration. Le code enveloppe la génération et la passe unique dans le même contexte « math ». Aucune relecture du noyau employé. | Non vérifiable sur les données. |
| Mode déterministe | « deterministe : true » | Constante. | Il agit sur la reproductibilité (P6, P7), pas sur l'équivalence entre deux chemins de calcul. |
| Type des poids | « torch.float32 » | Relu sur le premier paramètre ; la garde `exiger_type_des_poids` a contrôlé tous les paramètres. | Vérifié. La conversion bfloat16 → simple précision est exacte par construction ; son identité avec un chargement direct n'est testée que sur modèle jouet. |
| Espace de travail de cuBLAS | « :4096:8 » | Relu dans l'environnement. | Vérifié. |
| Implémentation d'attention | « sdpa » | Relue sur le modèle chargé. | Vérifié. |

La table demande un « diagnostic du noyau et des réglages consignés ». Les données consignées ne suffisent pas à le faire : trois réglages sont des intentions écrites, pas des états relus. C'est une limite de l'instrument, pas un écart au préenregistrement.

### 4.2 Alignement : positions, épisodes, couches

- **Plan des lots.** Je l'ai recalculé depuis les huit trajectoires scellées. Pour les 40 actions, il égale le résumé : longueur de contexte, remplissage, ligne finie avant les autres, positions capturées (contexte, plus le minimum des passes de décodage et des jetons générés), comparaisons décalées. Aucun écart.
- **Trajectoires.** Leurs 8 empreintes recalculées égalent celles du résumé.
- **Transcriptions.** Chaque empan d'action est exact. Elles ne font que s'allonger. Chaque action finit par un jeton d'arrêt (128001, 128008 ou 128009) ou à 256 jetons. Aucun jeton d'arrêt à l'intérieur d'une action.
- **Couches.** Les couches 7, 15 et 23 sont lues des deux côtés : même liste, mêmes crochets.
- **Épisodes.** Les épisodes 1 et 6 sont les lignes 1 et 6 du lot unique de 8.
- **Preuve directe.** Deux contextes entiers coïncident au bit près, aux 3 couches :
  - épisode 1, action (0,0) : 68 positions nulles sur 68 ;
  - épisode 6, action (0,1) : 140 positions nulles sur 140, sur une ligne **remplie à gauche** de 22 jetons. Au pas 1, les contextes diffèrent d'un épisode à l'autre. La bonne ligne, les bonnes positions, le bon masque et la bonne couche sont donc lus pour cette action.
- **Zone générée.** Ses maxima restent ≤ 9,8e-5 partout. Or un jeton décalé donne au moins 1,0965 (contrôle négatif, P3). Aucun désalignement de jeton n'est compatible avec les données.

### 4.3 Capture et conversion

- Simple précision de bout en bout. La copie de la carte vers le processeur ne change pas le type. L'écart se calcule en double précision.
- Sondes d'audit, pour les 40 actions : les deux tableaux sont distincts en mémoire, et une perturbation d'une unité au dernier rang est vue.
- Les 208 écarts nuls par couche sont exactement les deux contextes ci-dessus. Ce n'est pas un tableau comparé à lui-même : les tableaux sont distincts, et la zone générée de ces deux actions a des écarts non nuls (jusqu'à 5,8e-6 et 9,2e-6).

### 4.4 Forme de l'écart

Les données consignées vont dans le sens d'un arrondi qui dépend de la forme des calculs, et non d'un défaut de logique. C'est une hypothèse décrite, non prouvée.

- **Même génération, deux passes uniques.** Au pas 0, les 8 épisodes reçoivent le même contexte de 68 jetons, dans le même appel. Sauf dépendance au rang de la ligne, les lignes 1 et 6 rendent donc les mêmes activations. Or la passe avant unique de l'épisode 1 (transcription de 788 jetons) redonne ce contexte au bit près, et celle de l'épisode 6 (1 181 jetons) ne le redonne pas : médiane de 4e-6 à 5e-6. Deux passes avant ordinaires sur le même préfixe divergent donc selon leur longueur totale. Ce calcul ne met en jeu ni remplissage, ni positions explicites, ni cache.
- **Indifférence au remplissage.** Les maxima de contexte se répètent au bit près d'une action à la suivante, pour un même agent. Épisode 1, actions (0,4) à (0,8), couche 15 : 3,861125e-5, avec des remplissages de 349 à 1 337 jetons. Actions (1,7) à (1,9), couche 23 : 1,0719506e-4, sans remplissage. De même dans l'épisode 6. La génération rend donc, à une position donnée, la même valeur quel que soit le remplissage. Un défaut de remplissage, de masque ou de position la ferait varier.
- **Tailles des produits matriciels.** Les deux identités au bit près surviennent pour 544 lignes de matrice (8 × 68) contre 788, et pour 1 296 (8 × 162) contre 1 181. Pour d'autres couples, l'écart n'est pas nul : 544 contre 1 181, 1 296 contre 788, 1 560 contre 1 253. Un choix du noyau de produit matriciel selon la taille l'expliquerait. Je ne peux pas le vérifier.
- **Ordre de grandeur.** Les médianes par action valent environ 5e-6 (contexte) et 4e-6 (zone générée). Elles restent stables de la couche 7 à la couche 23, dans la fourchette attendue par le préenregistrement (1e-7 à 1e-5). Seules les queues dépassent.
- **Profil par zones.** Le maximum est dans le contexte, pas dans la zone générée. La règle « diffus » tient couche par couche. Pour les 4 actions fautives, le contexte domine (rapports de 4,4 à 27,6). Un défaut de décodage donnerait l'inverse : sur modèle jouet, le défaut D1 se concentre dans la zone générée.

### 4.5 Ce qui n'est pas vérifiable sans nouveau calcul

- L'état effectif du format TF32 et le noyau d'attention réellement employé pendant le run.
- Le mécanisme exact (quel noyau, quelle opération) et les positions des maxima. Les activations de la logique ne sont gardées nulle part : ni dans le dépôt, ni sur le disque de l'instance.
- L'absence d'un défaut de logique plus petit que ce plancher d'arrondi. L'ampleur du défaut D1 sur le modèle réel est inconnue ; sur modèle jouet, elle allait de 3,3e-4 à 6,0e-4. Seul le contrôle positif exigé par la table le dirait.
- La reproductibilité de l'écart lui-même : le rejeu dans le processus (P6) et le run B (P7) n'ont pas eu lieu.
- Les empreintes publiées des fichiers du modèle : l'instance les a contrôlées, pas moi.
- La production, le stockage, la relecture et le repère de précision (P4, P5, P8) : non joués.

### 4.6 Conclusion de l'audit

- Je ne trouve aucun artefact d'alignement, de capture ou de conversion.
- Sur sept réglages, trois ne sont pas relus. Le diagnostic que demande la table reste à faire.
- La lecture « précision probable » est robuste : elle tient zone par zone et couche par couche, et plusieurs indices indépendants l'appuient. Elle reste une probabilité ; la table ne la change pas en preuve.
- Rien de « trop propre » : P9 n'est pas déclenché, et les écarts nuls du contexte sont expliqués.

---

## 5. Verdict du critère 1 de G0

**Non concluant.** La preuve du critère 1 (« Harnais validé : déterminisme, équivalence d'activations, gardes testées ») n'est pas acquise sur le modèle réel. P2 est non concluant (précision probable) ; P4 à P8 ne sont pas atteints ; le run B n'a pas eu lieu.
La logique du harnais n'est pas réfutée pour autant.

---

## 6. Ce qui reste ouvert (nœud N-010)

**Ce que la table exige pour aller plus loin.**
- Une seule ligne prouve le critère : « P0 à P8 conformes dans A, P9 non déclenché ; lecture de B égale à celle de A ; P7 conforme ». Il faut donc un run A et un run B complets.
- Pour l'issue présente, la suite gelée : diagnostic du noyau et des réglages consignés ; nœud ; aucune révision à la hausse du seuil de logique sans contrôle positif.
- Tout changement de paramètre passe par une version 2 du préenregistrement (liste d'arrêt). Elle est contre-lue (R2) et scellée (R1). Toute dépense de calcul demande un GO sur devis. Le verdict revient ensuite à un juge neuf (R13).
- La table ne prévoit pas de relancement à l'identique pour cette issue : elle le réserve aux causes d'infrastructure.

**Voies que la table laisse ouvertes.** Je les décris sans les trancher : elles relèvent de Lazar.
1. **Diagnostic du noyau et des réglages.** Relire l'état effectif (format TF32, noyau d'attention). Éprouver l'hypothèse de forme, par exemple par des passes uniques de longueurs différentes sur un même préfixe. Ce diagnostic demande la carte graphique, donc un devis et un GO.
2. **Révision du seuil de logique par une version 2, seulement avec un contrôle positif** : défaut D1 injecté sur le modèle réel et vu au seuil révisé. Jamais sur le repère de précision. Jamais sur le maximum observé (1,27e-4).
3. **Autre changement du régime de la logique** (précision, formes, échantillon…). Cette ligne ne le nomme pas. Il n'est permis que par une version 2.

**Voies fermées par la table.** Relever le seuil sans contrôle positif. Fonder un seuil sur le repère de précision ou sur un maximum observé. Relancer à l'identique. Changer un paramètre sans version 2. Franchir G0 sans verdict scellé et sans GO.

**Fait utile au reste du nœud N-009 (destruction des instances).** Pour cette lecture, rien n'est requis du disque de l'instance 54298522. Tous les résultats sont poussés. La phase de logique n'écrit aucun tableau, et la production n'a pas eu lieu. La décision reste à Lazar.

---

## Annexe — fichiers de travail du juge

Ils sont dans mon espace, hors du dépôt : `/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/verdict-t04-1/`.

```
af2804f82a39b4ad81d5a6d8a02b1cc368184ee7c9bbd67cd79a8eab4cd1af79  recalcul_t04.py (intégrité, conformité, P0 à P3, P9, alignement, lecture rejouée)
1ab8b38658754849e7d486760aa245830ea7476bc785e3bef28ad6f8f9271a37  recalcul_t04-sortie.json (sa sortie)
3e4045511fe0049f007cd376872f2dd6c0185b6412acd2a3d37481065f8729ed  tableau_actions.py (tableau par action : longueurs, remplissage, maxima, médianes, écarts nuls)
d6010191f1d7fe9dca9ec7dfffc8099caa738dc34a36ccbbb6d6e0b12309f6db  formes.py (tailles des produits matriciels et maxima partagés ; descriptif)
```

Interpréteur : `/home/user/controle-ia/.venv/bin/python` (Python 3.11.15, torch 2.14.1+cu130, transformers 5.18.0, numpy 2.4.6), lancé avec `PYTHONDONTWRITEBYTECODE=1` pour ne rien écrire sous le dépôt. Code importé depuis une extraction du commit cité (`git archive 3a7b5e0`).
