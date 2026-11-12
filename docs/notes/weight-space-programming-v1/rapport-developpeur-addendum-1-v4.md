# SPARKS-EXP7-NUL — rapport du rédacteur-développeur : brouillon 4 de l'addendum n° 1 et code v4

Même rédacteur-développeur que pour les brouillons 2 et 3 (sous-agent Claude, Opus 5.5) ; il n'a écrit aucune
contre-lecture. Tâche : message de la mère du 4 novembre 2026 (≈ 22:55 UTC), après la contre-lecture du delta v3
(`docs/notes/weight-space-programming-v1/contre-lecture-delta-v3-v1/contre-lecture-delta-v3-v1.md`, sha256
`cf2ffcb0d52ed961185ba6750fcfbe138896aa3163fa7a7e9baef1e613048555`, lue en entier avec la démonstration de minuterie ;
sept compagnons du dossier « OK »). Travail du 4 novembre, de 22:53 à 23:30 UTC environ (`date -u`).
Interdits respectés : aucune poussée, aucun `.sha256` sur `main`, aucun fichier existant modifié, aucun réseau, aucune
dépense ; moins de 30 Mo employés, fichiers temporaires nettoyés.

**Verdict.** Code v4 : branche locale `prep/sparks-exp7-nul-v4`, commit `53d4eda68560a7eb5b2ceca1fd069f9fd9dcaa30`.
C'est deux commits sur `4c3bf146` (`96aae619`, puis `53d4eda6` qui renforce un essai), avec 20 fichiers neufs et aucun
fichier modifié ; la liste fermée v4 (94 fichiers) est conforme.
- Les huit changements de la contre-lecture sont faits.
- Essais et banc : section 3.
- Brouillon 4 : les 10 couples sont tous retenus, puis H-1 à H-6 ; les trois marqueurs restent.
- La répétition jouet corrigée est en section 5, prête à être jouée par la session mère.

## 1. Fichiers et empreintes

Sur `main` (fichiers neufs, sans compagnon) :

| Fichier | sha256 |
|---|---|
| `prereg/SPARKS-EXP7-NUL-addendum-1-brouillon4.md` | `925c11fe58fe157e2343d5d36b816aacbdeb0f677d63afa50a1c0818323d5f29` |
| `docs/notes/weight-space-programming-v1/brouillon4-addendum-1-v1/appliquer-couples-addendum-1-brouillon4-v1.py` | `4df7ed5fd42dadff87ca22884f6b9ebb2f96de1d3a934b2efe6c6e1b4f1903f4` |
| `docs/notes/weight-space-programming-v1/brouillon4-addendum-1-v1/sortie-appliquer-couples-addendum-1-brouillon4-v1.txt` | `91a12e7cafaef63cb30194183e65ac555fc575d5627f695933c1610a7e19d1c2` |
| `docs/notes/weight-space-programming-v1/essais-et-banc-sparks-v4/` (sorties brutes) | section 3 |
| ce rapport | — |

Le script vérifie ses entrées : brouillon 3 `12e47e51…`, couples `838882eb…`.
- Il applique K1 à K10 dans l'ordre, chacun unique au moment de son application. Le texte intermédiaire,
  `4ea5636bc604000c…`, est **égal au texte d'essai du contre-lecteur**.
- Il applique ensuite H-1 à H-6 : en-tête, table 0000, exception déclarée à K9, compléments de la liste de code v4
  (leçon R-1497 comprise), contre-lecture, pied.
- Il exige trois marqueurs et refuse d'écraser.
- **Aucun couple ne tombe** : les huit changements de code sont retenus.
- K9 dit « chacune mutée au banc ». H-2 y ajoute l'exception vraie : les gardes du script d'instance (`POUSSEE-VERIFIEE`,
  préfixe de la branche des sorties) ne se jouent qu'à la répétition et ne sont pas mutées.

Sur `prep/sparks-exp7-nul-v4` (chaque fichier avec son compagnon `.sha256`) :

