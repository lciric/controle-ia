# Contre-lecture du script de puissance de la garde δ — v1

Contre-lecteur neuf (règle R2), sans part à l'écriture du script. 29 octobre 2026, de 02:49 à 03:01 UTC (`date -u`).
Processeur seul, aucun réseau, aucune dépense. Rien n'a été écrit dans l'arbre v40 ni dans `source/`.

## Verdict

**Utilisable après corrections.**
Le script calcule la bonne statistique : il est identique à `pole/pari_apparie.trajectoire_log_garde` (v40) sur des
fractions réelles (écart ≤ 4·10⁻¹⁵). Il se reproduit à l'identique, et une graine neuve donne les mêmes chiffres.
Les planchers 93, 144, 48 et 74 sont exacts. Deux choses manquent avant le passage sur le fichier réel et avant de
citer les chiffres au préenregistrement de G1 : corriger la lecture des fichiers CSV (GD-05) et l'écrêtage (GD-09). La
lecture et les options du rapport ne tiennent pas en l'état (GD-01 à GD-04). Elles supposent un seuil de la garde, un
bruit et un lieu de lecture qui ne sont pas ceux du code du pôle, ou qui restent à établir.

Sources relues, empreintes vérifiées (`sha256sum -c`, toutes « OK ») : script `37c3dc7a…`, sortie `1cbf70f6…`, rapport
`1c4fc53f…`, manifeste `fcd2c003…`, journal vide `e3b0c442…`. Code du pôle : `pole/pari_apparie.py` `56bc8e03…` et
`pole/cycle.py` `798f0390…`. Les deux concordent avec `EMPREINTES-orchestrateur-pole-v7-v40.txt`. Je les ai copiés
dans `cl/outils/copie_pole/` pour les exécuter sans toucher l'arbre v40.

## Réponses aux sept questions

1. **Même garde que le pôle ?** Oui sur la statistique (démontré) : même Λ = {0,1 ; 0,3 ; 0,6 ; 0,9}, même moyenne
   sur Λ, même v = δ − g, test unilatéral contre « E[g] ≥ δ », franchissement par « ≥ log(seuil) » des deux côtés. Sur
   1 600 trajectoires binomiales (τ = 0,01 et 0,10), on trouve un écart maximal de 3,6·10⁻¹⁵ et aucun instant de
   franchissement différent. Il y a trois écarts :
   - l'écrêtage, absent du script (GD-09) ;
   - les booléens, acceptés par le script et refusés par le pôle (GD-10) ;
   - le seuil : le pôle n'a pas de seuil propre de garde, car la garde entre dans le minimum de la fiche (GD-01, GD-02).
   Pour les ex æquo, les deux codes comparent par « ≥ » au seuil et traitent pareil les atomes g = 0. Pour les non
   finis, NaN et ±∞ sont refusés des deux côtés (démontré).
2. **Reproduction.** Même graine, même commande : sortie identique hors `environnement` (démontré, Python 3.13.17 au
   lieu de 3.13.18, numpy 2.5.3). Graine neuve 918273645 : mêmes chiffres à ±0,02 près (honnête δ = 0,05, n = 93 :
   0,464 contre 0,459 ; n₈₀ identiques, sauf 49 contre 50 en gaussienne). Le plancher, calculé en fractions exactes,
   est le plus petit n tel que la moyenne sur Λ de (1 + λδ)ⁿ ≥ seuil. Il donne **93, 144, 48, 74**, comme le script.
   La richesse vaut 19,52 à 92 unités et 20,29 à 93. Avec λ = 0,9 seul, il faudrait 100, 147, 51 et 75 unités.
3. **Recentrage.** Il est correct pour ce qu'il vise : la cellule honnête a E[g] = 0, et la cellule frontière, centrée
   puis décalée de δ, a E[g] = δ exactement sous la loi empirique. Le nul est donc bien à la frontière (démontré :
   moyennes tirées 0,0000 et 0,0500). C'est un modèle de translation : la variance ne change pas avec le biais, alors
   qu'en binomiale elle passe de 0,045 à 0,081 à la frontière. La validité n'en dépend pas (l'inégalité de Ville tient
   pour toute loi), mais la puissance aux biais intermédiaires si. La cellule « brute » sert à lire la puissance si le
   candidat portait le biais observé. Seule sa ligne « honnête » a ce sens : ses lignes « frontière » et « tricheur »
   ne sont pas à la frontière (GD-07).
