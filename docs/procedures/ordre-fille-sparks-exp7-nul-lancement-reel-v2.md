# Ordre de la mère à la fille — SPARKS-EXP7-NUL : expérience réelle sous GO-2026-11-04-04 — v2

Écrit le 5 novembre 2026 vers 07:30 UTC (`date -u`) par le rédacteur-développeur, pour la mère, qui le relit et l'envoie.
Il **remplace la v1** (`ordre-fille-sparks-exp7-nul-lancement-reel-v1.md`, gardée, R12), écrite sur le code v9.

**Ne vaut qu'une fois l'addendum scellé, et après un troisième tir conforme** (section A.2).

Code : `prep/sparks-exp7-nul-v11`, commit `cabc06e5d7e1c62c519990ed9709103c23cb08ec`, appelé `CODE`. Les lignes sont citées à ce
commit :
- lanceur `scripts/lancer_sparks_exp7_nul_v11.sh`, cité « lanceur, l. n » ;
- amorce `scripts/amorce_instance_sparks_exp7_nul_v11.sh`, citée « amorce, l. n ».

## Hypothèses
1. La mère remplit le marqueur du tir, écrit `prereg/SPARKS-EXP7-NUL-addendum-1.md` (nom lu par `garde_code`) et le scelle.
2. Elle pose un **commit enfant de `CODE`** sur `prep/sparks-exp7-nul-v11`, qui ajoute **ces trois fichiers seulement**, puis le
   pousse :
   - `prereg/SPARKS-EXP7-NUL-addendum-1.md` ;
   - son `.sha256` ;
   - **`registres/go.md` de `main`**, qui porte l'extension de GO-2026-11-04-04 à 40 USD (ligne 245).

   Sans ce registre, le lanceur (l. 203) et l'amorce (l. 277) refusent. La garde du code ne refuse que `src/`, `tests/` et
   `scripts/` dans `CODE..LANCE`.
3. La fille lance depuis ce commit, appelé `LANCE`, avec `COURT=${LANCE:0:12}`.

## Ce que le code v11 fait de plus que la v9 (à savoir avant de lancer)
- **Premier geste** : ligne `AMORCE V10 DEMARRAGE <n> : <date>, machine, commit` (amorce, l. 85), avec un compteur gardé sur
  le disque.
  - Outils absents (`curl`, `git`, …) : installés par `apt-get` sous `timeout` (l. 145 et suivantes).
  - Destruction de secours par `python3` si `curl` manque (`supprimer`, l. 94).
- **Tout refus avant l'ordre consommé détruit l'instance** (`refus`, l. 215 ; `boucle`, l. 253 ; `destruction_immediate`,
  l. 137). Cela vaut pour la création comme pour le redémarrage.
  - Si la destruction échoue : `sleep infinity`, dit au journal. La fille détruit alors par l'identifiant.
- **Fin normale de phase** (fabrication, quel que soit son code ; fenêtre de copie ; phase causale sans destruction) :
  `arreter_instance` (l. 189) met l'instance à l'état voulu « stopped » par l'interface de Vast (clé du conteneur).
  - Elle exige HTTP 2xx et `"success": true`, écrit « ARRÊT OBTENU », puis sort.
  - Sinon, elle écrit « ARRÊT NON OBTENU … perdus : les couches des modèles et du départ restées sur le disque », puis
    **détruit**. Seules restent alors les sorties légères poussées sur `calcul/…`.
- **Au redémarrage, sans ordre neuf** : boucle présumée, destruction (v9). L'ordre est donc **toujours poussé avant le
  `start`**.

## Règles constantes
Celles de l'ordre v1, inchangées :
- aucune clé lue ni affichée ;
- `vastai` seulement par les commandes imprimées par le lanceur, jouées telles quelles ;
- aucune sortie brute de `vastai` ;
- destruction par l'identifiant avec `-y` ;
- aucune lecture de résultat avant l'étape 4 du « Plan d'analyse » (seuls `journal.txt` et les lignes « AMORCE V ») ;
- toute anomalie : destruction par l'identifiant, arrêt, et tu me le dis.

## A. Préalables (avant la création, puis avant chaque redémarrage)
1. `date -u`.
   - GO-2026-11-04-04 valide (base l. 242, extension l. 245, échéance le 18 novembre, non révoqué).
   - `registres/depenses.md` : revérifie ce qui est imputé à ce GO.
