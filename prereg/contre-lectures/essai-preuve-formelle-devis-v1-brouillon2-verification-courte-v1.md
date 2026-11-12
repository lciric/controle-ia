# Vérification courte — dessin et devis de l'essai « preuve formelle contre suite bon marché » (couche 4, pas (b) de R-2199), v1, brouillon 2

- **Rôle** : vérificateur neuf, sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`. Je n'ai écrit ni le dessin, ni ses scripts, ni la contre-lecture 1.
- **Modèle** : Claude Fable 5.2 (`claude-fable-5-2`) : autre modèle que le rédacteur (Opus 5.5), **même modèle que le contre-lecteur 1** (agent neuf, contexte neuf) ; N-052 nomme Fable 5.1 : écart à garder déclaré. Conflit possible : Fable 5.2 est une variante chiffrée des bras (D-3) ; je ne la recommande pas.
- **Heures** (relevées par `date -u`, le 2026-11-10) : début 13:48:29 UTC ; rapport écrit à 13:57:07 UTC.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-verification-courte-devis-lean-b2-v1.md` (`660d7001a8ca82a13c36f950c098e8d3af84e9040a7549c1bde227896914954b`, vérifiée avant lecture), interdits communs v2 recopiés.
- **Lu** : brouillon 2 (`05bcf094e3c26744242eb86c01b1c020e928dd6e7842eed34828d6f6b6de2af8`, égal à son compagnon) en entier ; journal v2 (`a56bc3e9…`) en entier ; contre-lecture 1 (`f565d51c…`) en entier ; les huit fichiers de `calculs-v2/` (empreintes égales aux compagnons) ; `registres/decisions.md`, lignes R-2230 et R-2235 seulement. Brouillon 1 (`9ccc9ac0…`) : passé aux scripts, non relu. Le message de relance que R-2230 résume ne m'a pas été donné : je m'en tiens à R-2230.
- **Non fait** : suite complète d'essais ; aucune vérification de prix sur page publique (aucun réseau) ; `calculs-v1/` non rejoué (fait par la contre-lecture 1) ; la formule du score de Tango que j'emploie vient de ma mémoire (forme de `PropCIs::scoreci.mp`), contrôlée sur deux cas limites seulement (elle se réduit à McNemar pour Δ₀ = 0 et au score binomial quand une case est vide) : **à vérifier sur la source** avant tout usage opposable.

## Verdict

