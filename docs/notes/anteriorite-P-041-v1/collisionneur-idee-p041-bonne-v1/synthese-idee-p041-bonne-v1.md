# Synthèse — l'idée P-041 est-elle bonne ? (ordre des coups) — v1

31 octobre 2026. Lecteur neuf (auteur de rien de ce qui est lu). Lus : envoi v3 (`1d285403…`, identique à `question-etage3.md`), faits v3 (`8ade357a…`), critères v3 gelés, `etat.md`, les douze cellules (empreintes égales à leurs compagnons, `sha256sum -c`), section 1 de `docs/notes/anteriorite-P-041-v1/note-anteriorite-P-041-workflow-v2.md` (`900db290…`). A Fable 5.1, B Opus 4.6, C Argon, D Kimi K3.1 Pro.

## Verdict

**Commun, trois pages sur quatre (B, C, D) : « bonne pour les deux », sous condition mesurable.** La condition : le bras 1 dépasse le bras 2 d'au moins l'effet minimal (3 points, illustratif) sur (ii) **et** sur (iii), et l'écart (ii) − (iii) du bras 2 dépasse celui du bras 1 d'au moins ce seuil. Les trois pages déclarent le même mode : θ est une cible auxiliaire prédite depuis les activations. A diverge : elle juge l'idée « plus probablement » bonne pour la conception et prédit un gain d'évaluation sous son seuil.
**La concordance porte sur la condition, pas sur l'issue prédite.** En support disjoint, le régime qui compte pour l'universalité, deux pages prédisent la condition « évaluation » remplie (B, C) et deux la prédisent manquée (A, D). Rien n'est construit ni mesuré (fait 3).
Verdict des modèles, ni décision ni porte. La collision avec Bailey et collègues ne change pas ce classement ; elle change la base à battre (section 6).

## 1. Les quatre pages du tour III.3 (critère 1)

Quatre pages lisibles : aucun refus, aucune écartée (critères 2, 17). C (Argon) compte comme proposition ; pas d'avis d'Argon à part (critère 16).

