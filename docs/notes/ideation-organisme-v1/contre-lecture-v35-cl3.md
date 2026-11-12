# Contre-lecture CL3 du différentiel v34 → v35 de la prise « idéation » (orchestrateur du pôle v7)

Je suis un contre-lecteur neuf (règle R2) : Opus 5.5. Je n'ai écrit ni le code relu (auteur : une instance Fable 5.1) ni
la relecture CL2. Relevés `date -u` : début 20:39, fin 20:50 UTC, le 28 octobre 2026.

Conditions de travail :
- aucun appel payant, aucun réseau, aucune clé ;
- rien de lu hors du dossier `relecture-v35/` et du kit d'agent installé dans `venv-pole` ;
- moteur simulé seulement. Le seul « juge externe » joué est un script factice local (`outils-cl3/argon_factice.py`).
  Le seul « outil en ligne de commande » lancé est un faux, local, qui pend (`outils-cl3/faux-cli/claude`).

Chemins : `pole/…`, `demonstrations/…` et `essais/…` désignent les fichiers sous `v35/orchestrateur-pole-v7/`. Mes
courses simulées sont sous `relecture-v35/simulee/` (cas A à D4) et mes scripts sous `relecture-v35/outils-cl3/`.

## Verdict : **lançable après corrections**

Aucun bloquant. Le bras d'Argon (le juge externe) ne peut plus lire les fiches pendant la course par le lanceur, et
« aucun outil » est réellement appliqué par le kit d'agent. Mais quatre défauts majeurs touchent le bras différé :
- un coût « pas un nombre » (NaN) passe ;
- un coût imprimé avant une sortie en échec n'est pas compté ;
- la commande d'Argon n'est consignée nulle part ;
- un bras simulé peut se jouer sur une course réelle et condamner le vrai.

Ces quatre défauts se corrigent en une vingtaine de lignes, puis une relecture ciblée v35 → v36. Il faut les corriger
avant la course et non entre la course et le bras, sinon les deux étapes tournent sur deux versions du code.

## 1. Comptes vérifiés

**Empreintes.** `sha256sum -c EMPREINTES-orchestrateur-pole-v7-v35.txt` donne **142 sur 142 conformes**, avant et après
ma relecture. Le compagnon `.sha256` est conforme (`87a59167…`), de même que `LISEZMOI-…-v35.md.sha256`. Aucun fichier de
l'arbre relu n'a été modifié ni ajouté (`find -newer` est vide).

**Différentiel.** `diff -rq` v34 ↔ v35 : seuls changent `pole/ideation.py`, `pole/adaptateurs.py`,
`demonstrations/ideation_v1.py` et `essais/test_v7_ideation.py`, plus le LISEZMOI et les empreintes v35. Les quatre
fichiers changés ont été lus en entier.

**Essais.** J'ai lancé la commande demandée, sous `env -i`, sur une **copie octet pour octet** de l'arbre v35
(`outils-cl3/copie-essais/`), pour ne pas créer `essais/_tmp` dans l'arbre relu. Résultat : **312 essais, 312 réussis**,
« OK », 165,8 s, code 0. Sortie complète : `outils-cl3/essais-sortie.txt`. Cela confirme l'annonce du LISEZMOI v35.

## 2. Constats CL34-01 à CL34-14

« Démontré » signifie que je l'ai exécuté. « Discriminant » signifie que l'essai échouerait sur la v34, donc qu'il sépare
le cas sain de l'artefact.

