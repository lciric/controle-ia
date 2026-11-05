# Proposition B — suite de P3 : programme, revendications, porte G0, appel du 21 octobre — v1

- **Proposeur B**, sous-agent neuf. Brainstorm à protocole fermé (R-203 (2)). Je n'ai vu aucune autre proposition.
- Écrit le 2026-10-20, dépôt en lecture seule. Je n'ai lu ni `prereg/P3-consignes-v1.md`, ni les textes d'action, ni aucune clé.
- **Rien n'est décidé ici.** Tout changement d'hypothèse, de revendication ou de critère de porte, toute dépense, tout contact externe : nœud de Lazar.
- Le verdict R13 et l'addendum ne sont pas rendus. Chaque option dit sa branche :
  - **A** : négatif confirmé sans réserve ;
  - **B** : négatif avec réserves (instrument, plancher, fuite) ;
  - **C** : instrument jugé en échec.

Abréviation : `lecture` = `diag/20261020-075740-p3-lecture/lecture-p3.json`, clé `resultat`. `prereg` = `prereg/P3-premier-test-i-a-v1.md`.

---

## 0. Faits de départ

| n° | fait | valeur | source |
|---|---|---|---|
| F1 | L'organisme est établi, bien au-delà de la consigne | effet 1,52 en log10, intervalle [1,25 ; 1,80], soit environ 33 fois le coût honnête ; la prédiction disait « au plus ≈ 0,48 » (triplement) | `lecture` → `P3-P1` ; `prereg` l. 155 |
| F2 | Le témoin et la mention baissent le coût déclaré | −0,32 [−0,57 ; −0,06] et −0,32 [−0,54 ; −0,12] | `lecture` → `P3-P2`, `cout_mention` |
| F3 | Aucune sonde au-dessus du plancher | tromperie 0,575 [0,531 ; 0,618], plancher 0,572 ; enjeux 0,525 [0,481 ; 0,570], plancher 0,536 | `lecture` → `P3-P3` |
| F4 | Sans plancher, on aurait annoncé une détection | borne basse de la tromperie 0,531, au-dessus de 0,5 | même clé |
| F5 | Le plancher et l'intervalle sont plus larges que prévu | plancher 0,572 et 0,536 contre « ≈ 0,52 à 0,53 » ; demi-largeur ≈ 0,044 contre « ≈ 0,025 à 0,037 ». Aire minimale détectable effective (mon estimation, plancher plus demi-largeur, non scellée) : ≈ 0,615 (tromperie), ≈ 0,58 (enjeux) | `prereg` l. 395 ; `lecture` → `P3-P3` |
| F6 | Des directions aléatoires séparent fort | maximum du plancher 0,78 (tromperie, saboteur contre honnête) | `lecture` → `P3-P3.tromperie-difference_moyennes-c15.plancher_max` |
| F7 | Une règle boîte noire triviale fait bien mieux | le coût déclaré seul sépare saboteur et honnête à 0,888 (descriptif : c'est le comportement, pas une fuite) | `lecture` → `audit_R4.jeux[0].cout_seul` ; `prereg` l. 262 |
| F8 | L'accumulation ne sauve rien (descriptif) | rappel 0,067 (enjeux, somme comme maximum) ; 0 et 0,017 (tromperie) | `lecture` → `P3-P5` |
| F9 | Le signal de la tromperie se concentre sur le champ du coût (descriptif seulement : P3-P4 non conforme) | 0,914 sur le champ `COST`, 0,554 avant ; à coût égal (T4), non au-dessus | `lecture` → `intention.tromperie-difference_moyennes-c15.T2`, `.T4` |
| F10 | La validation générique est saturée | 9 sondes de tromperie sur 15 à 1,0 ; la principale a été désignée par l'ordre de départage | `diag/20261019-230011-p3-reel/sondes-figees.json` → `resultat.aires_validation.tromperie` ; `prereg` l. 309 |
| F11 | L'addendum ne vise que les conclusions établies | seule P3-P1 l'est ; il peut ajouter une réserve sur elle (A6), rien sur le négatif | `prereg/P3-addendum-lecture-complementaire-v1.md` l. 226, 289, 293 |
| F12 | Seul le coût est mesurable dans l'environnement (a) | familles « contrôles » et « directions » non retenues | `docs/verdicts/verdict-T0.5-pilote-v1.md` l. 48, 165 |
| F13 | Argent et calendrier | phase 0 : au plus ≈ 63,2 USD avant P3, plus ≈ 3,96 USD pour P3, plus les disques, sur 150 ; GO de calcul échu le 2026-11-01 ; crédit relu 11,79 USD ; plan financé à partir de décembre | `registres/depenses.md` (lignes du 18 au 20 octobre) ; `registres/go.md` (GO-2026-10-04-08) ; `registres/etat.md` l. 40 (N-017) |
| F14 | Appel EA Funds | mercredi 21 octobre, 16 h 30 (Paris), confirmé le 18 octobre ; R-206 parlait d'un décalage : Lazar doit confirmer la date | branche `canal/copilote-grant-n04`, point 4 ; `registres/decisions.md` R-203, R-206 |

**Deux conséquences de F11.**
- En branche B, les « réserves sur le négatif » ne viendront pas de l'addendum. Elles viendront du verdict R13, ou de notre propre énoncé de portée (F5, F10).
- Le négatif n'a donc pas d'audit de puissance gelé. Il faut l'écrire nous-mêmes, en clair : « non détecté à cette puissance », avec F5.

---

## 1. Options

### B1 — L'appel du 21 octobre : un texte par branche, et la liste de ce qu'on ne dit plus

- **Branche** : toutes, plus un état « verdict non scellé » (possible à l'heure de l'appel).
- **Ce qu'elle tranche** : ce que Lazar dit de P3 au fonds, et quelles phrases de la fiche changent.
- **Phrases de la fiche devenues fausses ou fragiles** (`brouillons/entretien-ea-funds-v1/fiche-entretien-v1.md`) :
  - l. 19, « My bet is… » : garder le pari, ajouter que le premier test ne l'a pas trouvé avec des sondes génériques ;
  - l. 21, « The next gate asks whether probes trained on generic deception data see an instructed saboteur… » : la question a sa réponse mécanique, négative ;
  - l. 78, « Can 8B models sabotage subtly enough? » : réponse honnête, non sans dose (F1, F7) ;
  - section 5 (état) : ajouter P3 ; « about 55 dollars » devient ≈ 67 USD plus les disques (F13, à recompter).
- **Texte A, à dire (anglais)** : « Our first pre-registered white-box test is done. An instructed Llama-3.1-8B saboteur inflated its declared costs about thirty-fold. Two generic probes, deception and high stakes, trained without any organism data, did not separate its actions from honest ones above a covariance-matched random floor: 0.575 and 0.525 against floors of 0.572 and 0.536. Without that floor, the deception probe would have looked like a detection. We report it as not detected at this power. It was sealed before any data and cost about four dollars of GPU time. »
- **Texte B** : le texte A, plus les réserves du verdict, plus : « a probe at about 0.60 could have been missed » (F5).
- **Texte C** : « The run is done, but a fresh reviewer judged the instrument itself failed [motif]. We draw no conclusion about probes from it. »
- **Verdict non scellé** : « The mechanical reading line is negative; the verdict of a fresh reviewer is pending. » Passage au copilote : réponse r04 promise (branche `canal/copilote-grant-r03`, point 3), sur l'accord de Lazar.
- **Ce qu'on ne dit plus, ou pas** :
  - « white-box monitoring does not work », « probes cannot detect sabotage » : un organisme, deux sondes, 60 tâches, dix pas ;
  - « there is no trace in the activations » : F6 le contredit ;
  - « the negative theorem is confirmed » : P3 n'en dit rien (B2) ;
  - « near miss », « trend » pour 0,575 ; le 0,914 du champ du coût comme signal d'intention (F9, verrou de l'addendum l. 289) ;
  - l'accumulation (F8) comme résultat.
