#!/usr/bin/env python3
"""Commande externe d'Argon (gemini-4-argon) — version 3d : la v3c corrigée après sa contre-lecture (deux relecteurs neufs).

Lignée session-depot, 30 octobre 2026. Copie de `commande_argon_v3c.py` (empreinte `135a7153c94fb3c2…`, inchangée, R12).
Version : `commande-argon-v3d`. Lancée par `appel-argon-v4d.sh` (copie de la v4c dont le seul changement est le nom de la
commande lancée). Les codes 0 à 10 gardent leur sens ; un code est ajouté, le **11**.

## Ce qui change depuis la v3c, et pourquoi

1. **Jetons facturés hors des champs lus, par `totalTokenCount` (bloquant).** La v3c ne lisait jamais
   `usageMetadata.totalTokenCount`. Scénario démontré hors réseau (`poster` remplacé par un faux, plafond 3 USD, réglages
   figés de la v4c) : `promptTokenCount` 105, `candidatesTokenCount` 10, `totalTokenCount` 2 000 000 → code 0,
   `cout_usd` 0,0513 avec `--recherche-web`, 0,0013 sans ; si l'amont facture le total, la dépense dépasse le plafond et la
   commande rend un succès. Même classe de défaut que le bloquant 1 de la v3b. La v3d :
   (a) lit `totalTokenCount` comme les autres champs facultatifs de l'usage : absent, il ne compte pas (comportement de
       la v3c) ; présent mais mal formé (pas un entier ≥ 0, booléen compris), l'usage est **mal formé** (code 5 au pire
       cas, ou code 8 si les requêtes lues dépassent le maximum, comme tout champ d'usage mal formé depuis la v3b) ;
   (b) calcule l'**écart** = `totalTokenCount` − (jetons comptés au coût : `promptTokenCount` + `candidatesTokenCount` +
       `thoughtsTokenCount`, plus `toolUsePromptTokenCount` **avec `--recherche-web` seulement**, le seul mode où il est
       compté). Sans la recherche, des jetons d'outil rendus quand même ne sont pas comptés à part : ils tombent dans
       l'écart, donc comptés au prix de sortie et nommés, jamais ignorés (plus strict que la correction proposée, qui les
       retranchait dans les deux modes et les aurait laissés non comptés sans la recherche) ;
   (c) un écart > 0 est **compté au coût au prix de sortie** (prudent), dans le coût rendu et dans la comparaison exacte
       au plafond (code 10) ; avec `--recherche-web`, il est aussi compté **contre la provision d'outil** (comme
       l'excédent d'entrée) : excédent d'entrée + jetons d'outil + écart > `--provision-outil-jetons` → code 9 ;
   (d) un écart > 0 est **toujours un échec nommé**, **code 11** (`USAGE_INCOHERENT`) quand aucun des codes 7 à 10 ne
       le prend : texte vide, coût réel compté sur l'usage, écart compris. Pourquoi un échec et non un avertissement :
       un total au-delà des champs lus veut dire que l'usage ne se lit plus comme le suppose la garde (champ nouveau,
       facturation inconnue) ; un code 0 le rendrait invisible au noyau ; arrêter et lire, comme pour les codes 7 à 10.
       Ordre : 7, 8, 9, 10, puis 11 ; tous priment sur le code 5 ;
   (e) un écart < 0 (total sous la somme des champs lus) ne change ni le coût (la somme des champs, plus grande, est
       comptée) ni le code : avertissement seul.
   Champs de diagnostic ajoutés : `total_jetons` (le `totalTokenCount` lu, ou `null`) et `ecart_total_jetons` (l'écart,
   ou `null` sans total) ; `provision_outil_consommee_jetons` comprend l'écart positif.

Codes de sortie : ceux de la v3c (0, 2 à 10), plus **11 usage incohérent : `totalTokenCount` au-delà des jetons comptés**
(échec, texte vide, coût réel sur l'usage écart compris ; après 7 à 10, avant 5).

Usage : celui de la v3c (mêmes réglages), en remplaçant le nom du fichier par `commande_argon_v3d.py`.

## En-tête de la v3c (inchangé ci-dessous ; le point 1 ci-dessus le corrige là où il le contredit)

Commande externe d'Argon (gemini-4-argon) — version 3c : la v3b corrigée après sa contre-lecture (relecteur neuf).

Lignée session-depot, 30 octobre 2026. Copie de `commande_argon_v3b.py` (empreinte `e60204476bd133be…`, inchangée, R12).
Version : `commande-argon-v3c`. Lancée par `appel-argon-v4c.sh` (copie de la v4b qui lance cette commande et fige, après
`"$@"`, les prix et les bornes de la garde). Les codes 0 à 9 gardent leur sens ; un code est ajouté, le **10**.

## Ce qui change depuis la v3b, et pourquoi

1. **Coût au-delà du plafond rendu comme un succès (bloquant).** La v3b ne regardait que `toolUsePromptTokenCount` pour la
   provision d'outil ; une entrée facturée (`promptTokenCount`) au-delà de l'entrée gardée et un coût au-delà du plafond
   ne donnaient qu'un avertissement. Scénario démontré hors réseau (plafond 3 USD) : entrée facturée 60 400 jetons pour
   420 gardés (contenu de la recherche compté dans l'entrée), sortie maximale, 20 requêtes, 32 768 jetons d'outil → code
   0, `cout_usd` 3,4978. La v3c :
   (a) **avec ou sans `--recherche-web`**, tout coût calculé sur l'usage au-delà de `PLAFOND_SESSION_USD` est un **échec
       nommé, code 10** (`COUT_HORS_PLAFOND`) : texte vide (jamais rendu comme conforme), coût réel compté sur l'usage,
       pour la même raison que les codes 7, 8 et 9 (la somme des plafonds ne borne plus la dépense ; arrêter et lire). La
       comparaison est **exacte** (fractions : jetons entiers, prix et plafond lus par `repr`, comme la marge) : aucun
       échec dû au seul arrondi binaire au bord du pire cas, aucun dépassement réel masqué par lui. Ordre : 7, 8, 9, puis
       10 ; tous priment sur le code 5. Sans `--recherche-web`, c'est le **seul** changement de comportement par rapport
       à la v2 et à la v3b : une entrée facturée au-delà de l'entrée gardée qui porte le coût au-delà du plafond (CL44-03,
       jusqu'ici un avertissement à code 0) devient le code 10 ; en deçà du plafond, l'avertissement de la v2 reste seul ;
   (b) **avec `--recherche-web`**, l'excédent d'entrée facturée sur l'entrée gardée est compté **contre la provision
       d'outil** (même prix, celui d'entrée) : excédent + `toolUsePromptTokenCount` > `--provision-outil-jetons` → **code
       9** (même nom, message qui donne les deux parts). Champs de diagnostic ajoutés : `entree_excedent_jetons` (les deux
       modes) et `provision_outil_consommee_jetons` (avec la recherche seulement).
2. **`webSearchQueries` en partie illisible (mineur).** 30 chaînes et un `null` faisaient compter 20 requêtes (le maximum)
   au lieu de 30. La v3c : une liste qui porte au moins un élément qui n'est pas une chaîne fait compter **max(longueur de
   la liste, maximum du pire cas)** requêtes — tout élément compte, et jamais moins que le repli prudent de la v3b ; au-delà
   du maximum, code 8 comme pour une liste de chaînes. Les chaînes non vides sont listées ; origine « maximum_pire_cas ou
   longueur (webSearchQueries en partie illisible) », avertissement. (La contre-lecture proposait max(longueur, chaînes
   non vides), qui vaut la longueur et ferait compter 1 requête pour `[null]` là où la v3b en comptait 20 : écarté.)
3. **Jetons d'outil sans requête listée (mineur).** `webSearchQueries` vide, aucune source, `toolUsePromptTokenCount` > 0
   faisaient compter 0 requête. La v3c tient un `toolUsePromptTokenCount` entier > 0 pour un **témoin de recherche** au
   même titre que `groundingChunks`, `groundingSupports` et `searchEntryPoint` (v3b, point 2) : coût de recherche compté
   au maximum du pire cas, origine « maximum_pire_cas (requêtes vides, jetons d'outil facturés) » quand il est le seul
   témoin, avertissement. Le témoin est lu, sans contrôle de forme, avant la lecture de l'usage ; un
   `toolUsePromptTokenCount` mal formé reste traité comme en v3b (code 5 ou 8, pire cas).
4. **Enveloppe (mineur, `appel-argon-v4c.sh`).** La v4b passait `"$@"` après `--prix-entree` et `--prix-sortie` : le noyau
   pouvait baisser les prix, régler `--provision-outil-jetons 0` ou `--prix-requete-web-usd`. La v4c pose **après**
   `"$@"` : `--prix-entree 8.3 --prix-sortie 41.5 --prix-requete-web-usd 0.05 --max-requetes-web-pire-cas 20
   --provision-outil-jetons 32768 --url-base …` ; `argparse` garde la dernière occurrence (vérifié par les essais, sur
   l'analyseur et sur une exécution). Restent réglables par le noyau, sans être figés (pas de changement demandé) :
   `--delai-s` (posé avant `"$@"`, borné de toute façon par `timeout` 1700 s), `--marge-entree`, `--provision-pensee-jetons`,
   `--max-sortie-jetons`, `--sortie-min-jetons`, `--caracteres-par-jeton`, `--sans-compter-jetons`, `--sans-config-pensee`,
   `--modele`, `--recherche-web` : ils changent la garde avant envoi, jamais le contrôle après coup (codes 7 à 10).
5. **Documenté, non corrigé (mineurs 5 et 6 de la contre-lecture).**
   - Le masquage de la vraie clé dans le corps relayé par `relais_gemini_v2.py` se fait **par octets exacts** : une forme
     échappée de la clé dans le JSON de l'amont (`\\uXXXX`, par exemple) n'est pas reconnue par le relais ; décodée par
     cette commande, qui ne détient que la clé factice, elle traverserait jusqu'à la sortie. Risque résiduel, à corriger
     dans le relais (décoder puis masquer), pas ici.
   - Un signal (SIGTERM, SIGINT, délai) reçu **juste après** la réponse, avant la lecture de `groundingMetadata` (fenêtre
     de l'ordre de la microseconde, entre le retour de `poster` et l'arrêt de la minuterie) donne le code 6 au pire cas
     **sans** le supplément des requêtes lues au-delà du maximum (pas encore lues) : coût sous-estimé dans ce seul cas.

Codes de sortie : ceux de la v3b (0, 2 à 9), plus **10 coût calculé sur l'usage au-delà du plafond de session** (échec,
texte vide, coût réel sur l'usage ; après 7, 8 et 9, avant 5).

Usage : celui de la v3b (mêmes réglages), en remplaçant le nom du fichier par `commande_argon_v3c.py`.

## En-tête de la v3b (inchangé ci-dessous ; les points 1 à 5 ci-dessus le corrigent là où ils le contredisent)

Commande externe d'Argon (gemini-4-argon) — version 3b : la v3 corrigée après deux contre-lectures.

Lignée session-depot, 30 octobre 2026. Copie de `commande_argon_v3.py` (empreinte `b436b7a5977f3287…`, inchangée, R12).
Version : `commande-argon-v3b`. Lancée par `appel-argon-v4b.sh` (l'enveloppe v4, qui lance cette commande au lieu de la v3).
Sans `--recherche-web`, le corps envoyé, la garde, le coût et les codes restent ceux de la v2 ; seuls changent `version`, des
champs de diagnostic ajoutés au JSON, le masquage (étendu à toutes les chaînes, point 5), l'échappement de trois
séparateurs de ligne Unicode (point 6), qui ne change pas l'objet décodé, et deux sortes de parties de réponse désormais
refusées, `functionResponse` et `codeExecutionResult` (point 4 ; la v2 ne refusait que `functionCall` et `executableCode`).

## Ce qui change depuis la v3, et pourquoi

1. **Requêtes au-delà du maximum avec un usage illisible (majeur).** La v3 comptait alors le pire cas (qui ne paie que
   `--max-requetes-web-pire-cas` requêtes) et rendait le code 5 : coût sous-estimé, code faux. La v3b garde
   `supplement_recherche_usd` = max(0, requêtes lues − maximum) × prix par requête dès la lecture de `groundingMetadata`,
   l'ajoute à tout coût de repli au pire cas (échec nommé, interruption, erreur inattendue), et rend le **code 8** (au lieu
   du 5) quand les requêtes lues dépassent le maximum et que `usageMetadata` manque ou est mal formé
   (`toolUsePromptTokenCount` compris).
2. **Liste `webSearchQueries` vide alors qu'une recherche a eu lieu (majeur).** Si la liste est vide mais que
   `groundingChunks`, `groundingSupports` ou `searchEntryPoint` ne le sont pas, le coût compte le **maximum** du pire cas
   (origine « maximum_pire_cas (requêtes vides, sources présentes) », avertissement). 0 requête n'est gardé que si rien ne
   témoigne d'une recherche.
3. **Jetons d'outil non provisionnés (majeur).** Nouvelle option `--provision-outil-jetons N` (défaut **32 768 : SUPPOSÉ**,
   aucune mesure de `toolUsePromptTokenCount` sur gemini-4-argon), comptée **seulement avec `--recherche-web`** au prix
   d'entrée dans la garde avant envoi (donc dans `pire_cas_usd`, et payée avant la provision de pensée et la sortie). Après
   la réponse, `toolUsePromptTokenCount` > N rend le **code 9** (`JETONS_OUTIL_HORS_PROVISION`), un échec nommé, coût réel
   sur l'usage, pour la même raison que les codes 7 et 8. Ordre : 7, puis 8, puis 9 ; tous trois priment sur le code 5.
   Reste hors garde, comme en v2 (CL44-03, décision antérieure) : une entrée facturée au-dessus de l'entrée gardée
   (avertissement, code inchangé).
4. **Parties refusées.** Toute partie de réponse qui porte `functionCall`, `functionResponse`, `executableCode` ou
   `codeExecutionResult` est non conforme (code 5) ; le message dit « seul google_search est déclaré » avec l'option,
   « aucun outil n'est déclaré » sans elle.
5. **Masquage.** (a) `ligne()` masque la clé dans **toutes** les chaînes de l'objet rendu (`modele_servi`, `fin`, `texte`
   compris ; la v2 et la v3 rendaient `modele_servi` et `fin` bruts). (b) `nettoyer_web` masque la valeur brute, remplace
   les caractères non imprimables, masque de nouveau, puis, si la clé réapparaît une fois les blancs retirés (clé coupée
   par un caractère de contrôle ou un blanc), rend la forme sans blancs, masquée. La correction proposée (« masquer,
   nettoyer, masquer ») ne suffisait pas : une clé coupée par `\\x00` ne correspond à la clé ni avant ni après le
   remplacement par une espace. (c) **Sous l'enveloppe v4 ou v4b, cette commande ne détient que la clé factice
   `factice-relais`** : son masquage ne protège pas la vraie clé, qui n'est connue que du relais. Cette garantie repose sur
   le relais : `relais_gemini_v1.py` ne masque la vraie clé que dans les en-têtes relayés, pas dans le corps ;
   `relais_gemini_v2.py` (même dossier) la masque aussi dans le corps de la réponse.
6. **Dernière ligne lisible par `str.splitlines()`.** `json.dumps(ensure_ascii=False)` laisse bruts U+2028, U+2029 et
   U+0085, où `splitlines()` (l'adaptateur du noyau) coupe la ligne. La v3b les échappe en `\\u2028`, `\\u2029`,
   `\\u0085` après sérialisation : l'objet décodé est identique, les octets ne changent que si ces caractères sont présents
   (une ligne que l'adaptateur ne lisait pas). Les autres séparateurs de `splitlines()` (`\\x0b`, `\\x0c`, `\\x1c` à
   `\\x1e`) sont déjà échappés par `json.dumps`.
7. **Adresses des sources.** Seules `https://` et `http://` avec un hôte sont gardées ; sinon la source est rendue avec
   l'adresse « [adresse refusée : schéma X] » et un avertissement.
8. **Bornes du texte ajouté.** Au plus 50 requêtes et 50 sources listées (200 en v3) ; requêtes et titres coupés à 200
   caractères, adresses à 500 (une adresse de redirection de Google dépasse souvent 200) ; section « Sources consultées »
   plafonnée à 20 000 caractères (au-delà : coupée, marquée, avertissement). Les éléments non listés sont dits en
   avertissement. Le compte facturé n'est jamais coupé.

**Au devis (point 5 de la contre-lecture, pas de code).** Avec `--recherche-web`, le coût déclaré au noyau par un appel peut
aller jusqu'à `pire_cas_usd` sans dépense réelle correspondante : `groundingMetadata` absent (le modèle n'a pas cherché, cas
courant) ou requêtes illisibles font compter le maximum de requêtes (20 × 0,05 = 1 USD par défaut, SUPPOSÉ), et un usage
illisible fait compter tout le pire cas. La somme des coûts déclarés peut donc atteindre l'enveloppe du tour et arrêter la
course à tort. Régler `--max-requetes-web-pire-cas` et `--prix-requete-web-usd` après lecture du prix réel par Lazar est une
décision, pas un automatisme.

Codes de sortie : ceux de la v3 (0, 2 à 8), plus **9 jetons d'outil au-delà de la provision** (échec, coût sur l'usage).

Usage :
    python3 -I -B commande_argon_v3b.py [réglages de la v2] [--recherche-web] [--prix-requete-web-usd 0.05]
        [--max-requetes-web-pire-cas 20] [--provision-outil-jetons 32768]

## En-tête de la v3 (inchangé ci-dessous ; les points 1 à 8 ci-dessus le corrigent là où ils le contredisent)

Commande externe d'Argon (gemini-4-argon) — version 3 : appel nu par défaut, **recherche Google sur option**.

Lignée session-depot, 30 octobre 2026. Copie de `commande_argon_v2.py` (empreinte `6905ac71f126bfd4…`, `/opt/argon`,
inchangée, R12). Version : `commande-argon-v3`. Lancée par `appel-argon-v4.sh` (même enveloppe que la v3, qui lance cette
commande au lieu de la v2), derrière le relais Gemini local `relais_gemini_v1.py` (inchangé : il relaie le corps tel quel,
champ `tools` compris, et la réponse telle quelle ; son journal ne garde jamais `groundingMetadata`).

## Ce qui change depuis la v2, et pourquoi

Le directeur veut un appel d'Argon **avec recherche sur le Web** (outil de recherche de Google, « grounding with Google
Search »), sous un plafond de session de 3 USD. Les seuls changements :

(a) **Option `--recherche-web`** : ajoute au corps de `generateContent` le champ `tools: [{"google_search": {}}]`, et rien
    d'autre (ni `toolConfig`, ni fonction, ni consigne système). Sans l'option, le corps envoyé est **identique** à celui de
    la v2 (vérifié par les essais, octet pour octet sur l'objet JSON). Le corps de `countTokens` ne change jamais (contenus
    seuls). Un refus du champ par l'interface (HTTP 4xx) remonte tel quel, code 3, coût plancher : **aucun repli** (R5) ;
    relancer sans `--recherche-web` est une décision.
(b) **Lecture de `candidates[0].groundingMetadata`** : `webSearchQueries` (requêtes), `groundingChunks[].web.uri` et
    `.title` (sources, dans l'ordre, sans doublon d'adresse), `groundingSupports` (seulement leur nombre, au diagnostic).
    Le texte rendu au noyau est suivi d'une section « Sources consultées (recherche Google) » qui liste les requêtes, puis
    les titres et adresses des sources ; si `groundingMetadata` manque, la section le dit. Le JSON de la dernière ligne
    ajoute `requetes_web` (liste de chaînes) et `sources_web` (liste de `{"uri", "titre"}`) — toujours présents, vides
    sans l'option —, plus des champs de diagnostic que le noyau ignore (`recherche_web`, `requetes_web_facturees`,
    `requetes_web_origine`, `prix_requete_web_usd`, `max_requetes_web_pire_cas`, `cout_recherche_usd`, `appuis_web`,
    `outil_jetons`).
(c) **Coût de la recherche**, facturé hors des jetons :
    - `--prix-requete-web-usd` (défaut **0,05 : SUPPOSÉ**, volontairement haut, non lu sur la console de facturation ; le
      prix réel par requête, ou par consigne « ancrée » selon le modèle, est à lire par Lazar) ;
    - `--max-requetes-web-pire-cas` (défaut 20) : l'interface ne permet pas de borner le nombre de recherches ; ce
      maximum est une **hypothèse de garde** ;
    - garde du pire cas **avant envoi** : pire cas = entrée gardée × prix d'entrée + max-requêtes × prix par requête +
      (`maxOutputTokens` + provision de pensée) × prix de sortie ≤ plafond ; sinon refus sans envoi (code 4). Le reste du
      plafond paie d'abord les requêtes, puis la provision de pensée, puis la sortie ;
    - coût rendu = coût des jetons (v2) + (nombre de requêtes lues dans `webSearchQueries`, ou le **maximum** si
      `groundingMetadata` ou `webSearchQueries` manquent ou sont illisibles — prudent, signalé en avertissement) × prix ;
    - les jetons `usageMetadata.toolUsePromptTokenCount` (contexte apporté par l'outil, s'il est rendu) sont comptés au
      prix d'entrée (SUPPOSÉ) ; la garde avant envoi ne les borne pas : leur présence est dite en avertissement, avec le
      dépassement du plafond s'il y en a un (même traitement que l'entrée au-delà de la garde, CL44-03) ;
    - si le nombre de requêtes lues **dépasse** `--max-requetes-web-pire-cas`, la garde ne tient plus : **code 8**, un
      échec nommé (texte vide, coût réel compté sur l'usage et sur toutes les requêtes lues), pour la même raison que le
      code 7 de la v2 (la somme des plafonds ne borne plus la dépense ; arrêter et lire). Le code 7 prime sur le code 8,
      et les deux priment sur le code 5.
(d) **Aucune autre fonction ni aucun autre outil** n'est permis : le seul outil déclarable est `google_search`, sans
    option ; une réponse qui porte un appel de fonction ou du code exécutable reste non conforme (code 5).
(e) Cette docstring ; le nom du programme dans les messages d'erreur devient `commande_argon_v3`.

Sans `--recherche-web`, le comportement est celui de la v2 (même corps, même garde, même coût, mêmes codes) ; seuls
changent `version` et les champs ajoutés au JSON (listes vides, `recherche_web` faux).

Codes de sortie : ceux de la v2 (0, 2 à 7), plus **8 requêtes de recherche au-delà du maximum du pire cas** (échec, coût sur
l'usage et les requêtes lues).

Usage :
    python3 -I -B commande_argon_v3.py [réglages de la v2] [--recherche-web] [--prix-requete-web-usd 0.05]
        [--max-requetes-web-pire-cas 20]

## En-tête de la v2 (inchangé ci-dessous)

Commande externe d'Argon (gemini-4-argon) pour la course d'idéation du pôle — **appel nu**, version 2.

Lignée session-depot, 29 octobre 2026. Remplace `lancement-v1/commande_argon_v1.py` (empreinte `f3acf365…`, archivée sans
modification, R12). Même contrat que la v1 pour `AdaptateurCommandeExterne` (`pole/adaptateurs.py`, orchestrateur du pôle
v7, v43 et v44 : le fichier est identique).

## Ce qui change depuis la v1, et pourquoi

Contre-lecture `docs/notes/ideation-organisme-v1/contre-lecture-v44-cl11.md`, sections 4 et 6 :

- **CL44-02 (majeur) — pensées d'Argon non provisionnées.** La v1 bornait `maxOutputTokens` au reste du plafond mais
  facturait `thoughtsTokenCount` en plus, sans poser de `thinkingConfig` : si l'interface ne compte pas les pensées dans
  `maxOutputTokens`, le plafond est dépassé (3,43 > 3,1 démontré) ; si elle les compte, la sortie est tronquée
  (`MAX_TOKENS`). La v2 :
  1. réserve une **provision de pensée explicite** `--provision-pensee-jetons N` (défaut **8 192**), comptée au prix de
     sortie dans la garde **avant envoi** : pire cas = entrée gardée × prix d'entrée + (`maxOutputTokens` + N) × prix de
     sortie ≤ plafond. La garde tient quel que soit le comportement de l'interface : pensées hors de `maxOutputTokens`,
     elles sont payées par la provision ; pensées dans `maxOutputTokens`, la provision est une réserve de trop
     (conservateur) ;
  2. **pose** `generationConfig.thinkingConfig.thinkingBudget = N` (désactivable par `--sans-config-pensee`, explicite).
     Si l'interface refuse ce champ (HTTP 4xx), l'erreur remonte telle quelle, code 3, coût plancher comme tout 4xx de la
     v1 : **aucun repli silencieux** (R5) ; relancer sans le champ est une décision, pas un automatisme ;
  3. après la réponse, si `thoughtsTokenCount` > N : le journal (sortie d'erreur, champ `erreur`) le dit en clair et la
     commande rend le **code 7**, un **échec** : texte vide, coût réel compté sur l'usage. Pourquoi un échec et non un
     avertissement : (a) la provision est la seule hypothèse qui garantit le plafond de session ; quand elle est franchie,
     la garantie ne tient plus pour la session suivante non plus (la somme des plafonds ne borne plus la dépense de la
     course), et la course doit s'arrêter là où on le voit, non continuer sur une hypothèse fausse ; (b) avec
     `thinkingConfig` posé, un dépassement veut dire que l'interface n'honore pas le budget : fait nouveau, à lire avant
     toute dépense de plus ; (c) l'adaptateur du noyau traite **tout** code non nul comme une erreur (texte écarté, coût
     imprimé compté) : un « avertissement à code non nul » serait un échec qui ne dit pas son nom, et un code 0 le rendrait
     invisible au noyau. Le code 7 prime sur les non-conformités de la réponse (code 5) : il touche l'argent.
  Diagnostic ajouté : `lecture_pensees` vaut `hors_max_sortie` quand `candidatesTokenCount + thoughtsTokenCount` dépasse
  `maxOutputTokens` (démontré, sur cet appel : l'interface ne compte pas les pensées dans `maxOutputTokens`), sinon
  `indetermine` ; à lire au journal du premier appel (le contrôle d'Argon), comme le recommande CL44-02.
- **CL44-03 (mineur) — borne « à l'erreur de compte près ».** Une entrée facturée au-dessus de l'estimation dépassait le
  plafond (3,71 > 3,1 démontré). La v2 : `--compter-jetons` est **activé par défaut** (compte exact par `countTokens`,
  gratuit ; désactivable par `--sans-compter-jetons`, explicite ; `--compter-jetons` reste accepté) ; une **marge
  d'entrée** `--marge-entree` (défaut 0,05) multiplie l'entrée gardée : entrée gardée = ⌈max(estimée, comptée) × (1 +
  marge)⌉. Après la réponse, une entrée facturée (`promptTokenCount`) au-dessus de l'entrée gardée est dite au journal
  (avertissement, code inchangé : le noyau compte le coût déclaré et arrête la course si le plafond est dépassé).

Pourquoi **8 192** par défaut. C'est la plus grande puissance de deux qui garde **acceptées** les quatre tailles de
consigne mesurées par CL11 (§ 4 : contrôle 1 077 663 caractères à 3,1 ; passe 1 685 992 à 2,5 ; passe 2 1 173 975, garde
de la v44, à 3,1 ; juge 1 166 746 à 3,5), avec la marge de 5 % et `--sortie-min-jetons` 4 096 : la passe 2 garde 4 872
jetons de sortie (16 384 la refuserait, et refuserait aussi le contrôle). Elle couvre le cas démontré de CL44-02 (8 000
jetons de pensée). Coût de la réserve : 8 192 × 41,5 / 10⁶ ≈ 0,34 USD par session, rendu au noyau si Argon ne pense pas
(le coût rendu est celui de l'usage). Un budget de pensée plus grand exige un plafond de session plus grand : c'est au
devis de le dire. Réserve : si l'interface compte les pensées **dans** `maxOutputTokens`, la place du texte est
`maxOutputTokens` − pensées ≥ `maxOutputTokens` − N (budget honoré) ; à la passe 2 au bord, une troncature (code 5) reste
possible, au coût borné par le plafond.

Le reste du comportement de la v1 ne change pas (contrat, clé, appel nu, mandataire, barème, coût rendu, codes 0 à 6,
délai, signaux).

## Contrat (inchangé)

- la consigne arrive sur l'**entrée standard** (UTF-8) ; elle est envoyée telle quelle, en un seul message utilisateur ;
- l'environnement est minimal : le plafond de la session est lu dans `PLAFOND_SESSION_USD`, le rôle dans `ROLE_POLE`
  (`proposeur_ideation` ou `juge_ideation`) ; la clé est lue dans **`GEMINI_API_KEY`** (nom fixe), jamais en argument,
  jamais dans un fichier lu par ce script ; elle n'est jamais écrite (sortie, erreurs, journal) ;
- la **dernière ligne** de la sortie standard est **toujours** un objet JSON `{"texte": …, "cout_usd": …}` (plus des
  champs de diagnostic que le noyau ignore), avec un coût **fini et strictement positif**, aussi sur un échec.

Appel nu : une requête `generateContent` de l'interface de génération de contenu de Google, **aucun outil ni fonction
déclarés**, aucune consigne système, aucune reprise automatique (un échec est nommé et rendu ; la relance appartient au
noyau et à ses tentatives). Le seul champ ajouté au corps depuis la v1 est `generationConfig.thinkingConfig`. Le
mandataire réseau est celui de l'environnement (`HTTPS_PROXY`, `SSL_CERT_FILE`) ; une adresse en `http://` n'est permise
que vers la boucle locale (essais), et alors sans mandataire.

Barème (dollars par million de jetons) :
- entrée **8,3** : borne lue par Lazar sur la console de facturation de la clé (R-718 ; « ≤ 8,3 ») ;
- sortie **41,5 : SUPPOSÉ**, non lu — rapport 5 entre sortie et entrée, la convention du barème du code (`BAREME_INCONNU`,
  50 / 10, `pole/relais_reel.py`), appliqué à 8,3. Les pensées sont comptées au prix de sortie (SUPPOSÉ, comme en v1).
  Les deux prix sont réglables (`--prix-entree`, `--prix-sortie`) et consignés au manifeste par la ligne de commande.

Garde du pire cas, **avant tout envoi** : entrée estimée = caractères / 4 (`--caracteres-par-jeton`), ou le compte exact
`countTokens` s'il est plus grand (par défaut) ; entrée gardée = ⌈entrée × (1 + `--marge-entree`)⌉ ; sortie maximale
demandée = min(`--max-sortie-jetons`, ce que le reste du plafond paie au prix de sortie **moins la provision de pensée**) ;
si cette sortie est sous `--sortie-min-jetons`, autrement dit si entrée gardée + sortie minimale + provision dépassent le
plafond, **refus sans envoi** (code 4). Ainsi le pire cas facturable (entrée gardée + `maxOutputTokens` + provision) ne
dépasse jamais `PLAFOND_SESSION_USD`, sous deux hypothèses désormais **vérifiées après coup** : pensées ≤ provision (sinon
code 7) et entrée facturée ≤ entrée gardée (sinon avertissement au journal).

Coût rendu : sur l'usage rendu (`usageMetadata` : `promptTokenCount` au prix d'entrée ; `candidatesTokenCount` +
`thoughtsTokenCount` au prix de sortie) ; usage absent après un envoi → **pire cas** compté (prudent ; provision comprise) ;
rien envoyé, ou requête refusée par l'interface avant génération (HTTP 4xx) → coût plancher 1e-6 (le contrat interdit 0 ;
`envoye` et `cout_origine` le disent) ; erreur 5xx, connexion coupée après envoi, délai → pire cas.

Codes de sortie : 0 réponse conforme ; 2 réglage ou entrée refusés (rien envoyé) ; 3 interface (HTTP, connexion ; refus
de `thinkingConfig` compris) ; 4 pire cas au-dessus du plafond (rien envoyé) ; 5 réponse non conforme (vide, usage absent,
tronquée, bloquée, modèle servi différent, JSON illisible) ; 6 délai dépassé ou interruption (SIGTERM, SIGINT) ;
**7 pensées au-delà de la provision** (nouveau, échec, coût sur l'usage).

Usage (sous l'utilisateur distinct d'Argon, la clé posée par l'enveloppe de changement d'utilisateur) :
    python3 -I -B commande_argon_v2.py [--modele gemini-4-argon] [--url-base URL] [--prix-entree 8.3] [--prix-sortie 41.5]
        [--max-sortie-jetons 65536] [--sortie-min-jetons 4096] [--provision-pensee-jetons 8192] [--sans-config-pensee]
        [--marge-entree 0.05] [--sans-compter-jetons] [--delai-s 1500]
"""

