# Plan de lancement de la revalidation (T0.5) — v7 : préenregistrement v2 (N-018)

Depuis le plan v4 (`docs/procedures/revalidation-T0.5-v1/plan-lancement-revalidation-v4.md`), après l'échec de la v1 aux
tests sur l'instance 55292763 (R-132, R-134), la relecture R2 du candidat 2 de la v2 (R-135), la vérification de ses
corrections (R-136) et le contrôle mécanique des dernières corrections (R-137). Les plans v5 et v6, jamais versés, sont
remplacés par celui-ci. Ce qui change par rapport au plan v4 : le
préenregistrement (v2), passé au script de l'instance par `PREREG`, et la branche de résultats
`calcul/t05-revalidation-reel-v2`, passée par `BRANCHE` ; les scripts (générateur `remplir_revalidation_v2_r4.py`,
scellement `sceller_revalidation_v5.sh`, contrôles `controles_avant_depense_v7.sh`, lanceur
`lancer_revalidation_v7.sh`, récupération `recuperation_revalidation_v2.sh`) et leurs bancs (`essais_controles_v7.sh`,
`essais_lanceur_v7.sh`, `essais_scellement_v5b.sh` ; le banc 1 du scellement, `essais_scellement_v5.sh`, versait les
copies des scripts sans leur sceau et son cas sain était refusé à juste titre par la vérification de l'arbre : il est
gardé pour trace) ; le préalable du GO de Lazar sur N-018. Le reste du plan v4 vaut tel quel.

