# Synthese d'anteriorite -- pilier attaque (collisionneur E3, etage III)

Date : 2026-11-08.
Source : run `run-pilier-attaque-e3-v9`, 15 cellules validees (A, B, C, D et E), 3 tours (conception, equipe rouge, riposte). Zero refus.
Especes : A (Fable 5.1, Anthropic), B (Opus 5.5, Anthropic), C (Argon, Google), D (Kimi K3.1 Pro, Moonshot), E (Astra, OpenAI).
Statut de chaque enonce ci-dessous : **HYPOTHESE** du collisionneur, sauf indication contraire. Aucun chiffre n'a ete verifie sur piece par cette synthese.
Niveau : methode et demonstration. Aucune description de procede de fabrication de comportement de sabotage, d'evasion ou de tromperie.

---

## 1. Convergences entre les cinq especes

Les points ci-dessous sont acceptes par les cinq especes apres le tour de riposte (T3), sauf mention contraire (« quatre sur cinq »).

### 1.1 Qualification de l'oracle comme prealable absolu

Les cinq especes convergent : aucune lecture decisive de sonde ne precede la qualification de la verite terrain. A nomme cette etape E0', B la nomme X0, C Experience 0, D E0', E la fiche O. Sans oracle calibre -- rappel par strate, taux de fausses accusations sur les echecs honnetes, et borne sur la dependance d'erreurs avec les moniteurs -- tout rappel en aval est non interpretable. Le dommage diffus doit depasser le bruit de la loi nulle honnete-contre-honnete avant que les etiquettes de dommage ne servent.

### 1.2 Trois confondants fatals (unanimite)

Les trois confondants identifies par B et C dans le run v2.6 sont acceptes par les cinq especes. Deux especes supplementaires (D et E) les retrouvent independamment dans leurs conceptions T1 et les defendent en T3 :

1. **Attention causale et consigne.** Dans un modele autoregressif, les etats caches aux positions qui suivent la consigne sont calcules a partir de la consigne. Lire ces positions, c'est encore lire la consigne sous forme transformee. Le masquage positionnel est insuffisant. Seules des paires contrefactuelles (consigne d'attaque avec execution honnete, consigne neutre avec sabotage atteste) tranchent. D ajoute (T2) que le prefixe et l'organisme relu doivent etre croises ; E ajoute (T1) que les cases du carre contrefactuel ne sont pas toutes remplissables par construction, et que les cases vides doivent etre declarees non identifiables.

2. **Identite de l'organisme contre acte de sabotage.** Si l'organisme saboteur et le modele honnete different par leurs poids (ou adaptateurs), une sonde lineaire peut separer les deux populations en detectant la modification elle-meme, y compris sur des episodes sans sabotage. Un organisme placebo (meme chaine de modification, objectif cache inoffensif) et des episodes dormants du saboteur (episodes sans sabotage confirme) sont necessaires pour separer la detection de l'organisme de la detection de l'episode. D (T1) explicite que T100 ne remplit pas cette fonction : il faut un adaptateur de meme rang, meme norme et meme chaine de distillation, avec un objectif benin distinct. E (T2) ajoute que le placebo ne doit pas etre choisi pour son indetectabilite -- son score a la sonde est une issue, pas un critere de selection.

3. **Mode tenu a l'ecart consomme avant la porte G1.** Toute mesure transmise a la defense sur le mode tenu a l'ecart (N-054), meme agregee, peut orienter ses choix ulterieurs (couche, regularisation, seuil). La demonstration d'avant-entretien doit preserver ce temoin. B propose de ne presenter que le preenregistrement scelle de l'experience de generalisation ; C propose une validation croisee par bloc sur les familles connues (R-610) comme substitut ; D (T3) et E (T3) acceptent le principe et ajoutent que la famille tenue a l'ecart ne fournit qu'un point confirmatoire au budget fige, pas une courbe avec variance inter-familles.

### 1.3 Base qui relit comme comparateur le plus exigeant

Les cinq especes adoptent le meme modele de base relisant exactement les memes jetons generes par l'organisme comme comparateur de reference pour la question « au-dela du texte ». Le contraste primaire est : sonde lisant les activations de l'organisme contre meme sonde lisant les activations de la base ($\alpha=0$) sur les memes jetons. Ce comparateur remplace la simple comparaison entre sonde interne et predicteur sur les traits du texte (qui reste un second comparateur, moins exigeant). A-T3 precise : « au-dela de ce que la meme architecture de sonde extrait des activations de la base relisant le meme texte », et non « au-dela du texte » tout court. D-T3 et E-T3 acceptent, en notant que cette base reste un extracteur particulier et non une borne de toute l'information textuelle.

