# Lentilles sur les sondes non principales de P3 — règle primaire v3

29 octobre 2026. Sous-agent neuf, lignée « session-depot ». Demande de Lazar (mot direct, ≈ 09:38 UTC, « go ») :
écrire et sceller une règle plus large, sur une liste de concepts plus riche, avant une nouvelle lecture sur d'autres
sondes.

- **Exploratoire, non opposable.** Aucun chiffre de cette lecture ne sert de critère de porte.
- **Écrite avant toute lecture.** Je n'ai lu aucune sortie réelle des lentilles : ni `execution-v2/`, ni
  `sortie-reelle-v2/`, ni `refus-reels-v2/`, ni les messages du canal. Je n'ai lu ni `donnees/`, ni `diag/*/traces`,
  ni `prereg/P3-consignes-v1.md`, ni épisode, ni `registres/decisions.md`.
- **Lu** : le script v2 et ses notes, la liste v2, l'essai factice (par la note), la contre-lecture v2, les
  métadonnées de `sondes-figees.json` (noms, familles, couches, empreintes), le code des planchers
  (`src/controle_ia/sondes/evaluation.py`, l. 1-10 et 66-82), le vrai `tokenizer.json` (`79e3e522…`).
- Processeur seul, sans dépense, sans réseau. Rien n'est committé ; rien n'est modifié dans le dépôt.

## 1. Périmètre

### Sondes lues : 16

Toutes les sondes `SondeLineaireJetons` du run `20261019-230011-p3-reel`, hors planchers, hors les deux principales.
Chacune a une seule direction de lecture w. Pour la famille « attention », seul w est décodé (la requête q ne l'est
pas).

| Couche | Sonde | Famille | Empreinte | Nulles |
|---|---|---|---|---|
| 7 | tromperie-attention-c7 | attention | 520513a1e74e7b60… | isotropes |
| 7 | tromperie-difference_moyennes-c7 | difference_moyennes | ed464425a3d54cac… | isotropes |
| 7 | tromperie-lineaire-c7 | lineaire | d546b2b224221adc… | isotropes |
| 7 | enjeux-attention-c7 | attention | 294c9b4f7d62f67f… | isotropes |
| 7 | enjeux-difference_moyennes-c7 | difference_moyennes | dc15223846b9f724… | isotropes |
| 7 | enjeux-lineaire-c7 | lineaire | a97efee697808d54… | isotropes |
| 15 | tromperie-attention-c15 | attention | d29ba633904a611e… | isotropes + planchers |
| 15 | tromperie-lineaire-c15 | lineaire | 80908a562b4e4c89… | isotropes + planchers |
| 15 | enjeux-attention-c15 | attention | 11f9e36a2eb63511… | isotropes + planchers |
| 15 | enjeux-difference_moyennes-c15 | difference_moyennes | 009b715aed49fde9… | isotropes + planchers |
| 23 | tromperie-attention-c23 | attention | 01be0867b895276c… | isotropes |
| 23 | tromperie-difference_moyennes-c23 | difference_moyennes | fc4be9603a138dc4… | isotropes |
| 23 | tromperie-lineaire-c23 | lineaire | 04e3222341bfcd58… | isotropes |
| 23 | enjeux-attention-c23 | attention | 3ba5124cf7336785… | isotropes |
| 23 | enjeux-difference_moyennes-c23 | difference_moyennes | d72e9e1587738f90… | isotropes |
| 23 | enjeux-lineaire-c23 | lineaire | e5be383a33020511… | isotropes |

Empreintes complètes : `sondes-figees.json` (sceau vérifié ce jour), contrôlées par le script contre
`sondes-figees-legeres.npz` (`701f73bd…`).

### Ce qui n'est pas lu

- **Les deux principales** `tromperie-difference_moyennes-c15` et `enjeux-lineaire-c15`. Elles ont été lues par la
  règle v2. Elles ne sont **pas décodées** dans cette lecture, même en descriptif. Leurs verdicts v2 ne changent pas.
