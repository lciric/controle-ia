# Addendum 1 à l'ordre de la sonde de refus des lecteurs candidats Claude de l'étiqueteur v2 — v1

- **Ordre amendé** : `docs/procedures/ordre-sonde-refus-lecteur-c-etiqueteur-v2-v1.md` (`37b39e9a0ac3c2062e80a7e83fe657d76ea279d54f1cdcde5b9e4ed2ca95d029`, scellé, inchangé, R12).
- **Écrit par la session mère** `session_016QhUrrLeN21G7Z9KZobE42`, le 9 novembre 2026 à 11:13 UTC (`date -u`), R-2002.

## Cause

La fille clés 2 a exécuté l'étape 1 à 11:10:09Z : variable `RR_ANTHROPIC_API_KEY_RIGAUD` **absente** de son environnement (sa session a démarré avant le dépôt de la clé). Arrêt conforme, rien d'autre fait. La variable est présente dans la session mère (vérifiée par son nom à 11:12:55Z, valeur jamais lue).

## Décision de Lazar

Question posée dans la session mère à 11:11Z ; réponse choisie par Lazar, verbatim : « Moi, la mère (Recommandé) » (option : « Je la lance tout de suite dans ma session, sans lire les items : le script ne m'affiche que des comptes. »). Le « go » de dépense (GO-2026-11-09-02) a été écrit dans cette même session.

## Ce qui change (et seulement cela)

1. **Exécutante : la session mère**, à la place de la fille clés 2, dans son propre conteneur, mêmes étapes 0 à 8, même dossier de travail `/home/user/sonde-refus-lecteur-c-v1`, même entropie (celle de l'ordre scellé, 4013726077359997446), mêmes réglages, même règle.
2. **À l'aveugle** : la mère n'ouvre jamais les items, la clé, l'échantillon ni les réponses brutes ; elle ne lit que ce que le script imprime (comptes et empreintes), les manifestes et le nombre de lignes du journal. La phase 1 avait déjà été exécutée par la session mère (R-1757).
3. **Compte rendu** : à Lazar directement, comptes seulement (section 5 de l'ordre).
4. Le reste de l'ordre est inchangé.
