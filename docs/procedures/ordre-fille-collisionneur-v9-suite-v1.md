# Ordre à la fille — suite du tour v9 du collisionneur (GO-2026-11-02-31, option (b)) — v1

Écrit par session-depot le 3 novembre 2026 à 07:20 UTC (heure relevée par `date -u` à 07:20:10). Destinataire : la fille
`session_01XJ6Mgq5AWikCJZKnsMkbRZ`. Origine : mot de Lazar « kimi rechargé » (R-1101), en réponse à l'option (b) du 2 novembre
(« recharge Kimi puis reprise telle quelle une fois », addendum 3 de la passation `2026-11-02-2006`) ; solde Moonshot vérifié à
19,86 USD (R-1101). GO-2026-11-02-31 (plafond exactement 40 USD, échéance 16 novembre) : le dossier du run compte déjà 20,84 USD.

## 1. But
Jouer **exactement les deux cellules manquantes** du tour arrêté le 2 novembre à 20:34:53 UTC (code 5, Moonshot sans crédit) :
`E3-T3-reponse-D` (Kimi, `kimi-k3.1-pro`, essai 2 ; l'essai 1 est consigné ECHEC) et `E3-T3-reponse-E` (Astra, `gpt-6-astra`, essai 1),
en reprenant le même run `run-brainstorm-e3-v1`, sur une **copie** du dossier scellé tel quel (branche
`donnees/collisionneur-v9-brainstorm-v1`, commit `ac25c055`). Attendu ≈ 1,5 à 2 USD (D ≈ 0,4 à 0,8 ; E ≈ 1,1, pire 2,92).

## 2. Interdits propres à cette suite
- **Aucun appel à Argon** (C) : A1-v3 tient Argon jusqu'à sa fin. **Aucun appel à Claude** (A, B) : rien à jouer pour eux.
  Deux barrages : (a) avant la suite, `collisionneur_v9.py verifier` sur la copie doit montrer **13 cellules valides** et, comme
  seules non valides, `E3-T3-reponse-D` et `E3-T3-reponse-E` ; sinon refus, rien n'est lancé ; (b) dans l'environnement du
  collisionneur, `GEMINI_API_KEY` et `ANTHROPIC_API_KEY` reçoivent une valeur factice (par exemple `INTERDIT-SUITE-V1`), jamais la
  vraie clé : un appel imprévu à C, A ou B échoue sans dépense ni quota.
- Aucun fichier existant n'est écrasé (R12) ; le dossier scellé de `ac25c055` reste intact sur sa branche.
- Jamais de clé affichée, écrite ou passée en argument ; sortie scellée avant toute lecture ; arrêts par PID (R10).

## 3. Ce que tu écris (routine, sans appel), puis tu éprouves
1. Copie à l'octet de `donnees/collisionneur-v9-brainstorm-v1/` (à `ac25c055`) vers un dossier neuf de ton clone,
   `donnees/collisionneur-v9-brainstorm-v1-suite/` ; tous les compagnons `.sha256` de la copie vérifiés (`sha256sum -c`) avant tout.
2. `appel_controle_v11.py` : copie de `appel_controle_v10.py` (`a451f910…`) dont seul change le jeu d'espèces contrôlées : **D et E
   seulement**, lettres passées en argument et vérifiées comme sous-ensemble de `LETTRES` ; un appel par espèce, 1 024 jetons au plus.
3. `lancer-tour-brainstorm-v9-v1-suite.sh` : copie de `lancer-tour-brainstorm-v9-v1.sh` (`9edaeb26`) dont seuls changent :
   le run doit **exister** (refus s'il manque) ; Python du collisionneur lu dans `PY_COLLISIONNEUR` (exigé, avec `anthropic`) ;
   contrôle v11 vers `controle-brainstorm-v1-suite.json` (refus s'il existe) ; journaux du relais Kimi au suffixe `-suite-v1`
   (`--plafond-usd 3`, `--max-appels 4`, autres réglages inchangés) ; barrage (a) avant le contrôle ; barrage (b) dans `ENVI` ;
   **avant la suite** : empreintes de `run-brainstorm-e3-v1/journal.jsonl` et `run-brainstorm-e3-v1/etat.md` écrites dans
   `avant-suite-v1.txt` (scellé), puis retrait de **leurs deux seuls** compagnons `.sha256` (le collisionneur ajoute au journal et
   régénère l'état) ; même commande `etage3 --sortie run-brainstorm-e3-v1 --faits faits.md --question question.md --plafond-usd 40`
   (`PLAFOND_USD=40`, le plafond vaut pour tout le dossier : 20,84 déjà comptés) ; recherche des clés dans les sorties comme la v1.
4. Épreuves sans appel (R5, cas sain et artefact) : refus sans `GO_ID` ; refus si le run manque ; refus si un compagnon de la copie
   ne tient pas ; **refus si le barrage (a) voit une cellule à jouer hors de D et E du tour E3-T3** (artefact : copie d'essai où une
   cellule C est retirée) ; refus du contrôle v11 pour une lettre hors de D et E.

## 4. Avant le lancement : envoie-moi (sans attendre autre chose)
Empreintes de `appel_controle_v11.py`, du lanceur de suite et de `avant-suite-v1.txt` (après sa création au lancement, pas avant),
résultat des épreuves, commande exacte que tu lanceras. **Attends mon « lance »** : je réponds dans le quart d'heure.

## 5. Après la suite
Sceller avant toute lecture : nouveaux fichiers, `journal.jsonl` et `etat.md` (compagnons neufs), journaux de la suite, et
`EMPREINTES-tour-brainstorm-v9-v1-suite.txt` (scellé) ; `collisionneur_v9.py verifier` (attendu : 15 cellules valides, « tout
tient ») ; verser sur une branche de données neuve `donnees/collisionneur-v9-brainstorm-v1-suite` partie de `ac25c055` ; rapport
scellé : commit, empreintes, code de sortie, dépense par espèce (D, E, contrôle), heures `date -u`. Rien d'autre sur Argon tant
qu'A1-v3 vit.
