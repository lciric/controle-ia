# Plan de la voie « notations seules » (pilote de T0.5, juges 8B et 3B)

## En tête : la voie retenue et l'écart à soumettre

**Aucune voie n'est sans écart.** Le texte scellé (`prereg/T0.5-pilote-8B-v1.md`, l. 160-174) prévoit un seul run d'analyse, qui lit avec le code cité (`2660b07`) et ne cherche les notations que dans `diag/20261012-105125-t05-pilote-reel/`, par `charger_pilote`. Des notations produites par un autre run ne peuvent donc pas être lues sans un écart de procédure. Cet écart est un nœud : Lazar le tranche avant le scellement. Aucun module gelé (`MODULES_LECTURE`) n'est touché par la voie recommandée.

**Voie recommandée, la plus simple qui respecte le gel des modules de lecture :**
1. **Un run neuf, R′.** Un module neuf, `noter_pilote_a.py`, écrit `notations-8B-decisives.json` puis `notations-3B-decisives.json` dans `diag/R′/`. Il travaille sur l'`episodes.json` scellé du pilote (`45616303…`), avec les paramètres du pilote et les mêmes graines (entropie du manifeste `8c3d7985…`, clés `juge-<juge>/<épisode>/passe-<p>`).
2. **Une lecture par un module neuf et mince, `lire_notations_pilote.py`.** Il n'ajoute aucun calcul. Il appelle sans les modifier les fonctions gelées : `charger_pilote` (pour le pilote seul), `empreintes_des_ensembles`, `notes_alignees`, `lecture_juge`, `decomposition_complete` (sensibilité sur 100), `difference_appariee`, `declencheurs_audit` (partie des juges), `predictions` (on ne garde que P2 et P3), `tirer_relectures` (on ne garde que les réponses de juge) et `exiger_modules_cites`. Il utilise les graines d'analyse `analyse/bootstrap-parts-8B`, `…-3B`, `analyse/bootstrap-difference` et `analyse/audit`, issues de l'entropie citée. Il vérifie qu'elles sont égales à celles du manifeste de la première analyse. Rien n'est écrit dans le dossier du pilote. Le format et les familles ne sont pas relus.

**Écart minimal à soumettre (N-021) :** « Les notations décisives refaites sont lues hors de `charger_pilote`, par un module neuf qui n'appelle que les fonctions gelées au commit `2660b07`, sur les notations d'un run distinct. Son équivalence avec `analyser` est éprouvée par un test. »

**Autres voies, non recommandées :**
- **B2 : copier les notations et leurs sceaux dans le dossier du pilote, puis relancer `analyser`.** Cette voie n'écrit aucun code de lecture neuf, mais elle cumule quatre écarts :
  - deux runs mélangés dans le dossier du pilote ;
  - un second run d'analyse ;
  - un étiquetage repris hors des trois étapes ;
  - la suspension de la lecture qui revient (couverture des directions fécondes 0,930), et des relectures tirées de nouveau.

  Elle repose en plus sur un comportement non écrit de `verifier_resultat`, qui ne vérifie pas le dossier.
- **Modifier `charger_pilote` :** c'est une modification d'un module gelé. Écartée.

**Divergences entre les trois rapports, tranchées ici :**
- B2, recommandée par le rapport « lecture gelée », contre « rien n'est écrit dans le dossier du pilote », demandé par le rapport « texte et règles » : je retiens le module de lecture neuf.
- Fichier de notations partielles : je ne le retiens pas. Je retiens des compteurs et une ligne de progression par lot. Raison : un fichier partiel n'est pas lisible selon la règle « tout ou rien », et lui donner un statut ajouterait du texte.
- Un run par juge ou un run unique : je retiens **un run, une instance, une échéance par juge**.

## Étapes

**1. Proposition N-021 à Lazar (nœud : écart au préenregistrement scellé).** Durée : 1 à 2 heures.
- Fichiers : `docs/decisions/proposition-N-021-lecture-notations-v1.md` et son `.sha256`, `registres/decisions.md`, `registres/etat.md`.
- Contenu : l'écart ci-dessus, les deux autres voies, la recommandation, et le devis révisé (son plafond dépasse la fourchette de R-155).
- Aucun défaut sous 48 heures : on attend la réponse.
- En attendant, les étapes 2 à 5 avancent, car elles relèvent de la routine.

**2. Lanceur `src/controle_ia/environnements/noter_pilote_a.py` et `tests/test_noter_pilote_a.py` (routine).** Durée : 1 jour.

