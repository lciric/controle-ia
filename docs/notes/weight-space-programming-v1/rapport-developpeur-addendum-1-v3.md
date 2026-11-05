# SPARKS-EXP7-NUL — rapport du rédacteur-développeur : brouillon 3 de l'addendum n° 1 et code v3

Même rédacteur-développeur que pour le brouillon 2 et le code v2 (sous-agent Claude, Opus 5.5) ; il n'a écrit aucune
contre-lecture. Tâche : message de la mère du 4 novembre 2026 (≈ 22:15 UTC) après la contre-lecture du delta v2
(`docs/notes/weight-space-programming-v1/contre-lecture-delta-v2-v1/contre-lecture-delta-v2-v1.md`, sha256
`578fd025bf4a46fd075631eb5beed026a8e6f9e5358a15c72e0fc7ff3c2ea9cc`, lue en entier ; six compagnons du dossier « OK »).
Travail du 4 novembre, 22:15 → 23:00 UTC environ (`date -u`). Aucune poussée, aucun `.sha256` sur `main`, aucun fichier
existant modifié, aucun réseau, aucun modèle, aucune dépense ; disque : moins de 50 Mo employés, fichiers temporaires
nettoyés.

**Verdict.** Code v3 : branche locale `prep/sparks-exp7-nul-v3`, commit `4c3bf146498df471cd8615f035db9d9bb2c771fa` (un
commit sur `50fb15cd`), 26 fichiers neufs, aucun modifié ; liste fermée v3 de 74 fichiers (v2 et v3) conforme. Les six
changements de la contre-lecture sont faits. Essais : 197 passés sur 197. Banc : section 3. Le brouillon 3 est écrit par
script (11 couples, puis G-1 à G-6 ; trois marqueurs). La répétition jouet complète reste à jouer depuis une session
reliée au dépôt distant (section 5).

## 1. Fichiers et empreintes

Sur `main` (fichiers neufs, sans compagnon) :

| Fichier | sha256 |
|---|---|
| `prereg/SPARKS-EXP7-NUL-addendum-1-brouillon3.md` | `12e47e51525e0d820e8bbf599167ac49be12dbc1768b5635569ac027656ac424` |
| `docs/notes/weight-space-programming-v1/brouillon3-addendum-1-v1/appliquer-couples-addendum-1-brouillon3-v1.py` | `00ef58330eaa0f0dbffdf0568ebe9d1921b3d28fca1fd76b3e163a729e54c5a2` |
| `docs/notes/weight-space-programming-v1/brouillon3-addendum-1-v1/sortie-appliquer-couples-addendum-1-brouillon3-v1.txt` | `3dd51187411d8fb67bc5163595e309f4a304a85631f1519e6eb05e0b0c920fd7` |
| `docs/notes/weight-space-programming-v1/essais-et-banc-sparks-v3/` (sorties brutes des essais et du banc) | section 3 |
| ce rapport | — |

Le script vérifie ses entrées (brouillon 2 `7e98397e…`, couples `58321f8d…`) et applique les 11 couples dans l'ordre,
chacun unique au moment de son application. Après eux, le texte a l'empreinte `e5535c9658dab08f…`, **égale au texte
d'essai du contre-lecteur** (`e5535c96…`). Viennent ensuite G-1 à G-6 : en-tête, table 000, lignes A-22 et A-23,
section « Minuterie de destruction et redémarrages », compléments de la liste de code v3, contre-lecture et pied. Le
script refuse d'écraser la sortie et exige trois marqueurs « À REMPLIR ». Incident (R4) : une première sortie portait
une heure de début fausse (« 22:40 », dans le futur, saisie à la main) ; je l'ai effacée aussitôt, sans qu'elle soit lue
ni versée (`5a13694f…`), puis j'ai rejoué le script avec l'heure de `date -u` (22:28).

Sur la branche `prep/sparks-exp7-nul-v3` (chaque fichier avec son compagnon `.sha256`) :

