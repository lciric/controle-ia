# Journal de rédaction — consigne v1 du jeu de phrases des concepts de T0.7 (`consigne-concepts-sans-lien-T0.7-v1.md`)

- **Rédacteur** : Claude Opus 5.5, sous-agent neuf de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy` ; n'a écrit ni
  T0.7, ni son module, ni ses jeux, ni le brouillon 1 de la consigne des concepts, ni leurs contre-lectures. **Il a lu
  T0.7 (brouillon 20, passages) : exclu ensuite de tout rôle de lecteur de P3-bis.** Il n'a écrit **aucune phrase du jeu** ;
  il a écrit les huit paires d'exemple de la section 5 de la consigne, exclues du jeu par le contrôle C9.
- **Heures** (relevées par `date -u`) : travail commencé le 2026-11-10 à 07:53:10 UTC (vérification des empreintes) ;
  rédaction de la consigne commencée à 08:08:02 UTC ; journal commencé à 08:14:54 UTC ; heure du sceau : celle du
  compagnon `.sha256`, donnée dans le rapport à la mère.
- **Consigne suivie** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/consigne-lot3a-consigne-concepts-t07-v1.md`
  (`8a9a78c51cca12b909b4219c171ac67ffb2a9c2adf44c3af659406315dd9f382`, vérifiée avant lecture) ; **interdits communs v2**
  (`…/interdits-communs-v2.md`, `1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`, vérifiés), tenus en
  entier, règle 9 comprise.
- **Clone** : `main` au commit `a931ec5d` au départ ; la mère a avancé `main` pendant ce travail jusqu'à `61fc52a8`
  (R-2102 à R-2104) ; le différentiel ne touche ni `brouillons/`, ni `docs/procedures/`, ni `src/`, ni `scripts/`, et les
  six sources vérifiées au départ ont gardé leur empreinte (revérifiées à 08:14 UTC).

## 1. Sources lues (chemin, empreinte, ce qui a été lu)

