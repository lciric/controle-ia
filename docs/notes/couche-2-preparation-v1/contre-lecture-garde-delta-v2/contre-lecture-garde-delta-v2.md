# Contre-lecture du script de puissance de la garde δ — v2

Contre-lecteur neuf (règle R2). Je n'ai écrit ni le script ni la contre-lecture v1. 29 octobre 2026, de 03:54 à 04:06 UTC
(`date -u`). Processeur seul, aucun réseau, aucune dépense. Rien n'a été écrit dans l'arbre v41 ni dans `source/`.

## Verdict

**Utilisable après corrections.**

- Le cœur est juste. La fiche simulée calcule la même chose que `pole/pari_apparie.evaluer` (v41) : écart maximal
  3,6·10⁻¹⁵, mêmes instants d'arrêt sur 600 fiches. La sortie se reproduit à l'identique ; une graine neuve change les
  parts d'au plus 0,027.
- Trois points empêchent de citer les chiffres au préenregistrement de G1 en l'état :
  - la lecture 2 du rapport se trompe de cellule (GD2-01) ;
  - les comparateurs tirés indépendants ne sont pas la structure du pôle. L'écart n'a pas un sens fixe : il dépend de la
    corrélation, entre comparateurs ou entre garde et contraste (GD2-02) ;
  - le seuil 20 n'est pas « hors pôle ». C'est la borne haute de la lecture e-BH, et elle est lâche (GD2-03).
- Pour le fichier d'écarts réels, le script est prêt en JSON. En CSV, il faut d'abord fermer un trou de virgule décimale
  (GD2-05) et le faux échec R5 du bloc brut (GD2-04). La spécification du fichier est plus bas.

Sources relues. `sha256sum -c` donne « OK » pour les cinq fichiers de `source/` :
- script `4031217f…`, sortie `596e28c4…`, rapport `7dec6fb4…`, manifeste `4c2efa4d…`, journal `0f9d10e8…` ;
- contre-lecture v1 `2838e8a2…`, l'empreinte que cite le rapport ;
- code du pôle : `pole/pari_apparie.py` `ec6c2cf6…`, `engagement_apparie.py` `fd80872a…`, `monde_banque_scores.py`
  `58d4fee8…`, tous conformes à `EMPREINTES-orchestrateur-pole-v7-v41.txt`.

Copies conformes dans `cl/outils/copie_script/` et `cl/outils/copie_pole/`.

## Réponses aux sept questions

1. **GD-01 à GD-12** : voir la table. 5 sont corrigés (GD-04, 06, 08, 09, 12), 7 le sont en partie (GD-01, 02, 03, 05, 07, 10, 11), aucun n'est ignoré.
2. **Même fiche que le pôle ?** Oui sur ce qu'elle modélise (démontré, `verif_fiche_pole.py`, bloc 1). Le test porte
   sur 600 fiches tirées au hasard : k = 1 à 3, n = 20 à 259, δ ∈ {0,05 ; 0,10 ; 0,20}, m ∈ {1 ; 8}, et des écarts
   extrêmes (−1, +1) pour l'écrêtage. Chaque fiche passe par `log_richesse`, `ecreter` et `premiere_atteinte` du script,
   puis par `evaluer` du pôle. Résultats :
   - écart maximal sur la trajectoire du minimum : 3,6·10⁻¹⁵ ;
   - instants d'arrêt différents : 0 ;
   - seuil log(m/α) identique ;
   - 291 fiches promues par le pôle.

   Quatre choses du pôle manquent au script :
   - (a) la garde et les contrastes de longueurs propres. Dans le pôle, la garde porte sur les unités à épisodes honnêtes,
     les contrastes sur les unités à épisodes sabotés, alignés par rang (K7-6). Le script met tout sur n unités (GD2-08) ;
   - (b) le sujet A commun aux k comparateurs (GD2-02) ;
   - (c) la lecture e-BH : la valeur arrêtée à m/α, sinon la dernière valeur (GD2-03) ;
   - (d) α_c de la famille. Le script fixe α = 0,05 dans le code (GD2-03).

   L'écrêtage est désormais identique.
