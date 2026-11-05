# Devis de la course 2 (génération 1) et du pré-pilote recentré — bisociateur à trois bras, Kimi proposeur, notation croisée, Opus troisième juge — v6

Lignée session-depot (sous-agent), 31 octobre 2026, écrit vers 01:20 UTC (`date -u`). **Rien n'est lancé, aucun appel payant n'a servi à ce devis** (le skill `claude-api` a été lu sur disque pour les prix, sans appel). C'est un nœud de dépense : chaque lancement aura sa ligne de GO, écrite par la session principale sur le mot direct de Lazar. Ce devis n'écrit rien dans `registres/`.

**Remplace** le devis v5 (`devis-course-2-et-pre-pilote-v5.md`, `dd34ac41…`, script `06a9ad87…`, sortie `d1182707…`), archivé sans modification (R12). La v4 (`03e961d5…`, `011a0fc2…`, `b3c6a087…`) reste archivée elle aussi.

**Ce qu'il prend en compte**
- **le rapport du relecteur de la v5** (`nuit-rendus-2/verifier-devis-v5.md` du bloc-notes de la session, `9d66ff3e…`, verdict « conforme avec réserves ») : ses neuf constats sont traités au § 1, un par ligne ; son essai sur les plafonds souples (`verif-devis-v5/test_souple_b5.txt`) est refait dans le script v6 et redonné à l'identique aux bases de la v5 (§ 3.3, pont) ; celui du complément (`complement_reste.txt`) est refait à la façon du brouillon 5, sous une graine nouvelle (§ 5) ;
- le rapport du relecteur de la v4 (`nuit-rendus/verifier-devis-v4-course2.md`, `b39be6fe…`) : ses huit défauts restent traités (§ 1bis.2) ;
- les messages de conv-audit (branche `origin/canal/conv-audit-n04`, `cbdbc739`) : n° 266 (`b78f9b1e…`, pré-pilote recentré), n° 267 (`0c77987a…`, machine jetable, course 2 = génération 1), n° 268 (`49a64a80…`, trois bras, « ≈ 12 fusions par proposeur »), n° 269 (`b5f7057e…`, plafond 45 USD recommandé, machine jetable ; la v52 toujours introuvable dans git) ;
- les décisions relayées dans le registre de conv-audit (même branche, fichier `86cd5d5e…`) : **R-643, décision de Lazar** (« bras basique : garder » → trois bras, méta, Gu-Krenn et basique, une paire par session chacun) ; **R-642**, recommandation de conv-audit (« ≈ +4 fusions par proposeur ») ; **R-640, décision de Lazar** (machine jetable) ; **R-630, recommandation** de conv-audit (plafond du pré-pilote à 45 USD, sur le mot de Lazar « on augmente le plafond ») ; R-662 et R-663 (brouillon 5 et sa contre-lecture 4) ;
- **le brouillon 5 du préenregistrement du pré-pilote** (`preenregistrement-pre-pilote-course-2-brouillon5.md`, `96080471…`, script `96ee5852…`, sortie `d342b569…`) : 28 fonds, trois bras, ordre des étapes B, règle de sacrifice d'A1 (l. 292), plafonds de relais par étape, plafond 45 et arrêt d'étape 40, complément proposé 0,20 (P15), lecture « total 110 ou 123 » à confirmer (S17, C10, DEP6) ;
- les coûts réels de la nuit (`registres/depenses.md`, `a0d521ea…`, **l. 249 à 265**) et les journaux des relais de Kimi et du collisionneur (§ 2.2) ;
- le devis de la machine jetable v2 (`machine-jetable-v1/devis-et-plomberie-machine-jetable-v2.md`, `39260994…`), auquel ce devis renvoie (§ 6).

Tous les chiffres sortent du script `calcul-devis-course-2-et-pre-pilote-v6.py` et de sa sortie `calcul-devis-course-2-et-pre-pilote-v6.sortie.txt`, même dossier, compagnons `.sha256`. Rejeu `python3 -I` (numpy 2.5.3) : sortie identique octet pour octet. Le script garde les noms de graines de la v5 : une configuration que la v6 ne change pas redonne ses chiffres. Montants arrondis au dixième.

**Vocabulaire (constat 2).** « **Attendu aux bases** » = somme des bases, multipliées par le facteur de coupure de Kimi (1,447) ; ce n'est **pas** l'espérance du modèle. La « **moyenne tirée** » est l'espérance du modèle : elle ajoute les médianes de P11 (1,2 ou 1,4) là où la base n'est pas observée, et l'asymétrie des lois log-normales. Les deux sont donnés.

## 0. Verdict

- **Pré-pilote (brouillon 5) : ≈ 32,6 USD attendus aux bases au texte du brouillon, ≈ 34,6 dans la configuration recommandée** (D-g (b) et D-i (2), que le brouillon 5 ne chiffrait pas, CP5-05). **Moyenne tirée, sans plafond ni sacrifice : ≈ 40,8 et ≈ 43,5.** Le brouillon 5 disait 28,4.
- **45 USD suffisent pour la dépense, pas pour le plan.** Avec les plafonds de relais du brouillon 5 tenus fixes, la dépense reste sous 45 (quantile 99 % : 43,8 USD). Mais **une étape protégée bute sur son plafond de relais avec 0,99** : ces plafonds valent ≈ 1,2 à 1,7 fois l'attendu du brouillon 5 (3 pour É9), sous les dispersions de P11.
- **C'est la souplesse qui fait le travail, pas l'élargissement** (constat 1). Une étape protégée qui atteint son plafond de relais continue sur la marge restante sous le plafond. Avec les plafonds du brouillon 5 gardés et rendus souples :
  - **à 50 USD, arrêt d'étape 45** : sacrifice 0,17 (fusions retirées 0,12), étape protégée non lancée 0,021, coupée 0,063 (l'une ou l'autre 0,072) ; dépense médiane 40,6 USD, quantile 90 % 47,3 ;
  - **à 45 / 40** : sacrifice 0,41 (fusions 0,32), non lancée 0,051, coupée 0,168.
  - L'option recommandée par la v5 (plafonds au quantile 90 %, souples, 50 / 45) fait sacrifier davantage : 0,29 (fusions 0,26), non lancée 0,044, coupée 0,047 (l'une ou l'autre 0,080). Elle demande aussi deux règles nouvelles au lieu d'une.
  - **Recommandation : 50 / 45, plafonds de relais du brouillon 5 rendus souples pour les étapes protégées.**
- **Course 2, 4 sous-sessions, lecture B (24 fusions, ≈ 12 par proposeur, R-642 et n° 268) : ≈ 117,9 USD attendus aux bases, moyenne tirée ≈ 139,2, médiane tirée ≈ 134,9, ≈ 241 au pire.** En lecture A (12 fusions) : ≈ 109,8 aux bases, moyenne 129,3, ≈ 221 au pire. La v4 annonçait 85 aux bases et 180 au pire pour deux bras.
  - **L'écart de + 33,2 USD, par cause, en chaîne** (constat 8) : bases recalées sur les coûts observés (Argon proposeur, contrôles d'Argon par lancement, coupures de Kimi) **+ 16,1** ; trois grilles de lecture d'étiquettes, prises au plan du brouillon 5 **+ 6,4** ; troisième bras (R-643, 12 fusions) **+ 2,7** ; lecture B (24 fusions) **+ 8,0**.
- **Plafond total** (pré-pilote à 50 / 45 recommandé, puis la course sur le reste, complément conditionnel compté sur le reste, constat 3) :
  - **à 110 USD, 4 sous-sessions ont une probabilité < 0,01** au modèle indépendant (0,04 en variante corrélée), et il n'y a aucune course avec 0,52 ;
  - **à 160 USD**, 3 sous-sessions au moins avec 0,76 (0,80 sans complément) ;
  - **à 180 USD**, 4 sous-sessions avec 0,53 (0,57 sans complément).
- **Machine jetable** : à part, devis machine v2 (≈ 0,5 USD attendus, ≈ 7,4 au pire, GO proposé 10 USD), plus les appels de modèle des tests de mort, 0,6 USD par fiche (§ 6).

## 1. Ce qui change depuis la v5 : constat → correction

