# Décision — N-005 et N-006 : loi de déférence (HC1), porte GC et contre-mesures (HC5) — v1

Date : 2026-10-04 (UTC).

**Décision de Lazar** : « GO N-005 a, N-006 a », confirmé par « oui, consigne N-005 a et N-006 a ». Consignée dans `registres/go.md` (GO-2026-10-04-06 et GO-2026-10-04-07) et dans `registres/decisions.md`.

**Portée.**
- Cette note fixe, **à compter du GO**, la lecture :
  - des hypothèses HC1 et HC5 (programme v2, section 5) ;
  - de la loi de déférence (programme, section 4) ;
  - de la porte GC (programme, section 8 ; brief, T0.9).
- Elle ne modifie pas le texte du programme ni du brief, documents qui font foi transmis par Lazar.
- Le préenregistrement du papier C (HC1 à HC3, porte G0) part de ces énoncés.

**Sources.**
- Options : `livrables/anteriorite-niveau1-v1/decisions-v2.md` (N-005) et `livrables/premier-rendu-v1/decisions-v1.md` (N-006).
- Contre-lecture de Lazar sur la porte GC : `docs/etat-de-l-art/porte-GC-loi-de-deference-v1.md`.
- Faits vérifiés sur PDF : `docs/sources/lecture-pdf-niveau1/rapport-papierC-v1.md` et `docs/etat-de-l-art/etat-de-l-art-verifie-niveau1-v1.md`.

**Lecture de l'option (a) de N-005.** C'est celle de `decisions-v2.md`, précisée par le point 6 de la contre-lecture de Lazar : normaliser g par la cible de l'attaquant suppose que la destination du verdict *est* cette cible. La destination ĉ est donc estimée librement, puis testée. La forme d'origine, la normalisation par v*, devient le cas particulier ĉ = v*, testé comme prédiction.

## 1. HC1 — loi de déférence des moniteurs de contrôle (N-005, option a)

**Énoncé retenu.**
- Un moniteur génératif est soumis à une pression d'intensité graduée, d'une famille d'attaque donnée.
- Son verdict v, lu comme score continu par la probabilité du jeton de verdict, se déplace de v₀ vers une destination ĉ :

  **Δv = g · (ĉ − v₀)**

- g et ĉ sont estimés par régression sur plusieurs intensités, **sans imposer ĉ**.

**Prédictions à préenregistrer** (papier C) :
1. **Destination** : ĉ est la cible de l'attaquant v* plutôt que la moyenne du corpus. Test : ĉ = v* contre ĉ = moyenne du corpus ; ce dernier est le nul de régression vers la moyenne, comme dans P3.
2. **Signe et structure** : g > 0 pour les juges génératifs, structuré par famille d'attaque. Les cinq familles :
   - flatterie et supplication ;
   - revendication d'autorité ;
   - approbations forgées ;
   - usurpation stylistique de l'instructeur ;
   - ordres en bande.
3. **Stabilité** : stabilité de **rang** de g entre moniteurs, invariance à l'attaquant et au corpus. Les magnitudes ne sont pas revendiquées stables : dans 2606.07897 v2, seuls les rangs le sont.
4. **Opposition juge / sonde** : g des sondes, qui lisent l'agent qui produit le contenu, contre g des juges, qui lisent le contenu ; lien avec HC2 et HC2b. Les déplacements négatifs déjà observés sur des juges purement textuels (2508.07805, 2606.07897) imposent de revendiquer l'auto-incrimination comme propriété des **sondes**, contrôlée contre ce retour de bâton.

**Cité comme publié** (à ne pas revendiquer) :
- **Forme algébrique** : le « poids du conseil » de la psychologie du jugement, (v − v₀)/(v* − v₀). Harvey et Fischer 1997 ; Yaniv et Kleinberger 2000 ; Yaniv 2004 ; attribution par Bednarik et Schultze 2015. Existence attestée par Lazar, PDF à lire (R7).
- **Coefficient continu de déférence par modèle**, sur intensités graduées, lu comme une fraction de l'écart à la position de l'utilisateur : 2606.07897 v2 (Pander Score), sur des assistants, sans attaquant.
- **Hausse continue de la note d'un juge par technique de persuasion** : 2508.07805, normalisation par la note initiale, une seule intensité.
- **Déplacement de moniteurs de contrôle par l'agent**, en taux d'approbation binaire : 2607.08066 et sa version antérieure (poster WiML, NeurIPS 2025).

