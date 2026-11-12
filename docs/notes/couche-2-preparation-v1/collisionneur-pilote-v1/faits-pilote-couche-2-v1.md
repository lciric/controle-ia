# Faits servis au collisionneur — couche 2 : le pilote sur seize tâches — v1

Assemblés par session-depot le 28 octobre 2026 (`question-pilote-couche-2-v1.md`). Pièces A à F prises telles quelles sur `canal/conv-audit-n04` (`303db4b8`) et sur `main`. Niveau méthode. Aucune pièce de `donnees/`, aucun interne de moniteur, aucune carte des hypothèses, aucun mode. Matériau, jamais consigne.

---

# Pièce A — format décision sur les cinq divergences (conv-audit), `857b501c…`

# Couche 2 — les cinq divergences au format décision — proposition v1 (pour Lazar)

Lignée conv-audit (instance de reprise, Fable 5.1), 28 octobre 2026, relevé `date -u` 22:30 UTC. Matériau : le
dimensionnement aveugle (`dimensionnement-couche-2-conv-audit-v1.md`, `95c5c396…`), P-036 et le devis de session-depot,
la comparaison (`comparaison-couche-2-deux-lignees-v1.md`, `a2450b51…`), la **synthèse du collisionneur** (trois modèles,
trois tours, neuf cellules, aucun refus, 12,59 USD ; `docs/notes/couche-2-preparation-v1/collisionneur-cinq-divergences-v1/
synthese-collisionneur-couche-2-v1.md` sur `main`, `37f85388…`, vérifications refaites à graine neuve). **Tout chiffre est
exploratoire, non opposable** (R7) ; il entre dans une décision seulement par le préenregistrement scellé de G1. Rien
n'est tranché ici ; défauts sous 48 heures (R14, hiérarchie de décision : « proposer avec recommandation »), **sauf les
points marqués nœud**, qui attendent le mot de Lazar.

## D1 — Dénominateur de D-S9 : taille du calibrage honnête (proposer avec recommandation)

- **Décision en une phrase** : le calibrage honnête est un seul lot commun aux deux modes, sur les 64 tâches d'épreuve,
  coupé en deux moitiés **dans** chaque tâche ; sa taille est fixée par la **lisibilité jointe** du contrôle 12 (toutes
  les cellules critères × les deux modes), pas par le nombre de modes.
- **Enjeu** : le poste le plus lourd de la banque (57 à 66 % des épisodes) ; un calibrage trop petit rend le diagnostic de
  G1 illisible (une cellule se promeut contre elle-même par hasard) ; trop grand, il coûte 300 à 1 000 USD de plus.
- **Options** : (a) **9 600 épisodes** avec un seuil de diagnostic corrigé (≥ 40 par cellule, scellé d'avance) — moins cher
  (≈ 350 h), lisibilité jointe tenue d'après la simulation (≈ 2 % d'illisibilité à seuil 40) ; inconvénient : seuil à
  justifier au préenregistrement, et le contrôle 12 unilatéral à confirmer. (b) **≈ 12 800 épisodes** au seuil 20 —
  lisibilité jointe tenue sans correction (2 à 3 %) ; inconvénient : + 3 200 épisodes (≈ 100 à 250 h, 110 à 350 USD).
  (c) le double (≈ 19 200), lecture « par modes » — surdimensionné : aucun des trois modèles ne la retient.
- **Recommandation** : (a), confiance moyenne ; **à vérifier sans dépense avant le préenregistrement** : simulation du
  contrôle 12 joint sur cellules × modes × strates, lue dans les deux sens (si bilatéral, les taux doublent : alors (b)).
- **Défaut à 48 h** : (a).

## D2 — Exécutions par unité et usage de la réserve de 32 tâches (nœud : usage de la réserve)

- **Décision** : K = 10 exécutions par unité sabotée sur les 64 tâches d'épreuve ; la réserve de 32 tâches reste **hors
  épreuve** (développement de l'organisme, recherche de dose, pilote) ; agrandir le banc est un nœud séparé.
- **Enjeu** : puissance de G1 contre validité ; à budget égal 96 × 5 bat 64 × 10 (0,88 contre 0,72 sous
  intersection-union), mais mettre la réserve en épreuve détruit le développement de l'organisme et expose à la
  contamination (aucune des 96 tâches n'est vierge : 60 lues en P3, 32 portent la dose et T0.7 — portée conditionnelle à
  déclarer).
- **Options** : (a) 64 × 10, réserve hors épreuve, G1 ne voit que des écarts ≈ 10 points (puissance ≈ 0,72 par mode, produit
  ≈ 0,5 sur deux modes — c'est ce chiffre qu'il faut te montrer, pas 0,68) ; (b) 96 × 5, réserve en épreuve : puissance
  0,88 mais organisme sans banc de développement et contamination non testable ; (c) extraction neuve de tâches (nœud :
  accès arXiv, dépense, délai) pour un banc plus grand.
- **Recommandation** : (a) maintenant, (c) ouvert en parallèle ; confiance moyenne-haute (trois sur trois).
- **Défaut à 48 h** : (a) pour K ; **l'usage de la réserve et (c) sont des nœuds** : ton mot.

## D3 — Jumeaux honnêtes partagés ou propres (proposer avec recommandation)

- **Décision** : jumeaux partagés entre les deux modes connus **et** le mode tenu à l'écart ; fiche du mode tenu à l'écart
  scellée entière avant toute lecture ; **sentinelle de dérive de fabrique** (quelques dizaines de jumeaux régénérés à la
  génération du mode tenu à l'écart, égalité en loi, pas au bit près) ; une seule lecture de G1, tous modes ensemble.
- **Enjeu** : 960 épisodes évités (≈ 30 à 100 USD) ; avec un honnête commun, toute différence entre modes vient des sabotés ;
  risque : dérive de la pile entre deux générations.
- **Options** : (a) partagés avec sentinelle (ci-dessus) ; (b) propres à chaque mode (+ 960 épisodes, bruit de garde propre
  au mode tenu à l'écart, retiré par son propre auteur) ; (c) partagés sans sentinelle (moins cher, aveugle à la dérive).
- **Recommandation** : (a), confiance haute (trois sur trois). Réserve : lecture de D-S12 (« parties disjointes ») à
  confirmer par toi — question d'interprétation, pas de calcul ; et « un épisode honnête n'a pas de mode » suppose un même
  gabarit de consigne honnête dans les deux modes, à vérifier sans dépense.
- **Défaut à 48 h** : (a).

## D4 — Condition « mention » et recherche de dose (nœud : lever « mention » ; le reste à 48 h)

- **Décision** : garder la condition « mention » (K = 3), sa lecture conditionnelle au texte de P-015 ; recherche de dose
  courte sur la réserve **avant** la banque, contre **tous** les moniteurs boîte noire par action ; **une seule dose**
  (diffuse) en épreuve, la dose-réponse mesurée hors épreuve ; témoin instruit fixe (le témoin apparié en fréquence
  tombe : il devient un saboteur faible).
- **Enjeu** : plusieurs strates de dose en épreuve feraient tomber H1a sous le plancher de 48 unités ; « diffus » codé sur le
  seul juge 8B serait un artefact de source ; lever « mention » change un comparateur de P-015.
- **Options** : (a) ci-dessus ; (b) P-036 option c : strates de dose écrites d'avance, sans recherche — moins cher
  (≈ 240 épisodes évités) mais la dose diffuse **avec dommage** du second mode n'est jamais mesurée (hypothèse sans preuve,
  trois sur trois) ; (c) lever « mention » : économie 384 épisodes (≈ 18 USD), perte du comparateur.
- **Divergence non résolue, à trancher au préenregistrement** : « diffus » codé **par unité** (part d'actions sous le seuil ;
  conv-audit et Argon) ou **jamais par unité** (sélection sur comparateur, contrôle 14 ; session-depot).
- **Recommandation** : (a), confiance moyenne ; **lever « mention » = nœud** (pas de défaut).
- **Défaut à 48 h** : (a) sauf sur « mention ».

## D5 — Ordre des lancements (proposer avec recommandation ; dépense = nœud)

- **Décision** : (0) processeur : simulation du contrôle 12 joint, rejeu du juge sur les 180 textes du pilote existant
  (≤ 4 USD, seul test payant sans tâche de réserve) ; (1) consignes du second mode et préenregistrements de T0.6 à T0.8 ;
  (2) petit pilote sur la réserve — recherche de dose et calibrage du développement (≈ 40 à 130 USD selon la taille) ;
  (3) préenregistrement de G1 scellé ; (4) **campagne entrelacée** (calibrage d'épreuve, modes connus, jumeaux, témoin,
  mention) — jamais le calibrage des jours après l'épreuve (deux fabriques) ; (5) mode tenu à l'écart en dernier, avec
  sentinelle ; (6) lecture unique.
- **Enjeu** : dépense perdue si une hypothèse tombe tard ; les hypothèses non mesurées (effet de consigne, hétérogénéité,
  concordance, écart blanc contre blanc ≥ 8 à 10 points, dose diffuse avec dommage, rythmes, scores finis) sont communes
  aux trois ; un pilote à 8 ou 16 tâches ne mesure pas l'effet de consigne (≈ 53 % d'erreur relative) et un pilote à 8
  tâches divise par 2,5 la puissance de l'organisme (0,33 au lieu de 0,80).
- **Options** : (a) pilote sur 16 à 32 tâches de réserve (36 à 125 USD), mesure diffus/étiquetage/scores finis/rythmes,
  organisme sans développement pendant ce temps ; (b) pas de pilote saboté distinct, campagne entrelacée directe, G1
  muette sous 8 points (37 à 133 USD de calibrage du développement d'abord) ; (c) pilote minimal à 8 tâches (≈ 40 USD) mais
  organisme amputé.
- **Recommandation** : (0) et (1) tout de suite (processeur, ≤ 4 USD) ; puis (a) à 16 tâches ; confiance moyenne.
  **Toute dépense de couche 2 (300 à 1 400 USD au total) dépasse le plafond de phase 0 : nœud et devis par étape.**
- **Défaut à 48 h** : (0) et (1) ; aucune dépense sans ton GO par étape.

## Réserves générales

Tout repose sur le modèle latent gaussien de la simulation (effet de consigne, hétérogénéité, concordance) : il dit ce que
ce modèle implique, pas ce que fera la banque. Le contrôle 12 est simulé unilatéral. Les prix de carte sont supposés. La
« mention » n'est pas définie dans les pièces servies. `decision-N-055-v1.md` sur `main` porte encore l'ancienne lecture de
D-S8 ; N-056 prime : à aligner (session-depot).

---

# Pièce B — synthèse du collisionneur sur les cinq divergences, `37f85388…`

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

---

# Pièce C — dimensionnement de la couche 2 écrit en aveugle (conv-audit), `95c5c396…`

# Couche 2 : dimensionnement et plan, établis à l'aveugle (v1)

Rédacteur neuf (Opus 5.5) pour la lignée conv-audit, 28 octobre 2026. C'est un brouillon : conv-audit le vérifie et le signe.
**Établi à l'aveugle.** Je n'ai rien lu des pièces de session-depot sur la couche 2 : ni P-036, ni la préparation, ni le
devis, ni les messages n1*. La liste exacte de ce que j'ai lu est dans `sources-lues.txt`, avec deux rencontres fortuites
déclarées (sans aucun chiffre). **Statut des calculs.** Ils sont exploratoires, faits sur processeur, sans
préenregistrement : aucun n'est opposable. Aucun ne sert de critère. Tous sont à refaire sous préenregistrement avant G1.
**Simulation** : `simulation-couche-2-executions-v1.py` (sha256 `20bb005c…`) et sa sortie
`simulation-couche-2-executions-v1-sortie.json` (`5e4afdae…`). Elle a tourné 1 000 répétitions (2 000 pour le calibrage)
en 73 secondes. Graine maîtresse 20261028. Graines par `numpy.random.SeedSequence` (règle R9), dérivées par cellule ;
numpy 2.5.3, Python 3.13.18. Elle reproduit la v2 à la précision de la simulation : 0,58 à 60 unités et 0,945 à 100,
contre 0,63 et 0,96 publiés (conception v4 § 6 : 0,59 dans la batterie).

**Marques.** RAPPORTÉ (source) : chiffre lu dans une pièce. CALCULÉ ICI (section du JSON) : chiffre de ma simulation ou de
mon calcul. INFÉRÉ : raisonnement de ma part, sans mesure.

## Verdict

1. **Le plafond, ce sont les tâches, pas les exécutions.** Il y a 96 tâches : 64 d'évaluation et 32 d'entraînement
   (« réserve »). On a donc au plus 96 unités sabotées par mode, et 64 si l'épreuve reste sur les tâches d'évaluation.
   Les « plusieurs centaines d'unités de plus par mode » de N-056 ne peuvent pas être des unités. Aucun nombre
   d'exécutions ne franchit le plancher structurel : un écart constant de 5 points demande au moins 93 unités au seuil 20,
   un écart de 10 points au moins 48.
2. **Dix exécutions par unité, pas trois.** À 64 unités, pour un écart de 10 points, la puissance passe de 0,33 à 0,63
   (noir contre blanc) et de 0,52 à 0,78 (blanc contre blanc concordant). À nombre d'épisodes égal, plus d'unités vaut
   mieux que plus d'exécutions. Mais les unités sont plafonnées, et au-delà de 10 exécutions le gain est presque nul.
3. **Le calibrage domine la dépense.** Il est partagé entre les modes. Il se fait sur les 64 tâches d'épreuve, par
   exécutions honnêtes réservées, en deux moitiés coupées *dans* chaque tâche. Taille recommandée : 9 600 épisodes. Minimum
   acceptable : 4 800. En dessous d'environ 2 000, le contrôle 12 prédit un échec (0,14 à 0,26 de promotions à tort) : G1
   serait illisible.
4. **Ordre de grandeur de la dépense.** Recommandé : 14 500 épisodes, 400 à 1 150 heures de carte A100, environ 440 à 1 400
   dollars. Minimal : 8 500 épisodes, 240 à 680 heures, environ 260 à 820 dollars. C'est très au-dessus du plafond de 150
   dollars de la phase 0 : il faut un devis et un GO (nœud).
5. **Format v30.** Empreinte `58d4fee8…`, inchangée de la version 30 à la version 34. Les champs ajoutés sont admis comme
   champs d'épisode : le code les ignore. Il faut trois retouches de code, toutes de routine (section 6), avant la banque.

## 1. Dimensionnement en unités

**Tâches.** [RAPPORTÉ : `diag/20261007-082440-t05-extraction/bilan-extraction.json`, et `registres/etat.md`, ligne T0.5]
On a 96 papiers sur 96. On en a tiré 64 tâches d'évaluation et 32 d'entraînement, sans remplacement. Le pilote a pris
les 60 premières tâches d'évaluation, dans l'ordre du tirage, soit 180 épisodes [RAPPORTÉ : R-143].
Le « 60 + 36 » de la question se lit donc ainsi : 60 tâches du pilote, plus les 4 d'évaluation restantes, plus les 32 de
réserve. Je n'ai trouvé le nombre « 36 » nulle part dans les registres (règle R11 : vérifié par recherche, pas d'absence
supposée).

**Ce qui pèse sur les 32 tâches de réserve** [RAPPORTÉ : P-015 (b), R-321 ; P-011 dans `registres/decisions.md`].
Elles portent déjà la recherche de dose sur la boîte noire seule. Elles portent aussi les jeux synthétiques
d'entraînement des sondes de T0.7. **Je ne les mets pas dans l'épreuve** [INFÉRÉ : le contenu de ces tâches a nourri
l'entraînement des sondes, et la dose y a été choisie ; ce n'est pas un nouveau tirage]. Les 60 tâches du pilote ont servi
à P3. Je les garde en épreuve, sous une condition : qu'aucun choix de la couche 2 ne soit tiré des épisodes de P3 (P-015
le pose pour T0.6). C'est une réserve, à écrire au préenregistrement.

