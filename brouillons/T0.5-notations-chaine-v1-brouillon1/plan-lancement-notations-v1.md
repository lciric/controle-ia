# Plan de lancement des notations décisives refaites du pilote de T0.5 — v1 (brouillon 1)

Objet : refaire les notations décisives des juges 8B et 3B sur les ensembles scellés du pilote (N-020, option (a) ;
N-021, option (a) ; GO-2026-10-12-02, R-160), en lancement autonome. Préenregistrement complémentaire :
`prereg/T0.5-pilote-notations-v1.md` ; configuration : `prereg/T0.5-pilote-notations-config-v1.json`. Ce plan décline
le plan de lancement du pilote (`docs/procedures/pilote-T0.5-v1/plan-lancement-pilote-v3.md`), dont il garde l'ordre,
les gardes et les réserves, sauf ce qui suit.

**Différences avec le pilote**
- Aucune entropie n'est tirée : celle du pilote est reprise (mêmes clés, mêmes graines). Aucun générateur : le
  préenregistrement scellé est la copie, octet pour octet, du candidat relu et vérifié ; la configuration, celle de la
  configuration relue.
- Une seule étude, une amorce et un script d'instance à nom nouveau (`scripts/amorce_instance_t05_notations.sh`,
  `scripts/notations_t05_instance.sh`) ; aucun vecteur ; lignes de progression recopiées dans le journal.
- Décision de Lazar lue sur N-021 (colonne d'état à la forme exacte, R-163) et sur `GO-2026-10-12-02`.
- Crédit exigé : 7,5 heures × (prix de l'offre + instances d'autres projets en marche) + 1,2 USD.
- Base de la surveillance : création + 4 800 s, de sorte que le plafond du script de surveillance (base + 6 heures)
  tombe à la création + 26 400 s.
- Instances tolérées arrêtées : 55292763, 55458787 et l'instance du pilote 55538944 (gardée jusqu'au verdict
  complémentaire) ; instances d'autres projets de Lazar nommées en argument.

Les scripts s'exécutent depuis le bloc-notes (`notations-v1/`) ; leurs copies versées et scellées sont sous
`docs/procedures/notations-T0.5-v1/`. **Chaîne** (dix scripts, liste `CHAINE` du scellement) :
`construire_pilote_jouet_v1.py`, `controles_avant_depense_notations_v1.sh`, `lancer_notations_v1.sh`,
`sceller_notations_v1.sh`, `recuperation_notations_v1.sh`, `repetition_jouet_notations_v1.sh`,
`repetition_finale_notations_v1.sh`, `essais_lanceur_notations_v1.sh`, `essais_controles_notations_v1.sh`,
`essais_scellement_notations_v1.sh`. **Jamais** de `vastai show instance <id> --raw` ni de `vastai show instances --raw`
sans filtre : forme filtrée seulement, champs nommés.

0. **Préalables**, dans cet ordre :
   1. décision de Lazar consignée : `GO-2026-10-12-02` (type « revendication », Lazar, N-021, option (a)) ; colonne
      d'état de N-021 exactement « tranché (a) par Lazar : GO-2026-10-12-02 (R-160) » ; ligne R-160 ;
   2. contre-lecture R2 du brouillon du préenregistrement et du code (sous-agents neufs, fichiers donnés
      explicitement) ; rapports versés sous `prereg/contre-lectures/T0.5-notations-v1-relecture-…`, scellés ;
      corrections ; candidat relu (`brouillons/T0.5-pilote-notations-v1-candidat<k>.md`) et configuration relue versés,
      scellés ; vérification courte du candidat par un sous-agent neuf ; épingles écrites dans
      `controles_avant_depense_notations_v1.sh` : candidat, configuration, rapports, **commit du code relu**
      (`CODE_RELU`), **journal de la répétition jouet** (`REPETITION_JOUET`) ;
   3. **répétition jouet** (`repetition_jouet_notations_v1.sh C CANDIDAT RACINE`) au commit du code relu, la chaîne
      figée : quatre passages (sain ; branche présente, code 2 ; premier lancement manqué, code 1 ; relancement,
      code 0) ; récupération conforme en mode premier et en mode relance ; trois artefacts refusés, chacun à son seul KO
      (relance après notations : 0 ; notations manquantes : 4c ; ajout dans le dossier du pilote : 1c) ; journal versé,
      scellé, épinglé ;
   4. copies versées et scellées sous `docs/procedures/notations-T0.5-v1/` : les dix scripts, ce plan, le journal de la
      répétition jouet et les journaux des bancs ; **bancs** (un cas sain et un artefact par garde nouvelle) : lanceur,
      contrôles avant dépense (suite et tokeniseurs remplacés par des bouchons, joués en vrai par la répétition finale),
      scellement ; **répétition finale à blanc** (scellement puis contrôles, clone jetable) : conforme ;
   5. tout committé et poussé (commit des préalables C).
