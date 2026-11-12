# Essai Lean, outillage D-1a — rapport des corrections du harnais — v5

- **Pour** : la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`.
- **Écrit par** : l'auteur du harnais (sous-agent développeur, Opus 5.5, `claude-opus-5-5`).
- **Heures** (relevées par `date -u`) : contre-lecture vérifiée à 07:32 UTC ; rapport vers 08:15 UTC.
- **Lu, empreinte vérifiée** : `contre-lecture-courte-machine-harnais-d1a-v4.md` (`918662a7…`, égale à son compagnon), et la
  ligne R-2323 de `registres/decisions.md`.

## Livrable

- **Commit** `795fc074c200ea47e8aa9b9e88bae2222473adb5` (arbre `004e6768c1f04ab6c3d61f6f0aae457807fca4d4`), sur la branche
  `prep/lean-outillage-d1a-v5`, partie de `34ff42b7`.
  - Poussée seule, **sans fusion** ; quatre commits intermédiaires poussés tôt. Garde des secrets à 0 à chaque commit,
    chaînée par `&&`.
  - **Fichiers neufs** (R12) :
    - `src/controle_ia/lean_essai/minuterie_v5.py`, `hetzner_v5.py` ;
    - `tests/test_lean_essai_minuterie_v5.py` ;
    - `scripts/lean_essai_d1a_v5/mutations_harnais_v5.py`, `piloter_poste_v5.sh`.
  - Les modules v1 à v4 sont intacts. Empreintes : `empreintes-harnais-v5.txt`.
- **Essais** (`journal-essais-r5-v5.txt`) :
  - 57 essais v5, qui passent sous Python 3.13 et sous Python 3.11 ;
  - 306 essais v1 à v4, qui passent toujours (hors gardes v2, dont les artefacts ne sont pas dans l'arbre réduit) ;
  - jeton `HCLOUD_TOKEN` retiré de l'environnement des essais.
- **Mutations** (`journal-mutations-harnais-v5.json`) : 74 sur des copies, **74 tuées**, aucune par délai.
  - Méthode : import tracé, `-o pythonpath=` sur la copie, sans `PYTHONPATH` hérité.
  - Dans les enfants : jeton retiré, taille de fichier bornée.
  - Seuls les essais v5 sont lancés : chaque mutation est tuée par eux.
- **Procédure du poste local** : `procedure-poste-local-d1a-v5.md`, scellée, non committée.
- **Ni serveur, ni dépense, ni appel de modèle, ni appel à Hetzner** (pas même une lecture gratuite). **Aucune valeur de
  clé.**

## Verdict

**Corrigé hors machine** :
- **CLC4-01** est corrigé dans le code.
- **CLC4-02** est couvert par la procédure, avec le code qu'elle demande : préparation poussée avant toute création, heure
  limite, échéance bornée par la tâche de la mère, accès étiquetés pour la preuve du même projet, commande détachée.
- **CLC4-03, -05, -06 et -07** sont corrigés.
- **CLC4-08** : les onze survivantes de la contre-lecture sont tuées, n3, n10 et n18 en tête, ainsi que les trois déjà
  tuées.
- **Seconde machine** sous le même GO : refusée sans exception, et `--mot-de-lazar` est retiré.
- **CLC4-04** est couvert par `--detache`.

**Rien n'a tourné contre l'interface réelle de Hetzner.** La forme `location` et les statuts 401 et 403 restent des lectures
du journal public des changements et de la documentation. Les premières lectures réelles sont les pas M2 et M4 de la
procédure, faits par la mère.

## Corrections

| Défaut | Correction | Essais : cas sain / artefact | Mutations |
|---|---|---|---|
| **CLC4-01** emplacement | `hetzner_v5.lieu_du_serveur` : `location.name` (forme actuelle), sinon `datacenter.location.name` (ancienne forme), sinon `(None, "aucune")`, sans `KeyError` possible ; puis `--lieu` ; type et heure de création lus de même. | Quatre formes de réponse, plus des valeurs absurdes (`5`, `"x"`, `None`, liste, nom vide). La minuterie démarre et détruit à l'échéance sur chaque forme, et sans aucune forme : prix au pire cas, écrit au journal. | c01a, c01b, c01c |
| **CLC4-01** démarrage | **Tout le démarrage de `veiller` est sous retentatives**, borné par l'échéance : si elle passe sans lecture, la destruction par identifiant commence. Replis explicites. Prix retenu : le plus haut du prix passé et du prix lu. Devis revérifié ; s'il n'est pas tenu, destruction immédiate. Échéance comptée depuis la plus tôt de `--depuis` et de la création lue. Seuls le refus de nom (R10) et le refus durable arrêtent. Tout passe en arguments à la minuterie détachée : prix, lieu, échéance, taux, déjà-dépensé, GO, jeton, dépôt. | Deux lectures en échec puis démarrage ; échéance passée sans lecture ; devis non tenu (n16) ; plafond retranché (n20) ; prix passé plus bas ; refus de nom ; 401 dès la première lecture (code 3) ; arguments relus par l'analyseur de `veiller` (n9, n15). | c01d, c01e, c01j à c01m, n9a, n9b, n15a, n15b, n16, n20 |
| **CLC4-01** survie | `creer-et-armer` contrôle que la minuterie vit : PID vivant **et** première ligne « garder » en 60 secondes. Sinon, il détruit le serveur par son identifiant et s'arrête. | Minuterie morte ; minuterie muette ; lancement en échec (n3) ; contrôle par défaut sur un PID réel absent ; **un vrai processus détaché**, dans une session à lui, avec un faux client dans l'enfant : PID, `/proc`, première ligne « garder » réelle, arrêt par son PID ; un enfant qui meurt aussitôt est vu mort. | n3, c01f à c01i |
| **CLC4-03** dépôt | Racine du dépôt déduite de l'emplacement du module, ou donnée par `--depot`. Aucun chemin `/home/user` dans les sources (contrôlé par un essai). Dépôt sans registres : arrêt « donner --depot ». | `preparer --depot` sur un clone jetable ; source sans `/home/user`. | c03a, c03b |
| **CLC4-03** contrôle portable | `verifier-minuterie` : `/proc/PID/cmdline` sous Linux ; `kill -0 PID` puis `ps -ww -p PID -o command=` ailleurs (macOS). L'identifiant doit suivre `--identifiant`. Avec `--journal-minuterie`, la dernière ligne « garder » doit dater de moins de 5 minutes. | Branche Linux (vivante, autre processus, autre identifiant, absente) ; branche macOS (présent, autre, absent, autre utilisateur) ; `kill -0` et `ps` réels sur ce processus ; fraîcheur. | c03c à c03g |
| **CLC4-05** | `RefusDurable` (401, 403), distinct d'une erreur passagère. Trois refus durables au plus, en lecture comme en suppression, puis arrêt bruyant, **code 3**, et message « le détruire à la main par son identifiant N ». Sans journal, chaque échec est écrit sur la sortie d'erreur. | DELETE 403 durable : trois DELETE puis code 3 ; inventaire 401 : code 3 ; deux pannes passagères écrites puis destruction ; minuterie à l'échéance sur un 403 : code 3. | c05a à c05f |
| **CLC4-06** | Les serveurs du bon nom sont détruits d'abord ; ceux d'un autre nom ne sont jamais touchés, et l'arrêt les nomme. Le nom fixe est passé à la destruction : le contrôle du nom ne dépend pas du tri. | Bon nom par étiquette, autre nom étiqueté, bon nom sans étiquette : deux détruits, un nommé. Même chose par l'étiquette unique. | n1, n17, c06a, c06b |
| **CLC4-07** | `detruire`, la minuterie et `creer-et-armer` (sur un échec de la minuterie) soldent le journal des créations (`destruction_confirmee`), avec le GO et le jeton donnés ou lus sur les étiquettes du serveur. **Seconde machine refusée sans exception**, dans `preparer` et dans `creer-et-armer` ; `--mot-de-lazar` n'existe plus. | Coût du journal stable de 3 à 400 heures après `detruire --pas` ; ligne de solde de la minuterie ; seconde création refusée (journal, et registre « Hetzner NNNNNNNN ») ; `--mot-de-lazar` refusé par l'analyseur. | n18a, n18b, c07a à c07c |
| **CLC4-08**, autres | n5 : un statut 500 reste incertain. Note 1 : sur un refus 4xx, une recherche de contrôle par l'étiquette ; un serveur trouvé est détruit. n8 : intention exigée. n10 : un seul serveur du nom. n12 : inventaire de contrôle. n14 : pagination. n19 : jeton réutilisé. | 500 avec serveur créé : détruit ; 409 avec serveur créé : détruit ; 422 : « aucune création » soldée ; journal impossible à écrire : aucun appel ; serveur du nom déjà là : aucun appel ; apparition tardive : arrêt ; page suivante : arrêt ; jeton réutilisé : refus. | n5, n8, n10, n12, n14, n19 |
| **Inventaire** | `inventaire`, en lecture seule : serveurs de l'essai, par étiquettes et par nom, et adresses IP primaires attribuées à aucun serveur. | Deux serveurs et une adresse libre listés ; aucun DELETE ni POST. | i01, i02 |

## Procédure du poste local (CLC4-02, CLC4-04)

Le texte fait foi dans `procedure-poste-local-d1a-v5.md`. Le code qu'il demande :

- **`preparer`** :
  - écrit avant toute création le fichier de rattrapage : jeton, étiquettes, nom, heure de préparation, heure limite de
    création, `H` et `H + 24 h`, et les **deux messages autosuffisants des tâches de la mère**, avec leurs requêtes ;
  - refuse si l'heure limite est passée, si `H` est moins de 2 heures après la limite ou plus de 47 heures après maintenant,
    si le GO est invalide, ou si une machine existe déjà sous ce GO.
- **`creer-et-armer --rattrapage`** :
  - exige ce fichier **suivi par git, égal à `HEAD` et contenu dans une branche distante** (`fichier_pousse`, essayé avec un
    vrai `git` sur des dépôts jetables) ;
  - refuse après l'heure limite ;
  - fixe l'échéance de la minuterie à `min(création + 48 h, H − 1 h)`, et refuse s'il reste moins d'une heure.
- **`--detache --sortie F`** : la commande tourne dans une session à elle, sorties dans un fichier neuf. Elle rend aussitôt le
  PID et le fichier.
- **`acces-creer`, `acces-couper`, `acces-supprimer`** :
  - clé SSH et pare-feu étiquetés `creation=<jeton>`, que la mère relit par son propre jeton pour prouver le même projet ;
  - la mère prouve son droit d'écrire en créant puis supprimant un pare-feu vide, ce qui est gratuit ;
  - suppression seulement quand aucun serveur de l'essai ne reste, et après contrôle du nom.
- **La mère n'exécute aucun code de la branche** : ses tâches sont des requêtes de l'interface (annexe de la procédure). La
  fusion dans `main` n'est donc pas nécessaire à son garde-fou.
- **Pilote** : `piloter_poste_v5.sh` est le corps v4, avec l'en-tête du poste local ; seuls les noms des sorties changent.

## Réserves écrites

1. **Interface réelle non éprouvée.**
   - Points vus seulement sur un faux transport :
     - la forme `location` (affirmation du journal public des changements, relevée par la contre-lecture et non vérifiée ici) ;
     - le sens de 401 et 403 ;
     - les sélecteurs d'étiquettes ;
     - le champ `fingerprint` des clés SSH ;
     - le champ `assignee_id` des adresses IP primaires.
   - Le repli sans aucune forme d'emplacement garde la minuterie en vie, au prix du pire cas.
2. **La minuterie locale meurt avec l'ordinateur** (veille, extinction). La mère, armée avant la création à `H` et à
   `H + 24 h`, est le garde-fou de fond.
   - Au pire, avec les garde-fous locaux morts, la machine vit 71 heures, environ 30 USD pour `ccx33` : c'est une
     extrapolation du pire cas de la contre-lecture, non vérifiée ici.
   - Si les deux tâches de la mère échouent aussi, plus rien ne borne la dépense.
3. **Choix à confirmer** :
   - un devis non tenu au démarrage de la minuterie détruit tout de suite, au lieu de refuser de démarrer ;
   - `--depuis` est désormais exigé par `veiller`, et la plus tôt des deux heures compte, au lieu du refus de la v4 ;
   - la borne est de trois refus durables ;
   - la tâche de la mère tombe au plus 47 heures après la préparation, et l'heure limite de création au moins 2 heures avant
     elle.
4. **La poussée prouve que le fichier est sur une branche distante, pas que la mère l'a lu.** Le mot « armée » (M6) reste
   une étape humaine, que le code ne peut pas vérifier.
5. **Solde du journal** : une destruction faite par la mère à la main ne solde pas le journal local. La minuterie le solde à
   l'absence constatée, avec au plus une minute de retard : le coût est surestimé, jamais sous-estimé.
6. **Pas encore lancé sous macOS** : `ps -ww` et `kill -0` sont éprouvés en vrai sous Linux, et la branche macOS sur des
   faux. Python 3.11 ou plus récent est exigé : les essais ont tourné sous 3.11 et 3.13, pas sous le Python 3.9 du système
   macOS.
7. **Reste ouvert depuis la v4** : CLC3-05 (`readModuleData` sur un `.olean` hostile) et tout ce qui dépend de Lean ; le
   premier pas `noyau` sur la machine en décide.
8. **Hors de ma branche** : `.claude/hooks/garde_calcul.py` ne connaît toujours pas Hetzner. L'inventaire Hetzner de la
   routine de reprise est désormais dans `CLAUDE.md` (R-2322).
9. **Transparence** : pour rejouer exactement n1 à n20, j'ai lu dans le bac du contre-lecteur `mutations_cl4.py` et
   `demo_machine.py`, comme des données. Je n'ai lancé aucun de ses scripts, et surtout pas `lecture_gratuite.py`.

## Incident

- **Peu avant 07:55 UTC, un de mes essais v5 en cours d'écriture bouclait sans fin.** Le commit des modules, fait juste
  après le rétablissement, est daté de 07:55:55 UTC. Avec un dormeur muet et une horloge fixe, il
  écrivait un journal sans arrêt, et il a rempli le volume de `/tmp`.
  - J'ai arrêté la tâche par son identifiant, puis supprimé le seul dossier de sortie de cet essai, dans mon bac. Le fichier
    d'essais, tronqué à zéro par le disque plein, a été réécrit.
  - Ni le dépôt, ni les branches, ni les fichiers versés n'ont été touchés.
- **Parades** :
  - tout essai v5 dort par un dormeur borné, qui lève une exception hors de `Exception` au-delà de 2 000 pauses ;
  - le lanceur de mutations borne la taille des fichiers de ses enfants à 100 Mio.
- **Disque** : le volume n'a plus qu'environ 0,7 Go de libre, et pas de mon fait aujourd'hui.

## Fichiers versés (non committés, scellés)

| Fichier | Empreinte |
|---|---|
| `rapport-corrections-harnais-d1a-v5.md` (ce fichier) | compagnon `.sha256` |
| `procedure-poste-local-d1a-v5.md` | compagnon `.sha256` |
| `journal-essais-r5-v5.txt` | `23aa6e830262831de8d3399eeae9af39b1236e7cd43f4be49f34faff860efefb` |
| `journal-mutations-harnais-v5.json` | `eaf5a40e1bef3bd9dec2cca52ed49fdb82bd718c27018a72b3d57d611667c8db` |
| `empreintes-harnais-v5.txt` | `c8ac4cab55b579323ee050fe023f11090aaf8e9eae1f634c049bfb5b02438530` |

| Code v5 (commit `795fc074`) | Empreinte |
|---|---|
| `minuterie_v5.py` | `8f633665964e780388b2e645d4f30a803f5590d5128f58714bc2262a01bc487c` |
| `hetzner_v5.py` | `154ffef39d21807663f4c602c7b8a22408ebb3d73bee410c708b003ea3227768` |
| `test_lean_essai_minuterie_v5.py` | `f720c24c99896641f516dc3f345cdaaf20c5049d11307f9b111cb72d4299c9b7` |
| `mutations_harnais_v5.py` | `29efebdf7869ddc17d718d91c75f903b19a571d81b59004625c7c47b3662c659` |
| `piloter_poste_v5.sh` | `46a391d2b6a0cf57990520bd8c1b14a6bed561c710af478b57d49926911defee` |
