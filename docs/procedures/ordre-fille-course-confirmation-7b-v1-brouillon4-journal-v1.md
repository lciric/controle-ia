# Journal du rédacteur — ordre de la course de confirmation 7b de T0.6, brouillon 4 — v1

- **Qui** : rédacteur neuf, sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy` (Claude Opus 5.5) ; il n'a écrit ni l'ordre, ni ses brouillons 1 à 3, ni leur contre-lecture, ni T0.6, ni sa chaîne.
- **Quand** (`date -u`, 10 novembre 2026) : 10:14:08 (empreintes des pièces, début) ; 10:39:33 (registres relus pour les marqueurs remplis) ; 10:39:50 (couples écrits dans le dépôt) ; 10:39:51 (script joué, « TOUT PASSE ») ; 10:40:47 (début de ce journal) ; heure de scellement : compte rendu à la mère.
- **Dépôt** : `main`, tête locale `16223e42` au début, `7163ad84` à 10:39 (la mère committe pendant le travail). Écritures : le brouillon 4, ses couples, son script et ce journal, plus leurs compagnons, sous `docs/procedures/` ; le brouillon 3 (`eae1e64f99ce2e4f90b7cf28ffecda597d11d3f48d72b3898960342d8e9c3ad6`) reste tel quel (R12, empreinte revérifiée après l'écriture). Interdits communs v2 (`1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`, empreinte vérifiée) lus et tenus, règle 9 comprise ; gestes à déclarer : § 6.

## 1. Sources lues (empreintes et lignes)

- Brouillon 3 : `docs/procedures/ordre-fille-course-confirmation-7b-v1-brouillon3.md`, `eae1e64f…` ; son journal `adc3791e…` (égal à son compagnon).
- Contre-lecture : `docs/procedures/ordre-fille-course-confirmation-7b-v1-brouillon3-contre-lecture-v1.md`, `f738d855b35ca387195dc6ef0a4b700c7a1e186b3a2dbdda693c056862bf6849` (B1, C1 à C9, M1 à M14).
- Consigne de l'ordre : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/consigne-redaction-ordre-7b-v1.md`, `0dca9d5b…`.
- `registres/decisions.md` : R-2092 (l. 2050), R-2112 (l. 2070), R-2113 (l. 2071), R-2115 (l. 2073), R-2130 (l. 2088), R-2143 (l. 2101) ; aussi R-2051 et R-2090 (session d'un autre compte non joignable), R-2077, R-2079 (bascule du 13 à 12:00 UTC), R-2082, R-2087, R-2103 (D-4) ; R-2144 à R-2157 parcourues : seule R-2153 touche un ordre voisin (variante B), rien pour celui-ci.
- `registres/go.md` l. 291 (GO-2026-11-10-01), l. 296 (GO-2026-11-10-06) ; `registres/depenses.md` (aucune ligne sous GO-2026-11-02-28 ni GO-2026-11-10-01, 10:39:33Z) ; `registres/scellements-v1.md` (aucune ligne `SCELLEMENT-T07`, seules J-D et J-A, 10:39:33Z).
- Texte scellé de T0.6 (`ef31feff…`, lu, non touché) : « Liste d'arrêt » (l. 589 à 614), « Devis » (l. 676, 698 à 701 : 72 h, « une borne, non un droit », « génération des données comprise », « erreur de mémoire à la distillation »), plan d'analyse point 5 (l. 499 à 500 : passe unique), « Concordance » point 1 (l. 767). Configuration (`b7a5c1ba…`, lue, non touchée) : prix plafonds 1,3 et 4,7, stockage 0,08, téléchargement 40 Go à 0,05.
- Code gelé `1609a4bf` (par `git show`, non touché) : `lanceur_v6.py` l. 193 à 194 (`arret.json`), 225, 237, 299 (`morceaux=`), 305, 313, 323, 330 (`ligne_B`, `ligne_C`), 333 ; `amorce_instance_t06_v11.sh` l. 71 (marge 1 800 s), 78 (consignation 2 400 s), 101 à 126 (minuterie), 141 à 164, 284, 300 (`MOTIF_INTERDIT`), 318 à 322, 502 à 514 ; `lancer_t06_v13.sh` l. 113 (`champ`), 145, 237, 248 (`instance` dans `lancement.txt`), 264 ; `session_v2.py` l. 153 ; `session_v3.py` l. 83 à 110, 146 à 156 (code 1 si `arret`) ; `gardes.py` l. 49 à 52 ; `scellement.py` l. 72 (forme du compagnon). Garde de la session sur `main` : `.claude/hooks/garde_calcul.py` l. 37 à 38, 148 à 149.
- Ordre de la variante B, brouillon 3 (`b053a2207006c49d7aca8d8e5975d7539857474d98591368088cda1fc2a1b484`, par `git show prep/t07-module-v2:docs/procedures/ordre-execution-etape-a-t07-v1-brouillon3.md`) : marqueurs `BRANCHE_7B`, `RUN_T06_7B`, ligne `RUN-CONFIRMATION-T06` (l. 84, 110 à 111).
- Addendum v3 du bras B : `HEAD:docs/notes/g0-deux-semaines-v1/scellement-course-t06-v1/pieces-apres-couples/addendum-bras-b-v2-brouillon-v3-apres-couples-v1.md` et son compagnon, `1a372523…` (commit `4af5b0e3`, R-2092).

## 2. Constats et couples : tous appliqués

| Constat | Couples | Appliqué | Forme, écart à la lettre du couple |
|---|---|---|---|
| B1 | B4-44, B4-52, B4-57 | oui | texte du couple, plus deux précisions : « arrêtée après cette heure : aussitôt le rapatriement fait » (instance arrêtée entre 23:00Z et 00:00Z) ; lignes l. 71 et 78 de l'amorce citées pour 1 800 s et 2 400 s |
| C1 | B4-06, B4-07, B4-08, B4-34, B4-36, B4-37, B4-38 | oui | boucle et ligne neuve au caractère près ; cohérence : « (nom et compagnon) » au § 2 point 1, § 2 point 5, puce « Rapatriement », puce « Arrêt consigné » |
| C2 | B4-12, B4-21, B4-22, B4-50, B4-51, B4-58, B4-59 | oui | `LIGNE_REGISTRE_BRAS_B` rempli à `R-2092` ; clause `AUCUNE` retirée ; § 13 point 2 réduit à la phrase du couple |
| C3 | B4-02, B4-09, B4-59 | oui | définition du couple ; ordre de remplissage au § 14 ; la bascule du 13 novembre devient une règle de la mère (P2 et § 14) |
| C4 | B4-41, B4-43, B4-53 | oui | au caractère près ; cohérence : § 10 « remis par Lazar à la mère » |
| C5 | B4-15, B4-29, B4-30, B4-33, B4-35, B4-45, B4-46, B4-49, B4-54 | oui | ligne `ID=$(champ instance)…` au caractère près, trois fois ; au § 4.12, l'inventaire est lu une fois (`I`) puis compté (`nI`), forme équivalente à `bash "$W/inventaire.sh" \| grep -c "^$ID t06-v2 "` ; « sinon aucun geste » rendu mécanique (`stop`, `destroy`, `show instance` sous condition `nI = 1`) ; conséquence écrite au code 4 (aucune ligne `instance` : aucun geste sans un mot de Lazar qui nomme l'identifiant) |
| C6 | B4-38, B4-39 | oui | ligne Python au caractère près |
| C7 | B4-03, B4-42 | oui | au caractère près |
| C8 | B4-40, B4-41 | oui | attendu du couple, plus deux lignes du bloc des données : morceaux annoncés (`progres.txt`) et poussés ; lignes `ERREUR DE CHAÎNE (C11)` de `journal-instance.txt` |
| C9 | B4-05, B4-56, B4-57 | oui | § 0 et § 11 ; § 12 : « (GO-2026-11-10-06) » |
| M1 | B4-33, B4-35 | oui | condition `running` ou `loading`, jointe à celle de C5 |
| M2 | B4-45, B4-46, B4-54 | oui | attendu du couple ; aucun `sleep 60` dans le bloc (une attente au premier plan peut être refusée par l'outil de la session) : la fille relève l'inventaire une minute plus tard ; § 9 : deux demandes de destruction au plus |
| M3 | B4-31, B4-32 | oui | `echo "code $?"` après `depense 60` ; relevé de H60 ; chiffres refaits aux prix plafonds de la configuration, téléchargement de 0 à 2 USD : H200 (60 − 2 à 60) ÷ 4,78 = 12,13 à 12,55 h, écrit « 12 à 12,5 h » (arrondi ; l'heure qui fait foi est celle que rend `depense 60`) ; A100 ÷ 1,38 = 42,03 à 43,48 h (le couple disait « vers 12,5 h » pour H200) |
| M4 | B4-25, B4-26, B4-27, B4-28, B4-58 | oui | empreinte écrite au journal au § 4.9, relue et comparée au § 4.10 ; dix minutes mesurées sur la date du fichier (`stat -c %Y`) ; renvoi corrigé : la garde teste `LANCEMENTS` à la l. 149 de `garde_calcul.py` (la l. 148 est `garder_lanceur_v3`) |
| M5 | B4-19, B4-20 | oui | trois exclusions, « neuf exclusions » |
| M6 | B4-04, B4-16, B4-18, B4-59 | oui | marqueur gardé (non remplissable ce jour) ; qui et quand au § 14 ; valeur de repli ; première ligne du journal = identifiant de la session |
| M7 | B4-11, B4-21, B4-22 | oui | commande du couple ; `DEPENSE_ANTERIEURE_USD` rempli à `0` (B4-14) : autre compte que `0` à la remise → aucune création, compte rendu |
| M8 | B4-13, B4-24, B4-55 | oui | |
| M9 | B4-16, B4-17 | oui | seconde option : `${VAST_API_KEY:+VAST_API_KEY="$VAST_API_KEY"}` |
| M10 | B4-16, B4-17 | oui | tout le bloc sous `if mkdir "$W"; then … else echo "ARRÊT …"; fi` |
| M11 | B4-47, B4-48 | oui | |
| M12 | B4-09, B4-21, B4-22 | oui | |
| M13 | B4-55 | oui | « pour la ligne `RUN-CONFIRMATION-T06` que la mère inscrit » (P2 de la variante B) |
| M14 | B4-04, B4-10, B4-18, B4-53 | oui | |

Aucun constat non appliqué. Retouches de cohérence (déclarées, sans constat propre) : B4-01 (titre), B4-02 (statut), B4-15 (note de (A)), B4-23 (§ 4.6 : « refus observé par le rédacteur des brouillons 1 à 3, non rejoué au brouillon 4 »), B4-29 (code 4), B4-49 (§ 5 point 4 : `D` de la première instance), B4-58 et B4-59 (titres des § 13 et § 14). Rien du texte scellé de T0.6, de sa configuration ni de la chaîne n'est touché.

## 3. Marqueurs

Restent **trois**, une occurrence chacun (compté par le script) :

- `ID_SESSION_FILLE` (en-tête) : Lazar donne l'identifiant une fois la session fille ouverte ; la mère le recopie **avant le scellement de l'ordre** ; à défaut (session ouverte après), valeur « à laquelle Lazar remet cet ordre » ; dans les deux cas, la fille écrit son identifiant en première ligne de son journal (§ 4.0).
- `COMMIT_MAIN_REMISE` (§ 4.1) : la mère, au commit qui porte `SCELLEMENT-T07`, l'engagement et R-2092, parent du commit qui ajoute l'ordre scellé ; donc après le scellement de T0.7.
- `LIGNE_SCELLEMENT_T07` (§ 4.3) : la mère, après le scellement de T0.7 et son inscription dans `registres/scellements-v1.md` (aucune ligne ce jour, 10:39:33Z).

Remplis au brouillon 4 : `DEPENSE_ANTERIEURE_USD` = `0` (aucune ligne de dépense sous les deux GO, 10:39:33Z ; revérifié par la fille, § 4.3) ; `LIGNE_REGISTRE_BRAS_B` = `R-2092`. Ordre de remplissage (§ 14) : T0.7 scellé et inscrit ; engagement ; commit ; marqueurs ; scellement de l'ordre ; commit de l'ordre ; remise.

## 4. Script et sortie

`cd <bloc-notes> && /home/user/controle-ia-travail/.venv/bin/python -I -B /home/user/controle-ia-travail/docs/procedures/ordre-fille-course-confirmation-7b-v1-brouillon4-appliquer-v1.py /home/user/controle-ia-travail` : code 0 ; sortie gardée hors du dépôt (`a9aa1306…`). Résumé :

- brouillon 3 à son empreinte ; couples `769ea60e84dd11ab2a58ee6e1dcd9d3ea098f90520ca8ea40cf6db654d572668`, 59 couples, chacun présent une fois au moment de son application, disjoints, dans l'ordre du texte ;
- brouillon 4 écrit : `5f2167d705795db3d8e8850bbcf6cfc0c07750634d030b0ba0598379f4f8aef7`, 55 638 octets (44 501 au brouillon 3), 398 lignes ; même résultat qu'à l'essai fait d'abord dans le bloc-notes ;
- (1) titre et statut ; (2) 29 titres de sections, égaux hors § 13 et § 14 ; (3) trois marqueurs, une fois chacun, valeurs remplies présentes ; (4) 18 blocs `bash`, `bash -n` sans erreur, enveloppe et inventaire écrits par le § 4.0 compris ; (5) 7 extraits Python, `ast.parse` sans erreur ; (6) 78 jetons de garde, une seule baisse voulue (le commentaire « jamais un autre identifiant » du `stop`, remplacé par la condition de C5 et M1) ; (7) 56 phrases exigées pour 24 constats présentes, 15 phrases retirées absentes ; (8) essais en mémoire conformes : M10 (bloc joué deux fois, la seconde n'écrit rien), M9, C5 (trois cas), C5 et M1 (cinq cas de `stop`), C5 (trois cas de `destroy`), C1 (contenu de `resume.json` jamais demandé), C6 (huit cas, `partiel` jamais imprimé), C8, M4 (empreinte autre ou impression de plus de dix minutes : rien n'est exécuté) ; (9) 90 lignes retirées, 102 ajoutées ; « TOUT PASSE ».

## 5. Points ouverts

- Comme la contre-lecture, je n'ai rejoué ni les gardes du § 4.6 (clone et extraction interdits ici) ni rien de `vastai` : les états `running` et `loading` de M1, le texte de `show instance` et la lecture de la clé par `vastai` (M9) restent non vérifiés. Un autre état (« created », « offline ») ne reçoit pas de `stop` ; la destruction du § 4.13 suit.
- B1 demande une fille active le 17 novembre à 01:15 UTC si le run vit encore à 23:00Z le 16.
- Longueur : 55 638 octets, surtout les textes des couples de la contre-lecture.
- `DEPENSE_ANTERIEURE_USD` = `0` suppose aucune dépense sous GO-2026-11-02-28 ni GO-2026-11-10-01 avant la remise ; le contrôle M7 de la fille arrête la création sinon.
- Une contre-lecture du brouillon 4 (au moins du différentiel) est laissée à la décision de la mère (statut).

## 6. Gestes à déclarer

- Deux listes de noms suivis (`git ls-files` avec exclusions de `diag`, `runs`, `donnees`, `docs/notes/bras-attaque`, `scripts/extraire_mesures_epreuve_t06_v1.py`, `registres/index-bras-attaque*`), filtrées par `grep` : la première a affiché des noms de fichiers sous `docs/notes/epreuve-etiqueteur-v1/` (couples, scripts et journaux de l'épreuve de l'étiqueteur) ; noms seuls, aucun ouvert ; la seconde excluait ce dossier.
- `ls docs/procedures/` a affiché les noms de deux ordres de l'étiqueteur ; non ouverts.
- `git ls-tree --name-only prep/t07-module-v2 docs/procedures/` (un dossier, sans récursion) ; l'ordre de la variante B copié par `git show` dans le bloc-notes pour en lire les marqueurs.
- Les couples ont été écrits par un outil de travail du bloc-notes (`gen_couples_b4.py`, hors du dépôt, non livré) : anciens pris au caractère près dans le brouillon 3 par numéro de ligne à début vérifié, nouveaux écrits ou dérivés par remplacement vérifié ; le fichier livré des couples est la seule donnée qui fait foi.
- Essais en mémoire : `bash` dans un dossier temporaire, environnement réduit à PATH, HOME et LANG ; `vastai` remplacé par une fonction factice (le script refuse de jouer un code où un appel réel resterait) ; `git` remplacé par une fonction factice (C1) ; au § 4.10, seule une commande factice (`echo`) est exécutée ; M9 joué sous un nom neuf (`CLE_FACTICE`, valeur factice), seul cet argument imprimé.
- Aucun refus de permission ni de classifieur. Aucun appel externe, aucune dépense, aucune écriture git, aucun `vastai`, aucune valeur de clé lue ; aucun `lecture-sondes-t06.json`, aucune pièce de 7a, aucun chemin du bras d'attaque, rien de l'étiqueteur ouvert ; suite complète des essais non lancée.
