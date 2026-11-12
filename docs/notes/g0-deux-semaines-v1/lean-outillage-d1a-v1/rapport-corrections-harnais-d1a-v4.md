# Essai Lean, outillage D-1a — rapport des corrections du harnais — v4

- **Pour** : la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`.
- **Écrit par** : l'auteur du harnais (sous-agent développeur, Opus 5.5, `claude-opus-5-5`).
- **Heures** (relevées par `date -u`) : contre-lecture courte vérifiée à 03:45:46 UTC ; rapport vers 04:05 UTC.
- **Lu, empreinte vérifiée** : `contre-lecture-courte-harnais-d1a-v3.md` (`b6ca886d…`, égale à son compagnon), décision R-2307.

## Livrable

- **Commit** `34ff42b744ef567cfd536e5941316ce6db07ea1a` (arbre `3bd9597dfaab4147303946ef2976148ce27f587d`), sur la branche
  `prep/lean-outillage-d1a-v4`, partie de `5e7c080d`.
  - La branche est poussée seule, **sans fusion**. Les commits intermédiaires `73c2e804` et `de37a3c1` ont été poussés tôt,
    à cause des redémarrages du conteneur.
  - Les fichiers sont neufs et à nom versionné (R12). Les modules v1 à v3 sont intacts. Empreintes : `empreintes-harnais-v4.txt`.
- **Essais** : 106 essais v4 passent. Les essais v1, v2 et v3 passent toujours (200), hors ceux des gardes v2, dont les
  artefacts ne sont pas dans l'arbre réduit (`journal-essais-r5-v4.txt`).
- **Mutations** : 46 sur des copies, **46 tuées**, aucune par délai (`journal-mutations-harnais-v4.json`, script
  `scripts/lean_essai_d1a_v4/mutations_harnais_v4.py`). Méthode : import tracé, `-o pythonpath=` sur la copie, sans
  `PYTHONPATH` hérité.
- **Ni serveur, ni dépense, ni appel de modèle, ni appel à Hetzner. Aucune valeur de clé.**

## Verdict

- Les deux bloquants sont corrigés et éprouvés hors machine.
  - **CLC3-04** : le premier pas `noyau` est devenu discriminant.
  - **CLC3-07** : il y a des garde-fous hors du processus de la session.
- CLC3-08, CLC3-09, CLC3-10, CLC3-01, CLC3-02, CLC3-03 et CLC3-06 sont corrigés.
- Les douze survivantes de CLC3-11 sont tuées, k12 en tête.
- CLC3-05 reste en réserve écrite, avec deux atténuations faites.
- Rien de ce qui dépend de Lean n'est éprouvé : c'est le premier pas sur la machine.

## Les deux bloquants

### CLC3-04 — premier pas discriminant (`epreuve_isolement_v4.premier_pas_noyau`, `juger_noyau`)

- **G-L1 et G-L7 exigés.** Chaque item du groupe `noyau` doit réussir sa compilation (`.olean` présent) et voir le vérificateur
  aller au bout.
- **Rejeu nommé.** Un item qui doit être pris par le rejeu exige une ligne de rejeu présente, `ok: false`, dont l'erreur
  **nomme la constante fautive** (`constante_fautive` : `etape_1._hors_noyau`, `faux_lemme`).
- **Deux passages.** Le groupe est joué deux fois, avec G-L3+ puis sans (attendus `sans_suppl`) : G-L8 et G-L5 doivent prendre
  chaque item seuls. Le pas n'est conforme que si les deux passages le sont.
- **Artefact `simproc` réécrit** (`noyau_simproc_hors_noyau_v4.lean`). `simp` progresse par `and_self`, sans `try` ni retour
  arrière, dans une définition (`temoinSimproc`) ; `etape_1` s'appuie ensuite sur la déclaration ajoutée hors du noyau.
- **Essais :**
  - le cas de la contre-lecture (compilation en échec, vérificateur muet) n'est plus conforme ;
  - « aucune ligne de rejeu » et une erreur qui ne nomme pas la constante sont des écarts ;
  - G-L7 en échec sur l'item sain est un écart ;
  - les deux passages et les observations sont vérifiés avec un bac factice.
- **Mutations tuées** : c04a à c04e.
- **Observations sans jugement.** `observations_noyau` relève sans juger les refus à tort possibles : sous-terme de preuve dans
  l'énoncé, univers polymorphes.

### CLC3-07 — garde-fous hors du processus de la session (`minuterie_v4`, `hetzner_v4`)

| | Correction | Essai | Mutations |
|---|---|---|---|
| **(a)** | `minuterie_v4 detruire --pas d1a` cherche par les étiquettes fixes `essai=lean,pas=d1a` **et** par le nom `lean-outillage-d1a`. Chaque serveur trouvé voit son nom vérifié ; un serveur d'un autre nom n'est jamais touché. Destruction par identifiant, avec retentatives, puis inventaire de contrôle. Ni jeton, ni journal. | Étiqueté et nommé : tous deux détruits, le voisin de la course reste. Autre nom : refus, aucun DELETE. Pas `d1b` : non touché. Ligne de commande sans journal. | c07a, c07b, c10e |
| **(b)** | `creer-et-armer` lance `veiller` **détaché** (`setsid`, sans terminal). Le PID est écrit dans `minuterie-d1a-<jeton>-pid-v1.txt`, dans le dossier versé. `verifier-minuterie --fichier-pid …` contrôle par le PID que le processus vit et que sa ligne de commande est bien la sienne (R10). | `start_new_session`, arguments, fichier PID ; vivante, autre processus, processus absent. | c07c, c07d, c07e |
| **(c)** | La création rend la **ligne de procédure de la mère** (texte ci-dessous). | Heure de la tâche = échéance − 1 h ; mention de `send_later`. | c07f |
| **(d)** | **Avant l'appel de création**, l'intention écrit `rattrapage-machine-d1a-<jeton>-v1.json` dans `docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/`, à committer par la mère à la création. Il contient le jeton, les étiquettes fixes, le nom, l'échéance, les deux commandes de destruction et la ligne de procédure. Un jeton réutilisé est refusé. | Fichier présent pendant l'appel de création ; contenu ; jeton réutilisé. | c07g, c07h |

**Ligne de procédure pour la mère** (CLC3-07 c), rendue par `creer-et-armer` avec les heures réelles :

> PROCÉDURE MÈRE : armer tout de suite une tâche programmée unique (`send_later` de la session mère) pour **l'échéance moins
> une heure** (UTC), avec le message « Essai Lean D-1a, échéance de la machine `lean-outillage-d1a` : lancer
> `PYTHONPATH=src python -m controle_ia.lean_essai.minuterie_v4 detruire --pas d1a`, vérifier l'absence, inscrire l'arrêt et
> prévenir Lazar ». Puis committer le fichier de rattrapage.

## Autres corrections

| Défaut | Correction | Essai : cas sain / artefact | Mutations |
|---|---|---|---|
| **CLC3-08** création tardive | Sur une création incertaine, l'étiquette est cherchée à plusieurs reprises sur une fenêtre (10 min, toutes les 30 s). Tout serveur trouvé est détruit, après contrôle du nom (note 4). Si rien n'est trouvé : arrêt explicite « rattrapage par l'étiquette X à refaire », journal non soldé. Une création **refusée** par l'API (4xx) écrit « aucune création » et se solde (note 5). | Serveur apparu après la 1ʳᵉ recherche : détruit. Rien trouvé : non soldé. 422 : soldé, coût d'une heure seulement. | c08a à c08d |
| **CLC3-09** journal | `_ecrire` au mieux : `OSError` ⇒ sortie d'erreur, jamais d'exception dans une boucle. Seule l'intention, avant l'appel, est exigée : si elle ne s'écrit pas, rien n'est créé. | Disque plein simulé : `veiller` détruit quand même à l'échéance. | c09 |
| **CLC3-10** taux et type | Taux USD par EUR **fixé dans le code** à 1,25, la valeur la plus défavorable écrite (rapport de l'outillage v1, réserve 7, `0706b12f…`) ; une déclaration ne peut que le relever. Type limité à `ccx23`, `ccx33`, `cx53`, liste de la pièce MACHINE du même rapport. | Taux 0,5 ⇒ 1,25 ; 1,3 ⇒ 1,3 ; 0 ⇒ refus ; `ccx63` refusé avant tout appel, par la commande et par le client. | c10a à c10d |
| **CLC3-01** documentation | `/--` et `/-!` sont des lexèmes de trois caractères, et le corps du commentaire commence après eux. | `/--/ -- -/ axiom`, la variante à chaîne sur deux lignes, `/-!` : l'axiome est vu. Imbrication `/- /- -/ -- -/ axiom` : vu (k12). Artefact Lean `noyau_doc_commentaire_v4.lean`. | k12, c01 |
| **CLC3-02** trous | Le vérificateur v4 fixe `pp.maxSteps` (10⁸), `pp.deepTerms` et `pp.proofs` vrais, et `withoutErrToSorry`. Il rapporte `tronque` (`⋯`), `metavariables` et `messages_elaboration`. Le harnais refuse G-L5 dès qu'un de ces champs est mauvais **ou absent**, ou qu'un `⋯` paraît dans un texte. | 8 cas (troncature, `⋯` dans chaque forme, métavariable, message, champs absents). | c02a à c02c |
| **CLC3-03** imports | Le vérificateur exige des imports **exactement** égaux à `Init` et `Mathlib` ; le harnais le recontrôle indépendamment (G-L3 et G-L8). | `["Mathlib"]`, `[Init, Mathlib, Aesop]`, `[]`, `[Init, Mathlib.Tactic]` refusés. Artefact Lean `noyau_prelude_sans_import_v4.lean`. | c03 |
| **CLC3-06** signalement | Le vérificateur donne, pour chaque énoncé, la liste des constantes **de l'agent** qu'il cite. Pour une étape : signalement en tête de la feuille du relecteur. Pour `enonce_item` : **refus** (G-L5). Tout nom de constante de l'agent hors ASCII, sauf les indices, fait échouer G-L6. | Étape qui cite `carre` : acceptée, signalée en tête. Énoncé final qui la cite : refusé. Liste absente : refusée. `Cοprime` (omicron) : refusé. `x₁` : admis. Artefact `noyau_constante_grecque_v4.lean`. | c06a à c06c |
| **CLC3-11** | Un essai pour chacune des douze survivantes. | k12, k13 (`veiller --echeance-h 60`), k16 (taux 0,5), k03 (GO hors période), k11 (déclaré < registre), k01 (`depuis` = intention), k02 (deux serveurs d'une étiquette), k05 (témoin `exit-code`), k15 (deux lignes de rejeu), k14 (constante en double), k07 (nonce mal formé), k04 (`applied_to`). Plus `veiller --depuis` (plus tard que la création : refus). | k01 à k16, k13b, k13c |
| **Note 1** | `import Mathlib` retiré du vérificateur v4. Mathlib est importé à l'exécution par l'environnement de rejeu, qui porte aussi le code de ses délaborateurs. | à mesurer au premier pas | — |
| **Note 3, CLC3-05** | Inventaire par `lstat` : fichier ordinaire à un seul lien, `Item.olean` borné à 64 Mio. | Lien symbolique, second lien physique, `.olean` trop grand : refusés. | c05a, c05b |

## Premier pas sur la machine : ce qu'il doit établir (groupe `noyau` de `attendus-v4.json`)

Joué deux fois, avec G-L3+ puis sans.

| Item | Attendu |
|---|---|
| `sain_v1.lean` | toutes les gardes passent, rejeu et aller-retour réussis |
| `noyau_simproc_hors_noyau_v4.lean` | G-L1 et G-L7 passent ; rejeu `ok: false` qui nomme `etape_1._hors_noyau` ; G-L8 échoue |
| `noyau_run_cmd_hors_noyau_v3.lean` | même chose, en nommant `faux_lemme` |
| `noyau_instance_enonce_v3.lean` | G-L5 échoue (aller-retour), le rejeu passe |
| `noyau_prelude_sans_import_v4.lean` | G-L1 passe ; G-L3 et G-L8 échouent (imports) |
| `noyau_doc_commentaire_v4.lean` | G-L3 échoue (axiome vu par le texte et par le noyau) |
| `noyau_constante_grecque_v4.lean` | G-L5 et G-L6 échouent |
| `gl3_simproc_execution_v3.lean`, `gl3_aesop_tactique_v3.lean` | relevé « le code tourne-t-il à la compilation ? » ; acceptés sans G-L3+ |

Puis, sans jugement : `noyau_preuve_dans_enonce_v4.lean` et `noyau_univers_v4.lean`, pour voir si le harnais refuse à tort.

## Réserves écrites

1. **CLC3-05.** Un `.olean` hostile reste lu par `readModuleData`, qui n'est pas durci.
   - Atténuations faites : inventaire par `lstat`, borne de taille, seconde ligne textuelle obligatoire par défaut.
   - Non faites : refuser `--sans-supplementaires` hors épreuve ; lecture et vérification séparées (format `lean4export`).
2. **Rien n'est compilé ici.**
   - Vérificateur v4 : `withoutErrToSorry`, `getThe Core.State`, `MessageLog.toList`, `Expr.getUsedConstants`, options
     `pp.*`, `Std.HashMap`.
   - Artefacts du premier pas.
   - La survie de la déclaration ajoutée par le `simproc` dépend de l'élaboration des définitions sur la chaîne épinglée. Si
     elle ne survit pas, le premier pas le dira, car il ne peut plus se dire conforme à tort.
3. **La minuterie détachée meurt avec le conteneur.** C'est pourquoi la tâche programmée de la mère (c) et `detruire --pas d1a`
   (a) sont les garde-fous de fond. Il faut aussi relancer `verifier-minuterie` à chaque reprise : je propose de l'ajouter, avec
   l'inventaire Hetzner, à la routine de reprise (consigne de Lazar : je propose, il décide).
4. **Choix à confirmer.**
   - Une étape qui cite une constante de l'agent est **signalée** ; l'énoncé final est **refusé**. Le relecteur ou Lazar
     peuvent vouloir l'inverse.
   - Le taux de 1,25 et la liste de types viennent de mon propre rapport v1. Ce ne sont pas des pièces de Lazar.
5. **Hors de ma branche.** `garde_calcul.py` ne connaît toujours pas Hetzner.

## Fichiers versés (non committés, scellés)

| Fichier | Empreinte |
|---|---|
| `rapport-corrections-harnais-d1a-v4.md` (ce fichier) | compagnon `.sha256` |
| `journal-essais-r5-v4.txt` | `758af7384e3cea8d2e6657eaa21f01aba76524c65fbc54aa602aacdc9112c85a` |
| `journal-mutations-harnais-v4.json` | `026c6a00adf8fe9626dbad39b07efaa1b3d146a0503153f2b27c6d2bec18ed81` |
| `empreintes-harnais-v4.txt` | `255063a84e329bcb89484e7515e8ab954e0e4b9f2a1bc49cf01955b9729455b0` |

| Module v4 | Empreinte |
|---|---|
| `verificateur_noyau_v4.lean` | `1f744a4d8addde8579b55c2970c456b829a244216f98e58a5144e627021efe28` |
| `gardes_lean_v4.py` | `eb74783164b8697e4a8fad3a933ea30713a7b62d4098a038f1259dec535f5581` |
| `executeur_bac_v4.py` | `576c3ca4fbb27ca44506685bacf93a4a1dcaa354fec0863db8fe81be7f2351c8` |
| `epreuve_isolement_v4.py` | `a20712f0b3769a9c0dd70bf69fd16a97fc5844f68ae95a281d08bb6785f59bac` |
| `minuterie_v4.py` | `24167b6f2f4c66556505ac51c9e21ab47541e7e95b1a9860a03fc8970d34cd6b` |
| `hetzner_v4.py` | `ca80444b5c5357a11ac775be15870c01a0727730b2d97cf0197797880aa2afc5` |
