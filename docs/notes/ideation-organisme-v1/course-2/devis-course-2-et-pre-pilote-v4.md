# Devis de la course 2 (génération 1) et du pré-pilote recentré — bisociateur à deux bras, Kimi proposeur, notation croisée, Opus troisième juge — v4

Lignée session-depot (sous-agent), 30 octobre 2026, écrit vers 22:56 UTC (`date -u`). **Rien n'est lancé, aucun appel payant n'a servi à ce devis.** C'est un nœud de dépense ; chaque lancement aura sa ligne de GO, écrite par la session principale sur le mot direct de Lazar.

Il remplace le devis v3 (`devis-course-2-trois-juges-v3.md`, `74a3f731…`), archivé sans modification (R12). Il suit les décisions de Lazar relayées par conv-audit (`registres/decisions.md` de `origin/canal/conv-audit-n04`, `9fb3a398`, l. 848 à 854, fichier `f8c4a220…`) :
- **R-634** (n° 266, `b78f9b1e…`) : objectif « idées inédites et très plausibles », pas la mesure de l'organisme ; pré-pilote recentré sur la plausibilité ; retirés : bras hasard, mesure de l'auto-préférence (dix fonds écrits deux fois), dose-réponse ; notation croisée gardée ;
- **R-635 à R-639** (n° 267, `0c77987a…`) : bisociateur à **deux bras**, une paire par session chacun : **bras méta** (version 1, « trou à structure commune », paramètres à la main, SUPPOSÉ, gelés) et **bras Gu-Krenn** (simplifié par leurs traits publiés si leur modèle ne tourne pas à temps) ; le bras « loin en domaine, proche en concept » sort de la course ;
- **R-637 option A et R-640** : course 2 = génération 1, maintenant ; machine jetable pour l'étage de tests de mort (devis à part) ;
- **n° 264** (`675b0710…`) : Lazar dit « on augmente le plafond » du pré-pilote ; conv-audit recommande **45 USD**, en remplacement de la part « pré-pilote ≤ 32 » de GO-2026-10-30-07.

Tous les chiffres de ce devis sortent du script `calcul-devis-course-2-et-pre-pilote-v4.py` et de sa sortie `calcul-devis-course-2-et-pre-pilote-v4.sortie.txt` (même dossier, empreintes dans leurs `.sha256`). Les montants du texte sont arrondis au dixième.

## 0. Verdict

- **Pré-pilote recentré : ≈ 23 USD attendus, ≈ 43 au pire sans seconde version des témoins, ≈ 52 avec.** 45 USD suffisent : au modèle d'incertitude (SUPPOSÉ), le dépasser a une probabilité nulle (0 sur 20 000 tirages) ; 35 USD auraient suffi avec 0,97.
- **Course 2 à 4 sous-sessions : ≈ 85 USD attendus, ≈ 180 au pire** (médiane prudente ≈ 97). Avec le plafond total de 110 de GO-2026-10-30-07, la course ne tient à 4 sous-sessions qu'avec 0,19 ; à 3, avec 0,62.
- **Le nœud n'est pas le pré-pilote : c'est le plafond total.** Recommandation : plafond total 140 USD, séquencé (§ 7).

## 1. Ce qui change depuis le v3

| Poste | v3 | v4 | Raison |
|---|---|---|---|
| Coût d'un jugement de Kimi | 0,057 USD par fiche (SUPPOSÉ) | **0,026 (OBSERVÉ)** ; pire 0,153 inchangé | Kimi a jugé les 29 fiches de la course 1 : 222 635 jetons d'entrée, 31 010 de sortie, 0,755 USD (`registres/depenses.md`, l. 255) |
| Témoins du pré-pilote | 24, notés pour l'auto-préférence (sources appariées) | 24 rendus une fois, pour l'étalonnage seul | R-634 : auto-préférence retirée |
| Bisociation | 3 bras au pré-pilote (brouillon 3) ; absente du v3 | 2 bras, une paire chacun, au pré-pilote et à la course | R-638, R-639 |
| Aiguillage | 128 fiches de course | + fusions ; au pré-pilote : aiguilleur, second lecteur, adjudicateur | brouillon 3 du pré-pilote |
| Plafond du pré-pilote | 32 USD | 45 USD demandés (n° 264) | — |

