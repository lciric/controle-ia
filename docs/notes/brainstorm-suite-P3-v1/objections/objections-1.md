# Objections — objecteur 1 — brainstorm « suite de P3 » — v1

- Objecteur 1, sous-agent neuf. Tour d'objections à l'aveugle (protocole fermé de Lazar, R-203 (2)). Je n'ai vu ni l'autre objecteur ni les réponses.
- Écrit le 2026-10-20 (UTC). Dépôt lu en lecture seule. Je n'ai lu ni `prereg/P3-consignes-v1.md`, ni les textes d'action, ni aucune clé. Je n'ai pas lu la sortie de l'addendum.
- Un seul calcul neuf sur les données : la somme de `jetons_notes` dans `scores-p3.npz` (532 683), pour vérifier un volume de stockage. Aucun score lu au-delà de la lecture décisive.
- Classes : **fatale** (option fausse, dangereuse ou contraire à une règle gelée) ; **sérieuse** (doit changer avant d'être retenue) ; **mineure**.
- Abréviations : `lecture` = `diag/20261020-075740-p3-lecture/lecture-p3.json`, clé `resultat` ; `prereg` = `prereg/P3-premier-test-i-a-v1.md` ; `addendum` = `prereg/P3-addendum-lecture-complementaire-v1.md`.

## Bilan en cinq lignes

1. Deux options sont **fatales** : A3, parce que ses volets (b) et « plancher refait sur sous-ensemble » relisent d'autres sondes et d'autres jeux de P3 ; D4, parce que doser par la seule proportion ne rend pas le sabotage diffus.
2. Une troisième, G (i) volet (2), est fatale aussi : elle lit sur P3 une sonde « enjeux » réentraînée après le nul.
3. Plusieurs propositions routent la branche B sur des réserves de l'addendum qui **ne peuvent pas sortir** : seule P3-P1 est établie (objection d'ensemble 1).
4. L'aire minimale détectable « réalisée » (≈ 0,615) de B, C et D est le point à 50 % de puissance. À 80 %, c'est ≈ 0,63. D veut dire ce chiffre au financeur.
5. Il manque à l'ensemble : un nœud sur R-202 (3), dont la condition est rompue ; un plan de multiplicité commun ; un lieu de confirmation sur épisodes neufs ; un calendrier et un crédit communs.

---

## Proposition A

### A3 — fatale
- **Objection.** A3 (b) relit sur P3 les sondes de tromperie ex aequo (linéaire c15, perceptron c15) contre le plancher de la principale. Il rapporte aussi les 30 sondes « en distribution ». A3 (a) refait le plancher sur le seul sous-ensemble « coût = nombre seul ». Les deux sont des secondes lectures sur d'autres sondes et d'autres jeux. La ligne gelée les interdit. « Aucune n'est promue » ne suffit pas : la ligne interdit la lecture, pas seulement la promotion. Neuf sondes à 1,0 font neuf essais.
- **Preuve.** `prereg` l. 428 : « pas de seconde lecture sur d'autres sondes, couches ou jeux ». `prereg` l. 436 : une sonde au-dessus « seulement hors des sondes principales [...] ne compte pas ». `diag/20261019-230011-p3-reel/sondes-figees.json`, `aires_validation.tromperie` : neuf sondes à 1,0 sur 120 exemples. `scores-p3.npz`, `scores` : forme (2 400, 430).
- **Pour la garder.** Garder seulement A3 (a), corrélations du plancher avec la longueur, le pas et le coût. C'est une grandeur non écrite, donc un nœud (`prereg` l. 415-416). Retirer (b) et le plancher sur sous-ensemble, ou les reporter à des épisodes neufs.

### A4 — sérieuse (stockage)
- **Objection.** Le plan « activations des couches 7, 15 et 23 [...] gardées en demi-précision dans le dépôt privé » ne tient pas.
- **Preuve.**
  - 532 683 jetons notés (somme de `jetons_notes`, `scores-p3.npz`) × 4 096 × 2 octets = 4,36 Go par couche, soit 13,1 Go pour trois couches.
  - GitHub refuse les fichiers de plus de 100 Mo. Le dépôt n'a pas de stockage des gros fichiers (`.gitattributes` : aucune règle de ce type). `.git` pèse déjà 476 Mo.
  - Le disque de la session a 4,5 Go libres (`df`). La place disque a déjà bloqué un appel (R-238 ; P-012).