| N° | Constat du relecteur de la v5 | Correction dans la v6 | Où |
|---|---|---|---|
| 1 (moyen) | Décision 1 : il manque l'option « plafonds du brouillon 5 rendus souples », qui fait mieux que la recommandation ; le script ne la testait pas | Le script v6 joue quatre configurations nouvelles (45 / 40 et 50 / 45 ; texte du brouillon et configuration recommandée ; variante corrélée). Aux bases de la v5, il redonne exactement les chiffres du relecteur (0,12 ; 0,09 ; 0,010 ; 0,043 ; 38,8 USD et 0,32 ; 0,25 ; 0,025 ; 0,123). Lignes ajoutées au § 3.3 ; option (b) nouvelle à la décision 1 ; **recommandation revue** : 50 / 45, plafonds du brouillon 5 souples ; point 1 du § 3.4 réécrit (une seule règle changée). Écart déclaré : cette option n'est pas meilleure partout. La coupure d'une étape protégée y vaut 0,063, contre 0,047 pour l'ancienne recommandation ; « non lancée ou coupée » vaut 0,072 contre 0,080 | § 0, § 3.3, § 3.4, § 9 (décision 1) |
| 2 (mineur) | « Attendu » ne désigne pas l'espérance du modèle | Encadré « Vocabulaire » en tête ; « attendu aux bases » partout ; moyennes tirées ajoutées : course 4 sous-sessions, lecture B, 139,2 ; pré-pilote sans plafond, 43,5 aux bases v6 (41,7 aux bases v5, chiffre du relecteur) ; dépense moyenne sous la règle d'A1 pour chaque configuration | en-tête, § 0, § 3.2, § 3.3, § 4.3, § 5, § 9 |
| 3 (mineur) | Le tableau du plafond total ignore le complément conditionnel, que le brouillon 5 prend sur le reste (proposé avec 0,20) | Le complément est tiré (proposé avec 0,20, coût tiré) et retranché du reste ; colonnes « avec » et « sans complément » au § 5. Aux bases de la v5, 160 USD donnait 0,78 pour 3 sous-sessions au moins (relecteur). Aux bases v6, avec la configuration recommandée v6 : 0,76 | § 5, § 9 (décision 2) |
| 4 (mineur) | La décision 2 ne cite pas la lecture « total 123 » du brouillon 5 | Option (e) ajoutée : la ligne du pré-pilote s'ajoute au total (123 au plafond 45 du brouillon 5, 128 au plafond 50) ; deux variantes chiffrées : reste = total − dépense, ou reste fixé à 78 | § 5, § 9 (décision 2) |
| 5 (mineur) | Le pré-pilote n'a pas de pire cas par poste | Colonne « quantile 99 % tiré » par étape ; règle écrite : la borne d'une étape sacrifiable est son plafond de relais ; celle d'une étape protégée est son plafond de relais, élargi au plus à la marge sous S17 ; le pré-pilote entier est borné par S17 | § 3.2 |
| 6 (mineur) | Formulations trop fermes : « aucune chance (0,00) » ; « ≈ 1,35 fois l'attendu » ; « une étape coupée est “non mesuré (budget)” » donnée comme texte du brouillon | « < 0,01 au modèle indépendant (0,04 en variante corrélée) », probabilités à trois décimales dans la sortie ; « ≈ 1,2 à 1,7 fois l'attendu du brouillon 5, et 3 pour É9 » (rapports imprimés par le script) ; « lecture, à confirmer au brouillon 6 » : le brouillon 5 (l. 292, A1) ne dit « non mesuré (budget) » que pour une étape non lancée | § 0, § 3.2, § 3.3, § 3.4, § 8 |
| 7 (mineur) | Kimi en appel isolé : base non observée, tirée à la médiane 1,0 au lieu du 1,4 de P11 (≈ + 0,9 USD) | Famille nouvelle `juge_kimi_isole`, médiane 1,4, même dispersion (0,52), pour toute composante dont la base est l'appel isolé non observé de Kimi : jugements d'É6 et des fusions, et aussi rendus de Kimi en É3 et en seconde version, et complément (même base de 0,057, même règle). Les attendus aux bases ne bougent pas ; les tirages montent (É6 : médiane 7,9 → 8,8) ; les plafonds au quantile 90 % d'É3, É5bis, É6 et des fusions montent. Un pont imprime les chiffres à médiane 1,0 | § 2.4, § 3.2, § 3.3, sortie (pont) |
| 8 (mineur) | Citations : 0,1577 sans source ; `depenses.md` cité l. 249 à 264 sous une empreinte qui couvre l. 265 ; découpage « ≈ 17 + ≈ 16 du troisième bras » qui attribue au troisième bras les trois grilles d'étiquettes | Journal `run-texte-III-e3-v1/journal.jsonl` (`93d57901…`, cellule E3-T1-conception-D, Kimi servi, 5 932 / 14 585 jetons) cité au § 2.2 ; `depenses.md` cité l. 249 à 265, et la l. 265 (Kimi avec recherche, 0,39 USD, non retenue) est nommée ; décomposition refaite en chaîne par le script : bases + 16,1, trois grilles (plan du brouillon 5) + 6,4, troisième bras + 2,7, lecture B + 8,0 | en-tête, § 0, § 2.2, § 4.3 |
| 9 (mineur, rendu seulement) | Le rendu de la v5 lisait mal le n° 269 : celui-ci dit la **v52** introuvable dans git, pas le devis machine v2 absent | Rien à corriger dans le devis v5. La v6 lit le n° 269 correctement (en-tête) et précise au § 6 que les deux valeurs de la v52 viennent du devis machine v2 (l. 559-560), la v52 elle-même restant introuvable dans git | en-tête, § 6 |
| SUPPOSÉ ajouté par le relecteur | Les 6,00 USD d'Argon en course 1 ont été dépensés alors qu'Argon était aussi juge (R-804) : la passe à 3,00 pourrait être un peu surestimée | Ajouté au § 7, marqué plausible, non établi ; la base de 3,00 est gardée, au sens prudent | § 7 |

## 1bis. Ce qui avait changé de la v4 à la v5 (gardé)

### 1bis.1 Postes

