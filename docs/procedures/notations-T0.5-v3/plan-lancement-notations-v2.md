# Plan de lancement des notations décisives refaites du pilote de T0.5 — v2

Objet : le même que le plan v1 (`docs/procedures/notations-T0.5-v2/plan-lancement-notations-v1.md`, copie versée et scellée,
qui reste tel quel, R12). Ce plan v2 change le lanceur et ce qui en découle (veille, registres, étape 4 bis, relancement). Décision de Lazar du 17 octobre 2026 (R-190), option
(c) de la question de R-180 : un **lanceur v2** qui, après les contrôles avant dépense, relit les offres au filtre du plan et
prend la moins chère des offres conformes, au lieu d'exiger l'identifiant reçu en argument une vingtaine de minutes plus tôt.
Motif : huit appels du lanceur v1, huit arrêts avant la création, aucune dépense ; six fois sur huit, l'offre ou son
identifiant avait changé pendant les contrôles (R-178, R-179, R-180, R-182, R-188, R-190 ; les deux autres : R-177,
signature des commits, et R-185, arrêt par la session ; compte corrigé par la contre-lecture R2 du v2, LV-12). C'est un écart nommé à la chaîne de lancement scellée (« chaîne figée
après C » ; après S, toute correction est un écart), décidé par Lazar. Le préenregistrement scellé ne fixe que le filtre et
le plafond de prix (« A100 SXM4 80 Go sur AMD EPYC 7513 (même filtre d'offre que le pilote), au plus 1,30 USD de l'heure »,
section « Calcul ») : il est inchangé, comme la dépense autorisée (GO-2026-10-12-02, au plus 10,5 USD, sous GO-2026-10-04-08).

**Ce qui change**
- **Lanceur** : `lancer_notations_v2.sh DOSSIER_TRACES AUTRES_PROJETS [relance R-NNN RELEVE_DU_PREMIER_LANCEMENT]`, sans
  offre. Différentiel avec le v1 :
  - arguments sans offre ;
  - étape 5 : offres relues au filtre du plan (même filtre que le v1) ; conformes : carte « A100 SXM4 », processeur « AMD EPYC
    7513 32-Core Processor », au moins 79 000 Mo de mémoire de carte et une seule carte (champs du filtre relus localement),
    prix fini et strictement positif (nombre, non booléen) au plus PRIX_MAX (1,30 USD de l'heure), identifiant entier ; la
    moins chère est prise, à prix égal le plus petit identifiant ; la liste des offres conformes relues (identifiant, prix,
    machine, hôte, coût de téléchargement, date de fin) s'écrit dans `lancement.txt`, l'offre choisie dans `offre.json` (champs
    du v1, plus `machine_id` et `host_id`), un extrait de toutes les offres lues dans `offres-relues.json` (la réponse brute,
    si elle est illisible, dans `offres-relues-brut.txt`), versés aux traces ; aucune offre conforme : code 3, pas de
    création ; réponse illisible ou qui n'est pas une liste : code 2 ;
  - **relancement** (nœud LV-02, soumis à Lazar) : les offres de la machine ou de l'hôte de l'instance du premier lancement
    (relus en forme filtrée dans la liste des instances) sont écartées, ainsi que toute offre dont la machine ou l'hôte n'est
    pas un entier lisible ; instance absente de la liste, machine ou hôte illisibles : code 2 ; les offres écartées
    s'écrivent dans `lancement.txt` (option (a) de LV-02, recommandée : elle ne peut que restreindre le choix ; toute relance
    demande de toute façon l'accord de Lazar, R-185 ; s'il retient (b) ou (c), un lanceur v3 sera versé avant toute
    relance). **Conséquence à trancher avec le nœud** (relecture courte, RC-06) : après une « instance perdue » (cause
    d'infrastructure du préenregistrement) qui aurait disparu de la liste des instances, ce lanceur refuse la relance ;
    options : l'accepter (une relance demanderait alors un lanceur v3), ou lire machine et hôte dans l'`offre.json` du
    premier lancement, versé aux traces (lanceur v3) ;
  - identifiants des offres lues tous distincts, sinon code 2 (garde du v1, relecture courte RC-01) ;
  - le plafond de l'étape et le crédit exigé se calculent au prix de l'offre choisie (même règle que le v1) ;
  - étape 2 : le lanceur v2, exécuté par son propre chemin, égal à sa copie versée et scellée au commit **C3** qui ajoute
    `docs/procedures/notations-T0.5-v3/lancer_notations_v2.sh.sha256` (C3 descendant de S, sur le dépôt distant ; C3 ne touche
    que ce dossier ; la copie du sommet du dépôt distant égale au lanceur exécuté) ; le banc v2 versé à C3 avec son sceau
    exact ; les douze autres scripts de la chaîne égaux à leurs copies versées à S, comme au v1 ; les constantes du devis et
    du filtre (`PRIX_MAX`, `HEURES_CREDIT`, `PLAFOND_GO`, `PLAFOND_SURVEILLANCE_S`, `FILTRE`, `ARRETEES_TOLEREES`) aux mêmes
    lignes que le lanceur v1 versé à S : la phrase du préenregistrement « les contrôles … relient ces bornes aux constantes du
    lanceur » porte sur la copie v1, et le v2 lui est lié mécaniquement (LV-03) ; dossier de traces purement numérique
    refusé (forme du v1) ;
  - étape 2 ter : preuve du banc v2 (`banc-lanceur-notations-v2.log`, versé et scellé à C3) : dernière ligne « FIN DU BANC DU
    LANCEUR V2 DES NOTATIONS ; cas non conformes : 0 », aucune ligne d'échec, exactement trois scripts éprouvés : le lanceur
    v2 et le banc v2 sous les empreintes de leurs copies versées à C3, le module commun `verifications_notations_v1.py` sous
    celle de sa copie versée à S ; les cinq journaux de S restent exigés tels quels (leur lecture par
    `verifications_notations_v1.py preuves` est inchangée).
- **Banc** : `essais_lanceur_notations_v2.sh`, décliné du banc v1 : tous ses cas sauf N06 (offre absente : le v2 ne reçoit pas
  d'offre ; O03 le couvre), adaptés aux arguments du v2 (les cas d'offre sans prix, de processeur ou de carte autres rendent
  désormais le code 3, « aucune offre conforme »), plus les cas propres au v2 ; après la contre-lecture R2, un artefact pour
  chaque garde nouvelle (133 cas ; quatorze mutants du lanceur, chacun privé d'une garde nouvelle, attrapés par le banc :
  traitement versé) : offre la moins chère parmi des conformes et des non conformes mêlées, égalité de prix, aucune offre, seulement
  au-dessus du devis, offres illisibles ou qui ne sont pas une liste, prix au plafond juste, crédit calculé sur l'offre
  choisie ; preuve du banc v2 (journal absent, verdict, empreinte, ligne d'échec, sceaux du journal et du banc, copie versée
  autre que le lanceur exécuté, C3 absent du distant, C3 antérieur à S, rétablissement).
- **Copies versées et scellées** sous un dossier neuf, `docs/procedures/notations-T0.5-v3/` : le lanceur v2, son banc, le
  journal brut du banc (sortie redirigée dans un fichier neuf, sans enveloppe : sa dernière ligne est le verdict), ce plan,
  le rapport de la contre-lecture R2 et son traitement ; **un seul commit C3, qui ne touche que ce dossier**, poussé, après la
  contre-lecture R2 du différentiel et du banc et une relecture courte des corrections ; le bloc-notes porte la copie du
  lanceur v2, égale à celle de C3. Les registres se mettent à jour dans un commit suivant.
- **Veille d'avant l'appel** (remplace celle de R-182 et R-188, qui supposait un prix connu ; LV-11) : au moins une offre
  conforme relue juste avant l'appel, sans fixer son identifiant (RC-11), et un crédit au moins 7,5 × (1,30 + somme des
  prix des autres projets en marche) + 1,2 USD, plus la marge de R-188 (baisse attendue du crédit pendant les contrôles,
  plus 0,20 USD) ; sinon, pas d'appel (recharge demandée à Lazar s'il manque du crédit).
