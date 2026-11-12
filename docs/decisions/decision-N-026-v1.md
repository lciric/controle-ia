# Décision — N-026 : précision de la règle d'agrégation des sondes (bras de diagnostic « moyenne ») — v1

- **Décision de Lazar** : option (b), donnée dans la session 14 le 2026-10-20 vers 09:10 UTC (« go b ») ; GO-2026-10-20-03
  (type « règle ») ; R-258.
- **Question** (session 14, même échange) : la revue de la littérature demandée par Lazar après le verdict de P3 rapporte,
  d'après Gemini (non vérifié, R7), que les sondes de tromperie d'Apollo Research (2502.03407) agrègent par moyenne sur les
  jetons de la réponse ; faut-il modifier la règle qui l'interdit ?
- **Règle en cause** : brief v2 (`docs/brief-claude-code-programme-complet-v2.md`, section 2, l. 39, et interdits, l. 401) ;
  programme v2 (`docs/programme-controle-ia-v2.md`, règle gelée 1, l. 13) : « Sondes à agrégation max ou attention sur les
  tokens, jamais moyenne ni médiane : ces dernières sont évadables par apprentissage par renforcement sur les poids, max et
  attention résistent. »

## 1. Décision

La règle est **gardée telle quelle** pour toute sonde de production (moniteur, revendication, porte). Elle est **précisée**
ainsi :

- un **bras de diagnostic** à agrégation par moyenne (ou médiane) sur les jetons d'une action est **permis** dans un
  préenregistrement d'audit ou d'expérience, s'il remplit toutes ces conditions :
  1. il est écrit et nommé « bras de diagnostic, jamais en production » dans le préenregistrement scellé, avant toute lecture ;
  2. il est comparé au **même plancher apparié**, calculé avec la **même agrégation** que lui ;
  3. il ne sert jamais de moniteur, ne porte aucune revendication, ne fait franchir aucune porte, et ne remplace jamais le bras
     de production (maximum ou attention), qui reste lu et rapporté à côté ;
  4. son résultat se lit comme un diagnostic de l'instrument (« l'agrégation explique-t-elle le nul ? »), jamais comme une
     preuve de détection.

## 2. Enjeu et raisons

- La règle protège le moniteur contre un attaquant qui dilue sa trace (évasion par apprentissage par renforcement) : la
  thèse des papiers A et B s'appuie sur elle.
- Les succès rapportés avec la moyenne (Apollo, à vérifier) portent sur une tromperie verbalisée tout au long de la réponse,
  sans attaquant adapté à la sonde. Dans P3, la triche est localisée dans le champ du coût : la moyenne devrait la diluer ;
  le bras de diagnostic dira proprement si ce n'est pas le cas.

## 3. Ce qui ne change pas

- Le programme et le brief ne sont pas réécrits ; ils se lisent avec cette décision jusqu'à une version nouvelle transmise
  par Lazar. Aucun préenregistrement scellé n'est touché (P3 et son addendum restent tels qu'ils sont).
