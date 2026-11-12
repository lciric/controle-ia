# Ordre d'exécution de la phase 1 de l'épreuve de l'étiqueteur — brouillon v1

- **Rédacteur** : sous-agent Claude Opus 5.5 (`claude-opus-5-5`), 8 novembre 2026, de 00:18 à 00:35 (temps universel, `date -u` ; conteneur redémarré vers 00:25, rédaction reprise à 00:26, rien encore écrit sur le disque) ; rédacteur du préenregistrement et de ses scripts ; ni exécutant ni analyste de cette phase.
- **Statut** : brouillon pour la session mère. Deux marqueurs à remplir par elle avant de transmettre : `<<VARIABLE_CLE_ARGON>>` (section 1.5) et `<<GENERATION_PAR>>` (section 2). Les feux verts des étapes 2.5 et 4.1 sont écrits par la session mère pendant l'exécution.
- **Destinataire** : la session exécutante (fille 6). Elle applique cet ordre **à la lettre**. Tout écart, toute commande qui ne rend pas le résultat attendu, tout cas non prévu : **arrêt**, compte rendu à la session mère, aucune improvisation.
- **Fait foi** : le préenregistrement scellé `prereg/preenregistrement-epreuve-etiqueteur-v1.md` (empreinte `f73455b8b672c2b1a896b54badb6d8262fe9b422d4aa346f44c6efc76eef40fa`, commit `d858b66f936897e2e97f4846a9e25e9b705cea0b`, R-1744), sections « Lecteurs modèles », « Scripts de la phase 1 », « Ordre des opérations » (points 3 à 6), « Critères de lecture gelés » (liste d'arrêt), « Points ouverts » (point 3, relais de Kimi). En cas de désaccord entre cet ordre et le texte scellé, le texte scellé prime et l'exécutante s'arrête.
- **Répétition faite par le rédacteur** (sans aucun appel, dans le bloc-notes, sur la graine d'essai 20261107 et en mode simulé) : génération, tirage de la phase 2, liste des relectures, essai de format et lecture principale simulés, contrôle avant analyse : codes de fin 0, comptes 396, 396, 20, 20, 80, 60 ; essai de format au feu vert ; lecture principale partie avec `--depense-engagee` égale à la dépense de l'essai ; 456 réponses « ok » par lecteur. Le filtre de l'environnement des sections 3.1 et 3.2 a été essayé sur des variables factices (seuls les noms gardés restent). Les blocs de cet ordre ont été extraits du fichier et rejoués (00:32 à 00:34), racine déplacée dans le bloc-notes, graine d'essai à la place de l'entropie réelle : syntaxe des 20 blocs, 1.1, 1.3 (douze « OK », GO trouvé, entropie 17812956677980471985), 1.4 (24, 6, 79, 12 essais passés), 1.5 sur des noms factices (cas sain : code 0 ; variable absente ou marqueur non rempli : arrêt, code 1), 1.6, 2.1 à 2.4, 3.3, 3 bis, l'impression du manifeste de 3.4, 4.5 et 5 sur les sorties simulées ; 3.2 et 4.3 en mode réel avec une variable de clé factice absente : arguments, GO et commit acceptés, arrêt « variable absente : aucun appel », code 2. Le relais et les appels réels n'ont **pas** été essayés.

## Règles permanentes de l'exécutante (valent pour toutes les sections)

1. **Aucune clé lue ni affichée.** La présence d'une variable de clé se vérifie par son nom seulement (section 1.5). Jamais `env`, `printenv`, `set`, `export -p`, `echo $…` d'une variable de clé, ni lecture de `/proc/*/environ`. Aucune valeur de clé sur une ligne de commande : les clés passent par l'environnement hérité, filtré (sections 3.1 et 3.2).
2. **Aucune sortie brute.** L'exécutante n'ouvre, n'affiche ni ne résume **aucune** réponse des lecteurs (fichiers `reponses-phase1-*-v4*.jsonl`, champ `reponse_brute`, champ `motif`), aucun contenu des items, de la clé (`cle-*.jsonl`), du tirage de la phase 2, ni aucun résultat d'analyse. Elle ne lit que : les codes de fin, les empreintes, les nombres de lignes, et les champs nommés dans cet ordre, par les programmes écrits dans cet ordre (qui n'impriment que des nombres, des statuts et des empreintes).
3. **On n'écrase jamais** (R12) : chaque dossier de sortie est neuf ; si un chemin de cet ordre existe déjà au moment de sa création, arrêt.
4. **Arrêts par numéro de processus** (R10), jamais par motif de ligne de commande ; chaque numéro est écrit dans un fichier au lancement.
5. Aucun commit, aucune poussée, aucun fichier `.sha256`, aucun contact, aucune publication. Aucun module du programme importé hors des scripts nommés ici.
6. Heures relevées par `date -u` au début et à la fin de chaque section ; elles vont au compte rendu.
7. Chaque appel de l'outil de commande repart d'un interpréteur neuf : chaque bloc commence par `set -u; . /home/user/epreuve-etiqueteur-phase1-v1/variables-v1.sh` (sauf le bloc 1.1 qui crée ce fichier).
8. Options toujours écrites en entier, jamais abrégées (limite 14 du texte scellé ; le script de lecture refuse une option abrégée, code 2).

## 1. Préalables

### 1.1 Racine et variables (aucun secret dans ce fichier)

```bash
date -u
test ! -e /home/user/epreuve-etiqueteur-phase1-v1 || { echo "ARRET : la racine existe déjà"; exit 1; }
mkdir -p /home/user/epreuve-etiqueteur-phase1-v1
cat > /home/user/epreuve-etiqueteur-phase1-v1/variables-v1.sh <<'FIN'
RACINE=/home/user/epreuve-etiqueteur-phase1-v1
DEPOT=/home/user/controle-ia-travail
CODE=$RACINE/code
EPR=$RACINE/code/docs/notes/epreuve-etiqueteur-v1
RELAIS_SCRIPT=$RACINE/code/docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py
ENTREES=$RACINE/entrees
GEN=$RACINE/generation
TIRAGE=$RACINE/tirage-phase2
FORMAT=$RACINE/lecture-format
PRINC=$RACINE/lecture-principale
RELAIS_F=$RACINE/relais-format
RELAIS_P=$RACINE/relais-principale
CONSOLES=$RACINE/consoles
CR=$RACINE/compte-rendu
PY=/home/user/controle-ia-travail/.venv/bin/python
COMMIT_CODE=64e67cbd4a870a4bc8f861e7a4632c300283a3c2
COMMIT_SCELLE=d858b66f936897e2e97f4846a9e25e9b705cea0b
EMPREINTE_SCELLE=f73455b8b672c2b1a896b54badb6d8262fe9b422d4aa346f44c6efc76eef40fa
ENTROPIE=17812956677980471985
GO_ID=GO-2026-11-07-07
EMPREINTE_RELAIS=67f369518102b3f7408f28dab053a4d6f9bc2b676eadfaa338f55d39af99027e
NOM_CLE_ARGON='<<VARIABLE_CLE_ARGON>>'
NOM_CLE_KIMI=KIMI_API_KEY
PORT_RELAIS=8789
FIN
mkdir /home/user/epreuve-etiqueteur-phase1-v1/consoles /home/user/epreuve-etiqueteur-phase1-v1/compte-rendu /home/user/epreuve-etiqueteur-phase1-v1/entrees
sha256sum /home/user/epreuve-etiqueteur-phase1-v1/variables-v1.sh
```

Attendu : code 0. L'empreinte de `variables-v1.sh` va au compte rendu.

### 1.2 Code au commit scellé (arbre détaché, hors ligne) et entrées scellées

```bash
set -u; . /home/user/epreuve-etiqueteur-phase1-v1/variables-v1.sh
git -C "$DEPOT" fetch origin main
git -C "$DEPOT" cat-file -e "$COMMIT_CODE^{commit}" && git -C "$DEPOT" cat-file -e "$COMMIT_SCELLE^{commit}" || { echo "ARRET : commit absent"; exit 1; }
git -C "$DEPOT" worktree add --detach "$CODE" "$COMMIT_CODE"
test "$(git -C "$CODE" rev-parse HEAD)" = "$COMMIT_CODE" && echo "commit du code conforme"
test -z "$(git -C "$CODE" status --porcelain)" && echo "arbre propre"
git -C "$DEPOT" show "$COMMIT_SCELLE:prereg/preenregistrement-epreuve-etiqueteur-v1.md" > "$ENTREES/preenregistrement-epreuve-etiqueteur-v1.md"
git -C "$DEPOT" show "$COMMIT_SCELLE:registres/go.md" > "$ENTREES/go-d858b66f9.md"
```

Si `/home/user/controle-ia-travail` n'existe pas dans la session exécutante : arrêt et compte rendu (la session mère dit d'où cloner ; jamais vers `lciric/controle-ia`).

### 1.3 Empreintes (texte scellé, scripts, essais, relais, entrées du générateur) et GO

```bash
set -u; . /home/user/epreuve-etiqueteur-phase1-v1/variables-v1.sh
sha256sum -c - <<FIN
$EMPREINTE_SCELLE  $ENTREES/preenregistrement-epreuve-etiqueteur-v1.md
ceeef5290bac268cba2d4e5508f32372eaaedb39afd4ec777aa3fbb4d74cce7a  $EPR/generer_items_v2.py
341403e940180e1cfce80114848ddbdb5b0fe559d813e92948297c700de55c08  $EPR/epreuve_phases_v1.py
627ebcb7dc8f6bd334edc53562a6128f0009427a858317b6fc44d1c10ab15d37  $EPR/lire_items_phase1_v4.py
7c0555b4647a3e1e2c314b4e934345522cb72995712a789e044e81e77373fb9f  $EPR/analyser_phase1_v3.py
9224c043959391a5b19b4889694b208b00c9f66bbee7fef4770808af4286ca7c  $EPR/test_generer_items_v2.py
a097958005d48298e1d9bbb107741f3eb55bfe3a56633a9e15b3709abaaf1f4f  $EPR/test_lire_items_phase1_v4.py
734d7bcfd306d9d7064e541a1afc1aa15b86a48968469ca6e51c0b1e3f564182  $EPR/test_analyser_phase1_v3.py
61113bb97a5cd3a3757686d3fb278c213f1c4036bfbd653feaf32929f91743bf  $EPR/test_epreuve_phases_v1.py
$EMPREINTE_RELAIS  $RELAIS_SCRIPT
ba05fa13af2dd4f935334438b44d2d27fbc655a970721b10b90bd94b5846f284  $CODE/donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl
287e83485cba550098b80db809589398d8f2826c02dfa9cc2719a1063795d5aa  $CODE/donnees/t05-pilote-v1/taches-pilote-60-v1.json
FIN
echo "code sha256sum=$?"
grep -c "^| $GO_ID |" "$ENTREES/go-d858b66f9.md"
"$PY" -I -c "import hashlib,sys; e=hashlib.sha256(open(sys.argv[1],'rb').read()).hexdigest(); print('entropie', int(e[:16],16))" "$ENTREES/preenregistrement-epreuve-etiqueteur-v1.md"
"$PY" -I -c "import numpy, sys; print('python', sys.version.split()[0], 'numpy', numpy.__version__)"
```

Attendu : douze lignes « OK » et `code sha256sum=0` ; `1` pour le GO ; `entropie 17812956677980471985` ; numpy au moins 1.25. Sinon arrêt.

Le registre des GO **au commit du code** ne porte pas encore GO-2026-11-07-07 (vérifié par le rédacteur : 0 ligne) : le défaut de `--registre-go` (registre voisin du script) ferait refuser le mode réel. D'où le registre extrait du commit scellé, passé partout par `--registre-go "$ENTREES/go-d858b66f9.md"`.

### 1.4 Essais des scripts au commit du code (liste d'arrêt : un essai qui échoue, pas de génération)

```bash
set -u; . /home/user/epreuve-etiqueteur-phase1-v1/variables-v1.sh
for t in test_generer_items_v2 test_epreuve_phases_v1 test_lire_items_phase1_v4 test_analyser_phase1_v3; do
  env -i PATH=/usr/bin:/bin LANG=C.UTF-8 "$PY" -I -B -m pytest -q -p no:cacheprovider --noconftest -c /dev/null --rootdir "$EPR" "$EPR/$t.py" > "$CONSOLES/essais-$t-v1.log" 2>&1
  echo "$t code=$? : $(tail -n 1 "$CONSOLES/essais-$t-v1.log")"
done
```

Attendu : code 0 et « 24 passed », « 6 passed », « 79 passed », « 12 passed ». Ces essais tournent sans réseau et sans clé (`env -i`).

### 1.5 Variables de clé : présence vérifiée par le nom seulement

**Choix du nom de la variable d'Argon** : l'exécutante ne choisit pas. Le directeur a dit « clé existante » ; deux noms existent dans la session mère (`GEMINI_API_KEY`, `GEMINI_API_KEY_2`) et l'histoire des registres ne tranche pas sans lecture de valeur (R-388 : clé Gemini n° 2 dans `GEMINI_API_KEY_2` ; R-1540 : crédit d'Argon rechargé, « on va utiliser la clé »). La session mère remplace le marqueur `<<VARIABLE_CLE_ARGON>>` de la section 1.1 par le nom retenu, avant de transmettre l'ordre. Marqueur encore présent : arrêt.

```bash
set -u; . /home/user/epreuve-etiqueteur-phase1-v1/variables-v1.sh
case "$NOM_CLE_ARGON" in *'<<'*) echo "ARRET : marqueur de la variable d'Argon non rempli"; exit 1;; esac
ok=1
for n in "$NOM_CLE_ARGON" "$NOM_CLE_KIMI"; do
  if [[ "$n" =~ ^[A-Z_][A-Z0-9_]*$ ]] && [ -n "${!n:-}" ]; then echo "$n : présente"; else echo "$n : ABSENTE ou nom refusé"; ok=0; fi
done
[ "$ok" = 1 ] || { echo "ARRET : variable de clé absente"; exit 1; }
```

Attendu : deux lignes « présente », code 0. Le bloc n'affiche jamais une valeur (l'expansion indirecte ne sert qu'au test de non-vacuité). Une variable absente : arrêt (la liste d'arrêt du texte scellé : variable de la clé absente, arrêt avant tout appel).