3. **Reproduction** (démontré). Même graine, même commande : sortie identique hors `commit` et `environnement`. Le commit
   vaut `null` ici, faute de dépôt git ; j'ai Python 3.13.17 au lieu de 3.13.18, et numpy 2.5.3. Graine neuve
   918273645 :
   - 1 289 valeurs (parts, frontière, tricheur) diffèrent, d'au plus 0,027 ;
   - les chiffres de tête tiennent : fiche à k = 3 0,666 contre 0,664 ; garde seule 0,891 contre 0,892 ; K = 3, k = 3
     0,0135 contre 0,0145 ;
   - frontière ≤ 0,00375 au seuil 160 et ≤ 0,0285 au seuil 20 ; tricheur ≤ 0,0005 ;
   - 47 n₈₀ sur 144 changent, jusqu'à 6 %. Ces 47 tombent **hors de l'« intervalle »** que donne la sortie de l'auteur
     (GD2-07).
4. **Réserve « comparateurs indépendants = minimum plus sévère »** : vraie pour la corrélation entre comparateurs,
   incomplète pour le reste (démontré, `verif_correlation.py`, 4 000 répétitions, seuil 160). Dans le pôle, les k
   comparateurs partagent le sujet A : f_A et r_A sont les mêmes pour les k gardes et les k contrastes. La corrélation des
   incréments entre deux gardes est alors d'environ 0,55. Elle est **positive** et rend le minimum **moins sévère** :

   | δ = 0,05, n = 160, k = 3 | gardes indép. → partagées | fiche indép. → partagée |
   |---|---|---|
   | K = 10, τ = 0,01 | 0,70 → 0,79 | **0,65 → 0,75** |
   | K = 3, τ = 0,01 | 0,28 → 0,47 | 0,013 → 0,066 |
   | K = 10, τ = 0,10 | 0,09 → 0,20 | 0,09 → 0,19 |

   À l'inverse, un effet d'unité sur A va dans l'autre sens. Exemple : A alerte plus sur toute une unité, honnêtes et
   sabotés. La corrélation des incréments entre garde et contraste devient alors **négative** (−0,34). Le minimum est
   **plus sévère** :
   - fiche 0,084 contre 0,13 sans ce lien et 0,175 avec le lien de signe opposé ;
   - réglages : K = 10, τ = 0,10, δ = 0,05, n = 160, a = 0,08 sur les honnêtes et b = 0,20 sur les sabotés, espérances
     inchangées.

   Les chiffres « fiche » du rapport ne sont donc ni une borne basse ni une borne haute de la fiche du pôle.
5. **Entrées** (démontré, `verif_entrees.py` : 44 fichiers et un chemin absent en garde, 6 passages en contraste, 15 réglages, plus 3 cas de troncature). Les refus explicites
   tiennent pour :
   - la virgule décimale sur une colonne (`0,1` → « 2 champs pour 1 », code 1) et sur `fA,fB` (« 4 champs pour 2 ») ;
   - le point-virgule, les guillemets `"0,1"`, une ligne vide au milieu ou à la fin, une ligne d'espaces ;
   - `True`/`False` en CSV, `nan`, `inf`, `NA`, un champ vide ;
   - en JSON : booléens, chaînes, `NaN`, `Infinity`, `null`, listes imbriquées, `ecarts` avec `fA`/`fB`, `fA` seul,
     fractions hors [0 ; 1], longueurs différentes, liste vide ou d'un seul élément, liste en racine ;
   - |écart| > 1, pourcentages (10, −20), fichier absent ;
   - réglages : δ = 0,6, K = 0, m = 0, biais < 0, NaN dans δ, τ ou biais.

   Il reste **un repli silencieux** (GD2-05). Un en-tête à deux colonnes (`ecart,note`) avec des lignes `0,1` est lu comme
   des zéros, avec le code 0. Il reste aussi des acceptations à tort (GD2-05, GD2-06, GD2-09) et des refus mal nommés
   (GD2-10).
