# Essais de la brique 1 de la méta-conception : encodage et mémoire spectrale (v1)

Lignée conv-audit, sous-agent. Horodatage (temps universel) : 2026-10-26T18:04:39Z.
Travail sur processeur seul, bibliothèque standard de Python, sans réseau ni dépôt ; Python lancé avec `-I -B`.
Statut : essais **exploratoires, non préenregistrés**. Ils servent à juger les affirmations du rapport et à écrire un protocole qui, lui, devra être scellé (R1) et contre-lu (R2) avant d'être lancé. Aucun chiffre ici n'est un résultat décisif.

## Verdict

- **Diagnostic du rapport : partiel.** Le terme v² porte 97,7 % de l'énergie des vecteurs relevés réels, et les cinq premières directions propres vivent à 98 % ou plus sur les cinq coordonnées carrées. Mais σ1 n'est pas une « variance qui explose » : c'est la direction moyenne commune des carrés (toujours positifs), qui explique 98 % de σ1. Le code normalise déjà chaque vecteur en sortie. Le rapport σ1/σ6 = 60,96 se factorise en 5,41 (effet de moyenne, σ1/σ5) × 11,28 (effet d'échelle carrés/linéaires, σ5/σ6), et le second croît avec le nombre de jetons.
- **Remède (ii), normaliser la base avant relèvement : partiel, et c'est le meilleur levier d'information.** Le rappel du plus proche voisin gagne +0,135 [0,114 ; 0,156] sur 180 corpus. La corrélation avec l'étalon passe de 0,37 à 0,60, et de 0,014 à 0,48 sur le corpus réel. σ1/σ6 baisse fortement : de 76,5–94,6 à 9,1–9,4 à 50 cycles quand le vocabulaire partagé reste à 30 % ou moins, et d'un facteur 35 en moyenne sur les corpus statiques. Il ne passe pourtant sous 12 que dans 17 % des corpus statiques, et vaut encore 18,1 à 50 cycles avec 60 % de vocabulaire partagé.
- **Centrage (iii) seul : insuffisant.** σ1/σ6 ne passe jamais sous 12 (22 à 3664 en statique ; moyennes de 27 à 31 en générations, aucun flux sous 12). L'information est inchangée : −0,007 [−0,015 ; 0,002]. Combiné à (ii), le centrage passe le seuil dans 30 flux sur 30, sans aucune information supplémentaire.
- **SimHash : gain établi au niveau du mot, par construction ; indécis au niveau du texte.**
  - Mot : aire sous la courbe 0,987 contre 0,458 pour SHA-256, mais seulement 0,870 face aux mots de même suffixe.
  - Texte : +0,025 en synthétique, +0,083 avec flexions, −0,148 sur le corpus réel.
  - Spectre : le remède complet SimHash + normalisation échoue à P1 (14,1 à 17,0 à 50 cycles, 0 flux sur 30 sous 12).
- **P1 : non valide comme test.** Il peut échouer, mais pour de mauvaises raisons :
  - l'encodage nul, sans aucune information, le passe dans 100 % des cas ;
  - les corpus les mieux encodés l'échouent ;
  - avec centrage, il est acquis d'avance dans le régime de l'organisme.

  Une version qui peut échouer est proposée au § 5.

## 1. Cadre et entrées

- J'ai lu `fournis/organisme/` : `memoire_isvd.py` en entier, le § 2.11 de `CONCEPTION.md`, et dans `principal.py` les passages sur les traces et sur l'arrêt (lignes 872 à 935, 1310 à 1325, 1380 à 1392, 1845 à 1860, 1925 à 1960, 1990 à 2150). J'ai aussi lu `fournis/rapport-meta-conception.md` en entier et `fournis/memoire-isvd-gen18.json`.
- J'ai écrit uniquement sous `sortie/`.
- Empreintes SHA-256 des entrées :
  - `fournis/organisme/memoire_isvd.py` : `e39295c5d3d04a45ef3024347bf30ee6744aee88fd77ea058e2c8f231f3e1710`. La copie `sortie/organisme_copie/memoire_isvd.py` est identique (vérifié).
  - `fournis/memoire-isvd-gen18.json` : `4866918f475555cef7ad2fae2ed05a1a855f54239741bcf187f1cd24ef7b0857`.
  - `fournis/rapport-meta-conception.md` : `96d12112c8d8d7e376943fa42fc0a4d6faed52b7ed09ae9ecac981c65949c6cf`.
- Chaque chiffre ci-dessous provient de `sortie/resultats/*-v1.json`. Les tableaux complets sont regénérés par `lire_resultats_v1.py` dans `resultats/tableaux-v1.md`, qui donne l'empreinte de chaque fichier lu.

## 2. Méthode

### 2.1 Encodages et variantes

Variantes demandées :

- **(i) Code tel quel.** `extraire_vecteur_koopman` : la base est la somme des SHA-256 par jeton ; le relèvement applique v, sin v ou v² selon l'indice modulo 3 ; la norme vaut 1 en sortie.
- **(ii) Remède du rapport.** La base est ramenée à norme 1 avant le relèvement ; relèvement et normalisation sont ensuite inchangés.
- **(iii) Centrage.** Encodage (i), mais la moyenne pondérée des exemplaires est retranchée avant le spectre.
- **(iv)** (ii) et (iii) combinés.

