# Tokeniseur factice (lancement d'essai L4, 5 novembre 2026)

Tokeniseur BPE au niveau des octets, vocabulaire 3000, appris de façon déterministe (bibliothèque `tokenizers`
0.23.2) sur les 180 réponses des remises r00 à r05 et les 32 énoncés de la projection, par un script de la
session L4. **Ce n'est pas le tokeniseur de Llama-3.1-8B-Instruct** (empreinte attendue `79e3e522…`, absente du
dépôt, modèle à accès restreint, aucun téléchargement) : les jeux vérifiés avec lui ne sont pas scellables
(écart écrit au journal par `--empreinte-tokeniseur`). Le `tokenizer.json` factice de
`docs/notes/lentilles-sondes-p3-v1/…/essai-factice-v2/entrees/modele/` (`b52136fb…`) ne se charge pas avec
tokenizers 0.23.2 (« missing field `single_word` »), d'où ce remplacement.

sha256 : `cfc0c1439f9725cb5b8c6881077fe3140c3d9ca621d5876ccddf491fd503b1b8`