## 2. Bases

### 2.1 Prix (USD par million de jetons)

| Modèle | Entrée | Sortie | Provenance |
|---|---|---|---|
| Opus 5.5 | 4 | 20 | SOURCÉ : table `MODELES` de `collisionneur_v2.py` (`0e63febd…`) ; devis v1 § 1 |
| Kimi K3.1 Pro | 2 | 10 | SOURCÉ : page de prix lue le 30 octobre (devis v1 § 1, page `c62210a0…`) ; **OBSERVÉ conforme** : 222 635 × 2 + 31 010 × 10 = 0,755 USD, la somme facturée (l. 255) |
| Argon | 8,3 | 41,5 | entrée : borne lue par Lazar (R-718) ; **sortie : SUPPOSÉ** (rapport 5, `commande_argon_v3d.py`, `46c91df4…`) |
| Fable 5.1 (relecteur) | 10 | 50 | SOURCÉ : `collisionneur_v2.py` |
| Sonnet 5.5 (rédacteur, tiers metteur en forme) | 4 | 20 | **SUPPOSÉ** : prix absent du dépôt ; compté au prix d'Opus par prudence |
| Recherche sur le Web (antériorité) | 0,01 USD par recherche | — | **SUPPOSÉ** : prix non lu |

### 2.2 Coûts observés (`registres/depenses.md`)

- Course 1, tentative 2 : Argon proposeur **6,00 USD** pour 16 fiches (2 passes de 8), plus **1,75** de contrôles (l. 250). Le proposeur Fable coûtait 23,65 ; il ne sert plus.
- Juges sur 29 fiches : Opus 5.5 **3,31 USD** en 6 appels, soit 0,114 par fiche ; Argon **2,28**, soit 0,079 (l. 252).
- Kimi juge des mêmes 29 fiches : premier essai coupé à 300 s, **2,03 USD comptés au pire** par le relais (dépense réelle inconnue, à lire sur la console Moonshot) ; second essai, relais v3 en flux : **0,755 USD**, soit 0,026 par fiche (l. 254-255). Avec la coupure comptée au pire, le coût effectif est de 2,79 USD, soit 0,096 par fiche, sous le pire unitaire retenu (0,153).
- Rapport octets ÷ jetons observé : 851 581 octets pour 222 635 jetons, soit **3,8 octets par jeton** (l. 254-255). Il sert à convertir les tailles de texte en jetons.

### 2.3 Profils d'un acte (méthode)

Pour chaque acte, un profil de jetons (entrée, sortie) multiplié par le prix du modèle donne le coût attendu. Le profil est **observé** quand le registre donne les jetons (Kimi juge). Sinon, il est **choisi pour retrouver le coût observé** au prix sourcé : seul le coût est alors une mesure, le découpage reste SUPPOSÉ. À défaut de toute mesure, il reprend les bases SUPPOSÉES du v3 et du brouillon 3 du pré-pilote (`preenregistrement-pre-pilote-course-2-brouillon3.md`, `dcf937e7…`, branche de conv-audit).

