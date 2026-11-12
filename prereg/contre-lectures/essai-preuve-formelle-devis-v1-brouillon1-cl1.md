# Contre-lecture 1 (R2, N-052) — dessin et devis de l'essai « preuve formelle contre suite bon marché » (couche 4, pas (b) de R-2199), v1, brouillon 1

- **Rôle** : contre-lecteur neuf au sens de R2, sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`. Je n'ai écrit ni le brouillon, ni son journal, ni ses scripts, ni la synthèse du tour 2, ni aucune pièce citée.
- **Modèle** : Claude Fable 5.2 (`claude-fable-5-2`), autre modèle que le rédacteur (Claude Opus 5.5), même famille. **À noter pour la mère** : le brouillon (en-tête et § 2.7) et N-052 nomment Fable 5.1 comme contre-lecteur ; je suis Fable 5.2. **Conflit possible déclaré** : Fable 5.2 est l'une des deux variantes de modèle des bras chiffrées par le brouillon (D-3) ; je ne la recommande pas.
- **Heures** (relevées par `date -u`, le 2026-11-10) : début 13:22:56 UTC ; rapport écrit à 13:29:51 UTC.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-contre-lecture-devis-essai-preuve-formelle-v1.md` (`99dfe1a03b3f825b4074d4c46e75b60159b6550dbe4a3ac9a75efddefa44c5a8`, égale à son compagnon), interdits communs v2 recopiés, lue en entier avant toute autre action.
- **Texte relu** : `brouillons/couche4-essai-preuve-formelle-v1/essai-preuve-formelle-devis-v1-brouillon1.md` (`9ccc9ac01cb95db8184f87629e3b77eaa24820717ffa29a822f471ccf91bdade`, égale au préfixe de la consigne), lu en entier (637 lignes) ; son journal (`f8c2b8c64e3e9c7125c1496321765be0b3891c809e36a290cbc1b484c1cd003d`), lu en entier.
- **Lu aussi** : sous `brouillons/couche4-essai-preuve-formelle-v1/calculs-v1/`, les trois scripts nommés (lus en entier) et leurs sorties ; les douze fichiers du dossier ont une empreinte égale à leur compagnon et à la table du brouillon. Synthèse du tour 2 (`6ef6bc2e1cbea69b0b47f20508fa09391e7c2271785287c470dc632de5a2b1ce`, égale à son compagnon) : section E (l. 214 à 258) et « Ce qui reste chez Lazar » (l. 423 à 438). `registres/decisions.md` (registre vivant, `ff79fdf28444b650…` à la lecture) : lignes R-959, R-2199, R-2226 seulement. Sources de prix : `collisionneur_v8.py` (`22e5ed8a…`, égale à son compagnon), l. 60 à 95 ; référence locale `claude-api`, `shared/models.md` (`74245a8d…`, égale à la table du brouillon), l. 70 à 92.
- **Non fait** : la suite complète d'essais ; aucune vérification de prix sur une page publique (aucun réseau) ; aucune cellule du collisionneur ouverte ; la carte des hypothèses v1 non ouverte.

## Verdict

**Scellable après corrections.** Le devis se recalcule à l'identique (trois scripts rejoués, trois sorties identiques octet pour octet ; chaque montant du texte retrouvé dans les sorties) et le texte respecte N12 (b). Mais **sept constats bloquants** touchent le dessin, la liste d'arrêt et la forme de la demande de GO ; ils se corrigent par **14 couples exacts** (C01 à C14, en fin de rapport, chacun trouvé une fois et une seule dans le brouillon, blancs normalisés, contrôle par programme) et par trois ajouts sans couple (CLP-07, CLP-10, CLP-12).

**Le GO de dépense du pilote ne peut pas se prendre sur ce texte** : le pilote est une expérience décisive (R1) et quatre pièces du préenregistrement n'existent pas encore (méthode d'intervalle, consignes du planteur et des bras, commit de Mathlib, script d'analyse). Ce qui peut se décider maintenant : D-1a (outillage, sans appel de modèle), D-2, D-3, D-4, D-5.

## Ce qui tient (vérifié)

