# Contre-lecture CL4 du différentiel v35 → v36 de la prise « idéation » (orchestrateur du pôle v7)

Contre-lecteur neuf (règle R2) : Opus 5.5. Je n'ai écrit ni le code (auteur : une instance Fable 5.1) ni les relectures
précédentes. Relevés `date -u` : début 22:13, fin vers 22:35 UTC, le 28 octobre 2026.

Conditions : aucun réseau, aucune clé, aucun appel payant. Je n'ai rien lu hors de `relecture-v36/` et du kit d'agent de
`venv-pole`. Le seul « Argon » joué est un script factice local (`outils-cl4/argon_factice.py`), qui consigne ce qu'il
reçoit. Chemins : `pole/…`, `demonstrations/…` et `essais/…` désignent l'arbre `v36/orchestrateur-pole-v7/`.

## Verdict : **lançable après corrections**

Le cœur de la v36 tient. J'ai vérifié trois points par exécution :
- Argon ne reçoit, avant l'attestation, ni fiche d'un autre proposeur, ni note, ni classement.
- Sa seconde passe exige l'attestation du matériau.
- Le bras écrit un classement à trois juges : médiane par critère, porte sur l'agrégat, témoins lus chez chacun.

Quatre défauts **majeurs** restent à corriger avant la course, dont trois touchent la dépense ou la décision n° 118 :
- **CL36-01** : le bras se perd pour toujours sur un échec qui n'a rien envoyé à Argon (faute de frappe dans la commande,
  ou variable de clé dans l'environnement). La course est alors perdue.
- **CL36-02** : Argon proposeur ne passe aucun appel de contrôle et tourne après Opus et Fable. Une commande cassée arrête
  donc la course après la dépense Claude de la passe 1.
- **CL36-03** : rien n'impose Argon sur une course réelle. Sans `--juge-externe`, la course écrit un classement lisible à
  deux juges et rend 0.
- **CL36-04** : les plafonds du devis v6 totalisent 17 + 4 = 21 dollars, au-dessus des 20 dollars accordés.

Aucun ne demande de refonte ; une v37 courte et une relecture ciblée suffisent.

## 1. Comptes vérifiés

**Empreintes.**
- `sha256sum -c EMPREINTES-orchestrateur-pole-v7-v36.txt` : **143 sur 143 conformes**, avant et après la relecture.
- Les compagnons `EMPREINTES-…-v36.txt.sha256` et `LISEZMOI-…-v36.md.sha256` sont conformes.
- Une erreur de ma part : trois de mes scripts, lancés sans `-B`, ont créé `pole/__pycache__/` dans l'arbre relu. Je l'ai
  supprimé ; aucun fichier empreinté n'a été touché (vérifié après coup).

**Différentiel.** `diff -rq` v35 ↔ v36 : seuls changent `pole/ideation.py`, `pole/adaptateurs.py`,
`demonstrations/ideation_v1.py` et `essais/test_v7_ideation.py`, plus le LISEZMOI et les empreintes v36. J'ai lu les
quatre fichiers en entier.

**Essais.**
- Commande demandée lancée sous `env -i`, sur une copie de l'arbre (`outils-cl4/copie-essais/`).
- Résultat : **317 essais, 317 réussis**, « OK », 197,6 s, code 0 (`outils-cl4/essais-sortie.txt`). Conforme au LISEZMOI.
- **Essais de mutation** (`outils-cl4/mutations.sh`) : dix défauts réintroduits un par un dans une copie, puis
  `essais.test_v7_ideation` relancé. Résultats au § 2 et en CL36-05.

## 2. Constats CL35-01 à CL35-14

« Discriminant » veut dire que l'essai échoue quand le défaut est réintroduit (mutation Mn) ou que, par construction, il
échouerait sur la v35.

