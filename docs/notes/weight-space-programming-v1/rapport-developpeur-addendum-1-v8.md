# SPARKS-EXP7-NUL — additif v8 au rapport du développeur (code v8, minimal)

Même rédacteur-développeur. Tâche : message de la mère du 5 novembre 2026 (vers 02:04 UTC), après la répétition v7. Travail
de 02:04 à 03:56 UTC environ, coupé par deux redémarrages du conteneur (`date -u`). Mêmes interdits, tous tenus : aucune poussée, aucun `.sha256` sur `main`, aucun
fichier existant modifié, aucun réseau, aucune dépense, aucune clé lue. Cet additif complète les rapports v5, v6 et v7.

**Verdict.** Code v8 : branche locale `prep/sparks-exp7-nul-v8`, commit `4fd104072bcdf22bb0f5eb1daffca295858f0ac6`. C'est un commit sur `67dbad98`,
avec 20 fichiers neufs et aucun fichier modifié ; la liste fermée v8 (168 fichiers) est conforme. Le manifeste de chaque
phase cite désormais **l'addendum scellé** comme préenregistrement. Comptes : section 4. **Le brouillon 6 demande deux
couples, pas un** (section 3) : il lui manque aussi la section « Hypothèse ».

## 1. Ce que la garde exige, et comment R1 v4 s'en sert

`controle_ia.prereg.exiger_prereg_scelle(chemin)` (appelée par `manifeste.creer_manifeste` dès que `prereg` est donné) :
1. vérifie le sceau (`scellement.verifier` : compagnon `.sha256` au format de `sha256sum`, empreinte égale) ;
2. applique `prereg.problemes`, qui exige :
   - les **huit sections** de `prereg.SECTIONS` : Hypothèse ; Prédiction chiffrée et signe attendu ; Métrique ; Seuil ;
     Plan d'analyse ; Critères de lecture gelés ; Liste d'arrêt ; Contre-lecture ; chacune non vide et sans « À REMPLIR » ;
   - aucun « À REMPLIR » ailleurs, aucun marqueur de gabarit `<<NOM>>` ;
   - à la **« Contre-lecture »** : si elle a des entrées « Contre-lecture k » (en début de ligne, `ENTREE`), **chaque
     entrée porte deux empreintes entières distinctes** (64 chiffres hexadécimaux : brouillon relu et rapport) ; sans
     entrées, la section entière en porte au moins deux.

Le texte parent de SPARKS (`prereg/SPARKS-EXP7-NUL-preenregistrement-v1.md`, `4bacf20d…`) échoue au troisième point : sa
« Contre-lecture » ne cite que des empreintes abrégées. Il est scellé depuis le 4 novembre et ne peut pas changer (R1, R12).

**R1 v4** (`prereg/R1-addendum-relance-v4.md`, `0f10881b…`, branche `prep/r1-relance-v4`, commit de scellement `937f1317`) :
l'addendum porte les huit sections, dont une « Contre-lecture » avec les empreintes entières des deux contre-lectures et de
leurs couples ; le manifeste de chaque run le cite comme `preenregistrement` (le vérificateur de réception
`docs/notes/runs-r1-r2-r4-v1/reception-v4-v1/verifier_reception_r1_v4_v1.py`, l. 104 et 451, exige
`m["preenregistrement"] == {"chemin": "prereg/R1-addendum-relance-v4.md", "sha256": …}`), et les autres textes sont cités
ailleurs dans le manifeste.

## 2. Correction (code v8)

