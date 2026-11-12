# Plan de lancement des notations décisives refaites du pilote de T0.5 — v1 (brouillon 5)

Objet : refaire les notations décisives des juges 8B et 3B sur les ensembles scellés du pilote (N-020, option (a) ;
N-021, option (a) ; GO-2026-10-12-02, R-160), en lancement autonome. Préenregistrement complémentaire :
`prereg/T0.5-pilote-notations-v1.md` ; configuration : `prereg/T0.5-pilote-notations-config-v1.json`. Ce plan décline
le plan de lancement du pilote (`docs/procedures/pilote-T0.5-v1/plan-lancement-pilote-v3.md`), dont il garde l'ordre,
les gardes et les réserves, sauf ce qui suit. Brouillon 3 : traitement de la contre-lecture R2 de la chaîne
(surveillance propre aux notations, relevé cumulatif, relancement dans le plafond du GO, chaîne figée après C).
Brouillons 4 et 5 : traitement des deux tours de la vérification courte (preuves des essais lues avant S, répétition
jouet à sept artefacts, bancs comptés).

**Différences avec le pilote**
- Aucune entropie n'est tirée : celle du pilote est reprise (mêmes clés, mêmes graines). Aucun générateur : le
  préenregistrement scellé est la copie, octet pour octet, du candidat relu et vérifié ; la configuration, celle de la
  configuration relue.
- Une seule étude, une amorce et un script d'instance à nom nouveau (`scripts/amorce_instance_t05_notations.sh`,
  `scripts/notations_t05_instance.sh`) ; aucun vecteur ; lignes de progression recopiées dans le journal (juge, rang et
  durée des lots, une ligne de fin par juge ; aucun compte de réponses).
- Décision de Lazar lue sur N-021 (colonne d'état à la forme exacte, R-163) et sur `GO-2026-10-12-02`, par le module
  commun `verifications_notations_v1.py` (le même texte pour le scellement et les contrôles).
- Crédit exigé : 7,5 heures × (prix de l'offre + instances d'autres projets en marche) + 1,2 USD.
- Surveillance par `surveiller_notations_v1.sh` (nom nouveau, R12), plafond écrit en clair : la création + 26 400 s,
  sans base décalée ; relevé cumulatif des lignes « AMORCE » et « PROGRES » (`progres.txt`), jamais tronqué.
- Instances tolérées arrêtées : 55292763, 55458787 et l'instance du pilote 55538944 (gardée jusqu'au verdict
  complémentaire) ; instances d'autres projets de Lazar nommées en argument, jamais arrêtées ni détruites (55505836,
  55555587).

Les scripts s'exécutent depuis le bloc-notes (`notations-v1/`) ; leurs copies versées et scellées sont sous
`docs/procedures/notations-T0.5-v1/`. **Chaîne** (treize scripts, liste `CHAINE` du scellement) :
`construire_pilote_jouet_v1.py`, `verifications_notations_v1.py`, `controles_avant_depense_notations_v1.sh`,
`lancer_notations_v1.sh`, `sceller_notations_v1.sh`, `surveiller_notations_v1.sh`, `recuperation_notations_v1.sh`,
`repetition_jouet_notations_v1.sh`, `repetition_finale_notations_v1.sh`, `essais_lanceur_notations_v1.sh`,
`essais_controles_notations_v1.sh`, `essais_scellement_notations_v1.sh`, `essais_surveillance_notations_v1.sh`.
**Chaîne figée après C** : aucun script de la chaîne ne change après le commit des préalables C ; toute correction
fait un nouveau C, et les bancs, la répétition jouet et la répétition finale sont rejoués. Après S, toute correction est
un écart au préenregistrement scellé (nœud). **Jamais** de `vastai show instance <id> --raw` ni de
`vastai show instances --raw` sans filtre : forme filtrée seulement, champs nommés.

