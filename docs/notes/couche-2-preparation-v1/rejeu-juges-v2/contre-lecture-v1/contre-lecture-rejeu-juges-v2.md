# Contre-lecture R2 — rejeu v2 des juges (cellule « verdict-echelles », GO-2026-10-29-04)

Contre-lecteur neuf (sous-agent), auteur ni du code ni de la fiche. Début 29 octobre 2026, 07:24:06 UTC ; fin 08:21:02 UTC.
Aucune instance, aucune clé, aucun réseau payant. Le dépôt n'a pas été modifié : tout s'est fait sur des copies.

## Verdict

**Lançable après corrections.** Aucun constat bloquant. Un constat majeur (CLR2-01) : le lanceur ne vérifie pas que
le code lancé est bien celui que cite la fiche. Il se corrige en une ligne, ou par un contrôle à la main avant le
lancement. Les autres constats sont mineurs : formulation, précision, marges.

Ce qui est démontré en exécutant :
- suite ciblée : **219 réussis**, le nombre cité par la fiche ;
- lecture par le cache égale aux passes complètes, avec le **vrai tokeniseur** de Llama 3.1 ;
- garde d'encodage **réussie sur le vrai tokeniseur** du 8B (94 sur 94 valeurs) ;
- chaîne de l'instance en jouet de bout en bout ;
- lanceur devant un faux `vastai`, sur le cas sain et sur dix cas de refus ;
- devis : pire cas sous 4 USD.

## Brouillon relu (empreintes sha256, commit `cff3d90a`)

| fichier | sha256 |
|---|---|
| src/controle_ia/environnements/noter_rejeu_juges_v2.py | `8e12764194f3707b2b12bf3d9e0b9021e1d89b9bb88eb4bde958f7cb033da90c` |
| tests/test_noter_rejeu_juges_v2.py | `fee1cbb3ed6e4999c89420c5f17f1ab2d85ffec205c136e4604c98be9c53e0fa` |
| …/rejeu-juges-v2/config-rejeu-juges-v2.json | `52ef2a51d15e2f6dab48080c6988167375969da46fa53b3693f86e3dc85738df` |
| …/rejeu-juges-v2/devis-rejeu-juges-v2.md | `0f3f95322f6c7b86fef673a3adcc6fa0be1e678679e942791294b2e70cf138bf` |
| …/rejeu-juges-v2/fiche-lancement-rejeu-juges-v2.md | `325753691a973c872c609d837d426f78736967274b8c78475d6ed379ed6bba65` |
| scripts/rejeu_juges_instance_v2.sh | `2eb142e16414f1cca098cac61e36c594620cc2c069d2c335ee197a5bceb6f6d6` |
| scripts/amorce_rejeu_juges_v2.sh | `781a04b932b97254889a8f6cb16b11931a2b3bd865d2c6f30b00c5810829ccd0` |
| docs/procedures/rejeu-juges-v2/lancer_rejeu_juges_v2.sh | `b6b271ac61c9d902b783a2f8e4edb9ac42e19ef1c105ad0b8e79708f5ebf2da5` |

Ces empreintes sont aussi dans `empreintes-brouillon-relu.txt`. Le clone superficiel relu est au commit `aea6ab4`, qui
contient `cff3d90a`. Les huit fichiers y sont identiques (`sha256sum -c` : OK).

## Réponses aux sept questions

### 1. Tests (démontré)

- `pytest -q tests/test_noter_rejeu_juges_v2.py` : **45 passed in 44.71s**.
- Suite ciblée du script de l'instance (7 fichiers) : **219 passed in 632.02s (0:10:32)**.
  Le compte est égal à « Tests attendus : `219` ».
- La dernière ligne passe l'expression du script de l'instance.
- Aucun test n'est sauté selon la carte : aucun `skipif`, aucune condition sur `cuda` dans les 7 fichiers.
- Durée prévue sur l'instance : environ 18 minutes (INFÉRÉ). Calcul : la v1 a fait 174 tests en 993 s sur l'instance,
  et le même lot prend environ 590 s ici, soit un rapport d'environ 1,7.

