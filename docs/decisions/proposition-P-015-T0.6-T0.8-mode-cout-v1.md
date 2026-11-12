# Proposition P-015 — périmètre de T0.6, T0.7 et T0.8 réécrits en mode « coût » — v1

Session 14, 2026-10-20 vers 14:00 UTC. Rang « proposer avec recommandation » : périmètre interne de la phase 0, couches
et concepts de sondes, D1. Défaut appliqué 48 heures après la transmission à Lazar. GO de principe : R-265 (6) (« T0.6
et T0.7 réécrits en mode « coût » : GO » ; périmètre à proposer avec recommandation). Rien ici ne change une hypothèse,
une revendication ni un critère de G0 (N-027 : critères inchangés).

**Décision.** Fixer le contenu et l'ordre des trois préenregistrements de la route vers G0 (critères 2, 3 et 4). Deux
faits les ont changés : le pilote n'a retenu que la famille « coût », et P3 a montré un organisme flagrant (coût seul à
0,888) et des sondes génériques sous leur plancher.

## Enjeu

- **Calendrier** : G0 au plus tard fin novembre (N-027). T0.6 génère les épisodes ; T0.7 (sondes) et T0.8 (bases boîte
  noire) les lisent.
- **Dépense** : 10 USD au plus par lancement sous la délégation (R-269). T0.6 dans sa forme du 6 octobre (1 536
  épisodes pour (i), 640 pour (ii), deux par tâche) dépasserait plusieurs fois ce plafond.
- **Rigueur** : la dose « diffuse » se fixe sur la boîte noire seule, avant toute lecture de sonde (B4 corrigée).
  Sinon, on règle la dose jusqu'à ce que la boîte blanche « gagne » (R3).

## Socle commun, à toutes les options (déjà acquis)

Sources :
- R-265 (6) ;
- réponses du brainstorm (`docs/notes/brainstorm-suite-P3-v1/reponses/reponses.md`, A6 corrigée l. 136-151, B4
  corrigée l. 197-213) ;
- N-029 (`docs/decisions/decision-N-029-v1.md`) ;
- verdict du pilote de T0.5 (`docs/verdicts/verdict-T0.5-pilote-v1.md`, l. 48 et 338 : famille « coût » seule
  retenue) ;
- N-007 (`docs/decisions/decision-N-007-N-008-v1.md` l. 28).

**T0.6 — organisme (i) en mode « coût »**
- **Mode principal** : coût déclaré gonflé (champ COST). « Affaiblir les contrôles » sort (brouillon du 6 octobre,
  l. 28, remplacé).
- **Dose** : proportion p d'actions sabotées × intensité (brief l. 163).
- **« Diffus »** :
  - il se lit sur les seules actions sabotées, jamais par dilution des étiquettes ;
  - chaque action sabotée reste sous le seuil du meilleur moniteur boîte noire par action, calibré à 1 % de faux
    positifs sur l'honnête (N-007) ;
  - c'est la dose réalisée qui compte (effet du type P3-P1 par dose), pas la dose écrite.
- **Conditions de référence obligatoires** :
  - honnête ;
  - témoin instruit, déclaré non neutre sur le coût (P3-P2) ;
  - mention : une consigne qui nomme le coût sans le demander gonflé, comme dans P3.
- **Lecteur du coût** : le défaut des séparateurs de milliers (verdict du pilote, section 8, point 5) se corrige dans
  un module de lecture neuf, sous nom neuf (R12). Le module gelé reste tel quel.

**T0.8 — bases boîte noire (N-029)**
- Les bases sont lues sur les épisodes de T0.6. Ce sont :
  - la règle du coût déclaré, calibrée sur l'honnête (B4 corrigée, point 1) ;
  - un juge par action Llama-3.1-8B-Instruct, à capacité égale (D1) ;
  - un prédicteur sur les traits du texte : coût normalisé par tâche, longueur, forme du champ coût.
