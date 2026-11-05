# Contre-lecture CL2 du différentiel v31 → v34 de la prise « idéation » — orchestrateur du pôle v7

Contre-lecteur neuf (R2) : Opus 5.5, qui n'a rien écrit de ce qu'il relit (auteur : une instance Fable 5.1).
28 octobre 2026, 18:20 UTC (relevé `date -u`). Aucun appel payant, aucun réseau, aucune clé lue ni affichée (une garde
du noyau a imprimé les **noms** de variables de clé de mon environnement, jamais leurs valeurs ; j'ai relancé sous
`env -i`). Rien d'ouvert sous `donnees/` ni dans les zones interdites ; aucune pièce lue (seules leurs tailles et
empreintes). Chemins : `pole/…`, `demonstrations/…`, `essais/…` = sous `orchestrateur-pole-v7/` de la copie v34 ;
`devis-v4` = `ideation-organisme-approches-v1/devis-ideation-v4.md` ; « sortie simulée » =
`/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/ideation-simulee-v34-cl/`.

## Verdict : **lançable après corrections**

Les dix-huit constats de CL1 sont tous traités, onze entièrement, sept en partie. Les trois bloquants de la comparaison
avec la conception de l'affinage sont traités, et le bogue de la garde de liste est corrigé. Les deux scénarios demandés
se comportent comme attendu : témoins échoués → code 4, aucune « retenue » ; session en échec → arrêt dur, code 2.

Mais quatre défauts nouveaux empêchent de lancer la v34 telle quelle :
- **CL34-01, bloquant.** Une attestation passée à la course principale n'est jamais vérifiée. Argon (le juge externe)
  lit alors les fiches pendant la course, avant toute lecture humaine. Démontré avec un fichier quelconque comme
  attestation.
- **CL34-02, majeur.** « Aucun outil » est faux pour le kit d'agent : `allowed_tools=[]` ne retire aucun outil, il
  faut `tools=[]`. Démontré sur la ligne de commande que le kit construit.
