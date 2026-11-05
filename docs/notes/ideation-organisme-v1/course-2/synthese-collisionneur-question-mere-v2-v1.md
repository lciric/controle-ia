# Synthèse du collisionneur — question-mère v2 (quelle question poser à la course d'idéation) — v1

**Auteur** : sous-agent neuf (Opus 5.5), qui n'a écrit aucune pièce lue. Lecture commencée le 2026-10-29 à 22:29 UTC, rédaction
commencée à 22:32 UTC (`date -u`). Aucun commit, aucun réseau. Rien d'autre n'a été ouvert que les pièces ci-dessous, leurs
compagnons `.sha256` et la synthèse antérieure du tour « repli de G0 », qui donne le format. **Ce document est du matériau pour Lazar
et pour le recoupement de conv-audit. Il ne tranche rien.**

**Pièces.** Toutes sont lues sur `origin/donnees/collisionneur-question-mere-v2` par `git show`. Chaque empreinte recalculée est égale
à son compagnon `.sha256`. Aucune pièce n'est sans compagnon.

| Pièce | Empreinte (début) | Lignes |
|---|---|---|
| `question-question-mere-v2.md` | `e5a4bd858fdd3a81` | 200 |
| `faits-question-mere-v2.md` | `fa868221167ac686` | 1 274 |
| `E3-T1-conception-A.md` | `2332bc33311c50a0` | 156 |
| `E3-T1-conception-B.md` | `007c8a14588b7aaf` | 301 |
| `E3-T1-conception-C.md` | `2d930eac0ea98cb4` | 147 |
| `E3-T2-redteam-A.md` | `5d38d2c54580db15` | 105 |
| `E3-T2-redteam-B.md` | `5cd8393edfcf6a3c` | 197 |
| `E3-T2-redteam-C.md` | `13daad308fa92ea8` | 109 |
| `E3-T3-riposte-A.md` | `8b874fb5cfae84f9` | 100 |
| `E3-T3-riposte-B.md` | `ce957f2a4860a1ad` | 288 |
| `E3-T3-riposte-C.md` | `14f3872a4f414090` | 125 |

Les cellules sont sous `…/run-question-mere-e3-v2/cellules/`. On les note T1-A … T3-C, avec A = Fable 5.1, B = Opus 5.5 et
C = Gemini Argon. « l. n » renvoie à la ligne n de la cellule.

**Critères gelés** (question, l. 191-200) : un élément est « commun » s'il est donné par au moins deux répondants avec la même
définition opérationnelle. Sinon il est « divergent ».

**Réserve** : la phrase « l'avis d'Argon est lu à côté » vise sans doute le répondant Argon séparé (question, l. 81-83). Par
prudence, j'indique quand un élément commun tient **sans C**. A et B sont de la même famille de modèles, ce qui affaiblit un accord
qui ne repose que sur eux deux.

---

## 1. Verdict

1. Les trois modèles concluent qu'**une question de course n'est jugeable qu'après l'étalonnage de ses instruments sur des témoins
   plantés**. Ces instruments sont l'analyseur ou les juges, la mémoire anti-redite et la vérification d'antériorité. Les trois
   concluent aussi que **le signal à 8 milliards de paramètres doit être établi** avant de demander « de meilleures sondes ».
2. Le texte converge sur un gabarit de champs vérifiés mécaniquement. Il reste **neuf divergences**. Les principales portent sur
   les données servies, le statut du couplage de l'axe 8, la vérification de « inédit », la règle d'arrêt et la première expérience.
3. Aucune cellule ne contient de recette ni de famille de déplacements de loi : **rien n'est retiré**. Aucune cellule n'établit de
   résultat. Le couplage, « décisif », « inédit » et le signal à 8 milliards restent non établis chez les trois.

---

## 2. Ce qui est commun (état final)

