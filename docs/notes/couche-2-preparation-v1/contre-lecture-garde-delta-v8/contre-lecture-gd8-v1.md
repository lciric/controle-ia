# Contre-lecture GD8 — simulation de puissance de la garde δ, version 8 — v1

- Date : 30 octobre 2026, travail de 02:18 à 02:58 (UTC).
- Contre-lecteur : Claude Opus 5.5 (`claude-opus-5-5`), sous-agent **neuf** (règle R2) : je n'ai écrit aucune version de la garde δ ni de ses simulations.
- Objet : `origin/canal/conv-audit-n04` (commit `e1707aa4413396d4131f35efa651669e87d28916`), dossier
  `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/couche-2-conv-audit-v1/simulation-puissance-garde-delta-v8/`, extrait par `git archive`
  dans mon espace de travail (aucune autre lecture de `canal/*`, aucune lecture de `donnees/*`, `quarantaine/*`, `prereg/P3-consignes-v1.md`, `diag/*/traces`, ni du dossier
  `contre-lecture-garde-delta-v6/`). Je n'ai lu ni la v7 ni GD7 : le rapport v8 se suffit pour les points contrôlés.
- **Empreintes vérifiées** : rapport `rapport-puissance-garde-delta-v8.md` = `312f2cd0451a2692b19c703d041d6dd1fd363214b070f7f93fddf163e74ef9f1` ; script
  `simulation-puissance-garde-delta-v8.py` = `4c7c93a90e0be922e839f5826488edcc0745bde17f8a5de22f3a2a41bf75f1d1` ; manifeste d'ensemble
  `manifeste-puissance-garde-delta-v8-v2.json` = `a7dd020a734a634aca2340b403158ae1384e67bb405ba142ae364683178a2d26`. Les **206 compagnons `.sha256`** du dossier : 206 conformes, 0
  écart, aucun fichier sans compagnon. Les **35 empreintes** du tableau du § 12 du rapport : 35 conformes.
- Processeur seul, sans dépense. Graines par `numpy.random.SeedSequence`. Environnement de rejeu : Python 3.13.17, numpy 2.4.6, scipy 1.17.1 (la v8 : 3.13.18, 2.5.3, 1.18.1).

## Verdict

**Utilisable au préenregistrement après corrections** : les chiffres de puissance se reproduisent exactement, mais la table de lecture du pilote ne rend aucune
taille, avec sa propre règle, dès que la dispersion mesurée dépasse environ 0,05 (GD8-01), et le surcoût du neuvième comparateur (« +128 à +432 ») ne mesure pas
ce que la phrase lui fait dire (GD8-02).

## Ce qui est reproduit

| chiffre du rapport | rejeu GD8 (même script, même graine) | réimplémentation indépendante (autre graine) |
| --- | --- | --- |
| ρ = 0,17, 288 unités : 0,847 (seuil 40) ; 0,509 (seuil 160) | 0,847 ; 0,509 — identiques au bit | cellule la plus exigeante, moyenne de 21 graines : 0,837 et 0,497 (v8 sur les mêmes graines : 0,839 et 0,504) ; voir GD8-04 |
| ρ = 0,17, 400 unités : 0,980 ; 0,905 | 0,980 ; 0,905 — identiques | cellule la plus exigeante : 0,983 ; 0,9115 |
| ρ = 0,17 : n80 280 / 360 ; n90 320 / 400 ; n_h 304 / 384 | 280 / 360 ; 320 / 400 ; 304 / 384 — identiques | — |
| ρ = 0,10 : 0,970 / 0,768 ; n80 224 / 304 ; n_h 288 / 336 | identiques | cellule la plus exigeante : 0,969 ; 0,7555 |
| neuvième, écart 0,05, sans dispersion : 0,865 ; n80 264 / 344 ; surcoût +128 / +176 | identiques | 0,8665 |
| neuvième, écart 0,05, ρ = 0,17 : 0,312 ; n80 688 / 912 ; surcoût +432 / +568 | identiques | 0,319 |