| Acte | Modèle | Entrée | Sortie | Attendu (USD) | Pire (USD) | Provenance |
|---|---|---|---|---|---|---|
| Jugement d'une fiche | Kimi | 7 677 | 1 069 | 0,026 | 0,153 | OBSERVÉ (lot de 29 fiches par appel) ; pire du v3 |
| Jugement d'une fiche | Opus 5.5 | 17 000 | 2 300 | 0,114 | 0,153 | coût OBSERVÉ, découpage SUPPOSÉ ; pire = × 1,34 (v3) |
| Jugement d'une fiche | Argon | 5 000 | 900 | 0,079 | 0,105 | coût OBSERVÉ, découpage SUPPOSÉ ; pire × 1,34 |
| Lecture d'aiguillage | Claude, au prix d'Opus | 8 500 | 1 150 | 0,057 | 0,153 | SUPPOSÉ (v3 : moitié d'un jugement ; pire : un jugement entier) |
| Antériorité d'une fiche | Opus 5.5 avec recherche | 25 000 | 5 000 | 0,25 (5 recherches comprises) | 0,75 | SUPPOSÉ (v3) |
| Lecture d'étiquettes (concepts, niches) | au prix d'Opus | 4 000 | 450 | 0,025 | × 1,5 | SUPPOSÉ (brouillon 3) |
| Fusion d'une paire | Kimi | 50 000 | 30 000 | 0,40 | × 1,5 | SUPPOSÉ (brouillon 3) |
| Relecture d'un témoin | Fable 5.1 | 3 000 | 340 | 0,047 | × 1,36 | SUPPOSÉ (brouillon 3) |
| Passe de 8 fiches, course | Kimi | 250 000 | 75 000 | 1,25 | 4,75 | SUPPOSÉ : retrouve 2,5 / 9,5 USD par sous-session (v1, v3) ; **aucune mesure de Kimi proposeur** |
| Passe de 8 fiches, course | Argon | 150 000 | 24 000 | 2,24 | 3,0 | coût OBSERVÉ en course 1 (6,00 pour 2 passes, gros corpus) ; v3 : 4,5 / 6 par sous-session |

## 3. Pré-pilote recentré

### 3.1 Périmètre retenu pour le chiffrage

Le brouillon 4 du préenregistrement n'est pas écrit. Le chiffrage suit R-634 à la lettre ; les effectifs sont **SUPPOSÉ** et suivront le brouillon 4.
- **Étalonnage des trois juges sur témoins** : 24 témoins (P 8, N 11, C 3, G 2, pour tenir les effectifs minimaux P ≥ 8 et N ≥ 10 de S20), un seul rendu par fond (Kimi 8, Argon 8, tiers 8), un relecteur. Les trois juges notent tous les témoins et les 2 fusions.
- **Antériorité** : 8 fiches à antériorité plantée (Opus avec recherche).
- **Aiguillage** : aiguilleur sur 54 lectures (24 témoins, 10 fiches de Kimi, 6 difficiles, 12 concrets, 2 fusions) ; second lecteur sur les 10 fiches de Kimi ; adjudicateur sur les seules fiches en désaccord.
- **Garde de niveau méthode chez Kimi** : une passe de 10 fiches.
- **Chaîne de bisociation sur une paire par bras** : deux lecteurs d'étiquettes sur les 10 fiches de Kimi, une paire du bras méta et une du bras Gu-Krenn, 2 fusions par Kimi ; notes de paire sur processeur.
- **Hors chiffrage** (à trancher au brouillon 4) : passe « tableau » de Kimi (+ 2,0 attendus, + 4,0 au pire) ; mémoire anti-redite et table de l'axe 7 (+ 1,7, + 2,4). L'écriture des 12 concrets (bras d'attaque, sous-agent de la session, abonnement) est comptée à 0 USD (SUPPOSÉ, comme GO-2026-10-30-10).

### 3.2 Postes

| Poste | Appels | Jetons d'entrée | Jetons de sortie | Attendu (USD) | Pire (USD) |
|---|---|---|---|---|---|
| Rédacteur (Sonnet 5.5, au prix d'Opus) : 24 squelettes et déclarations, 8 fiches d'antériorité, 6 difficiles | 5 | 225 000 | 83 000 | 2,6 | 3,8 |
| Rendus des 24 témoins (Kimi 8 × 0,057 ; Argon 8 × 0,079 ; tiers 8 × 0,079) | 24 | — | — | 1,7 | 2,4 |
| Relecteur (Fable 5.1), 24 rendus | 24 | 72 000 | 8 200 | 1,1 | 1,5 |
| Kimi proposeur, passe de 10 fiches (garde de niveau méthode) | ≈ 4 | 300 000 | 140 000 | 2,0 | 4,0 |
| Aiguillage : aiguilleur 54, second lecteur 10, adjudicateur ≤ 10, nouvel essai | 64 | 544 000 | 73 600 | 4,1 | 11,6 |
| Juge Opus 5.5, 26 fiches | 1 à 6 | 442 000 | 59 800 | 3,0 | 4,0 |
| Juge Argon, 26 fiches | 1 à 6 | 130 000 | 23 400 | 2,1 | 2,7 |
| Juge Kimi, 26 fiches | 1 à 6 | 199 600 | 27 800 | 0,7 | 4,0 |
| Antériorité, 8 fiches | 8 | 200 000 | 40 000 | 2,0 | 6,0 |
| Bisociation : 20 lectures d'étiquettes, 2 fusions | 22 | 180 000 | 69 000 | 1,3 | 2,0 |
| Appels de contrôle (un par modèle, cinq modèles) | 5 | — | — | ≈ 0 | 0,5 |
| **Total, sans seconde version** | | | | **≈ 20,5** | **≈ 42,5** |
| Seconde version des témoins si les contrôles de forme échouent (probabilité 0,44, brouillon 3 : une version réussit avec 0,56) | | | | 5,8 si elle a lieu ; **2,5 pondérée** | 9,9 |
| **Total** | | | | **≈ 23,0** | **≈ 52,5** |

### 3.3 45 USD suffisent-ils ?

- **Oui.** Au modèle d'incertitude (§ 3.4), la dépense médiane est de **25,5 USD**, le quantile 90 % de **32,1**, le quantile 99 % de **37,7**. P(dépense > 45) = 0,000 ; P(> 40) = 0,004 ; P(> 35) = 0,033 ; P(> 32, l'ancien plafond) = 0,104.
- Le pire déterministe, 52,5 USD, empile tous les facteurs pessimistes et la seconde version. Il dépasse 45 ; la règle de sacrifice du brouillon 3 (fusions d'abord, l'aiguilleur et les juges jamais) le borne.
- L'écart avec la médiane de 35,5 du brouillon 3 (n° 264) vient du recentrage : il n'y a plus de rendus doubles, de passe « tableau », de troisième bras ni de mémoire. Il vient aussi du coût observé de Kimi juge, deux fois plus bas que sa base.
- 45 USD laissent donc ≈ 20 USD de marge. Ils ne coûtent rien s'ils ne sont pas dépensés, mais ils réservent cette part du plafond total (§ 5).

### 3.4 Modèle d'incertitude (SUPPOSÉ)

Pour chaque poste, le rapport mesuré ÷ attendu est tiré dans une loi log-normale, indépendante d'un poste à l'autre. Médianes reprises de P11 du brouillon 3 : 1,2 pour les passes de Kimi, 1,2 pour l'antériorité, 1,3 pour les fusions ; 1,0 pour Kimi juge, dont la base est désormais observée, et pour les autres postes. Écart-type du logarithme : 0,35 ; 0,5 pour Kimi ; 0,45 pour les juges croisés. 20 000 tirages ; graines `SeedSequence(20261030, spawn_key=(cle_de_tache(nom),))` (R9). Le modèle est grossier : il ignore les corrélations entre postes (un même relais lent touche tout) et ne simule pas la règle de sacrifice étape par étape.

## 4. Course 2 = génération 1

### 4.1 Structure chiffrée

- **4 sous-sessions** (texte I axes 1 à 5 et boucle ; texte I axe 7 ; axe 6 sans pistes ; axe 6 avec pistes), comme au v3. Chaque proposeur, **Kimi** et **Argon**, y fait 2 passes de 8 fiches : 128 fiches. **SUPPOSÉ** : Argon reste proposeur (R-813) ; les messages n° 266 et 267 ne nomment que Kimi.
- **Tableau minimal** : construit par programme, 0 USD ; son coût en jetons est compris dans les profils de passe.
- **Aiguilleur** : toutes les fiches et toutes les fusions, avant tout juge.
- **Notation croisée** : fiches de Kimi et fusions (faites par Kimi) notées par Argon, fiches d'Argon notées par Kimi ; 8 témoins par lot, notés par Kimi et par Argon.
- **Opus 5.5 troisième juge** : toutes les fiches, fusions et témoins.
- **Antériorité** : les 10 fiches notables de chaque sous-session et la moitié des fusions.
- **Bisociateur** : deux lecteurs d'étiquettes sur les 16 fiches de passe 1 de chaque sous-session ; une paire par bras (méta, Gu-Krenn), fusionnée par Kimi. « Une paire par session » se lit de deux façons, que la v53 tranchera :
  - **lecture A** (chiffrée par défaut) : une session = une sous-session, paires tirées parmi les fiches des deux proposeurs, soit 2 fusions par sous-session et 8 sur la course ;
  - **lecture B** : une session = une sous-session d'un proposeur, soit 4 fusions par sous-session et 16 sur la course.

### 4.2 Postes, 4 sous-sessions, lecture A

| Poste | Appels | Jetons d'entrée | Jetons de sortie | Attendu (USD) | Pire (USD) |
|---|---|---|---|---|---|
| Kimi proposeur (4 × 2 passes de 8) | ≈ 24 | 2 000 000 | 600 000 | 10,0 | 38,0 |
| Argon proposeur (4 × 2 passes de 8) | ≈ 24 | 1 200 000 | 192 000 | 17,9 | 24,0 |
| Contrôles d'Argon (course 1 : 1,75 OBSERVÉ) | — | — | — | 1,8 | 3,0 |
| Aiguilleur (128 fiches et 8 fusions) | 136 | 1 156 000 | 156 400 | 7,8 | 20,8 |
| Juges croisés : Argon sur 104 (64 fiches de Kimi, 8 fusions, 32 témoins) ; Kimi sur 96 (64 fiches d'Argon, 32 témoins) | ≈ 2 par lot | 1 257 000 | 196 300 | 10,7 | 25,6 |
| Opus 5.5 troisième juge (168 : fiches, fusions, témoins) | ≈ 24 | 2 856 000 | 386 400 | 19,2 | 25,7 |
| Antériorité (44 : 40 fiches notables, 4 fusions) | 44 | 1 100 000 | 220 000 | 11,0 | 33,0 |
| Bisociation : 128 lectures d'étiquettes, 8 fusions | 136 | 912 000 | 297 600 | 6,4 | 9,6 |
| Appels de contrôle | — | — | — | ≈ 0 | 0,5 |
| **Course, 4 sous-sessions (lecture A)** | | | | **≈ 84,7** | **≈ 180,2** |

### 4.3 Variantes

| Variante | Attendu (USD) | Pire (USD) | Médiane prudente (§ 3.4) | Quantile 90 % |
|---|---|---|---|---|
| 4 sous-sessions, lecture A | 84,7 | 180,2 | 96,5 | 117,9 |
| 4 sous-sessions, lecture B (16 fusions) | 90,9 | 191,3 | — | — |
| 3 sous-sessions, lecture A | 63,5 | 135,3 | 72,4 | 88,4 |
| 2 sous-sessions, lecture A | 42,4 | 90,4 | 48,3 | 58,9 |
| 4 sous-sessions allégées : 4 témoins par lot, antériorité sur 6 notables (option c, § 7) | 77,2 | 161,6 | 87,7 | 107,4 |

**Lecture**
- Le pire empile, comme au v3, quatre hypothèses pessimistes : Kimi proposeur à × 3,8 ; Kimi juge à × 5,9 de sa base observée ; antériorité à × 3 ; aiguillage au prix d'un jugement entier. Le pré-pilote en mesure trois : Kimi proposeur sur une passe, Kimi juge, antériorité. L'aiguillage est mesuré aussi.
- Une sous-session coûte ≈ 21 USD attendus. C'est l'unité de réduction prévue par GO-2026-10-30-07.
- Par rapport au v3 (79 attendus, 164 au pire) : le bisociateur ajoute ≈ 9,4 attendus (6,4 de lectures d'étiquettes et de fusions ; ≈ 3 d'aiguillage, de jugements et d'antériorité sur les fusions) ; Kimi juge observé en retire ≈ 3.

## 5. Totaux et plafond total

| | Attendu (USD) | Pire (USD) |
|---|---|---|
| Pré-pilote recentré (seconde version pondérée ; pire avec elle) | 23,0 | 52,5 (borné à 45 par la règle de sacrifice) |
| Course, 4 sous-sessions, lecture A | 84,7 | 180,2 |
| **Total** | **≈ 108** | **≈ 225** (≈ 233 sans la règle de sacrifice) |

**Ce que la course peut faire selon le plafond total** (dépense du pré-pilote tirée au modèle, puis course tirée au même modèle ; § 3.4) :

| Plafond total | Reste médian pour la course | Course à 4 | À 3 | À 2 | Aucune |
|---|---|---|---|---|---|
| 110 USD (GO-2026-10-30-07) | 84,5 | 0,19 | 0,62 | 0,19 | 0,001 |
| 130 USD | 104,5 | 0,68 | 0,31 | 0,01 | 0 |
| 140 USD | 114,5 | 0,85 | 0,15 | 0 | 0 |
| 110 USD, course allégée (option c) | 84,5 | 0,40 | 0,53 | — | — |

Le séquençage de GO-2026-10-30-07 tient dans tous les cas : relais plafonnés à chaque lancement ; course lancée seulement si son devis, refait sur les mesures du pré-pilote, tient dans le reste.

## 6. Ce que je ne sais pas

- **v53 non écrite** (conv-audit). Il en dépend :
  - la lecture A ou B de « une paire par session » (± 6 USD) ;
  - qui fusionne (Kimi ici, SUPPOSÉ) ;
  - le découpage des juges en appels (un lot de 29 fiches chez Kimi en un appel ; 6 appels chez Opus en course 1) : le coût par fiche en dépend fortement, car l'entrée de la consigne se répète à chaque appel ;
  - la voie d'Opus troisième juge (kit d'agent ou protocole) ;
  - le contenu servi au tableau minimal ;
  - le nombre de sous-sessions et le maintien d'Argon proposeur.
- **Brouillon 4 du pré-pilote non écrit** : effectifs des témoins (24 ici), maintien de la mémoire anti-redite, de la table de l'axe 7 et de la passe « tableau », seuils (dont S17, arrêt d'étape). La contre-lecture 3 est en cours.
- **Bras méta** : spécification attendue après les verdicts des collisionneurs (R-638). S'il faut un lecteur de niches de plus, ou la carte des chapelles, le poste « étiquettes » peut doubler (≈ + 3 USD sur la course).
- **Bras Gu-Krenn simplifié** : « paires de concepts jamais reliés » suppose une recherche de cooccurrence dans la littérature (OpenAlex, sans dépense de modèle : compté 0). Si elle passe par un modèle, elle n'est pas comptée.
- **Kimi proposeur** : aucune mesure. La base de 2,5 USD par sous-session date du v1 ; le profil de 250 000 jetons d'entrée et 75 000 de sortie par passe n'est qu'une conjecture compatible.
- **Prix non lus** : sortie d'Argon (41,5, SUPPOSÉ, haut par prudence) ; Sonnet 5.5 ; recherche sur le Web pour l'antériorité.
- **Coût réel du premier essai coupé de Kimi** : il est à lire sur la console Moonshot ; le registre le compte au pire (2,03 USD).
- **Tests de mort** : non chiffrés ici. L'étage tourne sur la machine jetable (R-640) : la location et la plomberie ont leur propre devis. Ses appels de modèle dépendent de la spécification de l'étage. R-636 recommande de l'activer entre générations, sur les fiches les mieux classées. Pour la génération 1, il viendrait **après** la course : poste à ajouter au devis refait.
- **Écriture des 12 concrets de l'aiguilleur** : comptée à 0 USD ; elle dépend de la revue de sécurité du bras d'attaque et du mot de Lazar sur R-819 (sans étalonnage, la porte C7 se ferme à coup sûr).

## 7. Réserves

- **Confidentialité** (déjà aux v2 et v3) : Kimi juge les fiches d'Argon, et les sorties de l'axe 6 partent chez Moonshot. Les fiches marquées par l'aiguillage ne partent chez aucun juge. À confirmer par Lazar avant le pré-pilote.
- **Notation croisée** : la source et le juge restent confondus sur les fiches. La mesure de l'auto-préférence étant retirée, seule la note d'Opus, portée sur toutes les fiches, donne une échelle commune aux deux sources. Les 8 témoins par lot gardent la correction de sévérité ; les réduire à 4 (option c) la rend plus imprécise.
- **Aucune bascule de modèle** sans mot de Lazar (GO-2026-10-30-07).
- **La ligne de GO** remplaçant la part « pré-pilote ≤ 32 » de GO-2026-10-30-07 est à écrire par la session principale, sur le mot direct de Lazar (n° 264). Ce devis n'écrit rien dans `registres/`.
- GO-2026-10-30-07 expire le **6 novembre**.

## 8. Décision pour Lazar (nœud de dépense)

**Décision** : quels plafonds pour le pré-pilote recentré et pour la course 2 (génération 1, bisociateur à deux bras) ?

**Enjeu** : le pré-pilote recentré coûte ≈ 23 USD attendus et tient largement dans 45. La course à 4 sous-sessions coûte ≈ 85 attendus (≈ 97 en médiane prudente, ≈ 180 au pire). Le plafond total actuel, 110, ne la laisse à 4 sous-sessions qu'une fois sur cinq.

**Options**
- **(a) Pré-pilote ≤ 45 ; plafond total relevé à 140 USD, séquencé.**
  - Avantage : course à 4 sous-sessions avec 0,85, et le pré-pilote n'a presque aucune chance d'être sacrifié.
  - Inconvénient : engage 30 USD de plus que GO-2026-10-30-07 ; le pire cas (≈ 225) reste hors plafond, tenu par le seul séquençage.
- **(b) Pré-pilote ≤ 45 ; plafond total gardé à 110 USD.**
  - Avantage : rien ne bouge au total ; c'est la lecture littérale du n° 264.
  - Inconvénient : course probablement réduite à 3 sous-sessions (0,62), à 2 avec 0,19. Il faudrait dire d'avance laquelle sort (l'axe 6 avec pistes, par exemple).
- **(c) Pré-pilote ≤ 45 ; total 110 ; course allégée d'avance** (4 témoins par lot au lieu de 8, antériorité sur 6 fiches notables au lieu de 10).
  - Avantage : 4 sous-sessions avec 0,40 sans relever le total ; ≈ 77 USD attendus.
  - Inconvénient : correction de sévérité plus imprécise, et moins de fiches vérifiées en antériorité, alors que la plausibilité est l'objectif déclaré.

**Recommandation** : **(a)**, confiance 0,6. L'objectif « inédit et plausible » repose sur l'antériorité et les témoins, les deux postes que (c) rogne. Le séquençage garde la main : le pré-pilote mesure trois des quatre facteurs du pire avant que la course ne s'engage.

**Défaut sous 48 heures** : aucun. C'est un nœud de dépense : sans mot de Lazar, rien n'est lancé et GO-2026-10-30-07 reste tel quel (pré-pilote ≤ 32, total 110).