- **CL34-03, majeur.** Argon peut omettre son coût, compté alors 0, statut `ok`. Un essai entérine ce comportement.
- **CL34-04, majeur.** Le bras différé (Argon joué après l'attestation) cumule cinq trous :
  - aucun appel de contrôle et aucun plafond total ;
  - les témoins ne sont pas lus chez Argon (régression depuis v33) ;
  - la consigne en attente n'est pas liée à l'attestation ;
  - un second lancement rappelle Argon (donc paie), puis plante.

La correction est courte : une dizaine de lignes de code et quatre essais inverses. Ensuite : relecture ciblée du
différentiel v34 → v35 par un modèle ≠ Fable, puis la marche à suivre ci-dessous. CL34-05 (aucune borne de temps par
session, constat 2 de la reproduction de R-599) est fortement recommandé. Les autres constats sont mineurs.

## Ce qui a été vérifié

- **Empreintes v34** : `sha256sum -c EMPREINTES-orchestrateur-pole-v7-v34.txt` → **141 sur 141 conformes** ; compagnon
  conforme ; revérifiées en fin de relecture (dossier relu intact).
- **Différentiel** `diff -ru` v31 ↔ v34 : changent seulement `pole/ideation.py` (931 lignes de différence),
  `pole/adaptateurs.py`, `demonstrations/ideation_v1.py`, `essais/test_v7_ideation.py`, plus les LISEZMOI v32 à v34.
  `pole/relais.py`, `pole/relais_reel.py`, `pole/outils.py` et `pole/garde_outils.py` sont identiques. Les quatre fichiers
  changés ont été lus en entier, ainsi que les LISEZMOI v32 à v34, les devis v2 à v4, la comparaison et le LISEZMOI du lot.
- **Essais de l'idéation** : la commande demandée (`discover -s essais -p 'test_v7_ideation*.py'` sous `-I`) échoue
  (« No module named 'essais' »). Avec `-t .` : **26 sur 26 passent**. La **suite complète** a été relancée sur une copie
  temporaire supprimée ensuite : **305 sur 305 passent** (194 s), ce qui confirme l'annonce du LISEZMOI v34.
- **Kit d'agent** (`claude-agent-sdk` 0.2.174, venv-pole), par introspection sans exécution :
  - `ClaudeAgentOptions` accepte `verbatim_prompts`, `sandbox`, `tools`, `effort`, `thinking` ;
  - l'outil en ligne de commande embarqué connaît `failIfUnavailable`, `denyRead`, `allowRead`,
    `autoAllowBashIfSandboxed` ;
  - la ligne de commande construite pour les options v34 est reproduite en démonstration F (CL34-02).
- **Courses simulées** (moteur simulé, sans dépense ; question, onze extraits, deux documents entiers retrouvés
  ailleurs, `fiches-anonymes.md`, témoins d'exemple v2 ; liste blanche de 16 fichiers construite par le lanceur) :

| cas | ce qui est fait | code | constat |
|---|---|---|---|
| A | course nominale, deux passes, pièces des juges, `--juge-externe` sans commande | **0** | 12 fiches validées, témoins conformes, classement lisible, bras « différé », consigne d'Argon scellée en attente ; coûts fictifs 2,80 |
| B | témoins à noms neutres (le juge simulé ne les reconnaît plus) | **4** | `temoins_ok` faux, `lisible_L2_L4` faux, **aucune « retenue » imprimée** |
| C | proposeur Fable en erreur en passe 2 (« 400 Bad request version », coût 0) | **2** | arrêt dur ; erreur réelle au manifeste de fin ; aucun juge appelé |
| C2 | juge Opus en erreur | **2** | arrêt dur ; aucun `classement.json` |
| D0 | course avec commande d'Argon, dans l'environnement de cette session | 1 | `CleDansEnvironnement` (noms seuls) : la garde du noyau joue, mais l'exception n'est pas rattrapée (traceback) |
| D | même course sous `env -i`, `--attestation-lecture-humaine` = un fichier texte quelconque, sans `--bras-rapporte-differe` | **0** | **la commande d'Argon reçoit la consigne avec « ## Les fiches » (23 054 caractères) pendant la course** → CL34-01 |
| E1 | bras différé sur A, attestation juste, commande qui omet `cout_usd` | **0** | coût compté **0,0** ; aucun appel de contrôle d'Argon → CL34-03, CL34-04 |
| E2 | même commande relancée | **1** | Argon **appelé une seconde fois** (journal : deux réceptions), puis `EcrasementInterdit` → CL34-04 |
| F | ligne de commande du kit pour `juge_ideation` (construite, jamais exécutée) | — | `--tools` ABSENT, `--allowedTools` ABSENT, `--effort` ABSENT ; avec `tools=[]` : `--tools ''` → CL34-02, CL34-08 |

## 1. Constats CL31-01 à CL31-18

| constat | statut | preuve (v34) | réserve |
|---|---|---|---|
| CL31-01 panne du duel, appel de contrôle, arrêt | **porté** | `pole/ideation.py:593-621` (appel de contrôle : statut, « OK », coût > 0, relais qui compte), `:704-706` (arrêt dur), `:103-115` (adresse http seule, sans chemin) ; lanceur `demonstrations/ideation_v1.py:195, 244-252, 263-265, 277-279` ; démos C, C2 | aucune borne de temps (CL34-05) ; `AdaptateurClaudeSDK` valide toujours avec `relais.valider_url_relais`, qui accepte `https` (`pole/adaptateurs.py:239` → `pole/relais.py:35`) : seul le lanceur applique la règle stricte |
| CL31-02 replis non bloquants | **porté** | `pole/ideation.py:704-706, 709-721` (liste vide, fiches en trop : tout refusé), `:733-735, 751-753, 774-776` (arrêts), `:289, 819` (`passe`) | `bruts[:MAX_FICHES_ABSOLU]` tronque en silence si `--nombre` > 12 (CL34-11) |
| CL31-03 aucun témoin | **porté** | `pole/ideation.py:331-369` (quatre classes imposées), `:540-565` (critère gelé par juge), `:842-844` ; lanceur `:273-279` (code 4) ; démo B | noms des témoins visibles par les juges (CL34-12) |
| CL31-04 auto-préférence, juge non Claude | **porté en partie** | `pole/ideation.py:507, 518-537` (unanimité, classements par juge, auto-préférence) ; `pole/adaptateurs.py:320-369` (juge externe) | porte franchissable par un seul juge et classement agrégé de la lignée des proposeurs : assumés et dits (devis-v4 § 5) ; témoins non lus chez Argon en différé (CL34-04) |
| CL31-05 juges sans pièces | **porté** | `pole/ideation.py:401-415, 427-428` ; devis v2 § 2 | `anteriorite-coevolution-…` (pièce des juges) est absente du lot (CL34-14) |
| CL31-06 garde perméable, quarantaine resservie | **porté en partie** | `pole/ideation.py:70-80, 299-316` (motifs élargis, chaînes feuilles), `:736-740` (garde avant la passe 2), `:744` (quarantaine jamais resservie), `:703` (signaux sur la réponse brute) ; devis-v4 § 1 (lecture humaine de tout) | paraphrases qui passent, faux positifs sur le vocabulaire du programme (CL34-10) ; `scripts/depot_expurge.py` non traité |
| CL31-07 pièces contournables | **porté** | `pole/ideation.py:121-170` (liste blanche par empreinte, liens refusés, normalisation) ; essais `:171-198` | — |
| CL31-08 outils et lectures | **porté en partie** | `pole/adaptateurs.py:26, 202` ; `pole/ideation.py:636-637` (deux tours au plus) ; lanceur `:207-209` (lectures interdites) | **sans effet au niveau du kit** (`allowed_tools=[]` ≠ aucun outil, CL34-02) ; « racine du dépôt » mal calculée hors de l'arborescence d'envoi (CL34-06) |
| CL31-09 coût | **porté en partie** | lanceur `:53-54` (plafonds par rôle et modèle) ; `pole/ideation.py:647-650, 683-686, 698` (plafond, coût = max(déclaré, relais)) ; devis v2 § 3, v3 § 2 | effort de réflexion non fixé (CL34-08) ; appels de contrôle et Argon hors du plafond total (CL34-07) |
| CL31-10 manifeste | **porté en partie** | `pole/ideation.py:655-675` (manifeste de départ scellé avant le premier appel : moteur, bac à sable, relais, empreintes), `:653` (coûts fictifs) ; démo A | version de l'outil en ligne de commande, commande d'Argon et lectures interdites non consignées ; fichiers des agents listés mais non scellés (`:702`) ; aucun manifeste de fin sur une exception autre que `CourseInterrompue` (`:849`) (CL34-09) |
| CL31-11 porte servie aux juges | **porté** | `pole/ideation.py:418-435` ; essai `essais/test_v7_ideation.py:347` | — |
| CL31-12 agrégat, ordre, départage | **porté** | `pole/ideation.py:441-453` (permutation par juge), `:489-512` (agrégat nommé, départage par empreinte) | — |
| CL31-13 passe 2 remplaçait la passe 1 | **porté** | `pole/ideation.py:741-756` (les fiches s'ajoutent) ; devis v2 § 2 (matériau `fiches-anonymes.md` seul) ; devis-v4 § 4 (L4 sur la passe 1) | — |
| CL31-14 sections servies entières | **porté** (par le devis) | `extraits-v1/` (onze extraits scellés, empreintes conformes à la liste) ; code inchangé (`pole/ideation.py:182-192`), assumé | quatre documents entiers restent servis ; à couvrir par la lecture humaine de la liste |
| CL31-15 sonde du bac à sable | **porté** | `pole/adaptateurs.py:118-136` (`--unshare-pid --proc /proc`) ; lanceur `:200-205` | utilisateur distinct de celui du relais : non vérifiable par le code (procédure) |
| CL31-16 affirmations fausses | **porté en partie** | docstrings réécrites (`pole/ideation.py:1-31`) | nouvelles affirmations fausses (CL34-13) |
| CL31-17 hygiène | **porté** | `pole/ideation.py:809-810` (clé écrite après les juges), `:216, 319-321` (champs internes retirés), `:173-179`, `:578-590` | — |
| CL31-18 essais | **porté en partie** | 26 essais, artefacts R5 | deux essais entérinent des défauts : `essais/test_v7_ideation.py:505` (coût manquant → `ok`) et `:544-556` (attestation passée en course : Argon joué dans la course) ; `:453-460` vérifie `allowed_tools == []`, pas l'absence d'outil |

**Compte : 11 portés, 7 portés en partie, 0 non porté.**

## 2. Les trois bloquants de la comparaison et le bogue de la garde de liste

1. **Lecteur nommé et bras rapporté différé.** Porté sur le chemin `--bras-rapporte-differe` :
   - la course écrit la consigne d'Argon en attente (`pole/ideation.py:784-795`) ;
   - `executer_bras_rapporte` exige une attestation qui porte l'empreinte de `fiches-validees.json` (`:905-911`) ;
   - le lecteur est nommé par le devis v4 (§ 1) et par le LISEZMOI du lot (décision de 19:02).

   **Contournable** (CL34-01) : la course principale accepte `attestation_lecture_humaine` et joue alors Argon sans rien
   vérifier (`:785, 796-808`). En outre, l'attestation ne lie pas la consigne envoyée (CL34-04).
2. **Classes de témoins et code 4.** Porté (`pole/ideation.py:327, 344-364` ; lanceur `:273-279` ; démo B).
3. **L4 restreinte à la passe 1.** Porté dans le devis (devis-v4 § 4). Le champ `passe` est dans chaque ligne
   (`pole/ideation.py:819`). C'est une règle de lecture, non codée, ce qui est acceptable.
4. **Bogue de la garde de liste.** Corrigé :
   - `feuilles_texte` (`pole/ideation.py:299-316`) rend les chaînes feuilles avec leurs vrais retours à la ligne ;
   - l'essai `essais/test_v7_ideation.py:139-141` couvre le cas ;
   - vérifié à la main : « 1. préparer\n2. agir » est signalé.

   « a) … b) … », les listes à puces et des paraphrases passent toujours (CL34-10).

## 3. Constats neufs (v32 à v34)

### CL34-01 — bloquant — L'attestation n'est vérifiée que sur le chemin différé : Argon peut lire les fiches pendant la course, avant tout humain

**Preuves.**
- `pole/ideation.py:785` : `if not attestation_lecture_humaine:` → différé ; sinon `:796-808` joue la commande externe sur
  la consigne qui contient les fiches. Le contenu de l'attestation n'est jamais lu ici : seule son empreinte est
  consignée (`:667-669`). L'attestation ne peut d'ailleurs pas porter l'empreinte de fiches qui n'existent pas encore.
- Le lanceur passe `--attestation-lecture-humaine` à la course principale dès qu'il est donné sans
  `--bras-rapporte-differe` (`demonstrations/ideation_v1.py:142, 254-262`).
- L'essai `essais/test_v7_ideation.py:544-556` érige ce chemin en fonctionnalité (« avec attestation dès la course : bras
  joué dans la course »), avec l'attestation d'une **autre** course.
