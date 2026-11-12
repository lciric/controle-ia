# Contre-lecture du différentiel — ordre de la course de confirmation 7b de T0.6, brouillon 5 (depuis le brouillon 3) — v1

- **Qui** : contre-lecteur neuf, sous-agent de la session mère, **Claude Fable 5.2** (`claude-fable-5-2`, d'après ce qu'il sait de lui). Il n'a écrit aucun brouillon de cet ordre, ni la contre-lecture du brouillon 3, ni le préenregistrement de T0.6, ni sa chaîne.
- **Quand** (`date -u`, 11 novembre 2026) : début 07:34:41 UTC ; dernières commandes 07:40:57 UTC ; heure de scellement : réponse à la mère.
- **Dépôt** : `main`, tête locale `eaeb201e` au début, `9a93f134` à 07:40 UTC (égale à `origin/main` local ; la mère committe pendant la lecture). Écritures dans le dépôt : ce fichier et son compagnon, rien d'autre ; aucun commit, aucune poussée, aucun `git fetch`.
- **Objets** (chaque empreinte vérifiée par `sha256sum -c` dans `docs/procedures/`, toutes « OK ») : brouillon 3 (`eae1e64f…`) et sa contre-lecture (`f738d855…`) ; brouillon 4 (`5f2167d7…`), couples (`769ea60e…`), script (`fb685237…`), journal (`3efee1a8…`) ; brouillon 5 (`876f85e831cfd657a74d7b18deb8b6817324a137cc67ecf69d68ef8352e65dc7`) et son script (`4d42f8ac…`).
- **Interdits** de la consigne tenus ; gestes à déclarer : § 5.

## 1. Verdict

**Pas encore scellable tel quel : trois corrections à faire par couples (CL5-1, CL5-2, CL5-3), quatre mineurs (CL5-4 à CL5-7). Aucun bloquant.** Une fois ces couples appliqués, l'ordre est **scellable dès que `COMMIT_MAIN_REMISE` est rempli**.

- Les deux scripts rejoués rendent les deux textes **à l'octet**.
- Les 59 couples du brouillon 4 appliquent B1, C1 à C9 et M1 à M14 **fidèlement et complètement** ; je n'y trouve aucune faille neuve de sécurité, d'embargo ni de dépense.
- Les deux marqueurs du brouillon 5 ont les bonnes valeurs.
- Les gardes du § 4.3 rejouées sur `main` atteignent tous les attendus du texte.
- Les gardes du § 4.6, rejouées pour la première fois : cas sain conforme, artefact bien refusé (code 1), **mais la commande de l'ordre n'affiche pas le message de refus attendu** (CL5-1).
- Calendrier, fenêtre, minuterie et liste d'arrêt scellée concordent.
- Le procédé de `COMMIT_MAIN_REMISE` est sain dans sa mécanique ; sa définition écrite est fragile (CL5-3).

## 2. Constats

### À corriger (couples sur le brouillon 5 ; chaque « ancien » y est présent exactement une fois, compté)

**CL5-1 — § 4.6 : la commande de l'artefact masque le refus qu'elle doit montrer.**
Rejoué : `"$PY" -I -B -c "$G" 2>&1 | tail -n 3` sur la tête de `main` rend le code 1, mais ses trois dernières lignes sont `exiger_code_importe_sous passe`, `exiger_citations_t06 …`, `exiger_prereg_scelle ef31feff…`. La sortie standard, mise en tampon dans un tube, sort après la trace d'erreur : le message « arbre gelé … modifié depuis le commit cité 1609a4bf2c15 » n'est jamais affiché. La fille ne peut pas constater l'attendu du texte ; un refus pour une autre cause aurait la même apparence. Avec `-u`, les trois dernières lignes sont les deux lignes du `raise` puis `controle_ia.gardes.GardeArret: arbre gelé (code, tests, scripts, dépendances, configuration) modifié depuis le commit cité 1609a4bf2c15` (rejoué). Le défaut date des brouillons 1 à 3 ; il échoue du côté sûr (rien n'est créé), mais coûterait un arrêt et un aller-retour avant le 15.

