# Contre-lecture 3 (R2, N-052) — préenregistrement de P3-bis, brouillon 6 — relecture courte de l'écart au brouillon 5 — v1

- Écrite le 2026-11-09, de 16:58 à 17:20 UTC (`date -u`), par un contre-lecteur neuf, Claude Fable 5.1 (`claude-fable-5-1`),
  autre modèle que le rédacteur des brouillons 4 à 6 (Opus 5.5). Je n'ai écrit aucun brouillon de P3-bis, de T0.7 ni de P3,
  ni la contre-lecture 2, ni la synthèse du collisionneur, ni R-2015, R-2020 ou R-2021. Marqueur : `CONTRE_LECTURE_3_P3BIS`.
- Texte relu : `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon6.md`
  (`aeb1f63a9e391c689e5b1ec4df6ae5ba0d2f309119949e0a0171f2e09d0fb9db`, recalculée) ; brouillon 5
  (`962dda898668150654c8ff08d42d00a5f9e77bc6f55b5723fc348ccc482954ce`, recalculée) comparé par `diff -u` : 21 hunks, tous
  dans les zones que la table « constats de la contre-lecture 2 et traitement » annonce (en-tête, tables, PB-15, métrique,
  plan 1, 3, 4, 5, 6, 8, 10, critères ligne 4, réserves, liste d'arrêt, code 2 (b) et (c), 5, 6, décisions, concordance,
  contre-lecture, marqueurs) ; le reste est mot pour mot.
- Lu aussi : contre-lecture 2 (`f12d7f21…`, recalculée, entière) ; R-2021 (`registres/decisions.md` l. 1979) et R-2023
  (l. 1981) ; T0.7 brouillon 15 (`7ed234bf5144a08036c6d41d452d89aad79e4cadc96adee24f0caf05fa28c0e2`, recalculée ; section
  « Écrits exigés par P3-bis », l. 1115-1312) ; `src/controle_ia/prereg.py` (entier, exécuté sur le brouillon 6) ;
  `src/controle_ia/t07/registre_v1.py` (l. 18-72) ; `premier_test_ia/run.py` l. 275-292 ; `statistiques.py` l. 32-46,
  173-196 ; `lecture.py` l. 305-325 ; `docs/procedures/P3-premier-test-v2/lancer_p3_v1.sh` l. 58-63.