| constat | verdict | preuve | endroit |
|---|---|---|---|
| **CL35-01** coût NaN, manifeste absent | **corrigé** | NaN, infini, 0, négatif et coût absent donnent `erreur` (`adaptateurs.py:423-427`). Le manifeste du bras est écrit avant les fichiers de lecture (`ideation.py:1177`). Essai discriminant par construction (`essais:83-86`). | `adaptateurs.py:411-428` |
| **CL35-02** coût perdu sur une sortie ≠ 0 | **corrigé en partie** | Dans l'adaptateur, le coût imprimé avant un échec est compté, et le plafond est compté s'il est illisible (`:453-463`). Essai discriminant (M5 : 2 échecs). **Reste un trou** : le coût d'un appel de contrôle **échoué** du bras n'entre pas au journal. Démontré en S3 : le message dit « plafond de session compté », mais `cout_total_usd: 0.0`. Voir CL36-01. | `ideation.py:1134-1137` |
| **CL35-03** commande non consignée | **corrigé** | `description()` figure au manifeste de départ (démontré en S1 : commande, empreintes, délai) et au manifeste du bras. Essai discriminant (M10). Réserve : CL36-10. | `ideation.py:770, 1117` |
| **CL35-04** bras simulé sur une course réelle | **corrigé** | Le bras relit `moteur` et `juges_externes` ; les refus tombent avant tout écrit (`ideation.py:1068-1079`). Essai discriminant (M9). Pour le proposeur, M2 fait échouer l'essai, mais **par accident** : le faux adaptateur lève `KeyError` et l'essai ne vérifie aucun appel. | |
| **CL35-05** plafond du bras | **corrigé** | Plafond externe relu au manifeste de départ, vérifié **avant** l'appel de contrôle (`ideation.py:1105-1108`). `PLAFOND_SESSION_USD` et `ROLE_POLE` sont transmis (démontré : la commande factice lit 0,2 au contrôle et 1,5 au jugement). Essai discriminant (absence du dossier de contrôle). | |
| **CL35-06** appel direct | **corrigé en partie** | Un adaptateur principal externe, ou le `.reel` externe d'un adaptateur mixte, est refusé. Essai discriminant (M7). **Reste** deux contournements : un mixte dont la partie **simulée** est la commande, et un nom « claude-sdk » qui suffit. Voir CL36-06. | `ideation.py:651-663` |
| **CL35-07** devis contre lanceur | **corrigé** | Démontré : `--commande-externe` seul est refusé (code 2), de même que commande plus `--juge-externe` seul (code 2). `--variable-transmise GEMINI_API_KEY` est refusé (code 2). **Aucun essai.** | `ideation_v1.py:242-243, 201` |
| **CL35-08** code 1 | **corrigé** | Démontré : moteur réel non armé donne le code 2. **Aucun essai.** | `ideation_v1.py:252-256` |
| **CL35-09** réglages du kit | **corrigé** | `reglages_kit` et `delai_session_s` figurent au manifeste (démontré). `--delai-session-s 0` est refusé (code 2). **Aucun essai.** | `adaptateurs.py:36-39` ; `ideation.py:774` |
| **CL35-10** version de l'outil | **corrigé** | Démontré sur le kit 0.2.174 : `_find_cli()` rend l'outil embarqué (`_bundled/claude`), alors qu'un `claude` est dans `PATH` (`/opt/node22/bin/claude`). **Aucun essai.** | `ideation_v1.py:164-170` |
| **CL35-11** affirmations | **corrigé en partie** | Les passages cités sont réécrits, mais il y a de **nouvelles** contradictions (CL36-11). | |
| **CL35-12** essais | **corrigé en partie** | Les essais de coûts dégénérés, du bras simulé et de la commande consignée sont discriminants. Ceux du délai et du sceau ne le sont pas (CL36-05). | |
| **CL35-13** petit-enfant survivant | **corrigé dans le code** | `start_new_session=True` et `os.killpg` (`adaptateurs.py:438-448`). **Essai non discriminant** (M1, CL36-05). | |
| **CL35-14** attestation | **corrigé dans le code** | `verifier_scelle` dans `_lire_attestation` (`ideation.py:666-674`). La consigne est lue une fois, en octets : empreintée, puis envoyée telle quelle (`:1094-1104, 1144`). **Essai non discriminant** (M8, CL36-05). | |

**Compte : 10 corrigés, 4 corrigés en partie, 0 non corrigé.**
- Parmi les 10 corrigés, 6 n'ont pas d'essai qui sépare le défaut : les essais manquent pour 07 à 10 et ne séparent pas
  le défaut pour 13 et 14.

## 3. Les quatre questions de confinement et de poids

