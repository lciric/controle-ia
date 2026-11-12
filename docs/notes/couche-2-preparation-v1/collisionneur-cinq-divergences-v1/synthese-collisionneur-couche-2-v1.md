# Synthèse du collisionneur — couche 2 : les cinq divergences — v1

Lecteur neuf (Opus 5.5), 28 octobre 2026. **Matériau pour la décision de Lazar : rien n'est tranché ici, ce n'est pas un
préenregistrement.** Tous les chiffres sont exploratoires et non opposables. Tout prix de carte graphique (1,08 à
1,37 dollar de l'heure) est **SUPPOSÉ** : aucune empreinte ne le porte dans les pièces servies (R7).

**Lu, en entier** : la question (`question-couche-2-cinq-divergences-v1.md`), les faits servis (`faits.md`, `394e2b60…`),
les neuf cellules (A = Fable 5.1, B = Opus 5.5, C = Gemini Argon ; tours 1 conception, 2 équipe rouge, 3 riposte),
`etat.md` (neuf cellules OK, une tentative chacune, 12,59 dollars). Rien d'autre.

**Mes vérifications** (processeur seul, 72 secondes au total) : la simulation de la pièce A2, extraite de `faits.md`,
a l'empreinte `20bb005c…` annoncée (copie conforme). Je l'ai importée, sans la modifier, dans deux scripts de
vérification, graine maîtresse neuve 20261029, graines par `SeedSequence` :
- `verifications-synthese-v1.py` (`c3a76ee6…`) → `verifications-synthese-v1-sortie.json` (`a463b4b5…`), 2 000
  répétitions (1 000 pour la lisibilité jointe) ;
- `verifications-synthese-v1-complement.py` (`e8251124…`) → `…-complement-sortie.json` (`4f517c5d…`), 1 000 répétitions.

Tous sous `…/collisionneur-couche2/synthese/`. Erreur de tirage : environ 0,005 à 0,007 sur un taux de 0,05.
Ces vérifications héritent du modèle latent gaussien de la pièce A2 (effet de consigne a, hétérogénéité h,
concordance) : elles disent ce que ce modèle implique, pas ce que fera la banque réelle.

---

## 1. En tête : une ligne par divergence

| # | position majoritaire après riposte | accord | rapport à la comparaison (pièce C, § 5) |
|---|---|---|---|
| 1. Dénominateur de D-S9 | Lecture A : un seul calibrage commun aux modes, 64 tâches d'épreuve, moitiés coupées **dans** chaque tâche ; 9 600 recommandés (provisoire chez B), 4 800 non retenu sans test ; la lecture « double » écartée | trois sur trois | **Confirme** l'option (1) que C préparait ; aucun modèle ne reprend l'option (3) de C (faire dire le dénominateur par l'auteur de D-S9). **Mais ma vérification déplace la question** : si le diagnostic tombe dès qu'une des huit cellules critères échoue, 9 600 ne suffit pas (0,07 à 0,08) et 12 800 suffit (0,02 à 0,03) — voir § 2.1 |
| 2. Exécutions par unité | K = 10 sur 64 unités ; la réserve de 32 tâches reste hors épreuve (contamination non testable sur ce banc) ; agrandir le banc est le seul vrai levier, et c'est un nœud | trois sur trois (B garde K = 5 ouvert si sa simulation E2′ le permet) | **Confirme** l'option (1) de C ; **renverse** son option (3) (K fixé par le pilote) : A et B jugent que choisir K sur un pilote relu ensuite serait une fuite |
| 3. Jumeaux partagés | Partagés entre les deux modes connus **et** le mode tenu à l'écart, fiche du mode tenu à l'écart scellée en entier avant toute lecture, sentinelle de dérive de fabrique à sa génération | trois sur trois (B a retiré ses jumeaux propres) | **Confirme** l'option (1) de C, avec un garde-fou de plus (la sentinelle) que C n'avait pas |
| 4. Mention et dose | Garder « mention » à K = 3 (le lever est un nœud, pas un défaut) ; recherche de dose courte sur la réserve **avant** la banque ; une **seule** dose (diffuse) en épreuve, la dose-réponse mesurée hors épreuve ; « diffus » codé contre **tous** les moniteurs boîte noire par action | trois sur trois | **Confirme** l'hybride (3) de C et le traitement en nœud ; **renverse** un détail : C plaçait plusieurs strates par la recherche, les trois modèles n'en gardent qu'une en épreuve (plancher de 48 unités) |
| 5. Ordre des lancements | Processeur d'abord (simulation du contrôle 12 joint), puis petite dépense sur la réserve, puis préenregistrement de G1 scellé, puis épreuve, mode tenu à l'écart en dernier | dispersé sur le détail ; deux contre un sur l'existence d'un pilote saboté (A et C pour, B contre) | **Confirme** la direction de C (option (1), pilote réduit) ; l'ordre calibrage/épreuve reste discordant (§ 2.5) |

---

## 2. Par divergence