import argparse
import json
import math
import os
import signal
import socket
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from fractions import Fraction

VERSION = "commande-argon-v3d"
MODELE_DEFAUT = "gemini-4-argon"
URL_BASE_DEFAUT = "https://generativelanguage.googleapis.com/v1beta"
VARIABLE_CLE = "GEMINI_API_KEY"
PRIX_ENTREE_DEFAUT = 8.3   # USD par million de jetons d'entrée : borne lue par Lazar (R-718)
PRIX_SORTIE_DEFAUT = 41.5  # SUPPOSÉ : rapport 5 du barème du code, non lu sur la console
CARACTERES_PAR_JETON_DEFAUT = 4.0
MAX_SORTIE_JETONS_DEFAUT = 65536
SORTIE_MIN_JETONS_DEFAUT = 4096
PROVISION_PENSEE_JETONS_DEFAUT = 8192  # CL44-02 : voir l'en-tête (plus grande puissance de deux qui garde les tailles CL11)
MARGE_ENTREE_DEFAUT = 0.05             # CL44-03
DELAI_DEFAUT_S = 1500.0    # sous le délai du noyau (1800 s) et sous l'arrêt dur de l'enveloppe (timeout 1700 s)
COUT_PLANCHER_USD = 1e-6   # le contrat exige un coût > 0 ; rien n'a été facturé
ROLES = ("proposeur_ideation", "juge_ideation")
HOTES_LOCAUX = {"127.0.0.1", "localhost", "::1"}
TAILLE_MAX_REPONSE = 50_000_000

