# Contre-lecture (R2) — préenregistrement « mesure unanime » v1 et son script d'analyse

- Contre-lecteur : sous-agent neuf, Opus 5.5 ; n'a écrit ni le préenregistrement ni le script.
- Début : 2026-10-27 23:15:41 UTC (`date -u`). Fin : voir la dernière ligne.
- Processeur seul ; aucun fichier du dépôt modifié ; aucun commit ; `scores-p3.npz` ni ouvert ni lu ; le script relu n'a
  tourné que sur des données synthétiques (importé sans modification par mes scripts de vérification).

## Verdict

1. **À corriger en v2** avant scellement : CM-1, CM-2, CM-3, CM-4, CM-5, CM-6, CM-7 changent le texte (et, pour CM-3, CM-4
   et CM-7, le code) ; CM-8 à CM-11 sont de moindre portée et se règlent dans la même v2.
2. Le script fait pour l'essentiel ce que le texte dit : plis, séparation sans chevauchement, rang conforme, règle de
   Ville et les six statistiques sont conformes à `bases/sequentiel.py` et à `processus_e.log_e_unilateral`. **Mais trois
   gardes de la liste d'arrêt n'existent pas**, et un score non fini fait tomber les alertes à zéro en silence (CM-3).
3. Sur le fond : **M3 est garanti par construction** (critique T2-C A(a)3, que la synthèse demande de trancher au
   préenregistrement et que le texte ne traite pas) ; **la prédiction de M2 dépend d'une corrélation naturelle non
   mesurée** : le synthétique de l'auteur lui-même donnerait « non concluant » (+0,09 < +0,10).

## Empreintes des fichiers lus

| fichier | empreinte SHA-256 |
|---|---|
| `brouillons/…/mesure-unanime-v1/preenregistrement-mesure-unanime-v1.md` | `7158affc04645bb21fe1f2934fdbbfc9333d5576d55d2f5b562444797b54a935` (attendue : conforme) |
| `brouillons/…/mesure-unanime-v1/analyse_fausses_alertes_v1.py` | `26dc9a3e71752e32c18cf516627a157f658f6c78624644c46f80330c3dcca2e4` (conforme) |
| `brouillons/…/mesure-unanime-v1/sortie-synthetique-essai.json` | `6ee24bd0ce27908407c2bb2be59242362444a354c8481b3afd5cd5cc4c128453` (conforme) |
| `src/controle_ia/bases/sequentiel.py` | `35a0983404d7a10d0bb736fa37307a108501785a207c27346be1cd02bab11ba8` |
| `src/controle_ia/simulation_t03/calibrage.py` | `a2be6f6b127032aced5d75acd9cdf7c18c17e28df89978bd7102cf692c560def` |
| `src/controle_ia/agregateurs/processus_e.py` | `1081469bea3564a57119b56c26ee25f27817a7e961abdf440a556dc476a15fc7` |
| `prereg/gabarit-preregistrement-v1.md` | `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e` |
| `origin/main:docs/notes/collisionneur-mesures-fortes-v1/synthese-mesures-fortes-v1.md` | `bed9107b67c969e0e9a97336000a569faf2c519dd556731ace14f29de404885e` (celle citée : conforme) |

Les trois fichiers du brouillon sont identiques à ceux du commit `0dbaf94b` (branche `canal/conv-audit-n04`).

## Mes scripts et sorties (même dossier que ce rapport, chacun avec compagnon `.sha256`)

- `verif_contre_lecture_v1.py` → `sortie-verif-contre-lecture-v1.json` ; graine `SeedSequence(20261027231500)`, enfants
  (0,) à (5,) ; effets épisode par `SeedSequence(20261027231500, spawn_key=(⌊10τ⌋, 7, ⌊10 r0⌋))`.
- `verif2_gardes_intervalles_v1.py` → `sortie-verif2-gardes-intervalles-v1.json` ; graine `SeedSequence(20261027232100)`,
  enfants (0,) à (2,).