| constat | verdict | preuve | endroit |
|---|---|---|---|
| **CL34-01** Argon avant la lecture humaine | **corrigé** (réserve : CL35-06) | Le cœur refuse l'attestation (`ideation.py:660-662`). L'adaptateur externe passé à la course n'est jamais appelé : `_adaptateur_externe` est inutilisé, seule la consigne est écrite, scellée (`:815-825`). Le lanceur refuse l'attestation sans `--bras-rapporte-differe` (`ideation_v1.py:227-228`). Démontré : cas A2 → code 2 ; cas A, avec `--commande-juge-externe` → **0 réception**. **Rejeu** : refusé si le manifeste du bras ou `reponse.md` existe (`:953-956`, `:993-994`) ; démontré en B1bis et B4, aucune nouvelle réception. **Sortie modifiée après l'attestation** : l'attestation lie l'empreinte des fiches et celle de la consigne réellement envoyée (`:960-961`, `:985-992`). Essai discriminant (`test_v7_ideation.py:529-536`). **Reste un chemin par appel direct** (CL35-06). | `ideation.py:660, 811-825, 953-998` |
| **CL34-02** aucun outil | **corrigé** | Ligne de commande construite, jamais exécutée (`cli_path=/bin/true`) pour `proposeur_ideation` et `juge_ideation`. Démontré : `--tools ''`, `--allowedTools` **absent**, `--effort high` ou `medium`, `--setting-sources=` vide. Aucun `--mcp-config`, `--plugin-dir` ni `--add-dir`. `skills=None`, `mcp_servers={}`, `can_use_tool=None`, `agents=None`. Le crochet n'est qu'un `PreToolUse` : il filtre, il n'ajoute rien. Le bac à sable et `dontAsk` ne créent pas d'outil. L'aide de l'outil embarqué dit : `Use "" to disable all tools`. Essai discriminant (`:637-655`). | `adaptateurs.py:208-212, 257-267` ; `outils-cl3/ligne-commande-kit-sortie.txt` |
| **CL34-03** coût manquant | **corrigé en partie** | Démontré (`outils-cl3/cout-externe-sortie.txt`). Absent, `null`, chaîne, négatif, booléen ou liste donnent `erreur`. Mais **NaN donne `ok`** avec un coût NaN ; `Infinity` donne `budget_depasse` avec un coût infini ; **0 donne `ok`** ; une sortie ≠ 0 avec `cout_usd: 1.9` imprimé compte **0**. L'essai ne couvre que le cas « absent » (`:508`). | `adaptateurs.py:396-414` → CL35-01, CL35-02 |
| **CL34-04** bras différé | **corrigé en partie** | Faits : appel de contrôle d'Argon, compté (démontré en B3 : 0,002 + 0,3 = 0,302) ; rejeu refusé ; sceaux vérifiés ; consigne attestée ; témoins lus chez Argon (B3 : `temoins_ok_bras_rapporte: true`) ; course en erreur → aucun bras (`:974-975`). Non faits : le plafond de session n'est **pas transmis** à la commande, il n'est vérifié qu'après coup (`adaptateurs.py:411`) ; le plafond total est vérifié **après** l'appel de contrôle (`:1009-1022`) ; le manifeste n'est **pas** écrit sur tous les chemins (B1, CL35-01) ; un bras simulé peut se jouer sur une course réelle (D3, CL35-04) ; la commande n'est pas consignée (CL35-03). Essai discriminant pour le rejeu, les témoins et le plafond imposé (`:518-604`). | `ideation.py:931-1066` |
| **CL34-05** borne de temps | **corrigé** | **Démontré sur un faux outil en ligne de commande qui pend** : délai 3 s ; le sous-processus du kit est arrêté avant le retour (8 s si l'outil accepte la demande d'arrêt, 13 s s'il l'ignore : arrêt forcé). Aucun orphelin après la fin de l'interpréteur (`outils-cl3/borne_temps.py`). Le kit avertit pourtant qu'une annulation `asyncio.wait_for` peut sauter l'escalade (`subprocess_cli.py:979-988`) : le comportement tient ici, mais **l'essai v35 ne le couvre pas**. Son faux kit n'a pas de sous-processus (`:657-683`). | `adaptateurs.py:282, 286-312` → CL35-12 |
| CL34-06 lectures interdites | **corrigé** | `SORTIE-controle` est dans les interdits. Démontré : un dossier de contrôle sous `SORTIE-controle` est accepté par `construire_options`. `--racine-depot` est consigné (`versions.racine_depot`). Le repli « cinq niveaux » est consigné mais non refusé. | `ideation_v1.py:137-149, 270-274` |
| CL34-07 plafond | **corrigé** | Défaut 17 (`ideation_v1.py:202`). Le coût des contrôles est passé à la course, compté au journal et dans le plafond (`ideation.py:681-682`). Essai discriminant (`:698-714`). Seul le coût **déclaré** des contrôles est compté, pas l'écart lu au relais (`ideation_v1.py:325`) : mineur. | |
| CL34-08 effort | **corrigé en partie** | L'effort est transmis (démontré : `--effort`). En revanche, il n'est **pas** consigné au manifeste de départ, contrairement à ce qu'écrit `adaptateurs.py:29`. Il n'y apparaît qu'à travers l'empreinte du code. | CL35-09 |
| CL34-09 manifeste et environnement | **corrigé en partie** | Faits : environnement minimal (`adaptateurs.py:374-383`, essai `:606-620`) ; `ProxyHandler({})` (`ideation_v1.py:129`) ; manifeste de fin sur toute exception de la course (`ideation.py:859-869`, essai `:716-728`). Non faits : la **commande d'Argon n'est jamais consignée** (CL35-03) ; la version consignée peut ne pas être celle de l'outil lancé (CL35-10) ; le lanceur rend **1**, avec une trace, sur certaines exceptions (CL35-08). | |
| CL34-10 garde | **corrigé** (signal assumé) | Pluriels ajoutés (`ideation.py:86-94`). Taux de quarantaine par proposeur (`:883-890`). Essai discriminant (`:685-689`). | |
| CL34-11 `--nombre` | **corrigé** | Refus au cœur (`ideation.py:657-659`) et au lanceur (`ideation_v1.py:229-230`). Démontré : cas A3 → code 2. Essai discriminant (`:703-705`). | |
| CL34-12 témoins | **corrigé** (code : rapport seulement) | `_longueurs_temoins` (`ideation.py:872-880`). L'essai vérifie seulement la présence d'une clé (`:336`) : faible (CL35-12). Les noms neutres sont une consigne au tiers (devis v5, point 4), sans contrôle par le code. | |
| CL34-13 affirmations | **corrigé en partie** | `complet` et le code 3 sont retirés. Mais il y a de **nouvelles** affirmations fausses (CL35-11). | |
| CL34-14 lot | **non vérifiable ici** | Le lot `livrables/lot-ideation-tournoi-v35-v1.zip` est hors du périmètre que j'ai le droit de lire. | — |

