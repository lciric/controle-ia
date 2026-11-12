# Ordre de course — A1-v4 (attaque de Goodhart contre le nul v9), hôte durable, lanceur durable v5 — v1

Écrit le 9 novembre 2026 (vers 01:57 UTC, `date -u`) par un rédacteur-développeur neuf, pour la mère
`session_016QhUrrLeN21G7Z9KZobE42`, qui le transmet. **Destinataire : la session exécutante neuve** que la mère crée, dans laquelle
Lazar écrit son mot. **Le texte scellé prime sur cet ordre** :
`docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/preenregistrement-attaque-goodhart-v5-v1.md`
(`d306a8faa45b3d77f1edb653406ced1facd4752b2aa00c2e77593538399a7fe6`, sections 4, 8, 13). Dérivé de l'ordre d'A1-v3
`ordre-fille-a1-v3-troisieme-course-v3.md` (forme : étape 0, préalables, location, après la location), transposé au lanceur durable v5
(`src/controle_ia/hote_durable_a1_v4_v5.py` `352380923e…`, amorce `scripts/amorce_hote_durable_a1_v4_v5.sh` `745040bf…`) et à la
contre-lecture du lanceur (`lanceur-durable-v5/contre-lecture-lanceur-durable-v5-v1.md`, `260ec3f9…`, R-1962) : **M-1** (ligne de GO
de la machine en toutes lettres), **M-2** (préalables vérifiés par `git` avant toute location), **M-3** (compagnon du texte au commit
public), mineurs m-1, m-3, m-5, m-6, m-7, m-8 (notes de lecture, section 9). Essais neufs de ces points :
`tests/test_lanceur_durable_v5_a1v4_course_v1.py`.

Aucune valeur de clé n'apparaît ici : **noms seulement**. Jamais `env`, `printenv`, `set`, ni aucun affichage d'une variable de clé.

## 1. Valeurs

| nom | valeur | d'où |
|---|---|---|
| `COMMIT_PRIVE` | `52b39cbb51edc94f6ade9be79d8b4e06570576a2` | commit X de `main` (R-1959) : lanceur durable v5 à ses chemins d'exécution, configuration (ii) v2 et compagnon ; ancêtre de `origin/main` |
| `COMMIT_CODE` | `b8c1db3add7cdda7fee876944c1e8f692a568e98` | code v5 et lecteur de l'épreuve (dépôt public), `commit_code_gele` de la configuration (ii) v2 |
| `COMMIT_PUBLIC` | `f39a7f4ab9e3da1e11629b1be329304cd5b8a1b0` | second commit public : texte scellé **et** compagnon par-dessus `COMMIT_CODE` (paquet `commit-public-code-v5-a1-v4-v2.bundle`, `ac46f3139ed4001d7b4d6a9dfaf3ae180daf293e85d396fc9070f1a16a9ac190`) ; **poussé par la mère seulement** (étape M) |
| `SHA_TEXTE` | `d306a8faa45b3d77f1edb653406ced1facd4752b2aa00c2e77593538399a7fe6` | texte scellé (R-1961) = son compagnon |
| `NOM_TEXTE` | `orchestrator/prereg/preenregistrement-attaque-goodhart-v5-v1.md` | nom exigé par la configuration (ii) v2 |
| `CONF` | `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/lanceur-durable-v5/configuration-mondes-variante-ii-v2.json` | `1eaa090d59ee9d3c96eaf93cdf9913bf831633d7bbf4a2bc29dbe5e4172c7587`, compagnon `e18d646f…` |
| `COMMIT_REGISTRE` | `740f49e2b27344b3188f9aba20b5f0115c3468ab` | `canal/conv-audit-n04` : dernier commit qui touche `registres/go.md` (12 commits sous la tête `adc1be82` le 9 novembre) ; ligne GO-2026-11-02-22 égale à l'octet à celle de `main` (l. 210) ; aucun identifiant en double ; garde de `main` : accepté à 200 USD ; copie `bdd492d103e654f7727496edf8712505dc0615e59bef6daaeca8fe6cf97f2476` (relevé du rédacteur, à confirmer par la mère, section 10) |
| GO de la machine | **`GO-2026-11-08-12`** (35 USD, échéance 2026-11-16, Lazar) | `registres/go.md` l. 283 ; texte, bloc `plan-gele`, `go_machine` |
| GO des appels | **`GO-2026-11-02-22`** (200 USD exactement, échéance 2026-11-16, Lazar) | l. 210 ; constante du lanceur durable v5, `--go` du lanceur gelé sur la machine |
| Dossier hors clone | `D=/home/user/hors-clone-a1-v4-v9-v1` (neuf) ; journal `J="$D/journal-location-a1-v4-v9-v1.log"` | |
| Clé d'Argon | variable **`GEMINI_API_KEY_2`**, par son nom (le lanceur la fait voyager sous le seul nom `CLE_ARGON`) | R-1540 |
| Jeton GitHub | variable **`CONTROLE_IA_GITHUB_TOKEN_2`** (jeton « classic » de GO-2026-11-05-06), par son nom ; **aucun `GH_TOKEN` dans l'`env -i` de la location** (sinon c'est lui qui partirait) | texte § 8, § 13 point 11 |
| Compte Vast | variable **`VAST_API_KEY`**, par son nom | |

