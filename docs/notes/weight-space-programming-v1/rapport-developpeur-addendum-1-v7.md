# SPARKS-EXP7-NUL — additif v7 au rapport du développeur (code v7, minimal)

Même rédacteur-développeur. Tâche : message de la mère du 5 novembre 2026 (vers 01:30 UTC), après la répétition v6. Travail de 01:30 à
02:40 UTC environ (`date -u`). Mêmes interdits, tous tenus : aucune poussée, aucun `.sha256` sur `main`, aucun fichier
existant modifié, aucun réseau, aucune dépense ; moins de 20 Mo employés. Cet additif complète les rapports v5 et v6.

**Verdict.** Code v7 : branche locale `prep/sparks-exp7-nul-v7`, commit `67dbad98df37b7f283913c0e489853a8a690b2f8`. C'est
un commit sur `f18837d1`, avec 16 fichiers neufs et aucun fichier modifié ; la liste fermée v7 (148 fichiers) est conforme.
Le script d'instance v7 trouve le paquet à chaque appel, sans perdre l'isolement `-I`. Comptes : section 3.

## 1. Défaut, portée, correction

**Défaut, confirmé.** `-I` vaut `-E -s -P` : Python ignore `PYTHONPATH` et ne met pas le dossier courant dans le chemin.
Le script d'instance exporte `PYTHONPATH=src`, puis appelle `python -I -B -m controle_ia…` : le module est introuvable.
Reproduit ici :
- `PYTHONPATH=src python -I -B -m controle_ia.scellement` → `ModuleNotFoundError: No module named 'controle_ia'` ;
- même échec pour un script lu sur l'entrée standard (`python -I -B - <<'PY'`), qui est le manifeste.

Pytest passe, parce qu'il pose lui-même `src` (configuration du dépôt).

**Portée : les scripts d'instance v1 à v6, tous.**

| Appel | Scripts touchés |
|---|---|
| Essai d'égalité des lots (`-m … egalite-lots`) | v2 à v6 |
| Manifeste (`python -I -B - … <<'PY'`) | v1 à v6 |
| Calcul (`-m … instance jouet\|fabriquer\|causal`) | v1 à v6 |
| Scellement des sorties (`-m controle_ia.scellement`) | v1 à v6 |

Les amorces et les lanceurs ne sont pas touchés. Ils appellent `python3 -I -B -c "import sys; sys.path.insert(0, '<dossier>'); …"` ou un fichier par son chemin, ou `PYTHONPATH=src python3 -B -m …`, sans `-I`.

**Correction, et pourquoi celle-ci.** Le script d'instance v7 définit une fonction `module NOM ARGS…` :

```
SRC="$PWD/src"   # le script est alors dans le clone, $DEPOT : chemin absolu
module() { python -u -I -B -c 'import runpy, sys; sys.path.insert(0, sys.argv[1]); n = sys.argv[2]; sys.argv = [n] + sys.argv[3:]; runpy.run_module(n, run_name="__main__", alter_sys=True)' "$SRC" "$@"; }
```

Les cinq appels passent par elle : lots, jouet, fabrication, causal, scellement. Le manifeste reçoit `"$SRC"` comme premier
argument et le pose en tête du chemin (`sys.path.insert(0, sys.argv.pop(1))`).

Raisons du choix :
1. **L'isolement est gardé.** Restent ignorés `PYTHON*` (dont un `PYTHONPATH` hérité), le site de l'utilisateur et le
   dossier courant, qui pourraient faire charger un autre code.
2. **Le seul ajout est un chemin absolu, explicite et fixe** : celui du clone extrait au commit vérifié.
3. `runpy.run_module(…, run_name="__main__", alter_sys=True)` est le mécanisme même de `-m` : le module s'exécute à
   l'identique, `argv` compris.
4. **Écartés** :
   - retirer `-I` : on perd l'isolement ;
   - `-P` seul : `PYTHONPATH` reste lu ;
   - installer le paquet (`pip install -e`) : cela change l'environnement de l'instance et demande le réseau à chaque
     installation ;
   - `cd src` : le dossier courant est retiré par `-I` de toute façon.