Variantes de référence ajoutées :

- **(v)** SimHash sur 3-grammes de caractères (projection), normalisé puis relevé : c'est le remède complet du rapport, appliqué au texte entier.
- **(vi)** (v) et centrage.
- **v_bin, vi_bin** : version binaire de SimHash.
- **« nul »** : une direction aléatoire par texte (graine tirée du SHA-256 du texte). Il ne porte aucune information.
- **« base »** : base SHA-256 normée, sans relèvement. Elle montre l'information disponible avant le relèvement.

Définition du SimHash :

- On découpe en 3-grammes chaque jeton bordé par « # ».
- La coordonnée i (de 0 à 15) d'un 3-gramme g vaut +1 si le bit i des 32 premiers bits de SHA-256(« brique1-simhash3-v1| » + g) vaut 1, et −1 sinon.
- La projection est la somme des vecteurs de signes ; la version binaire en prend le signe.
- La table effectivement utilisée est consignée dans `resultats/table-signes-simhash-essai3-v1.tsv` (345 3-grammes).

Tokeniseur : c'est celui de l'organisme, soit `[a-zA-Z0-9_\\]+` sur le texte en minuscules. Les lettres accentuées coupent donc les mots : « évaluation » devient « valuation ».

### 2.2 Mémoire

- **Statique.** On décompose Σ w ψψᵀ (ou la dispersion centrée) d'un corpus de deux façons : par le Jacobi du code (120 itérations) et par un Jacobi cyclique mené à convergence. Les rapports cités sont ceux de la décomposition exacte, sauf mention contraire.
- **Générations.** 50 générations de 40 traces, avec la construction de l'organisme : m = U Σ Uᵀ + Σ w ψψᵀ, troncature au rang 6, Σ arrondi à 6 décimales. On garde la version du code et la version exacte.
  - Pour (i), l'appel direct à `mettre_a_jour_memoire_isvd` et le chemin du pilote donnent des Σ **identiques bit à bit** sur les 30 flux.
  - Les variantes centrées gardent la moyenne courante et le poids total, et mettent à jour la dispersion par la formule des axes parallèles. Sans troncature, cette mise à jour égale le calcul d'un bloc à 1,4·10⁻⁶ près, écart dû à l'arrondi de Σ.

### 2.3 Corpus

- **Synthétiques.**
  - Vocabulaires : 5 domaines de 50 mots, 40 mots-outils, 30 mots de méthode. Les listes sont disjointes (vérifié). Tirage selon une loi de Zipf d'exposant 1.
  - `p_commun` est la part des jetons tirés du vocabulaire partagé (2/3 de mots-outils, 1/3 de mots de méthode). 20 % des textes sont des ponts entre deux domaines. Les poids sont uniformes sur [0,6 ; 0,9].
  - Grille statique : N ∈ {12, 25, 50} × p_commun ∈ {0 ; 0,3 ; 0,6} × 20 graines, soit 180 corpus de 30 à 300 jetons.
  - Régime générationnel : 20 à 100 jetons et 10 graines par niveau de vocabulaire partagé. Repères réels : les 27 textes réels ont 16 à 82 jetons, et les 40 mots-outils font 24,5 % des jetons des 12 exemplaires réels.
- **Réel d'ancrage.** 27 textes : les 12 exemplaires uniques du json et les 15 références moissonnées citées au § 3 du rapport. Réserve : ces 12 exemplaires sont ceux que la mémoire a retenus, donc les plus alignés sur u1.

### 2.4 Mesure d'information (fixée avant les essais 2 à 5)

- **Rappel au premier rang (noté R@1), mesure principale.**
  - Pour chaque texte i, on cherche son plus proche voisin par cosinus dans l'espace de la variante : ψ pour (i), (ii) et (v) ; ψ − μ pour (iii), (iv) et (vi).
  - C'est un succès si ce voisin appartient à l'ensemble des plus proches voisins de i par similarité de Jaccard des ensembles de jetons, ex aequo compris.
  - Le niveau du hasard est la moyenne de |étalon|/(N − 1).
  - On la calcule aussi sur les coordonnées de rang 6, c'est-à-dire ce que garde la mémoire.
- **Mesure secondaire.** Corrélation de rang de Spearman, sur toutes les paires, entre cosinus et Jaccard (ci-dessous « Spearman »).
- **Garde testée sur un cas sain et sur un artefact (R5).** Sacs de mots complets : R@1 = 0,88 (hasard 0,021). Encodage nul : R@1 = 0,02.
- **Graines.** On utilise `random.Random(graine)`, le même générateur que `random.seed`. La graine est formée des 8 premiers octets de SHA-256(« 20261026|tâche|indices »). La règle et la graine maîtresse sont consignées dans chaque manifeste de résultat.

## 3. Résultats

### Essai 1 — forme du spectre et origine

**Spectre réel** (json, génération 18) :