**M-1, en toutes lettres.** La location se fait **sous `GO_ID=GO-2026-11-08-12` et `GO_ID_MACHINE=GO-2026-11-08-12`**, et sous
aucune autre valeur. La garde de périmètre du lanceur (mots « machine » et « a1-v4 ») **admet aussi GO-2026-11-08-14** (150 USD,
échue le 10 novembre ; vérifié par programme, essais neufs) : ce qui la refuse est la ligne `go_machine: GO-2026-11-08-12` du texte
scellé, lue par `verifier_texte` chez le pilote et sur la machine (refus « go_machine = 'GO-2026-11-08-12', la ligne vérifiée
(GO_ID_MACHINE) est 'GO-2026-11-08-14' »). Les appels sont sous **GO-2026-11-02-22**, que le lanceur durable porte en constante (aucune
option) et passe au lanceur gelé par `--go GO-2026-11-02-22` sur la machine.

## 2. Étape M — poussée préalable du commit public (par la mère, sur le mot « go publication » de Lazar)

L'exécutante ne pousse **rien** vers le dépôt public. La mère, et elle seule, sur le mot écrit de Lazar « go publication » (point 1 (c)
du § 13 du texte : publication du texte scellé, distincte du résultat ; précédent R-1771), avec son heure et ses mots exacts au
registre :
```
P=$(mktemp -d)/ideation-organism; git clone -q https://github.com/lciric/ideation-organism.git "$P"
git -C "$P" fetch -q /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/commit-public-code-v5-a1-v4-v2.bundle \
    refs/heads/a1-v4-v5-texte-scelle:refs/heads/a1-v4-v5-texte-scelle
[ "$(git -C "$P" rev-parse a1-v4-v5-texte-scelle)" = f39a7f4ab9e3da1e11629b1be329304cd5b8a1b0 ] || exit 2
git -C "$P" merge-base --is-ancestor b8c1db3add7cdda7fee876944c1e8f692a568e98 f39a7f4ab9e3da1e11629b1be329304cd5b8a1b0 || exit 2
```
(compagnon du paquet vérifié avant : `sha256sum -c commit-public-code-v5-a1-v4-v2.bundle.sha256`.) Puis, après la garde des secrets
habituelle de la mère sur les deux commits (`b8c1db3a`, `f39a7f4a`) : si `origin/main` du dépôt public est encore
`8947bc80a5c2fee0cfee4f3cafbdaaca8ed77f3e`, poussée en avance rapide `git -C "$P" push origin f39a7f4ab9e3da1e11629b1be329304cd5b8a1b0:refs/heads/main` ;
sinon (le public a bougé), **jamais de forçage** : poussée sur une branche neuve `refs/heads/a1-v4-v5-texte-scelle`. La mère transmet à
l'exécutante le nom de la branche publique (`BRANCHE_PUBLIQUE`, `main` ou `a1-v4-v5-texte-scelle`). Jamais vers `lciric/controle-ia`.

## 3. Interdits (sans exception)

- **Rien vers `main`** du dépôt privé, **rien vers `lciric/controle-ia`**, rien vers le dépôt public : l'exécutante ne commite ni ne
  pousse, sauf son rapport sur sa branche de canal neuve (section 8). Aucun fichier suivi du clone privé n'est modifié : tout vit
  sous `$D`.
