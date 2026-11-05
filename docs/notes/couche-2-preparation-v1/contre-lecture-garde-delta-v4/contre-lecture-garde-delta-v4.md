# Contre-lecture du script de puissance de la garde δ — v4

Contre-lecteur neuf (règle R2). Je n'ai écrit ni le script, ni le rapport, ni les contre-lectures précédentes.
29 octobre 2026, de 06:00 à 06:17 UTC (`date -u`). Processeur seul, aucun réseau, aucune clé, aucune dépense. Rien
n'a été écrit dans `source/`, `source-v3/` ni dans l'arbre v41. Aucun dépôt git créé.

## Verdict

**Utilisable après corrections.**

- Le calcul est juste. L'espérance de l'effet d'unité est tenue : écart 4·10⁻¹³ par intégration indépendante, aucun
  écart Monte-Carlo au-delà de 2,5 erreurs types sur 52 cas (σ jusqu'à 3). La fiche simulée est `evaluer` du pôle
  (1 200 fiches, écart 3,6·10⁻¹⁵, aucun arrêt différent). La sortie principale v4 est identique à la v3 dans ses
  5 950 champs, tous seuils compris. Les quatre sorties se reproduisent à l'identique à même graine.
- Les chiffres du rapport sont dans les sorties. Une lecture ne l'est pas (GD4-01, moyen). « L'effet d'unité ne touche
  presque pas la garde » vient de l'échelle logit et du minimum des k gardes. La garde seule perd 0,46 → 0,36
  (K = 10, τ = 0,10, δ = 0,05). À dispersion égale des deux côtés, la garde baisse aussi (0,90 → 0,78). L'explication
  « la garde certifie une espérance » est fausse : le contraste aussi.
- Restent quatre points mineurs. Le souligné est toujours lu dans les CSV, seul cas que la v3 avait relevé (GD4-03).
  Les doublons ne sont repérés que par le nom de chemin (GD4-04). Le commit d'une sortie diffère du manifeste (GD4-05).
  Quelques replis et erreurs brutes demeurent (GD4-06).

Sources relues. `sha256sum -c` donne « OK » pour les sept fichiers de `source/` : script `5bf015b6…`, sortie
`574d4c95…`, effet 0,5 `45c0be20…`, effet 1,0 `36d95e6e…`, rapport `21ec90dc…`, journal `e3b0c442…` (vide), manifeste
`27d02e49…`. Même résultat pour les sept fichiers de `source-v3/`. Pôle : `pari_apparie.py` `ec6c2cf6…`. Copies
conformes dans `cl/outils/copie_script/` et `cl/outils/copie_pole/`. Environnement : Python 3.13.17 (auteur : 3.13.18),
numpy 2.5.3, sans scipy.

## Réponses aux sept questions

### 1. GD3-01 à GD3-08

Voir la table plus bas. 3 corrigés (GD3-03, GD3-06, GD3-07). 4 en partie (GD3-01, GD3-04, GD3-05, GD3-08).
GD3-02 : en partie, avec un reste déclaré. Aucun ignoré.

### 2. Sortie principale v4 contre v3 ; reproduction (démontré, `comparer_sorties.py`, `lancer_repro.sh`)

**v4 contre v3 (sorties de l'auteur).** 5 950 champs communs. 0 différence. Cela couvre les 216 cellules aux seuils 160
et 20, les n₈₀, les artefacts, la taille minimale et `lecture_des_seuils`. On exclut l'en-tête de traçabilité (version,
empreinte, commit, état, environnement, statut). Seul champ en plus dans la v4 :
`reglages/contraste_synthetique_de_secours`. Cause, à la lecture : avec σ = 0, la v4 consomme le générateur comme la v3.
Le changement de l'effet d'unité est hors de ce chemin.

**Même graine 20261029** (commandes du manifeste) :
- principale (`--repetitions 4000`, 928 s) : 5 951 champs, 0 différence avec la sortie de l'auteur. Contre la sortie
  v3 : 5 950 champs, 0 différence. L'identité v3 = v4 est donc reproduite, pas seulement lue ;
- σ = 0,5 et σ = 1,0 : 807 champs chacune, 0 différence ;
- en-tête de mes passages : `commit: null`, `etat_du_script: "hors dépôt git"` (juste ici, voir GD3-04).

**Graine neuve 918273645** (mêmes commandes) :
- principale : 1 310 parts diffèrent, d'au plus 0,033. Ce sont les mêmes chiffres qu'à la contre-lecture v3 à cette
  graine, ce qui est attendu : sortie identique. n₈₀ : plus grand écart absolu 2 368 contre 2 304 (2,7 %) ;
- σ = 0,5 : parts à 0,027 près ; σ = 1,0 : à 0,020 près ;
- tableau du § 2 à graine neuve (garde k / contrastes / fiche, σ = 0 ; 0,5 ; 1) :
  K = 10, τ = 0,01, δ = 0,05, k = 1 : 0,89/0,98/0,87 ; 0,90/0,94/0,84 ; 0,89/0,82/0,71.
  K = 10, τ = 0,01, k = 3 : 0,79/0,95/0,75 ; 0,78/0,88/0,67 ; 0,77/0,69/0,49.
  K = 10, τ = 0,10, δ = 0,05, k = 3 : 0,21/0,96/0,20 ; 0,19/0,87/0,15 ; 0,19/0,70/0,085.
  K = 3, τ = 0,01, k = 3 : 0,47/0,18/0,069 ; 0,46/0,16/0,051 ; 0,48/0,14/0,041.
  K = 3, τ = 0,10, δ = 0,10, k = 3 : 0,88/0,17/0,14 ; 0,87/0,17/0,135 ; 0,82/0,13/0,088.
  Chaque case à 0,03 près de celle de l'auteur. Les sens se conservent ;
- garde seule k = 1, K = 10, τ = 0,10, δ = 0,05 : 0,446 / 0,421 / 0,357 (auteur : 0,456 / 0,421 / 0,362). La baisse
  de GD4-01 tient à graine neuve ;
- 400 unités, K = 3 : 0,73 à 0,82 (τ = 0,01, k = 3) ; 0,33 à 0,44 (τ = 0,10, δ = 0,05, k = 3) ;
- lectures du § 3 : 64 unités ≤ 0,009, contrastes k = 1 de 0,075 à 0,122 ; 0,89 → 0,03 ; 0,45 ; 0,59 ; 0,99 ;
- artefacts sous effet : frontière ≤ 0,0033 (seuil 160), ≤ 0,0283 (seuil 20).

### 3. Effet d'unité en logit (démontré, `verif_esperance.py`, `verif_decomposition.py`)

**L'espérance est tenue.** Méthode indépendante de la quadrature du script. Je reprends la constante c que le script
applique (lue en u = 0) et j'intègre sigmoïde(logit p₀ + c + σx)·φ(x) par trapèzes (400 001 points sur [−12 ; 12]).
- σ ∈ {0,5 ; 1 ; 2 ; 3}, p₀ de 10⁻⁴ à 0,9999 (52 cas) : écart maximal |E − p₀| = 3,6·10⁻¹³. La constante n'atteint
  jamais les bornes ±20 de la dichotomie.
- Monte-Carlo indépendant (10⁷ tirages par cas, graine propre) : |z| ≤ 2,5 sur les 52 cas.
- De bout en bout par `LoiSynthetique.tirer` (20 000 × 160 unités ; K ∈ {3 ; 10}, τ ∈ {0,01 ; 0,10},
  σ ∈ {0 ; 0,5 ; 1 ; 3}) : E[g] = 0 et E[v] = 0,10, à 2,5 erreurs types près. Frontière E[g] = δ tenue à 0,05 et 0,10. Les
  artefacts restent donc des tests de la frontière, ce que la v3 avait perdu.
- Artefacts dans les sorties de l'auteur : frontière ≤ 0,0033 au seuil 160 (borne 0,00625), ≤ 0,0285 au seuil 20
  (borne 0,05).

**Ce n'est pas une dépendance pure.** L'effet change d'abord la loi de chaque incrément : la variance de f_A et de r_A
monte, à espérance égale. Il ajoute ensuite deux liens :
- entre les k comparateurs (u commun, en plus du sujet partagé) ;
- entre la garde et le contraste de la même unité (même u). Une unité « alerteuse » nuit à la garde et sert le
  contraste : les deux processus sont liés négativement.

Décomposition (4 000 répétitions, 160 unités, seuil 160, biais 0, σ logit = 1). Valeurs : k gardes / k contrastes /
fiche (garde seule entre crochets).

| loi, δ, k | Z sans effet | S script | E sans lien g-v | H honnêtes seuls | T sabotés seuls | B bêta ρ = 0,17 |
|---|---|---|---|---|---|---|
| K = 10, τ = 0,01, δ = 0,05, k = 1 | 0,90 / 0,98 / 0,88 | 0,88 / 0,83 / 0,71 | 0,89 / 0,83 / 0,72 | 0,87 / 0,98 / 0,86 | 0,90 / 0,85 / 0,74 | **0,78** / 0,83 / 0,63 |
| K = 10, τ = 0,01, δ = 0,05, k = 3 | 0,80 / 0,95 / 0,75 [0,90] | 0,77 / 0,68 / 0,49 [0,88] | 0,78 / 0,69 / 0,51 | 0,79 / 0,95 / 0,75 | 0,79 / 0,70 / 0,52 | 0,65 / 0,70 / 0,44 [**0,77**] |
| K = 10, τ = 0,10, δ = 0,05, k = 3 | 0,20 / 0,95 / 0,195 [0,44] | 0,19 / 0,71 / **0,083** [**0,37**] | 0,19 / 0,70 / **0,126** | 0,19 / 0,95 / 0,18 [0,38] | 0,20 / 0,69 / 0,13 | 0,17 / 0,69 / 0,11 [0,30] |
| K = 3, τ = 0,01, δ = 0,05, k = 3 | 0,48 / 0,18 / 0,069 | 0,46 / 0,13 / 0,046 | 0,49 / 0,13 / 0,050 | 0,47 / 0,17 / 0,062 | 0,48 / 0,13 / 0,050 | 0,46 / 0,13 / 0,053 |
| K = 3, τ = 0,10, δ = 0,10, k = 3 | 0,89 / 0,17 / 0,146 [0,95] | 0,82 / 0,135 / 0,086 [0,90] | 0,81 / 0,14 / 0,098 | 0,81 / 0,18 / 0,13 | 0,89 / 0,13 / 0,10 | 0,75 / 0,14 / 0,089 [0,86] |

B : effet bêta à espérance tenue, corrélation intra-unité ρ = 0,17 des deux côtés. C'est la valeur que le logit σ = 1
donne à p = 0,5. Erreur type d'une part : au plus 0,008.

**Pourquoi le contraste baisse et la garde non.**
1. **Échelle.** En logit, l'effet ajoute à p un écart-type d'environ σ·p(1 − p) : 0,012 à p = 0,01, contre 0,21 à
   p = 0,5 (mesuré). La corrélation intra-unité implicite vaut 0,015 côté honnêtes (τ = 0,01) et 0,17 côté sabotés.
   Le même σ disperse donc onze fois plus le contraste que la garde. Le contraste perd sa puissance par la variance
   (T ≈ S). Le lien n'y est pour rien (E ≈ S).
2. **Minimum des k gardes.** À τ = 0,10, la garde seule baisse nettement (0,44 → 0,37 ici ; 0,46 → 0,36 dans la sortie
   de l'auteur, k = 1). Le minimum des trois gardes bouge peu (0,20 → 0,19), parce que le u commun rend les trois gardes
   plus corrélées. La perte de chaque garde est compensée en partie.
3. **Ce n'est pas « la garde certifie une espérance ».** Le contraste certifie aussi une espérance (E[v] > 0). Les deux
   processus perdent de la puissance quand la variance monte. À dispersion égale des deux côtés (B), la garde baisse :
   0,90 → 0,78 (k = 1, τ = 0,01), 0,44 → 0,30 (garde seule, τ = 0,10).
4. **Le lien garde-contraste existe.** S contre E : la fiche perd 0,043 à K = 10, τ = 0,10 (0,083 contre 0,126, environ
   neuf erreurs types), au plus 0,02 ailleurs, de signe variable. C'est le second effet de GD2-02, dans le sens annoncé. La phrase « la fiche
   suit le contraste » omet ce lien.

### 4. Fiche simulée contre `evaluer` du pôle (démontré, `verif_fiche_pole.py`)

Oui, à la précision machine. 1 200 essais, k de 1 à 3, n et n_garde de 5 à 119 :
- 1 000 tirés par la loi synthétique v4 (736 avec effet logit σ ∈ {0,5 ; 1 ; 3}, partagé ou indépendant, biais 0 à
  0,025, δ ∈ {0,05 ; 0,10 ; 0,20}, m ∈ {1 ; 8}, α ∈ {0,05 ; 0,01}) ;
- 200 tirés par la loi réelle (brute ou recentrée, écarts −1 et +1 compris).

Résultats : écart maximal sur la trajectoire du minimum 3,6·10⁻¹⁵ ; 0 longueur différente ; 0 instant d'arrêt
différent ; 211 fiches promues, dont 104 à longueurs de garde et de contraste différentes.

### 5. Entrées (démontré, `verif_entrees.py` : 54 essais, 26 refus nommés, 3 erreurs brutes, 25 acceptations ; plus 4 essais en Q7)

**Refus annoncés : tous nommés** (code 1, « refus : … »).
- GD3-03 : `--ecarts-contraste` sans `--ecarts` (avec ou sans effectif) ; garde réelle sans contraste ; `--comparateurs`
  1,2,3 ou 1 ou 2,2 avec deux fichiers ; `--effectif-attendu` sans fichier.
- GD3-08 : même chemin de garde deux fois ; même chemin en garde et en contraste.
- GD3-02 : identifiants dans un autre ordre ; identifiants sur la garde seulement ; sur un seul fichier ; ids doublés
  (1 et « 1 ») ; 4 ids pour 5 écarts.
- GD3-05 : clé doublée, même imbriquée ; entier de 31 et de 401 chiffres ; souligné en JSON.
- Autres : `1e400` et `infinity` en CSV ; effet 3,0001 ou NaN.

**Acceptés sans rien dire, ou erreurs brutes** (GD4-03, GD4-04, GD4-06) :
- souligné en CSV, colonne `ecart` et colonnes `fA,fB` : `0.0_5` lu 0,05. Aussi `--deltas 0.0_5`, accepté, avec
  « 0.0_5 » recopié en sortie. Aussi `--effectif-attendu 0_5` ;
- `g1.json` et `./g1.json` pour deux comparateurs ; deux fichiers de même contenu (même empreinte) ; un fichier `ecarts`
  servant de garde et de contraste par `./` ;
- `--ecarts ""` : sortie toute synthétique, sans refus ;
- `--contraste-synthetique-de-secours` avec un contraste réel, ou sans aucun fichier : ignoré, mais écrit `true` dans
  `reglages`. Quand il sert, ni `lois` ni les cellules ne nomment la loi de secours (K, τ) ;
- `--effet-unite-a 1 --taux 0` : loi nommée `_effetA1.0`, mais aucun effet côté honnêtes (`proba_decalee` rend p₀
  constant à p₀ = 0) ;
- identifiants : 1 et « 1 » égaux d'un fichier à l'autre ; `true`, `null`, liste et objet acceptés comme identifiants ;
- erreurs brutes, sans « refus : » : fichier absent (`FileNotFoundError`), virgule finale dans `--ecarts`, dossier à la
  place d'un fichier (`IsADirectoryError`) ;
- message pauvre : clé doublée et entier démesuré donnent tous deux « JSON illisible (ValueError) », sans le motif.

### 6. Le rapport dit-il ce que disent les sorties ? (démontré, `verif_rapport.py`)

Les chiffres, oui. Les 54 nombres du tableau du § 2 sont dans les sorties à l'arrondi près. La colonne « garde » est le
**minimum des k gardes**, ce que le rapport ne dit pas. Sont aussi dans les sorties : les 400 unités (0,72 à 0,82 ;
0,31 à 0,44), les lectures 1 à 3 (≤ 0,011 ; 0,07 à 0,12 ; 0,20, 0,18 contre 0,48, 0,05 contre 0,19 ; 0,89 → 0,03 ;
0,46 ; 0,59 ; 0,99 à K = 3, τ = 0,01) et les artefacts.

Phrases non soutenues ou inexactes :
- § 2 : « l'effet d'unité ne touche presque pas la garde » et « la garde certifie une espérance ». Voir Q3 et GD4-01.
- Lecture 3 : « fragile … au bruit τ (→ 0,46 à 0,10), non à l'effet d'unité ». La même garde seule (k = 1) passe de
  0,46 à 0,36 à σ = 1 (sortie de l'auteur).
- § 2 : « la fiche suit le contraste ». Le lien garde-contraste retire jusqu'à 0,04 (GD4-02).
- § 1, GD3-04 : « manifeste et sortie portent le même commit ». La sortie σ = 0,5 porte `0f62f64a…` ; le manifeste
  et les deux autres sorties portent `220cc259…` (GD4-05).
- § 1, GD3-05 : « souligné dans un nombre : refusés (testés) ». Faux pour le CSV (GD4-03).
- § 1, GD3-08 : « même fichier pour deux comparateurs refusé ». Vrai pour le même chemin écrit à l'identique seulement
  (GD4-04).
- § 1, GD3-01 : « vérifié … sur 2 millions de tirages ». Aucune trace dans les fichiers. Je le confirme par ailleurs
  (Q3).
- Lecture 4 : « jusqu'à un facteur 5 à K = 3 ». Hérité de la v3, non relancé ici. D'après la sortie v3
  « indépendants » : 5,2 à τ = 0,01, δ = 0,05. À τ = 0,10, δ = 0,05 : 0 sur 4 000 contre 0,008, donc un facteur plus
  grand, mais sur de très petites parts.

### 7. Le reste déclaré : un seul ensemble d'unités (démontré, `verif_ensembles_unites.txt`, à la lecture)

**Pour un passage sur fichier réel**, la règle exige :
- la même longueur et un seul `--effectif-attendu` pour tous les fichiers ;
- les mêmes identifiants dans le même ordre s'il y en a. Sans identifiant, rien n'est contrôlé.

Conséquences démontrées :
- une garde à 6 unités et un contraste à 5 sont refusés, quel que soit l'effectif donné ;
- deux ensembles qui se recoupent (u1–u5 contre u1–u4, u7) sont refusés.

C'est un refus, pas un repli. Mais l'utilisateur doit couper la banque à l'**intersection** (unités qui ont des
honnêtes **et** des sabotés). Ce que cela empêche :
- utiliser les unités qui n'ont que des honnêtes (pour la garde) ou que des sabotés (pour le contraste). n et n_garde
  baissent tous deux ;
- garder la loi de la garde du pôle, si les unités à sabotés ont un autre taux d'alerte honnête que les autres (biais de
  sélection, non mesurable dans le script) ;
- donner deux effectifs. `--tailles-garde` simule bien deux longueurs, mais tirées des mêmes lignes ;
- représenter le décalage du pôle. Dans le pôle, la t-ième unité honnête et la t-ième sabotée de l'ordre secret ne sont
  pas forcément la même unité. Le script lit toujours la même ligne pour les deux. Le lien garde-contraste des données
  passe donc tel quel dans la fiche. C'est l'hypothèse la plus forte ; elle a coûté jusqu'à 0,04 en synthétique (Q3) ;
- porter des identifiants en CSV : la colonne `unite` est refusée, les identifiants n'existent qu'en JSON.

**Pour la lecture synthétique**, la règle ne contraint rien à σ = 0 : il n'y a pas d'unités nommées. Sous effet d'unité,
elle se traduit par `u_s = u_h[:, :, :n]` : même unité, même indice, donc lien garde-contraste maximal. Les chiffres
« σ = 0,5 / 1,0 » du rapport sont donc la version la plus liée. Sans lien (E), la fiche serait de 0,01 à 0,04 plus
haute.

## Constats

### GD4-01 — moyen — « L'effet d'unité ne touche presque pas la garde » : effet de l'échelle logit et du minimum des k gardes, pas propriété de la garde

**Preuve (démontré, Q3, `verif_decomposition.json`, `verif_esperance.json`, sorties de l'auteur).**
- Le logit σ = 1 ajoute un écart-type de 0,012 à p = 0,01, contre 0,21 à p = 0,5. Corrélation intra-unité implicite :
  0,015 contre 0,17.
- Garde seule, k = 1, sorties de l'auteur, K = 10, τ = 0,10, δ = 0,05 : 0,456 / 0,421 / 0,362 à σ = 0 / 0,5 / 1.
  K = 3, τ = 0,10, δ = 0,10 : 0,948 / 0,938 / 0,904.
- Le « 0,20 → 0,18 » du rapport est le minimum de trois gardes. Le u commun les rend plus corrélées, ce qui compense
  en partie.
- À dispersion égale des deux côtés (bêta, ρ = 0,17), la garde k = 1 passe de 0,90 à 0,78 (K = 10, τ = 0,01), et la
  garde seule de 0,44 à 0,30 (τ = 0,10).
- « la garde certifie une espérance » : le contraste aussi. La différence vient de la variance ajoutée, pas de la nature
  du processus.

**Correction.**
- Réécrire le § 2 et la lecture 3. L'effet est en logit ; il disperse peu près de τ = 0,01 et beaucoup près de 0,5.
  La conclusion « non à l'effet d'unité » ne vaut qu'à cette échelle, et à τ = 0,01.
- Donner la garde seule à côté du minimum des k gardes. Dire que la colonne « garde » est le minimum.
- Ajouter une sensibilité à dispersion égale des deux côtés (bêta-binomiale, ou ρ fixé), ou écrire que le choix
  d'échelle décide de la lecture.
- Pour le fichier réel : la surdispersion de f_A entre unités (variance observée contre variance binomiale) se mesure.
  La rapporter ; elle tranchera.

### GD4-02 — mineur — Effet d'unité : lien garde-contraste non séparé ; espérances effectives et décomposition non écrites en sortie

**Preuve (démontré).**
- S contre E (même u, ou u des sabotés tiré à part) : la fiche perd 0,043 à K = 10, τ = 0,10, δ = 0,05, k = 3 (0,083
  contre 0,126 ; erreur type environ 0,005), au plus 0,02 ailleurs.
- Le rapport écrit « la fiche suit le contraste ».
- La contre-lecture v3 demandait E[f_A] et E[r_A] effectifs en sortie, et la décomposition A–E : ni l'un ni l'autre
  n'est fait.

**Correction.** Écrire en sortie E[f_A], E[r_A] et l'écart-type ajouté de chaque loi. Ajouter une option « u des sabotés
indépendant » et rapporter les deux. Écrire que l'alignement (même unité, même indice) est l'hypothèse la plus liée.

### GD4-03 — mineur — GD3-05 : le souligné est encore lu dans les CSV, seul cas relevé par la v3

**Preuve (démontré, `verif_entrees.json`).**
- `ecart` / `0.0_5` et `fA,fB` / `0.1,0.0_5` : acceptés, lus 0,05 (moyennes 0,01 en sortie).
- `_reel_strict` ne sert qu'au JSON. Or le JSON refuse déjà le souligné par sa grammaire (`JSONDecodeError`). Les
  lignes 183-184 ne font rien (`pass`).
- `--deltas 0.0_5` et `--effectif-attendu 0_5` : acceptés.
- Le rapport dit « refusés (testés) ».

**Correction.** Dans `_csv`, refuser tout champ qui ne suit pas `^[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?$` (ou au moins
contenant `_`). Faire de même dans `_reels` et `_entiers`. Retirer les lignes 183-184.

### GD4-04 — mineur — GD3-08 : doublons repérés par le nom de chemin seulement

**Preuve (démontré).**
- `g1.json,./g1.json` : accepté, deux comparateurs identiques.
- `g1.json,g2.json` de même contenu (même empreinte `e79041d8…`) : accepté, sans mention.
- `--ecarts e_ecarts.json --ecarts-contraste ./e_ecarts.json` : le même fichier sert de garde et de contraste (forme
  `ecarts`, admise des deux côtés).

**Correction.** Comparer `os.path.realpath` et l'empreinte sha256. Refuser, ou écrire un champ « doublons d'empreinte »
en sortie. Exiger la forme `fA,fB` ou `rA,rB` pour distinguer garde et contraste, ou ajouter une clé de rôle.

### GD4-05 — mineur — GD3-04 : commit d'une sortie absent du manifeste ; codes de retour de git toujours non lus

**Preuve (démontré, en-têtes des sorties ; `verif_etat_git.py` avec un git simulé, aucun dépôt créé).**
- Sortie σ = 0,5 : `commit` `0f62f64a…`. Sortie principale et σ = 1,0 : `220cc259…`. Le manifeste n'écrit que
  `220cc259`. Le rapport dit « manifeste et sortie portent le même commit ».
- Hors dépôt : « hors dépôt git » (démontré aussi en vrai : mes passages le portent). Fichier ignoré : « non suivi ».
  Corrigés.
- Restent, à git simulé : dépôt sans commit → `commit: "HEAD"` ; git qui refuse le dépôt (propriétaire douteux) →
  « hors dépôt git » ; `git status` en échec sur un fichier suivi → « commité, non modifié ».

**Correction.** Lire `returncode` de `rev-parse` et de `status`. Écrire « inconnu » en cas d'échec. Mettre au manifeste
le commit de chaque sortie.

### GD4-06 — mineur — Replis et erreurs restants

**Preuve (démontré, Q5).**
- `--ecarts ""` : passage synthétique sans refus.
- `--contraste-synthetique-de-secours` ignoré s'il n'a pas d'objet, mais écrit `true`. Quand il sert, la loi de secours
  (K[0], τ[0]) n'est nommée ni dans `lois` ni dans les cellules.
- `--effet-unite-a` avec τ = 0 (ou τ + biais ≥ 1) : aucun effet côté honnêtes, nom de loi inchangé.
- Identifiants : comparés après `str()`, donc 1 = « 1 » ; `true`, `null`, listes, objets admis. Identifiants
  facultatifs et JSON seulement.
- Fichier absent, dossier, virgule finale : erreurs Python brutes.
- Clé doublée et entier démesuré : même message « JSON illisible (ValueError) », motif perdu.

**Correction.**
- Refuser `--ecarts ""`.
- Refuser le secours sans objet. Écrire `contraste: "synthétique de secours (K, τ)"` dans la loi.
- Refuser l'effet d'unité si p₀ ∈ {0 ; 1}, ou l'écrire.
- Identifiants : chaînes non vides seulement.
- Rattraper `OSError` en refus nommé. Garder le message de l'exception.

## Table GD3-01 à GD3-08

| constat v3 | état en v4 | preuve |
|---|---|---|
| GD3-01 effet d'unité = biais d'espérance | **en partie** | Mécanique corrigée : logit recentré, E[p] = p₀ à 4·10⁻¹³ (trapèzes), Monte-Carlo |z| ≤ 2,5, bout en bout E[g] = 0 et frontière E[g] = δ ; lecture v3 retirée. Restent la lecture « la garde ne bouge pas » (GD4-01), le lien non séparé, E[f_A] non écrit (GD4-02) |
| GD3-02 ensembles d'unités, identifiant | **en partie, reste déclaré** | Identifiants vérifiés, même ordre (5 refus démontrés). Facultatifs, JSON seulement, comparés par `str()` (GD4-06). Un seul ensemble : refus explicite des longueurs différentes, coupe à l'intersection imposée (Q7) |
| GD3-03 replis silencieux | **corrigé** | Les quatre cas sont des refus nommés (démontré). Résidus mineurs autour de l'option de secours (GD4-06) |
| GD3-04 état git, commit | **en partie** | « hors dépôt git » et « non suivi » justes. Commit de la sortie σ = 0,5 absent du manifeste ; codes de retour non lus (GD4-05) |
| GD3-05 entrées | **en partie** | Clé doublée (même imbriquée), entier de 31 à 401 chiffres : refus nommés. Souligné en CSV toujours lu (GD4-03) |
| GD3-06 lectures | **corrigé** | « dépend de K et de τ » avec les quatre cas, tous exacts ; « δ = 0,10 résiste sauf K = 3, τ = 0,10 » exact ; « 0,07 à 0,12 » exact |
| GD3-07 seuils | **corrigé** | `m = 8` seul : pas de borne haute ; `α = 0,01` : « 100 (m = 1) » ; e-BH non simulée, dite en réserve |
| GD3-08 rôle, doublon | **en partie** | `role` et `comparateur` en sortie (démontré). Doublon repéré par le chemin écrit seulement (GD4-04). Métadonnées toujours impossibles à joindre (non repris par l'auteur, non relevé de nouveau) |

## Non vérifié

- « Sujet partagé = structure du pôle » : repris des contre-lectures v2 et v3, `engagement_apparie.py` non relu
  (consigne).
- La loi réelle : aucun fichier d'écarts réels fourni.
- Les commits `220cc259…` et `0f62f64a…` : pas de dépôt ici. Les cas git dans un dépôt ne sont démontrés qu'à git
  simulé.
- Python 3.13.18 : j'ai la 3.13.17 ; sorties identiques hors environnement.
- La phrase « vérifié sur 2 millions de tirages » de l'auteur : aucune trace ; remplacée par ma vérification.
- Le facteur « jusqu'à 5 » du partage : lu dans la sortie v3 « indépendants », non relancé.
- Le dépassement mémoire à 100 000 répétitions × 20 000 unités (GD2-10, non borné) : non exécuté.

## Fichiers produits (sous `…/relecture-garde-delta-v4/cl/`)

| fichier | rôle |
|---|---|
| `outils/copie_script/sim_garde_v4.py`, `sim_garde_v3.py` | copies conformes (`5bf015b6…`, `7b636c1e…`) |
| `outils/copie_pole/pari_apparie.py` | copie conforme du pôle v41 (`ec6c2cf6…`) |
| `outils/comparer_sorties.py` → `sorties/comparaison-*.json` | Q2 : v3 contre v4, reproductions |
| `outils/lancer_repro.sh` → `sorties/repro-*.json`, `sorties/neuve-*.json`, `sorties/codes.txt` | Q2 : même graine, graine 918273645 |
| `outils/verif_esperance.py` → `sorties/verif_esperance.json` | Q3 : espérance tenue, écarts-types ajoutés |
| `outils/verif_decomposition.py` → `sorties/verif_decomposition.json`, `.log` | Q3 : variantes Z, S, E, H, T, B, Bh |
| `outils/verif_fiche_pole.py` → `sorties/verif_fiche_pole.json` | Q4 : 1 200 fiches contre `evaluer` |
| `outils/verif_entrees.py` → `sorties/verif_entrees.json`, `sorties/essais_entrees/` | Q5 |
| `sorties/verif_ensembles_unites.txt` | Q7 : refus des deux ensembles |
| `outils/verif_etat_git.py` → `sorties/verif_etat_git.json` | GD3-04 : git simulé |
| `outils/verif_rapport.py` → `sorties/verif_rapport_auteur.json`, `sorties/verif_rapport_neuve.json` | Q2, Q6 |

Empreintes : `cl/EMPREINTES-contre-lecture-garde-delta-v4.txt`. Les fichiers `.err` sont tous vides.
