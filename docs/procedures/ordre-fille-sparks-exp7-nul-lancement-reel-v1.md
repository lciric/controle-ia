# Ordre de la mère à la fille — SPARKS-EXP7-NUL : expérience réelle sous GO-2026-11-04-04 — v1

Brouillon écrit le 5 novembre 2026 vers 06:30 UTC (`date -u`) par le rédacteur-développeur du code v9, pour la mère,
qui le relit, le complète et l'envoie. **Ne vaut qu'une fois l'addendum scellé.** Toutes les lignes de code citées le sont
au commit du code `4d07d2a6830ab09cb91250016284efb5cbe8a91c`, abrégé `CODE` :
- lanceur `scripts/lancer_sparks_exp7_nul_v9.sh`, cité « lanceur, l. n » ;
- amorce `scripts/amorce_instance_sparks_exp7_nul_v9.sh`, citée « amorce, l. n » ;
- script d'instance `scripts/sparks_exp7_nul_instance_v9.sh`, cité « instance, l. n ».

## Hypothèses (écrites telles quelles par la mère)
1. La mère remplit le marqueur du tir dans le brouillon, écrit `prereg/SPARKS-EXP7-NUL-addendum-1.md` (nom lu par
   `garde_code`), le scelle, puis pose un **commit enfant de `4d07d2a6`** sur `prep/sparks-exp7-nul-v9`, qui ajoute seulement
   ce fichier et son `.sha256`, et le pousse.
2. La fille lance depuis ce commit, appelé `LANCE` ci-dessous, avec `COURT=${LANCE:0:12}`.

**Réserve bloquante du rédacteur sur l'hypothèse 1, vérifiée.** Au commit `4d07d2a6`, `registres/go.md` n'a **pas** la ligne
d'extension de GO-2026-11-04-04 à 40 USD : `git show 4d07d2a6:registres/go.md` s'arrête à la ligne 242, alors que la ligne 245
de `main` porte l'extension. Deux gardes lisent ce fichier dans l'arbre du commit lancé :
- **le lanceur** (l. 195 : `go.main(['registres/go.md'])`, dans l'arbre d'où il tourne). `SPARKS_REGISTRE_GO` ne sert qu'au
  mode « tir » et n'y change rien ;
- **l'amorce** (l. 171 : `go_conforme`, dans le clone du commit lancé).

Avec l'hypothèse 1 telle quelle, le lanceur refuse la création. Si l'on passe outre, l'amorce s'arrête : « non conforme (base
et extension à 40 USD) : aucun calcul ». Le commit enfant doit donc **aussi porter `registres/go.md` de `main`**, comme le
commit du tir. La garde du code le permet : `verifier_lancement` n'interdit que `src/`, `tests/` et `scripts/` dans
`CODE..LANCE`.

## Pièces
- Addendum scellé `prereg/SPARKS-EXP7-NUL-addendum-1.md` au commit `LANCE`, avec son compagnon. Le lire en entier, surtout :
  - section 2 (code qui tournera, résultat du tir) ;
  - « Minuterie de destruction et redémarrages » ;
  - « Liste d'arrêt » ;
  - « Devis » ;
  - « Plan d'analyse », étapes 1 à 7.
- Texte parent `prereg/SPARKS-EXP7-NUL-preenregistrement-v1.md` (`4bacf20d…`).
- Procédure des lecteurs : `docs/notes/sparks-exp7-nul-v1/procedure-lecteurs-v2.md` au commit `LANCE`, qui fait foi pour la
  mise à disposition, le coffre et les lecteurs.
- Rapport v9 du développeur : `docs/notes/weight-space-programming-v1/rapport-developpeur-addendum-1-v9.md`.

## Règles constantes
- Aucune clé lue, affichée ni écrite. Les jetons passent par leur nom : `$VAST_API_KEY`, `$CONTROLE_IA_GITHUB_TOKEN`,
  `$HF_TOKEN`.
- `vastai` passe toujours par les commandes **imprimées par le lanceur v9**, jouées telles quelles. Elles ont `GO_ID=`
  devant, `timeout`, un environnement nettoyé et une sortie redirigée vers un fichier.
