# Décision — N-019 — nœud de la revalidation v2 de T0.5 (critère R8) — v1

- Date : 2026-10-12 (UTC). Décidée par la session sous la délégation de Lazar du 2026-10-11 (R-140 : « reprends le
  travail en full autonomy pendant 12h en prenant les decisions qui font avancer au maximum les resultats avec des tests
  robusts, élimine les pistes fragiles »). Révocable par Lazar : le lancement du pilote attend de toute façon sa recharge
  du crédit Vast.ai (R-143), donc rien n'est dépensé sur cette décision avant qu'il l'ait vue.
- Verdict tranché : `docs/verdicts/verdict-T0.5-revalidation-v2.md` (`f98b56841d2c9f93c84381d16dcdf9f438c5380dfc36b14654c0dba152a8a018`), prononcé par un sous-agent neuf (R13)
  et contre-vérifié par deux sceptiques neufs ; préenregistrement `prereg/T0.5-revalidation-equivalence-pilote-v2.md`
  (`4ff2b07548e90fc515fe8944a789bf44267be6e239dee02d2b479e9c701dcc61`).

## Le nœud

La revalidation conclut au **nœud** : aucun noyau n'est retenu. Le bras « defaut » est conforme avec marge sur toute
l'équivalence (R1 : 99e centile maximal 0,1354 ≤ 0,15 ; contrôle négatif 160 sur 160 ; repère ; rejeu identique ;
domaine ; chemin ; mémoire 24,02 Gio ; audit, ρ ≤ 1,55), mais il manque **R8** : la durée projetée des épisodes du
pilote vaut 8 089,62 s pour un plafond gelé de 7 800 s (3,7 % au-dessus). Le bras « math » est tombé en panne de
mémoire, comme la note de mémoire le prévoyait au-delà d'environ 4 400 jetons remplis. Aucune des deux propositions
prêtes du texte gelé ne s'applique ; ses options écrites (seuil refondé, autre carte, autre lot) visent une équivalence
manquante, or l'équivalence est établie : seul le budget de temps manque.

La durée projetée est, par le code de lecture cité (`duree_projetee_pilote`), linéaire dans le nombre d'épisodes du
pilote : (`generation_s` + `passe_unique_s`) × épisodes du pilote / 16, avec `generation_s` = 665,8512 s et
`passe_unique_s` = 8,2839 s mesurés sur les 16 épisodes du bras « defaut » (`mesures-defaut.json`), soit 42,13 s par
épisode. Ces 16 épisodes jouaient les 16 tâches d'entraînement aux énoncés **les plus longs** (choix gelé de la
revalidation) ; la projection est donc prudente pour un pilote aux énoncés en moyenne plus courts (moyenne des 60 premières tâches : 4 108 caractères). Elle l'est aussi parce que la revalidation capturait les activations de toutes les actions (fraction 1,0), le pilote de 5 % seulement, et que le chronométrage de la génération inclut la capture (`episode.py`, l. 220-240) ; l'effet n'est pas mesuré. Le second sceptique du verdict a cherché une lecture du texte gelé qui retiendrait un noyau malgré R8 (exclure la capture de la projection) : elle ne tient pas ; cette décision ne la retient pas.

## Options

