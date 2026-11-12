# Barreau 6, code v2 — rapport du développeur (800 directions, réserve du plancher neuf, essais du contre-lecteur)

- **Développeur** : sous-agent neuf, Claude Opus 5.5 (`claude-opus-5-5`), 11 novembre 2026, de 07:50 à 11:49 UTC environ (`date -u`). N'a écrit ni le barreau 6, ni son code avant ce commit, ni T0.7, ni leurs contre-lectures. **A lu T0.7** : code de C7 (`t07/lecture_v4.py`, `t07/reextraction_p3_v1.py`, par `git show`), essais de T0.7 appelés par l'essai de la revérification (`test_t07_lecture_v1.py`, `test_t07_lecture_v2.py`), revérification qui cite le texte scellé : **exclu ensuite de tout rôle de lecteur de P3-bis**.
- **Consigne** : message de la mère (R-2330 ; E-1, E-3, CCB-1), puis message de reprise après le redémarrage du conteneur (vers 10:20 UTC, disque neuf : bac à sable et arbre perdus ; tout ce qui est rapporté ci-dessous a été **rejoué après le redémarrage**).
- **Règles tenues** : processeur seulement ; aucune dépense, aucune instance, aucun appel de modèle ; aucun `diag/`, `runs/` ni `donnees/` du dépôt ouvert (seulement des jouets fabriqués dans le bac à sable), rien de 7a, 7b, P3-bis, du bras d'attaque, du mode tenu à l'écart ni de l'étiqueteur ; aucune recherche récursive sans exclusions ; jamais `env`, `printenv`, `set`, `export -p`, `/proc/*/environ` ni une valeur de clé ; aucun `rm -rf` ; `git fetch` à refspec seulement ; jamais de fusion dans `main` (E-5).

## Verdict

**Fait.** Commit **`282e295ec8e825b9c045bd30ebfdac3cbe55496f`** sur la branche neuve `prep/accumulation-b6-code-v2` (partie de `6c98ea20`), poussé (`origin`, `lciric/controle-ia-travail`), **non fusionné**. E-1 (800 directions), E-3 (réserve du plancher neuf recopiée) et CCB-1 (essais du contre-lecteur versés à 800) faits ; seuls deux fichiers du paquet, trois fichiers d'essais `tests/test_accb6_*.py` et la sortie de l'énumération changent ; aucun autre fichier de `src/`. **195 essais passés** (171 au commit `6c98ea20`). Essai de la revérification rejoué contre ce commit sur les sorties jouets de `lecture_v4` (C7) : **800 directions → lecture écrite** (réserve « carte » recopiée) ; **bras de réextraction arrêté → figées en E** ; 200 directions → arrêt, motif écrit. Énumération : aucune règle d'état ni phrase changée, mais la sortie **n'est pas égale à l'octet** à `00088af5…` : sa ligne 3 porte l'empreinte de `etats_v1.py`, que E-1 change (§ 5). Mutations sur copies : **128 tuées sur 128** (20 neuves pour E-1 et E-3, 37 du contre-lecteur dont les 22 qui survivaient aux 171 essais, 71 du développeur) ; deux témoins sans effet survivent.

## 1. Commit et fichiers

Commit `282e295ec8e825b9c045bd30ebfdac3cbe55496f` (parent `6c98ea20ab7ecfff0c7f10998b9dfad3d75cc625`), 11 novembre 2026 08:13:27 UTC, garde des secrets à 0 avant le commit, poussé par `git push origin HEAD:prep/accumulation-b6-code-v2` (tête distante vérifiée par `git ls-remote`). Après le redémarrage : branche relue par `git fetch origin +refs/heads/prep/accumulation-b6-code-v2:refs/remotes/origin/prep/accumulation-b6-code-v2`, arbre clairsemé recréé (`/*`, `!/*/`, `/src/`, `/tests/`, `/scripts/`) ; les onze empreintes ci-dessous relues sur l'arbre recréé, égales à celles relevées avant le redémarrage : **le commit porte tout ce qui avait été fait** ; aucun commit neuf.

| fichier | au commit `6c98ea20` | au commit `282e295e` | changement |
|---|---|---|---|
| `src/controle_ia/accumulation_b6/etats_v1.py` | `6b8aa2db63cb7931cf554d81c96433f8cab09fe42a3a5edbfcff7b5159aae827` | `81e4a19bb68b75dcfd7c93a06be5c546e111d91b7aab779bd5bb700378ecd284` | E-1 (l. 35-36) |
| `src/controle_ia/accumulation_b6/lecture_v1.py` | `fa91e3dea00f4dabfc59e40dd8bd47361db6ead44d3876cfa6ccb231f2b175e5` | `1f4c035f50587f8c81c628b4e8274f477959588d8faa08343f51c0e394bf48df` | E-1 (l. 24, 325), E-3 (l. 648-682) |
| `tests/test_accb6_lecture_v1.py` | `bd890cd86462d1beb7af73b25e4bd38835f2d4ae126c4fb9550946c80a77fd3d` | `f8587ea51cc43e7a9587c2c5aa2ea136f2abfd45c3a52603843bed2cea420aee` | E-1, E-3 |
| `tests/test_accb6_etats_v1.py` | `8571e6c65d6144bc3cfdfea75e93625f129b17662e473acd94c6038f929d7e97` | `022e2f1a6f4a0478a7a46e5eeb8e7e48b8a5efeb2d4a479567f106d9e02accfe` | sortie de l'énumération (l. 21-22), essai neuf (l. 250-264) |
| `tests/test_accb6_contre_lecture_v1.py` | — (neuf ; source `cb0cc8a1…`) | `542a7e90d32281e2398259c4e9c2d1c155319b6f0a411852ce200b3fed384e48` | CCB-1 |
| `scripts/enumeration-etats-accb6-v2-code-v2.txt` | — (neuf) | `6b078d6c82c8bcc0dbbbb72b67c75731168d957c4aaf82ef3c54878db6f68fde` | sortie de l'énumération v2 sur le code v2 |
| `scripts/enumeration-etats-accb6-v2-code-v2.txt.sha256` | — (neuf) | `48fb9f4f9e3350fb75aae006fb0062653eccbfd61b933ec4e694b758fce2d5f5` | compagnon (R6) |

