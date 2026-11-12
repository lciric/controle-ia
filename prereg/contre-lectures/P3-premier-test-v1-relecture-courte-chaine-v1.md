**Relecture courte du traitement, angle chaîne (relecteur Ch)**

**Empreintes vérifiées**
- Candidat 1 : `8070b64085ae649c68b79222fdfbb1aea1fc7e99edc5510822ea387b82805dd0`. Égale à l'empreinte attendue.
- Brouillon 4 : `94e5ff12…`. Égale à l'empreinte citée par le traitement et par le candidat. Il n'a pas de sceau compagnon, alors que les brouillons 1 à 3 en ont un.
- Configuration candidat 3 : `702303e9…`. Consignes candidat 2 : `a68468fe…`. Les deux sceaux sont conformes.
- Contre-lectures : chaîne `57060da8…`, texte et code `98d7201b…`. Les deux sceaux sont conformes.
- Chaîne brouillon 2 : les 14 sceaux passent `sha256sum -c`.
  - Traitement : `ad1d88d2…`.
  - Scripts : module `b01831ad…`, contrôles `336726c3…`, lanceur `c0aae305…`, scellement `d984c841…`, surveillance `5a2fcc24…`, contrôle à cinq minutes `3af74295…`, récupération `66bab154…`, répétition jouet `2893fcd9…`, répétition finale `500c600b…`.
  - Bancs : lanceur `ac08a8ba…`, contrôles `fa518140…`, scellement `dc83f760…`, surveillance `bb7a3c35…`.
- Chaîne brouillon 1 : les 12 sceaux sont conformes.
- Commit `03cb538` = `03cb53804e0b98fe671b62ebf5ef2d819741e282`.
  - Amorce `0bfaeaa6…`, script de l'instance `2bfc6939…`, tests des gardes `cf4ab7b8…` : toutes égales aux empreintes citées.
  - Rien ne change dans src, tests ni scripts entre `03cb538` et la tête `00075fc`.
- Journaux non officiels : surveillance `a03cc82f…`, lanceur `a6ecf841…`, scellement passage 4 `1e528c94…`, contrôles passage 2 `2b6901f3…`, répétition passage 4 `f5bf0181…`.

**Constats**

