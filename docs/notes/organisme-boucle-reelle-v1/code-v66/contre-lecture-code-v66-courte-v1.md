# Contre-lecture courte du différentiel v65 → v66 de l'organisme d'idéation (boucle réelle) — v1

- **Contre-lecteur** : sous-agent neuf de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, modèle Claude Fable 5.2 (`claude-fable-5-2`), autre modèle que le développeur de la v66 (Claude Opus 5.5) : N-052. Je n'ai écrit ni la v65, ni la v66, ni la contre-lecture de la v65.
- **Heures** (temps universel, relevées par `date -u`, 10 novembre 2026) : début 13:44:08 ; suite rejouée 13:44:50 → 13:51:25 ; banc du développeur rejoué 13:45:00 → 14:14:26 ; essai à blanc rejoué 13:49:58 → 13:50:58 ; mes mutations 13:52:03 → 14:23:53 ; rapport écrit à partir de 14:25. La machine était chargée par d'autres sessions (charge moyenne relevée à 13 sur 4 cœurs à 14:09) : mes durées sont plus longues que celles du développeur, les comptes sont égaux.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-contre-lecture-courte-v66-v1.md`, sha256 `0d068b2321bb71e738ad66f3294ec4e9d87dfb5d000faa6c5d2467afdb5cf09e`, vérifiée avant lecture. Interdits communs v2 suivis : aucun fichier interdit ouvert, aucune recherche récursive sur un dossier qui en contient, aucune variable d'environnement lue ni affichée, aucun appel de modèle, aucun réseau, aucune dépense, aucune instance. Aucun refus de classifieur rencontré.
- **Arbre** `/home/user/organisme-v65-cl`, branche `prep/organisme-v66-boucle-reelle-v1`, tête `7e415cbaaa3ff602db43a44dad6b4307c08352c7` avant et après ; `git status` vide avant et après ; aucun `checkout`, `commit`, `push`, `fetch`. Toute mutation a été jouée sur une copie dans mon bac à sable. Je n'ai nettoyé que mon bac à sable.
- **Aucune dépense.**

## 0. Verdict

**« Utilisable pour la course »**, code v66 inchangé, **sous trois conditions hors du code** : deux écritures au texte à sceller (CLV66-01, CLV66-02) et un nœud sur les conditions des deux GO (CLV66-07).

