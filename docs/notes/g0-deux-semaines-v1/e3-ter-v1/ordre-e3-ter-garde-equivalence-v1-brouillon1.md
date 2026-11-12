# Ordre d'épreuve E3 ter — galop d'essai de la garde d'équivalence (99ᵉ centile) sur une carte, v1, brouillon 1

- **Statut** : brouillon de la session mère (`session_016QhUrrLeN21G7Z9KZobE42`), 8 novembre 2026 ≈ 14:20 UTC. **Non scellé, non commis, aucune ligne de GO encore** : la mère relit, remplit les `<<À VÉRIFIER>>`, crée la ligne de GO (devis § 8) sous l'autonomie GO-2026-11-08-05, puis remet l'ordre à une fille d'exécution.
- **Déclencheur** : point E3-6 du compte rendu d'E3 bis (R-1769, R-1784 B1) : la garde d'équivalence version 3 (99ᵉ centile, tolérance 0,2) **n'a contrôlé aucune action** sur la carte à E3 bis ; le contre-lecteur de l'ordre de course (couple O2) exige que la mère règle ce point avant toute création d'instance de la course (marqueur `<<REGLEMENT_E3_6>>`). Mot de Lazar, session mère, 8 novembre ≈ 14:05 UTC, verbatim : « (b) exiger d'abord un galop d'essai plus grand qui l'exerce — un run d'instance de plus (quelques USD, quelques heures), puis relecture. : go ».
- **Nature** : galop d'essai (R5) d'une garde d'arrêt, **sur un cas sain et sur deux artefacts**. Aucune donnée décisive n'en sort : rien de ce run n'alimente une lecture de T0.6, de P3 ou de G0. Les sondes, aires, coûts et tests croisés qu'écrit la chaîne ne sont **pas lus** (§ 4).

## 0. Pourquoi un galop, et pourquoi E3 bis n'a rien contrôlé

La garde tire, **par tâche**, un générateur neuf (`g["tache/<identifiant>"]`) : les pas contrôlés sont les mêmes pour toutes les conditions et tous les états d'adaptateur. À E3 bis (4 tâches, T = 4), il n'y avait donc que **16 paires (tâche, pas) indépendantes**, tirées à 5 % : probabilité qu'aucune ne soit retenue = 0,95¹⁶ ≈ **0,44**. Le résultat « 0 action contrôlée dans les six états » est donc l'issue la plus probable du tirage, pas un défaut du code ; mais il laisse la garde version 3 (99ᵉ centile) **jamais exercée sur une carte, à aucune dose**, alors que la course (64 tâches, T = 10 : 640 paires, ≈ 32 contrôlées, probabilité de moins de 10 ≈ 10⁻⁶) la jouera à dose 1 dans tous les états.

Ce que la garde fait (`src/controle_ia/harnais/episode.py`, branche `prep/t06-course-v12`, `7822a65b`) : pour chaque action retenue, (1) **équivalence** : les activations captées pendant la génération et celles d'une passe unique sur l'épisode complet doivent coïncider à chaque couche, 99ᵉ centile de l'écart < tolérance, sinon `GardeArret` immédiat (« génération ≠ passe unique ») ; (2) **contrôle négatif de phase** : décalée d'un jeton dans la zone générée, la même comparaison doit **dépasser** la tolérance pour ≥ 95 % des actions comparables (≥ 4 positions) ; sous 10 actions comparables la phase est « non concluant » et rien ne s'arrête. Le galop doit montrer les deux issues : **conforme** sur le cas sain, **arrêt** sur chaque artefact.

## 1. Cadre

