# Devis de la course 2 (génération 1) et du pré-pilote recentré — bisociateur à trois bras, Kimi proposeur, notation croisée, Opus troisième juge — v5

Lignée session-depot (sous-agent), 31 octobre 2026, écrit vers 00:50 UTC (`date -u`). **Rien n'est lancé, aucun appel payant n'a servi à ce devis** (le skill `claude-api` a été lu sur disque pour les prix, sans appel). C'est un nœud de dépense : chaque lancement aura sa ligne de GO, écrite par la session principale sur le mot direct de Lazar. Ce devis n'écrit rien dans `registres/`.

**Remplace** le devis v4 (`devis-course-2-et-pre-pilote-v4.md`, `03e961d5…`, script `011a0fc2…`, sortie `b3c6a087…`), archivé sans modification (R12).

**Ce qu'il prend en compte**
- le rapport du relecteur de la v4 (`nuit-rendus/verifier-devis-v4-course2.md` du bloc-notes de la session, `b39be6fe…`) : ses huit défauts sont traités au § 1.2 ;
- les messages de conv-audit (branche `origin/canal/conv-audit-n04`, `cbdbc739`) : n° 266 (`b78f9b1e…`, pré-pilote recentré), n° 267 (`0c77987a…`, machine jetable, course 2 = génération 1), n° 268 (`49a64a80…`, trois bras, « ≈ 12 fusions par proposeur »), n° 269 (`b5f7057e…`, plafond 45 USD recommandé, machine jetable) ;
- les décisions relayées dans le registre de conv-audit (même branche, fichier `86cd5d5e…`) : **R-643, décision de Lazar** (« bras basique : garder » → trois bras, méta, Gu-Krenn et basique, une paire par session chacun) ; **R-642**, recommandation de conv-audit (« ≈ +4 fusions par proposeur ») ; **R-640, décision de Lazar** (machine jetable) ; **R-630, recommandation** de conv-audit (plafond du pré-pilote à 45 USD, sur le mot de Lazar « on augmente le plafond ») ; R-662 et R-663 (brouillon 5 et sa contre-lecture 4) ;
- **le brouillon 5 du préenregistrement du pré-pilote**, plus récent que le brouillon 4 visé par le relecteur (`preenregistrement-pre-pilote-course-2-brouillon5.md`, `96080471…`, script `96ee5852…`, sortie `d342b569…`) : 28 fonds, trois bras, ordre des étapes B, règle de sacrifice d'A1, plafonds de relais par étape, plafond 45 et arrêt d'étape 40 ;
- les coûts réels de la nuit (`registres/depenses.md`, `a0d521ea…`, l. 249 à 264) et les journaux des relais de Kimi et du collisionneur (§ 2.2) ;
- le devis de la machine jetable v2 (`machine-jetable-v1/devis-et-plomberie-machine-jetable-v2.md`, `39260994…`), auquel ce devis renvoie (§ 6).

Tous les chiffres sortent du script `calcul-devis-course-2-et-pre-pilote-v5.py` (`06a9ad87…`) et de sa sortie `calcul-devis-course-2-et-pre-pilote-v5.sortie.txt` (`d1182707…`), même dossier, compagnons `.sha256`. Rejeu `python3 -I` (numpy 2.5.3) : sortie identique octet pour octet ; avec le `.venv` (numpy 2.4.6), seule la ligne des versions change. Montants arrondis au dixième.

## 0. Verdict

- **Pré-pilote (brouillon 5) : ≈ 32,6 USD attendus au texte du brouillon, ≈ 34,6 dans la configuration recommandée** (D-g (b) et D-i (2), que le brouillon 5 ne chiffrait pas, CP5-05). Le brouillon 5 disait 28,4.
- **45 USD suffisent pour la dépense, pas pour le plan.** Avec les plafonds de relais du brouillon 5, la dépense reste sous 45 (quantile 99 % : 43,5 USD). Mais **une étape protégée bute sur son plafond de relais avec 0,98** : ces plafonds valent ≈ 1,35 fois l'attendu, sous les dispersions de P11. Avec des plafonds de relais au quantile 90 % de chaque étape, rendus « souples » (§ 3.4), on obtient :
  - **à 45 USD** : un sacrifice avec 0,49 (fusions retirées 0,47), une étape protégée non lancée avec 0,065 ;
  - **à 50 USD, arrêt d'étape 45** : un sacrifice avec 0,20, une étape protégée non lancée avec 0,031, une étape coupée avec 0,037 ; dépense médiane 40,1 USD, quantile 90 % 46,4.
  - **Recommandation : 50 USD.**