Commit du code cité : `6ec7434119781a3abebac789174101b9ed6ae087` (670 tests ; seul `tests/test_validation_reelle.py`
change depuis la v1 dans l'arbre gelé). Les scripts s'exécutent depuis le bloc-notes (`revalidation-v2/`) ; leurs copies
versées et scellées sont sous `docs/procedures/revalidation-T0.5-v2/`, et le scellement comme le lanceur exigent
l'égalité des deux.

**Jamais** de `vastai show instance <id> --raw` ni de `vastai show instances --raw` sans filtre (Q-2) : forme filtrée
seulement, champs nommés.

0. **Préalables**, dans cet ordre :
   1. épingles écrites dans `controles_avant_depense_v7.sh` : candidats relu (2), vérifié (3) et final (5) (chemins sous
      `brouillons/`, empreintes ; le final aussi normalisé), rapports attendus (paires nom=empreinte, égales à
      l'ensemble des rapports de la v2 versés : relecture, vérification, contrôle mécanique, bancs) ;
   2. copies versées et scellées sous `docs/procedures/revalidation-T0.5-v2/` : générateur r4, contrôles v7 (épinglés),
      lanceur v7, scellement v5, récupération v2, les bancs (contrôles v7, lanceur v7, scellement v5 bancs 1 et 2), la
      répétition finale à blanc, ce plan ; journaux et sorties des bancs dans
      `prereg/contre-lectures/T0.5-revalidation-v2-verification-banc-controles-final-v1.tar` et
      `…-verification-banc-lanceur-scellement-v1.tar` ;
   3. répétition finale à blanc (`repetition_finale_scellement_v1.sh`) sur un clone jetable du commit des préalables :
      GO fictif, scellement puis contrôles avant dépense avec les épingles réelles ; tous conformes, sinon on corrige
      avant de demander le GO ;
   4. GO de Lazar sur N-018 : une ligne de `registres/go.md` (8 colonnes ; type « revendication » ; accordé par
      « Lazar » ; périmètre qui cite N-018), N-018 tranché dans `registres/decisions.md` (état : option (a) et ce GO),
      une ligne R-… qui consigne le GO ;
   5. tout committé et poussé.
1. **Scellement** : `sceller_revalidation_v5.sh <GO> <R-…>`. Régénère la v2 en mode reel à l'heure du scellement (fin
   « Pièces » remplie et reconstruite comme la reconstruisent les contrôles), exige l'égalité des scripts avec leurs
   copies versées, des candidats avec leurs épingles et de l'empreinte normalisée, scelle, un seul commit S, poussé.
   Banc : `essais_scellement_v5b.sh`, 8 artefacts refusés sans commit, un cas sain. S'il échoue après la copie de la
   v2 (scellement ou vérification de l'arbre), rien n'est committé ni poussé, mais la v2 et son sceau restent non
   suivis dans le dépôt : les retirer par leur nom, comprendre, puis rejouer.
2. **Contrôles avant dépense** : `controles_avant_depense_v7.sh S <dossier neuf>` (le lanceur les rejoue). Banc :
   `essais_controles_v7.sh`, un cas sain, 31 artefacts (A1 à A17, A3b, A9b, X1 à X12) et deux épingles mal formées
   (Z1, Z2) ; le banc du scellement joue aussi les contrôles de bout en bout sur la v2 qu'il scelle.
3. **Offre et crédit** : comme au plan v4 (prix ≤ 1,30 USD l'heure ; crédit ≥ 6 h × prix + 0,9 USD ; sinon nœud). Le
   processeur de l'offre est archivé (`cpu_name`, `cpu_arch`, `cpu_cores`). Risque résiduel déclaré : un hôte sans
   AVX2 ferait échouer trois tests (arrêt avant le run, environ 0,26 USD ; R-135, C-6).
4. **Création** : `lancer_revalidation_v7.sh <offre> <dossier de traces neuf>`, en un seul appel, aucun sous-agent en
   cours. Il refuse entre 23:30 et 00:00 UTC (au départ et juste avant la création ; T-7, VC-08) et sous 3 Go libres
   (bloc-notes et dossier des traces) ; il tolère l'instance arrêtée 55292763 si elle est relue arrêtée, et aucune autre
   (L-01) ; il exige que ses scripts égalent leurs copies versées à S ; il lit le GO de N-018 dans la v2 de S et le
   refuse s'il est révoqué dans le registre courant ; il relit `PREREG` et `BRANCHE` dans la v2 de S et les écrit, avec
   le GO, dans `lancement.txt`. **Codes** : 0 création ; 3 heure, place, crédit ou prix ; 2 tout autre arrêt avant la
   ligne « creation » de `lancement.txt` ; 4 tout échec après cette ligne : création douteuse, vérifier les instances
   par `vastai show instances` (sans `--raw`). Un argument ou un jeton absent donne 2 (CM-02). Banc :
   `essais_lanceur_v7.sh`, 19 cas. Consigner l'identifiant et l'heure dans `registres/etat.md`, la dépense
   dans `registres/depenses.md` (engagement avant la création), l'offre dans `traces/`.
   **4 bis** : entre 3 et 5 minutes après la création, `vastai logs <id> --tail 200`, masqué, dans
   `<traces>/journal-5min.txt` ; y trouver « AMORCE <date> : commit <S> », puis, dans le journal du script, la ligne
   « début : ETUDE=revalidation MODE=reel COMMIT=<S> BRANCHE=calcul/t05-revalidation-reel-v2 », « préenregistrement
   lu : 670 tests attendus » et « branche calcul/t05-revalidation-reel-v2 poussée avant l'installation ». Sinon : arrêt
   par identifiant (R10), nœud.
5. **Surveillance** : `PATH=<bloc-notes>/venv-vastai/bin:$PATH bash docs/procedures/surveiller-instance-t04-v1.sh <id>
   <CREATION> <dossier>` ; tâche de fond de 7 200 000 ms, relancée à l'identique ; plafond de 6 h ; rappel
   `send_later` à la création + 6 h 10.
6. **Sortie** : comme au plan v4. FIN (code 0, 1 ou 2) → arrêt immédiat par identifiant ; après l'arrêt, état relu
   « stopped » (forme filtrée), `registres/arrets.md`. Le conteneur relance l'amorce à chaque sortie (mode « args ») :
   ces redémarrages sont refusés par R12, sans effet ; arrêter dès la ligne « AMORCE … fin, code N ».
7. **Récupération** : `recuperation_revalidation_v2.sh S <dossier neuf>` (branche `calcul/t05-revalidation-reel-v2`,
   préenregistrement v2) : points 1 à 6 du plan v4 ; puis fusion dans `main`, poussée.
8. **Fin** : dépense consignée ; destruction des instances arrêtées proposée à Lazar ; verdict par un sous-agent neuf
   (`lire_bras`, `choisir_noyau`, depuis les résultats scellés), scellé, soumis à Lazar ; puis le pilote.

Réserves déclarées : jeton de l'instance non éprouvable depuis la session (poussée initiale sur l'instance, éprouvée par
la tentative de la v1) ; garde de calcul inactive dans cette session (rejouée par le lanceur) ; jetons dans les
arguments du processus vastai pendant la création (aucun sous-agent en cours) ; répétition jouet v3 de la chaîne :
passages 1 à 3 conformes, passage 4 interrompu par le disque plein de la session, et faite avec un texte jouet (rempli
par le générateur de la v1), non avec le texte de la v2 (VT-15) ; les lectures mécaniques de la v2 (tests attendus,
chemins, commit cité) sont éprouvées à part par le banc et le générateur. Reportés après le run : M-1 à M-3 de la
vérification 3, K-6, risques faibles de l'audit (R-133), C-6 (hôte sans AVX2), C-7, L-12, L-15 (retouches de l'amorce
gelée).