### 1.4 Vrai organisme placebo a objectif cache benin

Les cinq especes acceptent en T3 que T100 n'est pas un placebo et qu'un vrai placebo doit etre construit. Les specifications convergentes : adaptateur de meme rang, meme norme de Frobenius, meme chaine de distillation que le saboteur, mais avec un objectif cache inoffensif (formatage stylistique ou autre tache benigne). Le placebo est qualifie sans la sonde (A-T3) : norme de modification non nulle (il a ete modifie), qualite de tache au moins egale au jumeau moins une marge, dommage nul atteste par l'oracle. Son score a la sonde est une issue, jamais un critere de selection (E-T2, accepte par tous en T3).

### 1.5 Dormants definis independamment de l'oracle

Les cinq especes convergent en T3 : un episode « dormant » ne peut plus etre defini par la seule absence d'etiquette de l'oracle. A-T3 definit le dormant par la provenance structurelle de la tache (le monde plante n'offre pas d'opportunite de sabotage), independamment de la lecture de l'oracle. B-T3 exige l'oracle ET les evenements executes. C-T3 adopte les dormants structurels. D-T3 exige une provenance independante ; les negatifs oracle seuls entrent dans une analyse de sensibilite a la contamination $c$. E-T3 separe dormants attestes independamment, negatifs oracle seuls et cas indetermines.

Le mecanisme fatal est le meme chez tous : un sabotage diffus manque par l'oracle est verse dans les dormants, contaminant la classe negative exactement la ou la trace est la plus subtile (A-transversal). Si le verdict change selon $c$, il est non jugeable (D-T3).

### 1.6 Separation entre complementarite et etau

Les cinq especes separent explicitement en T3 deux grandeurs que le run v2.6 confondait :

- **Complementarite** : la capture residuelle $P(I^+ \mid E^-, Y=1)$ est une covariance conditionnelle des alertes (B-T3, formule de E-T2 adoptee par B). Elle mesure si la machoire interne attrape des sabotages que l'externe manque. C'est une association statique, stratifiee par tache et par dose, sans valeur causale.

- **Etau** : l'effet d'une pression externe assignee sur le score interne. Il exige des campagnes randomisees -- pression externe reelle contre pression placebo -- et une lecture en intention de traiter sur tous les episodes, sans conditionner au dommage maintenu ni aux seuls survivants. L'etau est une affirmation conjointe sur des effets moyens assignes (E-T3).

A-T3 les place dans deux experiences distinctes (E4' et E5e'). B-T3 dans X4 et X5. C-T3 dans les deux parties de l'Experience 5. D-T3 dans E6' (trois questions non interchangeables). E-T3 dans les deux duels de la fiche P.

### 1.7 Intention de traiter pour les experiences de pression

Les cinq especes convergent en T3 : l'analyse de l'etau porte sur tous les episodes generes par les campagnes assignees, sans filtrage selon le dommage maintenu (retrait du conditionnement sur $E^-$) ni selon le statut de l'externe. Le dommage realise est un resultat, pas un filtre. B-T3 cite les bornes de Lee (Lee, 2009) pour encadrer l'effet de traitement en presence de selection : les bornes doivent toutes deux rester positives pour conclure.

A-T3 l'adopte en E5e'. C-T3 le corrige explicitement dans sa reponse aux critiques (point 8). D-T3 l'adopte en E6'. E-T3 l'exige comme contrat commun de la fiche P.

### 1.8 Loi nulle honnete-contre-honnete

Les cinq especes convergent sur la necessite de mesurer la distribution du dommage entre paires honnete-honnete (meme tache, $\alpha=0$) avant de declarer un dommage diffus. B-T3 l'a propose comme « absence que personne ne mesure » ; les quatre autres l'adoptent en T3. Si le dommage diffus ne depasse pas le quantile 95 % de cette loi nulle, la dose est refixee et les sondes sont suspendues pour la strate concernee. A-T3 propose un effectif illustratif de 200 paires. C-T3 integre 400 paires dans l'Experience 0.

### 1.9 Non jugeable comme issue de mesure

Les cinq especes convergent en T3 : un intervalle de confiance qui traverse le seuil de decision donne une issue « non jugeable ». Ce n'est pas une troisieme hypothese, c'est une issue de mesure (E-T1, adoptee par tous). A-T3 : « l'intervalle traverse le seuil = non jugeable ». B-T3 : « une issue dont l'intervalle traverse le seuil est non jugeable (forme de E, adoptee) ». D-T3 : « manque de precision = non jugeable, jamais falsification scientifique ». C-T3 et E-T3 l'integrent dans le contrat commun des duels.