4. **Artefacts de la règle R5.** Frontière : 0 à 0,0125 au seuil 20, au plus 0,0005 au seuil 160. C'est sous les bornes
   de Ville, 1/20 et 1/160 (la borne au seuil 160 est 0,00625, pas α : GD-08). Tricheur : 0 partout (démontré). Le
   tricheur est le bon artefact contre une **inversion de signe** : le mutant « signe inversé » le certifie dans 100 %
   des cas à 960 unités. Mais tricheur et frontière ne séparent rien à 64 unités. J'ai ajouté des mutants (GD-08). La
   cellule honnête attrape « δ oublié ». La frontière attrape « δ doublé » et « marge de 0,01 en trop », mais seulement
   à 960 unités (0,88 et 0,69).
5. **Entrées.** Les refus explicites tiennent pour NaN, ±∞, null, un JSON vide, une liste vide, un seul écart, des
   longueurs fA/fB différentes, |écart| > 1, un CSV vide ou réduit à l'en-tête, une taille ≤ 0, δ hors ]0 ; 1[, m < 1
   et moins de 100 répétitions. Il y a **un repli silencieux grave** : un CSV à virgule décimale est lu comme des zéros
   (GD-05). Plusieurs replis silencieux sont mineurs (GD-09, GD-10).
6. **Rapport contre sortie.** Tous les chiffres du rapport sont dans la sortie (vérifié cellule par cellule). Quatre
   affirmations ne sont pas soutenues :
   - « aucune loi réelle ne le changera » (GD-06) ;
   - « le bruit réel compte peu » (GD-03) ;
   - « la garde est un test (m = 1) » (GD-01) ;
   - « les unités existent déjà dans le calibrage » comme lieu de lecture de la garde (GD-04).
   Le résumé transmis au contre-lecteur dit « à 160 unités et plus, 1,00 partout ». Ce n'est pas dans le rapport, et
   c'est faux au seuil 160 pour δ = 0,05 (0,90 en binomiale, 0,99 en gaussienne).
7. **Options.** Voir la dernière section : (c) est soutenue ; (a) et (b) ne le sont que sous des hypothèses non
   établies.

## Constats

### GD-01 — majeur — La garde n'a pas de seuil propre dans le pôle : la dichotomie « m = 1 ou m = 8 » est fausse
**Preuve (démontré, `outils/verif_equivalence.py`, bloc 4).**
- Dans `pari_apparie.evaluer`, la garde entre dans le **minimum** de la fiche. Ce minimum s'arrête au premier passage
  de log(m/α), où m est celui de la fiche (`seuil = math.log(m / alpha)`, commun aux contrastes et aux gardes).
- Avec des contrastes très favorables et g = 0 sur 64 unités, δ = 0,10 : m = 1 donne une fiche promue à l'unité 48 ;
  m = 8 donne une fiche **non promue**, garde finale 74,7 < 160.
- L'e-BH du pôle (`cycle.appliquer_multiplicite`, exécuté) retient une fiche dont l'e-valeur est ≥ m/(α·k*). Huit
  fiches identiques à 74,7 sont **toutes retenues** (k* = 8, seuil effectif 20). Une seule fiche à 74,7 ne l'est
  **pas** (seuil 160).

**Conséquence.** Le seuil 20 n'est pas « la garde comme un test ». C'est le cas le plus favorable de l'e-BH à huit
critères, quand les huit sont retenus. Le seuil 160 est le cas le plus défavorable, quand un seul l'est. Si G1 lit
huit critères en e-BH, l'option (a) a une puissance comprise entre 0,002 et 1,00 selon le nombre de critères vrais.
Ce n'est pas « 1,00 ».

**Correction.** Le rapport doit dire que les seuils 20 et 160 encadrent la lecture e-BH. Il faut soit simuler la
retenue e-BH en fonction de k*, soit fixer au préenregistrement que G1 est lue avec m = 1 si c'est l'intention.

### GD-02 — majeur — La puissance de la garde seule n'est pas la puissance de la fiche
**Preuve (démontré, `outils/verif_gardes_multiples.py`).**
- Le pôle prend le minimum des contrastes **et** d'une garde par comparateur (K9-9, `engagement_apparie.evaluer`).
  Une fiche de G1 qui doit battre plusieurs bases porte donc plusieurs gardes.
- Pour δ = 0,05, 160 unités, seuil 160, binomiale de τ = 0,01 : une garde donne 0,90, deux gardes 0,80, trois gardes
  0,71 (gardes indépendantes, contrastes non limitants).
- Le script mesure aussi le premier franchissement d'une garde seule. Il ne mesure pas l'instant où le minimum franchit,
  ni la valeur finale lue par l'e-BH quand k* > 1.

