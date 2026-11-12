# Contre-lecture neuve (R2) du delta brouillon 2 → brouillon 3 de l'addendum v4 de R1 — v1

**Verdict : scellable après couples** (19 couples, `couples-contre-lecture-delta-brouillon3-v1.json`, chaque « ancien » unique dans le brouillon 3).
Les 33 changements sont justes et conformes à la section 5 du rapport des ajouts ; seul défaut introduit : trois lignes du tableau des écarts coupées (V4-E5, V4-E6, V4-E12).
Réserve C32 : `garde_depense_v4_v1` garde 358 par défaut ; je recommande de corriger le code avant le scellement (confiance ≈ 0,6). Si c'est fait, il faut un brouillon 4 et les rejeux du § 6.

- Lecteur : sous-agent neuf (Opus 5.5). Je n'ai écrit ni l'addendum, ni le code, ni les contre-lectures précédentes. Consigne
  `docs/notes/runs-r1-r2-r4-v1/consigne-contre-lecture-delta-r1-v4-brouillon3-v1.md` (`8ebc97992db43e8aa0ebec162e8eda4a0cc49c1615850e2e0dbbc619ef8dc979`,
  vérifiée par `sha256sum` avant lecture).
- Heures (UTC, `date -u`) : début 08:06:13 ; fin : dernière ligne.
- Arbre `/home/claude/wt/r1-v4/`, branche `prep/r1-relance-v4`, tête `8bce1bc1`, lu en lecture seule. Entre `af1f2f4f` et
  `8bce1bc1`, seuls quatre fichiers sont ajoutés : le brouillon 3, le rapport de rédaction et leurs deux compagnons. Aucun fichier de code ne change.
- Pièces vérifiées : j'ai recalculé chaque sha256 et il est égal à son compagnon.
  - Brouillon 2 : `fed5fd3b832d1836abb27dc2e934aabcdbf5f3f4444e3cbb1c86359ee7986496`.
  - Brouillon 3 : `f24e416f49ac723a44687b71804be1f478dba588c6a077c9b9480cc926ea3046`.
  - Rapport de rédaction : `e44968d5744cacf71a9253a063facb19ea33349cb401c018c751e113b89f96aa`.
  - Rapport des ajouts : `0d8fd1827f58d091ac0405c4627c0b9408b61f55eb348102b4c8fed4d3f25efa`.
  - Contre-lecture complète : `e224ae8ab36541392e88bb0e406a6dc133795b430f676e99a5f0706a13d9a9f1`.
  - Rapport de la fille : `git show 97fb0681:…` donne `ae72aeaa7d7efebe6828f9244386aa2a22a62f3231e481cae405437f9ce87032`, qui dit « 381 passed in 1468.33s », 0 sauté, au départ de `af1f2f4f`.
- Interdits respectés : je n'ai lu aucun tableau d'activations, aucun score, aucune sortie d'analyse de détection. Aucun commit, aucun `.sha256`, aucun réseau,
  aucun modèle, aucune dépense, aucun fichier existant modifié. Les commandes ont tourné sous `timeout 120 nice -n 10`.

## 1. Les 33 changements, et rien d'autre

- **Diff recalculé** (`diff -u` du brouillon 2 au brouillon 3) : 321 lignes, comme le rapport. Mon empreinte de sortie
  (`f4659048…`) diffère de la sienne (`29ebeb0b…`). La cause probable est l'en-tête de `diff -u`, qui porte les heures des fichiers.
  Chaque bloc du diff correspond à un changement de C1 à C33. Je ne trouve aucun changement hors de la table.
- **Empreintes citées.** Les 9 fichiers de code neufs, les deux configurations, le devis v2 et les sorties citées
  (banc v2, épreuves, essais, pré-vol et son script, `codes.txt`, `reception-jouet.txt`, `surveillance-repetition.txt`)
  ont tous la même empreinte au commit `af1f2f4f` et sur disque, égale au texte. Le recalcul de
  `resolution_graine_lot_v3.empreinte_config` donne `a5a61077…` pour la v1 et `c34bf464…` pour la v2. La différence est d'une seule ligne,
  `voie_si_temoin_non_exact` (C2 juste).
- **Changements un par un.**
  - C3 et C21 : `CIBLES` du script v2 compte 26 fichiers, l. 258-265 ; le compte de 381 est celui de la fille. C33 est juste aussi.
  - C9, C12, C25, C29 et C30 : remplacement du nombre seul, justes.
  - C5, C6, C13 et C24 : voir le § 4.
  - C7 et C27 : le devis v2 donne « central ≈ 18 USD », le haut à ≈ 36 USD et le pire cas ≈ 57,2 USD (§§ 1 et 3). Justes.
  - C14 : le script fait l'étape « chaine » après « table-v4 » et avant « r1-rejeu » (l. 321-331). Juste.
  - C15 et C18 : la ligne de commande de `chaine_table_v4_v1` a bien `--config`, `--reparation`, `--table`, `--reception` et `--tokeniseur`.
    `recalculer_a_la_reception` appelle `rv3.construire_table_v4`. Les noms `resolution-graine-lot-v3-{temoin,reparation}`
    correspondent à `ecrire_resultat` (l. 766 et 944). Justes.
  - C31 : le journal porte « chaîne de la table v4 : conforme » ; `filtrer_journal` le rend « chaîne de la table v4 »
    (`surveillance-repetition.txt`). Juste.
  - C22 : la projection est bien + 75 min. Juste.
  - C32 : juste, mais il révèle un défaut du code (§ 2).