- **Démo D** : attestation = fichier texte « ceci n est pas une attestation » ; la commande reçoit deux consignes, l'appel
  de contrôle, puis 23 054 caractères dont « ## Les fiches ». Code 0, `bras_rapporte: {"argon": 0.9}`. N-053 point 5 et
  devis-v4 § 2 (« il se joue après l'attestation seulement ») sont violés.

**Correction.**
- Retirer le chemin en course : `executer_ideation` lève `CourseInterrompue` si `attestation_lecture_humaine` est donné
  avec des juges externes, ou l'ignore et diffère toujours.
- Le lanceur refuse `--attestation-lecture-humaine` sans `--bras-rapporte-differe`.
- Réécrire l'essai `:544-556` en artefact R5 (refus attendu).

### CL34-02 — majeur (à corriger avant lancement) — « Aucun outil » n'est pas appliqué par le kit d'agent

**Preuves.**
- Dans `claude-agent-sdk` 0.2.174, `allowed_tools` désigne les outils **auto-permis**, pas les outils disponibles
  (`types.py` : « To restrict which tools are available at all, use ``tools`` » ; `tools=[]` : « Disable all built-in
  tools »). Une liste vide n'émet même pas `--allowedTools`.
- **Démo F** (ligne construite par `SubprocessCLITransport._build_command`, jamais exécutée) : `--tools` absent, donc jeu
  d'outils par défaut. Restent Read, Glob, Grep, Write, Edit, Bash. Seuls les dix outils de `OUTILS_INTERDITS` sont retirés.
- Avec `permission_mode="dontAsk"`, `autoAllowBashIfSandboxed: True` (`pole/adaptateurs.py:211`) et le crochet, qui permet
  Bash et les outils de fichier dans le dossier (`pole/garde_outils.py:283-300`), l'agent garde probablement un terminal
  dans le bac à sable.

**Conséquences.**
- Les affirmations sont fausses : `pole/adaptateurs.py:24-26`, `demonstrations/ideation_v1.py:8`, `pole/ideation.py:4-5`,
  LISEZMOI v32 l. 19.
- Les définitions d'outils ajoutent environ 10 000 à 20 000 jetons (estimation) à chaque session, appel de contrôle
  compris. Pour Fable, cela rapproche l'appel de contrôle de son plafond de 0,20 USD.
- Un appel d'outil consomme l'un des deux tours : la session peut finir en `tours_epuises`, donc en arrêt dur après
  dépense.
- Par le terminal, l'agent peut lire tout ce qui n'est pas sous les trois chemins interdits (`/tmp`, `/srv`, `/etc`…). Le
  code l'admet : la garde par motifs se traverse (`pole/garde_outils.py:3-6`). Cela vaut aussi pour un fichier de clé
  d'Argon posé là.

**Correction.**
- Dans `AdaptateurClaudeSDK.lancer`, passer `tools=list(OUTILS_PAR_ROLE[role])` quand le rôle y figure (→ `--tools ''`),
  en gardant bac à sable et crochet.
- Essai qui construit la ligne de commande et exige `--tools ''`.
- Corriger les affirmations.

### CL34-03 — majeur — Juge externe : coût manquant accepté comme 0

**Preuves.**
- `pole/adaptateurs.py:363` : `cout = objet.get("cout_usd", 0.0)`.
- L'essai `essais/test_v7_ideation.py:505` attend `ok`, alors que le LISEZMOI v33 l. 11 annonce « coût manquant →
  `erreur` ».
- **Démo E1** : notes rendues sans `cout_usd` → `cout_compte_usd: 0.0`, code 0.

L'appel de contrôle d'Argon exige un coût > 0, mais il n'est fait qu'une fois, et pas du tout sur le chemin différé
(CL34-04).

**Correction.** `"cout_usd" not in objet` → `erreur` ; inverser l'essai.

### CL34-04 — majeur — Bras différé : ni contrôle, ni plafond total, ni témoins, consigne non liée, rejouable après dépense

**Preuves.** `pole/ideation.py:896-970` ; lanceur `:229-239`.
- **Aucun appel de contrôle** sur ce chemin. Le lanceur retourne avant (`:229-239`) ; démo E : journal d'Argon sans appel
  « OK ».
- **Aucun plafond total.** Seul le plafond par session d'Argon est appliqué (`:929`), ni compté ni vérifié contre le reste
  du budget de la course.
- **Témoins non lus chez Argon** : la lecture renvoie une phrase (`:960-961`). Régression depuis v33 (`:833` sur le
  chemin en course), alors que le devis v3 § 2 définit L5 comme « accord de rang … et conformité des témoins chez lui ».
  Les doublons et les clés nécessaires sont pourtant disponibles (`:912-913, 955`).
- **Consigne non liée.** `consigne-en-attente.md` est lue sans vérifier son sceau (`:924-928`) ; l'attestation ne porte
  pas son empreinte. Or c'est elle qui sort du périmètre : question, pièces des juges, fiches, témoins.
- **Rejouable.** Un second lancement rappelle Argon puis lève `EcrasementInterdit` sur `reponse.md` (`:934`), non
  rattrapée (lanceur `:234`) : **démo E2**, deux réceptions, code 1. Dépense doublée, sans manifeste.
- Sur notes invalides, aucun `manifeste-bras-rapporte.json` (`:951-953`).

**Correction.**
- Vérifier le sceau de chaque consigne en attente et exiger son empreinte dans l'attestation
  (`consignes_en_attente_sha256`).
- Refuser **avant l'appel** si `traces-<juge>/reponse.md` ou `manifeste-bras-rapporte.json` existe.
- Faire l'appel de contrôle d'Argon sur ce chemin (et le retirer de la course principale ; voir la marche à suivre).
- Plafond total relu dans `manifeste-fin.json`.
- `lecture_temoins(notes_externes, temoins, doublons_externes, cles)`, en relisant les témoins depuis la liste blanche
  de la course.
- Manifeste écrit sur tous les chemins.

### CL34-05 — majeur — Aucune borne de temps par session (constat 2 de la reproduction de R-599)

**Preuves.**
- `pole/adaptateurs.py:264, 268-283` : `asyncio.run(self._executer(…))` sans délai.
- La reproduction (`docs/notes/ideation-organisme-v1/repro-r599-v1/LISEZMOI-v1.md`, l. 15 et 23-24) montre que, l'amont
  en échec, l'agent réessaie jusqu'à la borne du montage (180 s) et ne rend rien. Sans borne, l'appel de contrôle peut
  pendre.
- Le juge externe, lui, a un délai (`delai_s=900`).

**Correction.** `asyncio.wait_for` avec un délai par rôle (≈ 120 s pour l'appel de contrôle, ≈ 15 min pour une session)
→ statut `erreur`, motif « délai dépassé » ; essai avec un faux kit qui pend.

### CL34-06 — mineur — Lectures interdites fragiles ; piège sur `SORTIE-controle`

**Preuves.**
- « Racine du dépôt » = cinq niveaux au-dessus du code (`demonstrations/ideation_v1.py:207-208`). C'est juste dans
  l'arborescence d'envoi (`…/envois/pole-scientifique-automatique-v1/`). Dans la copie du lot, cela désigne
  `/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-…`, pas le dépôt.
- Les agents de l'appel de contrôle travaillent sous `SORTIE-controle/`, qui n'est pas sous `SORTIE`.
  `construire_options` exige pourtant que le dossier soit sous un chemin interdit. Démontré : pour `SORTIE=/srv/courses/…`,
  le dossier `…-controle/claude-opus-5-5` est refusé (`ValueError`, traceback, code 1). C'est bruyant et sans dépense, mais
  c'est un piège au lancement.

**Correction.** `--racine-depot` explicite (ou `git rev-parse --show-toplevel`) ; contrôle sous `SORTIE/controle/`, ou
`SORTIE-controle` ajouté aux interdits ; interdits consignés au manifeste. En attendant : `SORTIE` sous le dossier
personnel de l'opérateur.

### CL34-07 — mineur — Le plafond de 20 USD n'est pas tenu par le code sur toute la course

**Preuves.**
- Les appels de contrôle ne sont pas comptés (`pole/ideation.py:593-621` ne remonte pas le coût ; lanceur `:245-249`).
- Argon en différé est hors total (CL34-04).
- Somme des plafonds de session : 2 + 5 + 2 + 5 + 3 + 1,5 = 18,5. Avec Argon (3) et les contrôles (≈ 0,6), on arrive à
  ≈ 22. Le relais ne borne que la part Claude.

**Correction.** Total Claude à 17 USD, au noyau (`--budget-total-usd 17`) et au relais (`--plafond-usd 17
--reserve-par-appel 3.5`) ; Argon ≤ 2,5 à 3 ; contrôles comptés au journal.

### CL34-08 — mineur — Effort de réflexion non fixé (demandé par CL31-09)

**Preuve.** Démo F : ni `--effort` ni `--thinking`.

**Correction.** `effort` (ou `thinking`) fixé par rôle dans `construire_options` et consigné au manifeste de départ.

### CL34-09 — mineur — Manifeste et environnement de la commande externe

**Preuves.**
- Le manifeste ne consigne :
  - ni la commande d'Argon ni l'empreinte de son script (seulement `[argon, gemini-argon, "juge-externe"]`) ;
  - ni la version de l'outil en ligne de commande ;
  - ni les lectures interdites.
- Une exception autre que `CourseInterrompue` laisse sans manifeste de fin : lecture du relais en panne, levée par
  `urllib`, qui suit les variables de mandataire (`demonstrations/ideation_v1.py:119-123`) ; `EcrasementInterdit` ;
  `CleDansEnvironnement` (démo D0).
- `AdaptateurJugeExterne` vérifie `self._environnement`, mais le sous-processus hérite de `os.environ`
  (`pole/adaptateurs.py:343-350`) : les essais (`environnement={}`) ne testent pas ce qui tourne.

**Correction.** Consigner tout cela. Passer à la commande un `env=` explicite et minimal (PATH, HOME, LANG, chemin du
fichier de clé), le même que celui qu'on vérifie. `ProxyHandler({})` pour `/relais/etat`. Rattraper toute exception dans
`executer_ideation` pour écrire le manifeste de fin.

### CL34-10 — mineur — Garde lexicale : paraphrases et faux positifs

**Preuves** (vérifiées à la main).
- **Passent** : « pour passer sous le radar du moniteur », « rendre la sonde aveugle », « dissimuler la manœuvre au
  détecteur », « a) … b) … », listes à puces, « injections » au pluriel.