OK, REGLAGE, INTERFACE, PIRE_CAS, NON_CONFORME, DELAI, PENSEES_HORS_PROVISION = 0, 2, 3, 4, 5, 6, 7

# v3 — recherche Google sur option (voir l'en-tête)
REQUETES_WEB_HORS_PIRE_CAS = 8
PRIX_REQUETE_WEB_DEFAUT = 0.05          # SUPPOSÉ : USD par requête de recherche, volontairement haut, non lu sur la console
MAX_REQUETES_WEB_PIRE_CAS_DEFAUT = 20   # hypothèse de garde : l'interface ne borne pas le nombre de recherches
TITRE_SOURCES = "Sources consultées (recherche Google)"
LONGUEUR_MAX_CHAMP_WEB = 500            # v3b (8) : une adresse au-delà est coupée (marquée « … »)
LONGUEUR_MAX_TEXTE_WEB = 200            # v3b (8) : une requête ou un titre au-delà est coupé (marqué « … »)
NOMBRE_MAX_ELEMENTS_WEB = 50            # v3b (8) : requêtes ou sources listées au plus (le compte facturé n'est pas coupé)
LONGUEUR_MAX_SECTION = 20_000           # v3b (8) : caractères de la section des sources, au plus
# v3b (3) : jetons d'outil (toolUsePromptTokenCount) provisionnés au prix d'entrée avec --recherche-web ; SUPPOSÉ
JETONS_OUTIL_HORS_PROVISION = 9
PROVISION_OUTIL_JETONS_DEFAUT = 32768
# v3b (4) : parties de réponse refusées (seul google_search est déclarable, et lui seul ne rend aucune de ces parties)
PARTIES_INTERDITES = ("functionCall", "functionResponse", "executableCode", "codeExecutionResult")
# v3c (1a) : coût calculé sur l'usage au-delà du plafond de session (avec ou sans recherche) : échec nommé
COUT_HORS_PLAFOND = 10
# v3d (1d) : totalTokenCount au-delà des jetons comptés au coût : échec nommé (écart compté au prix de sortie)
USAGE_INCOHERENT = 11