Rejeu : `rejeu-gd8-v1.sh` (quatre passages complets, 2 000 répétitions, options de `lancer-passages-v8.sh`), comparaison champ à champ par
`comparer-rejeu-gd8-v1.py` : **1 456 champs comparés (toutes les cellules, tous les n80 et n90, tous les points de dichotomie), 0 différence**, malgré une version de
numpy différente. Sorties, journaux et manifestes écrits par le script lui-même : `rejeu-v1/`. Sortie de la comparaison : `comparer-rejeu-gd8-v1-sortie.json`.
Réimplémentation : `independant-gd8-v1.py` (écrite depuis le texte du rapport, sans reprendre le code), sortie `independant-gd8-v1-sortie.json`.

## Réponses aux trois points prioritaires du § 10

1. **Strates, « portée commune nulle par construction »** : oui, à un reste près, et c'est plus fort que ce que dit le rapport — voir GD8-03. Les lignes « commune »
   ne testent rien d'autre que la construction ; elles décrivent en outre un monde **différent** de la référence (la strate y joue le rôle d'une difficulté partagée,
   corrélation des probabilités du sujet et des comparateurs côté sabotage ≈ 0,77 pour deux strates, 0,51 pour trois), d'où leur fiche brute à 0,990 et 0,984 contre 0,847.
2. **Incertitude de graine de n80** : résolue, et plus petite que ne le dit le § 7 — voir GD8-04. L'ajustement de la courbe de puissance sur les points déjà évalués donne
   un écart-type de graine ≤ 0,6 unité (0,2 %) ; c'est la dichotomie, qui rend la borne haute de son dernier pas, qui domine (+0 à +8 unités). La marge 1,06 suffit
   largement pour la graine ; elle ne couvre pas l'erreur de Monte-Carlo sur les **puissances** affichées, qui ne sont pas des minorants.
3. **Écrêtage après étalonnage** : effet nul dans le périmètre, vérifié dans `verif-ebh-pole-v8-sortie.json` (≤ 7,8 × 10⁻⁵ de valeurs hors de [−1 ; 1], différence de
   puissance 0 dans les huit sous-cas) — voir GD8-05 : la réserve porte sur le critère de vérification réécrit après trois échecs, et sur ce qu'il faut écrire au
   préenregistrement si l'étalonnage par strate devait servir.

## Constats

### GD8-01 — La règle de lecture de la table du pilote ne rend rien dès ρ̂ ≈ 0,04 à 0,07 ; « 0,17 → 304 / 384 » vaut pour le ρ vrai, pas pour le ρ mesuré