Gardes d'avant le manifeste :
- `verifier_resultat` sur l'`episodes.json` du pilote ; son empreinte doit être celle que cite le nouveau préenregistrement ; 180 fiches ;
- tâches égales à `arret.json` → `partiel.taches_sha256` ;
- paramètres des juges égaux à ceux du manifeste du pilote : `agent`, `juges`, `lot_juge`, `max_nouveaux_juge`, `temperature_juge`, `variante_juge`, `episodes_decisifs`, `episodes_notes_deux_fois`, `fils` ;
- refus si un fichier `notations-*-decisives.json` existe dans le dossier du pilote ;
- exactement 180 demandes par juge (60 A, 60 B, 60 C) ;
- citations du préenregistrement, `exiger_code_cite` ;
- graines de R′ égales à celles du pilote ;
- lots identiques au découpage d'origine (22 lots de 8 et 1 lot de 4).

Après le manifeste :
- déterminisme ;
- téléchargement des deux modèles (pour le 8B, le modèle se lit dans `config["agent"]`) ;
- contrôle du format des deux juges ;
- le 8B note, son fichier est écrit, il est libéré ;
- le 3B est chargé hors ligne, son format est recontrôlé, il note, son fichier est écrit ;
- `exiger_sans_signal`, puis le résumé.

Les nouveautés :
- **une échéance par juge**, contrôlée avant chaque lot, avec au plus un lot de dépassement ;
- **une ligne par lot dans `run.err`** : rang, durée, passes de décodage, lignes finies, aucun texte ;
- **les compteurs de lots faits dans `arret.json`**.

Tests, un cas sain et un artefact par garde (R5), sur le modèle de `tests/test_pilote_a.py` (l. 241-442 et 815-858) :
- bout en bout ;
- épisodes altérés ou rattachés à un autre manifeste ;
- paramètres différents ;
- notations déjà présentes ;
- autre entropie ;
- échéance pendant le 8B (aucun fichier, le 3B continue) et pendant le 3B (le fichier du 8B reste) ;
- échec du chargement du 3B, format hors ligne différent ;
- signal TERM converti, ou avalé ;
- bornes des échéances ;
- run réel sans préenregistrement.