**Confinement.** Démontré en S1 avec la commande factice, qui consigne chaque entrée (`outils-cl4/argon-journal.jsonl`).
- Passe 1 d'Argon : question et pièces seulement. Aucun « ## Les fiches », aucune fiche simulée d'Opus ni de Fable.
- Passe 2 : le matériau attesté et ses propres fiches seulement (`ideation.py:856`).
- Jugement : la consigne scellée, après l'attestation, sans aucune note des juges Claude. Les juges Claude passent après
  toutes les passes de proposition, donc Argon proposeur ne voit jamais leurs notes.
- Sans attestation du matériau, la course refuse avant toute session (S6), mais **après** les appels de contrôle Claude
  (CL36-09).
- Le matériau servi est celui que la liste blanche a vérifié. L'attestation compare l'empreinte par nom de fichier
  (`:743-745`).
- Deux réserves :
  - par appel direct, une commande peut encore juger dans la course (CL36-06) ;
  - le noyau ne confine pas la commande elle-même (CL36-07).

**Poids égal.**
- Agrégat : `statistics.median` dès trois juges (`ideation.py:524`). Porte : `max(médiane avantage, médiane originalité) ≥
  2` (`:530`). Unanimité chez les trois. Accords de rang par paire : 3 paires (démontré en S1-bras).
- Témoins : lus chez les trois (`:1167`), avec `lisible_L2_L4` pris sur les trois (`:1176`, discriminant par M6). Ils sont
  lus aussi chez Argon seul.
- Avant le bras, la course n'écrit ni `classement.json`, ni `classements-par-juge.json`, ni `lecture.json` (essai et S1).
- Panne d'Argon : `classement-sans-bras.json` marqué illisible et code 5 (S3).
- **Reste** : un chemin réel écrit un classement lisible à deux juges si l'option est oubliée (CL36-03).
- **Non couvert** : aucun essai ne vérifie que la médiane est réellement calculée (M3 passe).

**Codes de sortie.** Ils sont cohérents avec le devis :
- course : 0 ou 4 ;
- bras : 0, 4, 5 ou 2.

Deux écarts :
- un refus du plafond **avant** l'appel donne 2, pas 5 (`ideation.py:1106`, hors du `try`) ; c'est sain, car le bras
  reste rejouable, mais le devis (point 4) annonce « plafond → 5 » ;
- une exception autre que `CourseInterrompue` dans le bras donne 2, sans aucun classement, et le bras est perdu
  (CL36-01).

**Argon proposeur.**
- Même consigne utilisateur, mêmes pièces, même nombre, même garde, même quarantaine, même anonymisation (`vue_servie`,
  `normaliser_typographie`).
- Coût compté contre un plafond séparé, et refusé s'il est absent, non fini ou nul.
- Mais la **consigne système** des proposeurs Claude ne lui est pas transmise (CL36-07).

## 4. Constats neufs

### CL36-01 — majeur — Le bras se perd pour toujours sur un échec qui n'a rien envoyé à Argon

**Endroit.** `ideation.py:1132-1137` (appel de contrôle dans le `try`) ; `:1186-1199` (manifeste écrit sur toute
exception) ; `:1047-1049` (manifeste présent → refus définitif) ; `adaptateurs.py:389-395, 435` (variables de clé
vérifiées au lancement seulement).

**Défaut.** Démontré deux fois.
- **S3, faute de frappe dans le chemin du script** :
  - l'appel de contrôle échoue (code 5) ;
  - `classement-sans-bras.json` est écrit ;
  - `manifeste-bras-rapporte.json` existe ;
  - la relance avec la bonne commande est refusée (« déjà joué », code 2).

  Aucune fiche n'a quitté le noyau (la consigne de contrôle est « Réponds exactement OK »). Le coût éventuel du contrôle
  n'est pas compté : le journal donne 0,0, alors que le message dit « plafond de session compté ».
- **S4, `GEMINI_API_KEY` présent dans l'environnement au moment du bras** :
  - `CleDansEnvironnement` est levée au premier lancement, avant tout processus ;
  - le manifeste est écrit avec l'erreur, sans classement d'aucune sorte ;
  - code 2 ;
  - la relance sans la variable est refusée pour toujours.

  La commande factice n'a reçu aucun appel (journal inchangé).

