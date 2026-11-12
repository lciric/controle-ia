# Journal du brouillon 5 de la consigne de l'audit des fuites de T0.7 — v1

Travail commencé le 2026-11-11 à 13:47 UTC, à la réception du message de la mère ; journal écrit à partir de 13:50 UTC
(heures relevées par `date -u`). Auteur : l'agent du brouillon 4 (Claude Opus 5.5, `claude-opus-5-5`), sous-agent de la
session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, sous la même consigne
(`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-audit-fuites-t07-brouillon4-v1.md`,
`df38829a025db0f341b1a919d1c2afbfbd19c4f5c7019b8926483dd0f4cf629d`) et les mêmes interdits. Il suit les décisions de la mère
sur les questions du brouillon 4, consignées en R-2348 (lue dans `registres/decisions.md`). Auteur des brouillons 4 et 5,
cet agent est exclu de la contre-lecture des écarts. Aucun commit, aucune ligne de registre, aucun appel externe, aucune
dépense ; le brouillon 4 scellé n'est pas touché (R12).

## 1. Pièces

| pièce | chemin | sha256 |
|---|---|---|
| brouillon 5 | `brouillons/T0.7-audit-fuites-v1/T0.7-consigne-audit-fuites-v1-brouillon5.md` | `7228ce724d4f2a7c146124ceb70156cf99118b2acebcdc4b3b7d9e5d977d2b67` |
| couples | `…-brouillon5-pieces/couples-brouillon4-vers-brouillon5-v1.json` | `0234c144c969dabeb53fc1252d7bf09ff9b6b443fbd3dedb1b7d63b87aed06b1` |
| script | `…-brouillon5-pieces/appliquer_couples_brouillon5_v1.py` | `9e82b2c374fa617d151f90980c88b2e4c67b3eb44cd045504acbd82321ba6deb` |
| sortie brute du script (`appliquer`, 13:49 UTC) | `…-brouillon5-pieces/sortie-script-v1.txt` | `30f1b42243d9314a72be3c61efd5e8cfd93b514b014271d47c7fccce231b802b` |

`…` = `brouillons/T0.7-audit-fuites-v1/T0.7-consigne-audit-fuites-v1`. Le brouillon 4 est intact
(`f9f4bd380a3066371c88d39ede0ef60bde77070311cd2cd9ca221cf8f3f194c5`, égal à son compagnon).

**Procédé.** Le script charge le script scellé du brouillon 4 après contrôle de son empreinte (`7539b477…`), en réutilise
les fonctions et rejoue ses 19 essais sur jouets, plus un essai propre (texte du découpeur sans marqueur, empreintes
citées, aucun `git archive` prescrit). Il vérifie ensuite l'empreinte du brouillon 4 et de la réception R1 v4, la présence
du commit, du dossier et des trois empreintes dans R-2238, puis recalcule les trois empreintes du découpeur par `git show`
et les compare à R-2238 et aux compagnons du commit (arrêt sinon). Il applique enfin 9 couples, chacun présent une fois,
les défait (brouillon 4 à l'octet exigé) et exige pour seul marqueur restant `<<RAPPORT_CONTRE_LECTURE_2>>`, présent une
fois. Un essai à blanc a précédé ; la sortie réelle lui est égale à l'octet. **Vérification indépendante** (programme
distinct) : couples du JSON appliqués au brouillon 4 → brouillon 5 ; défaits → brouillon 4 ; puis les couples du brouillon
4 défaits → brouillon 3, à l'octet ; chaque « ancien » unique dans le brouillon 4, chaque « nouveau » unique dans le
brouillon 5 ; seul marqueur : `<<RAPPORT_CONTRE_LECTURE_2>>` ; la seule mention de `git archive` est l'interdiction « ni
`git archive` ».

## 2. Découpeur (Q-B4-1, R-2238, R-2348)

- `git cat-file -t c7484c43657a2ce22d76af33efd06aaa11a6aafa` → `commit` (13:47 UTC). `git show <commit>:<dossier>/` liste
  `LISEZMOI.md`, `special_tokens_map.json`, `tokenizer.json`, `tokenizer_config.json` et leurs quatre compagnons
  (`LISEZMOI.md` non lu).
- **Empreintes recalculées en entier par `git show <commit>:<chemin> | sha256sum`**, égales à R-2238, à la réception R1 v4
  (`bb6652f2…`, l. 70-72) et au compagnon de chacune dans le commit (`<hex>  <nom>`) :
  - `tokenizer.json` : `79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4` ;
  - `tokenizer_config.json` : `177c7b61e616fecb84c17ce0591acb92c6c4d60e9ac5ababfb940ff23bbcd424` ;
  - `special_tokens_map.json` : `6f38c73729248f6c127296386e3cdde96e254636cc58b4169d3fd32328d9a8ec`.
- **Procédure de l'auditeur jouée dans mon bac à sable** (13:48 UTC ;
  `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/audit-fuites-b4/essai-decoupeur/decoupeur/`) :
  trois fichiers écrits par `git show <commit>:<chemin> > <dossier>/<fichier>`, trois empreintes égales, puis
  `AutoTokenizer.from_pretrained(<dossier>, local_files_only=True)` hors ligne (`HF_HUB_OFFLINE=1`) : chargé
  (`TokenizersBackend`, `transformers` 5.18.0), aller et retour encodage-décodage exact sur une chaîne courte au format
  d'action. Aucun texte d'action, aucun fichier de `diag/`, `runs/` ou `donnees/` touché.