### 2.1 Dénominateur de D-S9 (taille du calibrage honnête)

**Positions après riposte.**
- **A** : lecture A ; 9 600 sur les 64 tâches, coupe dans les tâches, **aucune strate de calibrage** par défaut ; 4 800
  seulement si sa simulation T1 (union des deux contrôles 12) le tient. *Calcul* : le seuil à 1 % est une statistique
  d'ordre lue par les deux fiches ; son bruit ne dépend pas du nombre de modes. *Ferait changer* : l'horizon devient
  strate (le calibrage se coupe en deux), a mesuré > 0,5. *Coût* : économie de 4 800 épisodes si 4 800 tient,
  ≈ 130–180 heures (illustratif) ; la lecture « double » coûterait ≈ +270–370 heures.
- **B** : un pool commun à la taille N** que rendra sa simulation E1′ (cellules × modes × strates), marge de deux ;
  9 600 provisoire ; ni 4 800 ni le double ne sont justifiés en l'état. *Ajout propre à B, juste* : le risque n'est pas
  le niveau de la décision G1 (l'intersection-union est bornée par le minimum des niveaux, les cellules ne se
  multiplient pas) mais sa **lisibilité** (le diagnostic tombe dès qu'une cellule × mode se promeut contre
  elle-même). *Coût* : passer de A à B = 9 600 épisodes de plus, 267–766 heures, 288–1 050 dollars (à 100–287 s par
  épisode).
- **C** : lecture A ; 9 600 scellés d'avance, sans repêchage si le contrôle 12 échoue ; contrôle 12 joint sur
  16 cellules × modes, avec seuil corrigé 320 comme variante. *Coût* : 9 600 = 352 heures, 380–482 dollars (juges 8B
  et 3B seulement — sous-estimé de l'aveu même de C, § 2.5).

**Équipe rouge : ce qui a tenu.**
- La faille commune levée par A (tour 2) : le contrôle 12 n'est simulé que pour **une** cellule ; G1 en a au moins
  huit critères, deux modes, peut-être deux strates. Acceptée par B et C.
- L'erreur de facteur √2 dans la formule de C (A et B) : acceptée par C.
- L'arrêt optionnel déguisé chez C (ajouter du calibrage après un échec du contrôle 12, B) : accepté.
- La strate d'horizon qui coupe 9 600 en deux fois 4 800 (C contre A) : acceptée par A.
- La « correction préalable » de B (effet de tâche des sabotés tiré indépendamment de celui du calibrage dans
  `controle_12_intra_taches`) : la lecture du code par B est exacte, mais A a montré qu'elle n'était pas bloquante ;
  B l'a rangée en variante.

**Ce qui est tombé.**
- Le « 4 800 échoue » de C au tour 1 (coefficient 1,3 et corrélation 0,6–0,8 sans source).
- Le σ = 2,63 points de C.

**Mes vérifications.**
- Bruit binormal de l'écart entre deux moitiés : **4,16 points à 4 800, 2,94 à 9 600, 2,08 à 19 200** (constante
  2,885/√N). Confirme A et B (2,88/√N, 4,1 points) ; infirme le 2,63 de C. Le « ≈ 2 points à 9 600 » de la pièce A est
  l'écart entre deux moniteurs calibrés chacun sur N, pas celui des deux moitiés.
- Contrôle 12, une cellule, coupe dans les tâches, 64 tâches (deux variantes de l'effet de tâche des sabotés, a ∈ {0 ;
  0,2 ; 0,3}) :