Fichiers neufs, comme pour la v6 : script d'instance v7, amorce v7 (garde v7, script d'instance v7), lanceur v7 (garde v7,
amorce v7), garde du code v7 et liste fermée v7, essai v7, banc v7.

**Essais neufs** (`tests/test_sparks_exp7_nul_v7.py`) :
- **Cas sain** : l'essai lit dans le script v7 la définition de `SRC` et de `module`, et la ligne du premier appel (essai
  d'égalité des lots). Il les joue depuis un autre dossier, **sans aucun `PYTHONPATH`**, avec le même interpréteur
  isolé. Il exige « EGALITE LOTS OK » et `LOTS=oui`.
- **Témoin de la cause** : l'ancien appel, `python -I -B -m … egalite-lots` avec `PYTHONPATH=src`, échoue sur
  `No module named 'controle_ia'`.
- **Manifeste** : la tête du texte entre `<<'PY'` et `PY`, jouée sous `-I` depuis un autre dossier, importe
  `controle_ia.manifeste`.
- **Contrôle statique** : aucun `python -I -B -m controle_ia` ne reste, et cinq appels `module controle_ia.` sont présents.

**Mutations neuves (8)** :
- l'ancien appel des lots ;
- `src` non posé ;
- `src` relatif ;
- l'ancien appel du calcul jouet ;
- le manifeste sans `src` ;
- l'ancien appel du scellement ;
- l'amorce v7 qui appelle le script v6 ;
- le lanceur v7 qui passe l'amorce v6.

## 2. Fichiers et empreintes (branche `prep/sparks-exp7-nul-v7`, chacun avec son compagnon)

| Fichier | sha256 |
|---|---|
| `scripts/amorce_instance_sparks_exp7_nul_v7.sh` | `0b4dbd18c7f84b13509e40fa2e87290a759f1bd18da340fbb8e42328f501efbd` |
| `scripts/banc_mutations_sparks_exp7_nul_v7.py` | `b72e98ef096417e5bc5f8bc9f71a7183b518609753599708bb99e5a90f266746` |
| `scripts/lancer_sparks_exp7_nul_v7.sh` | `6b0dd89a614e44386ba19719f5ef3c3eb65cb15503aafde578576a2e2ce6d847` |
| `scripts/sparks_exp7_nul_instance_v7.sh` | `d3bfc400cb3ebb3ebbdd07e2e7c9a6e3318c4f2139a714328ecd1683e38ca7a5` |
| `src/controle_ia/sparks_exp7_nul_v7/__init__.py` | `e2a8196c7366ddd0de62764d96439027b4d69113536692b83277e58cdb5a7fc6` |
| `src/controle_ia/sparks_exp7_nul_v7/garde_code.py` | `bca34389efa472c5f1055691f9b5b03030a0661f581e47dd13b6eb401d6c9c41` |
| `src/controle_ia/sparks_exp7_nul_v7/liste-fermee-v1.txt` | `44a784a58581c9335cedc4b38acbd7a3ccfc89711fcb8e84305a594591ba6d86` |
| `tests/test_sparks_exp7_nul_v7.py` | `bcdf1a64a344641a3599f8ed0130a4545eefabe9b77896811b66991d83782c2b` |

`garde_code liste . 67dbad98…` (v7) → « LISTE FERMÉE CONFORME : 148 fichiers ».

## 3. Essais et banc

Fichiers d'essai : `tests/test_sparks_exp7_nul_v1.py` à `v4.py` et `tests/test_sparks_exp7_nul_v7.py`. Sorties brutes copiées sans `.sha256` dans `essais-et-banc-sparks-v7/`.