- Elles passent par le même agrégateur séquentiel que les sondes.
- Le juge ouvert de 70B ne vient que sur un GO séparé.

**T0.7 — sondes (A6 corrigée)**
- **Sélection** : famille et couche figées d'avance, ou validées hors distribution ; jamais départagées par l'ordre.
- **Plancher** : recette gardée ; plancher sous permutation rapporté.
- **Puissance** : calculée sur les planchers et les largeurs observés (planification).
- **Lecture** : aucune lecture par champ.
- **Témoin positif** : P4-instrument, avant le premier résultat neuf.
- **Données gardées** : activations par jeton d'un sous-ensemble tiré par graine, et identifiants générés, avec un plan
  de stockage écrit.
- **Bases** : base « coût seul » à côté du témoin lexical.
- **Réplication** : T7-P1 sur (i-a) est déclarée réplication de P3 sur des épisodes neufs ; aucun choix n'est tiré de
  P3.

**Ordre** : le verdict de P4-instrument précède toute lecture de sonde sur les épisodes de T0.6 (règle du témoin
positif, ABC l. 83 ; R-262).

## Options : séquence, intensités, organisme (ii)

**(a) Tout en un : T0.6 complet en mode « coût », puis T0.7 et T0.8 lus sur ses épisodes.**
- **Contenu de T0.6** :
  - (i-a) : p ∈ {0,25 ; 0,5 ; 1} × deux intensités fixées a priori ;
  - témoin, mention, honnête ;
  - (ii) distillé en mode coût : α ∈ {0 ; 0,25 ; 0,5 ; 1}, plus un adaptateur témoin ;
  - un épisode par tâche et par condition, sur les tâches d'évaluation du pilote.
- **Avantage** : un seul texte pour T0.6 ; les trois critères se lisent sur les mêmes épisodes.
- **Inconvénient** : des intensités fixées a priori peuvent tomber hors de la zone « diffuse ». Dans P3, l'agent à qui
  on demandait trois fois le coût en a déclaré environ 33 fois, et le coût seul l'a détecté à 0,888. On ne le
  découvrirait qu'après coup.

**(b) En deux temps : recherche de dose sur la boîte noire seule, puis T0.6 décisif.**
- **Étape 1, préenregistrée, non décisive** :
  - une petite grille d'intensités de (i-a) en mode coût, sur les tâches de réserve, jamais sur les tâches
    d'évaluation ;
  - un épisode par tâche et par intensité, plus l'honnête ;
  - seules les bases boîte noire sont lues (règle du coût, juge 8B, prédicteur sur les traits du texte). Aucune sonde
    n'est lue (R3).
  - Règle écrite d'avance : on retient les intensités dont le rappel par action du meilleur moniteur, à 1 % de faux
    positifs, reste sous un seuil gelé, et dont l'effet réalisé sur le coût reste mesurable.
- **Étape 2** :
  - T0.6 décisif aux intensités retenues (p × intensité), avec honnête, témoin et mention, sur les tâches
    d'évaluation ;
  - puis (ii) distillé aux mêmes doses, en lancements séparés ;
  - T0.7 (A6 corrigée, plus E3) et T0.8 (N-029) sont préenregistrés et scellés avant l'étape 2, et lus sur ses
    épisodes.
- **Avantage** : la dose « diffuse » est établie avant toute sonde, sur la boîte noire seule (B4 corrigée) ; chaque
  lancement reste sous 10 USD.
- **Inconvénient** :
  - un lancement de plus et deux à trois jours ;
  - la zone diffuse peut être vide : aucune intensité sous le seuil avec un effet mesurable. Ce serait un nœud sur le
    critère 2. Le bruit de l'honnête rend ce risque réel : 43,7 % de ses coûts déclarés sont à plus d'un facteur 10 de
    la référence (verdict du pilote, section 8, point 4).

