# Coupe du calibrage honnête du contrôle 12 : dans les tâches ou entre tâches — v1

Analyste neuf, 29 octobre 2026. **Exploratoire, processeur seul, non préenregistré, non opposable.** Lu : le rapport
du contrôle 12 joint et ses deux scripts, la synthèse du pilote complémentaire (section 3) et son script de
vérification, la pièce A2 (`20bb005c…`, importée sur place, non modifiée). Rien d'autre.

Fichiers (dans ce dossier, chacun avec son `.sha256`) : `coupe-calibrage-v1.py` (`87b2130b…`) →
`coupe-calibrage-v1-sortie.json` et `-journal.txt` ; `tableaux-coupe-calibrage-v1.py` → `tableaux-coupe-calibrage-v1.md`
(toutes les lignes, intervalles compris) ; `manifeste-coupe-calibrage-v1.json`. Graine maîtresse 202610291500.
Python 3.13.17, numpy 2.5.3.

## Verdict

1. **La coupe entre tâches est exclue à 64 tâches.** Au point de base (9 600 épisodes, seuil 40, bilatéral),
   l'échec joint vaut **0,54** [0,53–0,56] entre tâches, contre **0,029** [0,024–0,035] dans les tâches. Plus
   d'exécutions n'y change presque rien : 0,36 à 76 800 épisodes.
2. **« 48 au lieu de 64 » n'a pas de sens**, dans aucune lecture. La coupe entre tâches ne dispense d'aucune tâche :
   elle en demande 8 à 30 fois plus (section 3).
3. **La coupe dans les tâches tient sans dérive. La coupe temporelle (le code actuel) devient un détecteur de dérive.**
   - À 0,05 σ de dérive, l'échec joint vaut 0,082 (au-dessus de 0,05).
   - À 0,10 σ, il vaut 0,32 ; à 0,20 σ, 0,96.
   - **Tirée par graine** dans chaque tâche, la coupe reste à 0,024–0,027 à toute dérive.
4. **G1 ne dépend pas de la coupe**, puisque ses seuils viennent de tout le calibrage. Ce qui dépend de la coupe,
   c'est la part de G1 qui survit si un échec du contrôle 12 la bloque.

**Recommandation : couper dans les tâches, par un tirage aléatoire des graines scellé d'avance** (pas la parité),
**et tester la dérive par un test séparé.** Confiance ≈ 0,75 contre la coupe entre tâches, ≈ 0,6 pour le tirage par
graine plutôt que la coupe temporelle.

## 1. Modèle et comptes

Le modèle latent gaussien est celui du rapport du contrôle 12 joint, avec a = 0,3, h = 0,3 et ρ = 0 en base.
- **Cellules.** 8 cellules critères × 2 modes, soit 16 contrôles. Seuil conforme strict à 1 %. Les scores sont
  continus, ce qui équivaut au bris d'égalité aléatoire appliqué d'office ; la variante « grille 0,25 + bris » le
  vérifie.
- **Épreuve.** 64 unités, K = 10 sabotés par unité, sur les mêmes tâches que le calibrage. Richesse mélangée sur Λ.
- **Échec joint.** Au moins un contrôle sur 16 atteint 40, dans un sens ou dans l'autre (bilatéral). L'unilatéral
  est dans les tableaux.
- **Trois coupes.** (1) **Dans, temporelle** : premières exécutions de chaque tâche contre dernières (code actuel).
  (2) **Dans, par graine** : la moitié des exécutions de chaque tâche, tirée au hasard. (3) **Entre tâches** : 32
  tâches tirées au hasard contre les 32 autres, toutes leurs exécutions.
- **Dérive.** Linéaire en rang d'exécution dans chaque tâche, commune aux cellules, sur le calibrage seul. **d est
  l'écart entre les moyennes des deux moitiés temporelles, en σ total** (× 1,2 en σ intra-tâche). L'amplitude du
  premier au dernier rang vaut donc ≈ 2d.
- **G1.** Un sujet (rappel 0,50) contre les 8 critères (0,40), soit l'écart de 10 points. Seuils sur tout le
  calibrage. Intersection-union : minimum des 8 richesses, promotion à 20. Les deux modes sont exigés.