| source | empreinte | lu |
|---|---|---|
| consigne de la mère (lot 3, étape 1) | `8a9a78c5…` | en entier |
| interdits communs v2 | `1ee3b370…` | en entier |
| `brouillons/T0.7-concepts-sans-lien-consigne-v1-brouillon1.md` | `acc7bdfb…` | en entier |
| `docs/notes/g0-deux-semaines-v1/t07-jeux-inventaire-v1/inventaire-jeux-t07-v1.md` | `c9910a54…` | en entier (sections 3, 4.2, 4.3, 5 lot 3, 6, 7 en particulier) |
| `src/controle_ia/t07/sondes_neuves_v1.py` au commit `8dc1cb09` (`git show`) | `b1c59783…` | en entier |
| `src/controle_ia/t07/lecture_v2.py` au commit `8dc1cb09` (`git show`, `git grep` borné à ce fichier) | `9d5c1c05…` | l. 264-279 et lignes trouvées (phrases, concepts, `min_concepts`) |
| `src/controle_ia/t07/registre_v1.py` (égal sur `main` et à `8dc1cb09`) | `914b8f37…` | la constante `SCELLEMENT_CONCEPTS_T07` (l. 51) |
| `src/controle_ia/sondes/temoins.py` (égal sur `main` et à `8dc1cb09`) | `3b051b6f…` | l. 1-140 |
| `src/controle_ia/premier_test_ia/empans.py` (égal) | `58043c95…` | en entier |
| `src/controle_ia/harnais/formats.py` (égal) | `98dbfa9b…` | l. 1-110 |
| `src/controle_ia/manifeste.py` | `1a5c7464…` | `graines`, `generateur` (l. 37-55) |
| `src/controle_ia/harnais/validation_reelle.py` | `d25e4cd9…` | l. 83-87 (valeur de `date_string`) ; `git grep` de `FormatChat(` sur `src` |
| `src/controle_ia/scellement.py` | — | en-tête et emplacements d'écriture (pour le sceau) |
| `scripts/repetition_jouet_t07_v1.py` au commit `8dc1cb09` | `7ccd9bbb…` | l. 139-147 (phrases jouets) |
| `tests/test_t07_sondes_neuves_v1.py` au commit `8dc1cb09` | — | l. 84-95 (phrases jouets) |
| `brouillons/T0.7-sondes-v0-v1-brouillon20.md` | `9ef671ac…` | passages : l. 179, 243, 866-876, 992, 1076-1084, 1119-1126, 1374-1380, 1409, 1418-1432, 1822-1828, 2023-2026, 2061, 2448-2490, 2536 (et l'index des mentions par `grep` sur ce fichier nommé) |
| `brouillons/T0.7-sondes-v0-v1-brouillon3.md` | — | une ligne (l. 126 : « proposés : chats, météo, sports, géographie »), trouvée par `git grep` sur ce fichier nommé |
| `docs/decisions/proposition-P-013-T0.7-temoins-pain-axis-v1.md` | `44148087…` (compagnon conforme) | lignes trouvées par `grep` |
| `docs/procedures/consigne-jeux-synthetiques-T0.7-v3.md` | `d9de50a6…` | en entier (modèle de forme) |
| `scripts/verifier_jeux_synthetiques_t07_v2.py` | `e53c9c27…` | l. 142-240 (normalisation, écart relatif, mots interdits, journal) et lignes trouvées (`tokenizers`) |
| `registres/decisions.md` | — | lignes R-168, R-171, R-174, R-184 (trouvées), P-013, R-1655, R-1672 (trouvées), R-2100, R-2101, **R-2102, R-2103, R-2104** (lues après l'avance de `main`) |
| branche `donnees/tokeniseur-llama-3.1-8b-instruct-v1`, commit `03e3cbd9` (référence distante déjà présente dans le clone, aucun `fetch`) | `tokenizer.json` `79e3e522…`, `tokenizer_config.json` `177c7b61…`, `special_tokens_map.json` `6f38c737…` | empreintes par `git show` ; les deux premiers lus en mémoire pour le contrôle de la section 3 ; rien d'écrit sur disque |

**Jamais ouverts** : tout `lecture-sondes-t06.json` ; la lecture B et `donnees/lecture-b-7a-quarantaine-v1` ; tout `diag/`
et `runs/` de 7a ; `essai/t06-explo-v3` ; `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`,
`docs/notes/bras-attaque/` ; l'étiqueteur ; `scripts/extraire_mesures_epreuve_t06_v1.py` ; les textes d'actions de P3 ;
aucun fichier de P3-bis.

**Gestes à déclarer** (noms seulement, jamais de contenu) :
1. `ls donnees/` filtré par `grep -v -E '^(bras-attaque|mode-tenu-a-l-ecart)'` : les noms des entrées du dossier ont été
   listés, les deux préfixes interdits ôtés avant l'affichage ; rien n'a été ouvert.
2. `git ls-tree -r --name-only` sur **toute** la branche du tokeniseur, filtré par `grep -v` (préfixes `diag`, `runs`,
   `donnees/bras-attaque`, `donnees/mode-tenu`, `docs/notes/bras-attaque`) puis par `grep -i -E 'token|special'` : seuls
   des noms de fichiers liés au tokeniseur ont été affichés ; aucun chemin interdit n'a été affiché ni ouvert. **Le geste
   aurait dû borner `ls-tree` au dossier `donnees/tokeniseur-llama-3.1-8b-instruct-v1` avant le parcours** (règle 9 :
   l'exclusion était faite après le parcours des noms, non avant) ; déclaré ici.
3. Recherches : `git grep` sur des fichiers nommés ou sur `src` avec exclusions de `diag` et `runs`, `grep` sur des fichiers
   nommés ; aucune recherche récursive sur un dossier qui contient un chemin interdit.
4. Contrôles en mémoire (section 3) : interpréteur du dépôt, `PYTHONPATH=src`, script passé sur l'entrée standard,
   `-B` (aucun fichier `.pyc`), aucun fichier écrit ; seule entrée hors de l'arbre de travail : les blobs du tokeniseur
   par `git show`.
5. **Aucun** appel de modèle ni d'interface externe, aucune dépense, aucun `vastai`, aucune écriture git (ni `fetch`, ni
   index, ni commit). Rien d'écrit hors des deux sorties et de leurs compagnons `.sha256`.

## 2. Choix faits dans la consigne (chacun dit aussi dans la consigne, à sa place)

1. **Accord au module** (mandat) : un seul fichier `donnees/t07-concepts-v1/phrases-concepts-v1.jsonl`, première ligne
   `{"format_lecture": "message_utilisateur"}` ; clés exactes ; quatre concepts ; 64 paires par concept ; `indice` entier
   unique de 1 à 64 ; 8 à 40 jetons ; écart relatif au plus 0,15 en jetons du tokeniseur réel ; contrôle de la borne de
   128 jetons (E-10) ; dernier contrôle par `lire_phrases_concepts(…, min_concepts=4)`.
2. **D-4** : valeur `message_utilisateur` ; pendant la rédaction, le mot de Lazar « (a) go » a été lu par la mère comme
   réponse à D-4 (R-2102, 08:06 UTC) ; la consigne le cite, avec le chemin d'une éventuelle correction.
3. **DS-3 bis** (R-2104, 08:13 UTC) : le commit du module de référence est celui de la ligne `CODE-T07` ; C12 rejoué à ce
   commit s'il diffère de celui de l'assemblage.
4. **Noms des concepts sans accents** (`chats`, `meteo`, `sports`, `geographie`) : aucune forme Unicode ambiguë ; noms de
   directions et clés de graines en ASCII. Les noms de P-013 (b) restent la référence.
5. **Réserve de 8 paires par concept** (72 écrites) et **plancher de 56** : un retrait ne laisse pas de trou dans les
   indices ; sélection mécanique, table des indices écrite.
6. **Remise de l'écrivain** avec `domaine_neutre` et rotation de **huit domaines neutres** (N1 à N8) : côté neutre varié
   et identique pour les quatre directions ; le champ est ôté à l'assemblage. Le fichier final est écrit par le script,
   jamais par l'écrivain, qui ne connaît pas le format de lecture.
7. **Listes remises à l'écrivain** (annexes A et B), écart au brouillon 1 (§ 5, « sans les listes ») et au plan de
   l'inventaire (« la section 5 et les quatre noms seulement ») : précédent de la consigne v3 (§ 0) ; sans elles, les
   renvois et les retraits se multiplieraient. La remise à l'écrivain est extraite **par programme** de la consigne
   scellée, pour qu'on puisse prouver ce qu'il a reçu.
8. **Annexe A étendue** au-delà des catégories du brouillon 1 (affect, tromperie, intention, enjeux, surveillance,
   évaluation, intelligence artificielle) : compétition et résultat, argent et coût, vocabulaire des actions de l'agent
   (`action`, `control`, `prediction`, `estimate`, `hour`, `proposal`, `baseline`…), dommage et catastrophes, adresse et
   personne. Raison : une direction de « sports » ou de « météo » qui porterait la victoire, l'argent, le danger ou le
   vocabulaire des actions lues pourrait toucher les concepts de P3 et de T0.7 ; le témoin doit en être loin.
9. **Annexe B en deux parties** (noyau exigé, champ permis dans le seul concept) et **lexiques deux à deux disjoints** :
   une phrase d'un concept ne porte aucun mot d'un autre ; la phrase neutre aucun mot d'aucun.
10. **Aucun chiffre** dans les phrases ; **ASCII seulement** ; **une seule phrase** finie par un point.
11. **Quasi-doublons** : distance d'édition en mots au plus 1 entre deux phrases quelconques (généralise « à un mot près »
    du brouillon 1) ; exemples non repris (distance au plus 2, ou suite commune de 6 mots).
12. **Contrôle C4** : rejeu du chemin exact du module (`jetons_message_utilisateur` et `_ids`) avec le tokeniseur réel ;
    identité des comptes entre `tokenizers` et `transformers`.
13. **Contre-vérification** : 7 paires sur 64 par concept (⌈n/10⌉), entropie neuve, clé hors de vue et empreinte consignée
    avant le lecteur ; cinq questions fermées ; acceptation à au moins 6 conformes sur 7 et aucun « oui » à la question de
    l'affect et des sujets interdits, qui déclenche un second passage complet sur ce seul point ; aucun fichier de P3-bis
    donné, déclaré par le lecteur.
14. **Acceptation mécanique et ligne écrite dans la session de l'acceptation**, transposée de l'écrit (a) 2 des jeux.
15. **Aucun contrôle de recopie contre les textes de P3 ou de T0.6** : ces textes ne sont donnés ni à l'écrivain ni au
    script ; les sujets des phrases en sont disjoints et les listes couvrent le vocabulaire des actions.

## 3. Contrôle des annexes et des exemples (en mémoire, avant la remise)

Fait à 08:12 UTC environ, sur la consigne telle qu'écrite (blocs `format-lecture`, `annexe-a`, `annexe-b`, `exemples`
relus par programme), sans rien écrire. **Ce n'est pas le contrôle officiel** : le script de la section 6 le refera (cas
sain de C0) ; le gabarit a été rendu ici par `jinja2` (bac à sable) depuis `tokenizer_config.json`, non par
`transformers`.

