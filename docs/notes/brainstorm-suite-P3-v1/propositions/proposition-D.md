# Proposition D — suite de P3 — angle « avocat du diable » — v1

- Proposeur D, sous-agent neuf, 2026-10-20 (UTC). Protocole fermé de Lazar (R-203 (2)) : proposition indépendante, écrite
  sans voir les autres proposeurs. Rien ne change dans le programme sans sa décision.
- Lu : `prereg/P3-premier-test-i-a-v1.md` ; `prereg/P3-addendum-lecture-complementaire-v1.md` ;
  `diag/20261020-075740-p3-lecture/lecture-p3.json` (en entier) ; `diag/20261019-230011-p3-reel/sondes-figees.json` ; noms et
  formes des tableaux de `donnees/20261019-230011-p3-reel/scores-p3.npz` et `sondes-figees-legeres.npz` (aucun texte) ;
  `docs/notes/P3-mesures-v2/puissance-p3-v1.txt` ; `docs/programme-controle-ia-v2.md` ; brief v2 (porte G0) ; P-007, P-011,
  P-013 ; `brouillons/programme-approfondi-ABC-v1.md` ; `brouillons/T0.6-organismes-v0-v1-brouillon1.md` ;
  `registres/etat.md` ; `registres/decisions.md` (R-192, R-202, R-203, N-024, R-246 à R-255) ; `registres/depenses.md` ;
  `prereg/contre-lectures/relecture-externe-gemini-P3-v1.md` ; `src/controle_ia/environnements/propositions.py`.
- Pas lu, volontairement : `prereg/P3-consignes-v1.md`, les textes d'action, toute clé ou jeton ; et la sortie de l'addendum
  (`diag/20261020-075849-addendum-p3/`), pour ne pas trancher d'avance entre les branches A, B et C.
- Sauf mention, chaque chiffre vient de `lecture-p3.json` (clé citée). Aucun n'est un verdict. Aucun chiffre de l'état de
  l'art n'est opposable ici (R7) ; le seul cité (D3) est marqué « à revérifier ».

Branches : (A) nul confirmé sans réserve ; (B) nul avec réserves (instrument, plancher, fuite) ; (C) instrument jugé en échec.

---

## 0. Deux thèses opposées, et ce qui coûterait cher

### Thèse 1 : le nul est un artefact. Quatre mécanismes, chacun avec un indice

| explication concurrente | indice dans le dépôt | option qui la teste |
|---|---|---|
| (a) le plancher absorbe le signal | plancher de la tromperie, quantile 0,95 : **0,572** sur le vrai jeu saboteur contre honnête (`jeux.tromperie-difference_moyennes-c15.saboteur-honnete.plancher_quantile`) ; **0,525** sous étiquettes permutées (`placebo.…plancher_quantile`) ; **0,517 à 0,528** dans le modèle de puissance (`puissance-p3-v1.txt`, section « détection »). La borne basse de la sonde (**0,531**) aurait passé ces deux derniers seuils. Maximum du plancher : 0,781 | D1, D3 |
| (b) effet trop petit pour la puissance | demi-largeur observée ≈ 0,044 (de 0,531 à 0,618), contre 0,024 à 0,037 prévues ; effet minimal détectable réel ≈ **0,615** pour la tromperie (0,572 + 0,044) et ≈ 0,58 pour les enjeux (0,536 + 0,044), contre « ≈ 0,57 à 0,58 » écrit (prereg l. 157 et l. 396) | D1, D4 |
| (c) sondes génériques mal choisies | validation de la tromperie au plafond : 9 sondes sur 15 à 1,0, sur 120 exemples (`sondes-figees.json`, `resultat.aires_validation.tromperie`, `resultat.effectifs.tromperie.validation`) ; la principale est donc élue par l'ordre de départage (prereg l. 309-310), pas par la validation. Enjeux appris sur des jetons du message utilisateur, lus sur des jetons de l'assistant (prereg l. 299-301) | D3 |
| (d) l'organisme gonfle sans intention lisible | chez le saboteur, actions qui gonflent contre actions qui ne gonflent pas : tromperie 0,463, enjeux 0,592, toutes deux sous le plancher (`intention.*.T1`) ; texte trompeur seulement dans le contexte : mention contre honnête 0,501 (tromperie) ; mais le **champ du coût** sépare à **0,914** contre 0,554 pour les jetons qui le précèdent (`intention.tromperie-….T2`) | D2, D6 |

