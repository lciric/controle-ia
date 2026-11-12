# Essai Lean, outillage D-1a — contre-lecture courte des seuls points « machine » du harnais v4

- **Pour** : la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, puis Lazar.
- **Écrit par** : sous-agent neuf, quatrième contre-lecteur ; **modèle déclaré : Claude Fable 5.2 (`claude-fable-5-2`)**. Je
  n'ai écrit ni le harnais, ni ses corrections, ni aucune des trois contre-lectures. Réserve de lignée : les deux premières
  contre-lectures étaient aussi de Fable 5.2 ; l'auteur du harnais et le troisième lecteur sont Opus 5.5.
- **Date** : 11 novembre 2026, vers 07:45 UTC. Processeur seulement : aucune dépense, aucun serveur, aucune connexion SSH,
  aucun appel de modèle, aucun commit, aucune poussée. Un seul appel réel à Hetzner : la lecture gratuite `GET /v1/servers`
  (deux lectures, 07:27 UTC), jeton lu par son nom, jamais affiché.
- **Lu, empreintes vérifiées** : `contre-lecture-courte-harnais-d1a-v3.md` (`b6ca886d…`),
  `rapport-corrections-harnais-d1a-v4.md` (`366df746…`), `journal-essais-r5-v4.txt` (`758af738…`),
  `journal-mutations-harnais-v4.json` (`026c6a00…`) ; décisions R-2307 et R-2308 (ces lignes) ; ligne de GO-2026-11-10-13
  dans `registres/go.md` et dans `registres/depenses.md`.
- **Code** : commit `34ff42b744ef567cfd536e5941316ce6db07ea1a`, arbre clairsemé à moi ; modules lus : `minuterie_v4.py`
  (`24167b6f…`), `hetzner_v4.py` (`ca80444b…`), `epreuve_isolement_v4.py` (`a20712f0…`, pas `noyau`), et ce qu'ils
  importent (`minuterie_v1` à `v3`, `hetzner_v1` à `v3`, `garde_go_v1`), `attendus-v4.json`, `piloter_poste_v4.sh`.
- **Limite** : aucune chaîne Lean, aucun serveur. « (éprouvé) » = exécuté en Python sur le code du commit, faux transport,
  import tracé vers mon arbre. « (raisonné) » = lu dans le code ou dans une pièce publique, non exécuté.

## Verdict

**Location non permise en l'état. Deux défauts bloquants : CLC4-01 et CLC4-02.**

- **CLC4-01 (code)** : la minuterie détachée meurt à son démarrage sur l'interface actuelle de Hetzner, et
  `creer-et-armer` rend quand même un PID et « armée ». Le garde-fou (b) de CLC3-07 n'existe donc pas en pratique.
- **CLC4-02 (procédure)** : le garde-fou de la mère, tel qu'il est écrit, ne tient pas dans le montage « session locale ».
  La commande citée ne tourne pas dans l'arbre `main` de la mère, la mère n'apprend la création que si la session locale
  survit, et rien ne prouve que les deux jetons voient le même projet Hetzner.

Avec ces deux défauts ensemble, **si la session locale meurt après la création, plus rien d'automatique ne détruit le
serveur**. Pour `ccx33` au prix le plus haut du relevé, les 65 USD sont atteints en 155 heures (6,4 jours).

**Ce qui est levé** : CLC3-04, CLC3-08, CLC3-09, CLC3-10, et les volets (a) et (d) de CLC3-07.

**Ce qui suffit pour permettre la location** :

1. une correction de code courte (CLC4-01 : lire `location`, démarrage sous retentatives, survie de la minuterie contrôlée
   par `creer-et-armer`), contre-lue ;
2. la consigne de la session locale et la procédure de la mère écrites comme à la fin de cette note (CLC4-02 à CLC4-05).

Sans la correction de code, la location n'est défendable que si la consigne dit en toutes lettres que la minuterie locale ne
compte pas, et que la mère est le seul garde-fou. Je ne le recommande pas : c'est revenir à un seul garde-fou, celui de
CLC3-07.

## Tableau des défauts