- **Défaut introduit.** Les changements C16 à C20, C22 et C23 ont coupé trois lignes du tableau des écarts : V4-E5 sur 3 lignes, V4-E6 sur 5,
  V4-E12 sur 5 (l. 157-174). Une ligne de tableau Markdown ne se coupe pas : chaque morceau devient une ligne de tableau à cellules décalées,
  et un lecteur qui prend « | V4-E5 | » ligne à ligne tronque l'écart. Les couples 3 à 12 recollent ces lignes. Je les ai appliqués sur une copie :
  il reste 0 ligne coupée.
- **Remarque sur l'en-tête.** La table des changements est insérée sous un titre `##` avant la liste de l'en-tête (Auteur, GO, chemins).
  L'en-tête se lit donc comme une partie de cette section. C'est sans effet sur `lire_unique` ni sur `prereg.problemes` (mêmes deux problèmes).
  Je n'ai pas fait de couple.

## 2. C32 : le défaut de 358

**Ce qui garde 358 :**
- `src/controle_ia/runs_nuit/garde_depense_v4_v1.py`, en trois endroits : l. 32 (docstring, « tests `358` passés »),
  l. 302 (`verifier_surveillance(..., tests_attendus: int = 358)`) et l. 386 (`surveiller --tests`, `default=358`).
- `tests/test_garde_depense_v4_v1.py` s'appuie sur ce défaut : journaux « 358 passed », l. 73 et 89, et appels sans le nombre, l. 103-118.

**Ce qui ne garde aucun nombre :**
- `scripts/r1_v4_instance_v2.sh` lit « Tests attendus » dans le texte (`lire_unique`, l. 105) et exige
  `^$ATTENDUS passed…$` (l. 276).
- `scripts/amorce_instance_r1_v4_v2.sh` ne contient aucun compte, pas plus que le banc v2, la configuration v2 ou la v6.
- Les prompts des tâches (`prompt_tache`) ne portent aucun compte de tests.
- Les autres « 358 » des `registres/` sont sans rapport.

**Conséquence.** Un appel sans `--tests 381` rend « detruire » sur une instance saine. Or V4-E16 n'admet aucune reprise sur une garde,
et R3 exige une configuration neuve : la destruction coûterait donc un texte neuf.

**Correction de code proposée** (non appliquée ; R12 : noms nouveaux) :
- `garde_depense_v4_v2.py`, copie de la v1 dont les écarts sont marqués `# v2` :
  - `verifier_surveillance(lignes_filtrees, session, *, tests_attendus: int)` sans défaut ;
  - `s.add_argument("--tests", type=int, required=True)` ;
  - docstring : « tests au nombre de l'addendum scellé (381) ».
  - Variante plus sûre : `--prereg CHEMIN`, qui lit « Tests attendus : `…` » une seule fois, avec la règle de `lire_unique`.
- `tests/test_garde_depense_v4_v2.py` :
  - journaux à « 381 passed » et `tests_attendus=381` passé partout ;
  - artefacts : `surveiller` sans `--tests` → code 2 ; appel sans le nombre → `TypeError` ; « 358 passed » lu → « detruire ».
- En cascade : `scripts/r1_v4_instance_v3.sh` (`CIBLES`), `scripts/amorce_instance_r1_v4_v3.sh` (qui lance le script v3) et
  `scripts/banc_mutations_r1_v4_v3.py` (`GARDE`, `E_GARDE`).

**Autre voie, sans code.** On garde le texte tel quel : la commande `--tests 381` y est écrite avec sa mise en garde.
Le risque est alors une erreur d'opérateur. Je recommande la correction de code, avec une confiance d'environ 0,6.

## 3. Les cinq champs lus par le script

Avec la règle exacte de `lire_unique` (`grep -c "<champ> : \`"`, puis `sed`), chaque champ apparaît **une seule fois** :

| Champ | Valeur lue |
|---|---|
| Tests attendus | `381` |
| Chemin de la configuration de la réparation | `prereg/R1-reparation-v4-config-v2.json` |
| Chemin de la configuration du rejeu | `prereg/R1-rejeu-config-v6.json` |
| Chemin de la table de tokenisation v3 | `prereg/R1-table-tokenisation-v3.json` |
| Chemin du préenregistrement parent | `prereg/R1-R2-rejeu-p3-v1.md` |

Après application des 19 couples, le compte reste le même : 1, 1, 1, 1, 1. La table des changements ne reprend pas ces formes.

## 4. Voie unique (C5, C6, C13, C24)