### 2. La métrique « fini et appuyé »

**Même définition dans la fiche et dans le code.** La fiche (section « Métrique ») et `lire_par_probabilite_v2`
posent les mêmes conditions :
- les dix critères présents dans le bloc ;
- une valeur écrite à chaque position ;
- une masse M ≥ 0,5 à chaque position.

La masse M se calcule ainsi :
- c'est P(suite de jetons de la valeur, depuis le jeton de décision) × P(jeton terminal), sommée sur les valeurs admises ;
- un jeton terminal contient seulement des espaces et au moins un saut de ligne, ou c'est une fin de tour.

Le code ajoute deux échecs de l'instrument : « aucun jeton ne porte la valeur » et « log-probabilité non finie ». La
fiche les compte à part (« lectures en échec ») : c'est cohérent.

**Comparabilité avec la v1.** Sur un même texte, M v2 ≤ M v1, pour chaque critère :
- v2 multiplie par la probabilité d'une fin de ligne ;
- v2 multiplie par P(espace) pour les critères positifs ;
- v2 ne lit plus les jetons de tête (« 2.5 », « 10 », « 4 » sur [0, 3]).

Le k de la v2 ne se compare donc pas au 157 de la v1 comme une amélioration ou une dégradation de l'instrument. La
mesure est plus stricte, et la consigne a changé. Voir CLR2-05.

**Les chiffres de la v1 cités par la fiche sont exacts.** Je les ai vérifiés sur `lecture-rejeu-v1.json`, empreinte
`63b28eaf…` recalculée :
- 157 sur 180, et 107 sur 120 textes ;
- 21 notes écrites non admises : 19 « 4 hors de [0, 3] » et 8 non entières (6 + 1 + 1) ;
- 137 finis à la note écrite ;
- accord 0,737 ;
- 3B : 115.

**Choix 4 (l'espace comprise dans la masse) : justifié, sans échec artificiel mesurable.**
- Sur les textes réels de la v1 (cellule 8B, 172 blocs complets), **1 720 lignes sur 1 720** ont une espace après les
  deux-points. Pour le 3B aussi, 1 720 sur 1 720. Formes du 8B : « 9 » 1 638 fois, « -9 » 63, « 9 » suivi d'espaces 10,
  « 9.9 » 8, « -9.9 » 1. Outil : `outils/formes_v1.py`.
- Avec le vrai tokeniseur, l'espace est le jeton « ␣ » seul, sans autre découpage possible : « ␣2 » et « ␣10 »
  n'existent pas fusionnés, et « 10 » est un jeton à part.
- Inclure l'espace ne pénalise donc que les autres écritures réelles (« ␣** », « ␣- » sur une échelle positive), que la
  lecture écrite stricte refuse aussi.
- Ce choix rend aussi la v2 cohérente. En v1, l'espace comptait déjà pour les pénalités, où « ␣- » et « ␣ » divergent
  au premier jeton, mais pas pour les critères positifs.

Mesure sur un juge simulé (`outils/choix4_espace.py`), masse minimale sur les dix positions :

| P(espace après « : ») | masse v1 | masse v2 | appuyé v1 / v2 |
|---|---|---|---|
| 0,9992 | 0,6215 | 0,6205 | oui / oui |
| 0,9812 | 0,6215 | 0,6094 | oui / oui |
| 0,8802 | 0,6215 | 0,5466 | oui / oui |
| 0,6221 | 0,6215 | 0,3864 | oui / non |
| 0,3774 | 0,6215 | 0,2344 | oui / non |

L'effet n'existe que si le juge écrit autre chose qu'une espace dans plus d'environ 10 à 40 % des cas. Rien de tel en
v1.

### 3. Lecture par le cache rogné puis prolongé (démontré)

Outil : `outils/cache_contre_passes_completes.py`.
- **Banc** : un modèle jouet de type Llama (bibliothèque transformers 5.18, vrai `DynamicCache`, `crop` négatif). Il a
  le vocabulaire du **vrai tokeniseur de Llama 3.1** : 128 256 jetons, empreinte `79e3e522…`, égale à celle consignée
  en R-067.
- **Graines** : trois.
- **Cinq textes** :
  - forme à échelle ;
  - forme v1 ;
  - demi-point, gras, « 10 », valeur sans espace et espaces de fin ;
  - pénalités à -2, en dernière ligne ;
  - préambule et puces.
- **Référence** : une passe complète sans cache par valeur.
- **Résultat** : égalité partout. Écart relatif maximal 1,2e-5 en simple précision. 38 à 40 passes par notation.

**En bfloat16, la précision du réel, l'égalité n'est plus à 1e-4** (`outils/bf16_cache.py`). Écarts de log-masse :
- 5e-4 avec des logits peu contrastés ;
- 1,1e-2 avec un contraste modéré ;
- 0,16 avec des logits très contrastés.

Les probabilités renormalisées restent à moins de 1,5e-3. Voir CLR2-04.

**Gardes d'arrêt (R5).** La suite de l'auteur éprouve :
- « cache absent » ;
- le rognage impossible (au-delà de la longueur, et à 0) ;
- le prolongement d'un cache d'une autre longueur ;
- la lecture sans jeton terminal.

J'ai ajouté cinq artefacts pour les gardes qu'elle n'éprouve pas (`outils/test_gardes_complementaires_v2.py`,
**5 passed**) :
- passe principale qui rend un cache de longueur fausse ;
- passe principale qui rend des lignes manquantes ;
- prolongement qui rend une longueur fausse ;
- lecture sans contexte ;
- lot vide ou graines en nombre faux ;
- encodage du 3B rechargé hors ligne différent (arrêt avant toute phase, `arret.json` à phases vides).

