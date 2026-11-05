# SPARKS-EXP7-NUL — rapport du rédacteur-développeur : brouillon 5 de l'addendum n° 1 et code v5

Même rédacteur-développeur que pour les brouillons 2 à 4 (sous-agent Claude, Opus 5.5) ; il n'a écrit aucune
contre-lecture.

- **Tâche** : message de la mère du 4 novembre 2026 (vers 23:58 UTC), après la contre-lecture du delta v4.
- **Contre-lecture lue en entier**, avec ses démonstrations :
  `docs/notes/weight-space-programming-v1/contre-lecture-delta-v4-v1/contre-lecture-delta-v4-v1.md`, sha256
  `4bc7066e9ccbdb84a9db2e631b3da0200d483d680931e0b730b547355cb1a922`. Les huit compagnons du dossier sont « OK ».
- **Durée** : du 4 novembre à 23:55 UTC au 5 novembre vers 00:50 UTC (`date -u`), avec une coupure par un redémarrage
  du conteneur vers 00:12.
- **Interdits respectés** : aucune poussée, aucun `.sha256` sur `main`, aucun fichier existant modifié, aucun réseau,
  aucune dépense. Moins de 40 Mo employés ; les fichiers temporaires sont nettoyés.

**Verdict.**
- Code v5 : branche locale `prep/sparks-exp7-nul-v5`, commit `b7d342ef9ac1b2dc2633feaa1116b5dd7302e926`. C'est un commit
  sur `53d4eda6`, avec 22 fichiers neufs et aucun fichier modifié ; la liste fermée v5 (116 fichiers) est conforme.
- Les neuf changements de la contre-lecture sont faits, dont le mode « tir » du lanceur, avec sa commande écrite
  (section 5).
- Essais et banc : section 3.
- Brouillon 5 : les 8 couples sont tous retenus, puis M-1 à M-5 ; les trois marqueurs restent.
- Commande de la répétition : section 6.

## 1. Fichiers et empreintes

Sur `main` (fichiers neufs, sans compagnon) :

| Fichier | sha256 |
|---|---|
| `prereg/SPARKS-EXP7-NUL-addendum-1-brouillon5.md` | `851f75e4d07baa096cce28419b0b67e1725684d90f4d3d35e57e0dff90a4e63d` |
| `docs/notes/weight-space-programming-v1/brouillon5-addendum-1-v1/appliquer-couples-addendum-1-brouillon5-v1.py` | `9e6f4f434904d6150e25416a0aa9986a3fcf472e85b528c48d4399ef637d3b34` |
| `docs/notes/weight-space-programming-v1/brouillon5-addendum-1-v1/sortie-appliquer-couples-addendum-1-brouillon5-v1.txt` | `11a79c3e63daf2a610fd355baf5664aa09edc4c84714d7db9ea8ca74a43cf218` |
| `docs/notes/weight-space-programming-v1/essais-et-banc-sparks-v5/` (sorties brutes) | section 3 |
| ce rapport | — |

Le script vérifie ses entrées : brouillon 4 `925c11fe…`, couples `68230e9a…`.
- Il applique L1 à L8 dans l'ordre. Le texte intermédiaire, `56992343ecb410ed…`, est **égal au texte d'essai du
  contre-lecteur**.
- Il applique ensuite M-1 à M-5 : en-tête, table 00000, compléments de la liste de code v5, contre-lecture, pied.
- M-3 écrit que le tir tourne sous une ligne de GO à part, posée par la mère, avec `GO_ID` en paramètre et un plafond
  écrit d'au plus 5 USD. C'est la réponse au nœud du point 4 de la contre-lecture : l'extension de GO-2026-11-04-04 dit
  « scellé avant tout lancement ».

Sur `prep/sparks-exp7-nul-v5` (chaque fichier avec son compagnon `.sha256`) :

