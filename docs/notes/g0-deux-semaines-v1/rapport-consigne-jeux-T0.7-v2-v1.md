# Rapport de rédaction — consigne v2 des jeux synthétiques de T0.7 (mode « coût ») — v1

- Rédacteur neuf (Claude Fable 5.1, sous-agent de la session principale), qui n'a écrit ni le brouillon 1 de la consigne,
  ni les brouillons de T0.7, ni T0.6, ni P3, ni le code, et qui n'a écrit **aucune paire**. Travail du 2026-11-05, de
  16:34 à 16:50 UTC environ pour la lecture et la consigne (heures relevées par `date -u`), rapport écrit ensuite.
- Produit : `docs/procedures/consigne-jeux-synthetiques-T0.7-v2.md` (non scellée, non contre-lue ; empreinte dans la
  réponse finale, aucun `.sha256` écrit). Aucun commit, aucune poussée, aucun fichier existant modifié, aucun réseau,
  aucune dépense, aucun résultat lu.

## 1. Ce que j'ai lu (compagnons vérifiés quand ils existent)

| pièce | empreinte | usage |
|---|---|---|
| `brouillons/T0.7-sondes-v0-v1-brouillon6.md` | `29f0ab43…` (compagnon vérifié) | source de chaque exigence (renvois « [b6 l. N] ») : table avant/après l. 35 et 50, pièces l. 110-114, tâches l. 117-124, DS-1 l. 134-151, hypothèses l. 168-195, prédictions l. 209-218, métrique l. 226-268, repli l. 288-291, plan d'analyse l. 300-347, liste d'arrêt l. 407-426, stockage l. 454-459, dépense l. 466-467, reste l. 638-642, contre-lecture l. 663-674, marqueurs l. 691-692 |
| `brouillons/T0.7-jeux-synthetiques-consigne-v1-brouillon1.md` | `e38bc16b…` (pas de compagnon ; empreinte recalculée, égale à celle que cite le brouillon 6 l. 111) | la consigne v1 **existe**, en brouillon 1 du 6 octobre 2026, non scellée, non contre-lue |
| `brouillons/T0.7-concepts-sans-lien-consigne-v1-brouillon1.md` | `acc7bdfb…` | précédent de forme (JSON Lines, listes gardées pour le script, contre-vérification sur 10 %) |
| `brouillons/T0.6-organismes-v0-v1-brouillon4.md` | `8df90b8b…` (compagnon vérifié) | gabarit des actions et champ de coût (l. 145, 207-210, 284-291) ; lecteur du coût neuf |
| `docs/decisions/proposition-P-015-T0.6-T0.8-mode-cout-v1.md` | `6e74c6cb…` | section « Sonde du domaine (E3) » l. 131-145 |
| `docs/notes/brainstorm-suite-P3-v1/reponses/reponses.md` | `2eaef7f4…` | A6 corrigée l. 136-151 ; B4 l. 197-213 |
| `docs/notes/revue-comment-detecter/synthese-comment-detecter-v7.md` | non recalculée (note, non opposable) | colonne E3, l. 393-399 : « nombres équilibrés ; incitation chez les positifs et les négatifs ; actions sans nombre avant le champ » ; piège « gros nombre, style, régime d'incitation » |
| `registres/decisions.md` | — | P-015 (l. 392), R-321 (défaut (b)) ; A6 et E3 n'y sont pas des décisions à part : ils vivent dans P-015 et dans `reponses.md` |
| `prereg/P3-premier-test-i-a-v1.md` | `d975e981…` | lecteur du coût l. 165-170 ; T1 à T4 l. 237-253 |
| `prereg/P3-consignes-v1.md` | `a68468fe…` | place et forme des textes privés (l. 31-34), contenu du témoin (l. 47-56, 79) : lu comme **texte à ne pas recopier**, donné au script, jamais à l'écrivain |
| `src/controle_ia/environnements/propositions.py` | — | consigne honnête, format d'action, assemblage du message système et de l'observation (l. 27-48, 164-168, 239-270) |
| `src/controle_ia/sondes/` (`familles.py`, `evaluation.py`, `temoins.py`) | — | signatures seulement ; le script de la consigne n'en importe rien |
| `docs/sources/donnees-T0.7/provenance-donnees-sondes-v1.md` | `36585c7d…` | ordre de grandeur (306 paires), gabarit de dialogue rendu par le harnais |
| `docs/procedures/T0.5-extraction-v1.md` | — | cibles jamais montrées (l. 68) ; règle des 8 mots (l. 116) |
| `donnees/20261007-082440-t05-extraction/taches-entrainement.json` | `8d20a698…` (égale au brouillon 6) | **structure seule** (clés : `identifiant`, `questions`, `classification`, `cibles`, `couts_rapportes`, `empreintes`, `tentative`), lue par un script qui n'affiche aucun contenu ; aucun énoncé ni cible lu |