- Annexe A : 776 entrées en sept catégories (A1 166, A2 148, A3 123, A4 100, A5 96, A6 127, A7 16), toutes de la forme
  `[a-z]+( [a-z]+)*`, sans doublon. Annexe B : formes par concept et partie — `chats` 32 + 29, `meteo` 62 + 24, `sports`
  89 + 16, `geographie` 84 + 27 ; sans doublon ; **A ∩ B vide** ; quatre lexiques **deux à deux disjoints**.
- `exiger_concept_sans_affect` accepte `chats`, `meteo`, `sports`, `geographie`.
- Huit paires d'exemple : toutes conformes aux règles C2, C3, C5, C6, C7, C8 (entre elles) et à l'identité du gabarit ;
  longueurs en jetons (tokeniseur `79e3e522…`) : E1 18/17, E2 16/16, E3 15/14, E4 18/18, E5 17/17, E6 18/17, E7 16/16,
  E8 17/18 ; écart relatif maximal 0,067 ; mots 13 à 16 ; distance d'édition en mots dans la paire de 4 à 11 ; aucun
  quasi-doublon entre exemples.

## 4. Points ouverts (pour la contre-lecture R2 et la mère)

1. **Listes remises à l'écrivain** et section 5 + annexes au lieu de « la section 5 et les quatre noms seulement »
   (choix 7) : à confirmer par la mère.