| Fichier | sha256 |
|---|---|
| `scripts/amorce_instance_sparks_exp7_nul_v5.sh` | `c44a45de52cf43ee64aeaffaa1759c2f4f732eb27bb7c301bdd43952b45f6715` |
| `scripts/banc_mutations_sparks_exp7_nul_v5.py` | `22c244185a53ac4e7b324bb64167160d0ed3d25261b798e9d7df048423286ee5` |
| `scripts/lancer_sparks_exp7_nul_v5.sh` | `103b8a66bba55f1b6a92e20db8433b29ee2c0043b6f7ad34bef5bba2f27948c3` |
| `scripts/sparks_exp7_nul_instance_v5.sh` | `e490ff13953c26b8bd8cfbb6ad2517f008cac83b525eeb30141f68acffbc9a58` |
| `src/controle_ia/sparks_exp7_nul_v5/__init__.py` | `7c14050e9dbd210a5ca764f1e74d605f4e7d3a285646aeefe67ae00ac48e8a0c` |
| `src/controle_ia/sparks_exp7_nul_v5/garde_code.py` | `28b7b37071c4497b572da86fa9cbe146715d4abbb62af738360566aebbdc67cf` |
| `src/controle_ia/sparks_exp7_nul_v5/liste-fermee-v1.txt` | `fee4d799ab8ed0c6dd18fb9bd6485eef53f9752ffc42d6df099115fbe0789442` |
| `src/controle_ia/sparks_exp7_nul_v5/plan.py` | `21a1f332cd78c50b0c9f8125aaf77e032affb21f5e693f484c4d44786a30ec43` |
| `src/controle_ia/sparks_exp7_nul_v5/redemarrage.py` | `84a52cb0e8a67a0fad781153addfb854cf83701959c47e5f9fa9d0aecd5b0247` |
| `src/controle_ia/sparks_exp7_nul_v5/tir.py` | `da55dd19dadabe45532286f040bc407dc1c48203045832fee013364f0fcf3a18` |
| `tests/test_sparks_exp7_nul_v5.py` | `c846787885530ae14e6c9c22cef68720c6112cf3a0b627872a8808b7de55d48e` |

`garde_code liste . b7d342ef…` (v5) → « LISTE FERMÉE CONFORME : 116 fichiers ».

## 2. Les neuf changements

1. **`VAST_API_KEY`** est transmise à `vastai` par son nom, dans l'`env -i` du lanceur. L'essai le vérifie : le
   sous-processus la reçoit, et sa valeur n'est jamais imprimée.
2. **Lecture des sorties de `vastai`.**
   - `apres-creation` teste l'identifiant avec « success » vrai **avant** le certificat. Le cas mixte du contre-lecteur
     donne « CRÉÉE ». Un refus avec le code 0 (R-1506) donne « INCERTAINE », marqueur posé.
   - `apres-commande start|destroy` lit la sortie, jamais affichée : certificat → « non parvenu » ; motif de refus
     (`failed with error`, `"success": false`, …) → « REFUSÉ » ; sinon « ENVOYÉ, rien n'est tenu pour fait ». Il imprime
     ensuite la commande d'inventaire.
   - `inventaire` (`vastai show instance <id> --raw`) n'imprime que l'identifiant et l'état (`actual_status`,
     `cur_state`), comparés à l'attendu (`absente`, `exited` ou `running`).
3. **Durée réelle.**
   - Registre `p <ident> <plafond>` avant le lancement, `d <ident> <minutes réelles>` à la fin (`consigner_fin`).
   - La borne prend la durée réelle, ou le plafond s'il n'y a pas de fin. Une fin sans plafond, ou une ligne illisible :
     refus.
   - Essai au coin haut du devis (création le 5 à 12:00, fabrication réelle de 6 h, 18 copies de 30 min, prix
     0,80/0,05) : la phase causale reste admise, ≥ 60 min.
4. **Addendum reconnu en mode réel** (`addendum_reconnu`, après la garde du code).
   - Il faut l'empreinte attendue, passée à la création (`ADDENDUM_SHA256`, calculée par le lanceur au commit lancé), ou
     un commit lancé **contenu dans** `origin/main`.
   - Lecture retenue, déclarée : « contenu dans », et non « descendant », car une branche d'essai peut descendre de
     `main`. La mutation « descendant » est tuée.
   - En jouet, l'addendum n'est pas exigé.
   - Marqueur `sparks-v5-gardes-ok` : sans lui, un redémarrage n'exécute qu'un ordre « fin ». La copie et le causal sont
     refusés, ce qui ferme le trou du point 21.