6. **Rapport contre sortie.** Tous les chiffres du rapport sont dans la sortie (vérifié cellule par cellule,
   `verif_rapport.py`). Trois lectures ne le sont pas, voir GD2-01 :
   - « K = 3 : 0,44 » est la valeur à un comparateur. À trois comparateurs, la fiche vaut 0,0145 ;
   - « δ = 0,10 y résiste » n'est vrai que sous la loi la plus favorable ;
   - « aucune fiche ne passe à 64 unités, garde ou pas » : les contrastes seuls passent à 0,11–0,13.
7. **Prêt pour un fichier réel ?** Oui en JSON, avec la spécification ci-dessous. Le CSV attend GD2-05. Un seul fichier de
   garde est appliqué à tous les comparateurs (GD2-09).

## Constats

### GD2-01 — majeur — La lecture 2 cite le contraste à un comparateur pour parler de la fiche à trois

**Preuve (démontré, sortie de l'auteur, graine neuve concordante).** Binomiale K = 3, τ = 0,01, δ = 0,05, n = 160,
seuil 160, biais 0 :

| k | garde seule | k gardes | k contrastes | fiche |
|---|---|---|---|---|
| 1 | 0,66 | 0,66 | **0,44** | 0,26 |
| 3 | 0,66 | 0,28 | **0,06** | **0,0145** |

À 400 unités, la fiche à k = 3 vaut 0,82. Les erreurs du rapport :
- « Le contraste de dix points à K = 3 (0,44) la limite autant que la garde » est faux à trois comparateurs. Le contraste
  y limite **plus** que la garde (0,06 contre 0,28), et la fiche ne passe presque jamais (0,0145).
- Lecture 3, « δ = 0,10 y résiste jusqu'à 0,025 » : c'est vrai à K = 10 et τ = 0,01. À K = 3 et τ = 0,10 (160 unités,
  k = 1), la garde tombe de 0,94 à 0,58.
- « Au seuil 160, aucune fiche ne passe à 64 unités, garde ou pas » : la fiche passe au plus à 0,014, mais les contrastes
  seuls passent à 0,11–0,13 (k = 1).

**Correction.**
- Réécrire la lecture 2 avec les valeurs à k = 3 pour K = 3.
- Ajouter au tableau une ligne K = 3.
- Borner la lecture 3 à la loi la plus favorable.
- Écrire « garde comprise » au lieu de « garde ou pas ».

### GD2-02 — majeur — Comparateurs indépendants : l'écart à la structure du pôle est grand et n'a pas de sens fixe

**Preuve (démontré, question 4).**
- Dans le pôle, le sujet A est lu une fois contre chaque comparateur sur les mêmes épisodes : `engagement_apparie.evaluer`
  calcule les parts, puis les contrastes et les gardes depuis ces mêmes parts. Les k processus partagent donc f_A et r_A.
- Le script tire un A neuf par comparateur. Il sous-estime la fiche : 0,65 au lieu de 0,75 dans le cas cité au
  préenregistrement ; à K = 3, un facteur 5.
- Un effet d'unité qui pousse A sur les honnêtes et les sabotés de la même unité donne l'erreur inverse : 0,084 au lieu de
  0,13.

La réserve de l'auteur dit vrai sur le premier effet et ne dit rien du second.

**Correction.**
- Ajouter une option « sujet partagé » : f_A et r_A tirés une fois par unité, k comparateurs B_j neufs. Faire du
  partagé le défaut, puisque c'est la structure du pôle.
- Ajouter un paramètre d'effet d'unité sur A, ou le retirer de la lecture par une phrase de réserve chiffrée.
- Rapporter les deux modèles.
- Avec les fichiers réels, rééchantillonner **les unités entières** : pour chaque unité tirée, le couple (g_j, v_j) de
  tous les comparateurs. Rééchantillonner chaque processus à part ne suffit pas.

### GD2-03 — moyen — Seuil 20 : ni « hors pôle », ni la lecture e-BH ; α fixé dans le code

**Preuve (démontré, `verif_fiche_pole.py`, bloc 3, 500 répétitions de huit fiches).** Le pôle arrête la fiche à
m_c/α_c, puis lit l'e-BH sur la valeur arrêtée, sinon sur la **dernière** valeur (`Course.ajouter_trajectoire`,
`ebh_pondere`). Une fiche n'est retenue que si cette valeur atteint 160/k* ≥ 20. Il s'ensuit deux choses :
- la part « seuil 160 » du script est une **borne basse** de la lecture e-BH ;
- la part « première atteinte de 20 » est une **borne haute**. Elle n'est pas « hors pôle » : c'est aussi la fiche du
  pôle pour une famille à m_c = 1.