**3. Lecteur `src/controle_ia/environnements/lire_notations_pilote.py` et ses tests (routine pour l'écriture ; son emploi dépend de N-021).** Durée : une demi-journée.
- Il écrit, sous son propre manifeste de lecture, `diag/<run de lecture>/lecture-juges.json`, scellé.
- Gardes :
  - `exiger_modules_cites` contre `2660b07` ;
  - ses propres modules (lecteur et lanceur) comparés au commit S′ ;
  - graines d'analyse égales au manifeste de `20261012-150724-t05-pilote-analyse` ;
  - P1 et P4 à P7 recalculés avec les valeurs scellées de la première `lecture.json`, et égaux à elles : sinon arrêt.
- Test clé : sur un pilote jouet complet, les sorties « juges », « différence appariée », « P2 » et « P3 » doivent être **égales à celles d'`analyser`**. Artefacts : une notation altérée, une graine différente, un module gelé modifié.

**4. Scripts d'instance (routine).** Durée : un quart de journée.
- Fichiers : `scripts/amorce_instance_t05.sh` et `scripts/pilote_t05_instance.sh`, avec `ETUDE=notations` ; tests dans `tests/test_script_instance_t05.py`.
- Le script de l'instance :
  - lit tôt « Chemin des épisodes » et son sceau ;
  - lance le nouveau lanceur ;
  - ne pousse aucun vecteur ;
  - utilise la branche `calcul/t05-notations-reel-v1`.
- Les bornes dépendent de l'étude : 400 minutes de délai externe et 430 minutes de plafond de l'amorce pour `notations`. Pour `pilote` et `revalidation`, elles ne changent pas, ce qu'un test vérifie.
- Une valeur d'ETUDE inconnue est refusée (test).
- Le nombre de tests attendu change : il était de 689 et la nouvelle valeur sera citée.

**5. Relecture R2 du code par un sous-agent neuf (routine).** Durée : un quart de journée. On lui donne le différentiel depuis `7be281f` et la liste explicite des fichiers. Corrections, puis vérification courte.

**6. Préenregistrement complémentaire (routine pour la rédaction, après la réponse de Lazar à N-021).** Durée : une demi-journée.
- Fichiers : `prereg/T0.5-pilote-notations-v1.md` et `prereg/T0.5-pilote-notations-config-v1.json`, avec leurs sceaux.
- Contenu (rapport « texte et règles », section 2, points 1 à 11) :
  - renvoi aux critères gelés (`9ce91ba1…`), sans aucun seuil nouveau ;
  - entrées citées par empreinte ;
  - configuration identique au pilote ;
  - graines reprises ;
  - échéances par juge ;
  - liste d'arrêt ;
  - table de lecture du nouveau run : un juge dont le fichier est écrit est lu ; un nouvel arrêt est un nœud, sans nouvelle tentative implicite ;
  - voie de lecture tranchée par N-021, nommée comme un écart ;
  - population des relectures : 360 notations décisives, aucune descriptive ;
  - transparence : tous les résultats du pilote sont connus, aucune notation de juge ne l'est ;
  - nombre de tests attendu.
- Tout changement de `lot_juge`, `max_nouveaux_juge`, de la température ou des révisions des juges serait un écart, donc un nœud. On n'en fait aucun.

**7. Contre-lecture R2 du préenregistrement (routine).** Durée : une demi-journée. Elle est faite par un sous-agent neuf, avec les fichiers donnés explicitement. Fichiers : `prereg/contre-lectures/…`, corrections, puis vérification courte.

**8. Procédures déclinées de celles du pilote, dans `docs/procedures/notations-T0.5-v1/` (routine).** Durée : trois quarts de journée.
- Scripts :
  - `plan-lancement-notations-v1.md`
  - `controles_avant_depense_notations_v1.sh`
  - `lancer_notations_v1.sh`
  - `recuperation_notations_v1.sh`
  - `sceller_notations_v1.sh`
  - `essais_*_notations_v1.sh` et les journaux des bancs
- Ce qu'on garde et ce qu'on remplace suit la section 4 du rapport « chaîne d'instance ».
- Gardes nouvelles, chacune éprouvée sur un cas sain et sur un artefact :
  - GO de N-020 et ligne de dépense ;
  - état du pilote constaté : `arret.json` à l'étape « notations décisives par 8B », aucun fichier de notation ;
  - empreinte des épisodes égale à la citation ;
  - graines égales ;
  - `duree_max` par juge recalculée ;
  - `ETUDE=notations` ;
  - à la récupération : deux fichiers de 180 notations, alignés sur `ensemble_sha256` recalculé depuis l'`episodes.json` du pilote, et **aucun ajout dans le dossier du pilote** ;
  - instance 55538944 tolérée si elle existe encore ;
  - relancement interdit dès qu'un fichier de notations est sur la branche `-v1`.

**9. Scellement de S′ (routine).** Durée : 1 à 2 heures.
- `sceller_notations_v1.sh` : préenregistrement, configuration, code, procédures, sceaux, `verifier-arbre`, suite complète au commit S′.
- Aucune entropie nouvelle n'est tirée, puisque celle du pilote est reprise.
- Commit, puis poussée vers `controle-ia-travail`.

**10. Répétitions (routine).** Durée : 2 à 3 heures.
- Répétition jouet : quatre passages et récupérations, plus deux artefacts (épisodes altérés, notation manquante).
- Répétition finale : contrôles avant dépense sur S′, tous conformes.
- Les journaux sont scellés.

**11. Devis et demande de GO de dépense (nœud).** Durée : une demi-heure, puis attente.
- Message à Lazar au format de décision, avec le devis ci-dessous.
- `registres/go.md` (`GO-2026-10-NN-NN`), `registres/depenses.md` (engagement), `etat.md`.

**12. Lancement, après le GO (routine encadrée par le GO).** Durée : une demi-heure.
- `lancer_notations_v1.sh` avec `GO_ID` ; la garde de calcul est active.
- Contrôle à 5 minutes.
- La dépense est consignée dans `depenses.md`.

**13. Surveillance (routine).** Environ 4,5 heures de calendrier, au plus 7,3 heures.
- Surveillance en tâche de fond, avec un plafond à la création plus 26 400 s.
- On ne lit que les lignes de progression : rangs, durées, comptes, aucun texte.
- Tout dépassement du plafond donne un arrêt par l'identifiant de l'instance (R10), consigné dans `registres/arrets.md`.

**14. Récupération (routine).** Durée : 1 heure.
- `recuperation_notations_v1.sh`, fusion de la branche, sceaux vérifiés.
- Arrêt de l'instance par son identifiant dès que la poussée est constatée (R10), consigné dans `arrets.md` et `depenses.md`.
- Un nouvel arrêt pendant un juge est un nœud.

**15. Lecture par le code gelé (routine).** Durée : 1 à 2 heures.
- `lire_notations_pilote.py` au commit S′, puis `lecture-juges.json` scellé et committé.
- Si un déclencheur propre aux juges joue (« trop propre » ou « trop sale »), l'audit de symétrie R4 suit avant le verdict : relecture des 10 réponses de juge tirées par graine, par des sous-agents neufs, et recalcul indépendant. Durée : une demi-journée.

**16. Verdict R13 complémentaire.** Durée : une demi-journée.
- Fichier : `docs/verdicts/verdict-T0.5-pilote-notations-v1.md`, par un auteur neuf (et des sceptiques neufs, selon le précédent). Il est scellé ; le verdict v1 n'est jamais réécrit.
- Il est soumis à Lazar (nœud) : plan B ou rubrique gardée pour chaque juge, P2, P3, et l'usage des juges par T0.6 et T0.8.

**17. Passation à chaque fin de session (routine).** Fichiers : `registres/passations/…`, `etat.md`, commit, poussée.

**Durée de travail de session :** environ 3,5 à 4,5 jours avant la demande de GO, puis environ 1,5 jour du lancement au verdict. Cela laisse de la marge avant la fin de M0 (1er novembre).

## Devis

| poste | base | durée |
|---|---|---|
| mise en place (création → début du run, tests compris) | mesurée au pilote : 972 s | ≈ 970 s |
| téléchargements, chargements, formats des deux juges | 8B 128 s et 3B 48,7 s mesurés ; chargement hors ligne du 3B non mesuré | ≈ 300 s |
| notations du 8B (180, 23 lots) | plus de 7 565 s (borne basse) ; 7 900 s si 22 lots étaient faits, 9 700 s si 18 | 7 900 à 9 700 s |
| notations du 3B | aucune mesure ; 0,4 à 1,0 fois le 8B | 3 200 à 9 700 s |
| fin, scellement, poussées | estimation | ≈ 200 s |

- **Durée attendue :** environ 16 200 s, soit **environ 4,5 heures de carte**. Fourchette : 3,5 à 6,1 heures.
- **Échéances internes proposées :**
  - 8B : **12 000 s**, soit 1,24 fois l'estimation haute et 1,52 fois la basse ;
  - 3B : **10 000 s** ;
  - chacune contrôlée avant chaque lot, avec au plus un lot de dépassement (environ 600 s).
- **Bornes de l'instance :**
  - délai externe du run : 400 minutes ;
  - plafond de l'amorce : 430 minutes ;
  - surveillance : création plus 26 400 s.
- **Plafond de durée**, les deux échéances atteintes plus les dépassements : environ 24 700 s, soit **6,85 heures**.
- **Coût :**
  - attendu : environ **4,9 USD** au prix du pilote (1,0889 USD de l'heure) ;
  - fourchette : 3,8 à 6,6 USD ;
  - plafond : 7,5 USD à ce prix, **8,9 USD** au prix maximal du filtre (1,30 USD de l'heure) ;
  - en plus : téléchargement et disque, moins de 0,5 USD.
- **GO demandé : plafond de 9 USD.** Ce plafond dépasse la fourchette de 3 à 6 USD de R-155 : à dire explicitement dans la demande.
- **Crédit minimum exigé par le lanceur :** 7,5 heures au prix de l'offre plus 1,2 USD, soit environ 9,4 USD à 1,0889 USD de l'heure.
- **Marge :** l'échéance du 8B couvre un pilote qui n'aurait fait que 15 lots sur 23. Celle du 3B est mince seulement dans l'hypothèse pessimiste où le 3B serait aussi lent que le 8B.

## Réserves

- **Débit jamais mesuré.** On ne connaît ni le débit des juges, ni le nombre de lots faits au pilote. Le chiffre de 7 565 s n'est qu'une borne basse.
- **Plan B possible pour le 8B.** Des lots d'au moins 344 s laissent penser que les réponses vont souvent jusqu'au plafond de 3 072 jetons. Le motif « plus de 20 % de réponses incomplètes » du plan B pourrait alors jouer. C'est une hypothèse, sans mesure. La lecture reste ouverte.
- **Une autre carte.** Avec les mêmes graines, les notations peuvent différer de ce qu'aurait produit le pilote. Rien n'en a été lu, donc aucun tirage n'est refait au sort (R3).
- **Si Lazar préfère B2**, les étapes 3 et 15 changent :
  - la copie dans le dossier du pilote se fait dans un commit à part, par la session ;
  - un second run d'analyse se fait sous `T0.5-pilote-8B-v1.md` ;
  - l'étiquetage est repris, et contrôlé par l'égalité de l'engagement, des empreintes des lots, des familles et des kappas ;
  - la suspension de la lecture et les relectures doivent être réglées d'avance.

Fichiers lus pour ce plan (aucun n'a été écrit, aucune commande Vast.ai lancée, aucun fichier interdit par D-20 ouvert) :
- `/home/user/controle-ia-travail/prereg/T0.5-pilote-8B-v1.md`
- `/home/user/controle-ia-travail/registres/decisions.md`
- `/home/user/controle-ia-travail/registres/etat.md`
- `/home/user/controle-ia-travail/src/controle_ia/environnements/lire_pilote.py`
- `/home/user/controle-ia-travail/scripts/amorce_instance_t05.sh`
- `/home/user/controle-ia-travail/scripts/pilote_t05_instance.sh`
- `/home/user/controle-ia-travail/docs/procedures/pilote-T0.5-v1/lancer_pilote_v2.sh`