| Poste | v4 | v5 et v6 | Raison |
|---|---|---|---|
| Bras de bisociation | 2 (méta, Gu-Krenn) | **3 (méta, Gu-Krenn, basique)** | R-643 (décision de Lazar) ; n° 268 |
| Fusions de la course | 8 (lecture A) ou 16 (B) | **24 (lecture B, principale)** ou 12 (A) | « une paire par session chacun », « ≈ 12 fusions par proposeur » (n° 268) ; R-642 : « ≈ +4 fusions par proposeur » pour le basique |
| Lectures d'étiquettes | 2 lecteurs, une grille | **2 lecteurs × 3 grilles** (liste fermée, vocabulaire Gu-Krenn, niches du bras méta) | brouillon 5, É7 |
| Pré-pilote | plan du v4 (24 témoins) | **plan du brouillon 5** : 28 fonds, 56 lectures d'aiguillage, 3 fusions, seconde version, passe « tableau », table de l'axe 7, M6b en option | brouillon 5 (R-662) |
| Argon proposeur | 2,24 USD par passe | **3,00 par passe (OBSERVÉ)** ; pire 4,02 | relecteur de la v4, défaut 2 ; `depenses.md` l. 250 |
| Contrôles d'Argon | 1,75 pour toute la course | **1,75 par lancement**, un lancement par sous-session (SUPPOSÉ) | observé une fois, pour un lancement de 16 fiches (l. 250) |
| Coupures de Kimi | non comptées | **facteur 1,447 sur la dépense comptée** de chaque poste de Kimi | ≥ 3 coupures sur ≈ 13 appels longs le 30 octobre (§ 2.3) |
| Fusion d'une paire | 0,40 (SUPPOSÉ) | **0,204 (OBSERVÉ)**, 0,30 compté avec coupures ; pire 0,89 | médiane de 7 appels longs de Kimi (§ 2.2) |
| Kimi juge, appel isolé (pré-pilote, É6) | 0,026 (lot) | **0,057** par fiche ; **médiane 1,4 de P11 dans les tirages (v6)** | le brouillon 5 juge une fiche par appel ; l'observé (0,026) vaut pour un lot de 29 |
| Sonnet 5.5 | 4 / 20 (SUPPOSÉ, prix d'Opus) | **2 / 10 (SOURCÉ)** | table du skill `claude-api` |
| Recherche sur le Web | 0,01 (SUPPOSÉ) | **0,01 (SOURCÉ)** ; pire 0,05 | skill `claude-api`, `shared/managed-agents-core.md` l. 205 |
| Dispersions | 0,35 à 0,5 | **celles de P11** (0,22 à 0,72) | relecteur de la v4, défaut 3 |

### 1bis.2 Défauts du relecteur de la v4

| N° | Défaut | Traitement |
|---|---|---|
| 1 (majeur) | Dépassé par R-643 et le n° 268 (trois bras) ; effectifs du brouillon 4 | trois bras, lectures A et B ; effectifs du **brouillon 5** (plus récent que le brouillon 4) ; plafond total recalculé (§ 5) |
| 2 (moyen) | Argon proposeur sous l'observé | attendu aux bases 3,00 par passe, pire × 1,34 = 4,02 |
| 3 (moyen) | Dispersions plus étroites que P11 | σ = ln(haut ÷ bas) ÷ 2,563, tiré de chaque intervalle à 80 % de P11 (brouillon 5, l. 134) ; « probabilité nulle » n'est plus écrit ; une variante corrélée (ρ 0,5) est ajoutée |
| 4 (mineur) | Arrondis du § 0 | tous les montants au dixième, tels que la sortie les donne |
| 5 (mineur) | Attribution des décisions | décisions de Lazar : R-640, R-643 ; recommandations de conv-audit : R-630, R-642 (en-tête) |
| 6 (mineur) | Prix de la recherche | 0,01 sourcé (prix de liste) ; variante à 0,05 chiffrée : + 10,4 USD sur la course |
| 7 (mineur) | Postes sans compte d'appels | chaque poste a ses appels et ses jetons (§ 3.2, § 4.2), estimés et marqués SUPPOSÉ quand ils ne sont pas observés |
| 8 (information) | Interpréteur | usage écrit en tête du script ; rejeu vérifié |

## 2. Bases

### 2.1 Prix (USD par million de jetons)

| Modèle | Entrée | Sortie | Provenance |
|---|---|---|---|
| Opus 5.5 (juge, aiguilleur, antériorité, lecteurs) | 4 | 20 | SOURCÉ : table du skill `claude-api` (cache du 2026-10-06) ; `collisionneur_v2.py` (`0e63febd…`) |
| Sonnet 5.5 (rédacteur, tiers metteur en forme T) | **2** | **10** | SOURCÉ : table du skill `claude-api` ; la v4 le comptait au prix d'Opus |
| Fable 5.1 (relecteur) | 10 | 50 | SOURCÉ : idem |
| Kimi K3.1 Pro | 2 | 10 | SOURCÉ (page du 30 octobre) ; **OBSERVÉ conforme** : 222 635 × 2 + 31 010 × 10 = 0,755 USD (l. 255) ; 5 112 / 21 433 jetons → 0,2246, facturé 0,224554 (journal du relais, tour étroit) |
| Argon | 8,3 | 41,5 | entrée : borne lue par Lazar (R-718) ; sortie **SUPPOSÉ** (`commande_argon_v3d.py`, `46c91df4…`) ; cohérent avec deux coûts de la nuit, comptés au même barème : 2 452 / 10 164 → 0,44 (l. 256) ; 1 665 / 9 609 + 4 requêtes → 0,61 (l. 261) |
| Recherche sur le Web (Claude) | 0,01 par recherche | — | SOURCÉ : « web searches at $10 per 1,000 » (skill `claude-api`, `shared/managed-agents-core.md` l. 205, `c8da375c…`, prix de liste des agents gérés) ; **SUPPOSÉ** : même prix par l'API Messages ; pire 0,05 (barème d'Argon du dépôt) |

### 2.2 Coûts observés retenus (`registres/depenses.md`, `a0d521ea…`, l. 249 à 265 ; journaux)

| Observation | Source | Ce qu'elle fixe |
|---|---|---|
| Argon proposeur : 6,00 USD pour 2 passes de 8 fiches ; contrôles externes 1,75 | l. 249-250 (course 1, tentative 2, engagement et fin) | passe d'Argon 3,00 ; contrôles 1,75 par lancement |
| Juges sur 29 fiches : Opus 3,31 en 6 appels (0,114 par fiche) ; Argon 2,28 (0,079) | l. 252 | jugements d'Opus et d'Argon |
| Kimi juge, lot de 29 : 222 635 / 31 010 jetons, 0,755 USD ; premier essai coupé à 300,7 s, 2,03 compté au pire | l. 254-255 | 0,026 par fiche en lot ; une coupure |
| Appels longs de Kimi au collisionneur : 7 réussis, de 0,137 à 0,241 USD, médiane 0,204 (entrée 5 112 à 33 347, sortie 12 487 à 21 433, dont 46 à 85 % de raisonnement) | `donnees/collisionneur-texte-III-v1/run-texte-III-e3-v1/journal.jsonl` (`93d57901…` : 0,1577, cellule E3-T1-conception-D, 5 932 / 14 585 jetons) ; `run-texte-III-e3-v2/journal.jsonl` (`dfc54365…`) ; `run-texte-III-etroite-e3-v1/journal.jsonl` (`93a372fa…`) | fusion d'une paire |
| Tour étroit : appel de Kimi coupé (ConnectionResetError à 37 s), 0,355 compté au pire, puis rejoué pour 0,2246 | `relais-kimi-texte-III-etroite-journal-v1.jsonl` (`c4888981…`), `…-reprise-journal.jsonl` (`a137ee1c…`) ; l. 259 | une coupure |
| Tour P-041 : appel de Kimi coupé, 0,48 compté au pire ; 1,95 USD comptés au pire sur trois relais | l. 262 ; R-864 | une coupure |
| Argon, cellules longues du collisionneur : 7 013 à 13 542 jetons de sortie | mêmes journaux | Argon écrit long : appui de la passe à 3,00 |
| Tours du collisionneur de la nuit : 8,01 ; 8,16 ; 20,30 USD (12 cellules chacun) | l. 260, 262, 263 | **non retenus** : le collisionneur ne sert pas dans la course |
| OpenAlex : 197 681 œuvres sur l'allocation gratuite (0,99 USD de crédits gratuits, aucune facture) | l. 264 | cooccurrences du bras Gu-Krenn simplifié comptées à 0 (SUPPOSÉ) |
| Kimi K3.1 Pro avec recherche sur le Web : 6 tours, 20 recherches (0,10 USD), 0,39 USD au total | l. 265 | **non retenu** : aucun poste du devis ne fait chercher Kimi ; noté parce que l'empreinte couvre cette ligne |

### 2.3 Coupures de Kimi

- **Faits** : le 30 octobre, au moins 3 appels longs de Kimi ont été coupés sur ≈ 13. Le relais compte chaque coupure au pire (réservation), puis l'appel est rejoué. Rapport réservation ÷ coût réel : 2,7, puis 1,6, puis 2,4.
- **Modèle** : probabilité 0,2 par appel, rapport tiré parmi les trois observés. La dépense comptée sur un poste de Kimi vaut donc **1,447 fois** son coût sans coupure.
- **Pourquoi la compter** : c'est la dépense comptée qui consomme le plafond, même si Moonshot facture moins ; le coût réel des coupures reste à lire sur la console Moonshot.
- **Le pire** : il couvre une coupure au pire sur chaque appel (rapport 2,7), sauf pour la passe de Kimi, dont le pire reste celui du v4 (4,75 par passe, plus de 1,25 × 3,7).

### 2.4 Incertitude (SUPPOSÉ)

- **Loi** : chaque composante d'un poste est tirée en log-normale. Les médianes de P11 ne s'appliquent qu'aux bases non observées : 1,2 pour les passes de Kimi et pour l'antériorité ; **1,4 pour les appels isolés de Kimi** (jugement d'une fiche, rendu d'un témoin ; v6, constat 7). Partout ailleurs, la médiane est 1,0.
- **Écart-type du logarithme**, tiré des intervalles de P11 :

| Poste | Médiane | Écart-type |
|---|---|---|
| Opus | 1,0 | 0,22 |
| Argon | 1,0 | 0,30 |
| Kimi juge, en lot (observé) | 1,0 | 0,52 |
| **Kimi, appel isolé (non observé)** | **1,4** | 0,52 |
| Aiguilleur | 1,0 | 0,54 |
| Antériorité | 1,2 | 0,63 |
| Fusion | 1,0 | 0,70 |
| Passe de Kimi | 1,2 | 0,72 |
| Autres postes (hors P11) | 1,0 | 0,35 |

- **Tirages** : les coupures de Kimi sont tirées appel par appel. 20 000 tirages ; graines `SeedSequence(20261031, spawn_key=(cle_de_tache(nom),))` (R9), noms de tâches de la v5 gardés, une tâche nouvelle : `devis-v6-complement-propose`.
- **Corrélation** : le modèle principal tire les postes indépendamment. Une variante leur donne un facteur commun (ρ = 0,5), pour un relais lent qui touche tout.