- **Nombres aléatoires communs.** À paramètres égaux, les trois coupes lisent les mêmes mondes : leurs écarts viennent
  de la seule coupe.
- **Répétitions.** 4 000 par point au tableau principal, 2 000 ailleurs. Intervalles de Wilson à 95 %.

**Reproductions.**
- Coupe temporelle sans dérive : 0,029 (unilatéral 0,016), contre 0,027 (0,012) au rapport ; compatible.
- Écart-type de s1 − s2 : 0,075 σ dans les tâches et 0,209 σ entre tâches, contre 0,072 et 0,212 dans la synthèse.

## 2. Tableau principal

Échec joint du contrôle 12 : 16 contrôles, seuil 40, bilatéral, 9 600 épisodes, 4 000 répétitions. Demi-largeur de
Wilson ≈ ± 0,005 vers 0,03, ± 0,015 vers 0,5.

| a | dérive d (σ) | dans, temporelle | dans, par graine | entre tâches |
|---|---|---|---|---|
| 0,1 | 0 | 0,032 | 0,027 | 0,264 |
| 0,1 | 0,05 | **0,095** | 0,029 | 0,259 |
| 0,1 | 0,10 | **0,356** | 0,036 | 0,272 |
| 0,1 | 0,20 | **0,969** | 0,037 | 0,250 |
| 0,3 | 0 | 0,029 [0,024–0,035] | 0,025 [0,020–0,030] | **0,542** [0,527–0,558] |
| 0,3 | 0,05 | **0,082** [0,073–0,090] | 0,027 | 0,549 |
| 0,3 | 0,10 | **0,316** [0,301–0,330] | 0,025 | 0,544 |
| 0,3 | 0,20 | **0,965** | 0,024 | 0,536 |
| 0,5 | 0 | 0,019 | 0,017 | 0,681 |
| 0,5 | 0,05 | **0,067** | 0,021 | 0,663 |
| 0,5 | 0,10 | **0,276** | 0,021 | 0,678 |
| 0,5 | 0,20 | **0,947** | 0,019 | 0,681 |

**Mécanisme.**
- **Entre tâches**, l'effet de tâche n'est plus compensé. s1 − s2 porte alors un terme qui ne baisse qu'avec le nombre
  de tâches : 0,12, 0,21 et 0,32 σ pour a = 0,1, 0,3 et 0,5. Ce terme est presque commun aux 8 cellules, puisque
  l'effet de tâche est partagé.
- **Coupe temporelle sous dérive.** La moyenne de s1 − s2 vaut exactement −d (−0,050, −0,100, −0,200 mesurés). Ce
  biais se lit tout entier dans le sens « + » : l'unilatéral égale le bilatéral.
- **Coupe par graine.** La rampe se répartit au hasard entre les deux moitiés : la moyenne reste à 0, et
  l'écart-type ne bouge pas (0,074–0,077 σ).

**Puissance de G1** (écart de 10 points, deux modes). Elle est identique sous les trois coupes, par construction. Le
tableau donne aussi la part de G1 qui survit si un échec du contrôle 12 (seuil 40, bilatéral) la bloque.

| a = 0,3 | G1 seule | G1 et contrôle 12 propre : temporelle | par graine | entre tâches |
|---|---|---|---|---|
| d = 0 | 0,104 [0,095–0,114] | 0,100 | 0,102 | 0,047 |
| d = 0,10 | 0,103 | 0,072 | 0,101 | 0,053 |
| d = 0,20 | 0,104 | 0,005 | 0,102 | 0,046 |
| ρ = 0,8, d = 0 | 0,297 | 0,288 | 0,287 | 0,154 |

**Lecture de G1.**
- G1 par mode vaut 0,26 (0,22 à a = 0,1 ; 0,29 à a = 0,5). La dérive commune ne la déplace pas.
- **R4, réserve** : 0,10 sur deux modes est bas. Ce chiffre vient du pire cas que j'ai posé : 8 comparateurs, tous
  exactement 10 points sous le sujet, indépendants de lui dans l'épisode (ρ = 0). À ρ = 0,8, il vaut 0,30. Ce n'est
  pas une estimation de la puissance de G1 : seul le contraste entre coupes est l'objet ici.
