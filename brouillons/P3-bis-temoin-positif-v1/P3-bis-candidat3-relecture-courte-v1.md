# P3-bis : relecture courte de l'écart du candidat 2 au candidat 3 — v1

- Écrit le 2026-11-11 à 15:08 UTC (heure relevée par `date -u`) ; travail commencé à 15:02 UTC (`date -u`).
- Relecteur : agent neuf, **Claude Fable 5.2** (`claude-fable-5-2`), sous-agent de la session mère
  `session_01VJdZpSMxSdk2SJ1ScmdfNv`. Il n'a écrit ni P3-bis, ni ses couples, ni son code, ni sa chaîne, ni aucune de
  leurs contre-lectures ou relectures. **Aucun fichier de T0.7 ouvert** (ni texte, ni brouillon, ni note, ni module).
- Consigne : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-relecture-courte-p3bis-candidat3-v1.md`
  (`e0352c203a2b97bd461d4e6f143647e244e8182b6a7674c91ebe4f254feaddbf`, recalculée avant lecture, égale à l'empreinte
  donnée par la mère).
- Départ : `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-candidat2.md`
  (`eb7e5b8b671a71a745323135fc6aed5b0f30ad28e515575518189a2d22d71ecc`, recalculée).
- Arrivée : `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-candidat3.md`
  (`76ab66ce967796b944e2ca585ee0dc2d780189e8e0cbe429e390c427a46121cb`, recalculée au début et à la fin du travail,
  égale à son compagnon ; 361 196 octets).
- Pièces, sous `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-candidat3-pieces/`, chacune recalculée
  et égale à son compagnon : couples `P3-bis-preenregistrement-v1-candidat3-couples-v1.json`
  (`5dba04f866d21781193d8c244b74eb1345a09c156c585381f502d89f868ff999`, 17 couples C3-01 à C3-17), script
  `P3-bis-preenregistrement-v1-candidat3-faire-v1.py`
  (`9d4062366eaca946920316cc397abba34cbca99aa03e3d0bc9fc9e554752c332`), épingles proposées
  `P3-bis-epingles-proposees-v2.json` (`85500d90d98eb763704a0acc468de9bf64413bf3996ec574460d8dd8634c075b`), journal du
  candidat 3 (`c0814b44bcfee0e1f1bfb4e938db04c97c847c0735a66216693047b6b8f9aff2`, lu ; aucun de ses contrôles n'est
  repris ici sans avoir été refait).
- Méthode : programmes écrits par le relecteur dans son bac à sable
  (`/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/p3bis-relecture-c3/`, `m1.py` à
  `m7.py`), sans appel au script du rédacteur ; les autres commits lus par `git show <commit>:<chemin>`.

## Verdict

**« Relu, conforme ».** Le candidat 3 (`76ab66ce…`) est, à l'octet, le candidat 2 auquel on applique les 17 couples
C3. Aucune section gelée ne change. La chaîne citée est exacte aux deux commits. Le texte ne cite aucune empreinte qui
dépende de lui. Les onze rapports, les épingles proposées v2 et les pièces à verser sont justes. Aucun couple de
correction exigé, aucun nœud. Quatre notes (N-1 à N-4), sans effet sur le verdict.

## Constats

### Mandat 1 — couples, sections gelées, marqueurs

1. **Couples réappliqués = candidat 3, à l'octet** (`m1.py`). 17 couples, C3-01 à C3-17 dans l'ordre ; chaque
   « ancien » trouvé exactement une fois dans le texte courant, chaque « nouveau » absent avant son application ;
   résultat égal au candidat 3 octet pour octet.
2. **Couples défaits = candidat 2, à l'octet.** Dans l'ordre inverse, chaque « nouveau » trouvé exactement une fois
   dans le candidat 3 ; résultat égal au candidat 2 octet pour octet.
3. **Sept sections gelées égales à l'octet au candidat 2** (découpe du relecteur : titres de niveau 2) : « Hypothèse »
   (1 903 octets), « Prédiction chiffrée et signe attendu » (4 019), « Métrique » (10 552), « Seuil » (3 164), « Plan
   d'analyse » (50 835), « Critères de lecture gelés » (13 477), « Liste d'arrêt » (12 109) ; chacune présente une
   fois dans chaque texte. Sections qui changent : « Ce que le code et la chaîne doivent changer », « Préalables
   vérifiables du scellement », « Contre-lecture », « Marqueurs restants », plus l'en-tête et la table neuve. Les 17
   couples portent `section_gelee` nul.
4. **Titres** : 28 au candidat 2, 29 au candidat 3 ; le seul titre neuf est « Table « ce qui change du candidat 2 au
   candidat 3 » », en tête des tables ; aucun retiré. Entrées « Contre-lecture k » : 4 dans les deux textes.
5. **Aucun marqueur** : motif `<<[A-Z0-9_]+>>` de `controle_ia.prereg` : aucune occurrence ; « À REMPLIR » : 0. Les
   seuls « << » sont littéraux (`<<…>>` et le motif du titre « Marqueurs restants »), déjà au candidat 2. Trois
   « R-… » littéraux, tous dans des phrases gardées du candidat 2 (forme « date tenue : défaut échu, R-… » de P-11).
6. **`controle_ia.prereg.problemes` vide** sur le candidat 3 : `[]`.
7. **Phrase de la date tenue inchangée** : « **Candidat 2** : date tenue : mot de Lazar, R-2352 (2026-11-11, vers
   13:58 UTC), recopié tel quel : « Le candidat 2 est prêt.  scelle le et lnce le » ; la date proposée
   2026-11-20T12:00:00Z est tenue (P-11). » : une occurrence dans chaque texte, deux espaces après « prêt. » gardées ;
   mots égaux à ceux de R-2352.

### Mandat 2 — chaîne, circularité, règle (b)

8. **Douze fichiers au commit du code** `5e4575259478af3611e2c7fb1313342912caf484` : pour chacun, l'empreinte citée au
   point 6 (a) est celle de `git show 5e457525:<chemin>` et celle de son compagnon au même commit (forme
   `<sha256>  <nom>` et fin de ligne). Les quinze noms cités sont exactement les quinze fichiers `*p3bis_v2*` du
   dossier `docs/procedures/P3-bis-temoin-positif-v1/` (même liste aux deux commits).
9. **Trois bancs au commit de correction** `68ded698ce1bbfd8815d7b7ab28557775e4d2e5b` : `essais_controles_p3bis_v2.sh`
   (`36a88949…210d`), `essais_recuperation_p3bis_v2.sh` (`ae2e2d2f…f954`), `repetition_jouet_p3bis_v2.sh`
   (`750ec253…2e02`) : empreintes citées égales à `git show 68ded698:<chemin>` et aux compagnons du même commit. Les
   trois empreintes abrégées « au commit du code » (`98d03a60…`, `9e39f5ca…`, `2e4d1628…`) sont bien celles de ces
   fichiers à `5e457525` ; leurs formes entières ne sont plus dans le texte.
10. **Le commit de correction ne change que six fichiers** : son seul parent est le commit du code ; entre les deux,
    par descente des arbres là où les identifiants diffèrent, seuls changent les trois bancs et leurs trois
    compagnons. Les douze autres fichiers et leurs compagnons sont égaux aux deux commits. `68ded698` est sur la
    branche `prep/p3bis-bancs-epingles-v1` (tête `6283b129`, le commit du rapport, R-2373).
11. **Circularité : aucune.** Sept empreintes entières neuves au candidat 3 : les trois bancs (constat 9), le rapport
    du développeur des bancs (`a4020e30…`), la contre-lecture courte des bancs (`df732d18…`), la relecture courte du
    candidat 2 (`c559f2c8…`) et le candidat 2 (`eb7e5b8b…`). Toutes désignent des fichiers écrits avant le texte,
    dont aucun ne contient l'empreinte du candidat 3. Le texte ne cite ni sa propre empreinte, ni celle d'aucune des
    six pièces du dossier `…-candidat3-pieces/` (citées par leur nom seul), ni celle de cette relecture (renvoyée au
    registre). Deux commits neufs cités en entier : `68ded698…` et `a3116ff5…` (existent).
12. **Règle (b) exacte au regard des scripts.** Au commit du code : treize lignes `NOM=A_EPINGLER` dans
    `controles_avant_depense_p3bis_v2.sh` (l. 46 à 58), une dans `recuperation_p3bis_v2.sh` (`PY`, l. 42) : « treize
    et une », quatorze. `sceller_p3bis_v2.sh` accepte `scellement/p3bis-vN`, lit les épingles dans les contrôles,
    refuse toute épingle restante, et son étape 5 compare bien les quinze fichiers de `CHAINE` à leurs copies versées
    à HEAD. `releve` (bloc 4) et `piece` (étape 4) exigent le compagnon à la forme `<sha256>  <nom>`.
13. **Règle (b) exacte au regard de la branche `scellement/p3bis-v2`.** La branche existe (locale et distante, tête
    `10781b85b73db2d01c1be73c41bf8df5a5dfed11` au moment de la lecture) ; son seul parent est `68ded698` ; le commit du
    code en est ancêtre ; `d0d9fcb8` et `a3116ff5` (la v1) n'en sont pas ancêtres. Les quinze fichiers de la chaîne
    et leurs quinze compagnons y sont égaux à l'octet à ceux de `68ded698` : l'épinglage reste à faire, et le
    `git diff` annoncé entre `68ded698` et la branche montrera donc, après lui, les quatorze lignes et les deux
    compagnons seulement. Arbre gelé (`CHEMINS_GELES` : tout sauf les dossiers documentaires) : égal au commit du code
    à `68ded698` et à la tête de la v2 (seuls `docs/` et `registres/` diffèrent). La tête de la v1 distante est bien
    `a3116ff529587121b283259b404684e07f9806f2`.
14. **Ligne P-5 et ligne `CHAINE_P3BIS` de « Marqueurs restants »** (C3-12, C3-14, C3-15) : même règle que le point 6
    (b), mêmes nombres (trois bancs, dix autres fichiers, cinq compagnons, quatorze lignes).

### Mandat 3 — rapports, épingles, pièces à verser

15. **Onze rapports**, chacun cité au point 6 (b) par chemin et empreinte entière, sous la forme
    `` `<chemin>` (`<sha256>`) `` ; liste égale, dans l'ordre, à `RAPPORTS_ATTENDUS` des épingles proposées v2 et à sa
    table `rapports_attendus`. Pour chacun : empreinte du fichier sur disque égale ; compagnon égal (`<sha256>  <nom>`
    et fin de ligne) ; fichier et compagnon égaux sur `main` (tête `399e698c` à la lecture) et au commit `883a2432` ;
    chemin entre accents graves et empreinte présents dans le texte lu à plat (ce qu'exige le bloc 14) ; paire
    conforme au motif des contrôles. Les deux neufs : relecture courte du candidat 2 (`c559f2c8…`) et contre-lecture
    courte des bancs (`df732d18…`).
16. **Épingles proposées v2 justes.** Onze lignes proposées (les treize moins `CANDIDAT_RELU` et `PY`, non proposées,
    comme le dit le texte) : chaque « ligne au commit du code » est présente une fois, mot pour mot, dans les
    contrôles à `5e457525` ; chaque ligne proposée est cette ligne où seule la valeur remplace `A_EPINGLER`,
    commentaire gardé ; la fonction `epingle` du scellement en relit la valeur exacte. Valeurs : `CODE_RELU` = commit
    cité une fois à l'en-tête ; configuration (`612b0c6c…`), sortie de l'essai de fermeture (`93756286…`), longueurs
    attendues (`7c94d43c…`) citées par le texte sous la forme `` `<chemin>` (`<sha256>` `` ; consignes (`7d35576d…`)
    citées par chemin et par empreinte ; `CANDIDAT_RELU_CHEMIN` = chemin du candidat 3, écrit au point 6 (b) ; la
    configuration relue cite bien les consignes relues (`prereg/P3-bis-consignes-v1.md`, `7d35576d…`).
17. **Pièces à verser** : 19 entrées. Chacune des 18 qui portent une empreinte est égale, fichier et compagnon, au
    commit « où la prendre » (`883a2432` ; `dfb1ed7b` pour les longueurs attendues, absentes de `main` ; `68ded698`
    pour les trois bancs) ; les 54 mentions « presence » (à `d0d9fcb8`, `a3116ff5`, `68ded698`) sont toutes exactes.
    **Étape 4 du scellement** : les seize pièces qu'elle exige (candidat, configuration, consignes, essai de
    fermeture, longueurs, onze rapports) sont toutes dans la liste, aucune ne manque. **Étape 5** : les trois bancs
    sont dans la liste et déjà sur la v2 ; les dix autres fichiers y sont par filiation ; restent les deux fichiers
    épinglés et les sept journaux canoniques, que la note du fichier renvoie après le texte (voir N-2).

### Mandat 4 — table et en-tête

18. **Table « du candidat 2 au candidat 3 »** : six lignes ; les 17 couples y sont tous rattachés, chacun une fois
    (C3-01 à C3-08 ; C3-09 ; C3-10, C3-11, C3-12, C3-14, C3-15 ; C3-13, C3-16 ; C3-17), C3-10 deux fois à bon droit
    (règle et rapports). Colonnes « candidat 2 » et « candidat 3 » exactes (quinze puis douze et trois ; neuf puis
    onze ; branche non nommée puis `scellement/p3bis-v2`). La phrase sur les sections gelées est vraie (constats 2
    et 3).
19. **En-tête** : décisions R-2367, R-2373 et R-2374 présentes au registre de `883a2432` (R-2375 n'y est pas, à bon
    droit) ; état des préalables conforme au registre (R-2295, R-2340, R-2345, R-2349, R-2352, R-2358, R-2361) ;
    pièces citées (candidat 2, rapport des bancs, contre-lecture des bancs, relecture du candidat 2) égales à leurs
    compagnons sur `main` ; les six pièces neuves existent et sont scellées. À « Contre-lecture » (C3-13), ce que le
    texte prête à la relecture du candidat 2 est dans son rapport : « Relu, conforme », 22 couples, « Plan d'analyse »
    seul changé par N-1, notes N-1 à N-3, N-2 sur les compagnons.

## Notes (sans effet sur le verdict)

- **N-1 — forme du compagnon, une espace de moins.** Le point 6 (b) écrit « à la forme de `scellement.sceller`
  (`<sha256> <nom>` et fin de ligne) », avec une espace ; la forme réelle en a deux (`scellement.py` : `f"{h}  {p.name}\n"` ;
  R-2360 ; `piece` et `releve`). La référence qui fait foi, `scellement.sceller`, est nommée, et le contrôle se fait
  par programme : rien à corriger avant S. Si un texte neuf est écrit un jour, couple exact : ancien
  « (`<sha256> <nom>` et fin de ligne ; » → nouveau « (`<sha256>  <nom>` et fin de ligne ; ».
- **N-2 — pièces de l'étape 5 hors de la liste** (reprise de la N-1 de la relecture du candidat 2). Les deux fichiers
  épinglés, leurs compagnons, et les sept journaux canoniques avec leurs compagnons ne sont pas des entrées de
  `pieces_a_verser` ; `note_pieces` le dit. À compter par la mère dans son constat de P-5 et P-6. À la tête lue de la
  v2, aucun journal n'est versé (attendu).
- **N-3 — mentions « candidat 2 » gardées à la ligne P-5.** La colonne « préalable » de P-5 dit encore, sous
  l'étiquette « candidat 2 (R-2345) », « chemin `…-candidat2.md` » pour `CANDIDAT_RELU`. C'est de l'historique
  étiqueté, et le chemin du candidat 3 est écrit trois fois ailleurs (point 6 (b), « Contre-lecture », ligne
  `CANDIDAT_RELU` de « Marqueurs restants »). Sans effet sur la chaîne, qui lit l'épingle.
- **N-4 — majuscule d'une citation.** Le point 6 (a) cite la contre-lecture des bancs par « citable au scellement :
  commit `68ded698` » ; le rapport écrit « **Citable au scellement : commit `68ded698`** ». Les mots sont ceux de
  R-2374. Rien à corriger.

## Points ouverts pour la mère (hors mandat)

- Le mot de Lazar recopié (R-2352) dit « Le candidat 2 est prêt. scelle le et lnce le ». La phrase de la date tenue
  est inchangée, comme demandé, et aucune section gelée ne change ; savoir si ce mot couvre le scellement du candidat 3
  est une lecture de la mère, à consigner.
- `main` a avancé pendant la lecture (`154e3735`, puis `d967a642`, puis `399e698c`) ; les égalités « sur `main` » ont
  été prises à `399e698c` et à `883a2432`.

## Gestes déclarés

- Git, en lecture seule : `git show <commit>:<chemin>` (fichiers, et listes de dossiers : racine, `docs/`,
  `docs/procedures/`, `docs/procedures/P3-bis-temoin-positif-v1/`, noms seuls) ; `git rev-parse` (identifiants de
  commits, de branches et d'arbres) ; `git merge-base --is-ancestor` ; un `git log -1 --format` sur la tête de la v2
  (date et titre). Aucun `ls-tree`, aucun `diff`, aucun `fetch`, aucune écriture git.
- Registre : lignes R-2295, R-2340, R-2345, R-2349, R-2352, R-2356, R-2358, R-2360, R-2361, R-2367, R-2373, R-2374,
  R-2375 de `registres/decisions.md`, affichées par leur début de ligne ; R-2295 parle du bras d'attaque et d'un point
  de T0.7, R-2349 du lecteur de T0.7 (lignes de registre, aucun fichier ouvert).
- Lus en entier ou en partie : candidats 2 et 3, couples, journal et épingles du candidat 3 ; au commit du code,
  `sceller_p3bis_v2.sh`, `controles_avant_depense_p3bis_v2.sh`, les lignes d'épingle de `recuperation_p3bis_v2.sh`, la
  définition de `CHEMINS_GELES` ; `registres/go.md` de la v2 et de `main` comparés par programme (non affichés) ; le
  verdict de la contre-lecture des bancs et les notes de la relecture du candidat 2.
- Non ouverts : tout fichier de T0.7 ; tout chemin ou branche des interdits communs v2 ; `diag/`, `runs/`, `donnees/` ;
  le contenu des trois bancs corrigés (hachés seulement). Aucun appel de modèle, aucune dépense, aucun commit. Suite
  d'essais non lancée. Aucun refus de permission rencontré.
- Écrit : ce rapport et son compagnon ; le bac à sable nommé plus haut.

Relecteur : Claude Fable 5.2, agent neuf. Verdict : « relu, conforme ».
