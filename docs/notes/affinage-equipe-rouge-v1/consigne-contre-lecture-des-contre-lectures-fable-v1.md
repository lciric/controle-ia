# Consigne — contre-lecture des deux contre-lectures (Opus et Argon) de la conception de l'affinage, par Fable — v1

Tu es une instance **neuve** du modèle Fable 5.1. Tu n'as écrit ni la conception relue (écrite par une autre session Fable,
sans contexte sur le programme), ni les deux contre-lectures (l'une par Opus 5.5, l'autre par Gemini Argon). Le directeur
du programme, Lazar, a demandé que ces deux contre-lectures soient à leur tour relues par Fable. Réponds en **français**,
sans sigle non développé. Tu ne produis que ton rapport.

## Ce que tu lis (tous en entier)

1. La conception relue : `conception-affinage-equipe-rouge-v1.md` (empreinte `789141db…`).
2. La contre-lecture d'Opus : `contre-lecture-opus-v1.md` (`03bc2869…`, constats CL-O-01 à 28, attaques manquantes
   AM-O-01 à 13).
3. La contre-lecture d'Argon : `contre-lecture-argon-v1.md` (`cead9f44…`, constats CL-A-01 à 15, attaques manquantes
   AM-A-01 à 08).
4. La consigne commune qu'ils avaient : `consigne-contre-lecture-affinage-v1.md`.
5. Pour le contexte de la mission, le lot de l'auteur sous `lot/` (le brief prime pour l'exécution).

## Ce que tu fais

1. **Chaque constat, un par un** (les 43 constats et les 21 attaques manquantes) : « fondé », « partiellement fondé »,
   « non fondé » ou « à vérifier », avec la raison et l'endroit de la conception (section ou ligne) qui le prouve.
   Cherche en particulier les **erreurs de lecture** des contre-lecteurs (un défaut reproché que la conception traite
   déjà ailleurs), les **gravités mal placées** (un « bloquant » qui n'en est pas un, ou l'inverse), et les **corrections
   proposées qui créeraient un défaut nouveau** (par exemple une garde qui violerait l'invariant « aucun score de moniteur
   ni de juge dans la sélection d'un agent », ou qui rouvrirait une fuite).
2. **Convergences et divergences** : quels défauts les deux contre-lecteurs ont-ils trouvés indépendamment (signal fort) ?
   Où se contredisent-ils ? Qu'a vu l'un et pas l'autre ?
3. **Ce que les deux ont manqué** : défauts de la conception qu'aucun des deux ne relève.
4. **La position de l'auteur** : là où la conception a raison contre ses critiques, défends-la, preuves à l'appui. Tu n'as
   aucune loyauté envers l'auteur : tu as le même modèle, ce qui est exactement le risque d'indulgence à surveiller ;
   signale toi-même tout endroit où tu soupçonnes ta propre indulgence.
5. **La liste consolidée** des corrections pour une version 2 de la conception, dans l'ordre, chacune avec les constats
   qu'elle couvre et son coût (texte seulement, ou code, ou décision du directeur).

## Règles

Niveau méthode seulement : tu ne développes jamais une méthode par laquelle un agent échapperait à un moniteur ; tu ne
présentes jamais une supposition comme un fait ; aucun chiffre inventé ; une référence de la littérature seulement si tu
peux l'attribuer correctement, sinon « à vérifier ».

## Ce que tu rends

Un rapport en Markdown, au plus ≈ 7 000 mots : en tête un **verdict sur chacune des deux contre-lectures** (« juste »,
« juste avec erreurs », « à reprendre ») et un verdict révisé sur la conception elle-même ; puis le tableau des constats
(identifiant, verdict, gravité révisée, raison, endroit) ; puis convergences, divergences, angles morts communs, défense
de l'auteur, signaux d'indulgence ; puis la liste consolidée pour la version 2 ; puis ce que tu n'as pas pu vérifier.