- La coupe entre tâches coûterait la moitié de G1 si l'échec du contrôle 12 avait une conséquence. La coupe temporelle
  la coûterait sous dérive.

## 3. Variantes et « 48 au lieu de 64 »

**Variantes** (a = 0,3 ; seuil 40, bilatéral ; 2 000 répétitions ; détail dans `tableaux-coupe-calibrage-v1.md`).

| variante | temporelle | par graine | entre tâches |
|---|---|---|---|
| h = 0 (pire monde du rapport), d = 0 / 0,10 | 0,042 / **0,403** | 0,035 / 0,046 | 0,592 / 0,590 |
| ρ = 0,8, d = 0 / 0,10 | 0,027 / 0,234 | 0,028 / 0,024 | 0,499 / 0,470 |
| grille 0,25 + bris aléatoire, d = 0 / 0,10 | 0,019 / 0,328 | 0,022 / 0,026 | 0,531 / 0,552 |
| 3 modes, 24 contrôles, d = 0 / 0,10 | 0,033 / 0,394 | 0,038 / 0,033 | 0,559 / 0,586 |
| dérive d'une seule cellule, 0,10 / 0,20 | 0,071 / 0,369 | 0,024 / 0,028 | 0,552 / 0,531 |
| dérive en ordre des tâches, 0,10 / 0,20 | 0,028 / 0,035 | — | 0,566 / 0,568 (contiguë : 0,592 / 0,712) |

**Ce que montrent les variantes.**
- **24 contrôles.** La coupe dans les tâches tient sans dérive : 0,033 à 0,038. L'extrapolation du rapport (0,045 à
  0,055) était pessimiste.
- **Symétrie (R4).** Une dérive d'une tâche à l'autre (tâches fabriquées en série) n'atteint pas la coupe temporelle.
  Elle aggrave la coupe entre tâches contiguë (0,71). Aucune variante ne sauve la coupe entre tâches.

**À quelle taille la coupe entre tâches égale-t-elle la coupe dans les tâches ?** La cible est 0,029 à a = 0,3
(9 600 épisodes, 64 tâches).

| leviers (a = 0,3) | échec joint entre tâches |
|---|---|
| 64 tâches, 150 / 300 / 600 / 1 200 exécutions | 0,551 / 0,452 / 0,382 / 0,363 : **plancher, jamais atteint** |
| 9 600 épisodes répartis sur 128 / 320 / 640 / 1 920 / 9 600 tâches | 0,420 / 0,257 / 0,135 / 0,072 / 0,035 |
| 150 exécutions par tâche, 128 / 256 / 512 tâches | 0,282 / 0,106 / **0,022** (76 800 épisodes) |