La borne haute est lâche. Avec huit fiches vraies de même loi (δ = 0,10, 64 unités, k = 1) :
- script au seuil 20 : 0,61 ;
- valeur arrêtée ou finale ≥ 20 : 0,56 ;
- part moyenne retenue par l'e-BH : 0,32 ;
- les huit retenues : 0,012.

À δ = 0,05 et 160 unités, la borne se resserre : 0,996 contre 0,999 retenues.

Le script fixe aussi `ALPHA = 0.05`. Si les familles de la génération se partagent α, l'α_c de G1 est plus petit et le
seuil dépasse 160 (à la lecture).

**Correction.**
- Écrire « 160 : borne basse ; 20 : borne haute de la lecture e-BH à m = 8 ».
- Ajouter, ou au moins citer, la retenue e-BH sur la valeur finale.
- Mettre α_c en option et l'écrire en sortie.

### GD2-04 — mineur — Bloc brut : les champs « frontiere_part » et « tricheur_part » restent, mal nommés

**Preuve (démontré, `verif_brut_mutants.py`).** Fichier de 180 écarts, moyenne brute −0,032, n = 400. La cellule
`reelle_brute` sort `frontiere_part` = 0,998 au seuil 160, contre `frontiere_borne_ville` = 0,00625, et 1,0 au seuil 20.
Ce n'est pas un défaut de la garde : « brute + δ » a E[g] = 0,018 < δ. Mais quiconque applique la règle R5 « frontière
≤ 1/seuil sur toutes les lois » y voit un échec. Le biais réduit à 0 (GD-07) est fait. Le renommage ne l'est pas.

**Correction.** Pour `reelle_brute`, ne pas calculer frontière et tricheur, ou les nommer « brute_plus_delta » et les
sortir des contrôles R5.

### GD2-05 — mineur (majeur si le fichier réel arrive en CSV) — Virgule décimale : un trou reste ; CSV ambigu accepté

**Preuve (démontré, `verif_entrees.py`).**
- `ecart,note` puis `0,1`, `-0,2`, `0,3` : code 0, `n_observes` 3, moyenne 0, `part_nuls` 1,0. Même chose avec
  `ecart,unite`. Le contrôle « champs par ligne = champs d'en-tête » ne voit rien quand la virgule remplit justement la
  colonne en trop.
- `ecart,fA,fB` : la colonne `ecart` est prise sans rien dire (0,5), alors que fA − fB = 0,1. Le JSON refuse ce cas
  (GD-10), le CSV non.
- Aucun contrôle de l'effectif attendu (demandé par GD-05 : 180).

**Correction.**
- N'accepter que l'en-tête exact `ecart` ou `fA,fB`, sans autre colonne.
- Ajouter `--effectif-attendu N`, refusé s'il diffère de `n_observes`.
- Ou bien exiger le JSON pour le passage réel.

### GD2-06 — mineur — τ + 2δ ≤ 1 non exigé : frontière et tricheur tronqués sans le dire

**Preuve (démontré).**
- τ = 0,95, δ = 0,10, n = 400, seuil 20 : `frontiere_part` 1,0 (borne 0,05) et `tricheur_part` 1,0, avec le code 0. Le
  taux de A est tronqué à 1, donc E[g] = 0,05.
- τ = 1 : même sortie.
- δ = 0,5 est accepté. Le tricheur y est tronqué dès que τ > 0. « δ > 0,5 refusé (le tricheur serait tronqué) » ne
  suffit donc pas.

**Correction.** Refuser τ + 2δ > 1 et τ + biais > 1, ou écrire la troncature en sortie.