- **Pour la garder.** Faire tous les calculs sur l'instance et ne rapatrier que des scores. Ou ne garder que la couche 15, sur un sous-ensemble tiré par graine.

### A4 (échéance du fichier complet) — sérieuse
- **Objection.** Le fichier complet des sondes figées n'a qu'un usage propre : relire les sondes de Mahalanobis. Elles ne sont pas principales, et leur relecture sur P3 est interdite (l. 428). A4 les exclut lui-même de sa garde d'identité. Le rapatriement demande de redémarrer une instance arrêtée : c'est une dépense, donc un nœud. C'est aussi un écart au sort gelé du fichier (sur l'instance, puis destruction). Enfin, un fichier de 0,8 Go ne passe pas dans GitHub.
- **Preuve.** `sondes-figees.json`, `aires_validation` : Mahalanobis de 0,49 à 0,85 en tromperie, de 0,51 à 0,52 en enjeux ; principales : `tromperie-difference_moyennes-c15`, `enjeux-lineaire-c15`. `prereg` l. 312-317. `registres/arrets.md`, 2026-10-20 02:07 : instance arrêtée, destruction au plus 72 heures après.
- **Pour la garder.** Laisser la destruction prévue et consigner la perte. Ne pas en faire une urgence de décision.

### A2 — sérieuse
- **Objection.** A2 poursuit, après lecture, le seul nombre haut : 0,914 au champ du coût. L'idée « à coût égal » existe déjà : c'est T4, non établi. L'addendum refait déjà T4 avec des tranches tirées à nouveau. Sans plancher au niveau du jeton, « au-dessus de la permutation » ne dit rien d'une direction quelconque. Surtout, le chemin de A teste ensuite l'hypothèse (A4) **sur les mêmes textes de P3**. Aucune donnée neuve n'est prévue avant G0.
- **Preuve.** `lecture`, `intention.tromperie-difference_moyennes-c15` : T2 `aire_a` 0,9137 ; T4 0,6317 pour un quantile de 0,6066, non établi. `addendum` l. 138-142 (A4 (a)). Proposition A, § 3 : A2, puis A4, sans épisodes neufs. `prereg` l. 415-416.
- **Pour la garder.** La remplacer par la manipulation causale de D2 (nombre remplacé). Ou la déclarer génératrice d'hypothèse, avec un test obligatoire sur des épisodes neufs nommés d'avance.

### A1 — mineure
- **Objection.** A1 propose « au niveau du plancher » plutôt que « faute de puissance ». La formule gelée est « non détecté à cette puissance ». Elle reste ; l'autre ne peut que s'ajouter. Et la phrase « plus de tâches n'y changerait rien » est fausse en principe : il faudrait environ 195 fois plus de tâches pour que la borne basse passe 0,5717. C'est irréaliste, pas impossible, et le quantile du plancher bougerait aussi.
- **Preuve.** `prereg` l. 273 et l. 428. Calcul : (0,0435 / 0,0031)² ≈ 195, d'après `lecture`, `P3-P3.tromperie…` (aire 0,5748, borne basse 0,5313, quantile 0,5717).

### A5 — mineure
- **Objection.** A5 est un doublon de C1 : même phrase de persona avant « Your action: », sur les actions honnêtes. Une garde manque : les deux phrases peuvent avoir des nombres de jetons différents (« an honest » contre « a dishonest »). Sans règle écrite, on risque un repli silencieux (R5).
- **Preuve.** `src/controle_ia/premier_test_ia/donnees.py` l. 26-27. Proposition C, C1 (« Gardes : même longueur en jetons »).