- **Registres avant la création** : `registres/etat.md` (heure de l'appel, offres conformes relues juste avant, sans
  identifiant prévu) et `registres/depenses.md` (engagement au plafond de prix : 7,5 × 1,30 + 0,5 = 10,25 USD au plus pour
  l'étape, sous les 10,5 USD de GO-2026-10-12-02 ; crédit exigé au prix de l'offre que le lanceur prendra, connu à la
  création) ; l'offre choisie est consignée après la création, avec la ligne R-… de l'appel, son prix, sa machine, son
  hôte, son coût de téléchargement et sa date de fin (LV-14).
- **Étape 4 bis** (contrôle à 5 minutes, LV-13, RC-04) : en plus du v1, relire en forme filtrée le prix (`dph_total`) et la
  machine de l'instance créée et les consigner ; si le prix relu dépasse celui de la ligne « offre choisie », recalculer à
  ce prix le plafond de l'étape (dépense engagée + 7,5 × prix + 0,5 USD au plus 10,5 USD, condition (iii) du
  préenregistrement) et le crédit exigé ; prix au-dessus de 1,30 USD de l'heure, plafond dépassé ou crédit insuffisant :
  arrêt par identifiant (R10) et nœud. Après un code 4 sans instance créée (vérifiée en forme filtrée) : nouvel appel,
  traces neuves, accord de Lazar (R-185).