- Interdits tenus : rien lu sous `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ;
  aucune commande d'environnement ; aucune dépense ; aucun fichier modifié ; aucun commit ; ce rapport est le seul fichier
  écrit, sans compagnon.

## Verdict

**Scellable après corrections.** Les onze constats de la contre-lecture 2 sont traités comme la table l'annonce ; les douze
marqueurs restants sont tous remplissables au plus tard au candidat ; le registre des préalables et la garde `ouvrir` sont
cohérents entre eux ; la date du rendez-vous est écrite avec son défaut ; P3 est intact. Deux défauts majeurs, tous deux
sur la fermeture et sur une phrase, doivent être corrigés avant le candidat : la taille fixe de 16 777 216 octets est
**inatteignable par une archive `tar`** (le texte arrêterait toute fermeture), et la mention de repli du marqueur de la
garde adaptée **contredit la garde** qui lit le registre. Un canal résiduel de l'issue reste ouvert par la compression de
`git` ; remède à coût nul.

## Défauts, du plus grave au moins grave

**D1 (majeur) — 16 777 216 octets n'est pas une taille d'archive `tar` (l. 503-505, 754, 804).** GNU `tar` et le module
`tarfile` de Python terminent toute archive sur un multiple de l'enregistrement de 10 240 octets (`RECORDSIZE`, constante
du module, quelle que soit la taille de la bourre) ; 16 777 216 = 1 638 × 10 240 + 4 096. La garde « taille autre que
16 777 216 octets → arrêt de la fermeture » (l. 753-754) se déclencherait à chaque passage, l'essai différentiel ne
passerait jamais, et corriger le nombre après le scellement serait un écart (nœud). Correction : écrire une taille multiple
de 10 240 (par exemple **16 783 360 octets** = 1 639 × 10 240, ou 16 773 120 = 1 638 × 10 240), aux trois endroits, et
dire que la bourre est calculée pour que l'archive close atteigne exactement cette taille.

**D2 (majeur) — Mention de repli du marqueur de la garde adaptée contre la garde `ouvrir` (l. 921-925, 991 ; contre
l. 596-606).** Si Lazar n'a pas répondu au candidat, le marqueur reçoit « branche 1 fermée sous ce texte ; toute ouverture
anticipée suit la branche 2 ». Mais la branche 1 est décidée par la garde sur la seule présence de la ligne
`GARDE-ADAPTEE-T07-P3BIS` du registre, « jamais le texte de ce préenregistrement » (l. 565-566), et le même paragraphe dit que
cette ligne « cite ensuite le texte scellé de T0.7 qui porte la garde, s'il existe ». Si Lazar accorde DS-2 après le
scellement de P3-bis et que la ligne est inscrite, le texte scellé dit « fermée » et la garde ouvre : contradiction interne
sur un nœud de Lazar. Correction (une phrase) : la mention de repli devient « aucun mot de Lazar au candidat sur DS-2 : la
branche 1 n'existe que si la ligne `GARDE-ADAPTEE-T07-P3BIS` est inscrite avant la décision « ouvrir » ; sinon toute
ouverture anticipée suit la branche 2 », aux l. 923-924 et 991.

**D3 (majeur, fuite résiduelle) — La taille fixe ne ferme pas la taille comprimée (l. 503-508, 530-531).** `git` stocke
chaque objet comprimé par `zlib` ; la bourre tirée de `secrets` est incompressible, les fichiers de lecture (JSON, sorties)
ne le sont pas. La taille de l'objet (fichier sous `.git/objects/`, paquet de `git`) vaut donc ≈ taille fixe − gain de
compression des JSON, et ce gain dépend du contenu (listes `non_interpretables`, `reserves`, chaînes d'état) : c'est le canal
de D2 (b) de la contre-lecture 2, réouvert à l'échelle de quelques octets à quelques centaines. L'essai différentiel ne le
voit pas : « taille du paquet » est la taille non comprimée. Correction à coût nul : (i) mettre les sorties des lectures dans
une archive comprimée (`tar.gz` ou `.xz`) **à l'intérieur** du paquet, à côté de `sel.txt` et de la bourre, de sorte que le
corps du paquet soit incompressible de bout en bout et que la taille comprimée ne dépende plus que de la taille fixe (au bruit
de `deflate` sur des octets aléatoires près, sans rapport avec l'issue) ; (ii) ajouter à la classe 1 de l'essai différentiel
la longueur de `zlib.compress(paquet)` (ou la taille de l'objet écrit par `git hash-object -w`), à comparer entre issues
substituées à quelques octets près, écart déclaré.

**D4 (mineur, concordance) — « Seules `issue` et `ligne` sont exposées » (l. 600-601, 690-692) contre le fichier d'issue
commité entier.** Sous la branche 1, le fichier d'issue est commité (point 7, l. 544-545) ; il porte quatre clés (l. 684-687),
dont `verdict_sha256` : cette empreinte est exposée, de fait, avec l'issue. T0.7 brouillon 15 le relève (l. 1299-1302,
réserve (1)) et demande que « les deux textes disent la même chose ». Correction : écrire « seules `issue`, `ligne` et
l'empreinte du verdict en prose (`verdict_sha256`, non reconstructible par dictionnaire) sont exposées ; le verdict en
prose reste fermé », aux deux endroits.

**D5 (mineur, concordance avec T0.7 brouillon 15, écrit après le brouillon 6).** Le brouillon 15 (`7ed234bf…`, 16:10-16:19
UTC, R-2023) existe ; le brouillon 6 (16:03-16:10) ne pouvait le citer. À l'écriture du candidat : (a) la section
« Concordance » (titre l. 927 ; l. 939-940 « à écrire au brouillon 15 ») doit citer le brouillon 15 par chemin, empreinte et
sections (a), (b), (c), que les trois lignes d'écrit peuvent dès lors citer ; (b) le brouillon 15 nomme les renvois de P3-bis
par les anciens marqueurs `T07_B15_PERIMETRE_JEUX`, `_LANCEMENT_RELANCE`, `_ENGAGEMENT_ETAPE_A`, `_GARDE_ADAPTEE` (l. 1124-1126,
1298) : trois n'existent plus (lignes du registre des préalables) ; (c) sa garde G2 cite `docs/decisions/rendez-vous-P3-bis-v1.md`
au singulier (l. 1236) alors que le brouillon 6 versionne les décisions (`-v1`, `-v2`, l. 589-592 : la décision « ouvrir »
peut être dans `-v2.md`) ; T0.7 doit lire le fichier que cite la ligne `RENDEZ-VOUS-P3BIS-n` ou le journal, jamais `-v1` par
nom. (b) et (c) sont à transmettre au rédacteur de T0.7 ; rien à changer dans P3-bis pour eux. Le brouillon 15 ne cite
`registres/prealables-p3bis-v1.md` nulle part.

**D6 (mineur) — Durée réelle non bornée (l. 518-523, 530-533).** Le seuil de 30 s est mesuré sur jouet ; sur les données
réelles, rien ne borne l'écart de durée entre issues (PB-13 « non calculable » saute « quelques secondes », dit sans
mesure). C'est cohérent avec la classe 3 choisie pour l'heure du commit ; une phrase de plus suffirait : « la lecture réelle
mesure et écrit sa durée dans le paquet (classe 2) ; l'écart réel n'est connu qu'à l'ouverture et y est rapporté ».

## Ce que j'ai vérifié et trouvé juste

- **D1 à D11 de la contre-lecture 2** : chacun traité à l'endroit annoncé. D1 (a) `ARRETEES_TOLEREES` (l. 733-735, 845-847 ;
  `lancer_p3_v1.sh` l. 60-62 exact) ; D1 (b) registre et clés (l. 549-555) ; D2 (a) rien d'imprimé (l. 484-487, 503-508,
  818-820) ; D2 (b) bourre et essai (l. 503-505, 530-531) ; D2 (c) classe 3 et contrôle 60 s / 30 s (l. 518-523, 531-533) ;
  D2 (d) second paquet en morceaux ≤ 90 Mo, `resume.json`, `sondes-figees.json`, `arret.json`, manifeste en clair (l. 453-458,
  470-472, 749-752, 821-826) ; D3 date et versions (l. 583-592, 914-917) ; D4 longueurs et R-L (l. 384-389, 680-682 ;
  `run.py` l. 291 `jetons_par_action` exact) ; D5 PB-15 (l. 337, 390-395 ; `cout_de_tache` l. 37-44 et `etiquettes_gonflement`
  l. 173-196 exacts, bornes 2 et 1,25) ; D6 blocs (l. 628-633) ; D7 code 0 (l. 485-486, 519-520, 799) ; D8 (l. 586-588) ; D9
  (l. 561-564, empreinte du brouillon 14 entière) ; D10 (l. 663) ; D11 jointure (`episode`, `pas`), unicité, effectifs, code
  1 (l. 396-398 ; `run.py` l. 277 exact).
- **PB-15 et R-L sans effet sur l'issue** : PB-15 descriptive (l. 337) ; R-L réserve (l. 680-682) ; « elles ne changent
  jamais la valeur du fichier d'issue » (l. 675).
- **Marqueurs** : `prereg.problemes` sur le brouillon 6 rend exactement deux lignes : « contre-lecture 3 sans ses deux
  empreintes » (attendu : remplie au scellement) et douze marqueurs restants, les douze de la table (l. 991-1002) ; colonne
  « quand » : « avant le candidat », « au candidat » ou « avant le scellement » pour tous ; `<<T07_B15_GARDE_ADAPTEE>>`
  remplissable au candidat par la mention de repli (sous réserve de D2 ci-dessus). Aucun marqueur ne survit au scellement ;
  `exiger_prereg_scelle` ne refusera rien au lancement. L'entrée « Contre-lecture 2 » porte ses deux empreintes entières.
- **Registre des préalables et garde `ouvrir`** : format à quatre colonnes identique à celui que lit `registre_v1.py`
  (`CLE`, `DATE`, `SHA`, l. 39-43) ; registre distinct de `scellements-v1.md` (`CLES_CONNUES` l. 58 refuserait les clés
  neuves) ; clés d'écrit au plus une fois, `RENDEZ-VOUS-P3BIS-n` consécutifs à dates croissantes, « ouvrir » en dernière
  ligne seulement ; essais R5 énumérés (l. 568-570, 759-762, 805-811) ; la garde ne lit jamais le texte ni le fichier le plus
  récent par nom. Concordance avec les écrits (a), (b), (c) du brouillon 15 : le périmètre fermé (trois jeux, présence
  mécanique, instant de fermeture), les règles de lancement et de relance (déclencheur « si P3-bis tarde » retiré),
  l'engagement de jouer l'étape A quelle que soit l'issue, sont ce que les trois lignes exigent ; le principe commun du
  brouillon 15 (aucun fichier, journal ni décision de rendez-vous de P3-bis lu pour l'étape A) répond au canal `sondes_lues`.
- **Date du rendez-vous** : 2026-11-20T12:00:00Z aux l. 583, 914, 984, 197 ; R-2021 à 16:03 UTC → échéance 2026-11-11 16:03
  UTC, exacte ; mot de Lazar avant le scellement = version neuve, après = écart (l. 585-586, 766) ; aucune levée automatique.
- **R12** : `git diff --name-status 7a54d431d89745839220f882b41b13e8c62ecfdd HEAD -- <les treize chemins de l'en-tête>` au
  commit `a535b21f7` : six ajouts (`A`) seulement, les mêmes que le texte (l. 90-92) ; aucun fichier de P3 modifié ni retiré.
- **Fermeture, hors D1 à D3 et D6** : sel du paquet des lectures et du second paquet dans l'archive, jamais dérivé de
  l'entropie ; empreintes des fichiers contenus jamais affichées ; classe 1 fermée (l. 509-514) ; durée des lectures en
  classe 2 ; « non lu », arrêt sur garde, heure du commit et taille du second paquet en classe 3, chacune justifiée.

## Points pour la session mère

1. Corriger D1 et D2 (deux nombres et une phrase) avant le candidat ; D3 au code de `fermer` et à l'essai différentiel,
   sans changer le fond ; D4 par une phrase aux deux endroits.
2. Transmettre D5 (b) et (c) au rédacteur de T0.7 pour son texte scellé.
3. Rien ici ne demande un mot de Lazar de plus que ceux déjà posés (date du rendez-vous, défaut au 11 novembre 16:03 UTC ;
   DS-2, nœud sans défaut).
