# Plan de lancement du pilote 8B de T0.5 — v3

v3 (2026-10-12) : après les sceptiques de la relecture R2 (CH-03 : garde de relance des contrôles et de la récupération
lue sur un fichier, jamais par un tube vers `grep -q` sous `pipefail`, qui donnait un faux « sans episodes.json ») et la
vérification courte du candidat 2 (VH-01 à VH-12, VT-01) : le scellement relit lui-même les épingles, le code relu et le
journal de la répétition jouet (VH-01) ; la répétition jouet consigne et fait comparer les scripts qu'elle exécute
(VH-02) ; un arrêt avant la poussée initiale est un nœud, et ce qui le suit est écrit (VH-03, VT-01) ; banc du
scellement (VH-07) ; révocation lue par cellules (VH-05) ; récupération : dossier de travail propre, code 1 en échec,
copie versée exigée (VH-08, VH-12) ; proposition N-019 v2 ; préenregistrement rempli depuis le brouillon 10 (VT-01 à VT-03 : arrêts d'avant la poussée initiale en nœud, préséance « écrit et poussé », liste des causes fermée), relancement aligné (étape 5). La v2 est gardée.

v2 (2026-10-12) : après la relecture R2 du brouillon 8 (remarques TX, CO, NO, CH ;
`prereg/contre-lectures/T0.5-pilote-v1-relecture-b8-*`) : décision de Lazar sur N-019 exigée (GO cité par le
préenregistrement, contrôlé par le scellement, les contrôles avant dépense et le lanceur ; NO-03), colonne d'état de
N-019 à une forme exacte (CH-10) ; causes d'arrêt définies dans le préenregistrement (TX-01) ; lecture d'une fin en code 1
(CO-08) ; arbre gelé de S égal au code relu épinglé (CH-01) ; relancement qui tolère l'instance du premier lancement
(CH-02) ; bancs des contrôles et du lanceur (CH-03) ; carte limitée à l'A100 SXM4 (CH-04) ; parties masquées
reconstruites (CH-05) ; entrées du générateur sous sceau (CH-06, CH-07) ; scellement lisible (CH-08) ; récupération
complétée (CH-09) ; scripts, plan et répétitions alignés (CH-12) ; base de la surveillance (CH-13). La v1
(`plan-lancement-pilote-v1.md`) est gardée.

Remplace la procédure de lancement du pilote (brouillon 4, `brouillons/T0.5-pilote-8B-procedure-v1-brouillon4.md`),
antérieure à N-016 et à la chaîne durcie de la revalidation (état des lieux du pilote, ML-01 à ML-13, HR-05). Il suit la
chaîne de la revalidation v2 (`docs/procedures/revalidation-T0.5-v2/plan-lancement-revalidation-v7.md`), adaptée au
pilote. Préenregistrement : `prereg/T0.5-pilote-8B-v1.md` (brouillon 10 rempli) ; configuration :
`prereg/T0.5-pilote-config-v1.json` ; tâches : `donnees/t05-pilote-v1/taches-pilote-60-v1.json` (option (a) de la
proposition N-019, `docs/decisions/proposition-N-019-v2.md`).

Les scripts s'exécutent depuis le bloc-notes (`pilote-v1/`) ; leurs copies versées et scellées sont sous
`docs/procedures/pilote-T0.5-v1/`. **Chaîne** (treize scripts, liste `CHAINE` du scellement) : `deriver_taches_pilote_v1.py`,
`remplir_pilote_v1.py`, `normaliser_pilote_v1.py`, `controles_avant_depense_pilote_v1.sh`, `lancer_pilote_v1.sh`,
`sceller_pilote_v1.sh`, `recuperation_pilote_v1.sh`, `repetition_jouet_pilote_v1.sh`, `repetition_finale_pilote_v1.sh`,
`essais_lanceur_pilote_v1.sh`, `essais_controles_pilote_v1.sh`, `essais_generateur_pilote_v1.sh`,
`essais_scellement_pilote_v1.sh`. Le scellement exige l'égalité des treize copies avec le bloc-notes ; le lanceur, celle des trois qu'il exécute (contrôles, normaliseur, lanceur) avec leurs copies au commit S.
**Jamais** de `vastai show instance <id> --raw` ni de `vastai show instances --raw` sans filtre : forme filtrée
seulement, champs nommés.

0. **Préalables**, dans cet ordre :
   1. verdict R13 de la revalidation v2 scellé (`docs/verdicts/verdict-T0.5-revalidation-v2.md`) ; proposition N-019
      scellée (`docs/decisions/proposition-N-019-v2.md`, qui remplace la v1) ; **décision de Lazar** : GO de type « revendication » dans
      `registres/go.md` (accordé par Lazar, qui cite N-019 et l'option (a)) ; colonne d'état de la ligne N-019 de
      `registres/decisions.md` exactement « tranché (a) par Lazar : GO-AAAA-MM-JJ-NN (R-NNN) », rien d'autre ; ligne
      R-NNN qui consigne le GO. Une révocation de cette décision s'écrit par une ligne de type « révocation » de
      `registres/go.md` (colonne « type », lue par cellules) qui nomme le GO, et la colonne d'état quitte la forme exacte : ce sont les deux seules formes
      lues par la chaîne (aucun mot-clé cherché dans les lignes R-…). Sans GO, rien n'est scellé ni lancé ;
   2. fichier des 60 tâches dérivé (`deriver_taches_pilote_v1.py`), scellé, ajouté de force au suivi ;
   3. brouillon 10 scellé, son empreinte épinglée dans le générateur (`SHA_BROUILLON`) ; candidat rempli (générateur en
      mode `candidat`) versé sous `brouillons/`, scellé, et vérifié (R2) par des sous-agents neufs ; corrections
      faites ; épingles écrites dans `controles_avant_depense_pilote_v1.sh` : candidat vérifié (brut et normalisé),
      rapports attendus (état des lieux, relecture R2 et ses vérifications courtes), **commit du code relu** (`CODE_RELU`), **journal de la
      répétition jouet** (`REPETITION_JOUET`) ;
   4. copies versées et scellées sous `docs/procedures/pilote-T0.5-v1/` : les treize scripts de la chaîne, ce plan, le
      journal de la répétition jouet (`repetition-jouet-pilote-v1.log`) et les journaux des bancs ;
   5. **répétition jouet** de l'instance (`repetition_jouet_pilote_v1.sh`, ETUDE=pilote) **au commit du code relu** : son
      journal commence par « commit du code répété : <CODE_RELU entier> », puis « script répété : <nom> <sha256> »
      pour les cinq scripts qu'elle exécute (depuis des copies faites au début), une ligne par script, les cinq exactement,
      comparés par les contrôles avant dépense aux copies versées à S ; le script de la répétition est lancé depuis une
      copie figée (chemin absolu), sans toucher au bloc-notes pendant qu'elle tourne ; quatre passages (sain ; branche présente, code 2 ; premier lancement manqué, code 1 ;
      relancement, code 0) ; récupération conforme en mode premier et en mode relance ; deux artefacts refusés, chacun à
      son KO attendu (premier lancement avec épisodes ; notations manquantes) ; journal versé, scellé, épinglé, relu par
      les contrôles avant dépense. La chaîne est figée avant cette répétition. **Répétition finale à blanc** (`repetition_finale_pilote_v1.sh` : GO fictif dans un clone
      jetable, scellement puis contrôles) : conforme. **Bancs** (un cas sain et un artefact par garde nouvelle) : lanceur
      (`essais_lanceur_pilote_v1.sh`), contrôles avant dépense (`essais_controles_pilote_v1.sh`, cas de relance compris ;
      suite et tokeniseurs remplacés par des bouchons, joués en vrai par la répétition finale ; la garde des tokeniseurs
      n'a pas d'artefact isolable, toute configuration altérée étant arrêtée d'abord par « configuration = brouillon »),
      générateur (`essais_generateur_pilote_v1.sh`), scellement (`essais_scellement_pilote_v1.sh`) : conformes, lus cas
      par cas ;
   6. tout committé et poussé.
1. **Scellement** : `sceller_pilote_v1.sh <GO> <R-…>` (décision de Lazar sur N-019, vérifiée par le générateur dans les
   registres de HEAD et citée par le texte). Avant l'entropie, il refuse toute épingle restée « A_EPINGLER » ou tout
   rapport hors des deux familles, exige l'arbre gelé de HEAD égal au code relu épinglé, les copies versées de la chaîne et le journal
   de la répétition jouet suivis à HEAD, et ce journal à son empreinte épinglée, au code relu (VH-01, VH-09). Il tire l'entropie (`SeedSequence`), régénère le texte en mode `reel`
   (normalisé égal au candidat vérifié), scelle la configuration et le préenregistrement, un seul commit S, poussé, relu
   sur le dépôt distant. Tout arrêt sort en code 2 ; un échec avant le commit retire les fichiers qu'il a créés ; le
   dossier de travail (entropie tirée, texte, configuration) est retiré dans tous les cas ; les lignes ÉCHEC de
   `verifier-arbre` sont affichées.
2. **Contrôles avant dépense** : `controles_avant_depense_pilote_v1.sh S <dossier neuf>` (le lanceur les rejoue) :
   contenu de S, commit du code, arbre gelé égal au code cité **et au code relu épinglé**, empreintes des scripts,
   configuration et tâches, valeurs du verdict recalculées (lecture gelée rejouée à 192 puis à 180 épisodes : noyau,
   durée projetée, `duree_max_s`), décision de Lazar sur N-019 (GO conforme, non révoqué ; colonne d'état exacte ; ligne
   du registre ; GO de calcul non révoqué), index des invites à son empreinte citée, texte égal au candidat vérifié
   normalisé, **parties masquées reconstruites** (lignes des rapports, dates, nombre de tests), journal de la répétition
   jouet, rapports, branche absente, ligne « Lancement », `problemes()`, sceaux, `verifier-arbre`, gardes du lanceur du
   pilote, format des vrais tokeniseurs (8B, 3B), **suite complète des tests au commit S** dans l'environnement neuf
   (dernière ligne « N passed »), garde de calcul.
3. **Offre et crédit** : offre conforme au filtre (**A100 SXM4 seulement** : le débit des épisodes a été mesuré sur
   elle, CH-04 ; `gpu_ram ≥ 79`, une carte, CUDA ≥ 13.0, vérifiée, centre de données, fiabilité ≥ 0,99, mémoire vive
   ≥ 128 Go, disque ≥ 80 Go), relue par le lanceur (carte « A100 SXM4 » exigée), archivée avec le processeur
   (`cpu_name`, `cpu_arch`, `cpu_cores`), **limitée au processeur de la revalidation** (« AMD EPYC 7513 32-Core
   Processor » : débit mesuré sur lui, AVX2 ; sinon, le pilote attend une offre conforme) ; prix ≤ 1,30 USD l'heure ;
   **crédit ≥ 6 h × prix + 1,2 USD** (deux modèles téléchargés, environ 26 Go) ; sinon code 3, rien ne se crée :
   recharge demandée à Lazar. Cette marge couvre le risque d'un crédit épuisé pendant le run, qui arrêterait l'instance
   sans `arret.json` ni poussée (leçon de N-012).
4. **Création** : `lancer_pilote_v1.sh <offre> <dossier de traces neuf>`, en un seul appel, aucun sous-agent en cours.
   Refus entre 23:30 et 00:00 UTC (au départ et juste avant la création) ; au moins 3 Go libres ; instances arrêtées
   55292763 et 55458787 tolérées si relues arrêtées (et, en relance, celle du premier lancement), aucune autre ; scripts
   exécutés égaux à leurs copies versées à S ; jetons vérifiés avant les contrôles ; contrôles bornés à une heure ;
   colonne d'état de N-019 exacte, GO de Lazar cité par S, relu dans le registre courant, non révoqué, comme le GO de
   calcul ; `ETUDE=pilote`, `PREREG`, `BRANCHE`, `DEPOT_URL` passés ; étiquette `t05-pilote-v1`. Codes : 0 création ;
   3 heure, place, crédit ou prix ; 2 tout autre arrêt avant la ligne « creation » de `lancement.txt` ; 4 tout échec
   après : vérifier les instances (forme filtrée). **Avant** la création : identifiant prévu et heure dans
   `registres/etat.md`, engagement de dépense dans `registres/depenses.md` (étape de procédure : le lanceur ne la
   contrôle pas).
   **4 bis** : entre 3 et 5 minutes après la création, `vastai logs <id> --tail 200`, masqué, dans
   `<traces>/journal-5min.txt` : « AMORCE <date> : commit <S> », puis « début : ETUDE=pilote MODE=reel COMMIT=<S>
   BRANCHE=calcul/t05-pilote-reel-v1 », « préenregistrement lu : <N> tests attendus », la carte (`nvidia-smi`) et
   « branche … poussée avant l'installation ». Sinon : arrêt par identifiant (R10), nœud.
5. **Surveillance et relancement** : `PATH=<bloc-notes>/venv-vastai/bin:$PATH bash
   docs/procedures/surveiller-instance-t04-v1.sh <id> <base> <dossier>`, avec la **base écrite par le lanceur** dans
   `lancement.txt` (ligne « base de la surveillance », création − 3 900 s), recopiée telle quelle. Avec cette base, le
   message « PLAFOND : 6 heures depuis la création » du script de surveillance tombe en fait **17 700 s après la
   création** (5 heures du devis moins 5 minutes) : c'est ce plafond qui compte (CH-13). Tâche de fond de 7 200 000 ms,
   relancée à l'identique jusqu'à la fin ; rappel `send_later` à la création + 17 700 s + 10 minutes. **Relancement**
   unique, sans nouvelle version : seulement pour une cause d'infrastructure **après la poussée initiale**, au sens du
   préenregistrement (section « Critères de lecture gelés », Préséance et causes d'arrêt : réseau, préchargement
   compris ; instance perdue ; carte indisponible pour torch ou erreur de la carte autre que de mémoire ; mise en place
   trop lente ; signal TERM ou arrêt par la surveillance si la mise en place a dépassé 1 500 s ; jamais l'échéance
   interne), dans le reste du devis et du crédit, consignée par une ligne R-… qui cite la cause, l'étape et le motif,
   dit « relancement »,
   « pilote », « infrastructure » (en toute casse) et nomme une seule fois l'instance du premier lancement
   (« instance NNNNNNNN » : arrêtée, gardée, tolérée par le lanceur ; CH-02) ; `episodes.json` ni écrit ni poussé (absent de la branche `-v1` ; écrit mais non poussé : récupération depuis
   l'instance gardée, sinon nœud ; préséance) ; `lancer_pilote_v1.sh <offre> <traces neuves> relance R-…` (branche
   `calcul/t05-pilote-reel-v2`, mêmes contrôles rejoués en mode relance). **Arrêt avant la poussée initiale** (la
   branche `-v1` n'existe pas) : nœud (préenregistrement, Préséance) ; si Lazar décide un nouveau lancement, il détruit
   d'abord la première instance (rien n'y a été calculé : le lanceur ne la tolère pas en mode premier), puis le
   lancement se refait en mode premier, branche `-v1` neuve (VH-03).
6. **Sortie** : FIN (code 0, 1 ou 2), ÉTAT TERMINAL ou PLAFOND → arrêt immédiat par identifiant (R10). Un code 1 se lit
   sur le journal avant toute conclusion : arrêt consigné, ou run complet dont la poussée finale a échoué (« run complet,
   mais poussée finale impossible » : résultats et traces sur l'instance, gardée ; CO-08) ; état relu
   « stopped » (forme filtrée), `registres/arrets.md`. Les redémarrages de l'amorce par le conteneur (mode « args »)
   sont refusés par R12, sans effet ; arrêter dès la ligne « AMORCE … fin, code N ».
7. **Récupération** : `recuperation_pilote_v1.sh S <dossier neuf>` (`relance` pour la branche `-v2` : la branche `-v1`
   est lue et citée, sans `episodes.json`, liste de son arbre lue sur un fichier) ; elle exige d'être sa copie versée à S
   (VH-12), écrit ses fichiers de travail dans `<dossier neuf>.travail` et sort en code 1 si un contrôle échoue (VH-08) : ascendance, ajouts seulement, un run, sceaux, manifeste et citations
   (configuration, entropie, tâches, versions), issue ; run complet : fichiers exigés (épisodes, appariement, notations
   décisives et descriptives de chaque juge) et comptes exacts (180 épisodes ; notations de chaque juge égales aux
   passes des épisodes à ensemble non vide, au plus 240 ; paires de l'appariement), recalculés par les fonctions du code
   cité ; arrêt : état `partiel` affiché ; **vecteurs sur `donnees/t05/<run>`** (commit sans parent, empreinte égale à
   celle d'`episodes.json`) ; journal, carte et mémoire (`nvidia-smi.txt` : A100 SXM4, au moins 75 Gio), `pip freeze`
   versé ; aucun jeton ; puis fusion de la branche de résultats dans `main` (commit de fusion), poussée. **Aucune
   proposition de destruction de l'instance tant que les vecteurs ne sont pas vérifiés** (PL-11 ; leçon de N-012).
8. **Lecture** : préparation, étiquetage par des sous-agents neufs, lecture et analyse selon le préenregistrement, par un
   sous-agent neuf (R13 pour la partie qui touche le critère 2 de G0) ; verdict scellé, soumis à Lazar ; dépense
   consignée.

Réserves déclarées : jeton GitHub de l'instance non éprouvable depuis la session (poussée initiale sur l'instance) ;
garde de calcul inactive dans la session (rejouée par le lanceur) ; jetons dans les arguments du processus vastai pendant
la création (aucun sous-agent en cours) ; durée des juges jamais mesurée (préenregistrement, « Calcul ») ; le relancement
n'a été éprouvé qu'en répétition jouet ; la répétition jouet réutilise un environnement neuf existant
(`VENV_EXISTANT`) : l'installation depuis `requirements-gpu.txt` n'y est pas rejouée (elle a tourné en vrai sur
l'instance de la revalidation v2 ; place disque de la session) ; la vérification du GO repose sur le texte des registres
(lignes que la session écrit sous la dictée de Lazar) ; une révocation écrite ailleurs que dans les deux formes lues
(ligne « révocation » de `registres/go.md`, colonne d'état de N-019) n'arrête pas la chaîne : la session l'écrit sous ces
deux formes (CH-10) ; la délégation R-140 ne couvre pas N-019 : sans GO de Lazar, le pilote attend ; une recharge seule
n'est pas un GO ; l'état « partiel » d'un arrêt n'est affiché que sur un arrêt réel (la répétition jouet n'en produit
pas après le manifeste) ; une offre conforme (A100 SXM4, AMD EPYC 7513) peut se faire attendre.
