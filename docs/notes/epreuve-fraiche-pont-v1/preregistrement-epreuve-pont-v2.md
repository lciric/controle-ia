# Préenregistrement — « épreuve fraîche » du pont fiche de course → fiche-loi du pôle, premier essai, v2

- Auteur : sous-agent neuf de session-depot (rédacteur ; n'a écrit ni le pont ni sa conception), à la demande de session-depot ;
  exécution par session-depot. Aucun appel de modèle, aucun appel réseau, rien de scellé ni de commis par le rédacteur.
- Version 2 = version 1 (`preregistrement-epreuve-pont-v1.md`, brouillon relu
  `41dc127b278b3c4faf1fc22145a8d1492f43644d7721fb7e9275999409b23789`, gardé sans modification, R12) avec toutes les corrections
  acceptées de la contre-lecture 1 (CL-01 à CL-13 ; traitement de chacune dans la section « Contre-lecture »).
- Date (UTC) : 2026-11-01, version 1 achevée vers 17:30 (relevés `date -u` de 17:24 et 17:27) ; version 2 écrite à partir du
  relevé `date -u` de 18:02.
- Commit du code d'analyse : `donnees/` est ignoré par git sur `main` (versement éventuel sur une branche `donnees/*`, R-352) ;
  les empreintes de la section « Pièces gelées » font foi ; le commit du dépôt est aussi écrit par le lanceur dans le dossier du
  run (`environnement-run.json`, CL-11) ; commit du dépôt au moment du scellement : `96ae0d27`
- Documents qui font foi (chemin + empreinte) : conception du pont, section (g) « préenregistrement court du premier essai »
  (brouillon repris ici), sections (c), (d), (e) — `donnees/epreuve-fraiche-pont-v1/pont/conception-pont-fiche-loi-v1.md`,
  `5161e199e15dacc728d4b2e7b1769f700e0a293c05fb26d402dfe40d25c4a974` ; module `pont_v1.py`,
  `9fb2d9366e7764d4fc810b921e8565ca2dcae9af5f1b30ec8866efeb5d3eb692` ; consigne figée du traducteur
  (`pont_v1.CONSIGNE_TRADUCTEUR`, 2 404 caractères), `fd7aa5f2fc92967b2f8b9e9ca161676b8bdfd696431b73a0307b28bb5517e2e4` ;
  rapport de contre-lecture 1, `donnees/epreuve-fraiche-pont-v1/contre-lecture-preregistrement-epreuve-pont-v1.md`,
  `b688ae1f8104efe013be91bf8b1f12f918b40fd77c4f6eeea62877291723ff81` ; GO-2026-11-01-09 (`registres/go.md`, plafond 5 dollars,
  échéance 2026-11-08, mot direct de Lazar) ; R-964 (« j'insiste pour utiliser Kimi et Argon à la place pour le moment ») ;
  R-750 (règle des refus) ; règle N-053 (« pare-feu » : aucun score de juge dans une sélection).
- Empreinte de la valeur engagée (SHA-256 de la valeur, en ASCII, sans fin de ligne) : `dceb2a258b110a293b628b6f2d430cf378adcd7dd3fbe15e50c777005768af4f`

## Hypothèse

Question (conception, § g) : **le pont classe-t-il des fiches réelles de façon stable, et attrape-t-il ses témoins ?** L'essai ne
demande pas si les lois traduites sont vraies : il faudrait une épreuve fraîche, qui n'existe pas (toutes les épreuves des banques
T0.5 sont lues).

Hypothèses de travail, chacune jugée par un critère gelé (section « Critères de lecture gelés ») :
- **HP1 « dents »** : sur six témoins mêlés anonymes aux fiches, le pont rend la vérité écrite d'avance pour au moins cinq,
  dont les deux « aller-retour » (T1, T2) — critère L1.
- **HP2 « fidélité »** : deux traductions aveugles de familles différentes (Kimi, Argon) d'une même fiche s'accordent
  (`pont_v1.comparer_lois` : même cible, forme, objets, issue, sens ; effets à un facteur 2 au plus) dans au moins 60 % des fiches
  réelles où au moins une des deux traductions est une loi — critère L2.
- **HP3 « utilité »** (critère de mort du pont tel que conçu) : au moins une fiche réelle sort en loi (sortie 1 différée ou
  sortie 2, accord compris par construction du module) — critère L3.
- **HP4 « sûreté »** : aucune lecture de l'épreuve (aucun arrêt `LectureEpreuveInterdite`, aucun canari dans une réponse) —
  critère L4.
- **HP5 « défauts »** : les renvois de la famille « pont » (N6 à N11 : défauts de la traduction) restent rares — critère L5.

Renvoi au programme : prise idéation du pôle (décision de Lazar R-1037 de la branche conv-audit, « prévu mais pas construit :
fais-le ») ; aucune hypothèse du programme (H1 à H9) n'est testée ici ; l'essai mesure un instrument.

**Écarts au brouillon (g), décidés par le directeur ou par session-depot, déclarés** :
1. **Traducteurs Kimi (`kimi-k3.1-pro`) et Argon (`gemini-4-argon`) seulement** (R-964). Pour garder trois familles distinctes par
   fiche (auteur, traducteur, contre-traducteur ; `pont_v1.verifier_affectation`), **seules les fiches de Fable (famille
   Anthropic) sont éligibles** ; règle fixe, celle du module (`affectation_recommandee("anthropic")`) : **Kimi traduit, Argon
   contre-traduit**, pour toutes les fiches et tous les témoins. Le « 5 de Fable et 5 d'Argon » du brouillon devient « toutes
   les idées de Fable ». La quatrième famille disponible dans la session (OpenAI) n'est ni dans la liste fermée des familles du
   module (`pont_v1.FAMILLES`), ni dans le périmètre du GO : elle n'est pas utilisée (CL-08 c).
2. **Huit idées distinctes de Fable seulement** (15 fiches de Fable sur 29, toutes éligibles, fermées en 8 groupes par la note
   des doublons) : moins de 10, donc **les 8 sont prises** (aucune n'est écartée) ; les prédictions sont **ajustées par écrit**
   (section suivante). **8 fiches et 6 témoins, en deçà du périmètre du GO (« 10 fiches »), sans dépense de plus** (CL-08 a).
3. **Témoins T1 à T6 écrits par un « metteur en forme tiers »** : un **sous-agent neuf de session-depot** (famille Anthropic,
   au lieu de Sonnet 5.5 : Sonnet demanderait des crédits Claude d'interface de programmation, exclus par R-964, alors qu'un
   sous-agent de session-depot ne coûte rien, CL-08 b), lancé **après** le scellement et le tirage, sur une consigne fermée
   (`consigne-metteur-en-forme-temoins-v2.md`) qui lui donne le catalogue réel et le format de fiche, jamais la consigne du
   traducteur, jamais les fiches réelles, jamais la vérité attendue. Les témoins ont donc la famille d'auteur des fiches
   (Anthropic) : même affectation pour les quatorze passages, rien ne les distingue par le routage.
4. **Entropie du tirage** : empreinte du préenregistrement scellé **et** valeur de session-depot engagée par son empreinte avant
   le scellement (ligne d'en-tête ; marqueur à remplir par session-depot) — reprise du brouillon, rendue vérifiable par programme.
5. **Deux précisions de lecture, plus strictes ou plus prudentes que le brouillon** (CL-08 d) : L4 compte aussi les arrêts
   `LectureEpreuveInterdite` (pas seulement les canaris dans une réponse) ; L2 sur moins de 3 fiches traduites se lit « non
   lisible », là où le brouillon pouvait se lire « ambiguïté élevée ».

**Choix pris par le rédacteur (relus par la contre-lecture 1, corrigés selon elle)** :
6. **Représentant d'une idée tiré au hasard** parmi ses fiches éligibles de Fable, **jamais la mieux classée** : la sélection
   ne dépend d'aucune note de juge (pare-feu N-053, conception § e). L'éligibilité (champ `eligible` du classement, 27 sur 29)
   est reprise du brouillon ; elle est inerte ici (les 15 fiches de Fable sont éligibles). Signalé à conv-audit (CL-13 b) : ce
   champ voisine des notes (`eligible_unanimite`, `total`) ; s'il dérive d'une note, l'utiliser comme filtre en course 2 serait
   une sélection sur juge. Les doublons ont été signalés par les deux juges (identité, pas qualité) ; la paire signalée par un
   seul juge (argon-p2-02, fable-p2-03) reste séparée.
7. **Catalogue servi** = description publique **réelle** de la banque T0.5 `banque-t05-v2` (archive de l'orchestrateur v56,
   `exemples/banque-t05-v2.json`, `f26cc857…`), produite par le vrai `MondeBanque.description_publique()` : 4 traits,
   2 sous-populations, 13 moniteurs (nombre d'issues, effectifs d'épreuve et de calibrage) ; **aucune banque de scores** (la
   couche 2 n'existe pas). `banque-t05-v1` (mêmes épisodes, un trait de plus, remplacée) et les banques plantées de la couche
   1 bis ne sont pas servies. Aucune description sémantique ajoutée (le traducteur voit ce que voit un proposeur du pôle).
8. **État du noyau, jamais servi** (`noyau-pont-t05-v2-v1.json`) : prédicteurs connus des 13 moniteurs ajustés sur le calibrage par
   le vrai code v56 ; épreuve marquée **lue** (`epreuves_fraiches` faux) — « épreuves marquées lues » du brouillon s'entend dans
   l'état du noyau, pas dans le catalogue servi ; politique « fraîche seulement » ; **registre des lectures vide** (la mémoire du
   pôle n'est pas servie : G1 ne vaut que par la politique, sans effet sur le classement puisque toute épreuve est lue) ;
   sonde = traits des 40 instances de calibrage ; **canaris = identifiants des 80 instances d'épreuve** ; α = 0,05 ; m = 8.
9. **Couche v57 absente** : la stratégie « traduction_de_course » est ajoutée **en mémoire** au catalogue du vrai
   `proposeur.valider_proposition` (v56), dans le processus du lanceur seulement ; la vraie garde est injectée au module (qui ne
   l'appelle qu'en sortie 1, impossible ici) et **appliquée à chaque proposition compilée, à titre d'information** ; une
   proposition acceptée par le miroir du module mais **refusée par la vraie garde est une anomalie du module** : audit avant de
   lire L3 (CL-10 c).
10. **Refus et tour neuf (R-750, CL-04)**. Un refus (statut « REFUS » de l'API) arrête la fiche (le module la renvoie : N10 pour
    le traducteur, N8 pour le contre-traducteur) ; trois refus arrêtent le tour ; c'est la lecture de la conception (§ c) et du
    brouillon (§ g). **Un seul tour neuf**, reformulé par un **préambule plus technique et plus spécifique** écrit par
    session-depot après le tour (catégorie du refus lue, jamais la fiche), scellé, appliqué aux deux rôles, sur les seuls
    passages non classés ou refusés, sous le même GO et le même plafond cumulé. **Réserve de R-750** : si la catégorie du refus
    touche ce que nos règles interdisent (recette d'évasion, conduite d'attaque ou de sabotage), **aucun tour neuf**, le refus est
    définitif. Au tour neuf, **les deux rôles sont rappelés sur le même texte reformulé, y compris celui qui avait répondu** ; les
    réponses du premier tour sont gardées et rapportées (`reformules_premier_tour` de l'agrégat), jamais fusionnées ; le choix 11
    vaut à l'intérieur d'un tour. Le préambule n'ajoute que domaine et vocabulaire défini ; il ne modifie ni la consigne figée ni
    la fiche, et ne nomme ni sortie, ni code, ni témoin, ni l'épreuve (garde du préambule dans le lanceur). Une fiche lue au tour
    neuf est marquée « reformulé » ; un second refus est définitif.
11. **Échec de transport** (aucune réponse reçue) : une reprise à l'identique, **par le lanceur seulement, avec une nouvelle
    réservation au pire cas** ; une réponse reçue n'est jamais rejouée ; un appel sans usage lisible est compté **à son pire cas**.
    **Argon est appelé sans reprise interne** (`appeler_gemini(..., attentes=(0,))`, CL-05) : vérifié par le rédacteur, la
    fonction du collisionneur reprend par défaut aussi sur une coupure de connexion, qui peut survenir après une requête facturée ;
    ses reprises internes auraient pu dépenser hors de la réservation. Kimi : une seule tentative par appel (`appeler_kimi`).
    **Un coût lu au-dessus de son pire cas arrête le tour** (la garantie du plafond ne tiendrait plus).
12. **Témoins servis sous leur forme canonique** : validés par le vrai `ideation_v2.valider_fiche_ideation` (le validateur des
    fiches réelles), champs internes retirés, longueur servie dans la fourchette des 15 fiches de Fable (5 382 à 8 251
    caractères, mesure `len(json.dumps([fiche], ensure_ascii=False, indent=1))`), garde A4 des étiquettes, aucun canari ; **leur
    transcription des six descriptions est contrôlée par programme** (nombres, noms, signe, type exigés par la consigne) ; les
    étiquettes « T1 » à « T6 » y sont refusées ; ils sont **scellés et leurs empreintes inscrites au registre** avant le
    lancement, que le lanceur exige (CL-09).
13. **T6 sans chiffre hors de `3B:RIGOR`** (CL-03) : la consigne v2 fait désigner la classe visée en toutes lettres (« la classe
    la plus haute », sans « issue 1 ») et interdit le nom de banque (qui porte des chiffres) ; le lanceur refuse un T6 qui porte un
    chiffre hors de « 3B:RIGOR ». La vérité de T6 reste N2 ou N9. Reste le « 3 » de « 3B » : un effet de 3 cité depuis ce nom
    passerait la garde N9, qui vérifie la présence d'un nombre, pas son sens ; T6 serait alors « faux » par cette faiblesse
    connue, qu'il a aussi pour rôle de révéler.
14. **Ordre de passage : témoins dans la première moitié** (CL-12 b) : les six témoins sont placés à des positions tirées parmi
    les sept premières (sur quatorze), les fiches au hasard dans les places restantes. L'ordre ne protège rien chez le traducteur
    (un agent neuf par fiche, sans mémoire) ; il protège L1 contre un arrêt par la garde de plafond : avec un ordre uniforme,
    perdre les k derniers passages aurait coûté au moins un témoin avec une probabilité de 0,43 (k = 1), 0,69 (k = 2), 0,85
    (k = 3) ; ici, aucun témoin n'est perdu tant qu'au plus sept passages le sont (les fiches réelles sont perdues d'abord, ce
    que les règles de lisibilité de L2, L3, L5 et des prédictions prennent en compte).
15. **Plafonds de sortie** : Kimi 24 000 jetons, Argon 12 000 jetons (raisonnement compris) ; trois passages en parallèle (la
    garde attend les réservations en cours, elle n'arrête pas plus tôt à cause du parallélisme).
16. **Clés (CL-13 a)** : le lanceur shell passe les clés par la ligne de commande d'`env -i` jusqu'à son `exec`, ce qui les expose
    quelques microsecondes dans `/proc` ; pratique commune de tous les lanceurs du dépôt, conteneur à un seul utilisateur ;
    correction prévue dans une version ultérieure. Aucune clé n'est passée en argument du Python ou du relais, ni écrite en fichier.

## Prédiction chiffrée et signe attendu

Prédictions du brouillon (g), sur 10 fiches, **ajustées à 8 fiches** par la règle « multiplier par 0,8, arrondir à l'entier
le plus proche », sans autre changement :

| grandeur (fiches réelles traitées, sur 8) | brouillon (10 fiches) | **prédiction gelée (8 fiches)** | ce qui réfute |
|---|---|---|---|
| sortie 1 différée (loi sur une cible du catalogue, épreuve lue) | 1 (0 à 3) | **1 (intervalle 0 à 2)** | 3 ou plus |
| sortie 2 (loi qui attend un objet à construire, « couche 3 ») | 4 (2 à 6) | **3 (2 à 5)** | 0, 1, 6 ou plus |
| sortie 3 (non testable, renvoi motivé) | 5 (3 à 7) | **4 (2 à 6)** | 0, 1, 7 ou 8 |
| dont renvois de famille « pont » (N6 à N11) | ≤ 2 | **≤ 2** (1,6 arrondi au-dessus, dit) | 3 ou plus |
| accord des deux traductions (proportion) | ≥ 0,6 | **≥ 0,6** (proportion, inchangée) | moins de 0,6 sur au moins 3 fiches traduites |
| témoins justes | ≥ 5 sur 6 | **≥ 5 sur 6** (inchangé) | 4 ou moins, ou T1 ou T2 faux |
| sortie 1 (banque existante, épreuve fraîche) | — | **0** (impossible par construction : toute épreuve est lue) | 1 ou plus : anomalie, audit |

**Signes attendus (CL-06)** : sortie 2 > sortie 1 différée (3 contre 1) ; sortie 3 ≥ sortie 1 différée ; renvois et traductions à
égalité au centre (4 contre 4) : **aucun signe gelé entre eux** ; les deux traductions s'accordent plus qu'elles ne divergent
(accord ≥ 0,6) ; les témoins sont majoritairement justes. Les parts sont SUPPOSÉ (conception § b.3) : le format de la course 1
porte une loi prédictive en texte libre, rarement rattachée à un moniteur du catalogue ; la plupart des fiches traduisibles
devraient sortir en sortie 2.

## Métrique

Toutes mécaniques, calculées par `lancer_epreuve_pont_v2.agreger` sur les résultats du module ; aucune interprétation.
- **M1 classe** d'une fiche réelle traitée : sortie 1 (`loi_banque_existante`) ; **sortie 1 différée** (`loi_couche_3` dont la
  cible existe au catalogue : liste `manque` de la traduction du traducteur vide) ; **sortie 2** (`loi_couche_3` avec un objet à
  construire) ; **sortie 3** (`non_testable`), famille « fiche » (N1 à N5) ou « pont » (N6 à N11). Une fiche non traitée
  (interrompue, non lancée, échec technique) est « non classée » et comptée à part.
- **M2 accord** : dénominateur = fiches réelles traitées dont au moins une des deux traductions est une loi valide (état « loi »
  du module) ; numérateur = celles où `comparer_lois` rend l'accord. Une loi contre un renvoi, ou un contre-traducteur
  défaillant, compte comme désaccord. L'accord des renvois (mêmes codes) est rapporté, non décisif.
- **M3 témoin juste** (`verite-temoins-v1.json`) : T1, T2 → une loi dont la signature compilée égale la signature écrite
  (forme, banque, moniteur, traits dans l'ordre, issue, sens, sous-population) et dont l'effet est à un facteur 2 au plus
  (T1 : `8B:RIGOR`, issue 2, `jetons_par_action_ecart_type`, « + », 0,8 ; T2 : `3B:COHERENCE`, issue 0, interaction
  `actions_valides` sous condition `log_jetons_total` > 0, « − », 0,6) ; T3 → N5 ; T4 → N1 ; T5 → N3 ; T6 → N2 ou N9.
- **M4 incidents** : arrêts `LectureEpreuveInterdite` + réponses portant un canari.
- **M5 défauts** : renvois de famille « pont » parmi les fiches réelles traitées.
- **Rapporté, jamais décisif** : codes de renvoi, divergence de Kullback-Leibler symétrique entre les deux lois, puissance
  approchée et effectif requis, verdict de la vraie garde v56 sur chaque proposition compilée, refus, échecs techniques,
  drapeaux du module, dépense ; **réponses tronquées** (statut « TRONQUE » ou « VIDE » : plafond de sortie atteint), rapportées à
  part sans changer la classe mécanique (elles deviennent N10 ou N8 et comptent pour L5, CL-10 b) ; réponses du premier tour des
  passages reformulés.
Effectifs trop petits pour un intervalle utile : les comptes sont lus tels quels, sans intervalle de confiance (dit).

## Seuil

Fixés avant toute lecture, repris du brouillon (g), ajustés à 8 fiches là où ils sont des comptes :
- **L1** : au moins **5 témoins justes sur 6**, **et** T1 et T2 justes.
- **L2** : accord **≥ 0,6**, lu seulement si au moins **3** fiches réelles sont traduites (M2).
- **L3** : au moins **1 fiche réelle sur 8** en sortie 1 différée ou en sortie 2.
- **L4** : **0** incident.
- **L5** : renvois de famille « pont » **≤ ⌊0,3 × n⌋** fiches réelles, n = fiches réelles traitées (**≤ 2 sur 8** ; le brouillon
  disait ≤ 3 sur 10 ; 2,4 arrondi au-dessous, plus strict, dit).
- Plafond de dépense : **5 dollars cumulés** (premier tour et éventuel tour neuf), garde avant chaque appel.

## Plan d'analyse

**Données.** Entrées : `entree/fiches-validees.json` (29 fiches de la course 1, tentative 2, niveau méthode, passées par
l'aiguilleur), `entree/classement.json`, `entree/lecture-complementaire-doublons-argon-v1.md` (12 paires, 17 idées). Le tirage
ne lit des fiches que `auteur`, `identifiant_auteur`, `passe`, `nom`, `empreinte` ; il copie le contenu sans l'interpréter.

**Valeur engagée (CL-12 a)** : la valeur est tirée **une seule fois** (geste 2 du LISEZMOI) ; aucun tirage n'est exécuté sur les
entrées réelles avec la valeur réelle avant le scellement. Limite dite : l'engagement puis la révélation n'empêchent pas celui
qui scelle d'essayer plusieurs valeurs avant de sceller ; l'enjeu est faible (128 combinaisons de représentants, l'ordre).

**Inscription avant le tirage (CL-02, geste de session-depot)** : après le scellement et **avant le tirage**, session-depot
inscrit dans `registres/decisions.md` l'empreinte du préenregistrement scellé et celle de la valeur engagée (64 caractères
chacune, en entier), commet et pousse ; le préenregistrement et son compagnon peuvent aussi être versés sur une branche
`donnees/*` (R-352). **Le tirage ne court qu'après cette poussée** : `tirer_fiches_v2.py` refuse si l'une des deux empreintes
manque au registre sur le disque ou dans la référence poussée qu'on lui donne (`--ref-poussee`, lue par `git show`).

**Tirage (R9)** : `tirer_fiches_v2.py`, après l'inscription : `numpy.random.SeedSequence(entropy=[int(SHA-256 du préenregistrement
scellé, 16), int(valeur engagée, 16)])`, quatre enfants dérivés par tâche (sous-ensemble, représentants, numérotation, ordre) ;
sous-ensemble : 10 idées sans remise si plus de 10, sinon toutes (ici les 8) ; représentant tiré parmi les fiches éligibles de
Fable de l'idée ; numérotation anonyme F-01 à F-08 tirée ; ordre de passage tiré, témoins dans la première moitié (choix 14).
Contenu seul copié dans `fiches-tirees/` (champs internes retirés, garde des métadonnées du pont, garde A4 des étiquettes), un
manifeste d'empreintes (`manifeste-tirage-v2.json`) ; la valeur engagée y est révélée.

**Témoins (CL-09)** : écrits par le sous-agent tiers (écart 3) sur `consigne-metteur-en-forme-temoins-v2.md` ; contrôlés par
`lancer_epreuve_pont_v2.py verifier-temoins` (gabarit, garde A4, longueur, transcription des six descriptions, étiquettes
« T1 » à « T6 ») ; **la transcription du sous-agent est contrôlée par programme** (`lancer_epreuve_pont_v2.py
verifier-transcription --transcription <fichier JSONL du sous-agent>` : seuls sa consigne, ses six fichiers et la commande de
vérification sont permis) ; tout signalement → les six fiches sont jetées et réécrites par un nouveau sous-agent neuf. Les six
témoins sont ensuite **scellés** et leurs empreintes **inscrites en entier** dans `registres/decisions.md` ; le lanceur refuse de
tourner sans compagnons conformes ni inscriptions ; le lecteur neuf vérifie qu'elles concordent avec le manifeste de run.

**Passage** : `lancer-epreuve-pont-v2.sh lancer` (clés sous `env -i`, relais Kimi local par identifiant de processus, archive
v56 tirée de la branche de conv-audit et vérifiée par empreinte) ; pour chaque passage, dans l'ordre tiré, `pont_v1.traduire_fiche`
avec : catalogue et noyau gelés ci-dessous, affectation `{famille_auteur: anthropic, traducteur: kimi-k3.1-pro,
contre_traducteur: gemini-4-argon}`, canaris, α = 0,05, m = 8, politique « fraîche seulement », vraie garde v56 injectée. Le
traducteur et le contre-traducteur reçoivent **le même texte** (consigne figée, fiche, catalogue) ; le contre-traducteur ne voit
jamais la première traduction. Un passage = au plus deux appels (un seul si le traducteur faillit ou refuse), plus au plus une
reprise de transport par appel. **Avant tout appel (CL-11)**, le lanceur écrit et scelle dans le dossier du run
`environnement-run.json` : commit du dépôt, version et empreinte du Python des appels, liste des paquets installés (équivalent
de `pip freeze`, par `importlib.metadata`), empreintes des modules chargés ; il refuse de tourner si le commit est illisible.

**Coût estimé (SUPPOSÉ)** — barèmes du collisionneur v7 : Argon 10 et 50 dollars par million de jetons (entrée, sortie), Kimi 2
et 10. Entrée mesurée : 9 323 à 12 183 caractères par passage (fiches de Fable, catalogue réel), soit ≈ 2 700 à 3 500 jetons
(SUPPOSÉ 3,5 caractères par jeton). Sorties SUPPOSÉ, raisonnement compris : Kimi 2 000 à 12 000 jetons, Argon 1 500 à 6 000.
Par appel : Kimi ≈ 0,03 à 0,13 dollar ; Argon ≈ 0,11 à 0,33. Par passage ≈ 0,14 à 0,46 ; **14 passages ≈ 2,0 à 6,4 dollars,
valeur centrale ≈ 3,3** (Kimi 5 000 et Argon 3 000 jetons de sortie). Pire cas par appel (garde) : Kimi ≈ 0,25, Argon ≈ 0,64 ;
pire cas total ≈ 12,4 dollars : **la garde de plafond peut mordre**. Si elle arrête le tour, les passages restants sont « non
lancés » (des fiches réelles d'abord, choix 14), la lecture est partielle selon les règles ci-dessous, et tout complément
demande un nouveau devis. **Si le processus est tué** (borne de durée), la dépense reconstruite = dépense réglée au journal +
**pire cas de chaque appel commencé sans fin au journal** (le journal écrit un début avant chaque appel) ; pour Kimi, le journal du
relais sert de contrôle croisé (CL-10 a).

**Comparaisons** : aucune comparaison multiple décisive ; cinq critères lus séparément, chacun sur son seuil ; prédictions
rapportées tenues ou non tenues.

**Lisibilité (CL-07)** : L1 exige les 6 témoins traités ; L2 exige au moins 3 fiches traduites ; L3 « inutile en l'état » exige
les 8 fiches traitées (sinon, sans fiche utile, « non lisible ») ; L5 se lit sur les fiches traitées et est « non lisible » si
aucune fiche n'est traitée ; L4 se lit toujours. **Les prédictions de comptes (sorties et famille « pont ») ne se lisent que si
les 8 fiches sont traitées ; la prédiction d'accord, sur au moins 3 fiches traduites (comme L2) ; celle des témoins, si les 6
sont traités.** L'agrégat v2 code ces règles (`lisible`, `tenue` vide hors domaine) ; le lecteur neuf les vérifie.

**Rôles** : session-depot (valeur engagée, scellement, inscription et poussée, tirage, lancement du metteur en forme et contrôle
de sa transcription, scellement et inscription des témoins, lancement, consignation) ; sous-agent metteur en forme (témoins) ;
contre-lecteur neuf (R2) ; **lecteur neuf** (ni auteur de ce préenregistrement, ni du code, ni du lancement) qui applique les
critères gelés à `agregat-v2.json` (et `agregat-reprise-v2.json` s'il y a un tour neuf), fait l'audit de symétrie (R4) et écrit
la lecture agrégée. **conv-audit ne lit ni les fiches, ni les réponses, ni les fiches-lois** : il reçoit la lecture agrégée.
Lazar : GO (accordé), décisions D-P1 à D-P4 sur la suite.

**Ce que l'essai ne mesure pas** : la vérité des lois ; les parts sur la course 2 (autre format, autres axes) ; le pont sur des
fiches d'Argon ou de Kimi (aucune n'est éligible ici) ; l'indépendance des deux traducteurs au-delà de leur accord (deux
traductions peuvent partager une même lecture fausse : T1 et T2 en sont la seule mesure).

**Limites dites** : 8 fiches et 6 témoins, effectifs très petits ; tous les passages ont la même affectation. T1, T2, T3 et T6
nomment des objets du catalogue réel, ce que les fiches de la course 1 ne font pas. **Conséquence sur L1 (CL-03)** : T1 et T2
sont plus faciles qu'une fiche réelle (objets du catalogue nommés, un seul nombre, forme imposée) ; « dents » est une condition
nécessaire, jamais une preuve que le pont traduit fidèlement des fiches en texte libre ; « pas de dents » en est d'autant plus
informatif. Un traducteur qui devine une fiche de contrôle peut aussi changer de conduite (conscience d'évaluation, non mesurée
ici). T6 : voir le choix 13.

### Pièces gelées

Chemins depuis la racine du dépôt ; le lanceur refuse de tourner si l'une diffère (vérification sur disque, R11). Les pièces de
la version 1 (préenregistrement, tirage, lanceurs, consigne, essais v1) restent archivées, hors de ce tableau.

| pièce | SHA-256 | rôle |
|---|---|---|
| `donnees/epreuve-fraiche-pont-v1/pont/pont_v1.py` | `9fb2d9366e7764d4fc810b921e8565ca2dcae9af5f1b30ec8866efeb5d3eb692` | module du pont (conv-audit), inchangé |
| `donnees/epreuve-fraiche-pont-v1/pont/conception-pont-fiche-loi-v1.md` | `5161e199e15dacc728d4b2e7b1769f700e0a293c05fb26d402dfe40d25c4a974` | conception (fait foi) |
| `donnees/epreuve-fraiche-pont-v1/pont/test_pont_v1.py` | `4e31189b8eeaaa10b9af80637a518865426a2b6d910566ec691226e5e99e1f40` | essais du module (82 avec la v56) |
| `donnees/epreuve-fraiche-pont-v1/pont/LISEZMOI-pont-v1.md` | `7b1c131db760014798af159047849163bedc03b706f2f684dd0962ac4d6bd17a` | état du module |
| `donnees/epreuve-fraiche-pont-v1/entree/fiches-validees.json` | `a7068ba41ec4929edaedf28a5669a6f7d34773445dfad7295b6652085ce3b7f9` | fiches de la course 1 |
| `donnees/epreuve-fraiche-pont-v1/entree/classement.json` | `46cdfea8c458d22345b088a6d07d876d407dd7d22bb7aa80d3feb09a36fd9bbf` | éligibilité |
| `donnees/epreuve-fraiche-pont-v1/entree/lecture-complementaire-doublons-argon-v1.md` | `34bcdfa01fa05fc8558c97d76607ccca827fef0851282daf3a83353a03f7d36d` | idées distinctes |
| `donnees/epreuve-fraiche-pont-v1/catalogue-public-t05-v2-pont-v1.json` | `90f2440a966ad105867ac5fd04ead342e2d640ed9eef2759afa8fdfbd7eb1697` | catalogue servi |
| `donnees/epreuve-fraiche-pont-v1/noyau-pont-t05-v2-v1.json` | `4c07e7b46a4d239d8d34e4fbacb9a23de0a94097e1d0f79b6845c1deb106a44d` | état du noyau, jamais servi |
| `donnees/epreuve-fraiche-pont-v1/verite-temoins-v1.json` | `00030bb7ab72846de4426d3f6d1e42d775316eade92b24b0192402d929f8f429` | vérité des témoins, jamais servie (inchangée) |
| `donnees/epreuve-fraiche-pont-v1/consigne-metteur-en-forme-temoins-v2.md` | `255ca007001662c98b6b5aa1ab485d08ec50763a473dc4c82d31005ad5ae3a11` | consigne fermée des témoins (v2) |
| `donnees/epreuve-fraiche-pont-v1/tirer_fiches_v2.py` | `b61a9021db0a64a97236e1ea2f0acb275fdc9cd722f14abdb0bfc94d5c612d59` | tirage (v2 : inscription poussée, témoins en tête) |
| `donnees/epreuve-fraiche-pont-v1/lancer_epreuve_pont_v2.py` | `be3c43e61641ab91444c92714269651a0722f81362a46d20a6efce3825781f9f` | lanceur et agrégat (v2) |
| `donnees/epreuve-fraiche-pont-v1/lancer-epreuve-pont-v2.sh` | `c40b8527876e6a1231ecc292eb26e1c636279b98899101ceb934bf6c9f03d7b3` | lanceur shell (v2) |
| `donnees/epreuve-fraiche-pont-v1/test_epreuve_pont_v2.py` | `1a531edee5f7a22eae28fef9653bbccc2e1e1584e743440834cd1764353e25ba` | essais hors réseau (v2) |
| `donnees/epreuve-fraiche-pont-v1/contre-lecture-preregistrement-epreuve-pont-v1.md` | `b688ae1f8104efe013be91bf8b1f12f918b40fd77c4f6eeea62877291723ff81` | rapport de contre-lecture 1 |
| `donnees/espece-seule-v1/collisionneur_v7.py` | `c9725f025407c3ece3e8c16d19cfdfdec078f084a811f0a3b6ea3209be5d98dc` | appeler_gemini (sans reprise interne), appeler_kimi, coûts |
| `docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v3.py` | `d54ed2bce54f5c89e9f078d1a03b5d8159894d6565ae560c3601c1e63ca76239` | relais Kimi local |

Hors de ce tableau (pas sur `main`) : archive de l'orchestrateur v56, `CODE-orchestrateur-pole-v7-v56.zip`,
`29b1b38cfee5e279a06c947fdf1f855628b574e81e44c2d7e48a029151c1b24c`, tirée de la branche `origin/canal/conv-audit-n04` et vérifiée
par le lanceur shell avant dépliage.

## Critères de lecture gelés

| critère | issue observée | verdict | conséquence |
|---|---|---|---|
| L1 | ≥ 5 témoins justes sur 6, T1 et T2 justes | **dents** (HP1 confirmée) | — |
| L1 | sinon | **pas de dents** (HP1 réfutée) | aucun usage du pont en course 2 avant correction |
| L1 | moins de 6 témoins traités | non lisible | nouveau devis pour les témoins manquants |
| L2 | ≥ 3 fiches traduites et accord ≥ 0,6 | **fidélité** (HP2 confirmée) | — |
| L2 | ≥ 3 fiches traduites et accord < 0,6 | **ambiguïté élevée** (HP2 réfutée) | consigne du traducteur à revoir |
| L2 | moins de 3 fiches traduites | non lisible | lu avec L3 |
| L3 | une proposition refusée par la vraie garde v56 | **audit requis** avant toute lecture de L3 | anomalie du module (CL-10 c) |
| L3 | ≥ 1 fiche réelle en sortie 1 différée ou sortie 2 | **utile** (HP3 confirmée) | — |
| L3 | 0, les 8 fiches traitées | **inutile en l'état** (HP3 réfutée) | décision D-P1, options (b) ou (c) |
| L4 | 0 incident | **sûr** | — |
| L4 | ≥ 1 incident | **incident** | arrêt, enquête, aucune lecture des autres critères comme favorable avant l'enquête |
| L5 | aucune fiche traitée | non lisible | — |
| L5 | famille « pont » ≤ ⌊0,3 × n⌋ | **conforme** | — |
| L5 | au-delà | **consigne à revoir** | les réponses tronquées sont rapportées à part (CL-10 b) |

Combinaisons : le pont est **prêt pour la course 2** seulement si L1 « dents », L4 « sûr » et L5 « conforme » ; L2 et L3
qualifient l'usage (ambiguïté, utilité). « Pas de dents » l'emporte sur tout le reste. Une sortie 1 observée (impossible ici)
est une anomalie : audit avant toute lecture. Les prédictions de la section 2 sont rapportées « tenues », « non tenues » ou « non
lisibles » ; une prédiction non tenue n'est pas un verdict sur le pont, elle corrige les parts SUPPOSÉ de la conception.

**Symétrie (R4), en miroir (CL-01)** : déclenche le même audit **l'une quelconque** des issues suivantes. Côté propre : 6 témoins
justes sur 6 ; accord égal à 1,0 sur au moins 3 fiches traduites ; 8 fiches traduites sur 8. Côté sale : 0 témoin juste sur au
moins 3 traités ; accord égal à 0 sur au moins 3 fiches traduites ; 0 fiche traduite sur au moins 6 traitées. L'audit : entrées
distinctes par passage (empreintes des textes servis), réponses distinctes par rôle (empreintes), relecture des réponses brutes
des témoins (les nombres cités viennent-ils des champs cités ?), empreintes des pièces gelées. L'agrégat v2 code les six
déclencheurs (`audit_symetrie.declencheurs`) ; cette liste prime, le lecteur neuf la vérifie et conclut. Un critère tenu
exactement à son seuil est rapporté avec une réserve.

## Liste d'arrêt

| condition | action |
|---|---|
| préenregistrement non scellé, non conforme, ou pièce gelée modifiée ; GO absent, échu, révoqué ou d'un autre type | refus de lancer (aucun appel) |
| empreintes du préenregistrement scellé et de la valeur engagée non inscrites au registre, ou inscrites mais non poussées | refus de tirer (CL-02) |
| `fiches-tirees/` ou un témoin absent ; témoin hors gabarit, hors longueur, porteur d'une étiquette A4, d'une étiquette « T1 » à « T6 » ou d'un canari, ou qui ne transcrit pas sa description | refus de lancer |
| témoin non scellé, ou empreinte d'un témoin non inscrite au registre | refus de lancer (CL-09) |
| transcription du metteur en forme signalée (fichier interdit ouvert, ou commande hors de la vérification) | témoins jetés, réécrits par un nouveau sous-agent neuf |
| commit du dépôt illisible | refus de lancer (CL-11) |
| toute `LectureEpreuveInterdite` (clé d'épreuve dans le catalogue, métadonnée, canari dans l'entrée) | arrêt du tour avant tout appel du passage ; enquête |
| tout canari dans une réponse (N7, incident) | arrêt du tour ; enquête ; L4 « incident » |
| appel dont le pire cas dépasse ce qui reste sous 5 dollars cumulés | arrêt du tour (« plafond ») ; passages restants non lancés |
| coût lu au-dessus du pire cas réservé | arrêt du tour (« dépassement de réserve », CL-05) |
| trois refus (statut « REFUS » de l'API) | arrêt du tour ; tour neuf R-750 possible une fois, sauf réserve de R-750 |
| trois échecs techniques (deux échecs de transport chacun) | arrêt du tour |
| modèle servi différent du modèle demandé | réponse mise à l'écart, arrêt du tour (changer de modèle demande un GO) |
| borne du relais Kimi atteinte (plafond ou nombre d'appels) | arrêt du tour |
| toute autre erreur du module ou du lanceur | arrêt du tour, trace consignée, **aucun repli** |
| une clé trouvée dans une sortie | code 6 ; run invalide jusqu'à enquête ; clé à révoquer |

## Contre-lecture

- **Contre-lecture 1** — sous-agent neuf de session-depot (Opus 5.5, `claude-opus-5-5`), 2026-11-01, relevé `date -u` de 17:43 UTC ; brouillon relu `41dc127b278b3c4faf1fc22145a8d1492f43644d7721fb7e9275999409b23789` ; rapport `donnees/epreuve-fraiche-pont-v1/contre-lecture-preregistrement-epreuve-pont-v1.md`, `b688ae1f8104efe013be91bf8b1f12f918b40fd77c4f6eeea62877291723ff81` ; verdict « scellable après corrections » (13 constats : 5 moyens CL-01 à CL-05, 7 mineurs CL-06 à CL-12, 1 groupe de remarques CL-13 ; aucun bloquant ; aucune pièce gelée à changer) ; traitement de chaque constat (accepté, refusé et pourquoi) : **CL-01 accepté** — symétrie en miroir écrite mot pour mot (section « Critères de lecture gelés ») et codée en entier dans l'agrégat v2 (six déclencheurs) ; **CL-02 accepté** — inscription et poussée des deux empreintes avant le tirage, geste de session-depot, exigée par programme par `tirer_fiches_v2.py` (`--ref-poussee`) ; **CL-03 accepté** — conséquence sur L1 dite (« Limites dites ») ; pour T6, la consigne v2 interdit tout chiffre hors de « 3B:RIGOR » (classe en toutes lettres, banque non nommée), le lanceur le vérifie, la vérité de T6 reste N2 ou N9 et la faiblesse résiduelle (« 3 » de « 3B ») est dite (choix 13) ; **CL-04 accepté** — réserve de R-750, rappel des deux rôles au tour neuf, réponses du premier tour gardées et rapportées, contenu du préambule borné et gardé par programme (choix 10) ; **CL-05 accepté et vérifié** — `appeler_gemini` reprend par défaut aussi sur une coupure de connexion ; la v2 l'appelle avec `attentes=(0,)`, la seule reprise est celle du lanceur avec une nouvelle réservation au pire cas, et un coût au-dessus de son pire cas arrête le tour (choix 11) ; **CL-06 accepté** — signes réécrits ; **CL-07 accepté** — lisibilité complétée et codée ; **CL-08 accepté** — écarts complétés (a à d) ; **CL-09 accepté** — contrôle par programme de la transcription du sous-agent et de la transcription des descriptions dans les témoins, étiquettes « T1 » à « T6 » refusées, témoins scellés et inscrits exigés par le lanceur, concordance vérifiée par le lecteur ; **CL-10 accepté** — appels en cours comptés au pire cas (journal de début), réponses tronquées rapportées à part, refus de la vraie garde v56 = anomalie, audit avant L3 ; **CL-11 accepté** — commit, versions et paquets du Python des appels écrits et scellés dans le dossier du run avant tout appel ; **CL-12 accepté** — déclaration sur la valeur engagée ; ordre corrigé plutôt que seulement déclaré : témoins dans la première moitié (choix 14), probabilités 0,43, 0,69, 0,85 écrites ; **CL-13 accepté comme déclaration** — (a) `env -i` : pratique commune, conteneur à un seul utilisateur, correction prévue dans une version ultérieure (choix 16) ; (b) champ `eligible` signalé à conv-audit (choix 6). Conséquence : contrairement à « aucune pièce gelée à changer », les corrections CL-02, CL-03, CL-04, CL-05, CL-07, CL-09, CL-10, CL-11 et CL-12 sont codées dans des pièces neuves (`tirer_fiches_v2.py`, `lancer_epreuve_pont_v2.py`, `lancer-epreuve-pont-v2.sh`, `consigne-metteur-en-forme-temoins-v2.md`, `test_epreuve_pont_v2.py`) ; les pièces v1 restent archivées sans modification.