| option | contenu | avantage | inconvénient |
|---|---|---|---|
| **(a)** | pilote réduit aux **60 premières tâches d'évaluation dans l'ordre du tirage** (180 épisodes) ; même noyau, même lot, même carte, mêmes réglages ; R8 appliquée, telle quelle, à ce pilote : 674,1351 × 180 / 16 = **7 584,02 s ≤ 7 800 s** | aucun seuil, aucune formule, aucune lecture ne change ; aucun calcul supplémentaire ; trois épisodes par tâche gardés (familles, kappa) ; le précédent existe dans la table du pilote (« 16 premières tâches dans l'ordre du tirage ») | 4 tâches de moins (6 %) ; la décomposition des juges exige 48 tâches complètes sur 60 (12 de marge au lieu de 16) ; marge de R8 de 216 s |
| (b) | 64 tâches, deux épisodes par tâche (D retiré) : 5 393 s | 64 tâches pour les juges ; plus de temps après les épisodes | change le code de lecture (hypothèse D-23 : trois épisodes par tâche) ; familles et kappa sur deux épisodes par tâche (réserve de paires réduite d'un tiers) |
| (c) | nouvelle revalidation à un autre lot ou une autre carte (options écrites de la table gelée) | domaine plus rapide | ces options visent une équivalence manquante, or elle est établie avec marge ; nouveau préenregistrement, nouveau run, nouvelle chaîne ; le débit ne gagne qu'environ 10 % de 8 à 32 lignes (tirage sur le processeur, en un fil ; verdict de T0.4 v3) ; crédit insuffisant pour revalidation et pilote |
| (d) | relâcher R8 ou le plafond de 15 000 s | garde les 64 tâches | change un critère ou une formule gelés : écart à un préenregistrement scellé, hors de la délégation |

## Décision

**(a)**. Confiance ≈ 70 %. Le pilote porte sur les 60 premières tâches du fichier des tâches d'évaluation assemblé par
l'extraction (`donnees/20261007-082440-t05-extraction/taches-evaluation.json`,
`76cdeace861d2fff45ca732c55c2d97611dcd47edc7c27d62bdad4c37755e67e` ; ordre du tirage, rang de garde ; aucun
remplacement), recopiées à l'identique dans un fichier dérivé, scellé. Pour ce pilote, le bras « defaut » satisfait R1 à
R8 et l'audit, avec marge : **noyau « defaut »**. Formule gelée de `duree_max_s` : min(15 000 ; ⌈(1,2 × 7 584,02 +
7 200) / 60⌉ × 60) = min(15 000 ; 16 320) = **15 000 s**.

Ce que cette décision ne change pas : le verdict scellé de la revalidation (nœud, pour le pilote de 192 épisodes) ; R8
(7 800 s) et la formule de `duree_max_s` ; les seuils, prédictions, critères de lecture et constantes du pilote ; le
code de lecture. Elle change la taille de l'échantillon du pilote, encore en brouillon (non scellé).

## Risques déclarés

- **Durée des juges, jamais mesurée.** Il reste au pilote 15 000 − 7 584 ≈ 7 416 s après les épisodes. L'appariement
  passe désormais en premier (quelques minutes ; familles protégées, critère 2 de G0). Les notations décisives des deux
  juges sont estimées, sans mesure, entre environ 5 400 et 15 100 s (état des lieux, VR-03) : l'échéance peut arrêter
  les notations du second juge (3B). La table du pilote le lit déjà : juge incomplet en nœud, notation à refaire sur
  les ensembles déjà générés et scellés.
- **Marge de R8 mince** (216 s, 2,8 %), mais sans effet sur le déroulé : l'échéance interne est 15 000 s dans les deux
  cas, et la projection vient des énoncés les plus longs.
- **Énoncés** : réserve RV-5 maintenue (plus long énoncé du pilote : 6 786 caractères, aussi dans les 60 premières
  tâches ; revalidation : 3 709 à 5 340).

## Après la délégation

La délégation finit le 2026-10-12 à 10:40 UTC. N-019 reste tranchée tant que Lazar ne la révoque pas (une ligne R-… qui la révoque arrête le lanceur du pilote). La dépense du pilote relève du devis de la phase 0 (GO-2026-10-04-08) ; le lancement suit le plan dès que le crédit le permet, ce qui demande de toute façon la recharge de Lazar.

## Contrôles

La décision est soumise à la relecture R2 du préenregistrement du pilote (brouillon 8), avec une question explicite :
« la réduction à 60 tâches change-t-elle une lecture gelée de la revalidation ? ». Une réponse fondée « oui » ramène le
nœud à Lazar avant tout lancement.