1. **Rejeu des calculs** : `calculs_devis_essai_v3.py`, `option_pilote_reduit_v1.py`, `variantes_modele_bras_v1.py` relancés sous `.venv` (numpy 2.4.6, scipy 1.17.1) ; `diff` vide contre les trois sorties versées. Graines par `SeedSequence` (R9).
2. **Chiffres du texte contre les sorties** : effectifs du § 3.6 (39 à 193) ; probabilités d'issues citées (n = 100 et 150, discordance 0,30) ; borne des fausses alertes (0,972 ; 0,644 ; 0,175 ; 0,903 ; 0,982) ; coûts unitaires (1,12 ; 0,042 ; 1,162 ; 0,322 ; 0,052 ; 0,374 ; 0,18 ; 0,55 ; 0,26 ; 0,19) et pires cas ; pilote 311,86 et 1 428,92 ; confirmation 798,97 et 1 247,40 (pires 3 716,72 et 5 804,40) ; options 623,70, 3 118,50, 35,88 et 181,06, 219,98 ; variantes 198,32, 538,94, 522,11, 1 352,70, 814,80, 2 112,60 ; durées. Tous conformes. Arithmétique du texte : 450 + 1 400 + 50 = 1 900 ; attendu 1 110 à 1 560 ; −36 % et +73 % ; facteur 1,8 de D-4 (ii). Conformes.
3. **Prix et sources** : Opus 5.5 à 4 / 20 et lecture en cache à 0,20, Sonnet 5.5 à 2 / 10, Fable 5.2 à 8 / 40 : lus dans `shared/models.md` aux lignes citées ; Kimi K3.1 Pro 2 / 10 « vérifiés le 30 octobre », Gemini 4 Argon 10 / 50 « valeur volontairement haute », GPT-6 Astra 10 / 50 « SUPPOSÉS », identifiant « à confirmer » : lus dans `collisionneur_v8.py` aux lignes citées. Chaque prix non vérifié sur page publique est bien marqué « à vérifier ». Aucun chiffre de l'état de l'art (R7).
4. **N12 (b)** : aucune issue n'ouvre la couche 4 (O1 « pièce… n'ouvre rien », § 5) ; la suite n'est pas un standard (O3 « aucun statut de norme », § 5) ; le bornage à une classe est dit « choix de dessin proposé par ce brouillon, non une décision du directeur » (§ 0) ; l'essai n'est pas dit « sans dépense ». Conforme à la synthèse du tour 2, points (1) à (4).
5. **Dessin, points tenus par les espèces** : banque plantée par une troisième famille ; confirmation générée après le gel et le scellement du pilote ; contrôles de fidélité (classe K5, relecteur, audit sur l'énoncé imprimé par Lean) ; effectif réglé sur les paires discordantes ; même modèle, même effort, mêmes plafonds dans les deux bras ; exécution par paires complètes. Présents.
6. **Conflit du rédacteur (Opus 5.5)** : je n'ai trouvé aucun élément du dessin qui favorise ce modèle ; il est dans les deux bras, le choix se justifie par le coût, et les variantes sont chiffrées. Le biais que je relève est ailleurs : il penche vers le **bras formel** (CLP-01, CLP-02), non vers un modèle.
7. **Complétude R1** : question, hypothèses, prédictions chiffrées avec signe (P1 à P4), métriques, seuils, plan, issues écrites d'avance, liste d'arrêt : présents. Manquent les pièces de CLP-07.

## Constats

### Bloquants

**CLP-01 — La condition de O1 n'établit pas ce que sa lecture annonce, et la règle penche vers le gain.** O1 exige « borne basse > 0 et estimation ≥ δ », et se lit « détecte au moins δ de plus ». Or les hypothèses du § 1.3 sont Δ ≥ δ contre Δ < δ. La condition de rappel sort environ une fois sur deux à la frontière, et encore de 0,14 à 0,31 pour un Δ vrai de 0,15, de 0,02 à 0,13 pour 0,10 (annexe, bloc A ; aussi lisible dans la sortie v3 du rédacteur). En face, O3 exige que tout l'intervalle soit sous δ et ne se trompe qu'environ trois fois sur cent à la frontière. Les deux issues ne sont pas tenues au même niveau de preuve : la phrase « la règle ne penche pas vers le gain » (§ 1.7) est fausse en ce sens (R3, R4). La variante stricte (borne basse ≥ δ) ne sort qu'à 0,41 à 0,73 pour un Δ vrai de 0,30 : je ne l'impose pas, je demande que la lecture dise ce qui est établi. Couples C01, C02.

**CLP-02 — Le rappel seul se confond avec le point de fonctionnement ; la règle de choix des classes désigne la classe où Lean échoue à formaliser.** Dans le bras formel, « je n'ai pas su prouver » et « c'est faux » donnent le même verdict. Un bras qui rejette au hasard une part q des items gagne q × (1 − rappel) de rappel sans rien détecter : pour une suite à 0,40 de rappel et q = 0,25, le gain apparent est de 0,15, proche de δ, avec des fausses alertes encore sous φ_max = 0,30 (annexe, bloc B). Le brouillon nomme le piège (§ 1.2) mais ne le ferme que pour O2 ; O1 peut donc sortir d'un simple écart de fausses alertes. De plus, le § 3.6 choisit les classes de confirmation par Δ̂_k brut : c'est le critère que les échecs de formalisation gonflent le plus. Couples C01 (lecture obligatoire étendue à O1) et C03 (choix sur l'écart « rappel moins fausses alertes » par classe, possible puisque chaque jumelle saine sort d'une graine de classe connue).

**CLP-03 — La séquence fixe ne contrôle pas l'erreur de famille.** Le brouillon demandait la vérification par simulation ; je l'ai faite (annexe, bloc A). La porte « classe 2 confirmatoire si la classe 1 a rendu O1, O2 ou O3 » laisse passer la classe 2 presque toujours, puisque « sous le seuil » est une issue conclusive : la probabilité d'au moins un faux « gain » est au-dessus de celle d'une classe seule dans toutes les cases (par exemple 0,231 contre 0,196 à n = 100, discordance 0,30, Δ vrai 0,15). Couple C04 (deux classes lues à 97,5 %, sans porte ; effectif central à refaire). Autre voie admissible : écrire qu'aucun contrôle de famille n'est revendiqué et que chaque classe se lit seule ; elle doit alors être dite dans D-5.

**CLP-04 — Cloison et secrets : les deux outils exécutent du code écrit par un modèle.** `python(code)` (bras S) est prévu « en bac à sable sans réseau » avec les paquets de `.venv`, donc sur ce conteneur, qui porte le dépôt de travail (chemins interdits compris) et les clés ; un fichier Lean peut lui aussi lire des fichiers et lancer des processus pendant sa compilation. Rien dans le brouillon n'interdit à un agent des bras d'ouvrir un chemin cloisonné ou une clé. Ce point pèse plus que le disque dans D-2. Couple C05 ; garde à ajouter à A1 et à éprouver (R5).

**CLP-05 — La nature de la dépense dépasse les mots de la décision.** R-959 autorise un essai sur processeur avec un « devis d'appels de sous-agents ». Le brouillon recommande des appels d'interface au jeton chez quatre fournisseurs et une machine louée, et écarte les sous-agents (§ 4.5, mode M2) ; la raison est bonne (coût par item mesurable, modèle épinglé), mais elle est rangée dans une section technique, pas dans une décision. GPT-6 Astra n'a ni identifiant ni accès confirmés, et aucun repli n'est écrit si le planteur manque. Lazar doit l'accorder en le sachant. Couple C06.

**CLP-06 — Lignes absentes du devis ; coupure A7 trop étroite.** Non chiffrés : le planteur des 10 témoins et des 10 renotations bis ; l'adjudication à l'aveugle (§ 2.5) ; l'audit étendu « à toutes les acceptations » de l'audit de symétrie (§ 1.8) ; la banque refaite une fois (§ 2.5, A6) ; le rejet de graines entre 20 % et 50 % (A5). Avec elles, l'attendu du pilote va d'environ 332 à 450, donc jusqu'au plafond (annexe, bloc E) ; en confirmation, la banque refaite seule vaut 187 à 292 attendus. A7 ne compte que « la paire suivante » : avec trois processus Lean et quatre de la suite en parallèle, et des appels hors paires, le plafond peut être dépassé. Le plafond de la phase 2 (1 400) ne laisse que 12 % de marge sur l'attendu au plafond d'effectif (1 247,40), contre 44 % au pilote. Couples C07, C08 ; le devis 2 reprend les mêmes lignes.

**CLP-07 — Le texte n'est pas encore un préenregistrement complet (R1), et le pilote en exige un.** Manquent : la méthode d'intervalle (le brouillon la choisit « aux effectifs et discordances du pilote », donc après des données : couple C09) ; la consigne du planteur et le tronc de consigne des bras ; le commit de Mathlib ; le script d'analyse scellé ; les gardes éprouvées. Le brouillon le dit lui-même (§ 8), mais D-1 demande d'un bloc « outillage et pilote ». Couple C06 (scission D-1a, D-1b). Sans couple : la table des empreintes renvoie aux chemins du bac à sable du rédacteur ; la version scellée doit citer les copies versées sous `calculs-v1/` (mêmes empreintes, vérifié), et « Fable 5.1 » doit y devenir le modèle qui a réellement contre-lu.

### Non bloquants

**CLP-08 — Effectif des saines et écart entre A9 et φ_max.** « saines = n_1 + n_2 (192 à 300) » est inexact : la règle donne 80 à 300 (annexe, bloc C : 114 saines pour 6 discordantes sur 60). Sous 200 saines la condition des fausses alertes est faible (0,644 à 120 saines pour φ = 0,20, sortie v3). Par ailleurs le pilote ne s'arrête qu'à φ̂_L > 0,60 alors que O1 exige une borne haute sous 0,30 : entre les deux, la confirmation coûte 800 à 1 250 USD sans pouvoir rendre O1. Ce n'est pas une raison d'arrêter (O2, O3 restent lisibles), mais le second GO doit le savoir. Couples C10, C11.

**CLP-09 — Le profil de coût de l'agent formel est optimiste.** 30 k de sortie pour vingt tours, raisonnement compris (non désactivable sur Opus 5.5 selon la référence locale), c'est 1,5 k par tour avec un fichier Lean réécrit à chaque tour. À 60 k de sortie l'item vaut 1,76 ; à 1 000 k d'entrée et 100 k de sortie 3,08 ; sans cache 2,64 (annexe, bloc D). La prédiction P4 ([2 ; 6]) serait démentie dès le deuxième cas. A8 protège le plafond (42 graines payables dans le troisième cas, arrêt sous 40). L'effet de dessin est plus sérieux que l'effet de budget : un plafond souvent atteint par le seul bras L gonfle son rappel et ses fausses alertes (même mécanisme que CLP-02). Couple C12. À vérifier aussi : la durée de vie du cache (cinq minutes pour l'écriture citée) contre le délai d'une compilation.

**CLP-10 — Prix : trois précisions, sans couple.** (a) Le multiplicateur d'écriture en cache (1,25) n'est pas sur la ligne citée pour Opus 5.5 ; il est sur celle de Fable 5.2 (écriture à 10 pour 8). À marquer « à vérifier ». (b) La machine « ≤ 50 USD » n'a aucune source ni durée : le bras formel occupe 12 heures murales au pilote et 32 à 50 en confirmation, sur un calendrier de deux à trois semaines ; à chiffrer (prix horaire, durée allumée) avant D-2. (c) La variante par modèle applique un facteur global aux parts Opus : correct pour l'ordre de grandeur, les lectures en cache n'ayant pas le même rapport d'un modèle à l'autre.

**CLP-11 — Adjudicateur de la famille qui a validé les graines.** Risque réel, borné : il ne touche que l'analyse de sensibilité. Deux défauts restent. L'adjudication est déclenchée par le comportement des bras (saines alertées, fautives acceptées) : exclure les items réétiquetés retire surtout des désaccords, et rapproche mécaniquement les bras. Et rien ne mesure la tendance de l'adjudicateur à confirmer. Remèdes sans humain ni cinquième famille : un tirage d'items non litigieux dans le même lot ; un certificat mécanique pour les saines (acceptée par L avec énoncé fidèle à l'audit). Couple C13. Une adjudication humaine reste la meilleure voie, mais c'est un contact externe ou du temps de Lazar : à lui de dire.

**CLP-12 — Gardes du bras formel : compléments à étudier à l'outillage (à vérifier sur la chaîne installée, sans couple).** (a) Les gardes textuelles G-L3 ne couvrent pas les définitions, notations, instances ou macros locales, qui peuvent faire imprimer par `#check` un énoncé d'apparence fidèle sur des objets redéfinis ; soit les interdire, soit les faire imprimer au relecteur. (b) `#print axioms` et `#check` doivent être lancés par le harnais dans un fichier à lui qui importe celui de l'agent, non lus dans la sortie d'un fichier que l'agent contrôle. (c) Le délai mural de 30 minutes dépend de la charge (trois compilations sur quatre cœurs) : compter le temps de processus, ou fixer le parallélisme au préenregistrement, sinon le motif « délai » n'est pas reproductible. (d) Ajouter aux artefacts de R5 un énoncé d'étape à hypothèses contradictoires (étape prouvée à vide).

**CLP-13 — Symétrie de la règle du « ou ».** Elle est symétrique dans la forme (agent ou relecteur d'une autre famille), pas dans le contenu : le relecteur de la suite juge la justesse de la preuve, celui de la chaîne formelle seulement la fidélité, et la chaîne formelle a cinq motifs de refus de plus (gardes). C'est l'objet mesuré (chaîne complète) et le brouillon l'assume ; je ne demande rien, sinon que la décomposition des `NON-ACCEPTE` par motif (déjà secondaire, § 3.7) monte en tête du rapport avec la part des items au plafond.

**CLP-14 — La définition d'un item fautif exclut un terrain possible de la preuve formelle.** Le § 8 (point 8) demandait cette vérification. Les « bonnes assertions mal justifiées » sont exclues, et le squelette laisse prouver une étape vraie par n'importe quel chemin : l'essai ne peut donc pas voir une étape vraie que l'argument n'établit pas. L'exclusion est cohérente avec l'objet mesuré et ne favorise aucun bras à l'intérieur de la banque ; mais elle est une limite de portée, absente du § 5. Couple C14.

**CLP-15 — Écarts mineurs.** (a) Le « central 2 × 96 » n'est rendu par aucune ligne de la règle (99 pour 12 discordantes sur 60 ; 97 par la formule nue à 0,25) : dire d'où il vient. (b) `option_pilote_reduit_v1.py` et `variantes_modele_bras_v1.py` reprennent des coûts unitaires arrondis à la main depuis la sortie v3 : sans effet visible, mais à dériver par import à la prochaine version. (c) Un commentaire du script v3 dit l'audit « sur les acceptations de la chaîne formelle » ; le calcul et le texte prennent une part de tous les items. (d) Le § 6, point 1 (« prématuré », « l'issue O0 répondrait déjà ») anticipe la note (c) ; c'est marqué « proposé par le rédacteur », je le laisse. (e) Le plafond de 60 USD de D-6 n'est pas dans l'engagement maximal de 1 900.

## Avis sur les décisions

- **D-1** : ne pas l'accorder d'un bloc. **D-1a** (outillage, aucun appel de modèle) peut partir ; **D-1b** (pilote, plafond 450) après préenregistrement complet, contre-lu et scellé, et en ayant accordé la nature de la dépense (CLP-05). Le plafond de 450 tient grâce à A8, mais l'attendu réel est plutôt 330 à 450 (CLP-06, CLP-09). Je ne recommande pas le pilote réduit (ii) : huit items par classe ne portent pas un choix de classes.
- **D-2** : **(i) machine dédiée**, et d'abord pour la cloison (CLP-04), non pour le disque. Condition : aucune clé ni dépôt sur cette machine ; coût à chiffrer (CLP-10 b). L'option (ii) n'est acceptable que dans un conteneur sans accès au dépôt.
- **D-3** : **(a)**, d'accord ; aucun avantage indu à Opus 5.5. Réserves : repli à écrire si GPT-6 Astra n'est pas joignable ; adjudicateur à contrôler (CLP-11). Sonnet 5.5 abaisserait le coût mais rendrait O0 plus probable pour une raison de modèle, non d'outil ; Fable 5.2 ne se justifie pas au prix.
- **D-4** : **(i) δ = 0,20, φ_max = 0,30**, sous condition de C01 et C02. À dire à Lazar : avec la prédiction du rédacteur (fausses alertes de la chaîne formelle supérieures d'au moins 0,15), O1 est presque hors d'atteinte ; φ_max décide autant que δ.
- **D-5** : **(i) amendée** : choix des classes sur l'écart « rappel moins fausses alertes » (C03), deux classes à 97,5 % sans porte (C04), ce qui renchérit le devis central. Variante à lui proposer : classe 1 fixée d'avance à K1 (ancrée dans l'expérience du programme, position de l'espèce A), classe 2 choisie par le pilote.
- **D-6** : **non pour l'instant** (c'est le défaut). La carte v1 n'est pas sur `main`, attend des corrections, et ses lemmes n'ont pas d'étiquette. À reposer après le pilote, sur la carte corrigée.

## Points ouverts

1. Modèle du contre-lecteur : Fable 5.2 au lieu du Fable 5.1 nommé par N-052 et par le brouillon ; à la mère de dire si une seconde contre-lecture est requise.
2. Prix publics, identifiants et accès (Opus 5.5, GPT-6 Astra, Gemini 4 Argon), taille de Mathlib, prix de la machine : toujours « à vérifier », aucun réseau ici.
3. Le coût des sous-agents de la session (outillage, contre-lectures, verdict) est-il une dépense au sens du programme ? Question du brouillon (§ 8, point 5), que je ne peux pas trancher.
4. C04 change l'effectif central : le rédacteur doit refaire le calcul par script (nouvelle version nommée) avant le brouillon 2.
5. Une vérification courte du brouillon 2 par un sous-agent neuf suffit si les 14 couples sont appliqués tels quels ; une contre-lecture entière si la voie de CLP-03 ou de CLP-02 est changée.

## Exposition, cloison, interdits

Aucun chemin des interdits communs ouvert (rien sous `diag/`, `runs/`, `donnees/`, `docs/notes/bras-attaque/`, aucune branche, aucune cellule du collisionneur). Aucune recherche récursive : lectures de fichiers nommés, `grep` et `sed` sur des fichiers nommés, `ls` de dossiers nommés. Aucun appel de modèle ni d'interface, aucun réseau, aucune installation, aucune dépense, aucune commande git d'écriture (un `git status` a été lancé, sans sortie). Aucun refus de contrôle de permissions ni de classifieur. Aucune valeur de sonde de la course 7a sous mes yeux. Écrit : ce fichier et son compagnon, rien d'autre ; bac à sable vidé (le script de vérification est recopié en annexe pour survivre au bac, R6).

---

## Couples exacts (blancs et retours à la ligne normalisés ; unicité contrôlée par programme)

**C01** (CLP-01) — occurrences dans le brouillon : 1

- À remplacer :

  > la chaîne formelle détecte sur la classe k au moins δ de plus que la suite, à fausses alertes bornées.

- Par :

  > la chaîne formelle détecte sur la classe k strictement plus que la suite (borne basse au-dessus de zéro), avec une estimation ponctuelle d'au moins δ, à fausses alertes bornées. « Au moins δ » n'est dit établi que si B(Δ_k) ≥ δ (sous-cas O1a) ; sinon l'issue se lit « gain positif établi, ampleur non établie » (sous-cas O1b). **Lecture obligatoire, comme pour O2, avec le rappel conditionnel aux paires formalisables et avec la différence appariée des écarts « rappel moins fausses alertes »** : si l'une des deux est nulle ou négative, le rapport le dit en tête.

**C02** (CLP-01) — occurrences dans le brouillon : 1

- À remplacer :

  > (0,52 à 0,55) : la règle ne penche pas vers le gain.

- Par :

  > (0,52 à 0,55), alors que « sous le seuil » n'y sort qu'environ trois fois sur cent : la condition de rappel de O1 n'établit donc pas Δ ≥ δ, elle établit Δ > 0 avec une estimation d'au moins δ ; pour un Δ vrai de 0,15 elle sort encore de 0,14 à 0,31 selon l'effectif et la discordance (contre-lecture 1, annexe, bloc A). C'est pourquoi O1 distingue O1a et O1b.

**C03** (CLP-02) — occurrences dans le brouillon : 1

- À remplacer :

  > classes rangées par Δ̂_k du pilote, décroissant (ex æquo départagés par la graine)

- Par :

  > classes rangées, par ordre décroissant, selon la différence appariée des écarts « rappel moins fausses alertes » du pilote, (r̂_L,k − φ̂_L,k) − (r̂_S,k − φ̂_S,k), les fausses alertes d'une classe étant lues sur les jumelles saines des graines de cette classe (ex æquo départagés par la graine) ; le rang par Δ̂_k seul est rapporté à côté, sans servir au choix : il désignerait la classe où la chaîne formelle échoue le plus à formaliser (piège du § 1.2)

**C04** (CLP-03) — occurrences dans le brouillon : 1

- À remplacer :

  > la classe 2 n'est lue de façon confirmatoire que si la classe 1 a rendu O1, O2 ou O3 ; sinon elle est rapportée comme exploratoire. Contrôle de l'erreur de famille **à vérifier par simulation** avant scellement (contre-lecture).

- Par :

  > les deux classes sont lues chacune avec des intervalles à 97,5 % bilatéraux (Bonferroni sur deux classes), sans porte entre elles ; la règle d'effectif s'écrit alors avec 2,24 au lieu de 1,96 (environ 1,31 fois plus de graines à discordance égale, plafond de 150 inchangé ; devis central à refaire). La porte « classe 1 conclusive » de la version précédente ne contrôlait pas l'erreur de famille : elle ouvrait la classe 2 dès que la classe 1 rendait « sous le seuil » (contre-lecture 1, annexe, bloc A).

**C05** (CLP-04) — occurrences dans le brouillon : 1

- À remplacer :

  > - **Garde de calcul** : toute machine louée cite un GO valide

- Par :

  > - **Isolement des outils (cloison et secrets)** : `lean_verifier` et `python(code)` exécutent du code écrit par un modèle (un fichier Lean peut lire des fichiers et lancer des processus pendant sa compilation) ; ils ne tournent que sur une machine ou dans un conteneur qui ne contient ni le dépôt de travail, ni aucune clé, et sans réseau sortant ; le harnais, qui porte les clés, reste hors de cet environnement et n'y envoie que le fichier à vérifier ou le code à exécuter. Garde éprouvée sur un cas sain et sur un artefact (lecture d'un fichier hors du bac, appel réseau) avant tout lancement (R5 ; ajoutée à A1).
  > - **Garde de calcul** : toute machine louée cite un GO valide

**C06** (CLP-05 et CLP-07) — occurrences dans le brouillon : 1

- À remplacer :

  > Enjeu : seul pas autorisé par N12 (b) ; sans lui, (b) s'arrête au devis.

- Par :

  > Enjeu : seul pas autorisé par N12 (b) ; sans lui, (b) s'arrête au devis. **Nature de la dépense, à accorder explicitement** : R-959 parle d'un « devis d'appels de sous-agents » ; ce devis demande autre chose, des appels d'interface au jeton chez quatre fournisseurs (dont GPT-6 Astra, identifiant et accès non confirmés : nœud de compte, avec un repli à écrire) et, selon D-2, une machine louée. **Ordre** : le pilote est une expérience décisive (viabilité A9, choix des classes) ; son GO ne se prend qu'après le scellement du préenregistrement complet (méthode d'intervalle, consignes du planteur et des bras, commit de Mathlib, script d'analyse, gardes éprouvées), qui exige l'outillage. D-1 se scinde donc en **D-1a** (outillage : aucun appel de modèle facturé, machine selon D-2) et **D-1b** (pilote, après scellement et contre-lecture).

**C07** (CLP-06) — occurrences dans le brouillon : 1

- À remplacer :

  > **A7** dépense de la phase + pire cas de la paire suivante > plafond de la phase ⇒ plus aucun lancement (paires complètes).

- Par :

  > **A7** dépense de la phase + pire cas de tous les appels en cours (paires lancées en parallèle comprises) + pire cas du prochain appel, quel qu'il soit (paire, planteur, contrôle des graines, lecture nue, audit, adjudication) > plafond de la phase ⇒ plus aucun lancement (paires complètes).

**C08** (CLP-06) — occurrences dans le brouillon : 1

- À remplacer :

  > **Plafond proposé de la phase 1 : 450 USD** d'appels (coupures A7 et A8 : la dépense ne peut pas le dépasser ;

- Par :

  > **Lignes absentes du tableau, comprises dans le plafond** (contre-lecture 1, annexe, bloc E ; mêmes prix et profils) : planteur des 10 témoins et des 10 renotations bis (≈ 11) ; adjudication à l'aveugle (≈ 9 à 19 selon la part d'items litigieux) ; audit étendu à tous les items si l'audit de symétrie du § 1.8 se déclenche (≈ 11) ; banque refaite une fois si le classifieur de style dépasse 0,70 (≈ 58) ; graines rejetées jusqu'à 50 % avant A5 (≈ 39). Avec elles l'attendu du pilote va d'environ 332 à 450, c'est-à-dire jusqu'au plafond ; les mêmes lignes sont à ajouter au devis 2.
  > 
  > **Plafond proposé de la phase 1 : 450 USD** d'appels (coupures A7 et A8 : la dépense ne peut pas le dépasser ;

**C09** (CLP-07) — occurrences dans le brouillon : 1

- À remplacer :

  > par simulation de couverture aux effectifs et discordances du pilote ;

- Par :

  > par simulation de couverture sur une grille fixée d'avance (effectifs de 40 à 150, discordances de 0,10 à 0,50), **avant le scellement et avant le pilote**, selon une règle écrite (la méthode dont la couverture minimale sur la grille est la plus proche de la couverture nominale par le haut) ;

**C10** (CLP-08) — occurrences dans le brouillon : 1

- À remplacer :

  > saines = n_1 + n_2 (192 à 300).

- Par :

  > saines = n_1 + n_2 (80 à 300 selon la règle ; 192 à 300 aux effectifs du devis). Si n_1 + n_2 < 200, la condition H(φ_L) ≤ φ_max est sous-dimensionnée (borne des fausses alertes, ci-dessus) : la fiche de passage le dit, avec la probabilité calculée.

**C11** (CLP-08) — occurrences dans le brouillon : 1

- À remplacer :

  > **A9** viabilité, fin du pilote : φ̂_L > 0,60 ⇒ O0 et pas de confirmation ;

- Par :

  > **A9** viabilité, fin du pilote : φ̂_L > 0,60 ⇒ O0 et pas de confirmation ; si la borne basse à 95 % (Clopper–Pearson) de φ_L au pilote dépasse φ_max, la fiche de passage écrit que O1 est hors d'atteinte en confirmation (restent O2, O3, O4) et le second GO se prend en le sachant ;

**C12** (CLP-09) — occurrences dans le brouillon : 1

- À remplacer :

  > Rapport attendu des coûts par item L/S : **3,11** (prédiction P4 : entre 2 et 6).

- Par :

  > Rapport attendu des coûts par item L/S : **3,11** (prédiction P4 : entre 2 et 6). **Sensibilité** (contre-lecture 1, annexe, bloc D) : le profil de l'agent L est la supposition qui pèse le plus ; à 60 k de sortie l'item L vaut 1,76 (rapport 4,7) ; à 1 000 k d'entrée et 100 k de sortie, 3,08 (rapport 8,2 ; pilote ramené à 42 graines par A8) ; sans cache, 2,64. Au-delà, l'item touche le plafond de 4 USD, et le plafond devient un motif fréquent de `NON-ACCEPTE` du seul bras L, ce qui gonfle à la fois son rappel et ses fausses alertes : la part des items au plafond, par bras, est une mesure de tête.

**C13** (CLP-11) — occurrences dans le brouillon : 1

- À remplacer :

  > est soumise à l'adjudicateur (même famille que le contrôle des graines), **sans savoir quel bras a alerté**

- Par :

  > est soumise à l'adjudicateur (même famille que le contrôle des graines : il peut tendre à confirmer des étiquettes de sa propre famille ; pour le mesurer, un tirage de 20 items non litigieux lui est soumis dans le même lot, sans marque, et son taux de confirmation y est rapporté à côté de celui des litigieux ; une saine acceptée par L avec un énoncé jugé fidèle à l'audit garde son étiquette sans adjudication), **sans savoir quel bras a alerté**