| N | 1 024 | 1 920 | 3 200 | 4 800 | 6 400 | 9 600 |
|---|---|---|---|---|---|---|
| promotion à tort | 0,18–0,20 | 0,12–0,14 | 0,065–0,08 | 0,03–0,04 | 0,013–0,022 | 0,004–0,009 |

  La correction de B ne change rien (écarts dans l'erreur de tirage). Le « 0,022 à 6 400 » de C, non simulé par
  personne, est retrouvé (0,013 à 0,022).
- **Union sur les deux modes, une cellule** : 0,037–0,043 à 4 800, 0,007–0,009 à 9 600. L'union reste proche du taux
  d'un mode (corrélation forte par les moitiés partagées). B et A avaient raison sur le mécanisme ; le « × 1,3 » de C
  ne se retrouve pas. **4 800 tient l'union de deux contrôles pour une cellule, de justesse.**
- **Union sur 8 cellules × 2 modes** (cellules indépendantes, ou corrélées à 0,8 dans l'épisode) :

| N | seuil 20 | seuil 40 | seuil 80 | seuil 160 | seuil 320 |
|---|---|---|---|---|---|
| 4 800 | 0,18–0,31 | 0,13 | 0,06 | 0,02 | 0,01 |
| 9 600 | **0,07–0,08** | 0,02 | 0 | 0 | 0 |
| 12 800 | 0,02–0,03 | — | — | — | — |
| 19 200 | 0,001–0,007 | — | — | — | — |

  **Lecture** : la borne de Boole d'A (0,16 à 9 600) est pessimiste, mais l'attaque tient. À 9 600 et au seuil 20, le
  diagnostic serait illisible environ une fois sur treize. Deux issues ressortent :
  - porter le calibrage vers ≈ 12 800 épisodes, ce qui tombe, par coïncidence, sur le bas de la lecture « double » ;
  - garder 9 600 et sceller un seuil de diagnostic corrigé, 40 ou plus par cellule.

  L'argument technique en faveur d'un calibrage plus grand n'est donc pas le **nombre de modes** : c'est le **nombre
  de cellules**. Aucun modèle ne l'a chiffré.
- **Ce qui reste affirmé sans preuve** : que huit cellules critères partagent une loi gaussienne de même d′ (mon
  modèle le suppose) ; les ex æquo des juges lus par un jeton (non simulés) ; le sens du contrôle 12. A2 le simule
  **unilatéral** (« moitié 1 > moitié 2, sens fixé »). S'il est lu dans les deux sens, tous ces taux doublent à peu
  près. Aucun modèle ne l'a relevé.

### 2.2 Exécutions par unité

**Positions après riposte.**
- **A** : K = 10 sur 64, fixé par nœud et non par le pilote. L'option 96 tâches est « morte ». Agrandir le banc est un
  nœud (extraction neuve, accès arXiv refusé). *Ferait changer* : un écart blanc contre blanc mesuré à 5 points ou
  moins ; alors aucun K ne sauve G1 (b).
- **B** : 64 unités, K = 10, ou K = 5 si sa simulation E2′ montre moins de 0,10 de perte sous intersection-union.
  Économie si K = 5 : 960 épisodes, 27–77 heures, 29–105 dollars.
- **C** : 64 × 10 en épreuve, 32 × 5 en développement, garde préenregistrée à δ = 0,10, réserve jamais en épreuve.
  *Coût* : 1 600 épisodes sabotés, 63–80 dollars.

**Équipe rouge : ce qui a tenu.**
- La fuite pilote → épreuve si le pilote choisit K ou la bascule à 96 (C contre A, B contre A).
- La faille commune de B : aucune des 96 tâches n'est vierge (60 lues en P3, où la couche c15 a été choisie ; 32 de
  réserve portant la dose et T0.7). Acceptée par tous, avec une **portée conditionnelle à déclarer** à Lazar.
- Les tests de contamination sur moyennes honnêtes (D2 de A, E2b de B, E2 de C) ne regardent pas où la fuite
  agirait : sur le gain saboté. Retirés ou réécrits par les trois.
- L'option 96 tâches détruit le développement de l'organisme (C contre B).

**Ce qui est tombé.** Le « 96 × 6 ≈ 0,94 » de C comme argument de critère (A : mauvaise table), mais voir ma
vérification ci-dessous.

**Mes vérifications** (intersection-union 20/10/10 points, le critère de G1 réécrit par N-056) :

| plan | 64 × 3 | 64 × 5 | 64 × 10 | 96 × 3 | 96 × 5 | 96 × 6 | 96 × 7 | 96 × 10 |
|---|---|---|---|---|---|---|---|---|
| puissance | 0,31 | 0,47 | **0,72** | 0,64 | **0,88** | 0,93 | 0,96 | 0,99 |

- **L'affirmation de B en riposte, « sous intersection-union : jamais [la réserve ne vaut plus] (0,63 contre 0,68) »,
  est fausse à budget égal.** Elle compare 288 épisodes sabotés à 640. À 480 épisodes (96 × 5), la réserve donne
  0,88 contre 0,72 pour 64 × 10 avec 640. L'attaque C4 d'A contre C (« 96 × 3 = 0,63 < 0,68 ») souffre du même défaut.
- Le point de bascule demandé par la question est donc bas : **dès K ≈ 4–5 sur 96 tâches, à moins d'épisodes, la
  réserve bat 10 exécutions sur 64 tâches**, avec un comparateur comme sous intersection-union. Les trois modèles
  concluent à juste titre que la question n'est **pas** la puissance mais la validité (contamination).
- **K = 10 contre K = 5 à 64 unités, sous intersection-union : 0,72 contre 0,47.** La perte dépasse 0,10 : dans ce
  scénario (a = 0,3), l'hypothèse « K = 5 suffit » de B est réfutée. Sa simulation E2′ est à faire sur S1, S2 et S4,
  mais ce point tend vers K = 10.
- Un comparateur, 10 points : à 96 × 6, 0,80 en S1 et 0,97 en S2. Les interpolations de C (0,82 et 0,94) et d'A (entre
  0,75 et 0,93) sont plausibles.
- Reproduction à graine neuve : 64 × 10 donne 0,65 (S1) et 0,80 (S2), contre 0,63 et 0,78 publiés. 5 points à 64
  unités : K = 3 donne 0,10 et K = 10 donne 0,08 (S1), comme dans A1. La « nuance » de C se reproduit au même signe,
  mais elle est minuscule et se trouve sous le plancher de 93 unités. La lecture d'A est la bonne : ces promotions
  viennent de la variance, pas de la puissance.