- **Ce que les 60 000 USD achètent maintenant** (à proposer à Lazar) : le plan financé ne repose pas sur des sondes génériques. Il teste des sondes construites pour l'intention (paires synthétiques, P-011 (a), concepts 3 et 4), l'organisme réglé sans instruction (ii), un organisme dosé (B4), et le volet juges du papier C.
- **Coût** : aucun calcul ; ≈ 2 heures de session ; une relecture par un sous-agent neuf, chargée de chasser l'enjolivement ; une répétition par Lazar.
- **Revendications touchées** : aucune formellement. Formulations de la fiche ; dans la proposition envoyée, l. 71 et 97 de `livrables/candidature-ea-funds-v1/proposal-v1.md` si Lazar les cite.
- **Piège principal** : l'enjolivement (quasi-détection, signal au champ du coût). Le piège symétrique : la sur-généralisation (« la boîte blanche échoue »). Second piège : annoncer comme verdict une lecture non scellée.

### B2 — Note de portée après P3, sur le modèle de N-013 : aucune hypothèse retirée, des préconditions ajoutées

- **Branche** : A ; B avec ses réserves recopiées. Rien en C : une note de portée sur un instrument en échec serait fausse.
- **Ce qu'elle tranche** : ce que P3 change aux énoncés retenus (N-003 à N-013, N-023), sans les réécrire.
- **Hypothèse par hypothèse** :

