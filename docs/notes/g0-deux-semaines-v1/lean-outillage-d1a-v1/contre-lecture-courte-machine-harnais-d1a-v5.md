# Essai Lean, outillage D-1a — contre-lecture courte des seuls points « machine » du harnais v5

- **Pour** : la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, puis Lazar.
- **Écrit par** : sous-agent neuf, cinquième contre-lecteur des points machine ; **modèle déclaré : Claude Opus 5.5
  (`claude-opus-5-5`)**. Je n'ai écrit ni le harnais, ni sa procédure, ni aucune de ses contre-lectures. **Réserve de
  lignée** : même modèle que l'auteur du harnais ; les lecteurs v1, v2 et v4 étaient Fable 5.2, le v3 Opus 5.5.
- **Date** : 11 novembre 2026, vers 10:55 UTC. Processeur seulement : aucune dépense, aucun serveur, **aucun appel à
  Hetzner** (pas même une lecture gratuite), aucune connexion SSH, aucun appel de modèle, aucun commit, aucune poussée.
- **Lu, empreintes vérifiées** (`sha256sum -c`, dans le dossier de chaque compagnon) :
  - `contre-lecture-courte-machine-harnais-d1a-v4.md` (`918662a7…`) ;
  - `rapport-corrections-harnais-d1a-v5.md` (`2b538924…`) ;
  - `procedure-poste-local-d1a-v5.md` (`8e876a7a…`) ;
  - `journal-essais-r5-v5.txt`, `journal-mutations-harnais-v5.json`, `empreintes-harnais-v5.txt`,
    `types-serveurs-hetzner-releve-v1.txt` ;
  - décisions R-2323 et R-2331 de `registres/decisions.md` ; ligne de GO-2026-11-10-13 (`registres/go.md`, identique sur
    `main` et au commit v5).
- **Code** : différence `34ff42b7…..795fc074…` (5 fichiers neufs, v1 à v4 intacts). Arbre clairsemé à moi au commit
  `795fc074c200ea47e8aa9b9e88bae2222473adb5`. Les 5 empreintes égalent celles du rapport.
  - Lus en entier : `minuterie_v5.py`, `hetzner_v5.py`, `hetzner_v1` à `v4`, `minuterie_v1`, `piloter_poste_v5.sh`.
  - Lus pour les fonctions reprises : `minuterie_v2` à `v4`, `garde_go_v1`.
  - Aussi lus : la tête du fichier d'essais v5 et le lanceur de mutations v5 ; sur `main`, `.claude/hooks/garde_calcul.py`
    (motifs) et la tête de `scripts/depot_expurge.py`.
- **Limite** : ni poste de Lazar, ni macOS, ni interface réelle de Hetzner.
  - « (éprouvé) » : exécuté sur le code du commit, depuis mon arbre, import tracé, faux transport **écrit par moi**
    (forme actuelle : `location` seule, sans `datacenter`), ou vrais processus sans jeton.
  - « (raisonné) » : lu dans le code, dans la procédure ou dans la description des outils, non exécuté.

## Verdict

**Location permise : sans défaut bloquant pour la dépense ni pour la sûreté.** Avec les gardes vivants, la dépense est
bornée à 20,19 USD à 48 h pour `ccx33` au prix le plus haut du relevé. Une voie au-delà de 65 USD exige que trois choses
tombent ensemble : les deux tâches de la mère, la minuterie locale, et tout regard humain pendant 6,4 jours.

Deux conditions :

1. **Correction courte recommandée avant la location : CLC5-01.**
   - C'est une course dans le contrôle de survie de la minuterie (éprouvée, environ 4 % des lancements réels). Elle fait
     détruire à tort le serveur tout juste créé.
   - Ce n'est pas un défaut bloquant : la destruction va dans le sens prudent et coûte une heure entamée (0,42 USD).
   - Mais elle consomme la seule création permise sous ce GO. La refaire exige alors une consigne neuve, et le code la
     refuse dans le même clone.
2. **La consigne du poste local et la procédure de la mère doivent exiger les points de la dernière section.** Trois sont
   neufs :
   - CLC5-02 : une des deux tâches de la mère ne doit pas dépendre de la seule session mère ;
   - CLC5-04 : la routine de reprise de la mère ne doit pas détruire le serveur en tâche ;
   - CLC5-05 : les commandes du harnais tournent hors du bac à sable de Claude Code.