## 3. Pré-pilote recentré (brouillon 5)

### 3.1 Périmètre chiffré

C'est le plan du brouillon 5, dans l'ordre B de ses étapes, avec sa règle de sacrifice (A1).
- **Fonds** : 28, rendus une fois chacun (Kimi 9, Argon 9, T 10).
- **Aiguillage** : 56 lectures, plus 10 du second lecteur.
- **Juges** : trois juges sur les 28 rendus, un appel par fiche.
- **Bisociation** : passe « tableau » de Kimi, lectures d'étiquettes, 3 fusions (une paire par bras).
- **Autres étapes** : table de l'axe 7, paraphrases, 8 antériorités ; seconde version des témoins avec 0,43.
- **Configuration recommandée par le brouillon 5** : D-g (b), soit 4 fiches M6b, protégées ; D-i (2), soit 4 rendus appariés et 4 lectures d'aiguillage.

### 3.2 Postes (configuration recommandée ; le texte du brouillon retire les lignes D-g et D-i)

| Étape | Appels | Jetons d'entrée / sortie (SUPPOSÉ sauf mention) | Attendu b5 (bases v3) | **Attendu aux bases v6** | Moyenne tirée | **Quantile 99 % tiré (pire par poste)** | Plafond de relais b5 (÷ attendu b5) | P(dépasse ce plafond) | Plafond au quantile 90 % |
|---|---|---|---|---|---|---|---|---|---|
| É0 appels de contrôle (5 modèles) | 5 | ≈ 100 / 80 chacun (observé pour Kimi) | — | 0,0 | 0,0 | 0,0 | 0,5 (—) | 0,00 | 0,5 |
| É1 rédacteur (Sonnet 5.5), dont M6b | 6 | 270 000 / 129 000 | 2,6 | 1,8 | 1,9 | 4,0 | 3,3 (1,27) | 0,04 | 3,0 |
| É2 Kimi, passe 1 (10 fiches) | ≈ 4 | 300 000 / 140 000 (aucune mesure) | 2,0 | **2,9** | 4,5 | **20,8** | 3,0 (1,50) | **0,55** | 9,5 |
| É3 rendus : Kimi 9 + 2, Argon 9 + 2, T 10 | 32 | Kimi 8 000 / 4 000 ; Argon 5 000 / 900 (coût observé) ; T 5 000 / 2 500 | 2,0 | 2,1 | 2,7 | 5,4 | 2,8 (1,40) | **0,37** | 4,0 |
| É4 aiguilleur 56 + 4, second lecteur 10, adjudicateur, nouvel essai | ≈ 72 | 8 500 / 1 150 par lecture, au prix d'Opus | 4,1 | 4,3 | 5,1 | 14,7 | 5,5 (1,34) | **0,34** | 8,5 |
| É5 relecteur (Fable 5.1), 30 rendus | 30 | 3 000 / 340 | 1,4 | 1,4 | 1,5 | 3,2 | 1,9 (1,36) | 0,19 | 2,5 |
| É5bis seconde version des témoins (avec 0,43) | ≈ 75 | rédacteur × 0,6, rendus, relecteur, 28 lectures | 4,9 | 5,8 si elle a lieu | 6,8 | 11,3 | 6,6 (1,35) | 0,48 | 9,0 |
| É6 trois juges sur 28 rendus | 84 | Opus 17 000 / 2 300 et Argon 5 000 / 900 (coûts observés) ; Kimi 8 000 / 4 000 | 7,0 | 7,7 | 9,2 | 16,6 | 11,6 (1,66) | 0,13 | 12,5 |
| É7 passe « tableau » de Kimi, aiguilleur et second lecteur sur elle — S(4) | ≈ 24 | 300 000 / 140 000 ; 20 × 8 500 / 1 150 | 3,1 | 4,0 | 5,9 | **22,6** | 4,6 (1,48) | **0,52** | 10,5 |
| É7 lectures d'étiquettes, 10 fiches × 3 grilles × 2 lecteurs | 60 | 4 000 / 450, au prix d'Opus | 0,75 | **1,5** | 1,6 | 3,4 | 1,0 (1,33) | **0,88** | 2,5 |
| É7 fusions (3, Kimi), aiguilleur, trois juges — S(1) | 15 | fusion ≈ 25 000 / 15 000 (OBSERVÉ, appels longs) | 2,1 | 1,9 | 2,3 | 6,6 | 3,5 (1,67) | 0,11 | 4,0 |
| É7 Opus, table seule de l'axe 7 — S(3) | ≈ 2 | ≈ 75 000 / 20 000 | 0,7 | 0,7 | 0,7 | 1,2 | 1,0 (1,43) | 0,05 | 1,0 |
| É8 paraphrases (Sonnet 5.5) | ≈ 2 | ≈ 50 000 / 20 000 | 0,6 | 0,3 | 0,3 | 0,7 | 0,7 (1,17) | 0,01 | 0,5 |
| É9 antériorité, 8 fiches, 40 recherches — S(2) | 8 | 25 000 / 5 000 + 5 recherches | 2,0 | 2,0 | 2,9 | 10,5 | 6,0 (**3,00**) | 0,07 | 5,5 |
| É9b M6b, 4 fiches, lecture des PDF (protégée) | 8 | idem ; lecture d'un PDF 0,10 (b5, SUPPOSÉ) | (1,6) | 1,4 | 1,9 | 5,6 | 2,5 (1,56) | 0,20 | 3,5 |
| **Total sans seconde version** | | | **28,4** (texte du b5) | **32,1** (texte : 30,1) | | | 54,5 | | 77,0 |
| **Total, seconde version pondérée** | | | | **34,6** (texte : 32,6) | **43,5** (texte : 40,8), sans plafond ni sacrifice | | | | |

**Lecture**
- **Attendus aux bases** : proches de ceux du brouillon 5. Trois postes montent : Kimi (coupures comptées), les lectures d'étiquettes, la seconde version. Le rédacteur et le tiers T baissent : Sonnet est à son prix.
- **Moyennes tirées** : nettement au-dessus (43,5 contre 34,6). Les passes de Kimi (É2, É7) portent l'essentiel, avec leur médiane de 1,2, leur dispersion de 0,72 et leurs coupures.
- **Pire par poste (constat 5)** : la colonne « quantile 99 % tiré » donne ce que chaque étape coûterait sans relais. Ce qu'elle peut **compter** est plus court :
  - étape sacrifiable : son plafond de relais, fixe ;
  - étape protégée : son plafond de relais, élargi au plus à la marge sous S17 si les plafonds sont souples (§ 3.3) ;
  - pré-pilote entier : S17 (50 USD à la recommandation), par la règle d'A1.
- **Rapports plafond ÷ attendu du brouillon 5** : de 1,17 (É8) à 1,67 (fusions), et 3,00 pour É9 (constat 6).
- **Constat sur les lectures d'étiquettes** : le brouillon 5 compte 0,75 USD pour « trois par fiche, deux lecteurs ». À 0,025 USD par lecture (sa propre base), cela fait 30 lectures, donc un seul lecteur. Les accords S24 et S28 en demandent deux. Je compte 60 lectures (1,5 USD). **À corriger au brouillon 6.**
- **Complément conditionnel** (CP4-10, GO séparé) : 11,2 USD attendus aux bases (le brouillon 5 disait 11,6), moyenne tirée 13,3, médiane 13,0, quantile 90 % 16,3. Son plafond de 17,5 tient avec 0,951 (0,988 à la médiane 1,0 de la v5).

### 3.3 45 USD suffisent-ils ?

Règle d'A1 jouée étape par étape, dans l'ordre B. « Sacrifice » compte toute étape sacrifiable retirée ou réduite. « Non lancée » : une étape protégée ne tient pas sous S17 ; le brouillon 5 la dit « non mesuré (budget) ». « Coupée » : une étape protégée atteint son plafond de relais en cours de route (plafond élargi si souple). **Souple** : au lancement d'une étape protégée, son relais est plafonné à max(plafond de l'étape ; S17 − cumul − attendu aux bases des étapes restantes). Le relais reste donc un plafond dur, fixé au lancement.

