# Décision — N-029 : référence boîte noire de la comparaison boîte blanche contre boîte noire (nœud 4 du brainstorm sur la suite de P3) — v1

- **Décision de Lazar** : option (c) renforcée, donnée dans la session 14 le 2026-10-20, message reçu entre 11:25 et
  11:40 UTC (« option c renforcee »), en réponse à la recommandation de la session (même échange ; confiance ≈ 70 %) ; GO-2026-10-20-08 (type
  « décision ») ; R-276.
- **Ce qu'elle remplace** : la décision R-202 (3) du 2026-10-17 (`registres/decisions.md`) : « référence boîte noire par
  l'API Claude (crédits gratuits de Lazar, 200 USD) : un juge Claude relit les textes gardés après le run ». Sa condition,
  un préenregistrement scellé sans lecture des résultats de P3, est rompue : la lecture décisive de P3 est faite et aucun
  texte de cette référence n'a été scellé (note du brainstorm, `docs/notes/brainstorm-suite-P3-v1/note-decision-suite-P3-v1.md`,
  `a023093e…`, nœud 4 ; objections 1, l. 15 et l. 101 ; proposition D, l. 204-208).
- **Avis consultés** : Gemini, requête 011 (branche `canal/gemini`,
  `brouillons/canal_gemini/inbox_pour_claude/reponse_a_011_avis_reference_boite_noire.md` ; (c) renforcée, confiance
  85 %, non opposable) ; R-267.

## 1. Décision

La référence boîte noire du programme est **locale, reproductible, et lue sur les épisodes de l'organisme diffus**. Elle
prend la forme de la base T0.8 (brief v2, T0.8 ; critère 4 de G0) appliquée aux épisodes de T0.6, renforcée de deux bras :

1. **Juge par action à capacité égale** (T0.8, moniteur faible par action ; modèle selon la décision D1) : c'est la case
   boîte noire du plan 2 × 2 accès × agrégation (programme v2, section 0, décision 3 ; E1.2), à capacité égale avec
   l'agent lu par les sondes.
2. **Prédicteur sur les traits du texte, obligatoire** : un prédicteur simple, sans modèle de langue, sur des traits
   extraits du texte des actions (au moins : coût déclaré normalisé par tâche, longueur, forme du champ du coût). C'est la
   base boîte noire gratuite que toute sonde doit battre ; sur l'organisme flagrant de P3, le coût seul sépare déjà
   (0,8878, `diag/20261020-075740-p3-lecture/lecture-p3.json`, `c221d955…`). Ses traits sont fixés dans le préenregistrement
   de T0.8, avant toute lecture des épisodes de T0.6.
3. **Juge génératif ouvert de grande taille, en plafond, plus tard** (par exemple 70 milliards de paramètres, quantifié,
   lu par la probabilité du jeton de verdict) : il répond à l'objection « homme de paille ». Il n'est **pas** décidé ici :
   il demande un GO séparé (changement de modèle, interdit sans GO ; devis de calcul), après le verdict de G0.

**Retirés** : le juge Claude par l'API sur les textes de P3, et tout envoi de textes d'action du programme à un service
tiers pour cette référence.

## 2. Portée

- **Où se lit la comparaison** : sur les épisodes de T0.6 (organisme diffus, doses en proportion × intensité, note du
  brainstorm, socle commun), avec le même agrégateur séquentiel appliqué aux scores boîte noire (brief, T0.8). Elle ne se
  lit pas sur les textes de P3 (organisme flagrant ; lecture déjà faite).
- **Préenregistrements touchés** : celui de T0.8 (brouillons `brouillons/T0.8-*`) reçoit le bras 2 ; la réécriture de
  T0.6, T0.7 et T0.8 en mode « coût » (R-265 (6)) le porte, avec sa proposition de périmètre.
- **Critère 4 de G0** (base boîte noire, par action et séquentielle, sur le même jeu d'épisodes) : inchangé ; cette
  décision fixe seulement ce que « base boîte noire » contient.
- **Calendrier** : aucune comparaison boîte noire avant T0.6. Rien n'est à dire d'autre à l'appel EA Funds qu'« une
  comparaison préenregistrée, sur l'organisme diffus, contre des bases boîte noire locales et reproductibles ».
- **Crédits de l'API Claude de Lazar** : non engagés par cette décision. La session suggère de les réserver au papier C,
  où les juges génératifs de premier rang sont l'objet étudié (décision D2) ; c'est une proposition, pas une décision.

## 3. Ce qui ne change pas

- R-202 (1) et (2) (audit R4, condition « mention sans usage ») ; le plan 2 × 2 ; les portes et leurs critères ; la règle
  d'agrégation des sondes (N-026).
- Aucune hypothèse ni revendication n'est modifiée.