- **Gravité : majeure** (bloque l'usage « tel quel » au préenregistrement).
- Fichier : `rapport-puissance-garde-delta-v8.md`, lignes 83 à 98 (table et règle), 30 et 252 (tailles citées) ; `tableaux-v8.py`, lignes 150 à 180.
- Constat : la règle écrite est « ρ_haut = ρ̂ + 1,645 × écart-type de la lecture ; ligne égale ou immédiatement supérieure ; lire les deux hypothèses sur le sujet
  et prendre la plus grande ; au-delà de 0,25, la table ne dit rien ». Or la grille « ρ_A = 2 ρ_B » s'arrête à ρ_B = 0,085 : pour tout ρ_haut > 0,085, l'une des deux
  hypothèses n'a pas de ligne, et la règle « prendre la plus grande » n'est pas définie. Avec les écarts-types de lecture du rapport lui-même (côté sabotage), cela arrive
  dès ρ̂ = 0,04 (pilote de 50 unités), 0,06 (100 unités), 0,07 (288 unités). La grille « ρ_A = ρ_B » seule cesse de répondre à ρ̂ = 0,18 (50), 0,19 (100), 0,22 (288).
  Et pour ρ̂ = 0,17 lu sur 288 unités, ρ_haut = 0,200 : la ligne lue est 0,25, soit **384 / 496**, non 304 / 384. Les tailles « 304 / 384 à ρ = 0,17 » du § 0, du § 6 et
  de la phrase du § 9 sont celles du ρ **vrai**, ce que le texte ne dit pas.
- Essai : `python3 -I -B regle-table-lecture-gd8-v1.py <v8>/tableaux-v8-sortie.json <v8>/precision-rho-pilote-v8-sortie.json regle-table-lecture-gd8-v1-sortie.json` ;
  sortie (extrait) : `N = 288 : plus grand ρ̂ lu 0,06 ; premier sans réponse 0,07 ; sans l'hypothèse 2, premier sans réponse 0,22` ;
  `ρ̂ = 0,17 → ρ_haut 0,200 ; ligne hyp1 0,25, hyp2 aucune → n_h indéfini`.
- Autres limites de la table, relevées sans essai : (a) la cible est une puissance de 0,8 avec une marge de graine, non 0,9 : à n_h = 304 (ρ = 0,17), la cellule la
  plus exigeante vaut 0,8785 (`points_evalues` du passage `meme-rho0.17`) ; (b) ρ_A > 2 ρ_B n'est pas couvert ; (c) la lecture suppose un même ρ des deux côtés
  (GD8-07) ; (d) la monotonie est respectée (n80 pire 184, 200, 224, 280, 360 et 264, 280, 304, 360, 456 ; enveloppe croissante appliquée).
- Correction : (1) prolonger la grille « ρ_A = 2 ρ_B » au moins à ρ_B ∈ {0,10 ; 0,125 ; 0,17} (ρ_A jusqu'à 0,34) et « ρ_A = ρ_B » à 0,30 et 0,35, avec des lignes
  intermédiaires (0,125 ; 0,20), ou bien restreindre explicitement la règle à l'hypothèse ρ_A = ρ_B et dire pourquoi ; (2) écrire un **repli scellé hors table**
  (par exemple : arrêt et nœud de décision, ou taille maximale de la grille) ; (3) donner la table directement en ρ̂ pour la taille de pilote prévue (marge 1,645 × écart-type
  incluse), et réécrire § 0, § 6 et § 9 : « 304 / 384 si ρ vrai = 0,17 ; 384 / 496 si ρ̂ = 0,17 sur 288 unités ».

### GD8-02 — « +128 à +432 unités » (neuvième comparateur fort) n'est pas l'écart des tailles ; « +128 sans dispersion » est contredit par la table

- **Gravité : majeure** (chiffre destiné au préenregistrement).
- Fichier : rapport, lignes 36, 241 à 242, 256 et 305 ; `tableaux-v8.py`, ligne 311 ; `resume-v8.py`, lignes 128 à 130.
- Constat : le « surcoût » est le **maximum, sur les quatre cellules, de la différence par cellule** n80(9) − n80(8) ; ce n'est ni l'écart des n80 pires, ni l'écart
  des n_h. Sans dispersion : surcoût +128 (cellule K_h = 10, biais 0 : 248 − 120), mais n80 pire 184 → 264 (+80) et **n_h 288 → 288 (+0)** ; la fiche vaut d'ailleurs
  0,865 à 288 unités. La phrase « pour garder 0,8 il faut, **en plus** de la taille à huit comparateurs, +128 (sans dispersion) » (ligne 241) est donc fausse. Au seuil
  160 et à ρ = 0,17, l'écart des n_h est **+592** (384 → 976), plus que le +568 annoncé : la définition ne borne l'écart des tailles ni par en haut ni par en bas.
- Essai : `python3 -I -B comparer-rejeu-gd8-v1.py <rejeu> <v8> comparer-rejeu-gd8-v1-sortie.json` ; sortie :
  `neuf-k9-g0.05-nulle, retenue_ebh : surcoût max (rapport) 128 | n80 pire k8 → k9 184 → 264 | n_h 288 → 288 ( 0 )` ;
  `neuf-k9-g0.05-rho0.17, atteinte_160 : surcoût max 568 | n80 pire 360 → 912 | n_h 384 → 976 ( 592 )`. Depuis `tableaux-v8-sortie.json` (bloc `neuvieme`), écarts de n_h
  à écart 0,05, seuil 40 : 0 (sans dispersion), +112 (ρ = 0,05), +208 (bêta σ = 1,0), +224 (logit σ = 1,0), +256 (ρ = 0,10), +432 (ρ = 0,17) ; seuil 160 : +80, +240,
  +368, +368, +400, +592.
- Correction : rapporter au préenregistrement **les n_h à neuf comparateurs** (288 à 736 au seuil 40 ; 368 à 976 au seuil 160) ou l'écart des n_h (**+0 à +432** ;
  **+80 à +592**), et réécrire les lignes 36, 241 à 242, 256 et 305. Le +432 du seuil 40 à ρ = 0,17 coïncide par hasard avec l'écart des n_h.

### GD8-03 — Strates : la portée « commune » est nulle par construction et décrit un autre monde ; la portée « sujet » est un cas extrême non chiffré dans le texte

- **Gravité : moyenne** (interprétation ; la recommandation « ne pas compter sur les strates » n'en est pas changée).
- Fichier : rapport, lignes 155 à 179 et 315 à 316 ; script, lignes 704 à 748 (`_moyennes_strates`, `_rho_interne`, `decalages_strates`) et 877 à 878 (étalonnage).
- Constat : (a) en portée commune, la difficulté de strate multiplie l'espérance du sujet et des comparateurs ; l'étalonnage ne retire du contraste que la différence
  (0,50 − 0,40)·γ·d = ±0,04 (deux strates, γ = 0,4), soit 2,7 % (deux strates) et 1,3 % (trois strates) de la variance du contraste
  (`part_variance_ecart_prevue_par_strates_contraste` des sorties) : le gain nul est **voulu par le modèle**, non mesuré. (b) Plus important : à ρ total tenu, la strate
  commune est une composante **partagée** par le sujet et les comparateurs ; la corrélation de leurs probabilités côté sabotage vaut
  0,5·0,4·γ²·moyenne(d²)/√(0,17·0,25 × 0,17·0,24) ≈ **0,77** (deux strates) et **0,51** (trois strates) — l'équivalent de la copule c ≈ 0,8 et 0,5 du § 3.1. D'où la
  fiche brute 0,990 et 0,984, non comparable au 0,847 de référence ; le texte ne le dit pas. (c) En portée sujet, la strate explique, côté sabotage, **94 %, 63 %, 24 %
  et 16 %** de la variance inter-unités de A (deux strates γ = 0,4 ; trois strates γ = 0,4 ; deux, γ = 0,2 ; trois, γ = 0,2) et **≤ 1 %** côté honnête
  (`part_variance_pA_entre_strates_*` des sorties) : le meilleur cas (+0,054) suppose une covariable qui explique 63 % de la dispersion du sujet saboté, et la garde n'est
  pas touchée. (d) L'étalonnage est exact ; s'il était estimé, des décalages estimés sur les unités mêmes de l'épreuve rendraient le processus non prévisible.
- Essai : lecture des `moments_tires` des 15 passages de strates (cellule K_h = 10, biais 0, 288 unités) : `commune-S2-g0.4 : pA_strates sab 0,941 ; part_var_v_strates
  0,027 ; fiche 1,000` ; `sujet-S3-g0.4 : pA_strates sab 0,627, hon 0,006 ; part_var_v_strates 0,215`. Calcul de la corrélation : formule ci-dessus.
- Correction : présenter les lignes « commune » comme **témoin de construction** (et dire pourquoi leur fiche brute est haute), ou les remplacer par une portée
  partielle (γ_A ≠ γ_B), seul cas où l'étalonnage a quelque chose à retirer ; écrire au § 3.2 les parts de variance de (c) ; si l'étalonnage par strate devait servir,
  préenregistrer des décalages fixés avant l'épreuve (pilote), jamais estimés sur ses unités.

### GD8-04 — Incertitude de graine : n80 est stable à moins de 1 % ; les puissances affichées ne sont pas des minorants

- **Gravité : moyenne** (le § 7 conclut trop prudemment pour n80, et pas assez pour les puissances).
- Fichier : rapport, lignes 22 (« une puissance affichée est un minorant »), 263 à 279 (§ 7), 304 (« 2,2 % ») ; script, lignes 1016 à 1028 (la dichotomie rend `haut`).
- Constat n80 : sur les points déjà évalués par la dichotomie (quatre graines, aucun tirage nouveau), une régression logistique binomiale en n ajuste bien
  (déviance par degré de liberté 0,93 à 1,15) et donne, cellule la plus exigeante : ρ = 0,17, seuil 40 : n80 = **276,7 ± 0,6** (graines séparées 275,6 ; 277,0 ; 276,2 ;
  277,6), contre 280 par dichotomie ; seuil 160 : 356,2 ± 0,4 contre 352 à 360 ; ρ = 0,05 : 197,3 ± 0,3 et 272,1 ± 0,3 contre 200 et 272 à 280. L'écart-type de graine
  est ≤ 0,6 unité (≤ 0,2 %) ; ce que le § 7 appelle « dispersion de graine » est l'arrondi de la dichotomie, qui rend la borne haute de son pas (biais de +0 à +8
  unités). L'addition « 4,0 % + 3,1 % = 7,1 % » compte deux fois la résolution. La marge 1,06 couvre largement la graine (et la borne de 6 % de GD2-07 est très
  prudente).