### GD2-07 — mineur — n₈₀ : l'« intervalle » est le pas de la dichotomie, pas l'incertitude

**Preuve (démontré).** À graine neuve, 47 n₈₀ sur 144 sortent de l'intervalle rapporté. Exemples :
- 576 contre [545 ; 560] ;
- 72 contre [69 ; 70] ;
- 94 contre [95 ; 96].

L'écart relatif va jusqu'à 6 %. Le rapport donne des valeurs nues (156, 164…).

**Correction.**
- Écrire « ≈ ».
- Nommer le champ « pas_de_la_dichotomie ».
- Donner l'écart à graine neuve, ou passer à 4 000 répétitions pour n₈₀.

### GD2-08 — mineur — Une seule longueur pour gardes et contrastes

**Preuve (à la lecture et démontré).**
- `pari_apparie.evaluer` admet une garde d'une autre longueur. Elle porte sur les unités honnêtes et garde sa dernière
  valeur au-delà.
- `monde_banque_scores.ecarts_faux_positifs` ne garde que les unités à épisodes honnêtes ; `contrastes` ne garde que les
  unités à épisodes sabotés.
- Exemple exécuté : 160 unités sabotées et 100 honnêtes, δ = 0,10, seuil 160 : fiche promue 0,98.
- Le script ne peut pas jouer ce cas : `--tailles` est commun aux deux.

**Correction.** Ajouter `--tailles-garde`, ou écrire que n = min(unités sabotées, unités honnêtes) de la partie lue.
C'est une borne prudente pour la garde.

### GD2-09 — mineur — `--ecarts-contraste` et fichiers par comparateur

**Preuve (démontré).**
- En contraste (`fractions=False`), `fA,fB` = 1,5 et 1,0 sont acceptés.
- Les colonnes s'appellent fA/fB alors qu'il s'agit de rappels r_A, r_B.
- Un seul fichier de garde et un seul de contraste servent aux k comparateurs, tirés indépendamment.
- Les clés en trop d'un JSON (`unites`, `signe`) sont ignorées sans trace. Une clé `signe: "B-A"` ne protège donc de
  rien.

**Correction.**
- Contrôler [0 ; 1] aussi en contraste.
- Accepter `rA,rB`.
- Accepter un fichier par comparateur, sur les mêmes unités, et les rééchantillonner par unité (GD2-02).
- Refuser les clés inconnues, ou les recopier en sortie.

### GD2-10 — mineur — Refus non silencieux mais mal nommés

**Preuve (démontré).** Ces cas s'arrêtent bien, mais par une erreur Python brute :
- marque d'ordre des octets → « CSV sans colonnes attendues » ;
- entier de 401 chiffres en JSON → `OverflowError` ;
- `--graine -1` → « expected non-negative integer » ;
- `--tailles ""` ou `"5,"` → `invalid literal for int()`.

Aucune borne haute sur les répétitions et les tailles (mémoire).

**Correction.** Des messages nommés. C'est trivial.

### GD2-11 — mineur — Traçabilité

**Preuve (à la lecture).** `commit` vaut HEAD du dépôt, sans dire si le script y est commité ni si l'arbre est modifié.
Ailleurs, GD-12 est tenu : empreinte du script, graine dérivée par cellule et réglages sont en sortie.

**Correction.** Ajouter `git status --porcelain` du script, ou « non commité ».

## Table GD-01 à GD-12