2. **Troisième tir** (protocole de l'additif v11, section 5). Il doit avoir donné :
   - « ARRÊT OBTENU » ;
   - trois inventaires « exited » avec `cur_state` « stopped » sur au moins 5 minutes (verdict `boucle` : « arretee ») ;
   - après l'ordre « fin » et le `start`, `DEMARRAGES=2`, `BOUCLE=non`, puis « absente ».

   Tout autre résultat : aucune création, nœud de Lazar.
3. **Arbre au commit `LANCE`** :
   - `git rev-parse LANCE^` = `CODE` ;
   - `git diff --name-only CODE LANCE` = l'addendum, son `.sha256` et `registres/go.md`, rien d'autre.
4. **Épreuves des gardes**, dans cet arbre :
   - `sha256sum -c` du compagnon ;
   - `exiger_prereg_scelle` sur l'addendum ;
   - `garde_code lancement . CODE LANCE` (garde v11) → « LANCEMENT CONFORME » ;
   - `COMMIT_CODE=CODE PYTHONPATH=src python3 -m pytest -q tests/test_sparks_exp7_nul_v1.py … v4.py tests/test_sparks_exp7_nul_v11.py`
     → tous réussis (nombre à l'additif v11).
5. **Outils et branches** :
   - `vastai` 1.8.3 ; `$VAST_API_KEY`, `$CONTROLE_IA_GITHUB_TOKEN` et `$HF_TOKEN` présents, jamais affichés ;
   - ni `calcul/sparks-exp7-nul-v5-$COURT` ni `ordres/sparks-exp7-nul-v5-$COURT` n'existent ;
   - inventaire du compte sans sortie brute (ordre v1, A.7) ;
   - marqueur `$E/.creation-incertaine` absent.

## B. Offre, prix et état de dépense
Comme l'ordre v1, section B :
- recherche avec `'num_gpus=1 gpu_ram>=24 disk_space>=120 rentable=true verified=true'`, puis `offres` ;
- **`PRIX_STOCKAGE` = `storage_cost` × 120 ÷ 730** (et non la valeur imprimée par `offres`, faite pour 20 Go) ;
- `etat.json` avec **`"egalite_lots": false`** et 18 copies à la création ;
- `depense projeter` au plus 40 USD, sinon l'offre suivante ou un nœud.

## C. Session 1 — création, fabrication, arrêt
1. `bash scripts/lancer_sparks_exp7_nul_v11.sh creation OFFRE PRIX_CARTE PRIX_STOCKAGE LANCE CODE "$E/etat.json"`.
   - Le lanceur rejoue les gardes (l. 203 et suivantes).
   - Il imprime la création littérale (l. 212) : `GO_ID=GO-2026-11-04-04`, `--disk 120`, `ADDENDUM_SHA256` (l. 208),
     `GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN`, `HF_TOKEN=$HF_TOKEN`, échéance à la fin du 18 novembre (l. 195), amorce v11 tirée de
     `LANCE`.
   - **Joue-la telle quelle**, puis lis `apres-creation` (l. 76) comme à l'ordre v1, C.2.
2. **Surveillance** toutes les 30 min :
   - `inventaire` (l. 109) « running » ;
   - `journal-amorce FICHIER 1` (l. 121) : `DEMARRAGES=1`. `BOUCLE=oui` est un nœud.
3. **Fin de la fabrication** : le journal dit « fin de la fabrication, code N », puis « ARRÊT OBTENU (état voulu « stopped »
   … ) ».
   - Trois inventaires sur au moins 5 minutes, puis `boucle $ID` (l. 112) → « arretee ».
   - « ARRÊT NON OBTENU » ou instance « absente » : les couches sont perdues, nœud.
   - « boucle » : destruction imprimée, nœud.
4. **Versement, sans lecture** :
   ```
   git fetch origin refs/heads/calcul/sparks-exp7-nul-v5-$COURT:refs/remotes/origin/calcul/sparks-exp7-nul-v5-$COURT
   ```
   - `sha256sum -c` des sorties ; ne lire que `journal.txt` (ordre v1, C.6).
   - Mettre à jour `etat.json` : `egalite_lots` selon le journal, phases faites, heures.

## D. Copies par lots (chaque lot est un démarrage), puis lecteurs
Pour chaque lot :
1. Pousser l'ordre « copie » sur `refs/heads/ordres/sparks-exp7-nul-v5-$COURT` **avant** le `start`.
2. `depense projeter`, puis `redemarrage` (l. 217) et le `start` imprimé.
3. Le journal doit montrer :
   - `DEMARRAGES` = 1 + nombre de `start` envoyés (`journal-amorce FICHIER <ce nombre>`) ;
   - « ordre N (copie) accepté et consigné » ;
   - « COPIE prête ».
4. `vastai copy` (non éprouvé ; un échec est un nœud), puis `sha256sum -c MANIFESTE-LOT.txt`, puis la mise à disposition
   (procédure des lecteurs, point 6).
5. Au bout de `copie_minutes`, l'amorce **arrête l'instance** (« ARRÊT OBTENU »). Vérifie trois inventaires « exited » /
   « stopped » avant l'ordre suivant.

Ensuite viennent les lecteurs, puis l'**ouverture unique du coffre** (« Plan d'analyse », étape 4).

## E. Session 2 — contrôle causal
- Ordre « causal », avec `ordres/causal/cle-ouverte-v1.json` et `ordres/causal/reponses/<lecteur>/<cas>/reponse-v2.json`,
  poussé avant le `start`.
- Fin :
  - code 0 et poussée vérifiée : destruction par l'amorce (l. 347). Inventaire « absente » ;
  - sinon : « ARRÊT OBTENU », instance arrêtée, nœud de Lazar.
- Récupérer la branche :
  ```
  git fetch origin refs/heads/calcul/sparks-exp7-nul-causal-v5-$COURT-NNN:refs/remotes/origin/calcul/sparks-exp7-nul-causal-v5-$COURT-NNN
  ```

## F. Dépense, arrêts, rapport
Comme l'ordre v1, sections F et « Rapport ».

Pour une fin anticipée : pousser l'ordre « fin », puis `start`. L'amorce le traite avant la borne et se détruit (l. 320).
Sinon : `bash scripts/lancer_sparks_exp7_nul_v11.sh destruction $ID`.

Le rapport ajoute :
- les lignes « ARRÊT OBTENU / NON OBTENU » ;
- les comptes `DEMARRAGES` de chaque démarrage.
