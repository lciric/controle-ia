# Contre-lecture (R2) : préenregistrement « mesure unanime » v5 et son script, lecture entière

**Verdict : à corriger en v6.** Deux constats rendent une lecture discutable. (1) Le script ne calcule pas l'« excès apparié
de M4 » que définissent le texte et la table : il calcule la différence des médianes, alors que le texte et la table prennent la médiane des différences par sonde (CV5-2 ;
l'écart est petit, mais le texte écrit « le même que le script »). (2) M2 ter garde une seconde lecture conditionnée par r₀ dans
la colonne « réfutation » (CV5-1, reste de CV4-1). Trois issues de M2 ter attribuent encore plus que ce qui est mesuré (CV5-3). Le
reste est mineur. CV4-2 est fermé sur le fond : l'excès a le même calibrage et un rééchantillonnage apparié, ce qui annule le
faux « confirmé » par M3 « fragile ». Le mélange à pas fixé fait ce qu'il dit. Les quatorze gardes et la nouvelle garde sur le
chemin réel tiennent. Toutes les empreintes sont conformes.

- Contre-lecteur : sous-agent neuf Opus 5.5. Je n'ai écrit ni le préenregistrement, ni le script, ni la table, ni aucun des
  rapports précédents.
- Début : 2026-10-28 00:47:35 UTC (`date -u`). Fin : voir la dernière ligne. Les heures d'`ls` sont en heure de Paris
  (UTC + 1).
- Processeur seul. Je n'ai ouvert ni lu `donnees/20261019-230011-p3-reel/scores-p3.npz` ni aucun fichier de `donnees/`. Je
  n'ai pas calculé son empreinte, et l'empreinte `968414fc…` n'est donc **pas** vérifiée par moi. Je n'ai modifié aucun fichier
  du dépôt et je n'ai fait aucun commit. J'ai lancé le script v5 en `--test-gardes`, en `--synthetique` (reproduction de l'essai)
  et en mode réel **sur le fichier synthétique** que le test des gardes écrit dans mon dossier (`gardes-cv5/`). Je l'ai aussi
  importé sans modification dans mes simulations.

## Empreintes lues

| fichier | empreinte | état |
|---|---|---|
| `preenregistrement-mesure-unanime-v5.md` | `29f91ff3ac7dfff277b051e1fe2d99447fe2a569ddba6527b7de546935270320` | objet de la contre-lecture ; identique dans `76298f61` (HEAD) ; pas encore de compagnon (normal : il est créé au scellement) |
| `preenregistrement-mesure-unanime-v4.md` | `5718717133a877a2210036d3b28ec1904ce431e8478f530d38c5ca1e67dde27e` | conforme à l'en-tête ; v3 `3a52f304…`, v2 `e6369f43…`, v1 `7158affc…` conformes |
| `analyse_fausses_alertes_v5.py` | `8ceda031315e9304901e0f7682c242a0bcd37da6cbe3e1696699689b3bda72ca` | conforme ; compagnon conforme ; identique dans `f8872263` (cité) |
| `sortie-synthetique-essai-v5.json` | `b4d89904974f1837e5a62a6c951c05eead34dbbbd44bbbde5243082eed106eda` | conforme ; compagnon conforme ; dans `f8872263` ; **reproduit à l'octet près** par `--synthetique --tirages 5 --bootstrap 300` (même empreinte) |
| `table_m2bis_m4_v5.py` | `1459f54997b484362dd0cec5e0e99e50e101a950f12b99f48073bf42efeec509` | conforme ; compagnon conforme ; dans `f8872263` |
| `table-m2bis-m4-v5.json` | `95fdbac931cc8357a3bb808f02e87719548bd622af1d222d5c8f60448e86a53d` | conforme ; compagnon conforme ; dans `f8872263` |
| `contre-lecture-v4/rapport-…-v4.md` | `ef6b87704b00bd776608313adcb160984e3378109592930c0e5d17c88d7d4f86` | conforme ; compagnon conforme |
| `contre-lecture-v1/rapport-…-v1.md` ; `complement-v2.md` ; `contre-lecture-v3/rapport-…-v3.md` | `5d47ae52…bf2d` ; `e5ca74bb…f7dc` ; `0fb0734a…214c` | conformes |
| `src/controle_ia/bases/sequentiel.py` | `35a0983404d7a10d0bb736fa37307a108501785a207c27346be1cd02bab11ba8` | conforme ; « 0,21 à 0,35 » aux lignes 7 et 8 |
| synthèse `docs/notes/collisionneur-mesures-fortes-v1/synthese-mesures-fortes-v1.md` | `bed9107b…885e` | conforme **sur `origin/main`** (absente du `main` local) |
| `…/pari-de-signe/conception-pari-de-signe-v3.md` | `1518a12f…db14` | conforme ; ligne 117 : « dérive de composition calibrage → épreuve » |

Aucun espace réservé « ⟨…⟩ » dans le texte. Le seul gabarit est `<commit du scellement>` (ligne 185), et c'est voulu.

## 1. Fermeture de CV4-1 à CV4-6

| constat | état | où et pourquoi |
|---|---|---|
| CV4-1 (deux définitions de M2 ter) | **à moitié** | Le Seuil n'a plus qu'une définition, en cinq issues ordonnées (lignes 159 à 165), et « (r₀ ≤ 0,3) » a disparu des critères (ligne 197). En revanche, la colonne « réfutation » de M2 ter (ligne 97) garde une **condition sur r₀** (« ≤ 0 avec r₀ ≥ 0,3 ») et une **sixième étiquette** (« la dépendance ne se voit pas dans Ville à cette longueur »), qui recouvre les issues (1), (2) et (5). L'Hypothèse (lignes 59 et 60) garde aussi l'ancienne lecture : « s'il dépasse α, la dépendance naturelle des scores de P3 suffit ». Voir CV5-1. |
| CV4-2 (faux « confirmé » de M4 par M3 « fragile ») | **fermé sur le fond, à moitié dans le code** | Le mécanisme est juste. Le terme à τ = 0 et le bras M4 ont exactement le même calibrage : mêmes plis, même permutation, Xcal = X dans les deux cas, donc mêmes μ₀, σ et seuils (script, lignes 185, 452 et 456). Le rééchantillonnage tire le même jeu d'épisodes pour les deux termes (lignes 501 à 503). Un défaut de niveau commun aux deux termes s'annule au premier ordre. Mais le script calcule **médiane(M4) − médiane(τ = 0)** (lignes 492, 499 et 505), alors que le texte (lignes 82 à 84 et 140 à 143) et la table (lignes 62 et 69) définissent **médiane sur les sondes de (M4 − τ = 0) par sonde**. Ce n'est pas « le même excès que le script » (ligne 23). Voir CV5-2. |
| CV4-3 (ligne placebo non bornée) | **fermé** | Critères, ligne 206, et prédictions, ligne 103 : l'audit est borné aux 24 cellules de M3 et au maximum conforme du bras M4 ; le reste est rapporté avec le r₀ des deux groupes. |
| CV4-4 (attributions trop larges) | **à moitié** | (i) est fermé : l'issue (3) dit « marges et dépendance » quand le mélange dépasse α. (ii) est fermé pour le code : `melanger_actions_pas_fixe` (lignes 136 à 145) garde les marges par pas et le masque, détruit la dépendance (r₀ 0,39 → 0,008 ; réponse 4), et l'issue (4) exige la différence au mélange à pas fixé. Il reste que l'issue (3) dit « dépendance » sans regarder le mélange à pas fixé, et que l'issue (4) n'exige pas que Ville sur le mélange à pas fixé soit ≤ α, ce qui est l'analogue exact de (i). Une nouvelle issue (2) attribue aussi à tort (CV5-3). |
| CV4-5 (empreintes de la table) | **fermé** | Les empreintes de la table et de son script sont dans l'en-tête (ligne 22). Les compagnons du script, de la table, de sa sortie et de l'essai existent, et `sha256sum -c` passe sur les quatre. |
| CV4-6 (restes) | **fermé** (deux restes infimes) | La Métrique donne bien (K + 1 − rang)/(K + 1) (lignes 115 et 116). Les docstrings du script sont corrigées (lignes 21, 36, 40 à 44) et la table dit « code v5 », comme le texte (ligne 58). « Max ≈ 0,02 (0,4 à 0,5 L) » est écrit (lignes 87, 101 et 103) ; la table donne 0,38 à 0,52 L. La phrase en double a disparu. `--empreinte-attendue` figure dans la commande (1) et le code l'impose. `--tirages` et `--bootstrap` sont fixes. « À tout r₀ » est écrit. `--longueurs-json` est en place. Le renvoi à la simulation de la v4 est fait (lignes 245 à 247). « Quinze entrées » est juste. J'ai **vérifié en lançant** le refus de l'empreinte, des tirages, des rééchantillonnages et d'un E qui ne correspond pas aux longueurs (réponse 5). Restes : CV5-6. |

## 2. Réponses aux points du brief

**Point 2 : M2 ter.** Les issues sont des « sinon » successifs. La règle est donc exhaustive et sans recouvrement par construction : sur une
grille de 432 combinaisons, chaque combinaison tombe dans une issue et une seule (`sortie-verif-cv5-issues-v1.json`). Chaque issue a sa
ligne dans les critères (lignes 196 à 199 et 202). Dans le Seuil, r₀ n'est une condition nulle part. Il l'est encore dans la
colonne « réfutation » de la table des prédictions (CV5-1). Deux remarques : la valeur de Ville sur le mélange à pas fixé
n'entre dans aucune issue (CV5-3), et trois issues ont une attribution plus large que la mesure (CV5-3).

**Point 3 : excès apparié de M4.**
- **Même calibrage** : oui (voir CV4-2).
- **Rééchantillonnage apparié sur les épisodes** : oui.
- **Appariement par sonde** : non. Le script soustrait des médianes. J'ai reproduit l'essai synthétique avec les graines du
  script et je retrouve exactement 0,085, 0,0467 et 0,0383. La médiane des différences par sonde y vaut 0,0370. Sur trois mondes
  à 30 sondes hétérogènes (r₀ de 0 à 0,6), l'écart entre les deux définitions vaut −0,0047, −0,0003 et +0,0017. Les intervalles
  sont voisins (`sortie-verif-cv5-exces-v1.json`).
- **Fermeture du faux « confirmé »** : le seuil « excès > 0,02 et borne basse > 0 » le ferme.
  - Un défaut de niveau δ, commun aux deux termes, ne laisse qu'un résidu de second ordre. Mon estimation, par le rapport des
    densités au seuil (calcul, non simulé) : environ 0,2 δ, soit environ 0,01 pour δ = 0,05.
  - Ce résidu ne crée pas un excès à partir de rien.
- **Nouveau faux « confirmé »** : je n'en trouve pas.
- **Faux blocage** : je n'en trouve pas non plus. Un défaut qui abaisse le niveau abaisse aussi les deux termes, et la lecture va
  vers « non concluant », ce qui est prudent.

**Point 4 : mélange à pas fixé** (`sortie-verif-cv5-pas-fixe-v1.json`, 12 sondes, 5 mélanges, 2 mondes par scénario).
- **Marges par pas et masque gardés** : oui. C'est aussi ce que vérifie le test du script.
- **Dépendance intra-épisode détruite** : oui. Avec un effet épisode à r₀ = 0,4 et sans dérive, r₀ d'origine vaut 0,39 et 0,41 ;
  sur le mélange à pas fixé, 0,008 et −0,005 ; sur le mélange complet, −0,001. Ville vaut 0,067 et 0,083 sur les scores
  d'origine, 0,003 et 0,005 sur les deux mélanges. Les deux différences sont égales à 0,002 près.
- **Dérive linéaire avec le pas, sans effet épisode** : r₀ du mélange à pas fixé ≈ r₀ d'origine. Avec masques dispersés, −0,091
  contre −0,095, et −0,088 contre −0,087 ; le mélange complet ramène r₀ à ≈ 0. La dérive survit donc bien. Réelles moins mélange
  à pas fixé ≈ 0, comme attendu.
- **Ce qui n'était pas attendu** : réelles moins mélange **complet** est aussi ≈ 0 (de −0,007 à +0,007). Une dérive linéaire
  de la moyenne ne fait pas monter Ville : la standardisation est globale et les sommes cumulées se compensent. L'issue (5) ne
  se déclenchera donc guère pour une simple dérive de moyenne. Ce n'est pas un défaut.
- **r₀ biaisé par la dérive** : la dérive biaise r₀ vers le bas. À r₀ = 0,4 avec une forte dérive (β = 0,6 par pas), r₀ mesuré
  vaut 0,18 et 0,15. Or r₀ conditionne M4 et M2 bis (CV5-4).

**Point 5 : gardes.**
- `--test-gardes` sort **quinze entrées** : quatorze gardes et `correlation_saine` = 0,171. Aucune garde ne dort
  (`sortie-test-gardes-v5.json`).
- **`verifier_scores_invalides` sur le chemin réel** : la garde est appelée en tête de `un_passage` (ligne 176).
  - Sur un artefact passé à `un_passage` lui-même, elle refuse.
  - Pendant `main()` en mode réel, sur le fichier synthétique (3 réelles, 2 placebo, 20 tirages, 2 000 rééchantillonnages), elle
    est appelée **705 fois**, soit une fois par passage : 5 × (40 + 61 + 40) (`sortie-verif-cv5-chemin-reel-v1.json`).
- **Refus vérifiés en lançant** (`sortie-refus-mode-reel-v5.txt`) :
  - `--effectifs-seulement` sans empreinte, ou avec une empreinte vide ;
  - une empreinte fausse ;
  - `--tirages 5`, `--bootstrap 300`, `--tirages 5` avec `--effectifs-seulement` ;
  - l'absence de `--commit`.
  - Les valeurs par défaut écrites explicitement passent.
  - La table refuse `--E 50` avec 60 longueurs (`sortie-table-repertoire-v5.txt`).

**Point 6 : chiffres cités.** Tous ceux que j'ai recalculés sont conformes :
- 0,395 ; 0,0725 ; 0,077 ; 2/40 ; K = 39, rang 38 ;
- table v5 : Ville à τ = 0 (0,000 ; 0,033 ; 0,083 ; 0,133) ; Ville à τ = 2 (0,1375 à 0,1521) ; M2 bis (+0,138 ; +0,104 ;
  +0,065 ; +0,019) ; excès (0,143 ; 0,073 ; 0,027 ; 0,006) ; quantité brute (0,194 ; 0,124 ; 0,075 ; 0,0545) ; maximum (0,019 à
  0,026) ;
- essai v5 : « +0,03 pour les deux » (0,030 et 0,030 ; r₀ médian 0,201) ; descriptif ≈ 0,25 (0,23 à 0,27) ;
- marges de la contre-lecture v3 : 0,005 ; 0,016 ; 0,041 (ce sont des **moyennes** sur 360 couples, pas des médianes) ;
- simulation de la v4 : 340 mondes à τ = 0 ; 12 + 48 = 60 mondes sur les 24 cellules ; « fragile » à tort de 0 à 8 %.

Écart relevé : l'essai synthétique v5 donne une quantité de M4 de 0,085 et un excès de 0,038 à r₀ = 0,20. La table donne
0,124 et 0,073 à r₀ = 0,2. L'écart est dans la tolérance de ± 0,05, et l'essai n'a que 5 tirages communs à toutes les sondes : un
seul monde, à variance forte. C'est un essai du code, pas une prédiction ; je le note sans constat.

## 3. Constats

### CV5-1 : M2 ter garde une seconde lecture conditionnée par r₀ (moyen ; reste de CV4-1)

- **Où** : la colonne « réfutation » de M2 ter (ligne 97) dit : « différence réelles moins mélange à pas fixé ≤ 0 avec r₀ ≥ 0,3 →
  “la dépendance ne se voit pas dans Ville à cette longueur”, rapporté ». L'Hypothèse M2 (lignes 59 et 60) dit : « s'il dépasse
  α, la dépendance naturelle des scores de P3 suffit à invalider Ville-sous-indépendance ».
- **Problème** : le Seuil promet « une seule définition, r₀ rapporté et jamais condition ». La colonne « réfutation » ajoute
  une sixième étiquette, conditionnée par r₀ et lue sur une **valeur ponctuelle**, alors que les issues lisent des **bornes
  basses**. Elle recouvre trois issues. Si la différence au mélange complet est > 0, que celle au mélange à pas fixé est ≤ 0 et
  que r₀ = 0,4, le Seuil dit (5) « dérive de pas » et la colonne dit « la dépendance ne se voit pas » : ce sont deux lectures
  opposées du même cas. La phrase de l'Hypothèse est la définition de la v3, que le Seuil a remplacée.
- **Correction** :
  - Colonne « réfutation » de M2 ter : « aucune réfutation formelle ; l'issue est celle du Seuil (cinq issues) ; r₀
    rapporté ».
  - Lignes 59 et 60 : « s'il dépasse α, le Seuil dit pourquoi (cinq issues : marges, structure, dépendance, dérive) ».

### CV5-2 : l'excès apparié du script n'est pas celui du texte ni de la table (mineur à moyen ; reste de CV4-2)

- **Où** :
  - script, lignes 492 et 499 (`q`, `q0`), 505 (`"exces": q - q0`), 503 (rééchantillonnage) et 507 (placebo) ;
  - texte, lignes 23, 82 à 84, 101 et 140 à 143 (« par sonde … ; médiane sur les sondes », « le même que le script ») ;
  - table, lignes 62 et 69 (médiane des différences par couple monde-sonde).
- **Problème** : le script soustrait deux médianes au lieu de prendre la médiane des différences par sonde. L'appariement porte
  sur les épisodes, pas sur les sondes. Les deux quantités diffèrent de −0,0047 à +0,0017 dans mes quatre mondes. Cela ne
  change aucune lecture loin du seuil de 0,02, mais deux définitions coexistent pour un verdict, et l'appariement par sonde que
  le texte revendique n'est pas fait.
- **Correction** (au choix ; la première de préférence) :
  - (a) Dans le script, calculer la différence **par sonde**, puis sa médiane, pour la valeur ponctuelle, le rééchantillonnage
    et le placebo, par exemple `np.median(taux_bras − taux_0)` avec `taux_*` le vecteur par sonde de `quantite_m4` avant la
    médiane. Puis relancer l'essai synthétique et mettre à jour les empreintes.
  - (b) À défaut, écrire « différence des médianes » dans le texte et la table, et refaire la table.

### CV5-3 : trois issues de M2 ter attribuent plus que la mesure (mineur à moyen ; suite de CV4-4)

- **Où** : Seuil, issues (2), (3) et (4) (lignes 161 à 164) ; critères, lignes 196, 198 et 202.
- **Problème** (les trois cas sont dans `sortie-verif-cv5-issues-v1.json`) :
  - **(2) « marges seules »** se lit sur une borne basse ≤ 0 de la différence au mélange, **même quand Ville sur le mélange
    est ≤ α**. Exemple : réelles 0,07, mélange 0,005, intervalle de la différence qui touche 0. Le critère conclut alors « par
    la **forme** des scores, non par la dépendance ; la standardisation gaussienne est en cause », alors que le mélange
    lui-même ne dépasse pas α. C'est une attribution tirée d'une absence de preuve.
  - **(3) « marges et dépendance »** ne regarde pas le mélange à pas fixé : la « dépendance » peut y être une dérive de pas.
    Cela contredit la logique que la v5 adopte en (4) et (5).
  - **(4) « dépendance naturelle suffisante »** n'exige pas que Ville sur le mélange à pas fixé soit ≤ α. Si la dérive de pas
    pousse déjà Ville au-dessus de α, la dépendance ne « suffit » pas seule. C'est l'analogue exact de CV4-4 (i), que la v5 a
    accepté pour le mélange complet.
  - Ces cas sont peu probables avec des marges gaussiennes : quand Ville réelles > α, il faut r₀ ≳ 0,3, et la différence vaut
    alors 0,05 ou plus. Ils ne sont pas exclus avec des marges asymétriques et une dépendance faible. Ce sont des étiquettes
    rapportées, pas une porte. Le critère (4) dit toutefois « résultat sur P3 ».
- **Correction** : garder l'ordre (la règle reste exhaustive) et préciser :
  - (2) « marges seules » si la borne basse est ≤ 0 **et** que Ville sur le mélange est > α ; sinon « **non attribuable** »
    (ni les marges ni la structure établies ; rapporté avec les deux différences).
  - (3) « marges et structure intra-épisode » ; « marges et dépendance » seulement si la différence au mélange à pas fixé a
    aussi une borne basse > 0.
  - (4) « suffisante » si, en plus, Ville sur le mélange à pas fixé est ≤ α ; sinon « **dérive et dépendance** ».
  - Ajouter les lignes correspondantes aux critères.

### CV5-4 : r₀ est biaisé par une dérive avec le pas, et le r₀ du mélange à pas fixé n'est pas « ≈ 0 » dans ce cas (mineur)

- **Où** : Métrique, ligne 136 (« r₀ du mélange à pas fixé rapporté (attendu ≈ 0) ») ; r₀ conditionne M4 et M2 bis (lignes 99,
  101 et 157) et sert à interpoler la table.
- **Problème** : la corrélation intraclasse compte la dérive dans la variance intra-épisode.
  - Simulation, dérive seule et masques dispersés : r₀ = −0,09, gardé par le mélange à pas fixé.
  - Simulation, r₀ = 0,4 avec une forte dérive : r₀ mesuré 0,15 à 0,18.
  - « Attendu ≈ 0 » n'est vrai que sans dérive. Une dérive réelle ferait lire M4 « lisible » à tort, ou ferait interpoler la
    table au mauvais r₀.
- **Correction** :
  - Écrire « attendu ≈ 0 sans dérive ; un r₀ du mélange à pas fixé loin de 0 signale une dérive qui biaise r₀ ».
  - Rapporter aussi r₀ sur les scores **centrés par pas** (moyenne de chaque pas retirée), sans en faire une condition.
  - Définir « pas » comme l'indice `pas` des données (brut, invalides compris), pas comme le rang parmi les actions valides.

### CV5-5 : les commandes du Plan mêlent deux dossiers de travail (mineur ; l'échec est bruyant, rien n'est silencieux)

- **Où** : Plan, lignes 178 à 187.
- **Problème** :
  - `donnees/…` est relatif à la racine du dépôt.
  - `table_m2bis_m4_v5.py` importe le script par `sys.path.insert(0, ".")`. Sous `-I`, il ne marche que lancé depuis le
    dossier du préenregistrement : lancé depuis la racine, il donne `ModuleNotFoundError` (vérifié, `sortie-table-repertoire-v5.txt`).
  - `-I` ignore aussi `PYTHONPATH`.
- **Correction** : écrire le dossier de travail de chaque commande, ou des chemins absolus. Par exemple, tout lancer depuis le
  dossier du préenregistrement avec `--reel /home/claude/canal-conv-audit-n04/donnees/20261019-230011-p3-reel/scores-p3.npz`,
  et `effectifs-reel-v5.json` écrit dans ce même dossier.

### CV5-6 : restes (mineur)

- Plan, « Cellules » (ligne 175) : ajouter « + 8 du mélange à pas fixé ».
- Hypothèse M3 (lignes 75 et 76) : la liste « n'en font pas partie » doit nommer aussi le mélange à pas fixé.
- En-tête (lignes 18 à 21) : le détail des gardes ne compte pas comme le code. Le code a cinq cas sains (dont le chargement
  sain et E sain), quatre artefacts de calcul (dont K trop petit), trois artefacts de chargement, E minimal et la corrélation
  sur scores constants : 14 au total. Le texte omet le chargement sain et compte K deux fois. Le total, 15 entrées, est juste.
- Manifeste : le nombre de rééchantillonnages n'y figure pas. L'essai « 300 rééchantillonnages » n'est vérifiable que par
  reproduction. Je l'ai faite, et l'essai est identique à l'octet près, empreinte `b4d89904…` comprise. Ajouter `"bootstrap": args.bootstrap` au manifeste.
- Docstring de `un_passage` (lignes 172 à 174) : « la forme des marges se rapproche de la gaussienne ; seule la structure
  intra-épisode change ». La seconde moitié contredit la première ; écrire « la structure intra-épisode change, et la forme
  des marges un peu ».
- Hypothèse M2 (ligne 64) : « 0,005 gaussien, 0,016 Student, 0,041 lognormal » sont des **moyennes** de la contre-lecture v3.
  Le dire, puisque la lecture porte sur des médianes. Pour le mélange moyenné sur 20 permutations, la moyenne est le bon ordre
  de grandeur.

## Mes scripts et sorties (ce dossier, chacun avec un compagnon `.sha256`)

| fichier | contenu |
|---|---|
| `verif_cv5_v1.py` | parties `exces` (excès du script contre le texte et la table), `pas_fixe` (dérive et dépendance), `issues` (grille des cinq issues) ; script v5 importé sans modification ; graines `SeedSequence(2810202605, spawn_key=(partie, scénario, monde))` |
| `sortie-verif-cv5-exces-v1.json`, `sortie-verif-cv5-pas-fixe-v1.json`, `sortie-verif-cv5-issues-v1.json` | leurs sorties |
| `verif_cv5_chemin_reel_v1.py`, `sortie-verif-cv5-chemin-reel-v1.json` | garde des actions invalides : refus par `un_passage`, 705 appels pendant `main()` en mode réel sur le fichier synthétique |
| `sortie-mode-reel-sur-synthetique-v5.json` | la sortie de ce mode réel (fichier synthétique, 3 + 2 sondes) |
| `sortie-test-gardes-v5.json` | `--test-gardes` du script v5 (15 entrées) |
| `sortie-effectifs-synthetique-v5.json` | `--effectifs-seulement` sur le fichier synthétique (E = 60, K = 39 dans les dix plis, L = 0,05) |
| `sortie-refus-mode-reel-v5.txt`, `sortie-table-repertoire-v5.txt` | refus du mode réel et de la table, vérifiés en lançant |
| `sortie-synthetique-reproduite-v5.json` | `--synthetique --tirages 5 --bootstrap 300`, comparé à l'essai v5 |
| `gardes-cv5/scores-synthetique-gardes.npz`, `gardes-cv5/scores-synthetique-petit.npz` | fichiers synthétiques écrits par le test des gardes |

Interpréteur `/opt/venv-essaim-sim-v1/bin/python -I -B`, numpy 2.5.4.

Empreinte de ce rapport : dans `rapport-contre-lecture-mesure-unanime-v5.md.sha256`, à côté (un fichier ne peut pas contenir
sa propre empreinte).

Fin : 2026-10-28 01:00:38 UTC (`date -u`).