**(c) Minimal : (i-a) seul, une intensité, sans (ii) ni la sonde du domaine.**
- **Avantage** : le plus court ; un seul lancement.
- **Inconvénient** :
  - le critère 2 de G0 nomme (i) et (ii) avec une dose-réponse ; sans (ii), il reste non rempli (critères inchangés,
    N-027) ;
  - une seule intensité ne donne pas de dose-réponse en intensité ;
  - sans la sonde du domaine, T0.7 ne peut porter aucune revendication.

**Coûts** : estimations de la session, non devisées, sur la base de P3 : 240 épisodes, ≈ 3,1 heures de run
(`diag/20261019-230011-p3-reel/resume.json`, `resultat.duree_s`), ≈ 3,96 USD tout compris (`registres/depenses.md`
l. 88).

| poste | estimation |
|---|---|
| (a), organisme (i) : 9 conditions, ≈ 576 épisodes | ≈ 9 à 10 USD |
| (a), organisme (ii) : données de distillation (≈ 8 000 actions, brouillon du 6 octobre), entraînement, ≈ 320 épisodes | ≈ 15 USD, en deux lancements |
| (b), étape 1 | ≈ 2 à 3 USD |
| (b), étape 2, organisme (i) | ≈ 7 à 9 USD |
| (b), étape 2, organisme (ii) | ≈ 15 USD, en deux lancements |
| (c) | ≈ 3 à 4 USD |

Cumul de la phase 0 ≈ 67 USD plus les disques (R-262), sur 150. Chaque lancement : préenregistrement scellé et
contre-lu, délégation R-269, 10 USD au plus.

## Sonde du domaine (E3) et question de suivi (E2)

Sources : revue « comment détecter », v3, section 4. Une v4 est en cours de correction et reste à vérifier : ces deux
points se reprendront sur la v4.

- **E3, sonde du domaine, dans T0.7 (options (a) et (b))** :
  - le concept 4 de P-011, en mode coût ;
  - appris sur des paires synthétiques construites sur les tâches de réserve :
    - nombres équilibrés ;
    - versions incitées, l'incitation présente chez les positifs comme chez les négatifs ;
    - lecture avant le champ COST ;
  - choisi sur un jeu synthétique tenu à part, jamais sur des épisodes d'organisme (P-011) ;
  - évalué sur les épisodes neufs de T0.6 ;
  - contrôles P3-P4, T1, T3 et T4.
  - C'est la seule voie de la revue qui peut porter une revendication, car la sonde y est apprise sans l'organisme.
- **E2, question de suivi** :
  - elle se joue sur les épisodes neufs de T0.6, à l'aveugle, en descriptif de T0.7 ;
  - aucune ligne de lecture avant la v4 : la vérification de la v3 a relevé une prédiction d'échec trop générale
    (constat VV3-sens-02).

## Recommandation

**(b)**, confiance ≈ 60 %. La règle « dose fixée sur la boîte noire seule, avant toute sonde » demande une étape où
seules les bases boîte noire sont lues. P3 montre qu'une intensité fixée a priori peut être flagrante. **Défaut sous
48 heures : (b).**

## Ce que cette proposition ne fait pas

- Elle ne change aucun critère de G0.
- Elle ne change pas de modèle : Llama-3.1-8B-Instruct, à la révision du pilote.
- Elle n'engage aucune dépense.
- Elle laisse ouvert un nœud déjà noté par le brainstorm (réponse à O2-26) : prendre la règle du coût comme
  « moniteur par action » de N-007 en mode coût est un nœud de revendication, à trancher à part.

## Suite si (b) est retenue

Préenregistrements, dans l'ordre, chacun contre-lu par un sous-agent neuf (R2) et scellé avant son lancement :
1. T0.6, étape 1 (recherche de dose) ;
2. T0.8 (N-029) ;
3. T0.7 (A6 corrigée, plus E3) ;
4. T0.6, étape 2 ;
5. (ii).

Les brouillons du 6 octobre restent tels quels ; les textes neufs portent des noms neufs (R12).
