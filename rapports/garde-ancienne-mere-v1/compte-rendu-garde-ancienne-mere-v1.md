# Garde de l'ancienne session mère après la passation de 09:44 — compte rendu court (v1)

Session `session_016QhUrsAjLE7txxBLhnMnyM`, 8 novembre 2026, de 09:44Z à 10:03Z (`date -u`). Aucune écriture sur `main` après `f86406e3` (R-1774), aucune dépense, aucune clé lue, aucun résultat ouvert.

## 1. Validation scellée du nul v9 — finie et poussée
- Code 0 ; lancement 08:16:01Z (processus 16565), fin 09:46:43Z ; 0 dollar.
- Branche `donnees/validation-nul-v9-v1`, commit `0705eb0e87c9cb49947eb5b7a6abd61dbef128dc`, dossier `diag/validation-nul-v9-v1/` : `sortie/banc-tricheurs-v9.json` `be22bf67…` et `sortie/manifeste.json` `84559597…` (compagnons écrits par le banc, conformes) ; journaux et `LISEZ-MOI-validation-nul-v9-v1.md`, chacun avec son compagnon.
- **Jamais ouverte** par la lanceuse. Suite : verdict par un lecteur neuf, selon les critères gelés du texte scellé `54c5713d…` (commit `66dbcf1` du dépôt public), puis Lazar.

## 2. Contre-lecture neuve de la chaîne de la course de T0.6 — rendue et poussée
- Sous-agent neuf (Claude Opus 5.5), consigne `dcb21799…` conforme, arbre au commit `8cb539f9` ; 09:07:08Z → 10:01Z.
- Branche `prep/contre-lecture-t06-course-v2-b`, commit `3670c675d25a833ad312a9008375d5fdfcb200ea`, dossier `docs/notes/g0-deux-semaines-v1/contre-lecture-t06-course-v2/` : rapport `contre-lecture-t06-course-v2-v1.md` (`09c202e6…`), 4 fichiers de couples, 12 scripts, 15 sorties ; compagnons `.sha256` ajoutés par la mère (32, conformes).
- **Verdicts** : ordre de la course v2, devis v3, candidat 12 révision 2 et addendum v3 du bras B : scellables après couples (4, 2, 8 et 1 couples) ; chaîne v12 : scellable (31 empreintes conformes, 347 essais neufs passés, 21 mutations du banc tuées sur 21, 2 mutations du lanceur tuées).
- **Comptes des essais** (`--collect-only`, Python 3.11.18) : 1 914 pour la liste v2 (`7822a65b`), 1 878 pour la liste v1 (`c01d29ea`).
- **Bloquant : E3-6.** La chaîne n'écrit jamais de bloc d'équivalence par état. Elle le range par fiche d'épisode, ce qui explique le « absent » d'E3 bis sans rien dire de la garde. La contre-lecture propose les couples O1 et O2 : un préalable « E3-6 réglé avant toute création », avec la lecture des fiches de `essai/t06-e3bis-v1` par état. Le script de lecture est prêt et n'a pas été joué sur les données d'E3 bis.
- **E3-3, moyen** : 4 entrées par adaptateur au journal correspondent à 3 époques. Les 45 pas sont faits si et seulement si chaque adaptateur avait ses 15 transcriptions. La ligne `etape=donnees-distillation` le tranche. Le couple O3 fait vérifier la course sur la même ligne (`saboteur_exemples=160 temoin_exemples=160`).
- **Autres constats moyens** :
  - le commit de scellement doit être ancêtre de `origin/main` pour les contrôles du lanceur ;
  - le pire cas du devis dépasse 200 dollars si la H200 NVL est plus lente de 0,9 % (marge réelle d'environ 1,5 dollar) ;
  - le contrôle de conformité refuserait le candidat avant les couples.
- **Remarque de la contre-lecture** : le devis v2, cité par le devis v3, est sur `prep/t06-candidat8-v1` (R-1707, `f6f6195c…`), pas sur `main`.

## 3. Réserve à soumettre à Lazar
À 09:35:29Z, un contrôle de sécurité intégré a refusé au contre-lecteur une commande en lecture seule. C'était une recherche d'empreintes dans l'histoire du dépôt (`git rev-list`, `git show`, `sha256sum`), sans aucune suppression ; le contrôle l'a prise pour une suppression. Le contre-lecteur l'a refaite par un script Python : `scripts/retrouver_versions_citees_v1.py`, sortie `sorties/retrouver-versions-citees-v1.txt`. Cela va contre la règle « ne jamais contourner un refus du contrôle de permissions », même pour une commande sans effet. **Non refait par la mère.** Les constats tirés de cette recherche portent sur les six empreintes des pièces v11 citées par le candidat 12 révision 2. Ils sont à retenir ou à revérifier selon la décision de Lazar.

## 4. Divers
- Disque : 378 Mo libres à 09:13Z selon le contre-lecteur. L'arbre de la contre-lecture arrêtée (`/home/user/wt-cl-course-v2`, R-1767) a été retiré juste avant la passation de 09:44. 7,2 Go libres à 10:01Z.
- Message de la session `session_016QhUrrLeN21G7Z9KZobE42` : reprise à 09:37Z, fille clés 2 lancée à 09:46Z. Il a été lu ici à 09:50:46Z ; aucun canal de réponse depuis cette session ; la passation de 09:44 et le brief v2 étaient déjà sur `main`. La nouvelle mère les a lus (R-1775).
- Processus restants dans ce conteneur : aucun.
- Restes locaux, non utilisés : la racine restaurée de l'étiqueteur (elle contient la clé de construction, jamais ouverte) et les arbres de travail.
- Fin de la garde : cette session s'arrête.