- **Course 2, 4 sous-sessions, lecture B (24 fusions, ≈ 12 par proposeur, R-642 et n° 268) : ≈ 118 USD attendus, médiane tirée ≈ 135, ≈ 241 au pire.** En lecture A (12 fusions) : ≈ 110 attendus, ≈ 221 au pire. La v4 annonçait 85 attendus et 180 au pire pour deux bras.
  - L'écart vient des bases recalées sur les coûts observés : Argon proposeur, contrôles d'Argon, coupures de Kimi comptées au pire (≈ + 17 USD). Il vient aussi du troisième bras : trois grilles de lecture d'étiquettes, 24 fusions, et leur aiguillage, leurs jugements et leur antériorité (≈ + 16).
- **Le plafond total de 110 USD ne laisse aucune chance à 4 sous-sessions (0,00) et aucune course avec 0,42.** Il faut 160 USD pour une course à 3 sous-sessions au moins avec 0,82, et 180 pour 4 sous-sessions avec 0,58 (§ 5).
- **Machine jetable** : à part, devis machine v2 (≈ 0,5 USD attendus, ≈ 7,4 au pire, GO proposé 10 USD), plus les appels de modèle des tests de mort, 0,6 USD par fiche au défaut de la v52 (§ 6).

## 1. Ce qui change depuis la v4

### 1.1 Postes

