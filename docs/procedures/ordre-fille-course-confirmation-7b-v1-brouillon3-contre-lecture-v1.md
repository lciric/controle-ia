# Contre-lecture (R2) — ordre de la course de confirmation 7b de T0.6, brouillon 3 — v1

- **Qui** : contre-lecteur neuf, sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, Claude Fable 5.2 d'après ce qu'il sait de lui (autre modèle que le rédacteur, Claude Opus 5.5). Il n'a écrit ni l'ordre, ni ses brouillons, ni le préenregistrement de T0.6, ni sa chaîne.
- **Quand** (`date -u`, 10 novembre 2026) : début 10:02:33 UTC ; lecture finie et rédaction commencée à 10:11:30 UTC ; heure de scellement : dans la réponse à la mère.
- **Dépôt** : `main`, tête locale `ea4f519d` au début, `cda9e71a` à 10:11 UTC (la mère committe pendant la lecture). Lecture seule ; une seule écriture : ce fichier et son compagnon.
- **Objet** : `docs/procedures/ordre-fille-course-confirmation-7b-v1-brouillon3.md`, `eae1e64f99ce2e4f90b7cf28ffecda597d11d3f48d72b3898960342d8e9c3ad6` (égale à son compagnon) ; journal `adc3791eee69b1c4a7849716206b405f89cf08e0bac5164dc65169b5f69fb312` (égal à son compagnon).
- **Interdits communs v2** (`1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`, empreinte vérifiée) lus et tenus, règle 9 comprise ; gestes à déclarer : § 5.

## 1. Verdict

**À corriger avant scellement : un bloquant (B1), neuf points à corriger (C1 à C9), quatorze mineurs (M1 à M14).** Tous se règlent par couples de texte ; aucun ne demande de toucher au texte scellé, à la configuration ni à la chaîne.

Hors B1, l'ordre suit le texte scellé de T0.6 (`ef31feff…`) et sa configuration (`b7a5c1ba…`) : gardes de la chaîne, calendrier, plafond, seuils de 60, 180 et 200 USD, mot de Lazar avant toute H200, fenêtre de douze recherches, embargo sur `lecture-sondes-t06.json`, sorties attendues par la variante B. Les renvois de lignes au lanceur v13 et à l'amorce v11 sont exacts (§ 3).

## 2. Constats

### Bloquant

**B1 — « Dans tous les cas, au plus tard le 16 à 23:00Z » ferait détruire un run encore vivant, contre la « Liste d'arrêt » scellée.**
Le texte scellé (« Liste d'arrêt », en-tête) : « aucun couperet de temps » ; « l'instance encore en marche y consigne et pousse ses résultats partiels avant sa destruction par la minuterie » (17 novembre, 00:00 UTC). Le pire cas P1 du devis (création le 15 à 20:48Z, 27,2 h) finit exactement à cette heure. Lu à la lettre, le § 4.13 fait détruire par la fille, une heure avant, une instance dont le run tourne : résultats partiels non consignés perdus, écart au texte scellé. Le § 8 dit la bonne règle ; le § 4.13 et le § 12 la contredisent. De plus, une instance **arrêtée** n'a plus de minuterie (le conteneur est arrêté) : la phrase « avant la minuterie de l'amorce » n'a pas d'objet pour elle, et seule la fille la détruit.

- § 4.13, quatrième puce. Texte actuel → « - **Dans tous les cas, au plus tard le 2026-11-16 à 23:00Z** : fin de la couverture de la dépense et avant la minuterie de l'amorce (17 novembre 00:00 UTC). »
  Texte corrigé → « - **Instance arrêtée, ou dont l'amorce a écrit sa ligne de fin : destruction au plus tard le 2026-11-16 à 23:00Z** (fin de la couverture de la dépense ; une instance arrêtée n'a plus de minuterie, seule la fille la détruit). **Instance dont le run est encore vivant à cette heure : aucun geste de la fille** ; la minuterie de l'amorce consigne, pousse et détruit à partir du 17 novembre à 00:00 UTC (« Liste d'arrêt » du texte scellé ; § 8 ; amorce l. 101 à 126 : consignation bornée à 2 400 s, marge de destruction 1 800 s) ; la fille relève l'inventaire filtré le 17 à 01:15 UTC et, si l'instance y figure encore, la détruit par son identifiant, puis § 4.12. »
