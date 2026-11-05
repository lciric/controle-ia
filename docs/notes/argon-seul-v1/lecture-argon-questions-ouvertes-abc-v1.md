# Lecture neuve des trois réponses d'« Argon seul » aux questions ouvertes a, b, c — v1

**Auteur** : lecteur neuf, sous-agent, modèle : Claude Fable 5.1 (`claude-fable-5-1`). Je n'ai écrit ni les questions, ni les pièces servies, ni les réponses. Je ne décide rien et ne recommande rien : l'avis d'Argon est lu à côté et ne tranche rien (GO-2026-10-31-08).

**Date** : 2026-10-31, 18:35 UTC.

**Fichiers lus** (dossier `donnees/sauvegardes-restaurees-2026-10-31-v1/1315/argon-seul/`), empreintes recalculées par `sha256sum` ; les compagnons `.sha256` des six fichiers et des `lancement.txt` correspondent (`sha256sum -c` : OK partout) :

| fichier | sha256 recalculée |
|---|---|
| `question-argon-a-v1.md` | `724779aa32e039316f6b9981d250d29678a23dba4d7762ce537680abb1fe8e0a` |
| `question-argon-b-v1.md` | `c15556e776fce0b24004218ec3a144a7a67fe33acbeb0d324c5c8587e473449a` |
| `question-argon-c-v1.md` | `6885128241a8053252dc9891f7dbb17d2fc3a487ee6af0171e3ff671c00ec446` |
| `argon-seul-course2-prepilote-v1/reponse-argon-v1.json` (réponse A) | `d3c6a0852a2751c89a2a370da528c86537d2d6c5e5a13a30041ec352076ffa60` |
| `argon-seul-course2-questions-b-v1/reponse-argon-v1.json` (réponse B) | `8e0ce80c51571ad106c3563e94d3ea50660eee609d3d8617147489296bc866f4` |
| `argon-seul-course2-questions-c-v1/reponse-argon-v1.json` (réponse C) | `d35e82c3c0fbd38aa15ba45e9bb8e3507cb84892f42f0fcfccaf8defc867c58b` |

**Métadonnées des réponses** (champs du JSON) :

| réponse | coût (USD) | modèle demandé → servi | fin | jetons entrée / sortie | mots du texte | mots demandés |
|---|---|---|---|---|---|---|
| A (course 2, pré-pilote) | 1,0475 | gemini-4-argon → gemini-4-argon | STOP | 43 780 / 16 485 | ≈ 8 570 | « environ 6 000 au plus » |
| B (porte G0) | 0,6076 | gemini-4-argon → gemini-4-argon | STOP | 24 928 / 9 655 | ≈ 4 840 | « environ 5 000 au plus » |
| C (bisociation, arène, reste) | 0,5392 | gemini-4-argon → gemini-4-argon | STOP | 15 333 / 9 925 | ≈ 5 350 | « environ 5 000 au plus » |

Total : 2,19 USD. Dans les trois réponses, `pensees_jetons` = 0 et `lecture_pensees` = « indetermine » bien que `config_pensee` soit vrai : aucune trace de réflexion n'est comptée. La réponse A dépasse la longueur demandée d'environ 40 %. Les journaux `relais-gemini-*.log` et `*.jsonl` n'ont pas été lus (consigne).

**Convention de statut** dans les tables : VÉRIFIÉ = Argon renvoie à un fait servi et je le retrouve dans la question ; RAPPORTÉ = Argon s'appuie sur une source hors des faits servis ; SUPPOSÉ = raisonnement, calcul ou valeur propres à Argon, sans fait servi qui le porte. Quand une case mêle les deux, le statut dominant est donné d'abord. Les numéros de ligne qu'Argon cite (« l. 246 », « l. 363-365 ») ne sont pas vérifiables : les questions ne numérotent pas les lignes à l'intérieur des extraits ; ils tombent dans les plages servies et ne sont comptés ni comme exacts ni comme inexacts.

**Point préalable, commun aux trois dossiers : le retrait des recommandations est incomplet.** Les questions annoncent que les recommandations et confiances des auteurs ont été retirées. Plusieurs ont survécu dans le texte servi :
- question A, pièce 1 : Résumé pt 4 « (ajouter 4 fiches […] recommandé ; ou déclarer le vide) », pt 5 « (retarder le gel jusqu'à l'annexe, recommandé ; ou geler à deux bras […]) », pt 6 « (2) […] recommandé » ; section « Décisions à Lazar » : « **Configuration recommandée dans son ensemble […] : D-g (b), D-i (2), D-h (a), D-j oui, L1 à L3 et L5 à L7 telles que lues par l'auteur** » ; la table « Porte » a une colonne « Configuration recommandée » ; les « valeurs proposées au brouillon » des seuils sont elles-mêmes la proposition de l'auteur ;
- question A, pièce 3 : § 6 « Confiance de la décision 1 : moyenne, au plus » ; § 7, AF4 « Le recompte est ma recommandation » ;
- question A, pièce 4 : point 4 de « Ce qu'il faut de toi » : « Je ne le recommande pas : (A) n'en a pas besoin » (sonde HTTP simple) ;
- question B, pièce 1 : les passages du mémo de conv-audit recopiés mot pour mot gardent « **Reco (a), 0,7.** Défaut (a). » (G0-1), « **Reco (a), 0,6.** Défaut (a). » (G0-2), « **Reco (a), 0,75.** Défaut (a). » (G0-5) ; la colonne « option 1 » est annoncée comme le défaut de la grille ;
- question C, pièce 4 (déclarée « 0 retraits ») : § 3 (a) « proposait déjà fait 9 tel quel au tour 2, scores instruits à part », § 5 « proposition : fait 9 tel quel au tour 2, scores à part », § 6 « contre-lecture par une autre famille recommandée » ; pièce 2 : « confiance abaissée d'élevée à moyenne », « défaut inchangé » (corrections Q7-A5 et fin de pièce).

Conséquence pour la lecture : sur D-g, D-h, D-i, D-j, L1 à L7 (A), sur D-G0-8 et D-G0-15 (B) et sur la décision 3 / divergence (a) (C), l'accord d'Argon avec la position de l'auteur ne peut pas être lu comme un avis indépendant. Je le signale ligne à ligne par la mention « (reco. visible) ».

---

## 1. Question A — course 2 et pré-pilote

### 1.1 Table des décisions (49 entrées traitées ; S13, S14 et S15 regroupées par Argon)

