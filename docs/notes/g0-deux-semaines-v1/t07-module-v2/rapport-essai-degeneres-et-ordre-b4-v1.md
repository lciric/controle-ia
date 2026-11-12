# T0.7 — essai de la garde « tirages dégénérés » (GARDES-CODE-01) et ordre d'exécution de l'étape A, brouillon 4 : rapport — v1

- **Auteur** : sous-agent développeur **neuf** (Claude Opus 5.5, `claude-opus-5-5`) de la session mère
  `session_01VJdZpSMxSdk2SJ1ScmdfNv` ; n'a écrit ni T0.7, ni son module, ni ses ordres d'exécution, ni le script v2, ni leurs
  contre-lectures ; a lu T0.7 : exclu ensuite de tout rôle de lecteur de P3-bis.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-essai-degeneres-ordre-b4-t07-v1.md`,
  `a3e326e46bf00e6392a52e42204ab20e52dd3a3ecddec8e8b10bf26c79be1696` (vérifiée par `sha256sum` à 14:57 UTC, égale à son
  compagnon). Interdits communs v2 recopiés dans la consigne, lus et appliqués.
- **Heures** (seules celles-ci ont été relevées par `date -u`, le 2026-11-10) : début 14:57:45 UTC ; essais T0.7 de 15:05:55 à 15:13:49 ; poussée vérifiée à 15:14:28 ; mesure de `ATT` de 15:17:26 à 15:29:36 ; ordre brouillon 4 scellé à 15:32:34 ; rapport scellé à 15:34:12 UTC. L'essai, ses premiers passages et les mutations ont eu lieu entre 14:57:45 et 15:05:55 (heures intermédiaires non relevées).

## Verdict

**Partie 1 faite** : essai GARDES-CODE-01 versé sur `prep/t07-essai-degeneres-v1` (commit
`2c8ab779ca6df361d562e120ba34045be675853a`, poussé), cas sains et artefacts tenus, **quatre mutations sur quatre tuées**, aucun
changement sous `src/` (`git diff --quiet 37485ce5 HEAD -- src` : code 0). **Partie 2 faite** : ordre brouillon 4 écrit et
scellé, `ATT` **mesurée** dans un clone fait comme celui de l'instance : `346 passed, 2 skipped, 4 xfailed`. Script v2 non modifié ; sept
constats pour une v3 éventuelle (§ 13 de l'ordre), dont S-3 (un chemin de 7a cité par un registre n'est pas refusé par `interdit()` ; compensé par un contrôle de la fille) et S-1 (la ligne d'essais est comparée entière, avertissements compris).

## Partie 1 — essai GARDES-CODE-01

**Pièces lues** (empreintes recalculées) : contre-lecture orchestrée du brouillon 22
(`prereg/contre-lectures/T0.7-sondes-v0-v1-brouillon22-cl-orchestree-v1.md`, `47537dfa7d4f97d0266f72eb3d791996d2ea0aa8f35a098a721c1d72ab251a60`),
ligne GARDES-CODE-01 et CLO-03 ; brouillon 22 (`brouillons/T0.7-sondes-v0-v1-brouillon22.md`,
`8b84cba5bd527e10a3b835ebc0caa7e7da0e31af503904e51621d752d65f0a37`), l. 1864 et l. 2427-2438 ; `src/controle_ia/t07/lecture_v1.py`
(`62b34790…`, l. 840-877 : `lecture_jeux`, reprise l. 873-874), `lecture_v2.py` (`etape_b`, l. 1015-1133, appel l. 1063-1064),
`lectures_t07_v1.py` (reprises de `lire_avec_plancher`, `difference`, `placebo`, base « coût seul »), `plancher_v1.py`
(`comparer_scores_au_plancher`), `criteres_v1.py` (`etat_pour_sonde`, `issue_critere_3`, phrase L4b) ; paquet gelé
`src/controle_ia/sondes/evaluation.py` (`intervalle_blocs`, l. 40-63 : arrêt au-delà de 1 % de tirages sans les deux classes).

**Fichier neuf** : `tests/test_t07_tirages_degeneres_v1.py`, sha256 `c68fd68fc9e747aa34ed0853e1da6c8e0124ec0c3197287c40faa2ae746c5140`,
dans l'arbre `/home/user/wt-t07-degeneres`, branche `prep/t07-essai-degeneres-v1` (partie de `06deda58`), commit
`2c8ab779ca6df361d562e120ba34045be675853a`, poussé (`git ls-remote` : même tête). Garde des secrets : 0 avant le commit. Aucun autre
fichier ajouté ni changé.

**Ce que l'essai éprouve** (5 essais) :

| essai | niveau | cas | issue |
|---|---|---|---|
| `test_reprise_cas_sain_aucun_tirage_degenere[intervalle-0.9875]` et `[descriptif-0.95]` | `lecture_v1.lecture_jeux`, deux sondes, dix tâches, `(i-a)`, `S75`, `S100` | **cas sain** : positifs répartis sur les dix tâches | aucune lecture en échec, 0 tirage dégénéré, chaque lecture complète |
| `test_reprise_artefact_une_seule_tache_porte_les_positifs[intervalle-0.9875]` et `[descriptif-0.95]` | idem | **artefact** : positifs de `S75` sur la seule tâche `t000` | `S75` en « échec » pour chaque sonde ; motif **égal au message de l'arrêt gelé** (`intervalle_blocs` rejoué sous la même graine), plus de 2 tirages dégénérés sur 200 ; prédicteurs triviaux rapportés ; `(i-a)` et `S100` **égales au cas sain** ; état de la dose « E » |
| `test_bout_en_bout_cas_sain_et_artefact_lecture_v2` | chemin de l'instance : `lecture_v2.etape_a` puis `etape_b` sur le faux run de 7b (`tests/test_t07_lecture_v1.py`), doses jugées `S75` et `S100` | cas sain, puis artefact (colonne `tache` des lignes `S75` des mesures de T0.6 = `t000`, mesures rescellées, `episodes-t06.json` réécrit à leur empreinte) | sain : L2, aucune lecture en échec ; artefact : `S75` en échec pour les quatre sondes, motifs gelés écrits dans `lecture-t07.json` et dans la phrase de **L4b** (« aucune sonde lisible pour (ii) à la dose nommée (S75) ») ; `(i-a)`, `S100`, `S25`, `S50` lus, égaux au cas sain ; T7-P1 à T7-P19 présentes ; reprises de `lectures_t07_v1` sur `S75` (T7-P16, T7-P19, base « coût seul ») en échec au motif gelé ; aucun `arret-etape-b.json` |

**Mutations** (copies de `src/` dans le bac à sable, jouées avec `-o pythonpath="<copie>/src <arbre>/tests"`, `--rootdir` et `-c`
de l'arbre ; import réel tracé par un essai du bac à sable qui imprime et vérifie `controle_ia.__file__`,
`controle_ia.t07.lecture_v1.__file__`, `controle_ia.sondes.evaluation.__file__` sous la copie, et la présence de la marque de la
mutation dans le source chargé) :

| mutation | changement | essais en échec | motif de l'échec |
|---|---|---|---|
| m1, reprise retirée | `lecture_v1.py` l. 873 : `except GardeArret` → `except ZeroDivisionError` | 3 (les deux artefacts, le bout en bout) | `GardeArret` « … tirages sur 200 sans les deux classes … » non reprise ; `ArretApresManifeste` à l'étape B |
| m2, motif perdu | l. 874 : `"echec": str(err)` → `"echec": "échec"` | 3 | « motif autre que celui de l'arrêt gelé : 'échec' » |
| m3, arrêt étendu | l. 874 : l'échec d'une lecture rend toutes les lectures de toutes les sondes en échec | 3 | `(i-a)` en échec, résumé différent du cas sain |
| m4, seuil du paquet gelé affaibli | `sondes/evaluation.py` l. 59 : `0.01` → `0.5` | 3 | `S75` lue « au-dessus » au lieu de « échec » |

Sous chaque mutation, l'essai de trace passe (import de la copie) et les deux cas sains passent : **4 mutations, 4 tuées**.

**Essais joués** (arbre réduit `/home/user/wt-t07-degeneres`, `PYTHONDONTWRITEBYTECODE=1`, `-p no:cacheprovider`, `--basetemp`
au bac à sable) : le fichier neuf seul, 5 passés (8,4 s) ; `tests/test_t07*.py` (17 fichiers) et
`tests/test_verifier_jeux_synthetiques_t07_v2.py`, un processus, 15:05:55 à 15:13:49 UTC : **393 passés, 22 sautés, 3 échecs
attendus, 0 échec**, code 0 (473 s) ; les sauts tiennent à l'extraction réduite de cet arbre (ni `donnees/`, ni `docs/`, ni
`prereg/` : conditions de saut lues, non nommées une à une). Compte de l'instance : partie 2 (`ATT`). `git diff --quiet
37485ce50601b7d7ff9035bc34c734ec689ca731 HEAD -- src` : **code 0**.

## Partie 2 — ordre d'exécution de l'étape A, brouillon 4

**Pièces lues** (empreintes recalculées, égales aux annonces de la consigne) : ordre brouillon 3 (`b053a220…`) ; contre-lecture
courte v3 (`d0fe9053…`) ; rapport complémentaire 5 (`e58be6c9…`) ; contre-lecture courte option (c) (`7a327462…`) ;
`scripts/etape_a_t07_variante_b_v2.sh` (`e68d3306…`, lu en entier) ; R-2153, R-2220, R-2229, R-2231, R-2241, R-2246, R-2249 ;
`registres/go.md` (GO-2026-11-10-04, GO-2026-11-10-06).

**Écrit** : `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon4.md`, sha256 `d5047be2a1cc371917bc09352f66cd59f6a7d8b5d4f2c43e32d3c98a36f6d72c`, scellé (compagnon) ;
brouillons 1 à 3 intacts (empreintes recalculées après écriture, égales à leurs compagnons).

Ce qu'il porte : 
- **O-1 à O-6** (§ 0 bis, table : réglé par le script v2 / porté par l'ordre / reste) : O-1 essais avant le modèle, `ATT` mesurée
  (§ 11 bis), validité contrôlée par la fille (P12 : arbres `tests/` `79230a58…` et `src/` `744a9e16…` de S7, six chemins cités
  par la configuration) ; O-2 borne de taille et découpage (§ 5 bis, calcul écrit ; § 4.6 vérification des morceaux **sans en
  descendre aucun** : présence et compagnons contre le manifeste, `git ls-tree -l` écarté car il descendrait les morceaux ;
  commande éprouvée sur un dépôt jouet, cas sain `OK` et artefacts `ÉCART` ; § 9 recomposition avant l'étape B) ; O-3 texte
  corrigé (après « stopped », seule la fille détruit ; rappel daté à `ECH`, fille et mère) ; **O-4 : `ANT0` = dépense inscrite
  sous GO-2026-11-10-04 et GO-2026-11-10-06** (ligne (A), P8, § 4.5, § 6), plus deux gardes neuves : `ANT0` ≤ 4,5 USD (pire cas
  du devis 15,5 USD) et minuterie bornée par `HMAX` = min(12 h, (20 − ANT0 − 1,30) / prix horaire), création refusée sous
  39 240 s ; O-5 clone de la fille à registres nommés (le motif `/registres/*.md` du brouillon 3 extrayait
  `registres/index-bras-attaque-v1.md`) ; O-6 écart d'encodage du script → le bloc s'arrête, aucune création.
- **Option (c)** : P3 (périmètre exact, règle de fermeture par la garde du repli, passage « sans concepts » : phrases non lues,
  T7-P9 « non lue », R15 à l'étape B), marqueur `PERIMETRE_T07` (`JD,JA` à l'écriture), contrôle du § 4.1, neuvième argument du
  script ; **règle de C7** (R-2231) : P6 (`CODE-T07` cite `registres/code-t07/CODE-T07-v2.json`, champ `commit` = C7), P9
  (`src/` de C7 égal à `37485ce5`, `git diff --quiet C7 S7 -- src tests`, essais CLC-04 et GARDES-CODE-01 présents à S7).
- **Filtre d'inventaire** borné aux étiquettes `t06…` et `t07…` (§ 4.2, P10 ; CLO-08, R-2249) ; lecture stricte pour la
  variante B : l'instance de 7b (`t06-v2`) doit être détruite avant la création (P1), « autre que celle de 7b » ne valant que
  pour l'étape annexe abandonnée (à juger, § 10.3).
- **T0.7 cité par sa ligne `SCELLEMENT-T07`** (en-tête, P5), jamais par une empreinte (vérifié : aucune empreinte du texte ni
  d'un de ses brouillons dans l'ordre).
- **Script v2 non modifié** ; sept constats pour une v3 (§ 13) : S-1 comparaison de la ligne entière (avertissements compris) ;
  S-2 interpréteur de la mesure 3.13 contre 3.11 ; S-3 `interdit()` ne refuse pas un chemin de 7a cité par un registre
  (compensé : compte exigé à 0 au § 4.1) ; S-4 libellé CLC-08 ; S-5 étiquettes des autres tâches (concordance) ; S-6 borne de
  taille calculée après les paquets ; S-7 cosmétique. Aucun ne bloque l'ordre : chacun est compensé ou déclaré.

**`ATT`** : **`346 passed, 2 skipped, 4 xfailed`**, mesurée le 2026-11-10 de 15:17:26 à 15:29:36 UTC dans un clone
`--filter=blob:none --no-checkout --single-branch` de ma branche (tête `2c8ab779`, même atteignabilité que `main` à `06deda58`
plus l'essai), extraction partielle, registres nommés et fichiers cités recopiés comme aux étapes 2 et 3 du script v2, essais
`tests/test_t07_*.py` (17 fichiers) lancés par la commande exacte de l'étape 6 ; code 0, 716 s, aucun avertissement,
`essais.err` vide. Sautés : `test_t07_lecture_v1.py:504` (branche `origin/prep/t06-candidat8-v1`), `test_t07_lecture_v2.py:911`
(commit `061ac380`) ; échecs attendus : CT-01, CT-11, cas sain du journal (v2), ancien artefact du repli. **L'essai du miroir de
`familles_v2` passe** (`8cb539f9` atteignable : CLC-03 levé). Recoupement : 344 + 3 + 5 = 352 = 346 + 2 + 4. Écarts déclarés
(§ 11 bis de l'ordre) : étapes 4 et 5 non jouées (pas de course 7b), Python 3.13.16 local contre 3.11 sur l'instance, mesure
sur la branche et non sur `main`. Le marqueur `<<ATTENDU_ESSAIS_T07>>` n'est pas employé ; `ATT` vaut sous P12, sinon la
commande de remesure du § 11 bis s'applique. Script de mesure (bac à sable, non versé) : `98beca19…` ; sorties : `essais.txt`
`2b506a18…`, liste des essais `bd49a367…`, journal `d15f94b8…`.

## Points ouverts pour la mère

1. **Fusion de `prep/t07-essai-degeneres-v1` dans `main` avant C7** (R-2249, option (a) de GARDES-CODE-01 ; CLO-03 sans objet).
   `ATT` ne vaut que si l'arbre `tests/` de S7 est `79230a584e8675f1771fd4f0a9315de71c2bcbdc` (celui de `2c8ab779`) et l'arbre
   `src/` `744a9e16f1635ff402e798b4ac868a57311e44b8` (celui de `37485ce5`) : si `tests/` de `main` a bougé depuis `06deda58`, ou
   si un autre essai entre avant C7, remesure (commande du § 11 bis de l'ordre).
2. **Périmètre** (P3) : décider avant la création d'attendre ou non `SCELLEMENT-JEUX-T07-JC` et `SCELLEMENT-CONCEPTS-T07` ; à
   l'écriture, `main` (à `06deda58`) porte JD et JA seulement.
3. **Interpréteur** (S-2) : accepter le risque d'une ligne différente sous Python 3.11, ou remesurer sous 3.11 (`python3.11`
   présent sur la machine, sans `torch` ; installation ≈ 1 Go, disque serré).
4. **Script v3** : S-1, S-3, S-4, S-6 proposés (§ 13) ; aucun bloquant, l'ordre les compense ; décision de la mère.
5. **Concordance** (S-5) : les ordres de P3-bis, de T0.8 et du texte de validité ne doivent pas étiqueter leurs instances `t06…`
   ou `t07…`.
6. **Contre-lecture** de l'ordre brouillon 4 par un sous-agent neuf (R2) avant son scellement définitif ; points du § 10.
7. **Limites de l'essai GARDES-CODE-01** : le bout en bout passe par `lecture_v2` (chemin de l'instance) ; `lecture_v1.etape_b`
   n'est éprouvée qu'au niveau de la reprise (`lecture_jeux`, qu'elle appelle aussi) ; l'artefact de bout en bout réécrit les
   mesures du faux run et rescelle `episodes-t06.json` (jeu construit, comme L5).

## Interdits et écarts déclarés

- Aucun chemin interdit ouvert ; aucune valeur de sonde de 7a sous mes yeux ; aucun appel de modèle ; aucune dépense ; aucun
  secret lu. **Écart déclaré (règle 3)** : outre la poussée de ma branche (permise), un clone du dépôt de travail depuis GitHub
  (`https://github.com/lciric/controle-ia-travail.git`, par le mandataire de la session, sans jeton posé), exigé par la consigne
  pour mesurer `ATT` « dans un clone fait comme celui de l'instance ».
- Git : dans le dépôt du programme, lectures seulement (`git show`, `git log`, `git ls-tree`, `git rev-parse`, `git merge-base`,
  `git cat-file`, `git diff --quiet`) ; dans `/home/user/wt-t07-degeneres` seulement (exception de la consigne) : `git add` et
  `git commit` du seul fichier neuf, `git push -u origin prep/t07-essai-degeneres-v1`, puis `git ls-remote`. **Écart déclaré** :
  la mesure de `ATT` exige un clone fait comme celui de l'instance ; j'ai cloné (clone partiel à branche unique), réglé
  l'extraction partielle et extrait le commit mesuré **dans un dépôt neuf du bac à sable**, jamais dans le dépôt du programme ni
  dans mon arbre ; supprimé à la fin.
- Règle 9 : aucune recherche récursive sur un dossier qui contient un chemin interdit ; `git grep` sur des chemins nommés (`tests/`,
  `src/…`, `scripts`, `docs/procedures`, `brouillons/*.md`) avec exclusion de `docs/notes/bras-attaque` ; `grep` sur des fichiers
  nommés ; `du` sur `docs/notes/g0-deux-semaines-v1/`, `docs/sources/invites-2606.08892-v1/` et `brouillons/` (sans chemin
  interdit) ; `find` dans le bac à sable seulement. Dépôts jouets du bac à sable (essai de la commande des morceaux du § 4.6) :
  `git init`, `commit`, `rm` dans ces dépôts seulement.
- Écritures hors de mon arbre et du bac à sable : l'ordre brouillon 4 et ce rapport, et leurs compagnons (chemins nommés par la
  consigne). Bac à sable nettoyé à la fin.
- Aucun refus de permission ni de classifieur.