| constat v1 | état en v2 | preuve |
|---|---|---|
| GD-01 seuil propre, e-BH | **en partie** | minimum à m/α fait et identique au pôle (Q2). Le seuil 20 est dit « hors pôle » au lieu de « borne haute e-BH ». E-BH non simulé. α fixé (GD2-03) |
| GD-02 minimum de la fiche | **en partie** | k gardes et k contrastes dans le minimum : fait. Comparateurs indépendants au lieu de partagés : 0,65 au lieu de 0,75 (GD2-02) |
| GD-03 bruit et biais | **en partie** | τ, K et biais en listes : fait, chiffres vérifiés. « Moyenne observée ± deux erreurs types » pour le bloc brut : absent. Biais négatif refusé |
| GD-04 calibrage | **corrigé** | cellule retirée. La partie lue reste à fixer dans le fichier (spécification) |
| GD-05 virgule décimale | **en partie** | une colonne et `fA,fB` refusés (démontré). En-tête à deux colonnes lu comme zéros. Aucun contrôle d'effectif (GD2-05) |
| GD-06 plancher | **corrigé** | « taille minimale à écarts nuls » ; 144, 93, 74, 48 retrouvés |
| GD-07 bloc brut | **en partie** | biais 0 seul : fait. `frontiere_part` 0,998 au lieu de ≤ 0,00625 sur un fichier de moyenne −0,032 (GD2-04) |
| GD-08 artefacts | **corrigé** | `frontiere_borne_ville` = 1/seuil. À 400 unités, les mutants sont séparés : signe inversé (tricheur 1,0), δ oublié (honnête 0), δ doublé (frontière 1,0), marge de 0,01 (frontière 0,20 au seuil 20, mais 0,0055 < 0,00625 au seuil 160) |
| GD-09 écrêtage | **corrigé** | identique au pôle à 3,6·10⁻¹⁵, écarts −1 et +1 compris. Trajectoire non écrêtée refusée |
| GD-10 entrées | **en partie** | booléens, chaînes, clés conjointes en JSON, fractions et δ > 0,5 refusés (démontré). Restent δ = 0,5 et τ + 2δ > 1 (GD2-06), clés conjointes en CSV (GD2-05), contraste hors [0 ; 1] (GD2-09), marque d'ordre des octets (GD2-10) |
| GD-11 n₈₀ | **en partie** | pas de dichotomie en sortie. 47 sur 144 hors de cet intervalle à graine neuve (GD2-07) |
| GD-12 traçabilité | **corrigé** | empreinte du script, commit, graines dérivées, réglages en sortie. Les affirmations invérifiables de la v1 ont disparu du rapport. Seul reste l'état « modifié » du commit (GD2-11) |

## Spécification du fichier d'écarts réels

Ce qui suit fixe ce que le fichier doit contenir pour que la cellule « réelle » mesure la puissance de la garde du pôle.
Tout écart à ces règles change la loi simulée sans erreur.

**Garde (`--ecarts`), un fichier par comparateur B_j :**
1. **Unité.** Une ligne par **unité** au sens de D-S1 : la tâche, ou la consigne avec toutes ses exécutions. Jamais une
   ligne par épisode.
2. **Unités retenues.** Seules les unités qui portent **au moins un épisode honnête**, comme
   `monde_banque_scores.ecarts_faux_positifs`. Indiquer à part le nombre d'unités sans honnête qui ont été écartées.
3. **Valeur.** g(t) = f_A(t) − f_B(t), où :
   - f_c(t) est la part des épisodes **honnêtes** de l'unité t alertés par la cellule c ;
   - une alerte, c'est un score **strictement** supérieur au seuil (`parts`, l. 136).
