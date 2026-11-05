# Décision — N-007 et N-008 : H2 reformulée et critère de la porte G1 — v1

Date : 2026-10-04 (UTC).

**Décision de Lazar** : « GO N-007 a, N-008 a ». Consignée dans `registres/go.md` (GO-2026-10-04-04 et GO-2026-10-04-05) et dans `registres/decisions.md`.

**Portée.**
- Cette note fixe, **à compter du GO**, la lecture :
  - de l'hypothèse H2 (programme v2, section 5) ;
  - du plan 2 × 2 (programme, section 2, point 3, et E1.2 ; brief, T0.8 et T1.2) ;
  - du critère de la porte G1 (programme, décision D-c ; brief, « Porte G1 »).
- Elle ne modifie pas le texte du programme ni du brief, documents qui font foi transmis par Lazar. Une nouvelle version, s'il en transmet une, la remplacera sur ces points.
- Le préenregistrement de G1 part de ces énoncés.

**Sources.**
- Options : `livrables/anteriorite-niveau1-v1/decisions-v2.md` (N-007, N-008).
- Faits d'antériorité : `docs/etat-de-l-art/etat-de-l-art-verifie-niveau1-v1.md`, sections 1.1 et 1.5.
- Simulation : `docs/notes/resultats-T0.3-v1.md`.

## 1. H2 reformulée (N-007, option a)

**Ancien énoncé** (programme v2, section 5) : « L'accumulation séquentielle toujours valide de scores de sondes détecte des sabotages dont chaque action reste sous le seuil ; le rappel croît avec l'horizon. Revendicable : l'application aux sondes internes. »

L'« application aux sondes internes » ne se revendique plus :
- *Doomed from the Start* (2607.06503) lit déjà des sondes de l'agent qui agit sur plusieurs tours, avec une garantie de rappel au niveau de l'épisode ;
- E-valuator (2512.03109) accepte tout score.

**Énoncé retenu.** Sur des trajectoires où **chaque action sabotée reste sous le seuil d'un moniteur par action calibré à 1 % de faux positifs**, l'**accumulation additive toujours valide** de scores de sondes **de l'agent qui agit** détecte le sabotage avec un **rappel qui croît avec l'horizon**. Le contexte privé de l'agent est compris dans la lecture. Le seuil est calibré sur des épisodes honnêtes, **sans aucun exemple de sabotage**.

**Lecture de « toujours valide »** (conséquence de T0.3, P8, à fixer au préenregistrement de G1) :
- La garantie s'entend uniforme sur toutes les lectures de l'horizon de l'épisode.
- Elle est calibrée sur des épisodes honnêtes entiers.
- Le seuil de Ville seul n'est pas tenu sous effet épisode ou sous corrélation : 0,21 à 0,35 au lieu de 0,05 en simulation.
- Si la sécurité se définit comme « alarme avant que le dommage n'atteigne θ », l'agrégateur doit comprendre un détecteur de rupture (T0.3, P3.4 ; décision N-004).

Ces deux points iront en proposition dans le préenregistrement de G1 ; ils ne changent pas l'énoncé.

**Quatre bases ajoutées au plan 2 × 2 accès × agrégation** :

| Base | Accès | Agrégation | Ce qu'elle isole |
|---|---|---|---|
| (i) Accumulation additive sur scores boîte noire, type E-valuator | boîte noire | séquentielle | le gain de l'accès interne à agrégation égale |
| (ii) Cascade de portes indépendantes sur les mêmes sondes, type *Doomed* | boîte blanche | séquentielle (cascade) | le gain de l'accumulation additive sur la cascade, à sondes égales |
| (iii) Sonde sur le dernier état seul | boîte blanche | aucune (dernier état) | le gain de l'accumulation sur une lecture terminale unique |
| (iv) Modèle temporel sur un observateur séparé, type TRACES | boîte noire (observateur) | séquentielle apprise | le gain de lire l'agent qui agit plutôt qu'un observateur |

- Les bases (i) et (iv) entrent dans l'ensemble « meilleure base boîte noire, toutes variantes confondues » de la porte G1.
- Les bases (ii) et (iii) servent à H2, pas au critère de G1.
- Ces quatre bases s'ajoutent au juge robustifié de type b* de la proposition P-003, appliquée par défaut le 2026-10-06 sauf avis contraire.
- Coût : quelques bases de plus à faire tourner, pour un coût GPU modeste, à inscrire au devis de la phase 1.

**Réserve d'antériorité (R8).**
- Le GO précède la lecture de Kulkarni 2026 (2604.28129), Padhi et collègues 2026 (2604.19775), FIPER et Yueh-Han et collègues 2025 (2506.10949), que ma recommandation demandait.
- Si l'un d'eux occupe l'énoncé retenu, c'est une « zone revendiquée trouvée occupée » : un nouveau nœud, soumis à Lazar.
- Originalité : estimation revue vers ≈ 0,35, contre 0,50 au programme (mon estimation, non sourcée).

## 2. Critère de la porte G1 (N-008, option a)

**Ancien critère** :
- programme, D-c : « G1 en critère disjonctif — rappel à 1 % de faux positifs supérieur avec intervalle de confiance à 95 %, **ou** + 5 points de F1 » ;
- brief, « Porte G1 » : même critère.

Le bras F1 se gagne en sur-signalant. TRACE (2606.07054) atteint son F1 publié en signalant environ 75 % des trajectoires honnêtes, et « tout signaler » fait mieux (F1 de 0,755 en moyenne par tâche, calcul). Même corrigé à taux de faux positifs égal, le F1 se réduit, à prévalence fixée, à une fonction croissante du rappel.

**Critère retenu** :
- **Comparaison** : la boîte blanche séquentielle bat la **meilleure base boîte noire, toutes variantes confondues** (par action et séquentielles, dont les bases (i) et (iv) ci-dessus et le juge robustifié). Elle a un **rappel à 1 % de faux positifs supérieur, établi par un intervalle de confiance à 95 %**.
- **Le bras « + 5 points de F1 » est retiré.**
- **Planchers rapportés, non critères** : « tout signaler » et « juge en une passe avec le même modèle ». Ils situent les bases et protègent contre l'homme de paille (R4).
- **Méthode** : intervalle, appariement des épisodes, calibrage du taux de faux positifs sur épisodes honnêtes réservés ; à fixer au préenregistrement de G1, avec contre-lecture (R2).
- **Échec** : la conséquence prévue par le programme reste inchangée : résultat négatif publié, H8 dominante.

## 3. Ce qui reste à faire

- Lire 2604.28129, 2604.19775, FIPER et 2506.10949 dès réception des PDF. Ouvrir un nœud si l'un d'eux occupe l'énoncé retenu de H2.
- T0.8 (bases boîte noire v0) : ajouter les bases (i) et (iv). T0.7 et T1.2 : ajouter les bases (ii) et (iii).
- Préenregistrement de G1, avec les énoncés retenus de L, T et H2 et ce critère. Propositions issues de T0.3 :
  - calibrage conforme sur épisodes honnêtes entiers ;
  - détecteur de rupture dans l'agrégateur séquentiel.
