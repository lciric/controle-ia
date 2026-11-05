# Procédure — validation du harnais sur modèle réel (T0.4) — v1

Rédigée le 2026-10-04. Elle applique le préenregistrement `prereg/T0.4-validation-modele-reel-v1.md`, une fois scellé. Rien ne se lance avant le GO de Lazar sur le devis de la phase 0 (nœud N-002).

## 1. Préalables

| # | quoi | qui | état au 2026-10-04 |
|---|---|---|---|
| 1 | GO sur le devis de la phase 0 (150 dollars), consigné dans `registres/go.md` | Lazar | en attente (N-002) |
| 2 | Préenregistrement scellé et contre-lu | moi | en cours |
| 3 | Compte de location de machines de calcul (Vast.ai) | Lazar | à fournir |
| 4 | Jeton Hugging Face en lecture, licence de Llama 3.1 acceptée sur le compte | Lazar | à fournir |
| 5 | Jeton GitHub à grain fin, limité au dépôt `lciric/controle-ia` (lecture et écriture du contenu), pour que l'instance récupère le code et pousse ses résultats | Lazar | à fournir |

Qui lance l'instance :
- **Lazar lance**, en suivant les sections 2 à 5 : rien à changer dans cet environnement. C'est l'option recommandée pour la première session.
- **Je lance** : il faut alors trois choses.
  - L'accès réseau de cet environnement doit autoriser `console.vast.ai`.
  - Une variable d'environnement `VAST_API_KEY` doit être ajoutée dans les réglages de l'environnement. Jamais dans la conversation ni dans le dépôt.
  - L'outil `vastai` doit être installé.
  La garde de calcul bloque tout lancement qui ne cite pas un GO valide (`GO_ID=GO-AAAA-MM-JJ-NN …`).

Les jetons vivent dans les variables d'environnement de l'instance (`HF_TOKEN`, `GH_TOKEN`), jamais dans le dépôt ni dans un journal. Les machines de particuliers ne sont pas des tiers de confiance : préférer les offres en centre de données.

## 2. Instance

- 1 processeur graphique A100 80 Go (référence du devis) ou H100 80 Go.
- Version CUDA maximale affichée ≥ 13.0 : la roue figée de torch 2.14.1 vise CUDA 13.0. Sinon, voir `requirements-gpu.txt`.
- Au moins 32 Go de mémoire vive et 80 Go de disque.
- Image avec Python 3.11. Les bibliothèques CUDA viennent de la roue de torch ; l'hôte fournit le pilote.
- Durée attendue : 1 à 2 heures en tout (téléchargement du modèle, tests, run A, run B). Plafond : 6 heures, celles du devis.

## 3. Mise en place sur l'instance

Le script `scripts/validation_t04_instance.sh` enchaîne les sections 3 et 4 :
- mise en place et tests ;
- résolution de la révision ;
- run A, puis run B ;
- commits et poussée sur la branche `calcul/t04-validation` ;
- en cas d'arrêt, commit de ce qui existe, puis poussée.

Commande unique : `COMMIT=<commit de scellement> bash validation_t04_instance.sh`, avec `HF_TOKEN` et `GH_TOKEN` dans l'environnement de l'instance. Il peut aussi servir de script de démarrage de l'instance.

Il a été éprouvé ici en mode `jouet` (`MODE=jouet`, sans processeur graphique ni modèle réel), contre une copie nue du dépôt :
- cas sain : 155 tests, runs A et B, comparaison identique, poussée ;
- cas d'échec : run A impossible ; arrêt consigné, branche poussée, code de sortie 1 ;
- dossier de travail déjà présent : refus (R12).

Les commandes équivalentes, pas à pas :

```
nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv
git clone https://x-access-token:${GH_TOKEN}@github.com/lciric/controle-ia.git && cd controle-ia
git checkout <commit de scellement du préenregistrement>
git checkout -b calcul/t04-validation
python3.11 -m venv .venv && . .venv/bin/activate && pip install -r requirements-gpu.txt
python -c "import torch; print(torch.__version__, torch.version.cuda, torch.cuda.is_available())"
PYTHONPATH=src python -m pytest -q          # tout doit passer ; sinon arrêt et compte rendu
R=$(python -c "from huggingface_hub import HfApi; print(HfApi().model_info('meta-llama/Llama-3.1-8B-Instruct').sha)")
echo "$R"                                     # révision figée du programme, à consigner
```

## 4. Runs

```
PYTHONPATH=src python -m controle_ia.harnais.validation_reelle --revision "$R" \
    --prereg prereg/T0.4-validation-modele-reel-v1.md 2>&1 | tee run-A.log
A=<identifiant du run A, affiché en fin de run>
git add runs/$A diag/$A && git commit -m "T0.4 — validation réelle, run A ($A)"

PYTHONPATH=src python -m controle_ia.harnais.validation_reelle --revision "$R" \
    --prereg prereg/T0.4-validation-modele-reel-v1.md --rejeu-de "$A" 2>&1 | tee run-B.log
B=<identifiant du run B>
git add runs/$B diag/$B && git commit -m "T0.4 — validation réelle, run B ($B), rejeu entre processus"
git push origin calcul/t04-validation
```

- Le run B rejoue tout à la même entropie. Il écrit la comparaison scellée `diag/<B>/comparaison-<A>.json`.
- Les gros tableaux restent sur le disque de l'instance, sous `donnees/<run>/`, scellés sur place. Leurs empreintes sont dans `diag/<run>/resume.json`.
- Les copier ailleurs avant de détruire l'instance seulement si une décision le demande. La validation n'en a pas besoin.

## 5. Arrêts

- Tout « ARRÊT » (garde du code, panne, limite de 3 heures par processus) laisse `diag/<run>/arret.json` scellé. Le committer et le pousser, puis arrêter l'instance et me transmettre le motif.
- Aucun relancement avec un paramètre changé : il faudrait une nouvelle version du préenregistrement. Après une panne d'infrastructure (réseau, instance perdue), un seul relancement à l'identique est permis ; il se consigne.
- Fin de session : arrêter l'instance **par son identifiant** (`vastai stop instance <ID>`, R10). Aucun arrêt par motif de ligne de commande.

## 6. Après les runs (de mon côté)

1. Fusionner la branche `calcul/t04-validation` dans `main` ; vérifier les empreintes (`verifier-arbre`).
2. Registres :
   - `registres/depenses.md` : heures × prix ;
   - `registres/arrets.md` : identifiant d'instance, heure ;
   - `registres/decisions.md` : révision R figée ;
   - `registres/etat.md`.
3. Verdict sur le critère 1 de la porte G0, prononcé par un sous-agent neuf contre la lecture gelée du préenregistrement (R13), scellé, puis soumis à Lazar.