- Interpréteur `/opt/venv-essaim-sim-v1/bin/python -I -B` (Python 3.13.17, numpy 2.5.4 ; pas de scipy dans cet
  environnement, d'où le `log_ndtr` maison du script).

## Réponses aux questions

### 1. Le script fait-il ce que le préenregistrement dit ?

- **Plis** : `plis_de` prend les rangs i mod 10 d'une permutation tirée par l'enfant 0 : conforme. Avec E = 60, six
  épisodes par pli et K = 34 partout ; si E n'est pas multiple de 10, K varie d'un pli à l'autre et le manifeste ne donne
  que le minimum (CM-5).
- **Séparation normalisation / seuils / évaluation** : partition exacte (`setdiff1d`, puis tranches disjointes) : aucun
  chevauchement, aucune fuite de l'évaluation dans le calibrage. **Mais** la tranche de normalisation est prise dans
  l'ordre **trié** des indices (`setdiff1d` trie) : ce sont toujours les ~20 plus petits indices hors du pli ; 35 épisodes
  sur 60 ne servent jamais à la normalisation, l'indice le plus haut qui y sert est 24 (partie E). Le texte ne décrit pas
  ce partage (CM-4).
- **Rang conforme** : `rang_conforme` et `seuil_conforme` reproduisent `simulation_t03.calibrage` (même ⌈(K+1)(1−α) − 1e-9⌉,
  infini si le rang dépasse K) ; alarme au sens strict « > seuil », comme `bases.sequentiel.decider`. La copie n'a pas la
  garde « valeurs non finies » de l'original (CM-3).
- **Par action** : quantile 1 − τ_a des actions valides des épisodes de calibrage (normalisation + seuils), sur les scores
  bruts (équivalent aux standardisés, transformation croissante) ; alerte si le maximum de l'épisode dépasse : conforme.
- **Règle de Ville** : `log_e_unilateral` du script = celle de `processus_e` avec σ = 1 (écart maximal 1,1·10⁻¹⁶ sur
  S ∈ [−30, 30], n = 1…10, partie B) ; seuil `≥ log(1/α)` à un instant quelconque, comme `processus_e.premiere_alarme` :
  conforme.
- **Statistiques** : max, somme terminale, somme séquentielle (maximum courant de la somme partielle), Page (k = 0,5,
  maximum courant de C_t ≥ 0), processus e (maximum courant), balayage (w = 3) : valeurs finales identiques à
  `bases.sequentiel.trajectoires`/`finales`. Les actions invalides sont sautées : les fenêtres de balayage portent sur trois
  actions **valides** consécutives, qui peuvent enjamber un trou (à dire, CM-11).
- **Effet épisode** : ajouté aux scores bruts de tous les épisodes avant toute standardisation : conforme. Échelle
  `np.nanstd(X)` sur tous les épisodes gardés (le texte dit « σ_sonde », la docstring dit « σ_cal ») ; le même générateur
  sert à toutes les sondes l'une après l'autre, donc chaque sonde reçoit des effets différents (CM-7).
- **Moyenne sur tirages, intervalles par grappes** : conformes au texte (rééchantillonnage des épisodes, sondes et
  tirages ensemble ; différence de M2 appariée par le même tirage d'épisodes). Ce sont des intervalles **à alertes
  figées**, conditionnels aux calibrages (CM-8).
- **Bords** : T_e < w impossible (au moins 5 actions gardées, w = 3) ; rang > K arrêté au niveau du K minimal, infini
  par pli sinon ; σ = 0 arrêté **seulement** sur l'ensemble de normalisation (conforme au texte). **Score valide non fini :
  aucun arrêt** ; démontré (partie G) : un NaN dans une action valide de l'épisode 59 fait passer les alertes « par
  action » de 7 à 0, et cinq des six statistiques conformes à 0, sans erreur (CM-3).

### 2. Les prédictions sont-elles cohérentes et réfutables ?

- **M1** : 1 − 0,99^8 = 0,0773 ; moyenne de 1 − 0,99^T pour T uniforme sur {5…10} = 0,0725 ; T = 5 : 0,049 ; T = 10 :
  0,096. Le point « ≈ 0,075 » est juste pour une longueur moyenne d'environ 8. En échantillon fini, le quantile empirique
  de ~400 actions dépasse un peu 1 % par action : simulé 0,089 sous indépendance (r0 = 0), 0,076 à r0 = 0,2, 0,072 à 0,5,
  0,049 à 0,8 (partie C). La fourchette 0,05 à 0,12 tient sous dépendance faible ; à forte corrélation naturelle, M1 tombe
  en « non concluant », ce que la ligne « M1 réfuté » du tableau de lecture anticipe à peu près.
- **M1 bis** : raisonnement juste (à loi marginale fixée, une corrélation positive plus forte réduit la probabilité que le
  maximum dépasse un quantile marginal ; moins de tirages effectifs). Décroissance simulée à toutes les corrélations
  naturelles (par exemple 0,089 → 0,051 à r0 = 0). C'est presque un théorème : contrôle du code plus qu'hypothèse.
- **M2** : le signe est juste, **l'ordre de grandeur non**. La standardisation sur les actions poolées absorbe la variance
  ajoutée (σ_total ≈ √5 σ à τ = 2), donc la variance marginale des scores standardisés reste ≈ 1, mais la corrélation
  intra-épisode devient (r0 + τ²)/(1 + τ²) ≈ 0,8 à 0,96. Sur 5 à 10 actions, le processus e à ρ = 0,5 plafonne : à
  corrélation totale, S_n ≈ n·U et le seuil log 20 demande S_10 ≳ 9,1, soit P(U > 0,91) ≈ 0,18 au plus. Simulé avec le
  script (partie C, 12 sondes indépendantes, 4 tirages) :

  | corrélation naturelle r0 | Ville τ = 0 | Ville τ = 2 | différence |
  |---|---|---|---|
  | 0 | 0,003 | 0,129 | +0,126 |
  | 0,2 | 0,049 | 0,138 | +0,089 |
  | 0,5 | 0,072 | 0,127 | +0,055 |
  | 0,8 | 0,142 | 0,162 | +0,020 |

  La borne haute « +0,30 » est hors d'atteinte ; « ≥ +0,10 » n'est atteint que si r0 ≲ 0,15. Or des scores de sonde d'un
  même épisode (même tâche, même contexte) ont toutes les chances d'être corrélés. Le synthétique de l'auteur (r0 ≈ 0,23)
  donne +0,09 [0,082 ; 0,112] : **M2 y serait « non concluant » selon ses propres seuils**, et la ligne de lecture gelée
  conclurait « le mécanisme du théorème négatif n'est pas visible », alors que Ville est déjà à 0,12 > α à τ = 2 (CM-2).
- **M3** : niveau attendu 1 − ⌈35 × 0,95⌉/35 = 1/35 ≈ 0,0286 pour K = 34 (le rang 34 est le maximum des 34 : taux exact
  1/(K + 1)). Simulé : moyennes 0,021 à 0,035 dans toutes les cellules (partie C). Une sonde à τ = 0 (150 jeux, partie D) :
  P(taux > 0,075) = 0,007 à 0,02, P(taux > 0,10) = 0/150, quantile 95 % ≈ 0,05 à 0,06, P(taux = 0) ≤ 0,013. Les seuils
  1,5 α et « ≤ 20 % au-dessus de 2α » sont donc **raisonnables comme garde contre une panne grossière**, mais ils sont 2,6
  fois le niveau attendu : un doublement du taux (≈ 0,057) passerait « tenu ». Et M3 ne peut échouer que par un bogue ou une
  rupture d'échangeabilité, puisque l'injection touche calibrage et évaluation de la même façon (CM-1, CM-5).

### 3. La sortie synthétique est-elle cohérente ?

Oui, et elle confirme les constats. Par action à τ = 0 : 0,083 (dans la fourchette) ; M1 bis : 0,083 → 0,070 → 0,060 →
0,050 (décroissant) ; Ville à τ = 0 : 0,033 (M2 bis tenu) ; différence de Ville : +0,09 (sous le seuil de confirmation
+0,10, non dit). Médianes conformes à τ = 0 ≈ 0,017 : c'est l'effet conjoint (i) du rang maximal, qui fixe le niveau
attendu à 1/35 ≈ 0,029 et non à 0,05, et (ii) de la granularité 1/60 d'un taux sur 60 épisodes avec un seul tirage, dont
la loi est asymétrique (1,7 alerte attendue) : la médiane tombe sur 1/60 = 0,017 ou 2/60 = 0,033 (quartiles observés
0,017 et 0,033). À τ > 0 la moyenne sur tirages lisse vers 0,023 à 0,030. **Le texte ne le dit pas** : il écrit « niveau
réel attendu ≤ α en espérance » et « signe ≈ α », sans 1/(K + 1) ni granularité (CM-5).

### 4. Ce qui manque au regard du gabarit (R1)

Toutes les sections du gabarit existent et sont remplies. Manquent ou trompent : la réponse à T2-C A(a)3 et A(a)1 (CM-1) ;
une mesure de la corrélation naturelle, dont dépendent M1, M1 bis et M2 (CM-2) ; des gardes réellement codées et
testées sur un artefact (R5, CM-3) ; le niveau attendu 1/(K + 1) et E minimal (CM-5) ; un tableau de lecture qui couvre
toutes les combinaisons (CM-10) ; le bon commit et la provenance des chiffres internes (CM-9).

### 5. Les chiffres cités

- « À 1 % par action, environ 40 % des épisodes honnêtes de 50 actions alertent, sous indépendance » : **cité
  fidèlement** de la synthèse (section « Convergences », deuxième puce), qui le rattache à T1-A (a)4, T1-B a4, T1-C E-M2 ;
  arithmétique juste : 1 − 0,99^50 = 0,395.
- « T0.3 P8 : 0,21 à 0,35 » : **la synthèse ne le cite pas** ; `bases/sequentiel.py` le cite dans sa docstring (lignes 7
  et 8 : « la règle de Ville atteint 0,21 à 0,35 de faux positifs sous effet épisode (T0.3, P8) »). Le préenregistrement le
  donne sans chemin ni empreinte (R6, CM-9). Je n'ai pas vérifié ce chiffre à sa source de T0.3.
- Non vérifiés (hors de mes fichiers) : programme v2 § 3 et § 8.3, N-007, R-546, mot de Lazar du 27 octobre.

## Constats

### CM-1 — M3 garanti par construction ; la critique T2-C A(a)3 n'est pas traitée (grave)

- **Où** : Hypothèse, M3 ; Métrique, « Corrélation injectée … ajouté aux scores bruts de **tous** les épisodes » ; Critères,
  première ligne (« le comparateur de H2 se calibre par épisode entier »).
- **Ce qui manque** : la synthèse (« Pour ta décision », suite 1) dit « filtre de H2a et calibrage de l'injection contestés
  (T2-C A(a)1, A(a)3) ; à trancher au préenregistrement ». A(a)3 : « injectée aussi au calibrage, la corrélation passe la
  garde par construction ». C'est exactement M3 : sous échangeabilité des épisodes, le seuil conforme est valide par
  théorème, quel que soit τ. M3 ne peut échouer que par un bogue ou une rupture d'échangeabilité ; il ne prouve rien sur la
  supériorité du calibrage par épisode face à une dépendance que le calibrage n'a pas vue. Le texte ne cite ni A(a)3 ni
  A(a)1.
- **Correction** : (a) requalifier M3 en **contrôle de justesse** (code, plis, échangeabilité), pas en preuve ; (b) écrire
  la décision sur A(a)3 : soit la garder (injection des deux côtés, parce que le comparateur se calibre sur des épisodes
  honnêtes de même loi, et dire que c'est sa limite), soit ajouter un **bras descriptif « calibrage à τ = 0, évaluation à
  τ »** (dépendance absente du calibrage), sans verdict, qui montre ce que la garantie ne couvre pas ; (c) dire que A(a)1
  (filtre de H2a, rappel nul par construction) est hors du champ de cette mesure de fausses alertes et renvoyé au
  préenregistrement de H2 ; (d) dans la première ligne des critères, appuyer la conclusion sur M1 et M2 seuls, M3
  n'étant qu'une condition de validité.

### CM-2 — M2 mal dimensionné et dépendant d'une corrélation naturelle non mesurée (grave)

- **Où** : Prédictions, lignes M2 et M2 bis ; Seuil (M2 « ≥ 0,10 ») ; Critères, deuxième ligne.
- **Ce qui manque** : sur 5 à 10 actions, Ville à τ = 2 plafonne vers 0,13 à 0,16 (tableau de la réponse 2) ; « +0,30 »
  est impossible ; « ≥ +0,10 » exige r0 ≲ 0,15. Le synthétique de l'auteur donne +0,09 : non concluant. Si les scores
  réels sont déjà corrélés dans l'épisode, Ville est déjà au-dessus de α à τ = 0 et la différence est faible : la deuxième
  ligne de lecture (« le mécanisme du théorème négatif n'est pas visible à τ ≤ 2 sur P3 ») dirait alors le contraire de
  ce qui se passe.
- **Correction** : (a) mesurer et rapporter, par sonde, la **corrélation intra-épisode** des scores standardisés à τ = 0
  (corrélation intraclasse sur les épisodes gardés), définie dans la Métrique, médiane et quartiles pour réelles et
  placebo ; (b) M2 principal : **Ville à τ = 2 au-dessus de α** (médiane et borne basse > 0,05) ; la différence τ = 2 moins
  τ = 0 en secondaire, avec une prédiction conditionnelle à r0 (tableau ci-dessus, ou simulation de l'auteur gelée dans
  le texte) et une borne haute ramenée à ≈ +0,15 ; (c) ajouter une ligne de lecture « M2 bis au-dessus (Ville > α dès
  τ = 0) → mécanisme visible sur la dépendance naturelle ; différence plafonnée, pas une réfutation ».

### CM-3 — Gardes de la liste d'arrêt absentes ; échec silencieux sur score non fini ; R5 non tenu (grave)

- **Où** : Liste d'arrêt (« Score par action non fini … → arrêt (le code refuse) » ; « Fichier de données dont l'empreinte
  diffère … → arrêt ») ; script, `charger_reel`, `un_passage`, `seuil_conforme`.
- **Ce qui manque** : (i) aucun test de finitude des scores valides : un NaN hors de l'ensemble de normalisation donne des
  statistiques NaN, un seuil NaN ou des comparaisons fausses, donc **zéro alerte en silence** (démontré, partie G :
  par action 7 → 0 ; conformes 1 ou 2 → 0 ; la somme de Page traite le NaN comme une remise à zéro, `max(0.0, nan) = 0.0`) ;
  la copie de `seuil_conforme` a perdu la garde de l'original ; (ii) l'empreinte du fichier est calculée et écrite, jamais
  comparée à `968414fc…` ; (iii) les nombres de sondes (30 réelles, 400 placebo) et la règle qui les sépare (« plancher »
  dans le nom) ne sont ni écrits dans le texte ni vérifiés ; (iv) aucune garde n'est testée sur un artefact (R5) : la
  sortie synthétique ne teste que le cas sain.
- **Correction** : dans `charger_reel`, arrêt si un score valide n'est pas fini, si l'empreinte diffère de celle du texte,
  si les comptes ne sont pas 30 et 400 ; écrire la règle « plancher » dans la Métrique ; remettre la garde de finitude dans
  `seuil_conforme` ; joindre en v2 un essai de chaque garde sur un cas sain et sur un artefact (E < 44, σ = 0, NaN,
  empreinte fausse, comptes faux).

### CM-4 — Partage normalisation / seuils déterministe par ordre d'indice, non décrit (moyen)

- **Où** : script, `cal_idx = np.setdiff1d(...)` puis `cal_idx[:PART_NORMALISATION]` ; Métrique (le partage n'est pas
  décrit).
- **Ce qui manque** : `setdiff1d` trie ; la normalisation prend toujours les ~20 plus petits indices hors du pli
  (indices 0 à 24 ; 35 épisodes jamais), et les seuils les plus grands. Les indices suivent l'ordre trié des identifiants
  d'épisode. Si cet ordre suit la tâche ou le moment de la collecte, les épisodes d'évaluation de bas indice sont jugés
  contre des seuils pris sur les hauts indices : l'échangeabilité entre seuils et évaluation, dont dépend M3, peut se
  rompre, et la cause « ordre ? » que le tableau de lecture cite serait fabriquée par le code.
- **Correction** : prendre la normalisation dans l'ordre de la permutation tirée par la graine (ou un tirage par pli,
  graine consignée) et décrire ce partage dans la Métrique.

### CM-5 — Niveau conforme attendu non dit ; seuils de M3 lâches ; tailles minimales inexactes (moyen)

- **Où** : Prédictions, ligne M3 (« signe ≈ α ») ; Plan d'analyse, « Taille » (« ≥ 40 attendus », « K ≥ 34 ») ; Liste
  d'arrêt (« moins de 40 »).
- **Ce qui manque** : le niveau exact attendu 1 − ⌈(K + 1)(1 − α)⌉/(K + 1) = 1/35 ≈ 0,0286 pour K = 34 (0,57 α) ; la
  granularité 1/60 des taux à τ = 0. K ≥ 34 seulement si les 60 épisodes sont gardés ; K = E − ⌈E/10⌉ − 20 ; le rang
  conforme dépasse K dès K < 19, c'est-à-dire **E ≤ 43** : entre 40 et 43 épisodes gardés, la première garde passe et la
  deuxième arrête. Si E n'est pas multiple de 10, K varie d'un pli à l'autre (le manifeste n'en donne que le minimum). Les
  seuils de M3 valent 2,6 fois le niveau attendu (réponse 2).
- **Correction** : écrire le niveau attendu et la granularité ; remplacer « ≈ α » par « ≈ 1/(K + 1) ≤ α » ; écrire « E ≥ 44
  (K ≥ 19) » et « K = 34 si E = 60 » ; consigner K par pli. Option à considérer (le choix revient à l'auteur) :
  `PART_NORMALISATION = 15`, d'où K = 39 et un niveau exact de 1 − 38/40 = 0,05, ce qui rend M3 comparable à α ; à
  défaut, justifier 0,075 et 20 % par la simulation sous le nul (taux d'une sonde : quantile 95 % ≈ 0,05 à 0,06,
  P(> 0,10) < 1/150).

### CM-6 — Le contrôle placebo lit à tort tout écart comme un artefact (moyen)

- **Où** : Prédictions, ligne « contrôle » ; Critères, ligne « placebo ≠ réelles ».
- **Ce qui manque** : pour le comparateur par action et la règle de Ville, le taux dépend de la corrélation intra-épisode
  des scores (réponse 2) ; une sonde réelle, qui lit un trait de la tâche, peut légitimement avoir une corrélation
  intra-épisode différente d'une sonde aléatoire appariée en covariance. « Sur des honnêtes, rien ne distingue une sonde
  réelle d'une sonde aléatoire » n'est vrai que pour les taux conformes (≈ 1/(K + 1) pour toutes).
- **Correction** : limiter la lecture « artefact » aux cellules conformes ; pour par action et Ville, rapporter l'écart
  avec la corrélation intra-épisode des deux groupes (CM-2 (a)), sans audit automatique.

### CM-7 — Effet épisode tiré à part pour chaque sonde, sans que le texte le dise (moyen)

- **Où** : Métrique, « Corrélation injectée » ; script, `rngs_effet[tau][di]` réutilisé pour toutes les sondes
  successivement.
- **Ce qui manque** : chaque sonde reçoit un vecteur u_e différent (le générateur avance d'une sonde à l'autre), et les
  effets d'une sonde dépendent du nombre et de l'ordre des sondes avant elle. Le texte ne dit pas si u_e est commun aux
  sondes ; un effet épisode au sens du théorème négatif (l'épisode tout entier décalé) serait commun, et le contrôle
  « apparié » réelles contre placebo serait plus serré avec des effets communs.
- **Correction** : tirer un vecteur N(0, 1) par (τ, tirage), commun à toutes les sondes, multiplié par τ·σ_sonde ; ou
  écrire explicitement que les effets sont indépendants d'une sonde à l'autre, et dériver alors une graine par (sonde, τ,
  tirage).

### CM-8 — Intervalles conditionnels aux calibrages (mineur)

- **Où** : Métrique, « Résumés » ; script, boucles de rééchantillonnage.
- **Ce qui manque** : le rééchantillonnage des épisodes garde les alertes figées et ne refait pas le calibrage. Simulé
  (partie H, 40 jeux, r0 = 0,2, 6 sondes corrélées) : Ville à τ = 0, écart type de la médiane 0,013 par grappes contre
  0,0165 d'un jeu à l'autre (≈ 20 % trop étroit) ; par action, 0,020 contre 0,006 (prudent).
- **Correction** : écrire « intervalle conditionnel aux calibrages des dix plis » ; facultatif : refaire la validation
  croisée dans quelques centaines de rééchantillonnages pour les seules cellules à verdict (M1, M2), si le temps de calcul
  le permet (≈ 0,11 seconde par passage et par sonde).

### CM-9 — Provenance : commit faux, chiffre interne sans chemin, manifeste incomplet (mineur)

- **Où** : en-tête (« Commit du code d'analyse : `a71c388d` ») ; Hypothèse, M2 (« T0.3 P8 : 0,21 à 0,35 ») ; manifeste
  de sortie du script.
- **Ce qui manque** : `a71c388d` est le commit parent et ne contient pas le script ; le brouillon et le script sont entrés
  dans `0dbaf94b`. Le chiffre de T0.3 P8 n'a ni chemin ni empreinte (R6) ; sa seule source dans mes fichiers est la
  docstring de `bases/sequentiel.py` (`35a09834…`). Le manifeste n'écrit ni commit, ni empreinte du script, ni clés de
  dérivation des effets épisode, ni la permutation des plis (R9).
- **Correction** : citer le commit de scellement (ou `0dbaf94b`) ; citer pour P8 le fichier de résultats de T0.3 avec son
  empreinte (ou au moins `bases/sequentiel.py` et son empreinte) ; ajouter au manifeste commit, empreinte du script,
  `spawn_key` des effets et plis.

### CM-10 — Tableau de lecture incomplet ; conséquence programmatique présentée comme verdict (mineur)

- **Où** : Critères de lecture gelés.
- **Ce qui manque** : les issues « M1 non concluant », « M3 fragile », « M1 réfuté avec M2 confirmé ou non », « M2 bis
  au-dessus » n'ont pas de ligne (le gabarit demande « comment lire chaque combinaison »). La première ligne tire une
  conséquence pour H2 et G1 (« le seuil par action à 1 % ne définit que la sous-population de H2a ») : c'est une
  modification de lecture d'hypothèse, nœud de Lazar.
- **Correction** : compléter le tableau ; écrire la conséquence comme « proposée à Lazar ».

### CM-11 — Détails (mineur)

- `log_ndtr` maison (plancher 10⁻³⁰⁰, faute de scipy dans l'environnement) : exact à 10⁻¹⁶ sur |S| ≤ 30 ; sans effet
  sur les alertes ; à dire en commentaire.
- Docstring « σ_cal » contre texte « σ_sonde sur les épisodes gardés » : le code suit le texte (tous les épisodes, écart
  type sans correction) ; renommer.
- Balayage sur actions valides consécutives, qui peuvent enjamber une action invalide : à dire dans la Métrique.
- Les 30 sondes réelles partagent les épisodes : « part des sondes > 2α » compte des sondes corrélées ; à dire.
- Le chemin du rapport de contre-lecture annoncé (`contre-lecture-v1/…`, même dossier) diffère de celui où ce rapport est
  rendu (dossier de travail du contre-lecteur) : copier ce rapport et ses compagnons à l'endroit annoncé, ou corriger le
  chemin.

## Chiffres de ce rapport (tous dans `sortie-verif-contre-lecture-v1.json` ou `sortie-verif2-gardes-intervalles-v1.json`)

- M1 analytique : 0,0725 (T uniforme 5…10), 0,0773 (T = 8), 0,395 (T = 50) ; partie A.
- Niveau conforme attendu : 0,0286 (K = 34), 0,0500 (K = 39) ; K minimal 19 ; E minimal 44 ; partie A.
- Écart `log_e_unilateral` : 1,1·10⁻¹⁶ ; partie B.
- Taux selon r0 et τ : partie C (tableau de la réponse 2).
- Taux conforme d'une sonde sous le nul : partie D.
- Partage de normalisation : partie E (35 épisodes jamais ; indice maximal 24).
- NaN silencieux : partie G (verif2).
- Intervalles : partie H (verif2).

Fin : 2026-10-27 23:24:05 UTC (`date -u`).