### 1.6 Relais de Kimi : où trouver les commandes, comment le lancer

- **Procédure de référence** : branche `outils/commandes-tour-ferme-v1`, commit `12f9e0e38f2cf7adb61a9c3ddf0ee4c5c66556d9` (R-1129), dossier `docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/`, fichier `LISEZMOI-commandes-tour-ferme-v4.md`, section « Réglages exigés des relais » : instance neuve du relais pour chaque lancement, sans autre usage ; `--modeles-permis kimi-k3.1-pro --prix-entree 2 --prix-sortie 10 --prix-cache 2` (`--prix-cache` obligatoire) ; `GET /relais/etat` relevé avant le premier appel et après le dernier ; arrêt par numéro de processus. Lecture seule, sans extraire la branche : `git -C "$DEPOT" show 12f9e0e38f2cf7adb61a9c3ddf0ee4c5c66556d9:docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/LISEZMOI-commandes-tour-ferme-v4.md`. Les commandes clientes de ce tour (`commande_kimi_v6.py`, `commande_argon_v56_nuit_v6.py`) ne sont **pas** lancées ici : le client de cette épreuve est `lire_items_phase1_v4.py`.
- **Relais lancé** : `relais_kimi_v4.py` du commit du code (empreinte vérifiée en 1.3), version nommée par le texte scellé (« Points ouverts », point 3), sur la boucle locale, port 8789 (le défaut du script de lecture).
- **Réglages par lancement** (texte scellé, même point) : `--max-appels` **100** pour l'essai de format, **2 280** pour la lecture principale et la relecture ; `--plafond-usd` égal au reste du plafond de 300 dollars (300 pour l'essai de format ; 300 moins la dépense de l'essai pour la lecture principale) ; le script de lecture reçoit la **même** valeur à `--relais-max-appels`.
- Les commandes exactes sont aux sections 3.1 et 4.2. Le port doit être libre avant chaque lancement :