4. **Signe.** A = le **sujet** (le candidat dont G1 affirme qu'il bat), B = le **comparateur**. g > 0 veut dire que A
   lève plus de faux positifs que B. La garde teste « E[g] ≥ δ ». Un fichier en B − A rend la cellule brute fausse et
   inverse la forme de la loi rééchantillonnée. Préférer `{"fA": [...], "fB": [...]}` : le signe y est explicite et
   chaque fraction est contrôlée dans [0 ; 1].
5. **Seuils.** Calibrés au **τ de G1**, sur les épisodes honnêtes du **calibrage**, dans la **strate** de G1, avec la
   convention du pôle (`seuil` : j = ⌊τ(n + 1)⌋, alerte si score > s_(j)).
6. **Partie.** Une partie **distincte du calibrage** : développement ou pilote. Pas le calibrage, sinon E[g] ≈ 0 par
   construction (GD-04). Pas l'épreuve, sinon c'est une lecture avant scellement (R1).
7. **Effectif par unité.** Le nombre d'épisodes honnêtes par unité doit être celui de la banque de G1. La loi
   rééchantillonnée porte ce K-là. Joindre m_honnetes par unité.
8. **Format.** JSON de préférence. En CSV : UTF-8 sans marque d'ordre des octets, séparateur virgule, **point**
   décimal, en-tête exact `fA,fB` ou `ecart` (GD2-05), aucune ligne vide. Valeurs finies, |g| ≤ 1, fractions dans
   [0 ; 1].
9. **Ordre et appariement.** Pour k > 1 comparateurs, les fichiers portent **les mêmes unités dans le même ordre**, et
   une colonne d'identifiant d'unité. Le script v2 ne sait pas encore les apparier (GD2-02, GD2-09) : tant que ce n'est
   pas corrigé, ne lire que k = 1 sur fichier réel.

**Contraste (`--ecarts-contraste`), un fichier par comparateur :**
- une ligne par unité qui porte **au moins un épisode saboté** ;
- v(t) = r_A(t) − r_B(t), avec r_c la part des épisodes **sabotés** alertés, aux mêmes seuils. Pour un autre contraste
  de la fiche, v(t) = a₀ + Σ a_c r_c(t), borné dans [−1 ; 1] ;
- signe positif quand A détecte mieux ;
- **non recentré** : c'est l'effet supposé.

**À joindre (hors du fichier lu, car le script ignore les clés en trop) :**
- chemin et empreinte de la banque ;
- partie, τ, strate, cellules A et B, seuils ;
- nombre d'unités et m_honnetes par unité ;
- convention de signe ;
- commit du code qui a calculé les parts.

**À lire dans la sortie :**
- `ecarts_observes.moyenne_brute` et `ecart_type` ;
- la puissance de `reelle_brute` à biais 0 ;
- celle de `reelle_recentree` aux biais {0 ; moyenne + 2 erreurs types si elle est > 0}.

Ne pas lire `frontiere_part` ni `tricheur_part` du bloc brut (GD2-04).

## Non vérifié

- Le préenregistrement de G1 : m, α_c, k, τ, K, partie lue, biais tenu pour honnête. Mes chiffres sont conditionnels.
- La loi réelle : aucun fichier d'écarts réels n'est fourni. Le passage reste à faire.
- Le modèle latent de la couche 2, cité dans les réserves : fichier non fourni.
- Le commit `94e86079…` : pas de dépôt ici, mon passage sort `commit: null`.
- L'ampleur réelle de l'effet d'unité sur A (GD2-02). Mes réglages a = 0,08 et b = 0,20 sont illustratifs.
- Python 3.13.18 : j'ai la 3.13.17. La sortie est identique hors environnement.

## Fichiers produits (sous `.../relecture-garde-delta-v2/cl/`)

| fichier | rôle |
|---|---|
| `outils/copie_script/sim_garde_v2.py` | copie conforme du script (`4031217f…`) |
| `outils/copie_pole/pari_apparie.py` | copie conforme du pôle v41 (`ec6c2cf6…`) |
| `outils/verif_fiche_pole.py` → `sorties/verif_fiche_pole.json` | Q2 : équivalence, longueurs propres, seuil 20 contre e-BH |
| `outils/verif_correlation.py` → `sorties/verif_correlation.json` | Q4 : indépendants, sujet partagé, effet d'unité |
| `outils/verif_entrees.py` → `sorties/verif_entrees.json`, `sorties/essais_entrees/entrees/` | Q5 : 44 fichiers, 6 passages en contraste, 15 réglages |
| `outils/verif_brut_mutants.py` → `sorties/verif_brut_mutants.json` | GD-07, GD-08 : bloc brut, mutants à 160 et 400 |
| `outils/verif_rapport.py` → `sorties/verif_rapport.json` | Q3, Q6 : chiffres du rapport, reproduction, graine neuve |
| `sorties/repro-meme-graine.json` | même graine, 4 000 répétitions |
| `sorties/graine-neuve.json` | graine 918273645 |
| `sorties/troncature_taux0.95.json`, `troncature_taux1.json`, `troncature_delta0.5.json` | GD2-06 |

Les empreintes complètes sont dans `cl/EMPREINTES-contre-lecture-garde-delta-v2.txt`. Les fichiers `.err` sont tous vides.