| Fichier | sha256 |
|---|---|
| `scripts/amorce_instance_sparks_exp7_nul_v3.sh` | `b4edf787663f2eba66e07f1acece43b9b9e796953f3d36987cafb49d1796871c` |
| `scripts/banc_mutations_sparks_exp7_nul_v3.py` | `fb23aa9a0833f284e13d0f76f1c4db05b98ff1551f10566ed071e49b547ca002` |
| `scripts/lancer_sparks_exp7_nul_v3.sh` | `b42e9865154961912d27340512420783010e4b9f187ad793b7149be0911e94aa` |
| `scripts/sparks_exp7_nul_instance_v3.sh` | `ac2752dbadd99b9d540828a98cccb6e7f4836d1d31261ee3c84c10a9052e91ee` |
| `src/controle_ia/sparks_exp7_nul_v3/__init__.py` | `1f414bd0df775593b305ac7c5215427496ce1ad6f3cb0b87f05b5e6ff6f09f5c` |
| `src/controle_ia/sparks_exp7_nul_v3/analyse.py` | `e4cd3c0f32d8942ffd0dc0708c679a8d191d88997a183610c27c34eb2b78a556` |
| `src/controle_ia/sparks_exp7_nul_v3/bases.py` | `5c09e60f1821557df382b9ff93f1653118bcb416b0174bc33078d7b395bbec7f` |
| `src/controle_ia/sparks_exp7_nul_v3/garde_code.py` | `af3ea1e85c86cda7d1cf5a43f3f67b647b541e38cef42a7bacfb860351a59767` |
| `src/controle_ia/sparks_exp7_nul_v3/instance.py` | `e1b9313d74b23bee07f8108150b76ec980d9917300caed567b0eddc05e542113` |
| `src/controle_ia/sparks_exp7_nul_v3/liste-fermee-v1.txt` | `e7ca6eec5d62f0caf6e593c84ed8ff540b5c2e92b508111aef083dd04583a24e` |
| `src/controle_ia/sparks_exp7_nul_v3/plan.py` | `07bd273ad47c0b8f6f85974638f1775af55d3b417b544a3ecada9120255eab5b` |
| `src/controle_ia/sparks_exp7_nul_v3/redemarrage.py` | `be002e25ddca88550d1282520d7208ccaac36d0bba2b91e9f70ddaafc77a50b5` |
| `tests/test_sparks_exp7_nul_v3.py` | `3c6c9fec364fb48e32ee61aadd650802890ae726677a146fa9a384377c871897` |

Les 48 fichiers de la v2 sont inchangés : empreintes dans `rapport-developpeur-addendum-1-v2.md`.
`garde_code liste . 4c3bf146…` (v3) → « LISTE FERMÉE CONFORME : 74 fichiers ».

## 2. Les six changements, fonction par fonction

Les modules v3 sont **minces** : ils importent la v2 et ne redéfinissent que ce qui change. Le code déjà éprouvé par les
essais et le banc de la v2 reste donc celui qui tourne.

1. **Chemin de redémarrage.**
   - L'amorce v3 distingue création et redémarrage. Au redémarrage, elle exige que le commit du disque soit `COMMIT`,
     revoit le GO à la date, puis lit l'ordre à la tête de `calcul/sparks-exp7-nul-v3-ordres` (`git fetch --depth 1`,
     puis `git archive`).
   - `redemarrage.py` (bibliothèque standard seule) : `lire_ordre` (phases copie, causal ou fin ; clés fermées ; numéro
     égal au nom du fichier ; bornes) ; `dernier_ordre` ; `exiger_nouveau` et `marquer_fait` (un ordre déjà fait est
     refusé) ; `modeles_du_cas` (remplacements et pilotes) ; `preparer_lot` (liens en dur, manifeste d'empreintes,
     premier lot avec les couches du départ).
   - Le champ `deja_usd` de l'ordre est **relu à chaque démarrage** pour `depense duree`. Une copie est refusée sous
     `copie_minutes` + 5 minutes ; la phase causale sous 60 minutes.
   - La phase causale prend la clé et les réponses dans `ordres/causal/`. Le script d'instance v3 vérifie la poussée
     (`git ls-remote` égal à la tête locale) et écrit alors `POUSSEE-VERIFIEE`.