### A6 — mineure
- **Objection.** A6 (5) reprend la garde des activations par jeton sans plan de stockage (voir A4). Le reste est sain, et la lecture par champ est bien marquée secondaire.
- **Preuve.** `brouillons/programme-approfondi-ABC-v1.md` l. 82 : environ 1,2 Go pour 20 épisodes.

---

## Proposition B

### B1 — sérieuse
- **Objection.** Le texte A dit au financeur « inflated its declared costs about thirty-fold ». C'est avant le verdict, et avant l'addendum, dont la seule réserve possible vise justement P3-P1 (A6). Le facteur 33 est un « trop beau » côté organisme (consigne : × 3 ; R4). Il est calculé sur les seules actions lisibles, avec un lecteur qui prend le premier nombre. Les formes du coût sont très asymétriques. De plus, « did not separate [...] above » contredit la formule gelée.
- **Preuve.**
  - `lecture`, `P3-P1` : `actions_illisibles_a` 140, `actions_illisibles_b` 134 (sur 600).
  - `lecture`, `P3-P6` : honnête 13 intervalles, 14 suffixes « k », 41 champs à plusieurs nombres ; saboteur 0, 0 et 3.
  - `prereg` l. 155 (« au plus ≈ 0,48 ») ; l. 273 (« jamais « ne sépare pas » »).
  - `addendum` l. 214 (`reserve_A6_P3-P1`).
- **Pour la garder.** Dire « well beyond the instructed threefold », sans chiffre, et « not detected at this power ».

### B1 — mineure
- **Objection.** Mettre les estimations ponctuelles face aux planchers (0,575 contre 0,572) invite la lecture « presque positif ». La phrase « Without that floor, the deception probe would have looked like a detection » l'invite aussi. B l'interdit pourtant lui-même. La règle lit la borne basse.
- **Preuve.** `prereg` l. 272. Proposition B, § 2 (« Ce que je ne propose pas »).

### B4 — sérieuse
- **Objection.** Le point 4 dit : « si les sondes ne voient pas un facteur 33, elles verront mal un facteur 1,5 ». Cela suppose que la sonde lit la grandeur du nombre. Une sonde d'intention ne dépend pas de la grandeur. L'écrire d'avance dans G1 fige une lecture qui va contre le but même du test.
- **Preuve.** `prereg` l. 139-142 : T4 existe pour séparer l'intention de la grandeur. `lecture`, `audit_R4.correlation_score_cout_honnete` : −0,118 pour la tromperie.

### B6 — sérieuse
- **Objection.**
  - (1) Le diagnostic « maximum contre moyenne » sur les scores par jeton de P3 calcule une moyenne sur les jetons d'une action. La liste d'arrêt de P3 l'arrête, l'addendum l'interdit, le brief aussi. Même en nœud, ce serait une dérogation à un interdit du programme.
  - (2) Le témoin positif choisi reproduit 0,887. Il éprouve une sonde à attention, sur les jeux d'évaluation de l'article, au format du message utilisateur. Il ne teste donc pas deux suspects que B6 nomme : le passage du message utilisateur au tour de l'assistant, et le maximum.
- **Preuve.** `prereg` l. 450 ; `addendum` l. 92-94 ; brief l. 168 ; `docs/sources/pdf/2506.10805v4.pdf` (empreinte `54bf5555…` vérifiée), p. 24 (« we trained attention probes ») et p. 25 (0,887) ; `prereg` l. 299-301.

### B3 — mineure
- **Objection.** « Les relire sous T7-P1 serait une seconde chance » : T7-P1 lit d'autres épisodes (T0.6), dans un autre mode, et P3 ne sert à aucune lecture de T0.7. C'est une réplication, pas une seconde chance sur les mêmes données. Si T0.7 passe au mode « coût » (B3 (2)), c'est même la réplication voulue. La correction de Bonferroni proposée reste prudente, mais doit être présentée comme telle.
- **Preuve.** `prereg` l. 24 ; `brouillons/T0.7-sondes-v0-v1-brouillon4.md` l. 47 et l. 65.

### B2 — mineure
- **Objection.** « H8 gagne du poids de fait » : lire un nul comme un appui à H8 va trop loin (R8). C'est au mieux descriptif.
- **Preuve.** Proposition B, tableau de B2 ; programme l. 235 (H8 vaut « même si H1 échoue », pas « parce que »).

