# Essai Lean, outillage D-1a — vérification courte du différentiel v5 → v6 du harnais

- **Pour** : la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, puis Lazar.
- **Écrit par** : sous-agent neuf, vérificateur du tour 6 ; **modèle déclaré : Fable 5.2 (`claude-fable-5-2`)**, autre
  modèle que l'auteur du harnais (Opus 5.5). Je n'ai écrit ni le harnais, ni sa procédure, ni aucune de ses contre-lectures.
- **Date** : 11 novembre 2026, vers 11:40 UTC (`date -u`). Processeur seulement : aucune dépense, aucun serveur, aucun appel
  à Hetzner, aucune connexion SSH, aucun appel de modèle, aucun commit, aucune poussée.
- **Lu, empreintes vérifiées** :
  - `contre-lecture-courte-machine-harnais-d1a-v5.md` (`897b7438…`) ;
  - `rapport-corrections-harnais-d1a-v6.md` (`6f78484f…`) ;
  - `procedure-poste-local-d1a-v6.md` (`9e7f5172…`) ;
  - `journal-essais-r5-v6.txt` (`bec7e65f…`), `journal-mutations-harnais-v6.json` (`4466215c…`),
    `empreintes-harnais-v6.txt` ;
  - décisions R-2333 et R-2334 de `registres/decisions.md`.
- **Code** : commit `149babdc56f51925e9bc4e93a61041cc755bd2a3`, arbre clairsemé à moi. Les cinq empreintes égalent celles du
  rapport. Les quatre fichiers v6 sont neufs (R12) ; `hetzner_v5.py` est repris tel quel.
  - Lus en entier : `minuterie_v6.py`, `piloter_poste_v6.sh`.
  - Lus pour les fonctions reprises ou citées : `hetzner_v1` à `v5`, `minuterie_v4`, `couper_reseau_v1.sh`, la tête et la
    fin du lanceur de mutations, les essais des vrais processus et de m10.
- **Limite** : ni poste de Lazar, ni macOS, ni interface réelle de Hetzner, ni les outils de tâches de la mère.
  - « (éprouvé) » : exécuté sur le code du commit, depuis mon arbre, import tracé.
  - « (raisonné) » : lu dans le code, la procédure ou la description des outils, non exécuté.

## Verdict

**Consigne du poste local permise : le code v6 n'a aucun défaut bloquant, et ne demande pas de septième tour.**

Elle est permise **à condition que la consigne porte quatre exigences que la procédure v6 n'écrit pas** :

1. **VL6-01** : `git add` des fichiers nommés **avant** `garde-poste`, jamais `git commit -a`. Telle que la procédure la
   chaîne, la garde lit un index vide et rend « conforme » sans avoir rien lu (éprouvé).
2. **VL6-02** : l'identité git des commits du poste est fixée à la main. Sinon git peut la fabriquer avec le nom
   d'utilisateur et le nom de la machine, et aucune garde ne lit l'auteur d'un commit.
3. **VL6-03** : un essai à blanc d'une tâche en session neuve avant le mot « armée ». Rien ne prouve aujourd'hui qu'une
   session neuve a le jeton, le réseau et le droit d'envoyer une suppression sans attendre une permission.
4. **VL6-04** : la ligne « en tâche jusqu'à » est **poussée**, pas seulement committée.

Aucune donnée du poste n'est écrite par le code v6 dans un fichier versé, en marche normale (éprouvé et lu). Les chemins
restants passent par une fin anormale ou par git lui-même ; ils sont fermés par les exigences 1 et 2.

## CLC5-01 à CLC5-07