- **Signalés à tort** : « classe exfiltration, nommée par protocole » (forme même que la consigne demande), « Phase 1 :
  étalonnage des sondes », « injection de bruit dans les activations ».

**Correction.** Signal assumé : la lecture humaine de toutes les fiches reste la barrière. Rapporter le taux de
quarantaine par proposeur en L1 ; ajouter les pluriels.

### CL34-11 — mineur — `--nombre` non borné : troncature silencieuse au-delà de 12

**Preuve.** `pole/ideation.py:716` (`bruts[:MAX_FICHES_ABSOLU]`) ; lanceur `:146`.

**Correction.** Refuser `nombre ∉ [1, 12]`.

### CL34-12 — mineur — Témoins : noms révélateurs, injecteur sans classe

**Preuves.**
- Les juges voient `nom`. Les noms de l'exemple (« Verbeux vide », « Assuré occupé », « Jumeau ») désignent le piège ;
  le juge simulé les reconnaît justement à leur nom (`demonstrations/ideation_v1.py:94-98`).
- Le témoin injecteur du devis-v4 § 3 doit prendre l'une des quatre classes : le code n'en connaît pas de cinquième
  (`pole/ideation.py:344-345`).
- Aucune mesure de discernabilité (longueur, style).

**Correction** (consigne au tiers).
- Noms neutres et longueurs dans la fourchette des fiches.
- Injecteur classé `faux_falsifiabilite`, attendu inéligible, qui demande au juge « 3 partout ».
- Rapporter la longueur des témoins contre celle des fiches.