| # | Élément | A | B | C | Sans C |
|---|---|---|---|---|---|
| 1 | Étalonner l'analyseur ou les juges de la course **avant tout lancement**, sur des témoins plantés : fiches creuses, paraphrases de Q1–Q7, fiches de forme parfaite au contenu absurde, avantage faux | T3-A l. 68, 97 | T3-B l. 76-112, 283 | T3-C l. 124 | oui |
| 2 | Fausses alertes **par épisode, à tout instant**, sur trois jeux disjoints : calibrage, seuil, vérification | T3-A l. 27, 64 | T3-B l. 44, 216 | T3-C l. 14, 79 | oui |
| 3 | Contrôle par **consigne bénigne de longueur appariée** | T3-A l. 48, 62 | T3-B l. 52, 164 | T3-C l. 43, 79 | oui |
| 4 | Séparer **m1 (exécution) de m2 (lisibilité)** avant l'axe 1 | T3-A l. 88 | T3-B l. 258 | T3-C l. 117 | oui |
| 5 | **Aucune donnée de calibrage ou d'évaluation de G1 servie** ; partition tierce, intersection vide | T3-A l. 21, 39 | T2-B l. 180 | T3-C l. 12, 114 | oui |
| 6 | Mémoire anti-redite **étalonnée** sur des paraphrases plantées par une instance tierce et des fiches neuves sur les mêmes sources ; plongement nommé et figé | T3-A l. 16, 66 | T3-B l. 193-199 | T3-C l. 17 | oui |
| 7 | « Battre HELIOS » se mesure **contre la base (iii) exécutée sur notre banc** ; 0,38 n'est qu'un repère | T3-A l. 82 | T2-B l. 145-148 | T3-C l. 19 | oui |
| 8 | **Variance du seuil à 1 % propagée** (environ 3 dépassements sur 300 honnêtes, T2-B l. 78) | T3-A l. 26 | T2-B l. 78 | T3-C l. 21 | oui |
| 9 | Axe 4 : **loi jointe, multiplicité et taille d'effet minimale simulées** avant scellement ; témoin positif à effet connu | T3-A l. 29, 45 | T3-B l. 175-188 | T3-C l. 92 | oui |
| 10 | **Pas de pseudo-réplication** : randomisation par session, corrélation intra-classe | T3-A l. 22 | T3-B l. 116-123 | T3-C l. 31 | oui |
| 11 | Plan **2 × 2 grain des jetons × accumulation**, hors de G1 (idée de B au tour 2) | T3-A l. 64 | T2-B l. 39 | T3-C l. 37-40 | oui |
| 12 | Préalable « **rien de la consigne à la position lue** » ; l'organisme (ii) entre au duel s'il existe | T3-A l. 40, 62 | T3-B l. 159-171 | implicite (l. 95) | oui |
| 13 | Les axes « libres » de la lecture B1 **ne sont pas une vérité de terrain** ; occupants tirés de plusieurs documents ; vérification sans accès au dépôt | T3-A l. 23, 70 | T3-B l. 25, 134-147 | — | A + B |
| 14 | **Seuil unique s\* scellé**, issue « non jugeable par puissance » | T3-A l. 5 | autre règle (l. 124-128) | T3-C l. 28 | **non** |
| 15 | **Plancher au maximum de K directions aléatoires** | T3-A l. 19 | autre règle (l. 41) | T3-C l. 37 | **non** |
| 16 | Le **juge à pari apparié ne note pas le texte** d'une fiche | — | T2-B l. 108-112 | T3-C l. 20 | **non** |

Les trois tiennent « avantage décisif » et « inédit » pour **interprétatifs** (T1-A l. 15 ; T1-B l. 37 ; T1-C l. 71). Au sens gelé,
ils sont « non jugeables » tels que la question-mère les écrit.

---

## 3. Divergences

**D1 — Première expérience.**
- A : E6 (juges de la course), puis E3 (signal à 8 milliards), puis E7 et E5. E1 et E2 tiennent lieu de première course
  (T3-A l. 97).
- B : E1 en trois volets, avec E5 en parallèle. E2 et E6 attendent qu'E1 et E3 aient donné H_A (T3-B l. 283-287).
- C : un pré-pilote d'au plus 4 USD. Le verrou A porte sur le signal à 8 milliards ; le verrou B exige que les 15 fiches
  défectueuses sur 20 soient rejetées (T3-C l. 122-124).

**D2 — Forme de la question.**
- A : un noyau F1–F8 en texte unique ; E2 doit trancher entre texte unique et texte par axe (T1-A l. 115-143 ; T3-A l. 74).
- B : pas de texte, mais un noyau de neuf livrables et critères. La consigne de forme est lue comme une donnée (T3-B l. 32,
  263-281).