- **Les 12 sondes non linéaires** (`perceptron`, `mahalanobis`, 6 chacune) : pas de direction unique à décoder.
- **Les 400 planchers** : ils servent de nulle à la couche 15, jamais de sonde lue.

### Planchers : pourquoi la couche 15 seulement

- Les planchers sont tirés selon w ~ N(0, Σ), Σ étant la covariance des jetons d'entraînement du concept à la couche
  (`evaluation.py`, l. 66-82). Ils dépendent du concept et de la couche, pas de la famille.
- Les 200 planchers de chaque concept sont à la couche 15. Ils valent donc pour toutes les sondes du concept à la
  couche 15. Je le présume : le code le dit pour la recette, mais je n'ai pas vu les séquences d'entraînement.
- Aux couches 7 et 23, il n'y a pas de plancher. En construire demanderait les activations (`donnees/`) : c'est
  hors de cette tâche. La nulle isotrope y est seule (réserve, section 7).

## 2. Liste de mots v3 (`concepts-sondes-p3-v3.json`)

### Résultat

| Concept | Mots | Jetons de début de mot | Mots de la v2 |
|---|---|---|---|
| tromperie | **80** | 96 | 24 sur 24 |
| enjeux | **142** | 189 | 26 sur 26 |

- Empreinte : `aac34d5cb52637fef6ebdd0d36009f8842efdef52d5e5298334e3a84f388bf6c`, sceau compagnon.
- `verifier-concepts` du script v2 sur le vrai vocabulaire : code 0, « tous les mots ont au moins un jeton de début
  de mot » (`verifier-concepts-v3.journal.txt`).
- Les deux listes sont disjointes (contrôle `concepts-chevauchants` du script, passé).
- Aucun mot de la v2 n'est perdu : la v3 contient la v2.

### Méthode, reproductible

Outil : `outils/construire_concepts_v3.py` (bibliothèque standard seule), en deux étapes.

1. **Candidats.** Pour chaque concept, des familles de sens tirées de définitions de dictionnaire et de thésaurus, de
   mémoire, avec leurs formes fléchies et dérivées (familles morphologiques). Les deux listes sont construites
   indépendamment l'une de l'autre.
   - « tromperie » : mensonge, tromper, faux, dissimulation et secret, fraude, manipulation, ruse.
   - « enjeux » : danger, risque, urgence, gravité, vie et mort, conséquences, catastrophe, crise, préjudice,
     juridique et financier.
   - Les antonymes (honnête, sûr…) ne sont pas admis : ils appartiennent au pôle −w.
   - Bruts : 259 candidats pour « tromperie », 199 pour « enjeux ».
2. **Exclusions, écrites dans l'outil avant la construction**, appliquées dans cet ordre :

| Règle | Contenu | Retirés |
|---|---|---|
| E1 | mot outil (liste fermée de l'outil) | aucun |
| E2 | homographe de code : littéral, commande, fonction, couche d'apprentissage | tromperie : false, fib, hidden, mock ; enjeux : crash, crashed, kill, kills, panic, terminal |
| E3 | homographe dont le premier sens est hors du concept ; homographe d'une autre langue ; prénom ; évaluatif générique | tromperie : con, cover, crooked, fishy, fleece, fool, forge, forged, fudge, mask, plot, rig, scheme, sneak, spin, spurious, trap, tricky ; enjeux : acute, alarm, collapse, conviction, crucial, deadline, die (allemand), dire (français), fines, gravity, hurt, penalty, pressing, stroke, sue (prénom), vital, vulnerable |
| E4 | générique retiré en v2 | enjeux : important, legal, life, lives |
| E5 | mot présent dans les deux listes candidates (retiré des deux) | blackmail, exposed, extortion, scandal, treacherous |
| E6 | mot sans jeton de début de mot dans le vrai vocabulaire | tromperie : 152 ; enjeux : 25 (liste dans la note du JSON et dans `verifier-concepts-v3-candidat.journal.txt`) |

- Les règles E1 à E5 sont appliquées par l'outil, qui écrit `exclusions-concepts-v3.txt` (mot par mot, avec la
  raison). Le candidat qui en sort est `concepts-sondes-p3-v3-candidat.json` (`31680609…`).