**Compte : 9 corrigés, 4 corrigés en partie, 0 non corrigé, 1 non vérifiable.**

## 3. Constats neufs

### CL35-01 — majeur — Un coût « pas un nombre » est accepté ; le manifeste du bras n'est alors pas écrit

**Endroit.** `adaptateurs.py:408-414` ; `ideation.py:1019`, `:1030`, `:1059`, `:1064-1065` ; `outils.py:68`
(`allow_nan=False`).

**Défaut.** Un coût NaN donne le statut `ok`.
- `deja + NaN + plafond > total` est toujours faux : la garde du plafond total est **sans effet** dès qu'un coût NaN est
  au journal (pour un second juge externe, ou si l'appel de contrôle en déclarait un ; le contrôle exige pourtant un
  coût > 0, donc il refuse NaN).
- `Infinity` donne un coût infini.
- **Démontré (B1)** : Argon factice qui rend des notes valides avec `"cout_usd": NaN` → `ValueError` à l'écriture du
  manifeste, puis encore dans le `except`. Résultat : **aucun `manifeste-bras-rapporte.json`**, mais
  `notes-bras-rapporte.json`, `lecture-bras-rapporte.json` et `classements-…` sont **écrits et scellés**. Ils ressemblent
  à un succès et n'ont aucun coût consigné. Code 2, avec le message « le manifeste du bras est déjà écrit » faux
  (`ideation_v1.py:308`).
- La relance est refusée, ce qui est juste, car `reponse.md` existe.

**Correction.**
- Dans `AdaptateurJugeExterne.lancer` : `math.isfinite(cout)` exigé, sinon `erreur`.
- Côté réel, `cout > 0` exigé (un appel facturé ne coûte jamais 0).
- Écrire le manifeste avant les fichiers de lecture.
- Essais inverses : NaN, `Infinity`, 0.

### CL35-02 — majeur — Le coût d'Argon est perdu sur une sortie en échec

**Endroit.** `adaptateurs.py:394-398` (sortie ≠ 0 ou délai dépassé → coût 0,0) ; `ideation.py:1030`.