**Conséquence.** La pesée à poids égal décidée par Lazar (n° 118) est perdue pour cette course, et la course (8 à 16
dollars) avec elle. Les deux erreurs sont plausibles chez l'opérateur, qui manipule une clé Gemini ce soir-là. La règle
« jamais rejoué après dépense » s'applique ici à des échecs qui n'ont rien servi.

**Correction.**
- Vérifier `externe.environnement_commande()` et l'existence de l'exécutable **avant** le `try`, à côté du contrôle de
  plafond (`:1105`).
- Ne pas écrire `manifeste-bras-rapporte.json` sur un échec de l'appel de contrôle. Écrire à la place
  `bras-tentative-NN.json`, scellé, avec le coût compté (le plafond de 0,2 s'il est inconnu). Ce coût s'impute au plafond
  externe des tentatives suivantes, au plus deux.
- Garder le refus définitif dès que la consigne qui porte les fiches est partie : un marqueur scellé est écrit juste avant
  `adaptateur.lancer` (`:1144`).
- Essais inverses : commande absente, variable de clé présente, puis rejeu permis ; consigne partie, puis rejeu refusé.

### CL36-02 — majeur — Argon proposeur sans appel de contrôle, joué après Opus et Fable

**Endroit.** `ideation_v1.py:353-356` (contrôle des seuls modèles Claude) ; `ideation.py:729, 845-847` (ordre : Claude,
puis externes).

**Défaut.** Démontré en S5, avec une commande absente :
- le journal donne `opus ok, fable ok, argon erreur (plafond 1,0 compté, coût inconnu)` ;
- la course est arrêtée (code 2).

En réel, la passe 1 d'Opus et de Fable (plafonds 2 + 5 dollars) est déjà payée quand la commande d'Argon échoue pour la
première fois : clé, quota, chemin. Le dossier de sortie est consommé. Sous le plafond accordé de 20 dollars, une
seconde course n'est plus possible.

**Correction.**
- Appel de contrôle de la commande externe avant la course (rôle `proposeur_ideation`), compté dans `cout_externe_usd`
  (nouveau paramètre `cout_externe_deja_engage_usd`).
- Jouer Argon **en tête** de la passe 1 : sa session coûte de 0,3 à 0,8 dollar (estimation du devis, SUPPOSÉE).
- Essai : commande cassée → aucun appel Claude de proposition.

### CL36-03 — majeur — Rien n'impose Argon sur une course réelle ; l'oubli d'une option donne un classement lisible à deux juges

**Endroit.** `ideation_v1.py:264-265, 283-311` (aucune exigence sur `--juge-externe` ni `--proposeur-externe` avec
`--moteur claude-sdk`) ; `ideation.py:921-928` (sans juge externe, la course classe à deux juges et écrit
`classement.json`).

**Défaut.**
- Démontré au cœur (`outils-cl4/appels_directs.py`, cas a) : moteur « claude-sdk », aucun juge externe →
  `classement.json` écrit avec `lisible_L2_L4: true`, deux juges, « moyenne ».
- Démontré au lanceur en simulé (S2) : code 0 et « retenues » imprimées.
- Sur `--moteur claude-sdk`, le lanceur suit le même chemin : aucune ligne ne l'en distingue (lecture de `:283-311`).
- De même, oublier `--proposeur-externe` donne une course où Argon ne propose pas, sans aucune marque d'écart.

C'est exactement le « classement lisible à deux juges » que la décision n° 118 et le devis v6 (point 4) excluent. Le
seul garde est la mémoire de l'opérateur.

**Correction.**
- Sur `--moteur claude-sdk`, exiger au moins un `--juge-externe` et un `--proposeur-externe`, sauf un drapeau explicite
  `--sans-argon MOTIF`, consigné au manifeste.
- Au cœur, sur moteur réel, écrire `classement.json` sans juge externe seulement sous ce drapeau.
- Essai inverse.

### CL36-04 — majeur — Devis v6 : plafonds au-dessus des 20 dollars accordés

**Endroit.** Devis v6, point 1 (« côté Claude 17 », « côté Argon 4 », « Total ≤ 21 ») ; `ideation_v1.py:212-214`
(défauts 17 et 4).

**Défaut.**
- Le directeur a accordé **20 dollars au total**. Les plafonds du devis permettent 21.
- Le noyau réserve, côté Argon, 0,2 (contrôle) + 2 × 1 + 1,5 = 3,7. Côté Claude, il arrête à 17.
- Le pire cas tenu par le noyau est donc ≈ 20,7.
- S'y ajoute ce qu'une session déclare au-delà de son plafond (`budget_depasse`, compté puis arrêt) : le noyau le compte
  mais ne l'empêche pas.

**Correction (devis seulement).**
- `--budget-total-usd 16` et relais `--plafond-usd 16`, puis `--budget-externe-usd 3.7` : pire cas réservé 19,7.
- Écrire dans le devis « total ≤ 20 ».
- Vérifier que 16 laisse passer le dernier juge (le juge Opus passe tant que la dépense ne dépasse pas 14,5 ; l'attendu
  est de 7 à 14).

### CL36-05 — mineur — Essais qui ne séparent pas le défaut

**Endroit.** `essais/test_v7_ideation.py:106-128` (délai), `:291-301` (attestation non scellée), `:267` (médiane
nommée seulement), `:441-445` (proposeur simulé sur une course réelle).

**Défaut, démontré par mutation.**
- **M1** : `os.killpg` remplacé par `p.kill()`. L'essai du délai **passe** en 63 s : `communicate()` attend que le
  petit-enfant finisse ses 60 s, puis l'essai constate qu'il est mort.
- **M3** : médiane remplacée par moyenne. Tout passe : seul le **nom** de l'agrégat est vérifié.
- **M8** : vérification du sceau de l'attestation supprimée. Tout passe : l'attestation « non scellée » de l'essai est
  aussi incomplète, donc elle est refusée pour une autre raison.
- **M2** : l'essai échoue par `KeyError` du faux adaptateur, pas par l'assertion.
- Aucun essai sur le lanceur pour CL35-07 à CL35-10.

**Correction.**
- Borne de durée dans l'essai du délai (retour en moins de délai + 5 s).
- Trois juges dont la médiane ≠ la moyenne, et une porte qui bascule selon l'agrégat.
- Attestation complète mais au sceau faux.
- `self.assertEqual(simule.appels, [])` dans le cas du proposeur.
- Essais de `principal()` pour les refus et les codes.

### CL36-06 — mineur — Par appel direct, une commande externe juge encore dans la course

**Endroit.** `ideation.py:651-663` (seuls `nom` et `reel.nom` sont regardés ; le moteur réel est reconnu au seul nom
« claude-sdk ») ; `adaptateurs.py:338-347`.

**Défaut.**
- Démontré (`appels_directs.py`, cas b) : `AdaptateurMixte(reel=…, simule=AdaptateurCommandeExterne)`. La commande
  reçoit deux consignes de juge qui portent « ## Les fiches », sans aucune attestation. Le coût est **remis à 0** par le
  mixte.
- Démontré (cas a) : un adaptateur simulé nommé « claude-sdk » passe la vérification du moteur réel.

Le lanceur ne peut pas produire ces chemins.

**Correction.**
- Parcourir `reel` **et** `simule`, et refuser toute instance d'`AdaptateurCommandeExterne`.
- Sur moteur réel, exiger `isinstance(adaptateur, AdaptateurClaudeSDK)`.

### CL36-07 — mineur — Le confinement d'Argon repose sur la commande ; la consigne système n'est pas transmise

**Endroit.** `adaptateurs.py:438-439` (`cwd=dossier`, sans bac à sable) ; `ideation.py:831-834` (le dossier
d'Argon est sous la sortie, où les réponses d'Opus et de Fable de la même passe sont déjà écrites :
`proposeurs/<x>/…/reponse.md`) ; `adaptateurs.py:58-68` (consignes système, jamais passées à la commande) ; devis v6,
point 5.

**Défaut.**
- Le devis exige pour Claude « aucun outil » (`tools=[]`), mais rien de tel pour le modèle derrière la commande. Si la
  commande donnait au modèle un accès aux fichiers, rien dans le noyau ne l'empêcherait de lire hors de son dossier
  (non démontré : la commande réelle est hors de mon périmètre).
- « Même consigne » n'est vrai que pour la consigne utilisateur. La consigne système (niveau méthode, aucune recherche,
  juge aveugle) n'est pas transmise à Argon.