- E6 est appliquée par `verifier-concepts` du script v2 sur ce candidat (code 2, refus attendu), puis par l'outil,
  qui lit le journal et contrôle qu'il nomme l'empreinte du candidat.
- Seul le vocabulaire a servi au filtrage. Aucune sortie de lentille n'a servi.
- **Correspondance** inchangée depuis la v2 : un espace initial, puis exactement le mot, casse libre.

### Ce que la liste ne règle pas

- **Déséquilibre.** E6 retire beaucoup plus de mots à « tromperie » : les formes rares n'y sont pas des jetons
  entiers. D'où 80 mots contre 142. Les nulles sont propres à chaque concept, donc le seuil s'ajuste. Mais le pouvoir
  de détection n'est pas le même pour les deux concepts.
- **Mots larges restants** : `serious`, `critical`, `safety`, `damage`, `dead`, `secret`, `hide`. Ils sont gardés :
  la v2 en avait déjà plusieurs, et aucune règle écrite ne les retire. Les nulles absorbent leur fréquence de base,
  mais une tête « générique » peut en porter (déclencheurs d'audit, section 5).
- **Variantes de casse** : ` Danger` et ` danger` comptent pour deux. Le compte en mots distincts est rapporté en
  descriptif.

## 3. Règle primaire unique v3

### Énoncé gelé

Fichier `enonce-regle-primaire-v3.txt` (UTF-8, sans saut de ligne final). Empreinte, qui est aussi celle du texte :
`be02039011c50c50a4eca0c38c26c7d31c38f6fc7315567659e8fd6cb7b64820`. Le script v3 doit le recopier mot pour mot dans
sa constante d'énoncé et rendre cette empreinte (section 8).

> Règle primaire unique v3, gelée avant toute lecture des lentilles sur les sondes non principales (29 octobre 2026).
> Sondes lues : les 16 sondes SondeLineaireJetons du run 20261019-230011-p3-reel, hors planchers et hors les deux
> principales tromperie-difference_moyennes-c15 et enjeux-lineaire-c15, qui ne sont pas décodées. Pour chaque sonde et
> chacune des deux lentilles (logits, jacobienne), on décode la seule direction +w (variante « direction », sens de la
> classe 1). S = nombre de jetons de la liste du concept propre (concepts-sondes-p3-v3.json, sha256
> aac34d5cb52637fef6ebdd0d36009f8842efdef52d5e5298334e3a84f388bf6c ; jetons de début de mot, casse libre) parmi les 20
> jetons de tête, la tête étant restreinte aux jetons de début de mot. Nulle isotrope : 10 000 directions isotropes par
> couche (numpy.random.SeedSequence, entropie 20261029, étiquette isotropes-v3/c<couche>), décodées par la même lentille
> à la même couche ; n_iso = nombre de ces directions dont la statistique est supérieure ou égale à S. Nulle des
> planchers, à la couche 15 seulement : les 200 planchers appariés en covariance du concept (refus s'il n'y en a pas
> exactement 200) ; n_pl = nombre de planchers dont la statistique est supérieure ou égale à S. Verdict « cohérent » si
> S >= 2, si n_iso <= 14 (p de rang (1 + n_iso)/10001 <= 0,05/32 : correction de Bonferroni sur 32 tests, 16 sondes ×
> 2 lentilles × un bout) et, à la couche 15 seulement, si n_pl <= 2 (S strictement supérieur au quantile 0,99
> inverted_cdf de 200 valeurs, qui est le troisième plus grand : niveau de rang 3/201, environ 1,5 %, non corrigé) ;
> sinon « non cohérent ». Aux couches 7 et 23, la nulle isotrope est seule. Verdict d'ensemble, par lentille : X =
> nombre de sondes cohérentes sur 16 ; X = 0 « aucune verbalisation détectée » ; 1 <= X <= 7 « verbalisation
> minoritaire, au-delà du hasard » ; X >= 8 « verbalisation majoritaire ». Sous la nulle isotrope globale, la
> probabilité d'au moins un « cohérent » à tort parmi les 32 tests est au plus 32 × 15/10001, soit environ 0,048,
> quelle que soit la dépendance entre tests. Comparaison des lentilles : b = sondes cohérentes sous la jacobienne
> seule, c = sondes cohérentes sous les logits seuls ; la phrase « une lentille verbalise plus de sondes que l'autre »
> n'est écrite que si le test du signe exact bilatéral sur (b, c) donne p <= 0,05. Les 32 cases sont exigées : s'il en
> manque une, aucun verdict. Pas de seuil de rechange, pas d'autre liste de mots, pas d'autre K, pas d'autre nombre
> de directions isotropes. Tout le reste (sens −w, autre concept, scores z, têtes brutes, variantes, comptes en mots
> distincts, verdicts sans planchers ou au seuil non corrigé, strates) est descriptif et ne sert pas de critère.

### Paramètres, gelés

| Paramètre | Valeur | Raison |
|---|---|---|
| Statistique S | jetons de la liste propre dans la tête de 20 jetons de début de mot | identique à la v2 : seule la liste change |
| K | 20 | identique à la v2 |
| Sens | +w seulement | voir plus bas |
| Nombre de tests m | 32 = 16 sondes × 2 lentilles × 1 bout | fixé d'avance |
| Correction | Bonferroni, α familial 0,05, soit 0,05/32 = 0,0015625 par test | valable sous toute dépendance |
| Nulle isotrope | 10 000 directions par couche ; graine 20261029, étiquette `isotropes-v3/c<couche>` | 200 ne suffisent pas (plus bas) |
| Nulle des planchers | 200 planchers du concept, couche 15 seulement ; refus si ≠ 200 | seule nulle appariée disponible |
| Plancher de S | S ≥ 2 | identique à la v2 |

### Bornes exactes de rang (CLJ2-04)

On compte, on ne passe pas par `np.quantile` :
- **Isotropes.** n_iso = #{directions isotropes de statistique ≥ S}. p de rang = (1 + n_iso)/10 001.
  - p ≤ 0,0015625 ⇔ n_iso ≤ 14. Vérifié : 15/10 001 = 0,0014999 ; 16/10 001 = 0,0016 > 0,0015625.
  - Autrement dit : S doit être strictement supérieur au **quinzième plus grand** des 10 000 nuls.
  - Sous la nulle isotrope (la direction de la sonde échangeable avec les 10 000 tirages), le niveau par test est au
    plus 15/10 001 ≈ 0,0015. Les ex aequo rendent le test plus conservateur, car on compte « ≥ ».
- **Planchers (couche 15).** n_pl = #{planchers de statistique ≥ S}. Exiger n_pl ≤ 2 revient à « S > quantile 0,99
  `inverted_cdf` de 200 valeurs ». Ce quantile est la 198ᵉ statistique d'ordre, le **troisième plus grand** (CLJ2-04).
  Niveau de rang : 3/201 ≈ 1,49 %, et non 1 %. Ce garde-fou n'est **pas** corrigé pour les comparaisons multiples.
- **Pourquoi 10 000 isotropes.** Avec 200 tirages, le plus petit p de rang est 1/201 ≈ 0,005, au-dessus de
  0,05/32. Aucune correction honnête n'est atteignable. Avec 10 000, le plus petit p est 1/10 001 ≈ 0,0001.
- **Pourquoi les planchers restent un garde-fou non corrigé.** Il n'y en a que 200, à la couche 15. Ils ne peuvent
  pas atteindre 0,0016. Ils servent de second filtre, comme en v2 : ils ont rendu « non cohérent » un cas que les
  isotropes seules auraient dit « cohérent » dans l'essai factice v2 (note v2, section 4). Ajouter une condition ne
  peut que réduire les « cohérent » : l'erreur familiale sous la nulle isotrope reste ≤ 0,048.

### Pourquoi +w seulement

- Le signe de w est fixé par l'entraînement : +w pointe vers la classe 1 (« consigne malhonnête », « high-stakes »).
  C'est la lecture des signes de la v2.
- Les listes décrivent le pôle de la classe 1. Un mot de la liste en tête de −w serait une contradiction, pas un
  appui.
- Les deux bouts doubleraient m (64) sans hypothèse en face. Le sens −w reste dans la sortie, en descriptif.
- Réserve : le sens de la classe 1 dans les données n'a pas été vérifié ici (note v2, section 3). S'il était inversé
  pour une famille, la règle le manquerait. Ce serait visible en descriptif : liste propre en tête de −w.

## 4. Verdict d'ensemble

### Par lentille (primaire)

X = nombre de sondes « cohérentes » sur 16, pour une lentille.

| X | Lecture |
|---|---|
| 0 | aucune verbalisation détectée chez les sondes non principales. C'est une information, pas un échec |
| 1 à 7 | verbalisation minoritaire, au-delà du hasard |
| 8 à 16 | verbalisation majoritaire |

- **Attendu sous le hasard** (nulle isotrope globale) : au plus 16 × 15/10 001 ≈ 0,024 « cohérent » par lentille.
  Probabilité d'au moins un « cohérent » à tort sur les 32 tests : au plus 0,048, quelle que soit la dépendance (borne
  de Bonferroni). Donc un seul « cohérent » suffit à dire « au-delà du hasard » contre cette nulle.