| Configuration (configuration recommandée du b5 sauf mention) | Dépense médiane | Moyenne | Quantile 90 % | Quantile 99 % | Sacrifice | dont fusions | Protégée non lancée | **Protégée coupée** | Non lancée ou coupée |
|---|---|---|---|---|---|---|---|---|---|
| 45 / 40, plafonds du b5 fixes, texte du brouillon | 34,2 | 34,3 | 40,2 | 43,2 | 0,04 | 0,00 | 0,000 | **0,983** | 0,983 |
| 45 / 40, plafonds du b5 fixes | 36,4 | 36,4 | 41,7 | 43,8 | 0,11 | 0,03 | 0,009 | **0,991** | 0,991 |
| 45 / 40, plafonds du b5 souples, texte du brouillon | 37,7 | 37,0 | 42,3 | 44,3 | 0,30 | 0,21 | 0,029 | 0,103 | 0,111 |
| **45 / 40, plafonds du b5 souples** (nouvelle, constat 1) | 39,6 | 38,8 | 43,3 | 45,0 | 0,41 | 0,32 | 0,051 | 0,168 | 0,188 |
| 45 / 40, plafonds au quantile 90 %, fixes | 38,2 | 38,0 | 42,3 | 44,0 | 0,55 | 0,53 | 0,069 | 0,527 | 0,549 |
| 45 / 40, plafonds au quantile 90 %, souples (option (c) de la v5) | 38,4 | 38,3 | 42,5 | 44,5 | 0,58 | 0,56 | 0,088 | 0,112 | 0,166 |
| **50 / 45, plafonds du b5 souples (recommandation v6)** | **40,6** | **40,3** | **47,3** | **49,7** | **0,17** | **0,12** | **0,021** | **0,063** | **0,072** |
| idem, postes corrélés (ρ 0,5) | 38,9 | 38,1 | 48,7 | 50,0 | 0,27 | 0,20 | 0,133 | 0,157 | 0,180 |
| 50 / 45, plafonds au quantile 90 %, souples (recommandation v5) | 41,4 | 40,8 | 46,8 | 48,9 | 0,29 | 0,26 | 0,044 | 0,047 | 0,080 |
| idem, postes corrélés (ρ 0,5) | 40,0 | 38,1 | 48,1 | 49,9 | 0,33 | 0,31 | 0,141 | 0,114 | 0,169 |
| 50 / 45, plafonds au quantile 90 %, fixes | 40,9 | 40,4 | 46,6 | 48,5 | 0,23 | 0,20 | 0,033 | 0,520 | 0,531 |
| 50 / 45, plafonds au quantile 95 %, fixes | 39,8 | 39,7 | 45,5 | 48,0 | 0,43 | 0,40 | 0,032 | 0,266 | 0,284 |
| 55 / 50, plafonds au quantile 95 %, fixes | 41,9 | 41,5 | 48,9 | 52,5 | 0,17 | 0,15 | 0,015 | 0,260 | 0,270 |
| 32 / 28 (GO-2026-10-30-07 tel quel), plafonds du b5 fixes | 28,7 | 28,3 | 31,0 | 31,9 | 1,00 | 1,00 | 0,294 | 0,991 | 0,992 |

**Pont vers la v5 et le relecteur** (médiane 1,0 pour les appels isolés de Kimi, mêmes graines ; constats 1 et 7) :
- 50 / 45, plafonds du b5 souples : sacrifice 0,12, fusions 0,09, non lancée 0,010, coupée 0,043, médiane 38,8 ;
- 45 / 40, plafonds du b5 souples : 0,32 ; 0,25 ; 0,025 ; 0,123 ;
- 50 / 45, quantile 90 % souples : 0,20 ; 0,18 ; 0,031 ; 0,037 ; médiane 40,1.

Ce sont les chiffres du relecteur et ceux de la v5, à l'identique. Le passage à la médiane 1,4 durcit tout : + 0,05 à + 0,09 sur le sacrifice, + 0,01 à + 0,05 sur les étapes protégées. Il ne change pas l'ordre des options.

**Réponse.**
- **Pour la dépense, oui** : à 45 USD, avec les plafonds du brouillon 5 tenus fixes, on n'atteint jamais 45 (maximum tiré 44,9).
- **Pour le plan, non.**
  - **Ce qui casse** : avec les dispersions de P11, les plafonds de relais fixes du brouillon 5 coupent une étape protégée presque à coup sûr. En cause : les lectures d'étiquettes (0,88), É2 (0,55), É5bis si elle a lieu (0,48), É3 (0,37), É4 (0,34), É5 (0,19). Le brouillon 5 ne dit pas ce que devient une étape protégée coupée par son relais : il ne dit « non mesuré (budget) » que pour une étape non lancée (l. 292, A1). **Lecture, à confirmer au brouillon 6** : une étape protégée coupée a une mesure incomplète, donc « non mesuré (budget) », C13 non satisfaite, nœud. Le script v5 du brouillon 5 ne simulait pas ces coupures : il donnait une étape protégée non lancée avec 0,032.
  - **Élargir les plafonds de relais déplace le problème** : la règle d'A1 projette avec le plafond de chaque étape, donc des plafonds plus larges font sacrifier plus tôt. À 45 USD, au quantile 90 %, les fusions partent avec 0,56, et avec elles la chaîne de bisociation du pré-pilote.
  - **C'est la souplesse qui fait le travail** (constat 1) : à plafond égal, les plafonds du brouillon 5 rendus souples font moins sacrifier que les plafonds au quantile 90 % rendus souples (0,17 contre 0,29 à 50 USD ; 0,41 contre 0,58 à 45). Ils coupent un peu plus souvent une étape protégée (0,063 contre 0,047 à 50), à peu près autant sur « non lancée ou coupée » (0,072 contre 0,080 ; 0,180 contre 0,169 en variante corrélée).
- **Le couple recommandé** :
  - plafond **50 USD**, arrêt d'étape **45** ;
  - plafonds de relais **du brouillon 5, inchangés** ;
  - **souples** pour les étapes protégées (définition ci-dessus), fixes pour les sacrifiables.
- **Ce que ce couple donne** : sacrifice 0,17 (fusions 0,12), étape protégée non lancée 0,021, coupée 0,063 ; dépense médiane 40,6 USD, moyenne 40,3, quantile 90 % 47,3.

### 3.4 Ce qui est à porter au brouillon 6 (conv-audit, pas une décision de Lazar)

1. **Plafonds de relais** : garder ceux du brouillon 5 et rendre souples ceux des étapes protégées. Au lancement d'une étape protégée, son relais est plafonné à max(plafond de l'étape ; S17 − cumul − attendu aux bases des étapes restantes). C'est une seule règle changée dans A1 ; elle demande une contre-lecture. (La v5 proposait en plus de passer les plafonds au quantile 90 % : ce n'est plus recommandé, § 3.3.)
2. **Étape protégée coupée par son relais** : écrire son statut (lecture proposée : « non mesuré (budget) », C13 non satisfaite) ; le brouillon 5 ne le dit que pour une étape non lancée.
3. Lectures d'étiquettes : 60 lectures, pas 30 (§ 3.2).
4. Seconde version des témoins : 5,8 USD attendus aux bases si elle a lieu, contre 4,9 au brouillon 5. Elle comprend le relecteur sur 30 rendus et 28 lectures d'aiguillage.
5. Base du tiers T : prix de Sonnet 5.5 (2 / 10), au lieu du prix d'Argon.
6. Complément conditionnel : son plafond de 17,5 tient avec 0,951 aux bases v6 (médiane 1,4 pour Kimi isolé), et non plus 0,988.

## 4. Course 2 = génération 1

### 4.1 Structure chiffrée

- **Sous-sessions** : 4, comme au v3 et au v4. Kimi et Argon y font chacun 2 passes de 8 fiches, soit 128 fiches. **SUPPOSÉ** : Argon reste proposeur.
- **Bisociateur** : trois bras (R-643).
  - **Lecture B, principale** : une paire par bras et par proposeur dans chaque sous-session, soit 6 fusions par sous-session et 24 sur la course (« ≈ 12 par proposeur », n° 268 ; R-642).
  - **Lecture A** : une paire par bras et par sous-session, soit 12 fusions. C'est la lecture de C10 au brouillon 5 (S22, k = 1).
  - **Fusions** : écrites par Kimi (SUPPOSÉ, comme au brouillon 5).
  - **Lectures d'étiquettes** : 3 grilles × 2 lecteurs sur les 16 fiches de passe 1 de chaque sous-session.