2. **Minuterie de destruction sur la machine**, écrite dans l'amorce elle-même (texte entre `<<'MINUTERIE'` et
   `MINUTERIE`), en bash et `curl` seuls, lancée par `setsid` avant tout clone.
   - L'échéance absolue `ECHEANCE_UTC_S` est posée à la création, au plus `1795046400` (fin du 18), et gardée sur le
     disque.
   - La destruction part à l'échéance ou sur le fichier `sparks-v3-detruire` : `DELETE /instances/<CONTAINER_ID>/`, et
     en repli `vastai destroy instance <id> -y`, sortie jetée, seul le code de retour est journalisé. Elle recommence
     chaque minute pendant 30 minutes, puis écrit une alarme.
   - Identifiant non numérique : aucun geste. Aucun arrêt de la machine : quand une destruction est due, le processus
     principal attend la fin de la minuterie (`attendre_minuterie`).
   - Sans `curl` ou sans `git`, refus visible. Un démarrage après l'échéance ne calcule rien.
   - Modèle suivi : la sonde A1-v3 v4 (`sonde_hote_durable_a1_v3_v4.py`, `MINUTERIE`). Le script de démarrage de la sonde
     y installe `curl` ; ici l'amorce l'exige, comme le demande la consigne.
3. **Secondaire « sur M5 »** : `analyse.m5_secondaire` (M5 par c_b, par la base et par le lecteur). `analyse.analyser`
   v3 est celui de la v2, complété après coup, sans aucun tirage de plus : les intervalles de la v2 sont égaux à l'octet,
   ce que vérifie un essai.
4. **A priori de B3** : `bases.orientation_b3(…, a_priori)` vaut −1 au construit inversé ; égalité : l'a priori est
   gardé. `etalonnage_b3_b4(…, a_priori)` le reçoit, et `instance.a_priori_b3` et `bases_etalonnage` le transmettent ;
   `fabriquer` et `main` sont redéfinis pour appeler ces versions.
5. **Égalité des jetons** : essai `jetons_texte(format_conversation(tok) avec le message)` = `apply_chat_template(…,
   tokenize=True)`, sur le jouet avec et sans jeton de début. Artefact : la sortie brute du gabarit, qui garde le jeton
   de début, diffère bien.
6. **Banc v3** : 22 mutations v1, 50 v2 et 2 de plus sur la v2 (compte des bases, cas sans bases), plus 40 neuves
   (minuterie, amorce et lanceur en shell, redémarrages, M5, a priori, gardes de la v2 listées au point 26). Une
   mutation n'est **« tuée » qu'au code 1 avec « failed »** ; témoins verts exigés.
   - `garde_code` v3 charge la v2 par son chemin, pour rester importable seule, et lit la liste v3.
   - Le lanceur v3 traite la création et le redémarrage, imprime la commande littérale, refuse une échéance au-delà du
     18 et donne la destruction avec `-y`.

## 3. Essais et banc (commit `4c3bf146`)

Sorties brutes dans `essais-et-banc-sparks-v3/` (même dossier que ce rapport) :

| Mesure | Compte | Sortie (sha256) |
|---|---|---|
| Essais v1, v2 (inchangés) et v3 (38 cas) | **197 passés sur 197** (90 + 69 + 38), 0 sauté, 0 échec | `essais-4c3bf146.txt` `88d73184…` |
| Banc v3 : mutations du banc v1 (essais v1) | **22/22 tuées** (code 1 et « failed ») | `banc-4c3bf146.txt` `b6f9fb37…`, `.json` `e041a1e0…` |
| Banc v3 : mutations du banc v2 et deux de plus (essais v2) | **52/52 tuées** | idem |
| Banc v3 : mutations neuves (minuterie, amorce, lanceur, redémarrages, M5, a priori, point 26) | **40/40 tuées** ; trois témoins verts ; 0 inapplicable | idem |

Tout run est compté (R4) : un seul passage des essais et un seul banc à ce commit, tous deux complets. Avant le commit,
un passage des seuls essais v3 (35 passés, 1 sauté, la liste n'étant pas encore écrite) et un passage complet (196 et
1 sauté) ont servi au développement.

## 4. Ce que la v3 ne règle pas (réserves)

1. **Aucune exécution réelle.**
   - La minuterie n'a jamais appelé l'interface de Vast : `curl` et `vastai` étaient simulés, et la forme de la réponse
     du `DELETE` reste supposée. Un **tir réel** est exigé avant la création (R-1477).
   - L'image `pytorch/pytorch:2.9.1-cuda12.8-cudnn9-runtime` n'est pas vérifiée pour `curl` et `git` ; l'amorce refuse
     s'ils manquent.
2. **Le stockage de l'instance arrêtée n'est pas borné par la machine** (écrit au brouillon 3) : il ne l'est que par une
   session ou par le démarrage suivant.
