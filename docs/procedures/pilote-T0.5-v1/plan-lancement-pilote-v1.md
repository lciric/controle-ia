# Plan de lancement du pilote 8B de T0.5 — v1

Remplace la procédure de lancement du pilote (brouillon 4, `brouillons/T0.5-pilote-8B-procedure-v1-brouillon4.md`),
antérieure à N-016 et à la chaîne durcie de la revalidation (état des lieux du pilote, ML-01 à ML-13, HR-05). Il suit la
chaîne de la revalidation v2 (`docs/procedures/revalidation-T0.5-v2/plan-lancement-revalidation-v7.md`), adaptée au
pilote. Préenregistrement : `prereg/T0.5-pilote-8B-v1.md` (brouillon 8 rempli) ; configuration :
`prereg/T0.5-pilote-config-v1.json` ; tâches : `donnees/t05-pilote-v1/taches-pilote-60-v1.json` (N-019).

Les scripts s'exécutent depuis le bloc-notes (`pilote-v1/`) ; leurs copies versées et scellées sont sous
`docs/procedures/pilote-T0.5-v1/`, et le scellement comme le lanceur exigent l'égalité des deux. **Jamais** de
`vastai show instance <id> --raw` ni de `vastai show instances --raw` sans filtre : forme filtrée seulement, champs
nommés.

0. **Préalables**, dans cet ordre :
   1. verdict R13 de la revalidation v2 scellé (`docs/verdicts/verdict-T0.5-revalidation-v2.md`) ; décision N-019
      (`docs/decisions/decision-N-019-v1.md`) scellée et consignée (R-…), non révoquée ;
   2. fichier des 60 tâches dérivé (`deriver_taches_pilote_v1.py`), scellé, ajouté de force au suivi ;
   3. candidat rempli (générateur en mode `candidat`) versé sous `brouillons/` et relu (R2) par des sous-agents
      neufs ; corrections faites ; épingles écrites dans `controles_avant_depense_pilote_v1.sh` (candidat relu, brut et
      normalisé ; rapports attendus : état des lieux, relecture R2) ;
   4. copies versées et scellées sous `docs/procedures/pilote-T0.5-v1/` : dérivation, générateur, normaliseur,
      contrôles (épinglés), lanceur, scellement, récupération, répétitions, ce plan ;
   5. répétition jouet de l'instance (`repetition_jouet_pilote_v1.sh`, ETUDE=pilote, au commit du code cité) et
      répétition finale à blanc (scellement puis contrôles sur un clone jetable) : conformes ;
   6. tout committé et poussé.
1. **Scellement** : `sceller_pilote_v1.sh`. Il tire l'entropie (`SeedSequence`), régénère le texte en mode `reel`
   (normalisé égal au candidat relu), scelle la configuration et le préenregistrement, un seul commit S, poussé, relu sur
   le dépôt distant. Un échec avant le commit retire les fichiers qu'il a créés.
2. **Contrôles avant dépense** : `controles_avant_depense_pilote_v1.sh S <dossier neuf>` (le lanceur les rejoue) :
   contenu de S, commit du code, arbre gelé, empreintes des scripts, configuration et tâches, valeurs du verdict
   recalculées (noyau, durée projetée, `duree_max_s`), texte égal au candidat relu normalisé, rapports, branche absente,
   ligne « Lancement », `problemes()`, sceaux, `verifier-arbre`, gardes du lanceur du pilote, format des vrais
   tokeniseurs (8B, 3B), **suite complète des tests au commit S** dans l'environnement neuf (dernière ligne
   « N passed »), garde de calcul.
3. **Offre et crédit** : offre conforme au filtre (A100 SXM4 ou PCIe, `gpu_ram ≥ 79`, une carte, CUDA ≥ 13.0, vérifiée,
   centre de données, fiabilité ≥ 0,99, mémoire vive ≥ 128 Go, disque ≥ 80 Go), relue par le lanceur, archivée avec le
   processeur (`cpu_name`, `cpu_arch`, `cpu_cores`), **limitée au processeur de la revalidation** (« AMD EPYC 7513
   32-Core Processor » : débit des épisodes mesuré sur lui, AVX2 ; sinon, le pilote attend une offre conforme) ;
   prix ≤ 1,30 USD l'heure ; **crédit ≥ 6 h × prix + 1,2 USD**
   (deux modèles téléchargés, environ 26 Go) ; sinon code 3, rien ne se crée : recharge demandée à Lazar. Cette marge
   couvre le risque d'un crédit épuisé pendant le run, qui arrêterait l'instance sans `arret.json` ni poussée (leçon
   de N-012).
