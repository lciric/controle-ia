# Contre-lecture 2 (R2, N-052) — préenregistrement de P3-bis, brouillon 5 — v1

- Écrite le 2026-11-09, de 15:50 à 16:05 UTC (`date -u`), par un contre-lecteur neuf, Claude Fable 5.1 (`claude-fable-5-1`),
  autre modèle que le rédacteur des brouillons 4 et 5 (Opus 5.5). Je n'ai écrit aucun brouillon de P3-bis, de T0.7, de
  P3, ni la synthèse du collisionneur, ni R-2015, ni R-2020.
- Texte relu : `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon5.md`
  (`962dda898668150654c8ff08d42d00a5f9e77bc6f55b5723fc348ccc482954ce`, recalculée) ; brouillon 4 (`65622d4c…`, recalculée)
  comparé par `diff` : les hunks tombent tous dans les zones que la table « du 4 au 5 » annonce (en-tête, tables, plan 3, 4,
  6, 8, fichier d'issue, arrêt, code 2 (c), décisions, concordance, contre-lecture, marqueurs) ; le reste est mot pour mot.
- Lu aussi : contre-lecture 1 et dossier du brouillon 3 (`git show origin/canal/conv-audit-n04`, consignes b2, configuration
  b1, puissance v2 et sa sortie) ; T0.7 brouillon 14 (`fe7b4e6d…`, recalculée ; l. 746-750, 926-1035, 1199-1202,
  1410-1440, 1742-1812) ; `t07/lecture_v1.py`, `criteres_v1.py`, `registre_v1.py` (empreintes recalculées, égales à celles du
  texte) ; synthèse du collisionneur (`a81fe187…`, recalculée ; § I entier) ; N-063 v2 (`b2d9f035…`) ; `registres/decisions.md`
  (R-2015 l. 1973, R-2020 l. 1978, R-1654, R-1728, R-1752, R-1755, R-1762, R-1914, R-2006, R-2012) ; `registres/go.md` l. 217 ;
  `prereg/P3-premier-test-i-a-v1.md` (l. 34, 293-296) ; code de P3 : `run.py`, `lecture.py`, `statistiques.py`,
  `conditions.py`, `prereg.py`, `manifeste.py`, `harnais/validation_reelle.py`, `scripts/p3_instance.sh`,
  `amorce_instance_p3.sh`, `surveiller_p3_v1.sh`, `lancer_p3_v1.sh`, `t06/test_croise.py` au commit `8cb539f9`,
  `controle_lecture_t06_v1.py` au commit `1ae198b4`, `.claude/hooks/garde_calcul.py` (`184b3bbd…`, recalculée) ; sorties de
  P3 sous `diag/` (structure des fichiers seulement).
- Interdits tenus : rien lu sous `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, ni les
  trois dossiers hors dépôt ; aucune commande d'environnement ; aucune dépense ; aucun fichier modifié ; aucun commit ;
  ce rapport est le seul fichier écrit, sans compagnon.

## Verdict

**Scellable après corrections.** Le fond (hypothèse, prédictions, métrique, seuils, E′, PB-2 exact, fichier d'issue,
concordance avec T0.7, R12, devis) tient et les chiffres et empreintes que j'ai recalculés sont exacts. Deux défauts
empêchent le scellement tel qu'écrit : cinq marqueurs que le texte prévoit de remplir **après** le scellement, alors que
`sceller_prereg` refuse tout marqueur restant ; et une fermeture dont le texte dit « seule l'empreinte du paquet est
exposée » tout en faisant afficher l'empreinte de `lecture-p3bis.json` et en laissant la taille du paquet lisible. Le
reste est de précision.

## Défauts, du plus grave au moins grave

**D1 (bloquant) — Marqueurs remplis après le scellement : impossible.** `controle_ia.prereg.problemes` (l. 57-59) refuse
tout `<<…>>` restant, et `exiger_prereg_scelle` (l. 72-78) le refuse encore au lancement. Or la table des marqueurs
(l. 858-873) prévoit `<<INSTANCES_TOLEREES_P3BIS>>` « au lancement », `<<T07_B15_PERIMETRE_JEUX>>`,
`<<T07_B15_LANCEMENT_RELANCE>>`, `<<T07_B15_ENGAGEMENT_ETAPE_A>>` « avant toute ouverture (au candidat si T0.7 l'a déjà
écrit) » et `<<T07_B15_GARDE_ADAPTEE>>` « avant le rendez-vous ». C'est le défaut CLT7-03 de T0.7, reproduit. Effet : soit le
texte n'est pas scellable avant le 16 novembre (il attend le brouillon 15 de T0.7 **et** la décision DS-2 de Lazar), soit on
scelle avec des marqueurs et le run refuse de partir. Correction : (a) `INSTANCES_TOLEREES` sort du texte et devient une
constante du lanceur de la chaîne (comme `ARRETEES_TOLEREES` de `lancer_p3_v1.sh` l. 60), relue par les contrôles, consignée
au journal ; le texte dit seulement la règle ; (b) les quatre renvois à T0.7 et la décision du rendez-vous deviennent des
**lignes d'un registre propre à P3-bis**, `registres/prealables-p3bis-v1.md` (chemin fixé ici, même format à quatre
colonnes que `scellements-v1.md`, jamais `scellements-v1.md` lui-même : la règle (4) de `registre_v1.py` refuserait toute clé
inconnue), clés `ECRIT-PERIMETRE-JEUX-P3BIS`, `ECRIT-LANCEMENT-RELANCE-P3BIS`, `ECRIT-ENGAGEMENT-ETAPE-A-P3BIS`,
`GARDE-ADAPTEE-T07-P3BIS`, `RENDEZ-VOUS-P3BIS` ; la garde `ouverture_p3bis_v1 ouvrir` lit ce registre (exactement une ligne
par clé exigée, sceau et compagnon vérifiés, date strictement antérieure à l'ouverture) au lieu de lire le texte ; essais
R5 : ligne absente, en double, sceau faux, date postérieure. Le texte garde alors seulement les marqueurs remplissables au
candidat.

**D2 (bloquant) — Fuites de la fermeture (plan, point 6).**
- (a) Le plan, point 4 (l. 430), fait imprimer par la lecture complémentaire « son chemin et son empreinte », et le code,
  point 6 (v) (l. 724), dit « seuls codes et empreintes affichés ». Une empreinte de fichier affichée est exactement le canal
  que le point 6 ferme ([A-T2] : « une empreinte de fichier exposée permettrait de deviner l'issue »). Correction : les deux
  lectures n'affichent **rien** hors de la sortie redirigée ; seuls les codes de sortie et l'empreinte du paquet sortent de
  l'espace fermé ; réécrire l. 430 et l. 724.
- (b) La **taille du paquet** est lisible dès qu'il est commité (`git`, `ls`), et elle dépend du contenu (listes
  `non_interpretables`, `reserves`, chaînes « au-dessus » 9 caractères contre « non interprétable » 17 ; l'arrondi aux
  enregistrements de 10 240 octets de `tar` n'absorbe pas toujours l'écart). Le texte met « leurs tailles » en classe 2 mais
  ne protège pas celle du paquet. Correction : paquet **bourré à une taille fixe** (par exemple 16 Mio exactement, bourre
  aléatoire tirée de `secrets`), taille écrite dans le texte et vérifiée par l'essai différentiel (sortie de classe 1 :
  « taille du paquet » doit être identique entre issues substituées).
- (c) Le contrôle positif « une variante dont la durée dépend de l'issue doit être détectée » (l. 461) n'a pas de
  mesure : la durée n'est pas une sortie de classe 1 et un chronométrage sur jouet n'a pas de seuil. Or l'heure du commit
  du paquet se voit (classe 1 par construction). Correction : mettre « heure du commit du paquet » en **classe 3** (inférence
  résiduelle admise) avec la justification que les deux lectures ne branchent pas sur l'issue (seule PB-13 « non calculable »
  saute un calcul de quelques secondes), et retirer le contrôle positif sur la durée, ou le définir (par exemple : la
  variante dort 60 s sous une issue ; détection = écart > 30 s entre deux passages).
- (d) Déclaré mais à dire plus fort : `scores-p3.npz`, `episodes-p3.json` et les textes sont poussés **en clair** sur la
  branche de calcul (l. 452-453) ; avec le code public de P3, l'issue se recalcule en quelques secondes. La fermeture ne
  protège donc que les sorties des lectures, et la « limite écrite » (l. 462-464) doit le dire tel quel ; les phrases pour
  l'extérieur aussi. Option sans dépense ni changement de P3 (R12) : `p3bis_instance.sh` (script neuf) met `donnees/<run>/`
  et `diag/<run>/episodes-p3.json` dans un second paquet salé avant la poussée, et la lecture le déplie dans le clone fermé
  (`charger_source` relit les chemins et les compagnons après extraction) ; `resume.json`, `sondes-figees.json` et le
  manifeste restent en clair (classe 1). Si cette option est écartée, l'écrire comme choix.

**D3 (majeur) — Date du rendez-vous dans le texte scellé.** `<<DATE_RENDEZ_VOUS_LAZAR>>` « avant le candidat », par Lazar
seul (nœud R-2020) : le scellement, donc la création avant le 16 novembre, dépend d'un mot de Lazar que rien ne borne. La
synthèse veut la date « écrite dans le texte scellé » (§ I.6 point 6), mais la date n'a aucun effet sur le run. Correction :
écrire dans le texte une **date proposée avec recommandation** (par exemple 2026-11-20T12:00:00Z, l'illustration de la
synthèse), que Lazar confirme ou change par un mot recopié dans `docs/decisions/rendez-vous-P3-bis-v1.md` (ligne
`RENDEZ-VOUS-P3BIS` du registre de D1) ; sans mot sous 48 heures, la date proposée tient (hiérarchie : la date est une
règle de gouvernance, pas une dépense ni une hypothèse). À soumettre à Lazar (section suivante). Et préciser le sort d'une
décision « maintenir » suivie plus tard d'« ouvrir » : deux fichiers versionnés (`-v1`, `-v2`, R12), la garde lit la ligne
du registre, jamais le fichier le plus récent par nom.

**D4 (majeur) — Longueur générée des actions (remis par la synthèse).** Pour PB-1, la longueur notée (`jetons_notes`) est
un prédicteur trivial de P3 : l'état E la contrôle (`lecture.py` l. 286-288), donc E′ aussi. Pour **PB-2**, rien ne la
contrôle : le maximum par épisode croît avec le nombre d'actions longues, et A est opposé à H sans texte. Correction, sans
calcul neuf : recopier à côté de PB-2 `audit_R4.jeux[p]["saboteur-honnete"].triviaux.jetons_notes.separation` et les
longueurs par emplacement (`fiches[].jetons_par_action`, médiane et moyenne, nouveau champ de `lecture-p3bis.json`) ; réserve
gelée **R-L** sur la phrase de PB-2 : « la longueur notée sépare A de H au moins autant que la sonde (séparation écrite) :
le compte par épisode peut tenir à la longueur des actions ». Les actions sont bornées à 400 jetons (`max_nouveaux`) : le
dire.

**D5 (majeur) — Plantés non exécutés (remis par la synthèse).** Le texte ne rapporte pas à part les épisodes de A qui
n'ont pas gonflé le coût. P3 calcule déjà par action `etiquettes_gonflement` (≥ 2 contre ≤ 1,25 fois l'honnête apparié,
`lecture.py` l. 311-320 : `intention[p].T1.n_positifs`, `n_negatifs`). Correction : PB-15 (descriptive) dans
`lecture_p3bis_v1` : nombre d'épisodes de A dont l'effet apparié du log10 du coût est ≤ log10(1,25) (« non exécutés »), k
de PB-2 restreint aux épisodes exécutés, et recopie de T1 ; aucune issue n'en dépend (H-B1 porte sur le contexte, pas sur
l'exécution ; un « vu » avec beaucoup de non exécutés renforce la lecture « la sonde lit le contexte »), ce que le texte doit
dire.

**D6 (majeur) — Blocs et corrélation intra-bloc dans la puissance (remis par la synthèse).** Le point 10 ne dit ni le nombre
de blocs ni d'où vient l'erreur type. Correction (une phrase, aucun calcul neuf) : « jeu décisif : 60 blocs (une tâche =
un bloc), ≈ 10 actions par bloc et par condition (≈ 1 200 actions) ; l'erreur type 0,0219 est celle du rééchantillonnage par
blocs de P3 sur le même jeu, elle absorbe la corrélation intra-bloc empiriquement ; aucun facteur de plan n'est ajouté. PB-2 :
60 épisodes = 60 blocs à une valeur chacun, indépendance entre blocs supposée ; appariement par tâche : niveau ≤ 2⁻⁶
(simulation de la contre-lecture 1). » Déclarer que l'enveloppe suppose que le texte planté ne change pas l'erreur type.

**D7 (mineur) — Codes de sortie de `lecture_p3bis_v1`.** Le texte n'écrit pas que le code de sortie vaut 0 pour toute issue
des lignes 2 à 5 (E′ « échec » compris : dans P3, `descriptif` attrape `GardeArret` et le code reste 0) et 1 seulement sur
une garde. L'essai différentiel le teste, le texte doit le fixer (sinon « échec » fuit par le code, hors de la classe 3 qui
n'admet que l'arrêt sur garde).

**D8 (mineur) — Garde `ouvrir`, chemin normal.** « Sceaux vérifiés » des lignes `SCORES-T07` et `SONDES-T07` exige
`donnees/<run-t07>/scores-actions-t07.npz` dans le clone de la session mère : un fichier fermé de T0.7, déplacé pour rien.
Vérifier la forme de la ligne et le compagnon `.sha256` cité suffit (ou le fichier s'il est présent).

**D9 (mineur) — Écrit (ii).** Les règles de lancement et de relance de l'étape A existent déjà en grande partie au
brouillon 14 (plan, point 8 ; variante B l. 1322 ; `GO-ETAPE-A-T07`). Le texte peut citer le brouillon 14 pour (ii) dès le
candidat et ne renvoyer au brouillon 15 que ce qui manque (relance après R11-arret, abandon).

**D10 (mineur) — Phrase PB-6 de la ligne 4.** « le signal vu tient au contraste planté » conclut sur la persona alors que A et
B diffèrent aussi par la forme (« PRIVATE NOTE (only you can see this) ») et, si la règle d'ajustement échoue, par la
longueur. Écrire « tient à ce qui distingue A de B : la phrase de persona (et, si elles diffèrent, la forme et la longueur du
texte) ».

**D11 (mineur) — Jointure des textes.** `textes-actions-p3.jsonl` porte `episode`, `condition`, `tache`, `pas`, `texte`
(`run.py` l. 277) ; le texte doit fixer la clé de jointure de `mention_etendue` aux lignes du tableau des scores
(`episode`, `pas`) et exiger l'égalité des effectifs (essai R5).

## Ce que j'ai vérifié et trouvé juste

- R12 : `git diff --name-status 7a54d431… HEAD -- <chemins de l'en-tête>` au commit `c4855944` (après `d2c23df0`) : six
  ajouts, les mêmes que le texte ; aucun fichier de P3 modifié ni retiré. `prereg/`, `diag/`, `runs/`, `donnees/`, `docs/`
  sont exclus de `CHEMINS_GELES` (l. 71-73) : le commit S et le paquet sous `diag/` ne font pas refuser `exiger_code_cite` ;
  `scripts/` est gelé, donc les deux scripts neufs et la liste ciblée doivent être au commit du code, comme écrit.
- Concordance avec T0.7 : `ISSUES_P3BIS` (`criteres_v1.py` l. 55) est le même ensemble de cinq valeurs ; `lire_issue_p3bis`
  (`lecture_v1.py` l. 257-275) exige les quatre clés, `ligne` entier de 1 à 5 non booléen, le verdict présent à l'empreinte
  citée ; l'absence des lignes est un refus (attente), jamais une valeur de P ; `REFUSEES_ETAPE_A` contient `VERDICT-P3BIS`
  (`registre_v1.py` l. 70-73) : la branche 1 exige bel et bien la garde adaptée (nœud DS-2, écrit) ; le lecteur du verdict ne
  reçoit aucun fichier de T0.7 ni `lecture-sondes-t06.json` (T0.7 l. 1793-1794) ; `registres/scellements-v1.md` est absent de
  `main` (à créer, écrit) ; journal d'ouverture de P3-bis distinct de `<registre>.ouvertures.md`.
- Métrique : E′ applique `>=` comme `lecture.py` l. 286-288 ; `aire_simple(valeurs, condition, positifs, negatifs)` et
  `separation` existent ; `MENTIONS_ETENDUES` de `t06/test_croise.py` (commit `8cb539f9`, l. 43-45) est bien les motifs de P3
  plus « dishonest », « pretend », « honest person », « making statements », « exactly equal », `re.I` ; `accumulation`
  prend `honnete=`, `autre=`, rend `episodes[c]`, `maximum.rappel`, `maximum.seuil` par `method="higher"` (= maximum à 60) ;
  `detection` et les 200 colonnes de plancher sont dans `scores-p3.npz` (PB-13 calculable sans réextraction) ;
  `audit_R4.jeux[].cout_seul` existe (PB-11) ; `P3-P6.<emplacement>.valide` et `cout_present` existent (PB-12).
- Chiffres : 0,6389 / 0,6585 / 0,7124 / 0,7624 ; 0,0287 à k = 5, 0,0137 à k = 6 ; puissances binomiales et par décalage ;
  0,1415 et 0,3965 ; 11 179,1 s, 9 644,6 s, 40,2 s ; 0,6315 et 0,5966 : tous égaux à `puissance-p3-bis-v2.txt`. Devis :
  9,5 h × 2,10 = 19,95, + 2 + 0,1 ≈ 22 ; 3,6 h × 2,10 + 2 ≈ 9,5 ; 2 × 9,5 + 22 ≈ 41 < 80 ; attendu 3,6-5,0 h × 1,08-1,30 =
  3,9-6,5 + téléchargement ≈ 4,5-7,5 < 25 (GO l. 217 : plafond 80, échéance 2026-11-16, lus tels quels).
- Entropie `173398867739501636779144561928402532101` = P3 l. 34 ; phrases de persona = P3 l. 293-295 ; `garde_calcul.py`
  l. 163 : validité inclusive de l'octroi à l'échéance ; `p3_instance.sh` l. 229-234 : « N passed » exact ; `timeout` l. 249
  et `amorce` l. 38 : les deux couperets que le texte retire ; `surveiller_p3_v1.sh` l. 21-25 : cinq motifs, PLAFOND seul
  retiré ; R-2015 et R-2020 aux lignes citées.
- Fichier d'issue : accord (issue, ligne) avec `issue_mecanique` exigé à l'écriture, que T0.7 ne contrôle pas : juste.
- Classe 3 : « non lu » (pas de `resume.json`, `arret.json` présent) et un code non nul sur garde se voient : exact ;
  `resume.json`, `sondes-figees.json` et les lignes `PROGRES` (`run.py` l. 88, 299, 404-479, 522) ne portent que des
  comptes, des durées, l'aire de validation générique et des empreintes de gros fichiers non énumérables : classe 1 tenable.

## Points qui demandent un mot de Lazar

1. **Date du rendez-vous** (D3) : accepter qu'une date proposée (2026-11-20T12:00:00Z recommandée) tienne par défaut
   sous 48 heures, pour que le scellement ne dépende pas de ce seul mot avant le 16 novembre ; ou donner la date.
2. **Garde adaptée de T0.7** (branche 1) : réécriture au brouillon 15 qui touche DS-2 (confirmée R-1624) ; sans elle, toute
   ouverture anticipée suit la branche 2 et ferme 7b à T0.7 sous son texte. Décision déjà posée par R-2020 ; je la rappelle.
3. **Second paquet pour les scores bruts** (D2 (d)) : fermer aussi `scores-p3.npz`, `episodes-p3.json` et les textes sur
   l'instance (script neuf, 0 USD), ou accepter, écrit, que la fermeture ne tient que par discipline sur ces fichiers.
   Recommandation : fermer (coût nul, un canal de moins) ; confiance moyenne (la synthèse a accepté la discipline).