| Lettre | Modalité | Condition (seuil illustratif) | Repli écrit | Mode déclaré |
|---|---|---|---|---|
| A | conception (signalée : « plus probablement ») | support commun, bras 1 − bras 2′ ≥ 5 points sur (ii) et (iii), plus reparamétrisation sans chute | toute chute de reparamétrisation annule les deux verdicts | cible auxiliaire blanchie |
| B | les deux | conditions 1 à 3 : gains sur (ii) et (iii) ≥ 3 points ; reparamétrisation ; Δ > 3 points ; régime non précisé | conception si la condition 3 échoue ; « mauvaise » si la condition 2 échoue | cible auxiliaire (B abandonne l'entrée du tour III.1) |
| C | les deux | support disjoint à difficulté appariée ; gains ≥ 0,03 sur (ii) et (iii) ; Δ₁,₂ ≤ −0,03 (signe inversé par convention, même sens) | aucune si l'avantage disparaît en disjoint ou sous reparamétrisation | cible auxiliaire, tête linéaire |
| D | les deux | gains > δ_C sur (ii) et (iii) et R ≥ 0,03, « dans le régime considéré » | disjoint : au plus conception ; aucune si les gains disparaissent | cible auxiliaire, bras 2 à cible constante |

Citations :
- A — « conditionnel, plus probablement bonne pour la conception que pour l'évaluation ; aucune des deux n'est établie » ; « Δ₁₂ ≈ +3, donc sous Δ_min » (E3-T3-reponse-A).
- B — « bonne pour la conception ET pour l'évaluation, sous trois conditions mesurables » ; « Si les conditions 1 et 2 sont remplies mais pas la condition 3 : bonne pour la conception seulement » (E3-T3-reponse-B).
- C — « conditionnellement bonne pour les deux (conception et évaluation) » ; « le verdict rétrograde immédiatement à **bonne pour aucune** » (E3-T3-reponse-C).
- D — « Le verdict conditionnel est **bonne pour les deux** » ; « En support disjoint, si seuls les gains sur (ii)/(iii) subsistent, elle est au plus bonne pour la conception » (E3-T3-reponse-D).

**Pourquoi « commun ».** Les conditions de B, C et D portent sur les mêmes contrastes (bras 1 contre bras 2 sur (ii), sur (iii), et double différence sur (ii) − (iii)), dans le même sens. Les seuils diffèrent peu (3 points chez B et C, 0,03 chez D ; δ_C n'est pas chiffré dans la page de D, mais l'était à 0,03 dans E3-T1-conception-D). Un seuil différent ne rompt pas la concordance (critère 1). Le mode est le même : c'est la modalité « cible à prédire depuis les activations » de l'envoi. B l'écrit : « Ce mode est celui de la proposition A ; je le reprends explicitement » (E3-T3-reponse-B).

**Je rapporte, sans que cela rompe la concordance :**
1. Le régime diffère. C limite sa condition au support disjoint, D l'applique à chaque régime, B ne dit pas le régime.
2. Le bras 2 diffère : tête à gradients jetés (A), tête à cible constante (D), bras nu plus témoin 2′ (C), bras nu plus contrôle à θ permuté (B). Tous restent le bras 2 de l'envoi, mais un résultat ne se transpose pas tel quel d'une page à l'autre.
3. Les branches de repli divergent. Si le gain d'évaluation manque, B donne conception et D au plus conception (en disjoint), tandis que C donne aucune. Le critère 1 compare ces branches sans rompre le verdict commun.

A reste divergente. Le choix entre « conception » et « verdict sans condition mesurable » ne change rien au compte, car aucune des deux lectures ne concorde avec B, C, D.

## 2. L'issue prédite : là où le verdict se partage

Je lis les tableaux de prédictions de (ii) − (iii) (illustratifs) comme une double différence, bras 2 moins bras 1 :
- B : +4 points en commun, +5 en disjoint, au-dessus de son seuil de 3 dans les deux régimes (E3-T1-conception-B : bras 1 « 8 pp » et « 15 pp », bras 2 « 12 pp » et « 20 pp »).
- C : « prédiction illustrative $-0{,}04$ », soit un gain de 4 points dans les deux régimes (E3-T3-reponse-C).
- D : +6 points en commun, −1 en disjoint (E3-T1-conception-D) ; puis « sous le seuil en support disjoint (**HYPOTHÈSE**) » (E3-T3-reponse-D).
- A : +3 points, sous son seuil de 5 points, dans les deux régimes (E3-T3-reponse-A).

En support disjoint, B et C attendent donc « les deux », tandis que A et D n'attendent au mieux que « conception ». Le régime disjoint est celui de l'universalité (fait 1). B le relève dans sa critique de D : « le régime pertinent est le support disjoint, précisément celui où D n'a pas de prédiction claire » (E3-T2-critique-croisee-B). D l'accepte : « le support disjoint est prioritaire pour la prétention d’universalité » (E3-T3-reponse-D). **Le verdict commun dit à quelle mesure l'idée serait bonne, non qu'elle l'est.**

## 3. Ce qui a convergé entre le tour III.1 et le tour III.3

Corrections venues de la critique croisée, non de conceptions indépendantes (critère 15 : absentes de tout le tour III.1, sauf mention).
1. **Trajectoire commune aux bras 1 et 2.** Au tour III.1, les quatre pages couplaient les deux bras dans une boucle adaptative (critère 6, signalé pour les quatre). C le relève à propos de A : « C'est un dilemme méthodologique non résolu » (E3-T2-critique-croisee-C). D le relève aussi : « Le couplage des bras 1 et 2 est incompatible avec leur boucle adaptative » (E3-T2-critique-croisee-D). Au tour III.3, les familles des deux bras sont produites contre une défense de pilotage tierce. A dit le prix de ce choix : « sur la trajectoire commune, la boucle n'est plus adaptative aux défenses comparées » (E3-T3-reponse-A). C'est un élément nouveau.
2. **Score (iii) réévalué sur des tirages frais.** C le faisait déjà au tour III.1 (« puis réévalué sur $L=200$ lots frais », E3-T1-conception-C) : l'élément n'est pas nouveau. A l'adopte, sur un constat de biais d'extrême (E3-T3-reponse-A).
3. **Appariement de la difficulté par la puissance oracle p\*.** L'oracle est proposé par A au tour III.2 (« tout écart de l'oracle est difficulté intrinsèque, à soustraire », E3-T2-critique-croisee-A), puis repris par A, C et D au tour III.3. C'est un élément nouveau.
4. **Test de reparamétrisation déplacé vers l'entraînement.** B l'appliquait « **après le gel de la défense** » (E3-T1-conception-B). Le test était donc non informatif (critère 7) : « Test de reparamétrisation nul par construction » (E3-T2-critique-croisee-A). B le corrige (E3-T3-reponse-B).
5. **Validation de la convergence de la tête auxiliaire.** Le contrôle de convergence et le témoin de capacité 2′ (« gradients sont calculés puis *jetés* ») viennent de B au tour III.2 (E3-T2-critique-croisee-B). A et C les chiffrent au tour III.3 par R² ≥ 0,5 (E3-T3-reponse-A, E3-T3-reponse-C). C'est un élément nouveau.