**Correction.** Simuler le minimum, avec le nombre de gardes prévu par G1 et des contrastes plausibles, ou au moins
écrire que les chiffres sont des bornes hautes.

### GD-03 — majeur — « Le bruit réel compte peu » n'est vrai que pour τ = 0,01 et K = 10 ; la puissance s'effondre avec un petit biais
**Preuve (démontré, `outils/verif_sensibilite.py`, bloc A, 4 000 répétitions).** Puissance du candidat honnête :

| loi | δ = 0,10, n = 64, seuil 20 | δ = 0,05, n = 160, seuil 20 / 160 |
|---|---|---|
| binomiale K = 10, τ = 0,01 (script) | 1,00 | 1,00 / 0,89 |
| K = 10, τ = 0,05 | 0,97 | 0,99 / 0,58 |
| K = 10, τ = 0,10 | 0,89 | 0,93 / 0,43 |
| K = 10, τ = 0,20 | 0,76 | 0,77 / 0,33 |
| K = 3, τ = 0,10 | 0,59 | 0,54 / 0,20 |

Avec un biais réel modeste et τ = 0,01, la puissance chute :
- (a) avec E[g] = δ/4 = 0,025 : 0,54 ;
- (b) avec E[g] = 0,0125 : 0,95 au seuil 20 et 0,03 au seuil 160.

La garde est donc très sensible au point de fonctionnement τ de G1, au nombre d'épisodes honnêtes par unité et au biais
vrai du candidat. Rien de cela n'est fixé par le passage synthétique.

Dans le pôle, f est la part des **épisodes honnêtes de l'unité** alertés (`monde_banque_scores.parts`, l. 136). Le
nombre d'épisodes par unité n'est pas forcément K = 10 (à la lecture).

**Correction.**
- Ajouter au script une grille de E[g] (0, δ/4, δ/2, 3δ/4) et le τ de G1.
- Rapporter la puissance du bloc brut à la moyenne observée ± deux erreurs types.
- Retirer « le bruit réel compte peu ».

### GD-04 — majeur — Option (b) « garde lue sur le calibrage » : contraire au code et circulaire
**Preuve (à la lecture).**
- Le code lit la garde sur **la même partie** que les contrastes. `engagement_apparie.evaluer`, l. 167 à 178 :
  `parts = monde.parts(..., engagement["partie"], ...)`, puis `monde.ecarts_faux_positifs(parts, a, b, ordre)`.
  `ecarts_faux_positifs` ne garde que les unités qui portent des épisodes honnêtes.
- Les seuils des cellules sont calibrés au taux τ **sur les honnêtes du calibrage** (`monde_banque_scores.seuil`,
  l. 103 à 118). Sur le calibrage, f_A ≈ f_B ≈ τ par construction, donc E[g] ≈ 0 par construction. Une garde lue là
  certifierait sans pouvoir voir un écart hors échantillon.
- La fraîcheur des unités (K9-1) s'y oppose aussi.

**Correction.** Retirer « ou sur tout le calibrage, 960 » de l'option (b). Si (b) est gardée, nommer la partie fraîche
qui porte au moins 160 unités honnêtes et compter ces unités. Le n du script doit être le nombre d'unités **à
épisodes honnêtes** de la partie lue, pas le nombre d'unités de l'épreuve.

### GD-05 — majeur — Un CSV à virgule décimale est lu silencieusement comme des zéros
**Preuve (démontré, `outils/verif_entrees.py`, cas `virgule_decimale.csv`).**
- Le fichier contient `ecart` puis `0,1`, `-0,2`, `0,3`, `0,1`. Le script finit avec le code 0, `n_observes` = 4,
  moyenne 0 et quantiles tous à 0.
- `csv.DictReader` coupe à la virgule et range le reste sous la clé `None`, que le script ignore.
- Sur le fichier réel, cela donnerait g = 0 partout, donc la puissance maximale. Le risque est réel dans un dépôt
  francophone.

**Correction.** Refuser toute ligne qui porte une clé `None` ou un champ manquant (`restkey`/`restval` ou contrôle
explicite). Refuser une virgule dans une valeur. Ou n'accepter que le JSON pour le passage réel. Vérifier `n_observes`
contre l'effectif attendu (180).

### GD-06 — mineur — Le « plancher structurel » n'est pas un plancher
**Preuve (démontré, bloc B).** Le plancher suppose g = 0 partout. Des écarts négatifs (A a moins de faux positifs que
B) font monter la richesse plus vite. Avec E[g] = 0, pour δ = 0,05 et 64 unités, on mesure une certification au
seuil 20 dans :
- 0,085 des suites pour g = ±0,3 ;
- 0,074 des suites en binomiale de τ = 0,20 ;
- dès l'**unité 11** pour g = ±0,5.