- Constat puissances : les puissances sont tronquées à trois décimales, ce qui borne l'**arrondi**, non l'erreur de Monte-Carlo (erreur type ≈ 0,008 à 0,85). Valeurs de la
  v8 à 288 unités dans cette cellule, graines et étiquettes différentes : 0,847 (passage), 0,8475, 0,8345, 0,826, 0,8485, 0,8115, 0,848, 0,8395 (compléments et points
  de dichotomie), 0,849, 0,852, 0,832 (rejeu, graines 4 à 6), 0,8305 à 0,8485 (huit graines, `cellule-contre-point-gd8-v1-sortie.json`) : moyenne ≈ 0,84. Le 0,847 est
  un tirage du haut de cette distribution. La réimplémentation indépendante donne en moyenne ≈ 0,83 (11 graines, `graines-cellule-pire-gd8-v1-sortie.json`,
  `independant-gd8-v1-sortie.json`) ; l'écart à la v8 n'est pas systématique : test apparié sur 21 graines (501 à 521, `test-ecart-gd8-v1.py`), retenue e-BH v8 0,8385 contre réimplémentation 0,8368, différence +0,0017 ± 0,0027 ; atteinte de 160 : +0,007 ± 0,004. La valeur centrale de la cellule est donc ≈ 0,838 (seuil 40) et ≈ 0,50 (seuil 160) ; le 0,847 annoncé est environ une erreur type au-dessus.