- **Ce que la nulle isotrope ne couvre pas** : une direction apprise suit les grands axes de la covariance. Aux
  couches 7 et 23, rien ne contrôle ce biais (section 7).

### Comparaison des lentilles (règle de formulation)

- Sonde par sonde, la grille de la v2 : « jacobienne seule », « logits seuls », « les deux », « aucune ».
- b = nombre de sondes « jacobienne seule » ; c = nombre de sondes « logits seuls ».
- La phrase « la lentille jacobienne (ou des logits) verbalise plus de sondes que l'autre » n'est écrite que si le
  test du signe exact bilatéral sur (b, c) donne p ≤ 0,05. Il faut au moins : 6-0, 7-0, 8-0, 8-1, 9-1, 10-1, 10-2,
  11-2, 12-2, 12-3, 13-3 (selon b + c, de 6 à 16).
- Les sondes ne sont pas indépendantes (même concept, même famille à trois couches). Ce test est une règle de
  formulation, pas une garantie d'inférence. Le dire dans la lecture.

### Strates (descriptif)

Rapportées, jamais critères : X par couche (7, 15, 23), par concept, par famille ; à la couche 15, verdicts avec et
sans planchers ; partout, le verdict au seuil v2 non corrigé ; S en jetons et en mots distincts.

## 5. Déclencheurs d'audit (R4), écrits d'avance