- Ancien → `cd "$M" && "$PY" -I -B -c "$G" 2>&1 | tail -n 3;`
  Nouveau → `cd "$M" && "$PY" -I -B -u -c "$G" 2>&1 | tail -n 3;`
- Ancien → `**Artefact** (R5), code 1 : mêmes lignes, puis « `
  Nouveau → `**Artefact** (R5), code 1 : en dernière des trois lignes affichées, « `
- Ancien → `(refus observé par le rédacteur des brouillons 1 à 3, non rejoué au brouillon 4)`
  Nouveau → `(`-u` : sans lui, la sortie mise en tampon masque ce message ; cas sain et artefact rejoués hors ligne par la contre-lecture du brouillon 5, CL5-1)`

**CL5-2 — le titre et le statut disent encore « brouillon 4 », « Non contre-lu dans cette forme ».**
Le script du brouillon 5 ne change volontairement aucun autre octet ; un ordre scellé ne peut pas porter ces deux phrases, fausses à la remise.

- Ancien → `— v1, brouillon 4` (titre, première ligne)
  Nouveau → `— v1`
- Ancien → `- **Statut** : brouillon 4, écrit le`
  Nouveau → `- **Statut** : ordre v1 à sceller ; texte du brouillon 4, écrit le`
- Ancien → `**Non contre-lu dans cette forme** ; avant la remise : marqueurs dans l'ordre du § 14, scellement, commit, remise par Lazar ; contre-lecture du brouillon 4 (au moins du différentiel) si la mère la commande.`
  Nouveau → `Marqueurs de la mère remplis au brouillon 5 (`876f85e8…`, R-2324, R-2325). **Différentiel depuis le brouillon 3 contre-lu** par un lecteur neuf (`…-brouillon5-contre-lecture-v1.md`, Claude Fable 5.2), ses corrections CL5-1 à CL5-7 appliquées par couples ; reste avant la remise : `COMMIT_MAIN_REMISE`, scellement, commit, remise par Lazar.`