5. **Amorce prise par `git show "$COMMIT:…"`** dans la commande de création, et par `git show "$CODE:…"` dans le tir.
6. **Minuterie.**
   - Le corps du `DELETE` est gardé (`sparks-v5-delete-corps.txt`). Un `"success": false` n'est pas un succès.
   - Aucune tentative ne part si maintenant + 190 s dépasse la fin de la marge.
   - Témoin au journal si la minuterie d'un démarrage antérieur vit encore.
   - Ligne « outils » : présence de `unshare`, `chroot`, `prlimit` et `vastai`, lisible au journal du tir.
7. **Mode « tir » du lanceur** : section 5.
8. **Répétition corrigée** : section 6.
9. **Mutations** : 30 neuves, sur les points 12 et 14 à 24 de la contre-lecture, en plus des 144 du banc v4. Deux essais
   statiques ont été ajoutés pour que les mutations de l'ordre des gardes et du bloc « tir » soient tuées même dans la
   copie du banc, qui n'est pas un dépôt `git`.

## 3. Essais et banc (commit `b7d342ef`)

Sorties brutes dans `essais-et-banc-sparks-v5/` (même dossier que ce rapport) :

| Mesure | Compte | Sortie (sha256) |
|---|---|---|
| Essais v1 à v4 (inchangés) et v5 (52 cas) | **278 passés sur 278** (90 + 69 + 38 + 29 + 52), 0 sauté, 0 échec | `essais-b7d342ef.txt` `e16a248a…` |
| Banc v5 : mutations des bancs v1 à v4 | **22/22, 52/52, 40/40, 30/30 tuées** (code 1 et « failed ») | `banc-b7d342ef.txt` `08bcf44d…`, `.json` `3c168a16…` |
| Banc v5 : mutations neuves de la v5 | **30/30 tuées** ; cinq témoins verts ; 0 inapplicable | idem |

Tout run est compté (R4).
- Le premier passage complet des essais au commit `b7d342ef`, lancé avant le redémarrage du conteneur (vers 00:12 UTC),
  a été coupé : sortie partielle gardée au bloc-notes, sans fin ni compte. Les essais et le banc ont été relancés en
  entier ensuite.
- Avant le commit, pendant le développement, j'ai fait des passages partiels des essais v5 jusqu'au vert. Trois défauts
  y sont apparus et ont été corrigés : le registre lisait mal une ligne vide ou fautive ; dans `apres-commande`, le
  certificat était lu après le refus, et le motif « Error: » l'emportait ; le faux `curl` de l'essai du corps du `DELETE`
  était recopié.
- Un passage complet avant le commit a donné 277 passés et 1 sauté (l'essai du tir, la liste fermée v5 n'étant pas encore
  au commit).

## 4. Réserves

1. **Formes de sortie de `vastai` supposées.**
   - « Absente » est reconnue sur `no_such_instance`, `not found`, `404` ou une liste vide. Toute autre forme donne
     « illisible », que la session tranche.
   - L'état est lu sur `actual_status`.
   - Le tir doit les confirmer.
2. **`vastai copy` n'est pas éprouvé par le tir** : sans fabrication il n'y a aucun lot, et le conteneur est sorti.
   Risque déclaré, comme le redémarrage quand la carte de l'hôte est louée par un autre.
3. **Les gardes du script d'instance ne sont pas mutées** au banc (poussée vérifiée, préfixe) : elles ne se jouent qu'à
   la répétition.
4. **L'échéance du tir** est fixée à l'impression de la commande (maintenant + 20 à 30 min). Il faut créer dans les
   5 minutes, sinon réimprimer.
5. **Les branches d'essai** (`essai/sparks-v5-tir-…`, `ordres/sparks-exp7-nul-v5-…`) restent sur le dépôt distant, à
   supprimer par Lazar : le mandataire refuse les suppressions (contre-lecture v4, point 21).