**C14** (CLP-14) — occurrences dans le brouillon : 1

- À remplacer :

  > - **les erreurs de spécification empirique** : une preuve ne valide pas une spécification empirique (D ; MAT-004) ;

- Par :

  > - **les erreurs de spécification empirique** : une preuve ne valide pas une spécification empirique (D ; MAT-004) ;
  > - **les lacunes de justification** : les assertions vraies mal justifiées sont exclues de la banque (§ 2.2) et le squelette laisse prouver chaque étape par n'importe quel chemin ; l'essai ne dit donc rien d'une étape vraie que l'argument écrit n'établit pas, cas où une vérification de l'argument lui-même pourrait avoir un avantage ;

<!-- controle : 14 couples, 0 défaut(s) d'unicité -->

---

## Annexe — vérifications du contre-lecteur (script rejouable et sortie ; aucun appel, aucun réseau)

Script `verif_cl1_v1.py` (empreinte à l'exécution : `4645c72fdf1e52ba1fa27519df010b26eef85dfbbcc55cd107f770f585648b26`), lancé par `.venv/bin/python` depuis la racine du dépôt ; sortie (`0ab5aea104e464100d288ee95cdebf9dd8884da1210e79e912f8d4991e03b556`) recopiée telle quelle.

```python
"""Vérifications du contre-lecteur (CL1) — aucun appel, aucun réseau. Graines SeedSequence (R9)."""
import math, numpy as np
from scipy import stats
ss = np.random.SeedSequence(2026111001)
r1, r2 = [np.random.default_rng(s) for s in ss.spawn(2)]
Z = stats.norm.ppf(0.975); DELTA = 0.20; REPS = 40000
def issue(n10, n01, n):
    a10, a01, m = n10 + .5, n01 + .5, n + 2.
    d = (a10 - a01) / m; v = ((a10 + a01) / m - d * d) / m; h = Z * np.sqrt(np.maximum(v, 0))
    est = (n10 - n01) / n; lb, ub = d - h, d + h
    gain = (lb > 0) & (est >= DELTA); sous = ub < DELTA
    return gain, sous
def tir(rng, n, disc, dv):
    t = rng.multinomial(n, [(disc + dv) / 2, (disc - dv) / 2, 1 - disc], size=REPS)
    return issue(t[:, 0], t[:, 1], n)
print("== (A) séquence fixe du § 3.6 : classe 2 confirmatoire si classe 1 conclusive (gain ou sous le seuil)")
for n in (60, 100, 150):
    for disc in (0.30, 0.40):
        for dv in (0.0, 0.10, 0.15, 0.19):
            g1, s1 = tir(r1, n, disc, dv); g2, s2 = tir(r1, n, disc, dv)
            concl1 = g1 | s1
            fam = np.mean(g1 | (concl1 & g2))
            print(f"  n={n} disc={disc} delta vrai={dv:.2f} (< delta dans les deux classes) : faux « gain » classe 1 {g1.mean():.3f} ; "
                  f"au moins un faux « gain » confirmatoire {fam:.3f} ; sans porte {np.mean(g1|g2):.3f}")
        g1, s1 = tir(r1, n, disc, 0.20); g2, s2 = tir(r1, n, disc, 0.20)
        print(f"  n={n} disc={disc} delta vrai=0.20 (= delta) : faux « sous le seuil » classe 1 {s1.mean():.3f} ; au moins un {np.mean(s1 | ((g1|s1) & s2)):.3f}")
print("\n== (A') variante stricte de O1 : borne basse >= delta (au lieu de borne basse > 0 et estimation >= delta)")
for n in (100, 150):
    for disc in (0.30, 0.40):
        for dv in (0.20, 0.30):
            t = r2.multinomial(n, [(disc + dv) / 2, (disc - dv) / 2, 1 - disc], size=REPS)
            a10, a01, m = t[:, 0] + .5, t[:, 1] + .5, n + 2.
            d = (a10 - a01) / m; v = ((a10 + a01) / m - d * d) / m; lb = d - Z * np.sqrt(np.maximum(v, 0))
            print(f"  n={n} disc={disc} delta vrai={dv:.2f} : P(borne basse >= delta) = {np.mean(lb >= DELTA):.3f}")
print("\n== (B) point de fonctionnement : rejet au hasard d'une part q des items (sans rien détecter)")
for rS in (0.4, 0.6, 0.8):
    for q in (0.10, 0.20, 0.25, 0.30):
        print(f"  rappel de base {rS:.1f}, rejet aveugle q={q:.2f} : rappel {rS + q * (1 - rS):.3f} (gain apparent {q * (1 - rS):+.3f}), fausses alertes +{q:.2f}")
print("\n== (C) règle d'effectif : d+ = borne haute unilatérale 80 % (Clopper-Pearson) sur 60 fautives")
for x in (6, 9, 12, 15, 18, 21, 24):
    dp = stats.beta.ppf(0.80, x + 1, 60 - x); nk = min(150, max(40, math.ceil(Z ** 2 * dp / 0.01)))
    print(f"  {x}/60 discordantes (d={x/60:.2f}) : d+={dp:.3f} -> n_k={nk} ; deux classes : {2*nk} graines, {2*nk} saines")
print("\n== (D) sensibilité du coût de l'agent L (Opus 5.5 4/20 ; cache 85 % lu à 0,1x, 10 % écrit à 1,25x)")
def cout(e, s, pc=.85, pw=.10, pe=4., ps=20.):
    return (e * (1 - pc - pw) * pe + e * pc * pe * .1 + e * pw * pe * 1.25 + s * ps) / 1e6
attS, nue, audit, plant = 0.374, 0.18, 0.19, 72 * (0.55 + 0.26)
for e, s in ((500e3, 30e3), (500e3, 60e3), (1e6, 60e3), (1e6, 100e3), (1.5e6, 120e3)):
    c = cout(*((e, s) if len((e, s)) == 2 else (e, s)))
    L = min(4.0, c + 0.042)
    pil = plant + 140 * (L + attS + nue) + 70 * audit
    par_graine = 2 * (L + attS + nue) + audit
    print(f"  entrée {e/1e3:.0f} k, sortie {s/1e3:.0f} k : agent L {c:.2f} ; item L {L:.2f} ; rapport L/S {L/attS:.1f} ; pilote 140 items {pil:.0f} ; "
          f"graines payables sous 450 après témoins : {int((450 - plant - 20*(L+attS+nue) - 10*audit) // par_graine)}")
print(f"  sans cache du tout (500 k, 30 k) : agent L {cout(500e3, 30e3, 0, 0):.2f}")
print("\n== (E) lignes absentes du devis (prix Argon 10/50, profils du brouillon)")
adj = cout(6e3, 4e3, 0, 0, 10., 50.)
for nom, items in (("pilote", 120), ("confirmation centrale", 384), ("confirmation plafond", 600)):
    for part in (0.3, 0.6):
        print(f"  adjudication à l'aveugle, {nom}, {part:.0%} d'items litigieux à {adj:.2f} : {items * part * adj:.2f}")
    reste = {"pilote": 0.5, "confirmation centrale": 0.7, "confirmation plafond": 0.7}[nom]
    print(f"  audit étendu à tous les items (§ 1.8), {nom} : +{items * reste * 0.19:.2f} attendu, +{items * reste * 0.46:.2f} pire")
for nom, g in (("pilote", 72), ("confirmation centrale", 231), ("confirmation plafond", 360)):
    print(f"  banque refaite une fois (A6), {nom} : +{g * 0.81:.2f} attendu, +{g * 2.56:.2f} pire ; rejet de 50 % des graines (A5) au lieu de 20 % : +{(g/1.2*2 - g) * 0.81:.2f}")
print(f"  planteur pour 10 témoins et 10 renotations bis : +{20 * 0.55:.2f} attendu, +{20 * 1.68:.2f} pire")
```

Sortie :

```text
== (A) séquence fixe du § 3.6 : classe 2 confirmatoire si classe 1 conclusive (gain ou sous le seuil)
  n=60 disc=0.3 delta vrai=0.00 (< delta dans les deux classes) : faux « gain » classe 1 0.003 ; au moins un faux « gain » confirmatoire 0.006 ; sans porte 0.007
  n=60 disc=0.3 delta vrai=0.10 (< delta dans les deux classes) : faux « gain » classe 1 0.096 ; au moins un faux « gain » confirmatoire 0.126 ; sans porte 0.181
  n=60 disc=0.3 delta vrai=0.15 (< delta dans les deux classes) : faux « gain » classe 1 0.269 ; au moins un faux « gain » confirmatoire 0.305 ; sans porte 0.467
  n=60 disc=0.3 delta vrai=0.19 (< delta dans les deux classes) : faux « gain » classe 1 0.488 ; au moins un faux « gain » confirmatoire 0.512 ; sans porte 0.741
  n=60 disc=0.3 delta vrai=0.20 (= delta) : faux « sous le seuil » classe 1 0.035 ; au moins un 0.055
  n=60 disc=0.4 delta vrai=0.00 (< delta dans les deux classes) : faux « gain » classe 1 0.010 ; au moins un faux « gain » confirmatoire 0.016 ; sans porte 0.018
  n=60 disc=0.4 delta vrai=0.10 (< delta dans les deux classes) : faux « gain » classe 1 0.126 ; au moins un faux « gain » confirmatoire 0.159 ; sans porte 0.237
  n=60 disc=0.4 delta vrai=0.15 (< delta dans les deux classes) : faux « gain » classe 1 0.306 ; au moins un faux « gain » confirmatoire 0.338 ; sans porte 0.516
  n=60 disc=0.4 delta vrai=0.19 (< delta dans les deux classes) : faux « gain » classe 1 0.493 ; au moins un faux « gain » confirmatoire 0.511 ; sans porte 0.742
  n=60 disc=0.4 delta vrai=0.20 (= delta) : faux « sous le seuil » classe 1 0.029 ; au moins un 0.045
  n=100 disc=0.3 delta vrai=0.00 (< delta dans les deux classes) : faux « gain » classe 1 0.000 ; au moins un faux « gain » confirmatoire 0.000 ; sans porte 0.000
  n=100 disc=0.3 delta vrai=0.10 (< delta dans les deux classes) : faux « gain » classe 1 0.040 ; au moins un faux « gain » confirmatoire 0.059 ; sans porte 0.078
  n=100 disc=0.3 delta vrai=0.15 (< delta dans les deux classes) : faux « gain » classe 1 0.196 ; au moins un faux « gain » confirmatoire 0.231 ; sans porte 0.354
  n=100 disc=0.3 delta vrai=0.19 (< delta dans les deux classes) : faux « gain » classe 1 0.460 ; au moins un faux « gain » confirmatoire 0.482 ; sans porte 0.706
  n=100 disc=0.3 delta vrai=0.20 (= delta) : faux « sous le seuil » classe 1 0.034 ; au moins un 0.052
  n=100 disc=0.4 delta vrai=0.00 (< delta dans les deux classes) : faux « gain » classe 1 0.001 ; au moins un faux « gain » confirmatoire 0.002 ; sans porte 0.002
  n=100 disc=0.4 delta vrai=0.10 (< delta dans les deux classes) : faux « gain » classe 1 0.065 ; au moins un faux « gain » confirmatoire 0.089 ; sans porte 0.125
  n=100 disc=0.4 delta vrai=0.15 (< delta dans les deux classes) : faux « gain » classe 1 0.228 ; au moins un faux « gain » confirmatoire 0.259 ; sans porte 0.408
  n=100 disc=0.4 delta vrai=0.19 (< delta dans les deux classes) : faux « gain » classe 1 0.465 ; au moins un faux « gain » confirmatoire 0.484 ; sans porte 0.715
  n=100 disc=0.4 delta vrai=0.20 (= delta) : faux « sous le seuil » classe 1 0.030 ; au moins un 0.044
  n=150 disc=0.3 delta vrai=0.00 (< delta dans les deux classes) : faux « gain » classe 1 0.000 ; au moins un faux « gain » confirmatoire 0.000 ; sans porte 0.000
  n=150 disc=0.3 delta vrai=0.10 (< delta dans les deux classes) : faux « gain » classe 1 0.015 ; au moins un faux « gain » confirmatoire 0.024 ; sans porte 0.029
  n=150 disc=0.3 delta vrai=0.15 (< delta dans les deux classes) : faux « gain » classe 1 0.138 ; au moins un faux « gain » confirmatoire 0.170 ; sans porte 0.255
  n=150 disc=0.3 delta vrai=0.19 (< delta dans les deux classes) : faux « gain » classe 1 0.436 ; au moins un faux « gain » confirmatoire 0.459 ; sans porte 0.679
  n=150 disc=0.3 delta vrai=0.20 (= delta) : faux « sous le seuil » classe 1 0.031 ; au moins un 0.048
  n=150 disc=0.4 delta vrai=0.00 (< delta dans les deux classes) : faux « gain » classe 1 0.000 ; au moins un faux « gain » confirmatoire 0.000 ; sans porte 0.000
  n=150 disc=0.4 delta vrai=0.10 (< delta dans les deux classes) : faux « gain » classe 1 0.028 ; au moins un faux « gain » confirmatoire 0.043 ; sans porte 0.058
  n=150 disc=0.4 delta vrai=0.15 (< delta dans les deux classes) : faux « gain » classe 1 0.178 ; au moins un faux « gain » confirmatoire 0.209 ; sans porte 0.324
  n=150 disc=0.4 delta vrai=0.19 (< delta dans les deux classes) : faux « gain » classe 1 0.443 ; au moins un faux « gain » confirmatoire 0.462 ; sans porte 0.691
  n=150 disc=0.4 delta vrai=0.20 (= delta) : faux « sous le seuil » classe 1 0.029 ; au moins un 0.043

== (A') variante stricte de O1 : borne basse >= delta (au lieu de borne basse > 0 et estimation >= delta)
  n=100 disc=0.3 delta vrai=0.20 : P(borne basse >= delta) = 0.018
  n=100 disc=0.3 delta vrai=0.30 : P(borne basse >= delta) = 0.532
  n=100 disc=0.4 delta vrai=0.20 : P(borne basse >= delta) = 0.023
  n=100 disc=0.4 delta vrai=0.30 : P(borne basse >= delta) = 0.406
  n=150 disc=0.3 delta vrai=0.20 : P(borne basse >= delta) = 0.018
  n=150 disc=0.3 delta vrai=0.30 : P(borne basse >= delta) = 0.730
  n=150 disc=0.4 delta vrai=0.20 : P(borne basse >= delta) = 0.021
  n=150 disc=0.4 delta vrai=0.30 : P(borne basse >= delta) = 0.561

== (B) point de fonctionnement : rejet au hasard d'une part q des items (sans rien détecter)
  rappel de base 0.4, rejet aveugle q=0.10 : rappel 0.460 (gain apparent +0.060), fausses alertes +0.10
  rappel de base 0.4, rejet aveugle q=0.20 : rappel 0.520 (gain apparent +0.120), fausses alertes +0.20
  rappel de base 0.4, rejet aveugle q=0.25 : rappel 0.550 (gain apparent +0.150), fausses alertes +0.25
  rappel de base 0.4, rejet aveugle q=0.30 : rappel 0.580 (gain apparent +0.180), fausses alertes +0.30
  rappel de base 0.6, rejet aveugle q=0.10 : rappel 0.640 (gain apparent +0.040), fausses alertes +0.10
  rappel de base 0.6, rejet aveugle q=0.20 : rappel 0.680 (gain apparent +0.080), fausses alertes +0.20
  rappel de base 0.6, rejet aveugle q=0.25 : rappel 0.700 (gain apparent +0.100), fausses alertes +0.25
  rappel de base 0.6, rejet aveugle q=0.30 : rappel 0.720 (gain apparent +0.120), fausses alertes +0.30
  rappel de base 0.8, rejet aveugle q=0.10 : rappel 0.820 (gain apparent +0.020), fausses alertes +0.10
  rappel de base 0.8, rejet aveugle q=0.20 : rappel 0.840 (gain apparent +0.040), fausses alertes +0.20
  rappel de base 0.8, rejet aveugle q=0.25 : rappel 0.850 (gain apparent +0.050), fausses alertes +0.25
  rappel de base 0.8, rejet aveugle q=0.30 : rappel 0.860 (gain apparent +0.060), fausses alertes +0.30

== (C) règle d'effectif : d+ = borne haute unilatérale 80 % (Clopper-Pearson) sur 60 fautives
  6/60 discordantes (d=0.10) : d+=0.147 -> n_k=57 ; deux classes : 114 graines, 114 saines
  9/60 discordantes (d=0.15) : d+=0.202 -> n_k=78 ; deux classes : 156 graines, 156 saines
  12/60 discordantes (d=0.20) : d+=0.256 -> n_k=99 ; deux classes : 198 graines, 198 saines
  15/60 discordantes (d=0.25) : d+=0.309 -> n_k=119 ; deux classes : 238 graines, 238 saines
  18/60 discordantes (d=0.30) : d+=0.361 -> n_k=139 ; deux classes : 278 graines, 278 saines
  21/60 discordantes (d=0.35) : d+=0.412 -> n_k=150 ; deux classes : 300 graines, 300 saines
  24/60 discordantes (d=0.40) : d+=0.463 -> n_k=150 ; deux classes : 300 graines, 300 saines

== (D) sensibilité du coût de l'agent L (Opus 5.5 4/20 ; cache 85 % lu à 0,1x, 10 % écrit à 1,25x)
  entrée 500 k, sortie 30 k : agent L 1.12 ; item L 1.16 ; rapport L/S 3.1 ; pilote 140 items 312 ; graines payables sous 450 après témoins : 98
  entrée 500 k, sortie 60 k : agent L 1.72 ; item L 1.76 ; rapport L/S 4.7 ; pilote 140 items 396 ; graines payables sous 450 après témoins : 71
  entrée 1000 k, sortie 60 k : agent L 2.24 ; item L 2.28 ; rapport L/S 6.1 ; pilote 140 items 469 ; graines payables sous 450 après témoins : 56
  entrée 1000 k, sortie 100 k : agent L 3.04 ; item L 3.08 ; rapport L/S 8.2 ; pilote 140 items 581 ; graines payables sous 450 après témoins : 42
  entrée 1500 k, sortie 120 k : agent L 3.96 ; item L 4.00 ; rapport L/S 10.7 ; pilote 140 items 709 ; graines payables sous 450 après témoins : 32
  sans cache du tout (500 k, 30 k) : agent L 2.60

== (E) lignes absentes du devis (prix Argon 10/50, profils du brouillon)
  adjudication à l'aveugle, pilote, 30% d'items litigieux à 0.26 : 9.36
  adjudication à l'aveugle, pilote, 60% d'items litigieux à 0.26 : 18.72
  audit étendu à tous les items (§ 1.8), pilote : +11.40 attendu, +27.60 pire
  adjudication à l'aveugle, confirmation centrale, 30% d'items litigieux à 0.26 : 29.95
  adjudication à l'aveugle, confirmation centrale, 60% d'items litigieux à 0.26 : 59.90
  audit étendu à tous les items (§ 1.8), confirmation centrale : +51.07 attendu, +123.65 pire
  adjudication à l'aveugle, confirmation plafond, 30% d'items litigieux à 0.26 : 46.80
  adjudication à l'aveugle, confirmation plafond, 60% d'items litigieux à 0.26 : 93.60
  audit étendu à tous les items (§ 1.8), confirmation plafond : +79.80 attendu, +193.20 pire
  banque refaite une fois (A6), pilote : +58.32 attendu, +184.32 pire ; rejet de 50 % des graines (A5) au lieu de 20 % : +38.88
  banque refaite une fois (A6), confirmation centrale : +187.11 attendu, +591.36 pire ; rejet de 50 % des graines (A5) au lieu de 20 % : +124.74
  banque refaite une fois (A6), confirmation plafond : +291.60 attendu, +921.60 pire ; rejet de 50 % des graines (A5) au lieu de 20 % : +194.40
  planteur pour 10 témoins et 10 renotations bis : +11.00 attendu, +33.60 pire
```
