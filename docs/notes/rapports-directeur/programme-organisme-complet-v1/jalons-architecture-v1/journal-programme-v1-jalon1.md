# Journal du rédacteur de l'architecture de l'organisme — jalon 1 (sources lues, cloison tenue)

- **Rédacteur** : sous-agent neuf de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, modèle Claude Opus 5.5 ; je n'ai écrit
  aucune pièce de l'organisme ni du programme.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-architecture-programme-organisme-v1.md`,
  sha256 `7335655c594f41acb78f19fdfddad98af8e2bd7f65e3efbb909b7a855aaacf92` (égale à son compagnon, vérifiée à 11:59 UTC) ;
  interdits communs v2 `1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f` (égale à son compagnon).
- **Heures** (relevées par `date -u`) : début 11:59:11 UTC le 10 novembre 2026 ; ce jalon écrit après le relevé de 12:11:41 UTC.
- **Pourquoi un dossier de jalons** : l'outil de scellement refuse d'écraser une empreinte (R12) ; chaque jalon prend donc un nom
  neuf dans `jalons-architecture-v1/`, sous le dossier de sortie nommé par la consigne ; les fichiers finaux portent les noms
  exacts de la consigne.

## 1. Cloison et interdits : ce que je n'ai pas ouvert, et pourquoi