| Fichier | sha256 |
|---|---|
| `scripts/amorce_instance_sparks_exp7_nul_v4.sh` | `efc9f263f90482b16c4850d5bc2f0b650264c9cfddd6ad450515432f10a625ba` |
| `scripts/banc_mutations_sparks_exp7_nul_v4.py` | `41af2281c7832b995b4d70b15361fa2ff08aeca0495bcd10457e7e7cb079081d` |
| `scripts/lancer_sparks_exp7_nul_v4.sh` | `b53776fc51f32f560780197ab7db1116359f6b9136ca8efb488c9c8bf21aaced` |
| `scripts/sparks_exp7_nul_instance_v4.sh` | `2de49ab0445588dc69068a30b281c723e271a8dd9f39188547ceecb50596c951` |
| `src/controle_ia/sparks_exp7_nul_v4/__init__.py` | `f6b86e53a14d217c2fe36adfa8929ac07f189be043f07fae27289ba9670c10aa` |
| `src/controle_ia/sparks_exp7_nul_v4/garde_code.py` | `507814396906cdb5587e57783bd090d477327f7e2dc1e066986e4e6e9ddd9e91` |
| `src/controle_ia/sparks_exp7_nul_v4/liste-fermee-v1.txt` | `f97735ac1fc3b264575f389977ebd3b621f81cc71512477ff5d7c17a66ede916` |
| `src/controle_ia/sparks_exp7_nul_v4/plan.py` | `8ea645ca82dcf12ca330b52ca57b7a618acf4f73087321af95e032920e4f633c` |
| `src/controle_ia/sparks_exp7_nul_v4/redemarrage.py` | `395896e2499a9ad1c3cc7c28a49d7cf150aaba87aaf606ae67a226cb91d901b3` |
| `tests/test_sparks_exp7_nul_v4.py` | `91829f34969352eb17a4d26b20ddbc8fe2ea865aa744f511f27d5aaeac11f706` |

`garde_code liste . 53d4eda6…` (v4) → « LISTE FERMÉE CONFORME : 94 fichiers ».

## 2. Les huit changements

1. **`timeout` sur chaque étape de l'amorce avant le calcul** :
   - durées : clone, `sparse-checkout` et `checkout` 600 s ; `fetch`, `archive` et `tar` des ordres 300 s ; chaque garde
     Python 120 s (GO, durée, garde du code, borne, vérification, consignations) ; lot 900 s ; `vastai destroy` dans la
     minuterie 120 s ;
   - les délais peuvent être **raccourcis** par l'environnement (`AMORCE_T_*_S`, pour les essais), jamais allongés
     (`borne_t`) ;
   - artefact « `git` bloqué » : refus en moins de 30 s avec un délai de 3 s ;
   - au passage, le dossier des ordres est tiré par `mktemp` : deux démarrages dans la même seconde se heurtaient (défaut
     trouvé par les essais).
2. **Attente sur `$!`** : `PM=$!` juste après `setsid`, puis `attendre_minuterie` sur `PM`, au plus marge + 120 s.
   - Essais sous `unshare -pf --mount-proc` : reprise après l'échéance, et ordre « fin » au redémarrage : `DELETE` au
     journal.
   - Témoin, la démonstration du contre-lecteur reproduite : sans l'attente, aucun `DELETE`.