## CLC4-01 à CLC4-08

| Défaut | État | Preuve |
|---|---|---|
| **CLC4-01** minuterie morte au démarrage | **levé** (réserve CLC5-01) | **Éprouvé.** La minuterie démarre et détruit à l'échéance sur quatre formes de réponse : `location` seule (forme actuelle), `datacenter.location` seule, aucune forme avec `--lieu`, aucune forme sans rien (prix au pire cas 1,354 USD/h). Avec un prix passé plus bas que le prix lu, le plus haut (0,4206 USD/h) est retenu. Quatre pannes au démarrage, puis reprise. Pannes jusqu'après l'échéance : destruction par identifiant. 401 dès la première lecture : code 3 et message bruyant. **Vrai processus de minuterie**, sans jeton donc sans réseau, vivant mais muet : `creer_et_armer` détruit le serveur après 60,1 s réelles. Réserve : CLC5-01. |
| **CLC4-02** garde-fou de la mère | **levé** (réserves CLC5-02, CLC5-04) | (i) La mère n'exécute plus de code de la branche : ses tâches sont des requêtes de l'interface. (ii) Elle s'arme **avant** la création, d'après le fichier de rattrapage poussé : `creer-et-armer` refuse si ce fichier n'est pas suivi, égal à `HEAD` et contenu dans une branche distante (essais de l'auteur, vrai `git`). (iii) M2 et M3 prouvent le même projet et le droit d'écrire. (iv) Les deux messages se suffisent (lus en entier) ; mes mutations m03 à m05 (clause 401/403, sélecteur, « ne jamais recréer ») sont tuées. |
| **CLC4-03** chemin figé | **levé** sous Linux ; macOS raisonné seulement | Racine déduite du module ou donnée par `--depot` ; plus aucun `/home/user` dans le chemin utilisé. La branche macOS de `verifier-minuterie` n'est éprouvée que sur des faux. Ma mutation m11 (sortie de `ps` par défaut ignorée) survit : le câblage réel sous macOS n'est jamais exécuté. |
| **CLC4-04** rattrapage plus long qu'une commande | **levé** (réserve CLC5-05) | `--detache` lance la commande dans une session à elle et rend tout de suite (éprouvé : session neuve, `--detache` retiré chez l'enfant, sortie sans valeur d'environnement). Ici, un processus détaché par `setsid` survit à la fin de la commande et passe sous le PID 1 (éprouvé avec un `sleep` détaché). Les vraies minuteries tournent elles aussi dans une session à elles. |
| **CLC4-05** boucle muette sur 403 | **levé** | **Éprouvé**, pour `detruire --identifiant` et pour `--pas`, sans journal : DELETE refusé durablement ⇒ 3 DELETE, 15 s de pauses, code 3, 4 lignes sur la sortie d'erreur, message « le détruire à la main ». `veiller` à l'échéance sur un 403 : `DestructionRefusee` après 3 DELETE. |
| **CLC4-06** un autre nom bloque le bon | **levé** | **Éprouvé** : le bon serveur et deux serveurs étiquetés d'un autre nom ⇒ seul le bon est détruit ; les deux autres sont nommés dans l'arrêt et laissés intacts (R10). |
| **CLC4-07** journal non soldé ; mot de Lazar | **partiel** | **Éprouvé.** Après `detruire --identifiant`, le coût du journal reste à 1,68 USD à 3 h, 48 h et 400 h. `--mot-de-lazar` n'existe plus. Seconde machine refusée **dans le même clone**. **Admise dans un clone sans journal des créations**, alors même que le premier fichier de rattrapage poussé est présent : CLC5-03. |
| **CLC4-08** mutations survivantes | **levé** pour les 11 nommées | Les 74 mutations de l'auteur, **rejouées depuis mon arbre** : 74 tuées, témoin à 57 verts, chaque import tracé vers sa copie. Mes 16 mutations neuves : 11 tuées, 5 survivantes (CLC5-06). |

## Défauts neufs