| Poste | v4 | v5 | Raison |
|---|---|---|---|
| Bras de bisociation | 2 (méta, Gu-Krenn) | **3 (méta, Gu-Krenn, basique)** | R-643 (décision de Lazar) ; n° 268 |
| Fusions de la course | 8 (lecture A) ou 16 (B) | **24 (lecture B, principale)** ou 12 (A) | « une paire par session chacun », « ≈ 12 fusions par proposeur » (n° 268) ; R-642 : « ≈ +4 fusions par proposeur » pour le basique |
| Lectures d'étiquettes | 2 lecteurs, une grille | **2 lecteurs × 3 grilles** (liste fermée, vocabulaire Gu-Krenn, niches du bras méta) | brouillon 5, É7 |
| Pré-pilote | plan du v4 (24 témoins) | **plan du brouillon 5** : 28 fonds, 56 lectures d'aiguillage, 3 fusions, seconde version, passe « tableau », table de l'axe 7, M6b en option | brouillon 5 (R-662) |
| Argon proposeur | 2,24 USD par passe | **3,00 par passe (OBSERVÉ)** ; pire 4,02 | relecteur, défaut 2 ; `depenses.md` l. 250 |
| Contrôles d'Argon | 1,75 pour toute la course | **1,75 par lancement**, un lancement par sous-session (SUPPOSÉ) | observé une fois, pour un lancement de 16 fiches (l. 250) |
| Coupures de Kimi | non comptées | **facteur 1,45 sur la dépense comptée** de chaque poste de Kimi | ≥ 3 coupures sur ≈ 13 appels longs le 30 octobre (§ 2.3) |
| Fusion d'une paire | 0,40 (SUPPOSÉ) | **0,204 (OBSERVÉ)**, 0,30 compté avec coupures ; pire 0,89 | médiane de 7 appels longs de Kimi (§ 2.2) |
| Kimi juge, appel isolé (pré-pilote, É6) | 0,026 (lot) | **0,057** par fiche | le brouillon 5 juge une fiche par appel ; l'observé (0,026) vaut pour un lot de 29 |
| Sonnet 5.5 | 4 / 20 (SUPPOSÉ, prix d'Opus) | **2 / 10 (SOURCÉ)** | table du skill `claude-api` |
| Recherche sur le Web | 0,01 (SUPPOSÉ) | **0,01 (SOURCÉ)** ; pire 0,05 | skill `claude-api`, `shared/managed-agents-core.md` l. 205 |
| Dispersions | 0,35 à 0,5 | **celles de P11** (0,22 à 0,72) | relecteur, défaut 3 |

### 1.2 Défauts du relecteur de la v4

| N° | Défaut | Traitement |
|---|---|---|
| 1 (majeur) | Dépassé par R-643 et le n° 268 (trois bras) ; effectifs du brouillon 4 | trois bras, lectures A et B ; effectifs du **brouillon 5** (plus récent que le brouillon 4) ; option (a) recalculée (§ 5) ; il faut désormais **160 USD**, pas 140 |
| 2 (moyen) | Argon proposeur sous l'observé | attendu 3,00 par passe, pire × 1,34 = 4,02 |
| 3 (moyen) | Dispersions plus étroites que P11 | σ = ln(haut ÷ bas) ÷ 2,563, tiré de chaque intervalle à 80 % de P11 (brouillon 5, l. 134) ; « probabilité nulle » n'est plus écrit ; une variante corrélée (ρ 0,5) est ajoutée |
| 4 (mineur) | Arrondis du § 0 | tous les montants au dixième, tels que la sortie les donne |
| 5 (mineur) | Attribution des décisions | décisions de Lazar : R-640, R-643 ; recommandations de conv-audit : R-630, R-642 (en-tête) |
| 6 (mineur) | Prix de la recherche | 0,01 sourcé (prix de liste) ; variante à 0,05 chiffrée : + 10,4 USD sur la course |
| 7 (mineur) | Postes sans compte d'appels | chaque poste a ses appels et ses jetons (§ 3.2, § 4.2), estimés et marqués SUPPOSÉ quand ils ne sont pas observés |
| 8 (information) | Interpréteur | usage écrit en tête du script ; rejeu vérifié avec les deux numpy |

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

### 2.2 Coûts observés retenus (`registres/depenses.md`, journaux)

| Observation | Source | Ce qu'elle fixe |
|---|---|---|
| Argon proposeur : 6,00 USD pour 2 passes de 8 fiches ; contrôles externes 1,75 | l. 250 (course 1, tentative 2) | passe d'Argon 3,00 ; contrôles 1,75 par lancement |
| Juges sur 29 fiches : Opus 3,31 en 6 appels (0,114 par fiche) ; Argon 2,28 (0,079) | l. 252 | jugements d'Opus et d'Argon |
| Kimi juge, lot de 29 : 222 635 / 31 010 jetons, 0,755 USD ; premier essai coupé à 300,7 s, 2,03 compté au pire | l. 254-255 | 0,026 par fiche en lot ; une coupure |
| Appels longs de Kimi au collisionneur : 7 réussis, de 0,137 à 0,241 USD, médiane 0,204 (entrée 5 112 à 33 347, sortie 12 487 à 21 433, dont 46 à 85 % de raisonnement) | `donnees/collisionneur-texte-III-v1/run-texte-III-e3-v2/journal.jsonl` (`dfc54365…`), `run-texte-III-etroite-e3-v1/journal.jsonl` (`93a372fa…`) | fusion d'une paire |
| Tour étroit : appel de Kimi coupé (ConnectionResetError à 37 s), 0,355 compté au pire, puis rejoué pour 0,2246 | `relais-kimi-texte-III-etroite-journal-v1.jsonl` (`c4888981…`), `…-reprise-journal.jsonl` (`a137ee1c…`) ; l. 259 | une coupure |
| Tour P-041 : appel de Kimi coupé, 0,48 compté au pire ; 1,95 USD comptés au pire sur trois relais | l. 262 ; R-864 | une coupure |
| Argon, cellules longues du collisionneur : 7 013 à 13 542 jetons de sortie | mêmes journaux | Argon écrit long : appui de la passe à 3,00 |
| Tours du collisionneur de la nuit : 8,01 ; 8,16 ; 20,30 USD (12 cellules chacun) | l. 260, 262, 263 | **non retenus** : le collisionneur ne sert pas dans la course |
| OpenAlex : 197 681 œuvres sur l'allocation gratuite (0,99 USD de crédits gratuits, aucune facture) | l. 264 | cooccurrences du bras Gu-Krenn simplifié comptées à 0 (SUPPOSÉ) |

### 2.3 Coupures de Kimi (nouveau poste)

- **Faits** : le 30 octobre, au moins 3 appels longs de Kimi ont été coupés sur ≈ 13. Le relais compte chaque coupure au pire (réservation), puis l'appel est rejoué. Rapport réservation ÷ coût réel : 2,7, puis 1,6, puis 2,4.
- **Modèle** : probabilité 0,2 par appel, rapport tiré parmi les trois observés. La dépense comptée sur un poste de Kimi vaut donc **1,45 fois** son coût sans coupure.
- **Pourquoi la compter** : c'est la dépense comptée qui consomme le plafond, même si Moonshot facture moins ; le coût réel des coupures reste à lire sur la console Moonshot.
- **Le pire** : il couvre une coupure au pire sur chaque appel (rapport 2,7), sauf pour la passe de Kimi, dont le pire reste celui du v4 (4,75 par passe, plus de 1,25 × 3,7).

### 2.4 Incertitude (SUPPOSÉ)

- **Loi** : chaque composante d'un poste est tirée en log-normale. Les médianes de P11 ne s'appliquent qu'aux bases non observées : 1,2 pour les passes de Kimi et pour l'antériorité. Partout ailleurs, la médiane est 1,0.
- **Écart-type du logarithme**, tiré des intervalles de P11 :

| Poste | Écart-type |
|---|---|
| Opus | 0,22 |
| Argon | 0,30 |
| Kimi juge | 0,52 |
| Aiguilleur | 0,54 |
| Antériorité | 0,63 |
| Fusion | 0,70 |
| Passe de Kimi | 0,72 |
| Autres postes (hors P11) | 0,35 |

- **Tirages** : les coupures de Kimi sont tirées appel par appel. 20 000 tirages ; graines `SeedSequence(20261031, spawn_key=(cle_de_tache(nom),))` (R9).
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

| Étape | Appels | Jetons d'entrée / sortie (SUPPOSÉ sauf mention) | Attendu b5 (bases v3) | **Attendu compté v5** | Plafond de relais b5 | P(dépasse ce plafond) | Plafond au quantile 90 % |
|---|---|---|---|---|---|---|---|
| É0 appels de contrôle (5 modèles) | 5 | ≈ 100 / 80 chacun (observé pour Kimi) | — | 0,0 | 0,5 | 0,00 | 0,5 |
| É1 rédacteur (Sonnet 5.5), dont M6b | 6 | 270 000 / 129 000 | 2,6 | 1,8 | 3,3 | 0,04 | 3,0 |
| É2 Kimi, passe 1 (10 fiches) | ≈ 4 | 300 000 / 140 000 (aucune mesure) | 2,0 | **2,9** | 3,0 | **0,55** | 9,5 |
| É3 rendus : Kimi 9 + 2, Argon 9 + 2, T 10 | 32 | Kimi 8 000 / 4 000 ; Argon 5 000 / 900 (coût observé) ; T 5 000 / 2 500 | 2,0 | 2,1 | 2,8 | 0,17 | 3,5 |
| É4 aiguilleur 56 + 4, second lecteur 10, adjudicateur, nouvel essai | ≈ 72 | 8 500 / 1 150 par lecture, au prix d'Opus | 4,1 | 4,3 | 5,5 | **0,34** | 8,5 |
| É5 relecteur (Fable 5.1), 30 rendus | 30 | 3 000 / 340 | 1,4 | 1,4 | 1,9 | 0,19 | 2,5 |
| É5bis seconde version des témoins (avec 0,43) | ≈ 75 | rédacteur × 0,6, rendus, relecteur, 28 lectures | 4,9 | 5,8 si elle a lieu | 6,6 | 0,39 | 8,5 |
| É6 trois juges sur 28 rendus | 84 | Opus 17 000 / 2 300 et Argon 5 000 / 900 (coûts observés) ; Kimi 8 000 / 4 000 | 7,0 | 7,7 | 11,6 | 0,04 | 10,5 |
| É7 passe « tableau » de Kimi, aiguilleur et second lecteur sur elle — S(4) | ≈ 24 | 300 000 / 140 000 ; 20 × 8 500 / 1 150 | 3,1 | 4,0 | 4,6 | **0,52** | 10,5 |
| É7 lectures d'étiquettes, 10 fiches × 3 grilles × 2 lecteurs | 60 | 4 000 / 450, au prix d'Opus | 0,75 | **1,5** | 1,0 | **0,88** | 2,5 |
| É7 fusions (3, Kimi), aiguilleur, trois juges — S(1) | 15 | fusion ≈ 25 000 / 15 000 (OBSERVÉ, appels longs) | 2,1 | 1,9 | 3,5 | 0,09 | 3,5 |
| É7 Opus, table seule de l'axe 7 — S(3) | ≈ 2 | ≈ 75 000 / 20 000 | 0,7 | 0,7 | 1,0 | 0,05 | 1,0 |
| É8 paraphrases (Sonnet 5.5) | ≈ 2 | ≈ 50 000 / 20 000 | 0,6 | 0,3 | 0,7 | 0,01 | 0,5 |
| É9 antériorité, 8 fiches, 40 recherches — S(2) | 8 | 25 000 / 5 000 + 5 recherches | 2,0 | 2,0 | 6,0 | 0,07 | 5,5 |
| É9b M6b, 4 fiches, lecture des PDF (protégée) | 8 | idem ; lecture d'un PDF 0,10 (b5, SUPPOSÉ) | (1,6) | 1,4 | 2,5 | 0,20 | 3,5 |
| **Total sans seconde version** | | | **28,4** (texte du b5) | **32,1** (texte : 30,1) | 54,5 | | 73,5 |
| **Total, seconde version pondérée** | | | | **34,6** (texte : 32,6) | | | |

**Lecture**
- Les attendus sont proches de ceux du brouillon 5. Trois postes montent : Kimi (coupures comptées), les lectures d'étiquettes, la seconde version. Le rédacteur et le tiers T baissent : Sonnet est à son prix.
- **Constat sur les lectures d'étiquettes** : le brouillon 5 compte 0,75 USD pour « trois par fiche, deux lecteurs ». À 0,025 USD par lecture (sa propre base), cela fait 30 lectures, donc un seul lecteur. Les accords S24 et S28 en demandent deux. Je compte 60 lectures (1,5 USD). **À corriger au brouillon 6.**
- **Complément conditionnel** (CP4-10, GO séparé) : 11,2 USD attendus comptés (le brouillon 5 disait 11,6), médiane 11,8, quantile 90 % 14,6. Son plafond de 17,5 tient avec 0,988.

### 3.3 45 USD suffisent-ils ?

Règle d'A1 jouée étape par étape, dans l'ordre B. La dernière colonne donne la probabilité qu'une étape protégée bute sur son plafond de relais avant la fin ; « sacrifice » compte toute étape sacrifiable retirée ou réduite.

| Configuration | Dépense médiane | Quantile 90 % | Quantile 99 % | Sacrifice | dont fusions | Étape protégée non lancée | **Étape protégée coupée** |
|---|---|---|---|---|---|---|---|
| 45 / 40, plafonds du b5, texte du brouillon | 32,9 | 38,9 | 42,5 | 0,01 | 0,00 | 0,000 | **0,978** |
| 45 / 40, plafonds du b5, configuration recommandée | 35,2 | 40,9 | 43,5 | 0,05 | 0,01 | 0,005 | **0,985** |
| 45 / 40, plafonds au quantile 90 %, fixes | 37,6 | 42,0 | 43,7 | 0,45 | 0,42 | 0,052 | 0,519 |
| 45 / 40, plafonds au quantile 90 %, souples | 37,8 | 42,3 | 44,2 | 0,49 | 0,47 | 0,065 | 0,091 |
| **50 / 45, plafonds au quantile 90 %, souples** | **40,1** | **46,4** | **48,7** | **0,20** | **0,18** | **0,031** | **0,037** |
| idem, postes corrélés (ρ 0,5) | 38,4 | 48,0 | 49,8 | 0,28 | 0,25 | 0,122 | 0,105 |
| 50 / 45, plafonds au quantile 95 %, fixes | 39,1 | 45,1 | 47,8 | 0,32 | 0,30 | 0,024 | 0,277 |
| 55 / 50, plafonds au quantile 95 %, fixes | 40,3 | 48,0 | 52,3 | 0,11 | 0,09 | 0,011 | 0,273 |
| 32 / 28 (GO-2026-10-30-07 tel quel), plafonds du b5 | 28,0 | 30,7 | 31,8 | 1,00 | 1,00 | 0,202 | 0,986 |

**Réponse.**
- **Pour la dépense, oui** : à 45 USD, avec les plafonds du brouillon 5, on n'atteint jamais 45.
- **Pour le plan, non.**
  - **Ce qui casse** : avec les dispersions de P11, les plafonds de relais du brouillon 5 coupent une étape protégée presque à coup sûr. En cause : É2 (0,55), les lectures d'étiquettes (0,88), É4 (0,34), É5 (0,19), É3 (0,17). Au texte du brouillon, une étape coupée est « non mesuré (budget) », donc C13 ne tient pas et c'est un nœud. Le script v5 du brouillon 5 ne simulait pas ces coupures : il donnait une étape protégée non lancée avec 0,032.
  - **Élargir les plafonds de relais déplace le problème** : la règle d'A1 projette avec le plafond de chaque étape, donc des plafonds plus larges font sacrifier plus tôt. À 45 USD, ce sont les fusions qui partent (0,47), et avec elles la chaîne de bisociation du pré-pilote.
- **Le couple qui tient** :
  - plafond **50 USD**, arrêt d'étape **45** ;
  - plafond de relais de chaque étape au **quantile 90 %** de sa dépense ;
  - **souple** pour les étapes protégées : une étape qui atteint son plafond de relais continue sur la marge restante sous le plafond, c'est-à-dire le plafond moins le cumul moins l'attendu des étapes restantes.
- **Ce que ce couple donne** : sacrifice 0,20, étape protégée non lancée 0,031, étape coupée 0,037 ; dépense médiane 40,1 USD.

### 3.4 Ce qui est à porter au brouillon 6 (conv-audit, pas une décision de Lazar)

1. Plafonds de relais : passer de ≈ 1,35 fois l'attendu au quantile 90 % de chaque étape (colonne du § 3.2), et rendre souples ceux des étapes protégées (définition au § 3.3). C'est un changement de la règle d'A1, qui demande une contre-lecture.
2. Lectures d'étiquettes : 60 lectures, pas 30 (§ 3.2).
3. Seconde version des témoins : 5,8 USD attendus si elle a lieu, contre 4,9 au brouillon 5. Elle comprend le relecteur sur 30 rendus et 28 lectures d'aiguillage.
4. Base du tiers T : prix de Sonnet 5.5 (2 / 10), au lieu du prix d'Argon.

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
- **Mode de jugement** : par lots, comme en course 1 (SUPPOSÉ ; la v53 le fixera). La variante « un appel par fiche » est chiffrée au § 4.3.
- **Antériorité** : 10 fiches notables par sous-session, plus la moitié des fusions.
- **Contrôles d'Argon** : un lancement par sous-session (SUPPOSÉ).

### 4.2 Postes, 4 sous-sessions, lecture B

| Poste | Appels | Jetons d'entrée / sortie | Attendu de base | **Attendu compté** | Pire |
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

| Variante | Attendu compté | Pire | Médiane tirée | Quantile 90 % | Corrélé (ρ 0,5) : médiane ; quantile 90 % |
|---|---|---|---|---|---|
| 4 sous-sessions, lecture B | 117,9 | 241,3 | 134,9 | 173,9 | 129,9 ; 203,6 |
| 4 sous-sessions, lecture A | 109,8 | 220,6 | 125,1 | 161,2 | 120,7 ; 188,5 |
| 3 sous-sessions, lecture B | 88,4 | 181,1 | 101,1 | 130,4 | 97,4 ; 152,9 |
| 3 sous-sessions, lecture A | 82,3 | 165,2 | 93,6 | 120,8 | 90,3 ; 141,2 |
| 2 sous-sessions, lecture B | 58,9 | 120,9 | 67,3 | 87,1 | 64,9 ; 102,0 |
| 2 sous-sessions, lecture A | 54,9 | 110,6 | 62,4 | 80,9 | 60,3 ; 94,3 |
| 4, B, juges en appel isolé (une fiche par appel) | 122,2 | 246,9 | — | — | — |
| 4, B, un seul lancement (contrôles d'Argon une fois) | 112,6 | 232,3 | — | — | — |
| 4, B, allégée (4 témoins par lot, antériorité sur 6 notables) | 110,2 | 221,2 | — | — | — |
| 4, B, recherche à 0,05 USD | + 10,4 | — | — | — | — |

**Lecture**
- **Médiane et attendu** : la médiane tirée dépasse l'attendu compté, pour deux raisons. Les médianes de P11 sont prises à 1,2 pour Kimi proposeur et l'antériorité, et la somme de lois log-normales est asymétrique.
- **Ce que coûte une sous-session** : ≈ 29,5 USD attendus. C'est l'unité de réduction de GO-2026-10-30-07.
- **Du v4 au v5 (lecture B, + 33,2 USD)**, par poste, du plus lourd au plus léger :

| Poste | Écart (USD) |
|---|---|
| Lectures d'étiquettes (trois grilles) | + 6,4 |
| Argon proposeur observé | + 6,1 |
| Contrôles d'Argon par lancement | + 5,3 |
| Coupures sur Kimi proposeur | + 4,5 |
| Fusions (24 au lieu de 8, base observée, coupures) | + 3,9 |
| Juges croisés (fusions, coupures) | + 2,4 |
| Antériorité | + 2,0 |
| Opus troisième juge | + 1,9 |
| Aiguilleur | + 0,9 |

- **Leviers sans perte d'objectif** :
  - un seul lancement pour les contrôles d'Argon : − 5,3 USD, si la v53 le permet ;
  - lecture A : − 8,1 USD, mais deux fois moins de fusions pour comparer les bras ;
  - allégement : − 7,7 USD, mais moins d'antériorité vérifiée.

## 5. Totaux et plafond total

| | Attendu | Médiane tirée | Pire |
|---|---|---|---|
| Pré-pilote (configuration recommandée, seconde version pondérée) | 34,6 | 40,1 (50 / 45, plafonds souples) | 50 (plafond, règle d'A1) |
| Course, 4 sous-sessions, lecture B | 117,9 | 134,9 | 241,3 |
| **Total** | **≈ 152,5** | — | **≈ 291** |
| Hors total : complément conditionnel du pré-pilote | 11,2 | 11,8 | 17,5 (plafond b5) |
| Hors total : machine jetable (devis machine v2) | 0,5 | — | 7,4 (GO proposé 10) |
| Hors total : appels de modèle des tests de mort (v52 : 0,6 USD par fiche) | 3,0 (5 fiches) | — | 7,2 (12 fiches) |

**Ce que la course peut faire selon le plafond total.** La dépense du pré-pilote est tirée par la règle d'A1 à 50 / 45, avec des plafonds souples ; la course est tirée au même modèle ; reste = total − dépense du pré-pilote.

| Plafond total | Reste médian | Lecture B : à 4 ; à 3 ; à 2 ; aucune | Lecture A : à 4 ; à 3 ; à 2 ; aucune | B, corrélé ρ 0,5 : à 4 ; à 3 ; à 2 ; aucune |
|---|---|---|---|---|
| 110 (GO-2026-10-30-07) | 69,9 | 0,00 ; 0,02 ; 0,56 ; **0,42** | 0,00 ; 0,05 ; 0,66 ; 0,29 | 0,04 ; 0,15 ; 0,42 ; 0,38 |
| 140 | 99,9 | 0,04 ; 0,44 ; 0,49 ; 0,03 | 0,10 ; 0,54 ; 0,34 ; 0,02 | 0,24 ; 0,32 ; 0,34 ; 0,11 |
| **160** | **119,9** | **0,26 ; 0,56 ; 0,18 ; 0,01** | 0,41 ; 0,48 ; 0,10 ; 0,00 | 0,43 ; 0,31 ; 0,21 ; 0,04 |
| 180 | 139,9 | 0,58 ; 0,36 ; 0,05 ; 0,00 | 0,73 ; 0,24 ; 0,03 ; 0,00 | 0,61 ; 0,25 ; 0,12 ; 0,02 |

Le séquençage de GO-2026-10-30-07 tient dans tous les cas :
- les relais sont plafonnés à chaque lancement ;
- la course n'est lancée que si son devis, refait sur les mesures du pré-pilote, tient dans le reste ;
- sinon, elle est réduite. L'ordre de retrait des sous-sessions est à dire d'avance (par exemple, l'axe 6 avec pistes en premier).

Le pré-pilote mesure trois facteurs du pire : Kimi proposeur sur une passe, Kimi juge et l'antériorité, plus l'aiguillage et le taux de coupure de Kimi.

## 6. Machine jetable (à part)

- **Renvoi** : devis machine v2 (`docs/notes/ideation-organisme-v1/machine-jetable-v1/devis-et-plomberie-machine-jetable-v2.md`, `39260994…`), qui remplace la v1.
- **Machine** : Hetzner CPX32, 0,0577 EUR de l'heure hors taxes.
- **Coût** : ≈ 0,5 USD attendus et ≈ 7,4 au pire pour les séries S0, S1 et P de la génération 1. GO proposé : 10 USD, échéance le 15 novembre.
- **Appels de modèle des tests de mort** : hors devis machine, sur une ligne de GO à part. Au défaut de la v52, 0,5 USD pour le test et 0,1 pour le lecteur, ces deux valeurs étant SUPPOSÉES : 3,0 USD pour 5 fiches, 7,2 pour 12. Ils viennent **après** la course.
- **Ce que la v2 demande à Lazar** : ce GO ; le poste de passage (son ordinateur) ; le choix du projet Hetzner ; l'accord sur l'écart d'hôte AppArmor (R-a). Rien de cela n'est repris ici.

## 7. Ce que je ne sais pas (SUPPOSÉ)

- **Kimi proposeur** : aucune mesure. Les profils de 250 000 / 75 000 jetons par passe de course et de 300 000 / 140 000 par passe du pré-pilote sont ceux du v4. Les appels longs observés (12 000 à 21 000 jetons de sortie chacun) les rendent plausibles, pas mesurés.
- **Coupures de Kimi** : le taux de 0,2 repose sur ≈ 13 appels longs. Le coût réel d'une coupure est inconnu : console Moonshot. Les tours du tableau partagé et de la bisociation ne sont pas dépouillés ici.
- **Contrôles d'Argon** : 1,75 USD a été observé une fois, et j'ignore leur nature. J'ai supposé un lancement par sous-session ; avec un seul lancement, la course coûte − 5,3 USD.
- **Argon** : prix de sortie (41,5) non lu. Le découpage en jetons des passes et des jugements est conjectural ; seul le coût est observé.
- **Jugement isolé** : 0,057 par fiche pour Kimi, au lieu des 0,026 du lot. Aucune mesure d'un appel isolé n'existe pour aucun juge. Si Opus et Argon coûtent plus en appel isolé qu'en lot, É6 monte : son plafond de relais de 11,6 laisse ≈ 50 % de marge.
- **Prix de la recherche** : 0,01 est le prix de liste des agents gérés. Celui de l'API Messages n'est pas lu.
- **v53 non écrite** : elle fixera la lecture A ou B, qui fusionne, le découpage des juges (lots ou appels isolés), le nombre de lancements, le maintien d'Argon proposeur, le contenu du tableau minimal et la voie d'Opus troisième juge.
- **Brouillon 6** : la contre-lecture 4 (R-663) en demande un ; il est en cours. Il peut changer les effectifs, l'ordre des étapes (CP5-04) et la règle d'A1 (CP5-02, CP5-06).
- **Bras méta** : son annexe n'est pas écrite. Une grille plus riche ou la carte des chapelles peut doubler ses lectures (≈ + 3 USD sur la course).
- **Bras Gu-Krenn simplifié** : les cooccurrences passent par OpenAlex sur l'allocation gratuite (0 USD). Un modèle n'est pas compté.
- **Témoins de la course** : je les suppose réutilisés du pré-pilote, sans rendu nouveau. Les écrire à nouveau coûterait ≈ 0,2 USD par témoin.
- **Écriture des 12 concrets de l'aiguilleur** : comptée à 0 USD, sous-agent et abonnement de la session (R-819 non tranchée).

## 8. Réserves

- **Confidentialité** : Kimi juge les fiches d'Argon, et les sorties de l'axe 6 partent chez Moonshot. Les fiches aiguillées ne partent chez aucun juge. À confirmer par Lazar avant le pré-pilote.
- **Écart avec le brouillon 5** : il donne C10 (la course tient dans le reste) à 0,92, sur un devis médian de 103 USD pour k = 1. Sur mes bases, la course médiane à 4 sous-sessions en lecture A coûte 125. C10 vaut donc moins au plafond de 110, et le brouillon 6 doit reprendre ce devis.
- **Écart de lecture des fusions** : 24 pour conv-audit (n° 268, R-642), 12 pour le brouillon 5. C'est la décision 3.
- **Aucune bascule de modèle** sans le mot de Lazar.
- **GO-2026-10-30-07 expire le 6 novembre.** La ligne de GO nouvelle est à écrire par la session principale, sur le mot direct de Lazar.
- **R4, symétrie** : la coupure par les relais à 0,98 est un résultat « trop sale » du modèle ; je l'ai donc éprouvé (fin de la sortie). Au compte de lectures d'étiquettes du brouillon 5 (30), elle vaut encore 0,904 ; avec, en plus, des dispersions divisées par deux, 0,733. Elle tient surtout à É2 (attendu compté 2,9 pour un plafond de 3,0, à cause des coupures de Kimi) et aux plafonds fixés à ≈ 1,35 fois l'attendu. Elle reste à revoir quand le pré-pilote aura mesuré ses rapports réels.

## 9. Décisions pour Lazar (nœuds de dépense ; aucune n'a de défaut)

### Décision 1 — plafond du pré-pilote (S17)

**Décision** : quel plafond et quel arrêt d'étape pour le pré-pilote recentré ?

**Enjeu** : à 45 USD, la dépense tient, mais le plan ne passe pas. Avec les plafonds de relais du brouillon 5, une étape protégée bute presque toujours sur le sien. Si on les élargit, la règle de sacrifice retire les fusions une fois sur deux.

**Options**
- **(a) 45 / 40, plafonds de relais du brouillon 5.**
  - Avantage : la recommandation actuelle (R-630, brouillon 5) ; ne dépasse jamais 45.
  - Inconvénient : une étape protégée est coupée avec 0,98 (C13 fermée, nœud).
- **(b) 50 / 45, plafonds de relais au quantile 90 %, souples pour les étapes protégées** (règle à écrire au brouillon 6).
  - Avantage : sacrifice 0,20 ; étape protégée non lancée 0,031 ; coupée 0,037 ; médiane 40,1 USD.
  - Inconvénient : 5 USD de plus engagés sur le plafond total ; demande une règle nouvelle, à contre-lire.
- **(c) 45 / 40, plafonds au quantile 90 %, souples.**
  - Avantage : garde 45.
  - Inconvénient : fusions sacrifiées avec 0,47 (la chaîne de bisociation sort du pré-pilote une fois sur deux) ; étape protégée non lancée 0,065.

**Recommandation** : **(b)**, confiance 0,6.

**Défaut** : aucun. Sans mot de Lazar, GO-2026-10-30-07 reste tel quel (pré-pilote ≤ 32), et rien n'est lancé à 32 : le brouillon 5 prévoit l'arrêt par A15.

### Décision 2 — plafond total de la course 2 (génération 1)

**Décision** : quel plafond total séquencé pour le pré-pilote et la course ?

**Enjeu** : sur les coûts observés, la course à 4 sous-sessions coûte ≈ 118 USD attendus (médiane ≈ 135, pire ≈ 241). Le total actuel de 110 ne la laisse jamais à 4 sous-sessions, et à aucune avec 0,42.

**Options**
- **(a) 160 USD.**
  - Avantage : 3 sous-sessions au moins avec 0,82, et 4 avec 0,26 (0,41 en lecture A).
  - Inconvénient : 50 USD de plus que GO-2026-10-30-07 ; le pire (≈ 291) reste hors plafond, tenu par le seul séquençage.
- **(b) 180 USD.**
  - Avantage : 4 sous-sessions avec 0,58 (0,73 en lecture A).
  - Inconvénient : 70 USD de plus ; peu de gain si 3 sous-sessions suffisent à l'objectif.
- **(c) 140 USD.**
  - Avantage : 30 USD de plus seulement.
  - Inconvénient : course à 2 sous-sessions avec 0,49, à 4 avec 0,04.
- **(d) 110 USD, gardé.**
  - Avantage : rien ne bouge.
  - Inconvénient : course à 2 sous-sessions au mieux (0,56) ; aucune avec 0,42.

**Recommandation** : **(a) 160**, séquencé, avec l'ordre de retrait des sous-sessions dit d'avance. Le levier « un seul lancement des contrôles d'Argon » (− 5,3 USD) est à demander à la v53. Confiance 0,5 : le choix entre (a) et (b) dépend de ce que vaut pour Lazar la quatrième sous-session.

**Défaut** : aucun.

### Décision 3 — nombre de fusions de la course (lecture de « une paire par session »)

**Décision** : 24 fusions (une paire par bras et par proposeur dans chaque sous-session) ou 12 (une paire par bras et par sous-session) ?

**Enjeu** : ≈ 8 USD attendus (117,9 contre 109,8), et l'effectif de la comparaison entre bras, qui est la raison de garder le bras basique (R-642).

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