- σ1/σ6 = 60,963. Le rapport écrit 60,9, par troncature ; l'arrondi donne 61,0.
- σ1/σ5 = 5,406 et σ5/σ6 = 11,276.
- Part de chaque vecteur propre sur (linéaires ; sinus ; carrés) :
  - u1 : (0,02 ; 0 ; 0,98) ;
  - u2 à u5 : (0 ; 0 ; 1,00) ;
  - u6 : (0,99 ; 0 ; 0).
- Les composantes de u1 sur les cinq carrés sont toutes positives : 0,51 ; 0,37 ; 0,57 ; 0,39 ; 0,33.
- Les coordonnées sinus sont absentes des six directions.
- Sur les 12 exemplaires réels, 97,7 % de |ψ|² est sur les carrés, et ⟨ψ, u1⟩ vaut 0,922 en moyenne (minimum 0,895).

**Reproduction** :

- En générations (18 cycles de 40 traces), σ1/σ6 vaut 74,6 ± 12,0, 93,9 ± 16,0 et 89,7 ± 7,3 pour p_commun = 0 ; 0,3 ; 0,6. C'est le même ordre de grandeur que 61.
- La somme des σ vaut 532 à 533, contre 513 dans le json.
- La structure propre est la même : u1 à u5 sont à 0,99 ou plus sur les carrés, u6 à 0,98 ou plus sur les linéaires.
- Sur le corpus réel d'ancrage, traité en un seul lot, σ1/σ6 = 84,7.

**Origine 1 : la direction moyenne.**

- Part de σ1 portée par la moyenne, W‖μ‖²/σ1 :
  - 0,980 sur le corpus réel ;
  - 0,976 sur les 180 corpus statiques ;
  - 0,960 à 0,981 en générations.
- Quotient de Rayleigh μ̂ᵀMμ̂/σ1 : 0,9993 sur le réel, 0,997 en statique.
- |⟨u1, μ̂⟩| : 0,9996 sur le réel, 0,997 à 0,999 en générations.
- ⟨ψ, μ̂⟩ moyen : 0,830 sur le réel ; de 0,53 (3 jetons) à 0,81 (300 jetons).
- Réserve sur l'expression « quasi rang 1 » du brief : σ1 ne porte que 52 % de la trace réelle (rang effectif 3,96). σ2 à σ5 sont la variance des carrés autour de leur moyenne.

**Origine 2 : l'effet d'échelle.** Balayage en longueur (N = 50, p_commun = 0,3, 10 graines, encodage (i)) :

| jetons | part des carrés dans ψ | σ1/σ6 | σ1/σ5 | σ5/σ6 |
|---|---|---|---|---|
| 3 | 0,521 | 4,9 | 4,2 | 1,2 |
| 10 | 0,805 | 10,7 | 7,1 | 1,5 |
| 30 | 0,950 | 38,5 | 9,6 | 4,1 |
| 60 | 0,984 | 122,1 | 11,9 | 11,2 |
| 100 | 0,994 | 380,3 | 16,6 | 23,0 |
| 300 | 0,9996 | 6063 | 28,5 | 226,0 |

- σ5/σ6 (carrés contre linéaires) croît comme le nombre de jetons. σ1/σ5 (moyenne contre variance des carrés) croît lentement.
- Les deux hypothèses du brief sont confirmées : (a) l'échelle de la base, (b) la direction commune des carrés.

**Information sous (i).**

- Sur le corpus réel, R@1 = 0,000 (hasard 0,038) et Spearman = 0,014.
- La base SHA-256 avant relèvement garde pourtant Spearman = 0,570 et R@1 = 0,148.
- C'est donc le relèvement non normalisé qui efface la similarité, pas le hachage.

### Essai 2 — quatre variantes, mêmes corpus, mêmes graines

**180 corpus statiques** (30 à 300 jetons ; hasard de R@1 : 0,056) :

| variante | σ1/σ6 moyen [min ; max] | part ≤ 12 | R@1 | R@1 rang 6 | Spearman | Spearman rang 6 |
|---|---|---|---|---|---|---|
| (i) code | 848 [30 ; 14042] | 0 | 0,224 | 0,221 | 0,369 | 0,368 |
| (ii) base normée | 24,0 [7,2 ; 93,9] | 0,17 | 0,359 | 0,346 | 0,599 | 0,595 |
| (iii) centrage | 284 [22 ; 3664] | 0 | 0,217 | 0,216 | 0,345 | 0,344 |
| (iv) (ii) + (iii) | 12,3 [3,3 ; 65,3] | 0,60 | 0,362 | 0,353 | 0,543 | 0,544 |
| (v) SimHash | 31,7 [8,8 ; 84,0] | 0,01 | 0,383 | 0,373 | 0,580 | 0,577 |
| (vi) SimHash centré | 18,5 [5,0 ; 77,9] | 0,29 | 0,384 | 0,367 | 0,559 | 0,560 |
| nul | 2,4 [1,5 ; 4,5] | 1,00 | 0,059 | 0,055 | −0,003 | −0,002 |
| base sans relèvement | 23,4 [8,2 ; 81,3] | 0,11 | 0,381 | 0,362 | 0,621 | 0,616 |

Différences appariées de R@1, avec intervalle à 95 % par rééchantillonnage (n = 180) :

