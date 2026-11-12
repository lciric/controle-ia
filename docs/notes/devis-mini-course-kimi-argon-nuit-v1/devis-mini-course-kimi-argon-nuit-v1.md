# Devis : mini-course d'idéation réelle, Kimi et Argon seuls, nuit du 1er au 2 novembre 2026 (v1)

Demande : n° 323 de conv-audit, point 2. Aucune dépense, aucun lancement. `O` = copie de l'orchestrateur v56 (`…/scratchpad/v56-epreuve-pont/orchestrateur-v56/`).

## Verdict

**Oui, faisable cette nuit, de justesse.** Le code v56 accepte une composition faite seulement de Kimi et d'Argon, mais un lancement réel exige d'abord :
- trois pièces neuves ;
- un préenregistrement scellé et contre-lu.

Compter 6 à 8 heures de préparation, puis environ 2 h 30 de calcul en série. Si la préparation glisse, il reste un repli : le scénario C, sans bisociateur.

## Ce que dit le code (VÉRIFIÉ)

- **Étapes** : proposition, aiguillage, juges, passe « tableau », étiquettes, fusions (`O/pole/course2_v53.py:42`). Lanceur : `O/demonstrations/ideation_v8.py`.
- **Modèle par rôle** : il se fixe dans la configuration. Le code exige seulement un adaptateur pour chaque rôle et **ne contrôle jamais la famille** (`O/pole/course2_v54.py:88-91`).
- **Juges** : chaque juge note chaque fiche, sans contrôle de famille (`O/pole/noyau_v56.py:192-222`). Avec deux familles, chaque fiche a donc un juge de sa propre famille. L'autre lignée se lit après coup.
- **Adjudicateur** : il n'y en a pas dans la course. Il n'existe qu'au pré-pilote (`O/pole/prepilote_v54.py:13,94`).
- **Bisociateur** : exactement deux lecteurs (`course2_v54.py:266`), un choix de paires par programme et un metteur en fusion. Les bras se choisissent librement, aucun bras compris (`O/pole/configuration_v53.py:99`).
- **Fournisseurs** :
  - Kimi, par protocole, joue proposeur, juge et fusion (`O/pole/adaptateur_kimi_v53.py:34`) ;
  - Argon passe par une commande externe, qui joue proposeur et juge (`O/pole/adaptateurs.py:619`).
- **Appels en série** : le noyau n'appelle les modèles qu'un par un (aucun groupe de fils dans `noyau_v5*` ni `course2_v5*`). La concurrence du relais Kimi est sans effet.
- **Exigences du moteur réel** :
  - une porte de plafond par fournisseur (`O/pole/configuration_v56.py:174-180`) ;
  - un préenregistrement scellé et sa contre-lecture (docstring, point 3) ;
  - une ligne de GO et l'option `--confirmer-moteur-reel` (`ideation_v8.py:113-121`).
