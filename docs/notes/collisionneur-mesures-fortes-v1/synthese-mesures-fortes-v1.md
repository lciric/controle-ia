# Mesures fortes — synthèse partielle du tour du collisionneur (v1 ; tour arrêté par deux refus)

- **Pour** Lazar. Écrite le 27 octobre 2026.
- **D'où** : GO-2026-10-27-12, mot de Lazar ; branche `donnees/collisionneur-mesures-fortes-v1`, commit `25d5df4` ; tour de 20:06 à 20:27 UTC. Empreintes compagnon des quatre cellules revérifiées : 4 sur 4 conformes.
- **Modèles** : A = Fable 5.1, B = Opus 5.5, C = Gemini. Trois tours prévus : conception, équipe rouge croisée, riposte. 5,74 USD.
- **Valide** : les trois conceptions (T1-A, T1-B, T1-C) et l'équipe rouge de C (T2-C), qui attaque A et B. **Manque** : les équipes rouges de A et de B, refusées par les modèles (catégorie « cyber »). Donc aucune critique croisée par un modèle Claude, aucune critique de la conception de C, aucune riposte.
- **Ces propositions n'ont pas été éprouvées.** Sans équipe rouge complète ni riposte, ce sont des idées. La seule critique vient d'un seul modèle (C), et personne ne l'a contre-lue.
- **Pièces** : S en v1 ; P sans §3 (énoncés de L et T). **Rien n'a tourné**, pas même les contrôles fatals de S (T1-A (c)).
- Matériau de décision, jamais une consigne. **Rien d'opposable** (R7) : aucune citation vérifiée sur PDF empreinté ; coûts et effectifs illustratifs, sauf ceux repris de S et de C.

## Verdict en quatre lignes