- § 12. Texte actuel → « destruction au plus tard 2026-11-16T23:00Z. » Texte corrigé → « destruction d'une instance arrêtée au plus tard 2026-11-16T23:00Z ; run encore vivant : minuterie du 17 à 00:00Z (§ 4.13). »

### À corriger

**C1 — `resume.json` porte les lignes des tables B et C, et l'ordre en fait descendre le contenu.**
Code gelé, `lanceur_v6.py` l. 330 : `"ligne_B": ls["table_B"]["ligne"], "ligne_C": ls["table_C"]["ligne"]` ; ces clés sont retirées de la seule sortie standard (`resume_imprimable`, C02). La boucle du § 4.12 (`git show "$R:$f" | sha256sum`) fait entrer ce fichier dans le dépôt d'objets de `$M` et le passe à un outil. Rien n'est affiché, et 7a a fait de même (R-2039) ; mais l'ordre s'interdit pour `lecture-sondes-t06.json` jusqu'au hachage (§ 2.1), et laisse sur le disque de la fille, à une commande d'un affichage, les deux lignes que DT-4 ferme. La fille n'a aucun besoin du contenu : le compagnon suffit.

- § 4.12, ligne de la boucle. Texte actuel → `grep -E "^(runs|diag)/$RUN/" "$L" | grep -v '\.sha256$' | while IFS= read -r f; do …`
  Texte corrigé → `grep -E "^(runs|diag)/$RUN/" "$L" | grep -v '\.sha256$' | grep -vxF "diag/$RUN/resume.json" | while IFS= read -r f; do …` suivie d'une ligne neuve : `f=diag/$RUN/resume.json; grep -qxF "$f" "$L" && grep -qxF "$f.sha256" "$L" && git -C "$M" show "$R:$f.sha256" | grep -qxE '[0-9a-f]{64}  resume\.json' && echo "OK (compagnon seul) $f" || echo "resume.json absent ou compagnon non conforme"`
- § 2, point 1, à la fin. Ajouter → « `diag/<run>/resume.json` porte `ligne_B` et `ligne_C` (`lanceur_v6.py` l. 330) : même règle, son contenu n'est ni descendu ni haché ; seul son compagnon est lu. »
- § 2, point 4. Texte actuel → « `resume.json` (il porte `ligne_A`, `ligne_B`, `ligne_C`), » retirer `resume.json` de la liste des fichiers « hachés seulement ».
- § 4.12, « Attendu ». Texte actuel → « `OK` pour le manifeste, `distillation-t06.json`, `episodes-t06.json`, `lecture-cout-t06.json`, `resume.json` (hachés, **jamais affichés**) » Texte corrigé → « `OK` pour le manifeste, `distillation-t06.json`, `episodes-t06.json`, `lecture-cout-t06.json` (hachés, **jamais affichés**) ; `OK (compagnon seul)` pour `resume.json` ».

**C2 — § 7, P7 et § 13.2 disent l'addendum v3 du bras B « non rempli » : c'est faux depuis R-2092 (07:26 UTC, avant le brouillon 3).**
Vérifié : `docs/notes/g0-deux-semaines-v1/scellement-course-t06-v1/pieces-apres-couples/addendum-bras-b-v2-brouillon-v3-apres-couples-v1.md` est sur `main` (commit `4af5b0e3`), empreinte `1a372523290fdaf0a606db592295885f01ff9d6adc9b877fd72279fc6a44ccdf`, égale à son compagnon ; `grep -c '^| R-2092 |' registres/decisions.md` rend `1`. Un ordre scellé ne peut pas porter « aucune ligne du registre n'en consigne le scellement ».