**Présentable à Lazar pour D-1a : oui**, sous trois retouches de texte sans recalcul (VL-02, VL-03, et les deux phrases de VL-01 qui touchent D-5 et le § 1.7), que la mère peut aussi porter comme réserves dans son message plutôt que par un brouillon 3. **Aucun constat ne bloque D-1a sur le fond** : les 14 couples sont appliqués, le devis v4 se recalcule à l'identique, la cloison et la nature de la dépense sont écrites. **Trois constats bloquent le scellement du préenregistrement (donc D-1b), pas D-1a** : VL-01 (la règle de choix de la méthode d'intervalle, telle qu'écrite, ne peut pas contrôler les trois affirmations lues ; calcul exact fait), VL-04 (règle d'arrêt A8 incomplète), VL-05 (isolement : intégrité à l'intérieur de la machine non exigée, épreuve de garde en partie vide).

## Ce qui tient (rejoué dans le bac à sable, sur des copies, `python -I -B`)

1. **Couples (mandat 1)** : `appliquer_couples_cl1_v1.py` rejoué sur une copie du brouillon 1 et de la contre-lecture 1 : sortie identique à la sortie versée (au chemin de sortie près), jalon 3 d'empreinte `ff92495600cd094b821652d2a53bab16858e22a2eae2be12463760be25651719`, égale à celle du journal v2. Puis `retouches_brouillon2_v1.py` (48 retouches, R01 à R48), `deplacer_bloc_c05_v1.py` (R49), `deplacer_scenarios_c10_v1.py` (R50) sur une copie : le corps obtenu (avant la table des empreintes) est **identique au brouillon 2 versé à une ligne près**, celle de la retouche R51 (avantage de D-1b), décrite au journal et sans script. `table_et_controle_brouillon2_v1.py` n'a pas été rejoué tel quel (il écrit dans le dépôt par chemins relatifs et hache douze fichiers hors du dossier) : j'ai refait ses deux contrôles par un script à moi. Table : 28 lignes sur 29 égales au disque ; la 29ᵉ est `registres/decisions.md`, registre vivant, changé depuis (attendu).
2. **Chaque couple retrouvé** : le texte « Par » de C01 à C07, C09, C11 à C14 est présent une fois, mot pour mot. **C08** : le paragraphe ajouté est présent une fois, mot pour mot hors son titre ; la phrase reprise (« Plafond proposé de la phase 1 : 450 USD ») est remplacée par le plafond de D-1b à 550. **C10** : présent une fois avec « 150 à 300 aux scénarios du devis v4 » au lieu de « 192 à 300 aux effectifs du devis ». **Jugement** : les deux écarts sont **conformes au sens des couples** (C10 est la conséquence arithmétique de C04, vérifiée : 6 discordantes sur 60 donnent 2 × 75 graines ; C08 garde les lignes et les chiffre désormais dans le tableau). Le relèvement du plafond à 550 dépasse le couple : c'est une proposition du rédacteur, justifiée par un calcul que je retrouve (VL-04), à trancher par Lazar à D-1b. Résidus de texte : VL-07.
3. **Calculs (mandat 2)** : `calculs_devis_essai_v4.py` rejoué sous `.venv` : sortie identique octet pour octet à la sortie versée (`d44c4573437d436d35e2a37b331f02008081428c3161f3f90055f346d755e57e`). **Chiffres du brouillon 2 contre la sortie**, tous retrouvés : effectifs (51 à 252 ; 75, 102, 129, 150) ; issues à 97,5 % des § 1.7 et § 3.6 ; erreur de famille (0,020 à 0,026 ; 0,008 à 0,024 ; 0,027 à 0,060 ; 0,26 à 0,36) ; borne des fausses alertes ; coûts unitaires et rapport 3,11 et 8,24 ; réserve de A7 (32) ; tableau de D-1b (337,42 ; 346,78 ; 447,92 ; 457,28 ; 606,22 ; 615,58 ; 716,72 ; 726,08 ; 2 048,00) ; A8 (81, 107 ; 35, 41, 48, 54) ; tableau de la phase 2 et son détail ; variantes (223,88 ; 564,50 ; 866,80 ; 2 164,60) ; machine (48, 26, 62 à 70 heures ; 62,40 ; 33,80 ; 91,00 ; 14,40 à 57,60 ; 187,20) ; durées du § 4.4. Arithmétique : 65 + 550 + 35 + 1 900 + 91 = **2 641** ; 337 + 1 299 = 1 636 et 457 + 1 865 = 2 322 ; 457 + 32 = 489 ≤ 550 ; 1 865,20 + 32 = 1 897,20 ≤ 1 900.
4. **Lignes de CLP-06** : toutes présentes au pilote et en phase 2 (planteur des témoins et des renotations bis 11,00 ; adjudication avec le tirage de 20 items non litigieux 14,56 à 23,92 ; audit étendu 13,30 ; banque refaite 58,32 ; graines rejetées jusqu'à 50 % 38,88 ; banque de confirmation soumise à A6) ; A7 étendue et chiffrée. **Profil de CLP-09** : 1 000 k d'entrée et 100 k de sortie donnent bien 3,04 pour l'agent et 3,082 pour l'item, comme le bloc D de la contre-lecture 1.
5. **Ajouts sans couple** : CLP-07 (aucun chemin de bac à sable dans le texte ; contre-lecteur réel nommé ; 18 occurrences du marqueur « À REMPLIR », § 9), CLP-10 (a, b, c), CLP-12 (a à d : G-L6, G-L7, temps de processus, étape prouvée à vide), CLP-13 (motifs en tête) : présents. Décisions de la mère (R-2230) : D-1a et D-1b scindés, D-3 (a), D-4 (i), D-5 (i) amendée avec la variante K1, D-6 non pour l'instant : présentes au § 7, au format de décision.
6. **Cloison et dépense (mandat 5)** : le texte exige bien (a) une machine **sans clé ni dépôt du programme**, harnais hors de la machine (§ 4.5, deux puces ; D-2 (i) ; verdict, point 2) ; (b) une **garde éprouvée sur un cas sain et sur un artefact** (§ 4.5, § 3.1 R5, A1) ; (c) la **nature de la dépense** dite à Lazar (verdict, § 4.5, D-1, D-1b) ; (d) un **repli pour GPT-6 Astra** (§ 2.7 : R1 planteur Argon avec réserve écrite, R2 report ; marqueur de consigne de repli au § 9) ; (e) A12 : aucun appel facturé sans GO de D-1b. Compléments : VL-05.

## Constats

### VL-01 — O3 « sous le seuil » : limite écrite mais non bornée ; la règle de C09, telle qu'écrite, ne peut pas la borner (bloque le scellement ; deux phrases à retoucher avant présentation)

**Le fait est confirmé, par calcul exact** (énumération de la loi trinomiale, aucun tirage ; annexe, bloc A). Au gabarit de Wald ajusté, à Δ vrai = δ, « H(Δ) < δ » sort par classe de 0,013 à 0,031 pour une cible de 0,0125, soit **0,026 à 0,061 pour deux classes** (pire case : 60 graines, discordance 0,20) : la fourchette 0,027 à 0,060 du brouillon est juste. Le dépassement est maximal au bord où la suite ne détecte rien que la chaîne formelle manque (p₀₁ = 0, discordance = δ).

**Ce n'est pas un défaut du dessin** (deux classes, 97,5 %, sans porte : la structure contrôle la famille dès que chaque queue tient 0,0125) ; **c'est un défaut de la règle de choix de la méthode** (C09, § 3.6), que le brouillon présente comme le remède :
- **Newcombe ne répare pas O3** : 0,015 à 0,031 par classe (annexe, bloc B) ; il dépasse aussi côté « borne basse > 0 » (jusqu'à 0,0145).
- **Tango répare presque O3** (pire 0,0133, famille 0,026) et tient « borne basse > 0 » (pire 0,0126), **mais déplace le défaut sur O1a** : « B(Δ) ≥ δ » à Δ vrai = δ sort jusqu'à 0,0223 par classe (famille 0,044) au même bord (annexe, blocs A et C).
- Conséquence : la couverture bilatérale minimale de Tango à Δ = δ va de 0,966 à 0,976 selon l'effectif, celle de Newcombe descend vers 0,965 : **aucune des deux méthodes n'a une couverture minimale au-dessus du nominal** ; la règle « la plus proche de la couverture nominale par le haut » désigne un ensemble vide. Elle parle en outre de couverture bilatérale, alors que les trois affirmations lues sont unilatérales : une couverture bilatérale correcte peut cacher une queue à 0,02.
- Symétrie (R4) : au gabarit, les affirmations favorables à la chaîne formelle sont à peu près tenues et l'affirmation favorable à la suite ne l'est pas ; avec Tango, c'est l'inverse pour O1a.

**Ce qu'il faut, avant scellement** (travail sur processeur, faisable dès maintenant sans machine louée) :
1. Critère écrit **par queue et par affirmation** : « borne basse > 0 » à Δ = 0, « B ≥ δ » et « H < δ » à Δ = δ, chacune ≤ 0,0125 par classe ; la famille (deux classes, 0,025) et ce qu'elle contient sont écrits (VL-06).
2. Grille de la nuisance écrite : les valeurs de Δ (0 et δ), la discordance par pas fin **jusqu'au bord p₀₁ = 0**, les effectifs possibles (40 à 150) ; pour Newcombe, les rappels marginaux aussi (sa borne dépend des quatre cases).
3. **Énumération exacte** au lieu de tirages : à 40 000 tirages, l'écart-type sur 0,0125 est de 0,0006, ce qui ne sépare pas 0,0125 de 0,0133.
4. **Repli écrit si aucune méthode ne tient** (c'est le cas) : valeur critique calibrée par queue sur la grille. Ordre de grandeur (annexe, bloc C, score de Tango) : z* = 2,251 pour « borne basse > 0 », 2,266 pour « H < δ », 2,376 pour « B ≥ δ », contre 2,2414 ; soit 1 %, 2 % et 12 % d'effectif en plus à largeur égale.

**Recommandation** : score de Tango avec valeurs critiques calibrées par énumération exacte, une par affirmation, la fonction de calibrage étant scellée dans le script d'analyse (elle s'applique à l'effectif réalisé sans regarder les verdicts) ; O1a lu à sa valeur critique plus sévère sans redimensionner (sa puissance est déjà faible et le texte le dit). Effet sur le devis : négligeable (la règle d'effectif est au plafond de 150 dès 15 discordantes sur 60). La « simulation de C09 » du texte devient ce calcul.

**Avant présentation** (D-5 a un défaut sous 48 heures) : au § 7, D-5 (i), « contrôle de l'erreur de famille pour les affirmations établies » doit devenir « visé, à établir par le calcul de couverture avant scellement ; au gabarit, O3 dépasse (0,027 à 0,060) » ; au § 1.7, « sous le seuil n'y sort qu'environ trois fois sur cent » est un chiffre à 95 % : à 97,5 % par classe il vaut 0,013 à 0,029 pour une cible de 0,0125.

### VL-02 — D-1a : aucune règle d'arrêt ne tient le plafond de la machine (à ajouter avant présentation ; une phrase)

La seule dépense de D-1a est la machine ; le plafond de 65 USD repose sur 48 heures allumées (SUPPOSÉ) alors que le texte donne « 2 à 3 jours ». À la borne haute de 1,30 USD l'heure, 72 heures continues font 93,60. A7 ne compte que des appels ; A10 et A11 ne bornent pas un montant. **Il faut** : un compteur « heures allumées × prix horaire relevé à la location », arrêt par identifiant dès que le cumul atteint le plafond moins une heure, machine éteinte hors séance, prix et fournisseur consignés avant la location ; garde éprouvée (R5). Même règle pour les plafonds de machine de D-1b (35) et de la phase 2 (91).

### VL-03 — « Engagement maximal 2 641 USD » n'est pas un maximum (à reformuler avant présentation)

Le chiffre est exact comme somme des plafonds proposés et indicatifs. Mais le texte dit lui-même que le plafond de la phase 2 (1 900) est dépassé par l'attendu ordinaire au profil pire réaliste (2 451,40 ; 3 017,20 avec les lignes conditionnelles) et qu'il sera refait au devis 2. Si le pilote mesure ce profil, la phase 2 complète demande environ 2 483 à 3 049 (attendu plus réserve de A7), et le total environ **3 224 à 3 790 USD**. **Il faut** : « engagement aux plafonds proposés : 2 641 ; si le pilote mesure le profil pire réaliste, la phase 2 complète demanderait un plafond d'environ 2 500 à 3 050 (total 3 200 à 3 800), ou une phase 2 réduite sous 1 900 » ; et dire à Lazar que le premier GO n'engage que 65.

### VL-04 — A8 : calcul juste, règle d'arrêt incomplète (bloque le scellement, pas D-1a)

**Calcul vérifié** par un recalcul indépendant (annexe, bloc D) : au profil pire réaliste, charges fixes 149,14 plus réserve de A7 32, 7,618 par graine : **35 graines sous 450, 41 sous 500, 48 sous 550, 54 sous 600** ; au profil supposé 81 et 107. L'écart avec les 42 de la contre-lecture 1 vient de la réserve de A7 et de l'adjudication. Plafond minimal pour 40 graines à ce profil : 485,86 ; pour 60 : 638,22.

**La règle écrite ne dit pas ce que le script calcule** :
1. La formule du § 3.8, ⌊(plafond − dépense) / coût mesuré par graine⌋, ne retranche ni la réserve de A7 (32), ni les lignes restant à payer hors paires (adjudication, audit, renotations bis). Appliquée telle quelle, elle laisse passer 39 graines là où le script en donne 35 ; A8 peut donc dire « au moins 40 » et A7 couper ensuite en dessous. **Aucun texte ne dit ce qui arrive quand A7 coupe sous 40 graines.**
2. « après les 10 témoins et les 10 premières graines (20 items…) » : dix graines font vingt items, donc trente avec les témoins ; le script compte, lui, les 20 items de contrôle (témoins et renotations bis). À accorder.
3. **550 ne protège pas contre un bras formel au plafond par item** : si chaque item L coûte 4 USD, 37 graines sous 550 (arrêt) ; il faut 577,66 pour 40. Le texte ne le dit pas.
4. Le minimum de A8 (40 graines, 8 par classe) est l'effectif que D-1b (iii) écarte parce qu'il « ne porte pas un choix de classes » ; 48 graines font 9 blocs équilibrés, soit 45 graines équilibrées (9 par classe). À dire dans D-1b : au profil pire réaliste, le pilote payé à 550 est à peine au-dessus du pilote réduit écarté ; la variante (i bis) de D-5 (K1 fixée) en dépend moins.
5. Pistes sans relever le plafond, à chiffrer : finir sans parallélisme (réserve ramenée de 32 à 12), lecture nue en dernier (25,20, diagnostic).

### VL-05 — Isolement : ce qui manque à l'exigence (bloque le scellement ; à inscrire au périmètre de D-1a)

Le texte protège le dépôt et les clés. Il ne dit rien de **l'intérieur de la machine**, où tournent le code des deux bras et les contrôles du harnais :
1. **Intégrité du vérificateur** : le code d'un item (fichier Lean à la compilation, `python(code)`) peut modifier la chaîne Lean, le cache de Mathlib ou le fichier de contrôle du harnais (G-L7), ou laisser un fichier lu par un item suivant ou par l'autre bras. **Il faut** : un utilisateur sans privilège et un dossier neuf par item, chaîne et Mathlib en lecture seule, rien de persistant d'un item à l'autre, limites de processus et de mémoire ; la clé de la banque et les sorties de l'autre bras jamais sur la machine (à écrire en toutes lettres).
2. **Épreuve en partie vide** : sur une machine qui ne porte pas le dépôt, « lire un chemin du dépôt échoue » ne prouve rien. L'artefact doit viser un fichier leurre posé hors du dossier de l'item, le fichier de contrôle du harnais, la chaîne (écriture), et un fichier laissé pour l'item suivant ; chaque tentative échoue et se journalise.
3. **Réseau** : « sans réseau sortant » contredit l'installation de Lean et de Mathlib ; écrire l'ordre : réseau ouvert pour l'installation, puis fermé et éprouvé **avant** toute exécution de code écrit par un modèle.
4. **Repli du planteur** : R1 ou R2 doit être fixé dans le texte scellé ; sinon passer à R1 après le scellement est un écart à un préenregistrement (nœud).

### VL-06 — Niveaux des bornes de fausses alertes et famille (mineur ; avant scellement)

Le script prend le quantile 0,975 pour la borne haute de φ_L (queue de 0,025), que le texte appelle « Clopper–Pearson à 97,5 % » à côté d'intervalles « à 97,5 % bilatéraux » (queue de 0,0125) ; la borne basse de C11, même quantile, est dite « à 95 % ». À écrire sans équivoque (unilatéral ou bilatéral, queue). La famille contrôlée à 0,025 ne contient que les affirmations sur Δ ; « fausses alertes bornées » en est une de plus, à 0,025 : le dire. Hors mandat, pour la contre-lecture du préenregistrement : O2 se lit « rejette trop de preuves saines » sur la seule condition H(φ_L) > φ_max, qui n'établit pas φ_L > φ_max (même nature que CLP-01).

### VL-07 — Résidus de texte des couples (mineur)

(a) Paragraphe de C08 : « jusqu'au plafond » renvoie à l'ancien plafond de 450 ; « les mêmes lignes sont à ajouter au devis 2 » alors qu'elles y sont ; ses montants (≈ 11 pour l'audit étendu, ≈ 9 à 19 pour l'adjudication) diffèrent du tableau (13,30 ; 14,56 à 23,92). Le supprimer ou le dater. (b) Texte de C04 : « devis central à refaire » alors qu'il est refait et que le « central » est retiré. (c) Plafond indicatif de la phase 2 : avec 60 % d'items litigieux, 1 912,00 plus la réserve font 1 944, au-dessus de 1 900. (d) « 0,020 à 0,026 » pour « borne basse > 0 » : exact sur la grille du script ; le calcul exact donne jusqu'à 0,029 à 40 graines et forte discordance (gabarit seulement).

### VL-08 — Traçabilité (mineur, R6)

La table des empreintes du brouillon 2 ne cite pas les quatre scripts de retouche versés après son scellement (R-2235 l'explique) ; la retouche R51 n'a pas de script ; la sortie des retouches (`5fd73ac8…`) n'est pas versée. Le rejeu ci-dessus établit que le corps du brouillon 2 est exactement « jalon 3, R01 à R50, R51 ». À citer dans la prochaine version.

## Réponse aux six points du mandat

1. Couples rejoués : 14 retrouvés ; C08 et C10 conformes au sens.
2. Calcul v4 identique ; tables conformes ; 2 641 exact comme somme, mal nommé (VL-03) ; CLP-06 et CLP-09 traités.
3. O3 : limite écrite, non bornée ; défaut de la règle de C09, non du dessin ; remède chiffré (VL-01).
4. A8 : 35 et 48 exacts ; règle d'arrêt à compléter (VL-04).
5. Cloison, garde, nature de la dépense, repli : écrits ; compléments (VL-05).
6. **Présentable à Lazar pour D-1a : oui**, avec VL-02, VL-03 et les deux phrases de VL-01 ; rien ne manque au calcul.

## Exposition, cloison, interdits

Aucun chemin des interdits communs ouvert (rien sous `diag/`, `runs/`, `donnees/`, `docs/notes/bras-attaque/`, aucune branche). Aucune recherche récursive : fichiers nommés, `ls` de dossiers nommés, un `git grep` sur `registres/decisions.md` seul, un `git status --short` (lecture). Scripts du dépôt exécutés seulement depuis des copies dans `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/verif-devis-lean-b2/`, sur une copie de l'arbre utile. Aucun appel de modèle ni d'interface, aucun réseau, aucune installation, aucune dépense, aucune écriture git. Aucun refus rencontré. Aucune valeur de sonde de la course 7a sous mes yeux. Écrit dans le dépôt : ce fichier et son compagnon, rien d'autre.

---

## Annexe — scripts du vérificateur et sorties (rejouables ; aucun appel, aucun réseau)

Lancés par `.venv/bin/python -I -B` depuis le bac à sable (numpy et scipy de `.venv`). Empreintes à l'exécution : `verif_vl_v1.py` `97448ce63339c75845f2c2ac5e72fb89f13dfe92ecd6cde015f7719b2105475f`, sortie `646a9bbc41e1679b4195945724c4af42a3bf5f638c69a3bbcdc0a70e10da852e` ; `verif_vl_calibrage_v1.py` `fef51bb3af55f038e74729ef47a5658b2d3981d9bef73b7e6119c75ffdccbd05` (argument : le dossier qui contient le premier script), sortie `83a13e6008ee97fe048723dfd980c548e51682b0c4112a36871e097265a9a605`. Dans les sorties : « W » gabarit de Wald ajusté, « T » score de Tango ; « B>0|D=0 » fausse borne basse au-dessus de zéro quand Δ = 0 ; « H<d|D=d » faux « sous le seuil » quand Δ = δ ; « B>=d|D=d » faux O1a quand Δ = δ ; entre crochets, deux classes. Les blocs cités dans les constats : A et A′ (erreurs exactes), B (Newcombe), C du second script (grille fine et z*), D = bloc « (C) A8 » du premier script.

### `verif_vl_v1.py`

```python
"""verif_vl_v1.py — vérifications du vérificateur court (brouillon 2 du devis de l'essai Lean). Aucun appel, aucun réseau.
(A) erreurs unilatérales EXACTES (énumération de la loi trinomiale, aucun tirage) des trois affirmations lues, par classe et pour
deux classes indépendantes, au niveau 97,5 % bilatéral : gabarit de Wald ajusté du script v4 et score de Tango.
(B) Newcombe hybride (dépend des quatre cases : tirages, SeedSequence, R9).
(C) A8 : graines payables, recalcul indépendant, plus le profil « tout au plafond par item »."""
import math, sys
import numpy as np
from scipy import stats
from scipy.special import gammaln
Z = stats.norm.ppf(1 - 0.025 / 2); DELTA = 0.20; CIBLE = 0.0125

def loi(n, p10, p01):
    i = np.arange(n + 1)[:, None]; j = np.arange(n + 1)[None, :]
    ok = (i + j) <= n
    k = np.where(ok, n - i - j, 0)
    p00 = 1 - p10 - p01
    with np.errstate(divide="ignore", invalid="ignore"):
        lp = gammaln(n + 1) - gammaln(i + 1) - gammaln(j + 1) - gammaln(k + 1)
        lp = lp + np.where(i > 0, i * np.log(p10) if p10 > 0 else -np.inf, 0.0)
        lp = lp + np.where(j > 0, j * np.log(p01) if p01 > 0 else -np.inf, 0.0)
        lp = lp + np.where(k > 0, k * np.log(p00) if p00 > 0 else -np.inf, 0.0)
    pr = np.where(ok, np.exp(lp), 0.0)
    return i + 0 * j, j + 0 * i, pr

def wald(n10, n01, n, z):
    a10, a01, m = n10 + .5, n01 + .5, n + 2.
    d = (a10 - a01) / m; v = ((a10 + a01) / m - d * d) / m; h = z * np.sqrt(np.maximum(v, 0))
    return d - h, d + h

def score_tango(n10, n01, n, d0):
    """Statistique de score de Tango (1998) pour H : p10 - p01 = d0 (forme de PropCIs::scoreci.mp)."""
    b, c = n01.astype(float), n10.astype(float)
    A = 2 * n; B = -b - c + (2 * n - c + b) * d0; C = -b * d0 * (1 - d0)
    q = (np.sqrt(B * B - 4 * A * C) - B) / (2 * A)
    den = np.sqrt(np.maximum(n * (2 * q + d0 * (1 - d0)), 1e-300))
    return (c - b - n * d0) / den

print(f"z = {Z:.4f} ; cible par queue et par classe {CIBLE} ; cible de famille (deux classes) 0,025")
print("\n== (A) erreurs exactes par classe [famille de deux classes entre crochets]")
pire = {}
for n in (40, 60, 75, 102, 129, 150):
    for disc in (0.10, 0.20, 0.30, 0.40, 0.50):
        lig = [f"n={n:3d} disc={disc:.2f}"]
        # Delta vrai = 0 : fausse « borne basse > 0 »
        i, j, pr = loi(n, disc / 2, disc / 2)
        lb, ub = wald(i, j, n, Z)
        e = {"W: B>0|D=0": pr[lb > 0].sum(), "T: B>0|D=0": pr[score_tango(i, j, n, 0.0) > Z].sum()}
        if disc >= DELTA:
            i, j, pr = loi(n, (disc + DELTA) / 2, (disc - DELTA) / 2)
            lb, ub = wald(i, j, n, Z); s = score_tango(i, j, n, DELTA)
            e.update({"W: H<d|D=d": pr[ub < DELTA].sum(), "T: H<d|D=d": pr[s < -Z].sum(),
                      "W: B>=d|D=d": pr[lb >= DELTA].sum(), "T: B>=d|D=d": pr[s > Z].sum()})
        for k, v in e.items():
            lig.append(f"{k} {v:.4f} [{1 - (1 - v) ** 2:.4f}]")
            if v > pire.get(k, (0,))[0]: pire[k] = (v, n, disc)
        print("  " + " | ".join(lig))
print("\n   pires cases de la grille (par classe ; famille) :")
for k, (v, n, disc) in pire.items():
    print(f"   {k:14s} : {v:.4f} ; {1 - (1 - v) ** 2:.4f}  (n={n}, disc={disc:.2f})  {'AU-DESSUS' if v > CIBLE else 'sous'} la cible")

print("\n== (A') niveau qu'il faudrait au gabarit de Wald et au score de Tango pour que « H < delta » tienne 0,0125 sur la grille (disc >= 0,20)")
for nom in ("W", "T"):
    for z in np.arange(2.20, 3.21, 0.05):
        mx = 0
        for n in (40, 60, 75, 102, 129, 150):
            for disc in (0.20, 0.25, 0.30, 0.40, 0.50):
                i, j, pr = loi(n, (disc + DELTA) / 2, (disc - DELTA) / 2)
                v = pr[wald(i, j, n, z)[1] < DELTA].sum() if nom == "W" else pr[score_tango(i, j, n, DELTA) < -z].sum()
                mx = max(mx, v)
        if mx <= CIBLE:
            print(f"   {nom} : premier z de la grille (pas de 0,05) qui tient : {z:.2f} (pire case {mx:.4f}) ; effectif multiplié par {(z / Z) ** 2:.2f}")
            break
    else:
        print(f"   {nom} : aucun z jusqu'à 3,20")

print("\n== (B) Newcombe hybride (méthode 10), 400 000 tirages par case, erreurs par classe")
ss = np.random.SeedSequence(2026111013); rng = np.random.default_rng(ss.spawn(1)[0])
def wilson(x, n, z):
    p = x / n; c = (p + z * z / (2 * n)) / (1 + z * z / n); h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return c - h, c + h
def newcombe(a, b, c, d, z):
    n = a + b + c + d; p1 = (a + b) / n; p2 = (a + c) / n
    l1, u1 = wilson(a + b, n, z); l2, u2 = wilson(a + c, n, z)
    den = np.sqrt((a + b) * (c + d) * (a + c) * (b + d).astype(float))
    phi = np.where(den > 0, (a * d - b * c) / np.where(den > 0, den, 1), 0.0)
    th = (b - c) / n
    lo = th - np.sqrt(np.maximum((p1 - l1) ** 2 - 2 * phi * (p1 - l1) * (u2 - p2) + (u2 - p2) ** 2, 0))
    up = th + np.sqrt(np.maximum((p2 - l2) ** 2 - 2 * phi * (p2 - l2) * (u1 - p1) + (u1 - p1) ** 2, 0))
    return lo, up
for n in (75, 150):
    for disc in (0.20, 0.30, 0.40):
        for rS in (0.30, 0.60):
            out = [f"n={n:3d} disc={disc:.2f} rappel S={rS:.2f}"]
            for dv in (0.0, DELTA):
                p10, p01 = (disc + dv) / 2, (disc - dv) / 2; p11 = rS - p01; p00 = 1 - p11 - p10 - p01
                if min(p11, p00) < 0: out.append(f"D={dv:.2f} : impossible"); continue
                t = rng.multinomial(n, [p11, p10, p01, p00], size=400000)
                lo, up = newcombe(t[:, 0], t[:, 1], t[:, 2], t[:, 3], Z)
                out.append((f"B>0|D=0 {np.mean(lo > 0):.4f}" if dv == 0 else f"H<d|D=d {np.mean(up < DELTA):.4f} ; B>=d|D=d {np.mean(lo >= DELTA):.4f}"))
            print("  " + " | ".join(out))

print("\n== (C) A8 : graines payables, recalcul indépendant (prix et profils du brouillon 2)")
def c(pe, ps, e, s, lu=0., ec=0.): return (e * (1 - lu - ec) * pe + e * lu * pe * .1 + e * ec * pe * 1.25 + s * ps) / 1e6
S_ = c(4, 20, 100e3, 10e3, .8, .1) + c(2, 10, 6e3, 4e3); N_ = c(4, 20, 5e3, 8e3); T_ = c(10, 50, 5e3, 10e3)
G_ = c(10, 50, 6e3, 4e3); A_ = c(10, 50, 4e3, 3e3); ADJ = G_
for nom, L in (("supposé", c(4, 20, 500e3, 30e3, .85, .1) + c(2, 10, 6e3, 3e3)), ("pire réaliste", c(4, 20, 1e6, 100e3, .85, .1) + c(2, 10, 6e3, 3e3)), ("tout item L au plafond de 4 USD", 4.0)):
    fixe = 72 * (T_ + G_) + 20 * T_ + 20 * (L + S_ + N_) + 10 * A_ + 20 * ADJ
    pg = 2 * (L + S_ + N_) + A_ + 0.6 * ADJ
    lig = [f"profil « {nom} » (item L {L:.3f}) : fixe {fixe:.2f} + réserve A7 32 ; par graine {pg:.3f}"]
    for pl in (450, 500, 550, 600, 650):
        lig.append(f"{pl}: {int((pl - 32 - fixe) // pg)} (sans réserve {int((pl - fixe) // pg)})")
    lig.append(f"plafond minimal pour 40 graines : {fixe + 32 + 40 * pg:.2f} ; pour 60 : {fixe + 32 + 60 * pg:.2f}")
    print("  " + " ; ".join(lig))
```

### Sortie de `verif_vl_v1.py`

```text
z = 2.2414 ; cible par queue et par classe 0.0125 ; cible de famille (deux classes) 0,025

== (A) erreurs exactes par classe [famille de deux classes entre crochets]
  n= 40 disc=0.10 | W: B>0|D=0 0.0025 [0.0049] | T: B>0|D=0 0.0025 [0.0049]
  n= 40 disc=0.20 | W: B>0|D=0 0.0094 [0.0186] | T: B>0|D=0 0.0093 [0.0186] | W: H<d|D=d 0.0285 [0.0561] | T: H<d|D=d 0.0079 [0.0158] | W: B>=d|D=d 0.0029 [0.0059] | T: B>=d|D=d 0.0079 [0.0158]
  n= 40 disc=0.30 | W: B>0|D=0 0.0122 [0.0243] | T: B>0|D=0 0.0116 [0.0230] | W: H<d|D=d 0.0220 [0.0434] | T: H<d|D=d 0.0112 [0.0223] | W: B>=d|D=d 0.0071 [0.0141] | T: B>=d|D=d 0.0121 [0.0240]
  n= 40 disc=0.40 | W: B>0|D=0 0.0143 [0.0283] | T: B>0|D=0 0.0112 [0.0223] | W: H<d|D=d 0.0162 [0.0321] | T: H<d|D=d 0.0124 [0.0247] | W: B>=d|D=d 0.0099 [0.0197] | T: B>=d|D=d 0.0111 [0.0221]
  n= 40 disc=0.50 | W: B>0|D=0 0.0148 [0.0294] | T: B>0|D=0 0.0109 [0.0218] | W: H<d|D=d 0.0148 [0.0294] | T: H<d|D=d 0.0127 [0.0252] | W: B>=d|D=d 0.0122 [0.0242] | T: B>=d|D=d 0.0100 [0.0200]
  n= 60 disc=0.10 | W: B>0|D=0 0.0063 [0.0126] | T: B>0|D=0 0.0063 [0.0126]
  n= 60 disc=0.20 | W: B>0|D=0 0.0116 [0.0230] | T: B>0|D=0 0.0115 [0.0228] | W: H<d|D=d 0.0308 [0.0607] | T: H<d|D=d 0.0121 [0.0241] | W: B>=d|D=d 0.0020 [0.0041] | T: B>=d|D=d 0.0221 [0.0436]
  n= 60 disc=0.30 | W: B>0|D=0 0.0127 [0.0252] | T: B>0|D=0 0.0110 [0.0220] | W: H<d|D=d 0.0177 [0.0351] | T: H<d|D=d 0.0109 [0.0216] | W: B>=d|D=d 0.0069 [0.0137] | T: B>=d|D=d 0.0182 [0.0361]
  n= 60 disc=0.40 | W: B>0|D=0 0.0140 [0.0278] | T: B>0|D=0 0.0116 [0.0231] | W: H<d|D=d 0.0151 [0.0301] | T: H<d|D=d 0.0128 [0.0255] | W: B>=d|D=d 0.0107 [0.0212] | T: B>=d|D=d 0.0139 [0.0276]
  n= 60 disc=0.50 | W: B>0|D=0 0.0136 [0.0271] | T: B>0|D=0 0.0124 [0.0246] | W: H<d|D=d 0.0135 [0.0268] | T: H<d|D=d 0.0132 [0.0263] | W: B>=d|D=d 0.0127 [0.0253] | T: B>=d|D=d 0.0116 [0.0230]
  n= 75 disc=0.10 | W: B>0|D=0 0.0086 [0.0171] | T: B>0|D=0 0.0086 [0.0171]
  n= 75 disc=0.20 | W: B>0|D=0 0.0120 [0.0238] | T: B>0|D=0 0.0114 [0.0226] | W: H<d|D=d 0.0243 [0.0480] | T: H<d|D=d 0.0104 [0.0207] | W: B>=d|D=d 0.0047 [0.0093] | T: B>=d|D=d 0.0187 [0.0371]
  n= 75 disc=0.30 | W: B>0|D=0 0.0126 [0.0251] | T: B>0|D=0 0.0114 [0.0226] | W: H<d|D=d 0.0180 [0.0356] | T: H<d|D=d 0.0115 [0.0229] | W: B>=d|D=d 0.0089 [0.0176] | T: B>=d|D=d 0.0135 [0.0268]
  n= 75 disc=0.40 | W: B>0|D=0 0.0125 [0.0248] | T: B>0|D=0 0.0123 [0.0245] | W: H<d|D=d 0.0150 [0.0297] | T: H<d|D=d 0.0123 [0.0245] | W: B>=d|D=d 0.0119 [0.0237] | T: B>=d|D=d 0.0119 [0.0237]
  n= 75 disc=0.50 | W: B>0|D=0 0.0133 [0.0263] | T: B>0|D=0 0.0122 [0.0243] | W: H<d|D=d 0.0141 [0.0281] | T: H<d|D=d 0.0125 [0.0249] | W: B>=d|D=d 0.0130 [0.0259] | T: B>=d|D=d 0.0112 [0.0223]
  n=102 disc=0.10 | W: B>0|D=0 0.0109 [0.0216] | T: B>0|D=0 0.0109 [0.0216]
  n=102 disc=0.20 | W: B>0|D=0 0.0111 [0.0222] | T: B>0|D=0 0.0111 [0.0222] | W: H<d|D=d 0.0205 [0.0405] | T: H<d|D=d 0.0100 [0.0198] | W: B>=d|D=d 0.0044 [0.0088] | T: B>=d|D=d 0.0150 [0.0297]
  n=102 disc=0.30 | W: B>0|D=0 0.0123 [0.0245] | T: B>0|D=0 0.0123 [0.0245] | W: H<d|D=d 0.0178 [0.0352] | T: H<d|D=d 0.0118 [0.0235] | W: B>=d|D=d 0.0088 [0.0175] | T: B>=d|D=d 0.0130 [0.0259]
  n=102 disc=0.40 | W: B>0|D=0 0.0126 [0.0251] | T: B>0|D=0 0.0120 [0.0239] | W: H<d|D=d 0.0153 [0.0304] | T: H<d|D=d 0.0126 [0.0251] | W: B>=d|D=d 0.0113 [0.0225] | T: B>=d|D=d 0.0114 [0.0227]
  n=102 disc=0.50 | W: B>0|D=0 0.0135 [0.0269] | T: B>0|D=0 0.0122 [0.0243] | W: H<d|D=d 0.0133 [0.0264] | T: H<d|D=d 0.0128 [0.0254] | W: B>=d|D=d 0.0122 [0.0243] | T: B>=d|D=d 0.0113 [0.0225]
  n=129 disc=0.10 | W: B>0|D=0 0.0115 [0.0228] | T: B>0|D=0 0.0115 [0.0228]
  n=129 disc=0.20 | W: B>0|D=0 0.0119 [0.0236] | T: B>0|D=0 0.0119 [0.0236] | W: H<d|D=d 0.0294 [0.0579] | T: H<d|D=d 0.0086 [0.0171] | W: B>=d|D=d 0.0037 [0.0075] | T: B>=d|D=d 0.0192 [0.0381]
  n=129 disc=0.30 | W: B>0|D=0 0.0125 [0.0248] | T: B>0|D=0 0.0121 [0.0241] | W: H<d|D=d 0.0169 [0.0336] | T: H<d|D=d 0.0114 [0.0227] | W: B>=d|D=d 0.0094 [0.0186] | T: B>=d|D=d 0.0127 [0.0252]
  n=129 disc=0.40 | W: B>0|D=0 0.0126 [0.0250] | T: B>0|D=0 0.0122 [0.0243] | W: H<d|D=d 0.0147 [0.0292] | T: H<d|D=d 0.0129 [0.0256] | W: B>=d|D=d 0.0118 [0.0234] | T: B>=d|D=d 0.0117 [0.0233]
  n=129 disc=0.50 | W: B>0|D=0 0.0127 [0.0253] | T: B>0|D=0 0.0125 [0.0249] | W: H<d|D=d 0.0133 [0.0264] | T: H<d|D=d 0.0131 [0.0260] | W: B>=d|D=d 0.0131 [0.0260] | T: B>=d|D=d 0.0118 [0.0235]
  n=150 disc=0.10 | W: B>0|D=0 0.0114 [0.0226] | T: B>0|D=0 0.0114 [0.0226]
  n=150 disc=0.20 | W: B>0|D=0 0.0123 [0.0244] | T: B>0|D=0 0.0123 [0.0244] | W: H<d|D=d 0.0224 [0.0442] | T: H<d|D=d 0.0128 [0.0253] | W: B>=d|D=d 0.0041 [0.0081] | T: B>=d|D=d 0.0187 [0.0370]
  n=150 disc=0.30 | W: B>0|D=0 0.0127 [0.0252] | T: B>0|D=0 0.0120 [0.0238] | W: H<d|D=d 0.0156 [0.0309] | T: H<d|D=d 0.0117 [0.0232] | W: B>=d|D=d 0.0091 [0.0181] | T: B>=d|D=d 0.0133 [0.0265]
  n=150 disc=0.40 | W: B>0|D=0 0.0126 [0.0250] | T: B>0|D=0 0.0125 [0.0249] | W: H<d|D=d 0.0138 [0.0275] | T: H<d|D=d 0.0124 [0.0246] | W: B>=d|D=d 0.0112 [0.0223] | T: B>=d|D=d 0.0121 [0.0241]
  n=150 disc=0.50 | W: B>0|D=0 0.0132 [0.0261] | T: B>0|D=0 0.0123 [0.0244] | W: H<d|D=d 0.0131 [0.0260] | T: H<d|D=d 0.0130 [0.0258] | W: B>=d|D=d 0.0124 [0.0247] | T: B>=d|D=d 0.0119 [0.0237]

   pires cases de la grille (par classe ; famille) :
   W: B>0|D=0     : 0.0148 ; 0.0294  (n=40, disc=0.50)  AU-DESSUS la cible
   T: B>0|D=0     : 0.0125 ; 0.0249  (n=129, disc=0.50)  AU-DESSUS la cible
   W: H<d|D=d     : 0.0308 ; 0.0607  (n=60, disc=0.20)  AU-DESSUS la cible
   T: H<d|D=d     : 0.0132 ; 0.0263  (n=60, disc=0.50)  AU-DESSUS la cible
   W: B>=d|D=d    : 0.0131 ; 0.0260  (n=129, disc=0.50)  AU-DESSUS la cible
   T: B>=d|D=d    : 0.0221 ; 0.0436  (n=60, disc=0.20)  AU-DESSUS la cible

== (A') niveau qu'il faudrait au gabarit de Wald et au score de Tango pour que « H < delta » tienne 0,0125 sur la grille (disc >= 0,20)
   W : premier z de la grille (pas de 0,05) qui tient : 2.80 (pire case 0.0121) ; effectif multiplié par 1.56
   T : premier z de la grille (pas de 0,05) qui tient : 2.30 (pire case 0.0111) ; effectif multiplié par 1.05

== (B) Newcombe hybride (méthode 10), 400 000 tirages par case, erreurs par classe
  n= 75 disc=0.20 rappel S=0.30 | B>0|D=0 0.0132 | H<d|D=d 0.0307 ; B>=d|D=d 0.0046
  n= 75 disc=0.20 rappel S=0.60 | B>0|D=0 0.0138 | H<d|D=d 0.0238 ; B>=d|D=d 0.0046
  n= 75 disc=0.30 rappel S=0.30 | B>0|D=0 0.0139 | H<d|D=d 0.0202 ; B>=d|D=d 0.0088
  n= 75 disc=0.30 rappel S=0.60 | B>0|D=0 0.0145 | H<d|D=d 0.0182 ; B>=d|D=d 0.0086
  n= 75 disc=0.40 rappel S=0.30 | B>0|D=0 0.0127 | H<d|D=d 0.0180 ; B>=d|D=d 0.0102
  n= 75 disc=0.40 rappel S=0.60 | B>0|D=0 0.0141 | H<d|D=d 0.0154 ; B>=d|D=d 0.0102
  n=150 disc=0.20 rappel S=0.30 | B>0|D=0 0.0124 | H<d|D=d 0.0225 ; B>=d|D=d 0.0070
  n=150 disc=0.20 rappel S=0.60 | B>0|D=0 0.0127 | H<d|D=d 0.0223 ; B>=d|D=d 0.0068
  n=150 disc=0.30 rappel S=0.30 | B>0|D=0 0.0128 | H<d|D=d 0.0180 ; B>=d|D=d 0.0096
  n=150 disc=0.30 rappel S=0.60 | B>0|D=0 0.0132 | H<d|D=d 0.0160 ; B>=d|D=d 0.0101
  n=150 disc=0.40 rappel S=0.30 | B>0|D=0 0.0128 | H<d|D=d 0.0151 ; B>=d|D=d 0.0111
  n=150 disc=0.40 rappel S=0.60 | B>0|D=0 0.0128 | H<d|D=d 0.0147 ; B>=d|D=d 0.0111

== (C) A8 : graines payables, recalcul indépendant (prix et profils du brouillon 2)
  profil « supposé » (item L 1.162) : fixe 110.74 + réserve A7 32 ; par graine 3.778 ; 450: 81 (sans réserve 89) ; 500: 94 (sans réserve 103) ; 550: 107 (sans réserve 116) ; 600: 121 (sans réserve 129) ; 650: 134 (sans réserve 142) ; plafond minimal pour 40 graines : 293.86 ; pour 60 : 369.42
  profil « pire réaliste » (item L 3.082) : fixe 149.14 + réserve A7 32 ; par graine 7.618 ; 450: 35 (sans réserve 39) ; 500: 41 (sans réserve 46) ; 550: 48 (sans réserve 52) ; 600: 54 (sans réserve 59) ; 650: 61 (sans réserve 65) ; plafond minimal pour 40 graines : 485.86 ; pour 60 : 638.22
  profil « tout item L au plafond de 4 USD » (item L 4.000) : fixe 167.50 + réserve A7 32 ; par graine 9.454 ; 450: 26 (sans réserve 29) ; 500: 31 (sans réserve 35) ; 550: 37 (sans réserve 40) ; 600: 42 (sans réserve 45) ; 650: 47 (sans réserve 51) ; plafond minimal pour 40 graines : 577.66 ; pour 60 : 766.74
```

### `verif_vl_calibrage_v1.py`

```python
"""verif_vl_calibrage_v1.py — suite de verif_vl_v1.py : sur une grille fine de la nuisance (discordance, pas de 0,01, bord
p01 = 0 compris), pire erreur exacte par queue du score de Tango, et valeur critique z* qui tient 0,0125 par queue. Aucun tirage."""
import sys, numpy as np
sys.dont_write_bytecode = True
sys.path.insert(0, sys.argv[1])
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import verif_vl_v1 as v
Z, D, C = v.Z, v.DELTA, v.CIBLE
NS = (40, 60, 75, 102, 129, 150)
def scores(n):
    out = {"B>0|D=0": [], "H<d|D=d": [], "B>=d|D=d": []}
    for disc in np.round(np.arange(0.02, 0.601, 0.01), 2):
        i, j, pr = v.loi(n, disc / 2, disc / 2); out["B>0|D=0"].append((disc, v.score_tango(i, j, n, 0.0), pr, +1))
        if disc >= D - 1e-9:
            i, j, pr = v.loi(n, (disc + D) / 2, max((disc - D) / 2, 0.0)); s = v.score_tango(i, j, n, D)
            out["H<d|D=d"].append((disc, s, pr, -1)); out["B>=d|D=d"].append((disc, s, pr, +1))
    return out
print(f"score de Tango, z nominal {Z:.4f}, cible {C} par queue ; discordance de 0,02 à 0,60 par pas de 0,01")
zmax = {}
for n in NS:
    sc = scores(n); lig = [f"n={n:3d}"]
    for nom, cas in sc.items():
        pire = max(((pr[(sg * s) > Z].sum(), disc) for disc, s, pr, sg in cas))
        z = Z
        while max(pr[(sg * s) > z].sum() for disc, s, pr, sg in cas) > C: z += 0.005
        zmax[nom] = max(zmax.get(nom, 0), z)
        lig.append(f"{nom} : pire {pire[0]:.4f} (disc {pire[1]:.2f}), z* {z:.3f}")
    # couverture bilatérale minimale à Delta = delta
    cb = min((1 - pr[np.abs(s) > Z].sum(), disc) for disc, s, pr, sg in sc["H<d|D=d"])
    lig.append(f"couverture bilatérale minimale à Delta = delta : {cb[0]:.4f} (disc {cb[1]:.2f})")
    print("  " + " | ".join(lig))
print("z* qui tient sur toute la grille, par queue :", {k: round(x, 3) for k, x in zmax.items()},
      "; effectif multiplié par", {k: round((x / Z) ** 2, 2) for k, x in zmax.items()})
```

### Sortie de `verif_vl_calibrage_v1.py`

```text
score de Tango, z nominal 2.2414, cible 0.0125 par queue ; discordance de 0,02 à 0,60 par pas de 0,01
  n= 40 | B>0|D=0 : pire 0.0117 (disc 0.60), z* 2.241 | H<d|D=d : pire 0.0128 (disc 0.46), z* 2.256 | B>=d|D=d : pire 0.0121 (disc 0.31), z* 2.241 | couverture bilatérale minimale à Delta = delta : 0.9763 (disc 0.34)
  n= 60 | B>0|D=0 : pire 0.0124 (disc 0.54), z* 2.241 | H<d|D=d : pire 0.0132 (disc 0.49), z* 2.266 | B>=d|D=d : pire 0.0223 (disc 0.22), z* 2.261 | couverture bilatérale minimale à Delta = delta : 0.9658 (disc 0.20)
  n= 75 | B>0|D=0 : pire 0.0124 (disc 0.43), z* 2.241 | H<d|D=d : pire 0.0129 (disc 0.57), z* 2.261 | B>=d|D=d : pire 0.0187 (disc 0.20), z* 2.311 | couverture bilatérale minimale à Delta = delta : 0.9709 (disc 0.20)
  n=102 | B>0|D=0 : pire 0.0126 (disc 0.60), z* 2.251 | H<d|D=d : pire 0.0130 (disc 0.58), z* 2.266 | B>=d|D=d : pire 0.0153 (disc 0.22), z* 2.376 | couverture bilatérale minimale à Delta = delta : 0.9737 (disc 0.24)
  n=129 | B>0|D=0 : pire 0.0125 (disc 0.48), z* 2.251 | H<d|D=d : pire 0.0131 (disc 0.46), z* 2.256 | B>=d|D=d : pire 0.0192 (disc 0.20), z* 2.276 | couverture bilatérale minimale à Delta = delta : 0.9721 (disc 0.21)
  n=150 | B>0|D=0 : pire 0.0125 (disc 0.42), z* 2.251 | H<d|D=d : pire 0.0133 (disc 0.60), z* 2.256 | B>=d|D=d : pire 0.0187 (disc 0.20), z* 2.266 | couverture bilatérale minimale à Delta = delta : 0.9686 (disc 0.20)
z* qui tient sur toute la grille, par queue : {'B>0|D=0': np.float64(2.251), 'H<d|D=d': np.float64(2.266), 'B>=d|D=d': np.float64(2.376)} ; effectif multiplié par {'B>0|D=0': np.float64(1.01), 'H<d|D=d': np.float64(1.02), 'B>=d|D=d': np.float64(1.12)}
```
