# T0.7, module v2 — contre-lecture courte du code, option (c) des phrases des concepts (différentiel `8ae9fc44..37485ce5`) — v1

- **Contre-lecteur** : sous-agent **neuf** (Claude Fable 5.2, `claude-fable-5-2`), autre modèle que le développeur (Opus 5.5 ;
  N-052) ; n'a écrit ni T0.7, ni le module, ni ses contre-lectures. Il a lu T0.7 : exclu ensuite de tout rôle de lecteur de P3-bis.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-contre-lecture-courte-module-t07-option-c-v1.md`,
  `66fc7f348981d3427de77c22b4916ef8d8e0d5ba8af6a79179e0a5331b5b8148`, égale à son compagnon (vérifié à 12:40 UTC).
- **Heures** : travail du 2026-11-10, de 12:40:07 à 13:23:48 UTC ; toutes les heures de ce fichier sont relevées par `date -u`.
- **Arbre** : `/home/user/wt-t07-module-v2`, branche `prep/t07-module-v2`, tête `41648f2ebbe050bc0779349c75f93af8b22a3802` ;
  `src/`, `tests/` et `scripts/` de la tête égaux à ceux de `37485ce5` (`git diff --quiet 37485ce5 HEAD -- src tests scripts`).
  Aucun commit, aucun `checkout`, aucune poussée, aucun `fetch` dans le dépôt du programme ; arbre propre à la fin
  (`git status --short` vide avant l'écriture de ce fichier).

## Verdict

**`CODE-T07` inscriptible au commit `37485ce50601b7d7ff9035bc34c734ec689ca731`.**

Aucun constat bloquant pour l'inscription. Un point **bloquant pour l'ordre d'exécution** (pas pour la ligne `CODE-T07`) :
le commit `8cb539f9` doit être atteignable depuis `main` avant le lancement de l'instance (CLC-03). Deux constats à corriger
sans toucher au module (CLC-04 : essai manquant ; CLC-05 : lecture de R15 à porter au texte), trois mineurs (CLC-06 à CLC-08).

## Pièces lues, empreintes recalculées

| pièce | sha256 recalculé | égal à l'attendu |
|---|---|---|
| rapport du développeur `rapport-complementaire-5-option-c-v1.md` | `e58be6c9051d928e3818175ace1dbfd2db6afd2c6e725d7278032dbe13a90e90` | oui |
| banc `banc-mutations-t07-option-c-v1.json` | `0b54c163556cd683a420c8d981a18dc9b8ed134c715e945e5237c95d535aca33` | oui |
| répétition, `resume-passage4.json` | `6c6f2c8ded07017373d8cb9d50a47f0d5e45a61ba5f0ef24c8a334fa4ebf84f6` | oui |
| répétition, `journal-passage4.txt` | `7ca315daacdb0108d5d735d5bdb3619c3849e066ce6b16dff9d0eaaeef1244d2` | oui |
| script `scripts/etape_a_t07_variante_b_v2.sh` | `e68d3306bd76a549ec97eb6b153d03ec544c92944ae74293d8c0db8cfda62269` | oui |
| brouillon 21 (lu dans `/home/user/controle-ia-travail/brouillons/`, absent de cet arbre) | `f7dcb226efe8671b977ce906c286f7e7243f78a2c9fcf205cbfe5715866ea0cc` | oui |
| contre-lecture courte précédente (lue dans `/home/user/controle-ia-travail/docs/notes/g0-deux-semaines-v1/t07-module-v2/`, absente de cet arbre) | `d0fe90538160779ea6386a9f3a622ca0636575631254a76a5bec857915e4e8c6` | oui |

Tous les compagnons `.sha256` du dossier `t07-module-v2/` et de `repetition-jouet-variante-b-v3/` répondent (`sha256sum -c`).
R-2153, R-2155, R-2166, R-2183 et R-2220 lues dans `/home/user/controle-ia-travail/registres/decisions.md` (l. 2111, 2113, 2124,
2141, 2178). Brouillon 21 : l. 177-187 (lignes 5, 11, 17 de l'en-tête), 1277-1281, 1400-1406 (plan, point 10), 1447-1450, 1476-1478,
1792-1795 (R15), 2079-2081, 2534-2538 (« Accord au code », points 18 à 20).

Différentiel lu en entier : `git diff 8ae9fc44 37485ce5 -- src tests scripts` (module : 61 lignes ajoutées, 10 retirées, trois
fichiers ; `tests/` et `scripts/` : cinq fichiers, 1 170 lignes ajoutées). Les **18 empreintes** des fichiers de
`src/controle_ia/t07/` au commit `37485ce5`, recalculées par `git show 37485ce5:<fichier> | sha256sum`, sont égales à la table
du rapport (§ 9) : 18 fichiers, 0 écart. `src/` de `37485ce5` égal à `ae49f55d` ; `src/` et `tests/` égaux à `16f59d63`.

## 1. Exigences de R-2166 (brouillon 21, « Accord au code », point 20) : code, cas sain, artefact

Lignes au commit `37485ce5`, relues une à une.

| exigence | code (vérifié) | cas sain | artefact (R5) | jugement |
|---|---|---|---|---|
| (i) clé passée des exigées aux permises | `registre_v1.py` l. 69-71 | `test_cle_des_concepts_permise_et_non_exigee`, `test_repli_sans_ligne_des_concepts_garde_passee` | `test_repli_ligne_exigee_manquante_rien_calcule_puis_relance` ; ancien artefact en `xfail` strict (il échouerait s'il passait) ; m3 tuée | tenue |
| (ii) jeux lus sans condition sur la ligne des concepts | `lecture_v2.py` l. 500 (`ouvrir`), l. 295-300 | `test_ligne_absente_…` (30 couples appris sans la ligne) | m7 tuée | tenue |
| (ii) phrases lues seulement si la ligne précède **strictement** la fermeture | `lecture_v2.py` l. 301-310 (`lc["instant"] < int(fermeture)`, même comparaison que les jeux l. 298) ; fermeture rendue par `garde_adaptee_v1.instant_fermeture` (première `OUVERTURE-T07` du run, sinon l'ouverture en cours, sinon plus tôt sous G5) | `test_ligne_avant_…`, `test_ligne_juste_avant_la_fermeture_lue` (une seconde avant), `test_variante_B_ligne_avant_la_garde_du_repli_lue` | `test_ligne_posterieure_…`, `test_variante_B_ligne_inscrite_apres_la_garde_du_repli_exclue`, ligne à l'instant même (cas `y`) ; m1, m2 tuées | tenue |
| (ii) quatre concepts au moins en réel | `lecture_v2.py` l. 303 (`min_concepts`) et l. 501 (`4 if config["mode"] == "reel" else 1`) | lecture à trois concepts acceptée avec un minimum de trois | `test_trois_concepts_en_mode_reel_refus_quatre_exiges` ; m6 tuée | tenue au code ; **essai incomplet : CLC-04** |
| (ii) aucune phrase → aucune direction, aucune tâche de plancher de concept | `sondes_neuves_v1.py` l. 466 ; `lecture_v2.py` l. 850-851 ; garde neuve l. 902-904 | `test_ligne_absente_…`, `test_manifeste_sans_ligne_etat_non_lues` | `test_artefact_directions_apprises_sans_phrases_arret` ; m9, m12 tuées | tenue |
| état des phrases et plancher de concept au manifeste | `lecture_v2.py` l. 850-851, 860-862 | `test_manifeste_porte_l_etat_des_phrases_lues_et_non_lues` | m11 tuée | tenue (lecture : § 4) |
| (iii) T7-P9 « non lue : jeu des phrases des concepts non scellé à l'ouverture » | `lectures_t07_v1.py` l. 66-69, 245-253 ; état porté par l'index (`lecture_v2.py` l. 679, 925, 943) | `test_ligne_avant_…` (T7-P9 lue) | `test_ligne_absente_…`, `test_ligne_posterieure_…`, `test_artefact_index_incoherent_T7P9_arret_a_l_etape_B` ; m5, m8, m10 tuées | tenue |
| (iii) réserve R15 | `lectures_t07_v1.py` l. 64, 492-494 ; phrase égale mot pour mot au brouillon 21, l. 1794 | absente quand les phrases sont lues | présente une fois, motif « absente » ou « exclue pour de bon » ; m4 tuée | tenue quand les scores sont ouverts ; **CLC-05** |
| (iv) étape A menée au bout sans la ligne | ensemble | `test_ligne_absente_…` ; répétition, passage « sans concepts » | — | tenue |
| (v) contre-lecture courte et répétition au commit neuf | — | ce fichier ; répétition rejouée (§ 2) | — | tenue |

## 2. Les deux gardes neuves, le défaut corrigé du script, ce que j'ai rejoué

Tout est joué depuis l'arbre, `PYTHONPATH=src`, interpréteur `/home/user/controle-ia-travail/.venv/bin/python`,
`-p no:cacheprovider`, `--basetemp` et `TMPDIR` dans mon bac à sable.

| ce qui est joué | heures (UTC) | résultat |
|---|---|---|
| tous les `tests/test_t07*.py` (17 fichiers) et `tests/test_verifier_jeux_synthetiques_t07_v2.py`, un processus | 12:41:24 à 12:52:19 | **404 passés, 2 sautés, 4 échecs attendus (`xfail`), 0 échec**, code 0 (653,5 s) |
| l'essai du miroir, seul | ≈ 12:53 | **1 passé** (§ 3) |
| banc `scripts/banc_mutations_t07_option_c_v1.py` | 12:53:30 à ≈ 13:10 | **12 mutations, 12 tuées**, code 0 ; mêmes essais tueurs que le banc scellé du développeur ; fichiers rétablis octet pour octet |
| mutation de plus, du contre-lecteur (m13, § CLC-04) | ≈ 13:10 à 13:14 | **survit** : 48 passés, 2 `xfail`, code 0 ; `lecture_v2.py` rétabli, empreinte égale |
| répétition `scripts/repetition_jouet_variante_b_t07_v2.py`, complète | 13:14:37 à 13:22:25 | **12 verdicts conformes**, code 0 ; script joué `e68d3306…` ; dossier de 193 Mo, supprimé |
| répétition, artefact du contre-lecteur : script sans `registres/go.md` (`--script`, `--normal-seulement`) | 13:22:25 à 13:23:23 | **refus** : « REFUS : registres/go.md absent », repli en code 2, script en fin 3 |

- Sautés (2) : `test_t07_lecture_v1.py` l. 504 (branche `origin/prep/t06-candidat8-v1` non récupérée) ; `test_t07_lecture_v2.py`
  l. 911 (commit `061ac380` absent du clone). Les deux sont déclarés par l'essai.
- Échecs attendus (4) : CT-01, CT-11, cas sain du journal, ancien artefact du repli (`SCELLEMENT-CONCEPTS-T07` devenue permise).
- Écart au compte du développeur (403 passés, 1 échec) : l'essai du miroir passe maintenant (le commit est dans le clone).

**Garde neuve de l'étape A** (`lecture_v2.py` l. 902-904) : sans phrases lues, des directions rendues par l'apprentissage
arrêtent l'étape après le manifeste, avant toute notation. Cas sain : `test_ligne_absente_…` ; artefact :
`test_artefact_directions_apprises_sans_phrases_arret` (aucun fichier de scores écrit) ; m9 tuée. Conforme.

**Garde neuve de l'étape B** (`lectures_t07_v1.py` l. 245-248) : des directions dans l'index avec un état « non lues » arrêtent
l'étape B (`arret-etape-b.json`). Cas sain : `test_ligne_avant_…` ; artefact : `test_artefact_index_incoherent_T7P9_arret_a_l_etape_B` ;
m10 tuée. Conforme.

**Défaut corrigé du script v2** (`scripts/etape_a_t07_variante_b_v2.sh` l. 100-102) : `registres/go.md` est nommé dans
`REGISTRES`, recopié de `main` par la boucle des l. 149-150 ; `registres/index-bras-attaque*` reste hors de l'extraction (motifs
`/*` et `!/*/`, registres nommés seulement) et refusé par `interdit()` (l. 141). Le développeur déclarait le défaut « non
démontré ». **Je l'ai démontré** : le même script, `registres/go.md` retiré de `REGISTRES` (une ligne changée, copie dans mon bac
à sable, jamais dans l'arbre), est refusé par la garde du repli (« REFUS : registres/go.md absent ») ; le script du dépôt passe
(« registre registres/go.md recopié de main », garde passée, étape A en code 0). Cas sain et artefact tenus.

Pièces de mes rejeux, non versées (la consigne ne nomme qu'un chemin de sortie) et supprimées avec le bac à sable ; empreintes
relevées avant suppression : résumé de la répétition `29b12b24933182b5b1c963c881e9a47ad67367e9c53a078b6464df0229d10b14` ;
résumé de l'artefact `60bd30427e217336ca6dc6e1a2eda3ca9cdb6cd3dd56102881874f01b67202be` ; banc rejoué
`833e2a9cde374cbc33989fd049214b5086ac6cea2ada1bdf61272d326bac8406` ; script fautif
`124ad289a2eeaa3f5aca3f303bcac4f5d9cca61efb253a66ccfdd874dea9c434`.

## 3. Miroir de `familles_v2` (commit `8cb539f9`)

- **L'essai passe** dans ce clone : `tests/test_t07_lecture_v1.py::test_mahalanobis_miroir_egal_a_familles_v2_au_commit_8cb539f9`,
  1 passé seul, et passé dans la passe complète. `git show 8cb539f9:src/controle_ia/sondes/familles_v2.py` a l'empreinte
  `4fea2c52b754fc180974c80ed9e83a3656d1b6aef7382a4451b7532a144153ad`, celle que l'essai attend.
- **État du commit**, vérifié : `8cb539f9b7ecd20fab133bfffb590ca8e1fdfc63` est la tête de `origin/prep/t06-ordre-course-v2` ;
  il **n'est pas** ancêtre de `main` (`git merge-base --is-ancestor` : code 1), ni de la tête de cet arbre ; il est à **un seul
  commit** de sa base commune avec `main` (`7822a65b6`). Ce commit ajoute sept fichiers (un rendu, un brouillon de T0.6 et son
  script, un devis, un ordre de course et ses deux pièces), **aucun sous `src/` ni `tests/`**. Le fichier `familles_v2.py` est
  **le même objet** (`c74fa2e2…`) à `8cb539f9`, à `main`, à `origin/main`, à `8ae9fc44` et à la tête.
- **Conséquence pour l'instance, confirmée à la lecture du script** : le clone est `--single-branch --branch main` (l. 97) ;
  l'essai, « jamais sauté », échouerait ; le script exige `code 0` **et** la ligne attendue (l. 214) : arrêt en code 2 à l'étape 6.

**Avis sur la voie : rendre `8cb539f9` atteignable depuis `main`, par une fusion qui ne change pas l'arbre, puis mesurer.**

1. La mesure seule ne suffit pas. En mode `ARRET_APRES_ESSAIS`, la ligne mesurée porterait « 1 failed » ; hors mesure, le script
   refuse tout code autre que 0, quelle que soit la valeur d'`ATTENDU`. Il faudrait un script v3, donc une contre-lecture et une
   répétition de plus.
2. Changer l'essai (le sauter) contredit le texte (brouillon 12, marqueur 8 ; brouillon 14, en-tête) et change `tests/`.
3. La fusion (`git merge -s ours 8cb539f9` sur `main`, par la mère) ne change ni `src/`, ni `tests/`, ni aucun fichier : les 18
   empreintes de `CODE-T07` et le contrôle `git diff --quiet C7 S7 -- src tests` du script restent tenus. L'essai ne demande que
   la présence de l'objet du commit dans le clone ; l'objet du fichier est celui de `main`, déjà extrait (`/src/` est dans
   l'extraction partielle).
4. **Deux précautions.** (a) Après une fusion « ours », git tient la branche pour fusionnée alors que ses sept fichiers ne sont
   pas dans `main` : s'ils doivent y entrer un jour, ce sera par copie explicite. Une fusion ordinaire (qui les ajoute, hors de
   `src/` et `tests/`) convient aussi, si la mère préfère. (b) **Non vérifié** : le comportement dans un clone partiel
   (`--filter=blob:none`) à branche unique. Après la fusion, mesurer la ligne dans un clone fait comme celui de l'instance
   (mode `ARRET_APRES_ESSAIS`), ce que O-1 exige de toute façon pour fixer `ATTENDU` ; l'essai du commit `061ac380` s'y sautera
   (déclaré), la ligne mesurée le dira.

## 4. Points ouverts 2 à 4 du rapport

- **Point 2, R15 écrite seulement si les scores sont ouverts** : confirmé à la lecture (`lecture_v2.py` l. 1055-1083 :
  `lt.lectures` et `lt.reserves` ne sont appelées que sous `ouvre`). Scores fermés, `lecture-t07.json` écrit « T7-P3 à T7-P19 :
  non lues : scores non ouverts » et ne porte ni R15 ni l'état des phrases ; R14, elle, est écrite dans les deux cas (l. 1125).
  L'état des phrases reste au manifeste de l'étape A et dans `sondes-t07.json`. Rien n'est silencieux (T7-P9 est dite non lue,
  avec son motif), et R15 « accompagne toute phrase de validité », qui n'existe pas scores fermés. Mais le texte (l. 1794) dit
  « réserve écrite dans le résultat » sans cette condition : **CLC-05**, à porter au texte.
- **Point 3, « plancher de concept gardé au manifeste »** : la lecture du développeur est celle du texte qui fait foi. Le point
  20 (ii) du brouillon 21 dit « aucune phrase → aucune direction ni tâche de plancher de concept au manifeste » : les tâches
  `plancher-concept/<concept>/c<couche>` restent quand les phrases sont lues, disparaissent sinon ; l'état des phrases, écrit
  dans la configuration du manifeste avant toute graine, est un ajout cohérent. La formule de R-2166 est un résumé de la mère ;
  je la lis de même. Rien à corriger.
- **Point 4, étape A non complète** (jouet de la v2 initiale) : confirmé, hors du réel, inchangé ; T7-P9 y est « non lue : aucune
  direction de concept notée », sans R15. Rien à corriger.
- **Docstring périmée** (point 6 du rapport) : confirmée, `lecture_v1.py` l. 27 (« exigées `RUN-CONFIRMATION-T06`,
  `SCELLEMENT-CONCEPTS-T07` »). Sans effet sur le code. La corriger maintenant changerait une des 18 empreintes : à laisser pour
  la prochaine version du fichier (**CLC-06**).

## Constats

| n° | gravité | constat | ce qu'il faut |
|---|---|---|---|
| CLC-01 | conforme | Les exigences (i) à (v) du point 20 sont tenues au code ; chacune a un cas sain et un artefact, sauf la réserve de CLC-04. | rien |
| CLC-02 | conforme | Les deux gardes neuves ont chacune un cas sain et un artefact ; le défaut de `registres/go.md` est corrigé, et démontré par mon artefact. | rien |
| CLC-03 | **bloquant pour l'ordre d'exécution** (non pour `CODE-T07`) | `8cb539f9` n'est pas atteignable depuis `main` : sur l'instance, l'étape des essais s'arrêterait en code 2. | fusion sans changement d'arbre sur `main`, puis mesure de la ligne dans un clone fait comme celui de l'instance (§ 3) |
| CLC-04 | à corriger, **sans toucher au module** | Le lien « quatre concepts en mode réel » de `ouvrir` (l. 501) n'est couvert par aucun essai : ma mutation m13 (`4 if config["mode"] == "reel" else 1` remplacé par `1`) **survit** aux trois fichiers joués (`test_t07_option_c_concepts_v1.py`, `test_t07_corrections_cl1_v1.py`, `test_t07_sondes_neuves_v1.py`) ; à la lecture, aucun essai de `tests/test_t07*.py` ne passe par `ouvrir` en mode réel avec des phrases (non rejoué sur les 17 fichiers). La ligne est correcte et antérieure au différentiel. L'essai (iv) « trois concepts en mode réel → refus » donne le minimum à la main. | un essai par `ouvrir`, configuration en mode réel, trois concepts → refus ; il change `tests/`, donc à ajouter **avant** de fixer C7, ou à déclarer |
| CLC-05 | à porter au texte | R15 n'est écrite que scores ouverts (§ 4, point 2), alors que la table des réserves la dit « écrite dans le résultat ». | une phrase au texte (table des réserves, « Accord au code », point 20 (iii)) : « écrite quand les scores sont ouverts ; sinon l'état des phrases est au manifeste de l'étape A et dans `sondes-t07.json` » ; décision de la mère |
| CLC-06 | mineur | Docstring périmée, `lecture_v1.py` l. 27. | prochaine version du fichier |
| CLC-07 | mineur | Étape B : un index sans la clé `phrases_concepts` et sans direction donne « non lue : aucune direction de concept notée », sans R15 ni arrêt. Hors d'atteinte quand les étapes A et B tournent au même commit (`CODE-T07` contrôlée aux deux) ; m5 n'est tuée que par une assertion d'essai, pas par une garde. | à déclarer ; garde possible à la prochaine version |
| CLC-08 | mineur | Script v2, l. 362 : un repli en code 2 est journalisé « ligne manquante : attente », même quand le motif est un fichier absent (vu à mon artefact) ; le vrai motif est dans `repli-1.err`, poussé avec les traces. | libellé, à la prochaine version du script |

## Écarts déclarés

- La répétition (permise par la consigne, dans cet arbre) lit le commit `1609a4bf` par `git ls-tree` et `git show` restreints à
  `src/`, aux invites, aux deux fichiers de P3, à `registres/go.md` et à une configuration jouet ; elle fait des `checkout` et des
  `push` dans **ses dépôts jouets** du bac à sable, jamais dans le dépôt du programme. Sa course jouet écrit un
  `lecture-sondes-t06.json` factice, copié avec le dossier du run jouet, jamais ouvert ni affiché.
- Le banc et ma mutation m13 ont modifié puis rétabli `src/controle_ia/t07/lecture_v2.py`, `lectures_t07_v1.py` et
  `registre_v1.py` ; empreintes finales égales à celles du commit, `git status --short` vide.
- Brouillon 21, décisions et contre-lecture précédente lus dans `/home/user/controle-ia-travail/` (fichiers nommés), absents de
  cet arbre.
- Aucun fichier interdit ouvert ; aucune recherche récursive ; aucun appel de modèle ; aucune valeur d'une sonde de 7a sous mes
  yeux.
