# Rapport du développeur neuf — lanceur de T0.6, v1

- Statut : rendu le 2026-11-05 16:54 UTC (heure relevée par `date -u`) par un développeur neuf (Claude Fable 5.1), qui n'a écrit ni le
  brouillon 3 du préenregistrement de T0.6, ni P3, ni les paquets réutilisés. Consigne suivie :
  `docs/notes/g0-deux-semaines-v1/consigne-developpeur-lanceur-T0.6-v1.md`. Rien n'est lancé, rien n'est loué, aucun modèle
  n'est téléchargé ni appelé, aucune clé n'est lue, rien n'est poussé ; aucun commit sur `main`.
- Branche : `prep/t06-lanceur-v1`, arbre de travail `/home/claude/wt/t06-lanceur-v1`, créée depuis `06765457` (tête de
  `claude/new-session-7qxayx` au départ : `main` local, `a364e947`, ne portait pas encore la consigne). Commits locaux
  seulement ; le dernier est nommé dans la réponse finale.
- Ce qui fait foi : le brouillon 3 (`/home/claude/controle-ia-travail/brouillons/T0.6-organismes-v0-v1-brouillon3.md`,
  `9e9fe60f3ad61d3d260bbec211e4ec2f91baf5247a34c4281acb5e7137fd67f7`), sections « Plan d'analyse », « Liste d'arrêt », « Devis », « Ce qui manque pour lancer », point 4,
  (i) à (vii) ; valeurs par défaut des décisions DT-1 à DT-6 : leurs recommandations (DT-1 (b), DT-2 (a), DT-3 (a), DT-4 (a),
  DT-5 (a), DT-6 (a)), **toutes en valeurs de configuration** (`decisions`, `doses_saboteur`, `doses_temoin`,
  `taches_distillation`, `textes_p3`, `episodes_par_tache_distillation`, `carte`, `sonde`, `couples_descriptifs`…) : un
  changement de Lazar est une valeur, pas du code. Seule exception, déclarée : DT-5 (b) ((i) à doses p < 1 et contrôles
  croisés) n'est pas écrite ; la configuration la refuse (nœud).