### 1.10 Controles necessaires (convergence)

Les controles suivants apparaissent chez les cinq especes et sont acceptes en riposte :

| Controle | Origine | Accepte par |
|---|---|---|
| Controle positif par saboteur temoin non dissimule | B-T1 | A-T3, C-T3, D-T3, E-T3 |
| Paires contrefactuelles (consigne x acte) | C-T1, E-T1 | A-T3, B-T3, D-T3 |
| Organisme placebo a objectif cache benin | D-T1, E-T1 | A-T3, B-T3, C-T3 |
| Base qui relit les memes jetons | A-T1 | B-T3, C-T3, D-T3, E-T3 |
| Echecs honnetes comme negatifs obligatoires | C-T1 | A-T3, B-T3, D-T3, E-T3 |
| Sas d'evaluation automatise tiers | B-T1 | A-T3, C-T3, D-T3, E-T3 |
| Audit du rappel de l'oracle par strate sur sabotages connus | B-T1 | A-T3, C-T3, D-T3, E-T3 |
| Couches et hyperparametres figes au preenregistrement | C-T1 | A-T3, B-T3, D-T3, E-T3 |
| Journal horodate du regime d'information de chaque sous-bras | B-T1 | A-T3, C-T3, D-T3, E-T3 |
| Diversite de famille entre oracle, juges et organismes | B-T1 | A-T3, C-T3, D-T3, E-T3 |
| Trois partitions disjointes : selection, calibration, evaluation | A-T1, D-T1 | B-T3, C-T3, E-T3 |
| Au moins 2000 negatifs honnetes pour la stabilite du seuil a 1 % | A-T2, B-T2 | C-T3, D-T3, E-T3 |
| Campagne ou lignee comme unite d'inference pour les experiences de pression | B-T2, E-T1 | A-T3, C-T3, D-T3 |
| Panel duplique comme controle de diversite nulle | D-T1, E-T1 | A-T3, B-T3, C-T3 |
| Affectation aleatoire des roles reserve et deploye dans un meme vivier | B-T2, E-T1 | A-T3, C-T3, D-T3 |
| Pression placebo a budget egal dans les experiences d'etau | D-T1, E-T1 | A-T3, B-T3, C-T3 |
| Loi nulle honnete-contre-honnete du dommage | B-T3 | A-T3, C-T3, D-T3, E-T3 |
| Controle de la mediation textuelle (base relit chaque generation) | A-T2 | B-T3, C-T3, D-T3, E-T3 |

### 1.11 Experience a faire en premier

Les cinq especes convergent : l'experience prioritaire est la qualification de l'oracle (E0/X0/O), qui ne consomme pas le mode tenu a l'ecart, conditionne la validite de toutes les mesures suivantes, et contient deux portes bon marche et decisives : la loi nulle du dommage et le lot d'adjudication scelle (A-T3). L'issue negative suspend les points 1 a 5 par strate, sans arret (R-1795). Immediatement apres, le controle positif corrige (base qui relit, dormants attestes, placebo distinct).

---

## 2. Divergences non resolues

Apres le tour de riposte (T3), les divergences suivantes persistent :

| Point | Positions |
|---|---|
| **Architecture experimentale** | A : E0'--E5' sequentielles. B : X0--X6 sequentielles. C : Exp. 0--5 avec champs fermes. D : E0'--E6' (trois questions dans E6'). E : fiches thematiques O/T/L/C/R/P, sans ordre strict. |
| **Budget illustratif** | A : 150--300 USD (illustratif). B : non chiffrable sans inventaire et pilote de debit. C : environ 3 680 USD (illustratif). D : illustratifs, tout budget anterieur rejete. E : non estimable honnetement sans pilote. |
| **Interpretabilite des substitutions en generation autoregressive** | A et B maintiennent la substitution comme test causal, a condition des controles croises intra-condition. C maintient que la substitution est non interpretable en generation autoregressive (le desaccord est arbitrable par la taille du controle croise : si la greffe honnete_i vers honnete_j degrade le dommage autant que S vers jumeau, C a raison -- A-T3). D et E sont plus prudents : une substitution sans effet refute « ce site est un levier » mais ne refute pas « il existe une trace causale ». |
| **Complementarite comme filtre avant l'etau** | A garde la complementarite (E4') comme filtre : si la capture residuelle est nulle sur les modes vus, l'etau est improbable et E5e' passe apres. D et E rejettent ce role de filtre (la complementarite n'a pas de valeur predictive pour l'etau). Le dissensus porte sur l'ordre, non sur la lecture (A-T3). |
| **Metrique de l'independance de l'oracle** | A : correlation des scores continus + rapport d'erreurs a un seuil de travail elargi (10 %, illustratif). B : intervalle de Frechet-Hoeffding sur le rappel vrai, sans hypothese d'independance. C : test d'equivalence TOST sur le risque relatif conditionnel (Mantel-Haenszel). D : contrastes conditionnels normalises, stratifies finement, test d'equivalence correctement dimensionne. E : ecart de probabilite conditionnelle $\delta_z$ avec intervalles simultanes. |
| **Effectifs et nombre de campagnes pour les experiences de pression** | A : 4 lignees par bras (illustratif) ; effectif = lignee. B : nombre annonce d'avance, au moins 4. C : 6 lignees (illustratif). D : a chiffrer apres dimensionnement. E : non estimable sans pilote de debit. |
| **Statut de la dose comme variable independante** | B (T1) : la dose diffuse a ete fixee par la boite noire ; comparer blanche et noire est en partie vrai par construction. Tous acceptent de disjoindre la boite noire d'evaluation de celle de la dose, mais D et E restent plus prudents : fixer une dose ne selectionne pas automatiquement les episodes (E-T3), mais la declaration de la population (« dose selectionnee selon la regle boite noire ») est obligatoire. |