- **Aiguilleur** : sur toutes les fiches et toutes les fusions, avant tout juge.
- **Notation croisée** : Argon note les fiches de Kimi et les fusions, Kimi note les fiches d'Argon. 8 témoins par lot, notés par les deux, réutilisés du pré-pilote, sans rendu nouveau (SUPPOSÉ).
- **Opus 5.5 troisième juge** : toutes les fiches, fusions et témoins.
- **Mode de jugement** : par lots, comme en course 1 (SUPPOSÉ ; la v53 le fixera). Kimi en lot est observé : médiane 1,0. La variante « un appel par fiche » est chiffrée au § 4.3.
- **Antériorité** : 10 fiches notables par sous-session, plus la moitié des fusions.
- **Contrôles d'Argon** : un lancement par sous-session (SUPPOSÉ).

### 4.2 Postes, 4 sous-sessions, lecture B

| Poste | Appels | Jetons d'entrée / sortie | Base | **Attendu aux bases** (coupures comptées) | Pire |
|---|---|---|---|---|---|
| Kimi proposeur (8 passes de 8) | ≈ 24 | 2 000 000 / 600 000 (SUPPOSÉ, aucune mesure) | 10,0 | **14,5** | 38,0 |
| Argon proposeur (8 passes) | ≈ 8 à 24 | ≈ 1 600 000 / 256 000 (découpage SUPPOSÉ, coût OBSERVÉ) | 24,0 | **24,0** | 32,2 |
| Contrôles d'Argon (4 lancements) | 4 lots | inconnus (coût OBSERVÉ : 1,75 par lancement) | 7,0 | **7,0** | 12,0 |
| Aiguilleur (152) | 152 | 1 292 000 / 174 800 | 8,7 | 8,7 | 23,3 |
| Juges croisés : Argon sur 120, Kimi sur 96 | Argon ≈ 8 ; Kimi 4 lots | Argon 600 000 / 108 000 ; Kimi 737 000 / 102 600 (OBSERVÉ par fiche) | 11,9 | 13,1 | 27,3 |
| Opus 5.5 troisième juge (184) | ≈ 24 | 3 128 000 / 423 200 (coût OBSERVÉ par fiche) | 21,0 | 21,0 | 28,2 |
| Antériorité (52) | 52 + 260 recherches | 1 300 000 / 260 000 | 13,0 | 13,0 | 44,2 |
| Lectures d'étiquettes (384) | 384 | 1 536 000 / 172 800 | 9,6 | 9,6 | 14,4 |
| Fusions par Kimi (24) | 24 | ≈ 600 000 / 360 000 (OBSERVÉ par appel) | 4,9 | 7,1 | 21,4 |
| Tableau minimal (programme), appels de contrôle | — | — | 0,0 | 0,0 | 0,5 |
| **Total** | | | **110,1** | **117,9** | **241,3** |

### 4.3 Variantes