**CL5-3 — `COMMIT_MAIN_REMISE` : « parent » et « au commit de l'engagement » se contredisent, et « parent » peut devenir faux après le scellement.**
Le § 14 dit à la fois « **parent** du commit qui ajoute cet ordre scellé » et « la mère, au commit de l'engagement ». Le commit de l'engagement est `79e50d01c` ; depuis, `main` a reçu `eaeb201e`, `a74d082f`, `9a93f134` : il n'est plus le parent de rien d'utile. De plus la tête de `main` a bougé deux fois pendant ma lecture (fusions d'autres sessions) : un commit qui s'intercale entre le remplissage du marqueur et le commit de l'ordre rend « parent » faux dans un texte déjà scellé, qu'on ne réécrit pas (R12). La garde, elle, ne demande qu'un **ancêtre** (`merge-base --is-ancestor`, § 4.1) et reste juste dans tous ces cas.

- Ancien → `**parent** du commit qui ajoute cet ordre scellé ; l'ordre lui-même se vérifie par son compagnon et par l'empreinte du message de remise (§ 4.1) ; la mère, au commit de l'engagement (C3)`
  Nouveau → `**ancêtre** du commit qui ajoute cet ordre scellé : la tête de `main` relevée par la mère au moment du scellement (quarante caractères), déjà poussée, descendante du commit de l'engagement ; c'est le parent de ce commit si rien ne s'intercale ; l'ordre lui-même se vérifie par son compagnon et par l'empreinte du message de remise (§ 4.1) ; la mère, au scellement (C3, CL5-3)`
- Procédé conseillé à la mère (hors du texte) : relever `git rev-parse HEAD` (quarante caractères) et vérifier qu'il égale `origin/main` ; remplir ; sceller ; committer l'ordre ; vérifier `git merge-base --is-ancestor <valeur> HEAD` ; pousser ; alors seulement la remise.

### Mineurs

- **CL5-4** — § 14 : la table dit encore `LIGNE_SCELLEMENT_T07` « non remplissable le 10 novembre », et rien ne dit ce que le brouillon 5 a rempli.
  Ancien → `; non remplissable le 10 novembre (le registre ne porte que les lignes des jeux J-D et J-A)` Nouveau → `; remplie le 11 novembre (R-2321, R-2325)`.
  Ancien → `**Remplis au brouillon 4** (registres` Nouveau → `**Remplis au brouillon 5** (11 novembre, R-2324, R-2325) : `LIGNE_SCELLEMENT_T07` = la ligne du registre, à l'octet ; `ID_SESSION_FILLE` = valeur de repli (session non ouverte au scellement). **Remplis au brouillon 4** (registres`.
- **CL5-5** — `ID_SESSION_FILLE` en valeur de repli : le bloc du § 4.0 garde le gabarit `j "session <identifiant de la session fille>"`, que la fille doit remplacer à la main, sans que l'ordre dise d'où elle tient son identifiant ; l'en-tête ne le porte plus.
  Ancien → `en tête du journal, l'identifiant de la session (égal à celui de l'en-tête quand la mère l'y a écrit)` Nouveau → `en tête du journal, l'identifiant de la session, que la fille met à la place du gabarit `<identifiant de la session fille>` avant de jouer le bloc (elle le tient du message de remise de Lazar ou de son outil de session, jamais de `env` ; l'en-tête ne le porte pas : session ouverte après le scellement)`.
  Ancien → `- **La fille nommée en en-tête** exécute` Nouveau → `- **La fille désignée en en-tête** (celle à qui Lazar remet l'ordre) exécute`.
- **CL5-6** — § 4.13, écart sur les données : « destruction sur un mot de Lazar […], au plus tard le 16 à 23:00Z » ne dit pas ce que fait la fille sans mot à cette heure. R-2113 tranche (« attente du mot de Lazar avant destruction (borne du 16 à 23:00Z gardée) ») : l'écrire.
  Ancien → `(R-2113), au plus tard le 16 à 23:00Z.` Nouveau → `(R-2113) ; sans mot le 16 à 23:00Z, la borne joue : destruction, et le compte rendu nomme les données non poussées perdues avec l'instance.`
- **CL5-7** — rappel pour la remise, sans couple : le message de remise de Lazar doit donner le **chemin** et l'empreinte de l'ordre scellé (le § 4.1 dit « le compagnon de cet ordre » sans le nommer, et le nom change au scellement) ; la fille doit être active le 17 novembre à 01:15 UTC si le run vit encore le 16 à 23:00 UTC.

## 3. Ce qui a été vérifié

### (1) Scripts rejoués (bac à sable, hors du dépôt)

- Script du brouillon 4 sur une copie du brouillon 3 et des couples : code 0, « TOUT PASSE » (59 couples, chacun présent une fois ; 18 blocs `bash -n` ; 7 extraits Python ; 56 phrases exigées ; essais M10, M9, C5, M1, C1, C6, C8, M4 conformes) ; texte produit **identique à l'octet** (`cmp`) au brouillon 4 du dépôt, `5f2167d7…`.
- Script du brouillon 5 sur une copie du brouillon 4 et du registre des scellements : code 0 ; texte **identique à l'octet** au brouillon 5 du dépôt, `876f85e8…`. `diff` du brouillon 4 au brouillon 5 : deux lignes, l. 7 et l. 130, rien d'autre.

### (2) Les 59 couples contre la contre-lecture du brouillon 3

Tous lus un à un, anciens et nouveaux.

| Constat | Couples | Jugement |
|---|---|---|
| B1 | 44, 52, 57 | fidèle ; précision ajoutée « arrêtée après cette heure : aussitôt le rapatriement fait » juste ; 2 400 s et 1 800 s vérifiés (amorce l. 78 et 71), minuterie l. 101 à 126 exacte |
| C1 | 06, 07, 08, 34, 36, 37, 38 | fidèle, au caractère près ; le compagnon de `resume.json` a bien la forme « empreinte, deux espaces, nom » (`scellement.py`) ; `ligne_B` et `ligne_C` à la l. 330 de `lanceur_v6.py` |
| C2 | 12, 21, 22, 50, 51, 58, 59 | fidèle ; addendum et compagnon à `1a372523…` vérifiés sur `main`, ligne R-2092 une fois |
| C3 | 02, 09, 59 | appliqué comme demandé ; la formule demandée elle-même est fragile : CL5-3 |
| C4 | 41, 43, 53 | fidèle ; restent « copie à la mère » aux § 5 et § 6, lisibles par le canal du § 9 ; CL5-6 |
| C5 | 15, 29, 30, 33, 35, 45, 46, 49, 54 | fidèle et rendu mécanique (`nI = 1` avant `stop`, `destroy`, `show instance`) ; identifiant vide ou non numérique : aucun geste (0 ligne à l'inventaire), et la surveillance est refusée par le lanceur (l. 262 à 264) ; conséquence au code 4 juste |
| C6 | 38, 39 | fidèle ; motifs égaux à `MOTIF_INTERDIT` (amorce l. 300) |
| C7 | 03, 42 | fidèle |
| C8 | 40, 41 | fidèle ; forme de la ligne `PROGRES <instant> etape=episodes-ecrits … morceaux=N` conforme au code (`lanceur.py` l. 76 à 77, `lanceur_v6.py` l. 299) ; « ERREUR DE CHAÎNE (C11) » est bien le texte de l'amorce (l. 313) |
| C9 | 05, 56, 57 | fidèle ; GO-2026-11-10-06 : une ligne au registre |
| M1 à M14 | 04, 10, 11, 13, 14, 16 à 20, 24 à 28, 31, 32, 47, 48, 55 | fidèles ; M2 sans attente dans le bloc (déclaré au journal, acceptable) ; M3 chiffres refaits justes ; M4 : dix minutes mesurées sur la date du fichier, que le § 4.9 ne modifie pas |
| cohérence | 01, 02, 15, 23, 29, 49, 58, 59 | sans effet sur les gardes ; 01, 02 et 23 sont à reprendre (CL5-1, CL5-2) |

Seule baisse d'un jeton de garde : le commentaire « jamais un autre identifiant », remplacé par une condition mécanique plus forte.

### (3) Marqueurs du brouillon 5

- `LIGNE_SCELLEMENT_T07` : la ligne du texte est **égale à l'octet** à celle de `registres/scellements-v1.md` (fichier de travail et `HEAD`, même empreinte de ligne) ; une seule ligne au registre ; elle ne porte ni apostrophe ni caractère qui casserait la comparaison entre apostrophes du § 4.3. Chemin `prereg/T0.7-sondes-v0-v1.md`, empreinte `d7d180ec…` égale au fichier et à son compagnon sur `main` ; conforme à R-2321.
- `ID_SESSION_FILLE` : valeur de repli du § 14 (« à laquelle Lazar remet cet ordre »), avec une parenthèse explicative ajoutée ; conforme à la règle (session non ouverte). Suites : CL5-5.
- Reste un seul marqueur, `<<COMMIT_MAIN_REMISE>>`, une occurrence (§ 4.1).

### (4) Gardes du § 4.3 rejouées hors ligne

Jouées deux fois : sur `git show HEAD:registres/…`, puis telles quelles dans un clone à extraction partielle fait avec les motifs du § 4.1 (tête `9a93f134`, 07:40:57 UTC). Sorties, dans l'ordre : une ligne pour chacun des quatre GO ; `0` révocation ; `1` ligne `SCELLEMENT-T07` ; « ligne SCELLEMENT-T07 = celle de la remise » ; « T0.7 scellé : prereg/T0.7-sondes-v0-v1.md d7d180ec… » ; `1` ligne d'engagement ; `0` ligne de dépense hors de l'engagement ; `1` ligne R-2092 ; « addendum v3 du bras B scellé ». **Tous les attendus sont atteints.** La ligne d'engagement du registre et la citation du § 6 portent, aux retours à la ligne près, le texte de la section « Devis » du texte scellé (l. 705 à 709).

### (5) Gardes du § 4.6 et autres rejeux sans instance

- Deux clones locaux (`--shared`, branche `main` seule, sans extraction, puis extraction partielle par les 37 motifs du § 4.1) : aucun chemin interdit extrait (compté : 0 partout). Limite : clone du dépôt local et non du dépôt distant ; six fichiers de `registres/` et de `docs/` au commit S n'ont pas pu être extraits (objets absents du dépôt local), aucun dans l'arbre gelé.
- **Cas sain** (tête S) : code 0, les sept lignes attendues, valeurs égales au texte (`b7a5c1ba…`, `76cdeace…`, `8d20a698…`, `31538212097275005629337336542801867913`, `ef31feff…`, `1609a4bf2c15…`).
- **Artefact** (tête de `main`) : code 1, refus par `exiger_code_cite` ; message non affiché par la commande de l'ordre : **CL5-1**.
- § 4.2 rejoué dans le même clone : code 0 ; seule `.claude/hooks/garde_calcul.py` diffère ; les onze empreintes du § 1 ; lignée ; `commit_s = S` ; `ef31feff…`, `b7a5c1ba…`.
- § 4.1, dernière ligne, essayée avec `9a93f134` et `79e50d01c` : message affiché ; avec un commit inconnu : code 128, aucun message (échec du côté sûr).
- Non rejoué : § 4.4 (`controles` appelle le réseau), § 4.5, § 4.7 à 4.13 (outil de location).

### (6) Calendrier

- `session_v2 go` et `calendrier` rejoués hors ligne : conformes les 11, 14 et 15 novembre ; `calendrier` **refuse le 16** (« dernier jour de création (2026-11-15) dépassé ») ; `go` refuse le 17. Lignes égales à l'attendu du § 4.4.
- `1794873600` = 2026-11-17T00:00:00Z ; moins 27,2 h = 2026-11-15T20:48Z : égal au texte scellé (« Devis », calendrier).
- Fenêtre de GO-2026-11-07-02 : douze recherches à quinze minutes, 0 USD, puis H200 seulement après un mot de Lazar (R-2077) : conforme à la ligne du registre, plus stricte qu'elle.
- Minuterie : à l'échéance, consignation bornée à 2 400 s puis destruction dans une marge de 1 800 s, soit 01:10 UTC au plus tard ; le relevé de 01:15 UTC du § 4.13 est bien placé. « Liste d'arrêt » scellée : aucun couperet de temps, résultats partiels consignés avant la destruction par la minuterie : respectée depuis B1.
- Aujourd'hui 11 novembre : quatre jours avant le dernier jour de création ; le 14 vers 17:00 UTC garde une relance.

### (7) `COMMIT_MAIN_REMISE`

Le procédé est **sain** : la garde du § 4.1 n'exige qu'un ancêtre de la tête clonée ; tout descendant du commit de l'engagement porte `SCELLEMENT-T07`, l'engagement et R-2092 (vérifié à `79e50d01c` : 1, 1, 1) ; l'ordre lui-même est tenu par son compagnon et par l'empreinte du message de remise ; un commit non poussé ou mal recopié fait échouer la garde sans rien créer. Seule la définition écrite est à reprendre (CL5-3).

## 4. Ce que je n'ai pas vérifié

- Rien de l'outil de location : états `running` et `loading`, texte de `show instance`, lecture de la clé (M9).
- Le clone depuis le dépôt distant (filtre des blobs) ; `controles` en ligne.
- L'ordre de la variante B et le texte de T0.7 (seule son empreinte).
- Le mot exact de R-2113 sur l'attente de Lazar a été relu au registre ; R-2051 et R-2090 ne l'ont pas été.

## 5. Gestes à déclarer

- Deux clones locaux `--shared` dans le bac à sable (`…/agents/cl-ordre-7b-b5/w46/`) : les objets du dépôt y sont joints par référence, aucun chemin interdit extrait ni lu ; l'extraction de S a signalé six objets absents (noms de fichiers de `registres/` et de `docs/decisions/`, `docs/notes/` affichés par l'erreur, non ouverts).
- `ls docs/procedures/` filtré sur le nom de l'ordre ; `git log --oneline` (titres de quatre commits).
- Aucun refus de permission. Aucun appel externe, aucune dépense, aucune instance, aucune clé lue, aucun `lecture-sondes-t06.json`, aucune pièce de 7a, aucun chemin du bras d'attaque ouvert.
