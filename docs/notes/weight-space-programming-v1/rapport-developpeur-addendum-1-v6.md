# SPARKS-EXP7-NUL — additif v6 au rapport du développeur (code v6, minimal)

Même rédacteur-développeur. Tâche : message de la mère du 5 novembre 2026 (≈ 00:50 UTC), après la répétition v5 qu'elle a
jouée (R-1514 ; `docs/notes/weight-space-programming-v1/repetition-jouet-v5-v1/`). Travail de 00:53 à 02:00 UTC environ
(`date -u`). Mêmes interdits que pour la v5, tous tenus : aucune poussée, aucun `.sha256` sur `main`, aucun fichier
existant modifié, aucun réseau, aucune dépense ; moins de 20 Mo employés. Cet additif complète
`rapport-developpeur-addendum-1-v5.md`, qui reste valable pour tout ce qu'il ne cite pas ici.

**Verdict.** Code v6 : branche locale `prep/sparks-exp7-nul-v6`, commit `f18837d1a15e6a7e31f5ce573725d35ca9e17a85`. C'est
un commit sur `b7d342ef`, avec 16 fichiers neufs (8 fichiers et leurs compagnons) et aucun fichier modifié ; la liste
fermée v6 (132 fichiers) est conforme. L'essai du tir ne dépend plus ni du commit extrait ni de la date. Comptes :
section 3.

## 1. Cause et correction

**Cause.** L'essai `test_lanceur_mode_tir_commande_ecrite` (v5, l. 604-621) prenait `git rev-parse HEAD` pour commit du
code.
- Sur l'instance et dans la répétition, `HEAD` est un commit **enfant** : le code plus l'addendum.
- Le lanceur passe donc ce commit à `garde_code liste`, et la différence `55399606..HEAD` contient l'addendum, qui est
  hors de la liste fermée. La garde refuse, le code de retour vaut 2, et l'essai échoue.
- L'échec arrête le script d'instance avant tout calcul.
- L'essai lisait aussi `date.today()`, et `tir.py` contrôlait la validité du GO à la date du jour.

**Correction**, en fichiers neufs (R12 ; les fichiers v5 sont gardés tels quels) :
- **Essai v6** (`tests/test_sparks_exp7_nul_v6.py`) : copie de l'essai v5 sur les scripts v6. Seul l'essai du tir change :
  - le commit du code vient de `COMMIT_CODE`, posé par l'amorce sur l'instance, ou, à défaut, du dernier commit qui a
    écrit la liste fermée v6 (`git log -1 -- …/liste-fermee-v1.txt`) ; un commit enfant qui ajoute l'addendum ne touche
    pas cette liste ;
  - la ligne de GO a des dates fixes (5 et 6 novembre), et la date de contrôle est passée par `SPARKS_DATE_TIR` ;
  - un artefact s'ajoute : même registre, date du 7 novembre, refus « validité ».