| Variante | Attendu aux bases | Pire | **Moyenne tirée** | Médiane tirée | Quantile 90 % | Corrélé (ρ 0,5) : médiane ; quantile 90 % |
|---|---|---|---|---|---|---|
| 4 sous-sessions, lecture B | 117,9 | 241,3 | **139,2** | 134,9 | 173,9 | 129,9 ; 203,6 |
| 4 sous-sessions, lecture A | 109,8 | 220,6 | 129,3 | 125,1 | 161,2 | 120,7 ; 188,5 |
| 3 sous-sessions, lecture B | 88,4 | 181,1 | 104,4 | 101,1 | 130,4 | 97,4 ; 152,9 |
| 3 sous-sessions, lecture A | 82,3 | 165,2 | 96,8 | 93,6 | 120,8 | 90,3 ; 141,2 |
| 2 sous-sessions, lecture B | 58,9 | 120,9 | 69,6 | 67,3 | 87,1 | 64,9 ; 102,0 |
| 2 sous-sessions, lecture A | 54,9 | 110,6 | 64,6 | 62,4 | 80,9 | 60,3 ; 94,3 |
| 4, B, juges en appel isolé (une fiche par appel) | 122,2 | 246,9 | — | — | — | — |
| 4, B, un seul lancement (contrôles d'Argon une fois) | 112,6 | 232,3 | — | — | — | — |
| 4, B, allégée (4 témoins par lot, antériorité sur 6 notables) | 110,2 | 221,2 | — | — | — | — |
| 4, B, recherche à 0,05 USD | + 10,4 | — | — | — | — | — |

**Lecture**
- **Moyenne, médiane et attendu aux bases** : la moyenne et la médiane tirées dépassent l'attendu aux bases, pour deux raisons. Les médianes de P11 sont prises à 1,2 pour Kimi proposeur et l'antériorité, et la somme de lois log-normales est asymétrique (constat 2).
- **Ce que coûte une sous-session** : ≈ 29,5 USD attendus aux bases (≈ 35 en moyenne tirée). C'est l'unité de réduction de GO-2026-10-30-07.
- **Du v4 au v5 (lecture B, + 33,2 USD), par cause, en chaîne** (constat 8 ; calcul du script, de la v4 publiée lecture A à la v5 lecture B) :

| Maillon | Attendu aux bases | Écart (USD) |
|---|---|---|
| v4 publiée, lecture A (2 bras, 8 fusions, une grille) | 84,7 | — |
| même structure, **bases recalées sur l'observé** : Argon proposeur + 6,1 ; contrôles d'Argon par lancement + 5,3 ; coupures sur Kimi proposeur + 4,5 ; coupures sur Kimi juge + 1,1 ; fusion observée (0,204 au lieu de 0,40), coupures comprises − 0,8 | 100,8 | + 16,1 |
| **+ trois grilles d'étiquettes** (plan du brouillon 5, É7 ; pas le troisième bras) | 107,2 | + 6,4 |
| **+ troisième bras**, basique (R-643) : 12 fusions, lecture A | 109,8 | + 2,7 |
| **+ lecture B** : une paire par bras et par proposeur, 24 fusions (n° 268, R-642) | 117,9 | + 8,0 |

  La v5 écrivait « ≈ 17 observés + ≈ 16 du troisième bras ». Elle comptait dans le troisième bras les trois grilles, qui viennent du plan du brouillon 5, et la lecture B, qui vient du n° 268.
- **Leviers sans perte d'objectif** :
  - un seul lancement pour les contrôles d'Argon : − 5,3 USD, si la v53 le permet ;
  - lecture A : − 8,1 USD, mais deux fois moins de fusions pour comparer les bras ;
  - allégement : − 7,7 USD, mais moins d'antériorité vérifiée.

## 5. Totaux et plafond total

| | Attendu aux bases | Moyenne tirée | Médiane tirée | Pire |
|---|---|---|---|---|
| Pré-pilote (configuration recommandée, seconde version pondérée) | 34,6 | 43,5 sans plafond ; 40,3 sous la règle d'A1 (50 / 45, plafonds du b5 souples) | 40,6 (sous la règle d'A1) | 50 (S17, règle d'A1) |
| Course, 4 sous-sessions, lecture B | 117,9 | 139,2 | 134,9 | 241,3 |
| **Total** | **≈ 152,5** | ≈ 179,5 | — | **≈ 291** |
| Hors total : complément conditionnel du pré-pilote (proposé avec 0,20) | 11,2 | 13,3 | 13,0 | 17,5 (plafond b5) |
| Hors total : machine jetable (devis machine v2) | 0,5 | — | — | 7,4 (GO proposé 10) |
| Hors total : appels de modèle des tests de mort (v52 : 0,6 USD par fiche) | 3,0 (5 fiches) | — | — | 7,2 (12 fiches) |

**Ce que la course peut faire selon le plafond total.** La dépense du pré-pilote est tirée par la règle d'A1 à 50 / 45, plafonds du brouillon 5 souples. Le complément est proposé avec 0,20 ; son coût est tiré et pris sur le reste, comme au brouillon 5 (constat 3). La course est tirée au même modèle. Reste = total − dépense du pré-pilote − complément. Probabilités : 4 sous-sessions ; 3 ; 2 ; aucune course.

| Plafond total | Reste médian (avec complément) | **Lecture B, avec complément** | Lecture B, sans complément | Lecture A, sans complément | B, corrélé ρ 0,5, sans complément |
|---|---|---|---|---|---|
| 110 (GO-2026-10-30-07) | 67,5 | 0,000 ; 0,014 ; 0,466 ; **0,520** | 0,000 ; 0,017 ; 0,539 ; 0,444 | 0,000 ; 0,046 ; 0,649 ; 0,305 | 0,040 ; 0,146 ; 0,415 ; 0,398 |
| 123 (lecture « total 123 » du b5, plafond 45) | 80,5 | 0,001 ; 0,106 ; 0,675 ; 0,218 | 0,001 ; 0,126 ; 0,710 ; 0,163 | 0,006 ; 0,236 ; 0,665 ; 0,093 | 0,105 ; 0,234 ; 0,431 ; 0,231 |
| 128 (même lecture, plafond 50) | 85,5 | 0,004 ; 0,173 ; 0,680 ; 0,143 | 0,004 ; 0,206 ; 0,687 ; 0,103 | 0,017 ; 0,333 ; 0,592 ; 0,057 | 0,138 ; 0,263 ; 0,412 ; 0,187 |
| 140 | 97,5 | 0,031 ; 0,375 ; 0,543 ; 0,052 | 0,037 ; 0,424 ; 0,505 ; 0,035 | 0,090 ; 0,534 ; 0,355 ; 0,021 | 0,234 ; 0,314 ; 0,343 ; 0,109 |
| **160** | **117,5** | **0,213 ; 0,550 ; 0,227 ; 0,010** | 0,246 ; 0,556 ; 0,191 ; 0,007 | 0,398 ; 0,489 ; 0,108 ; 0,004 | 0,424 ; 0,315 ; 0,216 ; 0,045 |
| 180 | 137,5 | 0,530 ; 0,397 ; 0,071 ; 0,002 | 0,572 ; 0,369 ; 0,057 ; 0,002 | 0,716 ; 0,251 ; 0,031 ; 0,002 | 0,602 ; 0,254 ; 0,124 ; 0,020 |

- **Lecture « total 123 » au sens strict** (brouillon 5, S17, C10 : la course garde 110 − 32 = 78, quoi que dépense le pré-pilote) : lecture B, 4 sous-sessions 0,000 ; 3 : 0,054 ; 2 : 0,724 ; aucune 0,222 (avec complément : 0,000 ; 0,045 ; 0,661 ; 0,294). Lecture A : 0,001 ; 0,135 ; 0,735 ; 0,129.
- **Écart avec le brouillon 5** : il donne C10 à 0,98 sous cette lecture, sur un devis médian de 103 USD pour k = 1 ; sur mes bases, une course à 2 sous-sessions au moins tient avec ≈ 0,78 (lecture B) ou 0,87 (A), et à 3 au moins avec 0,05 à 0,14.
- **Comparaison** : avec la recommandation de la v5 au pré-pilote (quantile 90 % souples), les chiffres bougent de 0,013 au plus (sortie, second bloc), parce que les dépenses médianes ne diffèrent que de 0,8 USD.

Le séquençage de GO-2026-10-30-07 tient dans tous les cas :
- les relais sont plafonnés à chaque lancement ;
- la course n'est lancée que si son devis, refait sur les mesures du pré-pilote, tient dans le reste ;
- sinon, elle est réduite. L'ordre de retrait des sous-sessions est à dire d'avance (par exemple, l'axe 6 avec pistes en premier).

Le pré-pilote mesure trois facteurs du pire : Kimi proposeur sur une passe, Kimi juge et l'antériorité. Il mesure aussi l'aiguillage et le taux de coupure de Kimi.

## 6. Machine jetable (à part)

- **Renvoi** : devis machine v2 (`docs/notes/ideation-organisme-v1/machine-jetable-v1/devis-et-plomberie-machine-jetable-v2.md`, `39260994…`), qui remplace la v1.
- **Machine** : Hetzner CPX32, 0,0577 EUR de l'heure hors taxes.
- **Coût** : ≈ 0,5 USD attendus et ≈ 7,4 au pire pour les séries S0, S1 et P de la génération 1. GO proposé : 10 USD, échéance le 15 novembre.
- **Appels de modèle des tests de mort** : hors devis machine, sur une ligne de GO à part. Le devis machine v2 (l. 559-560) reprend deux défauts de la v52, 0,5 USD pour le test (`BUDGET_TEST_USD_DEFAUT`) et 0,1 pour le lecteur (`BUDGET_LECTEUR_USD_DEFAUT`), tous deux SUPPOSÉS par leur auteur : 3,0 USD pour 5 fiches, 7,2 pour 12. La v52 elle-même reste introuvable dans git (n° 269) : ces deux valeurs ne sont pas relues à la source. Ils viennent **après** la course.
- **Devis machine v3** : une v3 (`devis-et-plomberie-machine-jetable-v3.md`, `864f3d27…`, compagnon daté de 01:12 UTC) est apparue pendant la rédaction de ce devis. Elle corrige sept défauts de plomberie et de garde et écrit « Le devis ne change pas » (≈ 0,5 USD attendus, ≈ 7,4 au pire, GO proposé 10 USD ; la ligne des 0,6 USD par fiche est à sa l. 745). Je ne l'ai pas relue en entier : le renvoi reste à la v2, et les montants sont les mêmes.
- **Ce que la v2 demande à Lazar** : ce GO ; le poste de passage (son ordinateur) ; le choix du projet Hetzner ; l'accord sur l'écart d'hôte AppArmor (R-a). Rien de cela n'est repris ici.

## 7. Ce que je ne sais pas (SUPPOSÉ)

- **Kimi proposeur** : aucune mesure. Les profils de 250 000 / 75 000 jetons par passe de course et de 300 000 / 140 000 par passe du pré-pilote sont ceux du v4. Les appels longs observés (12 000 à 21 000 jetons de sortie chacun) les rendent plausibles, pas mesurés.
- **Coupures de Kimi** : le taux de 0,2 repose sur ≈ 13 appels longs. Le coût réel d'une coupure est inconnu : console Moonshot. Les tours du tableau partagé et de la bisociation ne sont pas dépouillés ici.
- **Contrôles d'Argon** : 1,75 USD a été observé une fois, et j'ignore leur nature. J'ai supposé un lancement par sous-session ; avec un seul lancement, la course coûte − 5,3 USD.
- **Argon** : prix de sortie (41,5) non lu. Le découpage en jetons des passes et des jugements est conjectural ; seul le coût est observé.
- **Argon proposeur à 3,00 par passe** (ajout du relecteur de la v5) : les 6,00 USD de la course 1 ont été dépensés alors qu'Argon était aussi juge, et « aucun juge n'a rendu de classement » (R-804). Une part de ces 6,00 pourrait venir du rôle de juge ; la passe serait alors un peu surestimée. C'est plausible, pas établi ; la base est gardée, au sens prudent.
- **Jugement isolé** : 0,057 par fiche pour Kimi, au lieu des 0,026 du lot, tiré à la médiane 1,4 de P11 (v6). Aucune mesure d'un appel isolé n'existe pour aucun juge. Si Opus et Argon coûtent plus en appel isolé qu'en lot, É6 monte : son plafond de relais de 11,6 est déjà dépassé avec 0,13 aux bases v6.
- **Rendus de Kimi** : même base (0,057) et même médiane 1,4 que le jugement isolé, par la même règle ; aucune mesure.
- **Prix de la recherche** : 0,01 est le prix de liste des agents gérés. Celui de l'API Messages n'est pas lu.
- **v53 non écrite** : elle fixera la lecture A ou B, qui fusionne, le découpage des juges (lots ou appels isolés), le nombre de lancements, le maintien d'Argon proposeur, le contenu du tableau minimal et la voie d'Opus troisième juge.
- **Brouillon 6** : la contre-lecture 4 (R-663) en demande un ; il est en cours. Il peut changer les effectifs, l'ordre des étapes (CP5-04) et la règle d'A1 (CP5-02, CP5-06).
- **Bras méta** : son annexe n'est pas écrite. Une grille plus riche ou la carte des chapelles peut doubler ses lectures (≈ + 3 USD sur la course).
- **Bras Gu-Krenn simplifié** : les cooccurrences passent par OpenAlex sur l'allocation gratuite (0 USD). Un modèle n'est pas compté.
- **Témoins de la course** : je les suppose réutilisés du pré-pilote, sans rendu nouveau. Les écrire à nouveau coûterait ≈ 0,2 USD par témoin.
- **Écriture des 12 concrets de l'aiguilleur** : comptée à 0 USD, sous-agent et abonnement de la session (R-819 non tranchée).
- **Complément** : sa proposition (0,20) est tirée indépendamment des coûts, alors que le brouillon 5 la lie au verdict de M1 ; le complément entier ne bouge aucune probabilité du § 5 de plus de 0,08 ; l'effet de cette indépendance est plus petit encore.

## 8. Réserves

- **Confidentialité** : Kimi juge les fiches d'Argon, et les sorties de l'axe 6 partent chez Moonshot. Les fiches aiguillées ne partent chez aucun juge. À confirmer par Lazar avant le pré-pilote.
- **Écart avec le brouillon 5** : il donne C10 (la course tient dans le reste) à 0,92, sur un devis médian de 103 USD pour k = 1. Sur mes bases, la course médiane à 4 sous-sessions en lecture A coûte 125. C10 vaut donc moins au plafond de 110, et le brouillon 6 doit reprendre ce devis.
- **Écart de lecture des fusions** : 24 pour conv-audit (n° 268, R-642), 12 pour le brouillon 5. C'est la décision 3.
- **Aucune bascule de modèle** sans le mot de Lazar.
- **GO-2026-10-30-07 expire le 6 novembre.** La ligne de GO nouvelle est à écrire par la session principale, sur le mot direct de Lazar.
- **R4, symétrie** : la coupure par les relais à 0,99 (plafonds fixes) est un résultat « trop sale » du modèle ; je l'ai donc éprouvé (fin de la sortie). Au compte de lectures d'étiquettes du brouillon 5 (30), elle vaut encore 0,938 ; avec, en plus, des dispersions divisées par deux, 0,803. Elle tient surtout à É2 (attendu aux bases 2,9 pour un plafond de 3,0, à cause des coupures de Kimi) et aux plafonds fixés à ≈ 1,2 à 1,7 fois l'attendu du brouillon 5. Elle reste à revoir quand le pré-pilote aura mesuré ses rapports réels.
- **Option recommandée au pré-pilote, pas meilleure partout** : elle coupe un peu plus souvent une étape protégée (0,063 contre 0,047), et un peu plus en variante corrélée sur « non lancée ou coupée » (0,180 contre 0,169). Je le déclare plutôt que d'écrire « domine ».

## 9. Décisions pour Lazar (nœuds de dépense ; aucune n'a de défaut)

### Décision 1 — plafond du pré-pilote (S17)

**Décision** : quel plafond, quel arrêt d'étape et quelle forme des plafonds de relais pour le pré-pilote recentré ?

**Enjeu** : à 45 USD, la dépense tient, mais le plan ne passe pas. Avec les plafonds de relais du brouillon 5 tenus fixes, une étape protégée bute presque toujours sur le sien. La souplesse règle cela ; l'élargissement fait sacrifier les fusions.

**Options**
- **(a) 45 / 40, plafonds de relais du brouillon 5, fixes.**
  - Avantage : la recommandation actuelle (R-630, brouillon 5) ; ne dépasse jamais 45.
  - Inconvénient : une étape protégée est coupée avec 0,99 (C13 fermée, nœud, lecture à confirmer au brouillon 6).
- **(b) 50 / 45, plafonds de relais du brouillon 5, rendus souples pour les étapes protégées** (nouvelle, constat 1 ; une règle à écrire au brouillon 6).
  - Avantage : sacrifice 0,17 (fusions 0,12) ; étape protégée non lancée 0,021, coupée 0,063 ; dépense médiane 40,6 USD (moyenne 40,3) ; une seule règle changée.
  - Inconvénient : 5 USD de plus engagés sur le plafond total ; règle nouvelle à contre-lire ; un peu plus de coupures que (d).
- **(c) 45 / 40, plafonds de relais du brouillon 5, souples** (nouvelle).
  - Avantage : garde 45 ; une seule règle changée.
  - Inconvénient : sacrifice 0,41 (fusions 0,32) ; étape protégée non lancée 0,051, coupée 0,168.
- **(d) 50 / 45, plafonds au quantile 90 %, souples** (recommandation de la v5).
  - Avantage : coupure la plus basse (0,047) ; non lancée 0,044.
  - Inconvénient : sacrifice 0,29 (fusions 0,26) ; deux règles changées ; dépense médiane 41,4.
- **(e) 45 / 40, plafonds au quantile 90 %, souples** (option (c) de la v5).
  - Avantage : garde 45.
  - Inconvénient : fusions sacrifiées avec 0,56 ; non lancée 0,088 ; deux règles changées. Fait moins bien que (c) sur le sacrifice et la non-lancée, mieux sur la coupure (0,112 contre 0,168).

**Recommandation** : **(b)**, confiance 0,6. Contre (d), elle gagne 0,12 sur le sacrifice, perd 0,016 sur la coupure et garde les plafonds déjà écrits du brouillon 5. Si Lazar tient à 45, (c) plutôt que (e).

**Défaut** : aucun. Sans mot de Lazar, GO-2026-10-30-07 reste tel quel (pré-pilote ≤ 32), et rien n'est lancé à 32 : le brouillon 5 prévoit l'arrêt par A15.

### Décision 2 — plafond total de la course 2 (génération 1)

**Décision** : quel plafond total séquencé pour le pré-pilote et la course ?

**Enjeu** : sur les coûts observés, la course à 4 sous-sessions coûte ≈ 117,9 USD attendus aux bases (moyenne tirée ≈ 139, médiane ≈ 135, pire ≈ 241). Le total actuel de 110 ne la laisse à 4 sous-sessions qu'avec < 0,01, et sans aucune course avec 0,52 (complément compté).

**Options** (pré-pilote à l'option (b) de la décision 1 ; complément compté sur le reste ; lecture B ; entre parenthèses, sans complément)
- **(a) 160 USD.**
  - Avantage : 3 sous-sessions au moins avec 0,76 (0,80), et 4 avec 0,21 (0,25 ; 0,40 en lecture A sans complément).
  - Inconvénient : 50 USD de plus que GO-2026-10-30-07 ; le pire (≈ 291) reste hors plafond, tenu par le seul séquençage.
- **(b) 180 USD.**
  - Avantage : 4 sous-sessions avec 0,53 (0,57 ; 0,72 en lecture A sans complément).
  - Inconvénient : 70 USD de plus ; peu de gain si 3 sous-sessions suffisent à l'objectif.
- **(c) 140 USD.**
  - Avantage : 30 USD de plus seulement.
  - Inconvénient : course à 2 sous-sessions avec 0,54, à 4 avec 0,03.
- **(d) 110 USD, gardé.**
  - Avantage : rien ne bouge.
  - Inconvénient : course à 2 sous-sessions au mieux (0,47) ; aucune avec 0,52.
- **(e) lecture « total 123 » du brouillon 5** (LECTURE À CONFIRMER de S17, C10 et DEP6 : la ligne nouvelle du pré-pilote s'ajoute au total séquencé ; 128 si le pré-pilote est à 50).
  - Avantage : la plus petite hausse (13 ou 18 USD) ; déjà écrite au brouillon 5.
  - Inconvénient : à 128, 3 sous-sessions au moins avec 0,18 (0,21), aucune course avec 0,14 ; si la course garde 78 au sens strict : 3 au moins 0,045, aucune 0,29.

**Recommandation** : **(a) 160**, séquencé, avec l'ordre de retrait des sous-sessions dit d'avance. Le levier « un seul lancement des contrôles d'Argon » (− 5,3 USD) est à demander à la v53. Confiance 0,5 : le choix entre (a) et (b) dépend de ce que vaut pour Lazar la quatrième sous-session.

**Défaut** : aucun.

### Décision 3 — nombre de fusions de la course (lecture de « une paire par session »)

**Décision** : 24 fusions (une paire par bras et par proposeur dans chaque sous-session) ou 12 (une paire par bras et par sous-session) ?

**Enjeu** : ≈ 8 USD attendus aux bases (117,9 contre 109,8 ; ≈ 10 en moyenne tirée, 139,2 contre 129,3), et l'effectif de la comparaison entre bras, qui est la raison de garder le bras basique (R-642).

**Options**
- **(a) 24 (lecture B).**
  - Avantage : lettre du n° 268 et de R-642 ; 8 fusions par bras au lieu de 4.
  - Inconvénient : + 8 USD ; 4 sous-sessions moins probables à plafond égal.
- **(b) 12 (lecture A).**
  - Avantage : − 8 USD ; lecture du brouillon 5 (S22, k = 1).
  - Inconvénient : 4 fusions par bras : aucune comparaison lisible.

**Recommandation** : **(a)**, confiance 0,55. À 4 fusions par bras, garder le basique « pour comparaison » n'a guère de sens.

**Défaut** : aucun. À trancher avant la v53 et le gel de S22.

### Hors de ce devis (GO séparés, rappel)

- **Machine jetable** : 10 USD (devis machine v2, § 6).
- **Appels de modèle des tests de mort** : 3 à 7,2 USD.
- **Complément conditionnel du pré-pilote** : plafond 17,5 USD, sur proposition après la porte.