**Défaut.** Le devis v5 (point 2) exige que la commande « imprime **toujours** `cout_usd` et sorte ≠ 0 sur tout échec ».
Le code ignore justement ce coût quand la sortie est ≠ 0. Ce qu'Argon a dépensé avant d'échouer est compté 0 : c'est un
repli silencieux sur une dépense.
- **Démontré (B2)** : la commande imprime `cout_usd: 1.9` puis sort en code 3 → journal du bras `[('erreur', 0.0)]`, coût
  total compté 0,002 (le contrôle seul).
- Sur un délai dépassé, le coût est inconnu et compté 0, sans marque.

**Correction.**
- Sur une sortie ≠ 0, lire la dernière ligne si elle est conforme et prendre son coût.
- Sinon, compter le **plafond de session** comme coût pessimiste et le marquer `cout_inconnu`.
- Même règle sur un délai dépassé.

### CL35-03 — majeur — La commande d'Argon n'est consignée nulle part

**Endroit.** `ideation_v1.py:283-297, 300-314, 336` ; `ideation.py:1003-1007`.

**Défaut.** `commande_externe` n'est renseignée que sur le chemin du bras. Ce chemin retourne **avant**
`executer_ideation`, et `executer_bras_rapporte` ne la reçoit pas. Le manifeste de départ porte donc toujours
`commande_externe: None` (démontré, cas A). Le manifeste du bras ne porte que `[argon, gemini-argon, "juge-externe"]`
(démontré, cas B3). La correction CL34-09 sur ce point est du code mort.

L'identité du script qui a parlé à Argon, son empreinte et ses arguments ne sont donc pas consignés, contrairement à la
règle R6 et au manifeste par exécution de R9.

**Correction.** Passer `description_commande_externe(commande)` à `executer_bras_rapporte` et l'écrire dans
`manifeste-bras-rapporte.json`, avec l'environnement transmis (noms seulement). Essai qui l'exige.

### CL35-04 — majeur — Un bras **simulé** se joue sur une course **réelle** et condamne le vrai bras