### Thèse 2 : le nul est le résultat le plus important du programme

- L'organisme (i-a) est **flagrant**. Il gonfle d'un facteur ≈ 33 : P3-P1 = 1,52 en log10, [1,25 ; 1,80] (`P3-P1`), alors que
  la prédiction gelée disait « au plus ≈ 0,48 », soit un triplement (prereg l. 155).
- Le **coût déclaré seul** sépare le saboteur de l'honnête à **0,888**, du témoin à 0,929, de la mention à 0,934
  (`audit_R4.jeux[].cout_seul`).
- Les deux sondes génériques restent au niveau d'une direction aléatoire : tromperie 0,575 [0,531 ; 0,618], enjeux 0,525
  [0,481 ; 0,570] (`jeux.*.saboteur-honnete`).
- L'accumulation sur dix actions ne rattrape rien : rappel 0 à 1,7 % (tromperie) et 6,7 % (enjeux) au seuil des épisodes
  honnêtes (`P3-P5`).
- Si cela tient : une sonde générique ne voit pas, au niveau de l'action, un sabotage qu'une règle d'une ligne lit dans le
  texte. Sur ce régime, c'est l'opposé de H1 (programme l. 93).

### Ce qui coûterait cher, dans chaque sens (R4)

- **Voir un artefact là où il n'y en a pas** : chemins qui bifurquent (28 autres sondes déjà notées dans `scores-p3.npz`,
  autres couches, fenêtres, T4 promu au rang de preuve) ; budget et douze jours brûlés avant G0 ; promesse fausse à l'appel
  EA Funds du 21 octobre (R-203 (3)) ; crédibilité d'un programme fondé sur le préenregistrement. Le texte gelé l'interdit :
  « pas de seconde lecture sur d'autres sondes, couches ou jeux » (prereg l. 428).
- **Voir un résultat définitif là où il n'y en a pas** : abandonner l'accès aux activations, ou lire P3 comme « δ = 0 »
  (hypothèse pivot, programme l. 64), sur un test dont l'effet minimal détectable valait ≈ 0,62, avec un organisme flagrant
  et deux sondes élues sur une validation au plafond. P3 n'a ni test d'équivalence ni taille d'effet minimale d'intérêt.

---

## D1 — Dire ce que « non détecté à cette puissance » veut dire, avec les nombres observés

- **Branche** : toutes (A, B, C) ; surtout A et B.
- **Ce qu'elle tranche** : la phrase du rapport (effet minimal détectable réel, pas celui du plan) et l'entrée de puissance
  de T0.7 et du préenregistrement de G1 (critère 6 de G0). Rien sur le signe de P3.
- **Contenu** : une note scellée, faite d'arithmétique sur des nombres déjà écrits ; aucune donnée relue.
  1. Effet minimal détectable réel = quantile du plancher observé + demi-largeur observée : ≈ 0,615 (tromperie), ≈ 0,58
     (enjeux), contre ≈ 0,57 à 0,58 écrits (prereg l. 157, l. 396).
  2. Hausse du plancher due aux vraies étiquettes : + 0,047 en tromperie (0,572 contre placebo 0,525), + 0,012 en enjeux
     (0,536 contre 0,524). Lecture : des directions aléatoires tirées dans la covariance des jetons de faits séparent déjà
     le saboteur de l'honnête (maximum 0,781). La condition se voit dans le flux résiduel ; la direction « tromperie » n'y
     est pas privilégiée. Ce n'est pas un défaut du plancher : c'est sa fonction.
  3. Le modèle de puissance de T0.7 et de G1 doit partir d'un plancher mesuré sous de vraies étiquettes, pas de « sondes
     aléatoires sans lien avec la condition » (hypothèse écrite au prereg l. 396-397 ; `puissance-p3-v1.txt`).
  4. Pour H2 et G1 : à l'aire observée, la somme sur dix actions donne 1,7 % à 6,7 % de rappel (`P3-P5`, seuil = maximum
     des 60 épisodes honnêtes, TC-17). L'horizon nécessaire à G1, à un δ de cet ordre, se calcule avant de sceller G1.
