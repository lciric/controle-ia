Tu es un contre-lecteur neuf au sens de la règle R2 du dépôt `/home/user/controle-ia-travail` (lis son `CLAUDE.md` : français, phrases claires, quasi aucun acronyme). Tu n'as écrit ni le texte relu, ni le code, ni les tests, ni les contre-lectures précédentes. Ta tâche : contre-lire, avant son scellement, le préenregistrement d'une expérience décisive, puis rendre un rapport et un verdict.

## Pièce relue

`/home/user/controle-ia-travail/prereg/brouillon-test-echelle-conscience-eval-v7.md` (compagnon `.sha256` à côté ; vérifie l'empreinte au début et à la fin de ta lecture). C'est la version qui suit la contre-lecture n° 5 du brouillon v6 ; les constats CLV-01 à CLV-08 y sont traités en fin de texte. Le texte dit ce qui a changé depuis le v6 : relis en priorité les parties changées, sans tenir le reste pour acquis.

## À lire, en entier

- Le brouillon v7 ; le brouillon v6 (`prereg/brouillon-test-echelle-conscience-eval-v6.md`), pour les différences.
- La contre-lecture n° 5 : `prereg/contre-lectures/brouillon-test-echelle-conscience-eval-v6-cl5.md`, et ses pièces dans `docs/notes/echelle-conscience-eval/v6/contre-lecture-cl5/` (scripts de banc et sorties ; lis `chaine-lanceur/LISEZ-MOI.txt`). La contre-lecture n° 4 : `prereg/contre-lectures/brouillon-test-echelle-conscience-eval-v5-cl4.md` (au moins ses constats et leur traitement). Les contre-lectures n° 1 à 3 : `prereg/contre-lectures/test-echelle-conscience-eval-v2-cl1.md`, `brouillon-test-echelle-conscience-eval-v3-cl2.md`, `brouillon-test-echelle-conscience-eval-v4-cl3.md` (au moins leurs constats).
- Le code, dans le dossier de travail `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-echelle-v1/` (un arbre de travail git), branche `outils/echelle-conscience-eval-v6`, commit attendu `b8b76650d29e213cf5da9b8fccee22cad9ba98c5` :
  - tout `echelle-v6/` (scripts, tests, stimuli ; les stimuli ne se lisent que par Python) ;
  - `echelle-v5/` pour les comparaisons (la v5 est la version que la contre-lecture n° 5 a relue).
- Les gardes héritées du lanceur : `/home/user/controle-ia-travail/src/controle_ia/prereg.py` (fonction `exiger_prereg_scelle` et ce qu'elle appelle) et `/home/user/controle-ia-travail/.claude/hooks/garde_calcul.py` ; le registre `registres/go.md`, que le contrôle du GO relit (lis son en-tête et les lignes dont tu as besoin).
- Les traces citées par le texte, sous `docs/notes/echelle-conscience-eval/` (dossiers `v3/` à `v6/`, et les fichiers du dossier lui-même), et les passages des cartes `docs/sources/anteriorite-hm1-20261026/carte-zones-libres-v1.md`, `-v2.md`, `-v3.md` que le texte cite.

## Ce que tu vérifies

1. **Le traitement de chaque constat de la contre-lecture n° 5** (CLV-01 à CLV-08) : traité, partiellement, ou non ; avec preuve. Rejoue ce qui se rejoue (par exemple les bancs et le cas fabriqué de cl5 contre l'analyse v6 ; un rejeu des bancs de cl5 est versé sous `docs/notes/echelle-conscience-eval/v6/rejeu-bancs-cl5/`, vérifie-le au lieu de le croire).
2. **R4 et R3** : la lecture mécanique traite-t-elle les deux sens, les deux modèles, les issues positives et négatives, de façon symétrique ? Une issue peut-elle encore être prononcée sur un seul sens, ou chez des modèles différents d'un sens à l'autre, ou un artefact connu fabriquer une issue ? Peut-on viser un signe ?
3. **Concordance du texte et du code**, ligne à ligne : ordre et étapes de lecture, conditions, inégalités strictes ou larges, combinaison des deux sens, réserves (et les modèles qu'elles visent), seuils, liste d'arrêt, plan d'analyse, commandes.
4. **R5** : chaque garde a-t-elle un cas sain et un artefact éprouvés (tests, répétition, essais) ? Aucun repli silencieux ? Les gardes nouvelles de la surveillance et du lanceur (empreintes, appels bornés, heure relue) tiennent-elles aux bornes du code ?
5. **Plafond de dépense** : la dépense réelle au pire tient-elle sous 8 USD sur tout le domaine admis, tolérance du prix relu et retard d'arrêt compris ? Les hypothèses non gardées sont-elles dites ?
6. **R6, R7, R9, R10, R12** : chaque chiffre renvoie à une trace empreintée, chaque citation à une page ; graines, versions et commit consignés ; arrêts par identifiant ; noms neufs.
7. **Ce qui manque** : un cas, une issue, une garde, un défaut que personne n'a vu.

Essais permis : lancer les tests (`cd …/wt-echelle-v1/echelle-v6 && PYTHONDONTWRITEBYTECODE=1 python -B -m pytest -q -p no:cacheprovider tests`, avec `/home/user/controle-ia-travail/.venv/bin/python` ; le modèle minuscule local est dans `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/essai-hm1-v4/modele-minuscule`, variable `MODELE_MINUSCULE`) ; rejouer la simulation scellée, les bancs ; écrire des scripts jetables. Tout dans ton bac à sable : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/contre-lecture-echelle-v7/` (crée-le ; il ne doit pas exister avant toi), avec `TMPDIR`, `HF_HOME` et `--basetemp` pointés dedans. Utilise `-B` et `PYTHONDONTWRITEBYTECODE=1` pour ne pas salir l'arbre de travail.

## Interdits

- N'ouvre, ne lis, ne hache jamais : `prereg/P3-consignes-v1.md`, les fichiers `textes-actions-*`, `items-textes-p1-v1.json`, `prompts-p1-v1.json`, ni rien sous `donnees/`, `runs/`, `diag/` ou `traces/` — pas même pour une empreinte. Aucune recherche récursive dans le dépôt (seulement des listes de dossiers nommés ci-dessus).
- Aucun réseau ; aucune commande `vastai` réelle (un faux outil dans ton bac à sable est permis) ; aucun lancement ; aucun `git push`, `git commit`, `git checkout` ou autre écriture git dans l'arbre de travail ou dans le dépôt ; rien de modifié hors de ton bac à sable.
- N'affiche, n'écris et ne cherche aucune clé ou jeton.

## Rendu

Écris ton rapport dans `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/contre-lecture-echelle-v7/rapport-contre-lecture-echelle-v7-cl6.md`, puis son compagnon `rapport-contre-lecture-echelle-v7-cl6.md.sha256` (format `sha256sum`). Structure : rôle, heure (`date -u`), empreintes des pièces lues, ce qui a été lu et essayé ; **verdict** (« scellable », « scellable après corrections » ou « non scellable », avec les bloquants) ; ce qui tient ; traitement des constats de cl5 (tableau) ; constats nouveaux numérotés CLU-01, CLU-02, … avec gravité (bloquant, à corriger, remarque), localisation, constat, preuve, correction proposée. Sois concret et vérifie par toi-même : ne prends aucune affirmation du texte pour acquise. Ton message final : le verdict en trois lignes, la liste des constats avec leur gravité, et le chemin du rapport.