### CLC5-01 — à corriger avant la location (non bloquant : sens prudent) — course dans le contrôle de survie

- **Où** :
  - `attendre_minuterie`, l. 500 à 513 : il rend « morte » au **premier** contrôle négatif, sans réessayer ;
  - `verifier_minuterie`, l. 472 à 478 : la lecture de `/proc/PID/cmdline` ;
  - `creer_et_armer`, l. 785 à 794 : le contrôle tombe juste après le lancement.
- **Chemin (éprouvé, vrais processus)** :
  1. Juste après le lancement, `/proc/PID/cmdline` de la minuterie peut se lire **vide**. J'ai observé 0 octet, état R,
     puis la bonne ligne de commande 1 à 3 ms plus tard.
  2. Explication probable : `Popen` rend la main dès que l'enfant a fermé ses descripteurs à l'`exec`, avant que le noyau
     ait posé les arguments du nouveau programme.
  3. Une ligne vide donne « le PID désigne un autre processus ». `creer_et_armer` détruit alors le serveur par son
     identifiant et rend « minuterie non armée ».
- **Fréquence** : 6 faux négatifs sur 138 lancements contrôlés (≈ 4 %). Le détail :
  - 2 sur 40 et 2 sur 60, au premier lancement d'un interpréteur neuf ;
  - 1 sur 20 en série ;
  - 1 sur le vrai chemin de `creer_et_armer`, avec `lancer_minuterie_detachee` et le contrôle par défaut, sur deux passages
    complets.
- **Effet** :
  - Le serveur est détruit à tort ; c'est sûr pour la dépense (une heure entamée).
  - La vraie minuterie démarre ensuite, constate l'absence et s'arrête.
  - Mais la seule création permise est consommée : la procédure interdit un second essai, et le code refuse une seconde
    machine dans le même clone.
  - Sous macOS, le contrôle passe par `ps` (raisonné : une fenêtre semblable est possible).
- **Correction** :
  - ne pas conclure sur un seul contrôle négatif : réessayer jusqu'au délai, et conclure « morte » seulement si jamais
    « vivante et ligne garder » dans le délai ;
  - mieux : garder l'objet `Popen` et lire `poll()`, qui dit sans course si l'enfant est fini ;
  - essai : un `verifier` qui répond « autre processus » une fois, puis « vivante ».

### CLC5-02 — à exiger par la consigne — les deux tâches de la mère dépendent de la seule session mère

- **Chemin (raisonné, description des outils de la mère)** :
  - La procédure arme deux `send_later`. Ils sont livrés **dans cette session-là** ; si un tour y est en cours, le message
    attend la fin du tour.
  - Le programme change de session par passations. Si la session qui porte les tâches est archivée, remplacée, ou occupée
    par un long tour, les deux tâches peuvent tomber ou glisser ensemble.
  - La borne « 71 h » de la procédure suppose une livraison à l'heure.
- **Correction (consigne)** :
  - au moins la seconde tâche est une tâche programmée qui **ouvre une session neuve à chaque déclenchement**, avec le
    message tel quel plus les formes `curl` de l'annexe ;
  - les deux tâches sont relues après création (actives, prochaine heure exacte) ;
  - leurs identifiants sont inscrits dans `registres/etat.md` et dans chaque passation jusqu'à la destruction confirmée ;
  - la session qui porte une tâche n'est pas archivée avant « aucun serveur de l'essai » ;
  - Lazar pose son propre rappel à `H + 1 h` : console de Hetzner, zéro serveur.

### CLC5-03 — mineur — seconde machine admise dans un clone sans journal des créations

- **Chemin (éprouvé)** : une création, puis une destruction, puis le journal des créations retiré. C'est l'état d'un clone
  neuf de la branche du poste si la session locale est morte avant L7. Alors `preparer` **et** `creer_et_armer` admettent
  une seconde machine, alors que `V/` porte le premier fichier de rattrapage, poussé à L3.
- **Borne** : les deux machines ne coexistent pas (même nom). Les tâches de la mère, qui visent les étiquettes fixes et le
  nom, couvrent aussi la seconde. Mais la seconde peut naître sans que la mère se soit réarmée, et le code ne peut pas
  vérifier « armée ».
