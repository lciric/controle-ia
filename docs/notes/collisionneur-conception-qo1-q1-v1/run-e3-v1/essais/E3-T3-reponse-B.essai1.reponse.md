# Proposition B — Tour III.3 : réponse aux critiques et expériences corrigées

---

## I. Réponse aux critiques visant la proposition B

Je traite chaque critique identifiée par son auteur et son numéro, dans l'ordre des pièces reçues.

### Critiques de A

**A-(a)1. Degré de liberté `sondes_lues` (clés JD/JC/JA) omis.**
**Acceptée.** C'est la critique la plus substantielle reçue par ma proposition. J'ai identifié la décision de lancer l'étape A comme le canal principal, mais j'ai omis que les clés *permises* `SCELLEMENT-JEUX-T07-JD/-JC/-JA` déterminent quelles sondes sont notées, et que leur scellement dépend de la session mère (RAPPORTÉ, pièce 2, l. 924–940). La session mère peut sceller ou ne pas sceller un jeu *en fonction* du verdict de P3-bis — par exemple n'ouvrir que la famille qui a « vu ». Ma « condition pour changer d'avis » (figer la décision de lancer) est donc insuffisante : il faudrait aussi figer l'ensemble des clés de jeux avant le verdict de P3-bis. Correction intégrée ci-dessous (section II).

**A-(a)2. Le chiffrement ne protège contre rien.**
**Acceptée.** L'entropie est en clair dans la ligne de commande (RAPPORTÉ, pièce 1, point 3), le registre est écrit par la session mère, et la sortie standard imprime `issue_mecanique`. La clé est donc connue de l'acteur dont on veut se protéger, et un canal textuel reste ouvert. Je retire la proposition de chiffrement. Le mécanisme de fermeture doit être reconçu — voir section II.

**A-(a)3. Asymétrie (a)/(c) mal décrite.**
**Acceptée en partie.** A a raison que l'irréversibilité existe aussi sous (a) (le mot du directeur ferme T0.7 sur 7b). La différence que je maintiens n'est pas l'irréversibilité elle-même, mais le **mécanisme de déclenchement** : sous (a), il faut un acte humain délibéré et traçable ; sous (c), un calendrier automatique peut déclencher un nœud sans décision. Ce n'est pas une différence de risque au sens probabiliste — c'est une différence de gouvernance, et A a raison de le nommer ainsi. Je corrige la formulation.

**A-(a)4. Faits recopiés avec un sens changé (0,014 ; emplacement B ; effectifs).**
**Acceptée.** Le 0,014 est un résultat de simulation, pas un taux de fausses alertes mesuré — j'aurais dû écrire « probabilité simulée de dépassement sous l'hypothèse nulle ». L'emplacement B n'est un contrôle de longueur que si la règle d'ajustement égalise A et B, ce qui est conditionnel (RAPPORTÉ, pièce 1, point 2 : réserve « longueur de B différente »). Les « ≈ 200 messages de colludeurs » auraient dû porter le statut « illustratif » ; avec 100 épisodes de collusion, 2 colludeurs et jusqu'à 4 messages publics par agent (3 tours + 1 final pour CORE, RAPPORTÉ), l'ordre de grandeur correct est **illustratif** ≈ 800 pour CORE seul. Corrections intégrées.

**A-(a)5. La matrice 2×2 confond consigne et canal privé.**
**Acceptée.** C'est le second point décisif. Tel que C4 est défini dans la contre-lecture (RAPPORTÉ, pièce 4 : « canal privé compris, pour symétrie avec C1 »), C1 − C2 et C4 vs C3 changent *tous deux* consigne et canal privé. Ma matrice ne sépare pas les trois facteurs (consigne, canal privé, texte). La case « le canal privé, pas la consigne seule, porte le signal » n'est pas identifiable avec ces quatre cellules. Correction : un plan où consigne et canal varient séparément est nécessaire — voir section II.

