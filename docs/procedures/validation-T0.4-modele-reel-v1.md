# Procédure — validation du harnais sur modèle réel (T0.4) — v1

Rédigée le 2026-10-04, scellée le même jour avec le préenregistrement qu'elle applique : `prereg/T0.4-validation-modele-reel-v1.md`, sha256 `3d0589c80fe97b134b193a797881395ec710966867c47ca9e87506c187cb8c96`. Brouillon 5 relu par la contre-lecture 5 (`prereg/contre-lectures/T0.4-rapport-contre-lecture-5-v1.md`), corrections R-1, R-2, R-4 et R-6 intégrées.
GO de calcul : GO-2026-10-04-08 (devis de la phase 0, plafond 150 dollars).

## 1. Préalables

| # | quoi | état au 2026-10-04 |
|---|---|---|
| 1 | GO sur le devis de la phase 0 | accordé (GO-2026-10-04-08) |
| 2 | Préenregistrement scellé et contre-lu | scellé le 2026-10-04 après cinq contre-lectures (sha256 `3d0589c8…6c96`) |
| 3 | Accès réseau de l'environnement à `console.vast.ai` | ouvert par Lazar ; vérifié (recherche d'offres : réponse 200) |
| 4 | Clé `VAST_API_KEY` dans l'environnement | posée par Lazar ; visible à partir de la session suivante |
| 5 | Jetons pour l'instance : Hugging Face en lecture (licence Llama 3.1 acceptée) et GitHub à grain fin limité à `lciric/controle-ia` (contenu en lecture et écriture) | posés par Lazar : variables du compte Vast.ai (`HF_TOKEN`, `GH_TOKEN`), ou de l'environnement (`HF_TOKEN`, `CONTROLE_IA_GITHUB_TOKEN`) |

À l'ouverture de la session de lancement, vérifier les noms des variables présentes, sans jamais afficher leurs valeurs. Deux cas :
- si `HF_TOKEN` et `CONTROLE_IA_GITHUB_TOKEN` sont présentes dans l'environnement, elles se passent à l'instance par `--env` ;
- sinon, ce sont les variables du compte Vast.ai qui servent. Le journal de l'amorce le confirme (« clonage impossible » sinon).

Jamais de jeton à l'écran ni dans le dépôt :
- `vastai show instance --raw` contient les variables de l'instance, donc les jetons. On n'en affiche que les champs utiles (identifiant, état, prix, carte) ;
- les commandes citent `$HF_TOKEN`, jamais une valeur.

## 2. Contrôles avant toute dépense

`COMMIT` est le commit de scellement du préenregistrement : celui qui a ajouté son empreinte compagnon. Trois contrôles, tous sur ce commit :

```
COMMIT=$(git log --diff-filter=A -1 --format=%H -- prereg/T0.4-validation-modele-reel-v1.md.sha256)
git show "$COMMIT":scripts/amorce_instance_t04.sh | sha256sum         # doit égaler l'empreinte citée
git show "$COMMIT":scripts/validation_t04_instance.sh | sha256sum     # doit égaler l'empreinte citée
git diff --stat 3a7b5e0523864f386c7ef528b663dbae83e046dd "$COMMIT" -- . ':(exclude)prereg' ':(exclude)brouillons' \
  ':(exclude)registres' ':(exclude)docs' ':(exclude)diag' ':(exclude)runs' ':(exclude)donnees' ':(exclude)livrables' \
  ':(exclude)papiers' ':(exclude)traces' ':(exclude)CLAUDE.md'                  # doit être vide
```