Chaque garde arrête sur son artefact et laisse passer le cas sain.

### 4. Garde d'encodage devant le vrai tokeniseur (démontré pour le 8B)

Outil : `outils/garde_encodage_vrai_tokeniseur.py`.

Fichiers de tokeniseur, données seules, sans code distant :
- 8B : `tokenizer.json`, empreinte `79e3e522635f…`, **égale au vrai tokeniseur de la révision `0e9e39f2` (R-067)** ;
- 3B : copie publique `unsloth/Llama-3.2-3B-Instruct`, empreinte `6b9e4e7f…`, **non vérifiée** contre la révision
  `0cb88a4f`.

Résultats :
- `controler_encodage_v2` **réussit pour les deux** : 47 valeurs (garde de v1), 94 valeurs (deux formes), sondes
  `X: -1` → [(2,4),(4,5)] et `X: 0` → [(2,3),(3,4)] ;
- 204 jetons terminaux, dont « \n », « \n\n », « ␣\n », « \r\n » ;
- 2 257 jetons portent un saut de ligne ;
- consigne v2 : 244 jetons ; bloc à échelles : 128 jetons (le devis supposait environ 130).
- Découpages réels :
  - `BALANCE (0 to 3): 2\n` → … `):`, `␣`, `2`, `\n` ;
  - `REDUNDANCY_PENALTY (-2 to 0): -1\n` → … `):`, `␣-`, `1`, `\n`.

Si un tokeniseur découpait autrement :
- la garde arrête à l'étape « contrôle de l'encodage des valeurs » ;
- c'est après le manifeste, le chargement du 8B et le contrôle du format, **avant** le préchargement du 3B et avant
  toute phase ;
- `arret.json` est scellé et poussé (essai `test_encodage_different_arrete_avant_toute_phase`, plus mon artefact pour
  le 3B rechargé).

**Coût perdu au pire** : démarrage, mise en place, suite ciblée et chargement du 8B (≈ 25 minutes, ≈ 0,5 à 0,6 USD à
1,25–1,43 USD/h), plus le téléchargement (≈ 0,1 à 0,2 USD), plus l'attente de l'arrêt par la session. Total ≈ 0,8 USD.
Ce risque est maintenant faible pour le 8B. Voir CLR2-06.

