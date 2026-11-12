# Orchestrateur du pôle, version 0.7.0 — proposeur enfichable, références gratuites, mondes de la grammaire — LISEZMOI v7

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Opus 5.5 pour cette version), v7 écrite à partir de 16:15 UTC
(heure lue sur `date -u`) ; v1 à v6 gardées telles quelles (R12). Sur l'option 3, unanime, du tour du collisionneur
« proposeur enfichable » (synthèse `docs/notes/collisionneur-proposeur-enfichable-v1/synthese-proposeur-enfichable-v1.md`
sur `main`, `0a209c33…`) : rendre le rôle « proposeur » enfichable et battre deux références gratuites avant tout duel payé.

| changement | fichiers |
|---|---|
| **proposeur enfichable** : `ConfigGeneration.proposeur` ∈ {« agent », « aleatoire », « mecanique »}, `--proposeur` ; les références ne coûtent rien et n'appellent aucun modèle ; leurs propositions passent par la même porte du gabarit ; leurs stratégies (« aleatoire_au_gabarit », « mecanique_sur_developpement ») sont refusées à un agent ; propositions écrites dans `traces-proposeur/propositions-reference.json` | `pole/proposeurs_references.py` (nouveau), `pole/proposeur.py`, `pole/cycle.py`, `pole/pole.py` |
| **référence aléatoire** : lois tirées au hasard au gabarit (moniteur, un ou deux traits, poids gaussiens bornés) | idem |
| **référence mécanique** : par moniteur, par sous-ensemble d'au plus deux traits, trois formes (softmax, par sous-population, si/sinon sur le signe d'un trait) ajustées sur la partie de développement ; meilleures par vraisemblance pénalisée (Schwarz) ; exige la phase exploratoire | idem |
| **partie de développement distincte du calibrage** : une banque qui porte une partie « developpement » la sert au proposeur ; sinon la partie de calibrage, et `meme_partie_que_le_connu` le dit (point du collisionneur : témoins, nul informé et exploration ajustés sur les mêmes 40 épisodes) | `pole/monde_banque.py` |
| **mondes tirés au hasard dans une grammaire** (monotone, combinaison, interaction, sous-population, seuil ; témoins vrais = lois exactes ; parties calibrage, développement, épreuve) | `exemples/generer_monde_grammaire_v1.py` (nouveau) |
| **démonstration** : quatre bras (scripté aveugle, scripté avec exploration, aléatoire, mécanique) sur 20 mondes | `demonstrations/demo_proposeurs_v7.py` (nouveau) ; lecture `../demonstration-proposeurs-v7/lecture-demo-proposeurs-v7-v1.md` |
| essais : `essais/test_v7_proposeurs_references.py` (6 nouveaux) | |

**196 essais passent** (190 de la v6, 6 nouveaux).

Résultat de la démonstration (exploratoire) : moniteurs non linéaires retrouvés **23 sur 35** par le chercheur mécanique,
5 par le proposeur scripté avec exploration, 2 à l'aveugle, 1 par le hasard ; aucun témoin faux promu ; tous les témoins
vrais non linéaires promus. Réserve : la grammaire des mondes est l'espace de recherche du mécanique.

## Lancer (depuis ce dossier)

```bash
PY=/opt/venv-essaim-sim-v1/bin/python
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v7.txt
$PY -I -B -m unittest                                                       # 196 essais, environ 3 minutes
$PY -I -B demonstrations/demo_proposeurs_v7.py DOSSIER_NEUF --graines 20    # 12 minutes, sans modèle
$PY -I -B exemples/generer_monde_grammaire_v1.py GRAINE DOSSIER_NEUF         # un monde
```

## Limites connues

- Le proposeur « agent » de la démonstration est le proposeur scripté du pôle (mon code), pas un modèle : le duel avec
  Opus 5.5 ou un chercheur de la littérature reste à payer, sur devis, après des mondes hors de la grammaire du mécanique.
- La grammaire est écrite par moi (limite déclarée du confondant d'autorat) ; chaque monde en est un tirage.
- Le reste : LISEZMOI v6.