- C : le seul texte complet, d'environ 7 650 caractères, avec cinq modules et deux étages (T3-C l. 56-105).

**D3 — Données servies aux idéateurs.**
- A : le verdict d'E3 seulement, jamais les vecteurs. Les notations ne sont servies que sur des copies disjointes. Toute lecture sur
  P3 est circulaire (T3-A l. 39, 74). A nie que P3 contamine G1 (T3-A l. 50).
- B : aucune tranche ; seulement la condition d'intersection vide (T2-B l. 180).
- C : une tranche isolée « TEI-0 », où les fiches sont exécutées et évaluées sur D_val (T3-C l. 12, 63).

**D4 — Couplage angle ↔ hypothèse violée.**
- A : compté, pas noté, jusqu'à ce que E1 tranche (T3-A l. 74).
- B : testé seulement si l'effet détectable est d'au plus 0,35. Sinon, c'est « un choix de conception tranché par Lazar »
  (T3-B l. 126-130).
- C : obligatoire dès la deuxième génération (T3-C l. 69, 104), testé sur six micro-courses par cellule (T3-C l. 31).

**D5 — « Avantage décisif ».**
- A : une liste fermée et une clause, ce qu'A déclare être un simple contrôle de présence (T3-A l. 32, 93).
- B : ajoute un fait des pièces et un test de rejet des avantages réfutés (E1-b). La composante positive est déclarée invérifiable
  (T3-B l. 95-103).
- C : une ressource absente des pièces annule la fiche (T3-C l. 76).

**D6 — « Inédit ».**
- A : E7, au moins dix revendications tirées d'au moins trois sources. Un échec fait passer l'axe 7 en bloc à « à vérifier »
  (T3-A l. 70).
- B : environ cinq documents, avec les strates « dans » et « hors » du dossier. Un échec réduit « inédit » à « non réfuté par
  [procédure] à [date] », sans note (T3-B l. 132-154).
- C : une citation prise dans les 23 papiers et une distance de plongement, sans vérification ouverte (T3-C l. 82). Or B a écrit
  qu'un dossier fermé ne peut pas établir « non occupé » (T1-B l. 41-43).

**D7 — Signal à 8 milliards.**
- A : sur processeur, avec les vecteurs existants et les préalables p1 et p2 (T3-A l. 62).
- B : le même dispositif, mais il faut d'abord lever la contradiction S6 entre « aucun agent saboteur fabriqué » et « vecteurs
  cités ». Un échec ne réfute que les sondes figées actuelles (T3-B l. 156-173).
- C : trois tailles, dont un 70 milliards sous GO, stratifiées par le dommage. Au verrou A, un échec déclenche « immédiatement » la
  bascule (T3-C l. 43-46, 123). C'est la conclusion trop large que T2-A l. 24 reprochait à B.

**D8 — Arrêt de la boucle.**
- A : si E5 échoue, il ne reste qu'un compte (T3-A l. 66).
- B : une mesure consignée tant que l'association entre nouveauté et survie n'a pas donné H_A sur deux générations (T3-B l. 203).
- C : une règle fondée sur la survie, comparée au plancher de deux sous-courses (T3-C l. 18).

**D9 — Juges-modèles et mort de la course.**
- A : deux juges examinés par E6. La course meurt si E6 donne H_B, ou si deux générations passent sans fiche hors des huit fiches
  de référence (T3-A l. 68, 95).
- B : le juge ne garde que la cohérence entre champs (E1-c). La course est stérile si |R| = 0 ou si la vérification externe ne
  retient rien (T3-B l. 219-229, 280).
- C : seul l'analyseur décide à l'étage 1 (T3-C l. 20). Son critère de mort de la course, critiqué (T2-B l. 156 ; T2-A l. 87),
  **n'est pas réécrit** (T3-C l. 13).

---

## 4. Ce que le tour 2 a abattu ; ce que le tour 3 a sauvé ou concédé