### 5. Banc de la chaîne et du lanceur (démontré, journaux dans `journaux-banc/`)

**Chaîne de l'instance en jouet** :
- **Dépôt distant simulé** : un dépôt nu local, avec un pilote jouet arrêté et des notations jouet construits par
  `outils/construire_jouet_v2.py`.
- **Moyens** : vraie amorce v2, vrai script de l'instance, `MODE=jouet`, `PREREG_ABSENT=1`, `SAUTER_TESTS=1`.

| cas | issue |
|---|---|
| A sain | code 0. Deux phases écrites (8B décisive, 3B descriptive). Branche `calcul/rejeu-juges-v2` poussée : résultats scellés, puis traces. `--lire` écrit `lecture-rejeu-v2.json` scellé ; `lecture_decisive` renseignée. |
| B branche existante | code 2 : « déjà présente sur le dépôt distant : arrêt avant l'installation (R12) ». |
| C TERM pendant le run | TERM envoyé **par PID** au `timeout` de l'amorce après le lot 1/2 (`outils/banc_term.sh`). Code 124. `arret.json` scellé (« signal TERM reçu… », phase 8B « en cours », 1 lot fait), commité et poussé. |
| D temps insuffisant | plafond 50 min : « 36 minutes < 45 : le run ne commence pas ». Code 1. Arrêt consigné, branche poussée. |
| E fiche non scellée | code 2 : « fiche ou son sceau absent : arrêt avant l'installation ». |
| E2 fiche scellée à marqueur | code 2 : « marqueur restant : arrêt avant l'installation ». |

**Lanceur devant un faux `vastai` 1.8.3** (`outils/faux_vastai`, `outils/banc_lanceur.sh`). Huit offres
factices :

| cas | issue |
|---|---|
| sain | code 0. Garde de calcul : GO-2026-10-29-04 accepté. Offre **107** choisie (1,25 USD/h), la moins chère des offres conformes. Écartées : fiabilité 0,90 ; CUDA 12.8 ; 32 Go de mémoire vive ; téléchargement 0,02 ; A100 PCIE ; 1,50 USD/h. `arret_au_plus_tard` = création + 8 400 s ; réveils à + 7 800 et + 8 700 s. `DEPOT_URL=…controle-ia-travail.git` passé par `--env` ; jetons masqués dans le journal. |
| GO absent de `go.md` | code 2, aucune création. |
| GO hors de sa période | code 2, aucune création. |
| autre instance sur le compte | code 2, aucune création. |
| crédit 4,20 USD | code 3, aucune création. |
| toutes offres au-dessus du plafond | code 3, « aucune offre conforme », aucune création. |
| jeton absent | code 2, aucune création. |
| fiche à marqueur (commit E2) | code 2, aucune création. |
| commit absent de `origin/main` | code 2, aucune création. |
| dossier de traces existant | code 2 (R12), aucune création. |
| branche de résultats présente | code 2, aucune création. |
| réponse de création illisible | code 4. Réponse masquée (« Erreur *** inattendue »). |

### 6. Critères gelés, liste d'arrêt, bornes, R9, R12

**Citations reprises de la v1.** Elles sont textuellement égales à celles de la fiche v1 : 15 intitulés. Le sceau de
la fiche v1 est conforme (`7b6b89d9…`). J'ai recalculé :
- épisodes `45616303…` ;
- notations du 8B `b103835b…` ;
- notations du 3B `51548526…` ;
- configuration v2 `186220d4…` (`empreinte_config`) ;
- consigne v2 `9bb0af34…`.

Tous sont exacts. Je n'ai pas relu les fichiers de `runs/` ni de `donnees/` (manifestes, tâches), par prudence sur
l'interdit. Le `sha256sum -c` de la session reste à faire. Chaque citation n'apparaît qu'une fois (8 intitulés, plus 2
notations).

**Critères et code concordent** :
- seuils 0,99, 0,5, 0,02 et 0,90 ;
- H_A si k ≥ 179 sur 180 ; H_B tranchée si k0 ≤ 116, vérifié par Wilson : 116 donne une borne haute de 0,987, 117
  donne 0,991 ;