3. **Ordres** :
   - branche `ordres/sparks-exp7-nul-v4-<COMMIT[:12]>`, jamais sous `calcul/` ;
   - clé `instance` (chiffres) égale à `CONTAINER_ID`, exigée par `redemarrage.lire_ordre(…, instance)`, sinon refus ;
   - `fait … || exit 2` (essai : un lien vers un dossier absent rend l'écriture impossible, et rien ne part).
4. **`deja_usd`** et borne de la machine :
   - les faits sont consignés en « numéro deja_usd » ; un `deja_usd` plus bas que celui d'un ordre exécuté est refusé ;
   - borne propre de la machine (`redemarrage.borne_machine`) : plafonds de démarrage consignés **avant** chaque
     lancement (`sparks-v4-demarrages.txt`, `|| exit 2`) × prix de la carte, plus le temps écoulé depuis la création
     (`sparks-v4-creation.txt`) × prix du stockage ;
   - l'amorce prend max(`deja_usd`, borne).
5. **Branches des sorties** : l'amorce pose `BRANCHE`.
   - Fabrication : `${BRANCHE_PREFIXE}sparks-exp7-nul-v4-<court>`. Causal : `…-causal-v4-<court>-<NNN>`.
   - Préfixe `calcul/` par défaut, ou `essai/` ; tout autre préfixe est refusé.
   - Le script d'instance v4 exige `BRANCHE` et en contrôle le préfixe.
6. **Lanceur v4** : il imprime des commandes littérales, que la garde de calcul voit ; elles sont sous `timeout`
   (create et start 300 s, destroy 120 s).
   - `env -i` ne garde que PATH, HOME, LANG et, s'ils sont présents, `HTTPS_PROXY`, `HTTP_PROXY`, `NO_PROXY`,
     `SSL_CERT_FILE` et `REQUESTS_CA_BUNDLE`, par leur nom seulement (R-1497). L'essai le vérifie : le sous-processus les
     reçoit, une autre variable ne passe pas, aucune valeur n'est imprimée.
   - La sortie de `vastai` va dans un fichier jamais affiché.
   - `apres-creation` ne rend que le code et l'identifiant. Un code non nul ou un délai pose `.creation-incertaine`, et
     toute création suivante est refusée. Une erreur de certificat donne un refus « non parvenu », sans marqueur.
   - `--label sparks-exp7-nul-v4-<court>`.
7. **Mutations** : 30 neuves sur la v4, couvrant les points 17 et 22 de la contre-lecture et la liste des changements,
   en plus des 114 du banc v3. « Tuée » seulement au code 1 avec « failed ».
8. **Répétition corrigée** : section 5.

## 3. Essais et banc

Sorties brutes dans `essais-et-banc-sparks-v4/` (même dossier que ce rapport). Au commit final `53d4eda6` :

| Mesure | Compte | Sortie (sha256) |
|---|---|---|
| Essais v1, v2, v3 (inchangés) et v4 (29 cas) | **226 passés sur 226** (90 + 69 + 38 + 29), 0 sauté, 0 échec | `essais-53d4eda6.txt` `12b815ec…` |
| Banc v4 : mutations du banc v1 | **22/22 tuées** (code 1 et « failed ») | `banc-53d4eda6.txt` `1f5a97df…`, `.json` `a68d866c…` |
| Banc v4 : mutations du banc v2 (avec les deux ajoutées en v3) | **52/52 tuées** | idem |
| Banc v4 : mutations du banc v3 | **40/40 tuées** | idem |
| Banc v4 : mutations neuves de la v4 | **30/30 tuées** ; quatre témoins verts ; 0 inapplicable | idem |

Tout run est compté (R4). Au premier commit v4 (`96aae619`), les essais donnaient 225/225 ; le banc donnait 22, 52, 40 et
**29/30** : une mutation survivait, « lanceur : succès sans “success” », parce que l'essai n'avait pas de sortie portant un
identifiant avec `success` faux. J'ai ajouté ce cas d'essai au commit `53d4eda6`, puis tout rejoué. Sorties de ce premier
passage : `essais-96aae619.txt` `e766df0f…`, `banc-96aae619.txt` `7d2f539d…`,
`banc-96aae619.json` `5f96ff43…`. Pendant le développement, avant le premier commit, j'ai fait trois
passages des seuls essais v4, jusqu'au vert : deux défauts y sont apparus et ont été corrigés, le faux `git` de l'essai
et le dossier des ordres qui se heurtait dans la même seconde.

## 4. Réserves

1. **Rien n'a tourné sur une machine réelle.** Le tir réel reste exigé (R-1477, liste du point 24 de la contre-lecture
   et K9) : `DELETE`, puis une lecture qui ne trouve plus l'instance ; `curl` et `git` dans l'image ; relance par
   `vastai start` ; `vastai copy` sans `sshd` ; instance « exited » sans carte facturée.