- Essais : `python3 -I -B ajustement-n80-gd8-v1.py <v8> ajustement-n80-gd8-v1-sortie.json` (sortie : `rho=0.17|retenue_ebh dichotomie : [280, 280, 280, 280] | ajusté
  n80 = 276.7 ± 0.6 (0.2 %), n90 = 315.2 ± 0.5, déviance/ddl 1.07`) ; `cellule-contre-point-gd8-v1.py` : même étiquette, la cellule et le point rendent la même valeur
  (0,847 = 0,847) ; graines 201 à 208 : moyenne cellule 0,8404, moyenne point 0,8399.
- Correction : remplacer au § 7 la mesure par graines (résolue à 8 unités) par l'ajustement de la courbe (n80 à l'unité près, avec son écart-type) ou rendre le milieu
  du dernier pas ; écrire « tronqué » sans « minorant », ou donner les puissances clés avec leur erreur type (≈ 0,008) et, pour les chiffres qui entrent au
  préenregistrement (0,847 ; 0,509 ; 0,980 ; 0,905), la moyenne sur plusieurs graines.

### GD8-05 — Écrêtage après étalonnage : sans effet ici ; critère de vérification réécrit après échecs, sorties échouées hors du dossier

- **Gravité : mineure.**
- Fichier : rapport, lignes 320 à 322 et 346 à 347 ; `verif-ebh-pole-v8.py`, lignes 65 à 70 et 218 à 241 ; script, lignes 877 à 878 et 918 à 919.
- Constat : la simulation écrête δ − g après l'étalonnage (`processus`), le juge exige g dans [−1 ; 1] ; pour le contraste, les deux conventions coïncident (v est
  écrêté dans les deux cas). Dans le périmètre vérifié (trois strates, γ = 0,4, ρ = 0,17, 288 unités), 2 × 10⁻⁶ à 7,8 × 10⁻⁵ des valeurs de garde sortent de [−1 ; 1] et la
  puissance des huit gardes est identique (différence 0,0 dans les huit sous-cas : lu dans `verif-ebh-pole-v8-sortie.json`, bloc `ecretage_etalonnage`). Le cas le plus
  décalé (deux strates, γ = 0,4 : ±0,2 sur le contraste) n'est pas dans le périmètre, mais il ne touche que le contraste, où les conventions coïncident. Réserves :
  (a) le critère a été **scindé après trois exécutions non conformes** (rapport, ligne 346) — c'est déclaré, mais c'est un critère écrit après lecture (règle R4) ;
  (b) les sorties échouées sont « conservées hors du dossier » : ni empreinte, ni chemin dans le dossier livré (règle R6).