- graines de l'audit `audit-r4/8B/verdict-echelles` ;
- 360 clés de graines, plus `modele-jouet`, clés distinctes par juge ;
- R9 par `SeedSequence` (code de la v1) ;
- R12 : run, dossier, branche, sceau et lecture jamais écrasés (cas B et essai R12).

**Lecture sans décision après coup.** La fiche le permet. `--lire` applique tout. Une cellule non écrite se lit
« non mesurée », et toute relance demande un nouveau GO, sauf la perte par l'hôte avant la première ligne `PROGRES`.

**Écarts de forme** : CLR2-03 (formulation de la borne des 45 minutes) et CLR2-07 (seconde instance).

**Bornes de temps cohérentes avec le code** :
- module : min(3 300 s, délai externe moins 6 min) ;
- phases 2 100 s et 1 200 s, chacune lancée seulement si le temps restant la couvre ;
- délai externe : min(65 min, temps restant moins 13 min) ;
- minimum 45 min ;
- amorce 120 min, puis KILL 5 min plus tard.

Le 3B ne tourne que si le 8B finit en moins d'environ 31 minutes. Voir CLR2-02.

### 7. Devis

| prix (USD/h) | pire facturé (140 min) | avec téléchargement et disque (≤ 0,32) | session perdue (147 min) |
|---|---|---|---|
| 1,00 | 2,33 | 2,65 | 2,77 |
| 1,25 | 2,92 | 3,24 | 3,38 |
| 1,40 | 3,27 | 3,59 | 3,75 |
| 1,43 (plafond) | 3,34 | 3,66 | 3,82 |

**La facture tient sous 4 USD au pire**, même au plafond du lanceur.

Rythmes réels de la v1 (journal de l'instance, branche `calcul/rejeu-juges-v1`) :
- démarrage jusqu'à la fin des tests ≈ 22 minutes ;
- chargements ≈ 1 minute.

Mon estimation pour la v2 (INFÉRÉE) : mise en place ≈ 23 min, chargements 1 à 2, 8B ≈ 18, 3B ≈ 11, poussées 2,
démarrage 3, arrêt par la session ≈ 5. Total ≈ 65 min, soit **≈ 1,4 à 1,7 USD** (devis : ≈ 1,5).

## Constats

**CLR2-01 — majeur — Le lanceur ne vérifie pas que l'arbre gelé du commit lancé est celui du commit du code cité.**
- **Ce que fait le module.** Au début du run, `exiger_code_cite` compare le commit du code cité à HEAD sur `CHEMINS_GELES`
  (`git diff --quiet CODE HEAD`). Cet arbre couvre tout sauf `docs`, `prereg`, `registres`, `diag`, `runs`, `donnees`,
  `traces`… : `src`, `tests`, `scripts`, `.claude`, `requirements*` y sont.
- **Ce que fait le lanceur.** Il vérifie seulement l'ascendance (`merge-base --is-ancestor`).
- **Le risque.** Plusieurs sessions committent sur `main` en même temps. HEAD a bougé trois fois pendant cette
  relecture : `cff3d90a`, `aea6ab4`, `6bad671a`. Si une autre session committe du code entre le commit du code et le
  commit de scellement, le run s'arrête au début, après ≈ 25 minutes payées (≈ 0,6 à 0,8 USD). Le nombre de tests peut
  aussi changer et arrêter plus tôt.
- **Correction.** Dans le lanceur, juste après le contrôle d'ascendance :
  `git -C "$T/clone" diff --quiet "$CODE" "$S" -- . ':(exclude)prereg' ':(exclude)brouillons' ':(exclude)registres' ':(exclude)docs' ':(exclude)diag' ':(exclude)runs' ':(exclude)donnees' ':(exclude)livrables' ':(exclude)papiers' ':(exclude)traces' ':(exclude)CLAUDE.md' || { echo "arbre gelé modifié depuis le commit du code"; exit 2; }`
  Ou la même commande à la main, consignée dans `lancement.txt`. Puis rejouer le cas sain du lanceur.

**CLR2-02 — mineur — La phase décisive est « tout ou rien » à 35 minutes, sur un rythme jamais mesuré.**
- **Le constat.** Si le 8B dépasse 2 100 s, aucun fichier n'est écrit et la cellule décisive est perdue (≈ 1,3 USD
  dépensés). Or, dans ce cas, le 3B ne pourrait pas tourner non plus (il faudrait 35 + 20 + 4 = 59 > 55 min). La borne
  de 35 minutes ne protège donc rien.