| Passage | Résultat | Sortie | sha256 |
|---|---|---|---|
| Essais à la tête `67dbad98` | 283 réussis, 0 échec, 0 sauté, code 0 | `essais-tete-67dbad98.txt` | `216f787f4cf3a989e80aca1fd58b99232efdeb07120ae62753e941653b6b0358` |
| Essais sur le commit enfant `733df998` (addendum factice, `COMMIT_CODE=67dbad98…`) | 283 réussis, 0 échec, 0 sauté, code 0 | `essais-enfant-733df998.txt` | `8c6b79a9ef680325bbe7b1b3995dfc7d16831cdb1e8936c12ee69de52402fec0` |
| Banc de mutations v7 | 188/188 tuées (code 1 et « failed ») : 22 v1, 52 v2, 40 v3, 30 v4, 30 v5, 6 v6, 8 v7 ; 7 témoins verts ; 0 défaut ; code 0 | `banc-67dbad98.txt` | `8a5d8f8d293468371df28a3baa2edd17f21614460f16f531e921944ee6370a3f` |
| Banc, détail | une ligne par mutation | `banc-67dbad98.json` | `cd72641bfb74083108883cc0eb0f5426fdcfa12aaac8c50d3c5c3fd6cbab9306` |

Les essais ont été passés une seule fois à la tête, une fois sur l'enfant et une fois au banc. Aucun passage n'a été écarté (R4).
Le témoin v6 du banc saute un essai : la copie du banc n'est pas un dépôt git et cet essai en exige un. Son pendant dans `test_sparks_exp7_nul_v7.py` passe à la tête comme sur l'enfant (0 sauté). Les 8 mutations v7 sont tuées par les quatre essais neufs et par l'essai statique v7.
Réserve (R4) : le résultat est entièrement propre. Il ne prouve que ceci : le paquet est trouvé sous `-I` pour les cinq appels et pour le manifeste, en mode jouet sur processeur. La fabrication et la phase causale réelles ne sont vérifiées que par la répétition (section 4).

## 4. Commande de répétition v7

C'est celle de la v6 (`rapport-developpeur-addendum-1-v6.md`, section 5), avec quatre changements :
- `CODE` est le commit v7 ;
- l'amorce est l'amorce v7 ;
- la branche d'essai est `essai/sparks-v7-repetition` ;
- les attendus du calcul sont rendus explicites.