**Endroit.** `ideation_v1.py:291-292` (repli : juge externe scripté quand la commande manque et que `--moteur` vaut
`simule`, la valeur par défaut) ; `ideation.py:931-1000` (le moteur de la course n'est jamais relu).

**Défaut.** La commande du bras documentée dans le LISEZMOI ne donne pas `--moteur`, donc le moteur vaut `simule`. Si
l'opérateur oublie `--commande-juge-externe`, le juge scripté note la course réelle.
- **Démontré (D3)** : course marquée `moteur: claude-sdk` au manifeste, puis bras sans commande → **code 0**. Des notes
  fictives sont scellées sous les noms réels (`notes-bras-rapporte.json`). Un « coût » de 0,6 est compté sans marque
  « fictif ». Le manifeste du bras ne porte que `simule-ideation` dans `juges`.
- Le vrai bras est ensuite **refusé pour toujours** (D3bis : « déjà joué »). Il ne peut se rejouer qu'en supprimant un
  fichier scellé, ce que la règle R12 interdit.

**Correction.**
- `executer_bras_rapporte` relit `depart["reglages"]["moteur"]` ; si c'est `claude-sdk`, il refuse tout adaptateur qui
  n'est pas une commande externe, **avant** tout écrit.
- Marquer `cout_fictif` dans le journal du bras.
- Vérifier aussi que le modèle donné pour chaque étiquette est celui de la course (`juges_externes_bras_rapporte`).

### CL35-05 — mineur — Plafond du bras : vérifié après l'appel de contrôle, partagé avec la course, sans réglage

**Endroit.** `ideation.py:976, 1009-1022` ; `ideation_v1.py:307` (`budget_total_usd=None` imposé) ;
`adaptateurs.py:385-414` (le plafond n'est pas passé à la commande).

**Défaut.**
- Argon est compté contre le **même** total de 17 que la part Claude. Si la course coûte plus de ≈ 13,8 dollars
  (17 − 3 − 0,2), l'appel de contrôle d'Argon est payé, puis le bras est refusé et marqué joué : il ne peut plus jamais
  se jouer.
- `--budget-total-usd` est ignoré en silence sur ce chemin.
- Le plafond de session (3) n'est qu'un constat après coup : la commande ne le reçoit pas.

**Correction.**
- Vérifier `deja + contrôle + session ≤ total` **avant** l'appel de contrôle.
- Faire lire `--budget-total-usd` par le bras, ou écrire dans le devis que le total de 17 inclut Argon.
- Passer le plafond à la commande (argument ou variable).

### CL35-06 — mineur — Un chemin par appel direct sert encore les fiches à une commande externe pendant la course

**Endroit.** `ideation.py:639-680` (aucune vérification sur l'adaptateur principal ni sur les modèles des juges) ;
`adaptateurs.py:330-332`.

**Défaut.** Le chemin est le suivant : `executer_ideation` reçoit un `AdaptateurMixte` dont le rôle réel
`juge_ideation` est un `AdaptateurJugeExterne`.
- **Démontré (D4a et D4b)** : la commande factice reçoit la consigne avec « ## Les fiches », sans aucune attestation.
- Cela vaut même sous une étiquette de modèle Claude (`("juge-opus", "claude-opus-5-5")`) : le nom de modèle n'est
  qu'une étiquette.
- De même, `moteur` est une chaîne libre, non liée à l'adaptateur (D3).

Le lanceur ne peut pas produire ce chemin, d'où la gravité mineure. Mais la phrase « la course n'appelle jamais un juge
externe » n'est vraie que par le lanceur.

**Correction.**
- Refuser dans `executer_ideation` tout adaptateur, ou tout `.reel` d'un adaptateur mixte, dont `nom == "juge-externe"`.
- Si `moteur == "claude-sdk"`, exiger un `AdaptateurClaudeSDK` et `verifier_modele_reel` sur chaque juge.
- Essai inverse.

### CL35-07 — mineur — Contradictions entre le devis v5 et le lanceur

**Endroit.** Devis v5, point 2 ; `ideation_v1.py:283-297, 289`.

**Défaut.**
- (a) Le devis dit `--commande-juge-externe` « **refusé** » dans la course. Le lanceur l'**accepte et l'ignore** en
  silence (démontré, cas A : code 0, aucun appel, rien consigné).
- (b) Le devis fait passer le chemin du fichier de clé « par `variables_transmises` ». Le lanceur construit
  `AdaptateurJugeExterne(commande)` **sans** `variables_transmises`, et aucune option ne les expose. La commande ne reçoit
  que `PATH`, `HOME`, `LANG`, `LC_ALL` et `TMPDIR`. Le mode opératoire du devis est donc inapplicable tel quel.
  L'opérateur improvisera, par exemple en passant le chemin de la clé en argument.

**Correction.**
- Refuser `--commande-juge-externe` hors du bras.
- Ajouter `--variable-transmise NOM` (répétable), refusée si c'est un nom de clé.
- Ou corriger le devis.

### CL35-08 — mineur — Le lanceur ne rend pas 2 sur toute exception

**Endroit.** `ideation_v1.py:255-257` (`MoteurNonArme` levée hors de tout `try`) ; `:319-324` (seule
`CourseInterrompue` est rattrapée autour de l'appel de contrôle) ; `:275-276`.

**Défaut.**
- Démontré : `--moteur claude-sdk` sans confirmation → trace et **code 1**.
- Par lecture, non démontré : une erreur de lecture du relais (`URLError`) ou `CleDansEnvironnement` pendant l'appel de
  contrôle, ou un délai négatif, sortent aussi en code 1 avec une trace.

Ces sorties ne dépensent rien, mais le LISEZMOI v35 annonce « le lanceur rend 2 sur toute exception » et le devis ne
prévoit que les codes 0, 4 et 2.

**Correction.** Envelopper tout `principal` après l'analyse des arguments.

### CL35-09 — mineur — Réglages du kit non consignés ; délai nul remplacé en silence

**Endroit.** `ideation.py:685-705` ; `adaptateurs.py:29` ; `ideation_v1.py:276`.

**Défaut.**
- `effort`, `tools` et le délai de session effectif n'apparaissent pas dans `manifeste-depart.json` (liste des clés
  relevée sur le cas A).
- `--delai-session-s 0` donne 1800 sans message (démontré).

**Correction.** Consigner `{role: {tools, effort}}` et `delai_s`. Refuser un délai ≤ 0.

### CL35-10 — mineur — La version consignée de l'outil en ligne de commande peut ne pas être celle qui tourne

**Endroit.** `ideation_v1.py:156-169`.

**Défaut.** Le lanceur interroge d'abord `shutil.which("claude")`. Or le kit 0.2.174 lance d'abord l'outil **embarqué**
(`subprocess_cli.py:257-260`). Si un `claude` est dans `PATH`, le manifeste consigne la mauvaise version.

**Correction.** Interroger `_find_cli()` d'abord, ou seul, et consigner son chemin.

### CL35-11 — mineur — Nouvelles affirmations fausses

**Endroit et défaut.**
- `adaptateurs.py:29` : effort « consigné au manifeste de départ », ce qui est faux (CL35-09).
- `ideation_v1.py:196` : l'aide de `--attestation-lecture-humaine` omet `consignes_en_attente_sha256`, qui est
  obligatoire.
- `ideation_v1.py:308` : « le manifeste du bras est déjà écrit », faux sur les refus d'avant le `try` (attestation
  illisible, sceau faux) et en B1.
- LISEZMOI v35, ligne CL34-09 : « commande du juge externe et empreinte de ses arguments-fichiers » au manifeste, faux
  (CL35-03).
- Docstring de `executer_bras_rapporte` (`ideation.py:944-945`) : « écrit sur tous les chemins », faux (CL35-01).

**Correction.** Réécrire ces passages.

### CL35-12 — mineur — Essais qui ne séparent pas le défaut

**Endroit et défaut.**
- `test_borne_de_temps_par_session` (`:657-683`) : faux kit sans sous-processus. Il passerait même si l'outil en ligne de
  commande restait vivant.
- `:336` : vérifie seulement la présence de la clé `temoins_hors_fourchette`.
- Aucun essai sur un coût NaN, infini, nul ou imprimé avant une sortie ≠ 0.
- Aucun essai sur un bras simulé joué sur une course réelle, ni sur la consignation de la commande.
- `:460-467` vérifie encore `allowed_tools == []`, sans objet depuis `tools=[]` (inoffensif).

**Correction.** Reprendre mes scripts `outils-cl3/borne_temps.py`, `cout_externe.py` et `appel_direct.py` en essais
inverses.

### CL35-13 — mineur — Délai de la commande d'Argon : un petit-enfant survit

**Endroit.** `adaptateurs.py:392-395` (`subprocess.run(..., timeout=…)` n'arrête que le fils direct).

**Défaut.** Démontré : une commande enveloppée par un interpréteur de commandes qui lance un « appel » long rend
`erreur` au bout de 2 s, mais le **petit-enfant reste vivant**. Je l'ai arrêté ensuite par son identifiant de processus
(1838). Si la commande d'Argon est un enveloppeur, l'appel continue et peut dépenser, sans être compté (CL35-02).

**Correction.** `start_new_session=True` et arrêt du groupe de processus (`os.killpg`) sur le délai. Ou exiger, dans le
devis, une commande sans enveloppeur.

### CL35-14 — mineur — Attestation non scellée, lue deux fois

**Endroit.** `ideation.py:957-958, 987-998`.

**Défaut.**
- Le sceau de l'attestation n'est pas vérifié, alors que le devis v5 (point 3) dit « scellée ».
- La consigne est empreintée puis relue : deux lectures du même fichier, avec un écart théorique entre la vérification et
  l'usage.

**Correction.** `verifier_scelle(attestation)` ; lire les octets une fois, empreinter ces octets et envoyer ces mêmes
octets.

**Compte des constats neufs : 0 bloquant, 4 majeurs (CL35-01 à 04), 10 mineurs (CL35-05 à 14).**

## 4. Le devis v5 au regard du code

| point du devis | code | verdict |
|---|---|---|
| 1. Total côté Claude 17 au noyau (défaut) | `ideation_v1.py:202` | conforme |
| 1. Relais `--plafond-usd 17 --reserve-par-appel 3.5` | relevant de l'opérateur ; `relais_reel.py` inchangé | non vérifiable par le code |
| 1. Contrôles comptés dans les 17 | coût déclaré seulement | conforme, avec la réserve de CL34-07 |
| 1. Argon ≤ 3, « tenu par le plafond de session » | constat après coup seulement ; Argon partage le total de 17 | en partie (CL35-05) |
| 2. Commande refusée dans la course | acceptée et ignorée | **non conforme** (CL35-07a) |
| 2. Clé passée par `variables_transmises` | non exposé par le lanceur | **inapplicable** (CL35-07b) |
| 2. Environnement minimal | conforme | conforme |
| 2. Coût toujours imprimé, sortie ≠ 0 sur échec | coût ignoré sur sortie ≠ 0 | **contradiction** (CL35-02) |
| 3. Attestation : champs exigés et vérifiés | conforme | conforme |
| 3. Attestation « scellée » | sceau non vérifié | en partie (CL35-14) |
| 3. Bras joué une fois, avec son contrôle et la relecture des témoins | conforme | conforme, sauf CL35-04 |
| 3. Manifeste du bras « sur tous les chemins » | non (CL35-01) | **non conforme** |
| 4. Quatre classes de témoins imposées | conforme | conforme |
| 4. Noms neutres, longueurs | rapport seulement | conforme : c'est la tâche du tiers |
| 5. `--racine-depot` et `versions.racine_depot` | conforme | conforme |
| 5. `--delai-session-s 1800` (défaut) | conforme, mais non consigné | en partie (CL35-09) |
| 5. Version de l'outil au manifeste | peut viser un autre binaire | en partie (CL35-10) |
| 7. Ordre de lancement | cohérent | ajouter : v36, puis relecture ciblée, avant les pièces |

La somme des plafonds de session Claude vaut 2 + 5 + 2 + 5 + 3 + 1,5 = 18,5 dollars, au-dessus du total de 17. Le noyau
arrête avant une session si la dépense comptée plus le plafond de cette session dépasse 17. Les deux derniers juges
passent tant que la dépense ne dépasse pas 14 avant le juge Fable, puis 15,5 avant le juge Opus. C'est cohérent avec
l'attendu de 7 à 14 dollars. Mais le haut de cette fourchette rejoint le seuil de 13,8 au-delà duquel Argon est refusé
(CL35-05).

## 5. Ce que je n'ai pas pu vérifier

- **Le comportement réel de l'outil en ligne de commande** avec `--tools ''` : seule la chaîne d'aide embarquée est lue,
  aucun lancement réel. Restent aussi à établir sa coupure sur `--max-budget-usd` et le compte du relais quand une
  session est interrompue en plein appel (le coût d'une session coupée est lu au relais : `ideation.py:727-729`).
- **L'arrêt du sous-processus** sur une autre version de Python ou du kit : démontré ici sur Python 3.13 avec le kit
  0.2.174, sur un faux outil qui pend avant l'initialisation. Je n'ai pas vérifié si l'outil réel lance des
  petits-enfants (bac à sable).
- **CL34-14** (lot et deux antériorités), **la commande réelle d'Argon** (barème, journalisation du modèle servi,
  gestion de la clé) et **`scripts/depot_expurge.py`** : hors de mon périmètre de lecture.
- **La lecture humaine et l'identité du lecteur** : c'est une procédure, hors du code.

## 6. Fichiers produits

- Rapport : `relecture-v35/contre-lecture-v35-cl3.md`.
- Scripts : `relecture-v35/outils-cl3/`
  - `ligne_commande_kit.py` et sa sortie ;
  - `borne_temps.py` et `faux-cli/claude` ;
  - `cout_externe.py` et sa sortie ;
  - `argon_factice.py` ;
  - `appel_direct.py` ;
  - `preparer_entrees.py` ;
  - `essais-sortie.txt` ;
  - la copie des essais `copie-essais/` (à supprimer à volonté).
- Courses simulées : `relecture-v35/simulee/`
  - A : nominale, avec la commande ignorée ;
  - A2 et A3 : refus ;
  - B1 : coût NaN ;
  - B2 : code 3 ;
  - B3 et B4 : nominale, puis rejeu refusé ;
  - C : course de B3 ;
  - D3 : bras simulé sur une course « réelle » ;
  - D4a et D4b : appel direct.
- Aucun processus laissé actif : le petit-enfant de CL35-13 a été arrêté par son identifiant (1838).