2. **Gardes du script d'instance non mutées** (poussée vérifiée, préfixe de la branche) : jouées seulement à la
   répétition.
3. **Le délai de `apres-creation`** : si `vastai create` dépasse ses 300 s, le marqueur est posé, mais une instance a pu
   naître. L'inventaire « sans sortie brute », qui précède le retrait du marqueur, reste à la session ; il n'y a pas
   d'outil d'inventaire dans ce code.
4. **La répétition jouet exerce la plomberie, pas les calculs** : la fabrication jouet s'arrête à « 0/28 dans les
   bornes », la copie échoue donc à « lot impossible », et la phase causale jouet échoue au chargement de `jouet`. Le
   chemin « poussée vérifiée → destruction » n'est couvert que par l'essai à script factice.

## 5. Répétition jouet corrigée (à jouer depuis la session mère, reliée au dépôt distant)

Conséquence à connaître : la branche `essai/sparks-v4-repetition` pousse au dépôt distant les commits du code v2 à v4
(l'instance clone ce qu'elle lance) ; elle est supprimée à la fin, mais les objets restent sur le dépôt.

Corrections, avec le point de la contre-lecture :
- chaque étape continue après l'échec attendu de la précédente, avec un contrôle explicite (19) ;
- les variables du mandataire et la configuration globale de `git` passent dans chaque `env -i` (20) ;
- une branche par phase, liée au commit et à l'ordre, préfixe `essai/` (21) ;
- les ordres vont sur la branche `ordres/…` du commit de répétition, depuis un dépôt à part ; l'arbre du code n'est pas
  touché (22) ;
- `timeout` partout ;
- toutes les minuteries sont arrêtées par leur numéro de processus.