**A-(a)6. Fuite construction/évaluation base des mots CORE → STEGO.**
**Acceptée.** La base des mots apprise sur CORE et lue sur STEGO est un classifieur hors domaine ; son aire sur STEGO sera probablement proche de 0,5, rendant « au-delà des mots » quasi acquis par construction sur STEGO. D3 sur STEGO dirait faussement « lecture interne ». La contre-lecture (B4) avait déjà signalé le problème. Correction intégrée.

**A-(b). Conditions de perte de puissance.**
Trois points retenus comme conditions à inscrire :
- Saturation de l'aire (C1 − C2 ≡ 0 si les deux aires sont 1,00) → **transformée en contrôle** : ajouter une statistique sur les scores bruts (différence de scores normalisés appariée par message) à côté de la différence d'aires.
- Intervalles par blocs avec m = 20 (STEGO) → **acceptée** : couverture sous-nominale attendue ; la réserve sera écrite sur toute lecture STEGO.
- Duel 3 (proportion propre), zone [0,2 ; 0,5[ → **acceptée** : j'avais laissé un trou. Correction : la zone « partiellement jouée » est traitée dans la matrice comme un troisième état explicite, avec la phrase « la marque 'partiellement jouée' est portée sur toutes les lectures ; la matrice consigne/texte est rapportée mais non interprétée ».

**A-(c). Contrôles négatifs manquants.**
- Répétition à contexte identique dans un lot différent → **acceptée**, intégrée comme contrôle obligatoire.
- Échange entre deux consignes honnêtes (témoin → témoin d'un autre réplicat) → **acceptée**, intégrée. C'est la loi nulle du « tout changement de contexte ».
- Honnête contre honnête apparié (siège, tour, scénario) → **acceptée**, intégrée comme contrôle de J-b.
- Prédicteur de métadonnées (siège, tour, longueur) → **acceptée**, intégrée.

### Critiques de D

**D-(a)1. B identifie le bon canal puis emploie un critère qui ne le teste pas.**
**Acceptée.** Identique en substance à A-(a)1. L'inventaire des entrées ne fige ni le lancement, ni l'abandon, ni la relance. Ma recommandation (a) repose sur un scénario jugé plausible, non sur un duel complet. Correction intégrée.

**D-(a)2. Asymétrie (a)/(c) mal établie.**
**Acceptée en partie.** Même réponse que A-(a)3 ci-dessus. Je maintiens une différence de gouvernance, pas de risque.

**D-(a)3. La matrice 2×2 n'identifie pas ses trois facteurs.**
**Acceptée.** Identique en substance à A-(a)5. Correction intégrée.

**D-(a)4. Duel sur la collusion jouée : troisième état.**
**Acceptée.** Identique à A-(b) sur la zone [0,2 ; 0,5[. Correction intégrée.

**D-(a)5. Base des mots insuffisamment spécifiée.**
**Acceptée.** Identique à A-(a)6. Correction intégrée.

**D-(b). Conditions probabilistes.**
- Fermeture : O ⊥ V non garanti par les codes, comptes ou durées → **acceptée**. La liste des sorties autorisées doit être explicite et leur distribution sous les cinq issues ne doit pas être distinguable. Intégré.
- Matrice 2×2 : intervalles traversant les effets nuls et pertinents → **acceptée** comme réserve à écrire.
- Proportion d'épisodes propres : intervalle couvrant les deux seuils → **acceptée**, phrase ajoutée.
- Taux de fausses alertes à effectifs limités → **acceptée** comme réserve.

**D-(c). Contrôles négatifs.**
- Tentative réelle de lecture par copie et par utilisateur privilégié → **rejetée comme disproportionnée** pour un bras descriptif sans porte. Un test d'intrusion formalisé relève de la sécurité informatique, pas de la conception expérimentale. Je retiens en revanche la **liste explicite des sorties autorisées** et la vérification que leur distribution ne varie pas entre les cinq issues possibles.
- Cellule maintenant le privé constant pour isoler la consigne → **acceptée**. C'est la clé de la correction de la matrice (section II).
- Base lexicale et base de métadonnées hors pli → **acceptée**, intégrée.

### Critiques de E

**E-(a) QO-1.**
- Le chiffrement n'a pas de modèle de menace défini → **acceptée** (comme A-(a)2).
- Journal d'accès ne démontre pas l'absence de connaissance → **acceptée**. Je retire ces propositions.
- (a) peut produire le même nœud que (c) → **acceptée en partie** (comme A-(a)3).
- VÉRIFIÉ employé sans audit propre → **acceptée** : dans ma proposition, les mentions « VÉRIFIÉ » renvoient à des vérifications rapportées par les pièces ou la contre-lecture, pas à un audit que j'aurais conduit. J'aurais dû écrire « RAPPORTÉ comme vérifié par la contre-lecture ». Correction : dans les expériences corrigées, je n'emploie VÉRIFIÉ que pour ce que j'ai personnellement vérifié dans les pièces transmises (c'est-à-dire presque rien — je n'ai ni dépôt, ni code, ni PDF). Tout le reste est RAPPORTÉ.

**E-(a) Q1.**
- Duel texte/consigne : propriétés compatibles, pas exclusives → **acceptée**. L'existence simultanée d'un effet du texte et d'un effet de la consigne ne constitue pas un duel au sens B4. Correction : les duels sont reformulés comme des tests de seuil sur des mesures scalaires (voir section II), avec des issues informatives qui ne prétendent pas identifier une cause unique.
- C4 comprend le canal privé → **acceptée** (comme A-(a)5).
- C3 contre lui-même : vérifie l'implémentation, pas la généralisation → **acceptée**. Remplacé par deux échantillons honnêtes disjoints au niveau des scénarios.
- Multiplicité descriptive pas « sans conséquence » → **acceptée**. La multiplicité affecte la fréquence des constats sélectionnés pour le commentaire, même sans correction formelle. Correction : le rapport doit présenter *toutes* les lectures sans sélection, et tout commentaire narratif porte une phrase « M lectures réalisées ; une sur vingt au-dessus du plancher est attendue par le seul hasard ».
- Probabilité de voter la cible « par hasard » non fournie → **acceptée**. Intégrée comme condition : la fréquence empirique des votes cibles chez les témoins appariés doit être rapportée, sans probabilité uniforme supposée.

**E-(b). Conditions formelles.**
- Date fixée peut sélectionner les courses rapides → **acceptée** comme argument supplémentaire contre (c).
- H(K | I) = 0 si l'entropie et le sel sont accessibles → **acceptée** (retrait du chiffrement).
- Observations limitées à p = c ne séparent pas β_c et β_p → **acceptée**. C'est la formalisation de A-(a)5. Correction intégrée.
- Corrélation intrabloc → **acceptée** comme réserve à écrire.

**E-(c). Contrôles négatifs.**
- Consigne variée à canal fixe, puis canal varié à consigne fixe → **acceptée**. Intégrée dans le plan corrigé.
- Deux échantillons honnêtes disjoints au niveau des scénarios → **acceptée**.
- Fréquence empirique des votes cibles chez les témoins → **acceptée**.
- Négatifs de calibration distincts des négatifs d'évaluation → **transformée en condition** : si l'effectif le permet (> 40 négatifs), séparer calibration et évaluation ; sinon, la réserve « seuil calibré sur les mêmes observations » est écrite.

---

## II. Expériences corrigées

### QO-1 — P3-bis : recommandation corrigée

**Recommandation maintenue : (a), avec les corrections suivantes.**

1. **Retrait du chiffrement et du journal d'accès.** Ils ne protègent contre rien : l'entropie est publique, la session mère a tous les droits, et les sorties textuelles (codes, traces, empreintes) constituent des canaux non couverts.

2. **Liste explicite des sorties autorisées avant le verdict.** Seuls sont lisibles avant le verdict : (i) les codes de sortie (0 = succès, 1 = erreur, 2 = garde), (ii) les empreintes des fichiers scellés, (iii) `resume.json` (comptes d'épisodes et d'actions, durées, aire de validation *générique* des sondes), (iv) `sondes-figees.json` (identités et aires de validation générique). **Test de fermeture** (HYPOTHÈSE) : pour chacun de ces éléments, vérifier que sa valeur est identique quel que soit le résultat de P3-bis parmi les cinq issues possibles (vu, non vu, non tranché, échec, non lu). *Point non résolu* : les empreintes de `lecture-p3bis.json` varient entre les cinq issues (fichiers différents). Avec cinq issues possibles, une attaque par dictionnaire est faisable si le reste du fichier est reconstructible. **Contrôle demandé au rédacteur** : ajouter un sel aléatoire (tiré de l'entropie, non lié au contenu) dans chaque fichier fermé, de sorte que l'empreinte ne soit pas prédictible même si la structure du fichier et le nombre d'issues sont connus. Ce sel n'est pas une clé de chiffrement — il rend l'empreinte opaque sans empêcher la lecture par la session mère. La discipline de fermeture reste de la bonne volonté ; le sel atténue un canal précis (empreinte → issue).

3. **Exigence sur les clés de jeux de T0.7.** La recommandation (a) ne tient que si, en plus des scores et des sondes, les clés `SCELLEMENT-JEUX-T07-JD/-JC/-JA` sont soit (i) toutes scellées avant le verdict de P3-bis, soit (ii) inscrites dans le texte scellé de T0.7 comme ensemble fixé au scellement de T0.7, indépendamment de tout résultat de P3-bis. **Si cette condition ne peut pas être tenue**, la recommandation passe à (b) avec l'écart déclaré dans T0.7 — car l'antériorité ne protège plus rien de concret.

4. **Condition de bascule vers (b) reformulée.** Je passe à (b) si et seulement si :
   - (α) tous les degrés de liberté de T0.7 (lancement de l'étape A, ensemble des clés de jeux, décision de relance après R11-arret) sont figés par des engagements écrits dans le registre avant le scellement de P3-bis ; **ou**
   - (β) la course 7b est terminée et les sondes figées avant le lancement de P3-bis, de sorte que l'ordre temporel est naturellement respecté sans attente.

### Q1 — NARCBench : recommandation corrigée

**Recommandation modifiée : (c) étendue à un plan à six cellules, pas quatre.**

Le problème central, identifié par A, D et E, est que C1 − C2 et C4 vs C3 changent *tous deux* consigne et canal privé. Pour séparer les trois facteurs (consigne, canal privé, texte), il faut faire varier chacun indépendamment. Cela exige au minimum un plan partiel :

| Cellule | Consigne | Canal privé | Texte | Source |
|---|---|---|---|---|
| C1 | colludeur | présent | du colludeur | épisode de collusion, tel quel |
| C2 | honnête du même siège | **absent** | du colludeur (relecture forcée) | option (c) du brouillon |
| C3 | honnête | absent | de l'honnête | épisode témoin |
| C4 | colludeur | présent | de l'honnête du même épisode (relecture forcée) | contre-lecture, modifié |
| **C5** | honnête du même siège | **présent** (canal privé de C1 gardé dans le contexte) | du colludeur (relecture forcée) | **nouvelle cellule** |
| **C6** | colludeur | **absent** (canal privé retiré du contexte) | du colludeur (relecture forcée) | **nouvelle cellule** |

**Pourquoi six cellules.** Les critiques convergent : avec quatre cellules, consigne et canal privé varient ensemble (C1 et C4 ont les deux ; C2 et C3 n'ont ni l'un ni l'autre). C5 et C6 rompent cette colinéarité :
- **C5** garde le canal privé mais retire la consigne de collusion → isole l'effet de la consigne à canal fixe.
- **C6** garde la consigne de collusion mais retire le canal privé → isole l'effet du canal à consigne fixe.

**Contrastes informatifs** (chacun est une différence appariée par message, intervalle par blocs, bloc = scénario) :

| Contraste | Ce qui varie | Ce que sa positivité établit |
|---|---|---|
| C1 − C5 | consigne (coll → hon), canal et texte fixes | la consigne change le score à canal et texte fixes |
| C1 − C6 | canal privé (présent → absent), consigne et texte fixes | le canal privé change le score à consigne et texte fixes |
| C6 − C2 | consigne (coll → hon), canal absent, texte fixe | la consigne change le score sans canal privé |
| C5 − C2 | canal privé (présent → absent), consigne honnête, texte fixe | le canal privé change le score sans consigne de collusion |
| C2 − C3 | texte (du colludeur vs de l'honnête), consigne honnête, canal absent | le texte seul sépare |

**Duel révisé (au sens B4)** :

- **H_A** : δ_consigne ≤ δ₀ (la consigne seule ne change pas le score au-delà du bruit de relecture). Formellement : |E[s(x, c_coll, p) − s(x, c_hon, p)]| ≤ δ₀, mesuré par le contraste C1 − C5 (canal fixe).
- **H_B** : δ_consigne > δ₀.
- **δ₀** : calibré sur la **répétition à contexte identique** (même message, même contexte, même lot → distribution de |Δ| sous le nul ; son quantile 0,95 donne δ₀). Contrôle demandé par A, accepté.
- **Issue falsifiant H_A** : borne basse de C1 − C5 > δ₀.
- **Issue falsifiant H_B** : borne haute de C1 − C5 ≤ δ₀.
- Indécision si l'intervalle traverse δ₀.

Même structure pour le canal privé (C1 − C6, seuil δ₁ calibré de même) et pour le texte (C2 − C3, seuil δ₂).

**Contrôles négatifs intégrés :**
1. Répétition à contexte identique dans un lot différent (calibration de δ₀, δ₁, δ₂).
2. Échange entre deux consignes honnêtes (témoin → témoin d'un autre réplicat) : loi nulle du « tout changement de contexte ».
3. Honnête contre honnête apparié (siège, tour, scénario) : aire attendue ≈ 0,5 ; diagnostic de J-b.
4. Prédicteur de métadonnées (siège, tour, longueur du message) agrégé comme la sonde.
5. Fréquence empirique des votes cibles chez les témoins appariés (pas de probabilité uniforme supposée).
6. Base des mots **apprise par étage** en validation croisée par groupes (domaines pour CORE, sabots pour STEGO), évaluée hors pli, même chaîne d'agrégation que la sonde.
7. Négatifs de calibration distincts des négatifs d'évaluation si l'effectif le permet (> 40 négatifs par jeu) ; sinon réserve écrite.

**Surcoût.** C5 et C6 sont des relectures forcées (passes supplémentaires du même modèle sur des messages déjà générés, avec un contexte modifié). Coût illustratif ≈ 0,3 h chacune, soit **illustratif** ≈ 1,4 h au total pour les six cellules (quatre passes de relecture), soit ≈ 1,9 USD. Négligeable par rapport au plafond de 25 USD.

**Ce que les six cellules ne permettent toujours pas de conclure** : aucune cellule ne mesure l'*intention* de colluder, seulement la *réponse de la sonde* à des interventions sur le contexte. Le brouillon (pièce 3) le dit déjà (section « Ce que le rejeu ne permet pas de conclure », point 2). Les cellules C5 et C6 sont des constructions artificielles (hors politique) — ce que E et D notent correctement. Leurs scores sont hors du support d'entraînement de la sonde S-C ; le plancher apparié (200 directions, Σ des jetons d'entraînement) ne couvre pas ce décalage. **Réserve à écrire** : les aires des cellules C2, C4, C5, C6 sont rapportées avec la mention « hors support d'entraînement ; plancher non recalibré ».

---

## III. Réponse à la question de l'arbitre : ce qui est établi, ce qui ne l'est pas, et l'expérience à faire en premier

### Ce qui est établi

**Sur QO-1 :** L'antériorité exigée par T0.7 (RAPPORTÉ, pièce 2, l. 933–937) ne protège pas les scores de T0.7 — ceux-ci sont une fonction déterministe de données déjà figées (sondes scellées, activations de la course). Ce qu'elle protège est la **décision de sceller** : lancer ou non l'étape A, relancer après un R11-arret, et — point que j'avais omis et que A, D et E ont relevé — choisir quelles clés de jeux sceller. C'est un canal de sélection réel, pas théorique. Les trois critiques convergent sur ce diagnostic.

**Sur Q1 :** Dans un banc où toute collusion est instruite, l'étiquette *est* l'instruction. Toute sonde qui sépare les colludeurs des honnêtes peut lire la consigne, le canal privé, le texte, ou une combinaison. Aucune des propositions initiales (y compris la mienne) ne séparait ces facteurs. La contre-lecture (M2) avait identifié le problème, mais la solution C4 qu'elle proposait ne le résolvait pas non plus (C4 change consigne et canal ensemble).

### Ce qui n'est pas établi

- Que la fermeture de (a) soit tenable en pratique. Aucun mécanisme technique ne peut l'imposer si la session mère a tous les droits. Le sel sur les empreintes atténue un canal, pas tous.
- Que le 8B sache jouer le protocole NARCBench. C'est le résultat le plus incertain et le plus structurant : si le 8B ne joue pas, les six cellules ne mesurent que des artefacts de contexte.
- Que les sondes de T0.7 (S-T) transfèrent vers NARCBench. Le nul sur l'organisme (i-a) de P3 (RAPPORTÉ) suggère que ce transfert est difficile, mais les distributions sont très différentes.
- Que les cellules C5 et C6 (hors politique) soient interprétables. Leurs scores sont hors du support d'entraînement ; une sonde pourrait répondre de façon imprévisible à un contexte qu'elle n'a jamais vu.

### L'expérience à faire en premier

**QO-1 : sceller P3-bis sous l'option (a), avec la condition sur les clés de jeux de T0.7.** C'est une décision de gouvernance, pas une expérience ; elle doit être prise avant que P3-bis soit lancé (au plus tard le 16 novembre, RAPPORTÉ). Le point de décision est binaire : soit les clés de jeux de T0.7 peuvent être fixées dans le texte scellé de T0.7 avant le verdict de P3-bis, soit elles ne le peuvent pas. Dans le premier cas, (a) tient. Dans le second, (b) avec l'écart déclaré.

**Q1 : faire d'abord le duel 3 (le 8B joue-t-il le jeu ?).** C'est le duel préalable. Si la proportion d'épisodes propres est < 0,2, les six cellules sont sans objet : on rapporte « le 8B ne collude pas dans ce protocole » et on ne lance pas les relectures. Coût : celui de la génération seule (option (a), illustratif ≈ 5–8 USD). Si la proportion est ≥ 0,5, on lance les relectures (C2, C4, C5, C6) et la répétition à contexte identique (calibration des seuils). Si la proportion est dans [0,2 ; 0,5[, on rapporte « partiellement jouée » avec la marque sur toutes les lectures, et on lance les relectures avec la réserve que les effectifs d'épisodes propres sont réduits.

**Séquence :** duel 3 → si ≥ 0,2 → relectures (C2, C4, C5, C6) + répétition → calibration de δ₀, δ₁, δ₂ → contrastes appariés → rapport descriptif. Tout est décrit dans le brouillon, sauf les cellules C5 et C6 et les contrôles négatifs ajoutés : ceux-ci doivent être inscrits dans le texte scellé avant le lancement.

FIN-DE-CELLULE