| Défaut | État | Preuve |
|---|---|---|
| **CLC5-01** course du contrôle de survie | **levé** | **Éprouvé, 82 lancements réels** de la minuterie (faux client dans l'enfant, sans jeton). Sur 70 lancements directs, une lecture du PID faite tout de suite après le lancement est négative **26 fois** : la course existe bien ici. Aucune conclusion « morte » : 35 par les lectures du PID seules (14 lectures négatives comptées en route), 35 par `poll()`. Puis 12 passages du vrai `creer_et_armer`, contrôle par défaut : le serveur reste 12 fois. Aucun processus ne reste. Mutations r01 à r04 et m09 tuées depuis mon arbre. |
| **CLC5-02** tâches de la mère | **tenu par la procédure**, réserve VL6-03 | Trois tâches : T1 dans la session à `H`, T2 et T3 en session neuve à `H + 30 min` et `H + 24 h`. Relues après création, identifiants dans `registres/etat.md` et les passations, session de T1 non archivée, rappel de Lazar à `H + 1 h`. Messages lus en entier dans le code : ils portent l'interface, la forme `curl` (en-tête sur l'entrée standard, `--max-time 30`), le contrôle du nom, les deux lectures, la conduite sur 401, 403 et erreur passagère, « ne jamais recréer ». Réserve : aucune de ces sessions neuves n'est éprouvée avant la création. |
| **CLC5-03** seconde machine | **levé** | Lu : `preparer` refuse tout `rattrapage-machine-d1a-*-v1.json` déjà présent ; `creer_et_armer` refuse tout autre que le sien, avant tout appel et sans journal des créations. Mutations t01 à t03 tuées depuis mon arbre. Reste vrai : un clone d'une autre branche ne porte pas le fichier ; d'où « un seul clone ». |
| **CLC5-04** routine de reprise | **tenu par la procédure**, réserve VL6-04 | `ligne_etat_mere` est dans le fichier de rattrapage ; M5 bis la recopie dans `registres/etat.md` avec les identifiants des tâches. La ligne dit quoi faire au-delà de l'heure, ou si elle manque. Réserve : M5 bis dit « committer », pas « pousser ». |
| **CLC5-05** bac à sable, mandataire | **tenu par la procédure**, réserve VL6-05 | Section 0, point 4 : commandes hors du bac à sable, pré-autorisées ; essai à blanc avant L1 (un `sleep` détaché survit à la commande, puis à la fin et à la reprise de la session) ; arrêt si un contrôle échoue. Réserve : le contrôle du mandataire ne peut pas décider tel qu'écrit. |
| **CLC5-06** mutations survivantes | **levé** | **Les 120 mutations de l'auteur rejouées depuis mon arbre : 120 tuées**, aucune par délai, témoin à 77 verts, chaque import tracé vers sa copie. **m10 rejouée en plus par un transport à moi** : sur le code du commit, un ou trois 404 erronés n'arrêtent pas la garde, qui détruit à l'échéance ; sur la copie mutée, la garde s'arrête, serveur allumé. Le serveur vraiment absent arrête toujours la garde. |
| **CLC5-07** données du poste | **levé dans le code** ; seconde ligne à réparer par la consigne (VL6-01, VL6-02) | Voir la section suivante. |

## CLC5-07 — où une donnée du poste pourrait encore passer

