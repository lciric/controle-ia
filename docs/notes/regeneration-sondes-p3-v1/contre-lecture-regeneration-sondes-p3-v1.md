# Contre-lecture (R2) — régénération du fichier complet des sondes figées de P3 — v1

Contre-lecteur neuf : sous-agent Opus 5.5, qui n'a rien écrit de ce qu'il relit. 28 octobre 2026.
Objet relu : devis (§ 3), fiche de lancement, `scripts/regenerer_sondes_p3_v1.py`, `scripts/regeneration_sondes_p3_instance_v1.sh`,
`scripts/amorce_regeneration_sondes_p3_v1.sh`, `docs/procedures/regeneration-sondes-p3-v1/lancer_regeneration_sondes_p3_v1.sh`,
`tests/test_regenerer_sondes_p3_v1.py`. Code de P3 lu au commit `97dd829` (`run.py`, `figees.py`, `manifeste.py`,
`harnais/validation_reelle.py`, `harnais/modeles.py`, `sondes/familles.py`, `sondes/evaluation.py`, `scripts/p3_instance.sh`).
Références : `diag/20261019-230011-p3-reel/sondes-figees.json`, `runs/20261019-230011-p3-reel/manifeste.json`. Banc : `banc-a.log`,
`banc-b.log`, `c1.log` à `c4.log`. Essais jouets relancés : **9 réussis** (214 s).

## Verdict : **lançable après corrections**

Aucun chemin ne donne un faux « accepté ». Le palier 1 se vérifie de lui-même (sceau). Au palier 2, des graines fausses ou des
données fausses finissent en « refusé ». Les gardes de P3 passent dans cette disposition. Le lanceur de P3 est bien appelé sans
changement, depuis l'arbre au commit `97dd829`, avec l'entropie citée par le préenregistrement. Il reste un défaut de conception
(CLR-01) : tel qu'il est monté, le run ne peut presque pas atteindre l'identité au bit près, qui est le but de la dépense. Il y a
aussi cinq défauts majeurs. Chacun se corrige en moins d'une heure, sans dépense.

## Constats

### CLR-01 — bloquant — `taskset` change le nombre de fils de l'algèbre linéaire de numpy, et rend le palier 1 presque inaccessible
- Fichiers : `scripts/regeneration_sondes_p3_instance_v1.sh:173` (`taskset -c 0-29`) ; fiche § 1 ; code de P3 touché :
  `sondes/familles.py:261-263` (`np.cov`, puis `np.linalg.inv` pour les six matrices de Mahalanobis) et `sondes/evaluation.py:74-79`
  (`np.linalg.cholesky` pour les 400 planchers).
- Défaut : la fiche ne raisonne que sur les fils de torch (`fils_effectifs` = 30). Elle oublie la bibliothèque d'algèbre linéaire de
  numpy (OpenBLAS, livrée avec numpy 2.4.6, compilée avec `MAX_THREADS=64`). Cette bibliothèque prend autant de fils que l'affinité
  du processus, dans la limite de 64. Elle ignore le quota du groupe de contrôle. P3 tournait avec une affinité de 128 et sans
  `taskset`, donc très probablement avec **64 fils** : c'est une inférence, P3 ne l'a pas consigné. La régénération, bornée à
  30 cœurs, en aura **30**.
- Mesure faite ici (scratchpad `cl-regen/blas.py`, `chol.py`, `ob.py` ; numpy 2.4.6) :
  - `np.linalg.inv` d'une covariance 2 048 × 2 048 donne quatre empreintes différentes avec 1, 2, 3 et 4 fils ;
  - `np.linalg.cholesky` diffère entre 1 et 2 fils ;
  - `np.cov` ne bouge pas.
  - Sous `taskset` à 2 cœurs, la variable `OPENBLAS_NUM_THREADS=4` reste plafonnée à 2 fils.
  - En revanche, un appel `scipy_openblas_set_num_threads64_(4)` à l'exécution donne bien 4 fils, et **le même résultat au bit
    près** que 4 fils sans `taskset`.
  - Conclusion : seul le nombre de fils compte, pas les cœurs sur lesquels ils tournent.