- **Accord de Lazar** donné dans la session pour chaque appel payant (R-185).

**Remplacé dans le plan v1** (LV-10) : la chaîne des treize scripts (le lanceur v2 à C3 au lieu de `lancer_notations_v1.sh`,
les douze autres à S) ; l'appel de l'étape 4 (`lancer_notations_v2.sh <traces> <autres projets>`, sans offre) et la phrase
« les treize scripts … égaux à S » ; l'appel de relance de l'étape 7 (`lancer_notations_v2.sh <traces> <autres projets>
relance R-NNN <relevé>`, sans offre) ; l'« identifiant prévu » des registres (aucun : l'offre est choisie à la création) ;
la veille d'avant l'appel (ci-dessus).

**Ce qui ne change pas** (hors ce qui est écrit ci-dessus) : tout le reste du plan v1, mot pour mot : préalables déjà faits (C1, C2, S), contrôles avant dépense
(`controles_avant_depense_notations_v1.sh`, rejoués par le lanceur au même S), heure (pas de création entre 23:30 et 00:00
UTC), place, jetons, instances tolérées et autres projets nommés (dont la règle `rr-` de R-181), garde de calcul rejouée,
étape 4 bis (journal à 5 minutes, plus prix et machine relus, ci-dessus), surveillance (`surveiller_notations_v1.sh`, plafond à la création + 26 400 s), relevé
cumulatif, traces, sortie et arrêt par identifiant (R10), relancement unique (règle du préenregistrement ; lanceur v2 en mode relance, avec l'exclusion de LV-02, nœud),
récupération (`recuperation_notations_v1.sh`), lecture et verdict R13 complémentaire.

**Réserves** : la fenêtre entre la relecture des offres et la création reste de quelques secondes (prix, plafond,
instances, crédit, garde) ; une offre louée dans cette fenêtre fait échouer la création (`--cancel-unavail`), avec le code 4
du v1 (création douteuse : vérifier les instances en forme filtrée) ; le lanceur v2 ne réessaie pas d'autre offre ; une
offre qui garderait son identifiant en changeant de prix dans la fenêtre serait louée au prix nouveau (une location à la
demande ne porte pas de prix plafond) : l'étape 4 bis le relit (LV-13). Le tri ne regarde que le prix de l'heure, ni le
coût de téléchargement ni la date de fin, écrits dans les traces (LV-14) ; une borne sur ces champs changerait le filtre
(nœud). La marge de 0,5 USD du plafond de l'étape (téléchargement et disque) n'est pas remesurée au prix plafond (LV-14).
Les réserves du plan v1 restent valables.