```bash
set -u; . /home/user/epreuve-etiqueteur-phase1-v1/variables-v1.sh
curl -sS --noproxy '*' --max-time 3 "http://127.0.0.1:$PORT_RELAIS/relais/etat" > /dev/null 2>&1 && echo "ARRET : port $PORT_RELAIS occupé" || echo "port $PORT_RELAIS libre"
```

## 2. Génération des items (une fois ; avant tout appel)

**Qui** : le texte scellé (« Ordre des opérations », point 3) confie la génération, le tirage de la phase 2 et la liste des relectures à la session mère. Marqueur à remplir par la session mère : `<<GENERATION_PAR>>` = « session mère » (l'exécutante saute alors 2.1 à 2.3, reçoit le dossier `$GEN` et `$TIRAGE` faits par ces mêmes commandes, et refait seulement 2.4) ou « session exécutante, par délégation écrite de la session mère du JJ/MM HH:MM » (l'exécutante fait 2.1 à 2.4). Marqueur non rempli : arrêt.

### 2.1 Items, clé, items de formation

```bash
set -u; . /home/user/epreuve-etiqueteur-phase1-v1/variables-v1.sh
date -u
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 "$PY" -I -B "$EPR/generer_items_v2.py" --actions "$CODE/donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl" --taches "$CODE/donnees/t05-pilote-v1/taches-pilote-60-v1.json" --sortie "$GEN" --entropie "$ENTROPIE" --commit "$COMMIT_CODE" --formation 20 > "$CONSOLES/console-generation-v1.log" 2>&1
echo "generation code=$?"
```