- **Lanceur v6** : la date du contrôle du GO du tir se règle (`SPARKS_DATE_TIR`, défaut : aujourd'hui). Il emploie la
  garde du code v6 et l'amorce v6.
- **Amorce v6** : copie de la v5 où seuls changent la garde du code (v6) et le script d'instance appelé (v6).
- **Script d'instance v6** : il joue les essais v1 à v4 et **v6**. L'essai v5 n'est plus joué : il est remplacé par l'essai
  v6 et reste gardé tel quel.
- **Garde du code v6** et liste fermée v6.
- **Banc v6** : banc v5 entier, plus 6 mutations des lignes qui changent.

Les noms des journaux, des fichiers de la machine et des branches restent ceux de la v5 (`sparks-v5-*`,
`ordres/sparks-exp7-nul-v5-…`), pour un changement minimal.

**Dépendances vérifiées** (essais v1 à v6) : aucun autre essai ne lit `HEAD`. Les instants employés (`time.time()`) sont
tous relatifs : échéance à maintenant ± n s, création à maintenant − 60 s. Les GO sont lus à des dates fixes (`GO_DATE`,
`date(2026, 11, 4)`).

**Seule dépendance restante, déclarée.** L'amorce calcule sa durée par `depense duree`, qui compte le stockage jusqu'à la
fin du 18 novembre, à partir de l'heure réelle. Les essais d'amorce qui exigent au moins 60 minutes (phase causale)
refuseraient donc à partir du 18 novembre au soir. C'est sans effet dans la validité du GO, et le code n'a pas d'usage
après elle ; je ne l'ai pas changé.

## 2. Fichiers et empreintes (branche `prep/sparks-exp7-nul-v6`, chacun avec son compagnon)

| Fichier | sha256 |
|---|---|
| `scripts/amorce_instance_sparks_exp7_nul_v6.sh` | `f3f02cad0cde301375bce1fca8268e6e0670d828785d0d6aff3e0fc1c3001467` |
| `scripts/banc_mutations_sparks_exp7_nul_v6.py` | `7bbeff525d062d8fae7771df2db4ac20c956dcac53e8a6f70743eecd26794ec9` |
| `scripts/lancer_sparks_exp7_nul_v6.sh` | `4c5c952a7a49d381d705a0f73599fb6b9e8581837497ad7f523eef0e78a7e9d2` |
| `scripts/sparks_exp7_nul_instance_v6.sh` | `6da021c6dea129af3a83c43f8d58c7900ddceecc089e2bf693d8d7850fbaf11d` |
| `src/controle_ia/sparks_exp7_nul_v6/__init__.py` | `0b9f51a644f6351e18c036b9cbf214c185e3218fefaa1b74ef5f6d0ebf6f80c4` |
| `src/controle_ia/sparks_exp7_nul_v6/garde_code.py` | `4e0db8a09b954e68771425a3836ca528401e30cdd51aa225a63950e09a932fa5` |
| `src/controle_ia/sparks_exp7_nul_v6/liste-fermee-v1.txt` | `6ec4f33ade89d251601f29c82b6768bc1e0b31e74acecc07905312e1d72cead6` |
| `tests/test_sparks_exp7_nul_v6.py` | `a5c9fe6f03e304dd434bcac33d0463eb6941541373842aeb2f0261f177ea320d` |

`garde_code liste . f18837d1…` (v6) → « LISTE FERMÉE CONFORME : 132 fichiers ».

## 3. Essais et banc

Sorties brutes dans `essais-et-banc-sparks-v6/` (même dossier que ce rapport). Le jeu d'essais est celui que joue le
script d'instance v6 : v1 à v4, puis v6.

| Mesure | Compte | Sortie (sha256) |
|---|---|---|
| Essais à la tête de la branche (`f18837d1`) | **279 passés sur 279** (90 + 69 + 38 + 29 + 53), 0 sauté | `essais-tete-f18837d1.txt` `2f630c34…` |
| Essais sur un commit **enfant factice** (`32c65937`) : code v6 + addendum fictif scellé, comme l'instance ; `COMMIT_CODE` posé comme le fait l'amorce | **279 passés sur 279**, 0 sauté (l'essai du tir compris) | `essais-enfant-32c65937.txt` `741e70de…` |
| Même commit enfant, essai du tir seul, **sans** `COMMIT_CODE` (repli par la liste fermée) | **1 passé** | `essai-tir-enfant-sans-commit-code.txt` `11e81be3…` |
| Banc v6 : bancs v1 à v5 entiers | **22/22, 52/52, 40/40, 30/30, 30/30 tuées** (code 1 et « failed ») | `banc-f18837d1.txt` `6e90a90b…`, `.json` `31527182…` |
| Banc v6 : mutations neuves | **6/6 tuées** ; six témoins verts ; 0 inapplicable | idem |

Le commit enfant est **local**, dans un arbre détaché à part (`/home/claude/wt/sparks-v6-enfant`), sans branche ; il n'est
jamais poussé, et l'arbre est retiré après l'essai.

Tout run est compté (R4). Avant le commit, un passage des seuls essais v6 a donné 51 passés et 1 sauté (l'essai du tir,
la liste fermée v6 n'étant pas encore au commit), puis j'ai fait deux passages ciblés.

L'essai v5 (`test_sparks_exp7_nul_v5.py`) n'est plus joué par le script d'instance v6. À la tête v6, son essai du tir
échouerait pour la même raison qu'à la répétition (`HEAD` ≠ code v5) : c'est le défaut corrigé, gardé tel quel (R12).

Limite du banc : l'essai du tir se saute dans la copie du banc, qui n'est pas un dépôt `git`. Les lignes v6 du lanceur et
des scripts y sont tuées par l'essai statique `test_v6_scripts_garde_v6_essais_v6_et_date_du_tir`. Le repli « dernier
commit de la liste fermée » n'est donc éprouvé que par le passage sur le commit enfant, pas par le banc.

## 4. Brouillon 5

Le brouillon 5 (`851f75e4…`) ne cite ni le commit du code ni les comptes : seulement « Code v5, branche
`prep/sparks-exp7-nul-v5` » et la liste fermée v5. Selon la consigne, je ne l'ai pas changé. Couple proposé pour le
brouillon suivant (`ancien` unique dans le brouillon 5) :

- ancien : `La liste fermée v5 (\`src/controle_ia/sparks_exp7_nul_v5/liste-fermee-v1.txt\`) compte les fichiers v2 à v5 ; la garde de lancement lit celle-ci.`
- nouveau : `La liste fermée v5 (\`src/controle_ia/sparks_exp7_nul_v5/liste-fermee-v1.txt\`) compte les fichiers v2 à v5. Code v6 (\`prep/sparks-exp7-nul-v6\`, descendant de la v5), minimal : essai du tir indépendant du commit extrait et de la date, scripts v6 (garde du code v6, essais v1 à v4 et v6) ; la liste fermée v6 (\`src/controle_ia/sparks_exp7_nul_v6/liste-fermee-v1.txt\`, fichiers v2 à v6) est celle que la garde de lancement lit.`

## 5. Commande de répétition v6

C'est celle de la v5 (`rapport-developpeur-addendum-1-v5.md`, section 6), avec trois changements :
- `CODE` est le commit v6 ;
- l'amorce est l'amorce v6 ;
- la branche d'essai est `essai/sparks-v6-repetition`.

Les attendus, les fichiers de la machine et les branches de sortie et d'ordres gardent les noms de la v5. Le script
d'instance v6 joue les essais v1 à v4 et v6 : attendu supplémentaire, « essais : … passed » au journal de la
fabrication.

```bash
#!/usr/bin/env bash
set -uo pipefail
CODE=f18837d1a15e6a7e31f5ce573725d35ca9e17a85
DEPOT=/home/user/controle-ia-travail
URL=https://github.com/lciric/controle-ia-travail.git
J=$(mktemp -d /tmp/repetition-sparks-v6-XXXX); mkdir -p "$J/faux-bin" "$J/racine" "$J/home"
T() { timeout -k 10 "$@"; }
T 600 git -C "$DEPOT" worktree add -q --no-checkout -b essai/sparks-v6-repetition "$J/prep" "$CODE"
T 60 git -C "$J/prep" sparse-checkout set --no-cone '/*' '!/*/' '/prereg/SPARKS-EXP7-NUL-*' '/registres/go.md'
T 600 git -C "$J/prep" checkout -q essai/sparks-v6-repetition
cp "$DEPOT/registres/go.md" "$J/prep/registres/go.md"
printf 'Addendum fictif de répétition (aucune valeur) ; commit du code %s\n' "$CODE" > "$J/prep/prereg/SPARKS-EXP7-NUL-addendum-1.md"
(cd "$J/prep/prereg" && sha256sum SPARKS-EXP7-NUL-addendum-1.md > SPARKS-EXP7-NUL-addendum-1.md.sha256)
T 60 git -C "$J/prep" add -A && T 60 git -C "$J/prep" -c user.name=essai -c user.email=essai@invalid commit -qm "essai : répétition v6 (addendum fictif)"
T 300 git -C "$J/prep" push -q origin essai/sparks-v6-repetition || { echo "poussée de la branche d'essai impossible : arrêt"; exit 2; }
LANCE=$(git -C "$J/prep" rev-parse HEAD); COURT=${LANCE:0:12}
printf '#!/bin/bash\necho "curl $*" >> "%s/faux.log"\nprintf 200\n' "$J" > "$J/faux-bin/curl"; chmod +x "$J/faux-bin/curl"
cp "${HOME}/.gitconfig" "$J/home/.gitconfig" 2>/dev/null || true
PROXY=(); for v in HTTPS_PROXY HTTP_PROXY NO_PROXY https_proxy http_proxy no_proxy GIT_SSL_CAINFO SSL_CERT_FILE REQUESTS_CA_BUNDLE; do
  [ -n "${!v:-}" ] && PROXY+=("$v=${!v}"); done
ENV=(env -i PATH="$J/faux-bin:/usr/sbin:/usr/bin:/sbin:/bin" HOME="$J/home" GIT_CONFIG_GLOBAL="$J/home/.gitconfig" "${PROXY[@]}"
     RACINE_AMORCE="$J/racine" MODE=jouet BRANCHE_PREFIXE=essai/ VENV_EXISTANT="$DEPOT/.venv" GO_DATE="$(date -u +%F)"
     COMMIT="$LANCE" COMMIT_CODE="$CODE" GH_TOKEN="${GH_TOKEN:-}" PRIX_HEURE_USD=0.8 PRIX_STOCKAGE_HEURE_USD=0.05
     ECHEANCE_UTC_S=$(( $(date +%s) + 7200 )) CONTAINER_ID=1 CONTAINER_API_KEY=factice DEPOT_URL="$URL")
A="$J/amorce-v6.sh"; T 60 git -C "$DEPOT" show "$CODE:scripts/amorce_instance_sparks_exp7_nul_v6.sh" > "$A"
etape() { T 3600 unshare -pf --mount-proc "${ENV[@]}" bash "$A" > "$J/$1.txt" 2>&1; echo "== $1 : code $?"; }
attendu() { if grep -qE -- "$3" "$2"; then echo "   OK   $1 : « $3 »"; else echo "   ÉCART $1 : « $3 » absent de $2"; fi; }
O="$J/ordres-depot"; T 60 git init -q "$O"; T 60 git -C "$O" remote add origin "$URL"; mkdir -p "$O/ordres"
ordre() { echo "$2" > "$O/ordres/ordre-$1.json"; T 60 git -C "$O" add ordres && T 60 git -C "$O" -c user.name=essai -c user.email=essai@invalid commit -qm "essai : ordre $1" \
          && T 300 git -C "$O" push -q origin "HEAD:refs/heads/ordres/sparks-exp7-nul-v5-$COURT"; }
etape 1-creation
attendu 1 "$J/1-creation.txt" "AMORCE V5 : outils : curl oui, git oui, unshare oui, chroot oui"
attendu 1 "$J/1-creation.txt" "mode jouet : addendum non exigé"
attendu 1 "$J/1-creation.txt" "fabrication, durée plafonnée"
attendu 1 "$J/racine/sparks/journal.txt" "essais : [0-9]+ passed"
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
attendu 3 "$J/racine/sparks-causal-002/journal.txt" "fin du calcul, code [1-9]"
attendu 3 "$J/3-causal.txt" "sans poussée vérifiée"
etape 4-rejoue; attendu 4 "$J/4-rejoue.txt" "ordre refusé"
ordre 003 '{"numero": 3, "instance": "1", "phase": "fin", "deja_usd": 2.0}'
etape 5-fin; attendu 5 "$J/5-fin.txt" "ordre 3 \(fin\)"
echo "   DELETE au journal : $(grep -c 'DELETE instance 1 ' "$J/racine/sparks-v5-minuterie.log") (attendu : 1)"
if pgrep -f "$J/racine/sparks-v5-minuterie.sh" >/dev/null; then echo "   ÉCART : minuterie restante"; else echo "   OK   aucune minuterie restante"; fi
echo "   branches à supprimer par Lazar : essai/sparks-v6-repetition essai/sparks-exp7-nul-v5-$COURT essai/sparks-exp7-nul-causal-v5-$COURT-002 ordres/sparks-exp7-nul-v5-$COURT"
T 120 git -C "$DEPOT" worktree remove --force "$J/prep"; T 60 git -C "$DEPOT" branch -D essai/sparks-v6-repetition
echo "sorties : $J/*.txt ; journal de la minuterie : $J/racine/sparks-v5-minuterie.log"
```

Résultat attendu : `OK` sur chaque ligne et `DELETE au journal : 1 (attendu : 1)`.

**Tir réel** : la commande de la section 5 du rapport v5 vaut avec le lanceur v6 et le commit v6 :

```
cd /home/claude/wt/sparks-exp7-nul-v6
SPARKS_REGISTRE_GO=/home/user/controle-ia-travail/registres/go.md \
  bash scripts/lancer_sparks_exp7_nul_v6.sh tir <OFFRE> <PRIX_CARTE> <PRIX_STOCKAGE> f18837d1a15e6a7e31f5ce573725d35ca9e17a85 <GO_ID_DU_TIR> 25
```