## 4. Ce qui reste divergent et dont dépend la condition

**Le test de reparamétrisation n'est pas le même d'une page à l'autre.** Or les quatre verdicts dépendent de son issue.
- D : « scelle \(g\) dans une classe d’isométries affines » (E3-T3-reponse-D).
- A : « toute φ affine est neutralisée par construction ; le test n'est informatif que par la composante **non linéaire monotone** » (E3-T3-reponse-A).
- A à propos de C, au tour III.2 : « Toute bijection lisse φ est absorbable par une tête de capacité suffisante » (E3-T2-critique-croisee-A).
- C répond par une tête strictement linéaire et un difféomorphisme cubique couplé (E3-T3-reponse-C) ; B oppose une transformation anisotrope à un témoin isométrique (E3-T3-reponse-B).

Si l'on suit l'argument de A, le test de D pourrait n'avoir aucune puissance. Chez D, la condition d'absence de chute serait alors remplie par construction. Aucune page ne le tranche ; A le range en non établi : « Que le test de reparamétrisation sépare lois et paramétrisation : cela dépend de la classe φ » (E3-T3-reponse-A).

## 5. Signalements par critère (compte rendu, sans réécriture)

- **Critère 4 (tour III.1).** (iii) sans réévaluation chez A (« min sur les θ explorés », E3-T1-conception-A), unité ambiguë chez D ; corrigés au tour III.3.
- **Critère 5.** B prend comme contrôle « indépendance exacte (graines séparées, régions disjointes de Θ) » (E3-T1-conception-B) ; or une graine séparée n'est pas une absence de dépendance. Le contrôle de A est inversé (accepté par A dans E3-T3-reponse-A). La validation de C est tautologique (« retrouve $D$ à $10^{-4}$ près », E3-T1-conception-C).
- **Critère 6.** « Contrôle négatif : Bras 3 » chez B (E3-T1-conception-B), qui n'est pas un nul ; budget de A sans les évaluations du générateur ; corrigés au tour III.3.
- **Critère 6 bis (tour III.1).** Fin de légitimité : A à l'étalonnage, plus une étape nommée, le « **gel** » ; B « à partir de l'étalonnage du seuil » ; C « dès la fin de l'entraînement des poids » ; D dès que l'information d'évaluation alimente sélection ou étalonnage. Au tour III.3, A rejoint C : « **sélection sur la perte de détection seule** » (E3-T3-reponse-A).
- **Critère 6 ter.** Les quatre tableaux ont leurs dix cases, signées et marquées illustratives. La condition d'échec de C était en « ET » au tour III.1, en contradiction avec le bloc 5 (E3-T2-critique-croisee-A), puis corrigée. C écrit « assurant une puissance $> 90\,\%$ » (E3-T3-reponse-C) : c'est une puissance présentée comme calculée, je la signale.
- **Critère 8.** Au moins deux duels sont retenus par page. Les duels 1 et 2 de B tiennent formellement, mais l'un a un contrôle négatif mal construit et l'autre une puissance nulle.
- **Critère 9.** Jugeable pour les quatre.
- **Critère 11.** B écrit « si le fait 11 se confirme (transfert négatif hors classe) » (E3-T3-reponse-B), alors que le fait 11 donne un signe mitigé.
- **Critère 12.**
  - C range une question parmi les faits rapportés : « RAPPORTÉ : Recevoir $\theta$ à l'entraînement diffère structurellement » (E3-T1-conception-C) ; or l'équivalence est une question.
  - C qualifie aussi ses propres affirmations « (VÉRIFIÉ par calcul) », sans formule (E3-T3-reponse-C).
  - B écrit « Le signe (ii) − (iii) > 0 est **établi sous la condition** » (E3-T3-reponse-B) ; c'est une hypothèse.
  - C cite « *born-again networks* » sans « référence à vérifier » (E3-T2-critique-croisee-C).
  - Aucun identifiant arXiv n'est donné par un modèle.
