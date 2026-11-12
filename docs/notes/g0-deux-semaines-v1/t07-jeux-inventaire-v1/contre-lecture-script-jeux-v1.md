# Contre-lecture courte du script de vérification des jeux synthétiques de T0.7 (D-5 (a), écart E-7) — v1

**Verdict (une ligne) : conforme à la consigne v3 pour les contrôles 2, 3, 6, 9, 10 et `assembler` ; aucun défaut
bloquant ; quatre défauts à corriger (essais manquants, garde de l'aire, ordre des lignes) et cinq mineurs ; aucun ne
change l'acceptation de J-D ni de J-A.**

- **Auteur** : contre-lecteur neuf (Claude Fable 5.2), sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`.
  Je n'ai écrit ni le script, ni ses essais, ni les jeux, ni T0.7, ni leurs contre-vérifications. **Exclu ensuite de
  tout rôle de lecteur de P3-bis.**
- **Heures** (relevées par `date -u`) : consigne vérifiée et lue le 2026-11-10 à 08:23:45 UTC ; essais rejoués de
  08:25:36 à 08:25:49 UTC ; rédaction commencée à 08:33:32 UTC ; scellement : heure du compagnon `.sha256`.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/consigne-cl-script-jeux-t07-v1.md`
  (`5988dd7e26aaaa3efb4eaa1d1dc514905d65c5170ccb598491161b67c92a67f9`, vérifiée avant lecture) ; interdits communs v2
  (`1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`, vérifiés), tenus en entier, règle 9 comprise.
- **Pièces lues** (empreintes recalculées ici) :
  - `scripts/verifier_jeux_synthetiques_t07_v2.py` au commit `bd02ae3e` :
    `e53c9c2729cf17ac1b0f3c6fbf81169c1d568bbccb85fb1535981b4094341d22`, **égal** au fichier de `main` (`56e09d9a`) et à
    l'empreinte écrite au journal du lot 1 ; lu en entier (1 320 lignes) ;
  - `tests/test_verifier_jeux_synthetiques_t07_v2.py` au commit `bd02ae3e` :
    `8c754af3536c5e769af87a28a9cdb34c749c554c16b1376492d5e9348eeda94d`, égal à `main` ; banc, essais sains, essais
    de l'assemblage et des contrôles 2, 3, 6, 9, 10 lus ; les autres par leurs noms ;
  - consigne v3 `docs/procedures/consigne-jeux-synthetiques-T0.7-v3.md`
    (`d9de50a6f4f7a8add3465ad53a5b894703f70b8777b7f8e428417ebfcd73b485`), en entier ;
  - `donnees/t07-jeux-synthetiques-v2/provenance-v2.md`
    (`f43676709242df3f4140bfa39b744ec08eb7bd24b7e7a85a5a46973fdc058b82`, compagnon conforme ; passages E-6 à E-8) ;
    `journal-verification-v2.txt` (`58906bb4c6e609397f5ec0e04e0219314994f4442de641b93536e902233641cb`, compagnon
    conforme ; en-tête, lignes de contrôle, bilan) ;
  - inventaire `docs/notes/g0-deux-semaines-v1/t07-jeux-inventaire-v1/inventaire-jeux-t07-v1.md`
    (`c9910a541dbfd80612fbe557a270b02acc99aef3e0f44c8095f676c3c8e0740b`) ;
  - en appui : `src/controle_ia/environnements/propositions.py` l. 236-269 (module gelé, assemblage des contextes) ;
    `docs/notes/g0-deux-semaines-v1/rapport-verifier-jeux-T0.7-v2-v1.md` l. 119-135 (choix déclarés du script) ;
    `registres/decisions.md`, ligne R-2106.
- **Jamais ouverts** : tout `lecture-sondes-t06.json` ; la lecture B et sa branche ; tout `diag/` et `runs/` de 7a ;
  `essai/t06-explo-v3` ; `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ;
  l'étiqueteur ; `scripts/extraire_mesures_epreuve_t06_v1.py` ; **les textes d'actions de P3** (ni ouverts, ni passés
  au script : aucun lancement du mode `verifier` sur des entrées réelles). Aucune recherche récursive : `grep` sur des
  fichiers nommés seulement. Aucun appel externe, aucune dépense, aucune écriture git. Aucun refus de permission ni de
  classifieur rencontré.
- **Écrit** : ce fichier et son compagnon ; le dossier temporaire `/home/user/cl-script-jeux-tmp/`, effacé par son
  chemin exact.

## 1. Essais rejoués

Une fois, à 08:25:36 UTC : `PYTHONPATH=src .venv/bin/python -m pytest -q tests/test_verifier_jeux_synthetiques_t07_v2.py
--basetemp /home/user/cl-script-jeux-tmp/basetemp -p no:cacheprovider` (sans cache ni code compilé écrits dans le
dépôt) : **66 essais passés, 0 échec** (12,3 s). Jeux factices écrits par les essais ; aucun texte de P3 lu.

## 2. Consigne v3 → script (contrôles du mandat)

| contrôle | exigence (consigne v3) | script (lignes) | jugement |
|---|---|---|---|
| **2** tâches | § 8 c. 2, § 2, § 7 : 32 identifiants, tous dans la réserve, aucun d'évaluation ; comptes 10, 10, 5 + 5 | `controle_2_taches` l. 683-712 ; `charger_enonces` l. 294-315 (chaque énoncé égal à la tâche de réserve, sinon refus, code 2) ; arrêt de la suite si tâche hors des énoncés, l. 1223-1225 | **conforme** ; nombre de tâches autre que 32 : écart écrit au journal (l. 1178-1179), jamais scellable |
| **3** contextes | § 8 c. 3, § 2, § 5.2, § 6.1 : recalcul à l'octet ; identiques (J-C, J-A) ; J-D : bloc à la fin du message système, rappel avant « Your action: » ; rotations A (mod 20) et B (mod 8), p = 10 r + k | `controle_3_contextes` l. 715-755 ; `contexte` l. 419-429 (module gelé, N = 1, T = 10, sans guide) ; `entree_attendue` l. 444-446 | **conforme** ; places vérifiées sur le module gelé (`propositions.py` l. 247-248 et 266-268) ; nombre d'entrées 20 et 8 contrôlé par `controle_banques` l. 766, 786 |
| **6** longueurs | § 8 c. 6, § 2 : 90 à 260 mots ; écart ≤ 15 % en mots, caractères, jetons, réponse entière et avant `COST:` (J-C, J-A) ; blocs 18-40, rappels 3-12, incitations 15-40 ; tokeniseur obligatoire, empreinte `79e3e522…`, sinon jeux non scellés | `controle_6_longueurs` l. 917-947 ; `charger_tokeniseur` l. 390-409 (refus, code 2) ; `controle_banques` et `_controler_entree_a` l. 758-825 | **conforme** ; « à 15 % près » lu |a − b| / max : choix déclaré (rapport du script, point 5), voir M-3 |
| **9** recopie | § 8 c. 9, § 7 : aucune suite de 8 mots commune avec les textes interdits ni avec l'énoncé ; blocs, rappels, incitations aussi ; doublons dans et entre les jeux ; bloc en double dans une tâche ; source absente déclarée | `controle_9_recopie` l. 981-1030 ; `charger_textes_interdits` l. 358-387 (fichier absent = refus) ; `--textes-absents` l. 1207-1209 | **conforme** ; exclusion des suites aussi présentes dans l'énoncé (l. 1001) : permise par le § 7 et sans trou, la même suite est alors un défaut « recopiée de l'énoncé » (l. 1003) |
| **10** fuite lexicale | § 8 c. 10 : par jeu et par mode, réponse entière et avant le champ, unigrammes et bigrammes ; défaut dur si ≥ 0,25 d'un côté et ≤ 0,05 de l'autre ; aire d'une régression logistique tf-idf, L2 fixe de 1, une tâche laissée de côté, moyenne ; ≥ 0,90 = réserve | `controle_10_fuite_lexicale` l. 1099-1138 ; `aire_sac_de_mots` l. 1046-1096 | **conforme** (seuils inclusifs, non arrondis avant comparaison ; pénalité ½·‖w‖², intercept libre, aucun tirage) ; voir C-3 |
| **`assembler`** | § 3, § 11 (formulaire) : `membre` tiré par graine, clé « ordre-membres » ; contextes assemblés ; `cout_declare`, `position_cost` calculés ; rien d'écrasé | `assembler` l. 480-560 ; `_membres_de_remise` l. 563-602 ; `membre_positif_en_A` l. 431-437 (R9, par paire) | **conforme** ; paire non assemblable exclue, listée, code 1 ; jeu vide = refus avant toute écriture ; le tirage est recontrôlé par le contrôle 1 (l. 672-676) ; voir C-4 |

**Repli silencieux** : aucun trouvé dans les contrôles 2, 3, 6, 9 ni dans `assembler`. Les paires sautées par les
contrôles 5 à 7 et 10 (`_valide_format`) portent déjà un défaut du contrôle 4. Deux points seulement ne sont pas
gardés : C-3 (aire) et M-1 (source absente non déclarée).

**Cas sain et artefact (R5)** : présents pour les contrôles 2 (4 essais), 3 (6), 6 (5), 9 (5), 10 (2) et `assembler`
(6 essais, plus le cas sain du banc) ; manques : C-1, C-2, M-4.

## 3. Défauts

### Bloquant

Aucun.

### À corriger (version suivante du script et de ses essais ; rien à refaire sur J-D ni J-A)

- **C-1 — Lecteurs des textes interdits sans essai (R5).** Les branches `.jsonl`, `.json`, `.txt`, le refus « aucun
  paragraphe cité » et le refus « extension inconnue » (l. 362-385) ne sont éprouvés par aucun essai : le banc ne passe
  qu'un `.md`. Or la branche `.jsonl` est celle qui lit les textes d'actions de P3 dans le lancement réel. Atténuation
  constatée : le journal du lot 1 (`58906bb4…`, l. 17-18) écrit 6 textes et 156 mots pour `P3-consignes-v1.md`,
  9 600 textes et 426 276 mots pour le fichier de P3 : la lecture n'était pas vide.
- **C-2 — Deux gardes sans artefact (R5).** (a) L'exclusion `(g & grammes_interdits) - ge` (l. 1001) : aucun essai avec
  une suite commune au texte interdit et à l'énoncé. (b) Les refus de `charger_enonces` « diffère de la tâche de
  réserve scellée » et « n'est pas une tâche de réserve » (l. 309-313), qui portent le « tous dans le fichier de
  réserve » du contrôle 2 et la base du contrôle 3 : seul le refus sur les clés est éprouvé.
- **C-3 — Aire du sac de mots sans garde.** `aire_sac_de_mots` ne lit pas `res.success` (l. 1090-1093) et saute un pli
  sans rien écrire (l. 1060-1061, l. 1094) ; seul le nombre de plis paraît au journal, sans défaut ni réserve s'il est
  inférieur au nombre de tâches. Une aire non convergée ou moyennée sur moins de 32 plis serait rapportée comme une
  autre. **Mesuré ici sur J-A scellé** (`5b040920…`, même fonction, `minimize` espionné, aucun fichier écrit) :
  32 plis et 32 convergences sur 32 pour chacune des quatre aires (au plus 15 itérations) ; aires 0,815 / 0,802
  (« contrôles »), 0,736 / 0,741 (« direction »), égales au journal. À corriger : défaut ou réserve si un pli manque ou
  ne converge pas.
- **C-4 — L'ordre des lignes porte l'étiquette.** `assembler` écrit toujours le membre d'étiquette 0 avant celui
  d'étiquette 1 (l. 524, 590, 602) : le champ `membre` est tiré, mais le rang de la ligne dans la paire ne l'est pas.
  Le § 3 de la consigne veut « qu'aucune position ne porte l'étiquette ». **Constaté sur les fichiers scellés** : J-D
  (`32f41288…`) et J-A (`5b040920…`), 320 lignes impaires sur 320 d'étiquette 0, 320 lignes paires sur 320 d'étiquette
  1 ; `membre` A réparti 149 / 171 (J-D) et 156 / 164 (J-A) entre étiquettes. Sans effet sur une lecture qui prend
  l'étiquette dans son champ ; à **déclarer** (provenance ou T0.7) et à faire tenir par la chaîne de T0.7 et par tout
  outil d'échantillonnage : aucun usage du rang de ligne. Version suivante : lignes écrites dans l'ordre A, B.

### Mineur

- **M-1** — `--textes-absents` est libre : rien n'oblige à passer ou à déclarer les épisodes de T0.6 ; une omission
  serait muette. Au lot 1, la source est déclarée (journal l. 19).
- **M-2** — Doublon cherché sur la réponse exacte, bloc en double par identifiant (choix déclaré, rapport du script,
  point 8). Mesuré ici après normalisation (sans casse ni ponctuation) : 0 réponse partagée par deux paires dans J-D,
  0 dans J-A, 0 entre J-D et J-A.
- **M-3** — « À 15 % près » lu sur le plus long des deux (choix déclaré, point 5). Sous la lecture sur le plus court,
  J-A aurait des dépassements : 6 paires en mots avant `COST:`, 4 en mots, 1 en caractères, 1 en caractères avant
  `COST:` (jetons non mesurés : tokeniseur absent de la machine). Pire écart sous la lecture du script : 0,145 (mots).
  J-D sans objet (réponse identique).
- **M-4** — Essais : aucun artefact où seul l'empan avant `COST:` dépasse ; aucune borne exacte (15 %, 0,25, 0,05) ;
  aucun essai d'une fuite par bigramme seul.
- **M-5** — Le contrôle 3 et `assembler` appellent la même fonction `contexte` : le contrôle ne peut pas voir une faute
  de cette fonction. Elle est vérifiée ici par lecture contre le module gelé, et par les assertions de l'essai sain
  (l. 277-299). L'égalité des copies d'annexes au texte de la consigne est hors du script (faite par le lot 1).
  La ligne de commande du § 8 ne porte ni le mot `verifier` ni `--tokeniseur` : écart de forme, déclaré dans l'en-tête.

## 4. Effet sur J-D et J-A (R-2106)

**Aucun défaut ne change l'acceptation de J-D ni de J-A.** La règle appliquée (32 tâches, code 0, contre-vérification
sans indice confirmé, aire < 0,90) repose sur des contrôles conformes ; les deux points non gardés qui touchent cette
règle sont mesurés sains sur les fichiers scellés (C-3 : 32 plis convergés, aires égales au journal ; M-2 : aucun
doublon). C-4 demande une déclaration, pas une réécriture : les fichiers scellés et leurs empreintes ne changent pas.
M-3 dépend d'un choix de lecture déjà déclaré.

## 5. Réserves de cette contre-lecture

1. Lecture courte, bornée au mandat : les contrôles 1, 4, 5, 7, 8 et le contrôle des annexes ne sont lus que là où
   les contrôles du mandat en dépendent.
2. Je n'ai relancé ni `verifier` ni `assembler` sur des entrées réelles (les textes de P3 ne doivent pas être passés au
   script) : le code 0 du lot 1 est lu dans son journal scellé, pas rejoué.
3. Les mesures de la section 3 lisent J-D et J-A scellés (textes des jeux, aucune activation, aucun score de sonde).
