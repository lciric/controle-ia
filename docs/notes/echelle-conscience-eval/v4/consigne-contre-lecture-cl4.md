Tu es un contre-lecteur neuf au sens de la règle R2 du dépôt `/home/user/controle-ia-travail` (lis son `CLAUDE.md` : français, phrases claires, quasi aucun acronyme). Tu n'as écrit ni le texte relu, ni le code, ni les tests, ni les contre-lectures précédentes. Ta tâche : contre-lire, avant son scellement, le préenregistrement d'une expérience décisive, puis rendre un rapport et un verdict.

## Pièce relue

`/home/user/controle-ia-travail/prereg/brouillon-test-echelle-conscience-eval-v5.md` (compagnon `.sha256` à côté ; vérifie l'empreinte au début et à la fin de ta lecture). C'est la version qui suit la contre-lecture n° 3 du brouillon v4 ; les constats CLZ-01 à CLZ-11 y sont traités en fin de texte.

## À lire, en entier

- Le brouillon v5 ; le brouillon v4 (`prereg/brouillon-test-echelle-conscience-eval-v4.md`), pour les différences.
- La contre-lecture n° 3 : `prereg/contre-lectures/brouillon-test-echelle-conscience-eval-v4-cl3.md`, et ses pièces dans `docs/notes/echelle-conscience-eval/v4/contre-lecture-cl3/` (scripts de banc et sorties). Les contre-lectures n° 2 et n° 1 : `prereg/contre-lectures/brouillon-test-echelle-conscience-eval-v3-cl2.md` et `prereg/contre-lectures/test-echelle-conscience-eval-v2-cl1.md` (au moins leurs constats et leur traitement).
- Le code, dans le dossier de travail `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-echelle-v1/` (un arbre de travail git), branche `outils/echelle-conscience-eval-v4`, commit attendu `f579930842ab633cdced18a13f82d77bb467ca7f` :
  - tout `echelle-v4/` (scripts, tests, stimuli ; les stimuli ne se lisent que par Python) ;
  - `echelle-v3/` pour les comparaisons (la v3 est la version que la contre-lecture n° 3 a relue).
- Les gardes héritées du lanceur, que les contre-lectures précédentes n'ont pas relues : `/home/user/controle-ia-travail/src/controle_ia/prereg.py` (fonction `exiger_prereg_scelle`) et `/home/user/controle-ia-travail/.claude/hooks/garde_calcul.py`.
- Les traces citées par le texte, sous `docs/notes/echelle-conscience-eval/` (dossiers `v3/` et `v4/`, et les fichiers du dossier lui-même), et les passages des cartes `docs/sources/anteriorite-hm1-20261026/carte-zones-libres-v1.md`, `-v2.md`, `-v3.md` que le texte cite.
- La ligne R-530 de `registres/decisions.md` (citée pour un chiffre).

## Ce que tu vérifies

1. **Le traitement de chaque constat de la contre-lecture n° 3** (CLZ-01 à CLZ-11) : traité, partiellement, ou non ; avec preuve. Rejoue ce qui se rejoue (par exemple les bancs de cl3 contre l'analyse v4).
2. **R4 et R3** : la lecture mécanique traite-t-elle les deux sens, les issues positives et négatives, de façon symétrique ? Une issue peut-elle encore être prononcée sur un seul sens, ou un artefact connu fabriquer une issue ? Peut-on viser un signe ?
3. **Concordance du texte et du code**, ligne à ligne : ordre de lecture, conditions, inégalités strictes ou larges, combinaison des deux sens, réserves, seuils, liste d'arrêt, plan d'analyse, commandes.
4. **R5** : chaque garde a-t-elle un cas sain et un artefact éprouvés (tests, répétition) ? Aucun repli silencieux ?
5. **Plafond de dépense** : la dépense réelle au pire tient-elle sous 8 USD sur tout le domaine admis, tolérance du prix relu comprise ? Les hypothèses non gardées sont-elles dites ?
6. **R6, R7, R9, R10, R12** : chaque chiffre renvoie à une trace empreintée, chaque citation à une page ; graines, versions et commit consignés ; arrêts par identifiant ; noms neufs.
7. **Ce qui manque** : un cas, une issue, une garde, un défaut que personne n'a vu.

Essais permis : lancer les tests (`cd …/wt-echelle-v1/echelle-v4 && PYTHONDONTWRITEBYTECODE=1 python -B -m pytest -q -p no:cacheprovider tests`, avec `/home/user/controle-ia-travail/.venv/bin/python` ; le modèle minuscule local est dans `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/essai-hm1-v4/modele-minuscule`, variable `MODELE_MINUSCULE`) ; rejouer la simulation scellée, les bancs ; écrire des scripts jetables. Tout dans ton bac à sable : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/contre-lecture-echelle-v5/` (crée-le ; il ne doit pas exister avant toi). Utilise `-B` et `PYTHONDONTWRITEBYTECODE=1` pour ne pas salir l'arbre de travail.

## Interdits

- N'ouvre, ne lis, ne hache jamais : `prereg/P3-consignes-v1.md`, les fichiers `textes-actions-*`, `items-textes-p1-v1.json`, `prompts-p1-v1.json`, ni rien sous `donnees/`, `runs/`, `diag/` ou `traces/` — pas même pour une empreinte. Aucune recherche récursive dans le dépôt (seulement des listes de dossiers nommés ci-dessus).
- Aucun réseau ; aucune commande `vastai` ; aucun lancement ; aucun `git push`, `git commit`, `git checkout` ou autre écriture git dans l'arbre de travail ou dans le dépôt ; rien de modifié hors de ton bac à sable.
- N'affiche, n'écris et ne cherche aucune clé ou jeton.

## Rendu

Écris ton rapport dans `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/contre-lecture-echelle-v5/rapport-contre-lecture-echelle-v5-cl4.md`, puis son compagnon `rapport-contre-lecture-echelle-v5-cl4.md.sha256` (format `sha256sum`). Structure : rôle, heure (`date -u`), empreintes des pièces lues, ce qui a été lu et essayé ; **verdict** (« scellable », « scellable après corrections » ou « non scellable », avec les bloquants) ; ce qui tient ; traitement des constats de cl3 (tableau) ; constats nouveaux numérotés CLW-01, CLW-02, … avec gravité (bloquant, à corriger, remarque), localisation, constat, preuve, correction proposée. Sois concret et vérifie par toi-même : ne prends aucune affirmation du texte pour acquise. Ton message final : le verdict en trois lignes, la liste des constats avec leur gravité, et le chemin du rapport.