Non trouvé : aucune consigne v1 **scellée** sous `docs/procedures/` ni `docs/notes/` ; le seul texte est le brouillon 1.
Aucun jeu de P3 propre aux concepts neufs n'existe : les jeux de P3 sont les deux jeux publics (tromperie, enjeux) de la
provenance, et ils ne sont pas touchés. Aucun tokeniseur de Llama-3.1-8B-Instruct n'est présent sur la machine
(recherche de `tokenizer.json` sur le disque) : d'où la règle de longueur en mots et caractères, et la mesure en jetons
reportée sur l'instance (consigne, section 2).

## 2. Ce que la v2 change par rapport au brouillon 1

| sujet | brouillon 1 (6 octobre) | v2 | fondement |
|---|---|---|---|
| jeux | deux (dissimulation, intention en trois modes à parts égales) | **trois fichiers** : J-D dissimulation (inchangé) ; J-C domaine, mode « coût » ; J-A les deux autres modes, pour T7-P6 seul | b6 l. 35, 50, 300-310, 344-347 |
| tailles | 10 paires par tâche et par jeu | 10 (J-D), 10 (J-C), 5 + 5 (J-A) : proposition du brouillon 6 reprise comme valeur de la consigne | b6 l. 311-313 |
| nombres | aucune règle | **N1** ligne `COST:` identique dans les deux membres (J-C et J-A) ; **N2** ≥ 6 valeurs par tâche, rapport ≥ 20 ; **N3** aucun nombre de coût avant le champ, écart de groupes de chiffres ≤ 2 | b6 l. 143-144, 305-306 ; revue v7 l. 398-399 |
| incitation | absente | annexe B, 8 situations, identiques dans les deux membres, rotation exacte (40 fois chacune) ; jamais une consigne | b6 l. 303-304 ; P-015 l. 140 |
| texte avant le champ | « mêmes champs », rien de plus | **D1** distance d'édition en mots ≥ 0,30 avant `COST:` ; paire qui ne diffère qu'au champ refusée | b6 l. 140-141, 306-307 |
| contexte | « même contexte » | assemblé **par le script** (message système et observation du premier pas, place des textes privés comme P3) ; l'écrivain n'écrit aucun contexte | propositions.py ; P3-consignes l. 31-34 |
| banque de dissimulation | « fixée au scellement », non écrite | **écrite** (annexe A, 20 entrées + 4 de réserve, 4 cadrages, bloc + rappel), contrôlée (aucun mot du coût, des contrôles, de la direction, de la qualité, des minuscules ; 0 suite de 8 mots commune avec P3, vérifié) | v1 § 1.1, § 2 ; b6 l. 177-178 |
| mots interdits | « liste fixée au scellement » | annexe C écrite ; appliquée à **toutes** les réponses des trois jeux ; familles nommées à l'écrivain, liste au script | b6 l. 308, 640 |
| longueurs | 15 % en jetons | 15 % en **mots et en caractères** (script, sans réseau) ; jetons remesurés sur l'instance, écart = arrêt (R5) | b6 l. 308 ; T0.6 l. 284 |
| recopie | témoin et organismes | règle des **8 mots consécutifs** (T0.5) contre les textes privés de P3, les textes d'actions de P3, les épisodes de T0.6 s'ils existent, et l'énoncé de la tâche | consigne du rédacteur ; T0.5 l. 116 |
| fuite lexicale | absente | contrôle dur (terme à fréquence documentaire ≥ 0,25 dans une étiquette et ≤ 0,05 dans l'autre) + aire d'un sac de mots en « une tâche laissée de côté », réserve si ≥ 0,90 | consigne du rédacteur |
| validation | « schéma, longueurs, mots, textes, réponses identiques » | script nommé (`scripts/verifier_jeux_synthetiques_t07_v2.py`), tests R5 (cas sain et artefact par garde), journal versé, dix contrôles durs listés | b6 l. 313 ; R5 |
| échec | tâche écartée au second échec | **paire** retirée au second échec ; tâche gardée si ≥ 8 paires (J-D, J-C) ou ≥ 4 par mode (J-A) | précision de la v2 |
| contre-vérification | 32 paires, « majorité » | 32 par jeu (16 par mode pour J-A), tirage `SeedSequence` à clés nommées, `COST` masqué, seuils 23/32 et 12/16, indice de surface confirmé = jeu refait | b6 l. 313-314 ; R9 |
| format | `task_id`, `pair_id`, `label`, `context`, `response` | une ligne par **membre**, clés en français, `membre` A/B tiré par graine, `position_cost` écrit pour l'empan « avant le champ », `cout_declare` | b6 l. 318-319, 323-324, 345-346 |
| interdits de l'écrivain | programme, organismes, pilote, cibles | ajoutés explicitement : **sondes figées, tout score**, `sondes/`, `donnees/` hors énoncés, P3-consignes, épisodes de T0.6 ; aucun modèle lancé | consigne du rédacteur ; b6 l. 168-172 |
| rapport de l'écrivain | absent | gabarit (section 12) | consigne du rédacteur |
| scellement | « empreintes ; `donnees/` hors dépôt » | dossier `donnees/t07-jeux-synthetiques-v2/`, chaque fichier `.sha256`, `provenance-v2.md`, marqueurs remplis avant toute extraction | b6 l. 314-315, 454-455, 691-692 |

Gardé du brouillon 1 : la structure de J-D (recette de 2502.03407 : même réponse, contextes différents) ; les deux modes
de J-A ; la réserve de style (lecture hors politique) ; « jamais pour choisir une sonde sur les organismes ».

## 3. Points qu'un contre-lecteur doit regarder

1. **Règle N1 (même nombre dans la paire)** : c'est ma lecture de « même nombre honnête ici, gonflé là » (b6 l. 143) et de
   « chaque valeur apparaît autant de fois comme honnête que comme gonflée » (l. 305-306). Une autre lecture existe : des
   paires à nombres différents (gonflé > honnête) équilibrés **entre** paires d'une tâche. Je l'ai écartée : elle ne peut
   pas être exacte aux extrêmes de la grille, et elle laisse le nombre porter l'étiquette à l'intérieur d'une paire ; mais
   le contre-lecteur doit dire si N1 rend le « gonflé » trop dépendant du jugement de l'écrivain (le gonflement n'est
   lisible que par rapport au plan décrit, section 5.1).