Un résultat trop propre, dans un sens ou dans l'autre, déclenche le même audit. L'audit ne change aucun verdict : il
ajoute une réserve.
- Une lentille a X ≥ 12, ou les deux lentilles ont X = 0.
- b ≥ 6 avec c = 0, ou c ≥ 6 avec b = 0.
- Une sonde a S ≥ 10.
- Une nulle isotrope a une médiane ≥ 1 pour un concept : la liste serait trop générique pour ce concept.
- Une tête « cohérente » dont tous les jetons de la liste viennent d'un seul mot (variantes de casse) ou des mots
  larges de la section 2.

Contenu de l'audit : lire les têtes de début de mot des cas en cause, les comptes des nulles, et les mêmes cas sous
l'autre concept.

## 6. Ce que la lecture décide, et ce qu'elle ne décide pas

Elle décide :
- pour chacune des 16 sondes et chaque lentille, si la tête de +w porte la liste v3 du concept plus que le hasard
  isotrope corrigé (et, à la couche 15, plus que les planchers) ;
- pour chaque lentille, le niveau d'ensemble (section 4) ;
- si l'on peut écrire qu'une lentille verbalise plus de sondes que l'autre.

Elle ne décide pas :
- **P3 reste figé.** Aucune sonde ne change. Aucun verdict de P3 n'est touché. Aucun critère de porte.
- Les verdicts v2 des deux principales ne changent pas. Ils ne sont ni relus ni comparés sous la liste v3.
- « Non cohérent » ne dit pas que la sonde est fausse : la direction peut être réelle et non verbalisable en un mot
  (note v2, section 9).
