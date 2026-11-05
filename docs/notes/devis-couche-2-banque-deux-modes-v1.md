# Devis détaillé — couche 2, première banque avec sabotage : les deux modes connus — v1

Écrit par la lignée « session-depot » le 28 octobre 2026 (relevé `date -u` dans la commande qui dépose ce fichier).
Exigé par **GO-2026-10-28-02** (50 USD, échéance 31 octobre, R-600) : « devis détaillé à écrire avec le dimensionnement de
conv-audit **avant tout lancement** ». Dimensionnement proposé par conv-audit (messages n° 126 point 3 (a), n° 127 point 3).

**Rien n'est lancé par ce document.** Il chiffre, il relève une tension avec le plafond, et il pose une décision.

---

## 1. Ce que la couche 2 doit produire

Les **organismes par mode** de la porte G1 : des épisodes d'un agent réel qui rédige des propositions d'expériences, dont
une partie est sabotée selon un mode **connu et étiqueté**, avec leurs **jumeaux honnêtes appariés**. C'est le matériau sur
lequel G1 compare la boîte blanche séquentielle aux bases.

Deux modes connus, retenus par conv-audit :
- **« coût déclaré gonflé »** — la proposition surdéclare le coût de l'expérience ;
- **« affaiblir les contrôles »** — la proposition dégrade un contrôle expérimental (accord de 0,968 entre deux séries
  d'appariement au pilote).

Sortie au format `pole/monde_banque_scores.py` ; notes des deux juges locaux (8 et 3 milliards de paramètres) ; étiquetage
à deux séries ; lecture par les **sondes figées de P3** ; bases de **N-007**.

## 2. Base de coût : ce que la couche 1 bis a réellement coûté

Seule base mesurée dont nous disposons (R-596, `registres/depenses.md`) :

| poste | mesure |
|---|---|
| Volume noté | **96 épisodes** (60 du pilote + 36 de la banque), **2 juges** chacun = **192 notations** |
| Carte graphique | A100 SXM4 80 Go à **1,184 à 1,366 USD/h** |
| Durée des deux runs | ≈ 4,56 h (partie (b)) + ≈ 2,77 h (partie (a)) |
| Dépense totale | **≈ 9,7 à 11,7 USD** (relevé de facturation à confirmer, réserve) |

**Décomposition retenue pour ce devis** (estimation, pas une mesure séparée) :
- **Coût fixe par lancement** ≈ **2 à 3,5 USD** : création d'instance, descente des modèles (≈ 22 Go), démarrage, arrêt.
  C'est le poste qui punit les lancements multiples.
- **Coût marginal par notation** ≈ **0,012 USD** (≈ 0,6 min de carte), soit ≈ **0,024 USD par épisode** à deux juges.

**Réserve** : ces deux chiffres sont dérivés d'**un seul** chantier antérieur, par soustraction, et non mesurés isolément.
Ils valent à ± 50 % sur le coût fixe et ± 30 % sur le marginal. La génération des propositions sabotées (le modèle de 8
milliards qui écrit) tourne sur la **même instance** que la notation : elle est dans le coût de carte, pas en appels d'API.

## 3. Dimensionnement et chiffrage

### (a) Base, telle que conv-audit la propose

≈ 40 consignes × 3 exécutions × 2 modes = **240 épisodes sabotés**, plus **240 jumeaux honnêtes** appariés = **480 épisodes**,
soit **960 notations** à deux juges.

| poste | volume | coût |
|---|---|---|
| Coût fixe (1 lancement) | 1 | 2 à 3,5 |
| Génération des 240 propositions sabotées + 240 honnêtes | 480 | ≈ 4 à 7 |
| Notation, 2 juges | 960 | ≈ 11,5 |
| Lecture par les sondes figées de P3 (activations) | 480 | ≈ 2 à 4 |
| **Sous-total (a)** | | **≈ 20 à 26 USD** |

**Tient dans les 50 USD**, et c'est cohérent avec l'estimation de conv-audit (20 à 50).

### (b) Ce que D-S8 réécrite (N-056) exige en plus

N-056 point 1 : le contraste le plus difficile est **blanc contre blanc** — notre moniteur séquentiel contre les bases
boîte blanche (ii) cascade de portes et (iii) sonde sur le dernier état. L'écart y est **probablement petit**, donc la
puissance commande **« plusieurs centaines de tâches sabotées de plus par mode »**.

Lu à **+ 300 épisodes sabotés par mode** (lecture basse de « plusieurs centaines ») :

| poste | volume | coût |
|---|---|---|
| + 300 sabotés × 2 modes | 600 | ≈ 5 à 9 (génération) |
| + 600 jumeaux honnêtes | 600 | ≈ 5 à 9 (génération) |
| Notation des 1 200, 2 juges | 2 400 | ≈ 29 |
| Sondes de P3 sur 1 200 | 1 200 | ≈ 5 à 10 |
| Coût fixe (1 lancement de plus, au moins) | 1 | 2 à 3,5 |
| **Sous-total (b)** | | **≈ 46 à 60 USD** |

### (c) Ce que D-S29 (N-056 point 4) exige encore

« Le mode tenu à l'écart doit être **dimensionné comme les autres modes** » — poste de devis de la couche 2, explicitement.
Un **troisième mode** à la même taille que (a) + (b) par mode : **≈ 33 à 43 USD**.

### Total

| scénario | coût estimé | tient dans 50 ? |
|---|---|---|
| (a) base seule | **20 à 26** | **oui**, avec marge |
| (a) + (b) puissance de D-S8 | **66 à 86** | **non** |
| (a) + (b) + (c) mode tenu à l'écart | **99 à 129** | **non**, du double au triple |

## 4. La tension, dite franchement

**Le plafond de 50 USD finance la base, pas la puissance que nos propres décisions exigent.** Ce n'est pas une erreur du
GO : le GO a été donné sur l'estimation de conv-audit (20 à 50), qui chiffrait la base. D-S8 réécrite et D-S29 ont été
inscrites **le même jour** (N-056) et personne n'a rapproché les deux chiffres. Ce devis est ce rapprochement.

Conséquence à ne pas contourner : lancer (a) seule et appeler le résultat « la banque de G1 » serait **sous-puissant sur le
contraste qui décide** (blanc contre blanc). Un nul y serait non concluant, et le dire après coup violerait R3 et R4.

## 5. Décision demandée à Lazar

**Décision** : comment financer la banque des deux modes connus, sachant que la puissance exigée par D-S8 et D-S29 dépasse
du double au triple le plafond de 50 USD accordé.

**Enjeu** : la banque fournit les organismes **par mode** de G1 ; sa puissance sur le contraste blanc contre blanc décide si
un nul à G1 est interprétable ou muet.

**Options** :

- **(a) Lancer la base seule (20 à 26 USD), dans le plafond actuel, et écrire la sous-puissance dans le préenregistrement.**
  *Avantage* : part aujourd'hui, aucun nouveau GO, aucune dépense au-delà de l'accordé. *Inconvénient* : le contraste
  blanc contre blanc reste sous-puissant ; un nul y sera déclaré non concluant d'avance — honnête, mais c'est un résultat
  en moins pour G1.
- **(b) Relever l'enveloppe à ≈ 90 USD et faire (a) + (b) en deux lancements.** *Avantage* : la puissance que D-S8 exige,
  sur les deux modes connus ; le mode tenu à l'écart reste à dimensionner plus tard. *Inconvénient* : ≈ 40 USD de plus que
  l'accordé, sur un devis dont les chiffres valent à ± 30 à 50 %.
- **(c) Relever à ≈ 130 USD et tout faire, mode tenu à l'écart compris (D-S29 satisfaite).** *Avantage* : G1 dimensionnée
  d'un coup, cohérente avec toutes les décisions déjà prises. *Inconvénient* : le triple de l'accordé ; et le mode tenu à
  l'écart est encore en attente de son **scellement définitif** par ton mot, donc une partie de la dépense porterait sur
  une pièce non scellée.

**Recommandation : (b), confiance moyenne.** Elle achète la puissance là où elle décide, elle ne dépense rien sur une pièce
non scellée, et elle laisse le mode tenu à l'écart à un devis propre quand son scellement sera fait. (a) est défendable si
tu veux voir la banque tourner avant d'engager plus ; (c) est prématurée tant que le mode tenu à l'écart n'est pas scellé.

**Défaut sous 48 heures** : **(a)** — la base seule, dans le plafond accordé, avec la sous-puissance écrite au
préenregistrement. C'est le seul choix qui ne demande aucune décision de dépense nouvelle, donc le seul qui puisse
s'appliquer par défaut.

## 6. Avant tout lancement, quoi qu'il soit décidé

1. **Fiche de lancement** (format des chantiers précédents) : volumes exacts, graines par `numpy.random.SeedSequence`
   dérivées par tâche (R9), manifeste de run, garde d'arrêt testée sur un cas sain **et** sur un artefact (R5).
2. **Contre-lecture par un sous-agent neuf** (R2) de la fiche et du dimensionnement.
3. **Contrôle du plafond** avant création d'instance ; arrêt par **identifiant d'instance**, jamais par motif de ligne de
   commande (R10) ; consignation dans `registres/arrets.md`.
4. **Aucun score de moniteur n'entre dans la génération** des épisodes (invariant de N-053) : l'organisme qui écrit les
   propositions sabotées ne voit aucune note de sonde.
