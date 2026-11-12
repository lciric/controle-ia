# Proposition — N-019 — nœud de la revalidation v2 de T0.5 (critère R8) — v2

- Date : 2026-10-12 (UTC). Rédigée par la session ; soumise à Lazar. **Nœud de décision, sans défaut** : sans GO, rien
  n'est scellé ni lancé pour le pilote. **Une recharge du crédit seule n'est pas un GO.** Réponse attendue :
  « GO N-019 (x) », x étant l'option retenue.
- Version 2 : elle remplace, comme pièce soumise, la v1 (`docs/decisions/proposition-N-019-v1.md`, c5d46e60…, gardée),
  après la vérification courte du candidat 2 (angle « N-019 », sous-agent neuf ; VN-01 à VN-14) : option « budget
  refait » ajoutée (celle que recommandait l'état des lieux), sort probable du juge 3B dit, marges et calendrier donnés,
  trois options et des options écartées.
- Statut : la décision `docs/decisions/decision-N-019-v1.md` (9058fa27…), prise par la session sous la délégation R-140,
  est **retirée** (R-145). La relecture R2 du pilote a établi qu'elle changeait une lecture gelée de la revalidation, ce
  que R-140 exclut (NO-01, NO-02, confirmées par deux sceptiques chacune) ; l'état des lieux l'avait déjà écrit (VR-02,
  VR-16). Portée de l'erreur : la chaîne d'alors n'exigeait pas ton GO et aurait pu lancer le pilote sur une simple
  recharge (NO-03) ; elle l'exige désormais (générateur, contrôles avant dépense, lanceur), et des bancs l'éprouvent.
- Pièces : verdict R13 `docs/verdicts/verdict-T0.5-revalidation-v2.md` ; préenregistrement scellé de la revalidation
  `prereg/T0.5-revalidation-equivalence-pilote-v2.md` (4ff2b075… ; l. 97 : R8) ; code `revalider_pilote_a.py`
  (`EPISODES_PILOTE = 192`) ; mesures `diag/20261011-225701-t05-revalidation-reel/mesures-defaut.json` ; rapports de la
  relecture R2 et de la vérification courte sous `prereg/contre-lectures/T0.5-pilote-v1-relecture-b8-*` (empreintes
  dans la ligne R-… qui consigne cette version).

## Décision demandée

Choisir comment sortir du nœud de la revalidation v2 : le bras « defaut » est conforme sur toute l'équivalence, mais la
durée projetée des épisodes du pilote (192 épisodes) vaut 8 089,62 s pour un plafond gelé R8 de 7 800 s.

## Enjeu

Sans noyau retenu, le pilote ne tourne pas ; il donne les familles d'idées (vérité terrain du critère 2 de G0) et la
qualification des deux juges (P-009, P-010). Le vrai risque est la durée des juges, jamais mesurée : dans un run de
15 000 s, l'estimation centrale de l'état des lieux (≈ 9 300 s pour l'appariement et les notations décisives, faite pour 64 tâches ; de 5 400 à 15 100 s) dépasse
le temps restant ; le 3B serait alors coupé (P3 non concluante, sa notation à refaire sur les ensembles scellés).

## Options

| option | contenu | avantage | inconvénient |
|---|---|---|---|
| **(a)** | pilote réduit aux **60 premières tâches dans l'ordre du tirage** (180 épisodes) ; R8 avec 180 au lieu de la constante 192 : 674,1351 × 180 / 16 = 7 584,02 s ≤ 7 800 s ; noyau « defaut » ; `duree_max_s` par la formule gelée : 15 000 s ; aucun seuil ni critère du pilote ne change | prêt (préenregistrement vérifié, chaîne et bancs) ; lancement quelques heures après ton GO et la recharge, lecture vers le 13 octobre ; familles d'idées et juge 8B probablement complets (l'appariement est joué en premier) | écart nommé à une lecture gelée (192 → 180), N choisi après lecture de R8 ; 4 tâches de moins ; marge mince (216 s, 2,8 %, par la formule linéaire ; 47 s, 0,6 %, par lots) ; temps des juges ≈ 7 416 s bruts, ≈ 5 600 à 6 900 s nets (appariement, de 5 à 27 minutes, et chargements, ≈ 200 s, déduits) : dans le cas central le **3B est coupé**, P3 non concluante, et sa notation est à refaire plus tard (code, préenregistrement et GO de calcul nouveaux) |
| (c) | nouvelle revalidation sur un autre domaine (autre lot ou autre carte) : option écrite du texte gelé | aucune lecture gelée touchée | nouveau préenregistrement et run (≈ 2 à 3 USD), puis le pilote, avec le même risque sur les juges ; « autre carte » sort de GO-2026-10-06-02 et renchérit le pilote ; gain incertain (le débit dépend de l'hôte) ; second nœud possible ; lecture vers le 16 ou 17 octobre |
| (e) | **budget refait** (recommandé par l'état des lieux) : R8 relâchée et deux runs (épisodes et appariement, puis notations des juges sur les ensembles scellés) ou un run allongé | couvre le cas central des deux juges (≈ 5,6 h d'instance, ≈ 6,7 USD ; cas pessimiste ≈ 8,0 h, ≈ 9,3 USD) | change un critère gelé (R8) et le plafond de 15 000 s ; code, tests, préenregistrement et relecture R2 nouveaux ; GO de calcul au-delà des 5 heures du devis ; lecture vers le 16 à 18 octobre |

Écartées : (b) 64 tâches à deux épisodes par tâche (d = 5 393,08 s, `duree_max_s` 13 680 s, ≈ 8 287 s pour les juges) :
écart plus grand (la constante de R8 et une hypothèse du code de lecture, trois épisodes par tâche ; code et relecture
nouveaux) ; (d) relâcher R8 seule dans 15 000 s : moins de temps pour les juges (≈ 6 910 s bruts) que (a).

Notes : la durée projetée d est prudente (la revalidation capturait les activations de toutes les actions, le pilote de
5 % ; effet non mesuré). Le lanceur n'admet que l'A100 SXM4 et l'hôte de la revalidation (AMD EPYC 7513) : une offre
conforme peut se faire attendre. Calendrier de P-007 : lecture du pilote prévue le 12 octobre, point de contrôle du
critère 2 le 19 ; (a) le tient, (c) et (e) le serrent.

## Recommandation

**(a)**, confiance moyenne (≈ 70 %) : l'écart le plus petit (une constante, même carte, même lot, même noyau), sans
dépense de plus, et la vérité terrain du critère 2 (familles d'idées) dans les temps ; le 3B, probablement coupé, se
complète ensuite par une notation sur les ensembles scellés. Choisir (e) si tu tiens à qualifier les deux juges dans un
seul pilote ; (c) si tu préfères ne toucher à aucune lecture gelée.

## Ce que ton GO déclenche

Sur (a) : une ligne dans `registres/go.md` (type « revendication », comme GO-2026-10-11-01 pour N-018), la colonne
d'état de N-019 « tranché (a) par Lazar : GO (R-…) », le scellement du préenregistrement du pilote, qui cite ton GO,
puis les contrôles avant dépense et la création, dès que le crédit le permet (recharge). Sur (c) ou (e) : un
préenregistrement nouveau, relu (R2), avant toute dépense.

## Pas de défaut

C'est un nœud : sans réponse, rien n'est scellé ni lancé. Les valeurs ci-dessus sont recalculées depuis les mesures
scellées (`mesures-defaut.json`) ; 674,1351 s par 16 épisodes ; 7 584,02 s ≤ 7 800 s ; 15 000 s ; noyau « defaut ».