**Correction.**
- Lancer la commande dans un dossier temporaire vide, hors de la sortie.
- Ajouter au devis : « la commande n'expose aucun outil au modèle, n'utilise aucun cache de conversation entre appels ».
- Transmettre la consigne système, en préfixe ou par fichier, et la consigner.

### CL36-08 — mineur — Une dépense réelle d'Argon est marquée fictive

**Endroit.** `ideation_v1.py:314-321` (`--commande-externe` accepté avec le moteur simulé, qui est la valeur par défaut) ;
`ideation.py:749` (`cout_fictif = not reel`).

**Défaut.** Démontré en S1 : course simulée, commande appelée deux fois, `cout_externe_usd: 0.6`, `cout_fictif: true`. Une
répétition avec la vraie commande dépenserait chez Argon sans que la dépense soit consignée comme réelle. Le bras du même
dossier, lui, marque `cout_fictif: false`.

**Correction.** Refuser `--commande-externe` avec le moteur simulé, sauf drapeau explicite. Sinon, consigner un
`cout_externe_fictif` distinct.

### CL36-09 — mineur — Des refus tombent après les appels de contrôle Claude

**Endroit.** `ideation_v1.py:353-357` (contrôle avant `executer_ideation`) ; `ideation.py:702-745`.

**Défaut.** Démontré :
- S6 : l'attestation du matériau absente est refusée, mais `S6-controle/` existe déjà ; le contrôle est fait.
- S8 : `--budget-externe-usd nan` est refusé par `ValueError` à l'écriture du manifeste. Les contrôles sont faits, et le
  dossier `S8` est créé, donc consommé.