| Cible | Critique (tour 2) | Réponse (tour 3) |
|---|---|---|
| A, E1 et E5 vrais par construction | T2-B l. 18-29 | Concédée : liste hors champs imposés, témoin neuf sur les mêmes pièces (T3-A l. 15-16) |
| A, « hors C1 » trivial ; famille nulle inversée | T2-B l. 31-51 | Transformée : huit fiches de référence ; la famille nulle contrôle les fausses alertes (T3-A l. 17, 20) |
| A et C, plancher non apparié à la sélection ; zones mortes | T2-B l. 41-45, 69-71 | Concédée : maximum sur K, s\* (T3-A l. 5, 19 ; T3-C l. 28, 37) |
| A, vecteurs de P3 servis | T2-C l. 17-19 | **Concédée en partie** : verdict seulement ; contamination de G1 **rejetée** (T3-A l. 39, 50) |
| B, E1 ne teste pas S3 ; surface prise pour un comparateur | T2-A l. 16, 30 ; T2-C l. 77-79 | Transformée : E1-b et E1-c, surface appariée (T3-B l. 24, 31, 95-112) |
| B, liste « libre » de B1 | T2-A l. 18 ; T2-C l. 66-71 | Concédée (T3-B l. 25, 59) |
| B, E2 sous-dimensionnée ; corrélation sur 2 ou 3 points | T2-C l. 87-93 | Concédée ; B corrige le calcul de C : environ 175 fiches par bras, et non 340 (T3-B l. 63-64) |
| B, conjonction de quatre seuils | T2-C l. 73-75 | **Asymétrie maintenue**, lot dimensionné (T3-B l. 60) |
| B, κ et prévalence | T2-A l. 36 | Concédée pour κ, **rejetée** pour les taux conditionnels (T3-B l. 37-38) |
| C, TED-0 sert à construire et à évaluer | T2-B l. 101-106 ; T2-A l. 61 | Concédée : TEI-0 disjointe (T3-C l. 12) |
| C, juge à mise appliqué à des fiches ; Lean avec `sorry` | T2-B l. 108-117 ; T2-A l. 73 | Concédée : deux étages, interdits et test de non-vacuité (T3-C l. 17, 20) |
| C, compteur lisant la carte des hypothèses | T2-B l. 119-122 ; T2-A l. 75 | Concédée : supprimé (T3-C l. 18) |
| C, 0,38 pris comme seuil ; 0,64 sans sa condition ; statuts ; 70 milliards ; budget | T2-B l. 145-154 ; T2-A l. 59, 77 | Concédée : deux générations coûtent jusqu'à 105,60 USD (T3-C l. 11, 19) |
| C, M3 et M4 non notables ; monotonie ; contrôle orthogonal ; analyse par protocole | T2-A l. 63, 69, 71 ; T2-B l. 133-164 | Concédée ou transformée (T3-C l. 13, 15, 16, 21) |
| A et C, 1 % par action | T2-A l. 67 : environ 26 % par épisode à 30 actions | Concédée par les trois (§ 2, élément 2) |

**Écartés selon les critères gelés** (par leurs auteurs au tour 3) :
- la tranche de T1-C l. 12, qui servait les honnêtes réservés, est **circulaire** ;
- le compteur de T1-C l. 124 lisait la carte des hypothèses, ce qui est interdit ;
- la « distance opérationnelle » (T1-C l. 31) est **non jugeable** (T2-A l. 73).

Aucune cellule ne demande de famille de déplacements. La mention de l'« omission d'un contrôle » (T1-C l. 122 ; T2-C l. 79) reprend
le glossaire servi.

**Restent ouverts** :
- la question de P3, entre A (T3-A l. 50) et C (T2-C l. 19) ;
- la conjonction de seuils de B ;
- le critère de mort de C ;
- l'étiquetage, par une instance tierce, des familles scellées « qui vérifient C_R » (T3-C l. 16, 49). Aucun mécanisme n'en garantit
  l'absence de fuite, ce que T2-B l. 141 demandait.

---

## 5. Recommandation pour la course