- **Critère 13.** Chez B, l'expérience corrigée est en section (b), hors de la page (c) (E3-T3-reponse-B) : je le signale. A, C et D ont les quatre éléments, en cinq lignes au plus, plus la ligne « à faire en premier ».
- **Critère 14.** Au-delà de 2 500 mots selon `wc -w` et selon les seuls mots à lettre : E3-T2-critique-croisee-C (4 416 ; 3 977), E3-T3-reponse-C (3 156 ; 2 657), E3-T2-critique-croisee-B (2 841 ; 2 561). Selon `wc -w` seulement : E3-T3-reponse-A (2 904), E3-T1-conception-B (2 686), E3-T1-conception-C (2 684), E3-T1-conception-A (2 502).
- **Critère 17.** Aucun refus ; E3-T2-critique-croisee-D a pris deux essais (OK), cause non lue.

## 6. Antériorité connue depuis le tour

D'après la section 1.1 de la note (RAPPORTÉ pour moi, PDF non relus ; R7), le cœur technique de P-041 est publié, avec un résultat négatif. Ce cœur, c'est une défense réentraînée contre les attaques passées, dans l'espace des activations, au rappel à 1 % de fausses alertes. La source : Bailey et collègues, `2412.09565v2`, §3.5, p. 11–13 : « adversarial training techniques do not easily lead to robust monitors ». La matrice (1.2, ligne 1+2) précise : « la défense connaît les instances passées, pas les paramètres ». Bailey n'apparaît ni dans les faits servis, ni dans l'envoi, ni dans aucune cellule (vérifié par recherche dans les fichiers).

**Ce qui ne change pas.**
1. Le classement : je rapporte le verdict des modèles sur les faits reçus.
2. L'objet de la condition : la défense de Bailey est l'analogue réel des bras 2 et 4 (instances, sans θ) ; le gain de θ sur le bras 2 n'est donc pas ce que Bailey occupe. La matrice range d'ailleurs « 2 au sens exact de P-041 … réunie avec 5 » parmi les combinaisons non trouvées, à vérification forte (1.3).
3. Les prédictions : les quatre tableaux donnent (ii) − (iii) positif pour tous les bras, 2 et 4 compris, ce qui est cohérent avec Bailey.

**Ce qui change.**
1. **Ce que la condition doit battre.** Si P-041 a une revendication, ce n'est plus que l'incrément de θ sur une défense dont l'analogue publié échoue. Les pages présentent la non-trouvaille comme établie, ce qui les rend incomplètes, pas fausses : « La réunion … n'a pas été trouvée, recherche non exhaustive (fait 12, RAPPORTÉ) » (E3-T3-reponse-A).
2. **Un argument a priori contre le gain dans la classe.** La note rapporte, d'après le test d'hypothèses robuste (Barni et Tondi ; Tondi, Merhav et Barni) : « l'information au-delà du paramètre de classe n'a donc de valeur qu'**hors** de la classe déclarée ». Or, par le cadre de la question, tous les régimes de l'expérience corrigée restent dans le schéma déclaré, y compris le sous-espace disjoint de C. À l'optimum, l'avantage de θ sur le score (iii) devrait donc s'annuler ; tout gain mesuré serait un effet de budget fini. Cela penche vers les prédictions de A et de D, et expose le plus la prédiction de C en support disjoint. Réserve : lois gaussiennes ou alphabets finis, exposants asymptotiques, non vérifié par moi.
3. **La portée d'un succès simulé.** La note (1.3) rappelle qu'un succès sur activations synthétiques « ne se traduit pas » toujours sur des activations réelles. Une condition remplie en simulation ne réfuterait pas Bailey.

