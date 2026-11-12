# Contre-lecture 1 (R2) de l'addendum 1 « gardes des analyses » (relance v4 de R1) et du code v6, v7, v4 — v1

- Contre-lecteur neuf (sous-agent, Claude Opus 5.5), 5 novembre 2026, 17:05 → 17:13 UTC (`date -u`), sur la consigne
  `docs/notes/runs-r1-r2-r4-v1/etape-F-v1/consigne-contre-lecture-addendum-gardes-v1.md`. Je n'ai écrit ni les analyses,
  ni leur code, ni l'addendum v4 de R1, ni la fiche v4, ni l'addendum relu. Aucune donnée de R1 v4 lue (rien sous
  `diag/`, `donnees/` de la relance ; `origin/calcul/r1-r2-reel-v1` jamais ouverte, seule la date de sa tête relevée) ;
  aucun commit, aucun `.sha256`, aucun réseau, aucune dépense.
- Pièces relues (canal `/home/claude/controle-ia-travail`, `canal/conv-audit-n04`, tête `c82dafeb`) : brouillon 1
  `5d3ab56c…e3d245` et rapport `879d2e93…3cbe8` (empreintes recalculées, égales) ; code et essais neufs (empreintes
  égales à celles du rapport et de l'addendum) ; différentiels hors renommage ; addendum v4 de R1 (`git show
  origin/prep/r1-relance-v4:…`, `0f10881b…` recalculé) ; fiche v4 (`605931f3…` recalculé), sections 3, 4 et 6, et
  `verifier_reception_r1_v4_v1.py` (gardes `texte`, `table-comparee`, `provenance`) ; les trois textes scellés
  (compagnons vérifiés : OK), règles « premier passage » et « second passage ».

## Verdict

1. Non scellable en l'état.
2. Scellable après : corrections de code K1 et K2 (ci-dessous), listes fermées et empreintes de constantes regénérées,
   les 15 couples de `couples-contre-lecture-addendum-gardes-v1.json` appliqués.
3. Puis accord de Lazar sur l'écart déclaré (second passage, point 6), borné comme le disent C10 à C15.

## Points (gravité : bloquant / à corriger / note)

1. Gardes contre l'addendum v4 (question 1) — **note, conforme** : `texte` (égalité de `preenregistrement` à
   `{chemin, sha256}` de l'addendum v4), `table-comparee` (`tokenisation.table_sha256` = sceau de la table versée **et**
   `resultat_reparation_sha256` = sceau du résultat de la réparation versé), `provenance` (`tokenisation.addendum` à
   l'identique, commande `rejeu_activations_v4`) sont exactement celles du paragraphe « Analyses (inchangées) » et de la
   fiche v4 (section 6) et comparent les mêmes valeurs que le script de réception ; les deux `entrees_v4.py` sont
   identiques hors du nom du module de constantes et de l'import de `lire_json`.
2. Rien d'autre ne change dans les lectures (question 1) — **note, conforme** : différentiels de `analyser` relus
   (v2→v6, v5→v7, v3→v4) : seuls s'ajoutent `exiger_texte`, la liste fermée lue dans le bloc de l'addendum, la garde de
   passage neuve, l'appel aux gardes, `config["addendum"]`, `reception_v4`, `lien.addendum` ; calcul, issue et rendu
   repris par référence (`lecture_v1.calculer`, `lecture_v2.issue`, `lecture_v5.*`, `lecture_v3.issue_v3`,
   `rendu_v3.rendre_v3`) ; graines : même règle Q9 sur l'empreinte du texte passé à `--prereg`, inchangé → mêmes graines
   que la course v3 ; plis de la lecture par épisode : entropie de `8e267952…`, inchangée.
3. Liste fermée du code (question 2) — **note, exacte** : rejoué `exiger_code_cite` des trois versions neuves sur le
   brouillon 1 (22, 33, 31 fichiers, constantes `6ab768f6…`, `d35cdfab…`, `47c988e6…` égales) ; chaque empreinte citée
   égale au disque ; listes des versions précédentes toujours vérifiées sur les textes (18, 26, 27) ;
   `prereg.problemes` : les deux lignes attendues d'un brouillon 1. Les corrections K1 et K2 changeront six empreintes et
   les trois empreintes de constantes : regénérer (rapport, section 6).
4. « Inchangés, dits tels quels » (question 2) — **à corriger** (C1, C13) : hypothèses, prédictions, métriques, seuils et
   critères gelés sont bien dits inchangés tels quels ; les **listes d'arrêt ne le sont pas** : la règle « second
   passage » des trois textes (principale l. 101 et 172, secondaire l. 140 et 204, par épisode l. 62 et 138) est remplacée,
   alors que « Objet » et « Liste d'arrêt » disent « inchangées ». Le dire là où c'est écrit.
5. Second passage (question 3) — **bloquant, nœud de Lazar** : oui, c'est un écart à des listes d'arrêt scellées (les
   textes ne permettent un second passage que pour une cause technique, « mêmes graines, même code » ; la secondaire dit
   qu'une fiche lancée « épuise ce texte ») ; il est déclaré, mais **le code ne le borne pas** : la tolérance est ouverte
   (tout manifeste qui cite le texte sans l'addendum est « antérieur », tout manifeste sous l'addendum d'une autre
   commande est « autre ») ; un quatrième passage sous `lecture_v2`, ou un passage sous un futur addendum, passeraient.
   Correction K2 et couples C10, C11, C14, C15 : liste fermée des trois manifestes de la course v3 (seuls cités dans
   `runs/`, vérifié : `0587c398…`, `79f2a758…`, `91f711c6…`) et des trois commandes gelées.
6. Lisibilité et borne (question 3) — **à corriger** (C3, C12) : écrire le statut des deux courses (les sorties v3, lues
   et jugées, R-1322, restent et sont rapportées ; la v4 est la lecture qui compte, fixée avant les données, jamais choisie
   sur ses résultats ; aucune n'efface l'autre) et « une seule lecture sous R1 v4, jamais une troisième, sous aucun
   addendum » ; la phrase actuelle (« un troisième passage exigerait un addendum nouveau ») ouvre la porte au lieu de la
   fermer. Dire aussi que la course v4 n'est pas aveugle à la v3 (seule liberté, la graine, fixée par les textes).
7. Place des gardes — **à corriger** (K1, C8, C9) : elles tournent après `charger_p3` et `charger_r1` (resp.
   `charger_activations_v3`), qui ouvrent les trois `.npz` et lisent `verdict_fidelite` ; rien n'est écrit si elles
   s'arrêtent, mais « rien n'est lu » n'est vrai qu'à moitié. Elles ne dépendent que du chemin du résultat cité par la
   fiche : les appeler juste après `lire_fiche`, avant tout chargeur.
8. Essais (question 4) — **note, conformes** : rejoués, 11 réussis sur 11 (117 s, commande de la consigne) ; chaque garde a
   un cas sain et des artefacts (addendum v3 jouet ; même chemin autre empreinte ; `table_sha256` ≠ ; table qui cite
   une autre réparation ; compagnon absent ; `tokenisation.addendum` ≠ ; commande v3 ; clé `tokenisation` absente) ;
   formats égaux aux attendus de la fiche v4 (4.1 et 4.4 : `preenregistrement` écrit par `creer_manifeste`, chemin relatif
   et empreinte ; `commande` ; `resultat.tokenisation.{table_sha256, addendum}` ; table à `resultat_reparation_sha256`
   au premier niveau, 4.3). K1 et K2 demandent des essais neufs (garde qui s'arrête sans `.npz` ouvert ; quatrième
   manifeste qui cite le texte ; manifeste de la course v3 altéré ; commande inconnue sous l'addendum).
9. Commit cité (question 5) — **à corriger** (C5) : `c82dafeb` porte déjà le brouillon 1 et le code ; le Plan (0.a)
   appelle commit cité « le premier commit de l'étape » ; dire que c'est celui du brouillon final.
10. Lecture entre les commandes décisives (question 5) — **à corriger** (C7) : chaque commande imprime l'issue sur la
    sortie standard (après scellement de ses sorties) ; l'opérateur verrait l'issue de la principale avant de lancer les
    deux autres. Rediriger vers un journal non affiché, seul le code de fin lu, journal scellé ; aucune issue lue avant les
    trois sorties committées et poussées.
11. Récupération (question 5) — **à corriger** (C2, C4) : `origin/calcul/r1-r2-reel-v1` (tête du 5 novembre, 02:36 UTC)
    et `origin/calcul/r1-v4-reparation-reel-v1` sont déjà dans le dépôt du canal ; « sans récupérer » et « avant toute
    récupération » sont inexacts : écrire « aucune extraction ni lecture avant le scellement ». Le reste de la section 5
    (refspec seule, `checkout` des seuls chemins, `.npz` hors index, témoin et `traces/` non extraits) ne lit rien de
    plus que ce que prévoient les textes.
12. Préalable de réception (question 6) — **à corriger** (C6) : le Plan ne pose pas comme condition la réception v4
    conforme (script en code 0, recalcul de la table égal à l'octet) ni sa consignation avec ce qui a été vu.
13. Nom du run de la réparation (question 6) — **note** : `20261104-234729-r1-v4-reparation-reel` est le seul nom de
    réparation v4 cité huit fois par les registres de `main` (deux autres noms de la même forme y figurent une fois chacun, non examinés) ;
    à revérifier sur le message de versement au `checkout` (un autre nom arrête, à bon droit).
14. Lecture par épisode (question 6) — **note** (K3, facultatif) : `lire_principale` exige la même fiche et le lien au
    texte, ce qui exclut la sortie de la course v3 ; exiger en plus `version` = code v6, `lien.addendum.sha256` = addendum
    et `reception_v4.run_rejeu` égal.
15. Arrêt technique après le manifeste — **note** (dans C12) : le code refuse tout second passage sous l'addendum ; la règle
    « mêmes graines, même code » des textes n'est donc exécutable que par une version neuve : nœud, dit d'avance.
16. Critères 3 et 4 de G0 — **note** : rien d'autre de bloquant trouvé ; le verdict R13 doit lire `reception_v4` et
    `passages` (Plan, point 8, déjà écrit) et la liste fermée des passages tolérés (K2).

## Corrections de code (liste à part ; versions neuves, R12 : le code `c82dafeb` n'est pas modifié en place)

- **K1** (`lecture_v6`, `lecture_v7`, `analyse_blanche_noire.lecture_v4`) : appeler `exiger_reception_v4` juste après
  `lire_fiche` / `lire_fiche_v3` (si R1 livré), avant `charger_p3`, `longueurs_textes`, `charger_r1`, `charger_run_v3`,
  `charger_activations_v3` ; essai : garde qui s'arrête sans aucun `.npz` ouvert (`numpy.load` remplacé par un piège).
- **K2** (`exiger_premier_passage_sous`, `exiger_premier_passage_v4`) : constantes gelées `PASSAGES_V3 = {run :
  empreinte du manifeste}` pour `20261103-072723-analyse-principale-r1-r2-v1` (`0587c398cc05f279251bbe747c3deaff1dee29cb191c94ce30090ce50a5e4643`),
  `20261103-072805-analyse-par-episode-v1` (`79f2a758e0c36f1d4aaa54a78e039ffc802074fe03e222120aff81a78f1a2083`),
  `20261103-072840-analyse-blanche-noire-v3` (`91f711c6eb903ca470b972a953ac12cdde31f211412a5629725895537d550adf`)
  et `COMMANDES_ADDENDUM` = les trois commandes des versions neuves (recopiées dans `analyse_blanche_noire.constantes_v4`) ;
  règle : manifeste illisible qui cite texte ou addendum → arrêt ; cite l'addendum → commande propre : arrêt, commande
  sœur gelée : toléré, autre : arrêt ; cite le texte (chemin ou empreinte dans ses octets, règle des textes) sans
  l'addendum → toléré seulement si son run est dans `PASSAGES_V3` avec la même empreinte, sinon arrêt ; écrire les noms
  tolérés dans `passages`.
- **K3** (facultatif, `lecture_v7`) : dans le mode décisif, exiger que le résultat de la principale porte `version` =
  `constantes_v6.VERSION`, `lien_au_preenregistrement.addendum.sha256` = empreinte de l'addendum et le même
  `reception_v4.run_rejeu`.