**Ce que le code écrit, en marche normale (lu, et éprouvé par les essais de l'auteur et les mutations g01 à g13).**

- Le fichier d'accès porte les identifiants, le nom, l'empreinte de la clé et les étiquettes. Ni adresse, ni règles : le
  client ne rend que l'identifiant et le nom du pare-feu.
- La clé part réduite à son type et à sa matière.
- `acces-couper` rend un nombre de règles. `verifier-coupure` masque les adresses, à la sortie comme au journal.
- Les sorties de `creer-et-armer` et de `--detache` portent des chemins relatifs. Les messages d'arrêt et la trace d'une
  erreur inattendue sont masqués.
- Les journaux de la minuterie et de la création ne portent ni chemin ni adresse. Le fichier PID porte le PID,
  l'identifiant et le jeton.
- Le pilote : `coupure-v6.txt` est la liste des règles `nftables` du serveur, sans adresse du poste. Les sondes et les
  épreuves ne relèvent ni la connexion SSH ni l'environnement.
- Les pièces versées par l'auteur (rapport, procédure, journaux) et le code neuf ne portent que des adresses de
  documentation et des chemins de l'atelier de l'auteur. Les trois commits ont pour auteur « Claude ».

**Chemins restants.**

| Chemin | Nature | Fermé par |
|---|---|---|
| Trace écrite avant `main` (interpréteur introuvable, module introuvable, erreur de syntaxe) dans la sortie d'un processus détaché : elle porte le chemin de l'interpréteur ou du clone, non masqué | raisonné | `garde-poste`, si le fichier est indexé avant (VL6-01) |
| Champ `erreur` des lignes « échec » des journaux (`str(e)` non masqué) | raisonné ; faible : le transport ne rend que le type de l'erreur | idem |
| Auteur et adresse des commits du poste | éprouvé pour la garde, raisonné pour macOS | VL6-02 |
| Chemin du clone écrit par un lien symbolique | éprouvé : non reconnu | relecture ; faible |
| Fichier binaire indexé | éprouvé : non lu (« Binary files differ ») | VL6-01 : `--fichier` |
| Nom d'utilisateur ou nom de machine seul | éprouvé : non reconnu ; réserve déjà écrite par l'auteur | discipline, relecture avant copie publique |
| Réponses de M2 chez la mère (les règles portent l'adresse) | raisonné | la procédure le dit ; la consigne doit donner le filtre exact |

## Défauts neufs

### VL6-01 — à exiger par la consigne — `garde-poste` rend « conforme » sans avoir rien lu

- **Où** : `_executer`, action `garde-poste`, l. 1072 à 1084 ; procédure, section 0 point 7, L3, L7, section 5.
- **Chemin (éprouvé, vrai dépôt git, dossier personnel factice)** :
  - la garde lit `git diff --cached` : ce qui est indexé et pas encore committé ;
  - index vide : code 0, `"conforme": true`, sans un mot sur le fait que rien n'a été lu ;
  - fichier modifié mais non indexé, qui porte l'adresse (cas de `git commit -a`) : code 0 ;
  - fichier neuf jamais indexé, qui porte le chemin du clone : code 0 ; le même par `--fichier` : code 1 ;
  - fichier binaire indexé avec l'adresse : code 0.
- **La procédure ne dit nulle part `git add` avant la garde.** À L3, elle dit « `garde-poste`, puis committer et pousser les
  deux fichiers » : les deux fichiers sont neufs, donc absents de l'index au moment de la garde. Suivie à la lettre, la garde
  ne lit rien, à L3, à L7 et à la section 5.
- **Poids** : c'est la seconde ligne. La première (le code n'écrit pas la donnée) tient. Une fuite exige donc une fin
  anormale, mais c'est exactement le cas que la garde devait couvrir. C'est aussi un repli silencieux (R5).
- **Correction (consigne)** : une seule forme, sans rien entre les trois commandes :
  `git add -- <fichiers nommés> && MV6 garde-poste --ip-poste IP_POSTE && git commit -m …`.
  - jamais `git commit -a`, jamais `git add` après la garde ;
  - en plus, `MV6 garde-poste --ip-poste IP_POSTE --fichier <pièce>` sur chaque sortie de processus détaché ;
  - avant la poussée, `git status --short` ne montre rien d'indexé ni de modifié dans `V`.
- **Correction (code, non bloquante)** : refuser un index vide et un fichier binaire ; lire aussi l'auteur.

### VL6-02 — à exiger par la consigne — identité git des commits du poste

- **Chemin** :
  - (éprouvé) un commit dont l'auteur est `utilisateur@machine.local` passe la garde : elle ne lit pas l'auteur ;
  - (raisonné) sans `user.name` ni `user.email` réglés, git peut les fabriquer à partir du nom d'utilisateur et du nom de
    la machine. Ils sont alors poussés avec chaque commit, et restent dans l'historique.
- **Correction (consigne)** : avant le premier commit, la session locale montre à Lazar `git config user.name` et
  `git config user.email`. Lazar choisit l'identité ; elle est posée pour ce clone seulement (`git config --local`). Aucun
  commit sans cette identité.

### VL6-03 — à exiger par la consigne — les tâches en session neuve ne sont jamais éprouvées avant « armée »

- **Chemin (raisonné, description des outils de la mère)** : M5 demande de relire les tâches (« actives, prochaine heure
  exacte »). Cela ne prouve pas qu'une session neuve :
  - a `HCLOUD_TOKEN` et atteint `api.hetzner.cloud` ;
  - peut lancer `curl -X DELETE` sans attendre une permission que personne ne donnera ;
  - a le dépôt, pour le point (5) du message.
- T2 et T3 sont le seul garde-fou qui ne dépend ni du poste ni de la session mère. S'il est mort-né, on retombe sur CLC5-02.
- **Correction (consigne)** : avant M6, une tâche d'essai en session neuve, à déclenchement immédiat, en lecture seule :
  elle lit les deux listes de serveurs (point 1 du message), n'écrit rien, ne supprime rien, et rend compte à la mère
  (nombre de serveurs, codes HTTP). Pas de mot « armée » sans ce compte rendu. T2 et T3 sont créées dans le même
  environnement, avec la notification activée.
- **À dire aussi dans le message de T2 et T3** : si le dépôt manque, sauter le point (5) et le dire ; sinon committer et
  pousser les registres.

### VL6-04 — mineur, à exiger par la consigne — la ligne « en tâche jusqu'à » n'est pas poussée

- **Chemin (raisonné)** : M5 bis dit « puis committer ». Une session neuve de la mère lit `registres/etat.md` dans son
  propre clone. Si la ligne n'est pas poussée sur `main`, elle manque, et la routine de reprise détruit le serveur au
  travail : le cas que CLC5-04 voulait éviter. C'est sûr pour la dépense.
- **Correction** : « committer et pousser sur `main` », avant M6.

### VL6-05 — mineur — le contrôle du mandataire ne peut pas décider

- **Chemin (éprouvé ici)** : `sorted(urllib.request.getproxies())` rend des noms de schéma (`https`, `no`…). Ils sont les
  mêmes pour un mandataire du système et pour un mandataire propre à la session. Le critère « jamais un mandataire propre à
  la session » ne se lit pas dans cette sortie.
- **Correction (consigne)** : `python3 -c "import urllib.request as u; print(sorted(u.getproxies_environment()))"` doit
  rendre `[]`. Un mandataire de session passe par les variables d'environnement. Sinon : arrêt, compte rendu.

### Notes (sans correction exigée)

1. **Borne de 480 s** : les pauses cumulées s'arrêtent à 315 s, mais sept requêtes au délai de 30 s s'y ajoutent, soit
   environ 525 s (raisonné). La consigne doit donner à `detruire` et `inventaire` un délai d'outil de 10 minutes, ou les
   lancer en arrière-plan. La procédure couvre déjà la coupure sans code.
2. **`--empreinte-mere`** (lu) : égalité stricte sur les 64 caractères, comparée avant tout appel ; une empreinte abrégée
   est refusée. La consigne doit dire à Lazar de transmettre l'empreinte entière.
3. **`adresse-serveur`** (lu) : une lecture, contrôle du nom, aucun journal ; l'adresse du serveur ne va que sur la sortie.
4. **Pilote** (lu) : chaque commande distante sous `timeout`, connexions bornées ; `scp` n'a que les bornes de connexion.
   `StrictHostKeyChecking=accept-new` écrit dans `~/.ssh/known_hosts` du poste, hors du dépôt.
5. **Code 5** (lu) : la borne lève hors des blocs qui rattrapent ; elle ne touche ni la minuterie ni `creer-et-armer`.

## Question 4 — le code neuf ouvre-t-il un trou ?

**Non, pour la dépense et la sûreté.**

- `--empreinte-mere`, le fichier d'accès poussé et `git ls-remote` ajoutent des refus avant tout appel ; aucun n'ouvre une
  voie de création.
- Le code 5 ne rend qu'une commande de premier plan plus courte ; les retentatives sans fin de la minuterie sont gardées.
- `adresse-serveur` est en lecture seule et ne lit que le serveur du nom exact.
- Le pilote borné ne change pas l'ordre des phases.
- Le seul point faible neuf est `garde-poste`, qui se dit garde et ne lit rien dans le cas courant (VL6-01).

## Ce que j'ai lancé

- **Essais depuis l'arbre**, jeton retiré de l'environnement, taille de fichier bornée, délai de 300 s :
  `PYTHONPATH=<arbre>/src:<bac>/essais …/.venv/bin/python -B -m pytest -q -o pythonpath= -p trace_import
  --basetemp=<bac>/pytest-tmp tests/test_lean_essai_*v6*.py` : **77 passed**. Import tracé vers
  `<arbre>/src/controle_ia/lean_essai/minuterie_v6.py`, `hetzner_v5.py`, `minuterie_v4.py` et `controle_ia/gardes.py`.
- **Mutations** : le lanceur de l'auteur, sur mon arbre, dans mon bac : 120 sur 120 tuées, témoin à 77 verts.
- **Scripts à moi** (`<bac>/essais/`, non versés) :
  - `demo_course_v6.py` : les 82 lancements réels ;
  - `demo_m10.py` : m10 par un transport à moi, sur le code du commit et sur une copie mutée ;
  - une suite de dix cas de `garde-poste` sur un vrai dépôt git, dans mon bac.
- **Vrais processus** : 82 minuteries sans jeton, chacune arrêtée par son PID (R10) ; contrôle final par `ps` : aucune.
- **Respect des interdits** : rien lu de `diag/`, `runs/`, du bras d'attaque, du mode tenu à l'écart, de T0.6, T0.7 ni de
  P3-bis ; aucune recherche récursive sur le dépôt ; aucune variable d'environnement listée, aucune valeur de clé ; aucun
  appel à Hetzner ; aucun commit, aucune poussée ; aucun `rm -rf`. Le lanceur de l'auteur retire lui-même ses copies, dans
  mon bac. Arbre retiré à la fin ; mes scripts et mes copies restent dans mon bac.
  `<bac>` = `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/verif-lean-v6`.
