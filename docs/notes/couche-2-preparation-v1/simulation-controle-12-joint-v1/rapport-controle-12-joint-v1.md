# Contrôle 12 joint de la couche 2 : 9 600 au seuil 40 ou 12 800 au seuil 20 — v1

Analyste neuf, 28 octobre 2026. **Exploratoire, processeur seul, non préenregistré, non opposable.** Lu : les pièces
A1, A2, C, D, la synthèse du collisionneur et ses vérifications ; rien d'autre du dépôt. Fichiers dans ce dossier, chacun
avec son `.sha256` : copie conforme de A2 (`20bb005c…`, importée, non modifiée) ; `controle-12-joint-v1.py`
(`ae936eda…`) → `…-sortie.json` (`fd1b4900…`) ; `controle-12-joint-v1-complement-ex-aequo.py` (`ad85985b…`) →
`…-sortie.json` (`7be741d6…`) ; manifeste (graine maîtresse 20261030, une suite `SeedSequence` par point via `rng_de`
de A2 ; Python 3.13.17, numpy 2.5.3).

## Verdict

1. **Les deux options tiennent 0,05 conjointement sur 16 contrôles, dans un sens comme dans les deux**, au point de base
   (a = 0,3 ; h = 0,3 ; cellules indépendantes dans l'épisode). (a) 9 600 au seuil 40 : 0,012 en unilatéral, 0,027 en
   bilatéral. (b) 12 800 au seuil 20 : 0,018 et 0,038.
2. **Le sens compte : le bilatéral double à peu près tout** (rapport 1,9 à 2,3). 9 600 au seuil 20 passe de 0,049 à
   0,10 et échoue. Sous lecture bilatérale, (b) touche ou dépasse 0,05 dans trois variantes pessimistes (au pire 0,060
   avec h = 0). (a) reste sous 0,039 partout dans le monde continu.
3. **Seuil 40 sur 64 unités ≈ calibrage 1,42 fois plus grand au seuil 20** (soit ≈ 13 600). (a) est donc un peu plus
   sûre que (b) sur le niveau, et coûte 3 200 épisodes de moins.
4. **Le prix du seuil 40 n'est pas payé par G1** s'il reste confiné au diagnostic. Il est payé par le diagnostic
   lui-même : sa sensibilité à une vraie dérive de calibrage est divisée par deux environ. S'il fuyait vers les fiches
   de G1 ou la garde, il coûterait cher (section 4).
5. **Le risque dominant, ce sont les ex æquo.** Scores discrets sans bris d'égalité : échec joint de 0,35 à 0,54
   (unilatéral), quelle que soit l'option. Un bris d'égalité aléatoire scellé (retouche 3 de A1, D-S13) rend le monde
   continu : préalable aux deux options.

**Recommandation : (a) 9 600 + seuil 40, sous conditions** (section 5). Confiance ≈ 0,6.

## 1. Ce que je simule, et comment je compte

**Contrôle 12** (A1 § 3, A2 `controle_12_intra_taches`). Une cellule est calibrée deux fois, sur deux moitiés
disjointes du calibrage honnête : s1 et s2, seuil conforme strict du code (j = ⌊τ(n + 1)⌋, τ = 1 %). On lit ensuite la
même cellule contre elle-même sur les 64 unités sabotées d'un mode (K = 10). Le processus est v(t) = alerte(s1) −
alerte(s2), avec la richesse mélangée de A2 sur Λ = {0,1 ; 0,3 ; 0,6 ; 0,9}. Il y a promotion à tort si la richesse
atteint le seuil de diagnostic (20, 30, 40, 60). Il n'y a pas de garde par défaut, comme A1 le demande ; la garde à
δ = 0,10 est une variante. **Unilatéral** : le seul sens « moitié 1 > moitié 2 », comme dans A2. **Bilatéral** : l'un
ou l'autre sens. **Échec joint** : au moins un contrôle (cellule × mode × strate) promu.

**Modèle** (extension de A2 et de V4 de la synthèse).
- Calibrage : 64 tâches d'épreuve × N/64 exécutions honnêtes, soit 75, 100, 150, 200 ou 250 par tâche.
- Score de la cellule c : Z = √a·U(tâche) + √(1 − a)·(√ρ·E(épisode) + √(1 − ρ)·bruit propre).
- Moitiés coupées **dans** chaque tâche : premières exécutions contre dernières.
- Sabotés : même effet de tâche U que le calibrage (mêmes tâches) ; A2 le tirait indépendant, c'est une variante.
  Hétérogénéité h·H(unité, mode), commune aux cellules. Rappel marginal de 0,40 au seuil de population. Deux modes,
  épisodes distincts, mêmes seuils s1 et s2 (calibrage partagé).

**Nombre de cellules critères : 8 par mode, soit 16 contrôles.**
- N-056, point 1 : G1 doit battre chaque moniteur boîte noire de la liste scellée, plus (ii) et (iii).
- A1 § 4 marque « critère » : (ii) cascade ; (iii) dernier état ; juge 8B par action ; (i) noir additif ; (iv) modèle
  temporel ; TRACE-lite ; juge robustifié b* ; prédicteur sur les traits du texte. Cela fait 8, le compte repris par
  la synthèse.
- Variantes : 9 × 2 si le sujet (blanc séquentiel) a aussi son contrôle 12 ; 10 + 9 si la règle du coût déclaré (même
  ligne que le prédicteur, famille spécialisée du mode « coût ») compte comme cellule à part dans ce mode.
- **Strates** : la synthèse retient une seule dose en épreuve, donc pas de strate « diffus » à l'épreuve. La strate
  d'horizon (retouche 1 de A1) est simulée en variante : 2 strates de 32 tâches, 32 contrôles.

**Répétitions.** 4 000 par point pour le tableau principal, 2 000 pour la sensibilité et les variantes. Intervalles de
Wilson à 95 %.

**Cohérence.** Partition et tri de A2 donnent le même seuil. Reproduction de la synthèse (8 × 2, h = 0, seuil 20,
ρ = 0 et 0,8) : 0,063 et 0,057 à 9 600 (synthèse : 0,078 et 0,068 à 1 000 tirages), 0,023 et 0,021 à 12 800 (0,031 et
0,020) ; compatible à l'erreur de tirage près.

## 2. Tableau principal

Taux d'échec joint (16 contrôles). a = 0,3 ; h = 0,3 ; 4 000 répétitions ; [intervalle de Wilson à 95 %].

| N | seuil | unilatéral, ρ = 0 | bilatéral, ρ = 0 | unilatéral, ρ = 0,8 | bilatéral, ρ = 0,8 |
|---|---|---|---|---|---|
| 4 800 | 20 | 0,246 [0,233–0,259] | 0,475 [0,460–0,491] | 0,171 [0,159–0,183] | 0,388 [0,373–0,403] |
| 4 800 | 30 | 0,164 [0,153–0,176] | 0,330 [0,315–0,344] | 0,113 [0,104–0,123] | 0,266 [0,252–0,280] |
| 4 800 | 40 | 0,120 [0,110–0,130] | 0,247 [0,234–0,261] | 0,085 [0,077–0,094] | 0,196 [0,184–0,209] |
| 4 800 | 60 | 0,073 [0,065–0,081] | 0,155 [0,144–0,167] | 0,052 [0,045–0,059] | 0,125 [0,115–0,136] |
| 6 400 | 20 | 0,149 [0,138–0,160] | 0,283 [0,269–0,297] | 0,121 [0,111–0,131] | 0,234 [0,221–0,247] |
| 6 400 | 30 | 0,089 [0,080–0,098] | 0,166 [0,154–0,177] | 0,072 [0,064–0,080] | 0,135 [0,125–0,146] |
| 6 400 | 40 | 0,057 [0,051–0,065] | 0,109 [0,099–0,119] | 0,045 [0,039–0,052] | 0,088 [0,079–0,097] |
| 6 400 | 60 | 0,027 [0,022–0,032] | 0,055 [0,048–0,063] | 0,028 [0,024–0,034] | 0,051 [0,045–0,059] |
| 9 600 | 20 | 0,049 [0,043–0,056] | **0,102** [0,093–0,111] | 0,042 [0,036–0,048] | 0,085 [0,076–0,094] |
| 9 600 | 30 | 0,024 [0,020–0,029] | 0,049 [0,043–0,056] | 0,020 [0,016–0,025] | 0,042 [0,036–0,048] |
| **9 600** | **40** | **0,012** [0,009–0,016] | **0,027** [0,022–0,032] | 0,010 [0,008–0,014] | 0,022 [0,017–0,027] |
| 9 600 | 60 | 0,005 [0,003–0,007] | 0,012 [0,009–0,015] | 0,005 [0,003–0,008] | 0,011 [0,008–0,014] |
| **12 800** | **20** | **0,018** [0,014–0,022] | **0,038** [0,033–0,044] | 0,015 [0,012–0,020] | 0,032 [0,027–0,038] |
| 12 800 | 30 | 0,007 [0,005–0,010] | 0,015 [0,012–0,019] | 0,007 [0,004–0,010] | 0,014 [0,010–0,018] |
| 12 800 | 40 | 0,003 [0,002–0,006] | 0,007 [0,004–0,010] | 0,003 [0,002–0,005] | 0,006 [0,004–0,009] |
| 12 800 | 60 | 0,001 [0,000–0,002] | 0,002 [0,001–0,003] | 0,001 [0,001–0,003] | 0,003 [0,001–0,005] |
| 16 000 | 20 | 0,007 [0,005–0,010] | 0,017 [0,014–0,022] | 0,007 [0,005–0,010] | 0,015 [0,012–0,019] |
| 16 000 | 30 | 0,002 [0,001–0,004] | 0,005 [0,003–0,007] | 0,002 [0,001–0,003] | 0,005 [0,003–0,007] |
| 16 000 | 40 | 0,001 [0,000–0,002] | 0,002 [0,001–0,003] | 0,001 [0,001–0,003] | 0,003 [0,002–0,006] |
| 16 000 | 60 | 0 [0–0,001] | 0 [0–0,001] | 0 [0–0,001] | 0 [0–0,001] |

**Pourquoi le bilatéral double.** Les deux modes lisent les mêmes seuils s1 et s2, et une même série d'épisodes est
comparée aux deux seuils. Si s1 < s2, alors v(t) ≥ 0 pour toute unité, et le sens « − » ne peut pas promouvoir. Pour
une cellule, les deux sens sont donc deux événements exclusifs de même probabilité : le bilatéral vaut exactement le
double. Sur 16 contrôles, le recouvrement ramène le rapport à 1,9–2,3.

**Pourquoi seuil et taille s'échangent.** Une richesse de 20 sur 64 unités demande un écart constant de 7,35 points.
Une richesse de 40 en demande 8,75, soit 1,19 fois plus. Le bruit de l'écart entre moitiés décroît en 1/√N (2,94
points à 9 600, synthèse V2). Passer de 20 à 40 vaut donc multiplier N par 1,19² ≈ 1,42 : 9 600 au seuil 40 se comporte
comme ≈ 13 600 au seuil 20. Le tableau le confirme : (a) est sous (b) dans les quatre colonnes.