- Le dernier contrôle est celui que le lanceur refait sur l'instance (arbre gelé). Le faire avant le lancement évite de payer un refus.
- L'arbre gelé comprend `.claude/` (réglages et gardes de la session), les fichiers de la racine et les dépendances. Entre le commit cité et le scellement, ne rien committer hors des dossiers documentaires et des sorties ; sinon, revenir au contenu du commit cité avant de sceller.
- Puis, sur le dépôt au commit de scellement : `problemes()` de `controle_ia.prereg` rend une liste vide pour le préenregistrement, son empreinte compagnon est vérifiée (`python -m controle_ia.scellement verifier prereg/T0.4-validation-modele-reel-v1.md`), et `verifier-arbre` dit « arbre intact ».

## 3. Offre

Critères (R-032 et R-033, contre-lectures 1 et 2) :
- une carte de 80 Go (A100 ou H100), `gpu_ram ≥ 79` ;
- version CUDA maximale ≥ 13.0 ;
- offre vérifiée, en centre de données, à la demande (pas d'enchère), fiabilité ≥ 0,99 ;
- mémoire vive ≥ 96 Go (marge sur la garde de 64 Go du lanceur), disque ≥ 80 Go ;
- à critères égaux, la moins chère.

Recherche, sans dépense :

```
vastai search offers "gpu_name in [A100_SXM4,A100_PCIE,H100_SXM,H100_PCIE,H100_NVL] gpu_ram>=79 num_gpus=1 cuda_vers>=13.0 verified=true datacenter=true reliability>=0.99 cpu_ram>=96 disk_space>=80 rentable=true" -o 'dph_total' --storage 80 --raw
```

Le 2026-10-04 vers 12:30 UTC, une recherche voisine (`cpu_ram>=64`, sans `gpu_ram`) rendait 4 offres :
- une A100 SXM4 à 0,75 dollar de l'heure, avec 64 Go de mémoire vive, trop juste ;
- puis des H100 à 2,85 dollars de l'heure et plus.

Les offres changent vite : la session de lancement refait la recherche. Avant de créer l'instance, elle consigne dans `registres/depenses.md` l'offre retenue, son prix horaire et le coût au plafond (6 heures × prix, plus le stockage), qui doit tenir dans le GO.

Durée attendue : 1 à 2 heures en tout. Plafond : 6 heures, **cumulées** sur toutes les tentatives.

## 4. Lancement (mode « args » : le conteneur exécute l'amorce, puis s'arrête)

L'amorce s'encode depuis le commit de scellement, après les contrôles de la section 2. La commande cite le GO, sinon la garde de calcul la bloque :

```
GO_ID=GO-2026-10-04-08 vastai create instance <offre> --image python:3.11-bookworm --disk 80 \
  --env "-e COMMIT=$COMMIT -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" \
  --entrypoint bash --args -c "echo $(git show "$COMMIT":scripts/amorce_instance_t04.sh | base64 -w0) | base64 -d > /root/amorce.sh && bash /root/amorce.sh"
```

- Si les jetons sont des variables du compte Vast.ai, `--env` ne porte que `COMMIT`.
- Consigner aussitôt l'identifiant de l'instance et l'heure de création dans `registres/etat.md` (instances actives).
- L'amorce clone le dépôt au commit, puis lance `scripts/validation_t04_instance.sh`. Celui-ci enchaîne :
  - la mise en place ;
  - les 178 tests : sortie standard aux runs, sortie d'erreur aux traces ;
  - la révision citée par le préenregistrement ;
  - le run A, commit et poussée ; puis le run B (rejeu entre processus), commit ;
  - les traces scellées et la poussée sur `calcul/t04-validation`.
- Délais figés :
  - TERM à 155 minutes par run (limite interne de 2 h 30), KILL cinq minutes plus tard ;
  - plafond de l'amorce à 345 minutes, KILL cinq minutes plus tard. Au TERM du plafond, le script d'instance transmet le signal au run en cours par son identifiant de processus, consigne l'arrêt et pousse. L'amorce verse ensuite ses propres traces (`traces/t04-plafond-…`).
- Filet de sortie : après la création de la branche de travail, toute sortie en échec du script d'instance que rien n'a consignée (mise en place, tests, commande en échec) consigne l'arrêt, verse les traces et pousse, en gardant le code de sortie.

## 5. Suivi

- Attendre en arrière-plan, sans `sleep` au premier plan : une boucle de surveillance interroge l'état (`vastai show instance <ID>`, champs utiles seulement) et la fin du journal (`vastai logs <ID>`) toutes les 5 minutes environ. Elle s'arrête à la ligne « AMORCE … fin, code N », ou à 6 heures depuis la création.
- Archiver le journal de l'instance (`vastai logs <ID>`) dans `traces/` du dépôt, scellé (`sha256sum`), dans la session de pilotage. C'est le seul témoin d'un arrêt d'avant le clonage (clonage impossible, commit introuvable, instance déjà utilisée) ou d'un KILL, et le témoin le plus complet de tous les autres.
- Ne rien relancer avec un paramètre changé : il faudrait une nouvelle version du préenregistrement.
- Relancement, selon la table du préenregistrement :
  - **cause d'infrastructure** (réseau, y compris pendant la mise en place ; instance perdue ; durée ou plafond de l'amorce, pour un run qui n'était pas complet) : un seul relancement à l'identique de A et de B. Il se fait sur une **instance neuve**, avec la même commande plus `-e BRANCHE=calcul/t04-validation-relance` dans `--env`. Il doit tenir dans le reste des 6 heures cumulées ; sinon, nœud et nouveau GO. Il se consigne (`registres/decisions.md`, `registres/depenses.md`) ;
  - **cause déterministe** (noyau refusé par le mode déterministe, mémoire insuffisante, tests en échec, mise en place en échec hors réseau : image, roue, pilote, carte absente) : aucun relancement ; nœud ;
  - **cause indéterminée** après lecture des traces et du journal : aucun relancement ; nœud ;
  - une paire A/B complète (résumés sans arrêt consigné ; pour B, avec la comparaison) ne se relance pas, même si le plafond frappe ensuite. Si B n'est pas complet, A et B se relancent ensemble, même si A l'était ;
  - A et B complets sur l'instance, résultats non poussés (« poussée impossible ») : lecture suspendue. Récupérer les fichiers sur le disque de l'instance arrêtée si elle le permet, puis lire comme d'ordinaire ; sinon, nœud (relancement de A et de B dans le plafond cumulatif, sur décision) ;
  - un commit « plafond de l'amorce atteint » ne prouve pas le plafond : l'amorce le pose pour tout code 124 ou 137. Si ce code arrive bien avant 345 minutes (heures des lignes « AMORCE »), avec « sortie imprévue (code 137) » dans le journal, c'est une commande tuée, en général faute de mémoire : cause déterministe, aucun relancement, nœud ;
  - l'amorce refuse de tourner deux fois sur la même instance (dossiers d'un essai précédent présents).

## 6. Fin

1. Arrêter l'instance **par son identifiant** : `vastai stop instance <ID>` (R10), dès la ligne de fin de l'amorce, à tout arrêt, ou au plafond.
   - Pas de destruction avant le verdict du critère 1 : le disque garde les gros tableaux (`donnees/`).
   - Consigner l'arrêt dans `registres/arrets.md`, et la dépense (heures × prix, plus stockage) dans `registres/depenses.md`.
2. Récupérer la branche `calcul/t04-validation` (ou `-relance`), vérifier les empreintes (`verifier-arbre`, et `sha256sum -c empreintes.sha256` dans chaque dossier de `traces/`), fusionner dans `main`.
3. Consigner la révision figée et le domaine de validité observé dans `registres/decisions.md`.
4. Faire prononcer le verdict du critère 1 de G0 par un sous-agent neuf, contre la lecture gelée (R13). Le sceller, puis le soumettre à Lazar.
5. Après le verdict : décider de la destruction de l'instance, et produire le zip versionné des livrables de T0.4 (R12).