```bash
#!/usr/bin/env bash
set -uo pipefail
CODE=67dbad98df37b7f283913c0e489853a8a690b2f8
DEPOT=/home/user/controle-ia-travail
URL=https://github.com/lciric/controle-ia-travail.git
J=$(mktemp -d /tmp/repetition-sparks-v7-XXXX); mkdir -p "$J/faux-bin" "$J/racine" "$J/home"
T() { timeout -k 10 "$@"; }
T 600 git -C "$DEPOT" worktree add -q --no-checkout -b essai/sparks-v7-repetition "$J/prep" "$CODE"
T 60 git -C "$J/prep" sparse-checkout set --no-cone '/*' '!/*/' '/prereg/SPARKS-EXP7-NUL-*' '/registres/go.md'
T 600 git -C "$J/prep" checkout -q essai/sparks-v7-repetition
cp "$DEPOT/registres/go.md" "$J/prep/registres/go.md"
printf 'Addendum fictif de répétition (aucune valeur) ; commit du code %s\n' "$CODE" > "$J/prep/prereg/SPARKS-EXP7-NUL-addendum-1.md"
(cd "$J/prep/prereg" && sha256sum SPARKS-EXP7-NUL-addendum-1.md > SPARKS-EXP7-NUL-addendum-1.md.sha256)
T 60 git -C "$J/prep" add -A && T 60 git -C "$J/prep" -c user.name=essai -c user.email=essai@invalid commit -qm "essai : répétition v7 (addendum fictif)"
T 300 git -C "$J/prep" push -q origin essai/sparks-v7-repetition || { echo "poussée de la branche d'essai impossible : arrêt"; exit 2; }
LANCE=$(git -C "$J/prep" rev-parse HEAD); COURT=${LANCE:0:12}
printf '#!/bin/bash\necho "curl $*" >> "%s/faux.log"\nprintf 200\n' "$J" > "$J/faux-bin/curl"; chmod +x "$J/faux-bin/curl"
cp "${HOME}/.gitconfig" "$J/home/.gitconfig" 2>/dev/null || true
PROXY=(); for v in HTTPS_PROXY HTTP_PROXY NO_PROXY https_proxy http_proxy no_proxy GIT_SSL_CAINFO SSL_CERT_FILE REQUESTS_CA_BUNDLE; do
  [ -n "${!v:-}" ] && PROXY+=("$v=${!v}"); done
ENV=(env -i PATH="$J/faux-bin:/usr/sbin:/usr/bin:/sbin:/bin" HOME="$J/home" GIT_CONFIG_GLOBAL="$J/home/.gitconfig" "${PROXY[@]}"
     RACINE_AMORCE="$J/racine" MODE=jouet BRANCHE_PREFIXE=essai/ VENV_EXISTANT="$DEPOT/.venv" GO_DATE="$(date -u +%F)"
     COMMIT="$LANCE" COMMIT_CODE="$CODE" GH_TOKEN="${GH_TOKEN:-}" PRIX_HEURE_USD=0.8 PRIX_STOCKAGE_HEURE_USD=0.05
     ECHEANCE_UTC_S=$(( $(date +%s) + 7200 )) CONTAINER_ID=1 CONTAINER_API_KEY=factice DEPOT_URL="$URL")
A="$J/amorce-v7.sh"; T 60 git -C "$DEPOT" show "$CODE:scripts/amorce_instance_sparks_exp7_nul_v7.sh" > "$A"
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
absent  3 "$J/racine/sparks-causal-002/run.err" "No module named"
attendu 3 "$J/racine/sparks-causal-002/journal.txt" "fin du calcul, code [1-9]"
attendu 3 "$J/3-causal.txt" "sans poussée vérifiée"
etape 4-rejoue; attendu 4 "$J/4-rejoue.txt" "ordre refusé"
ordre 003 '{"numero": 3, "instance": "1", "phase": "fin", "deja_usd": 2.0}'
etape 5-fin; attendu 5 "$J/5-fin.txt" "ordre 3 \(fin\)"
echo "   DELETE au journal : $(grep -c 'DELETE instance 1 ' "$J/racine/sparks-v5-minuterie.log") (attendu : 1)"
if pgrep -f "$J/racine/sparks-v5-minuterie.sh" >/dev/null; then echo "   ÉCART : minuterie restante"; else echo "   OK   aucune minuterie restante"; fi
echo "   branches à supprimer par Lazar : essai/sparks-v7-repetition essai/sparks-exp7-nul-v5-$COURT essai/sparks-exp7-nul-causal-v5-$COURT-002 ordres/sparks-exp7-nul-v5-$COURT"
T 120 git -C "$DEPOT" worktree remove --force "$J/prep"; T 60 git -C "$DEPOT" branch -D essai/sparks-v7-repetition
echo "sorties : $J/*.txt ; journal de la minuterie : $J/racine/sparks-v5-minuterie.log"
```

Résultat attendu : `OK` sur chaque ligne, dont « ARRET 0/28 modèles dans les bornes » au `run.err` de la fabrication et
« fin du calcul, code [1-9] » au journal de la phase causale. Le code de la phase causale est non nul, parce que le départ
« jouet » n'est pas un modèle publié : c'est l'échec voulu du calcul jouet. Le résultat attendu compte aussi
`DELETE au journal : 1 (attendu : 1)`.

**Tir réel** : la commande de la section 5 du rapport v5 vaut avec le lanceur v7 et le commit v7 :

```
cd /home/claude/wt/sparks-exp7-nul-v7
SPARKS_REGISTRE_GO=/home/user/controle-ia-travail/registres/go.md \
  bash scripts/lancer_sparks_exp7_nul_v7.sh tir <OFFRE> <PRIX_CARTE> <PRIX_STOCKAGE> 67dbad98df37b7f283913c0e489853a8a690b2f8 <GO_ID_DU_TIR> 25
```