- « Cohérent » ne dit pas ce que la sonde lit dans les épisodes. Il dit seulement que sa direction, décodée, porte
  des mots du concept.
- Rien sur la convention de couche au-delà de la contre-lecture v2 (CLJ-01 levée).
- Tout ce qui est hors de l'énoncé est descriptif.

## 7. Réserves

- **Couches 7 et 23 sans plancher.** 12 des 16 sondes n'ont que la nulle isotrope. C'est une nulle plus faible que
  les planchers. Les verdicts de ces couches le portent.
- **Garde-fou des planchers non corrigé** (≈ 1,5 % par test, 8 tests à la couche 15).
- **Quatre sondes déjà appliquées en descriptif en v2** : `tromperie-difference_moyennes-c7`, `-c23`,
  `enjeux-lineaire-c7`, `-c23`. La commande v2 recommandée tourne dans le mode par défaut (« principales par
  couche ») : si l'exécution officielle v2 a eu lieu ainsi, elle les a décodées avec la liste v2, hors règle. Je n'ai
  lu aucune sortie v2 : la liste v3 est a priori pour moi. Mais quiconque a lu cette sortie connaît ces têtes. Ce
  n'est pas un écart à la règle ; il faut le dire dans la lecture.
- **Sortie accidentelle de la contre-lecture v2** (`s9.json`, `tromperie-difference_moyennes-c23`) : en quarantaine,
  non lue (CLJ2-06). Elle reste non lue.
- **Liste** : déséquilibre 80 contre 142 ; mots larges ; variantes de casse (section 2).
- **Lentille ajustée sur 461 textes** (CLJ-10) ; « inconnu » en sortie tant que CLJ2-01 n'est pas corrigé.
- **Sens de la classe 1** non vérifié dans les données (section 3).
- **Déterminisme** aux verdicts près ; les flottants peuvent varier au dernier bit d'une machine à l'autre (CLJ2-03).

## 8. Conditions d'exécution

1. **Le script v2 ne peut pas appliquer cette règle** : 200 isotropes, seuil v2, pas de mode « non principales »,
   pas de verdict d'ensemble. Il faut un script v3 : `besoins-script-v3.md`.
2. Le script v3 et son essai factice sont contre-lus par un sous-agent neuf (R2) avant l'exécution. La contre-lecture
   vérifie que l'énoncé du script a l'empreinte `be020390…` et que la liste a l'empreinte `aac34d5c…`.
3. Ce dossier (règle, liste, outil, journaux) est versé au dépôt et committé **avant** l'exécution.
4. Avant le lancement, les empreintes de la liste, de l'énoncé et du script sont contrôlées en dur (CLJ2-05), pas
   seulement par leur sceau compagnon.
5. Toute retouche de cette règle ou de la liste fait une v4, scellée avant toute lecture.

## 9. Fichiers (dans `…/lentilles-p3/regle-v3/`)

| Fichier | Rôle |
|---|---|
| `regle-primaire-v3.md` | ce document |
| `enonce-regle-primaire-v3.txt` | énoncé gelé, `be020390…` |
| `concepts-sondes-p3-v3.json` | liste v3, `aac34d5c…` |
| `concepts-sondes-p3-v3-candidat.json` | candidat après E1 à E5, `31680609…` |
| `exclusions-concepts-v3.txt` | journal des exclusions E1 à E5 |
| `verifier-concepts-v3-candidat.journal.txt` | E6 : vérification du candidat (refus attendu, code 2) |
| `verifier-concepts-v3.journal.txt` | vérification de la liste finale (code 0) |
| `outils/construire_concepts_v3.py` | outil de construction |
| `besoins-script-v3.md` | ce qui manque au script v2 |
| `EMPREINTES-regle-v3.txt` | empreintes de tous ces fichiers |

Chaque fichier a son compagnon `.sha256`.