La docstring et le devis disent « refus avant tout appel ».

**Correction.**
- Une fonction `verifier_reglages(...)` du cœur, appelée par le lanceur **avant** le contrôle : liste blanche, pièces,
  attestation, étiquettes, plafonds.
- `math.isfinite` sur tous les plafonds.

### CL36-10 — mineur — Commande consignée, mais ni résolue ni comparée entre la course et le bras

**Endroit.** `adaptateurs.py:404-409` ; `ideation.py:1114-1118`.

**Défaut.**
- Un programme nommé par `PATH` (`python3`, `argon`) n'est pas empreinté (`os.path.isfile` est faux).
- Le bras ne compare pas sa commande à `depart.commande_externe`. Un script modifié entre la course et le bras passe
  sans marque.

**Correction.**
- Résoudre `commande[0]` par `shutil.which` et l'empreinter.
- Dans le bras, refuser un écart, ou le marquer.

### CL36-11 — mineur — Contradictions et lectures manquantes

**Endroit et défaut.**
- `ideation.py:8` (« agrège (moyenne par critère) ») et `:44-46` (« bras rapporté … ses notes ne sont jamais
  agrégées ») contredisent la v36.
- Lanceur, `:19` : `--juge-externe argon=…` ; devis : `argon-juge=…`.
- Devis, point 4 : « plafond → 5 », alors que le refus avant appel rend 2.
- La lecture L5 du devis lit « l'agrégat des deux juges Claude », que le code n'écrit pas : il n'y a que des classements
  par juge.
- `notes-par-juge.json`, désanonymisé par auteur, est lisible avant le bras : un classement à deux juges s'en calcule à
  la main. À dire dans le devis.
- Le bras ne relève pas les signaux de la garde sur la réponse d'Argon juge (`:1149` contre `:810`).
- Le bras se joue, et se paie, même si la course a déjà échoué sur ses témoins (code 4), ce qui rend le résultat
  illisible d'avance.

**Correction.**
- Réécrire ces passages.
- Écrire `agregat-deux-juges-claude.json`, marqué « pour L5 seulement, jamais un classement ».
- Bras sur course à témoins échoués : seulement sous drapeau.

### CL36-12 — mineur (latent) — Étiquette contenant « -p » : auto-préférence mal attribuée

**Endroit.** `ideation.py:554` (`ident.split("-p")[0]`).

**Défaut.** Démontré (cas c) : le proposeur « argon-pro », jugé par Argon, est compté « autre modèle ». Ce défaut est
latent avec les étiquettes du devis (opus, fable, argon).