- **Le risque.** Faible. Le pire supposé est de 30 minutes, mais la lecture des branches par le cache n'a jamais été
  chronométrée sur l'A100.
- **Correction (au choix de la session)** :
  - porter `duree_max_s` du 8B à 2 400 s et `DELAI_RUN_MIN` à 50, sans effet sur l'attendu ni sur le pire facturé ;
  - ou garder 2 100 s et l'écrire comme risque accepté.

**CLR2-03 — mineur — Une formulation inexacte sur la borne des 45 minutes.**
- **Le constat.** La liste d'arrêt de la fiche (« Chaîne de l'instance ») et le devis § 4 disent « temps restant
  avant le plafond de l'amorce sous 45 minutes ». La règle codée porte sur le délai du run, qui vaut le temps restant
  moins 13 minutes : le run ne commence pas s'il reste moins de 58 minutes avant le plafond. La section « Bornes de
  temps » de la fiche le dit juste.
- **Correction.** Reprendre la formule de « Bornes de temps » dans les deux endroits.

**CLR2-04 — mineur — La précision « à 1e-4 près » ne vaut qu'en simple précision.**
- **Le constat.** Au réel (bfloat16), la lecture mêle deux chemins numériques : la passe principale pour les valeurs
  du chemin écrit, le cache prolongé pour les autres. Sur le jouet, l'écart va jusqu'à 1e-2 de log-masse pour un
  contraste modéré.
- **L'effet.** Aucun sur la définition. Effet possible sur une masse à la limite de 0,5.
- **Correction.** Écrire dans la fiche (« Métrique ») : « égalité vérifiée en simple précision ; au réel, écart
  numérique de l'ordre du pour cent, sans correction ».

**CLR2-05 — mineur — La comparabilité avec la v1 n'est pas dite en toutes lettres.**
- **Correction.** Ajouter une phrase dans « Prédiction » ou « Critères » : « sur un même texte, M v2 ≤ M v1 (fin de
  ligne exigée, espace comptée, jetons de tête retirés) ; aucune différence de k entre v1 et v2 ne se lit comme un
  effet de l'instrument ou de la consigne ». Ajouter aussi la justification mesurée du choix 4 (1 720 lignes sur
  1 720 avec espace en v1).

**CLR2-06 — mineur — La fiche et le devis disent la garde d'encodage éprouvée « sur un tokeniseur simulé ».**
- **Le constat.** Elle est maintenant éprouvée sur le vrai tokeniseur du 8B (empreinte R-067) et sur une copie du 3B
  (empreinte non vérifiée) : 94 sur 94, 204 terminaux.
- **Correction.** Consigner ce résultat et ses empreintes.
- **Facultatif.** Exécuter `controler_encodage_v2` sur les deux tokeniseurs avant la suite de tests de l'instance :
  les tokeniseurs sont petits. Un échec coûterait alors ≈ 3 minutes au lieu de ≈ 25.

**CLR2-07 — mineur — La règle de la seconde instance est floue en pratique.**
- **Le constat.** Le devis permet une seconde instance si la première est perdue avant la première ligne `PROGRES`
  « et si le cumul reste sous 4 USD ». Avec un pire cas de 3,7 à 3,8 USD par instance, il faut que la première ait
  coûté au plus ≈ 0,2 USD, soit moins de ≈ 8 minutes de vie.