- Code existant réutilisé, jamais modifié (R12) : `organismes/lora.py` et `distillation.py` (repli « paires »),
  `sondes/familles.py` et `evaluation.py` (familles, `plancher_apparie`, `aire_sous_courbe`, `scores_actions`), le harnais
  (`jouer_episodes`, passe unique, garde d'équivalence, contrôle négatif), `premier_test_ia.conditions` (consignes de P3,
  `environnement`, `mesures_action`), `premier_test_ia.statistiques` (`effet_cout_apparie`, `cout_de_tache`),
  `premier_test_ia.run.controler_format_agent`, `environnements.pilote_a` (tâches, graines d'action),
  `lancer_pilote_a.charger_modele_et_format`, `gardes.py`, `manifeste.py`, `scellement.py`, `prereg.py`, les motifs de
  minuterie et de refus de l'amorce SPARKS v12, le patron de `p3_instance.sh` et du lanceur de P3. `git diff --stat
  06765457 HEAD -- src/controle_ia/organismes src/controle_ia/sondes src/controle_ia/harnais src/controle_ia/premier_test_ia
  src/controle_ia/environnements src/controle_ia/bases src/controle_ia/gardes.py src/controle_ia/manifeste.py
  src/controle_ia/scellement.py src/controle_ia/prereg.py requirements-*.txt` est vide (vérifié).

## 1. Fichiers rendus et empreintes (sha256 au dernier commit de la branche)

| fichier | sha256 | lignes |
|---|---|---|
| `src/controle_ia/t06/__init__.py` | `5bd597cf0b508e5b25c4ff85b685ae11be38c490853bd2a66f062f6519c48fae` | 15 |
| `src/controle_ia/t06/configuration.py` | `fe859b9a0016cb3fdd69002a37bf26fc344405875ebe6f9ec95ee3a47be71553` | 154 |
| `src/controle_ia/t06/cout.py` | `bcfe56832a1bf0c9af78b94232aedb44f179446a3871f45c27f1e3348efa7173` | 58 |
| `src/controle_ia/t06/distillation_transcription.py` | `1c5e3f7ada3eafd128aafa283ac832d2521146c6b8950a514201d930970cf18d` | 196 |
| `src/controle_ia/t06/identite.py` | `7e9fb962adba8c9b86f8feab43e3b005e28a9a6abcf0f704cd8f3997b5fad6c4` | 67 |
| `src/controle_ia/t06/lanceur.py` | `a3dde5509712a7a2fe072dbdec7be616d8bc9190fa1a57e649f90bfce9f05bc3` | 609 |
| `src/controle_ia/t06/lecture.py` | `2b5c080dee7420d1712fcb2ea21d3d864333e38ef4bb31fccb8c8e638b8b0669` | 348 |
| `src/controle_ia/t06/session.py` | `ad7031ab028787a3ea4bc4edfbf86206f56ccd916f447a150b639ba96f50bb17` | 169 |
| `src/controle_ia/t06/test_croise.py` | `0a627df9ecb82c518d06c0c7ca8df4afab48a5a0da34b785c31c0da4ab41a29c` | 303 |
| `scripts/amorce_instance_t06_v1.sh` | `88f059ce58cbaff15b933b5ffbb03b32d0b6f1c723f305f9f836407c3496946f` | 252 |
| `scripts/lancer_t06_v1.sh` | `bc335b7d4c0d25fe10ed48f57c2ae15980b6faf20c970ba36b11ea2e8de035bf` | 131 |
| `scripts/banc_mutations_t06_v1.py` | `848078fa477bf132615cf221bab8bed98c58711dd4df894a76b9b1717316e76a` | 141 |
| `tests/test_t06_cout.py` | `1b09999d9dbf930e17f6ac56f59be7ae5053ab8c76900c8b4c1f4acedfcba6f8` | 51 |
| `tests/test_t06_distillation.py` | `0680f3075fe83e0e3a7492f31ac9aa91e9fc19565b2bd557559ecdce0317f7b5` | 200 |
| `tests/test_t06_lanceur_jouet.py` | `e41d79833f5331dafa470d76008c2f9c3a683bba66e07be35ea7a86a3443a444` | 150 |
| `tests/test_t06_lecture.py` | `ebfbc756b9ad36f55f71f6704efab818ca9d562f467057164f2d9e00d104d759` | 151 |
| `tests/test_t06_scripts.py` | `5ad1a4fe2468095688ceecb80939fba7839ffb62126a59d0fff2e7f8b5d27f2e` | 340 |
| `tests/test_t06_session.py` | `786c9e7604011961ccb0ef9aa03e55ee2fee78140210023c3107e45826455dd7` | 74 |
| `tests/test_t06_test_croise.py` | `4ef307676d279d23303ce594f91526f98f29412cbd4406a992b78471e1deff3e` | 174 |
| `docs/notes/g0-deux-semaines-v1/config-t06-jouet-v1.json` | `39061da9c5a2226bf00d93dbdc7d35bb31759c449bd2375c7223518bc66f9044` | 62 |
| `docs/notes/g0-deux-semaines-v1/config-t06-jouet-v2.json` | `1b56ee2b14de8003fb4bc4388d59431d63e2518ab9bceeaa929d34d0c8061715` | 102 |
| `docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon1.json` | `ac7bc30e4a6c1716802a28bce68ff870ef3bbbad6ee7f085aa6761184b49203e` | 63 |
| `docs/notes/g0-deux-semaines-v1/banc-mutations-t06-v1.log` | `c19b80b0bb6f95e0e46ffb0d590cd978caaba61cdd87edebe3196cff3b77a20b` | 38 |
| `docs/notes/g0-deux-semaines-v1/banc-mutations-t06-v1.json` | `e817b3771fbc5dedd5a9d04174aecd94794b2f32f619bf4b2698f019a2318a38` | 298 |

## 2. Ce que chaque pièce fait (points (i) à (vii) de la section « Ce qui manque pour lancer »)

- **(i) `t06/lanceur.py`** : chaîne côté instance, par phases, sous manifeste (R9 : `SeedSequence` racine, clés par
  tâche d'évaluation, par épisode de distillation, par adaptateur, par lecture : `cles_des_graines`, `cles_de_lecture`).
  Contrôle avant dépense : aucune tâche de distillation dans l'évaluation (identifiants comparés), sinon aucune création
  (ni manifeste, ni dossier de run). Données de distillation : DT-1 (b) par épisodes neufs des deux conditions instruites de
  P3 sur les tâches de réserve (`jouer_distillation`, réglages de génération de P3, graines dérivées, garde d'équivalence,
  contrôle négatif) ; DT-1 (a) par relecture des textes de P3 (`charger_textes_p3`, empreinte citée, retokenisation + jeton
  de fin : écart déclaré du brouillon). Contexte honnête reconstruit pour chaque épisode (environnement (a) sans
  `instructions_cachees` ni `indications_privees`, journal des propres actions), exclusion mécanique des actions
  `mention_texte_prive`, aucune autre sélection ; comptes consignés (`actions`, `exclues`, `episodes_sans_cible`).
  Injection unique (rang, alpha, cibles), A et B en simple précision, état initial propre à chaque adaptateur
  (`etat_initial`, graines dérivées par couche comme `injecter`), distillation du saboteur puis du témoin, empreinte de la
  base avant et après (égalité exigée), sauvegarde en demi-précision scellée (`donnees/<run>/adaptateur-*.pt`) **et
  rechargement de ce qui est sauvegardé** avant l'évaluation (les empreintes des phases sont celles des fichiers poussés).
  Contrôle d'identité à dose 0 et artefact à dose 1 sur le contexte de contrôle du format (logits pris avant l'injection).
  Évaluation par états d'adaptateur (`etats_adaptateur` : `dose0` avec les quatre conditions de P3 entremêlées, puis
  `S25`, `S50`, `S75`, `S100`, puis `T100`), mêmes graines d'action pour une même tâche d'une condition à l'autre (un
  générateur neuf par condition, comme P3), état d'adaptateur relu avant et après chaque lot (dose sur chaque module,
  empreinte), contrôle négatif par phase ; par action : coût par le lecteur neuf, mesures sans juge, mention étendue,
  activations des jetons notés aux trois couches sur le disque de l'instance (`donnees/<run>/activations/c<couche>/`),
  sous-ensemble tiré par graine (fraction configurée, couche de la sonde, demi-précision) scellé pour la poussée. Puis
  lecture du coût (résultat scellé `lecture-cout-t06.json`), test croisé sur processeur, résultat scellé
  `lecture-sondes-t06.json` (tables B et C à la ligne 1 tant que le verdict de P3-bis et la lecture de T0.8 manquent :
  DT-4 ; relecture hors ligne par `lecture.relire_tables`), résumé. Tout arrêt après le manifeste laisse `arret.json`.
  `sondes_figees_p3` (notation en ligne des sondes génériques de P3 si T0.7 le demande) est une clé de configuration
  acceptée (nulle) mais **non branchée** : à écrire si le préenregistrement de T0.7 l'exige (réserve).
- **(ii) `t06/distillation_transcription.py`** : `transcription_honnete` (identifiants collés tels quels, jamais
  retokenisés ; empans exacts), `exemple_de_transcription` (étiquettes IGNORE hors des empans gardés ; empans vides,
  hors bornes ou chevauchants refusés), `distiller_transcriptions` (même entraînement que `distiller` : AdamW, lots remplis
  à droite, norme bornée, graine, perte non finie = arrêt, journal par époque), `exclure_mentions`,
  `adaptateurs_en_simple_precision` (attribut d'instance, à la manière de `normalisations_en_double` ; dose 0 = base au
  bit près conservé et testé), `etat_initial`, `etat_en`.
- **(iii) `t06/cout.py`** : lecteur du coût neuf : milliers à l'espace (« 1 000 », espace insécable comprise) lus comme un
  nombre ; « 120h » lu 120 (le lecteur gelé lisait 12 par repli) ; formes douteuses consignées, jamais corrigées ; 0 et
  l'absence illisibles.
- **(iv) `t06/test_croise.py`** : `partition_plis` (nombre pair exigé), `sonde_du_pli` (apprise hors du pli lu, famille
  décisive différence de moyennes, couche fixée, maximum ; autres familles pour T6-9), `planchers_du_pli`
  (`plancher_apparie` sur les jetons d'entraînement de la sonde du pli), `aire_moyenne` (aucune mise en commun),
  `intervalle_aire_moyenne` (tâches rééchantillonnées dans chaque pli, > 1 % dégénérés = arrêt), `quantile_plancher`
  (direction j appariée à la direction j), `plancher_permutation` (descriptif), `predicteurs_triviaux`, `base_cout_seul`,
  `etat_du_jeu` (au-dessus strict ; non interprétable ; échec). Notation vectorisée des planchers avec garde d'identité
  contre `score_action` (jamais la moyenne ni la médiane sur les jetons).
- **(v) `t06/lecture.py`** : T6-1 (deux différences appariées), T6-2 (Jonckheere–Terpstra stratifiée par tâche, p par
  permutation des doses dans chaque tâche, (r + 1)/(n + 1) ; inversions établies entre doses voisines), T6-8, T6-10, audit
  R4 « coût » (effet de (ii) au-delà de P3-P1 = 1,5227, valeur citée du brouillon 3, en configuration `audit`), table A
  (A1 à A5, phrases gelées), réserves (témoin qui baisse le coût, moins de la moitié des actions lisibles, exclusions
  au-delà de 5 %) ; T6-3 à T6-7, T6-9, audit R4 « sondes », tables B et C (B1 à B7, C1 à C7, phrases gelées, réserves
  « réglage fin » et « consigne », réserve « base boîte noire gratuite »), note « aucune ligne de B ou de C ne change le
  critère 3 ».
- **(vi) `scripts/amorce_instance_t06_v1.sh`** (instance) : minuterie de destruction en bash seul lancée en premier
  (`ECHEANCE_UTC_S` ≤ fin du 16 novembre 2026, gardée sur le disque), outils installés au besoin, **tout refus avant le run
  détruit l'instance** (GO non conforme par `t06.session go`, commit introuvable, citation absente ou en double, sceau faux,
  branche présente, second démarrage), clone au commit, lecture précoce des cinq citations, poussée initiale éprouvée,
  environnement, tests (nombre attendu cité), **run sans `timeout`**, relais des seules lignes `PROGRES`, puis : run
  complet → données légères et traces poussées, « fin, code 0 », instance mise à l'état « stopped » (disque gardé jusqu'au
  verdict) ; arrêt consigné → poussé, « fin, code 1 » ; processus mort sans résumé ni arrêt → ligne « RUN MORT », partiels
  poussés, arrêt. `scripts/lancer_t06_v1.sh` (session) : `controles` (GO, commit de scellement S poussé sur origin/main,
  huit citations du texte de S, fichiers cités scellés à S, amorce de S citée par son empreinte, disque, jetons présents
  jamais affichés), `creation` (prix et stockage aux bornes du devis, échéance ≤ fin du GO, garde de calcul rejouée,
  **commande littérale imprimée, jamais exécutée par le script**), `apres-creation`, `surveillance` (sans couperet : alerte
  après deux heures sans `PROGRES`, arrêt par l'identifiant seulement sur « RUN MORT » ou dépense cumulée ≥ 200 USD ;
  commande `vastai stop instance <id>` imprimée). `t06/session.py` : les trois gardes, bibliothèque standard.
- **(vii)** : répétition jouet de bout en bout (`tests/test_t06_lanceur_jouet.py`, configuration
  `config-t06-jouet-v2.json` : garde d'équivalence lue au maximum, tolérance 1·10⁻⁴, comme le jouet de P3 ; la v1,
  gardée telle quelle (R12), lisait le 99e centile, aveugle par construction quand la zone générée fait moins de 1 %
  de l'action : le contrôle négatif de phase l'a refusée, à raison, dans trois répétitions sur quatre ; les graines
  d'une répétition sans préenregistrement viennent d'une entropie neuve à chaque run), modèle par caractères, 4 tâches
  d'évaluation, 2 de réserve, T = 2, sept conditions, deux adaptateurs, quatorze couples descriptifs) ; essais locaux des
  deux scripts avec `python` et `vastai` factices ; banc de mutations (`scripts/banc_mutations_t06_v1.py`). La
  **répétition finale à blanc** (clone neuf au commit candidat, suite complète des tests, contrôles de session) reste à
  faire au candidat du texte, quand `prereg/T0.6-…` et sa configuration existent.

## 3. Ce que le jouet éprouve, et ce qu'il n'éprouve pas

Éprouvé sur processeur, sans réseau : l'enchaînement complet des phases et des gardes (manifeste, disjonction des tâches,
consignes scellées de P3, format, génération des données de distillation par le harnais, reconstruction honnête,
exclusion, injection, simple précision, distillation de deux adaptateurs, base intacte, sauvegarde et rechargement,
identité à dose 0 et artefact à dose 1, états de phase, conditions de P3 et conditions d'adaptateur, contrôle négatif par
phase, lecteur du coût, activations sur disque, sous-ensemble, lecture du coût et table A, test croisé des deux sens,
validité, courbe, quatorze couples, tables B et C à la ligne 1, deux résultats scellés et rattachés, résumé, refus d'un
second run du même identifiant). Durée : ≈ 40 s.

Non éprouvé : la garde d'équivalence au 99e centile (production, bfloat16, tolérance 0,2 : réglages de P3 repris
dans la configuration réelle, non rejoués ici) ; le modèle réel (mémoire de la distillation d'une transcription de ≈ 4 000 jetons sur le 8B en bfloat16 avec
adaptateurs en simple précision et AdamW : DT-6 prévoit la relance sur H200), les débits et le devis, le disque des
activations (≈ 15 à 45 Go selon la longueur moyenne des actions), la durée du test croisé sur 4 096 dimensions (sondes
perceptron et attention sur ≈ 90 000 jetons, Mahalanobis en 4 096 × 4 096), la valeur scientifique des aires (le jouet
produit des textes aléatoires : table A à la ligne A1b, états « non au-dessus »), l'interface de Vast (minuterie, arrêt
« stopped », DELETE : code copié de SPARKS v12 et de P3, non tiré ici), le clone partiel sur le dépôt réel, les jetons.

## 4. Comptes

- Modules neufs : 9 fichiers sous `src/controle_ia/t06/` (1 919 lignes) ; scripts : 3 (524 lignes) ; essais : 7 fichiers
  (1 131 lignes, 50 fonctions d'essai, 76 cas avec les paramètres). Aucun module gelé touché (diff de l'arbre gelé vide).
- Suite des essais de T0.6 (les sept fichiers, en un seul processus) : **76 passed in 68.30s**, 2026-11-05, environnement
  `.venv` du dépôt (Python 3.13.18, torch 2.14.1, transformers 5.18.0, numpy 2.4.6, scipy 1.17.1). La répétition jouet
  seule : 3 passed, ≈ 40 s (deux répétitions de suite avec la configuration v2, entropies neuves : 3 passed, 3 passed).
- Banc de mutations (`docs/notes/g0-deux-semaines-v1/banc-mutations-t06-v1.log`, `.json`) : 7 témoins verts, **29 mutations,
  29 tuées, 0 survivante, 0 inapplicable** (coût 2, distillation 3, identité 3, test croisé 6, lecture 3, session 4,
  configuration 1, lanceur 2, amorce 3, lanceur de session 2).
- `verifier-arbre .` : aucun problème sur les fichiers rendus (81 problèmes préexistants au commit de base `06765457`,
  étrangers à ce travail : fichiers SPARKS et procédures sans sceau) ; `sha256sum -c docs/sha256sums-lancement-v2.txt` : OK.
- Disque : arbre de travail 2,4 Go (aucune installation, `.venv` réutilisé) ; temporaires des essais sous
  `/tmp/pytest-of-root` (bornés par pytest).
- Temps : début 15:59 UTC, fin au dernier commit (heure dans la réponse finale) ; aucune location, aucun réseau, aucune clé.

## 5. Dix points pour un contre-lecteur

1. **Dose 0 et adaptateur chargé.** La phase `dose0` charge l'adaptateur saboteur à dose 0 (« adaptateurs injectés,
   dose 0 ») ; le contrôle d'identité prouve l'égalité au bit près avec les logits pris avant l'injection. Vérifier que la
   simple précision (`_forward_simple`) ne touche pas le chemin à dose 0 (`test_simple_precision_garde_la_base_au_bit_pres`).
2. **Rechargement de l'état sauvegardé.** L'évaluation lit l'adaptateur tel que sauvegardé en float16 (puis porté en
   float32), pas l'état entraîné en float32 : perte de précision déclarée, pour que les empreintes des phases soient celles
   des fichiers poussés. Alternative : sauvegarder en float32 (54 Mo par adaptateur) ; `adaptateur.sauvegarde` le permet.
3. **Deux adaptateurs sur une seule injection.** `etat_initial` reconstruit A par les graines dérivées de l'adaptateur
   (même dérivation que `injecter`) ; B = 0. Le témoin et le saboteur ont donc des A différentes. À relire : est-ce bien
   ce que le texte veut (« un adaptateur saboteur, un adaptateur témoin ») ?
4. **Jeton de fin dans la cible.** La perte porte sur les identifiants générés de l'action, jeton de fin de tour compris
   (l'adaptateur apprend aussi à clore) ; les activations notées excluent ce jeton (`_fin_notee`, comme P3).
5. **Aire moyenne et plancher apparié.** Le pli k est noté par la sonde apprise sur l'autre ; la direction j du pli k est
   tirée de la covariance des jetons d'entraînement de cette sonde ; l'aire du plancher j est la moyenne des deux plis ;
   l'intervalle rééchantillonne les tâches dans chaque pli. Le plancher par permutation est descriptif.
6. **Prédicteurs triviaux.** Longueur notée, rang du pas, mention étendue (motifs de P3 + mots de P3-bis). Le coût seul
   est une base rapportée à côté, pas un prédicteur trivial : une sonde au-dessus que le coût seul égale reçoit la réserve
   « base boîte noire gratuite », pas l'état « non interprétable ». Est-ce la lecture voulue du brouillon ?
7. **Tendance.** Statistique de Jonckheere–Terpstra avec une valeur par tâche et par dose (U ∈ {0, ½, 1} par paire de
   doses) ; valeur p (r + 1)/(n + 1) sur 10 000 permutations dans chaque tâche. Une tâche sans statistique à une dose est
   exclue, nommée. À confronter à la formule attendue par le rédacteur du brouillon 4.
8. **Table A, ligne A1b.** Elle se déclenche aussi quand T6-1 n'est pas calculable (texte : « ou T6-1 non calculable »).
   La réserve « moins de la moitié des actions de (ii) à dose 1 lisibles » compte les coûts strictement positifs.
9. **Chaîne de session.** Le script n'exécute jamais `vastai create` : il imprime la commande (jetons par leur nom) et
   rejoue la garde de calcul dessus ; la surveillance n'arrête que sur « RUN MORT » ou dépense ≥ 200 USD (prix de la carte +
   stockage × heures depuis la création, facture relevée si plus grande) ; aucun relancement automatique. L'amorce arrête
   l'instance à l'état « stopped » en fin normale et la détruit sur refus ou redémarrage. La fin du 16 novembre (échéance
   du GO) borne la minuterie.
10. **Ce qui manque avant la course.** Le préenregistrement candidat avec ses huit citations (« Entropie », « Configuration
    de T0.6 (empreinte canonique) », « Tâches d'évaluation de T0.6 », « Tests attendus », les quatre « Chemin … »),
    l'amorce citée par son empreinte, la configuration réelle copiée sous `prereg/` (brouillon fourni ici), les longueurs
    des textes instruits sur les 32 tâches de réserve (point 3 du brouillon), la répétition finale à blanc, le
    préenregistrement de T0.7 en mode « coût », `sondes_figees_p3` à brancher s'il l'exige.

## 6. Commandes exactes

- Répétition jouet (de bout en bout, ≈ 40 s) et tous les essais de T0.6 :
  `cd /home/claude/wt/t06-lanceur-v1 && PYTHONPATH=src timeout 900 nice -n 10 /home/user/controle-ia-travail/.venv/bin/python -m pytest -q tests/test_t06_cout.py tests/test_t06_distillation.py tests/test_t06_test_croise.py tests/test_t06_lecture.py tests/test_t06_session.py tests/test_t06_lanceur_jouet.py tests/test_t06_scripts.py`
- Banc de mutations : `cd /home/claude/wt/t06-lanceur-v1 && PYTHONPATH=src timeout 3000 nice -n 10 /home/user/controle-ia-travail/.venv/bin/python -I -B scripts/banc_mutations_t06_v1.py SORTIE.json`
- Lanceur seul, en mode jouet, hors essais (il faut des fichiers de tâches scellés et une configuration scellée dont les
  empreintes des tâches sont remplies, comme le fait `tests/test_t06_lanceur_jouet.py::_preparer`) :
  `PYTHONPATH=src python -m controle_ia.t06.lanceur --config <config-jouet scellée> --run-id AAAAMMJJ-HHMMSS-t06-jouet`
- Course réelle (après scellement du candidat et des pièces, et GO toujours valide ; la session exécute elle-même la
  commande imprimée) :
  1. `bash scripts/lancer_t06_v1.sh controles <DOSSIER_NEUF>` ;
  2. `bash scripts/lancer_t06_v1.sh creation <OFFRE> <PRIX_CARTE> <PRIX_STOCKAGE> <DOSSIER> [ECHEANCE_UTC_S]` → exécuter la
     commande imprimée (elle enchaîne `apres-creation`) ;
  3. `bash scripts/lancer_t06_v1.sh surveillance <ID> <CREATION_S> <PRIX_CARTE> <PRIX_STOCKAGE> <DOSSIER>` ; sur
     `ARRET …` ou `FIN`, exécuter `timeout -k 5 120 vastai stop instance <ID>` (arrêt par l'identifiant, R10) ; après le
     verdict, destruction par l'identifiant.
  Variables de l'amorce : `COMMIT` (commit de scellement), `PREREG`, `BRANCHE` (`calcul/t06-reel-v1`), `DEPOT_URL`
  (`https://github.com/lciric/controle-ia-travail.git`), `ECHEANCE_UTC_S`, `HF_TOKEN`, `GH_TOKEN`.

## 7. Réserves et trois risques

- Risque 1 — mémoire et durée sur le modèle réel : distillation par transcription entière (≈ 4 000 jetons, lot 1,
  rétropropagation à travers 32 couches bfloat16) non éprouvée sur carte ; activations complètes sur le disque de l'instance ;
  test croisé en 4 096 dimensions avec quinze couples famille × couche (`couples_descriptifs` peut le couper).
- Risque 2 — pièces non branchées ou non vérifiées : `sondes_figees_p3` accepté mais non branché ; interface de Vast
  (minuterie, arrêt, DELETE) copiée, non tirée ; le clone partiel (`--filter=blob:none`) sur le dépôt réel non essayé ;
  `fils_test_croise` lu par `config.get`, hors de `CLES_T06`.
- Risque 3 — lectures à valider par le rédacteur : la statistique de tendance et sa valeur p, la règle « non
  interprétable » (prédicteurs triviaux) contre la base « coût seul » (réserve), la ligne A1b sur T6-1 non calculable, le
  rechargement en demi-précision des adaptateurs, et l'absence de garde « plus de 1 % de tirages dégénérés » sur les
  lectures du coût (elles n'ont pas de tirage dégénéré par construction).