- (ii) − (i) = +0,135 [0,114 ; 0,156] ;
- (iii) − (i) = −0,007 [−0,015 ; 0,002] ;
- (iv) − (i) = +0,138 [0,117 ; 0,159] ;
- (iv) − (ii) = +0,003 [−0,005 ; 0,012].

**50 cycles (P1 au pied de la lettre)** : σ1/σ6 à la génération 50, et nombre de flux sous 12 sur 10 :

| variante | p_commun 0 | p_commun 0,3 | p_commun 0,6 |
|---|---|---|---|
| (i) | 76,5 (0/10) | 94,6 (0/10) | 89,8 (0/10) |
| (ii) | 9,1 (10/10) | 9,4 (10/10) | 18,1 (0/10) |
| (iii) | 26,9 (0/10) | 31,0 (0/10) | 27,2 (0/10) |
| (iv) | 8,9 (10/10) | 4,8 (10/10) | 2,7 (10/10) |
| (v) SimHash + normalisation | 15,5 (0/10) | 14,1 (0/10) | 17,0 (0/10) |
| (vi) | 14,2 (0/10) | 9,3 (10/10) | 4,4 (10/10) |
| nul | 1,2 (10/10) | 1,2 (10/10) | 1,2 (10/10) |

**Corpus réel d'ancrage** (27 textes ; hasard de R@1 : 0,038) :

| variante | σ1/σ6 | R@1 | Spearman |
|---|---|---|---|
| (i) | 84,7 | 0,000 | 0,014 |
| (ii) | 6,27 | 0,222 | 0,479 |
| (iii) | 13,85 | 0,037 | 0,003 |
| (iv) | 3,41 | 0,222 | 0,278 |
| (v) | 5,45 | 0,074 | 0,198 |
| nul | 2,10 | 0,000 | −0,024 |
| base | 5,39 | 0,148 | 0,570 |

Lecture :

- **(ii)** fait disparaître l'effet d'échelle. La part des carrés dans ψ tombe de 98 % à 11 % (60 jetons). σ5/σ6 à la génération 18 passe de 7,1–10,2 à 1,2–3,6. L'information est rendue : Spearman 0,60, contre 0,62 pour la base nue.
- Sous (ii), la direction commune persiste : W‖μ‖²/σ1 vaut 0,87 en statique et 0,65 à 0,97 en générations. σ1/σ6 dépasse donc 12 dès que le vocabulaire partagé ou la longueur augmentent : 18,1 à p_commun = 0,6, 34,3 à 300 jetons.
- **(iii)** retire la direction moyenne : |⟨u1, μ̂⟩| passe de 0,998 à 0,18 en statique. Il ne retire pas l'effet d'échelle : u1 à u4 restent sur les carrés. Aucun gain d'information.
- **(iv)** aplatit le spectre sans gagner d'information sur (ii). Spearman baisse même : 0,543 contre 0,599, et 0,278 contre 0,479 sur le réel. L'étalon de Jaccard contient en effet le recouvrement des mots-outils, que le centrage retire.

### Essai 3 — SimHash contre SHA-256 par jeton

On compare trois familles de 30 paires :

- **fléchies** : spectral/spectrale, spectral/spectraux, martingale/martingales, normalise/normalisation… ;
- **sans rapport** : les mêmes mots, appariés avec un décalage ;
- **sans rapport de même suffixe** : optimisation/organisation, regularisation/popularisation, gradient/ingredient…

Cosinus moyen ± écart-type :

| représentation | fléchies | sans rapport | même suffixe | aire fl./sans rapport | aire fl./même suffixe |
|---|---|---|---|---|---|
| SHA-256 par jeton | −0,015 ± 0,277 | 0,023 ± 0,254 | −0,032 ± 0,292 | 0,458 | 0,502 |
| SimHash, projection | 0,728 ± 0,157 | 0,055 ± 0,256 | 0,433 ± 0,252 | 0,987 | 0,870 |
| SimHash, binaire | 0,567 ± 0,185 | 0,100 ± 0,265 | 0,317 ± 0,264 | 0,917 | 0,783 |
| SimHash projection, normée puis relevée | 0,749 ± 0,155 | 0,043 ± 0,257 | 0,457 ± 0,269 | 0,986 | 0,883 |
| cosinus exact des 3-grammes (étalon) | 0,711 ± 0,093 | 0,010 ± 0,041 | 0,480 ± 0,152 | 1,000 | 0,913 |

- Corrélation de Spearman avec l'étalon exact : 0,859 pour la projection SimHash, 0,680 pour le binaire, −0,068 pour SHA-256.
- Au niveau du texte, différences de R@1 par rapport à (ii) :
  - (v) − (ii) = +0,025 [0,008 ; 0,042] sur les 180 corpus ;
  - corpus fléchi (la moitié des mots de contenu au pluriel) avec étalon par lemmes : (v) − (ii) = +0,083 [0,051 ; 0,115] ;
  - corpus réel : 0,074 contre 0,222 (Spearman 0,198 contre 0,479) ;
  - version binaire : v_bin − (ii) = −0,094 [−0,116 ; −0,074].

Lecture :