- Conséquence : avec 30 fils, les matrices de Mahalanobis, et sans doute les planchers, diffèrent dans les derniers bits. Le sceau
  `91b61c45…` est alors presque sûrement inaccessible. L'issue attendue devient « accepté avec déclaration », que Lazar voulait
  éviter (R-646). Ce n'est pas un faux verdict, mais une dépense qui manque son premier objet.
- Correction :
  1. Dans `regenerer_sondes_p3_v1.py`, avant `rp.executer`, importer numpy.
  2. Trouver sa bibliothèque OpenBLAS (`numpy.libs/*openblas*`), lire sa configuration (`scipy_openblas_get_config64_`) et fixer
     `scipy_openblas_set_num_threads64_(64)`.
  3. Relire le nombre obtenu. S'il diffère de 64, ou si `MAX_THREADS` n'est pas 64, arrêter en code 1.
  4. Consigner la configuration et le nombre de fils dans le rapport.
  5. Ajouter `env | grep -i -E 'thread|omp|mkl|blas'` à `machine.txt`.
  6. Ajouter un essai jouet (sous `taskset` à un cœur : nombre relu = valeur demandée).
  7. Écrire dans la fiche que les 64 fils de P3 sont **inférés** (affinité 128 consignée, plafond 64 de la bibliothèque), non
     consignés.
- Si l'on ne corrige pas : la fiche doit annoncer que le palier 1 est improbable par construction.

### CLR-02 — majeur — Les fils effectifs ne sont pas gardés avant le calcul
- Fichiers : chaîne `:140-141` ; script `:247-249` ; P3 `run.py:430-431`.
- Défaut :
  - Le contrôle `nproc --all ≥ 30` compte les processeurs de l'hôte. Il ignore le quota et l'ensemble de cœurs permis : ce contrôle
    est presque vide.
  - P3 calcule `fils_effectifs` seulement à l'entraînement, donc après la descente du modèle et l'extraction.
  - Un quota inférieur à 30 donnerait moins de fils, et des sondes probablement différentes. Le verdict rapporte les deux nombres
    mais n'en tient pas compte. On risque un « refusé » payé, ou un palier 2 obtenu dans d'autres conditions sans que rien le
    signale.
- Correction :
  - Dans le script, avant `executer`, poser `f = rp.fils_effectifs(config["fils_entrainement"], rp.coeurs_disponibles())` et exiger
    `f == ref_diag["fils_entrainement_effectifs"]` (30) ; sinon code 1. On ne perd alors que l'installation.
  - Ajouter au rapport un champ `conditions_egales` (fils de torch, fils d'OpenBLAS).
  - Dans la chaîne, prendre les 30 premiers cœurs de l'affinité réelle plutôt que `0-29` : les cœurs 0 à 29 peuvent manquer à
    l'ensemble permis du conteneur, et `taskset` échouerait. De préférence, prendre 30 cœurs physiques distincts (`lscpu -p`).
    Vérifier que `taskset` réussit.

### CLR-03 — majeur — La garde de calcul du lanceur ne bloque rien
- Fichier : `lancer_regeneration_sondes_p3_v1.sh:57-58` : `printf … | python3 garde_calcul.py && echo …`.
- Défaut : sous `set -e`, une commande qui échoue au milieu d'une liste `&&` n'arrête pas le script, et le piège `ERR` ne se déclenche
  pas. Je l'ai démontré : la garde rend 2 et le script continue jusqu'à la création. Si le GO était échu ou absent, l'instance serait
  quand même créée. C'est une garde jamais éprouvée sur un artefact (R5) et un repli silencieux.
- Aujourd'hui sans effet : GO-2026-10-28-11 est valide jusqu'au 15 novembre.
- Correction : `… | python3 …garde_calcul.py || { echo "garde de calcul : refus"; exit 2; }`, puis l'éprouver avec un GO inconnu. Le
  même motif vient sans doute de `lancer_banque_t05_v4.sh` : le vérifier là aussi.

### CLR-04 — majeur — Le fichier complet est perdu en cas de refus ou de panne après les sondes
- Fichiers : chaîne `:185-188` et `:196-209` ; `consigner_arret` (`:107-116`).
- Défaut :
  - Les morceaux ne sont poussés que si le verdict n'est pas « refusé ».
  - Une panne du code de comparaison après l'arrêt volontaire (code 1) ne pousse rien non plus.
  - Dans les deux cas, le fichier de 820 Mo ne vit que sur l'instance, que la session détruit « dès le versement lu ».
  - Or un refus de justesse (par exemple 2e-6 sur une sonde), ou un nœud qui décide « sondes v2 déclarées » (devis § 3.3), exigerait
    alors une seconde dépense.
- Correction : verser les morceaux dès que `donnees/$RUN/sondes-figees.npz` existe et que son sceau égale celui du résultat, quel que
  soit le verdict. Le commit porte le verdict ; rien n'est lu sans nœud (devis § 3.3 : « rien n'est utilisé », ce qui n'interdit pas de
  conserver). Dans `consigner_arret`, faire de même si le fichier existe.