**Nouveau module `controle_ia.sparks_exp7_nul_v8.manifeste_phase`** : le manifeste en ligne (texte sur l'entrée standard) du
script d'instance v7 est remplacé par un appel `module controle_ia.sparks_exp7_nul_v8.manifeste_phase "$RUN_ID" "$DEPART"
"$HTTP" "$PHASE" "$COMMIT_CODE" "$LOTS" "$MODE"`, par la fonction `module` de la v7 (isolement `-I` gardé). Dans l'ordre :
1. **texte parent** vérifié par son seul sceau, et contre l'empreinte gelée `plan.SHA_PREREG` ; cité dans la configuration
   (`texte_parent: {chemin, sha256}`) ;
2. **addendum** (`prereg/SPARKS-EXP7-NUL-addendum-1.md`) exigé ; absent → refus (« le texte parent seul ne gouverne pas ») ;
   aucun repli sur le texte parent ;
3. addendum factice de répétition (marque `addendum_factice.MARQUE`) hors du mode jouet → refus ;
4. addendum qui ne cite pas le commit du code en entier → refus (déjà exigé par la garde du code ; redit ici) ;
5. `creer_manifeste(…, prereg=<addendum>)` : `exiger_prereg_scelle` vérifie sceau et conformité de l'addendum.

Le manifeste porte `preenregistrement = {chemin de l'addendum, son empreinte}`. Les graines restent dérivées de
l'empreinte du texte parent (`plan.entropie_prereg()`), comme en v1 à v7 : aucun tirage ne change. La configuration gagne
trois clés : `mode`, `texte_parent`, `addendum_factice`. Les clés de la v7 restent.

Script d'instance v8 : un refus du manifeste écrit « manifeste refusé (addendum scellé exigé) : arrêt avant tout calcul » au
journal et sort en code 2, avant tout calcul. En v7, l'arrêt venait de `set -e`, en code 1, sans ligne de journal.

**Mode jouet** : `controle_ia.sparks_exp7_nul_v8.addendum_factice` (bibliothèque standard seule, chargeable par son chemin)
écrit un addendum **conforme et marqué factice**, avec son compagnon :
- titre : la marque « ADDENDUM FACTICE DE RÉPÉTITION (mode jouet ; aucune valeur ; jamais scellé au dépôt de travail) » ;
- le commit du code en entier ;
- les huit sections, chacune « Factice (répétition) : aucune valeur… » ;
- une « Contre-lecture factice » avec deux empreintes de chaînes connues, jamais celles d'une pièce réelle ;
- refus d'écraser un fichier existant (R12).

La répétition l'emploie (section 5).

Fichiers neufs, comme en v7 :
- script d'instance v8 ;
- amorce v8, qui emploie la garde v8 et le script d'instance v8 ;
- lanceur v8, qui emploie la garde v8 et l'amorce v8 ;
- garde du code v8 et liste fermée v8 ;
- `manifeste_phase` et `addendum_factice` ;
- essai v8 ;
- banc v8.

**Essais neufs** (`tests/test_sparks_exp7_nul_v8.py`, section 6). Ils jouent les lignes du script v8 (`SRC`, `module`, appel du
manifeste), hors de tout `PYTHONPATH`, dans un dépôt git neuf :
- **commit parent** (texte parent scellé, copié du dépôt, seul) → **refus**, code 2, « texte parent seul », ligne d'arrêt
  au journal, aucun `runs/` créé ; l'appel de la v7 (texte parent cité) y lève aussi « deux empreintes » ;
- **commit enfant** avec l'addendum factice : en jouet → **manifeste créé** :
  - `preenregistrement` = addendum et son empreinte ;
  - `texte_parent` = `4bacf20d…` ;
  - `commit` = le commit enfant ;
  - `addendum_factice` vrai ;

  en réel → **refus** ;
- **commit enfant** avec un addendum conforme non factice : en réel → manifeste créé ;
- addendum **non conforme**, en quatre variantes, chacune refusée :
  - empreintes abrégées ;
  - commit abrégé ;
  - « Hypothèse » absente ;
  - sceau faux ;
- **texte parent altéré** puis rescellé → refus (« empreinte gelée ») ;
- **témoin** : le texte parent réel n'est pas conforme (« deux empreintes ») ;
- l'addendum factice est marqué, conforme, sans écrasement ;
- **contrôle statique** :
  - l'amorce appelle deux fois le script d'instance v8 ;
  - le lanceur passe deux fois l'amorce v8 ;
  - le script lance les essais v8 ;
  - le manifeste passe avant le calcul.

Le contrôle des appels de la v7 compte désormais six appels `module`, sans texte sur l'entrée standard.

**Mutations neuves (11)** :
- `manifeste_phase` :
  - cite le texte parent (l'appel de la v7) ;
  - se replie en silence sur le texte parent sans addendum ;
  - admet l'addendum factice hors du jouet ;
  - n'exige pas le commit du code ;
  - ne vérifie pas le texte parent contre l'empreinte gelée ;
  - ne vérifie que le sceau de l'addendum, pas sa conformité ;
- `addendum_factice` :
  - « Contre-lecture » sans empreintes ;
  - non marqué ;
- script d'instance v8 :
  - refus du manifeste sans arrêt déclaré (`|| true`) ;
  - essais v7 au lieu des essais v8 ;
  - manifeste placé après le calcul.

Les mutations v7 sont rejouées sur les fichiers v8 et l'essai v8 (7 sur 8). La huitième, « manifeste sans src », n'a plus
d'objet : il n'y a plus de texte du manifeste sur l'entrée standard. L'appel `module` du manifeste est couvert par les
mutations « src non posé » et « src relatif ».

**Fichiers et empreintes** (branche `prep/sparks-exp7-nul-v8`, chacun avec son compagnon `.sha256` ; 20 fichiers neufs) :

| Fichier | sha256 |
|---|---|
| `scripts/amorce_instance_sparks_exp7_nul_v8.sh` | `7aca53f8787682bc2ee4fd06f12bd19c0e377868740022b5c6f678e678bfc642` |
| `scripts/banc_mutations_sparks_exp7_nul_v8.py` | `ab539f197cc1048444e18458ba34aea7b60fdef23b16ee850b19526b2c421e6f` |
| `scripts/lancer_sparks_exp7_nul_v8.sh` | `d46244eacb986195c413af7dc538e478d064152c9282c3399c98408abb4c55c6` |
| `scripts/sparks_exp7_nul_instance_v8.sh` | `73f832b124fd28594bed2f5d28b5637543eef65bd0aa6cadfdd37aaac36d4e4f` |
| `src/controle_ia/sparks_exp7_nul_v8/__init__.py` | `d2d11a67fabf6d13aa66b0c8c9471dc32a131669376839d6f3fd5e8e16e5f2f5` |
| `src/controle_ia/sparks_exp7_nul_v8/addendum_factice.py` | `7c82d259d86842c908873d1dc3b08f21b813007b0374c444399d5ef365d1188a` |
| `src/controle_ia/sparks_exp7_nul_v8/garde_code.py` | `b54c2c7d270bf42fc609c111c1e47e04c4447a0675d3bda25b52c455607da4a7` |
| `src/controle_ia/sparks_exp7_nul_v8/liste-fermee-v1.txt` | `9a66b37ab6646b5012317a997a19eaf53061161048a70ea3418d017da9db521d` |
| `src/controle_ia/sparks_exp7_nul_v8/manifeste_phase.py` | `35862365a4e172745e6f0015373474b4a431895e7dbdd1b6f7e60ac75590750f` |
| `tests/test_sparks_exp7_nul_v8.py` | `449e863e4b3016bb4ff184ed2d6a73a9cab31a60606b647a75ff7dcb1d3fd38e` |

`garde_code liste . 4fd10407…` (v8) → « LISTE FERMÉE CONFORME : 168 fichiers ».

## 3. Ce que cela demande au brouillon suivant (brouillon 6) : deux couples

Constat par script : `prereg.problemes` donne, sur le brouillon 5 (`851f75e4…`) :
- `section absente : Hypothèse` ;
- `marqueur À REMPLIR restant hors des sections exigées` (les trois marqueurs gardés, remplis au scellement) ;
- `section Contre-lecture sans les deux empreintes exigées (brouillon relu et rapport)`.

Un couple sur la « Contre-lecture » ne suffit donc pas : l'addendum doit aussi avoir sa section « Hypothèse ». Les deux
couples sont dans `essais-et-banc-sparks-v8/couples-brouillon6-manifeste-v1.json`, sans compagnon, avec leurs empreintes
calculées par script depuis les fichiers :

**Couple 1** : la section « Hypothèse », par renvoi, aucun énoncé changé.
- ancien : `## Prédiction chiffrée et signe attendu\n` ;
- nouveau : `## Hypothèse`, puis : « Inchangée : celle du texte v1 (`prereg/SPARKS-EXP7-NUL-preenregistrement-v1.md`,
  `4bacf20dbb8a0e3f369119841d6fb0b56069d0d31989431238b115df746dd52d`, scellé le 4 novembre 2026), section « Hypothèse »,
  reprise par renvoi ; cet addendum ne change aucun énoncé. La section est écrite ici parce que l'addendum scellé est le
  texte qui gouverne le run : le manifeste de chaque phase le cite comme préenregistrement (code v8,
  `controle_ia.sparks_exp7_nul_v8.manifeste_phase`), et `controle_ia.prereg.exiger_prereg_scelle` exige ses huit
  sections. », puis l'ancien.

**Couple 2** : la « Contre-lecture », avec des empreintes entières au format exigé.
- ancien : `## Contre-lecture\n\n` ;
- nouveau : `## Contre-lecture`, une phrase d'introduction, puis quatre entrées, une par contre-lecture faite. Chaque entrée
  porte, en entier, l'empreinte du brouillon relu et celle du rapport :

| Entrée | Brouillon relu | Rapport |
|---|---|---|
| **Contre-lecture 1** (complète) | brouillon 1 `80e3dc4bbfc58f5183a04ed9468f11d794852e6d8633febbcca109fa111371b2` | `contre-lecture-addendum-1-v1/contre-lecture-addendum-1-v1.md` `c6a82d7e5e33311ec448672e304bb1e42a616aa82308708f26cafe1630616c30` |
| **Contre-lecture 2** (delta v2) | brouillon 2 `7e98397e53784637c03c1f1f7450e582c25939a46d15ca53380ebf8b70958170` | `contre-lecture-delta-v2-v1/contre-lecture-delta-v2-v1.md` `578fd025bf4a46fd075631eb5beed026a8e6f9e5358a15c72e0fc7ff3c2ea9cc` |
| **Contre-lecture 3** (delta v3) | brouillon 3 `12e47e51525e0d820e8bbf599167ac49be12dbc1768b5635569ac027656ac424` | `contre-lecture-delta-v3-v1/contre-lecture-delta-v3-v1.md` `cf2ffcb0d52ed961185ba6750fcfbe138896aa3163fa7a7e9baef1e613048555` |
| **Contre-lecture 4** (delta v4) | brouillon 4 `925c11fe58fe157e2343d5d36b816aacbdeb0f677d63afa50a1c0818323d5f29` | `contre-lecture-delta-v4-v1/contre-lecture-delta-v4-v1.md` `4bc7066e9ccbdb84a9db2e631b3da0200d483d680931e0b730b547355cb1a922` |

Chaque brouillon relu a été vérifié dans le rapport, par son empreinte abrégée : 80e3dc4b, 7e98397e, 12e47e51, 925c11fe.
La prose actuelle de la section reste, sous les entrées.

**Vérification par script**, sur une copie du brouillon 5 hors du dépôt (effacée ensuite) :
- chaque « ancien » est unique ;
- après les deux couples, il ne reste que les trois « À REMPLIR » ;
- trois « À REMPLIR » remplis pour simulation → `problemes` = `[]` ;
- le couple 1 seul → le refus « deux empreintes » reste.

**Au scellement** :
- la contre-lecture du delta à venir (v5 à v8) ajoute une entrée « **Contre-lecture 5** », au même format : brouillon relu
  et rapport, en entier ;
- elle ne prend pas de marqueur « À REMPLIR » dans le brouillon, pour garder les trois marqueurs comptés ;
- la contre-lecture 5 et ses couples doivent être faits par un sous-agent neuf (R2), sur `git diff 53d4eda6..4fd104072bcdf22bb0f5eb1daffca295858f0ac6` et
  les rapports v5 à v8.

## 4. Essais et banc

Fichiers d'essai : `tests/test_sparks_exp7_nul_v1.py` à `v4.py` et `tests/test_sparks_exp7_nul_v8.py`. Sorties brutes copiées sans `.sha256` dans `essais-et-banc-sparks-v8/`.

| Passage | Résultat | Sortie | sha256 |
|---|---|---|---|
| Essais à la tête `4fd10407` | 293 réussis, 0 échec, 0 sauté, code 0 | `essais-tete-4fd10407.txt` | `bdeb832c0039ac8571a9b28400f1b72f258c3b88a702f5aed3f6837204b8cbfc` |
| Essais sur le commit enfant `2a85cf47` (addendum factice v8 écrit par `addendum_factice.py`, `COMMIT_CODE=4fd10407…`) | 293 réussis, 0 échec, 0 sauté, code 0 | `essais-enfant-2a85cf47.txt` | `c67aa6e5ad017b3faf8f409ce0e38734aa84989cc0129c948052fd8efd9e793b` |
| Banc de mutations v8 | 198/198 tuées (code 1 et « failed ») : 22 v1, 52 v2, 40 v3, 30 v4, 30 v5, 6 v6, 7 v7, 11 v8 ; 7 témoins verts ; 0 défaut ; code 0 | `banc-4fd10407.txt` | `6bfbf3a3052ab6500c8a3335408c4c95a1817a040f722d8b93e8bcfda759d47a` |
| Banc, détail | une ligne par mutation | `banc-4fd10407.json` | `ee89fcb0584ccb668adf624e062065fdfc62cf8974c29ab90381c8420c9a0920` |
| Couples du brouillon 6 | 2 couples | `couples-brouillon6-manifeste-v1.json` | `4312524d3b67c4cfc417f23f75b5e02825c04dcd7eed8196dd4c3ed7c160951b` |

Chaque passage a été joué une seule fois, et aucun n'a été écarté (R4). Les 15 essais neufs ont tous réussi du premier coup : c'est le banc qui les éprouve, et ses 11 mutations v8 sont toutes tuées. Le témoin v6 du banc saute un essai, parce que la copie du banc n'est pas un dépôt git. Son pendant dans `test_sparks_exp7_nul_v8.py` passe à la tête comme sur l'enfant, avec 0 sauté.
Réserve (R4) : le résultat est propre. Il prouve la création du manifeste sur des dépôts git neufs construits par l'essai. Une instance réelle n'est éprouvée que par la répétition (section 5) ; le passage local de bout en bout du script d'instance est décrit en fin de section 5.

## 5. Commande de répétition v8

C'est celle de la v7 (`rapport-developpeur-addendum-1-v7.md`, section 4), avec quatre changements :
- `CODE` est le commit v8 ; l'amorce est l'amorce v8 ; la branche d'essai est `essai/sparks-v8-repetition` ;
- **l'addendum fictif** est écrit par `addendum_factice.py`, tiré du commit du code (`git show`) et joué par son chemin ;
  il remplace le `printf` et le `sha256sum` de la v7, car l'ancien texte n'était pas conforme ;
- attendus neufs : « MANIFESTE CRÉÉ » et « ADDENDUM FACTICE (jouet) » au journal de la fabrication et de la phase causale ;
  « MANIFESTE REFUSÉ » absent ;
- attendus de la v7 gardés : « ARRET 0/28 modèles dans les bornes » au `run.err` de la fabrication ; « fin du calcul, code
  [1-9] » à la phase causale ; un seul DELETE.

```bash
#!/usr/bin/env bash
set -uo pipefail
CODE=4fd104072bcdf22bb0f5eb1daffca295858f0ac6
DEPOT=/home/user/controle-ia-travail
URL=https://github.com/lciric/controle-ia-travail.git
J=$(mktemp -d /tmp/repetition-sparks-v8-XXXX); mkdir -p "$J/faux-bin" "$J/racine" "$J/home"
T() { timeout -k 10 "$@"; }
T 600 git -C "$DEPOT" worktree add -q --no-checkout -b essai/sparks-v8-repetition "$J/prep" "$CODE"
T 60 git -C "$J/prep" sparse-checkout set --no-cone '/*' '!/*/' '/prereg/SPARKS-EXP7-NUL-*' '/registres/go.md'
T 600 git -C "$J/prep" checkout -q essai/sparks-v8-repetition
cp "$DEPOT/registres/go.md" "$J/prep/registres/go.md"
T 60 git -C "$DEPOT" show "$CODE:src/controle_ia/sparks_exp7_nul_v8/addendum_factice.py" > "$J/addendum_factice.py"
T 60 python3 -I -B "$J/addendum_factice.py" "$J/prep/prereg/SPARKS-EXP7-NUL-addendum-1.md" "$CODE" \
  || { echo "addendum factice non écrit : arrêt"; exit 2; }
T 60 git -C "$J/prep" add -A && T 60 git -C "$J/prep" -c user.name=essai -c user.email=essai@invalid commit -qm "essai : répétition v8 (addendum factice marqué)"
T 300 git -C "$J/prep" push -q origin essai/sparks-v8-repetition || { echo "poussée de la branche d'essai impossible : arrêt"; exit 2; }
LANCE=$(git -C "$J/prep" rev-parse HEAD); COURT=${LANCE:0:12}
printf '#!/bin/bash\necho "curl $*" >> "%s/faux.log"\nprintf 200\n' "$J" > "$J/faux-bin/curl"; chmod +x "$J/faux-bin/curl"
cp "${HOME}/.gitconfig" "$J/home/.gitconfig" 2>/dev/null || true
PROXY=(); for v in HTTPS_PROXY HTTP_PROXY NO_PROXY https_proxy http_proxy no_proxy GIT_SSL_CAINFO SSL_CERT_FILE REQUESTS_CA_BUNDLE; do
  [ -n "${!v:-}" ] && PROXY+=("$v=${!v}"); done
ENV=(env -i PATH="$J/faux-bin:/usr/sbin:/usr/bin:/sbin:/bin" HOME="$J/home" GIT_CONFIG_GLOBAL="$J/home/.gitconfig" "${PROXY[@]}"
     RACINE_AMORCE="$J/racine" MODE=jouet BRANCHE_PREFIXE=essai/ VENV_EXISTANT="$DEPOT/.venv" GO_DATE="$(date -u +%F)"
     COMMIT="$LANCE" COMMIT_CODE="$CODE" GH_TOKEN="${GH_TOKEN:-}" PRIX_HEURE_USD=0.8 PRIX_STOCKAGE_HEURE_USD=0.05
     ECHEANCE_UTC_S=$(( $(date +%s) + 7200 )) CONTAINER_ID=1 CONTAINER_API_KEY=factice DEPOT_URL="$URL")
A="$J/amorce-v8.sh"; T 60 git -C "$DEPOT" show "$CODE:scripts/amorce_instance_sparks_exp7_nul_v8.sh" > "$A"
etape() { T 3600 unshare -pf --mount-proc "${ENV[@]}" bash "$A" > "$J/$1.txt" 2>&1; echo "== $1 : code $?"; }
attendu() { if grep -qE -- "$3" "$2"; then echo "   OK   $1 : « $3 »"; else echo "   ÉCART $1 : « $3 » absent de $2"; fi; }
absent() { if grep -qE -- "$3" "$2" 2>/dev/null; then echo "   ÉCART $1 : « $3 » présent dans $2"; else echo "   OK   $1 : pas de « $3 »"; fi; }
O="$J/ordres-depot"; T 60 git init -q "$O"; T 60 git -C "$O" remote add origin "$URL"; mkdir -p "$O/ordres"
ordre() { echo "$2" > "$O/ordres/ordre-$1.json"; T 60 git -C "$O" add ordres && T 60 git -C "$O" -c user.name=essai -c user.email=essai@invalid commit -qm "essai : ordre $1" \
          && T 300 git -C "$O" push -q origin "HEAD:refs/heads/ordres/sparks-exp7-nul-v5-$COURT"; }
etape 1-creation
attendu 1 "$J/1-creation.txt" "AMORCE V5 : outils : curl oui, git oui, unshare oui, chroot oui"
attendu 1 "$J/1-creation.txt" "mode jouet : addendum non exigé"
attendu 1 "$J/1-creation.txt" "fabrication, durée plafonnée"
attendu 1 "$J/racine/sparks/journal.txt" "essais : [0-9]+ passed"
attendu 1 "$J/racine/sparks/journal.txt" "essai d'égalité des lots : oui"
attendu 1 "$J/racine/sparks/journal.txt" "MANIFESTE CRÉÉ : runs/.*préenregistrement prereg/SPARKS-EXP7-NUL-addendum-1.md"
attendu 1 "$J/racine/sparks/journal.txt" "ADDENDUM FACTICE \(jouet\)"
absent  1 "$J/racine/sparks/journal.txt" "MANIFESTE REFUSÉ|manifeste refusé"
attendu 1 "$J/racine/sparks/journal.txt" "manifeste runs/"
absent  1 "$J/racine/sparks/run.err" "No module named"
attendu 1 "$J/racine/sparks/run.err" "ARRET 0/28 modèles dans les bornes"
attendu 1 "$J/racine/sparks-v5-demarrages.txt" "^d [0-9]+ [0-9]+$"
ordre 001 '{"numero": 1, "instance": "1", "phase": "copie", "deja_usd": 1.0, "cas": ["vraie01"], "premier": true, "copie_minutes": 5}'
etape 2-copie
attendu 2 "$J/2-copie.txt" "ordre 1 \(copie\)"
attendu 2 "$J/2-copie.txt" "sans modèles dans les bornes"
attendu 2 "$J/2-copie.txt" "lot impossible"
mkdir -p "$O/ordres/causal/reponses" && echo '{}' > "$O/ordres/causal/cle-ouverte-v1.json" && touch "$O/ordres/causal/reponses/.garde"
ordre 002 '{"numero": 2, "instance": "1", "phase": "causal", "deja_usd": 2.0}'
etape 3-causal
attendu 3 "$J/3-causal.txt" "ordre 2 \(causal\)"
attendu 3 "$J/racine/sparks-causal-002/journal.txt" "essais : [0-9]+ passed"
attendu 3 "$J/racine/sparks-causal-002/journal.txt" "MANIFESTE CRÉÉ : runs/.*préenregistrement prereg/SPARKS-EXP7-NUL-addendum-1.md"
absent  3 "$J/racine/sparks-causal-002/journal.txt" "MANIFESTE REFUSÉ|manifeste refusé"
absent  3 "$J/racine/sparks-causal-002/run.err" "No module named"
attendu 3 "$J/racine/sparks-causal-002/journal.txt" "fin du calcul, code [1-9]"
attendu 3 "$J/3-causal.txt" "sans poussée vérifiée"
etape 4-rejoue; attendu 4 "$J/4-rejoue.txt" "ordre refusé"
ordre 003 '{"numero": 3, "instance": "1", "phase": "fin", "deja_usd": 2.0}'
etape 5-fin; attendu 5 "$J/5-fin.txt" "ordre 3 \(fin\)"
echo "   DELETE au journal : $(grep -c 'DELETE instance 1 ' "$J/racine/sparks-v5-minuterie.log") (attendu : 1)"
if pgrep -f "$J/racine/sparks-v5-minuterie.sh" >/dev/null; then echo "   ÉCART : minuterie restante"; else echo "   OK   aucune minuterie restante"; fi
echo "   branches à supprimer par Lazar : essai/sparks-v8-repetition essai/sparks-exp7-nul-v5-$COURT essai/sparks-exp7-nul-causal-v5-$COURT-002 ordres/sparks-exp7-nul-v5-$COURT"
T 120 git -C "$DEPOT" worktree remove --force "$J/prep"; T 60 git -C "$DEPOT" branch -D essai/sparks-v8-repetition
echo "sorties : $J/*.txt ; journal de la minuterie : $J/racine/sparks-v5-minuterie.log"
```

Résultat attendu : `OK` sur chaque ligne, et `DELETE au journal : 1 (attendu : 1)`. Les lignes attendues comprennent :
- « MANIFESTE CRÉÉ » et « ADDENDUM FACTICE (jouet) » au journal de la fabrication ;
- « ARRET 0/28 modèles dans les bornes » au `run.err` de la fabrication ;
- « MANIFESTE CRÉÉ » et « fin du calcul, code [1-9] » au journal de la phase causale.

Le code de la phase causale est non nul, parce que le départ « jouet » n'est pas un modèle publié : c'est l'échec voulu du
calcul jouet.

**Passage local de bout en bout du script d'instance v8**, sans amorce, en mode jouet et sans réseau. Les runs sont tous comptés (R4).

Dispositif :
- dépôt nu local : il emprunte les objets du dépôt de travail (`alternates`), et sa frontière superficielle est recopiée ;
- `DEPOT_URL=file://…` ;
- commit lancé : l'enfant `2a85cf47` ;
- `COMMIT_CODE=4fd10407…` ;
- `VENV_EXISTANT` : `.venv` du dépôt ;
- `env -i`.

Ce passage ne remplace pas la répétition : ni l'amorce, ni la minuterie, ni GitHub ne sont joués.

- **Fabrication (1 run, complet, code 3)**. Le journal donne, dans l'ordre :
  - « LANCEMENT CONFORME : code 4fd104072bcd, addendum 8fd57d1bff4b » ;
  - « essais : 293 passed » ;
  - « EGALITE LOTS OK » ;
  - « MANIFESTE CRÉÉ : runs/20261105-024300-sparks-exp7-nul-v5-fabrication/manifeste.json ; préenregistrement
    prereg/SPARKS-EXP7-NUL-addendum-1.md (8fd57d1bff4b…) ; texte parent 4bacf20dbb8a… ; ADDENDUM FACTICE (jouet) » ;
  - au `run.err` : « ARRET 0/28 modèles dans les bornes (< 90 %) : recette non reproduite » ;
  - « fin du calcul, code 3 » ;
  - sorties scellées, puis commit « SPARKS-EXP7-NUL v8 : fabrication (jouet), code 3 » ;
  - « poussée vérifiée ».

  Le manifeste porte :
  - `preenregistrement` = addendum, `8fd57d1b…` ;
  - `texte_parent` = `4bacf20d…` ;
  - `addendum_factice` vrai ;
  - `depot_propre` vrai.

  Un défaut du dispositif local, pas du code : le dépôt de travail est superficiel. Le clone partiel a donc écrit des
  avertissements « shallow roots » et un échec de récupération à la demande. Le clone, la garde et le calcul ont abouti.
- **Phase causale (2 runs, coupés tous deux par un redémarrage du conteneur, sans code de fin)**. Les deux journaux
  donnent « essais : 293 passed », puis « MANIFESTE CRÉÉ : runs/…-sparks-exp7-nul-v5-causal/manifeste.json ;
  préenregistrement prereg/SPARKS-EXP7-NUL-addendum-1.md (8fd57d1bff4b…) ; texte parent 4bacf20dbb8a… ; ADDENDUM FACTICE
  (jouet) ». Ces deux runs ont été lancés à 02:56 et à 03:42 UTC.

  Le calcul causal jouet et sa fin, « fin du calcul, code [1-9] », ne sont pas observés ici. Sur consigne de la mère, je ne
  les rejoue pas : la répétition les éprouve.

**Tir réel** : la commande de la section 5 du rapport v5 vaut avec le lanceur v8 et le commit v8. Il faut d'abord sceller le
brouillon 6, avec ses deux couples et la contre-lecture 5 :

```
cd /home/claude/wt/sparks-exp7-nul-v8
SPARKS_REGISTRE_GO=/home/user/controle-ia-travail/registres/go.md \
  bash scripts/lancer_sparks_exp7_nul_v8.sh tir <OFFRE> <PRIX_CARTE> <PRIX_STOCKAGE> 4fd104072bcdf22bb0f5eb1daffca295858f0ac6 <GO_ID_DU_TIR> 25
```