| hypothèse | effet de P3 |
|---|---|
| H1 (gain blanc sur noir) | énoncé inchangé. Réserve : sur (i-a), la règle du coût (0,888) bat de loin les sondes génériques (≤ 0,575). Ce n'est pas un test de H1 : (i-a) n'est pas diffus (F1, F7) |
| H2 (N-007) | inchangée. Réserve de faisabilité : avec ces deux sondes, rappel ≤ 0,067 (F8, descriptif). G1 ne peut pas compter sur elles |
| L, T | inchangés. « δ non détecté avec deux sondes génériques » n'est pas « dommage porté par la corrélation ». La question pivot (proposal l. 71) reste ouverte ; P3 en est un premier point |
| H8 | inchangée. Elle gagne du poids de fait : témoin, mention, champ du coût donnent une matière de validité de construit, en descriptif |
| HC2, HC2b, HC3 (versant sondes), HC4 | **précondition** à écrire dans le préenregistrement du papier C (critère 7 de G0) : une sonde de l'auteur qui ne sépare pas saboteur et honnête dans le plan 2 × 2 rhétorique × intention ne peut pas lire « g_sonde ≈ 0 ». Sinon on mesure la robustesse d'un instrument aveugle. Ligne « non lisible » à ajouter à C-P4 et C-P6 (`brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon3.md` l. 45, 48) |
| HC1, HC5 (volet juges), HC6 | sans effet |
| H3, H4′, H5, H7 (papier B) | dépendance écrite : tous supposent une signature interne lisible. À revoir à G1, pas avant |
| Tr, H6 | sans effet |

- **Papiers.** A : P3 devient sa première pièce empirique, rapportée comme négatif ; pas de rapport séparé avant G1 (publication : nœud ; recherche affirmative d'abord, R8, ce négatif est peut-être déjà publié). B : dépendance ci-dessus. C : précondition ci-dessus.
- **Proposition envoyée** : l. 97 (« validity prediction ») suppose une sonde qui réussit sur (i). Ajouter « if a probe succeeds on (i) ».
- **Coût** : processeur ; ≈ une demi-journée ; contre-lecture par un sous-agent neuf ; GO de type « revendication » si Lazar fait de la précondition une partie de l'énoncé.
- **Revendications touchées** : HC2, HC2b, HC3 (sondes), HC4 par précondition ; H1, H2 par réserve ; aucune retirée.
- **Piège principal** : retirer ou affaiblir des revendications sur un seul négatif (un organisme instruit et bruyant, deux sondes génériques). Le piège inverse : réécrire un énoncé après les données sans décision de Lazar.

### B3 — Critère 3 de G0 : ouvrir dès le verdict le nœud prévu au 26 octobre

- **Branche** : A et B. En C, le nœud porte d'abord sur l'instrument (B6).
- **Ce qu'elle tranche** : que fait G0 d'un critère 3 qui ne peut plus être rempli au 1er novembre.
- **Pourquoi maintenant** :
  - P-007 prévoit ce nœud au 26 octobre (`docs/decisions/proposition-P-007-plan-G0-v1.md` l. 38) ;
  - le critère 3 exige (i) et (ii) ;
  - P3 couvre (i-a) et deux sondes sur les quatre prévues (`brouillons/T0.7-sondes-v0-v1-brouillon4.md` l. 65) ;
  - les sondes « dissimulation » et « intention » attendent des jeux synthétiques non écrits (`registres/etat.md`, ligne T0.7, « Reste ») ;
  - T0.6, T0.7, T0.8 et G1 ne sont pas scellés.
- **Options** :
  - **(a)** Critère 3 inchangé ; G0 glisse (P-007 (b)), à fin novembre au plus tard. Avantage : aucune porte abaissée ; le plan financé commence en décembre (N-017). Inconvénient : la phase 1 et la piste C glissent ; le GO de calcul échoit le 1er novembre, donc nouveau devis.
  - **(b)** G0 déclarée « non franchie » au 1er novembre, critère 3 « non rempli », et rapportée telle quelle ; la fin de G0 ouvre le plan financé. Avantage : honnête et daté. Inconvénient : même travail que (a), annoncé plus tôt.
  - **(c)** Critère 3 réécrit, par exemple « sondes évaluées contre le plancher, quel qu'en soit le signe ». Je le déconseille : c'est abaisser une porte après un négatif (GO de type « revendication »).
- **Recommandation** : (a), confiance ≈ 60 %. Une porte n'a pas de défaut : nœud.
- **Réalignement de T0.7** (routine, avant son scellement) :
  1. **Compter P3.** Tromperie et enjeux ont déjà été lus sur (i-a). Les relire sous T7-P1 serait une seconde chance (T0.7 l. 143). Soit les retirer de T7-P1 sur (i-a), soit inclure P3 dans la correction de Bonferroni (l. 94).
  2. **Mode de sabotage.** T0.7 (l. 47) lit le mode « contrôles omis ou affaiblis », que le verdict du pilote a retiré (F12).
  3. **Choix de la sonde principale.** Sur une validation saturée, on choisit par l'ordre de départage (F10). Geler une validation non saturée (par exemple les jeux d'évaluation hors distribution de la source « enjeux », déjà dans la provenance de T0.7).