0. **Préalables**, dans cet ordre :
   1. décision de Lazar consignée : `GO-2026-10-12-02` (type « revendication », Lazar, N-021, option (a)) ; colonne
      d'état de N-021 exactement « tranché (a) par Lazar : GO-2026-10-12-02 (R-160) » ; ligne R-160 ;
   2. contre-lecture R2 du brouillon du préenregistrement, du code et de la chaîne (sous-agents neufs, fichiers donnés
      explicitement) ; rapports versés sous `prereg/contre-lectures/T0.5-notations-v1-relecture-…-v1.(md|json|tar)` (texte et code, chaîne, scripts, traitement), scellés,
      cités par le candidat ; corrections ; candidat relu (`brouillons/T0.5-pilote-notations-v1-candidat<k>.md`) et
      configuration relue versés, scellés ; commit du code relu (`CODE_RELU`), suite complète comptée à ce commit ;
   3. vérification courte, par des sous-agents neufs, du candidat, du différentiel du code (`a859045` → `CODE_RELU`)
      et de la chaîne (versée avec ses empreintes, face au candidat), en tours successifs : chaque tour relit le
      traitement du tour précédent (différentiels du texte, du code et de la chaîne), jusqu'à un tour dont les constats
      ne changent plus rien ou ne changent que des points de forme, relus par la session ; son rapport (tous les tours
      et leur traitement) est versé et scellé sous
      `docs/procedures/notations-T0.5-v1/verification-courte-candidat-v1.md`, hors de la famille des rapports cités (le
      candidat ne peut pas citer le rapport qui porte sur son texte final) ; un constat qui change le texte fait un
      candidat nouveau, et l'étape 2 reprend pour ce qui change ;
   4. **répétition jouet** (`repetition_jouet_notations_v1.sh <CODE_RELU> <candidat relu> <racine neuve>`) : quatre
      passages (sain, code 0 ; branche présente, code 2 ; premier lancement manqué, code 1 ; relancement, code 0) ;
      récupérations conformes : premier lancement, relance, arrêt synthétique pendant le deuxième juge (code 0) ;
      récupération des traces seules sur la branche sans run (code 4) ; sept artefacts refusés, chacun à son seul KO
      (relance après notations : 0 ; notations manquantes : 4c ; ajout dans le dossier du pilote : 1c ; ligne de fin de
      juge absente du journal : 6 ; dernier lot dans les traces du premier lancement : 0 ; notations rattachées à un autre run : 2b ; dernier lot dans le seul `run.err` des traces du premier lancement : 0) ; journal versé, scellé ;
   5. épingles écrites dans `controles_avant_depense_notations_v1.sh`, toutes ensemble : candidat, configuration,
      rapports, `CODE_RELU`, journal de la répétition jouet (`REPETITION_JOUET`) ; copies versées et scellées sous
      `docs/procedures/notations-T0.5-v1/` : les treize scripts et ce plan ; commit **C1**, poussé ;
   6. au commit C1, **bancs** (un cas sain et un artefact par garde nouvelle ; chacun écrit « script éprouvé : <script>
      <sha256> » pour chaque script qu'il éprouve, copies versées à C1) : lanceur, surveillance, contrôles avant dépense
      (suite et tokeniseurs remplacés par des bouchons, joués en vrai par la répétition finale), scellement ; puis
      **répétition finale à blanc** (scellement puis contrôles, clone jetable de C1) : conforme. Journaux versés sous
      `docs/procedures/notations-T0.5-v1/` (`banc-lanceur-notations-v1.log`, `banc-surveillance-notations-v1.log`,
      `banc-controles-notations-v1.log`, `banc-scellement-notations-v1.log`, `repetition-finale-notations-v1.log`) et
      scellés : commit **C2**, qui n'ajoute que ces journaux et leurs sceaux (`git diff --name-only C1 C2` vérifié) ; le
      lanceur exige, au commit de scellement, les cinq journaux, leur verdict conforme et chaque script éprouvé égal à sa
      copie versée (preuves des essais). Chaque journal versé est la sortie brute du banc ou de la répétition, redirigée
      dans un fichier neuf (aucune enveloppe, `time` ou code ajouté : sa dernière ligne est le verdict). **Avant le
      scellement**, au commit C2, la même lecture que le lanceur : `python3 -I verifications_notations_v1.py preuves
      <dossier des cinq journaux versés>`, code 0, et chaque ligne « <script> <sha256> » de sa sortie égale à la copie
      versée à C2 ; sortie consignée dans la ligne R-… des préalables (un journal refusé se découvre avant S, non à la
      création) ;
   7. registres : `registres/decisions.md` (ligne R-… des préalables : C1, C2, épingles, bancs, répétitions),
      `registres/etat.md` ; tout poussé.
1. **Scellement** : `sceller_notations_v1.sh` (sans argument) : un seul commit S qui n'ajoute que le préenregistrement,
   la configuration et leurs sceaux, poussé, relu sur le dépôt distant.
2. **Contrôles avant dépense** : `controles_avant_depense_notations_v1.sh S <dossier neuf>` (le lanceur les rejoue),
   suite complète des tests au commit S comprise (environ 24 minutes pour la suite au code relu dans la session de
   pilotage, sans autre calcul en parallèle ; journal versé sous `brouillons/T0.5-notations-suite-<commit>-v1.txt`).
3. **Dépense cumulée** : relire le cumul de la phase 0 dans `registres/depenses.md` ; si cumul + engagement de l'étape
   (10,5 USD) atteint l'alerte de 120 USD de GO-2026-10-04-08, aucun lancement (nœud). Cumul et engagement écrits dans
   `registres/depenses.md` avant la création. **Offre et crédit** : A100 SXM4 sur AMD EPYC 7513 seulement (même filtre que le pilote), prix ≤ 1,30 USD de l'heure ;
   crédit ≥ 7,5 h × (prix + autres projets en marche) + 1,2 USD ; sinon code 3 : demande de recharge à Lazar, avec le
   montant exigé et le crédit lu, aucune création avant. Pas de création entre 23:30 et 00:00 UTC. **Autres projets** :
   la liste passée au lanceur est celle des instances en marche relevées juste avant, en forme filtrée ; seules les
   instances connues d'autres projets de Lazar y entrent (55505836, 55555587) ; toute autre instance inconnue en marche
   est un nœud (question à Lazar), jamais arrêtée par la session.
4. **Création** : `bash <bloc-notes>/lancer_notations_v1.sh <offre> <traces neuves> <autres projets>` en un seul appel,
   aucun sous-agent en cours. Le lanceur exige les treize scripts du bloc-notes égaux à leurs copies versées à S, et les
   preuves des essais (cinq journaux, préalable 6). **Avant** : identifiant prévu et heure dans `registres/etat.md`, engagement dans
   `registres/depenses.md`. Le lanceur écrit dans `<traces>/lancement.txt` la création (secondes depuis l'époque) et le
   plafond de la surveillance (création + 26 400 s).
   Le lanceur écrit aussi la dépense maximale d'un premier lancement qui permettrait encore un relancement à ce prix
   (10,5 − 0,5 − 7,5 × prix USD ; au prix de 1,30 USD : 0,25 USD, soit une panne des premières minutes seulement).
   **4 bis** : entre 3 et 5 minutes après la création, `vastai logs <id> --tail 200`, masqué, dans
   `<traces>/journal-5min.txt` : « AMORCE <date> : commit <S> », « début : ETUDE=notations MODE=reel COMMIT=<S>
   BRANCHE=calcul/t05-notations-reel-v1 » (relancement : `…-v2`), « préenregistrement lu : <N> tests attendus » (N du
   texte scellé), la carte et « branche … poussée avant l'installation ». Sinon : arrêt par identifiant (R10), nœud.
5. **Surveillance** : en arrière-plan, `PATH=<dossier de vastai>:/usr/bin:/bin INTERVALLE=120 bash
   <bloc-notes>/surveiller_notations_v1.sh <id> <création> <traces>/surveillance-<k>` (k = 1, 2, …, dossier neuf à
   chaque fois, R12). Une tâche d'arrière-plan de la session dure au plus deux heures : si elle s'achève sans ligne de
   motif (FIN, ÉCHEC D'AMORCE, REDÉMARRAGE, ÉTAT TERMINAL, PLAFOND), la surveillance est réarmée aussitôt avec k + 1.
   Code 2 (outil introuvable, dossier existant, usage) : corrigé et réarmé dans les dix minutes, sinon arrêt de
   l'instance par identifiant (une instance sans surveillance ne reste pas en marche). Rappel `send_later` au plafond
   + 10 minutes. **Relevé cumulatif du lancement** : la réunion, dans l'ordre de k, des `progres.txt` de ses dossiers
   de surveillance, écrite dans un fichier neuf `<traces>/releve-cumulatif.txt` à la sortie, puis versée dans le dépôt
   à un seul emplacement, `traces/t05-notations-releve-<identifiant de l'instance>/releve-cumulatif.txt`, avec son sceau
   `releve-cumulatif.txt.sha256`, committée et poussée avant toute ligne R-… qui en dépend (préenregistrement, « Fini,
   établi sur les pièces » ; le lanceur, en relance, ne lit le relevé qu'à cet emplacement). Lignes de progression
   lues pour la conduite du run seulement (débit, échéances) et pour établir qu'un juge a fini (ligne `fin=`) : aucune
   décision n'en dépend hors des règles gelées. La ligne « run terminé » du journal ne nomme que le run (le résumé,
   comptes compris, reste dans `run.json`, versé aux traces).
6. **Traces de la session** : `lancement.txt`, `offre.json`, `controles.txt`, `journal-5min.txt` et les dossiers de la
   surveillance (le relevé cumulatif, lui, à son seul emplacement, étape 5) sont copiés sous
   `traces/t05-notations-v1-<date>/` du dépôt, avec `empreintes.sha256`, committés et
   poussés avant toute décision de relancement et avant la ligne de dépense (R6).
   **Sortie** : chaque motif de sortie de la surveillance (FIN, ÉCHEC D'AMORCE, REDÉMARRAGE, ÉTAT TERMINAL, PLAFOND)
   appelle l'arrêt immédiat de l'instance par son identifiant (`vastai stop instance <id>`, R10) ; état relu (forme
   filtrée) ; `registres/arrets.md` ; dépense consignée dans `registres/depenses.md`.
7. **Relancement** (unique) selon le préenregistrement (Critères de lecture gelés, Préséance, Causes d'un arrêt,
   Relancement), seulement si tout ce qui suit est établi sur les pièces : cause d'infrastructure après la poussée
   initiale ; aucun juge fini (ni fichier de notations, ni résumé, ni ligne `fin=` ou de dernier lot `lot=n/n` au relevé
   cumulatif ou dans les traces poussées, ni arrêt consigné d'un statut autre que « en cours ») ; dépense engagée
   + 7,5 h × prix de l'offre + 0,5 USD ≤ 10,5 USD (plafond de GO-2026-10-12-02) ; alerte à 120 USD non atteinte ;
   crédit suffisant (règle du lanceur). La règle qui fait foi est celle du préenregistrement (« Relancement ») ; ce plan
   la recopie. Ligne `| R-NNN | …` du registre des décisions, avant l'appel,
   qui cite la cause, l'étape et le motif, contient les mots « relancement », « notations » et « infrastructure »,
   nomme une seule fois l'instance du premier lancement sous la forme « instance NNNNNNNN » (huit chiffres) et porte une
   seule fois « dépense engagée X,XX USD » ; puis
   `bash <bloc-notes>/lancer_notations_v1.sh <offre> <traces neuves> <autres projets> relance R-NNN
   <traces du premier lancement>/releve-cumulatif.txt` (le lanceur exige que ce fichier soit égal à la copie versée et
   scellée à HEAD sous `traces/t05-notations-releve-<instance du premier lancement>/`, qu'il porte la ligne « AMORCE … :
   commit » du commit de scellement et aucune ligne `fin=` ni de dernier lot `lot=n/n` ; les contrôles rejouent la
   préséance sur la branche `-v1`, journal et `run.err` des traces compris). Sinon :
   nœud, demande de GO à
   Lazar.
8. **Récupération** : `recuperation_notations_v1.sh S <dossier neuf> [relance]` ; code 0 : fusion de la branche de
   résultats dans `main` (commit de fusion), poussée, ligne R-… ; code 4 (traces seules, aucun run) : traces lues pour
   qualifier la cause de l'arrêt (étape 7) ; code 1 : instance gardée, nœud. **Résultats écrits mais non poussés**
   (journal « poussée … impossible », branche absente, ou run absent de la branche alors que la surveillance a relevé
   une ligne `fin=`) : instance arrêtée et gardée, jamais détruite ; reprise depuis l'instance = nœud (devis :
   redémarrage, poussée depuis l'instance, arrêt), demande de GO à Lazar. Aucune proposition de destruction de
   l'instance avant une récupération conforme. Après la récupération conforme et la fusion, la destruction de l'instance
   est proposée à Lazar dans le même message (sauf juge écrit mais non poussé) ; tant qu'elle est gardée, son disque est
   consigné chaque jour dans `registres/depenses.md`, dans la dépense de l'étape.
9. **Lecture** : `lire_notations_pilote` avec `--prereg prereg/T0.5-pilote-notations-v1.md` (run de lecture distinct),
   audit R4 si déclenché, puis verdict R13 complémentaire par un sous-agent neuf, scellé, soumis à Lazar ; dépense
   consignée.

**Registres, dans l'ordre** : avant la création, `registres/etat.md` (identifiant prévu, heure) et
`registres/depenses.md` (engagement) ; à l'arrêt, `registres/arrets.md` (identifiant, motif, heure) et
`registres/depenses.md` (dépense lue) ; relancement, récupération, fusion et lecture : une ligne R-… chacun dans
`registres/decisions.md` ; puis `registres/etat.md` et la passation scellée (R14).

Réserves : jeton GitHub de l'instance non éprouvable depuis la session ; débit des juges jamais mesuré ; mise en place
estimée (environ 1 120 à 1 250 s depuis « AMORCE », sous le seuil de 1 500 s ; préenregistrement, « Mise en place »),
non mesurée sur l'instance ; le relancement et l'arrêt en cours de
juge n'ont été éprouvés qu'en répétition jouet (l'arrêt, sur une branche fabriquée) ; la répétition jouet réutilise un
environnement neuf existant ; la vérification du GO repose sur le texte des registres ; une offre conforme peut se
faire attendre ; l'instance d'un autre projet de Lazar en marche (55555587 à 15:05 UTC, 3,98 USD de l'heure) porterait
le crédit exigé à 7,5 × (1,30 + 3,98) + 1,2 ≈ 40,8 USD au prix plafond (≈ 10,95 USD sans elle).