**La parité demande, à a = 0,3 :** plusieurs milliers de tâches distinctes à 9 600 épisodes (0,072 à 1 920 ; 0,035 à
9 600 tâches d'une exécution), ou ≈ 400 à 500 tâches à 150 exécutions.
- À a = 0,1 (cible 0,032) : ≈ 150 à 200 tâches à 150 exécutions (0,052 à 128 ; 0,003 à 256), ou des milliers à
  9 600 épisodes.
- À a = 0,5 (cible 0,019) : ≈ 1 000 tâches à 150 exécutions (0,022 à 1 024).

**L'équivalence dans l'autre sens.** La coupe entre tâches à 9 600 épisodes vaut la coupe dans les tâches à ≈ 3 000
épisodes (64 × 50 : 0,487). Elle jette donc les deux tiers du calibrage. Les « 48 tâches » ne correspondent à rien :
- 48/64 du calibrage dans les tâches (≈ 7 200 épisodes) donne 0,082, ce qui échoue déjà.
- Aucune taille de la coupe entre tâches ne passe sous 64 tâches.

La synthèse note que le 48 de la pièce D est le plancher de H1a sous strates de dose. Je ne trouve aucune autre
source.

## 4. Recommandation

**Dans les tâches, avec moitiés tirées par graine.** Le tirage :
- est fait par `SeedSequence` ;
- est scellé avant la génération ;
- est indépendant du rang, de l'instance et de l'horodatage ;
- n'est ni pair/impair ni autre règle déterministe.

**Pourquoi.**
- C'est la seule coupe qui reste sous 0,05 dans toutes les cases simulées : au plus 0,046, à h = 0 et d = 0,10.
- Elle garde au contrôle 12 son rôle de garde-fou de niveau.
- Elle ne sacrifie rien de G1.

**Le prix.** Le contrôle 12 ne voit plus la dérive. Celle-ci doit être cherchée par un test temporel dédié : la
proposition E-6 d'A, sur les 9 600 honnêtes, lu avant tout saboté, avec son propre budget d'erreur et sa conséquence
scellée. Il ne faut pas compter sur le contrôle 12 pour cela.

**Ce qui ferait choisir la coupe temporelle (position de C, E-4 (b)).** Lazar veut que le contrôle 12 serve aussi
d'alarme de dérive. Elle sonne à 0,08 pour 0,05 σ, 0,32 pour 0,10 σ, 0,96 pour 0,20 σ. Mais alors :
- un échec ne distingue plus le bruit de la dérive ;
- la conséquence d'un échec doit être écrite pour les deux cas ;
- le taux de 0,05 n'est tenu que si la dérive est inférieure à ≈ 0,03 σ (interpolé), ce que le pilote ne peut pas établir
  (0,10 σ y est invisible).

**Ce qui rouvrirait la coupe entre tâches.**
- Un calibrage sur plusieurs centaines de tâches distinctes : ≈ 400 à 500 à 150 exécutions par tâche si a ≈ 0,3, mesuré.
  Cela suppose des tâches hors des 64 d'épreuve, une autre question que la pièce A2 (section F) ouvre.
- Un effet de tâche mesuré presque nul, a ≤ 0,05 (non simulé : à a = 0,1, c'est encore 0,26).
- Une raison de croire les exécutions d'une même tâche non échangeables pour une cause autre que le rang : cache
  partagé, flux de graines corrélé. Ni le tirage par graine ni la coupe temporelle ne la corrigent ; à tester au
  journal de fabrique.

**Ce qui ferait rejeter aussi la coupe par graine.** Une dérive périodique ou liée à l'identité des graines (instance
attribuée par graine) : le tirage doit être indépendant de l'attribution des instances, et cela se vérifie au journal.

## 5. Limites

- **Le monde est latent, gaussien et à variance commune.** a, h, ρ et les rappels sont supposés, pas mesurés.
  L'effet de tâche est commun aux cellules et indépendant d'une tâche à l'autre. Les queues lourdes et les scores
  bimodaux ne sont pas couverts.
- **La dérive est linéaire, commune aux cellules (sauf une variante) et touche le calibrage seul.** Les sabotés sont
  au milieu de la rampe. Une dérive qui touche aussi les sabotés, ou non monotone, ou corrélée au mode, n'est pas
  simulée.
- **G1 est simplifiée.** Les 8 comparateurs sont à 10 points, la corrélation est uniforme et l'hétérogénéité est
  commune. La puissance absolue est indicative ; seuls comptent les écarts entre coupes, nuls par construction hors
  blocage.
- **« Contrôle 12 propre » suppose qu'un échec bloque G1.** Je n'ai pas cherché la conséquence réelle d'un échec,
  conformément à la consigne de lecture.
- **Coupe entre tâches.** L'affectation est aléatoire, et l'épreuve porte sur les mêmes 64 tâches. Au-delà de 64
  tâches, le calibrage inclut des tâches hors épreuve, tirées de la même loi : c'est une hypothèse forte.
- **Précision.** Avec 2 000 à 4 000 répétitions, les écarts de moins de 0,01 entre coupes dans les tâches (sans dérive)
  ne sont pas résolus.
- **Statut.** Tout est à refaire sous préenregistrement, avec contre-lecture (R1, R2). Rien ici n'est opposable.
