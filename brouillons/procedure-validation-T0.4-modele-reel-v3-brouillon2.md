# Procédure — validation du harnais sur modèle réel (T0.4) — v3

Rédigée le 2026-10-05, scellée avec le préenregistrement qu'elle applique : `prereg/T0.4-validation-modele-reel-v2.md` (empreinte compagnon au scellement).
GO de calcul : GO-2026-10-04-08 (devis de la phase 0, plafond 150 dollars). GO de la version 2 : GO-2026-10-05-01 (N-010, option a).

**Version 3.** Elle remplace la version 2 (`docs/procedures/validation-T0.4-modele-reel-v2.md`, sha256 `e8a596c35f4f5e57c102f247cd39feed7debed8860b47ed2cb12d9bbcd7eb634`, gardée scellée), qui appliquait le préenregistrement v1. Ce qui change :
- préenregistrement v2 (logique en double précision, normalisations comprises, contrôle positif D1, réglages relus), code cité `dc7aa7fcd6b5b0c676ec7365d2a194a3c1924efc`, 192 tests ;
- carte de 141 Go (H200 ou H200 NVL) au lieu de 80 Go, garde de 130 Gio ; mémoire vive d'au moins 128 Go dans l'offre (garde de 96 Go) ;
- branche de résultats `calcul/t04-validation-v2` (défaut du script d'instance) ; relancement sur `calcul/t04-validation-v2-relance` ;
- plafond cumulatif : 0,56 heure déjà consommée sur 6 (`registres/depenses.md`) ; la surveillance est réglée sur le reste, moins 5 minutes.
Le reste (jetons, mode « args », surveillance, arrêt, destruction) est repris de la version 2. Le script de surveillance scellé (`docs/procedures/surveiller-instance-t04-v1.sh`) est inchangé ; son en-tête renvoie encore à la procédure v2.

## 1. Préalables

| # | quoi | état au 2026-10-05 |
|---|---|---|
| 1 | GO sur le devis de la phase 0 | accordé (GO-2026-10-04-08) |
| 2 | GO de la version 2 | accordé (GO-2026-10-05-01, N-010 option a) |
| 3 | Préenregistrement v2 scellé et contre-lu | à sceller |
| 4 | Accès réseau à `console.vast.ai` ; clé `VAST_API_KEY` | vérifiés (sessions du 2026-10-05) |
| 5 | Jetons de l'instance : Hugging Face en lecture (licence acceptée), GitHub à grain fin (`lciric/controle-ia`, contenu en lecture et écriture) | `HF_TOKEN`, `CONTROLE_IA_GITHUB_TOKEN` dans l'environnement ; jeton GitHub corrigé par Lazar le 2026-10-05 (N-009), vérifié par le clonage et la poussée des instances 54298522 et 54311651 |

À l'ouverture de la session de lancement, vérifier les noms des variables présentes, sans jamais afficher leurs valeurs. Deux cas :
- si `HF_TOKEN` et `CONTROLE_IA_GITHUB_TOKEN` sont présentes dans l'environnement, elles se passent à l'instance par `--env` ;
- sinon, ce sont les variables du compte Vast.ai qui servent. Le journal de l'amorce le confirme (« clonage impossible » sinon).

Jamais de jeton à l'écran ni dans le dépôt :
- `vastai show instance --raw` contient les variables de l'instance, donc les jetons. On n'en affiche que les champs utiles (identifiant, état, prix, carte) ;
- les commandes citent `$HF_TOKEN`, jamais une valeur ;
- la réponse de `vastai create` contient une clé de l'instance (`instance_api_key`), et un message d'erreur peut recopier la requête : ses deux sorties passent par le filtre de la section 4, qui ne garde que le succès et l'identifiant.

## 2. Contrôles avant toute dépense

`COMMIT` est le commit de scellement du préenregistrement v2 : celui qui a ajouté son empreinte compagnon. Trois contrôles, tous sur ce commit :

```
COMMIT=$(git log --diff-filter=A -1 --format=%H -- prereg/T0.4-validation-modele-reel-v2.md.sha256)
git show "$COMMIT":scripts/amorce_instance_t04.sh | sha256sum         # doit égaler l'empreinte citée
git show "$COMMIT":scripts/validation_t04_instance.sh | sha256sum     # doit égaler l'empreinte citée
git diff --stat dc7aa7fcd6b5b0c676ec7365d2a194a3c1924efc "$COMMIT" -- . ':(exclude)prereg' ':(exclude)brouillons' \
  ':(exclude)registres' ':(exclude)docs' ':(exclude)diag' ':(exclude)runs' ':(exclude)donnees' ':(exclude)livrables' \
  ':(exclude)papiers' ':(exclude)traces' ':(exclude)CLAUDE.md'                  # doit être vide
```

- Le dernier contrôle est celui que le lanceur refait sur l'instance (arbre gelé). Le faire avant le lancement évite de payer un refus.
- Entre le commit cité et le scellement, ne rien committer hors des dossiers documentaires et des sorties.
- Puis, sur le dépôt au commit de scellement : `problemes()` de `controle_ia.prereg` rend une liste vide pour le préenregistrement v2, son empreinte compagnon est vérifiée (`python -m controle_ia.scellement verifier prereg/T0.4-validation-modele-reel-v2.md`), et `verifier-arbre` dit « arbre intact ».

## 3. Offre

Critères (préenregistrement v2, Plan d'analyse, Machine ; note `docs/notes/memoire-double-precision-T0.4-v1.md`) :
- une carte de 141 Go : H200 ou H200 NVL ; `gpu_ram ≥ 139`. Sans offre conforme : nœud (pas d'autre carte sans accord de Lazar) ;
- version CUDA maximale ≥ 13.0 ;
- offre vérifiée, en centre de données, à la demande (pas d'enchère), fiabilité ≥ 0,99 ;
- mémoire vive ≥ 128 Go (marge sur la garde de 96 Go), disque ≥ 80 Go ;
- à critères égaux, la moins chère.

Recherche, sans dépense :

```
vastai search offers "gpu_name in [H200,H200_NVL] gpu_ram>=139 num_gpus=1 cuda_vers>=13.0 verified=true datacenter=true reliability>=0.99 cpu_ram>=128 disk_space>=80 rentable=true" -o 'dph_total' --storage 80 --raw
```

Le 2026-10-05 vers 12:20 UTC, une recherche voisine (fiabilité ≥ 0,98, mémoire vive ≥ 96 Go ; non archivée) rendait une H200 à 4,145 dollars de l'heure (CUDA 13.2, pilote 595.71.05, 252 Go de mémoire vive, fiabilité 0,9905), des H200 NVL de 5,50 à 5,87 dollars et une B200 à 9,48 dollars.

Coût au plafond cumulatif (5,44 heures d'horloge, plus le stockage) : environ 22,5 dollars sur une H200 à 4,145 dollars de l'heure, environ 32 dollars sur une H200 NVL à 5,87 dollars ; attendu : 4 à 8 dollars (1 à 1,5 heure).

Les offres changent vite : la session de lancement refait la recherche et archive sa sortie (champs utiles) dans `traces/`, scellée. Avant de créer l'instance, elle consigne dans `registres/depenses.md` l'offre retenue, son prix horaire et le coût au plafond (reste cumulatif × prix, plus le stockage), qui doit tenir dans le GO.

Durée attendue : 1 à 1,5 heure (A et B). Plafond : 6 heures **cumulées** sur toutes les tentatives de la v1 et de la v2 ; reste 5,44 heures au 2026-10-05.

## 4. Lancement (mode « args » : le conteneur exécute l'amorce ; à sa sortie, il redémarre et la relance : seule la session arrête l'instance)

L'amorce s'encode depuis le commit de scellement, après les contrôles de la section 2. La commande cite le GO, sinon la garde de calcul la bloque :

```
GO_ID=GO-2026-10-04-08 vastai create instance <offre> --image python:3.11-bookworm --disk 80 \
  --env "-e COMMIT=$COMMIT -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" \
  --entrypoint bash --args -c "echo $(git show "$COMMIT":scripts/amorce_instance_t04.sh | base64 -w0) | base64 -d > /root/amorce.sh && bash /root/amorce.sh" \
  --raw 2>&1 | python3 -c 'import json, sys
t = sys.stdin.read()
try:
    d = json.loads(t)
    print("succès :", d.get("success"), "; identifiant :", d.get("new_contract"))
except Exception:
    print("réponse illisible (non affichée, elle peut contenir des jetons) ; vérifier par vastai show instances")'
```

- Sans `BRANCHE`, les résultats vont sur `calcul/t04-validation-v2` (défaut du script d'instance au commit cité). La branche de la v1 (`calcul/t04-validation`) existe déjà : ne pas la viser.
- Consigner aussitôt l'identifiant de l'instance et l'heure de création dans `registres/etat.md` (instances actives).
- L'amorce clone le dépôt au commit, puis lance `scripts/validation_t04_instance.sh`. Celui-ci enchaîne :
  - la mise en place ;
  - les 192 tests : sortie standard aux runs, sortie d'erreur aux traces ;
  - la révision citée par le préenregistrement v2 ;
  - le run A, commit et poussée ; puis le run B (rejeu entre processus), commit ;
  - les traces scellées et la poussée.
- Délais figés :
  - TERM à 155 minutes par run (limite interne de 2 h 30), KILL cinq minutes plus tard ;
  - plafond de l'amorce à 345 minutes, KILL cinq minutes plus tard. Il dépasse le reste cumulatif (5,44 heures) : c'est la surveillance qui fait tenir le plafond cumulatif, en rendant la main à son terme pour que la session arrête l'instance.
- Filet de sortie : après la création de la branche de travail, toute sortie en échec du script d'instance que rien n'a consignée (mise en place, tests, commande en échec) consigne l'arrêt, verse les traces et pousse, en gardant le code de sortie.

## 5. Suivi

- Lancer en arrière-plan, sans `sleep` au premier plan, le script de surveillance :
  `bash docs/procedures/surveiller-instance-t04-v1.sh <ID> <création − 2 316 s> <dossier de travail de la session>`.
  - Le second argument retranche de la date de création (secondes depuis l'époque) les 0,56 heure déjà consommées (2 016 s) et 5 minutes pour le délai d'interrogation (300 s) : le motif PLAFOND tombe ainsi un peu avant le terme du reste cumulatif de 5,44 heures, et l'arrêt par l'identifiant suit à quelques minutes près. À chaque tentative suivante, retrancher le total consommé.
  - Le libellé du motif reste « PLAFOND : 6 heures depuis la création » : il désigne ce reste. Ce terme tombe avant le plafond de l'amorce (345 minutes) : un run encore en cours n'est pas consigné (pas d'`arret.json`) ; c'est la ligne d'infrastructure « durée » de la table ; les traces restent sur le disque de l'instance arrêtée.
  - Le script relève l'état (champs utiles seulement) et le journal (`vastai logs <ID> --tail 20000`) toutes les 2 minutes, jetons masqués. Il sort sur l'un de cinq motifs : FIN, ÉCHEC D'AMORCE, REDÉMARRAGE, ÉTAT TERMINAL, PLAFOND.
  - À sa sortie, quel que soit le motif, la session arrête l'instance **aussitôt**, par son identifiant (section 6).
  - Une tâche de fond dure au plus 2 heures : la réarmer jusqu'à la sortie.
- Archiver le journal de l'instance (`vastai logs <ID> --tail 20000`, jetons masqués) dans `traces/` du dépôt, scellé (`sha256sum`), dans la session de pilotage.
- Ne rien relancer avec un paramètre changé : il faudrait une version 3 du préenregistrement.
- Relancement, selon la table du préenregistrement v2 :
  - **cause d'infrastructure** (réseau, y compris pendant la mise en place ; instance perdue ; durée ou plafond de l'amorce, pour un run qui n'était pas complet) : un seul relancement à l'identique de A et de B, sur une **instance neuve**, avec la même commande plus `-e BRANCHE=calcul/t04-validation-v2-relance` dans `--env`. Il doit tenir dans le reste cumulatif ; sinon, nœud et nouveau GO. Il se consigne (`registres/decisions.md`, `registres/depenses.md`) ;
  - **cause déterministe** (noyau refusé par le mode déterministe, mémoire insuffisante, tests en échec, mise en place en échec hors réseau : image, roue, pilote, carte absente) : aucun relancement ; nœud ;
  - **cause indéterminée** après lecture des traces et du journal : aucun relancement ; nœud ;
  - une paire A/B complète (résumés sans arrêt consigné ; pour B, avec la comparaison) ne se relance pas, même si le plafond frappe ensuite. Si B n'est pas complet, A et B se relancent ensemble, même si A l'était ;
  - A et B complets sur l'instance, résultats non poussés (« poussée impossible ») : lecture suspendue ; récupérer les fichiers sur le disque de l'instance arrêtée si elle le permet, puis lire comme d'ordinaire ; sinon, nœud ;
  - un commit « plafond de l'amorce atteint » ne prouve pas le plafond : l'amorce le pose pour tout code 124 ou 137. Si ce code arrive bien avant 345 minutes (heures des lignes « AMORCE »), avec « sortie imprévue (code 137) » dans le journal, c'est une commande tuée, en général faute de mémoire : cause déterministe, aucun relancement, nœud ;
  - l'amorce refuse de tourner deux fois sur la même instance (dossiers d'un essai précédent présents) ;
  - un échec d'avant le clonage (jeton refusé, commit introuvable) n'est pas un arrêt de A ou de B : aucun run n'a commencé. Corriger la cause (les jetons relèvent de Lazar : nœud), puis relancer sur une instance neuve, dans le reste cumulatif.

## 6. Fin

1. Arrêter l'instance **par son identifiant** : `vastai stop instance <ID>` (R10), dès la ligne de fin de l'amorce, à tout arrêt, ou au plafond.
   - Pas de destruction avant le verdict du critère 1 : le disque garde les gros tableaux (`donnees/`).
   - Consigner l'arrêt dans `registres/arrets.md`, et la dépense (heures × prix, plus stockage) dans `registres/depenses.md`.
2. Récupérer la branche `calcul/t04-validation-v2` (ou `-relance`), vérifier les empreintes (`verifier-arbre`, et `sha256sum -c empreintes.sha256` dans chaque dossier de `traces/`), fusionner dans `main`.
3. Consigner le domaine de validité observé (dont le plus long contexte rempli) dans `registres/decisions.md`.
4. Faire prononcer le verdict du critère 1 de G0 par un sous-agent neuf, contre la lecture gelée du préenregistrement v2 (R13). Le sceller, puis le soumettre à Lazar.
5. Après le verdict : décider de la destruction de l'instance, et produire le zip versionné des livrables de T0.4 (R12).
6. La destruction d'une instance est irréversible : elle se soumet à Lazar, avec une recommandation.
