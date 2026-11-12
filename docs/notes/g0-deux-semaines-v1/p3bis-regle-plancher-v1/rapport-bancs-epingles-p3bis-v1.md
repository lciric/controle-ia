# P3-bis — bancs rejoués contre une chaîne épinglée : correction sur place — rapport v1

Écrit le 2026-11-11 à 14:36 UTC (heure relevée par `date -u`) par un développeur neuf (Claude Opus 5.5, `claude-opus-5-5`), sous la consigne `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-correction-bancs-epingles-p3bis-v1.md` (`2748d9442a7cb6f6ec2ca874f3bbdd9d91bd63fc6feef3a08350f9a804e9ce49`, empreinte vérifiée avant lecture) de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`. Je n'ai écrit ni P3-bis, ni son code, ni sa chaîne, ni aucune de leurs contre-lectures. Aucun fichier de T0.7 lu ; aucun chemin interdit ouvert ni extrait sur disque ; aucune dépense ; aucun appel externe hors la poussée de ma branche et sa relecture (`git ls-remote`) vers le dépôt de travail.

## Verdict

**Conforme.** Les trois bancs corrigés jouent conformes contre la chaîne non épinglée du commit du code (a) et contre la copie épinglée de `scellement/p3bis-v1` (b) : six passages, dernières lignes conformes, « cas non conformes : 0 » ; mêmes comptes de cas qu'avant (contrôles 42, récupération 46, répétition jouet 25 lignes conformes) ; lignes de cas identiques à celles des journaux de développement d'avant ; `git diff 5e457525 68ded698` ne touche que les trois bancs et leurs compagnons.

## Branche et commits

- Branche neuve `prep/p3bis-bancs-epingles-v1`, partie du commit du code `5e4575259478af3611e2c7fb1313342912caf484`, dans mon arbre `…/agents/p3bis-bancs/arbre` (jamais le dépôt principal).
- **Commit de la correction : `68ded698ce1bbfd8815d7b7ab28557775e4d2e5b`** (parent `5e457525…`, 2026-11-11T14:24:14Z), garde des secrets à 0 avant le commit et avant la poussée ; poussé par `git push origin prep/p3bis-bancs-epingles-v1`, tête distante relue par `git ls-remote` : `68ded698…`.
- Ce rapport et son compagnon : commit suivant sur la même branche (deux chemins neufs, rien d'autre).

## Empreintes (sha256)

| Fichier (`docs/procedures/P3-bis-temoin-positif-v1/`) | Avant (`5e457525`) | Après (`68ded698`) |
|---|---|---|
| `essais_controles_p3bis_v2.sh` | `98d03a603266ca851225f9f5c15c8aa62df832d3237756997b6f1c629370f2d2` | `36a88949fe435cb6dbf30de88789d2ccdd2829abdd1f83e2545605b434d6210d` |
| `essais_recuperation_p3bis_v2.sh` | `9e39f5ca204806b4b93c67917053fe03683ac393f39bc5c88281fc34d9975507` | `ae2e2d2f3525672c2d65fccbf41620897caf543d66b7ed6928251a28de35f954` |
| `repetition_jouet_p3bis_v2.sh` | `2e4d16280399f9273c35c93190566152b66ade0f22755c64219e11ae05f5370f` | `750ec2530cc4261a57a50a54c062e770e20399127247ba5918fa904267022e02` |

Compagnons réécrits sur place à la forme de `scellement.sceller` (`<sha256>  <nom>` et fin de ligne ; permission de la mère pour ces trois-là, R-2367), relus par `python -m controle_ia.scellement verifier` : trois « OK ». Les noms ne changent pas (le module commun, `JOURNAUX` et le scellement les nomment).

## Diff commenté (`git diff 5e4575259478af3611e2c7fb1313342912caf484 68ded698ce1bbfd8815d7b7ab28557775e4d2e5b`)

`--name-status` : six `M`, les trois bancs et leurs trois compagnons ; 27 lignes ajoutées, 8 retirées. Rien d'autre.

1. **`essais_controles_p3bis_v2.sh`**
   - En-tête : quatre lignes de commentaire (« Correction sur place … R-2367 … »).
   - Copie jouée (bloc Python) : `re.findall(rf"^{k}=A_EPINGLER.*$", …)` devient `re.findall(rf"^{k}=.*$", …)`. L'exigence d'une occurrence est celle d'avant (`assert len(lignes) == 1, k`, puis `t.count(ligne) == 1` dans `rep()`), comme la garde finale « aucune affectation à A_EPINGLER ». Contre des contrôles épinglés, la ligne entière (valeur épinglée et commentaire) est remplacée par la valeur du banc, exactement comme l'était la ligne `A_EPINGLER` : la copie jouée a la même forme sous (a) et sous (b) (« lignes changées dans la copie des contrôles : 18 » dans les deux journaux).
   - K34 : avant, le cas jouait `$ICI/controles_avant_depense_p3bis_v2.sh` lui-même, artefact valable tant que la chaîne n'était pas épinglée ; contre la chaîne épinglée, la garde « épingle restée » ne se serait plus déclenchée et le script aurait poursuivi vers `[ -x "$PY" ]` puis le clonage du vrai `DEPOT_URL`. Désormais : copie de la copie jouée (`controles-banc.sh` : dépôt nu local, valeurs du banc) où les treize épingles sont remises à `A_EPINGLER` par un `sed -E` ancré sur leurs treize noms ; garde de la copie : exactement 13 lignes changées et 13 lignes `^K=A_EPINGLER$`, sinon « copie K34 non sûre » (code 2). Verdict attendu inchangé : code 2 et « A_EPINGLER » dans la console. L'artefact ne dépend plus de l'état de la chaîne : il est le même sous (a) et sous (b), au chemin de la racine près.
2. **`essais_recuperation_p3bis_v2.sh`**
   - En-tête : quatre lignes de commentaire.
   - Copie jouée : garde neuve « une ligne `PY=` exigée » (`grep -c '^PY='` égal à 1, sinon code 2) ; `sed "s|^PY=A_EPINGLER.*|PY=$PYB|"` devient `sed "s|^PY=.*|PY=$PYB|"`. La garde existante « 2 lignes changées (DEPOT_URL, PY) » reste telle quelle (elle refusait la chaîne épinglée : la ligne `PY` ne changeait plus).
   - R01e : avant, le cas jouait `$ICI/recuperation_p3bis_v2.sh` lui-même ; désormais copie de la copie jouée où `PY` est remis à `A_EPINGLER` (`sed`), garde « exactement 1 ligne changée », sinon « copie R01e non sûre » (code 2). Verdict attendu inchangé : code 2 et « A_EPINGLER ».
3. **`repetition_jouet_p3bis_v2.sh`**
   - En-tête : trois lignes de commentaire.
   - Copie jouée de la récupération : même garde « une ligne `PY=` exigée » ; `sed "s|^PY=A_EPINGLER.*|…"` devient `sed "s|^PY=.*|…"`. Aucune étape ni vérification de la répétition ne change.

## Passages (a) et (b) — preuve (R5)

Dispositif :
- **(a) chaîne non épinglée** : mon arbre `…/agents/p3bis-bancs/arbre`, au commit `68ded698` (scripts de la chaîne du commit du code : contrôles `67c3c288…`, récupération `f95c60b9…`).
- **(b) copie épinglée** : second arbre à moi, jetable, détaché au même commit (`…/agents/p3bis-bancs/arbre-epingle`, aucune branche), dont `controles_avant_depense_p3bis_v2.sh` et `recuperation_p3bis_v2.sh` (et leurs compagnons) sont pris par `git show a3116ff529587121b283259b404684e07f9806f2:…` (contrôles `c3684087eae9bd568c6c7a7df689d32bc3ef611c7508a09371176a0c1e467ff7`, récupération `3b21c80cf9a040e779cbea2832f513d299b08c291eeed169cb8d1670df735cd9`, `sha256sum -c` conforme ; aucune ligne `A_EPINGLER`). `a3116ff5` est la tête distante de `scellement/p3bis-v1` ; la tête locale `d0d9fcb8` en est un ancêtre non épinglé (non utilisée).
- Place : `df -Pk` avant tout, 14 343 760 Ko libres (au moins 5 Go exigés) ; après création des deux arbres, 11 794 596 Ko.
- Six passages lancés ensemble par `…/agents/p3bis-bancs/outils/passages.sh`, chacun dans sa racine neuve (`racines-a/{controles,recuperation,jouet}`, `racines-b/{…}`), journal écrit dans `…/agents/p3bis-bancs/journaux/` (recopiés en annexe).

| Passage | Début → fin (UTC) | Code | Cas joués | Dernière ligne | Chaîne éprouvée | Journal (sha256) |
|---|---|---|---|---|---|---|
| (a) contrôles | 14:25:26 → 14:27:27 | 0 | 42 | FIN DU BANC DES CONTRÔLES DE P3-BIS ; cas non conformes : 0 | contrôles `67c3c288…` | `8f1b17b012416a2e20343ce59a0974c05f786c2ab54badc82b51eb291df81477` |
| (b) contrôles | 14:25:26 → 14:27:27 | 0 | 42 | FIN DU BANC DES CONTRÔLES DE P3-BIS ; cas non conformes : 0 | contrôles `c3684087…` | `89628d1979d95336f34b77952cf066c948aaa136af1eab2a5bc3c03c28005b24` |
| (a) récupération | 14:25:26 → 14:26:57 | 0 | 46 | FIN DU BANC DE LA RÉCUPÉRATION DE P3-BIS ; cas non conformes : 0 | récupération `f95c60b9…` | `13b1844835d5844fcb5d44041737c5800bf330f6c4a34dffca12c9d995d6b939` |
| (b) récupération | 14:25:26 → 14:26:57 | 0 | 46 | FIN DU BANC DE LA RÉCUPÉRATION DE P3-BIS ; cas non conformes : 0 | récupération `3b21c80c…` | `0cce6835b7b087f22c36ac4b7c240b1a2fadc78a3034a6ac9d72769f7be06669` |
| (a) répétition jouet | 14:25:26 → 14:35:02 | 0 | 25 lignes conformes (étapes et vérifications) | RÉPÉTITION JOUET DE LA CHAÎNE DE P3-BIS : CONFORME | récupération `f95c60b9…` | `674a5ac154198accfefd1ff8d9b84dd08a1c68134d45f54e0fb954c56cea807f` |
| (b) répétition jouet | 14:25:26 → 14:35:02 | 0 | 25 lignes conformes (étapes et vérifications) | RÉPÉTITION JOUET DE LA CHAÎNE DE P3-BIS : CONFORME | récupération `3b21c80c…` | `2e8b76d6ca859e994f3643e34c8f816f9ff85e657c0532c3527e50d20a902a75` |

Comparaison aux journaux de développement versés à `a3116ff5` (`banc-controles-p3bis-v2-dev.log` `8773d4eb…`, `banc-recuperation-p3bis-v2-dev.log` `31098d00…`, `repetition-jouet-p3bis-v2-dev.log` `5d7edeb2…`), après retrait des lignes « script éprouvé », des lignes de détail « | » (empreintes de commits synthétiques, différentes à chaque passage), des durées et heures, et, pour la répétition, des lignes de début, de durée et du commit de scellement synthétique : **identiques** pour les trois bancs, sous (a) comme sous (b) (mêmes cas, mêmes codes, mêmes nombres de KO, mêmes verdicts, dans le même ordre). Chaque journal neuf compte zéro ligne « NON CONFORME ». Les trois bancs corrigés y sont éprouvés sous leurs empreintes neuves (`36a88949…`, `ae2e2d2f…`, `750ec253…`).

Épreuve des journaux par le module commun, comme à la phase 2 (`verifications_p3bis_v2.py preuves DOSSIER banc-controles-p3bis-v2.log banc-recuperation-p3bis-v2.log repetition-jouet-p3bis-v2.log`, journaux copiés sous ces noms dans un dossier par passage) :
- (a) : code 0 ; dix scripts, chacun sous une seule empreinte dans les trois journaux (contrôles `67c3c28809f74808ec7fdfeeff4649f49dc9e4077e58253735b400531f3ef711`, récupération `f95c60b95e4e11563f29476560b0190228729f60c65162120c48a6bc6bdc467d`) ;
- (b) : code 0 ; dix scripts, chacun sous une seule empreinte (contrôles `c3684087eae9bd568c6c7a7df689d32bc3ef611c7508a09371176a0c1e467ff7`, récupération `3b21c80cf9a040e779cbea2832f513d299b08c291eeed169cb8d1670df735cd9`) ;
- les huit autres empreintes sont les mêmes sous (a) et (b) : bancs `36a88949…`, `ae2e2d2f…`, `750ec253…`, module commun `1524df5f…`, lanceur `029bdb5c…`, contrôle à cinq minutes `6f921349…`, surveillance `d6542107…`, destruction `cae56ec9…`.

## Cas changés

- **K34-epingles-non-remplies** (contrôles) : artefact fabriqué sur la copie jouée, les treize épingles remises à `A_EPINGLER`, au lieu du script réel. Joué : code 2, CONFORME, sous (a) et sous (b) ; console : « épingle restée « A_EPINGLER » : candidat non épinglé, aucun contrôle ».
- **R01e-epingle-non-remplie** (récupération) : artefact fabriqué sur la copie jouée, `PY=A_EPINGLER`, au lieu du script réel. Joué : code 2, CONFORME, sous (a) et sous (b) ; console : « épingle restée « A_EPINGLER » (PY) : aucune récupération ».
- Fabrications changées sans être des cas : copie jouée des contrôles (épingles remplacées quelle qu'en soit la valeur) ; copies jouées de la récupération, dans son banc et dans la répétition (`PY` quelle qu'en soit la valeur, une occurrence exigée).
- Tout autre cas : inchangé (lignes de cas identiques à celles d'avant, voir plus haut).

## Essais complémentaires (R4, R5) : gardes neuves et défaut reproduit

Joués après les six passages, dans l'arbre jetable (b), racines neuves `racines-c/`, par `…/agents/p3bis-bancs/outils/artefacts.sh` ; chacun s'arrête avant tout cas (aucun clonage, aucun appel externe). C1 et C2 rejouent les **anciens** bancs (`git show 5e457525:…`) contre la chaîne épinglée : ils montrent que (b) éprouve bien l'état qui cassait les bancs. A1 à A5 éprouvent chaque garde neuve « une occurrence exigée » sur un artefact (le cas sain de chacune est le passage correspondant ci-dessus).

| Essai | Banc joué | Artefact | Code | Motif attendu, relevé dans la console |
|---|---|---|---|---|
| C1 | **ancien** banc des contrôles (`98d03a60…`) | chaîne épinglée de `a3116ff5` | 2 | `AssertionError: CANDIDAT_RELU_CHEMIN` (le défaut rapporté, R-2367) |
| C2 | **ancien** banc de la récupération (`9e39f5ca…`) | chaîne épinglée de `a3116ff5` | 2 | « lignes changées dans la copie de la récupération : 1 », « copie de la récupération non sûre » |
| A1 | banc corrigé de la récupération | récupération épinglée à deux lignes `PY=` | 2 | « copie de la récupération non sûre : une ligne PY= exigée » |
| A2 | banc corrigé de la récupération | récupération épinglée sans ligne `PY=` | 2 | idem |
| A3 | répétition jouet corrigée | récupération épinglée à deux lignes `PY=` | 2 | idem (avant toute étape) |
| A4 | banc corrigé des contrôles | contrôles épinglés à deux lignes `PY=` | 2 | `AssertionError: PY` |
| A5 | banc corrigé des contrôles | contrôles épinglés sans ligne `CODE_RELU=` | 2 | `AssertionError: CODE_RELU` |

Journal `…/agents/p3bis-bancs/journaux/artefacts.log` (`ba1338b3164be26d8e08f7c9eb544e9dabda0e4ad88acb36e2458391f2fadc9e`, recopié en annexe) : 2026-11-11T14:35:24Z → 14:35:27Z, « essais complémentaires non conformes : 0 » ; l'arbre (b) remis ensuite à la chaîne épinglée et aux bancs corrigés, vérifié par `sha256sum -c` des cinq compagnons.

Réserve : les gardes de construction des deux artefacts (« copie K34 non sûre » : 13 lignes changées ; « copie R01e non sûre » : 1 ligne changée) n'ont été éprouvées que sur leur cas sain (les passages) ; elles ont le statut des gardes « copie K36 non sûre » et « copie R16 non sûre » existantes, qui ne peuvent se déclencher que sur une copie jouée corrompue par le banc lui-même.

## Écarts déclarés et réserves

1. **Remplissage des arbres** : `git worktree add --no-checkout`, `git sparse-checkout set --no-cone` (motifs d'extraction de la chaîne elle-même : `/*`, sans `docs/notes/bras-attaque/`, `diag/` et `runs/` de 7a, `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `diag/*/lecture-sondes-t06.json*`, `scripts/extraire_mesures_epreuve_t06_v1.py*` ; arbre (b) réduit à `src/`, `scripts/`, `tests/`, aux pièces nommées des bancs et à la racine), puis `git read-tree -mu HEAD`. Cette dernière commande n'est pas dans la liste explicite de l'exception (`worktree add`, `add`, `commit`, `push`) : elle ne touche que l'index de mes propres arbres et a servi à ce qu'aucun chemin interdit ne soit jamais extrait sur disque (absence vérifiée : `docs/notes/bras-attaque`, `diag/20261109-070232-t06-reel`, `runs/20261109-070232-t06-reel`, `scripts/extraire_mesures_epreuve_t06_v1.py`).
2. **Second arbre de travail** (b), détaché, jamais committé, retiré à la fin par `git worktree remove --force` sur son chemin exact.
3. En-têtes des trois bancs : une note de correction ajoutée ; le paragraphe « Copie jouée » de l'en-tête du banc des contrôles (« les épingles A_EPINGLER (valeurs du banc) ») laissé tel quel.
4. Garde des secrets : motif `(sk-ant-[A-Za-z0-9]|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|hf_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{12}|AIza[0-9A-Za-z_-]{20,}|PRIVATE[ ]KEY|xox[baprs]-)` sur `git diff --cached` (et sur le diff de la branche avant la poussée), 0 à chaque fois, chaîné par `&&` (la consigne ne fixe pas le motif : réunion des motifs des consignes sœurs).
5. Suite complète non lancée (règle 5) ; seuls les trois bancs, les essais complémentaires et des essais ciblés des transformations ont été joués.
6. Journaux complets gardés dans `…/agents/p3bis-bancs/journaux/` et recopiés en annexe ; racines effacées après coup par leur chemin exact (voir « Nettoyage »).
7. Point pour la mère : à la phase 2, les bancs rejoués après l'épinglage éprouveront les contrôles sous `c3684087…` et la récupération sous `3b21c80c…` ; les trois bancs corrigés portent désormais `36a88949…`, `ae2e2d2f…` et `750ec253…`.

## Nettoyage

Effacés à 14:35 UTC par leurs chemins exacts : `…/agents/p3bis-bancs/racines-a` (499 Mo), `…/racines-b` (499 Mo), `…/racines-c` (26 Mo), `…/preuves-a`, `…/preuves-b`, `…/comparaison` ; arbre jetable (b) retiré (`git worktree remove --force …/agents/p3bis-bancs/arbre-epingle`). `df -Pk` après : 11 804 948 Ko libres. Gardés : `…/agents/p3bis-bancs/journaux/` (sept journaux et `codes.txt`, `04801b84967e75f783b56a6f5e5e21d71434f04bc720fc7ca9dd648b8fd67d2a`) et `…/agents/p3bis-bancs/outils/` (lanceur des passages, essais complémentaires, assemblage de ce rapport) ; mon arbre `…/agents/p3bis-bancs/arbre` est retiré par son chemin exact après la poussée de ce rapport (la branche reste au dépôt local et sur `origin`).

`…` abrège `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad`.

## Annexe — journaux intégraux des passages

Chaque bloc reproduit le journal octet pour octet, entre la ligne qui suit la clôture d'ouverture et la clôture de fermeture (dernière fin de ligne comprise) ; son empreinte est écrite au-dessus.

### `banc-controles-a.log` (`8f1b17b012416a2e20343ce59a0974c05f786c2ab54badc82b51eb291df81477`, 10142 octets)

~~~~text
script éprouvé : controles_avant_depense_p3bis_v2.sh 67c3c28809f74808ec7fdfeeff4649f49dc9e4077e58253735b400531f3ef711
script éprouvé : verifications_p3bis_v2.py 1524df5f6432197fde4793a4fde56d4496407a107c88f5e294a6bc9716923054
script éprouvé : essais_controles_p3bis_v2.sh 36a88949fe435cb6dbf30de88789d2ccdd2829abdd1f83e2545605b434d6210d
lignes changées dans la copie des contrôles : 18 (13 épingles, CODE_P3, clonage, trois bouchons)
K00-sain : code 0 ; 0 KO ; CONFORME
    | CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES
    cas sain : 43 lignes OK, dernière ligne conforme : CONFORME
    cas sain : clone en extraction partielle, témoin docs/notes/bras-attaque/ absent du disque : CONFORME
K01-s-ajoute-un-fichier : code 1 ; 2 KO ; CONFORME
    | KO  1 contenu de S inattendu : A autre.txt A prereg/P3-bis-consignes-v1.md A prereg/P3-bis-consignes-v1.md.sha256 A prereg/P3-bis-temoin-positif-config-v1.json A prereg/P
    | KO  2 arbre gelé de S modifié depuis le commit du code
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K02-commit-cite-deux-fois : code 1 ; 4 KO ; CONFORME
    | KO  2 commit du code cité illisible, cité 2 fois, ou non ancêtre de S
    | KO  2 commit du code 5cdb4739235c64017c52344afb862ea085d16328 ≠ code relu épinglé bc75dc0bc919e2d12571eda0f19460798b2dcf45
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K03-commit-cite-autre : code 1 ; 3 KO ; CONFORME
    | KO  2 commit du code fbb83477fef99513c982c147752ffbcb6522d592 ≠ code relu épinglé bc75dc0bc919e2d12571eda0f19460798b2dcf45
    | KO  2 arbre gelé de S modifié depuis le commit du code
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K04-arbre-gele-modifie : code 1 ; 1 KO ; CONFORME
    | KO  2 arbre gelé de S modifié depuis le commit du code
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K05-identite-fichier-de-p3-modifie : code 1 ; 1 KO ; CONFORME
    | KO  3 identité avec P3 (code 0) : M src/controle_ia/gardes.py 
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K06-marqueur-restant : code 1 ; 3 KO ; CONFORME
    | KO  4 marqueurs restants dans le texte : <<CHAINE_P3BIS>> 
    | KO  4 problemes() non vide : ['marqueurs de gabarit restants : <<CHAINE_P3BIS>>']
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K07-problemes-non-vide : code 1 ; 2 KO ; CONFORME
    | KO  4 problemes() non vide : ['section absente : Contre-lecture']
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K08-texte-autre-que-le-relu : code 1 ; 1 KO ; CONFORME
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K09-config-autre-que-la-relue : code 1 ; 1 KO ; CONFORME
    | KO  4 prereg/P3-bis-temoin-positif-config-v1.json de S ≠ configuration relue
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K10-taches-non-citees : code 1 ; 2 KO ; CONFORME
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | KO  4 tâches non citées par leur empreinte
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K11-go-autre : code 1 ; 2 KO ; CONFORME
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | KO  5 GO : GO-2026-11-08-13 : seul GO-2026-11-10-02 est accepté pour P3-bis
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K12-go-revoque : code 1 ; 2 KO ; CONFORME
    | KO  5 GO : GO-2026-11-10-02 (ou GO-2026-11-02-29, qu'il prolonge) révoqué au registre des GO (GO-2026-11-10-99)
    | KO  5 garde de calcul sur le registre de S : GARDE (registres/go, R10) — commande bloquée : GO-2026-11-10-02 révoqué par GO-2026-11-10-99
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K13-garde-de-calcul : code 1 ; 1 KO ; CONFORME
    | KO  5 garde de calcul sur le registre de S : GARDE (registres/go, R10) — commande bloquée : registre GO mal formé ligne 12 : dates illisibles
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K14-essai-verse-non-conforme : code 1 ; 1 KO ; CONFORME
    | KO  6 essai de fermeture : sortie absente, d'une autre empreinte, non scellée, non citée ou non conforme
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K15-essai-non-cite : code 1 ; 2 KO ; CONFORME
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | KO  6 essai de fermeture : sortie absente, d'une autre empreinte, non scellée, non citée ou non conforme
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K16-essai-rejoue-non-conforme : code 1 ; 1 KO ; CONFORME
    | KO  6 essai de fermeture rejoué au commit S : code 1, « ESSAI DIFFÉRENTIEL DE FERMETURE : non conforme (cité) » : aucune création
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K17-longueurs-a-differe-de-t : code 1 ; 1 KO ; CONFORME
    | KO  7 longueurs : t7 : indication_gabarit A 91 ≠ T 92 (jeu décisif : aucun scellement, nœud)
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K18-longueurs-resume-autre : code 1 ; 1 KO ; CONFORME
    | KO  7 longueurs : résumé des longueurs ≠ longueurs attendues épinglées : {"consigne_gabarit": {"mention": {"92": 60}, "saboteur": {"90": 20, "91": 20, "92": 20}, "t
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K19-longueurs-non-citees : code 1 ; 2 KO ; CONFORME
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | KO  7 longueurs attendues non citées par le texte
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K20-n-cite-autre : code 1 ; 2 KO ; CONFORME
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | KO  8 liste ciblée : « 531 passed in 1.00s » (code 0 ; 530 attendus)
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K21-essai-en-echec : code 1 ; 1 KO ; CONFORME
    | KO  8 liste ciblée : « 1 failed, 530 passed in 1.00s » (code 1 ; 531 attendus)
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K22-liste-autre-empreinte : code 1 ; 2 KO ; CONFORME
    | KO  2 arbre gelé de S modifié depuis le commit du code
    | KO  8 liste ciblée absente ou d'empreinte autre que celle de scripts/p3bis_instance_v2.sh
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K23-versions-autres : code 1 ; 2 KO ; CONFORME
    | KO  2 arbre gelé de S modifié depuis le commit du code
    | KO  8 environnement PY : 2 dépendances épinglées relues ; écarts : ['numpy 2.4.6 ≠ 0.0.1']
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K24-config-hors-ecarts : code 1 ; 3 KO ; CONFORME
    | KO  4 configuration relue absent(e), non scellé(e) ou d'empreinte différente
    | KO  4 prereg/P3-bis-temoin-positif-config-v1.json de S ≠ configuration relue
    | KO  9 configuration : écarts à celle de P3 hors des écarts du texte : ['lot']
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K25-valeur-non-citee : code 1 ; 2 KO ; CONFORME
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | KO  10 valeur(s) non citée(s) par le texte : ["au plus 2,10 USD de l'heure"]
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K26-constante-autre : code 1 ; 2 KO ; CONFORME
    | KO  10 constantes de la chaîne différentes de celles du module commun : lancer_p3bis_v2.sh GO_CALCUL : ['GO-2026-11-08-13'] ≠ [GO-2026-11-10-02]
    | KO  14 verifier-arbre : ÉCHEC docs/procedures/P3-bis-temoin-positif-v1/lancer_p3bis_v2.sh : docs/procedures/P3-bis-temoin-positif-v1/lancer_p3bis_v2.sh : empreinte 7a923
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K27-instance-avec-timeout : code 1 ; 3 KO ; CONFORME
    | KO  2 arbre gelé de S modifié depuis le commit du code
    | KO  11 empreinte de scripts/p3bis_instance_v2.sh (49ad62987ff88e1673dfb36ea337c9fec736800a998466bc31269a376dc72f23) non citée
    | KO  11 scripts/p3bis_instance_v2.sh : commande « timeout » (aucun budget de temps)
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K28-instance-non-citee : code 1 ; 2 KO ; CONFORME
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | KO  11 empreinte de scripts/p3bis_instance_v2.sh (83820dfd8ef7205c44f89e63450d801d60b95eddecb504cd2af992fa5b1eaa5d) non citée
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K29-citation-en-double : code 1 ; 3 KO ; CONFORME
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | KO  12 lecture précoce : citation absente, en double, ou chemin inattendu
    | KO  12 intitulés absents ou cités plusieurs fois : « Chemin des consignes de P3 »
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K30-lancement-autre-branche : code 1 ; 2 KO ; CONFORME
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | KO  12 ligne « Lancement » : PREREG, BRANCHE ou DEPOT_URL autres
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K31-branche-presente : code 1 ; 1 KO ; CONFORME
    | KO  13 branche calcul/p3bis-reel-v1 : code 0 (2 attendu)
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K32-rapport-absent : code 1 ; 1 KO ; CONFORME
    | KO  14 rapport brouillons/P3-bis-temoin-positif-v1/contre-lecture-4-banc-v1.md absent, non scellé ou d'empreinte différente
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K33-sceau-faux-sous-docs : code 1 ; 1 KO ; CONFORME
    | KO  14 verifier-arbre : ÉCHEC docs/procedures/P3-bis-temoin-positif-v1/surveiller_p3bis_v2.sh : docs/procedures/P3-bis-temoin-positif-v1/surveiller_p3bis_v2.sh : emprein
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K33b-sceau-faux-des-taches : code 1 ; 1 KO ; CONFORME
    | KO  4 sceaux
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K36-extraction-entiere-refusee : code 2 ; CONFORME
    | REFUS : docs/notes/bras-attaque extrait sur disque (interdits communs v2, règle 9 ; CD-05) : aucun contrôle
K34-epingles-non-remplies : code 2 ; CONFORME
    | épingle restée « A_EPINGLER » : candidat non épinglé, aucun contrôle
K35-usage : code 2 ; CONFORME
    | usage : controles_avant_depense_p3bis_v2.sh S DOSSIER_NEUF BRANCHE (trois arguments)
K35b-branche-invalide : code 2 ; CONFORME
    | BRANCHE : calcul/p3bis-reel-v1, -v2 ou -v3 attendue
K35c-dossier-existant : code 2 ; CONFORME
    | /tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/p3bis-bancs/racines-a/controles/clone-k35c existe déjà
cas joués : 42
FIN DU BANC DES CONTRÔLES DE P3-BIS ; cas non conformes : 0
~~~~

### `banc-controles-b.log` (`89628d1979d95336f34b77952cf066c948aaa136af1eab2a5bc3c03c28005b24`, 10142 octets)

~~~~text
script éprouvé : controles_avant_depense_p3bis_v2.sh c3684087eae9bd568c6c7a7df689d32bc3ef611c7508a09371176a0c1e467ff7
script éprouvé : verifications_p3bis_v2.py 1524df5f6432197fde4793a4fde56d4496407a107c88f5e294a6bc9716923054
script éprouvé : essais_controles_p3bis_v2.sh 36a88949fe435cb6dbf30de88789d2ccdd2829abdd1f83e2545605b434d6210d
lignes changées dans la copie des contrôles : 18 (13 épingles, CODE_P3, clonage, trois bouchons)
K00-sain : code 0 ; 0 KO ; CONFORME
    | CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES
    cas sain : 43 lignes OK, dernière ligne conforme : CONFORME
    cas sain : clone en extraction partielle, témoin docs/notes/bras-attaque/ absent du disque : CONFORME
K01-s-ajoute-un-fichier : code 1 ; 2 KO ; CONFORME
    | KO  1 contenu de S inattendu : A autre.txt A prereg/P3-bis-consignes-v1.md A prereg/P3-bis-consignes-v1.md.sha256 A prereg/P3-bis-temoin-positif-config-v1.json A prereg/P
    | KO  2 arbre gelé de S modifié depuis le commit du code
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K02-commit-cite-deux-fois : code 1 ; 4 KO ; CONFORME
    | KO  2 commit du code cité illisible, cité 2 fois, ou non ancêtre de S
    | KO  2 commit du code 52d70dacd15c2753583dfe6f84318de2cf04661e ≠ code relu épinglé bc75dc0bc919e2d12571eda0f19460798b2dcf45
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K03-commit-cite-autre : code 1 ; 3 KO ; CONFORME
    | KO  2 commit du code fbb83477fef99513c982c147752ffbcb6522d592 ≠ code relu épinglé bc75dc0bc919e2d12571eda0f19460798b2dcf45
    | KO  2 arbre gelé de S modifié depuis le commit du code
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K04-arbre-gele-modifie : code 1 ; 1 KO ; CONFORME
    | KO  2 arbre gelé de S modifié depuis le commit du code
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K05-identite-fichier-de-p3-modifie : code 1 ; 1 KO ; CONFORME
    | KO  3 identité avec P3 (code 0) : M src/controle_ia/gardes.py 
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K06-marqueur-restant : code 1 ; 3 KO ; CONFORME
    | KO  4 marqueurs restants dans le texte : <<CHAINE_P3BIS>> 
    | KO  4 problemes() non vide : ['marqueurs de gabarit restants : <<CHAINE_P3BIS>>']
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K07-problemes-non-vide : code 1 ; 2 KO ; CONFORME
    | KO  4 problemes() non vide : ['section absente : Contre-lecture']
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K08-texte-autre-que-le-relu : code 1 ; 1 KO ; CONFORME
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K09-config-autre-que-la-relue : code 1 ; 1 KO ; CONFORME
    | KO  4 prereg/P3-bis-temoin-positif-config-v1.json de S ≠ configuration relue
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K10-taches-non-citees : code 1 ; 2 KO ; CONFORME
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | KO  4 tâches non citées par leur empreinte
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K11-go-autre : code 1 ; 2 KO ; CONFORME
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | KO  5 GO : GO-2026-11-08-13 : seul GO-2026-11-10-02 est accepté pour P3-bis
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K12-go-revoque : code 1 ; 2 KO ; CONFORME
    | KO  5 GO : GO-2026-11-10-02 (ou GO-2026-11-02-29, qu'il prolonge) révoqué au registre des GO (GO-2026-11-10-99)
    | KO  5 garde de calcul sur le registre de S : GARDE (registres/go, R10) — commande bloquée : GO-2026-11-10-02 révoqué par GO-2026-11-10-99
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K13-garde-de-calcul : code 1 ; 1 KO ; CONFORME
    | KO  5 garde de calcul sur le registre de S : GARDE (registres/go, R10) — commande bloquée : registre GO mal formé ligne 12 : dates illisibles
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K14-essai-verse-non-conforme : code 1 ; 1 KO ; CONFORME
    | KO  6 essai de fermeture : sortie absente, d'une autre empreinte, non scellée, non citée ou non conforme
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K15-essai-non-cite : code 1 ; 2 KO ; CONFORME
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | KO  6 essai de fermeture : sortie absente, d'une autre empreinte, non scellée, non citée ou non conforme
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K16-essai-rejoue-non-conforme : code 1 ; 1 KO ; CONFORME
    | KO  6 essai de fermeture rejoué au commit S : code 1, « ESSAI DIFFÉRENTIEL DE FERMETURE : non conforme (cité) » : aucune création
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K17-longueurs-a-differe-de-t : code 1 ; 1 KO ; CONFORME
    | KO  7 longueurs : t7 : indication_gabarit A 91 ≠ T 92 (jeu décisif : aucun scellement, nœud)
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K18-longueurs-resume-autre : code 1 ; 1 KO ; CONFORME
    | KO  7 longueurs : résumé des longueurs ≠ longueurs attendues épinglées : {"consigne_gabarit": {"mention": {"92": 60}, "saboteur": {"90": 20, "91": 20, "92": 20}, "t
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K19-longueurs-non-citees : code 1 ; 2 KO ; CONFORME
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | KO  7 longueurs attendues non citées par le texte
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K20-n-cite-autre : code 1 ; 2 KO ; CONFORME
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | KO  8 liste ciblée : « 531 passed in 1.00s » (code 0 ; 530 attendus)
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K21-essai-en-echec : code 1 ; 1 KO ; CONFORME
    | KO  8 liste ciblée : « 1 failed, 530 passed in 1.00s » (code 1 ; 531 attendus)
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K22-liste-autre-empreinte : code 1 ; 2 KO ; CONFORME
    | KO  2 arbre gelé de S modifié depuis le commit du code
    | KO  8 liste ciblée absente ou d'empreinte autre que celle de scripts/p3bis_instance_v2.sh
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K23-versions-autres : code 1 ; 2 KO ; CONFORME
    | KO  2 arbre gelé de S modifié depuis le commit du code
    | KO  8 environnement PY : 2 dépendances épinglées relues ; écarts : ['numpy 2.4.6 ≠ 0.0.1']
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K24-config-hors-ecarts : code 1 ; 3 KO ; CONFORME
    | KO  4 configuration relue absent(e), non scellé(e) ou d'empreinte différente
    | KO  4 prereg/P3-bis-temoin-positif-config-v1.json de S ≠ configuration relue
    | KO  9 configuration : écarts à celle de P3 hors des écarts du texte : ['lot']
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K25-valeur-non-citee : code 1 ; 2 KO ; CONFORME
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | KO  10 valeur(s) non citée(s) par le texte : ["au plus 2,10 USD de l'heure"]
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K26-constante-autre : code 1 ; 2 KO ; CONFORME
    | KO  10 constantes de la chaîne différentes de celles du module commun : lancer_p3bis_v2.sh GO_CALCUL : ['GO-2026-11-08-13'] ≠ [GO-2026-11-10-02]
    | KO  14 verifier-arbre : ÉCHEC docs/procedures/P3-bis-temoin-positif-v1/lancer_p3bis_v2.sh : docs/procedures/P3-bis-temoin-positif-v1/lancer_p3bis_v2.sh : empreinte 7a923
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K27-instance-avec-timeout : code 1 ; 3 KO ; CONFORME
    | KO  2 arbre gelé de S modifié depuis le commit du code
    | KO  11 empreinte de scripts/p3bis_instance_v2.sh (49ad62987ff88e1673dfb36ea337c9fec736800a998466bc31269a376dc72f23) non citée
    | KO  11 scripts/p3bis_instance_v2.sh : commande « timeout » (aucun budget de temps)
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K28-instance-non-citee : code 1 ; 2 KO ; CONFORME
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | KO  11 empreinte de scripts/p3bis_instance_v2.sh (83820dfd8ef7205c44f89e63450d801d60b95eddecb504cd2af992fa5b1eaa5d) non citée
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K29-citation-en-double : code 1 ; 3 KO ; CONFORME
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | KO  12 lecture précoce : citation absente, en double, ou chemin inattendu
    | KO  12 intitulés absents ou cités plusieurs fois : « Chemin des consignes de P3 »
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K30-lancement-autre-branche : code 1 ; 2 KO ; CONFORME
    | KO  4 prereg/P3-bis-temoin-positif-v1.md de S ≠ candidat relu
    | KO  12 ligne « Lancement » : PREREG, BRANCHE ou DEPOT_URL autres
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K31-branche-presente : code 1 ; 1 KO ; CONFORME
    | KO  13 branche calcul/p3bis-reel-v1 : code 0 (2 attendu)
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K32-rapport-absent : code 1 ; 1 KO ; CONFORME
    | KO  14 rapport brouillons/P3-bis-temoin-positif-v1/contre-lecture-4-banc-v1.md absent, non scellé ou d'empreinte différente
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K33-sceau-faux-sous-docs : code 1 ; 1 KO ; CONFORME
    | KO  14 verifier-arbre : ÉCHEC docs/procedures/P3-bis-temoin-positif-v1/surveiller_p3bis_v2.sh : docs/procedures/P3-bis-temoin-positif-v1/surveiller_p3bis_v2.sh : emprein
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K33b-sceau-faux-des-taches : code 1 ; 1 KO ; CONFORME
    | KO  4 sceaux
    | CONTRÔLES AVANT DÉPENSE : ÉCHEC
K36-extraction-entiere-refusee : code 2 ; CONFORME
    | REFUS : docs/notes/bras-attaque extrait sur disque (interdits communs v2, règle 9 ; CD-05) : aucun contrôle
K34-epingles-non-remplies : code 2 ; CONFORME
    | épingle restée « A_EPINGLER » : candidat non épinglé, aucun contrôle
K35-usage : code 2 ; CONFORME
    | usage : controles_avant_depense_p3bis_v2.sh S DOSSIER_NEUF BRANCHE (trois arguments)
K35b-branche-invalide : code 2 ; CONFORME
    | BRANCHE : calcul/p3bis-reel-v1, -v2 ou -v3 attendue
K35c-dossier-existant : code 2 ; CONFORME
    | /tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/p3bis-bancs/racines-b/controles/clone-k35c existe déjà
cas joués : 42
FIN DU BANC DES CONTRÔLES DE P3-BIS ; cas non conformes : 0
~~~~

### `banc-recuperation-a.log` (`13b1844835d5844fcb5d44041737c5800bf330f6c4a34dffca12c9d995d6b939`, 8252 octets)

~~~~text
script éprouvé : recuperation_p3bis_v2.sh f95c60b95e4e11563f29476560b0190228729f60c65162120c48a6bc6bdc467d
script éprouvé : detruire_p3bis_v2.sh cae56ec9cbd00485a9506a1af1bb9dfd8e4b493e966003cb0ed365fe6973ae46
script éprouvé : verifications_p3bis_v2.py 1524df5f6432197fde4793a4fde56d4496407a107c88f5e294a6bc9716923054
script éprouvé : essais_recuperation_p3bis_v2.sh ae2e2d2f3525672c2d65fccbf41620897caf543d66b7ed6928251a28de35f954
lignes changées dans la copie de la récupération : 2 (DEPOT_URL, PY)
R00-sain : code 0 ; 0 KO ; CONFORME
    | RÉCUPÉRATION : TOUS CONFORMES ; paquet des lectures 1633cbec92f235cc6dffec70970a85d872af597c2b3968a93e20df4e00302679 poussé sur calcul/p3bis-reel-v1
    paquet poussé relu par le banc (vrai module v2) : deux lectures décisives sous le texte, lecture complémentaire lecture_p3bis_v2 (règle (a') sur 800 directions, ancienne règle sur 200), issue mécanique « vu », ligne 4, durées écrites : CONFORME
    branche distante : un seul commit de plus, qui n'ajoute que le paquet et son compagnon ; paquet de 16 783 360 octets à l'empreinte imprimée : CONFORME
    clone en extraction partielle : témoin docs/notes/bras-attaque/ absent du disque (CD-05) : CONFORME
    rapport écrit (récupération.rapport.txt) ; aucune ligne de la classe 2 affichée (seules les lignes de code et l'empreinte) : CONFORME
    clone : aucun fichier du run en clair, aucune sortie de lecture restée (non suivis et ignorés compris) : CONFORME
R01-branche-main : code 2 ; 0 KO ; CONFORME
    | BRANCHE : calcul/p3bis-reel-v1, -v2 ou -v3 (jamais main)
R01b-branche-autre : code 2 ; 0 KO ; CONFORME
    | BRANCHE : calcul/p3bis-reel-v1, -v2 ou -v3 (jamais main)
R01c-dossier-existant : code 2 ; 0 KO ; CONFORME
    | /tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/p3bis-bancs/racines-a/recuperation/recup-R01c-dossier-existant existe déjà (R12)
R01d-s-invalide : code 2 ; 0 KO ; CONFORME
    | S invalide
R01e-epingle-non-remplie : code 2 ; CONFORME
R02-s-non-ancetre : code 1 ; 3 KO ; CONFORME
    | KO  0 récupération exécutée ≠ copie versée à S
    | KO  1a S n'est pas ancêtre de la branche
    | RÉCUPÉRATION : 3 CONTRÔLE(S) EN ÉCHEC
R03-donnees-en-clair : code 1 ; 2 KO ; CONFORME
    | KO  1c FICHIER DU RUN EN CLAIR sur la branche (écart « Toute ouverture hors de la garde », à consigner) : donnees/20261112-080000-p3bis-reel/scores-p3.npz donnees/202
    | KO  1c chemins hors périmètre : donnees/20261112-080000-p3bis-reel/scores-p3.npz donnees/20261112-080000-p3bis-reel/scores-p3.npz.sha256 
    | RÉCUPÉRATION : 2 CONTRÔLE(S) EN ÉCHEC (aucune lecture, aucun commit)
    fichier du run en clair : aucune lecture, aucun commit poussé : CONFORME
R04-episodes-en-clair : code 1 ; 3 KO ; CONFORME
    | KO  1c FICHIER DU RUN EN CLAIR sur la branche (écart « Toute ouverture hors de la garde », à consigner) : diag/20261112-080000-p3bis-reel/episodes-p3.json 
    | KO  1c chemins hors périmètre : diag/20261112-080000-p3bis-reel/episodes-p3.json 
    | RÉCUPÉRATION : 3 CONTRÔLE(S) EN ÉCHEC (aucune lecture, aucun commit)
R05-modification : code 1 ; 3 KO ; CONFORME
    | KO  1b 1 changement(s) autre(s) qu'un ajout
    | KO  1c chemins hors périmètre : docs/procedures/P3-bis-temoin-positif-v1/detruire_p3bis_v2.sh 
    | RÉCUPÉRATION : 3 CONTRÔLE(S) EN ÉCHEC (aucune lecture, aucun commit)
R06-deux-runs : code 1 ; 2 KO ; CONFORME
    | KO  1d runs : 20261112-080000-p3bis-reel 20261112-090000-p3bis-reel (un seul, au motif, avec son manifeste, attendu)
    | KO  3 run : résumé et arrêt tous deux présents, ou runs illisibles
    | RÉCUPÉRATION : 2 CONTRÔLE(S) EN ÉCHEC (aucune lecture, aucun commit)
R07-auteur-autre : code 1 ; 1 KO ; CONFORME
    | KO  1e auteurs : autre,instance de calcul (P3-bis)
    | RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC (aucune lecture, aucun commit)
R08-sceau-faux : code 1 ; 1 KO ; CONFORME
    | KO  2a verifier-arbre : ÉCHEC diag/20261112-080000-p3bis-reel/resume.json : diag/20261112-080000-p3bis-reel/resume.json : empreinte 3fc539399428… ≠ scellée 00000000
    | RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC (aucune lecture, aucun commit)
R09-run-sans-resume : code 4 ; 0 KO ; CONFORME
    | RÉCUPÉRATION SANS LECTURE (RUN SANS RÉSUMÉ) : TOUS CONFORMES
    run sans résumé : rapport « SANS LECTURE », aucun commit poussé : CONFORME
R10-aucun-run : code 4 ; 0 KO ; CONFORME
    | RÉCUPÉRATION DES TRACES SEULES (AUCUN RUN), SANS LECTURE : TOUS CONFORMES
    aucun run : traces seules, code 4 : CONFORME
R11-second-paquet-absent : code 1 ; 1 KO ; CONFORME
    | KO  3 second paquet absent (index ou morceaux)
    | RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC (aucune lecture, aucun commit)
R12-second-paquet-altere : code 1 ; 3 KO ; CONFORME
    | KO  4 lectures fermées : code 1, 0 code(s) 0 sur 4 (une garde a arrêté une étape : nœud ; la lecture n'est jamais rejouée pour la mise en paquet)
    | KO  4 paquet des lectures absent, d'une autre taille, ou compagnon autre
    | RÉCUPÉRATION : 3 CONTRÔLE(S) EN ÉCHEC (aucun commit)
    second paquet altéré : la ligne « motif du dépliage » du module v2 est admise (classe 1) et affichée : CONFORME
    second paquet altéré : dépliage refusé, aucun commit poussé, aucun fichier en clair resté : CONFORME
R13-entropie-autre : code 1 ; 1 KO ; CONFORME
    | KO  3 entropie du texte « 111111111111111111111 » (citée 1 fois) ≠ 173398867739501636779144561928402532101
    | RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC (aucune lecture, aucun commit)
R14-lecture-en-echec : code 1 ; 1 KO ; CONFORME
    | KO  4 lectures fermées : code 1, 2 code(s) 0 sur 4 (une garde a arrêté une étape : nœud ; la lecture n'est jamais rejouée pour la mise en paquet)
    | RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC (aucun commit)
    lecture refusée par sa propre garde (configuration citée autre que celle du run) : aucun commit poussé : CONFORME
R15-copie-non-versee : code 1 ; CONFORME
R16-extraction-entiere-refusee : code 2 ; CONFORME
    | REFUS : docs/notes/bras-attaque extrait sur disque (interdits communs v2, règle 9 ; CD-05) : aucune récupération
D00-sain : code 0 ; CONFORME
    | DESTRUCTION : instance 99999999 détruite par son identifiant (R10), absente de la liste relue
    destruction : un seul appel, par l'identifiant ; ligne à consigner : CONFORME
D01-instance-gardee : code 2 ; CONFORME
    | REFUS : instance gardée (second paquet en échec) : jamais détruite avant le paquet refait
D01b-gardee-meme-motif-fin : code 2 ; CONFORME
    | REFUS : instance gardée (second paquet en échec) : jamais détruite avant le paquet refait
D02-processus-mort : code 2 ; CONFORME
    | REFUS : surveillance sans motif FIN (PROCESSUS MORT) : nœud de Lazar, aucune destruction ici
D02b-sans-motif : code 2 ; CONFORME
    | REFUS : surveillance sans motif FIN (absent) : nœud de Lazar, aucune destruction ici
D03-recuperation-non-conforme : code 2 ; CONFORME
    | REFUS : récupération non conforme, ou d'une autre branche que calcul/p3bis-reel-v1 (« RÉCUPÉRATION : 3 CONTRÔLE(S) EN ÉCHEC (aucun commit) »)
D04-autre-branche : code 2 ; CONFORME
    | REFUS : récupération non conforme, ou d'une autre branche que calcul/p3bis-reel-v1 (« RÉCUPÉRATION : TOUS CONFORMES ; paquet des lectures aaaaaaaaaaaaaaaaaaaaaaaaaaa
D05-identifiant-autre : code 2 ; CONFORME
    | REFUS : identifiant : instance 99999998 : ce lanceur a créé 99999999 ; aucune autre n'est arrêtée ni détruite ici
D06-instance-toleree : code 2 ; CONFORME
    | REFUS : identifiant : instance 58936099 : dans ARRETEES_TOLEREES ; jamais touchée par cette chaîne
D07-destruction-en-echec : code 1 ; CONFORME
    | DESTRUCTION EN ÉCHEC : code 1, liste relue « présente » : agir par l'identifiant 99999999, à la main (R10), consigner
D08-encore-listee : code 1 ; CONFORME
    | DESTRUCTION EN ÉCHEC : code 0, liste relue « présente » : agir par l'identifiant 99999999, à la main (R10), consigner
D09-usage : code 2 ; CONFORME
    les instances tolérées ne sont jamais visées par un verbe (tout le banc) : CONFORME
cas joués : 46
FIN DU BANC DE LA RÉCUPÉRATION DE P3-BIS ; cas non conformes : 0
~~~~

### `banc-recuperation-b.log` (`0cce6835b7b087f22c36ac4b7c240b1a2fadc78a3034a6ac9d72769f7be06669`, 8252 octets)

~~~~text
script éprouvé : recuperation_p3bis_v2.sh 3b21c80cf9a040e779cbea2832f513d299b08c291eeed169cb8d1670df735cd9
script éprouvé : detruire_p3bis_v2.sh cae56ec9cbd00485a9506a1af1bb9dfd8e4b493e966003cb0ed365fe6973ae46
script éprouvé : verifications_p3bis_v2.py 1524df5f6432197fde4793a4fde56d4496407a107c88f5e294a6bc9716923054
script éprouvé : essais_recuperation_p3bis_v2.sh ae2e2d2f3525672c2d65fccbf41620897caf543d66b7ed6928251a28de35f954
lignes changées dans la copie de la récupération : 2 (DEPOT_URL, PY)
R00-sain : code 0 ; 0 KO ; CONFORME
    | RÉCUPÉRATION : TOUS CONFORMES ; paquet des lectures 4773c222896edb406d22f33a017eea15e11b00a2bf691db463d7b3cada9314f3 poussé sur calcul/p3bis-reel-v1
    paquet poussé relu par le banc (vrai module v2) : deux lectures décisives sous le texte, lecture complémentaire lecture_p3bis_v2 (règle (a') sur 800 directions, ancienne règle sur 200), issue mécanique « vu », ligne 4, durées écrites : CONFORME
    branche distante : un seul commit de plus, qui n'ajoute que le paquet et son compagnon ; paquet de 16 783 360 octets à l'empreinte imprimée : CONFORME
    clone en extraction partielle : témoin docs/notes/bras-attaque/ absent du disque (CD-05) : CONFORME
    rapport écrit (récupération.rapport.txt) ; aucune ligne de la classe 2 affichée (seules les lignes de code et l'empreinte) : CONFORME
    clone : aucun fichier du run en clair, aucune sortie de lecture restée (non suivis et ignorés compris) : CONFORME
R01-branche-main : code 2 ; 0 KO ; CONFORME
    | BRANCHE : calcul/p3bis-reel-v1, -v2 ou -v3 (jamais main)
R01b-branche-autre : code 2 ; 0 KO ; CONFORME
    | BRANCHE : calcul/p3bis-reel-v1, -v2 ou -v3 (jamais main)
R01c-dossier-existant : code 2 ; 0 KO ; CONFORME
    | /tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/p3bis-bancs/racines-b/recuperation/recup-R01c-dossier-existant existe déjà (R12)
R01d-s-invalide : code 2 ; 0 KO ; CONFORME
    | S invalide
R01e-epingle-non-remplie : code 2 ; CONFORME
R02-s-non-ancetre : code 1 ; 3 KO ; CONFORME
    | KO  0 récupération exécutée ≠ copie versée à S
    | KO  1a S n'est pas ancêtre de la branche
    | RÉCUPÉRATION : 3 CONTRÔLE(S) EN ÉCHEC
R03-donnees-en-clair : code 1 ; 2 KO ; CONFORME
    | KO  1c FICHIER DU RUN EN CLAIR sur la branche (écart « Toute ouverture hors de la garde », à consigner) : donnees/20261112-080000-p3bis-reel/scores-p3.npz donnees/202
    | KO  1c chemins hors périmètre : donnees/20261112-080000-p3bis-reel/scores-p3.npz donnees/20261112-080000-p3bis-reel/scores-p3.npz.sha256 
    | RÉCUPÉRATION : 2 CONTRÔLE(S) EN ÉCHEC (aucune lecture, aucun commit)
    fichier du run en clair : aucune lecture, aucun commit poussé : CONFORME
R04-episodes-en-clair : code 1 ; 3 KO ; CONFORME
    | KO  1c FICHIER DU RUN EN CLAIR sur la branche (écart « Toute ouverture hors de la garde », à consigner) : diag/20261112-080000-p3bis-reel/episodes-p3.json 
    | KO  1c chemins hors périmètre : diag/20261112-080000-p3bis-reel/episodes-p3.json 
    | RÉCUPÉRATION : 3 CONTRÔLE(S) EN ÉCHEC (aucune lecture, aucun commit)
R05-modification : code 1 ; 3 KO ; CONFORME
    | KO  1b 1 changement(s) autre(s) qu'un ajout
    | KO  1c chemins hors périmètre : docs/procedures/P3-bis-temoin-positif-v1/detruire_p3bis_v2.sh 
    | RÉCUPÉRATION : 3 CONTRÔLE(S) EN ÉCHEC (aucune lecture, aucun commit)
R06-deux-runs : code 1 ; 2 KO ; CONFORME
    | KO  1d runs : 20261112-080000-p3bis-reel 20261112-090000-p3bis-reel (un seul, au motif, avec son manifeste, attendu)
    | KO  3 run : résumé et arrêt tous deux présents, ou runs illisibles
    | RÉCUPÉRATION : 2 CONTRÔLE(S) EN ÉCHEC (aucune lecture, aucun commit)
R07-auteur-autre : code 1 ; 1 KO ; CONFORME
    | KO  1e auteurs : autre,instance de calcul (P3-bis)
    | RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC (aucune lecture, aucun commit)
R08-sceau-faux : code 1 ; 1 KO ; CONFORME
    | KO  2a verifier-arbre : ÉCHEC diag/20261112-080000-p3bis-reel/resume.json : diag/20261112-080000-p3bis-reel/resume.json : empreinte b0d0c2e4d1d7… ≠ scellée 00000000
    | RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC (aucune lecture, aucun commit)
R09-run-sans-resume : code 4 ; 0 KO ; CONFORME
    | RÉCUPÉRATION SANS LECTURE (RUN SANS RÉSUMÉ) : TOUS CONFORMES
    run sans résumé : rapport « SANS LECTURE », aucun commit poussé : CONFORME
R10-aucun-run : code 4 ; 0 KO ; CONFORME
    | RÉCUPÉRATION DES TRACES SEULES (AUCUN RUN), SANS LECTURE : TOUS CONFORMES
    aucun run : traces seules, code 4 : CONFORME
R11-second-paquet-absent : code 1 ; 1 KO ; CONFORME
    | KO  3 second paquet absent (index ou morceaux)
    | RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC (aucune lecture, aucun commit)
R12-second-paquet-altere : code 1 ; 3 KO ; CONFORME
    | KO  4 lectures fermées : code 1, 0 code(s) 0 sur 4 (une garde a arrêté une étape : nœud ; la lecture n'est jamais rejouée pour la mise en paquet)
    | KO  4 paquet des lectures absent, d'une autre taille, ou compagnon autre
    | RÉCUPÉRATION : 3 CONTRÔLE(S) EN ÉCHEC (aucun commit)
    second paquet altéré : la ligne « motif du dépliage » du module v2 est admise (classe 1) et affichée : CONFORME
    second paquet altéré : dépliage refusé, aucun commit poussé, aucun fichier en clair resté : CONFORME
R13-entropie-autre : code 1 ; 1 KO ; CONFORME
    | KO  3 entropie du texte « 111111111111111111111 » (citée 1 fois) ≠ 173398867739501636779144561928402532101
    | RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC (aucune lecture, aucun commit)
R14-lecture-en-echec : code 1 ; 1 KO ; CONFORME
    | KO  4 lectures fermées : code 1, 2 code(s) 0 sur 4 (une garde a arrêté une étape : nœud ; la lecture n'est jamais rejouée pour la mise en paquet)
    | RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC (aucun commit)
    lecture refusée par sa propre garde (configuration citée autre que celle du run) : aucun commit poussé : CONFORME
R15-copie-non-versee : code 1 ; CONFORME
R16-extraction-entiere-refusee : code 2 ; CONFORME
    | REFUS : docs/notes/bras-attaque extrait sur disque (interdits communs v2, règle 9 ; CD-05) : aucune récupération
D00-sain : code 0 ; CONFORME
    | DESTRUCTION : instance 99999999 détruite par son identifiant (R10), absente de la liste relue
    destruction : un seul appel, par l'identifiant ; ligne à consigner : CONFORME
D01-instance-gardee : code 2 ; CONFORME
    | REFUS : instance gardée (second paquet en échec) : jamais détruite avant le paquet refait
D01b-gardee-meme-motif-fin : code 2 ; CONFORME
    | REFUS : instance gardée (second paquet en échec) : jamais détruite avant le paquet refait
D02-processus-mort : code 2 ; CONFORME
    | REFUS : surveillance sans motif FIN (PROCESSUS MORT) : nœud de Lazar, aucune destruction ici
D02b-sans-motif : code 2 ; CONFORME
    | REFUS : surveillance sans motif FIN (absent) : nœud de Lazar, aucune destruction ici
D03-recuperation-non-conforme : code 2 ; CONFORME
    | REFUS : récupération non conforme, ou d'une autre branche que calcul/p3bis-reel-v1 (« RÉCUPÉRATION : 3 CONTRÔLE(S) EN ÉCHEC (aucun commit) »)
D04-autre-branche : code 2 ; CONFORME
    | REFUS : récupération non conforme, ou d'une autre branche que calcul/p3bis-reel-v1 (« RÉCUPÉRATION : TOUS CONFORMES ; paquet des lectures aaaaaaaaaaaaaaaaaaaaaaaaaaa
D05-identifiant-autre : code 2 ; CONFORME
    | REFUS : identifiant : instance 99999998 : ce lanceur a créé 99999999 ; aucune autre n'est arrêtée ni détruite ici
D06-instance-toleree : code 2 ; CONFORME
    | REFUS : identifiant : instance 58936099 : dans ARRETEES_TOLEREES ; jamais touchée par cette chaîne
D07-destruction-en-echec : code 1 ; CONFORME
    | DESTRUCTION EN ÉCHEC : code 1, liste relue « présente » : agir par l'identifiant 99999999, à la main (R10), consigner
D08-encore-listee : code 1 ; CONFORME
    | DESTRUCTION EN ÉCHEC : code 0, liste relue « présente » : agir par l'identifiant 99999999, à la main (R10), consigner
D09-usage : code 2 ; CONFORME
    les instances tolérées ne sont jamais visées par un verbe (tout le banc) : CONFORME
cas joués : 46
FIN DU BANC DE LA RÉCUPÉRATION DE P3-BIS ; cas non conformes : 0
~~~~

### `repetition-jouet-a.log` (`674a5ac154198accfefd1ff8d9b84dd08a1c68134d45f54e0fb954c56cea807f`, 3942 octets)

~~~~text
début de la répétition : 2026-11-11T14:25:26Z
script éprouvé : lancer_p3bis_v2.sh 029bdb5c114a6166a21fa93724d71a2bf6158dc9686993424f6fbe8462352b08
script éprouvé : controle_cinq_minutes_p3bis_v2.sh 6f9213499687d655e290ab96c1ab8a1cdb9ecd373b1d6beecb7efda962f40864
script éprouvé : surveiller_p3bis_v2.sh d65421073068466a3aa6cc90ef00e6c76b15ea7b3e61e254c1dbafad020afe9b
script éprouvé : recuperation_p3bis_v2.sh f95c60b95e4e11563f29476560b0190228729f60c65162120c48a6bc6bdc467d
script éprouvé : detruire_p3bis_v2.sh cae56ec9cbd00485a9506a1af1bb9dfd8e4b493e966003cb0ed365fe6973ae46
script éprouvé : verifications_p3bis_v2.py 1524df5f6432197fde4793a4fde56d4496407a107c88f5e294a6bc9716923054
script éprouvé : repetition_jouet_p3bis_v2.sh 750ec2530cc4261a57a50a54c062e770e20399127247ba5918fa904267022e02
lignes changées : lanceur 3 (DEPOT, DEPOT_URL, INTERVALLE_OFFRE_S) ; récupération 2 (DEPOT_URL, PY)
commit de scellement de la répétition : c6ee102d079de46070219b0da69bc02c12619a3f
T1-lanceur : code 0 ; 7 s ; CONFORME
    | succès : True ; identifiant 77777771 ; message : 
    lancement : instance 77777771 écrite, offre 111, branche v1 poussée par l'« instance » : CONFORME
T1-cinq-minutes : code 0 ; 1 s ; CONFORME
    | CONTRÔLE À CINQ MINUTES : CONFORME
T1-surveillance : code 0 ; CONFORME
    | FIN : AMORCE 2026-11-12T12:30:00Z : fin, code 0 ; instance 77777771 arrêtée par son identifiant (R10) ; état relu : actual_status=exited cur_state=stopped intended_sta
    surveillance : PROGRES relevé, dépense relevée sous 80 USD, arrêt par l'identifiant (instance arrêtée) : CONFORME
T1-recuperation : code 0 ; 15 s ; CONFORME
    | RÉCUPÉRATION : TOUS CONFORMES ; paquet des lectures b03b64788c0ebdb0916a131516999ce776b7cc4ddb8f950f100396fb40504341 poussé sur calcul/p3bis-reel-v1
    récupération : branche distante = commit du seul paquet (16 783 360 octets) et de son compagnon : CONFORME
    récupération : paquet ouvert (jouet) : lecture complémentaire lecture_p3bis_v2, règle (a') sur 800 directions, ancienne règle sur 200, issue « vu », ligne 4 : CONFORME
T1-destruction : code 0 ; 1 s ; CONFORME
    | DESTRUCTION : instance 77777771 détruite par son identifiant (R10), absente de la liste relue
T2-lanceur : code 0 ; 1 s ; CONFORME
    | succès : True ; identifiant 77777772 ; message : 
T2-cinq-minutes : code 0 ; 0 s ; CONFORME
    | CONTRÔLE À CINQ MINUTES : CONFORME
T2-surveillance : code 0 ; CONFORME
    | GARDER : fin, code 5 ; second paquet en échec : instance arrêtée par son identifiant, gardée, jamais détruite jusqu'au paquet refait (le run n'est pas rejoué) ; ins
T2-recuperation : code 4 ; 0 s ; CONFORME
    | RÉCUPÉRATION DES TRACES SEULES (AUCUN RUN), SANS LECTURE : TOUS CONFORMES
T2-destruction-refusee : code 2 ; 0 s ; CONFORME
    | REFUS : instance gardée (second paquet en échec) : jamais détruite avant le paquet refait
    instance du code 5 : arrêtée, jamais détruite : CONFORME
T3a-lanceur-refuse : code 2 ; 0 s ; CONFORME
    | instances : non tolérée(s), ou liste illisible (voir les lignes ci-dessus et lancement.txt) : pas de création
    instance gardée : toute création neuve refusée (liste fermée : nœud), branche v3 non créée : CONFORME
T3-lanceur : code 0 ; 1 s ; CONFORME
    | succès : True ; identifiant 77777773 ; message : 
T3-cinq-minutes-ko : code 1 ; 0 s ; CONFORME
    | CONTRÔLE À CINQ MINUTES : 2 KO ; instance 77777773 arrêtée par son identifiant (R10) ; nœud de Lazar
    contrôle à cinq minutes en échec : instance arrêtée, non détruite ; instance gardée de la tentative 2 jamais détruite : CONFORME
    aucun verbe sur les instances tolérées ; destructions : la seule instance de la fin normale : CONFORME
    aucun jeton dans les traces, sorties et états : CONFORME
durée de la répétition : 576 s ; fin : 2026-11-11T14:35:02Z
RÉPÉTITION JOUET DE LA CHAÎNE DE P3-BIS : CONFORME
~~~~

### `repetition-jouet-b.log` (`2e8b76d6ca859e994f3643e34c8f816f9ff85e657c0532c3527e50d20a902a75`, 3942 octets)

~~~~text
début de la répétition : 2026-11-11T14:25:26Z
script éprouvé : lancer_p3bis_v2.sh 029bdb5c114a6166a21fa93724d71a2bf6158dc9686993424f6fbe8462352b08
script éprouvé : controle_cinq_minutes_p3bis_v2.sh 6f9213499687d655e290ab96c1ab8a1cdb9ecd373b1d6beecb7efda962f40864
script éprouvé : surveiller_p3bis_v2.sh d65421073068466a3aa6cc90ef00e6c76b15ea7b3e61e254c1dbafad020afe9b
script éprouvé : recuperation_p3bis_v2.sh 3b21c80cf9a040e779cbea2832f513d299b08c291eeed169cb8d1670df735cd9
script éprouvé : detruire_p3bis_v2.sh cae56ec9cbd00485a9506a1af1bb9dfd8e4b493e966003cb0ed365fe6973ae46
script éprouvé : verifications_p3bis_v2.py 1524df5f6432197fde4793a4fde56d4496407a107c88f5e294a6bc9716923054
script éprouvé : repetition_jouet_p3bis_v2.sh 750ec2530cc4261a57a50a54c062e770e20399127247ba5918fa904267022e02
lignes changées : lanceur 3 (DEPOT, DEPOT_URL, INTERVALLE_OFFRE_S) ; récupération 2 (DEPOT_URL, PY)
commit de scellement de la répétition : 7dc7ac66b58f9e7e78857abc744a8fd47b144208
T1-lanceur : code 0 ; 7 s ; CONFORME
    | succès : True ; identifiant 77777771 ; message : 
    lancement : instance 77777771 écrite, offre 111, branche v1 poussée par l'« instance » : CONFORME
T1-cinq-minutes : code 0 ; 1 s ; CONFORME
    | CONTRÔLE À CINQ MINUTES : CONFORME
T1-surveillance : code 0 ; CONFORME
    | FIN : AMORCE 2026-11-12T12:30:00Z : fin, code 0 ; instance 77777771 arrêtée par son identifiant (R10) ; état relu : actual_status=exited cur_state=stopped intended_sta
    surveillance : PROGRES relevé, dépense relevée sous 80 USD, arrêt par l'identifiant (instance arrêtée) : CONFORME
T1-recuperation : code 0 ; 15 s ; CONFORME
    | RÉCUPÉRATION : TOUS CONFORMES ; paquet des lectures de6324c257580c47e238a74fdea7fb9c627b72f70b39f3b0e58f58da15b1e0b2 poussé sur calcul/p3bis-reel-v1
    récupération : branche distante = commit du seul paquet (16 783 360 octets) et de son compagnon : CONFORME
    récupération : paquet ouvert (jouet) : lecture complémentaire lecture_p3bis_v2, règle (a') sur 800 directions, ancienne règle sur 200, issue « vu », ligne 4 : CONFORME
T1-destruction : code 0 ; 0 s ; CONFORME
    | DESTRUCTION : instance 77777771 détruite par son identifiant (R10), absente de la liste relue
T2-lanceur : code 0 ; 2 s ; CONFORME
    | succès : True ; identifiant 77777772 ; message : 
T2-cinq-minutes : code 0 ; 0 s ; CONFORME
    | CONTRÔLE À CINQ MINUTES : CONFORME
T2-surveillance : code 0 ; CONFORME
    | GARDER : fin, code 5 ; second paquet en échec : instance arrêtée par son identifiant, gardée, jamais détruite jusqu'au paquet refait (le run n'est pas rejoué) ; ins
T2-recuperation : code 4 ; 1 s ; CONFORME
    | RÉCUPÉRATION DES TRACES SEULES (AUCUN RUN), SANS LECTURE : TOUS CONFORMES
T2-destruction-refusee : code 2 ; 0 s ; CONFORME
    | REFUS : instance gardée (second paquet en échec) : jamais détruite avant le paquet refait
    instance du code 5 : arrêtée, jamais détruite : CONFORME
T3a-lanceur-refuse : code 2 ; 0 s ; CONFORME
    | instances : non tolérée(s), ou liste illisible (voir les lignes ci-dessus et lancement.txt) : pas de création
    instance gardée : toute création neuve refusée (liste fermée : nœud), branche v3 non créée : CONFORME
T3-lanceur : code 0 ; 1 s ; CONFORME
    | succès : True ; identifiant 77777773 ; message : 
T3-cinq-minutes-ko : code 1 ; 0 s ; CONFORME
    | CONTRÔLE À CINQ MINUTES : 2 KO ; instance 77777773 arrêtée par son identifiant (R10) ; nœud de Lazar
    contrôle à cinq minutes en échec : instance arrêtée, non détruite ; instance gardée de la tentative 2 jamais détruite : CONFORME
    aucun verbe sur les instances tolérées ; destructions : la seule instance de la fin normale : CONFORME
    aucun jeton dans les traces, sorties et états : CONFORME
durée de la répétition : 576 s ; fin : 2026-11-11T14:35:02Z
RÉPÉTITION JOUET DE LA CHAÎNE DE P3-BIS : CONFORME
~~~~

### `artefacts.log` (`ba1338b3164be26d8e08f7c9eb544e9dabda0e4ad88acb36e2458391f2fadc9e`, 1747 octets)

~~~~text
début des essais complémentaires : 2026-11-11T14:35:24Z
chaîne de l'arbre (b) : c3684087eae9 3b21c80cf9a0 
C1-ancien-banc-controles-contre-chaine-epinglee : essais_controles_p3bis_v2.sh ; code 2 ; CONFORME
    |   File "<stdin>", line 14, in <module>
    | AssertionError: CANDIDAT_RELU_CHEMIN
C2-ancien-banc-recuperation-contre-chaine-epinglee : essais_recuperation_p3bis_v2.sh ; code 2 ; CONFORME
    | lignes changées dans la copie de la récupération : 1 (DEPOT_URL, PY)
    | copie de la récupération non sûre
    artefact : lignes PY= 2
A1-recuperation-deux-lignes-py : essais_recuperation_p3bis_v2.sh ; code 2 ; CONFORME
    | copie de la récupération non sûre : une ligne PY= exigée
A3-repetition-deux-lignes-py : repetition_jouet_p3bis_v2.sh ; code 2 ; CONFORME
    | début de la répétition : 2026-11-11T14:35:25Z
    | copie de la récupération non sûre : une ligne PY= exigée
    artefact : lignes PY= 0
A2-recuperation-sans-ligne-py : essais_recuperation_p3bis_v2.sh ; code 2 ; CONFORME
    | copie de la récupération non sûre : une ligne PY= exigée
    artefact : lignes PY= 2
A4-controles-deux-lignes-py : essais_controles_p3bis_v2.sh ; code 2 ; CONFORME
    |   File "<stdin>", line 14, in <module>
    | AssertionError: PY
    artefact : lignes CODE_RELU= 0
A5-controles-sans-epingle-code-relu : essais_controles_p3bis_v2.sh ; code 2 ; CONFORME
    |   File "<stdin>", line 14, in <module>
    | AssertionError: CODE_RELU
arbre (b) remis : controles_avant_depense_p3bis_v2.sh: OK recuperation_p3bis_v2.sh: OK essais_controles_p3bis_v2.sh: OK essais_recuperation_p3bis_v2.sh: OK repetition_jouet_p3bis_v2.sh: OK 
essais complémentaires non conformes : 0
fin des essais complémentaires : 2026-11-11T14:35:27Z
~~~~

### `codes.txt` (`04801b84967e75f783b56a6f5e5e21d71434f04bc720fc7ca9dd648b8fd67d2a`, 550 octets)

~~~~text
banc-recuperation-a : début 2026-11-11T14:25:26Z ; fin 2026-11-11T14:26:57Z ; code 0
banc-recuperation-b : début 2026-11-11T14:25:26Z ; fin 2026-11-11T14:26:57Z ; code 0
banc-controles-b : début 2026-11-11T14:25:26Z ; fin 2026-11-11T14:27:27Z ; code 0
banc-controles-a : début 2026-11-11T14:25:26Z ; fin 2026-11-11T14:27:27Z ; code 0
repetition-jouet-a : début 2026-11-11T14:25:26Z ; fin 2026-11-11T14:35:02Z ; code 0
repetition-jouet-b : début 2026-11-11T14:25:26Z ; fin 2026-11-11T14:35:02Z ; code 0
six passages finis : 2026-11-11T14:35:02Z
~~~~