```bash
#!/usr/bin/env bash
# Répétition jouet de SPARKS-EXP7-NUL v4 : création, redémarrage de copie, phase causale, fin. Aucune instance, aucun vastai,
# curl simulé (aucun appel à Vast) ; écrit seulement des branches essai/… et ordres/… sur le dépôt distant, supprimées à la fin.
set -uo pipefail
CODE=53d4eda68560a7eb5b2ceca1fd069f9fd9dcaa30           # commit du code v4 (le remplacer par le commit final s'il change)
DEPOT=/home/user/controle-ia-travail                   # clone de la session mère (relié au dépôt distant)
URL=https://github.com/lciric/controle-ia-travail.git
J=$(mktemp -d /tmp/repetition-sparks-v4-XXXX); mkdir -p "$J/faux-bin" "$J/racine" "$J/home"
T() { timeout -k 10 "$@"; }                            # tout est borné
# 0. Commit de répétition dans un arbre à part (l'arbre du code n'est pas touché) : addendum FICTIF scellé + GO de main
T 600 git -C "$DEPOT" worktree add -q --no-checkout -b essai/sparks-v4-repetition "$J/prep" "$CODE"
T 60 git -C "$J/prep" sparse-checkout set --no-cone '/*' '!/*/' '/prereg/SPARKS-EXP7-NUL-*' '/registres/go.md'
T 600 git -C "$J/prep" checkout -q essai/sparks-v4-repetition
cp "$DEPOT/registres/go.md" "$J/prep/registres/go.md"
printf 'Addendum fictif de répétition (aucune valeur) ; commit du code %s\n' "$CODE" > "$J/prep/prereg/SPARKS-EXP7-NUL-addendum-1.md"
(cd "$J/prep/prereg" && sha256sum SPARKS-EXP7-NUL-addendum-1.md > SPARKS-EXP7-NUL-addendum-1.md.sha256)
T 60 git -C "$J/prep" add -A && T 60 git -C "$J/prep" -c user.name=essai -c user.email=essai@invalid commit -qm "essai : répétition v4 (addendum fictif)"
T 300 git -C "$J/prep" push -q origin essai/sparks-v4-repetition || { echo "poussée de la branche d'essai impossible : arrêt"; exit 2; }
LANCE=$(git -C "$J/prep" rev-parse HEAD); COURT=${LANCE:0:12}
printf '#!/bin/bash\necho "curl $*" >> "%s/faux.log"\nprintf 200\n' "$J" > "$J/faux-bin/curl"; chmod +x "$J/faux-bin/curl"
cp "${HOME}/.gitconfig" "$J/home/.gitconfig" 2>/dev/null || true
PROXY=(); for v in HTTPS_PROXY HTTP_PROXY NO_PROXY https_proxy http_proxy no_proxy GIT_SSL_CAINFO SSL_CERT_FILE REQUESTS_CA_BUNDLE; do
  [ -n "${!v:-}" ] && PROXY+=("$v=${!v}"); done
ENV=(env -i PATH="$J/faux-bin:/usr/bin:/bin" HOME="$J/home" GIT_CONFIG_GLOBAL="$J/home/.gitconfig" "${PROXY[@]}"
     RACINE_AMORCE="$J/racine" MODE=jouet BRANCHE_PREFIXE=essai/ VENV_EXISTANT="$DEPOT/.venv" GO_DATE="$(date -u +%F)"
     COMMIT="$LANCE" COMMIT_CODE="$CODE" GH_TOKEN="${GH_TOKEN:-}" PRIX_HEURE_USD=0.8 PRIX_STOCKAGE_HEURE_USD=0.05
     ECHEANCE_UTC_S=$(( $(date +%s) + 7200 )) CONTAINER_ID=1 CONTAINER_API_KEY=factice DEPOT_URL="$URL")
A="$J/prep-code/scripts/amorce_instance_sparks_exp7_nul_v4.sh"
mkdir -p "$J/prep-code/scripts"; T 60 git -C "$DEPOT" show "$CODE:scripts/amorce_instance_sparks_exp7_nul_v4.sh" > "$A"
etape() { local n="$1"; shift; T 3600 "${ENV[@]}" bash "$A" > "$J/$n.txt" 2>&1; echo "== $n : code $?"
          cat "$J/racine/sparks-v4-minuterie.pid" >> "$J/minuteries.txt" 2>/dev/null || true; }
attendu() { if grep -q -- "$2" "$J/$1.txt"; then echo "   OK   $1 : « $2 »"; else echo "   ÉCART $1 : « $2 » absent"; fi; }
# Dépôt d'ordres à part, branche liée au commit de répétition
O="$J/ordres-depot"; T 60 git init -q "$O"; T 60 git -C "$O" remote add origin "$URL"; mkdir -p "$O/ordres"
ordre() { echo "$2" > "$O/ordres/ordre-$1.json"; T 60 git -C "$O" add ordres && T 60 git -C "$O" -c user.name=essai -c user.email=essai@invalid commit -qm "essai : ordre $1" \
          && T 300 git -C "$O" push -q origin "HEAD:refs/heads/ordres/sparks-exp7-nul-v4-$COURT"; }
# 1. Création : minuterie, GO, borne, durée, garde du code, fabrication jouet (attendu : arrêt de la fabrication jouet)
etape 1-creation
attendu 1-creation "minuterie lancée"; attendu 1-creation "AMORCE V4 : création"; attendu 1-creation "fabrication, durée plafonnée"
# 2. Redémarrage de copie (attendu : ordre lu, borne retenue, « lot impossible » en jouet)
ordre 001 '{"numero": 1, "instance": "1", "phase": "copie", "deja_usd": 1.0, "cas": ["vraie01"], "premier": true, "copie_minutes": 5}'
etape 2-copie
attendu 2-copie "AMORCE V4 : redémarrage"; attendu 2-copie "ordre 1 (copie)"; attendu 2-copie "borne retenue"; attendu 2-copie "lot impossible"
# 3. Redémarrage « causal » (clé et réponses factices ; attendu : branche essai/…-causal-v4-<court>-002, calcul jouet en échec, pas de destruction)
mkdir -p "$O/ordres/causal/reponses" && echo '{}' > "$O/ordres/causal/cle-ouverte-v1.json" && touch "$O/ordres/causal/reponses/.garde"
ordre 002 '{"numero": 2, "instance": "1", "phase": "causal", "deja_usd": 2.0}'
etape 3-causal
attendu 3-causal "ordre 2 (causal)"; attendu 3-causal "sans poussée vérifiée"
# 4. Ordre rejoué (attendu : refus), puis « fin » (attendu : DELETE par la minuterie, curl simulé)
etape 4-rejoue; attendu 4-rejoue "ordre refusé"
ordre 003 '{"numero": 3, "instance": "1", "phase": "fin", "deja_usd": 2.0}'
etape 5-fin
attendu 5-fin "ordre 3 (fin)"; grep -c "DELETE instance 1" "$J/racine/sparks-v4-minuterie.log" | sed 's/^/   DELETE au journal : /'
# 6. Nettoyage : toutes les minuteries par leur numéro (R10), branches distantes d'essai, arbre à part
sort -u "$J/minuteries.txt" 2>/dev/null | while read -r p; do kill "$p" 2>/dev/null && echo "   minuterie $p arrêtée"; done
for b in essai/sparks-v4-repetition "essai/sparks-exp7-nul-v4-$COURT" "essai/sparks-exp7-nul-causal-v4-$COURT-002" "ordres/sparks-exp7-nul-v4-$COURT"; do
  T 300 git -C "$DEPOT" push -q origin --delete "$b" 2>/dev/null && echo "   branche $b supprimée" || echo "   branche $b absente ou non supprimée"; done
T 120 git -C "$DEPOT" worktree remove --force "$J/prep"; T 60 git -C "$DEPOT" branch -D essai/sparks-v4-repetition
echo "sorties : $J/*.txt ; journal de la minuterie : $J/racine/sparks-v4-minuterie.log"
```