- **Une seule location** (l'hôte durable v5, étiquette `a1-v4-v9`). **Aucune autre instance** ; aucune commande `vastai` hors de
  `vastai --version`, `vastai search offers` (section 5) et des sous-commandes du lanceur (`inventaire`, `louer`, `controler`,
  `facturation`) ; aucun `vastai start`, `stop`, `destroy` à la main sauf la section 7, point 4, sur mot de la mère.
- **Ne jamais toucher les instances 58936096, 58936099, 58936100** (instances de Lazar ; `PROTEGEES` du lanceur) : ni arrêt, ni
  destruction, ni relance, ni étiquette ; elles peuvent figurer à l'inventaire : on les ignore.
- Aucun appel d'Argon par l'exécutante (aucun appel de contrôle : le texte n'en prévoit aucun). Aucune lecture de la sortie de la
  course. Aucun arrêt par motif de ligne de commande (R10) : par identifiant seulement.
- Jamais `env`, `printenv`, `set`, `declare -p`, `echo $<clé>`, ni la sortie brute de `vastai` à l'écran ou dans un journal.
- Aucune lecture de `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`.

## 4. Étape 0 — dossier neuf et modules (avant tout préalable)
```
COMMIT_PRIVE=52b39cbb51edc94f6ade9be79d8b4e06570576a2
D=/home/user/hors-clone-a1-v4-v9-v1; mkdir "$D" || exit 2          # neuf (R12) ; seul mkdir de l'ordre
J="$D/journal-location-a1-v4-v9-v1.log"
cd /home/user/controle-ia-travail && git fetch -q origin refs/heads/main:refs/remotes/origin/main \
 && git cat-file -e "$COMMIT_PRIVE^{commit}" \
 && for f in hote_durable_a1_v3.py hote_durable_a1_v3_v4.py sonde_hote_durable_a1_v3.py sonde_hote_durable_a1_v3_v10.py hote_durable_a1_v4_v5.py; do
      git show "$COMMIT_PRIVE:src/controle_ia/$f" > "$D/$f" || exit 2; done \
 && { echo "$(date -u +%FT%TZ) étape 0 : COMMIT_PRIVE $COMMIT_PRIVE"; (cd "$D" && sha256sum *.py); } >> "$J"
```
Empreintes attendues (sinon arrêt) : `hote_durable_a1_v4_v5.py` `352380923e612e3456f4c533d2e2e61af5e7b1a69bd2f99bc5ab39c24beebae2`,
`hote_durable_a1_v3.py` `5b853fde8987a472a191f769415068ecc15f1da8a042767bba4229dd5c29e0b1`, `hote_durable_a1_v3_v4.py`
`8101d33bdc259860290feb9a35fb3a93d50df06c84a4268a105f86a973ceef3f`, `sonde_hote_durable_a1_v3.py`
`f7c7f79ba974dd1e38743265caf88f09ce7d4d96ea4676f6d66e75cc9ebca69d`, `sonde_hote_durable_a1_v3_v10.py`
`37b70a0646874e3769a9e45ccf1438121f2126aecc8307234c3cc590f122b81c`. Le module tourne en fichier seul
(`python3 -I -B "$D/hote_durable_a1_v4_v5.py" …`) : il charge ses voisins.

## 5. Préalables (chacun écrit au journal `"$J"` avec sa sortie et l'heure `date -u` ; un échec : arrêt, rien loué, message à la mère)

Toutes les commandes `git` ci-dessous partent de `/home/user/controle-ia-travail` (`origin` = `lciric/controle-ia-travail` : vérifier
`git remote get-url origin | grep -q controle-ia-travail`, sinon arrêt).

1. **Outil et inventaire** : `vastai --version` = `1.8.3` ; inventaire filtré, sous l'`env -i` de la section 6 **sans**
   `GEMINI_API_KEY_2`, `GO_ID`, `GO_ID_MACHINE` :
   `env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 HTTPS_PROXY="${HTTPS_PROXY:-}" NO_PROXY="${NO_PROXY:-}" SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-${SSL_CERT_FILE:-}}" VAST_API_KEY="$VAST_API_KEY" python3 -I -B "$D/hote_durable_a1_v4_v5.py" inventaire > "$D/inventaire-avant-v1.json"` ;
   aucune instance d'étiquette `a1-v4-v9` (sinon arrêt) ; identifiants et étiquettes des autres instances écrits au journal, jamais
   touchés.
2. **Commit privé (M-2, point 1)** — chaque chemin présent à `COMMIT_PRIVE` et à son empreinte :
   ```
   while read attendu chemin; do
     git cat-file -e "$COMMIT_PRIVE:$chemin" || { echo "absent : $chemin" >> "$J"; exit 2; }
     vu=$(git show "$COMMIT_PRIVE:$chemin" | sha256sum | cut -c1-64); echo "$vu  $chemin" >> "$J"
     [ "$vu" = "$attendu" ] || { echo "ÉCART : $chemin" >> "$J"; exit 2; }
   done <<'FIN'
   745040bf9a3a0fc5049cc41b9ad13f29e4776370819095edb021724c914b38ca scripts/amorce_hote_durable_a1_v4_v5.sh
   352380923e612e3456f4c533d2e2e61af5e7b1a69bd2f99bc5ab39c24beebae2 src/controle_ia/hote_durable_a1_v4_v5.py
   5b853fde8987a472a191f769415068ecc15f1da8a042767bba4229dd5c29e0b1 src/controle_ia/hote_durable_a1_v3.py
   8101d33bdc259860290feb9a35fb3a93d50df06c84a4268a105f86a973ceef3f src/controle_ia/hote_durable_a1_v3_v4.py
   f7c7f79ba974dd1e38743265caf88f09ce7d4d96ea4676f6d66e75cc9ebca69d src/controle_ia/sonde_hote_durable_a1_v3.py
   37b70a0646874e3769a9e45ccf1438121f2126aecc8307234c3cc590f122b81c src/controle_ia/sonde_hote_durable_a1_v3_v10.py
   1eaa090d59ee9d3c96eaf93cdf9913bf831633d7bbf4a2bc29dbe5e4172c7587 docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/lanceur-durable-v5/configuration-mondes-variante-ii-v2.json
   e18d646ffd2f581294e304807193fbdc4d50952ec864a5dd6da0db070eb3e31f docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/lanceur-durable-v5/configuration-mondes-variante-ii-v2.json.sha256
   FIN
   git merge-base --is-ancestor 52b39cbb51edc94f6ade9be79d8b4e06570576a2 "$COMMIT_PRIVE" || exit 2
   git branch -r --contains "$COMMIT_PRIVE" | grep -qx '  origin/main' || exit 2
   ```
   Puis la copie de travail de la configuration, celle que `louer` lit : `sha256sum "$CONF"` = `1eaa090d…` et
   `(cd "$(dirname "$CONF")" && sha256sum -c configuration-mondes-variante-ii-v2.json.sha256)` OK.
3. **Commit public (M-2, point 2 ; M-3)**, après l'étape M et le nom `BRANCHE_PUBLIQUE` transmis par la mère :
   ```
   git ls-remote https://github.com/lciric/ideation-organism.git "refs/heads/$BRANCHE_PUBLIQUE" | grep -q '^f39a7f4ab9e3da1e11629b1be329304cd5b8a1b0' || exit 2
   git clone -q https://github.com/lciric/ideation-organism.git "$D/ideation-organism" \
    && git -C "$D/ideation-organism" checkout -q --detach f39a7f4ab9e3da1e11629b1be329304cd5b8a1b0 || exit 2
   [ "$(git -C "$D/ideation-organism" rev-parse HEAD)" = f39a7f4ab9e3da1e11629b1be329304cd5b8a1b0 ] || exit 2
   git -C "$D/ideation-organism" merge-base --is-ancestor b8c1db3add7cdda7fee876944c1e8f692a568e98 f39a7f4ab9e3da1e11629b1be329304cd5b8a1b0 || exit 2
   [ -z "$(git -C "$D/ideation-organism" status --porcelain)" ] || exit 2
   [ "$(git -C "$D/ideation-organism" show "f39a7f4ab9e3da1e11629b1be329304cd5b8a1b0:$NOM_TEXTE" | sha256sum | cut -c1-64)" = d306a8faa45b3d77f1edb653406ced1facd4752b2aa00c2e77593538399a7fe6 ] || exit 2
   [ "$(git -C "$D/ideation-organism" show "f39a7f4ab9e3da1e11629b1be329304cd5b8a1b0:$NOM_TEXTE.sha256" | cut -c1-64)" = d306a8faa45b3d77f1edb653406ced1facd4752b2aa00c2e77593538399a7fe6 ] || exit 2
   ```
   (Sans ce compagnon au commit poussé, la machine refuserait **après** son signe de vie et consommerait les noms v1 : M-2, M-3.)
4. **Branches de données absentes (M-2, point 3)** : `git ls-remote origin 'refs/heads/donnees/attaque-goodhart-v4-a1v4-*'` ne rend
   **rien** — ni `donnees/attaque-goodhart-v4-a1v4-v1`, ni `…-refus-v1`, ni `…-interrompue-v1`, ni `…-signe-de-vie-v1`. Une seule
   présente : arrêt (R12 ; seul un lanceur v6 à noms neufs ou un geste de Lazar permettrait alors de lancer).
5. **Pièces gelées** (extraites par la machine ; vérifiées ici sans exécution) :
   ```
   git fetch -q origin refs/heads/donnees/recuperation-collisionneur-v8-v1:refs/remotes/origin/donnees/recuperation-collisionneur-v8-v1 \
     refs/heads/canal/session-depot-reprise-n120:refs/remotes/origin/canal/session-depot-reprise-n120 \
     refs/heads/canal/conv-audit-n04:refs/remotes/origin/canal/conv-audit-n04
   N=donnees/mini-course-kimi-argon-v1/orchestrateur/nuit; R=origin/donnees/recuperation-collisionneur-v8-v1
   git show "$R:$N/commande_argon_v56_nuit_v2.py" | sha256sum      # 221df610681ed47bf66fbfef21d583006aa3e09a3147e22227faacd98622b851
   git show "$R:$N/registre_depense_cumulee_v1.py" | sha256sum     # 8ba92066b358ffb8206dea9e70251388c30620484fab1ac578778d9f21e578ff
   git show "$R:donnees/espece-seule-v1/collisionneur_v7.py" | sha256sum  # c9725f025407c3ece3e8c16d19cfdfdec078f084a811f0a3b6ea3209be5d98dc
   git show origin/canal/session-depot-reprise-n120:brouillons/canal-reprise-releve-v1/envois/session-depot/conf-a1-v3/configuration-mini-course-kimi-argon-v3.json | sha256sum
                                                                  # e5306c47e1b21a5e55b599411dba92c97e88aa98bb6d6fa91fc5d358a2bdde30
   ```
   Une empreinte autre : arrêt.
6. **Registre passé au lanceur gelé** : `git merge-base --is-ancestor 740f49e2b27344b3188f9aba20b5f0115c3468ab origin/canal/conv-audit-n04` ;
   `git rev-list --count 740f49e2b27344b3188f9aba20b5f0115c3468ab..origin/canal/conv-audit-n04` ≤ 200 (profondeur lue par la machine ;
   12 le 9 novembre) ; ligne égale à l'octet :
   `diff <(git show 740f49e2b27344b3188f9aba20b5f0115c3468ab:registres/go.md | grep '^| GO-2026-11-02-22 ') <(git show origin/main:registres/go.md | grep '^| GO-2026-11-02-22 ')` vide ;
   aucun identifiant en double :
   `git show 740f49e2b27344b3188f9aba20b5f0115c3468ab:registres/go.md | awk -F'|' '/^\| GO-/{print $2}' | sort | uniq -d` vide ;
   empreinte de la copie (`git show 740f49e2…:registres/go.md | sha256sum`) écrite au journal (`bdd492d1…` attendu).
7. **Lignes de GO sur `main`** : `git show origin/main:registres/go.md | grep -n 'GO-2026-11-02-22\|GO-2026-11-08-12'` au journal ;
   GO-2026-11-02-22 à **200 USD**, GO-2026-11-08-12 à **35 USD**, toutes deux « calcul », Lazar, échéance 2026-11-16 ; aucune ligne de
   type « révocation » qui nomme l'une ou l'autre. **Location avant le 16 novembre 2026, 00:00 UTC** (texte § 4 et § 13, point 11).
8. **Jeton GitHub** (par son nom) : `curl -sI -H "Authorization: Bearer ${CONTROLE_IA_GITHUB_TOKEN_2}" https://api.github.com/rate_limit | grep -i '^HTTP/\|^github-authentication-token-expiration'`
   (seules la ligne d'état et celle de l'échéance) : `200`, et aucune échéance ou une échéance postérieure à T0 + 82 h. L'exécutante
   écrit au journal que c'est le jeton « classic » de GO-2026-11-05-06 qui est sous ce nom (mot de la mère). Sinon : arrêt.
9. **Argon seul** (texte § 8) : la mère transmet par écrit la liste des utilisations d'Argon en cours ou prévues pendant la course
   (course de l'organisme d'idéation, épreuve de l'étiqueteur, réplication A1-v3 sous GO-2026-11-02-25, toute autre) ; **aucune**,
   écrit au journal avec l'heure ; jamais en même temps qu'une course A1-v3. Un doute : arrêt et message.
10. **Crédit d'Argon** (précaution du 402, texte § 8) : au journal, **l'un des deux**, avec heure et mots exacts — (a) la confirmation
    de Lazar que le crédit prépayé couvre au moins 200 USD, ou qu'une recharge automatique d'au moins ce montant est active ; ou (b)
    son mot qui abandonne la précaution, **avec son prix** (jusqu'à ≈ 121 USD perdus à l'attendu haut, ≈ 194 USD au pire, plus la
    machine). Sans (a) ni (b) : aucune location.
11. **Mots de Lazar** (texte § 13, point 1) : (c) « go publication » donné et la poussée de l'étape M faite (préalable 3 le
    prouve) ; (d) **mot écrit de Lazar dans cette session**, avant toute dépense, recopié tel quel au journal avec son heure ;
    (a) facultatif : une ligne d'extension de GO-2026-11-02-22 qui écrit « hôte durable » (sinon l'écart de lettre reste consigné,
    texte § 0.1, point 4). Sans (d) : aucune location.
12. **Aucun appel de contrôle d'Argon** : aucun n'est fait.

## 6. Vérifications sans création, puis location (une fois ; sortie brute de `vastai` jamais affichée)

Variables d'environnement transmises à `louer` : **ces noms seuls**, sous `env -i` (les quatre du mandataire sont des chemins et une
adresse, jamais affichés ; aucune n'est transmise à la machine : le corps ne porte que ses variables explicites).
```
COMMIT_PRIVE=52b39cbb51edc94f6ade9be79d8b4e06570576a2
COMMIT_PUBLIC=f39a7f4ab9e3da1e11629b1be329304cd5b8a1b0
SHA_TEXTE=d306a8faa45b3d77f1edb653406ced1facd4752b2aa00c2e77593538399a7fe6
COMMIT_REGISTRE=740f49e2b27344b3188f9aba20b5f0115c3468ab
NOM_TEXTE=orchestrator/prereg/preenregistrement-attaque-goodhart-v5-v1.md
CONF=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/lanceur-durable-v5/configuration-mondes-variante-ii-v2.json
D=/home/user/hors-clone-a1-v4-v9-v1; J="$D/journal-location-a1-v4-v9-v1.log"
[ "$(vastai --version 2>/dev/null)" = "1.8.3" ] || { echo "vastai 1.8.3 exigé"; exit 2; }
[ -f "$D/hote_durable_a1_v4_v5.py" ] && [ -d "$D/ideation-organism/.git" ] || { echo "étape 0 ou préalable 3 non fait"; exit 2; }
```
**6.1 `verifier-texte`** (code 0 exigé) :
```
python3 -I -B "$D/hote_durable_a1_v4_v5.py" verifier-texte --texte "$D/ideation-organism/$NOM_TEXTE" --sha-texte "$SHA_TEXTE" \
    --configuration-mondes "$CONF" > "$D/verifier-texte-v1.json" 2>> "$J"; echo "verifier-texte code $?" >> "$J"
```
Sortie attendue (rejouée par le rédacteur sur le commit reconstitué) : `"version": 1`, `"sha256": "d306a8fa…"`, `"mondes": "W2 et W2g"`,
`"lignes_gelees": 79`, `"plafond_usd": 200.0`, `"go": "GO-2026-11-02-22"`, `"go_machine": "GO-2026-11-08-12"`,
`"nom": "orchestrator/prereg/preenregistrement-attaque-goodhart-v5-v1.md"`, `"variante": "ii"`, `"fichiers_geles_publics_egaux": 13`,
`"configuration_sha256": "1eaa090d…"`. Toute autre valeur : arrêt.

**6.2 Registre et garde de `main`, offres** :
```
cd /home/user/controle-ia-travail && git fetch -q origin refs/heads/main:refs/remotes/origin/main \
 && git show origin/main:registres/go.md > "$D/registre-go-main.md" \
 && git show origin/main:.claude/hooks/garde_calcul.py > "$D/garde_calcul_main.py" \
 && timeout 300 vastai search offers 'num_gpus=1 rentable=true reliability>=0.98 cpu_cores_effective>=4 cpu_ram>=8 disk_space>=30 dph_total<=0.40' -o dph_total --storage 30 --raw > "$D/offres.json" \
 && OFFRE=$(python3 -I -B "$D/hote_durable_a1_v4_v5.py" offre --offres "$D/offres.json") && echo "offre $OFFRE" >> "$J"
```
**6.3 `louer --verifier-seulement`** (code 0 exigé ; aucune création) :
```
GO_ID=GO-2026-11-08-12 GO_ID_MACHINE=GO-2026-11-08-12 env -i GO_ID=GO-2026-11-08-12 GO_ID_MACHINE=GO-2026-11-08-12 \
  PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 HTTPS_PROXY="${HTTPS_PROXY:-}" NO_PROXY="${NO_PROXY:-}" SSL_CERT_FILE="${SSL_CERT_FILE:-}" \
  REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-${SSL_CERT_FILE:-}}" \
  GEMINI_API_KEY_2="$GEMINI_API_KEY_2" CONTROLE_IA_GITHUB_TOKEN_2="$CONTROLE_IA_GITHUB_TOKEN_2" VAST_API_KEY="$VAST_API_KEY" \
  timeout 1800 nice -n 10 python3 -I -B "$D/hote_durable_a1_v4_v5.py" louer \
    --registre-main "$D/registre-go-main.md" --garde-main "$D/garde_calcul_main.py" --offres "$D/offres.json" --offre "$OFFRE" \
    --commit-prive "$COMMIT_PRIVE" --commit-public "$COMMIT_PUBLIC" --texte "$D/ideation-organism/$NOM_TEXTE" --sha-texte "$SHA_TEXTE" \
    --configuration-mondes "$CONF" --racine-privee /home/user/controle-ia-travail --commit-registre "$COMMIT_REGISTRE" \
    --journal-local "$J" --verifier-seulement; echo "louer --verifier-seulement code $?" >> "$J"
```
Le journal doit porter, dans l'ordre : « machine GO-2026-11-08-12 (plafond lu 35 USD, échéance 2026-11-16) et appels GO-2026-11-02-22
(200 USD exact) acceptés par la garde de main » ; « configuration des mondes : variante (ii) ['W2', 'W2g'] ; …v2.json 1eaa090d… ; 13
fichiers gelés publics ; code gelé b8c1db3a… » ; « texte orchestrator/prereg/preenregistrement-attaque-goodhart-v5-v1.md : empreinte
d306a8fa… = compagnon = scellement ; … 79 lignes gelées, 13 fichiers gelés publics égaux » ; **« garde de dépense (1/2) »** et
**« garde de dépense (2/2, sur le corps) »**, coût au plus = prix × 81,42 h ≤ 35 (32,57 USD à 0,40 USD/h) ; « vérification seulement :
rien créé (variables : CHEMIN_CONFIGURATION_MONDES, CLE_ARGON, COMMIT_PRIVE, COMMIT_PUBLIC, COMMIT_REGISTRE, DEPOT_URL, ECHEANCE_UTC_S,
GH_TOKEN, GO_ID, GO_MACHINE, NOM_TEXTE, PRIX_H_USD, SHA_CONFIGURATION_MONDES, SHA_TEXTE) » — **quatorze noms, aucune variable du
mandataire**. Toute ligne « REFUS », un code autre que 0, ou une variable en plus : arrêt, rien loué, message.

**6.4 `louer`** (la location ; même commande que 6.3, **sans** `--verifier-seulement`, lancée **aussitôt** après un 6.3 en code 0 et
sur les mêmes offres) ; `echo "louer code $?" >> "$J"`. (`timeout 1800` : cinq créations de 300 s au plus tiennent.)

**Si `louer` rend 2 :**
- **« no_such_ask » final** (rien créé, aucun marqueur) : une seule reprise, dans un **dossier neuf**
  `D=/home/user/hors-clone-a1-v4-v9-v1b` (étape 0, préalable 3 pour le clone public, puis section 6 entière, recherche comprise) ;
  puis message.
- **Marqueur `"$J.creation-incertaine"` présent** : **aucune** nouvelle location ; inventaire filtré (préalable 1), puis message (une
  instance peut exister).
- Tout autre refus (GO, texte, configuration, offre, coût, clé) : rien créé ; message, **sans reprise**.

## 7. Après la location : surveillance, rapatriement, destruction, arrêts

1. **Aussitôt** : envoyer à la mère la « LIGNE POUR registres/etat.md » du journal (identifiant, T0, prix, échéance finale) et
   l'identifiant écrit dans `"$J.identifiant"`. L'état est dans `"$J.etat.json"` (identifiant, `t0_utc`, `borne_signe_de_vie_utc` =
   T0 + 30 min, `echeance_finale_utc`, `controles_utc`).
2. **Surveillance** — `controler` sous `env -i` **sans** `GEMINI_API_KEY_2`, `GO_ID` ni `GO_ID_MACHINE`, avec le jeton sous le nom que
   `controler` lit :
   ```
   env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 HTTPS_PROXY="${HTTPS_PROXY:-}" NO_PROXY="${NO_PROXY:-}" SSL_CERT_FILE="${SSL_CERT_FILE:-}" \
     REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-${SSL_CERT_FILE:-}}" GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN_2" VAST_API_KEY="$VAST_API_KEY" \
     python3 -I -B "$D/hote_durable_a1_v4_v5.py" controler --etat "$J.etat.json" --journal-local "$D/journal-controle-a1-v4-v9-v1.log"
   ```
   (`facturation` de même, à tout moment.) **Premier contrôle à T0 + 40 min, jamais avant** (m-6 : la machine peut passer jusqu'à
   ≈ 35 min en installations et clone avant son signe de vie) ; juste avant, lire l'inventaire filtré (`actual_status` de
   l'identifiant) et le journal de location, écrits au journal de contrôle. Puis aux heures de `controles_utc`, et à tout moment
   `git ls-remote origin 'refs/heads/donnees/attaque-goodhart-v4-a1v4-*'` (lecture des noms et des commits seulement). **Conduite par
   code** :
   - **0** — instance absente (détruite par elle-même ou par la minuterie) : message ; la mère consigne (`registres/arrets.md`) ; fin
     des contrôles.
   - **1** — détruite par le pilote (aucun signe de vie à T0 + 30 min : rien n'a tourné, aucun nom consommé) : message ; **aucune
     relocation** sans mot de la mère.
   - **2** — refus (étiquette autre, instance protégée, état illisible) : **aucun geste** ; vérifier `"$J.etat.json"` et
     l'identifiant ; message immédiat ; recontrôler une fois dans 10 min, puis attendre la mère.
   - **3** — destruction demandée mais encore listée : recontrôler dans 5 min (au plus trois fois), puis message.
   - **5** — listée avant ses bornes : recontrôler à l'heure suivante de l'état ; `stopped` ou `exited` avant l'échéance → message.
   - **6** — délai ou échec de `vastai` ou de `ls-remote` : recontrôler dans 5 min, au plus trois fois de suite, puis message (jamais
     « pas de signe de vie » sur un 6).
   - **7** — encore listée après l'échéance finale : **aucun geste** ; message ; la mère décide (données possibles sur le disque).
3. **Rapatriement** (la machine verse elle-même ; l'exécutante ne lit **aucun** résultat) : quand
   `donnees/attaque-goodhart-v4-a1v4-v1` (ou `…-refus-v1`, `…-interrompue-v1`) apparaît à `ls-remote`, écrire au journal son commit,
   puis, dans un dossier neuf, l'intégrité seule :
   ```
   B=donnees/attaque-goodhart-v4-a1v4-v1; mkdir "$D/rapatriement-v1" || exit 2
   git fetch -q origin "refs/heads/$B:refs/remotes/origin/$B" && git archive "origin/$B" "$B" | tar -x -C "$D/rapatriement-v1" \
    && (cd "$D/rapatriement-v1/$B" && sha256sum EMPREINTES-sortie-a1-v4-v1.txt && sha256sum -c --quiet EMPREINTES-sortie-a1-v4-v1.txt; echo "contrôle $?") >> "$J"
   ```
   Aucun fichier de la sortie n'est ouvert, affiché ni copié ailleurs ; rien n'est fusionné dans `main`. Le verdict (R13) et l'audit
   (texte § 7) sont faits par d'autres, sur ordre de la mère.
4. **Destruction par identifiant** : la machine se détruit elle-même par `CONTAINER_ID` après un versement vérifié ; le pilote ne
   détruit que par `controler` (identifiant de `"$J.etat.json"`, étiquette `a1-v4-v9` contrôlée, instances protégées refusées).
   Toute autre destruction : **seulement sur mot de la mère**, par l'identifiant de `"$J.etat.json"` après lecture de son étiquette
   `a1-v4-v9` à l'inventaire et vérification qu'il n'est pas 58936096, 58936099 ni 58936100 ; consignée (`registres/arrets.md`, par la
   mère).
5. **Arrêts et cas déclarés** (rien n'est relancé par l'exécutante) :
   - machine **arrêtée, non détruite** (versement non vérifié ou secret trouvé : journal « versement non vérifié », « VERSEMENT
     IMPOSSIBLE ») : aucun `vastai start`, aucun geste ; message ; la mère décide (R14) ;
   - reprise du conteneur : la machine ne relance rien, verse sur `…-interrompue-v1` et se détruit ; rapporter ;
   - voie hors borne (m-7) : machine qui ne lance jamais son script (état « loading » prolongé) → `controler` à T0 + 40 min la
     détruit faute de signe de vie (code 1) ; minuterie qui n'obtient jamais le `DELETE` → stockage seul facturé jusqu'à l'inventaire :
     code 7 → message ;
   - HTTP 402 d'Argon : aucune règle d'arrêt ajoutée ; la course s'arrête à son plafond (code 3) ; rapporter ;
   - utilisation d'Argon par un tiers pendant la course : écart déclaré, lu par l'audit A9, **jamais un arrêt** ;
   - tout refus de la machine après le signe de vie consomme les noms v1 : **aucune** seconde location (lanceur v6 ou geste de Lazar).

## 8. À qui rendre compte

À la **mère** seule (`session_016QhUrrLeN21G7Z9KZobE42`), par message, à chaque étape : étape 0, préalables (un par un, avec leurs
sorties de vérification, jamais une valeur de clé), 6.1, 6.3, 6.4 (identifiant), chaque contrôle, rapatriement, fin. Aucune question à
Lazar : tout passe par la mère ; le seul écrit de Lazar dans cette session est son mot (préalable 11 (d)), et ses mots du préalable 10
s'il les y écrit lui-même. Rapport court à la location et à la fin, scellé (`PYTHONPATH=src python -m controle_ia.scellement sceller`)
sous `$D`, poussé **seulement** sur une branche de canal neuve `canal/executante-a1-v4-v9-v1` du dépôt privé si la mère l'autorise ;
sinon remis par message. Les registres (`etat.md`, `decisions.md`, `depenses.md`, `arrets.md`) sont tenus par la mère.

## 9. Notes de lecture (mineurs de la contre-lecture)

- **m-1** : toute mention « v4-v<N> » ou « lanceur gelé v4 » des journaux du lanceur durable (message de refus du texte, docstrings)
  désigne le texte **v5-v1** et le lanceur gelé **v5** de la configuration (ii) v2 ; le module n'est pas retouché (empreinte gelée).
- **m-3, qui vérifie quoi** : le lanceur durable vérifie le nom du texte, son empreinte = `SHA_TEXTE` = compagnon, l'absence de
  marqueur, le bloc `plan-gele` (`mode`, `mondes`, `fournisseurs`, `go`, `plafond_usd` = 200, `go_machine` = la ligne vérifiée) et
  les **13** fichiers gelés publics de la configuration (sur le clone et dans le bloc) ; les **79** empreintes de la fermeture et
  l'entropie (= entier de l'empreinte) sont vérifiées par le **lanceur gelé v5** à `--verifier-seulement` sur la machine, avant tout
  appel (rejouées ici sur le commit reconstitué : `lire_preenregistrement` accepte, 79 = `FICHIERS_GELES`).
- **m-5** : dans le rendu de `verifier_go_machine`, `accorde` est la **date** d'accord ; le nom « Lazar » est contrôlé par la garde de
  `main`.
- **m-8** : le rapport du lanceur v5 (§ 2 et § 4) décrit la configuration **v1** (11 fichiers, lanceur gelé v4) ; la course prend la
  **(ii) v2** (13 fichiers, lanceur gelé v5, préfixe `preenregistrement-attaque-goodhart-v5-v`, étape `attaque_goodhart_v5/argon`).
- **M-1, réserve datée** : la réserve du rapport du lanceur (§ 6, « aucune telle ligne au registre de `main` ») était vraie le
  8 novembre à 17:00 UTC, fausse depuis 20:45 UTC (GO-2026-11-08-14).

## 10. Points laissés à la mère avant de transmettre

- Confirmer `COMMIT_REGISTRE=740f49e2…` (choisi par le rédacteur : dernier commit du canal qui touche le registre ; ligne égale, aucun
  doublon, garde acceptée) ou en donner un autre (texte § 13, point 7).
- Confirmer `COMMIT_PRIVE` = X ; un commit de `main` qui en descend est permis par le texte, à condition de rejouer le préalable 2.
- Sceller cet ordre et les essais neufs, les commiter ; faire l'étape M sur « go publication » et transmettre `BRANCHE_PUBLIQUE`.
- Dire si l'exécutante pousse son rapport sur `canal/executante-a1-v4-v9-v1` ou le remet par message.