def exact(x):
    """v3c (1a) : réel en fraction exacte, lu par `repr` comme la marge (8,3 vaut 83/10, 0,05 vaut 1/20)."""
    return Fraction(repr(float(x)))


def outil_recherche():
    """Le seul outil permis (d) : la recherche Google, sans option. Un objet neuf à chaque appel."""
    return [{"google_search": {}}]


def nettoyer_web(valeur, cle, longueur=LONGUEUR_MAX_CHAMP_WEB):
    """Chaîne lisible sur une ligne : sans caractère de contrôle, sans la clé, coupée à `longueur`.
    v3b (5b) : masque la valeur brute, remplace les caractères non imprimables par une espace, masque de nouveau ; si la clé
    réapparaît une fois tous les blancs retirés (clé coupée par un contrôle ou un blanc), rend cette forme compacte, masquée.
    Le masquage passe toujours avant la coupe."""
    brut = masquer(str(valeur), cle)
    texte = masquer("".join(c if c.isprintable() else " " for c in brut), cle).strip()
    if cle:
        compact = "".join(c for c in texte if not c.isspace())
        if cle in compact:
            texte = masquer(compact, cle)
    return texte if len(texte) <= longueur else texte[:longueur] + "…"


def adresse_permise(uri):
    """(True, None) pour une adresse `https://` ou `http://` avec un hôte ; sinon (False, schéma lisible)."""
    try:
        p = urllib.parse.urlsplit(uri)
        hote = p.hostname
    except ValueError:
        return False, "illisible"
    if p.scheme in ("https", "http") and hote:
        return True, None
    schema = "".join(c for c in p.scheme if c.isalnum() or c in "+-.")[:20]
    return False, (schema or "absent") if p.scheme not in ("https", "http") else f"{p.scheme} sans hôte"


def temoins_de_recherche(gm, outil_jetons=0):
    """Champs non vides de `groundingMetadata` qui témoignent d'une recherche (v3b, point 2) ; v3c (3) : plus
    `toolUsePromptTokenCount` quand l'usage en rend un entier > 0 (l'outil a apporté du contexte facturé)."""
    temoins = [nom for nom in ("groundingChunks", "groundingSupports", "searchEntryPoint")
               if isinstance(gm.get(nom), (list, dict, str)) and gm.get(nom)]
    if outil_jetons > 0:
        temoins.append("toolUsePromptTokenCount")
    return temoins


def temoin_outil(usage):
    """v3c (3) : `toolUsePromptTokenCount` s'il est un entier > 0, sinon 0 ; lu sans contrôle de forme (le contrôle reste
    celui de la v3b, après la lecture de l'usage). Ne lève jamais."""
    v = usage.get("toolUsePromptTokenCount") if isinstance(usage, dict) else None
    return v if isinstance(v, int) and not isinstance(v, bool) and v > 0 else 0