- Correction : verser les quatre sorties échouées dans le dossier avec leurs empreintes ; au préenregistrement, si l'étalonnage par strate est retenu, écrire la
  convention (« écart étalonné écrêté à [−1 ; 1] avant le pari ») et noter que l'écrêtage par en bas d'un contraste étalonné relève légèrement sa moyenne (sens non
  prudent, ici ≤ 10⁻⁴ × 0,2).

### GD8-06 — Neuvième comparateur : « SUPPOSÉ » manque à plusieurs endroits ; l'hypothèse « honnêtes inchangés » n'est dite que dans le script

- **Gravité : mineure.**
- Fichier : rapport ; script, lignes 33 à 35.
- Constat : « SUPPOSÉ » accompagne l'écart 0,05 aux lignes 36, 209, 240 et 305, et dans `tableaux-v8.md` (T7, ligne 472). Il manque : tableau du § 5 (lignes 213 à 232,
  colonne « écart du 9ᵉ » = 0,05) ; ligne 245 (« s'il est proche de 0,05 ») ; § 6.3, ligne 256 (« à ≈ 0,05, ajouter +128 à +432 unités ») ; § 6.4, ligne 258 (« s'il
  est fort ») ; ligne 308 à 309 (« +128 et +432 (table du § 5, écart 0,05) »). Par ailleurs le modèle garde f_B9 = τ côté honnête (seul r_B9 change) : un comparateur
  « fort » qui alerte plus sur les sabotés alerte vraisemblablement plus aussi sur les honnêtes ; c'est écrit dans le script (« honnêtes inchangés »), non dans le rapport.
- Essai : `grep -n -i "neuvi\|9ᵉ\|fort" rapport-puissance-garde-delta-v8.md`.
- Correction : marquer « SUPPOSÉ » à chacune de ces lignes et dans l'en-tête de colonne ; écrire au § 5 « côté honnête inchangé (SUPPOSÉ) ».

### GD8-07 — La lecture de ρ côté sabotage suppose le même ρ côté honnête ; l'écart n'est pas borné

- **Gravité : moyenne.**
- Fichier : rapport, lignes 116 à 117 et 313 à 314 ; script, lignes 501 à 505 et 602 à 615 (une seule concentration κ pour f et r).
- Constat : l'hypothèse est déclarée (« SUPPOSÉ »), mais au seuil 160 la garde est un maillon (0,751 au pire à ρ = 0,17, table « où la fiche perd-elle ») et le côté honnête
  n'est pas lisible au pilote (écart-type 0,071 à 288 unités). Des faux positifs concentrés sur quelques unités honnêtes difficiles — vraisemblable — donneraient un ρ
  honnête supérieur au ρ saboté ; le script ne permet pas de le simuler (κ commune).
- Correction : un passage avec ρ honnête = 2 × ρ saboté (option à ajouter, refusée par défaut) pour borner l'effet sur n80 au seuil 160, ou l'écrire comme condition
  de validité de la table au préenregistrement.

### GD8-08 — Fiches nulles avec neuvième comparateur : repli silencieux

- **Gravité : mineure** (sans effet sur les passages de la v8, qui ont N = 0).
- Fichier : script, lignes 597 à 600 (`variante_nulle` ne transmet pas `ecart9`).
- Constat : avec `--ecart-contraste-neuvieme` et `--fiches-nulles`, les fiches nulles sont tirées sans le neuvième comparateur particulier, sans refus ni mention
  (règle R5 : aucun repli silencieux).
- Essai : `python -I -B simulation-puissance-garde-delta-v8.py --repetitions 100 --taux 0.01 --deltas 0.05 --biais 0 --lecture-ebh A --m 8,2 --sans-n80 --comparateurs 9
  --K 5 --K-s 10 --tailles 64 --ecart-contraste-neuvieme 0.05 --fiches-nulles 1` → code 0, aucun refus, `fiches_nulles` = 1 (`rejeu-v1/essai-nulle-neuf-gd8.json`).