- Le gain annoncé existe au niveau du mot, mais il est acquis par construction : c'est la définition même d'un hachage de 3-grammes. Il amène des faux voisins de même suffixe (cosinus 0,43).
- Au niveau du texte, la somme des SHA-256 par jeton n'est pas « maximalement non informative » : la base garde Spearman = 0,62.
- Le gain de SimHash sur le texte est petit en synthétique, et de signe contraire sur le seul corpus réel disponible.

### Essai 4 — critère d'arrêt

**Le code v6.2.1 n'a pas de critère de convergence spectrale.**

- `fin_conception.json` s'écrit dans trois cas (`principal.py`, lignes 2103 à 2106) :
  - score interne ≥ 0,78 et au moins 2 exemplaires ;
  - ronde ≥ 2 et score ≥ 0,65 ;
  - dernière ronde.
- La mémoire n'entre que par « au moins 2 exemplaires ». Cette condition est vraie dès la première génération : 12 exemplaires retenus sur tous les flux.
- `CONCEPTION.md` § 2.11.4 annonce que l'organisme écrit `fin_conception.json` « dès que son score interne de Bregman-Tsallis et sa mémoire ISVD atteignent le seuil de convergence ». La partie mémoire n'est pas implémentée.
- Un changement d'encodage ne change donc rien à l'arrêt actuel.

**Critère hypothétique testé.**

- σ̂ = Σ / somme(Σ) sur le rang 6, et d(g) = max_k |σ̂_k(g) − σ̂_k(g − 1)|.
- Arrêt à la première génération où deux d(g) consécutifs sont inférieurs à ε.

Génération de déclenchement (médiane [minimum – maximum] sur 10 flux) :

| p_commun | ε | (i) | (iv) | nul |
|---|---|---|---|---|
| 0 | 0,005 | 9 [7–11] | 11 [6–15] | 11 [9–15] |
| 0 | 0,002 | 15 [11–19] | 25 [11–33] | 23 [18–28] |
| 0,3 | 0,005 | 8 [6–12] | 13 [8–15] | 11 [8–14] |
| 0,3 | 0,002 | 18 [11–22] | 24 [19–30] | 24 [10–33] |
| 0,6 | 0,005 | 8 [5–10] | 13 [9–16] | 11 [8–15] |
| 0,6 | 0,002 | 14 [7–28] | 28 [16–33] | 27 [20–30] |

d(g) décroît en 1/g pour toutes les variantes, encodage nul compris. À p_commun = 0,3, pour (i), (iv) et nul :

- d(10)·10 = 0,029 ; 0,048 ; 0,041 ;
- d(50)·50 = 0,035 ; 0,050 ; 0,050.

Lecture :

- À ε fixe, passer de (i) à (iv) retarde l'arrêt d'un facteur 1,2 à 2,0 pour ε ≤ 0,005. Un re-étalonnage serait donc nécessaire si un tel critère existait.
- Mais le critère déclenche aux mêmes générations sous l'encodage nul. Sur une mémoire qui accumule sans oubli, il mesure la dilution d'un lot dans la somme, pas une convergence.
- Un critère spectral éventuel doit être rapporté à un nul (permutation des lots, ou suivi de d(g)·g), jamais à un ε fixe.

Effet de bord de la troncature au rang 6 :

- Elle perd 1,2 à 1,5 % de l'énergie de chaque lot sous (i), 18 à 33 % sous (iv), et 62 % sous l'encodage nul.
- Le sous-espace de la mémoire reste proche de celui de l'accumulation sans troncature : recouvrement de 0,96 à 0,997 sous (i) et de 0,91 à 0,92 sous (iv).
- Seul l'encodage nul gèle son sous-espace (recouvrement 0,57 à 0,59).

### Essai 5 — P1 peut-il échouer, ou est-il acquis d'avance ?

P1 du rapport : « σ1/σ6 passe de 60,9 à ≤ 12 sur 50 cycles grâce à la normalisation sphérique pré-Koopman ».

1. **Il peut échouer.**
   - (ii) à p_commun = 0,6 : 18,1, avec 0 flux sur 10 sous 12 ;
   - (ii) sur 300 jetons : 34,3 ;
   - remède complet SimHash + normalisation : 14,1 à 17,0, avec 0 flux sur 30 sous 12.

   Il n'est donc pas acquis pour (ii) seul.
2. **Il est passé par un encodage sans information.** L'encodage nul reste à σ1/σ6 ≤ 4,5 dans 100 % des corpus et des flux (moyennes : 2,4 en statique, 1,2 en générations), avec Spearman ≈ 0.
3. **Il échoue là où l'information est la mieux conservée.** Sur des corpus structurés (2, 3 ou 5 domaines, 200 à 300 jetons, sans ponts), (iv) donne σ1/σ6 de 16 à 97 selon les corpus (moyennes par cellule de 19 à 60 ; aucun des 60 corpus sous 12), avec Spearman = 0,47 à 0,81. Un corpus à k domaines a k − 1 grandes valeurs propres centrées, donc un σ1/σ6 grand dès que k − 1 < 6.
4. **Avec centrage, il est acquis dans le régime de l'organisme** : (iv) passe dans 30 flux sur 30, avec σ1/σ6 de 2,5 à 9,7 selon les flux.
5. **Sa référence n'est pas fixe.** Le σ1/σ6 de v6.2.1 varie de 58,6 à 65,3 entre les générations 13 et 18 de l'archive, et croît avec la longueur des traces.