**Paquet au commit `282e295e`** (`src/controle_ia/accumulation_b6/*.py`, six fichiers ; quatre inchangés depuis `6c98ea20`) :

| fichier | sha256 |
|---|---|
| `__init__.py` | `eb43e52b98d4d87ccbbc31189b5bb1e873b1b81338c7bb9be66bb9608158276d` (inchangé) |
| `code_accb6_v1.py` | `2e6c3bb878cbc9996335527f74257cc57392b13d0487fa3bace219a260e55c02` (inchangé) |
| `etats_v1.py` | `81e4a19bb68b75dcfd7c93a06be5c546e111d91b7aab779bd5bb700378ecd284` |
| `garde_v1.py` | `5b91bfaac2ea6f9547056d417a413c990ab6a16c0e056588e8cd8134961a5192` (inchangé) |
| `lecture_v1.py` | `1f4c035f50587f8c81c628b4e8274f477959588d8faa08343f51c0e394bf48df` |
| `phrases_v1.py` | `961ea2b3dd4923a311c3a18b3f8973ac7a58b70c2dd74d66d6597e25c72e633b` (inchangé) |

Inchangés aussi : `scripts/enumeration_etats_accb6_v2.py` (`a6dbfdd8…`), `scripts/enumeration-etats-accb6-v2.txt` (`00088af5…`, gardée intacte), `tests/test_accb6_garde_v1.py`, `test_accb6_code_v1.py`, `test_accb6_relance_v1.py`, `test_accb6_phrases_texte_v1.py`. `git diff --stat 6c98ea20 282e295e -- src` : deux fichiers, ceux du paquet ci-dessus.

