# Ordre de la mère à la fille — R1 v4 : lancement des deux sessions sous GO-2026-11-03-03 — v1

Écrit le 4 novembre 2026 (heure au commit, `date -u`) par la session mère `session_01Qi7Gr6NLmhhAcdmnACBC7G` (conv-audit fusionnée avec session-depot). Destinataire : la fille `session_01Qi7Gr3s7JVgpRP17VcSyAf`. **Ceci est la « commande exacte de conv-audit »** qu'exigent le texte scellé (« Étape 1 », « Liste d'arrêt ») et la ligne `GO-2026-11-03-03`. Tu es la session de pilotage (tu portes les clés) ; tout ce qui n'est pas écrit ici suit le texte scellé, qui prime.

## Pièces
- Texte scellé : `prereg/R1-addendum-relance-v4.md`, sha256 `0f10881b32fa4c0e5ec1eb02cf88fbd0fcb6ad13f70b59abc2d84e45a99f61c8`, commit de scellement **`937f13177892933955c9c34839b4b45a4db745df`**, branche `prep/r1-relance-v4`. Lis-le en entier d'abord, surtout « Plan d'analyse » (étapes 1 à 4), « Liste d'arrêt », « Coût et GO », et l'écart V4-E12 (gardes de dépense).
- Contre-lectures faites, contrôles d'avant l'installation rejoués au commit de scellement (`docs/notes/runs-r1-r2-r4-v1/relance-v4-scellement-v1/controles-avant-installation-commit-scellement-v1.md` sur `main`), concordance d'un lecteur neuf : voir le message qui t'envoie cet ordre (chemin et empreinte).
- Dépenses déjà imputées à `GO-2026-11-03-03` : **0 USD** (`registres/depenses.md` de `main`, aucune ligne ; revérifie).

## Règles constantes
- Jamais lire, afficher ni écrire une clé ; les jetons passent par nom (`$HF_TOKEN`, `$CONTROLE_IA_GITHUB_TOKEN`).
- Arrêt et destruction **par l'identifiant d'instance seulement** (R10). Aucune lecture brute du journal de l'instance : tout journal passe par `filtrer` ou `surveiller` du module de garde (lecture aveugle) ; jamais un score ni un tableau d'activations.
- Tout `git fetch` avec refspec explicite ; aucune ref `donnees/…` en plus ; tu peux lire et pousser les seules branches `calcul/r1-v4-temoin-reel-v1` et `calcul/r1-v4-reparation-reel-v1` (créées par l'instance) et pousser sur `prep/r1-relance-v4` le seul commit de versement du témoin (étape B5).
- Garde des secrets à 0 avant tout commit. Toute anomalie hors de ce qui est écrit : tu détruis l'instance par son identifiant si elle tourne, tu t'arrêtes et tu me le dis.

## A. Avant chaque création (sessions 1 et 2)
1. `date -u` ; `GO-2026-11-03-03` valide ce jour (échéance 17 novembre, non révoqué) dans `registres/go.md` du dépôt d'où part la commande (`/home/user/controle-ia-travail`, branche `main` à jour).
2. Arbre de l'outil : `git fetch origin refs/heads/prep/r1-relance-v4:refs/remotes/origin/prep/r1-relance-v4` ; arbre à part au commit lancé (session 1 : `937f1317…` ; session 2 : commit du versement, B5) ; `git status --porcelain` vide ; `PYTHONPATH=src python -m controle_ia.scellement verifier prereg/R1-addendum-relance-v4.md prereg/R1-reparation-v4-config-v2.json prereg/R1-rejeu-config-v6.json prereg/R1-table-tokenisation-v3.json prereg/R1-R2-rejeu-p3-v1.md` : cinq OK.
3. Épreuves des gardes de dépense, consignées : `PYTHONPATH=src python -m controle_ia.runs_nuit.garde_depense_v4_v1 epreuves` → toutes conformes, sinon arrêt.
4. `VB=/opt/vastai-venv-v1/bin` (ou ton binaire `vastai` épinglé ; dis lequel) ; `$VB/vastai show instances` : aucune instance oubliée ; offre :
   ```
   FILTRE="gpu_name=A100_SXM4 gpu_ram>=79 num_gpus=1 cuda_vers>=13.0 datacenter=true reliability>=0.98 inet_down>=500 disk_space>=80 rentable=true dph_total<=1.40"
   $VB/vastai search offers "$FILTRE" -o 'dph_total' --storage 80
   ```
   `OFFRE` = la moins chère des conformes ; aucune : nœud, tu t'arrêtes et tu me le dis.

## B. Session 1 — témoin
1. Création (exacte ; `COMMIT=937f13177892933955c9c34839b4b45a4db745df`) :
   ```
   B64=$(git show "$COMMIT:scripts/amorce_instance_r1_v4_v2.sh" | base64 -w0)
   GO_ID=GO-2026-11-03-03 $VB/vastai create instance "$OFFRE" --raw --image python:3.11-bookworm --disk 80 --cancel-unavail \
       --label r1-v4-temoin \
       --env "-e COMMIT=$COMMIT -e SESSION=temoin -e BRANCHE=calcul/r1-v4-temoin-reel-v1 -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e PLAFOND_AMORCE_MIN=180 -e DELAI_ETAPE_MIN=120 -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" \
       --entrypoint bash --args -c "echo $B64 | base64 -d > /root/amorce.sh && bash /root/amorce.sh"
   ```
   Consigne aussitôt `ID`, `T0` (heure de création, `date -u`), prix horaire de l'offre, disque estimé (prix de stockage de l'offre × 80 Go, sur `H`).