### 2.2 Tirage de la phase 2 (avant toute lecture)

```bash
set -u; . /home/user/epreuve-etiqueteur-phase1-v1/variables-v1.sh
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 "$PY" -I -B "$EPR/epreuve_phases_v1.py" phase2 --items "$GEN/items-epreuve-v2.jsonl" --cle "$GEN/cle-epreuve-v2.jsonl" --entropie "$ENTROPIE" --sortie "$TIRAGE" > "$CONSOLES/console-tirage-phase2-v1.log" 2>&1
echo "tirage code=$?"
```

`--sortie` est un **dossier** : le fichier écrit est `$TIRAGE/tirage-phase2-v1.jsonl`.

### 2.3 Liste des jumeaux à relire

```bash
set -u; . /home/user/epreuve-etiqueteur-phase1-v1/variables-v1.sh
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 "$PY" -I -B "$EPR/analyser_phase1_v3.py" relectures --cle "$GEN/cle-epreuve-v2.jsonl" --sortie "$GEN/relectures-v1.txt" > "$CONSOLES/console-relectures-v1.log" 2>&1
echo "relectures code=$?"
```

### 2.4 Contrôle des comptes et empreintes (nombres de lignes seulement)

```bash
set -u; . /home/user/epreuve-etiqueteur-phase1-v1/variables-v1.sh
wc -l "$GEN/items-epreuve-v2.jsonl" "$GEN/cle-epreuve-v2.jsonl" "$GEN/items-formation-v2.jsonl" "$GEN/cle-formation-v2.jsonl" "$TIRAGE/tirage-phase2-v1.jsonl" "$GEN/relectures-v1.txt"
sha256sum "$GEN"/* "$TIRAGE/tirage-phase2-v1.jsonl" | tee "$CR/empreintes-generation-v1.txt"
date -u
```

Attendu : 396, 396, 20, 20, 80, 60 lignes ; trois codes 0 en 2.1 à 2.3. Sinon arrêt (liste d'arrêt : comptes différents du texte scellé, enquête écrite par la session mère). Les consoles de 2.1 à 2.3 ne sont pas ouvertes (le générateur y écrit son manifeste ; les comptes et empreintes ci-dessus suffisent).

### 2.5 Arrêt : dépôt chez le tiers par la session mère

L'exécutante **s'arrête** et envoie à la session mère le compte rendu de 1 et 2 (codes, comptes, empreintes). La session mère fait le dépôt chez le tiers (texte scellé, « Ordre des opérations », point 4 : empreinte du texte scellé, tables des seuils des deux phases, empreintes des items, de la clé et du tirage), puis écrit le **feu vert de dépôt** : heure du dépôt, empreintes déposées. L'exécutante vérifie que ces empreintes sont celles de `$CR/empreintes-generation-v1.txt` ; une différence : arrêt. **Aucun appel avant ce feu vert** (sans dépôt antérieur à la première lecture, l'épreuve ne décide plus rien).

## 3. Essai de format (20 items de formation, lancé seul)

### 3.1 Relais de Kimi, instance neuve : `--max-appels 100`, `--plafond-usd 300`

Lancé avec l'option `run_in_background` de l'outil de commande. Le sous-interpréteur retire de son environnement toute variable exportée sauf le chemin, le mandataire du réseau et la variable de la clé de Kimi, puis se remplace par Python (même numéro de processus, R10). Aucune valeur sur une ligne de commande.

```bash
set -u; . /home/user/epreuve-etiqueteur-phase1-v1/variables-v1.sh
mkdir "$RELAIS_F"
( while IFS= read -r v; do case "$v" in PATH|HTTPS_PROXY|https_proxy|"$NOM_CLE_KIMI") ;; *) unset "$v" 2>/dev/null ;; esac; done < <(compgen -e)
  export PATH=/usr/bin:/bin LANG=C.UTF-8 SSL_CERT_FILE=/root/.ccr/ca-bundle.crt
  exec "$PY" -I -B "$RELAIS_SCRIPT" --port "$PORT_RELAIS" --variable-cle "$NOM_CLE_KIMI" --modeles-permis kimi-k3.1-pro --plafond-usd 300 --reserve-par-appel 0.40 --prix-entree 2 --prix-sortie 10 --prix-cache 2 --max-appels 100 --delai-amont-s 1800 --delai-silence-s 600 --journal "$RELAIS_F/journal-relais-kimi-v1.jsonl"
) > "$RELAIS_F/console-relais-kimi-v1.log" 2>&1 &
echo $! > "$RELAIS_F/relais.pid"
cat "$RELAIS_F/relais.pid"
```

