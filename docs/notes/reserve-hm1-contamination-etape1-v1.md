# Réserve de contamination : test H-M1 → étape 1 (v1)

Écrite par la lignée « session-depot » le 26 octobre 2026, avant toute lecture des résultats du test H-M1 v3
(`donnees/test-hm1-v3`, `64ae2eec`, R-458), sur le point 9 de l'avis de conv-audit (n° 69). Scellée avant la lecture.

## Pourquoi

H-M1 tourne sur le modèle de l'étape 1 (Llama-3.1-8B-Instruct, révision `0e9e39f2…`), lit une sonde à la couche 16 au
dernier jeton, entraînée sur la part `train` de la famille « conscience d'évaluation » de `confrontation-v1`. Son résultat
peut orienter, même sans intention, des choix de l'étape 1 v10 que « session-depot » écrit : vues lues (couches,
position de jeton), poids d'une famille, témoins de surface ou de format, construction de la banque (v3, v5), seuils.

## Gel

- Référence scellée de l'étape 1 : `prereg/gradient-etape1-sondes-v9.md`
  `6abcbe61757a11c5b36c1ddb4be190a402e5b0bcddc09e95eed1d44a0104a9e6`.
- La v10 ne changera, par rapport à la v9, que ce qui est déjà décidé ou demandé **avant** cette lecture :
  1. correctifs du noyau BC5-01 et R-441 (bootstrap), traits à réindexer, porte 0 : pièces de conv-audit
     `etape1-v10-materiaux-conv-audit-v1/` (commit `c47c1f81`, branche `canal/conv-audit-n04`) ;
  2. banque v3 aux identifiants opaques (R-443), défauts relevés par conv-audit aux n° 61–62 ;
  3. tout correctif mécanique sans effet sur une hypothèse, un seuil, une vue ou une famille.
- Vues lues (couches 8, 12, 16, 20, 24 × dernier jeton, moyenne en diagnostic seulement), familles, score, seuils,
  hypothèses et règles de lecture de la v9 : **gelés** ; tout changement de l'un d'eux après cette lecture cite cette
  réserve, se déclare dans le texte v10 et passe par Lazar (nœud de décision).

## Ce que la réserve ne protège pas

- « session-depot » lira le résultat de H-M1 (ou son prononcé) et écrit la v10 : l'influence d'un auteur informé sur les
  choix non listés ne se mesure pas ; elle est déclarée, pas bornée.
- conv-audit écrit qu'il ne lira pas H-M1 avant ce gel ; ce gel ne l'engage pas au-delà.

## Lecture

Analyse figée `analyser_hm1_v2.py` (`d699b823…`), lancée par « session-depot » ; prononcé de la lecture par un sous-agent
neuf qui applique les critères gelés du préenregistrement v3 (`225b24c4…`) ; audit de symétrie par un autre sous-agent neuf
si la lecture est tranchée ou trop belle (R4).