def lire_recherche(rep, max_requetes, cle, outil_jetons=0):
    """Lit `candidates[0].groundingMetadata` ; ne lève jamais. Rend un dictionnaire : `requetes` (liste de chaînes),
    `sources` (liste de {"uri", "titre"}), `appuis` (nombre de `groundingSupports`), `facturees` (nombre de requêtes
    compté au coût), `origine` (d'où vient ce nombre) et `avertissements`. v3c (3) : `outil_jetons` (> 0) témoigne d'une
    recherche quand `webSearchQueries` est vide."""
    resultat = {"requetes": [], "sources": [], "appuis": 0, "facturees": max_requetes, "origine": None,
                "present": False, "avertissements": []}
    candidats = rep.get("candidates") if isinstance(rep, dict) else None
    c0 = candidats[0] if isinstance(candidats, list) and candidats and isinstance(candidats[0], dict) else {}
    gm = c0.get("groundingMetadata")
    if not isinstance(gm, dict):
        resultat["origine"] = "maximum_pire_cas (groundingMetadata absent)"
        resultat["avertissements"].append(
            f"recherche web demandée mais groundingMetadata absent de la réponse : aucune source rendue ; coût de recherche "
            f"compté au maximum du pire cas ({max_requetes} requêtes)")
        return resultat
    resultat["present"] = True
    requetes = gm.get("webSearchQueries")
    temoins = temoins_de_recherche(gm, outil_jetons)
    if isinstance(requetes, list) and not requetes and temoins:  # v3b (2) : une recherche a eu lieu, non listée
        resultat["origine"] = ("maximum_pire_cas (requêtes vides, jetons d'outil facturés)"  # v3c (3) : seul témoin
                               if temoins == ["toolUsePromptTokenCount"]
                               else "maximum_pire_cas (requêtes vides, sources présentes)")
        resultat["avertissements"].append(
            f"webSearchQueries vide alors que {', '.join(temoins)} ne le sont pas : coût de recherche compté au maximum "
            f"du pire cas ({max_requetes} requêtes)")
    elif isinstance(requetes, list) and all(isinstance(q, str) for q in requetes):
        resultat["facturees"] = len(requetes)
        resultat["origine"] = "webSearchQueries"
        resultat["requetes"] = [nettoyer_web(q, cle, LONGUEUR_MAX_TEXTE_WEB) for q in requetes[:NOMBRE_MAX_ELEMENTS_WEB]]
        if len(requetes) > NOMBRE_MAX_ELEMENTS_WEB:
            resultat["avertissements"].append(
                f"{len(requetes)} requêtes lues : {NOMBRE_MAX_ELEMENTS_WEB} listées, toutes comptées au coût")
    elif isinstance(requetes, list):  # v3c (2) : en partie illisible ; tout élément compte, jamais moins que le maximum
        lisibles = [q for q in requetes if isinstance(q, str) and q.strip()]
        illisibles = sum(not isinstance(q, str) for q in requetes)
        resultat["facturees"] = max(len(requetes), max_requetes)
        resultat["origine"] = "maximum_pire_cas ou longueur (webSearchQueries en partie illisible)"
        resultat["requetes"] = [nettoyer_web(q, cle, LONGUEUR_MAX_TEXTE_WEB) for q in lisibles[:NOMBRE_MAX_ELEMENTS_WEB]]
        resultat["avertissements"].append(
            f"webSearchQueries en partie illisible ({illisibles} élément(s) non chaîne sur {len(requetes)}) : coût de "
            f"recherche compté sur max(longueur {len(requetes)}, maximum du pire cas {max_requetes}) = "
            f"{resultat['facturees']} requêtes ; {min(len(lisibles), NOMBRE_MAX_ELEMENTS_WEB)} listée(s)")
    else:
        resultat["origine"] = "maximum_pire_cas (webSearchQueries absent ou illisible)"
        resultat["avertissements"].append(
            f"groundingMetadata sans webSearchQueries lisible ({type(requetes).__name__}) : coût de recherche compté au "
            f"maximum du pire cas ({max_requetes} requêtes)")
    morceaux = gm.get("groundingChunks")
    vues, autres, refusees, non_listees = set(), 0, 0, 0
    for m in morceaux if isinstance(morceaux, list) else []:
        web = m.get("web") if isinstance(m, dict) else None
        if not isinstance(web, dict) or not isinstance(web.get("uri"), str):
            autres += 1
            continue
        uri = nettoyer_web(web["uri"], cle)
        if uri in vues:
            continue
        if len(resultat["sources"]) >= NOMBRE_MAX_ELEMENTS_WEB:
            non_listees += 1
            continue
        vues.add(uri)
        permise, schema = adresse_permise(uri)  # v3b (7) : web seulement
        if not permise:
            refusees += 1
            uri = f"[adresse refusée : schéma {schema}]"
        titre = web.get("title")
        resultat["sources"].append({"uri": uri, "titre": nettoyer_web(titre, cle, LONGUEUR_MAX_TEXTE_WEB)
                                    if isinstance(titre, str) else ""})
    if autres:
        resultat["avertissements"].append(f"{autres} élément(s) de groundingChunks sans web.uri lisible : ignorés")
    if refusees:
        resultat["avertissements"].append(
            f"{refusees} adresse(s) de source refusée(s) (ni https:// ni http:// avec un hôte) : remplacées")
    if non_listees:
        resultat["avertissements"].append(
            f"{non_listees} source(s) au-delà des {NOMBRE_MAX_ELEMENTS_WEB} listées : non listées")
    appuis = gm.get("groundingSupports")
    resultat["appuis"] = len(appuis) if isinstance(appuis, list) else 0
    return resultat


def section_sources(recherche, prix_requete):
    """Section ajoutée au texte rendu au noyau (b) ; rend (texte, nombre de lignes coupées). v3b (8) : au plus
    LONGUEUR_MAX_SECTION caractères ; au-delà, les lignes suivantes sont remplacées par une ligne qui le dit."""
    lignes = ["", "", "---", TITRE_SOURCES, ""]
    if not recherche["present"]:
        lignes.append(f"Aucune métadonnée de recherche rendue par l'interface (groundingMetadata absent) : sources "
                      f"inconnues ; coût compté au maximum de {recherche['facturees']} requêtes à {prix_requete:g} USD.")
        return "\n".join(lignes), 0
    lignes.append("Requêtes :")
    lignes += [f"- « {q} »" for q in recherche["requetes"]] or ["- (aucune requête rendue)"]
    lignes += ["", "Sources :"]
    lignes += ([f"{i}. {s['titre'] or '(sans titre)'} — {s['uri']}" for i, s in enumerate(recherche["sources"], 1)]
               or ["- (aucune source rendue)"])
    gardees, longueur = [], 0
    for i, l in enumerate(lignes):
        if longueur + len(l) + 1 > LONGUEUR_MAX_SECTION:
            coupees = len(lignes) - i
            gardees.append(f"… (section coupée à {LONGUEUR_MAX_SECTION} caractères : {coupees} ligne(s) non reprise(s) ; "
                           "voir requetes_web et sources_web du JSON)")
            return "\n".join(gardees), coupees
        gardees.append(l)
        longueur += len(l) + 1
    return "\n".join(gardees), 0


class ErreurCommande(Exception):
    """Échec nommé : code de sortie, et ce qui a été envoyé ou non (pour le coût)."""

    def __init__(self, code, message, envoye=False, cout_origine="plancher"):
        super().__init__(message)
        self.code = code
        self.envoye = envoye
        self.cout_origine = cout_origine  # « plancher », « pire_cas » ou « usage »


class Interruption(Exception):
    """Délai global dépassé ou signal reçu."""


def masquer(texte, cle):
    """Ne laisse jamais passer la clé dans un message."""
    texte = str(texte)
    return texte.replace(cle, "[clé]") if cle else texte


def masquer_objet(objet, cle):
    """v3b (5a) : masque la clé dans toutes les chaînes d'un objet JSON (listes et dictionnaires, valeurs et clés)."""
    if not cle:
        return objet
    if isinstance(objet, str):
        return masquer(objet, cle)
    if isinstance(objet, list):
        return [masquer_objet(x, cle) for x in objet]
    if isinstance(objet, dict):
        return {masquer_objet(k, cle): masquer_objet(v, cle) for k, v in objet.items()}
    return objet


def echapper_separateurs(ligne_json):
    """v3b (6) : échappe U+2028, U+2029 et U+0085, où `str.splitlines()` coupe ; l'objet décodé reste identique."""
    return ligne_json.replace("\u2028", "\\u2028").replace("\u2029", "\\u2029").replace("\x85", "\\u0085")


def nombre_fini_positif(nom, valeur):
    try:
        v = float(valeur)
    except (TypeError, ValueError):
        raise ErreurCommande(REGLAGE, f"{nom} : nombre attendu (reçu {valeur!r})")
    if not math.isfinite(v) or v <= 0:
        raise ErreurCommande(REGLAGE, f"{nom} : réel fini strictement positif attendu (reçu {valeur!r})")
    return v


def nombre_fini_non_negatif(nom, valeur):
    """Rend la valeur en fraction exacte (aucun arrondi binaire dans la garde : 0,05 vaut 1/20)."""
    try:
        v = float(valeur)
    except (TypeError, ValueError):
        raise ErreurCommande(REGLAGE, f"{nom} : nombre attendu (reçu {valeur!r})")
    if not math.isfinite(v) or v < 0:
        raise ErreurCommande(REGLAGE, f"{nom} : réel fini positif ou nul attendu (reçu {valeur!r})")
    return Fraction(repr(v))


def valider_url_base(url):
    p = urllib.parse.urlparse(url)
    if p.scheme == "https" and p.hostname:
        return url.rstrip("/"), False
    if p.scheme == "http" and p.hostname in HOTES_LOCAUX:
        return url.rstrip("/"), True
    raise ErreurCommande(REGLAGE, f"--url-base : https, ou http vers la boucle locale seulement (reçu {url!r})")


def ouvreur(local):
    """Boucle locale : aucun mandataire. Sinon : mandataire et certificats de l'environnement."""
    if local:
        return urllib.request.build_opener(urllib.request.ProxyHandler({}))
    ca = os.environ.get("SSL_CERT_FILE")
    contexte = ssl.create_default_context(cafile=ca) if ca else ssl.create_default_context()
    return urllib.request.build_opener(urllib.request.HTTPSHandler(context=contexte))


def poster(ouv, url, cle, corps, delai_s):
    """POST JSON ; rend l'objet JSON. Lève HTTPError, URLError, OSError, ValueError."""
    requete = urllib.request.Request(url, data=json.dumps(corps, ensure_ascii=False).encode("utf-8"), method="POST",
                                     headers={"Content-Type": "application/json", "x-goog-api-key": cle})
    with ouv.open(requete, timeout=delai_s) as r:
        brut = r.read(TAILLE_MAX_REPONSE + 1)
    if len(brut) > TAILLE_MAX_REPONSE:
        raise ValueError("réponse trop longue")
    return json.loads(brut.decode("utf-8"))


def cout_usage(usage, prix_entree, prix_sortie):
    """(coût, détail) depuis `usageMetadata` ; lève ErreurCommande si l'usage est absent ou mal formé."""
    if not isinstance(usage, dict):
        raise ErreurCommande(NON_CONFORME, "usage absent de la réponse (usageMetadata) : pire cas compté",
                             envoye=True, cout_origine="pire_cas")
    def entier(nom, requis):
        v = usage.get(nom)
        if v is None and not requis:
            return 0
        if isinstance(v, bool) or not isinstance(v, int) or v < 0:
            raise ErreurCommande(NON_CONFORME, f"usage mal formé ({nom} = {v!r}) : pire cas compté",
                                 envoye=True, cout_origine="pire_cas")
        return v
    entree = entier("promptTokenCount", True)
    candidats = entier("candidatesTokenCount", False)
    pensees = entier("thoughtsTokenCount", False)
    # v3d (1a) : lu comme les autres champs facultatifs (mal formé : pire cas) ; absent : None, aucun écart compté
    total = entier("totalTokenCount", False) if usage.get("totalTokenCount") is not None else None
    sortie = candidats + pensees
    cout = entree * prix_entree / 1e6 + sortie * prix_sortie / 1e6
    return cout, {"entree": entree, "sortie": sortie, "candidats": candidats, "pensees": pensees, "total": total,
                  "brut": {k: usage[k] for k in sorted(usage) if isinstance(usage[k], (int, float))}}