- **Correction.** L'écrire en chiffres (« première ≤ 0,20 USD, sinon nouveau GO »), ou donner à la seconde un plafond
  d'amorce réduit.

**CLR2-08 — mineur — Des gardes du module ne sont éprouvées par aucun essai sur artefact (R5).**
- **Le constat.** Cinq gardes sont dans ce cas (liste au § 3). Elles tiennent toutes (`outils/test_gardes_complementaires_v2.py`,
  5 réussis).
- **Correction.** Verser ces essais dans `tests/test_noter_rejeu_juges_v2.py`. Les « Tests attendus » passeraient
  alors à 224 : recompter.

**CLR2-09 — mineur — Le premier réveil de garde (+ 130 min) tombe sur la fin au pire de l'amorce.**
- **Le constat.** Cette fin au pire vaut démarrage ≤ 5 + 120 + KILL 5 = 130 min. Un réveil qui détruit l'instance à
  cet instant peut couper la poussée des résultats partiels de la branche KILL. La v1 avait la même marge.
- **Correction.** Avant de détruire, le réveil lit la fin du journal (« AMORCE … fin »). Ou bien premier réveil à
  + 135 min (pire facturé inchangé : 3,82 USD au second réveil).

## Ce que je n'ai pas pu vérifier

- Les rythmes réels de la v2 sur A100 : lecture des branches par le cache, génération bornée, pic de mémoire.
- Le tokeniseur du 3B à sa révision exacte : la copie publique a l'empreinte `6b9e4e7f…`, non comparée à
  `0cb88a4f`.
- Le comportement de `DynamicCache.crop` et du prolongement en bfloat16 sur carte avec `sdpa`. Je l'ai éprouvé seulement
  sur processeur : float32 et bfloat16.
- Les empreintes des fichiers de `runs/` et de `donnees/` (manifestes, tâches), non relus par prudence sur
  l'interdit. Elles sont égales à celles de la fiche v1 scellée, et le module les contrôle avant le manifeste.
- La chaîne en mode réel : téléchargements, `requirements-gpu.txt`, vrai GitHub. Le cas KILL de l'amorce (code 137)
  n'est pas rejoué.
- La facturation réelle du disque et du téléchargement par Vast.ai (supposée ≤ 0,32 USD comme au devis).

## À faire par la session avant le lancement (rappel, sans constat)

1. Remplir le commit du code et la section « Contre-lecture » : empreinte du brouillon relu (tableau ci-dessus),
   chemin et empreinte de ce rapport. Retirer « À REMPLIR ». `prereg.problemes` exige les deux empreintes dans cette
   section.
2. Sceller la fiche, le devis, la configuration et `lancer_rejeu_juges_v2.sh`. `verifier-arbre` signale aujourd'hui
   4 fichiers sans empreinte compagnon. Puis recompter les tests après les corrections.
3. Faire `sha256sum -c` sur les fichiers de `runs/` et de `donnees/` cités, puis appliquer CLR2-01.

## Fichiers produits

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/relecture-rejeu-v2/`.
- `contre-lecture-rejeu-juges-v2.md` (ce rapport) ; `empreintes-brouillon-relu.txt`.
- `outils/` :
  - `garde_encodage_vrai_tokeniseur.py`, `cache_contre_passes_completes.py`, `bf16_cache.py` ;
  - `choix4_espace.py`, `formes_v1.py`, `test_gardes_complementaires_v2.py` ;
  - `construire_jouet_v2.py`, `banc_amorce.sh`, `banc_term.sh`, `banc_lanceur.sh`, `faux_vastai`.
- `journaux-banc/` : `banc-A…E2.log`, `lanceur-*.log`, `vastai-*.log`, `lancement-sain.txt`, `offres-factices.json`.
- `tok-llama31/`, `tok-llama32/` : fichiers de tokeniseur téléchargés, données seules.
- `v1-bruts/` : résultats bruts de la v1 extraits de `origin/calcul/rejeu-juges-v1`, hors traces.
- Les clones lourds du banc (copie, source, dépôt nu) ont été supprimés après usage : le disque était plein.