Le code ne contredit pas la voie unique :
- `lire_temoin` (l. 615-629) rend `voie = voie_de_reparation(lecture)`, soit « lot_fidele » pour « exact » comme pour « non exact »,
  et un arrêt sinon ;
- l'étape « reparation » refuse toute autre voie (l. 799-801) ;
- `exiger_config` refuse « passe_forcee » (l. 595).

Le texte, en revanche, garde « voie lue dans le témoin scellé », qui laisse croire à un choix. Le couple 17 le réécrit : la lecture est relue,
puis arrêt hors de « exact » ou « non exact », et elle ne choisit pas la voie.

Le reste est cohérent :
- P-T, le Statut, le critère « Témoin non exact » et le devis v2 (≈ 18 USD, au-delà des 5 à 12 USD du GO, sous son plafond de 60 USD) concordent.
- La Métrique garde `passe_forcee:…` comme troisième voie par cible, ce qui est exact : `consigner(..., "voie": f"passe_forcee:…")`, l. 913.

## 5. Résidus signalés par le rédacteur, et ceux que j'ajoute

| Résidu | Couple |
|---|---|
| Titre « v4, brouillon 1 » | Couple 1 → « brouillon 3 » |
| Statut de l'auteur « **Brouillon 1 (texte, non scellé)** » | Couple 2 |
| Métrique : « mesure à ajouter au code avant le scellement » | Couple 15 : mesure écrite par `mesure_independance` dans `lots_rapport[k]["independance_des_lignes"]`, non mesurée dans le repli à une cible |
| V4-E15 cite la v2 | Couple 16 : ajoute `resolution_graine_lot_v3.forcee_approchee`, que j'ai vérifiée identique à la v2 par `diff` |
| Liste d'arrêt : « 57 USD engagés » | Couple 14 : « 57 USD projetés à la vérification suivante, ou fin de l'amorce lue au journal », comme `decision_horaire` (`proj = dep + prix × (intervalle + marge)`, l. 216-230) et le devis v2, § 2 |

J'ajoute trois résidus que le rédacteur n'a pas signalés :
- V4-E12 dit aussi « alerte à 45 USD engagés, destruction à 57 USD engagés », alors que le code alerte à 45 engagés **ou projetés** : couple 13.
- Dans Essais, « témoin non exact → passe forcée » est la règle des essais de la v2 : le couple 18 le précise.
- Dans l'en-tête, la v3 remplace aussi `resolution_graine_lot_v2` dans les étapes, et la v2 reste importée par `chaine_table_v4_v1` pour
  `charger_table_v4` : couple 19.

Restent, sans couple :
- La section « Contre-lecture » dit « À faire » ; elle se remplit au scellement avec les deux empreintes, comme l'attend `prereg.problemes`.
  Sa liste de fichiers à lire (« deux modules », « le devis ») est vieillie.
- M3 n'est pas traité, mais le haut du devis v2 (≈ 24,9 h) reste sous le délai de 35 h.
- M4 est déclaré dans V4-E12 (« une destruction perd ce qui n'est pas poussé »).

## 6. Portée des 381 essais et des épreuves

**Sans changement de code.** Le commit de scellement n'ajoute que le texte, sous son nom scellé, et les compagnons. Les 381 essais, le banc, la
répétition et les épreuves valent si l'on vérifie au commit de scellement que chaque fichier de code cité a l'empreinte de `af1f2f4f`.
Les contrôles d'avant l'installation se rejouent au commit de scellement, comme le prévoit déjà le texte.

**Si C32 change un fichier de code**, il faut rejouer avant le scellement :
1. La suite complète avec le tokeniseur `0e9e39f2…`, au nouveau commit. Le compte change si un essai s'ajoute ; il faut alors mettre à jour
   « Tests attendus », V4-E10, la Liste d'arrêt, la Surveillance, les étapes 1 et 2 et les Essais.
2. Le banc v3, en entier, avec les mutations de surveillance comprises.
3. Les épreuves de dépense (`garde_depense_v4_v2 epreuves`, nouvelle sortie).
4. La répétition jouet des deux sessions, avec l'amorce v3 et le script v3 : cas sains, artefacts, surveillance sur ses journaux et recalcul de réception.
5. Les essais des gardes d'avant l'installation du script v3.
6. Les empreintes de l'en-tête, V4-E6, la commande de création (amorce v3) et l'étape 2.
7. Une nouvelle contre-lecture du delta.

Le pré-vol n'a pas à être rejoué : il n'importe pas `garde_depense`.

## Couples

`couples-contre-lecture-delta-brouillon3-v1.json` (19 couples, appliqués dans l'ordre).
- Couples 1 et 2 : titre et statut.
- Couples 3 à 12 : les trois lignes de tableau recollées.
- Couple 13 : V4-E12.
- Couple 14 : Liste d'arrêt.
- Couple 15 : Métrique.
- Couple 16 : V4-E15.
- Couple 17 : étape 3.
- Couple 18 : Essais.
- Couple 19 : en-tête.

Chaque « ancien » est unique dans le brouillon 3 et au moment de son application, vérifié par script sur une copie de travail.

Fin : 2026-11-04 08:13:36 UTC (`date -u`).