- **Avertissement relevé au chargement** (information, question Q-B5-1) : `transformers` 5.18.0 écrit « Ignoring
  clean_up_tokenization_spaces=True for BPE tokenizer TokenizersBackend » : le réglage de nettoyage des espaces de
  `tokenizer_config.json` n'est pas appliqué au décodage dans cette version.
- Note sur R-2348 (« clone revenu superficiel ») : à 13:32 et à 13:49 UTC, `git rev-parse --is-shallow-repository` rendait
  `false` ; l'absence venait de la branche de données non récupérée. Sans effet.

## 3. Couples du brouillon 4 au brouillon 5 (9)

| couple | décision | lieu |
|---|---|---|
| D00 | statut | titre : « brouillon 4 » → « brouillon 5 » |
| D01 | statut | statut du brouillon 5 (qui, quand, d'où ; brouillon 5 = brouillon 4 + couples) ; l'ancien statut devient « Brouillon 4 (historique) » |
| D02 | Q-B4-1 | en-tête, marqueurs : `CHEMIN_DECOUPEUR` rempli ; reste `RAPPORT_CONTRE_LECTURE_2` |
| D03 | Q-B4-1 | en-tête, ordre : remplissage du découpeur au brouillon 5, puis contre-lecture, puis scellement |
| D04 | Q-B4-5 | § 4, « Calendrier visé » : T0.7 scellé le 2026-11-11 (R-2321) ; consigne remplie, contre-lue et scellée avant l'audit ; audit relevant de l'étape B, après la poussée vérifiée de 7b, avant l'exécution de l'étape B ; aucune autre date |
| D05 | Q-B4-1 | § 6.1, `CHEMIN_DECOUPEUR` rempli : commit, dossier, branche, trois empreintes ; l'auditeur écrit les trois fichiers par `git show` dans un dossier neuf de son bac à sable, vérifie les empreintes **avant** de charger le découpeur, puis le charge depuis ce dossier ; ni `git archive`, ni `fetch` |
| D06 | Q-B4-2 | § 14.2, objet : différentiel du brouillon 2 au brouillon 5 |
| D07 | Q-B4-1 | § 14.2 : contrôle du remplissage du découpeur (écriture par `git show`) |
| D08 | Q-B4-2 | § 14.2 : fichiers à donner (brouillons 2 à 5, avec journaux et pièces) |

Q-B4-3 (couples de cohérence du brouillon 4 gardés) et Q-B4-4 (renvois laissés, correspondance au journal du brouillon 4,
§ 7) : rien à changer.

**Lecture de Q-B4-5.** Le message de la mère dit « l'audit se joue à l'étape B de T0.7, après la course 7b ». Le brouillon
garde la fenêtre du § 4 (« avant l'exécution de l'étape B », le fichier étant exigé par l'étape B) et la ligne gelée
`AUDIT-FUITES-T07` (« scellé avant l'exécution de l'étape B ») : j'ai donc écrit « relève de l'étape B (ligne exigée à
l'étape B) … avant l'exécution de l'étape B », sans contredire la fenêtre (question Q-B5-2).

## 4. Sources lues (en plus de celles du journal du brouillon 4)

| source | sha256 | ce qui a été lu |
|---|---|---|
| `registres/decisions.md` | fichier vivant | lignes R-2346 à R-2348 (R-2347 : début seulement, hors sujet) |
| brouillon 4 et ses pièces | `f9f4bd38…`, script `7539b477…` (égaux aux compagnons) | mes propres sorties |
| commit `c7484c43…` | — | par `git show` seulement : liste du dossier, trois fichiers, trois compagnons |
| réception R1 v4 | `bb6652f2…` (égale au compagnon) | empreintes, par programme |

## 5. Questions ouvertes pour la mère

- **Q-B5-1** (information pour l'audit) : en `transformers` 5.18.0, le nettoyage des espaces de `tokenizer_config.json` est
  ignoré au décodage (avertissement du § 2). Si la chaîne de 7b a décodé les textes avec une version qui l'appliquait, le
  contrôle `decode(ids[:jetons_notes], skip_special_tokens=True) == texte` du § 6.1 peut échouer et arrêter l'audit
  (arrêt prévu, aucun repli). La version de `transformers` de 7b est au manifeste et au rapport de l'auditeur (§ 9, point
  6). À regarder avant le lancement de l'auditeur. Je n'ai rien changé à la règle.
- **Q-B5-2** : si « l'audit se joue à l'étape B » voulait dire autre chose que la fenêtre écrite (avant l'exécution de
  l'étape B), le dire : D04 se corrige d'un couple.
- **Q-B5-3** (pour la contre-lecture) : le § 9 dit « Aucun autre chemin n'est écrit » à propos du dossier de l'auditeur ;
  les trois fichiers du découpeur sont écrits dans son bac à sable, hors du dépôt, comme `TMPDIR` (§ 7) et les fichiers de
  rejeu du contre-lecteur (§ 3). Je le lis comme permis ; un mot au § 9 lèverait le doute.