- Correction : transmettre `ecart9` dans `variante_nulle`, ou refuser la combinaison.

### GD8-09 — Graines, manifestes, empreintes, versions (R9, R6, R12)

- **Gravité : mineure.**
- R9 : graines par `SeedSequence([graine, sha256(étiquette)])`, graines dérivées écrites par cellule, une version de Python et de numpy pour tous les passages :
  conforme. Manque : le **commit** (« non lu », par choix GD7-09) — compensé par l'empreinte du script, mais la règle demande le commit ; `precision-rho-pilote-v8.py`,
  `incertitude-graine-n80-v8.py`, `verif-sans-git-v8.py` et les scripts de tableaux n'écrivent **pas de manifeste** propre (graine et numpy dans la sortie pour le premier,
  ni journal ni manifeste pour le second). Reproductibilité : bit à bit sous numpy 2.4.6 (constaté sur 1 456 champs).
- R6 : conforme (206 compagnons, 35 empreintes du § 12, toutes vérifiées) ; réserve de GD8-05 (b).
- R12 : conforme (`-v8`, `-v8-v2` ; gabarit, constructeur et manifeste remplacés gardés).
- Correction : déclarer le commit de l'arbre au lancement (lu par l'appelant hors du script, ce que GD7-09 permet) ; un manifeste par exécution pour les scripts
  auxiliaires.

## Critère 1 — le modèle représente-t-il la dispersion combinée et la lecture côté sabotage ?

Oui, pour ce qu'il dit : sujet partagé par les huit comparateurs (une probabilité d'unité par côté, tirée d'une bêta d'espérance tenue et de corrélation intra-unité
ρ_A), comparateurs indépendants entre eux et du sujet (ρ_B), honnêtes et sabotés tirés à part (« lien coupé »), richesse mélangée sur quatre λ, fiche au minimum
des seize processus, lecture (A) par la règle e-BH (Benjamini-Hochberg sur les e-valeurs) à deux modes. La réimplémentation écrite depuis le seul texte retrouve les
composantes (gardes, contrastes, atteinte de 40 et de 160) aux erreurs de Monte-Carlo près ; la règle e-BH appliquée à mes trajectoires donne la même chose que la
fonction de la v8. Hypothèses dites : oui, pour l'essentiel (§ 10.1, « SUPPOSÉ ») ; non dites ou insuffisamment : GD8-03 (c), GD8-06, GD8-07, et le fait que c = 0
(aucune difficulté partagée) est le cas prudent.

## Critère 4 — la table est-elle utilisable telle quelle ?

Non (GD8-01) : marge de lecture correcte dans son principe (1,645 × écart-type côté sabotage, écarts-types simulés), monotonie respectée, mais règle indéfinie hors
de la petite zone ρ̂ ≤ 0,03 à 0,06, et tailles du texte données au ρ vrai. La marge 1,06 de graine est suffisante (GD8-04).

## Fichiers de cette contre-lecture

Tous dans `docs/notes/couche-2-preparation-v1/contre-lecture-garde-delta-v8/`, scellés (compagnon `.sha256`), inventoriés avec empreintes dans
`manifeste-contre-lecture-gd8-v2.json` (commandes, versions, graines, commit local au lancement `317f670853fcd29cff5a8b590782e2221abe32c6` ; le `-v1`, écrit avant les derniers essais, est gardé, incomplet, R12) :
`rejeu-gd8-v1.sh` et `rejeu-v1/` (sorties, journaux et manifestes des quatre rejeux, essai GD8-08) ; `comparer-rejeu-gd8-v1.py` (+ sortie) ; `independant-gd8-v1.py`
(+ sortie, graine 20261030) ; `graines-cellule-pire-gd8-v1.py` (+ sortie, graines 101 à 110) ; `cellule-contre-point-gd8-v1.py` (+ sortie, graines 201 à 208) ;
`test-ecart-gd8-v1.py` (+ sorties, graines 501 à 521) ; `ajustement-n80-gd8-v1.py` (+ sortie) ; `regle-table-lecture-gd8-v1.py` (+ sortie). Les trois rejeux de cellule
aux graines 4, 5 et 6 (§ GD8-04) sont dans `rejeu-v1/`.