Conclusion : P1 est un test échouable, mais son issue dépend du vocabulaire partagé, de la longueur et du nombre de domaines, pas de l'information conservée. Un spectre plat est la signature du bruit isotrope.

**Variante de P1 donnée par la caste 2.** Elle annonce un rang effectif exp(−Σσ̂ ln σ̂) passant de 1,82 à ≥ 3,40. Or le json donne 3,96 avec σ̂ = σ/Σσ, et 1,98 avec σ²/Σσ². Aucune lecture ne donne 1,82, et avec la formule écrite, v6.2.1 dépasse déjà 3,40.

## 4. Verdicts par affirmation du rapport

| # | Affirmation (lieu dans le rapport) | Verdict | Chiffre qui le montre |
|---|---|---|---|
| A1 | « v² écrase le spectre (σ1 = 269 ≫ σ6 = 4,41) » (synthèse, castes 4 et 5) | partielle | v² porte 97,7 % de l'énergie réelle, et u1–u5 sont à 98 % ou plus sur les carrés. Mais σ1 est la direction moyenne (W‖μ‖²/σ1 = 0,98), pas une variance. Sa valeur absolue suit l'accumulation sans oubli : en simulation, Σσ = 532 à la génération 18 pour environ 540 de poids injecté. |
| A2 | « due à l'absence de normalisation avant v² ; la normalisation sphérique l'empêche » (§ 2, caste 4) | partielle | L'effet d'échelle disparaît : σ5/σ6 passe de 7,1–10,2 à 1,2–3,6. La direction commune reste : W‖μ‖²/σ1 = 0,65–0,97. σ1/σ6 dépasse 12 dans 83 % des corpus statiques. |
| A3 | « Koopman sur bruit blanc amplifie la variance isotrope » (caste 2) | réfutée | Le spectre est fortement anisotrope : σ1/σ6 = 61, et cinq directions sur six occupent les cinq coordonnées carrées. |
| A4 | « SHA-256 vers R¹⁶ est maximalement non informatif ; les cosinus se concentrent » (castes 1 et 3) | réfutée (niveau du texte) | Base SHA-256 : Spearman 0,621 (statique) et 0,570 (réel) ; R@1 0,381 contre 0,056 au hasard. Écart-type des cosinus de mots : 0,25 à 0,29. |
| A5 | « SHA-256 détruit la topologie locale ; SimHash 3-grammes préserve le cosinus » (synthèse, caste 2) | établie au niveau du mot, par construction | Aire sous la courbe 0,987 contre 0,458 ; Spearman 0,859 avec le cosinus exact. Réserve : 0,870 face aux mots de même suffixe. |
| A6 | La géométrie de la mémoire gagne avec SimHash (implicite) | partielle | +0,025 [0,008 ; 0,042] en synthétique et +0,083 avec flexions ; −0,148 sur le corpus réel ; version binaire −0,094. |
| A7 | P1 : « σ1/σ6 de 60,9 à ≤ 12 grâce à la normalisation sphérique » (prédiction) | partielle | (ii) donne 9,1–9,4 à p_commun ≤ 0,3, mais 18,1 à 0,6. SimHash + normalisation donne 14,1–17,0 (0 flux sur 30). |
| A8 | P1 est un protocole falsifiable qui atteste le gain | réfutée | L'encodage nul passe dans 100 % des cas sans aucune information. Les corpus structurés bien encodés échouent (0 sur 60). Avec centrage, 30 flux sur 30 passent. |
| A9 | Variante de la caste 2 : rang effectif de 1,82 à ≥ 3,40 | réfutée | Le json donne 3,96 (ou 1,98) ; v6.2.1 dépasse déjà 3,40. |
| A10 | « Le rang 6 capture la dérive des moments pairs ; filtre aveugle » (caste 4) | établie | u1–u5 sont sur les carrés. Sous (i), sur le corpus réel : R@1 = 0,000, Spearman = 0,014. |
| A11 | La mémoire spectrale entre dans l'arrêt par un « seuil de convergence » (CONCEPTION.md § 2.11.4) | réfutée | Le code ne lit que « au moins 2 exemplaires » (`principal.py`, lignes 2103 à 2106). |

## 5. Protocole P1′ — une version qui peut échouer

À sceller avant tout calcul (R1), puis à faire contre-lire par un sous-agent neuf (R2).

- **Hypothèse.** L'encodage proposé garde dans la mémoire de rang 6 plus de similarité entre textes que l'encodage v6.2.1.
- **Métrique principale.**
  - Corrélation de rang de Spearman, sur toutes les paires d'un corpus, entre deux grandeurs :
    - le cosinus des coordonnées de rang 6, avec les vecteurs propres tels que la mémoire les stocke ;
    - la similarité de Jaccard des ensembles de jetons.
  - Moyenne sur le banc de corpus.
  - Métrique secondaire : R@1 de rang 6.
  - σ1/σ6 est rapporté pour description, jamais comme seuil.
  - Le R@1 n'est pas retenu comme métrique principale parce qu'il reste faible sur les corpus très structurés. À l'essai 5, il vaut 0,05 à 0,14 sous (iv), soit deux à cinq fois le hasard, alors que la corrélation de Spearman sépare nettement (iv) du nul : 0,47 à 0,81 contre ≈ 0.