**Correction.** Prendre `auteur` dans la fiche, ou refuser « -p » dans les étiquettes.

**Compte des constats neufs : 0 bloquant, 4 majeurs (CL36-01 à 04), 8 mineurs (CL36-05 à 12).**

## 5. Le devis v6 au regard du code

| point | code | verdict |
|---|---|---|
| 1. Plafonds séparés 17 / 4 | défauts `ideation_v1.py:212-214` ; sessions Argon 1 et 1,5 (`:267-270`) | conforme au code ; **au-dessus du plafond accordé de 20** (CL36-04) |
| 1. `PLAFOND_SESSION_USD` passé | `adaptateurs.py:398-399` | conforme (démontré) |
| 2. Proposeur Argon dans la course, attestation du matériau scellée | `ideation.py:736-745` | conforme ; refus après les contrôles Claude (CL36-09) ; aucun contrôle d'Argon avant la dépense (CL36-02) |
| 2. Clé par `--variable-transmise`, nom de clé refusé | `ideation_v1.py:201`, `adaptateurs.py:386` | conforme (démontré) |
| 2. Clé « interdite en lecture aux agents Claude » | `interdits` = sortie, sortie-controle, dépôt, `~` (`ideation_v1.py:303`) | vrai seulement si le fichier est sous l'un d'eux (`~`, par exemple) ; `tools=[]` couvre le reste |
| 3. Aucun classement avant le bras ; trois juges ; médiane | `ideation.py:912-920, 1163-1183` | conforme ; mais l'oubli de `--juge-externe` donne un classement lisible à deux juges (CL36-03) |
| 4. Codes 0, 4, 5, 2 ; aucun repli | lanceur `:335-350, 375-386` | conforme, sauf « plafond → 5 » (c'est 2 avant appel) et le bras perdu en code 2 (CL36-01) |
| 5. Coût toujours présent, fini, > 0 ; groupe de processus arrêté | `adaptateurs.py:411-468` | conforme |
| 6. L0 chez les trois ; L3 accords par paire | `ideation.py:1167-1176, 954` | conforme ; L5 sans fichier (CL36-11) |
| 7. Ordre | — | ajouter : v37, relecture ciblée, **répétition de la commande d'Argon** (contrôle seul) avant la course |

## 6. Ce que je n'ai pas pu vérifier

- **La commande réelle d'Argon** : outils exposés au modèle, cache entre appels, journalisation du modèle servi, barème,
  coût déclaré contre coût facturé. Le noyau ne compte que le coût **déclaré** par la commande.
- **L'outil en ligne de commande réel** : `--tools ''`, coupure au plafond, compte du relais quand une session est
  interrompue. Rien n'a été lancé.
- **La lecture humaine et l'identité des lecteurs** des deux attestations : c'est une procédure, hors du code.
- **La fenêtre entre vérification et lecture d'une pièce** (`verifier_pieces` puis `open`, `ideation.py:191, 210`) : elle
  est théorique, de l'ordre de la milliseconde, et je ne l'ai pas exercée.

## 7. Fichiers produits

Tous sous `relecture-v36/` :
- Rapport : `contre-lecture-v36-cl4.md`.
- Scripts : `outils-cl4/`
  - `preparer_entrees.py` ;
  - `argon_factice.py` (local, consigne ses entrées dans `argon-journal.jsonl`) ;
  - `attester.py` ;
  - `appels_directs.py` et sa sortie ;
  - `mutations.sh` ;
  - `essais-sortie.txt` ;
  - `copie-essais/` (à supprimer à volonté).
- Courses simulées : `simulee/`
  - S1 : nominale, avec proposeur et juge externes ;
  - S1-bras : trois juges, code 0 ;
  - S1-script : bras scripté sur une course simulée, code 0 ;
  - S2 : sans juge externe, code 0 ;
  - S3 : faute de frappe, code 5, puis relance refusée ;
  - S4 : variable de clé, code 2, bras perdu ;
  - S5 : Argon en panne après Opus et Fable ;
  - S6 : attestation absente, après contrôle ;
  - S8 : NaN ;
  - D-a et D-b : appels directs.
- Aucun processus laissé actif (vérifié par `ps`).
