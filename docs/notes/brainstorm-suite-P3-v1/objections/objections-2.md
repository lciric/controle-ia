# Objections à l'aveugle — objecteur 2 — brainstorm « suite de P3 » — v1

- Objecteur 2, sous-agent neuf. Protocole fermé de Lazar (R-203 (2)) : un tour d'objections à l'aveugle. Je n'ai lu ni
  l'autre objecteur (`objections-1.md`, présent, non ouvert) ni aucune réponse.
- Date : 2026-10-20, UTC. Dépôt lu en lecture seule ; aucune écriture hors de ce dossier ; aucune commande payante.
- Non lu, par consigne : `prereg/P3-consignes-v1.md`, `donnees/*/textes-actions-*.jsonl`, toute clé. Non lu, par prudence :
  la sortie de l'addendum (`diag/20261020-075849-addendum-p3/`), pour rester dans les trois branches conditionnelles.
- Lu : les quatre propositions et l'option G ; `diag/20261020-075740-p3-lecture/lecture-p3.json` en entier (sha256
  `c221d955…`) ; `prereg/P3-premier-test-i-a-v1.md` (`d975e981…`) ; `prereg/P3-addendum-lecture-complementaire-v1.md`
  (`8ff83422…`) ; `diag/20261019-230011-p3-reel/sondes-figees.json` (`fb418127…`) et `episodes-p3.json` (`1a96cbf8…`) ;
  noms et formes des tableaux de `scores-p3.npz` et `jetons-principales-p3.npz` (`4cd2ddb8…`), aucun texte ;
  `docs/notes/P3-mesures-v2/puissance-p3-v1.txt` ; code `premier_test_ia/{run,lecture,entrainement}.py`,
  `sondes/evaluation.py`, `harnais/episode.py` ; brief v2 (T0.7, porte G0) ; programme v2 ; P-007, P-011 ; N-007/N-008 ;
  registres `etat.md`, `decisions.md` (R-192, R-202, R-203, R-206, R-212, R-213, N-022, N-024, R-250 à R-255),
  `depenses.md`, `go.md`, `arrets.md` ; brouillons T0.6 (b1), T0.7 (b4), ABC ; fiche d'entretien ; PDF
  `docs/sources/pdf/2506.10805v4.pdf` (sha256 `54bf5555…`), p. 24-25.