4. **Création** : `lancer_pilote_v1.sh <offre> <dossier de traces neuf>`, en un seul appel, aucun sous-agent en cours.
   Refus entre 23:30 et 00:00 UTC (au départ et juste avant la création) ; au moins 3 Go libres ; instances arrêtées
   55292763 et 55458787 tolérées si relues arrêtées, aucune autre ; scripts égaux à leurs copies versées à S ; N-019
   non révoquée ; `ETUDE=pilote`, `PREREG`, `BRANCHE`, `DEPOT_URL` passés ; étiquette `t05-pilote-v1`. Codes : 0
   création ; 3 heure, place, crédit ou prix ; 2 tout autre arrêt avant la ligne « creation » de `lancement.txt` ; 4
   tout échec après : vérifier les instances (forme filtrée). Consigner l'identifiant et l'heure dans
   `registres/etat.md`, l'engagement dans `registres/depenses.md` **avant** la création.
   **4 bis** : entre 3 et 5 minutes après la création, `vastai logs <id> --tail 200`, masqué, dans
   `<traces>/journal-5min.txt` : « AMORCE <date> : commit <S> », puis « début : ETUDE=pilote MODE=reel COMMIT=<S>
   BRANCHE=calcul/t05-pilote-reel-v1 », « préenregistrement lu : <N> tests attendus » et « branche … poussée avant
   l'installation ». Sinon : arrêt par identifiant (R10), nœud.
5. **Surveillance et relancement** : `PATH=<bloc-notes>/venv-vastai/bin:$PATH bash
   docs/procedures/surveiller-instance-t04-v1.sh <id> <base> <dossier>`, avec la **base écrite par le lanceur**
   (création − 3 900 s, soit un plafond de 17 700 s : 5 heures du devis moins 5 minutes) ; tâche de fond de 7 200 000 ms,
   relancée à l'identique jusqu'à la fin ; rappel `send_later` à la création + 17 700 s + 10 minutes. **Relancement**
   unique, sans nouvelle version : seulement pour une cause d'infrastructure consignée (ligne R-… qui dit
   « relancement », « pilote », « infrastructure »), `episodes.json` absent de la branche `-v1` (table de lecture,
   préséance) ; `lancer_pilote_v1.sh <offre> <traces neuves> relance R-…` (branche `calcul/t05-pilote-reel-v2`, mêmes
   contrôles rejoués en mode relance).
6. **Sortie** : FIN (code 0, 1 ou 2), ÉTAT TERMINAL ou PLAFOND → arrêt immédiat par identifiant (R10) ; état relu
   « stopped » (forme filtrée), `registres/arrets.md`. Les redémarrages de l'amorce par le conteneur (mode « args »)
   sont refusés par R12, sans effet ; arrêter dès la ligne « AMORCE … fin, code N ».
7. **Récupération** : `recuperation_pilote_v1.sh S <dossier neuf>` (`relance` pour la branche `-v2`) : ascendance,
   ajouts seulement, un run, sceaux, manifeste et citations (configuration, entropie, tâches), issue, **vecteurs sur
   `donnees/t05/<run>`** (commit sans parent, empreinte égale à celle d'`episodes.json`), journal, aucun jeton ; puis
   fusion de la branche de résultats dans `main` (commit de fusion), poussée. **Aucune proposition de destruction de
   l'instance tant que les vecteurs ne sont pas vérifiés** (PL-11 ; leçon de N-012).
8. **Lecture** : préparation, étiquetage par des sous-agents neufs, lecture et analyse selon le préenregistrement, par un
   sous-agent neuf (R13 pour la partie qui touche le critère 2 de G0) ; verdict scellé, soumis à Lazar ; dépense
   consignée.

Réserves déclarées : jeton GitHub de l'instance non éprouvable depuis la session (poussée initiale sur l'instance) ;
garde de calcul inactive dans la session (rejouée par le lanceur) ; jetons dans les arguments du processus vastai pendant
la création (aucun sous-agent en cours) ; durée des juges jamais mesurée (préenregistrement, « Calcul ») ; le relancement
n'a été éprouvé qu'en répétition jouet.