- **Coût** : 0 USD ; processeur ; une demi-journée, plus une contre-lecture R2 par un sous-agent neuf.
- **Revendications touchées** : aucune changée. Lecture du critère 3 de G0 ; puissance de G1 (critère 6) ; H2.
- **Piège principal** : faire de la note un récit de « presque positif ». L'estimation ponctuelle de la tromperie (0,5748)
  dépasse d'un cheveu le quantile du plancher (0,5717) : sans valeur sous la règle gelée, qui lit la borne basse
  (prereg l. 272). La note ne nomme aucun jeu « proche ». Sauter D1 coûte : on rapporte un nul « à 0,57 » qui était un nul
  à 0,62 (nul surinterprété). Surinterpréter D1 coûte : on rouvre P3. Toute grandeur non écrite est un nœud (prereg
  l. 415-416) : la note reste descriptive et va à Lazar.

## D2 — Nombre ou intention : contre-épreuve 2 × 2 par réécriture forcée sur les textes gardés

- **Branche** : A et B. Pas C (si l'instrument est en échec, ses scores ne lisent rien).
- **Ce qu'elle tranche** : le signal du champ du coût (T2 : 0,914 contre 0,554) vient-il du **nombre écrit** (équivalent
  d'un lecteur de texte) ou du **contexte privé** (ce qu'une sonde d'intention devrait lire) ?
- **Contenu** :
  - Passe sans génération (réécriture forcée) sur les textes gardés. L'environnement est déterministe à journal donné
    (`src/controle_ia/environnements/propositions.py`, `rejouer` et `observation`, l. 193-269) : chaque contexte se
    reconstruit.
  - Les 24 sondes non Mahalanobis et les **400 directions de plancher** sont versées
    (`donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz`, 424 indices). Le plancher du seul champ du coût devient
    calculable ; l'addendum le déclare impossible faute de scores par jeton du plancher (addendum, A2 (d)).
  - Plan, sur les actions du saboteur : contexte {consigne et indication du saboteur ; du témoin, même longueur en jetons
    (prereg l. 333-338)} × nombre du champ `COST` {original ; remplacé par la médiane honnête de la même tâche}. Miroir sur
    les actions du témoin : nombre gonflé inséré. Le témoin, pas l'honnête, sert de contexte « sans intention » : il porte
    une consigne privée de même place et de même longueur.
  - Score : maximum sur le champ du coût et sur l'action entière, jamais la moyenne ni la médiane.
  - Garde d'identité : la case d'origine doit redonner `scores-p3.npz` à une tolérance fixée d'avance (R5 : cas sain et
    artefact).
  - Prédiction de la session, écrite contre le positif (R3) : effet du nombre > 0 ; effet du contexte, à nombre égal, non
    détecté.
  - C'est, en miniature, le plan 2 × 2 « rhétorique × intention » du papier C (EC.2, programme l. 195) : ce qui est écrit
    contre ce qui est voulu.
- **Coût** : aucune génération ; ≈ 2 heures de carte A100 au plus, mise en place et tests compris (suite de tests : 1 603 s,
  prereg l. 383-384) : ≈ 2 à 3 USD, estimation. Sous GO-2026-10-04-08 : cumul ≈ 67 USD au plus sur 150 (63,2 USD au
  18 octobre, plus ≈ 3,96 USD de P3, plus les disques ; `registres/depenses.md`) ; crédit 11,79 USD. Trois à quatre jours :
  préenregistrement, contre-lecture R2, chaîne reprise de P3, devis et GO de Lazar (dépense : nœud).
- **Revendications touchées** : H8 (ce que mesure la sonde) ; Tr (où lire : le champ ou l'action) ; H1 sur (i) (les
  activations portent-elles autre chose que le texte ?) ; prédiction de validité (programme l. 135).