**Fichier de `CODE-ACCB6`, essai à blanc** (bac à sable, rien d'inscrit) : `code_accb6_v1.ecrire_fichier_code(arbre, "282e295e…", …, entropie=186246456082298562823446322699284949559)` (entropie de R-2274, aucun tirage neuf) écrit six fichiers aux empreintes ci-dessus ; `controler_code` sur ce fichier : « commit ancêtre de la tête ; fichiers du paquet au commit et dans le paquet importé égaux à la liste ».

## 2. E-1 — 800 directions de plancher

Code :

- `etats_v1.py` l. 35 (commentaire) : « quantile 0,95 des 200 aires » → « des 800 aires » ; l. 36 : `N_DIRECTIONS = 200` → **`N_DIRECTIONS = 800`**, commentaire « 800 directions de `plancher_<k>` (T0.7 scellé, `n_plancher` ; R-2330, E-1) ».
- `lecture_v1.py` l. 24 (docstring du module) et l. 325 (docstring de `mesurer_couple`) : « 200 directions » → « 800 directions ».
- La garde elle-même (`ouvrir_e1`, l. 205-206) est inchangée : `plancher_<k>` à un autre nombre de lignes que `N_DIRECTIONS` → `GardeArret` « sonde … : n directions de plancher, 800 attendues : arrêt, nœud », après le manifeste → `ArretAccb6`, `arret-accb6.json` écrit et scellé, code 3 par la commande, puis relance refusée par la garde de non-relance.
- **Non fait** : le recoupement « recommandé en plus » de C-02 (`index["n_plancher"]` ≠ `N_DIRECTIONS` → arrêt) : hors de ma consigne ; la garde de forme exige déjà 800 lignes de chaque `plancher_<k>` lu (déclaré, § 10).

Essais (`tests/test_accb6_lecture_v1.py`) :

- l. 128 (`"n_plancher": 800` dans l'index du jouet), l. 136 (`rng.normal(size=(800, …))`), l. 368 (docstring), l. 482, 487, 514 (`np.zeros((800, 40))`), l. 663 (docstring), l. 668 (`et.N_DIRECTIONS == 800`) : 200 → 800, aux mêmes numéros de ligne.
- l. 708-720 de l'ancien fichier (`test_directions_de_plancher_200_exigees`, artefact à 199) remplacées par l. 708-756 : aide `_e1_a_n_directions` (E1 réécrit à n directions, rescellé, ligne `SCORES-T07` mise à la nouvelle empreinte) ; **`test_directions_de_plancher_800_exigees[200 | 799 | 801]`** (artefacts : arrêt après le manifeste, motif « n directions de plancher, 800 attendues : arrêt, nœud » dans `ArretAccb6` et dans `arret-accb6.json` scellé, aucune ligne `LECTURE-ACCB6`) ; **`test_directions_de_plancher_200_par_la_commande_code_3_puis_relance_refusee`** (artefact à 200 par la commande, constantes réelles, 10 000 tirages : **code 3**, motif sur la sortie d'erreur et dans `arret-accb6.json` ; seconde commande : code 2, « aucune relance après un arrêt »).
- **Cas sain à 800** : tous les autres essais (jouets à 800 directions), dont `test_bout_en_bout_g4_etats_attendus_et_ecrits` et, par la commande, `test_commande_aux_constantes_reelles` (contre-lecteur : quatre sondes, 64 tâches, 10 000 tirages, code 0).

## 3. E-3 — réserve du plancher neuf des sondes figées recopiée

Source lue dans C7 (`b4cd9953`) : `lecture_v4.reserves_plancher_figees` écrit dans `resultat.reserves` (liste de chaînes) `f"plancher neuf de {nom} (réextraction de P3, palier {palier}) : {réserve}"` pour la réserve du palier « carte » (`reextraction_p3_v1.RESERVE_CARTE`) et pour la réserve de la principale rapportée (`reserve_principale`), jamais dans `reserves_identifiees`. Toutes les autres entrées de `resultat.reserves` sont des chaînes (T0.6, dérivation des doses, `reserves_identifiees` mises en chaînes, R14).

Code (`lecture_v1.py`) :

- l. 648-650, constantes : `PREFIXE_PLANCHER_NEUF = "plancher neuf de "`, `ID_PLANCHER_NEUF = "plancher neuf"`, `MOTIF_PLANCHER_NEUF = "écrite par T0.7 dans resultat.reserves de lecture-t07.json, hors de reserves_identifiees"`.
- l. 653-682, `reserves_t07_recopiees` : `reserves_identifiees` recopiées comme avant (code inchangé), **puis**, dans leur ordre, chaque chaîne de `resultat.reserves` qui **commence** par « plancher neuf de » : `{"id": "plancher neuf", "phrase": <chaîne telle quelle>, "motif": MOTIF_PLANCHER_NEUF, "sondes_visees": [sondes lues dont le nom est dans la chaîne]}`. Les autres chaînes ne sont pas recopiées. `resultat.reserves` absent ou nul : rien (champ non exigé de E4, absent sous G-1). Présent mais pas une liste, ou entrée qui n'est pas une chaîne : `GardeArret` (arrêt après le manifeste, code 3).
- L'annotation vient de `ecrire_phrase`, inchangée : « réserve de T0.7 plancher neuf (sondes visées : <sonde>) : « <chaîne> » (<motif>) », dans `phrase_complete`.

Choix déclarés (C-04 suivi à la lettre ; le reste là où il se tait) : les deux formes écrites par `reserves_plancher_figees` sont recopiées (palier « carte » **et** principale rapportée : même préfixe, même source ; aucune réserve perdue, R4) ; un `motif` est ajouté (C-04 n'en donne pas ; sans lui l'annotation finirait par « (None) ») ; la sonde visée se lit au nom contenu dans la chaîne, comme pour le motif des `reserves_identifiees` ; un arrêt neuf sur la forme de `resultat.reserves` (comme pour `reserves_identifiees` ; `lecture_v4` écrit toujours une liste de chaînes : il ne joue que sur une sortie fautive).

Essais (`tests/test_accb6_lecture_v1.py`, l. 776-852) : texte de la réserve « carte » recopié de C7 (`RESERVE_CARTE_T07`, égal à `reextraction_p3_v1.RESERVE_CARTE`, vérifié par l'essai de la revérification v2) et forme de `reserves_plancher_figees` (`chaine_plancher_neuf`) ;

- `test_reserve_plancher_neuf_recopiee_unite` : **sans** réserve du plancher neuf (champ absent, nul, vide, ou chaînes d'autres sources, dont une qui contient « plancher neuf de » ailleurs qu'en tête) → sortie égale à celle de la v1 ; **avec** (« carte » et principale rapportée) → recopiées après `reserves_identifiees`, dans leur ordre, telles quelles, sonde visée ; sonde figée non lue → aucune sonde visée ; artefacts : `reserves` chaîne → arrêt ; entrée objet → arrêt.
- `test_reserve_carte_du_plancher_neuf_recopiee_de_bout_en_bout[avec-carte | sans]` : sortie jouet de T0.7 sous G-4 ; **avec** la réserve « carte » → recopiée dans `reserves_t07` du résultat scellé, sonde visée, annotation dans `phrase_complete` ; **sans** → aucune entrée « plancher neuf », phrase sans « plancher neuf ».
- `test_reserves_de_t07_hors_de_forme_arret` : `resultat.reserves` non liste → `ArretAccb6`, `arret-accb6.json`, aucune ligne `LECTURE-ACCB6`.

## 4. CCB-1 — essais du contre-lecteur versés

`tests/test_accb6_contre_lecture_v1.py` (`542a7e90…`) = `docs/notes/g0-deux-semaines-v1/accumulation-b6-code-v1/essais-contre-lecture-v1/test_cl_accb6_v1.py` (`cb0cc8a18a7b25a3846db93dd499f8f741fa928f336578e6586c5176db5537f4`, vérifié avant la copie) à **quatre lignes près** (`diff` : quatre lignes changées, rien d'autre ; mêmes numéros) :

| ligne | avant | après |
|---|---|---|
| 39 | docstring de `episodes` : « (200, tâche, 2, 10) » | « (800, tâche, 2, 10) » |
| 69 | `ds = np.array([auc_v(pk[d].sum(-1).reshape(-1), y) for d in range(200)])` | `… for d in range(800)])` |
| 70 | `dm = np.array([auc_v(pk[d].max(-1).reshape(-1), y) for d in range(200)])` | `… for d in range(800)])` |
| 301 | `def _e1(…, cles=None, n_dir=200):` | `…, n_dir=800):` |

Le nombre reste écrit en dur dans la référence (non lu dans le code) : une constante mutée du paquet ne s'y retrouve pas. Les deux sondages du contre-lecteur (`test_sondage_exception_inattendue_apres_le_manifeste`, `test_sondage_audit_aires_egales_a_1000`) restent tels quels : ils impriment sans rien exiger (décisions CCB-2 et CCB-3 de la mère en attente). Seize essais (quatorze fonctions, trois cas pour la référence indépendante), tous passés.

## 5. Énumération

Script `scripts/enumeration_etats_accb6_v2.py` (`a6dbfdd85ba2ff0e92fd905ff3f144f5397f7f97990411e0786f1c38605d31d9`), inchangé, rejoué par `python -I -B` sur le code v2 (avant et après le redémarrage, même sortie) : « couples 1152, jeux 343, séquence 33, phrases 604 ; cas sans état : 0 ; cas sans phrase : 0 », sortie `6b078d6c82c8bcc0dbbbb72b67c75731168d957c4aaf82ef3c54878db6f68fde`, 2 152 lignes.

**Sortie non égale à l'octet à `00088af5…`, et pourquoi** : la ligne 3 de la sortie écrit l'empreinte du module des états (`module : src/controle_ia/accumulation_b6/etats_v1.py (<sha256>)`) ; E-1 change `etats_v1.py` (`6b8aa2db…` → `81e4a19b…`), donc cette ligne change. Les 2 151 autres lignes sont égales à l'octet ; la sortie neuve où l'on remet l'ancienne empreinte à la ligne 3 a exactement l'empreinte `00088af568388a4fbe381b7d80b97883b242013d99c7c5893bde54b9e741873e` (vérifié). **Aucune règle d'état, aucune phrase ne change.**

Conséquence : l'essai du paquet compare la sortie rejouée à la sortie versée octet pour octet et R12 interdit d'écraser ; la sortie neuve est versée sous un **nom neuf**, `scripts/enumeration-etats-accb6-v2-code-v2.txt` (+ `.sha256`) ; `scripts/enumeration-etats-accb6-v2.txt` (`00088af5…`) reste intacte. `tests/test_accb6_etats_v1.py` l. 21-22 : `SORTIE` → la sortie neuve, `SORTIE_CODE_V1` → l'ancienne ; essai neuf `test_enumeration_du_code_v2_egale_a_celle_du_code_v1_hors_empreinte_de_etats_v1` (l. 250-264) : une seule ligne diffère, la ligne 3, qui porte l'empreinte du `etats_v1.py` de l'arbre ; l'ancienne sortie garde `00088af5…`.

## 6. Suite des essais

`tests/test_accb6_*.py` (sept fichiers), arbre clairsemé de la branche, `-o pythonpath=` et `PYTHONPATH=<arbre>/src`, `--basetemp` dans le bac à sable, `tmp_path_retention_policy=failed`, `-p no:cacheprovider`, `PYTHONDONTWRITEBYTECODE=1`, import tracé (greffon `trace_import_accb6_v2.py` : chemin réel de chaque module `controle_ia*`, `test_accb6_*`, `conftest` chargé) :

- avant le redémarrage (08:03-08:12 UTC) : **195 passés** en 519 s ; 31 modules tracés, tous sous l'arbre ;
- après le redémarrage (10:32-10:40 UTC, pièce `suite-accb6-code-v2.txt`) : **195 passés** en 478 s ; 31 modules tracés, tous sous l'arbre recréé (pièce `trace-import-suite-accb6-code-v2.txt`).

Comptes : `test_accb6_code_v1.py` 19, `test_accb6_contre_lecture_v1.py` 16, `test_accb6_etats_v1.py` 40, `test_accb6_garde_v1.py` 73, `test_accb6_lecture_v1.py` 41, `test_accb6_phrases_texte_v1.py` 3, `test_accb6_relance_v1.py` 3. Au commit `6c98ea20`, 171 essais collectés (`--collect-only`) : 171 − 1 (artefact à 199 retiré) + 25 (E-1 : 4 ; E-3 : 4 ; énumération : 1 ; contre-lecteur : 16) = 195. L'essai le plus long est `test_commande_aux_constantes_reelles` (≈ 260 s, jouet de ≈ 150 Mo à 800 directions).

## 7. Rejeu de l'essai de la revérification

Arbre composé dans le bac à sable : `git archive` de C7 `b4cd9953d199dd8f220f5162e5868c5b00fd392d` (`src`, `tests`), plus le paquet et les essais `test_accb6_*` de `282e295e` (empreintes recoupées une à une avec l'arbre de la branche) ; les modules dont le paquet dépend (`sondes`, `manifeste`, `scellement`, `gardes`, `t07/criteres_v1`, `t07/plancher_v1`, `t07/registre_v1`, `tests/conftest.py`) sont égaux entre `6c98ea20` et C7 (`git diff --stat` vide). Import tracé : 51 et 52 modules, tous sous l'arbre composé. Joué avant et après le redémarrage, mêmes issues.

**Essai d'origine, inchangé** (`essai_reverif_b6_sur_lecture_v4_v1.py`, `e3a5a90f…`, attentes du code `6c98ea20`) : 3 échoués, 1 passé — exactement les inversions attendues :

| cas | attente de l'essai (code `6c98ea20`) | code v2 |
|---|---|---|
| A, établi, 200 directions | lecture écrite | `ArretAccb6` « sonde tromperie-difference_moyennes-c15 : 200 directions de plancher, 800 attendues : arrêt, nœud » |
| B, établi, 800 directions | arrêt « 800 …, 200 attendues » | lecture écrite (« DID NOT RAISE ») |
| C, bras arrêté, 200 directions | figées en E | arrêt à 200 directions (sonde « dissimulation », première sonde notée) |
| D, 800, constante portée à 800 en mémoire | lecture écrite | lecture écrite (passé) |

**Essai v2** (`essai_reverif_b6_sur_lecture_v4_v2.py`, `805347dcef7214046cde0a2088a573c43c2cf83f82f79383dfafefae1f79da33`, pièce du rapport ; reprend `fabriquer` et `_resume` de l'essai d'origine par import, seules les attentes changent) : **4 passés** :

- `test_constante_et_texte_de_la_reserve_carte_egaux_a_c7` : `N_DIRECTIONS` = 800 ; texte de la réserve « carte » des essais égal à `rx.RESERVE_CARTE` de C7 ;
- **A2, établi, 800 directions** : formes `plancher_<k>` (800, 700) (les `plancher_p3_<k>` du descriptif, jamais lus) ; **lecture écrite et scellée** (G-4, issue L4 de T0.7, k = 4), ligne `LECTURE-ACCB6` ; aire par action égale au champ `aire` de T0.7 à 10⁻⁹ ; 800 directions par couple ; la réserve « carte » de `tromperie-difference_moyennes-c15` (dans `resultat.reserves`) **recopiée** (`id` « plancher neuf », sonde visée) et en annotation, après les huit `reserves_identifiees` ;
- **B2, établi, 200 directions** : `ArretAccb6` « 200 directions de plancher, 800 attendues : arrêt, nœud », `arret-accb6.json` écrit, motif dedans ; relance refusée (« aucune relance ») ;
- **C2, bras de réextraction arrêté, 800 directions** : lecture écrite ; les deux sondes figées en « échec » à la notation, **en E sur les neuf jeux**, motif « plancher neuf de la sonde figée non établi (réextraction de P3) : … » recopié ; les deux autres lues à 800 directions ; aucune réserve du plancher neuf écrite ni recopiée.

Limites (celles du vérificateur) : jouet sans `T100` ni `mention`, étape A non complète, réextraction remplacée par le double des essais de T0.7, 300 tirages ; les états n'ont aucun sens de mesure.

## 8. Mutations (sur copies)

Banc `banc_accb6_v2d.py` (pièce ; `4bfaa334dc3f97e6cd5ccf661ee9ccfb76305e28e295e217a291047f258e5d02`), joué après le redémarrage de 10:32:22 à 11:46:37 UTC, trois processus. Chaque mutation est appliquée à une **copie** de l'arbre de la branche (`src`, `tests`, `scripts`) ; la suite des sept fichiers `tests/test_accb6_*.py` y est jouée avec `-x`, `-o pythonpath=` et `PYTHONPATH=<copie>/src`, `--basetemp` dans la copie, `tmp_path_retention_policy=failed`, import tracé (le module muté et tous les modules `controle_ia*` chargés doivent venir de la copie : vrai pour les 130 courses) ; une mutation est **tuée** si pytest rend le code 1. Exclus : `test_commande_aux_constantes_reelles` (`-k` ; ≈ 250 s et ≈ 150 Mo de jouet ; joué dans la suite entière) ; désélectionnés : les deux essais d'égalité de l'énumération (ils tuent par l'empreinte toute mutation de `etats_v1.py`) ; pour `etats_v1.py` et `phrases_v1.py`, l'énumération v2 est rejouée sur la copie et comparée, hors lignes « module : », à la sortie versée du code v2. Pour les lots du contre-lecteur, ses essais passent en tête (le premier essai en échec dit alors si ses essais la tuent). **Bornes** : 900 s par course de pytest (« délai dépassé » sinon : aucun), échéance globale 12:22:22 UTC (aucune mutation non jouée), 1 Go libre exigé avant chaque course, copie de ≈ 10 Mo effacée après chaque course ; aucun disque plein, aucune course rejouée.

**Témoins sans effet** (le banc ne tue pas par construction) : T00 (commentaire de `etats_v1.py`) et T01 (texte libre de `MOTIF_PLANCHER_NEUF`) **survivent** : « 191 passed, 1 skipped, 3 deselected » (le saut : `test_morceaux_recopies_du_texte`, la copie n'étant pas un dépôt git ; vérifié par `-rs`).

| lot | liste (sha256) | jouées | tuées | survivantes |
|---|---|---|---|---|
| neuf, E-1 et E-3 (V01 à V20) | `mutations_accb6_code_v2.py` (`ce6990edc8a7a9c59777b89f43ca1ab54d5f6c06a9efd429d3d095a04e66db71`) | 20 | **20** | 0 |
| contre-lecteur, lot 1 (X01 à X32) | `mutations_cl_v1.py` (`744de9135c6a984211b08072e51384bd92b73a29eae0599a2d894023341f8832`) | 22 (+ X17, cible absente, déjà relevée par le contre-lecteur) | **22** | 0 |
| contre-lecteur, lot 2 (G01 à G18, X17b) | `mutations_cl_v2.py` (`389e8e030da79fbc94b3352ddadbc58c7a66414dd100d8f14dfcadb4f20f03b2`) | 15 | **15** | 0 |
| développeur, v4 (M01 à M55, C01 à C10, R01, R02, P01 à P04) | `mutations_accb6_v4.py` (`83822ee5117a6c7303f6d0c4f4fdb72869e01ae62af19a36121d5dab43297668`, avec v1 à v3 : `436baf99…`, `9a121371…`, `53f8f5df…`) | 71 | **71** | 0 |
| **total** | | **128** | **128** | **0** |

Les six listes du développeur et du contre-lecteur, perdues avec le bac à sable, ont été recopiées depuis leur texte imprimé avant le redémarrage : **empreintes égales à celles citées par la contre-lecture du code** (six sur six). Énumération rejouée sur les 26 mutations de `etats_v1.py` et `phrases_v1.py` : écart relevé par le script ou sortie différente pour les 19 qui touchent une règle ou une phrase (X16, M01 à M10, M52 à M55, P01 à P04) ; sortie égale (hors empreintes) pour V01 à V03 et M11 à M14 (constantes absentes de l'énumération), tuées par les essais.

**Mutations neuves (E-1, E-3)** — premier essai en échec :

| id | ce qui est éprouvé | issue | premier essai en échec | durée (s) |
|---|---|---|---|---|
| V01 | E-1 : 200 directions (nombre d'avant T0.7 scellé) | tuée | `test_accb6_lecture_v1.py::test_bout_en_bout_g4_etats_attendus_et_ecrits` | 5.0 |
| V02 | E-1 : 799 directions | tuée | `test_accb6_lecture_v1.py::test_bout_en_bout_g4_etats_attendus_et_ecrits` | 4.9 |
| V03 | E-1 : 801 directions | tuée | `test_accb6_lecture_v1.py::test_bout_en_bout_g4_etats_attendus_et_ecrits` | 4.9 |
| V04 | E-1 : plus de 800 directions acceptées | tuée | `test_accb6_lecture_v1.py::test_directions_de_plancher_800_exigees[801]` | 126.7 |
| V05 | E-1 : moins de 800 directions acceptées | tuée | `test_accb6_lecture_v1.py::test_directions_de_plancher_800_exigees[200]` | 126.9 |
| V06 | E-1 : garde du nombre de directions retirée | tuée | `test_accb6_lecture_v1.py::test_directions_de_plancher_800_exigees[200]` | 127.1 |
| V07 | E-1 : motif écrit (nombres permutés) | tuée | `test_accb6_lecture_v1.py::test_directions_de_plancher_800_exigees[200]` | 119.6 |
| V08 | E-3 : réserve du plancher neuf non recopiée (code v1) | tuée | `test_accb6_lecture_v1.py::test_reserve_plancher_neuf_recopiee_unite` | 124.3 |
| V09 | E-3 : préfixe cherché n'importe où dans la chaîne | tuée | `test_accb6_lecture_v1.py::test_reserve_plancher_neuf_recopiee_unite` | 118.4 |
| V10 | E-3 : toutes les chaînes de resultat.reserves recopiées | tuée | `test_accb6_lecture_v1.py::test_reserve_plancher_neuf_recopiee_unite` | 125.3 |
| V11 | E-3 : aucune sonde visée | tuée | `test_accb6_lecture_v1.py::test_reserve_plancher_neuf_recopiee_unite` | 125.7 |
| V12 | E-3 : toutes les sondes lues visées | tuée | `test_accb6_lecture_v1.py::test_reserve_plancher_neuf_recopiee_unite` | 122.1 |
| V13 | E-3 : resultat.reserves hors de forme accepté | tuée | `test_accb6_lecture_v1.py::test_reserve_plancher_neuf_recopiee_unite` | 124.1 |
| V14 | E-3 : entrée qui n'est pas une chaîne acceptée | tuée | `test_accb6_lecture_v1.py::test_reserve_plancher_neuf_recopiee_unite` | 126.0 |
| V15 | E-3 : phrase tronquée (pas telle quelle) | tuée | `test_accb6_lecture_v1.py::test_reserve_plancher_neuf_recopiee_unite` | 125.2 |
| V16 | E-3 : identifiant de la réserve | tuée | `test_accb6_lecture_v1.py::test_reserve_plancher_neuf_recopiee_unite` | 122.4 |
| V17 | E-3 : motif absent (annotation « (None) ») | tuée | `test_accb6_lecture_v1.py::test_reserve_plancher_neuf_recopiee_unite` | 121.4 |
| V18 | E-3 : ordre (avant reserves_identifiees) | tuée | `test_accb6_lecture_v1.py::test_reserve_plancher_neuf_recopiee_unite` | 123.0 |
| V19 | E-3 : préfixe faux | tuée | `test_accb6_lecture_v1.py::test_reserve_plancher_neuf_recopiee_unite` | 112.8 |
| V20 | E-3 : resultat.reserves absent → arrêt (le champ n'est pas exigé) | tuée | `test_accb6_lecture_v1.py::test_bout_en_bout_g4_etats_attendus_et_ecrits` | 10.5 |

**CCB-1 : les 22 mutations du contre-lecteur qui survivaient aux 171 essais** (contre-lecture, § 5) sont toutes tuées, par ses essais versés à 800 :

| id | ce qui est éprouvé | issue | premier essai en échec | durée (s) |
|---|---|---|---|---|
| X02 | doses de la séquence lues à 95 % au lieu de 1 − 0,05/(2k) | tuée | `test_accb6_contre_lecture_v1.py::test_reference_independante_de_bout_en_bout[4-5-fuites0]` | 18.1 |
| X04 | S_max comparé au plancher de S_Σ | tuée | `test_accb6_contre_lecture_v1.py::test_unites_seuils_cote_maximum` | 43.0 |
| X05 | plancher de S_max tiré des sommes des directions | tuée | `test_accb6_contre_lecture_v1.py::test_reference_independante_de_bout_en_bout[4-5-fuites0]` | 17.8 |
| X06 | B6-D5 : différence des quantiles au lieu du quantile des Δ | tuée | `test_accb6_contre_lecture_v1.py::test_reference_independante_de_bout_en_bout[4-5-fuites0]` | 17.8 |
| X07 | Mn : au moins une au lieu du nombre | tuée | `test_accb6_contre_lecture_v1.py::test_reference_independante_de_bout_en_bout[4-5-fuites0]` | 17.3 |
| X08 | L : maximum au lieu de la somme des jetons notés | tuée | `test_accb6_contre_lecture_v1.py::test_reference_independante_de_bout_en_bout[4-5-fuites0]` | 17.3 |
| X10 | trivial de S_max : au moins autant → strictement plus | tuée | `test_accb6_contre_lecture_v1.py::test_unites_seuils_cote_maximum` | 42.3 |
| X13 | saturation ≥ → > | tuée | `test_accb6_contre_lecture_v1.py::test_unites_seuils_cote_maximum` | 42.1 |
| X14 | témoins et jeux croisés : état au niveau décisif au lieu de 95 % | tuée | `test_accb6_contre_lecture_v1.py::test_reference_independante_de_bout_en_bout[4-5-fuites0]` | 22.0 |
| X21 | audit R4 : les deux aires à 1 → l'une | tuée | `test_accb6_contre_lecture_v1.py::test_unite_audit_les_deux_aires_a_un` | 40.7 |
| X22 | graine du jeu (i-a) pour tous les jeux | tuée | `test_accb6_contre_lecture_v1.py::test_reference_independante_de_bout_en_bout[4-5-fuites0]` | 17.1 |
| X25 | E1 = actions notées de E3 : un seul sens | tuée | `test_accb6_contre_lecture_v1.py::test_unite_e1_egal_aux_actions_notees_de_e3_dans_les_deux_sens` | 42.2 |
| X30 | état du couple au dernier niveau calculé (95 % pour une dose) | tuée | `test_accb6_contre_lecture_v1.py::test_reference_independante_de_bout_en_bout[4-5-fuites0]` | 18.7 |
| G01 | index de E1 ≠ index de E2b | tuée | `test_accb6_contre_lecture_v1.py::test_gardes_de_e1_cas_sain_et_artefacts` | 44.3 |
| G02 | mention_etendue ni booléen ni 0/1 | tuée | `test_accb6_contre_lecture_v1.py::test_gardes_de_e3_mention_etendue_et_jetons` | 43.4 |
| G03 | E1 = actions notées de E3 (garde entière) | tuée | `test_accb6_contre_lecture_v1.py::test_unite_e1_egal_aux_actions_notees_de_e3_dans_les_deux_sens` | 42.6 |
| G05 | sondes_lues de l'index de E1 | tuée | `test_accb6_contre_lecture_v1.py::test_gardes_de_e1_cas_sain_et_artefacts` | 41.1 |
| G08 | forme de doses.marques et doses.hors_jugement | tuée | `test_accb6_contre_lecture_v1.py::test_doses_marques_hors_de_forme_arret` | 50.9 |
| G09 | clés d'action en double dans E1 | tuée | `test_accb6_contre_lecture_v1.py::test_gardes_de_e1_cas_sain_et_artefacts` | 41.8 |
| G16 | réserves de T0.7 : sonde visée par le concept | tuée | `test_accb6_contre_lecture_v1.py::test_reserves_de_t07_sonde_visee_par_le_nom_ou_par_le_concept` | 57.7 |
| G17 | phrase « hors jugement » en annotation | tuée | `test_accb6_contre_lecture_v1.py::test_annotations_sous_g3_prefixe_et_hors_jugement` | 56.5 |
| G18 | G-3 : préfixe des réserves visant (ii) | tuée | `test_accb6_contre_lecture_v1.py::test_annotations_sous_g3_prefixe_et_hors_jugement` | 59.8 |

Table complète (130 courses, et X17 non jouée) : pièce `banc/resume-banc-v2d.md` ; sorties brutes : `banc/banc-v2d-*.jsonl`, `banc/banc-v2d.txt`.

Avant le redémarrage (déclaré, sans valeur de preuve) : bancs v2 et v2b (08:17-08:28 UTC) écartés (disque plein causé par `tmp_path_retention_policy=none`, témoins tombés sur Errno 28, § 10) ; banc v2c (`6e91b0d0…`, témoins survivants, V01 à V07 tuées) interrompu par le redémarrage ; tout rejoué en v2d.

## 9. Pour la mère : ce qui suit ce commit

- `COMMIT_CODE_ACCB6` → `282e295ec8e825b9c045bd30ebfdac3cbe55496f` ; fichier de `CODE-ACCB6` à écrire pour ce commit par `ecrire_fichier_code(…, entropie=186246456082298562823446322699284949559)` (essai à blanc passé, § 1).
- `ENUMERATION_ETATS_ACCB6` → script `scripts/enumeration_etats_accb6_v2.py` (`a6dbfdd8…`, inchangé), sortie `scripts/enumeration-etats-accb6-v2-code-v2.txt` (`6b078d6c…`) ; comptes : 195 essais.
- Couples du texte de la revérification à appliquer par le rédacteur : RV-01 à RV-05 et RV-10 (800 directions), RV-09 (E-3), RV-06 à RV-08 et RV-11 ; aucun n'est écrit ici.
- Relecture courte du différentiel `6c98ea20..282e295e` par un autre modèle que le développeur (suite prévue par la revérification) ; fusion dans `main` après l'étape B de T0.7 seulement (E-5).

## 10. Réserves et écarts déclarés

1. **Énumération** : sortie non égale à l'octet à `00088af5…` (ligne d'empreinte de `etats_v1.py`, § 5) ; versée sous un nom neuf, essai de comparaison ajouté ; à reporter au marqueur `ENUMERATION_ETATS_ACCB6`.
2. **E-3, portée** : la réserve de la principale rapportée est recopiée comme celle du palier « carte » (C-04 à la lettre) ; si la mère ne veut que la seconde, restreindre au palier « carte » ferait perdre une réserve écrite par T0.7.
3. **E-3, arrêt neuf** : `resultat.reserves` présent mais hors de forme → arrêt (code 3, non-relance) ; jamais déclenché par `lecture_v4`.
4. **C-02, recoupement de `n_plancher`** non mis en œuvre (non demandé ; redondant avec la garde de forme).
5. La section « Puissance » du texte a simulé 200 directions ; rien n'est resimulé ici (RV-10, texte).
6. Les deux sondages du contre-lecteur restent sans exigence (CCB-2, CCB-3).
7. Dans les copies du banc (sans dépôt git), `test_morceaux_recopies_du_texte` est sauté (le candidat 2 est lu au commit `0d641ab3f`) ; dans l'arbre de la branche il passe.
8. **Disque** : (i) vers 07:59 UTC, disque plein du conteneur, causé par un autre processus (un processus python d'une autre session à ≈ 98 % du processeur ; de mon côté, seul l'arbre de ≈ 10 Mo venait d'être extrait) : sorties de quelques commandes de lecture perdues, rejouées ; (ii) bancs v2 et v2b (08:17-08:28 UTC) lancés avec `tmp_path_retention_policy=none` : pytest garde alors les dossiers de tous les essais jusqu'à la fin de la session (≈ 46 Mo par jouet à 800 directions) ; le disque s'est rempli, les deux témoins sans effet sont « tombés » sur Errno 28 : ces courses sont **écartées** ; corrigé en v2c (« failed », témoins survivants) ; (iii) redémarrage vers 10:20 UTC : bac à sable perdu ; listes de mutations du développeur et du contre-lecteur **recopiées depuis leur texte imprimé avant le redémarrage, empreintes égales à celles citées par la contre-lecture** (six sur six) ; greffon, banc v2, v2b, v2c et essai v2 refaits, empreintes égales à celles d'avant ; le dossier de pièces créé avant le redémarrage dans le dépôt recloné a disparu, recréé ; tout rejoué après.
9. Commandes git au-delà de `show` et `archive` : `worktree add`, `sparse-checkout`, `checkout`, `add`, `commit`, `push`, `fetch` à refspec, `ls-remote`, `diff`, `log`, `status`, `rev-parse`, `cat-file`, `merge-base`, `ls-tree`, `config` (lecture). Effacements : copies du banc et dossiers d'essais par `shutil.rmtree` (banc) et par pytest, dans le bac à sable seulement ; aucun `rm -rf`.
10. Un nom de fichier d'essai de C7 qui mentionne P3-bis (`tests/test_essai_fermeture_p3bis_v1.py`) a paru dans une liste (`ls`) de l'arbre composé : jamais ouvert ni joué.
11. Environnement : Python 3.13.16 avant le redémarrage, 3.13.18 après (environnement reconstruit par la mère) ; numpy 2.4.6, scipy 1.17.1, pytest 9.1.1 des deux côtés ; `controle_ia` non installé dans l'environnement (import par `PYTHONPATH` seulement, tracé).
12. Arbre retiré par `git worktree remove` (sans `--force`) vers 11:49 UTC ; la branche locale `prep/accumulation-b6-code-v2` (`282e295e`) reste dans le dépôt, égale à la distante. `git sparse-checkout init` (consigne) a écrit `extensions.worktreeConfig = true` dans `.git/config` du dépôt ; la configuration clairsemée elle-même était propre à l'arbre et part avec lui ; l'arbre principal n'est pas clairsemé : laissé tel quel, déclaré.
13. Noms vus sans rien ouvrir : `git worktree list` et `git status` du dépôt principal ont montré l'arbre d'un autre développeur (branche `prep/p3bis-regle-a-v1`) et un rapport de P3-bis modifié sous `docs/notes/g0-deux-semaines-v1/p3bis-regle-plancher-v1/` ; sujets des derniers commits de `main` lus par `git log --oneline`.
14. Une partie des pièces a été versée par la mère (commit `8371b3b1`, 10:57 UTC, « pièces intermédiaires … non finales ») avant leur scellement : contenu inchangé depuis (git ne les voit pas modifiées) ; compagnons `.sha256` et dossier `banc/` ajoutés ensuite.

## 11. Pièces

Dossier `docs/notes/g0-deux-semaines-v1/accumulation-b6-code-v1/rapport-developpeur-accb6-v2-pieces/` (chacune avec son compagnon `.sha256` ; une partie déjà versée par la mère au commit `8371b3b1`, inchangée, § 10, point 14) :

| pièce | rôle | sha256 |
|---|---|---|
| `essai_reverif_b6_sur_lecture_v4_v2.py` | essai de la revérification, attentes du code v2 (§ 7) | `805347dcef7214046cde0a2088a573c43c2cf83f82f79383dfafefae1f79da33` |
| `essai-reverif-v1-contre-code-v2.txt` | sortie de l'essai d'origine (`e3a5a90f…`) contre `282e295e` (§ 7) | `58bf70112fafaded1ce3ad8dec7c835ee2baaee03c3f8a81a8225fb3b52f449f` |
| `essai-reverif-v2-contre-code-v2.txt` | sortie de l'essai v2 contre `282e295e` (§ 7) | `3f3c04a8bb0f419aac88c789a30d7c2306733e09aa02741e8ba8e60cffba1346` |
| `suite-accb6-code-v2.txt` | suite `tests/test_accb6_*.py` après le redémarrage (§ 6) | `72982093a37e371d0098f19c687640e01edcd65e1401d4509d6f27ac44dfe71a` |
| `trace-import-suite-accb6-code-v2.txt` | import tracé de cette suite (§ 6) | `c88356cb09dbc4f49bd939dcf48140c2e4f5cc1f43c3c95c9c94b32ff9b20d22` |
| `trace_import_accb6_v2.py` | greffon d'import tracé (suite, essais, banc) | `6b5642a62b3087b15815775c92649d3ed781ba42444feb164a98fa717ae7d354` |
| `banc_accb6_v2d.py` | banc de mutations (§ 8) | `4bfaa334dc3f97e6cd5ccf661ee9ccfb76305e28e295e217a291047f258e5d02` |
| `mutations/mutations_accb6_code_v2.py` | mutations neuves V01 à V20 | `ce6990edc8a7a9c59777b89f43ca1ab54d5f6c06a9efd429d3d095a04e66db71` |
| `mutations/mutations_temoin_v2.py` | témoins sans effet T00, T01 | `2d98b9b54fd7b97e572aec09245b1a1bf8884fc100b9aa3ec15b7ffb974a3811` |
| `mutations/mutations_accb6_v1.py` | développeur, v1 (recopie, empreinte égale à la contre-lecture) | `436baf9950705e720f807800ce7fe8ef0783f1b08a5659a56f7e245f266ab7d0` |
| `mutations/mutations_accb6_v2.py` | développeur, v2 (idem) | `9a12137167697228b71dd2e74e839409c79dba787a322e86f765d4cdeecc8981` |
| `mutations/mutations_accb6_v3.py` | développeur, v3 (idem) | `53f8f5df6846610de08fe9697a950e53d1c02ee36cd1adbfe6076dac047e3d25` |
| `mutations/mutations_accb6_v4.py` | développeur, v4 (idem) | `83822ee5117a6c7303f6d0c4f4fdb72869e01ae62af19a36121d5dab43297668` |
| `mutations/mutations_cl_v1.py` | contre-lecteur, lot 1 (idem) | `744de9135c6a984211b08072e51384bd92b73a29eae0599a2d894023341f8832` |
| `mutations/mutations_cl_v2.py` | contre-lecteur, lot 2 (idem) | `389e8e030da79fbc94b3352ddadbc58c7a66414dd100d8f14dfcadb4f20f03b2` |
| `banc/banc-v2d.txt` | journal du banc | `8d5ad79b449b8b6d75971b80b0cd7898cdac9a568354d9e9daa2f8c1f8af0a38` |
| `banc/banc-v2d-mutations_temoin_v2.jsonl` | témoins | `dd8ca8a7048e9e70e748fcc06a443c0720c50bbb87b20415c62f3ed4886182a6` |
| `banc/banc-v2d-mutations_accb6_code_v2.jsonl` | lot neuf | `4d6104e0163f73de3782ef56ced8ad08cdd96d81688bed88ab5dca2934812016` |
| `banc/banc-v2d-mutations_cl_v1.jsonl` | contre-lecteur, lot 1 | `ecc0fcd70cb5d183e8ab620f1f952b9759c9eab880a4224e53b79a67864b5e14` |
| `banc/banc-v2d-mutations_cl_v2.jsonl` | contre-lecteur, lot 2 | `4271fc15c586d7a5dc6381f9eda78e652bf4f249d7fc2f653433152be58df92c` |
| `banc/banc-v2d-mutations_accb6_v4.jsonl` | développeur, v4 | `9adf0bc83b704168e3a1710da9846f4775e8fa4852b562173fde897a3324cb1b` |
| `banc/resume-banc-v2d.md` | table des 130 courses | `054432b67c3d655ea93271dc9467954cc5d134697a55013ca3ec56bb9480d25c` |
| `banc/resumer_banc.py` | script de la table | `19269868599f86a238d8e2859f97c7e083b0efd232badc830b5bc177f7ecb81b` |

Restent dans le bac à sable (non versés, non durables) : le fichier de `CODE-ACCB6` de l'essai à blanc (`…/scratchpad/accb6-v2/controle-code/code-accb6-essai-282e295e.json`, `1957d087d92f31d0219531c06dc5d3ad8058ff5fe20ccfc6b183b1fb5fadc090`, à ne pas inscrire : la mère l'écrit elle-même), l'arbre composé de l'essai et les sorties de l'énumération rejouée (égales à la sortie versée `6b078d6c…`).
