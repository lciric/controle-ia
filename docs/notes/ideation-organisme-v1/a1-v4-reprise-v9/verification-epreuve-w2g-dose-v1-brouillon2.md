# Vérification (R2) — texte court de l'épreuve hors ligne « W2 gradué », brouillon 2

**Objet** : `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/epreuve-w2g-dose-v1-brouillon2.md`, 237 lignes, sha256 `6bb4f6ec1380100169acbed26624cdae4f644c38c7c2f3ae7045300ed394e962` (relevée par `sha256sum`, égale à l'empreinte attendue). Question posée : le brouillon 2 applique-t-il correctement la contre-lecture du brouillon 1, sans introduire de défaut, et est-il scellable ?

**Vérificateur** : sous-agent neuf, modèle Fable 5.1 (autre modèle que le rédacteur du brouillon 2, Opus 5.5 ; N-052), qui n'a écrit ni le brouillon 1, ni le brouillon 2, ni la contre-lecture, ni le lecteur, ni ses essais, ni le brouillon 3, ni le code v5. Rédigé le 8 novembre 2026, de 19:56 à 20:05 UTC environ (`date -u`).

**Gestes faits** : `sha256sum` de huit pièces (brouillon 1 `829db6a5…`, brouillon 2 `6bb4f6ec…`, contre-lecture `2f422a63…`, lecteur `a9f462cb…`, essais du lecteur `6f5d3b61…`, patch du lecteur `26a37cd8…`, sortie des essais `e2ada891…`, brouillon 3 `c44f52cc…`, script de l'épreuve `c691a43d…`, cœur v5 `8692746a…`, patch v5 `12c39347…`, rapport v5 `c31d23b8…`) : **toutes égales aux empreintes citées par le texte**. `diff` du brouillon 1 et du brouillon 2 (sortie lue en entier par lecture parallèle des deux textes). Lecture **en entier** du lecteur, de ses essais, du script de l'épreuve, de la contre-lecture, des deux brouillons ; des fonctions `graine`, `verifier_entropie`, `wilson` du cœur v2 ; de `ecrire_scelle`, `ecrire_json_scelle`, `verifier_scelle`, `normaliser_texte` de `pole/outils.py` ; de `sceller` de `src/controle_ia/scellement.py` ; des lignes 71, 115–119, 126, 256, 262, 288 du brouillon 3 ; des lignes 59, 82, 109–114 du rapport v5 ; des lignes R-1897, R-1923, R-1926, R-1928, R-1929 du registre des décisions (l. 1855, 1881, 1884, 1886, 1887) ; de la sortie des essais (43 essais, « OK »). Par programme (`python3 -I`) : la citation de la règle du § 2 comparée au brouillon 1 et à la l. 126 du brouillon 3 ; le motif `<<[A-Z0-9_]+>>` cherché dans le brouillon 2. Une **copie de travail temporaire** dans mon dossier de brouillon (clone du dépôt public, `git checkout --detach 8947bc80…`, `git apply --check` puis `git apply` des **deux** patchs) : sept lignes « ?? », onze empreintes égales (huit modules, lecteur, essais, `pole/outils.py`), `--help` des deux scripts (code 0), lecteur sans `--duree-max-attendue` (code 4), lecteur sur un dossier vide disposé **exactement comme les chemins de la commande du § 4 bis** (dossier `…/epreuve-w2g-dose-v1-rejeu-v1`, lecture à côté) : code 2, garde 1 `sortie_absente`, lecture d'arrêt écrite et scellée à côté ; lecture demandée **dans** le dossier : code 4. Copie et dossier d'essai effacés. **L'épreuve n'a pas été exécutée ; les essais du lecteur n'ont pas été rejoués** (leur sortie scellée a été lue). Rien lu sous `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; aucune variable d'environnement affichée, aucune clé ; aucun fichier existant modifié ; aucun commit.

---

## Verdict

**Scellable après corrections de forme.** Aucun constat bloquant. **Un majeur** (de forme, inévitable : l'en-tête, la section 7 et l'annexe C décrivent encore un brouillon non vérifié et une proposition en attente ; la version scellée doit dire ce qu'elle est). **Sept mineurs**, aucun sur la règle, la grille, le seuil, le calcul de λ\*, les gardes ni les commandes. Les quatre majeurs et les onze mineurs de la contre-lecture sont traités, et traités correctement ; les six gardes de la section 6 sont celles du lecteur gelé, motif pour motif et dans son ordre ; les deux commandes sont exactes ; la règle de choix est identique au caractère près à celle du brouillon 3.

Mise en garde sur la consigne reçue (« marqueur levé par l'empreinte du fichier scellé ») : le marqueur **ne peut pas** être remplacé par l'empreinte du fichier (l'empreinte dépend du contenu, qui contiendrait l'empreinte : circulaire). L'annexe A du texte le traite correctement : le marqueur est levé par les **mots** « l'entier gros-boutiste de l'empreinte SHA-256 du présent fichier scellé, lue par `--entropie-texte` », déjà présents à la l. 81 juste après le marqueur ; la levée consiste à **supprimer** le jeton `<<ENTROPIE_EPREUVE>>` (et le point qui le suit), rien d'autre. L'empreinte naît au scellement et n'est écrite qu'au registre et dans les manifestes.

---

## Réponses aux cinq points demandés

### (1) Les 4 majeurs et les 11 mineurs : chacun traité, et correctement ?

| constat | traité ? | où (brouillon 2) | vérification |
|---|---|---|---|
| M-1 sortie complète fixe λ\* | oui | § 6 l. 186 ; § 5 l. 163 ; § 4 bis codes 0 et 3 | une sortie complète = code 0 du script, gardes passées, lecteur à 0 **ou 3** ; « aucune dose » est aussi définitif (nœud de Lazar) ; 0,40 et 0,50 acceptées d'avance, « ou toute autre dose rendue » ; texte neuf réservé à une trace arrêtée ou refusée. Conforme à la correction demandée, et plus complet (le code 3 du lecteur y est). |
| M-2 lecteur gelé | oui | § 4 tableau des pièces gelées l. 87–96 ; préalables 1 et 6 ; § 6 bis ; annexe B C1 | quatre empreintes écrites, exigées au registre **avec** celle du texte avant le lancement ; aucune modification après ; correction = version neuve, motif au registre **avant** relecture, deux lectures rapportées, λ\* divergents → Lazar ; la lecture porte l'empreinte du lecteur (code l. 513, vérifié). Conforme. |
| M-3 dose absente | oui | § 6 garde 2 l. 178 | `dose_absente` (`presentes != list(GRILLE_DOSES_W2G)`, ordre compris, code l. 280–286), `dose_manquante` (≠ champ `doses`, l. 287–288), `dose_incomplete` (`complete`, `repetitions` sur la dose et sur les quatre lignes, l. 289–293). Texte = code. |
| M-4 règle et cohérence des fichiers | oui | § 6 garde 3 l. 179 | seize motifs, **dans l'ordre exact du code** (l. 309–358) : `texte_non_scelle`, `incoherence_fichiers` (cinq champs), `mode`, `entropie`, `texte_sha256`, `texte_chemin`, `entropie_sous_2_64`, `grille`, `repetitions`, `processus`, `duree_max`, `versions`, `modules`, `epreuve`, `lignes`, `regle` (0,8 ; 0 sur les deux fichiers). Chemins exacts (`reglages.*` ; le fichier de résultats sans champ `texte`) : exacts, vérifiés sur le script de l'épreuve (l. 197–202, 233–237). |
| m-5 analogue de P10 | oui | § 5 l. 165 ; annexe C écart 1 | le lecteur imprime « P10 tenue par l'oracle » / « P10 en tension à λ\* » (code l. 473) ; le texte écrit la correspondance d'avance, même seuil 0,50 (`SEUIL_P10`), même comparaison (≥). Traitement sans changement de code, accepté par la mère (R-1929). Correct. |
| m-6 grille contient 0,0 | oui | § 2 l. 39 | « 11 doses dont 0,0 » ; `GRILLE_DOSES_W2G` l. 74 du cœur v5 : exact. **Une citation de ligne fausse** (héritée de la contre-lecture) : voir m-V2. |
| m-7 `choisir_dose` n'exclut pas 0 | oui | § 2 l. 39 ; § 6 gardes 5 et 6 | script l. 142–147 : exact ; `lambda_recalcule` exclut `dose <= 0` (lecteur l. 186) ; `lambda_dose_nulle` (l. 393–394) et `desaccord_lambda` ; garde 5 à la dose 0. Correct. |
| m-8 égalité du nom de clé | oui | § 6 garde 4 l. 180 | `cles_interdites` (l. 154–165) : `normaliser_texte(k) == "verite"` ou `k == "N"`, récursif, clés seulement. Texte = code. |
| m-9 marge de durée | oui | § 4 l. 85 ; commande l. 127 | `--duree-max-s 6700` sous `timeout 7000`, délai d'outil 7 200 ; ×1,49 sur 4 500 : exact ; `--duree-max-attendue 6700` au lecteur ; valeur de la mère R-1926. |
| m-10 essais | oui | § 6 ter l. 196 | vrai code 3 (`--duree-max-s 0.5`, essais l. 78, 325–332), cas sain au bassin (`--processus 2`, l. 77, 265–274), dose 0 retirée (l. 334–337) : présents dans les essais ; 43 passés, 0 échec, 0 sauté : égal à la sortie scellée (19:45:52 à 19:46:58). |
| m-11 « à la limite » → brouillon 4 seulement | oui | § 5 l. 164 | « et rien d'autre : ni rejeu, ni changement de grille, ni de seuil, ni de règle ». Correct. |
| m-12 antériorité de la règle | oui | § 2 l. 34 | « rendue à 17:00 UTC (R-1897, l. 1855), avant la première épreuve (17:19) » : R-1897 vérifiée (l. 1855, 17:00 UTC), rapport l. 59 (17:19 UTC). Correct. |
| m-13 secondes-processus | oui | § 4 l. 79 | 1 000 × 1,93 = 1 930 ; 1 930 − 200 × 1,93 = 1 544 ≈ 1 540. Correct. |
| m-14 console | oui | § 4 l. 123, 132–137 | chemin complet `$CONSOLE`, **à côté** du dossier (non dedans), scellée par `controle_ia.scellement sceller` (format « empreinte, deux espaces, nom », l. 72 de `scellement.py`, lu par `verifier_scelle` : `split()[0]`, compatible) ; lue par le lecteur, garde 1, exactement une ligne « code N » (`lire_code_console`, l. 168–175). Correct. |
| m-15 inversions et évaluations impossibles | oui, **avec un écart déclaré** | § 5 l. 166–167 ; § 6 « ce qui n'est pas un arrêt » | inversions de (a) : rapportées en information par la mère sur les bornes de Wilson écrites (le lecteur ne les cherche pas : exact, annexe C écart 2). Évaluations impossibles : le seuil d'arrêt proposé par la contre-lecture est **écarté et déclaré**, décision de la mère (R-1928 « rapportées sans arrêt », R-1929 « seuil … écarté, déclaré ») ; le choix est écrit avant lecture, sans seuil, λ\* inchangé quel que soit le compte, audit écrit avant report : conforme à R1 (aucun choix laissé après lecture). Un point de suite manque : voir m-V7. |
| demande R-1928 (commande de lecture, codes) | oui | § 4 bis | voir (3) et (4). |

### (2) La règle de choix est-elle identique à la l. 126 du brouillon 3 ?

**Oui, au caractère près**, vérifié par programme : la citation du § 2 du brouillon 2 est égale à celle du brouillon 1 et à l'extrait de la l. 126 du brouillon 3 (`c44f52cc…`). Les précisions du § 2 ne changent pas le sens : « au moins 800 sur 1 000 » est ce que fait le script (`taux ≥ 0.80`, l. 146 ; 800/1 000 et 0,8 ont la même représentation flottante) et ce que recalcule le lecteur en entiers (`5·promues(a) ≥ 4·n`, l. 190 : mathématiquement équivalent, et sans question d'arrondi) ; « (b) = 0 » à la même dose : `PROMOTIONS_RECOMBINAISON_MAX = 0`, l. 54 ; doses complètes seulement. L'exclusion de la dose 0 par le recalcul du lecteur (`dose <= 0`, l. 186) ne modifie aucun résultat possible : à la dose 0 la loi du monde est W2, membre du nul v9, (a) y vaut 0 par certificat ; si (a) > 0 à la dose 0, la garde 5 arrête avant tout choix. La variante « borne basse » reste écartée pour le motif de R-1923.

### (3) Les deux commandes sont-elles exactes au regard des deux scripts ?

**Oui.** Rejeu (§ 4 l. 125–128) : `dossier` positionnel ; `--entropie-texte` (groupe exclusif obligatoire avec `--graine`), `--repetitions`, `--processus`, `--duree-max-s` existent (`--help`, code 0, lu dans la copie) ; `--doses` omise → grille gelée des 11 doses (l. 68–69) ; dossier absent accepté (`makedirs`, l. 196), non vide refusé (l. 179) ; `$?` après `… 2>&1 ;` est le code de `timeout`, donc du script (0, 2, 3) ou 124 ; `-I -B` : numpy 2.5.3 et python 3.13.18 importables sous `-I` (vérifié : `python3 -I -B … --help` charge `pole` et `numpy`). Le script écrit `reglages.texte.chemin = abspath($TEXTE)` (l. 192) ; le lecteur compare par `realpath` au `--texte` reçu (l. 327) : même `$TEXTE`, égalité assurée. Aucune ligne de la console ne peut commencer par « code » hors celle de l'`echo` (lignes de `date -u`, de `loadavg`, de la table « dose λ | … », « règle du texte … », « durée … », « arrêt : … », « refus : … »).

Lecture (§ 4 bis l. 143–147) : `dossier` positionnel ; `--texte`, `--console`, `--lecture`, `--duree-max-attendue` obligatoires ; `--repetitions-attendues`, `--processus-attendus` facultatifs : tous présents (`--help`, code 0) ; `--duree-max-attendue 6700` est un flottant comparé à `reglages.duree_max_s` = 6700.0 écrit par le script (`type=float`, l. 176) : égal ; `$LECTURE` est **à côté** du dossier : accepté (essai fait, code 2 `sortie_absente` sur dossier vide, lecture d'arrêt écrite et scellée à côté ; une lecture dans le dossier est refusée, code 4) ; `$?` après `cd … && python3 … ; echo` est le code du lecteur. La lecture est faite après le scellement de la console : nécessaire, la garde 1 vérifie le compagnon de la console.

### (4) Les suites de chaque code sont-elles cohérentes avec « une sortie complète fixe λ\* » et avec R12 ?

**Oui**, avec une précision à écrire (m-V4). Code 0 → λ\* définitif ; code 3 → « aucune dose » définitif, nœud de Lazar ; les deux sont la « sortie complète » du § 6 l. 186. Code 2 → aucune dose lue ; garde la plus petite 1 à 4 → texte neuf (`…-v2.md`, entropie neuve) ; 5 ou 6 → nœud de Lazar avant tout texte neuf ; le lecteur rapporte la plus petite garde et toutes les refusantes (`garde`, `gardes_refusees`, l. 523) : la suite est bien définie. Code 4 → rien n'est écrit (vérifié : l. 503–512 avant toute lecture) ; si `$LECTURE` existe, la première lecture fait foi. Code 1 → § 6 bis (lecteur v2, lecture `-lecture-v2.json`). R12 : texte neuf = nom neuf, lecteur neuf = nom neuf, lecture neuve = nom neuf ; **mais** le texte ne dit pas que le dossier de sortie, la console et la lecture d'une seconde tentative prennent aussi des noms neufs (`…-rejeu-v2…`) ; le préalable 2 l'impose de fait (il exige leur absence) : à écrire (m-V4). Le refus du script (code 2 : rien joué, rien lu) compte comme « trace refusée » et demande un texte neuf : plus strict que nécessaire (aucune entropie consommée), mais cohérent avec « un scellement, un rejeu, une lecture » ; ce n'est pas un défaut.

### (5) Scellable en l'état, une fois le marqueur levé ?

**Non en l'état, oui après les corrections ci-dessous**, toutes de forme. Le marqueur : une seule occurrence de `<<[A-Z0-9_]+>>` dans le fichier (`<<ENTROPIE_EPREUVE>>`, l. 81) ; `DOSE_LAMBDA` est écrit en mots (« entre doubles chevrons ») et n'est pas pris par le motif. La levée est la suppression du jeton (voir la mise en garde du verdict). Ce qui empêche de sceller tel quel : le titre et la ligne de statut (l. 1, 3) disent « brouillon 2 … non encore vérifiées … non scellé ; un marqueur restant » ; la section 7 (l. 200) dit que la vérification est à faire ; l'annexe C (l. 219) soumet une proposition déjà tranchée (R-1929). Une version scellée qui se décrit comme un brouillon non vérifié n'est pas lisible ; ce sont les retouches normales de passage à `epreuve-w2g-dose-v1-v1.md` (M-V1).

---

## Constats

Classes : **B** bloquant (le texte ne peut pas être scellé tel quel), **M** majeur (à corriger avant scellement), **m** mineur (à corriger de préférence, sans enjeu de fond).

### Bloquants

Aucun.

### Majeurs

**M-V1 — En-tête, section 7 et annexe C encore au présent du brouillon (l. 1, 3, 200, 219).** À corriger avant le scellement, dans la version `epreuve-w2g-dose-v1-v1.md` :
- l. 1 : « (texte court, brouillon 2) » → « (texte court, v1, scellé) » ;
- l. 3 : remplacer « corrections non encore vérifiées par un autre modèle ; non scellé ; un marqueur restant (annexe A) » par « corrections vérifiées par un autre modèle (`verification-epreuve-w2g-dose-v1-brouillon2.md`, sha256 à relever) ; scellé ; aucun marqueur » ;
- l. 200 (section 7) : « Le présent brouillon 2 est **vérifié** avant scellement par … » → « Le brouillon 2 **a été vérifié** avant scellement par un sous-agent neuf d'un autre modèle (Fable 5.1), qui n'avait écrit ni ce texte, ni le lecteur : `verification-epreuve-w2g-dose-v1-brouillon2.md`, sha256 `…` : scellable après corrections de forme, 0 bloquant, 1 majeur de forme, 7 mineurs, tous appliqués ici » ; la liste « Fichiers à lui donner » et « À vérifier » passe au passé ou s'allège ;
- l. 219 (annexe C) : « **Proposition à la mère** (routine) : garder le lecteur tel quel … (confiance 0,7) ; sinon … » → « **Décision de la mère** (routine, R-1929) : lecteur gardé tel quel, scellement avec les traitements ci-dessus » ;
- l. 204 (annexe A) : « **Marqueur restant** : … à lever **au scellement** … » → « **Marqueur levé** : `ENTROPIE_EPREUVE` a été levé par les mots de la section 4 ; zéro occurrence du motif `<<[A-Z0-9_]+>>` vérifiée par programme avant scellement » ;
- l. 81 : supprimer « `<<ENTROPIE_EPREUVE>>`. » (la phrase « Levée retenue (R-1926 …) : l'entropie est l'entier gros-boutiste … » reste et suffit).
Ces retouches ne touchent ni la règle, ni la grille, ni les gardes, ni les commandes ; aucune ne doit être faite après le scellement.

### Mineurs

**m-V2 — Citation de ligne fausse, héritée de la contre-lecture (l. 39).** « `verifier_plan` du cœur v5, l. 459–460, la refuse en course » : le refus de la dose 0 est aux **l. 457–458** (`if d <= 0.0: raise AttaqueRefusee("dose_w2g : 0 refusé …")`) ; les l. 459–460 refusent une dose **hors grille**. Écrire « l. 457–458 ».

**m-V3 — « s'arrête à son premier motif » et « tous leurs motifs sont rapportés » (l. 175).** La garde 1 s'arrête à sa première **étape** et rapporte tous les motifs de cette étape (par exemple quatre `sortie_absente` pour quatre fichiers absents, vu à l'essai ; plusieurs `forme` possibles). La garde 3 s'arrête à `texte_non_scelle` (seul motif rendu alors, lecteur l. 309–310), tandis que les gardes 2 et 4 sont tout de même évaluées. Écrire : « elle s'arrête à sa première étape, dont tous les motifs sont rapportés … ; puis les gardes 2, 3 et 4 ensemble (… tous leurs motifs sont rapportés, sauf que la garde 3 ne rend que `texte_non_scelle` quand le texte n'est pas scellé) ».

**m-V4 — Noms d'une seconde tentative (l. 188).** Ajouter après « demande un texte neuf (`…-v2.md`, R12) » : « et des noms neufs pour le dossier de sortie, la console et la lecture (`…-rejeu-v2`, `…-rejeu-v2-console.txt`, `…-rejeu-v2-lecture-v1.json`), le préalable 2 exigeant l'absence des trois ».

**m-V5 — « tous acceptés par la mère, R-1926 » (l. 3).** Le seuil d'arrêt proposé par m-15 a ensuite été écarté (R-1928, R-1929) et le texte le déclare au § 5 ; écrire « tous acceptés (R-1926), le seuil d'arrêt proposé par m-15 étant ensuite écarté et déclaré (R-1928, section 5) ».

**m-V6 — Décisions citées par numéro de ligne d'un fichier vivant (l. 5, 34, 44, 200, 237).** Les numéros de ligne de `registres/decisions.md` bougeront ; les identifiants R-… suffisent et sont stables. Garder les identifiants, écrire les numéros de ligne comme « au 8 novembre » ou les retirer. Sans enjeu de fond.

**m-V7 — Suite de l'audit des évaluations impossibles (l. 167).** Le texte dit ce que l'audit **ne** fait **pas** (il ne change pas λ\*) mais pas ce qu'il peut entraîner. Ajouter : « si l'audit trouve un défaut de l'instrument, il est rapporté à Lazar (nœud) ; la mère ne substitue jamais une autre dose ni ne relance ». Cela ferme la dernière porte sans ajouter de seuil.

**m-V8 — Préalable 2 (l. 100).** Ajouter l'absence des compagnons : `test ! -e "$CONSOLE.sha256" && test ! -e "$LECTURE.sha256"` (le lecteur refuse déjà sur `$LECTURE.sha256`, code 4, l. 504 ; `controle_ia.scellement sceller` refuse une empreinte différente déjà présente). Confort, sans enjeu.

---

## Ce qui a été vérifié et tient

- Citation de la règle identique (brouillon 2 = brouillon 1 = brouillon 3 l. 126, par programme) ; précisions sans changement de sens ; variante « borne basse » écartée pour le motif de R-1923.
- Les six gardes du § 6 = les fonctions `garde_1` à `garde_6` du lecteur `a9f462cb…`, **motif pour motif** (34 motifs : 6 + 6 + 16 + 2 + 2 + 4), **dans l'ordre du code**, avec l'ordre d'application de `lire` (1 seule ; 2, 3, 4 ensemble ; 5 ; 6). Aucune garde du texte absente du lecteur, aucune garde du lecteur absente du texte.
- Les quatre écarts de l'annexe C sont réels, correctement décrits et sans effet sur λ\* : mots de P10 (code l. 473) ; inversions non cherchées par le lecteur ; motifs `epreuve`, `lignes`, `lecteur` sans essai propre (vérifié sur les 43 essais : aucun ne les déclenche ; toutes les autres gardes et motifs ont un artefact) ; détails chiffrés des gardes 5 et 6 (code l. 374, 376, 396) — « sans table ni intervalle » est le mot juste.
- § 6 ter conforme aux essais et à leur sortie scellée : 43 passés, 0 échec, 0 sauté, 19:45:52–19:46:58 UTC ; courses à `--processus 1` et `2`, `--duree-max-s 6700` et `0.5` ; refus attendus des sorties exploratoires (`mode`, `entropie`, `texte_sha256`, `texte_chemin`, `entropie_sous_2_64`, `grille`, `dose_absente`).
- Empreintes : les huit `MODULES_SHA256` du lecteur = les huit du § 4 point 3 = les huit relevées sur la copie patchée ; lecteur, essais, `pole/outils.py` égaux ; patch du lecteur s'applique après le patch v5 sur `8947bc80…` ; sept lignes « ?? » (cinq v5, deux lecteur).
- Codes de sortie du lecteur (0, 2, 3, 4, et 1 non volontaire) et leurs effets (lecture écrite ou non, scellée, refus d'écraser, refus dans le dossier) : conformes au code (l. 65–70, 497–544) et à l'essai fait.
- Constantes : `MODE_DECISIF`, `PYTHON` 3.13.18, `NUMPY` 2.5.3, `LIGNES`, `REGLE_DE_CHOIX` (0,8 ; 0), `SEUIL_LIMITE` 0,80, `SEUIL_P10` 0,50, `GRILLE_DOSES_W2G` (11 doses dont 0,0) : égales au texte ; machine : `nproc` 4, python 3.13.18, numpy 2.5.3.
- Chiffres du § 3 : inchangés depuis le brouillon 1 (déjà vérifiés par la contre-lecture) ; empreintes des six fichiers exploratoires égales au rapport l. 109–114.
- Numéros de ligne cités du script de l'épreuve (54, 58–60, 67–69, 82, 131, 139–148, 142–147, 172–176, 188–192, 208–209, 227–228, 231), du cœur v2 (104–108, 750) et du cœur v5 (74) : exacts ; une erreur (m-V2).
- Durée : 6 700 < 7 000 < 7 200 ; ×1,49 sur ≈ 4 500 s attendues ; `timeout` signale tout le groupe de processus (les enfants du bassin aussi), donc un code 124 ne laisse pas d'orphelins de calcul.

## Décompte

| classe | nombre |
|---|---|
| bloquant | 0 |
| majeur | 1 (M-V1, de forme) |
| mineur | 7 (m-V2 à m-V8) |

**Verdict : scellable après corrections** (M-V1 obligatoire ; m-V2 à m-V5 et m-V7 recommandés ; m-V6 et m-V8 au choix de la mère). Aucune correction ne touche la règle, la grille, le seuil, les gardes, les commandes ni les empreintes gelées ; aucune ne demande une version neuve du lecteur ni de ses essais. Après ces retouches et la levée du marqueur, le texte est scellable sous `epreuve-w2g-dose-v1-v1.md`.