- § 7, deuxième sous-puce. Texte actuel → « **addendum v3 scellé : non rempli** : sur `main`, seul le brouillon […] ; aucune ligne du registre n'en consigne le scellement ; » Texte corrigé → « **addendum v3 scellé : rempli** : copie après couples scellée sur `main` par la mère (R-2092), `docs/notes/g0-deux-semaines-v1/scellement-course-t06-v1/pieces-apres-couples/addendum-bras-b-v2-brouillon-v3-apres-couples-v1.md`, `1a372523290fdaf0a606db592295885f01ff9d6adc9b877fd72279fc6a44ccdf` ; la fille vérifie fichier et compagnon à cette empreinte (§ 4.3) ; »
- § 4.3, à la fin du bloc. Ajouter → `F=docs/notes/g0-deux-semaines-v1/scellement-course-t06-v1/pieces-apres-couples/addendum-bras-b-v2-brouillon-v3-apres-couples-v1.md; [ "$(git show "HEAD:$F" | sha256sum | cut -d' ' -f1)" = 1a372523290fdaf0a606db592295885f01ff9d6adc9b877fd72279fc6a44ccdf ] && [ "$(git show "HEAD:$F.sha256" | cut -d' ' -f1)" = 1a372523290fdaf0a606db592295885f01ff9d6adc9b877fd72279fc6a44ccdf ] && echo "addendum v3 du bras B scellé"`
- P7. Texte actuel → « **addendum v3 scellé** (**non rempli à la rédaction**, § 7) » Texte corrigé → « **addendum v3 scellé** (R-2092, § 7) ».
- § 14, `LIGNE_REGISTRE_BRAS_B` : valeur `R-2092`.
- § 13, point 2 : à retirer, ou à réduire à « la règle de l'ordre (addendum avant la création) est plus stricte que GO-2026-11-07-09 et -08-01 (« avant toute lecture ») ; elle est remplie ».

**C3 — le marqueur `COMMIT_MAIN_REMISE` est défini de façon impossible.**
§ 14 : « commit de `main` portant cet ordre scellé ». L'empreinte d'un commit dépend du contenu de l'ordre : elle ne peut pas y être écrite.

- § 14. Texte actuel → « commit de `main` portant cet ordre scellé, `SCELLEMENT-T07` et l'engagement » Texte corrigé → « commit de `main` qui porte `SCELLEMENT-T07`, l'engagement et la ligne du bras B, **parent** du commit qui ajoute cet ordre scellé ; l'ordre lui-même se vérifie par son compagnon et par l'empreinte du message de remise (§ 4.1) ».
- Ordre de remplissage à écrire au § 14 : T0.7 scellé et inscrit ; engagement ; commit ; marqueurs ; scellement de l'ordre ; commit de l'ordre ; remise. La clause de P2 « ligne absente le 13 novembre à 12:00 UTC : ordre suspendu » ne peut donc jouer que pour un ordre remis avant le scellement de T0.7, ce que le marqueur `LIGNE_SCELLEMENT_T07` exclut : la garder comme règle de la mère (R-2079), non comme geste de la fille.

**C4 — « mot de la mère », « écrit de la mère », « copie à la mère » : canal non dit, et écart à R-2113.**
R-2113 : « si une de ces données manque, compte rendu et attente du **mot de Lazar** avant destruction ». L'ordre écrit « mot de la mère » (§ 4.12, § 4.13). Par ailleurs une session d'un autre compte n'est pas joignable par la mère (R-2051, R-2090) : si la fille tient ses clés sur un autre compte, aucun mot de la mère ne lui parvient.

- § 4.13, troisième puce. Texte actuel → « **Écart sur les données** (§ 4.12) : destruction sur le mot de la mère. » Texte corrigé → « **Écart sur les données** (§ 4.12) : compte rendu, puis destruction sur un mot de Lazar écrit dans la session de la fille (R-2113), au plus tard le 16 à 23:00Z. »
- § 4.12, dernière phrase du bloc des données. Texte actuel → « compte rendu à la mère **avant** toute destruction. » Texte corrigé → « compte rendu à Lazar et à la mère **avant** toute destruction (§ 4.13). »
- § 9, première puce. Ajouter → « **Canal** : la fille écrit à Lazar dans sa session ; Lazar relaie à la mère. Un « écrit » ou un « addendum de la mère » est un fichier scellé sur `main`, nommé avec son empreinte dans un mot de Lazar écrit dans la session de la fille, qui en vérifie le compagnon avant d'agir. »

