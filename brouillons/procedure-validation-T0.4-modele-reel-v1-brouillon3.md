# Procédure — validation du harnais sur modèle réel (T0.4) — v1

Rédigée le 2026-10-04. Elle applique le préenregistrement `prereg/T0.4-validation-modele-reel-v1.md`, une fois scellé.
GO de calcul : GO-2026-10-04-08 (devis de la phase 0, plafond 150 dollars).

## 1. Préalables

| # | quoi | état au 2026-10-04 |
|---|---|---|
| 1 | GO sur le devis de la phase 0 | accordé (GO-2026-10-04-08) |
| 2 | Préenregistrement scellé et contre-lu | en cours (contre-lecture 3) |
| 3 | Accès réseau de l'environnement à `console.vast.ai` | ouvert par Lazar ; vérifié (recherche d'offres : réponse 200) |
| 4 | Clé `VAST_API_KEY` dans l'environnement | posée par Lazar ; visible à partir de la session suivante |
| 5 | Jetons pour l'instance : Hugging Face en lecture (licence Llama 3.1 acceptée) et GitHub à grain fin limité à `lciric/controle-ia` (contenu en lecture et écriture) | posés par Lazar : variables du compte Vast.ai (`HF_TOKEN`, `GH_TOKEN`), ou de l'environnement (`HF_TOKEN`, `CONTROLE_IA_GITHUB_TOKEN`) |

À l'ouverture de la session de lancement, vérifier les noms des variables présentes, sans jamais afficher leurs valeurs. Deux cas :
- si `HF_TOKEN` et `CONTROLE_IA_GITHUB_TOKEN` sont présentes dans l'environnement, elles se passent à l'instance par `--env` ;
- sinon, ce sont les variables du compte Vast.ai qui servent. Le journal de l'amorce le confirme (« clonage impossible » sinon).

## 2. Offre

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

Les offres changent vite : la session de lancement refait la recherche.

Durée attendue : 1 à 2 heures en tout. Plafond : 6 heures.

## 3. Lancement (mode « args » : le conteneur exécute l'amorce, puis s'arrête)

`COMMIT` est le commit de scellement du préenregistrement. L'amorce s'encode depuis ce commit, après contrôle de son empreinte citée par le préenregistrement :

```
COMMIT=<commit de scellement>
git show "$COMMIT":scripts/amorce_instance_t04.sh | sha256sum      # doit égaler l'empreinte citée
```

La commande cite le GO, sinon la garde de calcul la bloque :

```
GO_ID=GO-2026-10-04-08 vastai create instance <offre> --image python:3.11-bookworm --disk 80 \
  --env "-e COMMIT=$COMMIT -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" \
  --entrypoint bash --args -c "echo $(git show "$COMMIT":scripts/amorce_instance_t04.sh | base64 -w0) | base64 -d > /root/amorce.sh && bash /root/amorce.sh"
```

- Si les jetons sont des variables du compte Vast.ai, `--env` ne porte que `COMMIT`.
- L'amorce clone le dépôt au commit, puis lance `scripts/validation_t04_instance.sh`. Celui-ci enchaîne :
  - la mise en place ;
  - les 170 tests, dont la sortie va aux runs ;
  - la révision citée par le préenregistrement ;
  - le run A, commit, puis le run B (rejeu entre processus), commit ;
  - les traces et la poussée sur `calcul/t04-validation`.
- Délais figés : TERM à 155 minutes par run (limite interne de 2 h 30), KILL cinq minutes plus tard ; plafond de l'amorce à 345 minutes.

## 4. Suivi

- `vastai show instance <ID>` et `vastai logs <ID>`. Le journal de l'amorce se termine par « AMORCE … fin, code N ».
- Archiver le journal de l'instance (`vastai logs <ID>`) dans `traces/` du dépôt, dans la session de pilotage.
- Ne rien relancer avec un paramètre changé : il faudrait une nouvelle version du préenregistrement.
- Après une panne d'infrastructure, un seul relancement à l'identique de A et de B est permis, sur une instance neuve ou dans un dossier de travail neuf (`TRAVAIL`). Il se consigne.

## 5. Fin

1. Arrêter l'instance **par son identifiant** : `vastai stop instance <ID>` (R10).
   - Pas de destruction avant le verdict du critère 1 : le disque garde les gros tableaux (`donnees/`).
   - Consigner l'arrêt dans `registres/arrets.md`, et la dépense (heures × prix, plus stockage) dans `registres/depenses.md`.
2. Récupérer la branche `calcul/t04-validation`, vérifier les empreintes (`verifier-arbre`), fusionner dans `main`.
3. Consigner la révision figée et le domaine de validité observé dans `registres/decisions.md`.
4. Faire prononcer le verdict du critère 1 de G0 par un sous-agent neuf, contre la lecture gelée (R13). Le sceller, puis le soumettre à Lazar.
5. Après le verdict : décider de la destruction de l'instance, et produire le zip versionné des livrables de T0.4 (R12).