La sortie de l'auteur le montre déjà : à 93 unités, la médiane de certification est de 88 à 90 unités, sous le
plancher.

« Ce n'est pas un résultat de bruit [...] aucune loi réelle ne le changera » est donc faux. La conclusion (c) tient
pourtant : la puissance reste < 0,1 sur toutes les lois essayées.

**Correction.** Écrire « plancher sans bruit ; le bruit l'abaisse rarement et d'un peu ».

### GD-07 — mineur — Les cellules « frontière » et « tricheur » du bloc brut sont mal nommées
**Preuve (démontré).** Pour un fichier de moyenne brute −0,015, la « frontière » brute a E[g] = 0,035 et elle est
certifiée dans **1,00** des suites à 960 unités. Quiconque applique le contrôle de la règle R5 à ce bloc conclut à un
artefact raté.

**Correction.** Dans le bloc brut, ne garder que le biais 0. Sinon, renommer en « brute + δ » et exclure ce bloc des
contrôles R5.

### GD-08 — mineur — Critère des artefacts et pouvoir séparateur
**Preuve (démontré, bloc C).**
- Le rapport compare la frontière à α pour les deux seuils. La borne de Ville est 1/seuil, soit 0,00625 au seuil 160.
  Les valeurs observées la respectent.
- À 64 unités, les trois cellules ne séparent pas la garde correcte du mutant « signe inversé » pour δ = 0,05 (tricheur
  0,02), ni du mutant « marge de 0,01 en trop ».
- À 960 unités, elles séparent les quatre mutants : signe inversé, δ oublié, δ doublé, marge en trop.

**Correction.** Comparer la frontière à 1/seuil. Garder toujours une taille longue (960) dans les cellules
d'artefacts. Écrire que la cellule honnête est le cas sain et que le tricheur vise l'inversion de signe.

### GD-09 — mineur — Écrêtage absent : petit écart au pôle et NaN silencieux
**Preuve (démontré).**
- Le pôle calcule `max(-1, min(1, δ - g))`, le script non.
- Sur des fractions, seules les unités avec g < δ − 1 (en pratique g = −1) diffèrent. Le script est alors plus
  favorable : log richesse 2,99 contre 2,87 après six unités à g = −1.
- Si g > 1 + 1/0,9 − δ, ce qui arrive après recentrage d'un fichier biaisé (moyenne −0,8) plus le biais, `log1p`
  rend NaN. Le pôle, lui, écrête. Les cellules sortent alors une puissance 0 sans refus, avec un simple
  `RuntimeWarning` sur la sortie d'erreur.

**Correction.** `np.clip(delta - g, -1, 1)` comme le pôle, et refus explicite de tout NaN dans `lw`.

### GD-10 — mineur — Entrées acceptées ou tronquées sans le dire
**Preuve (démontré).**
- En JSON, les booléens (`true` vaut 1) et les chaînes (`"0.1"`) sont acceptés ; le pôle refuse les booléens.
- Quand `ecarts` et `fA`/`fB` sont présents ensemble, le script prend `ecarts` sans le dire.
- `fA`/`fB` hors de [0 ; 1] sont acceptés (1,5 − 1,0).
- Une ligne vide d'un CSV est sautée.
- δ = 0,6 : le tricheur annoncé à 1,2 est tiré à 0,99 (troncature).
- K = 0 est refusé avec un message trompeur (« écart non fini dans la trajectoire »).
- Un CSV avec marque d'ordre des octets (BOM) est refusé par un message qui ne dit pas pourquoi.
- Aucune borne haute sur les tailles : la mémoire vaut répétitions × n × 4 × 8 octets (à la lecture).

**Correction.** Refus nommés, contrôle de type, fA et fB dans [0 ; 1], δ < 0,5 ou troncature consignée.

### GD-11 — mineur — n₈₀ approchés
**Preuve (à la lecture et démontré).** La recherche de n₈₀ utilise 1 000 répétitions, une dichotomie arrêtée à
bas/32 près (± 2 unités entre 64 et 128) et des graines indépendantes par n. La graine neuve donne 49 au lieu de 50
en gaussienne.

**Correction.** Écrire « ≈ 102 » et donner l'intervalle de la dichotomie.

### GD-12 — mineur — Traçabilité
**Preuve (à la lecture).**
- La sortie ne porte ni l'empreinte du script, ni le commit, ni les graines dérivées. Le manifeste est écrit à la main
  (règles R6 et R9).