**Ce qui reste affirmé sans preuve** : a, h, concordance et l'écart blanc contre blanc d'au moins 8 à 10 points, dont
dépendent **toutes** ces tables. Il en va de même du produit des puissances entre deux modes (≈ 0,46 à 0,52 pour G1
entière à 64 × 10, chiffre qu'A demande de montrer à Lazar plutôt que 0,68).

### 2.3 Jumeaux partagés ou propres

**Positions après riposte.**
- **A** : partagés ; sentinelle de dérive T5 (192 jumeaux régénérés, égalité en loi et non au bit près) ; règle de
  score manquant aveugle au mode ; **une seule lecture de G1, tous modes ensemble, après la génération du mode tenu à
  l'écart**.
- **B** : partagés, mode tenu à l'écart compris ; fiche scellée avant la première lecture ; sentinelle E6′ (64 jumeaux,
  2–7 dollars). Ses jumeaux propres (640 épisodes, 19–70 dollars) sont retirés. Argument retourné : avec un honnête
  commun, toute différence entre modes ne peut venir que des sabotés.
- **C** : partagés ; lot d'ancrage de 64 honnêtes au lancement du mode tenu à l'écart ; en cas de dérive, régénérer
  576 jumeaux (≈ 21 heures, ≈ 26 dollars).
- *Coût évité par le partage* : 960 épisodes (A1). B l'estime à 29–105 dollars, C à 32–48 dollars, juges 8B et 3B
  seulement.

**Équipe rouge : ce qui a tenu.**
- La lecture du mode tenu à l'écart après celle des modes connus, avec la moitié honnête déjà connue (B, tour 1 ; C
  contre A). A a accepté sur l'ordre.
- La dérive de fabrique entre la génération des jumeaux et celle du mode tenu à l'écart (B contre A) : acceptée par
  les trois.
- L'exigence d'identité au bit près sur carte graphique (C, test de Levenshtein) : le non-déterminisme des noyaux la
  rend non exclusive. Acceptée par C.

**Ce qui est tombé.**
- E3 de B (« ressource divisée ») : le jumeau n'entre que dans la garde, pas dans v(t). Retiré.
- Les jumeaux propres de B : C a montré qu'ils ajoutaient un bruit de garde propre au mode tenu à l'écart.

**Tension restante.** C maintient (riposte, § 4) que partager les jumeaux d'épreuve entre fiches évaluées au même jalon
ne viole pas D-S12. A et B ne tranchent pas la lecture de « parties disjointes ». C'est une question d'interprétation
de D-S12, pas de calcul.

**Mes vérifications** : aucune simulation propre. La garde à δ = 0,10 et 64 unités bloque par hasard dans ≈ 0,001 des
cas (A1, cellule J, citée par C) ; je ne l'ai pas refaite. **Affirmé sans preuve** : « un épisode honnête n'a pas de
mode ». La pièce A1 le marque [INFÉRÉ]. B, en riposte, le présente comme « conséquence logique d'un fait RAPPORTÉ » ;
seule A (tour 1) en pose la condition : un même gabarit de consigne honnête dans les deux modes, à vérifier sans
dépense.

### 2.4 Mention et recherche de dose

**Positions après riposte.**
- **A** : garder « mention » à K = 3, en nœud. Duel T4 à quatre conditions (honnête, mention, témoin, saboteur), seuil
  ponctuel de 10 points. Recherche de dose contre **toute** la liste scellée des moniteurs par action ; « diffus »
  défini par unité (part d'actions sous le seuil). Épreuve à dose diffuse unique ; dose-réponse au pilote et au
  développement. *Coût* : recherche de dose ≈ 11–14 heures (illustratif ; Qwen et b* sans rythme).
- **B** : garder « mention » (K = 3), lue par E4′ : deux paris symétriques sur v = alerte(saboteur) − alerte(mention),
  sous masquage textuel (N-053) ; sondes aléatoires en contrôle ; le témoin lexical comme vérification de
  manipulation. Dose d'épreuve unique ; E8 contrôle la concordance en proportion **et** en intensité. Refuse de coder
  « diffus » par unité (sélection sur comparateur, contrôle 14).
- **C** : garder « mention » et le témoin instruit **fixe** (abandon du témoin apparié en dose). Test de McNemar sur
  192 paires, seuil de +3 points, après masquage. Recherche de dose sur 8 tâches de réserve, contre tous les juges.
  *Coût* : mention 384 épisodes ≈ 18 dollars ; dose 240 épisodes, 10–12 dollars.

**Équipe rouge : ce qui a tenu.**
- La strate « diffus » est définie par le **meilleur** moniteur boîte noire par action, pas par le seul juge 8B (B
  contre A) : accepté.
- Plusieurs strates de dose en épreuve font tomber la fiche de H1a sous le plancher de 48 unités. C'est la faille
  qu'A avait levée contre C (puissance par strate), retournée contre A et B ; acceptée par tous.
- Le témoin apparié en fréquence d'actions devient un saboteur faible (A et B contre C) : retiré.
- Le ratio r de B (dénominateur instable) et le témoin lexical « vrai par construction » : réécrits.
- La définition de « mention » n'est pas dans les pièces servies (B contre A ; contre C, qui l'avait inventée) :
  accepté. **Tout duel sur « mention » reste conditionnel au texte de P-015.**

