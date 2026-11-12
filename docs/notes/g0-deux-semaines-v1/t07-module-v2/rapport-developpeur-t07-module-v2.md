# Rapport du développeur neuf : module de lecture de T0.7, v2 (pour le brouillon 19) — v1

Consigne : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-09-2200-v1/consigne-developpement-module-t07-v1.md`
(`db327c18…`, égale à son compagnon). Texte de référence : `brouillons/T0.7-sondes-v0-v1-brouillon19.md` (`07039ed2…`). Arbre
`/home/user/wt-t07`, branche locale `prep/t07-module-v2`, partie de `eea731f5` ; extraction partielle (le disque était plein à
l'ouverture). Heures par `date -u`. Rédigé le 2026-11-10.

## Verdict

Les changements (x) à (xv) du brouillon 19 sont faits **en fichiers neufs** (R12), avec la garde adaptée de N-066 (G1 à G6, R14) et la
lecture du journal de P3-bis au format b8. Chaque garde neuve est éprouvée sur un cas sain et sur un artefact. L'énumération (0 bis)
du brouillon 17 est rejouée par les gardes du module, cas par cas (192 cas, 0 écart). **Le module n'est pas complet pour autant :
les sondes neuves ne sont toujours pas calculées.** Il s'agit des 30 couples neufs, du choix de la sonde principale par concept, des
prédictions T7-P3 à T7-P19, du placebo et de la base « coût seul ». C'est la pièce la plus lourde, et elle n'est pas commencée. En
mode réel, l'étape A refuse donc (code 2, motif écrit) dès qu'un jeu J-D ou J-C entre dans le périmètre. La configuration est écrite
comme **brouillon** : `entropie` reste nulle jusqu'au candidat (R9).

## Incident : disque plein, puis reprise

À 02:30 UTC il restait environ 3 Mo sur le disque. Le premier lancement des essais de référence a échoué sur `git init` dans une
fixture. Le classifieur a refusé ma commande de nettoyage de `/tmp/pytest-of-root` (motif « Shared Scratch Sweep » : elle touchait
aussi un dossier d'un autre processus). Je n'ai fait ni contournement ni nouvelle tentative. Vers 02:3x UTC, la mère a libéré
12 Go sans toucher à mon arbre. Contrôles faits ensuite :

- arbre propre (`git status` vide) ;
- index : 17 646 entrées ;
- fichier de motifs de l'extraction partielle intact ;
- connectivité de l'objet : `git fsck --connectivity-only` rend le code 0. Une première passe avait signalé des objets manquants
  sous `origin/main@{0}` : c'était une poussée de la mère en cours. La passe suivante est propre.

Rien n'était tronqué. J'ai relancé les essais de référence (`tests/test_t07_lecture_v1.py`) avec des dossiers temporaires mis
dans mon espace de travail, puis effacés : 138 passés, 1 sauté, en 201 s (02:34 à 02:37 UTC).

Un second redémarrage du conteneur (≈ 03:40 UTC) a fait perdre une suite complète en cours (arrivée à 70 %, sans résultat).
Après lui, le commit `9e844915` et ce rapport étaient intacts ; les essais de T0.7 ont été rejoués (section 4).

## 1. Inventaire : exigences du brouillon 19 qui touchent le module, contre le code

« v1 » désigne le module de `main` (`51a1874c`, R-1934), inchangé. « v2 » désigne les fichiers neufs de cette branche.

| exigence (brouillon 19) | lignes | état |
|---|---|---|
| clé obligatoire absente : arrêt qui la nomme | 2094-2096 | fait (v1, `_exiger`, `CleAbsente`) |
| manifeste de 7b, `episodes-t06.json`, `lecture-cout-t06.json` (table A), `arret.json` | 2098-2115, 2147 | fait (v1) ; `distillation-t06.json` sert seulement au repli, non mis en œuvre |
| fichier « mots et coût » (`ISSUE-MOTS-ET-COUT-T06`), lu selon T0.6 r6, point 3 | 2116, 2188-2198 | fait (v1) : objet à la racine ; clés en plus tolérées (`run_id`, `manifeste_sha256`, `plis`) ; `null` sur une dose non calculable ; ex aequo par le repli |
| fichier d'issue de P3-bis (`VERDICT-P3BIS`) | 2116-2117 | fait (v1, `lire_issue_p3bis`) ; jamais lu à l'étape A (v2) |
| **registre des préalables, fichier de décision du rendez-vous, journal de P3-bis au format b8** | 2117-2141 | **fait (v2, `journal_p3bis_v1`)** |
| audit des fuites et sa consigne | 2141-2143 | fait (v1) |
| scores de la base de T0.6 sous « recalcul » | 2143-2146 | fait (v1, format provisoire) ; sans objet sous « égalité » (valeur fixée) |
| mesures, textes, activations | 2148-2152 | fait (v1) ; textes non lus (témoins lexicaux non calculés) |
| **sondes figées : le seul fichier léger, 24 couples notés en descriptif, 200 directions par principale, fichier complet refusé** | 2153-2160, 2446-2448 | **fait (v2 : (xi), (xii))** |
| jeux génériques, phrases des concepts, provenance de P3, contrôle de disjonction des tâches d'évaluation et de réserve | 2161-2162 | **non fait** (seuls les sceaux des lignes de jeux sont lus) |
| **configuration : `garde_adaptee`, `portee_regle_4`** | 2163-2172 | **fait (v2 : (xiii), G6)** |
| **`sondes_lues` dérivée des lignes de jeux antérieures à la première ouverture de l'étape A et à la première ouverture de P3-bis** | 2172-2174, 2443-2446, 1587-1589 | **fait (v2 : (x), G5)** |
| fonctions sur scores (`comparer_scores_au_plancher` ; `difference_aires_appariee`, `aire_stratifiee` pour T4) | 2176-2186 | la première est faite (v1, essai d'égalité) ; les deux autres ne sont appelées nulle part (T4 non lue) |
| dérivation de Q, filtre par dose, P-064, P-065, scores de (ii) fermés sous L7b et L7c | 2188-2233 | fait (v1) ; repris tel quel par la v2 |
| essais R5 des brouillons 11 à 14 | 2234-2260, 2296-2323 | fait (v1) |
| **essais R5 des brouillons 15 à 17 (M-1, m-6, G1 à G5, R14, journal)** | 2261-2295 | **fait (v2)** |
| **G1 à G5 dans `ouvrir` ; ouverture réduite écrite dans `sondes-t07.json` et le manifeste ; R14** | 1524-1591, 2450-2457 | **fait (v2)** ; une ouverture réduite inscrite *pendant* l'étape A va dans `notation-t07.json` (écart 2) |
| sorties : `ouverture-t07.json`, `scores-actions-t07.npz`, `lecture-t07.json` | 2325-2353 | faits (v1, v2) ; dans `sondes-t07.json`, les 30 couples neufs et leurs aires de validation manquent ; dans `lecture-t07.json` manquent `placebo`, `bases.cout_seul`, `predictions` au-delà de T7-P1 et T7-P2, et les réserves R1 à R13 par identifiant (seule R14 a le sien) |
| aucune sortie sous un refus ; `REFUS-T07` écrite après tous les contrôles | 2357-2365 | fait (v1, v2) |
| relance, lecture unique, aucune relance après un code 3, G4 | 2367-2389 | fait (v1, v2) |
| énumérations : (0) 2 048 cas ; (0 bis) 192 cas ; grilles (1) à (3) | 2403-2414 | (0) : contre v1 et contre v2 ; **(0 bis) : v2, cas par cas** ; (1) à (3) : v1 |
| `lire_registre_t07` contre `controle_lecture_t06_v1.py` | 2414-2416 | **fait (v2) au commit `061ac380`** ; l'essai de la v1 se saute toujours, faute de sa branche |
| répétition jouet sur la chaîne de T0.6 en mode `jouet` ; repli du recalcul | 2419-2422 | **non faits** |
| commande en ligne, codes 0, 2 et 3 | 2459-2467 | fait ; la commande s'appelle `lecture_v2` (écart 5) |

**Les trois questions internes du module :**

- **Q9 (format du fichier des scores de la base) : sans objet.** `controle_aire` vaut « égalité » (marqueur `CONTROLE_AIRE_T06`). Le
  candidat r6 écrit `aire` comme « le même nombre », sans arrondi. Le format provisoire de la v1 n'est appelé que sous « recalcul ».
- **Q10 (valeur et nom des clés du niveau de la base) : la valeur est fixée, les noms restent à déclarer.** La valeur est 0,95
  (brouillon 19 et r6, point 2). Les noms `niveau_base_t06` et `scores_base_t06` ont été choisis par le développeur : le texte doit
  les écrire dans la liste des clés de la section « Module ».
- **Q11 (arrêt de T0.6 sans `lecture-cout-t06.json`) : toujours ouverte.** Le point 1 de r6 dit que la chaîne écrit
  `lecture-cout-t06.json` et « `resume.json` ou `arret.json` », mais pas si le premier existe quand la chaîne s'arrête. Le module
  suit la lettre : fichier absent → refus (attente).

## 2. Ce qui est fait (fichiers neufs ; aucun fichier existant modifié)

- `src/controle_ia/t07/journal_p3bis_v1.py` lit trois écrits de P3-bis :
  - le journal des ouvertures : forme vérifiée ligne à ligne (en-tête, six cellules, clé, date, mode, ordre des ouvertures). Une
    ligne `REFUS-OUVERTURE-P3BIS` n'est jamais une ouverture ;
  - le registre des préalables : `GARDE-ADAPTEE-T07-P3BIS` au plus une fois ; `RENDEZ-VOUS-P3BIS-N` à numéros consécutifs et dates
    strictement croissantes ; sceaux vérifiés ; toute autre clé refusée ;
  - le fichier de décision cité par la ligne de rendez-vous du même numéro, jamais un fichier pris par son nom.
- `src/controle_ia/t07/garde_adaptee_v1.py` porte les règles pures :
  - G1, G2 (motif selon la décision de la dernière ligne de rendez-vous), G3, G4, G5 et R14 ;
  - les appuis des lignes `reduite` et `pleine`, comparés aux lignes citées ;
  - `enumerer_0bis`, qui joue les 192 cas de (0 bis) par ces mêmes gardes. Chaque garde ne voit que ce qui existe à son instant :
    l'étape A à son ouverture, la fin de l'étape A, puis l'étape B.
- `src/controle_ia/t07/lecture_v2.py` remplace `ouvrir`, `etape_a`, `etape_b`, `exiger_configuration`, la liste des sondes lues et la
  notation, et reprend toutes les autres fonctions de la v1 sans les toucher. Ajouts :
  - à l'étape A, `VERDICT-P3BIS` est permise et admise sous G2. Le fichier d'issue n'est jamais lu à l'étape A ;
  - garde de fin d'étape A : nœud si une ligne `pleine` ou `pleine-anticipee` précède la fin, ou si `VERDICT-P3BIS` est inscrite sans
    ouverture réduite ;
  - à l'étape B, G3 passe avant `lire_issue_p3bis`. Un verdict en prose absent donne un refus (attente), jamais L0a ;
  - R14 est écrite, et L0b, L0c, L1 (fichier illisible), L7b et L7c sont marquées « finales pour 7b » sur un lancement réduit ;
  - les 24 couples figés sont notés à l'étape A et lus en descriptif à l'étape B (aire seule) ;
  - les activations sont lues couche par couche, une seule couche en mémoire à la fois ;
  - commande `empreinte-config`.
- `tests/test_t07_lecture_v2.py` : 63 essais (liste à la section 4).
- `brouillons/T0.7-sondes-v0-v1-brouillon19-pieces/configuration-t07-v1.json`, avec son compagnon. Nom proposé.
- Rien n'est écrit dans le brouillon 19.

## 3. Configuration de T0.7 (brouillon de configuration)

Fichier `brouillons/T0.7-sondes-v0-v1-brouillon19-pieces/configuration-t07-v1.json` (`8b2d8138…`), mode `reel`, clés exactement
`CLES_CONFIG` de la v2.

**Valeurs tirées du texte :**

- section « Module » : `niveau_decisif` 0,9875, `quantile_plancher` 0,95, `n_plancher` 200, `tirages_aire` 2 000,
  `permutations_placebo` 200, `mahalanobis_calcul` `produit_matriciel_v2`, `ecart_ex_aequo` 0,005, `couches` [7, 15, 23],
  `seuil_degeneres` 0,01, `registre`, `p064` true ;
- marqueurs fixés au brouillon 18 : `controle_aire` « egalite », `tolerance_aire` 5 × 10⁻⁴, `marques_autres_taches`
  [T06, T08, P3BIS, NARC] ;
- G6 : `garde_adaptee` true, `portee_regle_4` « restreinte » ;
- `familles` : les cinq familles des couples ;
- Q10 : `niveau_base_t06` 0,95, `scores_base_t06` nul ;
- `fichiers_sondes` = `planchers_p3` = le fichier léger `701f73bd…` ;
- sondes principales de P3 pour tromperie et enjeux ; sondes neuves (dissimulation, domaine) nulles ;
- `predicteurs_triviaux` [jetons_notes, pas, mention_etendue] (« Métrique ») ;
- `go_id_attendu` GO-2026-11-02-28 et `go_id_refuse` GO-2026-11-08-11 (l. 459, 2066).

**Valeurs encore ouvertes :**

- `entropie` : **nulle**. Elle est tirée au candidat (marqueur `ENTROPIE_T07`, R9). Le module refuse une entropie nulle.
- `reglages` : nul. Le texte nomme la clé sans lui donner de valeur, et elle reste sans objet tant que les sondes neuves ne sont pas
  apprises.
- `jetons_entrainement` : nul (aucune sonde neuve nommée).
- `code_t07_exige` : false (DS-3 bis non accordée).
- `preenregistrement` : `prereg/T0.7-sondes-v0-v1.md`.

## 4. Essais

- `tests/test_t07_lecture_v1.py` (inchangé) et `tests/test_t07_lecture_v2.py` : **201 passés, 1 sauté** (v1 : 138 passés, 1 sauté ; v2 : 63
  passés), en 309,5 s, sur cet arbre, au code du commit `9e844915` (03:08 à 03:13 UTC, en même temps que la suite complète).
  **Rejoués après le second redémarrage du conteneur** (≈ 03:40 UTC), au même commit : 201 passés, 1 sauté, en 370,0 s
  (03:49 à 03:55 UTC). Une tentative entre les deux (03:45 UTC) a donné 69 passés et 133 erreurs, toutes
  `FileNotFoundError` sur le dossier temporaire : par erreur, j'avais effacé le dossier parent du `--basetemp`, et pytest ne le
  recrée pas. Ce n'est pas un défaut du module ; le run est écarté et la suite complète lancée en même temps a été arrêtée.. Le saut est l'essai d'égalité de la v1, dont la branche manque ; la v2 le reprend au commit
  `061ac380`.
- Essais de la v2 (chacun sur un cas sain et sur au moins un artefact) :
  - configuration : (xiii), G6, (xii), mode réel, brouillon de configuration ;
  - périmètre : (x) en relance après R11 ; G5 (réduite, refus de P3-bis) ;
  - G1, et m-4 ;
  - G2 : cas sain avec fichier d'issue non lu, et douze artefacts ;
  - ouvertures pendant l'étape A ; verdict pendant l'étape A ; `pleine-anticipee` ;
  - G3 : cas sain, verdict en prose absent puis relance, empreinte autre, cinq artefacts de journal ;
  - G4 ; relance R11 sur le même lancement ; R14 avec L7b finale et (ii) fermée ;
  - journal mal formé (huit cas) ; journal sain ; préalables (six artefacts, plus un numéro de décision différent) ;
  - 24 couples (avec un artefact de Mahalanobis) ; fichier léger réel croisé avec `sondes-figees.json` (`fb418127…`, lu par
    `git show`) ; compte réel autre que 24 ;
  - énumérations (0 bis) (192 cas) et (0) (2 048 cas, garde v2) ;
  - antériorité du chemin normal ; B-1 avec relance et lecture unique ; commande en ligne ;
  - absence de moyenne ; égalité à `controle_lecture_t06_v1` au commit `061ac380` ; reprises de la garde A ; préalables absents.
- **Suite complète du dépôt sur cet arbre** (`-o tmp_path_retention_policy=failed`, au commit `9e844915`, de 03:56 à 04:52 UTC, en
  3 357 s) : **3 087 passés, 357 échoués, 13 erreurs, 24 sautés**. Aucun échec ni aucune erreur dans un essai de T0.7 (`test_t07_lecture_v1.py` et `test_t07_lecture_v2.py` : 0 sur 202).
  Les échecs viennent de 31 fichiers d'essais sans rapport avec ce module. Le plus gros groupe compte 98 échecs dans
  `test_extraire_t05.py` ; suivent 92 dans `test_lanceur_durable_v5_a1v4.py`, puis 28, 27 et 22 dans `test_noter_rejeu_juges_v1.py`,
  `test_noter_pilote_a.py` et `test_pilote_a.py`. Causes relevées dans les messages d'erreur :
  - fichiers absents de cette **extraction partielle** : `docs/notes/ideation-organisme-v1/…` (89),
    `docs/sources/invites-2606.08892-v1/…` et `invites-2606.07054-v1/…` (67), `docs/procedures/T0.5-extraction-v1/…` (39),
    `rapports/fille-ideation-1-v1/…` (2), `donnees/T0.7-faits-repe-v1/…` (1) ;
  - `git commit` sans rien à committer dans des essais du pilote A, après un refus de leur module (62) ;
  - des assertions qui en découlent ;
  - `pypandoc` absent de l'environnement (3).

  Ces causes sont attribuées à l'extraction partielle et à l'environnement, **sans vérification un à un**. La référence reste la
  suite complète de la mère sur un clone entier.

## 5. Valeurs que la mère mettra dans le brouillon 19

- `COMMIT_CODE_T07` : `9e8449156e2d01b44de16641154921e738b6afcf` (branche locale `prep/t07-module-v2`, non poussée). **Provisoire** : le code n'est ni contre-lu
  (R2) ni répété en jouet, et les sondes neuves manquent.
- `EMPREINTES_CODE_T07` (sha256 au commit ci-dessus) :

| fichier (au commit `9e844915`) | sha256 |
|---|---|
| `src/controle_ia/t07/__init__.py` (égal à `51a1874c`) | `553bd9d29b56f0923859da2d3a63fadf9891c4274b9bb23fc367496e77e5a61e` |
| `src/controle_ia/t07/criteres_v1.py` (égal à `51a1874c`) | `12b999fecce093372a29fb70d8c11eb7fe965f34c8746a31b399baaecc5ae8c5` |
| `src/controle_ia/t07/garde_adaptee_v1.py` (neuf) | `c404e21a8eeb0c50cbc78940e5df3ccb93a03383c15e3b43baa4b64f998c6bd0` |
| `src/controle_ia/t07/journal_p3bis_v1.py` (neuf) | `acb504cafcd06795b77a364df84f2e4c73f501c610261712fd023003398aa523` |
| `src/controle_ia/t07/lecture_v1.py` (égal à `51a1874c`) | `62b34790346123924c275c4e2021ea31db26837c5b7840e9e047d272a54c9678` |
| `src/controle_ia/t07/lecture_v2.py` (neuf) | `d6e433ddb9c49a37c9b0143313958c9df45a58ddab740a73ac39db303116e888` |
| `src/controle_ia/t07/mahalanobis_v1.py` (égal à `51a1874c`) | `b28163062aa8d39cf3894b327a7446f63d50d4f1394eac894b16b4da8ff962f9` |
| `src/controle_ia/t07/plancher_v1.py` (égal à `51a1874c`) | `ac6e8263293ed30c807ef91f8eab0adbcbf8e1b91d5e4c56e73dbffa1a7099dc` |
| `src/controle_ia/t07/registre_v1.py` (égal à `51a1874c`) | `914b8f374ce8f8bc6550d03c34c5f6c2a97ac93b8ce44da24fd88229185ffca0` |
| `tests/test_t07_lecture_v1.py` (égal à `51a1874c`) | `ae82fe0d606fa22223fa86f846788145b7c436d12fe65c2ddb3359a907329722` |
| `tests/test_t07_lecture_v2.py` (neuf) | `6274d6b97e706e166a0f3d8c53c204e9cbbe79b1166734e6260f6b4b888cafff` |

- `EMPREINTE_CONFIG_T07` : **pas encore de valeur valable.** L'empreinte canonique du brouillon de configuration (calculée par
  `lecture_v2.empreinte_canonique`) est `9564d0ecb49fc213cb35a560927499c5b3f898c11251ed81ef52202cd1bed2d5`. Elle changera dès que
  `entropie`, `p064` (P-064), `code_t07_exige` (DS-3 bis) ou `preenregistrement` seront fixés. La valeur finale sera rendue par
  `python -m controle_ia.t07.lecture_v2 empreinte-config <fichier scellé sous prereg/>`, qui refuse un brouillon incomplet.

## 6. Écarts entre texte et code (à trancher ou à écrire dans le texte)

1. **Sondes neuves non calculées** : 30 couples, choix de la sonde principale, aires de validation, règle d'ex aequo, T7-P3, T7-P4,
   T7-P6, T7-P9, T7-P10, T7-P15 à T7-P19, placebo (R9), base « coût seul », témoins lexicaux, directions des concepts. Le texte
   veut aussi, en mode réel, `fichiers_sondes` = le seul fichier léger. Les deux sondes neuves doivent donc être apprises à l'étape
   A, sur l'instance, avec le modèle. Le module refuse l'étape A réelle dès qu'un jeu J-D ou J-C est dans le périmètre : le refus
   est explicite, jamais silencieux.
2. Une ouverture réduite inscrite **pendant** l'étape A ne peut pas aller dans le manifeste ni dans `sondes-t07.json`, déjà scellés
   (R12). Elle est écrite dans `notation-t07.json`, et R14 la lit à l'étape B dans le journal.
3. Interprétations déclarées de la garde adaptée (`garde_adaptee_v1`, en tête du fichier) :
   - G1 est appliquée dès que `VERDICT-P3BIS` est lue, sur tout chemin. Elle rend donc `SCELLEMENT-T07` nécessaire à l'étape B ;
   - une ligne `pleine` datée exactement de la fin de l'étape A compte « avant » ;
   - la dernière ligne de rendez-vous « à la date de l'ouverture réduite » est la dernière datée strictement avant elle ;
   - une ligne de jeux datée exactement de l'instant de fermeture est hors du périmètre ;
   - les appuis des lignes `reduite` sont comparés à chaque lecture du journal (étapes A et B), même sans `VERDICT-P3BIS` ;
   - une ligne vide du journal est ignorée ;
   - les fichiers de P3-bis sont lus sous `RACINE`, comme les fichiers cités par le registre.
4. Clés de configuration que le texte ne nomme pas, gardées de la v1 : `entropie`, `go_id_attendu`, `go_id_refuse`,
   `fichiers_sondes`, `sondes_par_concept`, `planchers_p3`, `jetons_entrainement`, `conditions`, `predicteurs_triviaux`,
   `code_t07_exige`, `preenregistrement`, `niveau_base_t06`, `scores_base_t06`. Les clés `reglages` et `familles` sont nommées par
   le texte, mais sans valeur.
5. Commande : le texte nomme `python -m controle_ia.t07.lecture_v1`. La v2 est un fichier neuf, d'où `lecture_v2`. Le texte doit
   citer les neuf modules et les deux fichiers d'essais (« six modules » au brouillon 18).
6. Non faits, que le texte exige :
   - le contrôle de disjonction des tâches d'évaluation et de réserve ;
   - T4 (`aire_stratifiee`) et `difference_aires_appariee` ;
   - les réserves R1 à R13 par identifiant ;
   - les durées dans le résultat ;
   - la répétition jouet sur la chaîne de T0.6 ;
   - le repli du recalcul.
7. L'essai d'égalité de la v1 (`test_lire_registre_t07_egale_controle_lecture_t06`) n'a pas été modifié, comme la consigne
   l'interdit. Il se saute encore ; son double, pointé sur `061ac380`, passe.

## 7. Ce qui reste avant la contre-lecture du code (par un autre modèle)

1. Trancher l'écart 1 : écrire l'apprentissage des sondes neuves à l'étape A, ou bien changer le texte (par exemple, les sondes
   neuves fournies par un fichier scellé avant l'étape A). Puis écrire les lectures et réserves qui manquent (écart 6).
2. La répétition jouet, de bout en bout, sur `lanceur_v5` en mode `jouet`.
3. Le texte : nommer les clés de l'écart 4, la commande `lecture_v2`, les neuf modules et les deux fichiers d'essais ; trancher Q11.
4. Au candidat : `entropie`, P-064, DS-3 bis ; configuration copiée sous `prereg/` et scellée ; `EMPREINTE_CONFIG_T07` par
   `empreinte-config` ; `COMMIT_CODE_T07` et `EMPREINTES_CODE_T07` refaits après la contre-lecture.

## Interdits tenus

- Aucun fichier sous embargo n'a été ouvert, extrait ni listé par son nom. Aucune donnée réelle de 7a n'a été lue. Le seul fichier
  réel lu est le fichier léger de P3 ; la liste de P3 l'a été par `git show`.
- Ni `extraire_mesures_epreuve_t06_v1.py` ni `lecture-sondes-t06.json`.
- Aucune valeur de clé : ni `env`, ni `printenv`. La garde des secrets du dépôt (`depot_expurge_v5.secrets_dans`) a donné 0 sur les
  fichiers neufs avant chaque commit ; seul le compte a été imprimé.
- Aucun appel externe, aucune dépense. Ni `fetch` ni `push`. Rien n'a été fait sur `main` ni dans `/home/user/controle-ia-travail`
  (à part l'interpréteur). `/home/user/integ-t06` n'a pas été touché.
