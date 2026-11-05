# Proposition — N-019 — nœud de la revalidation v2 de T0.5 (critère R8) — v1

- Date : 2026-10-12 (UTC). Rédigée par la session ; soumise à Lazar. **Nœud de décision, sans défaut** : sans GO, rien
  n'est scellé ni lancé pour le pilote.
- Statut : cette proposition remplace, comme statut, la décision `docs/decisions/decision-N-019-v1.md`, prise le même jour
  par la session sous la délégation R-140 et **retirée** (R-145). La relecture R2 du pilote (angle « N-019 », sous-agent
  neuf, en sceptique : `prereg/contre-lectures/T0.5-pilote-v1-relecture-b8-*`) a établi que cette décision change une
  lecture gelée de la revalidation, ce que R-140 exclut ; l'état des lieux du pilote l'avait déjà écrit (bloquant 0,
  VR-02, VR-16), et la décision n'y avait pas répondu. C'est une erreur de la session. Le contenu technique de l'option
  (a) reste celui de la décision v1 ; ses valeurs ont été recalculées par la relecture (identiques).
- Pièces : verdict R13 `docs/verdicts/verdict-T0.5-revalidation-v2.md` (nœud) ; préenregistrement scellé de la
  revalidation `prereg/T0.5-revalidation-equivalence-pilote-v2.md` (l. 97 : R8) ; code cité
  `src/controle_ia/environnements/revalider_pilote_a.py` (`EPISODES_PILOTE = 192`, `duree_projetee_pilote`) ; mesures
  `diag/20261011-225701-t05-revalidation-reel/mesures-defaut.json`.

## Décision demandée

Choisir comment sortir du nœud de la revalidation v2 : le bras « defaut » y est conforme sur toute l'équivalence, mais
la durée projetée des épisodes du pilote (192 épisodes) vaut 8 089,62 s pour un plafond gelé R8 de 7 800 s.

## Enjeu

- Sans noyau retenu, le pilote ne tourne pas ; or il porte le critère 2 de G0 (familles d'idées, P1, P7) et la
  qualification des juges (P-009, P-010).
- R8 protège le temps laissé aux juges dans le run unique de 15 000 s : à 192 épisodes, il leur reste environ 6 910 s ;
  à 180, environ 7 416 s. Les notations décisives sont estimées, sans mesure, entre 4 600 et 13 500 s (état des lieux,
  VR-03) : l'enjeu réel est la durée des juges, plus que le passage formel de R8.
- La marge de R8 à 180 épisodes (216 s, 2,8 %) est du même ordre que les incertitudes connues : énoncés du pilote en
  moyenne 3 % plus courts que ceux de la revalidation, hôte, carte (le filtre admet l'A100 PCIe ; R8 a été mesurée sur
  SXM4).

## L'écart, nommé

Le texte scellé de la revalidation définit R8 par « (durée de génération + durée des passes uniques du bras) × 192 / 16
épisodes » (l. 97) ; le code cité fixe `EPISODES_PILOTE = 192`. L'option (a) remplace 192 par 180 (pilote réduit à 60
tâches) **après la lecture du résultat** : la règle de choix gelée passe du nœud, `(None, None)`, au noyau
`('defaut', None)` (rejeu de `lire_bras` par la relecture : seuls `R8_duree`, `conforme` et `conforme_avec_marge`
changent). C'est un écart à un préenregistrement scellé qui change une lecture : il relève de toi.

## Options

| option | contenu | avantage | inconvénient |
|---|---|---|---|
| **(a)** | pilote réduit aux **60 premières tâches d'évaluation dans l'ordre du tirage** (180 épisodes) ; R8 avec 180 au lieu de la constante 192 : 674,1351 × 180 / 16 = 7 584,02 s ≤ 7 800 s ; noyau « defaut » ; `duree_max_s` par la formule gelée : 15 000 s ; aucun seuil, aucune prédiction, aucun critère du pilote ne change | prêt : préenregistrement relu (R2), chaîne éprouvée ; aucune dépense de plus ; environ 506 s de plus pour les juges | écart nommé à une lecture gelée (192 → 180) ; 4 tâches de moins (6 %) ; la règle des 48 tâches complètes passe de 75 % à 80 % des tâches ; N = 60 est choisi après la lecture de R8 (61 passerait aussi, à 7 710 s ; 60 garde 2,8 % de marge) ; les 4 tâches retirées sont, par le hasard du tirage, toutes « experiments_only », dont trois parmi les cinq énoncés les plus courts |
| (b) | 64 tâches, deux épisodes par tâche (128 épisodes) | 64 tâches | change aussi la constante de R8 (192 → 128), et une hypothèse du code de lecture (trois épisodes par tâche : familles, kappa) : écart plus grand |
| (c) | nouvelle revalidation, sur un autre domaine (autre carte, autre lot) : option écrite du texte gelé | la seule option que le texte gelé écrit ; une carte plus rapide répondrait directement à R8 | nouveau préenregistrement, nouveau run (environ 2 à 3 USD), puis le pilote : quelques jours de plus et une recharge plus forte |
| (d) | relâcher R8 : 64 tâches, noyau « defaut » | 64 tâches ; rien à revalider | change un critère gelé ; moins de temps pour les juges (environ 6 910 s), donc un juge incomplet plus probable |

## Recommandation

**(a)**, confiance d'environ 70 % : c'est l'écart le plus petit (une constante, aucun seuil, même domaine : même carte,
même lot, même noyau), sans dépense de plus, et il augmente le temps laissé aux juges au lieu de le réduire. Choisir
(c) si tu préfères ne toucher à aucune lecture gelée : elle coûte un run et quelques jours.

## Ce que ton GO déclenche

Sur (a) : une ligne dans `registres/go.md` (type « revendication », comme GO-2026-10-11-01 pour N-018), la ligne N-019
tranchée, puis le scellement du préenregistrement du pilote, qui cite ton GO ; les contrôles avant dépense et le
lanceur exigent ce GO et refusent un GO révoqué. Le lancement suit dès que le crédit le permet (recharge).

## Pas de défaut

C'est un nœud : sans réponse, rien n'est scellé ni lancé. Tout ce qui ne dépend pas de ta réponse est préparé.
