# SPARKS-EXP7-NUL — contre-lecture du delta v5 → v8 (code `53d4eda6..4fd10407`, répétitions jouées v5 à v8) et du brouillon 6

Contre-lecteur neuf (R2, sous-agent Claude, Opus 5.5). Je n'ai écrit ni le texte, ni le code, ni aucune contre-lecture
précédente. Consigne : `consigne-contre-lecture-delta-sparks-v8-v1.md`, compagnon « OK » avant lecture. Travail du
5 novembre 2026, de 04:06 à 04:25 UTC (`date -u`). Lecture seule du dépôt et de l'arbre
`/home/claude/wt/sparks-exp7-nul-v8` (`git status` vide avant et après). Aucun commit, aucun `.sha256`, aucun réseau, aucun
modèle, aucune dépense, aucune clé lue. Moins de 5 Mo au bloc-notes. Une commande a été refusée par la garde de la session :
le lanceur v8 en mode « tir » joué hors réseau avec un registre de GO factice. Je ne l'ai pas contournée. Ce mode est lu
dans son code, dans l'essai qui le joue et dans l'exemple de sortie du rapport v5.

## Verdict

**À reprendre : le protocole du tir réel (cinq compléments, point 31) et un code v9 minimal (lanceur, deux lignes de l'amorce, `tir.py`). Le texte sera scellable après le tir, les 15 couples ci-joints et la contre-lecture neuve du delta v9.**
Les neuf changements de la contre-lecture v4 et les corrections v6, v7 et v8 sont faits. La répétition v8 les éprouve pour la bonne raison. Le brouillon 6 est exactement le brouillon 5 plus deux couples, ses quatre entrées portent les bonnes empreintes, et `prereg.problemes` rend `[]` une fois les trois marqueurs remplis.
Point à trancher par le tir, au premier rang : quatre faits du registre montrent des conteneurs lancés par leurs arguments qui **redémarrent en boucle** à la sortie de l'amorce. Le dessin suppose au contraire « le conteneur sort, l'instance est arrêtée ». Si le tir confirme la boucle, la borne de la machine ne tient plus et aucune création n'est permise sous ce texte.

## Empreintes vérifiées (compagnons, depuis le dossier de chaque fichier)

Toutes « OK », et égales aux préfixes de la consigne :
- brouillon 6 `9f82ad08…` et brouillon 5 `851f75e4…` ;
- couples du brouillon 6 `4312524d…` ;
- contre-lecture du delta v4 `4bc7066e…` et les 8 compagnons de son dossier ;
- rapports v5 `da4b4b64…`, v6 `2814152f…`, v7 `1c69f72b…`, v8 `3752a2d5…` ;
- sorties `essais-et-banc-sparks-v5` à `-v8` ;
- répétitions `repetition-jouet-v5-v1` à `-v8-v1`.

Code : `git diff --name-status --no-renames 53d4eda6 4fd10407` donne 74 « A » et aucun autre statut. Les 37 fichiers sont égaux à leur compagnon, lu au commit. Le script de la répétition v8 est égal à l'octet à celui de la section 5 du rapport v8.

## Points (gravité ; une ligne chacun)

### Q1. Les neuf changements de la contre-lecture v4, et les corrections v6, v7, v8
1. **Conforme — les neuf changements**, lus au code v8 :
   - (1) `VAST_API_KEY` par son nom : lanceur, l. 37-43 ;
   - (2) identifiant et « success » vrai testés avant le certificat (l. 52-62), `start` et `destroy` lus puis inventaire (l. 63-78) ;
   - (3) durée réelle : amorce l. 119-123, `redemarrage.py` l. 165-191 ;
   - (4) addendum reconnu et marqueur des gardes : amorce l. 124-131, 149-150 et 174 ;
   - (5) amorce prise par `git show` : lanceur l. 107 et 149 ;
   - (6) corps du `DELETE` et borne de 190 s : amorce l. 70-77 ;
   - (7) mode « tir » : lanceur l. 88-128, `tir.py` ;
   - (8) répétition jouée ;
   - (9) mutations : 30 sur 30 au banc.
2. **Conforme — v6.**
   - Correction : `_commit_du_code` (essai v8, l. 608-616) prend `COMMIT_CODE`, sinon le dernier commit qui écrit la liste fermée ; la date passe par `SPARKS_DATE_TIR`.
   - Épreuve : la répétition v8 extrait un commit enfant (`d7a89671`) différent du code. On y lit « essais : 293 passed » deux fois, et c'est bien l'essai du tir qui tombait en v5 (R-1514).
3. **Conforme — v7.**
   - Correction : fonction `module` (script d'instance v8, l. 68-71).
   - Épreuve, pour la bonne raison : aucun « No module named », « EGALITE LOTS OK », et un manifeste créé par `module`.
4. **Conforme — v8.**
   - Correction : `manifeste_phase` (l. 28-64) ; aucun repli, et la marque factice est refusée hors du mode jouet.
   - Épreuve : « MANIFESTE CRÉÉ … addendum (8fd57d1b…) ; texte parent 4bacf20d… ; ADDENDUM FACTICE (jouet) », en fabrication comme en phase causale.
   - La voie réelle (addendum non factice, `MODE=reel`) n'est éprouvée que par les essais v8, sur des dépôts neufs. C'est déclaré.
5. **Faible — un attendu tenu pour une autre raison que la sienne.** L'étape 3 attend « sans poussée vérifiée ». L'amorce l'écrit (l. 193) alors que le journal dit « poussée vérifiée » : la vraie cause est le code 1 du calcul. Mieux : attendre « fin de la phase causale, code [1-9] » et « poussée vérifiée », et corriger le message de l'amorce.
6. **Faible — des chemins jamais joués de bout en bout.**
   - La cause du code 1 causal n'est pas versée : ni `run.err`, ni la branche `…-causal-…-002`. Le code la rend probable : `charger_depart("jouet")`, `instance.py` l. 100-101.
   - `causal_instance` par lots et la voie réussie de la copie (lot construit, conteneur en vie) ne sont joués par aucune répétition.
   - Risque à déclarer au rapport du run.
7. **Mineur — deux noms restés de la v4 dans le texte**, couples N-7 et N-8 :
   - `sparks-v<N>-detruire` « même numéro que l'amorce » : l'amorce v8 pose `sparks-v5-detruire` ;
   - la branche `ordres/sparks-exp7-nul-v4-…` : l'amorce v8 lit `…-v5-…`.

### Q2. Le mode « tir » du lanceur v8, au vu des faits réels
8. **Majeur — la boucle de redémarrage contredit l'attendu « exited ».**
   - Les faits : R-458 ; `registres/arrets.md` (`07bc8f75…`), instances 58714588, 58714023, 58714191 et 58714336, les 1er et 2 novembre, « conteneur en boucle de redémarrage » ; R-1524 (b).
   - Le lancement en cause : R1 v4 était lancé par ses arguments (`--entrypoint bash --args -c`, `docs/procedures/ordre-fille-r1-v4-lancement-v1.md`, l. 34, `94940fa5…`), comme SPARKS (`--args bash -c`).
   - Le tir est sûr même en boucle : il se détruit au premier démarrage après l'échéance (amorce, l. 98) ou à l'ordre « fin ».
   - En revanche, une seule lecture « exited » ne distingue pas un arrêt d'une boucle. Le protocole doit compter les démarrages (point 31).
9. **Majeur (si la boucle est confirmée) — la borne de la machine ne compte pas les démarrages d'une boucle.**
   - Les voies de refus (« ordre refusé », « ordres illisibles ») sortent avant `consigner_demarrage`. La carte est pourtant facturée jusqu'à l'échéance, qui va jusqu'au 19 novembre à 00:00.
   - Le plafond de 40 USD ne serait plus tenu par la machine.
   - Conséquence : aucune création, nœud de Lazar et code neuf. Une piste : arrêter l'instance par l'interface de Vast à chaque fin de démarrage, à éprouver.
10. **Moyen — l'inventaire « absente » est mal lu.**
    - Dans la source de `vastai` 1.8.3, `show__instance` en `--raw` rend `{"instances": null}` pour une instance introuvable. Le lanceur (l. 74) lit alors « illisible ».
    - Le motif `404` n'est pas ancré. Si `actual_status` n'est pas une chaîne (instance en création), un identifiant ou un nombre qui contient « 404 » donne un faux « absente », dans le sens dangereux.
    - Correction v9 : `"status_code": 404` et `"instances": null` ancrés, ou une liste `show instances --raw` lue en JSON strict et filtrée par identifiant (la méthode de la sonde v10).
11. **Moyen — l'offre n'est pas contrôlée.**
    - Ni commande de recherche, ni contrôle `resource_type` = « gpu » : une offre « disk » donne `no_such_ask` (R-1510, R-1511).
    - Rien n'écrit comment tirer `PRIX_CARTE` (`dph_total`) et `PRIX_STOCKAGE` (prix du stockage par Go et par mois × 20 Go ÷ 730) de l'offre retenue.
12. **Moyen — le jeton passé à l'instance n'est pas tranché.**
    - Le tir passe `-e GH_TOKEN=$GH_TOKEN` de la session qui tire. L'ordre de R1 v4 passait `GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN` (l. 33), et N-009 nomme ce jeton à grain fin pour les instances.
    - Un jeton qui ne vaut qu'à travers le mandataire de la session ferait échouer le clone. Le tir le dirait (« clonage impossible » au lieu de « code ou addendum non conformes »), mais le choix doit être écrit avant.
13. **Moyen — le tir est annoncé après le scellement.** Le rapport v8 (fin de la section 5) dit qu'il « faut d'abord sceller le brouillon 6 ». C'est contraire au dessin :
    - contre-lecture v4, points 4 et 23 ;
    - M-3 et texte, « Restent, avant le scellement : le tir réel » ;
    - le tir n'a pas besoin de l'addendum, puisqu'il s'arrête à la garde du code (vérifié : `verifier_lancement`, garde v2 l. 86-90).
14. **Faible — un « no_such_ask » bloque la reprise.** Il donne « CRÉATION INCERTAINE », marqueur posé, ce qui bloque un second essai jusqu'à un inventaire. C'est prudent ; mieux, reconnaître `no_such_ask` comme un refus net après un inventaire.
15. **Faible — un `start` refusé peut passer pour « envoyé ».** En cas d'échec avec HTTP 200, `vastai start` n'imprime que le message (`start_instance_impl`), que les motifs de refus ne couvrent pas : le lanceur dit « ENVOYÉ ». C'est prudent, puisque l'inventaire suit. Mieux : exiger « starting instance <ID> ».
16. **Faible — des secrets restent sur le disque.**
    - La sortie brute de `show instance --raw` porte `extra_env`, donc `GH_TOKEN` en clair. La sonde v10 la masquait.
    - Le lanceur la garde dans `inventaire-<ID>.txt` et `tir-inv-2.txt`, non affichés mais gardés.
    - À effacer après le filtre, et à ne jamais verser.
17. **Faible — n'importe quelle ligne de GO valide passe.** `tir.py` accepte toute ligne « calcul », Lazar, ≤ 5 USD et valide, par exemple GO-2026-11-05-01 de la sonde d'A1-v3. Il faut exiger « SPARKS-EXP7-NUL » et « tir » au périmètre.
18. **Faible — `grep '^AMORCE V5'` sur `vastai logs` peut tout manquer** si les lignes portent un préfixe. Retirer l'ancre.
19. **Faible — l'ordre « fin » dépend de la borne** (amorce, l. 169). Un registre des démarrages illisible le refuse, et la destruction ne vient alors qu'à l'échéance. Mieux : traiter « fin » avant la borne.
20. **Conforme.**
    - Les deux flux sont lus : `> F 2>&1`.
    - Les variables du mandataire et `VAST_API_KEY` passent par leur nom.
    - `-y` est présent à la destruction et au repli de la minuterie ; `create` et `start` n'en demandent pas (source 1.8.3).
    - L'échéance du tir est de 20 à 30 minutes.
    - Le devis vaut 0,74 USD à 0,80/0,05, sous un plafond ≤ 5 USD.
21. **Nœud — clé d'instance (R-1527 ; compte).**
    - Absente du texte : couple N-11.
    - Elle tombe sous l'exclusion « compte ou secret » de GO-2026-11-04-10. Il faut la réponse de Lazar avant toute création.
    - Le tir n'exécute aucun code tiers.
22. **Nœud — conditions du tir.**
    - La ligne de GO du tir reste à poser (R-1508). L'autonomie GO-2026-11-04-10 finit vers 07:30 UTC aujourd'hui ; ensuite, il faut un mot de Lazar.
    - `vastai` est absent du chemin de ce conteneur (`which vastai` vide) : l'installer en version 1.8.3 dans la session qui tire.

### Q3. Brouillon 6
23. **Conforme — le brouillon 6 est bien le brouillon 5 plus deux couples.** Rejoué à l'octet (`9f82ad08…`) : chaque « ancien » est unique au moment de son application, et trois « À REMPLIR » restent.
24. **Conforme — les quatre entrées « Contre-lecture k ».** Les 8 empreintes sont égales aux fichiers sur le disque, et chaque rapport cite son brouillon par son empreinte abrégée.
25. **Conforme — `prereg.problemes` (code v8) :**
    - copie avec les trois marqueurs remplis pour simulation : `[]` ;
    - brouillon 6 tel quel : seul le marqueur reste ;
    - brouillon 5 : trois problèmes.
26. **Mineur — la section « Hypothèse » par renvoi.**
    - Fond : inchangé, c'est l'hypothèse du texte v1, l. 17-27, et les graines restent tirées du texte v1.
    - Forme : « cet addendum ne change aucun énoncé », lu au sens large, est faux (A-2, A-14, A-15). Couple N-5.
27. **Mineur — des parties restées au brouillon 5.**
    - Titre, en-tête, journal et pied disent encore « brouillon 5 » : couples N-1 à N-4, N-14, N-15.
    - La section 2 ne nomme pas les codes v6 à v8 et dit que la garde lit la liste v5, ce qui est faux en v8 : couple N-6.
28. **Mineur — le tir est décrit comme éprouvant `vastai copy`**, ce qu'il ne fait pas (« Épreuves ») : couple N-10.
29. **Faible — la marque factice ne doit jamais être citée en entier dans le texte scellé.** `manifeste_phase` refuse en mode réel tout addendum qui la contient. Elle est absente du brouillon 6 et des couples.

### Q4. Ce qui reste pour sceller (liste fermée)
30. Dans l'ordre :
    1. ligne de GO du tir : « calcul », ≤ 5 USD, périmètre « SPARKS-EXP7-NUL tir » ;
    2. **tir réel** sur v8, avec les compléments du point 31 ; rapport scellé du tir ; issue exigée : « arrêtée, sans relance automatique, carte non facturée », sinon nœud (points 8 et 9) ;
    3. **code v9** :
       - points 10, 11, 12 (jeton écrit), 15, 16, 17, 18, 19 et 5 ;
       - plus ce que le tir impose ;
       - avec essais, banc, répétition jouée et contre-lecture neuve du delta v9 (entrée « Contre-lecture 6 ») ;
    4. couples N-1 à N-15 appliqués (brouillon 7), plus un couple « compléments v9 » ;
    5. trois marqueurs remplis par script :
       - commit v9 ;
       - liste fermée v9, égale au fichier ;
       - comptes de tous les runs ;
    6. `problemes` = `[]` sur le texte final, puis scellement.

    Avant toute **création** (et non avant le scellement), il faut aussi la réponse de Lazar au nœud R-1527.

### Compléments du tir sur v8 (lecture seule ; recommandation, confiance moyenne : le tir n'attend pas v9)
31. Compléments :
    - (a) **Offre** :
      - `vastai search offers 'num_gpus=1 rentable=true verified=true' -o dph_total --raw`, sortie dans un fichier ;
      - garder `resource_type` = « gpu » ;
      - n'imprimer que `id`, `dph_total`, `storage_cost` et `resource_type` ;
      - prix calculés comme au point 11.
    - (b) **Jeton** écrit dans la commande, au choix de la mère (point 12).
    - (c) **Inventaire** par `vastai show instances --raw`, lu en JSON strict : une liste, sinon « illisible ». N'imprimer que `id`, `actual_status` et `cur_state` de l'instance ; effacer le fichier brut.
    - (d) **Boucle** :
      - trois inventaires sur au moins 5 minutes après l'étape 1 ;
      - nombre de lignes « AMORCE V5 … : redémarrage » dans `vastai logs <ID> --tail 400`, `grep` sans ancre ;
      - `dph_total` relevé.
    - (e) Effacer les sorties brutes de `vastai` après filtrage, et ne rien verser d'elles.

## Fichiers (ce dossier, neufs, sans compagnon)
- `contre-lecture-delta-v8-v1.md` : ce rapport.
- `couples-brouillon7-v1.json` : 15 couples, N-1 à N-15, à appliquer dans l'ordre au brouillon 6.
  - Chaque « ancien » est unique au moment de son application, et les trois « À REMPLIR » sont gardés.
  - Contrôles faits : `problemes` = `[]` sur le texte d'essai rempli, et la marque factice en est absente.
  - N-12 ajoute l'entrée « Contre-lecture 5 », avec l'empreinte entière de ce rapport.
  - L'empreinte du fichier de couples et celle du texte d'essai sont données dans la réponse à la mère, puisque le fichier cite ce rapport.