État avant le premier appel (le relais ne rend jamais la clé ; le programme n'imprime que des réglages et des compteurs) :

```bash
set -u; . /home/user/epreuve-etiqueteur-phase1-v1/variables-v1.sh
curl -sS --noproxy '*' --max-time 10 "http://127.0.0.1:$PORT_RELAIS/relais/etat" > "$RELAIS_F/etat-avant-v1.json"
"$PY" -I -c "
import json,sys
e=json.load(open(sys.argv[1])); p=open(sys.argv[2]).read().strip()
garde=('version','pid','modeles_permis','plafond_usd','max_appels','appels','depense_usd','prix_entree','prix_sortie','prix_cache')
print({k:v for k,v in e.items() if k in garde or 'cle' in k or 'env' in k})
print('numero de processus conforme' if str(e.get('pid'))==p else 'ARRET : numero de processus different')
" "$RELAIS_F/etat-avant-v1.json" "$RELAIS_F/relais.pid"
```

Attendu : `modeles_permis` = `['kimi-k3.1-pro']`, `plafond_usd` 300, `max_appels` 100, `appels` 0, numéro de processus conforme, et la preuve, écrite par le relais, que la variable de clé n'est plus dans son environnement. Sinon : arrêt du relais (section 3.4) et compte rendu.

### 3.2 Lecture de l'essai de format, mode réel

Lancé avec l'option `run_in_background` ; l'outil rappelle l'exécutante à la fin. Le code de fin est écrit dans un fichier.

```bash
set -u; . /home/user/epreuve-etiqueteur-phase1-v1/variables-v1.sh
date -u
( ( while IFS= read -r v; do case "$v" in PATH|HTTPS_PROXY|https_proxy|"$NOM_CLE_ARGON") ;; *) unset "$v" 2>/dev/null ;; esac; done < <(compgen -e)
    export PATH=/usr/bin:/bin LANG=C.UTF-8 SSL_CERT_FILE=/root/.ccr/ca-bundle.crt
    exec "$PY" -I -B "$EPR/lire_items_phase1_v4.py" --reel --lectures format --items "$GEN/items-epreuve-v2.jsonl" --formation "$GEN/items-formation-v2.jsonl" --relectures "$GEN/relectures-v1.txt" --question "$ENTREES/preenregistrement-epreuve-etiqueteur-v1.md" --sortie "$FORMAT" --entropie "$ENTROPIE" --plafond-dollars 300 --depense-engagee 0 --variable-cle-gemini "$NOM_CLE_ARGON" --relais-kimi "http://127.0.0.1:$PORT_RELAIS" --relais-empreinte "$EMPREINTE_RELAIS" --relais-max-appels 100 --go "$GO_ID" --registre-go "$ENTREES/go-d858b66f9.md" --commit "$COMMIT_CODE" --fils-par-lecteur 1
  ) > "$CONSOLES/console-lecture-format-v1.log" 2>&1 &
  P=$!; echo "$P" > "$CONSOLES/lecture-format.pid"; wait "$P"; echo "$?" > "$CONSOLES/code-lecture-format-v1.txt" )
```

`--question` pointe le texte scellé lui-même : le script en extrait le bloc de la question fermée entre ses deux marqueurs (empreinte du bloc à l'annexe du texte scellé).

### 3.3 Surveillance pendant la lecture (nombres seulement)

Toutes les dix minutes environ, et à la fin :

```bash
set -u; . /home/user/epreuve-etiqueteur-phase1-v1/variables-v1.sh
D="$FORMAT"; P=$(cat "$CONSOLES/lecture-format.pid"); kill -0 "$P" 2>/dev/null && echo "processus $P actif" || echo "processus $P fini"
"$PY" -I -c "
import json,sys,collections
d=sys.argv[1]
for L in 'AB':
    st=collections.Counter(); n=0; c=0.0
    for nom in (f'reponses-phase1-{L}-v4.encours.jsonl',):
        try:
            for x in open(f'{d}/{nom}',encoding='utf-8'):
                if x.strip(): r=json.loads(x); st[(r.get('lecture'), r.get('statut'))]+=1
        except FileNotFoundError: pass
    try:
        for x in open(f'{d}/journal-phase1-{L}-v4.jsonl',encoding='utf-8'):
            if x.strip(): r=json.loads(x); n+=1; c+=float(r.get('cout_estime') or 0)
    except FileNotFoundError: pass
    print(L, dict(st), 'tentatives', n, 'cout_estime_dollars', round(c,4))
" "$D"
```

Ce programme ne lit que les champs `lecture`, `statut` et `cout_estime` ; il n'imprime aucune réponse.

### 3.4 Après la fin : état du relais, arrêt du relais, manifeste

```bash
set -u; . /home/user/epreuve-etiqueteur-phase1-v1/variables-v1.sh
date -u; echo "code de fin de la lecture : $(cat "$CONSOLES/code-lecture-format-v1.txt")"
curl -sS --noproxy '*' --max-time 10 "http://127.0.0.1:$PORT_RELAIS/relais/etat" > "$RELAIS_F/etat-apres-v1.json"
"$PY" -I -c "
import json,sys
e=json.load(open(sys.argv[1]))
print({k:e.get(k) for k in ('pid','appels','depense_usd','engage_usd','restant_usd','refus','refus_modele','ecarts_modele_servi','usages_absents','delais_depasses','appels_au_dessus_de_la_reserve','reponses_par_statut')})
" "$RELAIS_F/etat-apres-v1.json"
P=$(cat "$RELAIS_F/relais.pid"); test "$("$PY" -I -c "import json,sys; print(json.load(open(sys.argv[1]))['pid'])" "$RELAIS_F/etat-apres-v1.json")" = "$P" && kill "$P"
timeout 30 tail --pid="$P" -f /dev/null; kill -0 "$P" 2>/dev/null && echo "ARRET : relais $P toujours vivant" || echo "relais $P arrêté"
"$PY" -I -c "
import json,sys
m=json.load(open(sys.argv[1]))
cf=m.get('controle_format') or {}
print('code', m.get('code_de_sortie'), 'arret', m.get('arret'), 'lecteurs_arretes', m.get('lecteurs_arretes'))
print('comptes', json.dumps(m.get('comptes')))
print('feu_vert', cf.get('feu_vert'), 'motifs', cf.get('motifs'), 'extrapolation_dollars', cf.get('extrapolation_dollars'), 'plafond_restant_dollars', cf.get('plafond_restant_dollars'))
print('par_lecteur', json.dumps(cf.get('par_lecteur')))
print('depense_estimee_dollars', repr(m.get('depense_estimee_dollars')), 'reserve_restante_dollars', m.get('reserve_restante_dollars'), 'tentatives_interrompues', m.get('tentatives_interrompues_comptees_au_pire'))
print('empreinte_reglages', m.get('empreinte_reglages'), 'relais_max_appels', m.get('relais_max_appels'), 'commit', m.get('commit'))
print('sorties', json.dumps(m.get('sorties')))
" "$FORMAT/manifeste-lecture-phase1-v4.json"
sha256sum "$FORMAT"/* "$RELAIS_F"/* | tee "$CR/empreintes-lecture-format-v1.txt"
```

Les champs imprimés du manifeste sont des comptes, des coûts, des statuts et des motifs écrits par le script (jamais une réponse). La console `console-lecture-format-v1.log` n'est pas ouverte.

Codes de fin (texte scellé) : 0 fin normale ; 2 refus avant tout appel (dont la variable de la clé d'Argon absente au départ : vérifié par le rédacteur) ; 3 garde de dépense ; 4 lecteur arrêté (modèle servi différent, pensée d'Argon au-delà de 8 192, sortie au-delà de la réservée) ; 5 arrêt général (clé absente ou refusée) ; 6 feu rouge ; 7 exception. **Tout code autre que 0** : arrêt, compte rendu, nœud du directeur avant toute lecture de réponse. Code 0 avec `feu_vert` différent de `True` : arrêt.

## 3 bis. Contrôle de la facture de l'essai de format

### Ce que rapporte l'exécutante (par lecteur, depuis le journal, nombres seulement)

```bash
set -u; . /home/user/epreuve-etiqueteur-phase1-v1/variables-v1.sh
"$PY" -I -c "
import json,sys
d=sys.argv[1]
for L in 'AB':
    s={'tentatives':0,'jetons_entree':0,'jetons_sortie':0,'jetons_pensee':0,'cout_estime_dollars':0.0,'modele_servi_different':0}
    debut=[]; fin=[]
    for x in open(f'{d}/journal-phase1-{L}-v4.jsonl',encoding='utf-8'):
        if not x.strip(): continue
        r=json.loads(x); s['tentatives']+=1
        for k in ('jetons_entree','jetons_sortie','jetons_pensee'): s[k]+=int(r.get(k) or 0)
        s['cout_estime_dollars']+=float(r.get('cout_estime') or 0)
        if r.get('modele_servi') and r.get('modele_servi')!=r.get('modele_demande'): s['modele_servi_different']+=1
        if r.get('debut'): debut.append(r['debut'])
        if r.get('fin'): fin.append(r['fin'])
    s['cout_estime_dollars']=round(s['cout_estime_dollars'],6)
    print(L, json.dumps(s), 'premier_appel', min(debut) if debut else None, 'dernier_appel', max(fin) if fin else None)
" "$FORMAT" | tee "$CR/facture-attendue-format-v1.txt"
```

Le compte rendu porte, pour Argon (`gemini-4-argon`, appel direct) et pour Kimi (`kimi-k3.1-pro`, par le relais) : tentatives, jetons d'entrée, de sortie et de pensée, dépense estimée, fenêtre horaire des appels (temps universel) ; pour Kimi, en plus, `appels` et `depense_usd` de l'état du relais après la lecture.

### Qui compare, et où

- **Le directeur**, sur la console de facturation de chaque fournisseur (Google pour Argon, Moonshot pour Kimi) : aucune interface de facturation n'est lisible par programme dans cette session (aucun hôte de facturation autorisé, aucune clé de facturation ; en ajouter une serait un nœud). La session mère lui transmet les nombres ci-dessus ; il écrit, pour chaque fournisseur et pour la seule fenêtre de l'essai de format : montant facturé hors taxes, jetons facturés (entrée, sortie, pensée si elle est détaillée).
- **La session mère** compare et écrit le résultat.
- Pour que la comparaison soit possible : **aucun autre usage** des deux clés pendant la fenêtre de l'essai (la session mère le garantit avant le lancement 3.2).

### Ce qui arrête (texte scellé, « Ordre des opérations », point 6)

Pour Argon comme pour Kimi : montant facturé hors taxes **supérieur** à la dépense estimée de ce lecteur ; jetons facturés différents des jetons écrits au-delà de l'arrondi d'affichage de la console ; modèle facturé différent du modèle demandé ; appels de l'essai impossibles à isoler sur la console (autre usage dans la fenêtre). Dans chacun de ces cas : **arrêt avant la lecture principale, nœud du directeur**. Le feu vert du script est nécessaire, non suffisant.

## 4. Lecture principale et relecture (396 items et 60 jumeaux)

### 4.1 Condition de départ : feu vert écrit de la session mère

L'exécutante ne lance rien de cette section sans un message de la session mère qui porte, en toutes lettres : « feu vert de la lecture principale » ; l'empreinte de `$FORMAT/manifeste-lecture-phase1-v4.json` (égale à celle de `$CR/empreintes-lecture-format-v1.txt`) ; la valeur `depense_estimee_dollars` de ce manifeste ; le résultat du contrôle de la facture, conforme pour les deux fournisseurs. Une seule différence : arrêt.

### 4.2 Relais de Kimi, instance neuve : `--max-appels 2280`, `--plafond-usd` = 300 moins la dépense de l'essai

```bash
set -u; . /home/user/epreuve-etiqueteur-phase1-v1/variables-v1.sh
curl -sS --noproxy '*' --max-time 3 "http://127.0.0.1:$PORT_RELAIS/relais/etat" > /dev/null 2>&1 && { echo "ARRET : port occupé"; exit 1; }
DEP=$("$PY" -I -c "import json,sys; print(repr(json.load(open(sys.argv[1]))['depense_estimee_dollars']))" "$FORMAT/manifeste-lecture-phase1-v4.json")
RESTE=$("$PY" -I -c "import math,sys; print('%.2f' % (math.floor((300-float(sys.argv[1]))*100)/100))" "$DEP")
echo "depense de l'essai $DEP ; plafond du relais $RESTE"
mkdir "$RELAIS_P"
( while IFS= read -r v; do case "$v" in PATH|HTTPS_PROXY|https_proxy|"$NOM_CLE_KIMI") ;; *) unset "$v" 2>/dev/null ;; esac; done < <(compgen -e)
  export PATH=/usr/bin:/bin LANG=C.UTF-8 SSL_CERT_FILE=/root/.ccr/ca-bundle.crt
  exec "$PY" -I -B "$RELAIS_SCRIPT" --port "$PORT_RELAIS" --variable-cle "$NOM_CLE_KIMI" --modeles-permis kimi-k3.1-pro --plafond-usd "$RESTE" --reserve-par-appel 0.40 --prix-entree 2 --prix-sortie 10 --prix-cache 2 --max-appels 2280 --delai-amont-s 1800 --delai-silence-s 600 --journal "$RELAIS_P/journal-relais-kimi-v1.jsonl"
) > "$RELAIS_P/console-relais-kimi-v1.log" 2>&1 &
echo $! > "$RELAIS_P/relais.pid"
cat "$RELAIS_P/relais.pid"
```

Puis l'état avant, par le bloc d'état de la section 3.1 où `RELAIS_F` est remplacé par `RELAIS_P` (les deux chemins `etat-avant-v1.json` et `relais.pid`). Attendu : `max_appels` 2 280, `plafond_usd` égal à `RESTE`, `appels` 0, numéro de processus conforme.

### 4.3 Lecture principale et relecture, mode réel

Lancé avec `run_in_background`. `--depense-engagee` reçoit la valeur exacte du manifeste de l'essai (le script refuse une valeur inférieure, et un plafond différent de 300).

```bash
set -u; . /home/user/epreuve-etiqueteur-phase1-v1/variables-v1.sh
date -u
DEP=$("$PY" -I -c "import json,sys; print(repr(json.load(open(sys.argv[1]))['depense_estimee_dollars']))" "$FORMAT/manifeste-lecture-phase1-v4.json")
( ( while IFS= read -r v; do case "$v" in PATH|HTTPS_PROXY|https_proxy|"$NOM_CLE_ARGON") ;; *) unset "$v" 2>/dev/null ;; esac; done < <(compgen -e)
    export PATH=/usr/bin:/bin LANG=C.UTF-8 SSL_CERT_FILE=/root/.ccr/ca-bundle.crt
    exec "$PY" -I -B "$EPR/lire_items_phase1_v4.py" --reel --lectures principale+relecture --feu-vert-format "$FORMAT/manifeste-lecture-phase1-v4.json" --items "$GEN/items-epreuve-v2.jsonl" --formation "$GEN/items-formation-v2.jsonl" --relectures "$GEN/relectures-v1.txt" --question "$ENTREES/preenregistrement-epreuve-etiqueteur-v1.md" --sortie "$PRINC" --entropie "$ENTROPIE" --plafond-dollars 300 --depense-engagee "$DEP" --variable-cle-gemini "$NOM_CLE_ARGON" --relais-kimi "http://127.0.0.1:$PORT_RELAIS" --relais-empreinte "$EMPREINTE_RELAIS" --relais-max-appels 2280 --go "$GO_ID" --registre-go "$ENTREES/go-d858b66f9.md" --commit "$COMMIT_CODE" --fils-par-lecteur 1
  ) > "$CONSOLES/console-lecture-principale-v1.log" 2>&1 &
  P=$!; echo "$P" > "$CONSOLES/lecture-principale.pid"; wait "$P"; echo "$?" > "$CONSOLES/code-lecture-principale-v1.txt" )
```

### 4.4 Surveillance et arrêts en cours de lecture

Le programme de la section 3.3, avec `D="$PRINC"` et `lecture-principale.pid`, toutes les quinze minutes environ. L'exécutante **arrête le processus de lecture par son numéro** (`kill "$(cat "$CONSOLES/lecture-principale.pid")"`), puis le relais (section 3.4 avec `RELAIS_P`), et rend compte, si :
- un lecteur compte **8 items « illisible » ou plus** dans la lecture `principale` (plus de 2 % de 396 : liste d'arrêt, pas de verdict) ;
- les tentatives augmentent sans que les statuts avancent pendant 45 minutes (crédit épuisé ou erreurs de transport persistantes : liste d'arrêt) ;
- la dépense estimée cumulée (`DEP` plus la somme des `cout_estime`) dépasse 300 dollars (ne doit pas arriver : la garde du script arrête avant).

Un lancement arrêté n'est **jamais** relancé par l'exécutante : la reprise, avec la dépense déjà engagée (somme des `cout_estime` du journal pour un lancement sans manifeste) et un plafond diminué d'autant, est un ordre nouveau de la session mère, dans un dossier de sortie nouveau.

### 4.5 Après la fin

Le bloc de la section 3.4, avec `code-lecture-principale-v1.txt`, `RELAIS_P`, `$PRINC/manifeste-lecture-phase1-v4.json` et `$CR/empreintes-lecture-principale-v1.txt` (le manifeste de cette lecture n'a pas de `controle_format` : ses lignes imprimeront `None`). Puis le contrôle des empreintes, sans ouvrir les réponses :

```bash
set -u; . /home/user/epreuve-etiqueteur-phase1-v1/variables-v1.sh
"$PY" -I -c "
import json,sys,hashlib
d=sys.argv[1]; m=json.load(open(d+'/manifeste-lecture-phase1-v4.json')); e={}
for L in 'AB':
    n=f'reponses-phase1-{L}-v4.jsonl'; e[L]=hashlib.sha256(open(f'{d}/{n}','rb').read()).hexdigest()
    print(n, e[L], 'egale au manifeste' if m['sorties'].get(n)==e[L] else 'ARRET : differente du manifeste')
print('A et B differentes' if e['A']!=e['B'] else 'ARRET : A et B identiques')
" "$PRINC"
date -u
```

## 5. Comportement face aux réponses ; analyse

- L'exécutante **ne lit aucune réponse** des lecteurs et **aucun résultat** : ni les fichiers de réponses, ni les journaux au-delà des champs nommés aux sections 3.3 et 3 bis, ni les consoles des lectures, ni la clé, ni le tirage. Elle ne lance **pas** l'analyse.
- Elle rapporte : codes de fin, empreintes (sections 2.4, 3.4, 4.5), comptes par statut, dépenses estimées par lecteur et cumulées, états du relais avant et après chaque lancement, heures.
- **L'analyse** est lancée après la lecture principale par un **lecteur neuf** (sous-agent qui n'a écrit ni le préenregistrement, ni les scripts, ni cet ordre, et n'a pas exécuté la lecture), sur ordre de la session mère, sur les deux fichiers finals du dernier lancement « principale+relecture » allé à son terme. Il refait d'abord le contrôle écrit du texte scellé : empreintes égales aux champs `sorties` du manifeste et différentes l'une de l'autre, et **champ `lecteur` de chaque ligne égal au lecteur du fichier** (`analyser_phase1_v3.py` ne le contrôle pas) ; sinon, pas d'analyse. Commande, à sortie fixée :

```bash
set -u; . /home/user/epreuve-etiqueteur-phase1-v1/variables-v1.sh
mkdir "$RACINE/analyse"
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 "$PY" -I -B "$EPR/analyser_phase1_v3.py" analyser --items "$GEN/items-epreuve-v2.jsonl" --cle "$GEN/cle-epreuve-v2.jsonl" --reponses-a "$PRINC/reponses-phase1-A-v4.jsonl" --reponses-b "$PRINC/reponses-phase1-B-v4.jsonl" --entropie "$ENTROPIE" --tirages 10000 --sortie "$RACINE/analyse/resultat-phase1-v1.json" > "$CONSOLES/console-analyse-v1.log" 2>&1
echo "analyse code=$?"
```

Un arrêt de l'analyse s'écrit comme issue au fichier de résultat, avec le code 0. Le verdict de phase 1 est prononcé par un autre sous-agent neuf (R13 par analogie), scellé, soumis au directeur.

## 6. Arrêts, compte rendu, règles

### Arrêts (en plus de ceux des sections précédentes et de la liste d'arrêt du texte scellé)

| constat | action |
|---|---|
| empreinte, commit, comptes, GO ou entropie différents de cet ordre | arrêt avant tout appel |
| marqueur `<<VARIABLE_CLE_ARGON>>` ou `<<GENERATION_PAR>>` non rempli ; variable de clé absente | arrêt avant tout appel |
| feu vert de dépôt (2.5) ou de lecture principale (4.1) absent ou différent | aucun lancement |
| un chemin de sortie existe déjà | arrêt (R12) |
| relais : état avant non conforme, numéro de processus différent, port occupé | arrêt du relais par son numéro, aucun lancement de lecture |
| code de fin de lecture autre que 0, ou feu rouge | arrêt, nœud du directeur avant toute lecture de réponse |
| facture non conforme (3 bis) | arrêt avant la lecture principale, nœud du directeur |
| 8 illisibles ou plus pour un lecteur en lecture principale ; lecture bloquée 45 minutes | arrêt de la lecture par son numéro de processus, puis du relais |
| une valeur de clé apparaît dans une sortie, une console ou un message | arrêt immédiat de tous les processus par leur numéro ; ne pas recopier ; signaler le fichier par son chemin seulement ; nœud du directeur (la clé est à renouveler) |
| relais encore vivant après son arrêt | `kill` du même numéro une seconde fois ; s'il survit, compte rendu immédiat |

### Compte rendu (fichier `$CR/compte-rendu-phase1-v1.md`, et message court à la session mère à chaque arrêt prévu : 2.5, fin de 3, fin de 4)

Heures de chaque section ; empreinte de `variables-v1.sh` ; résultats de 1.3 à 1.5 (OK, nombres d'essais passés, « présente » par nom) ; codes de fin ; comptes de 2.4 ; empreintes (`empreintes-generation-v1.txt`, `empreintes-lecture-format-v1.txt`, `empreintes-lecture-principale-v1.txt`) ; champs imprimés des manifestes ; facture attendue par lecteur ; états du relais avant et après ; numéros de processus lancés et arrêtés ; écarts et arrêts. Aucun extrait de réponse, de clé, d'item ou de tirage.

### Fin de session

Tous les processus lancés (relais, lectures) sont arrêtés par leur numéro et vérifiés morts (`kill -0`). L'arbre `$CODE` est laissé en place (la session mère le retire). Rien n'est commité ni poussé par l'exécutante.

## Points ouverts pour la session mère

1. `<<VARIABLE_CLE_ARGON>>` : nom de la variable de la clé d'Argon (« clé existante » du directeur).
2. `<<GENERATION_PAR>>` : le texte scellé attribue la génération à la session mère ; la déléguer à l'exécutante est un choix de la session mère, à écrire (s'il était vu comme un écart au texte scellé, c'est un nœud du directeur).
3. Joignabilité de `generativelanguage.googleapis.com` et de `api.moonshot.ai` depuis la session exécutante : non vérifiée par le rédacteur (aucun appel) ; un refus du réseau rendrait des items illisibles à l'essai de format, donc un feu rouge, sans dépense notable.
4. Durée : la lecture principale (456 items par lecteur, un fil par lecteur, raisonnement long chez Kimi) peut durer plusieurs heures ; la session exécutante doit rester ouverte jusqu'à la fin, ou l'ordre doit prévoir sa relève.
