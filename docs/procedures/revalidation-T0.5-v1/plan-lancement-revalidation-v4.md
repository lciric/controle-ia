# Plan de lancement de la revalidation (T0.5) — v4 (après les vérifications 1 à 4 du remplissage)

Commit du code cité : 3b8c049bec316272b4f65a0e51ef54a2c1e83217 (670 tests ; suite archivée dans la répétition jouet v5,
`T0.5-revalidation-repetition-jouet-v5.tar`, 903164d4…, « 670 passed in 475.09s »). Candidat vérifié : `candidat-6/`
(`remplir_revalidation_v4.py` ; empreinte, heure du scellement normalisée : 1977387f…).

**Jamais** de `vastai show instance <id> --raw` ni de `vastai show instances --raw` sans filtre : la réponse contient les
variables de l'instance, donc les jetons (vérification 4, Q-2). Toujours la forme filtrée :
`vastai show instance <id> --raw | python3 -c 'import json,sys; d=json.load(sys.stdin); print(d.get("actual_status"), d.get("cur_state"), d.get("status_msg"))'`.

1. **Scellement** (`sceller_revalidation_v2.sh`) : candidat régénéré à l'heure du scellement, comparé au candidat vérifié
   (identité, heure exceptée) ; rapports md et json des quatre vérifications et archives des répétitions v4 et v5 sous
   `prereg/contre-lectures/`, scellés ; préenregistrement et configuration sous `prereg/`, scellés ; registres
   (R-127 à R-129, état) ; un seul commit S ; poussée vers `lciric/controle-ia-travail`, `main`.
2. **Contrôles avant dépense** : `controles_avant_depense_v3.sh S <dossier neuf>` (le lanceur les rejoue).
3. **Offre et crédit.** L'offre conforme la moins chère, relevée juste avant (filtre du plan) ; prix ≤ 1,30 USD l'heure
   (devis), sinon nœud. Crédit ≥ 6 h × prix + 0,9 USD (préenregistrement, « Calcul »), sinon nœud : rien ne se crée,
   Lazar est prévenu.
4. **Création** : `lancer_revalidation_v3.sh <offre> <dossier de traces neuf>`, en un seul appel, aucun sous-agent en
   cours. Code 0 : identifiant dans `lancement.txt` ; code 3 : crédit ou prix, nœud ; code 4 : création douteuse,
   vérifier par `vastai show instances` (sans `--raw`). Consigner l'identifiant et l'heure dans `registres/etat.md`, la
   dépense dans `registres/depenses.md`, l'offre (`offre.json`) dans `traces/`, scellée.
   **4 bis (Q-1)** : entre 3 et 5 minutes après la création, `vastai logs <id> --tail 200`, masqué comme dans la
   surveillance, écrit dans `<traces>/journal-5min.txt` ; y trouver « AMORCE <date> : commit <S> » et, dès que la
   mise en place l'atteint, « branche calcul/t05-revalidation-reel-v1 poussée avant l'installation ». Sans la
   première ligne à 5 minutes, ou sur une ligne « AMORCE : … » d'échec : arrêt par identifiant (R10), consigné dans
   `registres/arrets.md`, nœud.
5. **Surveillance** : `PATH=<bloc-notes>/venv-vastai/bin:$PATH bash docs/procedures/surveiller-instance-t04-v1.sh
   <id> <CREATION> <dossier>` ; tâche de fond de 7 200 000 ms, relancée à l'identique à chaque sortie de l'outil sans
   motif ; plafond de 6 h depuis la création. Rappel `send_later` à la création + 6 h 10 min : vérifier l'instance
   (forme filtrée), l'arrêter par son identifiant si elle tourne encore.
6. **Sortie de la surveillance** : FIN (code 0, 1 ou 2) → arrêt immédiat par identifiant ; FIN au code 124 ou 137 →
   attendre les dernières lignes (« ----- …/journal.txt » ou « AMORCE : poussée impossible ») ou 60 s, relire, puis
   arrêter ; ÉCHEC D'AMORCE, REDÉMARRAGE, ÉTAT TERMINAL, PLAFOND → arrêt immédiat, journal archivé (masqué), nœud
   selon la procédure (section 5). Après l'arrêt : état relu « stopped » (forme filtrée), consigné dans
   `registres/arrets.md`.
7. **Récupération**, avant toute fusion, sur `git fetch origin calcul/t05-revalidation-reel-v1` (Q-10) :
   1. ascendance et contenu : `git merge-base --is-ancestor S FETCH_HEAD` ; `git diff --name-status S FETCH_HEAD` :
      seulement des ajouts sous `runs/<RUN>/`, `diag/<RUN>/` et `traces/t05-*/` ; un seul RUN
      `AAAAMMJJ-HHMMSS-t05-revalidation-reel` ; commits de « instance de calcul (T0.5) » ;
   2. sceaux, sur un clone propre : `verifier-arbre .` ; `verifier_resultat` sur chaque `diag/<RUN>/*.json` ;
      `sha256sum -c` dans chaque dossier de `traces/` ;
   3. manifeste : commit = S, préenregistrement et son empreinte, configuration 50930b37… (sans les quatre clés des
      tâches), entropie citée, versions de torch et de transformers, mode reel ;
   4. issue : exactement l'un de `resume.json` ou `arret.json` ; carte A100 ; mémoire de la carte ;
   5. journal : « 670 tests attendus », « poussée avant l'installation », « disponible True », « tests : 670 passed » ;
      journal de l'instance archivé, masqué, scellé, avec « AMORCE … fin, code N » ;
   6. aucune valeur de jeton dans le différentiel (recherche des valeurs, sans les afficher) ;
   puis fusion dans `main`, poussée.
8. **Fin** : dépense consignée ; destruction de l'instance arrêtée proposée à Lazar le jour même ; verdict par un
   sous-agent neuf (`lire_bras`, `choisir_noyau`, depuis les résultats scellés), scellé, soumis à Lazar.

Réserves déclarées : jeton de l'instance non éprouvable depuis la session (poussée initiale sur l'instance) ; garde de
calcul inactive dans cette session (rejouée par le lanceur) ; jetons dans les arguments du processus vastai pendant la
création (aucun sous-agent en cours) ; M-1 à M-3 de la vérification 3 (mineures, sans effet sur la règle) reportées
après le run ; K-6 (lanceur de T0.4).