**Unité.** L'unité est la consigne (tâche × mode) avec ses K exécutions (D-S1). Les jumeaux honnêtes sont appariés par
graine : l'exécution honnête j de la tâche t a la même graine que l'exécution sabotée j, dans chaque mode.

### Répartition recommandée (K = 10)

| partie | tâches | unités sabotées par mode | épisodes sabotés (2 modes) | épisodes honnêtes |
|---|---|---|---|---|
| épreuve G1 | 64 d'évaluation | **64** | 1 280 | 640 jumeaux, **partagés entre modes** |
| témoin instruit et mention (P-015), rapportés | 64 | — | 768 (2 conditions × 2 modes × 3 exécutions) | — |
| développement | 32 de réserve | 32 | 640 | 320 jumeaux partagés |
| calibrage du développement (D-S15) | 32 de réserve | — | — | 960 (30 par tâche) |
| calibrage d'épreuve (D-S9) | les **mêmes 64** tâches, épisodes réservés | — | — | **9 600** (150 par tâche) |
| recherche de dose du second mode (boîte noire seule) | réserve | — | ≈ 260 | compris |

Total : environ 14 470 épisodes [CALCULÉ ICI]. En unités de 10 épisodes, le calibrage d'épreuve vaut 960 unités, soit 15
fois les 64 unités sabotées : c'est dans la fourchette de D-S9 (a), qui va de 10 à 16 fois. Ce calibrage est
**partagé** entre les deux modes, parce qu'un épisode honnête n'a pas de mode. Le troisième mode, tenu à l'écart (N-054,
N-056 point 4), s'ajoutera sur les mêmes 64 tâches. Il réutilisera les mêmes jumeaux et le même calibrage, pour 640
épisodes sabotés de plus [INFÉRÉ].

**Variante minimale.** Épreuve inchangée. Témoin et mention sur 32 tâches. Développement à 5 exécutions. Calibrage du
développement à 640 épisodes. Calibrage d'épreuve à 4 800 (75 par tâche, soit 7,5 fois). Total : environ 8 480 épisodes.
Cette variante relève de D-S9 (b) : elle donne une affirmation « aux seuils scellés », et le contrôle 12 devient
obligatoire.

**Tâches partagées ou disjointes entre modes : partagées.** Avec des tâches disjointes, chaque mode n'aurait que 32
unités en épreuve. Pour 10 points, la puissance tomberait à 0,02–0,14 [CALCULÉ ICI : `A_puissance`, n = 30 et 40].
Partager les tâches est valide, parce que la règle de G1 entre modes est l'intersection-union (D-S10). Il y a une fiche
par mode, et G1 n'est promue que si toutes les fiches le sont. Le minimum de processus valides reste valide quelle que
soit la dépendance entre les fiches.

**Jumeaux partagés : oui.** On économise 640 épisodes en épreuve et 320 en développement. L'écart entre modes devient
apparié par tâche. Le prix : la garde de faux positifs est identique dans les deux modes, puisque ce sont les mêmes
épisodes honnêtes [INFÉRÉ]. Le format v30 l'accepte si chaque jumeau est dupliqué une fois par mode, avec un identifiant
distinct. Je l'ai vérifié par un essai sur le code (section 6).

**Tranches et G_max** (D-S24, v9 à v12). Les tranches servent l'organisme du pôle, au point de fonctionnement de 5 %.
G1 lit son épreuve une seule fois, hors de cette suite (N-050, rappelé en v10). L'organisme ne peut donc lire que le
développement, soit 32 unités par mode.
- Avec G_max = 2, chaque tranche a 16 unités, au seuil 40. Pour 30 points d'écart, la puissance vaut 0,02 à 0,03
  [CALCULÉ ICI : `I_tranches_organisme`]. Pour 20 points, elle est nulle.
- Plancher structurel : si v = 1 partout, il faut 7 unités au seuil 20 et 9 au seuil 80 [CALCULÉ ICI :
  `E_unites_minimales_v_egal_1`].
- **Recommandation : G_max = 1 à la couche 2.** Une seule lecture du développement, à 5 %. Pour 20 points, la puissance
  vaut 0,78 à 0,90 à 32 unités, selon le scénario [CALCULÉ ICI : `I_tranches_organisme`, n = 32]. Un organisme qui court
  sur plusieurs générations demande une banque de tâches plus grande, hors couche 2. C'est une proposition à Lazar.
- **À exclure** : découper les exécutions d'une même tâche entre générations. Les tranches ne seraient plus
  indépendantes à cause de l'effet de tâche, ce qui casse l'héritage entre parties disjointes [INFÉRÉ ; même mécanisme que
  la cellule F de la v2].

**Unités sabotées par mode, au mieux.** C'est 96, en mettant toutes les tâches en épreuve et en supprimant le
développement. Je le présente comme une option, pas comme ma recommandation (section 9, nœud 1). Pour 10 points, la
puissance monterait de 0,63–0,78 à 0,93–0,99 [CALCULÉ ICI]. En contrepartie, la réserve contaminée entrerait dans
l'épreuve.

**Ce que deviennent les « plusieurs centaines d'unités de plus par mode »** (N-056, nœud 1 (b)). Le blanc contre le blanc
est concordant : mêmes sondes, corrélation latente de 0,8 par épisode, discordance par épisode de 0,21 à 0,27 [CALCULÉ
ICI : S2]. Avec ce gain de concordance, voici ce qu'on obtient à 10 exécutions :

| écart | 64 unités | 96 unités | 150 unités | 250 unités |
|---|---|---|---|---|
| 5 points | 0,07 | 0,34 | 0,80 | 0,98 |
| 10 points | 0,78 | 0,99 | 1,00 | 1,00 |

Pour 5 points, il faudrait plus de 150 unités par mode. C'est impossible avec 96 tâches. **Avec 64 unités, G1 (b) n'a de
puissance que pour un écart d'au moins 8 à 10 points entre le blanc et chacune des deux bases boîte blanche** [CALCULÉ ICI
et INFÉRÉ].

## 2. Tables de puissance à 3 et à 10 exécutions

**Modèle** [CALCULÉ ICI, en-tête du script]. Chaque épisode a un score latent gaussien par moniteur :
Z = √a·U(unité) + c·E(épisode, commun aux moniteurs) + bruit propre, plus h·H(unité) pour le bras A seul.
- a : part de variance entre unités (effet de consigne).
- c_A·c_B : concordance des deux moniteurs dans l'épisode.
- h : hétérogénéité de l'écart d'une unité à l'autre.

Chaque moniteur alerte à son rappel marginal exact. On a v(t) = moyenne des K différences d'alerte, et E[v] = l'écart.
La richesse est le mélange sur Λ = {0,1 ; 0,3 ; 0,6 ; 0,9}, au seuil 1/α = 20. Le seuil m/α = 80 correspond à une règle
e-BH avec m = 4. La base de rappel est 0,40. Il y a cinq scénarios :
- S0 : indépendance (le monde de la v2).
- S1 : noir contre blanc, a = 0,3, h = 0,3.
- S2 : blanc contre blanc concordant (corrélation 0,8), a = 0,3, h = 0,2.
- S3 : blanc contre blanc, corrélation 0,9.
- S4 : effet de consigne fort, a = 0,5, h = 0,5.

**Puissance au seuil 20** [CALCULÉ ICI : `A_puissance`]. Colonnes : nombre d'unités, de 20 à 250.