3. **Le script d'instance v3 n'a pas été joué**, même en jouet (clone de 2,4 Go, section 5). En jouet, la fabrication
   s'arrête à « 0/28 dans les bornes », comme en v1 et v2. La copie d'un lot jouet échoue donc à « sans modèles dans les
   bornes », et la phase causale jouet échoue au chargement de `--depart jouet` : la répétition exerce la plomberie
   (minuterie, ordres, refus, poussée), pas les calculs.
4. **La branche des ordres porte un nom fixe** (`calcul/sparks-exp7-nul-v3-ordres`). Après la répétition, il faut la
   **supprimer** avant la vraie création : sinon un ordre d'essai de numéro plus élevé serait le « dernier ordre » d'un
   vrai redémarrage.
5. Le contrôle causal par lot de la v2 et l'étape 0 réelle sont inchangés et n'ont jamais tourné.

## 5. Commande exacte de la répétition jouet complète (session reliée au dépôt distant)

À jouer **après** la contre-lecture du delta v3 et avant le scellement, depuis un arbre clairsemé de
`prep/sparks-exp7-nul-v3`, avec un GO si la mère juge que la poussée de branches d'essai l'exige.

```bash
set -euo pipefail
CODE=4c3bf146498df471cd8615f035db9d9bb2c771fa        # commit du code (à remplacer par le commit final s'il change)
W=/home/claude/wt/sparks-exp7-nul-v3
J=$(mktemp -d /tmp/repetition-sparks-v3-XXXX); mkdir -p "$J/faux-bin" "$J/racine"
# 0. Branche d'essai (jamais main) : addendum FICTIF scellé + registre des GO de main.
git -C "$W" checkout -q -b essai/sparks-v3-repetition "$CODE"
cp /home/user/controle-ia-travail/registres/go.md "$W/registres/go.md"
printf 'Addendum fictif de répétition (aucune valeur) ; commit du code %s\n' "$CODE" > "$W/prereg/SPARKS-EXP7-NUL-addendum-1.md"
(cd "$W/prereg" && sha256sum SPARKS-EXP7-NUL-addendum-1.md > SPARKS-EXP7-NUL-addendum-1.md.sha256)
git -C "$W" add -A && git -C "$W" commit -qm "essai : répétition jouet v3 (addendum fictif)" && git -C "$W" push -q origin essai/sparks-v3-repetition
LANCE=$(git -C "$W" rev-parse HEAD)
# curl simulé : aucun appel réel à Vast pendant la répétition (le tir réel est une épreuve à part, R-1477)
printf '#!/bin/bash\necho "curl $*" >> "%s/faux.log"\nprintf 200\n' "$J" > "$J/faux-bin/curl"; chmod +x "$J/faux-bin/curl"
ENV=(env -i PATH="$J/faux-bin:/usr/bin:/bin" HOME="$J" RACINE_AMORCE="$J/racine" MODE=jouet BRANCHE=essai/sparks-v3-jouet
     VENV_EXISTANT=/home/user/controle-ia-travail/.venv GO_DATE="$(date -u +%F)" COMMIT="$LANCE" COMMIT_CODE="$CODE"
     GH_TOKEN="$GH_TOKEN" PRIX_HEURE_USD=0.8 PRIX_STOCKAGE_HEURE_USD=0.05 ECHEANCE_UTC_S=$(( $(date +%s) + 7200 ))
     CONTAINER_ID=1 CONTAINER_API_KEY=factice DEPOT_URL=https://github.com/lciric/controle-ia-travail.git)
# 1. Création : minuterie lancée, GO, durée, garde du code, fabrication jouet (attendu : code 3, « 0/28 dans les bornes »)
"${ENV[@]}" bash "$W/scripts/amorce_instance_sparks_exp7_nul_v3.sh" 2>&1 | tee "$J/1-creation.txt"
# 2. Redémarrage de copie : ordre 1 sur la branche des ordres (attendu : « lot impossible » en jouet, refus visible)
O="$J/ordres-depot"; git init -q "$O"; git -C "$O" remote add origin https://github.com/lciric/controle-ia-travail.git
pousser_ordre() { git -C "$O" add ordres && git -C "$O" -c user.name=essai -c user.email=essai@invalid commit -qm "essai : $1" \
                  && git -C "$O" push -q origin HEAD:refs/heads/calcul/sparks-exp7-nul-v3-ordres; }
mkdir -p "$O/ordres"
echo '{"numero": 1, "phase": "copie", "deja_usd": 1.0, "cas": ["vraie01"], "premier": true, "copie_minutes": 5}' > "$O/ordres/ordre-001.json"
pousser_ordre "ordre 1"
"${ENV[@]}" bash "$W/scripts/amorce_instance_sparks_exp7_nul_v3.sh" 2>&1 | tee "$J/2-copie.txt"
# 3. Redémarrage « causal » (clé et réponses factices) puis « fin » : la destruction passe par le curl simulé
mkdir -p "$O/ordres/causal/reponses" && echo '{}' > "$O/ordres/causal/cle-ouverte-v1.json" && touch "$O/ordres/causal/reponses/.garde"
echo '{"numero": 2, "phase": "causal", "deja_usd": 2.0}' > "$O/ordres/ordre-002.json"
pousser_ordre "ordre 2"
"${ENV[@]}" bash "$W/scripts/amorce_instance_sparks_exp7_nul_v3.sh" 2>&1 | tee "$J/3-causal.txt"   # attendu : pas de destruction (pas de poussée vérifiée)
echo '{"numero": 3, "phase": "fin", "deja_usd": 2.0}' > "$O/ordres/ordre-003.json"
pousser_ordre "ordre 3"
"${ENV[@]}" bash "$W/scripts/amorce_instance_sparks_exp7_nul_v3.sh" 2>&1 | tee "$J/4-fin.txt"; grep DELETE "$J/racine/sparks-v3-minuterie.log"
# 4. Nettoyage OBLIGATOIRE avant la vraie création : la branche des ordres d'essai doit disparaître
git -C "$W" checkout -q prep/sparks-exp7-nul-v3
git -C "$W" push -q origin --delete calcul/sparks-exp7-nul-v3-ordres essai/sparks-v3-repetition essai/sparks-v3-jouet
kill "$(cat "$J/racine/sparks-v3-minuterie.pid")" 2>/dev/null || true    # minuterie restante, par son PID (R10)
```