def modele_conforme(demande, servi):
    return isinstance(servi, str) and (servi == demande or servi.startswith(demande + "-")
                                       or servi == "models/" + demande)


def lire_reponse(rep, modele, recherche_web=False):
    """(texte, fin, modèle servi) d'une réponse conforme ; lève ErreurCommande (code 5) sinon. L'usage est lu à part."""
    if not isinstance(rep, dict):
        raise ErreurCommande(NON_CONFORME, "réponse non JSON objet", envoye=True, cout_origine="pire_cas")
    bloque = (rep.get("promptFeedback") or {}).get("blockReason")
    if bloque:
        raise ErreurCommande(NON_CONFORME, f"consigne bloquée par l'interface ({bloque})", envoye=True, cout_origine="usage")
    servi = rep.get("modelVersion")
    if not modele_conforme(modele, servi):
        raise ErreurCommande(NON_CONFORME, f"modèle servi {servi!r} ≠ modèle demandé {modele!r} (aucun changement de "
                             "modèle sans GO)", envoye=True, cout_origine="usage")
    candidats = rep.get("candidates") or []
    if not candidats:
        raise ErreurCommande(NON_CONFORME, "aucun candidat dans la réponse (réponse vide)", envoye=True, cout_origine="usage")
    c = candidats[0]
    fin = c.get("finishReason")
    parts = (c.get("content") or {}).get("parts") or []
    interdites = sorted({k for p in parts if isinstance(p, dict) for k in PARTIES_INTERDITES if k in p})
    if interdites:  # v3b (4)
        declare = "seul google_search est déclaré" if recherche_web else "aucun outil n'est déclaré"
        raise ErreurCommande(NON_CONFORME, f"appel de fonction ou exécution de code dans la réponse "
                             f"({', '.join(interdites)}) alors que {declare}", envoye=True, cout_origine="usage")
    texte = "".join(p.get("text", "") for p in parts if isinstance(p, dict) and not p.get("thought"))
    if fin == "MAX_TOKENS":
        raise ErreurCommande(NON_CONFORME, "sortie tronquée (MAX_TOKENS) : maxOutputTokens atteint", envoye=True,
                             cout_origine="usage")
    if fin != "STOP":
        raise ErreurCommande(NON_CONFORME, f"fin de génération {fin!r} (bloquée ou anormale)", envoye=True,
                             cout_origine="usage")
    if not texte.strip():
        raise ErreurCommande(NON_CONFORME, "réponse vide (texte vide, fin STOP)", envoye=True, cout_origine="usage")
    return texte, fin, servi


def analyseur():
    a = argparse.ArgumentParser(prog="commande_argon_v3d", description="Appel à Argon (contrat du noyau v43/v44) : nu par "
                                "défaut, recherche Google sur option.")
    a.add_argument("--modele", default=MODELE_DEFAUT)
    a.add_argument("--url-base", default=URL_BASE_DEFAUT)
    a.add_argument("--prix-entree", default=PRIX_ENTREE_DEFAUT, help="USD par million de jetons d'entrée (8,3 : Lazar)")
    a.add_argument("--prix-sortie", default=PRIX_SORTIE_DEFAUT, help="USD par million de jetons de sortie (41,5 : SUPPOSÉ)")
    a.add_argument("--caracteres-par-jeton", default=CARACTERES_PAR_JETON_DEFAUT)
    a.add_argument("--max-sortie-jetons", type=int, default=MAX_SORTIE_JETONS_DEFAUT)
    a.add_argument("--sortie-min-jetons", type=int, default=SORTIE_MIN_JETONS_DEFAUT)
    a.add_argument("--provision-pensee-jetons", type=int, default=PROVISION_PENSEE_JETONS_DEFAUT,
                   help="jetons de pensée provisionnés au prix de sortie dans la garde, et thinkingBudget posé (CL44-02)")
    a.add_argument("--sans-config-pensee", dest="config_pensee", action="store_false", default=True,
                   help="ne pas poser generationConfig.thinkingConfig (la provision reste comptée dans la garde)")
    a.add_argument("--marge-entree", default=MARGE_ENTREE_DEFAUT,
                   help="marge relative sur l'entrée gardée (0,05 = 5 %%) (CL44-03)")
    a.add_argument("--compter-jetons", dest="compter_jetons", action="store_true", default=True,
                   help="compte exact de l'entrée par countTokens (gratuit) — défaut depuis la v2")
    a.add_argument("--sans-compter-jetons", dest="compter_jetons", action="store_false",
                   help="garder sur l'estimation par caractères seulement")
    a.add_argument("--delai-s", default=DELAI_DEFAUT_S, help="délai global de la commande, en secondes")
    a.add_argument("--recherche-web", action="store_true", default=False,
                   help="v3 : déclare l'outil google_search (et lui seul) ; sans elle, corps identique à la v2")
    a.add_argument("--prix-requete-web-usd", default=PRIX_REQUETE_WEB_DEFAUT,
                   help="v3 : USD par requête de recherche (0,05 : SUPPOSÉ, volontairement haut)")
    a.add_argument("--max-requetes-web-pire-cas", type=int, default=MAX_REQUETES_WEB_PIRE_CAS_DEFAUT,
                   help="v3 : requêtes de recherche comptées dans la garde avant envoi (au-delà, après coup : code 8)")
    a.add_argument("--provision-outil-jetons", type=int, default=PROVISION_OUTIL_JETONS_DEFAUT,
                   help="v3b : jetons d'outil (toolUsePromptTokenCount) provisionnés au prix d'entrée dans la garde, avec "
                        "--recherche-web seulement (32 768 : SUPPOSÉ ; au-delà, après coup : code 9)")
    return a