1. **Scellement** : `sceller_notations_v1.sh` (sans argument) : un seul commit S qui n'ajoute que le préenregistrement,
   la configuration et leurs sceaux, poussé, relu sur le dépôt distant.
2. **Contrôles avant dépense** : `controles_avant_depense_notations_v1.sh S <dossier neuf>` (le lanceur les rejoue),
   suite complète des tests au commit S comprise (environ 26 minutes).
3. **Offre et crédit** : A100 SXM4 sur AMD EPYC 7513 seulement (même filtre que le pilote), prix ≤ 1,30 USD de l'heure ;
   crédit ≥ 7,5 h × (prix + autres projets en marche) + 1,2 USD ; sinon code 3, recharge demandée à Lazar.
4. **Création** : `lancer_notations_v1.sh <offre> <traces neuves> <autres projets>` en un seul appel, aucun sous-agent en
   cours. **Avant** : identifiant prévu et heure dans `registres/etat.md`, engagement dans `registres/depenses.md`.
   **4 bis** : entre 3 et 5 minutes après la création, `vastai logs <id> --tail 200`, masqué, dans
   `<traces>/journal-5min.txt` : « AMORCE <date> : commit <S> », « début : ETUDE=notations MODE=reel COMMIT=<S>
   BRANCHE=calcul/t05-notations-reel-v1 », « préenregistrement lu : <N> tests attendus » (N du texte scellé), la carte et « branche …
   poussée avant l'installation ». Sinon : arrêt par identifiant (R10), nœud.
5. **Surveillance** : `docs/procedures/surveiller-instance-t04-v1.sh <id> <base> <dossier>` avec la base écrite par le
   lanceur (création + 4 800 s) ; plafond réel : création + 26 400 s. Rappel `send_later` au plafond + 10 minutes. Lignes
   de progression (juge, rang et durée des lots, fin de chaque juge ; aucun compte de réponses) lues pour la conduite
   du run seulement (débit, échéances) et pour établir qu'un juge est « écrit » (ligne `fin=écrit`) : aucune décision
   n'en dépend hors des règles gelées. **Relancement** unique selon le préenregistrement (Critères de lecture gelés,
   Préséance, Causes d'un arrêt, Relancement) : cause d'infrastructure après la poussée initiale ; aucun juge fini sur
   les pièces (ni fichier, ni ligne `fin=`, ni statut « écrit » ou « échu ») ; dépense engagée + 7,5 h × prix de
   l'offre + 0,5 USD ≤ 10,5 USD ; mise en place lente au-delà de 1 500 s de la ligne « AMORCE » à la ligne « run : ».
   Ligne R-… qui cite la cause, l'étape et le motif, dit « relancement », « notations », « infrastructure » et nomme
   une seule fois l'instance du premier lancement ; puis
   `lancer_notations_v1.sh <offre> <traces neuves> <autres projets> relance R-…` (les contrôles rejouent la préséance
   sur la branche `-v1`). Sinon : nœud, demande de GO à Lazar.
6. **Sortie** : FIN, ÉTAT TERMINAL ou PLAFOND → arrêt immédiat par identifiant (R10) ; état relu (forme filtrée) ;
   `registres/arrets.md`.
7. **Récupération** : `recuperation_notations_v1.sh S <dossier neuf> [relance]` ; puis fusion de la branche de
   résultats dans `main` (commit de fusion), poussée. Aucune proposition de destruction de l'instance avant une
   récupération conforme.
8. **Lecture** : `lire_notations_pilote` (run de lecture distinct), audit R4 si déclenché, puis verdict R13
   complémentaire par un sous-agent neuf, scellé, soumis à Lazar ; dépense consignée.

Réserves : jeton GitHub de l'instance non éprouvable depuis la session ; débit des juges jamais mesuré ; le relancement
n'a été éprouvé qu'en répétition jouet ; la répétition jouet réutilise un environnement neuf existant ; la vérification
du GO repose sur le texte des registres ; une offre conforme peut se faire attendre ; l'instance d'un autre projet de
Lazar en marche (55555587 à 15:05 UTC, 3,98 USD de l'heure) porte le crédit exigé à environ 39 USD.