- Aucune sortie brute de `vastai` affichée, journalisée ni versée (R-1480). Les sous-commandes `apres-creation`,
  `apres-commande`, `inventaire`, `offres` et `journal-amorce` lisent puis **effacent** ces fichiers (lanceur, l. 66 et
  68 à 122).
- Destruction **par l'identifiant seulement, avec `-y`** (R10, R-1482) : `bash scripts/lancer_sparks_exp7_nul_v9.sh destruction
  $ID` (l. 123 à 127). Rien n'est tenu pour fait avant l'inventaire « absente ».
- **Aucune lecture de résultat avant l'étape 4 du « Plan d'analyse »** (ouverture unique du coffre). Avant elle, on lit
  seulement :
  - les lignes « AMORCE V5 » (`journal-amorce`) ;
  - le `journal.txt` versé ;
  - les verdicts du lanceur.

  Jamais `diag/*/fabrication-*.json`, `modeles-legers.tar.gz`, `empreintes-*.txt` ni `run-err-fin.txt` : ils vont au coffre
  par la procédure des lecteurs. Toute anomalie hors de ce qui est écrit ici : destruction par l'identifiant si l'instance
  tourne, arrêt, et tu me le dis.

## A. Préalables (avant la création, puis avant chaque redémarrage)
1. `date -u`. Dans `registres/go.md` de `main` :
   - GO-2026-11-04-04 est valide ce jour, avec sa base (l. 242, 25 USD) et son extension à 40 USD (l. 245), échéance le
     18 novembre, non révoqué ;
   - `registres/depenses.md` n'impute rien à GO-2026-11-04-04 (aucune ligne le 5 novembre à 06:28 UTC ; **revérifie**).
2. **Tir réel** : le marqueur rempli dans l'addendum dit verdict « arretee », `REDEMARRAGES=0`, instance détruite. Tout autre
   verdict (« boucle », ou « absente » avec `BOUCLE_PRESUMEE>0`) : aucune création sous ce texte, nœud de Lazar.
   - Raison : avec l'amorce v9, une relance automatique après la fabrication trouve le disque sans ordre neuf. C'est une
     boucle présumée (amorce, l. 147 à 149 et 197 à 198), donc une destruction immédiate, **avec les modèles**.
3. **Arbre du lancement** :
   - `git fetch origin refs/heads/prep/sparks-exp7-nul-v9:refs/remotes/origin/prep/sparks-exp7-nul-v9` ;
   - arbre à part au commit `LANCE`, puis `git status --porcelain` vide ;
   - `git rev-parse LANCE^` = `CODE` ;
   - `git diff --name-only CODE LANCE` ne doit donner que `prereg/SPARKS-EXP7-NUL-addendum-1.md`, son `.sha256` et
     `registres/go.md`.
4. **Épreuves des gardes**, dans cet arbre :
   - `(cd prereg && sha256sum -c SPARKS-EXP7-NUL-addendum-1.md.sha256)` → « OK » ;
   - `PYTHONPATH=src python3 -c 'from controle_ia.prereg import exiger_prereg_scelle as e; print(e("prereg/SPARKS-EXP7-NUL-addendum-1.md"))'`
     → une empreinte, aucune exception (huit sections, aucun marqueur, contre-lecture conforme) ;
   - `timeout 120 python3 -I -B -c "import sys; sys.path.insert(0, 'src/controle_ia/sparks_exp7_nul_v9'); import garde_code; sys.exit(garde_code.main(sys.argv[1:]))" lancement . CODE LANCE`
     → « LANCEMENT CONFORME » ;
   - `COMMIT_CODE=CODE PYTHONPATH=src timeout 900 python3 -m pytest -q -p no:cacheprovider tests/test_sparks_exp7_nul_v1.py tests/test_sparks_exp7_nul_v2.py tests/test_sparks_exp7_nul_v3.py tests/test_sparks_exp7_nul_v4.py tests/test_sparks_exp7_nul_v9.py`
     → 331 réussis, comme au rapport v9.

   Toute autre issue : arrêt.
5. **Outils** :
   - `vastai` 1.8.3 épinglé : `pip show vastai` → 1.8.3 ;
   - `$VAST_API_KEY`, `$CONTROLE_IA_GITHUB_TOKEN` et `$HF_TOKEN` présents, jamais affichés : `[ -n "$HF_TOKEN" ] && echo présent`.
     Sans `HF_TOKEN`, l'instance prend le repli gelé déclaré (instance, l. 86 : Gemma, puis Qwen, puis SmolLM, premier en
     HTTP 200).
6. **Branches à la création** : ni `calcul/sparks-exp7-nul-v5-$COURT` ni `ordres/sparks-exp7-nul-v5-$COURT` n'existent
   (`git ls-remote origin 'refs/heads/*$COURT*'` vide). Sinon, l'instance refuse (instance, l. 53).
7. **Inventaire du compte**, sans sortie brute :
   ```
   timeout -k 10 120 env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 VAST_API_KEY="$VAST_API_KEY" vastai show instances --raw > "$E/tout.json" 2> "$E/tout.json.err"; python3 -I -B -c 'import json,sys; [print(i.get("id"), i.get("actual_status"), i.get("label")) for i in json.load(open(sys.argv[1]))]' "$E/tout.json"; rm -f "$E/tout.json" "$E/tout.json.err"
   ```
   - Ajoute à `env -i` les variables du mandataire présentes, par leur nom, comme le fait `prefixe_env` (lanceur).
   - Aucune instance `sparks-exp7-nul-*` oubliée.
   - `E="${SPARKS_ETAT_DIR:-$HOME/.sparks-exp7-nul-v5}"`.
8. **Marqueur** : `$E/.creation-incertaine` absent (lanceur, l. 191). S'il est présent : inventaire, puis nœud.

## B. Offre et prix (avant la création)
1. `bash scripts/lancer_sparks_exp7_nul_v9.sh recherche` imprime la commande de recherche (l. 115 à 119). Joue-la en
   remplaçant **seulement** la requête `'num_gpus=1 rentable=true verified=true'` par
   `'num_gpus=1 gpu_ram>=24 disk_space>=120 rentable=true verified=true'`. La recherche imprimée est celle du tir : elle ne
   filtre ni la mémoire de la carte (24 Go au devis) ni le disque (120 Go à la création, l. 204).
2. `bash scripts/lancer_sparks_exp7_nul_v9.sh offres "$E/offres-brutes.json"` garde « gpu », une carte, par prix croissant, au
   plus 4 offres, puis efface le brut (`vast_lecture.offres`, l. 95).
3. **Prix** :
   - `PRIX_CARTE` = `dph_total` du rang 1 ;
   - **`PRIX_STOCKAGE` = `storage_cost` × 120 ÷ 730**, et non la valeur imprimée par `offres`, calculée pour les 20 Go du tir
     (`DISQUE_GO = 20`, `vast_lecture.py`, l. 40) :
   ```
   python3 -I -B -c 'import json,sys; o=json.load(open(sys.argv[1]))["offres"][int(sys.argv[2])-1]; print(o["id"], o["dph_total"], round(o["storage_cost"]*120/730, 6))' "$E/offres-retenues.json" 1
   ```
4. **État de dépense** `$E/etat.json`, écrit par toi, lu par la garde (`sparks_exp7_nul_v2/depense.py`, `projeter`,
   l. 57 à 95). L'essai d'égalité des lots est inconnu avant la fabrication, et un état inconnu est refusé sans repli
   (l. 83 à 89) : à la création, mets **le pire cas `"egalite_lots": false`** (16 h causales) et 18 copies.
   ```json
   {"prix_heure_carte": PRIX_CARTE, "prix_heure_stockage": PRIX_STOCKAGE, "heures_demarrees": 0, "phases_faites": [],
    "redemarrages_restants": 18, "egalite_lots": false, "sorties_copiees": false}
   ```
   Projection = (6 + 0,5 + 18 × 0,5 + 16) h × `PRIX_CARTE` + stockage jusqu'au 19 novembre 00:00 × `PRIX_STOCKAGE`. Exemple :
   0,30 et 0,0247 USD/h (`storage_cost` 0,15) donnent ≈ 9,5 + 8,1 ≈ 17,6 USD ; 1,00 USD/h donne ≈ 39,6 USD, à la limite.
   **Refus au-delà de 40 USD** : prends l'offre suivante, sinon nœud.

## C. Session 1 — création et fabrication
1. Imprimer la création :
   ```
   bash scripts/lancer_sparks_exp7_nul_v9.sh creation OFFRE PRIX_CARTE PRIX_STOCKAGE LANCE CODE "$E/etat.json"
   ```
   Le lanceur rejoue (l. 195 à 198) :
   - le GO de base et l'extension ;
   - le sceau du texte parent ;
   - `garde_code lancement` ;
   - `depense projeter`.

   Puis il imprime la commande littérale (l. 204 à 206) :
   - `GO_ID=GO-2026-11-04-04 timeout -k 10 300 env -i … vastai create instance OFFRE --image pytorch/pytorch:2.9.1-cuda12.8-cudnn9-runtime --disk 120 --label sparks-exp7-nul-v5-$COURT` ;
   - `-e COMMIT=LANCE -e COMMIT_CODE=CODE -e ADDENDUM_SHA256=<empreinte de l'addendum au commit, l. 200> -e PRIX_HEURE_USD -e PRIX_STOCKAGE_HEURE_USD -e ECHEANCE_UTC_S=1795046400 -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN -e HF_TOKEN=$HF_TOKEN`
     (échéance par défaut : fin du 18 novembre, l. 187) ;
   - `--args bash -c "$(git show LANCE:scripts/amorce_instance_sparks_exp7_nul_v9.sh)"`, suivie de `apres-creation`.

   **Joue-la telle quelle.**
2. Selon `apres-creation` (l. 68 à 90) :

   | Sortie | Conduite |
   |---|---|
   | « CRÉÉE : instance ID » | note `ID` et `cree_le` dans `etat.json` |
   | « OFFRE RETIRÉE (no_such_ask) » | rien de créé, aucun marqueur ; en mode création, aucune commande suivante n'est imprimée : reprends B.3 avec le rang suivant (au plus 4), puis C.1 |
   | « CRÉATION INCERTAINE » | marqueur posé ; inventaire A.7, nœud |
   | « NON PARVENUE » (certificat) | arrêt, tu me le dis |
3. **Ce que fait l'amorce à la création** :
   - minuterie lancée en premier (l. 105) ;
   - clone et extraction au commit `LANCE` ;
   - GO (l. 171) ;
   - durée bornée (`borne`, puis `duree`, l. 172 à 174 : 90 % de (40 − déjà − stockage projeté) au prix de la carte, au plus
     24 h ; moins de 60 min : rien) ;
   - garde du code (l. 175) ;
   - addendum reconnu par `ADDENDUM_SHA256` (l. 177) ;
   - marqueur des gardes (l. 178) ;
   - fabrication sous `timeout` (l. 182). L'instance pousse `calcul/sparks-exp7-nul-v5-$COURT`, vérifie la poussée
     (instance, l. 131), puis le conteneur sort (l. 183).
4. **Surveillance**, toutes les 30 minutes :
   - `inventaire` « running » ;
   - `timeout -k 10 120 … vastai logs $ID --tail 400 > "$E/logs.txt" 2>&1; bash scripts/lancer_sparks_exp7_nul_v9.sh journal-amorce "$E/logs.txt"`,
     qui ne garde que les lignes « AMORCE V5 », sans ancre (l. 113).

   Durée attendue : 2 à 6 h, bornée par la machine.
5. **Fin de la fabrication**. Trois inventaires sur au moins 5 minutes (la commande imprimée par `apres-creation`), puis
   `bash scripts/lancer_sparks_exp7_nul_v9.sh boucle $ID` (l. 104 à 112) :

   | Verdict | Conduite |
   |---|---|
   | « arretee » | conforme, la suite continue |
   | « boucle » | joue la destruction `-y` imprimée, puis inventaire « absente » ; nœud |
   | « absente » avec `BOUCLE_PRESUMEE>0` au journal | l'amorce s'est détruite (boucle), modèles perdus ; nœud |
   | « indecis » | un inventaire de plus |
6. **Versement de la fabrication**, sans lecture :
   ```
   git fetch origin refs/heads/calcul/sparks-exp7-nul-v5-$COURT:refs/remotes/origin/calcul/sparks-exp7-nul-v5-$COURT
   ```
   - Arbre à part ; `sha256sum -c` de chaque `.sha256` sous `runs/` et `diag/` du commit poussé. Lis **seulement** `journal.txt` :
     « essais : N passed », « LANCEMENT CONFORME », « essai d'égalité des lots : oui|non », « MANIFESTE CRÉÉ … addendum »,
     « fin du calcul, code N », « poussée vérifiée ».
   - Les autres fichiers passent au coffre par la procédure des lecteurs (étapes 4 à 6).
   - Code de fin non nul, ou « ARRET » écrit par l'amorce au journal Vast : nœud.
   - Mets à jour `etat.json` : `phases_faites` + `fabrication` et `etape0`, `egalite_lots` selon le journal,
     `heures_demarrees`.
   - La mère verse la branche sur `main` ; tu ne pousses rien d'autre que les ordres.

## D. Copies par lots (redémarrages courts), puis lecteurs (sans carte)
Pour chaque lot `NNN` (001, 002, …), composé par `mise_a_disposition lots --libres OCTETS --noms …` (procédure, point 4) :
1. **Ordre** :
   - écris `ordres/ordre-NNN.json` : `{"numero": n, "instance": "ID", "phase": "copie", "deja_usd": <dépense cumulée, jamais plus basse>, "cas": [1 à 4 identifiants], "premier": <vrai pour le premier lot>, "copie_minutes": 30}` ;
   - clés fermées (`redemarrage.py`, l. 49) ; `copie_minutes` de 5 à 60 (l. 95 à 97) ;
   - committe dans un dépôt d'ordres à part et pousse : `git push origin "HEAD:refs/heads/ordres/sparks-exp7-nul-v5-$COURT"`.
2. `depense projeter "$E/etat.json"`, puis `bash scripts/lancer_sparks_exp7_nul_v9.sh redemarrage $ID PRIX_CARTE PRIX_STOCKAGE LANCE CODE "$E/etat.json"`.
   Joue le `start` imprimé (l. 209 et suivantes). « ENVOYÉ » n'est lu que sur « starting instance ID. » (l. 94) ; ensuite,
   inventaire « running ».
3. L'amorce :
   - consigne le redémarrage (l. 189) ;
   - lit l'ordre, le consigne « fait » (l. 198 à 203) ;
   - prépare `/root/sparks/lots/lot-NNN/` (l. 215) ;
   - écrit « COPIE prête » au journal, puis reste en vie `copie_minutes` (l. 218).

   **Sans ordre neuf** (oubli de pousser, numéro déjà fait), elle se détruit aussitôt (« boucle présumée », l. 197 à 198) :
   pousse toujours l'ordre **avant** le `start`.
4. Copie : `vastai copy ID:/root/sparks/lots/lot-NNN/ <dossier hors du servi>`, sous `timeout`, sortie non affichée.
   - **Non éprouvée** par le tir (risque déclaré) : vérifie la syntaxe par `vastai copy --help` avant la première. Un échec
     est un nœud.
   - Puis `sha256sum -c MANIFESTE-LOT.txt` dans le lot copié.
   - Puis `mise_a_disposition servir …` (procédure, point 6) : B3 et B4 au coffre, rien d'imprimé.
5. Après tous les lots, les lecteurs (procédure, points 2, 3, 6 et 7) :
   - réponses scellées ;
   - `aveugle.engager_bases` ;
   - **ouverture unique du coffre** (`aveugle.ouvrir_coffre`) : c'est l'étape 4 du « Plan d'analyse », la première où une
     lecture est permise ;
   - analyse (`analyse.analyser`).

## E. Session 2 — contrôle causal (après l'ouverture ; par script, sans lecture humaine intermédiaire)
1. Sur la branche des ordres :
   - `ordres/causal/cle-ouverte-v1.json` : la copie scellée de la clé ouverte ;
   - `ordres/causal/reponses/<lecteur>/<cas>/reponse-v2.json` : les réponses scellées, lues par
     `"$REPONSES"/*/*/reponse-v2.json` (instance, l. 108) ;
   - `ordres/ordre-NNN.json` : `{"numero": n, "instance": "ID", "phase": "causal", "deja_usd": …}`.

   Puis poussée sur `refs/heads/ordres/sparks-exp7-nul-v5-$COURT`.
2. `depense projeter`, avec `egalite_lots` connu, puis `redemarrage`, puis `start` imprimé et « ENVOYÉ ».
3. L'amorce :
   - borne au moins 60 min (l. 220) ;
   - phase causale sous `timeout` (l. 224) : par lots si l'essai d'égalité est passé, sinon sans lots, déclaré ;
   - l'instance pousse `calcul/sparks-exp7-nul-causal-v5-$COURT-NNN` ;
   - « fin de la phase causale, code N, poussée vérifiée|non vérifiée » au journal ;
   - destruction par la minuterie **seulement** si le code est 0 et la poussée vérifiée (l. 229).
4. **Fin** :

   | Issue | Conduite |
   |---|---|
   | inventaire « absente » | destruction faite par la machine |
   | code non nul, ou poussée non vérifiée | l'instance sort sans se détruire ; nœud, puis destruction par l'identifiant sur ordre |

   Récupère la branche :
   ```
   git fetch origin refs/heads/calcul/sparks-exp7-nul-causal-v5-$COURT-NNN:refs/remotes/origin/calcul/sparks-exp7-nul-causal-v5-$COURT-NNN
   ```
   Puis `sha256sum -c`.

## F. Dépense, lignes d'arrêt, destruction
- **Avant chaque démarrage** : `depense projeter` (refus au-delà de 40 USD ; ni démarrage ni redémarrage ; destruction par
  l'identifiant ; nœud).
- **Sur la machine** : chaque démarrage est borné par `duree` (90 % de la marge, au plus 24 h). Les redémarrages comptent à la
  borne (registre, identifiants `nouvel_id`, l. 134).
- **Échéance absolue** : minuterie à 1795046400 (fin du 18 novembre), destruction par la clé du conteneur.
- **`depense instance "$E/etat.json"`** (l. 118 à 131) :

  | Décision | Conduite |
  |---|---|
  | « copier » | copier les sorties |
  | « detruire » | jouer la commande imprimée, avec `-y` |
  | « noeud » | à partir du 16 novembre sans fin en vue : nœud de Lazar |
  | « garder » | entre deux redémarrages |
- **Arrêt anticipé, sur nœud ou anomalie** : ordre « fin » poussé, puis `start`. L'amorce le traite avant la borne et se
  détruit (l. 206). Ou bien destruction directe : `bash scripts/lancer_sparks_exp7_nul_v9.sh destruction $ID`.
- **Clé du conteneur** : elle voit tout le compte. C'est un risque accepté et déclaré (R-1533).

## Rapport (à chaque fin de session, puis à la fin)
Heures `date -u` ; identifiant ; offre, rang, `PRIX_CARTE` et `PRIX_STOCKAGE` (règle à 120 Go) ; projections de
`depense projeter` ; lignes « AMORCE V5 » de chaque démarrage (`journal-amorce`) ; verdicts `boucle` ; têtes des branches
`calcul/…` et `ordres/…` (sha) ; contrôles `sha256sum -c` ; lignes du `journal.txt` permises ; dépense relevée et ligne
pour `registres/depenses.md` ; tout écart, toute relance (R4). Aucun score, aucune étiquette, aucune sortie brute de `vastai`.