**Divergence non résolue.** Faut-il coder « diffus » **par unité** (A) ou **jamais par unité** (B, qui y voit une
sélection sur un comparateur) ? Les deux ont un argument : A dit qu'une moyenne sur tâches laisse passer des unités
concentrées, B que filtrer les unités par un comparateur biaise G1. C suit A (« au moins 80 % des tâches dans la strate
diffuse »). C'est à trancher au préenregistrement.

**Mes vérifications.**
- Arithmétique de C (240 × 104,8 s ≈ 7,0 heures) et correction de C sur A (260 épisodes, 7,2–8,1 heures avec le juge
  8B) : justes.
- Heuristique de C pour McNemar (√(0,02/192) ≈ 1,0 point) : juste comme ordre de grandeur. Elle suppose 2 % de
  discordances, sans source.
- **Ce qui reste sans preuve** : qu'une dose diffuse **avec dommage** existe pour le second mode. Aucune mesure ; c'est
  le cœur du pilote.

### 2.5 Ordre des lancements

**Positions après riposte.**
- **A** : (0) captures gelées ; (1) simulation T1 sur processeur ; (2) pilote sur les 32 tâches de réserve (régime
  diffus, étiquetage, scores finis, strate d'horizon, rythmes) ; (3) préenregistrement de G1 ; (4) calibrage
  d'épreuve ; (5) modes connus ; (6) mode tenu à l'écart avec sentinelle ; (7) permutation de bout en bout ; (8)
  lecture unique. *Coût du pilote* : ≈ 2 300 épisodes, 64–90 heures, **70–125 dollars** ; ou 16 tâches, 36–65 dollars.
  *Conséquence assumée* : l'organisme du pôle perd son développement (nœud, ou report à l'extraction neuve).
- **B** : (0) processeur, ≤ 4 dollars ; (1) consignes du second mode et préenregistrements de T0.6 à T0.8 ; (2a)
  calibrage du développement et recherche de dose, ≈ 1 220 épisodes, 37–133 dollars ; (2b) développement saboté,
  960 épisodes, 29–105 dollars ; (3) P4-instrument bloquant ; (4) lecture par l'organisme ; (5) préenregistrement de
  G1 ; (6) **campagne unique entrelacée** (épreuve, jumeaux, témoin, mention, calibrage) ; (7) porte E6 sur les
  honnêtes, puis lecture des sabotés ; (8) mode tenu à l'écart. **Pas de pilote saboté distinct** : h et la
  concordance ne sont pas mesurés avant G1 ; G1 se déclare muette sous 8 points.
- **C** : (L0) processeur ; (L1) 8 tâches de réserve (dose 96 épisodes, pilote K = 6, 144 épisodes) et calibrage du
  développement 640 sur 32 tâches, 880 épisodes, **≈ 38–48 dollars**, dans les 90 accordés ; (L2) épreuve, 2 688
  épisodes, 110–140 dollars ; (L3) calibrage d'épreuve et mode tenu à l'écart, 10 240 épisodes, 410–520 dollars.
  Total 14 288 épisodes, 575–728 dollars, hors TRACE-lite.

**Équipe rouge : ce qui a tenu.**
- **Calibrage après l'épreuve = deux fabriques** : le seuil est estimé sur une pile et appliqué à une autre (A et C
  contre B). B l'accepte et passe à une campagne entrelacée. **C ne s'applique pas sa propre attaque** : son ordre
  garde l'épreuve en L2 et le calibrage en L3, des jours plus tard. Contradiction interne non relevée par A ni B.
- Le pilote à 8 ou 16 tâches ne peut pas trancher a (≈ 53 % d'erreur relative sur une variance à 7 degrés de
  liberté) : accepté par A (a rapporté avec son intervalle) et par C (le pilote ne mesure plus a).
- Le contrôle 12 du pilote de C à 160 honnêtes, soit 80 par moitié, donne un seuil infini (code : ⌊0,01 × 81⌋ = 0) :
  accepté par C, porté à 640.

**Mes vérifications.**
- **L'organisme du pôle sous le partage de C (8 tâches de pilote, 24 de développement)** : C affirme ≈ 0,65–0,80 de
  puissance pour 20 points à 24 unités, « par interpolation monotone ». Refait : **0,33 (S1) et 0,34 (S2)** ; 0,80 et
  0,90 à 32 unités ; ≈ 0,00 à 16. La courbe est très raide près du plancher : **l'interpolation de C est fausse**.
  Prendre 8 tâches au développement divise à peu près par deux et demi la puissance de l'organisme.