Résultat attendu : `OK` sur chaque ligne `attendu`, et `DELETE au journal : 1`. Dans `3-causal`, si la branche
`essai/…-causal-v4-<court>-002` n'existe pas encore, l'échec doit venir du calcul jouet, non d'une « branche déjà
présente ». Tout `ÉCART` se rapporte à la mère, sans correction sur place.

## 6. Dix points pour le contre-lecteur du delta v4 (le premier d'abord)

1. Chaque étape avant le calcul est sous `timeout`, et `borne_t` ne laisse rien allonger.
2. `PM=$!` : c'est le bon processus après `setsid` (pas de fourche quand le shell n'est pas meneur de groupe), et
   l'attente est bornée.
3. Ordres : clé `instance`, consignation avant l'action, `deja_usd` qui ne baisse pas ; format des faits « numéro
   deja_usd ».
4. Borne de la machine : plafonds consignés **avant** le lancement (un démarrage tué compte), et stockage depuis le
   premier démarrage, pas depuis la création chez Vast : l'écart est de quelques minutes.
5. Branches liées au commit et à l'ordre, et refus de tout préfixe autre que `calcul/` ou `essai/`.
6. Lanceur : commandes littérales que la garde de calcul voit ; variables du mandataire passées par leur nom ;
   `apres-creation` (expressions sur la sortie de `vastai`, forme supposée de `new_contract`).
7. Certificat = « non parvenu » sans marqueur : vérifier que ces motifs ne paraissent jamais après une création réussie.
8. Le script d'instance v4 exige `BRANCHE` ; ses gardes ne sont pas mutées (réserve 2).
9. Banc v4 : les 30 mutations neuves et leurs essais ciblés.
10. Répétition : séquence, contrôles, nettoyage, aucune écriture sous `calcul/`.