### CLR-05 — majeur — La fiche de lancement n'est pas scellée
- Fichiers : `docs/notes/regeneration-sondes-p3-v1/` (aucun `fiche-….md.sha256`) ; lanceur `:45` (ne contrôle que le devis).
- Défaut : le devis § 5.2 exige « la fiche de lancement, avec le critère du § 3, scellée » (R6). L'extension du GO pose la même
  condition.
- Correction : sceller la fiche après les corrections, et ajouter son contrôle au lanceur (étape 2).

### CLR-06 — majeur — Rien n'arrête la facturation si la session se perd
- Fichiers : fiche § 5 ; amorce `:31-36`.
- Défaut : l'amorce se termine, mais l'instance reste payante jusqu'à son arrêt par la session. Si la session tombe (fenêtre de dix
  heures en autonomie), on dépasse le plafond de 6 USD après environ 4 heures à 1,40 USD de l'heure.
- Correction :
  - À la création, programmer un réveil de la session (tâche programmée « une fois ») à création + 3 h, puis + 4 h, qui inventorie
    et arrête par identifiant (R10).
  - Consigner dans `lancement.txt` l'heure limite d'arrêt.

### CLR-07 — mineur — Biais non finis non détectés
- Fichier : script `:114-117`.
- Défaut : `abs(nan - nan)` ou `abs(inf - inf)` donne `nan`. Ensuite `max(nan, …)` dépend de l'ordre des arguments, et
  `nan > tolérance` est faux : la sonde passe. Le tri de `pires` est faussé de la même façon.
- Correction : exiger `math.isfinite` des deux biais, sinon signaler un problème et compter un écart infini.

### CLR-08 — mineur — Le § 3 (a) compare au fichier léger régénéré, et non au fichier régénéré
- Fichier : script `:241`.
- Défaut : on compare la référence au fichier **léger** régénéré, et l'on suppose qu'il a été tiré des mêmes objets que le fichier
  complet. C'est vrai dans le code de P3, mais rien ne le vérifie. On ne vérifie pas non plus les six matrices de Mahalanobis
  (présence, forme 4 096 × 4 096, valeurs finies). Seules leurs aires sont contrôlées.
- Correction : comparer la référence au fichier **complet** régénéré, par nom, en exigeant que le surplus soit exactement les six
  sondes de Mahalanobis. Vérifier `meta.complet` du fichier léger contre le sceau du fichier complet. Vérifier que `mu` et `P` sont
  finis et que `P` est symétrique.

### CLR-09 — mineur — Graines et versions non confrontées à celles de P3 dans le verdict
- Fichier : script `:244-255`.
- Défaut : le rapport ne reprend ni l'empreinte du nouveau manifeste, ni ses graines, ni ses versions (torch, numpy, transformers),
  et ne les compare pas à `runs/20261019-230011-p3-reel/manifeste.json`. Il n'y a pas de faux « accepté » possible (des graines
  fausses font échouer le palier 2), mais la provenance (R9) n'est pas affirmée.
- Correction : copier le manifeste de P3 dans `regen/ref/` (scellé). Exiger l'égalité de `graines`, de `config_sha256` et de
  `commit`. Rapporter les versions côte à côte.

### CLR-10 — mineur — Reconstitution des morceaux non vérifiée sur l'instance
- Fichier : chaîne `:198-200`.
- Correction : `cat sondes-figees.npz.morceau-* | sha256sum` doit égaler le sceau du fichier complet avant le premier commit.