## 7. Décisions

**Décision 1 — nœud de décision.** Décision : fixer ce que P-041 revendique encore, après Bailey, avant tout préenregistrement. Enjeu : « zone revendiquée trouvée occupée » est un nœud ; le cœur est occupé, avec un résultat négatif.
- (a) Restreindre la revendication à l'incrément de θ sur une base de type Bailey : les bras 2 et 4 deviennent la réplique de cette base au niveau des lois. Avantage : l'expérience corrigée des espèces reste telle quelle. Inconvénient : un positif en simulation ne réfute pas un négatif sur activations réelles.
- (b) Abandonner P-041 comme idée de conception et garder l'instrumentation. Avantage : aucun pari sur une zone à résultat négatif. Inconvénient : on perd la seule partie non trouvée.
- (c) D'abord faire vérifier Bailey sur PDF par un lecteur neuf (R7), puis choisir entre (a) et (b). Avantage : rien n'est opposable avant cela. Inconvénient : délai.

Recommandation : (c) puis (a), confiance moyenne. **Aucun défaut : nœud, j'attends ton GO.**

**Décision 2 — proposer avec recommandation.** Décision : rédiger, sans le sceller ni le lancer, le préenregistrement d'un pilote de jugeabilité sur processeur. Enjeu : sans tête, générateur et test de reparamétrisation validés, la condition est non jugeable ; A, C et D mettent ce pilote en premier : « si l'une échoue, aucun des W = 200 mondes n'est lancé » (E3-T3-reponse-A) ; « avant tout entraînement comparatif des bras » (E3-T3-reponse-D).
- (a) Pilote des instruments, avec en plus un facteur de budget (deux budgets totaux) pour tester l'effet de budget fini du point 2 de la section 6. Avantage : il sert quelle que soit l'issue de la décision 1. Inconvénient : il ne tranche rien sur θ.
- (b) Commencer par le duel de reparamétrisation, comme B. Avantage : bon marché. Inconvénient : la classe de transformations est disputée (section 4).
- (c) Rien avant la décision 1. Avantage : aucun travail perdu. Inconvénient : délai.

Recommandation : (a), confiance moyenne. Défaut sous 48 heures : (a) rédigé et laissé non scellé et non lancé tant que la décision 1 n'est pas tranchée.

**Décision 3 — dépense.** Décision : rejouer ou non l'étage 3 avec Bailey servi comme fait 16 (RAPPORTÉ). Enjeu : les espèces ont répondu sans connaître la collision.
- (a) Rejouer. Avantage : verdict informé. Inconvénient : dépense (run de référence : 8,16 USD, `etat.md`).
- (b) Ne pas rejouer et verser Bailey directement au préenregistrement. Avantage : sans dépense. Inconvénient : aucune contre-lecture des espèces.

Recommandation : (b), confiance moyenne, parce que le contraste tranché (θ contre échantillons) n'est pas celui que Bailey occupe. **Aucun défaut : c'est une dépense.**

## 8. Réserves

- **Dépendance entre espèces de même lignée.** A (Fable 5.1) et B (Opus 4.6) sont de la même lignée. Elles divergent sur la modalité, mais B a repris explicitement le mode de A (E3-T3-reponse-B). D a quitté son « maître » distillé après la critique de A (E3-T3-reponse-D, critique A.a1). La concordance de mode du tour III.3 vient donc en partie du tour III.2. Ce ne sont pas trois votes indépendants.
- **Effet de la question.** Les conditions de B, C, D reprennent les définitions du bloc 5 : leur concordance apporte peu. La question garde tout dans le schéma déclaré (là où l'argument de la section 6 prédit le moins de valeur pour θ), énonce d'avance l'hypothèse de reparamétrisation, et ne sert ni Bailey ni le test d'hypothèses robuste.
- **Non vérifié.** Aucune simulation ; chiffres des cellules illustratifs ; Bailey, Barni et Tondi lus à travers la section 1 de la note seulement ; comptes de mots approchés ; relevé des chiffres non marqués « illustratif » non exhaustif ; `journal.jsonl` et `essais/` non lus.