| chemin ou objet | geste | raison |
|---|---|---|
| `docs/notes/bras-attaque/` | non ouvert ; absence vérifiée par `test -d` seulement (dossier non extrait) | interdits 1 et 9 ; cloison R-2152, R-2170 |
| `orchestrator/pole/bras_attaque_v54.py` du dépôt public | ni ouvert, ni haché, ni passé à un script (exclu de chaque `git grep`) | cloison du bras ; existence seulement |
| `orchestrator/pole/reserve_tenue_a_l_ecart_v60.py`, `_v61.py`, leur démonstration et leurs deux modules d'essais | ni ouverts, ni hachés (exclus de chaque `git grep`) | rien sur le mode tenu à l'écart au-delà de son existence (prudence : la réserve du tour fermé peut s'y rattacher) |
| ligne 202 du `README.md` public (elle nomme le pôle du bras) | sautée à la lecture | même raison |
| sections « 3 bis » (adversaire scellé) et « 3 ter » (classes d'attaque cibles) du programme de conception v7 de conv-audit | non lues (seuls les titres, vus dans la table des matières) | niveau méthode (R-607) et cloison |
| dossier `bras-attaque-v1/` de la branche `canal/conv-audit-n04` | non ouvert (nom vu dans une liste de dossier) | cloison |
| `docs/notes/ideation-organisme-v1/course-2/coffre-attaques-inedites-v1/` | non ouvert (une ligne vue par `git grep` : décision D2 de Lazar sur N12, R-1057) | prudence : coffre d'attaques |
| `registres/index-bras-attaque-v1.md` | non ouvert | cloison |
| tout `donnees/`, toute branche `donnees/…` (collisionneur v8, v9, N12-N13) | non ouverts ; listés à partir du registre seulement | sorties scellées jamais lues (R1) |
| « programme depuis zéro » et « organisme depuis zéro » (toutes versions), `depuis-zero-comparaison-v1/`, `dossier-entretien-27-novembre-v1/pieces-bras-v1/` | non ouverts | cloison ; je n'ai pas pu établir quelles versions viennent de la session du bras, donc aucune n'est ouverte |
| `git log --all`, `git fetch`, `git ls-tree` | jamais lancés | interdits 1 et 4 ; les autres branches sont lues par `git show <commit>:<chemin>` seulement |

Aucun appel de modèle, aucune dépense, aucune clé lue, aucune commande d'environnement. Aucune recherche récursive : `git grep`
avec exclusions, ou `grep` sur des fichiers nommés.

## 2. Sources lues (empreintes calculées par `sha256sum` à 12:11 UTC)

### Dépôt de travail (`main`)
| pièce | sha256 | lecture |
|---|---|---|
| `docs/notes/rapports-directeur/rapport-principes-etat-goulots-entretien-organisme-2026-11-09-v1.md` | `22263fced8d43771f0a34b3cdd9b0e6b318e39d23189907a3e9736e74413b984` | entière |
| `docs/decisions/decision-N-044-v1.md` | `2b70bdac014d366d058a530680d016663b35ed73b8ca0cae9f2369206f5004bf` | entière |
| `docs/decisions/decision-N-045-v2.md` | `c7b05e39de381cee1d5ec2276745a0310bd3cc0857a6be0e0fb14eeb5042261d` | entière |
| `docs/decisions/decision-N-049-v1.md` | `8a5bf5e57e2bb447467388acb572e032d1a6a578a868db1b7304263a1c9d4460` | entière |
| `docs/decisions/decision-N-050-v1.md` | `a54b128df955dba34bb360fa2fea466c787026a934f25135d698e8cd925d5f58` | entière |
| `docs/decisions/decision-N-052-v1.md` | `817d218b22b8d1d4a2c03bb78fb4870867f19bd1a1f9c08b0a1873efbb31a384` | entière |
| `docs/decisions/decision-N-053-v1.md` | `2204256d744288be2708578c0fdc8c44c62a29b70b2727ed7e31ec142d1cdeae` | entière |
| `docs/decisions/decision-N-058-v1.md` | `854f2724864f1e45394e001f4aca7b0248753e5d2b0a66991e2ee8a7be87de9d` | entière |
| `docs/decisions/decision-N-059-v1.md` | `41aff854c38bed3a43aced62bd0c1b3af782c5a5f6174f335a175847b407e687` | entière |
| `docs/decisions/decision-N-060-v3.md` | `2b448f696503112c4acebd3d56748e2c9d9931d9e597f1991e3f278e651c5591` | entière |
| `docs/decisions/decision-N-064-v1.md` | `387c9d4eda5a1b3d0e8ec61def715bb88c1bf9883081d5796ea291879be63f97` | entière |
| `docs/decisions/decision-N-065-v1.md` | `f820e90da0920d505d22bc7b33fad4906181d43bd5af7e79418a3c161a8a65c4` | entière |
| `docs/notes/ideation-organisme-v1/course-2/collisionneur-n12-n13-v1/synthese-n12-n13-v2.md` (synthèse scellée) | `f0340581766c5fb4d97a0ccb06f0cf1738a15228385b332ee602e93a0be28f0a` | l. 1-32 et 63-108 |
| `docs/notes/rapports-directeur/resultats-pour-documents-v3/section-resultats-organisme-v3.html` (non contre-lue) | `d6d702f5383347f16c894065ce45d96745a20f6016243d5f3b956828b3a3d9fd` | entière |
| `docs/notes/rapports-directeur/resultats-pour-documents-v3/registre-affirmations-v3.md` | `38c24c925e151dc50f8b5b59eee9d8ff04c9b08e2cc4f52a9d9206553905780e` | abréviations et lignes B1-B53 |
| `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-inventaire-idees-organisme-v1.md` | `2f16dfd064540f9b360da7855424cad6fe6141bb584a6aead8ddee76f3fc7da1` | entière (pour ne pas refaire l'inventaire) |
| `registres/passations/2026-11-10-1159.md` | `e113d747251b1f004b55d7f7c549f08f83d226a9cd19b8f80e493b180d762121` | lignes sur l'organisme, § 5 à 7 |
| `brouillons/entretien-taif-v3/programme-entretien-taif-v16.md` | `186173d9d9b949bfb3922503adff1be9d60f49f07fb975750de4c88bd60a060e` | l. 300-330 seulement |
| `registres/decisions.md` (vivant) | `ffa5a882c112bbbed6aae01613677f33d5fc562275073003bc19e13589fcd7c6` à 12:11 UTC | lignes R- citées une à une |
| `registres/etat.md` (vivant) | `1ef56d65e747b59761833a17273a954d1398b5a505a7a076ec49c305cdadd548` | en-tête, l. 39-45, 65, 69, 198 |
| `registres/go.md` (vivant) | `2c396b016d4ab86bd3f09cc7e21173f19d0c9765cc1a85b8efc08e59c2bc39f0` | lignes de GO de l'organisme |
| `registres/depenses.md` (vivant) | `5268f0f09943ab37d103534206121a30a28b76807b8eae6bac98c3e0d77b02a9` | lignes des collisionneurs et courses de l'organisme |

### Dépôt public de l'organisme (`/home/user/ideation-organism`, tête `651019905ec267c2f339997a6bd67cb3707c4945`)
| pièce | sha256 | lecture |
|---|---|---|
| `README.md` | `b72c983eada4449931ff828d4e841aaf6708bce881657c745a8c113f3392321e` | entière sauf la l. 202 |
| `MANIFEST.md` | `c58638c9966d01ac1741ed90602e038e90b7e668d1e0cc58020cc670579fcf86` | structure, exclusions, lots ajoutés |
| `orchestrator/conception-v7-v1.md` | `31fc8c4bc286341fcbf10181be6779ecd20ddf9de092a2c885ce8d11b27fedee` | entière |
| `pont-fiche-loi-v1/LISEZMOI-pont-v1.md` | `7b1c131db760014798af159047849163bedc03b706f2f684dd0962ac4d6bd17a` | l. 1-60 |
| `orchestrator/pole/adaptateurs.py` | `a1a8ede8d38884a28365ee797dcd3018dbf09ea1baefa3f57cfcb3281c529c99` | l. 15-30 (rôles) |
| docstrings de tête de chaque module de `orchestrator/pole/` (fichiers cloisonnés exclus) | — | première docstring, 230 caractères |
| historique (`git log`) | — | tous les commits, sujets tronqués |

### Autres branches (lues par `git show <commit>:<chemin>`)
| pièce | sha256 (calculée sur la sortie de `git show`) | lecture |
|---|---|---|
| `origin/canal/conv-audit-n04` (`ec3863bbc`) : `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/programme-conception-organisme-v7.md` | `b7cd2f56bf99357caf51493ca0ed966753711926c91c094f971197b29c7192fd` (égale au compagnon) | l. 1-151 et 321-fin ; § 3 bis et 3 ter non lus |
| même dossier, `programme-conception-organisme-v6.md` | `6e95f6c5ae6bec23b86ec4eaca39d50ddd02a9e071942d99a74004827c6271c3` | l. 44-214 |
| même dossier, `programme-conception-organisme-v1.md` | `72fa0e609258d1a208195440c645f2b7f250c5c5bba70e304407ded09de3c6ff` (égale au compagnon) | recherche « couche » seulement |
| `origin/prep/organisme-v65-v1` (`3daf08e24`) : `docs/notes/organisme-boucle-reelle-v1/code-v65/rapport-developpeur-organisme-v65-v1.md` | `f84c14303eacf87e7e129955d3f9b7ba35fc7504545033c37b66b9c4ad5aff0c` | l. 1-60 |

## 3. Premiers constats qui orientent l'écriture

1. **Deux numérotations de « couches » coexistent** dans les pièces, plus une troisième dans les mots de la session-dépôt :
   (i) « couches d'essai sur le monde réel » 0, 1, 1 bis, 2, 3, 4 (programme de conception v6, § 4) ; (ii) « ordre de
   conception » 1 à 4 (v6, § 3 : proposeur v7 ; réécriture des rôles sous bac à sable v8 ; bras d'attaque, remplacé par neuf voies ;
   pôle théorie) ; (iii) R-920 et N12 : « couche 3 = réécriture de soi sous bac à sable ; couche 4 = pôle théorie et Lean ». Les
   couches 1 et 2 de la numérotation (iii) ne sont définies dans aucune pièce lisible lue ; la question N12-N13 qui les fixait peut-être
   est sous `donnees/` (non ouverte). Le document les présentera côte à côte, sans fusion silencieuse.
2. **« Organisme » a deux sens dans le dépôt** : les organismes-modèles saboteurs du programme de contrôle (T0.5, T0.6, « couche 1 bis »
   et « couche 2 » de T0.5 au registre) et l'organisme d'idéation. Le document ne traite que le second, et signale les homonymies.
3. **Décidé n'est pas codé** : la composition apprise, le coût dans le signal, la récompense d'héritage, le vivier par génération,
   `test_final`, les espèces `LOCAL:` et les questions ouvertes (N-044, N-045, N-049, N-050) n'ont aucune occurrence dans le code
   public de l'organisme (recherche par `git grep`, 12:11 UTC) ; le vivier de conception existe dans le noyau de l'étape 1
   (`noyau/vivier.py`, cité par N-049), autre base de code.
4. **Fait neuf pendant la lecture** : GO-2026-11-10-10 inscrit à 12:05 UTC (R-2206 ; enveloppe de 120 USD dont 45 pour la boucle
   réelle de l'organisme, mêmes conditions que GO-2026-11-08-02), qui lève le nœud de R-2202.

## 4. Plan du document (structure minimale de la consigne)
§ 1 objectif ultime et lien des lignées ; § 2 couches ; § 3 rôles et pôles ; § 4 juge, mondes plantés, pont, tests de mort, tour
fermé, boucle réelle v65 ; § 5 attaques et défenses du juge ; § 6 composition apprise, coût, héritage, vivier, `test_final`,
contre-lecteur, audit défensif ; § 7 rôles de l'organisme dans le programme ; § 8 calendrier, dépenses, GO, nœuds, prochains pas ;
table finale « mécanisme → état → source ».