- **Piège principal** : textes hors politique (le texte du saboteur n'a jamais été généré dans le contexte du témoin) et
  longueur du champ qui change avec le nombre de jetons du nombre (biais de longueur du maximum, constat G-01 de Gemini) :
  choisir des nombres de même nombre de jetons, sinon fenêtres de même longueur. Erreur sens « artefact » : se servir d'un
  effet de contexte pour relire P3, ou pour élire une fenêtre qu'on appliquerait aux mêmes épisodes. La ligne d'issue de P3
  ne change jamais ; une fenêtre retenue ne vaut que pour des épisodes neufs. Erreur sens « définitif » : conclure « la
  sonde lit le nombre » sans l'avoir montré.

## D3 — L'instrument voit-il quoi que ce soit ? Contrôle positif et confrontation du plancher

- **Branche** : C ; B si la réserve vise l'instrument (plancher, position du jeton dominant : A8 de l'addendum).
- **Ce qu'elle tranche** : la chaîne (données génériques → jetons de l'assistant → maximum → plancher apparié → intervalle
  par blocs) détecte-t-elle un concept certainement présent ? Si non, P3 parle de l'instrument, pas de l'organisme.
- **Contenu** : P3 n'a aucun contrôle positif de la chaîne des sondes. Le témoin sert à la validité (P3-P4), pas à prouver
  que l'instrument détecte. Trois pièces, préenregistrées avant toute lecture :
  1. Une sonde générique « titre en minuscules », apprise hors organisme (jeu de phrases écrit et scellé par un sous-agent
     neuf, comme pour P-013), lue sur témoin contre honnête. Le comportement est massif : 500 titres sans capitale sur 600
     chez le témoin, 4 chez l'honnête (`P3-P6`). Elle doit passer le plancher.
  2. Reproduction, par notre code, d'un résultat publié de models-under-pressure : aire moyenne 0,887 d'une sonde à
     attention sur Llama-3.1-8B (2506.10805v4, p. 24-25, selon `brouillons/programme-approfondi-ABC-v1.md` l. 27, brouillon
     non contre-lu : **à revérifier sur le PDF scellé avant tout préenregistrement**, R7).
  3. Confrontation de la recette du plancher au code du projet antérieur de Lazar, promise par le texte gelé
     (prereg l. 230-232, TC-16) et toujours attendue (`registres/etat.md`, « Ressources demandées à Lazar », l. 60-61).
  - Lecture : (1) échoue → instrument en échec, T0.7 ne part pas avec cette chaîne. (1) passe, (2) échoue → notre code
    d'entraînement est suspect. Les deux passent → le nul de P3 porte sur les concepts, pas sur la chaîne.
- **Coût** : (1) et (2) partagent la passe de D2 (+ 20 à 40 minutes de carte, ≈ 0,5 USD) ou ≈ 1,5 à 2 USD seuls,
  estimation ; (3) 0 USD, suspendu à un envoi de Lazar. Deux à trois jours.