| Élément | Valeur |
|---|---|
| Code | branche `prep/t06-course-v12`, commit `7822a65b` (celui d'E3 bis, inchangé) `<<À VÉRIFIER : commit exact du lanceur à passer au script ; nom du script de lancement pour la v12, E3 bis utilisait scripts/lancer_t06_v11.sh avec T06_BRANCHE_CODE=prep/t06-v11>>` |
| Branche d'essai (R12) | `essai/t06-e3ter-v1`, créée depuis `prep/t06-course-v12` ; jamais `main`, jamais une branche de la course |
| Carte | A100 SXM4 80 Go, prix max 2,10 USD/h (E3 bis : 2,069 constaté, stockage compris) ; mêmes seuils d'offre que `config-t06-epreuve-e3bis-v3.json` |
| GO | ligne nouvelle de `registres/go.md`, type calcul, à créer par la mère sous GO-2026-11-08-05 : `<<GO_E3TER>>` ; plafond § 8 |
| Dépense antérieure | `T06_DEPENSE_EPREUVES_ANTERIEURES_USD` = somme relevée des épreuves E2, E3, E3 bis `<<À VÉRIFIER : valeur exacte dans registres/depenses.md ; E3 bis seule = 3,652>>` |
| Mode | `reel`, `PREREG_ABSENT=1` (galop, pas d'expérience décisive), `T06_TESTS_ARGS` **non défini** |
| Pièces interdites | aucune pièce scellée de la course n'est touchée ; `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` jamais lus |

## 2. Dimensionnement retenu

Trois configurations, toutes dérivées de `config-t06-epreuve-e3bis-v3.json` (mêmes 4 tâches d'évaluation `e4b3179a…`, 3 tâches de distillation `74567f99…`, mêmes six états S25/S50/S75/S100/T100/dose 0, lot 8, `max_nouveaux` 400) :

| Fichier à créer (`docs/notes/g0-deux-semaines-v1/e3-ter-v1/`) | T | `fraction_equivalence` | `tolerance_equivalence` | Rôle |
|---|---|---|---|---|
| `config-t06-epreuve-e3ter-v1.json` | **10** | **0,5** | 0,2 | cas sain |
| `config-t06-epreuve-e3ter-artefact1-v1.json` | 10 | 0,5 | **1e-9** | artefact : l'équivalence doit **s'arrêter** |
| `config-t06-epreuve-e3ter-artefact2-v1.json` | 10 | 0,5 | **1e6** | artefact : le contrôle négatif doit **s'arrêter** |

Autres champs : `go_id` = `<<GO_E3TER>>`, `plafond_usd` = plafond de la ligne (§ 8), `calendrier` à jour `<<À VÉRIFIER>>`, `statistique_equivalence` `q99`, `actions_min_controle_negatif` 10, `positions_min_controle_negatif` 4, `fraction_min_controle_negatif` 0,95 (inchangés : ce sont les valeurs de la course).

**Pourquoi T = 10 et non 4** : T est celui de la course (`config-t06-reel-v1-brouillon5.json`) ; les contextes longs sont ce qui met la passe unique à l'épreuve, et avec T = 4 le tirage à 0,5 ne retient que 8 paires en espérance (probabilité d'en avoir moins de 10 : 0,77 → « non concluant » presque sûr). **Pourquoi 0,5 et non 0,05** : la fraction ne change que la densité de l'échantillon, pas le chemin de code ; au taux de la course il faudrait ≈ 30 tâches × T = 10 pour rendre le contrôle négatif concluant par état (≈ 6 h de carte, 15–20 USD attendus), ce que la course elle-même fera avec ses 64 tâches.

Attendus du tirage (cas sain) :

| Phase | Paires (tâche, pas) indépendantes | Actions contrôlées attendues | Probabilité de moins de 10 comparables |
|---|---|---|---|
| chaque état dosé (S25…T100) | 4 × 10 = 40 (les mêmes dans chaque état) | 20 | ≈ 3·10⁻⁴ |
| dose 0 (4 conditions) | 40 (× 4 conditions = 160 actions) | 80 | ≈ 0 |
| données de distillation (3 tâches × 5 épisodes × 2 conditions) | 15 générateurs × 10 = 150 | 75 | ≈ 0 |

Volume : 36 épisodes d'évaluation × 10 = 360 actions, 30 épisodes de distillation × 10 = 300 actions ; E3 bis en avait 144 + 120 à T = 4.

## 3. Artefacts (R5 : « aucun repli silencieux »)

- **Artefact 1** (tolérance 10⁻⁹) : la première action contrôlée du premier lot de distillation doit lever `GardeArret` « génération ≠ passe unique » (tout écart numérique non nul dépasse la tolérance). Attendu : arrêt dans les 5 premières minutes de la chaîne, code de sortie d'arrêt, message cité dans le journal, aucun épisode écrit en `diag/`.
- **Artefact 2** (tolérance 10⁶) : l'équivalence passe trivialement ; décalée d'un jeton, la comparaison ne dépasse jamais la tolérance ; à la fin de la phase « génération des données de distillation » (≥ 10 comparables attendus : ≈ 75), `exiger_controle_negatif_phase` doit lever « garde d'équivalence aveugle au décalage d'un jeton … ». Attendu : arrêt après le quatrième lot de distillation (≈ 10 min), message cité.
- Les deux artefacts sont des **configurations seules**, jouées sur la même instance après le cas sain, chacune dans un dossier de run neuf (R12). Un artefact à code (dose de l'adaptateur changée entre génération et passe unique) exercerait une inéquivalence réelle ; il demande un développeur et une contre-lecture : **option**, pas dans ce galop `<<À VÉRIFIER : la mère décide>>`.
- Si un artefact **ne s'arrête pas** : c'est le résultat le plus important du galop ; arrêt du galop, rien d'autre n'est lancé, compte rendu à la mère.

## 4. Ce que l'on lit, ce que l'on ne lit pas

**Lu** (par un script de lecture sur processeur, après scellement du `diag/` du run) : dans `diag/<run>/episodes-t06.json`, `fiches[k].equivalence` **regroupées par `phase`** (l'extracteur v1 lit `etats[<état>].equivalence`, clé que la chaîne n'écrit jamais : ne pas s'en servir pour ce point `<<À VÉRIFIER : écrire extraire_garde_equivalence_t06_v1.py, lecture seule de ces champs>>`) : nombre d'actions contrôlées, plus grand écart au 99ᵉ centile par couche, tolérance ; `controles_negatifs[<état>]` et celui de la distillation : `comparables`, `passent`, `courtes`, `fraction`, `min_des_maxima`, `lecture` (attendu : « conforme » dans les sept phases) ; pour chaque artefact : présence de `GardeArret`, message, moment ; durée et dépense.

**Non lu** : sondes, aires, test croisé, couples descriptifs, coûts par condition, textes des épisodes, tout ce qui regarde P3 ou H1. Le galop n'est pas une expérience : lire un signal y serait un run visant un signe (R3). Le `diag/` entier est scellé et gardé sur la branche d'essai ; seul l'extrait de la garde entre au compte rendu.

## 5. Étapes (fille d'exécution)

0. **Sur processeur, avant toute dépense** : rejouer le tirage de l'échantillon des trois configurations avec les graines du manifeste (`generateur(g["tache/<id>"])`, `graines_des_actions(gen, 1, T)` puis `gen.random(T) < fraction`) et consigner le nombre de paires retenues par tâche ; si une configuration en retient moins de 10 au total, la mère en est avertie avant la création `<<À VÉRIFIER : les graines du manifeste sont-elles connues avant la création, ou dérivées sur l'instance ? sinon cette étape se fait sur le manifeste d'E3 bis pour vérifier la formule 0,44>>`.
1. **Contrôles** : `controles-epreuve` pour les trois configurations (code 0 attendu, plafond d'épreuve + dépense antérieure ≤ plafond de la ligne).
2. **Création** : une seule instance, `GO_ID=<<GO_E3TER>>`, `MODE=reel`, `PREREG_ABSENT=1`, `CONFIG=…/config-t06-epreuve-e3ter-v1.json`, `BRANCHE=essai/t06-e3ter-v1` ; commande de création exécutée **une seule fois**, sans valeur de clé affichée ; `apres-creation` comme à E3 bis.
3. **Suite de tests ciblée sur l'instance** : `<<À VÉRIFIER : la mère décide ; le commit est celui d'E3 bis, déjà éprouvé 1878 tests en 4009 s sur une carte identique ; la rejouer coûte ≈ 1,1 h ≈ 2,3 USD ; recommandation : ne pas la rejouer, le consigner>>`.
4. **Cas sain** : surveillance par le journal (`PROGRES … etape=episodes phase=… actions=…`) ; aucune lecture de résultat pendant le run.
5. **Artefact 1 puis artefact 2** : mêmes commandes, configuration changée, dossier de run neuf ; relever code de sortie et message.
6. **Scellement** sur l'instance puis rapatriement : `diag/<run>` des trois runs, journaux, `lancement.txt` ; empreintes compagnon ; commit sur `essai/t06-e3ter-v1` ; push de cette branche seule (`git push -u origin essai/t06-e3ter-v1`, jamais `main`).
7. **Destruction par identifiant** (R10) dès le rapatriement vérifié ; inventaire avant et après **toujours** par `filtre_instances_vast_v1.py` (l'inventaire brut imprime des variables secrètes) ; instances 58936096, 58936099, 58936100 jamais touchées.
8. **Lecture** (§ 4) sur processeur, à partir des pièces scellées ; **compte rendu** (§ 7).

Consignes permanentes : clés par leur nom seulement (`VAST_API_KEY`), jamais `env`/`printenv`/`set`/`export -p`/`/proc/*/environ` ; garde des secrets à 0 avant tout commit ; `git fetch` toujours avec refspec explicite ; aucun appel de modèle, aucune autre dépense ; toute dépense exige le mot de Lazar dans la session qui dépense, ou la ligne de GO citée ici créée par la mère sous GO-2026-11-08-05 `<<À VÉRIFIER : la fille doit-elle attendre le mot de Lazar dans sa propre session, comme la fille idéation 2 l'a exigé à R-1819 ? la mère tranche avant de l'ouvrir>>`.

## 6. Arrêts

- Offre hors seuils, carte autre que l'A100 80 Go, prix > 2,10 USD/h : pas de création.
- Dépense relevée > plafond de la ligne : destruction immédiate, compte rendu.
- `GardeArret` sur le **cas sain** : arrêt du galop ; c'est un résultat (la garde ou la chaîne a un défaut à dose 1 ou à T = 10), à rapporter avec le message, sans relance.
- Artefact qui **ne s'arrête pas** : arrêt du galop (§ 3).
- Toute lecture d'un champ hors § 4 : à consigner comme écart.
- Durée de carte > 5 h : destruction, compte rendu (pire cas prévu 2×).

## 7. Compte rendu de la fille (nombres seuls, ≤ 300 mots)

Par phase (7) : actions contrôlées, écart q99 maximal par couche, tolérance, `comparables`/`passent`/`courtes`/`fraction`/`min_des_maxima`/`lecture`. Par artefact : arrêt oui/non, message, minute. Durée de carte, dépense relevée (carte, stockage, téléchargement), identifiant d'instance créé et détruit, commit de la branche d'essai, empreintes des `diag/`. Écarts à l'ordre. Rien d'autre.

## 8. Devis

| Poste | Heures | Base | USD |
|---|---|---|---|
| Installation, téléchargement du modèle | 0,25 | E3 bis | 0,5 |
| Cas sain (660 actions à T = 10 ; E3 bis : 264 actions à T = 4 en 33 min, lecture comprise) | 1,5–2,5 | ≈ 2,5× E3 bis en actions, contextes 2,5× plus longs | 3,1–5,2 |
| Artefacts 1 et 2 | 0,3 | arrêts attendus à 5 et 10 min | 0,6 |
| Stockage, téléchargement | — | E3 bis : ≈ 0,2 | 0,4 |
| **Attendu** (sans suite de tests) | ≈ 3 h à 2,07 USD/h | | **≈ 7** |
| Pire cas (hôte 2× lent, 2,10 USD/h) | ≈ 6 h | | ≈ 14 |
| **Plafond proposé** | | | **15** (20 si la suite de tests est rejouée : + 1,1 h) |

`<<À VÉRIFIER : le poste « lecture-cout duree_s=1257.9 » du journal d'E3 bis (a5c0e298, traces/t06-20261108-073203-zdSu/journal.txt) : s'il croît avec le nombre d'actions, le cas sain tend vers 2,5 h ; prix A100 du jour sur Vast>>`. Alternative non recommandée : au taux de la course (0,05) avec ≈ 30 tâches × T = 10, ≈ 6 h, attendu 15–20, plafond 40.

## 9. Ce qui suit le galop

1. La mère relit le compte rendu et les pièces scellées ; elle écrit la ligne de `registres/decisions.md` qui établit le règlement d'E3-6 (sept phases : actions contrôlées, écart q99 maximal, tolérance, lecture du contrôle négatif ; deux artefacts arrêtés ; référence à ce galop, commit et empreintes).
2. Elle remplit `<<REGLEMENT_E3_6>>` de l'ordre de course par le numéro de cette ligne (`grep -c '^| <numéro> |'` = 1 dans le registre de `main`), avec `<<COMMIT_COURSE>>`, `<<CONFIG_COURSE>>`, `<<EMPREINTE_PREREG_T06>>`.
3. Seconde contre-lecture de l'ordre rempli (R2, lecteur neuf), scellement du candidat 12, puis création de la course sous GO-2026-11-02-28 (carte GO-2026-11-07-02).
4. Si le cas sain s'arrête ou si un artefact ne s'arrête pas : pas de course ; développeur sur le lanceur, nouvelle version (R12), nouveau galop sur devis.

## 10. Points `<<À VÉRIFIER>>` (récapitulatif)

1. Commit exact et script de lancement de la v12 (E3 bis : `scripts/lancer_t06_v11.sh`, `T06_BRANCHE_CODE=prep/t06-v11`).
2. Valeur de `T06_DEPENSE_EPREUVES_ANTERIEURES_USD` (somme E2 + E3 + E3 bis dans `registres/depenses.md`).
3. Numéro de la ligne de GO à créer (`<<GO_E3TER>>`) et plafond retenu (15 ou 20).
4. Suite de tests sur l'instance : rejouée ou non.
5. Script de lecture de la garde (`fiches[k].equivalence` par `phase`, `controles_negatifs`), à écrire avant la création ; l'extracteur v1 ne convient pas pour ce point.
6. Graines : rejouables sur processeur avant la création, ou seulement sur le manifeste d'E3 bis.
7. Croissance du poste « lecture-cout » avec le nombre d'actions ; prix A100 du jour.
8. Mot de Lazar dans la session de la fille (R-1819) ou ligne de GO de la mère suffisante.
9. Artefact à code (inéquivalence réelle) : option à décider.
10. `calendrier` de la configuration (dernier jour de création, fin du GO).