### CLR-11 — mineur, hors de ce run — Poids du dépôt
- Défaut : `.git` pèse déjà 706 Mo, et les morceaux y ajoutent environ 820 Mo. Chaque instance future clone deux fois l'ensemble
  (amorce et chaîne, `git clone` sans `--single-branch`).
- Correction : à décider (stockage ailleurs, ou clones futurs en `--single-branch --branch main`). C'est un nœud du dépôt distant si
  l'on change de stockage.

### CLR-12 — mineur — Banc incomplet (R5)
- Défaut : le chemin **réel** du script n'a jamais tourné sur un cas sain : garde du répertoire courant, commit et arbre propre,
  `exiger_code_importe_sous` avec le script hors de l'arbre, `exiger_code_cite`, entropie citée, `creer_manifeste` avec le
  préenregistrement.
  - `c4` s'arrête à la carte, avant tout cela.
  - Les essais jouets remplacent `importer_p3`. Le banc A l'exerce, mais en mode jouet.
  - Aucun artefact n'éprouve CLR-01, CLR-02 ni CLR-07.
- Correction : un banc D gratuit sur processeur.
  - Clone à `97dd829`, `.venv` dans l'arbre, script en mode réel avec `--prereg`.
  - Arrêt attendu à « mémoire vive » ou à « processeur graphique demandé », avec `arret.json`.
  - Vérifier que les graines du manifeste créé égalent celles de P3.
  - Ajouter les essais jouets des corrections.

## Points vérifiés et conformes
- Le lanceur de P3 est importé depuis `racine/src` (`importer_p3`). `exiger_code_importe_sous` passe : le script est copié dans
  `/root/regen` et le chemin d'import est `racine/src`.
- L'arbre reste propre : `.venv/` et `donnees/` sont ignorés au commit de P3, le journal est hors de l'arbre, pytest tourne avec
  `-p no:cacheprovider`.
- `exiger_code_cite` compare des commits et passe, car HEAD est `97dd829` (le nom de branche ne compte pas).
- L'entropie vient du préenregistrement, que le mode réel rend obligatoire. Les graines ne dépendent que de l'entropie et des noms
  des tâches, pas de l'identifiant du run.
- `figees.ecrire_sondes` est déterministe : les horodatages internes du fichier zip sont fixés à 1980 quand `zipf.open` reçoit un nom.
  L'identifiant du run et la racine n'entrent pas dans le fichier.
- L'arrêt volontaire passe par `except Exception` dans `executer`, ce qui écrit `arret.json`. Il survient après l'écriture et le
  scellement des deux fichiers et du résultat `sondes-figees.json`, et avant le premier épisode.
- `verdict` suit le § 3 :
  - comparaison par nom ;
  - sondes manquantes ou en trop, formes, valeurs non finies dans les tableaux ;
  - égalité à la tolérance acceptée, au-delà refusée ;
  - comparaison vide refusée ;
  - aires d'un seul côté refusées.
  - La référence compte 30 aires, toutes finies.
- Les sceaux des références sont vérifiés deux fois. Le sceau attendu est vérifié contre la référence et contre le texte du script
  (lanceur, ligne 47).
- Jetons : jamais affichés. L'assistant d'identification écrit `${GH_TOKEN}` littéralement dans la configuration git, et la réponse
  de création est masquée.
- Branche vérifiée absente, puis poussée avant l'installation.
- Plafonds de temps : 240 minutes pour l'amorce, 150 minutes pour le run, arrêt TERM consigné.
- Le choix de l'offre est conforme à la fiche : EPYC 7513, au moins 31 cœurs, au moins 128 Go, CUDA ≥ 13.

## Non vérifié
- Le nombre de fils d'OpenBLAS réellement utilisé par P3 : 64 est inféré.
- L'identité au bit près, d'un hôte à l'autre, de l'extraction sur carte (même modèle de carte, pilote différent possible) et de
  l'entraînement de torch sur processeur : la bibliothèque mathématique d'Intel sans mode reproductible, l'alignement de la mémoire.
- La numérotation des cœurs de l'hôte (cœurs physiques ou jumeaux) et l'ensemble de cœurs permis par le conteneur.
- La durée réelle et la tenue du budget d'entraînement de 3 600 s sous 30 cœurs.
- Aucun calcul réel n'a été lancé.