## 5. Commande du tir réel (sous une ligne de GO neuve posée par la mère)

À jouer depuis la session mère, après la contre-lecture du delta v5, une fois la ligne de GO du tir posée dans
`registres/go.md` de `main` : type « calcul », accordée par Lazar, plafond **au plus 5 USD**, validité couvrant le jour du
tir.

Ce que le tir doit éprouver, et l'étape qui le montre :
- `DELETE` par la clé du conteneur, puis inventaire « absente » : étapes 4 et 5 ;
- `curl` et `git` dans l'image : étape 2, ligne « outils » (sans eux, l'amorce refuse et le dit) ;
- relance par `vastai start` avec le même environnement : étape 4, voie « redémarrage », ordre lu ;
- conteneur qui sort quand l'amorce sort : inventaire « exited » de l'étape 2 ;
- facturation d'une instance « exited » : champs filtrés de l'étape 2 ;
- `vastai copy` : non éprouvé (réserve 2).

Prix et offre sont relevés au moment du tir.

```bash
cd /home/claude/wt/sparks-exp7-nul-v5        # ou tout arbre de prep/sparks-exp7-nul-v5 relié au dépôt
SPARKS_REGISTRE_GO=/home/user/controle-ia-travail/registres/go.md \
  bash scripts/lancer_sparks_exp7_nul_v5.sh tir <OFFRE> <PRIX_CARTE_USD_H> <PRIX_STOCKAGE_USD_H> \
  b7d342ef9ac1b2dc2633feaa1116b5dd7302e926 <GO_ID_DU_TIR> 25
```

Le lanceur vérifie :
- la liste fermée du code ;
- la ligne de GO du tir (`tir.py` : type « calcul », Lazar, validité, révocation, plafond ≤ 5 USD) ;
- le devis du tir sous ce plafond : carte × (25 + 15 + 10) min + stockage × (25 + 60) min, soit 0,74 USD à 0,80/0,05.

