# Consigne de la mère — code du plancher v3 de T0.7 (remède (a') : règle (a) + 800 directions), v1

Décisions qui fondent ce travail : R-2285 (mot de Lazar, (a')), R-2298 (dimensionnement). Note v3 de l'analyste :
`docs/notes/g0-deux-semaines-v1/t07-module-v2/erreur-premiere-espece-lectures-decisives-t07-v3.md` (`760a562c…`), à lire en
entier (sections coût et sondes figées de P3). Notes v1 (`8e996ab0…`) et v2 (`5ccf0940…`) au même dossier.

## Base
- Branche `prep/t07-plancher-v2-v1` (`adb5f415…` : `plancher_v2.py`, `lecture_v3.py`, `lectures_t07_v2.py` et deux essais).
  Travaille sur une branche **neuve** `prep/t07-plancher-v3-v1` partie de `adb5f415`, dans un arbre à toi (worktree clairsemé :
  `/src/`, `/tests/`, `/scripts/`, plus les fichiers de racine). **Jamais de fusion dans `main`** : `main` garde `tests/`
  `79230a58…` et `src/` `744a9e16…` jusqu'au scellement de T0.7 (règle C7, R-2231).
- Configuration v6 : `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v2-pieces-v1/configuration-t07-v6.json`
  (`475669de…`). Texte : `brouillons/T0.7-sondes-v0-v1-candidat1.md` (`1718f2a0…`), sections « Plan d'analyse » (plancher,
  l. 1078-1100), ligne 381 (planchers de P3), « Calcul et dépense ». Ordre d'exécution :
  `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon5.md` (`d0b75d16…`).
- Code existant : `src/controle_ia/t07/plancher_v1.py` (`plancher_pour_sonde`, `scores_plancher`), `lecture_v1.py`
  (l. 534-575 et 683-705 : planchers de P3 réutilisés, `N_PLANCHER_REEL`), `lecture_v2.py`, `src/controle_ia/sondes/evaluation.py`
  (`plancher_apparie`, gelé), `figees` (sondes figées de P3).

## À faire (fichiers neufs, R12 ; aucun fichier existant modifié sauf nécessité déclarée)
1. **`n_plancher` = 800 en mode réel** : la constante et la garde de mode réel passent à 800 dans des modules neufs (ne pas
   modifier `lecture_v1.py`/`lecture_v2.py` : versions neuves si leurs gardes l'exigent). Configuration **v7** (fichier neuf,
   à côté de la v6) : seul `n_plancher` change, plus les clés neuves nécessaires ; empreinte canonique rapportée.
2. **Notation vectorisée du plancher** : fonction neuve qui note les 800 directions sur toutes les actions en un produit
   matriciel par lot (même agrégation que `noter_actions` : maximum ou attention selon la sonde), **éprouvée égale** à
   `scores_plancher` (au bit près si possible, sinon ≤ 10⁻¹², écart déclaré) sur le jouet et sur des tirages aléatoires,
   agrégations comprises ; mémoire bornée (lots). Aucune moyenne ni médiane sur les jetons.
3. **Sondes figées de P3, plancher neuf** : à l'étape A, sur l'instance, réextraire les jetons d'entraînement des sondes figées
   de P3 à la couche 15 (même harnais, même découpage, mêmes textes que P3 : retrouve dans le dépôt le code et les données
   d'entraînement de P3, étapes 1 à 4 ; cite chemins et empreintes) ; **garde d'identité** : les sondes refaites sur ces
   activations, par la recette de P3, égalent les poids figés (`sondes-figees-legeres.npz`, `701f73bd…`) à une tolérance
   **fixée d'avance** et justifiée (non-déterminisme de la carte compris) ; seconde garde si la graine des planchers de P3 se
   lit dans son manifeste (les 200 directions de P3 redonnées) ; puis 800 directions neuves par `plancher_apparie`, graine
   dérivée de l'entropie de T0.7 (`SeedSequence`, clé `plancher/<sonde>`), notées par la fonction du point 2 ; les 200 de P3
   gardées et notées en lecture descriptive. **Repli** si une garde échoue : arrêt écrit de ce seul bras, motif au manifeste,
   aucune bascule silencieuse vers les 200 (R5) ; le statut des lectures touchées est au texte (rédacteur du candidat 2),
   propose-le dans ton rapport.
4. **Essais R5** : chaque garde neuve a un cas sain et un artefact ; essais de mutation sur copies seulement, avec
   `-o pythonpath=` et l'import tracé (`pyproject.toml` met `src` d'abord, R-2246). Toute la suite de l'arbre passe.
5. **Coût** : estime le temps ajouté à l'étape A sur A100 (réextraction, notation des 800 directions par sonde, toutes sondes) à
   partir de mesures sur processeur et des relevés de P3 ; devis en USD au tarif A100 du devis de l'étape A (GO-2026-11-10-04 :
   A100 ≤ 7,6 USD au pire) ; dis si le total tient sous 20 USD.

## Interdits
- Jamais `diag/*/lecture-sondes-t06.json`, la lecture B de 7a, `donnees/lecture-b-7a-quarantaine-v1`,
  `donnees/mesure-unanime-v15-sortie-v1`, `essai/t06-explo-v3`, aucun `diag/` ni `runs/` de 7a ou 7b ; jamais
  `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, `registres/index-bras-attaque*`,
  `anteriorite-bras-informe*`, la branche `claude/compassionate-meitner-d4ryyk` ; jamais l'étiqueteur ni
  `scripts/extraire_mesures_epreuve_t06_v1.py` ; rien de P3-bis. Les données de P3 (`diag/20261019-230011-p3-reel/` et ses
  pièces) sont permises.
- Aucune recherche récursive sur la racine sans exclure ces chemins. Jamais `env`, `printenv`, `set` sans argument,
  `export -p`, `/proc/*/environ`, ni une valeur de clé. Aucune dépense, aucune instance, aucun appel de modèle. Pas de
  `git fetch` sans refspec. Aucun `rm -rf`. Un refus de permission ou de classifieur ne se contourne pas : il se rapporte.
- Garde des secrets à 0 avant chaque commit (motif de la mère, chaîné par `&&`) ; poussée de ta seule branche.

## Livrables
- Commit(s) sur `prep/t07-plancher-v3-v1`, poussés (`git push origin HEAD:prep/t07-plancher-v3-v1`, retentatives 2, 4, 8, 16 s).
- Rapport scellé (non committé) : `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/rapport-code-plancher-v3-v1.md`,
  avec configuration v7 et journal des essais scellés au même dossier.
- Réponse finale : commit, fichiers, essais (nombre, mutations), tolérance de la garde d'identité et sa justification,
  devis, repli proposé, réserves, ton modèle.