**Établi par les cellules** (la confiance indiquée est la mienne, sur la solidité de l'accord) :
1. **Ne rien lancer avant d'avoir étalonné les instruments de la course sur des témoins plantés** (§ 2, éléments 1 et 6). **0,85.**
2. **Inscrire dans le texte** les éléments 2, 3, 7, 8, 9 et 10 du § 2. **0,8.**
3. **Ne servir aucune donnée de calibrage ou d'évaluation de G1** (élément 5). **0,8.**
4. **Conditionner l'axe 1 à l'expérience sur le signal à 8 milliards** (élément 4). **0,75.**
5. **Ne pas noter « décisif » ni « inédit » tels quels.** **0,8.**

**Mon inférence** :
6. **Fondre E6 de A, E1 de B et le verrou B de C en un seul préenregistrement d'étalonnage.** Les coûts annoncés sont faibles :
   10 à 30 USD selon A (T3-A l. 97), « quelques dollars » selon B (T3-B l. 284), au plus 4 USD selon C (T3-C l. 122). **0,7.**
7. **Partir du texte v2 de C**, le seul complet, et y greffer quatre éléments : la règle de données de A, la vérification ouverte de
   B, le critère de mort de B et la table des écarts restreinte de B (T3-B l. 267). **0,55** ; le recoupement de conv-audit tranche.
8. **Garder hors du devis actuel les expériences à plusieurs courses.** Les coûts dérivés atteignent environ 158 USD
   (T1-B l. 274), 211 USD (T1-B l. 275) et 264 USD (T3-B l. 237). **0,8.**
9. **Lever la contradiction S6 par une lecture du registre, sans dépense**, avant l'expérience à 8 milliards. **0,7.**
10. **Compter un accord entre A et B seuls comme plus faible**, puisqu'ils sont de la même famille. **0,6.**

---

## 6. Questions pour Lazar (défaut appliqué sous 48 heures)

**Q1 — Étalonner avant d'écrire ou de lancer la question ?**
- Enjeu : une question notée par un instrument non examiné n'a pas d'issue falsifiable (T3-A l. 97).
- Options :
  - (a) un pré-pilote fondu de quelques dollars : sûr, mais il retarde la course ;
  - (b) une course v1 qui sert d'expérience sur sa propre forme : plus rapide, mais ses notes ne sont pas fiables ;
  - (c) un lancement tel quel : contraire à l'avis des trois modèles.
- Recommandation : (a), confiance 0,8. Défaut : (a), sous devis.

**Q2 — Quelles données servir aux idéateurs ?**
- Options :
  - (a) le verdict du test nul seulement, comme le veut A : sans fuite, mais pauvre ;
  - (b) une tranche TEI-0 avec exécution, comme le veut C : plus riche, mais il faut une partition tierce et une dépense ;
  - (c) rien.
- Recommandation : (a), confiance 0,65. Défaut : (a).

**Q3 — Le couplage de l'axe 8 est-il une règle de notation ?**
- Options :
  - (a) un compte jusqu'à ce qu'il soit testé, comme le veut A : prudent, mais le point 8 reste sans règle ;
  - (b) obligatoire dès la deuxième génération, comme le veut C : fidèle au point 8, mais il risque d'appeler des fiches creuses ;
  - (c) un choix de conception déclaré non testé, que tu tranches (le repli de B).
- Recommandation : (a), confiance 0,65. Défaut : (a).

**Q4 — Comment noter « inédit » ?**
- Options :
  - (a) une note provisoire, puis définitive après une vérification ouverte étalonnée, comme le veut B : solide, mais coûte des
    appels ;
  - (b) une citation prise dans les 23 papiers et une distance de plongement, comme le veut C : bon marché, mais elle ne dit que
    « non réfuté dans le dossier » ;
  - (c) « non réfuté par [procédure] à [date] », sans note.
- Recommandation : (c) jusqu'à la lecture de l'étalonnage, puis (a). Confiance 0,7. Défaut : (c).

**Q5 — Signal à 8 milliards : sur processeur, ou sur trois tailles ?**
- Options :
  - (a) sur processeur avec les vecteurs existants, après S6, comme le veulent A et B : gratuit, mais limité à la lisibilité ;
  - (b) sur 3, 8 et 70 milliards, stratifiés par le dommage, comme le veut C : sépare m1 de m2, mais demande un GO et un modèle de
    70 milliards dont la disponibilité est supposée (T3-C l. 11).
- Recommandation : (a), puis (b) sur devis si (a) est nul. Confiance 0,7. Défaut : (a).

**Q6 — Règle d'arrêt de la boucle.**
- Options :
  - (a) une mesure consignée seulement, comme le veulent A et B : sûre, mais sans arrêt automatique ;
  - (b) une règle fondée sur la survie, comparée au plancher de bruit, comme le veut C : automatique, mais non étalonnée.
- Recommandation : (a), confiance 0,75. Défaut : (a).