2. **Ampleur de l'annexe A** (776 entrées) : plus de renvois possibles ; certains mots communs sont refusés (`lie`,
   `goal`, `training`, `watch`, `title`, `hours`, `control`, `lost`, `felt`, `comfortable`) ; la réserve de 8 paires et le
   plancher de 56 sont faits pour l'absorber. À juger par le contre-lecteur.
3. **Seuils sans étalonnage** : 8 et 40 jetons, 0,15, distances 1 et 2, suite de 6 mots, 56, réserves de C13, 6 sur 7 :
   choix de cette consigne.
4. **Le côté neutre** (huit domaines d'objets courants) donne aux quatre directions une part commune ; réserve 2 de la
   consigne.
5. **D-4** : prise sur un mot bref de Lazar lu par la mère (R-2102) ; si Lazar le corrige, la section 2 dit la marche.
6. **Commit du module** : `8dc1cb09` ; la ligne `CODE-T07` (R-2104) peut en citer un autre ; C12 rejoué alors.
7. **Contre-lecture courte du script** (section 9, étape 2) : ajoutée par analogie avec D-5 des jeux ; à confirmer.
8. **Geste de parcours** déclaré en section 1, point 2 (`ls-tree -r` non borné, filtré après coup) : rien d'interdit n'a
   été affiché ni ouvert ; porté à la mère pour tenue.

## 5. Refus rencontrés

Aucun refus de permission ni de classifieur pendant ce travail.