- **Correction** : refuser dans `preparer` et dans `creer-et-armer` si `V/` porte un autre
  `rattrapage-machine-d1a-*-v1.json` sous ce GO. Ce fichier est poussé avant toute création, donc présent dans tout clone de
  la branche. Consigne : un seul clone, une seule préparation.

### CLC5-04 — à exiger par la consigne — la routine de reprise de la mère peut détruire le serveur en plein travail

- **Chemin (raisonné)** : `CLAUDE.md`, étape 4 de la routine de reprise (R-2322), dit que « tout serveur sans tâche en
  cours s'arrête par son identifiant ». Toute session neuve de la mère verra `lean-outillage-d1a` pendant le travail, et
  rien ne lui dit qu'il est en tâche.
- **Effet** : une destruction en plein travail. C'est sûr pour la dépense, et c'est d'ailleurs un troisième garde-fou utile.
- **Correction** : à l'armement, une ligne dans `registres/etat.md` : « serveur `lean-outillage-d1a` (étiquette
  `creation=<jeton>`) en tâche jusqu'à `<echeance_au_plus_tard>` ; au-delà, ou sans cette ligne, le détruire ».

### CLC5-05 — à exiger par la consigne — bac à sable de Claude Code et mandataire sur le poste

- **Chemin (raisonné, non éprouvé : je n'ai pas le poste)** : si la session locale tourne avec le bac à sable de Claude Code,
  les processus lancés en héritent.
  - Le réseau passe par un mandataire tenu par la session, qui meurt avec elle.
  - Sous Linux, l'espace de processus peut finir avec la commande.
  - « Le processus détaché continue » serait alors vrai sans réseau, ou faux.
  - Même risque si `HTTPS_PROXY` désigne un mandataire propre à la session : la minuterie en hérite.
- **Correction (consigne)** :
  - commandes du harnais hors du bac à sable ;
  - avant L5, un essai à blanc : un `sleep` détaché survit à la fin de la commande, puis à la fin de la session ;
  - `python3 -c "import urllib.request; print(sorted(urllib.request.getproxies()))"` ne rend que des noms, jamais une
    valeur, et doit rendre `[]` ou un mandataire du système.

### CLC5-06 — à corriger (R5) — 5 de mes 16 mutations survivent

| Mutation | Ce qui survit | Poids |
|---|---|---|
| **m10** | `veiller` conclut à l'absence sur **une seule** lecture (404) | **fort** : un 404 erroné arrêterait la garde, serveur allumé |
| m09 | `DELAI_SURVIE_S = 0` : aucune attente de la ligne « garder » | succès : chaque création serait détruite aussitôt (sens prudent) |
| m11 | `ps` par défaut ignoré (macOS) | succès sous macOS : minuterie toujours vue morte (sens prudent) |
| m01 | 4 refus durables en lecture au lieu de 3 | faible |
| m15 | 403 en lecture d'un serveur lu comme 404 | faible : l'inventaire refuse ensuite |

Tuées : m02 à m08, m12 à m14, m16. Le code lu est juste sur ces cinq points ; ce sont des gardes sans essai.

### CLC5-07 — mineur — adresse IPv4 publique du poste écrite et poussée

- **Chemin (éprouvé)** :
  - `acces-creer` écrit `ip_poste` dans le fichier d'accès, poussé à L3 ;
  - `couper_acces` n'en a pas besoin : il reprend `--ip-poste` ;
  - `scripts/depot_expurge.py` ne retire rien de ce dossier : seul `registres/**` est retiré parmi les registres de
    travail. Une copie publique future porterait donc l'adresse de Lazar.
- **Correction** :
  - ne pas l'écrire, ou ajouter `acces-machine-*` aux retraits ;
  - relire aussi les sorties de coupure (`coupure-v5.txt`) avant toute copie publique.

### Notes (sans correction exigée)

1. **`acces-couper`** pose les règles sur l'identifiant du fichier d'accès **sans relire le nom** du pare-feu (éprouvé sur un
   pare-feu renommé). Plausibilité faible ; `acces-supprimer`, lui, relit le nom.
2. **`fichier_pousse`** prouve qu'une référence distante locale contient le commit, pas que le dépôt distant l'a : une
   référence écrite à la main passe (éprouvé). La vraie preuve est le `fetch` de la mère (M1). En option : le mot « armée »
   porte l'empreinte du fichier de rattrapage que la mère a lu, et la session locale la compare avant L5.
3. **`creer-et-armer`** ne lie pas `--cle-ssh` et `--pare-feu` au fichier d'accès poussé. Dans un autre projet, ces
   identifiants n'existent pas et l'interface refuse (raisonné). La création n'est donc liée au projet prouvé que par la
   procédure.
4. **Fenêtre de 60 s** : une première lecture lente (délai de 30 s plus une pause) donne une minuterie « muette », donc une
   destruction (sens prudent). Une fenêtre de 120 à 180 s coûterait moins de 0,02 USD.
5. **Motif contradictoire** : le motif de `verifier_minuterie` dit « relancer la minuterie, ou detruire », alors que la
   procédure dit détruire. La consigne doit dire : jamais de relance.
6. **Veille sous macOS** : `caffeinate -i` n'empêche pas la veille capot fermé (raisonné). Une déconnexion de la session
   macOS tue aussi la minuterie.
7. **Messages de la mère** : complets sur le quoi faire. Ils ne portent ni les formes `curl` de l'annexe (en-tête sur
   l'entrée standard), ni la conduite sur une erreur passagère (réessayer, puis prévenir Lazar).
8. **Commandes sans borne** : `inventaire` et `detruire` réessaient sans fin sur une panne passagère, mais bruyamment. Au
   premier plan, l'outil les coupe : la consigne doit dire « refaire 15 minutes plus tard, puis prévenir Lazar ».
   `piloter_poste_v5.sh` n'a aucune borne par commande SSH ; l'installation de Mathlib dépasse les 10 minutes d'une commande
   de premier plan, d'où la consigne 9.

## Question 2 — les trois cas, et la dépense

Prix retenu : `ccx33`, prix le plus haut du relevé (0,3355 EUR/h) plus l'adresse (0,0010 EUR/h), taux 1,25 ⇒ 0,4206 USD/h.

| Cas | Ce qui se passe (code et procédure) | Ce qui le rattrape | Durée et coût au pire |
|---|---|---|---|
| **La session locale meurt juste après la création**, ordinateur allumé | Le processus détaché continue (éprouvé ici), contrôle la survie, rend la main. La minuterie détruit à `min(création + 48 h, H − 1 h)`, soit au plus préparation + 46 h. Rien d'utile n'est fait entre-temps. | la minuterie ; la mère à `H` | ≤ 46 h, 19,35 USD. Réserves : CLC5-05 (bac à sable), CLC5-01 (destruction à tort). |
| Elle meurt **et** le processus détaché est tué entre l'appel de création et la minuterie | Serveur allumé, aucune minuterie. | la mère à `H` (≤ 47 h après la préparation) ; à `H + 24 h` si la première tâche tombe | 47 h, 19,77 USD ; 71 h, 29,86 USD (30,29 avec l'heure entamée), **plus le retard de livraison** (CLC5-02) |
| **L'ordinateur s'éteint** ou dort | Après une extinction, la minuterie est morte ; la session locale reprise fait `verifier-minuterie` : non conforme deux fois, donc destruction. Après une veille, la minuterie reprend seule, et détruit aussitôt si l'échéance est passée (horloge murale). | la mère à `H`, puis `H + 24 h` | idem |
| **La mère détruit à distance** pendant le travail | La minuterie constate l'absence par deux lectures, solde le journal et s'arrête (essais de l'auteur ; m10 montre que la règle des deux lectures n'est pas gardée par un essai dans `veiller`). Le pilote s'arrête sur SSH (`set -e`). Pas de recréation : la procédure l'interdit et le code la refuse dans le même clone (pas dans un clone neuf : CLC5-03). | — | aucun coût. Deux sources : les tâches à `H` (au moins une heure après l'échéance de la minuterie : rien à détruire, normalement), et la routine de reprise (CLC5-04). |

**Un serveur peut-il rester allumé ? La dépense peut-elle dépasser 65 USD ?**

- **Gardes vivants** : non.
  - Au pire 20,19 USD à 48 h.
  - Deux machines ne coexistent pas (nom unique, contrôle de l'inventaire avant l'appel).
  - Le prix est revérifié au démarrage de la minuterie.
- **Une seule voie au-delà de 65 USD**, si tout tombe ensemble :
  - minuterie locale morte, et les deux tâches de la mère tombées ou retardées ;
  - aucune session de la mère pour faire la routine de reprise ;
  - personne pour regarder la console.
  - 65 USD sont alors atteints en **155 h (6,4 jours)** pour `ccx33`, 248 h pour `ccx23`, 900 h pour `cx53`.
- CLC5-02 et le rappel de Lazar ferment l'essentiel de cette voie.

## Question 3 — le code neuf ouvre-t-il un trou ?

- **Secrets sur disque : non.**
  - `HCLOUD_TOKEN` n'est jamais écrit : il passe seulement dans l'environnement de l'enfant, et les erreurs du transport ne
    portent que le type, avec `from None`.
  - La sortie de `--detache` ne porte aucune valeur d'environnement (éprouvé avec une variable factice).
  - Une clé privée, une clé sur deux lignes ou une clé `sk-` est refusée avant tout appel, sans écho du contenu (éprouvé).
  - La clé SSH est créée hors du dépôt par la procédure. Le fichier d'accès ne porte que des identifiants, le nom et
    l'empreinte publique, plus l'adresse du poste (CLC5-07).
- **Commandes non bornées** : voir la note 8 ; rien de muet.
  - `preparer`, `acces-*` et `verifier-minuterie` font des requêtes uniques (délai de 30 s) ou des lectures locales.
  - `creer-et-armer --detache` est borné par sa fenêtre de 10 minutes et le contrôle de 60 s, sauf une destruction en panne
    passagère, qui réessaie sans fin dans son processus détaché.
- **Destruction d'un serveur qui n'est pas le sien : non.**
  - Toute voie de DELETE relit le serveur par son identifiant et exige le nom exact `lean-outillage-d1a` (éprouvé :
    `--pas`, autres noms intacts).
  - `inventaire` est en lecture seule (essais i01 et i02 ; ma mutation m07 est tuée).
  - `acces-supprimer` relit les noms ; `acces-couper` non (note 1).

## Ce que la consigne du poste local et la procédure de la mère doivent exiger

**Avant toute création.**

1. **Code** : la v5 corrigée de CLC5-01, contre-lue courte. À défaut, la consigne dit quoi faire si `creer-et-armer` rend
   « minuterie non armée … serveur détruit » : section 4, compte rendu, et aucun second essai sans consigne neuve.
2. **Poste** :
   - `python3 --version` ≥ 3.11 ; `git`, `ssh`, `ssh-keygen` présents ;
   - **un seul clone**, dont `git remote -v` montre `lciric/controle-ia-travail` (jamais `lciric/controle-ia`) ;
   - une seule préparation ; toutes les commandes depuis la racine du clone ;
   - les commandes du harnais pré-autorisées, pour qu'aucune destruction n'attende une demande de permission.
3. **Hors du bac à sable de Claude Code** pour les commandes du harnais. Essai à blanc de survie d'un processus détaché, et
   aucun mandataire propre à la session (CLC5-05).
4. **Mère** :
   - M1 à M4 tels qu'écrits ; M5 avec **au moins une tâche en session neuve à chaque déclenchement** ;
   - les tâches relues après création ; leurs identifiants dans `registres/etat.md` et dans chaque passation (CLC5-02) ;
   - la ligne « en tâche jusqu'à … » pour la routine de reprise (CLC5-04) ;
   - le mot « armée » porte l'empreinte du fichier de rattrapage lu (note 2).
5. **Lazar** : un rappel personnel à `H + 1 h` pour regarder la console de Hetzner.

**À la création (session locale).**

6. **L5** une seule fois, détachée. Attente par commandes bornées ou en arrière-plan, 15 minutes au plus. Toute fin autre
   que l'objet JSON final ⇒ section 4. Aucun second essai.
7. **L6** dans la minute, puis **L7** tout de suite, journal des créations compris. Une fois poussé, il ferme CLC5-03 pour
   tout clone de la branche ; avant L7, seule la correction de CLC5-03 le ferme.

**Pendant le travail.**

8. **Ordinateur** sur secteur, veille coupée, capot ouvert, pas de déconnexion ; `caffeinate` lancé détaché.
9. **Phases du pilote** en arrière-plan, sorties dans des fichiers : l'installation dépasse la limite d'une commande de
   premier plan.
10. **À chaque reprise de session** : lire la sortie de la création et le fichier PID, puis `verifier-minuterie`.
    **Jamais de relance d'une minuterie.** Non conforme deux fois à 2 minutes d'écart ⇒ `detruire --identifiant N`.
11. **Jamais** renommer le serveur ni toucher à ses étiquettes. Machine injoignable ⇒ `inventaire` ; absente ⇒ pas de
    recréation, compte rendu.
12. **Tout `detruire` qui ne rend pas de code** (coupé par l'outil) : refaire 15 minutes plus tard, puis prévenir Lazar et
    la mère.

**À la fin.**

13. **Section 5** telle qu'écrite :
    - `inventaire` sans serveur ni adresse libre, puis `acces-supprimer` ;
    - la minuterie arrêtée par son PID (R10) si elle vit ;
    - pièces poussées ; la mère relit par son propre jeton avant de désarmer.
    - Aucune copie publique avec l'adresse du poste (CLC5-07).

## Ce que j'ai lancé

- **Essais depuis l'arbre**, jeton retiré de l'environnement :
  - commande : `PYTHONPATH=<arbre>/src:<bac>/essais …/.venv/bin/python -m pytest -q -o pythonpath= -p trace_import
    --basetemp=<bac>/pytest-tmp tests/test_lean_essai_*v5*.py`, où `trace_import` est un greffon à moi qui imprime le
    chemin des modules importés ;
  - résultat : **57 passed** ;
  - import tracé : `<bac>/arbre/src/controle_ia/lean_essai/minuterie_v5.py`, `hetzner_v5.py`, `minuterie_v4.py`,
    `controle_ia/gardes.py` ;
  - essais v1 à v4, sauf `gardes_v2` : **306 passed**.
- **Mutations** :
  - les 74 de l'auteur, rejouées par son lanceur sur mon arbre : 74 tuées, aucune par délai ;
  - mes 16 (`mutations_cl5.py`, témoin vert exigé) : 11 tuées.
  - Un premier passage de mes mutations, au témoin en échec (dossier de `--basetemp` absent), a été écarté.
- **Scripts dans mon bac** (`…/scratchpad/cl5-lean-d1a/essais/`, non versés), lancés avec `python -I -B` et sans jeton :
  - `faux_hetzner.py` : mon faux transport ;
  - `demo_clc4.py` : rejeu de CLC4-01 à CLC4-07 ;
  - `demo_reel.py` : vrai `creer_et_armer` avec une vraie minuterie détachée ;
  - `demo_course.py`, `demo_course20.py`, `demo_sonde_exec.py`, `demo_sonde_exec2.py` : CLC5-01 ;
  - `demo_trous.py` : question 3 ;
  - `mutations_cl5.py`.
- **Vrais processus** : 139 minuteries lancées sans jeton (aucun appel réseau possible) et un `sleep` détaché.
  - Chacun a été arrêté par son PID après contrôle de sa ligne de commande (R10), sauf deux minuteries que je n'ai pas
    arrêtées : elles étaient absentes ensuite (mortes au retrait de leur dossier temporaire, cause probable).
  - Contrôle final par `ps` : aucune ne reste.
- **Respect des interdits** :
  - rien lu de `diag/`, `runs/`, du bras d'attaque, du mode tenu à l'écart, de T0.6, T0.7 ni de P3-bis ;
  - aucune recherche récursive sur le dépôt ;
  - aucune variable d'environnement listée, aucune valeur de clé ;
  - aucun appel à Hetzner, aucun `rm -rf` ;
  - suppressions, toutes dans mon bac : un `rm -r` sur mes propres copies de mutations, avant le second passage ; les
    dossiers temporaires de mes scripts ; et les copies du lanceur de l'auteur, qui les retire lui-même (`shutil.rmtree`) ;
  - arbre retiré à la fin ; mes copies de mutations restent dans mon bac.