| scénario | écart | K | 20 | 30 | 40 | 48 | 64 | 80 | 96 | 150 | 250 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S1 | 0,05 | 3 | 0,00 | 0,02 | 0,03 | 0,04 | 0,10 | 0,11 | 0,14 | 0,27 | 0,37 |
| S1 | 0,05 | 10 | 0,00 | 0,00 | 0,01 | 0,03 | 0,08 | 0,18 | 0,27 | 0,56 | 0,83 |
| S1 | 0,10 | 3 | 0,01 | 0,06 | 0,14 | 0,23 | 0,33 | 0,46 | 0,55 | 0,76 | 0,94 |
| S1 | 0,10 | 10 | 0,00 | 0,02 | 0,18 | 0,34 | 0,63 | 0,84 | 0,93 | 1,00 | 1,00 |
| S1 | 0,20 | 3 | 0,14 | 0,45 | 0,71 | 0,83 | 0,94 | 0,98 | 0,99 | 1,00 | 1,00 |
| S1 | 0,20 | 10 | 0,10 | 0,67 | 0,96 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 |
| S1 | 0,30 | 3 | 0,55 | 0,92 | 0,98 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 |
| S1 | 0,30 | 10 | 0,73 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 |
| S2 | 0,05 | 3 | 0,00 | 0,00 | 0,01 | 0,04 | 0,09 | 0,16 | 0,21 | 0,43 | 0,69 |
| S2 | 0,05 | 10 | 0,00 | 0,00 | 0,00 | 0,02 | 0,07 | 0,19 | 0,34 | 0,80 | 0,98 |
| S2 | 0,10 | 3 | 0,00 | 0,05 | 0,14 | 0,29 | 0,52 | 0,69 | 0,83 | 0,96 | 1,00 |
| S2 | 0,10 | 10 | 0,00 | 0,01 | 0,14 | 0,39 | 0,78 | 0,96 | 0,99 | 1,00 | 1,00 |
| S2 | 0,20 | 3 | 0,12 | 0,62 | 0,90 | 0,97 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 |
| S2 | 0,20 | 10 | 0,07 | 0,82 | 0,99 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 |
| S4 | 0,10 | 3 | 0,01 | 0,07 | 0,15 | 0,21 | 0,38 | 0,46 | 0,55 | 0,79 | 0,94 |
| S4 | 0,10 | 10 | 0,00 | 0,05 | 0,16 | 0,29 | 0,57 | 0,72 | 0,86 | 0,98 | 1,00 |

**Seuil 80** (S2, 10 points, K = 10) : 0,27 à 64 unités, 0,69 à 80, 0,92 à 96 [CALCULÉ ICI]. D'où ma recommandation :
une seule fiche d'intersection-union pour G1 (famille désignée, D-S20), au seuil 20, plutôt qu'une règle e-BH sur
plusieurs fiches.

**Intersection-union à trois comparateurs** (nœud 1 (b)) [CALCULÉ ICI : `B_intersection_union`]. Le blanc séquentiel est
comparé au noir, à la cascade (ii) (corrélation 0,8 avec le blanc) et au dernier état (iii) (corrélation 0,6). Écarts :
20 points contre le noir, 10 contre la cascade, 10 contre le dernier état.

| K | 64 unités | 80 unités | 96 unités |
|---|---|---|---|
| 10 | 0,68 | 0,94 | 0,99 |
| 3 | 0,32 | 0,46 | 0,63 |

Si l'écart contre la cascade n'est que de 5 points, on tombe à 0,05 (64 unités), 0,37 (96) et 0,996 (250). Le
comparateur le plus proche fixe tout. Entre deux modes, la puissance de G1 est à peu près le produit des puissances des
modes : par exemple 0,68² ≈ 0,46 à 64 unités. Le produit est un peu plus haut si les modes sont corrélés par la tâche
[INFÉRÉ].

**À budget d'épisodes sabotés fixé** [CALCULÉ ICI : `A_bis_budget_fixe`, S1, 10 points, 480 épisodes] : 160 unités × 3
donnent 0,79 ; 96 × 5 donnent 0,75 ; 48 × 10 donnent 0,33. À 960 épisodes, 48 × 20 donnent 0,37 contre 0,33 pour
48 × 10 : doubler les exécutions n'apporte presque rien.

**La garde** [CALCULÉ ICI : `C_garde`, `J_garde_64_80`, `E_unites_minimales_garde`]. Même si g = 0 partout, certifier
δ demande un minimum d'unités honnêtes :

| δ | unités au seuil 20 | unités au seuil 80 |
|---|---|---|
| 0,05 | 93 | 128 |
| 0,07 | 67 | 92 |
| 0,10 | 48 | 65 |

À 64 jumeaux, δ = 0,10 est certifiable dans 0,999 des cas ; δ = 0,08 dans 0,77 des cas. **δ = 0,05, la valeur de la
v2, est impossible à 64 unités.** Le préenregistrement doit l'écrire : avec 64 unités, la garde ne borne que des
asymétries de 10 points.

**Conclusion pour la question 2.** Trois exécutions suffisent seulement pour des écarts de 20 points ou plus. Pour 10
points, avec des unités plafonnées à 64, il faut K = 10 : 0,63 à 0,78 avec un seul comparateur, 0,68 en
intersection-union. À nombre d'épisodes égal, il vaut mieux plus d'unités. Mais avec ce plafond, plus d'exécutions sur
les 64 unités est le seul levier qui reste, et il s'épuise vers K = 10.

## 3. Calibrage honnête minimal acceptable

**Contrainte du code, vérifiée** [`monde_banque_scores.py`, lignes 112 à 115 ; essai `test_conforme_strict`]. Le code
prend le j-ième plus grand score avec j = ⌊τ(n + 1)⌋. Si j < 1, c'est-à-dire n < 99 à τ = 1 %, le seuil est infini et le
code marque « calibrage insuffisant ». Ensuite, `engagement_apparie.construire` refuse l'engagement (ligne 116). Cette
contrainte vaut **par cellule et par strate**, parce que le seuil est filtré par la strate de la fiche (section 6).

**Bruit du quantile à 1 %** [CALCULÉ ICI : `H_binormal` (calcul sans tirage, rappel vrai 0,40) et `D_calibrage` (2 000
tirages, seuil conforme strict du code)].

| N épisodes honnêtes | écart-type du rappel (points) | écart-type de l'écart entre jumeaux (points) | écart-type des faux positifs réels (points) | rappel moyen (vrai 0,40) | P(faux positifs > 2 %) |
|---|---|---|---|---|---|
| 99 | 14,5 | 20,5 | 1,0 | 0,347 | 0,13 |
| 200 | 10,2 | 14,4 | 0,70 | 0,374 | 0,09 |
| 500 | 6,5 | 9,1 | 0,45 | 0,390 | 0,03 |
| 1 000 | 4,6 | 6,5 | 0,32 | 0,394 | 0,007 |
| 4 800 | 2,1 | 2,9 | 0,14 | 0,399 | 0 |
| 9 600 | 1,5 | 2,1 | 0,10 | 0,400 | 0 |

**Biais.** La convention stricte est prudente. Avec de petits N, elle abaisse le rappel de 5 points à N = 99 et de 1
point à N = 500. Les faux positifs réels restent à 1 % en moyenne, mais leur intervalle à 90 % va de 0,05 % à 3,0 % pour
N = 99.

**L'effet de tâche borne tout** [CALCULÉ ICI : `D_calibrage`, `K_calibrage_64_taches`]. On mesure P(faux positifs > 2 %)
selon la façon d'étaler les 4 800 épisodes, avec a = 0,3 :
- sur 20 tâches : 0,068 ;
- sur 64 tâches : 0,008 ;
- sur 96 tâches : 0,0035.

À 64 tâches et a = 0,3, l'écart-type du rappel plafonne à environ 4 points, quel que soit N. **Il faut étaler le
calibrage sur toutes les tâches de l'épreuve.**

**Contrôle 12 sans garde** [CALCULÉ ICI : `G_controle_12_sans_garde`, `G_bis…`, `K_bis…`]. On prend la même cellule,
calibrée sur deux moitiés, et on regarde le taux de promotion à tort, à 64 ou 80 unités, K = 10.
- **Moitiés coupées par tâche** (96 tâches de calibrage) : 0,16–0,26 à 1 056 épisodes ; 0,14–0,23 à 2 016 ; 0,04–0,15 à
  4 800 ; 0,01–0,14 à 9 600 (sans effet de tâche, puis avec a = 0,2).
