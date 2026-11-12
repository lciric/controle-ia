# Essai Lean, outillage D-1a — rapport des corrections du harnais — v6

- **Pour** : la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`.
- **Écrit par** : l'auteur du harnais (sous-agent développeur, Opus 5.5, `claude-opus-5-5`).
- **Heures** (relevées par `date -u`) : contre-lecture vérifiée à 10:57 UTC ; rapport vers 11:30 UTC.
- **Lu, empreinte vérifiée** : `contre-lecture-courte-machine-harnais-d1a-v5.md` (`897b7438…`, égale à son compagnon), et la
  ligne R-2333 de `registres/decisions.md`.
- **Contexte** : le conteneur a été réinitialisé ce matin. Je suis reparti de `795fc074`, récupéré par refspec ; mon ancien
  bac à sable avait disparu.

## Livrable

- **Commit** `149babdc56f51925e9bc4e93a61041cc755bd2a3` (arbre `a9dfcbb1fe6f7df3b71153f7907a46b4b1c02089`), sur la
  branche `prep/lean-outillage-d1a-v6`, partie de `795fc074`.
  - Poussée seule, **sans fusion** ; deux commits intermédiaires poussés tôt (`a4b142d6`, `d320a5c6`). Garde des secrets à 0 à chaque commit,
    chaînée par `&&`.
  - **Fichiers neufs** (R12) :
    - `src/controle_ia/lean_essai/minuterie_v6.py` ;
    - `tests/test_lean_essai_minuterie_v6.py` ;
    - `scripts/lean_essai_d1a_v6/mutations_harnais_v6.py`, `piloter_poste_v6.sh`.
  - `hetzner_v5.py` est repris tel quel. Les modules v1 à v5 sont intacts. Empreintes : `empreintes-harnais-v6.txt`.
- **Essais** (`journal-essais-r5-v6.txt`) :
  - **77 essais v6**, qui passent sous Python 3.13 et sous Python 3.11 ;
  - 363 essais v1 à v5, qui passent toujours (hors gardes v2, dont les artefacts ne sont pas dans l'arbre réduit) ;
  - jeton `HCLOUD_TOKEN` retiré de l'environnement des essais.
- **Mutations** (`journal-mutations-harnais-v6.json`) : **120 sur des copies, 120 tuées**, aucune par délai, témoin à
  77 verts.
  - Même méthode que la v5 : import tracé, `-o pythonpath=`, jeton retiré, taille de fichier bornée.
  - Un premier passage en avait laissé trois survivantes (m10, p13, p17) : c'étaient des trous des essais, pas du code.
    Elles sont tuées au second passage, sur le commit livré.
- **Procédure du poste local** : `procedure-poste-local-d1a-v6.md`, scellée, non committée.
- **Ni serveur, ni dépense, ni appel de modèle, ni appel à Hetzner. Aucune valeur de clé.** Les vrais processus des essais
  (minuteries avec un faux client dans l'enfant, `sleep`) ont été arrêtés par leur PID ; contrôle final par `ps` : aucun ne
  reste.

## Verdict

**Corrigé hors machine** :
- CLC5-01, -03 et -06 ;
- CLC5-07, impératif ;
- les trois notes mineures demandées.
- CLC5-02, -04 et -05 sont écrits dans la procédure v6, avec l'appui du code : trois tâches et une ligne d'état dans le
  fichier de rattrapage, pilote borné, essai à blanc.

**Rien n'a tourné contre l'interface réelle de Hetzner, ni sur le poste de Lazar.**

## Corrections

| Point | Correction | Essais : cas sain / artefact | Mutations |
|---|---|---|---|
| **CLC5-01** survie | `attendre_minuterie` conclut « morte » seulement par `Popen.poll()` du processus lancé (sans course), ou si aucune lecture du PID ne l'a vue vivante jusqu'au délai ; **jamais sur une seule lecture négative**. « Armée » dès qu'elle vit et a écrit une ligne « garder ». `lancer_minuterie_detachee` rend l'objet `Popen` (`_processus`, jamais imprimé). `creer-et-armer` contrôle par `poll()` par défaut. Délai porté à 120 s (note 4). | Deux lectures négatives puis vivante : armée, 2 négatives comptées. Toujours négative : « jamais vue vivante » au délai. `poll()` vivant puis fini (code 2). **Course reproduite avec de vrais processus** : un lanceur garde 0,4 s une autre ligne de commande avant `execv`. La première lecture est négative ; ni les lectures ni `poll()` ne concluent « morte ». **Vrai chemin de `creer_et_armer`** avec cette minuterie retardée : le serveur reste. **25 lancements réels en série** : 8 lectures négatives observées, aucune conclusion « morte ». | r01 à r04, m09 |
| **CLC5-03** | `preparer` refuse s'il existe déjà un `rattrapage-machine-d1a-*` dans le dossier versé. `creer-et-armer` refuse s'il en existe un autre que le sien. Les deux valent même sans journal des créations. | Seconde préparation : refusée. Autre fichier de rattrapage, journal absent : refus, aucun appel. | t01 à t03 |
| **CLC5-06** | Les 16 mutations de la contre-lecture sont rejouées sur la v6 : toutes tuées. Essais neufs : **m10** (dans la boucle de `veiller`, deux 404 erronés alors que le serveur reste à l'inventaire : la garde continue et détruit à l'échéance) ; m09 (délai par défaut) ; **m11** (branche macOS avec de vrais `kill -0` et `ps -ww`, sans `/proc`) ; m01 (exactement 3 lectures refusées) ; m15 (403 et 401 en lecture lèvent `RefusDurable`). | voir colonne de gauche | m01 à m16 |
| **CLC5-07** (impératif) | **Aucune donnée du poste dans ce qui est versé ou poussé** : <ul><li>le fichier d'accès ne porte plus ni l'adresse du poste ni les règles ;</li><li>la clé part sans son commentaire ;</li><li>`acces-couper` ne rend que le nombre de règles ;</li><li>`verifier-coupure` masque les adresses (sortie et journal), sauf `192.0.2.1/32` ;</li><li>les sorties ne portent que des chemins relatifs au clone ;</li><li>les messages, et les traces d'une erreur inattendue (attrapée dans `main`), ont le chemin du clone et le dossier personnel masqués.</li></ul>**`garde-poste --ip-poste IP`** lit l'index git (ou des fichiers nommés) et rend le code 1 s'il porte l'adresse du poste (bornée en mot), le dossier personnel ou le chemin du clone. Il n'écrit jamais la valeur, seulement la nature. La procédure le chaîne avant chaque commit. | Fichier d'accès et sortie de `acces-couper` sans l'adresse ; clé envoyée sans commentaire ; journal et sortie de `verifier-coupure` masqués ; résultat de création sans chemin absolu ; trace d'une erreur inattendue masquée. **`garde-poste` sur un vrai dépôt git** : index propre (avec une adresse voisine `…50`) : code 0 ; index avec l'adresse, avec le dossier personnel, avec le chemin du clone : code 1, nature nommée, valeur jamais écrite. | g01 à g13 |
| **Note 1** | `acces-couper` relit le nom du pare-feu avant de poser les règles. | Pare-feu renommé : refus, règles inchangées. | c01, m08 |
| **Note 2** | `fichier_pousse` lit la tête de la branche amont **par `git ls-remote`** et exige que le commit du fichier en soit un ancêtre. Une référence de suivi écrite à la main ne suffit plus. En plus, **`--empreinte-mere`** : `creer-et-armer` compare l'empreinte sha256 du fichier de rattrapage à celle que la mère a lue, avant tout appel. | Vrai `git` : non suivi ; sans amont ; poussé (vrai) ; modifié ; référence écrite à la main (refus) ; branche retirée du distant (refus). Empreinte fausse : refus, aucun appel ; empreinte juste, en majuscules : création. | c02, c03, c06, e01, p11a, p11b |
| **Note 3** | La clé SSH et le pare-feu de la création sont pris dans le **fichier d'accès poussé**, lui aussi exigé poussé. `--cle-ssh` et `--pare-feu` sont retirés. | Corps de la création : identifiants du fichier ; fichier d'accès absent ou non poussé : refus. | e02, e03 |
| **Notes 5, 7** | Motifs : « détruire par l'identifiant ; jamais de relance de la minuterie ». Trois tâches de la mère : rappel dans sa session à `H`, sessions neuves à `H + 30 min` et `H + 24 h`. Messages autosuffisants, avec les formes `curl` (en-tête sur l'entrée standard, `--max-time 30`) et la conduite sur une erreur passagère. Ligne « en tâche jusqu'à » (CLC5-04) et heure du rappel de Lazar (`H + 1 h`) dans le fichier de rattrapage. | Heures et modes des trois tâches ; contenu de chaque message ; ligne d'état. | e09 à e14, m03 à m05, p19 |
| **Note 8** | `detruire` et `inventaire` en ligne de commande : pauses cumulées bornées (`--duree-max-s`, 480 s par défaut), au-delà **code 5** « refaire dans 15 minutes ». La minuterie garde ses retentatives sans fin. Le pilote borne chaque commande SSH par `timeout` côté serveur, et chaque connexion par `ConnectTimeout` et `ServerAlive*`. | Panne passagère durable : code 5 avant 60 s ; inventaire en 500 : code 5 ; deux pannes puis succès : code 0. Pilote : chaque appel SSH borné, options présentes, `bash -n`. | e05 à e08, c04, c05 |
| **Lecture seule** | `adresse-serveur --identifiant N` donne l'adresse du serveur loué, pour le pilote, après contrôle du nom (R10). | Adresse rendue ; identifiant absent ; autre nom : refus. | e04 |

## Procédure du poste local v6 (CLC5-02, CLC5-04, CLC5-05)

Le texte fait foi dans `procedure-poste-local-d1a-v6.md`.

- **CLC5-02** :
  - trois tâches de la mère, dont **deux qui ouvrent une session neuve** ;
  - relues après création ;
  - identifiants inscrits dans `registres/etat.md` et dans chaque passation jusqu'à la destruction confirmée ;
  - la session qui porte la première n'est pas archivée avant « aucun serveur de l'essai » ;
  - rappel personnel de Lazar à `H + 1 h`.
- **CLC5-04** : la ligne `ligne_etat_mere` du fichier de rattrapage est recopiée par la mère dans `registres/etat.md` à
  l'armement. Au-delà de son heure, ou si elle manque, la routine de reprise détruit le serveur.
- **CLC5-05** :
  - commandes du harnais hors du bac à sable de Claude Code, pré-autorisées ;
  - **essai à blanc** avant toute préparation : un `sleep` détaché survit à la commande puis à la session ; les mandataires
    (noms seulement) rendent `[]` ou un mandataire du système.
- **Aussi** :
  - `garde-poste` avant chaque commit ;
  - le mot « armée » porte l'empreinte du fichier de rattrapage ;
  - un seul clone, une seule préparation ;
  - capot ouvert ;
  - pilote en arrière-plan, ses sorties hors du clone, versées seulement après `garde-poste --fichier` ;
  - jamais de relance d'une minuterie.

## Réserves écrites

1. **Interface réelle non éprouvée**, comme en v5. Les premières lectures réelles sont M2 et M4 de la mère.
2. **Poste de Lazar non éprouvé** : bac à sable, mandataire, `ps` et veille sous macOS. Les essais tournent sous Linux, avec
   de vrais `kill -0` et `ps -ww`. L'essai à blanc de la procédure en décide.
3. **CLC5-01** : la course est reproduite de façon sûre par un lanceur retardé. La course naturelle, elle, a été vue ici
   8 fois en 25 lancements, sans conclusion « morte ». Sous macOS, `poll()` reste sans course ; la branche `ps` n'est jamais
   seule juge à la création.
4. **CLC5-07, limites** :
   - `garde-poste` ne connaît que l'adresse du poste, son dossier personnel et le chemin du clone : ni le nom de la machine,
     ni celui de l'utilisateur ;
   - il ne lit que l'index ou les fichiers qu'on lui donne ;
   - l'adresse du poste reste chez Hetzner, dans les règles du pare-feu, ce qui est nécessaire ; les réponses de M2 la
     portent, et la procédure dit de n'en afficher que les identifiants et les noms.
5. **Choix à confirmer** :
   - trois tâches de la mère (à `H`, `H + 30 min` et `H + 24 h`) plutôt que deux ;
   - borne de 480 s pour `detruire` et `inventaire` en ligne de commande ;
   - délai de survie de 120 s ;
   - l'erreur inattendue attrapée dans `main` rend le code 1, avec une trace masquée.
6. **Reste ouvert depuis la v4** : CLC3-05 et tout ce qui dépend de Lean ; le premier pas `noyau` en décide.
7. **Hors de ma branche** : `.claude/hooks/garde_calcul.py` ne connaît toujours pas Hetzner. Selon la contre-lecture,
   `scripts/depot_expurge.py` ne retire rien de ce dossier ; aucun fichier d'accès n'y existe à ce jour.
8. **Transparence** : pour rejouer exactement m01 à m16, j'ai lu `mutations_cl5.py` et `demo_course.py` dans le bac du
   contre-lecteur, comme des données. Je n'ai lancé aucun de ses scripts.

## Fichiers versés (non committés, scellés)

| Fichier | Empreinte |
|---|---|
| `rapport-corrections-harnais-d1a-v6.md` (ce fichier) | compagnon `.sha256` |
| `procedure-poste-local-d1a-v6.md` | compagnon `.sha256` |
| `journal-essais-r5-v6.txt` | `bec7e65fc79cae41325a16fd750459448870872f0c03c9de6dfbf8870745f3c7` |
| `journal-mutations-harnais-v6.json` | `4466215c3ccfb27c9874d360a4bcb2a1f63b1a0e3c558e61a246f3b98b9f261d` |
| `empreintes-harnais-v6.txt` | `ee4abacf511b570bd833dcccc03db108e1d1d0f4041da97e22dfc08614fa88ff` |

| Code v6 (commit `149babdc`) | Empreinte |
|---|---|
| `minuterie_v6.py` | `8ee400d7476051ab2f6b9ffa44220492320d03e4124e65f98172874b2654ee6b` |
| `test_lean_essai_minuterie_v6.py` | `77cc464db46bb97bebd69fb972987bee5e130cb9ae2857297ae92c14a41b7671` |
| `mutations_harnais_v6.py` | `c864091d7fadf405e7e9cc1161cea5fc73c54d055965c6cc1760362d6b7caec4` |
| `piloter_poste_v6.sh` | `e85619ab14269c2ad377a4bf100b64f078e8ea3e0653ecbb09d34ddbd8cccc04` |
| `hetzner_v5.py` (repris tel quel) | `154ffef39d21807663f4c602c7b8a22408ebb3d73bee410c708b003ea3227768` |