2. **Armement des deux tâches planifiées** (V4-E12), dans les 10 minutes : `PYTHONPATH=src python -m controle_ia.runs_nuit.garde_depense_v4_v1 heure --T0 <T0> --prix <prix> --disque <disque> --imputees 0` donne l'heure de destruction (marge nulle ou négative : destruction immédiate par l'identifiant). Prompts par `prompt_tache("verification"|"destruction", "temoin", valeurs)` (valeurs : `identifiant`, `T0`, `prix_horaire`, `disque`, `deja_imputees`, `heure_destruction`), écrits tels quels, suivis d'**une seule ligne de localisation** hors champs (le module n'est pas sur `main`) : « Code des règles : `git fetch origin refs/heads/prep/r1-relance-v4:refs/remotes/origin/prep/r1-relance-v4`, commit `937f13177892933955c9c34839b4b45a4db745df`, `PYTHONPATH=src`. » ; vérifie que `lire_prompt` rend les mêmes champs avec et sans cette ligne (écart de pilotage déclaré au rapport, sans effet sur une règle) ; tâche (i) : `create_trigger`, nouvelle session à chaque tir, toutes les heures ; tâche (ii) : `create_trigger`, nouvelle session, `run_once_at` = heure de destruction ; notifications poussées. Puis second listing (`list_triggers`), `lire_prompt` et `exiger_armement` sur chacun : un refus → destruction par l'identifiant et arrêt. Envoie-moi aussitôt la ligne de dépense (identifiant, `T0`, prix, `H`, heure de destruction, identifiants des deux tâches) : je l'écris dans `registres/depenses.md`.
3. Surveillance, toutes les 10 minutes environ : `$VB/vastai show instance <ID>` ; `$VB/vastai logs <ID> | PYTHONPATH=src python -m controle_ia.runs_nuit.garde_depense_v4_v1 surveiller --session temoin --tests 381` (**`--tests 381` obligatoire** : sans lui le défaut, 358, ferait détruire une instance saine) ; « detruire » → destruction par l'identifiant, sans autre lecture ; `git ls-remote origin refs/heads/calcul/r1-v4-temoin-reel-v1`.
4. Fin : à `etape=fin` (ou fin de l'amorce lue par le filtre), vérifie que la branche est poussée, **détruis l'instance par son identifiant**, vérifie `show instances`, supprime les deux tâches (`delete_trigger`), dépense réelle relevée.
5. **Versement du témoin** : récupère `calcul/r1-v4-temoin-reel-v1` par refspec ; si `diag/<run>/arret.json` existe : arrêt, tu me le dis (pas de session 2). Sinon, sur `prep/r1-relance-v4` à partir de `937f1317`, un commit neuf qui ajoute **seulement** `runs/<run>/` et `diag/<run>/` copiés à l'octet (empreintes comparées) ; aucun autre fichier ; garde des secrets à 0 ; poussée sur `prep/r1-relance-v4`. Ne lis pas le contenu des résultats (seulement l'existence des fichiers, leurs sceaux et `arret.json`). Message à la mère : identifiant, dépense, run, commit du versement.

## C. Session 2 — réparation, table v4, rejeu (sans attendre ma réponse si B5 est conforme)
1. A, au commit du versement (`COMMIT=<commit du versement>`), avec `--imputees` = dépense réelle de la session 1 (et de toute reprise).
2. Création : la commande de B1 avec `--label r1-v4-reparation` et `--env "-e COMMIT=$COMMIT -e SESSION=reparation -e TEMOIN_RUN=<run> -e BRANCHE=calcul/r1-v4-reparation-reel-v1 -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e PLAFOND_AMORCE_MIN=2200 -e DELAI_ETAPE_MIN=2100 -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN"`.
3. Armement comme B2 (session `reparation`) ; surveillance comme B3 avec `--session reparation --tests 381` ; fin comme B4.
4. Rien n'est versé sur `calcul/r1-r2-reel-v1` ni lu : la récupération attend la fiche de réception v4 de la mère (étape 4 du texte).

## D. Reprise
Une seule par session, sur erreur d'infrastructure seulement (V4-E16 : clonage, installation, préchargement, carte indisponible, perte de l'instance, poussée refusée), jamais sur une garde, branche suffixée `-v2`, dépense cumulée recalculée (`--imputees`). Sinon : arrêt et message.

## Rapport
Court, scellé, sur `canal/fille-2026-11-04` : commits, identifiants, heures, dépenses, sorties des épreuves et de `surveiller` (filtrées), écarts. Message à la mère à chaque fin de session.