## 3. Sensibilité

À 9 600 et 12 800 : un paramètre bouge, les autres restent à la base (a = 0,3 ; h = 0,3 ; ρ = 0). 2 000 répétitions.
U = unilatéral, B = bilatéral. Intervalles dans la sortie (largeur ≈ ± 0,01 vers 0,05).

| variation | (a) 9 600, seuil 40, U | (a) B | (b) 12 800, seuil 20, U | (b) B | 9 600, seuil 20, U / B |
|---|---|---|---|---|---|
| effet de tâche a = 0,1 | 0,022 | 0,039 [0,031–0,048] | 0,031 | **0,050** [0,041–0,060] | 0,068 / 0,127 |
| a = 0,3 (base) | 0,014 | 0,029 | 0,022 | 0,033 | 0,054 / 0,111 |
| a = 0,5 | 0,010 | 0,018 | 0,016 | 0,033 | 0,039 / 0,076 |
| hétérogénéité h = 0 | 0,018 | 0,033 | 0,033 | **0,060** [0,050–0,071] | 0,066 / 0,130 |
| h = 0,3 (base) | 0,016 | 0,028 | 0,026 | 0,043 | 0,062 / 0,111 |
| h = 0,5 | 0,007 | 0,017 | 0,010 | 0,023 | 0,032 / 0,066 |
| concordance entre cellules ρ = 0 | 0,013 | 0,027 | 0,022 | 0,043 | 0,058 / 0,105 |
| ρ = 0,5 | 0,015 | 0,029 | 0,020 | 0,040 | 0,045 / 0,107 |
| ρ = 0,8 | 0,015 | 0,023 | 0,018 | 0,036 | 0,053 / 0,096 |
| ρ = 0,9 | 0,009 | 0,017 | 0,015 | 0,030 | 0,035 / 0,064 |
| 9 × 2 cellules (sujet compris) | 0,022 | 0,039 | 0,024 | 0,045 | 0,070 / 0,129 |
| 10 + 9 (sujet, règle du coût) | 0,022 | 0,037 | 0,026 | **0,050** [0,041–0,060] | 0,071 / 0,138 |
| sabotés à effet de tâche indépendant (A2) | 0,012 | 0,028 | 0,026 | 0,044 | 0,059 / 0,113 |
| garde à δ = 0,10 comprise | 0,014 | 0,026 | 0,021 | 0,035 | 0,059 / 0,112 |
| rappels hétérogènes (0,15 à 0,75) | 0,013 | 0,023 | 0,012 | 0,024 | 0,047 / 0,083 |
| pire combiné (a = 0,5 ; h = 0,5 ; 9 × 2) | 0,007 | 0,012 | 0,008 | 0,013 | 0,029 / 0,057 |
| 2 strates d'horizon (32 tâches chacune) | 0 | 0,001 | 0,001 | 0,002 | 0,004 / 0,009 |