- **Nuls.**
  1. L'encodage v6.2.1, apparié corpus par corpus.
  2. L'encodage aléatoire, avec une direction par texte.
  3. 1000 permutations des textes dans chaque corpus, qui donnent le 95e centile nul de la corrélation.
- **Seuil**, fixé avant les données. L'essai réussit si trois conditions sont réunies ; sinon il échoue :
  - gain moyen ≥ +0,10 sur v6.2.1 ;
  - borne basse de l'intervalle à 95 % (rééchantillonnage apparié) > 0 ;
  - corrélation au-dessus du 95e centile de permutation dans au moins 90 % des corpus.
- **Banc figé.**
  - Une grille synthétique à graines scellées, qui inclut p_commun = 0,6 et des textes de 300 jetons.
  - Le corpus réel d'ancrage tiré de `fournis/`.
  - Une moisson réelle neuve, jamais vue, d'au moins 100 traces.
- **Lecture symétrique (R4).** Un gain sur le synthétique accompagné d'un gain négatif sur le réel vaut réserve, pas succès.
- **S'il faut aussi un critère spectral.**
  - Analyse parallèle de Horn sur la mémoire centrée : on compte les valeurs propres qui dépassent le 95e centile de la valeur propre de même rang sous l'encodage aléatoire de même taille.
  - On l'accompagne d'une prédiction chiffrée, par exemple au moins k − 1 pour un corpus à k domaines. Ce critère peut échouer dans les deux sens.
- **Indication, non opposable** (seuil écrit après avoir vu ces données exploratoires) :
  - (ii) contre (i) : 0,595 contre 0,368 (+0,23) ; sur le corpus réel, 0,450 contre 0,011.
  - P1′ échouerait en revanche pour SimHash face à (ii) : 0,577 contre 0,595, soit −0,02.

## 6. Réserves

- **Corpus synthétiques** : petit vocabulaire (250 mots de contenu), donc un recouvrement de Jaccard plus fort qu'en réel. Le corpus réel ne compte que 27 textes, dont 12 sélectionnés par la mémoire elle-même.
- **Séparation Domaine/Opérateur du rapport** : non testée, car le lexique n'est pas spécifié. SimHash est appliqué au texte entier. Le verdict A7 sur le remède complet vaut pour cette lecture seulement.
- **Étalon par jetons** : il est aveugle à la morphologie. L'étalon par lemmes ne couvre que des pluriels synthétiques.
- **Jacobi du code** : il n'est pas convergé en 120 itérations. L'écart reste sous 0,26 % sur σ1 à σ6 sous (i) et atteint 4,5 % sous (ii) en statique (0,16 % sur une matrice générique). Les rapports code et exact restent à moins de 4 % en générations, et aucun verdict n'en dépend.
- **Poids et bonus** : poids uniformes ; aucun bonus multi-familles, car aucun mot-clé n'apparaît dans les corpus synthétiques.
- **Statut** : exploratoire, sans contre-lecture par un sous-agent neuf, puisque le brief interdit les sous-agents. À signaler pour R2.
- **Brouillons** : les sorties des passes de mise au point sont rangées sans modification dans `resultats/brouillons-1/`. Elles ont été produites par des versions antérieures des scripts, dont les empreintes figurent dans leurs manifestes. Aucun chiffre de ce rapport n'en vient.

## 7. Fichiers et empreintes (SHA-256)

Scripts (lancés par `python3 -I -B pilote_brique1_v1.py <essai> --horodatage "$(date -u +%Y-%m-%dT%H:%M:%SZ)"`) :

- `pilote_brique1_v1.py` : `d08f794c1d4b690183e6d55dd60fce373ff602fd2964143407aace40a874d38c`
- `brique1_communs_v1.py` : `7b2fa00e636b8e416ad4b7f4fafaab9e63697bca3d823c9d855c215c2767fcca`
- `simhash_ngrammes_v1.py` : `01ad6d0aa0305eb8528151cc81fb7e2b8413b7f88ef401a3a3ef49756b4913af`
- `lire_resultats_v1.py` : `7665c25a3bc07ccdc08ac9b5ced3417ef3c30fbb78c7a280a1ce6911cbce9352`
- `organisme_copie/memoire_isvd.py` : `e39295c5d3d04a45ef3024347bf30ee6744aee88fd77ea058e2c8f231f3e1710`