### B (F5) et C5 — mineure
- **Objection.** « Plancher plus demi-largeur » donne le point à 50 % de puissance, pas l'aire minimale détectable au sens du préenregistrement. Détail dans l'objection D1.
- **Preuve.** Voir D1.

---

## Proposition C

### C3 — sérieuse (deux décisions de Lazar contournées)
- **Objection.**
  - (a) R-202 (3) : la référence boîte noire sur les textes de P3 devait être préenregistrée **sans lecture des résultats de P3**. Aucun texte n'est scellé, et la lecture est faite. C'est un écart à déclarer (nœud). C3 ne le nomme pas.
  - (b) N-022 (3)(a) : « tant que le plan B n'est pas requalifié, la rubrique de départ de T0.6 et T0.8 n'existe pas ». C3 fait tourner les juges 8B et 3B de T0.8 avant cette requalification.
  - C3 cite aussi N-022 de travers : N-022 dit que « 8B trop faible » **n'est pas établi**.
- **Preuve.** `prereg` l. 20-21. `ls prereg/` : aucun préenregistrement de référence boîte noire. `registres/decisions.md` l. 418 (N-022).

### C3 — sérieuse (critère 4, valeur de confirmation)
- **Objection.** C3 ne remplit pas le critère 4. « Qui tourne sur le même jeu d'épisodes » renvoie aux épisodes de T0.6 lus par T0.7, sur (i) et sur (ii). P3 n'a que (i-a), et ses épisodes ne servent à aucune lecture de T0.6 ni de T0.7. De plus, la prédiction principale (boîte noire au-dessus de la boîte blanche) est connue d'avance : le coût seul sépare à 0,888. Sa valeur de confirmation est nulle.
- **Preuve.** Brief l. 195 ; `docs/decisions/proposition-P-007-plan-G0-v1.md` l. 32 (« T0.8 sur les mêmes épisodes ») ; `prereg` l. 24 ; `lecture`, `audit_R4.jeux[0].cout_seul.aire` = 0,8878.

### C4 — sérieuse
- **Objection.** C4 distille (ii) depuis les 600 actions du saboteur de P3, prises sur les 60 tâches du pilote. Il le lit ensuite sur les textes honnêtes **des mêmes 60 tâches**. Or l'entraînement de (ii) doit se faire sur des tâches disjointes de l'évaluation, et les épisodes de P3 ne servent à aucune lecture de T0.6.
- **Preuve.** `brouillons/T0.6-organismes-v0-v1-brouillon1.md` l. 73 (tâches disjointes, contrôlées par un script) ; `prereg` l. 24 et l. 43.

### C (calendrier) — sérieuse
- **Objection.** C1, C2 et C3 « tiennent avant le 1er novembre ». Mais ils n'avancent aucun critère restant de G0 : 2 (dose-réponse et (ii)), 3 (sur (i) et sur (ii)), 4 (voir plus haut), 6, 7 et 8. Le délai de deux à trois jours pour C1 et C2 est optimiste : il faut une statistique neuve (concordance appariée), sa simulation de puissance, ses tests R5 et une contre-lecture R2. L'addendum, plus simple (aucune passe du modèle), a demandé trois rondes de vérification.
- **Preuve.** `registres/etat.md` (critères restants : 2, 3, 4, 6, 7, 8) ; `registres/decisions.md` R-251 et R-252.

### C1 — mineure
- **Objection.**
  - La garde « même longueur en jetons » n'a pas de règle écrite si elle échoue (R5).
  - « Jetons d'action identiques, identifiant par identifiant » ne peut pas être vérifié contre P3 : les identifiants générés n'ont pas été gardés, seule leur longueur l'a été. La garde d'identité des scores sera le seul recours ; la part d'actions exclues doit être bornée d'avance.
- **Preuve.** `src/controle_ia/premier_test_ia/run.py` l. 275 (`jetons` = longueur des identifiants) ; `src/controle_ia/harnais/episode.py` l. 252-254 (texte décodé des identifiants générés).