Ce qu'il faut voir :
- 1 : « minuterie lancée » avant « création », « GO CONFORME », « LANCEMENT CONFORME », puis code 3 de la fabrication
  jouet ;
- 2 : « redémarrage », « ordre 1 (copie) », « lot impossible » ;
- 3 : « ordre 2 (causal) », échec du calcul jouet, « sans poussée vérifiée » ;
- 4 : « ordre 3 (fin) », `DELETE instance 1` au journal de la minuterie.

Avant la création réelle : tir réel de la minuterie sur une petite instance (R-1477), suivant
`amorce_sonde_hote_durable_a1_v3_v4.sh`.

## 6. Dix points pour le contre-lecteur du delta v3 (le premier d'abord)

1. Minuterie : la boucle d'attente, le drapeau, le `DELETE`, le repli `-y`, l'alarme ; aucun chemin où le code arrête
   la machine.
2. `attendre_minuterie` : le principal reste en vie tant que la minuterie détruit, sans attendre au-delà de la marge.
3. Échéance : posée à la création, bornée à `1795046400`, relue du disque ensuite (l'environnement est ignoré).
4. Ordres : validation fermée, refus d'un ordre rejoué, ordre consigné fait **avant** l'action (un échec ne se rejoue
   pas), `deja_usd` relu.
5. Lot de copie : liens en dur, manifeste, premier lot ; cas absents ou hors bornes refusés.
6. Phase causale : clé et réponses par la branche des ordres ; destruction seulement après poussée vérifiée.
7. Création : ordre des gardes (GO, durée, code) et refus avant tout calcul.
8. `analyse` v3 : le M5 secondaire ne change aucun tirage.
9. `bases` et `instance` v3 : a priori transmis au seul construit inversé.
10. Banc v3 : « tuée » au seul code 1 ; pas de mutation possible sur le script d'instance v3 (non jouable ici).

## 7. Ce qui reste avant le scellement

Contre-lecture du delta v3 (`git diff 50fb15cd..4c3bf146`) ; répétition jouet (section 5) ; tir réel de la minuterie ;
brouillon 4 avec les trois éléments de la section 2 (commit final, liste fermée v3 et empreintes, comptes ci-dessus) ;
scellement.