Lecture :
- **Sens contre-intuitif.** Un effet de tâche fort aide (la coupe dans les tâches l'annule) ; une hétérogénéité forte
  aussi (moins d'unités près des seuils). Le pire monde est **homogène, à faible effet de tâche, avec plus de
  cellules**. Mon « pire combiné » (a et h hauts) est en fait le plus clément : signalé (R4).
- **(a) ne dépasse jamais 0,039**, dans aucune ligne ni aucun sens. **(b) atteint ou dépasse 0,05 en bilatéral** dans
  trois lignes : h = 0, a = 0,1, et 10 + 9 cellules. En unilatéral, (b) reste sous 0,034.
- **Les strates d'horizon rendent le diagnostic aveugle ; elles ne le rendent pas propre.** Avec 32 unités, une
  promotion demande un écart constant de 15 points, alors que le calibrage par strate est deux fois plus bruité. Un
  contrôle 12 « réussi » par strate ne prouverait presque rien (R4 : trop beau, réserve).

**Ex æquo** (complément, 2 000 répétitions). Scores arrondis à une grille de 0,25 écart-type (≈ 13 à 20 niveaux sur la
plage utile, ordre de grandeur d'un juge lu par un jeton) ou de 0,05 écart-type. Convention stricte « > » du code.

| variante | (a) U | (a) B | (b) U | (b) B |
|---|---|---|---|---|
| grille 0,25, les 8 cellules, sans bris | **0,420** | **0,606** | **0,465** | **0,625** |
| grille 0,25, 3 cellules sur 8, sans bris | 0,196 | 0,352 | 0,271 | 0,432 |
| grille 0,25, 8 cellules, bris d'égalité aléatoire | 0,016 | 0,031 | 0,025 | 0,042 |
| grille 0,05, 8 cellules, sans bris | 0,015 | 0,032 | 0,032 | 0,055 |
| grille 0,05, 8 cellules, bris aléatoire | 0,012 | 0,026 | 0,018 | 0,032 |

**Mécanisme.** s1 et s2 tombent sur des niveaux de la grille ; quand le point à 1 % est dans un niveau, les deux
moitiés prennent souvent deux niveaux voisins. Le rappel saute d'un niveau entier (≈ 10 points à 0,25 écart-type), que
64 unités certifient sans peine. Ni N ni le seuil n'y font rien ; un ordre tiré dans chaque niveau supprime le saut.

## 4. Ce que coûte le seuil 40

**Sur G1 : rien, s'il reste confiné au contrôle 12.** Les fiches de G1 promeuvent à 1/α = 20 (D-S2, D-S6), et la garde
certifie à 20. Le seuil de diagnostic ne touche ni l'une ni l'autre.

**Sur le diagnostic lui-même : la moitié de sa sensibilité.** J'ai simulé une vraie dérive entre les moitiés d'une
seule cellule : la moitié 2 décalée de 0,05, 0,10 ou 0,15 écart-type, soit un écart de rappel de population de 1,9, 3,8
ou 5,7 points. Le tableau donne la probabilité de signaler la cellule dérivée (dans le bon sens, un mode).

| écart réel | 9 600, seuil 20 | (a) 9 600, seuil 40 | (b) 12 800, seuil 20 | 12 800, seuil 40 |
|---|---|---|---|---|
| 1,9 points | 0,030 | 0,009 | 0,013 | 0,002 |
| 3,8 points | 0,082 | 0,032 | 0,064 | 0,022 |
| 5,7 points | 0,217 | 0,098 | 0,199 | 0,074 |

La sensibilité dépend surtout du seuil (les 64 unités fixent l'écart minimal certifiable), peu de N : (b) garde le
double de celle de (a). Mais les deux sont faibles (au plus 1 sur 5 pour 6 points) : le contrôle 12 est un garde-fou
de niveau, pas un détecteur de dérive, qui se cherche par un test dédié (ordre des exécutions ou des instances).

**Si le seuil 40 fuyait vers G1 ou la garde** (contre-exemple à interdire au préenregistrement).
- Un comparateur, 64 unités, K = 10, écart de 10 points : la puissance passerait de 0,63 à 0,42 (S1) et de 0,81 à 0,56
  (S2). À 20 points, rien ne change.
- Certification de la garde à 64 unités : de 0,77 à 0,12 pour δ = 0,08, de 0,999 à 0,93 pour δ = 0,10.
- Plancher de la garde pour δ = 0,10 : de 48 à 57 unités.

**Réponse à la question.** Un seuil plus haut ne rend la garde plus sévère pour les vrais écarts que s'il s'applique
à la garde. Appliqué au seul contrôle 12, il fait l'inverse : le diagnostic devient plus clément envers une vraie
dérive de calibrage.

## 5. Recommandation

**(a) 9 600 épisodes honnêtes, seuil de diagnostic 40 par contrôle**, confiance ≈ 0,6. Cinq conditions :
1. Le seuil 40 est **scellé avant toute lecture** et écrit comme **propre au contrôle 12**. Les fiches de G1 et la
   garde restent à 20.
2. Le **sens est fixé au scellement** ; je recommande le bilatéral (une moitié qui sous-alerte est un défaut autant
   que l'inverse). (a) le tient avec marge (≤ 0,039) ; (b) pas toujours.
3. **Bris d'égalité aléatoire scellé** (retouche 3 de A1, D-S13) pour toute cellule à scores discrets, avant la banque.
   Sans lui, aucune option ne tient : premier poste, avant le débat sur N.
4. **Pas de strate de calibrage qui coupe les 9 600** en gardant 64 unités par contrôle : 4 800 par strate donnent au
   moins 0,12 au seuil 40. Si la strate coupe aussi les unités, le contrôle 12 devient aveugle : le dire, ne pas le
   compter comme réussi.
5. Le compte des cellules est **arrêté au préenregistrement**. Jusqu'à 10 + 9, (a) tient (0,037 en bilatéral).

**Pourquoi (a).**
- Elle est plus sûre sur le niveau : 0,012 et 0,027 contre 0,018 et 0,038 au point de base, et au plus 0,039 contre au
  plus 0,060 en sensibilité.
- Elle coûte 3 200 épisodes de moins, chacun noté par toutes les cellules critères : aux rythmes de A1 § 8 (non
  revérifiés), 37 à 49 heures de génération et 52 à 207 de moniteurs, soit ≈ 90 à 255 heures de carte, ≈ 100 à 310
  dollars.

**Ce qui ferait passer à (b) 12 800 au seuil 20.**
- Lazar veut que le contrôle 12 serve **aussi** de détecteur de dérive : (b) double sa sensibilité, mais un test dédié
  ferait mieux.
- On exige un seul seuil 1/α = 20 partout, par lisibilité. Mais (b) ne tient le bilatéral que de justesse.
- Le pilote de l'étape 7 mesure des queues honnêtes lourdes ou des scores bimodaux : le bruit des seuils monte à N
  égal, et seule la marge de N protège. Refaire alors ce calcul avec les lois mesurées.

**Ce qui ferait rejeter les deux.**
- Une cellule critère à scores discrets sans bris d'égalité.
- Plus d'environ 24 contrôles (troisième mode compris) : extrapolé, non simulé.
- Une dérive mesurée entre les premières et les dernières exécutions d'une tâche. La coupe dans les tâches suppose
  des exécutions échangeables.

## 6. Limites (ce que le modèle latent gaussien ne dit pas)

- **Lois des scores.** Toutes les cellules sont gaussiennes, de même variance, avec un rappel de 0,40 en base. Le bruit
  de l'écart entre moitiés est proportionnel au rapport des densités au point à 1 % (sabotés sur honnêtes). Une queue
  honnête lourde, un juge bimodal ou un score séquentiel (maximum courant d'un processus) changent ce rapport. La
  variante des rappels hétérogènes (0,15 à 0,75) ne couvre pas la forme des queues.
- **Discrétisation.** Seulement deux grilles uniformes. Un vrai juge lu par l'espérance du jeton a des niveaux inégaux,
  et une masse d'ex æquo au sommet peut dépasser 1 %. Ce cas ne se règle que par le bris d'égalité.
- **Corrélation entre cellules uniforme** (ρ de 0 à 0,9). La structure réelle est en blocs : les cellules blanches
  partagent les sondes, les cellules noires partagent le texte. Elle est encadrée, pas modélisée.
- **Effet de tâche commun aux cellules** ; ni effet propre à une cellule, ni interaction tâche × moitié hors la dérive
  de la section 4.
- **Définition du contrôle 12** prise dans A2 (même cellule, deux moitiés, sans garde, 64 unités, K = 10) ;
  `monde_banque_scores.py` non lu, conformément à la consigne. Une autre définition (jumeaux honnêtes, par fiche)
  changerait les chiffres ; la garde à δ = 0,10 change peu.
- **Pas de scores non finis.** Des notes de juge manquantes (constatées au pilote, pièce C) réduiraient N par cellule ;
  une exclusion serait en outre une sélection (N-053).
- **Mode tenu à l'écart non compté.** Un troisième mode sur les mêmes seuils ajoute 8 contrôles corrélés. À 24
  contrôles, (a) en bilatéral serait vers 0,045–0,055 par extrapolation linéaire de 16 → 19 contrôles (l'union
  croît moins vite que linéairement) ; non simulé, à refaire si D-S29 (a) est confirmée.
- **Rien n'est mesuré.** a, h, ρ, les rappels et les lois sont supposés. Le pilote de mesure (A1 § 8, étape 7) doit les
  fournir avant le préenregistrement. Tous ces chiffres sont à refaire sous préenregistrement, avec contre-lecture
  (R1, R2).