| id | fichier et ligne | ce qui est écrit | ce qui est juste, et la preuve | gravité | correction |
|---|---|---|---|---|---|
| RCh-01 | `verifications_p3_v1.py` l. 88-92 ; `registres/decisions.md` l. 352 (R-215, commit `18c24ef`) | Toute ligne R-… qui contient « révoqu…/révocation/retir…/annul… [de] [la] [décision] R-192 » est lue comme une révocation de R-192. | La ligne R-215 décrit les formes de révocation (« formes de révocation de R-192 », « annule R-192 ») sans rien révoquer. Pourtant, `python3 -I verifications_p3_v1.py go <candidat 1> registres/go.md registres/decisions.md` rend « décision R-192 révoquée, retirée ou annulée par R-215 », code 1, à la tête comme à `18c24ef`. Le même appel est conforme aux registres de `03cb538` et de `c0ebd6f`. Conséquences : le scellement s'arrête (l. 147-148) ; le bloc 4 des contrôles rend un KO ; le lanceur s'arrête (l. 131-132) ; la répétition finale ne peut pas être conforme ; les bancs officiels des contrôles (cas A00) et du scellement (cas S00), qui lisent les registres réels, non plus. Les bancs non officiels ont tourné avant R-215, sur les registres de `8db38d0`. Toute ligne future qui citera ces formes, par exemple le traitement de cette relecture, rebloquera la chaîne. | bloquant | Remplacer la recherche en texte libre par une forme exacte : une ligne de type « révocation » du registre des GO qui nomme R-192, ou une colonne décision qui commence par un préfixe fixe. Écrire cette forme mot pour mot au texte. Ajouter deux cas aux bancs : une ligne qui décrit les formes sans révoquer (texte de R-215), saine ; la forme exacte, refusée. Faire un brouillon 3 de la chaîne et rejouer les bancs du lanceur, des contrôles et du scellement. Ne pas réécrire R-215. |
| RCh-02 | candidat l. 44-47 ; module l. 88-92 | « une ligne R-… qui “révoque”, “retire” ou “annule” R-192 ; l'une ou l'autre présente, la chaîne refuse de lancer » | Le module ne voit pas des révocations formulées autrement. Sur les registres de `03cb538` plus une ligne, il rend « conforme » pour : « Lazar révoque, pour P3, la décision R-192. », « Lazar annule pour P3 sa décision R-192. », « Retrait de R-192 pour P3. », « R-192 : révoquée par Lazar pour P3. », « La décision R-192 (P3) est révoquée. » Le texte promet donc plus que ce que la chaîne contrôle. | mineur | Même correction que RCh-01 : une forme exacte, citée mot pour mot au texte. |
| RCh-03 | module l. 96-111 ; lanceur l. 102-110, 136 ; candidat l. 42-44 | L'accord est une ligne du jour qui contient « accord de Lazar », « P3 » et « lancement ». | `accord R-208`, `accord R-215` et `accord R-217` avec la date 2026-10-19 rendent tous « conforme ». R-208 dit pourtant « aucun appel payant sans l'accord de Lazar », et R-215 est le traitement de la chaîne. La garde ne repère donc pas le cas qu'elle vise : un appel lancé avant l'accord, alors qu'une ligne du jour mentionne l'accord. | mineur | Exiger une forme exacte, par exemple une colonne décision qui commence par « Accord de Lazar pour le lancement de P3 ». L'écrire au texte. Ajouter un cas au banc : une ligne du jour qui mentionne l'accord sans l'être (R-208), refusée. |
| RCh-04 | candidat l. 316-321 ; lanceur l. 182-188, 206, 280 | « soit au plus ≈ 11,2 USD » ; crédit exigé = 6,5 h × prix + 1,2 USD | (a) Le prix du stockage n'est pas borné : `storage_total_cost` est seulement archivé (l. 206). Le registre montre 0,074 USD de l'heure pour 80 Go (`registres/depenses.md` l. 19), soit 5,3 USD pour 72 heures au lieu de 1,94. (b) Au prix plafond, le crédit exigé vaut 9,65 USD, sous la borne de l'étape de 11,18 USD : le disque des 72 heures n'est pas couvert. Au brouillon 1, 9,0 USD couvraient la borne de 8,30 USD : le traitement de CH-10 a introduit cette régression. | mineur | Borner `storage_total_cost` au filtre, citer la borne au texte et la relier au bloc 9 ; ou écrire le disque « au prix de l'offre retenue » et retirer « au plus ». Relever la constante du crédit d'environ 3,2 USD, ou écrire au texte que le crédit est rechargé avant la garde de 72 heures. |
| RCh-05 | candidat l. 403-406 ; contrôles l. 46 | Les copies versées diffèrent du brouillon 2 par les épingles des contrôles « et leur ligne H ». | La ligne H du brouillon 2 est déjà le vrai bloc-notes (`…/p3-v1`), comme dans le lanceur (l. 50), le scellement (l. 29) et les bancs. Seule la copie d'essai C2 la changeait (en `p3-v1-brouillon2`, vu par `diff` avec `essai-C2/depot`). La changer au versement ferait lire aux contrôles un module que le lanceur ne vérifie pas (l. 75-81). | mineur | Retirer « et leur ligne H » du texte. Si le bloc-notes change, déclarer les lignes B, H, BN et PY des treize scripts. |
| RCh-06 | candidat l. 455 et l. 109 ; `prereg.py` l. 37-60 | Champ restant : « `[après la relecture courte : …]` » ; ligne 109 : « **[nœud … (R-203)** ». | `problemes()` ne cherche que « À REMPLIR » et les marqueurs entre doubles chevrons ; sur le candidat 1, elle rend [] (rejoué). Ni le bloc 9 ni le scellement ne voient ce champ. La citation des rapports n'est exigée que s'ils sont versés sous `prereg/contre-lectures/P3-premier-test-v1-*` (contrôles l. 183-192, scellement l. 105-118). La ligne 109 garde un crochet ouvrant sans fermeture, laissé par `construire_candidat1.py`. | mineur | Remplir le champ avant le versement (chemins et empreintes des trois rapports, versés sous ce préfixe et épinglés). Écrire « À REMPLIR » pour tout champ futur. Retirer le crochet. |
| RCh-07 | candidat l. 159-162 ; récupération l. 302-335 ; `manifeste.py` l. 137 | Les textes d'action sont « cherchés … dans tous les autres fichiers ajoutés ». | (1) Les tableaux `.npz` sont exclus (l. 322), et les chaînes du fichier léger des sondes ne sont pas bornées. (2) La recherche porte sur les octets bruts, alors que les résultats `.json` échappent les retours à la ligne et les guillemets. Une action de 64 à 200 caractères sur plusieurs lignes, recopiée dans un résultat, échappe donc aux deux contrôles. (3) Une action dégénérée faite de points retrouverait la barre de progression de `tests.txt` : faux KO. | pour information | Écrire « hors tableaux npz » au texte. Comparer aussi les fenêtres aux chaînes `.json` décodées dans `parcourir()`. Ignorer les fenêtres à un seul caractère répété. |
| RCh-08 | candidat l. 392-394, 323-324 | Liste d'arrêt de la création ; instances « rr- » tolérées. | La liste d'arrêt omet la borne de téléchargement et le KO du contrôle à cinq minutes. Le texte omet que les instances « rr- » doivent être nommées en argument (lanceur l. 245). | pour information | Compléter le texte. |
| RCh-09 | `traitement-CH-v1.md` l. 37 et question 3 | La destruction de 55292763 et 55458787 est « rendue à Lazar (R-213) ». | Ce fait était déjà dépassé par R-214 (13:18 UTC), avant le scellement du traitement (13:56). R-215 (3) et le candidat (l. 322-323) sont justes. | pour information | Aucune, à noter seulement. |

**Constats d'origine (CH)**
- CH-01 : traité. Cas A19 à deux KO (`essais_controles` l. 138, `jouer()` l. 93). Le journal du banc des contrôles, passage 2, rend A19 « 2 KO ; CONFORME ».
- CH-02 : traité. Module l. 39 et 63-64 ; lanceur l. 131-135, 291 et 302. Les cas G05, A06b et S24b sont conformes aux journaux.
- CH-03 : traité. Scellement l. 32, 76-82 et 133-145 ; répétition finale l. 28 et 45-56 ; cas S41 à S41d et P30a à P30j. J'ai rejoué `preuves` sur les quatre journaux non officiels : code 0. Chaque script éprouvé est égal au brouillon 2, sauf la copie d'essai des contrôles, ce qui est déclaré.
- CH-04 : traité. Lanceur l. 185-186 ; bloc 9 l. 250-251 ; cas P07f, P07g, P07i, P07k, O12 et O13 conformes. Le seuil de 16 cœurs est justifié et écrit au candidat (l. 302, 311).
- CH-05 : traité. Contrôle 6e de la récupération (l. 354-363) ; l'artefact q-v1 donne bien « KO 6e » au journal.
- CH-06 : traité. Récupération l. 135-171 et 214-228 ; artefacts o-v1 (KO 4c) et i-v1 (KO 2b) au journal.
- CH-07 : traité. Le cas des gardes réelles rend code 0, gardes 0, 3f et 6b jouées. Les artefacts u, v, k, t, j, l, p et s ont chacun un seul KO. Les gardes restées sans artefact sont déclarées.
- CH-08 : traité. Contrôles l. 103-120 ; cas A55 et A55b conformes.
- CH-09 : traité en partie. Le texte écrit les formes (l. 44-47), mais voir RCh-01 (bloquant) et RCh-02.
- CH-10 : traité en partie. Le téléchargement est borné (l. 187 ; cas P07h, P07j, O14, O15 ; bloc 9), « inatteignable » est retiré et les montants sont écrits. Voir RCh-04.
- CH-11 : traité en partie. Cas A10 à A13 conformes, mais voir RCh-03.
- CH-12 : traité. Le bloc 10 n'a plus de tolérance. B00, avec le vrai tokeniseur, rend 49 OK ; B01 à B05 sont conformes. Le bloc 9, rejoué sur le candidat 1, rend code 0.
- CH-13 : traité. Préfixe « rr- » au lanceur (l. 47, 245) ; cas V01 à V08 conformes.
- CH-14 : traité. J'ai vérifié toutes les lignes citées, artefacts et gardes redondantes.
- CH-15 : traité. Cas M15, M16, A30d et S18b conformes ; le module accepte le journal de la répétition, passage 4 (code 0).
- CH-16 : traité. Surveillance et contrôle à cinq minutes, l. 32-35 ; cas M11, M11b et C14 conformes.
- CH-17 : traité, selon R-215 (3). La liste est gardée telle quelle (lanceur l. 56) et reste sans effet, puisque les quatre instances sont détruites (R-212, R-214).
- CH-18 : traité. Récupération l. 210 et 299-335 ; l'artefact n-v1 donne bien KO 4f. Le texte doit gagner en précision (RCh-07).
- CH-19 : traité. Bloc 9 l. 225, bloc 10 l. 332-333 ; cas A49b conforme.
- CH-20 : traité. Contrôles l. 121-122 et 345-370.
- CH-21 : traité. Candidat l. 312-315 ; surveillance l. 6-7.
- CH-22 : traité. Lanceur l. 270-288 ; cas P08c et P08d conformes.
- CH-23 : traité. Le treizième script existe ; le lanceur écrit la fenêtre (l. 299-301) ; cas C00 à C19 conformes. Les lignes attendues figurent bien au commit `03cb538` : `p3_instance.sh` l. 52, 112, 126 et 200, amorce l. 24.
- CH-24 : sans objet. Les délais de 300 et 360 minutes figurent une fois chacun dans les scripts de l'instance au commit `03cb538`.

**Ce que je n'ai pas pu vérifier**
- Je n'ai rejoué aucun banc. RCh-01 se montre par un appel direct du module.
- Je n'ai pas joué le bloc 10 (il faut le réseau) ni la suite complète des tests.
- Le comportement de Vast.ai devant un crédit insuffisant pendant la garde de 72 heures.
- La répartition réelle de `storage_total_cost` sur les offres conformes.
- Les journaux officiels n'existent pas encore.
- La répétition jouet non officielle a tourné au code d'essai K, pas au commit `03cb538`. Les scripts de l'instance de K ne diffèrent de ceux de `03cb538` que par des commentaires et l'ordre des listes de fichiers.
- Le candidat versé différera du candidat 1 relu, puisque le champ de la relecture courte reste à remplir.

Mes fichiers de travail sont dans `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p3-relecture-courte/chaine/`. Le dépôt n'a pas été modifié : `git status` est vide.

**Jugement d'ensemble** : scellable après traitement. RCh-01 bloque tout : il faut un brouillon 3 du module, rejouer les bancs du lanceur, des contrôles et du scellement, puis une relecture courte de ce changement.