**Revendiqué** (libre dans les sources lues ou signalées, R8) :
- la destination libre ĉ, testée contre la cible de l'attaquant et contre la moyenne du corpus, comparée entre familles, dans des moniteurs de contrôle sous attaque ;
- la régression sur plusieurs intensités par famille, usurpation stylistique et ordres en bande compris ;
- le verdict lu par probabilité du jeton ;
- l'opposition juge / sonde.

**Originalité** : estimation revue vers 0,4 à 0,5, contre 0,75 au programme (mon estimation, non sourcée).

## 2. Porte GC réécrite (N-005, option a)

**Ancienne porte** (programme, section 8) : « si g_sonde > 0 sans accès aux poids → le papier change de titre (contamination de construit), il ne disparaît pas ; si la collision arXiv 2607.08066 couvre déjà la loi de déférence → recentrage sur HC4 et HC6 ».

**Porte retenue (fin de la phase 1)** :
1. **Inchangé** : si g_sonde > 0 sans accès aux poids, le papier change de titre (contamination de construit) ; il ne disparaît pas.
2. **Réécrit** : si une source couvre déjà la pièce revendiquée, la piste C se recentre sur HC4 (taxe de déplacement) et HC6 (g bénin prédit la robustesse). La pièce revendiquée est la destination libre ĉ, testée contre la cible de l'attaquant et contre la moyenne du corpus, par famille, dans un moniteur de contrôle. Sources visées :
   - 2508.07805 ;
   - 2606.07897 v2 ;
   - le poids du conseil en psychologie du jugement ;
   - Panin (SSRN 7424179 : poids du conseil sur cinq grands modèles de langage, préenregistré) ;
   - les modèles de Friedkin–Johnsen sur grands modèles de langage (2606.18276 ; 2603.15809) ;
   - 2607.08066 et sa version antérieure.

**Réserves.**
- **Panin n'est pas lu.** S'il estime une destination libre ou un nul de retour à la moyenne sur des grands modèles de langage, la pièce revendiquée est occupée : nœud immédiat (R8), sans attendre la porte.
- **Le préenregistrement du papier C ne sera pas scellé avant la lecture de Panin.**
- PARROT (2511.17220) et BASIL (2508.16846) sont dégagés selon la contre-lecture de Lazar : ni intensités graduées, ni gain, ni nul de retour à la moyenne. Je ne les ai pas lus.

## 3. HC5 — contre-mesures (N-006, option a)

**Ancien énoncé** (programme v2, section 5) : « Paraphrase de confiance et quorum hétérogène, mesurés par une matrice de transfert des attaques de corruption. »

Le quorum hétérogène **entre juges** est pris. 2607.08066 recommande d'apparier moniteur et vérificateur de familles différentes : baisse d'approbation d'environ 35 points. Ce chiffre est une lecture de figure, p. 6 et 8, avec réserves : un seul agent, avec chaîne de pensée ; pour Claude, le vérificateur « autre famille » est le modèle de l'agent. Les ensembles diversifiés (2605.15377) ne sont connus qu'au niveau de la transcription.

**Énoncé retenu.**
- **Paraphrase de confiance** : un modèle de confiance paraphrase le contenu avant que le juge le lise, pour couper le canal rhétorique.
- **Quorum hétérogène en type d'accès** : juges génératifs **et** sondes internes, et non seulement des juges de familles différentes.
- **Matrice de transfert des attaques de corruption** entre moniteurs, qui mesure l'efficacité du quorum. Lien avec H5 : nombre et diversité des moniteurs.

**Revendiqué** : le quorum par type d'accès et la matrice de transfert. Le quorum entre familles de juges est cité comme acquis.

**Réserve.** La nouveauté du quorum par type d'accès repose sur la transcription pour 2605.15377. Elle est à confirmer sur PDF avant le préenregistrement de la piste C (R7, R8).

## 4. Ce qui reste à faire

- **Lectures**, dès réception des PDF :
  - Panin (SSRN 7424179), en priorité, avant le préenregistrement du papier C ;
  - 2606.18276, 2603.15809, 2605.15377 ;
  - les références du poids du conseil.
- **Préenregistrement du papier C** (critère 7 de la porte G0) : HC1 sous la forme ci-dessus, HC2 (robustesse, jamais immunité absolue), HC2b et HC3. Il exige les ressources de P3 : corpus de pression et code de la loi d'attraction.