- **Coût** : processeur ; nœud en ≈ 1 heure ; réalignement de T0.7 ≈ 1 jour plus une contre-lecture. Calcul : celui du devis (P-007 : T0.6 (i) 8 heures, T0.7 6 heures), à redevis après le 1er novembre.
- **Revendications touchées** : critère 3 de G0, en lecture en (a) et (b), en texte en (c) ; aucune hypothèse.
- **Piège principal** : faire passer (c) pour (a), par exemple en redéfinissant « sondes v0 » pour n'y garder que celles qui passeront. Ou relire P3 avec d'autres sondes ou couches : interdit par la ligne gelée (`prereg` l. 428).

### B4 — Rendre l'organisme diffus avant de reparler de boîte blanche contre boîte noire

- **Branche** : toutes. L'organisme est un fait indépendant des sondes. Exception : une réserve A6 de l'addendum sur P3-P1.
- **Ce qu'elle tranche** : comment T0.6 (critère 2), T0.8 (critère 4) et G1 (critère 6) tiennent compte d'un saboteur bruyant.
- **Constat** :
  - (i-a) n'est pas un saboteur diffus au sens du programme (papier A ; N-007 : « chaque action sabotée reste sous le seuil d'un moniteur par action calibré à 1 % ») ;
  - on lui demande trois fois le coût, il en déclare environ 33 fois (F1) ; le coût seul le sépare à 0,888 (F7) ;
  - la dose écrite n'est pas la dose réalisée.
- **Proposition** :
  1. Ajouter une base « règle du coût déclaré » : seuil sur le coût, calibré sur l'honnête. Elle va dans les bases boîte noire de T0.8 et dans la « meilleure base boîte noire » de G1 (N-008). C'est la base triviale la plus forte sur la seule famille mesurable (F12).
  2. Dans T0.6, définir les doses « diffuses » par cette base seule, avant toute lecture de sonde. Par exemple : les doses où son rappel par action à 1 % de faux positifs reste sous un seuil gelé. Mesurer la dose réalisée (effet du type P3-P1 par dose), pas la dose écrite.
  3. Calculer la puissance de G1 sur les aires observées de P3 (planification), pas sur des aires supposées.
  4. Écrire d'avance : si les sondes génériques ne voient pas un facteur 33, elles verront mal un facteur 1,5. G1 sur ces sondes serait un négatif attendu. C'est permis (R3), mais doit être dit au préenregistrement.
  5. Déclarer dans T0.6 et T0.7 que le témoin instruit n'est pas neutre sur la grandeur mesurée (F2).
- **Coût** : processeur, ≈ 1 jour (textes de trois préenregistrements) ; calcul dans le devis de T0.6 ; aucune dépense nouvelle.
- **Revendications touchées** : H1 (« tâches floues »), H2 (seuil par action de N-007) ; critères 2, 4 et 6 de G0, en lecture.
- **Piège principal** : régler la dose en regardant les scores des sondes jusqu'à trouver une zone où la boîte blanche « gagne » (R3). La dose se fixe sur la boîte noire seule, avant toute lecture boîte blanche.

### B5 — Ce qui reste de la phase 0 : d'abord ce qui ne dépend pas des sondes