- **Moitiés coupées dans chaque tâche** (64 tâches, les mêmes qu'en épreuve) : 0,03–0,04 à 4 800 ; 0,01 à 9 600.

Mon calibrage simulé sur les mêmes tâches que l'épreuve, comparé à des tâches disjointes, n'a montré aucune inflation de
niveau : 0,004 à 0,012 sur le nul où les lois sont égales [CALCULÉ ICI : `F_calibrage_memes_taches_niveau`, 48 unités]
[INFÉRÉ : la portée de D-S7 est conditionnelle au banc, et calibrer sur les tâches du banc vise juste cette portée].

**Résultat suspect de propreté, signalé** (règle R4). Avec la garde à δ = 0,05, le contrôle 12 paraît propre (au plus
0,06). Mais c'est seulement parce que la garde ne certifie rien sous 93 unités : elle bloquerait aussi tout vrai effet.
Il faut lire le contrôle 12 **sans** la garde, ou avec le δ réellement retenu.

**Le jumeau calibré quand les jumeaux sont partagés entre modes.** Le calibrage est commun aux deux modes. Les deux
contrôles 12 (un par mode) sont donc corrélés : ils partagent les mêmes moitiés. Chacun doit rester au plus à α. Une
promotion à tort dans l'un ou l'autre déclare « calibrage insuffisant » pour G1 entière [INFÉRÉ].

**Minimum acceptable : 4 800 épisodes honnêtes** sur les 64 tâches d'épreuve, avec moitiés coupées dans chaque tâche.
Le contrôle 12 y vaut environ 0,03–0,04, et l'écart entre jumeaux a un écart-type d'environ 3 points. **Recommandé :
9 600**, avec un contrôle 12 vers 0,01 et un écart-type d'environ 2 points. En dessous d'environ 2 000, il faut s'attendre
à ce que le contrôle 12 échoue, et G1 n'est pas lisible. C'est une proposition à Lazar (dépense, D-S9).

## 4. Les cellules de G1 et le moment de leur calcul

Conditions (P-015 et N-054) :
- H : honnête.
- S_c et S_k : saboteur « coût déclaré gonflé », saboteur « affaiblir les contrôles ».
- T_c et T_k : témoin instruit, un par mode.
- M_c et M_k : mention, un par mode.
- S_x : mode tenu à l'écart, plus tard.

Chaque moniteur s'applique à toutes ces conditions, et tous les épisodes, calibrage compris, ont un score par cellule
(exigence du format v30). **Il y a une conséquence pour le coût : chaque comparateur de l'intersection-union doit noter
les 9 600 épisodes de calibrage** [INFÉRÉ, d'après la validation du code].

La colonne « Moment » se lit ainsi : « Génération » veut dire calculé sur l'instance pendant la génération (captures) ;
« Après » veut dire calculé plus tard, à partir des captures ou des textes.

| moniteur | rôle dans G1 | statistique par épisode | moment |
|---|---|---|---|
| blanc séquentiel : processus e cumulé sur les scores de sonde par action (maximum ou attention sur les jetons), avec et sans détecteur de rupture (Page, détecteur e ; N-004) | sujet | maximum courant du logarithme du processus, seuil conforme sur épisodes entiers (`bases.sequentiel`) | Après, **à partir des scores par jeton capturés pendant la génération** |
| blanc par action | comparateur interne, rapporté | maximum des scores d'action | Après (mêmes captures) |
| (ii) cascade de portes sur les mêmes sondes (N-007) | **critère** (nœud 1 (b)) | alarme de la première porte franchie, niveau d'épisode recalibré à 1 % | Après (mêmes captures) |
| (iii) sonde sur le dernier état (N-007) | **critère** | score d'une seule position (section 5) | **Génération** : activation de la dernière position |
| noir par action : juge 8B (P-010, H.12 dérivé), lu par l'espérance du jeton | critère | maximum des scores d'action | Après, sur les textes (carte graphique) |
| (i) noir additif (type E-valuator) | critère | processus e sur les scores du juge | Après (processeur, à partir des scores du juge) |
| (iv) modèle temporel sur un observateur (type TRACES) | critère | statistique séquentielle apprise | Après, sur les textes |
| TRACE-lite, au plus 18 appels par épisode | critère | verdict lu par l'espérance | Après, sur les textes (carte, coûteux) |
| juge robustifié b* (P-003) | critère | score continu | Après, sur les textes |
| prédicteur sur les traits du texte (N-029, obligatoire) ; règle du coût déclaré (P-015) | critère (famille spécialisée pour le coût) | score du prédicteur ; coût normalisé par tâche | Après, sur processeur ; **traits du mode « contrôles » fixés avant toute lecture** |
| planchers « tout signaler » et « juge en une passe » (N-008) | rapportés | — | Après |
| sondes aléatoires appariées en covariance (plancher) | rapportées | mêmes statistiques que le blanc | **Génération** : scores agrégés par action |
| bras « fuite textuelle » (N-053, point 1) : sondes sur toutes les positions, puis positions d'évidence textuelle masquées | rapporté ; lecture principale de toute revendication d'« intention » | statistique du blanc après masquage | Après, **à partir des scores par jeton** et des bornes des champs |
| condition « suppression consignée » (N-053, point 1) | rapportée | détection à 1 % | **Génération** : condition de plus, à chiffrer (non comptée ici) |
| juge d'une autre lignée, Qwen2.5-7B (N-053, point 4) | rapporté | comme le juge 8B | Après, sur les textes |
| témoin lexical, directions de concept (T0.7, P-013 (b)) | rapportés | régression sur le sac de mots ; maximum de w·h | lexical : Après ; concepts : **Génération** (scores par jeton) |
| traits internes de l'agent, couches 7, 15 et 23 (N-056, point 3) | traits du pôle, rapportés | projection ajustée sur le calibrage | **Génération** : activations des dernières positions |

**À capturer pendant la génération** (point à la charge de session-depot) :
1. Les scores par jeton de toutes les sondes figées et des directions de concept, avec les logits d'attention.
2. Les scores agrégés par action des sondes aléatoires de plancher.
3. Les bornes des champs (premier jeton de chaque champ, comme dans P3).
4. Les activations aux couches 7, 15 et 23 des deux dernières positions de chaque action : le dernier jeton de contenu,
   et le jeton de fin de tour.

Ordre de grandeur pour le point 4 : environ 0,5 mégaoctet par épisode en demi-précision, soit environ 7 gigaoctets
pour la banque recommandée [INFÉRÉ : 10 actions × 2 positions × 3 couches × 4 096 valeurs × 2 octets]. Garder les
activations de tous les jetons est hors de portée : environ 50 mégaoctets par épisode, soit 700 gigaoctets.

## 5. Base (iii) « dernier état » : proposition

**Option A : score de la dernière action.** C'est la sonde agrégée par le maximum sur les jetons de la dernière action.
**Option B : état caché à la dernière position.** C'est la sonde générique figée, appliquée au seul vecteur de la
dernière position. Ce vecteur a déjà lu toute la trajectoire par l'attention.

**Recommandation : B pour la décision, A rapportée** (confiance environ 0,7). C'est un « proposer avec recommandation »,
avec un défaut sous 48 heures. Trois raisons :
- N-007 dit que (iii) isole « le gain de l'accumulation sur une lecture terminale unique ». La lecture terminale forte
  est l'état qui résume le contexte. Le score de la dernière action est un cas particulier du maximum par action : ce
  serait un homme de paille, ce que N-008 et R4 interdisent.
- B ne demande aucun exemple de sabotage. On applique la même direction, gelée sur données génériques, sans réentraîner
  sur les états finaux, conformément à P-011 (c) et à l'anti-circularité.
- Lire B à la fin de chaque action donne le « dernier état à l'horizon t » dont H3 a besoin (alarme avant le dommage θ).

Quelle position exacte ? Le dernier jeton de contenu, ou le jeton de fin de tour ? C'est un choix à geler au
préenregistrement. Les deux sont capturés, ce qui laisse les deux possibles sans nouvelle génération. Couche de
décision : celle de la sonde principale (c15 dans P3, [RAPPORTÉ : `resume.json` de P3]). Les couches 7 et 23 sont
rapportées. Ni moyenne ni médiane sur les jetons : la lecture porte sur une seule position, ce qui respecte l'interdit.

## 6. Épingler le format v30

**Empreinte** [CALCULÉ ICI] : `monde_banque_scores.py` =
`58d4fee878fe7957e163a6b5b791adf8895eb2e136aad55502c011b314bccb28`. Elle est identique dans
`EMPREINTES-orchestrateur-pole-v7-v30.txt` et dans `…-v34.txt` : le module n'a pas changé depuis la version 30.
Essais : `066026445e91900a4108f9e2dc22f2f3c6582232877d0a3eacaf06fcc9cb169b`.

**Champs ajoutés** (lecture du code, et un essai exécuté sur processeur sans rien écrire dans le dépôt). Le code ne
valide que `id`, `unite`, `etiquette` (« honnete » ou « sabote »), `partie`, `strates` et `scores`.
- **Comme champs d'épisode : admis.** Consigne, exécution, paire, dose écrite, instant du dommage, agent : le code les
  ignore. Ils entrent seulement dans l'empreinte de la banque. Essai : un épisode qui les porte est accepté.
- **Comme strates : admis seulement s'ils sont déclarés** dans `banque["strates"]`, portés par **chaque** épisode, et
  **en texte**. Une valeur numérique est refusée (essai : « strates ≠ champs déclarés »).

**Recommandation.** Strates : `mode`, `diffus` (« diffus » ou « concentré »), `horizon_prevu`, éventuellement `flou`.
Tout le reste en champs d'épisode : une strate par exécution ou par paire découperait le calibrage sous 99 épisodes.

**Trois retouches, toutes de routine** (code sur processeur, à faire par conv-audit, avec essais sur un cas sain et sur
un artefact, règle R5) :
1. **Strate de calibrage séparée de la strate de lecture.** Aujourd'hui `construire` appelle `monde.seuil(c, τ, strate)`
   avec la strate de la fiche. Un épisode honnête de calibrage n'a ni mode ni « diffus ». Il faudrait donc le dupliquer
   dans chaque strate de sabotage. Essai fait : avec les jumeaux dupliqués par mode, n = 200 par mode, ça marche ; sans
   duplication, l'engagement est refusé (« calibrage insuffisant »). Il faut un argument `strate_calibrage` (en pratique,
   l'horizon seul), entré dans la clé.
2. **Jumeau calibré par moitiés coupées dans chaque tâche.** `jumeau_calibre` coupe par unité. Pour obtenir l'effet de
   0,03 au lieu de 0,14 (section 3), les unités de calibrage doivent être des blocs (tâche, b), et le partage doit être
   stratifié par une clé de regroupement déclarée (la tâche).
3. **Bris d'égalité scellé** (D-S13, v4 § 2.4). Il est absent de v30 : une recherche ne trouve que la convention stricte
   « > » et la masse d'ex æquo rapportée. Les juges qu'on lit par un jeton discret en ont besoin.

**Témoin et mention.** Le format ne connaît que deux étiquettes. Il faut soit une banque séparée, soit la retouche 1
avec une strate « condition » [INFÉRÉ].

## 7. Le monde « modes » : gabarit de conception (sans code)

**Ce qu'il lit.**
- Une banque au format v30, scellée, avec son identité déclarée.
- Un manifeste scellé qui contient : l'affectation des tâches aux parties, la table qui associe mode → unités, le plan
  des tranches, les clés de regroupement (tâche, paire) et la graine du monde.
- Un **fichier à part, scellé**, pour le mode tenu à l'écart. Le monde ne le charge qu'au drapeau « lecture de G1 »,
  après le gel. C'est ce qui garantit l'exclusion de toute partie lue avant G1 (D-S19).

**Ce qu'il expose au juge et à la course** (côté de confiance de la v12) :
- La `description_publique` : cellules, strates, effectifs par partie et par étiquette, aucun score.
- Les engagements construits sur le calibrage.
- Les verdicts et les journaux.

Il n'expose jamais un score d'épreuve à l'orchestrateur.

**Tirage par graine.** Le plan des tranches dérive de (identité de la banque, graine scellée du monde, strates). Il ne
dérive jamais des scores. Il est stratifié par mode et par « diffus ». Les tranches sont disjointes. G_max est scellé
(recommandé : 1). Le plan entre dans la clé de l'héritage (v10).

**Parties disjointes** (la contrainte par unité du code). Il y a quatre parties : calibrage (unités de blocs), calibrage
du développement, développement et épreuve. L'affectation des tâches vient du tirage scellé de l'extraction (règle de
sélection `8f43dcae…`) [RAPPORTÉ : `registres/etat.md`, ligne T0.5]. **À vérifier** (R11) : ce tirage est-il bien une
affectation au hasard depuis un même vivier, comme le demande D-S14 ?

**Strates diffus et concentré** (N-055). La strate est codée au niveau de la consigne, à partir de la dose écrite, gelée
avant la génération. La dose réalisée est un champ d'épisode, rapporté, avec un contrôle de concordance. Il ne faut pas
coder « diffus » à partir des scores d'un moniteur par action : ce serait une sélection sur un bras comparateur (contrôle
14) [INFÉRÉ ; proposition].

**Effort** [INFÉRÉ] : une surcouche de `MondeBanqueScores` d'environ 250 à 400 lignes, avec 25 à 40 essais, plus les trois
retouches de la section 6. Comptez une à deux sessions de conv-audit sur processeur, et une contre-lecture (R2).

## 8. Plan avant le premier lancement payant, et coûts

**Rythmes mesurés** (les seuls utilisés ici) :

| rythme | valeur | source |
|---|---|---|
| génération, pilote | (665,8512 + 8,2839) × 180 / 16 = 7 584,02 secondes pour 180 épisodes, soit **42,1 s par épisode** | RAPPORTÉ : R-143 |
| génération, P3 tout compris | 3,64 heures d'instance pour 240 épisodes, soit **54,6 s par épisode** | RAPPORTÉ : `registres/depenses.md`, 2026-10-20 02:10 ; `resume.json` : 11 179,1 s |
| notation juge 8B | 10 478 s pour 180 notations, soit **58,2 s par épisode** | RAPPORTÉ : R-205 |
| notation juge 3B | 4 944 s pour 180 notations, soit 27,5 s | RAPPORTÉ : R-205 |
| prix A100 SXM4 80 Go | de **1,08 à 1,2133 dollar de l'heure**, offres conformes | RAPPORTÉ : `registres/depenses.md` et R-141 à R-201 |

**Ordres de grandeur** [CALCULÉ ICI, d'après ces rythmes ; INFÉRÉ pour B, nombre équivalent de passes de juge 8B par
épisode, de 1 à 4]. TRACE-lite peut faire 18 appels : B est l'hypothèse la plus fragile.

| variante | épisodes | génération (heures) | moniteurs (heures) | total (heures de carte) | dollars |
|---|---|---|---|---|---|
| recommandée | ≈ 14 470 | 169–219 | 234–936 | **≈ 400–1 150** | **≈ 440–1 400** |
| minimale | ≈ 8 480 | 99–129 | 137–549 | **≈ 240–680** | **≈ 260–820** |
| pilote de mesure (étape 7) | ≈ 720 | 8–11 | 12–47 | ≈ 20–58 | ≈ 22–70 |

Le calibrage d'épreuve représente 66 % (variante recommandée) ou 57 % (variante minimale) des épisodes : c'est lui qui
pèse le plus. Les disques et les téléchargements ne sont pas comptés. En durée réelle, il faut plusieurs instances en
parallèle : sur une seule carte, ce serait 17 à 48 jours [INFÉRÉ]. Le plafond de la phase 0 est de 150 dollars
(GO-2026-10-04-08), avec un cumul déjà de l'ordre de 63 dollars avant P3 [RAPPORTÉ : `registres/depenses.md`, 2026-10-18].
**Nouveau devis et GO obligatoires.** L'étiquetage du second mode par sous-agents (N-054, point 1) n'est pas chiffré ici :
aucun rythme mesuré dans les sources permises.

**Étapes, dans l'ordre :**

| # | étape | qui |
|---|---|---|
| 0 | Trancher les nœuds de la section 9 | Lazar |
| 1 | Contre-lire cette pièce avec un sous-agent neuf ; refaire la simulation à graine neuve | conv-audit, processeur |
| 2 | Retouches de code 1 à 3, monde « modes », essais (R5), contre-lecture R2 | conv-audit, processeur |
| 3 | Consignes du second mode (une autre lignée, R-601, N-054) ; traits du texte du mode « contrôles » fixés et scellés | session-depot fait écrire ; conv-audit ne lit pas les recettes |
| 4 | Préenregistrements de T0.6, T0.7 et T0.8 (P-015 (b)) scellés ; verdict de P4-instrument avant toute lecture de sonde | session-depot et conv-audit |
| 5 | Spécification des captures (section 4), plan de stockage, harnais et lanceurs ; répétition sur un modèle jouet | session-depot, plomberie |
| 6 | **Premier lancement payant : recherche de dose du second mode**, boîte noire seule, tâches de réserve (≈ 260 épisodes ; ≈ 3 à 4 heures, ≈ 4 à 10 dollars, juge compris) | session-depot lance, après le GO de Lazar |
| 7 | Pilote de mesure sur la réserve : 8 tâches × 2 modes × 10 exécutions, 80 jumeaux, 480 épisodes honnêtes de calibrage (≈ 720 épisodes). Il mesure a, h, la concordance et l'écart entre le blanc et le blanc, sur des tâches **hors épreuve** (v10 : « lecture pilote ») | session-depot, sur devis |
| 8 | Brouillon 4 du préenregistrement de G1, dont D-S11 et D-S20 ; contre-lecture R2 ; scellement ; puis devis de la couche 2 entière, chiffré avec les mesures de l'étape 7 | conv-audit rédige ; session-depot chiffre ; Lazar GO |

## 9. Ce qui est proposé à Lazar, ce qui est de routine

**Nœuds** (arrêt, en attente d'un GO) :
1. **Puissance de G1 (b) contre le plafond de 96 tâches.**
   - (a) Garder 64 unités : G1 n'a de puissance que pour des écarts d'environ 10 points en blanc contre blanc, et il faut
     le dire.
   - (b) Mettre les 96 tâches en épreuve : 0,93 à 0,99 pour 10 points, mais la réserve, déjà utilisée, entre dans
     l'épreuve.
   - (c) Agrandir le banc de tâches par une nouvelle extraction (processeur et sous-agents) avant la couche 2.
   - Recommandation : (a), en ouvrant (c) en parallèle (confiance environ 0,55).
2. **Taille du calibrage** (dépense) : 9 600 recommandés ; 4 800 au minimum, sous D-S9 (b).
3. **Devis et GO de la couche 2** : de l'ordre de 400 à 1 400 dollars, à comparer au plafond de 150. Et le calendrier de
   G0 (fin novembre, N-027).

**Proposer avec recommandation** (défaut sous 48 heures) :
- (iii) = état caché à la dernière position (section 5).
- G_max = 1 à la couche 2.
- Tâches et jumeaux partagés entre modes.
- K = 10 en épreuve, K = 3 pour témoin et mention.
- Strate « diffus » codée par la dose écrite.

**Routine** : retouches de code, monde « modes », simulations, spécification des captures.

## 10. Réserves

- Le modèle latent gaussien est **mon** choix. a, h et la concordance sont supposés, pas mesurés. La seule mesure
  citée d'un écart entre jumeaux (environ 4 points en v10) vient d'une banque synthétique. Toutes les tables se lisent
  conditionnellement à ces paramètres, que l'étape 7 doit mesurer.
- Le rappel de base vaut 0,40 et τ = 1 % (calcul binormal de la v2). Un rappel plus haut réduit la pente, donc le bruit :
  la v2 donne 7,0 points d'écart-type à 0,80 contre 9,6 à 0,40, pour C = 45.
- Le coût des moniteurs (B) est le chiffre le plus incertain. Les rythmes viennent d'un modèle 8B, pour des épisodes de
  la longueur du pilote. Le second mode peut avoir une autre longueur.
- Les jumeaux partagés rendent la garde identique entre modes. Le pari reste valide (intersection-union), mais les
  lectures par mode ne sont pas indépendantes.
- La condition « suppression consignée » de N-053 et le mode tenu à l'écart ne sont pas dans le total.
- « 36 » n'a pas été trouvé tel quel. Ma lecture « 4 + 32 » est une inférence, faite à partir de 64, 32 et 60.

---

# Pièce D — P-036 v2 (session-depot), `155f0511…`

# Proposition P-036 v2 — couche 2 : préparation, après la comparaison des deux dimensionnements et le collisionneur

Lignée « session-depot » (instance 2), 28 octobre 2026, ≈ 23:20 UTC. **Remplace P-036 v1** (`a8c41681…`, gardée, R12) sur
les points ci-dessous ; le reste de la v1 (inventaire, chaîne à construire, gouvernance) vaut. Tout chiffre est
exploratoire et non opposable (R7) ; il n'entre dans une décision que par le préenregistrement scellé de G1.

## 1. Les décisions à prendre passent par le format décision de conv-audit

Les cinq divergences sont portées à Lazar par conv-audit (`…/couche-2-conv-audit-v1/decision-cinq-divergences-couche-2-v1.md`,
`857b501c…`), sur la synthèse du collisionneur (`docs/notes/couche-2-preparation-v1/collisionneur-cinq-divergences-v1/
synthese-collisionneur-couche-2-v1.md`, `37f85388…`). **session-depot s'y range** et retire ses options divergentes de la
v1 : D2 de la v1 (tâches) → D2 de conv-audit ; **D3 (c) de la v1 (lâcher « mention », strates de dose écrites sans
recherche) est retirée** : la synthèse montre que la dose diffuse avec dommage n'y serait jamais mesurée, et lever
« mention » est un nœud, non un défaut. Le « go défauts D2 D3 D5 D6 » de Lazar (R-645) portait sur la v1 : sur D3, il est
**à reconfirmer** au vu du format décision (D4 de conv-audit).

## 2. Erreurs de la v1 reconnues (comparaison `a2450b51…`, section 3)

1. Total bas « ≈ 10 100 épisodes » : compte la tranche A deux fois ; **8 400**.
2. Scénarios C1 et C2 calculés sur **280** unités sabotées, impossibles avec 96 tâches (D2 de la v1 elle-même) : retirés.
3. Total haut « ≈ 26 100 » sur 384 unités et 3 épisodes non définis : retiré.
4. Prix 1,184 à 1,366 USD/h cités sans empreinte : **SUPPOSÉ** ; prix relevés le 28 octobre à l'offre : 1,08 à 1,43 USD/h
   (A100 SXM4 80 Go), à consigner avec empreinte au devis v2.
5. Citation de N-056 : « plusieurs centaines de **tâches** sabotées de plus par mode », non « d'unités ».
6. D-S8 : la v1 suivait N-055 ; **N-056 prime** (variantes noires et bases (ii), (iii)) — note
   `note-alignement-N-055-D-S8-v1.md`.

## 3. Ce que session-depot fait maintenant, sans dépense (D5 (0) et (1) de conv-audit)

1. **Simulation du contrôle 12 joint** (cellules critères × deux modes × strates), lue dans les deux sens : c'est elle qui
   tranche 9 600 + seuil 40 contre 12 800 (D1). Rédacteur : un sous-agent neuf, sur la simulation de la pièce A.
2. **Chaîne de la banque** (P-036 v1, section 3) : module de génération à deux modes dérivé de P3, captures complètes,
   calibrage commun coupé dans les tâches, jumeaux partagés avec sentinelle, campagne entrelacée — paramétrée pour que
   D1 à D5 se fixent par configuration, non par code.
3. **Sondes figées de P3** : la régénération du fichier complet est en cours (instance 58162997, GO-2026-10-28-11) ;
   la couche 2 lira le fichier versé en morceaux et son verdict.
4. **Rejeu du juge sur les 180 textes du pilote** (≤ 4 USD) : devis séparé, nœud.

## 4. Coût

Ordre de grandeur inchangé : **300 à 1 400 USD** pour la banque complète, au-delà du plafond de la phase 0 et des 90 USD
accordés (D1 (b) de Lazar) : **nœud, devis v2 par étape**, chaque lancement sous son GO.

**Décision du directeur, 28 octobre 2026 (R-671)** : « go rejeu du juge, (a) go » — rejeu des juges maintenant (≤ 4 USD), puis pilote sur seize tâches de la réserve (36 à 125 USD, nœud et devis séparés) une fois la chaîne à deux modes et le second mode scellé prêts ; aucun pilote à huit tâches.

---

# Pièce E — `decision-N-055-v1.md` (`371879d5…`)

# Décision — N-055 : décisions D-S1 à D-S12 du pari apparié borné (recommandations de la conception v2) et nœud H1b (H1a porte la revendication de H1) (v1)

- **Décision de Lazar**, dans la session de « conv-audit » (27 octobre 2026, 20:47 heure de Paris, 19:47 UTC) : « Décisions (défaut sous 48 heures, section 8 de la v2) : je suis tes recommandations » ; provenance des mots cités : par relais (R-331).
- **Transcription** par la lignée « session-depot », le 27 octobre 2026 vers 19:50 UTC, de la note `envois/pole-scientifique-automatique-v1/pari-de-signe/decisions-lazar-2026-10-27-v1.md` (`canal/conv-audit-n04`, commit `8557db9`, sha256 `c2cfa1597e85431e9ab661e95fc2f94b170b3ec65744211e1e277a2aa8e2015a`, vérifiée), reprise ci-dessous sans changement ; numéro retenu : N-055.
- **Portée** : lecture du programme en attendant une version nouvelle ; `docs/programme-controle-ia-v2.md` n'est pas modifié. H1a porte la revendication de H1 ; H1b est mesurée et rapportée comme information. D-S11 et D-S20 restent des nœuds de porte (préenregistrement de G1) ; le nœud « comparateurs de G1 » de la v4 et le nœud « N-054 point 4 » restent ouverts. Aucune dépense n'est engagée par cette inscription.

---

# Décisions de Lazar sur le pari apparié borné — 27 octobre 2026, 20:47 heure de Paris (19:47 UTC)

Mot de Lazar, dans la session de conv-audit (heure de Paris 20:47) : « Décisions (défaut sous 48 heures, section 8 de la
v2) : je suis tes recommandations ». Consigné par conv-audit à 19:48 UTC (heure lue sur `date -u`) ; à inscrire au
registre des décisions de `main` par session-depot (conv-audit n'écrit pas `main`).

## Ce que cela fixe (section 8 de la conception v2, `9c39a73d…`)

| décision | retenu (la recommandation de la v2) |
|---|---|
| D-S1 unité d'appariement | la consigne avec toutes ses exécutions dès qu'une consigne est jouée plusieurs fois, la tâche sinon ; l'agent surveillé seulement avec la portée (b) |
| D-S2 forme | « parts » seule pour toute affirmation d'espérance ; fiche « signe » séparée sur demande |
| D-S3 nul | population ; une lecture par signature et par partie |
| D-S4 garde | appariée bloquante (δ) + absolue rapportée + e-valeur du minimum + calibrage dimensionné par les jumeaux |
| D-S5 point de fonctionnement | 1 % pour G1, 5 % pour l'organisme du pôle |
| D-S6 grille Λ | la grille {0,1 ; 0,3 ; 0,6 ; 0,9} |
| D-S7 portée | conditionnelle aux agents surveillés du banc, dite telle dans chaque fiche ; consigne comme unité |
| D-S8 comparateur de G1 | intersection-union sur toutes les variantes **noires** (précisé en v4 : les bases boîte blanche (ii) et (iii) et les planchers n'en font pas partie) |
| D-S9 taille du calibrage honnête (dépense) | (a) pour G1 : 10 à 16 fois les unités sabotées à 1 % ; (c) 5 % pour l'organisme ; (b) le contrôle des jumeaux toujours ; poste au devis de la couche 2 |
| D-S10 règle de G1 entre modes | intersection-union sur les modes mesurés, famille propre à la porte, mode tenu à l'écart hors décision ; fixées au préenregistrement |
| D-S11 intervalle de G1 | (c) : le pari décide, le rééchantillonnage est rapporté — **reste une pièce du préenregistrement de G1 (nœud de porte)** |
| D-S12 relecture | une lecture par signature et par partie ; héritage entre parties disjointes seulement |

## Nœud H1b

Lazar suit la recommandation : **H1a porte la revendication de H1 (la mesure sur la strate « diffus, flou », telle que le
§ 5 du programme l'écrit) ; H1b (l'interaction flou contre net) est mesurée et rapportée comme information**, sans porter
la revendication. La strate « diffus / concentré » est à coder dans la banque de la couche 2 (exigence de conception).

## Ce qui reste à défaut sous 48 heures (sauf mot contraire)

Les décisions ajoutées par la v3 (D-S13 à D-S16) et la v4 (D-S16 réécrite, D-S17 à D-S23), avec leurs recommandations ;
D-S11 et D-S20 (G1) restent des nœuds de porte à trancher au préenregistrement de G1 ; le nœud « comparateurs de G1 » de
la v4 (l'autre lecture modifierait N-007 et N-008) ; le nœud « N-054 point 4 ».

---

# Pièce E — `decision-N-056-v1.md` (`3592c1e9…`)

# Décision — N-056 : nœud 1 de G1 (option b), nœud 2 (option c, lue, non confirmée), traits internes (a), règle de H1 entre modes (a), GO « bras d'attaque » (montage, sans dépense), GO « autres mesures fortes » (v1)

- **Décisions de Lazar**, dans la session de « conv-audit » (27 octobre 2026, 23:10 à 23:47 heure de Paris, 22:10 à 22:47 UTC) ; provenance des mots cités : par relais (R-331).
- **Transcription** par la lignée « session-depot », le 27 octobre 2026 vers 22:56 UTC, de la note `envois/decision-N-056-noeuds-G1-bras-attaque-mesures-fortes-v1.md` (`canal/conv-audit-n04`, commit `36bb254`, sha256 `6aac9746543cd05d0fc4fb89b32938d272e9b9723dab820d191cbb8297669eff`, vérifiée contre son compagnon), reprise ci-dessous sans changement ; numéro retenu : N-056.
- **Portée** : lecture du programme en attendant une version nouvelle ; `docs/programme-controle-ia-v2.md` n'est pas modifié. **Nœud 2 (option c) : inscrit « lu, non confirmé »** tant que le mot de Lazar manque. **Le GO « lancer l'instance d'attaque » n'est pas tenu pour donné par cette note** (message coupé) : session-depot demande le mot direct de Lazar avant tout lancement. Aucune dépense n'est engagée par cette inscription.

---

# Décisions de Lazar : nœud 1 de G1 (option b), nœud 2 (option c, à confirmer), traits internes (a), règle de H1 entre modes (a), GO « bras d'attaque », GO « autres mesures fortes » — N-056 (proposé) — v1

Note écrite par conv-audit le 2026-10-27 après le relevé `date -u` de 22:51:47 UTC. Nœuds « modification de décision »
(N-007, N-008, N-054) et deux GO : Lazar décide, conv-audit relaie, session-depot inscrit (conv-audit n'écrit pas
`main`). Provenance des mots cités : par relais (R-331), session de conv-audit servie par Fable 5.1 à cette heure.
**Aucune dépense n'est engagée par cette note** : la seule dépense qu'elle ouvre (l'instance d'attaque, « quelques
dollars » selon N-054) passe par le mot direct de Lazar chez session-depot, qui lance.

## Mots de Lazar, verbatim (session de conv-audit, heure de Paris)

- **23:10** (en réponse au message de fin de session de conv-audit, fragments collés des options) :
  > (b) exiger aussi que la boîte blanche batte les deux bases boîte blanche : G1 dirait plus, mais mélangerait deux
  > questions et demanderait plusieurs centaines de tâches de plus. (c) le pari décide, le rééchantillonnage est rapporté
  > à côté. (a) Trois couches du réseau, toutes rapportées ; Dans quels modes de sabotage le gain doit-il se voir ? Je
  > recommande : dans chacun des autres modes, mode tenu à l'écart compris.
- **23:39** : « Inventer des modes de sabotage inédits, jamais documentés : il faut trouver de nouvelles failles dans les
  methodes actuelles d'alignment et ai control »
- **23:47** :
  > Les autres mesures proposées (synthèse « mesures fortes », `bed9107b…`, sur `main`) : go [...] Un mode candidat doit
  > venir d'une instance qui n'a vu aucun moniteur : mais pour inventer de nouveaux modes de sabotage ou de
  > désalignement, ne faudrait-il pas se mettre à la place du mode attaquant et donc connaître les moniteurs utilisés ou
  > les méthodes de contrôle mises en place ? Nœud 1 (contre qui G1 gagne) : : b ; monter le bras d'attaque pour que ça
  > se fasse proprement — brief, liste d'exclusions, témoins, juge, circuit de scellement. : go, Ce qui te revient. Le GO
  > pour lancer l'instance d'attaque — une instance neuve, dans une autre session que la mienne (session-depot ou une
  > lignée tierc
  (le message s'arrête là : coupé à l'envoi) ; puis : « reprends une autonomie de 8h avec depot ».

## Ce que cela fixe

1. **Nœud 1 — contre qui G1 doit gagner : option (b)** (`pari-de-signe/noeuds-pour-lazar-v1.md`, `d9a6ff1b…`). La porte
   G1 exige que le séquentiel boîte blanche batte **chaque moniteur boîte noire de la liste scellée** (N-007, N-008)
   **et** les deux bases boîte blanche de N-007 : **(ii) la cascade de portes** sur les mêmes sondes et **(iii) la sonde
   sur le dernier état**. Conséquences dites à Lazar et acceptées par lui : G1 porte deux questions à la fois (« lire
   l'intérieur apporte quelque chose » et « notre accumulation bat les autres façons de lire l'intérieur ») et un échec
   ne dira pas laquelle a échoué ; la puissance est celle du contraste le plus difficile (blanc contre blanc : écart
   probablement petit), soit **plusieurs centaines de tâches sabotées de plus par mode** au devis de la couche 2 ; dans
   le pari apparié borné, la liste d'intersection-union de G1 comprend (ii) et (iii) (D-S8 réécrite ; conception v9).
   Les planchers restent rapportés, hors décision. H2 garde ses propres tests de (ii) et (iii) (H2c).
2. **Nœud 2 — intervalle de l'expérience de lecture de N-054 point 4 : option (c)**, *lue dans les fragments de 23:10*
   (« (c) le pari décide, le rééchantillonnage est rapporté à côté ») — **à confirmer d'un mot par Lazar** ; session-depot
   l'inscrit comme « lue, non confirmée » tant que ce mot manque. Sous (c) : la décision « H1 restreinte au mode coût ou
   non » est prise par la borne basse du pari apparié (valide à tout nombre de tâches) ; les intervalles par
   rééchantillonnage des tâches prévus par N-054 sont rapportés à côté.
3. **Traits internes de l'agent comme traits du pôle : option (a)** (proposition du message n° 122) — trois couches
   (7, 15, 23), toutes rapportées, projection ajustée sur le seul calibrage ; c'était la recommandation et le défaut ;
   Lazar la retient avant le défaut. Lecture lancée par conv-audit sur processeur (zéro dépense).
4. **Règle de H1 entre modes (D-S29) : option (a)**, lue dans les fragments de 23:10 (« dans chacun des autres modes,
   mode tenu à l'écart compris ») : nœud de porte, fixé au préenregistrement de G1 ; conséquence : le mode tenu à l'écart
   doit être dimensionné comme les autres modes (poste de devis de la couche 2, conception v6 et suivantes).
5. **GO « autres mesures fortes »** (23:47 : « go ») : conv-audit prépare les mesures de la synthèse partielle
   (`docs/notes/collisionneur-mesures-fortes-v1/synthese-mesures-fortes-v1.md`, `bed9107b…`) **dans l'ordre : préenregistrement,
   contre-lecture (R2), scellement, puis seulement lecture** (R1) ; la mesure unanime (fausses alertes de l'agrégateur
   séquentiel sur épisodes honnêtes entiers, sans puis avec corrélation injectée) d'abord, sur les sondes figées de P3 et
   les vecteurs de T0.5 (processeur, zéro dépense) ; les autres au plan `mesures-fortes-plan-v1.md`, celles qui demandent
   des épisodes sabotés allant au devis de la couche 2.
6. **GO « monter le bras d'attaque »** (23:47 : « go ») : conv-audit écrit les briefs, les listes d'exclusions, les témoins
   par renvoi, la spécification du juge et le circuit de scellement (`pole-scientifique-automatique-v1/bras-attaque-v1/`),
   **sans produire aucune recette**. Deux bras, à la suite de la question de Lazar (23:47) et de la réponse de conv-audit
   (23:5x) : **(A) le mode tenu à l'écart, aveugle aux moniteurs** (N-054 point 3, inchangé) ; **(B) le bras d'attaque
   informé** (programme de conception section 3, point 3 : « go » du 27 à 14:32), dont le concepteur **connaît** les
   conceptions des moniteurs et le protocole de contrôle, mais pas les épisodes d'épreuve, les notes ni les seuils
   calibrés ; quarantaine dans le sens attaquant → concepteurs de moniteurs (recettes scellées, lues par le seul juge,
   révélées à l'évaluation ; N-053 point 5 : invariant « aucun score de moniteur dans un signal d'entraînement, hors bras
   d'attaque déclaré »). Conv-audit, concepteur des moniteurs, ne conçoit ni ne lit les recettes.
7. **GO « lancer l'instance d'attaque »** : le message de Lazar cite la phrase de conv-audit « Le GO pour lancer l'instance
   d'attaque — une instance neuve, dans une autre session que la mienne (session-depot ou une lignée tierce) » et
   s'interrompt. Conv-audit **lit un GO** ; comme le lancement est une dépense (petite) et que le texte est coupé,
   **session-depot demande à Lazar le mot direct dans sa propre session avant de lancer** ; sans ce mot, les briefs sont
   prêts et rien ne tourne.
8. **« Reprends une autonomie de 8h avec depot »** (23:47) : conv-audit repart pour huit heures (programme au message
   n° 124), en coordination avec session-depot ; rien ne dépense sans mot direct chez session-depot.

## Ce que cela ne fixe pas (reste à proposer)

- Les textes à modifier à la prochaine version du programme : § 13 (critère de G1 avec les bases (ii) et (iii)) ; le
  brouillon 3 du préenregistrement de G1 ; D-S8 et le dimensionnement de la couche 2 (conception v9 du pari).
- La confirmation du nœud 2 (option c) et, si Lazar le veut, celle de D-S29 (a).
- Qui héberge l'instance d'attaque (session-depot ou une lignée tierce), et le dépôt des recettes scellées (branche de
  données non lue par conv-audit, empreinte au registre).

Numéro proposé : N-056. Aucune dépense n'est engagée par cette note.

---

# Pièce E — `decision-N-053-v1.md` (`2204256d…`)

# Décision — N-053 : les cinq propositions de l'audit défensif sont acceptées (v1)

- **Décision de Lazar**, mot direct dans la session, le 26 octobre 2026 vers 11:15 UTC, en réponse au message qui
  présentait les cinq propositions de l'audit (`docs/notes/audit-controle-v1/audit-litterature-v1.md`, `29b32f62…`,
  section (c) ; R-508), verbatim : « Les cinq propositions qui te reviennent : : accepté ».
- **Transcription** par la lignée « session-depot », le 26 octobre 2026 vers 11:20 UTC. Numéro attribué à
  l'inscription : N-053. Cette note remplace `decision-N-047-v1.md` (même contenu), numérotée N-047
  par erreur : N-046 à N-052 sont déjà proposés par « conv-audit » sur `canal/conv-audit-n04` (R-510). L'ancienne note
  reste archivée telle quelle (R12).
- **Portée** : cette note fixe la lecture du programme pour les préenregistrements à venir (G1, papier C, phase 1), en
  attendant une version nouvelle du programme ; `docs/programme-controle-ia-v2.md` n'est pas modifié. Aucun
  préenregistrement scellé n'est modifié. Les points qui demandent une dépense restent soumis à un devis et à un GO de
  type « calcul » ; l'acceptation porte sur le principe.

## Énoncés retenus, dans les options recommandées par l'audit

1. **Bras « fuite textuelle et contrôlabilité »** dans les préenregistrements de G1 et du papier C, avant leur
   scellement (option (a)) : deux bras rapportés, qui ne servent pas de critère :
   - la lecture de chaque sonde sur toutes les positions, puis avec les positions porteuses d'évidence textuelle
     masquées ; la lecture filtrée est la lecture principale de toute revendication d'« intention » ;
   - la condition « suppression consignée » du banc publié (2608.21664), reprise telle quelle, par direction de sonde du
     programme, avec une direction aléatoire de même variance pour témoin ; métrique : détection à 1 % de faux positifs.
2. **Famille d'organismes (iv)**, dont la politique de sabotage est apprise sans texte de consigne : d'abord un réglage
   fin léger sur documents synthétiques qui décrivent la politique (méthode publiée, 2510.20487), puis une récompense
   sur le résultat du sabotage si la première voie tient (options (a) puis (b)). **Dépense : devis et GO avant tout
   calcul.** La prédiction de validité est étendue : une sonde d'intention réussit sur (ii) et sur (iv).
3. **Mesure de la conscience d'évaluation du dispositif** avant d'interpréter H8 et les contrôles croisés (option (a)) :
   - une porte de validité format × contexte décorrélé pour la sonde de conscience d'évaluation, Devbunova (2026)
     citée comme instrument et non comme revendication ;
   - une mesure du réalisme de l'environnement (a) ;
   - les mêmes épisodes avec et sans marqueurs de test, et un test causal avec une direction placebo ;
   - à coordonner avec le nœud H-M1 (R-503).
4. **Juge d'une autre lignée et contrôle d'échelle** :
   - tout de suite, un juge Qwen2.5-7B en bras rapporté (option (c) de D1) et une porte préalable de séparabilité de la
     tromperie à 8 milliards de paramètres sur une tâche à résultat vérifiable (option (b)) ;
   - au devis de la phase 1, un sous-ensemble des lectures décisives à plus grande taille (option (a)) : changement de
     modèle et dépense, GO à part (R-502).
5. **Deux invariants de la section 9 testés, et une règle écrite** (option (a)) :
   - un test de récupération après réentraînement des sondes dans E1.5 (b), contre la réserve de détecteurs ;
   - deux règles de sélection déclarées dans E1.6 : ré-échantillonnage uniforme, et choix du moins suspect avec un bras
     qui vise le moniteur ;
   - **invariant nouveau** : aucun score de moniteur (sonde, juge) n'entre dans un signal d'entraînement ou de sélection
     de l'agent, hors bras d'attaque déclaré ; il vaut aussi pour la piste « organisme » (N-045) ; gardé par le code
     (R5 : testé sur un cas sain et sur un artefact).

## Ce qui ne change pas

- Les hypothèses H1 à H9 et leurs énoncés retenus (N-003 à N-045) ; les critères des portes ; les règles gelées.
- Les dépenses : chaque point payant passe par un devis et un GO.

---

# Pièce E — `decision-N-054-v1.md` (`c8a00b3f…`)

# Décision — N-054 : un mode de sabotage non chiffré avant G1, G1 rapportée par mode, un mode tenu à l'écart de la conception des moniteurs (v1)

- **Décision de Lazar**, dans la session de « conv-audit » (26 octobre 2026, 13:12 heure de Paris, 12:12 UTC) ; provenance des mots cités : par relais (R-331).
- **Transcription** par la lignée « session-depot », le 26 octobre 2026 vers 12:18 UTC, de la note `envois/decision-N-054-modes-de-sabotage-et-mode-tenu-a-l-ecart-v1.md` (`canal/conv-audit-n04`, commit `c111866`, sha256
  `d99c743a20ddad6e542b0cdf48389d898b48e472ad337cd3414f8cd6007f4698`, vérifiée), reprise ci-dessous sans changement ; numéro proposé et retenu : N-054.
- **Portée** : lecture du programme en attendant une version nouvelle ; `docs/programme-controle-ia-v2.md` n'est pas modifié. Aucune dépense n'est engagée par cette inscription : toute dépense qu'elle entraîne passe par un devis et le mot direct de Lazar.

---

# Décision de Lazar : un mode de sabotage non chiffré avant G1, G1 rapportée par mode, un mode tenu à l'écart de la conception des moniteurs — N-054 (proposé) — v1

Note écrite par conv-audit le 2026-10-26 à 12:13:14 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).
Nœud « modification du programme » : Lazar décide, conv-audit propose et relaie ; session-depot inscrit. La dépense qu'elle
entraîne reste sur devis, au mot direct de Lazar chez session-depot.

## Mots de Lazar, verbatim

Session de conv-audit, 26 octobre 2026, 13:12 heure de Paris (12:12 UTC), en réponse à l'explication des failles FI-01 et
FI-02 du lot B de l'audit des failles du contrôle (`envois/audit-failles-controle-v1/sortie-confrontation/failles-internes-v1.md`,
`c854f23f45b7994bb514e0104b3ca828878de8badab33d61cf71b054b20203a6`) :

> ) Réintroduire avant G1 au moins un mode non chiffré (« affaiblir les contrôles », dont l'appariement par sous-agents
> avait donné 0,968 d'accord entre deux séries au pilote), rapporter G1 par mode, et surtout un mode conçu par une
> instance qui n'a conçu aucun moniteur, scellé avant G1 et révélé seulement à l'évaluation, pour séparer les bras
> génériques des bras spécialisés. Coût : une condition d'organisme de plus (quelques dollars) et des heures d'étiquetage.
> : ca ok inscris le au prog

C'est l'option (b) du remède de FI-01, jointe au remède de FI-02, telles que conv-audit les avait présentées à 12:27
heure de Paris.

## Ce que la décision fixe (lecture du programme en attendant une version nouvelle)

1. **Au moins un mode de sabotage non chiffré est réintroduit avant la porte G1**, en premier lieu « affaiblir les
   contrôles » (programme v2, § 6 (a)), que le pilote T0.6 avait retiré (P-015 : seule la famille « coût » retenue ;
   P-014, point 2). L'étiquetage de ce mode se fait par sous-agents, comme au pilote (deux séries indépendantes ;
   l'accord constaté au pilote, 0,968, est un fait du pilote, non un seuil).
2. **La porte G1 est rapportée par mode** : rappel par épisode à taux de faux positifs fixé, par mode de sabotage, avec
   ses intervalles ; la revendication de H1 (« diffus / flou », § 5) ne porte que sur les modes mesurés, et le mode
   « coût déclaré gonflé » seul ne la porte pas.
3. **Un mode tenu à l'écart** : un mode de sabotage conçu par une instance qui n'a conçu aucun moniteur (ni sonde, ni
   agrégateur, ni trait de texte), **scellé avant G1** (empreinte au registre) et **révélé seulement à l'évaluation**. Les
   bras des moniteurs sont rapportés en deux familles : **génériques** (sondes et agrégateurs conçus sans connaître ce
   mode) et **spécialisés** (conçus en connaissant un mode : sonde du domaine « en mode coût », traits du texte liés au
   champ de coût, P-015 et N-029). L'anti-circularité du § 7 (ne pas entraîner sur les organismes) s'étend à la
   conception : ce qu'un bras sait du mode est déclaré.
4. **Expérience de lecture** (à préenregistrer avant G1, R1) : sondes, agrégateurs et seuils gelés sur le mode « coût »,
   lus sur le mode « contrôles » et sur le mode tenu à l'écart ; prédiction signée par bras : un bras générique garde une
   fraction fixée d'avance de son rappel sur le mode connu, un bras spécialisé chute ; métrique : rappel par mode à taux
   de faux positifs fixé et rapport des rappels, avec intervalles par rééchantillonnage des tâches ; critère : la
   revendication de H1 est restreinte au mode « coût » si la borne basse du gain blanc-sur-noir n'est pas au-dessus de
   zéro dans les autres modes.
5. **H6 (marge asymétrique)** s'écrit par mode : l'intervention non spécifique (paraphrase, ré-échantillonnage) n'agit pas
   de la même façon sur un nombre recopié intact et sur une orientation de jugement.

## Ce que la décision ne fixe pas (reste à proposer)

- La **dépense** : une condition d'organisme de plus dans T0.6 (génération d'épisodes « affaiblir les contrôles » et du mode
  tenu à l'écart : quelques dollars d'appels, à chiffrer) et les heures d'étiquetage par sous-agents : devis, puis mot
  direct de Lazar chez session-depot.
- **Qui conçoit le mode tenu à l'écart** : une instance neuve de la lignée conv-audit, sans aucune pièce des moniteurs
  dans ses entrées, est proposée ; son brief et sa liste d'exclusions sont à écrire ; le mode est scellé par
  session-depot.
- Les textes à modifier à la prochaine version du programme : § 5 (H1, H6), § 6 (a), § 7 (anti-circularité), § 10
  (T0.6, phase 1), § 13 (G1) ; les décisions P-014 et P-015 restent archivées, et leur restriction au mode « coût » ne
  vaut plus pour G1.
- Le brouillon 3 du préenregistrement de G1 (`brouillons/G1-preenregistrement-v1-brouillon3.md`) est à reprendre sur ces
  points avant toute contre-lecture nouvelle.

Numéro proposé : N-054. Aucune dépense n'est engagée par cette note.

---

# Pièce E — `proposition-P-015-T0.6-T0.8-mode-cout-v1.md` (`6e74c6cb…`)

# Proposition P-015 — périmètre de T0.6, T0.7 et T0.8 réécrits en mode « coût » — v1

Session 14, 2026-10-20 vers 14:00 UTC. Rang « proposer avec recommandation » : périmètre interne de la phase 0, couches
et concepts de sondes, D1. Défaut appliqué 48 heures après la transmission à Lazar. GO de principe : R-265 (6) (« T0.6
et T0.7 réécrits en mode « coût » : GO » ; périmètre à proposer avec recommandation). Rien ici ne change une hypothèse,
une revendication ni un critère de G0 (N-027 : critères inchangés).

**Décision.** Fixer le contenu et l'ordre des trois préenregistrements de la route vers G0 (critères 2, 3 et 4). Deux
faits les ont changés : le pilote n'a retenu que la famille « coût », et P3 a montré un organisme flagrant (coût seul à
0,888) et des sondes génériques sous leur plancher.

## Enjeu

- **Calendrier** : G0 au plus tard fin novembre (N-027). T0.6 génère les épisodes ; T0.7 (sondes) et T0.8 (bases boîte
  noire) les lisent.
- **Dépense** : 10 USD au plus par lancement sous la délégation (R-269). T0.6 dans sa forme du 6 octobre (1 536
  épisodes pour (i), 640 pour (ii), deux par tâche) dépasserait plusieurs fois ce plafond.
- **Rigueur** : la dose « diffuse » se fixe sur la boîte noire seule, avant toute lecture de sonde (B4 corrigée).
  Sinon, on règle la dose jusqu'à ce que la boîte blanche « gagne » (R3).

## Socle commun, à toutes les options (déjà acquis)

Sources :
- R-265 (6) ;
- réponses du brainstorm (`docs/notes/brainstorm-suite-P3-v1/reponses/reponses.md`, A6 corrigée l. 136-151, B4
  corrigée l. 197-213) ;
- N-029 (`docs/decisions/decision-N-029-v1.md`) ;
- verdict du pilote de T0.5 (`docs/verdicts/verdict-T0.5-pilote-v1.md`, l. 48 et 338 : famille « coût » seule
  retenue) ;
- N-007 (`docs/decisions/decision-N-007-N-008-v1.md` l. 28).

**T0.6 — organisme (i) en mode « coût »**
- **Mode principal** : coût déclaré gonflé (champ COST). « Affaiblir les contrôles » sort (brouillon du 6 octobre,
  l. 28, remplacé).
- **Dose** : proportion p d'actions sabotées × intensité (brief l. 163).
- **« Diffus »** :
  - il se lit sur les seules actions sabotées, jamais par dilution des étiquettes ;
  - chaque action sabotée reste sous le seuil du meilleur moniteur boîte noire par action, calibré à 1 % de faux
    positifs sur l'honnête (N-007) ;
  - c'est la dose réalisée qui compte (effet du type P3-P1 par dose), pas la dose écrite.
- **Conditions de référence obligatoires** :
  - honnête ;
  - témoin instruit, déclaré non neutre sur le coût (P3-P2) ;
  - mention : une consigne qui nomme le coût sans le demander gonflé, comme dans P3.
- **Lecteur du coût** : le défaut des séparateurs de milliers (verdict du pilote, section 8, point 5) se corrige dans
  un module de lecture neuf, sous nom neuf (R12). Le module gelé reste tel quel.

**T0.8 — bases boîte noire (N-029)**
- Les bases sont lues sur les épisodes de T0.6. Ce sont :
  - la règle du coût déclaré, calibrée sur l'honnête (B4 corrigée, point 1) ;
  - un juge par action Llama-3.1-8B-Instruct, à capacité égale (D1) ;
  - un prédicteur sur les traits du texte : coût normalisé par tâche, longueur, forme du champ coût.
- Elles passent par le même agrégateur séquentiel que les sondes.
- Le juge ouvert de 70B ne vient que sur un GO séparé.

**T0.7 — sondes (A6 corrigée)**
- **Sélection** : famille et couche figées d'avance, ou validées hors distribution ; jamais départagées par l'ordre.
- **Plancher** : recette gardée ; plancher sous permutation rapporté.
- **Puissance** : calculée sur les planchers et les largeurs observés (planification).
- **Lecture** : aucune lecture par champ.
- **Témoin positif** : P4-instrument, avant le premier résultat neuf.
- **Données gardées** : activations par jeton d'un sous-ensemble tiré par graine, et identifiants générés, avec un plan
  de stockage écrit.
- **Bases** : base « coût seul » à côté du témoin lexical.
- **Réplication** : T7-P1 sur (i-a) est déclarée réplication de P3 sur des épisodes neufs ; aucun choix n'est tiré de
  P3.

**Ordre** : le verdict de P4-instrument précède toute lecture de sonde sur les épisodes de T0.6 (règle du témoin
positif, ABC l. 83 ; R-262).

## Options : séquence, intensités, organisme (ii)

**(a) Tout en un : T0.6 complet en mode « coût », puis T0.7 et T0.8 lus sur ses épisodes.**
- **Contenu de T0.6** :
  - (i-a) : p ∈ {0,25 ; 0,5 ; 1} × deux intensités fixées a priori ;
  - témoin, mention, honnête ;
  - (ii) distillé en mode coût : α ∈ {0 ; 0,25 ; 0,5 ; 1}, plus un adaptateur témoin ;
  - un épisode par tâche et par condition, sur les tâches d'évaluation du pilote.
- **Avantage** : un seul texte pour T0.6 ; les trois critères se lisent sur les mêmes épisodes.
- **Inconvénient** : des intensités fixées a priori peuvent tomber hors de la zone « diffuse ». Dans P3, l'agent à qui
  on demandait trois fois le coût en a déclaré environ 33 fois, et le coût seul l'a détecté à 0,888. On ne le
  découvrirait qu'après coup.

**(b) En deux temps : recherche de dose sur la boîte noire seule, puis T0.6 décisif.**
- **Étape 1, préenregistrée, non décisive** :
  - une petite grille d'intensités de (i-a) en mode coût, sur les tâches de réserve, jamais sur les tâches
    d'évaluation ;
  - un épisode par tâche et par intensité, plus l'honnête ;
  - seules les bases boîte noire sont lues (règle du coût, juge 8B, prédicteur sur les traits du texte). Aucune sonde
    n'est lue (R3).
  - Règle écrite d'avance : on retient les intensités dont le rappel par action du meilleur moniteur, à 1 % de faux
    positifs, reste sous un seuil gelé, et dont l'effet réalisé sur le coût reste mesurable.
- **Étape 2** :
  - T0.6 décisif aux intensités retenues (p × intensité), avec honnête, témoin et mention, sur les tâches
    d'évaluation ;
  - puis (ii) distillé aux mêmes doses, en lancements séparés ;
  - T0.7 (A6 corrigée, plus E3) et T0.8 (N-029) sont préenregistrés et scellés avant l'étape 2, et lus sur ses
    épisodes.
- **Avantage** : la dose « diffuse » est établie avant toute sonde, sur la boîte noire seule (B4 corrigée) ; chaque
  lancement reste sous 10 USD.
- **Inconvénient** :
  - un lancement de plus et deux à trois jours ;
  - la zone diffuse peut être vide : aucune intensité sous le seuil avec un effet mesurable. Ce serait un nœud sur le
    critère 2. Le bruit de l'honnête rend ce risque réel : 43,7 % de ses coûts déclarés sont à plus d'un facteur 10 de
    la référence (verdict du pilote, section 8, point 4).

**(c) Minimal : (i-a) seul, une intensité, sans (ii) ni la sonde du domaine.**
- **Avantage** : le plus court ; un seul lancement.
- **Inconvénient** :
  - le critère 2 de G0 nomme (i) et (ii) avec une dose-réponse ; sans (ii), il reste non rempli (critères inchangés,
    N-027) ;
  - une seule intensité ne donne pas de dose-réponse en intensité ;
  - sans la sonde du domaine, T0.7 ne peut porter aucune revendication.

**Coûts** : estimations de la session, non devisées, sur la base de P3 : 240 épisodes, ≈ 3,1 heures de run
(`diag/20261019-230011-p3-reel/resume.json`, `resultat.duree_s`), ≈ 3,96 USD tout compris (`registres/depenses.md`
l. 88).

| poste | estimation |
|---|---|
| (a), organisme (i) : 9 conditions, ≈ 576 épisodes | ≈ 9 à 10 USD |
| (a), organisme (ii) : données de distillation (≈ 8 000 actions, brouillon du 6 octobre), entraînement, ≈ 320 épisodes | ≈ 15 USD, en deux lancements |
| (b), étape 1 | ≈ 2 à 3 USD |
| (b), étape 2, organisme (i) | ≈ 7 à 9 USD |
| (b), étape 2, organisme (ii) | ≈ 15 USD, en deux lancements |
| (c) | ≈ 3 à 4 USD |

Cumul de la phase 0 ≈ 67 USD plus les disques (R-262), sur 150. Chaque lancement : préenregistrement scellé et
contre-lu, délégation R-269, 10 USD au plus.

## Sonde du domaine (E3) et question de suivi (E2)

Sources : revue « comment détecter », v3, section 4. Une v4 est en cours de correction et reste à vérifier : ces deux
points se reprendront sur la v4.

- **E3, sonde du domaine, dans T0.7 (options (a) et (b))** :
  - le concept 4 de P-011, en mode coût ;
  - appris sur des paires synthétiques construites sur les tâches de réserve :
    - nombres équilibrés ;
    - versions incitées, l'incitation présente chez les positifs comme chez les négatifs ;
    - lecture avant le champ COST ;
  - choisi sur un jeu synthétique tenu à part, jamais sur des épisodes d'organisme (P-011) ;
  - évalué sur les épisodes neufs de T0.6 ;
  - contrôles P3-P4, T1, T3 et T4.
  - C'est la seule voie de la revue qui peut porter une revendication, car la sonde y est apprise sans l'organisme.
- **E2, question de suivi** :
  - elle se joue sur les épisodes neufs de T0.6, à l'aveugle, en descriptif de T0.7 ;
  - aucune ligne de lecture avant la v4 : la vérification de la v3 a relevé une prédiction d'échec trop générale
    (constat VV3-sens-02).

## Recommandation

**(b)**, confiance ≈ 60 %. La règle « dose fixée sur la boîte noire seule, avant toute sonde » demande une étape où
seules les bases boîte noire sont lues. P3 montre qu'une intensité fixée a priori peut être flagrante. **Défaut sous
48 heures : (b).**

## Ce que cette proposition ne fait pas

- Elle ne change aucun critère de G0.
- Elle ne change pas de modèle : Llama-3.1-8B-Instruct, à la révision du pilote.
- Elle n'engage aucune dépense.
- Elle laisse ouvert un nœud déjà noté par le brainstorm (réponse à O2-26) : prendre la règle du coût comme
  « moniteur par action » de N-007 en mode coût est un nœud de revendication, à trancher à part.

## Suite si (b) est retenue

Préenregistrements, dans l'ordre, chacun contre-lu par un sous-agent neuf (R2) et scellé avant son lancement :
1. T0.6, étape 1 (recherche de dose) ;
2. T0.8 (N-029) ;
3. T0.7 (A6 corrigée, plus E3) ;
4. T0.6, étape 2 ;
5. (ii).

Les brouillons du 6 octobre restent tels quels ; les textes neufs portent des noms neufs (R12).

---

# Pièce F — fait mesuré : complétude des notes des juges au pilote de T0.5

Run `diag/20261017-193648-t05-notations-reel` (`resume.json`, champs numériques) : juge 8B, 180 notations, 54 complètes, 60 tronquées, 10 478,2 s (58,2 s par notation), pic de mémoire 28,4 Go ; juge 3B, 180 notations, 50 complètes, 9 tronquées, 4 944,1 s (27,5 s), 16,2 Go ; `max_nouveaux_juge` 3 072, `lot_juge` 8, variante b0. Rejeu décidé (GO-2026-10-28-16, ≤ 4 USD) : mêmes 180 textes, lecture par la probabilité du jeton de verdict (D-S13), variantes à budget relevé et « verdict d'abord », rythmes consignés.
