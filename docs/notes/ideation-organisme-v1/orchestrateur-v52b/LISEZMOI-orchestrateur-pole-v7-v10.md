# Orchestrateur du pôle, version 0.7.0 — script du duel des proposeurs, pari en forme « parts » seule, coût simulé jamais compté — LISEZMOI v10

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Fable 5.1 pour cette version), v10 écrite à partir de 18:09 UTC
(heure lue sur `date -u`) ; v1 à v9 gardées telles quelles (R12). Deux contre-lectures croisées du code (Fable sur les
versions écrites sous Opus, Opus sur celles écrites sous Fable) sont **en cours** : leurs constats feront une version
suivante ; celle-ci n'ajoute que le script d'enchaînement du duel (devis `../demonstration-proposeurs-v7/devis-duel-proposeurs-v1.md`,
`7687bcc6…`) et deux corrections qu'il a révélées.

| changement | fichiers |
|---|---|
| **script d'enchaînement du duel** : génère les mondes (grammaire v2, structures « trois traits » et « seuil décalé », graines 20261201…), joue les quatre bras (M-expl, M-aveugle à modèle ; mécanique, aléatoire en références gratuites) sur les mêmes mondes, mêmes témoins, même juge ; lit L1 à L5 ; règle d'arrêt après `--arret-apres` mondes ; `--moteur simule` (sans dépense, bras « à modèle » joués par le proposeur scripté : répétition de la plomberie, pas le duel) ou `--moteur claude-sdk --url-relais` (dépense, chez session-depot, sous GO, `--roles-reels proposeur`) | `demonstrations/duel_proposeurs_v7.py` (nouveau) |
| **pari apparié borné en forme « parts » seule** (conception v2, `../pari-de-signe/conception-pari-de-signe-v2.md`, constat C1 de sa contre-lecture : la forme « signe » teste un autre nul et son mélange n'est pas une surmartingale sous E[v] ≤ 0) ; contraste hors de [−1 ; 1] refusé | `demonstrations/duel_proposeurs_v7.py` (`pari_apparie`) |
| **coût simulé jamais compté** : dans l'adaptateur mixte, un rôle simulé déclarait au pôle son coût simulé (`COUTS_SIMULES` : 0,40 USD par expérimentateur, 0,15 par vérificateur) ; sur un duel payé, le budget de la course se serait épuisé sur des dollars fictifs et le coût par structure (L5) aurait été faux. Désormais le rôle simulé déclare 0 ; le chiffre simulé est gardé à part (`Resultat.cout_simule_usd`) | `pole/adaptateurs.py` (`AdaptateurMixte.lancer`, `Resultat`) |
| essais : pari « parts » (contraste plein promu au septième instant ; banque figée 90/10 de moyenne nulle : jamais promue par la forme parts, toujours par l'ancienne forme signe gardée comme artefact ; bornes ; suite vide) ; coût simulé mis à zéro dans l'adaptateur mixte, coût réel transmis | `essais/test_v7_duel.py` (nouveau, 5), `essais/test_v7_proposeurs_references.py` (+1) |

**208 essais passent** (202 de la v9, 6 nouveaux).

## Lancer (depuis ce dossier)

```bash
PY=/opt/venv-essaim-sim-v1/bin/python
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v10.txt
$PY -I -B -m unittest                                                              # 208 essais, environ 3 minutes
$PY -I -B demonstrations/duel_proposeurs_v7.py DOSSIER_NEUF --mondes 2 --moteur simule --arret-apres 1   # 40 s, sans modèle ni clé
```

Répétition faite ici (2 mondes, moteur simulé) : course au bout, lecture L1 à L5 écrite, règle d'arrêt déclenchée après
1 monde (« M-expl n'a retrouvé aucune structure » — attendu : le proposeur scripté n'est pas un modèle). Les dépenses
affichées dans cette répétition sont les coûts simulés de l'adaptateur simulé pur (pas mixte) : fictifs, et dits tels.

## Limites connues

- Le duel lui-même (dépense) attend les deux contre-lectures croisées et le GO de Lazar sur le devis.
- Le motif « filtre `delta0` des filles appliqué après la règle e-BH » (signalé par la contre-lecture du pari de signe,
  constat C9) n'est **pas** corrigé ici : il attend la contre-lecture du code, qui doit le quantifier.
- Le reste : LISEZMOI v9.