Il imprime ensuite les étapes. Exemple rendu avec une ligne de GO fictive `GO-2026-11-05-99` (sortie réelle du
lanceur, l'échéance changeant à chaque impression) :

```
0. Commit de tir (code b7d342ef9ac1 + registre des GO de main, SANS addendum : la création s'arrête d'elle-même à la garde du code) :
   T=$(mktemp -d); git worktree add -q --no-checkout -b essai/sparks-v5-tir-b7d342ef9ac1 "$T/tir" b7d342ef9ac1b2dc2633feaa1116b5dd7302e926
   git -C "$T/tir" sparse-checkout set --no-cone '/*' '!/*/' '/registres/go.md' && git -C "$T/tir" checkout -q essai/sparks-v5-tir-b7d342ef9ac1
   cp "/home/user/controle-ia-travail/registres/go.md" "$T/tir/registres/go.md" && git -C "$T/tir" commit -qam "essai : tir v5 (sans addendum)" && timeout 300 git -C "$T/tir" push -q origin essai/sparks-v5-tir-b7d342ef9ac1
   TIR=$(git -C "$T/tir" rev-parse HEAD)
1. Création (échéance de la minuterie dans 25 min ; étiquette de tir ; disque réduit) :
GO_ID=<GO_ID_DU_TIR> timeout -k 10 300 env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 VAST_API_KEY="$VAST_API_KEY" HTTPS_PROXY="$HTTPS_PROXY" vastai create instance <OFFRE> --image pytorch/pytorch:2.9.1-cuda12.8-cudnn9-runtime --disk 20 --label sparks-exp7-nul-tir-b7d342ef9ac1 \
  --env "-e COMMIT=$TIR -e COMMIT_CODE=b7d342ef9ac1b2dc2633feaa1116b5dd7302e926 -e PRIX_HEURE_USD=… -e PRIX_STOCKAGE_HEURE_USD=… -e ECHEANCE_UTC_S=<maintenant + 25 min> -e GH_TOKEN=$GH_TOKEN -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git" \
  --args bash -c "$(git show "b7d342ef9ac1b2dc2633feaa1116b5dd7302e926:scripts/amorce_instance_sparks_exp7_nul_v5.sh")" > "$HOME/.sparks-exp7-nul-v5/tir-creation-….txt" 2>&1; bash scripts/lancer_sparks_exp7_nul_v5.sh apres-creation "$HOME/.sparks-exp7-nul-v5/tir-creation-….txt" $?
   ID=<identifiant rendu>
2. Après 5 à 8 min : inventaire attendu « exited » (le conteneur sort quand l'amorce sort) ; lignes « AMORCE V5 » du journal ; champs de facturation filtrés.
3. Ordre « fin » pour cette instance, sur la branche ordres/sparks-exp7-nul-v5-${TIR:0:12} (dépôt d'ordres à part).
4. Relance : GO_ID=<GO_ID_DU_TIR> timeout -k 10 300 env -i … vastai start instance $ID > "…/tir-start.txt" 2>&1; bash scripts/lancer_sparks_exp7_nul_v5.sh apres-commande start "…/tir-start.txt" $? $ID
5. Après 3 à 5 min : inventaire attendu « absente » (destruction par la machine, aucune par la session).
6. Repli si l'instance existe encore à l'échéance + 10 min : bash scripts/lancer_sparks_exp7_nul_v5.sh destruction $ID.
7. vastai copy : non éprouvé par ce tir ; risque déclaré.
Devis : 0.7375 USD au plus (à 0,80/0,05), sous <GO_ID_DU_TIR>.
```

Les variables du mandataire (`HTTPS_PROXY`, et les autres présentes) et `VAST_API_KEY` apparaissent par leur nom
seulement.

Ce qu'il faut voir :
- étape 1 : « CRÉÉE : instance … » ;
- étape 2 : « INVENTAIRE : … état exited », puis la ligne « AMORCE V5 : outils : curl oui, git oui, … » et « code ou
  addendum non conformes » ;
- étape 4 : « start … ENVOYÉ » ;
- étape 5 : « INVENTAIRE : … état absente ».

Tout autre résultat se rapporte à la mère, sans correction sur place.

## 6. Répétition jouet corrigée (session mère, reliée au dépôt distant)

Corrections, avec le point de la contre-lecture v4 :
- `/usr/sbin` et `/sbin` dans le PATH (19) ;
- chaque démarrage dans son propre espace de processus (`unshare -pf --mount-proc`), si bien que les minuteries meurent
  avec leur démarrage (20) ;
- attendus précis (19) ;
- aucune tentative de tuer des minuteries par des numéros relevés dans un espace de processus à part (R10 : ces numéros
  ne désignent rien hors de lui) : on vérifie seulement qu'aucune ne reste ;
- branches d'essai listées pour Lazar (21).

Conséquence à connaître : la branche `essai/sparks-v5-repetition` pousse au dépôt distant les commits du code v2 à v5.

```bash
#!/usr/bin/env bash
set -uo pipefail
CODE=b7d342ef9ac1b2dc2633feaa1116b5dd7302e926
DEPOT=/home/user/controle-ia-travail
URL=https://github.com/lciric/controle-ia-travail.git
J=$(mktemp -d /tmp/repetition-sparks-v5-XXXX); mkdir -p "$J/faux-bin" "$J/racine" "$J/home"
T() { timeout -k 10 "$@"; }
T 600 git -C "$DEPOT" worktree add -q --no-checkout -b essai/sparks-v5-repetition "$J/prep" "$CODE"
T 60 git -C "$J/prep" sparse-checkout set --no-cone '/*' '!/*/' '/prereg/SPARKS-EXP7-NUL-*' '/registres/go.md'
T 600 git -C "$J/prep" checkout -q essai/sparks-v5-repetition
cp "$DEPOT/registres/go.md" "$J/prep/registres/go.md"
printf 'Addendum fictif de répétition (aucune valeur) ; commit du code %s\n' "$CODE" > "$J/prep/prereg/SPARKS-EXP7-NUL-addendum-1.md"
(cd "$J/prep/prereg" && sha256sum SPARKS-EXP7-NUL-addendum-1.md > SPARKS-EXP7-NUL-addendum-1.md.sha256)
T 60 git -C "$J/prep" add -A && T 60 git -C "$J/prep" -c user.name=essai -c user.email=essai@invalid commit -qm "essai : répétition v5 (addendum fictif)"
T 300 git -C "$J/prep" push -q origin essai/sparks-v5-repetition || { echo "poussée de la branche d'essai impossible : arrêt"; exit 2; }
LANCE=$(git -C "$J/prep" rev-parse HEAD); COURT=${LANCE:0:12}
printf '#!/bin/bash\necho "curl $*" >> "%s/faux.log"\nprintf 200\n' "$J" > "$J/faux-bin/curl"; chmod +x "$J/faux-bin/curl"
cp "${HOME}/.gitconfig" "$J/home/.gitconfig" 2>/dev/null || true
PROXY=(); for v in HTTPS_PROXY HTTP_PROXY NO_PROXY https_proxy http_proxy no_proxy GIT_SSL_CAINFO SSL_CERT_FILE REQUESTS_CA_BUNDLE; do
  [ -n "${!v:-}" ] && PROXY+=("$v=${!v}"); done
ENV=(env -i PATH="$J/faux-bin:/usr/sbin:/usr/bin:/sbin:/bin" HOME="$J/home" GIT_CONFIG_GLOBAL="$J/home/.gitconfig" "${PROXY[@]}"
     RACINE_AMORCE="$J/racine" MODE=jouet BRANCHE_PREFIXE=essai/ VENV_EXISTANT="$DEPOT/.venv" GO_DATE="$(date -u +%F)"
     COMMIT="$LANCE" COMMIT_CODE="$CODE" GH_TOKEN="${GH_TOKEN:-}" PRIX_HEURE_USD=0.8 PRIX_STOCKAGE_HEURE_USD=0.05
     ECHEANCE_UTC_S=$(( $(date +%s) + 7200 )) CONTAINER_ID=1 CONTAINER_API_KEY=factice DEPOT_URL="$URL")
A="$J/amorce-v5.sh"; T 60 git -C "$DEPOT" show "$CODE:scripts/amorce_instance_sparks_exp7_nul_v5.sh" > "$A"
etape() { T 3600 unshare -pf --mount-proc "${ENV[@]}" bash "$A" > "$J/$1.txt" 2>&1; echo "== $1 : code $?"; }
attendu() { if grep -qE -- "$3" "$2"; then echo "   OK   $1 : « $3 »"; else echo "   ÉCART $1 : « $3 » absent de $2"; fi; }
O="$J/ordres-depot"; T 60 git init -q "$O"; T 60 git -C "$O" remote add origin "$URL"; mkdir -p "$O/ordres"
ordre() { echo "$2" > "$O/ordres/ordre-$1.json"; T 60 git -C "$O" add ordres && T 60 git -C "$O" -c user.name=essai -c user.email=essai@invalid commit -qm "essai : ordre $1" \
          && T 300 git -C "$O" push -q origin "HEAD:refs/heads/ordres/sparks-exp7-nul-v5-$COURT"; }
# 1. Création : outils, minuterie, GO, borne, durée, garde du code, addendum non exigé en jouet ; fabrication jouet arrêtée à « 0/28 »
etape 1-creation
attendu 1 "$J/1-creation.txt" "AMORCE V5 : outils : curl oui, git oui, unshare oui, chroot oui"
attendu 1 "$J/1-creation.txt" "mode jouet : addendum non exigé"
attendu 1 "$J/1-creation.txt" "fabrication, durée plafonnée"
attendu 1 "$J/racine/sparks/run.err" "ARRET 0/28 modèles dans les bornes"
attendu 1 "$J/racine/sparks-v5-demarrages.txt" "^d [0-9]+ [0-9]+$"
# 2. Copie : ordre lu, borne sur la durée réelle, lot refusé car aucun modèle dans les bornes
ordre 001 '{"numero": 1, "instance": "1", "phase": "copie", "deja_usd": 1.0, "cas": ["vraie01"], "premier": true, "copie_minutes": 5}'
etape 2-copie
attendu 2 "$J/2-copie.txt" "ordre 1 \(copie\)"
attendu 2 "$J/2-copie.txt" "sans modèles dans les bornes"
attendu 2 "$J/2-copie.txt" "lot impossible"
# 3. Causal : branche essai/…-causal-v5-<court>-002 neuve, calcul jouet en échec (départ « jouet »), pas de destruction
mkdir -p "$O/ordres/causal/reponses" && echo '{}' > "$O/ordres/causal/cle-ouverte-v1.json" && touch "$O/ordres/causal/reponses/.garde"
ordre 002 '{"numero": 2, "instance": "1", "phase": "causal", "deja_usd": 2.0}'
etape 3-causal
attendu 3 "$J/3-causal.txt" "ordre 2 \(causal\)"
attendu 3 "$J/racine/sparks-causal-002/journal.txt" "fin du calcul, code [1-9]"
attendu 3 "$J/3-causal.txt" "sans poussée vérifiée"
# 4. Ordre rejoué : refus ; 5. fin : un seul DELETE (chaque minuterie meurt avec son démarrage)
etape 4-rejoue; attendu 4 "$J/4-rejoue.txt" "ordre refusé"
ordre 003 '{"numero": 3, "instance": "1", "phase": "fin", "deja_usd": 2.0}'
etape 5-fin; attendu 5 "$J/5-fin.txt" "ordre 3 \(fin\)"
echo "   DELETE au journal : $(grep -c 'DELETE instance 1 ' "$J/racine/sparks-v5-minuterie.log") (attendu : 1)"
# 6. Contrôles de fin : aucune minuterie restante ; branches d'essai à supprimer par Lazar ; arbre à part retiré
if pgrep -f "$J/racine/sparks-v5-minuterie.sh" >/dev/null; then echo "   ÉCART : minuterie restante"; else echo "   OK   aucune minuterie restante"; fi
echo "   branches à supprimer par Lazar : essai/sparks-v5-repetition essai/sparks-exp7-nul-v5-$COURT essai/sparks-exp7-nul-causal-v5-$COURT-002 ordres/sparks-exp7-nul-v5-$COURT"
T 120 git -C "$DEPOT" worktree remove --force "$J/prep"; T 60 git -C "$DEPOT" branch -D essai/sparks-v5-repetition
echo "sorties : $J/*.txt ; journal de la minuterie : $J/racine/sparks-v5-minuterie.log"
```

Résultat attendu : `OK` sur chaque ligne et `DELETE au journal : 1 (attendu : 1)`. Tout `ÉCART` se rapporte à la mère.

## 7. Dix points pour le contre-lecteur du delta v5 (le premier d'abord)

1. Mode « tir » : le commit de tir est le code plus le registre de `main`, sans addendum. La création doit s'arrêter à la
   garde du code, et l'ordre « fin » doit passer, car il ne demande pas le marqueur des gardes. Vérifier qu'aucun chemin
   du tir ne calcule.
2. `tir.py` : plafond ≤ 5 USD, formule du devis, bornes de durée, validité et révocation de la ligne de GO.
3. `addendum_reconnu` : empreinte, ou commit **contenu dans** `origin/main` (lecture retenue, à confirmer) ; et l'exemption
   en jouet.
4. Marqueur `sparks-v5-gardes-ok` : seul un ordre « fin » vaut sans lui.
5. Registre `p` et `d` : la durée réelle remplace le plafond seulement pour un démarrage qui a une fin ; il n'existe aucun
   chemin où une fin plus courte serait écrite par erreur.
6. Lanceur : ordre « identifiant, puis certificat » ; `apres-commande` (certificat, puis refus, puis envoyé) ; motifs de
   refus et d'absence (forme réelle à confirmer au tir).
7. Minuterie : corps du `DELETE` et borne de 190 s.
8. `VAST_API_KEY` passée par son nom ; aucune valeur imprimée.
9. Répétition : attendus et contrôle de fin des minuteries.
10. Banc v5 : les 30 neuves, et les deux essais statiques qui les tuent hors d'un dépôt `git`.