- **Mode simulé** : `--moteur simule` (le faux SDK ne sert qu'à Claude).
- **Commande d'Argon** : `/opt/argon/commande_argon_v2.py` est absente de ce conteneur (vérifié par `ls`). L'épreuve du pont appelait directement `appeler_gemini` (`donnees/espece-seule-v1/collisionneur_v7.py:423`), sans le noyau.

## Adaptations minimales (nouveaux noms, rien d'écrasé)

1. **`commande_argon_v56_nuit_v1.py`** (1,5 à 2 h) : enveloppe `appeler_gemini`, sans reprise interne, dans le contrat de la commande externe.
   - Entrée : la consigne sur l'entrée standard, puis les variables `PLAFOND_ETAPE_USD` et `MODELE_DEMANDE_POLE`.
   - Sortie : une dernière ligne JSON `{texte, cout_usd > 0, modele_servi}`.
   - Clé : lue hors du dépôt, jamais dans l'environnement de l'orchestrateur.
2. **`commande_kimi_v2.py`** (1 h) : reprend `commande_kimi_v1.py`, qui ne juge que, et y ajoute le rôle de proposeur et `PLAFOND_ETAPE_USD`. Les deux fournisseurs passent alors par la porte « environnement » (`O/pole/adaptateurs_v56.py:120-139`).
3. **Configuration et pièces figées** (1,5 à 2 h) :
   - consignes du proposeur (6 fiches), du juge, de l'aiguilleur, du lecteur et de la fusion ;
   - liste fermée de concepts (bras « basique » seul) ;
   - étiquettes interdites et plan de dépense.

   Aucune n'existe dans `course-2/pieces/`.
4. **`course2_nuit_v1.py`** (0,5 h) : sous-classe de `GenerationV56` sans passe « tableau ». Sinon la passe relance les proposeurs (aucun interrupteur).
5. **`trace_agregee_mini_course_v1.py`** (1 h) : agrégateur à liste blanche de clés.
6. **Répétition** en mode simulé, puis `--verifier-seulement` (0,5 h).

## Appels par rôle (scénario B)

| Rôle | Modèle | Appels | Base (USD) | Total (USD) | Durée unitaire |
|---|---|---|---|---|---|
| Proposeur, 6 fiches | Kimi | 1 | 0,36 | 0,36 | 19 min |
| Proposeur, 6 fiches | Argon | 1 | 0,58 | 0,58 | 2 à 3 min |
| Aiguilleur, 12 fiches et 1 fusion | Argon | 13 | 0,10 | 1,30 | moins de 1 min |
| Juges croisés | Kimi et Argon | 13 + 13 | 0,056 et 0,10 | 2,03 | 3 à 4 min et moins de 1 min |
| Lecteurs d'étiquettes | Kimi et Argon | 12 + 12 | 0,056 et 0,10 | 1,87 | idem |
| Metteur en fusion | Argon | 1 | 0,21 | 0,21 | 1 à 2 min |
| Contrôles | Kimi et Argon | 2 | 0,005 | 0,01 | — |
| **Total** | | **68** (Kimi 27, Argon 41) | | **≈ 6,4** | **≈ 2 h 30** |

**Bases de calcul** :
- **Kimi proposeur** : 0,36 USD pour 18 000 jetons d'entrée et 32 000 de sortie (`registres/depenses.md:305`, VÉRIFIÉ). Prix de Kimi : 2 et 10 USD par million de jetons, vérifiés (`collisionneur_v7.py:65-66`).
- **Argon** : 10 et 50 USD par million, prix prudent (`collisionneur_v7.py:62-63`, SUPPOSÉ).
- **Appels courts** : 3 000 jetons d'entrée ; en sortie, 5 000 pour Kimi et 1 500 pour Argon (SUPPOSÉ). Recoupées par `course-2/calcul-devis-course-2-et-pre-pilote-v6.sortie.txt:4` (juge Kimi 0,057 ; juge Argon 0,095 à 10 et 50 ; fusion 0,204).
- **Durées** : 19 min par appel long de Kimi (`depenses.md:306-307`, VÉRIFIÉ). Argon produit environ 65 jetons par seconde (19 039 en 291 s, `depenses.md:295`). Les durées des appels courts sont SUPPOSÉES.

## Scénarios

| Scénario | Appels | Estimé (USD) | Pire cas × 1,5 | Durée | Pire structurel |
|---|---|---|---|---|---|
| A : v56 telle quelle (passe « tableau » non jugée) | 82 | ≈ 8,5 | ≈ 12,8 | ≈ 3 h 10 | ≈ 18 |
| **B : recommandé, sans passe « tableau »** | **68** | **≈ 6,4** | **≈ 9,6** | **≈ 2 h 30** | ≈ 15,8 |
| C : repli, sans bisociateur ni fusion | 40 | ≈ 4,0 | ≈ 6,0 | ≈ 1 h 25 | ≈ 9 |

Le « pire structurel » suppose que chaque appel atteint son plafond de sortie :

| Appel | Plafond de sortie (jetons) |
|---|---|
| Proposeur Kimi | 65 536 |
| Proposeur Argon | 32 000 |
| Appel court de Kimi | 16 000 |
| Appel court d'Argon | 4 000 |

Le plafond dur de chaque étape, tenu par le noyau, coupe avant. **GO proposé : 10 USD pour B, 6 USD pour C.**

## À préenregistrer, puis faire contre-lire par un sous-agent neuf

- **Nature** : démonstration non décisive, sans signe visé (R3), aucun chiffre vers un papier.
- **Critères de lecture gelés** :
  - L1 : fin de la génération, ou arrêt sur un motif codé ;
  - L2 : comptes par étape (fiches proposées et acceptées, classes de l'aiguilleur, refus, verdicts présents et absents) ;
  - L3 : part de fiches « notables » par juge et selon la règle d'agrégation, et accord entre les deux juges ;
  - L4 : écart entre juge de la même famille et juge de l'autre famille. Il est rapporté comme réserve.
- **Liste d'arrêt** : plafond de l'étape atteint ; modèle servi différent ; trois échecs consécutifs ; débordement de la garde Kimi ; signal reçu ; canari dans la trace ; toute autre exception, sans repli.
- **Canaris** :
  - une chaîne unique dans chaque consigne, qui doit être absente de la trace ;
  - une fiche témoin factice, passée en mode simulé ;
  - chaque garde testée sur un cas sain et sur un artefact (R5).
- **Aucune fiche concrète ne sort** :
  - le dossier du run va sous `donnees/`, que `scripts/depot_expurge.py:51` exclut. Il contient `tableaux.json` (titres) et le coffre ;
  - le journal de l'aiguilleur ne copie jamais le contenu (`O/pole/noyau_v54.py:219-272`) ;
  - seul l'agrégateur écrit la trace publique : comptes par étape et par rôle, statuts, coûts, verdicts sous identifiant opaque avec la famille du juge ;
  - un contrôle par programme refuse la trace si elle contient un canari, un titre ou une suite de 6 mots tirée d'une fiche ;
  - la trace est scellée (R6).

## Réserves

- Deux familles seulement : le juge d'une autre lignée n'est pas imposé par le code.
- Le prix d'Argon et la durée des appels courts sont SUPPOSÉS.
- Coupure possible de Kimi après envoi (`depenses.md:300`).
- Départ vers 03 h UTC au plus tôt.