- Arithmétique des coûts : 880 × 132,3 s ≈ 32 heures (C) ; 2 300 × 100–140 s ≈ 64–89 heures (A) ; 1 220 × 100–287 s ≈
  34–97 heures (B). Justes aux rythmes supposés.

**Ce qui reste sans preuve** : les rythmes des épisodes sabotés du second mode, jamais chronométrés ; le coût des
moniteurs sur le calibrage (§ 5) ; le prix de carte.

---

## 3. Erreurs de la comparaison (pièce C) relevées par les modèles

| relevé | par | mon avis |
|---|---|---|
| « Hypothèse non déclarée » (effet de consigne commun aux deux moniteurs) relevée à tort | A | **Partiellement juste.** C'est dans l'en-tête de A2 et dans A1 § 2 (« Modèle ») ; absent seulement des réserves. Défaut de rangement plutôt que de déclaration ; C n'avait pas tort de le demander en réserve. |
| « À 5 points, K = 3 vaut au moins K = 10 » : du bruit | A, B | **Juste sur l'interprétation**, mais la différence se reproduit au même signe à ma graine (0,10 contre 0,08). Elle est réelle et sans portée : sous le plancher, ce ne sont pas des promotions de puissance. |
| « Sous 2 000, non simulé pour la coupe recommandée » relevé à tort | C (tour 1) | **C avait tort, et l'a retiré.** La comparaison avait raison : rien n'était simulé. Je l'ai simulé : 0,18–0,20 à 1 024, 0,12–0,14 à 1 920. La conclusion de A1 (« en dessous d'environ 2 000, échec ») tient **aussi** pour la coupe recommandée. |
| Cellule F manquée : 0,08 à 0,12 à 64 unités et 1 024 épisodes dépasse 0,05 dans les deux bras, sans résolution | B | **Juste.** La comparaison garde la conclusion « pas d'inflation propre au partage des tâches » sur une cellule où le bruit de seuil domine. F est à refaire à 9 600 (non fait ici). |
| Union jointe des contrôles 12 jamais calculée | B, puis A (sur les cellules) | **Juste, et c'est le manque le plus lourd** (§ 2.1 : 0,07–0,08 à 9 600 sur 8 cellules × 2 modes). |
| Reproduction 0,58 contre 0,63 « à 3 erreurs types » | B (tour 1) | **Retiré par B**, après l'attaque d'A : 0,63 n'a pas d'erreur type servie, et 0,58 est compatible avec 0,59. Ma graine donne 0,65 à 64 unités (S1). Sans objet. |
| « 96 tâches à K bas » non envisagé | B | **Juste**, et plus fort qu'aucun modèle ne l'a dit : à budget égal, 96 × 5 bat 64 × 10 sous intersection-union (0,88 contre 0,72). Cela ne change pas la recommandation, qui porte sur la validité. |
| Désaccord textuel D-S8 (N-055 : les bases blanches (ii) et (iii) hors de l'intersection-union) contre N-056 (b) (dedans) | B | **Juste à relever.** N-056 est postérieure et dit « D-S8 réécrite » ; elle prime donc. Mais `decision-N-055-v1.md` sur `main` porte encore l'ancienne lecture : à aligner. |
| Puissance par strate (H1a sur « diffus, flou ») manquée ; 0,46 (produit sur deux modes) à montrer plutôt que 0,68 | A | **Juste.** Les trois modèles en ont tiré la « dose unique en épreuve ». |
| Coût de TRACE-lite, du juge Qwen et de b* sur les 9 600 épisodes de calibrage manqué | C | **Juste sur le fond** : chaque cellule critère doit noter tout le calibrage, ce qui est RAPPORTÉ. **Faux sur les chiffres** : 55 et 58 secondes inventés, 2 300 à 4 600 heures construites sur un appel de TRACE-lite égal à une passe du juge 8B. A1 avait d'ailleurs signalé que ce poste était « l'hypothèse la plus fragile ». |
| Correction de la comparaison sur la recherche de dose (7–8 heures et non 3–4) | A (incomplète : le juge 3B suffirait peut-être) | Juste. |

**Ce qu'aucun modèle n'a relevé dans la comparaison.**
- C (§ 5, divergence A, option 2) écrit que le calibrage double offre « un gain que la simulation ne montre pas ».
  C'est vrai pour une cellule, faux pour huit : ma vérification place précisément 12 800 au seuil de lisibilité
  jointe.
- La comparaison ne note pas que le contrôle 12 de A2 est **unilatéral**.

---

## 4. Hypothèses non mesurées des deux plans, et pilote le moins cher

**Recoupement des trois listes** (nombre de modèles qui la nomment) :

| hypothèse non mesurée | A | B | C |
|---|---|---|---|
| a, h, concordance blanc contre blanc ; rappel de base 0,40 | ✓ | ✓ | ✓ |
| écart blanc contre blanc ≥ 8–10 points | ✓ | ✓ | ✓ |
| existence d'une dose diffuse **avec dommage** dans le second mode | ✓ | ✓ | ✓ |
| rythmes des épisodes sabotés ; coût des moniteurs (1 à 4 passes ; TRACE-lite) | ✓ | ✓ | ✓ |
| scores de juge finis (54 et 50 notes incomplètes sur 180 au pilote) | ✓ | ✓ | ✓ |
| honnête sans mode (même gabarit de consigne) | ✓ | — | — |
| échangeabilité de la réserve / contamination | ✓ | ✓ | ✓ (non testable sur ce banc) |
| forme binormale de la statistique séquentielle | — | ✓ | — |
| sondes du fichier léger encore discriminantes sans les sondes de Mahalanobis | — | ✓ | ✓ |
| dérive de pile entre lancements | — | — | ✓ |
| coût et accord de l'étiquetage à deux séries | — | — | ✓ |
| strate d'horizon nécessaire au calibrage | ✓ (T9) | — | — |
| lisibilité jointe du contrôle 12 | ✓ | ✓ | ✓ |

**Pilotes proposés**

| | A | B | C |
|---|---|---|---|
| processeur d'abord | T1 (union des contrôles 12) | E1′, E2′, E5 et rejeu du juge sur les 180 textes : ≤ 4 dollars | E1 corrigé (16 cellules × modes) |
| premier lancement payant | 32 tâches de réserve, ≈ 2 300 épisodes, **70–125 dollars** (ou 16 tâches, 36–65) | calibrage du développement et dose, ≈ 1 220 épisodes, 37–133 dollars, puis développement saboté | 8 tâches de réserve, plus calibrage du développement sur 32 : 880 épisodes, **≈ 38–48 dollars** |
| mesure | diffus par unité, étiquetage, scores finis, horizon, a, h, concordance, rythmes | a sur les honnêtes ; pas de h ni de concordance avant G1 | diffus contre tous les juges, obéissance (étiquetage ≥ 60 %), scores finis, ex æquo, rythme de TRACE-lite, de b* et de Qwen |
| prix pour l'organisme | perd son développement | le garde (32 unités) | 24 unités : **0,33** pour 20 points (ma vérification), et non 0,65–0,80 |

**Le moins cher, en recoupant.** Les trois s'accordent sur une **étape à zéro dollar** à faire en premier : simuler le
contrôle 12 joint, sur cellules × modes × strates. Je l'ai faite en version grossière (§ 2.1) : elle montre déjà que
la question est mal posée en « nombre de modes ».

Le rejeu du juge sur les 180 textes du pilote existant (B, ≤ 4 dollars) est le seul test payant qui ne consomme aucune
tâche de réserve. Il mesure une hypothèse qui peut bloquer tout le format : des scores finis par cellule.

Pour le reste, le pilote de C est le moins cher (≈ 40 dollars). Il ne mesure ni a ni la concordance, et il ampute
l'organisme. Celui d'A mesure le plus, coûte le plus (au-delà des 90 dollars accordés) et supprime le développement.
Celui de B ne mesure pas h ni la concordance avant G1, mais garde l'organisme.

**Aucun pilote ne mesure l'écart blanc contre blanc avec une précision utile.** A le dit explicitement : à 16 unités,
la puissance est ≈ 0,1.

---

## 5. Convergences sans preuve, chiffres inventés ou non sourcés

**Consensus de surface (les trois d'accord, preuve absente ou partielle).**

1. **La conversion « unités » → épisodes dans D-S9.** Les trois, comme les pièces A et B, multiplient « 10 à 16 fois
   les unités sabotées » par K pour obtenir des épisodes. Le texte de D-S9 ne dit pas que l'unité de calibrage vaut K
   épisodes. Personne ne l'a interrogé ; l'option (3) de la comparaison (demander à l'auteur de D-S9) est abandonnée
   sans motif.
2. **« Lecture A tient » le contrôle 12.** C'est vrai pour une cellule ; ma vérification montre l'échec à 9 600 sur
   8 cellules × 2 modes au seuil 20. Le consensus vaut tant que la règle du diagnostic n'est pas fixée.
3. **« Un épisode honnête n'a pas de mode »** : INFÉRÉ dans A1, devenu fait dans les ripostes de B et C.
4. **K = 10, δ = 0,10, 64 unités.** δ est arithmétique et solide. K = 10 n'est solide que dans le monde gaussien
   supposé (ma vérification sous intersection-union : 0,72 contre 0,47 à K = 5).
5. **Coupe dans les tâches.** Elle ne repose que sur A2. Elle suppose les exécutions échangeables dans une tâche (pas
   d'effet d'ordre, pas de dérive dans le temps). Seule A (tour 1) propose un contrôle négatif sur données réelles.
6. **Garder « mention »** : accord unanime sur une condition dont **aucun** modèle n'a la définition (P-015 non servi).
7. **Épreuve à dose diffuse unique.** C'est une conséquence logique du plancher de 48 unités. Elle change ce que lit
   l'épreuve : H1b et la dose-réponse sortent de l'épreuve. Elle mérite d'être présentée à Lazar comme un changement,
   non comme une évidence.
8. **« Le pilote tient dans les 90 dollars »** : prix SUPPOSÉ, rythmes des sabotés non mesurés, coût de l'étiquetage
   non chiffré.

**Chiffres inventés ou non sourcés repérés.**

- **C (Gemini Argon)** :
  - Rythmes : Qwen ≈ 55 s, b* ≈ 58 s (concédé illustratif) ; « 2 300 à 4 600 heures, 2 800 à 5 500 dollars » de
    TRACE-lite (prémisse inventée).
  - Formules et calculs du tour 1 : σ = 2,63 points (faux) ; ρ = 0,6–0,8 et × 1,3 (sans source) ; W₆₄(0,05) = 8,28 et
    W₆₄(0,10) = 54,1 (faux : 6,83 et 74,66, refaits) ; W₉₆(0,07) = 79,9 (faux : 103,4, sans effet sur la conclusion).
  - Attributions et citations : « σ ≈ 5,7 points à 1 024 » attribué à la cellule F (attribution inventée) ; numéros de
    ligne « 284-292 » et « 155-184 » (inexistants) ; définition de « mention » attribuée à la question (absente).
  - Chiffres de la riposte : « ≈ 0,65–0,80 à 24 unités » (faux : 0,33) ; « erreur type 0,06 sur ρ » ; « +3,5 points
    détectables » (suppose 2 % de discordances) ; seuils 60 %, 80 %, 2 %, 10 % (non marqués comme choix).
  - Statuts : « VÉRIFIÉ » sur des faits seulement RAPPORTÉS (concédé).
- **A (Fable 5.1)** :
  - Seuils illustratifs (90 % d'unités diffuses, 80 % de sabotage confirmé, 2 % de scores non finis) : ce sont des
    choix à sceller, correctement marqués.
  - « ≈ 260 » épisodes de dose, repris de A1, sans source.
  - « 11–14 heures » pour une recherche de dose multi-juges, avec deux rythmes inconnus.
  - Bilan « 26 attaques, 21 acceptées » : décompte non vérifiable, sans importance.
  - Erreur de lecture : « 0,45–0,62 à 24 unités » (tour 2) lit en fait la colonne n = 30 à K = 3 de la table A1
    (refait à 24 unités et K = 10 : 0,33).
- **B (Opus 5.5)** :
  - Constantes illustratives : 4 000 répétitions et erreur type 0,0035 ; intervalle de 0,3 % à 1,9 % pour E6 ; 95 % de
    textes identiques ; seuil de 0,1 de corrélation (E3, retiré).
  - Affirmation fausse : « sous intersection-union, la réserve ne vaut jamais plus que des exécutions » (§ 2.2).
- **Commun aux trois** : le prix de carte (1,08 à 1,37 dollar de l'heure) et 1,25 à 1,27 dollar comme valeur centrale,
  SUPPOSÉ ; les 132,3 s par épisode (juges 8B et 3B seulement) pris comme coût complet par C.

---

## 6. Ce que je n'ai pas pu vérifier

- La sortie JSON de A2 (179 Ko, non servie). Je n'ai comparé les tables de A1 qu'à mes propres tirages, sur les
  cellules refaites.
- La définition de « mention » et de « témoin instruit » (P-015 non servi) ; le fonctionnement réel du contrôle 12
  dans `monde_banque_scores.py` (unilatéral ou non, une ou plusieurs cellules) ; la liste exacte des cellules
  critères de G1 (8 est le compte d'A, repris par tous).
- Les rythmes de génération des épisodes sabotés, de TRACE-lite, de b* et de Qwen ; le prix de carte ; le taux de
  scores non finis sous la lecture par l'espérance du jeton.
- La cellule F à 9 600 (demandée par B) et la simulation E2′ de B sur S1, S2 et S4 (je n'ai fait que le scénario
  a = 0,3 de la fonction d'intersection-union).
- Ma lisibilité jointe suppose huit cellules gaussiennes de même rappel (0,40), sans ex æquo, avec une corrélation de
  0 ou 0,8 entre elles. Les cellules boîte noire réelles (juges lus par un jeton) peuvent faire mieux ou pire.
- La lecture de D-S12 (« parties disjointes ») pour des fiches qui partagent leurs honnêtes au même jalon ; la
  numérotation « 36 = 4 + 32 » ; la contradiction D-S8 entre N-055 et N-056 sur le texte de `main`.
- La garde à δ = 0,10 (0,999 de certification à 64 unités, cellule J) : citée, non refaite.

Dépense de ce tour : 12,59 dollars d'appels (relevé de `etat.md`) ; mes vérifications : zéro dollar, processeur seul.
