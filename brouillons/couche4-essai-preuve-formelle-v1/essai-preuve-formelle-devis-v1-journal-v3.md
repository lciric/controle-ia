# Journal — brouillon 3 du dessin et du devis de l'essai « preuve formelle contre suite bon marché » (couche 4, pas (b) de R-2199) — v3

- **Auteur** : même sous-agent rédacteur (Opus 5.5, `claude-opus-5-5`), session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`. Les journaux
  v1 et v2 restent intacts.
- **Ordre reçu de la mère** (message en cours de travail) : appliquer la vérification courte du brouillon 2 (`38e40d21…`, VL-01 à
  VL-08) avec ses décisions (VL-01 : critère par queue et par affirmation, grille avec Δ = 0, Δ = δ et le bord p₀₁ = 0, énumération
  exacte, score de Tango à valeurs critiques calibrées, formule vérifiée sur une source citée ou marquée `<<SOURCE_TANGO>>` avec repli,
  deux phrases corrigées ; VL-02 minuterie ; VL-03 somme des plafonds et enveloppe ; VL-04 A8, plafond pour le cas « tout item L à
  4 USD », aveu sur les 40 graines ; VL-05 intégrité intérieure, épreuve, ordre réseau, R2 par défaut ; VL-06 à VL-08) ; même consigne
  (`5403571b…`) et mêmes interdits ; brouillon 2 et `calculs-v2/` intacts ; sorties neuves sous `calculs-v3/` ; aucun commit.
- **Produit** : `brouillons/couche4-essai-preuve-formelle-v1/essai-preuve-formelle-devis-v1-brouillon3.md`
  (`717259ed1dfd5e4e9c591b3c7d22a4316ec1fe1195ea83bb887ca3f60fd2ac37`, scellé à 14:08:52 UTC) ; sous `calculs-v3/`, scellés :
  `calibrage_score_apparie_v1.py` (`ad0c1e2d…`), `sortie-calibrage-score-apparie-v1.txt` (`1a3bf7ee…`),
  `valeurs-critiques-calibrees-v1.json` (`fbd77a23…`), `calculs_devis_essai_v5.py` (`85a8fad1…`), `sortie-calculs-devis-v5.txt`
  (`5d1f1e2d…`), `retouches_brouillon3_v1.py` (`c18982c1…`), `sortie-retouches-brouillon3-v1.txt` (`ff38fa55…`),
  `table_brouillon3_v1.py` (`de04c13b…`), `sortie-table-brouillon3-v1.txt` (`d718c0da…`). Empreintes complètes : table du brouillon 3.
- Heures relevées par `date -u`.

## Chronologie

| Heure UTC | Fait |
|---|---|
| 13:58:22 | Vérification courte vérifiée (`38e40d21e60f7588233b3fda27b365c6a48abb97ecb9dd3a5ff94cb44ad73d8a`, égale à son compagnon) ; brouillon 2, journal v2 et les huit fichiers de `calculs-v2/` vérifiés intacts. |
| ≈ 13:58–14:00 | Vérification courte lue en entier (340 lignes, annexe et sorties comprises). Recherche, sans réseau, d'une source de la formule de Tango : aucun fichier du dépôt (`git ls-files`, `git grep` avec exclusions) ; le seul PDF où le mot apparaît (`docs/sources/pdf/anteriorite-P-041-v2/c7/2510.08240.pdf`, `55feef87…`, « The Alignment Waltz ») le cite pour un autre travail (« RL tango ») ; aucune bibliothèque installée ne l'implante (statsmodels absent, pas de R). Page de prix archivée de Gemini repérée (`docs/sources/prix/page-prix-gemini-api-20261108T054611Z.html`, `ad2140dd…`) et lue pour Gemini 4 Argon. |
| 14:02:14 | `calibrage_score_apparie_v1.py` écrit, corrigé (borne basse du maximum numérique pour Δ₀ < 0), lancé (6 secondes) : forme close contrôlée, erreurs exactes, valeurs critiques calibrées, issues exactes ; table des valeurs critiques écrite en JSON. |
| ≈ 14:03–14:05 | `calculs_devis_essai_v5.py` écrit et lancé : coûts unitaires identiques à la v4 ; A8 ; plafond de D-1b 578 ; phase 2 ; minuteries ; somme des plafonds et enveloppe ; sensibilité au prix d'Argon. 14:05:21 : les cinq fichiers scellés. |
| 14:05:43 | (fait de la mère) commit `331b41450` « Essai Lean brouillon 3 … EN COURS, NON SCELLÉS » : il contient les cinq fichiers de calcul déjà scellés. |
| ≈ 14:05–14:08 | `retouches_brouillon3_v1.py` (S01 à S33, puis S34 à S38 après relecture, relancé depuis le brouillon 2) ; `table_brouillon3_v1.py` ; contrôles : 0 défaut de tableau, 0 écart aux compagnons, aucun chemin du bac à sable, 20 marqueurs « À REMPLIR », 6 marqueurs `<<SOURCE_TANGO>>`. |
| 14:08:52 | Brouillon 3 scellé ; tout le dossier vérifié (`OK` partout). |
| (fin) | Présent journal écrit, puis scellé. |

## Application de la vérification courte

- **VL-01** : § 3.6 (puce « Méthode du préenregistrement », réécrite), § 1.6 (« Tests et bornes »), § 1.7 (sens des bornes ; phrase
  de C02 corrigée ; propriétés avec le score calibré), § 3.6 (issues et erreur de famille exactes), D-5 (i) (phrase corrigée), § 8 et
  § 9 (« À REMPLIR : SOURCE-TANGO »). **Source de Tango** : non trouvée ; formule écrite avec le marqueur `<<SOURCE_TANGO>>` ;
  **contrôle par dérivation** (bloc 0) : q de la forme close égal au maximum de vraisemblance sous contrainte calculé numériquement
  (écart maximal 6,01·10⁻⁹ sur 3 000 cas, dont Δ₀ négatifs) ; réduction exacte à McNemar pour Δ₀ = 0 ; **repli écrit** : statistique
  définie par ces principes, recalibrée par le même script. **Résultats exacts** (grille plus large que celle du vérificateur : tous
  les n de 40 à 150, discordance jusqu'à 0,80) : au z nominal, gabarit de Wald 0,0151 / **0,0506** / 0,0172 par classe pour « B > 0 »
  / « H < δ » / « B ≥ δ » ; Tango 0,0126 / 0,0142 / **0,0224** ; z* maximaux calibrés 2,2634 / 2,2939 / **2,5169** (le vérificateur,
  sur six effectifs et une discordance jusqu'à 0,60, trouvait 2,251 / 2,266 / 2,376 : même sens, valeurs plus sévères ici parce que la
  grille est plus fine en n et plus large en discordance).
- **VL-02** : A13 (minuteries de destruction 48 / 26 / 70 heures, cumul horaire, plafonds tenus à 1,30 USD l'heure) ; § 4.3 ; D-1a.
- **VL-03** : « engagement maximal » devient « somme des plafonds » (2 719) ; enveloppe au profil pire réaliste 3 252,40 à 3 865,00 ;
  le calcul du vérificateur (3 224,40 à 3 790,20, D-1b à 550, 30 % d'items litigieux) est reproduit au bloc 5 de la v5.
- **VL-04** : A8 réécrit (formule G = 10 + ⌊(P − D − R − H) / c⌋, réserve de A7 et charges hors graines retranchées ; « 20 items de
  contrôle » puis deux blocs de 5 graines ; G < 40 ⇒ arrêt ; coupure de A7 sous 40 ⇒ pilote descriptif) ; plafond de D-1b **578**
  (577,66, retrouvé) ; aveu sur les 40 graines (D-1b (iii)) et conséquences ; pistes chiffrées (réserve 12, lecture nue abandonnée).
- **VL-05** : puce « Intégrité à l'intérieur de la machine » (§ 4.5) ; artefacts de l'ancienne garde déclarés sans objet et remplacés
  par une épreuve qui a un sens ; ordre « réseau ouvert pour l'installation, puis coupé et éprouvé avant tout code écrit par un
  modèle » ; A1 ; **repli R2 retenu par défaut** dans le texte (§ 2.7 ; § 9).
- **VL-06** : bornes des fausses alertes dites unilatérales à 97,5 % (queue 0,025) ; borne basse de A9 précisée ; famille limitée aux
  affirmations sur Δ ; lecture de O2 précisée (H(φ_L) > φ_max n'établit pas φ_L > φ_max).
- **VL-07** : (a) paragraphe de C08 remplacé par une phrase datée ; (b) « devis central à refaire » remplacé ; (c) plafond indicatif de
  la phase 2 porté à 1 950 (1 944 avec 60 % d'items litigieux et la réserve) ; (d) fourchettes de tirage remplacées par le calcul exact.
- **VL-08** : table des empreintes avec les quatre scripts de retouche de `calculs-v2/`, R51 décrite (retouche à la main, sans script),
  composition du brouillon 2 et du brouillon 3 écrite sous la table.

## Écarts au texte des couples de la contre-lecture 1 (tous sur décision de la mère ou constat de la vérification courte)

1. **C09** : la règle « la méthode dont la couverture minimale sur la grille est la plus proche de la couverture nominale par le
   haut » est **remplacée** (VL-01 : elle désignait un ensemble vide) par le critère par queue et par affirmation, à valeurs critiques
   calibrées par énumération exacte. La puce entière est réécrite.
2. **C08** : le paragraphe ajouté (déjà retitré au brouillon 2) est remplacé par une phrase datée (VL-07 a).
3. **C04** : « devis central à refaire » devient « devis refait en v4, « central » retiré » (VL-07 b).
4. **C02** : « trois fois sur cent » est précisé « à 95 %, au gabarit du brouillon 1 », avec la valeur exacte à 97,5 % (VL-01).
5. **C11** : « borne basse à 95 % » est précisé « borne basse unilatérale à 97,5 % … borne basse de l'intervalle bilatéral à 95 % » (VL-06).

## Prix d'Argon (constat nouveau, sans effet sur les chiffres du devis)

La page archivée du 8 novembre (`ad2140dd…`) donne pour Gemini 4 Argon, au tarif standard payant : 2 / 10 USD par million de jetons
d'entrée / sortie jusqu'au 30 novembre 2026, 4 / 20 à partir du 1er décembre 2026 (cache 0,10 puis 0,20). Le devis garde 10 / 50
(prudent, comparabilité avec les chiffres vérifiés, dont 578) ; sensibilité au bloc 6 de la v5 (pilote ordinaire 309,47 au lieu de
337,42 ; plafond minimal pour 40 graines au cas « tout à 4 USD » 553,86 au lieu de 577,66).

## Fichiers du bac à sable (non versés, non cités par la table)

`/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/redacteur-devis-couche4/pdf-tango/2510.08240.txt` :
texte extrait du PDF du dépôt pour chercher le mot « tango » (contexte sans rapport). Rien d'autre de neuf.

## Exposition, cloison, interdits

- Lus : vérification courte (en entier) ; brouillon 2 (mon texte) ; une page de prix archivée (`docs/sources/prix/`) ; le texte d'un
  PDF de `docs/sources/pdf/` cherché pour un seul mot ; `git ls-files`, `git grep` avec exclusions, `git log`, `git ls-files` sur le
  dossier de sortie (lecture). Aucun chemin des interdits communs ouvert ; aucune recherche récursive non exclue.
- Aucun appel de modèle ni d'interface ; aucun réseau ; aucune installation ; aucune dépense ; **aucune écriture git** (les commits
  `b83345b22`, `a0e88b833` et `331b41450` sont de la mère). Aucun refus rencontré. Aucune valeur de sonde de la course 7a.
- Tous les scripts lancés par `.venv/bin/python -I -B` (aucun `__pycache__` écrit ; vérifié).