def executer(argv, entree_octets, environ):
    """Rend (code, objet de la dernière ligne, message d'erreur ou None). Ne lève jamais.
    Les avertissements (sans effet sur le code) sont dans `objet["avertissements"]`."""
    etat = {"envoye": False, "pire_cas_usd": None, "usage": None, "cle": None, "supplement_usd": 0.0}
    diag = {"version": VERSION, "role": environ.get("ROLE_POLE"), "modele_demande": None, "modele_servi": None,
            "fin": None, "envoye": False, "cout_origine": None, "pire_cas_usd": None, "max_sortie_jetons": None,
            "entree_jetons_estimee": None, "entree_jetons_comptee": None, "entree_jetons_garde": None,
            "marge_entree": None, "provision_pensee_jetons": None, "config_pensee": None, "pensees_jetons": None,
            "lecture_pensees": None, "usage": None, "avertissements": [], "erreur": None, "code": None,
            # v3 : champs de la recherche web (listes toujours présentes, vides sans --recherche-web)
            "requetes_web": [], "sources_web": [], "recherche_web": False, "requetes_web_facturees": None,
            "requetes_web_origine": None, "prix_requete_web_usd": None, "max_requetes_web_pire_cas": None,
            "cout_recherche_usd": None, "appuis_web": None, "outil_jetons": None,
            # v3b : provision des jetons d'outil (avec --recherche-web) ; supplément des requêtes lues au-delà du maximum
            "provision_outil_jetons": None, "supplement_recherche_usd": None,
            # v3c (1) : excédent de l'entrée facturée sur l'entrée gardée (les deux modes) ; part de la provision d'outil
            # consommée, excédent compris (avec --recherche-web seulement)
            "entree_excedent_jetons": None, "provision_outil_consommee_jetons": None,
            # v3d (1) : totalTokenCount lu, et son écart aux jetons comptés au coût
            "total_jetons": None, "ecart_total_jetons": None}

    def ligne(code, texte, cout, origine, erreur=None):
        diag.update(texte=texte, cout_usd=float(cout), cout_origine=origine, envoye=etat["envoye"], code=code,
                    erreur=masquer(erreur, etat["cle"]) if erreur else None, pire_cas_usd=etat["pire_cas_usd"])
        diag["avertissements"] = [masquer(a, etat["cle"]) for a in diag["avertissements"]]
        objet = {"texte": diag.pop("texte"), "cout_usd": diag.pop("cout_usd")}
        objet.update(diag)
        objet = masquer_objet(objet, etat["cle"])  # v3b (5a) : toutes les chaînes (modele_servi, fin, texte compris)
        return code, objet, objet["erreur"]

    def repli_pire_cas():
        """v3b (1) : pire cas avant envoi, plus les requêtes lues au-delà du maximum (0 tant que rien n'est lu) ; avec la
        recherche, jamais moins que le coût réel déjà lu sur l'usage (jetons d'outil au-delà de la provision). Sans la
        recherche, le supplément vaut 0 et le repli est celui de la v2."""
        repli = etat["pire_cas_usd"] + etat["supplement_usd"]
        if diag["recherche_web"] and etat["usage"] is not None:
            repli = max(repli, etat["usage"])
        return repli

    def sur_signal(num, _cadre):
        raise Interruption(f"signal {num} reçu")

    precedents = {}
    try:
        try:
            args = analyseur().parse_args(argv)
        except SystemExit:
            raise ErreurCommande(REGLAGE, "arguments refusés (voir la sortie d'erreur)")
        diag["modele_demande"] = args.modele
        prix_e = nombre_fini_positif("--prix-entree", args.prix_entree)
        prix_s = nombre_fini_positif("--prix-sortie", args.prix_sortie)
        cpj = nombre_fini_positif("--caracteres-par-jeton", args.caracteres_par_jeton)
        delai = nombre_fini_positif("--delai-s", args.delai_s)
        marge = nombre_fini_non_negatif("--marge-entree", args.marge_entree)
        if args.max_sortie_jetons < 1 or args.sortie_min_jetons < 1 or args.sortie_min_jetons > args.max_sortie_jetons:
            raise ErreurCommande(REGLAGE, "1 ≤ --sortie-min-jetons ≤ --max-sortie-jetons requis")
        provision = args.provision_pensee_jetons
        if provision < 0:
            raise ErreurCommande(REGLAGE, f"--provision-pensee-jetons : entier ≥ 0 requis (reçu {provision})")
        diag.update(marge_entree=float(marge), provision_pensee_jetons=provision, config_pensee=args.config_pensee)
        prix_req = nombre_fini_positif("--prix-requete-web-usd", args.prix_requete_web_usd)  # v3
        max_req = args.max_requetes_web_pire_cas
        if max_req < 1:
            raise ErreurCommande(REGLAGE, f"--max-requetes-web-pire-cas : entier ≥ 1 requis (reçu {max_req})")
        provision_outil = args.provision_outil_jetons  # v3b (3)
        if provision_outil < 0:
            raise ErreurCommande(REGLAGE, f"--provision-outil-jetons : entier ≥ 0 requis (reçu {provision_outil})")
        if args.recherche_web:
            diag.update(recherche_web=True, prix_requete_web_usd=prix_req, max_requetes_web_pire_cas=max_req,
                        provision_outil_jetons=provision_outil)
        url_base, local = valider_url_base(args.url_base)
        if "PLAFOND_SESSION_USD" not in environ:
            raise ErreurCommande(REGLAGE, "PLAFOND_SESSION_USD absent de l'environnement")
        plafond = nombre_fini_positif("PLAFOND_SESSION_USD", environ["PLAFOND_SESSION_USD"])
        role = environ.get("ROLE_POLE")
        if role not in ROLES:
            raise ErreurCommande(REGLAGE, f"ROLE_POLE ∉ {ROLES} (reçu {role!r})")
        cle = environ.get(VARIABLE_CLE) or ""
        etat["cle"] = cle or None
        if not cle.strip():
            raise ErreurCommande(REGLAGE, f"{VARIABLE_CLE} absente ou vide : l'enveloppe d'utilisateur distinct la pose")
        try:
            consigne = entree_octets.decode("utf-8")
        except UnicodeDecodeError:
            raise ErreurCommande(REGLAGE, "consigne : UTF-8 invalide sur l'entrée standard")
        if not consigne.strip():
            raise ErreurCommande(REGLAGE, "consigne vide sur l'entrée standard")

        for s in (signal.SIGALRM, signal.SIGTERM, signal.SIGINT):
            precedents[s] = signal.signal(s, sur_signal)
        signal.setitimer(signal.ITIMER_REAL, delai)

        ouv = ouvreur(local)
        contenus = [{"role": "user", "parts": [{"text": consigne}]}]
        estime = math.ceil(len(consigne) / cpj)
        diag["entree_jetons_estimee"] = estime
        entree_jetons = estime
        if args.compter_jetons:  # gratuit : aucune génération
            try:
                rep = poster(ouv, f"{url_base}/models/{args.modele}:countTokens", cle, {"contents": contenus}, delai)
            except urllib.error.HTTPError as e:
                raise ErreurCommande(INTERFACE, f"countTokens : HTTP {e.code} : "
                                     + e.read(300).decode("utf-8", "replace"))
            except (urllib.error.URLError, OSError, ValueError) as e:
                raise ErreurCommande(INTERFACE, f"countTokens : {type(e).__name__} : {e}")
            compte = rep.get("totalTokens") if isinstance(rep, dict) else None
            if isinstance(compte, bool) or not isinstance(compte, int) or compte <= 0:
                raise ErreurCommande(NON_CONFORME, f"countTokens : totalTokens absent ou invalide ({compte!r})")
            diag["entree_jetons_comptee"] = compte
            entree_jetons = max(estime, compte)
        entree_garde = math.ceil(entree_jetons * (1 + marge))  # CL44-03 : fraction exacte, aucun arrondi binaire
        diag["entree_jetons_garde"] = entree_garde
        cout_entree = entree_garde * prix_e / 1e6
        # v3 (c) : les requêtes de recherche du pire cas sont payées avant la provision de pensée et la sortie ;
        # sans --recherche-web, cout_recherche_max vaut 0.0 et la garde est exactement celle de la v2
        cout_recherche_max = max_req * prix_req if args.recherche_web else 0.0
        # v3b (3) : la provision des jetons d'outil, au prix d'entrée (SUPPOSÉ), payée avec les requêtes
        cout_outil_max = provision_outil * prix_e / 1e6 if args.recherche_web else 0.0
        cout_fixe = cout_entree + cout_recherche_max + cout_outil_max
        place = math.floor((plafond - cout_fixe) / (prix_s / 1e6)) if plafond > cout_fixe else 0
        max_sortie = min(args.max_sortie_jetons, place - provision)  # CL44-02 : la provision est réservée d'abord
        pire_min = cout_fixe + (args.sortie_min_jetons + provision) * prix_s / 1e6
        if max_sortie < args.sortie_min_jetons:
            recherche = (f" ; plus {max_req} requêtes de recherche à {prix_req:g} USD et {provision_outil} jetons d'outil "
                         f"provisionnés à {prix_e:g}" if args.recherche_web else "")
            raise ErreurCommande(PIRE_CAS, f"pire cas {pire_min:.4f} USD (entrée gardée {entree_garde} jetons, marge "
                                 f"{float(marge):g} comprise, à {prix_e:g} ; plus {args.sortie_min_jetons} jetons de sortie "
                                 f"et {provision} jetons de pensée provisionnés à {prix_s:g}{recherche}) > plafond de "
                                 f"session {plafond:g} USD : rien envoyé")
        diag["max_sortie_jetons"] = max_sortie
        etat["pire_cas_usd"] = round(cout_fixe + (max_sortie + provision) * prix_s / 1e6, 6)

        config = {"maxOutputTokens": max_sortie}
        if args.config_pensee:  # CL44-02 : budget de pensée posé ; un refus de l'interface remonte tel quel (R5)
            config["thinkingConfig"] = {"thinkingBudget": provision}
        corps = {"contents": contenus, "generationConfig": config}  # ni outil, ni fonction
        if args.recherche_web:  # v3 (a, d) : le seul outil permis, et rien d'autre (ni toolConfig, ni fonction)
            corps["tools"] = outil_recherche()
        try:
            etat["envoye"] = True
            rep = poster(ouv, f"{url_base}/models/{args.modele}:generateContent", cle, corps, delai)
        except urllib.error.HTTPError as e:
            detail = e.read(300).decode("utf-8", "replace")
            pose = (f" (thinkingConfig.thinkingBudget = {provision} posé ; aucun repli : relancer avec "
                    "--sans-config-pensee est une décision)") if args.config_pensee else ""
            if args.recherche_web:
                pose += (" (outil google_search déclaré ; aucun repli : relancer sans --recherche-web est une "
                         "décision)")
            if 400 <= e.code < 500:  # refusée avant génération : non facturée (SUPPOSÉ)
                raise ErreurCommande(INTERFACE, f"HTTP {e.code} : {detail}{pose}", envoye=True, cout_origine="plancher")
            raise ErreurCommande(INTERFACE, f"HTTP {e.code} : {detail}", envoye=True, cout_origine="pire_cas")
        except urllib.error.URLError as e:
            refus = isinstance(e.reason, (ConnectionRefusedError, socket.gaierror))
            if refus:
                etat["envoye"] = False
            raise ErreurCommande(INTERFACE, f"connexion : {type(e.reason).__name__} : {e.reason}", envoye=not refus,
                                 cout_origine="plancher" if refus else "pire_cas")
        except (OSError, ValueError) as e:  # délai de socket, coupure, JSON illisible : peut-être facturé
            raise ErreurCommande(INTERFACE if isinstance(e, OSError) else NON_CONFORME,
                                 f"{type(e).__name__} : {e}", envoye=True, cout_origine="pire_cas")
        signal.setitimer(signal.ITIMER_REAL, 0)
        usage = rep.get("usageMetadata") if isinstance(rep, dict) else None
        diag["modele_servi"] = rep.get("modelVersion") if isinstance(rep, dict) else None
        recherche = None
        if args.recherche_web:  # v3 (b) : lu avant tout contrôle, pour que le journal le porte aussi sur un échec
            recherche = lire_recherche(rep, max_req, cle, temoin_outil(usage))  # v3c (3) : jetons d'outil, témoin
            diag.update(requetes_web=recherche["requetes"], sources_web=recherche["sources"],
                        requetes_web_facturees=recherche["facturees"], requetes_web_origine=recherche["origine"],
                        appuis_web=recherche["appuis"])
            diag["avertissements"].extend(recherche["avertissements"])
            # v3b (1) : les requêtes lues au-delà du maximum s'ajoutent à tout repli au pire cas
            etat["supplement_usd"] = max(0, recherche["facturees"] - max_req) * prix_req
            diag["supplement_recherche_usd"] = round(etat["supplement_usd"], 6)
        hors_max = recherche is not None and recherche["facturees"] > max_req

        def usage_illisible(e):
            """v3b (1) : usage illisible et requêtes au-delà du maximum → code 8 (pire cas plus supplément), pas 5."""
            if not hors_max:
                return e
            return ErreurCommande(REQUETES_WEB_HORS_PIRE_CAS,
                                  f"requêtes de recherche au-delà du pire cas : {recherche['facturees']} lues dans "
                                  f"webSearchQueries > --max-requetes-web-pire-cas {max_req}, et {e} ; coût compté : pire "
                                  f"cas {etat['pire_cas_usd']:.6f} USD plus {recherche['facturees'] - max_req} requêtes à "
                                  f"{prix_req:g} USD ; la garde du plafond ne tient plus : arrêter et lire avant toute "
                                  "dépense de plus", envoye=True, cout_origine="pire_cas")

        try:
            cout, detail_usage = cout_usage(usage, prix_e, prix_s)  # lève (pire cas) si l'usage manque
        except ErreurCommande as e:
            raise usage_illisible(e)
        # v3d (1) : le total a son propre champ (total_jetons) ; le détail rendu reste celui de la v2
        diag["usage"] = {k: v for k, v in detail_usage.items() if k != "total"}
        outil = 0
        # v3c (1a) : le même coût, en fractions exactes, pour la seule comparaison au plafond (jamais rendu)
        cout_exact = (detail_usage["entree"] * exact(prix_e) + detail_usage["sortie"] * exact(prix_s)) / 10**6
        if args.recherche_web:  # v3 (c) : jetons de l'outil au prix d'entrée (SUPPOSÉ), requêtes au prix par requête
            outil = usage.get("toolUsePromptTokenCount")
            if outil is None:
                outil = 0
            elif isinstance(outil, bool) or not isinstance(outil, int) or outil < 0:
                raise usage_illisible(ErreurCommande(
                    NON_CONFORME, f"usage mal formé (toolUsePromptTokenCount = {outil!r}) : pire cas compté",
                    envoye=True, cout_origine="pire_cas"))
            diag["outil_jetons"] = outil
            cout_recherche = recherche["facturees"] * prix_req
            diag["cout_recherche_usd"] = round(cout_recherche, 6)
            cout = cout + outil * prix_e / 1e6 + cout_recherche
            cout_exact += outil * exact(prix_e) / 10**6 + recherche["facturees"] * exact(prix_req)
            if outil:
                diag["avertissements"].append(
                    f"jetons d'outil (toolUsePromptTokenCount) {outil} comptés au prix d'entrée ({outil * prix_e / 1e6:.6f} "
                    f"USD) ; provision {provision_outil}")
        # v3d (1b, 1c, 1e) : totalTokenCount au-delà des jetons comptés (outil compris avec la recherche seulement) :
        # l'écart est compté au prix de sortie (prudent), dans le coût rendu et dans la comparaison exacte au plafond
        total = detail_usage["total"]
        comptes = detail_usage["entree"] + detail_usage["sortie"] + outil
        ecart = None if total is None else total - comptes
        ecart_compte = max(0, ecart or 0)
        diag.update(total_jetons=total, ecart_total_jetons=ecart)
        if ecart_compte:
            cout += ecart_compte * prix_s / 1e6
            cout_exact += ecart_compte * exact(prix_s) / 10**6
            diag["avertissements"].append(
                f"usage incohérent : totalTokenCount {total} > jetons comptés {comptes} (entrée {detail_usage['entree']}, "
                f"sortie {detail_usage['sortie']}" + (f", outil {outil}" if args.recherche_web else "") + f") ; écart "
                f"{ecart_compte} jetons compté au prix de sortie ({ecart_compte * prix_s / 1e6:.6f} USD)")
        elif ecart is not None and ecart < 0:
            diag["avertissements"].append(
                f"totalTokenCount {total} < jetons comptés {comptes} : la somme des champs, plus grande, est comptée")
        hors_plafond = cout_exact > exact(plafond)  # v3c (1a) : avec ou sans recherche, comparaison exacte
        if hors_plafond:
            diag["avertissements"].append(f"coût réel {cout:.6f} USD > plafond de session {plafond:g} USD")
        etat["usage"] = cout
        if not (math.isfinite(cout) and cout > 0):
            raise ErreurCommande(NON_CONFORME, f"coût calculé sur l'usage non strictement positif ({cout!r})",
                                 envoye=True, cout_origine="pire_cas")
        candidats = rep.get("candidates") or []
        diag["fin"] = candidats[0].get("finishReason") if candidats and isinstance(candidats[0], dict) else None
        pensees = detail_usage["pensees"]
        diag["pensees_jetons"] = pensees
        diag["lecture_pensees"] = ("hors_max_sortie" if detail_usage["candidats"] + pensees > max_sortie
                                   else "indetermine")
        excedent = max(0, detail_usage["entree"] - entree_garde)  # v3c (1) : entrée facturée au-delà de l'entrée gardée
        diag["entree_excedent_jetons"] = excedent
        consommee = excedent + outil + ecart_compte  # v3c (1b), v3d (1c) : payés par la même provision
        if args.recherche_web:
            diag["provision_outil_consommee_jetons"] = consommee
        if excedent:  # CL44-03 : dit ; v3c : au-delà du plafond, code 10 (1a) ; avec la recherche, code 9 au-delà (1b)
            diag["avertissements"].append(
                f"entrée facturée {detail_usage['entree']} jetons > entrée gardée {entree_garde} (marge "
                f"{float(marge):g} comprise) : le plafond peut être dépassé de {(detail_usage['entree'] - entree_garde) * prix_e / 1e6:.6f} USD"
                + (f" ; avec --recherche-web, compté contre la provision d'outil : excédent {excedent} + jetons d'outil "
                   f"{outil} = {consommee} jetons, provision {provision_outil}" if args.recherche_web else ""))
        if pensees > provision:  # CL44-02 : la garde ne tient plus ; échec nommé, coût réel compté
            raise ErreurCommande(PENSEES_HORS_PROVISION,
                                 f"pensées au-delà de la provision : thoughtsTokenCount {pensees} > provision {provision} "
                                 f"jetons (thinkingConfig {'posé' if args.config_pensee else 'non posé'}) ; coût réel "
                                 f"{cout:.6f} USD compté sur l'usage, plafond de session {plafond:g} USD ; la garde du "
                                 "plafond ne tient plus : arrêter et lire avant toute dépense de plus",
                                 envoye=True, cout_origine="usage")
        if recherche is not None and recherche["facturees"] > max_req:  # v3 (c) : la garde ne tient plus ; échec nommé
            raise ErreurCommande(REQUETES_WEB_HORS_PIRE_CAS,
                                 f"requêtes de recherche au-delà du pire cas : {recherche['facturees']} lues dans "
                                 f"webSearchQueries > --max-requetes-web-pire-cas {max_req} ; coût réel {cout:.6f} USD "
                                 f"compté (toutes les requêtes lues à {prix_req:g} USD), plafond de session {plafond:g} "
                                 "USD ; la garde du plafond ne tient plus : arrêter et lire avant toute dépense de plus",
                                 envoye=True, cout_origine="usage")
        if args.recherche_web and consommee > provision_outil:  # v3b (3), v3c (1b) : excédent d'entrée compris
            raise ErreurCommande(JETONS_OUTIL_HORS_PROVISION,
                                 f"jetons d'outil au-delà de la provision : toolUsePromptTokenCount {outil} + entrée "
                                 f"facturée au-delà de l'entrée gardée {excedent} ({detail_usage['entree']} − "
                                 f"{entree_garde}) + écart de totalTokenCount {ecart_compte} = {consommee} > "
                                 f"--provision-outil-jetons {provision_outil} ; coût réel "
                                 f"{cout:.6f} USD compté sur l'usage, plafond de session {plafond:g} USD"
                                 f"{' (dépassé)' if hors_plafond else ''} ; la garde du plafond ne tient plus : arrêter et "
                                 "lire avant toute dépense de plus", envoye=True, cout_origine="usage")
        if hors_plafond:  # v3c (1a) : jamais un succès ; échec nommé, coût réel compté ; prime sur le code 5
            recherche_txt = (f", jetons d'outil {outil}, {recherche['facturees']} requêtes à {prix_req:g} USD"
                             if recherche is not None else "")
            raise ErreurCommande(COUT_HORS_PLAFOND,
                                 f"coût au-delà du plafond de session : coût réel {cout:.6f} USD calculé sur l'usage "
                                 f"(entrée facturée {detail_usage['entree']} jetons dont {excedent} au-delà de l'entrée "
                                 f"gardée {entree_garde}, sortie {detail_usage['sortie']} jetons{recherche_txt}, écart de "
                                 f"totalTokenCount {ecart_compte} jetons au prix de sortie) > "
                                 f"PLAFOND_SESSION_USD {plafond:g} USD ; texte non rendu ; la garde du plafond ne tient "
                                 "plus : arrêter et lire avant toute dépense de plus", envoye=True, cout_origine="usage")
        if ecart_compte:  # v3d (1d) : jamais un succès ; échec nommé, coût réel (écart compris) ; prime sur le code 5
            raise ErreurCommande(USAGE_INCOHERENT,
                                 f"usage incohérent : totalTokenCount {total} > jetons comptés au coût {comptes} ; écart "
                                 f"{ecart_compte} jetons compté au prix de sortie {prix_s:g} ; coût réel {cout:.6f} USD "
                                 f"compté sur l'usage, plafond de session {plafond:g} USD ; texte non rendu ; l'usage ne se "
                                 "lit plus comme le suppose la garde : arrêter et lire avant toute dépense de plus",
                                 envoye=True, cout_origine="usage")
        texte, fin, servi = lire_reponse(rep, args.modele, args.recherche_web)
        if recherche is not None:  # v3 (b) : la section des sources suit le texte rendu au noyau
            section, coupees = section_sources(recherche, prix_req)
            if coupees:
                diag["avertissements"].append(f"section des sources coupée à {LONGUEUR_MAX_SECTION} caractères "
                                              f"({coupees} ligne(s) non reprise(s) dans le texte)")
            texte = texte + section
        return ligne(OK, texte, cout, "usage")
    except ErreurCommande as e:
        signal.setitimer(signal.ITIMER_REAL, 0)
        if e.cout_origine == "usage" and etat["usage"] is not None:
            cout, origine = etat["usage"], "usage"
        elif e.cout_origine in ("usage", "pire_cas") and e.envoye and etat["pire_cas_usd"]:
            cout, origine = repli_pire_cas(), "pire_cas"  # v3b (1) : plus les requêtes lues au-delà du maximum
        else:
            cout, origine = COUT_PLANCHER_USD, "plancher"
        etat["envoye"] = etat["envoye"] and e.envoye
        return ligne(e.code, "", cout, origine, f"{type(e).__name__} : {e}")
    except Interruption as e:
        signal.setitimer(signal.ITIMER_REAL, 0)
        if etat["envoye"] and etat["pire_cas_usd"]:
            cout, origine = repli_pire_cas(), "pire_cas"
        else:
            cout, origine = COUT_PLANCHER_USD, "plancher"
        return ligne(DELAI, "", cout, origine, f"délai ou interruption : {e}")
    except Exception as e:  # noqa: BLE001 — jamais de sortie sans ligne JSON ; nommé
        signal.setitimer(signal.ITIMER_REAL, 0)
        cout, origine = ((repli_pire_cas(), "pire_cas") if etat["envoye"] and etat["pire_cas_usd"]
                         else (COUT_PLANCHER_USD, "plancher"))
        return ligne(NON_CONFORME if etat["envoye"] else REGLAGE, "", cout, origine,
                     f"erreur inattendue {type(e).__name__} : {e}")
    finally:
        for s, h in precedents.items():
            try:
                signal.signal(s, h)
            except (ValueError, OSError):
                pass


def principal(argv=None):
    code, objet, erreur = executer(sys.argv[1:] if argv is None else argv, sys.stdin.buffer.read(), os.environ)
    if erreur:  # d'abord : l'adaptateur ne garde que les 300 premiers caractères de la sortie d'erreur
        print(f"commande_argon_v3d : {erreur}", file=sys.stderr)
    for a in objet.get("avertissements") or []:
        print(f"commande_argon_v3d : avertissement : {a}", file=sys.stderr)
    # v3b (6) : U+2028, U+2029 et U+0085 échappés, pour que str.splitlines() de l'adaptateur ne coupe pas la ligne
    sys.stdout.write(echapper_separateurs(json.dumps(objet, ensure_ascii=False)) + "\n")
    sys.stdout.flush()
    return code


if __name__ == "__main__":
    sys.exit(principal())