**C5 — l'identifiant d'arrêt et de destruction est retapé à la main (R10).**
§ 4.11, § 4.12, § 4.13 : `ID=<identifiant créé>`. Une faute de frappe détruirait une autre instance du compte (58936096, 58936099, 58936100, 59845811 y figuraient à la fin de 7a, R-2039). Le lanceur écrit l'identifiant dans `lancement.txt` (l. 248) et refuse une surveillance sur un autre (l. 264).

- § 4.11, § 4.12, § 4.13. Texte actuel → `ID=<identifiant créé>` Texte corrigé → `ID=$(champ instance); [[ "$ID" =~ ^[0-9]+$ ]] || echo "ARRÊT : identifiant illisible dans lancement.txt"` (avec `D` de l'instance en vigueur dans (A)) ; et, avant `stop` comme avant `destroy` : `bash "$W/inventaire.sh" | grep -c "^$ID t06-v2 "` attendu `1`, sinon aucun geste.

**C6 — le `motif` d'`arret.json` s'imprime sans le filtre C01.**
§ 4.12 imprime 300 caractères du motif quelle que soit l'étape. Un arrêt aux étapes « test croisé » ou « résumé » naît dans le code des sondes ; l'amorce filtre ses propres relais par `MOTIF_INTERDIT` (l. 300, 511), l'ordre non.

- § 4.12, bloc de l'arrêt consigné. Texte actuel → `print("motif :", str(r.get("motif"))[:300])` Texte corrigé → `import re; m=str(r.get("motif")); print("motif :", "retenu (étape des sondes ou motif interdit, C01) : compte rendu" if r.get("etape") in ("test croisé","résumé") or re.search("au-dessus|interpr|échec|echec|aire=|bas=|haut=|ligne_|table_|plancher", m, re.I) else m[:300])` (dans la même commande `python3 -I -c`).

**C7 — la destruction dès le rapatriement s'écarte de ce que le texte scellé et la chaîne annoncent ; le dire.**
Texte scellé, « Devis » : « disque de l'instance arrêtée et gardée jusqu'au verdict, 72 h au plus » ; « Concordance », point 1 : « les activations de toutes les actions notées restent sur le disque de l'instance seulement » ; lanceur l. 346 et amorce l. 151 : « disque gardé jusqu'au verdict ». Aucune section gelée n'exige cette garde (vérifié : « Plan d'analyse », « Critères de lecture gelés », « Liste d'arrêt »), et le devis dit lui-même « une borne, non un droit ». L'écart est donc permis, mais il n'est écrit nulle part dans l'ordre, et Lazar le signe à la remise.

- § 4.13, première puce, à la fin. Ajouter → « **Déclaré** : le devis du texte scellé comptait une instance gardée arrêtée jusqu'au verdict de la table A (72 h au plus) ; elle est détruite plus tôt, sur décision de la mère (R-2112, R-2113). Perdus avec elle : les activations complètes des trois couches (recalculables par la passe unique, plan d'analyse, point 5) et tout fichier non poussé. Aucune section gelée ne demande cette garde. »
- En-tête, « Autorisation ». Ajouter → « R-2112, R-2113 : instance détruite dès le rapatriement vérifié (§ 4.13). »

**C8 — « au moins `1` morceau » ne dit pas que le sous-ensemble est complet.**
La variante B recalcule et compare ; un morceau manquant ne se verrait qu'après la création de son instance. Le nombre de morceaux est déjà public : `PROGRES … etape=episodes-ecrits … morceaux=N` (`lanceur_v6.py` l. 299), relayée au journal.

- § 4.12, « Attendu » des données. Texte actuel → « au moins `1` morceau » Texte corrigé → « autant de morceaux que le champ `morceaux=` de la ligne `PROGRES … etape=episodes-ecrits` de `progres.txt` (au moins `1`) ; aucune ligne `ERREUR DE CHAÎNE (C11)` au journal ».

