# Contre-lecture R2 du programme d'entretien Transformative AI Fund v9 — rapport CL2

Contre-lecteur neuf (règle R2) : je n'ai écrit aucune version du programme d'entretien, ni la ventilation. Modèle servant
déclaré par l'environnement : Opus 5.5. Relevé `date -u` au début : **08:37:21 UTC le 29 octobre 2026** ; à la fin : voir la
dernière ligne. Aucune dépense, aucun réseau, aucun fichier du dépôt modifié.

Pièce relue : `brouillons/entretien-taif-v3/programme-entretien-taif-v9.md`, empreinte recalculée `1e0969d8cd20ee7a…`,
identique à son compagnon ; relue en entier. Pièce de contrôle : v8 (`7917ed02…`, différence complète lue). Les numéros de
ligne renvoient à la v9 telle qu'empreintée.

Registres recalculés : `decisions.md` (`fe82018c…` à ma première lecture, puis `80946642…` après l'ajout de R-732),
`go.md` (`f637f3ac…`), `depenses.md` (`34025262…`), `arrets.md` (`f3d47db6…`). Lus : R-422, R-430, R-455, R-464, R-465, R-468,
R-469, R-474, R-477, R-484 à R-487, R-495, R-519, R-571, R-586, R-597 à R-604, R-609, R-611, R-615, R-617, R-623 à R-732 ;
`go.md` lignes 96 à 132 et les lignes GO-2026-10-24-05, -26-02, -26-04, -27-12 ; `depenses.md` lignes 93 à 230.
Sources secondaires lues et empreintes recalculées (toutes **conformes** aux débuts cités par la v9) : N-058 `854f2724`,
N-059 `41aff854`, N-060 v3 `2b448f69`, rapprochement `813f3b30`, note Fable `20ec8d43`, lecture du rejeu `8799f7d3`,
contre-lecture du rejeu v2 `b156da9f`, coupe du calibrage `c66c1eed`, contrôle 12 joint `7600f2d0`, devis du pilote v1
`044112d3` et v2 `b841b006`, P-036 v2 `155f0511`, devis de régénération `9c85bb5e`, vérification NaN `c743199a`, garde δ
v1 `2838e8a2` et v5 `ab0a9633`, synthèse P-26 `67810dfa`, CL1 `f4c7d194`, CL6 `4e701178`, CL8 `ffa07b12`, CL9 `eed46db3`,
synthèse du 28–29 `0fe556d0`, ventilation v2 `8ab00ab5`, note de dépenses `93969946`, HELIOS `02527fd4` et `6b51dbf5`,
verdicts `63444faa`, `0c8ecbdf`, `05e896da`, empreintes défensives `d13bc425`, passation Argon `4035d8ed`, CL1 de la v5
`e2eed9af`. Non ouverts, comme prescrit : `prereg/P3-consignes-v1.md`, `donnees/`, `diag/*/traces`, toute branche, tout
contenu de quarantaine, du mode tenu à l'écart, du collisionneur « évasion » et du bras d'attaque (seules les lignes de
registre qui les nomment ont été lues).

---

## (a) Verdict

**Peut faire foi après corrections — pas en l'état.** Les chiffres neufs sont justes : cumul ≈ 525 USD, 81,66 USD des deux
jours, ≈ 99 USD de carte graphique, 54,55 USD de collisionneur défensif, 176 550 → 183 150, toutes les empreintes citées.
Mais **deux affirmations neuves dites au fonds en anglais sont contredites par le registre**, et la v9 renvoie elle-même
l'interlocuteur à ce registre. (1) Les refus de modèles seraient « jamais reformulés » et l'on n'aurait « pas contourné ».
(2) « Toutes les questions refusées étaient défensives ». Il y a aussi cinq majeurs, dont un fait neuf : **l'entretien a lieu
demain, 30 octobre (R-732)**. Plusieurs points de la v9 supposent donc un délai qui n'existe plus.

Comptes : 2 bloquants, 6 majeurs, 9 mineurs. Le classement par urgence avant demain est en section (c).

---

## (b) Constats

### Bloquants

**CL2-01 — bloquant — « never reworded », « Did you route around it? No » : faux sur la fenêtre que la v9 ouvre elle-même.**
Citations : l. 744-747 (cadrage) : « it happened in at least ten rounds between the twenty-sixth and the twenty-ninth. Each
refusal is recorded as it stands and never reworded » ; l. 810-812 (section 7) : « No. Each refusal is recorded as it stands
and never reworded » ; l. 827-829 : « Our written rule is that a refusal is answered with a different, narrower question, not
a rewording of the same one » ; message 4, l. 771-772 ; front C, l. 355.
Preuve :
- **R-468 (26 octobre, ≈ 01:05 UTC)** est une règle permanente écrite du directeur : « quand Opus refuse, reformule
  systématiquement de manière conceptuelle, mathématique et technique pour éviter les refus ».
- Elle a été appliquée le 26, dans la fenêtre « 26 au 29 » que cite la v9. R-465 (« escalier », « reformule … pour éviter
  le refus ») et R-469 (« agents outillés », question nouvelle sur « le même fond ») ont eu des réponses valides (lignes 159
  et 160 de `depenses.md`, 0,59 et 0,47 USD). R-474 écrit en toutes lettres : « C'est le refus d'une question déjà
  reformulée ».
- Les précédents du 25 : R-422 et R-430 (« reformule … pour éviter les red flags »).
- R-484 : une reformulation de session-depot a été arrêtée par un filtre de sûreté. R-486 : le directeur a dit « on le
  fait » sur une course qui, selon la ligne elle-même, « contournerait le refus d'Opus et de Fable ». L'instance ne l'a pas
  exécutée (R-486, R-487).
- La règle actuelle, R-609, date du **28 octobre** et remplace cette pratique.

La v8 bornait le récit au 28 (« trois fois en un jour »). En l'élargissant au 26, la v9 fait entrer dans la fenêtre des
faits qui contredisent la phrase. La réponse l. 830 offre en plus « I can show you the register entries ».
Correction proposée (le contenu d'un contact externe est un **nœud** : Lazar choisit) :
- (a) Borner la règle à sa date : « since the twenty-eighth of October, our written rule is… ». Retirer le « No. » absolu.
  Retirer « never reworded » du cadrage et du message 4.
- (b) Dire l'historique tel quel, ce qui est plus fort devant un fonds de sécurité qu'un récit propre. Par exemple :
  « Before the twenty-eighth, we re-posed some refused questions to the same model in narrower mathematical terms. We
  stopped when a safety filter halted one of those rewordings, and the director replaced that rule with the current one. »
- Dans les deux cas, réécrire front C l. 354-355 : « jamais la même question reformulée » vaut depuis R-609, pas avant.

**CL2-02 — bloquant — « defensive questions » et « All the refused questions were defensive » : faux pour la fenêtre
citée.**
Citations : l. 744 (« models refuse some of our own defensive questions … at least ten rounds between the twenty-sixth and
the twenty-ninth ») ; l. 813 (« All the refused questions were defensive — measurement and sizing ») ; message 4, l. 768-769
(« des refus de modèles récurrents sur nos questions défensives (au moins dix tours…) »).
Preuve. Plusieurs tours refusés du 26 au 29 ne sont pas des questions défensives :
- **R-571** (« questions fortes », 27 octobre, refus de Fable et d'Opus) : « la question porte sur le « bras d'attaque » ».
- « Mesures fortes » (ligne 210 de `depenses.md`) : refus de catégorie « cyber ».
- « Programme TAIF » (26 octobre) : la question avait une « partie « contournements » » (R-487).
- « Rapport consolidé v2 » (R-519) portait sur des failles, et une réponse de session-depot y a été arrêtée par un filtre.

La phrase est juste **pour les quatre refus postérieurs à la v8** (front C, l. 347-348), pas pour « at least ten rounds »,
ni pour « all ».
Correction : restreindre « defensive » aux refus du 28 et du 29 (R-635, R-676, R-686). Dans la réponse l. 813, écrire :
« The refusals since the twenty-eighth were all on defensive questions — measurement and sizing. »

### Majeurs

**CL2-03 — majeur — compte et date des refus : « dès le 26 octobre » est faux, et « au moins dix » sous-compte.**
Citations : l. 357-359 (« dès le 26 octobre … au moins dix tours ») ; réserve 11 ; points à trancher 7.
Preuve, `depenses.md` :
- Des refus au collisionneur existent dès le **24 octobre** (lignes 97 et 101, dont un « cyber ») et le **25** (lignes 114,
  115, 119, 127, 128).
- Du 26 au 29, la v9 omet cinq lignes du 26 : 157 (escalier), 158 (agents outillés), 164 (agents sur le noyau), 166
  (interface de calcul bornée), 168 (littérature des boucles).
- Mon compte par dossier de question : **≈ 15 tours touchés du 26 au 29**, **≈ 20 du 24 au 29**. La granularité « tour »
  est à fixer : un dossier, ou un étage III.1 / III.2 / III.3.
- Côté symétrie (R4), le frein a aussi mordu sur nous le **26** : R-484 et R-519 sont deux arrêts par filtre de sûreté de
  réponses de session-depot. Ils sont absents de « deux arrêts de classifieur ».

Correction : « depuis le 24 octobre, une vingtaine de tours touchés, à notre compte de lignes ». Ou bien ne pas citer de
nombre et dire « recurring, since the first week the collider ran ». Donner le dénominateur (tours lancés sur la période) si
on cite un nombre.

**CL2-04 — majeur — R-597 est daté du 27 octobre, pas du 28.**
Citations : l. 743 (« On the twenty-eighth of October two attempts to assemble offensive tooling were halted ») ; l. 768
(« Deux arrêts de sécurité consignés le 28 octobre ») ; l. 327 et 363 ; l. 826.
Preuve : la ligne R-597 de `decisions.md` porte « 2026-10-27 », entre R-596 (27 octobre au soir) et R-598 (28 octobre,
07:00 UTC). R-611 est bien du 28. L'erreur vient de la v8, mais la v9 a réécrit ces paragraphes.
Correction : « on the twenty-seventh and twenty-eighth of October ». Ou « within twenty-four hours », si Lazar le préfère
après avoir vérifié l'heure exacte de R-597.

**CL2-05 — majeur — « each line under a capped written authorisation » : faux.**
Citations : l. 805 (réponse neuve « How much have you spent? ») ; l. 836 (« each under its own capped, written
authorisation », repris de la v8).
Preuve :
- GO-2026-10-24-05 : R-355 dit « Aucun plafond fixé par Lazar ». Sa ligne d'extension dit « sans plafond fixé par Lazar ».
  Environ 11,6 USD de carte y sont imputés (note de dépenses).
- GO-2026-10-26-04, extension : « sans plafond (mot de Lazar) ».
- La même réponse, l. 806-807, dit ensuite qu'un lot a été lancé « without authorisation ». Elle se contredit à une phrase
  d'intervalle.

Correction : « each line under a written authorisation, nearly all of them capped », ou retirer « capped ».

**CL2-06 — majeur — « hidden from the agent » est dit comme un fait ; c'est encore à vérifier.**
Citation : l. 818-819 (« For each experimental control the original paper contains — hidden from the agent — two readers… »).
Preuve : N-060 v3, section « Ce que la décision ne fixe pas » : « À vérifier avant l'usage : que l'agent ne voit pas
`cibles` et qu'aucun moniteur ne les lit ». La v9 le note elle-même (piste 44). La réponse omet aussi le repli écrit d'avance
(lire la seule condition, sans affirmer de dommage).
Correction : « kept hidden from the agent — a property we check before use ». Ajouter une phrase : « if the oracle fails its
tests, we report the condition only and claim no harm ».

**CL2-07 — majeur — le « cadrage de trois minutes » n'en tient plus trois.**
Citation : section 5, l. 716-754.
Preuve : 619 mots dans la v9, contre 530 dans la v8 (compte de mots des lignes citées). Au débit oral courant de 130 à
150 mots par minute, cela fait environ **4 min 10 s à 4 min 45 s**. L'hypothèse de débit est la mienne.
Correction : couper environ 170 mots. Candidats : le troisième lemme ; la phrase de reproductibilité au bit près, qui a sa
place dans la question « null » de la section 7 ; la phrase sur la reprise étroite. Garder les juges et les refus.

**CL2-08 — majeur — la date de l'appel est fixée à demain (R-732) ; la v9 suppose un délai qui n'existe plus.**
Citations :
- Section 9, point 1, l. 930 (« La date de l'appel (non fixée à notre connaissance ; fin octobre recommandée au 17 octobre,
  à réviser) ») et l. 940-941 (« la date de l'appel n'y figure toujours pas ») ; réserve 5, l. 1019.
- Défauts « sous 48 heures » : points à trancher 2 (l. 1065), 4 et 6 (« Défaut : (a) ») et 10 (nœuds N1 à N5 de P-26).
- « à vérifier chez conv-audit avant l'appel » (l. 75, 288).

Preuve : R-732 (mot direct de Lazar, ≈ 08:37 UTC) : « la date de l'entretien est fixée à vendredi 30 octobre ». R-732 demande
aussi de porter la date dans la v9 après la contre-lecture. Un défaut de 48 heures pris à ≈ 08:36 UTC le 29 tomberait le
31, **après l'appel**. Les points 2, 4 et 6 doivent donc être tranchés explicitement aujourd'hui. L'heure et le fuseau de
l'appel ne sont pas consignés.
Correction : section 9, point 1 → « vendredi 30 octobre 2026 (R-732) ; heure à consigner ». Retirer la réserve 5, ou la
réécrire. Remplacer chaque « défaut sous 48 heures » utile à l'appel par « à trancher avant le 30 ». Voir la section (c).

### Mineurs

**CL2-09 — « certifies nothing below about a hundred and fifty honest units » est trop fort.**
Citations : l. 799, 29-6 (« ne peut rien certifier sous 144 unités (plancher exact, seuil 160, sans biais) »).
Preuve : contre-lecture de la garde δ v1, GD-06 : « Le « plancher structurel » n'est pas un plancher ». On observe des
certifications sous le plancher : 0,085 des suites à 64 unités au seuil 20 ; médiane à 88-90 unités sous un plancher de 93.
La correction demandée par la source est « plancher sans bruit » (pas « sans biais »).
Correction : « almost never certifies below about a hundred and fifty » ; et, en 29-6 : « plancher sans bruit ».

**CL2-10 — incohérences internes de comptes.**
- « Ce qui ne change pas » dit « seul le chiffre du message 3 bouge » (l. 67). Or le message 4 est réécrit, et le message 3
  gagne une phrase.
- « porté de 20 à 60 en six extensions » (l. 506) : `go.md` montre cinq extensions (37, 49, 51,6, 52,6, 60).
- « dix contre-lectures » (l. 39, 504) compte CL10, qui est encore en cours (R-724) : neuf rendues.
- Piste 41 (l. 641) : « Six synthèses nouvelles », mais cinq sont énumérées.

**CL2-11 — en-tête et chiffre de départ.**
- « Remplace » (l. 8) alors que la v8 fait foi jusqu'au mot de Lazar (l. 1059). Écrire « remplacera, après validation ».
- L'empreinte `fe82018c…`, dite « jusqu'à R-728 » (l. 13), est celle du registre **jusqu'à R-731** : `head -959 | sha256sum`
  rend `fe82018c…`.
- « 447,7 (total exact de la note) » (l. 992) : c'est la somme des sous-totaux arrondis (95 + 352,7). La somme des lignes de
  la note fait 448,15. L'effet sur ≈ 525 est nul, mais « exact » est faux.

**CL2-12 — section 4, règle 5 : une recommandation du collisionneur présentée comme une décision.**
Citation : « le bris d'égalité s'applique d'office, après une porte des scores finis (accord des deux modèles du tour
complémentaire, R-694) », sous le chapeau « des décisions, pas des résultats » (l. 680-687).
Preuve : R-694 range ce point parmi « onze décisions au format décision » servies à conv-audit, non tranchées. La section
10, point 5, interdit de citer les sorties du collisionneur comme résultats.
Correction : « recommandé par le tour complémentaire, à trancher ». Seule D-S13 (R-685) est close.

**CL2-13 — « from code, seeds and versions alone » (l. 734, 787).**
R-667 et R-679 : le palier au bit près « n'est atteignable qu'à fils identiques » (OpenBLAS à 64 fils, torch à 30), sur le
même matériel. Correction : « from the same code, seeds, versions and hardware settings ».

**CL2-14 — tranche 0 : liste de blocages partielle.**
Citation : l. 556. Le devis v1, § 9, en compte dix. La v9 en cite six et omet le vérificateur de N-060 v3, les nœuds ouverts
(dont P-11), les accès et le GO. Le « rejeu lu » est en partie levé (R-704). Correction : « dix blocages gratuits (devis v1,
§ 9), dont… ».

**CL2-15 — section 8 : la conclusion tient, mais son titre dit plus que sa preuve.**
Le calcul est juste :
- Plafonds de la banque : 90 + 300 + 0 + 4 + 13 = 407 ; 549 + 1 400 + 124 + 4 + 13 = 2 090.
- Régime du collisionneur : 179,9 + 20,31 + 54,55 = 254,76 USD en six jours, soit ≈ 42 par jour ; E8 vaut ≈ 12 jours par
  mois.
- Option : 34 500 + 6 000 = 40 500 ; × 1,1 = 44 550 ; 138 600 + 44 550 = **183 150**, ce qui est juste.

Trois réserves :
- (i) Le titre « elle tient telle quelle » est sans condition, alors que le tableau dit « non vérifié pour le plancher ».
  Mettre la condition dans le titre.
- (ii) La sentinelle (GO-2026-10-29-03) est chiffrée « ≈ 1 100 paires **par lancement** ». La comptée une fois sous-estime
  une banque à plusieurs lancements. L'effet reste négligeable devant les lignes de 12 000.
- (iii) Le pilote, la tranche 0 et la banque de la couche 2 sont des dépenses d'octobre et novembre, **avant** le début du
  financement (1er décembre). Les rattacher aux lignes du budget mélange les deux périodes. Ce qui compte pour la demande, ce
  sont les banques de G1 au mois 4.

**CL2-16 — « des centaines d'unités honnêtes par mode » (l. 694-695 ; l. 801 : « hundreds of units per mode »).**
Le calibrage honnête est commun aux modes (R-665, point 1). Le « ≥ 288 par mode » vise les **sabotés**, et ce n'est qu'une
recommandation (synthèse P-26, l. 388). Correction : « des centaines d'unités honnêtes, et autant de sabotées par mode si la
recommandation est retenue ».

**CL2-17 — termes et anglais.**
- Piste 48 dit « désembedding », le front B dit « lentille des logits » : choisir un seul terme.
- « R7 » est appliqué à des mesures d'instrument internes (29-2, 29-6). R7 vise les chiffres de l'état de l'art :
  écrire « exploratoires, non opposables ».
- Front B : « la phrase « being preregistered » reste vraie » est affirmé sans vérification (la v9 dit le contraire
  quatre mots plus loin).
- En anglais, l. 793 : « the smaller judge 39 to 64 » → « 39 to 64 per cent ».

### Points vérifiés justes (rien à corriger)

- Changement 2 : 3,19 + 1,29 + 1,83 + 12,59 + 11,06 + 1,76 + 6,84 + 6,57 + 1,92 + 14,30 + 20,31 = **81,66**, ligne par
  ligne (lignes 213 à 230). Le 6,84 inclut les 2,58 du tour 1 : pas de double compte. 447,7 − 4,4 + 81,66 = **524,96** ;
  avec 6,01, 530,97. Carte graphique : 95 + 1,76 + 1,92 = **98,68**. Appels de modèles : 352,7 − 4,4 + 77,98 = 426,3.
  Collisionneur du 24 au 29 : ≈ 254,8.
- Changement 5 : 3,19 + 12,59 + 11,06 + 6,84 + 6,57 + 14,30 = **54,55**. Six tours, aucun sur l'évasion.
- Changements 1, 6, 7 (sauf CL2-10), 8, 13 et 14 : conformes à leurs sources. 29-1 (R-679 ; sceau `91b61c45…` ; 424 sur
  424 ; 1,76 USD). 29-2 (157/180 = 0,87, Wilson 0,82-0,91 ; 3B 0,39 à 0,64 ; − 0,28). 29-3, 29-4, 29-5 (0,54 ; 0,024-0,027 ;
  confiance 0,6-0,75). 29-6 (168 / 176 / 188… ; 0,89 → 0,03 à τ = 0,01, seuil 160 ; GD5-01 0,64-0,82, 0,18, 300 et 650 ;
  sauf CL2-09).
- Devis du pilote : v2 central ≈ 234, fourchette 90-549, 57 % ; v1 309, 135-667, ≈ 76 % SUPPOSÉ. P-036 v2 : 300 à 1 400.
  Lectures : 133 / 1 296 ≈ 0,10 par épisode.
- Changement 4 (écart de la synthèse v2) et changement 13 (réserve 3 de la ventilation à « ≈ 450 ») : exacts.
- Aucune recette d'attaque, de sabotage ou d'évasion écrite. Le mode tenu à l'écart n'est pas nommé. Les cellules en
  quarantaine sont décrites par leur seule existence (R-597, R-607, R-611 tenues). Le seul mode nommé, « affaiblir les
  contrôles », est un mode connu de la couche 2.

---

## (c) Urgence avant l'entretien du vendredi 30 octobre (R-732)

**Niveau 1 — aujourd'hui, avant toute répétition : le texte.**
1. Corriger CL2-01 et CL2-02 (refus), puis CL2-04, CL2-05 et CL2-06 : ce sont des phrases anglaises dites au fonds. Le
   choix entre CL2-01 (a) et (b) est un nœud de Lazar.
2. Raccourcir le cadrage à environ 450 mots (CL2-07).
3. v10 vérifiée par différence. Puis le mot de Lazar pour qu'elle fasse foi (point à trancher 1, sans défaut). Faute de mot,
   c'est la v8 qui fait foi, et la v8 contient l'erreur de date de CL2-04 et les « about 450 », « under a hundred ».

**Niveau 2 — décisions de Lazar dont le défaut de 48 heures tomberait après l'appel : à trancher aujourd'hui.**
4. La demande : confirmer 176 550 (extension sur le scénario ambitieux) ou 86 130 ; deux ou trois paliers ; le taux et les
   jours de E1 (ou dire « about 7,500, to be fixed ») ; E8 tel quel ou porté à 12 000 (point 2).
5. La formule du coût de carte graphique (point 4) et les résultats négatifs dans le cadrage (point 6).
6. Comment dire les refus (point 7, et CL2-01).
7. Dire ou non le lancement sans autorisation du 23 octobre (point 5). Cela demande d'abord la lecture de la facturation sur
   la console Vast.ai, à faire aujourd'hui.

**Niveau 3 — vérifications factuelles d'ici demain.**
8. L'état de T0 à T5 chez conv-audit. Sans confirmation, réécrire « Six further measurements are being preregistered » en
   « are designed and will be preregistered ».
9. La facturation de la relève du 23 octobre (voir point 7).
10. Consigner l'heure et le fuseau de l'appel.

**Niveau 4 — sécurité, urgent quel que soit l'appel.**
11. Révoquer les clés exposées les 27 et 28 octobre (R-624). Un fonds de sécurité peut demander comment les secrets sont
    tenus.

**Niveau 5 — peut attendre après l'appel.**
12. Le nœud HELIOS au fond : la réponse anglaise de la section 7 suffit pour demain.
13. P-26 (N1 à N6), V-2 et V-3, le devis du pilote au-delà de 90 USD, le scellement du mode tenu à l'écart, le PDF du papier
    C, l'écart de calendrier de G1 (dire la version envoyée), les champs `[TO COMPLETE]` (sauf demande du fonds), le PDF
    vulgarisé de la v9.

---

## (d) Ce qu'un évaluateur demanderait et que la v9 ne prépare pas

1. **Le dénominateur des refus.** « Une vingtaine de tours touchés » sur combien de tours lancés ? Taux par modèle ?
2. **Pourquoi 12 000 USD de carte graphique** au scénario ambitieux, si le programme n'en a dépensé qu'environ 100 en un
   mois ? Il faut une ligne de calcul (organismes de 70 milliards, banques de G1, réplication).
3. **Ce qui se passe si G0 échoue fin novembre**, avant le début du financement le 1er décembre : règle de décision et
   palier de repli.
4. **La revue de sécurité externe** : qui la fera, quel calendrier, quel état (rien n'a avancé), et le taux de E1 (non
   fixé).
5. **La garde des contenus en quarantaine** : où ils sont stockés, qui y a accès, et l'incident des clés exposées.
6. **Ce que chaque palier livre, et quand** : papiers, portes, dates. La v9 donne les montants, pas les livrables par palier.
7. **Le contrôle humain sur les agents** au vu de R-486. La question « How much of this is you » existe, mais pas sa
   réponse sur le jour où l'instance a refusé un ordre du directeur.

---

## (e) Non vérifié

- La proposition envoyée et son budget v3 (`737c482c…`, `037765b0…`), donc les lignes du plancher : pas recherchés par
  empreinte au-delà de l'arbre de travail lisible.
- La carte des hypothèses, l'en-tête du dossier du fonds et la branche `calcul/regeneration-sondes-p3-v1` : non lus
  (repris de la v8, ou interdits).
- L'heure exacte de R-597 en UTC : la ligne du registre porte le 27 octobre, sans heure lue.
- Le contenu des questions refusées : jugé sur les seules lignes de registre (R-487, R-519, R-571, ligne 210). Aucune
  question ni cellule ouverte.
- Mon compte de « ≈ 15 » et « ≈ 20 » tours : compte de lignes et de dossiers, granularité à fixer.
- Le débit oral du cadrage : 130 à 150 mots par minute, hypothèse.
- Les registres propres de conv-audit (T0 à T5, P4, P3b, R-383, R-416).
- Les dates « 27 et 28 » des clés exposées.
- La facturation réelle.

Relevé `date -u` à la fin : **08:47 UTC le 29 octobre 2026**.