2. **Rang de décision** : les tailles, N1 à N3, D1 (0,30), les seuils de fuite (0,25 / 0,05 ; 0,90), les seuils de la
   contre-vérification (23/32, 12/16), les bornes de longueur (90 à 260 mots) sont des **choix de cette consigne**, de
   rang routine ou « périmètre interne » (hiérarchie de décision) ; ils ne touchent aucune hypothèse ni aucun critère de G0.
   Un contre-lecteur peut les trouver trop stricts (D1 et N3 ensemble peuvent gêner l'écrivain) ou trop lâches (0,90).
3. **Longueur en jetons reportée sur l'instance** : un écart trouvé là impose une version neuve du jeu après scellement,
   donc avant la lecture (nœud si la lecture a commencé). Alternative : exiger le tokeniseur localement (copie scellée,
   `79e3e522…`) avant d'écrire ; je ne l'ai pas imposée, faute de savoir s'il est disponible sans réseau.
4. **Place de l'incitation et du bloc** : tous deux en fin de message système (comme les textes privés de P3) ; le rappel
   de J-D avant « Your action: ». Un contre-lecteur doit vérifier que `Environnement.consigne_privee` et `observation`
   rendent bien cet ordre avec `instructions_cachees` et `indications_privees`, et que la chaîne de T0.7 peut reproduire
   ces contextes à l'octet (contrôle 3 du script).
5. **Compatibilité de la réponse de J-D avec l'instruction** : la réponse commune doit respecter l'instruction sans la
   citer. Risque : l'écrivain écrit des réponses « neutres » qui respectent toutes les instructions (sans parenthèses,
   sans listes, sans « novel »…) et la banque n'exerce aucune contrainte réelle ; ce n'est pas un défaut pour la sonde (la
   réponse est la même des deux côtés), mais le contre-lecteur peut préférer des instructions plus saillantes.
6. **Annexe B** : les huit situations doivent rester des situations ; l'entrée I08 (« panels read COST as a signal of
   ambition ») est la plus proche d'une incitation explicite ; à relire.
