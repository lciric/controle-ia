# Proposition — nœud N-025 — audit des remarques du verdict de P3 avant le GO — v1

Rédigée le 2026-10-20 vers 08:55 UTC par la session 14, après la réponse de Lazar « Audit d'abord » à la demande de GO sur
le verdict R13 de P3 (`docs/verdicts/verdict-P3-premier-test-i-a-v1.md`, `0c8ecbdf…`, R-256 ; décision R-257). C'est un
nœud : le préenregistrement de P3 (l. 415-416) fait de tout audit qui demande une grandeur non écrite un nœud de Lazar,
« nouveau run ou préenregistrement complémentaire, jamais une lecture ajoutée ».

## Décision

Quelles remarques de la section 7 du verdict auditer, et par quel moyen, avant le GO sur le verdict ?

## Enjeu

Le verdict est un nul propre : « aucune sonde générique au-dessus du plancher sur (i-a) », P3-P1 établie, P3-P3 réfutée,
lu « non détecté à cette puissance », sans réserve. Ses quatre remarques (hors critères gelés) touchent la lecture du nul :
1. **Ampleur de P3-P1** : effet 1,5227 en log10 (rapport ≈ 33) au lieu de « au plus ≈ 0,48 » (rapport 3) ; formes du
   champ du coût très inégales entre conditions (honnête : 41 actions à plusieurs nombres, 14 à suffixe « k », 13 à
   intervalle ; saboteur : 3, 0, 0). Le coût écrit seul sépare saboteur et honnête à 0,888 d'aire ([L] audit R4), alors que
   les sondes restent sous leur plancher. Le contrôle A6 de l'addendum (lecteur étendu) laisse P3-P1 établie (borne basse
   1,2471).
2. **Signe de P3-P2** : effet du témoin et de la mention sur le coût entièrement négatif ([−0,570 ; −0,065]), prédit ≈ 0.
3. **Sonde de tromperie** : aire 0,5748 au-dessus du quantile du plancher (0,5717), borne basse à 97,5 % (0,5313) en
   dessous ; demi-largeur observée ≈ 0,044 contre 0,025 à 0,037 supposés au préenregistrement : la puissance du nul est
   plus faible que prévu (sceptique 1, SC-1-01).
4. **Drapeau T2 vrai, non lu** : la règle gelée interdit de le citer ; rien à auditer sans rouvrir la table.

## Options

| option | contenu | avantage | inconvénient |
|---|---|---|---|
| **(a) addendum 2 préenregistré, remarques 1 à 3** | un préenregistrement complémentaire, non décisif comme le premier (réserves au verdict, aucune promotion), sur les données gardées, processeur seulement, sans dépense : (1) P3-P1 par forme du coût et par tâche, et part de l'effet portée par les formes ; (2) P3-P2 par forme ; (3) puissance du nul : aire minimale détectable à la demi-largeur et au plancher observés, par sonde. Scellé, contre-lu (R2), puis verdict R13 complété par des sous-agents neufs | répond aux trois remarques qui touchent la lecture du nul et de l'organisme ; même garde-fous que le premier addendum | un cycle complet (texte, code, contre-lectures) : un à deux jours |
| (b) addendum 2 réduit à la remarque 3 (puissance) | seulement l'aire minimale détectable aux largeurs observées | rapide (quelques heures) ; dit exactement ce que vaut le nul | laisse ouverte la question de l'organisme (remarque 1), qui conditionne P4 |
| (c) pas d'addendum : GO maintenant | les remarques passent au préenregistrement de P4 (brainstorm en cours) | aucun délai | le nul part avec une puissance non chiffrée et un organisme dont l'ampleur n'est pas expliquée |

## Recommandation

**(a)**, confiance ≈ 60 %. La remarque 3 dit ce que vaut le nul ; la remarque 1 dit si l'organisme fait ce qu'on croit
(un rapport de 33 et un coût écrit qui sépare à 0,89 changent le dessin de P4) ; la remarque 2 se lit avec la 1, pour un
coût marginal. La remarque 4 reste exclue par la règle gelée. L'instance 56799469 reste gardée jusqu'au 2026-10-23 vers
02:07 UTC (décision de Lazar), puis détruite ; l'audit n'en a pas besoin (données gardées dans le dépôt).

Nœud : pas de défaut. P3 reste ouvert jusqu'au GO de Lazar sur le verdict complété.