- Plusieurs affirmations sont invérifiables ici :
  - « binomiale = loi de `garde(...)` de la couche 2 » (fichier non fourni) ;
  - σ = 0,028 lu dans le pilote complémentaire ;
  - « D-S la donnait déjà à 0,10 » ;
  - le commit `0147788b…` ;
  - la réserve R4 de la v40 (≈ 1 % à 120 unités).

**Correction.** Faire écrire au script son empreinte et ses réglages dans la sortie. Citer chemin et empreinte pour σ
et pour la loi de la couche 2.

## Les options (a), (b), (c) : ce que les chiffres soutiennent (sans trancher)

- **(c) δ = 0,05 à 64 unités, à écarter.** Soutenue : la puissance est 0 en synthétique et ≤ 0,085 sur toutes les lois
  essayées. Le motif doit être corrigé (GD-06).
- **(a) δ = 0,10, seuil 20, 64 unités.** La puissance de 1,00 suppose quatre choses à la fois : m = 1 ou huit critères
  tous retenus (GD-01), une seule garde (GD-02), τ = 0,01 et K = 10, et E[g] = 0 (GD-03). Si l'une manque, la
  puissance tombe :
  - 0,002 au seuil 160 ;
  - 0,89 à τ = 0,10 ;
  - 0,59 à K = 3 ;
  - 0,54 si E[g] = 0,025.
- **(b) δ = 0,05, ≥ 160 unités.** On obtient 1,00 au seuil 20 sous les mêmes hypothèses. Le reste est plus faible :
  - 0,90 au seuil 160 ;
  - 0,71 avec trois gardes ;
  - 0,58 à τ = 0,05 ;
  - 0,03 au seuil 160 si E[g] = 0,0125.
  Lire la garde sur le calibrage est exclu (GD-04).

**Ce qui manque pour trancher :**
- le τ de G1 ;
- le nombre d'unités **à épisodes honnêtes** de la partie lue, et d'épisodes honnêtes par unité ;
- m et la lecture e-BH de G1 (combien de critères, quel k* plausible) ;
- le nombre de gardes (comparateurs) ;
- le biais E[g] tenu pour « honnête » ;
- une simulation du minimum avec les contrastes ;
- le passage sur le fichier réel, après GD-05 et GD-09.

## Ce que je n'ai pas pu vérifier

- `simulation-couche-2-executions-v1.py` (non fourni) : l'identité « mêmes définitions » est vérifiée contre le pôle
  v40, pas contre ce fichier.
- L'origine de σ = 0,028, le commit de lancement, la décision D-S sur δ, le fichier d'essai de 180 écarts « fabriqué
  hors dépôt ».
- Le préenregistrement de G1 : m, comparateurs, partie lue, τ. Mes chiffres (a) et (b) sont conditionnels.
- Le passage sur la loi réelle (aucun fichier d'écarts réels fourni).

## Fichiers produits (sous `.../scratchpad/relecture-garde-delta/cl/`)

| fichier | sha256 |
|---|---|
| `outils/verif_equivalence.py` (équivalence avec le pôle, plancher exact, `evaluer`, e-BH) | `10aa6f04…809c4c` |
| `outils/verif_sensibilite.py` (bruit, biais, plancher, mutants) | `b5f6a27b…113516` |
| `outils/verif_entrees.py` (31 fichiers d'entrée et 12 options) | `5cd51da9…f88e44` |
| `outils/verif_gardes_multiples.py` | `1ddf7ef3…4590ce` |
| `outils/resumer.py` | `b65567d3…8eda` |
| `outils/copie_script/sim_garde.py` (copie conforme du script) | `37c3dc7a…a7463` |
| `outils/copie_pole/pari_apparie.py`, `cycle.py` (copies v40) | `56bc8e03…`, `798f0390…` |
| `sorties/repro-meme-graine.json` | `053ddc1c…eccac54e` |
| `sorties/graine-neuve.json` (graine 918273645) | `34f3e69b…79b3964` |
| `sorties/verif_equivalence.json` | `f603eed5…90c0fc326` |
| `sorties/verif_sensibilite.json` (graine 4242) | `1b41ebf2…9ed532` |
| `sorties/verif_entrees.json`, `sorties/essais_entrees/entrees/` | `12a6f2d5…b2405` |
| `sorties/verif_gardes_multiples.json` (graine 777) | `b0f2079c…bcae3c` |

Note : les empreintes complètes sont dans `cl/EMPREINTES-contre-lecture-garde-delta-v1.txt`. Les fichiers `.err`
sont tous vides, sauf les avertissements attendus et capturés dans `verif_entrees.json`.
