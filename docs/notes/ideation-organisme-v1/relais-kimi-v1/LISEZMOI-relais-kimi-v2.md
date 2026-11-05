# Relais Kimi v2 et essai d'un appel — LISEZMOI

Lignée session-depot (instance 2), 30 octobre 2026. Ce dossier complète la v1 (`LISEZMOI-relais-kimi-v1.md`), qui reste valable et n'est pas modifiée (R12).

## Fichiers
- `relais_kimi_v2.py` : la v1, plus l'option `--lister-modeles`. Le relais lit la clé dans la variable, fait **un seul** `GET /v1/models` en amont, imprime les identifiants de modèles (triés, un par ligne), puis sort sans servir. La clé n'est jamais imprimée. Codes de sortie : 0 si la liste est lue, 3 si l'amont répond mal (le corps n'est pas recopié), 2 pour un réglage invalide ou une clé absente. En mode service, les réglages de la v1 restent obligatoires.
- `test_relais_kimi_v2.py` : tous les essais de la v1 rejoués sur la v2, plus ceux de `--lister-modeles`.
- `essai_kimi_v1.sh` : un appel minimal à Kimi par le relais v2 (demande (c) du n° 245 de conv-audit). Son en-tête détaille les étapes et les codes de sortie.
- `faux_amont_kimi_v1.py` : le faux amont local de la variante à blanc.

## Essais (aucun réseau sortant, aucune vraie clé)
Depuis la racine du dépôt :
```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest -q -p no:cacheprovider docs/notes/ideation-organisme-v1/relais-kimi-v1/test_relais_kimi_v2.py
```
```bash
ESSAI_A_BLANC=1 bash docs/notes/ideation-organisme-v1/relais-kimi-v1/essai_kimi_v1.sh kimi-k3.1-pro <dossier-neuf>
```
Avec `MODELE_SERVI_A_BLANC=kimi-k2.5`, le faux amont sert un autre modèle : le relais rend 502 et le script sort en code 7.

## Mode réel
À lancer seulement dans une session neuve, où `KIMI_API_KEY` est posée dans les réglages de l'environnement (R-814), et sous une ligne de GO :
```bash
GO_ID=GO-AAAA-MM-JJ-NN bash docs/notes/ideation-organisme-v1/relais-kimi-v1/essai_kimi_v1.sh <identifiant-exact> <dossier-neuf>
```
Le script imprime une seule ligne : le statut, le modèle demandé, le modèle servi, le coût lu dans `/relais/etat` et le compte de refus de modèle. Le relais est plafonné à 0,5 USD et à un appel.