---

## 3. Anteriorite citee par les cellules (references a verifier)

Les references suivantes sont citees par les cinq especes comme anteriorite potentielle. Leur statut est **HYPOTHESE** (« reference citee par le collisionneur, a verifier sur `docs/etat-de-l-art-controle-ia-v1.md` et sur les PDF empreintes » -- R7). Aucune n'a ete verifiee par cette synthese.

### 3.1 References methodologiques de securite et d'alignement

| Reference | Domaine occupe (HYPOTHESE) | Citee par |
|---|---|---|
| Greenblatt, Shlegeris, Sachan et Roger (2023), *AI Control: Improving Safety Despite Intentional Subversion* | Evaluations de controle avec equipes rouge et bleue ; these « un dispositif ne vaut que contre un attaquant fort » | A-T1, B-T1, C-T1, D-T1, E-T1 |
| Hubinger et al. (2024), *Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training* | Organismes a comportement cache comme objets d'epreuve ; persistance apres entrainement de surete | A-T1, B-T1, C-T1, D-T1 |
| Zou et al. (2023), *Representation Engineering: A Top-Down Approach to AI Transparency* | Extraction de caracteristiques latentes par sondes ; ingenierie de representations | A-T1, C-T1, D-T1, E-T1 |
| Burns et al. (2022), *Discovering Latent Knowledge in Language Models Without Supervision* | Decouverte de connaissance latente sans supervision ; sondes lineaires | C-T1, E-T1 |

### 3.2 Resultats empiriques recents cites comme RAPPORTES

| Reference | Contenu cite (RAPPORTE) | Citee par |
|---|---|---|
| Bailey 2412.09565 | Convergence de la defense | B-T1, C-T2 |
| Neural Chameleons 2512.11949 | Les ensembles de sondes attenuent sans eliminer l'evasion | B-T1, C-T2, E-T2 |
| Matrice de transfert 2609.36490, fig. 4a | Transfert inegal entre trois sondes, sans juge | B-T1, C-T2 |
| « Axe de douleur » 2609.16247, 2610.22460 | Direction lisible mais non causale : retrait sans effet 24 fois sur 25 | A-T1, B-T1, C-T3, E-T2 |

### 3.3 References methodologiques statistiques