- **Revendications touchées** : critère 3 de G0 (« une sonde qui ne le bat pas n'existe pas », programme l. 143) ; aucune
  hypothèse.
- **Piège principal** : un contrôle positif trop facile. Les minuscules sont un trait lexical : le passer prouve le
  transport du signal, pas la lecture d'un concept abstrait ; d'où la pièce (2). Erreur sens « artefact » : retoucher la
  recette du plancher ou l'agrégation après avoir vu P3, puis relire P3 avec : interdit, la recette est gelée
  (prereg l. 230) ; une recette neuve ne vaut que pour un test neuf. Erreur sens « définitif » : déclarer les sondes
  génériques inutiles alors que la chaîne n'a jamais été éprouvée sur un positif connu.

## D4 — Déplacer le test là où l'accès aux activations aurait une raison d'exister : un organisme diffus

- **Branche** : A surtout ; B si les réserves ne touchent pas l'instrument.
- **Ce qu'elle tranche** : sur un sabotage que le texte ne trahit pas, une sonde figée fait-elle mieux que le lecteur de
  coût ? C'est la question de H1. P3 ne la pose pas.
- **Contenu** :
  - (i-a) tel que lancé est flagrant (× 33 ; coût seul 0,888 à 0,934). La boîte noire y gagne d'avance. Un nul, ou un
    positif, de la sonde y dit peu de H1, qui porte sur le sabotage diffus sur tâches floues (programme l. 93).
  - Réécrire T0.6 dans le mode « coût », seule famille retenue par le verdict du pilote (prereg l. 58-59) ; le brouillon de
    T0.6 est encore en mode « affaiblir les contrôles » (`brouillons/T0.6-organismes-v0-v1-brouillon1.md` l. 28, l. 40).
  - Dose par la **proportion p** d'actions avec indication (p ∈ {0,25 ; 0,5 ; 1}, même brouillon l. 75), pas par
    l'intensité : la consigne « × 3 » a donné × 33.
  - Référence : le **témoin**, pas l'honnête. Toute consigne privée baisse le coût déclaré : témoin − 0,32
    [− 0,57 ; − 0,07] (`P3-P2`), mention − 0,32 [− 0,54 ; − 0,12] (`cout_mention`). Elle change aussi la forme du champ :
    honnête, 14 suffixes « k » et 13 intervalles ; saboteur, 0 et 0 (`P3-P6`).
  - Sondes : les deux principales de P3, figées telles quelles. Aucune nouvelle élection.
  - Critère principal, sur des épisodes neufs : sonde contre lecteur de coût, à coût déclaré égal (la forme de T4).
- **Coût** : ≈ 38 s par épisode au pilote (prereg l. 385) ; 300 à 400 épisodes ≈ 3,2 à 4,2 heures, plus la mise en place :
  ≈ 5 à 7 USD, estimation ; recharge du crédit probable. Cinq à sept jours. Sert aussi le critère 2 de G0 (dose-réponse).
- **Revendications touchées** : H1 ; lemme L (pivot δ > 0, programme l. 64) ; H2 ; critères 2 et 3 de G0.
- **Piège principal** : R3. La dose et la consigne ne se règlent jamais sur les sondes, seulement sur une cible boîte noire
  écrite d'avance (par exemple : aire du coût seul au plus 0,65 à la dose la plus faible). Second piège : la dose-réponse
  peut ne pas être monotone, puisque l'organisme ne suit pas le chiffre de sa consigne. Erreur sens « artefact » :
  promouvoir le T4 de P3 (tromperie 0,632 [0,556 ; 0,703], plancher 0,607 : non établi) en preuve ; il n'est qu'une raison
  de poser la question sur des données neuves. Erreur sens « définitif » : conclure contre H1 sans avoir testé le régime
  diffus. Calendrier peu compatible avec G0 au 1er novembre : à décider avec D5.

## D5 — Prendre le nul au sérieux : nœud anticipé sur G0 et sur ce qu'on peut en dire

- **Branche** : A ; B avec ses réserves écrites. Pas C (en C, rien ne se dit de l'organisme).
- **Ce qu'elle tranche** : que faire du critère 3 de G0, et que dire du résultat, avant le point de contrôle du 26 octobre
  (P-007) plutôt qu'après.
- **Contenu** : note de décision à Lazar, au format du dépôt. Constat : sur un organisme instruit et flagrant, deux sondes
  génériques ne battent pas une direction aléatoire, quand une règle d'une ligne sur le texte sépare à 0,89. Options :
  - (a) G0 au 1er novembre sans le critère 3 sur (i-a) ; M0 prolongé de deux semaines (P-007 (b)) pour D4 ;
  - (b) bras principal du critère 3 changé : sondes apprises sur une famille, évaluées sur l'autre (P-011 (b)) ; exige
    l'organisme (ii) ;
  - (c) la validité de construit (H8 ; critère de succès 4, programme l. 235) avancée comme livrable de la phase 0, avec
    P3 comme première pièce.
  - Pour l'appel du 21 octobre : une phrase conditionnelle par branche, du type « nul préenregistré, non détecté à cette
    puissance (effet minimal détectable ≈ 0,62), sur un organisme flagrant ». Jamais « l'accès aux activations échoue ».
- **Coût** : 0 USD ; une demi-journée ; décision de Lazar (critère de porte ou hypothèse : nœud).
- **Revendications touchées** : H1 ; L et T ; H8 ; critère 3 de G0 ; critère de succès 4.
- **Piège principal** : deux lectures abusives. (1) « δ ≈ 0, donc le lemme tombe », ou P3 lu comme appui au théorème
  négatif. Le théorème parle d'un sabotage qui préserve la marginale par construction ; ici la marginale ne bouge pas parce
  que l'instrument ne la voit pas, ou pas assez. La « seconde fermeture » du brouillon ABC (l. 15) exige un test
  d'équivalence que P3 n'a pas. (2) Généraliser depuis un modèle, un organisme, deux sondes génériques, une agrégation (R8 :
  zone vierge = question). Erreur sens « définitif » : changer une hypothèse sur ce seul test. Erreur sens « artefact » :
  attendre le 26 octobre sans rien proposer et laisser glisser G0 en silence.

## D6 — Lire ce que fait le saboteur avant de chercher où il « pense »

- **Branche** : toutes.
- **Ce qu'elle tranche** : le saboteur ment-il au champ du coût (nombre multiplié, même projet), ou élargit-il le projet
  puis le chiffre honnêtement ? Dans le second cas, il n'y a pas de mensonge à détecter au champ du coût, et T2 lit le
  nombre.
- **Contenu** :
  - Un sous-agent neuf, qui n'a pas vu `lecture-p3.json`, code un échantillon tiré par graine (R9) des actions gardées
    (saboteur, témoin, honnête, mention), selon une grille scellée d'avance : nombre multiplié à portée égale ; portée
    élargie ; unité changée ; coût justifié ; mention de la note. Descriptif, sans prédiction de signe.
  - Référence boîte noire de R-202 (3) (juge Claude sur les textes gardés) : elle devait être préenregistrée « sans
    lecture des résultats de P3 avant son scellement » (prereg l. 20-21). Aucun texte scellé n'existe dans `prereg/`, et la
    lecture décisive est faite. À **déclarer** comme écart, et à décontaminer : invite écrite par un sous-agent qui n'a pas
    vu la lecture, sans un mot sur le coût. Le coût seul (0,888) est déjà une référence boîte noire par règle ; le juge
    apportera surtout les faux positifs sur témoin et mention.
- **Coût** : codage, 0 USD (processeur, sous-agents, une journée). Juge Claude : crédits gratuits de Lazar (R-202 (3)),
  clé propre au programme à fournir, textes envoyés à Anthropic (dépendance nouvelle) ; montant à chiffrer au devis.
- **Revendications touchées** : validité de l'organisme (i) (programme, section 7) ; critères 2 (organismes) et 4 (base
  boîte noire) de G0.
- **Piège principal** : un juge qui code des textes n'est pas une vérité terrain, et lire des textes après coup invite à
  raconter (R4). Les textes restent dans le dépôt privé (N-014 ; prereg l. 191-197). Erreur sens « artefact » : se servir
  du codage pour isoler, dans P3, les actions « vraiment trompeuses » et y relire les sondes : interdit. Erreur sens
  « définitif » : déclarer l'organisme « sans intention » sur la foi du seul codage ; il dit ce que fait le texte, pas ce
  que fait le modèle (D2 le dit).

---

## Ordre proposé, par branche

- **A** (nul confirmé sans réserve) : D1 et D5 tout de suite (processeur, avant l'appel du 21 octobre) ; D6 (codage) ;
  puis D2 et D3 (1)-(2) dans une seule passe de carte, si Lazar accorde le devis ; D4 seulement si Lazar prolonge M0.
- **B** (nul avec réserves) : D1 ; puis selon la réserve. Plancher ou fuite : D3 (1) et (3), puis D2. Position du jeton
  dominant (A8) : D3 d'abord. Lecteur du coût (A6) : D6 d'abord. D5 avec les réserves écrites.
- **C** (instrument en échec) : D3 seul d'abord ; D1 pour la puissance ; D2 et D4 suspendus jusqu'à un instrument éprouvé.
  D5 se réduit à : critère 3 non tenable au 1er novembre, nœud.

## Ce que je ne propose pas

- Lire les 28 autres sondes déjà notées dans `scores-p3.npz` : seconde lecture interdite (prereg l. 428), et elles n'ont
  pas de plancher (seules les deux principales en ont, prereg l. 228). Le hasard seul en ferait passer une ou deux.
- Changer la recette du plancher, la fenêtre ou l'agrégation, puis relire P3.
- Élire les sondes de T0.7 sur les résultats de P3 : P3 est (i-a), T0.7 évalue (i). Ce serait une élection sur la famille
  évaluée (anti-circularité, programme l. 137 ; prereg l. 24 : les épisodes de P3 ne servent à aucune lecture de T0.6 ni de
  T0.7).