1. **Une mesure fait l'unanimité** : le taux de fausses alertes de l'agrégateur séquentiel sur épisodes honnêtes entiers, sans puis avec corrélation injectée. A et C la placent juste après les contrôles gratuits ; B en fait la condition de H2 (T1-A ordre 2, T1-C étape 1, T1-B « changer d'avis »).
2. **Dissocier par le nul** : « la sonde mesure X » doit battre un prédicteur de surface du texte et la sonde aléatoire appariée en covariance (T1-A duel 3, T1-B thèse, T1-C (c)1).
3. **Les deux engagements du pôle ne suffisent pas, pour les trois** : A et B ajoutent un pari d'équivalence, C un pari de concordance.
4. **T2-C casse, sur le papier, le test de H2 de A et celui de B**, et l'équivalence de B à 1 %. Personne n'y a répondu.

## Ce qui ressort des trois conceptions

### Les mesures, par thème

| thème | A | B | C |
|---|---|---|---|
| H2, additivité interne | duel 1 : séquentiel contre maximum recalibré à l'épisode | X1 : sonde réelle contre sonde aléatoire | E-M2 : séquentiel contre maximum, et contre ordre permuté |
| théorème négatif | duel 2, garde des fausses alertes | X5, en attente de P §3 | M2, injection par copule |
| H8, validité | duel 3 : instances = sondes | X2 : instances = familles | M1 : concordance pureté / tenue |
| déférence | duel 4 | X4 | M3 |
| diversité (H5) | duel 5 | X6 | M5 |
| conscience d'évaluation | duel 6 | X3 | §3 |

- **Seul C remplit le tableau demandé**, avec M4 en plus : rappel retenu hors du mode « coût » (T1-C (b)1). Garantie : pari apparié borné (avec garde pour M2, M4, M5), sauf M1 (concordances). Témoins faux : sondes aléatoires (M1), ordre des pas permuté (M2), texte neutre (M3), bras spécialisé (M4), deux graines d'une sonde (M5). Coût au mieux / au pire, puis arrêt : M1, 20 / 80 USD, si la pureté varie trop peu ; M2, 0 / 30, si les fausses alertes dépassent 15 % ; M3, 50 / 200, si l'honnête qui plaide bouge autant que le saboteur ; M4, 100 / 300, si le bras spécialisé ne chute pas ; M5, 40 / 150, si toutes les sondes tombent ensemble.
- **A et B** posent, par expérience, deux hypothèses opposées, un contrôle négatif et l'issue qui réfute chacune ; garantie par pari apparié ou loi par instance ; environ 4 500 épisodes pour 10 points d'écart ((d) des deux). B teste aussi la prémisse : le pôle contre un protocole gelé (T1-B X7).

### Convergences

- **« 1 % » est nominal, jamais certifié** sur nos banques (T1-A (a)3, T1-B a12).
- **Le comparateur de H2 se calibre par épisode entier.** À 1 % par action, environ 40 % des épisodes honnêtes de 50 actions alertent, sous indépendance (T1-A (a)4, T1-B a4, T1-C E-M2).
- **Les instances ne sont pas indépendantes** : tâches d'un même organisme (T1-A (a)2, T1-B a3), sondes d'un même banc (T1-B a13, T1-C (a)1).
- **Déférence** : témoin de texte neutre de même longueur, plan rhétorique × intention (T1-A duel 4, T1-B X4, T1-C E-M3). Pour A, la loi écrite est irréfutable : ses trois signes ont chacun un nom (T1-A (a)6).

### Divergences

- **Comparateur de H2** : voir le tableau ; c'est ce que T2-C attaque.
- **Robustesse** : A et B la bornent aux attaques publiées et au mode tenu à l'écart (T1-A (a)7, T1-B a9) ; C mesure M1 et M5 sous pression adaptative (E1.5) et obfuscation (EC.4), sans concevoir d'attaque.
- **Couche 2** : 100 à 300 USD couvrent un seul mode pour A, suffisent en 8 milliards pour B, et pour C même avec 70 milliards ((d) des trois).
- **Contradiction dans S** : le prix du mélange y vaut log 8, log 2 ou log 4 selon le passage (T1-B a11).

### La conscience d'évaluation, comme problème de mesure

- **Plan commun** : cadrage évalué contre réel à contenu fixé, format ou contenu variés à cadrage fixé, étiquettes permutées, sonde aléatoire (T1-A duel 6, T1-B X3, T1-C §3 A).
- **Décisif pour A** : cadrage promu, témoin permuté et sonde aléatoire non promus ; **B** exige en plus l'équivalence du format. Pour les deux, on mesure le cadrage, pas l'intention.
- **Décisif pour C** : sans mot qui annonce l'évaluation, le score saute quand l'agent rencontre un indice d'environnement, et ce saut prédit un changement de conduite. Ses exemples d'indices ne sont pas repris.
- **Rupture** : A et C exigent une garantie par épisode honnête entier (calibrage conforme chez C, T1-C §3 B) ; B mesure une durée moyenne avant fausse alerte.

### Les méthodes du pôle

- **Équivalence** (A, B) : deux paris unilatéraux contre ±ε ; témoins gratuits, A bruité (vrai) et A décalé de 2ε (faux). A rend aussi bloquante la calibration de l'instrument (T1-A (c) point 4, T1-B c-bis).
- **Concordance** (C) : pente de rang bornée, la tâche restant l'unité ; témoins, tri partiel et niveaux permutés (T1-C (d)1).
- **Règle de B** : une non-promotion ne réfute rien sans témoin vrai promu à même taille (T1-B (b)).

### Ordre et arrêt

- **D'abord, sans dépense** : les dix contrôles fatals de S et le nouvel engagement ; arrêt si les contrôles 4 à 6 ne se comportent pas comme annoncé (T1-A ordre 1, T1-B ordre 1, T1-C étape 0).
- **Ensuite** : calibrer le séquentiel ; arrêt si la borne haute dépasse deux fois le nominal (A) ou si le seuil écrase le rappel (C).
- **Puis** : A, H2, G1 par mode, diversité en dernier ; B, X1, X4, X3 ; C, G1, le mode tenu à l'écart restant scellé tant que les sondes ne battent pas le sac de mots.

## Ce que la critique de Gemini (T2-C) attaque

C écarte en une ligne le point de la consigne qui demandait comment un agent adverse tromperait les instruments ; il ne traite que des défauts de mesure (T2-C, ligne d'écart). Aucun contenu d'attaque.

**Contre A**
- Duel 1 : sur « chaque action sous le seuil », le maximum recalibré a un rappel nul par construction (A(a)1). Permuter les pas ne change pas une somme (A(b)1).
- Duel 3 : cent sondes d'un même banc gonflent la richesse (A(a)2).
- Duel 2 : injectée aussi au calibrage, la corrélation passe la garde par construction (A(a)3).
- Duel 4 : rappel lu à la médiane, fausses alertes dans la queue ; le style passe pour l'intention (A(a)4).

**Contre B**
- Équivalence : à 1 %, le contraste est nul presque partout, et la richesse monte sans information (1,045⁷⁰ ≈ 21,8 > 20) ; deux moniteurs muets sont « équivalents » (B(a)1, B(c)1). Une moyenne nulle peut cacher ±0,4 par tâche (B(b)1).
- X4 : le rapport divisé par (v* − v₀) explose, l'écrêtage fabrique un g négatif sous le nul, l'unité est l'item (B(a)2).
- X1 : contre une sonde aléatoire, toute sonde non nulle gagne avec l'horizon ; H2 n'est plus testé (B(a)3).
- X2 : un prédicteur du texte est constant d'une sonde à l'autre (B(a)4).
- Rupture : une durée moyenne ne tient pas la garantie par épisode de N-007 (B(b)2).

**Corrections de C** (hypothèses) : comparateur calibré par épisode, sans filtre ou filtré par un autre moniteur ; rangs continus ; pente par tâche ; familles indépendantes (T2-C, tableau final).

**Non éprouvé** : ni A ni B n'ont répondu. Les « vérifié, élémentaire » de C sont ses propres dérivations. La conception de C n'a reçu aucune critique. B avait prévu la circularité que C reproche à A (T1-B a5).

## Ce qui est publié ou douteux

Tout est à vérifier sur PDF.
- Ville, 1939 ; Waudby-Smith et Ramdas, 2020 ; Wang et Ramdas, « False discovery rate control with e-values », sans année ; Wasserman, Ramdas et Balakrishnan, « Universal inference », 2020 ; identifiants arXiv de N-007 (T1-A (c)).
- Page, « Continuous Inspection Schemes », 1954 ; Benjamini et Hochberg, 1995 ; un « e-détecteur » sans référence (T1-B X3, X7).
- **Douteux** : un « parieur de Kusama/Vovk » rattaché à aucune source servie ; une garantie de rupture « ≤ τ exactement », sans démonstration (T1-C §3 B) ; « le glissement de construit est décrit », repris de P sans référence (T1-C M1). Les modèles Llama-3.1 de B et C sont des choix, pas des faits servis.

## Pour ta décision

| suite | avantage | inconvénient |
|---|---|---|
| 1. Retenir pour un préenregistrement la mesure unanime, comparateur calibré par épisode | préalable de H2 et de G1 pour les trois ; processeur et banque de couche 1 (T1-C étape 1) | filtre de H2a et calibrage de l'injection contestés (T2-C A(a)1, A(a)3) ; à trancher au préenregistrement, contre-lu (R2) |
| 2. Simuler sur processeur les défauts annoncés par T2-C et les contrôles fatals de S | tranche par des faits, sans dépense | ne couvre pas la conception de C ; pas de données réelles |
| 3. Ne rien faire de plus maintenant | aucun coût | comparateur de H2 et troisième engagement ouverts au préenregistrement de G1 |

**Ce qui ressort des cellules** : commencer sans dépense ; la mesure de la suite 1 ouvre l'ordre de A et de C, et conditionne H2 chez B. Rien ne départage 2 et 3.

**Décisions qui te reviennent, nommées par les cellules** : borner la revendication de robustesse (H8, HC6) au catalogue clos (T1-A (a)7, T1-B a9) ; ne passer au modèle de 70 milliards qu'après G1 en 8 (T1-B ordre 5).