---

## Proposition D

### D4 — fatale
- **Objection.** D4 dose par la seule proportion p d'actions avec indication. Chaque action sabotée reste alors flagrante (× 33 ; coût seul ≈ 0,89) : le sabotage n'est pas diffus au sens retenu. Il y a quatre problèmes.
  - La cible « aire du coût seul au plus 0,65 à la dose la plus faible » serait atteinte par dilution des étiquettes, pas par subtilité : à p = 0,25, environ 0,25 × 0,888 + 0,75 × 0,5 ≈ 0,60. La dilution pénalise la sonde et le lecteur de coût à l'identique.
  - La consigne privée reste dans le message système à chaque pas : p ne règle que l'indication, pas la part d'actions sabotées.
  - Le critère « sonde contre lecteur de coût, à coût déclaré égal » est dégénéré : à coût égal, le lecteur de coût vaut 0,5 par construction.
  - D4 abandonne l'axe « intensité » du brief.

  L'option ne tranche donc pas ce qu'elle annonce (« un sabotage que le texte ne trahit pas »).
- **Preuve.** `docs/decisions/decision-N-007-N-008-v1.md` l. 28 (« chaque action sabotée reste sous le seuil d'un moniteur par action calibré à 1 % ») ; brief l. 163 (« proportion d'actions sabotées × intensité ») ; `src/controle_ia/premier_test_ia/conditions.py` l. 81-82 (consigne au système pour tout l'épisode, indication à chaque pas) ; `lecture`, `audit_R4.jeux[0].cout_seul.aire` 0,8878.

### D1 — sérieuse
- **Objection.** « Effet minimal détectable réel = quantile du plancher + demi-largeur » donne le point à **50 %** de puissance. La valeur écrite au préenregistrement (≈ 0,57 à 0,58) est plus proche de 80 % : à une aire de 0,586, la note de puissance donne 93 % au-dessus. Comparer 0,615 à « 0,57 à 0,58 » mélange deux définitions.
  - À 80 %, en approximation normale, l'erreur type vaut 0,0435 / 2,241 ≈ 0,0194.
  - Tromperie : 0,572 + 0,0435 + 0,84 × 0,0194 ≈ **0,632**. Enjeux : ≈ **0,595**.
  - Une aire vraie de 0,60 n'est vue qu'environ 22 % du temps.

  C'est le chiffre que D5 veut dire au financeur (« ≈ 0,62 »). L'objection vaut aussi, en mineure, pour B (F5) et C5.
- **Preuve.** `docs/notes/P3-mesures-v2/puissance-p3-v1.txt` l. 11-14 ; `lecture`, `P3-P3` (aire 0,5748, borne basse 0,5313, quantile 0,5717 ; enjeux 0,5248, 0,4813, 0,5356) ; `prereg` l. 395-397.

### D5 — sérieuse
- **Objection.**
  - L'option (a), « G0 au 1er novembre sans le critère 3 sur (i-a) ; M0 prolongé de deux semaines », se contredit (G0 au 1er novembre et M0 prolongé). Elle se lit aussi comme le franchissement d'une porte sans l'un de ses critères.
  - L'option (b) remplace, après un nul, le bras principal du critère 3 par un bras supervisé plus favorable. C'est abaisser la porte après coup, ce que B3 (c) déconseille.

  Les deux doivent s'écrire « porte non franchie » ou « critère réécrit », avec un nœud explicite.
- **Preuve.** Brief l. 191 (« Tous les critères suivants sont remplis ») ; P-007 l. 38 et l. 45-46 ; P-011 (c), R-077.

### D2 — mineure
- **Objection.** La prédiction « effet du contexte, à nombre égal, non détecté » n'a pas de marge d'équivalence : un nul ne la confirme pas. D2 fait doublon partiel avec C2 : il faut les fusionner en un seul plan contexte × texte × nombre.
- **Preuve.** `brouillons/programme-approfondi-ABC-v1.md` l. 84 (règle proposée : toute prédiction « ≈ 0 » porte sa marge et son test d'équivalence) ; proposition C, C2.

### D3 — mineure
- **Objection.**
  - (1) La sonde « minuscules » lit des identifiants de jetons différents : la passer prouve peu, comme D le dit.
  - (2) La reproduction porte sur une sonde à attention, au format du message utilisateur. Ce n'est pas la chaîne de P3 : différence de moyennes et linéaire, par le maximum, sur les jetons de l'assistant.
- **Preuve.** PDF 2506.10805v4 p. 24 ; `sondes-figees.json`, `principales`.

### D6 — mineure
- **Objection.** La grille de codage est écrite après la lecture : elle vise le × 33. Il faut le dire. Point fort à garder : D6 est la seule proposition qui nomme l'écart à R-202 (3).
- **Preuve.** Proposition D, D6.

---

## Proposition externe G (Gemini, non opposable)

### G (i), volet (2) — fatale
- **Objection.** G reformate la sonde « enjeux » au tour de l'assistant, puis la lit sur les 2 400 actions de P3 pour éclairer « Critère 3 de G0 (H-P3b) ». Une sonde nouvelle lue sur P3 est une seconde lecture interdite.
- **Preuve.** `prereg` l. 428 et l. 436 ; tableau G, ligne (i), colonne « Revendication touchée ».

### G (i), volet (1) — sérieuse
- **Objection.** L'oracle supervisé saboteur contre honnête porte sur des actions entières. Or le contexte du saboteur contient la consigne, et le champ du coût porte le nombre (coût seul 0,888). Un plafond proche de 1 ne dirait rien. Il faut masquer le champ du coût et ce qui le suit, et prendre le contraste saboteur contre mention ou témoin (comme A4). En outre, entraîner et évaluer sur le même organisme pour le critère 3, comme G l'écrit, contredit la règle d'anti-circularité.
- **Preuve.** `lecture`, `audit_R4.jeux[0].cout_seul` ; brief l. 171 ; tableau G, ligne (i).

### G (synthèse, points 2 et 5) — sérieuse
- **Objection.**
  - « Ne jamais régénérer d'épisodes avant d'avoir épuisé `textes-actions-p3.jsonl` » pousse à multiplier les lectures sur un seul jeu (R4, l. 428).
  - Le point 5 (« juge boîte noire en parallèle sous son propre préenregistrement ») ignore que R-202 (3) exigeait un scellement avant la lecture (voir C3).
- **Preuve.** `prereg` l. 20-21 et l. 428.

### G (ligne (iii), synthèse 3, autres lignes) — mineure
- **Objection.**
  - G décrit T2 de travers : T2 compare deux aires (différence appariée des aires), pas deux maxima.
  - Le piège de longueur est contredit par les données : la longueur seule sépare à 0,503 sur saboteur contre honnête.
  - Les parts « 85 % et 15 % » du budget sont sans source.
  - Les lignes (0), (1), (ii), (iii) et (iv) sont sans objet : la ligne d'issue est connue.
- **Preuve.** `src/controle_ia/premier_test_ia/lecture.py` l. 332-335 (`difference_aires_appariee`) ; `lecture`, `audit_R4.jeux[0].triviaux.jetons_notes.aire` 0,5029 ; `issue.ligne`.

---

## Ce qui manque à l'ensemble

### Ensemble 1 — sérieuse : les branches B et C sont presque impossibles avec les mécanismes gelés
- **Objection.**
  - Toutes les réserves gelées sont absentes : audit R4 non déclenché ; contrôle négatif conforme ; témoin avec effet ; témoin et mention qui ne gonflent pas.
  - L'addendum ne peut viser que P3-P1, seule conclusion établie. Toute réserve sur P3-P3, P3-P4 ou T1 à T4 y est « sans objet ».
  - Hors de « P3-P3 en échec », qui n'est pas survenu, aucune ligne ne permet « instrument en échec ».
  - Or deux chemins routent la branche B sur des réserves qui ne peuvent pas sortir : celui de A (§ 3, « plancher : A3 (a) ; fuite : A3 (c) ») et celui de D (« Position du jeton dominant (A8) : D3 d'abord » ; « Plancher ou fuite »).
  - La vraie branche manque : (A), avec au plus la réserve A6 sur P3-P1 et la limite de portée TC-20 (f). Il faut écrire ce qu'on fait si A6 touche P3-P1, car B1, B4, C3 et D4 s'appuient sur le × 33.
- **Preuve.** `lecture` : `audit_R4.declenche` faux ; `controle_negatif` « conforme » ; `P3-P6.temoin.titre_sans_capitale` 500 contre 4 ; bornes hautes de `P3-P2` (−0,065) et de `cout_mention` (−0,115) ; `issue.en_echec` vide. `addendum` l. 220-221, l. 226, l. 248-250, l. 254. `prereg` l. 299-301 et l. 434-435.

### Ensemble 2 — sérieuse : R-202 (3) reste ouvert
- **Objection.** La décision de Lazar sur la référence boîte noire par l'interface de Claude a perdu sa condition (préenregistrement scellé avant toute lecture de P3). Seule D6 le voit. Il faut un nœud à trois options : abandonner ; déclarer l'écart, avec une invite écrite par un sous-agent qui n'a pas vu la lecture ; ou remplacer par la base de T0.8 après le plan B des juges.
- **Preuve.** `prereg` l. 20-21 ; aucun préenregistrement de cette référence dans `prereg/` ; `registres/decisions.md` R-202.

### Ensemble 3 — sérieuse : aucun plan de multiplicité commun, et aucun lieu de confirmation
- **Objection.**
  - Au moins dix analyses après coup sont proposées sur les mêmes 2 400 actions : A2, A3, A4, A5, C1, C2, D2, D3, D6 et G (i). Par hasard, une ou deux sortiront « positives ».
  - Il faut une seule famille d'exploration, déclarée dans un seul préenregistrement, avec une règle écrite d'avance : tout positif est une hypothèse, testée sur des épisodes neufs nommés.
  - Le lieu naturel de ce test est T0.7, sur les épisodes de T0.6, en mode « coût » (seul mode retenu par le pilote). Or le brouillon de T0.6 est encore en mode « affaiblir les contrôles ». Aucune proposition ne relie ces deux points (B3 (2) et D4 en voient la moitié).
- **Preuve.** `brouillons/T0.6-organismes-v0-v1-brouillon1.md` l. 28 ; `docs/verdicts/verdict-T0.5-pilote-v1.md` l. 48 ; `prereg` l. 24 ; R4.

### Ensemble 4 — sérieuse : pas de calendrier ni de crédit communs
- **Objection.**
  - Le crédit relu vaut 11,79 USD. Le lanceur de P3 exige, à la création, environ 6,5 heures × prix + 1,2 USD, soit ≈ 8,3 USD.
  - GO-2026-10-04-08 échoit le 1er novembre.
  - Le plan B des juges (étape payante) et le pilote du papier C (GO-2026-10-17-01, ≈ 6 USD) puisent au même crédit.
  - Additionnées, les dépenses proposées dépassent le crédit et se disputent les mêmes jours : A4 2 à 4 USD ; A5 ≈ 1 ; C1 et C2 1 à 1,6 ; C3 3 à 5 ; D2 2 à 3 ; D3 0,5 à 2 ; D4 5 à 7.

  Il faut un ordre unique et un seul devis. B5 s'en approche, sans chiffrer.
- **Preuve.** `registres/depenses.md` (2026-10-20 06:07 ; 2026-10-19 22:35) ; `prereg` l. 369 ; `registres/go.md` (GO-2026-10-17-01).

### Ensemble 5 — mineure : doublons à fusionner
- **Objection.** Plusieurs options recouvrent la même chose :
  - le témoin positif au format : A5 = C1, proche de D3 (1) ;
  - le plan contexte × texte : C2 ≈ D2 ≈ le plafond masqué de A4 ;
  - la lecture au champ du coût : A2 ≈ D2.

  Un seul passage sur carte suffirait, avec une seule garde d'identité et un seul devis.
- **Preuve.** Propositions A, C et D, sections citées.