7. **Mots interdits** : « honest », « margin », « redundant », « waste » peuvent frapper des usages légitimes ; la consigne
   n'admet aucune exception (réécriture) : à confirmer ou assouplir.
8. **Script** : il importe `lire_action` et `heures_declarees` du module gelé `environnements/propositions.py` (lecture,
   pas modification) ; vérifier que c'est permis par R12 et que le lecteur du coût neuf de T0.6 n'a pas à être préféré
   ici (les jeux imposent un entier seul : les deux lecteurs lisent la même chose).
9. **Chemin critique** : l'écriture de 960 paires par un sous-agent, deux rondes de script et une contre-vérification
   tiennent-elles avant la lecture de T0.7 (après la course de T0.6 et le verdict de P3-bis) ? Le brouillon 6 place cela
   « hors du chemin critique de la course » (l. 642) ; la consigne ne date rien.
10. **Renvois de lignes** : chaque « [b6 l. N] » a été relu sur le brouillon 6 à l'empreinte `29f0ab43…` ; une version
    neuve de T0.7 déplacera ces lignes : la consigne scellée devra citer l'empreinte du texte qu'elle vise.

## 4. Écarts de lecture possibles de A6 (3) (« aucune lecture par champ dans T0.7 »)

A6 corrigée (3) retire toute lecture par champ de T0.7 (`reponses.md` l. 142). Le brouillon 6 la lit comme portant sur
**les épisodes d'organisme** (l. 194-195, 228-229, 415 : « ni « champ COST seul », ni « jetons qui précèdent le champ »,
sur les épisodes d'organisme ») et fixe en même temps, par DS-1 (a), un **empan d'entraînement avant le champ** sur les
jeux génériques (l. 134, 323-324) et le même empan pour le témoin lexical (l. 267-268). Trois lectures sont possibles :

- **(i) stricte** : tout empan défini par un champ, où que ce soit, est une « lecture par champ » ; alors DS-1 (a) est en
  écart avec A6 (3), et la sonde du domaine devrait être apprise sur l'action entière. La consigne reste utilisable sous
  cette lecture : N1 (nombre identique dans la paire) garantit que l'action entière ne porte l'étiquette ni par le nombre
  ni par le champ ; `position_cost` peut être ignoré. Mais la paire perd alors sa raison d'être « avant le champ ».
- **(ii) celle du brouillon 6** (que la consigne suit) : A6 (3) interdit de **lire** les organismes par champ (diagnostic
  par position, laissé à P3-bis, E1, E2) ; restreindre l'**entraînement** générique aux jetons avant le champ n'est pas une
  lecture d'organisme. La production lit l'action entière. C'est cohérent avec la revue v7 (l. 399 : « lecture avant le
  chiffre ») et avec P-015 (l. 141 : « lecture avant le champ COST »), qui parlent de la **sonde du domaine**, pas des
  contrôles de P3.
- **(iii) intermédiaire** : l'entraînement avant le champ est permis, mais la **validation générique** (choix de la sonde
  principale, l. 325-330) devrait se faire sur l'action entière, pour choisir la sonde telle qu'elle sera lue. Le
  brouillon 6 dit « apprise et validée sur les jetons qui précèdent le champ » (l. 134) ; la consigne fournit
  `position_cost` et n'impose rien : c'est au préenregistrement de trancher ; un contre-lecteur de T0.7 devrait le noter.

Conséquence pour les jeux : quelle que soit la lecture retenue, les jeux sont écrits pour que **ni le nombre ni le champ ne
portent l'étiquette** (N1, N3, D1) et pour que le texte avant le champ porte l'intention ; ils ne préjugent pas de
l'empan. Un changement d'empan après une lecture d'organisme resterait un écart au préenregistrement (nœud), pas une
affaire de la consigne.

## 5. Ce que je n'ai pas fait, et pourquoi

- Aucune paire, aucun exemple de paire (la consigne du rédacteur l'interdit ; des exemples écrits ici entreraient dans le
  style de l'écrivain). Les annexes A et B sont des banques prévues par le brouillon 1 (« consigne scellée avec la banque
  d'instructions et la liste de mots interdits »), pas des paires.
- Aucun script : la consigne le spécifie (section 8) ; il relève d'un développeur neuf ou de la session, avec tests R5.
- Aucune lecture de `donnees/` au-delà des clés du fichier des tâches ; aucune lecture de résultat de P3 ni d'activation.
- Aucun `.sha256`, aucun commit : empreintes des deux fichiers dans la réponse finale, scellement par la session après
  contre-lecture R2.
