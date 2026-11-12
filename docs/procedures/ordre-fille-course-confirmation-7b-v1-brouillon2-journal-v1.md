# Journal du rédacteur — ordre de la course de confirmation 7b de T0.6, brouillon 2 — v1

- **Qui** : le rédacteur du brouillon 1 (sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, Claude Opus 5.5), sur la suite de mission envoyée par la mère après R-2087.
- **Quand** (`date -u`, 10 novembre 2026) : 07:12:03 (relevé avant la rédaction) ; 07:16:37 (avant la réécriture serrée) ; 07:23:54 (après les coupes, avant ce journal) ; heure de scellement : compte rendu à la mère.
- **Dépôt** : `main` à `142505c3` au début de la reprise (brouillon 1 versé à `fe24698d`, R-2087). Les deux seules écritures : le brouillon 2 et ce journal, plus leurs compagnons de scellement ; le brouillon 1 et son journal restent tels quels (R12).
- **Interdits** : interdits communs **v2** (`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md`, `1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`, vérifiés, lus en entier ; règle 9 neuve) ; un écart de forme à la règle 9, déclaré au § 4.

## 1. Décisions de la mère appliquées

| Point | Décision | Où dans le brouillon 2 |
|---|---|---|
| 1. Étape A de T0.7 | instance gardée arrêtée si `GO-ETAPE-A-T07` et le scellement de T0.7 sont inscrits au registre de `main` à la fin de la course, sinon détruite ; au plus tard le 16 à 23:00Z ; ordre d'exécution séparé cité par marqueur, non écrit | § 4.13 (vérification unique, commandes), § 4.14, § 9 (pas de `start` sous cet ordre), § 14 (marqueur `EMPREINTE_ORDRE_EXECUTION_ETAPE_A_T07`) |
| 2. Forme d'exécution | gardée de 7a, point à juger | § 4.10, § 13 point 1 |
| 3. Clonage de toutes les branches par l'amorce | accès mécanique connu, sans lecture ni affichage (R-2087) | § 2 point 6 |
| 4. Conditions de GO-2026-11-07-04 | vérifiées en lecture seule ; addendum v3 non scellé : aucune création avant un mot de Lazar | § 3 P7, § 4.3, § 7, § 14 |
| 5. Registre des scellements | marqueur gardé ; créé par la mère au scellement de T0.7 | § 4.3, § 14 |
| 6. Longueur | moins de 45 Ko, sans retirer une garde | 44 976 octets (contre 65 403 au brouillon 1) |

## 2. Vérification des conditions du bras B (lecture seule, `git grep` avec exclusions ou fichiers nommés)

- Commandes : `git grep -n -i "bras B v4\|bras_b_v4" -- registres/decisions.md` ; `git grep -n -i "addendum" -- registres/decisions.md` ; `git grep -n "1a372523" -- . ':(exclude)docs/notes/bras-attaque' ':(exclude)scripts/extraire_mesures_epreuve_t06_v1.py' ':(exclude)diag' ':(exclude)runs'` ; `git grep -n -l … -- registres docs/procedures prereg ':(exclude)docs/notes/bras-attaque'` ; `git grep -n -i "addendum" -- registres/go.md registres/etat.md` ; `grep` sur le seul rapport nommé de la contre-lecture de la chaîne v12 ; `git show --stat fe240b24` et `git show fe240b24:<addendum après couples>` (en-tête seulement).
- **Code et essais du bras B v4 contre-lus : rempli.** R-1761 (rendu du bras B v4 : `317a7ea5…`, 44 essais, banc 21 sur 21 ; « addendum non contre-lu ») ; R-1781 (contre-lecture neuve de la chaîne de la course) ; rapport `docs/notes/g0-deux-semaines-v1/contre-lecture-t06-course-v2/contre-lecture-t06-course-v2-v1.md`, `09c202e62d4cd4d9af2c0100183ac9cffb90387025d784a81eeeb1df57d13a02` (compagnon conforme) : verdict « scellable » pour la chaîne v12 (qui joue `bras_b_v4` par défaut), § 2 « Bras B v4 conforme à GO-2026-11-08-01 » (l. 107 à 116 : tolérance 0,3 borne incluse, lecture stricte, 44 essais rejoués, banc 21 sur 21).
- **Addendum v3 scellé : non rempli.** Sur `main` : le brouillon `docs/notes/g0-deux-semaines-v1/bras-b-v2/addendum-bras-b-v2-brouillon-v3.md` (`2ec90141…`), jugé « scellable après couples » (1 couple, R-1781, rapport l. 39) ; la copie après couples `addendum-bras-b-v2-brouillon-v3-apres-couples-v1.md` (`1a372523290fdaf0a606db592295885f01ff9d6adc9b877fd72279fc6a44ccdf`, « prêt », R-1784) n'existe que dans le commit `fe240b24` (branche `prep/scellement-course-t06-v1`, non ancêtre de `main`) et son en-tête dit « brouillon v3 … que la session mère scellera avant toute lecture du bras B » ; `git grep 1a372523` ne trouve que R-1784 et une sortie JSON de la contre-lecture ; aucune ligne du registre n'en consigne le scellement. GO-2026-11-07-09 (l. 269) et GO-2026-11-08-01 (l. 272) demandent l'addendum « scellé avant toute lecture » du bras B.
- **Ordre** : cet ordre, contre-lu et scellé avant la remise (à faire).
- **Conséquence écrite** (décision de la mère) : P7 ; la fille ne crée rien sans la ligne de la mère qui consigne le scellement (marqueur `LIGNE_REGISTRE_BRAS_B`, valeur `AUCUNE` sinon) ou sans un mot de Lazar sur ce point dans sa session. **Signalé à la mère.**