- Les dix corrections CLV65-01 à CLV65-10 sont faites et tiennent, au code et par essais (cas sain et artefact). La suite, le banc et l'essai à blanc se rejouent à l'identique.
- **Aucun constat bloquant dans le code** : rien ne touche une dépense, et je n'ai trouvé aucun chemin par lequel un relevé **produit par le cœur gelé** recevrait une issue fausse.
- Deux constats touchent la lettre de la section 8 du brouillon du texte (CLV66-01 : un arrêt de la garde 18 en génération 2 n'est pas lu « C4 (partielle) » ; CLV66-02 : P6 est tenue à vide si deux champs manquent au relevé). Les deux cas ne peuvent pas être produits par le cœur gelé (vérifié à la lecture, section 3). Ils se lèvent au texte (ce que je recommande) ou par une v67 (petite, mais noms neufs et nouvelle contre-lecture).
- **Ce qui changerait mon verdict** : si la mère veut que la lecture gelée refuse par elle-même tout relevé où ces champs manquent, sans clause au texte, c'est « après corrections » (CLV66-01 et CLV66-02 au code).

## 1. Ce que j'ai rejoué

Interpréteur `/home/user/controle-ia-travail/.venv/bin/python -I -B` ; `TMPDIR` et `--basetemp` dans mon bac à sable.

| pièce | annonce du développeur | ce que j'obtiens |
|---|---|---|
| empreintes des 58 fichiers versés contre leurs compagnons | conformes | 58 sur 58 ; rapport `f6433d38…`, contre-lecture v65 `c4ddfc7f…`, consigne du développeur `264e8a08…` égales |
| empreintes des cinq fichiers gelés v66, de l'outil, de la configuration, du banc (tête `7e415cb`) | table de la section 3 | égales |
| empreintes de deux fichiers d'essais (tête `7e415cb`) | `194d342f…` et `895cabf5…` | **`277ed353…` et `2c4f9773…`** : la table donne celles du commit `3ba4727` (CLV66-06, mineur) |
| suite des neuf fichiers (`POLE_ESSAI_BAC_REEL_NON_JOUE=1`) | `323 passed, 4 skipped, 326 subtests passed` | **`323 passed, 4 skipped, 326 subtests passed in 394.56s (0:06:34)`**, code 0 ; les quatre sautés sont les essais du vrai bac (`-rs`) |
| banc de mutations v66 (`--processus 3`) | `133 tuées pour la raison attendue sur 133` | **`133 tuées pour la raison attendue sur 133 mutations`**, code 0 ; mutation par mutation, mêmes issues et mêmes essais en échec que `mutations-v66-final.json` |
| essai à blanc, 14 étapes (script versé `6e864ed6…`, vrai registre et dossier `configuration-v6/` donnés) | codes 2, 0, 0, 3, 0, 3, 2, 2, 3, 0, 2, 0, 0, 0 | **mêmes codes** ; sorties d'étapes égales après retrait des chemins, des durées et des empreintes ; lectures C1, C5, C5 |
| décisions des trois relevés à blanc (cartes, lois plantées, promotions, verdicts, retenues, vues servies, archives, incidents, recherche de la loi plantée, lignes de tranche) | — | **égales** à celles des relevés versés ; relevé non reproductible à l'octet (le mien `4e9fe665…`, le sien `81b7fb54…`), comme dit |
| blocs du texte (étape 12) | `9933ee11…`, héritage `93dcf517…` | égaux à l'octet |
| vrai registre des GO (étape 13, lecture seule, `2c396b01…`) | 255 identifiants, 34 lignes d'extension ; 45 lu pour les deux GO ; 40 et 50 refusés | égal |
| dossier de course (étape 14) | « configuration v6 conforme `4743ddbe…` » | égal ; la configuration versée est l'exemple de l'arbre, à l'octet ; v5 → v6 ne change que les chemins des commandes, le nom de la section, le retrait du GO et l'en-tête |

Sorties gardées dans mon bac à sable (`/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/cl-v66/`) : `sorties/suite.txt` `208c6a73…`, `sorties/banc.txt` `cd4615d5…`, `sorties/banc.json` `dd5812e4…`, `sorties/mes-mutations.txt` `cc88a2f0…`, `sorties/mes-mutations.json` `8c1be656…` ; sondes : `sondes/sonde_lecture.py` `dc5a4833…`, `sondes/sonde_coeur.py` `3b34c7dc…`, `sondes/sonde_registre.py` `e2310525…`, `sondes/mes_mutations.py` `fbd85a74…`, `sondes/comparer_blanc.py` `aa6445a2…`. Dossiers provisoires retirés.

## 2. Mandat 1 — les dix constats de la contre-lecture v65

Lignes de `pole/boucle_reelle_v66.py` (cœur), `pole/lecture_boucle_reelle_v66.py` (lecture), `demonstrations/boucle_reelle_v66.py` (lanceur), `pole/registre_go_v66.py` (registre).

| constat | levé ? | au code | par essai (sain / artefact) et par mes sondes | réserve |
|---|---|---|---|---|
| **CLV65-01** lecture qui prononce C1 sans fausse jugée | **oui** | lecture 82-127 (`completude`), 195, 208-225 ; A1 : 255-258 | les six altérations de la contre-lecture v65 rendent C5 (essai `test_C5_releve_incomplet…`) ; mes 25 altérations (section 3) : toutes les conditions de P1 refusent | P6 reste vraie à vide sur deux champs : CLV66-02 |
| **CLV65-02 (a)** arrêt qui masque une brèche | **oui** | cœur 421-449 (jugements écrits avant l'étage), 459-469 | étape 9 de l'essai à blanc (12 cartes et 10 lois plantées au relevé partiel) ; `test_artefact_arret_ne_masque_pas_une_fausse_promue` ; ma sonde : fausse promue en génération 2 puis arrêt à la relecture finale → C5, « C4 (partielle) » et « C2 (partielle) » | un arrêt **dans** le juge (garde 18) n'écrit rien : CLV66-01 |
| **CLV65-02 (b)** héritage refusé non lu comme écart | **oui** | cœur 547-554, 579-584 (empreinte relue sur disque, en octets) ; lecture 149-153, 176-178 | trois essais d'artefact ; branche « lue ≠ écrite » atteinte | — |
| **CLV65-03** vue servie non vérifiée | **oui** | garde 23 : cœur 141-169, 364-374, 388-392 ; lecture 144-146, 161-163, 170-172 | `test_artefact_la_generation_2_ne_sert_que_K1` (arrêt, incident 23, C5 et C4 partielle) ; mes mutations K02 à K05, K11, K12 tuées | la garde vérifie le texte **remis à l'adaptateur** (`ProposeurAdaptateur.proposer`), pas ce que la commande externe transmet ensuite ; la lecture ne recompare pas les textes reçus (CLV66-03) |
| **CLV65-04** gardes sans essai sur artefact | **oui** | essais v66 | les 26 mutations tirées des miennes de la v65 sont tuées pour la raison attendue (banc rejoué) | trois survivantes parmi mes vingt nouvelles (section 5) |
| **CLV65-05** garde 7 reprise à moitié | **oui** | cœur 561-565, 585-589 (`exiger_sans_temoin`), 150-152, 472-476 | trois essais d'artefact ; mes mutations K06 à K10 tuées | — |
| **CLV65-06** banc à 37 sur 38 avec `bwrap` | **oui, à la lecture** | lanceur 87 (`WHICH`), 301, 310 ; l'essai `…sans_repli_partout` remplace `WHICH` et ne saute jamais ; le banc refuse une sélection toute sautée | joué ici sans `bwrap` seulement | à confirmer sur la machine (section 6) |
| **CLV65-07** registre réel refusé | **oui** | registre 44-83 (règle de la garde), 109-150 | section 4 | section 4 |
| **CLV65-08** mesures promises et absentes | **oui** | cœur 93-130 (membre dominant, empreinte d'engagement), 186-270 (recherche chez l'expérimentateur et le vérificateur), 273-331 (jetons), 334-342 (lignes de tranche) ; lecture 291-338 (Wilson) | essais de la classe `Mesures` ; à blanc : 0 touche hors de la loi gelée | jetons jamais vus sur une sortie réelle ; l'enveloppe `EtageMesure` n'a jamais tourné avec le moteur réel (section 6) |
| **CLV65-09** garde 22 | **oui** | lanceur 271-294, ordre 411-441 (texte, monde, configuration, GO, garde 17, garde 22, sonde, garde 15, rôles en dernier) | `test_garde_22_…` ; mes mutations K13 à K16, K18, K20 tuées | l'identité comparée après la sonde est celle **réglée** sur l'exécuteur ; la mesure sur l'hôte est celle de la sonde (`controler_hote_apres_sonde`, code ancien) : à voir sur la machine |
| **CLV65-10** chemins de la configuration | **oui** | lanceur 205-253 | étape 14 ; essais `ConfigurationV6` | le relais Argon (`servir`) cherche par défaut `collisionneur_v7.py` trois dossiers au-dessus de la commande : dans le dossier de course ce défaut ne mène nulle part, `--collisionneur` explicite exigé (hors du lanceur, à écrire dans les commandes de la machine) |

## 3. Mandat 2 — l'écart déclaré par le développeur (génération 2, membres d'archive lus C4 et non C5)

**Conforme au texte. Je recommande de le garder.**

- La prédiction P6 du brouillon (section 4.1) dit en toutes lettres : « nombre de membres d'archive des cartes de la génération 2 = celui qu'impose {K1} ∪ retenues ». La ligne C4 de la section 8 nomme « archive de la génération 2 ≠ {K1} ∪ retenues ». Un nombre de membres en écart en génération 2 est donc une P6 manquée : C4. Le relevé n'est pas « incomplet » : la mesure y est, et elle montre l'écart.
- Ce que rend la lecture, vérifié par sonde sur le relevé à blanc versé, altéré en mémoire : fausse F1 de la génération 2 avec un membre de trop → **C4** ; avec zéro membre → **C4** ; membres absents (non jugée) → **C5** et « C4 (partielle) » ; promue et membres en écart → **C4** (l'audit A2 se déclenche aussi, diagnostic « défaut de chaîne ») ; copie ou carte réelle en écart → **C4** ; F1 de la génération 1 en écart → **C5** (garde 18). Aucun de ces cas ne rend C1 ni C2 à tort.
- À écrire au texte (section 8, ligne C5) : « en génération 2, une loi jugée avec un autre nombre de membres que celui qu'impose {K1} ∪ retenues relève de P6 (C4), non du relevé incomplet ».
- **Limite, qui est le constat CLV66-01** : dans le cœur, la garde 18 arrête la course **avant** que cet écart entre au relevé ; la branche C4 de la lecture pour les lois plantées n'est donc atteinte que sur un relevé altéré, et l'arrêt réel est lu C5 seul.

## 4. Mandat 3 — lecteur du registre des GO

**Équivalent à `garde_calcul.lire_go`, sur le vrai registre et sur 32 artefacts à moi (33 comparaisons sur 33).** La boucle de lecture est la même ligne pour ligne (lu côte à côte) ; même motif de ligne.

- Sonde : la garde chargée depuis `.claude/hooks/garde_calcul.py` (sa fonction `bloquer` remplacée par une exception), comparée à `lire_registre_go_v66` : admis ou refusé, puis identifiants, dates, type, accordant, périmètre, référence et extensions.
- **Vrai registre** (`2c396b01…`, lecture seule) : admis des deux côtés, 255 identifiants, 34 lignes d'extension, champs égaux.
- **Artefacts** : extension admise, majuscule, même jour, échéance plus proche, deux extensions ; refus : doublon simple, extension antérieure, d'échéance plus lointaine, d'un autre accordant, d'un autre type, précédée de gras, extension puis doublon ; GO de calcul sans échéance ; GO sans échéance et extension datée ; 7 colonnes ; barre dans une cellule ; date illisible ; ligne indentée et identifiant en gras (ignorées des deux côtés) ; tabulations ; fins de ligne Windows ; marque d'ordre d'octets en tête ; octets hors UTF-8 (`UnicodeDecodeError` des deux côtés ; dans le lanceur : code 2) ; fichier absent ; dossier ; lien symbolique.
- **Les deux GO de la course**, au 10 novembre 2026 : GO-2026-11-08-02 → **45 USD** (montant seul) ; GO-2026-11-10-10 → **45 USD** (part « organisme » d'une enveloppe de 120, parts organisme 45 et Bailey 75). **Refusés pour les deux** : 40, 44,99, 45,01, 50, 75, 120. Part « Bailey » demandée à 45 : refus. Validité : refus la veille de l'accord et le 1er décembre, lu le 30 novembre.
- Montants sur artefacts (une trentaine de cellules) : refus d'une somme des parts autre que le total, d'un nombre étranger (« report de 10 possible », « plafond porté à 60 », « v2 »), d'une part nommée deux fois, d'un montant approché, « par lancement », d'une autre monnaie, d'un second montant, d'un GO révoqué, d'un GO qui porte une extension, d'un autre accordant, d'un autre type, d'un montant requis non numérique, nul ou négatif. Lus, et c'est voulu : « 45 USD (organisme 45) » comme montant seul ; « organisme 045 » ; « Organisme » en majuscule.
- **Ce que le lecteur ne lit pas** : les conditions écrites dans le périmètre d'un GO (CLV66-07).
- **Conséquence pratique de la règle 1** (GO à extension refusé) : si l'un des deux GO est corrigé par une ligne d'extension, le lanceur le refusera. Une correction doit être une ligne neuve à identifiant neuf, citée par le texte.

## 5. Mandat 4 — mes vingt mutations sur les gardes neuves (23, 7, 22)

Une copie de `orchestrator/` par mutation, dans mon bac à sable ; un remplacement exact présent une seule fois ; essais : classes entières `VueServie`, `Garde7EtCopies`, `JugementsAuReleve`, `EssaiABlanc`, `Mesures` et tout le fichier de lecture (cœur et lecture), ou `Machine`, `BrancheReelle`, `EssaiABlanc` (lanceur). Copie saine : tout passe. **17 tuées, 3 survivent.**

| mutation | garde | ce qui est retiré | sort |
|---|---|---|---|
| K01 | 23 | une entrée de la vue servie qui n'est pas un objet n'est plus refusée | **survit** — sans effet pratique : la boucle suivante lève alors une autre erreur, arrêt quand même, mais sans incident 23 consigné |
| K02 | 23 | les identifiants attendus tirés de l'héritage lu, et non du fichier écrit par la génération 1 | tuée (`heritage_d_un_autre_contenu`) |
| K03 | 23 | une trace d'appel périmée est admise (« un appel de plus » non exigé) | tuée |
| K04, K05 | 23 | incident non consigné, avant puis après l'appel | tuées |
| K11 | 23 | texte attendu bâti sur une vue réduite à sa première loi | tuée (la course saine s'arrête) |
| K12 | 23 | loi servie comparée à elle-même, non à l'archive | tuée |
| K06 | 7 | lois plantées de la génération en cours oubliées (sélection et vue) | tuée |
| K07 | 7 | identifiants des lois plantées de la génération 1 vidés avant la génération 2 | tuée |
| K08 | 7 | identifiants servis oubliés (réels seuls) | tuée |
| K09 | 7 | incident de sélection non consigné | tuée |
| K10 | 7 | la lecture ne lit plus les incidents de la garde 7 | tuée |
| K13 | 22 | `bwrap` illisible admis | tuée |
| K14 | 22 | utilisateur 0 admis | tuée |
| K15 | 22 | sonde non exigée dans la description | tuée |
| K16 | 22 | « demande = reel » non exigée | tuée |
| K17 | 22 | description **sans** champ « factice » admise (`is not False` devient « vrai ») | **survit** — l'essai n'a que « factice = vrai » ; un cas « champ absent » manque |
| K18 | 15 | garde 15 jouée après la construction des rôles (portes posées avant) | tuée |
| K19 | 22 | à blanc, bac réel, superutilisateur : identité du bac non exigée | **survit** — aucun essai ne joue cette branche (un essai à doublures est possible sans `bwrap`) ; c'est la branche de l'essai à blanc `--bac reel` de la machine |
| K20 | 22 | `bwrap` 0.8 admis | tuée |

## 6. Mandat 5 — ce qui n'est pas éprouvable sans `bwrap`, et ce qu'il faut jouer sur la machine de la course

`bwrap` est absent de cette machine. **Non éprouvé ici :**

1. Garde 3, cas sain, et garde 22 en situation : `bwrap --version` réel, lanceur en superutilisateur, sonde réussie, propriétaire du fichier témoin sur l'hôte égal à 64097, dossier racine en 0700.
2. Les quatre essais sautés (`test_boucle_reelle_v66.py` l. 740, `test_boucle_reelle_v65.py` l. 553, `test_tour_ferme_v64.py` l. 1485, `test_v59_boucle_fermee.py` l. 332) et l'essai à blanc `--bac reel --utilisateur-bac 64097`, qui est aussi le seul passage par la branche de K19.
3. La branche réelle du lanceur au-delà de la garde 22 avec les vraies pièces : garde 15 réelle, construction des adaptateurs et des commandes, portes de plafond des relais, `--verifier-seulement` sans doublure.
4. Le banc sur une machine qui a `bwrap` (CLV65-06 : 133 sur 133 attendu) et la suite sous le numpy de la machine.
5. **Deux choses qui n'existent que dans la course payée** : l'enveloppe `EtageMesure` avec le moteur réel de l'étage (à blanc, le moteur est simulé ; à la lecture, l'étage v5 n'emploie que `lancer` et `modeles_servis_permis`, que l'enveloppe délègue) ; le relevé des jetons sur la dernière ligne JSON des vraies commandes (les deux commandes v6 écrivent bien un champ `usage`, lu dans leur code).

**À jouer sur la machine, dans cet ordre, avant le lancement :**

1. La suite des neuf fichiers **sans** `POLE_ESSAI_BAC_REEL_NON_JOUE` (zéro essai sauté attendu ; les essais du vrai registre seront déclarés non joués si le dépôt de travail n'y est pas).
2. Le banc : `python3 -I -B essais/mutations_boucle_reelle_v66.py --processus 4` → 133 sur 133, code 0.
3. L'essai à blanc `--bac reel --utilisateur-bac 64097`, lanceur en superutilisateur : code 0, tous les étages « factice : faux », puis sa lecture.
4. La commande réelle avec `--verifier-seulement` : « vérification : conforme », aucun appel, aucune porte posée ; y lire la description du bac (identité 64097) et les chemins résolus des commandes.
5. Copier `registres/go.md` de `main` sur la machine et noter son empreinte au rapport de course : le lanceur lit ce fichier-là.
6. Lancer le relais Argon avec `--collisionneur` explicite.

## 7. Constats

Gravité : **B** bloque ; **C** à corriger ou à écrire au texte ; **m** mineur ; **i** information. **Aucun constat B.**

### CLV66-01 (C, lettre de la section 8) — un arrêt de la garde 18 en génération 2 n'est pas lu « C4 (partielle) »

La garde 18 lève **dans** le juge (cœur 117-119), avant l'écriture des jugements (cœur 421) et sans incident consigné ; la lecture ne lit que les incidents des gardes 7, 21 et 23 (lecture 134). Sonde (juge d'essai qui, en génération 2, juge les lois plantées avec la seule archive {K1}, le défaut de la v64) : arrêt « PlanteeSansArchive : loi plantée F1 jugée avec 4 membre(s) d'archive ; l'archive de sa génération en impose 40 », aucun incident, aucun jugement de la génération 2 au relevé, lecture **C5, rien de partiel**. Or c'est l'écart de P6 que le développeur lit C4 (section 3), et la section 8 veut qu'un arrêt ne masque pas un écart de lecture de la sélection. La cause est tout de même écrite dans `cause_c5`.

Portée : **non atteignable par le cœur gelé**. Le nombre attendu et le nombre mesuré sortent de la même fonction (`nul_v8.membres_archive_v8`) sur la même archive ; seul le paramètre d'essai `archive_des_plantees` les sépare, et le lanceur ne le passe jamais.

**Ce qu'il faut**, au choix : (a) au texte, section 8, ligne C5 : « un arrêt de la garde 18 en génération 2 se lit C5, cause écrite ; il vaut écart de P6 et le rapport le dit » ; (b) au code (v67) : consigner l'incident (garde 18, génération) autour de l'appel du juge, le faire lire comme écart de P6 quand la génération est 2, un essai sain, un artefact (ma sonde), une mutation.

### CLV66-02 (C, lecture) — P6 tenue à vide si deux champs manquent au relevé

Sur le relevé à blanc versé, altéré en mémoire : `lecture_selection` absente → **C1** ; `archives_de_jugement["2"]` absente → **C1**. La comparaison « empreinte lue = écrite » est sautée quand la lecture de sélection manque (lecture 147-153) et la comparaison de l'archive quand elle manque (lecture 170-172) ; `completude` n'exige ni l'une ni l'autre. Même famille que CLV65-01, côté P6.

Portée : **non atteignable par le cœur gelé** (`lecture_selection` est écrite avant toute génération 2, cœur 550 ou 560 ; l'archive de jugement à chaque génération, cœur 422 ; « complet » n'est posé qu'à la fin).

**Ce qu'il faut**, au choix : (a) au texte, section 8, ligne C1 : « C1 ne se prononce que si le relevé porte la lecture de la sélection (sans refus, empreinte lue égale à l'empreinte écrite) et l'archive de jugement de la génération 2 ; sinon C5 », vérifié par le lecteur du verdict ; (b) au code (v67) : deux conditions de plus dans `completude`, essais et mutations.

### CLV66-03 (m) — autres champs que la lecture ne recompare pas

Sans effet sur une issue d'un relevé du cœur gelé ; à joindre à une v67 s'il y en a une. La lecture rend C1 quand : aucun appel n'est consigné dans la vue servie de la génération 2, ou un texte reçu diffère du texte bâti (la garde 23 du cœur arrête, la lecture ne revérifie pas) ; l'empreinte relue de la sélection finale diffère du bilan ; `lu_sur_disque` diffère de `lu` ; les retenues de la génération 2 manquent. Une loi promue sans verdict dans un relevé dit complet se lit C3 (vraies) ou C6 (T-ELIM) et non C5 : prudent, jamais C1.

### CLV66-04 (C, texte ; décision de fond) — C1 sans aucune carte réelle retenue

Sonde (les deux proposeurs sans proposition lisible en génération 1, ce qui est un refus mesuré et non un arrêt) : course complète, aucune retenue, aucune copie, vue de la génération 2 égale à {K1}, lecture **C1**, `p5_copies_refusees` nul. C'est conforme au texte (section 3.7 : copies « si au moins une carte réelle a été retenue » ; C1 = P1, P4, P6), mais la génération 2 lit alors une sélection vide : la fermeture de la boucle n'est pas éprouvée, et la phrase de résultat ne le dit pas. **À trancher au texte** par la mère, et par Lazar si c'est un changement de critère : soit le dire dans la ligne C1 et dans l'audit A1 (« sans retenue, P5 et P6 ne prouvent rien de la lecture de la sélection »), soit en faire une issue à part.

### CLV66-05 (m) — trois gardes ou branches sans essai sur artefact

K01, K17, K19 (section 5). K19 est la seule de portée réelle ; un essai à doublures suffit.

### CLV66-06 (m) — rapport du développeur, table de la section 3

Les empreintes de `essais/test_boucle_reelle_v66.py` et de `essais/test_registre_go_v66.py` sont celles du commit `3ba4727`, pas de la tête `7e415cb` (le jalon 3 les a retouchés). Fichiers non gelés ; le bloc du texte n'est pas touché (`9933ee11…` rejoué à l'octet). À ne pas recopier dans un registre.

### CLV66-07 (C, hors code ; à régler avant le lancement, pas avant le scellement du code) — conditions écrites des deux GO

- GO-2026-11-08-02 : « après le code **v65** contre-lu ».
- GO-2026-11-10-10 : « code **v65** contre-lu » et « configuration **v5** (`995eb918…`) ».

La course jouera le code v66 et la configuration v6 (`4743ddbe…`). L'empreinte `995eb918…` n'est celle d'aucune configuration de l'organisme (v5 = `bff138d8…`, vérifié). Le lecteur ne lit que le montant. **Nœud** : la mère fait dire à Lazar que le GO vaut pour le code v66 contre-lu et la configuration v6, par une ligne neuve à identifiant neuf (une ligne d'extension ferait refuser le GO par le lanceur, section 4).

### CLV66-08 (i) — divers

- Message d'arrêt à préfixe doublé (« ArretTour : ArretTour : … »), étape 6 de l'essai à blanc.
- `test_vrai_registre_lu` porte un chemin absolu et une date : non joué hors de cette machine, et il change de branche après le 30 novembre.
- En mode réel, le manifeste écrit les **noms** des variables d'environnement du processus (jamais leurs valeurs) : comme en v64 et v65.
- Non traité par le développeur, dit par lui : une fausse ou une copie promue en génération 2 est encore envoyée au test de mort (vu dans ma sonde : F3 promue artificiellement, « survit » avec l'exécuteur factice) ; cas de brèche seulement.

## 8. Points ouverts pour la mère

1. Choisir pour CLV66-01 et CLV66-02 : clauses au texte (je recommande) ou v67.
2. Trancher CLV66-04 au texte.
3. Régler CLV66-07 avant tout lancement.
4. Texte : reprendre aussi la liste du développeur (son rapport, section 9, point 2) et la phrase de la section 3 de ce rapport.
5. Jouer sur la machine les six points de la section 6.
