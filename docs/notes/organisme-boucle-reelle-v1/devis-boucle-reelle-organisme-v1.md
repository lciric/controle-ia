# Devis — la plus petite course réelle de la boucle complète de l'organisme d'idéation — v1

- **Rédacteur** : Claude Opus 5.5 (`claude-opus-5-5`), rédacteur neuf. 7 novembre 2026, écrit vers 23:48 (temps universel, `date -u`).
- **Pour** : le dessin du brouillon 1 (`preenregistrement-boucle-reelle-organisme-v1-brouillon1.md`, sections 3 et 12) ;
  feu vert de préparation GO-2026-11-07-11 (« dépense sur devis, après scellement »). **Ce devis n'engage aucune dépense** :
  il appelle un feu vert de dépense du directeur, après le scellement.
- **Prix** : aucun prix n'a été vérifié sur une grille de fournisseur aujourd'hui (aucun accès réseau permis) ; chaque prix
  unitaire porte « à vérifier ». Les ancres mesurées sont citées avec leur source.

## 1. Ancres mesurées (sources)

| ancre | valeur | source |
|---|---|---|
| deuxième course réelle (Kimi et Argon, une génération) | 62 appels, 1,47 dollar, soit 0,0237 dollar par appel | `README.md` de l'organisme, ligne 125 (`bdd6516f…`) |
| troisième course d'A1-v3 (Argon seul) | 960 appels, 58,44887 dollars ; 3 792 407 jetons d'entrée, 410 496 de sortie ; 0,0609 dollar par appel (3 950 jetons d'entrée, 428 de sortie en moyenne) ; appel le plus cher 0,609 dollar | `docs/verdicts/verdict-attaque-goodhart-v3-troisieme-course-v1.md`, section 4 (`7dade9ef…`) |
| tailles des consignes dans l'essai à blanc (caractères) | proposeur 13 552 (génération 1) et 15 730 (génération 2) ; expérimentateur 10 536 à 12 072 (médiane 11 218) ; vérificateur 8 060 à 8 220 | `essai-a-blanc-v1/sorties/releve-v64-factice-g2-tour-ferme-v1-etage1.json` (`2d19d6d3…`), champs `appels_proposeurs` et `appels_etage` |
| sessions par carte testée dans l'essai à blanc | 2 d'expérimentateur (un tour d'exécution, un tour de fin), 1 de vérificateur | même relevé (54 et 27 sessions pour 27 testées) |
| bornes gelées de la v64 | expérimentateur 0,80 dollar par carte (12 tours au plus) ; vérificateur 0,10 dollar par carte ; session de proposeur 0,50 dollar | `pole/tour_ferme_v64.py` (`35a8294e…`), lignes 144 à 151 ; `configuration-tour-ferme-v4.json` (`15b34adf…`), `plafonds_session` |
| barème prudent des commandes | Kimi 2,0 dollars par million de jetons d'entrée ; Argon 10,0 | `configuration-tour-ferme-v4.json`, `fournisseurs.<kimi, argon>.prix_entree_usd_par_million_jetons` |

## 2. Prix unitaires retenus (tous « à vérifier »)

| fournisseur, modèle | entrée (dollars par million de jetons) | sortie (dollars par million de jetons) | provenance |
|---|---|---|---|
| Argon, `gemini-4-argon` | 10 — **à vérifier** | 50 — **à vérifier** | barème prudent de la configuration v4 pour l'entrée ; sortie **déduite** des comptes d'A1-v3 : (58,44887 − 3,792407 × 10) / 0,410496 = 50,0 exactement, ce qui rend la paire (10 ; 50) vraisemblable, sans la prouver |
| Kimi, `kimi-k3.1-pro` | 2 — **à vérifier** | 10 — **à vérifier, supposé** (aucune mesure de Kimi seul dans les pièces lues) | barème prudent pour l'entrée ; sortie supposée, prudente |

Jetons : trois caractères par jeton (barème prudent des commandes).

## 3. Appels × jetons × prix

### 3.1 Par appel

| rôle (fournisseur) | entrée (jetons) | sortie (jetons) | prix d'un appel, central | borne |
|---|---|---|---|---|
| proposeur (Kimi), génération 1 et 2 | 4 500 à 5 200 | 3 000 (jusqu'à 15 000 s'il raisonne longuement) | ≈ 0,04 à 0,16 ; retenu 0,08 | 0,50 par session |
| proposeur (Argon) | 4 500 à 5 200 | 3 000 (raisonnement caché compris) | 0,045 + 0,15 ≈ 0,20 | 0,50 par session |
| expérimentateur (Kimi), par tour | 3 700 à 5 000 (la session croît d'un tour à l'autre) | 500 à 1 000 | ≈ 0,01 à 0,02 ; prudent 0,04 ; prix prudent du tour fermé 0,06 | 0,80 par carte (12 tours) |
| vérificateur (Argon), une session par carte testée | 2 700 | 200 à 1 000 | 0,027 + 0,01 à 0,05 ≈ 0,04 à 0,08 ; retenu 0,06 | 0,10 par carte |
| gardien, juge statistique, oracle, lecture | — | — | 0 (aucun appel de modèle : gardien mécanique) | — |

### 3.2 Nombre de cartes testées

- **Lois plantées, génération 1** : V1 et V2 (toujours promues), V3 (0,617), V4 (0,501), T-ELIM (1,0) : **4,12 attendues**,
  5 au plus (simulation, `sorties-puissance-v1/puissance-boucle-reelle-v1-r1000.json`, `a23959fa…`). F1 à F4 : 0 (refusées
  par construction). T-MAL : refusée au gardien.
- **Génération 2** : F1 à F4 et les copies : 0 sous une chaîne correcte ; 8 au plus si la chaîne casse (cas compté au plafond).
- **Cartes réelles** : inconnues (premier passage de ces proposeurs dans ce monde). Hypothèse centrale : 3 promues en
  génération 1, 2 en génération 2 ; au plus 12 et 12.

### 3.3 Total

Coût d'une course = (cartes testées) × (tours × prix du tour + prix du vérificateur) + 4 appels de proposeurs (2 × 0,08 +
2 × 0,20 = 0,56 dollar).

| cartes testées | 2 tours, prix central (0,02 et 0,06) | 2 tours, prix prudents (0,04 et 0,08) | 12 tours à 0,06, vérificateur 0,08 |
|---|---|---|---|
| 4,12 (aucune carte réelle promue) | 0,97 | 1,22 | 3,86 |
| **9,12 (hypothèse centrale)** | **1,47** | **2,02** | **7,86** |
| 14,12 (6 et 4 cartes réelles promues) | 1,97 | 2,82 | 11,86 |
| 29 (toutes les cartes réelles promues dans les deux générations) | 3,46 | 5,20 | 23,76 |

Appels attendus (hypothèse centrale, 2 tours) : 4 de proposeurs, ≈ 18 sessions d'expérimentateur, ≈ 9 de vérificateur, soit
**≈ 31 appels pour ≈ 1,5 à 2 dollars** (même ordre que la deuxième course réelle : 62 appels, 1,47 dollar) ; ≈ 120 appels et
≈ 8 dollars si chaque test prend ses 12 tours.

### 3.4 Pire cas sous les bornes gelées (ce qui fixe le plafond)

| cas | cartes testées | Kimi | Argon | total |
|---|---|---|---|---|
| chaîne correcte, tout promu | 17 + 12 = 29 | 29 × 0,80 + 2 × 0,50 = 24,20 | 29 × 0,10 + 2 × 0,50 = 3,90 | 28,10 |
| chaîne cassée (fausses et copies de la génération 2 promues aussi) | 29 + 8 = 37 | 37 × 0,80 + 1,00 = 30,60 | 37 × 0,10 + 1,00 = 4,70 | 35,30 |

## 4. Machine

Le vrai bac à sable exige `bwrap` (bubblewrap) ≥ 0.9, un utilisateur dédié sans privilège et un noyau qui permet les espaces
de noms ; le conteneur de ce jour n'a pas `bwrap` (essai à blanc, étape 1, refus en code 2). Deux voies :
- **(a) machine louée jetable, processeur seul** (aucune carte graphique n'est utile) : prix horaire d'une petite machine
  à vérifier (la machine d'A1-v3, avec une carte, coûtait 0,0617 dollar par heure : verdict d'A1-v3, constat 4). Durée attendue
  2 à 4 heures (4 appels de proposeurs jusqu'à 1 750 secondes chacun, ≈ 9 cartes testées à quelques minutes chacune),
  plus 30 minutes d'essai à blanc `--bac reel` et des essais avant le lancement. **≈ 0,5 dollar attendu ; plafond 5 dollars**
  (≈ 50 heures à 0,10 dollar par heure ; la garde de durée de l'étage est 72 heures).
- **(b) une machine du directeur** avec `bwrap` : coût nul, mais elle doit être déclarée jetable (liste blanche de
  l'environnement, garde 15) et ne porter aucune clé hors des relais.

## 5. Plafond proposé

- **Modèles : 40 dollars, parts Kimi 33 et Argon 7** (somme égale au plafond au centime, garde de la v64). Il couvre le pire
  cas de la chaîne cassée (35,30 dollars ; Kimi 30,60 ; Argon 4,70) : aucune issue ne peut devenir « non jugeable » par défaut
  de plafond, et une brèche ne peut pas être masquée par un arrêt de dépense (décision de Lazar du 2 novembre 2026 citée par
  le tour fermé : « je ne veux pas de résultats non concluants par défaut de conception, de plafond »).
- **Machine : 5 dollars** (voie (a)) ou 0 (voie (b)).
- **Total demandé : 45 dollars au plus ; attendu ≈ 2 à 3 dollars** (≈ 1,5 à 2 pour les modèles, ≈ 0,5 pour la machine).
- Variante (décision D1 du brouillon : garder les deux bras de référence du tour fermé) : + ≈ 2 dollars attendus (calé sur le
  devis du tour fermé, section 12 : bras aléatoire ≈ 2,5 dollars et recopie ≈ 1,2 dollar sur trois générations) ; plafond
  + 15 dollars (≈ 16 cartes de plus à leurs bornes).
- La course ne s'impute sur aucun autre plafond ; les relais gardent chacun leur plafond cumulé (commandes v6 :
  `--plafond-cumule-usd`), à régler sur les parts ci-dessus dans la configuration v5 (pièce M6).

## 6. Ce que le devis ne couvre pas

Le développement du code v65 et ses essais (processeur, sans dépense) ; une reprise après panne d'un relais (texte neuf et
devis neuf) ; toute génération 3 ; les juges d'idées à modèle (hors de la chaîne) ; la vérification des prix sur les grilles
des fournisseurs, à faire par la session de dépôt avant le feu vert.