Résultats (chaque manifeste porte l'horodatage, la version de Python 3.13.17, les graines et les empreintes ci-dessus) :

- `resultats/verifications-v1.json` : `29bc36a4c46e2f150c3b6b30fe61ce2095f373b9489c30a8f59029916b20c2f4`
- `resultats/reel-v1.json` : `5da88e60d38854527c216b1afd4dc2d24d78d272003876fbfda97ebbd8de04c2`
- `resultats/essai1-v1.json` : `a91504917924fd8e3390ee12558390e369d7f20c372480b060ed68fcfb6fa59c`
- `resultats/essai2-v1.json` : `6c67454c2c5366b28cd427fcfdec78790519516fe55060a26f623612b75ea543`
- `resultats/essai3-v1.json` : `c3ef827f396023cd666969db1d670318648309b47e6bef92d140749e9bdf1c01`
- `resultats/essai5-v1.json` : `47e55bd15fced9d7d51d569fbe580b6abb119d426556c8387f6d1eb2a932b9df`
- `resultats/generations-v1.json` (essais 1, 2 et 4) : `017fefe007cbb49358c24bea5ada2eb027e23d097c95b4f219b4d638c3583f28`
- `resultats/table-signes-simhash-essai3-v1.tsv` : `88e5a66e202c791a70cd51e3abf4dd13825eaa7b985d727fd26c7d03958782b4`
- `resultats/tableaux-v1.md` : `a2f6c6694d65dad68b73bf2ffc955cab824ca697bd071c5c028137687f242f7a`

Chaque fichier a un compagnon `.sha256`, vérifiable par `sha256sum -c` depuis son dossier.

## 8. Génération 0 — sélection par réfutation (une ligne par affirmation)

Affirmations du rapport :

- B1-01 « Le terme v² domine la mémoire spectrale » — **survit** — 97,7 % de |ψ|² réel sur les carrés ; u1–u5 à 98 % ou plus sur les carrés.
- B1-02 « σ1 = 269 traduit une explosion de variance due à v² » — **éliminée** — σ1 est la direction moyenne (W‖μ‖²/σ1 = 0,98 ; quotient de Rayleigh 0,9993) ; sa valeur suit le poids accumulé (en simulation, Σσ = 532 pour environ 540 injectés).
- B1-03 « La normalisation sphérique pré-Koopman supprime l'écrasement d'échelle par v² » — **survit** — part des carrés de 98 % à 11 % ; σ5/σ6 de 7,1–10,2 à 1,2–3,6.
- B1-04 « Cette normalisation suffit à ramener σ1/σ6 ≤ 12 » — **indécise** — 17 % des corpus statiques ; 10 flux sur 10 à p_commun ≤ 0,3 mais 0 sur 10 à 0,6 ; 6,27 sur le corpus réel.
- B1-05 « Koopman sur bruit blanc amplifie la variance isotrope » — **éliminée** — σ1/σ6 = 61, une seule direction propre hors des carrés.
- B1-06 « SHA-256 vers 16 dimensions est maximalement non informatif, cosinus concentrés » — **éliminée** — base : Spearman 0,62 (statique) et 0,57 (réel) ; R@1 0,381 contre 0,056.
- B1-07 « SimHash 3-grammes préserve la proximité morphologique que SHA-256 détruit » — **survit** — aire 0,987 contre 0,458 ; faux voisins de même suffixe : 0,870.
- B1-08 « SimHash améliore la géométrie de la mémoire au niveau du texte » — **indécise** — +0,025 et +0,083 en synthétique ; −0,148 sur le réel.
- B1-09 « SimHash + normalisation sphérique ramène σ1/σ6 ≤ 12 sur 50 cycles » — **éliminée** — 14,1 à 17,0, 0 flux sur 30 (texte entier ; séparation Domaine/Opérateur non testée).
- B1-10 « P1 atteste le gain de la v6.3 » — **éliminée** — encodage nul : 100 % sous 12 (≤ 4,5 partout) ; corpus structurés bien encodés : 0 sur 60.
- B1-11 « Rang effectif de 1,82 en v6.2.1 » (caste 2) — **éliminée** — 3,96 (σ) ou 1,98 (σ²) sur le json.
- B1-12 « Le rang 6 suit les moments pairs et devient aveugle à la similarité » (caste 4) — **survit** — sous (i), sur le réel : R@1 = 0,000 (hasard 0,038) ; Spearman = 0,014.
- B1-13 « La mémoire spectrale entre dans l'arrêt par un seuil de convergence » (CONCEPTION.md § 2.11.4) — **éliminée** — seule condition lue : au moins 2 exemplaires (`principal.py`, lignes 2103 à 2106).

Hypothèses du brief (pas du rapport) :

- H-a « La base non normalisée a des composantes qui croissent avec le nombre de jetons » — **survit** — σ5/σ6 passe de 1,2 (3 jetons) à 226 (300 jetons).
- H-b « Les carrés ont une direction commune que la normalisation par vecteur n'enlève pas » — **survit** (sauf « quasi rang 1 ») — 97 à 98 % de σ1 ; mais σ1 ne fait que 52 % de la trace (rang effectif 3,96).
- H-c1 « Le centrage seul suffit à passer P1 » — **éliminée** — jamais sous 12 (22 à 3664 en statique ; moyennes de 27 à 31 en générations, 0 flux sur 30).
- H-c2 « (ii) + centrage rend P1 acquis d'avance dans le régime de l'organisme » — **survit** — 30 flux sur 30 sous 12 (2,5 à 9,7), sans gain d'information sur (ii) (+0,003 [−0,005 ; 0,012]).
- H-d « Un critère de Cauchy à ε fixe reste valable après un changement d'encodage » — **éliminée** — médianes de déclenchement multipliées par 1,2 à 2,0 (ε ≤ 0,005) ; l'encodage nul déclenche aux mêmes générations.