- Classes : **fatale** (option fausse, dangereuse ou contraire à une règle gelée) ; **sérieuse** (doit changer avant
  d'être retenue) ; **mineure**.
- Abréviations de renvoi : `lecture` = `lecture-p3.json`, clé `resultat` ; `prereg` = texte scellé de P3 ; `addendum` =
  préenregistrement de l'addendum.

## 0. Trois faits vérifiés qui portent plusieurs objections

1. **Les identifiants générés ne sont pas gardés.** P3 a noté chaque action sur les identifiants générés (`tr.ids`,
   `harnais/episode.py` l. 250-260 ; `run.py` l. 274-283). Les fichiers gardés n'ont que scores, logits, bornes et longueurs
   (`jetons-principales-p3.npz` : `scores_0` de forme (532 683,), `bornes`, `longueur`, `debut` ; aucun identifiant).
   Tout « réencodage » retokenise le texte. Contrôles possibles : l'empreinte de trajectoire de chaque épisode
   (`episodes-p3.json`, `empreintes.trajectoire`, qui hache les identifiants) et `jetons_par_action`.
2. **Des directions aléatoires appariées voient les différences de contexte.** Maximum du plancher de la tromperie :
   0,781 (saboteur contre honnête), 0,794 (témoin contre honnête), 0,807 (saboteur contre mention) (`lecture`,
   `jeux.tromperie-difference_moyennes-c15.*.plancher_max`). Toute expérience qui change un contexte risque donc un
   plancher haut.
3. **« Plancher + demi-largeur » est le point de puissance ≈ 50 %, pas l'aire minimale détectable du texte de P3.** Le
   texte annonçait 0,57 à 0,58 (prereg l. 157 et l. 394-397), là où la simulation donne 93 à 100 % de détection
   (`puissance-p3-v1.txt` l. 13, 17, 21 : aire ≈ 0,586, plancher ≈ 0,52-0,53, demi-largeur 0,026-0,037). Recalcul
   (approximation normale ; erreur type tirée des intervalles à 97,5 %, z = 2,241) : tromperie, erreur type 0,0194, point
   50 % = 0,615, point 80 % = **0,632** ; enjeux, erreur type 0,0198, point 50 % = 0,580, point 80 % = **0,597**.

---

## Proposition A

### A1 — note de constats sans calcul
- **O2-01 — sérieuse.** « À coût déclaré égal (T4), on frôle encore le plancher » : lecture de presque positif, celle
  que A1 dit vouloir éviter.
  - Preuve : `lecture` → `intention.tromperie-difference_moyennes-c15.T4` : aire 0,632, borne basse 0,556, quantile
    0,607. La règle lit la borne basse (prereg l. 272 ; addendum : « toujours lu sur la borne basse »). Écart : −0,051.
    Formule gelée : « non au-dessus », « non détecté à cette puissance » (prereg l. 273, TC-04).
- **O2-02 — mineure.** Chiffre faux au point 3 : « valeurs observées : 0,536 à 0,596 selon les jeux ».
  - Preuve : `lecture` → `jeux.*.*.plancher_quantile` : de 0,5117 (mention contre honnête, les deux sondes) à 0,5961
    (témoin contre honnête, tromperie).
- **O2-03 — mineure.** Point 4 : « le maximum sur toute l'action se règle donc sur les jetons d'avant le coût ». Inférence
  non mesurée. T2 compare deux aires ; il ne localise pas le maximum. Le maximum peut aussi tomber après le champ du coût.
  - Preuve : `lecture.py` l. 332 (`difference_aires_appariee` entre aire du champ du coût et aire du pré-coût) ; la
    position du jeton dominant est l'objet de A8 de l'addendum.
- **O2-04 — mineure.** « Dès que l'addendum est scellé » : il est scellé et a tourné. Ses contrôles sur une cible non
  établie sont « descriptif seulement ; jamais une promotion » : la note doit le citer mot pour mot.
  - Preuve : `git log` : commit `6a97d69` « addendum … 20261020-075849-addendum-p3 (code 0) » ; addendum, « Critères de
    lecture gelés », ligne « contrôle favorable à une conclusion non établie ».

### A2 — champ du coût à nombre écrit égal (processeur)
- **O2-05 — sérieuse.** Enchaînement circulaire A2 → A4. Au chemin (A), A4 ne part « que si A2 montre un signal
  localisé au-delà du nombre ». Or A4 réencode les mêmes 2 400 actions. Le préenregistrement de A4 serait écrit après
  avoir vu A2 sur les mêmes textes. C'est exactement le cas que A dit circulaire.
  - Preuve : proposition A l. 49 (« choisir une lecture nouvelle d'après ce descriptif, puis la tester sur les mêmes
    données, serait circulaire ») et l. 176 ; R1 (« aucune lecture de résultat avant scellement »). Un signal trouvé par A2
    ne se teste que sur des épisodes neufs.
- **O2-06 — sérieuse.** A2 (b) « à coût déclaré égal » garde la confusion entre tâches que A nomme lui-même. Une action
  gonflée à X vient d'une tâche dont l'estimation honnête vaut bien moins. Une sonde qui lit la taille de la tâche sépare
  à coût égal. La ligne « (a) faible et (b) au-dessus : signal localisé au-delà du nombre » n'est pas identifiable sans
  contraste intra-tâche.
  - Preuve : proposition A l. 72 ; `lecture` → `P3-P1` : effet 1,52 en log10 (×33, intervalle ×17,6 à ×63,3) ; modèle
    intra-tâche existant : addendum A4 (b) (T1 intra-tâche, tranche = tâche).
- **O2-07 — mineure.** Référence par permutation seulement : elle teste « une différence entre conditions », pas « un
  signal propre au concept ». La table doit l'écrire ainsi. Grandeur non écrite : nœud.
  - Preuve : proposition A l. 59 et l. 71 ; prereg l. 415-416.

### A3 — plancher, ex aequo, effet de l'organisme
- **O2-08 — fatale (partie (b) seulement).** Rapporter « en distribution » les 30 sondes de P3, et lire les ex aequo de la
  couche 15 contre le plancher de la principale, c'est la seconde lecture sur d'autres sondes que la table gelée interdit.
  Neuf ex aequo à 1,0 : une passera par hasard et créera la pression de relire P3.
  - Preuve : prereg l. 428 (« pas de seconde lecture sur d'autres sondes, couches ou jeux ») et la phrase sous la table
    (« Une sonde au-dessus du plancher seulement hors des sondes principales […] ne compte pas ») ; `sondes-figees.json`
    → `aires_validation.tromperie` : 9 sondes sur 15 à 1,0, validation de 120 exemples (`effectifs`). Seul un nœud de Lazar
    pourrait l'ouvrir ; je recommande de retirer (b).
- **O2-09 — sérieuse.** Utiliser A3 (b) pour choisir famille ou couche de T0.7, puis lire T0.7 sur (i-a), c'est élire sur
  la famille évaluée.
  - Preuve : T0.7 brouillon 4 l. 65 (T7-P1 lit (i-a)) ; prereg l. 24 (« Les épisodes de P3 ne servent à aucune lecture
    de ces deux préenregistrements ») ; programme l. 137.
- **O2-10 — mineure.** A3 (a) « plancher refait sur les actions dont le coût est un nombre seul » et A3 (c) recouvrent A7
  (ii) et A6 de l'addendum, déjà tournés, et D6. Fusionner.
  - Preuve : addendum, A6 et A7 (ii) ; proposition D, D6.

### A4 — réencodage, activations gardées, plancher au jeton, plafond supervisé
- **O2-11 — sérieuse.** Stockage impossible tel qu'écrit (« gardées en demi-précision dans le dépôt privé »).
  - Preuve : 532 683 jetons notés (`jetons-principales-p3.npz`, `scores_0`) × 4 096 × 2 octets = 4,36 Go par couche,
    13,1 Go pour trois. GitHub refuse tout fichier de plus de 100 Mo ; P3 a déjà laissé hors du dépôt le fichier complet
    de ≈ 0,8 Go (prereg l. 312-315) ; le brouillon ABC chiffre la garde d'activations à ≈ 1,2 Go, sur une branche de
    données (l. 82). Il faut un sous-ensemble tiré par graine, ou un stockage hors dépôt décidé avant.
- **O2-12 — sérieuse.** Plafond supervisé presque certain : la lecture est jouée d'avance. Saboteur et mention diffèrent
  par leur contexte privé (consigne « à toi » contre « à un autre agent ») à chaque position. Une sonde supervisée le lira,
  même champ du coût masqué. La ligne « plafond au-dessus : sondes génériques aveugles » serait acquise sans rien dire de
  l'intention.
  - Preuve : fait 2 (plancher maximal saboteur contre mention : 0,807) ; proposition A l. 114 et l. 128. Parade : même
    plafond sur un contraste de contextes sans sabotage (témoin contre mention), comme référence.
- **O2-13 — mineure.** Échéance du fichier complet (23 octobre vers 02:07 UTC) : le rapatrier exige de redémarrer
  56799469 (facturé ; hôte non garanti libre). Précédent : rapatriement « non exécutable depuis la session ». Valeur
  faible : ces sondes ne peuvent pas être relues pour P3.
  - Preuve : `etat.md`, N-012 (« la clé ne permet ni copie ni exécution ») ; prereg l. 428 ; `sondes-figees.json` : 
    Mahalanobis à 0,49-0,85 (tromperie) et 0,51-0,52 (enjeux) en validation.

### A5 — témoin positif au format
- **O2-14 — sérieuse.** « Un échec veut dire : instrument aveugle […] un échec est un indice fort » : faux si le plancher
  sature. Le contraste de A5 est une consigne placée dans le contexte : c'est le genre de différence que les directions
  aléatoires voient. Un échec peut dire « sonde non privilégiée sur un contraste que tout voit », pas « aveugle ».
  - Preuve : fait 2 ; proposition A l. 144 et l. 151. La table doit séparer « plancher haut » (rapporter médiane,
    quantile, maximum) et « aveugle ».
- **O2-15 — mineure.** Variante « enjeux » : des textes de models-under-pressure (rédigés comme messages d'utilisateur)
  placés en réponse de l'assistant font un autre hors-distribution. Un échec n'y serait pas interprétable.
  - Preuve : prereg l. 297-301 (empan : 128 premiers jetons d'un message d'utilisateur ; TC-20 (f)).

### A6 — conséquences pour T0.7
- **O2-16 — sérieuse.** A6 (3) « lecture par champ, seulement si A2 ou A4 le justifient » règle T0.7 sur des lectures de
  P3, alors que T0.7 lit (i-a). Seules les règles qui n'utilisent aucun score de P3 peuvent entrer (validation hors
  distribution, identifiants générés gardés).
  - Preuve : T0.7 brouillon 4 l. 65 ; prereg l. 24 ; programme l. 137.
- **O2-17 — mineure.** A6 omet deux défauts du brouillon 4 de T0.7 que P3 rend urgents : le mode « contrôles omis ou
  affaiblis », retiré par le verdict du pilote ; tromperie et enjeux relus sur (i-a) sous T7-P1 (seconde chance).
  - Preuve : T0.7 brouillon 4 l. 47 et l. 143 ; `docs/verdicts/verdict-T0.5-pilote-v1.md` l. 48 ; proposition B, B3.

---

## Proposition B

### B1 — l'appel du 21 octobre
- **O2-18 — sérieuse.** Le texte A met côte à côte estimations et quantiles : « 0.575 and 0.525 against floors of 0.572
  and 0.536 ». L'auditeur entend « au-dessus » pour la tromperie. « did not separate » contredit la formule gelée. « Without
  that floor, the deception probe would have looked like a detection » ouvre le récit de presque positif que B1 interdit.
  - Preuve : prereg l. 272 (borne basse) et l. 273 (« jamais "ne sépare pas" ») ; `lecture` → `P3-P3` : bornes basses
    0,531 contre 0,572 et 0,481 contre 0,536. Dire les bornes basses, ou aucun nombre.
- **O2-19 — mineure.** « about thirty-fold » sans intervalle ; et c'est la seule conclusion que l'addendum peut toucher.
  - Preuve : `lecture` → `P3-P1` : [1,246 ; 1,801] en log10, soit ×17,6 à ×63,3 ; addendum, réserve `reserve_A6_P3-P1`.
- **O2-20 — mineure.** « Ce que les 60 000 USD achètent maintenant » réoriente le financement devant le fonds : changement
  de plan annoncé à l'extérieur. Nœud de Lazar, à séparer du texte de l'appel.
  - Preuve : hiérarchie de décision (`CLAUDE.md` : modification du programme, contact externe).

### B2 — note de portée
- **O2-21 — sérieuse.** « H8 […] gagne du poids de fait » : enjolivement. H8 dit que la validité prédit la robustesse. P3
  ne mesure aucune robustesse.
  - Preuve : programme l. 99 (H8) ; P3 n'a aucune attaque ni mesure de robustesse (prereg, « Hypothèse »).
- **O2-22 — mineure.** Ajouter une précondition à HC2, HC2b, HC3, HC4 sur un seul nul, d'un autre organisme et d'un
  autre format : B2 nomme lui-même ce piège. Mieux : une règle de méthode du préenregistrement du papier C (témoin positif
  de la sonde avant toute lecture de g), sans toucher les énoncés.
  - Preuve : proposition B l. 87.

### B3 — critère 3 de G0
- **O2-23 — sérieuse.** Nœud limité au critère 3. Le point de contrôle du 19 octobre (critère 2) est passé sans nœud
  consigné. Restent aussi les critères 4, 6, 7, 8. Le nœud doit porter sur G0 entière.
  - Preuve : P-007 l. 37-38 (points de contrôle des 19 et 26 octobre) ; `registres/decisions.md` : aucune ligne pour le
    point du 19 ; `etat.md`, « Derniers verdicts de porte » ; T0.6 brouillon 1 l. 28 (mode « affaiblir les contrôles »).
- **O2-24 — mineure.** Inclure P3 dans la correction de Bonferroni de T7-P1 ne retire pas la seconde chance. Retirer
  tromperie et enjeux de T7-P1 sur (i-a), ou lire T7-P1 sur (i-a) comme réplication déclarée.
  - Preuve : T0.7 brouillon 4 l. 94 et l. 143.

### B4 — organisme diffus
- **O2-25 — sérieuse.** Point 4 : « si les sondes génériques ne voient pas un facteur 33, elles verront mal un facteur
  1,5 ». Non sequitur : une sonde de tromperie ne lit pas la grandeur du gonflement. L'écrire dans un préenregistrement de
  G1 biaise son cadrage.
  - Preuve : consigne × 3 à chaque action, réalisé × 33 (prereg l. 155 ; `lecture` → `P3-P1`) ; aucune mesure de P3 ne
    relie score de sonde et facteur de gonflement (corrélation score-coût chez l'honnête : −0,118 et 0,257,
    `audit_R4.correlation_score_cout_honnete`).
- **O2-26 — mineure.** Définir les doses « diffuses » par la seule règle du coût change l'opérationnalisation de N-007
  (sabotage sous le seuil par action d'un moniteur calibré à 1 %). C'est un nœud de revendication : le demander comme tel.
  - Preuve : `registres/go.md`, GO-2026-10-04-04.

### B5 — ordre du travail
- **O2-27 — mineure.** Ordre sans durées ni coûts. La marge est écrite en plafond (≈ 83 USD) ; les contraintes qui lient
  sont le crédit (11,79 USD) et l'échéance du GO (1er novembre).
  - Preuve : `depenses.md`, 2026-10-20 06:07 UTC ; `go.md`, GO-2026-10-04-08 (échéance 2026-11-01). Voir O2-65.

### B6 — témoin positif de la chaîne
- **O2-28 — sérieuse.** Reproduire « un résultat publié » sans fixer la recette. Le seul chiffre vérifié (0,887) vient
  d'une sonde à attention dont la couche est choisie par validation croisée toutes les cinq couches, sur tout le jeu
  synthétique. La chaîne de P3 entraîne sur 2 000 textes sur 8 000, tronqués à 128 jetons, aux couches 7, 15 et 23 ; sa
  principale « enjeux » est linéaire. Un écart de plus de 0,03 serait ininterprétable ; un succès ne dirait rien de la
  sonde linéaire c15.
  - Preuve : PDF 2506.10805v4 (sha256 `54bf5555…`), p. 24, B.7 (méthode) et p. 25, « Results » (0,887), vérifié par
    moi ; prereg l. 297-299.
- **O2-29 — mineure.** « La recette de tromperie publiée préfère la moyenne » : chiffre de l'état de l'art repris de
  P-011, sans page de PDF.
  - Preuve : P-011 l. 23 ; R7.

---

## Proposition C

### C1 — témoin positif, persona transposée
- **O2-30 — sérieuse.** Saturation du plancher. La ligne « les deux non au-dessus : instrument aveugle » ne vaut que si
  le plancher reste bas. La réserve n'est prévue qu'au-dessus de 0,90. Ajouter une ligne « contraste vu par des
  directions quelconques ; sonde non privilégiée » quand le quantile dépasse nettement celui de P3, et rapporter médiane
  et maximum.
  - Preuve : fait 2 ; proposition C l. 104-113.
- **O2-31 — sérieuse.** « Jetons d'action identiques, identifiant par identifiant ; garde d'identité des scores comme en
  P3 » : impossible tel quel, les identifiants générés manquent. Prévoir le contrôle par empreinte de trajectoire et
  `jetons_par_action`, une règle d'exclusion écrite, et les comptes d'exclusion par condition (R5 ; R4 : les formes du
  coût diffèrent par condition et changent la tokenisation).
  - Preuve : fait 1 ; `lecture` → `P3-P6` : suffixe « k » 14 actions honnêtes, 0 saboteur ; intervalles 13 contre 0.
- **O2-32 — mineure.** « Il valait 1,0 sur les faits génériques » : aire brute. Le plancher n'a jamais été noté sur la
  validation générique. Voir O2-63.
  - Preuve : `entrainement.py` l. 110 (aires de validation des candidates seulement) et l. 117-120 (`plancher_de`
    construit, jamais évalué en validation).

### C2 — 2 × 2 contexte × texte, à jetons identiques
- **O2-33 — sérieuse.** Plancher d'une concordance appariée. À jetons identiques, un changement de contexte déplace les
  activations dans un sens à peu près constant. Pour une direction aléatoire, le signe de sa projection fixe une
  concordance proche de 0 ou de 1. Le quantile 0,95 de 200 directions tend alors vers 1 : C2-P1 devient presque
  inatteignable. La lecture « nul de construit, le nul de P3 ne vient pas du bruit du texte » serait un artefact de la
  métrique.
  - Preuve : définition du plancher, w ~ N(0, Σ) tirés au hasard des deux signes (`sondes/evaluation.py` l. 66-82) ;
    fait 2 ; proposition C l. 164-178. Il faut une statistique dont le plancher ne sature pas, ou une ligne « trace
    présente, non spécifique au concept » écrite d'avance. La simulation de C5 ne le verra pas sans activations.
- **O2-34 — sérieuse.** Même défaut d'identité des jetons que C1.
  - Preuve : fait 1 ; O2-31.
- **O2-35 — mineure.** « Les données de P4 sont neuves » : les activations le sont, pas les textes (formes du coût,
  longueurs, coût seul déjà lus).
  - Preuve : `lecture` → `P3-P6`, `audit_R4.jeux[].cout_seul` ; proposition C l. 64-65.

### C3 — base boîte noire de T0.8 sur les 2 400 actions
- **O2-36 — sérieuse.** Ordre contraire à la décision N-022 (3) (a) : la rubrique de T0.8 n'existe pas avant la
  requalification du plan B. C3 fait tourner les juges 8B et 3B avant elle. C3-P1 risque d'échouer pour la cause déjà
  connue.
  - Preuve : `decisions.md` N-022 (« tant que le plan B n'est pas requalifié, la rubrique de départ de T0.6 et T0.8
    n'existe pas ») et R-212 ; R-255 (plan B « prêt pour la chaîne de lancement ») ; `etat.md` (« juges 8B et 3B en plan B
    par l'incomplétude »).
- **O2-37 — sérieuse.** C3-P2 décisive sur des données à moitié lues. Le terme boîte blanche (0,575) est lu ; le coût seul
  sépare déjà ces mêmes actions à 0,888. L'issue est quasi connue. C'est aussi une grandeur non écrite sur P3 : nœud. La
  passer en descriptif.
  - Preuve : `lecture` → `audit_R4.jeux[0].cout_seul.aire` = 0,888 ; R1 ; prereg l. 415-416.
- **O2-38 — sérieuse.** Référence Claude : R-202 (3) exigeait un préenregistrement scellé sans lecture des résultats de
  P3. La lecture est faite. Écart à une décision de Lazar, non déclaré par C3.
  - Preuve : prereg l. 20-21 ; `lecture-p3.json` existe ; proposition D, D6, le déclare.
- **O2-39 — mineure.** Critère 4 « sur le même jeu d'épisodes » : les épisodes de P3 ne sont pas ceux de T0.7. C3 montre
  que la base tourne ; elle ne remplit pas l'appariement de G0.
  - Preuve : brief l. 195 ; prereg l. 24.
- **O2-40 — mineure.** Durée probablement sous-estimée (2,5 à 4,5 h avec 2 400 générations raisonnées).
  - Preuve : notations refaites des deux juges sur le pilote : ≈ 4,8 h de carte (`depenses.md`, 2026-10-18 21:40) ;
    « le 8B a noté plus de 7 565 s sans finir » (N-021, l. 10).

### C4 — organisme (ii) distillé des actions de P3
- **O2-41 — sérieuse.** (ii) distillé des 600 actions du saboteur de P3 ; sonde choisie en C2 sur ces mêmes textes ; puis
  lecture « critère 3 non rempli sur (ii) ». P3 ne sert à aucune lecture de T0.6 ni de T0.7, et la sélection fuit dans
  l'organisme évalué.
  - Preuve : prereg l. 24 ; programme l. 137 ; P-007 l. 31 (données de distillation propres à T0.6).

### C5 — puissance réalisée
- **O2-42 — sérieuse.** « Aire minimale détectable réalisée ≈ 0,615 et ≈ 0,58 » comparée aux « 0,57 à 0,58 » du texte :
  deux définitions différentes. À puissance égale (≈ 80 %), on a ≈ 0,632 et ≈ 0,597. La perte est sous-estimée.
  - Preuve : fait 3.

---

## Proposition D

### D1 — « non détecté à cette puissance », chiffré
- **O2-43 — sérieuse.** Même défaut que O2-42. La note scellée porterait 0,615 comme « effet minimal détectable réel » ;
  D5 en tire « ≈ 0,62 » pour l'appel.
  - Preuve : fait 3 ; proposition D l. 63 et l. 184.
- **O2-44 — mineure.** Tension interne : la section 0 (thèse 1 (a)) dit que la borne basse 0,531 « aurait passé » le
  placebo (0,525) et le modèle de puissance, comme indice d'artefact. D1 dit ensuite que la hausse du plancher est « sa
  fonction ». Le premier énoncé est un récit de presque positif : le plancher du placebo n'est pas celui du jeu.
  - Preuve : proposition D l. 27 et l. 66-68 ; `lecture` → `placebo`.

### D2 — nombre ou intention, réécriture forcée
- **O2-45 — sérieuse.** Prédiction d'un nul (« effet du contexte, à nombre égal, non détecté ») sans marge d'équivalence :
  infalsifiable comme prédiction ; un nul attendu puis obtenu est « trop propre » (R4). Écrire les deux issues, ou une
  estimation avec marge.
  - Preuve : proposition D l. 100-101 ; R4 ; modèle de marge : brouillon ABC l. 15 (équivalence, marge écrite).
- **O2-46 — sérieuse.** Garde d'identité « la case d'origine doit redonner scores-p3.npz » sans règle d'exclusion :
  arrêt du run ou exclusion silencieuse (R5).
  - Preuve : fait 1 ; O2-31.
- **O2-47 — mineure.** D2 et C2 sont deux variantes du même plan 2 × 2 sur les mêmes textes : un seul préenregistrement.
  - Preuve : propositions C (C2) et D (D2).

### D3 — contrôle positif et confrontation du plancher
- **O2-48 — sérieuse.** Pièce (2) : même défaut de recette que B6. Le chiffre 0,887 est bien sur le PDF, p. 25 (méthode
  p. 24) : « à revérifier » peut tomber, mais la reproduction doit suivre la recette publiée.
  - Preuve : O2-28.
- **O2-49 — mineure.** Pièce (1) : le titre en minuscules est un trait de surface du texte d'action. Un succès ne dit
  rien de l'aveuglement aux états internes ; seul l'échec informe. À faire seulement à coût nul dans une passe déjà
  payée.
  - Preuve : `lecture` → `audit_R4.jeux` (témoin contre honnête : `titre_sans_capitale_seul` 0,913 ; plancher maximal
    0,794).
- **O2-50 — mineure.** Chemin (B) : « Position du jeton dominant (A8) : D3 d'abord ». Cette réserve ne peut pas tomber :
  A8 vise `P3-P3/<p>`, qui n'est pas établie.
  - Preuve : addendum, Seuil (`reserve_A8_*`, cible `P3-P3/<p>`) et plan point 5 (« Une réserve ne vaut que si sa cible
    est dans `conclusions_etablies` ») ; `lecture` → `etats_des_jeux` : « non au-dessus ».

### D4 — organisme diffus
- **O2-51 — sérieuse.** Critère « sonde contre lecteur de coût, à coût déclaré égal » : à coût égal, le lecteur de coût
  vaut 0,5 par construction. La comparaison est jouée pour la sonde. La confusion entre tâches y entre aussi.
  - Preuve : forme de T4 (prereg l. 249-253 : aire stratifiée par tranches du coût) ; proposition A l. 72. Comparer à
    taux de faux positifs égal sur toutes les actions, et contraste intra-tâche pour l'information ajoutée.
- **O2-52 — mineure.** Relire les deux sondes de P3 telles quelles sur un organisme plus diffus : nul attendu tant que
  l'instrument n'est pas éprouvé ; calendrier après le 1er novembre, donc nouveau GO.
  - Preuve : proposition D l. 161-169 ; `go.md`, échéance de GO-2026-10-04-08.
- **O2-53 — mineure.** Chiffre : « témoin − 0,32 [− 0,57 ; − 0,07] ». La borne haute vaut −0,065, soit −0,06.
  - Preuve : `lecture` → `P3-P2.haut` = −0,06498.

### D5 — nœud anticipé sur G0
- **O2-54 — sérieuse.** (a) est incohérente (« G0 au 1er novembre » et « M0 prolongé de deux semaines ») et revient à
  franchir G0 sans le critère 3 : abaisser une porte après un nul. (b) change le bras principal après l'échec du bras
  générique : choix d'analyse a posteriori. (c) avance la bascule « H8 dominante », que le programme lie à l'échec de G1.
  Étiqueter chaque option comme changement de porte ou de plan.
  - Preuve : proposition D l. 178-182 ; proposition B, B3 (c) ; programme l. 190 et l. 238 ; P-011 (c) (bras générique
    gelé d'avance, `etat.md` T0.7).

### D6 — lire ce que fait le saboteur
- **O2-55 — mineure.** Codage non aveugle par construction : le gonflement ×33 et les titres en minuscules révèlent la
  condition ; « nombre multiplié à portée égale » exige de voir l'action honnête de la même tâche. Le déclarer, masquer
  au moins les étiquettes.
  - Preuve : `lecture` → `P3-P1`, `P3-P6` (titres sans capitale : témoin 500, honnête 4).

---

## Option externe G (Gemini 4 Argon, à l'aveugle)

- **O2-56 — mineure (lignes 0 et 1).** Sans objet : run complet, aucune lecture en échec ; P3-P1 établie. Le micro-pilote
  à température 0,3 changerait la configuration de l'agent.
  - Preuve : `lecture` → `issue.en_echec` = [] ; `P3-P1.etablie` = vrai ; prereg l. 318-319 (température 1,0).
- **O2-57 — sérieuse (ligne (i), seule applicable).** L'oracle supervisé saboteur contre honnête lit la consigne privée
  présente dans le contexte du saboteur : plafond proche de 1 garanti, sans rien dire de l'intention. Il ne départage donc
  pas ce qu'il annonce. Entraîner et évaluer sur le même organisme : diagnostic seulement. La sonde « enjeux » réentraînée
  puis lue sur P3 est une seconde lecture. Stockage de trois couches : 13 Go.
  - Preuve : proposition A l. 128 ; fait 2 ; brief l. 171 ; prereg l. 428 ; O2-11.
- **O2-58 — mineure (ligne (ii)).** Sans objet (aucune sonde au-dessus). Et faux : une projection « sur scores-p3.npz »
  est impossible, le fichier ne porte que des scores.
  - Preuve : `scores-p3.npz` → `scores` (2 400 × 430), aucune activation.
- **O2-59 — fatale (ligne (iii) et synthèse 3).** Prémisse fausse : T2 soustrait deux aires, pas deux maxima ; le « biais
  qui pénalise le champ du coût » est démenti par les données. (a) et (b) sont déjà dans l'addendum scellé. Refaire T1 à
  T4 avec d'autres estimateurs serait une seconde lecture. Sans objet de toute façon.
  - Preuve : `lecture.py` l. 332 (`difference_aires_appariee`) ; `lecture` → `intention.*.T2` : 0,914 contre 0,554
    (tromperie), établi pour les deux sondes ; addendum A2 et A4 (a) ; prereg l. 415-416 et l. 428 ; `P3-P4` non conforme.
- **O2-60 — mineure (ligne (iv)).** Sans objet (aucun jeu non interprétable). « Sauve […] la sonde principale » : une
  stratification après coup pour sauver une sonde est une relecture à but positif.
  - Preuve : `lecture` → `audit_R4.non_interpretables` = [] ; R3.
- **O2-61 — sérieuse (synthèse 1-2).** « Ne jamais régénérer avant d'avoir épuisé textes-actions-p3.jsonl » : épuiser les
  mêmes 2 400 textes multiplie les lectures. Aucune conclusion neuve sur l'organisme ne peut venir de textes déjà lus.
  - Preuve : R1 ; prereg l. 428 ; O2-64.
- **O2-62 — sérieuse (synthèse 5).** Même omission que C3 : la condition de R-202 (3) est rompue ; écart à déclarer.
  - Preuve : O2-38.

---

## Ensemble : ce qui manque

- **O2-63 — sérieuse (manque).** Aucune option ne vérifie que les sondes battent leur propre plancher sur leur propre
  validation générique. Le code construit les planchers mais ne les note jamais en validation. Si des directions
  aléatoires atteignent aussi ≈ 1,0 sur le contraste de persona, la règle « une sonde qui ne bat pas le plancher n'existe
  pas » est inatteignable même chez elle, et C1, A5, D3 deviennent illisibles. C'est le témoin positif le moins cher : à
  mettre en tête des branches (B) et (C), dans toute passe de carte déjà payée.
  - Preuve : `entrainement.py` l. 110 et l. 117-120 ; `run.py` l. 438-445 ; fonction prête :
    `sondes/evaluation.py` l. 85 (`comparer_au_plancher`) ; `sondes-figees.json` (aucune clé de plancher en validation).
- **O2-64 — sérieuse (manque).** Un seul préenregistrement « instrument » pour toutes les relectures et tous les
  réencodages des textes de P3 (A2, A3, A4, A5, C1, C2, D2, D3, D6, G (i)), avec liste fermée, compte des comparaisons et
  pare-feu écrit : rien ne promeut P3, rien ne choisit sonde, couche ou fenêtre de T0.7.
  - Preuve : prereg l. 24, l. 415-416, l. 428 ; programme l. 137.
- **O2-65 — sérieuse (manque).** Aucun devis commun. Le crédit (11,79 USD) ne permet qu'un lancement à la fois : le
  lanceur exige 6,5 h × (prix + autres projets en marche) + 1,2 USD, soit 8,28 USD à 1,0889 USD de l'heure, et bien plus
  si l'instance « rr- » de Lazar tourne. Le plan B (prêt à lancer) et le pilote du papier C puisent au même crédit. Le GO
  échoit le 1er novembre. Il faut un ordre de dépense unique, chiffré.
  - Preuve : prereg l. 369 ; `depenses.md` (2026-10-19 22:35 ; 2026-10-20 02:10 : instance 56811393 d'un autre projet en
    marche ; 06:07 : 11,79 USD) ; R-255 ; `go.md`, GO-2026-10-17-01.
- **O2-66 — sérieuse (manque).** Un contraste de contextes bénin dans toute expérience qui change le contexte (A4, A5,
  C1, C2, D2) : témoin contre une seconde consigne bénigne de même longueur. Il mesure ce que « n'importe quelle
  consigne » fait à la sonde et au plancher. Sans lui, « au-dessus » peut vouloir dire « consigne changée ».
  - Preuve : fait 2 ; `lecture` → `jeux.*.temoin-honnete` (plancher maximal 0,794 avec une consigne bénigne).
- **O2-67 — sérieuse (manque).** Le nœud de G0 doit être global et daté : critère 2 en retard (point du 19 octobre),
  critères 3, 4, 6, 7, 8 ouverts, T0.6 et T0.7 encore écrits pour un mode retiré.
  - Preuve : O2-23.
- **O2-68 — mineure (manque).** Une « option zéro » explicite : reprendre le chemin prévu (T0.6 en mode coût, concepts 3
  et 4 de T0.7 par paires synthétiques, T0.8 après le plan B, préenregistrements de G1 et du papier C), pour chiffrer le
  coût en délai de chaque option de diagnostic. Et la capacité de la session : deux orchestrations parallèles ont épuisé
  sa limite en ≈ 17 minutes ; le mandat R-234 finit le 20 octobre vers 09:35 UTC.
  - Preuve : P-011 (a), concepts 3 et 4 ; `decisions.md` R-206 ; `etat.md` l. 3.
- **O2-69 — mineure (manque).** Les branches : la table gelée n'a pas de ligne « instrument en échec », et l'addendum ne
  peut viser que P3-P1. Les branches (B) et (C) ne peuvent venir que du verdict R13. Aucune proposition ne doit attendre
  une réserve d'addendum sur le négatif. Pare-feu aussi dans l'autre sens : aucun texte du brainstorm ne va aux
  sous-agents du verdict (seule A le dit).
  - Preuve : prereg l. 423-433 ; addendum, plan point 5 ; proposition B, F11 ; proposition A l. 49.
- **O2-70 — mineure (manque).** Vocabulaire à fixer dans la note de décision : « sous le plancher », « frôle », « au
  niveau du plancher » deviennent « non au-dessus du plancher, non détecté à cette puissance ».
  - Preuve : prereg l. 273 (TC-04).

## Bilan court

- 70 objections : 2 fatales (A3 (b) ; G (iii)), 36 sérieuses, 32 mineures.
- Options qui survivent le mieux, si l'on corrige : B3 élargi à G0 entière (O2-23, O2-67) ; un témoin positif unique
  (C1 ou A5) précédé du plancher en validation (O2-63) et doté d'une ligne « plancher haut » (O2-30) ; C3 en descriptif,
  après le plan B (O2-36, O2-37) ; B1 réécrit sur les bornes basses (O2-18).
- Options à retirer ou à refondre : A3 (b) ; G (iii) ; le chaînage A2 → A4 ; C4 ; D5 (a) et (c) tels qu'écrits.