| Défaut | État | Preuve |
|---|---|---|
| **CLC3-04** premier pas `noyau` discriminant | **levé** (hors Lean) | Éprouvé : pour les 9 items du groupe, « compilation en échec » et « vérificateur muet », avec et sans G-L3+, donnent 2 à 11 écarts, jamais « conforme » (36 cas). G-L1 et G-L7 exigés, ligne de rejeu présente, constante fautive nommée, deux passages. L'item sain exige un rejeu réussi : un vérificateur qui échouerait toujours ne passe pas. Reste, comme prévu : rien n'est compilé avec Lean. |
| **CLC3-07 (a)** `detruire --pas d1a` | **levé** | Éprouvé : étiquettes fixes et nom, sans jeton ni journal ; un serveur d'un autre nom n'est pas touché. Deux réserves : CLC4-05 (boucle muette) et CLC4-06 (un serveur étiqueté d'un autre nom bloque tout). |
| **CLC3-07 (b)** minuterie détachée | **non levé** | CLC4-01 : elle meurt au démarrage (`KeyError: 'datacenter'`, éprouvé). `setsid`, PID versé et `verifier-minuterie` sont justes en eux-mêmes. |
| **CLC3-07 (c)** tâche programmée | **partiel** | La ligne de procédure est rendue, avec la bonne heure (échéance moins une heure, éprouvé). Mais elle est rendue après la création, à la session locale, et elle vise le `send_later` de la mère : CLC4-02. |
| **CLC3-07 (d)** fichier de rattrapage | **levé**, à adapter | Éprouvé : écrit avant l'intention et avant l'appel ; présent même quand rien n'est trouvé dans la fenêtre. Dans le montage local, il naît sur l'ordinateur de Lazar : c'est la session locale qui doit le pousser (CLC4-02). |
| **CLC3-08** création tardive | **levé** | Éprouvé : serveur apparu à la 3ᵉ recherche, détruit ; 21 recherches sur la fenêtre ; apparu après la fenêtre : arrêt explicite, journal non soldé, puis `detruire --pas d1a` le prend. Statuts 500 et 503 : traités comme incertains. Réserve : CLC4-04 (durée de la commande). |
| **CLC3-09** journal en échec | **levé** | Éprouvé : disque plein à la 2ᵉ écriture, `veiller` détruit quand même à l'échéance. Reste mineur : seule `OSError` est attrapée ; un journal fermé (`ValueError`) tue encore la boucle (éprouvé, peu plausible). |
| **CLC3-10** taux et type | **levé** | Éprouvé : taux déclaré 0,5 ou 1,0 ⇒ 1,25 retenu ; 1,3 ⇒ 1,3 ; 0 et −1 refusés ; `ccx63` refusé avant tout appel. Pire cas à 48 h : `ccx33` 20,19 USD, `ccx23` 12,58 USD, `cx53` 3,47 USD (prix les plus hauts du relevé `types-serveurs-hetzner-releve-v1.txt`, plus l'adresse, taux 1,25). |

## Défauts neufs

### CLC4-01 — bloquant — la minuterie détachée meurt à son démarrage

- **Où** : `minuterie_v4.py`, action `veiller` de la ligne de commande, l. 419 à 429 ; `creer_et_armer`, l. 356 à 363.
- **Chemin 1 (éprouvé sur faux transport ; fait de l'interface lu, non éprouvé sur un serveur réel)** :
  1. La ligne 426 lit `s["datacenter"]["location"]["name"]`.
  2. Le journal public des changements de Hetzner (`docs.hetzner.cloud/changelog`) porte deux entrées : 16 décembre 2025,
     propriété `datacenter` dépréciée pour « Servers » et « Primary IPs », remplacée par `location` ; 1ᵉʳ juillet 2026,
     « We removed the `datacenter` property in the request body and response of `Servers` and `Primary IPs` ».
  3. Avec une réponse sans `datacenter`, `veiller` lève `KeyError` avant sa boucle : aucun DELETE, serveur allumé.
  4. Les essais de l'auteur passent parce que leur faux transport rend encore `datacenter` (essai, l. 40).
- **Chemin 2 (éprouvé)** : même sans ce retrait, tout le démarrage est hors retentatives. Une seule lecture en échec
  (`ErreurHetzner`) à cet instant tue la minuterie. Trois lectures sont concernées : le serveur, les types, les prix.
- **Chemin 3 (éprouvé)** : `creer_et_armer` rend l'identifiant, l'échéance et un PID dès que le processus est lancé. Il ne
  contrôle pas qu'il vit encore. Avec un processus mort aussitôt, le rendu est le même, serveur allumé.
- **Limite de ma preuve** : le projet n'a aucun serveur (lecture gratuite : 0 serveur), donc je n'ai pas vu une réponse
  réelle. La lecture du journal des changements passe par un outil qui résume ; les deux entrées ont été relues une seconde
  fois, mot pour mot.
- **Correction** :
  - lire `s["location"]["name"]`, avec repli sur `datacenter` s'il existe ;
  - mieux : passer le prix horaire et le lieu à la minuterie par ses arguments, puisque `creer_et_armer` les connaît déjà,
    et mettre le démarrage sous les mêmes retentatives que la boucle ;
  - dans `creer_et_armer` : attendre la première ligne « garder » du journal de la minuterie et contrôler le PID ; sinon,
    détruire par identifiant et lever ;
  - un essai avec une réponse sans `datacenter`, et un essai « minuterie morte au démarrage ».

### CLC4-02 — bloquant tant que la consigne ne l'impose pas — le garde-fou de la mère ne tient pas dans le montage local

- **(i) Commande non exécutable (éprouvé)** : la ligne de procédure cite
  `PYTHONPATH=src python -m controle_ia.lean_essai.minuterie_v4 detruire --pas d1a`. Dans l'arbre de travail de la mère
  (`main`), le dossier `src/controle_ia/lean_essai/` n'existe pas : la branche v4 n'est pas fusionnée. À l'échéance, la
  commande échoue (« No module named »), et un arbre posé sous `/tmp` ne survit pas à un redémarrage du conteneur.
- **(ii) La mère n'apprend rien si la session locale meurt (raisonné)** : la ligne de procédure et le fichier de rattrapage
  sont produits sur l'ordinateur de Lazar, la première après la création. Si la session locale meurt entre l'appel de
  création et son compte rendu, la mère n'a ni l'heure, ni le jeton, ni même le fait qu'un serveur existe. « La mère
  committe le fichier » est impossible : il n'est pas chez elle.
- **(iii) Même projet, même droit (raisonné)** : un jeton Hetzner vaut pour un projet. Si le jeton de la session locale
  est d'un autre projet que celui de la mère, `detruire --pas d1a` rend « aucun serveur de l'essai » : un constat faux et
  rassurant. Si le jeton de la mère est en lecture seule, la destruction boucle (CLC4-05).
- **(iv) Une tâche programmée réveille un modèle (raisonné)** : le message de la tâche doit donc se suffire, commandes
  comprises, sans rien supposer de la mémoire de la session.
- **Ce qui tient déjà (éprouvé, lecture gratuite à 07:27 UTC)** : depuis le conteneur de la mère, l'interface de Hetzner
  répond (statut 200), `HCLOUD_TOKEN` est présent, le projet a 0 serveur, aucun aux étiquettes de l'essai, aucun du nom
  `lean-outillage-d1a`. `detruire --pas d1a` n'a besoin ni du jeton de création ni du journal : la mère peut donc s'armer
  **avant** la création.
- **Correction** : par la consigne et la procédure (section finale). Côté code, rien d'obligatoire ; fusionner la branche
  corrigée dans `main` avant la location règle (i).

### CLC4-03 — à corriger avant la location — chemin du dépôt figé dans le code

- **Où** : `minuterie_v3.DEPOT = Path("/home/user/controle-ia-travail")`, repris par `minuterie_v4` pour le registre des
  GO, le registre des dépenses, le journal des créations et le dossier versé.
- **Chemin (raisonné)** : sur l'ordinateur de Lazar, ce chemin n'existe pas. `creer-et-armer` s'arrête sur « registre des
  GO absent » : échec fermé, rien n'est créé. Sur macOS, `/home/user` ne peut pas être créé simplement.
- **Risque** : le contournement. La session locale appellerait `creer_et_armer` depuis un script à elle (les chemins sont
  des paramètres : toutes les gardes restent dans la fonction, mais ce n'est plus le chemin éprouvé), ou l'interface de
  Hetzner à la main, sans aucune garde.
- **Aussi** : `verifier-minuterie` lit `/proc`. Sur macOS, il répond toujours « processus absent » (sens prudent, mais il
  pousse à relancer une minuterie qui vit).
- **Correction** : racine du dépôt déduite du fichier (`Path(__file__).resolve().parents[3]`) ou donnée par un argument
  `--depot` ; `verifier-minuterie` par `os.kill(pid, 0)` et `ps -p PID -o command=` quand `/proc` manque. À défaut : la
  consigne fixe le seul contournement permis, et interdit tout appel direct de création.

### CLC4-04 — à exiger par la consigne — le rattrapage dure plus qu'une commande de premier plan

- **Chemin (raisonné sur l'outil, durées éprouvées)** : en création incertaine, `creer-et-armer` cherche l'étiquette 21 fois
  sur 600 secondes, plus les appels. Une commande de premier plan de Claude Code est arrêtée à 2 minutes par défaut, 10 au
  plus. La commande est donc tuée au milieu du rattrapage : serveur peut-être allumé, aucune minuterie (elle n'est lancée
  qu'après une création certaine).
- **Correction** : lancer `creer-et-armer` détaché, sorties dans un fichier, et lire ce fichier ; après toute fin anormale,
  `detruire --pas d1a` tout de suite, puis encore 15 minutes plus tard.

### CLC4-05 — à corriger — `detruire --pas d1a` peut boucler sans fin et sans un mot

- **Chemin (éprouvé)** : DELETE refusé durablement (403, jeton en lecture seule), sans `--journal` : après 12 essais et
  2 115 secondes de pauses, la commande boucle encore, sortie standard et sortie d'erreur vides. Dans une session, l'outil
  la tue sans que rien ne dise pourquoi.
- **Correction** : borne d'essais par défaut sur la ligne de commande de `detruire`, échec écrit sur la sortie d'erreur ;
  en attendant, la consigne exige `--journal`, une borne de temps, et le repli par l'identifiant.

### CLC4-06 — mineur — un serveur d'un autre nom bloque la destruction du bon

- **Chemin (éprouvé)** : un serveur du bon nom et un serveur étiqueté `essai=lean,pas=d1a` d'un autre nom ⇒ `GardeArret`,
  « aucun n'est touché » : le bon serveur reste allumé. Un serveur **renommé** échappe à la minuterie, à
  `detruire --pas` et à `detruire --identifiant` (les trois refusent : c'est R10, voulu).
- **Plausibilité** : faible, il faut une main qui renomme ou qui étiquette. Le nom est unique dans un projet Hetzner
  (raisonné, non éprouvé), donc ce code ne peut pas créer deux serveurs du même nom.
- **Correction** : détruire d'abord ceux du bon nom, puis lever pour les autres. Consigne : ne jamais renommer.

### CLC4-07 — mineur — journal des créations jamais soldé ; « mot de Lazar » satisfait par le GO lui-même

- **Chemin 1 (éprouvé)** : après une création réussie puis une destruction normale (minuterie détachée ou `detruire`),
  aucune ligne `destruction_confirmee` n'est écrite au journal des créations. `cout_journal` compte donc jusqu'à
  « maintenant » : 13,62 USD à 48 h, 56,75 à 200 h, 113,50 à 400 h, pour un serveur détruit. Échec fermé (une seconde
  création finit refusée à tort), mais le déjà-dépensé du journal est faux.
- **Chemin 2 (éprouvé)** : `--mot-de-lazar GO-2026-11-10-13`, c'est-à-dire le GO déjà cité, est admis comme mot de Lazar.
  Après destruction du premier serveur, une seconde création passe. Deux serveurs ne coexistent pas (contrôle du nom,
  éprouvé), et le déjà-dépensé du journal borne la somme ; mais le mot n'a plus de sens.
- **Correction** : `detruire` et la minuterie soldent le journal ; le mot de Lazar doit différer du GO de la création.
  Consigne : une seule création, jamais de seconde sans retour à Lazar.

### CLC4-08 — à corriger — 11 mutations neuves survivent sur 14

Copie par mutation, import tracé vers la copie, sans `PYTHONPATH` hérité, les 106 essais v4 rejoués. Le code lu est juste
sur ces points ; ce sont des gardes sans essai (R5).

| Mutation | Ce qui survit | Poids |
|---|---|---|
| n3 | minuterie non lancée : le serveur n'est plus détruit | **fort** (serveur allumé sans minuterie) |
| n10 | contrôle « un serveur du même nom existe déjà » retiré du client v4 | **fort** (un seul serveur par pas) |
| n18 | seconde machine admise sans mot de Lazar dans `creer_et_armer` | plafond |
| n9, n20 | déjà-dépensé non transmis à la minuterie détachée, ou non retranché de son plafond | plafond |
| n15 | taux transmis à la minuterie détachée remplacé par 1,0 | plafond (relevé à 1,25 par le code) |
| n16 | devis non revérifié au démarrage de `veiller` | plafond |
| n8 | intention non exigée avant l'appel de création | rattrapage |
| n5 | statut 500 traité comme un refus (« aucune création ») | rattrapage |
| n12 | inventaire de contrôle après `detruire --pas` retiré | faible |
| n14 | garde de pagination de la recherche par étiquettes fixes retirée | faible |

Tuées : n1 (contrôle du nom avant destruction), n17 (recherche par nom), n19 (jeton réutilisé).

### Notes

1. **Refus 4xx** : un 4xx à la création écrit « aucune création » sans une seule recherche par étiquette (éprouvé). C'est
   juste pour l'interface de Hetzner (raisonné). Une recherche de contrôle ne coûterait rien.
2. **Adresse IPv4 primaire** : créée avec le serveur, elle est en principe supprimée avec lui (raisonné, non éprouvé).
   `detruire` ne le contrôle pas ; à vérifier à la main après la destruction (quelques centimes par mois sinon).
3. **Ordinateur en veille** : une minuterie détachée sur un ordinateur portable est suspendue par la veille et tuée par
   l'extinction. Même corrigée, elle ne remplace pas la tâche de la mère.
4. **Ligne des dépenses** : la ligne de GO-2026-11-10-13 a 3 cellules. `creer-et-armer` exigera `--deja-depense-usd 0`
   (voulu ; R-2297 : 0,00 USD à ce jour).

## Question 3 — voies restantes

**Un serveur reste allumé.**

| Cas | Ce qui se passe aujourd'hui | Ce qui le rattrape |
|---|---|---|
| La session locale meurt avant l'appel de création | rien n'est créé ; fichier de rattrapage et intention sur le disque | rien à faire |
| Elle meurt pendant l'appel ou juste après (avant la minuterie) | serveur allumé, aucune minuterie | la mère seule, et seulement si elle s'est armée avant (CLC4-02) |
| Elle meurt après le lancement de la minuterie | minuterie morte dès le démarrage (CLC4-01) | la mère seule |
| Création incertaine, commande tuée par l'outil (CLC4-04) | serveur peut-être allumé, aucune minuterie | `detruire --pas d1a`, la mère |
| Ordinateur en veille ou éteint | minuterie suspendue ou tuée | la mère |
| La mère ne voit pas le bon projet, ou ne peut pas écrire | « aucun serveur » ou boucle muette | rien : à prouver avant (CLC4-02 iii) |
| Serveur renommé | tous les garde-fous refusent | une main humaine |

**La mère détruit à distance pendant que la locale travaille (éprouvé pour la minuterie, raisonné pour le reste).**

- La minuterie locale constate l'absence par deux lectures et s'arrête proprement.
- `piloter_poste_v4.sh` échoue sur SSH et s'arrête (`set -e`) : aucune dépense, des sorties partielles.
- Le risque est la suite : la session locale croit à une panne et recrée. Sans mot de Lazar, c'est refusé ; avec le GO
  lui-même pour mot, c'est admis (CLC4-07). La consigne doit l'interdire.
- Course étroite : si la mère lance `detruire --pas d1a` pendant que l'appel de création est en vol, elle ne trouve rien et
  rend « aucun serveur de l'essai ». D'où la seconde tâche de la mère, plus tard.

**Deux serveurs coexistent.**

- Par ce code, non : nom fixe, contrôle de l'inventaire avant l'appel (éprouvé), unicité du nom dans le projet (raisonné).
- Reste le cas de deux projets (deux jetons), que la preuve du même projet ferme.

**La dépense dépasse 65 USD.**

- Garde-fous vivants : non. Pire cas 20,19 USD à 48 h ; la minuterie détruit dès que le cumul atteint le plafond moins une
  heure ; créations incertaines, une heure entamée chacune.
- Tous garde-fous morts : `ccx33` 155 h (6,4 jours) ; `ccx23` 248 h (10,3 jours) ; `cx53` 900 h (37,5 jours), aux prix les
  plus hauts du relevé et au taux de 1,25. C'est le cas des lignes 2 à 6 du premier tableau, d'où le verdict.

## Ce que la consigne de la session locale et la procédure de la mère doivent exiger

**Avant toute création (mère).**

1. La branche corrigée est contre-lue et fusionnée dans `main`, ou bien le message de la tâche programmée contient les
   commandes qui recréent un arbre au commit voulu. La commande de destruction est essayée à blanc par la mère : elle doit
   rendre « aucun serveur de l'essai ».
2. **Même projet, droit d'écrire** : la session locale crée la clé SSH et le pare-feu (gratuits) et en donne les
   identifiants ; la mère les relit par son propre jeton. Les identifiants doivent se retrouver. Le droit d'écrire de la
   mère se prouve par une création puis une suppression d'un objet gratuit.
3. **La mère s'arme avant la création**, pas après : une tâche programmée à une **heure absolue H** (fin prévue du travail
   plus une marge, 47 heures au plus après le feu vert), et une seconde 24 heures plus tard. Message complet : commande
   `detruire --pas d1a --journal …` sous une borne de temps, inventaire de contrôle, repli « lire l'identifiant par les
   étiquettes, puis détruire par cet identifiant », inscription dans `registres/arrets.md`, mot à Lazar.
4. La consigne donne à la session locale une **heure limite de création** (bien avant H) : passé cette heure, elle ne crée
   plus et rend la main.
5. Proposition à Lazar, déjà faite en R-2307 : l'inventaire Hetzner dans la routine de reprise.

**À la création (session locale).**

6. Une seule voie : `minuterie_v4` (ou sa version corrigée) `creer-et-armer`, au commit dit par la consigne, depuis un
   clone à jour (registres compris). **Jamais** d'appel direct de création, jamais de console, jamais de second essai sans
   retour à Lazar, jamais `--mot-de-lazar`. Type dans la liste ; `--deja-depense-usd 0`.
7. La commande est lancée **détachée**, sorties dans un fichier (CLC4-04). L'ordinateur reste branché, veille coupée,
   jusqu'à la destruction.
8. Dès le retour : pousser le fichier de rattrapage sur une branche du dépôt de travail et donner à Lazar, pour la mère,
   l'identifiant, l'échéance et le PID.
9. Dans la minute : `verifier-minuterie`, **et** lire dans le journal de la minuterie une première ligne « garder ». Si
   l'un des deux manque : `detruire --identifiant N` tout de suite, et arrêt.
10. Après toute fin anormale de `creer-et-armer` : `detruire --pas d1a --journal …`, inventaire, puis la même chose
    15 minutes plus tard.

**Pendant et après (session locale).**

11. Ne jamais renommer le serveur ni toucher à ses étiquettes.
12. Si la machine ne répond plus : lire l'inventaire. Si elle est absente, la mère l'a détruite : **ne pas recréer**,
    rendre compte.
13. À la fin : `detruire --identifiant N --journal …` (ou `--pas d1a`), inventaire de contrôle, contrôle qu'aucune adresse
    IPv4 primaire ne reste, arrêt de la minuterie par son PID (R10) si elle vit, pièces poussées. Lazar prévient la mère, qui
    vérifie par sa propre lecture avant de désarmer ses tâches.

## Ce que j'ai lancé

- **Essais** : `PYTHONPATH=<arbre>/src …/.venv/bin/python -m pytest -q -o pythonpath= --basetemp=<bac>/pytest-tmp
  tests/test_lean_essai_*v4*.py` depuis l'arbre ⇒ `106 passed`. Import tracé :
  `…/scratchpad/cl4-lean-d1a/arbre/src/controle_ia/lean_essai/minuterie_v4.py` et `hetzner_v4.py`.
- **Scripts dans mon bac à sable** (`…/scratchpad/cl4-lean-d1a/essais/`, non versés), lancés avec `python -I -B` :
  - `demo_machine.py` : CLC4-01 (trois chemins), CLC4-05, CLC4-06, CLC4-07 chemin 1, statuts de création, rejeu de
    CLC3-04, -08, -09, -10 ;
  - `demo_mot.py` : CLC4-07 chemin 2, contrôle du nom ;
  - `mutations_cl4.py` : CLC4-08 ;
  - `lecture_gratuite.py` : `GET /v1/servers` (nombre, noms comparés, étiquettes ; aucune valeur de clé).
- **Lecture publique** : `docs.hetzner.cloud/changelog`, deux fois (entrées du 16 décembre 2025 et du 1ᵉʳ juillet 2026).
- **Respect des interdits** : rien lu de `diag/`, `runs/`, du bras d'attaque, du mode tenu à l'écart, de T0.6, T0.7 ni de
  P3-bis. Aucune recherche récursive sur la racine du dépôt. Aucune variable d'environnement listée, aucune valeur de clé.
  Aucun `rm -rf`. Arbre retiré à la fin ; les copies des mutations restent dans mon bac à sable.