### CL34-13 — mineur — Affirmations fausses et états impossibles

**Preuves.**
- « Aucun outil » (CL34-02).
- LISEZMOI v33 l. 11, « coût manquant → erreur » (CL34-03).
- `pole/ideation.py:31` dit le juge non Claude impossible (faux depuis v33).
- Docstring `executer_ideation` « v33 » (`:629`).
- `lecture["complet"]` toujours vrai (`:824`, tout juge manquant lève avant).
- Code 3 inatteignable (lanceur `:277-278` ; « aucune fiche » lève avant → code 2).

**Correction.** Réécrire ; supprimer ou documenter les gardes qui ne peuvent pas jouer.

### CL34-14 — mineur (lot) — Quatre pièces de la liste blanche absentes du lot

**Preuves.**
- 13 des 17 empreintes de `liste-blanche-sans-temoins-v1.json` sont conformes aux fichiers du lot.
- Absents du lot :
  - `conception-pole-scientifique-v1.md` (`a4f94148…`) et `integration-proposeurs-ia-v1.md` (`974b2dbe…`) : trouvés,
    conformes, dans `scratchpad/depot-lot-fable-v1/` ;
  - `anteriorite-coevolution-et-boite-blanche-v1.md` et `anteriorite-universalite-metriques-v1.md` : **introuvables
    ici**. La première est aussi une pièce des juges (devis v2 § 2).