## 3. Sources lues pour le brouillon 2 (en plus de celles du journal du brouillon 1, `92fb53e7…`)

| Source | Empreinte | Lignes |
|---|---|---|
| `brouillons/T0.7-sondes-v0-v1-brouillon19.md` | `07039ed28065e835b0c6b5ca150438cd8b3bfb3927833009aaa8b31855c5b1ad` (compagnon conforme) | l. 1446 à 1462 (« Lancement nominal », variante B) ; l. 1905 à 1935 (« Calcul et dépense ») ; recherche de `GO-ETAPE-A-T07` dans ce seul fichier (l. 427, 1248, 1447, 1845, 1955, 2030, 2048, 2069 : forme de la clé, extrait scellé `registres/go-extraits/GO-ETAPE-A-T07-v1.md`) |
| `registres/decisions.md` (tête de `main`) | — | R-1754, R-1761, R-1763, R-1781, R-1784 ; R-2086 (interdits v2) ; R-2087 (décisions de la mère) |
| `registres/go.md` | — | l. 269 (GO-2026-11-07-09), l. 272 (GO-2026-11-08-01) |
| rapport de la contre-lecture de la chaîne v12 | `09c202e6…` | l. 21, 24, 30 à 40, 82, 83, 93, 94, 105 à 116, 125, 133, 139, 158 |
| commit `fe240b24` | — | liste des fichiers ; en-tête de la copie de l'addendum après couples |

## 4. Choix faits, essais, incident

- **Commandes inchangées** depuis le brouillon 1 (vérifiées par `bash -n`, extrait Python par `ast.parse`, motifs d'extraction égaux à ceux de l'amorce, contrôles du § 4.9 éprouvés au brouillon 1 sur une commande simulée), sauf : script `inventaire.sh` écrit au § 4.0 (même commande filtrée, une seule fois) ; variable `L` au § 4.12 ; fichier `ligne-scellement-t07.txt` écrit au § 4.3 pour la comparaison de fin de course ; bloc neuf du § 4.13 (empreinte de l'extrait calculée sur la sortie de `git show`, non sur une variable, pour ne pas perdre la fin de ligne).
- **Étape A** : conditions réduites aux deux lignes que nomme la mère ; vérification faite une seule fois, après une fin normale ; la fille ne redémarre pas l'instance (le redémarrage relève de l'ordre d'exécution de l'étape A) ; destruction au plus tard 2026-11-16T23:00Z dans tous les cas.
- **Contrôle des gardes** : une liste de 58 jetons (seuils, dates, interdits, gardes, commandes) comparée entre les deux brouillons : aucun perdu (un seul, `pkill`, rétabli).
- **Repères de durée** regroupés (distillation ≈ 4 h 20, épisodes ≈ 6 h 50, test croisé et couples ≈ 1 h 46 : lecture A, § 4 et § 7).
- **Écart de forme à la règle 9** (interdits v2) : pour retrouver les fichiers d'addendum, `git ls-files | grep -i "addendum-bras-b"` a parcouru la liste de tous les chemins suivis **sans exclure** `docs/notes/bras-attaque/` (seuls des noms contenant « addendum-bras-b » sont sortis, aucun hors de `docs/notes/g0-deux-semaines-v1/`) ; aucun fichier interdit ouvert ni affiché. Recherches suivantes faites avec `git grep` et exclusions, ou sur des fichiers nommés.
- **Aucun refus** de permission ni de classifieur ; aucun appel externe, aucune dépense, aucune écriture git, aucune lecture de valeur de clé, aucun fichier de sondes, de 7a, du bras d'attaque ou de l'étiqueteur ouvert.

## 5. Points ouverts

1. **Addendum v3 du bras B non scellé** : à sceller par la mère (copie après couples `1a372523…` prête sur `fe240b24`) et à consigner, ou mot de Lazar ; GO-2026-11-07-09 et -08-01 ne l'exigent qu'avant la lecture du bras B (§ 13, point 2).
2. **Ordre d'exécution de l'étape A** (`docs/procedures/ordre-execution-etape-a-t07-v1.md`) et **ligne `GO-ETAPE-A-T07`** : à écrire, contre-lire et sceller (R-2087, point 5 : GO de l'étape A demandé à Lazar ce jour) ; sans eux à la fin de la course, l'instance est détruite.
3. **Forme d'exécution** de la commande de création : à juger par la contre-lecture.
4. **Versions** de `vastai` et de torch chez la fille : vérifiées par elle (P9).