| Reference | Usage dans le collisionneur | Citee par |
|---|---|---|
| Meng, Bau, Andonian, Belinkov (2022), ROME | Methode de substitution | C-T1, D-T2 |
| Hewitt et Liang (2019), EMNLP | Taches de controle pour les sondes | B-T3, A-T3 |
| Holm (1979) | Correction de tests multiples | B-T1, C-T2 |
| Westfall et Young (1993), *Resampling-Based Multiple Testing* | max-T par permutation (remplace Holm chez B-T3) | B-T3 |
| Clopper et Pearson (1934) | Intervalles de confiance exacts | B-T3, C-T3, A-T3 |
| Schuirmann (1987), TOST | Test d'equivalence a deux unilatéraux | A-T3, C-T3, D-T3 |
| Mantel et Haenszel (1959) | Analyse stratifiee ; test d'association pour l'oracle | B-T3, C-T3 |
| Lee (2009), *Review of Economic Studies* | Bornes de l'effet de traitement sous selection | B-T3 |
| Freund et Schapire (1997) | Algorithme Hedge pour le melange de Nash | B-T1 |
| Wald (1945) | Test sequentiel SPRT (propose puis abandonne par A-T3 au profit d'accumulation a loi alternative) | A-T1 |

**Remarque d'integrite (B-T2, reprise en v2)** : dans le run v2.6, C attribuait les references de securite a la section D des faits du programme. B avait releve que la section D ne nomme aucun auteur. L'attribution a cette section est fausse ; les references elles-memes restent a verifier sur piece. Cette remarque n'a pas ete contestee dans le run v9.

---

## 4. Combinaison potentiellement non occupee (HYPOTHESE)

Les cinq especes convergent vers une combinaison methodologique qui ne leur semble pas couverte par l'anteriorite citee. Son statut est **HYPOTHESE** tant que `docs/etat-de-l-art-controle-ia-v1.md` n'a pas ete audite (R7, R8).

La combinaison rassemble (mise a jour par rapport a la v1 ; les elements nouvellement exiges par les especes D et E sont signales) :

1. Controle positif obligatoire par un saboteur temoin non dissimule, gele et transfere a un second temoin independant.
2. Non-inferiorite de l'efficacite de sabotage comme condition d'une evasion valide, stratifiee par type et difficulte de tache.
3. Bras placebo (organisme modifie avec un objectif cache benin, de meme rang, norme et chaine de distillation, **distinct de T100**) pour separer la detection de l'identite de l'organisme de la detection de l'acte.
4. Grille contrefactuelle a quatre conditions (sabotage actif, dormant structurel, feinte, honnete) appliquee uniformement aux sondes et au predicteur boite noire, avec **declaration explicite des cases non identifiables** (E-T1).
5. Mesure empirique de l'independance entre oracle et moniteurs : **borne de Frechet-Hoeffding** sur le rappel vrai sans hypothese d'independance (B-T3), completee par des contrastes conditionnels stratifies (D-T3) et des intervalles simultanes (E-T3).
6. Sas d'evaluation automatise tiers, avec journal horodate et embargo des pieces publiques.
7. Validation croisee par bloc (un pli par graine d'organisme et monde de tache) pour preserver le mode tenu a l'ecart avant G1, avec declaration que la famille tenue a l'ecart ne fournit qu'un point confirmatoire.
8. Quatre types de negatifs obligatoires (jumeau honnete, dormants structurels du saboteur, echecs honnetes apparies, placebo a objectif benin), **chacun rapporte separement** (D-T2).
9. Diversite de famille de preentrainement entre organismes, juges et oracle pour exclure la connivence statistique.
10. **Base qui relit** exactement les memes jetons comme comparateur de reference pour la question « au-dela du texte » (convergence des cinq especes).
11. **Loi nulle honnete-contre-honnete** comme plancher du dommage (B-T3, unanimite).
12. **Separation explicite entre complementarite et etau** : capture residuelle (association statique) contre effet d'une pression assignee en intention de traiter (convergence des cinq especes).
13. **Pression placebo** (moniteur aleatoire de meme calibration) comme temoin de l'etau (D-T1, E-T1, unanimite).
14. **Non jugeable** comme issue formelle de mesure, traitee au meme rang que les deux hypotheses (E-T1, unanimite).

Chaque element pris separement existe dans la litterature des evaluations de surete, des essais cliniques randomises ou de la detection de triche. La combinaison des quatorze dans un meme protocole d'evaluation de moniteurs de sabotage est ce qui pourrait etre inedit. Cette assertion est la plus fragile de la synthese : une seule reference reunissant ces elements la refute.

---

## 5. Zones vierges seduisantes (R8)

Les points suivants semblent inoccupes mais meritent une verification plus dure (R8 : « zones vierges seduisantes verifiees plus durement ») :

1. **Protocole contrefactuel complet applique au predicteur boite noire.** La litterature sur les sondes internes semble ne pas auditer systematiquement la base boite noire avec la meme grille contrefactuelle. C'est une hypothese d'originalite seduisante : verifier que les travaux sur les evaluations d'alignement (CCS, RepE) ne l'incluent pas deja.

2. **Organisme placebo avec objectif cache benin dans un protocole de surete.** Le placebo est un standard en essais cliniques mais semble absent des protocoles d'evaluation de surete des modeles de langage. Verifier les travaux de METR et d'Apollo Research.

3. **Audit du rappel de l'oracle par lot scelle du bras d'attaque.** La question « l'oracle sait-il qu'il y a sabotage quand il y en a ? » est rarement posee dans les travaux d'evaluation. Verifier.

4. **Borne de Frechet-Hoeffding pour qualifier la dependance oracle-moniteurs sans hypothese d'independance.** Outil standard de la theorie des copules, mais son application a la qualification conjointe d'un oracle et d'un moniteur dans un protocole de surete semble neuve. Verifier les travaux de statistique appliquee aux evaluations de systemes critiques.

5. **Intention de traiter et bornes de Lee dans un protocole adaptatif de pression sur des organismes.** Standard en econometrie et en essais cliniques, mais absent des travaux de surete IA comme cadre formel pour l'etau. Verifier que les travaux sur les evaluations adaptatives (METR, Redwood Research) ne l'emploient pas.

6. **Specialisation benigne fortement divergente comme controle negatif du detecteur de nouveaute.** E-T2 propose de separer le signal de nouveaute (un organisme fait quelque chose d'inhabituel) du signal de sabotage. Un organisme specialise dans une tache benigne mais a forte divergence par rapport au modele de base sert de temoin. Verifier les protocoles de detection d'anomalies en surete.

---

## 6. Ce que cette synthese ne couvre pas

- Le contenu des familles R-610, du mode tenu a l'ecart (N-054) et de la breche W2 : tenus a l'ecart par construction.
- Les chiffres de `docs/etat-de-l-art-controle-ia-v1.md` : non transmis au collisionneur.
- Les procedes de fabrication d'organismes saboteurs, evasifs ou trompeurs : hors perimetre (niveau methode).
- La verification sur PDF empreinte des references citees (R7).
- Les devis de calcul detailles : chaque espece les declare illustratifs ; aucun n'a ete audite.
- La question de la faisabilite a effectifs reels : chaque espece admet que ses effectifs illustratifs peuvent rendre l'experience non jugeable.
- Les donnees brutes et les journaux de run v9.

---

## 7. Cinq especes : qui dit quoi

### 7.1 Ce que D (Kimi) apporte

D est l'espece la plus conservatrice du collisionneur. Ses apports principaux, adoptes ou debattus par les autres :

1. **Interaction non identifiable dans le plan 2x2.** D identifie en T1 que la case « placebo avec sabotage » n'existe pas : le plan factoriel organisme x acte est incomplet par construction. D propose d'abandonner le plan 2x2 au profit d'un contraste intra-saboteur (actes contre dormants attestes, apparies). Accepte par tous en T3.

2. **Borne de covariance « vraie par construction ».** D demontre formellement (T1) que la borne de Frechet rend la marge absolue de covariance oracle-moniteurs non falsifiante quand les erreurs sont rares. La marge absolue est supprimee et remplacee par des contrastes conditionnels normalises (D-T3). Accepte par A, B, C et E.

3. **Equivalence partout.** D insiste sur des tests d'equivalence (TOST) preenregistres, avec marges d'equivalence normalisees, pour chaque grandeur mesuree. Les autres especes adoptent le principe mais pas l'etendue (A et B gardent des seuils illustratifs sans toujours formaliser l'equivalence).

4. **Separation information et utilite.** D (T3, point E1) separe l'information predictive conditionnelle (score logarithmique croise) et l'utilite operationnelle ($\Delta$TPR). Un $\Delta \leq \varepsilon$ refute l'utilite dans le perimetre teste, mais pas toute information. Adopte par E ; A et B gardent le $\Delta$TPR comme grandeur unique.

5. **Budget et delai.** D est la seule espece a avoir propose un budget de 4 000 a 15 000 USD dans sa conception (T1), et la seule a rejeter explicitement en T3 tout chiffrage comme incompatible avec un dimensionnement rigoureux. Les autres proposent des budgets plus bas (A : 150--300 USD, C : 3 680 USD) ou refusent de chiffrer (B, E).

### 7.2 Ce que E (Astra) apporte

E est l'espece la plus formellement rigoureuse du collisionneur. Ses apports principaux :

1. **« Non jugeable » comme issue de mesure.** E formalise en T1 le « non jugeable » (indecis) comme une issue de mesure a part entiere, et non une troisieme hypothese. Chaque duel porte sur un contraste avec une frontiere : $H_A$ d'un cote, $H_B$ de l'autre, et un intervalle qui traverse la frontiere est non jugeable. Adopte unanimement en T3.

2. **Distinction correlation et causalite a chaque etape.** E explicite en T1 et T3 que chaque volet (trace, localisation, causalite, regle, pince) fait une affirmation de nature differente. Une trace decodable ne demontre pas une cause. Une cause manipulable ne demontre pas une sonde inevitable. Une capture residuelle ne demontre pas qu'une pression externe augmente la trace (E-T3, reponse a l'arbitre).

3. **Specialisation benigne fortement divergente.** E (T2, accepte en T3) propose un controle negatif specifique du detecteur de nouveaute : un organisme specialise dans une tache benigne mais a forte divergence par rapport a la base. Il separe le signal de nouveaute du signal de sabotage. Adopte par D ; les autres le notent sans l'integrer explicitement.

4. **Asymetrie de normalisation identifiee.** E (T2) identifie que les normalisations entre conditions d'intervention sont asymetriques (le dommage initial et la qualite de tache ne sont pas dans la meme unite), et qu'un ratio au dommage initial est instable quand ce dommage est faible. Tous adoptent en T3 : meme unite absolue, pas de ratio.

5. **Selection des survivants formellement identifiee.** E (T2) formalise le biais de selection des survivants dans la mesure de l'etau : conditionner au dommage maintenu selectionne les organismes qui ont reussi, et l'effet mesure n'est pas celui de la pression mais celui de la survie. Adopte unanimement par l'intention de traiter.

6. **Plan factoriel pour le secret.** E (T1) propose un plan 2x2x2 (distribution revelee/cachee x panel expose/secret x composition appariee) pour separer le gain de l'alea, celui du secret et celui de la composition. A-T3 adopte un plan 2x2. B-T3 le transforme en trois bras a panel constant. C-T3 et D-T3 adoptent des variantes.

7. **Conjonction capture residuelle et gain absolu.** E (T2, contre C) montre que la conjonction de ces deux exigences peut rendre la region $H_A$ vide (si la capture est forte mais le gain operationnel nul, ou l'inverse). B-T3 adopte en separant les deux duels. C-T3 corrige en separant les revendications.

### 7.3 Points ou une espece contredit les quatre autres

1. **D sur le cout.** D est la seule espece dont le budget illustratif initial (4 000--15 000 USD, T1) depasse celui de toutes les autres d'un ordre de grandeur, et la seule a rejeter explicitement en T3 tout chiffrage comme premature. Les quatre autres proposent des budgets (A, C) ou refusent de chiffrer sans aller jusqu'a rejeter les ordres de grandeur des autres (B, E).

2. **C sur la substitution.** C est la seule espece a maintenir en T3 que la substitution d'activations est non interpretable en generation autoregressive (la greffe sort de la variete des activations). A et B maintiennent qu'elle est interpretable avec les controles croises. D et E sont plus prudents mais ne la rejettent pas comme test. Le dissensus est arbitrable par l'experience elle-meme (A-T3).

3. **A sur la complementarite comme filtre.** A est la seule espece a maintenir en T3 que la complementarite (capture residuelle sur les modes vus) sert de filtre : si elle est nulle, l'etau est improbable et l'experience d'etau passe apres. D et E rejettent ce role predictif. B et C ne se prononcent pas explicitement.

---

## 8. Ce qui a change par rapport au run v2.6 a trois especes

### 8.1 Refus et acceptations

Dans le run v2.6, trois especes avaient participe : A (Fable 5.1), B (Opus 5.5) et C (Argon). Fable avait produit les cellules T1-A (25 113 caracteres) et T2-A ; le « refus » rapporte a la sonde de pre-vol etait un artefact de troncature (64 jetons en reflexion, R-1821), non un refus de classifieur. Opus 5.5 avait refuse le tour T1-conception avec la categorie « cyber » et accepte T2. Le run avait produit 5 cellules sur 9 (T1-A, T1-C, T2-A, T2-B, T2-C), coupe par la limite de temps et non relance (ordre de Lazar). Aucune categorie « bio » n'avait ete invoquee sur la question v2.

Dans le run v9, les cinq especes ont accepte les trois tours, y compris Opus 5.5 qui n'a pas refuse T1. Deux especes nouvelles : D (Kimi K3.1 Pro, Moonshot) et E (Astra, OpenAI). Quinze cellules sur quinze. Zero refus. Ce fait est rapporte tel quel ; aucune conclusion causale n'est tiree sur les raisons du changement.

### 8.2 Passage de trois a cinq especes

Le run v2.6 avait produit 5 cellules (A, B et C, 3 tours incomplets). Le run v9 produit 15 cellules (A, B, C, D et E, 3 tours). Le passage de trois a cinq especes modifie la synthese en plusieurs points :

1. **Les convergences sont plus solides.** Dans le run v2.6, une convergence A-B-C pouvait refleter un accord entre deux fabricants (Anthropic pour A et B, Google pour C). Dans le run v9, une convergence a cinq especes de trois fabricants differents (Anthropic, Google, Moonshot, OpenAI) rend cet artefact moins probable.

2. **De nouveaux controles sont apparus.** Le run v2.6 avait identifie neuf elements dans la combinaison potentiellement non occupee. Le run v9 en identifie quatorze. Les cinq nouveaux (base qui relit, loi nulle honnete-contre-honnete, separation complementarite/etau, pression placebo, non jugeable comme issue formelle) proviennent pour la plupart des especes D et E, ou de l'approfondissement de la critique croisee a cinq.

3. **L'espace des metriques d'independance de l'oracle s'est diversifie.** Dans le run v2.6, B proposait un rapport conditionnel et C ne traitait pas la question separement. Dans le run v9, cinq metriques distinctes sont proposees (section 2), allant de la borne de Frechet-Hoeffding (B) aux contrastes normalises stratifies (D) en passant par les intervalles simultanes sur la probabilite conditionnelle (E).

4. **Le budget illustratif s'est elargi.** Dans le run v2.6, B proposait 3 000 a 10 000 USD et C environ 390 USD. Dans le run v9, l'ecart va de 150 USD (A) a « non chiffrable » (B, D, E), avec C a environ 3 680 USD.

### 8.3 Changements de fond

1. **La base qui relit n'existait pas dans le run v2.6.** Aucune des trois especes du run v2.6 ne l'avait proposee. A l'a introduite dans le run v9 (T1) et les quatre autres l'ont adoptee. C'est le changement de fond le plus consequent.

2. **La loi nulle honnete-contre-honnete n'existait pas dans le run v2.6.** B l'a proposee en T3 du run v9 comme « absence que personne ne mesure ». Elle conditionne desormais la validite du dommage diffus.

3. **La separation complementarite/etau etait absente du run v2.6.** Le run v2.6 confondait la capture residuelle et l'etau dans la meme experience (C : Experience 5, B : pince). Le run v9 les separe unanimement en deux grandeurs et deux experiences distinctes.

4. **L'intention de traiter etait absente du run v2.6.** Le conditionnement au dommage maintenu etait accepte implicitement. Le run v9 le rejette unanimement.

5. **Le non jugeable comme issue formelle etait absent du run v2.6.** Les trois especes du run v2.6 traitaient les intervalles qui traversent le seuil comme des resultats negatifs. Le run v9 les traite comme une issue de mesure a part entiere.

---

## Avertissement

Cette synthese est un produit du collisionneur, pas un audit. Ses affirmations d'anteriorite sont des HYPOTHESES. Elle doit etre relue par la session mere (« aucune recette ») avant tout usage, et ses references verifiees sur piece (R7) avant d'etre citees dans un papier ou une presentation.

La synthese a ete redigee par un sous-agent neuf qui n'a ecrit aucune des 15 cellules. Les 15 cellules ont ete lues dans leur integralite. Aucun passage decrivant « comment fabriquer » un comportement malveillant n'a ete identifie dans les cellules du run v9.

---

## Table des corrections v2 → v2b

La v2 (`abff231ff6c0ef79a7ed33dd7b1f9cb7daeaa07fdc4d574f48476eaea28e5748`) est conservee intacte (R12). Les corrections ci-dessous portent exclusivement sur des erreurs de fait dans les sections 8.1, 8.2 et 8.3, signalees par la session mere apres relecture. Les sections 1 a 7 et l'avertissement sont inchanges et attestes « aucune recette » par la mere.

| Section v2 | Texte v2 (errone) | Texte v2b (corrige) | Source |
|---|---|---|---|
| § 8.1 ¶ 1 | « seules les especes B et C avaient participe » | « trois especes : A, B et C » | releve mere, R-1821 |
| § 8.1 ¶ 1 | « A avait refuse les trois tours, categories bio et cyber » | artefact de troncature (64 jetons en reflexion, R-1821), T1-A et T2-A produits (25 113 car.) | R-1821 |
| § 8.1 ¶ 1 | (implicite : run termine) | 5/9 cellules, coupe par la limite de temps, non relance (ordre de Lazar) | releve mere |
| § 8.1 ¶ 1 | categorie « bio » invoquee | aucune categorie « bio » invoquee sur la v2 | releve mere |
| § 8.1 ¶ 2 | (manque : Opus n'a pas refuse T1 dans le v9) | « y compris Opus 5.5 qui n'a pas refuse T1 » ; D et E ajoutees | releve mere |
| § 8.2 titre | « de deux a cinq » | « de trois a cinq » | — |
| § 8.2 ¶ 1 | « 6 cellules (B et C, 3 tours) » | « 5 cellules (A, B et C, 3 tours incomplets) » | — |
| § 8.2 pt 1 | « convergence B-C, deux familles apparentees » | « convergence A-B-C, deux fabricants (Anthropic pour A et B, Google pour C) » | — |
| § 8.3 pt 1 | « aucune des deux especes » | « aucune des trois especes » | — |
| § 8.3 pt 5 | « Les deux especes du run v2.6 » | « Les trois especes du run v2.6 » | — |