**Correction.** Les obtenir sur la branche avant la liste blanche, avec les empreintes de la liste de conv-audit.

## 4. Marche à suivre pour le lancement (ordre)

1. **v35** : corriger CL34-01 à CL34-04 (obligatoire) et CL34-05 (recommandé). Les mineurs CL34-06, -07, -08, -11
   coûtent quelques lignes. Ensuite : 305 essais et plus, nouvelles empreintes, **relecture ciblée v34 → v35** par un
   modèle ≠ Fable (R2).
2. **Pièces** : obtenir les deux antériorités manquantes (CL34-14) ; vérifier les 17 empreintes.
3. **Témoins** : un tiers (sous-agent neuf, ni proposeur ni juge, n'ayant vu aucun moniteur) écrit les quatre classes et
   l'injecteur. Noms neutres, longueurs comparables (CL34-12), jamais ceux de l'exemple. Fichier versionné et scellé.
4. **Liste blanche** : `--construire-liste-blanche` sur les 17 fichiers et les témoins (18) ; scellée ; lecture humaine
   de la liste.
5. **Machine** :
   - `bwrap` et `socat` ; kit 0.2.174 et outil en ligne de commande dans `$PY` ;
   - sonde du `/proc` neuf. Sans elle, agents sous un utilisateur non root distinct de celui du relais ;
   - `SORTIE` neuve, **sous le dossier personnel de l'opérateur** (CL34-06) ; jamais versée avant l'attestation.
6. **Clé Anthropic** :
   - clé tournée (R-589) dans un fichier d'une ligne en mode 600 ;
   - relais lancé sous `env -i` :
     `env -i PATH=… HOME=… $PY -I -B -m pole.relais_reel --fichier-cle F --plafond-usd 17 --reserve-par-appel 3.5 --port 0 --journal J`
     (lit puis supprime le fichier) ;
   - `demonstrations/verification_cle_proc_v7.py --pid <identifiant du relais>` au cas sain, versé.
7. **Commande d'Argon** (fournie par session-depot, à sceller avec son empreinte) :
   - lit la consigne sur l'entrée standard ;
   - imprime en dernière ligne `{"texte": …, "cout_usd": …}` avec un coût **toujours** présent ;
   - sort avec un code ≠ 0 sur tout échec ;
   - tient elle-même son plafond (≤ 2,5 à 3 USD).

   Sa clé : un fichier mode 600 lisible des seuls opérateur et commande. Il est **créé seulement à l'étape 11**, ce qui
   suppose de déplacer l'appel de contrôle d'Argon sur le chemin différé (CL34-04). Avec la v34 telle quelle, le lanceur
   exige la commande dès la course réelle (`demonstrations/ideation_v1.py:221-224`) et appelle Argon en contrôle avant la
   course. La clé devrait alors exister pendant que les agents Claude tournent, ce qui n'est acceptable qu'avec
   CL34-02 corrigé et le fichier sous un chemin interdit ou à un autre utilisateur. **Jamais** de variable de clé dans
   l'environnement du noyau : la garde le refuse (démo D0).
8. **GO** : ligne dans `registres/go.md`, citant le devis v4 et le mot de Lazar (dépense : nœud).
9. **Course principale**, sous `env -i PATH=… HOME=… LANG=…` (ni nom de clé ni variable de mandataire) :
   - `--moteur claude-sdk --url-relais http://127.0.0.1:PORT --confirmer-moteur-reel --budget-total-usd 17` ;
   - pièces, pièces des juges, matériau, `--seconde-passe`, `--juge-externe argon=gemini-argon` ;
   - **jamais `--attestation-lecture-humaine` ici**.

   L'appel de contrôle par modèle est fait par le lanceur ; il échoue vite si le relais ou l'amont est en panne (avec
   CL34-05). Codes de sortie : 0 lisible, 4 témoins échoués, 2 arrêt.
10. **Lecture humaine** par le lecteur nommé (sous-agent neuf de session-depot, aucun moniteur vu, décision de 19:02). Il
    lit :
    - les réponses brutes (`traces-*/reponse.md`) ;
    - `fiches-en-quarantaine.json` et **toutes** les fiches validées ;
    - **la consigne en attente d'Argon** (ce qui sortira du périmètre).

    Il écrit l'attestation `{lecteur, fiches_validees_sha256, consignes_en_attente_sha256 (après v35), lu_le}`, scellée.
11. **Bras différé** :
    `--bras-rapporte-differe --attestation-lecture-humaine A --juge-externe argon=gemini-argon --commande-juge-externe "…"`,
    une seule fois (CL34-04).
12. **Versement scellé** de `SORTIE` et `SORTIE-controle` ; contre-lecture ; lectures L0 à L5 selon les devis v2 à v4
    (L4 sur la passe 1 ; aucune lecture par proposeur pour choisir un modèle).

## 5. Coût du devis v4 au regard du code

**Tailles mesurées** sur la course simulée (consignes réelles, sans les deux antériorités manquantes) :
- proposeur, passe 1 : **143 488 caractères** ;
- proposeur, passe 2 : **184 973** (avec huit vraies fiches de passe 1 : ≈ 200 000 à 210 000) ;
- juge : **110 220** avec 12 fiches courtes ; avec 32 vraies fiches et 4 témoins : ≈ 180 000 à 200 000.

Ajouter les deux antériorités (taille inconnue ; supposées 20 000 à 40 000 caractères) et, tant que CL34-02 n'est pas
corrigé, les définitions d'outils (≈ 10 000 à 20 000 jetons).

À ≈ 3,2 caractères par jeton (français, hypothèse), on obtient en entrée :
- ≈ 62 000 à 78 000 jetons par proposeur en passe 1 ;
- ≈ 80 000 à 98 000 en passe 2 ;
- ≈ 72 000 à 82 000 par juge, soit environ trois fois l'hypothèse de CL1 : les juges reçoivent maintenant les pièces
  (CL31-05).

**Barème du relais** (inchangé, `pole/relais_reel.py:44-50`) : Opus 4 / 20 / 5 ; Fable 10 / 50 / 12,5 dollars par
million de jetons (entrée / sortie / écriture de cache).

| session | entrée (écriture de cache) | sortie, réflexion comprise | total | plafond par session |
|---|---|---|---|---|
| proposeur Opus, passe 1 | ≈ 0,35 | 0,20 à 0,80 | 0,55 à 1,15 | 2 |
| proposeur Opus, passe 2 | ≈ 0,45 | 0,20 à 0,80 | 0,65 à 1,25 | 2 |
| proposeur Fable, passe 1 | ≈ 0,88 | 0,50 à 2,00 | 1,38 à 2,88 | 5 |
| proposeur Fable, passe 2 | ≈ 1,13 | 0,50 à 2,00 | 1,63 à 3,13 | 5 |
| juge Opus | ≈ 0,39 | 0,20 à 0,60 | 0,59 à 0,99 | 1,5 |
| juge Fable | ≈ 0,96 | 0,50 à 1,50 | 1,46 à 2,46 | 3 |
| appels de contrôle (Opus et Fable) | | | ≈ 0,20 à 0,35 | 0,2 chacun |
| **part Claude** | | | **≈ 6,5 à 12,2** | |
| Argon (barème inconnu) | | | ≈ 0,1 à 3 | 3 |
| **course entière** | | | **≈ 6,6 à 15** | 20 |

**Lecture.**
- La fourchette du devis (≈ 7 à 14 USD) est cohérente avec le code.
- Le plafond de 20 tient en attente raisonnable. Il n'est pas garanti par le code sur Argon et les contrôles (CL34-07).
- **Risques précis :**
  - le juge Fable approche son plafond de 3 si sa réflexion dépasse ≈ 40 000 jetons, ou si un second tour relit sans
    cache ;
  - **l'appel de contrôle de Fable** à 0,20 USD peut échouer en `budget_depasse` à cause des définitions d'outils : arrêt
    bruyant, sans perte notable. Porter `--budget-controle-usd` à 0,5 ou corriger CL34-02 ;
  - un tour consommé par une tentative d'outil (CL34-02) peut finir en `tours_epuises` après dépense.

## 6. Ce que je n'ai pas pu vérifier

- **Le comportement réel du kit d'agent et de l'outil en ligne de commande**, faute de lancement réel :
  - en mode `dontAsk`, si les outils en lecture seule sont refusés et si Bash est auto-permis dans le bac à sable (j'ai
    seulement établi que les outils restent **disponibles**) ;
  - si `filesystem.denyRead` s'applique aux commandes du terminal ;
  - quand `max_budget_usd` coupe ;
  - si l'outil en ligne de commande connaît les prix d'Opus 5.5 et de Fable 5.1 ;
  - s'il fait des appels auxiliaires par le relais ;
  - si le cache fonctionne à travers le relais.
- **Le dernier maillon de R-599** (relais → amont réel avec la vraie clé) : à établir par l'appel de contrôle, sous GO.
- **La commande d'Argon** : non fournie. Ni son barème ni son modèle réel (H-07 : le modèle servi n'est pas journalisé)
  ni son traitement de la clé.
- **La taille et le contenu** des deux antériorités absentes ; le rapport réel caractères/jetons ; le contenu des
  pièces, non lu.
- **`scripts/depot_expurge.py`** (exclusion de `traces-*` et de la quarantaine) : non lu.
- **Qui a codé ou vu des moniteurs** chez session-depot (condition du lecteur) : procédure, hors du code.

## Fichiers produits

- Ce rapport :
  `/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/contre-lecture-v34-cl2.md`.
- La sortie simulée :
  `/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/ideation-simulee-v34-cl/`.
  Elle contient :
  - les cas A à F (dossiers, sorties standard, codes) ;
  - les listes blanches de la simulation et les témoins à noms neutres ;
  - trois petits outils de démonstration dans `outils-cl/` (enveloppe de panne, juge externe factice sans réseau,
    construction de la ligne de commande du kit sans exécution).

La copie temporaire de la suite complète a été supprimée. Le dossier relu est intact (141 sur 141 empreintes conformes
en fin de relecture ; le dossier `essais/_tmp` créé par le premier lancement des essais a été retiré).