**C9 — § 0 et § 11 : « mot de Lazar pour sa dépense » est dépassé.**
GO-2026-11-10-06 est inscrit (R-2115, `registres/go.md` l. 296).

- § 0 et § 11. Texte actuel → « (instance séparée, ordre d'exécution à part, mot de Lazar pour sa dépense ; R-2112) » Texte corrigé → « (instance séparée, ordre d'exécution à part, sous GO-2026-11-10-06 ; R-2112, R-2115) ».

### Mineurs

- **M1** — § 4.12 : `vastai stop` est dans le même bloc que l'inventaire, donc joué même si l'instance est déjà arrêtée. Scinder en deux blocs, ou conditionner : `bash "$W/inventaire.sh" | grep -E "^$ID t06-v2 (running|loading)" && timeout -k 5 120 vastai stop instance "$ID"`.
- **M2** — § 4.13 : à 7a, `show instance --raw` après destruction a rendu « un texte autre » et l'inventaire filtré a fait foi (R-2039). Écrire l'attendu : « l'un ou l'autre message ; **l'absence de l'identifiant dans l'inventaire filtré fait foi** ; encore présent après 60 s : une seconde demande, puis compte rendu ».
- **M3** — § 4.11 : le compte rendu à 60 USD ne se déclenche que si la fille compare l'heure à H60. Ajouter : « à chaque relance de la surveillance et à chaque relevé, `[ "$(date +%s)" -ge <H60> ] && echo "60 USD atteints"` ; sur H200, H60 tombe vers 12,5 h de marche » ; et : « code 1 de `depense 60` (cumul déjà à 60 USD à la création) : compte rendu aussitôt ».
- **M4** — § 4.10 (point 1 du § 13, à juger) : forme **acceptable**. Vérifié : la garde de la session ne se déclenche que sur le texte `vastai create` (`garde_calcul.py` l. 38, 148) et ne voit donc pas cette commande ; le lanceur rejoue la même garde sur le texte exact (l. 236) et le § 4.9 contrôle la ligne. Deux ajouts : empreinte du fichier relevée au § 4.9 (`sha256sum "$F"`) et revérifiée dans le bloc du § 4.10 ; exécution dans les dix minutes qui suivent l'impression, sinon nouvelle recherche.
- **M5** — § 4.1 : si `main` porte un jour `diag/`, `runs/` ou `donnees/` du run de 7a, les motifs `/diag/`, `/runs/`, `/donnees/` les extrairaient dans `$M`. Je n'ai pas vérifié leur présence (interdit). Défense sans coût : ajouter `'!/diag/20261109-070232-t06-reel/' '!/runs/20261109-070232-t06-reel/' '!/donnees/20261109-070232-t06-reel/'` aux exclusions (neuf écarts déclarés au lieu de six).
- **M6** — § 14, `ID_SESSION_FILLE` : dire qui le donne (Lazar, une fois la session ouverte, avant le scellement de l'ordre) ; à défaut, remplacer par « la session à laquelle Lazar remet cet ordre, qui écrit son identifiant en première ligne de son journal ».
- **M7** — P6 : la fille ne vérifie pas `ANT0`. Ajouter au § 4.3 : `git show HEAD:registres/depenses.md | grep -F -e GO-2026-11-02-28 -e GO-2026-11-10-01 | grep -vci engagement` (attendu `0` si `ANT0` vaut 0 ; sinon somme recopiée au journal). Vérifié ce jour : aucune ligne de dépense sous ces deux GO.
- **M8** — P10, § 4.7 : la « Liste d'arrêt » dit « une instance du programme déjà sur le compte : aucune création » ; la chaîne lit « étiquette qui commence par `t06-v2` » (`session_v2.verifier_instances`, l. 153). Écrire cette lecture dans l'ordre, et faire figurer au compte rendu les autres instances vues (identifiant, étiquette, état), que la fille ne touche pas.
- **M9** — § 4.0 : l'enveloppe pose `VAST_API_KEY=""` quand la variable est absente. Selon la façon dont `vastai` lit sa clé, une variable vide peut masquer le fichier de clé (non vérifié : outil absent ici). Si `VAST_API_KEY` est « absente » au § 4.0, le dire à la mère avant le § 4.8, ou ne passer la variable à `env -i` que si elle est présente.
- **M10** — § 4.0 : après « ARRÊT : $W existe déjà », le bloc continue et réécrit `v13.sh` et `inventaire.sh` (R12). Mettre le reste du bloc sous la condition du `mkdir`.
- **M11** — § 5, point 1 (b) : le texte scellé dit « erreur de mémoire à la distillation » ; l'ordre y joint l'étape « données de distillation ». Lecture défendable (le devis compte « distillation, génération des données comprise »), à écrire comme telle dans le message à Lazar, avec l'étape exacte.
- **M12** — § 4.3 : exiger aussi le chemin du texte de T0.7 (R-2103, D-4) : `[ "$P7" = prereg/T0.7-sondes-v0-v1.md ]`.
- **M13** — § 10 : nommer dans le compte rendu les trois valeurs que l'ordre de la variante B attend comme marqueurs : branche en vigueur (`BRANCHE_7B`), run (`RUN_T06_7B`), empreinte du manifeste (ligne `RUN-CONFIRMATION-T06`).
- **M14** — P5 et § 9 : le message de remise de Lazar se recopie verbatim, avec l'heure, au journal de la fille, comme ses autres mots.

## 3. Ce qui a été vérifié et trouvé conforme

- **Empreintes** : texte scellé `ef31feff…` et configuration `b7a5c1ba…` sur `main` ; les onze fichiers du § 1 de l'ordre recalculés au commit `1609a4bf`, égaux ; `git diff --quiet 1609a4bf HEAD` sur le lanceur, l'amorce et `src/controle_ia/t06/` : code 0 ; sous `.claude/`, seule `hooks/garde_calcul.py` diffère ; S ancêtre de la tête ; pièces du bras B `910a53dc…`, `4fb0da20…`, `317a7ea5…`.
- **Configuration** : GO-2026-11-02-28, plafond 200, dernier jour de création 2026-11-15, fin du GO 2026-11-17T00:00:00Z (`1794873600`, recalculé), A100 SXM4 ≤ 1,30, H200 NVL ≤ 4,70, stockage ≤ 0,08, disque 150, étiquette `t06-v2` : égaux au § 1.
- **Gardes de la chaîne, rejouées hors ligne** (code de `main`, égal au code gelé ; registre de `main`) : `session_v2 go` conforme les 10, 15 et 16, refus le 17 ; `calendrier` (v2 et v3) conforme les 10 et 15, **refus le 16** (« dernier jour de création (2026-11-15) dépassé ») ; les deux lignes attendues du § 4.4 sont, au caractère près, celles que le code imprime. GO en dur : lanceur l. 83, 123, 197, 204 ; amorce l. 60, 372, 398. La prolongation GO-2026-11-10-01 n'est lue nulle part : l'ordre le dit.
- **Commandes** : arguments de `controles`, `creation auto course|relance`, `surveillance`, `session_v3 depense` (6 et 7 arguments) conformes aux signatures ; les quinze noms de l'enveloppe ; les neuf variables de la commande imprimée (l. 235) et les expressions du § 4.9 ; codes 0, 2, 3, 4, 5 ; champs de `lancement.txt` ; messages des commits de l'amorce (l. 525, 529, 416, 435) ; étapes « données de distillation » et « distillation » (`lanceur_v6.py` l. 225, 237) ; clés du manifeste et valeur attendue (`depot_propre` et `reserves` : forcés par `creer_manifeste`).
- **Dépense** : 200 USD (lanceur l. 197, 226 ; minuterie l. 101 à 110) ; H60 par `depense 60` (dépense antérieure et téléchargement compris) ; 180 USD ; engagement mot pour mot celui du texte scellé.
- **H200** : § 5 conforme au texte scellé (en-tête, R-2077 et contre-lecture 6 : `creation auto relance` seulement après le mot, au bout de la fenêtre comme après une erreur de mémoire).
- **Embargo** : `lecture-sondes-t06.json` et son compagnon exclus des clones, des listes et du rapatriement ; les diffs par noms sans détection de renommage ne descendent aucun contenu ; sorties du bras B ni rapatriées ni ouvertes (le motif de run `…-t06-reel` et le motif des traces les écartent) ; `run.json` des traces est sans ligne de table (C02). Reste C1.
- **Concordance avec la variante B** (`b053a220…`, lu par `git show prep/t07-module-v2:…`) : elle lit `runs/<run>/manifeste.json`, `diag/<run>/episodes-t06.json`, `distillation-t06.json`, `arret.json`, et sous `donnees/<run>/` adaptateurs, mesures, textes, manifeste et morceaux ; tous poussés par l'amorce (l. 318 à 322, 523 à 529) et vérifiés par l'ordre de 7b ; son P1 (fin normale, rapatriement vérifié, instance de 7b détruite) et son P2 (`RUN-CONFIRMATION-T06` inscrite par la mère) s'accordent aux § 4.13, 10 et 11 ; étiquettes `t06-v2` et `t07-b-v1` sans conflit d'inventaire. Restent C8 et M13.
- **Marqueurs** : cinq, une occurrence chacun (compté). `DEPENSE_ANTERIEURE_USD` : `0` attendu, conforme au registre ce jour. `LIGNE_REGISTRE_BRAS_B` : `R-2092`. `LIGNE_SCELLEMENT_T07` : **non remplissable aujourd'hui**, `registres/scellements-v1.md` ne porte que les lignes des jeux J-D et J-A ; son format (clé, date, chemin, empreinte) est celui que lit le § 4.3. `COMMIT_MAIN_REMISE` : C3. `ID_SESSION_FILLE` : M6.
- **Préalables** : T0.7 scellé (P2), addendum du bras B (P7, à réécrire : C2), remise par Lazar (P5, § 9) sont tous posés avant toute création.

## 4. Ce que je n'ai pas vérifié

- Les gardes du § 4.6 n'ont pas été rejouées (ni clone, ni extraction : écritures git interdites) ; les sorties attendues (« observées par le rédacteur ») sont prises telles quelles. Concordent avec le texte scellé : entropie `31538212097275005629337336542801867913`, tâches `76cdeace…` et `8d20a698…`, « Tests attendus : `2022` ».
- Aucune commande de `vastai` ni de réseau : forme des réponses de l'outil, version 1.8.3, texte de `show instance` après destruction, lecture de la clé (M9).
- Aucune pièce de 7a (run, traces, lecture A) : les repères de durée du § 4.11 et le devis sont comparés au seul texte scellé.
- Le contenu de l'addendum v3 du bras B, de l'ordre de 7a et de ses addenda, des brouillons 1 et 2 de l'ordre de 7b (le brouillon 2 a seulement été comparé au 3 : les seuls changements sont ceux du journal).
- Le préenregistrement de T0.7 (non scellé ce jour) et le code de la variante B ; seule la liste de ce qu'elle lit a été rapprochée.
- La présence ou l'absence des dossiers de 7a sur `main` (M5).
- Si la session fille et la mère sont sur le même compte (C4).

## 5. Gestes à déclarer

- `git diff --stat 1609a4bf 935262b1` sans restriction de chemin (79 fichiers ajoutés par S ; douze derniers noms affichés, tous des compagnons de rapports et les quatre fichiers de `prereg/`) : parcours mécanique de tout l'arbre des deux commits, aucun contenu affiché.
- `git for-each-ref` filtré sur `t07-module-v2` : les noms de toutes les branches sont passés dans le tube, un seul est sorti.
- `ls registres/` : le nom `index-bras-attaque-v1.md` s'est affiché ; fichier non ouvert.
- Aucun refus de permission ni de classifieur. Aucun appel externe, aucune dépense, aucune écriture git, aucune valeur de clé lue ; aucun `lecture-sondes-t06.json`, aucune pièce de 7a, aucun chemin du bras d'attaque ouvert.
