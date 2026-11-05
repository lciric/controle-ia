# Proposition — nœud N-010 — suite de la validation de T0.4 sur modèle réel — v1

Rédigée le 2026-10-05 par la session de mise en œuvre, après le verdict R13 scellé `docs/verdicts/verdict-T0.4-critere-1-G0-v1.md` (sha256 `fb9919f9c4d7d73fd03bdcf65e03ef2492dd1951d4ffb10b43cd08d1e361f277`). Décision de Lazar attendue : c'est un nœud (modification d'hypothèse ou de paramètre), sans défaut.

## Décision

Comment rendre concluant le contrôle de logique (P2) sur le modèle réel, sans relever le seuil que la table gelée interdit de relever.

## Enjeu

- Le critère 1 de la porte G0 (« harnais validé ») est **non concluant** (verdict R13).
- Run A `20261005-102042-validation-reelle`, carte A100, simple précision stricte : l'écart entre génération et passe unique atteint 1,27e-4 à la couche 23, pour un seuil gelé de 1e-4.
  - Il croît avec la profondeur : maxima de 2,4e-5 (couche 7), 9,8e-5 (15) et 1,27e-4 (23).
  - Il est diffus (contexte 1,27e-4, zone générée 9,8e-5).
  - Les médianes, environ 5e-6, restent dans la fourchette attendue. Seules les queues dépassent le seuil.
  - Le contrôle négatif est conforme : 40 actions sur 40, minimum 1,10.
- Le juge a constaté que deux passes avant ordinaires sur un même préfixe divergent selon leur longueur totale, sans cache ni remplissage. Cela va dans le sens d'un arrondi qui dépend de la forme des produits matriciels (hypothèse décrite, non prouvée).
- Il a aussi relevé une limite de l'instrument : trois réglages (format TF32, réductions en précision réduite, mode déterministe) sont écrits par le code, pas relus. Le diagnostic que demande la table ne peut donc pas se faire sur les données consignées.
- À ce niveau d'arrondi, un défaut subtil de décodage ne se distinguerait plus. Sur modèle jouet, le défaut D1 allait de 3,3e-4 à 6,0e-4 ; son ampleur sur le modèle réel est inconnue.
- Toute option passe par une version 2 du préenregistrement : contre-lecture par un sous-agent neuf, scellement, puis juge neuf.
- Budget de carte restant pour T0.4 : 5,59 heures sur 6 ; dépensé à ce jour, environ 0,8 dollar.

## Options

Dans les trois options, la version 2 relit l'état effectif des réglages et le consigne : format TF32 des produits matriciels et de cuDNN, mode déterministe, noyaux d'attention permis. C'est ce qui manquait au diagnostic.

**(a) Contrôle de logique en double précision, seuil inchangé (1e-4), avec contrôle positif.**
- La phase de logique tourne en double précision sur la carte. La conversion des poids bfloat16 est exacte. Les captures restent en double précision.
- L'arrondi attendu tombe très en dessous de 1e-4. La bibliothèque calcule encore la normalisation et les rotations de position en simple précision, mais de la même façon dans les deux chemins.
- Contrôle positif : le défaut D1 (positions décodées décalées de +1) est injecté sur le modèle réel ; il doit être vu au-dessus du seuil.
- Production en bfloat16, rejeu dans le processus et run B : inchangés.
- Avantages :
  - la logique et la précision sont séparées proprement ;
  - le seuil gelé garde son sens ;
  - un seul cycle de travail ;
  - la carte A100 calcule en double précision à peu près aussi vite qu'en simple précision stricte.
- Inconvénients :
  - changement de code (chargement, capture et relecture en double précision ; tests sur modèle jouet), donc nouveau commit cité et contre-lectures ;
  - environ 73 Go de mémoire sur une carte de 80 Go : serré, mais sous la garde de 75 Gio ;
  - H-logique change de régime (double au lieu de simple précision) : c'est une modification d'hypothèse, qui revient à Lazar.

**(b) Diagnostic préenregistré en simple précision, puis seuil révisé avec contrôle positif.**
- Un run court mesure le plancher d'arrondi entre deux calculs identiques en logique mais différents en formes : passes uniques de longueurs différentes sur un même préfixe. Il mesure aussi l'effet de D1 injecté sur le modèle réel.
- Une version 2 fixe un seuil de logique entre les deux, avec une marge, comme la table l'exige (« vu au seuil révisé »).
- Avantage : on reste dans la précision de travail des sondes.
- Inconvénients :
  - deux cycles (diagnostic, puis version 2), et plus de temps de carte ;
  - le plancher dépend de la profondeur, de la longueur et du lot, donc le seuil est fragile hors du domaine observé.

**(c) Garder ce résultat comme description de l'arrondi en simple précision, sans version 2.**
- Avantage : aucun coût.
- Inconvénient : le critère 1 de G0 reste non concluant. La porte G0 ne peut pas se franchir sur ce critère.

## Recommandation

**(a)**, confiance d'environ 75 %. C'est la seule voie qui garde le seuil gelé et donne un contrôle de logique net. Le contrôle positif répond à l'exigence de la table, et le coût de carte reste faible : 1 à 2 heures, environ 1 à 2 dollars sur une A100.

Le risque principal est la mémoire de la carte. Il est couvert par les gardes existantes : la mémoire de la carte est contrôlée au lancement, et un manque de mémoire est une cause déterministe, donc un nœud, sans relancement.

## Défaut

Aucun : nœud. J'attends ton GO sur une option.

## Autre décision en attente (N-009, reste)

Les trois instances arrêtées (54183350, 54285455, 54298522) ne contiennent rien dont la lecture ait besoin : le juge le confirme pour 54298522. Leurs disques coûtent environ 3 dollars par jour à elles trois. Recommandation : les détruire, dans la console Vast.ai, ou sur ton accord explicite.