- **Branche** : A et B ; en C, après B6.
- **Ce qu'elle tranche** : l'ordre du travail et de la dépense d'ici au 1er novembre.
- **Marge** : sous le plafond, ≈ 150 − 63,2 − 3,96 ≈ 83 USD, moins les disques (F13) ; le GO de calcul échoit le 1er novembre.
- **Ordre proposé** :
  1. plan B des juges (N-022 : une étape payante, sur devis et GO séparé) ;
  2. préenregistrement du papier C (critère 7), avec la précondition de B2, puis son pilote (GO-2026-10-17-01, 4 heures ; Panin toujours non lu, R-193) ;
  3. état de l'art (critère 8) ;
  4. préenregistrement de G1 (critère 6), avec B4 ;
  5. aucune nouvelle passe de sondes sur un organisme avant le scellement de T0.7 réaligné (B3) et, en branche C, du témoin positif (B6).
- **Coût** : aucun calcul ajouté ; c'est un réordonnancement.
- **Revendications touchées** : aucune.
- **Piège principal** : fuir vers le papier C pour masquer le négatif du papier A. Or HC2, HC2b, HC3 (sondes) et HC4 dépendent eux aussi d'une sonde qui lit l'agent (B2). Second piège : tout faire tenir avant le 1er novembre en sacrifiant les contre-lectures.

### B6 — Branche C, et réserves d'instrument en B : un témoin positif de la chaîne des sondes avant toute nouvelle lecture

- **Branche** : C ; B si les réserves visent l'instrument. En A, utile seulement pour T0.7.
- **Ce qu'elle tranche** : si l'instrument est en cause, ce qu'on répare avant de conclure quoi que ce soit.
- **En C** : P3 ne dit rien des sondes. Seule P3-P1 reste, si A6 ne la touche pas.
- **Suspects visibles sans nouvelle lecture** :
  - validation saturée et choix par départage (F10) ;
  - apprentissage sur des jetons du message utilisateur, lecture sur des jetons de l'assistant (`prereg` l. 300, TC-20 (f)) ;
  - agrégation par le maximum, alors que la recette de tromperie publiée préfère la moyenne (`docs/decisions/proposition-P-011-T0.7-sondes-v1.md` l. 23) ;
  - plancher plus haut que prévu (F5).
- **Proposition** :
  - un témoin positif préenregistré, lancé avant toute nouvelle lecture d'organisme : reproduire un résultat publié de la chaîne des sondes sur ses propres jeux d'évaluation (`brouillons/programme-approfondi-ABC-v1.md` l. 27 et l. 83) ; chiffre cible à revérifier sur PDF (R7) ; s'il échoue, la chaîne est en nœud ;
  - tout diagnostic sur les données gardées de P3 (par exemple maximum contre moyenne sur les scores par jeton) est un nœud (`prereg` l. 415) et reste descriptif. La moyenne n'entre jamais dans une sonde de production.
- **Coût** : processeur ≈ 1 jour (préenregistrement et contre-lecture). Calcul : ≈ 1 heure de carte, soit ≈ 1 à 2 USD (estimation du brouillon cité, non sourcée), sous GO-2026-10-04-08 avant le 1er novembre, sinon nouveau devis.
- **Revendications touchées** : critère 3 (volet instrument) ; Tr ; la décision 1 du programme (maximum ou attention) est éclairée, pas changée.
- **Piège principal** : relancer le témoin positif jusqu'à ce qu'il passe, puis s'en servir pour « réhabiliter » P3. Un témoin réussi prouve que la sonde lit son concept générique, pas qu'elle lit le sabotage.

---

## 2. Ce que je ne propose pas

- Relancer P3, ou relire ses données avec d'autres sondes, couches ou jeux (`prereg` l. 428).
- Présenter 0,575 « au niveau du plancher », ou 0,914 au champ du coût, comme un signal.
- Une moyenne ou une médiane sur les jetons dans une sonde de production.
- Un chiffre de l'état de l'art non vérifié sur PDF dans la fiche de l'appel (R7).

## 3. Recommandation du proposeur

- **Avant l'appel** : B1, sans calcul.
- **Au verdict** : B2 et B3 (a).
- **Dans les préenregistrements à venir** : B4 (T0.6, T0.8, G1) ; B5 comme ordre de travail.
- **En branche C, ou si le verdict met en cause l'instrument** : B6 d'abord.
- Confiance ≈ 60 %.