| décision | option choisie par Argon | raison (une ligne) | pire cas donné | ce qui le ferait changer d'avis | statut |
|---|---|---|---|---|---|
| S1 (exactitude équilibrée des juges) | garder 0,80 | le complément étalonne 0,80 → 0,63, 0,85 → 0,88, contient 0,70 à 0,16 ; 0,75 ferait passer un juge à 0,75 avec 0,47 | Kimi échoue par bruit, complément 11,6 à 12,5 USD ou nœud | complément (plafond 17,5) indisponible, ou exigence C1-C2 > 0,50 (0,38 sous P1) | VÉRIFIÉ |
| S2 (rappel minimal sur P) | garder 0,70 | évite un 0,80 obtenu par rejet systématique ; P ≥ 8 | juge sévère mais valide rejeté | P < 8 (pas de 0,125) | VÉRIFIÉ (P ≥ 8) ; SUPPOSÉ (arithmétique 1,00 / 0,60) |
| S3 (plancher d'échec) | garder 0,70 | défaillant : 0,01 à 0,90, 0,04 à 0,85, 0,84 à 0,60 | juge à 0,70 consomme le complément | prédiction de Kimi sous 0,75 | VÉRIFIÉ |
| S4 (Fleiss ; Cohen ; plancher) | garder 0,45 ; 0,35 ; 0,30 | P3 0,55 [0,35 ; 0,75], erreur-type 0,15–0,20 SUPPOSÉ ; C3 0,91 | deux juges décorrélés sur N2 (0,60) | C3 marginale rejetant > 15 % des runs où S1 passe | VÉRIFIÉ ; seuil 15 % SUPPOSÉ |
| S6 (fidélité du rendu) | garder 0,95 ; 1,00 ; 1,00 | A1 : la qualité plantée est celle du squelette | le relecteur à 1,00 déclenche C14 (0,09) | incompatibilité par construction entre C14 et S6 | VÉRIFIÉ |
| S7 (fausses alertes mémoire) | garder 0,05 ; 0,10 | P6 0,06 [0,02 ; 0,15] ; 25 sur ≈ 250 | 10 % de fiches inédites écartées en course | moins de 50 paires de vérification | VÉRIFIÉ ; seuil 50 SUPPOSÉ |
| S8 (rappel mémoire) | garder 0,80 | P6 0,85 ; 8/9 passe, 7/9 non ; conceptuel 0,60 | deux paraphrases conceptuelles manquées | ≥ 3 conceptuelles sur 9 | VÉRIFIÉ |
| S9 (union axe 7) | garder 0,75 ; 0,15 | P7 union 0,75, fausses alertes 0,10 ; C6 0,952 / 0,970 | table seule sacrifiée (0,116–0,124), C6 0,81 | L2 tranchée « retrait » : abaisser à 0,60 | VÉRIFIÉ |
| S10 (aiguilleur, rappel) | garder 0,90 (11/12) ; 0,75 | H-PP4 ; C7 0,85 « 0,66 direct + 0,31 à corriger » | deux fiches C4 manquées | C4 > 4 des 12 concrets | VÉRIFIÉ ; décomposition inexacte (§ 1.2, n° 1) |
| S11 (aiguilleur, fausses alertes) | garder 0,10 ; 0,34 | 3 sur 34 pour P8 0,03 ; 2 sur 6 pour 0,20 [0,05 ; 0,40] | un tiers des fiches denses censuré | rien à cet effectif | VÉRIFIÉ |
| S12 (débordement Kimi) | garder 0,10 | 0,05 intenable : « zéro sur 20 » borne à 0,14 (0,26 sur 10) ; C8 0,914 | passe « tableau » coupée (0,505), M5 sur 10 fiches | rien | VÉRIFIÉ |
| S13 / S14 / S15 (antériorité) | garder 0,90 ; 0,70 ; 0,10 | 0/9, 2/9, 2/22 ; P10 ; C9 0,986 | M6 réduite (0,19–0,24) : une erreur sur 3 altérées fait 0,667 | réduction > 0,30 : règle d'arrondi | VÉRIFIÉ |
| S16 (coût mesuré ÷ supposé) | garder ×1,30 | C10 0,999 sous 160 ; coupures Kimi ×1,447 | Kimi juge 1,4 [0,8 ; 3,0] dépasse et force un devis refait | si P11 est calculé hors ×1,447 : ×1,50 pour Kimi | VÉRIFIÉ ; condition SUPPOSÉ |
| S18 (aire témoins / Kimi ; effectif) | **alternative 0,75 ; 6 (R-2)** | C5 0,57 par version ; aire 0,62 ± 0,09 ; seconde version 5,8 USD « plus de 4 fois sur 10 » | différence stylistique de surface tolérée | C5 par version déjà > 0,75 à 0,70 | VÉRIFIÉ |
| S19 (aire P / N par la forme) | garder 0,65 | protège A4, A5 ; P12 0,55 ± 0,12 | régénération des témoins | ancres de S6 forçant une différence de longueur : 0,70 (R-3) | VÉRIFIÉ |
| S20 (ambigus ; effectifs) | garder 4 ; P ≥ 8, N ≥ 10 | 10 % SUPPOSÉ → 2,3 sur 23 ; puissance 0,90 / 0,71 / 0,50 | 5 ambigus → seconde version | rien | VÉRIFIÉ |
| S21 (titre ; résumé) | garder 120 ; 200 | 200 = borne commune de la pièce 3 (AF5) | titre long tronqué | > 10 % des titres OpenAlex > 120 | VÉRIFIÉ ; seuil SUPPOSÉ |
| S23 (k paires par bras) | garder k = 1 | H-PP9 éprouve la chaîne, pas l'effet ; k = 2 : +1,9 USD | la seule fusion échoue à l'aiguilleur (0,10) | budget > 55 USD | VÉRIFIÉ |
| S24 (Jaccard concepts) | garder 0,40 | P14 0,45 [0,25 ; 0,65] | 0,38 par bruit | liste > 200 entrées | VÉRIFIÉ ; seuil SUPPOSÉ |
| S25 (m meilleures paires) | garder m = 3 | ni moyenne diluée ni paire unique | fiche à un seul concept pénalisée | médiane < 2 concepts par fiche à l'essai S31 | SUPPOSÉ (aucun fait servi sur m) |
| S27 (couverture Gu-Krenn) | garder 0,60 (réserve) | P14 0,50 [0,20 ; 0,90] ; réserve hors porte (L6) | aucun | L6 « retrait » : abaisser à 0,30 | VÉRIFIÉ |
| S30 (rappel M6b, si D-g b) | garder 3 sur 4 (réserve) | 0,60 par fiche ; 3/4 avec 0,475 ; 4/4 : 0,13, borne 0,47 | alerte une fois sur deux | rien | VÉRIFIÉ ; « 0,13 » SUPPOSÉ (calcul propre) |
| S31 (substitut Gu-Krenn) | garder la spécification | sortie de l'annexe (CP5-01), C12 0,97 ; programmée sans jugement | moisson trop étroite, couverture sous S27 | essai à blanc sur la moisson | VÉRIFIÉ |
| D-e (domaine, concept) | (i) | seule option qui sépare les deux espaces et rend S24 mesurable | argmax dégénéré dans une case unique | S24 sous 0,20 en É0 | VÉRIFIÉ |
| D-f (rôles neufs) | (i) T = Sonnet 5.5, relecteur = Fable 5.1 | A9 : ni rendu ni relecture par un juge ; (ii) et (iii) sont des juges | biais de famille (CP2-05) | quatrième famille disponible | VÉRIFIÉ |
| D-g (antériorité non citée) | (b) M6b (reco. visible) | « inédit » n'est éprouvé par rien ; 1,4 USD ; porte 0,175 → 0,173 | M6 réduite 0,19 → 0,24, fusions 0,16 → 0,20 | 4 PDF non réunis (DEP2c) avant le gel | VÉRIFIÉ ; chiffres de porte inexacts (§ 1.2, n° 2) |
| D-h (gel et bras méta) | (a) retarder (reco. visible) | collisionneurs lancés le 30 octobre ; (b) : C12 0,86, porte 0,155 | annexe après le 7 novembre → nouvelle ligne de GO | annexe non contre-lue au 5 novembre avec DEP4, DEP5 prêtes | VÉRIFIÉ |
| D-i (plan des fonds) | (2) (reco. visible) | paires inter-fournisseurs ; C6 0,936 → 0,952 ; +0,55 USD ; (3) biaisée par le script | surcoût 0,55, ≈ 2 paires descriptives | rien | VÉRIFIÉ |
| D-j (Gu-Krenn sans reproduction) | oui (reco. visible) | A6 : gardes en aval ; « non » réactive S26 | 8 fusions sous-optimales sur 24 | validation de session-depot : pire que le hasard | VÉRIFIÉ ; « 8 sur 24 » SUPPOSÉ |
| L1 (passe « tableau ») | gardée (reco. visible) | M5 à 20 fiches (0,47) ; borne 0,14 contre 0,26 ; C8 0,92 → 0,914 | coupée par son relais 4,6 USD (0,486–0,505) | orchestrateur incapable d'arrêter proprement | VÉRIFIÉ |
| L2 (table seule) | gardée (reco. visible) | 0,7 USD ; C6 0,81 → 0,952 | perte de 0,7 USD (0,043) | aucun | VÉRIFIÉ |
| L3 (désaccord hors score) | hors score (reco. visible) | R-638, garde R5 ligne 24 | paire consensuelle plutôt qu'en tension | > 80 % de paires redondantes aux collisionneurs (R-630) | VÉRIFIÉ ; seuil 80 % SUPPOSÉ |
| L5 (fusions retirées) | lue sur les paires, réserve, O15 (a) (reco. visible) | sacrifice de rang 1 (0,16–0,20) ne doit pas être un nœud | course sans fusion jugée | erreurs de formatage à l'essai É0 | VÉRIFIÉ |
| L6 (S27 réserve) | réserve (reco. visible) | A19, R-635 ; 0,50 attendu < 0,60 | bras sur peu de fiches | rien | VÉRIFIÉ |
| L7 (brouillon 3) | accepté (reco. visible) | remplacé avant la contre-lecture 3 ; 4, 5, 6 contre-lus ; CL5 sur le gelé | aucun | section disparue sans trace | VÉRIFIÉ |
| DEP5 (étalonnage aiguilleur) | oui, lever le défaut R-819 | au défaut, porte à 0 | délai des 12 concrets | rien | VÉRIFIÉ |
| A15 (confidentialité) | oui, sous trois conditions | A15 : « aucun lancement » ; aiguilleur en amont ; risque 0,05 × 0,08 | fiche débordante lue par un juge externe | interdiction de tout envoi de résumés à des API commerciales | VÉRIFIÉ ; conditions (1) à (3) et produit 0,004 SUPPOSÉ |
| Texte III, déc. 1 (loi sur K) | (a) uniforme sur population finie | seule non circulaire et recalculable ; sélection traitée par γ / Wallenius | forte pénalité de n* sous sélection | générateur de familles à loi connue et scellée | VÉRIFIÉ |
| Texte III, déc. 2 (estimateur) | (c) point + [37, +∞[, intervalle suspendu | aucun intervalle établi ; borne perdue sous dépendance ; G² 12,85 ; 163,0 à 186,3 | moins informatif | résultat de l'expérience première | VÉRIFIÉ |
| Texte III, déc. 3 (couverture) | (a) incidence 0,845 (0,155), abondance rapportée | plan d'incidence ; Chao1 abandonné ; critique de C erronée | cible 0,155 plus stricte | surestimation montrée par l'expérience première | VÉRIFIÉ |
| Texte III, déc. 4 (zone d'indifférence) | (a) oui | perte de couverture près de τ, défenses saines refusées | familles de la bande non tranchées, paramètre à sceller | erreur-type < 0,01 τ | VÉRIFIÉ ; seuil 0,01 τ SUPPOSÉ |
| Texte III, déc. 5 (minimum observé) | (a) obligatoire, non certifié | quantile masque un effondrement ; coût nul | lecture comme pire cas sur K | rien | VÉRIFIÉ |
| Tableau, déc. 1 (défaut, course 2) | **(a) course 2 figée** (position de A seule) | le pré-pilote réel n'éprouve que M8 ; la batterie de la pièce 3 serait un second pré-pilote « ni chiffré ni couvert par les 160 USD » | course sans échange riche | budget et délai dédiés hors 160 USD avant le 14 novembre | VÉRIFIÉ (M8, S21, 14 nov.) ; « non couvert » SUPPOSÉ |
| Tableau, déc. 2 (ordre) | (a) détecteur d'abord (si pré-pilote du tableau) | moins cher, condition nécessaire | qualification séquentielle plus longue | protocole de D (toutes paires à l'aveugle) | VÉRIFIÉ ; « humaine » SUPPOSÉ |
| Tableau, déc. 3 (bras comparatif) | **option nouvelle (d) : aucun bras** ; sinon (a) | nœud de dépense ; hors périmètre si déc. 1 (a) | exception non testée | GO dédié | SUPPOSÉ (option inventée) ; « toutes les espèces » inexact (§ 1.2, n° 3) |
| Tableau, déc. 4 (unité de code) | (a) chemin ou transformation (D) | risque porté par les chemins, pas par le découpage | recompte formel | unité sans emploi si déc. 1 (a) | VÉRIFIÉ |
| Tableau, déc. 5 (qualité jugée) | (b) information seulement | A4, R-634, N-058 | tableau profond non avantagé | qualité = survie aux tests de mort | VÉRIFIÉ |
| Tableau, déc. 6 (critères 8 et 1) | (a) tour III.1, lecture stricte | AF2, AF5 ; (b) est un écart | corrections du tour III.3 sans effet sur le compte | rien | VÉRIFIÉ |
| Machine jetable (louer ; architecture ; projet ; hôte ; sonde ; clé) | **oui, 10 USD ; (A) mixte ; projet dédié ; (R-d) puis (R-b) en S0, (R-a) en repli ; sonde : non ; clé d'hôte jetable** | (B) sort le jeton, (C) écart « jamais poussé » ; (R-a) affaiblit une défense noyau ; S0 < 0,2 USD | classifieur bloque `ssh` : commandes à la main, 5 à 10 min | debian-13 indisponible ou bwrap bloqué en S0 : (R-a) d'avance | VÉRIFIÉ ; versions de debian-13 présentées comme acquises alors que SUPPOSÉ dans la pièce (§ 1.2, n° 4) |

**Liaisons et priorités données par Argon** : lot 1 (D-g, D-i, L1, L2, L5, S18, sous S17), lot 2 (S21, L1 et décisions 1, 2, 3, 5 du tableau), lot 3 (D-j, S25, S27, S31, L6), lot 4 (déc. 2 et 3 du texte III, expérience première). Trois premières : A15 + DEP5 + D-h (a) ; GO machine jetable ; décision 1 (a) du tableau.

### 1.2 Affirmations inexactes sur les faits servis (A)

Trente-quatre chiffres ou renvois recoupés (liste § 4). Inexacts ou mal attribués :

1. **S10** : « C7 à 0,85 (0,66 direct + 0,31 à corriger) ». La pièce donne « 0,85 (direct 0,66 ; à corriger 0,31) » sans dire que ces deux nombres s'additionnent ; 0,66 + 0,31 = 0,97 ≠ 0,85. La présentation en somme est propre à Argon et fausse arithmétiquement.
2. **D-g** : « impact négligeable sur la porte (0,175 → 0,173, soit −0,002 avec D-i (2)) » et « dépense médiane passant de 37,6 à 40,1 USD » attribués à M6b. La pièce dit : « D-g (b) ajoutée à D-i (2) la fait passer de 0,176 à 0,173 (−0,003, sortie v9 ; D-g (b) seule n'est pas jouée) » ; 0,175 et 37,6 sont le texte de base (D-g a **et** D-i 1), 40,1 la configuration retenue (D-g b **et** D-i 2). Argon impute à M6b seule l'effet joint des deux décisions, avec le mauvais point de départ.
3. **Tableau, décision 3** : « (a') complet libre, que toutes les espèces jugent exposé aux instructions glissées, section 7 AF1 ». AF1 dit : « B tient le complet pour exposé et le minimal pour sûr ». Une espèce, pas toutes.
4. **Machine jetable** : « debian-13 (qui embarque nativement Python 3.13 et bwrap 0.11 sans dépôt tiers deadsnakes) » présenté comme acquis. La pièce range ces versions sous « SUPPOSÉ » (« reprises de la v1 sans source ; à lire dans `etat-v1.txt` en S0 ») et « Debian 13 sans restriction AppArmor » aussi. Argon fonde son premier choix d'hôte sur des faits que la pièce elle-même ne tient pas.
5. **Tableau, décision 1** : « second pré-pilote dédié au tableau qui n'est ni chiffré dans le devis v6 ni couvert par l'enveloppe de 160 USD (Pièce 1, L4) ». L4 dit seulement que le total séquencé est de 160 USD pré-pilote compris ; rien dans les faits ne dit si une batterie du tableau y entre ou non. Renvoi qui ne porte pas l'affirmation.
6. **DEP5** : « pré-pilote à 40 USD » : l'attendu est 32,1 USD, la médiane 40,1, le plafond 50. Approximation, pas une erreur de fond.
7. **S4** : « le seuil de 0,45 donne une probabilité de succès de C3 de 0,91 » : la ligne C3 de la table mêle l'accord **et** la réfutation (ii) (rejet des C 0,30) ; 0,91 n'est pas l'effet du seul seuil.

Exacts (parmi les recoupés) : S1 (0,80 [0,65 ; 0,92] ; 0,63 / 0,88 / 0,16 ; 0,47 contre 0,29 ; 11,6–12,5 ; 17,5 ; 0,38), S3 (0,01 / 0,04 / 0,84), S7 (0,06 [0,02 ; 0,15] ; 25 sur ≈ 250), S8 (8/9, 7/9 ; 0,60), S9 (0,75 [0,50 ; 0,90] ; 0,952 / 0,970 ; 0,116–0,124 ; 0,81), S11 (3 sur 34 ; 2 sur 6 ; 0,20 [0,05 ; 0,40]), S12 (0,14 ; 0,26 ; 0,914 ; 0,505), S13-15 (0/9, 2/9, 2/22 ; 0,986 ; 6, 3, 11), S16 (×1,447 ; 0,999 ; 0,992 à ×1,175), S18 (0,57 ; 0,81 ; 0,62 ± 0,09 ; 5,8), S19 (0,55 ± 0,12), S20 (0,90 / 0,71 / 0,50), S23 (+1,9), S24 (0,45 [0,25 ; 0,65]), S27 (0,50 [0,20 ; 0,90]), S30 (0,475 ; 0,47), D-h (0,86 ; 0,155 ; 7 novembre), D-i (0,936 → 0,952 ; 0,176 ; +0,55), L1 (0,47 ; 4,6 ; 0,486–0,505), L2 (0,7 ; 0,043), L5 (0,16–0,20), texte III (49,19 ; 47,00 ; [40,6 ; 78,4] ; [39,9 ; 71,0] ; 12,85 ; 163,0–186,3 ; 0,845 ; 0,778 ; 0,155 ; 0,222 ; [37, +∞[), tableau (60 paires ; 24 à 30 plantations ; 4 + 12 cases ; 400 caractères ; 5 + 3 ; 120 / 200), machine (0,5 ; 7,4 ; 10 USD ; 15 novembre ; 0,2 ; 5 à 10 min).

### 1.3 Options manquantes proposées par Argon (A)

- Tableau, décision 3 : option (d) « aucun bras comparatif avant la course 2 », avec (a) en repli pour une course ultérieure.
- S16 : ×1,50 pour les seuls postes de Kimi, conditionnel à la base de calcul de P11.
- S27 : 0,30 si L6 devenait « retrait » ; S9 : 0,60 si L2 devenait « retrait » ; S14 réduit : « 1 erreur sur 3 » si la réduction de M6 dépasse 0,30.
- A15 : trois conditions (fiches synthétiques seulement ; aiguilleur en amont des envois ; les 12 concrets jamais envoyés à Moonshot ni Google). La troisième n'est ni dans les faits ni contraire à eux.
- Machine jetable : ordre d'essai (R-d) → (R-b) → (R-a) en S0 ; clé d'hôte jetable par cloud-init (la pièce la nomme comme durcissement possible « à Lazar d'en décider ») ; (R-a) « autorisé d'avance comme repli ».
- D-g : condition d'arrêt « 4 PDF non empreintés avant le gel ».

### 1.4 Ce qu'Argon n'a pas traité (A)

- La réserve « Dépendance » de la pièce 3 (A, B et le synthétiseur de la même famille) et la réserve « Effet de la question » (unanimité sur le défaut « en partie construite », confiance « moyenne, au plus ») : Argon tranche la décision 1 du tableau sans peser qu'il retient la position d'une espèce sur quatre et que la majorité (b) est la lecture de B, C, D.
- La « fermeture fragile » de l'exception (pièce 3, § 6) : non mentionnée.
- L'option de plan « M6 jouée juste après É1 » (pièce 1, « Autres cas », « à la décision de Lazar si elle l'intéresse ») : non examinée.
- Le « réappariement par un second lecteur » (texte III, « hors décision statistique ») : non examiné.
- Machine jetable : le point 3 (projet actuel ou dédié) reçoit une réponse, mais la réserve 5 (Python 3.13 par dépôt tiers, repli 3.12 = écart à CL16) n'est traitée que par le détour debian-13 ; la réserve 7 (fuites hors pare-feu : métadonnées, secours, DNS) n'est pas lue ; le texte proposé pour `decisions.md` (§ 8) non plus.
- Le biais de script de la variante (3) de D-i est cité, mais pas la question de savoir si une graine nouvelle est due avant le gel.
- La longueur : la réponse A dépasse la consigne d'environ 2 500 mots ; D-g à D-j ne figuraient pas dans la liste « Décisions à examiner » (seuls D-e, D-f y sont), ce qu'Argon signale et choisit de traiter ; cela n'est pas une faute, mais c'est là que la recommandation visible est la plus nette.

---

## 2. Question B — porte G0

### 2.1 Table des décisions (15 entrées ; D-G0-8 + DIV-2, D-G0-13 + DIV-1, D-G0-15 + DIV-3 regroupées par Argon ; 18 objets)

| décision | option choisie par Argon | raison (une ligne) | pire cas donné | ce qui le ferait changer d'avis | statut |
|---|---|---|---|---|---|
| D-G0-1 (échéances, scellement, défauts) | **option nouvelle** : échéance au **verdict scellé** (30 nov., 31 janv.), ouverture N jours avant (ex. 24 janv.), plus de lecture tardive à la seconde lecture, mot de Lazar couvrant dates, scellement et régime des défauts, aucun défaut sur DIV-1 à 3 | CL6-01 (bloquant : borne lue à l'ouverture) et CL6-05 (R-796 (3) : aucun défaut sur les décisions de porte) | blocage mineur avant la fenêtre ou divergence non tranchée → grille non scellable ou « non franchie » mécanique | décision de Lazar faisant des dates des coupures de commits | VÉRIFIÉ (CL6-01, CL6-04, CL6-05) |
| D-G0-2 (critère 2 délégué à T0.6) | option 1, après correction CL6-08 | la grille ne fixe aucun seuil nouveau ; T0.6 passe M-0.2 à M-0.4 | conditions (a)-(d), non servies (SUPPOSÉ), trop faibles | (a)-(d) sans monotonie ni effet entre deux doses | VÉRIFIÉ ; (a)-(d) SUPPOSÉ, marqué |
| D-G0-3 (« tourne », T0.8) | option 1 | brief : « tourne », pas « détecte » ; seuil fixé par T0.8 avant le run | seuil de scores finis trop bas (50 %) laissé passer | part de scores finis < 95 % | VÉRIFIÉ ; seuils 50 % / 95 % SUPPOSÉ |
| D-G0-4 (décisions renvoyées, critères 6 et 7) | **option 2 (condition)** | Métrique : « pièce scellée à laquelle manque un contenu […] exigé » = invalide ; une réserve « ne change aucun état » | oubli mineur bloque G0 | décision listée devenue caduque | VÉRIFIÉ |
| D-G0-5 (garde P-007, T0.6 à T0.8) | **option 2 (invalide)** | preuves acquises hors du domaine de validité du harnais | oubli d'appel dans T0.8 invalide le critère 4 (boîte noire, SUPPOSÉ) | propriété invariante ou sans objet pour une tâche | VÉRIFIÉ (Métrique) ; lecture du « domaine » SUPPOSÉ |
| D-G0-6 (modèle, lignée du lecteur) | option 1 | N-052, choix 9 du repli ; « à défaut, signalé » évite un arrêt | même modèle si indisponibilité | si le lecteur interprétait : arrêt exigé | VÉRIFIÉ |
| D-G0-7 (version suivante) | option 1 (sous CL6-02, 03, 08) | option 2 « contraire à R-765 » ; précédent T0.4 v2-v3 | bogue découvert après verdict pendant le report : incorrigible | modification de R-765 par Lazar | VÉRIFIÉ |
| D-G0-8 + DIV-2 (verdict scellé, critères 1 à 5) | **option table / mémo G0-5 (a)** : verdict scellé pour 1 à 5, valeur copiée et classe (reco. visible) | « le lecteur compte, il n'analyse pas » ; compatibilité grille / table | réécriture de M-0.5, F-4.x, F-5.x et contre-lecture avant le 15 nov. | péril sur la date du 15 nov. | VÉRIFIÉ |
| D-G0-9 (critère 8, périmètre) | **option 2, (B) en condition** | brief : « aucun chiffre » ; réserve sans effet ; négatifs de 8 ne gèlent jamais | chiffre oublié dans un document (B) : « négatif » au 30 nov., sans gel | annexe E (non servie, SUPPOSÉ) incluant des brouillons figés | VÉRIFIÉ ; annexe E SUPPOSÉ, marqué |
| D-G0-10 (critère 5, « validés ») | option 1, avec la ligne ancrée de CL6-07 | plus mécanique qu'une ligne de synthèse | prédiction « non concluant » dans T0.3 met le critère en échec | table de T0.3 définissant le succès sur un sous-ensemble | VÉRIFIÉ |
| D-G0-11 (P4-instrument absent / postérieur) | option 1 (invalide) | ordre R1 rompu = invalide (M-0.4) | décalage d'horodatage administratif ; gel si D:5 (c) | rien ; maintenir « invalide ne gèle pas » (DIV-5) | VÉRIFIÉ |
| D-G0-12 (TRACE-lite absent) | **option 2 (absent)** | « lecture littérale du brief T0.8 » (annexe B) ; contenu exigé manquant | critère 4 échoue bien qu'un autre agrégateur tourne | décision de Lazar retirant TRACE-lite avant scellement | VÉRIFIÉ |
| D-G0-13 + DIV-1 (gel, portée au 30 nov.) | option 1 / DIV-1 (i) | concilie les deux volets de R-765 ; (ii) contredirait le précédent T0.4 | désalignement avec la table (L2bis) | mot de Lazar sur son intention dans R-765 | VÉRIFIÉ |
| D-G0-14 (négatif gelant, précédence, (c) (d) (e)) | **option nouvelle** : option 1 amendée par CL6-02, 03, 06, 07, 08, plus un point (f) ; DIV-5 : « invalide ne gèle pas », avec nœud si invalidité volontaire | cinq constats majeurs rendent la v7 défectueuse (faux gels, faux non concluants, brèche (m3)) | classe : contournement procédural du gel par invalidation volontaire d'une pièce (non détaillé ici) ; parade : gel lu sur l'artefact d'arrêt du run même sans verdict | essais sur artefacts de l'annexe G de la v8 | VÉRIFIÉ ; parade SUPPOSÉ |
| D-G0-15 + DIV-3 (reprise après arrêt) | **option nouvelle** : variante D:1 (a) de la table v7 (suspension bornée par l'heure du verdict ; « non franchie » faute de verdict), plus un traitement des trois causes sans ouverture | CL6-04 : défaut sans borne, contradictoire, table périmée | incident à 22 h le 31 janvier : « non franchie » ; atténué si coupure au 24 janvier | délai de grâce borné décidé par Lazar | VÉRIFIÉ ; règle pour les trois causes SUPPOSÉ |

**Liaisons et priorités** : bloc A (D-G0-1, 15, DIV-3), bloc B (D-G0-7, 11, 13, 14, DIV-1, DIV-5), bloc C (D-G0-8, 10, DIV-2), bloc D (D-G0-4, 5, 9, 12 : « condition » contre « réserve »). Trois premières : D-G0-1 (+15, DIV-3) ; D-G0-13 + 14 + DIV-1 ; D-G0-8 / DIV-2.

Argon répond à la question « un constat de CL6 change-t-il le sens d'une décision ? » pour chaque point : oui pour D-G0-1, 14, 15 (majeur), D-G0-8 (CL6-05), D-G0-13 (CL6-05), indirect pour D-G0-2, 7, 10, 11, aucun pour 3, 4, 5, 6, 9, 12.

### 2.2 Affirmations inexactes sur les faits servis (B)

Vingt renvois recoupés. Les chiffres cités (1/32 ≈ 0,031 absent ici ; dates du 30 novembre, 31 janvier, 15 novembre, 24 janvier ; N-010, N-011, T0.4 v2 et v3 ; R-765, R-750, R-796 (3) ; D:5 (c) ; « 1 536 combinaisons, 16 cas » non repris ; `M-0.5`, `F-4.x`, `F-5.x` ; `L2bis`) correspondent aux pièces. Je relève :

1. **D-G0-8** : « rédiger un verdict normalisé de plus pour les critères 4 et 5 ». DIV-2 dit que la grille exige déjà un verdict pour 2, 3, 4 (rapport de fonctionnement suffisant pour 4), lit 5 sur le code gelé et 1 sur sa série de verdicts ; la forme « valeur copiée et classe » toucherait aussi 1, 2, 3. Le coût est sous-décrit.
2. **D-G0-14, résumé de CL6-03** : « faisant basculer tous les négatifs par table dans la branche (e) indéterminée = gelant ». CL6-03 le dit pour un négatif par table à la première lecture ; la règle de transition de D-G0-14 (e) ne rend gelant que les verdicts scellés **après** la grille. « Tous » est trop large.
3. **D-G0-1** : Argon écrit que l'option 1 « omet de demander l'autorisation explicite de Lazar sur le mécanisme des défauts ». La grille demande un « mot explicite » sur D-G0-1 ; CL6-05 reproche qu'il ne dise pas « sur quoi ». Nuance : omission de précision, pas d'exigence.
4. **D-G0-9** : l'option 2 de l'annexe B est « (B) ou (C) en condition » ; Argon retient (B) sans dire ce qu'est (C) ni pourquoi il l'écarte (le périmètre (C) n'est pas servi).
5. **D-G0-12** : « similaire à N-029 citée l. 1249 » : N-029 porte sur le contenu de la base et le jeu d'épisodes (critère 4), pas sur un retrait de composant ; l'analogie est d'Argon.

Aucune erreur de chiffre trouvée dans B ; les écarts sont des élargissements de portée.

### 2.3 Options manquantes proposées par Argon (B)

- D-G0-1 réécrite sur le verdict (reprise de la correction CL6-01 (i)-(iv)).
- D-G0-14 (f) : (β) « oui » sans prononcé négatif → non concluant, non gelant (reprise de CL6-02) ; DIV-5 avec clause de nœud en cas d'invalidité volontaire ; une parade de gel lue sur l'artefact d'arrêt d'un run sans verdict.
- D-G0-15 : variante bornée de la table v7 complétée pour les trois causes sans ouverture (ouverture unique régularisée sur mot de Lazar, `C_lecture` au dernier commit avant l'échéance d'ouverture initiale).
- Bloc D nommé comme une seule « question de philosophie » (condition contre réserve), à trancher d'un coup.

### 2.4 Ce qu'Argon n'a pas traité (B)

- CL6-05 (c) : « jusque-là la grille garde son défaut » pour DIV-1 et DIV-2 est un défaut de plus ; Argon le mentionne pour D-G0-8 sans dire ce qu'il en fait pour DIV-1.
- CL6-01 (iii) : l'ambiguïté « ouverture ou verdict » pour la **première** lecture renvoie à N-027, que seule une décision de Lazar peut lire ; Argon tranche « verdict » pour les deux lectures sans distinguer ce qui relève de N-027.
- Le passage tronqué de CL6-01 dans l'extrait servi (ligne qui commence par « md\` l. 993 ») n'est pas signalé.
- La règle de transition (onze verdicts sans ligne de forme, annexe G) et son effet sur (e) : citée en passant, non examinée pour les preuves existantes.
- Les « onze autres choix » du repli (choix 2, 4 à 12) : hors question, non abordés ; mais Argon ne dit pas que ses choix D-G0-1 et D-G0-9 règlent aussi les choix 3 et 7 de la synthèse repli, comme la pièce l'indique.
- Le critère 4 lu « sur un rapport de fonctionnement » (grille) contre « verdict scellé » (table) : la conséquence pour une preuve T0.8 déjà existante n'est pas regardée.

---

## 3. Question C — bisociation, arène P-041 et le reste

### 3.1 Table des décisions (18 entrées ; décision 3 du tour 1 et divergence (a) du tour 2 regroupées par Argon)

| décision | option choisie par Argon | raison (une ligne) | pire cas donné | ce qui le ferait changer d'avis | statut |
|---|---|---|---|---|---|
| Q6, D1 (corriger la réponse en v2) | (a) v2 à deux niveaux | trois formules réfutées ; glissement iVAE (Q6-AFF-2) | rédaction inutile si l'Expérience 0 tue la thèse en quelques heures | Expérience 0 processeur franchit d'abord le critère de mort | VÉRIFIÉ |
| Q6, D2 (préenregistrer, générateur, devis) | (a) processeur d'abord, devis GPU ensuite | Q6-AFF-6 : banc non sur processeur (50 h, 192 h-GPU, « centaines d'heures ») ; X→U ~2 h CPU | plongements OpenAlex absents → devis GPU immédiat | constat d'absence des plongements | VÉRIFIÉ ; « (c) bloquerait la Q6 sur la Q7 » inexact (§ 3.2, n° 1) |
| Q6, D3 (courses de l'étape 2) | (a) exigence du préenregistrement | « sans cela aucune course ne sépare estimer d'identifier » ; puissance de B fausse (Q6-AFF-5) | taille d'échantillon prohibitive | devis au-delà du plafond : basculer sur (c), pas (b) | VÉRIFIÉ |
| Q6, D4 (relancer Kimi) | (a) relancer, 1 à 3 USD | deux lignées seulement ; complaisance possible de C ; 2 000–20 000 € jamais confrontés | nouvel échec technique | échec d'un test de connectivité ou indisponibilité > 24 h → (b) | VÉRIFIÉ ; « ping » SUPPOSÉ |
| Q7, D7-1 (critère de mort) | (i) Mort 0 à 3 de A + critère de B | confusion hypothèse / bisociateur ; (ii) trop étroite, (iii) garde la confusion | « non-jugeabilité » sauvant l'hypothèse | seuils Mort 0 / Morts 1-3 non exclusifs → (iii) | VÉRIFIÉ |
| Q7, D7-2 (porte de nécessité) | **(i) amendée** : dispositif de A + les deux comparateurs (A et B) en bras distincts | ablation placée en premier par les trois ; désaccord A/B sur le comparateur ; contrôles omis | test trop conservateur sur petit pilote | trivialité de RAF démontrée par la lecture des PDF → (ii) | VÉRIFIÉ |
| Q7, D7-3 (journalisation) | (i) champs complets | « la génération 2 ne tranche rien » sans eux ; coût nul | surcharge légère | champ exigeant des appels modèle supplémentaires | VÉRIFIÉ ; « coût nul » SUPPOSÉ |
| Q7, D7-4 (duel de dose) | (i) reporter à la question 3 | puissance insuffisante à 10 lots par dose ; C place la dose après Gate 0 et duel 2 | seuil d'allumage abrupt, dose fixe sous le seuil : faux négatif | porte et endogénéité réussies, Q3 sans protocole → (ii) | VÉRIFIÉ |
| Q7, D7-5 (dépense) | GO sur devis, plafond 35 USD, porte seule | 15 à 35 USD, modèles ouverts ; arrêt précoce | perte de 35 USD | devis > 100 USD, ou (ii) en D7-2 | VÉRIFIÉ ; seuil 100 SUPPOSÉ |
| P-041, déc. 3 + div. (a) (générateur informé) | (a) fait 9 tel quel ; scores à part, renvoyés à une question séparée (reco. visible) | N-053 (fait 4) ; « touche N-053 et N-056 » ; étanchéité | épreuve plus faible ; effondrement face à un générateur exploitant les scores (Bailey) | banc prouvant l'isolation d'un second run avec scores ; budget doublé | VÉRIFIÉ ; Bailey RAPPORTÉ |
| P-041, déc. 5 (budget) | (a) le préenregistrement le fixe, après le banc instrumental | (b) = écart à F7 et sans objet, tour 2 fini | K = 8 hors budget | rien | VÉRIFIÉ |
| div. (b) (réplications) | K = 8 paires (A, C) | B n'atteint 0,05 qu'en retirant Holm ; D double le coût ; 1/256 ≈ 0,004 | puissance insuffisante → « inconclus » | coût par paire (K = 6 ou K = 12–16) | VÉRIFIÉ ; « point d'équilibre exact » surdit (§ 3.2, n° 3) |
| div. (c) (estimand du débordement) | C-T3 (Δ_déb, signe négatif) + A-T3 en secondaire | seul estimand lié au certificat L | L non délivré → Δ_déb incalculable | c'est la raison du repli sur A-T3 | VÉRIFIÉ |
| div. (d) (arrêt anticipé) | C-T3 et D-T3 : arrêt sur invariants seulement, diagnostics consignés | arrêt dépendant des données biaise et brise la symétrie des paires ; A-T3 l. 106 | budget gaspillé après T/2 | boucles bloquantes : délai matériel, pas test statistique | VÉRIFIÉ ; argument de biais SUPPOSÉ |
| div. (e) (zone (0, δ)) | formulation unifiée : enjambement = « inconclus » ; inclusion stricte dans (0, δ_H) = « effet réel sous la marge » | divergence « en partie mal posée » : deux géométries | aucun | rien | VÉRIFIÉ |
| div. (f) (pilote) | simulation sur banc jouet, sans pilote réel | banc instrumental unanime ; lois HYPOTHÈSE (D) ; B, C | variance réelle plus grande → « inconclus » | banc sans information sur la variance → une paire sacrifiée | VÉRIFIÉ |
| Malléabilité, M_plafond | **règle structurelle** : plus grand d tel que terme de continuité ≤ 0,10 et grille × N_vérif dans le budget, **plafond absolu ≤ 9** | pièce 4 : « pour d_θ ≥ 10, certificat structurellement non délivrable » ; pièce 5 : M_max = d_camouflage | dès P-ML1a confirmée (≥ 10), nœud de redimensionnement systématique | abandon de la certification par grille → 32 ou 64 | SUPPOSÉ (identification d_θ = M_max, formule hybride) ; renvois VÉRIFIÉ |
| Malléabilité, couches | multiples de 4 (8 couches sur 32) | « multiples de 8 » n'en donne que 4 ; profil par couche et max sur les couches | temps doublé (120 contre 60 exécutions) | profilage d'une couche > 1/8 du budget → grille adaptative 4 + 2 | VÉRIFIÉ ; arithmétique SUPPOSÉ |

**Liaisons et priorités** : bloc « dimensionnement du certificat » (déc. 5, div. (b), (f), M_plafond) ; bloc « régime informé » (déc. 3 / (a), (c), (d)) ; bloc « porte de la question 7 » (D7-1 à D7-5) ; bloc « préconditions de la question 6 » (D1, D2). Trois premières : D4 (Kimi) ; D7-2 / D7-5 (+ D7-3) ; banc instrumental P-041 + déc. 5 + (f) + M_plafond.

Note sur la pièce 5 : le protocole servi décrit un procédé d'optimisation d'entrées adverses contre un moniteur figé (classe seulement ; non reproduit ici). Argon en reprend les paramètres dans son pire cas (5 graines × 3 seuils) sans en ajouter.

### 3.2 Affirmations inexactes sur les faits servis (C)

Vingt-deux chiffres et renvois recoupés : 50 h, 192 h-GPU, 400 €, ~2 h CPU, 2 000–20 000 €, ~200 $, 1 650–2 300 €, 1 à 3 USD, 30–35 et 15–30 USD, K = 8, 2^8 = 256, ≈ 0,004, 1/32 ≈ 0,031, 16 + 4 = 36, L_Lip·h > 0,10, d_θ ≥ 10, N_vérif = 50 000, N_min = 10, 8 couches sur 32, p. 13 de Bailey, A-T3 l. 34 / 49 / 56–58 / 70 / 78–83 / 87 / 99–101 / 106 / 112–125, B-T3 l. 67 / 127–137, C-T3 l. 8 / 10 / 38 / 44 / 62 / 88–96, D-T3 l. 70 / 107 / 116–117. Tous exacts. Inexacts :

1. **D2** : « Attendre G0 (c) bloquerait inutilement la Question 6 sur la Question 7 ». L'option (c) de D2 renvoie à la porte G0 du programme ; la « porte G0 » de la question 7 (D7-2, D7-5) est un autre objet portant le même nom. Argon confond les deux.
2. **M_plafond** : « règle de délivrabilité de A-T3 l. 70 et C-T3 l. 10 » pour « L_Lip · h · √d / 2 ≤ 0,10 ». La pièce 4 donne deux formules distinctes : A-T3 « K·h·√d_θ/2 » (terme du certificat) et C-T3 « L_Lip·h > 0,10 → non délivré ». La formule hybride n'est dans aucune cellule.
3. **div. (b)** : « K = 8 est le point d'équilibre exact mentionné dans le noyau consensuel ». Le noyau dit « K ≥ 8 (illustratif) ».
4. **M_plafond** : l'égalité d_θ = d_camouflage = M_max est posée comme lue dans la pièce 5 ; la pièce 5 dit que M_max est versé au générateur « comme dimension de camouflage » pour dimensionner ses familles ; que la grille du certificat ait d_θ pour dimension n'est écrit nulle part dans les faits servis.
5. **D7-2** : « dispositif complet de A (remplacement iso-longueur + seconde famille de modèles) » : D7-2 (i) dit « iso-longueur + apparié en pertinence + seconde famille » ; Argon omet l'appariement en pertinence dans la parenthèse, puis le réintroduit comme comparateur ; « de modèles » n'est pas dans la pièce.
6. **div. (f)** : « convergence B, C et D-T3 » : la pièce dit « non résolu » et range A d'un côté (pilote puis décisif), D d'un autre (scénarios), B et C ensemble ; appeler cela une convergence est une lecture d'Argon.

### 3.3 Options manquantes proposées par Argon (C)

- D7-2 : les deux comparateurs de spécificité (fiche appariée en pertinence hors lignée ; fiche aléatoire du lot) en bras distincts dès la génération 1.
- div. (c) : estimand de C-T3 en principal, celui d'A-T3 en repli préenregistré si le certificat n'est pas délivré.
- div. (e) : vocabulaire unifié « enjambement » / « inclusion stricte ».
- div. (f) : une paire d'étalonnage sacrifiée, exclue des K paires, si le banc jouet n'informe pas la variance.
- M_plafond : règle structurelle plutôt que valeur ; plafond ≤ 9 ; valeurs 32 ou 64 si la certification change de méthode.
- Couches : grille adaptative en deux temps (multiples de 8, puis deux multiples de 4 autour du maximum).
- D4 : test de connectivité à coût quasi nul avant la relance.

### 3.4 Ce qu'Argon n'a pas traité (C)

- Pièce 4, § 6, réserve R4 « trop propre » (quatre héritages positifs, quatre x = 0,80, quatre transferts « positifs mais dégradés ») : non mentionnée, alors qu'elle pèse sur la lecture de la convergence du tour 2.
- Pièce 4, § 6 : rédacteur de la même famille que B ; contre-lecture non faite ; familles tierces RAPPORTÉ (fait 10) : non mentionnés.
- Pièce 3, décision 4 (où instruire les voies (ii), (iii) et l'examen final) est déclarée « exécutée ou dépassée » par la question ; Argon y renvoie pourtant dans sa décision 3 (« question séparée avec les voies (ii) et (iii) »), c'est-à-dire prend position sur l'option (a) d'une décision hors liste.
- Pièce 2, réserve « la convergence peut refléter la formulation de la question (R8) » et « deux espèces sur trois de la même lignée » : non pesées dans D7-1, où Argon reconnaît l'appui d'une seule lignée mais tranche quand même.
- Pièce 1, réserve « les établis sont des théorèmes rapportés de mémoire, jamais lus sur PDF » : pas de conséquence tirée pour D1.
- Pièce 5 : la valeur de N_min (10, illustratif), δ_min, ε = 0,05, le nombre de graines (5, CL-M6) : hors question, non commentés ; en revanche l'incohérence « multiples de 4 ou 8, soit environ 8 couches » est relevée par Argon.
- La divergence (b) et le budget (déc. 5) sont liés par Argon, mais le coût par réplication n'est chiffré par aucune pièce ni par Argon.

---

## 4. Bilan des recoupements

- Chiffres ou renvois recoupés : A 34, B 20, C 22, soit 76.
- Inexacts ou mal attribués : A 7 (dont 2 erreurs de chiffre : S10 et D-g ; 5 de portée ou de statut), B 5 (tous de portée), C 6 (dont 1 confusion d'objet, 2 formules ou égalités non servies, 3 de portée). Total 18.
- Aucune pièce inventée. Aucun chiffre hors des faits présenté comme servi, sauf la formule hybride de M_plafond et les versions de debian-13 présentées comme acquises. Les marqueurs SUPPOSÉ demandés par la consigne sont posés par Argon sur les conditions (a)-(d) de D-G0-2, l'annexe E de D-G0-9 et un point de D-G0-5 ; ils manquent sur les calculs propres (0,004 ; 0,13 ; « 8 sur 24 » ; 120 contre 60), sur les seuils propres (15 %, 50 paires, 200 entrées, 80 %, 100 USD, 95 %) et sur les versions de debian-13.

## 5. Points où Argon s'écarte le plus de ce que les faits laissaient attendre

1. **Tableau partagé, décision 1 (A)** : la pièce 3 dit que (a) « course 2 figée » est la position de A seule (1 sur 4) et (b) celle de B, C, D ; sa réserve note que l'unanimité sur le défaut est en partie construite. Argon choisit (a), invente l'option (d) « aucun bras » pour la décision 3, et appuie le tout sur une inférence non servie (la batterie du tableau « non couverte par les 160 USD »). Les décisions 2 et 3 deviennent sans objet par ce seul choix.
2. **Porte G0, bloc « condition contre réserve » (B)** : sur les quatre points où la grille proposait « réserve » (D-G0-4, 5, 12, et (B) en réserve pour D-G0-9), Argon choisit systématiquement la condition bloquante ; sur DIV-2 il choisit la forme de la table contre la grille. C'est la lecture la plus sévère possible de la porte, cohérente avec la Métrique servie mais contraire au défaut de la grille sur chacun de ces points.
3. **Machine jetable (A)** : l'auteur demandait l'accord sur l'écart d'hôte (R-a) ; Argon le refuse en premier choix et fait passer en tête `debian-13` puis (R-b), sur des versions que la pièce marque SUPPOSÉ ; il ajoute la clé d'hôte jetable que la pièce laissait à Lazar.
4. **M_plafond (C)** : là où la question demandait « valeur et règle », Argon dérive une borne dure (≤ 9) en identifiant la dimension du certificat de P-041 à la malléabilité mesurée, identification que les faits ne font pas ; sous cette règle, toute confirmation de P-ML1a (N_min = 10) ouvre aussitôt le nœud de redimensionnement, ce qu'Argon reconnaît comme pire cas.
5. Plus petit mais net : **texte III, décision 2**, Argon retient (c), option de D seul, contre (a) choisie par trois modèles sur quatre, sur l'argument « aucun intervalle établi » ; et **S18** est le seul seuil où Argon quitte la valeur proposée (0,70 → 0,75), au nom du bruit sur C5. Enfin la **priorité 1 de C** est donnée à D4 (relance de Kimi, 1 à 3 USD, déjà échouée une fois), ce que l'enjeu des pièces ne laissait pas attendre.

Pour mémoire : sur D-g, D-h, D-i, D-j, L1 à L7, D-G0-8, D-G0-15 et la décision 3 / divergence (a) de P-041, l'accord d'Argon avec les positions d'auteur restées visibles dans les faits servis ne renseigne pas sur son indépendance.

Fin de la lecture. Aucune recommandation.
